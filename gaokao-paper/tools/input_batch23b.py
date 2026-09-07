# -*- coding: utf-8 -*-
r"""第23批（下）：M-T-108 已知单调性求参（4题）

来源：2024高中数学热点题型归纳完整解析版.pdf 专题3 p75~p76（PDF 页 74~75）

## 题型套路

已知 $f$ 在区间 $I$ 上单调增（减）$\iff$ $f'(x)\geqslant0$（$\leqslant0$）在 $I$ 上恒成立
$\to$ **参变分离** $\to$ 求另一侧的最值。

本批三道变式分别是三种分离后的形态：

| 题 | 分离后 | 求最值的方法 |
|---|---|---|
| V1 | $h(x)=ax^{2}+(1-2a)x-a^{2}-2\geqslant0$ | 对称轴 + 端点 |
| V2 | $a\leqslant\dfrac{(x+2)^{2}}{x-1}$ | 基本不等式 / 导数 |
| V3 | $2x^{2}+ax-1\leqslant0$ | 二次函数端点法 |

## 两处原书问题（已记入 review）

1. **E1**：详解说 $a=0$ 成立，但答案写 $0<a\leqslant1$ —— 自相矛盾，
   严格答案应为 $0\leqslanta\leqslant1$。
2. **V1**：详解的 $h(x)$ 常数项写成 $-a^{2}-2a$，由答案反推应为 $-a^{2}-2$。
"""

T108_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=\dfrac a3x^{3}-ax^{2}+x+1$．" "\n"
        r"（1）若 $f(x)$ 在 $(-\infty,+\infty)$ 上是增函数，求 $a$ 的取值范围．"
    ),
    'opts': [],
    'answer': r"$0<a\leqslant1$（原书答案；严格应为 $0\leqslanta\leqslant1$，见 review）",
    'analysis': (
        r"$f'(x)=ax^{2}-2ax+1$，按 $a=0$、$a>0$、$a<0$ 三类讨论其在 $\mathbb R$ 上恒 $\geqslant0$ 的条件。"
    ),
    'solution': (
        r"$f'(x)=ax^{2}-2ax+1$．要求 $f'(x)\geqslant0$ 对一切 $x\in\mathbb R$ 成立．" "\n"
        r"① $a=0$：$f'(x)=1>0$，成立；" "\n"
        r"② $a>0$：$f'$ 是开口向上的二次函数，最小值在 $x=\dfrac{2a}{2a}=1$ 处，" "\n"
        r"$f'(x)_{\min}=f'(1)=a-2a+1=1-a\geqslant0\Rightarrow a\leqslant1$，故 $0<a\leqslant1$；" "\n"
        r"③ $a<0$：$f'$ 开口向下，$x\to+\infty$ 时 $f'(x)\to-\infty$，"
        r"不可能恒 $\geqslant0$，舍去．" "\n"
        r"综上（含 $a=0$ 的情形）$0\leqslanta\leqslant1$；原书答案写作 $0<a\leqslant1$．"
    ),
    'review': (
        r"★ 提取文本作「f (x)= x 3- ax 2+ x + 1」，$\frac a3x^3$ 的分数线、"
        r"$x^3$ 与 $ax^2$ 的上标全丢，「a」与「3」被拆到相邻行。"
        r"由详解「$f'(x)=ax^2-2ax+1$」反推："
        r"$\frac{\mathrm d}{\mathrm dx}\left(\frac a3x^3\right)=ax^2$ ✓、"
        r"$\frac{\mathrm d}{\mathrm dx}(-ax^2)=-2ax$ ✓、"
        r"$\frac{\mathrm d}{\mathrm dx}(x+1)=1$ ✓，故题干确为 $f(x)=\frac a3x^3-ax^2+x+1$ ✓。" "\n"
        r"**⚠ 原书自相矛盾（已标记，供复核）**：" "\n"
        r"详解写「当 $a=0$ 时，$f'(x)=1>0$，故结论成立」，"
        r"但末尾「综上得 $a$ 的取值范围是 $0<a\leqslant1$」把 $a=0$ 排除了。" "\n"
        r"$a=0$ 时 $f(x)=x+1$ 确实是 $\mathbb R$ 上的增函数，**结论成立是事实**，"
        r"故严格答案应为 $0\leqslanta\leqslant1$。" "\n"
        r"按项目约定**答案照原书录入**（$0<a\leqslant1$），"
        r"此处如实标注矛盾，供日后与原书核对。**建议列入 D 类存疑。**"
    ),
    'difficulty': 0.65,
    'topics': ['M-T-108'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-108-E1',
}

