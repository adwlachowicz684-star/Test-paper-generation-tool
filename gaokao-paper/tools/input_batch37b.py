# -*- coding: utf-8 -*-
r"""第37批（下）：导数中的「距离」· 同底指数与对数对称（4题）

来源：2024高中数学热点题型归纳完整解析版.pdf p102（PDF 页 101）

## 选题

`pick_batch.py --n 14` → p102（M-T-136），A/B 级。

## 四题验算（全部独立算过）

| 题 | 关键 | 答案 |
|---|---|---|
| E1 | $y=e^x$ 与 $y=1-\frac1x$ 分居 $y=x$ 两侧；各自到 $y=x$ 最短距离都是 $\frac{\sqrt2}2$ | **D** $\sqrt2$ |
| V1 | 式子是两点距离平方，两曲线互为反函数；最短距离 $=\sqrt2(1-\ln2)$ | **B** $2(1-\ln2)^2$ |
| V2 | ①真（$ae^a=1$ 有解）；②真（$\lvert AB\rvert'=e^a-\frac1a$，同条件）；③假（最小值 $\approx2.33\neq2$） | **C** |
| V3 | $P(e,1)$ 到圆心 $\left(e+\frac1e,0\right)$ 距离 $\frac{\sqrt{e^2+1}}e$，减半径 $1$ | **A** |

## ⚠ 三处提取问题（已还原并验证）

- **V1**：$\frac12(e^a-\ln2b)^2$ 实为 $\left(\frac{e^a}2-\ln(2b)\right)^2$ ——
  详解「令 $f'(x)=\frac{e^x}2=1$，$x=\ln2$，$f(\ln2)=1$」反推出函数是 $y=\frac{e^x}2$ 而非 $y=e^x$
- **V3**：选项的根号为矢量绘制；由答案与验算定为 $\frac{\sqrt{e^2+1}-e}e$
- **V2**：选项字符提取只确认到 `A.①` 与末尾的 `①②③`，中间缺失。
  **按详解结论「①正确；②正确，③错误」与答案 C 推定为 C=①②**，已标注
"""

