# -*- coding: utf-8 -*-
r"""第 113 批：导数构造函数小题 + 导数压轴解答题

    python3 tools/run_batch.py 113

## 选题依据

按「详解完整 + 同页聚堆 + 无图依赖 + 可独立数值验算」筛出，原文集中在 p084、p113、p117、p123、p125 五页：

- M-T-117-V2、M-T-117-V3（p084）：构造 $xf\left(x\right)$ 与 $e^{x}f\left(x\right)-2e^{x}$
- M-T-146-V1、M-T-146-V2（p113）：反函数求导与端点值讨论型
- M-T-151-V1、M-T-151-V2（p117）：求参与构造巧证
- M-T-159-E1、M-T-159-V1、M-T-159-V2（p123）：单调性 / 零点 / 双变量不等式
- M-T-160-E1（p125）：凹凸翻转型

10 题全部由我独立推导一遍并数值对拍（过程写进每题 review）。

## 本批跳过 3 题（已登记）

- **M-T-116-E1、M-T-116-V1（p082）**：OCR 中根号普遍丢失（$\sqrt3$ 存成 `3`、$\sqrt2$ 存成 `2`），且四个选项与详解交错、无法可靠重建。
- **M-T-160-V1（p125）**：第（2）问所求式的 $\dfrac{x+1-e}{xe^{x+1-e}}$ 结构在原文中破碎（`- e1` 结尾），无法确认分母，不硬凑。

## 第一条：构造 $F\left(x\right)=xf\left(x\right)$ 后直接积分（M-T-117-V2）

$$F'\left(x\right)=xf'\left(x\right)+f\left(x\right)=e^{x}\left(x-2\right)\ \Longrightarrow\ F\left(x\right)=e^{x}\left(x-3\right)+C$$

> ⭐⭐ 判据：**$xf'\left(x\right)+f\left(x\right)$ 就是 $\left[xf\left(x\right)\right]'$**，看到这个组合直接写 $F=xf$。
> ⭐ $e^{x}\left(x-2\right)$ 的原函数是 $e^{x}\left(x-3\right)$（因为 $\left[e^{x}\left(x-3\right)\right]'=e^{x}\left(x-3\right)+e^{x}=e^{x}\left(x-2\right)$）—— 这个「$-3$ 不是 $-2$」最易错。

## 第二条：$f\left(x\right)+f'\left(x\right)>k$ 构造 $e^{x}f\left(x\right)-ke^{x}$（M-T-117-V3）

$$g\left(x\right)=e^{x}f\left(x\right)-2e^{x}\ \Longrightarrow\ g'\left(x\right)=e^{x}\left[f\left(x\right)+f'\left(x\right)-2\right]>0$$

> ⭐⭐ 判据：**$f+f'$ 配 $e^{x}$**，且常数项 $-k$ 要乘 $e^{x}$ 一起放进 $g$。
> ⭐ 本题 $g\left(0\right)=f\left(0\right)-2=2018$，而不等式恰是 $g\left(x\right)>2018$ —— 两端都指向同一个数，这就是构造正确的信号。

## 第三条：$F'\left(x\right)=\frac1x-e^{x}$ 的零点是 $\Omega$ 常数（M-T-146-V1）

$\frac1x$ 递减、$-e^{x}$ 递减 ⟹ $F'$ 严格递减，只需两个端点变号：$F'\left(\frac12\right)=2-\sqrt e>0$、$F'\left(1\right)=1-e<0$。

> ⭐⭐ 判据：**两个递减函数之和仍递减**，于是「有且只有一个变号零点」只需验两点异号。
> 数值上 $x_{0}\approx0.567143$（正是 $\Omega$ 常数，满足 $xe^{x}=1$）。

## 第四条：端点值讨论型的「先必要后充分」（M-T-146-V2）

$p\left(x\right)>0$ 在 $\left[1,+\infty\right)$ 恒成立。先取 $x=1$ 得**必要条件** $p\left(1\right)=1-a>0$，即 $a<1$；再证 $a<1$ 时 $p'\left(x\right)=4\left(x-a\right)\left(\ln x+1\right)>0$，故 $p$ 递增、$p\left(1\right)$ 就是最小值，**充分性也得证**。

> ⭐⭐ 判据：**$a>1$ 那一支不用算到底** —— 最小值 $p\left(a\right)=a^{2}\left(1-2\ln a\right)-a=a\cdot q\left(a\right)$，而 $q\left(a\right)<q\left(1\right)=0$，直接矛盾。
> ⭐ $q'\left(a\right)=-1-2\ln a$（原书写作 $1-2\ln a$，漏了 $-1$，结论不受影响）。

## 第五条：$\dfrac{f\left(x\right)+2}{x}$ 型分离参数（M-T-159-V1）

$f\left(x\right)\ge bx-2$ ⟺ $f\left(x\right)+2\ge bx$ ⟺ $\dfrac{f\left(x\right)+2}{x}\ge b$（$x>0$）。

> ⭐⭐ 判据：**参数是 $b$ 的一次项 ⟹ 除以 $x>0$ 直接分离**，不必讨论。
> $\dfrac{x+1-\ln x}{x}=1+\dfrac{1-\ln x}{x}$，其导数 $g'\left(x\right)=\dfrac{\ln x-2}{x^{2}}$ ⟹ 最小在 $x=e^{2}$ 处，$g_{\min}=1-\dfrac1{e^{2}}$。

## 第六条：双变量 $m>n$ 型 ⟹ 化为单变量单调性（M-T-159-V2）

$$me^{n}+n<ne^{m}+m\ \Longleftrightarrow\ m\left(e^{n}-1\right)<n\left(e^{m}-1\right)\ \Longleftrightarrow\ \frac{e^{n}-1}{n}<\frac{e^{m}-1}{m}$$

> ⭐⭐ 判据：**把 $m$、$n$ 分别移到不等号两侧，凑成同一个函数的两个取值**，剩下只需证 $h\left(x\right)=\dfrac{e^{x}-1}{x}$ 递增。
> $h'\left(x\right)=\dfrac{e^{x}\left(x-1\right)+1}{x^{2}}$，分子 $\varphi\left(x\right)=e^{x}\left(x-1\right)+1$ 满足 $\varphi\left(0\right)=0$、$\varphi'\left(x\right)=xe^{x}>0$。

## 第七条：「两个最值点不同」给出严格不等号（M-T-160-E1）

$f\left(x\right)=x\ln x$ 最小值 $-\frac1e$ 在 $x=\frac1e$ 取到；$m\left(x\right)=\frac x{e^{x}}-\frac2e$ 最大值 $-\frac1e$ 在 $x=1$ 取到。

> ⭐⭐ 判据：**两端极值相等但取等点不同 ⟹ 严格不等号成立**。这是「证明 $>$ 但两边极值相同」类题的唯一出路。
"""

# ==========================================================================
#  M-T-117  导数构造函数（小题）
# ==========================================================================

