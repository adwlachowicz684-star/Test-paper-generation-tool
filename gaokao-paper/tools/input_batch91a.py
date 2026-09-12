# -*- coding: utf-8 -*-
r"""第 91 批：三角函数与解三角形综合（12 题）

M-T-224（4）、M-T-216（4）、M-T-217（4）

## ★★ 12 题全部独立验算（数值对拍 / 端点检验）

| 题 | 我的验算 | 答案 |
|---|---|---|
| M-T-224-E1 | $a=\sqrt7$，$m_a=\frac12\sqrt{2+18-7}=\frac{\sqrt{13}}2$ ✓；$S=\frac{3\sqrt3}4$ | **$\frac\pi3$；$\frac{3\sqrt3}4$** |
| M-T-224-V1 | 选① $c=4\sqrt5=8.944$，$AD^2=65$；选②另解 $c=10\sqrt5$，$a=20$，$AD=10\sqrt2$ | **$\sqrt{65}$；$\sqrt{65}$ 或 $10\sqrt2$** |
| M-T-224-V2 | $b=13$ ⟹ $a^2=259$，$m_a^2=\frac{338+50-259}4=\frac{129}4$ ✓；$\cos\angle ADB+\cos\angle ADC=0$ ✓ | **$\frac{2\pi}3$；$\frac{65\sqrt3}4$** |
| M-T-224-V3 | $b=2\sqrt3\sin\frac\pi3=3$，$ac=4$，$a^2+c^2=13$（判别式 $21-16=5>0$）⟹ $S=\sqrt3$ | **$\frac\pi3$；$\sqrt3$** |
| M-T-216-E1 | 四点抽样 $f(x)$ 与 $\sin(2x+\frac\pi6)$ 完全相等；$f(\frac C2)=1$ ⟹ $C=\frac\pi3$ | **$\pi$；正三角形** |
| M-T-216-V1 | 化简 $f=\sin(\omega x-\frac\pi3)+\frac{\sqrt3}2+m$；②③ 都只给 $m$ 且冲突，故必选①；增区间上界 $\frac{5\pi}{12}$ | **见解析；$\frac{5\pi}{12}$** |
| M-T-216-V2 | $f=2\sin(2x+\frac\pi3)$；$g=2\sin(\frac x2+\frac\pi6)$，扫描值域 $[-1,2]$ | **$\pi$，$x=\frac\pi{12}+\frac{k\pi}2$；$[-1,2]$** |
| M-T-216-V3 | 按 $\cos^2x$ 版代入 $\theta=0$ 得 $\cos2x=0\in[-1,1]$ ✓，且能复现详解中间式 | **$\theta=\frac{k\pi}2-\frac\pi4$；$[-\frac{\sqrt{15}}3,\frac{\sqrt{15}}3]$** |
| M-T-217-E1 | $f=\sin(x+\frac\pi6)$；选① $-(\cos(2x+\frac\pi6))$、选② $\sin(2x-\frac\pi3)$，值域都 $[-1,\frac12]$ | **见解析；$a\in[-1,\frac12]$** |
| M-T-217-V1 | 左移后 $2\sin(2x+\varphi+\frac{5\pi}6)$ 偶 ⟹ $\varphi=-\frac\pi3$；区间端点值 $1,2,\sqrt3$ | **$2\sin(2x-\frac\pi6)$；$[\sqrt3,2)$** |
| M-T-217-V2 | $\omega=\frac34$ 时相位区间 $[-\frac\pi2,\frac\pi2]$；零点间距 $\frac\pi2$，30 个零点跨 29 个间隔 | **$2\sin(2x+\frac\pi3)$；$(0,\frac34]$；$\frac{29\pi}2$** |
| M-T-217-V3 | $2\sin^2\frac\alpha2-1=-\cos\alpha$ ⟹ $f=2\sin(\omega x+\varphi-\frac\pi6)$；$m=1$ 时两根 $x=0,\frac\pi6$ ✓ | **$2\cos2x$；$[1,2)$** |

## 六处根号 / 上标还原（全部有硬判据）

- M-T-224-E1 答案 `3 3/4` ⟹ **$\frac{3\sqrt3}4$**；中线 `13/2` ⟹ **$\frac{\sqrt{13}}2$**（$m_a=\frac12\sqrt{2b^2+2c^2-a^2}$ 反推）
- M-T-224-V1 题面 `cosA = 5/5` ⟹ **$\frac{\sqrt5}5$**（$\frac55=1$ ⟹ $A=0$，退化）；
  答案 `65`、`10 2`、`4 5` ⟹ **$\sqrt{65}$、$10\sqrt2$、$4\sqrt5$**
- M-T-224-V2 题面 `3(acosC-b)` ⟹ **$\sqrt3(a\cos C-b)$**（否则 $\tan A=-\frac1{\sqrt3}$，$A=\frac{5\pi}6$ 与答案不符）；
  `129/2` ⟹ **$\frac{\sqrt{129}}2$**；答案 `65 3/4` ⟹ **$\frac{65\sqrt3}4$**
- M-T-224-V3 题面「外接圆半径为 3」⟹ **$\sqrt3$**（否则 $b=2\cdot3\cdot\frac{\sqrt3}2=3\sqrt3\ne3$，与详解 $b=3$ 不符）；
  `17/2` ⟹ **$\frac{\sqrt{17}}2$**；答案 `3.` ⟹ **$\sqrt3$**
- M-T-216-V3 题面 `cos2x` ⟹ **$\cos^2x$**（**上标丢失**）。
  判据极硬：按 $\cos2x$ 版，方程化为 $\cos2x=\frac12$ 与 $\theta$ 无关（取 $\theta=0$、$x=\frac\pi6$ 代入验证成立 ✓），
  题目将失去意义；按 $\cos^2x$ 版化简恰得详解的中间式 $2(\sin2\theta-1)\cos2x=\sin2\theta$ ✓
- M-T-217-V1 答案 `[ 3,2)` ⟹ **$[\sqrt3,2)$**

## 一处题干残缺的找回（M-T-217-V3）

V3 的题干被截到 **V2 详解的末尾**（原文 `11. 已知函数f(x)=3sin(ωx+φ)+2sin2(ωx+φ)/2-1(ω>0,0<φ<π) 为偶函数，且f(x) 图象的相邻两对称轴间的距离为π/2`）。
已从 V2 solution 尾部取回并补全，否则 V3 只有「(1) 求 $f(x)$ 的解析式」而无函数可求。

## 一题跳过（M-T-214，4 题）

「$y=A\sin(\omega x+\varphi)$ 的部分图象如图所示」——四题**全部依赖未提取的图象**。
关键数据（最高点 $\left(\frac\pi{12},2\right)$、$A+B=1$ 与 $-A+B=-3$ 等）只存在于图中，
若不补图则学生无从下手，若改写题干则改变了原题。本批改录 M-T-217（同为三角函数、无图依赖）。
"""

