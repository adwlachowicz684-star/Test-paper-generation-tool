# -*- coding: utf-8 -*-
"""按高考卷版式生成试卷 + 答案与解析卷

架构：每种题型是一个独立的「矩形模块」，模块内部格式由
paper_template.py 的配置驱动。整卷 = 模块按顺序垒起来。
"""
import sys, os, json, re, glob, subprocess

# 路径基于 __file__ 推导。硬编码 /data/workspace 在 Windows 上会直接 import 失败。
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract3 import extract, extract_answer, split_rich, merge_sqrt
from gkbank import (crop_figs, strip_tail_blank, split_leaked_opts, normalize_tail_blank, mark_subscripts)
import paper_template as T

# 切片根目录，与 py/main.py、py/build_html.py 保持同源
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLICE = os.path.join(ROOT, 'src', 'slices')
OUT = os.path.join(ROOT, 'out')

from docx import Document
from docx.table import _Cell
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_UNDERLINE
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement, parse_xml

M_NS = 'http://schemas.openxmlformats.org/officeDocument/2006/math'
W_NS = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
NO_SPACE_BEFORE = '，。；：、）】》！？’”…—·'
NO_SPACE_AFTER = '（【《‘“'


def _is_cjk(ch):
    o = ord(ch)
    return (0x4E00 <= o <= 0x9FFF or 0x3000 <= o <= 0x303F
            or 0xFF00 <= o <= 0xFFEF)


def join_text(parts):
    s = ''
    for p in (x.strip() for x in parts):
        if not p:
            continue
        if not s:
            s = p
            continue
        a, b = s[-1], p[0]
        if b in NO_SPACE_BEFORE or a in NO_SPACE_AFTER:
            s += p
        elif _is_cjk(a) and _is_cjk(b):
            s += p
        else:
            s += ' ' + p
    return s


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


# ---------------- OMML 公式 ----------------
def _mrun(txt, size=21, italic=True):
    """单个 OMML 公式 run。

    **必须显式写 `<m:sty>`** —— 这是本函数最容易踩的坑：

    OMML 数学区里 `<m:t>` 的**默认字体是斜体**，即使 run 里没有
    `<m:i/>` 也一样。所以区间 `(0,1)`、函数名 `f` 会全部显示成斜体，
    而且从 XML 上看不出任何问题（没有斜体标记却渲染成斜体）。

    正体要写 `<m:sty m:val="p"/>`，斜体写 `<m:sty m:val="i"/>`，
    两者都不能省略。
    """
    sty = '<m:sty m:val="i"/>' if italic else '<m:sty m:val="p"/>'
    it = '<m:i/>' if italic else ''
    return ('<m:r><m:rPr><m:rFonts m:ascii="%s" m:hAnsi="%s"/>'
            '%s%s<m:sz m:val="%d"/><m:szCs m:val="%d"/>'
            '</m:rPr><m:t>%s</m:t></m:r>') % (
        T.FONT["math"], T.FONT["math"], it, sty, size, size, esc(txt))


def _plain_runs(txt, size=21, italic=True, up=()):
    """把纯文本按「正体 / 斜体」拆成多个 OMML run。

    原来整段文本只有一个 run，于是 `f(x)` 里的 f 和 x 用同一种字体，
    而 `(0,1)` 会因为「数学区默认斜体」整体变斜。
    拆开后：函数名与括号数字正体、变量斜体。
    """
    if not txt:
        return _mrun('', size, italic)
    try:
        from mathml import split_math_style
        segs = split_math_style(txt, up)
    except Exception:
        return _mrun(txt, size, italic)
    if not segs:
        return _mrun(txt, size, italic)
    return ''.join(_mrun(s, size, not upright) for s, upright in segs)


def _trim_math_arg(s):
    """去掉参数尾部多余的分隔符。

    PDF 提取时根号后紧跟的逗号常被误吞进花括号：
        半径为 √2 的圆锥 → ``\sqrt{2,}``
    不清理的话 Word 里就显示成 √(2,)。
    """
    import re as _re
    return _re.sub(r'[,，]$', '', str(s if s is not None else '').strip()).strip()


def _omml_cases(body, size=21, italic=True, up=()):
    """cases 环境 → OMML <m:d>（带左花括号的矩阵）。

    OMML 没有 cases 环境，用「分隔符为 { 的矩阵」实现：
    每行 <m:mr>，每格 <m:e>。

    **必须同时被 _minner 与 omml_segs 调用** ——
    两者都遍历段列表，只加一处会漏掉顶层或嵌套的情况
    （这个坑已经踩过三次：向量、粗体、cases）。
    """
    # 先把行/列解析出来，两条渲染路径共用
    parsed = []
    for line in body.split('\\\\'):
        line = line.strip()
        if not line:
            continue
        parsed.append([c.strip() for c in line.split('&')])

    # 降级路径：左大括号 + 每行一组 run。
    # 标准 <m:d> 在个别 Word 版本 / 兼容模式下会「括号在、内容空白」，
    # 且完全不报错。这时把 T.CASES_MODE 改成 "text" 即可绕过。
    if T.CASES_MODE == 'text':
        out = [_mrun('{', size, italic)]
        for ri, cells in enumerate(parsed):
            if ri:
                out.append(_mrun(' ', size, italic))
            out.append(_minner('  '.join(cells), size, italic, up))
        return ''.join(out)

    rows = []
    ncol = max((len(c) for c in parsed), default=1)
    for cells in parsed:
        cs = ''.join('<m:e>%s</m:e>'
                     % _minner(c, size, italic, up) for c in cells)
        if cs:
            rows.append('<m:mr>%s</m:mr>' % cs)

    # dPr 的四个注意点（全是踩过的坑）：
    #   1. **不能用 &#0;**：XML 1.0 不允许空字符的字符引用，
    #      parse_xml 抛异常 → omml_math 返回 None → 整个公式静默消失。
    #   2. **sepChr 必须是空**：它是「行内列分隔符」，
    #      写成 &#124;(|) 会在「表达式」和「条件」之间插一根竖线。
    #   3. **不能有 m:algn** —— CT_DPr 的 sequence 只有
    #      begChr/sepChr/endChr/grow/shp/ctrlPr，**没有 algn**。
    #      放进去就是非法结构，Word 会「括号在、内容空白」且不报错。
    #      列对齐要写在 m:mcPr 的 m:mcJc 里。
    #   4. m:grow="on"（ST_OnOff 标准值）、m:shp="match" 不能省。
    #
    # **m:e 里必须包一层 m:m（矩阵）** —— 直接放 m:mr 的话，
    # Word 同样表现为「大括号在、里边的分段全空白」。
    # m:m 里要有 m:mPr > m:mcs > m:mc，列数与列对齐在这里声明。
    return ('<m:d><m:dPr>'
            '<m:begChr m:val="&#123;"/>'
            '<m:sepChr m:val=""/>'
            '<m:endChr m:val=""/>'
            '<m:grow m:val="on"/>'
            '<m:shp m:val="match"/>'
            '</m:dPr><m:e><m:m><m:mPr><m:mcs><m:mc><m:mcPr>'
            '<m:count m:val="%d"/><m:mcJc m:val="left"/>'
            '</m:mcPr></m:mc></m:mcs></m:mPr>%s</m:m></m:e></m:d>'
            % (ncol, ''.join(rows)))


