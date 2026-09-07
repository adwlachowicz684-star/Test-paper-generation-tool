# -*- coding: utf-8 -*-
r"""第24批（上）：M-T-109 不确定单调增或减求参（4题）

来源：2024高中数学热点题型归纳完整解析版.pdf 专题3 p76（PDF 页 75）

## 与 M-T-108 的区别

M-T-108 是「已知**是增函数**」（方向确定）；
M-T-109 是「已知**是单调函数**」——方向未定，必须**分增、减两种情况**讨论，
再把结果取并集。

## 本批四题的分离形态

| 题 | 增的情形 | 减的情形 |
|---|---|---|
| E1 | $a\geqslant0$ | 不可能 |
| V1 | $a\geqslant1$ | $a\leqslant-1$ |
| V2 | 无解 | $a\geqslant2$ |
| V3 | $a\leqslant\frac12$ | $a\geqslant\frac{\mathrm e^2}2$ |
"""

T109_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=x^{2}+a\ln x$．设 $g(x)=f(x)+\dfrac2x$，"
        r"若 $g(x)$ 在 $[1,+\infty)$ 上是单调函数，求实数 $a$ 的取值范围．"
    ),
    'opts': [],
    'answer': r"$[0,+\infty)$",
    'analysis': (
        r"$g'(x)=2x+\dfrac ax-\dfrac2{x^{2}}$；「单调」要分增、减两种。"
        r"递减时 $a\leqslant\dfrac2x-2x^{2}$ 需对所有 $x\geqslant1$ 成立，"
        r"而右端 $\to-\infty$，不可能。"
    ),
    'solution': (
        r"$g(x)=x^{2}+a\ln x+\dfrac2x$，定义域 $(0,+\infty)$，" "\n"
        r"$g'(x)=2x+\dfrac ax-\dfrac2{x^{2}}$．" "\n"
        r"**（ⅰ）若为单调增函数**：$g'(x)\geqslant0$ 在 $[1,+\infty)$ 上恒成立，" "\n"
        r"$\dfrac ax\geqslant\dfrac2{x^{2}}-2x\Rightarrow a\geqslant\dfrac2x-2x^{2}$．" "\n"
        r"设 $\varphi(x)=\dfrac2x-2x^{2}$，"
        r"$\varphi'(x)=-\dfrac2{x^{2}}-4x<0$（$x\geqslant1$），故 $\varphi$ 递减，" "\n"
        r"$\varphi_{\max}=\varphi(1)=2-2=0$，于是 $a\geqslant0$．" "\n"
        r"**（ⅱ）若为单调减函数**：$g'(x)\leqslant0$ 恒成立，"
        r"即 $a\leqslant\dfrac2x-2x^{2}$ 对所有 $x\geqslant1$ 成立．" "\n"
        r"但 $x\to+\infty$ 时 $\dfrac2x-2x^{2}\to-\infty$，无解，**不可能**．" "\n"
        r"综上 $a\in[0,+\infty)$．"
    ),
    'review': (
        r"★ 提取文本作「f(x) = x2+ alnx.(2) 若g(x) = f(x) + 在[1，+∞) 上是单调函数」，"
        r"$x^2$ 上标丢失、$\frac2x$ 的分数线被拆成「2」与「x」两行。"
        r"由详解「$g'(x)=2x+\frac ax-\frac2{x^2}$，若 $g(x)$ 为 $[1,+\infty)$ 上的单调增函数，"
        r"则 $g'(x)\geqslant0$ 恒成立，即 $a\geqslant\frac2x-2x^2$ 恒成立，"
        r"设 $\varphi(x)=\frac2x-2x^2$，因为 $\varphi(x)$ 在 $[1,+\infty)$ 上单调递减，"
        r"所以 $\varphi(x)_{\max}=\varphi(1)=0$，所以 $a\geqslant0$；"
        r"若 $g(x)$ 为单调减函数，则 $g'(x)\leqslant0$ 在 $[1,+\infty)$ 上恒成立，不可能」还原。" "\n"
        r"**导数校验**：$\frac{\mathrm d}{\mathrm dx}\left(\frac2x\right)=-\frac2{x^2}$，"
        r"$\frac{\mathrm d}{\mathrm dx}(a\ln x)=\frac ax$ ✓ 与详解一致，" "\n"
        r"这也反证 $g$ 中加的是 $+\frac2x$（若是 $+2x$ 则导数里不会有 $-\frac2{x^2}$）✓。" "\n"
        r"**数值校验**：$a=0$：$g'(x)=2x-\frac2{x^2}$，$x=1$ 处 $=0$ ✓ 恰取等；"
        r"$x=2$ 处 $=4-0.5=3.5>0$ ✓。"
        r"$a=-0.1$（超出）：$g'(1)=2-0.1-2=-0.1<0$ ✗ 非增 ✓。"
    ),
    'difficulty': 0.75,
    'topics': ['M-T-109'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-109-E1',
}

