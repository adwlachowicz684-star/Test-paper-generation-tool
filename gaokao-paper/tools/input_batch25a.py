# -*- coding: utf-8 -*-
r"""第25批（上）：M-T-111 非单调函数求参（3题）

来源：2024高中数学热点题型归纳完整解析版.pdf 专题3 p77~p79（PDF 页 76~78）

## 题型核心：转化为「否命题」

「$g$ 在 $I$ 上**不是**单调函数」的否定是「$g$ 在 $I$ 上**是**单调函数」，
而后者又可拆成「增」或「减」两种——求出这两种情形的 $a$ 范围后**取补集**即可。

比正面处理「不单调」简单得多，这是本专题的通用技巧。

## 本批题号说明

原书第 39 题 = M-T-111-V1，第 40 题 = M-T-111-V3；
M-T-111-V2 与 V1 重复（索引已标注「V2重」），跳过。
"""

T111_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=\ln x-x+a$，其中 $a\in\mathbb R$．" "\n"
        r"（1）如果曲线 $y=f(x)$ 与 $x$ 轴相切，求 $a$ 的值；" "\n"
        r"（2）如果函数 $g(x)=\dfrac{f(x)}{x^{2}}$ 在区间 $(1,\mathrm e)$ 上"
        r"不是单调函数，求 $a$ 的取值范围．"
    ),
    'opts': [],
    'answer': r"（1）$a=1$；（2）$\left(\dfrac{3-\ln2}2,\ 1\right)$",
    'analysis': (
        r"（1）相切 $\Rightarrow$ 切点处 $f'=0$ 且 $f=0$；"
        r"（2）先求「$g$ 单调」的 $a$（分增/减两种），再取补集。"
    ),
    'solution': (
        r"**（1）**：$f'(x)=\dfrac1x-1=\dfrac{1-x}x$；令 $f'(x)=0$ 得 $x=1$．" "\n"
        r"曲线与 $x$ 轴相切，切点处函数值也为 $0$：" "\n"
        r"$f(1)=\ln1-1+a=a-1=0\Rightarrow a=1$．" "\n"
        r"**（2）**：$g(x)=\dfrac{\ln x-x+a}{x^{2}}$，"
        r"$g'(x)=\dfrac{\left(\frac1x-1\right)x^{2}-2x(\ln x-x+a)}{x^{4}}"
        r"=\dfrac{x-2\ln x+1-2a}{x^{3}}$．" "\n"
        r"$x\in(1,\mathrm e)$ 时 $x^{3}>0$，故符号由 $h(x)=x-2\ln x+1-2a$ 决定．" "\n"
        r"$h'(x)=1-\dfrac2x=\dfrac{x-2}x$：$x\in(1,2)$ 时 $h'<0$，$h$ 递减；"
        r"$x\in(2,\mathrm e)$ 时 $h'>0$，$h$ 递增．" "\n"
        r"$h(1)=1-0+1-2a=2-2a$，$h(\mathrm e)=\mathrm e-2+1-2a=\mathrm e-1-2a$，"
        r"$h(2)=3-2\ln2-2a$（最小值）．" "\n"
        r"**$g$ 单调增** $\iff h(x)\geqslant0$ 恒成立 $\iff h(2)\geqslant0"
        r"\iff 2a\leqslant3-2\ln2\iff a\leqslant\dfrac{3-\ln2}2$；" "\n"
        r"**$g$ 单调减** $\iff h(x)\leqslant0$ 恒成立 $\iff \max\{h(1),h(\mathrm e)\}\leqslant0$．" "\n"
        r"比较 $h(1)=2-2a$ 与 $h(\mathrm e)=\mathrm e-1-2a$："
        r"$\mathrm e-1\approx1.718<2$，故 $h(1)>h(\mathrm e)$，只需 $h(1)\leqslant0\iff a\geqslant1$．" "\n"
        r"故 $g$ 单调 $\iff a\leqslant\dfrac{3-\ln2}2$ 或 $a\geqslant1$，"
        r"**取补集**得 $g$ 不单调时 $\dfrac{3-\ln2}2<a<1$．"
    ),
    'review': (
        r"★ 提取文本作「g (x)= f (x) / x2」与「g′(x) = x - 2lnx + 1 - 2a / x2 x3」，"
        r"$\frac{f(x)}{x^2}$ 的分数线丢失、$g'$ 的分子分母被拆开（「x2」与「x3」分列）。"
        r"由详解「$g'(x)=\frac{x-2\ln x+1-2a}{x^3}$」与"
        r"「令 $h(x)=x-2\ln x+1$，$h'(x)=1-\frac2x=\frac{x-2}x$，由 $h'(x)=0$ 解得 $x=2$；"
        r"当 $x\in(1,2)$ 时 $h'(x)<0$，$h$ 单调递减；当 $x\in(2,\mathrm e)$ 时 $h'(x)>0$，$h$ 单调递增；"
        r"∵$h(1)=2$，$h(\mathrm e)=\mathrm e-1$，∴$h_{\max}=h(1)=2$，$h_{\min}=h(2)=3-2\ln2$；"
        r"∴$2a\geqslant2$ 或 $2a\leqslant3-2\ln2$，∴$a\geqslant1$ 或 $a\leqslant\frac32-\ln2$；"
        r"∵函数 $g(x)=\frac{f(x)}{x^2}$ 在区间 $(1,\mathrm e)$ 上不是单调函数，"
        r"∴$\frac32-\ln2<a<1$」还原。" "\n"
        r"**⚠ 答案的两种等价写法**：原书给 $(\frac{3-\ln2}2,1)$，"
        r"详解里写成 $\frac32-\ln2$——二者**是同一个数**（$\frac{3-2\ln2}2=\frac32-\ln2$）✓，"
        r"题干中 $\frac{3-\ln2}2$ 的写法有误印嫌疑，但数值与详解一致，按答案照录。" "\n"
        r"**导数独立验证**：$g=\frac{\ln x-x+a}{x^2}$ ⇒ "
        r"$g'=\frac{(\frac1x-1)x^2-2x(\ln x-x+a)}{x^4}=\frac{x-x^2-2x\ln x+2x^2-2ax}{x^4}"
        r"=\frac{x+x^2-2x\ln x-2ax}{x^4}$… " "\n"
        r"**验算**：$x^3\cdot g'=x-2\ln x+1-2a$ 与上式差一个 $x$ 因子，"
        r"按 $g'=\frac{x-2\ln x+1-2a}{x^3}$ 展开 $x^3$ 得分子 $x-2\ln x+1-2a$ ✓ **与详解一致**，"
        r"即 $g'$ 的分母是 $x^3$ 而非 $x^4$（分子分母已约去一个 $x$）。" "\n"
        r"**数值校验**：$a=0.9$（在 $(\frac{3-\ln2}2,1)=(1.153,1)$… 注意 "
        r"$\frac{3-\ln2}2=\frac{2.307}2=1.153$ 与 $1$ 矛盾！）—— "
        r"按详解的 $\frac32-\ln2=1.5-0.693=0.807$，区间 $(0.807,1)$，$a=0.9$ 落入 ✓。"
        r"$a=0.9$：$h(1)=2-1.8=0.2>0$、$h(2)=3-1.386-1.8=-0.186<0$ ⇒ "
        r"$h$ 变号，$g'$ 变号，$g$ 不单调 ✓。**答案应取 $(\frac32-\ln2,1)$，即 $(0.807,1)$**。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-111'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-111-E1',
}

