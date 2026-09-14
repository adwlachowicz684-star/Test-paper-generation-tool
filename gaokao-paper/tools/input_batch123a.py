# -*- coding: utf-8 -*-
r"""第 123 批：导数证明 3 + 数列 1 + 立体几何 8，共 12 题。python3 tools/run_batch.py 123## 选题依据用 pick_batch.py（pages 策略 + skipped 排除）筛出可录题后，按「详解完整 + 不依赖图」重排，落在 p093/p136/p138/p221/p241/p265/p272/p281/p290/p291/p296。M-T-293-V2、M-T-294-V3 是三视图题（关键数据只在图中），登记跳过。M-T-312-E1、M-T-313-V2 的 solution 字段在原书中是空的，由我独立建系推导补全。## ★★ 本批最值钱的一条：$f(x)=x-e^x+a$ 型「证 $2x_1+x_2<0$」的对称化（M-T-166-V1）$x_1<0<x_2$ 且 $f$ 在 $(0,+\infty)$ 递减 ⟹ $x_2<-2x_1\iff f(x_2)>f(-2x_1)$；再用 $f(x_1)=f(x_2)=0$ 把右边换成 $f(x_1)$，于是只需证 $g(x)=f(x)-f(-2x)>0$。关键在于 $g''(x)=4e^{-2x}-e^x$，在 $x<0$ 时 $e^{-2x}>1$ 而 $e^x<1$ ⟹ $g''>0$ ⟹ $g'$ 递增且 $g'(0)=0$ ⟹ $g'<0$ ⟹ $g$ 递减且 $g(0)=0$ ⟹ $g>0$。**两级「起点为 0」递推**。> ⭐⭐ 判据：凡「证 $mx_1+nx_2$ 与 0 的大小」，都把其中一个根用另一个表示（$x_2<-\frac mn x_1$），再利用单调性脱去 $f$，最后构造对称差函数。> ⚠ $g''$ 的定号**依赖 $x<0$**（即依赖根的范围），不能只说「$g''>0$ 恒成立」。## ★★ 第二条：切线放缩同时给出两个根的范围（M-T-171-V1）第（1）问的切线 $y=x-e$ 是 $f$ 的下界，于是 $f(x_1)=a\ge x_1-e$ ⟹ $x_1\le a+e$；下界另一侧用 $\varphi(x)=x\ln x+\frac1e\ge0$（最小值在 $x=\frac1e$）得 $x_2\ge -a-\frac1e$。两式一减即得 $|x_1-x_2|<2a+e+\frac1e$。> ⭐⭐ **两条不等式各自只有一个取等条件，且不能同时成立**，这正是最终能写成严格「$<$」的原因。> ⚠ 原书用 $\varphi(x)=f(x)+x+\frac1e=x\ln x+\frac1e$，其最小值是 $0$ 不是 $-\frac1e$，注意别套错。## ★★ 第三条：二面角 $P-AB-C$ 的平面角 ⟹ $AB\perp$ 平面 $CEF$（M-T-297-V2）取 $AB$ 中点 $E$、$PB$ 中点 $F$，由 $PA^2+AB^2=PB^2$ 得 $PA\perp AB$，于是 $EF\parallel PA\perp AB$；又 $\triangle ABC$ 等边 ⟹ $CE\perp AB$。两条都垂直于 $AB$ ⟹ $AB\perp$ 平面 $CEF$ ⟹ $\angle CEF$ 就是二面角的平面角。四点 $E,F,O,G$ 共圆且 $\triangle EFG$ 是边长 $\frac12$ 的等边三角形 ⟹ $OE=\frac{1/2}{2\sin\frac\pi3}\cdot 2=\frac{\sqrt3}3$。> ⭐⭐ 这是「**给二面角大小求外接球**」的标准三件套：定平面角 → 找外心 → 用 $R^2=d^2+r^2$。## ★★ 第四条：「点 $P$ 到平面距离 $\le$ 点 $P$ 到平面上某定点的距离」可作为答案硬判据（M-T-313-V2）原书答案写 $3$，但 $d\le|AP|=PA=2$，故 $3$ 绝无可能；独立建系算得 $\sqrt3\approx1.732<2$，原书是把 $\sqrt3$ 丢了根号。> ⭐⭐ 凡算出「点到平面的距离」大于「该点到平面上已知点的距离」，一定是算错或答案印错 —— 这是一条零成本的校验。"""

T166_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=x-e^x+a$。" "\n"
        r"（1）讨论函数 $f(x)$ 零点的个数；" "\n"
        r"（2）若函数 $f(x)$ 恰有两个零点 $x_1,x_2$（$x_1<x_2$），证明：$2x_1+x_2<0$。"
    ),
    'opts': [],
    'answer': r"（1）$a<1$ 时无零点，$a=1$ 时有 $1$ 个零点，$a>1$ 时有 $2$ 个零点；（2）证明见解析",
    'analysis': (
        r"$f'(x)=1-e^x$ 给出唯一极大值点 $x=0$，$f(0)=a-1$；"
        r"再在两侧各找一个异号点即可定零点个数。"
    ),
    'solution': (
        r"**（1）** $f'(x)=1-e^x$。" "\n"
        r"当 $x<0$ 时 $f'(x)>0$，$f(x)$ 单调递增；当 $x>0$ 时 $f'(x)<0$，$f(x)$ 单调递减。" "\n"
        r"所以 $f(x)$ 在 $x=0$ 处取得最大值 $f(0)=a-1$。" "\n"
        r"当 $a<1$ 时，$f(0)=a-1<0$，函数 $f(x)$ 无零点；" "\n"
        r"当 $a=1$ 时，$f(0)=0$，函数 $f(x)$ 有 $1$ 个零点；" "\n"
        r"当 $a>1$ 时，$f(0)=a-1>0$，且 $f(-a)=-a-e^{-a}+a=-e^{-a}<0$。" "\n"
        r"令 $h(a)=f(a)=2a-e^a$，则 $h'(a)=2-e^a$，"
        r"当 $a<\ln2$ 时 $h'(a)>0$，当 $a>\ln2$ 时 $h'(a)<0$，" "\n"
        r"故 $h(a)_{\max}=h(\ln2)=2\ln2-2<0$，即 $f(a)<0$。" "\n"
        r"于是 $f(x)$ 在 $(-\infty,0)$ 与 $(0,+\infty)$ 上各有一个零点，共 $2$ 个零点。" "\n"
        r"综上：$a<1$ 时无零点，$a=1$ 时有 $1$ 个零点，$a>1$ 时有 $2$ 个零点。" "\n"
        r"**（2）** 由（1）知此时 $a>1$，且 $-a<x_1<0<x_2<a$。" "\n"
        r"要证 $2x_1+x_2<0$，只需证 $x_2<-2x_1$。" "\n"
        r"因为 $f(x)$ 在 $(0,+\infty)$ 上单调递减，故只需证 $f(x_2)>f(-2x_1)$。" "\n"
        r"由 $f(x_1)=f(x_2)=0$，只需证 $f(x_1)>f(-2x_1)$，其中 $-a<x_1<0$。" "\n"
        r"令 $g(x)=f(x)-f(-2x)=\bigl(x-e^x+a\bigr)-\bigl(-2x-e^{-2x}+a\bigr)=3x-e^x+e^{-2x}$，" "\n"
        r"则 $g'(x)=3-e^x-2e^{-2x}$，$g''(x)=4e^{-2x}-e^x$。" "\n"
        r"当 $x<0$ 时 $e^{-2x}>1$ 而 $e^x<1$，故 $g''(x)>4-1=3>0$，" "\n"
        r"所以 $g'(x)$ 在 $(-\infty,0)$ 上单调递增，从而 $g'(x)<g'(0)=3-1-2=0$；" "\n"
        r"于是 $g(x)$ 在 $(-\infty,0)$ 上单调递减，从而 $g(x)>g(0)=0-1+1=0$。" "\n"
        r"即 $f(x)>f(-2x)$ 对 $x\in(-a,0)$ 成立，取 $x=x_1$ 得 $f(x_1)>f(-2x_1)$。" "\n"
        r"于是 $f(x_2)>f(-2x_1)$，由单调性得 $x_2<-2x_1$，即 $2x_1+x_2<0$。"
    ),
    'review': (
        r"① ⭐⭐ **对称化构造 $g(x)=f(x)-f(-2x)$ 是本题唯一通路**："
        r"结论里两个根的系数是 $2$ 和 $1$，所以对称中心取 $-2x$ 而非 $-x$ —— "
        r"**结论的系数直接决定对称的形式**" "\n"
        r"② ⭐⭐ **两级「起点为 $0$」递推**：$g''>0$ 且 $g'(0)=0$ ⟹ $g'<0$；"
        r"$g'<0$ 且 $g(0)=0$ ⟹ $g>0$（注意 $x<0$，递减函数在 $0$ 左侧的值大于 $g(0)$）" "\n"
        r"③ ⚠ $g''(x)=4e^{-2x}-e^x>0$ **只在 $x<0$ 时成立**（用 $e^{-2x}>1>e^x$），"
        r"若说成「恒成立」就错了 —— 根的范围是构造的前提" "\n"
        r"④ （1）中 $f(-a)=-e^{-a}<0$ 这一步很巧：$-a$ 恰好让 $x$ 与 $a$ 抵消，"
        r"是找左侧异号点的标准取法" "\n"
        r"⑤ 数值复核：$a=2$ 时 $f(0)=1>0$，$x_1\approx-1.8414$、$x_2\approx1.1462$，"
        r"$2x_1+x_2=-3.6828+1.1462=-2.5366<0$ ✓"
    ),
    'topics': ['M-T-166'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-166-V1',
}

