# -*- coding: utf-8 -*-
"""LaTeX 片段 → MathML 转换（浏览器原生渲染，零依赖）

为什么用 MathML：
  - Chrome 109+ / Firefox / Safari 全部原生支持（MathML Core）
  - 不需要任何 JS、CSS、字体文件 → 离线可用，单文件交付
  - 矢量渲染，打印清晰
  - 相比手写 OMML(Word 公式)XML，MathML 是标准且可读的

输入：extract3.split_rich() 切出的片段
  ('t', 文本) | ('f', 分子, 分母) | ('s', 被开方数)
"""
import re
from html import escape

# 需要作为标识符（斜体）的字符：字母、希腊字母
IDENT = re.compile(r'[A-Za-z\u0370-\u03ff]')
# 数字与运算符用 <mn>/<mo>（正体）


def _tok(s):
    """把一串字符包成 MathML 叶子节点"""
    if not s:
        return ''
    out = []
    i = 0
    n = len(s)
    while i < n:
        ch = s[i]
        if IDENT.match(ch):
            # 连续字母作为一个标识符（如 sin、cos、ab）
            j = i
            while j < n and IDENT.match(s[j]):
                j += 1
            out.append('<mi>%s</mi>' % escape(s[i:j]))
            i = j
        elif ch.isdigit() or ch == '.':
            j = i
            while j < n and (s[j].isdigit() or s[j] == '.'):
                j += 1
            out.append('<mn>%s</mn>' % escape(s[i:j]))
            i = j
        else:
            # 运算符 / 括号 / 其他符号
            out.append('<mo>%s</mo>' % escape(ch))
            i += 1
    return ''.join(out)


def _trim_arg(s):
    """去掉参数尾部多余的分隔符。

    PDF 提取时根号后紧跟的逗号常被误吞进花括号：
        「半径为 √2 的圆锥」 → ``\sqrt{2,}``
    渲染出来就是 √(2,)，逗号是脏数据。
    只去**尾部**孤立的逗号，不动 ``\sqrt{2,5}``。
    """
    return re.sub(r'[,，]$', '', str(s if s is not None else '').strip()).strip()


def _mi_or_mn(s):
    """参数内容 → MathML。

    **必须递归**：``\frac{\sqrt{3}}{2}`` 的分子本身是根号，
    不递归的话 `\sqrt{3}` 会被 _tok() 逐字符拆成
    ``<mo>\</mo><mi>sqrt</mi><mo>{</mo>...``，
    屏幕上就显示成源码文本 —— 正是要修的问题。
    """
    if not s:
        return '<mi></mi>'
    t = _trim_arg(s)
    if not t:
        return '<mi></mi>'

    # 先递归：参数里若还有 \frac / \sqrt，整棵子树重新解析
    # 延迟 import：extract3 也会用到本模块，顶层 import 会循环依赖。
    from extract3 import split_rich
    from extract3 import merge_script
    inner = merge_script(split_rich(t))
    if inner and any(x[0] in ('f', 's', 'm', 'p', 'sp') for x in inner):
        kids = []
        for sg in inner:
            if sg[0] == 't':
                if sg[1]:
                    kids.append('<mtext>%s</mtext>' % escape(sg[1]))
            elif sg[0] == 'f':
                kids.append(frac(sg[1], sg[2]))
            elif sg[0] == 's':
                kids.append(sqrt(sg[1]))
            elif sg[0] == 'm':
                kids.append(sub(sg[1], sg[2]))
            elif sg[0] == 'p':
                kids.append(sup(sg[1], sg[2]))
            elif sg[0] == 'sp':
                kids.append(subsup(sg[1], sg[2], sg[3]))
        if kids:
            return '<mrow>%s</mrow>' % ''.join(kids)
        return '<mi></mi>'

    # 无嵌套：走简单路径
    if re.fullmatch(r'[A-Za-z\u0370-\u03ff]+', t):
        return '<mi>%s</mi>' % escape(t)
    if re.fullmatch(r'[\d.]+', t):
        return '<mn>%s</mn>' % escape(t)
    # 混合内容（如 "E1 − E2"、"2mER"）→ 逐字符拆分
    kids = _tok(t)
    return '<mrow>%s</mrow>' % kids if kids else '<mi></mi>'


def frac(num, den):
    return ('<mfrac><mrow>%s</mrow><mrow>%s</mrow></mfrac>'
            % (_mi_or_mn(num), _mi_or_mn(den)))


def sqrt(inner):
    return '<msqrt><mrow>%s</mrow></msqrt>' % _mi_or_mn(inner)


def sub(base, sub_txt):
    """下标：<msub><mi>a</mi><mrow>n+1</mrow></msub>"""
    return '<msub>%s<mrow>%s</mrow></msub>' % (_mi_or_mn(base), _mi_or_mn(sub_txt))


def sup(base, sup_txt):
    """上标：<msup><mi>x</mi><mrow>2</mrow></msup>"""
    return '<msup>%s<mrow>%s</mrow></msup>' % (_mi_or_mn(base), _mi_or_mn(sup_txt))


def subsup(base, sub_txt, sup_txt):
    """同时有上下标：<msubsup>（如 x²₁）"""
    return ('<msubsup>%s<mrow>%s</mrow><mrow>%s</mrow></msubsup>'
            % (_mi_or_mn(base), _mi_or_mn(sub_txt), _mi_or_mn(sup_txt)))


