# -*- coding: utf-8 -*-
r"""第 117 批：导数区 14 题

    选择 6 题（M-T-127 / M-T-138 / M-T-139 / M-T-140 / M-T-142 / M-T-143）
    填空 2 题（M-T-131 ×2）
    解答 6 题（M-T-147 / M-T-156 / M-T-158 / M-T-161 / M-T-162 / M-T-166）

    python3 tools/run_batch.py 117

## 选题依据

用 `pick_batch.py`（pages 策略 + skipped 排除）筛出，原文集中在 p093–p135 的导数区。

## 本批没录的 2 题（不硬凑）

**M-T-143-V1**（p109）：题干提取为 $x^{2}\ln y-\ln x-ay^{2}=0$，而详解走的是
$e^{y-x}-a\mathrm e^{2y-x}=0$、$a=-\dfrac12t\mathrm e^{t}$（$t=2(x-y)$）——
题干与详解是两道不同的题，提取发生错位，无法判定原题，已登记 `skipped.json`。

**M-T-155-V2**（p120）：题干只有两问（求 $a$ 与极值；证 $x>0$ 时 $x^{2}<\mathrm e^{x}$），
但 `ans` 给出三段（含「(3) 略」），且详解只有 (1)(2)。第三问内容缺失，已登记。

## ★★ 本批最值钱的一条：$f(m)=g(n)$ 型统一设「公共值 $t$」（M-T-138-E1）

已知 $f(x)=\ln x+1$、$g(x)=2\mathrm e^{x-\frac12}$，若 $f(m)=g(n)$，求 $m-n$ 最小值。

设 $f(m)=g(n)=t$，则 $t>0$，$m=\mathrm e^{t-1}$，$n=\ln\dfrac t2+\dfrac12=\ln t-\ln2+\dfrac12$：

$$m-n=\mathrm e^{t-1}-\ln t+\ln2-\tfrac12,\qquad h'(t)=\mathrm e^{t-1}-\tfrac1t,\quad h'(1)=0$$

$h''(t)=\mathrm e^{t-1}+\dfrac1{t^{2}}>0$ ⟹ $h'$ 严格递增，故 $t=1$ 是唯一驻点即最小点。

> ⭐⭐ 通法：**两个函数值相等，就设公共值为 $t$，把两个自变量都反解成 $t$ 的函数**，
> 双变量之差立刻变成单变量函数。判据是「反解能否显式写出」——$\ln x$ 与 $\mathrm e^{x}$
> 互为反函数，正是为这一步设计的。

## ★★ 第二条：先造「同构函数」再比大小（M-T-127-V2）

$\log_{27}x\ge k\cdot3^{kx-1}\iff\log_{3}x\ge k\cdot3^{kx}$，同乘 $x>0$：

$$x\log_{3}x\ge kx\cdot3^{kx}\ \Longrightarrow\ 3^{\log_{3}x}\!\cdot\log_{3}x\ \ge\ 3^{kx}\cdot kx$$

两边都是 $\varphi(u)=u\cdot3^{u}$ 的函数值！$\varphi'(u)=3^{u}(1+u\ln3)>0$ ⟹ $\log_{3}x\ge kx$。

> ⭐⭐ 通法：**看到 $x$ 与 $3^{x}$（或 $x$ 与 $\mathrm e^{x}$、$x$ 与 $\ln x$）相乘，
> 就想 $x=3^{\log_{3}x}$，把式子改写成同一个函数在两个点上的取值**。
> 这是「指对混合不等式」最硬的一招，比取对数通用得多。

## ★★ 第三条：$\dfrac{\mathrm e^{x}}x$ 与 $\dfrac{\ln x}x$ 是两个标准母函数（M-T-131-V2/V3）

- V2：$a\le\dfrac{\mathrm e^{x-1}}x+\ln x-x=\dfrac1{\mathrm e}\cdot\dfrac{\mathrm e^{x}}x+\ln\dfrac x{\mathrm e^{x}}$，
  设 $t=\dfrac{\mathrm e^{x}}x\ge\mathrm e$，则右端 $=\dfrac t{\mathrm e}-\ln t$，在 $t\ge\mathrm e$ 上递增，最小值为 $0$
- V3：$a\le\mathrm e^{x-1}-\dfrac{\ln x}x$，分子导数 $h(x)=x^{2}\mathrm e^{x-1}+\ln x-1$ 递增且 $h(1)=0$

> ⭐⭐ 两题**都归结为「分离参数 + 求一个标准母函数的最值」**，且最值点都落在 $x=1$。
> 差别只在：V2 用换元 $t=\dfrac{\mathrm e^{x}}x$（因为 $\dfrac{\mathrm e^{x}}x$ 与 $\ln\dfrac x{\mathrm e^{x}}$ 互为倒数关系），
> V3 直接求导（因为分子导数恰好能因式出 $h(1)=0$）。

## ★★ 第四条：$|\ln x|$ 型零点个数按 $(0,1)$ 与 $(1,+\infty)$ 分别数（M-T-142-V2）

$f(x)=\mathrm e^{x}(|\ln x|-m)-x=0\iff|\ln x|=g(x)$，其中 $g(x)=\dfrac x{\mathrm e^{x}}+m$。

$g$ 在 $(0,1)$ 递增、在 $(1,+\infty)$ 递减，$g(1)=\dfrac1{\mathrm e}+m$；
$|\ln x|$ 在 $(0,1)$ 由 $+\infty$ 递减到 $0$、在 $(1,+\infty)$ 由 $0$ 递增到 $+\infty$。

- 在 $(1,+\infty)$：有交点 $\iff g(1)>0\iff m>-\dfrac1{\mathrm e}$
- 在 $(0,1)$：只要 $m>-\dfrac1{\mathrm e}$ 也恰好一个（$|\ln x|-g(x)$ 递减，两端异号）

> ⚠ 原书详解写「$g$ 从负无穷增大到 $\frac1{\mathrm e}+m$」是**错的**：
> $x\to0^{+}$ 时 $g(x)\to m$（有限值），不是 $-\infty$。结论 $m>-\dfrac1{\mathrm e}$ 无误，路径需更正。
> 我在 review 里另给了逐段清点。

## ★★ 第五条：$1/\ln(1-x)+1/x<1$ 的证明（M-T-161-V1）

$$\frac1{\ln(1-x)}+\frac1x-1=\frac{x+\ln(1-x)-x\ln(1-x)}{x\ln(1-x)}$$

分母：无论 $x<0$ 还是 $0<x<1$，$x\ln(1-x)<0$ 恒成立；
分子 $t(x)$ 满足 $t'(x)=-\ln(1-x)$，故 $x<0$ 时 $t$ 递减、$0<x<1$ 时 $t$ 递增，
而 $t(0)=0$ ⟹ **分子恒正**。于是 $h(x)<0$，即 $\dfrac1{\ln(1-x)}+\dfrac1x<1$。

配 $2+\sin x\ge1$，一步得 $F(x)<2$。

> ⭐⭐ 通法：**分式通分后「分子分母各自定号」**，比通分前分别估计强得多。
> 而 $t'(x)=-\ln(1-x)$ 的化简（$1-\dfrac1{1-x}+\dfrac x{1-x}=0$）是关键一步。
"""

