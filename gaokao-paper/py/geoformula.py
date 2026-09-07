# -*- coding: utf-8 -*-
"""基于几何坐标重建行内公式（根号 / 分式）。

PDF 中分式被拆成「分子行 + 分数线 + 分母行」，内容流顺序错乱，
但几何坐标完整。本模块按坐标还原，输出 LaTeX。

处理顺序：先识别根号（消耗掉根号横线），再用剩余横线识别分式。
"""
import pymupdf, re
from collections import Counter

BAR_H = 2.0            # 水平细线：线高上限
BAR_W_MIN = 3.0
BAR_W_MAX = 220.0
UP_MAX = 24.0          # 分子纵向搜索范围
DOWN_MAX = 14.0
X_TOL = 1.0            # x 重叠容差（收紧，避免把左侧正文当分子）
LINE_TOL = 4.5         # 同一视觉行的 y 容差
RADICALS = ('√', '∛')
# 分子/分母中不应出现的孤立标点
PUNCT = set('{}()[]（）【】=，。、；：？！')


# ---------------- 上下标（几何判定） ----------------
# 为什么必须在拆解阶段做：
#   PDF 把下标排成「字号变小 + 基线下移」，上标相反。这是**无损信息**，
#   拆出来时不用，后面就只能靠「字母+数字」猜 —— 而 a2 既可能是 a₂ 也
#   可能是 a²，猜必有错。
#
# 判定必须同时满足两个条件，缺一不可：
#   1. 字号明显小于正文（< 正文 × 0.85）
#   2. 基线相对正文基线有偏移（> 0.8pt）
#
# 只有偏移、字号不变的（如 dy ≈ -7.1）不是上标 ——
# PyMuPDF 常把**下一个视觉行**并进同一个 line，那个行距偏移是假的。
# ---------------- 上下标判定 ----------------
SCRIPT_SIZE_R = 0.85   # 字号 < 正文 × 此比例 → 判定为上下标
SCRIPT_X_TOL = 2.5     # 与基底字符的 x 邻接容差（pt）
# 偏移上限（相对正文字号）。
# 实测真实上下标 |dy| ≤ 0.4×字号（上标 3.8pt、下标 0.4~1.6pt），
# 而跨行假关系 |dy| ≈ 1.4×字号（一个行距）。
# 取 0.7 作为界：覆盖全部众数区间，跨行的一律排除。
SCRIPT_MAX_DY_R = 0.7
# 注意：**不设最小偏移阈值**。核素符号 ¹₄₇N 的下标偏移只有 +0.04×字号，
# 设了阈值就会漏。方向（正负）才是判据，大小不是。


