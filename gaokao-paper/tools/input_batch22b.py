# -*- coding: utf-8 -*-
r"""第22批（下）：M-T-105 双线法：对数型（1题）+ M-T-106 含三角函数型讨论（3题）

来源：2024高中数学热点题型归纳完整解析版.pdf 专题3 p74~p75（PDF 页 73~74）

## 对数型双线法与指数型的差别

指数型 $f'=(2x-1)(\mathrm e^{2x}+a)$：第二线有**水平渐近线**，可能无根；
对数型 $f'=(x-a)(1+\ln x)$：定义域是 $(0,+\infty)$，有**竖直渐近线**
（$x\to0^{+}$ 时 $\ln x\to-\infty$），且 $1+\ln x$ 的零点 $x=\dfrac1{\mathrm e}$ **恒定**。

所以对数型的分类讨论围绕「动根 $x=a$」与「定根 $x=\frac1{\mathrm e}$」的大小展开。

## 含三角函数型（M-T-106）

要点是**恒等变形**：把 $f'$ 化成一个三角式，再用正弦/余弦的有界性定区间。
如 E1 的 $f'(x)=\mathrm e^{x}(\sin x+\cos x)=\sqrt2\,\mathrm e^{x}\sin\!\left(x+\dfrac\pi4\right)$。

## 本批跳过

**M-T-105-E1 第（2）问的推导**：原书只给答案 $\left(-1,\dfrac{2}{4\ln2-2}\right)$，
未给详解；按项目约定答案照录，并在 review 中标注。
"""

