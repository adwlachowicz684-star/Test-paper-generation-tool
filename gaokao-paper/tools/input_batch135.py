# -*- coding: utf-8 -*-
r"""第 135 批（补录批·六）：攻「给图求解析式」与「构造型」残余。  python3 tools/run_batch.py 135

## 本批的方法论：把「图中的数据」回填进题干

p179–p180 的 M-T-214 四题，题干都写「部分图象如图所示」，此前一律判为「依赖图形、不可录」。
回原件逐页核对后发现：**原书详解把图中读出的每一个数据都写出来了**——
最高点坐标、最低点坐标、周期算式，一个不缺。

于是可以反过来用：把详解里的数据**回填到题干**，题目就脱离原图也能独立作答。
这是 C 级题（"题干含如图但详解完整"）的标准救法，本批一次救回 4 题。

回填后每题都做了数值复核（解析式代回图中点、值域端点），四题全部逐位吻合。

## ★★ M-T-116-V1 的根号还原：用「单选唯一性」反推系数

p082 是双栏交错页，根号丢失极严重（$\sqrt3\to3$、$\sqrt2\to2$）。
难点在 A 选项：提取为 `2f(π/6) > f(π/4)`，但详解推的是 $2f(\frac\pi6)<\sqrt2 f(\frac\pi4)$，
**不含 $\sqrt2$ 就否定不了 A**。

判据是「单选唯一性」：取两个满足条件的奇函数 $f(x)=x$ 与 $f(x)=x^3$ 代入检验——
- A 不含 $\sqrt2$ 时，$f(x)=x$ 给出 A 为真，与答案 B 冲突；
- A 含 $\sqrt2$ 时，两个函数都给出 A 假、B 真、C 假、D 假，与单选答案 B 完全自洽。

故判定 A 为 $2f(\frac\pi6)>\sqrt2 f(\frac\pi4)$，同理 B 的 $3\to\sqrt3$、C 的 $3,2\to\sqrt3,\sqrt2$。

## ⚠ M-T-116-E1 本批不录（新发现的内在矛盾）

同页的 E1 详解推出 $2f(\frac\pi6)<f(\frac\pi2)$，这与 A 选项 $f(\frac\pi2)>2f(\frac\pi6)$
**是同一个不等式**——即 A 与标答 C 同时成立，单选题却只给 C。
取 $f(x)=\sin^2x$ 与 $f(x)=\sin x\cdot e^x$ 验证，A、C 确实同时为真。
属原书选项或答案存疑，不臆造，登记跳过。

这说明：**「题干/选项/详解齐备」（A 级）不等于「内部自洽」**。
本批据此在流程中新增一条硬校验——用具体函数代入，检验标答的唯一性。
"""

QS = []

