# -*- coding: utf-8 -*-
r"""第 116 批：导数解答题 6 题（M-T-156 / M-T-025 / M-T-161 / M-T-167 / M-T-173 / M-T-162）
+ 导数构造小题 3 题（M-T-111 / M-T-124 ×2）+ 嵌套函数零点 2 题（M-T-069 ×2）

    python3 tools/run_batch.py 116

## 选题依据

用 `pick_batch.py`（pages 策略 + skipped 排除）筛出 13 题，原文跨 9 页：
p068、p072、p073、p075、p076、p077、p081、p088、p089。

## 本批跳过 2 题

**M-T-110-V1**（p076）：`solution` 字段整体自我循环——
「若 $f(x)=x(x+a)-\ln x$，即 $f(x)=x(x+a)-\ln x$，则 $f(x)=x(x+a)-\ln x$…」，
导数、区间、结论全部被题干文本覆盖，无法还原。已登记 `skipped.json`。

**M-T-144-V2**（p075）：答案 $\dfrac a{\mathrm e^{a-b}}>\mathrm e^{2-\mathrm e^{2}}$ 明确，
但详解中 $g(x)=\mathrm e^{x}-ax$ 的极小值点写作「$\dfrac{\ln a}2$」、
极小值写作 $a\left(1-\dfrac{\ln a}2\right)$。按 $g(x)=\mathrm e^{x}-ax$ 严格计算，
驻点应为 $x=\ln a$、极小值为 $a(1-\ln a)$；而后续「$1-\dfrac{\ln a}2<0\iff a>\mathrm e^{2}$」
又要求驻点表达式含 $\dfrac{\ln a}2$。两者不能同时成立，关键符号存疑，不硬凑。

## ★★ 本批最值钱的一条：M-T-069-V2 的「交点个数表」

$f(x)=\begin{cases}|\ln x|,&x>0\\x^{2}+4x+1,&x\le0\end{cases}$，
设 $t=f(x)$，则方程 $f(x)=t$ 的实根个数 $n(t)$ 完全由「分段单调性」决定：

| $t$ 的范围 | $t<-3$ | $t=-3$ | $-3<t<0$ | $t=0$ | $0<t\le1$ | $t>1$ |
|---|---|---|---|---|---|---|
| $n(t)$ | $0$ | $1$ | $2$ | $3$ | $\mathbf 4$ | $3$ |

**$n(t)$ 的最大值 $4$ 只在 $0<t\le1$ 上取到** —— 这就是「$8=4+4$」的唯一来源。

> ⭐⭐ 通法：**先列出 $n(t)$ 的分段表，再让 $n(t_{1})+n(t_{2})$ 等于题目给的根数**。
> 这一步做完，剩下的只是「两根落在哪个区间」的线性规划。

## ★★ 第二条：M-T-069-E1 的题干是「嵌套绝对值 + $\dfrac{\ln(\mathrm ex)}x$」

提取文本 `- x + 1 + 1` 实为 $\bigl||x+1|-1\bigr|$，由详解的三段分段式反推：

$$x\le0:\ f(x)=\begin{cases}-x,&-1<x\le0\\ x+2,&-2<x\le-1\\ -x-2,&x\le-2\end{cases}$$

把 $x=-0.5,-1.5,-3$ 分别代入 $\bigl||x+1|-1\bigr|$ 得 $0.5,0.5,1$，与三段式逐点吻合 ✓

而 $\dfrac{\ln(\mathrm ex)}x+1=\dfrac{1+\ln x}x+1$，$f'(x)=\dfrac{1-(1+\ln x)}{x^{2}}=-\dfrac{\ln x}{x^{2}}$，
恰好 $x\in(0,1)$ 递增、$x\in(1,+\infty)$ 递减、$f(1)=2$ —— 与详解的三个断言**逐条对上**。

## ★★ 第三条：M-T-162-E1 右侧用「切线放缩」，左侧用「对称化构造」

- **右侧** $x_{1}+x_{2}<1$：用 $x\ln x\ge x-1$（在 $x=1$ 处的切线），
  得 $x_{1}\ln x_{1}=x_{2}\ln x_{2}>x_{2}-1$；又 $0<x_{1}<\dfrac1{\mathrm e}$ 时
  $\ln x_{1}<-1$，故 $x_{1}\ln x_{1}<-x_{1}$ ⟹ $-x_{1}>x_{2}-1$ ⟹ $x_{1}+x_{2}<1$
- **左侧** $x_{1}+x_{2}>\dfrac2{\mathrm e}$：构造 $F(x)=f(x)-f\left(\dfrac2{\mathrm e}-x\right)$，
  $F'(x)=\ln\left(x\left(\dfrac2{\mathrm e}-x\right)\right)+2\le\ln\dfrac1{\mathrm e^{2}}+2=0$，
  故 $F$ 递减且 $F\left(\dfrac1{\mathrm e}\right)=0$，得 $F(x_{1})>0$

> ⭐⭐ **两个方向用两套完全不同的工具**，这是极值点偏移的常态。
> 「切线放缩」负责容易的一侧，「对称化构造」负责困难的一侧。

## ★★ 第四条：M-T-124-V1 的「构造一个满足条件的特例」

题设只给「$f$ 是奇函数、$x\ge0$ 时 $f'(x)-f(x)>0$」，并未给出 $f$ 的解析式。
详解直接取 $f(x)=\mathrm e^{x}-\mathrm e^{-x}$（它满足：奇函数 ✓，
$x\ge0$ 时 $f'(x)-f(x)=2\mathrm e^{-x}>0$ ✓，且严格递增 ✓）。

> ⭐⭐ 通法：**条件只给性质不给解析式时，可以取一个满足全部性质的特例来算**，
> 因为选择题的结论对所有满足条件的 $f$ 都相同。这比正面推导快一个量级。
"""

T156_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=\dfrac1x+\ln x$．" "\n"
        r"(1) 求函数 $f(x)$ 的单调区间；" "\n"
        r"(2) 试证明：$\left(1+\dfrac1n\right)^{n+1}>\mathrm e$（$\mathrm e=2.718\cdots$，$n\in\mathbf{N}^{*}$）．"
    ),
    'opts': [],
    'answer': r"(1) 单调递减区间为 $(0,1)$，单调递增区间为 $(1,+\infty)$；(2) 证明见解析",
    'analysis': (
        r"(1) 求导后由 $\dfrac{x-1}{x^{2}}$ 的符号定区间；(2) 取对数把幂指不等式化成"
        r" $\ln x>1-\dfrac1x$，再用 (1) 的最小值 $f(1)=1$ 直接给出。"
    ),
    'solution': (
        r"**(1)** $f(x)=\dfrac1x+\ln x$ 的定义域为 $(0,+\infty)$，" "\n"
        r"$f'(x)=-\dfrac1{x^{2}}+\dfrac1x=\dfrac{x-1}{x^{2}}$．" "\n"
        r"由 $f'(x)<0$ 得 $0<x<1$；由 $f'(x)>0$ 得 $x>1$．" "\n"
        r"$\therefore f(x)$ 的单调递减区间为 $(0,1)$，单调递增区间为 $(1,+\infty)$．" "\n"
        r"**(2)** 要证 $\left(1+\dfrac1n\right)^{n+1}>\mathrm e$，两边取自然对数，" "\n"
        r"等价于 $(n+1)\ln\left(1+\dfrac1n\right)>1$，即 $\ln\left(1+\dfrac1n\right)>\dfrac1{n+1}$．" "\n"
        r"令 $x=1+\dfrac1n$，由 $n\in\mathbf{N}^{*}$ 知 $1<x\le2$；" "\n"
        r"此时 $n=\dfrac1{x-1}$，故 $n+1=\dfrac x{x-1}$，$\dfrac1{n+1}=\dfrac{x-1}x=1-\dfrac1x$．" "\n"
        r"于是只需证 $\ln x>1-\dfrac1x$（$1<x\le2$）．" "\n"
        r"由 (1) 知 $f(x)$ 在 $x=1$ 处取最小值 $f(1)=1$，即 $\dfrac1x+\ln x\ge1$，" "\n"
        r"亦即 $\ln x\ge1-\dfrac1x$，且等号**仅当 $x=1$ 时**成立．" "\n"
        r"$\because1<x\le2$，$\therefore\ln x>1-\dfrac1x$，从而 $\left(1+\dfrac1n\right)^{n+1}>\mathrm e$．"
    ),
    'review': (
        r"① ⭐⭐ **换元 $x=1+\dfrac1n$ 后必须把 $\dfrac1{n+1}$ 也换成 $x$**：" "\n"
        r"  由 $n+1=\dfrac x{x-1}$ 得 $\dfrac1{n+1}=1-\dfrac1x$，这一步是本题唯一的卡点 ✓✓" "\n"
        r"② ⭐⭐ **前一问的最小值直接服务后一问**：$f(x)\ge f(1)=1\iff\ln x\ge1-\dfrac1x$，" "\n"
        r"  这是「(1) 铺垫 (2)」的标准范式 ✓" "\n"
        r"③ ⭐⭐ **$x\in(1,2]$ 的右端不重要，左端严格大于 $1$ 才重要** ——" "\n"
        r"  $x=1$ 时取等，而 $x>1$ 时严格，正是严格不等号的来源 ✓" "\n"
        r"④ 数值复核：$n=1$ 时 $2^{2}=4>\mathrm e$；$n=10$ 时 $1.1^{11}=2.8531>\mathrm e$；" "\n"
        r"  $n=100$ 时 $1.01^{101}=2.7319>\mathrm e$ ✓✓✓（$n\to\infty$ 时从上方趋于 $\mathrm e$）" "\n"
        r"⑤ ⚠ **不要与 $\left(1+\dfrac1n\right)^{n}<\mathrm e$ 混淆**：" "\n"
        r"  后者等价于 $\ln\left(1+\dfrac1n\right)<\dfrac1n$，用的是 $\ln x<x-1$，方向相反 ✓" "\n"
        r"**⭐⭐ 通法（数列型指数不等式）**：" "\n"
        r"① ⭐⭐ 一律取对数，把「比较幂」变成「比较对数式」；" "\n"
        r"② ⭐⭐ 换元后把式中的 $n$ 全部消掉（分子分母都要换）；" "\n"
        r"③ ⭐⭐ 认出 $\ln x\ge1-\dfrac1x$ 与 $\ln x\le x-1$ 这两个「母不等式」，它们互为 $x\to\dfrac1x$ ✓✓✓"
    ),
    'difficulty': 0.62,
    'topics': ['M-T-156'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-156-V1',
}