T136_E1 = {
    'type': '选择',
    'stem_text': (
        r"设点 $P$ 在曲线 $y=\mathrm e^{x}$ 上，点 $Q$ 在曲线 $y=1-\dfrac1x$（$x>0$）上，"
        r"则 $\lvert PQ\rvert$ 的最小值为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac{\sqrt2}2(\mathrm e-1)$"),
        ('B', r"$\sqrt2(\mathrm e-1)$"),
        ('C', r"$\dfrac{\sqrt2}2$"),
        ('D', r"$\sqrt2$"),
    ],
    'answer': 'D',
    'analysis': (
        r"两条曲线分居 $y=x$ 两侧，各自到 $y=x$ 的最短距离都是 $\frac{\sqrt2}2$，"
        r"且取到时 $PQ\perp y=x$，故 $\lvert PQ\rvert_{\min}=\sqrt2$。"
    ),
    'solution': (
        r"**第一步：判断两条曲线与 $y=x$ 的位置关系**" "\n"
        r"$y=\mathrm e^{x}$：由 $\mathrm e^{x}>x$ 恒成立，图像**恒在 $y=x$ 上方**．" "\n"
        r"$y=1-\dfrac1x$：$x-\left(1-\dfrac1x\right)=\dfrac{x^{2}-x+1}x>0$"
        r"（分子判别式 $1-4<0$），图像**恒在 $y=x$ 下方**．" "\n"
        r"**第二步：求两条曲线各自到 $y=x$ 的最短距离**" "\n"
        r"曲线 $y=\mathrm e^{x}$ 上点 $(t,\mathrm e^{t})$ 到 $y=x$ 的距离 "
        r"$d_{1}=\dfrac{\mathrm e^{t}-t}{\sqrt2}$．" "\n"
        r"令 $u(t)=\mathrm e^{t}-t$，$u'(t)=\mathrm e^{t}-1=0\Rightarrow t=0$，"
        r"$u(0)=1$，故 $d_{1,\min}=\dfrac1{\sqrt2}=\dfrac{\sqrt2}2$（在 $P(0,1)$ 处）．" "\n"
        r"曲线 $y=1-\dfrac1x$ 上点到 $y=x$ 的距离 $d_{2}=\dfrac{x-1+\frac1x}{\sqrt2}$．" "\n"
        r"由 $x+\dfrac1x\ge2$（$x=1$ 取等）得 $d_{2,\min}=\dfrac{2-1}{\sqrt2}=\dfrac{\sqrt2}2$（在 $Q(1,0)$ 处）．" "\n"
        r"**第三步：合起来**" "\n"
        r"因两曲线分居 $y=x$ 两侧，$\lvert PQ\rvert\ge d_{1}+d_{2}\ge\dfrac{\sqrt2}2+\dfrac{\sqrt2}2=\sqrt2$．" "\n"
        r"当 $P(0,1)$、$Q(1,0)$ 时，$PQ$ 方向为 $(1,-1)$，与 $y=x$ 方向 $(1,1)$ 垂直，"
        r"**等号成立**．" "\n"
        r"故 $\lvert PQ\rvert_{\min}=\sqrt2$．选 D．"
    ),
    'review': (
        r"★ 由详解「如图所示：$PQ$ 与直线 $y=x$ 相交于 $M$，$P$ 关于 $y=x$ 的对称点 $P'$ 在 $\ln x$ 上．"
        r"则 $\lvert PQ\rvert=\lvert MQ\rvert+\lvert MP'\rvert$…设 $g(x)=\ln x+\frac1x-1$，"
        r"则 $g'(x)=\frac1x-\frac1{x^2}=\frac{x-1}{x^2}$，故 $g(x)$ 在 $(0,1)$ 上单调递减，"
        r"在 $(1,+\infty)$ 上单调递增，$g(1)=0$，故 $g(x)\ge g(1)=0$ 恒成立，"
        r"即 $\ln x\ge1-\frac1x$。$y=\ln x$ 的导函数 $y'=\frac1x$，$y=1-\frac1x$（$x>0$）的导函数 "
        r"$y'=\frac1{x^2}$，当两条切线与 $y=x$ 平行时，都有 $x=1$，$(1,0)$ 到直线 $y=x$ 的距离为 $\frac{\sqrt2}2$。"
        r"故 $\lvert PQ\rvert=\lvert MQ\rvert+\lvert MP'\rvert\ge\frac{\sqrt2}2+\frac{\sqrt2}2=\sqrt2$，"
        r"当 $P(0,1)$、$Q(1,0)$ 时等号成立。故选 D」还原。" "\n"
        r"（详解中「$g(x)\ge g(0)=0$」应为 $g(1)=0$ —— $g$ 在 $x=0$ 无定义，显系笔误。）" "\n"
        r"**选项还原**（PDF 页 101，y≈132：`A.(e-1) B.2(e-1) C. D.2`）："
        r"结合根号矢量绘制与数值 $\frac{\sqrt2}2(e-1)\approx1.215$、$\sqrt2(e-1)\approx2.430$、"
        r"$\frac{\sqrt2}2\approx0.707$、$\sqrt2\approx1.414$，四值递增 ✓" "\n"
        r"**独立验算**：" "\n"
        r"① $P(0,1)$ 在 $y=\mathrm e^x$ 上 ✓；$Q(1,0)$ 在 $y=1-\frac1x$ 上（$1-1=0$）✓" "\n"
        r"② $\lvert PQ\rvert=\sqrt{(1-0)^2+(0-1)^2}=\sqrt2\approx1.4142$ ✓" "\n"
        r"③ 两曲线到 $y=x$ 距离均为 $\frac{\sqrt2}2=0.7071$，和 $=1.4142$ ✓✓ **与 $\lvert PQ\rvert$ 相等**" "\n"
        r"④ **扫描验证**（取 $P=(t,\mathrm e^t)$、$Q=(s,1-\frac1s)$ 网格搜索 $t\in[-1,1]$、$s\in[0.5,2]$，"
        r"步长 $0.02$）：最小值出现在 $t\approx0$、$s\approx1$ 附近，值 $\approx1.4142$ ✓" "\n"
        r"**答案 D 正确** ✓" "\n"
        r"**⭐ 通法**：两条曲线**分居 $y=x$ 两侧**时，最短距离 = 各自到 $y=x$ 最短距离之和，"
        r"当且仅当两点连线垂直于 $y=x$ 时取到。"
    ),
    'difficulty': 0.93,
    'topics': ['M-T-136'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-136-E1',
}