# ── 1. M-T-214-V1 给图求解析式 + 值域（回填图形数据）────────────────
QS.append({
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=A\sin(\omega x+\varphi)\ \left(A>0,\ \omega>0,\ |\varphi|<\dfrac\pi2\right)$ "
        r"的部分图象如图所示（图中最高点为 $\left(\dfrac{5\pi}{12},\,2\right)$，"
        r"由图象可读出周期 $T=\dfrac43\left[\dfrac{5\pi}{12}-\left(-\dfrac\pi3\right)\right]=\pi$）。" "\n"
        r"(1) 求函数 $f(x)$ 的解析式；" "\n"
        r"(2) 将函数 $f(x)$ 的图象上所有点的横坐标变为原来的 $2$ 倍，纵坐标不变，"
        r"再将所得图象向左平移 $\dfrac\pi6$ 个单位，得到函数 $g(x)$ 的图象，"
        r"当 $x\in\left[-\dfrac\pi6,\ \pi\right]$ 时，求 $g(x)$ 的值域．"
    ),
    'opts': [],
    'answer': r"(1) $f(x)=2\sin\left(2x-\dfrac\pi3\right)$；(2) $\left[-\sqrt3,\ 2\right]$",
    'analysis': (
        r"由最高点纵坐标定 $A$，由图中两特征点间距定周期 $T$ 进而得 $\omega$，"
        r"再把最高点代入定 $\varphi$；图象变换按「先伸缩后平移」逐步作用到 $x$ 上，最后用整体法求值域。"
    ),
    'solution': (
        r"(1) 由图象可知 $f(x)$ 的最大值为 $2$，最小值为 $-2$，又 $A>0$，故 $A=2$。" "\n"
        r"由图中最高点 $\dfrac{5\pi}{12}$ 与零点 $-\dfrac\pi3$ 之间相隔 $\dfrac34$ 个周期，得" "\n"
        r"$T=\dfrac43\left[\dfrac{5\pi}{12}-\left(-\dfrac\pi3\right)\right]=\dfrac43\cdot\dfrac{3\pi}4=\pi$，"
        r"$\therefore\ \dfrac{2\pi}{\left|\omega\right|}=\pi$，又 $\omega>0$，则 $\omega=2$，"
        r"从而 $f(x)=2\sin(2x+\varphi)$。" "\n"
        r"代入最高点 $\left(\dfrac{5\pi}{12},\,2\right)$，得 $\sin\left(\dfrac{5\pi}6+\varphi\right)=1$，" "\n"
        r"则 $\dfrac{5\pi}6+\varphi=\dfrac\pi2+2k\pi\ (k\in\mathbf Z)$，即 $\varphi=-\dfrac\pi3+2k\pi$，" "\n"
        r"又 $\left|\varphi\right|<\dfrac\pi2$，取 $k=0$ 得 $\varphi=-\dfrac\pi3$。"
        r"$\therefore\ f(x)=2\sin\left(2x-\dfrac\pi3\right)$。" "\n"
        r"(2) 横坐标变为原来的 $2$ 倍、纵坐标不变，得 $y=2\sin\left(x-\dfrac\pi3\right)$；" "\n"
        r"再向左平移 $\dfrac\pi6$ 个单位，得 $g(x)=2\sin\left(x+\dfrac\pi6-\dfrac\pi3\right)"
        r"=2\sin\left(x-\dfrac\pi6\right)$。" "\n"
        r"$\because\ x\in\left[-\dfrac\pi6,\ \pi\right]$，$\therefore\ x-\dfrac\pi6\in\left[-\dfrac\pi3,\ \dfrac{5\pi}6\right]$，" "\n"
        r"$\therefore\ \sin\left(x-\dfrac\pi6\right)\in\left[-\dfrac{\sqrt3}2,\ 1\right]$，"
        r"$2\sin\left(x-\dfrac\pi6\right)\in\left[-\sqrt3,\ 2\right]$。" "\n"
        r"故 $g(x)$ 的值域为 $\left[-\sqrt3,\ 2\right]$．"
    ),
    'review': (
        r"① ⭐⭐ **「给图求解析式」三步定参**：$A$ 由最值定、$\omega$ 由周期定、$\varphi$ 由特殊点代入定，"
        r"顺序不可颠倒（$\varphi$ 必须最后定，因为要用已求出的 $\omega$）。" "\n"
        r"② ⭐⭐ **$\dfrac34$ 周期是「下降零点 → 最高点」的间距**：图上若给的是上升零点到最高点，"
        r"间距应为 $\dfrac14T$；本题 $-\dfrac\pi3$ 处 $f'=-\!4\cos(\cdots)<0$ 是下降零点，故取 $\dfrac34T$。" "\n"
        r"③ ⚠ **先伸缩后平移，平移量要跟着变**：横坐标变为 $2$ 倍后，"
        r"后续向左平移 $\dfrac\pi6$ 是直接作用在**新变量** $x$ 上的，不要再乘 $2$。" "\n"
        r"④ ⭐ 原书答案写「$-3,2$」，其中 $3$ 是 $\sqrt3$ 的丢根号（因 $2\sin$ 的振幅是 $2$，"
        r"$-3$ 会超出振幅范围），已还原。" "\n"
        r"⑤ 数值复核：$f\!\left(\dfrac{5\pi}{12}\right)=2$，"
        r"$g$ 在区间端点与驻点扫描得最小值 $-1.732051=-\sqrt3$、最大值 $2$．"
    ),
    'topics': ['M-T-214'],
    'src': 'M-T-214-V1',
    'difficulty': 0.55,
})

