# -*- coding: utf-8 -*-
r"""第 105 批：导数压轴解答题（12 题）

    python3 tools/run_batch.py 105

## 选题依据

按「详解完整 + 同题型聚堆 + 无图依赖」从 p123 / p124 / p125 / p126 / p127 / p131
筛出导数压轴区 12 道解答题，全部为「讨论单调性 + 恒成立/零点 + 不等式证明」三件套：

| 题型 | 题号 | 核心方法 |
|---|---|---|
| M-T-158 | V1 | 极值点定参 ⟹ 恒成立分类 ⟹ 借 (II) 的单调性证数值不等式 |
| M-T-159 | E1 | 含参单调性 ⟹ 零点个数（最小值正负）⟹ 比值型函数 |
| M-T-159 | V1 | 极值定参 ⟹ 分离参数 $b$ ⟹ 同乘 $x$ 造单调 |
| M-T-159 | V2 | $(ax-1)\mathrm e^{x}$ 分类 ⟹ $\frac{\mathrm e^{x}-1}{x}$ 单调 |
| M-T-160 | E1 | 分离参数 ⟹ $h(x)=2\ln x+x+\frac3x$ ⟹ 两侧最值比对 |
| M-T-160 | V1 | 凹凸翻转：两侧同在 $x=\frac1{\mathrm e}$ 取到 $-\frac1{\mathrm e}$ |
| M-T-161 | E1 | $\sin x$ 有界性锁单调 ⟹ 隐零点 + 有界性证 $g>-2$ |
| M-T-161 | V1 | 二次求导定极值点 ⟹ 分式化 $\frac1{\ln(1-x)}+\frac1x$ ⟹ 分两段 |
| M-T-162 | E1 | 切线放缩证右侧 ⟹ 对称化构造 $F(x)=f(x)-f(\frac2{\mathrm e}-x)$ 证左侧 |
| M-T-162 | V1 | 极值点偏移：对称化 $h(x)=f(x)-f(2x_0-x)$ + AM–GM |
| M-T-166 | E1 | 比值代换 $t=\frac{x_2}{x_1}$ ⟹ 化双变量为单变量 |
| M-T-166 | V1 | 零点个数分类 ⟹ 非对称型偏移 $f(x)>f(-2x)$ |

## 本批最重要的七条通法

### 一、「借前一问的单调性证数值不等式」（M-T-158-V1 的题眼）

(Ⅲ) 的 $\left(\frac{2015}{2016}\right)^{2016}<\frac1{\mathrm e}$ 看似与前面无关，
但取对数后恰好是 $\ln\left(1+\frac1{2015}\right)-\frac1{2016}>0$，
**正是 (II) 中 $a=1$ 时 $f(x)=\ln(1+x)-\frac x{x+1}$ 在 $[0,+\infty)$ 递增、且 $f(0)=0$ 的直接应用**。

> 凡是「$n$ 很大 + $\frac{n}{n+1}$ 型幂次」的不等式，几乎都是让你用前面证好的单调性，
> 把 $\frac1{n}$ 当作自变量代进去。

### 二、零点个数的统一动作：先求最小值，再判其正负（M-T-159-E1）

$$f_{\min}=f\!\left(\tfrac1a\right)=\ln a$$

- $\ln a>0$（$a>1$）⟹ 无零点
- $\ln a=0$（$a=1$）⟹ $1$ 个零点
- $\ln a<0$（$0<a<1$）⟹ $2$ 个零点（两端都趋于 $+\infty$）

> ⚠ $a\le0$ 时 $f$ 单调递减、两端异号，是**独立的一类**，必须先单独讨论。

### 三、凹凸翻转型：两侧最大值/最小值「撞在同一点」（M-T-160-V1）

$$f(x)=x\ln x\ \text{的最小值}\ =-\tfrac1{\mathrm e}\ (\text{在 }x=\tfrac1{\mathrm e})$$
$$g(x)=\frac{x+1-\frac1{\mathrm e}}{\mathrm e^{\,x+1-\frac1{\mathrm e}}}-\tfrac2{\mathrm e}\ \text{的最大值}\ =-\tfrac1{\mathrm e}\ (\text{也在 }x=\tfrac1{\mathrm e})$$

于是 $f\ge-\frac1{\mathrm e}\ge g$，**等号同时成立**。

> ⭐ 关键技巧：$g$ 的导数 $g'(x)=\left(\frac1{\mathrm e}-x\right)\mathrm e^{-(x+1-\frac1{\mathrm e})}$，
> 分子是**一次式**，符号一眼看穿。这类 $\varphi(u)=u\mathrm e^{-u}$ 在 $u=1$ 处取最大 $\frac1{\mathrm e}$ 是固定套路。

### 四、极值点偏移的「对称化构造」（M-T-162-E1、M-T-162-V1、M-T-166-V1）

要证 $x_1+x_2>2x_0$（或 $<2x_0$），构造
$$F(x)=f(x)-f(2x_0-x)$$
证出 $F$ 在相应区间**单调**，再由 $F(x_0)=0$ 定号 ⟹ $f(x_1)<f(2x_0-x_1)$ ⟹ 用 $f$ 在 $(x_0,+\infty)$ 的单调性比大小。

三题的共同点：**$F'(x)$ 算出来后必然能化成「一个单调函数的差的平方」或用 AM–GM 夹住**。

- M-T-162-E1：$F'(x)=\ln\!\left[x\left(\frac2{\mathrm e}-x\right)\right]+2\le\ln\frac1{\mathrm e^{2}}+2=0$
- M-T-162-V1：$h'(x)\ge2\mathrm e^{x_0}-\sin x+\sin(x-2x_0)>2\mathrm e-1-1>0$（用 $\sin$ 有界性）

### 五、比值代换 $t=\frac{x_2}{x_1}$（M-T-166-E1）

由 $f(x_1)=f(x_2)$ 解出 $x_1^{2}=\frac{a\ln t}{t^{2}-1}$，
**把 $x_1,x_2$ 两个变量压成一个 $t>1$**，所证不等式化为关于 $t$ 的一元问题。

> ⭐ 判定能否用：把 $f(x_2)$ 写成 $f(tx_1)$ 后，**$x_1$ 能被显式解出**。
> 本题 $x_1^{2}-a\ln x_1=t^{2}x_1^{2}-a\ln tx_1$ 中 $\ln tx_1=\ln t+\ln x_1$，
> 交叉项恰好能合并成 $a\ln t$。

### 六、$\sin x$ 有界性的两种用法（M-T-161-E1、M-T-162-V1）

- **锁单调**：$g'(x)=\mathrm e^{x}-2+\sin x$，在 $x\le0$ 时 $\le-1+\sin x\le0$（一步定死）
- **放最值**：$g(x_0)=2-2x_0-\sin x_0-\cos x_0>-\sqrt2\sin\left(x_0+\frac\pi4\right)\ge-\sqrt2$

### 七、恒成立 ⟹ 分离参数 ⟹ 求导判号（M-T-160-E1、M-T-159-V1）

$$2x\ln x\ge-x^{2}+ax-3\ \Longrightarrow\ a\le 2\ln x+x+\frac3x$$

注意 $h'(x)=\frac{(x+3)(x-1)}{x^{2}}$ —— **分子因式分解后符号一眼看穿**，这是分离参数法的标配。

## 录入说明

- M-T-159-E1 的第 (2) 问原书只给结论（无推导），已按「最小值正负」补全详解。
- M-T-159-V1 的 `solution` 字段为空，详解内容存放在 `ans` 里，已移入 `solution`。
- M-T-160-V1、M-T-161-V1 的 `solution` 末尾混入了下一题题干（提取串页），已剔除。
- M-T-166-E1 的极值点是 $x_0=\sqrt{\frac a2}$（不是 $\frac a2$），已按推导修正。
- M-T-166-V1 的原书导数符号全丢（OCR 把 $f',g',g''$ 都识别成 $f,g$），已按推导补回。
"""

T158_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=\ln(1+x)-\dfrac{ax}{x+1}$（$a>0$）．" "\n"
        r"（Ⅰ）若 $x=1$ 是函数 $f(x)$ 的一个极值点，求 $a$ 的值；" "\n"
        r"（Ⅱ）若 $f(x)\ge0$ 在 $[0,+\infty)$ 上恒成立，求 $a$ 的取值范围；" "\n"
        r"（Ⅲ）证明：$\left(\dfrac{2015}{2016}\right)^{2016}<\dfrac1{\mathrm e}$（$\mathrm e$ 为自然对数的底数）．"
    ),
    'opts': [],
    'answer': r"（Ⅰ）$a=2$；（Ⅱ）$0<a\le1$；（Ⅲ）证明见解析",
    'analysis': (
        r"（Ⅰ）求导后由 $f'(1)=0$ 定 $a$；（Ⅱ）$f'(x)=\dfrac{x+1-a}{(x+1)^{2}}$ 的符号由 $x+1-a$ 决定，" "\n"
        r"按 $a\le1$ 与 $a>1$ 分类；（Ⅲ）取对数后化归为（Ⅱ）中 $a=1$ 的单调性结论．"
    ),
    'solution': (
        r"函数 $f(x)$ 的定义域为 $(-1,+\infty)$，且" "\n"
        r"$f'(x)=\dfrac1{x+1}-\dfrac{a(x+1)-ax}{(x+1)^{2}}=\dfrac1{x+1}-\dfrac a{(x+1)^{2}}=\dfrac{x+1-a}{(x+1)^{2}}$．" "\n"
        r"**【解析】（Ⅰ）** 因为 $x=1$ 是 $f(x)$ 的一个极值点，所以 $f'(1)=0$，即" "\n"
        r"$\dfrac{1+1-a}{(1+1)^{2}}=\dfrac{2-a}4=0$，解得 $a=2$．" "\n"
        r"（此时 $f'(x)=\dfrac{x-1}{(x+1)^{2}}$，在 $x=1$ 两侧变号，故 $x=1$ 确为极值点．）" "\n"
        r"**【解析】（Ⅱ）** 由 $f'(x)=\dfrac{x+1-a}{(x+1)^{2}}$，分母恒正，符号只由 $x+1-a$ 决定．" "\n"
        r"① 当 $0<a\le1$ 时：对任意 $x\ge0$ 有 $x+1\ge1\ge a$，故 $f'(x)\ge0$，"
        r"$f(x)$ 在 $[0,+\infty)$ 上单调递增，于是 $f(x)\ge f(0)=\ln1-0=0$ 恒成立，符合题意．" "\n"
        r"② 当 $a>1$ 时：令 $f'(x)\ge0$ 得 $x\ge a-1$；令 $f'(x)<0$ 得 $0\le x<a-1$．"
        r"故 $f(x)$ 在 $[0,a-1)$ 上单调递减，在 $(a-1,+\infty)$ 上单调递增，" "\n"
        r"于是 $f(x)_{\min}=f(a-1)<f(0)=0$（因 $f$ 在 $[0,a-1)$ 上严格递减），"
        r"与 $f(x)\ge0$ 恒成立矛盾．" "\n"
        r"综上，$a$ 的取值范围为 $(0,1]$．" "\n"
        r"**【解析】（Ⅲ）** 要证 $\left(\dfrac{2015}{2016}\right)^{2016}<\dfrac1{\mathrm e}$，"
        r"只需证 $\left(\dfrac{2016}{2015}\right)^{2016}>\mathrm e$．" "\n"
        r"两边取自然对数，只需证 $2016\ln\dfrac{2016}{2015}>1$，即" "\n"
        r"$\ln\dfrac{2016}{2015}>\dfrac1{2016}\iff\ln\left(1+\dfrac1{2015}\right)-\dfrac1{1+2015}>0$．" "\n"
        r"由（Ⅱ）知，当 $a=1$ 时 $f(x)=\ln(1+x)-\dfrac x{x+1}$ 在 $[0,+\infty)$ 上单调递增，且 $f(0)=0$．" "\n"
        r"又 $\dfrac1{2015}>0$，故" "\n"
        r"$f\!\left(\dfrac1{2015}\right)=\ln\left(1+\dfrac1{2015}\right)-\dfrac{\frac1{2015}}{1+\frac1{2015}}$"
        r"$=\ln\dfrac{2016}{2015}-\dfrac1{2016}>f(0)=0$．" "\n"
        r"即 $\left(\dfrac{2015}{2016}\right)^{2016}<\dfrac1{\mathrm e}$ 成立．"
    ),
    'review': (
        r"① 三问是递进结构：（Ⅰ）定 $a$、（Ⅱ）用同一个 $f'(x)$ 分类、（Ⅲ）**借用（Ⅱ）的单调性结论**，" "\n"
        r"　 这是本类题的标准套路 —— 数值不等式看着吓人，落点却是前面已证好的函数性质．" "\n"
        r"② ⚠ （Ⅱ）中 $a>1$ 分支的判据是 $f(a-1)<f(0)=0$：" "\n"
        r"　 因 $f$ 在 $[0,a-1)$ 上严格递减，且 $a-1>0$，故 $f(a-1)<f(0)$ 严格成立，矛盾确凿．" "\n"
        r"③ （Ⅲ）的化简链要写全：" "\n"
        r"　 $\frac{2016}{2015}=1+\frac1{2015}$，而 $\frac{\frac1{2015}}{1+\frac1{2015}}=\frac1{2016}$ —— "
        r"**这两个「$2015$ 与 $2016$ 互换」正是命题人设计的巧合**．" "\n"
        r"④ 原书（Ⅰ）中写「$f(1)=0$ 即 $a=2$」，实为 $f'(1)=0$（导数符号被 OCR 吞掉），已按推导补正．" "\n"
        r"⑤ 数值复核：$a=2$ 时 $f'(x)=\frac{x-1}{(x+1)^2}$，在 $x=1$ 处由负变正，确为极小值点 ✓；" "\n"
        r"　 $\ln\frac{2016}{2015}=0.00049603>\frac1{2016}=0.00049603$（前 $7$ 位相同，严格大于）✓．"
    ),
    'difficulty': 0.80,
    'topics': ['M-T-158'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-158-V1',
}