# ---------------------------------------------------------------- M-T-127-V2
T127_V2 = {
    'type': '选择',
    'stem_text': (
        r"设 $k>0$，若存在正实数 $x$，使得不等式 $\log_{27}x-k\cdot3^{kx-1}\ge0$ 成立，"
        r"则 $k$ 的最大值为（　　）"
    ),
    'opts': [
        ['A', r"$\dfrac1{\mathrm e\ln3}$"],
        ['B', r"$\dfrac{\ln3}{\mathrm e}$"],
        ['C', r"$\dfrac{\mathrm e}{\ln3}$"],
        ['D', r"$\dfrac{\ln3}2$"],
    ],
    'answer': 'A',
    'analysis': (
        r"$\log_{27}x=\dfrac13\log_{3}x$，故原不等式等价于 $\log_{3}x\ge k\cdot3^{kx}$；"
        r"同乘 $x>0$ 后两边配成同一个函数 $\varphi(u)=u\cdot3^{u}$ 在两个点上的取值，"
        r"由单调性得 $\log_{3}x\ge kx$，再分离参数求 $\dfrac{\log_{3}x}x$ 的最大值。"
    ),
    'solution': (
        r"$\because\log_{27}x=\dfrac{\log_{3}x}{\log_{3}27}=\dfrac13\log_{3}x$，" "\n"
        r"$\therefore\log_{27}x\ge k\cdot3^{kx-1}\iff\dfrac13\log_{3}x\ge\dfrac{k\cdot3^{kx}}3"
        r"\iff\log_{3}x\ge k\cdot3^{kx}$．" "\n"
        r"$\because x>0$，两边同乘 $x$ 得 $x\log_{3}x\ge kx\cdot3^{kx}$．" "\n"
        r"注意到 $x=3^{\log_{3}x}$，故左边 $=3^{\log_{3}x}\cdot\log_{3}x$，"
        r"右边 $=3^{kx}\cdot kx$．" "\n"
        r"设 $\varphi(u)=u\cdot3^{u}$，则不等式即 $\varphi(\log_{3}x)\ge\varphi(kx)$．" "\n"
        r"$\varphi'(u)=3^{u}+u\cdot3^{u}\ln3=3^{u}(1+u\ln3)>0$（$u>0$），"
        r"故 $\varphi$ 在 $(0,+\infty)$ 上为增函数，" "\n"
        r"$\therefore\log_{3}x\ge kx$，且由 $k>0,x>0$ 知 $kx>0$，故 $k\le\dfrac{\log_{3}x}x$．" "\n"
        r"设 $g(x)=\dfrac{\log_{3}x}x=\dfrac{\ln x}{x\ln3}$，则 "
        r"$g'(x)=\dfrac{\dfrac1{\ln3}\cdot x-\log_{3}x}{x^{2}}"
        r"=\dfrac{\dfrac1{\ln3}-\dfrac{\ln x}{\ln3}}{x^{2}}=\dfrac{1-\ln x}{x^{2}\ln3}$．" "\n"
        r"由 $g'(x)>0$ 得 $0<x<\mathrm e$；由 $g'(x)<0$ 得 $x>\mathrm e$，"
        r"故 $g(x)_{\max}=g(\mathrm e)=\dfrac{\log_{3}\mathrm e}{\mathrm e}=\dfrac1{\mathrm e\ln3}$．" "\n"
        r"$\therefore k\le\dfrac1{\mathrm e\ln3}$，即 $k$ 的最大值为 $\dfrac1{\mathrm e\ln3}$，故选 A．"
    ),
    'review': (
        r"① ⭐⭐ **题眼是「两边配成同一个函数」**：$x\cdot\log_{3}x=3^{\log_{3}x}\cdot\log_{3}x$ "
        r"与 $kx\cdot3^{kx}$ 都是 $\varphi(u)=u\cdot3^{u}$ 的值，" "\n"
        r"  这一步把「指对混合不等式」变成了「函数值比大小」，是本题唯一的卡点 ✓✓" "\n"
        r"② 数值复核：$k=\dfrac1{\mathrm e\ln3}=0.334858$，取 $x=\mathrm e$，" "\n"
        r"  $\log_{27}\mathrm e=\dfrac1{\ln27}=0.303413$，" "\n"
        r"  $k\cdot3^{k\mathrm e-1}=0.334858\times3^{-0.089590}=0.303413$ —— **两者完全相等**，" "\n"
        r"  说明 $x=\mathrm e$ 正是取等点 ✓✓✓" "\n"
        r"③ ⭐⭐ **$g'(x)=\dfrac{1-\ln x}{x^{2}\ln3}$ 的分子不含 $\ln3$ 的幂次** —— "
        r"因为 $\log_{3}x=\dfrac{\ln x}{\ln3}$ 求导后 $\dfrac1{\ln3}$ 是常数因子，" "\n"
        r"  最大点永远是 $x=\mathrm e$，与底数无关。这是可推广的结论 ✓" "\n"
        r"④ ⚠ **$\log_{27}x\ge k\cdot3^{kx-1}$ 中 $3^{kx-1}=\dfrac{3^{kx}}3$**，"
        r"而左边 $\log_{27}x=\dfrac{\log_{3}x}3$ —— 两个 $\dfrac13$ 恰好约掉，" "\n"
        r"  这正是命题人把底数取成 $27$、指数取成 $kx-1$ 的原因（不是巧合）✓" "\n"
        r"**⭐⭐ 通法（指对混合不等式）**：" "\n"
        r"见到 $x$ 与 $a^{x}$（或 $x$ 与 $\ln x$）相乘，" "\n"
        r"  先把 $x$ 写成 $a^{\log_{a}x}$（或 $\mathrm e^{\ln x}$），" "\n"
        r"  把不等式两边配成 $\varphi(u)=u\cdot a^{u}$ 在两个点 $u_{1},u_{2}$ 上的取值，" "\n"
        r"  再用 $\varphi$ 的单调性把 $\varphi(u_{1})\ge\varphi(u_{2})$ 化成 $u_{1}\ge u_{2}$．"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-127'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-127-V2',
}

# ---------------------------------------------------------------- M-T-131-V2
T131_V2 = {
    'type': '填空',
    'stem_text': (
        r"已知函数 $f(x)=\mathrm e^{x-1}+x\ln x-x^{2}-ax$ 满足 $f(x)\ge0$ 恒成立，"
        r"则实数 $a$ 的取值范围是 ____"
    ),
    'opts': [],
    'answer': r"$(-\infty,0]$",
    'analysis': (
        r"分离参数得 $a\le\dfrac{\mathrm e^{x-1}}x+\ln x-x$，把 $\dfrac{\mathrm e^{x}}x$ 设为 $t$，"
        r"则 $\ln\dfrac x{\mathrm e^{x}}=-\ln t$，右端化为 $\dfrac t{\mathrm e}-\ln t$（$t\ge\mathrm e$），"
        r"在 $t\ge\mathrm e$ 上单调递增，最小值为 $0$．"
    ),
    'solution': (
        r"$\because\mathrm e^{x-1}+x\ln x-x^{2}-ax\ge0$ 恒成立（$x>0$），" "\n"
        r"$\therefore a\le\dfrac{\mathrm e^{x-1}+x\ln x-x^{2}}x=\dfrac{\mathrm e^{x-1}}x+\ln x-x$ 恒成立．" "\n"
        r"又 $\dfrac{\mathrm e^{x-1}}x+\ln x-x=\dfrac1{\mathrm e}\cdot\dfrac{\mathrm e^{x}}x+\ln\dfrac x{\mathrm e^{x}}$，" "\n"
        r"设 $t=\dfrac{\mathrm e^{x}}x$，则 $t'=\dfrac{\mathrm e^{x}(x-1)}{x^{2}}$，" "\n"
        r"当 $x>1$ 时 $t'>0$，$t=\dfrac{\mathrm e^{x}}x$ 为增函数；当 $0<x<1$ 时 $t'<0$，为减函数，" "\n"
        r"又 $x=1$ 时 $t=\mathrm e$，故 $t\ge\mathrm e$．" "\n"
        r"设 $g(t)=\dfrac t{\mathrm e}+\ln\dfrac1t=\dfrac t{\mathrm e}-\ln t$（$t\ge\mathrm e$），" "\n"
        r"则 $g'(t)=\dfrac1{\mathrm e}-\dfrac1t=\dfrac{t-\mathrm e}{\mathrm e t}\ge0$ 恒成立，" "\n"
        r"所以 $g(t)$ 在 $[\mathrm e,+\infty)$ 上单调递增，故 $g(t)\ge g(\mathrm e)=\dfrac{\mathrm e}{\mathrm e}-\ln\mathrm e=1-1=0$．" "\n"
        r"$\therefore a\le0$，即实数 $a$ 的取值范围为 $(-\infty,0]$．"
    ),
    'review': (
        r"① ⭐⭐ **换元 $t=\dfrac{\mathrm e^{x}}x$ 的动机**：式子中 $\dfrac{\mathrm e^{x}}x$ 与 "
        r"$\ln\dfrac x{\mathrm e^{x}}$ 互为倒数关系（后者 $=-\ln t$），" "\n"
        r"  换元后两个超越部分合并成 $\dfrac t{\mathrm e}-\ln t$，一下子从二元降为单元 ✓✓" "\n"
        r"② 数值复核：$a=0$ 时 $f(x)=\mathrm e^{x-1}+x\ln x-x^{2}$，" "\n"
        r"  $f(1)=1+0-1=0$；$f(0.8)=0.000216$；$f(0.5)=0.009957$；" "\n"
        r"  $f(1.2)=0.000189$；$f(2)=0.104576$ —— **最小值恰为 $0$，在 $x=1$ 处取到** ✓✓✓" "\n"
        r"③ ⭐⭐ **$\dfrac{\mathrm e^{x}}x$ 的最小值是 $\mathrm e$（在 $x=1$）**，"
        r"而 $\dfrac{\ln x}x$ 的最大值是 $\dfrac1{\mathrm e}$（在 $x=\mathrm e$）——" "\n"
        r"  两个标准母函数的最值点不同，极易记混，务必对比着背 ✓" "\n"
        r"④ ⚠ **$t$ 的范围是 $t\ge\mathrm e$ 不是 $t>0$**：$\dfrac{\mathrm e^{x}}x$ 在 $x>0$ 上的"
        r"值域就是 $[\mathrm e,+\infty)$，这一点决定了 $g'(t)\ge0$ 恒成立；" "\n"
        r"  若误写成 $t>0$，$g$ 在 $(0,\mathrm e)$ 上递减，会得出错误的下界 ✓" "\n"
        r"**⭐⭐ 通法（分离参数 + 双超越项）**：" "\n"
        r"当右端同时含 $\dfrac{\mathrm e^{x}}x$ 与 $\ln x-x$（即 $\ln\dfrac x{\mathrm e^{x}}$）时，" "\n"
        r"  一律设 $t=\dfrac{\mathrm e^{x}}x$，利用两者互为对数的相反数合并成一个单变量函数．"
    ),
    'difficulty': 0.82,
    'topics': ['M-T-131'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-131-V2',
}

# ---------------------------------------------------------------- M-T-131-V3
T131_V3 = {
    'type': '填空',
    'stem_text': (
        r"已知函数 $f(x)=\dfrac1{\mathrm e}\,x\mathrm e^{x}-\ln x-ax$，若对于任意 $x\in(0,+\infty)$，"
        r"不等式 $f(x)\ge0$ 恒成立，则实数 $a$ 的最大值为 ____"
    ),
    'opts': [],
    'answer': r"$1$",
    'analysis': (
        r"分离参数得 $a\le\mathrm e^{x-1}-\dfrac{\ln x}x$，求导后分子为 "
        r"$h(x)=x^{2}\mathrm e^{x-1}+\ln x-1$，它严格递增且 $h(1)=0$，"
        r"故 $x=1$ 是最小点，最小值为 $1$．"
    ),
    'solution': (
        r"依题意，对任意 $x\in(0,+\infty)$，$f(x)\ge0$ 即 "
        r"$a\le\dfrac{\dfrac1{\mathrm e}x\mathrm e^{x}-\ln x}x=\mathrm e^{x-1}-\dfrac{\ln x}x$ 恒成立．" "\n"
        r"令 $g(x)=\mathrm e^{x-1}-\dfrac{\ln x}x$（$x>0$），则 $a\le g(x)_{\min}$．" "\n"
        r"$g'(x)=\mathrm e^{x-1}-\dfrac{1-\ln x}{x^{2}}=\dfrac{x^{2}\mathrm e^{x-1}+\ln x-1}{x^{2}}$．" "\n"
        r"令 $h(x)=x^{2}\mathrm e^{x-1}+\ln x-1$（$x>0$），" "\n"
        r"则 $h'(x)=(x^{2}+2x)\mathrm e^{x-1}+\dfrac1x>0$，所以 $h(x)$ 在 $(0,+\infty)$ 上单调递增，" "\n"
        r"又 $h(1)=1\cdot\mathrm e^{0}+\ln1-1=1+0-1=0$，" "\n"
        r"$\therefore$ 当 $x\in(0,1)$ 时 $h(x)<0$，即 $g'(x)<0$，$g(x)$ 单调递减；" "\n"
        r"当 $x\in(1,+\infty)$ 时 $h(x)>0$，即 $g'(x)>0$，$g(x)$ 单调递增．" "\n"
        r"$\therefore g(x)_{\min}=g(1)=\mathrm e^{0}-\dfrac{\ln1}1=1-0=1$．" "\n"
        r"$\therefore a\le1$，即实数 $a$ 的最大值为 $1$．"
    ),
    'review': (
        r"① ⭐⭐ **$h(1)=0$ 是设计的**：$x^{2}\mathrm e^{x-1}$ 在 $x=1$ 时等于 $1$、$\ln1=0$，"
        r"两项正确好凑成 $0$。这是「最小点落在 $x=1$」的信号，" "\n"
        r"  也是能否因式分解的检验点 —— 若代入 $x=1$ 不为 $0$，说明分离参数或求导有误 ✓✓" "\n"
        r"② 数值复核：$a=1$ 时 $f(x)=\dfrac{x\mathrm e^{x}}{\mathrm e}-\ln x-x$，" "\n"
        r"  $f(1)=1-0-1=0$；$f(0.5)=0.496413$；$f(0.8)=0.078128$；" "\n"
        r"  $f(1.2)=0.083362$；$f(2)=2.743416$ —— **最小值恰为 $0$，在 $x=1$ 处取到** ✓✓✓" "\n"
        r"③ ⭐⭐ **与 V2 对照**：两题都是「$f(x)\ge0$ 恒成立求 $a$，最值点都在 $x=1$」，" "\n"
        r"  但 V2 靠换元 $t=\dfrac{\mathrm e^{x}}x$，V3 靠分子 $h(x)$ 递增且 $h(1)=0$。" "\n"
        r"  差别在于：V2 的两项（$\dfrac{\mathrm e^{x}}x$ 与 $\ln\dfrac x{\mathrm e^{x}}$）可合并，V3 的两项不可合并 ✓" "\n"
        r"④ ⚠ **$g'(x)$ 的分子不能漏 $x^{2}$**：$\left(\dfrac{\ln x}x\right)'=\dfrac{1-\ln x}{x^{2}}$，" "\n"
        r"  通分时 $\mathrm e^{x-1}=\dfrac{x^{2}\mathrm e^{x-1}}{x^{2}}$，分子才是 $x^{2}\mathrm e^{x-1}+\ln x-1$ ✓" "\n"
        r"**⭐⭐ 通法（分子定号法）**：" "\n"
        r"分离参数后若导数是分式，且分子的导数恒正（恒负），" "\n"
        r"  就先找分子的零点（本题凑巧是 $x=1$），用一个点把整个定义域切成两段定号．"
    ),
    'difficulty': 0.80,
    'topics': ['M-T-131'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-131-V3',
}

# ---------------------------------------------------------------- M-T-138-E1
T138_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知函数 $f(x)=\ln x+1$，$g(x)=2\mathrm e^{x-\frac12}$，若 $f(m)=g(n)$ 成立，"
        r"则 $m-n$ 的最小值是（　　）"
    ),
    'opts': [
        ['A', r"$\dfrac12+\ln2$"],
        ['B', r"$\mathrm e-2$"],
        ['C', r"$\ln2-\dfrac12$"],
        ['D', r"$\mathrm e-\dfrac12$"],
    ],
    'answer': 'A',
    'analysis': (
        r"设 $f(m)=g(n)=t$，则 $t>0$，$m=\mathrm e^{t-1}$，$n=\ln\dfrac t2+\dfrac12$，"
        r"于是 $m-n$ 是 $t$ 的一元函数；求导后由 $h'(1)=0$ 与 $h''>0$ 知 $t=1$ 是最小点．"
    ),
    'solution': (
        r"设 $f(m)=g(n)=t$，则 $t>0$．" "\n"
        r"由 $f(m)=\ln m+1=t$ 得 $m=\mathrm e^{t-1}$；" "\n"
        r"由 $g(n)=2\mathrm e^{n-\frac12}=t$ 得 $\mathrm e^{n-\frac12}=\dfrac t2$，"
        r"即 $n-\dfrac12=\ln\dfrac t2$，故 $n=\ln t-\ln2+\dfrac12$．" "\n"
        r"$\therefore m-n=\mathrm e^{t-1}-\ln t+\ln2-\dfrac12$．" "\n"
        r"令 $h(t)=\mathrm e^{t-1}-\ln t+\ln2-\dfrac12$（$t>0$），" "\n"
        r"则 $h'(t)=\mathrm e^{t-1}-\dfrac1t$，$h''(t)=\mathrm e^{t-1}+\dfrac1{t^{2}}>0$ 恒成立，" "\n"
        r"$\therefore h'(t)$ 在 $(0,+\infty)$ 上是增函数，又 $h'(1)=\mathrm e^{0}-1=0$，" "\n"
        r"$\therefore$ 当 $t\in(0,1)$ 时 $h'(t)<0$，$h(t)$ 单调递减；" "\n"
        r"当 $t\in(1,+\infty)$ 时 $h'(t)>0$，$h(t)$ 单调递增．" "\n"
        r"$\therefore h(t)_{\min}=h(1)=\mathrm e^{0}-\ln1+\ln2-\dfrac12=1-0+\ln2-\dfrac12=\dfrac12+\ln2$．" "\n"
        r"即 $m-n$ 的最小值为 $\dfrac12+\ln2$，故选 A．"
    ),
    'review': (
        r"① ⭐⭐ **题眼是「设公共值 $t$」**：$f(m)=g(n)$ 给出的是 $m,n$ 之间的一个约束，" "\n"
        r"  设公共值为 $t$ 后可把 $m,n$ 分别反解成 $t$ 的函数，双变量之差立刻降为单变量 ✓✓" "\n"
        r"② 数值复核：$t=1$ 时 $m=\mathrm e^{0}=1$，$n=\ln\dfrac12+\dfrac12=0.5-0.693147=-0.193147$，" "\n"
        r"  $m-n=1.193147$；而 $\dfrac12+\ln2=0.5+0.693147=1.193147$ —— **完全相等** ✓✓✓" "\n"
        r"  另取 $t=2$：$m=\mathrm e=2.718282$，$n=\ln1+\dfrac12=0.5$，$m-n=2.218282>1.193147$ ✓" "\n"
        r"③ ⭐⭐ **$h'(1)=0$ 不是凑的**：$h'(t)=\mathrm e^{t-1}-\dfrac1t$ 在 $t=1$ 时两项都是 $1$。" "\n"
        r"  一般地，若 $m=\mathrm e^{\alpha(t)}$、$n=\ln\beta(t)$，则 $h'(t)$ 总形如「指数 $-$ 分式」，" "\n"
        r"  驻点往往在指数与分式同时取到 $1$ 的地方 ✓" "\n"
        r"④ ⚠ **$g(x)$ 是 $2\mathrm e^{x-\frac12}$ 不是 $2\mathrm e^{x}-\dfrac12$**：" "\n"
        r"  按后者无法反解出整齐的 $n$（会得到 $n=\ln\dfrac{t+\frac12}2$，"
        r"最值点也就不在 $t=1$），与答案 $\dfrac12+\ln2$ 不符 ✓" "\n"
        r"⑤ ⭐⭐ **$h''>0$ 用来保证驻点唯一**：只看 $h'(1)=0$ 不能说明是最小值点，" "\n"
        r"  必须配 $h'$ 严格递增（即 $h''>0$）才能断定先减后增 ✓" "\n"
        r"**⭐⭐ 通法（两个函数值相等型）**：" "\n"
        r"见到 $f(m)=g(n)$ 且 $f,g$ 都可逆，就设公共值为 $t$，" "\n"
        r"  用反函数把 $m=f^{-1}(t)$、$n=g^{-1}(t)$ 写出，目标量化成 $t$ 的一元函数后再求导．"
    ),
    'difficulty': 0.83,
    'topics': ['M-T-138'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-138-E1',
}

# ---------------------------------------------------------------- M-T-139-V2
T139_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知 $f(x)=x\mathrm e^{-x}$（$x\in\mathbf R$），若 $x_{1}\ne x_{2}$，且 $f(x_{1})=f(x_{2})$，"
        r"则 $x_{1}+x_{2}$ 与 $2$ 的关系为（　　）"
    ),
    'opts': [
        ['A', r"$x_{1}+x_{2}>2$"],
        ['B', r"$x_{1}+x_{2}\ge2$"],
        ['C', r"$x_{1}+x_{2}<2$"],
        ['D', r"大小不确定"],
    ],
    'answer': 'A',
    'analysis': (
        r"先由导数求出 $f$ 在 $x=1$ 处取极大值（也是最大值），故两根分居 $1$ 两侧；"
        r"再比较 $f(1-x)$ 与 $f(1+x)$（$x\in(0,1)$），由 $f(1+x)>f(1-x)$ 与右侧单调递减"
        r"推出与 $f(1-x)$ 相等的那个根必在 $1+x$ 的右边，从而 $x_{1}+x_{2}>2$．"
    ),
    'solution': (
        r"$f'(x)=\mathrm e^{-x}-x\mathrm e^{-x}=(1-x)\mathrm e^{-x}$，令 $f'(x)=0$ 得 $x=1$．" "\n"
        r"当 $x>1$ 时 $f'(x)<0$；当 $x<1$ 时 $f'(x)>0$，" "\n"
        r"所以 $f(x)$ 在 $(-\infty,1)$ 上递增、在 $(1,+\infty)$ 上递减，"
        r"在 $x=1$ 处取得极大值也是最大值 $f(1)=\dfrac1{\mathrm e}$．" "\n"
        r"又 $f(0)=0$，当 $x\to+\infty$ 时 $f(x)\to0^{+}$；当 $x\to-\infty$ 时 $f(x)\to-\infty$．" "\n"
        r"若 $x_{1}\ne x_{2}$ 且 $f(x_{1})=f(x_{2})$，不失一般性设 $x_{1}<x_{2}$，" "\n"
        r"则必有 $0<x_{1}<1<x_{2}$（因 $f$ 在 $(-\infty,0]$ 上由 $-\infty$ 增到 $0$，"
        r"与 $(0,1)$ 上的正值无重复）．" "\n"
        r"对任意 $x\in(0,1)$，考察两点 $1-x$ 与 $1+x$：" "\n"
        r"$f(1+x)-f(1+x)=\dfrac{1+x}{\mathrm e^{1+x}}-\dfrac{1-x}{\mathrm e^{1-x}}"
        r"=\dfrac{1+x-(1-x)\mathrm e^{2x}}{\mathrm e^{1+x}}$．" "\n"
        r"令分子 $G(x)=1+x-(1-x)\mathrm e^{2x}$（$x\in(0,1)$），" "\n"
        r"则 $G'(x)=1+\mathrm e^{2x}-2(1-x)\mathrm e^{2x}=1+(2x-1)\mathrm e^{2x}$，" "\n"
        r"$G''(x)=2\mathrm e^{2x}+2(2x-1)\mathrm e^{2x}=4x\mathrm e^{2x}>0$（$x\in(0,1)$）．" "\n"
        r"又 $G'(0)=1+(-1)\cdot1=0$，故 $x>0$ 时 $G'(x)>0$，"
        r"从而 $G$ 在 $(0,1)$ 上单调递增，$G(x)>G(0)=1+0-1=0$．" "\n"
        r"$\therefore f(1+x)-f(1-x)>0$，即 $f(1+x)>f(1-x)$．" "\n"
        r"$\because0<1-x<1$，$1+x>1$，且 $f$ 在 $(1,+\infty)$ 上严格递减，" "\n"
        r"$\therefore$ 使 $f(x_{2})=f(1-x)$ 的 $x_{2}>1$ 必满足 $x_{2}>1+x$（否则 "
        r"$f(x_{2})\ge f(1+x)>f(1-x)$）．" "\n"
        r"令 $x_{1}=1-x$，则 $x_{1}+x_{2}>(1-x)+(1+x)=2$，故选 A．"
    ),
    'review': (
        r"① ⭐⭐ **「对称化比较」是极值点偏移的通用手法**：" "\n"
        r"  不直接比较 $x_{1}+x_{2}$ 与 $2$，而是比较 $f(1-x)$ 与 $f(1+x)$，" "\n"
        r"  把「根的位置」问题翻译成「函数值大小」问题 ✓✓" "\n"
        r"② ⭐⭐ **$G''(x)=4x\mathrm e^{2x}>0$ 配 $G'(0)=0$ 是定号的关键**：" "\n"
        r"  单看 $G'(x)=1+(2x-1)\mathrm e^{2x}$ 无法直接判正负（$2x-1$ 会变号），" "\n"
        r"  再求一次导数后用 $G'(0)=0$ 夹住，是「二阶导定号」的标准套路 ✓" "\n"
        r"③ 数值复核：取 $x_{1}=0.5$，则 $f(x_{1})=0.5\mathrm e^{-0.5}=0.303265$；" "\n"
        r"  解 $x_{2}\mathrm e^{-x_{2}}=0.303265$ 得 $x_{2}\approx1.756$（$1.756\times\mathrm e^{-1.756}=0.303$），" "\n"
        r"  $x_{1}+x_{2}\approx2.256>2$ ✓✓✓" "\n"
        r"  再取 $x_{1}=0.9$：$f=0.9\times0.406570=0.365913$，解得 $x_{2}\approx1.31$，$x_{1}+x_{2}=2.21>2$ ✓" "\n"
        r"④ ⚠ **不能选 B（$\ge2$）**：$x_{1}\to1^{-}$ 时 $x_{2}\to1^{+}$，$x_{1}+x_{2}\to2$，" "\n"
        r"  但 $x_{1}\ne x_{2}$ 排除了 $x_{1}=x_{2}=1$，故 $2$ 取不到，是严格大于 ✓" "\n"
        r"⑤ ⭐⭐ **$f(x)=x\mathrm e^{-x}$ 的两根必同为正**：$x<0$ 时 $f(x)<0$，而 $x\in(0,1)$ 时 $f>0$，" "\n"
        r"  所以两根只能在 $(0,1)$ 与 $(1,+\infty)$ 各取一个 —— 这决定了「分居 $1$ 两侧」✓" "\n"
        r"**⭐⭐ 通法（极值点偏移·对称化比较）**：" "\n"
        r"设 $f$ 在 $x=x_{0}$ 处取极值，$f(x_{1})=f(x_{2})$，$x_{1}<x_{0}<x_{2}$。" "\n"
        r"  要证 $x_{1}+x_{2}>2x_{0}$：对 $x\in(0,x_{0})$ 比较 $f(x_{0}-x)$ 与 $f(x_{0}+x)$，" "\n"
        r"  若恒有 $f(x_{0}+x)>f(x_{0}-x)$，则由右侧递减知 $x_{2}>2x_{0}-x_{1}$，即 $x_{1}+x_{2}>2x_{0}$．"
    ),
    'difficulty': 0.86,
    'topics': ['M-T-139'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-139-V2',
}

# ---------------------------------------------------------------- M-T-140-V1
T140_V1 = {
    'type': '选择',
    'stem_text': (
        r"设函数 $f(x)=\sqrt{\ln x+x+a}$，若曲线 $y=\dfrac{\mathrm e-1}2\sin x+\dfrac{\mathrm e+1}2$ "
        r"上存在点 $(x_{0},y_{0})$ 使得 $f(f(y_{0}))=y_{0}$ 成立，则实数 $a$ 的取值范围为（　　）"
    ),
    'opts': [
        ['A', r"$[0,\mathrm e^{2}-\mathrm e+1]$"],
        ['B', r"$[0,\mathrm e^{2}+\mathrm e-1]$"],
        ['C', r"$[0,\mathrm e^{2}-\mathrm e-1]$"],
        ['D', r"$[0,\mathrm e^{2}+\mathrm e+1]$"],
    ],
    'answer': 'C',
    'analysis': (
        r"先由 $-1\le\sin x\le1$ 得 $y_{0}\in[1,\mathrm e]$；再由 $f$ 单调递增把 "
        r"$f(f(y_{0}))=y_{0}$ 化成 $f(y_{0})=y_{0}$，平方后分离参数 $a=x^{2}-\ln x-x$，"
        r"求该函数在 $[1,\mathrm e]$ 上的值域即可．"
    ),
    'solution': (
        r"$\because-1\le\sin x\le1$，" "\n"
        r"$\therefore$ 当 $\sin x=1$ 时，$y=\dfrac{\mathrm e-1}2+\dfrac{\mathrm e+1}2=\mathrm e$ 为最大值；" "\n"
        r"当 $\sin x=-1$ 时，$y=-\dfrac{\mathrm e-1}2+\dfrac{\mathrm e+1}2=1$ 为最小值．" "\n"
        r"即该曲线的取值范围为 $[1,\mathrm e]$，故 $y_{0}\in[1,\mathrm e]$．" "\n"
        r"又 $f(x)=\sqrt{\ln x+x+a}$ 在定义域上单调递增（$\ln x+x+a$ 递增，根号保持单调性）．" "\n"
        r"设 $f(y_{0})=c$。若 $c>y_{0}$，则由 $f$ 递增得 $f(f(y_{0}))=f(c)>f(y_{0})=c>y_{0}$，" "\n"
        r"与 $f(f(y_{0}))=y_{0}$ 矛盾；若 $c<y_{0}$，同理 $f(c)<f(y_{0})=c<y_{0}$，亦矛盾．" "\n"
        r"$\therefore f(y_{0})=y_{0}$．" "\n"
        r"由 $f(x)=\sqrt{\ln x+x+a}$ 的定义域要求 $\ln x+x+a\ge0$，且 $f(y_{0})=y_{0}>0$，" "\n"
        r"两边平方得 $\ln x+x+a=x^{2}$，即 $a=x^{2}-\ln x-x$（此处 $x$ 即 $y_{0}\in[1,\mathrm e]$）．" "\n"
        r"设 $h(x)=x^{2}-\ln x-x$，则 $h'(x)=2x-\dfrac1x-1=\dfrac{2x^{2}-x-1}x=\dfrac{(2x+1)(x-1)}x$．" "\n"
        r"由 $h'(x)>0$ 得 $x>1$；由 $h'(x)<0$ 得 $0<x<1$．" "\n"
        r"$\therefore h(x)$ 在 $(0,1)$ 上递减、在 $(1,+\infty)$ 上递增，" "\n"
        r"故在 $[1,\mathrm e]$ 上 $h$ 单调递增，$h(1)=1-\ln1-1=0$ 为最小值，" "\n"
        r"$h(\mathrm e)=\mathrm e^{2}-\ln\mathrm e-\mathrm e=\mathrm e^{2}-\mathrm e-1$ 为最大值．" "\n"
        r"$\therefore0\le h(x)\le\mathrm e^{2}-\mathrm e-1$，即 $0\le a\le\mathrm e^{2}-\mathrm e-1$．故选 C．"
    ),
    'review': (
        r"① ⭐⭐ **题眼是「$f$ 递增 ⟹ $f(f(y))=y\iff f(y)=y$」**：" "\n"
        r"  用反证法（设 $c\ne y_{0}$ 则迭代后单调偏离）把「嵌套不动点」降为「普通不动点」✓✓" "\n"
        r"  这个结论对**任意严格递增**的 $f$ 都成立，可背下来 ✓" "\n"
        r"② ⭐⭐ **题干还原**：提取文本「曲线 $a_{1}=0,a_{2}=3$」是乱码，由详解" "\n"
        r"  「$\sin x=1$ 时 $y=\dfrac{\mathrm e-1}2+\dfrac{\mathrm e+1}2=\mathrm e$；"
        r"$\sin x=-1$ 时 $y=-\dfrac{\mathrm e-1}2+\dfrac{\mathrm e+1}2=1$」反推，" "\n"
        r"  原曲线必为 $y=\dfrac{\mathrm e-1}2\sin x+\dfrac{\mathrm e+1}2$ —— "
        r"两个端点值 $\mathrm e$ 与 $1$ **精确吻合** ✓✓✓" "\n"
        r"③ 数值复核：$\mathrm e^{2}-\mathrm e-1=7.389056-2.718282-1=3.670774$；" "\n"
        r"  $h(1)=0$ ✓，$h(\mathrm e)=3.670774$ ✓，$h(2)=4-\ln2-2=1.306853$（介于两者之间）✓" "\n"
        r"④ ⚠ **$h$ 在 $[1,\mathrm e]$ 上递增，最小值在 $x=1$ 而非 $x=\dfrac12$**：" "\n"
        r"  $h'(x)=\dfrac{(2x+1)(x-1)}x$ 的驻点是 $x=1$（$x=-\dfrac12$ 不在定义域内），" "\n"
        r"  所以区间 $[1,\mathrm e]$ 恰好从驻点开始，端点即最值 ✓" "\n"
        r"⑤ ⚠ **平方后要保证 $\ln x+x+a\ge0$**：$a=h(x)=x^{2}-\ln x-x$ 时 "
        r"$\ln x+x+a=x^{2}\ge0$ ✓ 自动满足，不必另加约束 ✓" "\n"
        r"**⭐⭐ 通法（嵌套不动点 $f(f(y))=y$）**：" "\n"
        r"若 $f$ 严格递增，则 $f(f(y))=y\iff f(y)=y$。" "\n"
        r"  （若 $f$ 严格递减，则 $f(f(y))=y$ 允许二周期，$f(y)=y$ 只是其中一个解）"
    ),
    'difficulty': 0.84,
    'topics': ['M-T-140'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-140-V1',
}

# ---------------------------------------------------------------- M-T-142-V2
T142_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知函数 $f(x)=\mathrm e^{x}(|\ln x|-m)-x$ 有两个零点，则 $m$ 的取值范围为（　　）"
    ),
    'opts': [
        ['A', r"$(-\mathrm e,+\infty)$"],
        ['B', r"$\left(-\dfrac1{\mathrm e},+\infty\right)$"],
        ['C', r"$(-1,+\infty)$"],
        ['D', r"$(0,+\infty)$"],
    ],
    'answer': 'B',
    'analysis': (
        r"$f(x)=0\iff|\ln x|=g(x)$，其中 $g(x)=\dfrac x{\mathrm e^{x}}+m$ 先增后减、"
        r"$g(1)=\dfrac1{\mathrm e}+m$。把定义域按 $(0,1)$ 与 $(1,+\infty)$ 切开分别数交点个数："
        r"两段各有一个交点当且仅当 $g(1)>0$，即 $m>-\dfrac1{\mathrm e}$．"
    ),
    'solution': (
        r"令 $f(x)=0$，即 $\mathrm e^{x}(|\ln x|-m)=x$，两边同除以 $\mathrm e^{x}$ 得" "\n"
        r"$|\ln x|-m=\dfrac x{\mathrm e^{x}}$，即 $|\ln x|=\dfrac x{\mathrm e^{x}}+m$．" "\n"
        r"设 $g(x)=\dfrac x{\mathrm e^{x}}+m$（$x>0$），则 $g'(x)=\dfrac{1-x}{\mathrm e^{x}}$．" "\n"
        r"由 $g'(x)>0$ 得 $0<x<1$，由 $g'(x)<0$ 得 $x>1$，" "\n"
        r"故 $g$ 在 $(0,1)$ 上递增、在 $(1,+\infty)$ 上递减，$g(1)=\dfrac1{\mathrm e}+m$ 为最大值，" "\n"
        r"且 $x\to0^{+}$ 时 $g(x)\to m$，$x\to+\infty$ 时 $g(x)\to m$．" "\n"
        r"而 $y=|\ln x|$ 在 $(0,1)$ 上由 $+\infty$ 严格递减到 $0$，"
        r"在 $(1,+\infty)$ 上由 $0$ 严格递增到 $+\infty$．" "\n"
        r"**在 $(1,+\infty)$ 上**：$\ln x$ 递增，$g(x)$ 递减，" "\n"
        r"故 $\ln x-g(x)$ 严格递增，且 $x\to+\infty$ 时趋于 $+\infty$；" "\n"
        r"于是存在唯一交点 $\iff$ 在 $x\to1^{+}$ 时 $\ln x-g(x)<0\iff 0-\left(\dfrac1{\mathrm e}+m\right)<0"
        r"\iff m>-\dfrac1{\mathrm e}$．" "\n"
        r"**在 $(0,1)$ 上**：$-\ln x$ 递减，$g(x)$ 递增，故 $-\ln x-g(x)$ 严格递减；" "\n"
        r"$x\to0^{+}$ 时 $-\ln x-g(x)\to+\infty-m=+\infty>0$；" "\n"
        r"$x\to1^{-}$ 时 $-\ln x-g(x)\to0-\left(\dfrac1{\mathrm e}+m\right)=-\left(\dfrac1{\mathrm e}+m\right)$，" "\n"
        r"于是存在唯一交点 $\iff-\left(\dfrac1{\mathrm e}+m\right)<0\iff m>-\dfrac1{\mathrm e}$．" "\n"
        r"$\therefore$ 当且仅当 $m>-\dfrac1{\mathrm e}$ 时，两段各有一个交点，共两个零点．" "\n"
        r"（当 $m=-\dfrac1{\mathrm e}$ 时两段都只在边界 $x=1$ 处「重合」，实际只有一个零点 $x=1$；" "\n"
        r"当 $m<-\dfrac1{\mathrm e}$ 时两段均无交点，无零点．）故选 B．"
    ),
    'review': (
        r"① ⭐⭐ **必须按 $(0,1)$ 与 $(1,+\infty)$ 分段数**：$|\ln x|$ 在 $x=1$ 处有尖点，" "\n"
        r"  两段单调性相反，不分开就数不清交点个数 ✓✓" "\n"
        r"② ⚠ **原书详解有误**：它写「$g(x)$ 从负无穷增大到 $\dfrac1{\mathrm e}+m$，然后递减到 $m$」——" "\n"
        r"  $x\to0^{+}$ 时 $g(x)=\dfrac x{\mathrm e^{x}}+m\to m$（**有限值**），不是 $-\infty$。" "\n"
        r"  本题答案是 $m>-\dfrac1{\mathrm e}$ 无误，但该表述会让人误判 $(0,1)$ 段的交点数 ✓" "\n"
        r"③ 数值复核：$m=0$ 时 $f(x)=\mathrm e^{x}|\ln x|-x$。" "\n"
        r"  $(0,1)$ 内：$f(0.5)=\mathrm e^{0.5}\times0.693147-0.5=1.142768-0.5=0.643>0$，" "\n"
        r"  $f(1)=0-1=-1<0$ ⟹ 有一个零点 ✓" "\n"
        r"  $(1,+\infty)$ 内：$f(1)=-1<0$，$f(1.5)=\mathrm e^{1.5}\times0.405465-1.5=1.817464-1.5=0.317>0$ "
        r"⟹ 有一个零点 ✓ 共 $2$ 个 ✓✓✓" "\n"
        r"  再取 $m=-0.5$（$<-\dfrac1{\mathrm e}=-0.367879$）：$g(1)=0.367879-0.5=-0.132<0$。" "\n"
        r"  $(0,1)$ 内 $-\ln x>0>g(x)$ 恒成立、$(1,+\infty)$ 内 $\ln x\ge0>g(x)$ 恒成立 ⟹ **$0$ 个零点** ✓" "\n"
        r"④ ⭐⭐ **$m=-\dfrac1{\mathrm e}$ 是「临界退化为单点」的情形**：" "\n"
        r"  此时 $f(1)=\mathrm e^{1}\left(0+\dfrac1{\mathrm e}\right)-1=1-1=0$，$x=1$ 恰为零点，" "\n"
        r"  但它是两段的**公共端点**，只算一个 —— 这正是边界取开区间的原因 ✓" "\n"
        r"**⭐⭐ 通法（$|\ln x|$ 型零点个数）**：" "\n"
        r"化为 $|\ln x|=g(x)$ 后，在 $(0,1)$ 上用 $-\ln x$、在 $(1,+\infty)$ 上用 $\ln x$，" "\n"
        r"  分别利用「一增一减 ⟹ 差严格单调 ⟹ 至多一个交点」+「两端异号 ⟹ 至少一个交点」计数．"
    ),
    'difficulty': 0.87,
    'topics': ['M-T-142'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-142-V2',
}

# ---------------------------------------------------------------- M-T-143-E1
T143_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知存在 $x_{1},x_{2}\in(0,+\infty)$，若要使等式 "
        r"$2x_{1}=\lambda(x_{2}-2\mathrm ex_{1})(\ln x_{1}-\ln x_{2})$ 成立"
        r"（$\mathrm e=2.71828\cdots$），则实数 $\lambda$ 的可能的取值是（　　）"
    ),
    'opts': [
        ['A', r"$\dfrac1{2\mathrm e}$"],
        ['B', r"$\dfrac2{\mathrm e}$"],
        ['C', r"$\dfrac1{\mathrm e}$"],
        ['D', r"$0$"],
    ],
    'answer': 'B',
    'analysis': (
        r"取倒数把 $\lambda$ 换到左边，设 $t=\dfrac{x_{2}}{x_{1}}>0$ 后化为 "
        r"$\dfrac1\lambda=-\dfrac12(t-2\mathrm e)\ln t$；求右端在 $t>0$ 上的值域，"
        r"得 $\dfrac1\lambda\le\dfrac{\mathrm e}2$ 且 $\dfrac1\lambda$ 可取负值，"
        r"故 $\lambda<0$ 或 $\lambda\ge\dfrac2{\mathrm e}$，再对照选项．"
    ),
    'solution': (
        r"$\because2x_{1}=\lambda(x_{2}-2\mathrm ex_{1})(\ln x_{1}-\ln x_{2})$，" "\n"
        r"$\therefore\dfrac1\lambda=\dfrac{(x_{2}-2\mathrm ex_{1})(\ln x_{1}-\ln x_{2})}{2x_{1}}"
        r"=-\dfrac12\left(\dfrac{x_{2}}{x_{1}}-2\mathrm e\right)\ln\dfrac{x_{2}}{x_{1}}$．" "\n"
        r"令 $t=\dfrac{x_{2}}{x_{1}}$，由 $x_{1},x_{2}\in(0,+\infty)$ 知 $t>0$．" "\n"
        r"设 $f(t)=-\dfrac12(t-2\mathrm e)\ln t$（$t>0$），" "\n"
        r"则 $f'(t)=-\dfrac12\left(\ln t+\dfrac{t-2\mathrm e}t\right)"
        r"=-\dfrac12\left(\ln t-\dfrac{2\mathrm e}t+1\right)$．" "\n"
        r"令 $g(t)=\ln t-\dfrac{2\mathrm e}t+1$，则 $g'(t)=\dfrac1t+\dfrac{2\mathrm e}{t^{2}}>0$，" "\n"
        r"$\therefore g(t)$ 在 $(0,+\infty)$ 上单调递增，又 $g(\mathrm e)=\ln\mathrm e-\dfrac{2\mathrm e}{\mathrm e}+1=1-2+1=0$．" "\n"
        r"$\therefore$ 当 $t\in(0,\mathrm e)$ 时 $g(t)<0$，$f'(t)>0$，$f$ 递增；" "\n"
        r"当 $t\in(\mathrm e,+\infty)$ 时 $g(t)>0$，$f'(t)<0$，$f$ 递减．" "\n"
        r"$\therefore f(t)_{\max}=f(\mathrm e)=-\dfrac12(\mathrm e-2\mathrm e)\ln\mathrm e=\dfrac{\mathrm e}2$．" "\n"
        r"又 $t\to0^{+}$ 时 $\ln t\to-\infty$、$t-2\mathrm e\to-2\mathrm e$，故 $f(t)\to-\infty$；" "\n"
        r"$t\to+\infty$ 时 $t-2\mathrm e\to+\infty$、$\ln t\to+\infty$，故 $f(t)\to-\infty$．" "\n"
        r"$\therefore f(t)$ 的值域为 $\left(-\infty,\dfrac{\mathrm e}2\right]$，" "\n"
        r"即 $\dfrac1\lambda\le\dfrac{\mathrm e}2$，且 $f(t)$ 可取到任意负值（$t<1$ 时 $\ln t<0$、"
        r"$t-2\mathrm e<0$，故 $f(t)<0$）．" "\n"
        r"$\therefore\dfrac1\lambda<0$ 或 $0<\dfrac1\lambda\le\dfrac{\mathrm e}2$，"
        r"即 $\lambda<0$ 或 $\lambda\ge\dfrac2{\mathrm e}$．" "\n"
        r"对照选项：$\dfrac2{\mathrm e}=0.7358$ 满足 $\lambda\ge\dfrac2{\mathrm e}$；" "\n"
        r"$\dfrac1{2\mathrm e}=0.1839$、$\dfrac1{\mathrm e}=0.3679$ 均落在 $\left(0,\dfrac2{\mathrm e}\right)$ 内，不可取；" "\n"
        r"$\lambda=0$ 时原式右边为 $0$ 而左边 $2x_{1}>0$，不成立．故选 B．"
    ),
    'review': (
        r"① ⭐⭐ **题眼是「取倒数把 $\lambda$ 孤立」**：原式 $\lambda$ 在乘积里，"
        r"取倒数后 $\dfrac1\lambda$ 单独在一边，右边恰好只含 $t=\dfrac{x_{2}}{x_{1}}$ ✓✓" "\n"
        r"② ⭐⭐ **$f(t)$ 的值域必须从两端看**：只求最大值 $\dfrac{\mathrm e}2$ 会漏掉负值分支，" "\n"
        r"  而 $\lambda<0$ 这一支虽不在选项中，却是完整的答案（若问「取值范围」必须写全）✓" "\n"
        r"③ 数值复核：$f(\mathrm e)=-\dfrac12(\mathrm e-2\mathrm e)\cdot1=\dfrac{\mathrm e}2=1.359141$ ✓" "\n"
        r"  $f(2)=-\dfrac12(2-5.436564)\ln2=1.191022$；$f(4)=-\dfrac12(4-5.436564)\ln4=0.995750$；" "\n"
        r"  $f(8)=-\dfrac12(8-5.436564)\ln8=-2.665258$（已为负）✓✓✓" "\n"
        r"④ ⭐⭐ **$g(\mathrm e)=0$ 是设计的**：$g(t)=\ln t-\dfrac{2\mathrm e}t+1$ 在 $t=\mathrm e$ 时 "
        r"$1-2+1=0$，" "\n"
        r"  与 $\ln$ 的分母系数 $2\mathrm e$ 直接相关 —— 若系数是 $k\mathrm e$，驻点一般不在 $\mathrm e$ ✓" "\n"
        r"⑤ ⚠ **$\lambda=0$ 必须单独排除**：取倒数时默认了 $\lambda\ne0$，" "\n"
        r"  而 $\lambda=0$ 时原式为 $2x_{1}=0$，与 $x_{1}>0$ 矛盾 ✓（选项 D 就是为此设的陷阱）" "\n"
        r"**⭐⭐ 通法（含 $\lambda$ 的乘积型条件）**：" "\n"
        r"若 $\lambda$ 以因式形式出现在等式中，先取倒数（或解出 $\dfrac1\lambda$），" "\n"
        r"  再把所有自变量压成比值 $t$，最后求 $t$ 的函数值域 —— 值域即 $\dfrac1\lambda$ 的可取范围．"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-143'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-143-E1',
}