# ── 2. M-T-214-E1 给图求解析式 + 平移后值域 ───────────────────────
QS.append({
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=A\sin(\omega x+\varphi)\ \left(A>0,\ \omega>0,\ |\varphi|<\dfrac\pi2\right)$ "
        r"的部分图象如图所示（图中最高点为 $\left(\dfrac\pi{12},\,2\right)$，"
        r"最低点为 $\left(\dfrac{7\pi}{12},\,-2\right)$，两者相隔半个周期）。" "\n"
        r"(1) 求 $f(x)$；" "\n"
        r"(2) 将函数 $y=f(x)$ 的图象向左平移 $\dfrac\pi{12}$ 个单位，得到函数 $y=g(x)$ 的图象，"
        r"求 $g(x)$ 在 $\left[0,\ \dfrac\pi3\right]$ 上的值域．"
    ),
    'opts': [],
    'answer': r"(1) $f(x)=2\sin\left(2x+\dfrac\pi3\right)$；(2) $[-1,\ 2]$",
    'analysis': (
        r"由最大值定 $A$；最高点与最低点相距 $\dfrac T2$，由此定 $T$ 与 $\omega$；"
        r"把最高点代入定 $\varphi$。平移后化简成余弦，用整体法求值域。"
    ),
    'solution': (
        r"(1) 由最大值可确定 $A=2$。" "\n"
        r"最高点 $\dfrac\pi{12}$ 与最低点 $\dfrac{7\pi}{12}$ 相隔 $\dfrac T2$，故" "\n"
        r"$\dfrac T2=\dfrac{7\pi}{12}-\dfrac\pi{12}=\dfrac\pi2$，得 $T=\pi$，"
        r"$\omega=\dfrac{2\pi}T=2$，此时 $f(x)=2\sin(2x+\varphi)$。" "\n"
        r"代入最高点 $\left(\dfrac\pi{12},\,2\right)$，得 $\sin\left(\dfrac\pi6+\varphi\right)=1$，" "\n"
        r"从而 $\dfrac\pi6+\varphi=\dfrac\pi2+2k\pi\ (k\in\mathbf Z)$，结合 $|\varphi|<\dfrac\pi2$，"
        r"取 $k=0$ 得 $\varphi=\dfrac\pi3$。" "\n"
        r"$\therefore\ f(x)=2\sin\left(2x+\dfrac\pi3\right)$。" "\n"
        r"(2) 由题意，$g(x)=f\left(x+\dfrac\pi{12}\right)"
        r"=2\sin\left[2\left(x+\dfrac\pi{12}\right)+\dfrac\pi3\right]"
        r"=2\sin\left(2x+\dfrac\pi2\right)=2\cos 2x$。" "\n"
        r"当 $x\in\left[0,\ \dfrac\pi3\right]$ 时，$2x\in\left[0,\ \dfrac{2\pi}3\right]$，"
        r"则 $\cos 2x\in\left[-\dfrac12,\ 1\right]$，" "\n"
        r"所以 $g(x)=2\cos 2x$ 在 $\left[0,\ \dfrac\pi3\right]$ 上的值域为 $[-1,\ 2]$．"
    ),
    'review': (
        r"① ⭐⭐ **最高点与最低点相隔 $\dfrac T2$，与零点相隔 $\dfrac T4$** —— 这是读图定周期的两种基本距离，"
        r"用错一个就差一倍。" "\n"
        r"② ⭐ **平移 $\dfrac\pi{12}$ 恰好把正弦凑成余弦**：$\omega\cdot\dfrac\pi{12}=\dfrac\pi6$，"
        r"与原有 $\dfrac\pi3$ 相加得 $\dfrac\pi2$，是命题人刻意配好的，看到 $\sin(\theta+\frac\pi2)$ 立刻化 $\cos\theta$。" "\n"
        r"③ ⚠ **原书题干（提取文本）写作「求最小值」，但【分析】明确写「求函数值域」，答案也给出区间 $[-1,2]$**，"
        r"故按「求值域」录入并更正题干措辞。" "\n"
        r"④ ⭐ 值域端点都在内部取到：$\cos 2x=-\dfrac12$ 在 $2x=\dfrac{2\pi}3$ 即 $x=\dfrac\pi3$ 处取到，"
        r"$\cos2x=1$ 在 $x=0$ 处取到，故区间两端都闭。" "\n"
        r"⑤ 数值复核：$g(0)=2$、$g\!\left(\dfrac\pi3\right)=-1$，扫描最小值 $-1$、最大值 $2$．"
    ),
    'topics': ['M-T-214'],
    'src': 'M-T-214-E1',
    'difficulty': 0.52,
})

