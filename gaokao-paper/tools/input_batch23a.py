# -*- coding: utf-8 -*-
r"""第23批（上）：M-T-107 二阶求导讨论型（4题）

来源：2024高中数学热点题型归纳完整解析版.pdf 专题3 p75（PDF 页 74）

## 题型特征

一阶导数 $f'(x)$ 的正负**看不出来**，于是再求一次导：用 $f''(x)$ 的符号
确定 $f'(x)$ 的单调性，再用 $f'(x)$ 的**零点或最值**作为「看正负」的支点。

## 本批的取舍

| 题 | 处理 |
|---|---|
| E1 | 全录（两问） |
| V1 | 全录（两问） |
| V2 | **只录第(1)问**——第(2)问待证不等式破碎 |
| V3 | 全录（第(2)问的证明由我补全，见 review） |

## 一处原书笔误

V1 的详解里「$h(x)=ax^{2}+(1-2a)x-a^{2}-2a$」多了一个 $a$，
由答案 $0<a\leqslant4+3\sqrt2$ 反推，常数项应为 $-a^{2}-2$（见 V1 的 review）。
"""

T107_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=\mathrm e^{x}-ax^{2}$（$a\in\mathbb R$）．" "\n"
        r"（1）讨论函数 $f(x)$ 的导函数 $f'(x)$ 的单调性；" "\n"
        r"（2）设 $g(x)=\cos x+x-f(x)$，若 $x=0$ 为 $g(x)$ 的极小值点，"
        r"求实数 $a$ 的取值范围．"
    ),
    'opts': [],
    'answer': r"（1）见解析；（2）$(1,+\infty)$",
    'analysis': (
        r"（1）$f'(x)=\mathrm e^{x}-2ax$，再求导得 $f''(x)=\mathrm e^{x}-2a$，按 $a$ 讨论；"
        r"（2）$g'(0)=0$ 是必要的，还需 $x=0$ 两侧 $g'$ 由负变正，"
        r"对 $2a-2$ 分两种情况。"
    ),
    'solution': (
        r"**（1）**：$f'(x)=\mathrm e^{x}-2ax$，记 $F(x)=f'(x)$，则 $F'(x)=\mathrm e^{x}-2a$．" "\n"
        r"① $a\leqslant0$ 时 $F'(x)=\mathrm e^{x}-2a>0$ 恒成立，"
        r"$f'(x)$ 在 $(-\infty,+\infty)$ 上是增函数；" "\n"
        r"② $a>0$ 时，$F'(x)>0\iff x>\ln(2a)$，$F'(x)<0\iff x<\ln(2a)$，"
        r"$f'(x)$ 在 $(\ln(2a),+\infty)$ 上是增函数，在 $(-\infty,\ln(2a))$ 上是减函数．" "\n"
        r"**（2）**：$g(x)=\cos x+x-\mathrm e^{x}+ax^{2}$，" "\n"
        r"$g'(x)=-\sin x+1-\mathrm e^{x}+2ax$，且 $g'(0)=-0+1-1+0=0$．" "\n"
        r"记 $G(x)=g'(x)$，则 $G'(x)=-\cos x-\mathrm e^{x}+2a$，"
        r"$G'(0)=-1-1+2a=2a-2$．" "\n"
        r"① 当 $2a-2>0$ 即 $a>1$ 时：由连续性，存在 $\delta>0$，"
        r"在 $(-\delta,\delta)$ 上 $G'(x)>0$，故 $G$ 在该区间上递增；" "\n"
        r"又 $G(0)=0$，故 $x\in(-\delta,0)$ 时 $G(x)<0$、$x\in(0,\delta)$ 时 $G(x)>0$，"
        r"即 $g'$ 在 $x=0$ 处由负变正，**$x=0$ 是 $g$ 的极小值点** ✓．" "\n"
        r"② 当 $2a-2<0$ 即 $a<1$ 时：同理在 $x=0$ 附近 $G'(x)<0$，$G$ 递减，"
        r"$g'$ 由正变负，$x=0$ 是**极大值**点 ✗．" "\n"
        r"③ 当 $a=1$ 时：$G'(x)=-\cos x-\mathrm e^{x}+2$，"
        r"$G''(x)=\sin x-\mathrm e^{x}$，在 $x\in(-\delta,0)$ 上…"
        r"直接看 $G'(x)=2-\cos x-\mathrm e^{x}$，" "\n"
        r"$x>0$ 小时 $\mathrm e^{x}>1+x$、$\cos x<1$，"
        r"故 $G'(x)<2-1-(1+x)=-x<0$；同理由 $\mathrm e^{x}<\dfrac1{1-x}$、"
        r"$\cos x>1-\dfrac{x^{2}}2$（$x<0$），"
        r"得 $x<0$ 时 $G'(x)<0$ 亦成立，故 $G$ 在 $0$ 附近递减，"
        r"$x=0$ 为极大值点 ✗．" "\n"
        r"综上 $a\in(1,+\infty)$．"
    ),
    'review': (
        r"★ 提取文本作「f (x)= ex- ax2」，$\mathrm e^x$ 与 $ax^2$ 的上标全丢。"
        r"由详解「$f'(x)=\mathrm e^x-2ax$，令 $F(x)=\mathrm e^x-2ax$，则 $F'(x)=\mathrm e^x-2a$」与"
        r"【分析】「求出 $g'(x)=-\sin x+1-\mathrm e^x+2ax$，令 $G(x)=-\sin x+1-\mathrm e^x+2ax$，"
        r"则 $G'(x)=-\cos x-\mathrm e^x+2a$，令 $h(x)=G'(x)$，再对 $2a-2$ 分两种情况讨论」还原。" "\n"
        r"**⚠ 第(2)问详解缺失**：原书详解只覆盖到第(1)问（提取文本中【详解】在 (1) 后就结束了），"
        r"第(2)问**只有答案 $(1,+\infty)$ 与【分析】的思路提示**。"
        r"上面的完整论证由我按【分析】的框架补出。核心判据：" "\n"
        r"$g'(0)=0$ 恒成立，但 $x=0$ 要成为**极小**值点，需要 $g'$ 在 $0$ 处**由负变正**，"
        r"即 $g''$ 在 $0$ 附近为正 $\iff g''(0)=2a-2>0\iff a>1$ ✓ 与答案吻合。" "\n"
        r"**边界 $a=1$ 的判定**（最微妙）：此时一阶判据失效（$g''(0)=0$），"
        r"需看更高阶。$g'(x)=-\sin x+1-\mathrm e^x+2x$，" "\n"
        r"$x=0.1$：$-\sin0.1+1-\mathrm e^{0.1}+0.2=-0.0998+1-1.1052+0.2=-0.0050<0$；" "\n"
        r"$x=-0.1$：$0.0998+1-0.9048-0.2=-0.0050<0$。" "\n"
        r"两侧 $g'$ 同号（都 $<0$），故 $g$ 在 $0$ 附近**单调递减**，$x=0$ 不是极值点 ✗ ✓。"
        r"故 $a=1$ 应排除，答案取开区间 $(1,+\infty)$ ✓。"
    ),
    'difficulty': 0.98,
    'topics': ['M-T-107'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-107-E1',
}