def _minner(s, size=21, italic=True, up=()):
    """参数内容 → OMML 内部片段（不含外层 <m:oMath>）。

    **必须递归**：``\frac{\sqrt{3}}{2}`` 的分子本身是根号，
    不递归的话分子会被当成普通文本 run，
    Word 里就显示成源码 ``\sqrt{3}`` —— 正是要修的问题。
    """
    from extract3 import split_rich, merge_script
    t = _trim_math_arg(s)
    if not t:
        return _mrun('', size, italic)

    segs = merge_script(split_rich(t))
    # 'C'（cases）必须在列表里 —— 漏了的话，嵌在 rac 等结构里的
    # cases 会被判为"无公式"，整段走 _plain_runs 变成纯文本源码。
    if not any(g[0] in ('f', 's', 'm', 'p', 'sp', 'L', 'C') for g in segs):
        return _plain_runs(t, size, italic, up)

    out = []
    for g in segs:
        if g[0] == 'L':
            # 人工录入的 $...$ 通用公式。
            # 复用「先转内部片段、再包 OMML」的路径：
            # $ 内部若含 \frac/\sqrt/上下标，由 omml_segs 递归处理；
            # 纯符号（\mathbb{R}、\le 等）落到 _mrun 输出字符。
            out.append(omml_latex(g[1], size, italic, up))
        elif g[0] == 't':
            if g[1]:
                out.append(_plain_runs(g[1], size, italic, up))
        elif g[0] == 'f':
            out.append('<m:f><m:fPr><m:type m:val="bar"/></m:fPr>'
                       '<m:num>%s</m:num><m:den>%s</m:den></m:f>'
                       % (_minner(g[1], size, italic, up),
                          _minner(g[2], size, italic, up)))
        elif g[0] == 'C':
            out.append(_omml_cases(g[1], size, italic, up))
        elif g[0] in ('V', 'O', 'H'):
            # 向量箭头 / 上划线 / 帽号：OMML 用 <m:acc>（在上加字符）
            # 或 <m:bar>（上划线）。
            # 缺了这些分支，段会被忽略，Word 里整段内容消失。
            _chr = {'\\overrightarrow': '\u2192',
                    '\\overleftarrow': '\u2190',
                    '\\overleftrightarrow': '\u2194',
                    '\\vec': '\u20d7',
                    '\\overline': '\u00af',
                    '\\hat': '\u005e'}.get(g[2], '\u2192')
            body = _minner(g[1], size, italic, up)
            if g[0] == 'O':
                out.append('<m:bar><m:barPr><m:pos m:val="top"/></m:barPr>'
                           '<m:e>%s</m:e></m:bar>' % body)
            else:
                out.append('<m:acc><m:accPr><m:chr m:val="%s"/></m:accPr>'
                           '<m:e>%s</m:e></m:acc>' % (_chr, body))
        elif g[0] == 'B':
            # 粗体（\boldsymbol）：OMML 用 <m:b/> 在 run 属性里
            _bi = '<m:b/>'
            out.append(_minner(g[1], size, italic, up).replace(
                '<m:sz m:val=', _bi + '<m:sz m:val='))
        elif g[0] == 's':
            out.append('<m:rad><m:radPr><m:degHide m:val="1"/></m:radPr>'
                       '<m:deg/><m:e>%s</m:e></m:rad>'
                       % _minner(g[1], size, False, up))
        elif g[0] == 'm':
            # 下标 a_{n+1} → <m:sSub><m:e>基底</m:e><m:sub>下标</m:sub></m:sSub>
            out.append('<m:sSub><m:e>%s</m:e><m:sub>%s</m:sub></m:sSub>'
                       % (_minner(g[1], size, True, up), _minner(g[2], size, False, up)))
        elif g[0] == 'p':
            # 上标 x^{2} → <m:sSup><m:e>基底</m:e><m:sup>上标</m:sup></m:sSup>
            out.append('<m:sSup><m:e>%s</m:e><m:sup>%s</m:sup></m:sSup>'
                       % (_minner(g[1], size, True, up), _minner(g[2], size, False, up)))
        elif g[0] == 'sp':
            # 同时有上下标 → <m:sSubSup>（顺序：e, sub, sup）
            out.append('<m:sSubSup><m:e>%s</m:e><m:sub>%s</m:sub>'
                       '<m:sup>%s</m:sup></m:sSubSup>'
                       % (_minner(g[1], size, True, up), _minner(g[2], size, False, up),
                          _minner(g[3], size, False, up)))
    return ''.join(out)


def omml_latex(src, size=21, italic=False, up=()):
    """人工录入的 LaTeX → Word 原生公式（OMML）

    与 HTML 端 latex_inline() 规则一致：先展开宏为 Unicode，
    再把 \frac / \sqrt / 上下标转成 OMML 结构。
    这样 Word 里双击公式仍可编辑。
    """
    import extract3 as _E
    # 先展开宏（\mathbb{R} -> ℝ、\le -> ≤、x_1 -> x_{1}），
    # 再走 split_rich 解析 \frac/\sqrt/上下标结构。
    # 顺序不能反：split_rich 不认 \mathbb 这类宏，
    # 直接喂会原样输出 "\mathbb{R}" 这样的源码文本。
    # 数集（\mathbb{R}）必须正体，但 latex_expand 会把它展开成普通的 R，
    # 「这是数集」的信息就丢了 —— 所以展开**之前**先把字母记下来，
    # 作为 force_upright 传给切分函数。
    # 注意正则里的反斜杠层数：raw string 里写 \\s 会被正则当成
    # 「字面反斜杠 + 字母 s」，而不是 \s 空白类。
    # 曾因多写一层导致这里静默 except 掉，\mathbb{R} 被判成变量（斜体）。
    try:
        import re as _re2
        up = set(up) | {
            ch for m in _re2.finditer(
                r'\\(?:mathbb|mathbf)\s*\{([^{}]*)\}', src)
            for ch in m.group(1) if ch.isalpha()}
    except Exception:
        pass
    try:
        from mathml import latex_expand
        src = latex_expand(src)
    except Exception:
        pass
    segs = _E.merge_script(_E.split_rich(src))
    return omml_segs(segs, size, italic, up)


