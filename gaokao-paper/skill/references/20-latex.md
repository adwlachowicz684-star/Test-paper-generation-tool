# LaTeX 书写规范（模式 A 必读）

## 定界符

**公式必须用 `$...$` 包裹**，这是 `split_rich()` 识别通用 LaTeX 的唯一方式。

```
对：定义在 $\mathbb{R}$ 上的奇函数 $f(x)$ 满足 $f(2-x)=f(x)$
错：定义在 \mathbb{R} 上的奇函数 f(x) 满足 f(2-x)=f(x)
```

不包 `$` 的 LaTeX 会**原样输出源码**，页面上直接显示 `\mathbb{R}`。

一个 `$...$` 是一个完整的 `<math>` 元素。

**公式与中文分段包裹**——中文留在 `$` 外，只把数学部分包起来：

```
对：$f(x)$ 满足 $f(2-x)=f(x)$
错：$f(x)满足$
```

中文进 MathML 会渲染异常（基线、字距都不对）。

## 支持的命令

### 结构命令（三个名字等价）

```
\frac{分子}{分母}   \dfrac{分子}{分母}   \tfrac{分子}{分母}
\sqrt{被开方数}     \sqrt[次数]{被开方数}
```

三者行内渲染完全等价。Word 端会归一成 `\frac`。

### 上下标

```
x_1        x^2        x_1^2
a_{n+1}    x^{2n}     \log_{\frac{1}{2}}2
```

花括号可省略（单字符时），系统会自动补。
但**多字符必须加花括号**：`x_12` 是 `x₁2` 不是 `x₁₂`。

### 数集（恒等映射，不做 Unicode 转换）

```
\mathbb{R} → R      \mathbb{N} → N      \mathbb{Z} → Z
\mathbb{Q} → Q      \mathbb{C} → C
```

**写 `\mathbb{R}`，系统会渲染成正体的 `R`。**

直接写 Unicode `ℝ` 也可以，但**不推荐**——不少中文字体缺黑板粗体字形，
会渲染成方块 □。试卷要打印给孩子做，出方块比不美观严重得多。

### 关系与运算

```
\le \leq ≤      \ge \geq ≥      \ne \neq ≠      \approx ≈      \equiv ≡
\in ∈    \notin ∉    \subset ⊂    \subseteq ⊆    \cup ∪    \cap ∩
\times ×   \cdot ⋅   \div ÷   \pm ±   \mp ∓   \ast ∗   \circ ∘
\to →   \rightarrow →   \leftarrow ←   \Rightarrow ⇒   \Leftarrow ⇐
\leftrightarrow ↔   \mapsto ↦
\perp ⊥   \parallel ∥   \angle ∠   \triangle △   \cong ≅
\infty ∞   \forall ∀   \exists ∃   \partial ∂   \nabla ∇
\emptyset ∅   \varnothing ∅
\therefore ∴   \because ∵   \ldots …   \cdots ⋯
```

### 希腊字母（38 个）

```
\alpha \beta \gamma \delta \epsilon \varepsilon \zeta \eta \theta \vartheta
\iota \kappa \lambda \mu \nu \xi \pi \varpi \rho \sigma \tau \upsilon
\phi \varphi \chi \psi \omega
\Gamma \Delta \Theta \Lambda \Xi \Pi \Sigma \Upsilon \Phi \Psi \Omega
```

### 函数名（自动正体，26 个）

```
sin cos tan cot sec csc  arcsin arccos arctan  sinh cosh tanh
ln lg log exp  max min lim  sup inf arg deg dim det gcd
```

### 其他

```
\text{中文或文本}    \mathrm{...}      → 输出正体文本
\mathbb{} \mathbf{}                   → 数集/粗体
\left( \right)                        → 括号尺寸（行内会被忽略，可写可不写）
\, \; \! \quad \qquad                 → 间距
```

**未知命令的输出行为**：去掉反斜杠保留名字（如 `\foo` → `foo`），
**不会静默吞掉**。所以写错了能在页面上看到，便于发现。

但 `\frac` `\sqrt` 是保留命令，不会被去掉反斜杠。

## 常见题目的写法

### 函数与区间（最高频，也是原卷最容易提取错的）

```
$f(x)$              $f(2-x)=f(x)$       $f(x+1)$
$(0,1)$             $[-1,11)$           $x\in[-1,0]$
$g(x)=f(x)+\dfrac{x+4}{1-2x}$
```

**凡是 `f` 后面跟的东西都要包进括号**——PDF 里这些括号是矢量绘制，
提取必丢，人工录入时最容易漏。

### 数列

```
$a_n$   $a_{n+1}$   $S_n$   $b_n=a_{2n}$   $\{a_n\}$
```

集合的花括号要转义：`\{a_n\}`，否则会被当成分组。

### 三角与向量

```
$\sin x$   $\cos^2 x$   $\vec{a}\cdot\vec{b}$   $|\vec{a}|$
$\overrightarrow{AB}$
```

向量命令已完整支持，三端都渲染为原生符号：

| 命令 | HTML | Word |
|---|---|---|
| `\overrightarrow{AB}` | `<mover>` + → | `<m:acc><m:chr m:val="→"/>` |
| `\overline{z}`（共轭） | `<mover>` + ¯ | `<m:bar>` |
| `\boldsymbol{m}` | `<mstyle mathvariant="bold">` | run 加 `<m:b/>` |

用到新命令前，先在「支持的命令清单」里确认，
并跑一遍 `latex_inline` / `omml_latex` 看输出。

### 几何

```
$AB\perp CD$    $\angle ABC$    $\triangle ABC$
三棱锥 $A-BCD$   平面 $ABD\perp$ 平面 $BCD$
```

