# -*- coding: utf-8 -*-
"""高考卷排版模板配置

设计原则：每种题型是一个独立的「矩形模块」，模块内部格式正确，
整卷就是模块按顺序垒起来。改这里的参数，所有试卷同步生效。

新增题型只需：
  1) 在 QTYPES 里注册；
  2) 在 make_paper.py 里写一个 render_xxx(q, ctx) 函数。
"""

# ============ 一、页面 ============
PAGE = {
    "width": 21.0,          # cm
    "height": 29.7,
    "margin_lr": 2.4,
    "margin_tb": 2.2,
}
# A4 减去左右边距后的可用正文宽度
BODY_W = PAGE["width"] - 2 * PAGE["margin_lr"]      # 16.2 cm

# ============ 二、字体与字号 ============
FONT = {
    "cn": "宋体",
    "en": "Times New Roman",
    "title": "黑体",
    "math": "Cambria Math",
    "mono": "Consolas",
}
SIZE = {
    "title": 16,
    "subtitle": 11,
    "section": 11,
    "stem": 10.5,
    "option": 10.5,
    "figure_caption": 8,
    "answer": 10.5,
    "analysis": 9.5,
    "meta": 9.5,
    "note": 9,
    "source": 9,
}

# ============ 三、卷头 ============
TITLE = {
    "align": "center",
    "space_after": 2,
    "sub_space_after": 4,
    "rule_size": 16,        # 分隔线粗细（1/8 pt 的倍数）
    "rule_space": 5,
    "meta_col_w": [3.0, 13.2],
}

# ============ 四、分节标题 ============
SECTION = {
    "size": 11,
    "bold": True,
    "color": (0x1F, 0x38, 0x64),
    "space_before": 8,
    "space_after": 3,
}

# ============ 五、题干 ============
STEM = {
    "size": 10.5,
    "space_before": 6,
    "space_after": 2,
    "line": 1.4,
    "num_bold": True,
    "keep_with_next": True,     # 题干与紧随的选项/插图不分离
}

# ============ 五之二、题号位置 ============
# 规则：题号独占左侧一列，题干/选项/插图/留白整体右移，
#       题号与内容分离 → 扫题时一眼定位到第 N 题。
# 悬挂缩进（hanging indent）：题干换行后与题干首行对齐，
#       不会跑到题号下面——这是高考试卷的标准排法。
QNUM = {
    "hang_cm": 0.85,        # 悬挂缩进宽度（题号列宽）
    "color": (0x1F, 0x38, 0x64),   # 与答案卷同色，全卷统一
    "bold": True,
    "html_min_em": 2.4,     # HTML 端题号列最小宽度
}

# ============ 六、选择题选项 ============
# 规则：按「选项文本长度」决定列数，列宽固定 → 跨题对齐
OPTIONS = {
    "size": 10.5,
    "line": 1.25,
    "indent": 0,                # 由表格列位置控制，不再用缩进
    "col_rules": [
        # (选项最大字符数, 列数)
        (8, 4),                 # A.a B.b C.c D.d   → 四个并排
        (26, 2),                # 中等长度          → 两列两行
        (10 ** 6, 1),           # 较长              → 每行一个
    ],
    "space_after": 1,
}

# ============ 七、填空题 ============
# 规则：题干中的填空标记渲染为下划线
# 分段函数（cases）的渲染模式
#   "omml" —— 标准 <m:d> 矩阵（Word 原生，可编辑，推荐）
#   "text" —— 降级：左大括号 + 多行文本，100% 能显示但不可编辑
# 若 Word 里出现「大括号在但里面内容空白」，把这里改成 "text" 即可，
# 不用改代码逻辑。两条路径共用同一份行/列解析。
CASES_MODE = "omml"

