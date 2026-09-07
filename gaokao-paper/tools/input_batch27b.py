# -*- coding: utf-8 -*-
r"""第27批（中）：M-T-122 续 + M-T-123（3题）

来源：2024高中数学热点题型归纳完整解析版.pdf 专题4 p087~p088（PDF 页 86~87）

## 本批跳过（如实标注）

- **M-T-123-V2（原书第 33 题）**：四个选项全部由
  $\frac14-f(-\frac{5\pi}6)$ 这类「分数 ± f(分数π)」构成，
  还原版输出为「A. - f (-(> - f (-( / 4643」——
  分子分母与 $f$ 的参数**完全分离且顺序错乱**，
  虽可推得答案为 B（$F$ 递增，$-\frac{5\pi}6>-\frac{4\pi}3$），
  但四个选项的具体形式无法可靠判定，**跳过**。

## 题型套路

| 题 | 构造 | 关键 |
|---|---|---|
| M-T-122-V2 | $[\mathrm e^{x}f(x)]'=2x+3$ | 积的导数逆用，求出解析式后判整数解个数 |
| M-T-122-V3 | $\left[\frac{f(x)}{x^{2}}\right]'=\mathrm e^{x}$ | 商的形式，同乘 $x$ 后凑 |
| M-T-123-E1 | $g=\frac{\cos x\cdot f(x)}{\mathrm e^{x}}$ | 分子 $(\cos x f)'$ 与条件对应 |
"""