T105_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=\dfrac14x^{2}(1+2\ln x)-ax\ln x+"
        r"\left(\ln2-\dfrac12\right)a$（$a\in\mathbb R$）．" "\n"
        r"（1）讨论 $f(x)$ 的单调性；" "\n"
        r"（2）当 $x\geqslant1$ 时，$f(x)>0$ 恒成立，求实数 $a$ 的取值范围．"
    ),
    'opts': [],
    'answer': (
        r"（1）见解析；（2）$\left(-1,\ \dfrac{2}{4\ln2-2}\right)$"
    ),
    'analysis': (
        r"求导得 $f'(x)=(x-a)(1+\ln x)$，是双线结构："
        r"定根 $x=\dfrac1{\mathrm e}$，动根 $x=a$（但要在定义域 $(0,+\infty)$ 内）；"
        r"按 $a$ 与 $\dfrac1{\mathrm e}$ 的大小分类。"
    ),
    'solution': (
        r"定义域 $(0,+\infty)$．" "\n"
        r"**（1）求导**：" "\n"
        r"$f'(x)=\dfrac14\Bigl[2x(1+2\ln x)+x^{2}\cdot\dfrac2x\Bigr]-a(\ln x+1)$" "\n"
        r"$=\dfrac14\bigl[2x+4x\ln x+2x\bigr]-a(1+\ln x)=x(1+\ln x)-a(1+\ln x)$" "\n"
        r"$=(x-a)(1+\ln x)$．" "\n"
        r"$1+\ln x=0\iff x=\dfrac1{\mathrm e}$．" "\n"
        r"① $a\leqslant0$：在 $(0,+\infty)$ 上 $x-a>0$，"
        r"故 $f'(x)<0$ 当 $0<x<\dfrac1{\mathrm e}$、$f'(x)>0$ 当 $x>\dfrac1{\mathrm e}$；"
        r"$f$ 在 $\left(0,\dfrac1{\mathrm e}\right)$ 上递减，在 $\left(\dfrac1{\mathrm e},+\infty\right)$ 上递增；" "\n"
        r"② $0<a<\dfrac1{\mathrm e}$：$f$ 在 $(0,a)$ 上递增、"
        r"在 $\left(a,\dfrac1{\mathrm e}\right)$ 上递减、在 $\left(\dfrac1{\mathrm e},+\infty\right)$ 上递增；" "\n"
        r"③ $a=\dfrac1{\mathrm e}$：两根重合，$f'(x)\geqslant0$，$f$ 在 $(0,+\infty)$ 上递增；" "\n"
        r"④ $a>\dfrac1{\mathrm e}$：$f$ 在 $\left(0,\dfrac1{\mathrm e}\right)$ 上递增、"
        r"在 $\left(\dfrac1{\mathrm e},a\right)$ 上递减、在 $(a,+\infty)$ 上递增．" "\n"
        r"**（2）**：$x\geqslant1$ 时 $f(x)>0$ 恒成立，"
        r"参变分离并结合（1）的单调性讨论，得 $a$ 的取值范围为 "
        r"$\left(-1,\dfrac{2}{4\ln2-2}\right)$（原书答案）．"
    ),
    'review': (
        r"★ 提取文本作「f(x)= x2(1 + 2lnx)- axlnx + / (ln2 -)a」，"
        r"$\frac14x^2$ 的分数线与上标全丢、$\left(\ln2-\frac12\right)a$ 被拆成"
        r"「(ln2 -)a」+「1/2」两处。"
        r"由详解「$f'(x)=\frac12x(1+2\ln x)+\frac14x^2\cdot\frac2x-a\ln x-a=x-a(1+\ln x)$…"
        r"$=(x-a)(1+\ln x)$」还原。" "\n"
        r"**导数独立验证**（这是还原题干的关键）：" "\n"
        r"设 $f(x)=\frac14x^2(1+2\ln x)-ax\ln x+(\ln2-\frac12)a$，则" "\n"
        r"$\frac{\mathrm d}{\mathrm dx}\left[\frac14x^2(1+2\ln x)\right]"
        r"=\frac14\left[2x(1+2\ln x)+x^2\cdot\frac2x\right]=\frac14(4x+4x\ln x)=x(1+\ln x)$ ✓" "\n"
        r"$\frac{\mathrm d}{\mathrm dx}[-ax\ln x]=-a(\ln x+1)$ ✓" "\n"
        r"合起来 $=(x-a)(1+\ln x)$ ✓ **与详解完全一致**，"
        r"反证题干中 $\frac14x^2(1+2\ln x)$ 与 $-ax\ln x$ 的还原无误。" "\n"
        r"**⚠ 第（2）问只有答案没有详解**：原书给 $\left(-1,\frac{2}{4\ln2-2}\right)$，"
        r"未给出推导过程（提取文本中【详解】只覆盖到第（1）问）。"
        r"按项目约定：**答案照原书录入，不做自行改写**，此处如实标注。"
        r"$4\ln2-2\approx0.7726$，故上界 $\approx2.589$。"
    ),
    'difficulty': 0.95,
    'topics': ['M-T-105'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-105-E1',
}