def to_mathml(segs):
    """片段列表 → 一行 <math> 元素

    segs: [('t',文本) | ('f',分子,分母) | ('s',被开方数), ...]

    返回 '' 表示没有任何需要公式渲染的内容（纯文本）。
    """
    has_math = any(s[0] in ('f', 's', 'm', 'p', 'sp') for s in segs)
    if not has_math:
        return ''
    kids = []
    for sg in segs:
        if sg[0] == 't':
            if sg[1]:
                # 纯文本段：用 <mtext>，避免空格被吃掉
                kids.append('<mtext>%s</mtext>' % escape(sg[1]))
        elif sg[0] == 'f':
            kids.append(frac(sg[1], sg[2]))
        elif sg[0] == 's':
            kids.append(sqrt(sg[1]))
        elif sg[0] == 'm':
            kids.append(sub(sg[1], sg[2]))
        elif sg[0] == 'p':
            kids.append(sup(sg[1], sg[2]))
        elif sg[0] == 'sp':
            kids.append(subsup(sg[1], sg[2], sg[3]))
    if not kids:
        return ''
    body = kids[0] if len(kids) == 1 else '<mrow>%s</mrow>' % ''.join(kids)
    return ('<math xmlns="http://www.w3.org/1998/Math/MathML" '
            'display="inline">%s</math>' % body)


# ---------------- 化学式 ----------------
# 简单上下标：H_2_O、SO_4_^2-
SUB_SUP = re.compile(r'([A-Za-z\u0370-\u03ff][a-z]?)_(\d+)(?:\^([-\d+]+))?')


def chem(s):
    """把 H_2_O / SO_4_^2- 转成带 sub/sup 的 HTML（用于 Markdown 格式列）"""
    def _r(m):
        base, sub, sup = m.group(1), m.group(2), m.group(3)
        out = escape(base)
        if sub:
            out += '<sub>%s</sub>' % escape(sub)
        if sup:
            out += '<sup>%s</sup>' % escape(sup)
        return out
    return SUB_SUP.sub(_r, escape(s))


# ==========================================================================
# 通用行内 LaTeX → MathML
# ==========================================================================
#
# 为什么需要它：
#   split_rich() 只认 \frac / \sqrt / _{} / ^{} 四种模式，
#   那是为**自动提取**设计的（PDF 里只还原得出这几种结构）。
#   人工录入用的是标准 LaTeX（$\mathbb{R}$、$\le$、$x_1$ ...），
#   直接喂给 split_rich 会原样输出源码 —— 屏幕上显示
#   "定义在 $\mathbb{R}$ 上的奇函数 $f(x)$"，非常难看。
#
#   所以单独写一个通用转换器，覆盖高考数学常用语法。
#   仍走 MathML：浏览器原生、离线可用、矢量打印。