T224_E1 = {
    'type': '解答',
    'stem_text': (
        r"在 $\triangle ABC$ 中，$a\sin\left(B+\dfrac\pi6\right)=\dfrac{b+c}{2}$，且 $BC$ 边上的中线长为 $\dfrac{\sqrt{13}}2$，$AB=3$．" "\n"
        r"(1) 求角 $A$ 的大小；" "\n"
        r"(2) 求 $\triangle ABC$ 的面积．"
    ),
    'opts': [],
    'answer': r"(1) $A=\dfrac\pi3$；(2) $S_{\triangle ABC}=\dfrac{3\sqrt3}4$",
    'analysis': (
        r"(1) 正弦定理把 $a,b,c$ 换成 $\sin A,\sin B,\sin C$，再用 $\sin C=\sin(A+B)$ 展开，"
        r"$\sin A\cos B$ 项恰好抵消，剩下 $\sin B(\sqrt3\sin A-\cos A-1)=0$；"
        r"(2) 用向量式 $\vec{AB}+\vec{AC}=2\vec{AD}$ 两边平方，配 $A=\frac\pi3$ 与 $c=3$ 解出 $b$．"
    ),
    'solution': (
        r"**(1)** 由正弦定理 $a=2R\sin A$，$b=2R\sin B$，$c=2R\sin C$，代入得" "\n"
        r"$\sin A\sin\left(B+\dfrac\pi6\right)=\dfrac{\sin B+\sin C}{2}$，" "\n"
        r"即 $\sin A\left(\dfrac{\sqrt3}2\sin B+\dfrac12\cos B\right)=\dfrac{\sin B+\sin C}2$．" "\n"
        r"两边乘 $2$：$\sqrt3\sin A\sin B+\sin A\cos B=\sin B+\sin C$．" "\n"
        r"$\because\sin C=\sin(A+B)=\sin A\cos B+\cos A\sin B$，" "\n"
        r"$\therefore\sqrt3\sin A\sin B+\sin A\cos B=\sin B+\sin A\cos B+\cos A\sin B$，" "\n"
        r"即 $\sqrt3\sin A\sin B=\sin B+\cos A\sin B$，整理得 $\sin B\left(\sqrt3\sin A-\cos A-1\right)=0$．" "\n"
        r"$\because B\in(0,\pi)$，$\therefore\sin B\ne0$，$\therefore\sqrt3\sin A-\cos A=1$，" "\n"
        r"即 $2\sin\left(A-\dfrac\pi6\right)=1$，$\sin\left(A-\dfrac\pi6\right)=\dfrac12$．" "\n"
        r"$\because A\in(0,\pi)$，$\therefore A-\dfrac\pi6=\dfrac\pi6$，即 $A=\dfrac\pi3$．" "\n"
        r"**(2)** 设 $BC$ 的中点为 $D$，则 $\vec{AB}+\vec{AC}=2\vec{AD}$，两边平方得" "\n"
        r"$\lvert\vec{AB}\rvert^{2}+\lvert\vec{AC}\rvert^{2}+2\lvert\vec{AB}\rvert\lvert\vec{AC}\rvert\cos A=4\lvert\vec{AD}\rvert^{2}$．" "\n"
        r"$\because AB=c=3$，$A=\dfrac\pi3$，$AD=\dfrac{\sqrt{13}}2$，$\therefore9+b^{2}+2\times3b\times\dfrac12=4\times\dfrac{13}4=13$，" "\n"
        r"即 $b^{2}+3b-4=0$，解得 $b=1$（负值舍去）．" "\n"
        r"$\therefore S_{\triangle ABC}=\dfrac12bc\sin A=\dfrac12\times1\times3\times\dfrac{\sqrt3}2=\dfrac{3\sqrt3}4$．"
    ),
    'review': (
        r"**① 提 $\sin B$ 是题眼**：$\sqrt3\sin A\sin B=\sin B+\cos A\sin B$ ⟹ 提公因子 $\sin B$，" "\n"
        r"再由 $\sin B\ne0$ 放行，得到只含 $A$ 的方程 ✓✓✓" "\n"
        r"② **$\sin C=\sin(A+B)$ 展开后 $\sin A\cos B$ 抵消**：这是「边化角」能成功的根本原因，" "\n"
        r"若展开后不抵消，说明方向错了 ✓✓✓" "\n"
        r"③ **辅助角方向**：$\sqrt3\sin A-\cos A=2\sin\left(A-\frac\pi6\right)$（**是减号**），" "\n"
        r"写成 $A+\frac\pi6$ 则 $2\sin(A+\frac\pi6)=1$ 会给出 $A=0$ 或 $\frac{2\pi}3$，与答案矛盾 ✓✓✓" "\n"
        r"④ **中线用向量平方而非中线长公式**：$\vec{AB}+\vec{AC}=2\vec{AD}$ 一步到位，" "\n"
        r"比记 $m_a=\frac12\sqrt{2b^2+2c^2-a^2}$ 更不易错 ✓✓✓" "\n"
        r"⑤ 数值对拍：$b=1,c=3,A=\frac\pi3$ ⟹ $a^2=1+9-3=7$，$a=\sqrt7$；" "\n"
        r"$m_a=\frac12\sqrt{2\times1+2\times9-7}=\frac12\sqrt{13}=\frac{\sqrt{13}}2$ ✓ **与题设完全吻合**" "\n"
        r"$S=\frac12\times1\times3\times\frac{\sqrt3}2=\frac{3\sqrt3}4=1.2990$ ✓" "\n"
        r"**答案 $\frac\pi3$、$\frac{3\sqrt3}4$ 均正确** ✓" "\n"
        r"**⭐⭐ 通法（中线 + 边角混合）**：" "\n"
        r"① ⭐⭐ **中线题首选向量式** $\vec{AB}+\vec{AC}=2\vec{AD}$，两边平方即出现 $b^2+c^2+2bc\cos A$ ✓；" "\n"
        r"② ⭐⭐ **$\sin C=\sin(A+B)$ 展开后观察抵消**：凡条件含 $b+c$ 或 $a\sin(\cdots)$，必走这条路 ✓；" "\n"
        r"③ ⭐⭐ **提公因子后由 $\sin B\ne0$ 放行** —— 三角形内角的正弦永不为零，这是标准收尾 ✓；" "\n"
        r"④ ⭐⭐ **解出 $b$ 后用中线长反验**：$m_a=\frac12\sqrt{2b^2+2c^2-a^2}$ 必须等于题设值 ✓；" "\n"
        r"⑤ ⚠ **辅助角是减号时别写成加号**，$\sqrt3\sin A-\cos A=2\sin(A-\frac\pi6)$ ✓✓"
    ),
    'difficulty': 0.78,
    'topics': ['M-T-224'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-224-E1',
}

T224_V1 = {
    'type': '解答',
    'stem_text': (
        r"在① $\dfrac a{\cos A}=\dfrac b{\cos B}$；② $\dfrac{a^{2}}{\tan A}=\dfrac{b^{2}}{\tan B}$ 这两个条件中任选一个，" "\n"
        r"补充在下面问题中并作答．已知在锐角 $\triangle ABC$ 中，角 $A$，$B$，$C$ 的对边分别为 $a$，$b$，$c$，____．" "\n"
        r"(1) 判断 $\triangle ABC$ 的形状；" "\n"
        r"(2) 在 (1) 的条件下，若 $\cos A=\dfrac{\sqrt5}5$，$b=10$，$AD$ 为 $BC$ 边上的中线，求 $AD$ 的长．"
    ),
    'opts': [],
    'answer': (
        r"(1) 选①，$\triangle ABC$ 是等腰三角形；选②，$\triangle ABC$ 是等腰三角形或直角三角形；" "\n"
        r"(2) 选①，$AD=\sqrt{65}$；选②，$AD=\sqrt{65}$ 或 $AD=10\sqrt2$"
    ),
    'analysis': (
        r"(1) 选①用正弦定理化为 $\tan A=\tan B$；选②化为 $\sin A\cos A=\sin B\cos B$ 即 $\sin2A=\sin2B$，"
        r"由正弦相等得 $2A=2B$ 或 $2A+2B=\pi$ 两支；(2) 等腰支中 $a=b=10$，先求底边 $c=2b\cos A$，"
        r"再在 $\triangle ABD$ 中用余弦定理；直角支中 $C=\frac\pi2$，由 $\cos A$ 得斜边与 $BC$，用勾股求 $AD$．"
    ),
    'solution': (
        r"**(1) 选①**：由正弦定理 $\dfrac a{\cos A}=\dfrac b{\cos B}$ 得 $\dfrac{\sin A}{\cos A}=\dfrac{\sin B}{\cos B}$，即 $\tan A=\tan B$．" "\n"
        r"又 $A,B$ 是三角形内角，$\therefore A=B$，$\triangle ABC$ 是**等腰三角形**．" "\n"
        r"**选②**：由正弦定理得 $\dfrac{\sin^{2}A}{\tan A}=\dfrac{\sin^{2}B}{\tan B}$，即 $\sin A\cos A=\sin B\cos B$，" "\n"
        r"$\therefore\sin2A=\sin2B$．又 $A,B$ 为三角形内角，" "\n"
        r"$\therefore2A=2B$ 或 $2A+2B=\pi$，即 $A=B$ 或 $A+B=\dfrac\pi2$，" "\n"
        r"$\therefore\triangle ABC$ 是**等腰三角形或直角三角形**．" "\n"
        r"**(2) 选①**：$A=B$，则 $a=b=10$，$BD=\dfrac a2=5$．" "\n"
        r"由正弦定理 $c=\dfrac{a\sin C}{\sin A}=\dfrac{a\sin2A}{\sin A}=2a\cos A=2\times10\times\dfrac{\sqrt5}5=4\sqrt5$．" "\n"
        r"在 $\triangle ABD$ 中由余弦定理：" "\n"
        r"$AD^{2}=AB^{2}+BD^{2}-2AB\cdot BD\cos B=\left(4\sqrt5\right)^{2}+5^{2}-2\times4\sqrt5\times5\times\dfrac{\sqrt5}5=80+25-40=65$，" "\n"
        r"$\therefore AD=\sqrt{65}$．" "\n"
        r"**选②**：当 $A=B$ 时同选①，$AD=\sqrt{65}$；" "\n"
        r"当 $A+B=\dfrac\pi2$ 时，$C=\dfrac\pi2$．由 $\cos A=\dfrac{\sqrt5}5$ 得 $\sin A=\dfrac{2\sqrt5}5$．" "\n"
        r"$\therefore c=\dfrac b{\cos A}=\dfrac{10}{\sqrt5/5}=10\sqrt5$，$a=c\sin A=10\sqrt5\times\dfrac{2\sqrt5}5=20$，" "\n"
        r"$CD=\dfrac a2=10$．在 ${\rm Rt}\triangle ACD$ 中：$AD=\sqrt{AC^{2}+CD^{2}}=\sqrt{10^{2}+10^{2}}=10\sqrt2$．" "\n"
        r"$\therefore$ 选②时 $AD=\sqrt{65}$ 或 $10\sqrt2$．"
    ),
    'review': (
        r"**① 两个条件给出的信息量不同**：①只给 $A=B$（一支），②给 $\sin2A=\sin2B$（**两支**），" "\n"
        r"这正是「选②有两种答案」的根源 ✓✓✓" "\n"
        r"② **$\sin2A=\sin2B$ 必须写全两支**：$2A=2B$ 或 $2A+2B=\pi$。" "\n"
        r"只写 $A=B$ 会漏掉直角三角形这一支 ✓✓✓" "\n"
        r"③ **等腰支求 $c$ 用 $c=2a\cos A$**：因 $A=B$ 时 $C=\pi-2A$，$\sin C=\sin2A$，" "\n"
        r"$\frac{c}{\sin2A}=\frac a{\sin A}$ ⟹ $c=2a\cos A$ ✓✓✓" "\n"
        r"④ **直角支中 $c$ 是斜边**：$C=\frac\pi2$ ⟹ $c=\frac b{\cos A}$（$\cos A=\frac bc$）✓✓✓" "\n"
        r"⑤ 数值对拍：$\cos A=\frac{\sqrt5}5=0.4472$，$\cos2A=2\times0.2-1=-0.6$，$\cos C=0.6$；" "\n"
        r"$c^2=100+100-200\times0.6=80$，$c=8.944=4\sqrt5$ ✓；" "\n"
        r"$AD^2=80+25-2\times8.944\times5\times0.4472=65$ ✓；" "\n"
        r"直角支：$c=22.361=10\sqrt5$，$a=20$，$AD=\sqrt{100+100}=14.142=10\sqrt2$ ✓ **完全闭合**" "\n"
        r"⑥ ⚠ **题设说锐角三角形，但条件②可推出 $C=\frac\pi2$（直角）**，二者不完全相容；" "\n"
        r"原书答案保留了 $10\sqrt2$ 这一支，故一并录入，此处如实说明 ✓" "\n"
        r"**⭐⭐ 通法（三选一 / 二选一的条件题）**：" "\n"
        r"① ⭐⭐ **先判每个条件的信息量**：只含一边的（$\frac a{\cos A}=\frac b{\cos B}$）给一支；" "\n"
        r"含平方或二倍角的（$\frac{a^2}{\tan A}$）往往给两支 ✓；" "\n"
        r"② ⭐⭐ **$\sin2A=\sin2B$ ⟹ $A=B$ 或 $A+B=\frac\pi2$** 是固定结论，可背 ✓；" "\n"
        r"③ ⭐⭐ **等腰三角形中 $c=2a\cos A$**（底边 = $2\times$腰$\times\cos$底角）✓；" "\n"
        r"④ ⭐⭐ **直角三角形中 $c=\frac b{\cos A}$**，配勾股求中线 ✓；" "\n"
        r"⑤ ⚠ **答案必须按「选① / 选②」分列**，且选②的两个值都要写全 ✓✓"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-224'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-224-V1',
}

T224_V2 = {
    'type': '解答',
    'stem_text': (
        r"在 $\triangle ABC$ 中，内角 $A$，$B$，$C$ 的对边分别为 $a$，$b$，$c$，且 $\sqrt3\left(a\cos C-b\right)=c\sin A$．" "\n"
        r"(1) 求角 $A$；" "\n"
        r"(2) 若 $AD$ 为 $BC$ 边上的中线，$AD=\dfrac{\sqrt{129}}2$，$AB=5$，求 $\triangle ABC$ 的面积．"
    ),
    'opts': [],
    'answer': r"(1) $A=\dfrac{2\pi}3$；(2) $S_{\triangle ABC}=\dfrac{65\sqrt3}4$",
    'analysis': (
        r"(1) 正弦定理边化角后，把 $\sin B$ 写成 $\sin(A+C)$ 展开，$\sin A\cos C$ 项恰好抵消，"
        r"剩下 $-\sqrt3\cos A\sin C=\sin A\sin C$，约去 $\sin C$ 得 $\tan A$；"
        r"(2) 在 $\triangle ABD$ 与 $\triangle ACD$ 中各写一次余弦定理，利用 $\cos\angle ADB+\cos\angle ADC=0$ 消去角，"
        r"再与 $\triangle ABC$ 的余弦定理联立解出 $b$．"
    ),
    'solution': (
        r"**(1)** 由正弦定理得 $\sqrt3\left(\sin A\cos C-\sin B\right)=\sin C\sin A$．" "\n"
        r"$\because\sin B=\sin(A+C)=\sin A\cos C+\cos A\sin C$，" "\n"
        r"$\therefore\sqrt3\left(\sin A\cos C-\sin A\cos C-\cos A\sin C\right)=\sin C\sin A$，" "\n"
        r"即 $-\sqrt3\cos A\sin C=\sin A\sin C$．" "\n"
        r"$\because\sin C\ne0$，$\therefore\tan A=-\sqrt3$，又 $0<A<\pi$，$\therefore A=\dfrac{2\pi}3$．" "\n"
        r"**(2)** 设 $AC=b$，则 $BD=DC=\dfrac a2$．在 $\triangle ABD$ 中，由余弦定理：" "\n"
        r"$\cos\angle ADB=\dfrac{AD^{2}+BD^{2}-AB^{2}}{2\cdot AD\cdot BD}=\dfrac{\dfrac{129}4+\dfrac{a^{2}}4-25}{2\times\dfrac{\sqrt{129}}2\times\dfrac a2}=\dfrac{29+a^{2}}{2\sqrt{129}\,a}$；" "\n"
        r"在 $\triangle ACD$ 中，由余弦定理：" "\n"
        r"$\cos\angle ADC=\dfrac{AD^{2}+DC^{2}-AC^{2}}{2\cdot AD\cdot DC}=\dfrac{\dfrac{129}4+\dfrac{a^{2}}4-b^{2}}{2\times\dfrac{\sqrt{129}}2\times\dfrac a2}=\dfrac{129+a^{2}-4b^{2}}{2\sqrt{129}\,a}$．" "\n"
        r"$\because\angle ADB+\angle ADC=\pi$，$\therefore\cos\angle ADB+\cos\angle ADC=0$，" "\n"
        r"即 $\left(29+a^{2}\right)+\left(129+a^{2}-4b^{2}\right)=0$，得 $2a^{2}-4b^{2}+158=0$．" "\n"
        r"在 $\triangle ABC$ 中由余弦定理：$a^{2}=b^{2}+c^{2}-2bc\cos A=b^{2}+25-2\times5b\times\left(-\dfrac12\right)=b^{2}+25+5b$．" "\n"
        r"代入上式：$2\left(b^{2}+25+5b\right)-4b^{2}+158=0$，即 $b^{2}-5b-104=0$，" "\n"
        r"解得 $b=13$ 或 $b=-8$（舍去）．" "\n"
        r"$\therefore S_{\triangle ABC}=\dfrac12bc\sin A=\dfrac12\times13\times5\times\dfrac{\sqrt3}2=\dfrac{65\sqrt3}4$．"
    ),
    'review': (
        r"**① 把 $\sin B$ 写成 $\sin(A+C)$ 是唯一出路**：因为式子里的 $\cos C$ 要用 $C$ 表达，" "\n"
        r"展开后 $\sin A\cos C$ 恰好抵消，只剩 $-\sqrt3\cos A\sin C$ ✓✓✓" "\n"
        r"② **约去 $\sin C$ 而非 $\sin A$**：右边是 $\sin A\sin C$，两边都有 $\sin C$，约去后得 $\tan A$ ✓✓✓" "\n"
        r"③ ⚠ **两式相加时常数项不同**：$\cos\angle ADB$ 的分子是 $\frac{129}4+\frac{a^2}4-\mathbf{25}$（减 $AB^2$，" "\n"
        r"$25=\frac{100}4$，故 $129-100=29$）；而 $\cos\angle ADC$ 减的是 $b^2$，化成 $\frac{4b^2}4$，" "\n"
        r"$129$ **保持不变**。所以相加是 $29+129=158$ 而不是 $29+29=58$ —— 这是我第一遍算错的地方 ✓✓✓" "\n"
        r"④ **$\cos\angle ADB+\cos\angle ADC=0$ 是中线题的标准桥梁**（互补角余弦相反）✓✓✓" "\n"
        r"⑤ 数值对拍：$b=13,c=5,A=\frac{2\pi}3$ ⟹ $a^2=169+25+65=259$；" "\n"
        r"$m_a^2=\frac{2\times169+2\times25-259}4=\frac{338+50-259}4=\frac{129}4$ ✓ **与题设 $AD=\frac{\sqrt{129}}2$ 吻合**；" "\n"
        r"代回两余弦：$AD^2=\frac{129}4=32.25$，$BD^2=\frac{259}4=64.75$，$AB^2=25$，$AC^2=169$，" "\n"
        r"$(32.25+64.75-25)+(32.25+64.75-169)=72-72=0$ ✓；" "\n"
        r"$S=\frac12\times13\times5\times\frac{\sqrt3}2=\frac{65\sqrt3}4=28.146$ ✓ **完全闭合**" "\n"
        r"**⭐⭐ 通法（中线 + 互补角余弦）**：" "\n"
        r"① ⭐⭐ **中线题在两个小三角形中各写一次余弦定理，利用 $\cos\angle ADB+\cos\angle ADC=0$ 消角** ✓；" "\n"
        r"② ⭐⭐ **消角后仍有两个未知量 $a,b$**，必须再写一次 $\triangle ABC$ 的余弦定理（用已求出的 $A$）联立 ✓；" "\n"
        r"③ ⭐⭐ **$\sin B=\sin(A+C)$ 展开是「边化角」的收尾动作**，展开后必有一项抵消 ✓；" "\n"
        r"④ ⚠ **相加前把分子通分到同分母**，尤其注意「减 $AB^2$」与「减 $AC^2$」造成的常数差 ✓✓；" "\n"
        r"⑤ ⚠ **$b=-8$ 必须舍去**（边长为正），这是唯一的取根依据 ✓✓"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-224'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-224-V2',
}

T224_V3 = {
    'type': '解答',
    'stem_text': (
        r"在 $\triangle ABC$ 中，角 $A$，$B$，$C$ 所对的边分别为 $a$，$b$，$c$，且满足 $\cos C=\dfrac ab-\dfrac c{2b}$．" "\n"
        r"(1) 求角 $B$；" "\n"
        r"(2) 若 $\triangle ABC$ 外接圆的半径为 $\sqrt3$，且 $AC$ 边上的中线长为 $\dfrac{\sqrt{17}}2$，求 $\triangle ABC$ 的面积．"
    ),
    'opts': [],
    'answer': r"(1) $B=\dfrac\pi3$；(2) $S_{\triangle ABC}=\sqrt3$",
    'analysis': (
        r"(1) 去分母得 $2b\cos C=2a-c$，正弦定理化角后把 $\sin A$ 写成 $\sin(B+C)$ 展开，"
        r"$2\sin B\cos C$ 项抵消，得 $\sin C(2\cos B-1)=0$；"
        r"(2) 由 $R=\sqrt3$ 与 $B=\frac\pi3$ 得 $b=3$，再用向量式 $2\vec{BD}=\vec{BA}+\vec{BC}$ 平方得 $a^2+c^2+ac=17$，"
        r"与余弦定理 $a^2+c^2-ac=9$ 相减即得 $ac$．"
    ),
    'solution': (
        r"**(1)** 由 $\cos C=\dfrac ab-\dfrac c{2b}$ 得 $2b\cos C=2a-c$．由正弦定理：" "\n"
        r"$2\sin B\cos C=2\sin A-\sin C=2\sin(B+C)-\sin C=2\sin B\cos C+2\cos B\sin C-\sin C$．" "\n"
        r"$\therefore2\cos B\sin C-\sin C=0$，即 $\sin C\left(2\cos B-1\right)=0$．" "\n"
        r"$\because C\in(0,\pi)$，$\therefore\sin C\ne0$，$\therefore\cos B=\dfrac12$．" "\n"
        r"又 $B\in(0,\pi)$，$\therefore B=\dfrac\pi3$．" "\n"
        r"**(2)** 由正弦定理 $\dfrac b{\sin B}=2R=2\sqrt3$，$\therefore b=2\sqrt3\times\dfrac{\sqrt3}2=3$．" "\n"
        r"设 $D$ 为 $AC$ 边的中点，则 $BD=\dfrac{\sqrt{17}}2$．由向量加法法则 $2\vec{BD}=\vec{BA}+\vec{BC}$，两边平方：" "\n"
        r"$4\lvert\vec{BD}\rvert^{2}=\lvert\vec{BA}\rvert^{2}+\lvert\vec{BC}\rvert^{2}+2\vec{BA}\cdot\vec{BC}$，即 $17=c^{2}+a^{2}+2ac\cos B=c^{2}+a^{2}+ac$　①" "\n"
        r"又由余弦定理：$b^{2}=c^{2}+a^{2}-2ac\cos B$，即 $9=c^{2}+a^{2}-ac$　②" "\n"
        r"①$-$② 得 $8=2ac$，即 $ac=4$．" "\n"
        r"$\therefore S_{\triangle ABC}=\dfrac12ac\sin B=\dfrac12\times4\times\dfrac{\sqrt3}2=\sqrt3$．"
    ),
    'review': (
        r"**① 去分母优先**：$\cos C=\frac ab-\frac c{2b}$ 两边乘 $2b$ 得 $2b\cos C=2a-c$，" "\n"
        r"化成「边 × 角」的乘积后才好用正弦定理 ✓✓✓" "\n"
        r"② **$2\sin B\cos C$ 在左右两边同时出现并抵消**：这是本题设计的关键，" "\n"
        r"抵消后直接得到 $\sin C(2\cos B-1)=0$ ✓✓✓" "\n"
        r"③ **两式相减即得 $ac$**：① $a^2+c^2+ac=17$ 与 ② $a^2+c^2-ac=9$ **只差 $ac$ 的符号**，" "\n"
        r"相减是这类题最快的一步，不需求出 $a,c$ 各自的值 ✓✓✓" "\n"
        r"④ **$R=\sqrt3$ 直接给 $b$**：$b=2R\sin B$，无需绕道 ✓✓✓" "\n"
        r"⑤ 数值对拍：$ac=4$，$a^2+c^2=13$ ⟹ $(a+c)^2=21$，判别式 $21-16=5>0$（**三角形确实存在**）；" "\n"
        r"$a,c=\frac{\sqrt{21}\pm\sqrt5}2=1.173,\ 3.409$；$S=\frac12\times4\times\frac{\sqrt3}2=\sqrt3=1.7321$ ✓" "\n"
        r"⑥ 原题「外接圆半径为 3」实为 $\sqrt3$：若 $R=3$ 则 $b=2\times3\times\frac{\sqrt3}2=3\sqrt3\ne3$，" "\n"
        r"与详解的 $b=3$ 矛盾 ✓ **根号丢失确认**" "\n"
        r"**⭐⭐ 通法（中线 + 两式相减）**：" "\n"
        r"① ⭐⭐ **向量式 $2\vec{BD}=\vec{BA}+\vec{BC}$ 平方得 $a^2+c^2+2ac\cos B$**（注意是 $+\cos B$）✓；" "\n"
        r"② ⭐⭐ **余弦定理给 $a^2+c^2-2ac\cos B$**，两式**只差交叉项的符号**，相减即得 $ac$ ✓；" "\n"
        r"③ ⭐⭐ **求得 $ac$ 后不必解出 $a,c$**，面积 $\frac12ac\sin B$ 直接可用 ✓；" "\n"
        r"④ ⭐⭐ **$2R\sin B$ 求边**：给外接圆半径时优先用正弦定理 ✓；" "\n"
        r"⑤ ⚠ **最后用判别式确认三角形存在**：$(a+c)^2-4ac\ge0$，否则说明前面算错 ✓✓"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-224'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-224-V3',
}

T216_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=2\sin\left(\dfrac\pi4-x\right)\cos\left(\dfrac\pi4-x\right)-\cos\left(\dfrac\pi3+2x\right)$．" "\n"
        r"(1) 求函数 $f(x)$ 的最小正周期；" "\n"
        r"(2) 在锐角 $\triangle ABC$ 中，内角 $A$，$B$，$C$ 所对的边分别为 $a$，$b$，$c$，" "\n"
        r"若 $f\left(\dfrac C2\right)=1$，且 $c^{2}=ab$，试判断 $\triangle ABC$ 的形状．"
    ),
    'opts': [],
    'answer': r"(1) $T=\pi$；(2) $\triangle ABC$ 是正三角形",
    'analysis': (
        r"(1) 用 $2\sin\theta\cos\theta=\sin2\theta$ 把第一项化为 $\cos2x$，再展开 $\cos\left(\frac\pi3+2x\right)$，"
        r"合并为 $\sin\left(2x+\frac\pi6\right)$；(2) 由 $f\left(\frac C2\right)=1$ 得 $\sin\left(C+\frac\pi6\right)=1$ 从而 $C=\frac\pi3$，"
        r"再与 $c^2=ab$ 及余弦定理联立得 $a=b$．"
    ),
    'solution': (
        r"**(1)** $f(x)=2\sin\left(\dfrac\pi4-x\right)\cos\left(\dfrac\pi4-x\right)-\cos\left(\dfrac\pi3+2x\right)$" "\n"
        r"$=\sin\left(\dfrac\pi2-2x\right)-\left(\cos\dfrac\pi3\cos2x-\sin\dfrac\pi3\sin2x\right)$" "\n"
        r"$=\cos2x-\left(\dfrac12\cos2x-\dfrac{\sqrt3}2\sin2x\right)=\dfrac{\sqrt3}2\sin2x+\dfrac12\cos2x=\sin\left(2x+\dfrac\pi6\right)$．" "\n"
        r"$\therefore T=\dfrac{2\pi}2=\pi$，即函数的最小正周期为 $\pi$．" "\n"
        r"**(2)** $f\left(\dfrac C2\right)=\sin\left(C+\dfrac\pi6\right)=1$．" "\n"
        r"$\because0<C<\dfrac\pi2$，$\therefore\dfrac\pi6<C+\dfrac\pi6<\dfrac{2\pi}3$，$\therefore C+\dfrac\pi6=\dfrac\pi2$，$C=\dfrac\pi3$．" "\n"
        r"又 $c^{2}=ab$，由余弦定理 $c^{2}=a^{2}+b^{2}-2ab\cos C=a^{2}+b^{2}-ab$，" "\n"
        r"$\therefore ab=a^{2}+b^{2}-ab$，即 $\left(a-b\right)^{2}=0$，$a=b$．" "\n"
        r"$\because C=\dfrac\pi3$ 且 $a=b$，$\therefore A=B=\dfrac{\pi-C}2=\dfrac\pi3$，" "\n"
        r"$\therefore\triangle ABC$ 是**正三角形**．"
    ),
    'review': (
        r"**① 第一项用倍角公式一步化 $\cos2x$**：$2\sin\theta\cos\theta=\sin2\theta$，$\theta=\frac\pi4-x$ ⟹ $\sin(\frac\pi2-2x)=\cos2x$ ✓✓✓" "\n"
        r"② **展开 $\cos(\frac\pi3+2x)$ 时符号**：$=\frac12\cos2x-\frac{\sqrt3}2\sin2x$，" "\n"
        r"前面有负号 ⟹ $-\frac12\cos2x+\frac{\sqrt3}2\sin2x$ ✓✓✓" "\n"
        r"③ **合并方向**：$\frac{\sqrt3}2\sin2x+\frac12\cos2x=\sin(2x+\frac\pi6)$（$\cos$ 系数 $\frac12=\sin\frac\pi6$）✓✓✓" "\n"
        r"④ **$f(\frac C2)=1$ 时相位范围必须核对**：$C\in(0,\frac\pi2)$ ⟹ $C+\frac\pi6\in(\frac\pi6,\frac{2\pi}3)$，" "\n"
        r"$\frac\pi2$ 在此区间内 ✓，故 $C=\frac\pi3$ 是唯一解 ✓✓✓" "\n"
        r"⑤ **判断形状要给足理由**：由 $a=b$ 只能得等腰，必须再用 $C=\frac\pi3$ 推出 $A=B=\frac\pi3$ 才是正三角形 ✓✓✓" "\n"
        r"⑥ 数值对拍：取 $x=0,0.3,1.1,2.0$ 四点，$2\sin(\frac\pi4-x)\cos(\frac\pi4-x)-\cos(\frac\pi3+2x)$ 与 $\sin(2x+\frac\pi6)$" "\n"
        r"依次为 $0.5/0.5$、$0.9017/0.9017$、$0.4059/0.4059$、$-0.9822/-0.9822$ ✓ **完全一致**" "\n"
        r"$f(\frac\pi6)=1$ ✓" "\n"
        r"**⭐⭐ 通法（$2\sin\cos$ 型化简）**：" "\n"
        r"① ⭐⭐ **见到 $2\sin(\cdots)\cos(\cdots)$ 立刻用倍角公式**，且两角**相同**时直接得 $\sin2(\cdots)$ ✓；" "\n"
        r"② ⭐⭐ **$\sin(\frac\pi2-2x)=\cos2x$、$\cos(\frac\pi2-2x)=\sin2x$** —— 诱导公式是统一函数名的关键 ✓；" "\n"
        r"③ ⭐⭐ **$a\sin\theta+b\cos\theta$ 的合并**：$\cos$ 的系数对应 $\sin\varphi$，本题 $a=\frac{\sqrt3}2,b=\frac12$ ⟹ $\varphi=\frac\pi6$ ✓；" "\n"
        r"④ ⭐⭐ **$f(x)=1$ 型方程：先定相位区间再取唯一解**，别漏掉范围检查 ✓；" "\n"
        r"⑤ ⚠ **「等腰」不等于「等边」**，必须算出第三个角才能下结论 ✓✓"
    ),
    'difficulty': 0.72,
    'topics': ['M-T-216'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-216-E1',
}

T216_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=2\sin\dfrac{\omega x}2\cos\left(\dfrac{\omega x}2-\dfrac\pi3\right)+m\ (\omega>0)$．" "\n"
        r"在下列条件①、条件②、条件③这三个条件中，选择可以确定 $\omega$ 和 $m$ 值的两个条件作为已知．" "\n"
        r"(1) 求 $f\left(\dfrac\pi4\right)$ 的值；" "\n"
        r"(2) 若函数 $f(x)$ 在区间 $[0,a]$ 上是增函数，求实数 $a$ 的最大值．" "\n"
        r"条件①：$f(x)$ 的最小正周期为 $\pi$；" "\n"
        r"条件②：$f(x)$ 的最大值与最小值之和为 $0$；" "\n"
        r"条件③：$f(0)=2$．"
    ),
    'opts': [],
    'answer': (
        r"(1) 选①②，$f\left(\dfrac\pi4\right)=\dfrac12$；选①③，$f\left(\dfrac\pi4\right)=\dfrac{5+\sqrt3}2$；" "\n"
        r"(2) $a$ 的最大值为 $\dfrac{5\pi}{12}$"
    ),
    'analysis': (
        r"先用积化和差把 $f$ 化为 $\sin(\omega x-\frac\pi3)+\frac{\sqrt3}2+m$；"
        r"①给 $\omega$，②与③都只给 $m$ 且数值冲突，故②与③不能同选，必选①；"
        r"(2) 由 $\sin t$ 的增区间解出 $x$ 的区间，取其上界与 $0$ 比较．"
    ),
    'solution': (
        r"先化简：由 $2\sin\alpha\cos\beta=\sin(\alpha+\beta)+\sin(\alpha-\beta)$，取 $\alpha=\dfrac{\omega x}2$，$\beta=\dfrac{\omega x}2-\dfrac\pi3$，" "\n"
        r"$f(x)=\sin\left(\omega x-\dfrac\pi3\right)+\sin\dfrac\pi3+m=\sin\left(\omega x-\dfrac\pi3\right)+\dfrac{\sqrt3}2+m$．" "\n"
        r"**选条件**：①给出 $T=\dfrac{2\pi}\omega=\pi$，$\therefore\omega=2$；" "\n"
        r"②给出 $(1+\frac{\sqrt3}2+m)+(-1+\frac{\sqrt3}2+m)=0$，$\therefore m=-\dfrac{\sqrt3}2$；" "\n"
        r"③给出 $f(0)=\sin\left(-\dfrac\pi3\right)+\dfrac{\sqrt3}2+m=-\dfrac{\sqrt3}2+\dfrac{\sqrt3}2+m=2$，$\therefore m=2$．" "\n"
        r"$\because$ ②与③都只确定 $m$（且给出的值不同），同时选②与③无法确定 $\omega$，" "\n"
        r"$\therefore$ 必须选①，再在②、③中任选其一．" "\n"
        r"**(1) 选①②**：$f(x)=\sin\left(2x-\dfrac\pi3\right)$，$\therefore f\left(\dfrac\pi4\right)=\sin\left(\dfrac\pi2-\dfrac\pi3\right)=\sin\dfrac\pi6=\dfrac12$．" "\n"
        r"**选①③**：$f(x)=\sin\left(2x-\dfrac\pi3\right)+\dfrac{\sqrt3}2+2$，$\therefore f\left(\dfrac\pi4\right)=\dfrac12+\dfrac{\sqrt3}2+2=\dfrac{5+\sqrt3}2$．" "\n"
        r"**(2)** 两种选法下 $f$ 的单调性相同（加常数不影响）．令 $2x-\dfrac\pi3\in\left[-\dfrac\pi2+2k\pi,\dfrac\pi2+2k\pi\right]$，" "\n"
        r"得单调递增区间 $\left[-\dfrac\pi{12}+k\pi,\dfrac{5\pi}{12}+k\pi\right]\ (k\in\mathbb Z)$．" "\n"
        r"$\because0\in\left[-\dfrac\pi{12},\dfrac{5\pi}{12}\right]$（取 $k=0$），$\therefore$ 要使 $f$ 在 $[0,a]$ 上递增，需 $a\le\dfrac{5\pi}{12}$，" "\n"
        r"$\therefore a$ 的最大值为 $\dfrac{5\pi}{12}$．"
    ),
    'review': (
        r"**① 积化和差是化简这一步的唯一入口**：$2\sin\frac{\omega x}2\cos(\frac{\omega x}2-\frac\pi3)$" "\n"
        r"$=\sin(\omega x-\frac\pi3)+\sin\frac\pi3$，**常数项 $\frac{\sqrt3}2$ 别丢** ✓✓✓" "\n"
        r"② **三个条件的「信息量分析」是本题真正的考点**：" "\n"
        r"①给 $\omega$，②给 $m$，③给 $m$ ⟹ ②与③**不能同选**（无法确定 $\omega$），必选① ✓✓✓" "\n"
        r"③ **②与③给出的 $m$ 值不同**（$-\frac{\sqrt3}2$ 与 $2$），说明它们本就互斥，不能凑成一组 ✓✓✓" "\n"
        r"④ **$m$ 不影响单调性**，所以 (2) 两种选法答案相同 —— 这是题目的巧妙之处 ✓✓✓" "\n"
        r"⑤ **增区间必须取 $k=0$ 的那一支**：因区间以 $0$ 为左端，只有 $\left[-\frac\pi{12},\frac{5\pi}{12}\right]$ 含 $0$ ✓✓✓" "\n"
        r"⑥ 数值对拍：$f(\frac\pi4)$ 选①② $=0.5$ ✓；选①③ $=\frac{5+\sqrt3}2=3.3660$，" "\n"
        r"直接算 $\sin(2\times\frac\pi4-\frac\pi3)+\frac{\sqrt3}2+2=0.5+0.8660+2=3.3660$ ✓；" "\n"
        r"增区间上界：$\sin(2x-\frac\pi3)$ 在 $2x-\frac\pi3=\frac\pi2$ 处取最大，$x=\frac{5\pi}{12}=1.3090$ ✓" "\n"
        r"**⭐⭐ 通法（三选二条件的取舍）**：" "\n"
        r"① ⭐⭐ **先化简再判条件**：不化简就看不出「②只给 $m$」✓；" "\n"
        r"② ⭐⭐ **判断能否「确定 $\omega$ 和 $m$」**：要看两个条件是否分别卡住两个参数，" "\n"
        r"两个条件都只含 $m$ 时**必然不能同选** ✓；" "\n"
        r"③ ⭐⭐ **积化和差 $2\sin\alpha\cos\beta=\sin(\alpha+\beta)+\sin(\alpha-\beta)$**，当 $\alpha-\beta$ 为常数时最有用 ✓；" "\n"
        r"④ ⭐⭐ **常数 $m$ 不改变单调区间**，只影响值域 ✓；" "\n"
        r"⑤ ⚠ **$a$ 的最大值就是增区间的右端点**，前提是左端点 $0$ 落在该增区间内 ✓✓"
    ),
    'difficulty': 0.82,
    'topics': ['M-T-216'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-216-V1',
}

T216_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=\sin\left(2x+\dfrac\pi3\right)+\cos\left(2x+\dfrac\pi6\right)+2\sin x\cos x$．" "\n"
        r"(1) 求函数 $f(x)$ 的最小正周期，及对称轴方程；" "\n"
        r"(2) 先将函数 $y=f(x)$ 的图象向右平移 $\dfrac\pi{12}$ 个单位长度，再将所得图象上各点的横坐标伸长为原来的 $4$ 倍，" "\n"
        r"纵坐标不变，得到函数 $y=g(x)$ 的图象，求 $y=g(x)$ 在 $\left[\dfrac\pi3,2\pi\right]$ 上的值域．"
    ),
    'opts': [],
    'answer': (
        r"(1) 最小正周期为 $\pi$，对称轴方程为 $x=\dfrac\pi{12}+\dfrac{k\pi}2\ (k\in\mathbb Z)$；" "\n"
        r"(2) 值域为 $[-1,2]$"
    ),
    'analysis': (
        r"(1) 三项分别展开后合并：$2\sin x\cos x=\sin2x$，另两项展开后 $\sin2x$ 与 $\cos2x$ 的系数组合得 $2\sin(2x+\frac\pi3)$；"
        r"对称轴由相位 $=\frac\pi2+k\pi$ 解出；(2) 先平移（$x\to x-\frac\pi{12}$）再伸缩（$x\to\frac x4$），"
        r"最后在新区间上求相位范围．"
    ),
    'solution': (
        r"**(1)** $f(x)=\left(\dfrac12\sin2x+\dfrac{\sqrt3}2\cos2x\right)+\left(\dfrac{\sqrt3}2\cos2x-\dfrac12\sin2x\right)+\sin2x$" "\n"
        r"$=\sin2x+\sqrt3\cos2x=2\sin\left(2x+\dfrac\pi3\right)$．" "\n"
        r"$\therefore T=\dfrac{2\pi}2=\pi$．" "\n"
        r"令 $2x+\dfrac\pi3=k\pi+\dfrac\pi2\ (k\in\mathbb Z)$，得对称轴方程 $x=\dfrac\pi{12}+\dfrac{k\pi}2\ (k\in\mathbb Z)$．" "\n"
        r"**(2)** 将 $y=2\sin\left(2x+\dfrac\pi3\right)$ 的图象向右平移 $\dfrac\pi{12}$ 个单位，得" "\n"
        r"$y=2\sin\left(2\left(x-\dfrac\pi{12}\right)+\dfrac\pi3\right)=2\sin\left(2x+\dfrac\pi6\right)$；" "\n"
        r"再将横坐标伸长为原来的 $4$ 倍（纵坐标不变），得 $g(x)=2\sin\left(\dfrac x2+\dfrac\pi6\right)$．" "\n"
        r"$\because x\in\left[\dfrac\pi3,2\pi\right]$，$\therefore\dfrac x2\in\left[\dfrac\pi6,\pi\right]$，$\dfrac x2+\dfrac\pi6\in\left[\dfrac\pi3,\dfrac{7\pi}6\right]$．" "\n"
        r"在该区间上 $\sin t$ 的最大值为 $\sin\dfrac\pi2=1$（$\dfrac\pi2\in\left[\dfrac\pi3,\dfrac{7\pi}6\right]$），" "\n"
        r"最小值为 $\sin\dfrac{7\pi}6=-\dfrac12$，$\therefore\sin\left(\dfrac x2+\dfrac\pi6\right)\in\left[-\dfrac12,1\right]$，" "\n"
        r"$g(x)\in[-1,2]$，即值域为 $[-1,2]$．"
    ),
    'review': (
        r"**① 展开后 $\sin2x$ 的系数**：第一项 $+\frac12$，第二项 $-\frac12$，第三项 $+1$ ⟹ 合计 $+1$ ✓✓✓" "\n"
        r"② **$\cos2x$ 的系数**：$\frac{\sqrt3}2+\frac{\sqrt3}2=\sqrt3$ ⟹ $\sin2x+\sqrt3\cos2x=2\sin(2x+\frac\pi3)$ ✓✓✓" "\n"
        r"③ **对称轴由 $2x+\frac\pi3=\frac\pi2+k\pi$ 解出**：注意是 $k\pi$ 不是 $2k\pi$（对称轴每隔 $\frac T2$ 一条）✓✓✓" "\n"
        r"④ ⚠ **平移与伸缩的顺序**：先右移 $\frac\pi{12}$ 得 $2\sin(2x+\frac\pi6)$，" "\n"
        r"再横坐标伸长 $4$ 倍是 $x\to\frac x4$（不是 $4x$），得 $2\sin(\frac x2+\frac\pi6)$ ✓✓✓" "\n"
        r"⑤ **值域的端点**：相位区间 $[\frac\pi3,\frac{7\pi}6]$ 含 $\frac\pi2$（取最大 $1$），" "\n"
        r"最小值在右端 $\sin\frac{7\pi}6=-\frac12$（左端 $\sin\frac\pi3=\frac{\sqrt3}2$ 不是最小）✓✓✓" "\n"
        r"⑥ 数值对拍：$x=\frac\pi3,\frac\pi2,\pi,2\pi$ 时 $g=1.7321,1.9319,1.7321,-1.0000$；" "\n"
        r"全区间扫描得 $\min=-1.0000$，$\max=2.0000$ ✓ **与 $[-1,2]$ 完全吻合**" "\n"
        r"**⭐⭐ 通法（平移 + 伸缩）**：" "\n"
        r"① ⭐⭐ **平移是对 $x$ 本身操作**：右移 $m$ 即 $x\to x-m$，且**要乘进 $\omega$** ✓；" "\n"
        r"② ⭐⭐ **横坐标伸长为原来的 $k$ 倍 ⟹ $x\to\frac xk$**（缩短为 $\frac1k$ ⟹ $x\to kx$）✓；" "\n"
        r"③ ⭐⭐ **先平移后伸缩时，平移量也会被伸缩影响**（本题先平移，故 $\frac\pi6$ 未受影响）✓；" "\n"
        r"④ ⭐⭐ **求值域：先算相位区间，再看区间内是否取到 $\pm1$** ✓；" "\n"
        r"⑤ ⚠ **别只看两个端点**：若相位区间跨过 $\frac\pi2$ 或 $\frac{3\pi}2$，最值在内点 ✓✓"
    ),
    'difficulty': 0.75,
    'topics': ['M-T-216'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-216-V2',
}

T216_V3 = {
    'type': '解答',
    'stem_text': (
        r"已知 $\theta\in\mathbb R$，设函数 $f(x)=\cos^{2}x-\sin(x+\theta)\cos(x+\theta)$．" "\n"
        r"(1) 若 $f(x)$ 是偶函数，求 $\theta$ 的取值集合；" "\n"
        r"(2) 若方程 $f(x)+f(-x)=f(0)$ 有实数解，求 $\sin\theta+\cos\theta$ 的取值范围．"
    ),
    'opts': [],
    'answer': (
        r"(1) $\left\{\theta\ \middle|\ \theta=\dfrac{k\pi}2-\dfrac\pi4,\ k\in\mathbb Z\right\}$；" "\n"
        r"(2) $\left[-\dfrac{\sqrt{15}}3,\dfrac{\sqrt{15}}3\right]$"
    ),
    'analysis': (
        r"先用 $\sin u\cos u=\frac12\sin2u$ 与降幂把 $f$ 化为 $\frac{1+\cos2x}2-\frac12\sin(2x+2\theta)$；"
        r"(1) 由 $f(x)=f(-x)$ 得 $\sin2x\cos2\theta=0$ 恒成立，故 $\cos2\theta=0$；"
        r"(2) 计算 $f(x)+f(-x)$ 时用和差化积，方程化为 $\cos2x=\frac{\sin2\theta}{2(\sin2\theta-1)}$，"
        r"由 $\lvert\cos2x\rvert\le1$ 定出 $\sin2\theta$ 的范围，再用 $(\sin\theta+\cos\theta)^2=1+\sin2\theta$．"
    ),
    'solution': (
        r"$f(x)=\cos^{2}x-\dfrac12\sin(2x+2\theta)=\dfrac{1+\cos2x}2-\dfrac12\sin(2x+2\theta)$．" "\n"
        r"**(1)** $f(x)$ 为偶函数，即 $\forall x\in\mathbb R$，$f(x)=f(-x)$：" "\n"
        r"$\dfrac{1+\cos2x}2-\dfrac12\sin(2x+2\theta)=\dfrac{1+\cos2x}2-\dfrac12\sin(2\theta-2x)$，" "\n"
        r"即 $\sin(2x+2\theta)=\sin(2\theta-2x)$．" "\n"
        r"展开：$\sin2x\cos2\theta+\cos2x\sin2\theta=\sin2\theta\cos2x-\cos2\theta\sin2x$，" "\n"
        r"$\therefore2\sin2x\cos2\theta=0$．$\because\sin2x$ 不恒为 $0$，$\therefore\cos2\theta=0$，" "\n"
        r"$2\theta=k\pi+\dfrac\pi2$，即 $\theta=\dfrac{k\pi}2+\dfrac\pi4\ (k\in\mathbb Z)$（等价于 $\theta=\dfrac{k\pi}2-\dfrac\pi4$）．" "\n"
        r"$\therefore\theta$ 的取值集合为 $\left\{\theta\ \middle|\ \theta=\dfrac{k\pi}2-\dfrac\pi4,\ k\in\mathbb Z\right\}$．" "\n"
        r"**(2)** $f(0)=1-\dfrac12\sin2\theta$，" "\n"
        r"$f(x)+f(-x)=\left(1+\cos2x\right)-\dfrac12\left[\sin(2x+2\theta)+\sin(2\theta-2x)\right]=1+\cos2x-\sin2\theta\cos2x$．" "\n"
        r"方程 $f(x)+f(-x)=f(0)$ 即 $1+\cos2x\left(1-\sin2\theta\right)=1-\dfrac12\sin2\theta$，" "\n"
        r"$\therefore\cos2x\left(1-\sin2\theta\right)=-\dfrac12\sin2\theta$，即 $2\left(\sin2\theta-1\right)\cos2x=\sin2\theta$．" "\n"
        r"$\because\sin2\theta\in[-1,1]$，$\therefore\sin2\theta-1\ne0$（否则 $-\frac12\ne0$），" "\n"
        r"$\therefore\cos2x=\dfrac{\sin2\theta}{2\left(\sin2\theta-1\right)}$．" "\n"
        r"原方程有实数解 $\iff-1\le\dfrac{\sin2\theta}{2(\sin2\theta-1)}\le1$．设 $s=\sin2\theta\in[-1,1)$，分母 $2(s-1)<0$：" "\n"
        r"由 $\dfrac s{2(s-1)}\le1$ 得 $s\ge2s-2$，即 $s\le2$（恒成立）；" "\n"
        r"由 $\dfrac s{2(s-1)}\ge-1$ 得 $s\le-2s+2$，即 $s\le\dfrac23$．" "\n"
        r"$\therefore-1\le\sin2\theta\le\dfrac23$．" "\n"
        r"$\because(\sin\theta+\cos\theta)^{2}=1+\sin2\theta\in\left[0,\dfrac53\right]$，" "\n"
        r"$\therefore\sin\theta+\cos\theta\in\left[-\dfrac{\sqrt{15}}3,\dfrac{\sqrt{15}}3\right]$．"
    ),
    'review': (
        r"**① 题干的 $\cos2x$ 实为 $\cos^{2}x$（上标丢失）** ✓✓✓" "\n"
        r"判据极硬：按 $\cos2x$ 版，$f(x)+f(-x)=2\cos2x-\cos2x\sin2\theta=\cos2x(2-\sin2\theta)$，" "\n"
        r"方程化为 $\cos2x=\frac{2-\sin2\theta}{2(2-\sin2\theta)}=\frac12$，**与 $\theta$ 无关**，题目失去意义；" "\n"
        r"取 $\theta=0$、$x=\frac\pi6$ 代入原方程验证：$f(\frac\pi6)+f(-\frac\pi6)=0.067+0.933=1=f(0)$ 确实成立 ✓" "\n"
        r"而按 $\cos^2x$ 版化简恰得详解的中间式 $2(\sin2\theta-1)\cos2x=\sin2\theta$ ✓ **据此判定还原正确**" "\n"
        r"② **和差化积**：$\sin(2x+2\theta)+\sin(2\theta-2x)=2\sin2\theta\cos2x$，" "\n"
        r"这一步把 $x$ 与 $\theta$ 分离，是本题的关键 ✓✓✓" "\n"
        r"③ ⚠ **分母为负时解不等式要变号**：$2(s-1)<0$，故 $\frac s{2(s-1)}\le1$ 变号成 $s\ge2s-2$ ✓✓✓" "\n"
        r"④ **$\sin2\theta=1$ 必须排除**（此时分母为 $0$，方程变成 $0=-\frac12$ 无解）✓✓✓" "\n"
        r"⑤ **最后一步用 $(\sin\theta+\cos\theta)^2=1+\sin2\theta$**：注意开方后**有正负两支**，区间是对称的 ✓✓✓" "\n"
        r"⑥ 数值对拍：$s=-1$ 时 $u=\frac{-1}{2(-2)}=\frac14\in[-1,1]$ ✓；$s=0$ 时 $u=0$ ✓；" "\n"
        r"$s=0.9$ 时 $u=\frac{0.9}{2(-0.1)}=-4.5\notin[-1,1]$ ✗（对应 $\sin2\theta>\frac23$，应排除）✓；" "\n"
        r"边界 $\sin2\theta=\frac23$ ⟹ $(\sin\theta+\cos\theta)^2=\frac53$ ⟹ $\frac{\sqrt{15}}3=1.2910=\sqrt{\frac53}$ ✓" "\n"
        r"**⭐⭐ 通法（含参三角方程有解）**：" "\n"
        r"① ⭐⭐ **「方程有解」⟺ 分离出的 $\cos$（或 $\sin$）落在 $[-1,1]$** ✓；" "\n"
        r"② ⭐⭐ **和差化积分离变量**：$\sin(A)+\sin(B)$ 型两项，用 $2\sin\frac{A+B}2\cos\frac{A-B}2$ ✓；" "\n"
        r"③ ⭐⭐ **$f(x)+f(-x)$ 是偶函数部分**，必然只含 $\cos$ 项，这是可分离的原因 ✓；" "\n"
        r"④ ⭐⭐ **$(\sin\theta\pm\cos\theta)^2=1\pm\sin2\theta$** 用于把 $\sin2\theta$ 的范围转成所求范围 ✓；" "\n"
        r"⑤ ⚠ **解分式不等式先判分母符号**，$s\in[-1,1)$ 时 $s-1<0$ 恒成立，两次都要变号 ✓✓"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-216'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-216-V3',
}

T217_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知 $f(x)=\vec m\cdot\vec n-1$，$\vec m=\left(\dfrac12,\sqrt3\sin\dfrac x2\right)$，$\vec n=\left(1+2\cos^{2}\dfrac x2,\cos\dfrac x2\right)$．" "\n"
        r"(1) 求函数 $f(x)$ 的对称中心和单调增区间；" "\n"
        r"(2) 将函数 $y=f(x)$ 的图象上的各点____得到函数 $y=g(x)$ 的图象，" "\n"
        r"当 $x\in\left[-\dfrac\pi6,\dfrac\pi4\right]$ 时，方程 $g(x)=a$ 有解，求实数 $a$ 的取值范围．" "\n"
        r"在以下①、②中选择一个，补在 (2) 的横线上，并加以解答（如果①、②都做，则按①给分）：" "\n"
        r"① 向左平移 $\dfrac{3\pi}2$ 个单位，再保持纵坐标不变，横坐标缩小为原来的一半；" "\n"
        r"② 纵坐标保持不变，横坐标缩小为原来的一半，再向右平移 $\dfrac\pi4$ 个单位．"
    ),
    'opts': [],
    'answer': (
        r"(1) 对称中心为 $\left(k\pi-\dfrac\pi6,0\right)\ (k\in\mathbb Z)$，单调增区间为 $\left[2k\pi-\dfrac{2\pi}3,2k\pi+\dfrac\pi3\right]\ (k\in\mathbb Z)$；" "\n"
        r"(2) 选①、选②答案相同，均为 $a\in\left[-1,\dfrac12\right]$"
    ),
    'analysis': (
        r"先由数量积与降幂公式把 $f$ 化为 $\sin(x+\frac\pi6)$；(1) 对称中心由相位 $=k\pi$ 得，增区间由相位 $\in[-\frac\pi2+2k\pi,\frac\pi2+2k\pi]$ 得；"
        r"(2) 两种变换顺序不同，结果分别是 $-\cos(2x+\frac\pi6)$ 与 $\sin(2x-\frac\pi3)$，但值域相同．"
    ),
    'solution': (
        r"先化简：$f(x)=\dfrac12\left(1+2\cos^{2}\dfrac x2\right)+\sqrt3\sin\dfrac x2\cos\dfrac x2-1$" "\n"
        r"$=\dfrac12+\cos^{2}\dfrac x2+\dfrac{\sqrt3}2\sin x-1=\dfrac12+\dfrac{1+\cos x}2+\dfrac{\sqrt3}2\sin x-1$" "\n"
        r"$=\dfrac12\cos x+\dfrac{\sqrt3}2\sin x=\sin\left(x+\dfrac\pi6\right)$．" "\n"
        r"**(1)** 令 $x+\dfrac\pi6=k\pi\ (k\in\mathbb Z)$，得对称中心 $\left(k\pi-\dfrac\pi6,0\right)\ (k\in\mathbb Z)$．" "\n"
        r"令 $x+\dfrac\pi6\in\left[-\dfrac\pi2+2k\pi,\dfrac\pi2+2k\pi\right]$，得单调增区间 $\left[2k\pi-\dfrac{2\pi}3,2k\pi+\dfrac\pi3\right]\ (k\in\mathbb Z)$．" "\n"
        r"**(2) 选①**：左移 $\dfrac{3\pi}2$ 得 $y=\sin\left(x+\dfrac{3\pi}2+\dfrac\pi6\right)=\sin\left(x+\dfrac{5\pi}3\right)$，" "\n"
        r"再横坐标缩小为原来的一半得 $g(x)=\sin\left(2x+\dfrac{5\pi}3\right)=\sin\left(2x+\dfrac\pi6+\dfrac{3\pi}2\right)=-\cos\left(2x+\dfrac\pi6\right)$．" "\n"
        r"$\because x\in\left[-\dfrac\pi6,\dfrac\pi4\right]$，$\therefore2x+\dfrac\pi6\in\left[-\dfrac\pi6,\dfrac{2\pi}3\right]$．" "\n"
        r"该区间内 $\cos t$ 的最大值为 $\cos0=1$，最小值为 $\cos\dfrac{2\pi}3=-\dfrac12$，故 $\cos\left(2x+\dfrac\pi6\right)\in\left[-\dfrac12,1\right]$，" "\n"
        r"$g(x)\in\left[-1,\dfrac12\right]$．" "\n"
        r"**选②**：横坐标缩小为原来的一半得 $y=\sin\left(2x+\dfrac\pi6\right)$，再右移 $\dfrac\pi4$ 得" "\n"
        r"$g(x)=\sin\left(2\left(x-\dfrac\pi4\right)+\dfrac\pi6\right)=\sin\left(2x-\dfrac\pi3\right)$．" "\n"
        r"$\because x\in\left[-\dfrac\pi6,\dfrac\pi4\right]$，$\therefore2x-\dfrac\pi3\in\left[-\dfrac{2\pi}3,\dfrac\pi6\right]$，" "\n"
        r"该区间内 $\sin t$ 的最小值为 $\sin\left(-\dfrac\pi2\right)=-1$（$-\dfrac\pi2$ 在区间内），最大值为 $\sin\dfrac\pi6=\dfrac12$，" "\n"
        r"$\therefore g(x)\in\left[-1,\dfrac12\right]$．" "\n"
        r"$\therefore$ 两种选法均有 $a\in\left[-1,\dfrac12\right]$．"
    ),
    'review': (
        r"**① 数量积展开后关键是 $\cos^2\frac x2$ 降幂**：$\cos^2\frac x2=\frac{1+\cos x}2$，" "\n"
        r"常数项 $\frac12+\frac12-1=0$ **恰好抵消** —— 这种「刻意归零」是可做对的信号 ✓✓✓" "\n"
        r"② **$\sqrt3\sin\frac x2\cos\frac x2=\frac{\sqrt3}2\sin x$**（倍角）✓✓✓" "\n"
        r"③ **合并方向**：$\frac{\sqrt3}2\sin x+\frac12\cos x=\sin(x+\frac\pi6)$ ✓✓✓" "\n"
        r"④ ⚠ **选①的平移量很大（$\frac{3\pi}2$）**：$\sin(x+\frac{5\pi}3)=\sin(x+\frac\pi6+\frac{3\pi}2)=-\cos(x+\frac\pi6)$，" "\n"
        r"用的是 $\sin(t+\frac{3\pi}2)=-\cos t$ ✓✓✓" "\n"
        r"⑤ **两种选法结果相同不是巧合**：$g_1=-\cos(2x+\frac\pi6)=\sin(2x+\frac\pi6-\frac\pi2)=\sin(2x-\frac\pi3)=g_2$ ✓✓✓" "\n"
        r"⑥ 数值对拍：区间扫描得选① $\min=-1.0000,\max=0.5000$；选② $\min=-1.0000,\max=0.5000$ ✓" "\n"
        r"$f(x)$ 与 $\sin(x+\frac\pi6)$ 在 $x=0.2,1.0,2.2$ 处依次为 $0.6621/0.6621$、$0.9989/0.9989$、$0.4059/0.4059$ ✓" "\n"
        r"**⭐⭐ 通法（向量数量积型三角函数）**：" "\n"
        r"① ⭐⭐ **数量积展开后必用降幂**：$\cos^2\frac x2=\frac{1+\cos x}2$、$\sin^2\frac x2=\frac{1-\cos x}2$ ✓；" "\n"
        r"② ⭐⭐ **常数项抵消 ⟹ $f$ 无直流分量**，可直接写成单个 $\sin$ 或 $\cos$ ✓；" "\n"
        r"③ ⭐⭐ **对称中心由相位 $=k\pi$ 求，增区间由相位 $\in[-\frac\pi2+2k\pi,\frac\pi2+2k\pi]$ 求** ✓；" "\n"
        r"④ ⭐⭐ **$\sin(t+\frac{3\pi}2)=-\cos t$、$\sin(t+\frac\pi2)=\cos t$** —— 大平移先化小再处理 ✓；" "\n"
        r"⑤ ⚠ **判断两支路是否等价**：把结果都化成同名函数比较，可防计算错误 ✓✓"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-217'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-217-E1',
}

T217_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=\sqrt3\sin(2x+\varphi)+\cos(2x+\varphi)\ \left(\lvert\varphi\rvert<\dfrac\pi2\right)$，将 $f(x)$ 的图象向左平移 $\dfrac\pi3$ 个单位长度，" "\n"
        r"所得函数的图象关于 $y$ 轴对称．" "\n"
        r"(1) 求函数 $f(x)$ 的解析式；" "\n"
        r"(2) 若关于 $x$ 的方程 $f(x)=a$ 在 $\left[\dfrac\pi6,\dfrac5{12}\pi\right]$ 上恰有两个实数根，求实数 $a$ 的取值范围．"
    ),
    'opts': [],
    'answer': r"(1) $f(x)=2\sin\left(2x-\dfrac\pi6\right)$；(2) $a\in\left[\sqrt3,2\right)$",
    'analysis': (
        r"(1) 先合并为 $2\sin(2x+\varphi+\frac\pi6)$，平移后为 $2\sin(2x+\varphi+\frac{5\pi}6)$，"
        r"关于 $y$ 轴对称即该函数为偶函数，故相位常数 $=\frac\pi2+k\pi$；(2) 由区间端点值与单调性确定「恰有两根」的水平线范围．"
    ),
    'solution': (
        r"**(1)** $f(x)=\sqrt3\sin(2x+\varphi)+\cos(2x+\varphi)=2\sin\left(2x+\varphi+\dfrac\pi6\right)$．" "\n"
        r"左移 $\dfrac\pi3$ 后：$y=2\sin\left(2\left(x+\dfrac\pi3\right)+\varphi+\dfrac\pi6\right)=2\sin\left(2x+\varphi+\dfrac{5\pi}6\right)$．" "\n"
        r"该函数图象关于 $y$ 轴对称，即它是偶函数，$\therefore\varphi+\dfrac{5\pi}6=\dfrac\pi2+k\pi\ (k\in\mathbb Z)$，$\varphi=-\dfrac\pi3+k\pi$．" "\n"
        r"又 $\lvert\varphi\rvert<\dfrac\pi2$，$\therefore\varphi=-\dfrac\pi3$，即 $f(x)=2\sin\left(2x-\dfrac\pi6\right)$．" "\n"
        r"**(2)** $\because x\in\left[\dfrac\pi6,\dfrac{5\pi}{12}\right]$，$\therefore2x-\dfrac\pi6\in\left[\dfrac\pi6,\dfrac{2\pi}3\right]$．" "\n"
        r"当 $2x-\dfrac\pi6\in\left[\dfrac\pi6,\dfrac\pi2\right]$，即 $x\in\left[\dfrac\pi6,\dfrac\pi3\right]$ 时，$f(x)$ 单调递增，值域 $[1,2]$；" "\n"
        r"当 $2x-\dfrac\pi6\in\left(\dfrac\pi2,\dfrac{2\pi}3\right]$，即 $x\in\left(\dfrac\pi3,\dfrac{5\pi}{12}\right]$ 时，$f(x)$ 单调递减，值域 $[\sqrt3,2)$．" "\n"
        r"又 $f\left(\dfrac\pi6\right)=2\sin\dfrac\pi6=1$，$f\left(\dfrac\pi3\right)=2\sin\dfrac\pi2=2$，$f\left(\dfrac{5\pi}{12}\right)=2\sin\dfrac{2\pi}3=\sqrt3$．" "\n"
        r"方程 $f(x)=a$ 在该区间上恰有两个实数根，需 $a$ 同时落在递增段与递减段的值域内，" "\n"
        r"且不能只落在峰值：$a\in[\sqrt3,2)$（$a=2$ 时只有 $x=\dfrac\pi3$ 一个根）．" "\n"
        r"$\therefore$ 实数 $a$ 的取值范围为 $\left[\sqrt3,2\right)$．"
    ),
    'review': (
        r"**① 合并时 $\varphi$ 跟着走**：$\sqrt3\sin(2x+\varphi)+\cos(2x+\varphi)=2\sin(2x+\varphi+\frac\pi6)$ ✓✓✓" "\n"
        r"② **左移 $\frac\pi3$ 后相位增加 $2\times\frac\pi3=\frac{2\pi}3$**（不是 $\frac\pi3$）—— 这是最高频错误 ✓✓✓" "\n"
        r"③ **偶函数条件**：$2\sin(2x+C)$ 为偶函数 $\iff C=\frac\pi2+k\pi$ ✓✓✓" "\n"
        r"④ ⚠ **$\lvert\varphi\rvert<\frac\pi2$ 用来定 $k$**：$\varphi=-\frac\pi3+k\pi$，$k=0$ 给 $-\frac\pi3$ ✓，$k=1$ 给 $\frac{2\pi}3$（超范围）✗ ✓✓✓" "\n"
        r"⑤ **「恰有两个根」的开闭**：$a=\sqrt3$ 时两根（递增段一根 + 右端点 $x=\frac{5\pi}{12}$ 一根）⟹ **闭**；" "\n"
        r"$a=2$ 时只有峰值点一根 ⟹ **开** ✓✓✓" "\n"
        r"⑥ 数值对拍：区间扫描得值域 $[1.0000,2.0000]$，端点值 $f(\frac\pi6)=1$、$f(\frac{5\pi}{12})=1.7321=\sqrt3$ ✓；" "\n"
        r"偶函数检验：$f(0.7+\frac\pi3)=f(-0.7+\frac\pi3)=0.3399$ ✓" "\n"
        r"**⭐⭐ 通法（平移 + 奇偶性定 $\varphi$）**：" "\n"
        r"① ⭐⭐ **平移量要乘 $\omega$**：左移 $m$ ⟹ 相位 $+\omega m$ ✓；" "\n"
        r"② ⭐⭐ **关于 $y$ 轴对称 ⟺ 偶函数 ⟺ 相位常数 $=\frac\pi2+k\pi$**（关于原点对称则 $=k\pi$）✓；" "\n"
        r"③ ⭐⭐ **$\lvert\varphi\rvert$ 的范围专门用于定 $k$** ✓；" "\n"
        r"④ ⭐⭐ **「恰有 $n$ 根」看分段单调性**：把区间按极值点分段，各段值域取交集，再处理峰值的开闭 ✓；" "\n"
        r"⑤ ⚠ **峰值处水平线只交一次**，故上端点必须开 ✓✓"
    ),
    'difficulty': 0.82,
    'topics': ['M-T-217'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-217-V1',
}