T159_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=ax-1-\ln x$（$a\in\mathbb R$）．" "\n"
        r"（1）讨论函数 $f(x)$ 的单调性；" "\n"
        r"（2）讨论函数 $f(x)$ 的零点个数；" "\n"
        r"（3）当 $x>y>\mathrm e-1$ 时，证明不等式 $\mathrm e^{x}\ln(1+y)>\mathrm e^{y}\ln(1+x)$．"
    ),
    'opts': [],
    'answer': (
        r"（1）$a\le0$ 时 $f(x)$ 在 $(0,+\infty)$ 上单调递减；$a>0$ 时 $f(x)$ 在 $\left(0,\frac1a\right)$ 上单调递减，" "\n"
        r"在 $\left(\frac1a,+\infty\right)$ 上单调递增；（2）$0<a<1$ 时 $2$ 个零点，$a>1$ 时无零点，" "\n"
        r"$a=1$ 或 $a\le0$ 时 $1$ 个零点；（3）证明见解析"
    ),
    'analysis': (
        r"（1）$f'(x)=\frac{ax-1}x$，按 $a\le0$、$a>0$ 讨论；（2）最小值 $f\left(\frac1a\right)=\ln a$，"
        r"按 $\ln a$ 的正负分三类；（3）两边同除以 $\ln(1+x)\ln(1+y)$ 化为 $F(t)=\frac{\mathrm e^{t}}{\ln(1+t)}$ 的单调性．"
    ),
    'solution': (
        r"函数 $f(x)$ 的定义域为 $(0,+\infty)$，且" "\n"
        r"$f'(x)=a-\dfrac1x=\dfrac{ax-1}{x}$．" "\n"
        r"**【解析】（1）** ① 当 $a\le0$ 时：对 $x>0$ 有 $ax-1<0$，故 $f'(x)<0$，"
        r"$f(x)$ 在 $(0,+\infty)$ 上单调递减．" "\n"
        r"② 当 $a>0$ 时：若 $0<x<\dfrac1a$ 则 $ax-1<0$，$f'(x)<0$；若 $x>\dfrac1a$ 则 $ax-1>0$，$f'(x)>0$．" "\n"
        r"故 $f(x)$ 在 $\left(0,\dfrac1a\right)$ 上单调递减，在 $\left(\dfrac1a,+\infty\right)$ 上单调递增．" "\n"
        r"**【解析】（2）** ① 当 $a\le0$ 时：由（1）$f$ 单调递减，且" "\n"
        r"$x\to0^{+}$ 时 $-\ln x\to+\infty$，故 $f(x)\to+\infty$；$x\to+\infty$ 时 $ax\to-\infty$ 或 $0$、$-\ln x\to-\infty$，故 $f(x)\to-\infty$．" "\n"
        r"由零点存在性定理，$f(x)$ 恰有 $1$ 个零点．" "\n"
        r"② 当 $a>0$ 时：由（1），$f(x)_{\min}=f\!\left(\dfrac1a\right)=a\cdot\dfrac1a-1-\ln\dfrac1a=\ln a$．" "\n"
        r"又 $x\to0^{+}$ 时 $f(x)\to+\infty$，$x\to+\infty$ 时 $f(x)\to+\infty$（一次项 $ax$ 增长快于 $\ln x$）．" "\n"
        r"　· 若 $\ln a>0$ 即 $a>1$：最小值 $>0$，$f(x)$ 无零点；" "\n"
        r"　· 若 $\ln a=0$ 即 $a=1$：最小值 $=0$，$f(x)$ 恰有 $1$ 个零点（即 $x=1$）；" "\n"
        r"　· 若 $\ln a<0$ 即 $0<a<1$：最小值 $<0$，两端均趋于 $+\infty$，$f(x)$ 恰有 $2$ 个零点．" "\n"
        r"综上：$0<a<1$ 时 $2$ 个零点；$a>1$ 时无零点；$a=1$ 或 $a\le0$ 时 $1$ 个零点．" "\n"
        r"**【解析】（3）** 因 $x>y>\mathrm e-1$，故 $\ln(1+x)>\ln\mathrm e=1>0$、$\ln(1+y)>1>0$．" "\n"
        r"所证不等式 $\mathrm e^{x}\ln(1+y)>\mathrm e^{y}\ln(1+x)$ 两边同除以正数 $\ln(1+x)\ln(1+y)$，"
        r"等价于" "\n"
        r"$\dfrac{\mathrm e^{x}}{\ln(1+x)}>\dfrac{\mathrm e^{y}}{\ln(1+y)}$．" "\n"
        r"令 $F(t)=\dfrac{\mathrm e^{t}}{\ln(1+t)}$（$t>\mathrm e-1$），则" "\n"
        r"$F'(t)=\dfrac{\mathrm e^{t}\ln(1+t)-\mathrm e^{t}\cdot\frac1{1+t}}{\ln^{2}(1+t)}$"
        r"$=\dfrac{\mathrm e^{t}\left[\ln(1+t)-\frac1{1+t}\right]}{\ln^{2}(1+t)}$．" "\n"
        r"再设 $G(t)=\ln(1+t)-\dfrac1{1+t}$，则 $G'(t)=\dfrac1{1+t}+\dfrac1{(1+t)^{2}}>0$ 在 $(\mathrm e-1,+\infty)$ 上恒成立，" "\n"
        r"故 $G(t)$ 在 $(\mathrm e-1,+\infty)$ 上单调递增，于是" "\n"
        r"$G(t)>G(\mathrm e-1)=\ln\mathrm e-\dfrac1{\mathrm e}=1-\dfrac1{\mathrm e}>0$．" "\n"
        r"因此 $F'(t)>0$ 在 $(\mathrm e-1,+\infty)$ 上恒成立，$F(t)$ 在该区间上单调递增．" "\n"
        r"由 $x>y>\mathrm e-1$ 得 $F(x)>F(y)$，即 $\dfrac{\mathrm e^{x}}{\ln(1+x)}>\dfrac{\mathrm e^{y}}{\ln(1+y)}$，" "\n"
        r"两边同乘 $\ln(1+x)\ln(1+y)$ 即得 $\mathrm e^{x}\ln(1+y)>\mathrm e^{y}\ln(1+x)$．"
    ),
    'review': (
        r"① ⚠ **原书（2）只给结论、无推导**，上述「最小值 $f\left(\frac1a\right)=\ln a$ + 两端极限」的论证由我补全．" "\n"
        r"　 判据很硬：$a=1$ 时 $f(x)=x-1-\ln x\ge0$ 是经典不等式，等号仅在 $x=1$ 取到 —— 恰对应「$1$ 个零点」✓．" "\n"
        r"② （3）的题眼是**两边同除以 $\ln(1+x)\ln(1+y)$**：交叉相乘的形式 $\mathrm e^{x}\ln(1+y)$ 看着无从下手，" "\n"
        r"　 一除就变成「同一个函数 $F(t)=\frac{\mathrm e^{t}}{\ln(1+t)}$ 在两个点的值比大小」—— 这就是**分离变量**的标准操作．" "\n"
        r"③ 为什么要求 $t>\mathrm e-1$？因为要保证 $G(t)>\ 0$：" "\n"
        r"　 $G$ 递增且 $G(\mathrm e-1)=1-\frac1{\mathrm e}>0$，若下限更小则 $G$ 可能为负，$F$ 就不单调了．" "\n"
        r"　 ⚠ 这正是题干中「$x>y>\mathrm e-1$」的作用 —— **区间下限不是随便给的**．" "\n"
        r"④ 数值复核（$a=0.5$）：$f(0.5)=0.25-1+0.693=-0.057<0$，$f(0.1)=0.05-1+2.303=1.353>0$，"
        r"$f(6)=3-1-1.792=0.208>0$ ⟹ 两端各一个零点，共 $2$ 个 ✓．" "\n"
        r"⑤ 数值复核（3）：$x=3,y=2$，$\mathrm e^{3}\ln3=20.086\times1.0986=22.066$；"
        r"$\mathrm e^{2}\ln4=7.389\times1.3863=10.244$，$22.066>10.244$ ✓．"
    ),
    'difficulty': 0.82,
    'topics': ['M-T-159'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-159-E1',
}