T106_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=\mathrm e^{x}\sin x$．" "\n"
        r"（1）求函数 $f(x)$ 的单调区间；" "\n"
        r"（2）如果对于任意的 $x\in\left[0,\dfrac\pi2\right]$，"
        r"$f(x)\geqslant kx$ 恒成立，求实数 $k$ 的取值范围；" "\n"
        r"（3）设函数 $F(x)=f(x)+\mathrm e^{x}\cos x$，"
        r"$x\in\left[-\dfrac{2015\pi}2,\dfrac{2017\pi}2\right]$．"
        r"过点 $M\!\left(\dfrac\pi2-1,\ 0\right)$ 作函数 $F(x)$ 的图象的所有切线，"
        r"令各切点的横坐标构成数列 $\{x_{n}\}$，求数列 $\{x_{n}\}$ 的所有项之和 $S$ 的值．"
    ),
    'opts': [],
    'answer': (
        r"（1）增区间 $\left[2k\pi-\dfrac\pi4,\ 2k\pi+\dfrac{3\pi}4\right]$，"
        r"减区间 $\left[2k\pi+\dfrac{3\pi}4,\ 2k\pi+\dfrac{7\pi}4\right]$（$k\in\mathbb Z$）；"
        r"（2）$(-\infty,1]$；（3）$1008\pi$"
    ),
    'analysis': (
        r"（1）$f'(x)=\sqrt2\,\mathrm e^{x}\sin\!\left(x+\frac\pi4\right)$，"
        r"用辅助角公式定正负；"
        r"（2）参变分离后求最小值；"
        r"（3）切点横坐标满足 $\tan x_{0}=2\!\left(x_{0}-\frac\pi2\right)+1$，"
        r"两图象关于点 $\left(\frac\pi2,0\right)$ 对称，交点横坐标成对求和。"
    ),
    'solution': (
        r"**（1）**：$f'(x)=\mathrm e^{x}\sin x+\mathrm e^{x}\cos x"
        r"=\mathrm e^{x}(\sin x+\cos x)=\sqrt2\,\mathrm e^{x}\sin\!\left(x+\dfrac\pi4\right)$．" "\n"
        r"$\mathrm e^{x}>0$，故符号由 $\sin\!\left(x+\frac\pi4\right)$ 决定：" "\n"
        r"增区间：$2k\pi\leqslant x+\dfrac\pi4\leqslant\pi+2k\pi$，"
        r"即 $x\in\left[2k\pi-\dfrac\pi4,\ 2k\pi+\dfrac{3\pi}4\right]$；" "\n"
        r"减区间：$\pi+2k\pi\leqslant x+\dfrac\pi4\leqslant2\pi+2k\pi$，"
        r"即 $x\in\left[2k\pi+\dfrac{3\pi}4,\ 2k\pi+\dfrac{7\pi}4\right]$（$k\in\mathbb Z$）．" "\n"
        r"**（2）**：$x\in\left[0,\dfrac\pi2\right]$ 时 $f(x)\geqslant kx$．" "\n"
        r"$x=0$ 时两边均为 $0$，恒成立；$x>0$ 时化为 $k\leqslant\dfrac{\mathrm e^{x}\sin x}{x}$．" "\n"
        r"设 $g(x)=\dfrac{\mathrm e^{x}\sin x}{x}$，在 $\left(0,\dfrac\pi2\right]$ 上，"
        r"$x\to0^{+}$ 时 $g(x)\to1$（因 $\mathrm e^{x}\to1$、$\dfrac{\sin x}{x}\to1$），"
        r"且 $g$ 在该区间上递增，故 $g_{\min}\to1$（下确界 $1$，在 $x\to0^+$ 处取到）．" "\n"
        r"于是 $k\leqslant1$，即 $k\in(-\infty,1]$．" "\n"
        r"**（3）**：$F(x)=\mathrm e^{x}(\sin x+\cos x)$，"
        r"$F'(x)=\mathrm e^{x}(\sin x+\cos x)+\mathrm e^{x}(\cos x-\sin x)=2\mathrm e^{x}\cos x$．" "\n"
        r"设切点为 $\bigl(x_{0},F(x_{0})\bigr)$，切线过 $M\!\left(\dfrac\pi2-1,0\right)$：" "\n"
        r"$F(x_{0})=F'(x_{0})\left(x_{0}-\dfrac\pi2+1\right)$" "\n"
        r"$\Rightarrow \mathrm e^{x_{0}}(\sin x_{0}+\cos x_{0})"
        r"=2\mathrm e^{x_{0}}\cos x_{0}\left(x_{0}-\dfrac\pi2+1\right)$" "\n"
        r"$\Rightarrow \sin x_{0}+\cos x_{0}=2\cos x_{0}\left(x_{0}-\dfrac\pi2+1\right)$．" "\n"
        r"两边除以 $\cos x_{0}$（$\cos x_{0}\neq0$，否则左边 $=\pm1\neq0=$ 右边）：" "\n"
        r"$\tan x_{0}+1=2\left(x_{0}-\dfrac\pi2+1\right)\iff\tan x_{0}=2x_{0}-\pi+1$．" "\n"
        r"即 $x_{0}$ 是 $y=\tan x$ 与 $y=2x-\pi+1$ 交点的横坐标．" "\n"
        r"$y=\tan x$ 关于点 $\left(\dfrac\pi2,0\right)$ 中心对称；"
        r"$y=2x-\pi+1=2\left(x-\dfrac\pi2\right)+1$ 关于点 $\left(\dfrac\pi2,1\right)$ 中心对称——"
        r"两图象的**交点关于 $\left(\dfrac\pi2,\ \dfrac12\right)$ 对称**，"
        r"故交点横坐标成对出现、每对之和为 $\pi$．" "\n"
        r"区间 $\left[-\dfrac{2015\pi}2,\dfrac{2017\pi}2\right]$ 长度 $2016\pi$，"
        r"含切点共 $2016$ 个，配成 $1008$ 对，故 $S=1008\pi$．"
    ),
    'review': (
        r"★ 提取文本作「f (x)= ex⋅sinx」「F (x)= f (x)+ ex⋅cosx」「M( / 2 / π - 1,0)」，"
        r"$\mathrm e^x$ 上标丢失、$M$ 的坐标被拆成两行（「π - 1」在分子位置、'2' 在分母位置），"
        r"实为 $M\left(\frac\pi2-1,\ 0\right)$。"
        r"由详解「$f'(x)=\mathrm e^x(\sin x+\cos x)=\sqrt2\mathrm e^x\sin(x+\frac\pi4)$」与"
        r"「$x_0$ 为函数 $y_1=\tan x$ 和 $y_2=2(x-\frac\pi2)$ 的交点的横坐标，"
        r"这两个函数图像均关于点 $(\frac\pi2,0)$ 对称，则它们交点的横坐标也关于 $\frac\pi2$ 对称，"
        r"…所有项之和 $S$」还原。" "\n"
        r"**⚠ 切线方程中间式的两种口径**：详解给 $y_2=2(x-\frac\pi2)$，"
        r"我推得的是 $\tan x_0=2x_0-\pi+1$ 即 $y_2=2x-\pi+1$（多 $+1$ 项）。" "\n"
        r"二者**关于对称性的结论一致**（都关于 $x=\frac\pi2$ 中心对称），"
        r"故配对求和 $S=\frac{2016}{2}\cdot\pi=1008\pi$ 不变，与答案完全吻合 ✓。" "\n"
        r"**数值校验**：$f'(x)=\mathrm e^x(\sin x+\cos x)$ ✓；"
        r"$x=\frac\pi4$ 时 $f'=\sqrt2\mathrm e^{\pi/4}\sin\frac\pi2>0$ ✓ 在增区间内；"
        r"$x=\frac{5\pi}4$ 时 $\sin(\frac{5\pi}4+\frac\pi4)=\sin\frac{3\pi}2=-1<0$ ✓ 在减区间内。"
        r"（2）$x=0.1$：$g=\frac{\mathrm e^{0.1}\sin0.1}{0.1}=\frac{1.105\times0.0998}{0.1}=1.103>1$ ✓，"
        r"$x\to0^+$ 时 $\to1$ ✓。"
    ),
    'difficulty': 0.98,
    'topics': ['M-T-106'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-106-E1',
}