## 校验写法是否正确

入库前用这两个函数自查：

```python
import sys; sys.path.insert(0, 'py')
import mathml as M

print(M.latex_inline(r'\frac{\sqrt{3}}{2}'))
# 应输出含 <mfrac> 与 <msqrt> 的 MathML，且无反斜杠残留

print(M.latex_expand(r'\dfrac{9}{2}'))
# 应为 \frac{9}{2}
```

**校验方法**：跑这两个函数，输出里**只应有 MathML 标签，无反斜杠残留**。
看到命令名（如 `dfrac`、`vec`）就说明该命令未被识别，
按 `30-pitfalls.md` 的 [A1](30-pitfalls.md#a1-公式显示成源码命令名) 补进 `MACRO` 表。

## 推荐写法对照

左列是正确写法，右列说明另一种写法的实际结果——知道它会被解析成什么，
就能判断要不要避开。

| 推荐写法 | 另一种写法的结果 |
|---|---|
| `$f(x)$` 包定界符 | 不包 `$` → 原样输出源码文本 |
| `\mathbb{R}` | 直接写 `ℝ` → 字体缺字形时显示方块 □ |
| `\frac{1}{2}` | `\frac1 2` → 解析成 `\frac{1}` 然后 `2` 独立 |
| `$f(x)$ 满足` | `$f(x)满足$` → 中文进 MathML，渲染异常 |
| `x_{12}` | `x_12` → 实际是 `x₁2`（下标只取单字符） |
| 用已支持的命令 | 未支持命令 → 输出命令名，页面上显示 `dfrac`、`vec` |

**命令是否支持，以 `MACRO` 表为准。**

MACRO: 105 条

不在表里的走「未知宏」分支输出命令名——这个行为是故意的，
便于在页面上直接发现。补充命令时同步更新上面的数字。

补充新命令时同步更新这个数字，`tools/check_skill_docs.py` 会校验它。

## 一个完整示例

```python
{
    'type': '选择',
    'stem_text': '已知定义域为 $\\mathbb{R}$ 的函数 $f(x)$ 的图像关于原点对称，'
                 '且 $f(3-x)+f(-x)=0$，若曲线 $y=f(x)$ 在 $(6,f(6))$ 处切线的斜率为 $4$，'
                 '则曲线 $y=f(x)$ 在 $(-2022,f(-2022))$ 处的切线方程为（　　）',
    'opts': [['A', '$y=-4x-8088$'],
             ['B', '$y=4x+8088$'],
             ['C', '$y=-\\frac{1}{4}x-\\frac{1011}{2}$'],
             ['D', '$y=\\frac{1}{4}x+\\frac{1011}{2}$']],
    'answer': 'B',
}
```

注意题干末尾的 `（　　）`——**选择题要保留一个作答位**（见 `21-review-rules.md`）。


## 支持的命令清单（完整）

| 类别 | 命令 |
|---|---|
| 分数 | `\frac` `\dfrac` `\tfrac` |
| 根式 | `\sqrt{x}` `\sqrt[n]{x}` |

根号后跟单字符时**写花括号更稳妥**（`\sqrt{6}` 而非 `\sqrt6`）：
HTML 端两者都行，Word 端靠 `latex_expand` 自动补，双保险更安心。
| 上下标 | `x^2` `x_1` `a_{n+1}` |
| **向量** | `\overrightarrow{AB}` `\overleftarrow{AB}` `\vec{a}` |
| **上划线** | `\overline{z}`（共轭复数） |
| **粗体** | `\boldsymbol{m}` `\pmb{m}` |
| 数集 | `\mathbb{R}` `\mathbb{N}` `\mathbf{a}` |
| 希腊字母 | `\alpha` `\pi` `\theta` `\Delta` … |
| 关系符 | `\le` `\ge` `\ne` `\approx` `\equiv` `\sim` |
| 集合 | `\in` `\notin` `\cup` `\cap` `\subset` `\subseteq` |
| 运算 | `\times` `\cdot` `\div` `\pm` `\to` `\rightarrow` |
| 角度 | `\circ`（90^\circ）`\angle` `\prime` |
| 其他 | `\log` `\sin` `\max`（函数名自动正体）、`\left` `\right` |

**`\underline` 未支持**：命令名里的下划线会和「补花括号」正则冲突
（`_u` 会被当成下标）。K12 数学基本用不到，需要时用 `\overline` 或直接文字描述。

**写新命令前先确认它在三端都实现了**：
- HTML：`mathml.py` 的 `_parse_expr`
- Word：`mathml.py` 的 `latex_expand` + `extract3.py` 的 `split_rich` + `make_paper.py` 的 `omml_segs`
- 前端：`src/app/render.js` 的 `parseLatex`

只改一处会导致同一道题在不同端显示不一致。


## cases 环境

```latex
$f(x)=\begin{cases}x^2, & x\leqslant 0\\ 4\sin x, & 0<x\leqslant \pi\end{cases}$
```

行间用 `\\` 分隔，列间用 `&` 分隔。

- HTML / 前端：`<mrow><mo stretchy="true">{</mo><mtable>`
- Word：`<m:d>` + `<m:begChr m:val="{"/>`

## 上标基底的四种形态

| 形态 | 例子 | 基底提取 |
|---|---|---|
| 函数名整词 | `\log_2 x` | `log` |
| 数字串 | `90^\circ` | `90` |
| 括号组 | `(x-1)^2` | `(x-1)` |
| 单字符 | `x^2` | `x` |

优先级从高到低。闭括号不是字母也不是数字，
必须有专门的配对规则，否则上标被静默丢弃。