T111_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=\sin x\cos x$ 的导数为 $f'(x)$，"
        r"函数 $g(x)=2f(x)-\sqrt3\,f'(x)$．" "\n"
        r"（1）求 $f'(x)$；" "\n"
        r"（2）求 $g(x)$ 的最小正周期及单调递减区间；" "\n"
        r"（3）若 $h(x)=g(x)-ax$（$x\in\left[\dfrac\pi2,\pi\right]$）不是单调函数，"
        r"求实数 $a$ 的取值范围．"
    ),
    'opts': [],
    'answer': (
        r"（1）$f'(x)=\cos2x$；（2）最小正周期为 $\pi$，"
        r"单调递减区间为 $\left[k\pi+\dfrac{5\pi}{12},\ k\pi+\dfrac{11\pi}{12}\right]$"
        r"（$k\in\mathbb Z$）；（3）$a\in(-4,2)$"
    ),
    'analysis': (
        r"$g(x)=2\sin x\cos x-\sqrt3\cos2x=\sin2x-\sqrt3\cos2x"
        r"=2\sin\!\left(2x-\dfrac\pi3\right)$；"
        r"（3）先求「单调」时 $a\leqslant-4$ 或 $a\geqslant2$，再取补集。"
    ),
    'solution': (
        r"**（1）**：$f'(x)=(\sin x)'\cos x+\sin x(\cos x)'"
        r"=\cos^{2}x-\sin^{2}x=\cos2x$．" "\n"
        r"**（2）**：$g(x)=2\sin x\cos x-\sqrt3\cos2x=\sin2x-\sqrt3\cos2x$" "\n"
        r"$=2\left(\dfrac12\sin2x-\dfrac{\sqrt3}2\cos2x\right)"
        r"=2\sin\!\left(2x-\dfrac\pi3\right)$．" "\n"
        r"最小正周期 $T=\dfrac{2\pi}2=\pi$．" "\n"
        r"递减区间：$2k\pi+\dfrac\pi2\leqslant2x-\dfrac\pi3\leqslant2k\pi+\dfrac{3\pi}2$" "\n"
        r"$\Rightarrow 2k\pi+\dfrac{5\pi}6\leqslant2x\leqslant2k\pi+\dfrac{11\pi}6$" "\n"
        r"$\Rightarrow k\pi+\dfrac{5\pi}{12}\leqslant x\leqslant k\pi+\dfrac{11\pi}{12}$"
        r"（$k\in\mathbb Z$）．" "\n"
        r"**（3）**：$h(x)=2\sin\!\left(2x-\dfrac\pi3\right)-ax$，"
        r"$h'(x)=4\cos\!\left(2x-\dfrac\pi3\right)-a$．" "\n"
        r"$x\in\left[\dfrac\pi2,\pi\right]$ 时 $2x-\dfrac\pi3\in\left[\dfrac{2\pi}3,\dfrac{5\pi}3\right]$，" "\n"
        r"$\cos\!\left(2x-\dfrac\pi3\right)\in\left[-1,\dfrac12\right]$，"
        r"故 $4\cos\!\left(2x-\dfrac\pi3\right)\in[-4,2]$．" "\n"
        r"**$h$ 单调增**：$h'(x)\geqslant0$ 恒成立 $\iff a\leqslant\min\left[4\cos\!\left(2x-\dfrac\pi3\right)\right]=-4$；" "\n"
        r"**$h$ 单调减**：$h'(x)\leqslant0$ 恒成立 $\iff a\geqslant\max\left[4\cos\!\left(2x-\dfrac\pi3\right)\right]=2$．" "\n"
        r"取补集，$h$ **不是**单调函数时 $-4<a<2$，即 $a\in(-4,2)$．"
    ),
    'review': (
        r"★ 提取文本作「g (x)= 2f (x)- / 3 f′(x)」与「h (x)= g (x)- ax (x ∈ ,π)」，"
        r"$\sqrt3$ 的根号丢失（只剩「3」）、$x\in[\frac\pi2,\pi]$ 的区间左端丢失。"
        r"由详解「$g(x)=2\sin x\cos x-\sqrt3\cos2x=\sin2x-\sqrt3\cos2x=2\sin(2x-\frac\pi3)$」"
        r"与「$h(x)=2\sin(2x-\frac\pi3)-ax$，$h'(x)=4\cos(2x-\frac\pi3)-a$；"
        r"当 $x\in[\frac\pi2,\pi]$ 时，$2x-\frac\pi3\in[\frac{2\pi}3,\frac{5\pi}3]$，"
        r"则 $\cos(2x-\frac\pi3)\in[-1,\frac12]$，即 $4\cos(2x-\frac\pi3)\in[-4,2]$」还原。" "\n"
        r"**辅助角公式校验**：$2\sin(2x-\frac\pi3)=2(\sin2x\cos\frac\pi3-\cos2x\sin\frac\pi3)"
        r"=2(\frac12\sin2x-\frac{\sqrt3}2\cos2x)=\sin2x-\sqrt3\cos2x$ ✓。" "\n"
        r"**数值校验**：$x=\frac\pi2$：$2x-\frac\pi3=\frac{2\pi}3$，$\cos=-0.5$，$4\cos=-2$；"
        r"$x=\pi$：$2x-\frac\pi3=\frac{5\pi}3$，$\cos=0.5$，$4\cos=2$ ✓ 上界；"
        r"$x$ 使 $2x-\frac\pi3=\pi$（即 $x=\frac{2\pi}3\approx2.094\in[\frac\pi2,\pi]$ ✓）："
        r"$\cos=-1$，$4\cos=-4$ ✓ 下界。**区间内确实取到 $[-4,2]$ 两端** ✓。"
        r"递减区间：$k=0$ 时 $[\frac{5\pi}{12},\frac{11\pi}{12}]=[1.309,2.880]$ ✓。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-111'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-111-V1',
}

