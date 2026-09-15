# -*- coding: utf-8 -*-
r"""第 132 批（补录批·一）：从 50 道待录题里先攻「我能独立裁定」的 6 题。  python3 tools/run_batch.py 132  ## 选题依据  结项后剩余 50 题（65 条跳过登记 - 15 条重复）。本批不按页码贪心，而按 **「能否可靠裁定」** 筛选：题干与详解在原件中可完整读出、且我能独立推导出答案的题。  本批 6 题中，**4 题答案与原书一致**（补录即可），**2 题经推导发现原书答案有误** （M-T-181-E1、M-T-190-V1），作为 A 类勘误录入。  ## ★★ 两处 A 类勘误（原书答案错误）  ### 1. M-T-181-E1：原书答案 B($-1$) 错，正确为 C($-2$)  $f(x)=\dfrac{\sin x-1}{3-2\cos x-2\sin x}$。分母 $=(1-\sin x)^2+(1-\cos x)^2$， 分子 $=-(1-\sin x)$，故 $f=-\dfrac{u}{u^2+v^2}$（$u=1-\sin x,\ v=1-\cos x$）。  求导令分子为零得 $2-\cos x-2\sin x=0$，即 $\cos x+2\sin x=2$，配合 $\sin^2x+\cos^2x=1$ 得 $5\sin^2x-8\sin x+3=0$ ⟹ $\sin x=1$（此时 $f=0$，非最小）或 $\sin x=\dfrac35$。  $\sin x=\dfrac35,\ \cos x=\dfrac45$ 时 $u=\dfrac25,\ v=\dfrac15,\ u^2+v^2=\dfrac15$， $f=-\dfrac{2/5}{1/5}=\mathbf{-2}$。数值扫描（$2\times10^6$ 点）最小值 $=-2.0000000$ ✓  > **原书错在哪**：详解令 $g=\dfrac{1-\cos x}{1-\sin x}$ 后写 $f=-\dfrac1{1+g^2}$， > 正确应为 $f=-\dfrac1{(1-\sin x)(1+g^2)}$ —— **丢了因子 $(1-\sin x)$**。 > 在 $x=0$（即 $u=1$）处两者碰巧都等于 $-1$，详解便误判那是最小值。  ### 2. M-T-190-V1：原书答案 A 错，正确为 B  由射影定理 $c\cos B+b\cos C=a$，条件化为 $\sin B\cdot\dfrac a{bc}=\dfrac ac$ ⟹ $\dfrac{\sin B}b=1$ ⟹ $b=\sin B=\dfrac{\sqrt3}2$，且 $2R=1$。  $a+c=\sin A+\sin\left(\dfrac{2\pi}3-A\right)=\sqrt3\sin\left(A+\dfrac\pi6\right)$， $A\in\left(0,\dfrac{2\pi}3\right)$ ⟹ $a+c\in\left(\dfrac{\sqrt3}2,\sqrt3\right]$。  > **硬判据**：$A=\dfrac\pi3$（等边）时条件成立、$a+c=\sqrt3$ **精确取到**， > 右端必闭。原书标 A（两端开）错误。 """

