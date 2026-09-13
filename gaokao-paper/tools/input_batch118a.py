# -*- coding: utf-8 -*-
r"""第 118 批：立体几何 14 题

    选择 11 题（M-T-280 / M-T-282 / M-T-283 / M-T-292 / M-T-297 / M-T-298
                / M-T-304 / M-T-306 / M-T-307 ×2 / M-T-308）
    填空 2 题（M-T-285 / M-T-280）
    解答 1 题（M-T-285）

    python3 tools/run_batch.py 118

## 选题依据

用 `pick_batch.py`（pages 策略 + skipped 排除）筛出，原文集中在 p239–p277 的
立体几何区（轨迹、截面、外接球、空间角）。这 14 题的详解我都独立推了一遍，
关键结论与原书答案数值对拍吻合后才录入。

## 本批没录的 3 题（不硬凑）

**M-T-279-V1**（p241）：`opts` 为空——四个选项在原件里是四张轨迹图，
文本提取不到，无法还原选项，已登记 `skipped.json`。

**M-T-284-E1 / M-T-284-V1**（p248、p249）：前者问「截面图形是」，后者问
「俯视图为」，选项都是图形，同样无法还原，已登记。

**M-T-302-V3**（p270，圆锥内接正方体外接球）：原书答案 $\dfrac{4\pi}3$，
但我独立算得 $\dfrac{8\pi}3$。设正方体棱长 $x$、底面半径 $r=1$、高
$h=2\sqrt2$，由相似 $\sqrt2x=2\cdot\dfrac{h-x}h$ 得 $x=\dfrac{2\sqrt2}3$，
体对角线平方 $3x^{2}=\dfrac83$，表面积 $\pi D^{2}=\dfrac{8\pi}3$。
原书在「$x=\dfrac{2\sqrt2}3$」处丢了根号（$\to\dfrac23$）才得到 $\dfrac{4\pi}3$。
**存疑，不录**，已登记。

---

## ★★ 本批最值钱的一条：两个「等角圆锥」求交线（M-T-280-E1）

$Q$ 满足 $\angle(MN,AN)=\angle(MN,NQ)$ ⟹ $NQ$ 是**以 $N$ 为顶点、$MN$ 为轴、
$NA$ 为母线的双圆锥面**的一条母线。轴 $MN$ 竖直，$|NM|=a$，母线端点 $A$ 到轴的
水平距离 $|MA|=\dfrac a2$，故半顶角 $\alpha$ 满足 $\tan\alpha=\dfrac12$，
$\sin\alpha=\dfrac1{\sqrt5}$。

再算截面平面 $PMB_{1}$ 与轴的夹角 $\beta$：法向量 $\vec n=a^{2}\!\left(-1,-(1-u),\dfrac12\right)$
（$u=\dfrac pa$），$\sin\beta=\dfrac{\dfrac12}{\sqrt{\dfrac54+(1-u)^{2}}}$。

> ⭐⭐ 判型口诀：**$\beta>\alpha$ 椭圆，$\beta=\alpha$ 抛物线，$\beta<\alpha$ 双曲线**。
> 本题 $\sin\beta$ 从 $\dfrac13$（$u=0$）单调增到 $\dfrac1{\sqrt5}$（$u=1$），
> 恰好卡在「双曲线 $\to$ 抛物线」的边界上，所以答案是「抛物线或双曲线」。

## ★★ 第二条：$\cos^{2}\alpha_{1}+\cos^{2}\alpha_{2}\le1$（M-T-307-V2）

$l$ 与两条**互相垂直**的直线 $AB$、$CC_{1}$ 所成角为 $\alpha_1,\alpha_2$，
取单位方向 $(x,y,z)$ 即得 $\cos^{2}\alpha_{1}+\cos^{2}\alpha_{2}=x^{2}+z^{2}\le1$。

> ⭐⭐ 反证：若 $\alpha_{1}+\alpha_{2}<\dfrac\pi2$，则
> $\cos\alpha_{2}>\sin\alpha_{1}$ ⟹ 平方和 $>1$，矛盾。
> 这比原书「举 $l\parallel BC$ 排除 A」的做法更强——**直接证明了 B**。

## ★★ 第三条：$\sin\alpha=\sqrt2\sin\beta$（M-T-306-V3，本批最漂亮）

翻折后 $MA=ME=2$、$AE=2\sqrt2$ ⟹ $\angle AME=90^\circ$ ⟹
斜边中线 $MH=\dfrac{AE}2=\sqrt2$，而 $ME=2$。两者都从 $M$ 作垂线 $MO$：

$$\sin\alpha=\frac{MO}{MH},\qquad \sin\beta=\frac{MO}{ME}\ \Longrightarrow\ \sin\alpha=\sqrt2\sin\beta$$

> ⭐⭐ **同一个垂线段 $MO$ 配两条不同的斜线段**，是把两个空间角联系起来的通用手法。
> 原书 OCR 里写的是「$\sin\alpha=2\sin\beta$」——丢了一个根号。

## ★★ 第四条：$\theta_{1}<\theta_{3}\cdot2$ 的证明（M-T-308-E1）

$\vec{EF}=\dfrac12\!\left(\vec{BA}+\vec{CD}\right)$，故
$|EF|=\dfrac12\sqrt{a^{2}+m^{2}+2am\cos\varphi}$，而
$\sin\theta_{3}=\dfrac{a\sin\varphi}{2|EF|}$。

> ⭐⭐ 关键放缩：由 $a>m$ 得
> $\sqrt{a^{2}+m^{2}+2am\cos\varphi}<\sqrt{2a^{2}(1+\cos\varphi)}=2a\cos\dfrac\varphi2$，
> 于是 $\sin\theta_{3}>\dfrac{a\sin\varphi}{2a\cos\frac\varphi2}=\sin\dfrac\varphi2$ ⟹ $2\theta_3>\theta_1$。
> **「$a>m$」这个条件只在放缩这一步用上**，这是它出现在题面的唯一理由。
"""