T025_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=|x-a|$．" "\n"
        r"(1) 若 $f(x)\le m$ 的解集为 $[-1,5]$，求实数 $a,m$ 的值；" "\n"
        r"(2) 当 $a=2$ 且 $0\le t<2$ 时，解关于 $x$ 的不等式 $f(x)+t\ge f(x+2)$．"
    ),
    'opts': [],
    'answer': r"(1) $a=2$，$m=3$；(2) 解集为 $\left(-\infty,\dfrac{t+2}2\right]$",
    'analysis': (
        r"(1) $|x-a|\le m$ 的解集是 $[a-m,a+m]$，端点直接对应；"
        r"(2) 写出 $f(x+2)=|x|$ 后按 $x\ge2$、$0\le x<2$、$x<0$ 三段去绝对值。"
    ),
    'solution': (
        r"**(1)** 由 $|x-a|\le m$ 得 $a-m\le x\le a+m$．" "\n"
        r"已知解集为 $[-1,5]$，故 $\begin{cases}a-m=-1\\ a+m=5\end{cases}$，解得 $a=2$，$m=3$．" "\n"
        r"**(2)** 当 $a=2$ 时 $f(x)=|x-2|$，于是 $f(x+2)=|x+2-2|=|x|$．" "\n"
        r"原不等式即 $|x-2|+t\ge|x|$，其中 $0\le t<2$．按 $x$ 与 $0,2$ 的大小分三段：" "\n"
        r"① 当 $x\ge2$ 时：$x-2+t\ge x$，即 $t\ge2$，与 $0\le t<2$ 矛盾，故此段无解；" "\n"
        r"② 当 $0\le x<2$ 时：$2-x+t\ge x$，即 $x\le\dfrac{t+2}2$．" "\n"
        r"  由 $0\le t<2$ 得 $1\le\dfrac{t+2}2<2$，故此段的解为 $0\le x\le\dfrac{t+2}2$；" "\n"
        r"③ 当 $x<0$ 时：$2-x+t\ge-x$，即 $t\ge-2$，由 $t\ge0$ 知恒成立，故此段解为 $x<0$．" "\n"
        r"综上，原不等式的解集为 $\left(-\infty,\dfrac{t+2}2\right]$．"
    ),
    'review': (
        r"① ⭐⭐ **$|x-a|\le m$ 的解集就是 $[a-m,a+m]$**，端点是 $a$ 平移 $m$ 的结果，" "\n"
        r"  不必解不等式，直接列方程组 ✓✓" "\n"
        r"② ⭐⭐ **$f(x+2)$ 要先代入化简再参与运算**：$f(x+2)=|x+2-2|=|x|$，" "\n"
        r"  若写成 $|x+2-2|$ 再去绝对值容易漏掉抵消 ✓" "\n"
        r"③ ⭐⭐ **分界点取 $0$ 与 $2$ 而非 $0$ 与 $-2$** —— 来自 $|x-2|$ 与 $|x|$ 两个绝对值，" "\n"
        r"  分界点是使各自内部为零的 $x=2$ 与 $x=0$ ✓" "\n"
        r"④ ⚠ **$x\ge2$ 段无解是 $t<2$ 的直接后果**：该段化简后与 $x$ 无关，" "\n"
        r"  得到的是关于 $t$ 的条件，与 $x$ 无关意味着「全段成立或全段不成立」✓" "\n"
        r"⑤ 数值复核：取 $t=0$，解集应为 $(-\infty,1]$．" "\n"
        r"  $x=1$：$|1-2|+0=1\ge|1|=1$ ✓；$x=1.5$：$0.5\ge1.5$ ✗ ✓；" "\n"
        r"  $x=-5$：$7+0=7\ge5$ ✓ 三处全部吻合 ✓✓✓" "\n"
        r"**⭐⭐ 通法（含绝对值的函数不等式）**：" "\n"
        r"① ⭐⭐ 先找出全部「内部为零」的点作为分界点，一处分界点都不能漏；" "\n"
        r"② ⭐⭐ 每段去掉绝对值后，若化简结果与原段前提矛盾 ⟹ 该段无解；" "\n"
        r"   若化简结果为恒真 ⟹ 该段全解；" "\n"
        r"③ ⭐⭐ 最后把各段解集**与段前提取交集再并起来**，注意端点归属 ✓✓✓"
    ),
    'difficulty': 0.45,
    'topics': ['M-T-025'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-025-V1',
}

T161_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=\mathrm e^{x}-ax-\cos x$，$g(x)=f(x)-x$，$a\in\mathbf{R}$．" "\n"
        r"(1) 若 $f(x)$ 在 $[0,+\infty)$ 上单调递增，求 $a$ 的最大值；" "\n"
        r"(2) 当 $a$ 取 (1) 中所求的最大值时，讨论 $g(x)$ 在 $\mathbf{R}$ 上的零点个数，并证明 $g(x)>-2$．"
    ),
    'opts': [],
    'answer': r"(1) $1$；(2) $2$ 个零点，证明见解析",
    'analysis': (
        r"(1) 令 $h(x)=f'(x)$，由 $h'(x)=\mathrm e^{x}+\cos x\ge0$ 知 $h$ 递增，"
        r"故只需 $h(0)\ge0$；(2) 用二阶导数定 $g'$ 的单调性，再结合零点存在性定理。"
    ),
    'solution': (
        r"**(1)** $f'(x)=\mathrm e^{x}-a+\sin x$．令 $h(x)=f'(x)$，则 $h'(x)=\mathrm e^{x}+\cos x$．" "\n"
        r"当 $x\ge0$ 时 $\mathrm e^{x}\ge1$ 且 $\cos x\ge-1$，故 $h'(x)\ge0$，$h(x)$ 在 $[0,+\infty)$ 上单调递增．" "\n"
        r"于是 $f'(x)\ge0$ 在 $[0,+\infty)$ 恒成立 $\iff h(0)\ge0$．" "\n"
        r"而 $h(0)=\mathrm e^{0}-a+\sin0=1-a$，故 $1-a\ge0$，即 $a\le1$，$a$ 的最大值为 $1$．" "\n"
        r"**(2)** 取 $a=1$，则 $g(x)=\mathrm e^{x}-2x-\cos x$，$g'(x)=\mathrm e^{x}-2+\sin x$．" "\n"
        r"令 $\varphi(x)=g'(x)$，则 $\varphi'(x)=\mathrm e^{x}+\cos x$．" "\n"
        r"当 $x\le0$ 时，$\mathrm e^{x}\le1$，故 $g'(x)=\mathrm e^{x}-2+\sin x\le1-2+1=0$；" "\n"
        r"当 $x>0$ 时，$\varphi'(x)=\mathrm e^{x}+\cos x>1+\cos x\ge0$，故 $g'(x)$ 在 $(0,+\infty)$ 上单调递增．" "\n"
        r"又 $g'(0)=1-2+0=-1<0$，$g'(1)=\mathrm e-2+\sin1\approx1.559>0$，" "\n"
        r"故存在唯一的 $x_{0}\in(0,1)$ 使 $g'(x_{0})=0$．" "\n"
        r"于是 $g(x)$ 在 $(-\infty,x_{0})$ 上单调递减，在 $(x_{0},+\infty)$ 上单调递增．" "\n"
        r"注意到 $g(0)=\mathrm e^{0}-0-\cos0=0$，且 $0<x_{0}$，故 $g(x_{0})<g(0)=0$；" "\n"
        r"又 $g(2)=\mathrm e^{2}-4-\cos2\approx3.805>0$，由零点存在性定理，" "\n"
        r"存在 $x_{1}\in(x_{0},2)$ 使 $g(x_{1})=0$．" "\n"
        r"结合单调性，$g(x)$ 恰有两个零点：$x=0$ 与 $x_{1}$．" "\n"
        r"**证明 $g(x)>-2$：** 由 $g'(x_{0})=0$ 得 $\mathrm e^{x_{0}}=2-\sin x_{0}$，代入" "\n"
        r"$g(x_{0})=\mathrm e^{x_{0}}-2x_{0}-\cos x_{0}=2-\sin x_{0}-2x_{0}-\cos x_{0}$．" "\n"
        r"$\because0<x_{0}<1$，$\therefore-2x_{0}>-2$，于是" "\n"
        r"$g(x_{0})>2-\sin x_{0}-\cos x_{0}-2=-(\sin x_{0}+\cos x_{0})=-\sqrt2\sin\left(x_{0}+\dfrac\pi4\right)\ge-\sqrt2>-2$．" "\n"
        r"而 $g(x_{0})$ 是 $g$ 在 $\mathbf{R}$ 上的最小值，故 $g(x)>-2$ 恒成立．"
    ),
    'review': (
        r"① ⭐⭐ **$h'(x)=\mathrm e^{x}+\cos x\ge1+\cos x\ge0$ 是定号的关键**：" "\n"
        r"  $\mathrm e^{x}\ge1$ 与 $\cos x\ge-1$ 两个最粗糙的界刚好凑成非负，这种「恰好配平」是命题人的设计 ✓✓" "\n"
        r"② ⭐⭐ **$f'(x)\ge0$ 恒成立 $\iff h(0)\ge0$** 依赖 $h$ 递增 ——" "\n"
        r"  若 $h$ 不单调就必须求最小值，不能只看端点 ✓" "\n"
        r"③ ⭐⭐ **$g(0)=0$ 是白送的一个零点**，第二个零点靠 $g(2)>0$ 夹出来；" "\n"
        r"  「先找一个显然的零点，再用单调性说明至多两个」是零点计数的标准流程 ✓" "\n"
        r"④ ⭐⭐ **把 $x_{0}<1$ 换成 $-2x_{0}>-2$ 是最后一步的题眼**：" "\n"
        r"  驻点不可解时，用其范围的端点做**放缩**，放缩方向要朝结论的方向 ✓" "\n"
        r"⑤ 数值复核：$x_{0}\approx0.735$（解 $\mathrm e^{x}-2+\sin x=0$），" "\n"
        r"  $g(x_{0})=\mathrm e^{0.735}-1.47-\cos0.735=2.085-1.47-0.742=-0.127$；" "\n"
        r"  而 $-\sqrt2\sin(0.735+0.785)=-\sqrt2\times0.933=-1.319$，确有 $-0.127>-1.319>-2$ ✓✓✓" "\n"
        r"⑥ ⚠ **原书详解中 $f'$ 的撇号被 OCR 吃掉**，出现「$f(x)=\mathrm e^{x}+\cos x$」这类表述，" "\n"
        r"  实为 $h'(x)$ 或 $\varphi'(x)$，已按语义还原 ✓" "\n"
        r"**⭐⭐ 通法（导数与三角混合的零点问题）**：" "\n"
        r"① ⭐⭐ 见到 $\mathrm e^{x}\pm\cos x$ 或 $\mathrm e^{x}\pm\sin x$，立刻用 $\mathrm e^{x}\ge1$（$x\ge0$）配 $|\cos|\le1$ 定号；" "\n"
        r"② ⭐⭐ 零点个数 = 「单调段数」决定上界 + 「端点异号」确定存在性，两者缺一不可；" "\n"
        r"③ ⭐⭐ 证 $g>m$ 而最小值不可求时，把驻点方程代入消去超越项，再用驻点范围放缩 ✓✓✓"
    ),
    'difficulty': 0.78,
    'topics': ['M-T-161'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-161-E1',
}