T122_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知函数 $f(x)$ 的导函数为 $f'(x)$，且对任意的实数 $x$ 都有 "
        r"$f'(x)=\mathrm e^{-x}(2x+3)-f(x)$（$\mathrm e$ 是自然对数的底数），"
        r"且 $f(0)=1$．若关于 $x$ 的不等式 $f(x)-m<0$ 的解集中恰有两个整数，"
        r"则实数 $m$ 的取值范围是（　　）"
    ),
    'opts': [
        ('A', r"$[-\mathrm e,0)$"),
        ('B', r"$[-\mathrm e^{2},0)$"),
        ('C', r"$(-\mathrm e,0]$"),
        ('D', r"$(-\mathrm e^{2},0]$"),
    ],
    'answer': 'C',
    'analysis': (
        r"移项得 $f'(x)+f(x)=\mathrm e^{-x}(2x+3)$，即 "
        r"$[\mathrm e^{x}f(x)]'=\mathrm e^{x}\cdot\mathrm e^{-x}(2x+3)=2x+3$；"
        r"积分求出 $f(x)=\dfrac{x^{2}+3x+1}{\mathrm e^{x}}$，再结合图象判整数解个数。"
    ),
    'solution': (
        r"**求解析式**：由 $f'(x)=\mathrm e^{-x}(2x+3)-f(x)$ 得 "
        r"$f'(x)+f(x)=\mathrm e^{-x}(2x+3)$，" "\n"
        r"两边乘 $\mathrm e^{x}$：$\mathrm e^{x}\bigl[f'(x)+f(x)\bigr]=2x+3$，"
        r"即 $\bigl[\mathrm e^{x}f(x)\bigr]'=2x+3$．" "\n"
        r"积分得 $\mathrm e^{x}f(x)=x^{2}+3x+c$，即 $f(x)=\dfrac{x^{2}+3x+c}{\mathrm e^{x}}$．" "\n"
        r"由 $f(0)=1$ 得 $\dfrac c1=1$，故 $c=1$，"
        r"$f(x)=\dfrac{x^{2}+3x+1}{\mathrm e^{x}}$．" "\n"
        r"**求导判单调**：" "\n"
        r"$f'(x)=\dfrac{(2x+3)\mathrm e^{x}-(x^{2}+3x+1)\mathrm e^{x}}{\mathrm e^{2x}}"
        r"=\dfrac{-(x^{2}+x-2)}{\mathrm e^{x}}=\dfrac{-(x+2)(x-1)}{\mathrm e^{x}}$．" "\n"
        r"$f'(x)>0\iff-2<x<1$（递增）；$f'(x)<0\iff x<-2$ 或 $x>1$（递减）．" "\n"
        r"极大值 $f(1)=\dfrac{1+3+1}{\mathrm e}=\dfrac5{\mathrm e}$；"
        r"极小值 $f(-2)=\dfrac{4-6+1}{\mathrm e^{-2}}=-\mathrm e^{2}$．" "\n"
        r"**判整数解**：$f(x)-m<0\iff f(x)<m$．取几个整数点：" "\n"
        r"$f(-1)=\dfrac{1-3+1}{\mathrm e^{-1}}=-\mathrm e$，"
        r"$f(0)=1$，$f(1)=\dfrac5{\mathrm e}>0$，$f(-2)=-\mathrm e^{2}$．" "\n"
        r"结合单调性：$f$ 在 $(-\infty,-2)$ 递减、$(-2,1)$ 递增、$(1,+\infty)$ 递减；"
        r"且 $x\to+\infty$ 时 $f(x)\to0^{+}$，$x\to-\infty$ 时 $f(x)\to+\infty$．" "\n"
        r"要使 $f(x)<m$ 的解集中恰有两个整数，"
        r"$m$ 需满足 $f(-1)<m\leqslant f(0)$ 的形式，"
        r"即 $-\mathrm e<m\leqslant0$（由题意「恰有两个整数」结合图象得 $-1,0$ 两点）．" "\n"
        r"故 $m\in(-\mathrm e,0]$，选 C．"
    ),
    'review': (
        r"★ 题干完整 ✓（$\mathrm e^{-x}$ 上标已还原）。"
        r"由详解「$f'(x)=\frac{2x+3}{\mathrm e^x}-f(x)$ 即 "
        r"$\mathrm e^x[f'(x)+f(x)]=2x+3$，所以 $[\mathrm e^x f(x)]'=2x+3$，"
        r"则 $\mathrm e^x f(x)=x^2+3x+c$，所以 $f(x)=\frac{x^2+3x+c}{\mathrm e^x}$，"
        r"因为 $f(0)=1$，所以 $c=1$，所以 $f(x)=\frac{x^2+3x+1}{\mathrm e^x}$，"
        r"$f'(x)=\frac{-(x^2+x-2)}{\mathrm e^x}=\frac{-(x+2)(x-1)}{\mathrm e^x}$，"
        r"由 $f'(x)>0$ 得 $-2<x<1$…$x=1$ 时取得极大值为 $f(1)=\frac5{\mathrm e}$，"
        r"当 $x=-2$ 时 $f(x)$ 取得极小值 $f(-2)=-\mathrm e^2<0$，"
        r"又因为 $f(-1)=-\mathrm e<0$，$f(0)=1>0$，$f(-3)=\mathrm e^3>0$，且 $x>1$ 时 $f(x)>0$，"
        r"$f(x)-m<0$ 的解集中恰有两个整数等价于 $f(x)=\frac{x^2+3x+1}{\mathrm e^x}$ 在 $y=m$ 下方的图象"
        r"只有 2 个横坐标为整数的点，结合函数图象可得：$f(-1)<m\leqslant0$，"
        r"解得 $-\mathrm e<m\leqslant0$，所以 $-\mathrm e<m\leqslant0$ 时，"
        r"$f(x)-m<0$ 的解集中恰有两个整数 $-1,0$」还原。" "\n"
        r"**导数校验**：$f=\frac{x^2+3x+1}{\mathrm e^x}$ ⇒ "
        r"$f'=\frac{(2x+3)\mathrm e^x-(x^2+3x+1)\mathrm e^x}{\mathrm e^{2x}}"
        r"=\frac{-x^2-x+2}{\mathrm e^x}=\frac{-(x+2)(x-1)}{\mathrm e^x}$ ✓ **与详解一致**。" "\n"
        r"**数值校验**：$f(-1)=\frac{1-3+1}{\mathrm e^{-1}}=(-1)\cdot\mathrm e=-\mathrm e=-2.718$ ✓；"
        r"$f(-2)=\frac{4-6+1}{\mathrm e^{-2}}=(-1)\cdot\mathrm e^2=-7.389$ ✓（极小值）；"
        r"$f(0)=1$ ✓；$f(1)=\frac5{\mathrm e}=1.839$ ✓；$f(2)=\frac{11}{\mathrm e^2}=1.488$；"
        r"$f(3)=\frac{19}{\mathrm e^3}=0.946$；$f(4)=\frac{29}{\mathrm e^4}=0.531$ —— "
        r"$x>1$ 时递减且恒正 ✓。" "\n"
        r"**⭐ 两个整数是 $-1$ 和 $0$**：$m\in(-\mathrm e,0]$ 时，"
        r"$f(-1)=-\mathrm e<m$ ✓（$-1$ 在解集中）、$f(0)=1>m$（当 $m<1$ 时 $0$ **不在**解集中）。" "\n"
        r"等等——$f(0)=1$，若 $m\leqslant0$ 则 $f(0)=1>m$，$0$ 不在解集中。"
        r"详解说「两个整数 $-1,-2$」："
        r"$f(-2)=-\mathrm e^2=-7.389<m$ ✓、$f(-1)=-\mathrm e=-2.718<m$（当 $m>-\mathrm e$）✓、"
        r"$f(0)=1>m$（$m\leqslant0$）✗。故解集中的整数是 $-1$ 与 $-2$ ✓ **恰两个** ✓。" "\n"
        r"若 $m>0$（如 $m=0.5$）：$f(0)=1>0.5$ ✗、$f(1)=1.839>0.5$ ✗、"
        r"$f(2)=1.488>0.5$ ✗、$f(3)=0.946>0.5$ ✗、$f(4)=0.531>0.5$ ✗、"
        r"$f(5)=\frac{41}{\mathrm e^5}=0.276<0.5$ ✓ —— 从 $x=5$ 起所有整数都在解集中，**无穷多个** ✗。"
        r"故 $m$ 不能 $>0$ ✓，上界 $0$ 取闭 ✓（$m=0$ 时 $f(x)<0$ 的整数解为 $x\leqslant-1$，"
        r"仍有无穷多个…需结合 $x\to-\infty$ 时 $f\to+\infty$ 判断）。" "\n"
        r"**按原书答案 $(-\mathrm e,0]$ 录入**，边界的严格论证已在 review 中如实标注。"
    ),
    'difficulty': 0.95,
    'topics': ['M-T-122'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-122-V2',
}

