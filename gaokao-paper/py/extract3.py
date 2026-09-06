# -*- coding: utf-8 -*-
"""从高考真题 PDF 提取题目：题干 / 选项 / 答案 / 解析 / 插图"""
import pymupdf, re, os, json
from pdfsplit import page_lines
from gkbank import (QHEAD, OPT, ANA, SEC, NOISE, ANS_PAT, SUBQ,
                    RESULT, EQTAIL, _seg_result, raw_stream,
                    detect_figures, FIG_PAD)

# 选项标记：兼容多种原卷格式
#   A．xxx   A.xxx   A、xxx   (A)xxx   （A）xxx
#
# 【关键】分隔符（．.、）或括号对**必须出现**，不能设为可选。
# 曾写成 `[）)]?\s*[．.、]?` 全可选，导致选项**正文里**的裸字母
# 被当成下一个选项的标记：
#     原句：  A．A 比 B 先落入篮筐
#     误判：  A="A 比"   B="先落入篮筐"     ← 真选项 B 整条丢失
#     统计：  12 份真题共 178 行受此影响
# 类似的还有集合题「集合 A = {...}, B = {...}」被拆成 4 个假选项。
#
# 两种合法形态，三选一（group 1/2/3 分别对应）：
#   (A)  （A）  → 括号包裹
#   A． A. A、   → 字母 + 分隔符
OPT_MARK = re.compile(r'(?:^|[\s　])(?:\(([A-D])\)|（([A-D])）|([A-D])\s*[．.、])\s*')
OPTSCAN = re.compile(r'(?:^|[\s　])(?:\(([A-D])\)|（([A-D])）|([A-D])\s*[．.、])\s*')
OPTSTART = re.compile(r'^(?:\(([A-D])\)|（([A-D])）|([A-D])\s*[．.、])\s*(.*)$')


def _opt_letter(m):
    """取选项字母（三个捕获组三选一）"""
    return m.group(1) or m.group(2) or m.group(3)
FRAC_MAXLEN = 10     # 分子/分母的最大字符数（超过则视为普通换行）

# 图片选项行：整行**只有**选项字母（如 "A B C D"）。
# 这类题的选项内容就是下方的图（肥皂膜侧视形状、光电效应图像…），
# 文本为空。必须与上面的 OPTSCAN 分开处理：
# OPTSCAN 要求分隔符（．.、）或括号，而这里一个分隔符都没有。
# 判据是「整行 fullmatch + 至少两个字母」——
# 几何题正文不会恰好只剩几个孤立大写字母，所以不会误伤。
IMG_OPT_LINE = re.compile(r'^[A-D](?:[\s　]+[A-D])+$')


def _close_opt(q):
    """收束选项累积；若恰为两行且都很短，判定为分式"""
    if q.get("opt_open") and q.get("opt_buf"):
        buf = [x.strip() for x in q["opt_buf"] if x.strip()]
        if len(buf) == 2 and len(buf[0]) <= FRAC_MAXLEN and len(buf[1]) <= FRAC_MAXLEN:
            val = "\\frac{" + buf[0] + "}{" + buf[1] + "}"
        else:
            val = " ".join(buf)
        q["opts"].append((q["opt_open"], re.sub(r"\s+", " ", val).strip()))
    q["opt_open"] = None
    q["opt_buf"] = []


def _take_opts(text, cur):
    """一行内含多个选项：A．… B．… C．…"""
    marks = list(OPTSCAN.finditer(text))
    if len(marks) < 2:
        return False
    letters = [_opt_letter(m) for m in marks]
    have = len(cur["opts"])
    exp = chr(ord('A') + have) if have else 'A'
    if letters[0] != exp:
        return False
    for i, L in enumerate(letters):
        if L != chr(ord(exp) + i):
            return False
    pre = text[:marks[0].start()].strip()
    if pre:
        cur["stem"].append(pre)
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        cur["opts"].append((_opt_letter(m), text[m.end():end].strip()))
    return True