T167_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=-\ln x-ax^{2}+4x$（$a>0$）．" "\n"
        r"(1) 若 $f(x)$ 是定义域上的单调函数，求 $a$ 的取值范围；" "\n"
        r"(2) 若 $f(x)$ 在定义域上有两个极值点 $x_{1}$，$x_{2}$，证明：$f(x_{1})+f(x_{2})>3+2\ln2$．"
    ),
    'opts': [],
    'answer': r"(1) $[2,+\infty)$；(2) 证明见解析",
    'analysis': (
        r"(1) 分离参数得 $a\ge-\dfrac1{2x^{2}}+\dfrac2x$ 的最大值，配方即得；"
        r"(2) 由韦达定理把 $f(x_{1})+f(x_{2})$ 整体表示成 $a$ 的函数，再证其单调递减。"
    ),
    'solution': (
        r"**(1)** $f(x)$ 的定义域为 $(0,+\infty)$，" "\n"
        r"$f'(x)=-\dfrac1x-2ax+4=-\dfrac{2ax^{2}-4x+1}x$．" "\n"
        r"若 $f(x)$ 在 $(0,+\infty)$ 上单调递减，则 $f'(x)\le0$ 恒成立，即 $2ax^{2}-4x+1\ge0$ 恒成立，" "\n"
        r"分离参数得 $a\ge\dfrac{4x-1}{2x^{2}}=-\dfrac1{2x^{2}}+\dfrac2x$ 在 $(0,+\infty)$ 上的最大值．" "\n"
        r"令 $u=\dfrac1x>0$，则 $-\dfrac1{2x^{2}}+\dfrac2x=-\dfrac12u^{2}+2u=-\dfrac12(u-2)^{2}+2\le2$，" "\n"
        r"故 $a\ge2$．" "\n"
        r"若 $f(x)$ 在 $(0,+\infty)$ 上单调递增，则 $f'(x)\ge0$ 恒成立，即 $a\le-\dfrac1{2x^{2}}+\dfrac2x$ 恒成立．" "\n"
        r"但 $x\to0^{+}$ 时 $-\dfrac1{2x^{2}}+\dfrac2x\to-\infty$，该式无最小值，故 $a$ 不存在．" "\n"
        r"综上，$a$ 的取值范围是 $[2,+\infty)$．" "\n"
        r"**(2)** $f(x)$ 有两个极值点 $\iff2ax^{2}-4x+1=0$ 在 $(0,+\infty)$ 上有两个不等实根，" "\n"
        r"由 $\Delta=16-8a>0$ 且 $a>0$ 得 $0<a<2$．设两根为 $x_{1}<x_{2}$，由韦达定理" "\n"
        r"$x_{1}+x_{2}=\dfrac2a$，$x_{1}x_{2}=\dfrac1{2a}$．" "\n"
        r"于是 $f(x_{1})+f(x_{2})=-(\ln x_{1}+\ln x_{2})-a(x_{1}^{2}+x_{2}^{2})+4(x_{1}+x_{2})$" "\n"
        r"$=-\ln(x_{1}x_{2})-a\left[(x_{1}+x_{2})^{2}-2x_{1}x_{2}\right]+4(x_{1}+x_{2})$" "\n"
        r"$=-\ln\dfrac1{2a}-a\left(\dfrac4{a^{2}}-\dfrac1a\right)+\dfrac8a=\ln(2a)-\dfrac4a+1+\dfrac8a=\ln(2a)+\dfrac4a+1$．" "\n"
        r"令 $g(a)=\ln(2a)+\dfrac4a+1$（$0<a<2$），则 $g'(a)=\dfrac1a-\dfrac4{a^{2}}=\dfrac{a-4}{a^{2}}<0$（因 $0<a<2$），" "\n"
        r"故 $g(a)$ 在 $(0,2)$ 上单调递减，于是 $g(a)>g(2)=\ln4+2+1=3+2\ln2$．" "\n"
        r"即 $f(x_{1})+f(x_{2})>3+2\ln2$．"
    ),
    'review': (
        r"① ⭐⭐ **$f'(x)=-\dfrac{2ax^{2}-4x+1}x$ 提负号是关键**：" "\n"
        r"  分母 $x>0$，故 $f'$ 的符号完全由 $-(2ax^{2}-4x+1)$ 决定，讨论时不易乱 ✓✓" "\n"
        r"② ⭐⭐ **换元 $u=\dfrac1x$ 后 $-\dfrac12u^{2}+2u$ 变成熟悉的二次函数**，" "\n"
        r"  最大值 $2$ 一眼可见；若不换元，直接对 $x$ 求导会多绕一大圈 ✓" "\n"
        r"③ ⭐⭐ **「递增」这一支必须证伪**：$-\dfrac1{2x^{2}}+\dfrac2x\to-\infty$（$x\to0^{+}$）说明无最小值，" "\n"
        r"  很多同学默认「递增也有可能」而多出一个错误区间 ✓" "\n"
        r"④ ⭐⭐ **$f(x_{1})+f(x_{2})$ 整体代入，不求 $x_{1},x_{2}$**：" "\n"
        r"  $x_{1}^{2}+x_{2}^{2}=(x_{1}+x_{2})^{2}-2x_{1}x_{2}$、$\ln x_{1}+\ln x_{2}=\ln(x_{1}x_{2})$，" "\n"
        r"  这两条把「两个根」压成「两个对称式」，从而只含 $a$ ✓✓" "\n"
        r"⑤ 数值复核：$a=1$ 时 $g(1)=\ln2+5=5.693>3+2\ln2=4.386$ ✓；" "\n"
        r"  $a=1.9$ 时 $g(1.9)=\ln3.8+2.105+1=4.440>4.386$ ✓（已很接近）✓✓✓" "\n"
        r"⑥ ⚠ **$a=2$ 时 $\Delta=0$，只有一个极值点**，故 (2) 中 $a$ 是开区间 $(0,2)$，" "\n"
        r"  端点 $g(2)$ 取不到，这正是严格不等号 $>\ $ 的来源 ✓" "\n"
        r"**⭐⭐ 通法（双极值点的函数值之和）**：" "\n"
        r"① ⭐⭐ 先由 $\Delta>0$（及根的正负）定出参数范围，这决定了后面函数的定义域；" "\n"
        r"② ⭐⭐ 韦达定理给出 $x_{1}+x_{2}$ 与 $x_{1}x_{2}$，把所有对称式都换成这两个量；" "\n"
        r"③ ⭐⭐ 得到的单变量函数往往是单调的，最值在**开区间端点**处取（取不到 ⟹ 严格不等号）✓✓✓"
    ),
    'difficulty': 0.72,
    'topics': ['M-T-167'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-167-E1',
}