def omml_segs(segs, size=21, italic=False, up=()):
    """片段列表 → OMML（omml_latex 与内部递归共用）"""
    out = []
    for g in segs:
        if g[0] == 't':
            if g[1]:
                out.append(_plain_runs(g[1], size, italic, up))
        elif g[0] == 'L':
            out.append(omml_segs(_E_merge(g[1]), size, italic, up))
        elif g[0] == 'C':
            # 顶层（非嵌套）的 cases 段。
            # **这一处不能省**：omml_segs 与 _minner 是两个独立函数，
            # 各自遍历段列表。只在 _minner 里加分支的话，
            # 顶层的 C 段（最常见的情况）不会被处理。
            out.append(_omml_cases(g[1], size, italic, up))
        elif g[0] == 'f':
            out.append('<m:f><m:fPr><m:type m:val="bar"/></m:fPr>'
                       '<m:num>%s</m:num><m:den>%s</m:den></m:f>'
                       % (_minner(g[1], size, italic, up),
                          _minner(g[2], size, italic, up)))
        elif g[0] in ('V', 'O', 'H'):
            # 向量箭头 / 上划线 / 帽号：OMML 用 <m:acc>（在上加字符）
            # 或 <m:bar>（上划线）。
            # 缺这些分支时段落被静默丢弃 —— Word 里整段内容消失且不报错。
            _chr = {'\\overrightarrow': '→',
                    '\\overleftarrow': '←',
                    '\\overleftrightarrow': '↔',
                    '\\vec': '⃗',
                    '\\overline': '‾',
                    '\\hat': '^'}.get(g[2], '→')
            body = _minner(g[1], size, italic, up)
            if g[0] == 'O':
                out.append('<m:bar><m:barPr><m:pos m:val="top"/></m:barPr>'
                           '<m:e>%s</m:e></m:bar>' % body)
            else:
                out.append('<m:acc><m:accPr><m:chr m:val="%s"/></m:accPr>'
                           '<m:e>%s</m:e></m:acc>' % (_chr, body))
        elif g[0] == 'B':
            # 粗体（\boldsymbol）：OMML 在 run 属性里加 <m:b/>
            out.append(_minner(g[1], size, italic, up).replace(
                '<m:sz m:val=', '<m:b/><m:sz m:val='))
        elif g[0] == 's':
            out.append('<m:rad><m:radPr><m:degHide m:val="1"/></m:radPr>'
                       '<m:deg/><m:e>%s</m:e></m:rad>'
                       % _minner(g[1], size, False, up))
        elif g[0] == 'm':
            out.append('<m:sSub><m:e>%s</m:e><m:sub>%s</m:sub></m:sSub>'
                       % (_minner(g[1], size, True, up), _minner(g[2], size, False, up)))
        elif g[0] == 'p':
            out.append('<m:sSup><m:e>%s</m:e><m:sup>%s</m:sup></m:sSup>'
                       % (_minner(g[1], size, True, up), _minner(g[2], size, False, up)))
        elif g[0] == 'sp':
            out.append('<m:sSubSup><m:e>%s</m:e><m:sub>%s</m:sub>'
                       '<m:sup>%s</m:sup></m:sSubSup>'
                       % (_minner(g[1], size, True, up), _minner(g[2], size, False, up),
                          _minner(g[3], size, False, up)))
    return ''.join(out)


def _E_merge(src):
    from extract3 import split_rich, merge_script
    return merge_script(split_rich(src))


def omml_frac(num, den):
    xml = ('<m:oMath xmlns:m="%s" xmlns:w="%s">'
           '<m:f><m:fPr><m:type m:val="bar"/></m:fPr>'
           '<m:num>%s</m:num><m:den>%s</m:den></m:f></m:oMath>') % (
        M_NS, W_NS, _minner(num), _minner(den))
    return parse_xml(xml)


def omml_sqrt(inner):
    xml = ('<m:oMath xmlns:m="%s" xmlns:w="%s">'
           '<m:rad><m:radPr><m:degHide m:val="1"/></m:radPr>'
           '<m:deg/><m:e>%s</m:e></m:rad></m:oMath>') % (
        M_NS, W_NS, _minner(inner, italic=False))
    return parse_xml(xml)




def omml_sub(base, sub_txt):
    """下标 → Word 原生公式（可双击编辑）"""
    xml = ('<m:oMath xmlns:m="%s" xmlns:w="%s">'
           '<m:sSub><m:e>%s</m:e><m:sub>%s</m:sub></m:sSub>'
           '</m:oMath>') % (M_NS, W_NS, _minner(base), _minner(sub_txt, italic=False))
    return parse_xml(xml)


def omml_sup(base, sup_txt):
    """上标 → Word 原生公式（可双击编辑）"""
    xml = ('<m:oMath xmlns:m="%s" xmlns:w="%s">'
           '<m:sSup><m:e>%s</m:e><m:sup>%s</m:sup></m:sSup>'
           '</m:oMath>') % (M_NS, W_NS, _minner(base), _minner(sup_txt, italic=False))
    return parse_xml(xml)

# ---------------- 基础排版 ----------------
def R(p, text, size=10.5, bold=False, color=None, cn=None, italic=False):
    r = p.add_run(text)
    r.font.size = Pt(size)
    r.bold = bold
    r.italic = italic
    r.font.name = T.FONT["en"]
    r._element.rPr.rFonts.set(qn('w:eastAsia'), cn or T.FONT["cn"])
    if color:
        r.font.color.rgb = RGBColor(*color)
    return r


def omml_subsup(base, sub_txt, sup_txt):
    """同时有上下标 → <m:sSubSup>（顺序：e, sub, sup）"""
    xml = ('<m:oMath xmlns:m="%s" xmlns:w="%s">'
           '<m:sSubSup><m:e>%s</m:e><m:sub>%s</m:sub>'
           '<m:sup>%s</m:sup></m:sSubSup></m:oMath>') % (
        M_NS, W_NS, _minner(base), _minner(sub_txt, 18), _minner(sup_txt, 18))
    return parse_xml(xml)


def omml_math(src, size=21):
    """人工录入的 $...$ 公式 → Word 原生公式元素

    先宏展开（\\mathbb{R}→ℝ、x_1→x_{1}），再转 OMML 结构。
    这样在 Word 里双击仍可编辑，不是图片。
    """
    inner = omml_latex(src, size)
    if not inner:
        return None
    xml = ('<m:oMath xmlns:m="%s" xmlns:w="%s">%s</m:oMath>'
           % (M_NS, W_NS, inner))
    try:
        return parse_xml(xml)
    except Exception:
        return None


def rich(p, text, size=10.5, bold=False, color=None):
    """写入文本，\\frac{}{} / \\sqrt{} / _{} / $...$ 渲染为 Word 原生公式"""
    from extract3 import merge_script
    for seg in merge_script(split_rich(text)):
        if seg[0] == 't':
            if seg[1]:
                R(p, seg[1], size, bold, color)
        elif seg[0] == 'L':
            # 人工录入的 $...$ 通用公式。
            # 缺这个分支时公式会被**静默丢弃** ——
            # 页面上看到「定义在  上的奇函数」，中间空一块，
            # 而且没有任何报错，极难发现。
            el = omml_math(seg[1])
            if el is not None:
                p._p.append(el)
        elif seg[0] == 'f':
            p._p.append(omml_frac(seg[1], seg[2]))
        elif seg[0] == 's':
            p._p.append(omml_sqrt(seg[1]))
        elif seg[0] == 'm':
            p._p.append(omml_sub(seg[1], seg[2]))
        elif seg[0] == 'p':
            p._p.append(omml_sup(seg[1], seg[2]))
        elif seg[0] == 'sp':
            p._p.append(omml_subsup(seg[1], seg[2], seg[3]))


