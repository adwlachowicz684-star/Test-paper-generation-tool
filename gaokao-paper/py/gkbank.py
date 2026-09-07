# -*- coding: utf-8 -*-
import re
"""基础正则与工具函数"""
import pymupdf, re, os

# 题号行。允许行首有少量「残留前缀」：多栏排版下，上一栏末尾的括号、
# 孤立数字等会漂到下一栏首行（例：'  ( ) 16. 已知…'、'2 19. (1) 求…'）。
# 前缀限定为「不含中文的 0~8 个字符」，中文正文因此不会被误判。
# 两条约束：
#   (1) ([1-9]\d?) —— 题号从 1 起，'0.…' 不是题号；
#   (2) (?!\d)     —— 题号后的句点不能紧跟数字，
#                     否则解析里的数值 '11.8' 会被当成第 11 题。
QHEAD = re.compile(r'^(?:[（(]\s*[)）]\s*|\d\s+)?([1-9]\d?)\s*[．.、](?!\d)\s*(.*)$')
OPT   = re.compile(r'^([A-D])\s*[．.、]\s*(.*)$')
ANA   = re.compile(r'^【(详解|解析|答案|分析)】(.*)$')
SEC   = re.compile(r'^[一二三四五六七八九十]+、')
NOISE = re.compile(r'注意事项|答题卡|考生务必|考试结束|答题前|条形码|核准|涂黑|草稿纸')
ANS_PAT = [
    re.compile(r'故选\s*([A-D])'),
    re.compile(r'答案[是为：:\s]*([A-D])'),
    re.compile(r'选\s*([A-D])\s*项'),
    re.compile(r'故选\s*([A-D]{1,4})'),
]
SUBQ   = re.compile(r'[（(]\s*(\d{1,2})\s*[)）]')
RESULT = re.compile(r'(?:解得|可得|则有|故)\s*([^，。；]{1,40}?)\s*[。；]')
EQTAIL = re.compile(r'=\s*([^，。；\s][^，。；]{0,30})')

# 插图判定：矢量图形的最小边长（公式构件多为细线，边长很小）
FIG_MIN = 25
# 插图区外扩（用于包含图中的字母标注，如物理图的 a/b/c/d/g/h/i/O）
FIG_PAD = 18
# 小于该字号且落在插图扩展区内的文字 → 判定为图标注，排除
LABEL_SIZE = 9.5

# 原卷页脚（第 3 页 共 8 页 / 第3页共8页 / 3 / 8）
# ---------------- 题干清洗 ----------------
# 作答位：原卷选择题在题干末尾留「（    ）」给考生填答案。
# 组卷网等题库站也是这么存的（如「且，则（　　）A．16B．18…」）。
# 但我们的渲染把选项排到题干**下方**，这个作答位就成了多余尾巴，
# 而且提取时可能被重复抓取，变成「( ) ( ) ( ) ( ) ( )」。
#
# 要求括号前有空白：避免误伤「f( )」这类真实函数记号。
TAIL_BLANK = re.compile(r'\s*(?<![A-Za-z0-9])(?:[（(]\s*[)）]\s*)+$')

# 选项漏进题干：原卷分栏/换行导致 A．B．C．D．被拼进题干。
# 形如「…则（ ） C. … D. …」—— 作答位后面直接跟着选项。
LEAKED_OPTS = re.compile(
    r'(?P<head>.*?[（(]\s*[)）])\s*(?P<tail>[A-D]\s*[．.、].*)$', re.S)
# 切分漏进来的选项（保留字母）
LEAK_SPLIT = re.compile(r'(?:^|\s)([A-D])\s*[．.、]\s*')


# 作答位：选择题题干末尾给考生填答案的位置。
# 高考卷标准样式是全角括号 + 全角空格。
ANSWER_BLANK = '（　　）'


# ---------------- 下标识别 ----------------
# 现状：PDF 提取把下标压成了普通字符（a_{n+1} → an+1、F_{1} → F1）。
# 而「字母+数字」有**歧义**：x3 可能是 x³（立方）也可能是 x₃（下标），
# 所以不能无脑转换，必须靠上下文判定。
#
# 三条规则，置信度从高到低，逐条收紧：