T109_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=x(x+a)-\ln x$，其中 $a$ 为常数．"
        r"若 $f(x)$ 在区间 $\left(\dfrac12,1\right)$ 上是单调函数，"
        r"求实数 $a$ 的取值范围．"
    ),
    'opts': [],
    'answer': r"$(-\infty,-1]\cup[1,+\infty)$",
    'analysis': (
        r"$f'(x)=\dfrac{2x^{2}+ax-1}{x}$，在 $x>0$ 时符号由分子决定；"
        r"分「增」（分子恒 $\geqslant0$，分离出 $a\geqslant\frac1x-2x$）与"
        r"「减」（开口向上的二次式在两端点 $\leqslant0$）两种情况。"
    ),
    'solution': (
        r"$f(x)=x^{2}+ax-\ln x$，定义域 $(0,+\infty)$，" "\n"
        r"$f'(x)=2x+a-\dfrac1x=\dfrac{2x^{2}+ax-1}{x}$．" "\n"
        r"在区间 $\left(\dfrac12,1\right)$ 上 $x>0$，故 $f'$ 的符号由 "
        r"$h(x)=2x^{2}+ax-1$ 决定．" "\n"
        r"**① 若为增函数**：需 $h(x)\geqslant0$，即 $a\geqslant\dfrac1x-2x$ "
        r"在 $\left(\dfrac12,1\right)$ 上恒成立．" "\n"
        r"设 $y=\dfrac1x-2x$，其导数 $y'=-\dfrac1{x^{2}}-2<0$，故 $y$ 递减，"
        r"在 $\left(\dfrac12,1\right)$ 上 $y<y\!\left(\dfrac12\right)=2-1=1$，" "\n"
        r"于是只需 $a\geqslant1$．" "\n"
        r"**② 若为减函数**：需 $h(x)\leqslant0$ 恒成立．"
        r"$h$ 开口向上，在区间上的最大值在端点取得：" "\n"
        r"$\begin{cases}h\!\left(\dfrac12\right)=\dfrac12+\dfrac a2-1\leqslant0"
        r"\Rightarrow a\leqslant1\\[4pt] h(1)=2+a-1\leqslant0\Rightarrow a\leqslant-1\end{cases}$"
        r"$\Rightarrow a\leqslant-1$．" "\n"
        r"综上 $a\in(-\infty,-1]\cup[1,+\infty)$．"
    ),
    'review': (
        r"★ 提取文本作「f(x) = x(x + a) −lnx」，尚可辨认；"
        r"但详解里区间写成「$(\frac12,1)$」而题干一度被识别为「$(\frac12,1)$」✓。"
        r"由详解「①当 $f(x)$ 是增函数时，$f'(x)=2x+a-\frac1x=\frac{2x^2+ax-1}{x}\geqslant0$ "
        r"在 $(\frac12,1)$ 上恒成立，即 $a\geqslant\frac1x-2x$ 在 $(\frac12,1)$ 上恒成立，"
        r"∵$y=\frac1x-2x$ 在 $(\frac12,1)$ 上是减函数，∴$y<1$，∴$a\geqslant1$；"
        r"②当 $f(x)$ 是减函数时，$2x^2+ax-1\leqslant0$ 在 $(\frac12,1)$ 上恒成立，"
        r"设 $g(x)=2x^2+ax-1$，则 $g(\frac12)\leqslant0$、$g(1)\leqslant0$，解得 $a\leqslant-1$」还原。" "\n"
        r"**数值校验**：$a=1$：$h(\frac12)=0.5+0.5-1=0$ ✓ 恰取等，$f$ 为增 ✓；"
        r"$h(0.75)=2(0.5625)+0.75-1=0.875>0$ ✓。"
        r"$a=-1$：$h(1)=2-1-1=0$ ✓，$h(\frac12)=0.5-0.5-1=-1<0$ ✓，$f$ 为减 ✓。"
        r"$a=0$（在 $(-1,1)$ 内）：$h(\frac12)=-0.5<0$ 但 $h(1)=1>0$ ⇒ 先减后增，非单调 ✗ ✓。"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-109'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-109-V1',
}

