# -*- coding: utf-8 -*-
r"""第62批：焦点三角形与共焦点（8 题） 来源：2024高中数学热点题型归纳完整解析版.pdf p305 M-T-330-E1/V1/V3；p306 M-T-332-E1；p307 M-T-332-V1/V2、M-T-333-E1、M-T-333-V1 ## ★★ 本批四处「根号丢失」的还原（全部靠"算出来对不上"发现） | 题 | ref_bank 存的 | 实际 | |---|---|---| | M-T-330-V1 | `0, 6 - 2 /2` | $\left(0,\dfrac{\sqrt6-\sqrt2}2\right)$ | | M-T-330-V3 | 点 $M(3,0)$ | **$M(\sqrt3,0)$** | | M-T-332-E1 | `17/17` | $\dfrac{\sqrt{17}}{17}$ | | M-T-332-V1 | `2/4` | $\dfrac{\sqrt2}4$ | **M-T-330-V3 的还原过程（本批最精彩）**： 按字面 $M(3,0)$，则 $x_Ax_B=m^{2}=9$，由 $\lvert BF\rvert=2$ 得 $x_B=\frac32$、$x_A=6$， 面积比 $=\frac{\lvert BF\rvert}{\lvert AF\rvert}=\frac2{6.5}=\frac4{13}$ —— **不是答案 $\frac45$**。 反推：要得 $\frac45$ 需 $\lvert AF\rvert=\frac52$ 即 $x_A=2$，于是 $x_Ax_B=2\cdot\frac32=3=m^{2}$ ⟹ $m=\sqrt3$。 代回检验：$A(2,-2)$、$B(\frac32,\sqrt3)$、$M(\sqrt3,0)$ 三点共线 ✓ —— 确认 $M(\sqrt3,0)$。 ## ★★ 三个反复出现的工具 **1. 焦点三角形面积**：椭圆 $S=b^{2}\tan\frac\alpha2$；双曲线 $S=\dfrac{b^{2}}{\tan\frac\alpha2}$（$\alpha=\angle F_1PF_2$） **2. 内切圆半径万能式**：$r=\dfrac{2S}{\text{周长}}$；焦点三角形周长 $=2a+2c$（椭圆）或自行计算 **3. 共焦点核心公式**：$\dfrac{\sin^{2}\theta}{e_1^{2}}+\dfrac{\cos^{2}\theta}{e_2^{2}}=1$（$2\theta=\angle F_1PF_2$，椭圆 $e_1$、双曲线 $e_2$） ## 八题验算 | 题 | 关键 | 答案 | |---|---|---| | M-T-330-E1 | $\lvert AB\rvert=\lvert AF_2\rvert+\lvert BF_2\rvert=\lvert BF_1\rvert$ ⟹ 等腰直角 | $4$ | | M-T-330-V1 | $r=\frac{b^{2}}a$，钝角 ⟹ $\frac{b^{4}}{a^{2}}>2c^{2}$ ⟹ $e^{4}-4e^{2}+1>0$ | $\left(0,\frac{\sqrt6-\sqrt2}2\right)$ | | M-T-330-V3 | $\triangle CBB^{\prime}\sim\triangle CAA^{\prime}$ ⟹ 面积比 $=\frac{\lvert BF\rvert}{\lvert AF\rvert}$ | $\frac45$ | | M-T-332-E1 | 重心定 $x_1+x_2=\frac12$、$y_1+y_2=1$ ⟹ $\lvert x_1-x_2\rvert=\frac{\sqrt3}4$、$\lvert AB\rvert=\frac{\sqrt{51}}4$ | $\frac{\sqrt{17}}{17}$ | | M-T-332-V1 | 内心 $\frac12(\lvert PF_1\rvert-\lvert PF_2\rvert)R=\lambda cR$ ⟹ $\lambda=\frac ae=\frac1e$ | $\frac{\sqrt2}4$ | | M-T-332-V2 | 周长 $=4a=16$、$r=\frac12$ ⟹ $S=4$；又 $S=3\lvert y_1-y_2\rvert$ | $\frac43$ | | M-T-333-E1 | $m=a_1+a_2,n=a_1-a_2$ 代入余弦定理 | B | | M-T-333-V1 | $\theta=\frac\pi6$ 代入共焦点公式，两边乘 $4$ | $4$ | """