# 前置断言：不能紧跟在字母/数字/反斜杠/下划线之后。
#   - 排除字母数字：避免拆散 \frac、x2 这类已有结构
#   - 排除反斜杠：避免匹配 LaTeX 命令名（\frac、\sqrt）
#   - 排除下划线：避免对已转换的 a_{n} 二次处理
#   **不排除 {**：{an}、\frac{Sn}{an} 里的下标同样要转换
_PRE = r'(?<![A-Za-z0-9\\_])'

# 1) 大写字母 + 数字 —— 几乎必是下标
#    F1/F2（焦点）、P1/P2/P3（点）、A1B1C1（棱柱顶点）
# 前置只排除字母 / 反斜杠 / 下划线，**不排除数字**：
# 「A1B1C1」里 B1 的前一位是数字 1，连数字一起排除的话
# 只有 A1 被转换，B1C1 会漏掉（棱柱/立方体顶点常这样连写）。
# 只排除小写字母 / 反斜杠 / 下划线。
# 大写字母和数字都要放行，否则两处会漏：
#   「A1B1C1」B1 前是数字 1 → 必须放行数字
#   「AB = AA1」A1 里第二个 A 前是大写 A（侧棱 AA₁）→ 必须放行大写
_PRE_NUM = r'(?<![a-z\\_])'
SUB_BIG = re.compile(_PRE_NUM + r'([A-Z\u0370-\u03ff])(\d+)')

# 2) 字母 + n（可带 +数字/-数字）—— 数列项
#    an / bn / Sn / xn / an+1 / a2n
#    **必须排除函数名**：ln（自然对数）会被误判成 l 下标 n
# 支持三种形态：
#   an      → a_{n}
#   an+1    → a_{n+1}   （必须整段匹配，否则会变成 a_{n}+1）
#   a2n     → a_{2n}    （「记 bn = a2n」里的复合下标）
SUB_N = re.compile(_PRE + r'([A-Za-z\u0370-\u03ff])(n(?:[+-]\d+)?|\d+n)(?![A-Za-z])')

# 3) 小写字母 + 数字 —— 歧义最大，只在有强证据时转换
#    证据：同一题干里同时出现「该字母 + n」（x1 与 xn 并存），
#    说明这是一个 x1, x2, …, xn 的下标序列。
#    没有证据的一律不动：x3 = x³、y2 = y²、b2 = b² 都是上标。
SUB_SMALL = re.compile(_PRE + r'([a-z\u0370-\u03ff])(\d+)(?![A-Za-z0-9])')

# 函数名黑名单（规则 2 的例外）
_NOT_SUB = {'ln', 'sin', 'cos', 'tan', 'log', 'min', 'max', 'sec', 'csc'}


def mark_subscripts(text):
    """把压平的下标还原成 LaTeX `_{}`。

    应转换：
        「数列 {an} 满足 a1 = 1, an+1 = an + 2」→「{a_{n}} … a_{1} … a_{n+1}」
        「F1, F2 是椭圆的焦点」           →「F_{1}, F_{2}」
        「x1, x2, · · · , xn」             →「x_{1}, x_{2}, …, x_{n}」
        「在正三棱柱 ABC − A1B1C1 中」    →「A_{1}B_{1}C_{1}」

    不转换（避免把上标误改成下标）：
        「f (x) = x3 − x + 1」        x3 是 x³（题干里没有 xn）
        「抛物线 y2 = 2px」           y2 是 y²
        「f (x) = |2x − 1| − 2 ln x」 ln 是函数名，不是 l 下标 n
    """
    if not text:
        return text
    t = str(text)

    # 规则 3 需要整串信息：先找出哪些字母有「序列证据」
    seq_ok = set()
    for m in SUB_N.finditer(t):
        if (m.group(1) + m.group(2)).lower() not in _NOT_SUB:
            seq_ok.add(m.group(1))

    cands = []
    for lv, pat in ((1, SUB_BIG), (2, SUB_N)):
        for m in pat.finditer(t):
            base, sub = m.group(1), m.group(2)
            if lv == 2 and (base + sub).lower() in _NOT_SUB:
                continue
            cands.append((m.start(), m.end(), base, sub, lv))
    for m in SUB_SMALL.finditer(t):
        if m.group(1) in seq_ok:
            cands.append((m.start(), m.end(), m.group(1), m.group(2), 3))

    # 同一位置只保留优先级最高的（lv 小者优先），且不允许区间重叠
    cands.sort(key=lambda x: (x[0], x[4], -(x[1] - x[0])))
    picked, last_end = [], -1
    for c in cands:
        if c[0] < last_end:
            continue
        picked.append(c)
        last_end = c[1]

    out, pos = [], 0
    for st, en, base, sub, _lv in picked:
        out.append(t[pos:st])
        out.append('%s_{%s}' % (base, sub))
        pos = en
    out.append(t[pos:])
    return ''.join(out)