T073_E1 = {
    'type': '填空',
    'stem_text': (
        r"已知函数 $f(x)=\begin{cases}\dfrac a{x-1},&x\le0,\\[2mm]\lg x,&x>0,\end{cases}$"
        r"若关于 $x$ 的方程 $f[f(x)]=0$ 仅有一解，则实数 $a$ 的取值范围是 ____"
    ),
    'answer': r"$(-1,0)\cup(0,+\infty)$",
    'analysis': (
        r"先排除 $a=0$（此时 $x\le0$ 上 $f(x)\equiv0$，方程有无数解）。"
        r"由 $f[f(x)]=0$ 得 $\lg f(x)=0$ 即 $f(x)=1$（$\dfrac a{f(x)-1}=0$ 因 $a\ne0$ 无解）；"
        r"再由 $f(x)=1$ 得 $x=10$ 或 $x=a+1$（后者需 $x\le0$）。"
        r"$x=10$ 恒为一解，故须 $x=a+1$ 不是解，即 $a+1>0$。"
    ),
    'solution': (
        r"若 $a=0$，则当 $x\le0$ 时 $f(x)=\dfrac0{x-1}=0$，于是 $f[f(x)]=f(0)=\dfrac a{-1}=0$"
        r"对一切 $x\le0$ 成立，方程有无数个解，不合题意，故 $a\ne0$。" "\n"
        r"由 $f[f(x)]=0$，对外层 $f$ 而言：$f(u)=0$ 意味着 $\lg u=0$（$u>0$）或"
        r"$\dfrac a{u-1}=0$（$u\le0$）。因 $a\ne0$，后者无解，故只能 $\lg u=0$，即 $u=1$，"
        r"亦即 $f(x)=1$。" "\n"
        r"解 $f(x)=1$：" "\n"
        r"① 当 $x>0$ 时 $\lg x=1$，得 $x=10$，这**恒为一个解**；" "\n"
        r"② 当 $x\le0$ 时 $\dfrac a{x-1}=1$，得 $x=a+1$，它成为解的条件是 $a+1\le0$，即 $a\le-1$。" "\n"
        r"要使方程**仅有一解**，必须让 ② 不产生新解，故 $a+1>0$，即 $a>-1$。" "\n"
        r"结合 $a\ne0$，得 $a$ 的取值范围是 $(-1,0)\cup(0,+\infty)$．"
    ),
    'review': (
        r"① ⭐⭐ **先查 $a=0$ 是否退化**：$a=0$ 时内层恒为 $0$，方程有无数解，这是本题第一个坎。" "\n"
        r"② ⭐⭐ **$f(u)=0$ 要分两段看，且 $\dfrac a{u-1}=0$ 因 $a\ne0$ 直接无解** ——"
        r"不少同学会误以为 $u=1$ 是它的解，从而把结论算错。" "\n"
        r"③ ⭐ **$\lg x=1$ 给的是常数解 $x=10$**，它不受 $a$ 影响，所以「仅有一解」等价于"
        r"另一支无解，而不是去数总解数。" "\n"
        r"④ ⚠ **$x=a+1$ 必须落在 $x\le0$ 段才作数**：这是分段函数嵌套最易漏的定义域检验。" "\n"
        r"⑤ 自检：取 $a=-\dfrac12\in(-1,0)$，则 $x=a+1=\dfrac12>0$ 不在该段，只有 $x=10$ 一解 ✓；"
        r"取 $a=-2<-1$，则 $x=a+1=-1\le0$ 是第二解，共两解 ✗。" "\n"
        r"**通法（嵌套方程 $f[f(x)]=0$）**：① 先排使内层退化的参数值；② 由外层解出 $f(x)$ 的目标值；"
        r"③ 逐段解并**逐段检验定义域**；④ 用「恒有解 + 无新增解」定参数范围。"
    ),
    'difficulty': 0.6,
    'topics': ['M-T-073'],
    'kp1': '函数与导数',
    'kp2': '复合函数与嵌套函数零点',
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-073-E1',
}