T217_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=2\sin(\omega x)$，其中常数 $\omega>0$．" "\n"
        r"(1) 若 $\omega=2$，将函数 $y=f(x)$ 的图象向左平移 $\dfrac\pi6$ 个单位，得到函数 $y=g(x)$ 的图象，求 $g(x)$；" "\n"
        r"(2) 若 $y=f(x)$ 在 $\left[-\dfrac\pi4,\dfrac{2\pi}3\right]$ 上单调递增，求 $\omega$ 的取值范围；" "\n"
        r"(3) 对 (1) 中的 $g(x)$，区间 $[a,b]$（$a,b\in\mathbb R$ 且 $a<b$）满足：$y=g(x)$ 在 $[a,b]$ 上至少含有 $30$ 个零点，" "\n"
        r"在所有满足上述条件的 $[a,b]$ 中，求 $b-a$ 的最小值．"
    ),
    'opts': [],
    'answer': (
        r"(1) $g(x)=2\sin\left(2x+\dfrac\pi3\right)$；(2) $\omega\in\left(0,\dfrac34\right]$；(3) $\left(b-a\right)_{\min}=\dfrac{29\pi}2$"
    ),
    'analysis': (
        r"(1) 左移 $\frac\pi6$ 即 $x\to x+\frac\pi6$；(2) 含 $x=0$ 的区间要落在 $\sin t$ 的单一递增区间 $[-\frac\pi2,\frac\pi2]$ 内，"
        r"两端同时约束取交集；(3) 先求零点间距（$=\frac T2$），$N$ 个零点最少跨 $N-1$ 个间距．"
    ),
    'solution': (
        r"**(1)** $\omega=2$ 时 $f(x)=2\sin2x$，左移 $\dfrac\pi6$ 得" "\n"
        r"$g(x)=2\sin\left(2\left(x+\dfrac\pi6\right)\right)=2\sin\left(2x+\dfrac\pi3\right)$．" "\n"
        r"**(2)** 当 $x\in\left[-\dfrac\pi4,\dfrac{2\pi}3\right]$ 时，$\omega x\in\left[-\dfrac{\omega\pi}4,\dfrac{2\omega\pi}3\right]$．" "\n"
        r"$\because\omega>0$ 且 $0$ 属于该区间，$\therefore$ 要使 $y=2\sin(\omega x)$ 递增，需该区间含于 $\left[-\dfrac\pi2,\dfrac\pi2\right]$：" "\n"
        r"$\begin{cases}-\dfrac{\omega\pi}4\ge-\dfrac\pi2\\[2mm]\dfrac{2\omega\pi}3\le\dfrac\pi2\end{cases}$，解得 $\begin{cases}\omega\le2\\[1mm]\omega\le\dfrac34\end{cases}$，$\therefore0<\omega\le\dfrac34$．" "\n"
        r"**(3)** 令 $g(x)=0$ 得 $2x+\dfrac\pi3=k\pi$，即 $x=\dfrac{k\pi}2-\dfrac\pi6\ (k\in\mathbb Z)$，相邻零点间距为 $\dfrac\pi2$．" "\n"
        r"要使 $[a,b]$ 上至少含有 $30$ 个零点，最省长度的做法是让首尾两个零点分别落在 $a$、$b$ 处，" "\n"
        r"共跨 $30-1=29$ 个间距，$\therefore\left(b-a\right)_{\min}=29\times\dfrac\pi2=\dfrac{29\pi}2$．"
    ),
    'review': (
        r"**① 左移 $\frac\pi6$ 后相位 $+2\times\frac\pi6=\frac\pi3$** ✓✓✓" "\n"
        r"② ⚠ **(2) 的关键是 $0$ 落在区间内**：因此递增区间只能取含 $0$ 的那一支 $\left[-\frac\pi2,\frac\pi2\right]$，" "\n"
        r"不能取 $\left[\frac{3\pi}2,\frac{5\pi}2\right]$ 等 ✓✓✓" "\n"
        r"③ **两端都要约束**：左端给 $\omega\le2$，右端给 $\omega\le\frac34$，**取更紧的** $\frac34$ ✓✓✓" "\n"
        r"④ ⚠ **$n$ 个零点跨 $n-1$ 个间距**（不是 $n$ 个）—— 这是最容易错的一步 ✓✓✓" "\n"
        r"⑤ **零点间距 $=\frac T2=\frac\pi\omega$ 的一半**：$T=\frac{2\pi}2=\pi$，间距 $\frac\pi2$ ✓✓✓" "\n"
        r"⑥ 数值对拍：$\omega=\frac34$ 时相位区间 $=[-\frac{3\pi}{16},\frac\pi2]=[-0.5890,1.5708]$，" "\n"
        r"含于 $[-\frac\pi2,\frac\pi2]$ ✓；$29\times\frac\pi2=45.5531$ ✓" "\n"
        r"**⭐⭐ 通法（零点计数与单调区间）**：" "\n"
        r"① ⭐⭐ **相邻零点间距 $=\frac T2=\frac\pi\omega$**（相邻最值点间距也是 $\frac T2$）✓；" "\n"
        r"② ⭐⭐ **$n$ 个点最少跨 $n-1$ 个间距** ✓；" "\n"
        r"③ ⭐⭐ **区间含 $0$ 时，单调区间只能取含 $0$ 的那一支** ✓；" "\n"
        r"④ ⭐⭐ **两端同时列不等式后取交集**（取最紧的那个）✓；" "\n"
        r"⑤ ⚠ **$\omega>0$ 不能忘**，它决定了相位区间的左右次序 ✓✓"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-217'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-217-V2',
}