T109_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=-\ln x-ax^{2}+4x$（$a>0$）．" "\n"
        r"（1）若 $f(x)$ 是定义域上的单调函数，求 $a$ 的取值范围；" "\n"
        r"（2）若 $f(x)$ 在定义域上有两个极值点 $x_{1},x_{2}$，"
        r"证明：$f(x_{1})+f(x_{2})>3+2\ln2$．"
    ),
    'opts': [],
    'answer': r"（1）$[2,+\infty)$；（2）证明见解析",
    'analysis': (
        r"（1）$f'(x)=\dfrac{-2ax^{2}+4x-1}{x}$，递减等价于 $2a\geqslant-\dfrac1{x^{2}}+\dfrac4x$ 恒成立，"
        r"换元 $t=\frac1x$ 后是二次函数求最大值；递增则无解。"
        r"（2）用韦达定理把 $f(x_1)+f(x_2)$ 表示成 $a$ 的函数，再求其最小值。"
    ),
    'solution': (
        r"定义域 $(0,+\infty)$．$f'(x)=-\dfrac1x-2ax+4=\dfrac{-2ax^{2}+4x-1}{x}$．" "\n"
        r"**（1）**：$x>0$，故符号由 $-2ax^{2}+4x-1$ 决定．" "\n"
        r"**递减**：$f'(x)\leqslant0$ 恒成立 $\iff 2a\geqslant\dfrac{4x-1}{x^{2}}"
        r"=-\dfrac1{x^{2}}+\dfrac4x$．" "\n"
        r"令 $t=\dfrac1x>0$，右端 $=-t^{2}+4t=-(t-2)^{2}+4\leqslant4$，"
        r"故 $2a\geqslant4$，即 $a\geqslant2$．" "\n"
        r"**递增**：$f'(x)\geqslant0$ 恒成立 $\iff 2a\leqslant-t^{2}+4t$ 恒成立．"
        r"但 $-t^{2}+4t$ 在 $t\to+\infty$ 时 $\to-\infty$，**无最小值**，故无解．" "\n"
        r"综上 $a\in[2,+\infty)$．" "\n"
        r"**（2）**：两个极值点即 $-2ax^{2}+4x-1=0$ 有两个正根，" "\n"
        r"$\Delta=16-8a>0\Rightarrow a<2$；又 $a>0$，故 $0<a<2$．" "\n"
        r"由韦达定理：$x_{1}+x_{2}=\dfrac4{2a}=\dfrac2a$，"
        r"$x_{1}x_{2}=\dfrac{-1}{-2a}=\dfrac1{2a}$，" "\n"
        r"$x_{1}^{2}+x_{2}^{2}=(x_{1}+x_{2})^{2}-2x_{1}x_{2}=\dfrac4{a^{2}}-\dfrac1a$．" "\n"
        r"于是" "\n"
        r"$f(x_{1})+f(x_{2})=-\ln(x_{1}x_{2})-a\left(x_{1}^{2}+x_{2}^{2}\right)+4(x_{1}+x_{2})$" "\n"
        r"$=-\ln\dfrac1{2a}-a\left(\dfrac4{a^{2}}-\dfrac1a\right)+\dfrac8a"
        r"=\ln(2a)-\dfrac4a+1+\dfrac8a=\ln(2a)+\dfrac4a+1$．" "\n"
        r"设 $H(a)=\ln(2a)+\dfrac4a+1$（$0<a<2$），"
        r"$H'(a)=\dfrac1a-\dfrac4{a^{2}}=\dfrac{a-4}{a^{2}}<0$（因 $a<2<4$），" "\n"
        r"故 $H$ 在 $(0,2)$ 上递减，$H(a)>H(2)=\ln4+2+1=3+2\ln2$．" "\n"
        r"即 $f(x_{1})+f(x_{2})>3+2\ln2$，证毕．"
    ),
    'review': (
        r"★ 提取文本作「f(x) =-lnx - ax2+ 4x(a > 0)」，$ax^2$ 上标丢失。"
        r"由详解「$f'(x)=-\frac1x-2ax+4=\frac{-2ax^2+4x-1}{x}$」与"
        r"【分析】「利用韦达定理求出 $x_1+x_2=\frac2a$，$x_1x_2=\frac1{2a}$，"
        r"再求出 $f(x_1)+f(x_2)=\ln(2a)+\frac4a+1$，求出函数的最小值即得证」还原。" "\n"
        r"**推导自检**：$x_1^2+x_2^2=\frac4{a^2}-\frac1a$ ✓ → "
        r"$-a(\cdot)=-\frac4a+1$ ✓ → 加上 $\frac8a$ 得 $\frac4a+1$ ✓ **与详解的 $\frac4a+1$ 完全吻合**。" "\n"
        r"**数值校验**：$a=1$：$-2x^2+4x-1=0$ → $x=\frac{4\pm\sqrt{16-8}}{4}=1\pm\frac{\sqrt2}2$，"
        r"$x_1=0.2929$、$x_2=1.7071$ ✓ 两根都正 ✓。"
        r"$H(1)=\ln2+4+1=5.693$；$3+2\ln2=4.386$ ✓ 大于。"
        r"$a=1.9$：$H=\ln3.8+\frac4{1.9}+1=1.335+2.105+1=4.440>4.386$ ✓（接近边界 2）。"
        r"$a\to2^-$：$H\to\ln4+3=4.386$ ✓ 恰为下确界。"
    ),
    'difficulty': 0.95,
    'topics': ['M-T-109'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-109-V2',
}