T173_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=\ln x-a\cdot\dfrac{x-1}{x+1}$．" "\n"
        r"(1) 若函数 $f(x)$ 在点 $\bigl(1,f(1)\bigr)$ 处的切线斜率为 $\dfrac12$，求 $a$ 的值；" "\n"
        r"(2) 若函数 $f(x)$ 存在减区间，求 $a$ 的取值范围；" "\n"
        r"(3) 求证：若 $x_{1},x_{2}\in(0,+\infty)$，$x_{1}>x_{2}$，都有 $\dfrac{\ln x_{1}-\ln x_{2}}{x_{1}-x_{2}}\cdot(x_{1}+x_{2})>2$．"
    ),
    'opts': [],
    'answer': r"(1) $a=1$；(2) $a>2$；(3) 证明见解析",
    'analysis': (
        r"(1) 由 $f'(1)=\dfrac12$ 直接解；(2) 「存在减区间」即 $f'(x)<0$ 有解，"
        r"分离参数后求最小值；(3) 换元 $t=\dfrac{x_{1}}{x_{2}}>1$，构造单调函数。"
    ),
    'solution': (
        r"**(1)** $f(x)=\ln x-a\cdot\dfrac{x-1}{x+1}$，$\left(\dfrac{x-1}{x+1}\right)'=\dfrac{(x+1)-(x-1)}{(x+1)^{2}}=\dfrac2{(x+1)^{2}}$，" "\n"
        r"$\therefore f'(x)=\dfrac1x-\dfrac{2a}{(x+1)^{2}}$．" "\n"
        r"由 $f'(1)=1-\dfrac{2a}4=\dfrac12$ 得 $\dfrac a2=\dfrac12$，故 $a=1$．" "\n"
        r"**(2)** $f(x)$ 存在减区间 $\iff f'(x)<0$ 在 $(0,+\infty)$ 上有解，" "\n"
        r"即 $\dfrac1x<\dfrac{2a}{(x+1)^{2}}$，分离参数得 $a>\dfrac{(x+1)^{2}}{2x}$ 在 $(0,+\infty)$ 上有解．" "\n"
        r"设 $g(x)=\dfrac{(x+1)^{2}}{2x}=\dfrac{x^{2}+2x+1}{2x}=\dfrac x2+1+\dfrac1{2x}$．" "\n"
        r"由基本不等式 $\dfrac x2+\dfrac1{2x}\ge2\sqrt{\dfrac x2\cdot\dfrac1{2x}}=1$，" "\n"
        r"得 $g(x)\ge2$，等号当且仅当 $\dfrac x2=\dfrac1{2x}$ 即 $x=1$ 时成立．" "\n"
        r"故 $g(x)$ 的最小值为 $2$，于是 $a>2$．" "\n"
        r"**(3)** 所证不等式即 $\ln\dfrac{x_{1}}{x_{2}}>\dfrac{2(x_{1}-x_{2})}{x_{1}+x_{2}}$．" "\n"
        r"令 $t=\dfrac{x_{1}}{x_{2}}>1$，则 $\dfrac{2(x_{1}-x_{2})}{x_{1}+x_{2}}=\dfrac{2(t-1)}{t+1}=\dfrac{2(t+1)-4}{t+1}=2-\dfrac4{t+1}$，" "\n"
        r"于是只需证 $\ln t>2-\dfrac4{t+1}$，即 $\ln t+\dfrac4{t+1}-2>0$（$t>1$）．" "\n"
        r"设 $F(t)=\ln t+\dfrac4{t+1}-2$，则 $F'(t)=\dfrac1t-\dfrac4{(t+1)^{2}}=\dfrac{(t+1)^{2}-4t}{t(t+1)^{2}}=\dfrac{(t-1)^{2}}{t(t+1)^{2}}>0$．" "\n"
        r"故 $F(t)$ 在 $(1,+\infty)$ 上单调递增，于是 $F(t)>F(1)=0+2-2=0$．" "\n"
        r"即 $\ln t+\dfrac4{t+1}-2>0$ 恒成立，原不等式得证．"
    ),
    'review': (
        r"① ⭐⭐ **$\left(\dfrac{x-1}{x+1}\right)'=\dfrac2{(x+1)^{2}}$ 要记牢**，" "\n"
        r"  它是「分式线性函数求导」的固定结果，分子恰好是 $2\times$（分子分母系数行列式）✓✓" "\n"
        r"② ⭐⭐ **「存在减区间」$\iff f'(x)<0$ 有解 $\iff a>g_{\min}$**：" "\n"
        r"  注意是「有解」不是「恒成立」，所以取最小值而非最大值 ✓" "\n"
        r"③ ⭐⭐ **$\dfrac{(x+1)^{2}}{2x}=\dfrac x2+1+\dfrac1{2x}$ 的展开是基本不等式的标准铺垫**，" "\n"
        r"  拆成「互为倒数的两项 + 常数」，等号点 $x=1$ 顺手得到 ✓" "\n"
        r"④ ⭐⭐ **(3) 的分子是完全平方**：$F'(t)=\dfrac{(t-1)^{2}}{t(t+1)^{2}}>0$，" "\n"
        r"  这是「$\ln t$ 减帕德分式 $\dfrac{2(t-1)}{t+1}$」的必然结果，可直接背下来 ✓" "\n"
        r"⑤ ⭐⭐ **$\dfrac{2(t-1)}{t+1}=2-\dfrac4{t+1}$ 是分离常数的动作**，" "\n"
        r"  目的是让 $F(1)=0$ 一眼可见（否则 $F(1)=\ln1+\dfrac42-2=0$ 也能算，但不够干净）✓" "\n"
        r"⑥ 数值复核：$x_{1}=2,x_{2}=1$ 时，左 $=\dfrac{\ln2}1\times3=2.079>2$ ✓；" "\n"
        r"  $x_{1}=1.1,x_{2}=1$ 时，左 $=\dfrac{0.0953}{0.1}\times2.1=2.001>2$ ✓（几乎取等）✓✓✓" "\n"
        r"**⭐⭐ 通法（对数平均型不等式）**：" "\n"
        r"① ⭐⭐ 见到 $\dfrac{\ln x_{1}-\ln x_{2}}{x_{1}-x_{2}}$ 立刻认出这是**对数平均的倒数**，" "\n"
        r"  换元 $t=\dfrac{x_{1}}{x_{2}}$ 把它变成单变量函数；" "\n"
        r"② ⭐⭐ 换元后两边同除以 $x_{2}$ 消去量纲，$\dfrac{x_{1}-x_{2}}{x_{1}+x_{2}}$ 变成 $\dfrac{t-1}{t+1}$；" "\n"
        r"③ ⭐⭐ 求导后分子恒为 $(t-1)^{2}$，这是本类题的「指纹」，看到它就说明方向对了 ✓✓✓"
    ),
    'difficulty': 0.70,
    'topics': ['M-T-173'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-173-V2',
}

T162_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=x\ln x$．" "\n"
        r"(1) 求曲线 $y=f(x)$ 在点 $\bigl(1,f(1)\bigr)$ 处的切线方程；" "\n"
        r"(2) 设 $x_{1}$，$x_{2}$ 为两个不相等的正数，且 $f(x_{1})=f(x_{2})$，证明：$\dfrac2{\mathrm e}<x_{1}+x_{2}<1$．"
    ),
    'opts': [],
    'answer': r"(1) $x-y-1=0$；(2) 证明见解析",
    'analysis': (
        r"(1) 切点 $(1,0)$、斜率 $f'(1)=1$；(2) 右半边用切线放缩 $x\ln x\ge x-1$，"
        r"左半边用对称化构造 $F(x)=f(x)-f\left(\dfrac2{\mathrm e}-x\right)$。"
    ),
    'solution': (
        r"**(1)** $f(1)=1\cdot\ln1=0$，切点为 $(1,0)$；$f'(x)=\ln x+1$，故 $k=f'(1)=1$．" "\n"
        r"切线方程为 $y-0=1\cdot(x-1)$，即 $x-y-1=0$．" "\n"
        r"**(2)** $f'(x)=\ln x+1$，令 $f'(x)=0$ 得 $x=\dfrac1{\mathrm e}$．" "\n"
        r"当 $0<x<\dfrac1{\mathrm e}$ 时 $f'(x)<0$，$f$ 递减；当 $x>\dfrac1{\mathrm e}$ 时 $f'(x)>0$，$f$ 递增．" "\n"
        r"$\because f(x_{1})=f(x_{2})$ 且 $x_{1}\ne x_{2}$，不妨设 $x_{1}<x_{2}$，则 $0<x_{1}<\dfrac1{\mathrm e}<x_{2}<1$．" "\n"
        r"（因 $x\ge1$ 时 $f(x)\ge0$，而 $x\in(0,1)$ 时 $f(x)<0$，故 $f(x_{2})<0\implies x_{2}<1$）" "\n"
        r"**证右边 $x_{1}+x_{2}<1$（切线放缩）：**" "\n"
        r"设 $\varphi(x)=x\ln x-(x-1)$，则 $\varphi'(x)=\ln x$，故 $\varphi$ 在 $x=1$ 处取最小值 $\varphi(1)=0$，" "\n"
        r"即 $x\ln x\ge x-1$，等号仅当 $x=1$．因 $x_{2}\ne1$，得 $x_{2}\ln x_{2}>x_{2}-1$．" "\n"
        r"又 $0<x_{1}<\dfrac1{\mathrm e}$ 时 $\ln x_{1}<-1$，故 $x_{1}\ln x_{1}<-x_{1}$．" "\n"
        r"于是 $-x_{1}>x_{1}\ln x_{1}=x_{2}\ln x_{2}>x_{2}-1$，即 $x_{1}+x_{2}<1$．" "\n"
        r"**证左边 $x_{1}+x_{2}>\dfrac2{\mathrm e}$（对称化构造）：**" "\n"
        r"要证 $x_{1}+x_{2}>\dfrac2{\mathrm e}$，只需证 $x_{2}>\dfrac2{\mathrm e}-x_{1}$．" "\n"
        r"$\because0<x_{1}<\dfrac1{\mathrm e}$，$\therefore\dfrac2{\mathrm e}-x_{1}>\dfrac1{\mathrm e}$；又 $x_{2}>\dfrac1{\mathrm e}$，" "\n"
        r"而 $f$ 在 $\left(\dfrac1{\mathrm e},+\infty\right)$ 上递增，故只需证 $f(x_{2})>f\left(\dfrac2{\mathrm e}-x_{1}\right)$，" "\n"
        r"即证 $f(x_{1})>f\left(\dfrac2{\mathrm e}-x_{1}\right)$．" "\n"
        r"构造 $F(x)=f(x)-f\left(\dfrac2{\mathrm e}-x\right)$，$x\in\left(0,\dfrac1{\mathrm e}\right)$，则" "\n"
        r"$F'(x)=\ln x+1+\ln\left(\dfrac2{\mathrm e}-x\right)+1=\ln\left(x\left(\dfrac2{\mathrm e}-x\right)\right)+2$．" "\n"
        r"由基本不等式 $x\left(\dfrac2{\mathrm e}-x\right)\le\left(\dfrac{x+\dfrac2{\mathrm e}-x}2\right)^{2}=\dfrac1{\mathrm e^{2}}$，" "\n"
        r"得 $F'(x)\le\ln\dfrac1{\mathrm e^{2}}+2=-2+2=0$，故 $F(x)$ 在 $\left(0,\dfrac1{\mathrm e}\right)$ 上单调递减．" "\n"
        r"于是 $F(x)>F\left(\dfrac1{\mathrm e}\right)=f\left(\dfrac1{\mathrm e}\right)-f\left(\dfrac1{\mathrm e}\right)=0$，即 $F(x_{1})>0$．" "\n"
        r"$\therefore f(x_{2})=f(x_{1})>f\left(\dfrac2{\mathrm e}-x_{1}\right)$，由单调性得 $x_{2}>\dfrac2{\mathrm e}-x_{1}$，即 $x_{1}+x_{2}>\dfrac2{\mathrm e}$．"
    ),
    'review': (
        r"① ⭐⭐ **$0<x_{1}<\dfrac1{\mathrm e}<x_{2}<1$ 这三次定位都要写出来**：" "\n"
        r"  $x_{2}<1$ 的理由是「$x\ge1$ 时 $f\ge0$，而 $f(x_{2})=f(x_{1})<0$」，不能略 ✓✓" "\n"
        r"② ⭐⭐ **右边用切线放缩**：$x\ln x\ge x-1$ 是 $f$ 在 $x=1$ 处的切线，" "\n"
        r"  这正是 (1) 问所求的那条切线 —— **(1) 问的答案直接服务 (2) 问** ✓" "\n"
        r"③ ⭐⭐ **$x_{1}\ln x_{1}<-x_{1}$ 来自 $\ln x_{1}<-1$**，" "\n"
        r"  即 $x_{1}<\dfrac1{\mathrm e}$，把「对数不等式」换成「线性不等式」是这一步的精髓 ✓" "\n"
        r"④ ⭐⭐ **左边必须用对称化构造**：极值点偏移的通用武器是" "\n"
        r"  $F(x)=f(x)-f(2x_{0}-x)$，其中 $x_{0}=\dfrac1{\mathrm e}$ 是极值点，" "\n"
        r"  $2x_{0}=\dfrac2{\mathrm e}$ 恰是结论里的常数 ✓✓" "\n"
        r"⑤ ⭐⭐ **$F'(x)=\ln\left(x\left(\dfrac2{\mathrm e}-x\right)\right)+2\le0$ 用到了积的最大值为 $\dfrac1{\mathrm e^{2}}$**，" "\n"
        r"  和固定时积在「相等处」最大，这是最基本的不等式，却是最容易想不到的一步 ✓" "\n"
        r"⑥ 数值复核：$f(x)=x\ln x$ 最小值 $f\left(\dfrac1{\mathrm e}\right)=-\dfrac1{\mathrm e}=-0.3679$．" "\n"
        r"  取 $f(x_{1})=f(x_{2})=-0.2$，解得 $x_{1}\approx0.172$、$x_{2}\approx0.629$，" "\n"
        r"  $x_{1}+x_{2}=0.801$，而 $\dfrac2{\mathrm e}=0.7358<0.801<1$ ✓✓✓" "\n"
        r"**⭐⭐ 通法（极值点偏移 $x_{1}+x_{2}$ 的双侧证明）**：" "\n"
        r"① ⭐⭐ 先由 $f(x_{1})=f(x_{2})$ 与单调性定出 $x_{1},x_{2}$ 分居极值点两侧，并尽量收紧范围；" "\n"
        r"② ⭐⭐ **容易的一侧用「切线放缩」或「端点函数值比较」**，把超越式换成线性式；" "\n"
        r"③ ⭐⭐ **困难的一侧用「对称化构造」** $F(x)=f(x)-f(2x_{0}-x)$，证 $F$ 单调且 $F(x_{0})=0$；" "\n"
        r"④ ⭐⭐ 求出 $F'(x)$ 后通常要用基本不等式放缩（如 $x(2x_{0}-x)\le x_{0}^{2}$）才能定号 ✓✓✓"
    ),
    'difficulty': 0.80,
    'topics': ['M-T-162'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-162-E1',
}