T117_V2 = {
    'type': '填空',
    'stem_text': (
        r"函数 $f\left(x\right)$ 是定义在 $\left(0,+\infty\right)$ 上的可导函数，$f'\left(x\right)$ 为其导函数，"
        r"若 $xf'\left(x\right)+f\left(x\right)=e^{x}\left(x-2\right)$ 且 $f\left(3\right)=0$，"
        r"则不等式 $f\left(x\right)<0$ 的解集为 ____"
    ),
    'stem': [
        r"函数 $f\left(x\right)$ 是定义在 $\left(0,+\infty\right)$ 上的可导函数，$f'\left(x\right)$ 为其导函数，"
        r"若 $xf'\left(x\right)+f\left(x\right)=e^{x}\left(x-2\right)$ 且 $f\left(3\right)=0$，"
        r"则不等式 $f\left(x\right)<0$ 的解集为 ____",
    ],
    'opts': [],
    'answer': r"$\left(0,3\right)$",
    'analysis': (
        r"由 $xf'\left(x\right)+f\left(x\right)=\left[xf\left(x\right)\right]'$，构造函数 $F\left(x\right)=xf\left(x\right)$；"
        r"再由 $F\left(3\right)=3f\left(3\right)=0$ 定出积分常数，得到 $f\left(x\right)$ 的显式，直接解不等式。"
    ),
    'solution': (
        r"由乘积求导法则，" "\n"
        r"$$\left[xf\left(x\right)\right]'=xf'\left(x\right)+f\left(x\right)=e^{x}\left(x-2\right).$$" "\n"
        r"又 $\left[e^{x}\left(x-3\right)\right]'=e^{x}\left(x-3\right)+e^{x}=e^{x}\left(x-2\right)$，故可设" "\n"
        r"$$xf\left(x\right)=e^{x}\left(x-3\right)+C.$$" "\n"
        r"由 $f\left(3\right)=0$ 得 $3f\left(3\right)=e^{3}\left(3-3\right)+C=C=0$，即 $C=0$，于是" "\n"
        r"$$f\left(x\right)=\frac{e^{x}\left(x-3\right)}x,\qquad x>0.$$" "\n"
        r"因为 $e^{x}>0$、$x>0$，所以 $f\left(x\right)<0$ 等价于 $x-3<0$，即 $0<x<3$。" "\n"
        r"故解集为 $\left(0,3\right)$。"
    ),
    'review': (
        r"① ⭐⭐ **识别 $\left[xf\left(x\right)\right]'$**：$xf'\left(x\right)+f\left(x\right)$ 是乘积求导的标志性组合，"
        r"见到就写 $F\left(x\right)=xf\left(x\right)$。" "\n"
        r"② ⚠ **$e^{x}\left(x-2\right)$ 的原函数是 $e^{x}\left(x-3\right)$ 而非 $e^{x}\left(x-2\right)$**：" "\n"
        r"   $\left[e^{x}\left(x-3\right)\right]'=e^{x}\left(x-3\right)+e^{x}=e^{x}\left(x-2\right)$，常数差 $1$ 来自 $\left(e^{x}\right)'=e^{x}$。" "\n"
        r"   若误写成 $e^{x}\left(x-2\right)$，则由 $F\left(3\right)=0$ 得 $C=-e^{3}$，后续全错。" "\n"
        r"③ ⭐ **用 $F\left(3\right)=0$ 而非 $f\left(3\right)=0$ 定常数**：$F\left(3\right)=3f\left(3\right)=0$，两者等价（因 $3\ne0$）。" "\n"
        r"④ 数值复核（$f\left(x\right)=e^{x}\left(x-3\right)/x$）：" "\n"
        r"   $x=0.5$：$f=e^{0.5}\left(-2.5\right)/0.5=-8.2436<0$ ✓；" "\n"
        r"   $x=1$：$f=e^{1}\left(-2\right)/1=-5.4366<0$ ✓；" "\n"
        r"   $x=2$：$f=e^{2}\left(-1\right)/2=-3.6945<0$ ✓；" "\n"
        r"   $x=3$：$f=0$ ✓（端点）；$x=3.5$：$f=4.7308>0$ ✓" "\n"
        r"**通法（$xf'+f$ 型）**：" "\n"
        r"① 写 $F\left(x\right)=xf\left(x\right)$，则 $F'=xf'+f$；" "\n"
        r"② 对 $F'$ 积分（注意 $e^{x}$ 类要凑 $e^{x}\left(x-k\right)$ 的形式）；" "\n"
        r"③ 用已知点定常数，还原 $f\left(x\right)=F\left(x\right)/x$，再解不等式。"
    ),
    'difficulty': 0.58,
    'topics': ['M-T-117'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-117-V2',
}

T117_V3 = {
    'type': '选择',
    'stem_text': (
        r"设定义在 $\mathbf R$ 上的函数 $f\left(x\right)$ 的导函数为 $f'\left(x\right)$，"
        r"若 $f\left(x\right)+f'\left(x\right)>2$，$f\left(0\right)=2020$，"
        r"则不等式 $e^{x}f\left(x\right)>2e^{x}+2018$（其中 $e$ 为自然对数的底数）的解集为（　　）"
    ),
    'stem': [
        r"设定义在 $\mathbf R$ 上的函数 $f\left(x\right)$ 的导函数为 $f'\left(x\right)$，"
        r"若 $f\left(x\right)+f'\left(x\right)>2$，$f\left(0\right)=2020$，"
        r"则不等式 $e^{x}f\left(x\right)>2e^{x}+2018$（其中 $e$ 为自然对数的底数）的解集为（　　）",
    ],
    'opts': [
        ('A', r"$\left(0,+\infty\right)$"),
        ('B', r"$\left(2018,+\infty\right)$"),
        ('C', r"$\left(2020,+\infty\right)$"),
        ('D', r"$\left(-\infty,0\right)\cup\left(2018,+\infty\right)$"),
    ],
    'answer': 'A',
    'analysis': (
        r"构造 $g\left(x\right)=e^{x}f\left(x\right)-2e^{x}$，则 $g'\left(x\right)=e^{x}\left[f\left(x\right)+f'\left(x\right)-2\right]>0$，"
        r"故 $g$ 递增；又 $g\left(0\right)=f\left(0\right)-2=2018$，原不等式即 $g\left(x\right)>g\left(0\right)$。"
    ),
    'solution': (
        r"设 $g\left(x\right)=e^{x}f\left(x\right)-2e^{x}$，则" "\n"
        r"$$g'\left(x\right)=e^{x}f\left(x\right)+e^{x}f'\left(x\right)-2e^{x}=e^{x}\left[f\left(x\right)+f'\left(x\right)-2\right].$$" "\n"
        r"因为 $f\left(x\right)+f'\left(x\right)>2$ 且 $e^{x}>0$，所以 $g'\left(x\right)>0$，即 $g\left(x\right)$ 在 $\mathbf R$ 上单调递增。" "\n"
        r"又 $g\left(0\right)=e^{0}f\left(0\right)-2e^{0}=f\left(0\right)-2=2020-2=2018$。" "\n"
        r"原不等式 $e^{x}f\left(x\right)>2e^{x}+2018$ 等价于" "\n"
        r"$$e^{x}f\left(x\right)-2e^{x}>2018,\quad\text{即}\quad g\left(x\right)>2018=g\left(0\right).$$" "\n"
        r"由 $g$ 递增得 $x>0$，故解集为 $\left(0,+\infty\right)$，选 A。"
    ),
    'review': (
        r"① ⭐⭐ **$f+f'$ 配 $e^{x}$**：$\left[e^{x}f\left(x\right)\right]'=e^{x}\left(f+f'\right)$，这是最基础的构造之一。" "\n"
        r"② ⭐ **常数 $-2$ 也要乘 $e^{x}$**：$g=e^{x}f-2e^{x}$，于是 $g'=e^{x}\left(f+f'-2\right)$ 恰好用上已知条件。" "\n"
        r"   若只取 $g=e^{x}f\left(x\right)$，则 $g'=e^{x}\left(f+f'\right)>2e^{x}$，得不到单调性的干净结论。" "\n"
        r"③ ⭐⭐ **两端都指向 $2018$ 是强信号**：$g\left(0\right)=2018$，待解不等式化为 $g\left(x\right)>2018$。" "\n"
        r"   这种「构造后两端恰好对齐」说明构造方向正确；若对不齐，多半是常数项没配对。" "\n"
        r"④ ⚠ **干扰项 B、C 的设计**：$2018$、$2020$ 分别来自 $f\left(0\right)-2$ 与 $f\left(0\right)$，" "\n"
        r"   命题人把「中间量」做成选项，看你是否误把 $g\left(0\right)$ 当成 $f\left(0\right)$。" "\n"
        r"⑤ 单调性复核：$g$ 严格递增，$g\left(x\right)>g\left(0\right)\iff x>0$ ✓" "\n"
        r"**通法（$f+f'>k$ 型）**：" "\n"
        r"① 构造 $g\left(x\right)=e^{x}f\left(x\right)-ke^{x}$；" "\n"
        r"② 由 $g'=e^{x}\left(f+f'-k\right)$ 的符号定单调；" "\n"
        r"③ 把待解不等式整理成 $g\left(x\right)>g\left(x_{0}\right)$ 的形式（通常 $x_{0}$ 是已知点）。"
    ),
    'difficulty': 0.55,
    'topics': ['M-T-117'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-117-V3',
}

# ==========================================================================
#  M-T-146  导数压轴：反函数与端点值讨论型
# ==========================================================================

T146_V1 = {
    'type': '解答',
    'stem_text': (
        r"若函数 $f\left(x\right)$ 的反函数记为 $f^{-1}\left(x\right)$，已知函数 $f\left(x\right)=e^{x}$．" "\n"
        r"（1）设函数 $F\left(x\right)=f^{-1}\left(x\right)-f\left(x\right)$，试判断函数 $F\left(x\right)$ 的极值点个数；" "\n"
        r"（2）当 $x\in\left[0,\dfrac\pi2\right]$ 时，$f\left(x\right)\cdot\sin x\ge kx$，求实数 $k$ 的取值范围．"
    ),
    'stem': [
        r"若函数 $f\left(x\right)$ 的反函数记为 $f^{-1}\left(x\right)$，已知函数 $f\left(x\right)=e^{x}$．",
        r"（1）设函数 $F\left(x\right)=f^{-1}\left(x\right)-f\left(x\right)$，试判断函数 $F\left(x\right)$ 的极值点个数；",
        r"（2）当 $x\in\left[0,\dfrac\pi2\right]$ 时，$f\left(x\right)\cdot\sin x\ge kx$，求实数 $k$ 的取值范围．",
    ],
    'opts': [],
    'answer': r"（1）$1$ 个；（2）$\left(-\infty,1\right]$",
    'analysis': (
        r"（1）$f^{-1}\left(x\right)=\ln x$（$x>0$），故 $F\left(x\right)=\ln x-e^{x}$；"
        r"$F'\left(x\right)=\frac1x-e^{x}$ 是两个减函数之差，严格递减，验两点异号即可定唯一零点。"
        r"（2）作 $g\left(x\right)=e^{x}\sin x-kx$，由 $g\left(0\right)=0$ 知必须有 $g'\left(0\right)\ge0$，"
        r"再用 $h\left(x\right)=e^{x}\left(\sin x+\cos x\right)$ 的单调性分类。"
    ),
    'solution': (
        r"（1）由 $f\left(x\right)=e^{x}$ 得 $f^{-1}\left(x\right)=\ln x$（$x>0$），于是" "\n"
        r"$$F\left(x\right)=\ln x-e^{x},\qquad x>0,\qquad F'\left(x\right)=\frac1x-e^{x}.$$" "\n"
        r"在 $\left(0,+\infty\right)$ 上，$\dfrac1x$ 单调递减，$-e^{x}$ 也单调递减，故 $F'\left(x\right)$ 严格递减。" "\n"
        r"又 $F'\left(\dfrac12\right)=2-\sqrt e>0$（因 $\sqrt e\approx1.6487$），$F'\left(1\right)=1-e<0$，" "\n"
        r"所以 $F'\left(x\right)$ 在 $\left(0,+\infty\right)$ 上有且只有一个变号零点，" "\n"
        r"即 $F\left(x\right)$ 有且只有一个极值点。" "\n"
        r"（2）令 $g\left(x\right)=f\left(x\right)\sin x-kx=e^{x}\sin x-kx$，$x\in\left[0,\dfrac\pi2\right]$，" "\n"
        r"题意即 $g\left(x\right)\ge0$ 恒成立。注意 $g\left(0\right)=0$。" "\n"
        r"$$g'\left(x\right)=e^{x}\left(\sin x+\cos x\right)-k.$$" "\n"
        r"令 $h\left(x\right)=e^{x}\left(\sin x+\cos x\right)$，则" "\n"
        r"$$h'\left(x\right)=e^{x}\left(\sin x+\cos x\right)+e^{x}\left(\cos x-\sin x\right)=2e^{x}\cos x>0\quad\left(x\in\left(0,\frac\pi2\right)\right),$$" "\n"
        r"故 $h\left(x\right)$ 在 $\left[0,\dfrac\pi2\right]$ 上单调递增，值域为 $\left[h\left(0\right),h\left(\dfrac\pi2\right)\right]=\left[1,e^{\pi/2}\right]$。" "\n"
        r"① 当 $k\le1$ 时，$g'\left(x\right)=h\left(x\right)-k\ge1-k\ge0$，$g$ 单调递增，" "\n"
        r"　 故 $g\left(x\right)\ge g\left(0\right)=0$ 恒成立，满足题意；" "\n"
        r"② 当 $1<k<e^{\pi/2}$ 时，由 $h$ 递增且连续知存在唯一 $x_{0}\in\left(0,\dfrac\pi2\right)$ 使 $h\left(x_{0}\right)=k$，" "\n"
        r"　 当 $x\in\left(0,x_{0}\right)$ 时 $h\left(x\right)<k$，即 $g'\left(x\right)<0$，$g$ 递减，" "\n"
        r"　 故 $g\left(x\right)<g\left(0\right)=0$，不满足题意；" "\n"
        r"③ 当 $k\ge e^{\pi/2}$ 时，$g'\left(x\right)=h\left(x\right)-k\le0$，$g$ 在 $\left[0,\dfrac\pi2\right]$ 上递减，" "\n"
        r"　 当 $x>0$ 时 $g\left(x\right)<g\left(0\right)=0$，不满足题意。" "\n"
        r"综上，$k\in\left(-\infty,1\right]$。"
    ),
    'review': (
        r"① ⭐⭐ **反函数先写出来**：$f\left(x\right)=e^{x}$ 的反函数是 $\ln x$，定义域 $x>0$。" "\n"
        r"   忘记写定义域会导致 $F\left(x\right)$ 的定义域错误。" "\n"
        r"② ⭐⭐ **两个减函数之和仍递减**：$F'=\frac1x-e^{x}$ 中 $\frac1x$ 减、$-e^{x}$ 减，故 $F'$ 严格递减，" "\n"
        r"   于是「唯一变号零点」只需验两点异号，不必解方程。" "\n"
        r"③ 数值复核：$F'\left(0.5\right)=0.3513>0$、$F'\left(0.567\right)=0.0007\approx0$、$F'\left(1\right)=-1.7183<0$ ✓" "\n"
        r"   零点 $x_{0}\approx0.567143$（$\Omega$ 常数，满足 $xe^{x}=1$）。" "\n"
        r"④ ⭐ **$h'\left(x\right)=2e^{x}\cos x$ 的化简技巧**：" "\n"
        r"   $\left(\sin x+\cos x\right)'=\cos x-\sin x$，与本身相加后 $\sin x$ 抵消，只剩 $2\cos x$。" "\n"
        r"⑤ ⭐⭐ **$k\le1$ 的临界性**：$g\left(0\right)=0$ 且要求 $g\ge0$，$g$ 必须从 $x=0$ 起不下降，" "\n"
        r"   故 $k\le h\left(0\right)=1$ 是必要条件；本题它恰好也是充分的（因 $h$ 递增）。" "\n"
        r"⑥ 数值复核：$k=1$ 时 $g$ 在 $\left[0,\frac\pi2\right]$ 上的最小值为 $0$（在 $x=0$ 取到）✓；" "\n"
        r"   $k=1.5$ 时最小值为 $-0.0581<0$ ✗；$k=2$ 时最小值为 $-0.2194<0$ ✗" "\n"
        r"**通法（端点型恒成立）**：" "\n"
        r"① 把不等式移项成 $g\left(x\right)\ge0$，注意 $g\left(0\right)$ 是否为 $0$；" "\n"
        r"② 若 $g\left(0\right)=0$，则必须有 $g'\left(0\right)\ge0$（先得必要条件）；" "\n"
        r"③ 对 $g'$ 中含参数的项提取成独立函数 $h\left(x\right)$，用 $h$ 的单调性验证充分性。"
    ),
    'difficulty': 0.68,
    'topics': ['M-T-146'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-146-V1',
}

T146_V2 = {
    'type': '解答',
    'stem_text': (
        r"设函数 $f\left(x\right)=\left(x^{2}-2ax\right)\ln x+bx^{2}$，$a,b\in\mathbf R$．" "\n"
        r"（1）当 $a=1$，$b=-1$ 时，设 $g\left(x\right)=\left(x-1\right)^{2}\ln x+x$，"
        r"求证：对任意的 $x>1$，$g\left(x\right)-f\left(x\right)>x^{2}+x+e-e^{x}$；" "\n"
        r"（2）当 $b=2$ 时，若对任意 $x\in\left[1,+\infty\right)$，不等式 $2f\left(x\right)>3x^{2}+a$ 恒成立，"
        r"求实数 $a$ 的取值范围．"
    ),
    'stem': [
        r"设函数 $f\left(x\right)=\left(x^{2}-2ax\right)\ln x+bx^{2}$，$a,b\in\mathbf R$．",
        r"（1）当 $a=1$，$b=-1$ 时，设 $g\left(x\right)=\left(x-1\right)^{2}\ln x+x$，求证：对任意的 $x>1$，$g\left(x\right)-f\left(x\right)>x^{2}+x+e-e^{x}$；",
        r"（2）当 $b=2$ 时，若对任意 $x\in\left[1,+\infty\right)$，不等式 $2f\left(x\right)>3x^{2}+a$ 恒成立，求实数 $a$ 的取值范围．",
    ],
    'opts': [],
    'answer': r"（1）证明见解析；（2）$\left(-\infty,1\right)$",
    'analysis': (
        r"（1）代入 $a=1,b=-1$ 后，$g\left(x\right)-f\left(x\right)$ 中的 $x^{2}\ln x$ 项恰好抵消，"
        r"化简得 $\ln x+x+x^{2}$，所证式化为 $e^{x}+\ln x-e>0$。"
        r"（2）移项得 $p\left(x\right)=\left(2x^{2}-4ax\right)\ln x+x^{2}-a>0$，"
        r"由 $p'\left(x\right)=4\left(x-a\right)\left(\ln x+1\right)$ 按 $a\le1$ 与 $a>1$ 分类。"
    ),
    'solution': (
        r"（1）当 $a=1$，$b=-1$ 时，$f\left(x\right)=\left(x^{2}-2x\right)\ln x-x^{2}$，于是" "\n"
        r"$$g\left(x\right)-f\left(x\right)=\left(x-1\right)^{2}\ln x+x-\left(x^{2}-2x\right)\ln x+x^{2}$$" "\n"
        r"$$=\big[\left(x^{2}-2x+1\right)-\left(x^{2}-2x\right)\big]\ln x+x+x^{2}=\ln x+x+x^{2}.$$" "\n"
        r"故所证不等式等价于 $\ln x+x+x^{2}>x^{2}+x+e-e^{x}$，即 $e^{x}+\ln x-e>0$。" "\n"
        r"令 $h\left(x\right)=e^{x}+\ln x-e$，则 $h'\left(x\right)=e^{x}+\dfrac1x>0$，" "\n"
        r"故 $h\left(x\right)$ 在 $\left(1,+\infty\right)$ 上单调递增，于是 $h\left(x\right)>h\left(1\right)=e+0-e=0$。" "\n"
        r"即 $e^{x}+\ln x-e>0$ 成立，原不等式得证。" "\n"
        r"（2）当 $b=2$ 时，$f\left(x\right)=\left(x^{2}-2ax\right)\ln x+2x^{2}$，" "\n"
        r"$2f\left(x\right)>3x^{2}+a$ 等价于" "\n"
        r"$$\left(2x^{2}-4ax\right)\ln x+x^{2}-a>0.$$" "\n"
        r"令 $p\left(x\right)=\left(2x^{2}-4ax\right)\ln x+x^{2}-a$，$x\in\left[1,+\infty\right)$，则" "\n"
        r"$$p'\left(x\right)=\left(4x-4a\right)\ln x+\frac{2x^{2}-4ax}x+2x=4\left(x-a\right)\ln x+4x-4a=4\left(x-a\right)\left(\ln x+1\right).$$" "\n"
        r"当 $x\ge1$ 时 $\ln x+1>0$，故 $p'\left(x\right)$ 的符号由 $x-a$ 决定。" "\n"
        r"① 当 $a\le1$ 时，$x\ge1\ge a$，$p'\left(x\right)\ge0$，$p\left(x\right)$ 在 $\left[1,+\infty\right)$ 上单调递增，" "\n"
        r"　 故 $p_{\min}=p\left(1\right)=0+1-a=1-a$。由 $p\left(x\right)>0$ 恒成立得 $1-a>0$，即 $a<1$。" "\n"
        r"② 当 $a>1$ 时，$p\left(x\right)$ 在 $\left[1,a\right)$ 上递减、在 $\left(a,+\infty\right)$ 上递增，" "\n"
        r"　 故 $p_{\min}=p\left(a\right)=\left(2a^{2}-4a^{2}\right)\ln a+a^{2}-a=a^{2}\left(1-2\ln a\right)-a=a\big[a\left(1-2\ln a\right)-1\big]$。" "\n"
        r"　 设 $q\left(a\right)=a\left(1-2\ln a\right)-1$（$a>1$），则 $q'\left(a\right)=1-2\ln a-2=-1-2\ln a<0$，" "\n"
        r"　 故 $q\left(a\right)$ 在 $\left(1,+\infty\right)$ 上递减，$q\left(a\right)<q\left(1\right)=1\times1-1=0$。" "\n"
        r"　 又 $a>0$，故 $p_{\min}=a\cdot q\left(a\right)<0$，与 $p\left(x\right)>0$ 恒成立矛盾。" "\n"
        r"综上，实数 $a$ 的取值范围为 $\left(-\infty,1\right)$。"
    ),
    'review': (
        r"① ⭐⭐ **（1）中 $x^{2}\ln x$ 项恰好抵消是刻意设计**：" "\n"
        r"   $\left(x-1\right)^{2}=x^{2}-2x+1$，减去 $\left(x^{2}-2x\right)$ 后只剩 $1$，故 $g-f$ 中 $\ln x$ 的系数恰为 $1$。" "\n"
        r"   这种「系数恰好化简」是还原正确的强信号。" "\n"
        r"② ⚠ **原书把 $e^{x}$ 印成 $e^{2}$**（记为 $e2$）：若按 $e^{2}$，则 $h\left(x\right)=e^{2}+\ln x-e$ 恒正，" "\n"
        r"   $h\left(1\right)=e^{2}-e\approx4.67\ne0$，与详解「$h\left(x\right)>h\left(1\right)$」的逻辑链断裂。" "\n"
        r"   按 $e^{x}$ 则 $h\left(1\right)=0$，且 $h$ 递增，完美闭合 ✓ 已进 A 类勘误。" "\n"
        r"③ 数值复核（1）：$x=1.01$ 时 $e^{x}+\ln x-e=0.0373>0$；$x=1.5$ 时 $=2.1689>0$；" "\n"
        r"   $x\to1^{+}$ 时趋于 $0$（取不到），故严格 $>$ 成立 ✓" "\n"
        r"④ ⭐⭐ **（2）的端点值法**：先取 $x=1$ 得必要条件 $p\left(1\right)=1-a>0$，即 $a<1$；" "\n"
        r"   再验证 $a<1$ 时 $p'\ge0$，$p$ 递增，$p\left(1\right)$ 就是最小值 —— 充分性同时得证。" "\n"
        r"   这种「先必要后充分」比直接分类讨论更省事。" "\n"
        r"⑤ ⚠ **原书 $q'\left(a\right)$ 写作 $1-2\ln a$，漏了 $-1$**：正确为 $q'\left(a\right)=-1-2\ln a$。" "\n"
        r"   两者对 $a>1$ 都为负（$1-2\ln a$ 需 $a>\sqrt e$ 才为负），但按原文的写法在 $1<a<\sqrt e$ 时会得出相反结论。" "\n"
        r"⑥ 数值复核（2）：$a=1$ 时 $p\left(1\right)=0$，不满足 $>0$ ✗（故是开区间）；" "\n"
        r"   $a=0.9$ 时 $p\left(1\right)=0.1>0$ ✓；" "\n"
        r"   $a=1.2$ 时 $p_{\min}=p\left(1.2\right)=-0.285<0$ ✗（$a>1$ 确实无解）✓" "\n"
        r"**通法（端点值讨论型）**：" "\n"
        r"① 移项整理成 $p\left(x\right)>0$ 在 $\left[1,+\infty\right)$ 恒成立；" "\n"
        r"② 先代左端点得必要条件（往往一步定出范围）；" "\n"
        r"③ 求导并把符号分解为「$\left(x-a\right)\times$ 恒正因式」，按参数与区间端点的大小分类；" "\n"
        r"④ 另一侧用「最小值 $<0$ 与恒成立矛盾」排除，不必解出具体范围。"
    ),
    'difficulty': 0.72,
    'topics': ['M-T-146'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-146-V2',
}

# ==========================================================================
#  M-T-151  导数压轴：求参与构造巧证
# ==========================================================================

T151_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f\left(x\right)=ax^{2}-\left(a+2\right)x+\ln x$．" "\n"
        r"（1）当 $a>0$ 时，若 $f\left(x\right)$ 在区间 $\left[1,e\right]$ 上的最小值为 $-2$，求 $a$ 的取值范围；" "\n"
        r"（2）若对任意 $x_{1},x_{2}\in\left(0,+\infty\right)$，$x_{1}<x_{2}$，且 $f\left(x_{1}\right)+2x_{1}<f\left(x_{2}\right)+2x_{2}$ 恒成立，"
        r"求 $a$ 的取值范围．"
    ),
    'stem': [
        r"已知函数 $f\left(x\right)=ax^{2}-\left(a+2\right)x+\ln x$．",
        r"（1）当 $a>0$ 时，若 $f\left(x\right)$ 在区间 $\left[1,e\right]$ 上的最小值为 $-2$，求 $a$ 的取值范围；",
        r"（2）若对任意 $x_{1},x_{2}\in\left(0,+\infty\right)$，$x_{1}<x_{2}$，且 $f\left(x_{1}\right)+2x_{1}<f\left(x_{2}\right)+2x_{2}$ 恒成立，求 $a$ 的取值范围．",
    ],
    'opts': [],
    'answer': r"（1）$a\ge1$；（2）$0\le a\le8$",
    'analysis': (
        r"（1）$f'\left(x\right)=\dfrac{\left(2x-1\right)\left(ax-1\right)}x$，两个驻点为 $x=\dfrac12$ 与 $x=\dfrac1a$；"
        r"因区间是 $\left[1,e\right]$，只需按 $\dfrac1a$ 与 $1$、$e$ 的大小分类。"
        r"（2）「$x_{1}<x_{2}$ 时 $f\left(x_{1}\right)+2x_{1}<f\left(x_{2}\right)+2x_{2}$」就是 $g\left(x\right)=f\left(x\right)+2x$ 单调递增，"
        r"化为 $g'\left(x\right)\ge0$ 恒成立，再用判别式。"
    ),
    'solution': (
        r"函数 $f\left(x\right)$ 的定义域为 $\left(0,+\infty\right)$，且" "\n"
        r"$$f'\left(x\right)=2ax-\left(a+2\right)+\frac1x=\frac{2ax^{2}-\left(a+2\right)x+1}x=\frac{\left(2x-1\right)\left(ax-1\right)}x.$$" "\n"
        r"（1）当 $a>0$ 时，令 $f'\left(x\right)=0$ 得 $x=\dfrac12$ 或 $x=\dfrac1a$。" "\n"
        r"① 当 $0<\dfrac1a\le1$ 即 $a\ge1$ 时，在 $\left[1,e\right]$ 上 $f'\left(x\right)>0$，$f\left(x\right)$ 单调递增，" "\n"
        r"　 故最小值为 $f\left(1\right)=a-\left(a+2\right)+0=-2$，符合题意；" "\n"
        r"② 当 $1<\dfrac1a<e$ 时，最小值为 $f\left(\dfrac1a\right)<f\left(1\right)=-2$，不合题意；" "\n"
        r"③ 当 $\dfrac1a\ge e$ 时，$f\left(x\right)$ 在 $\left(1,e\right)$ 上单调递减，" "\n"
        r"　 故最小值为 $f\left(e\right)<f\left(1\right)=-2$，不合题意。" "\n"
        r"综上，$a\ge1$。" "\n"
        r"（2）设 $g\left(x\right)=f\left(x\right)+2x=ax^{2}-ax+\ln x$，则题设等价于 $g\left(x\right)$ 在 $\left(0,+\infty\right)$ 上单调递增，" "\n"
        r"即 $g'\left(x\right)=2ax-a+\dfrac1x=\dfrac{2ax^{2}-ax+1}x\ge0$ 在 $\left(0,+\infty\right)$ 上恒成立。" "\n"
        r"因 $x>0$，只需 $\varphi\left(x\right)=2ax^{2}-ax+1\ge0$ 恒成立。" "\n"
        r"① 当 $a=0$ 时，$\varphi\left(x\right)\equiv1>0$，成立；" "\n"
        r"② 当 $a\ne0$ 时，需 $a>0$（否则开口向下，$x\to+\infty$ 时 $\varphi\to-\infty$）。" "\n"
        r"　 此时 $\varphi\left(x\right)$ 是开口向上的二次函数，图象过定点 $\left(0,1\right)$，对称轴 $x=\dfrac14>0$，" "\n"
        r"　 故只需判别式 $\Delta=a^{2}-8a\le0$，解得 $0<a\le8$。" "\n"
        r"综上，$0\le a\le8$。"
    ),
    'review': (
        r"① ⭐⭐ **因式分解 $2ax^{2}-\left(a+2\right)x+1=\left(2x-1\right)\left(ax-1\right)$**：" "\n"
        r"   验 $\left(2x-1\right)\left(ax-1\right)=2ax^{2}-2x-ax+1=2ax^{2}-\left(a+2\right)x+1$ ✓" "\n"
        r"   这一步是本题的题眼，两个驻点一眼可见。" "\n"
        r"② ⚠ **（1）中驻点 $\frac12$ 不在 $\left[1,e\right]$ 内**：分类时只需比较 $\frac1a$ 与 $1$、$e$，" "\n"
        r"   若把 $\frac12$ 也纳入讨论会多出无用的类别。" "\n"
        r"③ ⭐ **（2）的翻译**：「对任意 $x_{1}<x_{2}$ 有 $f\left(x_{1}\right)+2x_{1}<f\left(x_{2}\right)+2x_{2}$」" "\n"
        r"   ⟺ $g\left(x\right)=f\left(x\right)+2x$ 严格递增 ⟺ $g'\left(x\right)\ge0$（且不恒为零）。" "\n"
        r"④ ⭐⭐ **$\varphi\left(x\right)$ 过定点 $\left(0,1\right)$ 且对称轴 $x=\frac14$ 与 $a$ 无关** —— " "\n"
        r"   对称轴固定是能用判别式的理由（最小值点不会跑出 $x>0$ 的范围）。" "\n"
        r"⑤ 数值复核（1）：$a=1$ 时 $\left[1,e\right]$ 上最小值为 $-2.000000$ ✓；" "\n"
        r"   $a=0.5$ 时最小值为 $-2.3069<-2$ ✗；$a=0.8$ 时最小值为 $-2.0269<-2$ ✗；" "\n"
        r"   $a=1.5,2,3$ 时均为 $-2.000000$ ✓（因 $f\left(1\right)\equiv-2$ 与 $a$ 无关）" "\n"
        r"⑥ 数值复核（2）：$a=0$ 时 $\varphi\equiv1$ ✓；$a=8$ 时 $\varphi\left(x\right)=16x^{2}-8x+1=\left(4x-1\right)^{2}\ge0$，" "\n"
        r"   最小值恰为 $0$ ✓（边界）；$a=8.5$ 时最小值为 $-0.0625<0$ ✗；$a=9$ 时 $-0.125<0$ ✗" "\n"
        r"**通法（单调性型求参）**：" "\n"
        r"① 把「$x_{1}<x_{2}\implies\cdots$」翻译成 $g\left(x\right)$ 单调；" "\n"
        r"② $g'\left(x\right)\ge0$ 通分后得到分子二次函数，" "\n"
        r"③ 按「开口方向 + 判别式 + 对称轴位置」三要素讨论（本题对称轴固定，只需前两条）。"
    ),
    'difficulty': 0.66,
    'topics': ['M-T-151'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-151-V1',
}

T151_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f\left(x\right)=\left(x-1\right)e^{x}-\dfrac t2x^{2}$，其中 $t\in\mathbf R$．" "\n"
        r"（1）讨论函数 $f\left(x\right)$ 的单调性；" "\n"
        r"（2）当 $t=3$ 时，证明：不等式 $f\left(x_{1}+x_{2}\right)-f\left(x_{1}-x_{2}\right)>-2x_{2}$ 恒成立"
        r"（其中 $x_{1}\in\mathbf R$，$x_{2}>0$）．"
    ),
    'stem': [
        r"已知函数 $f\left(x\right)=\left(x-1\right)e^{x}-\dfrac t2x^{2}$，其中 $t\in\mathbf R$．",
        r"（1）讨论函数 $f\left(x\right)$ 的单调性；",
        r"（2）当 $t=3$ 时，证明：不等式 $f\left(x_{1}+x_{2}\right)-f\left(x_{1}-x_{2}\right)>-2x_{2}$ 恒成立（其中 $x_{1}\in\mathbf R$，$x_{2}>0$）．",
    ],
    'opts': [],
    'answer': r"（1）见解析；（2）证明见解析",
    'analysis': (
        r"（1）$f'\left(x\right)=xe^{x}-tx=x\left(e^{x}-t\right)$，两个零点是 $x=0$ 与 $x=\ln t$（后者仅 $t>0$ 时存在），"
        r"按 $t\le0$、$0<t<1$、$t=1$、$t>1$ 四类讨论 $\ln t$ 与 $0$ 的大小。"
        r"（2）移项成 $f\left(x_{1}+x_{2}\right)+\left(x_{1}+x_{2}\right)>f\left(x_{1}-x_{2}\right)+\left(x_{1}-x_{2}\right)$，" "\n"
        r"即证 $g\left(x\right)=f\left(x\right)+x$ 单调递增，再用 $e^{x}\ge x+1$ 证 $g'\left(x\right)\ge0$。"
    ),
    'solution': (
        r"（1）$f\left(x\right)$ 的定义域为 $\mathbf R$，且" "\n"
        r"$$f'\left(x\right)=e^{x}+\left(x-1\right)e^{x}-tx=xe^{x}-tx=x\left(e^{x}-t\right).$$" "\n"
        r"① 当 $t\le0$ 时，$e^{x}-t>0$ 恒成立，故 $f'\left(x\right)$ 与 $x$ 同号：" "\n"
        r"　 $f\left(x\right)$ 在 $\left(-\infty,0\right)$ 上单调递减，在 $\left(0,+\infty\right)$ 上单调递增；" "\n"
        r"② 当 $0<t<1$ 时，$\ln t<0$，$f'\left(x\right)=0$ 的两根为 $x=\ln t$ 与 $x=0$（$\ln t<0$）：" "\n"
        r"　 $x<\ln t$ 时 $x<0$、$e^{x}-t<0$，$f'>0$；$\ln t<x<0$ 时 $x<0$、$e^{x}-t>0$，$f'<0$；" "\n"
        r"　 $x>0$ 时 $x>0$、$e^{x}-t>0$，$f'>0$。" "\n"
        r"　 故 $f\left(x\right)$ 在 $\left(-\infty,\ln t\right)$、$\left(0,+\infty\right)$ 上单调递增，在 $\left(\ln t,0\right)$ 上单调递减；" "\n"
        r"③ 当 $t=1$ 时，$\ln t=0$，$f'\left(x\right)=x\left(e^{x}-1\right)\ge0$ 恒成立（$x>0$ 时两项同正，$x<0$ 时两项同负），" "\n"
        r"　 故 $f\left(x\right)$ 在 $\mathbf R$ 上单调递增；" "\n"
        r"④ 当 $t>1$ 时，$\ln t>0$：" "\n"
        r"　 $x<0$ 时 $x<0$、$e^{x}-t<0$（因 $x<0<\ln t$），$f'>0$；" "\n"
        r"　 $0<x<\ln t$ 时 $x>0$、$e^{x}-t<0$，$f'<0$；$x>\ln t$ 时两项同正，$f'>0$。" "\n"
        r"　 故 $f\left(x\right)$ 在 $\left(-\infty,0\right)$、$\left(\ln t,+\infty\right)$ 上单调递增，在 $\left(0,\ln t\right)$ 上单调递减。" "\n"
        r"（2）当 $t=3$ 时，$f\left(x\right)=\left(x-1\right)e^{x}-\dfrac32x^{2}$。所证不等式可改写为" "\n"
        r"$$f\left(x_{1}+x_{2}\right)+\left(x_{1}+x_{2}\right)>f\left(x_{1}-x_{2}\right)+\left(x_{1}-x_{2}\right).$$" "\n"
        r"（因右端 $-2x_{2}=\left(x_{1}-x_{2}\right)-\left(x_{1}+x_{2}\right)$。）" "\n"
        r"设 $g\left(x\right)=f\left(x\right)+x=\left(x-1\right)e^{x}-\dfrac32x^{2}+x$，" "\n"
        r"则上式即 $g\left(x_{1}+x_{2}\right)>g\left(x_{1}-x_{2}\right)$。由 $x_{2}>0$ 知 $x_{1}+x_{2}>x_{1}-x_{2}$，" "\n"
        r"故只需证 $g\left(x\right)$ 在 $\mathbf R$ 上单调递增，即证 $g'\left(x\right)\ge0$。" "\n"
        r"$$g'\left(x\right)=xe^{x}-3x+1.$$" "\n"
        r"当 $x\ge0$ 时，由 $e^{x}\ge x+1$ 得 $xe^{x}\ge x\left(x+1\right)=x^{2}+x$，于是" "\n"
        r"$$g'\left(x\right)\ge x^{2}+x-3x+1=x^{2}-2x+1=\left(x-1\right)^{2}\ge0.$$" "\n"
        r"当 $x<0$ 时，$e^{x}<1$，故 $e^{x}-3<-2<0$，又 $x<0$，得 $x\left(e^{x}-3\right)>0$，" "\n"
        r"于是 $g'\left(x\right)=x\left(e^{x}-3\right)+1>1>0$。" "\n"
        r"综上，$g'\left(x\right)\ge0$ 在 $\mathbf R$ 上恒成立，故 $g\left(x\right)$ 单调递增，原不等式成立。"
    ),
    'review': (
        r"① ⭐⭐ **$f'\left(x\right)=x\left(e^{x}-t\right)$ 的分解**：$x$ 与 $e^{x}-t$ 各自的零点分别是 $0$ 与 $\ln t$，" "\n"
        r"   分类的本质是比较这两个零点的大小（以及 $\ln t$ 是否存在）。" "\n"
        r"② ⚠ **$t\le0$ 时 $\ln t$ 不存在**，不能写「$\ln t<0$」——必须单独作为第一类。" "\n"
        r"③ ⭐ **$t=1$ 时 $f'=x\left(e^{x}-1\right)\ge0$ 恒成立**：$x>0$ 时 $e^{x}>1$，$x<0$ 时 $e^{x}<1$，" "\n"
        r"   两者同号，这是「退化为单调」的情形，易漏。" "\n"
        r"④ ⭐⭐ **（2）的移项技巧**：把 $-2x_{2}$ 拆成 $\left(x_{1}-x_{2}\right)-\left(x_{1}+x_{2}\right)$，" "\n"
        r"   于是两端结构完全相同，只剩一个函数 $g$ 在两个点的值 —— 这就是「结构相同」型构造。" "\n"
        r"⑤ ⚠ **原书详解中 $g\left(x\right)$ 写作 $\left(x-1\right)e^{x}-x^{2}+x$（漏了系数 $\frac32$）**：" "\n"
        r"   若按 $-x^{2}$，则 $g'=xe^{x}-2x+1$，与详解随后写的 $xe^{x}-3x+1$ 矛盾。" "\n"
        r"   由 $g'=xe^{x}-3x+1$ 反推可知 $g\left(x\right)=\left(x-1\right)e^{x}-\frac32x^{2}+x$ ✓" "\n"
        r"⑥ ⭐ **$x<0$ 时的放缩方向**：$e^{x}<1$ ⟹ $e^{x}-3<-2$，乘负数 $x$ 后变正，" "\n"
        r"   这一步符号最容易搞反。" "\n"
        r"⑦ 数值复核：$g'\left(-3\right)=9.8506>0$、$g'\left(-1\right)=3.6321>0$、$g'\left(-0.5\right)=2.1967>0$、" "\n"
        r"   $g'\left(0\right)=1>0$、$g'\left(0.5\right)=0.3244>0$、$g'\left(1\right)=0.7183>0$、$g'\left(2\right)=9.7781>0$ ✓" "\n"
        r"   注意 $x=1$ 时下界 $\left(x-1\right)^{2}=0$，而实际 $g'\left(1\right)=0.7183>0$，放缩是松的但足够用。" "\n"
        r"**通法（结构相同型构造）**：" "\n"
        r"① 把不等式移项，使两端成为「同一函数在不同点的值」；" "\n"
        r"② 比较两点的大小（本题 $x_{1}+x_{2}>x_{1}-x_{2}$ 由 $x_{2}>0$ 保证）；" "\n"
        r"③ 转化为证明该函数的单调性，即证其导数 $\ge0$；" "\n"
        r"④ 证 $xe^{x}-3x+1\ge0$ 这类式子时，$x\ge0$ 用 $e^{x}\ge x+1$，$x<0$ 用 $e^{x}<1$ 分段。"
    ),
    'difficulty': 0.74,
    'topics': ['M-T-151'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-151-V2',
}

# ==========================================================================
#  M-T-159  导数压轴：单调性 / 零点 / 双变量
# ==========================================================================

T159_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f\left(x\right)=ax-1-\ln x$（$a\in\mathbf R$）．" "\n"
        r"（1）讨论函数 $f\left(x\right)$ 的单调性；" "\n"
        r"（2）讨论函数 $f\left(x\right)$ 的零点个数；" "\n"
        r"（3）当 $x>y>e-1$ 时，证明不等式 $e^{x}\ln\left(1+y\right)>e^{y}\ln\left(1+x\right)$．"
    ),
    'stem': [
        r"已知函数 $f\left(x\right)=ax-1-\ln x$（$a\in\mathbf R$）．",
        r"（1）讨论函数 $f\left(x\right)$ 的单调性；",
        r"（2）讨论函数 $f\left(x\right)$ 的零点个数；",
        r"（3）当 $x>y>e-1$ 时，证明不等式 $e^{x}\ln\left(1+y\right)>e^{y}\ln\left(1+x\right)$．",
    ],
    'opts': [],
    'answer': (
        r"（1）$a\le0$ 时在 $\left(0,+\infty\right)$ 上单调递减；$a>0$ 时在 $\left(0,\dfrac1a\right)$ 上单调递减、在 $\left(\dfrac1a,+\infty\right)$ 上单调递增；" "\n"
        r"（2）$0<a<1$ 时 $2$ 个零点，$a>1$ 时无零点，$a=1$ 或 $a\le0$ 时 $1$ 个零点；（3）证明见解析"
    ),
    'analysis': (
        r"（1）$f'\left(x\right)=\dfrac{ax-1}x$，按 $a\le0$ 与 $a>0$ 分类。"
        r"（2）$a>0$ 时最小值为 $f\left(\dfrac1a\right)=\ln a$，由 $\ln a$ 的符号定零点个数；"
        r"$a\le0$ 时 $f$ 递减且两端趋于异号无穷，必有唯一零点。"
        r"（3）等价于 $\dfrac{e^{x}}{\ln\left(1+x\right)}>\dfrac{e^{y}}{\ln\left(1+y\right)}$，即证 $F\left(t\right)=\dfrac{e^{t}}{\ln\left(1+t\right)}$ 在 $\left(e-1,+\infty\right)$ 上递增。"
    ),
    'solution': (
        r"（1）$f\left(x\right)$ 的定义域为 $\left(0,+\infty\right)$，$f'\left(x\right)=a-\dfrac1x=\dfrac{ax-1}x$。" "\n"
        r"① 当 $a\le0$ 时，$ax-1<0$ 恒成立，故 $f'\left(x\right)<0$，$f\left(x\right)$ 在 $\left(0,+\infty\right)$ 上单调递减；" "\n"
        r"② 当 $a>0$ 时，令 $f'\left(x\right)=0$ 得 $x=\dfrac1a$：" "\n"
        r"　 $0<x<\dfrac1a$ 时 $f'\left(x\right)<0$，$f\left(x\right)$ 单调递减；" "\n"
        r"　 $x>\dfrac1a$ 时 $f'\left(x\right)>0$，$f\left(x\right)$ 单调递增。" "\n"
        r"（2）① 当 $a\le0$ 时，$f\left(x\right)$ 在 $\left(0,+\infty\right)$ 上单调递减，" "\n"
        r"　 且 $x\to0^{+}$ 时 $f\left(x\right)\to+\infty$（因 $-\ln x\to+\infty$），" "\n"
        r"　 $x\to+\infty$ 时 $f\left(x\right)\to-\infty$，故 $f\left(x\right)$ 有且只有 $1$ 个零点；" "\n"
        r"② 当 $a>0$ 时，由（1）知 $f\left(x\right)$ 的最小值为" "\n"
        r"$$f\left(\frac1a\right)=a\cdot\frac1a-1-\ln\frac1a=1-1+\ln a=\ln a.$$" "\n"
        r"　 （ⅰ）若 $\ln a>0$ 即 $a>1$，则最小值 $>0$，$f\left(x\right)$ 无零点；" "\n"
        r"　 （ⅱ）若 $\ln a=0$ 即 $a=1$，则最小值为 $0$，$f\left(x\right)$ 有且只有 $1$ 个零点（在 $x=1$ 处）；" "\n"
        r"　 （ⅲ）若 $\ln a<0$ 即 $0<a<1$，则最小值 $<0$，又 $x\to0^{+}$ 与 $x\to+\infty$ 时均有 $f\left(x\right)\to+\infty$，" "\n"
        r"　　　 故 $f\left(x\right)$ 有 $2$ 个零点。" "\n"
        r"综上：$0<a<1$ 时 $2$ 个零点，$a>1$ 时无零点，$a=1$ 或 $a\le0$ 时 $1$ 个零点。" "\n"
        r"（3）当 $x>y>e-1$ 时，$\ln\left(1+x\right)>0$、$\ln\left(1+y\right)>0$，" "\n"
        r"故所证不等式等价于 $\dfrac{e^{x}}{\ln\left(1+x\right)}>\dfrac{e^{y}}{\ln\left(1+y\right)}$。" "\n"
        r"设 $F\left(t\right)=\dfrac{e^{t}}{\ln\left(1+t\right)}$（$t>e-1$），则" "\n"
        r"$$F'\left(t\right)=\frac{e^{t}\ln\left(1+t\right)-e^{t}\cdot\dfrac1{1+t}}{\ln^{2}\left(1+t\right)}=\frac{e^{t}\left[\ln\left(1+t\right)-\dfrac1{1+t}\right]}{\ln^{2}\left(1+t\right)}.$$" "\n"
        r"设 $G\left(t\right)=\ln\left(1+t\right)-\dfrac1{1+t}$，则 $G'\left(t\right)=\dfrac1{1+t}+\dfrac1{\left(1+t\right)^{2}}>0$，" "\n"
        r"故 $G\left(t\right)$ 在 $\left(e-1,+\infty\right)$ 上单调递增，于是" "\n"
        r"$$G\left(t\right)>G\left(e-1\right)=\ln e-\frac1e=1-\frac1e>0.$$" "\n"
        r"又 $e^{t}>0$、$\ln^{2}\left(1+t\right)>0$，故 $F'\left(t\right)>0$，即 $F\left(t\right)$ 在 $\left(e-1,+\infty\right)$ 上单调递增。" "\n"
        r"由 $x>y>e-1$ 得 $F\left(x\right)>F\left(y\right)$，即所证不等式成立。"
    ),
    'review': (
        r"① ⭐⭐ **最小值 $f\left(\frac1a\right)=\ln a$ 是本题的枢纽**：" "\n"
        r"   $f\left(\frac1a\right)=a\cdot\frac1a-1-\ln\frac1a=1-1+\ln a=\ln a$，两项恰好抵消，只剩 $\ln a$。" "\n"
        r"   这种「化简后只剩一个 $\ln$」是命题人的刻意设计。" "\n"
        r"② ⭐ **$a\le0$ 时的两端极限**：$x\to0^{+}$ 时 $-\ln x\to+\infty$ 主导，" "\n"
        r"   $x\to+\infty$ 时 $ax$（$a<0$）或 $-\ln x$（$a=0$）主导，均趋于 $-\infty$ ⟹ 必穿过 $x$ 轴一次。" "\n"
        r"③ ⚠ **$a=1$ 与 $a\le0$ 的零点个数相同（都是 $1$）但成因不同**：" "\n"
        r"   前者是「最小值恰为 $0$」（相切），后者是「单调递减且两端异号」（穿过）。" "\n"
        r"④ ⭐⭐ **（3）的等价变形**：$e^{x}\ln\left(1+y\right)>e^{y}\ln\left(1+x\right)$ ⟺ $\dfrac{e^{x}}{\ln\left(1+x\right)}>\dfrac{e^{y}}{\ln\left(1+y\right)}$。" "\n"
        r"   判据：**把下标相同的量放到同一侧**，就能看出是同一个函数在两个点的取值。" "\n"
        r"⑤ ⭐ **$F'\left(t\right)$ 的分子用 $G\left(t\right)$ 单独处理**：" "\n"
        r"   $G\left(e-1\right)=1-\frac1e\approx0.6321>0$，且 $G$ 递增 ⟹ 分子恒正。" "\n"
        r"   区间左端取 $e-1$（而非 $0$）正是为了让 $\ln\left(1+t\right)$ 刚好大于 $1/e$。" "\n"
        r"⑥ 数值复核（2）：$a=2$ 时 $f_{\min}=f\left(0.5\right)=0.6931>0$（无零点）✓；" "\n"
        r"   $a=1$ 时 $f_{\min}=f\left(1\right)=0$（$1$ 个）✓；" "\n"
        r"   $a=0.5$ 时 $f_{\min}=f\left(2\right)=-0.6931<0$，且 $f\left(0.1\right)=1.3526>0$、$f\left(10\right)=1.697>0$（$2$ 个）✓；" "\n"
        r"   $a=0$ 时 $f\left(x\right)=-1-\ln x$，零点 $x=e^{-1}=0.3679$（$1$ 个）✓；" "\n"
        r"   $a=-1$ 时 $f\left(0.1\right)=1.2026>0$、$f\left(1\right)=-2<0$（$1$ 个）✓" "\n"
        r"⑦ 数值复核（3）：$x=3,y=2$ 时 $e^{3}\ln3=22.063>e^{2}\ln2=5.121$ ✓" "\n"
        r"**通法（双变量指数对数不等式）**：" "\n"
        r"① 把下标相同的量移到同一侧，凑成 $\dfrac{e^{x}}{\ln\left(1+x\right)}$ 这类单变量函数；" "\n"
        r"② 求导后分子若是「$\ln\left(1+t\right)-\dfrac1{1+t}$」型，单独设 $G\left(t\right)$ 证其为正；" "\n"
        r"③ 利用区间左端点（如 $e-1$）使 $G$ 的值恰好可算。"
    ),
    'difficulty': 0.71,
    'topics': ['M-T-159'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-159-E1',
}

T159_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f\left(x\right)=ax-1-\ln x$（$a\in\mathbf R$）．" "\n"
        r"（1）当 $a=2$ 时，求函数 $f\left(x\right)$ 的单调区间；" "\n"
        r"（2）若函数 $f\left(x\right)$ 在 $x=1$ 处取得极值，对任意 $x\in\left(0,+\infty\right)$，$f\left(x\right)\ge bx-2$ 恒成立，"
        r"求实数 $b$ 的取值范围；" "\n"
        r"（3）当 $x>y>e-1$ 时，求证：$e^{x-y}>\dfrac{\ln\left(x+1\right)}{\ln\left(y+1\right)}$．"
    ),
    'stem': [
        r"已知函数 $f\left(x\right)=ax-1-\ln x$（$a\in\mathbf R$）．",
        r"（1）当 $a=2$ 时，求函数 $f\left(x\right)$ 的单调区间；",
        r"（2）若函数 $f\left(x\right)$ 在 $x=1$ 处取得极值，对任意 $x\in\left(0,+\infty\right)$，$f\left(x\right)\ge bx-2$ 恒成立，求实数 $b$ 的取值范围；",
        r"（3）当 $x>y>e-1$ 时，求证：$e^{x-y}>\dfrac{\ln\left(x+1\right)}{\ln\left(y+1\right)}$．",
    ],
    'opts': [],
    'answer': (
        r"（1）在 $\left(0,\dfrac12\right)$ 上单调递减，在 $\left(\dfrac12,+\infty\right)$ 上单调递增；" "\n"
        r"（2）$b\le1-\dfrac1{e^{2}}$；（3）证明见解析"
    ),
    'analysis': (
        r"（1）$a=2$ 时 $f'\left(x\right)=\dfrac{2x-1}x$，驻点 $x=\dfrac12$。"
        r"（2）由 $f'\left(1\right)=0$ 得 $a=1$；$f\left(x\right)\ge bx-2$ 等价于 $\dfrac{f\left(x\right)+2}x\ge b$，"
        r"设 $g\left(x\right)=1+\dfrac{1-\ln x}x$，求其最小值。"
        r"（3）等价于 $e^{x}\ln\left(y+1\right)>e^{y}\ln\left(x+1\right)$，同 M-T-159-E1（3）。"
    ),
    'solution': (
        r"（1）当 $a=2$ 时，$f\left(x\right)=2x-1-\ln x$，定义域为 $\left(0,+\infty\right)$，" "\n"
        r"$$f'\left(x\right)=2-\frac1x=\frac{2x-1}x.$$" "\n"
        r"当 $0<x<\dfrac12$ 时 $f'\left(x\right)<0$，$f\left(x\right)$ 单调递减；" "\n"
        r"当 $x>\dfrac12$ 时 $f'\left(x\right)>0$，$f\left(x\right)$ 单调递增。" "\n"
        r"故单调递减区间为 $\left(0,\dfrac12\right)$，单调递增区间为 $\left(\dfrac12,+\infty\right)$。" "\n"
        r"（2）$f'\left(x\right)=a-\dfrac1x$，由 $f\left(x\right)$ 在 $x=1$ 处取得极值知 $f'\left(1\right)=a-1=0$，即 $a=1$。" "\n"
        r"此时 $f\left(x\right)=x-1-\ln x$。由 $x>0$，$f\left(x\right)\ge bx-2$ 等价于" "\n"
        r"$$\frac{f\left(x\right)+2}x\ge b,\quad\text{即}\quad\frac{x+1-\ln x}x=1+\frac{1-\ln x}x\ge b.$$" "\n"
        r"设 $g\left(x\right)=1+\dfrac{1-\ln x}x$（$x>0$），则" "\n"
        r"$$g'\left(x\right)=\frac{-\dfrac1x\cdot x-\left(1-\ln x\right)}{x^{2}}=\frac{-1-1+\ln x}{x^{2}}=\frac{\ln x-2}{x^{2}}.$$" "\n"
        r"当 $0<x<e^{2}$ 时 $g'\left(x\right)<0$，$g\left(x\right)$ 单调递减；当 $x>e^{2}$ 时 $g'\left(x\right)>0$，$g\left(x\right)$ 单调递增。" "\n"
        r"故 $g_{\min}=g\left(e^{2}\right)=1+\dfrac{1-\ln e^{2}}{e^{2}}=1+\dfrac{1-2}{e^{2}}=1-\dfrac1{e^{2}}$。" "\n"
        r"由 $b\le g\left(x\right)$ 恒成立得 $b\le g_{\min}=1-\dfrac1{e^{2}}$。" "\n"
        r"（3）所证不等式等价于 $e^{x}\ln\left(y+1\right)>e^{y}\ln\left(x+1\right)$，" "\n"
        r"即 $\dfrac{e^{x}}{\ln\left(x+1\right)}>\dfrac{e^{y}}{\ln\left(y+1\right)}$（因 $x>y>e-1$ 时两对数均为正）。" "\n"
        r"设 $F\left(t\right)=\dfrac{e^{t}}{\ln\left(t+1\right)}$（$t>e-1$），则" "\n"
        r"$$F'\left(t\right)=\frac{e^{t}\left[\ln\left(t+1\right)-\dfrac1{t+1}\right]}{\ln^{2}\left(t+1\right)}.$$" "\n"
        r"设 $G\left(t\right)=\ln\left(t+1\right)-\dfrac1{t+1}$，则 $G'\left(t\right)=\dfrac1{t+1}+\dfrac1{\left(t+1\right)^{2}}>0$，" "\n"
        r"故 $G\left(t\right)>G\left(e-1\right)=\ln e-\dfrac1e=1-\dfrac1e>0$，从而 $F'\left(t\right)>0$。" "\n"
        r"于是 $F\left(t\right)$ 在 $\left(e-1,+\infty\right)$ 上单调递增，由 $x>y>e-1$ 得 $F\left(x\right)>F\left(y\right)$，" "\n"
        r"即 $e^{x-y}>\dfrac{\ln\left(x+1\right)}{\ln\left(y+1\right)}$ 成立。"
    ),
    'review': (
        r"① ⭐⭐ **（2）的分离参数技巧**：$f\left(x\right)\ge bx-2$ ⟺ $f\left(x\right)+2\ge bx$ ⟺ $\dfrac{f\left(x\right)+2}x\ge b$（$x>0$）。" "\n"
        r"   判据：**参数 $b$ 是一次项系数 ⟹ 除以 $x>0$ 直接分离，无需讨论**。" "\n"
        r"② ⭐ **$g\left(x\right)=1+\dfrac{1-\ln x}x$ 的导数**：" "\n"
        r"   $\left(\dfrac{1-\ln x}x\right)'=\dfrac{-\frac1x\cdot x-\left(1-\ln x\right)}{x^{2}}=\dfrac{\ln x-2}{x^{2}}$，" "\n"
        r"   分子 $\ln x-2$ 的零点 $x=e^{2}$ 就是最小值点。" "\n"
        r"③ 数值复核：$g\left(1\right)=2$、$g\left(2\right)=1.1534$、$g\left(e\right)=1$、" "\n"
        r"   $g\left(e^{2}\right)=0.864665=1-\dfrac1{e^{2}}$ ✓（最小值）、$g\left(20\right)=0.9002>e^{-2}$ 修正值 ✓" "\n"
        r"   取等验证：$b=1-\frac1{e^{2}}$ 时，$x=e^{2}$ 处 $f\left(e^{2}\right)+2=e^{2}+1-2=6.3891$，$b\cdot e^{2}=0.8647\times7.3891=6.3891$，两端相等 ✓" "\n"
        r"④ ⭐ **（3）与 M-T-159-E1（3）是同一题的两种写法**：" "\n"
        r"   $e^{x-y}>\dfrac{\ln\left(x+1\right)}{\ln\left(y+1\right)}$ ⟺ $e^{x}\ln\left(y+1\right)>e^{y}\ln\left(x+1\right)$，" "\n"
        r"   两题可用完全相同的 $F\left(t\right)=\dfrac{e^{t}}{\ln\left(t+1\right)}$ 处理。" "\n"
        r"⑤ ⚠ **$a=1$ 的来历**：$f$ 在 $x=1$ 处取得极值 ⟹ $f'\left(1\right)=0$ ⟹ $a=1$。" "\n"
        r"   注意「取得极值」对可导函数即「导数为零」，不必再验证是否为极值点（题设已保证）。" "\n"
        r"**通法（一次项参数恒成立）**：" "\n"
        r"① 整理成 $A\left(x\right)\ge b\cdot x$ 的形式；" "\n"
        r"② 由 $x>0$ 除以 $x$ 分离出 $b\le\dfrac{A\left(x\right)}x$；" "\n"
        r"③ 对 $\dfrac{A\left(x\right)}x$ 求导（商的导数），用分子零点定最小值。"
    ),
    'difficulty': 0.70,
    'topics': ['M-T-159'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-159-V1',
}