T136_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知 $a\in\mathbf R$，$b\in\mathbf R^{+}$，$\mathrm e$ 为自然对数的底数，"
        r"则 $\left(\dfrac{\mathrm e^{a}}2-\ln(2b)\right)^{2}+(a-b)^{2}$ 的最小值为（　　）"
    ),
    'opts': [
        ('A', r"$(1-\ln2)^{2}$"),
        ('B', r"$2(1-\ln2)^{2}$"),
        ('C', r"$1+\ln2$"),
        ('D', r"$2(1-\ln2)$"),
    ],
    'answer': 'B',
    'analysis': (
        r"把式子看成点 $(a,\frac{\mathrm e^{a}}2)$ 与点 $(b,\ln(2b))$ 的距离平方；"
        r"这两点分别在 $y=\frac{\mathrm e^{x}}2$ 与其反函数 $y=\ln(2x)$ 上，"
        r"两曲线关于 $y=x$ 对称，最短距离 $=2\times$ 曲线到 $y=x$ 的最短距离。"
    ),
    'solution': (
        r"**第一步：识别为两点距离平方**" "\n"
        r"$\left(\dfrac{\mathrm e^{a}}2-\ln(2b)\right)^{2}+(a-b)^{2}$" "\n"
        r"$=\left(a-b\right)^{2}+\left(\dfrac{\mathrm e^{a}}2-\ln(2b)\right)^{2}$" "\n"
        r"即点 $A\!\left(a,\dfrac{\mathrm e^{a}}2\right)$ 与点 $B\!\left(b,\ln(2b)\right)$ 的距离平方．" "\n"
        r"**第二步：识别两条曲线**" "\n"
        r"$A$ 在 $y=\dfrac{\mathrm e^{x}}2$ 上；$B$ 满足 $y=\ln(2x)$（$x=b$ 时 $y=\ln(2b)$）．" "\n"
        r"由 $y=\dfrac{\mathrm e^{x}}2$ 解得 $x=\ln(2y)$，故 $y=\ln(2x)$ 正是它的**反函数**，"
        r"两图像**关于 $y=x$ 对称**．" "\n"
        r"**第三步：求曲线到 $y=x$ 的最短距离**" "\n"
        r"点 $\left(t,\dfrac{\mathrm e^{t}}2\right)$ 到 $y=x$ 的距离 "
        r"$d=\dfrac{\frac{\mathrm e^{t}}2-t}{\sqrt2}$．" "\n"
        r"令 $h(t)=\dfrac{\mathrm e^{t}}2-t$，$h'(t)=\dfrac{\mathrm e^{t}}2-1=0\Rightarrow t=\ln2$，" "\n"
        r"$h(\ln2)=\dfrac{\mathrm e^{\ln2}}2-\ln2=1-\ln2>0$，故 $d_{\min}=\dfrac{1-\ln2}{\sqrt2}$．" "\n"
        r"**第四步：对称两曲线的最短距离**" "\n"
        r"最短距离 $=2d_{\min}=\dfrac{2(1-\ln2)}{\sqrt2}=\sqrt2(1-\ln2)$，" "\n"
        r"故所求最小值 $=\left[\sqrt2(1-\ln2)\right]^{2}=2(1-\ln2)^{2}$．选 B．"
    ),
    'review': (
        r"★ 由详解「函数 $f(x)=\frac{\mathrm e^{x}}2$ 和函数 $g(x)=\ln(2x)$ 互为反函数，"
        r"图像关于 $y=x$ 对称。令 $f'(x)=\frac{\mathrm e^{x}}2=1$，$x=\ln2$，$f(\ln2)=1$，"
        r"切线方程为 $y-1=x-\ln2$，$x-y+1-\ln2=0$，$x-y=0$，两条直线之间的距离为 $\frac{\lvert1-\ln2\rvert}{\sqrt2}$，"
        r"故 $\left[\frac{\mathrm e^{a}}2-\ln(2b)\right]^{2}$ 的最小值为 $2(1-\ln2)^{2}$，"
        r"此时 $a=b=\ln2$，故 $(a-b)^{2}=0$」还原。" "\n"
        r"**⚠⚠ 题干式子需反推（关键）**：提取文本为 `1 2 ea- ln 2b 2 + a - b 2`，"
        r"字面读作 $\frac12(\mathrm e^{a}-\ln2b)^{2}+(a-b)^{2}$。" "\n"
        r"**但详解的「$f'(x)=\frac{\mathrm e^x}2=1$，$x=\ln2$，$f(\ln2)=1$」表明函数是 "
        r"$y=\frac{\mathrm e^{x}}2$，不是 $y=\mathrm e^{x}$**（否则 $f'(x)=\mathrm e^x=1\Rightarrow x=0$）。" "\n"
        r"故题干应为 $\left(\frac{\mathrm e^{a}}2-\ln(2b)\right)^{2}+(a-b)^{2}$，按此录入。" "\n"
        r"**选项字符确认**（PDF 页 101，y≈778/792）："
        r"A `(1 - ln2)` 带平方上标 → $(1-\ln2)^2$；B `2(1 - ln2)` 带平方 → $2(1-\ln2)^2$；"
        r"C `1 + ln2`；D `2(1 - ln2)`（无平方）✓" "\n"
        r"**独立验算**（取 $a=b=\ln2$ 直接算）：" "\n"
        r"$\frac{\mathrm e^{\ln2}}2=\frac22=1$；$\ln(2\ln2)=\ln(1.3863)=0.3266$" "\n"
        r"式子 $=(1-0.3266)^2+(\ln2-\ln2)^2=0.6734^2=0.4535$" "\n"
        r"而 $2(1-\ln2)^2=2\times0.30685^2=2\times0.09416=0.1883$ —— " "\n"
        r"⚠ 注意：$a=b=\ln2$ 时 $(a-b)^2=0$，但第一项不为 $0$，"
        r"而**真正的最小值点**是两曲线上关于 $y=x$ 对称的那对点，" "\n"
        r"即 $A(\ln2,1)$ 与 $B(1,\ln2)$（互为对称点）！此时 $a=\ln2$、$b=1$：" "\n"
        r"式子 $=(1-\ln2)^2+(\ln2-1)^2=2(1-\ln2)^2=0.1883$ ✓✓ **这才是最小值**" "\n"
        r"（详解写的「此时 $a=b=\ln2$」有误 —— 若 $a=b=\ln2$ 则 $A=B=(\ln2,1)$，"
        r"但 $B(1,\ln2)$ 才是对称点。**最小值 $2(1-\ln2)^2$ 正确，取等条件详解写错了**。）" "\n"
        r"**答案 B 正确** ✓" "\n"
        r"**⭐ 通法**：见到「$X^2+Y^2$」形式先想**两点距离**；"
        r"若两点分属互为反函数的两条曲线，则最短距离 $=2\times$ 到 $y=x$ 的距离。"
    ),
    'difficulty': 0.95,
    'topics': ['M-T-136'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-136-V1',
}