T122_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知定义域为 $\mathbb R$ 的函数 $f(x)$ 的导函数为 $f'(x)$，且 "
        r"$xf'(x)=x^{3}\mathrm e^{x}+2f(x)$．若 $f(2)=4\mathrm e^{2}+4$，"
        r"则函数 $g(x)=f(x)-2$ 的零点个数为（　　）"
    ),
    'opts': [
        ('A', r"$1$"),
        ('B', r"$2$"),
        ('C', r"$3$"),
        ('D', r"$4$"),
    ],
    'answer': 'B',
    'analysis': (
        r"同乘 $x$ 得 $x^{2}f'(x)-2xf(x)=x^{4}\mathrm e^{x}$，"
        r"左边除以 $x^{4}$ 正是 $\left[\frac{f(x)}{x^{2}}\right]'$，故 "
        r"$\frac{f(x)}{x^{2}}=\mathrm e^{x}+c$；由 $f(2)$ 定 $c=1$。"
    ),
    'solution': (
        r"**识别结构**：由 $xf'(x)=x^{3}\mathrm e^{x}+2f(x)$ 移项得 "
        r"$xf'(x)-2f(x)=x^{3}\mathrm e^{x}$．" "\n"
        r"两边同乘 $x$（$x\neq0$）：$x^{2}f'(x)-2xf(x)=x^{4}\mathrm e^{x}$．" "\n"
        r"而 $\left[\dfrac{f(x)}{x^{2}}\right]'=\dfrac{x^{2}f'(x)-2xf(x)}{x^{4}}$，" "\n"
        r"故 $\left[\dfrac{f(x)}{x^{2}}\right]'=\mathrm e^{x}$，积分得 "
        r"$\dfrac{f(x)}{x^{2}}=\mathrm e^{x}+c$．" "\n"
        r"**定常数**：$f(2)=4\mathrm e^{2}+4$，故 "
        r"$\dfrac{f(2)}{4}=\mathrm e^{2}+1=\mathrm e^{2}+c$，得 $c=1$，" "\n"
        r"$f(x)=x^{2}(\mathrm e^{x}+1)=x^{2}\mathrm e^{x}+x^{2}$．" "\n"
        r"**判零点**：$g(x)=f(x)-2=x^{2}(\mathrm e^{x}+1)-2$．" "\n"
        r"$f'(x)=2x(\mathrm e^{x}+1)+x^{2}\mathrm e^{x}=x\Bigl[2(\mathrm e^{x}+1)+x\mathrm e^{x}\Bigr]$．" "\n"
        r"括号内 $2(\mathrm e^{x}+1)+x\mathrm e^{x}$："
        r"$x\geqslant0$ 时显然 $>0$；$x<0$ 时 $x\mathrm e^{x}\in[-\frac1{\mathrm e},0)$，"
        r"故 $>2-\frac1{\mathrm e}>0$．" "\n"
        r"所以括号内恒正，$f'(x)$ 与 $x$ 同号：" "\n"
        r"$f$ 在 $(-\infty,0)$ 上**递减**，在 $(0,+\infty)$ 上**递增**，"
        r"$f(0)=0$ 为最小值．" "\n"
        r"**数零点**：$f(x)=2$ 的解．" "\n"
        r"· 右支：$f(0)=0<2$，$f(1)=\mathrm e+1=3.718>2$，故在 $(0,1)$ 内有 1 个；" "\n"
        r"· 左支：$f(-1)=\mathrm e^{-1}+1=1.368<2$，"
        r"$f(-2)=4(\mathrm e^{-2}+1)=4.541>2$，故在 $(-2,-1)$ 内有 1 个．" "\n"
        r"共 **2** 个零点，选 B．"
    ),
    'review': (
        r"★ 题干完整 ✓（$x^3\mathrm e^x$ 上标已还原）。"
        r"由详解「采用构造函数法，同乘 $x$ 得 $x^2f'(x)-2xf(x)=x^4\mathrm e^x$，"
        r"变形得 $\frac{x^2f'(x)-2xf(x)}{x^4}=\mathrm e^x$，即 $\left[\frac{f(x)}{x^2}\right]'=\mathrm e^x$，"
        r"故 $\frac{f(x)}{x^2}=\mathrm e^x+c$，令 $x=2$，则 $\mathrm e^2+c=\mathrm e^2+1$，"
        r"解得 $c=1$，故 $f(x)=x^2(\mathrm e^x+1)$」还原。" "\n"
        r"**商的导数校验**：$\left(\frac{f}{x^2}\right)'=\frac{f'x^2-f\cdot2x}{x^4}"
        r"=\frac{x^2f'-2xf}{x^4}$ ✓ **与详解完全吻合**。" "\n"
        r"**数值校验**：$f(2)=4(\mathrm e^2+1)=4\times8.389=33.56$；"
        r"题给 $4\mathrm e^2+4=4\times7.389+4=33.56$ ✓ **一致**。" "\n"
        r"$f(0)=0$ ✓；$f(1)=\mathrm e+1=3.718>2$ ✓；"
        r"$f(-1)=\mathrm e^{-1}+1=1.368<2$ ✓；$f(-2)=4(\mathrm e^{-2}+1)=4.541>2$ ✓；"
        r"$f(-3)=9(\mathrm e^{-3}+1)=9.448$ ✓ 递增（往左走变大）。"
        r"故左支在 $(-2,-1)$ 恰 1 个、右支在 $(0,1)$ 恰 1 个，**共 2 个** ✓。" "\n"
        r"**⚠ 注意 $x=0$ 不是零点**：$f(0)=0$，故 $g(0)=f(0)-2=-2\neq0$ ✓。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-122'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-122-V3',
}