T159_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f\left(x\right)=\left(ax-1\right)e^{x}$，$a\in\mathbf R$．" "\n"
        r"（1）讨论 $f\left(x\right)$ 的单调区间；" "\n"
        r"（2）当 $m>n>0$ 时，证明：$me^{n}+n<ne^{m}+m$．"
    ),
    'stem': [
        r"已知函数 $f\left(x\right)=\left(ax-1\right)e^{x}$，$a\in\mathbf R$．",
        r"（1）讨论 $f\left(x\right)$ 的单调区间；",
        r"（2）当 $m>n>0$ 时，证明：$me^{n}+n<ne^{m}+m$．",
    ],
    'opts': [],
    'answer': r"（1）见解析；（2）证明见解析",
    'analysis': (
        r"（1）$f'\left(x\right)=\left(ax+a-1\right)e^{x}$，由 $e^{x}>0$ 知符号取决于 $ax+a-1$，"
        r"按 $a=0$、$a>0$、$a<0$ 三类讨论（后两类的驻点为 $x=\dfrac1a-1$）。"
        r"（2）移项成 $m\left(e^{n}-1\right)<n\left(e^{m}-1\right)$，即 $\dfrac{e^{n}-1}n<\dfrac{e^{m}-1}m$，"
        r"转化为证 $h\left(x\right)=\dfrac{e^{x}-1}x$ 在 $\left(0,+\infty\right)$ 上递增。"
    ),
    'solution': (
        r"（1）$f\left(x\right)$ 的定义域为 $\mathbf R$，且" "\n"
        r"$$f'\left(x\right)=ae^{x}+\left(ax-1\right)e^{x}=\left(ax+a-1\right)e^{x}.$$" "\n"
        r"因 $e^{x}>0$，故 $f'\left(x\right)$ 的符号由 $u\left(x\right)=ax+a-1$ 决定。" "\n"
        r"① 当 $a=0$ 时，$u\left(x\right)\equiv-1<0$，$f'\left(x\right)<0$，$f\left(x\right)$ 在 $\mathbf R$ 上单调递减；" "\n"
        r"② 当 $a>0$ 时，$u\left(x\right)$ 单调递增，零点为 $x=\dfrac{1-a}a=\dfrac1a-1$：" "\n"
        r"　 $x<\dfrac1a-1$ 时 $f'\left(x\right)<0$，$f\left(x\right)$ 单调递减；" "\n"
        r"　 $x>\dfrac1a-1$ 时 $f'\left(x\right)>0$，$f\left(x\right)$ 单调递增；" "\n"
        r"③ 当 $a<0$ 时，$u\left(x\right)$ 单调递减，零点仍为 $x=\dfrac1a-1$：" "\n"
        r"　 $x<\dfrac1a-1$ 时 $u\left(x\right)>0$，$f'\left(x\right)>0$，$f\left(x\right)$ 单调递增；" "\n"
        r"　 $x>\dfrac1a-1$ 时 $u\left(x\right)<0$，$f'\left(x\right)<0$，$f\left(x\right)$ 单调递减。" "\n"
        r"（2）所证不等式 $me^{n}+n<ne^{m}+m$ 可移项化为" "\n"
        r"$$me^{n}-m<ne^{m}-n,\quad\text{即}\quad m\left(e^{n}-1\right)<n\left(e^{m}-1\right).$$" "\n"
        r"因 $m>0$、$n>0$，两边同除以 $mn$ 得 $\dfrac{e^{n}-1}n<\dfrac{e^{m}-1}m$。" "\n"
        r"设 $h\left(x\right)=\dfrac{e^{x}-1}x$（$x>0$），则" "\n"
        r"$$h'\left(x\right)=\frac{xe^{x}-\left(e^{x}-1\right)}{x^{2}}=\frac{e^{x}\left(x-1\right)+1}{x^{2}}.$$" "\n"
        r"设 $\varphi\left(x\right)=e^{x}\left(x-1\right)+1$，则 $\varphi'\left(x\right)=e^{x}\left(x-1\right)+e^{x}=xe^{x}>0$（$x>0$），" "\n"
        r"故 $\varphi\left(x\right)$ 在 $\left(0,+\infty\right)$ 上单调递增，于是 $\varphi\left(x\right)>\varphi\left(0\right)=e^{0}\left(-1\right)+1=0$。" "\n"
        r"从而 $h'\left(x\right)>0$，即 $h\left(x\right)$ 在 $\left(0,+\infty\right)$ 上单调递增。" "\n"
        r"由 $m>n>0$ 得 $h\left(m\right)>h\left(n\right)$，即 $\dfrac{e^{m}-1}m>\dfrac{e^{n}-1}n$，" "\n"
        r"故 $n\left(e^{m}-1\right)>m\left(e^{n}-1\right)$，即 $ne^{m}-n>me^{n}-m$，亦即 $me^{n}+n<ne^{m}+m$，得证。"
    ),
    'review': (
        r"① ⭐⭐ **（1）中 $a<0$ 与 $a>0$ 的单调性方向相反**：" "\n"
        r"   $a>0$ 时 $u\left(x\right)=ax+a-1$ 递增（先减后增），$a<0$ 时递减（先增后减）。" "\n"
        r"   两者的驻点都是 $x=\frac1a-1$，但单调区间顺序要交换。" "\n"
        r"② ⚠ **$a=0$ 时驻点不存在**：$\frac1a-1$ 无意义，必须单独作为第一类。" "\n"
        r"③ ⭐⭐ **（2）的移项是关键**：$me^{n}+n<ne^{m}+m$ 中常数 $m,n$ 与指数项混杂，" "\n"
        r"   把 $m$ 移到含 $e^{n}$ 的一侧、$n$ 移到含 $e^{m}$ 的一侧，就凑出 $m\left(e^{n}-1\right)<n\left(e^{m}-1\right)$。" "\n"
        r"   判据：**目标是让两侧成为「同一函数在不同点的值」**，即 $\dfrac{e^{n}-1}n$ 与 $\dfrac{e^{m}-1}m$。" "\n"
        r"④ ⭐ **$h'\left(x\right)$ 的分子 $\varphi\left(x\right)=e^{x}\left(x-1\right)+1$ 是经典结构**：" "\n"
        r"   $\varphi\left(0\right)=0$ 且 $\varphi'\left(x\right)=xe^{x}>0$（$x>0$），这是 $e^{x}\ge1+x$ 的等价形式（整理即得 $e^{x}\left(x-1\right)+1>0$ 对 $x\ne0$）。" "\n"
        r"⑤ 数值复核（2）：$m=2,n=1$ 时 $me^{n}+n=2e+1=6.4366$，$ne^{m}+m=e^{2}+2=9.3891$，$6.4366<9.3891$ ✓；" "\n"
        r"   $h\left(0.5\right)=1.2974<h\left(1\right)=1.7183<h\left(2\right)=3.1945<h\left(3\right)=6.3618$ ✓（$h$ 递增）" "\n"
        r"⑥ **本页原文在 $f'\left(x\right)=\left(ax+a-1\right)e^{x}$ 后即截断（跨页），（1）（2）的详解由我独立补完并数值验证。**" "\n"
        r"**通法（$m>n$ 型双变量不等式）**：" "\n"
        r"① 移项使两侧结构对称：$\cdots\left(e^{n}-1\right)<\cdots\left(e^{m}-1\right)$；" "\n"
        r"② 同除以两变量之积，化为 $\dfrac{e^{n}-1}n<\dfrac{e^{m}-1}m$；" "\n"
        r"③ 设 $h\left(x\right)=\dfrac{e^{x}-1}x$，用 $e^{x}\ge1+x$ 证其递增。"
    ),
    'difficulty': 0.73,
    'topics': ['M-T-159'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-159-V2',
}