FILL = {
    "size": 10.5,
    "space_before": 6,
    "space_after": 2,
    "line": 1.4,
    "blank": {
        # 题干中表示「待填」的标记 → 下划线
        # **半角 . 和全角 ． 都要认**。
        # PDF 提取会把原卷的全角「．」变成 ASCII 句点，
        # 21 道填空题里 14 道是半角、只有 3 道是全角。
        # 只写 ． 的话三分之二的填空处渲染不出下划线。
        #
        # 半角 . 的误伤风险（小数点 3.14、省略号）已排除：
        # 每条都要求句点处于「待填位置」——紧跟 = / 为 / 是，
        # 或位于句末、后接分句标点与括注。
        "patterns": [
            # LaTeX 填空标记：人工录入时会写 \underline{\hspace{2em}}，
            # 但三端都不支持 \underline（命令名里的下划线与下标正则冲突），
            # 不转换的话页面上直接显示这个源码。
            # 在这里识别后交给原生下划线渲染，与 ____ 走同一条路径。
            r"\\underline\s*\{\s*\\hspace\s*\{[^}]*\}\s*\}",
            r"\\underline\s*\{[^}]*\}",
            r"_{2,}",                       # ____
            r"＿{1,}",                       # 全角下划线
            # 「离心率为 ．」「a = .」—— 紧跟在 为/是/= 之后
            r"(?<=[为是＝])\s*[.．]",
            r"(?<==)\s*[.．]",
            # 句末孤立句点：「…共有 种.」「…取值范围是 .」
            #
            # **必须加后顾断言 (?<![_＿\u3000])**：
            # 题干是「…有__________．」时，正则先匹配了 `_{2,}`，
            # 接着从句号处继续匹配，句号位于串尾 → 命中本条
            # → **一个填空处渲染出两段下划线**（末尾还吞掉了句号）。
            # 第 2 批两道填空题都是这样。
            # 句号紧跟填空标记时它只是句号，不是第二个空。
            r"(?<![_＿\u3000])[.．](?=\s*(?:[（(]|$|[；，。！？；])）?)",
            # 「θ=，」等号后直接标点（下划线丢失时的兜底）
            r"(?<==)(?=[，。；])",
        ],
        "char": "\u3000",      # 下划线载体（全角空格，兜底用）
        "chars": 5,             # 个数（CSS 未生效时的兜底长度）
        "width_em": 4.0,        # 下划线宽度（em）——实际生效的画法
        "style": "single",      # single / double
    },
}

# ============ 八、解答题答题空间 ============
SOLVE = {
    "size": 10.5,
    "space_before": 6,
    "space_after": 2,
    "line": 1.4,
    "answer_space": {
        "base": 1.6,            # 基础高度 cm
        "per_score": 0.28,      # 每分增加的高度
        "min": 3.0,
        "max": 7.2,
        "row_h": 20,            # 空白行的固定行高（磅）
    },
    "last_scale_steps": (1.0, 0.82, 0.66, 0.5, 0.34, 0.18),
    # 末页若为空，按上表逐档缩减最后一题留白，消除空白页
}

# ============ 九、插图 ============
FIGURE = {
    "dpi": 300,
    "target_kb": 30,            # 线条图目标体积
    "photo_kb": 35,             # 照片类目标体积
    # 小题：插图在右、选项在左
    "choice": {
        "layout": "left_opts_right_fig",
        "w_single": 4.9,        # 单张图区宽度
        "w_multi_base": 1.1,    # 多图：base + step × 张数
        "w_multi_step": 1.3,
        "w_multi_max": 6.4,
        "per_row": 4,           # 每行最多几张
        "cell_pad": 0.25,
        "max_h": 4.6,
    },
    # 大题：插图在题目文字下方，靠右
    "solve": {
        "layout": "below_right",
        "w_single": 4.9,
        "w_multi_base": 1.1,
        "w_multi_step": 1.3,
        "w_multi_max": 6.4,
        "per_row": 4,
        "max_h": 4.6,
    },
    # 图注：{n}=图序号，{q}=题号
    "caption": {
        "show": True,
        # {n}=图序号（该题内从 1 起），{q}=题号
        "text": "第{q}题图",        # 单图：标注题号，便于组卷后回溯
        "text_multi": "第{q}题图{n}",  # 多图：题号 + 图序号
        "size": 8,
        "color": (0x88, 0x88, 0x88),
        "align": "center",
        "space_after": 2,
    },
}