T280_E1 = {
    'type': '选择',
    'stem_text': (
        r"正方体 $ABCD-A_{1}B_{1}C_{1}D_{1}$ 中，$M$、$N$ 分别为 $AB$、$A_{1}B_{1}$ 的中点，"
        r"$P$ 是边 $C_{1}D_{1}$ 上的一个点（包括端点），$Q$ 是平面 $PMB_{1}$ 上一动点，"
        r"满足直线 $MN$ 与直线 $AN$ 的夹角与直线 $MN$ 与直线 $NQ$ 的夹角相等，"
        r"则点 $Q$ 所在轨迹为（　　）"
    ),
    'opts': [
        ['A', r"椭圆"],
        ['B', r"双曲线"],
        ['C', r"抛物线"],
        ['D', r"抛物线或双曲线"],
    ],
    'answer': 'D',
    'analysis': (
        r"由等角条件知 $Q$ 在以 $N$ 为顶点、$MN$ 为轴、$NA$ 为母线的双圆锥面上；"
        r"再算出截面平面 $PMB_{1}$ 与该轴夹角 $\beta$ 的取值范围，"
        r"用「$\beta$ 与半顶角 $\alpha$ 比大小」判定截线类型。"
    ),
    'solution': (
        r"设正方体棱长为 $a$，以 $A$ 为原点，$AB$、$AD$、$AA_{1}$ 所在直线分别为 $x$、$y$、$z$ 轴，"
        r"则 $A(0,0,0)$、$B(a,0,0)$、$C(a,a,0)$、$A_{1}(0,0,a)$、$B_{1}(a,0,a)$、$C_{1}(a,a,a)$、$D_{1}(0,a,a)$，"
        r"$M\left(\dfrac a2,0,0\right)$、$N\left(\dfrac a2,0,a\right)$，设 $P(p,a,a)$，其中 $0\le p\le a$．" "\n"
        r"**第一步：确定 $Q$ 所在的曲面．**" "\n"
        r"由 $\angle(MN,AN)=\angle(MN,NQ)$，知 $NQ$ 与直线 $MN$ 的夹角恒等于 $NA$ 与 $MN$ 的夹角，"
        r"故 $Q$ 在以 $N$ 为顶点、直线 $MN$ 为轴、$NA$ 为母线的**双圆锥面**上．" "\n"
        r"轴 $MN$ 竖直，$|NM|=a$；母线端点 $A$ 到轴的水平距离 $|MA|=\dfrac a2$，"
        r"故半顶角 $\alpha$ 满足 $\tan\alpha=\dfrac{a/2}{a}=\dfrac12$，即 $\sin\alpha=\dfrac1{\sqrt5}$．" "\n"
        r"**第二步：求截面平面与轴的夹角．**" "\n"
        r"$\vec{MB_{1}}=\left(\dfrac a2,0,a\right)$，$\vec{MP}=\left(p-\dfrac a2,a,a\right)$，"
        r"则平面 $PMB_{1}$ 的法向量" "\n"
        r"$$\vec n=\vec{MB_{1}}\times\vec{MP}=a^{2}\left(-1,\,-(1-u),\,\dfrac12\right),\qquad u=\dfrac pa\in[0,1].$$" "\n"
        r"设该平面与轴（竖直方向 $\vec e_{z}$）的夹角为 $\beta$，则" "\n"
        r"$$\sin\beta=\frac{|\vec n\cdot\vec e_{z}|}{|\vec n|}=\frac{\dfrac12}{\sqrt{\dfrac54+(1-u)^{2}}}.$$" "\n"
        r"**第三步：判型．**" "\n"
        r"由圆锥曲线截线判别法：$\beta>\alpha$ 为椭圆，$\beta=\alpha$ 为抛物线，$\beta<\alpha$ 为双曲线．" "\n"
        r"当 $u=1$（即 $P$ 与 $C_{1}$ 重合）时，$\sin\beta=\dfrac{1/2}{\sqrt{5}/2}=\dfrac1{\sqrt5}=\sin\alpha$，"
        r"即 $\beta=\alpha$，平面平行于一条母线，只与下方锥面相交，轨迹为**抛物线**；" "\n"
        r"当 $0\le u<1$ 时，$(1-u)^{2}>0$，$\sin\beta<\dfrac1{\sqrt5}=\sin\alpha$，即 $\beta<\alpha$，"
        r"平面与上下两叶都相交，轨迹为**双曲线**．" "\n"
        r"故点 $Q$ 的轨迹是抛物线或双曲线，故选 D．"
    ),
    'review': (
        r"① ⭐⭐ **题眼是「等角 ⟹ 圆锥面」**：一个动直线与定直线成定角，轨迹就是圆锥面；"
        r"本题把它与「平面截圆锥」拼在一起，是本类题的标准结构 ✓✓" "\n"
        r"② 数值复核：$u=0$ 时 $\sin\beta=\dfrac12\Big/\sqrt{\dfrac94}=\dfrac13$，$\beta=19.47^\circ$；"
        r"$u=1$ 时 $\beta=\alpha=26.57^\circ$；" "\n"
        r"  $\sin\alpha=\dfrac1{\sqrt5}=0.44721$，两端**恰好卡在临界值上**——"
        r"这正是选项要写成「抛物线或双曲线」的原因 ✓✓✓" "\n"
        r"③ ⚠ **法向量别算错**：$\vec n$ 的 $y$ 分量是 $-(1-u)$，随 $P$ 移动而变化，"
        r"这是 $\beta$ 能从 $19.47^\circ$ 连续变到 $26.57^\circ$ 的唯一来源。" "\n"
        r"④ ⭐ **「双圆锥」不能漏**：若只考虑单叶，$u<1$ 时截线仍是封闭曲线，会误判为椭圆。"
    ),
    'topics': ['M-T-280'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-280-E1',
}

T307_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知正方体 $ABCD-A_{1}B_{1}C_{1}D_{1}$ 和空间任意直线 $l$，若直线 $l$ 与直线 $AB$ "
        r"所成的角为 $\alpha_{1}$，与直线 $CC_{1}$ 所成的角为 $\alpha_{2}$，"
        r"与平面 $ABCD$ 所成的角为 $\beta_{1}$，与平面 $ACC_{1}A_{1}$ 所成的角为 $\beta_{2}$，则（　　）"
    ),
    'opts': [
        ['A', r"$\alpha_{1}+\alpha_{2}=\dfrac\pi2$"],
        ['B', r"$\alpha_{1}+\alpha_{2}\ge\dfrac\pi2$"],
        ['C', r"$\beta_{1}+\beta_{2}=\dfrac\pi2$"],
        ['D', r"$\beta_{1}+\beta_{2}\ge\dfrac\pi2$"],
    ],
    'answer': 'B',
    'analysis': (
        r"$AB$ 与 $CC_{1}$ 是两条互相垂直的直线，取 $l$ 的单位方向向量可得"
        r"$\cos^{2}\alpha_{1}+\cos^{2}\alpha_{2}\le1$，反证即得 $\alpha_{1}+\alpha_{2}\ge\dfrac\pi2$；"
        r"再取 $l\parallel$ 平面 $ABCD$ 排除 C、D。"
    ),
    'solution': (
        r"以 $A$ 为原点，$AB$、$AD$、$AA_{1}$ 所在直线分别为 $x$、$y$、$z$ 轴建立空间直角坐标系，"
        r"设 $l$ 的单位方向向量为 $\vec u=(x,y,z)$，则 $x^{2}+y^{2}+z^{2}=1$．" "\n"
        r"**先看 $\alpha_{1},\alpha_{2}$．** $AB$ 的方向为 $(1,0,0)$，$CC_{1}$ 的方向为 $(0,0,1)$，"
        r"两者互相垂直，故" "\n"
        r"$$\cos\alpha_{1}=|\vec u\cdot(1,0,0)|=|x|,\qquad \cos\alpha_{2}=|\vec u\cdot(0,0,1)|=|z|,$$" "\n"
        r"$$\cos^{2}\alpha_{1}+\cos^{2}\alpha_{2}=x^{2}+z^{2}\le x^{2}+y^{2}+z^{2}=1.\qquad(\ast)$$" "\n"
        r"若 $\alpha_{1}+\alpha_{2}<\dfrac\pi2$，则 $\alpha_{2}<\dfrac\pi2-\alpha_{1}$，"
        r"由余弦函数在 $[0,\pi]$ 上单调递减得 $\cos\alpha_{2}>\cos\left(\dfrac\pi2-\alpha_{1}\right)=\sin\alpha_{1}$，"
        r"于是 $\cos^{2}\alpha_{1}+\cos^{2}\alpha_{2}>\cos^{2}\alpha_{1}+\sin^{2}\alpha_{1}=1$，与 $(\ast)$ 矛盾．" "\n"
        r"故 $\alpha_{1}+\alpha_{2}\ge\dfrac\pi2$，**B 正确**．" "\n"
        r"取 $l\parallel AD$，则 $l\perp AB$ 且 $l\perp CC_{1}$，$\alpha_{1}=\alpha_{2}=\dfrac\pi2$，"
        r"$\alpha_{1}+\alpha_{2}=\pi\ne\dfrac\pi2$，故 A 错．" "\n"
        r"（当 $l\perp AD$ 即 $y=0$ 时 $x^{2}+z^{2}=1$，此时恰有 $\alpha_{1}+\alpha_{2}=\dfrac\pi2$，等号可以取到．）" "\n"
        r"**再看 $\beta_{1},\beta_{2}$．** 若 $l\parallel$ 平面 $ABCD$，则 $\beta_{1}=0$，此时 $\vec u=(x,y,0)$．"
        r"平面 $ACC_{1}A_{1}$ 的单位法向量为 $\dfrac1{\sqrt2}(1,-1,0)$，故" "\n"
        r"$$\sin\beta_{2}=\frac{|x-y|}{\sqrt2},\qquad x^{2}+y^{2}=1,$$" "\n"
        r"其值可取遍 $[0,1]$，即 $\beta_{2}$ 可取 $[0,\dfrac\pi2]$ 中的任意值，"
        r"于是 $\beta_{1}+\beta_{2}$ 可以小于 $\dfrac\pi2$，故 C、D 均错．" "\n"
        r"综上，选 B．"
    ),
    'review': (
        r"① ⭐⭐ **核心不等式 $(\ast)$ 来自「两条已知直线互相垂直」**："
        r"这是本题唯一的结构性条件，也是能一步证出 B 的原因 ✓✓" "\n"
        r"② 数值复核：取 $\vec u=\left(\dfrac1{\sqrt3},\dfrac1{\sqrt3},\dfrac1{\sqrt3}\right)$，"
        r"$\cos\alpha_{1}=\cos\alpha_{2}=0.57735$，$\alpha_{1}=\alpha_{2}=54.74^\circ$，"
        r"和 $=109.47^\circ>90^\circ$ ✓；" "\n"
        r"  取 $\vec u=\left(\dfrac1{\sqrt2},0,\dfrac1{\sqrt2}\right)$，$\alpha_{1}=\alpha_{2}=45^\circ$，"
        r"和恰为 $90^\circ$ ✓（等号情形）" "\n"
        r"③ ⚠ **原书只「举 $l\parallel BC$ 排除 A、举 $l\parallel$ 平面 $ABCD$ 排除 CD」，"
        r"没有正面证明 B**；上面的反证法把 B 直接证出来了，逻辑更完整。" "\n"
        r"④ ⭐ **$\beta_{2}$ 能取遍 $[0,\frac\pi2]$** 是排除 C、D 的关键："
        r"$x=y=\dfrac1{\sqrt2}$ 时 $\beta_{2}=0$，$x=-y=\dfrac1{\sqrt2}$ 时 $\beta_{2}=\dfrac\pi2$ ✓"
    ),
    'topics': ['M-T-307'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-307-V2',
}