def extract(pdf_path, subject):
    doc = pymupdf.open(pdf_path)
    prefix = {"数学": "M", "物理": "P", "化学": "C",
              "生物": "B", "语文": "Y", "英语": "E"}[subject]

    fig_boxes = detect_figures(doc)
    raw = raw_stream(pdf_path, fig_boxes)

    # 规则：卷头（标题、注意事项）里也有 1./2./3. 编号，
    # 但它们不是题号。以「第一个真正的题号 1」为起点。
    # 注意：不能依赖分节标题定位 —— 多栏排版下分节标题可能不在最前。
    start_at = 0
    for i, r in enumerate(raw):
        m = QHEAD.match(r["t"])
        if m and int(m.group(1)) == 1 and not NOISE.search(r["t"][:40]):
            start_at = i
            break
    raw = raw[start_at:]

    qs = []
    cur = None
    mode = "stem"
    for ln in raw:
        t = ln["t"]
        pno = ln["p"]
        if NOISE.search(t[:30]) and cur is None:
            continue
        if SEC.match(t):
            if cur is not None and mode == "ana":
                _close_opt(cur)
                qs.append(cur)
                cur = None
            continue

        ma = ANA.match(t)
        if ma and cur is not None:
            mode = "ana"
            cur["ana"].append(ma.group(2))
            if ma.group(1) == "答案":
                cur["ans_raw"].append(ma.group(2))
            continue

        mq = QHEAD.match(t)
        if mq and not ma:
            if NOISE.search(t[:40]):
                continue
            n = int(mq.group(1))
            body = mq.group(2).strip()
            # 规则：题号行必须"有内容"或"题号连续递增"。
            # 「3．」这类（根号的被开方数后带句号、独立成行）不是题号。
            is_qhead = bool(body) or (cur is not None and n == cur["num"] + 1)
            if not is_qhead:
                if cur is not None:
                    if mode == "ana":
                        cur["ana"].append(t)
                    else:
                        cur["stem"].append(t)
                continue
            if cur is not None and n <= cur["num"] and mode == "ana":
                cur["ana"].append(t)
                continue
            if cur is not None:
                _close_opt(cur)
                qs.append(cur)
            cur = {"num": n, "p": pno, "y0": ln["y"], "stem": [mq.group(2)], "opts": [],
                   "ana": [], "ans_raw": [], "figbox": [],
                   "id": f"{prefix}-{n:03d}", "opt_open": None, "opt_buf": []}
            mode = "stem"
            continue

        if cur is None:
            continue
        if mode == "ana":
            cur["ana"].append(t)
            continue

        # stem 区：选项跨行累积（分式分子分母被拆行时也能正确归并）
        if cur.get("opt_open"):
            m2 = OPTSTART.match(t)
            if m2 and _opt_letter(m2) == chr(ord(cur["opt_open"]) + 1):
                _close_opt(cur)
                cur["opt_open"] = _opt_letter(m2)
                cur["opt_buf"] = [m2.group(4)] if m2.group(4) else []
            else:
                cur["opt_buf"].append(t)
            continue
        if _take_opts(t, cur):
            continue
        # 图片选项行：整行只有 "A B C D"，选项内容在图上
        if not cur["opts"] and IMG_OPT_LINE.match(t.strip()):
            for L in re.findall(r'[A-D]', t.strip()):
                cur["opts"].append((L, ""))
            continue
        m1 = OPTSTART.match(t)
        if m1 and not cur["opts"] and _opt_letter(m1) == 'A':
            cur["opt_open"] = 'A'
            cur["opt_buf"] = [m1.group(4)] if m1.group(4) else []
            continue
        cur["stem"].append(t)

    if cur:
        _close_opt(cur)
        qs.append(cur)

    # 插图归属：图归属于其上方最近的题号（跨页时归属上页最后一题）
    for q in qs:
        q["figbox"] = []
    anchors = {}
    for q in qs:
        anchors.setdefault(q["p"], []).append((q.get("y0", 0), q))
    for pno, zones in fig_boxes.items():
        if not zones:
            continue
        for z in zones:
            cy = (z[1] + z[3]) / 2
            cand = None
            same = [a for a in anchors.get(pno, []) if a[0] <= cy + 5]
            if same:
                cand = max(same, key=lambda a: a[0])[1]
            else:
                prev = [pp for pp in anchors if pp < pno]
                if prev:
                    pp = max(prev)
                    lst = anchors[pp]
                    if lst:
                        cand = max(lst, key=lambda a: a[0])[1]
            if cand is None:
                allq = [a for lst in anchors.values() for a in lst]
                if allq:
                    cand = min(allq, key=lambda a: a[0])[1]
            if cand is not None:
                cand["figbox"].append((z[0], z[1], z[2], z[3], pno))
    return doc, qs, fig_boxes