# ============ 十、答案与解析卷 ============
ANSWER_SHEET = {
    "size": 10.5,
    "space": 6,             # 每题上间距
    "indent": 0.6,
    "answer_color": (0xC0, 0x00, 0x00),
    "source_color": (0x80, 0x80, 0x80),
    "analysis_color": (0x33, 0x55, 0x33),
    "label_answer": "【答案】",
    "label_source": "【来源】",
    "label_analysis": "【解析】",
    "source_template": "{src} · 第 {num} 题",
    "no_answer_text": "（原卷无答案）",
}

# ============ 十一、题型注册表 ============
# 每种题型对应一个渲染模块；新增题型在此登记
QTYPES = {
    "单选": {"renderer": "render_choice", "blank": False, "fig_layout": "choice"},
    "多选": {"renderer": "render_choice", "blank": False, "fig_layout": "choice"},
    "选择": {"renderer": "render_choice", "blank": False, "fig_layout": "choice"},
    "填空": {"renderer": "render_fill", "blank": False, "fig_layout": "solve"},
    "解答": {"renderer": "render_solve", "blank": True, "fig_layout": "solve"},
    "实验": {"renderer": "render_solve", "blank": True, "fig_layout": "solve"},
    "计算": {"renderer": "render_solve", "blank": True, "fig_layout": "solve"},
}

# ============ 十二、分节识别规则 ============
# 用于从试卷中判断某题属于哪个分节（决定题型与是否留白）
SECTION_RULES = {
    # 科目 -> [(题号范围, 题型, 是否留白)]
    "数学": [
        ((1, 8), "单选", False),
        ((9, 11), "多选", False),
        ((12, 14), "填空", False),
        ((15, 19), "解答", True),
    ],
    "物理": [
        ((1, 11), "单选", False),
        ((12, 16), "解答", True),
    ],
}


def qtype_of(subject, num):
    """按规则判断题目类型"""
    for (lo, hi), t, blank in SECTION_RULES.get(subject, []):
        if lo <= num <= hi:
            return t, blank
    return "解答", True


def cols_for(maxlen):
    """按选项**渲染宽度**决定列数。

    单位是「半角字符宽」，不是源码字符数（见下方渲染宽度估算）。

    容量核算（A4，BODY_W=16.2cm，字号 10.5pt）：
        半角字符 ≈ 0.5em = 5.25pt ≈ 0.185cm
        4 列 → 每列 4.05cm ≈ 可容纳 19.9 字符宽（已扣「A．」前缀 2 宽）
        2 列 → 每列 8.10cm ≈ 41.7
        1 列 → 16.20cm   ≈ 85.5

    当前阈值（8 / 26）比容量留了很大余量，偏保守——
    好处是不会溢出，代价是部分本可并排的选项被降列。
    要放宽就把阈值往上调，但不要超过上表的容量。
    """
    for lim, cols in OPTIONS["col_rules"]:
        if maxlen <= lim:
            return cols
    return 1


def col_capacity(cols):
    """该列数下每列能容纳的渲染宽度（用于校验是否放得下）"""
    char_cm = 0.5 * OPTIONS["size"] / 28.35      # 半角字符宽（cm）
    return BODY_W / cols / char_cm - 2           # 扣掉「A．」前缀


# ============ 六之二、公式渲染宽度估算 ============
# 规则：**分数/根号按"渲染后的视觉宽度"算，不按源码字符数算。**
#
# 曾有两次错误估算，方向相反：
#   1. 把 \frac{...}{...} 替换成 'xx'（2 字符）→ 估太短
#      $f(2017)<f(2018)<f(2019)$ 被判 4 列，实际放不下被 CSS 裁掉
#   2. 按源码字符数算 → 估太长
#      $\dfrac{4}{3}$ 源码 13 字符，但渲染成上下堆叠的分数只有约 1 字符宽，
#      被误判成 2 列；其实四个选项 $\dfrac{4}{3}$ 这类完全排得下一行。
#
# 关键在于 \frac{a}{b} 是**上下两行**：宽度 = max(w(a), w(b))，
# 而不是 w(a)+w(b)。\sqrt{x} 同理，只比内容稍宽。
import re as _re