# ==========================================================================
#  M-T-160  导数压轴：凹凸翻转型
# ==========================================================================

T160_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知 $f\left(x\right)=x\ln x$，$g\left(x\right)=-x^{2}+ax-3$．" "\n"
        r"（1）求函数 $f\left(x\right)$ 的单调区间；" "\n"
        r"（2）对一切 $x\in\left(0,+\infty\right)$，$2f\left(x\right)\ge g\left(x\right)$ 恒成立，求实数 $a$ 的取值范围；" "\n"
        r"（3）证明：对一切 $x\in\left(0,+\infty\right)$，都有 $\ln x>\dfrac1{e^{x}}-\dfrac2{ex}$．"
    ),
    'stem': [
        r"已知 $f\left(x\right)=x\ln x$，$g\left(x\right)=-x^{2}+ax-3$．",
        r"（1）求函数 $f\left(x\right)$ 的单调区间；",
        r"（2）对一切 $x\in\left(0,+\infty\right)$，$2f\left(x\right)\ge g\left(x\right)$ 恒成立，求实数 $a$ 的取值范围；",
        r"（3）证明：对一切 $x\in\left(0,+\infty\right)$，都有 $\ln x>\dfrac1{e^{x}}-\dfrac2{ex}$．",
    ],
    'opts': [],
    'answer': (
        r"（1）在 $\left(0,\dfrac1e\right)$ 上单调递减，在 $\left(\dfrac1e,+\infty\right)$ 上单调递增；" "\n"
        r"（2）$\left(-\infty,4\right]$；（3）证明见解析"
    ),
    'analysis': (
        r"（1）$f'\left(x\right)=\ln x+1$，驻点 $x=\dfrac1e$。"
        r"（2）分离参数得 $a\le2\ln x+x+\dfrac3x$，设 $h\left(x\right)$ 求最小值。"
        r"（3）两边同乘 $x>0$ 得 $x\ln x>\dfrac x{e^{x}}-\dfrac2e$，"
        r"即证 $f\left(x\right)>m\left(x\right)$；$f_{\min}=-\dfrac1e$ 在 $x=\dfrac1e$ 取到，$m_{\max}=-\dfrac1e$ 在 $x=1$ 取到，"
        r"两端极值相等但取等点不同，故严格大于成立。"
    ),
    'solution': (
        r"（1）$f\left(x\right)=x\ln x$ 的定义域为 $\left(0,+\infty\right)$，$f'\left(x\right)=\ln x+1$。" "\n"
        r"令 $f'\left(x\right)=0$ 得 $x=\dfrac1e$。" "\n"
        r"当 $0<x<\dfrac1e$ 时 $f'\left(x\right)<0$，$f\left(x\right)$ 单调递减；" "\n"
        r"当 $x>\dfrac1e$ 时 $f'\left(x\right)>0$，$f\left(x\right)$ 单调递增。" "\n"
        r"故单调递减区间为 $\left(0,\dfrac1e\right)$，单调递增区间为 $\left(\dfrac1e,+\infty\right)$。" "\n"
        r"（2）$2f\left(x\right)\ge g\left(x\right)$ 即 $2x\ln x\ge-x^{2}+ax-3$，整理得" "\n"
        r"$$a\le2\ln x+x+\frac3x.$$" "\n"
        r"设 $h\left(x\right)=2\ln x+x+\dfrac3x$（$x>0$），则" "\n"
        r"$$h'\left(x\right)=\frac2x+1-\frac3{x^{2}}=\frac{x^{2}+2x-3}{x^{2}}=\frac{\left(x+3\right)\left(x-1\right)}{x^{2}}.$$" "\n"
        r"当 $0<x<1$ 时 $h'\left(x\right)<0$，$h\left(x\right)$ 单调递减；当 $x>1$ 时 $h'\left(x\right)>0$，$h\left(x\right)$ 单调递增。" "\n"
        r"故 $h_{\min}=h\left(1\right)=0+1+3=4$。由 $a\le h\left(x\right)$ 恒成立得 $a\le4$，" "\n"
        r"即 $a\in\left(-\infty,4\right]$。" "\n"
        r"（3）因 $x>0$，所证不等式等价于 $x\ln x>\dfrac x{e^{x}}-\dfrac2e$，即 $f\left(x\right)>m\left(x\right)$，" "\n"
        r"其中 $m\left(x\right)=\dfrac x{e^{x}}-\dfrac2e$。" "\n"
        r"由（1）知 $f\left(x\right)$ 的最小值为 $f\left(\dfrac1e\right)=\dfrac1e\ln\dfrac1e=-\dfrac1e$，当且仅当 $x=\dfrac1e$ 时取到。" "\n"
        r"对 $m\left(x\right)$，$m'\left(x\right)=\dfrac{e^{x}-xe^{x}}{e^{2x}}=\dfrac{1-x}{e^{x}}$：" "\n"
        r"当 $0<x<1$ 时 $m'\left(x\right)>0$，$m\left(x\right)$ 单调递增；当 $x>1$ 时 $m'\left(x\right)<0$，$m\left(x\right)$ 单调递减。" "\n"
        r"故 $m\left(x\right)$ 的最大值为 $m\left(1\right)=\dfrac1e-\dfrac2e=-\dfrac1e$，当且仅当 $x=1$ 时取到。" "\n"
        r"于是对一切 $x>0$ 有 $f\left(x\right)\ge-\dfrac1e\ge m\left(x\right)$。" "\n"
        r"又 $f\left(x\right)=-\dfrac1e$ 仅当 $x=\dfrac1e$，$m\left(x\right)=-\dfrac1e$ 仅当 $x=1$，两者不可能同时取到，" "\n"
        r"故 $f\left(x\right)>m\left(x\right)$ 恒成立，即 $\ln x>\dfrac1{e^{x}}-\dfrac2{ex}$ 成立。"
    ),
    'review': (
        r"① ⭐⭐ **（3）是「凹凸翻转型」的典范**：$f$ 的最小值与 $m$ 的最大值恰好都是 $-\dfrac1e$，" "\n"
        r"   但取等点分别是 $x=\dfrac1e$ 与 $x=1$ —— **「极值相等 + 取等点不同」是严格不等号的唯一来源**。" "\n"
        r"   判据：凡是要证 $A>B$ 而 $\min A=\max B$ 的，都必须说明两个最值点不同。" "\n"
        r"② ⭐ **两边同乘 $x$ 的目的**：把 $\ln x$ 变成 $x\ln x$，即（1）中已研究过的 $f\left(x\right)$，" "\n"
        r"   这就是「用前一问的结论」的典型用法。" "\n"
        r"③ ⭐ **$h'\left(x\right)=\dfrac{\left(x+3\right)\left(x-1\right)}{x^{2}}$ 的分解**：" "\n"
        r"   分子 $x^{2}+2x-3=\left(x+3\right)\left(x-1\right)$，正根 $x=1$ 是最小值点（$x+3>0$ 恒成立）。" "\n"
        r"④ ⭐ **$m'\left(x\right)=\dfrac{1-x}{e^{x}}$**：" "\n"
        r"   $\left(\dfrac x{e^{x}}\right)'=\dfrac{e^{x}-xe^{x}}{e^{2x}}=\dfrac{1-x}{e^{x}}$，最大值在 $x=1$ 处。" "\n"
        r"⑤ 数值复核（2）：$h\left(1\right)=4$ ✓（最小值）；$h\left(0.5\right)=5.1137$、$h\left(2\right)=4.8863$、$h\left(3\right)=6.1972$ 均 $>4$ ✓" "\n"
        r"   取等验证：$a=4$ 时，$x=1$ 处 $2f\left(1\right)=0=g\left(1\right)=-1+4-3=0$ ✓" "\n"
        r"⑥ 数值复核（3）：$x=\dfrac1e$ 时 $f=-0.367879$、$m=-0.481113$，$f-m=0.113233>0$ ✓；" "\n"
        r"   $x=1$ 时 $f=0$、$m=-0.367879$，$f-m=0.367879>0$ ✓；" "\n"
        r"   $x=0.2$ 时 $f-m=0.250125>0$；$x=2$ 时 $f-m=1.851383>0$；$x=3$ 时 $f-m=3.882235>0$ ✓" "\n"
        r"**通法（凹凸翻转型）**：" "\n"
        r"① 把待证式两边同乘（或同除）一个正量，使两边变成已研究过的函数；" "\n"
        r"② 分别求左端的最小值与右端的最大值；" "\n"
        r"③ 若两者相等，必须指出取等点不同，才能得出严格不等号。"
    ),
    'difficulty': 0.69,
    'topics': ['M-T-160'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-160-E1',
}

QS = [
    T117_V2, T117_V3,
    T146_V1, T146_V2,
    T151_V1, T151_V2,
    T159_E1, T159_V1, T159_V2,
    T160_E1,
]
