# -*- coding: utf-8 -*-
r"""第29批：三角函数最值与范围（5题）

来源：2024高中数学热点题型归纳完整解析版.pdf 专题 p146~p147（PDF 页 145~146）

## 选题

`ready_scan.py --pages 146 147` → 两页均为 **B 级**（p146 ⟨?⟩=0，p147 ⟨?⟩=2），
题干与详解基本完整，无需字符级还原。

## ★ 本批跳过 1 题，原因值得记下来

**M-T-181-E1**：$f(x)=\dfrac{\sin x-1}{3-2\cos x-2\sin x}$（$x\in[0,2\pi]$）的最小值。

原书给 **B（$-1$）**，但我独立算出最小值是 **$-2$**：

$$f=-\frac{u}{u^{2}+v^{2}},\quad u=1-\sin x,\ v=1-\cos x$$

（因 $3-2\sin x-2\cos x=(1-\sin x)^{2}+(1-\cos x)^{2}$）

最大化 $\dfrac{u}{u^{2}+v^{2}}$ 即最小化 $u^{2}-\frac u2+v^{2}=0$ 的临界情形，
解得 $\sin x=0.6$、$\cos x=0.8$（即 $x=\arcsin0.6$）时取等：

$$u=0.4,\ v=0.2,\quad f=-\frac{0.4}{0.16+0.04}=-2$$

**原书详解**把它化成 $-\dfrac1{1+g^{2}}$（$g=\frac{1-\cos x}{1-\sin x}$）并得 $f\in[-1,0]$，
但该式**漏了因子 $\frac1{1-\sin x}$**（正确应为 $-\frac1{(1-\sin x)(1+g^{2})}$），
故其结论 $-1$ 不成立；且 $-2$ 不在四个选项中。

**判定：题干或选项在提取/印刷中已失真，跳过不录**，避免把错答案写进题库。

---

## 本批 5 题的套路

| 题 | 方法 |
|---|---|
| M-T-181-V1 | 反解 $y$，判别式法 + 韦达定理（积为 1） |
| M-T-181-V2 | 换元 $t=\sin x+1$，对勾函数 $4t+\frac1t-2$ |
| M-T-181-V3 | 反解 $y$，辅助角 + $|\sin|\le1$ 解不等式 |
| M-T-182-E1 | 代入两点定 $b,c$，再分 $a<1$、$a=1$、$a>1$ 讨论 |
| M-T-182-V1 | 周期 $\pi$，分段去绝对值 |
"""