def strip_tail_blank(text):
    """去掉题干尾部多余的作答位括号（不含重新加回）。"""
    if not text:
        return text
    return TAIL_BLANK.sub('', str(text)).rstrip()


def normalize_tail_blank(text, keep=False):
    """尾部连续空括号 → **恰好一个**作答位。

    keep=True（选择题）：归一化为「（　　）」
        「…单调递增的区间是 ( ) ( ) ( ) ( ) ( )」→「…单调递增的区间是（　　）」
        「…则该过程中跨膜电流的平均值为（ ）」    →「…平均值为（　　）」
        「…则该卫星（ ）」                        →「…则该卫星（　　）」

    keep=False（填空/解答）：全部去掉
        填空题的填空处由渲染层转成下划线，不该出现括号；
        解答题更不需要。

    为什么不能直接删掉作答位：高考卷选择题题干末尾**本来就有**
    「（　　）」，它和下方选项是共存的，学生做题时习惯看到它。
    之前整段删除，卷面就变成了「…则 A．… B．…」，反而不像试卷。

    只处理**尾部**连续空括号；中间的空括号是公式占位符，
    真实内容常被提取到紧随其后的位置，删了反而丢信息。
    """
    if not text:
        return text
    out = TAIL_BLANK.sub('', str(text)).rstrip()
    if not keep:
        return out
    # 作答位前不该留句号（高考卷里作答位后也没有句号）。
    # 先剥掉再拼接，否则会出现「…则。（　　）」这种怪样式。
    out = re.sub(r'[。．]\s*$', '', out).rstrip()
    return out + ANSWER_BLANK


def split_leaked_opts(text):
    """把误并入题干尾部的选项切出来。

    返回 (清洗后的题干, [(字母, 文本), ...])。
    没发现泄漏时原文返回。
    """
    if not text:
        return text, []
    m = LEAKED_OPTS.match(str(text))
    if not m:
        return text, []
    tail = m.group('tail')
    parts = LEAK_SPLIT.split(tail)
    # split 结果：[前导空串, 字母1, 文本1, 字母2, 文本2, ...]
    opts = []
    for i in range(1, len(parts) - 1, 2):
        letter, body = parts[i], parts[i + 1].strip()
        if body:
            opts.append((letter, body))
    if not opts:
        return text, []
    return m.group('head').rstrip(), opts


PAGEFOOT = re.compile(
    r'第\s*\d+\s*页\s*共\s*\d+\s*页|第\s*\d+\s*页\s*共\s*\d+\s*頁|'
    r'^\s*\d+\s*/\s*\d+\s*$')


def detect_figures(doc, min_size=6, gap=12, fig_min=40):
    """按页检测插图区。
    插图常由许多小图元（线段、字符位图）拼成，先按小图元聚类，
    再按聚类后的整体尺寸（宽高均 >= fig_min）判定是否为插图，
    以此排除解析区里的大片公式（通常高度不足）。
    """
    out = {}
    for pno, pg in enumerate(doc):
        boxes = []
        # 矢量图形：保留细线（水平线 height 常为 0），仅按长度过滤
        for dr in pg.get_drawings():
            r = dr["rect"]
            if max(r.width, r.height) >= min_size:
                boxes.append([r.x0, r.y0, r.x1, r.y1])
        # 位图：排除字符级小图（10x15pt 上下的字母、根号）
        try:
            for im in pg.get_image_info():
                b = im["bbox"]
                if (b[2] - b[0]) >= min_size and (b[3] - b[1]) >= min_size:
                    boxes.append([b[0], b[1], b[2], b[3]])
        except Exception:
            pass
        merged = []
        for b in sorted(boxes, key=lambda x: (x[1], x[0])):
            hit = None
            for m in merged:
                if not (b[2] < m[0] - gap or b[0] > m[2] + gap
                        or b[3] < m[1] - gap or b[1] > m[3] + gap):
                    hit = m
                    break
            if hit:
                hit[0] = min(hit[0], b[0]); hit[1] = min(hit[1], b[1])
                hit[2] = max(hit[2], b[2]); hit[3] = max(hit[3], b[3])
            else:
                merged.append(b[:])
        out[pno] = [tuple(m) for m in merged
                    if (m[2] - m[0]) >= fig_min and (m[3] - m[1]) >= fig_min]
    return out