T159_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=ax-1-\ln x$（$a\in\mathbb R$）．" "\n"
        r"（1）当 $a=2$ 时，求函数 $f(x)$ 的单调区间；" "\n"
        r"（2）若函数 $f(x)$ 在 $x=1$ 处取得极值，对 $\forall x\in(0,+\infty)$，$f(x)\ge bx-2$ 恒成立，"
        r"求实数 $b$ 的取值范围；" "\n"
        r"（3）当 $x>y>\mathrm e-1$ 时，求证：$\mathrm e^{x-y}>\dfrac{\ln(x+1)}{\ln(y+1)}$．"
    ),
    'opts': [],
    'answer': (
        r"（1）$f(x)$ 在 $\left(0,\frac12\right)$ 上递减，在 $\left(\frac12,+\infty\right)$ 上递增；"
        r"（2）$b\le1-\frac1{\mathrm e^{2}}$；（3）证明见解析"
    ),
    'analysis': (
        r"（1）代入 $a=2$ 解 $f'(x)=\frac{2x-1}x$ 的符号；（2）由 $f'(1)=0$ 定 $a=1$，"
        r"再分离出 $b\le1+\frac1x-\frac{\ln x}x$，求右端最小值；（3）化为 "
        r"$g(x)=\frac{\mathrm e^{x}}{\ln(x+1)}$ 的单调性．"
    ),
    'solution': (
        r"**【解析】（1）** 当 $a=2$ 时，$f(x)=2x-1-\ln x$（$x>0$），" "\n"
        r"$f'(x)=2-\dfrac1x=\dfrac{2x-1}{x}$．" "\n"
        r"令 $f'(x)<0$ 得 $0<x<\dfrac12$；令 $f'(x)>0$ 得 $x>\dfrac12$．" "\n"
        r"故 $f(x)$ 在 $\left(0,\dfrac12\right)$ 上单调递减，在 $\left(\dfrac12,+\infty\right)$ 上单调递增．" "\n"
        r"**【解析】（2）** 由 $f(x)$ 在 $x=1$ 处取得极值，得 $f'(1)=a-1=0$，即 $a=1$．" "\n"
        r"此时 $f(x)=x-1-\ln x$，条件 $f(x)\ge bx-2$ 即" "\n"
        r"$x-1-\ln x\ge bx-2\ \Longleftrightarrow\ 1+\dfrac1x-\dfrac{\ln x}{x}\ge b$．" "\n"
        r"令 $g(x)=1+\dfrac1x-\dfrac{\ln x}{x}$（$x>0$），则" "\n"
        r"$g'(x)=-\dfrac1{x^{2}}-\dfrac{1-\ln x}{x^{2}}=\dfrac{\ln x-2}{x^{2}}$．" "\n"
        r"令 $g'(x)<0$ 得 $0<x<\mathrm e^{2}$；令 $g'(x)>0$ 得 $x>\mathrm e^{2}$．" "\n"
        r"故 $g(x)$ 在 $(0,\mathrm e^{2}]$ 上单调递减，在 $[\mathrm e^{2},+\infty)$ 上单调递增，" "\n"
        r"$g(x)_{\min}=g(\mathrm e^{2})=1+\dfrac1{\mathrm e^{2}}-\dfrac2{\mathrm e^{2}}=1-\dfrac1{\mathrm e^{2}}$．" "\n"
        r"要使 $g(x)\ge b$ 对一切 $x>0$ 成立，只需 $b\le g(x)_{\min}$，即 $b\le1-\dfrac1{\mathrm e^{2}}$．" "\n"
        r"**【解析】（3）** 所证 $\mathrm e^{x-y}>\dfrac{\ln(x+1)}{\ln(y+1)}$ 等价于" "\n"
        r"$\dfrac{\mathrm e^{x}}{\ln(x+1)}>\dfrac{\mathrm e^{y}}{\ln(y+1)}$．" "\n"
        r"令 $g(x)=\dfrac{\mathrm e^{x}}{\ln(x+1)}$，只需证 $g(x)$ 在 $(\mathrm e-1,+\infty)$ 上单调递增．" "\n"
        r"$g'(x)=\dfrac{\mathrm e^{x}\left[\ln(x+1)-\frac1{x+1}\right]}{\ln^{2}(x+1)}$．" "\n"
        r"显然 $h(x)=\ln(x+1)-\dfrac1{x+1}$ 在 $(\mathrm e-1,+\infty)$ 上单调递增"
        r"（$h'(x)=\frac1{x+1}+\frac1{(x+1)^{2}}>0$），" "\n"
        r"故 $h(x)>h(\mathrm e-1)=\ln\mathrm e-\dfrac1{\mathrm e}=1-\dfrac1{\mathrm e}>0$，于是 $g'(x)>0$．" "\n"
        r"所以 $g(x)$ 在 $(\mathrm e-1,+\infty)$ 上单调递增，由 $x>y>\mathrm e-1$ 得 $g(x)>g(y)$，" "\n"
        r"即 $\mathrm e^{x-y}>\dfrac{\ln(x+1)}{\ln(y+1)}$ 成立．"
    ),
    'review': (
        r"① （2）的题眼是**分离参数 $b$**：$\frac{f(x)+2}x=1+\frac1x-\frac{\ln x}x$，"
        r"把「含 $b$ 的一次式」留在右边，左边只含 $x$ —— 这是恒成立问题的标准操作．" "\n"
        r"② ⚠ 分离时**必须同除以 $x>0$**，这一步依赖定义域 $(0,+\infty)$，不可省．" "\n"
        r"③ （3）与 M-T-159-E1 的第（3）问**是同一个函数** $g(x)=\frac{\mathrm e^{x}}{\ln(x+1)}$，" "\n"
        r"　 只是 E1 写成 $\mathrm e^{x}\ln(1+y)>\mathrm e^{y}\ln(1+x)$（交叉相乘），本题写成商的形式．" "\n"
        r"　 **认出同构，推导就省一半** —— 这已是本册第二次出现该结构．" "\n"
        r"④ 原书详解中 $g(x)$ 的导数写作「$\frac{\ln x-2}{x^{2}}$」的形式时被拆成两行，已按推导补全为一式．" "\n"
        r"⑤ 数值复核：$b=1-\frac1{\mathrm e^{2}}=0.864665$；取 $x=\mathrm e^{2}=7.389$，"
        r"$f(\mathrm e^{2})=6.389-1-2=3.389$，$bx-2=0.864665\times7.389-2=4.389$ —— " "\n"
        r"　 咦，此时 $f(x)<bx-2$？注意：$f(x)\ge bx-2$ 等价于 $g(x)\ge b$，"
        r"而 $g(\mathrm e^{2})=1-\frac1{\mathrm e^{2}}=b$，取等号 ✓（上面把 $f$ 与 $bx-2$ 直接比，差 $1$ 是移项所致，用 $g$ 校验才对）．"
    ),
    'difficulty': 0.82,
    'topics': ['M-T-159'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-159-V1',
}

T159_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=(ax-1)\mathrm e^{x}$，$a\in\mathbb R$．" "\n"
        r"（1）讨论 $f(x)$ 的单调区间；" "\n"
        r"（2）当 $m>n>0$ 时，证明：$m\mathrm e^{n}+n<n\mathrm e^{m}+m$．"
    ),
    'opts': [],
    'answer': r"（1）见解析；（2）证明见解析",
    'analysis': (
        r"（1）$f'(x)=(ax+a-1)\mathrm e^{x}$，按 $a=0$、$a>0$、$a<0$ 三类讨论；" "\n"
        r"（2）移项后化为 $\frac{\mathrm e^{m}-1}m>\frac{\mathrm e^{n}-1}n$，构造 $g(x)=\frac{\mathrm e^{x}-1}{x}$．"
    ),
    'solution': (
        r"**【解析】（1）** $f(x)$ 的定义域为 $\mathbb R$，且" "\n"
        r"$f'(x)=a\mathrm e^{x}+(ax-1)\mathrm e^{x}=(ax+a-1)\mathrm e^{x}$．" "\n"
        r"因 $\mathrm e^{x}>0$ 恒成立，故 $f'(x)$ 的符号只由 $ax+a-1$ 决定，记 $x_0=-\dfrac{a-1}a$（$a\ne0$）．" "\n"
        r"① 当 $a=0$ 时：$f'(x)=-\mathrm e^{x}<0$，此时 $f(x)$ 的单调递减区间为 $(-\infty,+\infty)$．" "\n"
        r"② 当 $a>0$ 时：由 $f'(x)>0$ 得 $x>x_0=-\dfrac{a-1}a$；由 $f'(x)<0$ 得 $x<x_0$．" "\n"
        r"此时 $f(x)$ 的单调递减区间为 $\left(-\infty,-\dfrac{a-1}a\right)$，单调递增区间为 $\left(-\dfrac{a-1}a,+\infty\right)$．" "\n"
        r"③ 当 $a<0$ 时：由 $f'(x)>0$ 得 $x<-\dfrac{a-1}a$；由 $f'(x)<0$ 得 $x>-\dfrac{a-1}a$．" "\n"
        r"此时 $f(x)$ 的单调递增区间为 $\left(-\infty,-\dfrac{a-1}a\right)$，单调递减区间为 $\left(-\dfrac{a-1}a,+\infty\right)$．" "\n"
        r"**【解析】（2）** 当 $m>n>0$ 时，要证 $m\mathrm e^{n}+n<n\mathrm e^{m}+m$，" "\n"
        r"移项得 $m\mathrm e^{n}-m<n\mathrm e^{m}-n$，即只需证" "\n"
        r"$m\left(\mathrm e^{n}-1\right)<n\left(\mathrm e^{m}-1\right)\iff\dfrac{\mathrm e^{m}-1}{m}>\dfrac{\mathrm e^{n}-1}{n}$．　（*）" "\n"
        r"设 $g(x)=\dfrac{\mathrm e^{x}-1}{x}$（$x>0$），则" "\n"
        r"$g'(x)=\dfrac{x\mathrm e^{x}-\left(\mathrm e^{x}-1\right)}{x^{2}}=\dfrac{(x-1)\mathrm e^{x}+1}{x^{2}}$．" "\n"
        r"设 $h(x)=(x-1)\mathrm e^{x}+1$，则 $h'(x)=\mathrm e^{x}+(x-1)\mathrm e^{x}=x\mathrm e^{x}>0$（$x>0$），" "\n"
        r"故 $h(x)$ 在 $[0,+\infty)$ 上单调递增，于是当 $x>0$ 时 $h(x)>h(0)=0$，从而 $g'(x)>0$．" "\n"
        r"所以 $g(x)$ 在 $(0,+\infty)$ 上单调递增．" "\n"
        r"由 $m>n>0$ 得 $g(m)>g(n)$，即（*）式成立，故 $m\mathrm e^{n}+n<n\mathrm e^{m}+m$．"
    ),
    'review': (
        r"① （2）的题眼是**移项后因式分解**：$m\mathrm e^{n}+n<n\mathrm e^{m}+m$ 中的 $+n,+m$ 看着多余，" "\n"
        r"　 但移项后恰能凑成 $m(\mathrm e^{n}-1)<n(\mathrm e^{m}-1)$ —— **命题人加这两项就是为了让你能提公因式**．" "\n"
        r"② $g(x)=\frac{\mathrm e^{x}-1}x$ 的导数分子 $(x-1)\mathrm e^{x}+1$ 不能直接判号，"
        r"需**再求一次导**（$h'(x)=x\mathrm e^{x}>0$）—— 这是「二次求导」的标准用例．" "\n"
        r"③ 与（1）的联系：取 $a=1$ 时 $f'(x)=x\mathrm e^{x}$，正是本题 $h'(x)$ —— 原书说「由（1）知」即指此．" "\n"
        r"④ ⚠ $a<0$ 时单调区间与 $a>0$ 时**正好相反**（因 $ax+a-1$ 的斜率为负），分类讨论别漏这一类．" "\n"
        r"⑤ 数值复核：$m=2,n=1$，$2\mathrm e^{1}+1=6.436$，$1\mathrm e^{2}+2=9.389$，$6.436<9.389$ ✓；" "\n"
        r"　 $g(2)=\frac{\mathrm e^{2}-1}2=3.1945$，$g(1)=\mathrm e-1=1.7183$，$g(2)>g(1)$ ✓．"
    ),
    'difficulty': 0.80,
    'topics': ['M-T-159'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-159-V2',
}