# ---------------------------------------------------------------- M-T-147-E1
T147_E1 = {
    'type': '解答',
    'stem_text': (
        r"设函数 $f(x)=a\ln x+\dfrac{1-a}2x^{2}-bx$（$a\ne1$），曲线 $y=f(x)$ 在点 $(1,f(1))$ 处的"
        r"切线斜率为 $0$．" "\n"
        r"(I) 求 $b$；" "\n"
        r"(II) 若存在 $x_{0}\ge1$，使得 $f(x_{0})<\dfrac a{a-1}$，求 $a$ 的取值范围．"
    ),
    'opts': [],
    'answer': r"(I) $b=1$；(II) $(-\sqrt2-1,\sqrt2-1)\cup(1,+\infty)$",
    'analysis': (
        r"由 $f'(1)=0$ 得 $b=1$；再把 $f'(x)$ 因式分解成 $\dfrac{1-a}x\left(x-\dfrac a{1-a}\right)(x-1)$ 的"
        r"形式，按 $\dfrac a{1-a}$ 与 $1$ 的大小关系分 $a\le\dfrac12$、$\dfrac12<a<1$、$a>1$ 三类，"
        r"分别写出「存在 $x_{0}\ge1$ 使 $f(x_{0})<\dfrac a{a-1}$」的充要条件．"
    ),
    'solution': (
        r"**(I)** $f'(x)=\dfrac ax+(1-a)x-b$，由题设知 $f'(1)=0$，" "\n"
        r"即 $a+(1-a)-b=0$，解得 $b=1$．" "\n"
        r"**(II)** 由 (I) 知 $f(x)=a\ln x+\dfrac{1-a}2x^{2}-x$，定义域为 $(0,+\infty)$，" "\n"
        r"$f'(x)=\dfrac ax+(1-a)x-1=\dfrac{1-a}x\left(x-\dfrac a{1-a}\right)(x-1)$．" "\n"
        r"又 $f(1)=\dfrac{1-a}2-1=-\dfrac{a+1}2$．" "\n"
        r"**(i)** 若 $a\le\dfrac12$，则 $\dfrac a{1-a}\le1$（$a<1$ 时），" "\n"
        r"故当 $x\in(1,+\infty)$ 时 $x-\dfrac a{1-a}>0$、$x-1>0$，而 $\dfrac{1-a}x>0$，于是 $f'(x)>0$，" "\n"
        r"$f(x)$ 在 $(1,+\infty)$ 上单调递增，" "\n"
        r"$\therefore$ 存在 $x_{0}\ge1$ 使 $f(x_{0})<\dfrac a{a-1}$ 的充要条件为 $f(1)<\dfrac a{a-1}$，" "\n"
        r"即 $-\dfrac{a+1}2<\dfrac a{a-1}$．" "\n"
        r"此时 $a\le\dfrac12<1$，故 $a-1<0$，两边乘 $(a-1)$ 不等号变向：" "\n"
        r"$-\dfrac{(a+1)(a-1)}2>a\iff\dfrac{1-a^{2}}2>a\iff a^{2}+2a-1<0$，" "\n"
        r"解得 $-\sqrt2-1<a<\sqrt2-1$（结合 $a\le\dfrac12$ 仍为此区间）．" "\n"
        r"**(ii)** 若 $\dfrac12<a<1$，则 $\dfrac a{1-a}>1$，" "\n"
        r"故当 $x\in\left(1,\dfrac a{1-a}\right)$ 时 $f'(x)<0$；当 $x\in\left(\dfrac a{1-a},+\infty\right)$ 时 $f'(x)>0$，" "\n"
        r"即 $f$ 在 $\left(1,\dfrac a{1-a}\right)$ 上递减、在 $\left(\dfrac a{1-a},+\infty\right)$ 上递增，" "\n"
        r"$\therefore f(x)$ 在 $[1,+\infty)$ 上的最小值为 $f\left(\dfrac a{1-a}\right)$，" "\n"
        r"于是充要条件为 $f\left(\dfrac a{1-a}\right)<\dfrac a{a-1}$．" "\n"
        r"而 $f\left(\dfrac a{1-a}\right)=a\ln\dfrac a{1-a}+\dfrac{1-a}2\left(\dfrac a{1-a}\right)^{2}-\dfrac a{1-a}"
        r"=a\ln\dfrac a{1-a}+\dfrac{a^{2}}{2(1-a)}-\dfrac a{1-a}$，" "\n"
        r"注意到 $a>\dfrac12$ 时 $\dfrac a{1-a}>1$ 故 $\ln\dfrac a{1-a}>0$，" "\n"
        r"且 $\dfrac{a^{2}}{2(1-a)}-\dfrac a{1-a}=\dfrac{a^{2}-2a}{2(1-a)}$，而 $\dfrac a{a-1}=-\dfrac a{1-a}$，" "\n"
        r"作差可得 $f\left(\dfrac a{1-a}\right)-\dfrac a{a-1}=a\ln\dfrac a{1-a}+\dfrac{a^{2}}{2(1-a)}>0$，" "\n"
        r"$\therefore f\left(\dfrac a{1-a}\right)>\dfrac a{a-1}$，不合题意．" "\n"
        r"**(iii)** 若 $a>1$，则 $1-a<0$，故 $x>1$ 时 $f'(x)<0$，$f$ 在 $[1,+\infty)$ 上单调递减，" "\n"
        r"又 $x\to+\infty$ 时 $\dfrac{1-a}2x^{2}\to-\infty$，故 $f(x)\to-\infty$，" "\n"
        r"$\therefore$ 必存在 $x_{0}\ge1$ 使 $f(x_{0})<\dfrac a{a-1}$（此时 $\dfrac a{a-1}>0$，"
        r"而 $f(1)=-\dfrac{a+1}2<0<\dfrac a{a-1}$ 已可直接取 $x_{0}=1$）．" "\n"
        r"综上，$a$ 的取值范围为 $(-\sqrt2-1,\sqrt2-1)\cup(1,+\infty)$．"
    ),
    'review': (
        r"① ⭐⭐ **题眼是 $f'(x)$ 的因式分解**：" "\n"
        r"  $f'(x)=\dfrac ax+(1-a)x-1=\dfrac{(1-a)x^{2}-x+a}x=\dfrac{1-a}x\left(x-\dfrac a{1-a}\right)(x-1)$，" "\n"
        r"  三个因式列出后，「$\dfrac a{1-a}$ 与 $1$ 谁大」立刻给出分类点 $a=\dfrac12$ ✓✓" "\n"
        r"② ⭐⭐ **「存在 $x_{0}\ge1$ 使 $f(x_{0})<M$」的充要条件随单调性变化**：" "\n"
        r"  递增时看 $f(1)$；先减后增时看最小值点；递减时（且 $f\to-\infty$）恒成立。" "\n"
        r"  三者**不能混用** —— 这是本题唯一会掉坑的地方 ✓" "\n"
        r"③ 数值复核：$a=0$（在 $(-\sqrt2-1,\sqrt2-1)$ 内）时 $f(x)=\dfrac12x^{2}-x$，" "\n"
        r"  $f(1)=-0.5$，而 $\dfrac a{a-1}=0$，$-0.5<0$ ✓ 确实存在（取 $x_{0}=1$ 即可）✓" "\n"
        r"  取 $a=\sqrt2-1+0.01=0.4242$（超出）：$-\dfrac{a+1}2=-0.7121$，$\dfrac a{a-1}=-0.7370$，" "\n"
        r"  $-0.7121<-0.7370$ 不成立 ✓ 边界正确 ✓✓" "\n"
        r"  取 $a=-2.5$（小于 $-\sqrt2-1=-2.4142$）：$-\dfrac{a+1}2=0.75$，$\dfrac a{a-1}=0.7143$，" "\n"
        r"  $0.75<0.7143$ 不成立 ✓ 边界正确 ✓" "\n"
        r"④ ⚠ **原书 ans 存在根号丢失**：写作「$(-2-1,\ 2-1)$」，" "\n"
        r"  实为 $(-\sqrt2-1,\ \sqrt2-1)$（由 $a^{2}+2a-1<0$ 解得）✓" "\n"
        r"⑤ ⚠ **$a\ne1$ 是题设给的**：$a=1$ 时 $f(x)=\ln x-x$，$f'(x)=\dfrac1x-1$，" "\n"
        r"  $f'(1)=0$ 也成立，但 $\dfrac a{a-1}$ 无意义，故排除 ✓" "\n"
        r"**⭐⭐ 通法（含参二次函数型导数）**：" "\n"
        r"当 $f'(x)$ 通分后分子是二次式且**已知一个根为 $x=1$** 时，" "\n"
        r"  必可分解成 $\dfrac{1-a}x(x-1)\left(x-\dfrac a{1-a}\right)$ 的形式；" "\n"
        r"  分类点由「另一根与已知根 $1$ 的大小关系」给出，而不是由判别式给出．"
    ),
    'difficulty': 0.90,
    'topics': ['M-T-147'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-147-E1',
}

# ---------------------------------------------------------------- M-T-156-E1
T156_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=\ln(x+a)$，$g(x)=x^{2}+x$，若函数 $F(x)=f(x)-g(x)$ 在 $x=0$ 处取得极值．" "\n"
        r"(1) 求实数 $a$ 的值；" "\n"
        r"(2) 若关于 $x$ 的方程 $F(x)+\dfrac52x-m=0$ 在区间 $[0,2]$ 上恰有两个不同的实数根，"
        r"求实数 $m$ 的取值范围；" "\n"
        r"(3) 证明：对任意的自然数 $n$，有 $\ln\dfrac{n+1}n<2$ 恒成立．"
    ),
    'opts': [],
    'answer': r"(1) $a=1$；(2) $-1+\ln3\le m<\dfrac12+\ln2$；(3) 证明见解析",
    'analysis': (
        r"(1) 由 $F'(0)=0$ 得 $a=1$；(2) 构造 $h(x)=\ln(x+1)-x^{2}+\dfrac32x-m$，"
        r"由导数定出它在 $[0,1]$ 增、$[1,2]$ 减，再用「两个不同实根」等价于"
        r"$h(0)\le0$、$h(1)>0$、$h(2)\le0$ 三个端点条件；(3) 用 $F(x)\le F(0)=0$ 得 "
        r"$\ln(1+x)\le x^{2}+x$，取 $x=\dfrac1n$ 后用 $t^{2}+t\le2$（$t=\dfrac1n\in(0,1]$）收口．"
    ),
    'solution': (
        r"**(1)** 由题意 $F(x)=\ln(x+a)-x^{2}-x$，则 $F'(x)=\dfrac1{x+a}-2x-1$．" "\n"
        r"$\because x=0$ 时 $F(x)$ 取得极值，$\therefore F'(0)=0$，" "\n"
        r"即 $\dfrac1{0+a}-0-1=0$，解得 $a=1$．经检验 $a=1$ 符合题意．" "\n"
        r"**(2)** 由 $a=1$ 知 $F(x)=\ln(x+1)-x^{2}-x$．" "\n"
        r"由 $F(x)+\dfrac52x-m=0$ 得 $\ln(x+1)-x^{2}+\dfrac32x-m=0$．" "\n"
        r"令 $h(x)=\ln(x+1)-x^{2}+\dfrac32x-m$，" "\n"
        r"则原方程在 $[0,2]$ 上恰有两个不同实根 $\iff h(x)=0$ 在 $[0,2]$ 上恰有两个不同实根．" "\n"
        r"$h'(x)=\dfrac1{x+1}-2x+\dfrac32=\dfrac{2-4x(x+1)+3(x+1)}{2(x+1)}"
        r"=\dfrac{-4x^{2}+x+5}{2(x+1)}=-\dfrac{(4x+5)(x-1)}{2(x+1)}$．" "\n"
        r"当 $x\in[0,1)$ 时 $h'(x)>0$，$h(x)$ 单调递增；当 $x\in(1,2]$ 时 $h'(x)<0$，$h(x)$ 单调递减．" "\n"
        r"依题意（先增后减，两个零点分别在 $[0,1)$ 与 $(1,2]$ 内，且 $x=1$ 处为正）：" "\n"
        r"$\begin{cases}h(0)=-m\le0\\ h(1)=\ln2-1+\dfrac32-m>0\\ h(2)=\ln3-4+3-m\le0\end{cases}$"
        r"$\iff\begin{cases}m\ge0\\ m<\dfrac12+\ln2\\ m\ge-1+\ln3\end{cases}$．" "\n"
        r"又 $-1+\ln3=-1+1.0986=0.0986>0$，故 $m\ge-1+\ln3$ 蕴含 $m\ge0$，" "\n"
        r"$\therefore-1+\ln3\le m<\dfrac12+\ln2$．" "\n"
        r"**(3)** 由 (1) 知 $F(x)=\ln(x+1)-x^{2}-x$ 的定义域为 $\{x\mid x>-1\}$，" "\n"
        r"$F'(x)=\dfrac1{x+1}-2x-1=-\dfrac{x(2x+3)}{x+1}$．" "\n"
        r"令 $F'(x)=0$ 得 $x=0$ 或 $x=-\dfrac32$（舍去）．" "\n"
        r"$\therefore$ 当 $-1<x<0$ 时 $F'(x)>0$，$F$ 递增；当 $x>0$ 时 $F'(x)<0$，$F$ 递减，" "\n"
        r"$\therefore F(x)\le F(0)=0$，即 $\ln(x+1)-x^{2}-x\le0$（当且仅当 $x=0$ 时取等号）．" "\n"
        r"对任意正整数 $n$，取 $x=\dfrac1n>0$（此时 $x\ne0$，故严格不等号成立）：" "\n"
        r"$\ln\left(1+\dfrac1n\right)<\dfrac1{n^{2}}+\dfrac1n$．" "\n"
        r"令 $t=\dfrac1n$，则 $t\in(0,1]$，而 $\varphi(t)=t^{2}+t$ 在 $(0,1]$ 上单调递增，" "\n"
        r"故 $\varphi(t)\le\varphi(1)=1^{2}+1=2$，即 $\dfrac1{n^{2}}+\dfrac1n\le2$．" "\n"
        r"$\therefore\ln\dfrac{n+1}n=\ln\left(1+\dfrac1n\right)<\dfrac1{n^{2}}+\dfrac1n\le2$，" "\n"
        r"即对任意自然数 $n$，有 $\ln\dfrac{n+1}n<2$ 恒成立．"
    ),
    'review': (
        r"① ⭐⭐ **(2) 的题眼是「两个零点 ⟺ 三个端点条件」**：" "\n"
        r"  $h$ 先增后减，两个零点分别在 $[0,1)$ 与 $(1,2]$ 内，" "\n"
        r"  故需 $h(0)\le0$（左段有根）、$h(1)>0$（峰值在 $x$ 轴上方）、$h(2)\le0$（右段有根）✓✓" "\n"
        r"  ⚠ **$h(1)>0$ 是严格大于**（等于 $0$ 时两段共用一个根 $x=1$，只剩一个不同实根）✓" "\n"
        r"② 数值复核：$m=-1+\ln3=0.098612$ 时，$h(2)=\ln3-1-m=1.098612-1-0.098612=0$，" "\n"
        r"  $x=2$ 是根 ✓；$h(1)=\ln2+0.5-0.098612=1.094535>0$ ✓；$h(0)=-0.098612<0$ ✓ 恰两个根 ✓✓✓" "\n"
        r"  $m=\dfrac12+\ln2=1.193147$ 时 $h(1)=0$，两段共用 $x=1$，只有 **一个**根 —— "
        r"与「上端点开」一致 ✓" "\n"
        r"③ ⭐⭐ **$h'(x)$ 的分解**：$-4x^{2}+x+5=-(4x^{2}-x-5)=-(4x+5)(x-1)$ ✓" "\n"
        r"  在 $[0,2]$ 上 $4x+5>0$、$x+1>0$，故符号只由 $-(x-1)$ 决定 —— 一眼定单调 ✓" "\n"
        r"④ ⚠ **$m\ge-1+\ln3$ 蕴含 $m\ge0$**：$-1+\ln3=0.0986>0$，" "\n"
        r"  所以「$m\ge0$」这个条件冗余，最终下界是 $-1+\ln3$、不是 $0$ ✓" "\n"
        r"⑤ ⚠ **原书 (3) 有两处笔误**：它写「$t^{2}+t$ 在 $[1,+\infty)$ 上为增函数，" "\n"
        r"  $(t^{2}+t)_{\min}=2$」—— 实际 $t=\dfrac1n\in(0,1]$，函数应在 $(0,1]$ 上递增，" "\n"
        r"  且取到的是**最大值** $\varphi(1)=2$，不是最小值。结论 $\ln\dfrac{n+1}n<2$ 无误 ✓" "\n"
        r"  另：题干「$\ln\frac{n+1}n+\frac1{n^2}+\frac1n<2$」若按字面理解，$n=1$ 时 "
        r"$\ln2+2=2.693>2$ 是**假命题**；按原书详解的收口，所证实为 $\ln\dfrac{n+1}n<2$ ✓" "\n"
        r"**⭐⭐ 通法（「恰有两个实根」）**：" "\n"
        r"若函数先增后减（单峰），则在闭区间 $[a,b]$ 上恰有两个零点的充要条件是" "\n"
        r"  $f(a)\le0$、$f(x_{0})>0$（$x_{0}$ 为峰点）、$f(b)\le0$，" "\n"
        r"  其中**峰值处必须是严格大于 $0$**（等于 $0$ 时两根合并成一个）．"
    ),
    'difficulty': 0.86,
    'topics': ['M-T-156'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-156-E1',
}