def _mark_scripts(spans):
    """基于**字号比例 + 偏移方向**标注上下标（只标注，不合并）。

    判据：
      1. 字号 < 正文 × SCRIPT_SIZE_R  → 是上下标
      2. 基线偏移 > 0 → 下标；< 0 → 上标

    正文字号取**全页众数**：不能取单行众数，分式会把单行的
    字号分布搅乱（分子分母都是小字号）。

    基底搜索必须 **y、x 双重约束**：
      - 只比对 x 不比对 y 会跨行误配 —— 核素 ¹⁴₇N 的「14」(x=378.2)
        与页面顶部另一个 span 的 x 范围重叠，被当成基底，
        dy 算出 +14.4（其实跨了 8 行），上标被判成下标。
      - |dy| 上限 SCRIPT_MAX_DY_R × 正文字号，天然排除跨行
        （真实上下标 |dy| ≤ 0.4×字号，跨行假关系 ≈ 1.4×字号）
    """
    if not spans:
        return spans

    def size_of(sp):
        return round(sp.get("size") or 0, 1)

    body = Counter(size_of(sp) for sp in spans).most_common(1)[0][0]
    if not body:
        return spans

    body_spans = [sp for sp in spans
                  if size_of(sp) >= body * SCRIPT_SIZE_R
                  and sp.get("oy") is not None]
    if not body_spans:
        return spans

    max_dy = body * SCRIPT_MAX_DY_R

    def find_base(sp, oy):
        """找 x 邻接且同视觉行的正文基底，取 |dy| 最小者。

        返回 (dy, 基底 span)；找不到返回 (None, None)。
        """
        best, best_b, best_abs = None, None, 1e9
        for b in body_spans:
            if not (b["x0"] - SCRIPT_X_TOL <= sp["x0"] <= b["x1"] + SCRIPT_X_TOL):
                continue                   # x 不邻接
            dy = oy - round(b["oy"], 1)
            if abs(dy) > max_dy or abs(dy) < 1e-6:
                continue                   # 跨行或方向不明
            if abs(dy) < best_abs:
                best_abs, best, best_b = abs(dy), dy, b
        return best, best_b

    # 第一轮：直接找得到正文基底的
    for sp in spans:
        sp["_script"] = None
        sp["_base"] = None
        if size_of(sp) >= body * SCRIPT_SIZE_R:
            continue
        oy = sp.get("oy")
        if oy is None:
            continue
        oy = round(oy, 1)
        best, best_b = find_base(sp, oy)
        if best is None:
            continue
        sp["_script"] = "sub" if best > 0 else "sup"
        sp["_dy"] = best
        sp["_base"] = best_b          # 存对象引用，避免二次搜索

    # 第二轮：链式归属。
    # 「a_{n+1}」被 PDF 拆成 a | n | +1 三个 span，
    # 「+1」与基底 a 之间隔着 n，x 距离超出容差 → 找不到基底。
    # 此时若与**同类型的已标记 script** x 紧邻，就继承它的类型和基底。
    for sp in spans:
        if sp.get("_script") or size_of(sp) >= body * SCRIPT_SIZE_R:
            continue
        for other in spans:
            if not other.get("_script") or other is sp:
                continue
            if other.get("oy") is None or sp.get("oy") is None:
                continue
            if abs(other["oy"] - sp["oy"]) > 0.5:
                continue                   # 必须同一基线（同一层上下标）
            # x 紧邻：other 的右端紧接 sp 的左端
            if abs(other["x1"] - sp["x0"]) > SCRIPT_X_TOL:
                continue
            sp["_script"] = other["_script"]
            sp["_dy"] = other.get("_dy", 0)
            sp["_base"] = other.get("_base")
            break

    return spans


def _apply_script_merge(spans):
    """把上下标 span 合并进它的基底 span，输出 LaTeX `^{}` / `_{}`。

    在**分式识别之后**调用：被分式消耗掉的 span 已标记 `_used`，
    这里跳过它们 —— 分式内部保持平文本，不会被跨分式误配。
    （曾因此把上标「−9」误配到隔壁分式的分母 t 上。）

    基底在 `_mark_scripts` 阶段已确定并存在 `_base` 字段，
    这里**不再重新搜索** —— 二次搜索会因子集/容差不一致而丢题
    （a_{n+1} 的「+1」就是这么消失的）。

    输出形态：
        基底在左 → `a_{n+1}`、`x^{2}`
        基底在右 → `^{14}_{7}N`（核素符号，上下标画在 N 的左上/左下）
    """
    groups = {}
    for sp in spans:
        if not sp.get("_script") or sp.get("_used") or sp.get("_base") is None:
            continue
        groups.setdefault(id(sp["_base"]), []).append(sp)

    if not groups:
        return spans

    for sp in spans:
        g = groups.get(id(sp))
        if not g:
            continue
        g.sort(key=lambda x: x["x0"])
        sup = "".join(str(x["t"]).strip() for x in g if x["_script"] == "sup")
        sub = "".join(str(x["t"]).strip() for x in g if x["_script"] == "sub")

        body_txt = str(sp["t"])
        if sp["x0"] > g[0]["x0"]:
            # 基底在上下标右边 → 核素式
            pre = ""
            if sup:
                pre += "^{%s}" % sup
            if sub:
                pre += "_{%s}" % sub
            sp["t"] = pre + body_txt
            sp["x0"] = min(float(sp["x0"]), float(g[0]["x0"]))
        else:
            if sup:
                body_txt += "^{%s}" % sup
            if sub:
                body_txt += "_{%s}" % sub
            sp["t"] = body_txt
            sp["x1"] = max([float(sp.get("x1") or 0)]
                           + [float(x.get("x1") or 0) for x in g])

        for x in g:
            x["_used"] = True             # 已并入基底，不再单独成 item
    return spans