T108_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=\ln(ax+1)+\dfrac{x^{3}}3-x^{2}-ax$（$a\in\mathbb R$）．" "\n"
        r"（1）若 $y=f(x)$ 在 $[4,+\infty)$ 上为增函数，求实数 $a$ 的取值范围．"
    ),
    'opts': [],
    'answer': r"$0<a\leqslant4+3\sqrt2$",
    'analysis': (
        r"$f'(x)=\dfrac a{ax+1}+x^{2}-2x-a\geqslant0$ 在 $[4,+\infty)$ 上恒成立；"
        r"去分母（需 $ax+1>0$）后化为二次式 $h(x)\geqslant0$，"
        r"由对称轴位置知 $h$ 在 $[4,+\infty)$ 上递增，只需 $h(4)\geqslant0$。"
    ),
    'solution': (
        r"$f'(x)=\dfrac a{ax+1}+x^{2}-2x-a$．要求在 $[4,+\infty)$ 上 $f'(x)\geqslant0$．" "\n"
        r"需 $ax+1>0$（对数定义域），以下解得 $a>0$，该条件自动满足．" "\n"
        r"$f'(x)\geqslant0\iff\dfrac a{ax+1}+x^{2}-2x-a\geqslant0$，"
        r"两边乘 $ax+1>0$：" "\n"
        r"$a+(x^{2}-2x-a)(ax+1)\geqslant0$" "\n"
        r"$\Rightarrow a+ax^{3}-2ax^{2}-a^{2}x+x^{2}-2x-a\geqslant0$" "\n"
        r"$\Rightarrow ax^{3}-2ax^{2}+x^{2}-a^{2}x-2x\geqslant0$" "\n"
        r"$\Rightarrow x\bigl[ax^{2}+(1-2a)x-a^{2}-2\bigr]\geqslant0$．" "\n"
        r"因 $x\geqslant4>0$，等价于 $h(x)=ax^{2}+(1-2a)x-a^{2}-2\geqslant0$ 在 $[4,+\infty)$ 恒成立．" "\n"
        r"由答案 $a>0$，此时 $h$ 是开口向上的二次函数，"
        r"对称轴 $x=\dfrac{2a-1}{2a}=1-\dfrac1{2a}<1<4$，"
        r"故 $h$ 在 $[4,+\infty)$ 上**单调递增**，只需 $h(4)\geqslant0$：" "\n"
        r"$h(4)=16a+4(1-2a)-a^{2}-2=-a^{2}+8a+2\geqslant0$" "\n"
        r"$\Rightarrow a^{2}-8a-2\leqslant0\Rightarrow 4-3\sqrt2\leqslant a\leqslant4+3\sqrt2$．" "\n"
        r"结合 $a>0$，得 $0<a\leqslant4+3\sqrt2$．"
    ),
    'review': (
        r"★ 提取文本作「f(x) = ln(ax + 1) + / x3 / - x2- ax(a ∈R)．3」，"
        r"$\frac{x^3}{3}$ 的分数线与上标全丢，分子「x3」与分母「3」分离。"
        r"由详解「$f'(x)=\frac{a}{ax+1}+x^2-2x-a$」反推：$x^2$ 项来自 $\frac{x^3}{3}$ ✓、"
        r"$-2x$ 来自 $-x^2$ ✓、$-a$ 来自 $-ax$ ✓，故题干还原无误。" "\n"
        r"**⚠ 详解的常数项笔误**：详解写「$h(x)=ax^2+(1-2a)x-a^2-2a>0$」，"
        r"末尾多了一个 $a$。按 $-a^2-2a$ 算：$h(4)=16a+4-8a-a^2-2a=-a^2+6a+4$，"
        r"得 $0<a\leqslant3+\sqrt{13}\approx6.606$，**与答案 $4+3\sqrt2\approx8.243$ 不符** ✗；" "\n"
        r"按 $-a^2-2$ 算：$h(4)=-a^2+8a+2$，得 $a\leqslant4+3\sqrt2$ ✓ **与答案吻合**。" "\n"
        r"故取 $-a^2-2$，并在此如实标注原书笔误。" "\n"
        r"**数值校验**：$a=8$（$<8.243$）：$h(4)=-64+64+2=2>0$ ✓；"
        r"$a=9$（超出）：$h(4)=-81+72+2=-7<0$ ✗ ✓。"
        r"另验 $f'(4)$（$a=8$）：$\frac{8}{33}+16-8-8=0.242>0$ ✓。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-108'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-108-V1',
}