# 宏 -> Unicode 字符
MACRO = {
    # 关系
    # leqslant / geqslant 与 le / leq 完全等价（都是 ≤ ≥），
    # 缺了它们会输出 <mi>leqslant</mi> 这样的命令名。
    r'\le': '≤', r'\leq': '≤', r'\leqslant': '≤', r'\eqslantless': '≤',
    r'\ge': '≥', r'\geq': '≥', r'\geqslant': '≥', r'\eqslantgtr': '≥',
    r'\ne': '≠', r'\neq': '≠', r'\approx': '≈', r'\equiv': '≡',
    # --- 算子 ---
    # \sum \prod \int 漏了会输出 <mi>sum</mi>（页面显示 "sumlimits"）。
    # 它们在 MathML 里是 <mo>，与关系符同类。
    r'\sum': '∑', r'\prod': '∏', r'\int': '∫', r'\iint': '∬',
    r'\oint': '∮', r'\bigcup': '⋃', r'\bigcap': '⋂',
    # --- 逻辑与推理（充要条件、命题章节高频）---
    r'\iff': '⟺', r'\implies': '⟹', r'\impliedby': '⟸',
    r'\Leftrightarrow': '⇔', r'\Rightarrow': '⇒', r'\Leftarrow': '⇐',
    r'\nRightarrow': '⇏',   # 不能推出；漏了会直接显示命令名
    r'\nLeftarrow': '⇍', r'\nleftrightarrow': '↮',
    r'\niff': '⇎', r'\nimplies': '⇏',
    r'\lnot': '¬', r'\neg': '¬', r'\land': '∧', r'\wedge': '∧',
    r'\lor': '∨', r'\vee': '∨', r'\forall': '∀', r'\exists': '∃',
    # --- 几何与二元运算 ---
    r'\odot': '⊙', r'\otimes': '⊗', r'\oplus': '⊕', r'\times': '×',
    r'\div': '÷', r'\pm': '±', r'\mp': '∓', r'\cdot': '⋅',
    r'\ast': '∗', r'\circ': '∘', r'\bullet': '∙', r'\star': '⋆',
    r'\perp': '⊥', r'\parallel': '∥', r'\angle': '∠', r'\triangle': '△',
    r'\square': '□', r'\cong': '≅', r'\sim': '∼', r'\simeq': '≃',
    # --- 定义与关系杂项 ---
    r'\triangleq': '≜', r'\doteq': '≐', r'\propto': '∝',
    r'\prec': '≺', r'\succ': '≻', r'\preceq': '⪯', r'\succeq': '⪰',
    r'\ll': '≪', r'\gg': '≫', r'\to': '→',
    # --- K12 集合与逻辑高频符号 ---
    # 这几个漏了会直接输出命令名（页面显示 "mid"、"subsetneq"、"complement"），
    # 是第一批教辅录入时用户逐个发现的。
    r'\mid': '∣',             # 集合描述法的分隔符 {x | x>0}
    r'\nmid': '∤',
    r'\subsetneq': '⊊',       # 真子集
    r'\supsetneq': '⊋',
    r'\subsetneqq': '⫋',
    r'\supsetneqq': '⫌',
    r'\complement': '∁',      # 补集，常写作 \complement_U A
    r'\setminus': '∖',        # 差集
    r'\setminus ': '∖',
    r'\varnothing': '∅', r'\emptyset': '∅',
    r'\therefore': '∴', r'\because': '∵',
    r'\sim': '∼', r'\propto': '∝', r'\doteq': '≐',
    # 集合与逻辑
    r'\in': '∈', r'\notin': '∉', r'\ni': '∋',
    r'\subset': '⊂', r'\subseteq': '⊆', r'\supset': '⊃',
    r'\supseteq': '⊇', r'\cup': '∪', r'\cap': '∩',
    r'\varnothing': '∅', r'\emptyset': '∅',
    r'\forall': '∀', r'\exists': '∃',
    # 运算
    r'\times': '×', r'\cdot': '⋅', r'\div': '÷',
    r'\pm': '±', r'\mp': '∓', r'\ast': '∗', r'\circ': '∘',
    # 箭头
    r'\to': '→', r'\rightarrow': '→', r'\leftarrow': '←',
    r'\Rightarrow': '⇒', r'\Leftarrow': '⇐',
    r'\leftrightarrow': '↔', r'\mapsto': '↦',
    r'\nRightarrow': '⇏', r'\nLeftarrow': '⇍',
    r'\nleftrightarrow': '↮', r'\nrightarrow': '↛', r'\nleftarrow': '↚',
    # 几何
    r'\perp': '⊥', r'\parallel': '∥', r'\angle': '∠',
    r'\triangle': '△', r'\square': '□', r'\cong': '≅',
    # 其他
    r'\infty': '∞', r'\ldots': '…', r'\cdots': '⋯', r'\dots': '…',
    r'\prime': '′', r'\degree': '°', r'\partial': '∂',
    r'\nabla': '∇', r'\therefore': '∴', r'\because': '∵',
    r'\pm': '±', r'\surd': '√',
}
# 希腊字母
GREEK = {
    'alpha': 'α', 'beta': 'β', 'gamma': 'γ', 'delta': 'δ',
    'epsilon': 'ϵ', 'varepsilon': 'ε', 'zeta': 'ζ', 'eta': 'η',
    'theta': 'θ', 'vartheta': 'ϑ', 'iota': 'ι', 'kappa': 'κ',
    'lambda': 'λ', 'mu': 'μ', 'nu': 'ν', 'xi': 'ξ',
    'pi': 'π', 'varpi': 'ϖ', 'rho': 'ρ', 'sigma': 'σ',
    'tau': 'τ', 'upsilon': 'υ', 'phi': 'ϕ', 'varphi': 'φ',
    'chi': 'χ', 'psi': 'ψ', 'omega': 'ω',
    'Gamma': 'Γ', 'Delta': 'Δ', 'Theta': 'Θ', 'Lambda': 'Λ',
    'Xi': 'Ξ', 'Pi': 'Π', 'Sigma': 'Σ', 'Upsilon': 'Υ',
    'Phi': 'Φ', 'Psi': 'Ψ', 'Omega': 'Ω',
}
# 黑板粗体（数集）
#
# 恒等映射：\mathbb{R} -> R，不做 Unicode 转换。
# 原因有两个：
#   1. 用户要求 —— 试卷上写 R 就够了，ℝ 反而多余
#   2. 更关键的：Unicode 黑板粗体（ℝ ℕ ℤ ℚ ℂ）在不少中文字体里
#      **没有对应字形**，渲染成方块 □。试卷是要打印给孩子做的，
#      出现方块比不美观严重得多。
BB = {}
# 函数名（正体）
FUNCS = ('sin', 'cos', 'tan', 'cot', 'sec', 'csc',
         'arcsin', 'arccos', 'arctan', 'sinh', 'cosh', 'tanh',
         'ln', 'lg', 'log', 'exp', 'max', 'min', 'lim',
         'sup', 'inf', 'arg', 'deg', 'dim', 'det', 'gcd')

# 识别「字母 + 左括号 = 函数调用」时可跳过的命令：
#   \left 等定界命令            → f\left(x\right)
#   \! \, \; \quad 等间距命令   → f\!(x)
_LEFT_SKIP = {'left', 'bigl', 'Bigl', 'biggl', 'Biggl',
              '!', ',', ':', ';', ' ', 'quad', 'qquad', ',', 'thinspace'}
_CMD_RE = re.compile(r'\\[a-zA-Z]+|\\.')

# 运算符/定界符/其他：一律正体
_UPRIGHT_CHARS = set('()[]{}<>=+-*/|!,:;\'`~^_&%#@?°′″')


def is_func_call(s, j):
    """s 在位置 j 之后（跳过空白、\\left、\\! 等）是否是左括号。

    **只对单个字母启用**：f(x)、g(x) 里的 f/g 是函数名，应排正体；
    而 abc(d) 视为多个变量相乘，仍排斜体。

    必须跳过间距命令：``f\\!\\left(-\\dfrac{1}{2}\\right)`` 里
    f 后面先是 ``\\!`` 再是 ``\\left``，不匹配的话 f 会被误判成变量（斜体）。
    """
    n = len(s)
    while j < n:
        if s[j].isspace():
            j += 1
            continue
        if s[j] == '\\':
            m = _CMD_RE.match(s, j)
            if not m:
                return False
            name = m.group(0)[1:]
            if name in _LEFT_SKIP:
                j = m.end()
                continue
            return False          # 其他命令（\sin 等）不构成函数调用
        break
    return j < n and s[j] in '(['