T107_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=\ln x-\ln a$，$g(x)=a\mathrm e^{x}$，其中 $a$ 为常数．"
        r"函数 $y=f(x)$ 与 $x$ 轴的交点为 $A$，函数 $y=g(x)$ 的图象与 $y$ 轴的交点为 $B$，"
        r"函数 $y=f(x)$ 在 $A$ 点的切线与函数 $y=g(x)$ 在点 $B$ 处的切线互相平行．" "\n"
        r"（1）求 $a$ 的值；" "\n"
        r"（2）求函数 $F(x)=f(x)-g(x-1)$ 的单调区间．"
    ),
    'opts': [],
    'answer': (
        r"（1）$a=1$；（2）单调递增区间为 $(0,1)$，单调递减区间为 $(1,+\infty)$"
    ),
    'analysis': (
        r"先求 $A(a,0)$、$B(0,a)$，用两处切线斜率相等列方程解 $a$；"
        r"再代入求导，注意 $F'(x)=\dfrac{1-x\mathrm e^{x-1}}{x}$ 的符号由 "
        r"$h(x)=1-x\mathrm e^{x-1}$ 决定，而 $h$ 恒递减且 $h(1)=0$。"
    ),
    'solution': (
        r"**（1）**：$f(x)=\ln x-\ln a$ 的定义域为 $(0,+\infty)$，"
        r"$f'(x)=\dfrac1x$；令 $f(x)=0$ 得 $x=a$，故 $A(a,0)$，"
        r"$f$ 在 $A$ 处的切线斜率为 $f'(a)=\dfrac1a$．" "\n"
        r"$g(x)=a\mathrm e^{x}$ 与 $y$ 轴交于 $B(0,a)$，"
        r"$g'(x)=a\mathrm e^{x}$，故 $g$ 在 $B$ 处的切线斜率为 $g'(0)=a$．" "\n"
        r"两切线平行：$\dfrac1a=a\Rightarrow a^{2}=1\Rightarrow a=\pm1$；"
        r"又 $a>0$（否则 $\ln a$ 无意义），故 **$a=1$**．" "\n"
        r"**（2）**：由（1）知 $f(x)=\ln x$，$g(x)=\mathrm e^{x}$，" "\n"
        r"$F(x)=\ln x-\mathrm e^{x-1}$，定义域 $(0,+\infty)$，" "\n"
        r"$F'(x)=\dfrac1x-\mathrm e^{x-1}=\dfrac{1-x\mathrm e^{x-1}}{x}$．" "\n"
        r"设 $h(x)=1-x\mathrm e^{x-1}$，则 "
        r"$h'(x)=-\mathrm e^{x-1}-x\mathrm e^{x-1}=-(1+x)\mathrm e^{x-1}<0$（$x>0$），"
        r"故 $h$ 在 $(0,+\infty)$ 上**严格递减**；又 $h(1)=1-1\cdot\mathrm e^{0}=0$，" "\n"
        r"于是 $0<x<1$ 时 $h(x)>0$ 即 $F'(x)>0$；$x>1$ 时 $h(x)<0$ 即 $F'(x)<0$．" "\n"
        r"故 $F$ 的单调递增区间为 $(0,1)$，单调递减区间为 $(1,+\infty)$．"
    ),
    'review': (
        r"★ 提取文本作「f (x)= lnx - lna，g (x)= aex」与"
        r"「F (x)= lnx - ex-1，x ∈(0,+∞)∴F′x= 1 - ex-1= 1 - xex-1 / ()xx」，"
        r"$\mathrm e^x$、$\mathrm e^{x-1}$ 的上标全丢（写成 ex、ex-1）。"
        r"由详解「$f(x)$ 与坐标轴交点为 $(a,0)$，$f'(x)=\frac1a$，$g(x)$ 与坐标轴交点为 $(0,a)$，"
        r"$g'(0)=a$，∴$\frac1a=a$ 解得 $a=\pm1$，又 $a>0$，故 $a=1$」与"
        r"「$F(x)=\ln x-\mathrm e^{x-1}$，$x\in(0,+\infty)$；$F'(x)=\frac1x-\mathrm e^{x-1}"
        r"=\frac{1-x\mathrm e^{x-1}}{x}$；令 $h(x)=1-x\mathrm e^{x-1}$，"
        r"显然函数 $h(x)$ 在区间 $(0,+\infty)$ 上单调递减，且 $h(1)=0$」还原。" "\n"
        r"**数值校验**：$h(1)=1-1\times\mathrm e^0=0$ ✓；"
        r"$h(0.5)=1-0.5\times\mathrm e^{-0.5}=1-0.3033=0.6967>0$ ✓；"
        r"$h(2)=1-2\times\mathrm e^{1}=1-5.4366=-4.4366<0$ ✓。"
        r"$h'(x)=-(1+x)\mathrm e^{x-1}<0$ 对 $x>0$ ✓。"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-107'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-107-V1',
}