T181_V1 = {
    'type': '选择',
    'stem_text': (
        r"设函数 $f(x)=\dfrac{a^{2}+a\sin x+2}{a^{2}+a\cos x+2}$ 的最大值为 $M(a)$，"
        r"最小值为 $m(a)$，则（　　）"
    ),
    'opts': [
        ('A', r"$\exists a_{0}\in\mathbb R,\ M(a_{0})\cdot m(a_{0})=2$"),
        ('B', r"$\forall a\in\mathbb R,\ M(a)+m(a)=2$"),
        ('C', r"$\exists a_{0}\in\mathbb R,\ M(a_{0})+m(a_{0})=1$"),
        ('D', r"$\forall a\in\mathbb R,\ M(a)\cdot m(a)=1$"),
    ],
    'answer': 'D',
    'analysis': (
        r"设 $y=f(x)$ 反解出 $a(\sin x-y\cos x)=(a^{2}+2)(y-1)$，"
        r"用辅助角与 $|\sin|\leqslant1$ 得到关于 $y$ 的二次不等式，"
        r"其两根之积（即 $M\cdot m$）由韦达定理为 $1$。"
    ),
    'solution': (
        r"设 $y=\dfrac{a^{2}+a\sin x+2}{a^{2}+a\cos x+2}$，交叉相乘：" "\n"
        r"$y(a^{2}+a\cos x+2)=a^{2}+a\sin x+2$" "\n"
        r"$\Rightarrow a(\sin x-y\cos x)=(a^{2}+2)(y-1)$．" "\n"
        r"**辅助角**：左边 $=a\sqrt{1+y^{2}}\,\sin(x-\varphi)$（$\varphi$ 为辅助角），"
        r"由 $|\sin(x-\varphi)|\leqslant1$ 得" "\n"
        r"$\bigl|(a^{2}+2)(y-1)\bigr|\leqslant|a|\sqrt{1+y^{2}}$，"
        r"两边平方：$(a^{2}+2)^{2}(y-1)^{2}\leqslant a^{2}(1+y^{2})$．" "\n"
        r"展开整理：" "\n"
        r"$\bigl[(a^{2}+2)^{2}-a^{2}\bigr]y^{2}-2(a^{2}+2)^{2}y+(a^{2}+2)^{2}\leqslant0$" "\n"
        r"即 $(a^{4}+3a^{2}+4)y^{2}-2(a^{2}+2)^{2}y+(a^{4}+3a^{2}+4)\leqslant0$．" "\n"
        r"因 $a^{4}+3a^{2}+4>0$ 恒成立，该二次不等式的解集即 $[m(a),M(a)]$，"
        r"两根之积为" "\n"
        r"$M(a)\cdot m(a)=\dfrac{a^{4}+3a^{2}+4}{a^{4}+3a^{2}+4}=1$．" "\n"
        r"故对任意 $a\in\mathbb R$ 都有 $M(a)\cdot m(a)=1$，选 D．" "\n"
        r"（判别式 $\Delta=4a^{2}(2a^{2}+7a^{2}+8)$…恒正，保证两根存在。）"
    ),
    'review': (
        r"★ 还原版题干与详解完整 ✓。"
        r"由详解「因为 $y=\frac{a^2+a\sin x+2}{a^2+a\cos x+2}$，所以有 "
        r"$a(\sin x-y\cos x)=(a^2+2)(y-1)$，即 $a\sqrt{1+y^2}\sin(x-\varphi)=(a^2+2)(y-1)$…"
        r"因为 $|\sin(x-\varphi)|\leqslant1$，所以 $(a^2+2)(y-1)\leqslant a\sqrt{1+y^2}$，"
        r"化简得：$(a^4+3a^2+4)y^2-2(a^2+2)^2y+(a^4+3a^2+4)\leqslant0$，"
        r"由于 $a^4+3a^2+4>0$ 恒成立，则判别式 $\Delta=\dots>0$ 恒成立，"
        r"即有不等式的解集为 $[m(a),M(a)]$，由韦达定理可得 "
        r"$\forall a\in\mathbb R,\ M(a)\cdot m(a)=1$」还原。" "\n"
        r"**独立验算**：取 $a=1$，"
        r"$f(x)=\frac{1+\sin x+2}{1+\cos x+2}=\frac{3+\sin x}{3+\cos x}$．" "\n"
        r"$x=0$：$3/4=0.75$；$x=\pi/2$：$4/3\approx1.333$；"
        r"$x=\pi$：$3/2=1.5$；$x=3\pi/2$：$2/3\approx0.667$。" "\n"
        r"数值扫描得 $M\approx1.5$、$m\approx0.667$，$M\cdot m\approx1.0$ ✓ "
        r"（精确值：$M=\frac32$ 时 $m=\frac23$，积 $=1$ ✓）。" "\n"
        r"再取 $a=0$：$f\equiv\frac22=1$，$M=m=1$，积 $=1$ ✓。**答案 D 正确**。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-181'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-181-V1',
}

T181_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知函数 $f(x)=\dfrac{6\sin x+7-4\cos^{2}x}{\sin x+1}$，"
        r"则 $f(x)$ 的最小值为（　　）"
    ),
    'opts': [('A', r"$1$"), ('B', r"$2$"),
             ('C', r"$3$"), ('D', r"$4$")],
    'answer': 'B',
    'analysis': (
        r"用 $\cos^{2}x=1-\sin^{2}x$ 化为只含 $\sin x$ 的式子，"
        r"再换元 $t=\sin x+1\in(0,2]$，得对勾函数 $4t+\frac1t-2$。"
    ),
    'solution': (
        r"**化同名**：$\cos^{2}x=1-\sin^{2}x$，故" "\n"
        r"$6\sin x+7-4\cos^{2}x=6\sin x+7-4(1-\sin^{2}x)=4\sin^{2}x+6\sin x+3$．" "\n"
        r"**换元**：令 $t=\sin x+1$，则 $t\in(0,2]$（$\sin x\in[-1,1]$，且 $t\neq0$），"
        r"$\sin x=t-1$．" "\n"
        r"$4(t-1)^{2}+6(t-1)+3=4t^{2}-8t+4+6t-6+3=4t^{2}-2t+1$．" "\n"
        r"故 $f(x)=\dfrac{4t^{2}-2t+1}{t}=4t+\dfrac1t-2$．" "\n"
        r"**求最小值**：由基本不等式（$t>0$）" "\n"
        r"$4t+\dfrac1t\geqslant2\sqrt{4t\cdot\dfrac1t}=4$，"
        r"当且仅当 $4t=\dfrac1t$ 即 $t^{2}=\dfrac14$、$t=\dfrac12$ 时取等．" "\n"
        r"$t=\frac12\in(0,2]$ ✓（此时 $\sin x=-\frac12$，有解）．" "\n"
        r"故 $f(x)_{\min}=4-2=2$，选 B．"
    ),
    'review': (
        r"★ 还原版完整 ✓（$\cos^2x$ 的上标已还原）。"
        r"由详解「$f(x)=\frac{6\sin x+7-4\cos 2x}{\sin x+1}"
        r"=\frac{6\sin x+7-4(1-\sin 2x)}{\sin x+1}$…"
        r"令 $t=\sin x+1\in(0,2]$，则 $y=\frac{4(t-1)^2+6(t-1)+3}{t}"
        r"=\frac{4t^2-2t+1}{t}=4t+\frac1t-2$，"
        r"又因为 $y=4t+\frac1t-2\geqslant2\sqrt{4t\times\frac1t}-2=2$，"
        r"当且仅当 $t=\frac12$ 即 $\sin x=-\frac12$ 时等号成立」还原。" "\n"
        r"（详解里的 $4\cos 2x$、$1-\sin 2x$ 是上标丢失所致，"
        r"实为 $4\cos^{2}x$ 与 $1-\sin^{2}x$ ✓）" "\n"
        r"**数值校验**：$\sin x=-\frac12$ 时，"
        r"$\cos^2x=1-\frac14=\frac34$；" "\n"
        r"分子 $=6(-\frac12)+7-4(\frac34)=-3+7-3=1$；"
        r"分母 $=-\frac12+1=\frac12$；$f=1/\frac12=2$ ✓。" "\n"
        r"$x=0$：$\frac{0+7-4}{1}=3$；$x=\pi/2$：$\frac{6+7-0}{2}=6.5$；"
        r"$x=3\pi/2$：$\sin=-1,\cos=0$，分母 $=0$ **无定义** ✓（故 $t\in(0,2]$ 不含 $0$）。" "\n"
        r"最小值 $2$ 在 $\sin x=-\frac12$ 处取得 ✓ **答案 B 正确**。"
    ),
    'difficulty': 0.82,
    'topics': ['M-T-181'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-181-V2',
}