def split_math_style(t, force_upright=(), default_italic=True):
    """把一段公式文本按「正体 / 斜体」切分。

    返回 [(文本, 是否正体), ...]，拼接后等于原文。

    数学排版规范（ISO 80000-2，也是高考卷的实际排法）：

    | 内容 | 字体 | 例子 |
    |---|---|---|
    | 函数名 | **正体** | ``sin`` ``log`` ``max``，以及 ``f(`` ``g(`` 这类单字母函数 |
    | 数集 | **正体** | ``\\mathbb{R}``（通过 force_upright 传入） |
    | 数字、运算符、括号 | **正体** | ``(0,1)`` ``-1`` ``+`` |
    | 变量 | **斜体** | ``x`` ``y`` ``n`` ``a`` |

    default_italic=True：无法判定的单个字母按**变量**处理（斜体）。
    这是与 HTML 端 `<mi>x</mi>` 保持一致的关键 ——
    两端必须同一规则，否则同一道题在网页和 Word 里字体不同。
    """
    if not t:
        return []
    up = set(force_upright or ())
    out, n, i = [], len(t), 0
    while i < n:
        c = t[i]
        # ---- 数字 / 小数点 ----
        if c.isdigit() or c == '.':
            j = i
            while j < n and (t[j].isdigit() or t[j] == '.'):
                j += 1
            out.append((t[i:j], True))
            i = j
            continue
        # ---- 西文字母 ----
        if c.isascii() and c.isalpha():
            j = i
            while j < n and t[j].isascii() and t[j].isalpha():
                j += 1
            word = t[i:j]
            if word in up:                       # 数集等外部指定
                out.append((word, True))
            elif word in FUNCS:                  # 多字母函数名
                out.append((word, True))
            elif len(word) == 1 and is_func_call(t, j):
                out.append((word, True))         # f(x) 里的 f
            elif len(word) == 1:
                out.append((word, not default_italic))
            else:
                # 多字母且非函数名：按变量逐个切（abc = a·b·c）
                for ch in word:
                    out.append((ch, not default_italic))
            i = j
            continue
        # ---- 希腊字母与 CJK：保持原样，按 default 处理 ----
        if c.isalpha():
            j = i
            while j < n and t[j].isalpha():
                j += 1
            if j - i == 1:
                out.append((t[i:j], not default_italic))
            else:
                out.append((t[i:j], True))
            i = j
            continue
        # ---- 运算符 / 括号 / 其他 ----
        if c in _UPRIGHT_CHARS or not c.isalnum():
            j = i
            while j < n and (t[j] in _UPRIGHT_CHARS or not t[j].isalnum()):
                if t[j].isspace():
                    break
                j += 1
            if j == i:
                j = i + 1
            out.append((t[i:j], True))
            i = j
            continue
        out.append((c, True))
        i += 1
    # 合并相邻且同属性的小段，减少 run 数量
    merged = []
    for seg, u in out:
        if merged and merged[-1][1] == u:
            merged[-1] = (merged[-1][0] + seg, u)
        else:
            merged.append((seg, u))
    return merged


def _read_arg(s, i):
    """读一个 {..} 参数。返回 (内容, 下一位置)。没有花括号则读单字符。"""
    if i >= len(s):
        return '', i
    if s[i] == '{':
        depth = 0
        j = i
        while j < len(s):
            if s[j] == '{':
                depth += 1
            elif s[j] == '}':
                depth -= 1
                if depth == 0:
                    return s[i + 1:j], j + 1
            j += 1
        return s[i + 1:], len(s)      # 未闭合，容错
    return s[i], i + 1



def _read_script_arg(s, i):
    """读上下标的参数（``x^2`` 里 ^ 后面那一段）。

    与 _read_arg 的区别：_read_arg 对非 ``{`` 只取**单个字符**，
    于是 ``90^\\circ`` 的上标被取成 ``\\``，剩下的 circ 被当成
    变量 c·i·r·c 逐个输出 —— 页面显示成「90^\ c i r c」完全乱排。

    上下标参数支持三种形式：
        ``{..}``   → 取组内内容
        ``\\cmd``  → 取整条命令（\\circ、\\alpha 等）
        其他      → 单个字符
    """
    if i >= len(s):
        return '', i
    if s[i] == '{':
        return _read_arg(s, i)
    if s[i] == '\\':
        m = re.match(r'\\[a-zA-Z]+|\\.', s[i:])
        if m:
            return m.group(0), i + m.end()
        return s[i], i + 1
    return s[i], i + 1