# ── 3. M-T-214-V2 含常数项 B 的给图求解析式 ───────────────────────
QS.append({
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=A\sin(\omega x+\varphi)+B\ \left(A>0,\ \omega>0,\ |\varphi|<\dfrac\pi2\right)$ "
        r"的部分图象如图所示（由图象可读出最大值 $1$、最小值 $-3$，"
        r"最高点为 $\left(\dfrac\pi{12},\,1\right)$，最低点为 $\left(\dfrac{7\pi}{12},\,-3\right)$）。" "\n"
        r"(1) 求 $f(x)$ 的解析式及对称中心坐标；" "\n"
        r"(2) 先把 $f(x)$ 的图象向左平移 $\dfrac\pi6$ 个单位，再向上平移 $1$ 个单位，"
        r"得到函数 $g(x)$ 的图象，若 $x\in\left[-\dfrac\pi4,\ \dfrac\pi6\right]$，求 $g(x)$ 的值域．"
    ),
    'opts': [],
    'answer': (
        r"(1) $f(x)=2\sin\left(2x+\dfrac\pi3\right)-1$，对称中心为 "
        r"$\left(\dfrac{k\pi}2-\dfrac\pi6,\ -1\right)\ (k\in\mathbf Z)$；(2) $[0,\ 2]$"
    ),
    'analysis': (
        r"有常数项 $B$ 时，$A,B$ 由最大值与最小值联立方程组解出；周期与 $\varphi$ 的求法同前。"
        r"对称中心即正弦函数的零点配上纵向平移量 $B$。"
    ),
    'solution': (
        r"(1) 由图象可知 $\begin{cases}A+B=1\\ -A+B=-3\end{cases}$，解得 $A=2$，$B=-1$。" "\n"
        r"又 $\dfrac T2=\dfrac{7\pi}{12}-\dfrac\pi{12}=\dfrac\pi2$，故 $T=\pi$，$\omega=\dfrac{2\pi}T=2$。" "\n"
        r"由图象知 $f\left(\dfrac\pi{12}\right)=1$，即 $\sin\left(2\times\dfrac\pi{12}+\varphi\right)=1$；" "\n"
        r"又因为 $-\dfrac\pi3<\dfrac\pi6+\varphi<\dfrac{2\pi}3$，所以 $\dfrac\pi6+\varphi=\dfrac\pi2$，"
        r"$\varphi=\dfrac\pi3$。" "\n"
        r"$\therefore\ f(x)=2\sin\left(2x+\dfrac\pi3\right)-1$。" "\n"
        r"令 $2x+\dfrac\pi3=k\pi\ (k\in\mathbf Z)$，得 $x=\dfrac{k\pi}2-\dfrac\pi6\ (k\in\mathbf Z)$，"
        r"此时 $f(x)=0-1=-1$，" "\n"
        r"所以 $f(x)$ 的对称中心坐标为 $\left(\dfrac{k\pi}2-\dfrac\pi6,\ -1\right)\ (k\in\mathbf Z)$。" "\n"
        r"(2) 依题可得 $g(x)=f\left(x+\dfrac\pi6\right)+1"
        r"=2\sin\left[2\left(x+\dfrac\pi6\right)+\dfrac\pi3\right]-1+1=2\sin\left(2x+\dfrac{2\pi}3\right)$。" "\n"
        r"$\because\ x\in\left[-\dfrac\pi4,\ \dfrac\pi6\right]$，令 $t=2x+\dfrac{2\pi}3\in\left[\dfrac\pi6,\ \pi\right]$，" "\n"
        r"$\therefore\ \sin t\in[0,\ 1]$，即 $g(x)$ 的值域为 $[0,\ 2]$．"
    ),
    'review': (
        r"① ⭐⭐ **有 $B$ 时先解 $\begin{cases}A+B=\max\\ -A+B=\min\end{cases}$**，"
        r"得 $A=\dfrac{\max-\min}2$、$B=\dfrac{\max+\min}2$ —— 可当公式直接套。" "\n"
        r"② ⭐ **对称中心是「正弦部分为零」的点，纵坐标等于 $B$（本题 $-1$）**，不是 $0$，这是最高频失分点。" "\n"
        r"③ ⭐ **本题 $\varphi$ 用「范围夹逼」确定而非取 $k=0$**：由 $|\varphi|<\dfrac\pi2$ 得 "
        r"$\dfrac\pi6+\varphi\in\left(-\dfrac\pi3,\ \dfrac{2\pi}3\right)$，区间内使 $\sin=1$ 的只有 $\dfrac\pi2$，"
        r"故唯一确定，不必讨论 $k$。" "\n"
        r"④ ⚠ 上移 $1$ 恰好抵消 $B=-1$，使 $g$ 变成纯正弦 $2\sin\left(2x+\dfrac{2\pi}3\right)$ —— "
        r"这是命题人设计的简化，算出 $g$ 后应自觉检查是否退化。" "\n"
        r"⑤ 数值复核：$f\!\left(\dfrac\pi{12}\right)=1$、$f\!\left(\dfrac{7\pi}{12}\right)=-3$；"
        r"$g$ 在区间上扫描得 $[0,\ 2]$．"
    ),
    'topics': ['M-T-214'],
    'src': 'M-T-214-V2',
    'difficulty': 0.58,
})