def _spans_of_page(pg, drop_zones=None, pad=26, small=9.5):
    """词级 span（带精确坐标）。

    drop_zones 为插图区列表；落在其外扩范围内且字号偏小或为短 ASCII
    标记（如 a/b/c/d、g/h/i/O）的 span 判定为图中标注，予以剔除。
    """
    out = []
    _ln = 0                       # PyMuPDF line 序号（用于上下标基线归属）
    for b in pg.get_text("dict")["blocks"]:
        if b["type"] != 0:
            continue
        for l in b["lines"]:
            _ln += 1
            for s in l["spans"]:
                t = s["text"]
                if not t.strip():
                    continue
                x0, y0, x1, y1 = s["bbox"]
                if drop_zones:
                    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
                    line = t.strip()
                    # 图标注用斜体（a/b/c/d、g/h/i/O、B/C/A/D），正文数字是正体。
                    # 只看「短 ASCII」会把题干里的 5、39、m0 一并误删。
                    italic = ("Italic" in s["font"]) or ("Oblique" in s["font"])
                    short_mark = (len(line) <= 3 and italic
                                  and re.fullmatch(r"[A-Za-z0-9\u2032\u00b7\-]+", line or "x"))
                    if round(s["size"], 1) < small or short_mark:
                        hit = False
                        for z in drop_zones:
                            if (z[0] - pad <= cx <= z[2] + pad
                                    and z[1] - pad <= cy <= z[3] + pad):
                                hit = True
                                break
                        if hit:
                            continue
                out.append({"t": t, "x0": x0, "x1": x1,
                            "y0": y0, "y1": y1,
                            "cy": (y0 + y1) / 2,
                            # 基线 y：判定上下标的关键。
                            # bbox 的中心 cy 会被字号和字形影响，
                            # 只有 origin[1] 才是真正的排版基线。
                            "oy": round(s["origin"][1], 1)
                            if s.get("origin") else (y0 + y1) / 2,
                            "size": round(s["size"], 1),
                            "font": s["font"],
                            "ln": _ln,
                            "_used": False, "_idx": len(out)})
    # 先标上下标再返回：下游（根号/分式/聚行）看到的就是已合并的文本
    return _mark_scripts(out)


def _bars_of_page(pg):
    """水平细线（分数线 / 根号横线 / 下划线）"""
    bars = []
    for dr in pg.get_drawings():
        r = dr["rect"]
        w, h = r.width, r.height
        if h <= BAR_H and BAR_W_MIN <= w <= BAR_W_MAX:
            bars.append({"x0": r.x0, "x1": r.x1, "y": (r.y0 + r.y1) / 2,
                         "w": w, "h": h, "_used": False})
    return bars


# ---------------- 根号 ----------------
def _find_radicals(spans, bars):
    """识别 √ 及其覆盖内容，返回 [(根号span, 内容文本, x0, x1, y)]"""
    out = []
    for s in spans:
        if not any(r in s["t"] for r in RADICALS):
            continue
        # 根号横线：左端紧邻 √ 右侧，且纵向落在 √ 的垂直范围内
        best = None
        for b in bars:
            if b["_used"]:
                continue
            if b["x0"] < s["x0"] - 2:
                continue
            if b["x0"] > s["x1"] + 4:
                continue
            if not (s["y0"] - 2 <= b["y"] <= s["y1"] + 3):
                continue
            d = abs(b["y"] - (s["y0"] + s["y1"]) / 2)
            if best is None or d < best[0]:
                best = (d, b)
        if not best:
            continue
        bar = best[1]
        # 根号内容：横线覆盖范围内、√ 右侧、横线下方（横线是盖在内容顶部的）
        inner = []
        for t in spans:
            if t is s or t["_used"]:
                continue
            if t["x0"] < s["x1"] - 1.5:
                continue
            if t["x0"] > bar["x1"] + 1:
                continue
            if t["cy"] < bar["y"] - 3:
                continue
            if t["cy"] > bar["y"] + s["size"] * 1.9:
                continue
            inner.append(t)
        inner.sort(key=lambda t: t["x0"])
        txt = "".join(t["t"] for t in inner).strip()
        cy_inner = (sum(t["cy"] for t in inner) / len(inner)) if inner else bar["y"]
        bar["_used"] = True
        s["_used"] = True
        for t in inner:
            t["_used"] = True
        out.append({"x0": s["x0"], "x1": max(bar["x1"], s["x1"]),
                    "y": s["y0"], "cy": cy_inner,
                    "bot": bar["y"], "txt": txt})
    return out


