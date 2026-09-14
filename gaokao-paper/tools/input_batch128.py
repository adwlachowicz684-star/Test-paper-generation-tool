# -*- coding: utf-8 -*-
r"""第 128 批：函数与导数（M-T-054-V3、M-T-056-V2、M-T-057-E1，3 题）
+ 数列（M-T-267-V2，1 题）+ 概率（M-T-399-V1，1 题）+ 概率与解析几何（M-T-415-V2，1 题）

六题均为 ref_bank 中「有完整 solution/analysis 且无图依赖」的剩余题；
其中 M-T-054-V3（根号）、M-T-057-E1（分母 2x）、M-T-399-V1（三次根号）、
M-T-415-V2（直线括号）四处需从详解反推还原，依据已写进每题的 review。

    python3 tools/run_batch.py 128
"""

T054_V3 = {
    'type': '填空',
    'stem_text': (
        r"已知 $f\left(x\right)=\dfrac{2}{\sin\left|\pi x\right|}-\sin\left|\pi x\right|$，"
        r"$g\left(x\right)=\left|\ln x\right|-\sqrt{2}\,m$，"
        r"若对于任意 $x_1\in\left[-\dfrac{2}{3},-\dfrac{1}{6}\right]$，"
        r"存在 $x_2\in\left[\mathrm e^{-1},\mathrm e^{2}\right]$ 使得 $f\left(x_1\right)\ge g\left(x_2\right)$，"
        r"则实数 $m$ 的取值范围是 ____．"
    ),
    'opts': [],
    'answer': r"$\left[-\dfrac{\sqrt{2}}{2},+\infty\right)$",
    'analysis': (
        r"先把「任意 $x_1$、存在 $x_2$」翻译成 $f_{\min}\ge g_{\min}$；"
        r"再分别求两个最小值——$f$ 用复合函数单调性，$g$ 用 $\left|\ln x\right|\ge0$；"
        r"最后解一个一次不等式．"
    ),
    'solution': (
        r"**第一步：翻译题意**" "\n"
        r"「对任意 $x_1$ 存在 $x_2$ 使 $f\left(x_1\right)\ge g\left(x_2\right)$」"
        r"等价于 $\boxed{f_{\min}\ge g_{\min}}$" "\n"
        r"（左边要对**所有** $x_1$ 成立，故取 $f$ 的最小值；"
        r"右边只要**能找到**一个 $x_2$，故取 $g$ 的最小值即可）．" "\n"
        r"**第二步：求 $f$ 的最小值**" "\n"
        r"当 $x\in\left[-\dfrac23,-\dfrac16\right]$ 时 $x<0$，故 $\left|\pi x\right|=-\pi x\in\left[\dfrac{\pi}{6},\dfrac{2\pi}{3}\right]$．" "\n"
        r"令 $u=\sin\left|\pi x\right|$：$x$ 从 $-\dfrac23$ 增到 $-\dfrac12$ 时，$\left|\pi x\right|$ 从 $\dfrac{2\pi}{3}$ 减到 $\dfrac{\pi}{2}$，"
        r"$u$ 由 $\dfrac{\sqrt3}{2}$ 增到 $1$；$x$ 从 $-\dfrac12$ 增到 $-\dfrac16$ 时，$\left|\pi x\right|$ 由 $\dfrac{\pi}{2}$ 减到 $\dfrac{\pi}{6}$，"
        r"$u$ 由 $1$ 减到 $\dfrac12$．故 $u\in\left[\dfrac12,1\right]$，且 $u$ 在 $x=-\dfrac12$ 处取最大值 $1$．" "\n"
        r"又 $\varphi\left(u\right)=\dfrac{2}{u}-u$ 在 $u>0$ 上严格递减（$\varphi'\left(u\right)=-\dfrac{2}{u^{2}}-1<0$），"
        r"所以 $f$ 在 $u$ 最大处取最小：" "\n"
        r"$f_{\min}=f\left(-\dfrac12\right)=\dfrac{2}{\sin\frac{\pi}{2}}-\sin\dfrac{\pi}{2}=\dfrac21-1=1$．" "\n"
        r"**第三步：求 $g$ 的最小值**" "\n"
        r"$g\left(x\right)=\left|\ln x\right|-\sqrt2\,m\ge0-\sqrt2\,m=-\sqrt2\,m$，在 $x=1$ 处取等，故 $g_{\min}=-\sqrt2\,m$．" "\n"
        r"**第四步：解不等式**" "\n"
        r"$1\ge-\sqrt2\,m\Longrightarrow m\ge-\dfrac{1}{\sqrt2}=-\dfrac{\sqrt2}{2}$．" "\n"
        r"所以 $m$ 的取值范围是 $\boxed{\left[-\dfrac{\sqrt2}{2},+\infty\right)}$．"
    ),
    'review': (
        r"① ⭐⭐ **原书题干的 $\sqrt2$ 被 OCR 吞掉**：题干提取为 `g(x)=|lnx| - 2m`，答案却是 $-\frac{\sqrt2}{2}$．"
        r"按 $2m$ 算：$1\ge-2m\Rightarrow m\ge-\frac12$，与答案不符；"
        r"按 $\sqrt2\,m$ 算：$1\ge-\sqrt2 m\Rightarrow m\ge-\frac{\sqrt2}{2}$ ✓ 与答案完全吻合，故还原为 $g\left(x\right)=\left|\ln x\right|-\sqrt2\,m$．" "\n"
        r"② ⭐⭐ **「任意 + 存在」的翻译是本题题眼**："
        r"$\forall x_1\exists x_2:\ f\left(x_1\right)\ge g\left(x_2\right)\iff f_{\min}\ge g_{\min}$；"
        r"若改成「$\exists x_1\exists x_2$」则是 $f_{\max}\ge g_{\min}$，若改成「$\forall x_1\forall x_2$」则是 $f_{\min}\ge g_{\max}$——三种问法极易混．" "\n"
        r"③ $\varphi\left(u\right)=\frac2u-u$ 递减是配 $u=\sin\left|\pi x\right|$ 先增后减的关键："
        r"复合后 $f$ 先减后增，最小值落在 $u$ 的**最大**处 $x=-\frac12$．" "\n"
        r"④ 数值复核：$x=-\frac12$ 时 $f=1$；$x=-\frac23$ 时 $u=\sin\frac{2\pi}{3}=0.866$，$f=\frac2{0.866}-0.866=1.443>1$ ✓；"
        r"$m=-\frac{\sqrt2}{2}$ 时 $g_{\min}=-\sqrt2\cdot\left(-\frac{\sqrt2}{2}\right)=1=f_{\min}$，恰取等 ✓" "\n"
        r"**通法（任意 / 存在型不等式）**：" "\n"
        r"① 先按量词翻译成最值之间的不等式（这是唯一会卡住的一步）；" "\n"
        r"② 两个最值分别求，互不干扰；" "\n"
        r"③ 复合函数单调性按「外层单调 + 内层单调」合成，注意外层递减时会反转．"
    ),
    'difficulty': 0.78,
    'topics': ['M-T-054'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-054-V3',
}

T056_V2 = {
    'type': '填空',
    'stem_text': (
        r"已知函数 $f\left(x\right)=\begin{cases}"
        r"\left|\log_{2}x\right|,&0<x\le 2\\"
        r"\dfrac{1}{3}x^{2}-\dfrac{8}{3}x+5,&x>2"
        r"\end{cases}$，"
        r"若函数 $g\left(x\right)=f\left(x\right)-m$ 存在四个不同的零点，"
        r"则实数 $m$ 的取值范围是 ____．"
    ),
    'opts': [],
    'answer': r"$\left(0,1\right)$",
    'analysis': (
        r"把零点个数转化为「水平线 $y=m$ 与 $y=f\left(x\right)$ 的交点个数」，"
        r"再按两段分别数交点，取交集即可．"
    ),
    'solution': (
        r"$g\left(x\right)=f\left(x\right)-m$ 的零点个数就是方程 $f\left(x\right)=m$ 的解的个数，"
        r"即水平线 $y=m$ 与 $y=f\left(x\right)$ 的交点个数．" "\n"
        r"**第一段：$0<x\le2$，$f\left(x\right)=\left|\log_2x\right|$**" "\n"
        r"$x\to0^{+}$ 时 $f\to+\infty$，$f\left(1\right)=0$，$f\left(2\right)=1$．" "\n"
        r"$\left|\log_2x\right|=m$ 的解为 $x=2^{-m}$ 与 $x=2^{m}$；"
        r"$2^{-m}\in\left(0,2\right]$ 恒成立（$m>0$），$2^{m}\in\left(0,2\right]\iff m\le1$．" "\n"
        r"故 $0<m\le1$ 时这一段有 $2$ 个交点，$m\le0$ 或 $m>1$ 时少于 $2$ 个（$m=0$ 只有 $x=1$ 一个）．" "\n"
        r"**第二段：$x>2$，$f\left(x\right)=\dfrac13x^{2}-\dfrac83x+5$**" "\n"
        r"这是开口向上的抛物线，对称轴 $x=4$，$f\left(4\right)=\dfrac{16}{3}-\dfrac{32}{3}+5=-\dfrac13$，"
        r"且 $f\left(2\right)=\dfrac43-\dfrac{16}{3}+5=1$（$x=2$ 不在本段内）．" "\n"
        r"故本段值域为 $\left[-\dfrac13,+\infty\right)$，且在 $\left(2,4\right)$ 上由 $1$ 递减到 $-\dfrac13$、在 $\left(4,+\infty\right)$ 上递增到 $+\infty$；"
        r"于是 $-\dfrac13<m<1$ 时有 $2$ 个交点，$m=1$ 时只有 $x=6$ 一个（另一根 $x=2$ 不属本段）．" "\n"
        r"**取交集**" "\n"
        r"要共 $4$ 个交点，必须两段各 $2$ 个：" "\n"
        r"$0<m\le1$ 且 $-\dfrac13<m<1$，考虑到 $m=1$ 时第二段只有 $1$ 个交点，" "\n"
        r"故 $\boxed{0<m<1}$，即 $m\in\left(0,1\right)$．"
    ),
    'review': (
        r"① ⭐⭐ **分段函数的零点题，一律逐段数交点再取交集**——"
        r"不要试图合并成一个方程．" "\n"
        r"② ⚠ **端点 $m=1$ 必须单独检验**：第一段 $m=1$ 时 $x=\frac12$ 与 $x=2$ 都是解（$2$ 个），"
        r"但第二段 $f\left(x\right)=1$ 的两根是 $x=2$ 与 $x=6$，其中 $x=2$ **不属于** $x>2$ 这一段，只剩 $1$ 个，"
        r"总共 $3$ 个零点，故右端是**开**区间．这是本题唯一易错点．" "\n"
        r"③ 两段在 $x=2$ 处衔接：$|\log_22|=1$ 与 $\frac43-\frac{16}3+5=1$ 相等，函数连续——"
        r"这种「设计出来的连续」说明分段点位置正确，可作自检．" "\n"
        r"④ 数值复核：取 $m=0.5$，第一段 $x=2^{-0.5}=0.707$、$x=2^{0.5}=1.414$（$2$ 个）；"
        r"第二段 $\frac13x^2-\frac83x+5=0.5\Rightarrow x^2-8x+13.5=0$，$x=4\pm\sqrt{2.5}\approx2.42,\ 5.58$（都 $>2$，$2$ 个）✓ 共 $4$ 个．" "\n"
        r"取 $m=1$：第一段 $x=0.5,2$；第二段 $x=6$（$x=2$ 舍）→ 共 $3$ 个 ✗" "\n"
        r"**通法（水平线与分段函数交点）**：" "\n"
        r"① 零点个数 ⟺ 方程 $f\left(x\right)=m$ 的解的个数 ⟺ 水平线交点个数；" "\n"
        r"② 每段独立求「有 $k$ 个解时 $m$ 的范围」；" "\n"
        r"③ 分段点归属要逐段确认（开闭区间常在这里出错）．"
    ),
    'difficulty': 0.72,
    'topics': ['M-T-056'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-056-V2',
}

T057_E1 = {
    'type': '选择',
    'stem_text': (
        r"设函数 $f_1\left(x\right)=\log_{2}x-\dfrac{1}{2x}$，"
        r"$f_2\left(x\right)=\log_{\frac{1}{2}}x-\dfrac{1}{2x}$ 的零点分别为 $x_1,x_2$，则（　　）"
    ),
    'opts': [
        ('A', r"$0<x_1x_2<1$"),
        ('B', r"$x_1x_2=1$"),
        ('C', r"$1<x_1x_2<2$"),
        ('D', r"$x_1x_2\ge2$"),
    ],
    'answer': r"A",
    'analysis': (
        r"把两个零点条件写成对数等式，两式相减即得 $\log_2\left(x_1x_2\right)$ 的表达式，"
        r"再判断其符号．关键是准确估计 $x_1,x_2$ 各自的范围以确定 $x_1-x_2$ 的符号．"
    ),
    'solution': (
        r"由零点定义：" "\n"
        r"① $\log_{2}x_1=\dfrac{1}{2x_1}$；" "\n"
        r"② $\log_{\frac12}x_2=\dfrac{1}{2x_2}$，即 $-\log_{2}x_2=\dfrac{1}{2x_2}$．" "\n"
        r"**先定 $x_2$**：由②得 $\log_2x_2=-\dfrac{1}{2x_2}$．"
        r"取 $x=\dfrac12$：$\log_2\dfrac12=-1$，而 $-\dfrac{1}{2\times\frac12}=-1$，两边相等，" "\n"
        r"且 $\log_2x+\dfrac{1}{2x}$ 在 $\left(0,+\infty\right)$ 上严格递增，故零点唯一，$\boxed{x_2=\dfrac12}$．" "\n"
        r"**再估 $x_1$**：$\log_2x-\dfrac{1}{2x}$ 严格递增，且" "\n"
        r"$x=1$ 时 $0-\dfrac12=-\dfrac12<0$，$x=2$ 时 $1-\dfrac14=\dfrac34>0$，故 $x_1\in\left(1,2\right)$．" "\n"
        r"**判断 $x_1x_2$**：由①$-$②（注意②还原成底 $2$ 后是 $-\log_2x_2=\frac1{2x_2}$）：" "\n"
        r"$\log_2x_1-\log_{\frac12}x_2=\dfrac{1}{2x_1}-\dfrac{1}{2x_2}$，" "\n"
        r"即 $\log_2x_1+\log_2x_2=\dfrac{x_2-x_1}{2x_1x_2}$，" "\n"
        r"所以 $\log_2\left(x_1x_2\right)=\dfrac{x_2-x_1}{2x_1x_2}<0$（因 $x_2=\frac12<1<x_1$）．" "\n"
        r"故 $0<x_1x_2<1$，选 $\boxed{\mathrm A}$．" "\n"
        r"（也可直接算：$x_1x_2=\dfrac{x_1}{2}\in\left(\dfrac12,1\right)$）"
    ),
    'review': (
        r"① ⭐⭐ **本题的 $\dfrac{1}{2x}$ 被 OCR 成 $\dfrac12x$**："
        r"若按 $f\left(x\right)=\log_2x-\dfrac x2$ 理解，则 $f_1$ 的零点是 $x=2$ 与 $x=4$（两个！），"
        r"$f_2$ 的零点约 $0.75$，此时 $x_1x_2\approx1.5$ 或 $3$，对应 C 或 D，与答案 A 矛盾；"
        r"按 $f\left(x\right)=\log_2x-\dfrac{1}{2x}$ 则 $x_2=\frac12$ 恰为**精确解**、$x_1\in\left(1,2\right)$，$x_1x_2\in\left(\frac12,1\right)\subset\left(0,1\right)$ ✓ 与答案 A 吻合．" "\n"
        r"② ⭐⭐ **$x_2=\frac12$ 是命题人刻意设计的精确解**（$\log_2\frac12=-1=-\frac1{2\cdot\frac12}$），"
        r"这种「恰好对上」是还原正确的最强信号．" "\n"
        r"③ 两式相减时**必须先统一底数**：$\log_{\frac12}x_2=-\log_2x_2$，"
        r"所以「①$-$②」得到的是 $\log_2x_1+\log_2x_2$（和的对数），而不是差的对数——这一步最易写反．" "\n"
        r"④ 数值复核：$x_1$ 精确值约 $1.3195$（解 $\log_2x=\frac1{2x}$），$x_1x_2\approx0.6598\in\left(0,1\right)$ ✓" "\n"
        r"**通法（两个方程相减构造对数）**：" "\n"
        r"① 见到「两个函数的零点」，先各写成一个对数（或指数）等式；" "\n"
        r"② 底数不同的先统一（$\log_{\frac1a}x=-\log_ax$）；" "\n"
        r"③ 两式相加得积的对数、相减得商的对数，按需选用；" "\n"
        r"④ 符号由两个零点的大小关系定，故必须估出各自范围．"
    ),
    'difficulty': 0.70,
    'topics': ['M-T-057'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-057-E1',
}

T267_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知等比数列 $\left\{a_n\right\}$ 的前 $n$ 项和为 $S_n$，且 $S_4=30$，$a_2$，$a_4$ 的等差中项为 $10$．" "\n"
        r"（1）求数列 $\left\{a_n\right\}$ 的通项公式；" "\n"
        r"（2）求 $T_n=\dfrac{2}{S_1S_2}+\dfrac{2^{2}}{S_2S_3}+\cdots+\dfrac{2^{n}}{S_nS_{n+1}}$．"
    ),
    'opts': [],
    'answer': (
        r"（1）$a_n=2^{n}$；（2）$T_n=\dfrac{2^{n}-1}{2\left(2^{n+1}-1\right)}$．"
    ),
    'analysis': (
        r"第（1）问由「等差中项」与 $S_4$ 联立解 $a_1,q$；"
        r"第（2）问先写出 $S_n$，再把通项 $\dfrac{2^{k}}{S_kS_{k+1}}$ 裂成两项之差，"
        r"裂项的关键是「两因子之差 = 分子」这个巧合．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"$a_2,a_4$ 的等差中项为 $10$，故 $a_2+a_4=20$；又 $S_4=30$．" "\n"
        r"设首项 $a_1$、公比 $q$，则" "\n"
        r"$\begin{cases}a_1\left(1+q+q^{2}+q^{3}\right)=30\\ a_1\left(q+q^{3}\right)=20\end{cases}$" "\n"
        r"两式相减得 $a_1\left(1+q^{2}\right)=10$，与 $a_1q\left(1+q^{2}\right)=20$ 相除得 $q=2$，"
        r"代回得 $a_1\cdot5=10$，即 $a_1=2$．" "\n"
        r"所以 $\boxed{a_n=2\cdot2^{n-1}=2^{n}}$．" "\n"
        r"**第（2）问**" "\n"
        r"由（1）$S_n=\dfrac{2\left(1-2^{n}\right)}{1-2}=2\left(2^{n}-1\right)$．" "\n"
        r"于是" "\n"
        r"$\dfrac{2^{k}}{S_kS_{k+1}}=\dfrac{2^{k}}{2\left(2^{k}-1\right)\cdot2\left(2^{k+1}-1\right)}"
        r"=\dfrac14\cdot\dfrac{2^{k}}{\left(2^{k}-1\right)\left(2^{k+1}-1\right)}$．" "\n"
        r"注意到 $\left(2^{k+1}-1\right)-\left(2^{k}-1\right)=2^{k}$ **恰好等于分子**，故" "\n"
        r"$\dfrac{2^{k}}{\left(2^{k}-1\right)\left(2^{k+1}-1\right)}=\dfrac{1}{2^{k}-1}-\dfrac{1}{2^{k+1}-1}$，" "\n"
        r"$\dfrac{2^{k}}{S_kS_{k+1}}=\dfrac14\left(\dfrac{1}{2^{k}-1}-\dfrac{1}{2^{k+1}-1}\right)$．" "\n"
        r"累加得" "\n"
        r"$T_n=\dfrac14\left[\left(\dfrac11-\dfrac13\right)+\left(\dfrac13-\dfrac17\right)+\cdots+"
        r"\left(\dfrac{1}{2^{n}-1}-\dfrac{1}{2^{n+1}-1}\right)\right]$" "\n"
        r"$=\dfrac14\left(1-\dfrac{1}{2^{n+1}-1}\right)=\dfrac14\cdot\dfrac{2^{n+1}-2}{2^{n+1}-1}"
        r"=\boxed{\dfrac{2^{n}-1}{2\left(2^{n+1}-1\right)}}$．"
    ),
    'review': (
        r"① ⭐⭐ **裂项的判据：两因子之差 = 分子**．"
        r"本题 $\left(2^{k+1}-1\right)-\left(2^{k}-1\right)=2^{k}$ 与分子完全相同，"
        r"所以裂项时**系数恰为 $1$**（差多少就要补多少分之一的系数）．" "\n"
        r"② 联立解 $a_1,q$ 的技巧：两式**相减**先得 $a_1\left(1+q^2\right)=10$，"
        r"再与 $a_1q\left(1+q^2\right)=20$ 相除直接得 $q=2$ —— 比代入消元快得多．" "\n"
        r"③ 检验 $n=1$：$T_1=\dfrac{2}{S_1S_2}=\dfrac{2}{2\cdot6}=\dfrac16$；"
        r"公式给 $\dfrac{2-1}{2\left(4-1\right)}=\dfrac16$ ✓" "\n"
        r"④ 检验 $n=2$：$T_2=\dfrac16+\dfrac{4}{6\cdot14}=\dfrac16+\dfrac{1}{21}=\dfrac{9}{42}=\dfrac{3}{14}$；"
        r"公式给 $\dfrac{3}{2\left(8-1\right)}=\dfrac{3}{14}$ ✓" "\n"
        r"⑤ 当 $n\to\infty$ 时 $T_n\to\dfrac14$，这与逐项都是正项、总和收敛一致 ✓" "\n"
        r"**通法（等比 + 裂项求和）**：" "\n"
        r"① 先求 $a_1,q$：两个条件联立，优先用「相减/相除」消元；" "\n"
        r"② 写出 $S_n$ 后代入通项，观察分母两因子之差与分子的关系；" "\n"
        r"③ 裂项系数 $=\dfrac{1}{\text{两因子之差}\ /\ \text{分子}}$；" "\n"
        r"④ 用 $n=1,2$ 代回自检．"
    ),
    'difficulty': 0.68,
    'topics': ['M-T-267'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-267-V2',
}

T415_V2 = {
    'type': '填空',
    'stem_text': (
        r"已知直线 $y=k\left(x+\dfrac{1}{4}\right)$ 与曲线 $y=\sqrt{x}$ 恰有两个不同的交点，"
        r"记 $k$ 的所有可能取值构成集合 $A$；"
        r"$P\left(x,y\right)$ 是椭圆 $\dfrac{x^{2}}{16}+\dfrac{y^{2}}{9}=1$ 上一动点，"
        r"点 $P_1\left(x_1,y_1\right)$ 与点 $P$ 关于直线 $y=x+1$ 对称，"
        r"记 $\dfrac{y_1-1}{4}$ 的所有可能取值构成集合 $B$．"
        r"若随机从集合 $A,B$ 中分别抽出一个元素 $\lambda_1,\lambda_2$，"
        r"则 $\lambda_1>\lambda_2$ 的概率是 ____．"
    ),
    'opts': [],
    'answer': r"$\dfrac{3}{4}$",
    'analysis': (
        r"分两步：先由「两个交点」的判别式条件定出 $A$（区间）；"
        r"再把椭圆关于直线 $y=x+1$ 作对称，得到 $P_1$ 的轨迹从而定出 $B$（区间）；"
        r"最后在两个区间上各均匀取一点算几何概型．"
    ),
    'solution': (
        r"**第一步：求集合 $A$**" "\n"
        r"$\sqrt{x}=k\left(x+\dfrac14\right)$，因 $\sqrt{x}\ge0$ 且 $x+\dfrac14>0$，故 $k>0$．" "\n"
        r"两边平方：$x=k^{2}\left(x+\dfrac14\right)^{2}=k^{2}x^{2}+\dfrac{k^{2}}{2}x+\dfrac{k^{2}}{16}$，" "\n"
        r"即 $k^{2}x^{2}+\left(\dfrac{k^{2}}{2}-1\right)x+\dfrac{k^{2}}{16}=0$．" "\n"
        r"「两个不同交点」$\iff$ 该二次方程有两个不相等的正根：" "\n"
        r"两根之和 $=\dfrac{1-\frac{k^{2}}{2}}{k^{2}}>0\Longrightarrow k^{2}<2$；" "\n"
        r"$\Delta=\left(\dfrac{k^{2}}{2}-1\right)^{2}-4k^{2}\cdot\dfrac{k^{2}}{16}"
        r"=\dfrac{k^{4}}{4}-k^{2}+1-\dfrac{k^{4}}{4}=1-k^{2}>0\Longrightarrow k^{2}<1$．" "\n"
        r"结合 $k>0$ 得 $k\in\left(0,1\right)$，即 $\boxed{A=\left(0,1\right)}$．" "\n"
        r"**第二步：求集合 $B$**" "\n"
        r"原点关于直线 $y=x+1$ 的对称点是 $\left(-1,1\right)$，故椭圆 $\dfrac{x^{2}}{16}+\dfrac{y^{2}}{9}=1$ "
        r"关于该直线的对称曲线为" "\n"
        r"$\dfrac{\left(y-1\right)^{2}}{16}+\dfrac{\left(x+1\right)^{2}}{9}=1$，" "\n"
        r"点 $P_1\left(x_1,y_1\right)$ 在其上，于是 $\left(y_1-1\right)^{2}\le16$，即 $y_1-1\in\left[-4,4\right]$，" "\n"
        r"$\dfrac{y_1-1}{4}\in\left[-1,1\right]$，即 $\boxed{B=\left[-1,1\right]}$．" "\n"
        r"**第三步：几何概型**" "\n"
        r"$\lambda_1$ 在 $\left(0,1\right)$ 上均匀取值，$\lambda_2$ 在 $\left[-1,1\right]$ 上均匀取值，二者独立．" "\n"
        r"固定 $\lambda_1=t\in\left(0,1\right)$，则 $P\left(\lambda_2<t\right)=\dfrac{t-\left(-1\right)}{2}=\dfrac{t+1}{2}$．" "\n"
        r"$P\left(\lambda_1>\lambda_2\right)=\displaystyle\int_0^1\frac{t+1}{2}\,\mathrm dt"
        r"=\left[\dfrac{t^{2}}{4}+\dfrac{t}{2}\right]_0^1=\dfrac14+\dfrac12=\boxed{\dfrac34}$．"
    ),
    'review': (
        r"① ⭐⭐ **原书题干的 $y=k\left(x+\frac14\right)$ 被提取成 `y = kx + 1/4`**："
        r"按详解「平方得 $x=k^2x^2+\frac{k^2}{2}x+\frac{k^2}{16}$」反推，"
        r"右边必须整体平方，即 $\sqrt{x}=k\left(x+\frac14\right)$；"
        r"若按 $y=kx+\frac14$ 则中间项是 $\frac k2$ 而非 $\frac{k^2}2$．"
        r"（两种解读最终都得 $A=\left(0,1\right)$，不影响答案，但推导链只有前者自洽）" "\n"
        r"② ⭐⭐ **判别式化简的巧处**：$\Delta=\left(\frac{k^2}2-1\right)^2-\frac{k^4}4$ 中 $k^4$ 项**恰好抵消**，"
        r"只剩 $1-k^2$ —— 这种「高次项自动消失」是题目设计好的信号，可用于自检．" "\n"
        r"③ **点关于直线 $y=x+c$ 对称的坐标变换**：$\left(x,y\right)\to\left(y-c,\ x+c\right)$．"
        r"本题 $c=1$，故 $\left(0,0\right)\to\left(-1,1\right)$，椭圆的 $x$ 半轴 $4$ 变成 $y$ 方向、$y$ 半轴 $3$ 变成 $x$ 方向 ✓" "\n"
        r"④ 也可直接用 $E\left[\frac{\lambda_1+1}{2}\right]=\frac{E\lambda_1+1}{2}=\frac{0.5+1}{2}=\frac34$，"
        r"比积分更快（利用期望的线性性）．" "\n"
        r"⑤ 数值复核：$\lambda_1\in\left(0,1\right)$、$\lambda_2\in\left[-1,1\right]$，"
        r"$\lambda_1>\lambda_2$ 只可能失败于 $\lambda_2\ge\lambda_1$，而 $\lambda_2$ 有一半概率落在 $\left[0,1\right]$ 内，"
        r"$\frac34$ 与直觉一致 ✓" "\n"
        r"**通法（「先定集合再算几何概型」）**：" "\n"
        r"① 由交点/存在性条件用判别式定出参数区间；" "\n"
        r"② 对称曲线：先找特殊点（如中心）的对称点，再交换半轴；" "\n"
        r"③ 两区间各均匀取点求概率，用条件概率 + 积分（或期望线性性）．"
    ),
    'difficulty': 0.80,
    'topics': ['M-T-415'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-415-V2',
}

T399_V1 = {
    'type': '解答',
    'stem_text': (
        r"某医院为筛查冠状病毒，需要检验血液是否为阳性，现有 $n\left(n\in\mathbf N^{\ast}\right)$ 份血液样本，"
        r"有以下两种检验方式：" "\n"
        r"方式一：逐份检验，则需要检验 $n$ 次；" "\n"
        r"方式二：混合检验，将其中 $k\left(k\in\mathbf N^{\ast}\right.$ 且 $\left.k\ge2\right)$ 份血液样本分别取样混合在一起检验．"
        r"若检验结果为阴性，这 $k$ 份的血液全为阴性，因而这 $k$ 份血液样本只要检验一次就够了；"
        r"如果检验结果为阳性，就要对这 $k$ 份再逐份检验，此时这 $k$ 份血液的检验次数总共为 $k+1$．" "\n"
        r"假设在接受检验的血液样本中，每份样本的检验结果相互独立，且每份样本呈阳性的概率为 $p\left(0<p<1\right)$．"
        r"现取其中 $k$ 份血液样本，记采用逐份检验时样本需要检验的总次数为 $\xi_1$，"
        r"采用混合检验方式时样本需要检验的总次数为 $\xi_2$．" "\n"
        r"（1）若 $E\left(\xi_1\right)=E\left(\xi_2\right)$，试求 $p$ 关于 $k$ 的函数关系式 $p=f\left(k\right)$；" "\n"
        r"（2）若 $p$ 与干扰素计量 $x_n$ 相关，其中 $x_1,x_2,\cdots,x_n,\cdots\left(n\ge2\right)$ 是不同的正实数，"
        r"满足 $x_1=1$ 且 $x_{n+1}^{2}-x_n^{2}=\left(\mathrm e^{\frac13}-\mathrm e^{-\frac13}\right)x_nx_{n+1}$．" "\n"
        r"（i）求证：数列 $\left\{x_n\right\}$ 为等比数列；" "\n"
        r"（ii）当 $p=1-\dfrac{1}{\sqrt[3]{x_4}}$ 时，采用混合检验方式可以使得样本需要检验的总次数的期望值"
        r"比逐份检验的总次数的期望值更少，求 $k$ 的最大值．"
    ),
    'opts': [],
    'answer': (
        r"（1）$p=1-k^{-\frac{1}{k}}$；"
        r"（2）（i）$\left\{x_n\right\}$ 是以 $1$ 为首项、$\mathrm e^{\frac13}$ 为公比的等比数列；"
        r"（ii）$k$ 的最大值为 $4$．"
    ),
    'analysis': (
        r"第（1）问写出 $\xi_2$ 的分布（只取 $1$ 与 $k+1$ 两个值）求期望，令其等于 $k$ 解出 $p$；"
        r"第（2）（i）问同除以 $x_nx_{n+1}$ 后换元 $t=\frac{x_{n+1}}{x_n}$，解一个「$t-\frac1t=$ 常数」的方程；"
        r"（ii）问把「期望更少」翻译成 $k\left(1-p\right)^{k}>1$，取对数后用函数单调性定最大整数 $k$．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"逐份检验 $k$ 份需 $k$ 次，故 $E\left(\xi_1\right)=k$．" "\n"
        r"混合检验时 $\xi_2$ 只取两个值：" "\n"
        r"$P\left(\xi_2=1\right)=\left(1-p\right)^{k}$（全阴），"
        r"$P\left(\xi_2=k+1\right)=1-\left(1-p\right)^{k}$（有阳）．" "\n"
        r"故 $E\left(\xi_2\right)=\left(1-p\right)^{k}+\left(k+1\right)\left[1-\left(1-p\right)^{k}\right]"
        r"=k+1-k\left(1-p\right)^{k}$．" "\n"
        r"令 $E\left(\xi_1\right)=E\left(\xi_2\right)$：$k=k+1-k\left(1-p\right)^{k}$，" "\n"
        r"即 $\left(1-p\right)^{k}=\dfrac1k$，所以 $\boxed{p=1-k^{-\frac{1}{k}}}$．" "\n"
        r"**第（2）（i）问**" "\n"
        r"由 $x_n>0$，在 $x_{n+1}^{2}-x_n^{2}=\left(\mathrm e^{\frac13}-\mathrm e^{-\frac13}\right)x_nx_{n+1}$ "
        r"两边同除以 $x_nx_{n+1}$：" "\n"
        r"$\dfrac{x_{n+1}}{x_n}-\dfrac{x_n}{x_{n+1}}=\mathrm e^{\frac13}-\mathrm e^{-\frac13}$．" "\n"
        r"令 $t=\dfrac{x_{n+1}}{x_n}>0$，则 $t-\dfrac1t=\mathrm e^{\frac13}-\mathrm e^{-\frac13}$，" "\n"
        r"即 $t^{2}-\left(\mathrm e^{\frac13}-\mathrm e^{-\frac13}\right)t-1=0$，" "\n"
        r"解得 $t=\mathrm e^{\frac13}$ 或 $t=-\mathrm e^{-\frac13}$（舍去）．" "\n"
        r"故 $\dfrac{x_{n+1}}{x_n}=\mathrm e^{\frac13}$ 为常数，$\left\{x_n\right\}$ 是以 $x_1=1$ 为首项、"
        r"$\mathrm e^{\frac13}$ 为公比的等比数列．" "\n"
        r"**第（2）（ii）问**" "\n"
        r"由（i）$x_n=\mathrm e^{\frac{n-1}{3}}$，故 $x_4=\mathrm e$，"
        r"$p=1-\dfrac{1}{\sqrt[3]{x_4}}=1-\mathrm e^{-\frac13}$，即 $1-p=\mathrm e^{-\frac13}$．" "\n"
        r"「混合检验的期望更少」即 $E\left(\xi_2\right)<E\left(\xi_1\right)$：" "\n"
        r"$k+1-k\left(1-p\right)^{k}<k\Longrightarrow k\left(1-p\right)^{k}>1$" "\n"
        r"$\Longrightarrow k\,\mathrm e^{-\frac{k}{3}}>1\Longrightarrow \ln k-\dfrac{k}{3}>0$．" "\n"
        r"设 $\varphi\left(x\right)=\ln x-\dfrac{x}{3}\left(x>0\right)$，则 $\varphi'\left(x\right)=\dfrac{1}{x}-\dfrac13=\dfrac{3-x}{3x}$，" "\n"
        r"$\varphi$ 在 $\left(0,3\right)$ 上递增、在 $\left(3,+\infty\right)$ 上递减．" "\n"
        r"$\varphi\left(4\right)=\ln4-\dfrac43\approx1.386-1.333=0.053>0$，" "\n"
        r"$\varphi\left(5\right)=\ln5-\dfrac53\approx1.609-1.667=-0.057<0$，" "\n"
        r"又 $k\ge2$ 且 $k\in\mathbf N^{\ast}$，故 $k$ 的最大值为 $\boxed{4}$．"
    ),
    'review': (
        r"① ⭐⭐ **原书题干的 $p=1-\dfrac{1}{\sqrt[3]{x_4}}$ 被 OCR 成 `p = 1 - 1 3 x4`**："
        r"只有还原成三次根号才能闭合——此时 $1-p=\mathrm e^{-\frac13}$，"
        r"代入后得 $\ln k-\frac k3>0$，恰好对应详解的 $\varphi\left(x\right)=\ln x-\frac x3$ 与答案 $k=4$ ✓．"
        r"若按 $p=1-\frac13x_4=1-\frac{\mathrm e}3$ 或 $p=1-\frac{1}{3x_4}$，"
        r"则分别得 $\ln k-k\left(\ln3-1\right)>0$、$\ln k-k\left(1+\ln3\right)>0$，"
        r"与详解的 $\frac x3$ 都对不上．" "\n"
        r"② ⭐⭐ **$E\left(\xi_2\right)=k+1-k\left(1-p\right)^{k}$ 是本题的核心表达式**，"
        r"混合检验的期望次数 $=1\times P(\text{全阴})+\left(k+1\right)\times P(\text{有阳})$，" "\n"
        r"与 $k$ 比较即得判据 $k\left(1-p\right)^{k}\lessgtr1$（小于 $1$ 则混合检验更优）．" "\n"
        r"③ **（i）的换元 $t=\frac{x_{n+1}}{x_n}$ 是处理二次齐次递推的标准动作**："
        r"同除以 $x_nx_{n+1}$ 后必得 $t-\frac1t=C$ 的形式，两根之积为 $-1$，"
        r"故正根 $t=\mathrm e^{\frac13}$、负根 $t=-\mathrm e^{-\frac13}$，直接舍负根即可．" "\n"
        r"④ 数值复核：$k=4$ 时 $k\mathrm e^{-\frac k3}=4\mathrm e^{-1.333}=4\times0.2636=1.054>1$ ✓；"
        r"$k=5$ 时 $5\mathrm e^{-1.667}=5\times0.1889=0.944<1$ ✓ 临界确在 $4$ 与 $5$ 之间．" "\n"
        r"⑤ 检验（1）：$k=4$ 时 $p=1-4^{-\frac14}=1-0.7071=0.2929$，"
        r"此时 $\left(1-p\right)^k=0.7071^4=0.25=\frac14$ ✓ 与 $E\xi_1=E\xi_2$ 一致．" "\n"
        r"**通法（混合检验与期望比较）**：" "\n"
        r"① $\xi_2$ 只取 $1$ 与 $k+1$ 两个值，列出分布律即可；" "\n"
        r"② 「更优」的判据统一写成 $k\left(1-p\right)^{k}<1$；" "\n"
        r"③ 含 $k$ 又有 $\ln k$ 的不等式，取对数后构造函数求导，"
        r"最后代两个相邻整数定最大（小）值；" "\n"
        r"④ 二次齐次递推 ⟹ 同除以乘积 ⟹ 换元 $t$ ⟹ 解 $t-\frac1t=C$．"
    ),
    'difficulty': 0.76,
    'topics': ['M-T-399'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-399-V1',
}

QS = [
    T054_V3, T056_V2, T057_E1,
    T267_V2,
    T399_V1,
    T415_V2,
]