def raw_stream(pdf_path, fig_boxes=None, pad=FIG_PAD, small=LABEL_SIZE):
    """原始文本流：基于几何坐标重建，分式/根号内联为 LaTeX。

    相比直接读 PDF 内容流，几何重建能正确还原被拆行的分式，
    并自动剔除插图中的字母标注、清除原卷页脚。
    """
    from geoformula import build_geo_lines
    doc = pymupdf.open(pdf_path)
    rows = []
    # 整卷统一的栏结构（在 build_geo_lines 内部按栏切分后再聚行）
    try:
        from geoformula import document_columns
        doc_cols = document_columns(doc)
    except Exception:
        doc_cols = None
    for pno, pg in enumerate(doc):
        zones = (fig_boxes or {}).get(pno, [])
        try:
            lines = build_geo_lines(pg, drop_zones=zones or None, cols=doc_cols)
        except Exception:
            lines = []
            for ln in pg.get_text().split("\n"):
                t = re.sub(r"\s+", " ", ln).strip()
                if t:
                    lines.append({"y": 0.0, "x": 0.0, "t": t})
        for ln in lines:
            t = PAGEFOOT.sub("", ln["t"]).strip()
            if not t:
                continue
            if re.fullmatch(r"[\d\s/\-—.]*", t):
                continue
            rows.append({"p": pno, "t": t, "y": ln["y"], "x": ln["x"]})
    return rows


def _seg_result(seg):
    m = RESULT.search(seg)
    if m:
        v = m.group(1).strip()
        if 1 <= len(v) <= 40:
            return v
    eqs = EQTAIL.findall(seg)
    if eqs:
        v = eqs[-1].strip()
        if 1 <= len(v) <= 40:
            return v
    return ""


def crop_figs(doc, qs, outdir, fig_boxes, dpi=300, pad=FIG_PAD, min_sz=15,
              target_kb=30, photo_kb=35):
    """按插图区裁图（外扩以包含图中的字母标注）。
    照片类位图（连续色调）用 JPEG 压缩，线条图用 PNG，
    并对超标图片自动降 dpi，控制单图体积。
    """
    os.makedirs(outdir, exist_ok=True)
    for q in qs:
        boxes = q.get("figbox") or []
        q["figs"] = []
        if not boxes:
            continue
        boxes = sorted(boxes, key=lambda b: (b[4], b[1]))
        for gi, (x0, y0, x1, y1, pno) in enumerate(boxes, 1):
            if (x1 - x0) < min_sz or (y1 - y0) < min_sz:
                continue
            pg = doc[pno]
            cx0 = max(0, x0 - 6);           cy0 = max(0, y0 - pad)
            cx1 = min(pg.rect.width, x1 + 6); cy1 = min(pg.rect.height, y1 + pad)
            clip = pymupdf.Rect(cx0, cy0, cx1, cy1)
            # 该区域内是否有真位图（照片）；字符级小位图不算
            photo = False
            try:
                for im in pg.get_image_info():
                    b = im["bbox"]
                    if (b[2] - b[0]) >= 40 and (b[3] - b[1]) >= 40:
                        ix = max(b[0], cx0) < min(b[2], cx1)
                        iy = max(b[1], cy0) < min(b[3], cy1)
                        if ix and iy:
                            photo = True
                            break
            except Exception:
                pass
            # 逐级降 dpi，直到体积达标
            limit = photo_kb if photo else target_kb
            for d in ([dpi, 200, 150, 110] if photo else [dpi, 240, 200, 165]):
                pix = pg.get_pixmap(clip=clip, dpi=d)
                if photo:
                    data = pix.tobytes("jpeg", jpg_quality=85)
                    ext = "jpg"
                else:
                    data = pix.tobytes("png")
                    ext = "png"
                if len(data) // 1024 <= limit or d <= 110:
                    break
            fn = f"{q['id']}_fig{gi}.{ext}"
            fp = os.path.join(outdir, fn)
            with open(fp, "wb") as f:
                f.write(data)
            q["figs"].append({"file": fn, "w": pix.width, "h": pix.height,
                              "kb": len(data) // 1024})