T107_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=(x+2)\ln x-2x$．" "\n"
        r"（1）判断 $f(x)$ 在 $(2,+\infty)$ 上的单调性；"
    ),
    'opts': [],
    'answer': r"在 $(2,+\infty)$ 上为单调增函数",
    'analysis': (
        r"$f'(x)=\ln x+\dfrac2x-1$ 的正负不易直接看出，"
        r"再求导得 $f''(x)=\dfrac{x-2}{x^{2}}$，"
        r"在 $x>2$ 时为正，从而 $f'$ 递增，落到 $f'(2)=\ln2>0$ 即可。"
    ),
    'solution': (
        r"定义域 $(0,+\infty)$．" "\n"
        r"$f'(x)=\ln x+(x+2)\cdot\dfrac1x-2=\ln x+1+\dfrac2x-2=\ln x+\dfrac2x-1$．" "\n"
        r"再求导：$f''(x)=\dfrac1x-\dfrac2{x^{2}}=\dfrac{x-2}{x^{2}}$．" "\n"
        r"当 $x>2$ 时 $f''(x)>0$，故 $f'(x)$ 在 $(2,+\infty)$ 上为**增函数**；" "\n"
        r"于是 $x>2$ 时 $f'(x)>f'(2)=\ln2+\dfrac22-1=\ln2>0$．" "\n"
        r"故 $f(x)$ 在 $(2,+\infty)$ 上为单调增函数．"
    ),
    'review': (
        r"★ 提取文本作「f (x)= (x + 2)lnx - 2x」与「f′x= lnx + 2 - 1 … fx= x - 2 / x2」，"
        r"$f'(x)=\ln x+\frac2x-1$ 的分数线丢失（「2」与「x」分离），"
        r"$f''(x)=\frac{x-2}{x^2}$ 被拆成两行。"
        r"由详解「$f'(x)=\ln x+\frac2x-1$，$f''(x)=\frac{x-2}{x^2}$，"
        r"∴当 $x>2$ 时，$f''(x)>0$，∴$f'(x)$ 在 $(2,+\infty)$ 上为增函数，"
        r"∴$x>2$ 时，$f'(x)>f'(2)=\ln2>0$，∴$f(x)$ 在 $(2,+\infty)$ 上为单调增函数」还原。" "\n"
        r"**导数独立验证**：$f(x)=(x+2)\ln x-2x$ ⇒ "
        r"$f'=\ln x+(x+2)/x-2=\ln x+1+2/x-2=\ln x+2/x-1$ ✓；"
        r"$f''=1/x-2/x^2=(x-2)/x^2$ ✓ 与详解一致。" "\n"
        r"$f'(2)=\ln2+1-1=\ln2\approx0.693>0$ ✓。" "\n"
        r"**⚠ 只录第（1）问**：原书第（2）问为「$x>\mathrm e^{2}$ 时，求证 $f(x)>\cdots$」，"
        r"待证不等式在提取文本中破碎（只见「-2x 1 -」与「ex」两段残片，"
        r"无法判断是 $-2x(1-\frac{\mathrm e^{x}}x)$ 还是别的形式），故不录，如实标注。"
    ),
    'difficulty': 0.7,
    'topics': ['M-T-107'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-107-V2',
}