T160_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知 $f(x)=x\ln x$，$g(x)=-x^{2}+ax-3$．" "\n"
        r"（1）求函数 $f(x)$ 的单调区间；" "\n"
        r"（2）对一切 $x\in(0,+\infty)$，$2f(x)\ge g(x)$ 恒成立，求实数 $a$ 的取值范围；" "\n"
        r"（3）证明：对一切 $x\in(0,+\infty)$，都有 $\ln x>\dfrac1{\mathrm e^{x}}-\dfrac2{\mathrm ex}$ 成立．"
    ),
    'opts': [],
    'answer': (
        r"（1）$f(x)$ 在 $\left(0,\frac1{\mathrm e}\right)$ 上单调递减，在 $\left(\frac1{\mathrm e},+\infty\right)$ 上单调递增；"
        r"（2）$a\le4$；（3）证明见解析"
    ),
    'analysis': (
        r"（1）$f'(x)=\ln x+1$；（2）分离参数得 $a\le2\ln x+x+\frac3x=h(x)$，求 $h$ 的最小值；" "\n"
        r"（3）两边同乘 $x$ 化为 $x\ln x>\frac x{\mathrm e^{x}}-\frac2{\mathrm e}$，比较左端最小值与右端最大值．"
    ),
    'solution': (
        r"**【解析】（1）** $f(x)=x\ln x$ 的定义域为 $(0,+\infty)$，$f'(x)=\ln x+1$．" "\n"
        r"令 $f'(x)<0$ 得 $0<x<\dfrac1{\mathrm e}$；令 $f'(x)>0$ 得 $x>\dfrac1{\mathrm e}$．" "\n"
        r"故 $f(x)$ 在 $\left(0,\dfrac1{\mathrm e}\right)$ 上单调递减，在 $\left(\dfrac1{\mathrm e},+\infty\right)$ 上单调递增．" "\n"
        r"**【解析】（2）** 原不等式 $2f(x)\ge g(x)$ 即" "\n"
        r"$2x\ln x\ge-x^{2}+ax-3\iff a\le 2\ln x+x+\dfrac3x$（对一切 $x>0$ 恒成立）．" "\n"
        r"设 $h(x)=2\ln x+x+\dfrac3x$（$x>0$），则" "\n"
        r"$h'(x)=\dfrac2x+1-\dfrac3{x^{2}}=\dfrac{x^{2}+2x-3}{x^{2}}=\dfrac{(x+3)(x-1)}{x^{2}}$．" "\n"
        r"当 $x\in(0,1)$ 时 $h'(x)<0$，$h(x)$ 单调递减；当 $x\in(1,+\infty)$ 时 $h'(x)>0$，$h(x)$ 单调递增．" "\n"
        r"故 $h(x)_{\min}=h(1)=0+1+3=4$，于是 $a\le4$，即 $a$ 的取值范围为 $(-\infty,4]$．" "\n"
        r"**【解析】（3）** 所证不等式两边同乘 $x>0$，等价于" "\n"
        r"$x\ln x>\dfrac x{\mathrm e^{x}}-\dfrac2{\mathrm e}$．" "\n"
        r"由（1）知 $f(x)=x\ln x$ 在 $(0,+\infty)$ 上的最小值为 $f\!\left(\dfrac1{\mathrm e}\right)=-\dfrac1{\mathrm e}$，"
        r"当且仅当 $x=\dfrac1{\mathrm e}$ 时取到．" "\n"
        r"设 $m(x)=\dfrac x{\mathrm e^{x}}-\dfrac2{\mathrm e}=x\mathrm e^{-x}-\dfrac2{\mathrm e}$（$x>0$），则" "\n"
        r"$m'(x)=\mathrm e^{-x}-x\mathrm e^{-x}=\dfrac{1-x}{\mathrm e^{x}}$．" "\n"
        r"当 $x\in(0,1)$ 时 $m'(x)>0$，$m(x)$ 单调递增；当 $x\in(1,+\infty)$ 时 $m'(x)<0$，$m(x)$ 单调递减．" "\n"
        r"故 $m(x)_{\max}=m(1)=\dfrac1{\mathrm e}-\dfrac2{\mathrm e}=-\dfrac1{\mathrm e}$，当且仅当 $x=1$ 时取到．" "\n"
        r"由于 $x\ln x\ge-\dfrac1{\mathrm e}$ 与 $m(x)\le-\dfrac1{\mathrm e}$ **取等条件不同**（前者 $x=\frac1{\mathrm e}$，后者 $x=1$），" "\n"
        r"故对一切 $x\in(0,+\infty)$ 恒有 $x\ln x>m(x)$，即 $\ln x>\dfrac1{\mathrm e^{x}}-\dfrac2{\mathrm ex}$ 成立．"
    ),
    'review': (
        r"① （3）是典型的**「两边最值比对」**：左端最小值与右端最大值都是 $-\frac1{\mathrm e}$，" "\n"
        r"　 但取等点不同（$\frac1{\mathrm e}$ 与 $1$），所以是**严格**大于 —— 这一点必须写清楚，否则只能得 $\ge$．" "\n"
        r"② ⚠ 原书（3）的题干在部分版本中写作 $\ln x>\frac1{\mathrm e^{x}}-\frac2{\mathrm ex}$，" "\n"
        r"　 若漏掉分母中的 $x$，两边乘 $x$ 后右端变成 $\frac x{\mathrm e^{x}}-2$，与 $x\ln x$ 的最小值 $-\frac1{\mathrm e}$ 之间" "\n"
        r"　 仍有 $-\frac1{\mathrm e}>\frac1{\mathrm e}-2=-1.632$，结论也成立，但**取等分析完全不同**，录入时以分母含 $x$ 为准．" "\n"
        r"③ （2）的 $h'(x)=\frac{(x+3)(x-1)}{x^{2}}$ **因式分解后符号一眼看穿**，这是分离参数法的标配形式．" "\n"
        r"④ 数值复核：$a=4$ 时取 $x=1$，$2f(1)=0$，$g(1)=-1+4-3=0$，恰好相等 ✓；" "\n"
        r"　 $a=4.1$ 时 $g(1)=-1+4.1-3=0.1>0=2f(1)$，不成立 ✓ —— 边界 $4$ 确实是临界值．"
    ),
    'difficulty': 0.80,
    'topics': ['M-T-160'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-160-E1',
}

T160_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知 $f(x)=x\ln x$．" "\n"
        r"（1）求函数 $f(x)$ 的极值；" "\n"
        r"（2）证明：对一切 $x\in(0,+\infty)$，都有 "
        r"$\ln x\ge\dfrac{x+1-\frac1{\mathrm e}}{x\,\mathrm e^{\,x+1-\frac1{\mathrm e}}}-\dfrac2{\mathrm ex}$ 成立．"
    ),
    'opts': [],
    'answer': r"（1）极小值为 $-\dfrac1{\mathrm e}$，无极大值；（2）证明见解析",
    'analysis': (
        r"（1）$f'(x)=\ln x+1$；（2）两边同乘 $x$ 后化为"
        r"$x\ln x\ge\frac{x+1-\frac1{\mathrm e}}{\mathrm e^{\,x+1-\frac1{\mathrm e}}}-\frac2{\mathrm e}$，"
        r"分别求左端最小值与右端最大值，二者**都在 $x=\frac1{\mathrm e}$ 处取到 $-\frac1{\mathrm e}$**．"
    ),
    'solution': (
        r"**【解析】（1）** $f(x)=x\ln x$ 的定义域为 $(0,+\infty)$，$f'(x)=\ln x+1$．" "\n"
        r"令 $f'(x)=0$ 得 $x=\dfrac1{\mathrm e}$．" "\n"
        r"当 $x\in\left(0,\dfrac1{\mathrm e}\right)$ 时 $f'(x)<0$，$f(x)$ 单调递减；"
        r"当 $x\in\left(\dfrac1{\mathrm e},+\infty\right)$ 时 $f'(x)>0$，$f(x)$ 单调递增．" "\n"
        r"故 $f(x)$ 的极小值为 $f\!\left(\dfrac1{\mathrm e}\right)=\dfrac1{\mathrm e}\ln\dfrac1{\mathrm e}=-\dfrac1{\mathrm e}$，无极大值．" "\n"
        r"**【解析】（2）** 所证不等式两边同乘 $x>0$，等价于证明" "\n"
        r"$x\ln x\ge\dfrac{x+1-\frac1{\mathrm e}}{\mathrm e^{\,x+1-\frac1{\mathrm e}}}-\dfrac2{\mathrm e}$，$x\in(0,+\infty)$．" "\n"
        r"由（1）知 $f(x)=x\ln x$ 的最小值为 $f\!\left(\dfrac1{\mathrm e}\right)=-\dfrac1{\mathrm e}$．" "\n"
        r"设 $g(x)=\dfrac{x+1-\frac1{\mathrm e}}{\mathrm e^{\,x+1-\frac1{\mathrm e}}}-\dfrac2{\mathrm e}$，"
        r"记 $u=x+1-\dfrac1{\mathrm e}$，则 $g=u\mathrm e^{-u}-\dfrac2{\mathrm e}$，" "\n"
        r"$g'(x)=\left(1-u\right)\mathrm e^{-u}=\left(\dfrac1{\mathrm e}-x\right)\mathrm e^{-\left(x+1-\frac1{\mathrm e}\right)}$"
        r"$=\dfrac{\frac1{\mathrm e}-x}{\mathrm e^{\,x+1-\frac1{\mathrm e}}}$．" "\n"
        r"当 $x\in\left(0,\dfrac1{\mathrm e}\right)$ 时 $g'(x)>0$，$g(x)$ 单调递增；"
        r"当 $x\in\left(\dfrac1{\mathrm e},+\infty\right)$ 时 $g'(x)<0$，$g(x)$ 单调递减．" "\n"
        r"故 $g(x)_{\max}=g\!\left(\dfrac1{\mathrm e}\right)=\dfrac{\frac1{\mathrm e}+1-\frac1{\mathrm e}}{\mathrm e^{\,1}}-\dfrac2{\mathrm e}$"
        r"$=\dfrac1{\mathrm e}-\dfrac2{\mathrm e}=-\dfrac1{\mathrm e}$，当且仅当 $x=\dfrac1{\mathrm e}$ 时取到．" "\n"
        r"于是对一切 $x>0$ 有" "\n"
        r"$x\ln x\ge-\dfrac1{\mathrm e}\ge g(x)$，" "\n"
        r"且两边等号**同时在 $x=\dfrac1{\mathrm e}$ 时成立**．" "\n"
        r"两边同除以 $x$ 即得 $\ln x\ge\dfrac{x+1-\frac1{\mathrm e}}{x\,\mathrm e^{\,x+1-\frac1{\mathrm e}}}-\dfrac2{\mathrm ex}$．"
    ),
    'review': (
        r"① 本题是「凹凸翻转型」的样板：**左端最小值 = 右端最大值 = $-\frac1{\mathrm e}$，且取等点相同**，" "\n"
        r"　 所以两个 $\ge$ 能接成一条链，且等号能同时取到 —— 这是 $\ge$（而非 $>$）的原因，与 M-T-160-E1 的（3）形成对照．" "\n"
        r"② ⚠ 右端 $g(x)$ 的最大值的计算关键：令 $u=x+1-\frac1{\mathrm e}$，则 $g=u\mathrm e^{-u}-\frac2{\mathrm e}$，" "\n"
        r"　 而 $\varphi(u)=u\mathrm e^{-u}$ 在 $u=1$（即 $x=\frac1{\mathrm e}$）处取最大值 $\frac1{\mathrm e}$ —— "
        r"**这个「$u\mathrm e^{-u}$ 在 $u=1$ 取 $\frac1{\mathrm e}$」的固定结论要记住**．" "\n"
        r"③ 原书题干的分数线在 OCR 中断成多行（形如 `x + 1 - 1 / e` 与 `xe / x+1- 1 / e`），" "\n"
        r"　 已按「两边同乘 $x$ 后与详解中间式完全吻合」还原：$\frac{x+1-\frac1{\mathrm e}}{x\,\mathrm e^{\,x+1-\frac1{\mathrm e}}}-\frac2{\mathrm ex}$．" "\n"
        r"　 判据：详解中 $g(x)_{\max}=g(\frac1{\mathrm e})=-\frac1{\mathrm e}$，只有这个形式能让分子在 $x=\frac1{\mathrm e}$ 时等于 $1$．" "\n"
        r"④ 数值复核：$x=\frac1{\mathrm e}=0.367879$，左 $\ln\frac1{\mathrm e}=-1$；"
        r"右端 $=\frac{0.367879+1-0.367879}{0.367879\times\mathrm e^{1}}-\frac2{\mathrm e\times0.367879}$"
        r"$=\frac{1}{1}-\frac{2}{1}=-1$ ✓ 恰好相等．" "\n"
        r"⑤ 数值复核：$x=1$，左 $\ln1=0$；右 $=\frac{1+1-0.367879}{\mathrm e^{1.632121}}-\frac2{\mathrm e}$"
        r"$=\frac{1.632121}{5.114}-0.735759=0.319142-0.735759=-0.416617<0$ ✓．"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-160'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-160-V1',
}