# ---------------- 分式 ----------------
def _pick(spans, bar, side, limit):
    """收集分子(side=-1)/分母(side=+1)。

    三处关键：
    ① 按 y0（顶部）筛选而非 bbox 中心 —— 数字与希腊字母高度不同。
    ② x 方向用中心点判定 —— 只要求边缘接触会把紧邻左侧的「A．」误当分子。
    ③ 收集纵向范围内「全部」成分后按 x 排序 —— 分式的主体与下标
       y0 通常不同（下标更低），只取最近一行会把「E1 − E2」拆成「12」。
    """
    cand = []
    for s in spans:
        if s["_used"]:
            continue
        if side < 0:
            if not (bar["y"] - limit <= s["y0"] <= bar["y"] - 1.0):
                continue
        else:
            if not (bar["y"] + 0.5 <= s["y0"] <= bar["y"] + limit):
                continue
        cx = (s["x0"] + s["x1"]) / 2
        if not (bar["x0"] - X_TOL <= cx <= bar["x1"] + X_TOL):
            continue
        cand.append(s)
    if not cand:
        return None
    # 合并「主体行 + 下标行」：两者 y0 通常差 3~5pt
    cand.sort(key=lambda s: -s["y0"])
    top = cand[0]["y0"]
    grp = [s for s in cand if s["y0"] >= top - 5.0]
    # 过滤误入的孤立标点（花括号、等号等）
    grp = [s for s in grp
           if not (len(s["t"].strip()) == 1 and s["t"].strip() in PUNCT)]
    if not grp:
        return None
    grp.sort(key=lambda s: s["x0"])
    return [(0, s["x0"], s) for s in grp]


def _find_fracs(spans, bars):
    out = []
    for bar in sorted(bars, key=lambda b: -b["w"]):
        if bar["_used"]:
            continue
        num = _pick(spans, bar, -1, UP_MAX)
        den = _pick(spans, bar, +1, DOWN_MAX)
        if not num or not den:
            continue
        ntxt = "".join(c[2]["t"] for c in num).strip()
        dtxt = "".join(c[2]["t"] for c in den).strip()
        if not ntxt or not dtxt:
            continue
        if len(ntxt) > 14 or len(dtxt) > 14:
            continue
        for c in num:
            c[2]["_used"] = True
        for c in den:
            c[2]["_used"] = True
        bar["_used"] = True
        out.append({
            "x0": min(bar["x0"], min(c[2]["x0"] for c in num + den)),
            "x1": max(bar["x1"], max(c[2]["x1"] for c in num + den)),
            "top": min(c[2]["y0"] for c in num),
            "bot": max(c[2]["y1"] for c in den),
            "cy": bar["y"],
            "num": ntxt, "den": dtxt,
        })
    return out


# ---------------- 行重建 ----------------
def _radical_as_span(r):
    """把根号转成虚拟 span，使其能作为分式的分子/分母参与识别"""
    return {"t": r["latex"], "x0": r["x0"], "x1": r["x1"],
            "y0": r["y"], "y1": r["bot"], "cy": r["cy"],
            "size": 10.5, "font": "virtual", "_used": False,
            "_idx": -1, "_virt": True}