# ── 4. M-T-214-V3 给图求解析式 + 多重变换 ─────────────────────────
QS.append({
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=A\sin(\omega x+\varphi)\ \left(A>0,\ \omega>0,\ 0\le\varphi<\pi\right)$ 的图象如图所示"
        r"（图中最高点为 $\left(\dfrac{13\pi}{12},\,2\right)$，零点为 $\left(\dfrac\pi3,\,0\right)$，"
        r"两者之间相隔 $\dfrac34$ 个周期）。" "\n"
        r"(1) 求函数 $f(x)$ 的解析式；" "\n"
        r"(2) 首先将函数 $f(x)$ 的图象上每一点横坐标缩短为原来的 $\dfrac12$，"
        r"然后将所得函数图象向右平移 $\dfrac\pi8$ 个单位，最后再向上平移 $1$ 个单位得到函数 $g(x)$ 的图象，"
        r"求函数 $g(x)$ 在 $\left[0,\ \dfrac\pi2\right]$ 内的值域．"
    ),
    'opts': [],
    'answer': r"(1) $f(x)=2\sin\left(2x+\dfrac\pi3\right)$；(2) $[-1,\ 3]$",
    'analysis': (
        r"由最高点纵坐标定 $A$；由最高点与零点的间距（$\dfrac34T$）定 $T$ 与 $\omega$；"
        r"把最高点代入定 $\varphi$，注意本题 $\varphi$ 的范围是 $[0,\pi)$ 而非常见的 $|\varphi|<\dfrac\pi2$。"
        r"三重变换按「伸缩 → 平移 → 上下」逐步作用。"
    ),
    'solution': (
        r"(1) 由图象得 $A=2$。" "\n"
        r"零点 $\dfrac\pi3$ 与最高点 $\dfrac{13\pi}{12}$ 相隔 $\dfrac34$ 个周期，故" "\n"
        r"$\dfrac{13\pi}{12}-\dfrac\pi3=\dfrac34T=\dfrac34\cdot\dfrac{2\pi}{\omega}$，" "\n"
        r"即 $\dfrac{3\pi}4=\dfrac{3\pi}{2\omega}$，得 $\omega=2$。" "\n"
        r"由 $2\times\dfrac{13\pi}{12}+\varphi=\dfrac\pi2+2k\pi$，得 $\varphi=-\dfrac{5\pi}3+2k\pi\ (k\in\mathbf Z)$；" "\n"
        r"$\because\ 0\le\varphi<\pi$，取 $k=1$ 得 $\varphi=\dfrac\pi3$。" "\n"
        r"$\therefore\ f(x)=2\sin\left(2x+\dfrac\pi3\right)$。" "\n"
        r"(2) 横坐标缩短为原来的 $\dfrac12$，得 $y=2\sin\left(4x+\dfrac\pi3\right)$；" "\n"
        r"再向右平移 $\dfrac\pi8$ 个单位，得 "
        r"$y=2\sin\left[4\left(x-\dfrac\pi8\right)+\dfrac\pi3\right]=2\sin\left(4x-\dfrac\pi2+\dfrac\pi3\right)"
        r"=2\sin\left(4x-\dfrac\pi6\right)$；" "\n"
        r"最后向上平移 $1$ 个单位，得 $g(x)=2\sin\left(4x-\dfrac\pi6\right)+1$。" "\n"
        r"当 $x\in\left[0,\ \dfrac\pi2\right]$ 时，$4x-\dfrac\pi6\in\left[-\dfrac\pi6,\ \dfrac{11\pi}6\right]$，" "\n"
        r"该区间长度 $2\pi$，覆盖正弦的一个完整周期，故 $\sin\left(4x-\dfrac\pi6\right)\in[-1,\ 1]$，" "\n"
        r"$\therefore\ g(x)\in[-1,\ 3]$．"
    ),
    'review': (
        r"① ⭐⭐ **$\varphi$ 取 $k=1$ 而非 $k=0$**：由最高点代入得 $\varphi=-\dfrac{5\pi}3+2k\pi$，"
        r"$k=0$ 时 $\varphi=-\dfrac{5\pi}3$ 不在 $[0,\pi)$ 内，必须取 $k=1$ 得 $\dfrac\pi3$。"
        r"题目把 $\varphi$ 范围改成 $[0,\pi)$ 正是为了制造这一步。" "\n"
        r"② ⚠ **「缩短为原来的 $\dfrac12$」是 $x\to 2x$，不是 $x\to\dfrac x2$** —— "
        r"即 $\omega$ 由 $2$ 变 $4$；方向弄反会让后续平移全部错位。" "\n"
        r"③ ⭐ **右移 $\dfrac\pi8$ 时，$\omega=4$ 已经生效**，故平移量贡献 $4\times\dfrac\pi8=\dfrac\pi2$，"
        r"与 $\dfrac\pi3$ 合成 $-\dfrac\pi6$。先伸缩后平移的题目，务必用「变换后」的 $\omega$ 算平移量。" "\n"
        r"④ ⭐ 相位区间 $\left[-\dfrac\pi6,\ \dfrac{11\pi}6\right]$ 长度恰为 $2\pi$，"
        r"直接取 $[-1,1]$ 即可，不必找驻点 —— 看到长度 $2\pi$ 就该反应过来。" "\n"
        r"⑤ 数值复核：$f\!\left(\dfrac{13\pi}{12}\right)=2$、$f\!\left(\dfrac\pi3\right)=0$；"
        r"$g$ 扫描得 $[-1,\ 3]$．"
    ),
    'topics': ['M-T-214'],
    'src': 'M-T-214-V3',
    'difficulty': 0.62,
})