_FRAC_RE = _re.compile(r'\\(?:d|t)?frac\s*(?=\{)')
_SQRT_RE = _re.compile(r'\\sqrt\s*(?:\[[^\]]*\])?\s*(?=\{)')
# 渲染为正体文字的命令：宽度按名字长度算（sin → 3 字符）
_TEXT_CMDS = {'sin', 'cos', 'tan', 'cot', 'sec', 'csc', 'arcsin', 'arccos',
              'arctan', 'sinh', 'cosh', 'tanh', 'ln', 'lg', 'log', 'exp',
              'max', 'min', 'lim', 'sup', 'inf', 'arg', 'deg', 'dim', 'det',
              'gcd'}
# 不占视觉宽度的命令（间距与括号定界）
_ZERO_CMDS = {'!', ',', ';', ':', 'quad', 'qquad', 'left', 'right', 'big',
              'Big', 'bigg', 'Bigg'}


def _take_group(s, i):
    """s[i] == '{'，返回 (内容, 结束下标)。花括号可嵌套。"""
    depth, j = 0, i
    while j < len(s):
        if s[j] == '{':
            depth += 1
        elif s[j] == '}':
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
        j += 1
    return s[i + 1:], len(s)


def _rw(s):
    """递归估算一段 LaTeX 的渲染宽度（单位：半角字符宽）"""
    total, i = 0.0, 0
    while i < len(s):
        c = s[i]
        if c == '{':                                   # 分组：宽度即内容宽度
            inner, i = _take_group(s, i)
            total += _rw(inner)
            continue
        if c == '\\':
            m = _FRAC_RE.match(s, i)
            if m:                                      # \frac{a}{b} 上下堆叠
                j = m.end()
                num, j = _take_group(s, j) if j < len(s) and s[j] == '{' \
                    else (s[j], j + 1)
                den, j = _take_group(s, j) if j < len(s) and s[j] == '{' \
                    else (s[j], j + 1)
                # 分数线左右各留一点，故 +0.4
                total += max(_rw(num), _rw(den)) + 0.4
                i = j
                continue
            m = _SQRT_RE.match(s, i)
            if m:                                      # \sqrt{x} 略宽于内容
                j = m.end()
                inner, j = _take_group(s, j) if j < len(s) and s[j] == '{' \
                    else (s[j], j + 1)
                total += _rw(inner) + 0.8
                i = j
                continue
            m = _re.match(r'\\([a-zA-Z]+|.)', s[i:])
            if m:
                name = m.group(1)
                i += m.end()
                if name in _ZERO_CMDS:
                    total += 0.0
                elif name in _TEXT_CMDS:
                    total += len(name) * 0.9
                else:
                    total += 1.0                       # 单字符命令按 1
                continue
        if c in '^_':                                  # 上/下标：压扁后更窄
            i += 1
            inner, i = _take_group(s, i) if i < len(s) and s[i] == '{' \
                else (s[i], i + 1)
            total += _rw(inner) * 0.65
            continue
        if c in ' \t':
            i += 1
            continue
        total += 2.0 if ord(c) > 0x2E80 else 1.0       # 中日韩字符算 2 宽
        i += 1
    return total


def render_width(text):
    """估算一段含 $...$ 文本的渲染宽度。

    行内公式按渲染宽度算，行外文本按字符数算（中文 2，西文 1）。
    """
    if not text:
        return 0.0
    total = 0.0
    for seg in _re.split(r'(\$[^$]*\$)', text):
        if not seg:
            continue
        if len(seg) >= 2 and seg[0] == '$' and seg[-1] == '$':
            total += _rw(seg[1:-1])
        else:
            for ch in seg:
                total += 2.0 if ord(ch) > 0x2E80 else 1.0
    return total