def _build_lines_in_col(spans, bars):
    """在单一栏内：识别根号 → 分式 → 聚行（内部实现）"""

    # 1) 先识别根号，转成虚拟 span 后再识别分式
    radicals = _find_radicals(spans, bars)
    for r in radicals:
        r["latex"] = ("\sqrt{%s}" % r["txt"]) if r["txt"] else "\sqrt{}"
    for r in radicals:
        r["_span"] = _radical_as_span(r)
    spans = spans + [r["_span"] for r in radicals]

    fracs = _find_fracs(spans, bars)

    # 分式已识别完毕（被消耗的 span 标记了 _used），
    # 此时再合并上下标才安全 —— 分式内部保持平文本。
    spans = _apply_script_merge(spans)

    items = []
    for s in spans:
        if s["_used"] or s.get("_virt"):
            continue
        items.append({"x0": s["x0"], "x1": s["x1"], "y": s["cy"],
                      "t": s["t"], "k": "t", "bot": s["y1"]})
    for f in fracs:
        # 分式的视觉中心 = 分数线位置，与同行正文的视觉中心一致
        items.append({"x0": f["x0"], "x1": f["x1"], "y": f["cy"],
                      "t": "\\frac{%s}{%s}" % (f["num"], f["den"]), "k": "f"})

    for r in radicals:
        if r["_span"]["_used"]:
            continue          # 已被分式吸收为分子/分母
        items.append({"x0": r["x0"], "x1": r["x1"], "y": r["cy"],
                      "t": r["latex"], "k": "r"})

    items.sort(key=lambda i: (i["y"], i["x0"]))

    lines = []
    cur = None
    for it in items:
        if cur is None or abs(it["y"] - cur["y"]) > LINE_TOL:
            if cur:
                lines.append(cur)
            cur = {"y": it["y"], "parts": [it]}
        else:
            cur["parts"].append(it)
            cur["y"] = min(cur["y"], it["y"])
    if cur:
        lines.append(cur)

    out = []
    for ln in lines:
        ln["parts"].sort(key=lambda p: p["x0"])
        buf = []
        prev = None
        for p in ln["parts"]:
            if prev is not None and p["x0"] - prev > 1.0:
                if buf and not buf[-1].endswith(" "):
                    buf.append(" ")
            buf.append(p["t"])
            prev = p["x1"]
        txt = re.sub(r"\s+", " ", "".join(buf)).strip()
        if txt:
            out.append({"y": ln["y"], "x": ln["parts"][0]["x0"], "t": txt})
    return out


# ---------------- 分栏检测 ----------------
QNUM_RE = re.compile(r'^\d{1,2}\s*[．.、]')


WIDE_PAGE = 700        # 页面宽度门槛：低于此值视为单栏


def _validate_cols(pg, starts, xs, max_cols=4):
    """校验候选栏起点：间距、栏宽、题号数三重把关。

    贪心接受：只有与「上一个已接受栏」的间距够大才接受新栏。
    这样既能挡掉 A4 单栏卷里解析编号聚成的假峰（185/456），
    也能剔除多栏卷中个别缩进造成的杂散簇（如 608/612）。
    """
    if len(starts) < 2:
        return []
    W = pg.rect.width
    min_gap = 250 if W < 700 else 150
    min_w = 200 if W < 700 else 300
    need = max(min_gap, min_w)          # 栏宽 = 到下一栏的距离
    keep = [starts[0]]
    for x in starts[1:]:
        if x - keep[-1] >= need:
            keep.append(x)
    # 最后一栏宽度也要够
    if W - 50 - keep[-1] < min_w:
        keep = keep[:-1]
    if len(keep) < 2:
        return []
    # 每栏都要有若干题号
    counts = []
    for i, k in enumerate(keep):
        nxt = keep[i + 1] if i + 1 < len(keep) else 10 ** 9
        counts.append(sum(1 for x in xs if k - 12 <= x < nxt))
    if min(counts) < 2:
        return []
    return keep[:max_cols]


def _cluster_xs(xs, x_tol=12, min_per_col=2):
    """把横坐标聚成簇，返回每簇的最小值。

    x_tol 取 12 而非 60：真实栏起点在各页精确到 1pt 以内（54/421/793），
    而解析段落里的编号、缩进造成的偏移是散点。用 60 会把它们
    并进同一个簇，簇起点被带偏（如 793 → 685），栏边界随之错位。
    """
    groups = []
    for x in sorted(xs):
        if groups and x - groups[-1][-1] <= x_tol:
            groups[-1].append(x)
        else:
            groups.append([x])
    groups = [g for g in groups if len(g) >= min_per_col]
    return sorted(min(g) for g in groups)