def P(doc, before=0, after=3, indent=0, align=None, line=1.4):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    pf.line_spacing = line
    if indent:
        pf.left_indent = Cm(indent)
    if align:
        p.alignment = align
    return p


def setup(doc):
    s = doc.sections[0]
    s.page_width, s.page_height = Cm(T.PAGE["width"]), Cm(T.PAGE["height"])
    s.left_margin = s.right_margin = Cm(T.PAGE["margin_lr"])
    s.top_margin = s.bottom_margin = Cm(T.PAGE["margin_tb"])
    st = doc.styles['Normal']
    st.font.name = T.FONT["en"]
    st.font.size = Pt(T.SIZE["stem"])
    st.element.rPr.rFonts.set(qn('w:eastAsia'), T.FONT["cn"])
    st.paragraph_format.line_spacing = T.STEM["line"]
    st.paragraph_format.space_after = Pt(2)


def hr(doc, color="2E75B6", sz=12, after=6):
    p = P(doc, after=after)
    pPr = p._p.get_or_add_pPr()
    b = OxmlElement('w:pBdr')
    bt = OxmlElement('w:bottom')
    bt.set(qn('w:val'), 'single')
    bt.set(qn('w:sz'), str(sz))
    bt.set(qn('w:space'), '1')
    bt.set(qn('w:color'), color)
    b.append(bt)
    pPr.append(b)
    return p


def no_borders(table):
    tblPr = table._tbl.tblPr
    bd = OxmlElement('w:tblBorders')
    for e in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        el = OxmlElement('w:' + e)
        el.set(qn('w:val'), 'none')
        el.set(qn('w:sz'), '0')
        bd.append(el)
    tblPr.append(bd)
    lay = OxmlElement('w:tblLayout')
    lay.set(qn('w:type'), 'fixed')
    tblPr.append(lay)


def set_cols(table, widths, allow_split=True):
    tbl = table._tbl
    grid = tbl.find(qn('w:tblGrid'))
    if grid is None:
        grid = OxmlElement('w:tblGrid')
        tbl.insert(0, grid)
    for gc in list(grid):
        grid.remove(gc)
    for w in widths:
        gc = OxmlElement('w:gridCol')
        gc.set(qn('w:w'), str(int(w * 567)))
        grid.append(gc)
    no_borders(table)
    for row in table.rows:
        trPr = row._tr.get_or_add_trPr()
        if allow_split:
            for tag in ('w:cantSplit', 'w:keepNext'):
                for old in trPr.findall(qn(tag)):
                    trPr.remove(old)
                el = OxmlElement(tag)
                el.set(qn('w:val'), '0')
                trPr.append(el)
        for i, c in enumerate(row.cells):
            if i < len(widths):
                c.width = Cm(widths[i])


def head_block(doc, title, sub, meta_rows):
    p = P(doc, after=T.TITLE["space_after"], align=WD_ALIGN_PARAGRAPH.CENTER)
    R(p, title, T.SIZE["title"], True, (0x1F, 0x38, 0x64), T.FONT["title"])
    p = P(doc, after=T.TITLE["sub_space_after"], align=WD_ALIGN_PARAGRAPH.CENTER)
    R(p, sub, T.SIZE["subtitle"], False, (0x44, 0x44, 0x44))
    hr(doc, sz=T.TITLE["rule_size"], after=T.TITLE["rule_space"])
    t = doc.add_table(rows=1, cols=2)
    t.style = 'Table Grid'
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for k, v in meta_rows:
        c = t.add_row().cells
        pa = c[0].paragraphs[0]
        pa.alignment = WD_ALIGN_PARAGRAPH.CENTER
        R(pa, k, T.SIZE["meta"], True)
        R(c[1].paragraphs[0], v, T.SIZE["meta"])
    set_cols(t, T.TITLE["meta_col_w"])
    t.rows[0]._element.getparent().remove(t.rows[0]._element)
    P(doc, after=6)


# ---------------- 插图 ----------------
def _fig_path(sub, fg):
    return os.path.join(SLICE, sub, fg['file'])


def _fig_size(sub, fg, maxw, maxh):
    from PIL import Image
    fp = _fig_path(sub, fg)
    if not os.path.exists(fp):
        return None
    try:
        iw, ih = Image.open(fp).size
    except Exception:
        return None
    w = min(maxw, iw / T.FIGURE["dpi"] * 2.54)
    h = w * ih / iw
    if h > maxh:
        h = maxh
        w = h * iw / ih
    return fp, w, h


def _fig_block_w(figs, cfg):
    n = len(figs)
    if n == 1:
        return cfg["w_single"]
    return min(cfg["w_multi_max"], cfg["w_multi_base"] + cfg["w_multi_step"] * n)


def _add_caption(container, text, width):
    cap = T.FIGURE["caption"]
    if not cap["show"] or not text:
        return
    p = container.add_paragraph() if hasattr(container, 'add_paragraph') else P(container)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(cap["space_after"])
    p.paragraph_format.line_spacing = 1.0
    if not isinstance(container, _Cell):      # cell 里的图注随表格走
        body_indent(p)
    R(p, text, cap["size"], False, cap["color"])


def _table_align(table, where="right"):
    """设置整个表格在页面中的水平位置（用于大题插图靠右）"""
    tblPr = table._tbl.tblPr
    jc = tblPr.find(qn('w:jc'))
    if jc is None:
        jc = OxmlElement('w:jc')
        tblPr.append(jc)
    jc.set(qn('w:val'), where)