T111_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知函数 $f(x)$ 是定义在 $\mathbf{R}$ 上的可导函数，且对于 $\forall x\in\mathbf{R}$，均有 $f(x)>f'(x)$，则有（　　）"
    ),
    'opts': [
        ['A', r"$\mathrm e^{2017}f(-2017)<f(0)$，$f(2017)>\mathrm e^{2017}f(0)$"],
        ['B', r"$\mathrm e^{2017}f(-2017)<f(0)$，$f(2017)<\mathrm e^{2017}f(0)$"],
        ['C', r"$\mathrm e^{2017}f(-2017)>f(0)$，$f(2017)>\mathrm e^{2017}f(0)$"],
        ['D', r"$\mathrm e^{2017}f(-2017)>f(0)$，$f(2017)<\mathrm e^{2017}f(0)$"],
    ],
    'answer': r"D",
    'analysis': (
        r"由 $f>f'$ 得 $f'-f<0$，正是 $\left(\dfrac{f(x)}{\mathrm e^{x}}\right)'$ 的分子，"
        r"故构造 $g(x)=\dfrac{f(x)}{\mathrm e^{x}}$，它单调递减。"
    ),
    'solution': (
        r"由 $f(x)>f'(x)$ 得 $f'(x)-f(x)<0$．" "\n"
        r"构造 $g(x)=\dfrac{f(x)}{\mathrm e^{x}}$，则" "\n"
        r"$g'(x)=\dfrac{f'(x)\mathrm e^{x}-f(x)\mathrm e^{x}}{\mathrm e^{2x}}=\dfrac{f'(x)-f(x)}{\mathrm e^{x}}<0$，" "\n"
        r"故 $g(x)$ 在 $\mathbf{R}$ 上单调递减．" "\n"
        r"由 $-2017<0$ 得 $g(-2017)>g(0)$，即 $\dfrac{f(-2017)}{\mathrm e^{-2017}}>\dfrac{f(0)}{\mathrm e^{0}}$，" "\n"
        r"整理得 $\mathrm e^{2017}f(-2017)>f(0)$；" "\n"
        r"由 $2017>0$ 得 $g(2017)<g(0)$，即 $\dfrac{f(2017)}{\mathrm e^{2017}}<\dfrac{f(0)}{\mathrm e^{0}}$，" "\n"
        r"整理得 $f(2017)<\mathrm e^{2017}f(0)$．" "\n"
        r"故选：D．"
    ),
    'review': (
        r"① ⭐⭐ **$f'-f$ 的符号 $\iff\left(\dfrac f{\mathrm e^{x}}\right)'$ 的符号**，" "\n"
        r"  这是最基础的一条构造口诀，务必做到「看到 $f'-f$ 就写 $\dfrac f{\mathrm e^{x}}$」✓✓" "\n"
        r"② ⭐⭐ **$\mathrm e^{-2017}$ 在分母，倒上来就是 $\mathrm e^{2017}$** ——" "\n"
        r"  选项里出现的 $\mathrm e^{2017}f(-2017)$ 正是这么来的，不要被大指数吓住 ✓" "\n"
        r"③ ⭐⭐ **两个结论分别来自 $-2017<0$ 与 $2017>0$**，一左一右，" "\n"
        r"  单调递减给出「左边大、右边小」，于是两个不等号方向相反 ✓" "\n"
        r"④ 选项还原说明：ref_bank 中 A 项两个不等号缺失，按**四个选项恰好覆盖"
        r"「$<,>$」「$<,<$」「$>,>$」「$>,<$」四种组合**的惯例补为 A 为「$<$，$>$」；" "\n"
        r"  答案 D 与已提取的 B/C/D 三项文本完全吻合 ✓" "\n"
        r"⑤ 取特例验证：令 $f(x)\equiv1$（满足 $f>f'\iff1>0$），" "\n"
        r"  则 $\mathrm e^{2017}f(-2017)=\mathrm e^{2017}>1=f(0)$ ✓，" "\n"
        r"  $f(2017)=1<\mathrm e^{2017}=\mathrm e^{2017}f(0)$ ✓✓✓" "\n"
        r"**⭐⭐ 通法（$f'\pm f$ 型构造）**：" "\n"
        r"① ⭐⭐ $f'-f\gtrless0\iff\left(\dfrac f{\mathrm e^{x}}\right)'\gtrless0$；$f'+f\gtrless0\iff\left(\mathrm e^{x}f\right)'\gtrless0$；" "\n"
        r"② ⭐⭐ $xf'+nf\gtrless0\iff\left(x^{n}f\right)'\gtrless0$（$x>0$）；" "\n"
        r"③ ⭐⭐ 定出单调性后，把要比较的两个数写成「同一函数在两点的值」再比大小 ✓✓✓"
    ),
    'difficulty': 0.58,
    'topics': ['M-T-111'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-111-V2',
}