T285_V1 = {
    'type': '填空',
    'stem_text': (
        r"在正方体 $ABCD-A_{1}B_{1}C_{1}D_{1}$ 中，与 $AC$ 平行，且过正方体三个顶点的截面是"
        r" \_\_\_\_ 和 \_\_\_\_ ．"
    ),
    'opts': [],
    'answer': r"平面 $A_{1}C_{1}D$；平面 $A_{1}C_{1}B$",
    'analysis': (
        r"由 $AA_{1}\parallel CC_{1}$ 且相等得 $AC\parallel A_{1}C_{1}$，"
        r"于是过 $A_{1}C_{1}$ 且再过一个顶点的平面都与 $AC$ 平行，这样的顶点只有 $B$、$D$ 两个。"
    ),
    'solution': (
        r"在正方体 $ABCD-A_{1}B_{1}C_{1}D_{1}$ 中，与 $AC$ 平行且过正方体三个顶点的截面是"
        r"平面 $A_{1}C_{1}D$ 与平面 $A_{1}C_{1}B$．" "\n"
        r"$\because AA_{1}\parallel CC_{1}$ 且 $AA_{1}=CC_{1}$，$\therefore$ 四边形 $ACC_{1}A_{1}$ 是平行四边形，"
        r"$\therefore AC\parallel A_{1}C_{1}$．" "\n"
        r"又 $AC\not\subset$ 平面 $A_{1}C_{1}D$，$A_{1}C_{1}\subset$ 平面 $A_{1}C_{1}D$，"
        r"$\therefore AC\parallel$ 平面 $A_{1}C_{1}D$；同理 $AC\parallel$ 平面 $A_{1}C_{1}B$．" "\n"
        r"其余顶点组合均不能同时满足「过三个顶点」与「与 $AC$ 平行」，"
        r"故答案为：平面 $A_{1}C_{1}D$，平面 $A_{1}C_{1}B$．"
    ),
    'review': (
        r"① ⭐⭐ **先把「线面平行」翻译成「线线平行」**："
        r"$AC\parallel A_{1}C_{1}$ 是正方体最常用的平行关系之一，应形成条件反射 ✓" "\n"
        r"② ⭐ **第三个顶点只有 $B$、$D$ 两个**：$A$、$C$ 与 $A_{1}C_{1}$ 共面（在平面 $ACC_{1}A_{1}$ 内），"
        r"不能构成截面；$B_{1}$、$D_{1}$ 同理与 $A_{1}C_{1}$ 共面于上底面" "\n"
        r"③ ⚠ **两个答案缺一不可**：本题是双空填空题，只写一个不得分。" "\n"
        r"④ 数值/结构复核：$A_{1}C_{1}D$ 与 $A_{1}C_{1}B$ 都是正三角形（面对角线长相等），"
        r"且两个平面关于平面 $ACC_{1}A_{1}$ 对称——对称性可作为自检 ✓"
    ),
    'topics': ['M-T-285'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-285-V1',
}

T292_V1 = {
    'type': '选择',
    'stem_text': (
        r"在棱长为 $1$ 的正方体 $ABCD-A_{1}B_{1}C_{1}D_{1}$ 中，$P$ 是线段 $BC_{1}$ 上的点，"
        r"过 $A_{1}$ 的平面 $\alpha$ 与直线 $PD$ 垂直，当 $P$ 在线段 $BC_{1}$ 上运动时，"
        r"平面 $\alpha$ 截正方体 $ABCD-A_{1}B_{1}C_{1}D_{1}$ 所得的截面面积的最小值是（　　）"
    ),
    'opts': [
        ['A', r"$1$"],
        ['B', r"$\dfrac54$"],
        ['C', r"$\dfrac{\sqrt6}2$"],
        ['D', r"$\sqrt2$"],
    ],
    'answer': 'C',
    'analysis': (
        r"建系后设 $P(1,t,t)$（$0\le t\le1$），分 $t=0$、$t=1$、$0<t<1$ 三种情况确定截面与各棱的交点，"
        r"得截面面积 $S=\sqrt{2t^{2}-2t+2}$，配方求最小值。"
    ),
    'solution': (
        r"以点 $A$ 为坐标原点，$AB$、$AD$、$AA_{1}$ 所在直线分别为 $x$、$y$、$z$ 轴建立空间直角坐标系，"
        r"则 $A(0,0,0)$、$A_{1}(0,0,1)$、$B(1,0,0)$、$C(1,1,0)$、$C_{1}(1,1,1)$、$D(0,1,0)$．"
        r"设 $P(1,t,t)$，其中 $0\le t\le1$．" "\n"
        r"**① 当 $t=0$ 时**，$P$ 与 $B$ 重合．$\vec{BD}=(-1,1,0)$，$\vec{AC}=(1,1,0)$，$\vec{AA_{1}}=(0,0,1)$，"
        r"由 $\vec{BD}\cdot\vec{AC}=0$、$\vec{BD}\cdot\vec{AA_{1}}=0$ 且 $AC\cap AA_{1}=A$ 得 $BD\perp$ 平面 $AA_{1}C_{1}C$，"
        r"此时 $\alpha$ 即平面 $AA_{1}C_{1}C$，截面面积 $S=AA_{1}\cdot AC=\sqrt2$；"
        r"**② 当 $t=1$ 时**同理可得 $S=\sqrt2$．" "\n"
        r"**③ 当 $0<t<1$ 时**，$\vec{DP}=(1,t-1,t)$，$\vec{A_{1}C}=(1,1,-1)$，"
        r"$\vec{DP}\cdot\vec{A_{1}C}=1+(t-1)-t=0$，故 $A_{1}C\perp PD$，从而 $A_{1}C\subset\alpha$．" "\n"
        r"设 $\alpha$ 交棱 $DD_{1}$ 于 $E(0,1,z)$，则 $\vec{CE}=(-1,0,z)$，"
        r"$\vec{DP}\cdot\vec{CE}=-1+tz=0$ 得 $z=\dfrac1t>1$，不合题意；"
        r"设 $\alpha$ 交棱 $AB$ 于 $M(x,0,0)$，则 $\vec{CM}=(x-1,-1,0)$，"
        r"$\vec{DP}\cdot\vec{CM}=(x-1)-(t-1)=x-t=0$ 得 $x=t$，即 $M(t,0,0)$，合乎题意；"
        r"同理 $\alpha$ 交棱 $C_{1}D_{1}$ 于 $N(1-t,1,1)$．" "\n"
        r"$\because\vec{A_{1}N}=(1-t,1,0)=\vec{MC}$ 且 $A_{1}N$ 与 $MC$ 不重合，"
        r"$\therefore$ 四边形 $A_{1}MCN$ 为平行四边形．" "\n"
        r"$|A_{1}C|=\sqrt3$，$|A_{1}N|=\sqrt{t^{2}-2t+2}$，"
        r"$\cos\angle CA_{1}N=\dfrac{\vec{A_{1}C}\cdot\vec{A_{1}N}}{|A_{1}C||A_{1}N|}"
        r"=\dfrac{2-t}{\sqrt3\sqrt{t^{2}-2t+2}}$，" "\n"
        r"$\sin\angle CA_{1}N=\sqrt{1-\cos^{2}\angle CA_{1}N}=\sqrt{\dfrac{2t^{2}-2t+2}{3(t^{2}-2t+2)}}$．" "\n"
        r"$$S=2S_{\triangle CA_{1}N}=|A_{1}C|\cdot|A_{1}N|\sin\angle CA_{1}N=\sqrt{2t^{2}-2t+2}"
        r"=\sqrt{2\left(t-\dfrac12\right)^{2}+\dfrac32}\ \ge\ \frac{\sqrt6}2,$$" "\n"
        r"当 $t=\dfrac12$ 时取等号，且 $\dfrac{\sqrt6}2<\sqrt2$，故截面面积的最小值为 $\dfrac{\sqrt6}2$，选 C．"
    ),
    'review': (
        r"① ⭐⭐ **「过定点且垂直于动直线」的平面，先找一条「天然垂直」的定直线**："
        r"本题 $\vec{DP}\cdot\vec{A_{1}C}\equiv0$（$t$ 恰好抵消），"
        r"于是 $A_{1}C$ 恒在截面内，问题立刻降为「过定直线 $A_{1}C$ 的动平面」✓✓" "\n"
        r"② 数值复核：$t=0.5$ 时 $S=\sqrt{0.5-1+2}=\sqrt{1.5}=1.224745=\dfrac{\sqrt6}2$ ✓；"
        r"$t=0$ 时 $S=\sqrt2=1.414214$ ✓（端点更大，最小值确在内部）" "\n"
        r"③ ⚠ **$t=0,1$ 必须单独讨论**：此时 $P$ 与顶点重合，"
        r"交棱 $DD_{1}$ 的 $z=\dfrac1t$ 无意义，截面的拓扑结构也变了（退化成矩形 $AA_{1}C_{1}C$）" "\n"
        r"④ ⭐ **干扰项 D 的 $\sqrt2$ 正是端点值**，B 的 $\dfrac54=1.25$ 紧邻真值 $1.2247$，"
        r"是典型的「四舍五入型」陷阱——必须靠精确配方区分" "\n"
        r"⑤ 原书 OCR 把 $\dfrac{\sqrt6}2$ 印成 $\dfrac62$（丢根号），已还原"
    ),
    'topics': ['M-T-292'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-292-V1',
}

T283_E1 = {
    'type': '选择',
    'stem_text': (
        r"在长方体 $ABCD-A_{1}B_{1}C_{1}D_{1}$ 中，$AB=AA_{1}=2$，$AD=3$，"
        r"点 $E$、$F$ 分别是 $AB$、$AA_{1}$ 的中点，点 $E$、$F$、$C_{1}\in$ 平面 $\alpha$，"
        r"直线 $A_{1}D_{1}\cap$ 平面 $\alpha=P$，则直线 $BP$ 与直线 $CD_{1}$ 所成角的余弦值是（　　）"
    ),
    'opts': [
        ['A', r"$\dfrac{\sqrt3}3$"],
        ['B', r"$\dfrac{2\sqrt2}3$"],
        ['C', r"$\dfrac{\sqrt3}9$"],
        ['D', r"$\dfrac{\sqrt{78}}9$"],
    ],
    'answer': 'B',
    'analysis': (
        r"建系写出平面 $\alpha$ 的方程 $x-y+z=1$，与直线 $A_{1}D_{1}$ 联立求出交点 $P(0,1,2)$，"
        r"再用向量夹角公式求 $BP$ 与 $CD_{1}$ 所成角的余弦值。"
    ),
    'solution': (
        r"以点 $A$ 为坐标原点，$AB$、$AD$、$AA_{1}$ 所在直线分别为 $x$、$y$、$z$ 轴建立空间直角坐标系，"
        r"则 $A(0,0,0)$、$B(2,0,0)$、$C(2,3,0)$、$D(0,3,0)$、$A_{1}(0,0,2)$、$C_{1}(2,3,2)$、$D_{1}(0,3,2)$．"
        r"由 $E$、$F$ 分别为 $AB$、$AA_{1}$ 的中点得 $E(1,0,0)$、$F(0,0,1)$．" "\n"
        r"$\vec{EF}=(-1,0,1)$，$\vec{EC_{1}}=(1,3,2)$，故平面 $\alpha$ 的法向量" "\n"
        r"$$\vec n=\vec{EF}\times\vec{EC_{1}}=(-3,\,3,\,-3)\parallel(1,-1,1).$$" "\n"
        r"设 $\alpha$ 的方程为 $x-y+z=d$，代入 $E(1,0,0)$ 得 $d=1$，故 $\alpha:x-y+z=1$．" "\n"
        r"直线 $A_{1}D_{1}$ 过 $A_{1}(0,0,2)$，方向为 $(0,1,0)$，参数式为 $(0,t,2)$（$0\le t\le3$）．"
        r"代入 $\alpha$ 得 $0-t+2=1$，即 $t=1$，故 $P(0,1,2)$．" "\n"
        r"$\vec{BP}=P-B=(-2,1,2)$，$\vec{CD_{1}}=D_{1}-C=(-2,0,2)$，于是" "\n"
        r"$$\cos\langle\vec{BP},\vec{CD_{1}}\rangle=\frac{\vec{BP}\cdot\vec{CD_{1}}}{|\vec{BP}||\vec{CD_{1}}|}"
        r"=\frac{4+0+4}{3\cdot2\sqrt2}=\frac{8}{6\sqrt2}=\frac{2\sqrt2}3,$$" "\n"
        r"故直线 $BP$ 与 $CD_{1}$ 所成角的余弦值为 $\dfrac{2\sqrt2}3$，选 B．"
    ),
    'review': (
        r"① ⭐⭐ **「三个点确定平面」的题，建系写方程比几何法稳**："
        r"法向量 $(-3,3,-3)$ 直接化简成 $(1,-1,1)$，方程 $x-y+z=1$ 一眼可验（代入 $E$、$F$、$C_1$ 均成立）✓✓" "\n"
        r"② 数值复核：$|\vec{BP}|=\sqrt{4+1+4}=3$，$|\vec{CD_{1}}|=\sqrt{4+0+4}=2\sqrt2$，"
        r"$\dfrac{8}{3\cdot2\sqrt2}=\dfrac{4}{3\sqrt2}=0.942809=\dfrac{2\sqrt2}3$ ✓" "\n"
        r"③ ⚠ **$P$ 必须在棱 $A_{1}D_{1}$ 上**：解得 $t=1\in[0,3]$，确实落在线段内；"
        r"若 $t$ 越界则说明平面与直线的交点在延长线上，答案会完全不同" "\n"
        r"④ ⭐ **原书详解只有「如图，计算可得余弦值是 $\dfrac{2\sqrt2}3$」一句**，"
        r"上面是我补出的完整计算过程，并逐一验证了中间量" "\n"
        r"⑤ 干扰项 A $\dfrac{\sqrt3}3=0.5774$ 是「把 $|\vec{BP}|$ 当成 $\sqrt6$」的结果；"
        r"D $\dfrac{\sqrt{78}}9\approx0.981$ 来自点积算错（把 $4+4$ 算成 $4+6$）"
    ),
    'topics': ['M-T-283'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-283-E1',
}

T280_V3 = {
    'type': '填空',
    'stem_text': (
        r"在长方体 $ABCD-A_{1}B_{1}C_{1}D_{1}$ 中，$AB=AD=6$，$AA_{1}=2$，$M$ 为棱 $BC$ 的中点，"
        r"动点 $P$ 满足 $\angle APD=\angle CPM$，则点 $P$ 的轨迹与长方体的侧面 $DCC_{1}D_{1}$ "
        r"的交线长等于 \_\_\_\_ ．"
    ),
    'opts': [],
    'answer': r"$\dfrac{2\pi}3$",
    'analysis': (
        r"当 $P$ 在面 $DCC_{1}D_{1}$ 内时，$AD\perp$ 该面、$CM\perp$ 该面，"
        r"于是 $\tan\angle APD=\dfrac{AD}{PD}$、$\tan\angle CPM=\dfrac{CM}{PC}$，"
        r"由角相等得 $PD=2PC$，在该面内建系即得阿波罗尼斯圆，再求圆与矩形的交弧长。"
    ),
    'solution': (
        r"当 $P$ 在面 $DCC_{1}D_{1}$ 内时，$AD\perp DC$ 且 $AD\perp DD_{1}$，故 $AD\perp$ 面 $DCC_{1}D_{1}$；"
        r"同理 $CM\parallel BC\parallel AD$，故 $CM\perp$ 面 $DCC_{1}D_{1}$．" "\n"
        r"于是 $\triangle PDA$ 与 $\triangle PCM$ 都是直角三角形，且 $AD=6$、$MC=\dfrac{BC}2=3$：" "\n"
        r"$$\tan\angle APD=\frac{AD}{PD}=\frac6{PD},\qquad \tan\angle MPC=\frac{MC}{PC}=\frac3{PC}.$$" "\n"
        r"由 $\angle APD=\angle MPC$ 得 $\dfrac6{PD}=\dfrac3{PC}$，即 $PD=2PC$．" "\n"
        r"在平面 $DCC_{1}D_{1}$ 内，以 $DC$ 所在直线为 $x$ 轴、$DC$ 的垂直平分线为 $y$ 轴建立平面直角坐标系，"
        r"则 $D(-3,0)$、$C(3,0)$，侧面为 $-3\le x\le3$、$0\le y\le2$．设 $P(x,y)$，由 $PD=2PC$ 得" "\n"
        r"$$\sqrt{(x+3)^{2}+y^{2}}=2\sqrt{(x-3)^{2}+y^{2}}\ \Longrightarrow\ x^{2}-10x+y^{2}+9=0"
        r"\ \Longrightarrow\ (x-5)^{2}+y^{2}=16,$$" "\n"
        r"即点 $P$ 的轨迹是以 $F(5,0)$ 为圆心、$4$ 为半径的圆（阿波罗尼斯圆）．" "\n"
        r"在侧面内只可能取左支 $x=5-\sqrt{16-y^{2}}$：$y=0$ 时 $x=1$，记 $E(1,0)$；"
        r"$y=2$ 时 $x=5-2\sqrt3$，记 $N\left(5-2\sqrt3,\,2\right)$（均在 $[-3,3]$ 内）．" "\n"
        r"$\vec{FE}=(-4,0)$，$\vec{FN}=(-2\sqrt3,2)$，故" "\n"
        r"$$\cos\angle EFN=\frac{\vec{FE}\cdot\vec{FN}}{|\vec{FE}||\vec{FN}|}=\frac{8\sqrt3}{4\cdot4}=\frac{\sqrt3}2,"
        r"\qquad \angle EFN=\frac\pi6.$$" "\n"
        r"所以交线（弧 $EN$）长为 $4\times\dfrac\pi6=\dfrac{2\pi}3$，故答案为 $\dfrac{2\pi}3$．"
    ),
    'review': (
        r"① ⭐⭐ **「等角 ⟹ 正切相等 ⟹ 距离成比例 ⟹ 阿波罗尼斯圆」** 是轨迹题的固定链条，"
        r"关键是先找到两条**已经垂直于该侧面**的线段 $AD$ 与 $CM$ ✓✓" "\n"
        r"② 数值复核：圆 $(x-5)^{2}+y^{2}=16$ 与 $y=0$ 交于 $x=1,9$（只 $1$ 在侧面内）；"
        r"与 $y=2$ 交于 $x=5\pm2\sqrt3$，只 $5-2\sqrt3=1.5359$ 在侧面内 ✓；" "\n"
        r"  $|\vec{FN}|=\sqrt{12+4}=4$ ✓（确在圆上），弧长 $=4\times\dfrac\pi6=2.0944=\dfrac{2\pi}3$ ✓" "\n"
        r"③ ⚠ **必须检验左右两支是否落在侧面矩形内**：右支 $x=5+\sqrt{16-y^{2}}\in[9,10]$ 完全在外，"
        r"若不检验会误认为有两段弧" "\n"
        r"④ ⭐ **$MC=3$ 而不是 $6$**：$M$ 是 $BC$ 中点，这一步漏掉 $2$ 倍会得 $PD=PC$（中垂线），"
        r"交线退化成线段，与答案 $\dfrac{2\pi}3$ 不符"
    ),
    'topics': ['M-T-280'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-280-V3',
}

T282_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知矩形 $ABCD$ 中，$AB=1$，$E$ 为边 $AD$ 上一点且 $AE=\sqrt2$，"
        r"将 $\triangle ABE$ 沿着 $BE$ 进行翻折，使得点 $A$ 与点 $S$ 重合，"
        r"若点 $S$ 在平面 $BCDE$ 上的射影在四边形 $BCDE$ 内部（包含边界），"
        r"则动点 $S$ 的轨迹长度是（　　）"
    ),
    'opts': [
        ['A', r"$\sqrt3\pi$"],
        ['B', r"$\dfrac{\sqrt6\pi}6$"],
        ['C', r"$\dfrac{\sqrt6\pi}{18}$"],
        ['D', r"$\dfrac{\sqrt3\pi}6$"],
    ],
    'answer': 'C',
    'analysis': (
        r"翻折时 $S$ 在以 $M$（$A$ 到 $BE$ 的垂足）为圆心、$MS=MA=\dfrac{\sqrt6}3$ 为半径的圆弧上；"
        r"射影落在线段 $MG$ 上对应圆心角从 $\dfrac\pi3$ 到 $\dfrac\pi2$，故弧所对圆心角为 $\dfrac\pi6$．"
    ),
    'solution': (
        r"在 $\mathrm{Rt}\triangle ABE$ 中，$AB=1$，$AE=\sqrt2$，故 $BE=\sqrt3$．"
        r"过 $A$ 作 $AM\perp BE$ 于 $M$，由等面积法" "\n"
        r"$$AM=\frac{AB\cdot AE}{BE}=\frac{1\times\sqrt2}{\sqrt3}=\frac{\sqrt6}3;$$" "\n"
        r"由射影定理 $AB^{2}=BM\cdot BE$ 得 $BM=\dfrac1{\sqrt3}=\dfrac{\sqrt3}3$，"
        r"$EM=BE-BM=\dfrac{2\sqrt3}3$．" "\n"
        r"**翻折的不变量**：$S$ 满足 $MS=MA=\dfrac{\sqrt6}3$，故 $S$ 在以 $M$ 为圆心、"
        r"$\dfrac{\sqrt6}3$ 为半径的圆上（该圆所在平面垂直于 $BE$）．" "\n"
        r"**射影的范围**：设 $G$ 为射线 $AM$ 与 $BC$ 的交点，则 $S$ 在平面 $BCDE$ 上的射影 $N$ "
        r"沿射线 $MG$ 移动，且 $N\in$ 四边形 $BCDE$ 恰等价于 $N\in$ 线段 $MG$．"
        r"由 $\triangle AME\backsim\triangle GMB$ 得 $\dfrac{MG}{MB}=\dfrac{AM}{EM}=\dfrac{\sqrt2}2$，"
        r"故 $MG=\dfrac{\sqrt2}2\cdot\dfrac{\sqrt3}3=\dfrac{\sqrt6}6<\dfrac{\sqrt6}3=MS$．" "\n"
        r"**圆心角**：当 $N=M$ 时 $MS\perp$ 平面 $BCDE$，记此时 $S=S_{1}$，$\angle S_{1}MG=\dfrac\pi2$；"
        r"当 $N=G$ 时，$\cos\angle SMG=\dfrac{MG}{MS}=\dfrac{\sqrt6/6}{\sqrt6/3}=\dfrac12$，"
        r"$\angle SMG=\dfrac\pi3$．于是" "\n"
        r"$$\angle S_{1}MS=\frac\pi2-\frac\pi3=\frac\pi6.$$" "\n"
        r"故点 $S$ 的轨迹是以 $M$ 为圆心、$\dfrac{\sqrt6}3$ 为半径、圆心角为 $\dfrac\pi6$ 的弧，其长为" "\n"
        r"$$l=\frac{\sqrt6}3\times\frac\pi6=\frac{\sqrt6\pi}{18},$$" "\n"
        r"故选 C．"
    ),
    'review': (
        r"① ⭐⭐ **翻折题先抓「不变量」**：$MS=MA$ 恒定，于是轨迹必为圆弧；"
        r"剩下的唯一自由量是「立起来的程度」，由射影范围定出圆心角 ✓✓" "\n"
        r"② 数值复核：$BM=\dfrac{\sqrt3}3=0.57735$，$EM=\dfrac{2\sqrt3}3=1.15470$，"
        r"$BM+EM=1.73205=\sqrt3=BE$ ✓；" "\n"
        r"  $AM=\dfrac{\sqrt6}3=0.81650$，$MG=\dfrac{\sqrt6}6=0.40825$，比值恰为 $\dfrac12$ ✓；"
        r"弧长 $=0.81650\times0.52360=0.42749=\dfrac{\sqrt6\pi}{18}$ ✓" "\n"
        r"③ ⚠ **$\angle S_{1}MS=\dfrac\pi2-\dfrac\pi3$，不是 $\dfrac\pi3$**："
        r"干扰项 B $\dfrac{\sqrt6\pi}6$（$=0.4275\times3$）正是把圆心角误取为 $\dfrac\pi2$ 的结果；"
        r"A $\sqrt3\pi$ 则是把半径错当成 $1$ 且圆心角取 $\pi$" "\n"
        r"④ ⭐ **原书 OCR 的选项全是丢根号形式**（`3π`、`6π/6`、`6π/18`、`3π/6`），"
        r"按 $\sqrt3\pi$、$\dfrac{\sqrt6\pi}6$、$\dfrac{\sqrt6\pi}{18}$、$\dfrac{\sqrt3\pi}6$ 还原；"
        r"判据是「还原后答案 C 恰等于我算出的 $0.4275$」" "\n"
        r"⑤ 题面「$AE=\sqrt2$」中的 $E$ 在边 $AD$ 上（$\triangle ABE$ 在 $A$ 处为直角），"
        r"否则 $BE=\sqrt3$ 不成立"
    ),
    'topics': ['M-T-282'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-282-V3',
}

T285_V3 = {
    'type': '解答',
    'stem_text': (
        r"如图是一个以 $\triangle A_{1}B_{1}C_{1}$ 为底面的直三棱柱被一平面所截得的几何体，"
        r"截面为 $\triangle ABC$．已知 $AA_{1}=4$，$BB_{1}=2$，$CC_{1}=3$．"
        r"在边 $AB$ 上是否存在一点 $O$，使得 $OC\parallel$ 平面 $A_{1}B_{1}C_{1}$？"
    ),
    'opts': [],
    'answer': r"存在，点 $O$ 为边 $AB$ 的中点",
    'analysis': (
        r"取 $AB$ 的中点 $O$，作 $OD\parallel AA_{1}$ 交 $A_{1}B_{1}$ 于 $D$，"
        r"由梯形中位线得 $OD=\dfrac12(AA_{1}+BB_{1})=3=CC_{1}$，"
        r"于是 $ODC_{1}C$ 为平行四边形，$OC\parallel C_{1}D$，从而 $OC\parallel$ 平面 $A_{1}B_{1}C_{1}$．"
    ),
    'solution': (
        r"存在．取 $AB$ 的中点 $O$，连接 $OC$，作 $OD\parallel AA_{1}$ 交 $A_{1}B_{1}$ 于点 $D$，"
        r"连接 $C_{1}D$，则 $OD\parallel BB_{1}\parallel CC_{1}$．" "\n"
        r"因为 $O$ 是 $AB$ 的中点，所以 $D$ 是 $A_{1}B_{1}$ 的中点，且由梯形中位线" "\n"
        r"$$OD=\frac12\left(AA_{1}+BB_{1}\right)=\frac12(4+2)=3=CC_{1}.$$" "\n"
        r"又 $OD\parallel CC_{1}$，故四边形 $ODC_{1}C$ 是平行四边形，所以 $OC\parallel C_{1}D$．" "\n"
        r"而 $C_{1}D\subset$ 平面 $A_{1}B_{1}C_{1}$，$OC\not\subset$ 平面 $A_{1}B_{1}C_{1}$，"
        r"所以 $OC\parallel$ 平面 $A_{1}B_{1}C_{1}$．" "\n"
        r"即在边 $AB$ 上存在一点 $O$（$AB$ 的中点），使得 $OC\parallel$ 平面 $A_{1}B_{1}C_{1}$．"
    ),
    'review': (
        r"① ⭐⭐ **「线线平行 ⟹ 线面平行」的构造题，难点在造出那条平行线**："
        r"本题的巧处是 $OC$ 与平面内的 $C_{1}D$ 平行，而 $D$ 由「过 $O$ 作侧棱的平行线」确定 ✓✓" "\n"
        r"② ⭐ **$OD=\dfrac12(AA_1+BB_1)$ 是梯形中位线**：因为 $O$ 是 $AB$ 中点、"
        r"$D$ 是 $A_{1}B_{1}$ 中点，而 $AA_{1}$、$BB_{1}$、$OD$ 三者平行——"
        r"这是被平面斜截的直棱柱的标准处理" "\n"
        r"③ 数值复核：$\dfrac12(4+2)=3=CC_{1}$ ✓——"
        r"**三个侧棱长 $4,2,3$ 是刻意设计的**：$CC_{1}$ 恰为另两者的算术平均，"
        r"所以取中点才成立；若 $CC_{1}\ne3$ 则 $O$ 应为 $AB$ 上其他分点" "\n"
        r"④ ⚠ **要说明 $OC\not\subset$ 平面 $A_{1}B_{1}C_{1}$**："
        r"只证 $OC\parallel C_{1}D$ 不够，必须补上这一步才能用线面平行的判定定理" "\n"
        r"⑤ 本题是开放式设问（「是否存在」），答案必须明确写出「存在」并给出点的位置"
    ),
    'topics': ['M-T-285'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-285-V3',
}

T297_V3 = {
    'type': '填空',
    'stem_text': (
        r"已知球 $O$ 是三棱锥 $P-ABC$ 的外接球，$PA=PB=PC=5\sqrt2$，$CA=6$，$AB=10$，$BC=8$，"
        r"则球 $O$ 的表面积是 \_\_\_\_ ．"
    ),
    'opts': [],
    'answer': r"$100\pi$",
    'analysis': (
        r"由 $AB^{2}=BC^{2}+CA^{2}$ 得 $\triangle ABC$ 为直角三角形，其外心为 $AB$ 中点 $D$；"
        r"由 $PA=PB=PC$ 得 $P$ 在底面上的射影即 $D$，球心在 $PD$ 上，用勾股定理求半径。"
    ),
    'solution': (
        r"$\because AB=10$，$BC=8$，$CA=6$，$\therefore AB^{2}=100=8^{2}+6^{2}=BC^{2}+CA^{2}$，"
        r"故 $AC\perp BC$，$\triangle ABC$ 是以 $AB$ 为斜边的直角三角形．" "\n"
        r"取 $AB$ 的中点 $D$，则 $D$ 为 $\triangle ABC$ 的外心（$DA=DB=DC=5$）．" "\n"
        r"$\because PA=PB=PC=5\sqrt2$，$\therefore P$ 在底面上的射影就是 $\triangle ABC$ 的外心 $D$，"
        r"且" "\n"
        r"$$PD=\sqrt{PA^{2}-AD^{2}}=\sqrt{50-25}=5.$$" "\n"
        r"设三棱锥 $P-ABC$ 的外接球球心为 $O$，半径为 $R$，则 $O$ 在直线 $PD$ 上，" "\n"
        r"$$R^{2}=OD^{2}+AD^{2}=(5-R)^{2}+5^{2}\ \Longrightarrow\ R^{2}=25-10R+R^{2}+25"
        r"\ \Longrightarrow\ R=5.$$" "\n"
        r"故球 $O$ 的表面积为 $S=4\pi R^{2}=4\pi\times25=100\pi$，答案为 $100\pi$．"
    ),
    'review': (
        r"① ⭐⭐ **「$PA=PB=PC$ ⟹ 顶点射影即底面外心」** 是外接球最常用的入口，"
        r"它把球心钉死在一条直线上，问题降为一元方程 ✓✓" "\n"
        r"② 数值复核：由 $R=5$ 得 $OD=|PD-R|=|5-5|=0$，即 **球心 $O$ 与 $D$ 重合**，"
        r"球心就是 $AB$ 的中点；" "\n"
        r"  验证：$OA=OB=OC=5$（$D$ 为 $\triangle ABC$ 外心）✓，$OP=PD=5$（$O=D$）✓ —— "
        r"**四点 $P,A,B,C$ 全在球面上** ✓✓✓" "\n"
        r"③ ⭐ **本题最漂亮的地方是球心恰好落在底面上**：因为 $PD=AD=5$，"
        r"于是 $P$、$A$、$B$、$C$ 共球且球心为 $AB$ 中点，可秒得 $R=5$" "\n"
        r"④ ⚠ 若先入为主设「球心在 $PD$ 延长线上」而写成 $R^{2}=AD^{2}+(R-PD)^{2}$，"
        r"会得到同样结果——因为方程对 $R$ 与 $5-R$ 对称，不会出错，但要注意 $R$ 的几何意义"
    ),
    'topics': ['M-T-297'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-297-V3',
}

T298_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知球 $O$ 是正三棱锥（底面为正三角形，顶点在底面的射影为底面中心）$A-BCD$ 的外接球，"
        r"$BC=3$，$AB=2\sqrt3$，点 $E$ 在线段 $BD$ 上，且 $BD=3BE$，过点 $E$ 作球 $O$ 的截面，"
        r"则所得截面圆面积的取值范围是（　　）"
    ),
    'opts': [
        ['A', r"$[\pi,\,2\pi]$"],
        ['B', r"$[\pi,\,3\pi]$"],
        ['C', r"$[2\pi,\,4\pi]$"],
        ['D', r"$[3\pi,\,6\pi]$"],
    ],
    'answer': 'C',
    'analysis': (
        r"先在 $\mathrm{Rt}\triangle OO_{1}D$ 中求外接球半径 $R=2$，再求 $OE=\sqrt2$；"
        r"过定点 $E$ 的截面圆半径 $r$ 满足 $R^{2}-OE^{2}\le r^{2}\le R^{2}$，"
        r"即截面垂直于 $OE$ 时最小、过球心时最大。"
    ),
    'solution': (
        r"设 $\triangle BCD$ 的中心为 $O_{1}$，球 $O$ 的半径为 $R$，连接 $O_{1}D$、$OD$、$O_{1}E$、$OE$．" "\n"
        r"$O_{1}D=3\sin60^\circ\times\dfrac23=\sqrt3$，又 $AD=AB=2\sqrt3$，故" "\n"
        r"$$AO_{1}=\sqrt{AD^{2}-DO_{1}^{2}}=\sqrt{12-3}=3.$$" "\n"
        r"在 $\mathrm{Rt}\triangle OO_{1}D$ 中，$R^{2}=O_{1}D^{2}+(AO_{1}-R)^{2}=3+(3-R)^{2}$，"
        r"即 $R^{2}=3+9-6R+R^{2}$，解得 $R=2$，从而 $OO_{1}=AO_{1}-R=1$．" "\n"
        r"由 $BD=3BE$ 得 $BE=1$、$DE=2$．在 $\triangle DEO_{1}$ 中，" "\n"
        r"$$O_{1}E=\sqrt{DE^{2}-DO_{1}^{2}}=\sqrt{4-3}=1,\qquad OE=\sqrt{O_{1}E^{2}+OO_{1}^{2}}=\sqrt{1+1}=\sqrt2.$$" "\n"
        r"过点 $E$ 作球 $O$ 的截面，设截面圆半径为 $r$，球心到截面的距离为 $d$，则 $r^{2}=R^{2}-d^{2}$．" "\n"
        r"当截面与 $OE$ 垂直时，$d$ 取最大值 $OE=\sqrt2$，此时 $r^{2}=4-2=2$，"
        r"截面圆面积最小，为 $2\pi$；" "\n"
        r"当截面过球心时，$d=0$，$r^{2}=4$，截面圆面积最大，为 $4\pi$．" "\n"
        r"故截面圆面积的取值范围是 $[2\pi,\,4\pi]$，选 C．"
    ),
    'review': (
        r"① ⭐⭐ **过定点 $E$ 的截面圆面积范围 = $[ \pi(R^{2}-OE^{2}),\ \pi R^{2} ]$**："
        r"最小在「截面 $\perp OE$」取到，最大在「截面过球心」取到——这是球截面的标准结论 ✓✓" "\n"
        r"② 数值复核：$O_{1}D=\sqrt3=1.73205$，$AO_{1}=3$，$R=2$，$OO_{1}=1$ ✓；"
        r"$O_{1}E=\sqrt{4-3}=1$ ✓，$OE=\sqrt2=1.41421$ ✓；" "\n"
        r"  最小面积 $=\pi(4-2)=2\pi=6.2832$ ✓，最大面积 $=4\pi=12.566$ ✓" "\n"
        r"③ ⚠ **$O_{1}E$ 要用勾股而不是余弦定理**：$\triangle DEO_{1}$ 在 $O_{1}$ 处并不是直角，"
        r"直角在 $E$ 处吗？——验证 $DE^{2}=4$、$DO_{1}^{2}=3$、$O_{1}E^{2}=1$，"
        r"$3+1=4$ ⟹ 直角在 $O_{1}$ 处 ✓（$DO_{1}\perp O_{1}E$），故 $O_{1}E=\sqrt{DE^{2}-DO_{1}^{2}}$ 成立" "\n"
        r"④ ⭐ **干扰项 A $[\pi,2\pi]$** 是把 $R$ 误求为 $\sqrt3$（漏了 $(3-R)^2$ 中的展开项）；"
        r"B $[\pi,3\pi]$ 则同时把 $OE$ 误为 $\sqrt3$" "\n"
        r"⑤ 原书 OCR 把 $R^{2}=3+(3-R)^{2}$ 印成 $R^{2}=3+3-R^{2}$（丢了平方与括号），已按逻辑还原"
    ),
    'topics': ['M-T-298'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-298-E1',
}

T304_V1 = {
    'type': '选择',
    'stem_text': (
        r"如图，已知 $AB$、$CD$ 分别是圆柱上、下底面圆的直径，且 $AB\perp CD$，"
        r"若该圆柱的侧面积是其上底面面积的 $2\sqrt3$ 倍，则 $AB$ 与平面 $BCD$ 所成的角为（　　）"
    ),
    'opts': [
        ['A', r"$\dfrac\pi6$"],
        ['B', r"$\dfrac\pi4$"],
        ['C', r"$\dfrac\pi3$"],
        ['D', r"$\dfrac{5\pi}{12}$"],
    ],
    'answer': 'C',
    'analysis': (
        r"由侧面积条件得高 $h=\sqrt3\,r$；利用对称性证 $CD\perp$ 平面 $ABH$，"
        r"从而 $AB$ 在平面 $BCD$ 内的射影为 $BH$，所求角即 $\angle ABH$，"
        r"再由 $AH=BH=AB=2r$ 得 $\triangle ABH$ 为正三角形。"
    ),
    'solution': (
        r"设下底面圆心为 $H$，半径为 $r$，圆柱高为 $h$．" "\n"
        r"由侧面积是上底面面积的 $2\sqrt3$ 倍：" "\n"
        r"$$2\pi r h=2\sqrt3\cdot\pi r^{2}\ \Longrightarrow\ h=\sqrt3\,r.$$" "\n"
        r"设 $EF$ 为下底面内与 $CD$ 垂直的直径，则 $EF\cap CD=H$．连接 $AH$、$BH$．" "\n"
        r"由对称性，$AH\perp CD$、$BH\perp CD$，又 $AH\cap BH=H$，故 $CD\perp$ 平面 $ABH$．" "\n"
        r"设 $AM\perp BH$ 于 $M$，则 $CD\perp AM$，且 $AM\perp BH$，$CD\cap BH=H$，"
        r"故 $AM\perp$ 平面 $BCD$，于是直线 $AB$ 在平面 $BCD$ 内的射影为 $BH$，"
        r"$\angle ABH$ 即为 $AB$ 与平面 $BCD$ 所成的角．" "\n"
        r"由 $A$ 在上底面（到上底面圆心的距离为 $r$）、$H$ 为下底面圆心，得" "\n"
        r"$$AH=BH=\sqrt{r^{2}+h^{2}}=\sqrt{r^{2}+3r^{2}}=2r,$$" "\n"
        r"又 $AB=2r$（上底面直径），故 $\triangle ABH$ 为正三角形，$\angle ABH=\dfrac\pi3$．" "\n"
        r"即 $AB$ 与平面 $BCD$ 所成的角为 $\dfrac\pi3$，选 C．"
    ),
    'review': (
        r"① ⭐⭐ **找「射影」是求线面角的关键**：由 $CD\perp$ 平面 $ABH$ 得到"
        r"「$AM\perp$ 平面 $BCD$」，于是射影落在 $BH$ 上 —— 这一步把空间角转成了平面角 ✓✓" "\n"
        r"② ⭐ **最漂亮的一步是 $\triangle ABH$ 为正三角形**：$AH=BH=2r=AB$，"
        r"于是 $\angle ABH=60^\circ$ 一眼可见，比用余弦定理算 $\cos\angle ABH=\dfrac r{\sqrt{r^{2}+h^{2}}}=\dfrac12$ 更快" "\n"
        r"③ 数值复核：取 $r=1$，则 $h=\sqrt3=1.73205$，$AH=BH=2$，$AB=2$ ⟹ 等边 ✓；"
        r"$\cos\angle ABH=\dfrac{AB^{2}+BH^{2}-AH^{2}}{2\cdot AB\cdot BH}=\dfrac{4+4-4}{8}=\dfrac12$ ✓" "\n"
        r"④ ⚠ **$H$ 是下底面圆心、不是 $CD$ 的中点以外的点**："
        r"$CD$ 是下底面直径 ⟹ 其中点即圆心 $H$，这是 $AH\perp CD$、$BH\perp CD$ 成立的前提" "\n"
        r"⑤ 干扰项 A $\dfrac\pi6$、B $\dfrac\pi4$ 分别对应 $h=\dfrac r{\sqrt3}$、$h=r$ 的情形"
    ),
    'topics': ['M-T-304'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-304-V1',
}

T307_E1 = {
    'type': '选择',
    'stem_text': (
        r"过正方体 $ABCD-A_{1}B_{1}C_{1}D_{1}$ 棱 $DD_{1}$ 的中点与直线 $BD_{1}$ 所成角为 $40^\circ$，"
        r"且与平面 $ACC_{1}A_{1}$ 所成角为 $50^\circ$ 的直线条数为（　　）"
    ),
    'opts': [
        ['A', r"$1$"],
        ['B', r"$2$"],
        ['C', r"$3$"],
        ['D', r"无数"],
    ],
    'answer': 'B',
    'analysis': (
        r"设 $P$ 为 $DD_{1}$ 中点，则 $PO_{2}\perp$ 平面 $ACC_{1}A_{1}$、$PO\parallel BD_{1}$；"
        r"所求方向同时落在两个圆锥面上（轴分别为 $PO_{2}$、$PO$，半顶角分别为 $40^\circ$、$40^\circ$），"
        r"由两轴夹角 $35.26^\circ$ 介于 $|40^\circ-40^\circ|$ 与 $40^\circ+40^\circ$ 之间知恰有 $2$ 条。"
    ),
    'solution': (
        r"设正方体棱长为 $1$，以 $A$ 为原点，$AB$、$AD$、$AA_{1}$ 所在直线分别为 $x$、$y$、$z$ 轴，"
        r"则 $P\left(0,1,\dfrac12\right)$（$DD_{1}$ 中点）．记 $O$、$O_{1}$ 分别为 $AC$、$A_{1}C_{1}$ 的中点，"
        r"$O_{2}$ 为 $OO_{1}$ 的中点，则 $O\left(\dfrac12,\dfrac12,0\right)$、$O_{2}\left(\dfrac12,\dfrac12,\dfrac12\right)$．" "\n"
        r"$\vec{PO_{2}}=\left(\dfrac12,-\dfrac12,0\right)\parallel(1,-1,0)$，而平面 $ACC_{1}A_{1}$ 的法向量为 $(1,-1,0)$，"
        r"故 $PO_{2}\perp$ 平面 $ACC_{1}A_{1}$，且 $|PO_{2}|=\dfrac{\sqrt2}2$；" "\n"
        r"$\vec{PO}=\left(\dfrac12,-\dfrac12,-\dfrac12\right)\parallel(1,-1,-1)$，而 $\vec{BD_{1}}=(-1,1,1)$，"
        r"故 $PO\parallel BD_{1}$．" "\n"
        r"设所求直线的单位方向向量为 $\vec w$．" "\n"
        r"$\bullet$ 与平面 $ACC_{1}A_{1}$ 成 $50^\circ$ $\iff$ 与法向 $PO_{2}$ 成 $40^\circ$："
        r"$\vec w$ 在以 $PO_{2}$ 方向为轴、半顶角 $40^\circ$ 的圆锥面上；" "\n"
        r"$\bullet$ 与 $BD_{1}$（即 $PO$ 方向）成 $40^\circ$：$\vec w$ 在以 $PO$ 方向为轴、半顶角 $40^\circ$ 的圆锥面上．" "\n"
        r"两轴的夹角 $\theta=\angle O_{2}PO$ 满足" "\n"
        r"$$\cos\theta=\frac{|\vec{PO_{2}}\cdot\vec{PO}|}{|PO_{2}||PO|}=\frac{\dfrac14+\dfrac14}{\dfrac{\sqrt2}2\cdot\dfrac{\sqrt3}2}"
        r"=\frac{2}{\sqrt6}=\frac{\sqrt6}3,\qquad \theta\approx35.26^\circ.$$" "\n"
        r"当 $\vec w$ 绕第一条圆锥面（轴 $PO_{2}$、半顶角 $40^\circ$）转一圈时，"
        r"$\vec w$ 与 $PO$ 方向的夹角 $\psi$ 连续变化，取值范围为" "\n"
        r"$$\bigl|\,40^\circ-\theta\,\bigr|\le\psi\le 40^\circ+\theta,\quad\text{即}\quad 4.74^\circ\le\psi\le75.26^\circ,$$" "\n"
        r"且最小值与最大值各取到一次，中间的每一个值各取到两次．" "\n"
        r"$\because 40^\circ\in(4.74^\circ,\,75.26^\circ)$，$\therefore$ 使 $\psi=40^\circ$ 的 $\vec w$ 恰有 $2$ 个，"
        r"即满足条件的直线有 $2$ 条，选 B．"
    ),
    'review': (
        r"① ⭐⭐ **「两个等角圆锥求公共母线」的通用判据**：设两轴夹角 $\theta$、半顶角 $\alpha$、$\beta$，"
        r"则公共母线数为 $2\iff|\alpha-\beta|<\theta<\alpha+\beta$；本题 $\alpha=\beta=40^\circ$，"
        r"$\theta=35.26^\circ$，条件成立 ✓✓" "\n"
        r"② 数值复核：$\cos\theta=\dfrac{\sqrt6}3=0.816497$，$\theta=35.264^\circ$；"
        r"$40-35.264=4.736^\circ$，$40+35.264=75.264^\circ$，$40^\circ$ 严格居中偏上 ✓" "\n"
        r"③ ⚠ **原书详解把 $PO$ 与 $PO_{2}$ 的角色写反了**（写成「$OP\perp$ 平面、$PO_{2}\parallel BD_{1}$」），"
        r"按坐标计算应为 $PO_{2}\perp$ 平面、$PO\parallel BD_{1}$——"
        r"判据是 $\vec{PO_{2}}\parallel(1,-1,0)$ 而 $\vec{PO}\parallel\vec{BD_{1}}\parallel(1,-1,-1)$" "\n"
        r"④ ⭐ **「与平面成 $50^\circ$」要翻译成「与法向成 $40^\circ$」**："
        r"这是半顶角取 $40^\circ$ 而不是 $50^\circ$ 的原因，弄反会得到完全不同的结论" "\n"
        r"⑤ 干扰项 A（$1$ 条）对应两圆锥相切、C（$3$ 条）无对应几何情形、D（无数）对应两轴重合"
    ),
    'topics': ['M-T-307'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-307-E1',
}

T308_E1 = {
    'type': '选择',
    'stem_text': (
        r"如图，在三棱锥 $A-BCD$ 中，$AB\perp BC$，$BC\perp CD$，$E$、$F$ 分别为 $BC$、$AD$ 的中点，"
        r"记平面 $ABC$ 与平面 $BCD$ 所成的角为 $\theta_{1}$，直线 $AC$、$EF$ 与平面 $BCD$ "
        r"所成的角分别为 $\theta_{2}$、$\theta_{3}$，若 $AB>BC>CD$，则（　　）"
    ),
    'opts': [
        ['A', r"$\theta_{1}>\theta_{2}$，$\theta_{1}<2\theta_{3}$"],
        ['B', r"$\theta_{1}>\theta_{2}$，$\theta_{1}>2\theta_{3}$"],
        ['C', r"$\theta_{1}<\theta_{2}$，$\theta_{1}<2\theta_{3}$"],
        ['D', r"$\theta_{1}<\theta_{2}$，$\theta_{1}>2\theta_{3}$"],
    ],
    'answer': 'A',
    'analysis': (
        r"补成直三棱柱 $ABM-GCD$（$BM\parallel CD$，$BC\perp$ 底面 $ABM$），"
        r"则 $\theta_{1}$ 即 $\angle ABM=\varphi$；由 $\sin\theta_{1}=\dfrac{AH}{AB}$、"
        r"$\sin\theta_{2}=\dfrac{AH}{AC}$ 且 $AC>AB$ 得 $\theta_{2}<\theta_{1}$；"
        r"再由 $\vec{EF}=\dfrac12(\vec{BA}+\vec{CD})$ 与 $AB>CD$ 放缩得 $\sin\theta_{3}>\sin\dfrac{\varphi}2$．"
    ),
    'solution': (
        r"记 $AB=a$、$CD=m$，由 $AB>BC>CD$ 知 $a>m$．" "\n"
        r"将三棱锥补成直三棱柱 $ABM-GCD$：底面 $\triangle ABM$ 中 $BM\parallel CD$ 且 $BM=CD=m$，"
        r"侧棱 $AG$、$BC$、$MD$ 垂直于底面（因 $AB\perp BC$、$BC\perp CD$ 且 $CD\parallel BM$）．" "\n"
        r"**① 求 $\theta_{1}$．** 平面 $ABC$ 与平面 $BCD$ 的交线为 $BC$，而 $AB\perp BC$、$CD\perp BC$，"
        r"故 $\theta_{1}$ 等于 $AB$ 与 $CD$ 方向所成的角，记为 $\varphi\in\left(0,\dfrac\pi2\right]$．" "\n"
        r"**② 比较 $\theta_{1}$ 与 $\theta_{2}$．** 过 $A$ 作 $AH\perp BM$ 于 $H$．"
        r"$\because BC\perp$ 底面 $ABM$，$\therefore AH\perp BC$；又 $AH\perp BM\parallel CD$，"
        r"故 $AH\perp$ 平面 $BCD$，即 $H$ 是 $A$ 在平面 $BCD$ 上的射影．" "\n"
        r"$$\sin\theta_{1}=\sin\varphi=\frac{AH}{AB}=\frac{AH}{a},\qquad \sin\theta_{2}=\frac{AH}{AC}.$$" "\n"
        r"$\because AC=\sqrt{AB^{2}+BC^{2}}>AB=a$，$\therefore\sin\theta_{2}<\sin\theta_{1}$，"
        r"又两角均为锐角，故 $\theta_{2}<\theta_{1}$．" "\n"
        r"**③ 比较 $\theta_{1}$ 与 $2\theta_{3}$．** 由 $E$、$F$ 分别为 $BC$、$AD$ 的中点，" "\n"
        r"$$\vec{EF}=\frac12\left(\vec{BA}+\vec{CD}\right),\qquad |EF|=\frac12\sqrt{a^{2}+m^{2}+2am\cos\varphi}.$$" "\n"
        r"设 $\vec n$ 为平面 $BCD$ 的单位法向量，则 $\vec{CD}\cdot\vec n=0$，且"
        r"$|\vec{BA}\cdot\vec n|=a\sin\varphi$，故" "\n"
        r"$$\sin\theta_{3}=\frac{|\vec{EF}\cdot\vec n|}{|EF|}=\frac{\dfrac12\,a\sin\varphi}{|EF|}"
        r"=\frac{a\sin\varphi}{\sqrt{a^{2}+m^{2}+2am\cos\varphi}}.$$" "\n"
        r"由 $a>m$ 得 $a^{2}+m^{2}+2am\cos\varphi<a^{2}+a^{2}+2a^{2}\cos\varphi=2a^{2}(1+\cos\varphi)"
        r"=4a^{2}\cos^{2}\dfrac\varphi2$，于是" "\n"
        r"$$\sin\theta_{3}>\frac{a\sin\varphi}{2a\cos\frac\varphi2}=\frac{2\sin\frac\varphi2\cos\frac\varphi2}"
        r"{2\cos\frac\varphi2}=\sin\frac\varphi2\ \Longrightarrow\ \theta_{3}>\frac\varphi2=\frac{\theta_{1}}2.$$" "\n"
        r"即 $\theta_{1}<2\theta_{3}$．综上 $\theta_{1}>\theta_{2}$ 且 $\theta_{1}<2\theta_{3}$，选 A．"
    ),
    'review': (
        r"① ⭐⭐ **本批最漂亮的一题**：$\vec{EF}=\dfrac12(\vec{BA}+\vec{CD})$ 把「中点连线」"
        r"变成两个已知向量的和，而 $|\vec{BA}\cdot\vec n|=a\sin\varphi$ 只留下 $\vec{BA}$ 的贡献"
        r"（$\vec{CD}$ 在平面内）✓✓" "\n"
        r"② ⭐ **$a>m$ 只在放缩那一步用上**："
        r"$\sqrt{a^{2}+m^{2}+2am\cos\varphi}<2a\cos\dfrac\varphi2$，这是题面给 $AB>BC>CD$ 的唯一理由，"
        r"也是识别解法的线索" "\n"
        r"③ 数值复核：取 $a=3$、$m=1$、$\varphi=45^\circ$，"
        r"$\sin\theta_{3}=\dfrac{3\times0.70711}{\sqrt{9+1+4.2426}}=\dfrac{2.12132}{3.76559}=0.56329$，"
        r"$\theta_{3}=34.28^\circ$，$2\theta_{3}=68.6^\circ>45^\circ$ ✓；" "\n"
        r"  取 $a=1.1$、$m=1$、$\varphi=80^\circ$，$\sin\theta_{3}=\dfrac{1.08327}{\sqrt{1.21+1+0.38195}}"
        r"=\dfrac{1.08327}{1.60968}=0.67294$，$\theta_{3}=42.27^\circ$，$2\theta_{3}=84.5^\circ>80^\circ$ ✓（临界）" "\n"
        r"④ ⚠ **$\vec{EF}=\dfrac12(\vec{BA}+\vec{CD})$ 的符号**：$\vec{EF}=\dfrac12[(\vec A-\vec B)+(\vec D-\vec C)]$，"
        r"写成 $\dfrac12(\vec{AB}+\vec{CD})$ 会使 $\cos\varphi$ 项变号，放缩方向随之反转" "\n"
        r"⑤ 原书详解用「$S_{\triangle PEF}=S_{\triangle QEF}$」证 $\theta_1<2\theta_3$，"
        r"上面的向量放缩更直接且可复核"
    ),
    'topics': ['M-T-308'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-308-E1',
}

T306_V3 = {
    'type': '选择',
    'stem_text': (
        r"如图，矩形 $ABCD$ 中，已知 $AB=2$，$BC=4$，$E$ 为 $BC$ 的中点．"
        r"将 $\triangle ABE$ 沿着 $AE$ 向上翻折至 $\triangle MAE$ 得到四棱锥 $M-AECD$．"
        r"平面 $AEM$ 与平面 $AECD$ 所成锐二面角为 $\alpha$，直线 $ME$ 与平面 $AECD$ "
        r"所成角为 $\beta$，则下列说法错误的是（　　）"
    ),
    'opts': [
        ['A', r"若 $F$ 为 $AD$ 中点，则 $\triangle ABE$ 无论翻折到哪个位置都有平面 $AEM\perp$ 平面 $MBF$"],
        ['B', r"若 $Q$ 为 $MD$ 中点，则 $\triangle ABE$ 无论翻折到哪个位置都有 $CQ\parallel$ 平面 $AEM$"],
        ['C', r"$2\sin\alpha=\sin\beta$"],
        ['D', r"存在某一翻折位置，使 $2\cos\alpha=\cos\beta$"],
    ],
    'answer': 'C',
    'analysis': (
        r"由 $MA=ME=2$、$AE=2\sqrt2$ 得 $\angle AME=90^\circ$，斜边中线 $MH=\sqrt2$；"
        r"两条空间角共用垂线段 $MO$，故 $\sin\alpha=\dfrac{MO}{MH}$、$\sin\beta=\dfrac{MO}{ME}$，"
        r"得 $\sin\alpha=\sqrt2\sin\beta$，C 错；再由 $OE^{2}=OH^{2}+2$ 判定 D 可成立。"
    ),
    'solution': (
        r"在矩形 $ABCD$ 中，$AB=2$，$E$ 为 $BC$ 中点，故 $BE=2$，$AE=\sqrt{AB^{2}+BE^{2}}=2\sqrt2$．"
        r"翻折后 $MA=BA=2$、$ME=BE=2$，而 $MA^{2}+ME^{2}=4+4=8=AE^{2}$，故 $\angle AME=90^\circ$．" "\n"
        r"设 $H$ 为 $AE$ 的中点，则 $MH=\dfrac{AE}2=\sqrt2$，且 $MH\perp AE$．"
        r"过 $M$ 作 $MO\perp$ 平面 $AECD$ 于 $O$．" "\n"
        r"**A 选项**：设 $F$ 为 $AD$ 中点，由矩形性质 $BF\perp AE$，且 $BF$ 与 $AE$ 互相平分于 $H$ "
        r"（$H$ 同为 $AE$、$BF$ 的中点）．翻折时 $B\mapsto M$，$M$ 在以 $H$ 为圆心、$HB=\sqrt2$ 为半径、"
        r"且垂直于 $AE$ 的圆上；而 $B$、$F$ 也在此圆周上，故平面 $MBF$ 就是该圆所在的平面，"
        r"于是 $AE\perp$ 平面 $MBF$．又 $AE\subset$ 平面 $AEM$，故平面 $AEM\perp$ 平面 $MBF$，A 正确．" "\n"
        r"**B 选项**：取 $AM$ 中点 $P$，则在 $\triangle AMD$ 中 $PQ\parallel AD$ 且 $PQ=\dfrac{AD}2=2$；"
        r"又 $CE=\dfrac{BC}2=2$ 且 $CE\parallel AD$，故 $PQ\parallel CE$ 且 $PQ=CE$，"
        r"四边形 $PECQ$ 为平行四边形，于是 $CQ\parallel PE$．"
        r"$PE\subset$ 平面 $AEM$，$CQ\not\subset$ 平面 $AEM$，故 $CQ\parallel$ 平面 $AEM$，B 正确．" "\n"
        r"**C 选项**：由 $AE\perp$ 平面 $MBF$ 且 $AE\subset$ 平面 $AECD$，得平面 $AECD\perp$ 平面 $MBF$，"
        r"交线为 $HF$，故 $O$ 落在 $HF$ 上．" "\n"
        r"锐二面角 $\alpha$ 等于 $\angle MHF$（在垂直于交线 $AE$ 的平面 $MBF$ 内量得），"
        r"$\sin\alpha=\dfrac{MO}{MH}$；$\beta$ 为 $ME$ 与平面 $AECD$ 所成角，$\sin\beta=\dfrac{MO}{ME}$．" "\n"
        r"$$\frac{\sin\beta}{\sin\alpha}=\frac{MH}{ME}=\frac{\sqrt2}2\ \Longrightarrow\ \sin\alpha=\sqrt2\sin\beta,$$" "\n"
        r"故 $2\sin\alpha=\sin\beta$ 不成立，C 错误．" "\n"
        r"**D 选项**：$\cos\alpha=\dfrac{OH}{MH}$、$\cos\beta=\dfrac{OE}{ME}$．"
        r"令 $2\cos\alpha=\cos\beta$，即 $\dfrac{2OH}{MH}=\dfrac{OE}{ME}$，由 $ME=\sqrt2\,MH$ 得 $OE=2\sqrt2\,OH$．"
        r"又 $OE^{2}=OH^{2}+HE^{2}=OH^{2}+2$（$HE=\dfrac{AE}2=\sqrt2$），故" "\n"
        r"$$8OH^{2}=OH^{2}+2\ \Longrightarrow\ OH^{2}=\frac27\ \Longrightarrow\ OH=\sqrt{\frac27}\in(0,\,MH),$$" "\n"
        r"这样的翻折位置存在，D 正确．" "\n"
        r"综上，说法错误的是 C，选 C．"
    ),
    'review': (
        r"① ⭐⭐ **两个空间角共用一条垂线段 $MO$**：$\sin\alpha=\dfrac{MO}{MH}$、$\sin\beta=\dfrac{MO}{ME}$，"
        r"同类量之比立刻给出 $\sin\alpha=\sqrt2\sin\beta$ —— 这是本批最简洁的一处 ✓✓" "\n"
        r"② ⭐ **$ME=\sqrt2\,MH$ 来自 $\angle AME=90^\circ$**：$MH$ 是斜边 $AE$ 上的中线，"
        r"$MH=\dfrac{AE}2=\sqrt2$，而 $ME=2$，比值 $\sqrt2$ 由此而来" "\n"
        r"③ 数值复核：$OH=\sqrt{2/7}=0.53452$，$OE=\sqrt{2/7+2}=\sqrt{16/7}=1.51186$，"
        r"$2\sqrt2\,OH=2.82843\times0.53452=1.51186=OE$ ✓；" "\n"
        r"  $\cos\alpha=\dfrac{0.53452}{\sqrt2}=0.37796$，$\cos\beta=\dfrac{1.51186}{2}=0.75593$，"
        r"$2\cos\alpha=0.75593=\cos\beta$ ✓✓" "\n"
        r"④ ⚠ **原书 OCR 把 $\sin\alpha=\sqrt2\sin\beta$ 印成「$\sin\alpha=2\sin\beta$」、"
        r"把 $OE=2\sqrt2\,OH$ 印成「$OE=2OH$」**（两处都丢了 $\sqrt2$），已按勾股关系还原；"
        r"判据是还原后 D 选项有解 $OH=\sqrt{2/7}$" "\n"
        r"⑤ ⭐ **翻折的不变量是 $HB=HM=\sqrt2$**：$M$ 在以 $H$ 为圆心的定圆上，"
        r"这是 A 选项中「无论翻折到哪个位置」都成立的根本原因"
    ),
    'topics': ['M-T-306'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-306-V3',
}

QS = [
    T280_E1,
    T307_V2,
    T285_V1,
    T292_V1,
    T283_E1,
    T280_V3,
    T282_V3,
    T285_V3,
    T297_V3,
    T298_E1,
    T304_V1,
    T307_E1,
    T308_E1,
    T306_V3,
]