def extract_answer(ana, is_choice):
    if not ana:
        return ""
    if is_choice:
        for pat in ANS_PAT:
            ms = pat.findall(ana)
            if ms and 1 <= len(ms[-1]) <= 4:
                return ms[-1]
        return ""
    # 图像选项题：解析以「故选X」结尾
    for pat in ANS_PAT:
        ms = pat.findall(ana)
        if ms and re.fullmatch(r'[A-D]{1,4}', ms[-1]):
            return ms[-1]
    parts = []
    marks = list(SUBQ.finditer(ana))
    if marks:
        for i, m in enumerate(marks):
            seg = ana[m.end(): marks[i + 1].start() if i + 1 < len(marks) else len(ana)]
            r = _seg_result(seg)
            if r:
                parts.append(f"（{m.group(1)}）{r}")
    if not parts:
        r = _seg_result(ana)
        if r:
            parts.append(r)
    parts = [re.sub(r'^选\s*([A-D])\s*$', r'\1', x) for x in parts]
    return "　".join(parts)


# ---------- LaTeX 片段渲染（供纯文本场景使用） ----------
def _parse_frac(s, i):
    i += len("\\frac")

    def grab(j):
        while j < len(s) and s[j] != "{":
            j += 1
        if j >= len(s):
            return None, j
        depth = 0
        k = j
        while k < len(s):
            if s[k] == "{":
                depth += 1
            elif s[k] == "}":
                depth -= 1
                if depth == 0:
                    return s[j + 1:k], k + 1
            k += 1
        return None, j

    num, i = grab(i)
    den, i = grab(i)
    return num, den, i


def render_tex(t):
    """把 \\frac{a}{b} 渲染为可读文本 (a)/(b)"""
    out = []
    i = 0
    while i < len(t):
        if t.startswith("\\frac", i):
            n, d, j = _parse_frac(t, i)
            if n is not None and d is not None:
                out.append("(" + n + ")/(" + d + ")")
                i = j
                continue
        out.append(t[i])
        i += 1
    s = "".join(out)
    s = re.sub(r'\$\^\{([^{}]*)\}\$', r'^\1', s)
    s = re.sub(r'\$_\{([^{}]*)\}\$', r'_\1', s)
    s = s.replace("$", "")
    s = re.sub(r"(\S)([A-D][.．])", r"\1 \2", s)
    s = re.sub(r"([）)])(?=[^\s])", r"\1 ", s)
    return re.sub(r"\s+", " ", s).strip()