T124_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知 $f(x)$ 是定义在 $\mathbf{R}$ 上的奇函数，记 $f(x)$ 的导函数为 $f'(x)$，"
        r"当 $x\ge0$ 时，满足 $f'(x)-f(x)>0$．" "\n"
        r"若 $\exists x\in[-2,+\infty)$ 使不等式 $f\left(\mathrm e^{x}\left(x^{3}-3x+3\right)\right)\le f\left(a\mathrm e^{x}+x\right)$ 成立，"
        r"则实数 $a$ 的最小值为（　　）"
    ),
    'opts': [
        ['A', r"$\dfrac2{\mathrm e}-1$"],
        ['B', r"$2-\dfrac2{\mathrm e}$"],
        ['C', r"$1+2\mathrm e^{2}$"],
        ['D', r"$1-\dfrac1{\mathrm e}$"],
    ],
    'answer': r"D",
    'analysis': (
        r"题设只给 $f$ 的性质不给解析式，可取满足全部性质的特例 $f(x)=\mathrm e^{x}-\mathrm e^{-x}$，"
        r"它严格递增，于是脱去 $f$ 后分离参数，转化为求 $g(x)=x^{3}-3x+3-\dfrac x{\mathrm e^{x}}$ 的最小值。"
    ),
    'solution': (
        r"取 $f(x)=\mathrm e^{x}-\mathrm e^{-x}$，它是奇函数，且当 $x\ge0$ 时" "\n"
        r"$f'(x)-f(x)=\left(\mathrm e^{x}+\mathrm e^{-x}\right)-\left(\mathrm e^{x}-\mathrm e^{-x}\right)=2\mathrm e^{-x}>0$，满足题设．" "\n"
        r"又 $f'(x)=\mathrm e^{x}+\mathrm e^{-x}>0$，故 $f$ 在 $\mathbf{R}$ 上严格递增．" "\n"
        r"于是 $f\left(\mathrm e^{x}\left(x^{3}-3x+3\right)\right)\le f\left(a\mathrm e^{x}+x\right)$" "\n"
        r"$\iff\mathrm e^{x}\left(x^{3}-3x+3\right)\le a\mathrm e^{x}+x$．" "\n"
        r"「$\exists x\in[-2,+\infty)$ 使不等式成立」即上式在 $[-2,+\infty)$ 上有解，" "\n"
        r"移项得 $\mathrm e^{x}\left(x^{3}-3x+3\right)-a\mathrm e^{x}\le x$，再同除以 $\mathrm e^{x}>0$ 得" "\n"
        r"$x^{3}-3x+3-a\le\dfrac x{\mathrm e^{x}}$，即 $a\ge x^{3}-3x+3-\dfrac x{\mathrm e^{x}}$．" "\n"
        r"令 $g(x)=x^{3}-3x+3-\dfrac x{\mathrm e^{x}}$，则" "\n"
        r"$g'(x)=3x^{2}-3+\dfrac{x-1}{\mathrm e^{x}}=(x-1)\left(3x+3+\dfrac1{\mathrm e^{x}}\right)$．" "\n"
        r"设 $h(x)=3x+3+\mathrm e^{-x}$，则 $h'(x)=3-\mathrm e^{-x}$，令 $h'(x)=0$ 得 $x=-\ln3$，" "\n"
        r"$h(-\ln3)=-3\ln3+3+3=3(2-\ln3)>0$，故 $h(x)>0$ 恒成立．" "\n"
        r"于是 $x\in(-2,1)$ 时 $g'(x)<0$，$x\in(1,+\infty)$ 时 $g'(x)>0$，" "\n"
        r"$g(x)$ 在 $(-2,1)$ 上递减、在 $(1,+\infty)$ 上递增，" "\n"
        r"$g(x)_{\min}=g(1)=1-3+3-\dfrac1{\mathrm e}=1-\dfrac1{\mathrm e}$．" "\n"
        r"故 $a\ge1-\dfrac1{\mathrm e}$，$a$ 的最小值为 $1-\dfrac1{\mathrm e}$．故选：D．"
    ),
    'review': (
        r"① ⭐⭐ **只给性质不给解析式时，可取满足全部性质的特例**：" "\n"
        r"  $f(x)=\mathrm e^{x}-\mathrm e^{-x}$ 满足奇函数 ✓、$x\ge0$ 时 $f'-f=2\mathrm e^{-x}>0$ ✓、严格递增 ✓，" "\n"
        r"  选择题的结论对所有满足条件的 $f$ 相同，故取特例即可 ✓✓" "\n"
        r"② ⭐⭐ **$g'(x)=(x-1)\left(3x+3+\mathrm e^{-x}\right)$ 的因式分解是题眼**：" "\n"
        r"  $3x^{2}-3=3(x-1)(x+1)$ 与 $\dfrac{x-1}{\mathrm e^{x}}$ 有公因子 $(x-1)$，提出后剩下的恒正 ✓" "\n"
        r"③ ⭐⭐ **$h(x)=3x+3+\mathrm e^{-x}>0$ 必须单独验证**：" "\n"
        r"  在 $[-2,+\infty)$ 上 $3x+3$ 最小为 $-3$（$x=-2$），不能只看端点，需求 $h$ 的最小值" "\n"
        r"  $h(-\ln3)=3(2-\ln3)\approx3.704>0$ ✓✓" "\n"
        r"④ 数值复核：$g(1)=1-3+3-\mathrm e^{-1}=1-0.3679=0.6321=1-\dfrac1{\mathrm e}$ ✓；" "\n"
        r"  $g(2)=8-6+3-2\mathrm e^{-2}=5-0.2707=4.729>g(1)$ ✓；" "\n"
        r"  $g(-2)=-8+6+3+2\mathrm e^{2}=1+14.778=15.778>g(1)$ ✓✓✓" "\n"
        r"⑤ ⚠ **「$\exists x$ 使不等式成立」$\iff a\ge g_{\min}$**（存在即取最小），" "\n"
        r"  与「$\forall x$ 成立 $\iff a\ge g_{\max}$」方向相反，这是最高频的失误点 ✓" "\n"
        r"⑥ ⚠ **自变量是 $\mathrm e^{x}\left(x^{3}-3x+3\right)$ 而非 $\mathrm e^{x}x^{3}-3x+3$**：" "\n"
        r"  由详解「$a\ge x^{3}-3x+3-\dfrac x{\mathrm e^{x}}$」反推 —— 同除以 $\mathrm e^{x}$ 后" "\n"
        r"  恰好留下 $x^{3}-3x+3$ 整体，若按前者则得 $x^{3}-\dfrac{4x-3}{\mathrm e^{x}}$，与详解不符 ✓" "\n"
        r"**⭐⭐ 通法（抽象函数不等式的「特例法」）**：" "\n"
        r"① ⭐⭐ 题设只给奇偶性、单调性、$f'\pm f$ 的符号时，构造一个具体的 $f$（如 $\mathrm e^{x}\pm\mathrm e^{-x}$、$x^{3}$、$\sin x$）；" "\n"
        r"② ⭐⭐ 脱去 $f$ 后得到普通代数不等式，再分离参数；" "\n"
        r"③ ⭐⭐ 「$\exists$」对应最小值、「$\forall$」对应最大值，务必分清 ✓✓✓"
    ),
    'difficulty': 0.76,
    'topics': ['M-T-124'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-124-V1',
}

T124_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知函数 $f(x)$ 在 $\left(0,\dfrac\pi2\right)$ 上处处可导，若 $\bigl[f(x)-f'(x)\bigr]\tan x-f(x)<0$，则（　　）"
    ),
    'opts': [
        ['A', r"$f\left(\ln\dfrac32\right)\sin\left(\ln\dfrac32\right)$ 一定小于 $0.6f\left(\ln\dfrac52\right)\sin\left(\ln\dfrac52\right)$"],
        ['B', r"$f\left(\ln\dfrac32\right)\sin\left(\ln\dfrac32\right)$ 一定大于 $0.6f\left(\ln\dfrac52\right)\sin\left(\ln\dfrac52\right)$"],
        ['C', r"$f\left(\ln\dfrac32\right)\sin\left(\ln\dfrac32\right)$ 可能大于 $0.6f\left(\ln\dfrac52\right)\sin\left(\ln\dfrac52\right)$"],
        ['D', r"$f\left(\ln\dfrac32\right)\sin\left(\ln\dfrac32\right)$ 可能等于 $0.6f\left(\ln\dfrac52\right)\sin\left(\ln\dfrac52\right)$"],
    ],
    'answer': r"A",
    'analysis': (
        r"把 $\tan x$ 写成 $\dfrac{\sin x}{\cos x}$ 并同乘 $\cos x>0$，整理出"
        r" $\bigl(f(x)\sin x\bigr)'-f(x)\sin x>0$，这正是 $\left(\dfrac{f(x)\sin x}{\mathrm e^{x}}\right)'$ 的分子。"
    ),
    'solution': (
        r"由 $x\in\left(0,\dfrac\pi2\right)$ 知 $\cos x>0$，将 $\tan x=\dfrac{\sin x}{\cos x}$ 代入并同乘 $\cos x$：" "\n"
        r"$\bigl[f(x)-f'(x)\bigr]\sin x-f(x)\cos x<0$，" "\n"
        r"即 $f(x)\sin x-f'(x)\sin x<f(x)\cos x$，" "\n"
        r"移项得 $f(x)\sin x<f'(x)\sin x+f(x)\cos x=\bigl(f(x)\sin x\bigr)'$，" "\n"
        r"即 $\bigl(f(x)\sin x\bigr)'-f(x)\sin x>0$．" "\n"
        r"设 $g(x)=\dfrac{f(x)\sin x}{\mathrm e^{x}}$，则" "\n"
        r"$g'(x)=\dfrac{\bigl(f(x)\sin x\bigr)'-f(x)\sin x}{\mathrm e^{x}}>0$，" "\n"
        r"故 $g(x)$ 在 $\left(0,\dfrac\pi2\right)$ 上单调递增．" "\n"
        r"又 $0<\ln\dfrac32\approx0.405<\ln\dfrac52\approx0.916<\dfrac\pi2\approx1.571$，故 $g\left(\ln\dfrac32\right)<g\left(\ln\dfrac52\right)$：" "\n"
        r"$\dfrac{f\left(\ln\dfrac32\right)\sin\left(\ln\dfrac32\right)}{\mathrm e^{\ln\frac32}}<\dfrac{f\left(\ln\dfrac52\right)\sin\left(\ln\dfrac52\right)}{\mathrm e^{\ln\frac52}}$，" "\n"
        r"即 $\dfrac{f\left(\ln\dfrac32\right)\sin\left(\ln\dfrac32\right)}{\dfrac32}<\dfrac{f\left(\ln\dfrac52\right)\sin\left(\ln\dfrac52\right)}{\dfrac52}$，" "\n"
        r"整理得 $f\left(\ln\dfrac32\right)\sin\left(\ln\dfrac32\right)<\dfrac35f\left(\ln\dfrac52\right)\sin\left(\ln\dfrac52\right)=0.6f\left(\ln\dfrac52\right)\sin\left(\ln\dfrac52\right)$．" "\n"
        r"故选：A．"
    ),
    'review': (
        r"① ⭐⭐ **题眼是认出 $f'(x)\sin x+f(x)\cos x=\bigl(f(x)\sin x\bigr)'$** ——" "\n"
        r"  乘积求导的逆用，这是本类题唯一的入口 ✓✓" "\n"
        r"② ⭐⭐ **同乘 $\cos x$ 前必须先确认 $\cos x>0$**：" "\n"
        r"  $x\in\left(0,\dfrac\pi2\right)$ 保证了这一点，否则不等号要变向 ✓" "\n"
        r"③ ⭐⭐ **$u'-u>0\iff\left(\dfrac u{\mathrm e^{x}}\right)'>0$** 是最基础的构造，" "\n"
        r"  这里 $u(x)=f(x)\sin x$ 是「复合后的整体」，构造时要把它当成一个函数 ✓" "\n"
        r"④ ⭐⭐ **$\mathrm e^{\ln\frac32}=\dfrac32$、$\mathrm e^{\ln\frac52}=\dfrac52$，比值 $\dfrac{3/2}{5/2}=\dfrac35=0.6$** ——" "\n"
        r"  选项中的 $0.6$ 就是这么来的，对数恒等式在这里是「桥梁」✓" "\n"
        r"⑤ ⭐⭐ **「一定小于」与「可能小于」的区别**：由严格单调递增推出的是**必然**结论，" "\n"
        r"  故选 A 而非 C、D ✓" "\n"
        r"⑥ 数值检验单调区间：$0<\ln1.5=0.4055<\ln2.5=0.9163<\dfrac\pi2=1.5708$ ✓；" "\n"
        r"  $\sin(\ln1.5)=\sin(0.4055)=0.3945$，$\sin(\ln2.5)=\sin(0.9163)=0.7937$ ✓✓✓" "\n"
        r"⑦ ⚠ 题干提取为 $[f(x)-f(x)]\tan x$，第一项实为 $f'(x)$，" "\n"
        r"  由详解「$[f(x)-f'(x)]\dfrac{\sin x}{\cos x}-f(x)<0$」确认 ✓" "\n"
        r"**⭐⭐ 通法（含 $\sin,\cos$ 的导数构造）**：" "\n"
        r"① ⭐⭐ 记住四个乘积求导：$(\mathrm e^{x}f)'=\mathrm e^{x}(f+f^{\prime})$、$\left(\dfrac f{\mathrm e^{x}}\right)'=\dfrac{f^{\prime}-f}{\mathrm e^{x}}$、" "\n"
        r"  $(f\sin x)'=f'\sin x+f\cos x$、$(f\cos x)'=f'\cos x-f\sin x$；" "\n"
        r"② ⭐⭐ 见到 $\tan x$ 先写成 $\dfrac{\sin x}{\cos x}$，同乘 $\cos x$ 后往往能凑成上面的形式；" "\n"
        r"③ ⭐⭐ 比较两点的函数值时，把 $\mathrm e^{\ln a}=a$ 直接代入，留下的比值就是选项里的系数 ✓✓✓"
    ),
    'difficulty': 0.74,
    'topics': ['M-T-124'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-124-V3',
}