T074_E1 = {
    'type': '填空',
    'stem_text': (
        r"已知函数 $f(x)=\begin{cases}-x^2+2x+1,&x\le2,\\[2mm]|\log_2(x-2)|,&x>2,\end{cases}$"
        r"则方程 $f\left(x+\dfrac1{4x}+1\right)=a$ 恰好有 $6$ 个不同的解，"
        r"则实数 $a$ 的取值范围是 ____"
    ),
    'answer': r"$(0,1]$",
    'analysis': (
        r"令 $t=x+\dfrac1{4x}+1$，则 $t\in(-\infty,0]\cup[2,+\infty)$，且 $t=0,2$ 各对应 $1$ 个 $x$、"
        r"其余 $t$ 各对应 $2$ 个 $x$。再数 $f(t)=a$ 在该 $t$ 范围内的解：$t\le0$ 段 $f$ 递增、值域 $(-\infty,1]$；"
        r"$t>2$ 段 $f(t)=|\log_2(t-2)|$，$a>0$ 时两解。按 $a$ 分类计数，$a\in(0,1]$ 时恰为 $6$ 个。"
    ),
    'solution': (
        r"令 $t=x+\dfrac1{4x}+1$（$x\ne0$），原方程化为 $f(t)=a$。" "\n"
        r"**第一步：求 $t$ 的范围及每个 $t$ 对应的 $x$ 个数。**" "\n"
        r"由基本不等式，$x>0$ 时 $x+\dfrac1{4x}\ge2\sqrt{\dfrac14}=1$（$x=\dfrac12$ 取等）；"
        r"$x<0$ 时 $x+\dfrac1{4x}\le-1$（$x=-\dfrac12$ 取等）。故 $t\in(-\infty,0]\cup[2,+\infty)$。" "\n"
        r"由 $x+\dfrac1{4x}=t-1$ 得 $4x^2-4(t-1)x+1=0$，"
        r"$\Delta=16(t-1)^2-16=16t(t-2)$。所以 $t=0$ 或 $t=2$ 时 $\Delta=0$，各对应 $1$ 个 $x$；"
        r"$t<0$ 或 $t>2$ 时 $\Delta>0$，各对应 $2$ 个 $x$。" "\n"
        r"**第二步：数 $f(t)=a$ 的解。**" "\n"
        r"当 $t\le0$ 时 $f(t)=-(t-1)^2+2$，对称轴 $t=1$，故在 $t\le0$ 上**单调递增**， 值域为 $(-\infty,f(0)]=(-\infty,1]$。于是 $a\le1$ 时恰有 $1$ 个 $t$（$a=1$ 时 $t=0$；$a<1$ 时 $t<0$）。" "\n"
        r"当 $t=2$ 时 $f(2)=-4+4+1=1$（用第一段）。" "\n"
        r"当 $t>2$ 时 $f(t)=|\log_2(t-2)|$，令其等于 $a$：$a>0$ 时 $t=2+2^a$ 与 $t=2+2^{-a}$ 两个解；"
        r"$a=0$ 时只有 $t=3$ 一个解；$a<0$ 时无解。" "\n"
        r"**第三步：按 $a$ 分类计数。**" "\n"
        r"$\bullet\ a>1$：$t\le0$ 段无解，$t>2$ 段两个 $t$ 各给 $2$ 个 $x$，共 $4$ 个；" "\n"
        r"$\bullet\ a=1$：$t=0$ 给 $1$ 个 $x$，$t=2$ 给 $1$ 个 $x$，$t=4$ 与 $t=\dfrac52$ 各给 $2$ 个 $x$，共 $1+1+2+2=\mathbf6$ 个 ✓；" "\n"
        r"$\bullet\ 0<a<1$：$t\le0$ 段一个 $t<0$ 给 $2$ 个 $x$，$t>2$ 段两个 $t$ 各给 $2$ 个 $x$，共 $2+2+2=\mathbf6$ 个 ✓；" "\n"
        r"$\bullet\ a=0$：$t\le0$ 段 $t=1-\sqrt2$ 给 $2$ 个 $x$，$t=3$ 给 $2$ 个 $x$，共 $4$ 个；" "\n"
        r"$\bullet\ a<0$：$t\le0$ 段给 $2$ 个 $x$，$t>2$ 段无解，共 $2$ 个。" "\n"
        r"综上，$a$ 的取值范围是 $(0,1]$．"
    ),
    'review': (
        r"① ⭐⭐ **换元 $t=x+\dfrac1{4x}+1$ 后，$t$ 的范围是两段而非一段**："
        r"$x>0$ 给 $t\ge2$、$x<0$ 给 $t\le0$，中间的 $(0,2)$ 是空隙，这决定了后面必须分段数解。" "\n"
        r"② ⭐⭐ **每个 $t$ 对应几个 $x$ 由判别式定**：$\Delta=16t(t-2)$，"
        r"所以 $t=0,2$ 是「单根」只给 $1$ 个 $x$，其余给 $2$ 个 $x$ —— **端点必须单独数**，"
        r"这正是 $a=1$ 能凑出 $6$ 个解的关键。" "\n"
        r"③ ⭐ **$f(t)$ 在 $t\le0$ 上单调（因对称轴 $t=1$ 在右侧）**，故该段至多一个 $t$，不必解方程。" "\n"
        r"④ ⭐ **$|\log_2(t-2)|=a$ 的解数**：$a>0$ 两个、$a=0$ 一个、$a<0$ 无 —— 绝对值型对数方程的标准结论。" "\n"
        r"⑤ ⚠ **$t=2$ 处要用第一段算**：$f(2)=-4+4+1=1$，而不能用 $|\log_2 0|$。" "\n"
        r"⑥ 数值复核：$a=1$ 时解为 $x=-\dfrac12$、$x=\dfrac12$、以及 $t=4$ 与 $t=\dfrac52$ 对应的各 $2$ 个根，"
        r"共 $6$ 个 ✓；$a=0.5$ 时共 $6$ 个 ✓；$a=0$ 时共 $4$ 个 ✓。" "\n"
        r"**通法（$f(g(x))=a$ 型解数）**：① 换元 $t=g(x)$ 求值域，并标出 $t$ 与 $x$ 的对应个数；"
        r"② 在 $t$ 的值域内数 $f(t)=a$ 的解；③ 按 $a$ 分段，把「$t$ 的个数 × 每个 $t$ 的 $x$ 个数」加总；"
        r"④ 端点（$\Delta=0$、$f$ 的分段点、极值点）单独讨论。"
    ),
    'difficulty': 0.72,
    'topics': ['M-T-074'],
    'kp1': '函数与导数',
    'kp2': '复合函数与嵌套函数零点',
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-074-E1',
}