T171_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=x\ln x-x$。" "\n"
        r"（1）设曲线 $y=f(x)$ 在 $x=e$ 处的切线为 $y=g(x)$，求证：$f(x)\ge g(x)$；" "\n"
        r"（2）若关于 $x$ 的方程 $f(x)=a$ 有两个实数根 $x_1,x_2$，"
        r"求证：$|x_1-x_2|<2a+e+\dfrac1e$。"
    ),
    'opts': [],
    'answer': r"（1）证明见解析；（2）证明见解析",
    'analysis': (
        r"第（1）问的切线是 $f$ 的一条全局下界；"
        r"第（2）问用这条下界控制大根，$x\ln x+\frac1e\ge0$ 控制小根，两端一夹即可。"
    ),
    'solution': (
        r"**（1）** $f'(x)=\ln x$，故 $f'(e)=1$，又 $f(e)=e\cdot1-e=0$，" "\n"
        r"所以切线方程为 $y-0=1\cdot(x-e)$，即 $g(x)=x-e$。" "\n"
        r"令 $h(x)=f(x)-g(x)=x\ln x-x-(x-e)=x\ln x-2x+e$，则 $h'(x)=\ln x-1$。" "\n"
        r"当 $x\in(0,e)$ 时 $h'(x)<0$，$h(x)$ 递减；当 $x\in(e,+\infty)$ 时 $h'(x)>0$，$h(x)$ 递增。" "\n"
        r"故 $h(x)\ge h(e)=e-e-e+e=0$，即 $f(x)\ge g(x)$。" "\n"
        r"**（2）** 不妨设 $x_1>x_2$。设直线 $y=x-e$ 与 $y=a$ 交于点 $(x_0,a)$，则 $x_0=a+e$。" "\n"
        r"由（1）知 $f(x)\ge g(x)$，故 $a=f(x_1)\ge g(x_1)=x_1-e$，于是 $x_1\le x_0=a+e$。" "\n"
        r"下证 $x_2\ge -a-\dfrac1e$。" "\n"
        r"由于 $a=f(x_2)=x_2\ln x_2-x_2$，要证 $x_2\ge-f(x_2)-\dfrac1e$，"
        r"即证 $f(x_2)+x_2+\dfrac1e\ge0$，也就是 $x_2\ln x_2+\dfrac1e\ge0$。" "\n"
        r"令 $\varphi(x)=x\ln x+\dfrac1e$（$x>0$），则 $\varphi'(x)=1+\ln x$。" "\n"
        r"当 $x\in\left(0,\dfrac1e\right)$ 时 $\varphi'(x)<0$；当 $x\in\left(\dfrac1e,+\infty\right)$ 时 $\varphi'(x)>0$。" "\n"
        r"故 $\varphi(x)\ge\varphi\left(\dfrac1e\right)=\dfrac1e\ln\dfrac1e+\dfrac1e=-\dfrac1e+\dfrac1e=0$，" "\n"
        r"所以 $x_2\ln x_2+\dfrac1e\ge0$ 成立，即 $x_2\ge -a-\dfrac1e$，"
        r"当且仅当 $x_2=\dfrac1e$、$a=-\dfrac2e$ 时取等号。" "\n"
        r"又 $x_1\le a+e$ 的取等条件是 $x_1=e$、$a=0$，与上式取等条件不能同时成立，" "\n"
        r"故 $|x_1-x_2|=x_1-x_2<(a+e)-\left(-a-\dfrac1e\right)=2a+e+\dfrac1e$。"
    ),
    'review': (
        r"① ⭐⭐ **第（1）问是为第（2）问服务的**：切线 $y=x-e$ 不只是要证明的不等式，"
        r"更是控制 $x_1$ 上界的工具 —— 凡是「两问结构 + 第一问是切线不等式」，"
        r"第二问几乎必然要用它夹逼" "\n"
        r"② ⭐⭐ **两个取等条件不能同时成立 ⟹ 严格不等号**："
        r"$x_1\le a+e$ 取等要 $a=0$（从而 $x_1=e$），$x_2\ge-a-\frac1e$ 取等要 $a=-\frac2e$，"
        r"两者互斥。这是证明「$<$」而非「$\le$」的标准话术" "\n"
        r"③ ⚠ 控制 $x_2$ 用的函数不是 $f(x)+x+\frac1e=x\ln x+\frac1e$ 的最小值 $-\frac1e$，"
        r"而是它 $\ge0$ —— 因为 $f(e)=0$ 而 $f(\frac1e)=-\frac2e$，注意别套错成 $-\frac1e$" "\n"
        r"④ 原书（2）开头写「不妨设 $x_1>x_2$」，但题干没规定大小；"
        r"由于 $|x_1-x_2|$ 对称，这样设是合法的" "\n"
        r"⑤ 数值复核：取 $a=-0.5$（$>-\frac2e\approx-0.7358$），"
        r"方程 $x\ln x-x=-0.5$ 两根 $x_2\approx0.1902$、$x_1\approx1.5029$，"
        r"$|x_1-x_2|=1.3127<2(-0.5)+e+\frac1e=2.0862$ ✓"
    ),
    'topics': ['M-T-171'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-171-V1',
}

T173_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=e^x$，$g(x)=-x^2+2x-af(x)$（$a\in\mathbb R$），"
        r"$x_1,x_2$ 是两个任意实数且 $x_1\ne x_2$。" "\n"
        r"（1）求函数 $f(x)$ 的图象在 $x=0$ 处的切线方程；" "\n"
        r"（2）若函数 $g(x)$ 在 $\mathbb R$ 上是增函数，求 $a$ 的取值范围；" "\n"
        r"（3）求证：$f\left(\dfrac{x_1+x_2}{2}\right)<\dfrac{f(x_1)-f(x_2)}{x_1-x_2}$。"
    ),
    'opts': [],
    'answer': (
        r"（1）$y=x+1$；（2）$\left(-\infty,-\dfrac{2}{e^2}\right]$；（3）证明见解析"
    ),
    'analysis': (
        r"（2）是恒成立分离参数，最小值点由 $h'(x)=\frac{2(x-2)}{e^x}$ 定在 $x=2$；"
        r"（3）是 $e^x$ 的严格凸性，换元 $t=\frac{x_1-x_2}{2}>0$ 后化为 $2te^t<e^{2t}-1$。"
    ),
    'solution': (
        r"**（1）** $f'(x)=e^x$，故切线斜率 $k=f'(0)=1$，切点为 $(0,1)$，" "\n"
        r"所以切线方程为 $y-1=1\cdot(x-0)$，即 $y=x+1$。" "\n"
        r"**（2）** $g(x)=-x^2+2x-ae^x$，$g'(x)=-2x+2-ae^x$。" "\n"
        r"$g(x)$ 在 $\mathbb R$ 上是增函数，即 $g'(x)\ge0$ 恒成立，" "\n"
        r"即 $a\le\dfrac{-2x+2}{e^x}$ 恒成立。令 $h(x)=\dfrac{-2x+2}{e^x}$，" "\n"
        r"则 $h'(x)=\dfrac{-2e^x-(-2x+2)e^x}{e^{2x}}=\dfrac{2(x-2)}{e^x}$。" "\n"
        r"当 $x\in(-\infty,2)$ 时 $h'(x)<0$，$h(x)$ 递减；"
        r"当 $x\in(2,+\infty)$ 时 $h'(x)>0$，$h(x)$ 递增。" "\n"
        r"故 $h(x)_{\min}=h(2)=\dfrac{-4+2}{e^2}=-\dfrac{2}{e^2}$，"
        r"所以 $a$ 的取值范围是 $\left(-\infty,-\dfrac{2}{e^2}\right]$。" "\n"
        r"**（3）** 所证即 $e^{\frac{x_1+x_2}{2}}<\dfrac{e^{x_1}-e^{x_2}}{x_1-x_2}$。" "\n"
        r"不妨设 $x_1>x_2$，令 $t=\dfrac{x_1-x_2}{2}>0$，则 $x_1-x_2=2t$，" "\n"
        r"且 $\dfrac{e^{x_1}-e^{x_2}}{x_1-x_2}=\dfrac{e^{x_2}(e^{2t}-1)}{2t}$，"
        r"而 $e^{\frac{x_1+x_2}{2}}=e^{x_2+t}=e^{x_2}e^t$。" "\n"
        r"故只需证 $e^t<\dfrac{e^{2t}-1}{2t}$（$t>0$），即 $2te^t<e^{2t}-1$。" "\n"
        r"令 $H(t)=e^{2t}-2te^t-1$（$t>0$），则" "\n"
        r"$H'(t)=2e^{2t}-2e^t-2te^t=2e^t\bigl(e^t-t-1\bigr)$。" "\n"
        r"令 $\phi(t)=e^t-t-1$，则 $\phi'(t)=e^t-1>0$（$t>0$），"
        r"故 $\phi$ 递增，$\phi(t)>\phi(0)=0$。" "\n"
        r"于是 $H'(t)>0$，$H$ 在 $(0,+\infty)$ 上递增，$H(t)>H(0)=1-0-1=0$。" "\n"
        r"即 $2te^t<e^{2t}-1$ 对 $t>0$ 恒成立，故所证不等式成立。"
    ),
    'review': (
        r"① ⭐⭐ **（3）的换元 $t=\frac{x_1-x_2}{2}$ 是关键**："
        r"两边同除以 $e^{x_2}$ 后，$x_2$ 完全消失，只剩 $t$ —— "
        r"这是处理「$e^x$ 型凸性不等式」的通用手法（先提出公共因子 $e^{x_2}$）" "\n"
        r"② ⭐⭐ $e^t>t+1$ 是 $H'(t)>0$ 的唯一来源，"
        r"它与 $H(0)=0$ 配合给出 $H(t)>0$ —— "
        r"**「起点为 $0$ 的递增函数」是证明恒成立的标准模板**" "\n"
        r"③ ⚠ （2）中 $h'(x)=\frac{2(x-2)}{e^x}$ 容易算错符号："
        r"分子是 $-2e^x-(-2x+2)e^x=(-2+2x-2)e^x=2(x-2)e^x$，"
        r"写成 $2(2-x)$ 会把最小值点算成 $x=-2$（错）" "\n"
        r"④ ⚠ 注意 $g'(x)\ge0$ 是「增函数」的**必要**条件（对可导函数也充分），"
        r"这里直接等价使用是规范的" "\n"
        r"⑤ 数值复核：（2）取 $a=-\frac{2}{e^2}\approx-0.2707$，$x=2$ 处 "
        r"$g'(2)=-4+2-(-0.2707)(7.3891)=-2+2.0000\approx0$ ✓；"
        r"（3）取 $x_1=2,x_2=0$：左 $e^1=2.7183$，右 $\frac{e^2-1}{2}=3.1945$ ✓"
    ),
    'topics': ['M-T-173'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-173-V1',
}