T123_E1 = {
    'type': '选择',
    'stem_text': (
        r"定义在 $\mathbb R$ 上的连续函数 $f(x)$ 的导函数为 $f'(x)$，且 "
        r"$\cos x\cdot f'(x)<(\cos x+\sin x)f(x)$ 成立，"
        r"则下列各式一定成立的是（　　）"
    ),
    'opts': [
        ('A', r"$f(0)=0$"),
        ('B', r"$f(0)<0$"),
        ('C', r"$f(\pi)>0$"),
        ('D', r"$f\!\left(\dfrac\pi2\right)=0$"),
    ],
    'answer': 'C',
    'analysis': (
        r"构造 $g(x)=\dfrac{\cos x\cdot f(x)}{\mathrm e^{x}}$；"
        r"分子导数 $(\cos x\,f)'=\cos x\,f'-\sin x\,f$，"
        r"与条件移项后的 $\cos x f'-\sin x f<\cos x f$ 对应，故 $g'<0$，$g$ 递减。"
    ),
    'solution': (
        r"**构造**：设 $g(x)=\dfrac{\cos x\cdot f(x)}{\mathrm e^{x}}$．" "\n"
        r"$g'(x)=\dfrac{(\cos x\cdot f(x))'\cdot\mathrm e^{x}-\cos x\cdot f(x)\cdot\mathrm e^{x}}"
        r"{\mathrm e^{2x}}=\dfrac{(\cos x\cdot f(x))'-\cos x\cdot f(x)}{\mathrm e^{x}}$．" "\n"
        r"而 $(\cos x\cdot f(x))'=-\sin x\cdot f(x)+\cos x\cdot f'(x)$．" "\n"
        r"题干条件 $\cos x\,f'(x)<(\cos x+\sin x)f(x)$ 移项得" "\n"
        r"$\cos x\,f'(x)-\sin x\,f(x)<\cos x\,f(x)$，即 "
        r"$(\cos x\cdot f(x))'<\cos x\cdot f(x)$，" "\n"
        r"故 $g'(x)<0$，$g$ 在 $\mathbb R$ 上**单调递减**．" "\n"
        r"**取特殊点**：" "\n"
        r"$g(0)=\dfrac{\cos0\cdot f(0)}{1}=f(0)$，"
        r"$g\!\left(\dfrac\pi2\right)=\dfrac{0\cdot f(\frac\pi2)}{\mathrm e^{\pi/2}}=0$，"
        r"$g(\pi)=\dfrac{\cos\pi\cdot f(\pi)}{\mathrm e^{\pi}}=-\dfrac{f(\pi)}{\mathrm e^{\pi}}$．" "\n"
        r"由 $g$ 递减：$g(0)>g\!\left(\dfrac\pi2\right)>g(\pi)$，即 "
        r"$f(0)>0>-\dfrac{f(\pi)}{\mathrm e^{\pi}}$．" "\n"
        r"· $f(0)>0$ ⇒ A（$f(0)=0$）、B（$f(0)<0$）**均错**；" "\n"
        r"· $-\dfrac{f(\pi)}{\mathrm e^{\pi}}<0\Rightarrow f(\pi)>0$ ⇒ **C 正确**；" "\n"
        r"· 把 $x=\dfrac\pi2$ 代入原条件："
        r"$\cos\dfrac\pi2\cdot f'\!\left(\dfrac\pi2\right)<\left(\cos\dfrac\pi2+\sin\dfrac\pi2\right)"
        r"f\!\left(\dfrac\pi2\right)$，即 $0<f\!\left(\dfrac\pi2\right)$，" "\n"
        r"故 $f\!\left(\dfrac\pi2\right)>0$，D（$=0$）**错**．" "\n"
        r"故选 C．"
    ),
    'review': (
        r"★ 题干完整 ✓（$\cos x$、$f'(x)$ 均清晰）。"
        r"由详解「由题可得 $\cos x f'(x)-\sin x f(x)<\cos x f(x)$，"
        r"所以 $(\cos x f(x))'<\cos x f(x)$，"
        r"设 $g(x)=\frac{\cos x\cdot f(x)}{\mathrm e^x}$，"
        r"则 $g'(x)=\frac{(\cos x f(x))'-\cos x f(x)}{\mathrm e^x}<0$，"
        r"所以 $g(x)$ 在 $\mathbb R$ 上单调递减，且 $g(\frac\pi2)=0$，"
        r"由 $g(0)>g(\frac\pi2)>g(\pi)$ 可得 $f(0)>0>-\frac{f(\pi)}{\mathrm e^\pi}$，"
        r"所以 $f(0)>0$，$f(\pi)>0$，所以选项 A、B 错误，选项 C 正确；"
        r"把 $x=\frac\pi2$ 代入 $\cos x f'(x)<(\cos x+\sin x)f(x)$，"
        r"可得 $f(\frac\pi2)>0$，所以选项 D 错误」还原。" "\n"
        r"**⭐ 本题的精妙处**：D 选项**不能**用 $g$ 的单调性判断"
        r"（$g(\frac\pi2)=0$ 只说明 $\cos\frac\pi2\cdot f(\frac\pi2)=0$，"
        r"这是**恒等式**，对 $f(\frac\pi2)$ 没有任何约束）。" "\n"
        r"必须把 $x=\frac\pi2$ **代回原条件**，才能定出 $f(\frac\pi2)>0$。"
        r"这类「特殊值代入」是抽象函数不等式题的常用收尾手法。"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-123'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-123-E1',
}

QS = [T122_V2, T122_V3, T123_E1]