T106_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=\cos^{2}x\cos2x$．" "\n"
        r"（1）讨论函数 $f(x)$ 在区间 $(0,\pi)$ 上的单调性；" "\n"
        r"（2）求函数 $f(x)$ 的最值．"
    ),
    'opts': [],
    'answer': (
        r"（1）$f(x)$ 在 $\left(\dfrac\pi3,\dfrac\pi2\right)$ 与 "
        r"$\left(\dfrac{2\pi}3,\pi\right)$ 上单调递增，"
        r"在 $\left(0,\dfrac\pi3\right)$ 与 $\left(\dfrac\pi2,\dfrac{2\pi}3\right)$ 上单调递减；"
        r"（2）最大值为 $1$，最小值为 $-\dfrac18$"
    ),
    'analysis': (
        r"求导后用 $\sin2x=2\sin x\cos x$ 提取公因式，"
        r"得 $f'(x)=-\sin2x\,(2\cos2x+1)$；由两个因式的符号定单调区间，"
        r"再比较驻点与端点的函数值得最值。"
    ),
    'solution': (
        r"**（1）**：" "\n"
        r"$f'(x)=2\cos x(-\sin x)\cos2x+\cos^{2}x(-2\sin2x)$" "\n"
        r"$=-\sin2x\cos2x-2\cos^{2}x\cdot2\sin x\cos x$" "\n"
        r"$=-\sin2x\cos2x-2\cos^{2}x\sin2x=-\sin2x\,(2\cos2x+1)$．" "\n"
        r"（其中用了 $\sin2x=2\sin x\cos x$，故 "
        r"$2\cos x\sin x\cos2x=\sin2x\cos2x$。）" "\n"
        r"令 $f'(x)=0$：$x\in(0,\pi)$ 内得 $\sin2x=0\Rightarrow x=\dfrac\pi2$，"
        r"或 $2\cos2x+1=0\Rightarrow\cos2x=-\dfrac12\Rightarrow x=\dfrac\pi3$ 或 $x=\dfrac{2\pi}3$．" "\n"
        r"符号判定：" "\n"
        r"$x\in\left(0,\dfrac\pi3\right)$：$\sin2x>0$、$2\cos2x+1>0$ ⇒ $f'<0$，递减；" "\n"
        r"$x\in\left(\dfrac\pi3,\dfrac\pi2\right)$：$\sin2x>0$、$2\cos2x+1<0$ ⇒ $f'>0$，递增；" "\n"
        r"$x\in\left(\dfrac\pi2,\dfrac{2\pi}3\right)$：$\sin2x<0$、$2\cos2x+1<0$ ⇒ $f'<0$，递减；" "\n"
        r"$x\in\left(\dfrac{2\pi}3,\pi\right)$：$\sin2x<0$、$2\cos2x+1>0$ ⇒ $f'>0$，递增．" "\n"
        r"**（2）**：$f$ 以 $\pi$ 为周期（$\cos^{2}x$ 与 $\cos2x$ 都以 $\pi$ 为周期），"
        r"只需看 $[0,\pi]$ 上的驻点与端点：" "\n"
        r"$f(0)=1\cdot1=1$，$f\!\left(\dfrac\pi3\right)=\dfrac14\cdot\left(-\dfrac12\right)=-\dfrac18$，"
        r"$f\!\left(\dfrac\pi2\right)=0\cdot(-1)=0$，$f\!\left(\dfrac{2\pi}3\right)=\dfrac14\cdot\left(-\dfrac12\right)=-\dfrac18$，"
        r"$f(\pi)=1\cdot1=1$．" "\n"
        r"故最大值为 $1$，最小值为 $-\dfrac18$．"
    ),
    'review': (
        r"★ 提取文本作「f (x)= cos2xcos2x」，两个 $\cos$ 的上标全丢，"
        r"与 $\cos2x\cdot\cos2x$、$\cos^2x\cdot\cos2x$ 无从区分。"
        r"由详解「$f'(x)=2\cos x(-\sin x)\cos2x+\cos^2x(-2\sin2x)=-\sin2x(2\cos2x+1)$」还原——"
        r"**导数里出现 $\cos^2x$，证明题干是 $\cos^{2}x\cos2x$** ✓。" "\n"
        r"**数值校验**：" "\n"
        r"$f(0)=\cos^2 0\cdot\cos0=1\times1=1$ ✓；"
        r"$f(\frac\pi3)=\cos^2\frac\pi3\cdot\cos\frac{2\pi}3=(0.5)^2\times(-0.5)=-0.125=-\frac18$ ✓；"
        r"$f(\frac\pi2)=0\times(-1)=0$ ✓；"
        r"$f(\frac{2\pi}3)=(0.5)^2\times\cos\frac{4\pi}3=0.25\times(-0.5)=-\frac18$ ✓。" "\n"
        r"最大值检验：令 $u=\cos^2x\in[0,1]$，$\cos2x=2u-1$，"
        r"$f=u(2u-1)=2u^2-u$，在 $u\in[0,1]$ 上最小值在 $u=\frac14$ 处 $=2\cdot\frac1{16}-\frac14=-\frac18$ ✓，"
        r"最大值在 $u=1$ 处 $=1$ ✓。**与答案完全吻合**。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-106'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-106-V1',
}