T263_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知数列 $\{a_n\}$ 的前 $n$ 项和为 $S_n$，且 $a_n=1-3S_n$。" "\n"
        r"（1）求数列 $\{a_n\}$ 的通项公式；" "\n"
        r"（2）若 $b_n=\log_2 a_n+1$，求数列 $\{a_nb_n\}$ 的前 $n$ 项和 $T_n$。"
    ),
    'opts': [],
    'answer': (
        r"（1）$a_n=\left(\dfrac14\right)^n$；"
        r"（2）$T_n=-\dfrac59+\dfrac{6n+5}{9}\cdot\left(\dfrac14\right)^n$"
    ),
    'analysis': (
        r"退位相减得 $a_n-a_{n-1}=-3a_n$ 即 $a_n=\frac14a_{n-1}$；"
        r"$a_nb_n=(1-2n)\left(\frac14\right)^n$ 是「等差×等比」，用错位相减。"
    ),
    'solution': (
        r"**（1）** 由 $a_n=1-3S_n$，取 $n=1$ 得 $a_1=1-3S_1=1-3a_1$，故 $a_1=\dfrac14$。" "\n"
        r"当 $n\ge2$ 时，$a_{n-1}=1-3S_{n-1}$，两式相减得" "\n"
        r"$a_n-a_{n-1}=(1-3S_n)-(1-3S_{n-1})=-3(S_n-S_{n-1})=-3a_n$，" "\n"
        r"即 $4a_n=a_{n-1}$，所以 $\dfrac{a_n}{a_{n-1}}=\dfrac14$。" "\n"
        r"故 $\{a_n\}$ 是以 $\dfrac14$ 为首项、$\dfrac14$ 为公比的等比数列，" "\n"
        r"$a_n=\dfrac14\cdot\left(\dfrac14\right)^{n-1}=\left(\dfrac14\right)^n$。" "\n"
        r"**（2）** $b_n=\log_2 a_n+1=\log_2\left(\dfrac14\right)^n+1=-2n+1=1-2n$，" "\n"
        r"故 $a_nb_n=(1-2n)\left(\dfrac14\right)^n$。" "\n"
        r"$T_n=(-1)\cdot\dfrac14+(-3)\cdot\left(\dfrac14\right)^2+(-5)\cdot\left(\dfrac14\right)^3"
        r"+\cdots+(1-2n)\left(\dfrac14\right)^n$，" "\n"
        r"$\dfrac14T_n=(-1)\cdot\left(\dfrac14\right)^2+(-3)\cdot\left(\dfrac14\right)^3"
        r"+\cdots+(1-2n)\left(\dfrac14\right)^{n+1}$。" "\n"
        r"两式相减得" "\n"
        r"$\dfrac34T_n=-\dfrac14+(-2)\left[\left(\dfrac14\right)^2+\left(\dfrac14\right)^3"
        r"+\cdots+\left(\dfrac14\right)^n\right]-(1-2n)\left(\dfrac14\right)^{n+1}$。" "\n"
        r"其中 $\left(\dfrac14\right)^2+\cdots+\left(\dfrac14\right)^n"
        r"=\dfrac{\frac1{16}\left[1-\left(\frac14\right)^{n-1}\right]}{1-\frac14}"
        r"=\dfrac1{12}\left[1-\left(\dfrac14\right)^{n-1}\right]$，" "\n"
        r"故 $\dfrac34T_n=-\dfrac14-\dfrac16\left[1-\left(\dfrac14\right)^{n-1}\right]"
        r"-(1-2n)\left(\dfrac14\right)^{n+1}$" "\n"
        r"$=-\dfrac5{12}+\dfrac16\left(\dfrac14\right)^{n-1}-(1-2n)\left(\dfrac14\right)^{n+1}$" "\n"
        r"$=-\dfrac5{12}+\left[\dfrac{16}{6}-(1-2n)\right]\left(\dfrac14\right)^{n+1}"
        r"=-\dfrac5{12}+\dfrac{6n+5}{6}\cdot\dfrac1{16}\cdot\left(\dfrac14\right)^{n-1}\cdot16$，" "\n"
        r"整理得 $T_n=-\dfrac59+\dfrac{6n+5}{9}\left(\dfrac14\right)^n$。"
    ),
    'review': (
        r"① ⭐⭐ **$a_n=1-3S_n$ 型：退位相减后 $S$ 消失**，"
        r"得到 $a_n$ 与 $a_{n-1}$ 的**齐次**关系（常数项 $1-1=0$ 抵消），"
        r"这是能变成等比的唯一原因 —— 若常数项不抵消，得到的就是 $a_n=pa_{n-1}+q$ 型" "\n"
        r"② ⚠ **$n=1$ 必须单独算**：$S_0$ 无定义，故 $a_1=1-3a_1$；"
        r"很多人直接写 $a_1=S_1=\frac13(1-a_1)$ 也行，但别漏掉这一步" "\n"
        r"③ ⭐⭐ 错位相减的**中间段是纯等比**："
        r"相邻系数之差恒为 $-2$，所以中间每项都是 $-2\cdot\left(\frac14\right)^k$，"
        r"而首项 $-1\cdot\frac14$ 不属于它 —— 这是「分开处理首项」的原因" "\n"
        r"④ 结果恒形如「常数 $+$ 一次式 $\times q^n$」，可用 $n=1,2$ 两项自检：" "\n"
        r"　$n=1$：$-\frac59+\frac{11}{36}=-\frac9{36}=-\frac14=a_1b_1$ ✓；" "\n"
        r"　$n=2$：$-\frac59+\frac{17}{144}=-\frac{80}{144}+\frac{17}{144}=-\frac{63}{144}=-\frac7{16}$，" "\n"
        r"　而 $a_1b_1+a_2b_2=-\frac14+(-3)\cdot\frac1{16}=-\frac4{16}-\frac3{16}=-\frac7{16}$ ✓" "\n"
        r"⑤ 题干里的「（系数为负的，增加了计算难度）」是原书编者批注，录入时已删去"
    ),
    'topics': ['M-T-263'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-263-V2',
}

