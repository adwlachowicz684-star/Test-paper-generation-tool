# -*- coding: utf-8 -*-
r"""第24批（下）：M-T-110 存在单调增(减)区间（3题）

来源：2024高中数学热点题型归纳完整解析版.pdf 专题3 p77~p78（PDF 页 76~77）

## 与前面几个题型的区别（关键！）

| 题型 | 条件 | 数学表述 |
|---|---|---|
| M-T-108 | 在 $I$ 上**是**增函数 | $f'(x)\geqslant0$ **恒成立** |
| M-T-110 | 在 $I$ 上**存在**增区间 | $f'(x)>0$ **有解** |

「恒成立」看**最小值/最大值**；
「有解」看**最大值 > 0**（或最小值 < 0）。**别把两者搞混**——这是本专题最易错处。

## 本批跳过

**M-T-110-V1（原书第 36 题）**：提取文本严重损坏，
题干与详解中的每一处表达式都被替换成了「f(x) = x(x + a) −lnx」这个字符串本身
（例如「若 f(x) = x(x+a)−lnx，即 f(x) = x(x+a)−lnx，从而 f(x) 在 R 上是减函数」），
**答案也变成了题干**。无任何可还原的信息，跳过。
"""

T110_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=x+a\ln x$ 在 $x=1$ 处的切线与直线 $x+2y=0$ 垂直，"
        r"函数 $g(x)=f(x)+\dfrac12x^{2}-bx$．" "\n"
        r"（1）求实数 $a$ 的值；" "\n"
        r"（2）若函数 $g(x)$ 存在单调递减区间，求实数 $b$ 的取值范围．"
    ),
    'opts': [],
    'answer': r"（1）$a=1$；（2）$(3,+\infty)$",
    'analysis': (
        r"（1）直线 $x+2y=0$ 斜率为 $-\frac12$，与之垂直的斜率为 $2$，故 $f'(1)=2$；"
        r"（2）「存在递减区间」$\iff$ $g'(x)<0$ **有解**，"
        r"即分子 $\mu(x)=x^{2}-(b-1)x+1$ 能取到负值——需要顶点在正半轴且判别式 $>0$。"
    ),
    'solution': (
        r"**（1）**：$f'(x)=1+\dfrac ax$，在 $x=1$ 处切线斜率为 $f'(1)=1+a$．" "\n"
        r"直线 $x+2y=0$ 即 $y=-\dfrac x2$，斜率为 $-\dfrac12$；"
        r"与之垂直的直线斜率为 $2$，" "\n"
        r"故 $1+a=2$，得 $a=1$．" "\n"
        r"**（2）**：由（1）$f(x)=x+\ln x$，" "\n"
        r"$g(x)=x+\ln x+\dfrac12x^{2}-bx=\ln x+\dfrac12x^{2}-(b-1)x$（$x>0$），" "\n"
        r"$g'(x)=\dfrac1x+x-(b-1)=\dfrac{x^{2}-(b-1)x+1}{x}$．" "\n"
        r"「存在单调递减区间」$\iff$ $g'(x)<0$ 在 $(0,+\infty)$ 上**有解**"
        r"$\iff$ $\mu(x)=x^{2}-(b-1)x+1$ 能取负值（注意 $x>0$）．" "\n"
        r"$\mu(0)=1>0$，开口向上，故需" "\n"
        r"$\begin{cases}\Delta=(b-1)^{2}-4>0\\ "
        r"\text{对称轴 } \dfrac{b-1}2>0\end{cases}$"
        r"$\Rightarrow\begin{cases}b>3\ \text{或}\ b<-1\\ b>1\end{cases}\Rightarrow b>3$．" "\n"
        r"故 $b\in(3,+\infty)$．"
    ),
    'review': (
        r"★ 提取文本作「f (x)= x + alnx 在x = 1 处的切线与直线x + 2y = 0 垂直，"
        r"函数g (x)= f (x)+ x2- bx」，$\frac12x^2$ 的分数线与上标丢失（写成 x2），"
        r"一度会误读成 $+x^2$。"
        r"由详解「$g(x)=\ln x+\frac12x^2-(b-1)x$（$x>0$），"
        r"$g'(x)=\frac1x+x-(b-1)=\frac{x^2-(b-1)x+1}{x}$」**反推锁定为 $\frac12x^2$** ✓"
        r"（若是 $+x^2$ 则导数里 $x$ 的系数是 $2$ 而非 $1$）。" "\n"
        r"**数值校验**：$a=1$ 时 $f'(1)=1+1=2$ ✓ 与直线 $x+2y=0$ 垂直 ✓。"
        r"$b=4$（$>3$）：$\mu(x)=x^2-3x+1$，$\Delta=9-4=5>0$，"
        r"根 $x=\frac{3\pm\sqrt5}2$，两根间 $\mu<0$ ✓ 存在递减区间 ✓。"
        r"$b=3$：$\mu=x^2-2x+1=(x-1)^2\geqslant0$，$g'\geqslant0$ 恒成立，无递减区间 ✗ ✓（故取开区间）。"
        r"$b=2$：$\mu=x^2-x+1$，$\Delta=1-4<0$，恒正 ✗ ✓。"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-110'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-110-E1',
}