T108_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=\ln(x-1)+\dfrac a{x+2}$（$a\in\mathbb R$）．" "\n"
        r"（1）若函数 $f(x)$ 在定义域上是单调递增函数，求实数 $a$ 的取值范围．"
    ),
    'opts': [],
    'answer': r"$a\leqslant12$",
    'analysis': (
        r"定义域 $(1,+\infty)$；$f'(x)=\dfrac1{x-1}-\dfrac a{(x+2)^{2}}\geqslant0$ 恒成立，"
        r"分离得 $a\leqslant\dfrac{(x+2)^{2}}{x-1}$，求右侧最小值即可。"
    ),
    'solution': (
        r"定义域为 $(1,+\infty)$．$f'(x)=\dfrac1{x-1}-\dfrac a{(x+2)^{2}}$．" "\n"
        r"要在 $(1,+\infty)$ 上恒有 $f'(x)\geqslant0$，即" "\n"
        r"$a\leqslant\dfrac{(x+2)^{2}}{x-1}$ 对一切 $x>1$ 成立．" "\n"
        r"设 $g(x)=\dfrac{(x+2)^{2}}{x-1}$（$x>1$），求其最小值．" "\n"
        r"**方法1（基本不等式）**：令 $u=x-1>0$，则 $x+2=u+3$，" "\n"
        r"$g(x)=\dfrac{(u+3)^{2}}u=\dfrac{u^{2}+6u+9}u=u+6+\dfrac9u"
        r"\geqslant2\sqrt{u\cdot\dfrac9u}+6=6+6=12$，" "\n"
        r"当且仅当 $u=\dfrac9u$ 即 $u=3$、$x=4$ 时取等号，故 $g_{\min}=12$．" "\n"
        r"**方法2（导数）**：$g'(x)=\dfrac{2(x+2)(x-1)-(x+2)^{2}}{(x-1)^{2}}"
        r"=\dfrac{(x+2)(x-4)}{(x-1)^{2}}$，" "\n"
        r"$1<x<4$ 时 $g'<0$，$x>4$ 时 $g'>0$，故 $g$ 在 $x=4$ 处取最小值 $g(4)=\dfrac{36}{3}=12$．" "\n"
        r"综上 $a\leqslant12$．"
    ),
    'review': (
        r"★ 提取文本作「f(x) = ln()+ / 3x + 2 / (a ∈R)．」，"
        r"$\ln$ 的参数与分式被拆散，**多出一个「3」**（疑为相邻行的排版残片）。"
        r"由详解「函数定义域为 $(1,+\infty)$，$f'(x)=\frac1{x-1}-\frac a{(x+2)^2}$」**反推锁定题干**：" "\n"
        r"$\frac1{x-1}$ 只能来自 $\ln(x-1)$ ✓；"
        r"$-\frac a{(x+2)^2}$ 只能来自 $+\frac a{x+2}$ ✓；"
        r"定义域 $(1,+\infty)$ 与 $\ln(x-1)$ 一致 ✓。" "\n"
        r"若按「$3x+2$」理解则为 $\frac a{3x+2}$，导数是 $-\frac{3a}{(3x+2)^2}$，与详解不符 ✗。" "\n"
        r"**数值校验**：$g(4)=\frac{(4+2)^2}{4-1}=\frac{36}{3}=12$ ✓；"
        r"$g(2)=\frac{16}{1}=16>12$ ✓；$g(7)=\frac{81}{6}=13.5>12$ ✓。"
        r"$a=12$ 时：$f'(x)=\frac1{x-1}-\frac{12}{(x+2)^2}$，$x=4$ 处 $=\frac13-\frac{12}{36}=0$ ✓ 恰取等；"
        r"$x=2$ 处 $=1-\frac{12}{16}=0.25>0$ ✓。"
    ),
    'difficulty': 0.7,
    'topics': ['M-T-108'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-108-V2',
}