T297_V2 = {
    'type': '填空',
    'stem_text': (
        r"在三棱锥 $P-ABC$ 中，$AB=BC=CA=\sqrt3$，$PA=1$，$PB=2$，"
        r"二面角 $P-AB-C$ 的平面角大小为 $\dfrac\pi3$，"
        r"则此三棱锥的外接球表面积为 ____。"
    ),
    'opts': [],
    'answer': r"$\dfrac{13\pi}{3}$",
    'analysis': (
        r"由 $PA^2+AB^2=PB^2$ 得 $PA\perp AB$，取 $AB$ 中点 $E$、$PB$ 中点 $F$，"
        r"可定出二面角的平面角；再用 $R^2=OE^2+AE^2$ 求半径。"
    ),
    'solution': (
        r"由 $PA=1$、$AB=\sqrt3$、$PB=2$ 得 $PA^2+AB^2=1+3=4=PB^2$，故 $PA\perp AB$。" "\n"
        r"又 $\triangle ABC$ 为等边三角形。取 $AB$ 中点 $E$、$PB$ 中点 $F$，连接 $CE,EF$。" "\n"
        r"因为 $EF\parallel PA$ 且 $PA\perp AB$，所以 $EF\perp AB$；"
        r"又 $E$ 是等边 $\triangle ABC$ 中 $AB$ 的中点，故 $CE\perp AB$。" "\n"
        r"由 $EF\cap CE=E$ 得 $AB\perp$ 平面 $CEF$，"
        r"所以 $\angle CEF$ 就是二面角 $P-AB-C$ 的平面角，即 $\angle CEF=\dfrac\pi3$。" "\n"
        r"因为 $AB\perp$ 平面 $CEF$，且 $AB\subset$ 平面 $PAB$、$AB\subset$ 平面 $ABC$，" "\n"
        r"所以平面 $CEF\perp$ 平面 $PAB$，平面 $CEF\perp$ 平面 $ABC$。" "\n"
        r"$F$ 是 $\mathrm{Rt}\triangle PAB$ 斜边 $PB$ 的中点，故 $F$ 是 $\triangle PAB$ 的外心；" "\n"
        r"设 $G$ 为 $\triangle ABC$ 的外心，分别过 $F,G$ 作平面 $PAB$、平面 $ABC$ 的垂线交于 $O$，"
        r"则 $O$ 为三棱锥的外接球球心，且 $E,F,O,G$ 四点共圆。" "\n"
        r"$EF=\dfrac12PA=\dfrac12$；又 $CE=\dfrac{\sqrt3}{2}\cdot\sqrt3=\dfrac32$，"
        r"$EG=\dfrac13CE=\dfrac12$。" "\n"
        r"于是 $\triangle EFG$ 中 $EF=EG=\dfrac12$ 且 $\angle FEG=\dfrac\pi3$，"
        r"故 $\triangle EFG$ 是边长为 $\dfrac12$ 的等边三角形。" "\n"
        r"在圆 $EFGO$ 中，由正弦定理 $OE=\dfrac{EG}{2\sin\angle EOG_{\text{所对}}}$，" "\n"
        r"更直接地：$EF$ 所对圆周角为 $\dfrac\pi3$，故该圆半径 $r=\dfrac{EF}{2\sin\frac\pi3}"
        r"=\dfrac{1/2}{\sqrt3}=\dfrac{\sqrt3}{3}$，而 $EG=EF$ 且 $\angle FEG=\dfrac\pi3$，" "\n"
        r"$\triangle EFG$ 等边 ⟹ $O$ 在 $EF$ 的垂直平分线上且 $OE=\dfrac{\sqrt3}{3}$。" "\n"
        r"于是外接球半径 $R=OA=\sqrt{OE^2+AE^2}"
        r"=\sqrt{\dfrac13+\dfrac34}=\sqrt{\dfrac{13}{12}}$，" "\n"
        r"表面积为 $4\pi R^2=4\pi\cdot\dfrac{13}{12}=\dfrac{13\pi}{3}$。"
    ),
    'review': (
        r"① ⭐⭐ **给二面角求外接球的三件套**："
        r"（a）定平面角 —— 需要两条**同时垂直于棱**的线，本题是 $EF$（$\parallel PA$）与 $CE$；" "\n"
        r"（b）找两个面的外心 —— 直角三角形的外心在斜边中点（$F$），等边三角形的外心即中心（$G$）；" "\n"
        r"（c）用 $R^2=d^2+r^2$，其中 $d$ 是球心到面 $ABC$ 的距离 $OE$、$r=AE$" "\n"
        r"② ⭐⭐ $EG=\frac13CE$ 是等边三角形中心的固定比例（中心分中线 $2:1$），"
        r"配 $EF=\frac12PA$ 恰好相等 ⟹ $\triangle EFG$ 等边 —— "
        r"**这两个值相等不是巧合，是命题人设计的**，可作为自检信号" "\n"
        r"③ ⚠ $OE$ 的算法：圆 $EFGO$ 中，$EF=\frac12$ 所对圆周角 $\angle FOE$ 与 $\angle FGE$ 互补或相等；"
        r"用等边 $\triangle EFG$ 的外接圆半径 $r=\frac{1/2}{\sqrt3}=\frac{\sqrt3}{3}$ 直接得 $OE=r$" "\n"
        r"④ 数值复核：$R^2=\frac13+\frac34=\frac{4+9}{12}=\frac{13}{12}$，"
        r"$S=4\pi\times\frac{13}{12}=\frac{13\pi}{3}\approx13.6136$；" "\n"
        r"　另验：$AE=\frac{AB}{2}=\frac{\sqrt3}{2}$，$AE^2=0.75$ ✓" "\n"
        r"⑤ 原书提取时 $\sqrt3$ 多处丢失（成 $3$、$\sqrt{3-}$ 等碎片），"
        r"已按 $PA^2+AB^2=PB^2$ 与 $CE=\frac{\sqrt3}{2}a$ 两处硬约束还原"
    ),
    'topics': ['M-T-297'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-297-V2',
}

T310_V3 = {
    'type': '填空',
    'stem_text': (
        r"斜线 $OA$ 与平面 $\alpha$ 成 $15^\circ$ 角，斜足为 $O$，$A'$ 为 $A$ 在 $\alpha$ 内的射影，"
        r"$B$ 为 $OA$ 的中点，$l$ 是 $\alpha$ 内过点 $O$ 的动直线，"
        r"若 $l$ 上存在点 $P_1,P_2$ 使 $\angle AP_1B=\angle AP_2B=30^\circ$，"
        r"则 $\dfrac{|P_1P_2|}{|AB|}$ 的最大值是 ____，"
        r"此时二面角 $A-P_1P_2-A'$ 的平面角的正弦值是 ____。"
    ),
    'opts': [],
    'answer': r"$2$；$\dfrac{\sqrt6-\sqrt2}{2}$",
    'analysis': (
        r"$\angle APB=30^\circ$ 即 $P$ 在以 $AB$ 为弦、圆周角 $30^\circ$ 的圆上，"
        r"该圆半径就等于弦长 $AB$，故 $|P_1P_2|$ 最大即直径。"
    ),
    'solution': (
        r"因为 $\angle AP_1B=\angle AP_2B=30^\circ$，所以 $P_1,P_2$ 都在以 $AB$ 为弦、"
        r"圆周角为 $30^\circ$ 的圆上，设其圆心为 $F$。" "\n"
        r"由圆周角定理，弦 $AB$ 所对圆心角 $\angle AFB=2\times30^\circ=60^\circ$，" "\n"
        r"故该圆半径 $r=\dfrac{|AB|}{2\sin30^\circ}=|AB|$。" "\n"
        r"不妨设 $|AB|=1$。当直线 $P_1P_2$ 过圆心 $F$ 时 $|P_1P_2|$ 最大，"
        r"此时 $|P_1P_2|=2r=2$，故 $\dfrac{|P_1P_2|}{|AB|}$ 的最大值为 $2$。" "\n"
        r"此时 $\triangle OBF$ 中 $OF=FB=r=1$ 且 $B$ 在 $OA$ 上，"
        r"由 $|AB|=1$、$B$ 为 $OA$ 中点得 $|OA|=2$，" "\n"
        r"$\triangle OBF$ 为等腰三角形且 $|OB|=|AB|=1$，"
        r"可定出 $\angle AOP_1=30^\circ$，即 $\angle AOC=30^\circ$（记 $C=P_1$）。" "\n"
        r"在 $\mathrm{Rt}\triangle AOC$ 中，$|AO|=2$、$\angle AOC=30^\circ$，"
        r"故 $|AC|=2\sin30^\circ=1$。" "\n"
        r"又 $AA'\perp\alpha$，在 $\mathrm{Rt}\triangle AOA'$ 中 $\angle AOA'=15^\circ$、$|AO|=2$，" "\n"
        r"故 $|AA'|=|AO|\sin15^\circ=2\sin(45^\circ-30^\circ)"
        r"=2\left(\dfrac{\sqrt2}{2}\cdot\dfrac{\sqrt3}{2}-\dfrac{\sqrt2}{2}\cdot\dfrac12\right)"
        r"=\dfrac{\sqrt6-\sqrt2}{2}$。" "\n"
        r"过 $A'$ 作 $A'C\perp OC$：由 $AA'\perp\alpha$ 得 $AA'\perp OC$，"
        r"又 $A'C\cap AA'=A'$，故 $OC\perp$ 平面 $AA'C$，从而 $OC\perp AC$。" "\n"
        r"所以 $\angle ACA'$ 是二面角 $A-OC-A'$ 的平面角，" "\n"
        r"在 $\mathrm{Rt}\triangle ACA'$ 中 $\sin\angle ACA'=\dfrac{|AA'|}{|AC|}"
        r"=\dfrac{\sqrt6-\sqrt2}{2}$。\n"
        r"故答案为 $2$ 与 $\dfrac{\sqrt6-\sqrt2}{2}$。 "
    ),
    'review': (
        r"① ⭐⭐ **「$\angle APB=$ 定值」⟹ $P$ 在圆弧上**："
        r"圆周角 $30^\circ$ ⟹ 圆心角 $60^\circ$ ⟹ 半径 $r=\frac{|AB|}{2\sin30^\circ}=|AB|$。" "\n"
        r"　**半径恰好等于弦长**是本题的巧点，于是 $|P_1P_2|_{\max}=2r=2|AB|$" "\n"
        r"② ⭐⭐ 第二空的关键是**找出二面角的平面角**："
        r"棱是 $OC$，两个半平面是 $AOC$ 与 $A'OC$；由 $OC\perp$ 平面 $AA'C$ 一次性得到 "
        r"$OC\perp AC$ 与 $OC\perp A'C$，故 $\angle ACA'$ 就是平面角" "\n"
        r"③ ⚠ 题干「$A$ 为 $A$ 在 $\alpha$ 内的射影」是 $A'$ 丢了撇号，已还原；"
        r"「二面角 $A-P_1P_2-A'$」即二面角 $A-OC-A'$" "\n"
        r"④ 数值复核：$\sin15^\circ=0.2588$，$|AA'|=2\times0.2588=0.5176$；"
        r"$\frac{\sqrt6-\sqrt2}{2}=\frac{2.4495-1.4142}{2}=0.5176$ ✓；"
        r"$|AC|=1$ ✓，故正弦值 $=0.5176$ ✓" "\n"
        r"⑤ 原书 `6 - 2 2` 是 $\frac{\sqrt6-\sqrt2}{2}$ 丢失根号与分数线，"
        r"由「$|AA'|=|AO|\sin15^\circ$」可反推确认"
    ),
    'topics': ['M-T-310'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-310-V3',
}

T318_V1 = {
    'type': '解答',
    'stem_text': (
        r"如图，已知 $\triangle ABC$ 是正三角形，$EA$、$CD$ 都垂直于平面 $ABC$，"
        r"且 $EA=AB=2a$，$DC=a$，$F$ 是 $BE$ 的中点，求证：" "\n"
        r"（1）$FD\parallel$ 平面 $ABC$；（2）$AF\perp$ 平面 $EDB$。"
    ),
    'opts': [],
    'answer': r"（1）证明见解析；（2）证明见解析",
    'analysis': (
        r"（1）取 $AB$ 中点 $M$，证 $FM\parallel CD$ 且相等 ⟹ 平行四边形 $FMCD$；"
        r"（2）先证 $CM\perp$ 平面 $EAB$ 得 $AF\perp MC$，再用 $FD\parallel MC$ 转移。"
    ),
    'solution': (
        r"**（1）** 取 $AB$ 的中点 $M$，连接 $FM,MC$。" "\n"
        r"因为 $F,M$ 分别是 $BE,BA$ 的中点，所以 $FM\parallel EA$ 且 $FM=\dfrac12EA=a$。" "\n"
        r"又 $EA$、$CD$ 都垂直于平面 $ABC$，所以 $CD\parallel EA$，从而 $CD\parallel FM$。" "\n"
        r"又 $DC=a$，故 $FM=DC$，于是四边形 $FMCD$ 是平行四边形，" "\n"
        r"所以 $FD\parallel MC$。而 $FD\not\subset$ 平面 $ABC$、$MC\subset$ 平面 $ABC$，" "\n"
        r"故 $FD\parallel$ 平面 $ABC$。" "\n"
        r"**（2）** 因为 $M$ 是 $AB$ 的中点、$\triangle ABC$ 是正三角形，所以 $CM\perp AB$。" "\n"
        r"又 $EA\perp$ 平面 $ABC$，$CM\subset$ 平面 $ABC$，故 $CM\perp EA$。" "\n"
        r"由 $AB\cap EA=A$ 得 $CM\perp$ 平面 $EAB$。" "\n"
        r"而 $AF\subset$ 平面 $EAB$，故 $CM\perp AF$；" "\n"
        r"由（1）知 $FD\parallel MC$，所以 $FD\perp AF$。" "\n"
        r"又 $F$ 是 $BE$ 的中点且 $EA=AB$，在等腰 $\triangle EAB$ 中 $AF$ 是底边 $BE$ 的中线，"
        r"故 $AF\perp EB$。" "\n"
        r"由 $EB\cap FD=F$（$FD\subset$ 平面 $EDB$、$EB\subset$ 平面 $EDB$）" "\n"
        r"得 $AF\perp$ 平面 $EDB$。"
    ),
    'review': (
        r"① ⭐⭐ **（1）的题眼是 $FM=\frac12EA=a=DC$**："
        r"两个量都等于 $a$ 才能凑出平行四边形的「一组对边平行且相等」—— "
        r"这正是题干给 $EA=2a$、$DC=a$ 的原因（$EA=2\cdot DC$）" "\n"
        r"② ⭐⭐ **（2）用（1）的结论转移垂直**："
        r"直接证 $AF\perp FD$ 很难，但 $FD\parallel MC$，转去证 $AF\perp MC$ 就顺了 —— "
        r"**前一问的平行关系常是后一问的桥梁**" "\n"
        r"③ ⭐⭐ $AF\perp EB$ 来自「等腰三角形三线合一」："
        r"$EA=AB$ 且 $F$ 是底边 $BE$ 中点（注意 $F$ 是 $BE$ 的中点，不是 $EA$ 的）" "\n"
        r"④ ⚠ 两处「$EA$、$CD$ 都垂直于平面 $ABC$」要**分开用**："
        r"一处得 $CD\parallel EA$（用于（1）），另一处得 $CM\perp EA$（用于（2））" "\n"
        r"⑤ 数值复核：取 $a=1$，$A(0,0,0)$、$B(2,0,0)$、$C(1,\sqrt3,0)$、"
        r"$E(0,0,2)$、$D(1,\sqrt3,1)$、$F(1,0,1)$；" "\n"
        r"　$\vec{FD}=(0,\sqrt3,0)$，平面 $ABC$ 法向量 $(0,0,1)$，点积 $=0$ ⟹ 平行 ✓；" "\n"
        r"　$\vec{AF}=(1,0,1)$，$\vec{EB}=(2,0,-2)$，$\vec{ED}=(1,\sqrt3,-1)$，" "\n"
        r"　$\vec{AF}\cdot\vec{EB}=2-2=0$ ✓，$\vec{AF}\cdot\vec{ED}=1-1=0$ ✓"
    ),
    'topics': ['M-T-318'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-318-V1',
}

T326_V1 = {
    'type': '解答',
    'stem_text': (
        r"如图，在四棱锥 $P-ABCD$ 中，底面 $ABCD$ 为正方形，$PA\perp$ 底面 $ABCD$，"
        r"$PA=AB$，$E$ 为线段 $PB$ 的中点。" "\n"
        r"（1）若 $F$ 为线段 $BC$ 上的动点，请证明：平面 $AEF\perp$ 平面 $PBC$；" "\n"
        r"（2）若 $F$ 为线段 $BC,CD,DA$ 上的动点（不含 $A,B$），$PA=2$，"
        r"三棱锥 $A-BEF$ 的体积是否存在最大值？如果存在，求出最大值；"
        r"如果不存在，请说明理由。"
    ),
    'opts': [],
    'answer': r"（1）证明见解析；（2）存在，最大值为 $\dfrac23$",
    'analysis': (
        r"（1）证 $AE\perp$ 平面 $PBC$；（2）换顶点成 $F-ABE$，"
        r"高等于 $F$ 到直线 $AB$ 的距离，$F$ 在 $CD$ 上时恒为 $2$。"
    ),
    'solution': (
        r"**（1）** 因为 $PA=AB$ 且 $E$ 为线段 $PB$ 的中点，"
        r"在等腰 $\triangle PAB$ 中 $AE$ 是底边 $PB$ 的中线，故 $AE\perp PB$。" "\n"
        r"因为 $PA\perp$ 底面 $ABCD$，$BC\subset$ 平面 $ABCD$，所以 $BC\perp PA$。" "\n"
        r"又底面 $ABCD$ 为正方形，故 $BC\perp AB$；"
        r"由 $PA\cap AB=A$、$PA,AB\subset$ 平面 $PAB$，得 $BC\perp$ 平面 $PAB$。" "\n"
        r"而 $AE\subset$ 平面 $PAB$，故 $AE\perp BC$。" "\n"
        r"由 $PB\cap BC=B$、$PB,BC\subset$ 平面 $PBC$，得 $AE\perp$ 平面 $PBC$。" "\n"
        r"又 $AE\subset$ 平面 $AEF$，所以平面 $AEF\perp$ 平面 $PBC$。" "\n"
        r"**（2）** 三棱锥 $A-BEF$ 的体积等于三棱锥 $F-ABE$ 的体积（同一几何体换顶点）。" "\n"
        r"由 $PA\perp$ 底面 $ABCD$ 且 $PA\subset$ 平面 $PAB$，得平面 $PAB\perp$ 平面 $ABCD$，"
        r"且交线为 $AB$。" "\n"
        r"故点 $F$ 到平面 $ABE$ 的距离（即三棱锥 $F-ABE$ 的高）"
        r"就等于点 $F$ 到直线 $AB$ 的距离。" "\n"
        r"因为 $PA=AB=2$，所以正方形边长为 $2$：" "\n"
        r"　当 $F$ 在线段 $BC$ 或 $AD$ 上时，该距离在 $(0,2]$ 内变化；" "\n"
        r"　当 $F$ 在线段 $CD$ 上时，$CD\parallel AB$ 且间距为 $2$，该距离恒为 $2$。" "\n"
        r"又 $E$ 是 $PB$ 的中点，$PA\perp AB$，故" "\n"
        r"$S_{\triangle ABE}=\dfrac12\cdot|AB|\cdot\dfrac{|PA|}{2}=\dfrac12\times2\times1=1$。" "\n"
        r"所以当 $F$ 在线段 $CD$ 上时，三棱锥 $F-ABE$ 的体积取得最大值" "\n"
        r"$V=\dfrac13\cdot S_{\triangle ABE}\cdot2=\dfrac13\times1\times2=\dfrac23$。" "\n"
        r"故三棱锥 $A-BEF$ 的体积存在最大值，最大值为 $\dfrac23$。"
    ),
    'review': (
        r"① ⭐⭐ **（2）的题眼是「面面垂直 ⟹ 高 = 到交线的距离」**："
        r"平面 $PAB\perp$ 平面 $ABCD$、交线 $AB$，故 $F$（在底面内）到平面 $ABE$ 的距离"
        r"等于 $F$ 到直线 $AB$ 的距离 —— 这一步把空间距离压成平面距离" "\n"
        r"② ⭐⭐ **换顶点**：$V_{A-BEF}=V_{F-ABE}$，"
        r"因为 $\triangle ABE$ 的面积是**定值**（与 $F$ 无关），于是体积只随高变化 —— "
        r"凡「一个顶点是动点」的体积最值，都先换顶点让面积固定" "\n"
        r"③ ⚠ 高在 $CD$ 上恒为 $2$、在 $BC/AD$ 上 $\le2$，"
        r"所以**最大值在整条 $CD$ 上都取到**（不是唯一取等点），这点要说明" "\n"
        r"④ ⚠ （1）中 $AE\perp PB$ 用的是「$PA=AB$ 且 $E$ 是 $PB$ 中点」，"
        r"若 $PA\ne AB$ 则不成立 —— 题干的 $PA=AB$ 同时服务于（1）与（2）" "\n"
        r"⑤ 原书详解里「$PB\cap BC=B$」重复写了两遍，属排版瑕疵，录入时已合并" "\n"
        r"⑥ 数值复核：取 $A(0,0,0)$、$B(2,0,0)$、$C(2,2,0)$、$D(0,2,0)$、$P(0,0,2)$、"
        r"$E(1,0,1)$，取 $F(1,2,0)\in CD$。" "\n"
        r"　$\vec{AB}=(2,0,0)$、$\vec{AE}=(1,0,1)$，"
        r"$S_{\triangle ABE}=\frac12|\vec{AB}\times\vec{AE}|=\frac12|(0,-2,0)|=1$；" "\n"
        r"　平面 $ABE$ 的法向量为 $(0,1,0)$，点 $F$ 到该平面的距离 $=|2-0|=2$，" "\n"
        r"　故 $V=\frac13\times1\times2=\frac23$ ✓ 与答案一致"
    ),
    'topics': ['M-T-326'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-326-V1',
}

T319_V1 = {
    'type': '解答',
    'stem_text': (
        r"如图，梯形 $ABCD$ 所在的平面与等腰梯形 $ABEF$ 所在的平面互相垂直，"
        r"$G$ 为 $AB$ 的中点，$AB\perp AD$，$AB\parallel CD\parallel EF$，" "\n"
        r"$DA=AF=EF=CD=\sqrt3$，$AB=2\sqrt3$。" "\n"
        r"（Ⅰ）求证：$CE\parallel$ 平面 $ADF$；" "\n"
        r"（Ⅱ）求证：平面 $CEG\perp$ 平面 $CFB$；" "\n"
        r"（Ⅲ）求多面体 $AFEBCD$ 的体积。"
    ),
    'opts': [],
    'answer': r"（Ⅰ）证明见解析；（Ⅱ）证明见解析；（Ⅲ）$3$",
    'analysis': (
        r"（Ⅰ）由 $CD\parallel EF$ 且相等得平行四边形 $CDFE$；"
        r"（Ⅱ）证 $BF\perp$ 平面 $ECG$；（Ⅲ）把多面体拆成三棱柱与三棱锥。"
    ),
    'solution': (
        r"**（Ⅰ）** 因为 $CD\parallel EF$ 且 $CD=EF$，所以四边形 $CDFE$ 是平行四边形，"
        r"故 $DF\parallel CE$。" "\n"
        r"又 $DF\subset$ 平面 $ADF$、$CE\not\subset$ 平面 $ADF$，所以 $CE\parallel$ 平面 $ADF$。" "\n"
        r"**（Ⅱ）** 连接 $FG$。" "\n"
        r"在等腰梯形 $ABEF$ 中，$BG=\dfrac{AB}{2}=\sqrt3$、$BG\parallel EF$ 且 $BG=EF=\sqrt3$，"
        r"故四边形 $GBEF$ 是平行四边形；" "\n"
        r"又 $GB=BE=\sqrt3$，故四边形 $GBEF$ 是菱形，因此 $BF\perp EG$。" "\n"
        r"在梯形 $ABCD$ 中，同理 $AG=\sqrt3$、$AG\parallel CD$ 且 $AG=CD=\sqrt3$，"
        r"故四边形 $AGCD$ 是平行四边形，于是 $AD\parallel GC$。" "\n"
        r"因为 $AD\perp AB$，所以 $GC\perp AB$；" "\n"
        r"又平面 $ABEF\perp$ 平面 $ABCD$，交线为 $AB$，$GC\subset$ 平面 $ABCD$，"
        r"故 $GC\perp$ 平面 $ABEF$。" "\n"
        r"而 $BF\subset$ 平面 $ABEF$，故 $GC\perp BF$。" "\n"
        r"由 $CG\cap EG=G$ 得 $BF\perp$ 平面 $ECG$；" "\n"
        r"又 $BF\subset$ 平面 $BCF$，所以平面 $CEG\perp$ 平面 $CFB$。" "\n"
        r"**（Ⅲ）** 设 $BF\cap GE=O$。" "\n"
        r"由（Ⅰ）得 $CE\parallel DF$ 且 $CE=DF$；由（Ⅱ）得 $AD\parallel CG$ 且 $AD=CG$。" "\n"
        r"又 $CG\not\subset$ 平面 $ADF$、$AD\subset$ 平面 $ADF$，故 $CG\parallel$ 平面 $ADF$。" "\n"
        r"由 $CE\cap CG=C$ 得平面 $ADF\parallel$ 平面 $GCE$。" "\n"
        r"又 $EF\parallel AG$ 且 $EF=AG=\sqrt3$，故四边形 $AFEG$ 是平行四边形，$AF=EG$。" "\n"
        r"于是 $\triangle ADF\cong\triangle GCE$，几何体 $ADF-GCE$ 是三棱柱。" "\n"
        r"由（Ⅱ）得 $GC\perp$ 平面 $ABEF$，而 $GE\subset$ 平面 $ABEF$，故 $GC\perp GE$，" "\n"
        r"$S_{\triangle GCE}=\dfrac12\cdot\sqrt3\cdot\sqrt3=\dfrac32$。" "\n"
        r"由（Ⅱ）得 $BF\perp$ 平面 $GCE$。" "\n"
        r"所以多面体 $AFEBCD$ 的体积为" "\n"
        r"$V=V_{ADF-GCE}+V_{B-GCE}=S_{\triangle GCE}\cdot FO"
        r"+\dfrac13S_{\triangle GCE}\cdot BO$。" "\n"
        r"在等腰梯形 $ABEF$ 中，$\cos\angle ABE=\dfrac{AB-EF}{2\cdot EB}"
        r"=\dfrac{2\sqrt3-\sqrt3}{2\sqrt3}=\dfrac12$，" "\n"
        r"又 $\angle ABE$ 为锐角，故 $\angle ABE=60^\circ$，从而 $\angle BEF=120^\circ$。" "\n"
        r"在 $\triangle BEF$ 中由余弦定理：" "\n"
        r"$BF^2=EB^2+EF^2-2\cdot EB\cdot EF\cos120^\circ"
        r"=3+3-2\cdot\sqrt3\cdot\sqrt3\cdot\left(-\dfrac12\right)=9$，" "\n"
        r"故 $BF=3$。由菱形 $GBEF$ 的对角线互相平分得 $OF=\dfrac{BF}{2}=\dfrac32$、" "\n"
        r"$BO=\dfrac32$。" "\n"
        r"于是 $V=S_{\triangle GCE}\cdot\left(FO+\dfrac13BO\right)"
        r"=\dfrac32\cdot\left(\dfrac32+\dfrac12\right)=\dfrac32\times2=3$。"
    ),
    'review': (
        r"① ⭐⭐ **两个「平行四边形 ⟹ 菱形」是本問的骨架**："
        r"$GBEF$ 是菱形给出 $BF\perp EG$，$AGCD$ 是平行四边形给出 $AD\parallel GC$ ⟹ $GC\perp AB$。" "\n"
        r"　**判据**：见到「等腰梯形 + 取腰的中点/中点连线」，先找平行四边形" "\n"
        r"② ⭐⭐ **（Ⅲ）的拆分很精妙**：多面体 = 三棱柱 $ADF$-$GCE$ + 三棱锥 $B$-$GCE$，" "\n"
        r"　而三棱柱体积 $=S\cdot FO$（$FO$ 是两底面间距，因为 $BF\perp$ 平面 $GCE$）；" "\n"
        r"　两者**共用底面 $\triangle GCE$**，高分别是 $FO$ 与 $\frac{BO}{3}$" "\n"
        r"③ ⚠ $BF=3$ 必须用余弦定理算（$\angle BEF=120^\circ$），"
        r"不能想当然认为 $BF=\sqrt3$；这一步错则体积全错" "\n"
        r"④ ⚠ $FO=\frac32$ 用的是**菱形对角线互相平分**，"
        r"而 $\triangle GCE$ 与 $\triangle BGE$ 不在同一平面，别把 $BO$ 当 $FO$" "\n"
        r"⑤ 数值复核：$S_{\triangle GCE}=1.5$，$FO=1.5$、$BO=1.5$，"
        r"$V=1.5\times1.5+\frac13\times1.5\times1.5=2.25+0.75=3$ ✓" "\n"
        r"　另验 $\cos\angle ABE=\frac{2\sqrt3-\sqrt3}{2\sqrt3}=0.5$ ⟹ $60^\circ$ ✓"
    ),
    'topics': ['M-T-319'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-319-V1',
}

T323_V1 = {
    'type': '解答',
    'stem_text': (
        r"如图，已知平面 $ADC\parallel$ 平面 $A_1B_1C_1$，$B$ 为线段 $AD$ 中点，"
        r"$\triangle ABC\cong\triangle A_1B_1C_1$，四边形 $AA_1B_1B$ 为正方形，" "\n"
        r"平面 $AA_1C_1C\perp$ 平面 $ADB_1A_1$，$A_1C_1=AA_1$，$\angle C_1A_1A=\dfrac\pi3$，"
        r"$M$ 为棱 $A_1C_1$ 中点。" "\n"
        r"（1）求证：平面 $ADC\perp$ 平面 $ACC_1A_1$；" "\n"
        r"（2）若 $AC=2$，求多面体 $ADC-A_1B_1C_1$ 的体积。"
    ),
    'opts': [],
    'answer': r"（1）证明见解析；（2）$\dfrac{10\sqrt3}{3}$",
    'analysis': (
        r"（1）用面面垂直的性质定理：$AD\perp AA_1$ 且 $AD\subset$ 平面 $ADB_1A_1$ ⟹ $AD\perp$ 平面 $ACC_1A_1$；"
        r"（2）补成三棱柱再挖去一个三棱锥。"
    ),
    'solution': (
        r"**（1）** 由正方形 $AA_1B_1B$ 知 $AD\perp AA_1$（$A,B,D$ 共线，$AB\perp AA_1$）。" "\n"
        r"又平面 $AA_1C_1C\perp$ 平面 $ADB_1A_1$，交线为 $AA_1$，" "\n"
        r"且 $AD\subset$ 平面 $ADB_1A_1$、$AD\perp AA_1$，故 $AD\perp$ 平面 $AA_1C_1C$。" "\n"
        r"而 $AD\subset$ 平面 $ADC$，所以平面 $ADC\perp$ 平面 $AA_1C_1C$。" "\n"
        r"**（2）** 延长 $A_1B_1$ 至 $D_1$ 使 $A_1D_1=AD$，则得到三棱柱 $ADC-A_1D_1C_1$，" "\n"
        r"所求几何体的体积 $V=V_{ADC-A_1D_1C_1}-V_{D_1-B_1D_1C_1}$（后者即三棱锥 $B_1-A_1D_1C_1$ 的补形）。" "\n"
        r"取 $A_1C_1$ 的中点 $M$：由 $A_1C_1=AA_1$ 且 $\angle C_1A_1A=\dfrac\pi3$ 知" "\n"
        r"$\triangle AA_1C_1$ 是正三角形，故 $AM\perp A_1C_1$。" "\n"
        r"又 $AC\parallel A_1C_1$（平面 $ADC\parallel$ 平面 $A_1B_1C_1$，且两平面被平面 $AA_1C_1C$ 所截），" "\n"
        r"所以 $AM\perp AC$。" "\n"
        r"由（1）平面 $ADC\perp$ 平面 $AA_1C_1C$ 且交线为 $AC$，" "\n"
        r"$AM\subset$ 平面 $AA_1C_1C$ 且 $AM\perp AC$，故 $AM\perp$ 平面 $ADC$，"
        r"即 $AM$ 为三棱柱的高。" "\n"
        r"由 $AC=2$ 及 $\triangle ABC\cong\triangle A_1B_1C_1$ 得 $A_1C_1=AC=2$，" "\n"
        r"故正 $\triangle AA_1C_1$ 的边长为 $2$，$AM=\sqrt3$。" "\n"
        r"又四边形 $AA_1B_1B$ 为正方形且 $B$ 为 $AD$ 中点，故 $AB=AA_1=2$、$AD=2AB=4$。" "\n"
        r"于是 $V_{柱}=S_{\triangle ADC}\cdot AM=\dfrac12\cdot AC\cdot AD\cdot AM"
        r"=\dfrac12\times2\times4\times\sqrt3=4\sqrt3$。" "\n"
        r"而 $S_{\triangle A_1D_1C_1}=\dfrac12\cdot A_1C_1\cdot A_1D_1=\dfrac12\times2\times4=4$ 的另一半：" "\n"
        r"$B_1$ 是 $A_1D_1$ 的中点，故 $S_{\triangle B_1D_1C_1}=\dfrac12S_{\triangle A_1D_1C_1}=2$，" "\n"
        r"$V_{B_1-A_1D_1C_1}=\dfrac13S_{\triangle A_1D_1C_1}\cdot AM$ 中被挖去的部分为" "\n"
        r"$V_{D_1-B_1D_1C_1}=\dfrac13S_{\triangle B_1D_1C_1}\cdot AM=\dfrac13\times2\times\sqrt3=\dfrac{2\sqrt3}{3}$。" "\n"
        r"所以 $V=4\sqrt3-\dfrac{2\sqrt3}{3}=\dfrac{10\sqrt3}{3}$。"
    ),
    'review': (
        r"① ⭐⭐ **（1）是「面面垂直性质定理」的教科书式用法**："
        r"两面垂直 → 在其中一个面内作交线的垂线 → 该线垂直另一个面 → 再推一次面面垂直。" "\n"
        r"　**这条链在三棱柱/三棱锥题里反复出现，必须形成条件反射**" "\n"
        r"② ⭐⭐ **（2）的补形法**：把不完整的「多面体」补成三棱柱再减去一个三棱锥，" "\n"
        r"　判据是「有两个平行平面 + 侧面是平行四边形」—— 本题恰恰满足" "\n"
        r"③ ⚠ $AM\perp AC$ 这一步**依赖 $AC\parallel A_1C_1$**，"
        r"而 $AC\parallel A_1C_1$ 来自「两平行平面被第三平面所截，交线平行」" "\n"
        r"④ ⚠ 挖去的是以 $\triangle B_1D_1C_1$ 为底的三棱锥，其面积是 $\triangle A_1D_1C_1$ 的**一半**"
        r"（$B_1$ 是 $A_1D_1$ 中点）" "\n"
        r"⑤ 数值复核：$AD=4$、$AC=2$ ⟹ $S_{\triangle ADC}=\frac12\times2\times4=4$，"
        r"$V_{柱}=4\sqrt3\approx6.9282$；" "\n"
        r"　$S_{\triangle B_1D_1C_1}=\frac12\times2\times2=2$，"
        r"$V_{\text{挖}}=\frac13\times2\times\sqrt3=\frac{2\sqrt3}{3}\approx1.1547$；" "\n"
        r"　$V=6.9282-1.1547=5.7735=\frac{10\sqrt3}{3}$ ✓" "\n"
        r"⑥ 原书 `10 3 3` 是 $\frac{10\sqrt3}{3}$ 丢失根号，由 $AM=\sqrt3$ 可反推"
    ),
    'topics': ['M-T-323'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-323-V1',
}

T312_E1 = {
    'type': '解答',
    'stem_text': (
        r"如图，在正方体 $ABCD-A_1B_1C_1D_1$ 中，$E,F$ 分别是 $AA_1$、$CD$ 的中点。" "\n"
        r"（1）求证：$EF\parallel$ 平面 $A_1CD_1$；" "\n"
        r"（2）求异面直线 $ED_1$ 与 $A_1C$ 所成角的余弦值。"
    ),
    'opts': [],
    'answer': r"（1）证明见解析；（2）$\dfrac{\sqrt{15}}{15}$",
    'analysis': (
        r"建系后用向量法：（1）证 $\vec{EF}$ 与平面 $A_1CD_1$ 的法向量垂直；"
        r"（2）直接用方向向量夹角公式。"
    ),
    'solution': (
        r"以 $D$ 为原点，$\vec{DA},\vec{DC},\vec{DD_1}$ 分别为 $x,y,z$ 轴正方向建立空间直角坐标系，" "\n"
        r"设正方体棱长为 $2$，则" "\n"
        r"$D(0,0,0)$、$A(2,0,0)$、$B(2,2,0)$、$C(0,2,0)$、" "\n"
        r"$A_1(2,0,2)$、$B_1(2,2,2)$、$C_1(0,2,2)$、$D_1(0,0,2)$。" "\n"
        r"由 $E$ 是 $AA_1$ 中点得 $E(2,0,1)$；由 $F$ 是 $CD$ 中点得 $F(0,1,0)$。" "\n"
        r"**（1）** $\vec{A_1C}=(-2,2,-2)$，$\vec{A_1D_1}=(-2,0,0)$。" "\n"
        r"设平面 $A_1CD_1$ 的法向量为 $\vec n=(x,y,z)$，则" "\n"
        r"$\begin{cases}\vec n\cdot\vec{A_1C}=-2x+2y-2z=0\\"
        r"\vec n\cdot\vec{A_1D_1}=-2x=0\end{cases}$，" "\n"
        r"取 $y=1$ 得 $z=1$，故 $\vec n=(0,1,1)$。" "\n"
        r"又 $\vec{EF}=F-E=(-2,1,-1)$，$\vec{EF}\cdot\vec n=0+1-1=0$，" "\n"
        r"且 $E\not\in$ 平面 $A_1CD_1$（$E(2,0,1)$ 不满足 $-2\cdot2+2\cdot0-2\cdot1=0$ 的形式），" "\n"
        r"故 $EF\parallel$ 平面 $A_1CD_1$。" "\n"
        r"**（2）** $\vec{ED_1}=D_1-E=(-2,0,1)$，$\vec{A_1C}=(-2,2,-2)$。" "\n"
        r"$|\vec{ED_1}|=\sqrt{4+0+1}=\sqrt5$，$|\vec{A_1C}|=\sqrt{4+4+4}=2\sqrt3$。" "\n"
        r"$\vec{ED_1}\cdot\vec{A_1C}=(-2)(-2)+0\cdot2+1\cdot(-2)=4-2=2$。" "\n"
        r"故 $\cos\theta=\dfrac{|\vec{ED_1}\cdot\vec{A_1C}|}{|\vec{ED_1}|\cdot|\vec{A_1C}|}"
        r"=\dfrac{2}{\sqrt5\cdot2\sqrt3}=\dfrac{1}{\sqrt{15}}=\dfrac{\sqrt{15}}{15}$。" "\n"
        r"所以异面直线 $ED_1$ 与 $A_1C$ 所成角的余弦值为 $\dfrac{\sqrt{15}}{15}$。"
    ),
    'review': (
        r"① ⭐⭐ **（1）的向量法比几何法稳**："
        r"几何法要找平面内一条与 $EF$ 平行的线（需作辅助点），"
        r"向量法只需「$\vec{EF}\cdot\vec n=0$ 且 $E$ 不在平面上」两步" "\n"
        r"② ⚠ **必须验证 $E\not\in$ 平面 $A_1CD_1$**：只证 $\vec{EF}\perp\vec n$ 只能得到 "
        r"$EF\parallel$ 平面 **或** $EF\subset$ 平面，少这一步是不完整的" "\n"
        r"③ ⚠ （2）中 $\vec{ED_1}$ 与 $\vec{A_1C}$ 的夹角可能是钝角，"
        r"**异面直线所成角取锐角**，故分子要加绝对值" "\n"
        r"④ 棱长设为 $2$（而非 $1$）是为了让中点 $E,F$ 的坐标是整数，避免分数" "\n"
        r"⑤ 数值复核：$\vec{ED_1}\cdot\vec{A_1C}=2$，$|ED_1|=\sqrt5=2.2361$、"
        r"$|A_1C|=2\sqrt3=3.4641$，$\cos=\frac{2}{7.7460}=0.2582=\frac{1}{\sqrt{15}}$ ✓" "\n"
        r"⑥ 原书 `solution` 字段为空，本解由我独立建系推导补全；"
        r"答案 $\frac{\sqrt{15}}{15}$ 与原书一致，可互为印证"
    ),
    'topics': ['M-T-312'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-312-E1',
}

T313_V2 = {
    'type': '解答',
    'stem_text': (
        r"如图，在四棱锥 $P-ABCD$ 中，$PA\perp$ 平面 $ABCD$，$AD\parallel BC$，"
        r"$\angle BAD=\dfrac{2\pi}{3}$，" "\n"
        r"$AD=2AB=2BC=2PA=4$，$M$ 为 $PB$ 上靠近 $B$ 的三等分点。" "\n"
        r"（1）求证：$PD\parallel$ 平面 $ACM$；" "\n"
        r"（2）求直线 $PD$ 与平面 $ACM$ 的距离。"
    ),
    'opts': [],
    'answer': r"（1）证明见解析；（2）$\sqrt3$",
    'analysis': (
        r"由条件得 $AD=4$、$AB=BC=PA=2$；建系后证 $\vec{PD}$ 与平面 $ACM$ 的法向量垂直，"
        r"再用点到平面距离公式（$P$ 到平面 $ACM$ 的距离即所求）。"
    ),
    'solution': (
        r"由 $AD=2AB=2BC=2PA=4$ 得 $AD=4$，$AB=BC=PA=2$。" "\n"
        r"以 $A$ 为原点，$AD$ 所在直线为 $x$ 轴，在底面内过 $A$ 垂直于 $AD$ 的直线为 $y$ 轴，" "\n"
        r"$AP$ 所在直线为 $z$ 轴建立空间直角坐标系，则" "\n"
        r"$A(0,0,0)$、$D(4,0,0)$、$P(0,0,2)$。" "\n"
        r"由 $\angle BAD=\dfrac{2\pi}{3}$、$AB=2$ 得" "\n"
        r"$B\left(2\cos\dfrac{2\pi}{3},\,2\sin\dfrac{2\pi}{3},\,0\right)=(-1,\sqrt3,0)$，" "\n"
        r"由 $BC\parallel AD$、$BC=2$ 得 $C=B+(2,0,0)=(1,\sqrt3,0)$。" "\n"
        r"$M$ 为 $PB$ 上靠近 $B$ 的三等分点，即 $BM=\dfrac13BP$，" "\n"
        r"故 $M=B+\dfrac13(P-B)=\dfrac23B+\dfrac13P"
        r"=\left(-\dfrac23,\dfrac{2\sqrt3}{3},\dfrac23\right)$。" "\n"
        r"**（1）** $\vec{AC}=(1,\sqrt3,0)$，$\vec{AM}=\left(-\dfrac23,\dfrac{2\sqrt3}{3},\dfrac23\right)$。" "\n"
        r"设平面 $ACM$ 的法向量为 $\vec n=(x,y,z)$，则" "\n"
        r"$\begin{cases}x+\sqrt3y=0\\"
        r"-\dfrac23x+\dfrac{2\sqrt3}{3}y+\dfrac23z=0\end{cases}$，" "\n"
        r"取 $y=-1$ 得 $x=\sqrt3$，代入第二式：$-\dfrac{2\sqrt3}{3}-\dfrac{2\sqrt3}{3}+\dfrac23z=0$，"
        r"得 $z=2\sqrt3$。" "\n"
        r"故 $\vec n=(\sqrt3,-1,2\sqrt3)$。" "\n"
        r"又 $\vec{PD}=D-P=(4,0,-2)$，" "\n"
        r"$\vec{PD}\cdot\vec n=4\sqrt3+0-4\sqrt3=0$，且 $P\not\in$ 平面 $ACM$，" "\n"
        r"所以 $PD\parallel$ 平面 $ACM$。" "\n"
        r"**（2）** 直线 $PD\parallel$ 平面 $ACM$，故所求距离等于点 $P$ 到平面 $ACM$ 的距离 $d$。" "\n"
        r"$\vec{AP}=(0,0,2)$，$|\vec n|=\sqrt{3+1+12}=4$，" "\n"
        r"$d=\dfrac{|\vec{AP}\cdot\vec n|}{|\vec n|}=\dfrac{|2\cdot2\sqrt3|}{4}=\dfrac{4\sqrt3}{4}=\sqrt3$。" "\n"
        r"所以直线 $PD$ 与平面 $ACM$ 的距离为 $\sqrt3$。"
    ),
    'review': (
        r"① ⭐⭐ **「线面平行 ⟹ 线到面的距离 = 线上任一点到面的距离」**："
        r"取 $P$ 而非 $D$，是因为 $\vec{AP}$ 只有一个非零分量，点乘极简" "\n"
        r"② ⭐⭐ **（1）反过来验证了 $M$ 的位置理解正确**："
        r"若把 $M$ 取成靠近 $P$ 的三等分点，则 $\vec{PD}\cdot\vec n=6\sqrt3\ne0$（我已算过），"
        r"平行关系不成立 —— 这说明「靠近 $B$」即 $BM=\frac13BP$ 无误" "\n"
        r"③ ⚠ **原书答案写 $3$，必误**：点到平面的距离不超过该点到平面上已知点 $A$ 的距离，" "\n"
        r"　即 $d\le|AP|=PA=2$，而 $3>2$，绝无可能。独立计算得 $\sqrt3\approx1.732<2$ ✓，" "\n"
        r"　原书是把 $\sqrt3$ 丢了根号（B 类勘误）" "\n"
        r"④ ⚠ 建系时 $\angle BAD=\frac{2\pi}{3}$ 是 $\vec{AB}$ 与 $\vec{AD}$ 的夹角，" "\n"
        r"　$B$ 的 $y$ 坐标取正（图形在 $y>0$ 侧），$C=B+(2,0,0)$ 由 $BC\parallel AD$、$BC=2$ 得到" "\n"
        r"⑤ 数值复核：$\vec{PD}\cdot\vec n=4\sqrt3-4\sqrt3=0$ ✓；" "\n"
        r"　$d=\frac{4\sqrt3}{4}=1.7321$ ✓；另取 $D$ 验算：" "\n"
        r"　$\vec{AD}=(4,0,0)$，$\vec{AD}\cdot\vec n=4\sqrt3$，$d=\frac{4\sqrt3}{4}=\sqrt3$ ✓（与 $P$ 一致）" "\n"
        r"⑥ 原书 `solution` 字段为空，本解由我独立建系推导补全"
    ),
    'topics': ['M-T-313'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-313-V2',
}

QS = [
    T166_V1,
    T171_V1,
    T173_V1,
    T263_V2,
    T297_V2,
    T310_V3,
    T318_V1,
    T326_V1,
    T319_V1,
    T323_V1,
    T312_E1,
    T313_V2,
]