T093_V1 = {
    'type': '选择',
    'stem_text': (
        r"若 $x_1,x_2\in\mathbf R$，则 $(x_1-\mathrm e^{x_2})^2+(x_2-\mathrm e^{x_1})^2$ 的最小值是（　　）"
    ),
    'opts': [('A', r'$1$'), ('B', r'$2$'), ('C', r'$3$'), ('D', r'$4$')],
    'answer': r"B",
    'analysis': (
        r"原式是 $y=\mathrm e^x$ 上点 $A(x_1,\mathrm e^{x_1})$ 与 $y=\ln x$ 上点 $B(\mathrm e^{x_2},x_2)$ "
        r"距离的平方。两曲线关于 $y=x$ 对称，故最短距离 $=2\times$（$y=\mathrm e^x$ 上的点到直线 $y=x$ 的最短距离）。"
        r"与 $y=x$ 平行的切点由 $\mathrm e^{x_0}=1$ 得 $x_0=0$，切点 $(0,1)$ 到 $y=x$ 的距离为 $\dfrac1{\sqrt2}$，"
        r"故最小距离 $\sqrt2$，其平方为 $2$．"
    ),
    'solution': (
        r"记 $A(x_1,\mathrm e^{x_1})$、$B(\mathrm e^{x_2},x_2)$，则" "\n"
        r"$(x_1-\mathrm e^{x_2})^2+(x_2-\mathrm e^{x_1})^2=|AB|^2$。" "\n"
        r"点 $A$ 在曲线 $y=\mathrm e^x$ 上；对点 $B$，令 $u=\mathrm e^{x_2}>0$，则 $x_2=\ln u$，"
        r"即 $B=(u,\ln u)$ 在曲线 $y=\ln x$ 上。" "\n"
        r"因为 $y=\mathrm e^x$ 与 $y=\ln x$ 互为反函数，图象关于直线 $y=x$ 对称，"
        r"所以 $|AB|$ 的最小值等于曲线 $y=\mathrm e^x$ 上的点到直线 $y=x$ 的最小距离的 $2$ 倍。" "\n"
        r"设 $y=\mathrm e^x$ 在点 $(x_0,\mathrm e^{x_0})$ 处的切线与 $y=x$ 平行，由 $y'=\mathrm e^x$ 得"
        r"$\mathrm e^{x_0}=1$，即 $x_0=0$，切点为 $(0,1)$。" "\n"
        r"点 $(0,1)$ 到直线 $x-y=0$ 的距离 $d=\dfrac{|0-1|}{\sqrt{1^2+(-1)^2}}=\dfrac1{\sqrt2}$。" "\n"
        r"于是 $|AB|_{\min}=2d=\sqrt2$，所求最小值为 $|AB|_{\min}^2=2$．" "\n"
        r"故选 B．"
    ),
    'review': (
        r"① ⭐⭐ **识别距离的平方**：$(x_1-\mathrm e^{x_2})^2+(x_2-\mathrm e^{x_1})^2$ 中，"
        r"横坐标之差与纵坐标之差**交叉出现**，这正说明两点分别在两条曲线上，而非同一曲线。" "\n"
        r"② ⭐⭐ **反函数关于 $y=x$ 对称 ⟹ 两曲线间最短距离 $=2\times$ 单条曲线到 $y=x$ 的最短距离**。"
        r"这是本题的核心捷径，比直接对两个变量求偏导快得多。" "\n"
        r"③ ⭐ **最短距离点必是「与 $y=x$ 平行的切点」**：由 $\mathrm e^{x_0}=1$ 得 $x_0=0$，"
        r"切点 $(0,1)$，对称点 $(1,0)$ 在 $y=\ln x$ 上 ✓。" "\n"
        r"④ ⚠ **最后一步别忘了平方**：题目问的是距离平方，$\sqrt2$ 的平方是 $2$，不是 $\sqrt2$。" "\n"
        r"⑤ 数值复核：$A(0,1)$、$B(1,0)$ 时 $|AB|^2=(0-1)^2+(1-0)^2=2$ ✓；"
        r"取 $x_1=x_2=0$ 则得 $1+1=2$ 也是 $2$（但此时两点重合于 $(0,1)$？——"
        r"$B(\mathrm e^0,0)=(1,0)$，两点不同，距离确为 $\sqrt2$）✓" "\n"
        r"**通法（两曲线上两点距离最值）**：① 认出距离平方结构；② 若两曲线互为反函数，"
        r"用对称性化为「单曲线到 $y=x$ 的距离」；③ 平行切线定最短距离点；④ 注意所求的是距离还是距离平方。"
    ),
    'difficulty': 0.68,
    'topics': ['M-T-093'],
    'kp1': '函数与导数',
    'kp2': '导数切线与公切线',
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-093-V1',
}