T108_V3 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=x^{2}+ax-\ln x$（$a\in\mathbb R$）．" "\n"
        r"（1）若函数 $f(x)$ 在 $[1,2]$ 上是减函数，求实数 $a$ 的取值范围．"
    ),
    'opts': [],
    'answer': r"$a\leqslant-\dfrac72$",
    'analysis': (
        r"$f'(x)=\dfrac{2x^{2}+ax-1}{x}\leqslant0$ 在 $[1,2]$ 上恒成立；"
        r"因 $x>0$，等价于开口向上的二次式 $h(x)=2x^{2}+ax-1\leqslant0$ 在 $[1,2]$ 上恒成立，"
        r"只需两端点 $\leqslant0$。"
    ),
    'solution': (
        r"定义域 $(0,+\infty)$．$f'(x)=2x+a-\dfrac1x=\dfrac{2x^{2}+ax-1}{x}$．" "\n"
        r"在 $[1,2]$ 上 $x>0$，故 $f'(x)\leqslant0\iff h(x)=2x^{2}+ax-1\leqslant0$．" "\n"
        r"$h$ 是开口向上的二次函数，在区间 $[1,2]$ 上的最大值必在端点取得，"
        r"故只需：" "\n"
        r"$\begin{cases}h(1)=2+a-1=a+1\leqslant0\\ "
        r"h(2)=8+2a-1=2a+7\leqslant0\end{cases}$"
        r"$\Rightarrow\begin{cases}a\leqslant-1\\ a\leqslant-\dfrac72\end{cases}$" "\n"
        r"取交集得 $a\leqslant-\dfrac72$．"
    ),
    'review': (
        r"★ 提取文本作「f (x)= x2+ ax - lnx,a ∈R」，$x^2$ 的上标丢失。"
        r"由详解「$f'(x)=2x+a-\frac1x=\frac{2x^2+ax-1}{x}\leqslant0$ 在 $[1,2]$ 上恒成立，"
        r"令 $h(x)=2x^2+ax-1$，有 $h(1)\leqslant0$、$h(2)\leqslant0$，"
        r"得 $a\leqslant-1$、$a\leqslant-\frac72$，得 $a\leqslant-\frac72$」还原——"
        r"导数里的 $2x^2$ 反证题干是 $x^2$ 而非 $2x$ ✓。" "\n"
        r"**数值校验**：$a=-\frac72=-3.5$：$h(1)=2-3.5-1=-2.5\leqslant0$ ✓；"
        r"$h(2)=8-7-1=0$ ✓ 恰取等；$h(1.5)=4.5-5.25-1=-1.75<0$ ✓。"
        r"$a=-3$（$>-\frac72$）：$h(2)=8-6-1=1>0$ ✗ 故不满足 ✓。"
        r"$f'(2)=\frac{8-7-1}{2}=0$ ✓。"
    ),
    'difficulty': 0.7,
    'topics': ['M-T-108'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-108-V3',
}

QS = [T108_E1, T108_V1, T108_V2, T108_V3]