T110_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=ax-\dfrac{1+x}{\mathrm e^{x}}$．" "\n"
        r"（1）若曲线 $y=f(x)$ 在点 $\bigl(0,f(0)\bigr)$ 处的切线方程为 $y=x+b$，"
        r"求实数 $a,b$ 的值；" "\n"
        r"（2）若函数 $f(x)$ 在区间 $(0,2)$ 上存在单调增区间，"
        r"求实数 $a$ 的取值范围；" "\n"
        r"（3）若 $f(x)$ 在区间 $(0,2)$ 上存在极大值，求实数 $a$ 的取值范围"
        r"（直接写出结果）．"
    ),
    'opts': [],
    'answer': (
        r"（1）$a=1,\ b=-1$；（2）$\left(-\dfrac1{\mathrm e},+\infty\right)$；"
        r"（3）$\left(-\dfrac1{\mathrm e},\ -\dfrac2{\mathrm e^{2}}\right)$"
    ),
    'analysis': (
        r"关键是求导：$f'(x)=a-\dfrac{1-(1+x)}{\mathrm e^{x}}=a+\dfrac x{\mathrm e^{x}}$"
        r"（商的导数化简后分子为 $-x$，再与前面的负号抵消）；"
        r"（2）「存在增区间」$\iff$ $f'(x)>0$ **有解** $\iff$ "
        r"$f'$ 在 $(0,2)$ 上的**最大值** $>0$。"
    ),
    'solution': (
        r"**（1）**：$f'(x)=a-\dfrac{1\cdot\mathrm e^{x}-(1+x)\mathrm e^{x}}{\mathrm e^{2x}}"
        r"=a-\dfrac{-x}{\mathrm e^{x}}=a+\dfrac x{\mathrm e^{x}}$．" "\n"
        r"$f'(0)=a+0=a$；切线 $y=x+b$ 的斜率为 $1$，故 $a=1$．" "\n"
        r"$f(0)=0-\dfrac{1+0}{1}=-1$，切点为 $(0,-1)$，代入切线：$-1=0+b$，故 $b=-1$．" "\n"
        r"**（2）**：「存在单调增区间」$\iff$ $f'(x)=a+\dfrac x{\mathrm e^{x}}>0$ "
        r"在 $(0,2)$ 上**有解**，" "\n"
        r"即只需 $f'(x)$ 在 $(0,2)$ 上的**最大值** $>0$．" "\n"
        r"设 $h(x)=\dfrac x{\mathrm e^{x}}$，$h'(x)=\dfrac{1-x}{\mathrm e^{x}}$：" "\n"
        r"$x\in(0,1)$ 时 $h'>0$，$h$ 递增；$x\in(1,2)$ 时 $h'<0$，$h$ 递减；" "\n"
        r"故 $h$ 在 $x=1$ 处取最大值 $h(1)=\dfrac1{\mathrm e}$．" "\n"
        r"于是 $f'_{\max}=a+\dfrac1{\mathrm e}>0$，即 $a>-\dfrac1{\mathrm e}$，" "\n"
        r"$a\in\left(-\dfrac1{\mathrm e},+\infty\right)$．" "\n"
        r"**（3）**：$f$ 在 $(0,2)$ 上存在极大值，需 $f'$ 在 $(0,2)$ 内由正变负．"
        r"结合 $h$ 先增后减的形状，" "\n"
        r"得 $a\in\left(-\dfrac1{\mathrm e},\ -\dfrac2{\mathrm e^{2}}\right)$（原书答案）．"
    ),
    'review': (
        r"★ 提取文本作「f(x) = ax -． / ex / 1 + x」与"
        r"「f′(x) = a -= + a / ex ex / 1 - (1 + x) x」，"
        r"$\frac{1+x}{\mathrm e^x}$ 的分数线丢失，分子「1 + x」与分母「ex」分列两行；"
        r"导数那行更乱：实际是 $f'(x)=a-\frac{1-(1+x)}{\mathrm e^x}=a+\frac{x}{\mathrm e^x}$，"
        r"中间的「1 - (1 + x)」就是分子化简过程。"
        r"由详解「$f'(x)=a-\frac{1-(1+x)}{\mathrm e^x}=\frac{x}{\mathrm e^x}+a$，所以 $f'(0)=a$；"
        r"切线斜率为 1，即 $a=1$，$f(0)=-1=b$」还原。" "\n"
        r"**导数独立验证**：$\frac{\mathrm d}{\mathrm dx}\frac{1+x}{\mathrm e^x}"
        r"=\frac{\mathrm e^x-(1+x)\mathrm e^x}{\mathrm e^{2x}}=\frac{-x}{\mathrm e^x}$ ✓，"
        r"故 $f'=a-\frac{-x}{\mathrm e^x}=a+\frac{x}{\mathrm e^x}$ ✓。" "\n"
        r"**数值校验**：$h(1)=\frac1{\mathrm e}=0.3679$ ✓；$h(2)=\frac2{\mathrm e^2}=0.2707$ ✓；"
        r"$h(0.5)=\frac{0.5}{\mathrm e^{0.5}}=0.3033$ ✓ 均小于 $h(1)$。"
        r"（3）的下界 $-\frac2{\mathrm e^2}=-0.2707$ 正是 $-h(2)$——"
        r"即要求 $f'(2)=a+h(2)<0$（右端为负才能出现极大值）✓ 与（2）的上界 $a>-\frac1{\mathrm e}$ 组合自洽 ✓。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-110'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-110-V2',
}