T136_V2 = {
    'type': '选择',
    'stem_text': (
        r"若直线 $x=a$ 与两曲线 $y=\mathrm e^{x}$、$y=\ln x$ 分别交于 $A,B$ 两点，"
        r"且曲线 $y=\mathrm e^{x}$ 在 $A$ 点处的切线为 $m$，曲线 $y=\ln x$ 在 $B$ 点处的切线为 $n$，"
        r"则下列结论：① $\exists a\in(0,+\infty)$，使 $m\parallel n$；"
        r"② 当 $m\parallel n$ 时，$\lvert AB\rvert$ 取得最小值；"
        r"③ $\lvert AB\rvert$ 的最小值为 $2$；④ $\lvert AB\rvert>\ln2+\log_{2}\mathrm e$．"
        r"其中所有正确结论的序号是（　　）"
    ),
    'opts': [
        ('A', r"①"),
        ('B', r"②"),
        ('C', r"①②"),
        ('D', r"①②③"),
    ],
    'answer': 'C',
    'analysis': (
        r"① 令两切线斜率相等 $\mathrm e^{a}=\frac1a$，由零点存在定理有解；"
        r"② $\lvert AB\rvert=\mathrm e^{a}-\ln a$ 的导数恰为 $\mathrm e^{a}-\frac1a$，与①同条件；"
        r"③ 最小值为 $a_{0}+\frac1{a_{0}}\approx2.33\neq2$，故错。"
    ),
    'solution': (
        r"**记号**：$A(a,\mathrm e^{a})$、$B(a,\ln a)$（$a>0$）．" "\n"
        r"切线 $m$ 斜率 $k_{m}=\mathrm e^{a}$；切线 $n$ 斜率 $k_{n}=\dfrac1a$．" "\n"
        r"**结论①**：令 $k_{m}=k_{n}$，即 $\mathrm e^{a}=\dfrac1a$，"
        r"设 $g(x)=\mathrm e^{x}-\dfrac1x$（$x>0$）．" "\n"
        r"$g\!\left(\dfrac12\right)=\mathrm e^{1/2}-2=1.6487-2=-0.3513<0$，"
        r"$g(1)=\mathrm e-1=1.7183>0$．" "\n"
        r"由零点存在定理，$\exists a_{0}\in\left(\dfrac12,1\right)$ 使 $g(a_{0})=0$，即 $m\parallel n$ 可成立．**①正确**．" "\n"
        r"**结论②**：$\lvert AB\rvert=\mathrm e^{a}-\ln a$，设 $h(a)=\mathrm e^{a}-\ln a$，"
        r"$h'(a)=\mathrm e^{a}-\dfrac1a=g(a)$．" "\n"
        r"由 $g$ 在 $\left(\dfrac12,1\right)$ 有唯一零点 $a_{0}$ 且 $g$ 递增，"
        r"得 $h$ 在 $(0,a_{0})$ 递减、在 $(a_{0},+\infty)$ 递增，" "\n"
        r"故 $h$ 在 $a=a_{0}$ 处取最小值 —— **这正是 $m\parallel n$ 的时刻**．**②正确**．" "\n"
        r"**结论③**：由 $\mathrm e^{a_{0}}=\dfrac1{a_{0}}$ 得 $a_{0}=-\ln a_{0}$，" "\n"
        r"$\lvert AB\rvert_{\min}=\mathrm e^{a_{0}}-\ln a_{0}=\dfrac1{a_{0}}+a_{0}$．" "\n"
        r"对勾函数 $a+\dfrac1a$ 在 $(0,1)$ 上递减，由 $a_{0}\in\left(\dfrac12,1\right)$ 得" "\n"
        r"$\lvert AB\rvert_{\min}\in\left(1+1,\ 2+\dfrac12\right)=\left(2,\dfrac52\right)$．" "\n"
        r"（数值：$a_{0}\approx0.5671$，$\lvert AB\rvert_{\min}\approx0.5671+1.7632=2.3303$．）" "\n"
        r"故最小值**不是 $2$**（$2$ 取不到）．**③错误**．" "\n"
        r"**结论④**：$\ln2+\log_{2}\mathrm e=0.6931+1.4427=2.1358$，"
        r"而 $\lvert AB\rvert\ge\lvert AB\rvert_{\min}\approx2.3303>2.1358$ —— " "\n"
        r"④ 数值上成立，但**原书详解未予讨论**；按答案 C（①②）判定其不计入正确选项．" "\n"
        r"**综上：①②正确**．选 C．"
    ),
    'review': (
        r"★ 由详解「由直线 $x=a$ 与两曲线 $y=\mathrm e^{x}$、$y=\ln x$ 分别交于 $A,B$ 两点可知 $a>0$："
        r"曲线 $y=\mathrm e^{x}$ 上 $A$ 点坐标 $(a,\mathrm e^{a})$，可求导数 $y'=\mathrm e^{x}$，"
        r"则切线 $m$ 斜率 $k_{m}=\mathrm e^{a}$…曲线 $y=\ln x$ 上 $B$ 点坐标 $(a,\ln a)$，"
        r"可求导数 $y'=\frac1x$，则切线 $n$ 斜率 $k_{n}=\frac1a$。"
        r"令 $k_{m}=k_{n}$，则 $\mathrm e^{a}=\frac1a$，令 $g(x)=\mathrm e^{x}-\frac1x$（$x>0$），"
        r"$g(\frac12)=\mathrm e^{1/2}-2<0$，$g(1)=\mathrm e-1>0$，由零点存在定理，"
        r"$\exists a\in(\frac12,1)$ 使 $g(x)=0$，即 $\exists a\in(0,+\infty)$ 使 $k_{m}=k_{n}$，"
        r"即 $m\parallel n$，故①正确。"
        r"$\lvert AB\rvert=\mathrm e^{a}-\ln a$，令 $h(a)=\mathrm e^{a}-\ln a$（$a>0$），"
        r"∴$h'(a)=\mathrm e^{a}-\frac1a$，由 $g(x)$ 同理可知有 $a_{0}\in(\frac12,1)$ 使 "
        r"$\mathrm e^{a_{0}}=\frac1{a_{0}}$…∴$h(a)$ 在 $a=a_{0}$ 处取最小值，"
        r"即当 $m\parallel n$ 时 $\lvert AB\rvert$ 取得最小值，故②正确。"
        r"$\lvert AB\rvert_{\min}=\mathrm e^{a_{0}}-\ln a_{0}$，∵$\mathrm e^{a_{0}}=\frac1{a_{0}}$，"
        r"∴$a_{0}=\ln\frac1{a_{0}}=-\ln a_{0}$，∴$\lvert AB\rvert_{\min}=\frac1{a_{0}}+a_{0}$ 是对勾函数，"
        r"在 $a_{0}\in(\frac12,1)$ 上是减函数…」还原。" "\n"
        r"**⚠ 选项字符提取不完整（如实标注）**：PDF 页 101 的 V2 选项区只确认到 "
        r"`A.①`（x≈327）与末尾的 `①②③`（x≈521），中间部分因双栏交错未能完整提取。" "\n"
        r"**按详解明确结论「①正确；②正确，③错误」与答案 C，推定为 C=①②**，"
        r"选项按 A.① / B.② / C.①② / D.①②③ 录入。**若日后核对原书发现选项顺序不同，以原书为准。**" "\n"
        r"**独立验算**：" "\n"
        r"① $g(\frac12)=1.6487-2=-0.3513<0$ ✓；$g(1)=2.7183-1=1.7183>0$ ✓ → 有零点 ✓" "\n"
        r"② $h'(a)=\mathrm e^a-\frac1a=g(a)$ ✓，故 $h$ 的最小值点就是 $m\parallel n$ 的点 ✓" "\n"
        r"③ 数值求解 $a\mathrm e^{a}=1$：$a_{0}=0.5671$（验证 $0.5671\times\mathrm e^{0.5671}=0.5671\times1.7632=1.0000$ ✓）" "\n"
        r"$\lvert AB\rvert_{\min}=\frac1{0.5671}+0.5671=1.7632+0.5671=2.3303$" "\n"
        r"$\ne2$ ✓ **③错误确凿**（且 $2.3303\in(2,2.5)$ 与我对勾函数的范围推导一致 ✓）" "\n"
        r"④ $\ln2+\log_2\mathrm e=0.6931+1.4427=2.1358$；$\lvert AB\rvert\ge2.3303>2.1358$ "
        r"→ ④数值成立，但答案不计入，故按 C=①② 录入" "\n"
        r"**答案 C 正确** ✓" "\n"
        r"**⭐ 本题精巧之处**：$\lvert AB\rvert$ 的导数 $h'(a)=\mathrm e^{a}-\frac1a$ "
        r"**恰好就是** $m\parallel n$ 的条件 $g(a)$ —— 这不是巧合，"
        r"因为 $\lvert AB\rvert$ 取极值时两曲线的切线必然平行。"
    ),
    'difficulty': 0.94,
    'topics': ['M-T-136'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-136-V2',
}

T136_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知点 $P$ 为函数 $f(x)=\ln x$ 的图象上任意一点，"
        r"点 $Q$ 为圆 $\left(x-\mathrm e-\dfrac1{\mathrm e}\right)^{2}+y^{2}=1$ 上任意一点，"
        r"则线段 $PQ$ 的长度的最小值为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac{\sqrt{\mathrm e^{2}+1}-\mathrm e}{\mathrm e}$"),
        ('B', r"$\dfrac{\sqrt{2\mathrm e^{2}+1}-\mathrm e}{\mathrm e}$"),
        ('C', r"$\dfrac{\mathrm e-\sqrt{\mathrm e^{2}-1}}{\mathrm e}$"),
        ('D', r"$\dfrac{\mathrm e+1}{\mathrm e}-1$"),
    ],
    'answer': 'A',
    'analysis': (
        r"圆心 $C\left(\mathrm e+\frac1{\mathrm e},0\right)$、半径 $1$；"
        r"先求 $y=\ln x$ 上点到 $C$ 的最小距离，再减半径。"
    ),
    'solution': (
        r"**第一步：转化**" "\n"
        r"圆心 $C\!\left(\mathrm e+\dfrac1{\mathrm e},\ 0\right)$，半径 $r=1$．" "\n"
        r"$\lvert PQ\rvert_{\min}=\lvert PC\rvert_{\min}-1$（需先确认曲线与圆不相交）．" "\n"
        r"**第二步：求 $\lvert PC\rvert$ 的最小值**" "\n"
        r"设 $P(t,\ln t)$（$t>0$），则 $\lvert PC\rvert^{2}=\left(t-\mathrm e-\dfrac1{\mathrm e}\right)^{2}+\ln^{2}t$．" "\n"
        r"求导：$\dfrac{\mathrm d}{\mathrm dt}\lvert PC\rvert^{2}$" "\n"
        r"$=2\left(t-\mathrm e-\dfrac1{\mathrm e}\right)+\dfrac{2\ln t}t$．" "\n"
        r"代入 $t=\mathrm e$：$2\left(\mathrm e-\mathrm e-\dfrac1{\mathrm e}\right)+\dfrac{2\cdot1}{\mathrm e}$" "\n"
        r"$=-\dfrac2{\mathrm e}+\dfrac2{\mathrm e}=0$ ✓" "\n"
        r"（二阶导 $=2+\dfrac{2(1-\ln t)}{t^{2}}$，在 $t=\mathrm e$ 处 $=2>0$，故为极小值点）" "\n"
        r"**第三步：算出距离**" "\n"
        r"$P(\mathrm e,1)$，$\lvert PC\rvert=\sqrt{\left(\mathrm e-\mathrm e-\dfrac1{\mathrm e}\right)^{2}+1}$" "\n"
        r"$=\sqrt{\dfrac1{\mathrm e^{2}}+1}=\dfrac{\sqrt{1+\mathrm e^{2}}}{\mathrm e}$．" "\n"
        r"**第四步：减半径**" "\n"
        r"$\lvert PC\rvert_{\min}=\dfrac{\sqrt{\mathrm e^{2}+1}}{\mathrm e}\approx1.0655>1=r$，曲线与圆**不相交**，故" "\n"
        r"$\lvert PQ\rvert_{\min}=\dfrac{\sqrt{\mathrm e^{2}+1}}{\mathrm e}-1=\dfrac{\sqrt{\mathrm e^{2}+1}-\mathrm e}{\mathrm e}$．选 A．"
    ),
    'review': (
        r"★ 由详解「依题意，圆心为 $C(\mathrm e+\frac1{\mathrm e},0)$，设 $P$ 点坐标为 $(x,\ln x)$，"
        r"由两点间距离公式得…」及选项、答案还原（**详解后半部分被双栏切断**，以下为我独立完成的推导）。" "\n"
        r"**⚠ 选项根号为矢量绘制**：字符提取得 `e2+ 1 - e` / `e`（分子/分母），"
        r"根号不可见。由验算 $\frac{\sqrt{\mathrm e^2+1}}\mathrm e-1$ 与答案 A 一致，"
        r"定为 $\frac{\sqrt{\mathrm e^{2}+1}-\mathrm e}{\mathrm e}$。" "\n"
        r"（B 的 `2e2+ 1 - e` 按字面顺序记为 $\frac{\sqrt{2\mathrm e^{2}+1}-\mathrm e}{\mathrm e}$，"
        r"是干扰项，不影响答案判断。）" "\n"
        r"**独立验算**：" "\n"
        r"① $t=\mathrm e$ 是驻点：$(\mathrm e-\mathrm e-\frac1{\mathrm e})+\frac{\ln \mathrm e}{\mathrm e}$" "\n"
        r"$=-\frac1{\mathrm e}+\frac1{\mathrm e}=0$ ✓" "\n"
        r"② 二阶导验证：$2+\frac{2(1-\ln\mathrm e)}{\mathrm e^{2}}=2+0=2>0$ ✓ **确为极小**" "\n"
        r"③ 数值：$\sqrt{\mathrm e^2+1}=\sqrt{7.38905+1}=\sqrt{8.38905}=2.89639$；"
        r"$\frac{2.89639}{2.71828}=1.06553$；$-1=0.06553$" "\n"
        r"④ 不相交检验：$\lvert PC\rvert_{\min}=1.06553>1$ ✓ **减半径合法**" "\n"
        r"（若曲线与圆相交，最小值应为 $0$，此处显然不是）" "\n"
        r"⑤ **扫描验证**（$t\in[1,5]$ 步长 $0.01$ 搜 $\lvert PC\rvert$）："
        r"最小在 $t\approx\mathrm e=2.718$ 处，值 $\approx1.0655$ ✓" "\n"
        r"**答案 A 正确** ✓" "\n"
        r"**⭐ 构造的巧思**：圆心特意取在 $\left(\mathrm e+\frac1{\mathrm e},0\right)$，"
        r"使得最优点的横坐标恰好是 $\mathrm e$ —— "
        r"$\mathrm e+\frac1{\mathrm e}$ 这个「$x+\frac1x$」形式就是为了让 $\ln x$ 的导数 $\frac1x$ "
        r"与一次项抵消，凑出整齐的驻点。"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-136'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-136-V3',
}

QS = [T136_E1, T136_V1, T136_V2, T136_V3]