def add_figs(container, figs, sub, maxw, cfg, qnum=None,
             align=WD_ALIGN_PARAGRAPH.CENTER):
    """插入图片（每行最多 per_row 张），可选图注"""
    if not figs:
        return
    cap = T.FIGURE["caption"]
    per_row = cfg["per_row"]
    if len(figs) == 1:
        sz = _fig_size(sub, figs[0], maxw, cfg["max_h"])
        if sz:
            fp, w, h = sz
            p = container.add_paragraph()
            p.alignment = align
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(1)
            if not isinstance(container, _Cell):
                body_indent(p)
            p.add_run().add_picture(fp, width=Cm(w))
        if cap["show"]:
            txt = cap["text"].format(n=1, q=qnum)
            _add_caption(container, txt, maxw)
        return
    n = len(figs)
    cols = min(per_row, n)
    rows = (n + cols - 1) // cols
    cw = maxw / cols
    t = container.add_table(rows=rows * (2 if cap["show"] else 1), cols=cols)
    if not isinstance(container, _Cell):      # 带图题的插图在 cell 里，不重复缩进
        table_indent(t)
    if align == WD_ALIGN_PARAGRAPH.RIGHT:
        _table_align(t, "right")
    elif align == WD_ALIGN_PARAGRAPH.LEFT:
        _table_align(t, "left")
    for i, fg in enumerate(figs):
        r, c = divmod(i, cols)
        cell = t.cell(r * (2 if cap["show"] else 1), c)
        cell.width = Cm(cw)
        pad = cfg.get("cell_pad", 0.25)
        sz = _fig_size(sub, fg, cw - pad, cfg["max_h"])
        if sz:
            fp, w, h = sz
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(1)
            p.add_run().add_picture(fp, width=Cm(w))
        if cap["show"]:
            cc = t.cell(r * 2 + 1, c)
            cc.width = Cm(cw)
            txt = cap["text_multi"].format(n=i + 1, q=qnum)
            _add_caption(cc, txt, cw)
    set_cols(t, [cw] * cols)


# ---------------- 选项 ----------------
def add_opts(container, opts, width, qnum=None, figs=None, sub=None):
    """选项模块：列宽固定，跨题对齐"""
    if not opts:
        return
    # 分列依据：**渲染宽度**，不是源码字符数。
    #
    # 这里曾有个双重错误：
    #   1. 正则只认 \frac|\sqrt，**不认 \dfrac** —— 于是 $\dfrac{4}{3}$
    #      整个按源码算成 15 字符，被误判成 2 列
    #   2. 即便认了，替换成 'xx' 也估得太短 —— $f(2017)<f(2018)<f(2019)$
    #      被算成 2 字符判 4 列，渲染时放不下被裁掉
    # 正确做法是按"渲染出来的视觉宽度"算：分数上下堆叠，
    # 宽度 = max(分子, 分母)。见 paper_template.render_width。
    lens = [T.render_width(t or '') for _, t in opts]
    cols = T.cols_for(max(lens) if lens else 0)
    rows = (len(opts) + cols - 1) // cols
    cw = width / cols
    t = container.add_table(rows=rows, cols=cols)
    # 选项与题干首行对齐（题号已左凸出）。
    # 带图题的选项在外层表格的 cell 里，外层表格会整体缩进，
    # 这里再缩进一次会双倍偏移。
    if not isinstance(container, _Cell):
        table_indent(t)
    for i, (L, txt) in enumerate(opts):
        r, c = divmod(i, cols)
        cell = t.cell(r, c)
        cell.width = Cm(cw)
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = T.OPTIONS["space_after"]
        p.paragraph_format.line_spacing = T.OPTIONS["line"]
        R(p, f"{L}．", T.OPTIONS["size"], True)
        rich(p, txt, T.OPTIONS["size"])
    set_cols(t, [cw] * cols)


# ---------------- 填空题下划线 ----------------
def render_blank_stem(doc, stem, qnum, size=None):
    """题干模块（填空题）：按位置把填空标记渲染为下划线"""
    size = size or T.FILL["size"]
    cfg = T.FILL["blank"]
    pat = "|".join("(?:%s)" % x for x in cfg["patterns"])
    p = P(doc, before=T.FILL["space_before"], after=T.FILL["space_after"],
          line=T.FILL["line"])
    hang_indent(p)
    _qnum_run(p, qnum, size, True)
    pos = 0
    for m in re.finditer(pat, stem):
        if m.start() > pos:
            rich(p, stem[pos:m.start()], size)
        sp = p.add_run(cfg["char"] * cfg["chars"])
        sp.font.size = Pt(size)
        sp.font.name = T.FONT["en"]
        sp._element.rPr.rFonts.set(qn('w:eastAsia'), T.FONT["cn"])
        if cfg["style"] == "single":
            sp.font.underline = True
        elif cfg["style"] == "double":
            sp.font.underline = WD_UNDERLINE.DOUBLE
        pos = m.end()
    if pos < len(stem):
        rich(p, stem[pos:], size)
    return p


# ---------------- 答题留白 ----------------
def blank(doc, cm, scale=1.0):
    cfg = T.SOLVE["answer_space"]
    n = max(1, int(round(cm * scale / 0.72)))
    for _ in range(n):
        sp = doc.add_paragraph()
        pf = sp.paragraph_format
        pf.space_before = Pt(0)
        pf.space_after = Pt(0)
        pf.line_spacing = Pt(cfg["row_h"])
        body_indent(sp)
        R(sp, "", T.SIZE["stem"])


def answer_space_cm(score):
    cfg = T.SOLVE["answer_space"]
    return max(cfg["min"], min(cfg["max"], cfg["base"] + score * cfg["per_score"]))


# ---------------- 题号独立左列（悬挂缩进） ----------------
def _qnum_run(p, qnum, size=None, bold=None):
    """题号 run：加粗 + 统一色，与答案卷一致"""
    qn = T.QNUM
    return R(p, f"{qnum}．", size or T.STEM["size"],
             qn["bold"] if bold is None else bold, qn["color"])


def hang_indent(p, cm=None):
    """段落悬挂缩进：首行左凸出题号，换行后与题干首行对齐

    这是高考试卷的标准排法。题号独占左侧，不会淹没在正文里。
    """
    cm = T.QNUM["hang_cm"] if cm is None else cm
    pf = p.paragraph_format
    pf.left_indent = Cm(cm)
    pf.first_line_indent = Cm(-cm)
    return p


def body_indent(p, cm=None):
    """普通内容缩进（不悬挂）：选项、插图、留白与题干首行对齐"""
    cm = T.QNUM["hang_cm"] if cm is None else cm
    p.paragraph_format.left_indent = Cm(cm)
    return p


def table_indent(t, cm=None):
    """表格整体右移（python-docx 无直接属性，需写 tblInd）

    1 cm = 567 twips。
    """
    from docx.oxml.ns import qn as _qn
    from docx.oxml import OxmlElement
    cm = T.QNUM["hang_cm"] if cm is None else cm
    tblPr = t._tbl.tblPr
    el = OxmlElement('w:tblInd')
    el.set(_qn('w:w'), str(int(round(cm * 567))))
    el.set(_qn('w:type'), 'dxa')
    tblPr.append(el)
    return t


# ---------------- 题干（通用） ----------------
def render_stem(doc, qnum, stem, smark="", figs=None, sub=None):
    figs = figs or []
    p = P(doc, before=T.STEM["space_before"], after=T.STEM["space_after"],
          line=T.STEM["line"])
    if figs or True:
        p.paragraph_format.keep_with_next = T.STEM["keep_with_next"]
    hang_indent(p)                      # 题号左凸，换行后对齐题干首行
    _qnum_run(p, qnum, T.STEM["size"], T.STEM["num_bold"])
    rich(p, (smark + "　" + stem) if smark else stem, T.STEM["size"])
    return p