T110_V3 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=x\ln x-ax^{2}$，$a\in\mathbb R$．" "\n"
        r"（1）若函数 $f(x)$ 存在单调增区间，求实数 $a$ 的取值范围；"
    ),
    'opts': [],
    'answer': r"$a<\dfrac12$",
    'analysis': (
        r"$f'(x)=1+\ln x-2ax$；「存在增区间」$\iff$ $f'(x)>0$ **有解**"
        r"$\iff$ $2a<\dfrac{1+\ln x}{x}$ 有解 $\iff$ $2a<\left(\dfrac{1+\ln x}{x}\right)_{\max}$。"
    ),
    'solution': (
        r"定义域 $(0,+\infty)$．$f'(x)=1+\ln x-2ax$．" "\n"
        r"「存在单调增区间」$\iff$ $f'(x)>0$ 在 $(0,+\infty)$ 上**有解**，" "\n"
        r"即 $2a<\dfrac{1+\ln x}{x}$ 有解，只需 $2a<\left(\dfrac{1+\ln x}{x}\right)_{\max}$．" "\n"
        r"设 $g(x)=\dfrac{1+\ln x}{x}$，则 "
        r"$g'(x)=\dfrac{\frac1x\cdot x-(1+\ln x)}{x^{2}}=\dfrac{-\ln x}{x^{2}}$：" "\n"
        r"$x\in(0,1)$ 时 $g'(x)>0$，$g$ 递增；$x\in(1,+\infty)$ 时 $g'(x)<0$，$g$ 递减；" "\n"
        r"故 $g_{\max}=g(1)=\dfrac{1+0}{1}=1$．" "\n"
        r"于是 $2a<1$，即 $a<\dfrac12$．"
    ),
    'review': (
        r"★ 提取文本作「f (x)= xlnx - ax2，a ∈R」，$ax^2$ 上标丢失。"
        r"由详解「由题函数存在增区间，即需 $f'(x)=1+\ln x-2ax>0$ 有解，"
        r"即 $2a<\frac{1+\ln x}{x}$ 有解，设 $g(x)=\frac{1+\ln x}{x}$，"
        r"$g'(x)=\frac{-\ln x}{x^2}$，当 $x\in(0,1)$ 时 $g'(x)>0$、当 $x\in(1,+\infty)$ 时 $g'(x)<0$，"
        r"故当 $2a<g(x)_{\max}=1$，∴$a<\frac12$ 时，函数 $f(x)$ 存在增区间」还原。" "\n"
        r"**导数校验**：$\frac{\mathrm d}{\mathrm dx}(x\ln x)=\ln x+1$ ✓；"
        r"$g'(x)=\frac{\frac1x\cdot x-(1+\ln x)\cdot1}{x^2}=\frac{1-1-\ln x}{x^2}=\frac{-\ln x}{x^2}$ ✓。" "\n"
        r"**数值校验**：$a=\frac12$：$f'=1+\ln x-x$，在 $x=1$ 处 $=0$，其余 $x\neq1$ 处 "
        r"由 $\ln x\leqslant x-1$ 知 $1+\ln x-x\leqslant0$ ⇒ 无增区间 ✗ ✓（故取严格小于）。"
        r"$a=0.4$：$f'(1)=1-0.8=0.2>0$ ✓ 有增区间 ✓。"
        r"$a=0$：$f'=1+\ln x$，$x>1/\mathrm e$ 时 $>0$ ✓。"
    ),
    'difficulty': 0.7,
    'topics': ['M-T-110'],
    'src': '2024高中数学热点题型归纳完整版解析版.pdf · M-T-110-V3',
}

QS = [T110_E1, T110_V2, T110_V3]
