# -*- coding: utf-8 -*-
r"""第38批（下）：不等式选讲 · 绝对值（4题）

来源：2024高中数学热点题型归纳完整解析版.pdf p418（PDF 页 417）

## 选题

`pick_batch.py --n 14` → p418（M-T-026），A 级。

## ★ 绝对值三大公式（本专题通法）

1. $\lvert x-a\rvert\le m\iff a-m\le x\le a+m$
2. $\lvert x-a\rvert+\lvert x-b\rvert\ge\lvert a-b\rvert$（三角不等式，取等当 $x$ 在 $a,b$ 之间）
3. $f(x)>c$ 恒成立 $\iff f_{\min}>c$；$\exists x$ 使 $f(x)<c\iff f_{\min}<c$

## 四题验算（全部独立推导）

| 题 | 关键 | 答案 |
|---|---|---|
| E1 | $\lvert x+1\rvert\le\lvert x-2\rvert$ 平方 → $x\le\frac12$；$\min f=\lvert a+2\rvert\ge2$ | (1) $x\le\frac12$；(2) $a\ge0$ 或 $a\le-4$ |
| V1 | $[-1,3]\subseteq[a-3,a+3]$；$\lvert x-2a\rvert+\lvert x\rvert\ge2\lvert a\rvert\ge1-2a$ | (1) $[0,2]$；(2) $\frac14$ |
| V2 | 分 $x\ge-3$、$x<-3$ 解；$\lvert t+\frac1t\rvert\le2$ 与 $\ge2$ 夹逼 | (1) $m=2$；(2) $t=\pm1$ |
| V3 | 三段去绝对值；$f_{\min}=3$，$a^{2}-2a<3$ | (I) $(-\infty,-3]\cup[2,+\infty)$；(II) $(-1,3)$ |
"""

T026_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=\lvert x-2\rvert+\lvert x+a\rvert$．" "\n"
        r"（1）若 $a=1$，解不等式 $f(x)\le2\lvert x-2\rvert$；" "\n"
        r"（2）若 $f(x)\ge2$ 恒成立，求实数 $a$ 的取值范围．"
    ),
    'opts': [],
    'answer': r"（1）$x\le\dfrac12$；（2）$a\ge0$ 或 $a\le-4$",
    'analysis': (
        r"（1）代入 $a=1$ 后两边消去 $\lvert x-2\rvert$，化为 $\lvert x+1\rvert\le\lvert x-2\rvert$，平方求解；"
        r"（2）用三角不等式求出 $f$ 的最小值 $\lvert a+2\rvert$，令其 $\ge2$。"
    ),
    'solution': (
        r"**（1）**当 $a=1$ 时，$f(x)=\lvert x-2\rvert+\lvert x+1\rvert$．" "\n"
        r"不等式 $f(x)\le2\lvert x-2\rvert$ 即 "
        r"$\lvert x-2\rvert+\lvert x+1\rvert\le2\lvert x-2\rvert$，" "\n"
        r"两边消去一个 $\lvert x-2\rvert$，得 $\lvert x+1\rvert\le\lvert x-2\rvert$．" "\n"
        r"两边非负，平方：$(x+1)^{2}\le(x-2)^{2}$，" "\n"
        r"即 $x^{2}+2x+1\le x^{2}-4x+4$，得 $6x\le3$，故 $x\le\dfrac12$．" "\n"
        r"**解集为 $\left\{x\mid x\le\frac12\right\}$．**" "\n"
        r"**（2）**由三角不等式" "\n"
        r"$f(x)=\lvert x-2\rvert+\lvert x+a\rvert=\lvert 2-x\rvert+\lvert x+a\rvert\ge\lvert(2-x)+(x+a)\rvert=\lvert a+2\rvert$．" "\n"
        r"（当 $(2-x)(x+a)\ge0$，即 $x$ 在 $-a$ 与 $2$ 之间时取等）" "\n"
        r"故 $f_{\min}=\lvert a+2\rvert$．要使 $f(x)\ge2$ 恒成立，只需 $\lvert a+2\rvert\ge2$：" "\n"
        r"$a+2\ge2$ 或 $a+2\le-2$，解得 $a\ge0$ 或 $a\le-4$．" "\n"
        r"**故 $a$ 的取值范围为 $(-\infty,-4]\cup[0,+\infty)$．**"
    ),
    'review': (
        r"★ 由详解「（1）当 $a=1$ 时，$f(x)\le2\lvert x-2\rvert$，即 $\lvert x+1\rvert\le\lvert x-2\rvert$，"
        r"解得 $x\le\frac12$；（2）$f(x)=\lvert x-2\rvert+\lvert x+a\rvert\ge\lvert x-2-(x+a)\rvert=\lvert a+2\rvert$，"
        r"若 $f(x)\ge2$ 恒成立，只需 $\lvert a+2\rvert\ge2$，即 $a+2\ge2$ 或 $a+2\le-2$，"
        r"解得 $a\ge0$ 或 $a\le-4$」还原。" "\n"
        r"**独立验算**：" "\n"
        r"（1）取 $x=0\le\frac12$：$\lvert0+1\rvert=1\le\lvert0-2\rvert=2$ ✓ 成立" "\n"
        r"取 $x=1>\frac12$：$\lvert1+1\rvert=2\le\lvert1-2\rvert=1$？**不成立** ✓ 符合" "\n"
        r"边界 $x=\frac12$：$\lvert1.5\rvert=1.5\le\lvert-1.5\rvert=1.5$ ✓ 取等" "\n"
        r"（2）取 $a=0$：$f=\lvert x-2\rvert+\lvert x\rvert\ge2$ ✓（最小值恰为 $2$，在 $x\in[0,2]$ 取到）" "\n"
        r"取 $a=-4$：$f=\lvert x-2\rvert+\lvert x-4\rvert\ge2$ ✓（在 $x\in[2,4]$ 取等）" "\n"
        r"取 $a=-1$（应不满足）：$f=\lvert x-2\rvert+\lvert x-1\rvert\ge1<2$ ✗ 正确排除 ✓" "\n"
        r"**答案正确** ✓" "\n"
        r"**⭐ 通法**：「$f(x)\ge c$ 恒成立」⟹ 先求 $f_{\min}$，再令 $f_{\min}\ge c$。"
    ),
    'difficulty': 0.82,
    'topics': ['M-T-026'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-026-E1',
}