T181_E1 = {
    'type': '选择',
    'stem_text': (
        r"函数 $f(x)=\dfrac{\sin x-1}{3-2\cos x-2\sin x}$（$x\in[0,2\pi]$）的最小值是（　　）"
    ),
    'opts': [('A', r'$-\dfrac12$'), ('B', r'$-1$'), ('C', r'$-2$'), ('D', r'$-3$')],
    'answer': r"C",
    'analysis': (
        r"分母 $=(1-\sin x)^2+(1-\cos x)^2$，分子 $=-(1-\sin x)$，故"
        r"$f=-\dfrac u{u^2+v^2}$（$u=1-\sin x,\ v=1-\cos x$）。求导令分子为零得 $\cos x+2\sin x=2$，"
        r"配合 $\sin^2x+\cos^2x=1$ 得 $\sin x=\dfrac35$（另一根 $\sin x=1$ 给 $f=0$ 非最小），"
        r"此时 $\cos x=\dfrac45$，$u=\dfrac25,\ v=\dfrac15$，$f=-\dfrac{2/5}{1/5}=-2$。"
        r"数值扫描最小值 $=-2.0000000$ 与之吻合。"
    ),
    'solution': (
        r"注意到 $(1-\sin x)^2+(1-\cos x)^2=1-2\sin x+\sin^2x+1-2\cos x+\cos^2x=3-2\sin x-2\cos x$，"
        r"即分母恰为 $(1-\sin x)^2+(1-\cos x)^2$。记 $u=1-\sin x\ge0,\ v=1-\cos x\ge0$，则" "\n"
        r"$f(x)=-\dfrac u{u^2+v^2}$。" "\n"
        r"当 $\sin x=1$ 即 $x=\dfrac\pi2$ 时 $u=0$，$f=0$，不是最小值。下设 $u>0$。" "\n"
        r"对 $f(x)$ 求导，令导函数分子为零：" "\n"
        r"$f'=\dfrac{-\cos x\cdot(3-2\sin x-2\cos x)+(\sin x-1)\cdot(-2\sin x+2\cos x)}{(3-2\sin x-2\cos x)^2}$，" "\n"
        r"分子 $=-3\cos x+2\sin x\cos x+2\cos^2x+2\sin x\cos x-2\sin^2x+2\sin x-2\cos x$" "\n"
        r"$=2(\sin^2x+\cos^2x)-\cos x-2\sin x=2-\cos x-2\sin x$（其中 $2\sin x\cos x$ 项恰好抵消）。" "\n"
        r"令 $2-\cos x-2\sin x=0$，即 $\cos x=2-2\sin x$。代入 $\sin^2x+\cos^2x=1$：" "\n"
        r"$\sin^2x+(2-2\sin x)^2=1\ \Longrightarrow\ 5\sin^2x-8\sin x+3=0$" "\n"
        r"$\Longrightarrow\ \sin x=1$ 或 $\sin x=\dfrac35$。" "\n"
        r"$\sin x=1$ 已讨论（$f=0$）；取 $\sin x=\dfrac35$，则 $\cos x=2-2\times\dfrac35=\dfrac45$，"
        r"此时 $u=\dfrac25,\ v=\dfrac15,\ u^2+v^2=\dfrac{4+1}{25}=\dfrac15$，" "\n"
        r"$f=-\dfrac{2/5}{1/5}=-2$。" "\n"
        r"比较端点：$x=0$ 时 $f=\dfrac{-1}{3-2}=-\dfrac12\times2=-1$（即 $f(0)=-1$）；"
        r"$x=\dfrac\pi2$ 时 $f=0$；$x=\dfrac{3\pi}2$ 时 $\sin x=-1,\cos x=0$，$f=\dfrac{-2}{3+2}=-\dfrac25$。"
        r"故最小值为 $-2$。" "\n"
        r"故选 C．" "\n"
        r"**附：原书详解的失误**——它令 $g=\dfrac{1-\cos x}{1-\sin x}$ 后写 $f=-\dfrac1{1+g^2}$，"
        r"但正确应为 $f=-\dfrac1{(1-\sin x)(1+g^2)}$，即**丢了因子 $(1-\sin x)$**。"
        r"在 $x=0$ 处 $1-\sin x=1$，两者碰巧同为 $-1$，详解遂误判最小值为 $-1$。"
    ),
    'review': (
        r"① ⭐⭐ **分母凑成平方和**：$3-2\sin x-2\cos x=(1-\sin x)^2+(1-\cos x)^2$ ——"
        r"这一步把三角最值问题转成了「$(u,v)$ 平面上的分式」，是本题的钥匙。" "\n"
        r"② ⭐⭐ **求导后 $\sin x\cos x$ 项必抵消**：分子化为 $2(\sin^2x+\cos^2x)-\cos x-2\sin x=2-\cos x-2\sin x$，"
        r"这种「交叉项自动消掉」是三角分式求导的常态，可用来自检。" "\n"
        r"③ ⭐ **$\cos x+2\sin x=2$ 与单位圆联立得二次方程** $5\sin^2x-8\sin x+3=0$，"
        r"两根为 $1$ 与 $\dfrac35$，其中 $\sin x=1$ 使分子为 $0$（$f=0$），须剔除。" "\n"
        r"④ ⚠ **必须比较分段点与驻点**：$x=0$ 给 $-1$、$x=\dfrac{3\pi}2$ 给 $-\dfrac25$、驻点给 $-2$。" "\n"
        r"⑤ ⚠ **原书答案 B($-1$) 有误**，正确为 C($-2$)。已作为 A 类勘误登记。" "\n"
        r"⑥ 数值复核：$2\times10^6$ 点扫描得最小值 $-1.99999999999$，取等处 $\sin x=0.600001,\ \cos x=0.800000$，"
        r"与理论值 $\left(\dfrac35,\dfrac45\right)$ 逐位吻合 ✓" "\n"
        r"**通法（三角分式最值）**：① 分母凑平方和或化为 $A\sin(x+\varphi)+B$；② 求导后利用"
        r"$\sin^2+\cos^2=1$ 化简；③ 驻点与 $x=0,\dfrac\pi2,\pi,\dfrac{3\pi}2,2\pi$ 等端点一起比较；"
        r"④ 用「值域合理性」（如本题 $f\in[-2,0]$）做量级自检。"
    ),
    'difficulty': 0.72,
    'topics': ['M-T-181'],
    'kp1': '三角函数',
    'kp2': '三角函数最值与范围',
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-181-E1',
}