# ---------------- 题型模块 ----------------
def render_choice(doc, q, ctx):
    """选择题模块：题干 → （左选项 / 右插图）

    【曾漏掉题干】只写了选项和图，导出的卷子是
    「一、单项选择题」下面直接跟「A．… B．…」，题干整段不见，
    而选项还在 —— 看起来像转换丢数据，实际是这里根本没渲染。

    题干必须写在最前，且 figs=None：
    插图由下方表格的右列承载，若这里再传 figs 会重复插入。
    """
    render_stem(doc, q['num'], q.get('stem_text') or '',
                q.get('smark') or '', None, ctx['sub'])
    figs = q.get('figs') or []
    if figs:
        cfg = T.FIGURE["choice"]
        fw = _fig_block_w(figs, cfg)
        lw = T.BODY_W - fw
        t = doc.add_table(rows=1, cols=2)
        table_indent(t)                       # 整块（选项+插图）与题干首行对齐
        add_opts(t.cell(0, 0), q['opts'], lw - 0.3, qnum=q['num'])
        add_figs(t.cell(0, 1), figs, q.get('subject') or ctx['sub'],
                 fw - 0.4, cfg, qnum=q['num'])
        set_cols(t, [lw, fw])
        P(doc, after=1)
    else:
        add_opts(doc, q['opts'], T.BODY_W, qnum=q['num'])
        P(doc, after=1)


def render_fill(doc, q, ctx):
    """填空题模块：题干（填空处下划线）→ 插图（下方靠右）"""
    figs = q.get('figs') or []
    render_blank_stem(doc, q['stem_text'], q['num'])
    if figs:
        cfg = T.FIGURE["solve"]
        fw = _fig_block_w(figs, cfg)
        add_figs(doc, figs, q.get('subject') or ctx['sub'], fw, cfg, qnum=q['num'],
                 align=WD_ALIGN_PARAGRAPH.RIGHT)


def render_solve(doc, q, ctx):
    """解答题模块：题干 → 插图（下方靠右）→ 答题留白"""
    figs = q.get('figs') or []
    render_stem(doc, q['num'], q['stem_text'], q.get('smark', ''), figs, ctx['sub'])
    if figs:
        cfg = T.FIGURE["solve"]
        fw = _fig_block_w(figs, cfg)
        add_figs(doc, figs, q.get('subject') or ctx['sub'], fw, cfg, qnum=q['num'],
                 align=WD_ALIGN_PARAGRAPH.RIGHT)
    if ctx.get('sec_blank'):
        sc = ctx.get('last_scale', 1.0) if q['num'] == ctx.get('last_num') else 1.0
        blank(doc, answer_space_cm(q.get('score', 8)), sc)


RENDERERS = {
    'render_choice': render_choice,
    'render_fill': render_fill,
    'render_solve': render_solve,
}


# ---------------- 试卷组装 ----------------
# ---------------- 内容自适应：字段预处理 ----------------
SCORE_RE = re.compile(r'^[（(]\s*(\d+)\s*分[)）]')


def qtype_guess(q):
    """按内容判断题型：有选项→选择；有分值→解答；否则填空"""
    if len(q.get('opts') or []) >= 2:
        return '选择'
    if SCORE_RE.search(' '.join(q.get('stem') or [])):
        return '解答'
    return '填空'


def _needs_answer_blank(q):
    """该不该在题干末尾保留作答位「（　　）」。

    只有选择题需要。高考卷选择题题干末尾本来就有作答位，
    它和下方选项是共存的 —— 之前整段删掉，
    卷面变成「…则 A．… B．…」，反而不像试卷。
    """
    st = (q.get('subtype') or '').strip()
    if st.startswith('单选') or st.startswith('多选'):
        return True
    t = (q.get('type') or '').strip()
    return t == '选择' and len(q.get('opts') or []) >= 2


def _prep_fields(q):
    """补齐渲染所需字段：stem_text / smark / score

    **不能破坏已有数据**。

    曾无条件执行 `' '.join(q.get('stem') or [])`，而入库后的题目
    只保留 `stem_text`、没有 `stem` 原始列表（拆题时已合并）。
    于是每次调用都把 `stem_text` 覆盖成空字符串 ——
    导出的试卷只剩题号和选项，**题干整段消失**，且没有任何报错。

    正确做法：`stem` 存在（刚拆题、还在内存里）才从中重建；
    否则原样保留已有的 `stem_text`。
    """
    stem_lines = q.get('stem')
    if stem_lines:
        stem = re.sub(r'\s+', ' ', ' '.join(stem_lines)).strip()
    else:
        # 已入库的题目：直接用 stem_text，不再重建
        stem = (q.get('stem_text') or '').strip()

    # 清掉误并入题干的分节标题。
    # 拆题时若分节标题与题目在同一文本块（多见于原卷分页处），
    # 会被当成题干的一部分，打印出来就是「…母线长 三、填空题 为 ( )」。
    stem = re.sub(
        r'[一二三四五六七八九十]+、\s*'
        r'(?:单项选择题|多项选择题|选择题|填空题|解答题|非选择题)'
        r'(?:[:：][^。]{0,60})?',
        '', stem)
    stem = re.sub(r'\s{2,}', ' ', stem).strip()

    # 题干尾部的作答位「（    ）」：原卷留给考生填答案，
    # 但选项已渲染到题干下方，这个尾巴是多余的（还常被重复抓取成
    # 「( ) ( ) ( ) ( ) ( )」）。
    # 选项漏进题干的（如「…则（ ） C. … D. …」）也在这里切回 opts。
    # 下标还原：PDF 提取把 a_{n+1} / F_{1} 压成了 an+1 / F1，
    # 不还原的话卷面上看到的都是「an+1」这种平文本。
    stem = mark_subscripts(stem)

    stem, leaked = split_leaked_opts(stem)
    # 选择题保留（并归一化为）一个作答位「（　　）」；
    # 填空/解答不加 —— 填空题的填空处由渲染层转成下划线。
    stem = normalize_tail_blank(stem, keep=_needs_answer_blank(q))
    if leaked:
        have = {str(o[0]).strip().upper() for o in (q.get('opts') or [])}
        for letter, body in leaked:
            # 只补**缺失的**字母。已存在的可能是正确选项
            # （少数题目提取时选项被截断成碎片，那种要重新拆卷，
            #  不能在这里猜——静默覆盖会把好数据改坏）。
            if letter.upper() not in have:
                q.setdefault('opts', []).append([letter, body])
                have.add(letter.upper())
        q['opts'] = sorted(q.get('opts') or [], key=lambda o: str(o[0]))

    m = SCORE_RE.match(stem)
    if m:
        q['score'] = int(m.group(1))
        q['smark'] = '（%d分）' % q['score']
        stem = stem[m.end():].strip()
    else:
        if not q.get('score'):
            q['score'] = 0
        q['smark'] = q.get('smark') or ''
    q['stem_text'] = stem

    ana_lines = q.get('ana')
    if ana_lines:
        q['ana_text'] = re.sub(r'\s+', ' ', ' '.join(ana_lines)).strip()
    else:
        q['ana_text'] = (q.get('ana_text') or '').strip()
    return q