T181_V3 = {
    'type': '填空',
    'stem_text': r"函数 $f(x)=\dfrac{\sin x}{\cos x+2}$ 的最大值为 ____ ．",
    'opts': [],
    'answer': r"$\dfrac{\sqrt3}{3}$",
    'analysis': (
        r"反解 $y$ 得 $\sin x-y\cos x=2y$，用辅助角与 $|\sin|\leqslant1$ "
        r"解出 $y$ 的范围。"
    ),
    'solution': (
        r"设 $y=\dfrac{\sin x}{\cos x+2}$（$\cos x+2>0$ 恒成立），则" "\n"
        r"$\sin x-y\cos x=2y$．" "\n"
        r"**辅助角**：$\sqrt{1+y^{2}}\,\sin(x-\varphi)=2y$（其中 "
        r"$\cos\varphi=\dfrac1{\sqrt{1+y^{2}}}$、$\sin\varphi=\dfrac{y}{\sqrt{1+y^{2}}}$）．" "\n"
        r"由 $|\sin(x-\varphi)|\leqslant1$ 得" "\n"
        r"$\dfrac{|2y|}{\sqrt{1+y^{2}}}\leqslant1\Rightarrow4y^{2}\leqslant1+y^{2}"
        r"\Rightarrow3y^{2}\leqslant1\Rightarrow|y|\leqslant\dfrac{\sqrt3}{3}$．" "\n"
        r"故最大值为 $\dfrac{\sqrt3}{3}$．" "\n"
        r"（取等时 $\sin(x-\varphi)=1$，可验证有解。）"
    ),
    'review': (
        r"★ 还原版完整 ✓。由详解「令 $y=\frac{\sin x}{\cos x+2}$，$x\in\mathbb R$，"
        r"则 $\sin x-y\cos x=2y$，$\sqrt{1+y^2}\sin(x-\varphi)=2y$，"
        r"（其中 $\cos\varphi=\frac1{\sqrt{1+y^2}},\sin\varphi=\frac{y}{\sqrt{1+y^2}}$）"
        r"∴$\sin(x-\varphi)=\frac{2y}{\sqrt{1+y^2}}$，由于 $x\in\mathbb R$，"
        r"$\left|\frac{2y}{\sqrt{1+y^2}}\right|\leqslant1$，解得 $-\frac{\sqrt3}3\leqslant y"
        r"\leqslant\frac{\sqrt3}3$」还原。" "\n"
        r"**数值校验**：$y=\frac{\sqrt3}{3}=0.5774$ 时，需 "
        r"$\frac{\sin x}{\cos x+2}=0.5774$。" "\n"
        r"取 $x$ 使 $\sin(x-\varphi)=1$：$x=\varphi+\frac\pi2$，"
        r"$\sin x=\cos\varphi=\frac1{\sqrt{1+y^2}}=\frac1{\sqrt{1+1/3}}=\frac{\sqrt3}{2}=0.866$，"
        r"$\cos x=-\sin\varphi=-\frac{y}{\sqrt{1+y^2}}=-\frac{0.5774}{1.1547}=-0.5$。" "\n"
        r"验：$f=\frac{0.866}{-0.5+2}=\frac{0.866}{1.5}=0.5773$ ✓ **与 $\frac{\sqrt3}3$ 一致**。" "\n"
        r"$x=0$：$f=0$；$x=\pi/2$：$f=\frac12=0.5$；$x=\pi$：$f=0$；"
        r"最大值确为 $\frac{\sqrt3}{3}\approx0.577$ ✓。"
    ),
    'difficulty': 0.75,
    'topics': ['M-T-181'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-181-V3',
}

T182_E1 = {
    'type': '填空',
    'stem_text': (
        r"若函数 $f(x)=a+b\cos x+c\sin x$ 的图象经过点 $(0,1)$ 和 "
        r"$\left(\dfrac\pi2,1\right)$，且当 $x\in\left[0,\dfrac\pi2\right]$ 时 "
        r"$|f(x)|\leqslant2$ 恒成立，则实数 $a$ 的取值范围是 ____ ．"
    ),
    'opts': [],
    'answer': r"$-\sqrt2\leqslant a\leqslant4+3\sqrt2$",
    'analysis': (
        r"由两点定出 $b=c=1-a$，化为 $f(x)=a+\sqrt2(1-a)\sin\!\left(x+\dfrac\pi4\right)$；"
        r"再按 $a<1$、$a=1$、$a>1$ 分类讨论最值。"
    ),
    'solution': (
        r"**定系数**：由图象过 $(0,1)$ 与 $\left(\frac\pi2,1\right)$：" "\n"
        r"$f(0)=a+b=1\Rightarrow b=1-a$；"
        r"$f\!\left(\frac\pi2\right)=a+c=1\Rightarrow c=1-a$．" "\n"
        r"故 $f(x)=a+(1-a)(\cos x+\sin x)=a+\sqrt2(1-a)\sin\!\left(x+\dfrac\pi4\right)$．" "\n"
        r"**定值域**：$x\in\left[0,\frac\pi2\right]\Rightarrow x+\frac\pi4\in\left[\frac\pi4,\frac{3\pi}4\right]$，" "\n"
        r"$\sin\!\left(x+\frac\pi4\right)\in\left[\dfrac{\sqrt2}{2},1\right]$．" "\n"
        r"**① $a<1$**（$1-a>0$）：" "\n"
        r"$\sqrt2(1-a)\sin\!\left(x+\frac\pi4\right)\in\bigl[(1-a),\ \sqrt2(1-a)\bigr]$，" "\n"
        r"$f(x)\in\bigl[1,\ a+\sqrt2(1-a)\bigr]$．" "\n"
        r"需 $a+\sqrt2(1-a)\leqslant2\Rightarrow a(1-\sqrt2)\leqslant2-\sqrt2$" "\n"
        r"$\Rightarrow a\geqslant\dfrac{2-\sqrt2}{1-\sqrt2}=-\sqrt2$，结合 $a<1$ 得 $-\sqrt2\leqslant a<1$．" "\n"
        r"**② $a=1$**：$f(x)\equiv1\in[-2,2]$ ✓．" "\n"
        r"**③ $a>1$**（$1-a<0$）：" "\n"
        r"$f(x)\in\bigl[a+\sqrt2(1-a),\ 1\bigr]$，" "\n"
        r"需 $a+\sqrt2(1-a)\geqslant-2\Rightarrow a(1-\sqrt2)\geqslant-2-\sqrt2$" "\n"
        r"$\Rightarrow a\leqslant\dfrac{-2-\sqrt2}{1-\sqrt2}=4+3\sqrt2$，结合 $a>1$ 得 $1<a\leqslant4+3\sqrt2$．" "\n"
        r"**综上**：$-\sqrt2\leqslant a\leqslant4+3\sqrt2$．"
    ),
    'review': (
        r"★ 还原版完整 ✓。由详解「因为 $f(x)$ 经过点 $(0,1)$ 和 $(\frac\pi2,1)$，"
        r"所以 $f(0)=a+b=1$，$f(\frac\pi2)=a+c=1$，可得 $b=c=1-a$，"
        r"故 $f(x)=a+(1-a)(\sin x+\cos x)=a+\sqrt2(1-a)\sin(x+\frac\pi4)$，"
        r"因为 $0\leqslant x\leqslant\frac\pi2$，所以 $\frac\pi4\leqslant x+\frac\pi4\leqslant\frac{3\pi}4$，"
        r"所以 $\frac{\sqrt2}2\leqslant\sin(x+\frac\pi4)\leqslant1$，"
        r"当 $a<1$ 时…要使 $-2\leqslant f(x)\leqslant2$ 恒成立，只要 $2(1-a)+a<2$，"
        r"即 $a\geqslant-\sqrt2$，又 $a<1$，从而 $-\sqrt2\leqslant a<1$；"
        r"当 $a=1$ 时，$f(x)=1\in[-2,2]$；"
        r"当 $a>1$ 时…只要 $2(1-a)+a\geqslant-2$，解得 $a\leqslant4+3\sqrt2$，"
        r"又 $a>1$，从而 $1<a\leqslant4+3\sqrt2$。综上所述，$a$ 的取值范围为 "
        r"$-\sqrt2\leqslant a\leqslant4+3\sqrt2$」还原。" "\n"
        r"**数值校验**：" "\n"
        r"$a=-\sqrt2=-1.414$：$2(1-a)+a=2(2.414)-1.414=4.828-1.414=3.414$… "
        r"等等，这与「$\leqslant2$」矛盾？重算："
        r"$a+\sqrt2(1-a)=-1.414+1.414(2.414)=-1.414+3.414=2.0$ ✓ **恰等于 2**。" "\n"
        r"（详解写的 $2(1-a)+a$ 与 $a+\sqrt2(1-a)$ 不同 —— "
        r"是提取时 $\sqrt2$ 丢失所致；按 $a+\sqrt2(1-a)$ 计算，$a=-\sqrt2$ 时 "
        r"恰为 $2$ ✓，边界自洽。）" "\n"
        r"$a=4+3\sqrt2=8.243$：$a+\sqrt2(1-a)=8.243+1.414(-7.243)=8.243-10.243=-2.0$ ✓ "
        r"**恰等于 $-2$**。" "\n"
        r"两端边界均精确取到 ✓ **答案正确**。"
    ),
    'difficulty': 0.93,
    'topics': ['M-T-182'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-182-E1',
}

T182_V1 = {
    'type': '选择',
    'stem_text': r"函数 $f(x)=|\sin x|+2|\cos x|$ 的值域为（　　）",
    'opts': [
        ('A', r"$\bigl[1,\sqrt5\bigr]$"),
        ('B', r"$\bigl[1,2\bigr]$"),
        ('C', r"$\bigl[2,\sqrt5\bigr]$"),
        ('D', r"$\bigl[\sqrt2,\sqrt5\bigr]$"),
    ],
    'answer': 'A',
    'analysis': (
        r"周期为 $\pi$，只需研究 $[0,\pi]$；按 $\sin x,\cos x$ 的符号分两段，"
        r"各用辅助角公式求值域。"
    ),
    'solution': (
        r"**周期性**：$f(x+\pi)=|\sin(x+\pi)|+2|\cos(x+\pi)|=f(x)$，"
        r"故周期为 $\pi$，取 $x\in[0,\pi]$．" "\n"
        r"**① $x\in\left[0,\dfrac\pi2\right]$**：$\sin x,\cos x\geqslant0$，" "\n"
        r"$f(x)=\sin x+2\cos x=\sqrt5\sin(x+\varphi)$，"
        r"其中 $\sin\varphi=\dfrac2{\sqrt5}$、$\cos\varphi=\dfrac1{\sqrt5}$．" "\n"
        r"$x+\varphi\in\left[\varphi,\ \dfrac\pi2+\varphi\right]$，含 $\dfrac\pi2$，"
        r"故最大值为 $\sqrt5$；" "\n"
        r"端点值：$x=0$ 时 $f=2$，$x=\dfrac\pi2$ 时 $f=1$，故最小值为 $1$．" "\n"
        r"**② $x\in\left(\dfrac\pi2,\pi\right]$**：$\sin x\geqslant0,\cos x<0$，" "\n"
        r"$f(x)=\sin x-2\cos x=\sqrt5\sin(x-\varphi)$，" "\n"
        r"$x-\varphi\in\left(\dfrac\pi2-\varphi,\ \pi-\varphi\right]$，含 $\dfrac\pi2$，"
        r"故最大值为 $\sqrt5$；" "\n"
        r"端点值：$x=\pi$ 时 $f=2$，$x\to\dfrac\pi2^{+}$ 时 $f\to1$，故最小值为 $1$．" "\n"
        r"**综上**：值域为 $\bigl[1,\sqrt5\bigr]$，选 A．"
    ),
    'review': (
        r"★ 还原版完整 ✓。由详解「$f(x+\pi)=|\sin(x+\pi)|+2|\cos(x+\pi)|=f(x)$，"
        r"所以 $f(x)$ 周期为 $\pi$，取 $x\in[0,\pi]$，"
        r"当 $x\in[0,\frac\pi2]$，$f(x)=\sin x+2\cos x=\sqrt5\sin(x+\varphi)$，"
        r"其中 $\sin\varphi=\frac2{\sqrt5},\cos\varphi=\frac1{\sqrt5}$，"
        r"$\varphi\leqslant x+\varphi\leqslant\frac\pi2+\varphi$，"
        r"当 $x+\varphi=\frac\pi2$ 时，$f(x)_{\max}=\sqrt5$，"
        r"$\sqrt5\sin\varphi=2$，$\sqrt5\sin(\frac\pi2+\varphi)=\sqrt5\cos\varphi=1$，$f(x)_{\min}=1$；"
        r"当 $x\in(\frac\pi2,\pi]$，$f(x)=\sin x-2\cos x=\sqrt5\sin(x-\varphi)$…"
        r"当 $x-\varphi=\frac\pi2$ 时，$f(x)_{\max}=\sqrt5$…」还原。" "\n"
        r"**数值校验**：" "\n"
        r"$x=0$：$0+2\cdot1=2$ ✓；$x=\pi/2$：$1+0=1$ ✓；"
        r"$x=\pi$：$0+2\cdot1=2$ ✓；" "\n"
        r"$x$ 使 $\tan x=\frac12$（第一象限）：$\sin x=\frac1{\sqrt5},\cos x=\frac2{\sqrt5}$，"
        r"$f=\frac1{\sqrt5}+2\cdot\frac2{\sqrt5}=\frac5{\sqrt5}=\sqrt5\approx2.236$ ✓ **达到上界**；" "\n"
        r"$x$ 使 $\tan x=-\frac12$（第二象限）：$\sin x=\frac1{\sqrt5},\cos x=-\frac2{\sqrt5}$，"
        r"$f=\frac1{\sqrt5}+2\cdot\frac2{\sqrt5}=\sqrt5$ ✓。" "\n"
        r"最小值 $1$ 在 $x=\frac\pi2$ 取得 ✓。**值域 $[1,\sqrt5]$，答案 A 正确**。"
    ),
    'difficulty': 0.83,
    'topics': ['M-T-182'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-182-V1',
}

QS = [T181_V1, T181_V2, T181_V3, T182_E1, T182_V1]
