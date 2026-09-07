import pymupdf, re, os
from collections import Counter

SMALL = 9.0      # 小字号 = 真上下标
BODY_MIN = 12    # 正文行最少字符
NEAR = 13.0      # 成分归属正文行的最大垂直距离

def page_spans(pg, exclude=None, pad=26, small=9.5):
    """提取 span；exclude 为插图区列表，落在其外扩范围内且字号偏小的 span
    判定为图中字母标注（如 a/b/c/d、g/h/i/O），予以剔除。"""
    out=[]
    for b in pg.get_text("dict")["blocks"]:
        if b["type"]!=0: continue
        for l in b["lines"]:
            for s in l["spans"]:
                if not s["text"].strip(): continue
                if exclude:
                    cx=(s["bbox"][0]+s["bbox"][2])/2
                    cy=(s["bbox"][1]+s["bbox"][3])/2
                    hit=False
                    for z in exclude:
                        if (z[0]-pad<=cx<=z[2]+pad and z[1]-pad<=cy<=z[3]+pad
                                and round(s["size"],1)<small):
                            hit=True; break
                    if hit: continue
                out.append({"t":s["text"],"size":round(s["size"],1),
                            "x0":s["bbox"][0],"x1":s["bbox"][2],
                            "y0":s["bbox"][1],"y1":s["bbox"][3],
                            "base":round(s["origin"][1],1)})
    out.sort(key=lambda s:(s["base"], s["x0"]))
    return out

def frac_bars(pg):
    """检测分数线：水平细线，且上下方均有文本"""
    bars=[]
    for dr in pg.get_drawings():
        r=dr["rect"]
        if r.width>3 and r.height<1.2 and r.width<80:
            bars.append({"x0":r.x0,"x1":r.x1,"y":(r.y0+r.y1)/2,"w":r.width})
    return bars

def assign_fracs(spans, bars):
    """用分数线把 span 标记为分子/分母，返回新的 span 列表（分式折叠为 LaTeX）"""
    used=set()
    fracs=[]
    for bar in bars:
        # 分子：线上方 4~13pt，x 区间重叠
        up=[s for s in spans if id(s) not in used and
            bar["y"]-13 < s["base"] < bar["y"]-3 and
            s["x1"]>bar["x0"]-2 and s["x0"]<bar["x1"]+2]
        dn=[s for s in spans if id(s) not in used and
            bar["y"]+3 < s["base"] < bar["y"]+13 and
            s["x1"]>bar["x0"]-2 and s["x0"]<bar["x1"]+2]
        if up and dn:
            n="".join(s["t"].strip() for s in sorted(up,key=lambda s:s["x0"]))
            d="".join(s["t"].strip() for s in sorted(dn,key=lambda s:s["x0"]))
            if n and d:
                for s in up+dn: used.add(id(s))
                fracs.append({"x0":min(s["x0"] for s in up+dn),
                              "x1":max(s["x1"] for s in up+dn),
                              "y":bar["y"],"text":f"$\\frac{{{n}}}{{{d}}}$","role":"frac"})
    remain=[s for s in spans if id(s) not in used]
    return remain, fracs

def group_by_base(spans, tol=2.5):
    groups=[]; cur=[]; cb=None
    for s in spans:
        if cb is None or abs(s["base"]-cb)<=tol:
            cur.append(s); cb = s["base"] if cb is None else cb
        else:
            if cur: groups.append((cb,cur))
            cur=[s]; cb=s["base"]
    if cur: groups.append((cb,cur))
    out=[]
    for base,grp in groups:
        grp.sort(key=lambda s:s["x0"])
        out.append({"base":base,"text":"".join(s["t"] for s in grp),
                    "size":Counter(s["size"] for s in grp).most_common(1)[0][0],
                    "n":len("".join(s["t"] for s in grp).strip()),
                    "x0":min(s["x0"] for s in grp),"x1":max(s["x1"] for s in grp)})
    return out

def page_lines(pg, exclude=None):
    spans=page_spans(pg, exclude=exclude)
    spans,fracs=assign_fracs(spans, frac_bars(pg))
    groups=group_by_base(spans)
    body=[g for g in groups if g["n"]>=BODY_MIN]
    frag=[g for g in groups if g not in body]
    lines=[{"y":b["base"],"text":b["text"],"x0":b["x0"],"x1":b["x1"],"frags":[]} for b in body]
    for f in frag:
        if not lines: continue
        tgt=min(lines,key=lambda L:abs(L["y"]-f["base"]))
        if abs(tgt["y"]-f["base"])<=NEAR: tgt["frags"].append(f)
    for fr in fracs:
        if not lines: continue
        tgt=min(lines,key=lambda L:abs(L["y"]-fr["y"]))
        if abs(tgt["y"]-fr["y"])<=NEAR: tgt["frags"].append(fr)
    lines.sort(key=lambda L:L["y"])
    for L in lines:
        items=[{"x0":L["x0"],"text":L["text"],"role":"body"}]
        for f in L["frags"]:
            if f.get("role")=="frac": items.append({"x0":f["x0"],"text":f["text"],"role":"frac"})
            else:
                off=f["base"]-L["y"]
                if f["size"]<SMALL: role="sup" if off<-1.5 else "sub"
                else: role="body"
                items.append({"x0":f["x0"],"text":f["text"],"role":role})
        items.sort(key=lambda it:it["x0"])
        buf=""
        for it in items:
            if it["role"]=="sup": buf+=f"$^{{{it['text'].strip()}}}$"
            elif it["role"]=="sub": buf+=f"$_{{{it['text'].strip()}}}$"
            else: buf+=it["text"]
        L["text"]=re.sub(r"\s+"," ",buf).strip()
    return lines