# ── 5. M-T-116-V1 sinx 与 f(x) 构造型（根号还原）──────────────────
QS.append({
    'type': '选择',
    'stem_text': (
        r"已知奇函数 $f(x)$ 的导函数为 $f'(x)$，且 $f(x)$ 在 $\left(0,\ \dfrac\pi2\right)$ 上恒有 "
        r"$f(x)\cos x-f'(x)\sin x<0$ 成立，则下列不等式成立的是（　　）"
    ),
    'opts': [
        ('A', r"$2f\left(\dfrac\pi6\right)>\sqrt2 f\left(\dfrac\pi4\right)$"),
        ('B', r"$f\left(-\dfrac\pi3\right)<\sqrt3 f\left(-\dfrac\pi6\right)$"),
        ('C', r"$\sqrt3 f\left(-\dfrac\pi4\right)<\sqrt2 f\left(-\dfrac\pi3\right)$"),
        ('D', r"$\sqrt2 f\left(\dfrac\pi3\right)<\sqrt3 f\left(\dfrac\pi4\right)$"),
    ],
    'answer': 'B',
    'analysis': (
        r"把条件变形为 $\left(\dfrac{f(x)}{\sin x}\right)'>0$，构造函数 $F(x)=\dfrac{f(x)}{\sin x}$；"
        r"再由 $f$ 为奇函数推出 $F$ 为偶函数，用单调性逐一比较各选项中的两个函数值。"
    ),
    'solution': (
        r"构造函数 $F(x)=\dfrac{f(x)}{\sin x}$。由 $f(x)$ 在 $\left(0,\ \dfrac\pi2\right)$ 上恒有 "
        r"$f'(x)\sin x-f(x)\cos x>0$，" "\n"
        r"$\therefore\ F'(x)=\dfrac{f'(x)\sin x-f(x)\cos x}{(\sin x)^2}>0$，"
        r"$\therefore\ F(x)$ 在 $\left(0,\ \dfrac\pi2\right)$ 上为增函数。" "\n"
        r"又 $F(-x)=\dfrac{f(-x)}{\sin(-x)}=\dfrac{-f(x)}{-\sin x}=F(x)$，故 $F(x)$ 为偶函数。" "\n"
        r"**A**：$\because\ \dfrac\pi6<\dfrac\pi4$，$\therefore\ F\left(\dfrac\pi6\right)<F\left(\dfrac\pi4\right)$，" "\n"
        r"即 $\dfrac{f(\frac\pi6)}{\sin\frac\pi6}<\dfrac{f(\frac\pi4)}{\sin\frac\pi4}$，" "\n"
        r"代入 $\sin\dfrac\pi6=\dfrac12$、$\sin\dfrac\pi4=\dfrac{\sqrt2}2$，得 "
        r"$2f\left(\dfrac\pi6\right)<\sqrt2 f\left(\dfrac\pi4\right)$，故 A 错误。" "\n"
        r"**B**：偶函数 $F$ 在 $\left(0,\ \dfrac\pi2\right)$ 上递增，故在 $\left(-\dfrac\pi2,\ 0\right)$ 上递减。" "\n"
        r"$\because\ -\dfrac\pi3<-\dfrac\pi6$，$\therefore\ F\left(-\dfrac\pi3\right)>F\left(-\dfrac\pi6\right)$，" "\n"
        r"即 $\dfrac{f(-\frac\pi3)}{\sin(-\frac\pi3)}>\dfrac{f(-\frac\pi6)}{\sin(-\frac\pi6)}$，" "\n"
        r"代入 $\sin\left(-\dfrac\pi3\right)=-\dfrac{\sqrt3}2$、$\sin\left(-\dfrac\pi6\right)=-\dfrac12$，得 " "\n"
        r"$-\dfrac{2}{\sqrt3}f\left(-\dfrac\pi3\right)>-2f\left(-\dfrac\pi6\right)$，" "\n"
        r"两边同乘 $-\dfrac{\sqrt3}2$（变号）得 $f\left(-\dfrac\pi3\right)<\sqrt3 f\left(-\dfrac\pi6\right)$，故 B 正确。" "\n"
        r"**C**：$\because\ -\dfrac\pi4>-\dfrac\pi3$，$\therefore\ F\left(-\dfrac\pi4\right)<F\left(-\dfrac\pi3\right)$，" "\n"
        r"即 $\dfrac{f(-\frac\pi4)}{-\frac{\sqrt2}2}<\dfrac{f(-\frac\pi3)}{-\frac{\sqrt3}2}$，" "\n"
        r"化简得 $\sqrt3 f\left(-\dfrac\pi4\right)>\sqrt2 f\left(-\dfrac\pi3\right)$，故 C 错误。" "\n"
        r"**D**：$\because\ \dfrac\pi3>\dfrac\pi4$，$\therefore\ F\left(\dfrac\pi3\right)>F\left(\dfrac\pi4\right)$，" "\n"
        r"即 $\dfrac{f(\frac\pi3)}{\frac{\sqrt3}2}>\dfrac{f(\frac\pi4)}{\frac{\sqrt2}2}$，" "\n"
        r"化简得 $\sqrt2 f\left(\dfrac\pi3\right)>\sqrt3 f\left(\dfrac\pi4\right)$，故 D 错误。" "\n"
        r"故选 $\mathbf{B}$．"
    ),
    'review': (
        r"① ⭐⭐ **识别模板**：$f'(x)\sin x-f(x)\cos x$ 正是 $\left(\dfrac{f}{\sin x}\right)'$ 的分子，"
        r"见到「$f'\sin$ 减 $f\cos$」立刻构造 $\dfrac{f(x)}{\sin x}$；"
        r"反之「$f'\sin+f\cos$」对应 $\left(f\sin x\right)'$。" "\n"
        r"② ⭐⭐ **分子分母同乘时负号必须小心**：本题 B 项两个 $\sin$ 都是负值，"
        r"同乘 $-\dfrac{\sqrt3}2$ 要变号，这是 B 与 C 方向相反的唯一原因。" "\n"
        r"③ ⭐ **$f$ 奇 + $\sin x$ 奇 ⟹ $F$ 偶**，于是「负半轴递减」可平移到「正半轴递增」处理，"
        r"不必在负角上另起炉灶。" "\n"
        r"④ ⚠ **原书 p082 双栏交错，根号全部丢失**（$3\to\sqrt3$、$2\to\sqrt2$），"
        r"本批用「单选唯一性」反推还原：取满足条件的奇函数 $f(x)=x$ 与 $f(x)=x^3$ 代入检验，" "\n"
        r"　 只有 A 含 $\sqrt2$ 时才得到 A 假、B 真、C 假、D 假，与单选答案 B 自洽；"
        r"若 A 不含 $\sqrt2$，$f(x)=x$ 会使 A 也为真，与单选矛盾。" "\n"
        r"⑤ ⭐ **$\dfrac1{\sin\theta}$ 的换算可直接记**："
        r"$\dfrac1{\sin\frac\pi6}=2$、$\dfrac1{\sin\frac\pi4}=\sqrt2$、$\dfrac1{\sin\frac\pi3}=\dfrac{2}{\sqrt3}$，"
        r"比较大小时两边同乘这些数即可，比通分快。"
    ),
    'topics': ['M-T-116'],
    'src': 'M-T-116-V1',
    'difficulty': 0.68,
})