T026_V1 = {
    'type': '解答',
    'stem_text': (
        r"设 $f(x)=\lvert x-a\rvert$，$a\in\mathbf R$．" "\n"
        r"（1）当 $-1\le x\le3$ 时，$f(x)\le3$，求 $a$ 的取值范围；" "\n"
        r"（2）若对任意 $x\in\mathbf R$，$f(x-a)+f(x+a)\ge1-2a$ 恒成立，求实数 $a$ 的最小值．"
    ),
    'opts': [],
    'answer': r"（1）$[0,2]$；（2）$\dfrac14$",
    'analysis': (
        r"（1）$\lvert x-a\rvert\le3$ 的解集是 $[a-3,a+3]$，要求 $[-1,3]$ 包含于其中；"
        r"（2）代入得 $\lvert x-2a\rvert+\lvert x\rvert$，用三角不等式求最小值为 $2\lvert a\rvert$。"
    ),
    'solution': (
        r"**（1）**$\lvert x-a\rvert\le3\iff a-3\le x\le a+3$，解集为 $[a-3,\ a+3]$．" "\n"
        r"「当 $-1\le x\le3$ 时 $f(x)\le3$」即区间 $[-1,3]$ 包含于该解集：" "\n"
        r"$\begin{cases}a-3\le-1\\a+3\ge3\end{cases}\iff\begin{cases}a\le2\\a\ge0\end{cases}$，故 $a\in[0,2]$．" "\n"
        r"**（2）**$f(x-a)=\lvert x-a-a\rvert=\lvert x-2a\rvert$，$f(x+a)=\lvert x+a-a\rvert=\lvert x\rvert$．" "\n"
        r"由三角不等式" "\n"
        r"$f(x-a)+f(x+a)=\lvert x-2a\rvert+\lvert x\rvert=\lvert 2a-x\rvert+\lvert x\rvert\ge\lvert(2a-x)+x\rvert=2\lvert a\rvert$．" "\n"
        r"（当 $x$ 在 $0$ 与 $2a$ 之间时取等）故最小值为 $2\lvert a\rvert$．" "\n"
        r"要使 $\ge1-2a$ 恒成立，需 $2\lvert a\rvert\ge1-2a$．" "\n"
        r"· 若 $a\ge0$：$2a\ge1-2a\iff4a\ge1\iff a\ge\dfrac14$；" "\n"
        r"· 若 $a<0$：$-2a\ge1-2a\iff0\ge1$，**无解**．" "\n"
        r"故 $a\ge\dfrac14$，**最小值为 $\dfrac14$**．"
    ),
    'review': (
        r"★ 由详解「（1）$f(x)=\lvert x-a\rvert\le3$，即 $a-3\le x\le a+3$，"
        r"依题意：$\begin{cases}a-3\le-1\\a+3\ge3\end{cases}$，由此得 $a$ 的取值范围是 $[0,2]$；"
        r"（2）$f(x-a)+f(x+a)=\lvert x-2a\rvert+\lvert x\rvert\ge\lvert(x-2a)-x\rvert=2\lvert a\rvert$，"
        r"当且仅当 $(x-2a)x\le0$ 时等号成立…最小值为 $\frac14$」还原。" "\n"
        r"**独立验算**：" "\n"
        r"（1）取 $a=0$：$[-3,3]\supseteq[-1,3]$ ✓；取 $a=2$：$[-1,5]\supseteq[-1,3]$ ✓；"
        r"取 $a=3$（应排除）：$[0,6]\not\supseteq[-1,3]$ ✗ 正确排除 ✓" "\n"
        r"（2）取 $a=\frac14$：$\lvert x-\frac12\rvert+\lvert x\rvert\ge\frac12$，而 $1-2a=\frac12$ → 恰取等 ✓" "\n"
        r"取 $a=0.2<\frac14$：$2a=0.4$，而 $1-2a=0.6$，$0.4\ge0.6$ ✗ 不成立 ✓ 正确排除" "\n"
        r"取 $a=-1$：$2\lvert a\rvert=2$，$1-2a=3$，$2\ge3$ ✗ 不成立 ✓ 负数无解得证" "\n"
        r"**答案正确** ✓" "\n"
        r"**⭐ 易错点**：第（2）问要**分 $a$ 的正负**讨论 $\lvert a\rvert$，"
        r"直接写 $2a\ge1-2a$ 会漏掉 $a<0$ 的情形（虽然本题 $a<0$ 无解，但必须验证）。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-026'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-026-V1',
}

T026_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知不等式 $\lvert x+3\rvert<2x+1$ 的解集为 $\{x\mid x>m\}$．" "\n"
        r"（Ⅰ）求 $m$ 的值；" "\n"
        r"（Ⅱ）设关于 $x$ 的方程 $\lvert x-t\rvert+\left\lvert x+\dfrac1t\right\rvert=m$（$t\ne0$）"
        r"有实数根，求实数 $t$ 的值．"
    ),
    'opts': [],
    'answer': r"（Ⅰ）$m=2$；（Ⅱ）$t=\pm1$",
    'analysis': (
        r"（Ⅰ）按 $x\ge-3$、$x<-3$ 分段去绝对值；"
        r"（Ⅱ）用三角不等式得左边最小值为 $\left\lvert t+\frac1t\right\rvert$，"
        r"方程有解要求它 $\le m=2$，再用基本不等式夹逼取等。"
    ),
    'solution': (
        r"**（Ⅰ）**按绝对值内符号分段（注意右边 $2x+1$ 也须为正才有解）：" "\n"
        r"· 当 $x\ge-3$ 时：$x+3<2x+1\iff x>2$，结合 $x\ge-3$ 得 $x>2$；" "\n"
        r"· 当 $x<-3$ 时：$-(x+3)<2x+1\iff-x-3<2x+1\iff-4<3x\iff x>-\dfrac43$，"
        r"与 $x<-3$ **矛盾，无解**．" "\n"
        r"故解集为 $\{x\mid x>2\}$，**$m=2$**．" "\n"
        r"**（Ⅱ）**由三角不等式" "\n"
        r"$\lvert x-t\rvert+\left\lvert x+\dfrac1t\right\rvert"
        r"=\lvert x-t\rvert+\left\lvert-x-\dfrac1t\right\rvert"
        r"\ge\left\lvert(x-t)+\left(-x-\dfrac1t\right)\right\rvert=\left\lvert t+\dfrac1t\right\rvert$．" "\n"
        r"方程有实数根 $\iff$ 最小值 $\le m=2$，即 $\left\lvert t+\dfrac1t\right\rvert\le2$．" "\n"
        r"另一方面，由基本不等式" "\n"
        r"$\left\lvert t+\dfrac1t\right\rvert=\lvert t\rvert+\dfrac1{\lvert t\rvert}\ge2$"
        r"（$t$ 与 $\frac1t$ 同号，故绝对值可直接拆开）．" "\n"
        r"两边夹逼：$2\le\left\lvert t+\dfrac1t\right\rvert\le2$，故 $\left\lvert t+\dfrac1t\right\rvert=2$，" "\n"
        r"取等条件为 $\lvert t\rvert=\dfrac1{\lvert t\rvert}$，即 $\lvert t\rvert=1$，**$t=\pm1$**．"
    ),
    'review': (
        r"★ 由详解「（Ⅰ）…$\begin{cases}x<-3\\-(x+3)<2x+1\end{cases}$ 或 "
        r"$\begin{cases}x\ge-3\\x+3<2x+1\end{cases}$…得 $x=2$，依题意 $m=2$。" "\n"
        r"（Ⅱ）因为 $m=2=\lvert x-t\rvert+\lvert x+\frac1t\rvert\ge\lvert x-t-(x+\frac1t)\rvert=\lvert t+\frac1t\rvert$，"
        r"当且仅当 $(x-t)(x+\frac1t)\le0$ 时等号成立。∵$m=2$，∴需要 $\lvert t\rvert+\frac1{\lvert t\rvert}\le2$；"
        r"另一方面 $\lvert t\rvert+\frac1{\lvert t\rvert}\ge2$，当且仅当 $\lvert t\rvert=\frac1{\lvert t\rvert}$ 时等号成立，"
        r"∴只有 $\lvert t\rvert=1$」还原。" "\n"
        r"**独立验算**：" "\n"
        r"（Ⅰ）取 $x=3>2$：$\lvert6\rvert=6<2\times3+1=7$ ✓ 成立" "\n"
        r"取 $x=1<2$：$\lvert4\rvert=4<3$？**不成立** ✓ 符合" "\n"
        r"取 $x=-4$（属第二段）：$\lvert-1\rvert=1<-7$？不成立 ✓ 无解得证" "\n"
        r"（Ⅱ）取 $t=1$：方程 $\lvert x-1\rvert+\lvert x+1\rvert=2$，"
        r"当 $x\in[-1,1]$ 时左边 $=2$ ✓ **有解**（无穷多解）" "\n"
        r"取 $t=2$：$\lvert x-2\rvert+\lvert x+0.5\rvert\ge2.5>2$ ✗ **无解** ✓ 正确排除" "\n"
        r"取 $t=-1$：$\lvert x+1\rvert+\lvert x-1\rvert=2$ ✓ 同上，有解" "\n"
        r"**答案正确** ✓" "\n"
        r"**⭐ 本题精华**：「方程有解」$\iff$ 左边最小值 $\le$ 右边。"
        r"而最小值由三角不等式给出，再用基本不等式从下方夹住 —— "
        r"**上下夹逼**是求参数取值的经典手法。"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-026'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-026-V2',
}