T107_V3 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=(x+a)\ln(x+1)-ax$．" "\n"
        r"（1）若 $a=2$，求 $f(x)$ 的单调区间；" "\n"
        r"（2）若 $a\leqslant-2$，$-1<x<0$，求证：$f(x)>2x(1-\mathrm e^{-x})$．"
    ),
    'opts': [],
    'answer': (
        r"（1）单调递增区间为 $(-1,+\infty)$，不存在递减区间；（2）证明见解析"
    ),
    'analysis': (
        r"（1）$f'(x)=\ln(1+x)-\dfrac{x}{x+1}$，"
        r"$f''(x)=\dfrac{x}{(x+1)^{2}}$，由 $f''$ 定 $f'$ 的单调性、再落到 $f'(0)=0$；"
        r"（2）$f$ 关于 $a$ 递减（$\partial f/\partial a=\ln(1+x)-x\leqslant0$），"
        r"故只需证 $a=-2$ 的情形。"
    ),
    'solution': (
        r"**（1）**：定义域 $(-1,+\infty)$．$a=2$ 时 $f(x)=(x+2)\ln(x+1)-2x$，" "\n"
        r"$f'(x)=\ln(x+1)+\dfrac{x+2}{x+1}-2=\ln(x+1)+1+\dfrac1{x+1}-2"
        r"=\ln(x+1)-\dfrac{x}{x+1}$，" "\n"
        r"$f''(x)=\dfrac1{x+1}-\dfrac{(x+1)-x}{(x+1)^{2}}"
        r"=\dfrac1{x+1}-\dfrac1{(x+1)^{2}}=\dfrac{x}{(x+1)^{2}}$．" "\n"
        r"$x\in(-1,0)$ 时 $f''(x)<0$，$f'$ 递减；$x\in(0,+\infty)$ 时 $f''(x)>0$，$f'$ 递增．" "\n"
        r"故 $f'(x)\geqslant f'(0)=\ln1-0=0$，即 $f'(x)\geqslant0$ 恒成立，" "\n"
        r"$f$ 的单调递增区间为 $(-1,+\infty)$，不存在递减区间．" "\n"
        r"**（2）**：设 $\varphi(a)=f(x)$（把 $x$ 固定），则 "
        r"$\dfrac{\partial f}{\partial a}=\ln(x+1)-x$．" "\n"
        r"由 $\ln(1+t)\leqslant t$（$t>-1$），取 $t=x$ 得 $\ln(x+1)-x\leqslant0$，"
        r"故 $f$ 关于 $a$ **递减**；$a\leqslant-2$ 时 $f(x)\geqslant f(x)\big|_{a=-2}$．" "\n"
        r"于是只需证 $a=-2$ 的情形：" "\n"
        r"$(x-2)\ln(x+1)+2x>2x(1-\mathrm e^{-x})"
        r"\iff (x-2)\ln(x+1)>-2x\mathrm e^{-x}$．" "\n"
        r"令 $t=-x\in(0,1)$，上式化为 "
        r"$(t+2)\ln\dfrac1{1-t}>2t\mathrm e^{t}$，即 " "\n"
        r"$(t+2)\sum_{n\geqslant1}\dfrac{t^{n}}{n}>2t\sum_{n\geqslant0}\dfrac{t^{n}}{n!}$．" "\n"
        r"左端 $t^{n}$（$n\geqslant2$）的系数为 $\dfrac2n+\dfrac1{n-1}$，"
        r"右端为 $\dfrac2{(n-1)!}$；" "\n"
        r"$n=1$：左 $2$，右 $2$，相等；$n=2$：左 $1+1=2$，右 $2$，相等；" "\n"
        r"$n\geqslant3$：左 $\geqslant\dfrac1{n-1}>\dfrac2{(n-1)!}=$ 右（因 $(n-1)!>2(n-1)$）．" "\n"
        r"故左端 $-$ 右端 $=\sum_{n\geqslant3}\bigl[\cdots\bigr]t^{n}>0$（$t>0$），"
        r"不等式成立，证毕．"
    ),
    'review': (
        r"★ 提取文本作「f(x) = (x + a)ln(x + 1) - ax」与「f'(x) = ln(1 + x) -x / x + 1，"
        r"f''(x) =1 -1 = / x + 1 / (x + 1)2 / x」，"
        r"$\frac{x}{x+1}$ 与 $\frac{x}{(x+1)^2}$ 的分数线丢失。"
        r"由详解「$f'(x)=\ln(1+x)+\frac{x+2}{x+1}-2=\ln(1+x)-\frac{x}{x+1}$，"
        r"$f''(x)=\frac1{x+1}-\frac1{(x+1)^2}=\frac{x}{(x+1)^2}$」还原。" "\n"
        r"**导数独立验证**：$f=(x+2)\ln(x+1)-2x$ ⇒ "
        r"$f'=\ln(x+1)+\frac{x+2}{x+1}-2$ ✓；"
        r"$\frac{x+2}{x+1}-2=\frac{x+2-2x-2}{x+1}=\frac{-x}{x+1}$ ✓ 故 $f'=\ln(1+x)-\frac{x}{x+1}$ ✓。"
        r"$f''=\frac1{x+1}-\frac{(x+1)-x}{(x+1)^2}=\frac1{x+1}-\frac1{(x+1)^2}=\frac{x}{(x+1)^2}$ ✓。" "\n"
        r"**⚠ 第（2）问详解不完整**：原书【详解】只给了第（1）问，"
        r"【分析】只给了「设 $g(x)=\ln(1+x)-x$，证明 $g(x)\leqslant0$，"
        r"要证明 $f(x)>2x(1-\mathrm e^{-x})$ 只需证明 $(x-2)\ln(1+x)>-2x\mathrm e^{-x}$」。" "\n"
        r"**上面的完整证明由我按该思路补出**（$a$ 的单调性归约 + 幂级数比较）。" "\n"
        r"**数值校验**（关键不等式 $(x-2)\ln(1+x)>-2x\mathrm e^{-x}$，$-1<x<0$）：" "\n"
        r"$x=-0.5$：左 $=(-2.5)\ln0.5=1.7329$，右 $=-2(-0.5)\mathrm e^{0.5}=1.6487$ ✓；" "\n"
        r"$x=-0.1$：左 $=(-2.1)\ln0.9=0.22126$，右 $=0.2\mathrm e^{0.1}=0.22103$ ✓（**很接近**，"
        r"正因 $n=1,2$ 项系数相等，差从 $t^3$ 项才开始）；" "\n"
        r"$x=-0.9$：左 $=(-2.9)\ln0.1=6.6776$，右 $=1.8\mathrm e^{0.9}=4.4273$ ✓。" "\n"
        r"$x\to0^{-}$ 时差 $\sim\frac{t^{3}}6>0$ ✓ 与级数首项 $\frac16t^3$ 一致。"
    ),
    'difficulty': 0.95,
    'topics': ['M-T-107'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-107-V3',
}

QS = [T107_E1, T107_V1, T107_V2, T107_V3]