def _parse_expr(s, i, stop=None):
    """解析表达式直到 stop 集合中的字符或末尾。

    返回 (MathML 片段列表, 下一位置)。
    """
    out = []
    n = len(s)
    while i < n:
        c = s[i]
        if stop and c in stop:
            break

        # ---- 宏 ----
        if c == '\\':
            j = i + 1
            m = re.match(r'[a-zA-Z]+', s[j:]) or re.match(r'.', s[j:])
            name = m.group(0) if m else ''
            key = '\\' + name
            k = j + len(name)

            # 转义花括号 \{ \}：集合的花括号必须转义（否则被当分组），
            # 但走"未知宏"分支会输出 <mi>{</mi> —— mi 默认斜体，
            # {1,2} 的花括号就会显示成斜体，很怪。显式用 <mo> 保持正体。
            if name in ('{', '}'):
                out.append('<mo>%s</mo>' % name)
                i = k
                continue

            # \begin{cases} ... \end{cases}：分段函数。
            # 高中数学高频（分段函数、分段数列、绝对值分段讨论），
            # 不支持的话会输出 "begin cases" 源码，完全无法阅读。
            if name == 'begin':
                _m2 = re.match(r'\s*\{([a-zA-Z*]+)\}', s[k:])
                if _m2:
                    env = _m2.group(1)
                    endtag = '\\end{' + env + '}'
                    _k2 = s.find(endtag, k + _m2.end())
                    if _k2 < 0:
                        _k2 = len(s)
                    body = s[k + _m2.end():_k2]
                    rows = []
                    for line in body.split('\\\\'):
                        line = line.strip()
                        if not line:
                            continue
                        cells = []
                        for cell in line.split('&'):
                            _kd, _ = _parse_expr(cell.strip(), 0)
                            cells.append('<mtd>%s</mtd>'
                                         % (''.join(_kd) or '<mi></mi>'))
                        if cells:
                            rows.append('<mtr>%s</mtr>' % ''.join(cells))
                    if env in ('cases', 'dcases'):
                        # rowspacing 必须显式收紧：
                        # mtable 默认行距较松，2 行的 cases 会让左侧
                        # stretchy 的 { 被撑得很高，视觉上"括号特别大"。
                        # 0.15ex 接近 Word 分段函数的间距。
                        # 三个措施压低高度（stretchy 的 { 会跟随 mtable 全高）：
                        #   1. mstyle displaystyle="false" —— 最有效。
                        #      非展示模式下分式、上下标都用紧凑形式，行高明显变小。
                        #   2. rowspacing="0.1ex" —— 收紧行间距
                        #   3. framespacing="0 0" —— 去掉 mtable 外框留白
                        #
                        # 单靠 rowspacing 收不住（实测 0.15ex 仍显大），
                        # 因为浏览器对 stretchy 字符有最小拉伸尺寸。
                        out.append('<mrow><mo stretchy="true">{</mo>'
                                   '<mstyle displaystyle="false">'
                                   '<mtable columnspacing="0.6em" '
                                   'rowspacing="0.1ex" framespacing="0 0" '
                                   'columnalign="left">%s</mtable>'
                                   '</mstyle></mrow>'
                                   % ''.join(rows))
                    else:
                        out.append('<mtable>%s</mtable>' % ''.join(rows))
                    i = _k2 + len(endtag)
                    continue

            # \left \right \middle 只影响括号尺寸，MathML 里由 mrow 自动处理。
            # \middle 用于集合定义里 \left\{x\;\middle|\;...\right\} 的竖线，
            # 不支持会输出 <mi>middle</mi>（连带着把后面的 | 也吃掉）。
            if name in ('left', 'right', 'middle',
                        'big', 'Big', 'bigg', 'Bigg',
                        'bigl', 'bigr', 'Bigl', 'Bigr',
                        'bigm', 'Bigm', 'biggm', 'Biggm'):
                i = k
                continue
            # \limits \nolimits \displaystyle 等只影响排版，
            # MathML 里上下标位置由 mo 的 movablelimits 自动决定。
            # 不跳过会把 \sum\limits_{k=1}^{n} 渲染成 <mi>limits</mi>。
            if name in ('limits', 'nolimits', 'displaystyle', 'textstyle',
                        'scriptstyle', 'scriptscriptstyle'):
                i = k
                continue
            # 间距命令
            if name in (',', ';', ':', '!', 'quad', 'qquad', ' '):
                i = k
                continue
            if name == '\\':                      # 换行（行内忽略）
                i = k
                continue

            # \frac{}{}（\dfrac / \tfrac 是同一结构的变体：
            # 行内渲染没有 display 与 text 之分，三者等价。
            # 早期只认 frac，\dfrac 会落进"未知宏"分支，
            # 输出 <mi>dfrac</mi><mn>1</mn><mn>2</mn>，分数结构整个丢失）
            if name in ('frac', 'dfrac', 'tfrac'):
                num, p = _read_arg(s, k)
                den, p2 = _read_arg(s, p)
                out.append('<mfrac><mrow>%s</mrow><mrow>%s</mrow></mfrac>'
                           % (_mi_or_mn(num) if not _need_parse(num)
                              else _group(_parse_expr(num, 0)[0]),
                              _mi_or_mn(den) if not _need_parse(den)
                              else _group(_parse_expr(den, 0)[0])))
                i = p2
                continue
            # \sqrt[n]{x} 或 \sqrt{x}
            if name == 'sqrt':
                if k < n and s[k] == '[':
                    e = s.find(']', k)
                    idx = s[k + 1:e] if e > 0 else ''
                    body, p = _read_arg(s, (e + 1) if e > 0 else k)
                    b = (_mi_or_mn(body) if not _need_parse(body)
                         else _group(_parse_expr(body, 0)[0]))
                    out.append('<mroot><mrow>%s</mrow><mrow>%s</mrow></mroot>'
                               % (b, _mi_or_mn(idx)))
                    i = p
                else:
                    body, p = _read_arg(s, k)
                    b = (_mi_or_mn(body) if not _need_parse(body)
                         else _group(_parse_expr(body, 0)[0]))
                    out.append('<msqrt><mrow>%s</mrow></msqrt>' % b)
                    i = p
                continue
            # \mathbb{R}
            # 数集必须**正体**：斜体的 R 会被当成普通变量，
            # 而 \mathbb{R} 表示的是实数集这个固定对象。
            # 加 mathvariant="normal" 与函数名同样处理，
            # 否则 CSS 里 `math mi{font-style:italic}` 会把它变斜。
            # ---- 向量 / 上划线 / 粗体 ----
            # 这三个是中学数学的高频记号，缺了会原样输出命令名：
            #   \overrightarrow{CA} → <mi>overrightarrow</mi><mi>C</mi><mi>A</mi>
            # 页面显示成「overrightarrowCA」，完全读不通。
            if name in ('overrightarrow', 'overleftarrow', 'overleftrightarrow', 'UNDL',
                        'vec', 'overline', 'underline', 'hat', 'bar'):
                body, p = _read_arg(s, k)
                kids, _ = _parse_expr(body, 0)
                inner = _group(kids) if kids else '<mi></mi>'
                _ACC = {'overrightarrow': '\u2192',      # →
                        'overleftarrow': '\u2190',      # ←
                        'overleftrightarrow': '\u2194',  # ↔
                        'vec': '\u20d7',                # 组合右箭头
                        'overline': '\u00af',           # ¯
                        'underline': '\u0332',          # ̲
                        'hat': '\u005e',                # ^
                        'bar': '\u00af'}
                # overrightarrow 用 stretchy 让箭头随内容拉长；
                # vec 是单个字符上的组合箭头，不拉伸。
                stretch = 'true' if name.startswith('over') else 'false'
                out.append('<mover accent="true"><mrow>%s</mrow>'
                           '<mo stretchy="%s">%s</mo></mover>'
                           % (inner, stretch, _ACC[name]))
                i = p
                continue
            if name in ('boldsymbol', 'pmb'):
                body, p = _read_arg(s, k)
                kids, _ = _parse_expr(body, 0)
                inner = _group(kids) if kids else '<mi></mi>'
                out.append('<mstyle mathvariant="bold">%s</mstyle>' % inner)
                i = p
                continue
            if name == 'mathbb' or name == 'mathbf':
                body, p = _read_arg(s, k)
                out.append('<mi mathvariant="normal">%s</mi>'
                           % escape(BB.get(body.strip(), body)))
                i = p
                continue
            # \text{...}
            if name == 'text' or name == 'mathrm':
                body, p = _read_arg(s, k)
                out.append('<mtext>%s</mtext>' % escape(body))
                i = p
                continue
            # 希腊字母
            if name in GREEK:
                out.append('<mi>%s</mi>' % escape(GREEK[name]))
                i = k
                continue
            # 符号宏
            if key in MACRO:
                out.append('<mo>%s</mo>' % escape(MACRO[key]))
                i = k
                continue
            # 函数名
            # 必须用 mathvariant="normal"：多字符 <mi> 的"自动正体"
            # 是 MathML 规范行为，但浏览器实现不一致（有渲染成斜体的），
            # 显式声明才可靠。见 CSS 里的 math mi[mathvariant=normal]。
            if name in FUNCS:
                out.append('<mi mathvariant="normal">%s</mi>' % escape(name))
                i = k
                continue
            # 未知宏：原样输出（不吞掉，便于发现）
            out.append('<mi>%s</mi>' % escape(name))
            i = k
            continue

        # ---- 上下标 ----
        if c in ('_', '^'):
            # 基底 = 前一个节点（没有则空）
            base = out.pop() if out else '<mi></mi>'
            arg, i2 = _read_script_arg(s, i + 1)
            a = (_mi_or_mn(arg) if not _need_parse(arg)
                 else _group(_parse_expr(arg, 0)[0]))
            # 后面是否紧跟另一个（x_1^2）
            peek = None
            j2 = i2
            while j2 < n and s[j2] in ' \t':
                j2 += 1
            if j2 < n and s[j2] in ('_', '^') and s[j2] != c:
                a2, i3 = _read_script_arg(s, j2 + 1)
                b2 = (_mi_or_mn(a2) if not _need_parse(a2)
                      else _group(_parse_expr(a2, 0)[0]))
                peek = (s[j2], b2)
                i2 = i3
            if peek:
                other, ob = peek
                if c == '_':
                    out.append('<msubsup>%s%s%s</msubsup>' % (base, a, ob))
                else:
                    out.append('<msubsup>%s%s%s</msubsup>' % (base, ob, a))
            elif c == '_':
                # msub/msup 的第二个子元素应是**单个表达式**。
                # <mfrac> 本身合法，但外面再包一层 <mrow> 更规范，
                # 也避免渲染器对多元素参数的理解差异。
                out.append('<msub>%s<mrow>%s</mrow></msub>' % (base, a))
            else:
                out.append('<msup>%s<mrow>%s</mrow></msup>' % (base, a))
            i = i2
            continue

        # ---- 分组 ----
        if c == '{':
            body, p = _read_arg(s, i)
            kids, _ = _parse_expr(body, 0)
            out.append(_group(kids))
            i = p
            continue
        if c == '}':
            i += 1
            continue

        # ---- 普通字符 ----
        if IDENT.match(c):
            j = i
            while j < n and IDENT.match(s[j]):
                j += 1
            word = s[i:j]
            # 多字母函数名整体输出为正体。
            # 原来要求后面紧跟 '([{'，导致单独的 $\max$、$\ln$ 被拆成
            # 单个字母逐个输出 —— 既错（m·a·x）又会渲染成斜体变量。
            if word in FUNCS:
                out.append('<mi mathvariant="normal">%s</mi>' % escape(word))
            elif len(word) == 1 and is_func_call(s, j):
                # 单字母函数：f(x)、g(x) 里的 f/g 是**函数名**，应排正体。
                # 原来一律按变量输出成 <mi>f</mi>，渲染成斜体。
                # 必须跳过 \left / \! 等，否则 f\!\left(x\right) 会漏判。
                out.append('<mi mathvariant="normal">%s</mi>' % escape(word))
            else:
                for ch in word:
                    out.append('<mi>%s</mi>' % escape(ch))
            i = j
            continue
        if c.isdigit() or c == '.':
            j = i
            while j < n and (s[j].isdigit() or s[j] == '.'):
                j += 1
            out.append('<mn>%s</mn>' % escape(s[i:j]))
            i = j
            continue
        if c in '+-*/=<>()[]|':
            # 定界符（圆括号、方括号、竖线）显式声明**不可拉伸**。
            #
            # <mo> 默认 stretchy=true，会跟随所在 mrow 的总高度拉伸。
            # 于是 f(x)={cases} 里的 ( ) 会被右侧 2 行高的分段函数
            # 一起拉到同样高度 —— 就是用户说的"f(x) 的括号特别大"。
            #
            # 中学数学里 f(x)、[a,b]、|x| 这些 99% 不需要拉伸，
            # 而 Word 端 OMML 本来就没有 stretchy 概念（默认不拉伸），
            # 所以这里设 false 反而让两端更一致。
            if c in '()[]|':
                out.append('<mo stretchy="false">%s</mo>' % escape(c))
            else:
                out.append('<mo>%s</mo>' % escape(c))
            i += 1
            continue
        if c in ' \t\n':
            i += 1
            continue
        out.append('<mo>%s</mo>' % escape(c))
        i += 1
    return out, i