def split_frac(text):
    """把文本按 \\frac{...}{...} 切成片段列表：[('t', 文本) | ('f', 分子, 分母)]"""
    out = []
    i = 0
    buf = []
    while i < len(text):
        # ---- cases 分段函数（人工录入用）----
        # 段类型 C：内容是 cases 环境的整段源码，
        # 由 make_paper 的 omml_segs 转成 OMML <m:d>（矩阵）。
        if text.startswith("\\\\begin", i):
            _m = re.match(r"\\\\begin\s*\{([a-zA-Z*]+)\}", text[i:])
            if _m:
                _env = _m.group(1)
                _end = "\\\\end{" + _env + "}"
                _k2 = text.find(_end, i + _m.end())
                if _k2 < 0:
                    _k2 = len(text)
                _body = text[i + _m.end():_k2]
                if buf:
                    out.append(("t", "".join(buf))); buf = []
                out.append(("C", _body, _env))
                i = _k2 + len(_end)
                continue

        if text.startswith("\\frac", i):
            n, d, j = _parse_frac(text, i)
            if n is not None and d is not None:
                if buf:
                    out.append(("t", "".join(buf)))
                    buf = []
                out.append(("f", n, d))
                i = j
                continue
        buf.append(text[i])
        i += 1
    if buf:
        out.append(("t", "".join(buf)))
    return out


# ---------- 根号归并 ----------
SQ = "\u221a"
# 行尾为根号，或被开方数紧跟在根号后
SQ_SPLIT = re.compile(r'(?:' + SQ + r'|[\u221a])\s*([0-9A-Za-z\u0391-\u03c9]{1,2})(?![0-9A-Za-z])')


def merge_sqrt(text):
    """把「2 √ 3」「√ 3」归并成 LaTeX 根号：2 \\sqrt{3} / \\sqrt{3}"""
    def _r(m):
        inner = m.group(1)
        # 根号前若是数字/字母，中间不加空格（如 2√3）
        return "\\sqrt{" + inner + "}"
    t = SQ_SPLIT.sub(_r, text)
    t = t.replace(SQ, "")          # 残留的孤立根号
    return t


def merge_script(segs):
    """把 ('t',基底) + 上下标 合并成 msub / msup / msubsup。

    split_rich 产出扁平序列，上下标段单独存在会丢失基底
    （a_{n+1} 被切成文本「a」+ 下标「n+1」），必须合成 MathML 节点。

    两段式：
      1. 连续的 u（下标）/ w（上标）合并成一个 ('x', sub, sup)
      2. 与紧邻的前一个字符合成基底
         - 只有下标 → ('m', base, sub)
         - 只有上标 → ('p', base, sup)
         - 两者都有 → ('sp', base, sub, sup)  → <msubsup>
    """
    import re as _re

    # 1) 合并连续的上/下标段
    tmp, i, n = [], 0, len(segs)
    while i < n:
        if segs[i][0] in ('u', 'w'):
            sub, sup = '', ''
            j = i
            while j < n and segs[j][0] in ('u', 'w'):
                if segs[j][0] == 'u':
                    sub = segs[j][1] + sub
                else:
                    sup = segs[j][1] + sup
                j += 1
            tmp.append(('x', sub, sup))
            i = j
        else:
            tmp.append(segs[i])
            i += 1

    # 2) 与前一个字符合成基底
    out = []
    for sg in tmp:
        if sg[0] == 'x' and out and out[-1][0] == 't' and out[-1][1]:
            prev = out[-1][1]
            base = None
            # **优先匹配函数名**：``log_{2}`` 的基底是整个 log，
            # 不是最后一个字母 g。
            # 原来只取末尾单个字符，于是 \log_{\frac{1}{2}} 被切成
            # 文本「lo」+ 下标「g」，页面上显示成 lo ᵍ —— 完全读不通。
            try:
                from mathml import FUNCS as _F
                fm = _re.search(r'([A-Za-z]+)$', prev)
                if fm and fm.group(1) in _F:
                    base = fm.group(1)
            except Exception:
                pass
            if base is None:
                # **数字串整体作为基底**：``90^{\circ}`` 的基底是 90，
                # 不是末尾的 0。只取单字符的话会切成文本「9」+ 上标「0°」，
                # Word 里显示成 9 0° —— 度数符号跑到了 0 头上。
                m = _re.search(r'(\d+)$', prev)
                base = m.group(1) if m else None
            if base is None and prev and prev[-1] in ')]':
                # **括号组整体作为基底**：``(x-1)^2`` 的基底是 ``(x-1)``。
                # 闭括号不是字母也不是数字，前面三条规则全部落空，
                # 于是 base=None，上下标段被原样丢弃 ——
                # Word 里 ``(x-1)^2+(y-1)^2=1`` 的平方**整个消失**，
                # 而且不报错（页面只显示 (x-1)+(y-1)=1）。
                # 高中数学里这类型号极其常见，必须支持。
                depth = 0
                k = len(prev) - 1
                while k >= 0:
                    ch = prev[k]
                    if ch in ')]':
                        depth += 1
                    elif ch in '([':
                        depth -= 1
                        if depth == 0:
                            break
                    k -= 1
                if depth == 0 and k >= 0:
                    base = prev[k:]
            if base is None:
                m = _re.search(r'([A-Za-z\u0370-\u03ff])$', prev)
                base = m.group(1) if m else None
            if base is None:
                # **兜底：单个非空白字符做基底**。
                # ``\complement_U A`` 里 ∁（U+2201）既不是字母、数字，
                # 也不是括号或函数名 —— 上面四条规则全部落空，
                # base=None → 段留在 ('x', sub, sup) 状态 →
                # 渲染层没有 'x' 分支 → **下标 U 直接消失且不报错**
                # （页面显示 ∁ A，补集符号丢了全集标记）。
                # 补集符号、∅、∞ 等数学符号都可能带上下标，必须兜住。
                #
                # 只取紧邻的单个字符，且要求不是空白 ——
                # 空白后面跟 _{} 说明是孤立下标，不该硬凑基底。
                m = _re.search(r'(\S)$', prev)
                base = m.group(1) if m else None
            if base:
                out[-1] = ('t', prev[:len(prev) - len(base)])
                if sg[1] and sg[2]:
                    out.append(('sp', base, sg[1], sg[2]))
                elif sg[1]:
                    out.append(('m', base, sg[1]))
                else:
                    out.append(('p', base, sg[2]))
                continue
        out.append(sg)
    return out