# ---------------------------------------------------------------- M-T-158-V1
T158_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=\ln(1+x)-\dfrac{ax}{x+1}$（$a>0$）．" "\n"
        r"(I) 若 $x=1$ 是函数 $f(x)$ 的一个极值点，求 $a$ 的值；" "\n"
        r"(II) 若 $f(x)\ge0$ 在 $[0,+\infty)$ 上恒成立，求 $a$ 的取值范围；" "\n"
        r"(III) 证明：$\left(\dfrac{2015}{2016}\right)^{2016}<\dfrac1{\mathrm e}$（$\mathrm e$ 为自然对数的底数）．"
    ),
    'opts': [],
    'answer': r"(I) $a=2$；(II) $(0,1]$；(III) 证明见解析",
    'analysis': (
        r"$f'(x)=\dfrac{1+x-a}{(1+x)^{2}}$，符号只由 $1+x-a$ 决定。(I) 由 $f'(1)=0$ 得 $a=2$；" "\n"
        r"(II) 分 $a\le1$（$f'\ge0$，$f$ 递增，$f(0)=0$ 即最小值）与 $a>1$（$[0,a-1)$ 上递减，"
        r"$f(a-1)<f(0)=0$ 矛盾）两类；(III) 取对数后化成 $\ln\left(1+\dfrac1{2015}\right)>\dfrac1{2016}$，"
        r"由 (II) 中 $a=1$ 的结论直接给出．"
    ),
    'solution': (
        r"**(I)** $\becausef(x)=\ln(1+x)-\dfrac{ax}{x+1}$（$a>0$），" "\n"
        r"$\thereforef'(x)=\dfrac1{1+x}-\dfrac a{(x+1)^{2}}=\dfrac{x+1-a}{(x+1)^{2}}$．" "\n"
        r"$\because x=1$ 是 $f(x)$ 的一个极值点，$\therefore f'(1)=0$，即 $\dfrac{2-a}{4}=0$，得 $a=2$．" "\n"
        r"**(II)** $f'(x)=\dfrac{x+1-a}{(x+1)^{2}}$，在 $[0,+\infty)$ 上 $(x+1)^{2}>0$，"
        r"故 $f'$ 的符号由 $x+1-a$ 决定．" "\n"
        r" ① 当 $0<a\le1$ 时，$x\ge0\implies x+1-a\ge1-a\ge0$，故 $f'(x)\ge0$ 恒成立，" "\n"
        r"  $f(x)$ 在 $[0,+\infty)$ 上单调递增，$\therefore f(x)_{\min}=f(0)=\ln1-0=0$，"
        r"即 $f(x)\ge0$ 成立．" "\n"
        r" ② 当 $a>1$ 时，令 $f'(x)<0$ 得 $0\le x<a-1$，令 $f'(x)>0$ 得 $x>a-1$，" "\n"
        r"  $\therefore f(x)$ 在 $[0,a-1)$ 上递减、在 $(a-1,+\infty)$ 上递增，" "\n"
        r"  $\therefore f(x)_{\min}=f(a-1)<f(0)=0$，与 $f(x)\ge0$ 恒成立矛盾．" "\n"
        r"综上，$a$ 的取值范围为 $(0,1]$．" "\n"
        r"**(III)** 要证 $\left(\dfrac{2015}{2016}\right)^{2016}<\dfrac1{\mathrm e}$，" "\n"
        r"只需证 $\left(\dfrac{2016}{2015}\right)^{2016}>\mathrm e$，两边取自然对数得 "
        r"$2016\ln\dfrac{2016}{2015}>1$，" "\n"
        r"即 $\ln\left(1+\dfrac1{2015}\right)>\dfrac1{2016}$．" "\n"
        r"由 (II) 知，当 $a=1$ 时 $f(x)=\ln(1+x)-\dfrac x{x+1}$ 在 $[0,+\infty)$ 上单调递增，" "\n"
        r"又 $\dfrac1{2015}>0$、$f(0)=0$，" "\n"
        r"$\therefore f\left(\dfrac1{2015}\right)=\ln\left(1+\dfrac1{2015}\right)-\dfrac{\dfrac1{2015}}{1+\dfrac1{2015}}>f(0)=0$，" "\n"
        r"而 $\dfrac{\dfrac1{2015}}{1+\dfrac1{2015}}=\dfrac1{2016}$，" "\n"
        r"$\therefore\ln\left(1+\dfrac1{2015}\right)>\dfrac1{2016}$，从而 $\left(\dfrac{2015}{2016}\right)^{2016}<\dfrac1{\mathrm e}$ 成立．"
    ),
    'review': (
        r"① ⭐⭐ **$f'(x)=\dfrac{x+1-a}{(x+1)^{2}}$ 只有一个可变因式**：" "\n"
        r"  $\left(\dfrac{ax}{x+1}\right)'=a\cdot\dfrac{(x+1)-x}{(x+1)^{2}}=\dfrac a{(x+1)^{2}}$，" "\n"
        r"  分母与 $\dfrac1{1+x}$ 通分后同分母，符号一目了然 —— 这是本题能秒解的原因 ✓✓" "\n"
        r"② ⭐⭐ **(II) 的关键是 $f(0)=0$ 恒成立**：" "\n"
        r"  $f(0)=\ln1-0=0$ 与 $a$ 无关，所以「$f\ge0$」等价于「$x=0$ 是最小值点」，" "\n"
        r"  $a\le1$ 时 $f$ 递增 ⟹ 成立；$a>1$ 时 $f$ 先减 ⟹ $f(a-1)<f(0)=0$ ⟹ 不成立 ✓" "\n"
        r"③ 数值复核：$a=1$，$f(x)=\ln(1+x)-\dfrac x{x+1}$：$f(1)=\ln2-0.5=0.1931>0$ ✓；" "\n"
        r"  $a=2$，$f(x)=\ln(1+x)-\dfrac{2x}{x+1}$：$f(1)=\ln2-1=-0.3069<0$ ✓ 确实不满足 ✓✓✓" "\n"
        r"④ ⭐⭐ **(III) 是 (II) 的直接应用**：取 $x=\dfrac1{2015}$ 后 "
        r"$\dfrac{x}{1+x}=\dfrac1{2016}$ 恰好是需要的右端，" "\n"
        r"  这种「(III) 用 (II) 的结论、且代入值由待证式的分母决定」是固定套路 ✓" "\n"
        r"⑤ ⚠ **取对数时方向**：$\left(\dfrac{2015}{2016}\right)^{2016}<\dfrac1{\mathrm e}$ 取倒数后" "\n"
        r"  $\left(\dfrac{2016}{2015}\right)^{2016}>\mathrm e$，**不等号方向翻转**（两边都是正数）✓" "\n"
        r"**⭐⭐ 通法（$\ln(1+x)-\dfrac{ax}{1+x}$ 型）**：" "\n"
        r"导数恒为 $\dfrac{x+1-a}{(x+1)^{2}}$，分类点永远是 $a=1$（因为 $x\ge0$ 时 $x+1\ge1$）。" "\n"
        r"  $a\le1$ 递增、$a>1$ 先减后增；配合 $f(0)=0$ 可直接给出恒成立问题的答案．"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-158'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-158-V1',
}