T190_V1 = {
    'type': '选择',
    'stem_text': (
        r"在 $\triangle ABC$ 中，角 $A,B,C$ 的对边分别为 $a,b,c$，"
        r"若 $\sin(A+C)\left(\dfrac{\cos B}b+\dfrac{\cos C}c\right)=\dfrac{\sin A}{\sin C}$，$B=\dfrac\pi3$，"
        r"则 $a+c$ 的取值范围是（　　）"
    ),
    'opts': [
        ('A', r'$\left(\dfrac{\sqrt3}2,\sqrt3\right)$'),
        ('B', r'$\left(\dfrac{\sqrt3}2,\sqrt3\right]$'),
        ('C', r'$\left[\dfrac{\sqrt3}2,\sqrt3\right)$'),
        ('D', r'$\left[\dfrac{\sqrt3}2,\sqrt3\right]$'),
    ],
    'answer': r"B",
    'analysis': (
        r"由射影定理 $c\cos B+b\cos C=a$，条件化为 $\sin B\cdot\dfrac a{bc}=\dfrac ac$，"
        r"而 $\dfrac{\sin A}{\sin C}=\dfrac ac$，故 $\dfrac{\sin B}b=1$，即 $b=\sin B=\dfrac{\sqrt3}2$，"
        r"且 $2R=1$。于是 $a+c=\sin A+\sin\left(\dfrac{2\pi}3-A\right)=\sqrt3\sin\left(A+\dfrac\pi6\right)$。"
        r"$A\in\left(0,\dfrac{2\pi}3\right)$ 得 $a+c\in\left(\dfrac{\sqrt3}2,\sqrt3\right]$，"
        r"$A=\dfrac\pi3$（等边）时取到右端 $\sqrt3$。"
    ),
    'solution': (
        r"因为 $A+B+C=\pi$，所以 $\sin(A+C)=\sin B$。" "\n"
        r"又由射影定理 $c\cos B+b\cos C=a$，于是" "\n"
        r"$\dfrac{\cos B}b+\dfrac{\cos C}c=\dfrac{c\cos B+b\cos C}{bc}=\dfrac a{bc}$。" "\n"
        r"原条件化为 $\sin B\cdot\dfrac a{bc}=\dfrac{\sin A}{\sin C}$。" "\n"
        r"由正弦定理 $\dfrac a{\sin A}=\dfrac c{\sin C}$ 得 $\dfrac{\sin A}{\sin C}=\dfrac ac$，代入上式：" "\n"
        r"$\sin B\cdot\dfrac a{bc}=\dfrac ac\ \Longrightarrow\ \dfrac{\sin B}b=1\ \Longrightarrow\ b=\sin B=\sin\dfrac\pi3=\dfrac{\sqrt3}2$。" "\n"
        r"再由 $b=2R\sin B$ 得 $2R=1$，故 $a=\sin A,\ c=\sin C$。" "\n"
        r"由 $B=\dfrac\pi3$ 得 $A+C=\dfrac{2\pi}3$，即 $C=\dfrac{2\pi}3-A$，其中 $A\in\left(0,\dfrac{2\pi}3\right)$。" "\n"
        r"$a+c=\sin A+\sin\left(\dfrac{2\pi}3-A\right)=\sin A+\dfrac{\sqrt3}2\cos A+\dfrac12\sin A$" "\n"
        r"$=\dfrac32\sin A+\dfrac{\sqrt3}2\cos A=\sqrt3\left(\dfrac{\sqrt3}2\sin A+\dfrac12\cos A\right)$"
        r"$=\sqrt3\sin\left(A+\dfrac\pi6\right)$。" "\n"
        r"由 $A\in\left(0,\dfrac{2\pi}3\right)$ 得 $A+\dfrac\pi6\in\left(\dfrac\pi6,\dfrac{5\pi}6\right)$，"
        r"$\sin\left(A+\dfrac\pi6\right)\in\left(\dfrac12,1\right]$。" "\n"
        r"所以 $a+c\in\left(\dfrac{\sqrt3}2,\sqrt3\right]$：" "\n"
        r"$\bullet$ 当 $A+\dfrac\pi6=\dfrac\pi2$ 即 $A=\dfrac\pi3$ 时，$a+c=\sqrt3$（**可以取到**）；" "\n"
        r"$\bullet$ 当 $A\to0^+$ 或 $A\to\dfrac{2\pi}3{}^-$ 时 $a+c\to\dfrac{\sqrt3}2$，但 $A$ 不能取端点值，"
        r"故 $\dfrac{\sqrt3}2$ 取不到。" "\n"
        r"故选 B．" "\n"
        r"**附：原书标答 A 有误。** 取 $A=B=C=\dfrac\pi3$（等边），则 $a=b=c=\dfrac{\sqrt3}2$，"
        r"代入条件：左边 $=\sin\dfrac{2\pi}3\left(\dfrac{\cos\frac\pi3}{\sqrt3/2}+\dfrac{\cos\frac\pi3}{\sqrt3/2}\right)"
        r"=\dfrac{\sqrt3}2\times\dfrac{2}{\sqrt3}=1$，右边 $=\dfrac{\sin\frac\pi3}{\sin\frac\pi3}=1$，"
        r"条件成立且 $a+c=\sqrt3$ **精确取到**，故右端必为闭区间。"
    ),
    'review': (
        r"① ⭐⭐ **射影定理化简**：$c\cos B+b\cos C=a$ 是本题的钥匙，把两个分式合成一个，"
        r"$\dfrac{\cos B}b+\dfrac{\cos C}c=\dfrac a{bc}$。" "\n"
        r"② ⭐⭐ **$\dfrac{\sin A}{\sin C}=\dfrac ac$ 直接用正弦定理替换**，避免了边角混算。" "\n"
        r"③ ⭐ **由 $\dfrac{\sin B}b=1$ 同时得到两件事**：$b=\dfrac{\sqrt3}2$（边）与 $2R=1$（外接圆直径），"
        r"后者使 $a=\sin A$、$c=\sin C$，把边的问题完全化为角的问题。" "\n"
        r"④ ⭐ **$a+c=\sqrt3\sin\left(A+\dfrac\pi6\right)$ 的振幅是 $\sqrt3$**，"
        r"由 $\sqrt{\left(\dfrac32\right)^2+\left(\dfrac{\sqrt3}2\right)^2}=\sqrt3$ 得来，可自检。" "\n"
        r"⑤ ⚠ **右端点是否取到，取决于 $A=\dfrac\pi3$ 是否合法** —— 等边三角形合法，"
        r"且此时条件成立，故 $\sqrt3$ 必取到。原书答案 A（两端都开）忽略了这一点。" "\n"
        r"⑥ ⚠ **左端 $\dfrac{\sqrt3}2$ 取不到**，因 $A\to0$ 或 $C\to0$ 都导致三角形退化。" "\n"
        r"⑦ 数值复核：$2\times10^5$ 点扫描得 $a+c\in[0.866027,1.732051]$，"
        r"即 $\left(\dfrac{\sqrt3}2,\sqrt3\right]$ ✓；$A=\dfrac\pi3$ 时 $a+c=1.7320508=\sqrt3$ ✓" "\n"
        r"**通法（解三角形求边和范围）**：① 用射影定理/正弦定理把条件化为边或角的关系；"
        r"② 求出外接圆直径 $2R$ 与已知边；③ 把边和写成单角的正弦型；④ 由角的范围定区间，"
        r"并**逐端点检验是否取到**（退化情形必开）。"
    ),
    'difficulty': 0.62,
    'topics': ['M-T-190'],
    'kp1': '三角函数',
    'kp2': '解三角形小题(一)',
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-190-V1',
}