def _need_parse(s):
    """参数里是否还有需要递归解析的结构"""
    return bool(re.search(r'\\[a-zA-Z]|[_^{}]', s or ''))


def _group(kids):
    if not kids:
        return '<mi></mi>'
    if len(kids) == 1:
        return kids[0]
    return '<mrow>%s</mrow>' % ''.join(kids)


def latex_inline(s):
    """行内 LaTeX → 完整 <math> 元素（MathML Core）

    人工录入的题目用它渲染 $...$ 包裹的公式。
    例如 $\\frac{1}{4}x$ → <math><mfrac>...</mfrac><mi>x</mi></math>
    """
    t = (s or '').strip()
    if not t:
        return ''
    kids, _ = _parse_expr(t, 0)
    if not kids:
        return ''
    return ('<math xmlns="http://www.w3.org/1998/Math/MathML" '
            'display="inline">%s</math>' % _group(kids))



# LaTeX 源码里不该出现的控制字符。
# 录入时若用了非 raw 的 Python 字符串，``\varnothing`` 的 ``\v``
# 会被解释成垂直制表符 U+000B，于是存进库的是 ``\x0barnothing``：
#   - HTML 端：\x0b 不可见，页面显示 ``arnothing``
#   - Word 端：U+000B 是 XML 1.0 非法字符，parse_xml 抛异常
#              → omml_math 返回 None → **整个公式被丢弃**（空白）
# 两者都不报错，极难发现。
# 只还原 \x0b（垂直制表符 = \v）：
#   LaTeX 里 \v 开头的命令很少（\varnothing 最常见），
#   而正文里出现 U+000B 几乎必然是转义事故。
#   \x0c(换页) / \x07 / \x08 不做还原 ——
#   它们在文本里更可能是误录入，还原成 \f 反而造出错误命令。
_CTRL_LATEX = {
    '\x0b': 'v',
}


