# 渲染问题排查

按**看到的症状**查，每节给出：现象 → 诊断 → 做法 → 验证。

## 已验证项（用户实测确认，不需要再反复确认）

| 项目 | 状态 | 说明 |
|---|---|---|
| 分式 $\frac{a}{b}$ | ✓ 显示正确 | 分数线正常，不平铺 |
| 根号 $\sqrt{x}$ | ✓ 显示正确 | 完整包住被开方式 |
| 嵌套根式 $\sqrt{5}+\sqrt{10\sqrt5}$ | ✓ 显示正确 | |
| 分段函数 cases | ✓ 显示正确 | Word 用 `m:m` 包裹后内容正常 |

用户 2026-09-05 打开 HTML 实测确认。**后续批次不必再就这些项目反复征求确认**，
有新结构（如新的矩阵、极限符号等）时再单独确认。

## 症状速查表

| 看到的 | 查这一节 |
|---|---|
| 页面显示 `\frac{1}{2}` 这种源码 | [公式显示成源码](#a1-公式显示成源码命令名) |
| 显示 `dfrac94`、`arnothing`、`xinZ` | [A1](#a1-公式显示成源码命令名) |
| 显示 `90^\ c i r c` | [A2](#a2-命令参数只取到单个字符) |
| 公式整段消失、页面中间空白 | [A3](#a3-公式整段消失) |
| Word 里空白但 HTML 正常 | [A3](#a3-公式整段消失)、[A4](#a4-只在-word-端异常) |
| ∈ 显示成 in | [A4](#a4-只在-word-端异常) |
| 分数下标只有最后几个生效 | [A5](#a5-连续上下标只生效一部分) |
| `(x-1)²` 的平方丢了 | [A6](#a6-基底提取失败) |
| 该正体的斜体、该斜体的正体 | [A7](#a7-正斜体判定) |
| 显示 `sqrt6`、`\sqrt6` | [A9](#a9-sqrt-后跟单字符只影响-word-端) |
| `f(x)` 括号被撑得很大 | [B1](#b1-fx-的括号被-cases-撑大) |
| 选项只剩 `A．B．C．D．` | [B2](#b2-选项被-css-裁掉) |
| 题目挤到页面右侧 | [B3](#b3-题目挤到页面右侧) |
| 答案卷题号全是 0 | [B4](#b4-答案卷题号是-0-或与试卷错位) |
| Word 统计公式数对不上 | [C1](#c1-统计-word-公式必须算上表格) |
| 改了代码没生效 | [D1](#d1-改代码没生效) |

---

# A. 公式渲染

## A1 公式显示成源码/命令名

**现象**：页面上出现 `\frac{1}{2}`、`dfrac94`、`arnothing`、`xinZ`、`subsetneq`。

**诊断**：命令不在符号表里，走了「未知宏」分支，命令名被当文本输出。
确认方式——看输出里是命令名本身（不是乱码）：

```html
<mi>dfrac</mi><mn>9</mn><mn>4</mn>   ← 页面显示 dfrac94
```

**做法**：在 `py/mathml.py` 的 `MACRO` 表里补该命令，三端同步：

| 层 | 文件 | 补在哪 |
|---|---|---|
| HTML / Word | `py/mathml.py` | `MACRO` 字典 |
| 前端练习页 | `src/app/render.js` | `MACRO` 字典 |

`\dfrac` / `\tfrac` 走 `latex_expand` 归一成 `\frac`（OMML 无 display/text 之分）。
归一的位置要在「保留结构命令」**之前**，否则 `\dfrac` 被当结构保留，
`split_rich` 再匹配 `\frac` 就失败了。

`\mathbb{R}` 渲染为普通 `R`：Unicode 黑板粗体（ℝ ℕ ℤ）在很多中文字体里缺字形，
会显示成方块。

**验证**：源码泄漏扫描（见 [C3](#c3-每批必跑源码泄漏扫描)）该项为 0。

## A2 命令参数只取到单个字符

**现象**：`90^\circ` 显示成 `90^\ c i r c`。

**诊断**：参数读取对非 `{...}` 形式只取单字符，于是取到 `\`，
剩下 `circ` 被当三个变量 c·i·r·c。

**做法**：参数以 `\` 开头时读**完整命令名**（连续字母）。

**验证**：`ML.latex_inline(r'90^\circ')` 输出含 `<mo>&#176;</mo>` 或 `°`，无 `circ`。

## A3 公式整段消失

**现象**：页面中间空一块，或 Word 里只有括号没有内容，且不报错。

**诊断**：三处会静默吞掉公式，逐个排查：

1. **XML 非法字符** → `parse_xml` 抛异常 → `omml_math` 返回 `None` → `rich()` 跳过
   - 典型：U+000B（Python 把 `\v` 解释成垂直制表符）
   - 典型：`&#0;` —— XML 1.0 不允许空字符的字符引用
2. **`rich()` 缺分支** → 段类型没人处理，直接丢弃
3. **基底提取失败** → 段停在中间态，渲染层丢弃（见 [A6](#a6-基底提取失败)）

**做法**：

```python
# 1. repair_ctrl()：\x0b + 后续字母 → 还原成 \v + 字母（拼回 \varnothing 等）
#    只还原 \x0b。\x0c/\x07/\x08 更可能是误录入，还原会造出错误命令。
#    **必须用 lambda**：替换串里的 \\ 会被 re 当转义序列吃掉。
s = re.sub(re.escape(ch) + r'(?=[a-zA-Z])', lambda m: '\\' + letter, s)
# 2. 其余 XML 非法控制字符删除（保留 \t \n \r）
s = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', s)
```

排查这类问题的顺序：数据在 `bank.json` 里吗 → `split_rich` 切出来了吗 →
渲染层有对应分支吗。

**验证**：**断言解析结果，不检查字符串**——字符串看着对，解析可能失败：

```python
d = docx.Document(); p = d.add_paragraph()
rich(p, r'$f(x)=\begin{cases}x^2, & x\le0\\4\sin x,&0<x\le\pi\end{cases}$', 10.5)
assert p._p.xml.count('<m:oMath>') == 1   # 公式没被丢弃
assert p._p.xml.count('<m:d>') == 1       # cases 结构在
```

## A4 只在 Word 端异常

**现象**：HTML 正常，Word 异常（或反过来）。

**诊断**：两端走**不同的代码路径**：

| | HTML | Word |
|---|---|---|
| 解析器 | `mathml.latex_inline()` 递归 | `mathml.latex_expand()` + `split_rich` |
| 结构 | 直接出 MathML | 展开宏 → 切段 → OMML |

所以一端的修复不会自动同步到另一端。

**案例**：`x\in\mathbb{Z}` 的 ∈ 在 Word 里变 `in`。
`\mathbb` 先展开成 `Z`，于是 `\in` 后面是字母 `Z`，
被负向前瞻 `(?![a-zA-Z])` 挡住 → 不替换 → 落到未知宏去掉反斜杠 → 输出 `xinZ`。

**做法**：`latex_expand` 里**符号宏（GREEK + MACRO）必须在 `\mathbb` / `\text` 之前处理**。

**验证**：两端同口径统计（见 [C2](#c2-两端结构数同口径统计)）。

## A5 连续上下标只生效一部分

**现象**：`ABCD-A_1B_1C_1D_1` 只有末尾的 `D_1` 变成下标。

**诊断**：正则里的负向前瞻 `(?![{a-zA-Z0-9])` 挡住了后面跟字母的情况。

**做法**：上下标参数的匹配条件要放行**大写字母和数字**：

```python
# 错：A_1 后面是 B → 前瞻失败
re.sub(r'_([0-9a-zA-Z])(?![{a-zA-Z0-9])', ...)
# 对：放行大写与数字
```

**验证**：`ABCD-A_1B_1C_1D_1` 里 4 个 `1` 全部成下标。

## A6 基底提取失败

**现象**：`(x-1)^2` 的平方整个消失；`\complement_U A` 的下标 `U` 消失。

**诊断**：基底提取按优先级尝试，前几条规则全部落空就会失败：

| 顺序 | 规则 | 覆盖 |
|---|---|---|
| 1 | 函数名整词（`\log` `\sin`） | 函数名 |
| 2 | 连续数字串 | `90^` |
| 3 | 配对括号 | `(x-1)^2` ← 闭括号不是字母数字，必须单独一条 |
| 4 | 单个字符 | `x^2` |
| 5 | **紧邻的单个非空白字符**（兜底） | `∁_U` ← `∁` 不是字母数字 |

第 3 条（括号配对）和第 5 条（兜底）是踩坑后补的。

**做法**：按上表五条顺序实现，缺一不可。

**验证**：`\complement_U A` 渲染出 `∁` 带下标 `U`（不是空）；
`(x-1)^2` 的平方在。

## A7 正斜体判定

**现象**：区间 `(0,1)` 全斜体；`f(x)` 的 f 斜体；Word 里公式全斜体。

**诊断**：

- **HTML**：MathML 规范说 `<mn>`/`<mo>` 该正体，但浏览器实现不一致 → 必须显式写 CSS
- **Word**：OMML 数学区的 `<m:t>` **默认就是斜体**，即使 run 里没有 `<m:i/>`
  ——从 XML 上完全看不出问题

**做法**：

HTML 端显式声明 + 对非变量加 `mathvariant`：

```css
math mi{ font-style:italic; }                       /* 变量 → 斜体 */
math mn, math mo, math mtext{ font-style:normal; }  /* 数字/括号 → 正体 */
math mi[mathvariant="normal"]{ font-style:normal; }
```

Word 端**每个 run 都显式写 `<m:sty>`**（正体 `p` / 斜体 `i`），一个都不能省。

判定规则：

| 内容 | 字体 |
|---|---|
| 单个字母 + 后面跟左括号（`f(x)`） | 正体（函数名） |
| `\log` `\sin` `\max` 等 | 正体 |
| `\mathbb{R}` | 正体 |
| `(0,1)` `-1` `+` | 正体 |
| `x` `y` `n` `a` `m` | **斜体**（变量） |

**必须跳过间距命令**：`f\!\left(x\right)` 里 f 后面先是 `\!` 再是 `\left`，
不跳过就漏判。

**验证**：Word 产物里 `无 sty 的 run` 数为 0。

## A8 cases 分段函数的标准写法

**现象**：Word 里「大括号在、里面内容空白」；HTML 输出 `begin{cases}` 源码。

**诊断**：连续报了三轮才查对——前两轮凭印象猜，越改越糟；
第三轮查 OOXML 规范，两个错误一次定位。

**做法**：OMML 的 `m:d` 必须长这样：

```xml
<m:d>
  <m:dPr>
    <m:begChr m:val="&#123;"/>   <!-- { -->
    <m:sepChr m:val=""/>         <!-- 列间无分隔符 -->
    <m:endChr m:val=""/>         <!-- 右侧无分隔符 -->
    <m:grow m:val="on"/>         <!-- ST_OnOff 标准值 -->
    <m:shp m:val="match"/>       <!-- 分隔符高度跟随内容 -->
  </m:dPr>
  <m:e><m:m><m:mPr><m:mcs><m:mc><m:mcPr>
    <m:count m:val="2"/><m:mcJc m:val="left"/>
  </m:mcPr></m:mc></m:mcs></m:mPr>
    <m:mr>...</m:mr>             <!-- 每行 -->
  </m:m></m:e>
</m:d>
```

四个要点：

1. `m:e` 里**必须包一层 `m:m`**（矩阵）—— 直接放 `m:mr` 会渲染成空壳
2. `dPr` 里**没有 `m:algn`** —— CT_DPr 的 sequence 只有
   begChr/sepChr/endChr/grow/shp/ctrlPr。列对齐写在 `m:mcPr` 的 `m:mcJc`
3. `sepChr` 是**行内列分隔符**，写 `|` 会在表达式和条件之间插竖线。cases 应该是空
4. 属性顺序按 CT_DPr 的 sequence

**降级开关**：`paper_template.py` 的 `CASES_MODE` 改成 `"text"`，
走「`{` + 多行文本」，100% 能显示但不可编辑。

**验证**：见 [A3](#a3-公式整段消失) 的断言代码。

## A9 `\sqrt` 后跟单字符，只影响 Word 端

**现象**：`\sqrt6` 在 HTML 里正常，Word 里显示成 `\sqrt6` 或 `sqrt6`。

**诊断**：与 [A4](#a4-只在-word-端异常) 同源——两端路径不同。
`latex_inline`（HTML）是递归解析器，自己能处理单字符参数；
`latex_expand` + `split_rich`（Word）只认 `\sqrt{..}` 形式，
切不出 S 段就落到未知宏分支。

上下标早就补了花括号（`x_1 → x_{1}`），`\sqrt` 漏了——
因为录入时习惯写 `\sqrt{6}`，这个坑一直没暴露，
直到第2批录入写了一批 `\sqrt6` 才发现。

**做法**：在 `latex_expand` 末尾补花括号，与上下标同一位置：

```python
t = re.sub(r'\\sqrt(?![{[])([^\\\s{[])', r'\\sqrt{\1}', t)
```

两个排除条件：

| 条件 | 防止 |
|---|---|
| `(?![{[])` | 破坏已有的 `\sqrt{6}` 和 `\sqrt[3]{x}` |
| `([^\\\s{[])` | 吃掉反斜杠把 `\sqrt\frac{1}{2}` 切成 `\sqrt{\frac}12` |

**验证**：13 处实测用例全绿，含防误伤。

**数据层也写规范**：代码兜底之外，录入时统一写 `\sqrt{6}`，双保险。

---

# B. 布局排版

## B1 `f(x)` 的括号被 cases 撑大

**现象**：`f(x)={cases}` 里 `f(x)` 的圆括号和分段函数一样高。

**诊断**：`<mo>` 默认 `stretchy=true`，会跟随所在 `mrow` 的总高度拉伸。
调 `rowspacing` / `framespacing` 都收不住——**问题不在 cases 的 `{`**。

**做法**：定界符 `()[]|` 一律输出 `<mo stretchy="false">`。
中学数学里 f(x)、[a,b]、|x| 基本不需要拉伸；
而 Word 端 OMML 本来就不拉伸，这样改两端更一致。

cases 的 `{` 保持 `stretchy="true"` —— 它本来就该撑高。

HTML 端压低 cases 高度用三管齐下：

```xml
<mrow><mo stretchy="true">{</mo>
  <mstyle displaystyle="false">     <!-- 最关键：非展示模式行高更小 -->
    <mtable columnspacing="0.6em" rowspacing="0.1ex"
            framespacing="0 0" columnalign="left">...</mtable>
  </mstyle></mrow>
```

**验证**：`latex_inline(r'f(x)=...')` 输出含 `<mo stretchy="false">(</mo>`。

## B2 选项被 CSS 裁掉

**现象**：只剩「A．B．C．D．」看不到内容，但 HTML 源码里选项都在。

**诊断**：分列时把公式算短了。`$f(2017)<f(2018)<f(2019)$` 被算成 2 字符 → 判 4 列，
实际渲染 20+ 字符 → `overflow:hidden` 裁掉。
MathML 是整体元素，**超出即消失**（不像文本能用省略号截断）。

**做法**：

1. `_math_len()` 按公式**视觉宽度**算：`\frac{a}{b}` 取 max 不是相加，
   `\sqrt[n]{x}` 加 0.8，上标 `0.65·w(n)`，函数名按名字长度，中文算 2
2. 含 `$...$` 的选项加 `.opts-noclip`，`overflow:visible`

**只在 HTML 端出现** —— Word 没有 overflow 概念。这个差异是判断线索。

**验证**：短选项 4 列、中等公式 2 列、长公式 1 列，且无空选项。

## B3 题目挤到页面右侧

**现象**：题号在左，内容整体偏右。

**诊断**：`grid-row: 1 / -1` 的 `-1` 指向**显式网格**的最后一条线，
而 `.q` 没定义 `grid-template-rows`（行是隐式生成的），覆盖不到所有行。

**做法**：改用嵌套容器，`.q` 只有两个 grid item：

```html
<div class="q">
  <div class="qnum">1．</div>
  <div class="qmain">   ← 题干/选项/插图/留白全在这里，内部流式排布
```

题号之后的内容不会再流回第 1 列。

**配套**：题号左凸后，选项表格、插图、留白、解析段都要一起缩进（Word 端用
`w:tblInd` 和段落缩进）。带图题的选项在外层表格 cell 里，
**外层已缩进，cell 内不能再缩进一次**，用 `isinstance(container, _Cell)` 区分。

**验证**：三种题型（选择/填空/解答）的题干、选项、图都包在 `.qmain` 里。

## B4 答案卷题号是 0 或与试卷错位

**现象**：答案卷全是「0．」；或题号对但内容对不上。

**诊断**：**顺序错比题号错危险**——题号一眼能看见，顺序错很难发现。
孩子对着答案卷找第 5 题，看到的是另一道题的解析。

试卷走 `auto_sections()` 重排 `num = 1..N` 并按 `sort_key` 排序，
答案卷如果直接传 `picked`，就用原始 `num`（人工录入默认 0）和原始顺序。

**做法**：**两卷共用 `order_and_number()`**，排序键收敛到
`make_paper.sort_key()` 一处：`(科目出现顺序, 题型序, 题号, id)`。

**验证**：抽题对照**题干与解析的语义**，不只是比题号序列
（两份都是 1..10 但内容可能错位）：

```
题号 1 → 题干"定义在 R 上的奇函数 f(x) 满足 f(2-x)"
       → 解析"由 f(2-x)=f(x) 知图象关于直线 x=1"  ✓ 语义吻合
```

## B5 屏幕预览不像 A4

**现象**：屏幕排版与打印不一致。

**诊断**：`.paper` 的 padding 与 `@page` 的页边距用了不同的值。

**做法**：屏幕把 `.paper` 做成一张真 A4 纸，padding **直接用页边距值**；
打印时归零。

```css
@media screen{ .paper{ width:210mm; min-height:297mm; padding:22mm 24mm; } }
@media print { .paper{ width:auto; padding:0; } }   /* 必须归零 */
```

打印归零不能省：`padding` 只在整个元素的首尾，多页文档第 2 页起会多叠加一次。

---

# C. 数据与校验

## C1 统计 Word 公式必须算上表格

**现象**：统计 Word 的 `<m:f>` 只有 6 个，以为公式丢了。

**诊断**：**选项在表格里**，只数 `d.paragraphs` 会漏掉大部分。

**做法**：

```python
full = ''.join(p._p.xml for p in d.paragraphs)
for t in d.tables:                      # ← 必须加
    for row in t.rows:
        for c in row.cells:
            full += c._tc.xml
# m:f = 19  ← 与 HTML 一致
```

**每次统计 Word 都要带表格。** 这个坑导致过一次误判。

## C2 两端结构数同口径统计

**现象**：两端数字对不上，白排查一轮。

**诊断**：一端算 stem、另一端算 stem+opts，口径不同。

**做法**：两端用**同一份文本**统计：

```python
txt = (q['stem_text'] or '') + ' ∣ '.join(t for _, t in (q.get('opts') or []))
hh = BH._rich_html(txt)
ww = MP.omml_latex(q['stem_text'] or '') + \
     ''.join(MP.omml_latex(t) for _, t in (q.get('opts') or []))
```

匹配串对照：

| 结构 | HTML | Word |
|---|---|---|
| 分数 | `<mfrac>` | `<m:f>` |
| 根号 | `<msqrt>` | `<m:rad>` |
| 下标 | `<msub>` + `<msubsup>` | `<m:sSub>` + `<m:sSubSup>` |
| 上标 | `<msup>` + `<msubsup>` | `<m:sSup>` + `<m:sSubSup>` |

**验证**：四项数字 HTML 与 Word 完全相等。

## C3 每批必跑：源码泄漏扫描

命令名出现在输出里 = 该命令未被支持。**靠脚本扫，不靠肉眼看。**

```python
PATS = {
    'mid': r'>mid<', 'subsetneq': r'>subsetneq<', 'complement': r'>complement<',
    'setminus': r'>setminus<', 'underline': r'underline', 'hspace': r'hspace',
    'par': r'>par<', '反斜杠{': r'>\\{<', '$定界': r'>\$<',
    'begin': r'>begin<', 'dfrac': r'>dfrac<', '&#0;': r'&#0;',
    'notin': r'notin', 'arnothing': r'arnothing',
}
# HTML 与 Word 的 XML 都要扫，全部为 0 才通过
```

**补充新命令时，把它的旧名字（以及常见误写）一并加进这张表**——
扫得到才算真的修好了。

## C4 每批必跑：控制字符扫描

**必须 `json.load()` 之后再扫**——JSON 文本里控制字符是字面的 `\u000b`
六个字符，扫原始文本永远扫不到。

```python
import re, json
BAD = re.compile(r'[\x00-\x08\x0b\x0c\x0e-\x1f]')
bank = json.load(open('data/bank.json', encoding='utf-8'))
n = sum(len(BAD.findall(json.dumps(q, ensure_ascii=False))) for q in bank)
assert n == 0
```

## C5 清洗数据要同时清 `stem_text` 和 `stem` 列表

**现象**：清理了 `\underline` / `\par`，重新导出还在。

**诊断**：`_prep_fields` 是 **stem 列表优先**：

```python
if stem_lines:                      # ← 只要有 stem 列表
    stem = ' '.join(stem_lines)     # ← 就用它覆盖
else:
    stem = q.get('stem_text') or ''
```

只改 `stem_text`，会被脏的 `stem` 覆盖回去，且无任何报错。

**做法**：批量替换时两个字段一起清。踩过两次（underline 一次、`\par` 一次）。

---

# D. 自己的操作失误

这几条是**反复踩过的操作陷阱**，每次改代码前扫一遍。

## D1 改代码没生效

按这个顺序排查：

**① 插错了函数。** `split_frac` 和 `split_rich` 里都有 `\frac` 分支，
`_minner` 和 `omml_segs` 里都有 `\sqrt` 分支。
用 `replace(..., 1)` 会插到前一个函数里——**测试全绿但功能没生效**，
因为新代码在不会执行的分支里。踩过三次。

做法：加分支时**两个函数都加**，并写端到端用例验证（而非单测）。

**② 反斜杠层数错了。** Python 字符串里 `\b` 是退格符、`\v` 是垂直制表符、
`\n` 是换行。在 heredoc 里写 JS 注释用普通三引号，文件里会被写入 `\x08`
这类控制字符，后续 replace 全部匹配不上，且完全看不出原因。

做法：**LaTeX 相关字符串一律用 raw 前缀** `r"""..."""`。

**③ re 替换串被当转义序列。** 替换串 `'\\' + letter` 里的 `\\` 会被 re 解析。

做法：**用 lambda**：`re.sub(pat, lambda m: '\\' + letter, s)`。

**④ assert 失败导致文件没保存。** `replace → assert → write` 的写法，
断言一失败前面的改动全丢，表现得"跑完没报错但没生效"。

做法：断言前先写文件，或把断言挪到写入前并打印具体失败原因。

**⑤ 缓存。** 改了 Python 代码跑 `find . -name __pycache__ -delete` 再验。

## D2 过时的测试断言要删

上一轮的断言在新的实现下可能永久失败（如移除 `m:algn` 后还断言 `shp < algn`）。
留着会让人**习惯性忽略红色输出**——测试全绿才有意义。

做法：改实现时同步检查相关断言，失效的直接删或改。

## D3 端到端校验优于字符串检查

之前的验证方式是检查生成的字符串，**字符串看着对，解析可能失败、
符号可能没展开**——连续几轮都"验证通过"却漏掉真问题。

做法：关键渲染一律**实际生成 docx/HTML 后解析 XML 断言**（见 [A3](#a3-公式整段消失)）。

## D4 排查猜不如查规范

cases 的问题连报三轮，前两轮凭印象"修正"（猜 dPr 不够标准、
猜 XML 非法字符），越改越糟。第三轮查 OOXML schema，两个错误一次定位。

做法：涉及标准格式（OMML / MathML / CSS grid）的问题，
**先查规范再动手**。

---

# 跑回归

```bash
python3 tools/selftest.py          # 后端
node tools/test.mjs                # 前端
python3 tools/check_skill_docs.py  # 改了底层代码时
```

新发现的坑，修完**顺手加一条回归用例**锁死。
上面每一节的做法基本都有对应用例，改代码时它们会兜底。


## C. 数据校验

### 填空位两端都渲染不出来 → 先查核对工具的锚点

**现象**：`check_render.py` 结果里选择题全过、填空题全挂（如 6/18）。

**诊断**：渲染其实正常。锚点函数只去掉了全角 `＿＿＿＿＿`，
而题目用半角 `____` 录入，锚点带着 `____` 去匹配，
但 `____` 在两端都被渲染成了下划线元素、不在文本里。

**做法**：`anchor_of()` 里用 `re.sub(r'[＿_]{2,}', '', s)` 两种都去。

**验证**：先确认渲染没问题 —— 直接数 HTML 里的 `blank-u` 元素个数，
与「单空题数 + 双空题数×2」比对。数量对得上就是核对工具的问题。

### 已录题目被重复计入待录

**现象**：计划清单里出现「T011 还没录」这类假象，实际早已录完。

**诊断**：src 用了 PDF 的连续编号，与 ref_bank 的 key 对不上，
自动映射只命中一部分。

**做法**：新批次 src 直接写 ref_bank 的 key（见 50-topics.md）。

**验证**：`done_keys(bank)` 返回数应等于「已录题数 - 补录题数」，
且 `待录 + 重复 + 已录 == ref_bank 总数`。


## A. 公式渲染

### 命令名被当文本输出（页面显示 frac / sum / middle）

**现象**：页面上出现 `sumlimits`、`middle`、`subsetneq`、`overrightarrow` 这类命令名，
而不是对应符号。有时连带把后面的内容吃掉。

**诊断**：`latex_inline` 遇到不认识的命令会走"未知宏"分支，
把命令名当 `<mi>` 输出（`<mi>` 默认还是斜体）。

**做法**：把命令补进 `mathml.MACRO`（符号→字符）或
`latex_inline` 的跳过列表（`\left` `\limits` 这类只影响排版的）。

**验证**：不要靠肉眼看，全库扫一遍最可靠：

```python
import re, mathml as ML
OK = {'sin','cos','tan','log','ln','max','min','lim','exp'}
for q in bank:
    for fld in ('stem_text','solution','answer','analysis'):
        for m in re.finditer(r'<mi>([a-zA-Z]{3,})</mi>', ML.latex_inline(q.get(fld) or '')):
            if m.group(1) not in OK:
                print('未渲染:', q['id'], fld, m.group(1))
```

**一次补齐而不是每次补一个**：第 11 批发现 `\middle` 不支持，
顺手全库扫描又找出 `\sum` `\limits` `\odot` `\Leftrightarrow`
`\triangleq` `\iff` 等 6 个。
**每录一批就跑一次全库扫描**，能提前发现下一批会踩的坑。

当前 MACRO 98 条，覆盖关系符、集合、逻辑、几何、算子、定义符六大类。

### 只影响排版的命令要"跳过"而不是"翻译"

`\left` `\right` `\middle` `\limits` `\displaystyle`
`\!` `\,` `\;` `\quad` 这类命令**没有对应字符**，
正确处理是跳过（`i = k; continue`），让后面的内容继续解析。

若误加进 MACRO 会输出一个空 `<mo></mo>` 或奇怪字符。

注意 `\;` 在 `latex_expand` 里由 `\[,;:!]` 处理，
但 `\!` 等间距命令也要一并跳过，否则 `f\!\left(x\right)`
里的函数名判定会失败（f 后面不是左括号）。