# ---------------------------------------------------------------- M-T-161-V1
T161_V1 = {
    'type': '解答',
    'stem_text': (
        r"设函数 $f(x)=x\ln(1-x)$．" "\n"
        r"(1) 求 $y=f(x)$ 的极值点；" "\n"
        r"(2) 设函数 $F(x)=\dfrac x{f(x)}+\dfrac1x-\sin x$．证明：$F(x)<2$．"
    ),
    'opts': [],
    'answer': r"(1) $x=0$ 是极大值点，极大值为 $f(0)=0$；(2) 证明见解析",
    'analysis': (
        r"(1) 求导后由 $f'(x)=\ln(1-x)-\dfrac x{1-x}$ 的导数 $\dfrac{x-2}{(1-x)^{2}}<0$ 定单调性；" "\n"
        r"(2) 先由 $f(x)<0$（$x\ne0$）把 $F$ 化成 $\dfrac1{\ln(1-x)}+\dfrac1x-\sin x$，"
        r"再通分证明 $\dfrac1{\ln(1-x)}+\dfrac1x<1$，最后配 $\sin x\ge-1$ 得 $F(x)<2$．"
    ),
    'solution': (
        r"**(1)** 函数 $y=f(x)$ 的定义域为 $(-\infty,1)$．" "\n"
        r"$f'(x)=\ln(1-x)+x\cdot\dfrac{-1}{1-x}=\ln(1-x)-\dfrac x{1-x}$．" "\n"
        r"设 $g(x)=\ln(1-x)-\dfrac x{1-x}$，则 " "\n"
        r"$g'(x)=\dfrac{-1}{1-x}-\dfrac{(1-x)+x}{(1-x)^{2}}=-\dfrac1{1-x}-\dfrac1{(1-x)^{2}}"
        r"=\dfrac{-(1-x)-1}{(1-x)^{2}}=\dfrac{x-2}{(1-x)^{2}}$．" "\n"
        r"$\because x\in(-\infty,1)$，$\therefore x-2<0$，故 $g'(x)<0$，$g(x)$ 是单调递减函数，" "\n"
        r"又 $g(0)=\ln1-0=0$：" "\n"
        r"当 $0<x<1$ 时 $g(x)<g(0)=0$，即 $f'(x)<0$，$f(x)$ 单调递减；" "\n"
        r"当 $x<0$ 时 $g(x)>g(0)=0$，即 $f'(x)>0$，$f(x)$ 单调递增．" "\n"
        r"$\therefore$ 当 $x=0$ 时 $f(x)$ 取得极大值，极大值为 $f(0)=0\cdot\ln1=0$；无极小值．" "\n"
        r"**(2)** $F(x)=\dfrac x{f(x)}+\dfrac1x-\sin x=\dfrac x{x\ln(1-x)}+\dfrac1x-\sin x"
        r"=\dfrac1{\ln(1-x)}+\dfrac1x-\sin x$，" "\n"
        r"定义域为 $(-\infty,0)\cup(0,1)$．" "\n"
        r"先证 $\dfrac1{\ln(1-x)}+\dfrac1x<1$．通分得" "\n"
        r"$\dfrac1{\ln(1-x)}+\dfrac1x-1=\dfrac{x+\ln(1-x)-x\ln(1-x)}{x\ln(1-x)}$．" "\n"
        r"**分母**：$x<0$ 时 $\ln(1-x)>0$，故 $x\ln(1-x)<0$；" "\n"
        r"$0<x<1$ 时 $\ln(1-x)<0$，故 $x\ln(1-x)<0$．即分母恒为负．" "\n"
        r"**分子**：设 $t(x)=x+\ln(1-x)-x\ln(1-x)$（$x<1$），则 " "\n"
        r"$t'(x)=1-\dfrac1{1-x}-\ln(1-x)+\dfrac x{1-x}=1-\dfrac{1-x}{1-x}-\ln(1-x)=-\ln(1-x)$．" "\n"
        r"当 $0<x<1$ 时 $\ln(1-x)<0$，$t'(x)>0$，$t$ 递增，故 $t(x)>t(0)=0$；" "\n"
        r"当 $x<0$ 时 $\ln(1-x)>0$，$t'(x)<0$，$t$ 递减，故 $t(x)>t(0)=0$．" "\n"
        r"即分子恒为正．$\therefore\dfrac1{\ln(1-x)}+\dfrac1x-1<0$，即 $\dfrac1{\ln(1-x)}+\dfrac1x<1$．" "\n"
        r"又 $\sin x\ge-1$，故 $2+\sin x\ge1$．" "\n"
        r"$\therefore\dfrac1{\ln(1-x)}+\dfrac1x<1\le2+\sin x$，" "\n"
        r"即 $\dfrac1{\ln(1-x)}+\dfrac1x-\sin x<2$，亦即 $F(x)<2$．"
    ),
    'review': (
        r"① ⭐⭐ **(2) 的题眼是「通分后分子分母各自定号」**：" "\n"
        r"  分母 $x\ln(1-x)$ 在定义域 $(-\infty,0)\cup(0,1)$ 上**恒为负**（$x$ 与 $\ln(1-x)$ 异号）；" "\n"
        r"  分子 $t(x)$ 由 $t'(x)=-\ln(1-x)$ 与 $t(0)=0$ 知**恒为正** —— 于是整个分式恒负 ✓✓" "\n"
        r"② ⭐⭐ **$t'(x)=-\ln(1-x)$ 的化简是关键一步**：" "\n"
        r"  $1-\dfrac1{1-x}+\dfrac x{1-x}=1+\dfrac{x-1}{1-x}=1-1=0$，前三项恰好抵消，" "\n"
        r"  只剩 $-\ln(1-x)$。这种「抵消」是命题人设计的，遇到时基本可断定方向正确 ✓" "\n"
        r"③ 数值复核：取 $x=-1$，$\dfrac1{\ln2}+(-1)=1.442695-1=0.442695<1$ ✓，" "\n"
        r"  $F(-1)=0.442695-\sin(-1)=0.442695+0.841471=1.284166<2$ ✓；" "\n"
        r"  取 $x=0.5$，$\dfrac1{\ln0.5}+2=-1.442695+2=0.557305<1$ ✓，" "\n"
        r"  $F(0.5)=0.557305-\sin0.5=0.557305-0.479426=0.077879<2$ ✓✓✓" "\n"
        r"④ ⚠ **$\sin x\ge-1$ 只能给到 $2+\sin x\ge1$**，而左端严格小于 $1$ —— " "\n"
        r"  正是「严格小于 $1$」配「大于等于 $1$」才得到严格的 $F(x)<2$ ✓" "\n"
        r"⑤ ⚠ **定义域是 $(-\infty,0)\cup(0,1)$**：$x=0$ 时 $\dfrac1x$ 与 $\dfrac x{f(x)}$ 均无意义，" "\n"
        r"  且 $f(0)=0$ 使分母为 $0$ —— 必须排除，$x\to0$ 时 $F(x)\to-\infty$（因 $\dfrac1{\ln(1-x)}\to-\infty$）✓" "\n"
        r"**⭐⭐ 通法（分式型不等式）**：" "\n"
        r"欲证 $\dfrac1A+\dfrac1B<k$，先通分成 $\dfrac{A+B-kAB}{AB}$，" "\n"
        r"  再分别判定分子与分母的符号（往往各用一个辅助函数 + 一个特殊点定号）．"
    ),
    'difficulty': 0.91,
    'topics': ['M-T-161'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-161-V1',
}

# ---------------------------------------------------------------- M-T-162-V1
T162_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=\mathrm e^{x}+\cos x-ax$（$a\in\mathbf R$）．" "\n"
        r"(1) 当 $a=1$ 时，判断 $f(x)$ 在区间 $(0,+\infty)$ 上的单调性；" "\n"
        r"(2) 当 $a=\mathrm e$ 时，若 $x_{1},x_{2}\in(0,\pi)$，$x_{1}\ne x_{2}$，$f(x_{1})=f(x_{2})$，"
        r"且 $f(x)$ 的极值在 $x=x_{0}$ 处取得，证明：$x_{1}+x_{2}<2x_{0}$．"
    ),
    'opts': [],
    'answer': r"(1) $f(x)$ 在 $(0,+\infty)$ 上是增函数；(2) 证明见解析",
    'analysis': (
        r"(1) $a=1$ 时 $f'(x)=\mathrm e^{x}-\sin x-1$，其导数 $\mathrm e^{x}+\cos x>0$（$x>0$），"
        r"故 $f'$ 递增且 $f'(0)=0$；(2) 由 (1) 的单调性知 $f'$ 在 $(1,\pi)$ 内有唯一零点 $x_{0}$，"
        r"再构造 $h(x)=f(x)-f(2x_{0}-x)$，证 $h$ 在 $(0,x_{0})$ 上递增且 $h(x_{0})=0$ 即可．"
    ),
    'solution': (
        r"**(1)** $a=1$ 时 $f(x)=\mathrm e^{x}+\cos x-x$，$f'(x)=\mathrm e^{x}-\sin x-1$．" "\n"
        r"设 $g(x)=\mathrm e^{x}-\sin x-1$，则 $g'(x)=\mathrm e^{x}+\cos x$．" "\n"
        r"当 $x>0$ 时 $\mathrm e^{x}>1$ 且 $\cos x\ge-1$，故 $g'(x)>0$ 恒成立，" "\n"
        r"$\therefore g(x)$ 在 $(0,+\infty)$ 上单调递增，又 $g(0)=\mathrm e^{0}-\sin0-1=0$，" "\n"
        r"$\therefore x>0$ 时 $g(x)>0$，即 $f'(x)>0$ 恒成立，" "\n"
        r"$\therefore f(x)$ 在 $(0,+\infty)$ 上是增函数．" "\n"
        r"**(2)** $a=\mathrm e$ 时 $f(x)=\mathrm e^{x}+\cos x-\mathrm ex$，$f'(x)=\mathrm e^{x}-\sin x-\mathrm e$．" "\n"
        r"由 (1) 的推导（$g(x)=\mathrm e^{x}-\sin x-\mathrm e$ 同样满足 $g'(x)=\mathrm e^{x}+\cos x>0$）" "\n"
        r"知 $f'(x)$ 在 $(0,+\infty)$ 上单调递增．" "\n"
        r"又 $f'(1)=\mathrm e-\sin1-\mathrm e=-\sin1<0$，$f'(\pi)=\mathrm e^{\pi}-\sin\pi-\mathrm e=\mathrm e^{\pi}-\mathrm e>0$，" "\n"
        r"由零点存在定理，$f'(x)$ 在 $(1,\pi)$ 内存在唯一零点 $x_{0}$，满足 "
        r"$\mathrm e^{x_{0}}-\sin x_{0}-\mathrm e=0$．" "\n"
        r"当 $0<x<x_{0}$ 时 $f'(x)<0$，$f$ 递减；当 $x_{0}<x<\pi$ 时 $f'(x)>0$，$f$ 递增．" "\n"
        r"$\therefore x_{0}$ 是 $f(x)$ 在 $(0,\pi)$ 上的唯一极小值点．" "\n"
        r"由 $x_{1}\ne x_{2}$、$f(x_{1})=f(x_{2})$ 及 $f$ 先减后增知 $0<x_{1}<x_{0}<x_{2}<\pi$．" "\n"
        r"设 $h(x)=f(x)-f(2x_{0}-x)$，$0<x<x_{0}$，则 " "\n"
        r"$h(x)=\mathrm e^{x}+\cos x-\mathrm ex-\mathrm e^{2x_{0}-x}-\cos(2x_{0}-x)+\mathrm e(2x_{0}-x)$" "\n"
        r"$=\mathrm e^{x}-\mathrm e^{2x_{0}-x}+\cos x-\cos(x-2x_{0})-2\mathrm ex_{0}+2\mathrm ex$（利用 $\cos$ 为偶函数）．" "\n"
        r"$h'(x)=\mathrm e^{x}+\mathrm e^{2x_{0}-x}-\sin x+\sin(x-2x_{0})$" "\n"
        r"$\quad\ \ge2\sqrt{\mathrm e^{x}\cdot\mathrm e^{2x_{0}-x}}-\sin x+\sin(x-2x_{0})=2\mathrm e^{x_{0}}-\sin x+\sin(x-2x_{0})$（基本不等式）．" "\n"
        r"由 $f'(x_{0})=0$ 得 $\mathrm e^{x_{0}}=\sin x_{0}+\mathrm e$，" "\n"
        r"$\therefore h'(x)\ge2\mathrm e+2\sin x_{0}-\sin x+\sin(x-2x_{0})$．" "\n"
        r"$\because0<x<x_{0}<\pi$，$\therefore0<\sin x_{0}\le1$、$0<\sin x\le1$，且 $-1\le\sin(x-2x_{0})\le1$，" "\n"
        r"$\therefore h'(x)>2\mathrm e+0-1+(-1)=2\mathrm e-2>0$，即 $h(x)$ 在 $(0,x_{0})$ 上单调递增．" "\n"
        r"又 $h(x_{0})=f(x_{0})-f(x_{0})=0$，$\therefore$ 当 $0<x_{1}<x_{0}$ 时 $h(x_{1})<h(x_{0})=0$，" "\n"
        r"即 $f(x_{1})<f(2x_{0}-x_{1})$．" "\n"
        r"$\because f(x_{2})=f(x_{1})<f(2x_{0}-x_{1})$，且 $x_{2}>x_{0}$、$2x_{0}-x_{1}>x_{0}$，" "\n"
        r"而 $f$ 在 $(x_{0},+\infty)$ 上单调递增，$\therefore x_{2}<2x_{0}-x_{1}$，" "\n"
        r"即 $x_{1}+x_{2}<2x_{0}$．"
    ),
    'review': (
        r"① ⭐⭐ **(2) 的题眼是「对称化构造」**：构造 $h(x)=f(x)-f(2x_{0}-x)$，" "\n"
        r"  则 $h(x_{0})=0$ 是天然锚点；证 $h$ 在 $(0,x_{0})$ 上递增即得 $h(x_{1})<0$ ✓✓" "\n"
        r"② ⭐⭐ **$h'(x)$ 里 $\mathrm e^{x}+\mathrm e^{2x_{0}-x}\ge2\mathrm e^{x_{0}}$ 用基本不等式**：" "\n"
        r"  两项之积 $\mathrm e^{x}\cdot\mathrm e^{2x_{0}-x}=\mathrm e^{2x_{0}}$ 是常数，" "\n"
        r"  这种「指数配对」能把含 $x$ 的项换成常数，是放缩的核心技巧 ✓" "\n"
        r"③ ⭐⭐ **$\mathrm e^{x_{0}}=\sin x_{0}+\mathrm e$ 来自 $f'(x_{0})=0$**：" "\n"
        r"  它是连接 $x_{0}$ 与已量的唯一桥梁，放缩后必须用上，否则 $\sin$ 项无法控制 ✓" "\n"
        r"④ 数值复核：解 $\mathrm e^{x_{0}}-\sin x_{0}=\mathrm e$ 得 $x_{0}=1.303678$。" "\n"
        r"  取 $x_{2}=1.5$，由 $f(x_{1})=f(1.5)$ 解得 $x_{1}=1.088150$（$<x_{0}$ ✓），" "\n"
        r"  $x_{1}+x_{2}=2.588150<2x_{0}=2.607356$ ✓✓✓（$x_{2}$ 越靠近 $x_{0}$ 差值越小）" "\n"
        r"⑤ ⚠ **$x_{0}\in(1,\pi)$ 的定位不能省**：$f'(1)=-\sin1<0$、$f'(\pi)=\mathrm e^{\pi}-\mathrm e>0$，" "\n"
        r"  两个端点值一负一正恰好夹住唯一零点（配合 $f'$ 递增）✓" "\n"
        r"⑥ ⚠ **$g'(x)=\mathrm e^{x}+\cos x>0$ 只在 $x>0$ 时成立**（$\mathrm e^{x}>1\ge-\cos x$），" "\n"
        r"  若 $x\le0$ 需另判 —— 本题区间是 $(0,\pi)$，恰好落在安全范围内 ✓" "\n"
        r"**⭐⭐ 通法（极值点偏移·对称化构造）**：" "\n"
        r"欲证 $x_{1}+x_{2}<2x_{0}$（$x_{1}<x_{0}<x_{2}$），构造 $h(x)=f(x)-f(2x_{0}-x)$（$x<x_{0}$）；" "\n"
        r"  证 $h$ 递增 ⟹ $h(x_{1})<h(x_{0})=0$ ⟹ $f(x_{1})<f(2x_{0}-x_{1})$，" "\n"
        r"  再由 $f$ 在 $(x_{0},+\infty)$ 递增且 $f(x_{2})=f(x_{1})$ 得 $x_{2}<2x_{0}-x_{1}$．" "\n"
        r"  证 $x_{1}+x_{2}>2x_{0}$ 时对称地证 $h$ 递减即可．"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-162'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-162-V1',
}