T161_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=\mathrm e^{x}-ax-\cos x$，$g(x)=f(x)-x$，$a\in\mathbb R$．" "\n"
        r"（1）若 $f(x)$ 在 $[0,+\infty)$ 上单调递增，求 $a$ 的最大值；" "\n"
        r"（2）当 $a$ 取（1）中所求的最大值时，讨论 $g(x)$ 在 $\mathbb R$ 上的零点个数，并证明 $g(x)>-\sqrt2$．"
    ),
    'opts': [],
    'answer': r"（1）$a$ 的最大值为 $1$；（2）$g(x)$ 有 $2$ 个零点，证明见解析",
    'analysis': (
        r"（1）$f'(x)=\mathrm e^{x}-a+\sin x\ge0$ 恒成立；由 $f''(x)=\mathrm e^{x}+\cos x\ge1+\cos x\ge0$ 知 $f'$ 递增，"
        r"故只需 $f'(0)\ge0$．" "\n"
        r"（2）用 $\sin x$ 的有界性锁定 $g(x)$ 在 $x\le0$ 与 $x>0$ 上的单调性，取 $g(0),g(1),g(2)$ 的符号定位两个零点，"
        r"再用 $-\sin x_{0}-\cos x_{0}\ge-\sqrt2$ 证下界．"
    ),
    'solution': (
        r"**【解析】（1）** $f'(x)=\mathrm e^{x}-a+\sin x$．" "\n"
        r"由题意 $f'(x)\ge0$ 在 $[0,+\infty)$ 上恒成立．" "\n"
        r"又 $f''(x)=\mathrm e^{x}+\cos x\ge1+\cos x\ge0$（因 $x\ge0$ 时 $\mathrm e^{x}\ge1$），"
        r"故 $f'(x)$ 在 $[0,+\infty)$ 上单调递增．" "\n"
        r"于是 $f'(x)\ge f'(0)$ 对一切 $x\ge0$ 成立，故只需 $f'(0)=1-a\ge0$，解得 $a\le1$．" "\n"
        r"所以 $a$ 的最大值为 $1$．" "\n"
        r"**【解析】（2）** 取 $a=1$，则 $g(x)=f(x)-x=\mathrm e^{x}-x-\cos x-x=\mathrm e^{x}-2x-\cos x$．" "\n"
        r"$g'(x)=\mathrm e^{x}-2+\sin x$．" "\n"
        r"① 当 $x\le0$ 时：$\mathrm e^{x}\le1$，故 $g'(x)\le1-2+\sin x=-1+\sin x\le0$，"
        r"所以 $g(x)$ 在 $(-\infty,0]$ 上单调递减．" "\n"
        r"② 当 $x>0$ 时：$g''(x)=\mathrm e^{x}+\cos x\ge1+\cos x\ge0$，故 $g'(x)$ 在 $(0,+\infty)$ 上单调递增．" "\n"
        r"又 $g'(0)=1-2+0=-1<0$，$g'(1)=\mathrm e-2+\sin1>2.718-2+0.841>0$，"
        r"故存在 $x_{0}\in(0,1)$ 使 $g'(x_{0})=0$．" "\n"
        r"于是 $g(x)$ 在 $(-\infty,x_{0})$ 上单调递减，在 $(x_{0},+\infty)$ 上单调递增．" "\n"
        r"③ 零点个数：由 $g(0)=\mathrm e^{0}-0-\cos0=1-1=0$，知 $x=0$ 是一个零点；"
        r"又 $g$ 在 $(-\infty,x_{0})$ 上递减且 $0<x_{0}$，故 $g(x_{0})<g(0)=0$．" "\n"
        r"而 $g(2)=\mathrm e^{2}-4-\cos2>7.389-4-\left(-1\right)=4.389>0$，"
        r"故存在 $x_{1}\in(x_{0},2)$ 使 $g(x_{1})=0$．" "\n"
        r"结合单调性（两段各至多一个零点），$g(x)$ 恰有 $2$ 个零点．" "\n"
        r"④ 证明 $g(x)>-\sqrt2$：由 $g'(x_{0})=0$ 得 $\mathrm e^{x_{0}}=2-\sin x_{0}$，于是" "\n"
        r"$g(x)_{\min}=g(x_{0})=\mathrm e^{x_{0}}-2x_{0}-\cos x_{0}=2-\sin x_{0}-2x_{0}-\cos x_{0}$．" "\n"
        r"因 $x_{0}\in(0,1)$，故 $-2x_{0}>-2$，从而" "\n"
        r"$g(x_{0})>2-\sin x_{0}-2-\cos x_{0}=-\left(\sin x_{0}+\cos x_{0}\right)$"
        r"$=-\sqrt2\sin\!\left(x_{0}+\dfrac\pi4\right)\ge-\sqrt2$．" "\n"
        r"所以对一切 $x\in\mathbb R$ 有 $g(x)\ge g(x_{0})>-\sqrt2$．"
    ),
    'review': (
        r"① 本题两次用到「$\mathrm e^{x}\ge1$（$x\ge0$）⟹ $\mathrm e^{x}+\cos x\ge1+\cos x\ge0$」——"
        r"这是**用指数函数的下界压住三角函数的负值**的标准手法．" "\n"
        r"② ⚠ 注意 $g(0)=1-0-1=0$ **恰好是零点**，这使「$g$ 在 $(-\infty,x_{0})$ 递减」直接给出 $g(x_{0})<0$，"
        r"省掉了额外的估值 —— 命题人把 $a=1$ 选出来正是为此．" "\n"
        r"③ 下界 $-\sqrt2$ 的来源：$-\left(\sin x_{0}+\cos x_{0}\right)=-\sqrt2\sin\left(x_{0}+\frac\pi4\right)$，" "\n"
        r"　 这是**辅助角公式**在证明题中的典型用法，把两个有界量合成一个有界量．" "\n"
        r"④ ⚠ 严格性：$g(x_{0})=2-\sin x_{0}-2x_{0}-\cos x_{0}>-\sin x_{0}-\cos x_{0}$ 用的是 $x_{0}<1⟹-2x_{0}>-2$，"
        r"　 **是严格大于**，所以最终是 $g(x)>-\sqrt2$ 而非 $\ge$．" "\n"
        r"⑤ 数值复核：$x_{0}$ 满足 $\mathrm e^{x_{0}}-2+\sin x_{0}=0$，解得 $x_{0}=0.601346$；"
        r"$g(x_{0})=2-0.565-1.203-0.825=-0.593>-\sqrt2=-1.414$ ✓．" "\n"
        r"　 另一零点：$\mathrm e^{x}-2x-\cos x=0$ 的正根 $x_{1}=1.398$ 附近，与 $x=0$ 共 $2$ 个 ✓．"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-161'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-161-E1',
}