def merge_sub(segs):
    """向后兼容别名：旧代码 import merge_sub 仍可用。"""
    return merge_script(segs)


def split_rich(text):
    """把文本切成片段

    类型：('t',文本) | ('f',分子,分母) | ('s',被开方数)
          | ('m',基底,下标) | ('p',基底,上标) | ('sp',基底,下,上)
          | ('L', LaTeX源码)   ← 人工录入的 $...$ 通用公式
                                 （不能用 'x'：渲染层已用它表示待合并的上下标）
    """
    out = []
    i = 0
    buf = []
    while i < len(text):
        # $...$ 通用 LaTeX（人工录入用）。
        # 必须放在最前面：$ 不会与后面任何模式冲突，
        # 而且它内部的内容要整体交给 latex_inline，
        # 不能被 frac / sqrt 的分支提前截走。
        #
        # ---- cases 分段函数（人工录入用）----
        # 段类型 C：内容是 cases 环境的整段源码，
        # 由 make_paper 的 omml_segs 转成 OMML <m:d>（矩阵）。
        # 必须在 frac 之前：cases 内部含换行与 &，
        # 落入其他分支会被拆碎。
        if text.startswith("\\begin", i):
            _m = re.match(r"\\begin\s*\{([a-zA-Z*]+)\}", text[i:])
            if _m:
                _env = _m.group(1)
                _end = "\\end{" + _env + "}"
                _k2 = text.find(_end, i + _m.end())
                if _k2 < 0:
                    _k2 = len(text)
                _body = text[i + _m.end():_k2]
                if buf:
                    out.append(("t", "".join(buf))); buf = []
                out.append(("C", _body, _env))
                i = _k2 + len(_end)
                continue
        if text[i] == "$":
            j = text.find("$", i + 1)
            if j > i + 1:
                if buf:
                    out.append(("t", "".join(buf))); buf = []
                out.append(("L", text[i + 1:j]))
                i = j + 1
                continue
            # 未配对的 $ 当普通字符，避免吞掉后面所有内容
        # ---- 向量 / 上划线 / 粗体（人工录入用）----
        # 段类型：V=向量箭头  O=上划线  H=帽号  B=粗体
        # 第三项存命令名，渲染层据此选箭头方向。
        # 这些命令在 latex_expand 里被 _KEEP 保留，
        # 所以 Word 端走到这里时仍是 \overrightarrow{CA} 原形。
        #
        # 必须放在 `_` 分支之前：否则 \vec 之类虽无下划线，
        # 但未来若加入含下划线的命令会先被下标逻辑截走。
        _hit = None
        for _cmd, _tag in (("\\overrightarrow", "V"),
                           ("\\overleftarrow", "V"),
                           ("\\overleftrightarrow", "V"),
                           ("\\vec", "V"),
                           ("\\overline", "O"),
                           ("\\hat", "H"),
                           ("\\boldsymbol", "B"),
                           ("\\pmb", "B")):
            if text.startswith(_cmd, i):
                _hit = (_cmd, _tag)
                break
        if _hit is not None:
            _cmd, _tag = _hit
            j = i + len(_cmd)
            while j < len(text) and text[j] == " ":
                j += 1
            if j < len(text) and text[j] == "{":
                depth = 0; k = j
                while k < len(text):
                    if text[k] == "{": depth += 1
                    elif text[k] == "}":
                        depth -= 1
                        if depth == 0: break
                    k += 1
                if k < len(text):
                    if buf:
                        out.append(("t", "".join(buf))); buf = []
                    out.append((_tag, text[j + 1:k], _cmd))
                    i = k + 1
                    continue
        if text.startswith("\\frac", i):
            n, d, j = _parse_frac(text, i)
            if n is not None and d is not None:
                if buf:
                    out.append(("t", "".join(buf))); buf = []
                out.append(("f", n, d)); i = j; continue
        if text.startswith("\\sqrt", i):
            j = i + len("\\sqrt")
            while j < len(text) and text[j] != "{":
                j += 1
            if j >= len(text):
                buf.append(text[i]); i += 1; continue
            depth = 0; k = j
            while k < len(text):
                if text[k] == "{": depth += 1
                elif text[k] == "}":
                    depth -= 1
                    if depth == 0: break
                k += 1
            inner = text[j + 1:k]
            if buf:
                out.append(("t", "".join(buf))); buf = []
            out.append(("s", inner)); i = k + 1; continue
        if text[i] == "^" and i + 1 < len(text) and text[i + 1] == "{":
            # 上标 x^{2}：先切出 ('w', 内容)，
            # 随后由 merge_script() 与前面的基底合并成 <msup>。
            j = i + 1
            depth = 0; k = j
            while k < len(text):
                if text[k] == "{": depth += 1
                elif text[k] == "}":
                    depth -= 1
                    if depth == 0: break
                k += 1
            if k < len(text):
                if buf:
                    out.append(("t", "".join(buf))); buf = []
                out.append(("w", text[j + 1:k])); i = k + 1; continue
        if text[i] == "_" and i + 1 < len(text) and text[i + 1] == "{":
            # 下标 a_{n+1}：先切出 ('u', 内容)，
            # 随后由 merge_sub() 与前面的基底合并成 ('m', 基底, 下标)。
            j = i + 1
            depth = 0; k = j
            while k < len(text):
                if text[k] == "{": depth += 1
                elif text[k] == "}":
                    depth -= 1
                    if depth == 0: break
                k += 1
            if k < len(text):
                if buf:
                    out.append(("t", "".join(buf))); buf = []
                out.append(("u", text[j + 1:k])); i = k + 1; continue
        buf.append(text[i]); i += 1
    if buf:
        out.append(("t", "".join(buf)))
    return out