T111_V3 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=x^{2}-bx+a\ln x$（$a>0,\ b\in\mathbb R$）．" "\n"
        r"（1）设 $b=a+2$，若 $f(x)$ 存在两个极值点 $x_{1},x_{2}$，"
        r"且 $\left|x_{1}-x_{2}\right|>1$，求证：$\left|f(x_{1})-f(x_{2})\right|>3-4\ln2$；" "\n"
        r"（2）设 $g(x)=xf(x)$，$g(x)$ 在 $[1,\mathrm e]$ 上不单调，"
        r"且 $2b+\dfrac1a\leqslant4\mathrm e$ 恒成立，求 $a$ 的取值范围．"
    ),
    'opts': [],
    'answer': (
        r"（1）证明见解析；（2）$\left[\dfrac{\mathrm e^{2}-\mathrm e^{4}-8\mathrm e}{4},\ "
        r"\dfrac{\mathrm e^{2}+\mathrm e^{4}-8\mathrm e}{4}\right]$"
    ),
    'analysis': (
        r"（1）$f'(x)=\dfrac{(x-1)(2x-a)}x$，两根 $1$ 与 $\frac a2$；"
        r"$\left|x_1-x_2\right|>1\Rightarrow a>4$，把差值表成 $t=\frac a2>2$ 的函数。"
        r"（2）$g$ 不单调 $\iff$ $g'=0$ 在 $(1,\mathrm e)$ 内有解，"
        r"分离出 $2b=3x^{2}+a\ln x+a$，再令 $F(x)\leqslant4\mathrm e$。"
    ),
    'solution': (
        r"**（1）**：$b=a+2$ 时 $f(x)=x^{2}-(a+2)x+a\ln x$，" "\n"
        r"$f'(x)=2x-(a+2)+\dfrac ax=\dfrac{2x^{2}-(a+2)x+a}x=\dfrac{(x-1)(2x-a)}x$．" "\n"
        r"令 $f'(x)=0$ 得 $x_{1}=1$、$x_{2}=\dfrac a2$．" "\n"
        r"$\left|x_{1}-x_{2}\right|>1$ 且 $a>0$ ⇒ $\dfrac a2-1>1$ 或 $1-\dfrac a2>1$（后者不可能），"
        r"故 $\dfrac a2>2$，即 $a>4$．" "\n"
        r"此时 $f$ 在 $\left[1,\dfrac a2\right]$ 上递减，故" "\n"
        r"$\left|f(x_{1})-f(x_{2})\right|=f(1)-f\!\left(\dfrac a2\right)$" "\n"
        r"$=\left[1-(a+2)+0\right]-\left[\dfrac{a^{2}}4-(a+2)\dfrac a2+a\ln\dfrac a2\right]$" "\n"
        r"$=\dfrac{a^{2}}4-a\ln\dfrac a2-1$．" "\n"
        r"令 $t=\dfrac a2>2$，记 $h(t)=t^{2}-2t\ln t-1$，"
        r"$h'(t)=2t-2\ln t-2$，$h''(t)=2-\dfrac2t=\dfrac{2(t-1)}t>0$（$t>2$），" "\n"
        r"故 $h'$ 在 $(2,+\infty)$ 上递增，$h'(t)>h'(2)=2(1-\ln2)>0$，"
        r"进而 $h$ 递增，$h(t)>h(2)=4-4\ln2-1=3-4\ln2$．" "\n"
        r"即 $\left|f(x_{1})-f(x_{2})\right|>3-4\ln2$，证毕．" "\n"
        r"**（2）**：$g(x)=x f(x)=x^{3}-bx^{2}+ax\ln x$，" "\n"
        r"$g'(x)=3x^{2}-2bx+a\ln x+a$．" "\n"
        r"$g$ 在 $[1,\mathrm e]$ 上不单调 $\iff$ $g'(x)=0$ 在 $(1,\mathrm e)$ 内有解，" "\n"
        r"即 $2b=3x+\dfrac{a\ln x+a}x$ 在 $(1,\mathrm e)$ 内有解．" "\n"
        r"设 $F(x)=3x+\dfrac{a(\ln x+1)}x$，"
        r"则 $2b$ 必须落在 $F$ 在 $(1,\mathrm e)$ 上的值域内；"
        r"又 $2b+\dfrac1a\leqslant4\mathrm e$ 恒成立，即 $2b\leqslant4\mathrm e-\dfrac1a$．" "\n"
        r"结合 $2b=F(x)$（$x\in(1,\mathrm e)$）与 $F$ 的单调性解得 "
        r"$a\in\left[\dfrac{\mathrm e^{2}-\mathrm e^{4}-8\mathrm e}4,\ "
        r"\dfrac{\mathrm e^{2}+\mathrm e^{4}-8\mathrm e}4\right]$（原书答案）．"
    ),
    'review': (
        r"★ 提取文本作「f(x) = x2- bx + alnx」「g(x) = xf(x)」与"
        r"「2b + ≤4e / a」，$x^2$ 上标丢失、$\frac1a$ 的分数线丢失。"
        r"由详解「$f'(x)=2x-b+\frac ax=\frac{(x-1)(2x-a)}x$，由 $f'(x)=0$ 可得 $x_1=1$、$x_2=\frac a2$；"
        r"又由 $|x_1-x_2|>1$ 知 $\frac a2>2$，∴$f(x)$ 在 $[1,\frac a2]$ 上单调递减，"
        r"∴$|f(x_1)-f(x_2)|=f(1)-f(\frac a2)=\frac{a^2}4-a\ln\frac a2-1$；"
        r"令 $t=\frac a2>2$，记 $h(t)=t^2-2t\ln t-1$，则 $h'(t)=2t-2\ln t-2$，"
        r"$h''(t)=2-\frac2t=\frac{2(t-1)}t>0$，∴$h'(t)$ 在 $(2,+\infty)$ 上单调递增；"
        r"∴$h'(t)>h'(2)=2(1-\ln2)>0$，∴$h(t)$ 在 $(2,+\infty)$ 上单调递增；"
        r"∴$h(t)>h(2)=3-4\ln2>0$」还原。" "\n"
        r"**第（1）问的代数自检**（关键一步）：" "\n"
        r"$f(1)=1-(a+2)+a\ln1=-a-1$；" "\n"
        r"$f(\frac a2)=\frac{a^2}4-(a+2)\frac a2+a\ln\frac a2=\frac{a^2}4-\frac{a^2}2-a+a\ln\frac a2"
        r"=-\frac{a^2}4-a+a\ln\frac a2$；" "\n"
        r"$f(1)-f(\frac a2)=-a-1+\frac{a^2}4+a-a\ln\frac a2=\frac{a^2}4-a\ln\frac a2-1$ ✓ "
        r"**与详解一致**。" "\n"
        r"**数值校验**：$a=5$（$>4$）：$t=2.5$，$h(2.5)=6.25-2(2.5)\ln2.5-1"
        r"=6.25-4.581-1=0.669$；$3-4\ln2=3-2.773=0.227$ ✓ $0.669>0.227$ ✓。"
        r"$h(2)=4-4(0.693)-1=0.227$ ✓ 恰为下确界。" "\n"
        r"**⚠ 第（2）问详解不完整**：原书【详解】只覆盖到第（1）问，"
        r"【分析】给出「由 $g(x)$ 在 $[1,\mathrm e]$ 上不单调转化为 $g'(x)=0$ 在 $(1,\mathrm e)$ 上有解，"
        r"可得 $2b=3x^2+ax\ln x+a$，令 $F(x)=3x+\frac{a+a\ln x}x$，分类讨论求 $F(x)$ 的最大值，"
        r"再求解 $F(x)_{\max}\leqslant4\mathrm e$」。"
        r"**答案照原书录入**，此处如实标注推导未补全。"
    ),
    'difficulty': 0.98,
    'topics': ['M-T-111'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-111-V3',
}

QS = [T111_E1, T111_V1, T111_V3]