T330_E1 = {
    'type': '填空',
    'stem_text': (
        r"已知 $F_1,F_2$ 分别是双曲线 $x^{2}-\dfrac{y^{2}}{b^{2}}=1$ 的左、右焦点，$A$ 是双曲线上在第一象限内的点，"
        r"若 $\lvert AF_2\rvert=2$ 且 $\angle F_1AF_2=45^\circ$．延长 $AF_2$ 交双曲线右支于点 $B$，"
        r"则 $\triangle F_1AB$ 的面积等于 ____"
    ),
    'opts': [],
    'answer': r"$4$",
    'analysis': (
        r"由定义得 $\lvert AF_1\rvert=4$；由 $A,F_2,B$ 共线且 $F_2$ 在中间得 $\lvert AB\rvert=\lvert AF_2\rvert+\lvert BF_2\rvert=\lvert BF_1\rvert$，"
        r"故 $\triangle ABF_1$ 等腰；再由底角 $45^\circ$ 知它是等腰直角三角形，斜边 $\lvert AF_1\rvert=4$。"
    ),
    'solution': (
        r"由 $x^{2}-\dfrac{y^{2}}{b^{2}}=1$ 知 $a=1$，故 $2a=2$．" "\n"
        r"**第一步：$\lvert AF_1\rvert$**" "\n"
        r"$A$ 在右支上，由双曲线定义 $\lvert AF_1\rvert-\lvert AF_2\rvert=2a=2$，又 $\lvert AF_2\rvert=2$，得 $\lvert AF_1\rvert=4$．" "\n"
        r"**第二步：证 $\triangle ABF_1$ 为等腰三角形**" "\n"
        r"设 $\lvert BF_2\rvert=t$，则 $\lvert BF_1\rvert=t+2a=t+2$．" "\n"
        r"因 $A$ 在第一象限的右支上，而 $F_2(c,0)$ 在右支「开口内」，故直线 $AF_2$ 与右支的两个交点 $A,B$ 分居 $F_2$ 两侧，" "\n"
        r"即 $F_2$ 在线段 $AB$ 上，于是 $\lvert AB\rvert=\lvert AF_2\rvert+\lvert BF_2\rvert=2+t=\lvert BF_1\rvert$．" "\n"
        r"**第三步：定形状**" "\n"
        r"由 $\lvert AB\rvert=\lvert BF_1\rvert$ 知 $\triangle ABF_1$ 等腰（腰为 $AB$ 与 $BF_1$，底为 $AF_1$）．" "\n"
        r"又 $A,F_2,B$ 共线，$\angle BAF_1=\angle F_2AF_1=45^\circ$，故底角 $\angle BAF_1=\angle AF_1B=45^\circ$，" "\n"
        r"顶角 $\angle ABF_1=90^\circ$ —— $\triangle ABF_1$ 是**等腰直角三角形**．" "\n"
        r"**第四步：求面积**" "\n"
        r"斜边 $\lvert AF_1\rvert=4$，故直角边 $\lvert AB\rvert=\lvert BF_1\rvert=\dfrac4{\sqrt2}=2\sqrt2$，" "\n"
        r"$S_{\triangle F_1AB}=\dfrac12\cdot\lvert AB\rvert\cdot\lvert BF_1\rvert=\dfrac12\cdot2\sqrt2\cdot2\sqrt2=\dfrac12\cdot8=4$．"
    ),
    'review': (
        r"★ 题干、答案完整 ✓。原书 p305 详解：" "\n"
        r"「由题意知 $a=1$，根据双曲线定义 $\lvert AF_1\rvert-\lvert AF_2\rvert=2a$，所以 $\lvert AF_1\rvert=4$，" "\n"
        r"$\lvert BF_1\rvert-\lvert BF_2\rvert=2$，所以 $\lvert BF_1\rvert=2+\lvert BF_2\rvert$。由图知 $\lvert AB\rvert=\lvert AF_2\rvert+\lvert BF_2\rvert=2+\lvert BF_2\rvert$，" "\n"
        r"所以 $\lvert BA\rvert=\lvert BF_1\rvert$，$\triangle ABF_1$ 为等腰三角形，又因为 $\angle F_1AF_2=45^\circ$，所以 $\angle ABF_1=90^\circ$，" "\n"
        r"则 $\triangle ABF_1$ 为等腰直角三角形，所以 $\lvert AB\rvert=\lvert BF_1\rvert=2\sqrt2$。所以 $S=\frac12\times2\sqrt2\times2\sqrt2=4$」" "\n"
        r"—— **$\lvert AF_1\rvert=4$、等腰、$\angle ABF_1=90^\circ$、$\lvert AB\rvert=2\sqrt2$、$S=4$ 全部与我的推导一致** ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **$a=1$**：$x^{2}-\frac{y^{2}}{b^{2}}=1$ 中 $a^{2}=1$ ✓✓" "\n"
        r"② **$\lvert AF_1\rvert=4$**：定义差 $=2a=2$，$\lvert AF_1\rvert=2+2=4$ ✓✓✓" "\n"
        r"③ **$F_2$ 在 $A,B$ 之间**：$F_2(c,0)$、$c>1=a$，右支为 $x\ge1$ 的「杯形」，$F_2$ 在杯内 ⟹ 过 $F_2$ 的直线与右支交于两点且 $F_2$ 在中间 ✓✓" "\n"
        r"④ **$\lvert AB\rvert=\lvert BF_1\rvert$**：$\lvert AB\rvert=2+t$、$\lvert BF_1\rvert=t+2$ ✓✓✓ **恒等**" "\n"
        r"⑤ **等腰直角三角形自洽**：腰 $2\sqrt2$、$2\sqrt2$，斜边 $=\sqrt{8+8}=4=\lvert AF_1\rvert$ ✓✓✓" "\n"
        r"⑥ **$b$ 是否可求（检验题设相容性）**：需存在 $b$ 与点 $A$ 使 $\lvert AF_2\rvert=2$、$\angle F_1AF_2=45^\circ$。" "\n"
        r"在 $\triangle AF_1F_2$ 中，$\lvert AF_1\rvert=4$、$\lvert AF_2\rvert=2$、$\angle F_1AF_2=45^\circ$，由余弦定理：" "\n"
        r"$(2c)^{2}=16+4-2\cdot4\cdot2\cos45^\circ=20-16\cdot\dfrac{\sqrt2}2=20-8\sqrt2\approx8.686$，$c\approx1.473>a=1$ ✓ **合理**" "\n"
        r"$b^{2}=c^{2}-a^{2}\approx2.169-1=1.169>0$ ✓✓ **存在**" "\n"
        r"⑦ **数值检验**：取 $c=1.473$、$b^{2}=1.169$。$\lvert AF_1\rvert=4$、$\lvert AF_2\rvert=2$、$\lvert F_1F_2\rvert=2.946$。" "\n"
        r"检验三角形：$\cos\angle F_1AF_2=\frac{16+4-8.686}{2\cdot4\cdot2}=\frac{11.314}{16}=0.7071$ ⟹ 角 $=45^\circ$ ✓✓✓" "\n"
        r"**答案 $4$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（双曲线焦点弦上的等腰构造）**：" "\n"
        r"① ⭐⭐ **本题的破题眼是「$\lvert AB\rvert=\lvert AF_2\rvert+\lvert BF_2\rvert$」与「$\lvert BF_1\rvert=\lvert BF_2\rvert+2a$」恰好相等**，" "\n"
        r"因为 $\lvert AF_2\rvert=2=2a$ —— 只要**弦端点到近焦点的距离恰好等于 $2a$**，就必然出现等腰；" "\n"
        r"② ⭐ **过焦点的直线与同支交于两点时，焦点在两点之间**（见 M-T-328-E1 同款结论）—— " "\n"
        r"这是把 $\lvert AB\rvert$ 写成**两焦半径之和**（而非差）的依据，弄反就全错；" "\n"
        r"③ ⭐ **等腰 + 一个 $45^\circ$ 底角 ⟹ 等腰直角**：$45^\circ+45^\circ=90^\circ$，顶角必为 $90^\circ$；" "\n"
        r"④ ⭐ **已知斜边求面积最快**：等腰直角 $S=\frac{\text{斜边}^2}4=\frac{16}4=4$ —— 不必先算腰；" "\n"
        r"⑤ 检验题设相容性：**用余弦定理反算 $c$**，确认 $c>a$ 且 $b^{2}>0$（本题 $c\approx1.473$、$b^{2}\approx1.169$ ✓）。"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-330'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-330-E1',
}

T330_V1 = {
    'type': '填空',
    'stem_text': (
        r"点 $M$ 是椭圆 $\dfrac{x^{2}}{a^{2}}+\dfrac{y^{2}}{b^{2}}=1$（$a>b>0$）上的点，以 $M$ 为圆心的圆与 $x$ 轴相切于椭圆的焦点 $F$，"
        r"圆 $M$ 与 $y$ 轴相交于 $P,Q$，若 $\triangle PQM$ 是钝角三角形，则椭圆离心率的取值范围是 ____"
    ),
    'opts': [],
    'answer': r"$\left(0,\dfrac{\sqrt6-\sqrt2}2\right)$",
    'analysis': (
        r"圆心 $M$ 在 $F$ 正上方，半径 $r=\lvert y_M\rvert=\frac{b^{2}}a$；$P,Q$ 在 $y$ 轴上且 $MP=MQ=r$，"
        r"故钝角只能在顶点 $M$，等价于半顶角 $>45^\circ$，即 $\sqrt{r^{2}-c^{2}}>c$ ⟹ $e^{4}-4e^{2}+1>0$。"
    ),
    'solution': (
        r"**第一步：定圆心与半径**" "\n"
        r"圆与 $x$ 轴相切于焦点 $F(c,0)$，故圆心 $M$ 在 $F$ 的正上方（或下方），可设 $M(c,y_M)$，半径 $r=\lvert y_M\rvert$．" "\n"
        r"$M$ 在椭圆上：$\dfrac{c^{2}}{a^{2}}+\dfrac{y_M^{2}}{b^{2}}=1\Rightarrow y_M^{2}=b^{2}\!\left(1-\dfrac{c^{2}}{a^{2}}\right)=b^{2}\cdot\dfrac{a^{2}-c^{2}}{a^{2}}=\dfrac{b^{4}}{a^{2}}$，" "\n"
        r"故 $r=\dfrac{b^{2}}a$．" "\n"
        r"**第二步：把「钝角」翻译成不等式**" "\n"
        r"设 $MN\perp y$ 轴于 $N$，则 $N(0,y_M)$、$\lvert MN\rvert=c$，且由对称性 $\lvert PN\rvert=\lvert NQ\rvert=\sqrt{r^{2}-c^{2}}$．" "\n"
        r"因 $MP=MQ=r$，$\triangle PQM$ 是等腰三角形（顶点 $M$）．等腰三角形的两个底角相等且必为锐角，" "\n"
        r"故「钝角」只能是顶角 $\angle PMQ$．由 $MN$ 平分顶角，$\angle PMQ>90^\circ\iff\angle PMN>45^\circ$，" "\n"
        r"即 $\tan\angle PMN=\dfrac{\lvert PN\rvert}{\lvert MN\rvert}>1\iff\lvert PN\rvert>\lvert MN\rvert\iff r^{2}-c^{2}>c^{2}$．" "\n"
        r"**第三步：化成关于 $e$ 的不等式**" "\n"
        r"$\dfrac{b^{4}}{a^{2}}>2c^{2}$，代入 $b^{2}=a^{2}-c^{2}$ 并记 $e=\dfrac ca$：" "\n"
        r"$\dfrac{(a^{2}-c^{2})^{2}}{a^{2}}>2c^{2}\iff(1-e^{2})^{2}>2e^{2}\iff e^{4}-4e^{2}+1>0$．" "\n"
        r"令 $u=e^{2}\in(0,1)$：$u^{2}-4u+1>0$，根为 $u=2\pm\sqrt3$，故 $u<2-\sqrt3$（另一支 $u>2+\sqrt3>1$ 舍去）．" "\n"
        r"于是 $e<\sqrt{2-\sqrt3}$，而 $\sqrt{2-\sqrt3}=\dfrac{\sqrt6-\sqrt2}2$（因 $\left(\frac{\sqrt6-\sqrt2}2\right)^{2}=\frac{8-4\sqrt3}4=2-\sqrt3$）．" "\n"
        r"又 $e>0$，故 $e\in\left(0,\dfrac{\sqrt6-\sqrt2}2\right)$．"
    ),
    'review': (
        r"★ 题干、答案完整 ✓。原书 p305 详解：" "\n"
        r"「∵ 圆 $M$ 与 $x$ 轴相切于焦点 $F$，∴ 不妨设 $M(c,y)$，则（因为相切，则圆心与 $F$ 的连线必垂直于 $x$ 轴）…" "\n"
        r"$M$ 在椭圆上，则 $y=\pm\frac{b^{2}}a$（$a^{2}=b^{2}+c^{2}$），∴ 圆的半径为 $\frac{b^{2}}a$，过 $M$ 作 $MN\perp y$ 轴于 $N$，则 $PN=NQ$，$MN=c$…" "\n"
        r"∵ $\angle PMQ$ 为钝角，则 $\angle PMN=\angle QMN>45^\circ$，$PN=NQ>MN=c$，所以得 $\frac{b^{4}}{a^{2}}-c^{2}>c^{2}$…" "\n"
        r"$\frac1{e^{2}}-4+e^{2}>0$，$e^{4}-4e^{2}+1>0$，$(e^{2}-2)^{2}-3>0$…∴ $0<e<\frac{\sqrt6-\sqrt2}2$」" "\n"
        r"—— **$r=\frac{b^{2}}a$、$PN=c$ 的比较、$e^{4}-4e^{2}+1>0$、右端 $\frac{\sqrt6-\sqrt2}2$ 全部与我的推导一致** ✓✓✓" "\n"
        r"**⚠ 答案还原**：ref_bank 存 `0, 6 - 2 /2`，实为 $\left(0,\frac{\sqrt6-\sqrt2}2\right)$（**两个根号都丢了**）。" "\n"
        r"**判定依据**：$\frac{\sqrt6-\sqrt2}2=\frac{2.449-1.414}2=0.5176$；而 $e<\sqrt{2-\sqrt3}=\sqrt{0.2679}=0.5176$ ✓✓✓ **完全吻合**" "\n"
        r"（若按字面「$6-2$ 再除以 $2$」得 $2>1$，不是合法离心率，可直接排除）" "\n"
        r"**独立验算**：" "\n"
        r"① **$r=\frac{b^{2}}a$**：$\frac{c^{2}}{a^{2}}+\frac{y^{2}}{b^{2}}=1$ ⟹ $y^{2}=b^{2}(1-\frac{c^{2}}{a^{2}})=b^{2}\cdot\frac{b^{2}}{a^{2}}=\frac{b^{4}}{a^{2}}$ ✓✓✓" "\n"
        r"② **$\lvert MN\rvert=c$**：$M(c,y_M)$ 到 $y$ 轴的距离 $=c$ ✓✓" "\n"
        r"③ **$\lvert PN\rvert=\sqrt{r^{2}-c^{2}}$**：$P,Q$ 是圆与 $y$ 轴交点，$\lvert PN\rvert^{2}=r^{2}-\lvert MN\rvert^{2}$ ✓✓✓" "\n"
        r"④ **钝角只能在顶点 $M$**：$MP=MQ=r$ ⟹ 底角相等；若底角 $\ge90^\circ$ 则两底角和 $\ge180^\circ$ 矛盾 ✓✓✓" "\n"
        r"⑤ **$\angle PMQ>90^\circ\iff\angle PMN>45^\circ$**：$MN$ 是顶角平分线（等腰三角形三线合一）✓✓" "\n"
        r"$\tan\angle PMN=\frac{\lvert PN\rvert}{\lvert MN\rvert}>1\iff\lvert PN\rvert>c$ ✓✓✓" "\n"
        r"⑥ **$u^{2}-4u+1>0$ 的解**：$u=\frac{4\pm\sqrt{16-4}}2=2\pm\sqrt3$ ✓✓；$u<2-\sqrt3=0.2679$ 或 $u>2+\sqrt3$（舍）✓✓✓" "\n"
        r"⑦ **$\sqrt{2-\sqrt3}=\frac{\sqrt6-\sqrt2}2$**：$(\frac{\sqrt6-\sqrt2}2)^{2}=\frac{6+2-2\sqrt{12}}4=\frac{8-4\sqrt3}4=2-\sqrt3$ ✓✓✓" "\n"
        r"⑧ **数值检验**：取 $e=0.5\in(0,0.5176)$。设 $a=1$，则 $c=0.5$、$b^{2}=0.75$、$r=\frac{0.75}1=0.75$。" "\n"
        r"$\lvert PN\rvert=\sqrt{0.5625-0.25}=\sqrt{0.3125}=0.559>c=0.5$ ✓ **钝角** ✓✓✓" "\n"
        r"取 $e=0.6>0.5176$：$c=0.6$、$b^{2}=0.64$、$r=0.64$。$\lvert PN\rvert=\sqrt{0.4096-0.36}=\sqrt{0.0496}=0.2227<c$ ✗ **锐角** ✓✓✓ **排除正确**" "\n"
        r"⑨ **$P,Q$ 存在性**：需 $r>c$（$y$ 轴与圆相交），由 $\lvert PN\rvert>c$ 自动保证 ✓✓" "\n"
        r"**答案 $\left(0,\frac{\sqrt6-\sqrt2}2\right)$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（圆的切线 + 等腰三角形的钝角）**：" "\n"
        r"① ⭐⭐ **「圆与 $x$ 轴相切于焦点 $F$」⟹ 圆心在 $F$ 的正上方、半径 $=\lvert y_M\rvert$** —— " "\n"
        r"这一步把「圆」和「椭圆上的点」直接挂钩，是整题的枢纽；" "\n"
        r"② ⭐ **$M$ 在椭圆上且 $x_M=c$ ⟹ $\lvert y_M\rvert=\frac{b^{2}}a$**（$=a(1-e^{2})$）—— 建议记住，" "\n"
        r"它就是「焦点正上方的椭圆高度」，很多题都出现；" "\n"
        r"③ ⭐ **等腰三角形的钝角只能在顶点**（底角相等，不可能单个 $\ge90^\circ$）—— 这就省去了分类讨论；" "\n"
        r"④ ⭐ **「钝角」⟹「半顶角 $>45^\circ$」⟹「$\lvert PN\rvert>\lvert MN\rvert$」**，用正切把角度转成**边长比较**，计算量骤减；" "\n"
        r"⑤ ⭐ **$e^{4}-4e^{2}+1>0$ 这类「双二次」不等式**：换元 $u=e^{2}$，注意 $u\in(0,1)$ 只留一支；" "\n"
        r"⑥ **$\sqrt{2-\sqrt3}=\frac{\sqrt6-\sqrt2}2$ 这个二重根式化简**很常用，用平方验证即可；" "\n"
        r"⑦ ⚠ **答案里连续两个根号极易全丢**（本题存为 `6-2 /2`），**凡区间型答案先算数值再比对**。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-330'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-330-V1',
}

T330_V3 = {
    'type': '填空',
    'stem_text': (
        r"设抛物线 $y^{2}=2x$ 的焦点为 $F$，过点 $M(\sqrt3,0)$ 的直线与抛物线相交于 $A,B$ 两点，"
        r"与抛物线的准线相交于点 $C$，$\lvert BF\rvert=2$，则 $\triangle BCF$ 与 $\triangle ACF$ 的面积之比"
        r"$\dfrac{S_{\triangle BCF}}{S_{\triangle ACF}}=$ ____"
    ),
    'opts': [],
    'answer': r"$\dfrac45$",
    'analysis': (
        r"两个三角形共顶点 $F$、底边 $BC$ 与 $AC$ 在同一直线上，故面积比 $=\frac{\lvert BC\rvert}{\lvert AC\rvert}$；"
        r"由 $\triangle CBB^{\prime}\sim\triangle CAA^{\prime}$（$A^{\prime},B^{\prime}$ 为准线上的投影）得它就等于 $\frac{\lvert BB^{\prime}\rvert}{\lvert AA^{\prime}\rvert}=\frac{\lvert BF\rvert}{\lvert AF\rvert}$。"
    ),
    'solution': (
        r"由 $y^{2}=2x$ 知 $p=1$，焦点 $F\!\left(\dfrac12,0\right)$，准线 $x=-\dfrac12$．" "\n"
        r"**第一步：把面积比化成焦半径之比**" "\n"
        r"$\triangle BCF$ 与 $\triangle ACF$ 有公共顶点 $F$，底边 $BC,AC$ 共线，故 $\dfrac{S_{\triangle BCF}}{S_{\triangle ACF}}=\dfrac{\lvert BC\rvert}{\lvert AC\rvert}$．" "\n"
        r"设 $A^{\prime},B^{\prime}$ 分别是 $A,B$ 在准线上的投影（即 $AA^{\prime}\perp$ 准线、$BB^{\prime}\perp$ 准线），则 $A^{\prime},B^{\prime},C$ 都在准线上，且 $AA^{\prime}\parallel BB^{\prime}$，" "\n"
        r"于是 $\triangle CBB^{\prime}\sim\triangle CAA^{\prime}$，得 $\dfrac{\lvert BC\rvert}{\lvert AC\rvert}=\dfrac{\lvert BB^{\prime}\rvert}{\lvert AA^{\prime}\rvert}$．" "\n"
        r"由抛物线定义 $\lvert AA^{\prime}\rvert=\lvert AF\rvert$、$\lvert BB^{\prime}\rvert=\lvert BF\rvert$，故" "\n"
        r"$\dfrac{S_{\triangle BCF}}{S_{\triangle ACF}}=\dfrac{\lvert BF\rvert}{\lvert AF\rvert}$．" "\n"
        r"**第二步：求 $\lvert AF\rvert$**" "\n"
        r"由 $\lvert BF\rvert=x_B+\dfrac p2=x_B+\dfrac12=2$ 得 $x_B=\dfrac32$．" "\n"
        r"设直线 $AB$：$y=k(x-\sqrt3)$（过 $M(\sqrt3,0)$），代入 $y^{2}=2x$：" "\n"
        r"$k^{2}(x-\sqrt3)^{2}=2x\Rightarrow k^{2}x^{2}-(2\sqrt3k^{2}+2)x+3k^{2}=0$，故 $x_Ax_B=\dfrac{3k^{2}}{k^{2}}=3$．" "\n"
        r"于是 $x_A=\dfrac3{x_B}=\dfrac3{3/2}=2$，$\lvert AF\rvert=x_A+\dfrac12=\dfrac52$．" "\n"
        r"**第三步：得比值**" "\n"
        r"$\dfrac{S_{\triangle BCF}}{S_{\triangle ACF}}=\dfrac{\lvert BF\rvert}{\lvert AF\rvert}=\dfrac2{5/2}=\dfrac45$．"
    ),
    'review': (
        r"★ 题干、答案完整 ✓。原书 p305 详解：" "\n"
        r"「设 $F$ 到直线 $AB$ 的距离为 $d$，则 $\frac{S_{\triangle BCF}}{S_{\triangle ACF}}=\ldots$ 设 $AB:y=k(x-3)$ 代入 $y^{2}=2x$ 中易得 $x_Ax_B=3$，" "\n"
        r"从而可得 $x_A=2$…$\lvert AA^{\prime}\rvert=\frac52$，$\lvert BB^{\prime}\rvert=2$ ∴ $\frac{S_{\triangle BCF}}{S_{\triangle ACF}}=\frac45$」" "\n"
        r"—— **$x_Ax_B=3$、$x_A=2$、$\lvert AA^{\prime}\rvert=\frac52$、$\lvert BB^{\prime}\rvert=2$、结果 $\frac45$ 与我的推导一致** ✓✓✓" "\n"
        r"**⚠ 题干还原（本批最精彩的一处）**：ref_bank 存「过点 $M(3,0)$」，**实为 $M(\sqrt3,0)$（根号丢失）**。" "\n"
        r"**判定依据（反证）**：" "\n"
        r"① 若 $M(3,0)$，由 $x_Ax_B=m^{2}=9$ 与 $x_B=\frac32$ 得 $x_A=6$、$\lvert AF\rvert=6.5$，" "\n"
        r"比值 $=\frac2{6.5}=\frac4{13}\neq\frac45$ —— **与答案矛盾** ✗" "\n"
        r"② 要得 $\frac45$ 需 $\lvert AF\rvert=\frac52$ 即 $x_A=2$，则 $x_Ax_B=2\cdot\frac32=3=m^{2}$ ⟹ $m=\sqrt3$ ✓✓✓" "\n"
        r"**代回检验**：$B(\frac32,\sqrt3)$（$y_B^{2}=3=2x_B$ ✓）、$A(2,-2)$（$y_A^{2}=4=2x_A$ ✓）。" "\n"
        r"直线 $AB$ 斜率 $=\frac{\sqrt3-(-2)}{3/2-2}=\frac{3.732}{-0.5}=-7.464$；过 $M(\sqrt3,0)$ 的该直线在 $x=2$ 处：" "\n"
        r"$y=-7.464(2-1.732)=-7.464\times0.268=-2.0$ ✓✓✓ **恰为 $A$ 点** —— 三点共线确认" "\n"
        r"$\lvert AF\rvert=2+\frac12=\frac52$ ✓、$\lvert BF\rvert=\frac32+\frac12=2$ ✓ ⟹ 比值 $\frac45$ ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **$p=1$**：$y^{2}=2px=2x$ ⟹ $p=1$，焦点 $(\frac12,0)$、准线 $x=-\frac12$ ✓✓" "\n"
        r"② **面积比 $=\frac{\lvert BC\rvert}{\lvert AC\rvert}$**：两三角形共顶点 $F$，底边共线 ⟹ 高相同 ✓✓✓" "\n"
        r"③ **$\triangle CBB^{\prime}\sim\triangle CAA^{\prime}$**：$AA^{\prime}\parallel BB^{\prime}$（都垂直准线）、$C,A^{\prime},B^{\prime}$ 共线（都在准线上）✓✓" "\n"
        r"相似比 $\frac{\lvert BC\rvert}{\lvert AC\rvert}=\frac{\lvert BB^{\prime}\rvert}{\lvert AA^{\prime}\rvert}$ ✓✓✓" "\n"
        r"④ **$x_Ax_B=m^{2}$**：过 $(m,0)$ 的直线 $y=k(x-m)$ 代入 $y^{2}=2x$：" "\n"
        r"$k^{2}x^{2}-(2k^{2}m+2)x+k^{2}m^{2}=0$ ⟹ $x_Ax_B=\frac{k^{2}m^{2}}{k^{2}}=m^{2}$ ✓✓✓ **通式**" "\n"
        r"$m=\sqrt3$ ⟹ $x_Ax_B=3$ ✓✓（这正是原书「易得 $x_Ax_B=3$」的来源 —— **反证了 $m=\sqrt3$**）" "\n"
        r"⑤ **数值检验（坐标法直算）**：$B(\frac32,\sqrt3)$、$A(2,-2)$、$C$ 在 $x=-\frac12$ 处。" "\n"
        r"直线斜率 $-7.464$，在 $x=-\frac12$ 处 $y=-7.464(-0.5-1.732)=16.66$，$C=(-0.5,16.66)$。" "\n"
        r"$\lvert BC\rvert=\sqrt{(1.5+0.5)^{2}+(1.732-16.66)^{2}}=\sqrt{4+222.6}=15.05$" "\n"
        r"$\lvert AC\rvert=\sqrt{(2+0.5)^{2}+(-2-16.66)^{2}}=\sqrt{6.25+348.6}=18.84$" "\n"
        r"比值 $=\frac{15.05}{18.84}=0.799\approx\frac45$ ✓✓✓ **吻合**" "\n"
        r"**答案 $\frac45$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（抛物线弦与准线交点：相似三角形）**：" "\n"
        r"① ⭐⭐ **看到「弦与准线交于 $C$」+「两个三角形面积比」，第一步就想到 $\triangle CBB^{\prime}\sim\triangle CAA^{\prime}$**，" "\n"
        r"于是面积比 $=\frac{\lvert BC\rvert}{\lvert AC\rvert}=\frac{\lvert BB^{\prime}\rvert}{\lvert AA^{\prime}\rvert}=\frac{\lvert BF\rvert}{\lvert AF\rvert}$ —— " "\n"
        r"**直接把几何比转成焦半径之比**，不必求 $C$ 的坐标；" "\n"
        r"② ⭐ **过 $x$ 轴上点 $(m,0)$ 的弦满足 $x_Ax_B=m^{2}$**（对 $y^{2}=2px$ 恒成立，与斜率无关）—— 这个通式非常好用；" "\n"
        r"③ ⭐ **焦半径 $\lvert PF\rvert=x_P+\frac p2$**（$y^{2}=2px$），配合②可一步锁定两端点；" "\n"
        r"④ ⚠ **本题的 $m=\sqrt3$ 在提取时丢成了 $3$** —— " "\n"
        r"**凡是题面算出来的结果与标答不符，优先怀疑「某个数字的根号丢了」**，用 $x_Ax_B=m^{2}$ 反推 $m$ 即可；" "\n"
        r"⑤ 检验：把 $A,B,C$ 坐标全算出来直算长度比（$0.799\approx\frac45$），是最稳的收尾。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-330'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-330-V3',
}

T332_E1 = {
    'type': '填空',
    'stem_text': (
        r"已知 $F$ 是抛物线 $y^{2}=4x$ 的焦点，$A,B$ 在抛物线上，且 $\triangle ABF$ 的重心坐标为"
        r"$\left(\dfrac12,\dfrac13\right)$，则 $\dfrac{\bigl\lvert\lvert FA\rvert-\lvert FB\rvert\bigr\rvert}{\lvert AB\rvert}=$ ____"
    ),
    'opts': [],
    'answer': r"$\dfrac{\sqrt{17}}{17}$",
    'analysis': (
        r"重心给 $x_A+x_B=\frac12$、$y_A+y_B=1$；由 $y^{2}=4x$ 得 $y_A^{2}+y_A^{2}\!\to y_A^2+y_B^2=2$、$y_Ay_B=-\frac12$，"
        r"进而 $\lvert y_A-y_B\rvert=\sqrt3$、$\lvert x_A-x_B\rvert=\frac{\sqrt3}4$、$\lvert AB\rvert=\frac{\sqrt{51}}4$。"
    ),
    'solution': (
        r"由 $y^{2}=4x$ 知 $p=2$，焦点 $F(1,0)$．设 $A(x_A,y_A)$、$B(x_B,y_B)$．" "\n"
        r"**第一步：由重心定两坐标和**" "\n"
        r"$\dfrac{x_A+x_B+1}3=\dfrac12\Rightarrow x_A+x_B=\dfrac12$；$\dfrac{y_A+y_B+0}3=\dfrac13\Rightarrow y_A+y_B=1$．" "\n"
        r"**第二步：求 $y_Ay_B$**" "\n"
        r"$y_A^{2}=4x_A$、$y_B^{2}=4x_B$ ⟹ $y_A^{2}+y_B^{2}=4(x_A+x_B)=2$．" "\n"
        r"$(y_A+y_B)^{2}=y_A^{2}+y_B^{2}+2y_Ay_B\Rightarrow1=2+2y_Ay_B\Rightarrow y_Ay_B=-\dfrac12$．" "\n"
        r"**第三步：求两条差值**" "\n"
        r"$(y_A-y_B)^{2}=(y_A+y_B)^{2}-4y_Ay_B=1+2=3\Rightarrow\lvert y_A-y_B\rvert=\sqrt3$．" "\n"
        r"$x_A-x_B=\dfrac{y_A^{2}-y_B^{2}}4=\dfrac{(y_A-y_B)(y_A+y_B)}4=\dfrac{\sqrt3}4$（取绝对值）．" "\n"
        r"$\lvert AB\rvert=\sqrt{(x_A-x_B)^{2}+(y_A-y_B)^{2}}=\sqrt{\dfrac3{16}+3}=\sqrt{\dfrac{51}{16}}=\dfrac{\sqrt{51}}4$．" "\n"
        r"**第四步：焦半径之差**" "\n"
        r"$\lvert FA\rvert=x_A+\dfrac p2=x_A+1$，$\lvert FB\rvert=x_B+1$，故 $\bigl\lvert\lvert FA\rvert-\lvert FB\rvert\bigr\rvert=\lvert x_A-x_B\rvert=\dfrac{\sqrt3}4$．" "\n"
        r"$\dfrac{\bigl\lvert\lvert FA\rvert-\lvert FB\rvert\bigr\rvert}{\lvert AB\rvert}=\dfrac{\sqrt3/4}{\sqrt{51}/4}=\dfrac{\sqrt3}{\sqrt{51}}=\dfrac1{\sqrt{17}}=\dfrac{\sqrt{17}}{17}$．"
    ),
    'review': (
        r"★ 题干、答案完整 ✓。原书 p306 详解：" "\n"
        r"「由 $\vec{AB}=5\vec{FB}$ 可得 $\vec{AF}=4\vec{FB}$，设 $\lvert AF\rvert=4m,\lvert BF\rvert=m$…" "\n"
        r"过 $A,B$ 分别做准线的垂线，垂足为 $A^{\prime},B^{\prime}$…$\lvert AA^{\prime}\rvert=\frac{4m}e$，$\lvert BB^{\prime}\rvert=\frac me$…" "\n"
        r"因为 $AB$ 斜率为 $\sqrt3$，所以在 $\triangle ABD$ 中 $\angle BAD=60^\circ$，可得 $\lvert AD\rvert=\frac12\lvert AB\rvert$…" "\n"
        r"即 $\frac{4m}e-\frac me=\ldots$，解得 $e=\frac52$，$C$ 的离心率为 $\frac52$…$\frac{\lvert\lvert FA\rvert-\lvert FB\rvert\rvert}{\lvert AB\rvert}=\frac{\sqrt{17}}{17}$」" "\n"
        r"（⚠ 详解中混入了**另一道双曲线题**的片段 —— $\vec{AB}=5\vec{FB}$、斜率 $\sqrt3$、$e=\frac52$ 都属于那道题，" "\n"
        r"与本填空无关。**但最末的 $\frac{\sqrt{17}}{17}$ 与本答案一致** ✓）" "\n"
        r"**⚠ 答案还原**：ref_bank 存 `17/17`，实为 $\frac{\sqrt{17}}{17}$（**根号丢失**）。" "\n"
        r"**判定依据**：我的推导给 $\frac1{\sqrt{17}}=\frac{\sqrt{17}}{17}\approx0.2425$；若按字面 $\frac{17}{17}=1$，" "\n"
        r"意味着 $\lvert\lvert FA\rvert-\lvert FB\rvert\rvert=\lvert AB\rvert$，与三角形不等式矛盾（两边之差必小于第三边）✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **$p=2$、$F(1,0)$**：$y^{2}=2px=4x$ ⟹ $p=2$ ✓✓" "\n"
        r"② **$x_A+x_B=\frac12$、$y_A+y_B=1$**：重心 $=\frac{A+B+F}3$ ✓✓✓" "\n"
        r"③ **$y_A^{2}+y_B^{2}=2$**：$4(x_A+x_B)=4\cdot\frac12=2$ ✓✓✓" "\n"
        r"④ **$y_Ay_B=-\frac12$**：$(y_A+y_B)^{2}=1=2+2y_Ay_B$ ⟹ $y_Ay_B=-\frac12$ ✓✓✓" "\n"
        r"⑤ **$\lvert y_A-y_B\rvert=\sqrt3$**：$1-4(-\frac12)=1+2=3$ ✓✓✓" "\n"
        r"⑥ **$y_A,y_B$ 具体值**：$t^{2}-t-\frac12=0$ ⟹ $t=\frac{1\pm\sqrt3}2$，即 $y_A=\frac{1+\sqrt3}2=1.366$、$y_B=\frac{1-\sqrt3}2=-0.366$。" "\n"
        r"检验：$y_A+y_B=1$ ✓、$y_Ay_B=\frac{1-3}4=-\frac12$ ✓✓✓" "\n"
        r"$x_A=\frac{y_A^{2}}4=\frac{1.866}4=0.4665$、$x_B=\frac{0.134}4=0.0335$；$x_A+x_B=0.5$ ✓✓✓" "\n"
        r"⑦ **$\lvert x_A-x_B\rvert=\frac{\sqrt3}4$**：$0.4665-0.0335=0.433=\frac{\sqrt3}4=\frac{1.732}4=0.433$ ✓✓✓" "\n"
        r"⑧ **$\lvert AB\rvert=\frac{\sqrt{51}}4$**：$\sqrt{0.433^{2}+1.732^{2}}=\sqrt{0.1875+3}=\sqrt{3.1875}=1.7854$；$\frac{\sqrt{51}}4=\frac{7.141}4=1.785$ ✓✓✓" "\n"
        r"⑨ **焦半径**：$\lvert FA\rvert=x_A+1=1.4665$、$\lvert FB\rvert=x_B+1=1.0335$；差 $=0.433$ ✓✓" "\n"
        r"检验 $\lvert FA\rvert$ 定义：$A(0.4665,1.366)$、$F(1,0)$ ⟹ $\sqrt{(0.5335)^{2}+1.366^{2}}=\sqrt{0.2846+1.866}=\sqrt{2.151}=1.4666$ ✓✓✓" "\n"
        r"⑩ **最终比值**：$\frac{0.433}{1.7854}=0.2425=\frac1{\sqrt{17}}=\frac{\sqrt{17}}{17}$ ✓✓✓" "\n"
        r"**答案 $\frac{\sqrt{17}}{17}$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（抛物线上的「和差」题）**：" "\n"
        r"① ⭐⭐ **凡是给「重心/中点」的，第一步就是写坐标和**：$x_A+x_B$、$y_A+y_B$ 立刻得到；" "\n"
        r"② ⭐ **抛物线 $y^{2}=2px$ 上两点，用 $y$ 作自变量最方便**：$x=\frac{y^{2}}{2p}$ 代入，" "\n"
        r"于是 $x_A+x_B=\frac{y_A^{2}+y_B^{2}}{2p}$、$x_A-x_B=\frac{(y_A-y_B)(y_A+y_B)}{2p}$ —— " "\n"
        r"**$x$ 的差自动带上 $(y_A+y_B)$ 因子**，本题因此得 $\frac{\sqrt3}4$；" "\n"
        r"③ ⭐ **$(y_A-y_B)^{2}=(y_A+y_B)^{2}-4y_Ay_B$** —— 已知和、求差的万能式；" "\n"
        r"④ ⭐ **焦半径 $\lvert PF\rvert=x_P+\frac p2$**，所以 $\lvert\lvert FA\rvert-\lvert FB\rvert\rvert=\lvert x_A-x_B\rvert$（**常数 $\frac p2$ 抵消**）；" "\n"
        r"⑤ ⚠ **答案 $\frac{\sqrt{17}}{17}$ 会被提取成 `17/17`**，看到「分子分母相同」这类怪答案，**立刻想到根号丢失**；" "\n"
        r"用三角形不等式（两边之差 $<$ 第三边）可秒判：$\frac{17}{17}=1$ 不可能 ✓"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-332'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-332-E1',
}

T332_V1 = {
    'type': '填空',
    'stem_text': (
        r"已知点 $P$ 为双曲线 $\dfrac{x^{2}}{a^{2}}-\dfrac{y^{2}}{b^{2}}=1$（$a>0,b>0$）右支上的一点，"
        r"点 $F_1,F_2$ 分别为双曲线的左、右焦点，双曲线的一条渐近线的斜率为 $\sqrt7$，"
        r"若 $M$ 为 $\triangle PF_1F_2$ 的内心，且 $S_{\triangle PMF_1}=S_{\triangle PMF_2}+\lambda S_{\triangle MF_1F_2}$，则 $\lambda$ 的值为 ____"
    ),
    'opts': [],
    'answer': r"$\dfrac{\sqrt2}4$",
    'analysis': (
        r"设内切圆半径为 $R$，三项面积分别为 $\frac12\lvert PF_1\rvert R$、$\frac12\lvert PF_2\rvert R$、$\frac12\lvert F_1F_2\rvert R$，"
        r"代入后 $\frac12(\lvert PF_1\rvert-\lvert PF_2\rvert)=\lambda c$，即 $\lambda=\frac ae=\frac1e$；由 $\frac ba=\sqrt7$ 得 $e=2\sqrt2$。"
    ),
    'solution': (
        r"设 $\triangle PF_1F_2$ 的内切圆半径为 $R$（内心 $M$ 到三边的距离都是 $R$）．" "\n"
        r"$S_{\triangle PMF_1}=\dfrac12\lvert PF_1\rvert R$，$S_{\triangle PMF_2}=\dfrac12\lvert PF_2\rvert R$，$S_{\triangle MF_1F_2}=\dfrac12\lvert F_1F_2\rvert R=\dfrac12\cdot2c\cdot R=cR$．" "\n"
        r"代入 $S_{\triangle PMF_1}=S_{\triangle PMF_2}+\lambda S_{\triangle MF_1F_2}$：" "\n"
        r"$\dfrac12\lvert PF_1\rvert R=\dfrac12\lvert PF_2\rvert R+\lambda cR\Rightarrow\dfrac12\bigl(\lvert PF_1\rvert-\lvert PF_2\rvert\bigr)=\lambda c$．" "\n"
        r"$P$ 在右支上，由定义 $\lvert PF_1\rvert-\lvert PF_2\rvert=2a$，故 $\dfrac12\cdot2a=\lambda c$，即 $a=\lambda c$，" "\n"
        r"$\lambda=\dfrac ac=\dfrac1e$．" "\n"
        r"由渐近线斜率 $\dfrac ba=\sqrt7$ 得 $e=\sqrt{1+\dfrac{b^{2}}{a^{2}}}=\sqrt{1+7}=2\sqrt2$，" "\n"
        r"$\lambda=\dfrac1{2\sqrt2}=\dfrac{\sqrt2}4$．"
    ),
    'review': (
        r"★ 题干、答案完整 ✓（**详解未提取**，上述为我独立推导）。" "\n"
        r"ref_bank 存 `2/4`，实为 $\frac{\sqrt2}4$（**根号丢失**），与我的推导吻合 ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **面积公式**：内心 $M$ 到三边距离为 $R$，$\triangle PMF_1$ 以 $PF_1$ 为底、高为 $R$ ⟹ $S=\frac12\lvert PF_1\rvert R$ ✓✓✓" "\n"
        r"② **代入**：$\frac12\lvert PF_1\rvert R=\frac12\lvert PF_2\rvert R+\lambda cR$，约去 $R$（$R>0$）✓✓" "\n"
        r"$\frac12(\lvert PF_1\rvert-\lvert PF_2\rvert)=\lambda c$ ✓✓✓" "\n"
        r"③ **$\lvert PF_1\rvert-\lvert PF_2\rvert=2a$**（右支）✓✓⟹ $a=\lambda c$ ⟹ $\lambda=\frac ac=\frac1e$ ✓✓✓" "\n"
        r"④ **$e=2\sqrt2$**：$e^{2}=1+\frac{b^{2}}{a^{2}}=1+7=8$ ⟹ $e=2\sqrt2$ ✓✓✓" "\n"
        r"⑤ **$\lambda=\frac{\sqrt2}4$**：$\frac1{2\sqrt2}=\frac{\sqrt2}{2\sqrt2\cdot\sqrt2}=\frac{\sqrt2}4$ ✓✓✓" "\n"
        r"⑥ **数值检验**：取 $a=1$，则 $b=\sqrt7$、$c=2\sqrt2=2.828$。$e=2.828$、$\lambda=\frac1{2.828}=0.3536=\frac{\sqrt2}4$ ✓✓✓" "\n"
        r"取 $P$ 为右顶点 $(1,0)$：$\lvert PF_1\rvert=c+a=3.828$、$\lvert PF_2\rvert=c-a=1.828$，差 $=2=2a$ ✓✓✓" "\n"
        r"$\triangle PF_1F_2$ 此时退化（$P,F_1,F_2$ 共线）—— 改取 $P$ 使 $x=2$：$y^{2}=7(4-1)=21$，$y=\sqrt{21}=4.583$。" "\n"
        r"$\lvert PF_1\rvert=\sqrt{(2+2.828)^{2}+21}=\sqrt{23.31+21}=\sqrt{44.31}=6.657$" "\n"
        r"$\lvert PF_2\rvert=\sqrt{(2-2.828)^{2}+21}=\sqrt{0.685+21}=\sqrt{21.685}=4.657$；差 $=2.000$ ✓✓✓ **恰为 $2a$**" "\n"
        r"$\lambda=\frac{\lvert PF_1\rvert-\lvert PF_2\rvert}{2c}=\frac2{5.657}=0.3536$ ✓✓✓ **与 $\frac{\sqrt2}4$ 一致**" "\n"
        r"**答案 $\frac{\sqrt2}4$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（内心的面积拆分）**：" "\n"
        r"① ⭐⭐ **内心把三角形拆成三个小三角形，各自面积 $=\frac12\times(\text{对应边})\times R$** —— " "\n"
        r"这是处理「内心 + 面积关系」的唯一入口，务必第一时间使用；" "\n"
        r"② ⭐ **约去 $R$ 后，面积关系就变成了边长关系**：本题直接给出 $\lvert PF_1\rvert-\lvert PF_2\rvert=2\lambda c$；" "\n"
        r"③ ⭐ **再套曲线定义**：右支 $\lvert PF_1\rvert-\lvert PF_2\rvert=2a$ ⟹ $\lambda=\frac ae=\frac1e$ —— " "\n"
        r"**结果只与 $e$ 有关，与 $P$ 的位置无关**，这正是题目敢只给渐近线斜率的原因；" "\n"
        r"④ ⚠ **左支上则是 $\lvert PF_2\rvert-\lvert PF_1\rvert=2a$，$\lambda$ 会是负的** —— 看清 $P$ 在哪一支；" "\n"
        r"⑤ **$e=\sqrt{1+(\frac ba)^{2}}$**，渐近线斜率给 $\frac ba$ 就是给 $e$，一步到位；" "\n"
        r"⑥ ⚠ **答案 $\frac{\sqrt2}4$ 提取成 `2/4`**（与 M-T-327-E1 同款），用数值 $\frac{\sqrt2}4=0.3536\neq0.5$ 立判 ✓"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-332'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-332-V1',
}

T332_V2 = {
    'type': '填空',
    'stem_text': (
        r"椭圆 $\dfrac{x^{2}}{16}+\dfrac{y^{2}}7=1$ 的左、右焦点分别为 $F_1,F_2$，弦 $AB$ 过点 $F_1$，"
        r"若 $\triangle ABF_2$ 的内切圆周长为 $\pi$，$A,B$ 两点的坐标分别为 $(x_1,y_1),(x_2,y_2)$，"
        r"则 $\lvert y_1-y_2\rvert=$ ____"
    ),
    'opts': [],
    'answer': r"$\dfrac43$",
    'analysis': (
        r"内切圆周长 $\pi$ ⟹ $r=\frac12$；$\triangle ABF_2$ 的周长 $=4a=16$；由 $S=\frac12\cdot$周长$\cdot r$ 得 $S=4$；"
        r"又 $S=S_{\triangle AF_1F_2}+S_{\triangle BF_1F_2}=3\lvert y_1\rvert+3\lvert y_2\rvert=3\lvert y_1-y_2\rvert$。"
    ),
    'solution': (
        r"由 $a^{2}=16,b^{2}=7$ 得 $a=4$、$c=\sqrt{16-7}=3$，故 $\lvert F_1F_2\rvert=2c=6$．" "\n"
        r"**第一步：求内切圆半径**" "\n"
        r"内切圆周长 $=2\pi r=\pi\Rightarrow r=\dfrac12$．" "\n"
        r"**第二步：求 $\triangle ABF_2$ 的周长**" "\n"
        r"弦 $AB$ 过 $F_1$，故 $\lvert AB\rvert=\lvert AF_1\rvert+\lvert BF_1\rvert$．" "\n"
        r"由椭圆定义 $\lvert AF_1\rvert+\lvert AF_2\rvert=2a$、$\lvert BF_1\rvert+\lvert BF_2\rvert=2a$，于是" "\n"
        r"周长 $=\lvert AB\rvert+\lvert AF_2\rvert+\lvert BF_2\rvert=(\lvert AF_1\rvert+\lvert AF_2\rvert)+(\lvert BF_1\rvert+\lvert BF_2\rvert)=4a=16$．" "\n"
        r"**第三步：求面积**" "\n"
        r"$S=\dfrac12\cdot\text{周长}\cdot r=\dfrac12\cdot16\cdot\dfrac12=4$．" "\n"
        r"**第四步：把面积写成 $\lvert y_1-y_2\rvert$**" "\n"
        r"因 $A,F_1,B$ 共线且 $F_1$ 在 $x$ 轴上，$A,B$ 分居 $x$ 轴两侧，故" "\n"
        r"$S=S_{\triangle AF_1F_2}+S_{\triangle BF_1F_2}=\dfrac12\cdot\lvert F_1F_2\rvert\cdot\lvert y_1\rvert+\dfrac12\cdot\lvert F_1F_2\rvert\cdot\lvert y_2\rvert=3\lvert y_1\rvert+3\lvert y_2\rvert=3\lvert y_1-y_2\rvert$．" "\n"
        r"（因 $y_1,y_2$ 异号，$\lvert y_1\rvert+\lvert y_2\rvert=\lvert y_1-y_2\rvert$）" "\n"
        r"故 $3\lvert y_1-y_2\rvert=4\Rightarrow\lvert y_1-y_2\rvert=\dfrac43$．"
    ),
    'review': (
        r"★ 题干、答案完整 ✓（**详解未提取**，上述为我独立推导）。答案与原书标注 $\frac43$ 一致 ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **$a=4,c=3$**：$a^{2}=16$、$b^{2}=7$ ⟹ $c=\sqrt9=3$ ✓✓；$\lvert F_1F_2\rvert=6$ ✓✓" "\n"
        r"② **$r=\frac12$**：$2\pi r=\pi$ ⟹ $r=\frac12$ ✓✓✓" "\n"
        r"③ **周长 $=4a=16$**：$\lvert AB\rvert=\lvert AF_1\rvert+\lvert BF_1\rvert$（$F_1$ 在弦 $AB$ 上）✓✓" "\n"
        r"$(\lvert AF_1\rvert+\lvert AF_2\rvert)+(\lvert BF_1\rvert+\lvert BF_2\rvert)=8+8=16$ ✓✓✓" "\n"
        r"④ **$S=\frac12\cdot16\cdot\frac12=4$**：三角形面积 $=\frac12\cdot$周长$\cdot$内切圆半径（通用公式）✓✓✓" "\n"
        r"（验证：$S=\sum\frac12\cdot\text{边}\cdot r=\frac12 r\sum\text{边}=\frac12\cdot\frac12\cdot16=4$ ✓）" "\n"
        r"⑤ **$S=3\lvert y_1-y_2\rvert$**：$\frac12\cdot6\cdot(\lvert y_1\rvert+\lvert y_2\rvert)=3(\lvert y_1\rvert+\lvert y_2\rvert)$ ✓✓" "\n"
        r"$A,B$ 在 $x$ 轴两侧（弦过 $F_1$ 且不垂直于 $y$ 轴时）⟹ $y_1y_2<0$ ⟹ $\lvert y_1\rvert+\lvert y_2\rvert=\lvert y_1-y_2\rvert$ ✓✓✓" "\n"
        r"⑥ **数值检验**：取过 $F_1(-3,0)$ 的竖直线 $x=-3$：$y^{2}=7(1-\frac9{16})=7\cdot\frac7{16}=\frac{49}{16}$，$y=\pm\frac74$。" "\n"
        r"$\lvert y_1-y_2\rvert=\frac72=3.5\neq\frac43$ —— 但此时**内切圆周长不是 $\pi$**，故该弦不满足条件 ✓ 无关" "\n"
        r"改取斜弦：设直线 $y=k(x+3)$，与椭圆联立可解；取 $k=1$：" "\n"
        r"$\frac{x^{2}}{16}+\frac{(x+3)^{2}}7=1\Rightarrow7x^{2}+16(x^{2}+6x+9)=112\Rightarrow23x^{2}+96x+32=0$" "\n"
        r"$x=\frac{-96\pm\sqrt{9216-2944}}{46}=\frac{-96\pm\sqrt{6272}}{46}$；$\sqrt{6272}=79.20$ ⟹ $x_1=-0.365$、$x_2=-3.809$" "\n"
        r"$y_1=x_1+3=2.635$、$y_2=x_2+3=-0.809$；$y_1,y_2$ 异号 ✓" "\n"
        r"$\lvert y_1-y_2\rvert=3.444$；$\lvert AB\rvert=\sqrt{2}\cdot\lvert x_1-x_2\rvert=1.414\times3.444=4.870$" "\n"
        r"$\lvert AF_2\rvert$：$F_2(3,0)$，$A(-0.365,2.635)$ ⟹ $\sqrt{11.32+6.94}=\sqrt{18.26}=4.273$" "\n"
        r"$B(-3.809,-0.809)$ ⟹ $\sqrt{46.36+0.654}=\sqrt{47.01}=6.857$" "\n"
        r"周长 $=4.870+4.273+6.857=16.00$ ✓✓✓ **确为 $16$**（与 $4a$ 一致，验证了③）" "\n"
        r"$S=\frac12\cdot6\cdot(2.635+0.809)=3\times3.444=10.33$；$r=\frac{2S}{\text{周长}}=\frac{20.66}{16}=1.291$ ⟹ 周长 $2\pi r=8.11\neq\pi$ ✗" "\n"
        r"（该弦不满足题设，但**周长恒为 $16$ 已严格验证** ✓✓，而 $r$ 由题设给 $\frac12$，故 $S$ 必为 $4$）" "\n"
        r"⟹ $\lvert y_1-y_2\rvert=\frac S3=\frac43$ ✓✓✓" "\n"
        r"**答案 $\frac43$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（焦点弦三角形的内切圆）**：" "\n"
        r"① ⭐⭐ **过焦点的弦 $AB$ 与另一焦点构成的 $\triangle ABF_2$，其周长恒为 $4a$** —— " "\n"
        r"因为 $\lvert AB\rvert=\lvert AF_1\rvert+\lvert BF_1\rvert$，配上两条定义式正好凑成两个 $2a$。**这个结论要记牢**；" "\n"
        r"② ⭐ **$S=\frac12\cdot$周长$\cdot r$**（内切圆半径的万能式），于是「周长 $+r$」一给，面积立得；" "\n"
        r"③ ⭐ **$\triangle ABF_2$ 的面积 $=\frac12\lvert F_1F_2\rvert\cdot(\lvert y_1\rvert+\lvert y_2\rvert)$**，" "\n"
        r"因为 $F_1$ 在 $AB$ 上，把它拆成两个以 $F_1F_2$ 为底的小三角形；" "\n"
        r"④ ⚠ **$y_1,y_2$ 异号才能合并成 $\lvert y_1-y_2\rvert$** —— 弦过 $x$ 轴上的点 $F_1$，两端点必在 $x$ 轴两侧（除非弦就是 $x$ 轴，此时面积为 $0$，不合题意）；" "\n"
        r"⑤ 检验：**任取一条过 $F_1$ 的弦算周长**（本题得 $16.00$），可严格验证①，比验证最终答案更快。"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-332'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-332-V2',
}

T333_E1 = {
    'type': '选择',
    'stem_text': (
        r"椭圆与双曲线共焦点 $F_1,F_2$，它们的交点 $P$ 对两公共焦点 $F_1,F_2$ 的张角为 $\angle F_1PF_2=2\theta$，"
        r"椭圆与双曲线的离心率分别为 $e_1,e_2$，则（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac{\cos^{2}\theta}{e_1^{2}}+\dfrac{\sin^{2}\theta}{e_2^{2}}=1$"),
        ('B', r"$\dfrac{\sin^{2}\theta}{e_1^{2}}+\dfrac{\cos^{2}\theta}{e_2^{2}}=1$"),
        ('C', r"$\dfrac{e_1^{2}}{\cos^{2}\theta}+\dfrac{e_2^{2}}{\sin^{2}\theta}=1$"),
        ('D', r"$\dfrac{e_1^{2}}{\sin^{2}\theta}+\dfrac{e_2^{2}}{\cos^{2}\theta}=1$"),
    ],
    'answer': 'B',
    'analysis': (
        r"设 $\lvert PF_1\rvert=m,\lvert PF_2\rvert=n$，由两曲线定义得 $m=a_1+a_2$、$n=a_1-a_2$；"
        r"代入余弦定理 $m^{2}+n^{2}-2mn\cos2\theta=4c^{2}$，化简即得 $\frac{\sin^{2}\theta}{e_1^{2}}+\frac{\cos^{2}\theta}{e_2^{2}}=1$。"
    ),
    'solution': (
        r"设椭圆长半轴为 $a_1$、双曲线实半轴为 $a_2$，公共焦距为 $2c$．设 $\lvert PF_1\rvert=m$、$\lvert PF_2\rvert=n$．" "\n"
        r"由椭圆定义 $m+n=2a_1$，由双曲线定义 $\lvert m-n\rvert=2a_2$（不妨 $m>n$），解得" "\n"
        r"$m=a_1+a_2$，$n=a_1-a_2$．" "\n"
        r"在 $\triangle PF_1F_2$ 中由余弦定理（$\angle F_1PF_2=2\theta$）：" "\n"
        r"$m^{2}+n^{2}-2mn\cos2\theta=(2c)^{2}=4c^{2}$．" "\n"
        r"代入 $m,n$：$m^{2}+n^{2}=2(a_1^{2}+a_2^{2})$，$mn=a_1^{2}-a_2^{2}$，故" "\n"
        r"$2(a_1^{2}+a_2^{2})-2(a_1^{2}-a_2^{2})\cos2\theta=4c^{2}$，即" "\n"
        r"$a_1^{2}(1-\cos2\theta)+a_2^{2}(1+\cos2\theta)=2c^{2}$．" "\n"
        r"用 $1-\cos2\theta=2\sin^{2}\theta$、$1+\cos2\theta=2\cos^{2}\theta$：" "\n"
        r"$2a_1^{2}\sin^{2}\theta+2a_2^{2}\cos^{2}\theta=2c^{2}\Rightarrow\dfrac{a_1^{2}\sin^{2}\theta}{c^{2}}+\dfrac{a_2^{2}\cos^{2}\theta}{c^{2}}=1$．" "\n"
        r"由 $e_1=\dfrac c{a_1}$、$e_2=\dfrac c{a_2}$ 得 $\dfrac{\sin^{2}\theta}{e_1^{2}}+\dfrac{\cos^{2}\theta}{e_2^{2}}=1$，故选 **B**．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓。原书 p307 详解：" "\n"
        r"「设椭圆的长轴长为 $2a_1$，双曲线的实轴长为 $2a_2$，并设 $\lvert PF_1\rvert=m,\lvert PF_2\rvert=n$，焦距为 $2c$，" "\n"
        r"在 $\triangle PF_1F_2$ 中，由余弦定理得 $m^{2}+n^{2}-2mn\cos2\theta=(2c)^{2}$，由椭圆和双曲线的定义得" "\n"
        r"$m+n=2a_1$、$m-n=2a_2$，解得 $m=a_1+a_2$、$n=a_1-a_2$。代入得 $(a_1+a_2)^{2}+(a_1-a_2)^{2}-2(a_1+a_2)(a_1-a_2)\cos2\theta=4c^{2}$，" "\n"
        r"即 $a_1^{2}+a_2^{2}+(a_1^{2}-a_2^{2})\cos2\theta=2c^{2}$，∴ $a_1^{2}(1-\cos2\theta)+a_2^{2}(1+\cos2\theta)=2c^{2}$，" "\n"
        r"即 $2a_1^{2}\sin^{2}\theta+2a_2^{2}\cos^{2}\theta=2c^{2}$，∴ $\frac{a_1^{2}\sin^{2}\theta}{c^{2}}+\frac{a_2^{2}\cos^{2}\theta}{c^{2}}=1$，" "\n"
        r"因此 $\frac{\sin^{2}\theta}{e_1^{2}}+\frac{\cos^{2}\theta}{e_2^{2}}=1$。故选：B」" "\n"
        r"—— **与我的推导逐字一致** ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **$m=a_1+a_2$、$n=a_1-a_2$**：$m+n=2a_1$ ✓、$m-n=2a_2$ ✓✓✓" "\n"
        r"② **$m^{2}+n^{2}=2(a_1^{2}+a_2^{2})$**：$(a_1+a_2)^{2}+(a_1-a_2)^{2}=2a_1^{2}+2a_2^{2}$ ✓✓✓" "\n"
        r"③ **$mn=a_1^{2}-a_2^{2}$** ✓✓✓" "\n"
        r"④ **$2(a_1^{2}+a_2^{2})-2(a_1^{2}-a_2^{2})\cos2\theta=4c^{2}$** ⟹ 除以 $2$：" "\n"
        r"$a_1^{2}+a_2^{2}-(a_1^{2}-a_2^{2})\cos2\theta=2c^{2}$ ⟹ $a_1^{2}(1-\cos2\theta)+a_2^{2}(1+\cos2\theta)=2c^{2}$ ✓✓✓" "\n"
        r"⑤ **半角公式**：$1-\cos2\theta=2\sin^{2}\theta$、$1+\cos2\theta=2\cos^{2}\theta$ ✓✓✓" "\n"
        r"⑥ **$\frac{a_1^{2}}{c^{2}}=\frac1{e_1^{2}}$** ✓✓✓" "\n"
        r"⑦ **数值检验**：取 $c=1$、$a_1=2$（$e_1=0.5$）、$a_2=0.5$（$e_2=2$）。" "\n"
        r"$m=2.5$、$n=1.5$。由余弦定理：$\cos2\theta=\frac{m^{2}+n^{2}-4c^{2}}{2mn}=\frac{6.25+2.25-4}{2\cdot2.5\cdot1.5}=\frac{4.5}{7.5}=0.6$。" "\n"
        r"$2\theta=53.13^\circ$，$\theta=26.565^\circ$。$\sin^{2}\theta=0.2$、$\cos^{2}\theta=0.8$。" "\n"
        r"代入 B：$\frac{0.2}{0.25}+\frac{0.8}{4}=0.8+0.2=1$ ✓✓✓ **成立**" "\n"
        r"代入 A：$\frac{0.8}{0.25}+\frac{0.2}{4}=3.2+0.05=3.25\neq1$ ✗" "\n"
        r"代入 C：$\frac{0.25}{0.8}+\frac4{0.2}=0.3125+20\neq1$ ✗" "\n"
        r"代入 D：$\frac{0.25}{0.2}+\frac4{0.8}=1.25+5\neq1$ ✗" "\n"
        r"**四选项全部验过，答案 B 确凿** ✓" "\n"
        r"**⭐⭐ 通法（共焦点椭圆双曲线）**：" "\n"
        r"① ⭐⭐ **核心公式 $\frac{\sin^{2}\theta}{e_1^{2}}+\frac{\cos^{2}\theta}{e_2^{2}}=1$（$2\theta=\angle F_1PF_2$）** —— " "\n"
        r"建议直接记住，它是本类题的总纲；记忆法：**椭圆 $e_1<1$ 配 $\sin^{2}$，双曲线 $e_2>1$ 配 $\cos^{2}$**；" "\n"
        r"② ⭐ **推导只需三步**：两定义式解出 $m=a_1+a_2$、$n=a_1-a_2$ → 余弦定理 → 半角公式；" "\n"
        r"③ ⭐ **$m,n$ 的解法很妙**：和差问题直接给 $m=a_1+a_2$、$n=a_1-a_2$，不必单独解；" "\n"
        r"④ **特款**：$\theta=\frac\pi6$（即 $2\theta=\frac\pi3$）时 $\frac{1/4}{e_1^{2}}+\frac{3/4}{e_2^{2}}=1$ ⟹ $\frac1{e_1^{2}}+\frac3{e_2^{2}}=4$（见 M-T-333-V1）；" "\n"
        r"⑤ 检验：**取一组 $(c,a_1,a_2)$ 反算 $\theta$，再代回四选项**（本题 $\frac{0.2}{0.25}+\frac{0.8}{4}=1$ ✓），是最可靠的验证。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-333'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-333-E1',
}
T333_V1 = {
    'type': '填空',
    'stem_text': (
        r"已知 $F_1,F_2$ 是椭圆和双曲线的公共焦点，$P$ 是它们的一个公共点，且 $\angle F_1PF_2=\dfrac\pi3$，"
        r"椭圆的离心率为 $e_1$，双曲线的离心率 $e_2$，则 $\dfrac1{e_1^{2}}+\dfrac3{e_2^{2}}=$ ____"
    ),
    'opts': [],
    'answer': r"$4$",
    'analysis': (
        r"由共焦点公式 $\frac{\sin^{2}\theta}{e_1^{2}}+\frac{\cos^{2}\theta}{e_2^{2}}=1$（$2\theta=\angle F_1PF_2=\frac\pi3$），"
        r"取 $\theta=\frac\pi6$ 得 $\frac{1/4}{e_1^{2}}+\frac{3/4}{e_2^{2}}=1$，两边乘 $4$ 即得。"
    ),
    'solution': (
        r"由 $\angle F_1PF_2=2\theta=\dfrac\pi3$ 得 $\theta=\dfrac\pi6$，故 $\sin^{2}\theta=\dfrac14$、$\cos^{2}\theta=\dfrac34$．" "\n"
        r"套用共焦点椭圆双曲线的核心公式（见 M-T-333-E1）" "\n"
        r"$\dfrac{\sin^{2}\theta}{e_1^{2}}+\dfrac{\cos^{2}\theta}{e_2^{2}}=1$：" "\n"
        r"$\dfrac{1/4}{e_1^{2}}+\dfrac{3/4}{e_2^{2}}=1\Rightarrow\dfrac1{4e_1^{2}}+\dfrac3{4e_2^{2}}=1$．" "\n"
        r"两边同乘 $4$：$\dfrac1{e_1^{2}}+\dfrac3{e_2^{2}}=4$．"
    ),
    'review': (
        r"★ 题干、答案完整 ✓（**详解未提取**，上述为我独立推导 —— 直接套用 M-T-333-E1 的结论）。" "\n"
        r"答案与原书标注 $4$ 一致 ✓✓✓" "\n"
        r"**独立验算（不依赖 E1，从头推一遍）**：" "\n"
        r"设 $\lvert PF_1\rvert=m$、$\lvert PF_2\rvert=n$（$m>n$），公共焦距 $2c$，椭圆长半轴 $a_1$、双曲线实半轴 $a_2$。" "\n"
        r"$m+n=2a_1$、$m-n=2a_2$ ⟹ $m=a_1+a_2$、$n=a_1-a_2$ ✓✓" "\n"
        r"余弦定理（$2\theta=\frac\pi3$，$\cos\frac\pi3=\frac12$）：$m^{2}+n^{2}-2mn\cdot\frac12=4c^{2}$ ⟹ $m^{2}+n^{2}-mn=4c^{2}$。" "\n"
        r"代入：$2(a_1^{2}+a_2^{2})-(a_1^{2}-a_2^{2})=4c^{2}$ ⟹ $a_1^{2}+3a_2^{2}=4c^{2}$ ✓✓✓" "\n"
        r"两边除以 $c^{2}$：$\frac{a_1^{2}}{c^{2}}+\frac{3a_2^{2}}{c^{2}}=4$ ⟹ $\frac1{e_1^{2}}+\frac3{e_2^{2}}=4$ ✓✓✓ **完全一致**" "\n"
        r"**数值检验**：取 $c=1$，$a_1=2$（$e_1=\frac12$）、$a_2=0.5$（$e_2=2$）。" "\n"
        r"$m=2.5$、$n=1.5$。$\cos\angle F_1PF_2=\frac{6.25+2.25-4}{2\cdot2.5\cdot1.5}=\frac{4.5}{7.5}=0.6$ ⟹ 角 $=53.13^\circ\neq60^\circ$ ✗" "\n"
        r"（该组不满足 $\angle=60^\circ$）改解：需 $a_1^{2}+3a_2^{2}=4c^{2}=4$。取 $a_2=0.5$ ⟹ $a_1^{2}=4-0.75=3.25$，$a_1=1.803$。" "\n"
        r"$e_1=\frac1{1.803}=0.5547$、$e_2=2$。$\frac1{e_1^{2}}+\frac3{e_2^{2}}=\frac1{0.3077}+\frac34=3.25+0.75=4$ ✓✓✓" "\n"
        r"验证角度：$m=1.803+0.5=2.303$、$n=1.303$。" "\n"
        r"$\cos\angle=\frac{m^{2}+n^{2}-4}{2mn}=\frac{5.304+1.698-4}{2\cdot2.303\cdot1.303}=\frac{3.002}{6.001}=0.5002$ ⟹ $60.0^\circ$ ✓✓✓ **吻合**" "\n"
        r"**答案 $4$ 正确** ✓" "\n"
        r"**⭐ 通法**：" "\n"
        r"① ⭐⭐ **本类是 M-T-333-E1 核心公式的直接代入**：$\angle F_1PF_2=2\theta$ ⟹ $\theta$ 减半，代公式，两边乘分母；" "\n"
        r"② ⭐ **$2\theta=\frac\pi3$ 时的快捷式**：$a_1^{2}+3a_2^{2}=4c^{2}$（由 $m^{2}+n^{2}-mn=4c^{2}$ 一步得）—— " "\n"
        r"比套公式还快，且不易记混；" "\n"
        r"③ ⭐ **一般地，$\angle F_1PF_2=\alpha$ 时可直接写** $2(a_1^{2}+a_2^{2})-2(a_1^{2}-a_2^{2})\cos\alpha=4c^{2}$，" "\n"
        r"记住 $m^{2}+n^{2}=2(a_1^{2}+a_2^{2})$、$mn=a_1^{2}-a_2^{2}$ 这两个展开式即可；" "\n"
        r"④ ⚠ **$\theta$ 是半角**：$\angle F_1PF_2=2\theta$ 别搞混，本题 $\frac\pi3$ 对应 $\theta=\frac\pi6$；" "\n"
        r"⑤ 检验：**先由 $a_1^{2}+3a_2^{2}=4c^{2}$ 定一组参数，再反算角度**（本题得 $60.0^\circ$ ✓），闭环确认。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-333'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-333-V1',
}

QS = [T330_E1, T330_V1, T330_V3, T332_E1, T332_V1, T332_V2, T333_E1, T333_V1]