# ---------------- 内容自适应：自动分节 ----------------
CN_NUM = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']


def _sec_title(sub, qtype, n, idx=0, show_subject=False):
    """分节标题。

    idx: 该科内的分节序号（0 起），决定「一、二、三…」
    show_subject: 混编卷时加科目前缀，否则数学题和物理题
                  共用「一、选择题」会让读者分不清哪段是哪科。
    """
    cn = CN_NUM[idx] if idx < len(CN_NUM) else str(idx + 1)

    if sub == '数学':
        if qtype == '多选':
            txt = ('%s、选择题：本题共 %d 小题。在每小题给出的选项中，'
                   '有多项符合题目要求。全部选对的得满分，'
                   '部分选对的得部分分，有选错的得 0 分。' % (cn, n))
        elif qtype == '选择':
            txt = ('%s、选择题：本题共 %d 小题。在每小题给出的四个选项中，'
                   '只有一项是符合题目要求的。' % (cn, n))
        elif qtype == '填空':
            txt = '%s、填空题：本题共 %d 小题。' % (cn, n)
        else:
            txt = ('%s、解答题：本题共 %d 小题。解答应写出文字说明、'
                   '证明过程或演算步骤。' % (cn, n))
    elif sub == '物理':
        if qtype == '选择':
            txt = '%s、单项选择题：共 %d 题。每题只有一个选项最符合题意。' % (cn, n)
        elif qtype == '填空':
            txt = '%s、填空题：共 %d 题。' % (cn, n)
        else:
            txt = ('%s、非选择题：共 %d 题。解答时请写出必要的文字说明、'
                   '方程式和重要的演算步骤。' % (cn, n))
    else:
        # 化学 / 生物 / 语文 / 英语：通用标题
        name = {'选择': '选择题', '多选': '选择题', '填空': '填空题'}.get(qtype, '解答题')
        txt = '%s、%s：共 %d 题。' % (cn, name, n)

    return ('【%s】%s' % (sub, txt)) if show_subject else txt


def _qtype_of_q(q):
    """判断题型：**读题目自带的字段，绝不按题号区间推测**。

    三个来源，优先级从高到低：

    1. `subtype`（最准）—— 原卷直接标了「单选题」「多选题」。
       不能靠「前 8 题单选、其余多选」这种猜法：
       题目自带了信息却不用，题量不足 8 时会造出空分节，
       多选在前的选择题段又会把单选判成多选（用户看到
       「三个选择题大分组」就是这么来的）。
    2. `type` —— 拆题时按原卷结构判定过。
    3. 内容推测（兜底）。

    为什么不能按题号推：混编卷里物理第 12 题会被套进数学的规则表
    （数学 12 题是填空题），判成解答题 → 凭空多出一大片留白。
    """
    st = (q.get('subtype') or '').strip()
    if st.startswith('多选'):
        return '多选'
    if st.startswith('单选'):
        return '选择'
    t = (q.get('type') or '').strip()
    if t in ('选择', '多选', '填空', '解答', '实验', '计算'):
        return t
    return qtype_guess(q)


def sort_key(q):
    """全局唯一排序键 —— 分节和编号都必须用它。

    曾有两次排序：auto_sections 按 (题型, 题号) 排，
    _renumber 又按 (题号) 排。两次顺序不一致，
    再按「各分节题数」依次切分时，题目就被分到了错误的分节 ——
    结果「填空题」分节里躺着一道物理解答题。
    """
    TYPE_ORDER = {'选择': 0, '多选': 1, '填空': 2,
                  '实验': 3, '计算': 4, '解答': 5}
    return (q.get('_subj_order', 0),
            TYPE_ORDER.get(_qtype_of_q(q), 9),
            q.get('num') or 0,
            q.get('id') or '')


def order_and_number(sub, qs):
    """排序 + 题号重排为 1..N，返回有序的扁平题目列表。

    **试卷与答案卷必须共用这一个函数。**

    曾有两次排序：auto_sections 按 (题型, 题号) 排，
    _renumber 又按 (题号) 排。两次顺序不一致，
    再按「各分节题数」依次切分时，题目就被分到了错误的分节 ——
    结果「填空题」分节里躺着一道物理解答题。

    后来答案卷又因为**不调用本函数**（直接用 q['num']），
    出现两个问题：
      1. 人工录入的题 num 默认 0，答案卷题号全是「0．」
      2. 更严重：顺序与试卷不一致 —— 孩子对着答案卷找第 5 题，
         实际是另一道题。题号错看得出来，顺序错很难发现。
    """
    # 科目顺序 = 题目首次出现的顺序
    subj_order, n = {}, 0
    for q in qs:
        sj = q.get('subject') or sub
        if sj not in subj_order:
            subj_order[sj] = n
            n += 1

    for q in qs:
        q['_subj_order'] = subj_order.get(q.get('subject') or sub, 0)

    ordered = sorted(qs, key=sort_key)

    # 编排序号（全局连续 1..N）
    for i, q in enumerate(ordered, 1):
        q['num'] = i

    return ordered


def auto_sections(sub, qs):
    """按内容分节，并把题号统一重排为 1..N。

    分组键是 (科目, 题型)：
      - 混编卷里数学和物理各成一段，两科都看得见；
        否则整卷只会显示「数学」的分节标题，物理题被淹没其中。
      - 不再按「前 8 题单选」硬切，改用题目自带的 subtype。
    """
    ordered = order_and_number(sub, qs)
    multi = len({q.get('subject') or sub for q in qs}) > 1

    # 按 (科目, 题型) 连续分组
    spans = []                       # [科目, 题型, [题目...]]
    for q in ordered:
        sj = q.get('subject') or sub
        t = _qtype_of_q(q)
        if spans and spans[-1][0] == sj and spans[-1][1] == t:
            spans[-1][2].append(q)
        else:
            spans.append([sj, t, [q]])

    secs, idx_of = [], {}
    for sj, t, group in spans:
        idx_of[sj] = idx_of.get(sj, 0)
        secs.append((
            _sec_title(sj, t, len(group), idx_of[sj], show_subject=multi),
            [q['num'] for q in group],
            '',
            t in ('解答', '实验', '计算'),
        ))
        idx_of[sj] += 1

    # 清理临时字段
    for q in qs:
        q.pop('_subj_order', None)
    return secs


def has_blank_last_page(path):
    """末页是否为纯空白页。

    最后一道解答题留白过多时会溢出，生成一个只有页眉页脚的空页。
    这里用 PyMuPDF 渲染检测：末页若没有任何文本内容即视为空白。

    无法渲染时（缺依赖或文件异常）返回 False —— 宁可多试一次重排，
    也不要因为检测失败而误判为「没有空白页」。
    """
    try:
        import pymupdf
        doc = pymupdf.open(path)
        if len(doc) < 2:
            doc.close()
            return False
        last = doc[len(doc) - 1]
        blank = not last.get_text().strip()
        doc.close()
        return blank
    except Exception:
        return False