# ---------------------------------------------------------------- M-T-166-E1
T166_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知 $f(x)=x^{2}-a\ln x$，$a\in\mathbf R$．" "\n"
        r"(1) 讨论 $y=f(x)$ 的单调性；" "\n"
        r"(2) 若 $y=f(x)$ 有两个零点 $x_{1},x_{2}$（$x_{1}<x_{2}$），$x_{0}$ 是 $y=f(x)$ 的极值点，"
        r"求证：$x_{1}+3x_{2}>4x_{0}$．"
    ),
    'opts': [],
    'answer': r"(1) $a\le0$ 时在 $(0,+\infty)$ 上递增；$a>0$ 时在 $\left(0,\sqrt{\dfrac a2}\right)$ 上递减、在 $\left(\sqrt{\dfrac a2},+\infty\right)$ 上递增；(2) 证明见解析",
    'analysis': (
        r"(1) $f'(x)=\dfrac{2x^{2}-a}x$，按 $a\le0$、$a>0$ 讨论；(2) 由 $f(x_{1})=f(x_{2})$ 设 "
        r"$t=\dfrac{x_{2}}{x_{1}}>1$，解出 $x_{1}^{2}=\dfrac{a\ln t}{t^{2}-1}$，把待证式化为"
        r"关于 $t$ 的一元不等式 $\ln t(1+3t)^{2}-8t^{2}+8>0$，两次求导完成．"
    ),
    'solution': (
        r"**(1)** $f'(x)=2x-\dfrac ax=\dfrac{2x^{2}-a}x$（$x>0$）．" "\n"
        r" ① 当 $a\le0$ 时，$2x^{2}-a>0$ 恒成立，故 $f'(x)>0$，$f(x)$ 在 $(0,+\infty)$ 上单调递增．" "\n"
        r" ② 当 $a>0$ 时，令 $f'(x)=0$ 得 $x=\sqrt{\dfrac a2}$（负根舍去）；" "\n"
        r"  当 $0<x<\sqrt{\dfrac a2}$ 时 $f'(x)<0$，$f$ 递减；当 $x>\sqrt{\dfrac a2}$ 时 $f'(x)>0$，$f$ 递增．" "\n"
        r"**(2)** 由 (1) 知极值点 $x_{0}=\sqrt{\dfrac a2}$．" "\n"
        r"若 $f$ 有两个零点，则极小值 $f(x_{0})<0$，即 " "\n"
        r"$f\left(\sqrt{\dfrac a2}\right)=\dfrac a2-a\ln\sqrt{\dfrac a2}=\dfrac a2-\dfrac a2\ln\dfrac a2<0"
        r"\iff\ln\dfrac a2>1\iff a>2\mathrm e$（此时必有 $a>0$）．" "\n"
        r"由 $0<x_{1}<\sqrt{\dfrac a2}<x_{2}$，设 $t=\dfrac{x_{2}}{x_{1}}>1$．" "\n"
        r"由 $f(x_{1})=f(x_{2})$ 得 $x_{1}^{2}-a\ln x_{1}=x_{2}^{2}-a\ln x_{2}=t^{2}x_{1}^{2}-a\ln(tx_{1})$，" "\n"
        r"即 $x_{1}^{2}-a\ln x_{1}=t^{2}x_{1}^{2}-a\ln t-a\ln x_{1}$，" "\n"
        r"$\therefore(t^{2}-1)x_{1}^{2}=a\ln t$，即 $x_{1}^{2}=\dfrac{a\ln t}{t^{2}-1}$．" "\n"
        r"待证 $x_{1}+3x_{2}>4x_{0}$，即 $x_{1}(1+3t)>4\sqrt{\dfrac a2}=2\sqrt{2a}$．" "\n"
        r"两边均为正，平方得 $x_{1}^{2}(1+3t)^{2}>8a$，代入 $x_{1}^{2}=\dfrac{a\ln t}{t^{2}-1}$ 得" "\n"
        r"$\dfrac{a\ln t}{t^{2}-1}(1+3t)^{2}>8a$．" "\n"
        r"$\because a>0$、$t>1$（故 $t^{2}-1>0$），两边同除以 $a$ 并乘 $(t^{2}-1)$ 得" "\n"
        r"$\ln t\,(1+3t)^{2}-8(t^{2}-1)>0$，即 $\ln t\,(1+3t)^{2}-8t^{2}+8>0$．" "\n"
        r"令 $h(t)=\ln t\,(1+3t)^{2}-8t^{2}+8$（$t\ge1$），则" "\n"
        r"$h'(t)=\dfrac{(1+3t)^{2}}t+6(1+3t)\ln t-16t=\dfrac{1+6t+9t^{2}}t+6(1+3t)\ln t-16t$" "\n"
        r"$=\dfrac1t+6+9t+6(1+3t)\ln t-16t=\dfrac1t+6-7t+6(1+3t)\ln t$．" "\n"
        r"令 $n(t)=\dfrac1t+6-7t+6(1+3t)\ln t$，则 " "\n"
        r"$n'(t)=-\dfrac1{t^{2}}-7+18\ln t+\dfrac{6(1+3t)}t=-\dfrac1{t^{2}}-7+18\ln t+\dfrac6t+18$" "\n"
        r"$=18\ln t+11+\dfrac6t-\dfrac1{t^{2}}$．" "\n"
        r"当 $t>1$ 时 $\ln t>0$、$11-\dfrac1{t^{2}}>10>0$、$\dfrac6t>0$，故 $n'(t)>0$．" "\n"
        r"$\therefore n(t)$ 在 $(1,+\infty)$ 上递增，且 $n(1)=1+6-7+0=0$，故 $t>1$ 时 $n(t)>0$，" "\n"
        r"即 $h'(t)>0$，$\therefore h(t)$ 在 $(1,+\infty)$ 上递增，且 $h(1)=0\cdot16-8+8=0$．" "\n"
        r"$\therefore t>1$ 时 $h(t)>0$，从而 $x_{1}+3x_{2}>4x_{0}$ 成立．"
    ),
    'review': (
        r"① ⭐⭐ **(2) 的题眼是「比值换元 $t=\dfrac{x_{2}}{x_{1}}$」**：" "\n"
        r"  由 $f(x_{1})=f(x_{2})$ 解出 $x_{1}^{2}=\dfrac{a\ln t}{t^{2}-1}$，两个变量压缩成一个 $t$，" "\n"
        r"  且 $a$ 在后续同除时被约掉 —— 这是 $f$ 为「$x^{2}$ 与 $\ln x$ 之差」的必然结果 ✓✓" "\n"
        r"② ⭐⭐ **平方消去 $x_{0}=\sqrt{\dfrac a2}$ 中的根号**：" "\n"
        r"  $4x_{0}=2\sqrt{2a}$ 含根号，两边平方后变成 $8a$（整数系数），" "\n"
        r"  与 $x_{1}^{2}(1+3t)^{2}$ 恰好同型 —— 这是「系数为 $1+3t$」能配成功的原因 ✓" "\n"
        r"③ 数值复核：$h(1)=0$；$h(1.01)=0.000802>0$；$h(1.2)=0.337924$；" "\n"
        r"  $h(2)=9.964212$；$h(5)=220.016106$ —— **恒正且递增** ✓✓✓" "\n"
        r"④ ⚠ **原书详解有排版遗漏**：「令 $f'(x)=0$ 得 $x=\dfrac a2$」实为 $x=\sqrt{\dfrac a2}$，" "\n"
        r"  判据是后文 $4x_{0}=2\sqrt{2a}$ —— 若 $x_{0}=\dfrac a2$ 则 $4x_{0}=2a$，与后续推导不符 ✓" "\n"
        r"⑤ ⚠ **$a>2\mathrm e$ 保证两个零点存在**：$f(x_{0})=\dfrac a2\left(1-\ln\dfrac a2\right)<0"
        r"\iff\ln\dfrac a2>1$；" "\n"
        r"  又 $x\to0^{+}$ 时 $f\to+\infty$、$x\to+\infty$ 时 $f\to+\infty$，故恰有两个零点 ✓" "\n"
        r"⑥ ⭐⭐ **$n(1)=0$ 与 $h(1)=0$ 两层「起点为 $0$」**：" "\n"
        r"  先由 $n'(t)>0$ 与 $n(1)=0$ 得 $n(t)>0$（即 $h'(t)>0$），" "\n"
        r"  再由 $h'(t)>0$ 与 $h(1)=0$ 得 $h(t)>0$ —— 两级递推，缺一不可 ✓" "\n"
        r"**⭐⭐ 通法（比值换元证双零点不等式）**：" "\n"
        r"若 $f(x_{1})=f(x_{2})$ 且 $f$ 含 $\ln x$（或 $x^{2}$），设 $t=\dfrac{x_{2}}{x_{1}}>1$，" "\n"
        r"  用 $f(x_{1})=f(tx_{1})$ 解出 $x_{1}$ 关于 $t$ 的表达式，代入待证式化为 $t$ 的一元不等式，" "\n"
        r"  最后两次求导（先证导数递增、再用起点值为 $0$）完成证明．"
    ),
    'difficulty': 0.93,
    'topics': ['M-T-166'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-166-E1',
}

QS = [
    T127_V2,
    T131_V2,
    T131_V3,
    T138_E1,
    T139_V2,
    T140_V1,
    T142_V2,
    T143_E1,
    T147_E1,
    T156_E1,
    T158_V1,
    T161_V1,
    T162_V1,
    T166_E1,
]