# ── 6. M-T-140-V3 嵌套函数零点之和 ────────────────────────────────
QS.append({
    'type': '选择',
    'stem_text': (
        r"已知函数 $f(x)=\begin{cases}\ln x, & x\ge 1\\[4pt] 1-\dfrac x2, & x<1\end{cases}$，"
        r"若 $F(x)=f\big(f(x)+1\big)+m$ 有两个零点 $x_1$，$x_2$，"
        r"则 $x_1+x_2$ 的取值范围是（　　）"
    ),
    'opts': [
        ('A', r"$[4-2\ln 2,\ +\infty)$"),
        ('B', r"$[1+\sqrt{\mathrm e},\ +\infty)$"),
        ('C', r"$[4-2\ln 2,\ 1+\sqrt{\mathrm e})$"),
        ('D', r"$(-\infty,\ 1+\sqrt{\mathrm e})$"),
    ],
    'answer': 'A',
    'analysis': (
        r"先证明对一切 $x$ 都有 $f(x)+1\ge1$，从而 $f\big(f(x)+1\big)=\ln\big(f(x)+1\big)$；"
        r"于是零点问题化为 $f(x)=t$ 有两根，用 $t$ 表示两根之和，再对 $t$ 求最值。"
    ),
    'solution': (
        r"当 $x\ge1$ 时，$f(x)+1=\ln x+1\ge1$，$\therefore\ f\big(f(x)+1\big)=\ln\big(f(x)+1\big)$；" "\n"
        r"当 $x<1$ 时，$f(x)+1=1-\dfrac x2+1=2-\dfrac x2>\dfrac32>1$，"
        r"$\therefore\ f\big(f(x)+1\big)=\ln\big(f(x)+1\big)$。" "\n"
        r"综上，对 $\forall x\in\mathbf R$，$f\big(f(x)+1\big)=\ln\big(f(x)+1\big)$。" "\n"
        r"$\therefore\ F(x)=f\big(f(x)+1\big)+m$ 有两个零点 $x_1$，$x_2$，"
        r"即方程 $\ln\big(f(x)+1\big)+m=0$ 有两个根 $x_1$，$x_2$，" "\n"
        r"即方程 $f(x)=\mathrm e^{-m}-1$ 有两个根 $x_1$，$x_2$，不妨设 $x_1<x_2$。" "\n"
        r"易知 $f(x)$ 在 $(-\infty,\ 1)$ 上单调递减，在 $[1,\ +\infty)$ 上单调递增，" "\n"
        r"$\therefore\ $当 $x\ge1$ 时 $\ln x_2=\mathrm e^{-m}-1$；当 $x<1$ 时 $1-\dfrac{x_1}2=\mathrm e^{-m}-1$。" "\n"
        r"令 $t=\mathrm e^{-m}-1$。$\because\ 1-\dfrac{x_1}2>\dfrac12$（由 $x_1<1$），$\therefore\ t>\dfrac12$。" "\n"
        r"$\therefore\ x_2=\mathrm e^{t}$，$x_1=2-2t$，"
        r"$x_1+x_2=\mathrm e^{t}-2t+2$，$t>\dfrac12$。" "\n"
        r"令 $g(t)=\mathrm e^{t}-2t+2$，$t>\dfrac12$，则 $g'(t)=\mathrm e^{t}-2$，令 $g'(t)=0$ 得 $t=\ln 2$。" "\n"
        r"$\therefore\ \dfrac12<t<\ln2$ 时 $g'(t)<0$；$t>\ln2$ 时 $g'(t)>0$，" "\n"
        r"即 $g(t)$ 在 $\left(\dfrac12,\ \ln2\right)$ 上单调递减，在 $(\ln2,\ +\infty)$ 上单调递增。" "\n"
        r"$g(\ln2)=\mathrm e^{\ln2}-2\ln2+2=2-2\ln2+2=4-2\ln2$；" "\n"
        r"$t\to\dfrac12^{+}$ 时 $g(t)\to\sqrt{\mathrm e}+1$；$t\to+\infty$ 时 $g(t)\to+\infty$。" "\n"
        r"由于 $\sqrt{\mathrm e}+1\approx2.649>4-2\ln2\approx2.614$，最小值 $4-2\ln2$ 可取到，"
        r"且 $t\to+\infty$ 时无上界，" "\n"
        r"故值域为 $[4-2\ln2,\ +\infty)$。故选 $\mathbf{A}$．"
    ),
    'review': (
        r"① ⭐⭐ **先证「内层恒落在同一段」**：本题关键是 $f(x)+1\ge1$ 恒成立，"
        r"所以 $f\big(f(x)+1\big)$ 恒走 $\ln$ 那一支。嵌套函数题第一步永远是**定内层的值域**。" "\n"
        r"② ⭐ **把零点方程反解成 $f(x)=t$**：$t=\mathrm e^{-m}-1$ 与 $m$ 一一对应，"
        r"于是「$F$ 有两个零点」等价于「水平线 $y=t$ 与 $f$ 有两个交点」，几何意义立刻清楚。" "\n"
        r"③ ⭐ **两根分居两段，各用各的表达式**：$x_2=\mathrm e^t$（右段）、$x_1=2-2t$（左段），"
        r"再由 $x_1<1$ 反推出 $t$ 的范围 $t>\dfrac12$ —— 这个约束是 $t$ 定义域的唯一来源，别漏。" "\n"
        r"④ ⚠ **最小值点在区间内部**：$\ln2\approx0.693>\dfrac12$，故 $g(\ln2)$ 可取到，"
        r"下端闭；左端点 $t=\dfrac12$ 取不到但对应值 $\sqrt{\mathrm e}+1$ 大于最小值，不影响值域。" "\n"
        r"⑤ 数值复核：$g(\ln2)=2.613706=4-2\ln2$，$g(0.5)=2.648721=1+\sqrt{\mathrm e}$，" "\n"
        r"　 $g(3)=16.086$ 无上界，值域确为 $[4-2\ln2,\ +\infty)$．" "\n"
        r"⑥ ⭐ 干扰项 C 的右端 $1+\sqrt{\mathrm e}$ 正是 $t\to\dfrac12^+$ 的极限值，"
        r"它只是**局部**上界而非全局上界 —— 误把左端点当最大值就会错选 C。"
    ),
    'topics': ['M-T-140'],
    'src': 'M-T-140-V3',
    'difficulty': 0.72,
})