T209_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知 $\triangle ABC$ 的内角 $A,B,C$ 的对边分别为 $a,b,c$，"
        r"且 $a\cos B+\sqrt3\,a\sin B=c+1$，$b=1$，点 $G$ 是 $\triangle ABC$ 的重心，"
        r"且 $AG=\dfrac{\sqrt{21}}3$，则 $\triangle ABC$ 的面积为（　　）"
    ),
    'opts': [('A', r'$\dfrac32$'), ('B', r'$\sqrt3$'), ('C', r'$3$'), ('D', r'$2\sqrt3$')],
    'answer': r"B",
    'analysis': (
        r"由 $b=1$ 把条件写成 $a\cos B+\sqrt3\,a\sin B=c+b$，正弦定理后得"
        r"$\sqrt3\sin A=\cos A+1$，解得 $\cos A=\dfrac12$、$\sin A=\dfrac{\sqrt3}2$。"
        r"重心给 $AG=\dfrac23AD$，故中线 $AD=\dfrac{\sqrt{21}}2$；由中线长公式 $2c^2-a^2=19$，"
        r"与余弦定理 $a^2=c^2-c+1$ 联立得 $c=4$，面积 $=\dfrac12bc\sin A=\sqrt3$．"
    ),
    'solution': (
        r"因为 $b=1$，条件可写成 $a\cos B+\sqrt3\,a\sin B=c+b$。" "\n"
        r"由正弦定理 $a=2R\sin A$ 等，约去 $2R$ 得" "\n"
        r"$\sin A\cos B+\sqrt3\sin A\sin B=\sin C+\sin B$。" "\n"
        r"又 $\sin C=\sin(A+B)=\sin A\cos B+\cos A\sin B$，代入：" "\n"
        r"$\sin A\cos B+\sqrt3\sin A\sin B=\sin A\cos B+\cos A\sin B+\sin B$，" "\n"
        r"即 $\sqrt3\sin A\sin B=\cos A\sin B+\sin B$。因 $\sin B\ne0$，两边约去 $\sin B$：" "\n"
        r"$\sqrt3\sin A=\cos A+1$。" "\n"
        r"平方（或联立 $\sin^2A+\cos^2A=1$）：$3(1-\cos^2A)=(\cos A+1)^2$，"
        r"即 $3-3\cos^2A=\cos^2A+2\cos A+1$，整理得 $2\cos^2A+\cos A-1=0$，"
        r"解得 $\cos A=\dfrac12$ 或 $\cos A=-1$。" "\n"
        r"$\cos A=-1$ 时 $A=\pi$ 不成三角形，舍去；故 $\cos A=\dfrac12$，$\sin A=\dfrac{\sqrt3}2$。" "\n"
        r"设 $D$ 为 $BC$ 中点，则 $G$ 在 $AD$ 上且 $AG=\dfrac23AD$，"
        r"所以 $AD=\dfrac32AG=\dfrac32\times\dfrac{\sqrt{21}}3=\dfrac{\sqrt{21}}2$。" "\n"
        r"由中线长公式 $AD^2=\dfrac{2b^2+2c^2-a^2}4$：" "\n"
        r"$\dfrac{21}4=\dfrac{2+2c^2-a^2}4\ \Longrightarrow\ 2c^2-a^2=19$。" "\n"
        r"由余弦定理 $\cos A=\dfrac{b^2+c^2-a^2}{2bc}=\dfrac12$，代入 $b=1$：" "\n"
        r"$1+c^2-a^2=c\ \Longrightarrow\ a^2=c^2-c+1$。" "\n"
        r"代入前式：$2c^2-(c^2-c+1)=19$，即 $c^2+c-20=0$，"
        r"解得 $c=4$ 或 $c=-5$（舍）。" "\n"
        r"所以 $S_{\triangle ABC}=\dfrac12bc\sin A=\dfrac12\times1\times4\times\dfrac{\sqrt3}2=\sqrt3$。" "\n"
        r"故选 B．"
    ),
    'review': (
        r"① ⭐⭐ **把 $1$ 写成 $b$**：条件是 $a\cos B+\sqrt3\,a\sin B=c+1$，"
        r"由 $b=1$ 改写成 $c+b$，式子立刻关于 $a,b,c$ 齐次，才能整体用正弦定理。" "\n"
        r"② ⭐⭐ **$\sin C=\sin(A+B)$ 展开后 $\sin A\cos B$ 项两边抵消**，"
        r"剩下 $\sqrt3\sin A\sin B=(\cos A+1)\sin B$，约去 $\sin B\ne0$ 得 $\sqrt3\sin A=\cos A+1$。" "\n"
        r"③ ⭐ **$\sqrt3\sin A=\cos A+1$ 的标准处理**：平方 + $\sin^2+\cos^2=1$ 得"
        r"$2\cos^2A+\cos A-1=0$，根为 $\dfrac12$ 与 $-1$，后者使 $A=\pi$ 舍去。" "\n"
        r"④ ⭐ **重心 ⟹ $AG=\dfrac23AD$**，故 $AD=\dfrac32AG$；再用中线长公式"
        r"$AD^2=\dfrac{2b^2+2c^2-a^2}4$ 把「长度条件」翻译成边的方程。" "\n"
        r"⑤ ⭐ **两个方程联立消 $a^2$**：$2c^2-a^2=19$ 与 $a^2=c^2-c+1$ 得 $c^2+c-20=0$，"
        r"正整数根 $c=4$ 很整齐，可自检。" "\n"
        r"⑥ 数值复核：$c=4,b=1,\cos A=\dfrac12$ ⟹ $a^2=16-4+1=13$，$a=\sqrt{13}$；"
        r"$AD^2=\dfrac{2+32-13}4=\dfrac{21}4$ ✓，$AG=\dfrac23\times\dfrac{\sqrt{21}}2=\dfrac{\sqrt{21}}3$ ✓；"
        r"面积 $\dfrac12\times1\times4\times\dfrac{\sqrt3}2=\sqrt3$ ✓" "\n"
        r"**通法（含重心的解三角形）**：① 条件齐次化后用正弦定理化为角的关系；② 解出某个角；"
        r"③ 重心/中线条件用 $AG=\dfrac23AD$ 与中线长公式转成边的关系；④ 与余弦定理联立求边；⑤ 求面积。"
    ),
    'difficulty': 0.6,
    'topics': ['M-T-209'],
    'kp1': '三角函数',
    'kp2': '解三角形小题(二)',
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-209-V1',
}

QS = [T073_E1, T074_E1, T093_V1, T181_E1, T190_V1, T209_V1]