def repair_ctrl(s):
    """修复被 Python 转义破坏的 LaTeX 命令（如 \x0b + arnothing）。

    同时兜底删掉其余 XML 非法控制字符，
    避免它们混进 OMML 导致整个公式静默消失。
    """
    if not s:
        return s
    for ch, letter in _CTRL_LATEX.items():
        if ch in s:
            # 后面跟字母 → 还原成 \<letter>（拼回原命令）
            #
            # **必须用 lambda 而不是替换字符串**：
            # 替换串里的 `\\v` 会被 re 当成转义序列解析，
            # 写成 `'\\' + letter` 得到的不是字面反斜杠 + v。
            # lambda 的返回值不做转义解析，最安全。
            s = re.sub(re.escape(ch) + r'(?=[a-zA-Z])',
                       lambda m: '\\' + letter, s)
            # 剩余的（后面不是字母）直接删掉
            s = s.replace(ch, '')
    # 其余 XML 1.0 非法控制字符一律删除（保留 \t \n \r）
    s = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', s)
    return s


def latex_expand(s):
    r"""把 LaTeX 宏展开为 Unicode 纯文本，保留 \frac/\sqrt/上下标结构。

    Word 端（OMML）用它：先展开宏，再把剩下的结构交给
    split_rich() -> omml_segs()。不动结构是因为 split_rich
    已经能正确处理 \frac{}{}、\sqrt{}、_{}、^{}。

    HTML 端不需要它 —— 那边有完整的 latex_inline() 递归解析器。

    另外把「无花括号的上下标」补上花括号（x_1 -> x_{1}），
    否则 split_rich 认不出来（它只匹配 _{} 形式）。
    """
    if not s:
        return ''
    t = repair_ctrl(str(s))

    # 转义花括号：\{ \} -> { }
    # 不去反斜杠的话 Word 里会显示 \{1,2\}，
    # 而且 \{ 里的 { 会被后续的分式/上下标解析当成分组起点，引发连锁错误。
    t = t.replace('\\{', '{').replace('\\}', '}')

    # 去 \left \right 与间距命令
    t = re.sub(r'\\(left|right|middle)(?![a-zA-Z])', '', t)
    t = re.sub(r'\\[,;:!](?![a-zA-Z])', '', t)
    t = re.sub(r'\\(?:thinspace|medspace|thickspace|negthinspace)(?![a-zA-Z])', '', t)
    t = re.sub(r'\\(quad|qquad)(?![a-zA-Z])', ' ', t)

    # 希腊字母（长名优先，避免 \varphi 被 \phi 抢先）
    for name in sorted(GREEK, key=len, reverse=True):
        t = re.sub(r'\\' + name + r'(?![a-zA-Z])', GREEK[name], t)

    # 符号宏（长名优先：\leq 先于 \le）
    for key in sorted(MACRO, key=len, reverse=True):
        t = re.sub(re.escape(key) + r'(?![a-zA-Z])', MACRO[key], t)

    # \mathbb{X} / \mathbf{X}
    #
    # **必须在符号宏之后处理**，顺序反了会出静默错误：
    #   ``x\in\mathbb{Z}`` 若先展开 \mathbb → ``x\inZ``，
    #   此时 \in 后面是字母 Z，被负向前瞻 ``(?![a-zA-Z])`` 挡住
    #   → \in 不替换 → 落到"未知宏"分支去掉反斜杠 → 输出 ``xinZ``。
    #   Word 里显示成 xinZ（用户反馈的"∈ 显示成了 in"）。
    # 先处理符号宏则：``x∈\mathbb{Z}`` → ``x∈Z``，正确。
    #
    # HTML 端不受影响（走 latex_inline 递归解析，不用 expand），
    # 所以这个 bug 只在 Word 端出现，更难发现。
    def _bb(m):
        return BB.get(m.group(1).strip(), m.group(1))
    t = re.sub(r'\\(?:mathbb|mathbf)\s*\{([^{}]*)\}', _bb, t)

    # \text{...} / \mathrm{...}
    t = re.sub(r'\\(?:text|mathrm)\s*\{([^{}]*)\}', r'\1', t)

    # \dfrac / \tfrac -> \frac。
    # Word 的 OMML 没有 display/text 之分，三者完全等价；
    # 而 split_rich() 只认 \frac，保留 \dfrac 会让整个分式
    # 退化成普通文本（页面上显示 f(\dfrac{9}{2})）。
    # 归一必须在"保留结构命令"那步之前做，否则会被一起保留。
    t = re.sub(r'\\(?:frac|dfrac|tfrac)(?![a-zA-Z])', r'\\frac', t)

    # 未知宏：去掉反斜杠保留名字（不静默吞掉，便于发现）。
    # 但 \frac / \sqrt 必须保留反斜杠 —— 它们是要交给
    # split_rich() 继续解析的**结构**，丢掉反斜杠就变成普通文本
    # "frac{1}{4}"，渲染出来是错的。
    # 'begin' / 'end' 也要保留：cases 环境由 extract3.split_rich
    # 解析成 C 段。丢掉反斜杠会变成普通文本 "begin{cases}"。
    _KEEP = ('frac', 'dfrac', 'tfrac', 'sqrt', 'begin', 'end',
             # 向量 / 上划线 / 粗体：Word 端要转成 <m:acc>/<m:bar>/粗体 run，
             # 丢掉反斜杠就变成普通文本「overrightarrow{CA}」。
             'overrightarrow', 'overleftarrow', 'overleftrightarrow',
             # 不含 \underline：命令名里的下划线会与「补花括号」正则冲突
             # （_u 会被当成下标），而它在 K12 数学中几乎用不到。
             'vec', 'overline', 'hat', 'bar',
             'boldsymbol', 'pmb')

    def _unknown(m):
        return m.group(0) if m.group(1) in _KEEP else m.group(1)

    t = re.sub(r'\\([a-zA-Z]+)', _unknown, t)

    # 无花括号的上下标补花括号：x_1 -> x_{1}, x^2 -> x^{2}
    #
    # 【曾有的负向前瞻是个 bug】
    # 原来写 `_([0-9a-zA-Z])(?![{a-zA-Z0-9])`，要求下标字符后面
    # **不能**跟字母数字 —— 本意是避免误伤，实际把最常见的情况全废了：
    #
    #   ABCD-A_1B_1C_1D_1
    #     A_1 后面是 B → 前瞻失败，不展开
    #     B_1 后面是 C → 失败
    #     C_1 后面是 D → 失败
    #     D_1 后面是结尾 → 只有它展开
    #
    # 结果 Word 里显示成「ABCD-A _1B _1C _1D₁」——
    # 前三个下标变成字面量 `_1`，只有最后一个是对的。
    # 正方体、棱柱、多变量题（x_1+x_2）全中招。
    #
    # 按 LaTeX 规则，`_` 只作用于**下一个 token**，
    # 所以 `_1` 后面无论跟什么，下标都是 `1`。直接去掉负向前瞻即可。
    # 已加大括号的 `x_{12}` 不会命中（后面是 `{`），不受影响。
    # 同时支持命令：``^\\circ`` → ``^{\\circ}``。
    # 否则 Word 端会把 ^ 当字面量留下，显示成「90^∘」。
    # **必须先保护 \begin{..} / \end{..}**：
    # 否则 \begin{cases} 会被上面两条当成「begin 的下标是 {cases}」，
    # 变成 \begin_{cases}，cases 环境整个破掉。
    t = re.sub(r'\\(begin|end)\s*\{([a-zA-Z*]+)\}', r'\\\1@\2@', t)
    t = re.sub(r'_(\\[a-zA-Z]+|[^{\s])', r'_{\1}', t)
    t = re.sub(r'\^(\\[a-zA-Z]+|[^{\s])', r'^{\1}', t)
    t = re.sub(r'\\(begin|end)@([a-zA-Z*]+)@', r'\\\1{\2}', t)

    # \sqrt 后跟单字符时补花括号：\sqrt6 -> \sqrt{6}
    #
    # 与上下标同理，split_rich() 只认 \sqrt{..} 形式。不补的话
    # \sqrt6 切不出 S 段，落到未知宏分支：
    #   - HTML 端：输出 <mi>sqrt</mi><mn>6</mn> → 页面显示 "sqrt6"
    #   - Word 端：\ 单独成段、sqrt 成文本、6 成数字 → 显示 "\sqrt6"
    # 两者都不报错（第2批录入时答案卷里发现了 13 处，靠扫描才发现）。
    #
    # 两个排除条件：
    #   (?![{[])   —— 已有花括号 \sqrt{6}、可选参数 \sqrt[3]{x} 不动
    #   ([^\\\s{[]) —— 只吃单个「原子」，且不吃反斜杠，
    #                 否则 \sqrt\frac{1}{2} 会被切成 \sqrt{\frac}12
    t = re.sub(r'\\sqrt(?![{[])([^\\\s{[])', r'\\sqrt{\1}', t)

    return t