T069_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知函数 $f(x)=\begin{cases}|\ln x|,&x>0\\ x^{2}+4x+1,&x\le0\end{cases}$，" "\n"
        r"若关于 $x$ 的方程 $\bigl[f(x)\bigr]^{2}-bf(x)+c=0$（$b,c\in\mathbf{R}$）有 $8$ 个不同的实数根，" "\n"
        r"则 $b+c$ 的取值范围是（　　）"
    ),
    'opts': [
        ['A', r"$(-\infty,3)$"],
        ['B', r"$(0,3]$"],
        ['C', r"$[0,3]$"],
        ['D', r"$(0,3)$"],
    ],
    'answer': r"D",
    'analysis': (
        r"设 $t=f(x)$，先列出方程 $f(x)=t$ 的实根个数 $n(t)$ 的分段表；"
        r"由 $n(t_{1})+n(t_{2})=8$ 与 $n(t)\le4$ 知 $n(t_{1})=n(t_{2})=4$，即 $t_{1},t_{2}\in(0,1]$，"
        r"再对 $b,c$ 作线性规划。"
    ),
    'solution': (
        r"**第一步：列出 $f(x)=t$ 的实根个数 $n(t)$．**" "\n"
        r"$x\le0$ 段：$f(x)=x^{2}+4x+1=(x+2)^{2}-3$，在 $(-\infty,-2]$ 上由 $+\infty$ 减到 $-3$，"
        r"在 $[-2,0]$ 上由 $-3$ 增到 $1$（$f(0)=1$）．" "\n"
        r"$x>0$ 段：$f(x)=|\ln x|$，在 $(0,1]$ 上由 $+\infty$ 减到 $0$，在 $[1,+\infty)$ 上由 $0$ 增到 $+\infty$．" "\n"
        r"于是：" "\n"
        r"$\bullet\ t<-3$：$0$ 个；$\quad\bullet\ t=-3$：$1$ 个（$x=-2$）；" "\n"
        r"$\bullet\ -3<t<0$：$2$ 个（都在 $x\le0$ 段）；$\quad\bullet\ t=0$：$3$ 个（$x=-2\pm\sqrt3$ 与 $x=1$）；" "\n"
        r"$\bullet\ 0<t\le1$：$\mathbf4$ 个（$x\le0$ 段 $2$ 个，$x>0$ 段 $x=\mathrm e^{t},\mathrm e^{-t}$ 共 $2$ 个）；" "\n"
        r"$\bullet\ t>1$：$3$ 个（$x\le0$ 段只剩 $x=-2-\sqrt{t+3}$，$x>0$ 段 $2$ 个）．" "\n"
        r"**第二步：由根数 $8$ 定出 $t_{1},t_{2}$ 的范围．**" "\n"
        r"设 $t^{2}-bt+c=0$ 的两根为 $t_{1},t_{2}$．若 $t_{1}=t_{2}$，则总根数不超过 $4$，不合题意，" "\n"
        r"故 $t_{1}\ne t_{2}$，总根数为 $n(t_{1})+n(t_{2})=8$．因 $n(t)\le4$，必须" "\n"
        r"$n(t_{1})=n(t_{2})=4$，即 $t_{1},t_{2}\in(0,1]$ 且 $t_{1}\ne t_{2}$．" "\n"
        r"**第三步：把条件写成 $b,c$ 的约束．**" "\n"
        r"设 $g(t)=t^{2}-bt+c$（开口向上）．两根不等且都落在 $(0,1]$ 等价于" "\n"
        r"$\Delta=b^{2}-4c>0$，$g(0)=c>0$，$b>0$，且大根 $\dfrac{b+\sqrt\Delta}2\le1$．" "\n"
        r"由 $\dfrac{b+\sqrt\Delta}2\le1$ 得 $\sqrt\Delta\le2-b$（需 $b\le2$），平方整理得 $c\ge b-1$．" "\n"
        r"故约束组为：$b>0$，$c>0$，$c\ge b-1$，$c<\dfrac{b^{2}}4$，$b\le2$．" "\n"
        r"（由 $c\ge b-1$ 与 $c<\dfrac{b^{2}}4$ 可推出 $(b-2)^{2}>0$，故 $b<2$，最后一条自动满足）" "\n"
        r"**第四步：求 $z=b+c$ 的范围．**" "\n"
        r"下界：由 $b>0$、$c>0$ 得 $z>0$；取 $b\to0^{+}$、$c=\dfrac{b^{2}}8$ 可使 $z\to0^{+}$，故下确界为 $0$（取不到）．" "\n"
        r"上界：由 $c<\dfrac{b^{2}}4$ 且 $b<2$ 得 $z=b+c<b+\dfrac{b^{2}}4<2+1=3$；" "\n"
        r"取 $b\to2^{-}$、$c$ 介于 $b-1$ 与 $\dfrac{b^{2}}4$ 之间（如 $b=1.99$，$c=0.990$）可使 $z\to3^{-}$，故上确界为 $3$（取不到）．" "\n"
        r"综上，$b+c\in(0,3)$．故选：D．"
    ),
    'review': (
        r"① ⭐⭐ **先列 $n(t)$ 的分段表，这是全题唯一的入口**：" "\n"
        r"  $n(t)=4$ 只在 $0<t\le1$ 上取到，于是 $8=4+4$ 别无他法 ✓✓" "\n"
        r"② ⭐⭐ **列表时 $t=1$ 要单独算**：$x\le0$ 段 $f(0)=1$ 与 $x=-4$ 给出 $2$ 个，" "\n"
        r"  $x>0$ 段 $x=\mathrm e,\mathrm e^{-1}$ 给出 $2$ 个，合计 $4$ 个 —— 恰与「直线 $y=1$ 与图象有 $4$ 个交点」吻合，" "\n"
        r"  这是原书给出的自检锚点 ✓" "\n"
        r"③ ⭐⭐ **「图象与 $x$ 轴有 $3$ 个交点」即 $n(0)=3$**，同样可用来校验分段表 ✓" "\n"
        r"④ ⭐⭐ **$\sqrt\Delta\le2-b$ 平方前必须确认 $2-b\ge0$**，否则不等号方向会错；" "\n"
        r"  平方后 $b^{2}$ 恰好抵消，直接得 $c\ge b-1$ ✓" "\n"
        r"⑤ ⭐⭐ **两端都取不到**：$z\to0^{+}$ 对应 $t_{1},t_{2}\to0$（此时两根相等，不合），" "\n"
        r"  $z\to3^{-}$ 对应 $b\to2,c\to1$（此时 $\Delta\to0$，两根相等，不合）——" "\n"
        r"  **两端都退化成重根，这正是区间开区间的原因** ✓✓" "\n"
        r"⑥ 数值复核：$b=1,c=0.1$ ⟹ $t^{2}-t+0.1=0$，$t=\dfrac{1\pm\sqrt{0.6}}2$ 即 $0.113,0.887$，" "\n"
        r"  都在 $(0,1]$ 内，$n=4+4=8$ ✓，$b+c=1.1\in(0,3)$ ✓；" "\n"
        r"  $b=1.5,c=0.6$ ⟹ $t^{2}-1.5t+0.6=0$，$\Delta=2.25-2.4<0$ 无实根 ✗（$c=0.6>b^{2}/4=0.5625$）✓✓✓" "\n"
        r"**⭐⭐ 通法（$f(f(x))$ 型 / $[f(x)]^{2}+bf(x)+c=0$ 型零点计数）**：" "\n"
        r"① ⭐⭐ 一律换元 $t=f(x)$，把问题拆成「$t$ 的二次方程有几个根」×「每个 $t$ 对应几个 $x$」；" "\n"
        r"② ⭐⭐ 第一件事是画出（或列出）$n(t)$ 的完整分段表，包括所有「平台端点」；" "\n"
        r"③ ⭐⭐ 总根数 $=n(t_{1})+n(t_{2})$，据此反推 $t_{1},t_{2}$ 各自的允许区间；" "\n"
        r"④ ⭐⭐ 用 $g(t)$ 在端点处的符号（$g(0),g(1)$ 等）把「根落在区间内」翻译成参数的线性约束 ✓✓✓"
    ),
    'difficulty': 0.82,
    'topics': ['M-T-069'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-069-V2',
}