def build_paper(qs, sub, title, sub_title, meta, secs, outdir, last_scale=1.0):
    doc = Document()
    setup(doc)
    head_block(doc, title, sub_title, meta)

    ctx = {'sub': sub}
    last_num = max((max(r) for _, r, _, sb in secs if sb), default=None)
    ctx['last_num'] = last_num
    ctx['last_scale'] = last_scale

    for sec_name, nums, note, sec_blank in secs:
        p = P(doc, before=T.SECTION["space_before"], after=T.SECTION["space_after"])
        R(p, sec_name, T.SECTION["size"], T.SECTION["bold"],
          T.SECTION["color"], T.FONT["title"])
        if note:
            p = P(doc, after=4, indent=0.5)
            R(p, note, T.SIZE["note"], False, (0x66, 0x66, 0x66))

        for n in nums:
            q = next((x for x in qs if x['num'] == n), None)
            if not q:
                continue
            # 题型从题目自身读取，不用 T.qtype_of(sub, n)。
            # 后者按题号区间查全局规则表，混编卷会串到别的科目结构上去。
            qtype = _qtype_of_q(q)
            spec = T.QTYPES.get(qtype, T.QTYPES["解答"])
            ctx['sec_blank'] = sec_blank and spec['blank']
            RENDERERS[spec['renderer']](doc, q, ctx)

    safe = (sub_title or '练习卷').replace('_', '-')
    path = os.path.join(outdir, f'试卷-{safe}.docx')
    doc.save(path)
    return path


# ---------------- 答案与解析卷 ----------------
def build_answer(qs, sub, title, sub_title, meta, src_label, outdir="."):
    doc = Document()
    setup(doc)
    head_block(doc, title + '　参考答案与解析', sub_title, meta)
    A = T.ANSWER_SHEET
    n_ans = n_ana = 0
    for q in qs:
        ans = q.get('answer')
        ana = q.get('ana_text', '')
        if not ans and not ana:
            continue
        p = P(doc, before=A["space"], after=1)
        # 与试卷统一：题号左凸出，来源/解析整体缩进与其对齐
        hang_indent(p)
        _qnum_run(p, q['num'], T.SIZE["answer"], True)
        if ans:
            # **必须用 rich() 而不是 R()**。
            # 答案是 LaTeX（如 `$f(x)\notin M$，$g(x)\in M$`），
            # 用 R() 会当纯文本原样输出 —— 页面上看到的是
            # 源码原样输出（用户反馈的"∈ 显示成了 in"，
            # 其实是 \notin 里的 in 被当成普通文本了）。
            # 解析行本来就用的 rich()，答案行漏了 —— 同一处两样写法。
            rich(p, A["label_answer"] + ans, A["size"], True,
                 A["answer_color"])
            n_ans += 1
        else:
            R(p, A["label_answer"] + A["no_answer_text"],
              A["size"], True, (0x99, 0x99, 0x99))
        # 来源优先用题目自己的 src 字段。
        # 原来统一用 src_label（=第一题的 year + 科目），
        # 人工录入的题没有 year，结果全部显示「 数学」，
        # 而每题其实都带了具体来源（如「2024热点题型归纳 变式16」）。
        src_txt = (q.get('src') or '').strip() or src_label
        src = A["source_template"].format(src=src_txt, num=q['num'])
        p = P(doc, after=2, indent=A["indent"])
        body_indent(p)                  # 与题号左凸后的题干首行对齐
        # 来源也可能含 LaTeX（如「变式 $a_{10}$」），同样用 rich()
        rich(p, A["label_source"] + src, T.SIZE["source"], False,
             A["source_color"])
        if ana:
            p = P(doc, after=4, indent=A["indent"])
            body_indent(p)
            R(p, A["label_analysis"], T.SIZE["analysis"], True, A["analysis_color"])
            rich(p, ana, T.SIZE["analysis"], False, A["analysis_color"])
            n_ana += 1
    safe = (sub_title or '练习卷').replace('_', '-')
    path = os.path.join(outdir, f'答案与解析-{safe}.docx')
    doc.save(path)
    return path, n_ans, n_ana


def last_page_info(docx_path, tmp="/tmp/_chk"):
    import pymupdf
    os.makedirs(tmp, exist_ok=True)
    for f in glob.glob(tmp + "/*.pdf"):
        os.remove(f)
    try:
        subprocess.run(["python", "/data/skills/docx/scripts/office/soffice.py",
                        "--headless", "--convert-to", "pdf", "--outdir", tmp, docx_path],
                       timeout=220, capture_output=True)
    except Exception:
        return (0, -1)
    pdfs = glob.glob(tmp + "/*.pdf")
    if not pdfs:
        return (0, -1)
    try:
        d = pymupdf.open(pdfs[0])
        last = [l for l in d[d.page_count - 1].get_text().split("\n") if l.strip()]
        return (d.page_count, len(last))
    except Exception:
        return (0, -1)

def _main():
    """单份调试用主流程（批量处理请用 batch.py）"""
    import paper_template as _T
    os.makedirs(SLICE, exist_ok=True)
    SUBJ = [('数学', '收集到的真题/数学/2026全国I卷数学.pdf',
             '2026 年普通高等学校招生全国统一考试', '数学（全国I卷）',
             '2026 全国I卷'),
            ('物理', '收集到的真题/物理/2026江苏卷物理.pdf',
             '2026 年江苏省普通高中学业水平选择性考试', '物理（江苏卷）',
             '2026 江苏卷')]
    META = {
     '数学': [('满分 / 时长', '150 分 / 120 分钟'),
              ('适用范围', '全国 I 卷适用地区'),
              ('试卷结构', '选择题 8 题 + 多选题 3 题 + 填空题 3 题 + 解答题 5 题')],
     '物理': [('满分 / 时长', '100 分 / 75 分钟'),
              ('适用范围', '江苏省普通高中学业水平选择性考试'),
              ('试卷结构', '单项选择题 11 题 + 非选择题 5 题')],
    }
    for sub, path, t1, t2, src in SUBJ:
        doc, qs, fb = extract(path, sub)
        crop_figs(doc, qs, os.path.join(SLICE, sub), fb)
        for q in qs:
            q['answer'] = extract_answer(' '.join(q['ana']), len(q['opts']) >= 2)
            _prep_fields(q)
        secs = auto_sections(sub, qs)
        pp = None
        for scale in _T.SOLVE["last_scale_steps"]:
            pp = build_paper(qs, sub, t1, t2, META[sub], secs, '.', scale)
            npg, nlast = last_page_info(pp)
            if nlast > 1:
                break
        ap, na, nan = build_answer(qs, sub, t1, t2, META[sub], src)
        print(f'{sub}: {len(qs)}题 答案{na} 解析{nan}')


if __name__ == "__main__":
    _main()