T026_V3 = {
    'type': '解答',
    'stem_text': (
        r"已知 $f(x)=\lvert x-1\rvert+\lvert x+2\rvert$．" "\n"
        r"（Ⅰ）解不等式 $f(x)\ge5$；" "\n"
        r"（Ⅱ）若关于 $x$ 的不等式 $f(x)>a^{2}-2a$ 对任意 $x\in\mathbf R$ 恒成立，"
        r"求 $a$ 的取值范围．"
    ),
    'opts': [],
    'answer': r"（Ⅰ）$(-\infty,-3]\cup[2,+\infty)$；（Ⅱ）$(-1,3)$",
    'analysis': (
        r"（Ⅰ）按 $x\le-2$、$-2<x<1$、$x\ge1$ 三段去绝对值；"
        r"（Ⅱ）先求 $f_{\min}=3$，再由「恒成立」得 $a^{2}-2a<3$。"
    ),
    'solution': (
        r"**（Ⅰ）**两个零点为 $x=-2$、$x=1$，分三段：" "\n"
        r"· 当 $x\le-2$ 时：$f(x)=(1-x)+(-x-2)=-2x-1$，" "\n"
        r"$-2x-1\ge5\iff-2x\ge6\iff x\le-3$，结合 $x\le-2$ 得 $x\le-3$；" "\n"
        r"· 当 $-2<x<1$ 时：$f(x)=(1-x)+(x+2)=3$，$3\ge5$ **不成立**；" "\n"
        r"· 当 $x\ge1$ 时：$f(x)=(x-1)+(x+2)=2x+1$，" "\n"
        r"$2x+1\ge5\iff x\ge2$，结合 $x\ge1$ 得 $x\ge2$．" "\n"
        r"**综上，解集为 $(-\infty,-3]\cup[2,+\infty)$．**" "\n"
        r"**（Ⅱ）**由三角不等式" "\n"
        r"$f(x)=\lvert x-1\rvert+\lvert x+2\rvert\ge\lvert(x-1)-(x+2)\rvert=3$，" "\n"
        r"当 $-2\le x\le1$ 时取等，故 $f_{\min}=3$．" "\n"
        r"（也可由（Ⅰ）中的分段结果直接看出中间段恒为 $3$）" "\n"
        r"要使 $f(x)>a^{2}-2a$ 对任意 $x$ 恒成立，只需 $f_{\min}>a^{2}-2a$：" "\n"
        r"$a^{2}-2a<3\iff a^{2}-2a-3<0\iff(a-3)(a+1)<0\iff-1<a<3$．" "\n"
        r"**故 $a$ 的取值范围为 $(-1,3)$．**"
    ),
    'review': (
        r"★ 题干、答案完整 ✓（**原书详解在下一页、未提取到**，"
        r"上述推导为我独立完成，并用答案交叉验证）。" "\n"
        r"**独立验算**：" "\n"
        r"（Ⅰ）取 $x=-3$：$f=\lvert-4\rvert+\lvert-1\rvert=4+1=5\ge5$ ✓ 取等（端点闭）" "\n"
        r"取 $x=-2.5$：$f=\lvert-3.5\rvert+\lvert-0.5\rvert=3.5+0.5=4<5$ ✗ 不在解集内 ✓" "\n"
        r"取 $x=2$：$f=\lvert1\rvert+\lvert4\rvert=5\ge5$ ✓ 取等" "\n"
        r"取 $x=0$：$f=1+2=3<5$ ✗ 正确排除 ✓" "\n"
        r"（Ⅱ）取 $a=0\in(-1,3)$：$a^2-2a=0$，$f_{\min}=3>0$ ✓ 恒成立" "\n"
        r"取 $a=-1$（边界）：$a^2-2a=1+2=3$，$f_{\min}=3$ → $3>3$ ✗ **不成立** ✓ 开区间正确" "\n"
        r"取 $a=3$（边界）：$9-6=3$，同样 $3>3$ ✗ ✓ 开区间正确" "\n"
        r"取 $a=4$（应排除）：$16-8=8$，$3>8$ ✗ 不成立 ✓ 正确排除" "\n"
        r"**答案正确** ✓" "\n"
        r"**⭐ 易错点**：（Ⅱ）是 $f(x)>\cdots$ **严格大于**，"
        r"所以条件是 $f_{\min}>a^{2}-2a$（严格），端点 $a=-1,3$ 处 $f_{\min}=3=a^2-2a$，"
        r"不满足严格大于，**必须取开区间**。若题干是 $\ge$ 则可取闭区间。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-026'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-026-V3',
}

QS = [T026_E1, T026_V1, T026_V2, T026_V3]