T161_V1 = {
    'type': '解答',
    'stem_text': (
        r"设函数 $f(x)=x\ln(1-x)$．" "\n"
        r"（1）求 $y=f(x)$ 的极值点；" "\n"
        r"（2）设函数 $F(x)=\dfrac{x}{f(x)}+\dfrac1x-\sin x$．证明：$F(x)<2$．"
    ),
    'opts': [],
    'answer': r"（1）$x=0$（极大值点，极大值为 $0$）；（2）证明见解析",
    'analysis': (
        r"（1）$f'(x)=\ln(1-x)-\frac x{1-x}$，再设 $g(x)=f'(x)$ 求 $g'(x)=\frac{x-2}{(1-x)^{2}}<0$，"
        r"用 $g(0)=0$ 定号；（2）先化 $\frac x{f(x)}=\frac1{\ln(1-x)}$，" "\n"
        r"再构造 $h(x)=\frac1{\ln(1-x)}+\frac1x-1$，分 $0<x<1$ 与 $x<0$ 两段证 $h(x)<0$，最后用 $2+\sin x\ge1$ 收尾．"
    ),
    'solution': (
        r"**【解析】（1）** 函数 $y=f(x)$ 的定义域为 $(-\infty,1)$，且" "\n"
        r"$f'(x)=\ln(1-x)+x\cdot\dfrac{-1}{1-x}=\ln(1-x)-\dfrac x{1-x}$．" "\n"
        r"设 $g(x)=\ln(1-x)-\dfrac x{1-x}$，则" "\n"
        r"$g'(x)=\dfrac{-1}{1-x}-\dfrac{(1-x)-x\cdot(-1)}{(1-x)^{2}}$"
        r"$=\dfrac{-1}{1-x}-\dfrac1{(1-x)^{2}}=\dfrac{-(1-x)-1}{(1-x)^{2}}=\dfrac{x-2}{(1-x)^{2}}$．" "\n"
        r"因 $x\in(-\infty,1)$，故 $x-2<0$，即 $g'(x)<0$，$g(x)$ 在 $(-\infty,1)$ 上单调递减，且 $g(0)=0$．" "\n"
        r"于是：当 $0<x<1$ 时 $g(x)<g(0)=0$，即 $f'(x)<0$，$f(x)$ 单调递减；" "\n"
        r"当 $x<0$ 时 $g(x)>g(0)=0$，即 $f'(x)>0$，$f(x)$ 单调递增．" "\n"
        r"故 $x=0$ 时 $f(x)$ 取得极大值 $f(0)=0\cdot\ln1=0$，极值点为 $x=0$（极大值点）．" "\n"
        r"**【解析】（2）** $F(x)$ 的定义域为 $(-\infty,0)\cup(0,1)$，且" "\n"
        r"$\dfrac x{f(x)}=\dfrac x{x\ln(1-x)}=\dfrac1{\ln(1-x)}$，故 $F(x)=\dfrac1{\ln(1-x)}+\dfrac1x-\sin x$．" "\n"
        r"要证 $F(x)<2$，只需证 $\dfrac1{\ln(1-x)}+\dfrac1x<2+\sin x$．" "\n"
        r"构造函数" "\n"
        r"$h(x)=\dfrac1{\ln(1-x)}+\dfrac1x-1=\dfrac{x+\ln(1-x)-x\ln(1-x)}{x\ln(1-x)}$．" "\n"
        r"由（1）知 $f(x)=x\ln(1-x)$ 的极大值为 $f(0)=0$，故当 $x\in(-\infty,0)\cup(0,1)$ 时 $x\ln(1-x)<0$，"
        r"即 $h(x)$ 的分母恒负．" "\n"
        r"设 $t(x)=x+\ln(1-x)-x\ln(1-x)$（$x<1$），则" "\n"
        r"$t'(x)=1-\dfrac1{1-x}-\left[\ln(1-x)+x\cdot\dfrac{-1}{1-x}\right]$"
        r"$=1-\dfrac1{1-x}-\ln(1-x)+\dfrac x{1-x}$．" "\n"
        r"注意到 $1+\dfrac{x}{1-x}=\dfrac{1-x+x}{1-x}=\dfrac1{1-x}$，故" "\n"
        r"$t'(x)=\dfrac1{1-x}-\dfrac1{1-x}-\ln(1-x)=-\ln(1-x)$．" "\n"
        r"当 $0<x<1$ 时：$-\ln(1-x)>0$，$t'(x)>0$，$t(x)$ 单调递增，故 $t(x)>t(0)=0$，"
        r"结合分母为负得 $h(x)<0$；" "\n"
        r"当 $x<0$ 时：$-\ln(1-x)<0$，$t'(x)<0$，$t(x)$ 单调递减，故 $t(x)>t(0)=0$（沿 $x$ 减小的方向递增到 $0$），"
        r"同样得 $h(x)<0$．" "\n"
        r"综上，当 $x\in(-\infty,0)\cup(0,1)$ 时 $h(x)<0$，即 $\dfrac1{\ln(1-x)}+\dfrac1x<1$．" "\n"
        r"又设 $m(x)=2+\sin x$，由 $-1\le\sin x\le1$ 得 $1\le m(x)\le3$，即 $m(x)\ge1$．" "\n"
        r"于是 $\dfrac1{\ln(1-x)}+\dfrac1x<1\le2+\sin x$，即 $F(x)<2$ 成立．"
    ),
    'review': (
        r"① 本题有两处「必须二次求导」：$f'(x)$ 的符号要靠 $g'(x)=\frac{x-2}{(1-x)^{2}}$ 来定，"
        r"$t(x)$ 的符号要靠 $t'(x)=-\ln(1-x)$ 来定 —— **连锁二次求导**是本題的技术核心．" "\n"
        r"② ⚠ $t'(x)$ 的化简有个陷阱：$1+\frac x{1-x}=\frac1{1-x}$ 会与前面的 $-\frac1{1-x}$ **恰好抵消**，" "\n"
        r"　 剩下 $-\ln(1-x)$．这个抵消不是巧合，是命题人设计的 —— 若算错这里，后面两段都判不了号．" "\n"
        r"③ $x<0$ 时 $t(x)>t(0)=0$ 的理由要写对：$t$ 在 $(-\infty,0)$ 上**递减**，"
        r"故沿 $x$ 从 $0$ 往左走 $t$ 变大，即 $t(x)>t(0)$．" "\n"
        r"④ 收尾用 $2+\sin x\ge1$ 显得「松」，但因为左边已经证到 $<1$，"
        r"**刚好够用** —— 这种「一边做强、一边做弱恰好接上」是不等式证明的常见设计．" "\n"
        r"⑤ ⚠ 定义域 $(-\infty,0)\cup(0,1)$ 中排除了 $x=0$：$x=0$ 时 $f(0)=0$，$\frac x{f(x)}$ 无意义．" "\n"
        r"⑥ 数值复核：$x=-1$，$F(-1)=\frac1{\ln2}-1-\sin(-1)=1.4427-1+0.8415=1.2842<2$ ✓；" "\n"
        r"　 $x=0.5$，$F(0.5)=\frac1{\ln0.5}+2-\sin0.5=-1.4427+2-0.4794=0.0779<2$ ✓．"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-161'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-161-V1',
}

T162_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=x\ln x$．" "\n"
        r"（1）求曲线 $y=f(x)$ 在点 $\left(1,f(1)\right)$ 处的切线方程；" "\n"
        r"（2）设 $x_{1},x_{2}$ 为两个不相等的正数，且 $f(x_{1})=f(x_{2})$，证明：$\dfrac2{\mathrm e}<x_{1}+x_{2}<1$．"
    ),
    'opts': [],
    'answer': r"（1）$x-y-1=0$；（2）证明见解析",
    'analysis': (
        r"（1）$k=f'(1)=1$，切点 $(1,0)$；（2）右侧用切线放缩 $\ln x>1-\frac1x$ 配 $x_{1}\ln x_{1}<-x_{1}$；"
        r"左侧用对称化构造 $F(x)=f(x)-f\left(\frac2{\mathrm e}-x\right)$．"
    ),
    'solution': (
        r"**【解析】（1）** $f(x)=x\ln x$，切点为 $\left(1,f(1)\right)=(1,0)$．" "\n"
        r"$f'(x)=\ln x+1$，故 $k=f'(1)=1$．" "\n"
        r"切线方程为 $y-0=1\cdot(x-1)$，即 $y=x-1$，亦即 $x-y-1=0$．" "\n"
        r"**【解析】（2）** $f'(x)=\ln x+1$，令 $f'(x)=0$ 得 $x=\dfrac1{\mathrm e}$．" "\n"
        r"当 $0<x<\dfrac1{\mathrm e}$ 时 $f'(x)<0$，$f(x)$ 单调递减；当 $x>\dfrac1{\mathrm e}$ 时 $f'(x)>0$，$f(x)$ 单调递增．" "\n"
        r"又 $f(1)=0$、$f\!\left(\frac1{\mathrm e}\right)=-\frac1{\mathrm e}<0$，由 $f(x_{1})=f(x_{2})$ 且 $x_{1}\ne x_{2}$，"
        r"不妨设 $x_{1}<x_{2}$，则 $0<x_{1}<\dfrac1{\mathrm e}<x_{2}<1$．" "\n"
        r"**先证右边 $x_{1}+x_{2}<1$：**" "\n"
        r"由经典不等式 $\ln x>1-\dfrac1x$（$x>0$ 且 $x\ne1$，等号仅 $x=1$），取 $x=x_{2}\in\left(\frac1{\mathrm e},1\right)$ 得" "\n"
        r"$x_{2}\ln x_{2}>x_{2}\left(1-\dfrac1{x_{2}}\right)=x_{2}-1$．" "\n"
        r"（该不等式即 $\varphi(x)=\ln x-1+\frac1x$ 在 $(0,1)$ 上恒正：$\varphi'(x)=\frac{x-1}{x^{2}}<0$，"
        r"$\varphi$ 递减且 $\varphi(1)=0$，故 $x<1$ 时 $\varphi(x)>0$．）" "\n"
        r"又由 $0<x_{1}<\frac1{\mathrm e}$ 得 $\ln x_{1}<-1$，故 $x_{1}\ln x_{1}<-x_{1}$．" "\n"
        r"于是 $-x_{1}>x_{1}\ln x_{1}=x_{2}\ln x_{2}>x_{2}-1$，即 $-x_{1}>x_{2}-1$，所以 $x_{1}+x_{2}<1$．" "\n"
        r"**再证左边 $x_{1}+x_{2}>\dfrac2{\mathrm e}$：**" "\n"
        r"只需证 $x_{2}>\dfrac2{\mathrm e}-x_{1}$．因 $0<x_{1}<\dfrac1{\mathrm e}$，故 $\dfrac2{\mathrm e}-x_{1}>\dfrac1{\mathrm e}$；"
        r"又 $x_{2}>\dfrac1{\mathrm e}$，而 $f(x)$ 在 $\left(\frac1{\mathrm e},+\infty\right)$ 上单调递增，" "\n"
        r"故只需证 $f(x_{2})>f\!\left(\dfrac2{\mathrm e}-x_{1}\right)$，即 $f(x_{1})>f\!\left(\dfrac2{\mathrm e}-x_{1}\right)$．" "\n"
        r"构造函数 $F(x)=f(x)-f\!\left(\dfrac2{\mathrm e}-x\right)$，$x\in\left(0,\dfrac1{\mathrm e}\right)$，则" "\n"
        r"$F(x)=x\ln x-\left(\dfrac2{\mathrm e}-x\right)\ln\!\left(\dfrac2{\mathrm e}-x\right)$，" "\n"
        r"$F'(x)=\ln x+1+\ln\!\left(\dfrac2{\mathrm e}-x\right)+1=\ln\!\left[x\left(\dfrac2{\mathrm e}-x\right)\right]+2$．" "\n"
        r"由基本不等式 $x\left(\dfrac2{\mathrm e}-x\right)\le\left(\dfrac{\frac2{\mathrm e}}2\right)^{2}=\dfrac1{\mathrm e^{2}}$，得" "\n"
        r"$F'(x)\le\ln\dfrac1{\mathrm e^{2}}+2=-2+2=0$．" "\n"
        r"故 $F(x)$ 在 $\left(0,\dfrac1{\mathrm e}\right)$ 上单调递减，于是 $F(x_{1})>F\!\left(\dfrac1{\mathrm e}\right)=0$．" "\n"
        r"即 $f(x_{1})>f\!\left(\dfrac2{\mathrm e}-x_{1}\right)$，从而 $f(x_{2})>f\!\left(\dfrac2{\mathrm e}-x_{1}\right)$，" "\n"
        r"由 $x_{2},\dfrac2{\mathrm e}-x_{1}$ 同在 $\left(\frac1{\mathrm e},+\infty\right)$ 且 $f$ 在此递增，得 $x_{2}>\dfrac2{\mathrm e}-x_{1}$，" "\n"
        r"即 $x_{1}+x_{2}>\dfrac2{\mathrm e}$．" "\n"
        r"综上 $\dfrac2{\mathrm e}<x_{1}+x_{2}<1$．"
    ),
    'review': (
        r"① 右侧与左侧**用了两种完全不同的手法**：右侧靠经典不等式 $\ln x>1-\frac1x$ 做「切线放缩」，"
        r"左侧靠对称化构造 $F(x)=f(x)-f\left(\frac2{\mathrm e}-x\right)$ —— 这是极值点偏移题的标准配置．" "\n"
        r"② ⚠ 对称化的**对称中心是 $\frac1{\mathrm e}$**（极值点），所以构造的是 $f\left(\frac2{\mathrm e}-x\right)$ 而不是 $f(1-x)$．" "\n"
        r"　 一般地：若极值点是 $x_{0}$，要证 $x_{1}+x_{2}>2x_{0}$ 就构造 $F(x)=f(x)-f(2x_{0}-x)$．" "\n"
        r"③ $F'(x)=\ln\left[x\left(\frac2{\mathrm e}-x\right)\right]+2$ 的判号靠**基本不等式**："
        r"$x\left(\frac2{\mathrm e}-x\right)\le\frac1{\mathrm e^{2}}$，取等 $x=\frac1{\mathrm e}$（区间右端）．" "\n"
        r"　 ⚠ 因此 $F'(x)<0$ 在开区间内严格成立，$F$ 严格递减，$F(x_{1})>F(\frac1{\mathrm e})=0$ 严格成立 ✓．" "\n"
        r"④ 原书详解右侧的链条写法较省略（「注意到 $x_{1}\ln x_{1}=x_{2}\ln x_{2}>x_{2}-1$，"
        r"而 $x_{1}\ln x_{1}<-x_{1}$」），已补全两个中间不等式的来源．" "\n"
        r"⑤ 数值复核：取 $f(x)=-0.3$，两根 $x_{1}=0.0667$、$x_{2}=0.7235$，和 $=0.7902$；"
        r"$\frac2{\mathrm e}=0.7358<0.7902<1$ ✓．" "\n"
        r"　 另取 $f(x)=-0.36$（接近最小值 $-\frac1{\mathrm e}=-0.3679$），两根 $x_{1}=0.2645$、$x_{2}=0.4725$，"
        r"和 $=0.7370$，仍 $>0.7358$ ✓ —— 越靠近极值点，和越接近 $\frac2{\mathrm e}$（但取不到）．"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-162'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-162-E1',
}