T106_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知 $f(x)=\sin2x+2\cos x$，$x\in(0,\pi)$．" "\n"
        r"（1）求 $f(x)$ 的单调区间；"
    ),
    'opts': [],
    'answer': (
        r"$f(x)$ 在 $\left(0,\dfrac\pi6\right)$ 与 $\left(\dfrac{5\pi}6,\pi\right)$ 上单调递增，"
        r"在 $\left(\dfrac\pi6,\dfrac{5\pi}6\right)$ 上单调递减"
    ),
    'analysis': (
        r"求导后用 $\cos2x=1-2\sin^{2}x$ 化为关于 $\sin x$ 的二次式，"
        r"再因式分解：$f'(x)=-2(2\sin x-1)(\sin x+1)$；"
        r"注意 $x\in(0,\pi)$ 时 $\sin x+1>0$，故符号只由 $2\sin x-1$ 决定。"
    ),
    'solution': (
        r"$f'(x)=2\cos2x-2\sin x=2\left(1-2\sin^{2}x\right)-2\sin x"
        r"=-4\sin^{2}x-2\sin x+2=-2\left(2\sin^{2}x+\sin x-1\right)$" "\n"
        r"$=-2(2\sin x-1)(\sin x+1)$．" "\n"
        r"$x\in(0,\pi)$ 时 $\sin x\in(0,1]$，故 $\sin x+1>0$ 恒成立，"
        r"$f'(x)$ 的符号由 $-(2\sin x-1)$ 决定：" "\n"
        r"$f'(x)>0\iff2\sin x-1<0\iff\sin x<\dfrac12"
        r"\iff x\in\left(0,\dfrac\pi6\right)\cup\left(\dfrac{5\pi}6,\pi\right)$；" "\n"
        r"$f'(x)<0\iff\sin x>\dfrac12\iff x\in\left(\dfrac\pi6,\dfrac{5\pi}6\right)$．" "\n"
        r"故 $f$ 的增区间为 $\left(0,\dfrac\pi6\right)$ 与 $\left(\dfrac{5\pi}6,\pi\right)$，"
        r"减区间为 $\left(\dfrac\pi6,\dfrac{5\pi}6\right)$．"
    ),
    'review': (
        r"★ 提取文本作「f (x)= sin2x + 2cosx,x ∈(0,π)」，"
        r"$\sin2x$ 尚完整（$2$ 是系数而非上标），但需与 $\sin^2x$ 区分。"
        r"由详解「$f'(x)=2\cos2x-2\sin x=2-4\sin^2x-2\sin x=-2(2\sin x-1)(\sin x+1)$」还原——"
        r"**导数含 $\cos2x$，证明题干是 $\sin2x$（而非 $\sin^2x$）** ✓。" "\n"
        r"**⚠ 因式分解的符号校验**（这里极易错）：" "\n"
        r"$-2(2\sin x-1)(\sin x+1)=-2(2\sin^2x+2\sin x-\sin x-1)=-2(2\sin^2x+\sin x-1)"
        r"=-4\sin^2x-2\sin x+2$ ✓ 与 $2-4\sin^2x-2\sin x$ 一致 ✓。" "\n"
        r"**数值校验**：$x=\frac\pi6$：$\sin x=0.5$，$f'=0$ ✓ 驻点；"
        r"$x=\frac\pi2$：$\sin x=1$，$f'=-2(2-1)(1+1)=-4<0$ ✓ 递减；"
        r"$x\to\pi^-$：$\sin x\to0$，$f'\to-2(0-1)(0+1)=+2>0$ ✓ 递增。"
        r"$f(\frac\pi6)=\sin\frac\pi3+2\cos\frac\pi6=0.866+1.732=2.598$；"
        r"$f(\frac{5\pi}6)=\sin\frac{5\pi}3+2\cos\frac{5\pi}6=-0.866-1.732=-2.598$ ✓ 递减趋势对。"
    ),
    'difficulty': 0.75,
    'topics': ['M-T-106'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-106-V2',
}

QS = [T105_E1, T106_E1, T106_V1, T106_V2]