def detect_columns(pg, spans=None, min_per_col=2, x_tol=12, max_cols=4):
    """检测单页的栏起始 x 坐标（单栏返回 []）。

    关键：题号是分栏最可靠的标志 —— 每栏题号都从固定 x 起步，
    而同一 y 高度上会并存各栏内容，所以既不能按 y 聚行后再分栏，
    也难靠「栏间空隙」判断（空隙窄且常被插图、长公式跨过）。

    做法：取所有题号 span，按 x 聚类；有几簇就有几栏。
    """
    if spans is None:
        spans = _spans_of_page(pg)
    # 前提：只有宽幅页面才可能是多栏
    if pg.rect.width < WIDE_PAGE:
        return []
    qn = [s for s in spans if QNUM_RE.match(s["t"].strip())]
    if len(qn) < 2:
        return []
    xs = [s["x0"] for s in qn]
    starts = _cluster_xs(xs, x_tol=x_tol, min_per_col=min_per_col)
    return _validate_cols(pg, starts, xs, max_cols=max_cols)


def split_columns(pg, lines):
    """分栏页：按栏从左到右（栏内按 y）拼接，先左栏全部再右栏"""
    cols = detect_columns(pg)
    if len(cols) < 2:
        return lines
    bounds = cols + [10 ** 9]
    out = []
    for i in range(len(bounds) - 1):
        lo, hi = bounds[i], bounds[i + 1]
        seg = [ln for ln in lines if lo - 5 <= ln["x"] < hi]
        if seg:
            out.extend(seg)
    return out if out else lines


def build_geo_lines(pg, drop_zones=None, cols=None):
    """重建页面逻辑行，根号/分式内联为 LaTeX。

    关键顺序：先按栏切分，再在栏内聚行。
    三栏排版下同一 y 高度会并存三栏内容，若先聚行，
    会把「{ }」和隔壁栏的「11. 已知…」粘成一行，导致题号丢失。

    返回 [{"y": float, "x": float, "t": str}, ...]，按阅读顺序。
    """
    spans_all = _spans_of_page(pg, drop_zones=drop_zones)
    bars_all = _bars_of_page(pg)
    if not spans_all:
        return []

    if not cols:
        cols = detect_columns(pg, spans=spans_all)
    if len(cols) >= 2:
        # 分栏区间：第一栏从页左边延伸到「第二栏起点」，
        # 即 [0, cols[1]) [cols[1], cols[2]) … [cols[-1], ∞)。
        # 不能写成 [0, cols[0]) —— 那会造出一个宽度只有几十 pt 的窄栏，
        # 把题号（x≈49）和它的正文（x≈67）切开，题号行因无内容而被丢弃。
        bounds = [0] + cols[1:] + [10 ** 9]
        groups = []
        for i in range(len(bounds) - 1):
            lo, hi = bounds[i], bounds[i + 1]
            g_spans = [s for s in spans_all if lo <= s["x0"] < hi]
            g_bars = [b for b in bars_all if lo <= b["x0"] < hi]
            if g_spans:
                groups.append((g_spans, g_bars))
    else:
        groups = [(spans_all, bars_all)]

    out = []
    for spans, bars in groups:
        out.extend(_build_lines_in_col(spans, bars))
    return out


def document_columns(doc, max_pages=None):
    """整卷统一的栏结构。

    为什么不能用单页：末页题目少，单页聚类会把只有 1~2 个题号的栏过滤掉；
    而该栏题号恰好与前两栏处在同一 y 高度，会被粘进同一行，整道题丢失。

    做法：累积全卷所有页的题号横坐标再聚类 —— 同一栏的题号
    在各页都从相同 x 起步，累积后样本充足。
    """
    if max_pages is None:
        max_pages = doc.page_count
    if not doc.page_count or doc[0].rect.width < WIDE_PAGE:
        return []          # A4 单栏卷，无需分栏
    xs_all = []
    for pno in range(min(doc.page_count, max_pages)):
        try:
            spans = _spans_of_page(doc[pno])
        except Exception:
            continue
        for s in spans:
            if QNUM_RE.match(s["t"].strip()):
                xs_all.append(s["x0"])
    if len(xs_all) < 4:
        return []
    starts = _cluster_xs(xs_all, x_tol=12, min_per_col=2)
    # 校验用第一页的尺寸
    return _validate_cols(doc[0], starts, xs_all, max_cols=4)