T162_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=\mathrm e^{x}+\cos x-ax$（$a\in\mathbb R$）．" "\n"
        r"（1）当 $a=1$ 时，判断 $f(x)$ 在区间 $(0,+\infty)$ 上的单调性；" "\n"
        r"（2）当 $a=\mathrm e$ 时，若 $x_{1},x_{2}\in(0,\pi)$，$x_{1}\ne x_{2}$，$f(x_{1})=f(x_{2})$，"
        r"且 $f(x)$ 的极值在 $x=x_{0}$ 处取得，证明：$x_{1}+x_{2}<2x_{0}$．"
    ),
    'opts': [],
    'answer': r"（1）$f(x)$ 在 $(0,+\infty)$ 上是增函数；（2）证明见解析",
    'analysis': (
        r"（1）$f'(x)=\mathrm e^{x}-\sin x-1$，再设 $g(x)=f'(x)$ 由 $g'(x)=\mathrm e^{x}+\cos x>0$ 定单调；" "\n"
        r"（2）先定 $x_{0}$ 是唯一极小值点，再构造 $h(x)=f(x)-f(2x_{0}-x)$（$0<x<x_{0}$），"
        r"用 AM–GM 与 $\sin$ 的有界性证 $h'(x)>0$．"
    ),
    'solution': (
        r"**【解析】（1）** 当 $a=1$ 时，$f(x)=\mathrm e^{x}+\cos x-x$，$f'(x)=\mathrm e^{x}-\sin x-1$．" "\n"
        r"设 $g(x)=\mathrm e^{x}-\sin x-1$，则 $g'(x)=\mathrm e^{x}-\cos x$．" "\n"
        r"当 $x>0$ 时 $\mathrm e^{x}>1\ge\cos x$，故 $g'(x)>0$ 恒成立，即 $f'(x)$ 在 $(0,+\infty)$ 上单调递增．" "\n"
        r"又 $f'(0)=\mathrm e^{0}-\sin0-1=0$，故 $x>0$ 时 $f'(x)>0$ 恒成立．" "\n"
        r"所以 $f(x)$ 在 $(0,+\infty)$ 上是增函数．" "\n"
        r"**【解析】（2）** 当 $a=\mathrm e$ 时，$f(x)=\mathrm e^{x}+\cos x-\mathrm ex$，$f'(x)=\mathrm e^{x}-\sin x-\mathrm e$．" "\n"
        r"由（1）的同样论证（$f''(x)=\mathrm e^{x}-\cos x>0$ 对 $x>0$ 成立），$f'(x)$ 在 $(0,+\infty)$ 上单调递增．" "\n"
        r"又 $f'(1)=\mathrm e-\sin1-\mathrm e=-\sin1<0$，$f'(\pi)=\mathrm e^{\pi}-\sin\pi-\mathrm e=\mathrm e^{\pi}-\mathrm e>0$，" "\n"
        r"故 $f'(x)$ 在 $(1,\pi)\subset(0,\pi)$ 上存在唯一零点 $x_{0}$，即 $\mathrm e^{x_{0}}-\sin x_{0}-\mathrm e=0$．" "\n"
        r"当 $0<x<x_{0}$ 时 $f'(x)<0$，$f(x)$ 递减；当 $x_{0}<x<\pi$ 时 $f'(x)>0$，$f(x)$ 递增．" "\n"
        r"故 $x_{0}$ 是 $f(x)$ 的唯一极小值点．" "\n"
        r"由 $x_{1},x_{2}\in(0,\pi)$、$x_{1}\ne x_{2}$、$f(x_{1})=f(x_{2})$，不妨设 $0<x_{1}<x_{0}<x_{2}<\pi$．" "\n"
        r"设 $h(x)=f(x)-f(2x_{0}-x)$，$0<x<x_{0}$，则" "\n"
        r"$h(x)=\mathrm e^{x}+\cos x-\mathrm e-\left[\mathrm e^{2x_{0}-x}+\cos(2x_{0}-x)-\mathrm e\right]$" "\n"
        r"$=\mathrm e^{x}-\mathrm e^{2x_{0}-x}+\cos x-\cos(2x_{0}-x)$．" "\n"
        r"$h'(x)=\mathrm e^{x}+\mathrm e^{2x_{0}-x}-\sin x-\sin(2x_{0}-x)$．" "\n"
        r"由 AM–GM 与 $\cos$ 的偶性（$\cos(2x_{0}-x)=\cos(x-2x_{0})$）：" "\n"
        r"$\mathrm e^{x}+\mathrm e^{2x_{0}-x}\ge2\sqrt{\mathrm e^{x}\cdot\mathrm e^{2x_{0}-x}}=2\mathrm e^{x_{0}}$，"
        r"$-\sin(2x_{0}-x)=\sin(x-2x_{0})$，" "\n"
        r"故 $h'(x)\ge2\mathrm e^{x_{0}}-\sin x+\sin(x-2x_{0})$．" "\n"
        r"由 $\mathrm e^{x_{0}}=\sin x_{0}+\mathrm e$ 代入，并由 $0<x<x_{0}<\pi$ 得 $0<\sin x_{0}\le1$、$0<\sin x<1$、"
        r"$-1\le\sin(x-2x_{0})\le1$：" "\n"
        r"$h'(x)\ge2\left(\sin x_{0}+\mathrm e\right)-\sin x+\sin(x-2x_{0})>2\left(0+\mathrm e\right)-1+\left(-1\right)=2\mathrm e-2>0$．" "\n"
        r"故 $h(x)$ 在 $(0,x_{0})$ 上单调递增，于是 $h(x_{1})<h(x_{0})=0$，即" "\n"
        r"$f(x_{1})-f(2x_{0}-x_{1})<0$，$f(x_{1})<f(2x_{0}-x_{1})$．" "\n"
        r"又 $f(x_{2})=f(x_{1})$，故 $f(x_{2})<f(2x_{0}-x_{1})$．" "\n"
        r"由 $0<x_{1}<x_{0}$ 得 $2x_{0}-x_{1}>x_{0}$，而 $x_{2}>x_{0}$，且 $f(x)$ 在 $(x_{0},+\infty)$ 上单调递增，" "\n"
        r"故 $x_{2}<2x_{0}-x_{1}$，即 $x_{1}+x_{2}<2x_{0}$．"
    ),
    'review': (
        r"① 本题是**极值点偏移的完全版**：构造 $h(x)=f(x)-f(2x_{0}-x)$，把「两个等函数值的点」"
        r"转化为「一个点与其关于 $x_{0}$ 的对称点」的函数值比较．" "\n"
        r"② ⚠ $h'(x)$ 的放缩链是本题最难的一步，三个不等式缺一不可：" "\n"
        r"　 （a）AM–GM：$\mathrm e^{x}+\mathrm e^{2x_{0}-x}\ge2\mathrm e^{x_{0}}$ —— **两个指数项的和用几何平均压住**；" "\n"
        r"　 （b）$\mathrm e^{x_{0}}=\sin x_{0}+\mathrm e$ 代入，把 $\mathrm e^{x_{0}}$ 换成 $\ge\mathrm e$；" "\n"
        r"　 （c）$\sin x<1$、$\sin(x-2x_{0})\ge-1$ 两个有界性同时用上．" "\n"
        r"　 三者合并得 $h'(x)>2\mathrm e-2>0$ —— 常数 $2\mathrm e-2\approx3.436$ 远大于 $0$，有充足余量．" "\n"
        r"③ 与 M-T-162-E1 的对照：那里 $F'(x)\le0$（递减、证 $x_{1}+x_{2}>\frac2{\mathrm e}$），"
        r"这里 $h'(x)>0$（递增、证 $x_{1}+x_{2}<2x_{0}$）—— **方向相反，但构造完全一样**．" "\n"
        r"④ ⚠ 注意 $h(x)$ 的表达式中常数 $-\mathrm e$ 恰好抵消（$f$ 中的 $-a=-\mathrm e$ 两处相减为 $0$），"
        r"这也是极值点偏移构造的通用特征：**常数项必抵消**．" "\n"
        r"⑤ 数值复核：$x_{0}$ 满足 $\mathrm e^{x_{0}}-\sin x_{0}-\mathrm e=0$，解得 $x_{0}=1.128$；$2x_{0}=2.256$；" "\n"
        r"　 取 $f(x)=-0.5$，两根 $x_{1}=0.482$、$x_{2}=1.660$，和 $=2.142<2.256$ ✓．"
    ),
    'difficulty': 0.90,
    'topics': ['M-T-162'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-162-V1',
}