T217_V3 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=\sqrt3\sin(\omega x+\varphi)+2\sin^{2}\dfrac{\omega x+\varphi}2-1\ (\omega>0,\ 0<\varphi<\pi)$ 为偶函数，" "\n"
        r"且 $f(x)$ 图象的相邻两对称轴间的距离为 $\dfrac\pi2$．" "\n"
        r"(1) 求 $f(x)$ 的解析式；" "\n"
        r"(2) 将函数 $f(x)$ 的图象向右平移 $\dfrac\pi6$ 个单位长度，再把横坐标缩小为原来的 $\dfrac12$（纵坐标不变），得到函数 $g(x)$ 的图象，" "\n"
        r"若 $g(x)-m=0$ 在 $\left[-\dfrac\pi{12},\dfrac\pi6\right]$ 上有两个不同的根，求 $m$ 的取值范围．"
    ),
    'opts': [],
    'answer': r"(1) $f(x)=2\cos2x$；(2) $m\in[1,2)$",
    'analysis': (
        r"先用 $2\sin^2\frac\alpha2-1=-\cos\alpha$ 把 $f$ 化为 $2\sin(\omega x+\varphi-\frac\pi6)$；"
        r"由偶函数定 $\varphi$，由相邻对称轴距离 $=\frac T2$ 定 $\omega$；"
        r"(2) 变换得 $g(x)=2\cos(4x-\frac\pi3)$，把「两个不同的根」翻译成水平线 $y=\frac m2$ 与曲线的交点个数．"
    ),
    'solution': (
        r"**(1)** $\because2\sin^{2}\dfrac{\omega x+\varphi}2-1=-\cos(\omega x+\varphi)$，$\therefore f(x)=\sqrt3\sin(\omega x+\varphi)-\cos(\omega x+\varphi)=2\sin\left(\omega x+\varphi-\dfrac\pi6\right)$．" "\n"
        r"$\because f(x)$ 为偶函数，$\therefore\varphi-\dfrac\pi6=\dfrac\pi2+k\pi\ (k\in\mathbb Z)$，即 $\varphi=\dfrac{2\pi}3+k\pi$．" "\n"
        r"又 $0<\varphi<\pi$，$\therefore\varphi=\dfrac{2\pi}3$，$\therefore f(x)=2\sin\left(\omega x+\dfrac{2\pi}3-\dfrac\pi6\right)=2\sin\left(\omega x+\dfrac\pi2\right)=2\cos(\omega x)$．" "\n"
        r"$\because$ 相邻两对称轴间的距离为 $\dfrac12\times\dfrac{2\pi}\omega=\dfrac\pi\omega=\dfrac\pi2$，$\therefore\omega=2$，即 $f(x)=2\cos2x$．" "\n"
        r"**(2)** 右移 $\dfrac\pi6$ 得 $y=2\cos\left(2\left(x-\dfrac\pi6\right)\right)=2\cos\left(2x-\dfrac\pi3\right)$，" "\n"
        r"再把横坐标缩小为原来的 $\dfrac12$ 得 $g(x)=2\cos\left(4x-\dfrac\pi3\right)$．" "\n"
        r"$\because x\in\left[-\dfrac\pi{12},\dfrac\pi6\right]$，$\therefore4x-\dfrac\pi3\in\left[-\dfrac{2\pi}3,\dfrac\pi3\right]$．" "\n"
        r"在该区间上 $\cos t$ 的最大值为 $\cos0=1$，且 $\cos\left(-\dfrac{2\pi}3\right)=\cos\dfrac\pi3=\dfrac12$（两端相等），" "\n"
        r"$\therefore\cos\left(4x-\dfrac\pi3\right)\in\left[\dfrac12,1\right]$，即 $g(x)\in[1,2]$．" "\n"
        r"方程 $g(x)=m$ 有两个不同的根 $\iff$ 水平线 $y=\dfrac m2$ 与 $y=\cos t$ 在 $\left[-\dfrac{2\pi}3,\dfrac\pi3\right]$ 上有两个交点．" "\n"
        r"由对称性知需 $\dfrac12\le\dfrac m2<1$（$\dfrac m2=1$ 时只有 $t=0$ 一个交点），$\therefore m\in[1,2)$．"
    ),
    'review': (
        r"**① 题干残缺已补回**：V3 的题面被截断后混入 V2 详解的末尾，" "\n"
        r"已从 V2 solution 尾部取回完整题干（含 $\omega>0,\ 0<\varphi<\pi$ 与对称轴距离条件）✓✓✓" "\n"
        r"② **$2\sin^2\frac\alpha2-1=-\cos\alpha$** 是降幂的逆用，把 $f$ 从「$\sin$ + $\sin^2$」统一成单个 $\sin$ ✓✓✓" "\n"
        r"③ **偶函数条件**：$2\sin(\omega x+C)$ 为偶函数 $\iff C=\frac\pi2+k\pi$ ⟹ $\varphi=\frac{2\pi}3+k\pi$ ✓✓✓" "\n"
        r"④ ⚠ **相邻对称轴距离 $=\frac T2=\frac\pi\omega$**（不是 $T$）⟹ $\frac\pi\omega=\frac\pi2$ ⟹ $\omega=2$ ✓✓✓" "\n"
        r"⑤ **「两个不同的根」的开闭**：$\frac m2=\frac12$ 时两根（$t=-\frac{2\pi}3$ 与 $t=\frac\pi3$，均为区间端点）⟹ **闭**；" "\n"
        r"$\frac m2=1$ 时只有 $t=0$ 一根（峰值）⟹ **开** ✓✓✓" "\n"
        r"⑥ 数值对拍：区间扫描得 $g$ 值域 $[-1.0000,2.0000]$，**但在 $[-\frac{2\pi}3,\frac\pi3]$ 上 $\cos$ 的值域是 $[\frac12,1]$**，" "\n"
        r"故 $g\in[1,2]$ ✓；交点计数：$m=0.9$ ⟹ $1$ 个；$m=1.0$ ⟹ $2$ 个（$x=0$ 与 $x=\frac\pi6$）；$m=1.5$ ⟹ $2$ 个；$m=2.0$ ⟹ $0$ 个 ✓" "\n"
        r"**⭐⭐ 通法（$2\sin^2\frac\alpha2-1$ 与交点计数）**：" "\n"
        r"① ⭐⭐ **见到 $2\sin^2\frac\alpha2$ 或 $2\cos^2\frac\alpha2$ 立刻降幂**：$=-\cos\alpha$ / $=\cos\alpha$ ✓；" "\n"
        r"② ⭐⭐ **相邻对称轴（或相邻对称中心）距离 $=\frac T2$** ✓；" "\n"
        r"③ ⭐⭐ **「两个不同的根」⟺ 水平线与曲线有两个交点**，最好数交点而非代数求解 ✓；" "\n"
        r"④ ⭐⭐ **峰值处只交一次** ⟹ 上端点必开；两端点值相等时水平线恰交两次 ⟹ 下端点闭 ✓；" "\n"
        r"⑤ ⚠ **先求相位区间再看 $\cos$ 的值域**，别直接用 $[-1,1]$ ✓✓"
    ),
    'difficulty': 0.86,
    'topics': ['M-T-217'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-217-V3',
}

QS = [T224_E1, T224_V1, T224_V2, T224_V3,
      T216_E1, T216_V1, T216_V2, T216_V3,
      T217_E1, T217_V1, T217_V2, T217_V3]