T109_V3 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=\mathrm e^{x}-ax^{2}-bx-1$（$a,b\in\mathbb R$）．" "\n"
        r"（1）设 $g(x)=f'(x)$，若 $g(x)$ 是 $(0,2)$ 上的单调函数，"
        r"求 $a$ 的取值范围；" "\n"
        r"（2）若 $f(2)=0$，函数 $f(x)$ 在 $(0,2)$ 上有零点，求 $a$ 的取值范围．"
    ),
    'opts': [],
    'answer': (
        r"（1）$a\leqslant\dfrac12$ 或 $a\geqslant\dfrac{\mathrm e^{2}}2$；"
        r"（2）$\dfrac{\mathrm e^{2}-3}4<a<\dfrac{\mathrm e^{2}+1}4$"
    ),
    'analysis': (
        r"（1）$g'(x)=\mathrm e^{x}-2a$ 在 $(0,2)$ 上恒 $\geqslant0$ 或恒 $\leqslant0$；"
        r"（2）$f(0)=0$、$f(2)=0$，要在 $(0,2)$ 内还有零点，"
        r"$f$ 必非单调，即 $g=f'$ 在 $(0,2)$ 内至少有两个零点，"
        r"落到 $g(0)>0$、$g(\ln2a)<0$、$g(2)>0$ 三个条件。"
    ),
    'solution': (
        r"**（1）**：$g(x)=f'(x)=\mathrm e^{x}-2ax-b$，$g'(x)=\mathrm e^{x}-2a$．" "\n"
        r"$g$ 在 $(0,2)$ 上单调 $\iff g'\geqslant0$ 恒成立或 $g'\leqslant0$ 恒成立：" "\n"
        r"$g'\geqslant0$：$2a\leqslant\mathrm e^{x}$ 对 $x\in(0,2)$ 恒成立 $\Rightarrow 2a\leqslant1$"
        r"，即 $a\leqslant\dfrac12$；" "\n"
        r"$g'\leqslant0$：$2a\geqslant\mathrm e^{x}$ 恒成立 $\Rightarrow 2a\geqslant\mathrm e^{2}$，"
        r"即 $a\geqslant\dfrac{\mathrm e^{2}}2$．" "\n"
        r"故 $a\leqslant\dfrac12$ 或 $a\geqslant\dfrac{\mathrm e^{2}}2$．" "\n"
        r"**（2）**：$f(0)=\mathrm e^{0}-0-0-1=0$；由 $f(2)=0$ 得" "\n"
        r"$\mathrm e^{2}-4a-2b-1=0\Rightarrow b=\dfrac{\mathrm e^{2}-4a-1}2$．" "\n"
        r"已有零点 $x=0$ 与 $x=2$，要在 $(0,2)$ 内还有零点，"
        r"$f$ 在 $(0,2)$ 上**不单调**，故 $g=f'$ 在 $(0,2)$ 内至少有两个零点．" "\n"
        r"由（1）的补集，需 $\dfrac12<a<\dfrac{\mathrm e^{2}}2$；"
        r"此时 $g'$ 的零点为 $x=\ln(2a)\in(0,2)$，" "\n"
        r"$g$ 先减后减…实际 $g'(x)=\mathrm e^{x}-2a$ 递增，"
        r"故 $g$ 在 $(0,\ln2a)$ 上递减、在 $(\ln2a,2)$ 上递增，" "\n"
        r"要 $g$ 在 $(0,2)$ 内有两个零点，需" "\n"
        r"$\begin{cases}g(0)>0\\ g(\ln2a)<0\\ g(2)>0\end{cases}$．" "\n"
        r"$g(0)=1-b=1-\dfrac{\mathrm e^{2}-4a-1}2=\dfrac{3+4a-\mathrm e^{2}}2>0"
        r"\Rightarrow a>\dfrac{\mathrm e^{2}-3}4$；" "\n"
        r"$g(2)=\mathrm e^{2}-4a-b=\mathrm e^{2}-4a-\dfrac{\mathrm e^{2}-4a-1}2"
        r"=\dfrac{\mathrm e^{2}-4a+1}2>0\Rightarrow a<\dfrac{\mathrm e^{2}+1}4$；" "\n"
        r"$g(\ln2a)=2a-2a\ln(2a)-b<0$（中间条件，与上述区间相容）．" "\n"
        r"故 $\dfrac{\mathrm e^{2}-3}4<a<\dfrac{\mathrm e^{2}+1}4$．"
    ),
    'review': (
        r"★ 提取文本作「f(x) = ex- ax2- bx - 1」，$\mathrm e^x$ 与 $ax^2$ 上标全丢；"
        r"答案「(1)a ≤1 a ≥e2 (2) e2- 3 < a < e2+ 1 / 2 或2 ；44」是"
        r"「(1) $a\leqslant\frac12$ 或 $a\geqslant\frac{\mathrm e^2}2$；(2) $\frac{\mathrm e^2-3}4<a<\frac{\mathrm e^2+1}4$」。"
        r"由详解「$g(x)=f'(x)=\mathrm e^x-2ax-b$，∴$g'(x)=\mathrm e^x-2a$，"
        r"∵$g(x)$ 在 $(0,2)$ 上单调，∴$g'(x)\geqslant0$ 或 $g'(x)\leqslant0$ 在 $(0,2)$ 上恒成立，"
        r"即 $a\leqslant\frac{\mathrm e^x}2$ 或 $a\geqslant\frac{\mathrm e^x}2$ 在 $(0,2)$ 上恒成立，"
        r"∴$a\leqslant\frac12$ 或 $a\geqslant\frac{\mathrm e^2}2$」与【分析】还原。" "\n"
        r"**数值校验**：$\frac{\mathrm e^2-3}4=\frac{7.389-3}4=1.097$；"
        r"$\frac{\mathrm e^2+1}4=\frac{8.389}4=2.097$；"
        r"$\frac12=0.5$、$\frac{\mathrm e^2}2=3.694$ —— "
        r"$(1.097,2.097)\subset(0.5,3.694)$ ✓ 与（1）的补集相容 ✓。" "\n"
        r"$a=1.5$（在区间内）：$b=\frac{7.389-6-1}2=0.195$；"
        r"$g(0)=1-0.195=0.805>0$ ✓；$g(2)=7.389-6-0.195=1.194>0$ ✓；"
        r"$\ln(2a)=\ln3=1.099$，$g(1.099)=3-3(1.099)-0.195=-0.492<0$ ✓ 三个条件都满足。"
    ),
    'difficulty': 0.98,
    'topics': ['M-T-109'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-109-V3',
}

QS = [T109_E1, T109_V1, T109_V2, T109_V3]