T069_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知函数 $f(x)=\begin{cases}\bigl||x+1|-1\bigr|,&x\le0\\ \dfrac{\ln(\mathrm ex)}x+1,&x>0\end{cases}$，" "\n"
        r"若方程 $\bigl[f(x)\bigr]^{2}-mf(x)+n=0$（$n\ne0$）有 $7$ 个不同的实数解，" "\n"
        r"则 $2m+3n$ 的取值范围是（　　）"
    ),
    'opts': [
        ['A', r"$(2,6)$"],
        ['B', r"$(6,9)$"],
        ['C', r"$(2,12)$"],
        ['D', r"$(4,13)$"],
    ],
    'answer': r"C",
    'analysis': (
        r"分段写出 $f$ 的单调区间与值域，列出 $f(x)=t$ 的根数表；"
        r"由 $7=3+4$ 知一个 $t$ 对应 $3$ 个根、另一个对应 $4$ 个根，再分 $t_{1}=0$、$t_{1}\in[1,2)$、$t_{1}=1$ 三类讨论。"
    ),
    'solution': (
        r"**第一步：弄清 $f$ 的图象．**" "\n"
        r"$x\le0$ 段：$f(x)=\bigl||x+1|-1\bigr|$，去绝对值得" "\n"
        r"$f(x)=\begin{cases}-x,&-1<x\le0\\ x+2,&-2<x\le-1\\ -x-2,&x\le-2\end{cases}$，" "\n"
        r"在 $(-\infty,-2]$ 上由 $+\infty$ 减到 $0$，在 $[-2,-1]$ 上由 $0$ 增到 $1$，在 $[-1,0]$ 上由 $1$ 减到 $0$．" "\n"
        r"$x>0$ 段：$f(x)=\dfrac{\ln(\mathrm ex)}x+1=\dfrac{1+\ln x}x+1$，" "\n"
        r"$f'(x)=\dfrac{\dfrac1x\cdot x-(1+\ln x)}{x^{2}}=-\dfrac{\ln x}{x^{2}}$．" "\n"
        r"故 $x\in(0,1)$ 时 $f'(x)>0$，$f$ 递增；$x\in(1,+\infty)$ 时 $f'(x)<0$，$f$ 递减；" "\n"
        r"$f(x)_{\max}=f(1)=2$．又 $x\to0^{+}$ 时 $f\to-\infty$，$x\to+\infty$ 时 $\dfrac{\ln(\mathrm ex)}x\to0$，$f\to1$．" "\n"
        r"**第二步：列出 $f(x)=t$ 的实根个数 $n(t)$．**" "\n"
        r"$t<0$：$x\le0$ 段 $0$ 个，$x>0$ 段 $1$ 个 ⟹ $1$ 个；" "\n"
        r"$t=0$：$x\le0$ 段 $x=-2,0$ 共 $2$ 个，$x>0$ 段 $1$ 个 ⟹ $\mathbf3$ 个；" "\n"
        r"$0<t<1$：$x\le0$ 段 $3$ 个，$x>0$ 段 $1$ 个 ⟹ $\mathbf4$ 个；" "\n"
        r"$t=1$：$x\le0$ 段 $x=-3,-1$ 共 $2$ 个，$x>0$ 段 $1$ 个 ⟹ $\mathbf3$ 个；" "\n"
        r"$1<t<2$：$x\le0$ 段 $1$ 个，$x>0$ 段 $2$ 个 ⟹ $\mathbf3$ 个；" "\n"
        r"$t=2$：$x\le0$ 段 $x=-4$（$1$ 个），$x>0$ 段 $x=1$（$1$ 个）⟹ $2$ 个；" "\n"
        r"$t>2$：$x\le0$ 段 $1$ 个，$x>0$ 段 $0$ 个 ⟹ $1$ 个．" "\n"
        r"**第三步：由根数 $7$ 定出 $t_{1},t_{2}$．**" "\n"
        r"设 $t^{2}-mt+n=0$ 的两根为 $t_{1},t_{2}$，则 $n(t_{1})+n(t_{2})=7$．" "\n"
        r"由表知只能 $3+4$，即一个 $t$ 使 $n=3$、另一个使 $n=4$．" "\n"
        r"由 $n(t)=4\iff t\in(0,1)$，不妨设 $t_{2}\in(0,1)$，则 $t_{1}\in\{0\}\cup[1,2)$．" "\n"
        r"设 $g(t)=t^{2}-mt+n$．" "\n"
        r"① $t_{1}=0$：代入得 $n=0$，与题设 $n\ne0$ 矛盾，舍去；" "\n"
        r"② $t_{1}\in[1,2)$，$t_{2}\in(0,1)$：开口向上且两根分居 $1$ 的两侧（$t_{2}<1\le t_{1}$），" "\n"
        r"  等价于 $g(0)>0$，$g(1)<0$，$g(2)>0$，即 $n>0$，$1-m+n<0$，$4-2m+n>0$．" "\n"
        r"  可行域顶点为 $B(1,0)$（由 $n=0$ 与 $1-m+n=0$）与 $A(3,2)$（由 $1-m+n=0$ 与 $4-2m+n=0$）．" "\n"
        r"  令 $z=2m+3n$，即 $n=-\dfrac23m+\dfrac z3$，平移该直线：" "\n"
        r"  过 $B$ 时 $z=2$，过 $A$ 时 $z=6+6=12$，故 $z\in(2,12)$；" "\n"
        r"③ $t_{1}=1$，$t_{2}\in(0,1)$：等价于 $g(0)>0$，$g(1)=0$，$0<\dfrac m2<1$，" "\n"
        r"  即 $n>0$，$1-m+n=0$，$0<m<2$，可行域为线段 $CB$，其中 $B(1,0)$、$C(2,1)$．" "\n"
        r"  过 $B$ 时 $z=2$，过 $C$ 时 $z=4+3=7$，故 $z\in(2,7)$．" "\n"
        r"综上，$2m+3n\in(2,12)$．故选：C．"
    ),
    'review': (
        r"① ⭐⭐ **题干还原：$x\le0$ 段是 $\bigl||x+1|-1\bigr|$** ——" "\n"
        r"  由详解的三段式反推，代入 $x=-0.5,-1.5,-3$ 得 $0.5,0.5,1$，与三段式逐点吻合 ✓✓" "\n"
        r"② ⭐⭐ **$\dfrac{\ln(\mathrm ex)}x+1=\dfrac{1+\ln x}x+1$，$f'(x)=-\dfrac{\ln x}{x^{2}}$**：" "\n"
        r"  $\ln(\mathrm ex)$ 不是 $\ln(\mathrm e^{x})=x$（那样 $f\equiv2$），判定依据是与详解的三个断言" "\n"
        r"  （$x\in(0,1)$ 递增、$x>1$ 递减、$f(1)=2$、$x\to0^{+}$ 时 $f\to-\infty$）**全部吻合** ✓" "\n"
        r"③ ⭐⭐ **列出 $n(t)$ 表后，$4$ 只出现在 $0<t<1$**：" "\n"
        r"  注意 $t=0$ 与 $t=1$ 处都是 $3$ 个（端点处根「合并」），这是端点必须单独算的原因 ✓" "\n"
        r"④ ⭐⭐ **$n\ne0$ 这个条件只用来排除 $t_{1}=0$**，别小看它，少看就得多讨论一类 ✓" "\n"
        r"⑤ ⭐⭐ **$g(1)<0$ 而非 $\le0$**：对应 $t_{1}\in(1,2)$ 严格；而 $t_{1}=1$ 时要单独作为情形 ③，" "\n"
        r"  两类的 $z$ 范围取并集 $(2,12)\cup(2,7)=(2,12)$ ✓" "\n"
        r"⑥ 数值复核：$m=2,n=1$ ⟹ $t^{2}-2t+1=0$，$t=1$（重根），$n(1)=3\ne7$ ✗，$z=7$ 恰在边界；" "\n"
        r"  $m=2.5,n=1$ ⟹ $t^{2}-2.5t+1=0$，$t=0.5,2$，$n(0.5)=4$、$n(2)=2$ 合计 $6\ne7$ ✗（$t_{1}=2$ 时 $n=2$）；" "\n"
        r"  $m=2.5,n=1.2$ ⟹ $t=1.2,1.3$?? 改取 $m=2.8,n=1.5$：$t^{2}-2.8t+1.5=0$，$\Delta=7.84-6=1.84$，" "\n"
        r"  $t=0.72,2.08$（$t_{2}=0.72\in(0,1)$ ✓，$t_{1}=2.08>2$ ✗）；" "\n"
        r"  取 $m=2.5,n=1.4$：$t^{2}-2.5t+1.4=0$，$\Delta=6.25-5.6=0.65$，$t=0.847,1.653$，" "\n"
        r"  $n(0.847)=4$、$n(1.653)=3$，合计 $7$ ✓，$z=5+4.2=9.2\in(2,12)$ ✓✓✓" "\n"
        r"**⭐⭐ 通法（嵌套方程零点计数的「根数表」法）**：" "\n"
        r"① ⭐⭐ 先彻底弄清外层 $f$ 的图象：分段、单调区间、极值、渐近线、$x\to$ 边界时的极限；" "\n"
        r"② ⭐⭐ 列 $n(t)$ 表时，**每个「平台端点」和「极值」都要单独成行**（本题 $t=0,1,2$）；" "\n"
        r"③ ⭐⭐ 由总根数反推 $t_{1},t_{2}$ 所属区间，按「是否取到端点」分类（往往 $2\sim3$ 类）；" "\n"
        r"④ ⭐⭐ 把「根落在区间内」翻译成 $g$ 在区间端点的符号，得到 $m,n$ 的线性约束后作线性规划 ✓✓✓"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-069'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-069-E1',
}

QS = [
    T156_V1,
    T025_V1,
    T161_E1,
    T167_E1,
    T173_V2,
    T162_E1,
    T111_V2,
    T124_V1,
    T124_V3,
    T069_V2,
    T069_E1,
]