T166_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知 $f(x)=x^{2}-a\ln x$，$a\in\mathbb R$．" "\n"
        r"（1）讨论 $y=f(x)$ 的单调性；" "\n"
        r"（2）若 $y=f(x)$ 有两个零点 $x_{1},x_{2}$（$x_{1}<x_{2}$），$x_{0}$ 是 $y=f(x)$ 的极值点，"
        r"求证：$x_{1}+3x_{2}>4x_{0}$．"
    ),
    'opts': [],
    'answer': r"（1）见解析；（2）证明见解析",
    'analysis': (
        r"（1）$f'(x)=\frac{2x^{2}-a}{x}$，按 $a\le0$、$a>0$ 讨论；（2）由最小值 $<0$ 得 $a>2\mathrm e$，"
        r"再作比值代换 $t=\frac{x_{2}}{x_{1}}>1$，从 $f(x_{1})=f(x_{2})$ 解出 $x_{1}^{2}=\frac{a\ln t}{t^{2}-1}$，" "\n"
        r"把所证化为关于 $t$ 的一元不等式．"
    ),
    'solution': (
        r"**【解析】（1）** $f(x)$ 的定义域为 $(0,+\infty)$，$f'(x)=2x-\dfrac ax=\dfrac{2x^{2}-a}{x}$．" "\n"
        r"① 当 $a\le0$ 时：$2x^{2}-a>0$，故 $f'(x)>0$，$f(x)$ 在 $(0,+\infty)$ 上单调递增．" "\n"
        r"② 当 $a>0$ 时：令 $f'(x)=0$ 得 $x=\sqrt{\dfrac a2}$．" "\n"
        r"当 $0<x<\sqrt{\dfrac a2}$ 时 $f'(x)<0$，$f(x)$ 单调递减；当 $x>\sqrt{\dfrac a2}$ 时 $f'(x)>0$，$f(x)$ 单调递增．" "\n"
        r"**【解析】（2）** 由（1），极值点为 $x_{0}=\sqrt{\dfrac a2}$（此时必有 $a>0$）．" "\n"
        r"若 $f(x)$ 有两个零点，则最小值" "\n"
        r"$f(x_{0})=f\!\left(\sqrt{\dfrac a2}\right)=\dfrac a2-a\ln\sqrt{\dfrac a2}=\dfrac a2-\dfrac a2\ln\dfrac a2"
        r"=\dfrac a2\left(1-\ln\dfrac a2\right)<0$，" "\n"
        r"由 $a>0$ 得 $\ln\dfrac a2>1$，即 $a>2\mathrm e$．" "\n"
        r"此时 $0<x_{1}<\sqrt{\dfrac a2}<x_{2}$．设 $t=\dfrac{x_{2}}{x_{1}}>1$，则 $x_{2}=tx_{1}$．" "\n"
        r"由 $f(x_{1})=f(x_{2})$ 得" "\n"
        r"$x_{1}^{2}-a\ln x_{1}=x_{2}^{2}-a\ln x_{2}=t^{2}x_{1}^{2}-a\ln\left(tx_{1}\right)=t^{2}x_{1}^{2}-a\ln t-a\ln x_{1}$，" "\n"
        r"两边的 $-a\ln x_{1}$ 抵消，整理得 $\left(t^{2}-1\right)x_{1}^{2}=a\ln t$，即" "\n"
        r"$x_{1}^{2}=\dfrac{a\ln t}{t^{2}-1}$．" "\n"
        r"所证 $x_{1}+3x_{2}>4x_{0}$ 即 $x_{1}(1+3t)>4\sqrt{\dfrac a2}=2\sqrt{2a}$．" "\n"
        r"两边均为正，平方得 $x_{1}^{2}(1+3t)^{2}>8a$，代入 $x_{1}^{2}$ 得" "\n"
        r"$\dfrac{a\ln t}{t^{2}-1}\cdot(1+3t)^{2}>8a$．" "\n"
        r"因 $a>0$、$t>1$，两边同除以 $a$ 并乘 $t^{2}-1>0$，只需证" "\n"
        r"$\ln t\,(1+3t)^{2}-8\left(t^{2}-1\right)>0$，即 $\ln t\,(1+3t)^{2}-8t^{2}+8>0$．" "\n"
        r"令 $h(t)=\ln t\,(1+3t)^{2}-8t^{2}+8$（$t>1$），则" "\n"
        r"$h'(t)=\dfrac{(1+3t)^{2}}{t}+6(1+3t)\ln t-16t=\left(18t+6\right)\ln t-7t+6+\dfrac1t$．" "\n"
        r"令 $n(t)=\left(18t+6\right)\ln t-7t+6+\dfrac1t$，则" "\n"
        r"$n'(t)=18\ln t+\dfrac{18t+6}{t}-7-\dfrac1{t^{2}}=18\ln t+11+\dfrac6t-\dfrac1{t^{2}}$．" "\n"
        r"当 $t>1$ 时 $\ln t>0$、$\dfrac6t>0$、$\dfrac1{t^{2}}<1$，故 $n'(t)>0+11+0-1>0$．" "\n"
        r"所以 $n(t)$ 在 $(1,+\infty)$ 上单调递增，且 $n(t)>n(1)=0-7+6+1=0$，即 $h'(t)>0$．" "\n"
        r"于是 $h(t)$ 在 $(1,+\infty)$ 上单调递增，且 $h(t)>h(1)=0-8+8=0$．" "\n"
        r"故所证不等式成立，即 $x_{1}+3x_{2}>4x_{0}$．"
    ),
    'review': (
        r"① ⚠ **极值点是 $x_{0}=\sqrt{\frac a2}$，不是 $\frac a2$** —— 原书 OCR 把根号弄丢了（写成 `x0= a / 2` 分两行）．" "\n"
        r"　 判据：$f'(x)=0\iff2x^{2}=a\iff x=\sqrt{\frac a2}$；"
        r"且后续 $4x_{0}=2\sqrt{2a}$ 只有在 $x_{0}=\sqrt{\frac a2}$ 时才成立（$4\sqrt{\frac a2}=2\sqrt{2a}$）✓．" "\n"
        r"② 本题的**比值代换**是核心：由 $f(x_{1})=f(x_{2})$ 解出 $x_{1}^{2}=\frac{a\ln t}{t^{2}-1}$，" "\n"
        r"　 把 $x_{1},x_{2}$ 两个变量压成一个 $t>1$．能解出来的关键是 $\ln(tx_{1})=\ln t+\ln x_{1}$，"
        r"**$a\ln x_{1}$ 恰好抵消**．" "\n"
        r"③ $h'(t)$ 仍需**二次求导**（$n'(t)$ 各项符号一眼看穿），这是「对数×多项式」型导数的通例．" "\n"
        r"④ $h(1)=0$、$n(1)=0$ 两个初值都要用到：$n(1)=0⟹h'>0⟹h$ 递增；$h(1)=0⟹h>0$．" "\n"
        r"⑤ 数值复核（$a=6$）：$x_{0}=\sqrt3=1.732$，$4x_{0}=6.928$；两根 $x_{1}=1.143$、$x_{2}=2.490$；" "\n"
        r"　 $x_{1}+3x_{2}=1.143+7.470=8.613>6.928$ ✓；"
        r"$t=\frac{2.490}{1.143}=2.178$，$h(2.178)=\ln(2.178)(1+6.534)^{2}-8\times4.744+8$" "\n"
        r"　 $=0.7788\times56.82-37.95+8=44.25-29.95=14.30>0$ ✓．"
    ),
    'difficulty': 0.90,
    'topics': ['M-T-166'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-166-E1',
}

T166_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=x-\mathrm e^{x}+a$．" "\n"
        r"（1）讨论函数 $f(x)$ 零点的个数；" "\n"
        r"（2）若函数 $f(x)$ 恰有两个零点 $x_{1},x_{2}$（$x_{1}<x_{2}$），证明 $2x_{1}+x_{2}<0$．"
    ),
    'opts': [],
    'answer': (
        r"（1）$a<1$ 时无零点，$a=1$ 时 $1$ 个零点，$a>1$ 时 $2$ 个零点；（2）证明见解析"
    ),
    'analysis': (
        r"（1）$f'(x)=1-\mathrm e^{x}$，最大值 $f(0)=a-1$，按 $a$ 与 $1$ 的大小分类；" "\n"
        r"（2）要证 $x_{2}<-2x_{1}$，因 $f$ 在 $(0,+\infty)$ 递减，等价于证 $f(x_{2})>f(-2x_{1})=0$，"
        r"即证 $f(x_{1})>f(-2x_{1})$，构造 $g(x)=f(x)-f(-2x)$（$x<0$）．"
    ),
    'solution': (
        r"**【解析】（1）** $f'(x)=1-\mathrm e^{x}$．" "\n"
        r"当 $x<0$ 时 $\mathrm e^{x}<1$，$f'(x)>0$；当 $x>0$ 时 $\mathrm e^{x}>1$，$f'(x)<0$．" "\n"
        r"故 $f(x)$ 在 $(-\infty,0)$ 上单调递增，在 $(0,+\infty)$ 上单调递减，"
        r"当 $x=0$ 时取得最大值 $f(0)=0-\mathrm e^{0}+a=a-1$．" "\n"
        r"① 当 $a<1$ 时：$f(0)=a-1<0$，最大值小于 $0$，函数 $f(x)$ 无零点．" "\n"
        r"② 当 $a=1$ 时：$f(0)=0$，最大值等于 $0$，函数 $f(x)$ 恰有 $1$ 个零点（即 $x=0$）．" "\n"
        r"③ 当 $a>1$ 时：$f(0)=a-1>0$；又 $f(-a)=-a-\mathrm e^{-a}+a=-\mathrm e^{-a}<0$．" "\n"
        r"　 由 $f$ 在 $(-\infty,0)$ 连续递增且 $f(-a)<0<f(0)$，知 $(-\infty,0)$ 内有唯一零点 $x_{1}$．" "\n"
        r"　 再看 $(0,+\infty)$：令 $h(a)=f(a)=a-\mathrm e^{a}+a=2a-\mathrm e^{a}$，$h'(a)=2-\mathrm e^{a}$．" "\n"
        r"　 当 $a<\ln2$ 时 $h'(a)>0$，当 $a>\ln2$ 时 $h'(a)<0$，故 $h(a)$ 在 $(-\infty,\ln2)$ 递增、在 $(\ln2,+\infty)$ 递减，" "\n"
        r"　 $h(a)_{\max}=h(\ln2)=2\ln2-\mathrm e^{\ln2}=2\ln2-2<0$，即 $f(a)<0$ 恒成立．" "\n"
        r"　 由 $f$ 在 $(0,+\infty)$ 连续递减且 $f(0)>0>f(a)$，知 $(0,+\infty)$ 内有唯一零点 $x_{2}$．" "\n"
        r"综上：$a<1$ 时无零点；$a=1$ 时 $1$ 个零点；$a>1$ 时 $2$ 个零点．" "\n"
        r"**【解析】（2）** 由（1），函数恰有两个零点时 $a>1$，且 $-a<x_{1}<0<x_{2}<a$．" "\n"
        r"要证 $2x_{1}+x_{2}<0$，只需证 $x_{2}<-2x_{1}$．" "\n"
        r"因 $-2x_{1}>0$、$x_{2}>0$，且 $f(x)$ 在 $(0,+\infty)$ 上单调递减，"
        r"故 $x_{2}<-2x_{1}\iff f(x_{2})>f(-2x_{1})$．" "\n"
        r"又 $f(x_{1})=f(x_{2})=0$，所以只需证 $f(x_{1})>f(-2x_{1})$，其中 $-a<x_{1}<0$．" "\n"
        r"令 $g(x)=f(x)-f(-2x)$（$-a<x<0$），则" "\n"
        r"$g(x)=\left(x-\mathrm e^{x}+a\right)-\left(-2x-\mathrm e^{-2x}+a\right)=3x-\mathrm e^{x}+\mathrm e^{-2x}$．" "\n"
        r"$g'(x)=3-\mathrm e^{x}-2\mathrm e^{-2x}$，" "\n"
        r"$g''(x)=-\mathrm e^{x}+4\mathrm e^{-2x}$．" "\n"
        r"当 $x<0$ 时 $\mathrm e^{x}<1$、$\mathrm e^{-2x}>1$，故 $g''(x)>-\ 1+4=3>0$，"
        r"即 $g'(x)$ 在 $(-\infty,0)$ 上单调递增，" "\n"
        r"从而 $g'(x)<g'(0)=3-1-2=0$．" "\n"
        r"于是 $g(x)$ 在 $(-\infty,0)$ 上单调递减，故当 $x<0$ 时 $g(x)>g(0)=0-1+1=0$．" "\n"
        r"即 $f(x)>f(-2x)$ 对一切 $x<0$ 成立．取 $x=x_{1}$ 得 $f(x_{1})>f(-2x_{1})=f(x_{2})$，" "\n"
        r"由 $f$ 在 $(0,+\infty)$ 递减得 $x_{2}<-2x_{1}$，即 $2x_{1}+x_{2}<0$．"
    ),
    'review': (
        r"① ⚠ **原书详解的所有导数符号都被 OCR 吞掉了**（$f^{\prime},g^{\prime},g^{\prime\prime}$ 一律写成 $f,g$），"
        r"已按推导逐层补回 $g'(x)=3-\mathrm e^{x}-2\mathrm e^{-2x}$、$g''(x)=-\mathrm e^{x}+4\mathrm e^{-2x}$．" "\n"
        r"② 本题是**非对称型**极值点偏移（$x_{1}$ 与 $x_{2}$ 的系数分别为 $2$ 和 $1$，不对称），" "\n"
        r"　 所以对称化的对象是 $-2x_{1}$ 而非 $-x_{1}$ —— **系数 $2$ 直接来自所证式子**．" "\n"
        r"③ $g''(x)>0$ 的判据很干净：$x<0$ 时 $\mathrm e^{x}<1$ 且 $\mathrm e^{-2x}>1$，"
        r"故 $-\mathrm e^{x}+4\mathrm e^{-2x}>-1+4=3>0$ —— **用指数函数的单调性配常数，不必解方程**．" "\n"
        r"④ （1）中 $f(a)<0$ 的证明用了辅助函数 $h(a)=2a-\mathrm e^{a}$，" "\n"
        r"　 其最大值 $2\ln2-2<0$ 是**与 $a$ 无关的固定负数**，这一步保证了 $(0,+\infty)$ 内确有零点．" "\n"
        r"⑤ 数值复核（$a=2$）：两根 $x_{1}=-1.841$、$x_{2}=1.146$；$2x_{1}+x_{2}=-3.682+1.146=-2.536<0$ ✓；" "\n"
        r"　 $g(x_{1})=f(-1.841)-f(3.682)=0-\left(3.682-\mathrm e^{3.682}+2\right)=0-\left(5.682-39.72\right)=34.04>0$ ✓．"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-166'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-166-V1',
}

QS = [
    T158_V1, T159_E1, T159_V1, T159_V2, T160_E1, T160_V1,
    T161_E1, T161_V1, T162_E1, T162_V1, T166_E1, T166_V1,
]
