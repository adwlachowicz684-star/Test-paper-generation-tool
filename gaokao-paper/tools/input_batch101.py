# -*- coding: utf-8 -*-
r"""第 101 批：立体几何解答题（平行证明 + 角与距离计算）

    python3 tools/run_batch.py 101

## 选题依据

按「详解完整 + 同题型聚堆 + 无图依赖」筛出 p284-p289 的立体几何解答题，
共 12 题，全部为解答题（证明 + 计算），集中在 M-T-312 ~ M-T-318 七个连续题型：

| 题型 | 题号 | 核心方法 |
|---|---|---|
| M-T-312 | V1, V2 | 平行四边形/中位线证线面平行；建系求二面角与线面角 |
| M-T-313 | E1 | 相似比 + 重心性质；等体积转换求体积 |
| M-T-314 | E1, V1, V2 | 面面平行证线面平行；建系求二面角与点到面距离 |
| M-T-315 | E1, V2 | 线面垂直判定；共线/平行的存在性讨论 |
| M-T-316 | V1 | 圆柱表面积；构造平行四边形证面面平行 |
| M-T-317 | E1, V1 | 正四棱锥对称性；两平面交线法证共线 |
| M-T-318 | E1 | 勾股定理逆定理证线面垂直；多面体体积比 |

> 选这批的理由：p284-p296 共 24 题待录且全为 A 级，是全书最后几个「高密
> 度且干净」的区块之一，读完 13 页可支撑两批。

## 本批最重要的三条通法

### 一、等体积转换是「求体积」题的默认起手式

M-T-312-V1 求 $V_{P-ACE}$：直接求要算 $P$ 到平面 $ACE$ 的距离，很麻烦；
换成 $V_{E-ACP}$ 后，因 $E$ 是 $PB$ 中点且 $P$ 在平面 $ACP$ 上，
$E$ 到平面 $ACP$ 的距离恰为 $B$ 到该平面距离的一半，于是

$$V_{E-ACP}=\frac12V_{B-ACP}=\frac12V_{P-ABC}=\frac12\cdot\frac13S_{\triangle ABC}\cdot PC$$

> **通法**：所求四面体的顶点若在某条线段的**中点/分点**上，优先考虑
> 「换顶点」把未知高变成已知高。

### 二、面面平行 ⟹ 线面平行，是「做平行平面法」

M-T-314-E1：分别证 $OD\parallel$ 平面 $PBC$、$OE\parallel$ 平面 $PBC$，
由 $OE\cap OD=O$ 得平面 $ODE\parallel$ 平面 $PBC$，从而 $DE\parallel$ 平面 $PBC$。

> **通法**：当**找不到**与所求直线平行的「现成直线」时，改为证明
> 「包含该直线的某个平面 ∥ 目标平面」。找这个平面的办法是：
> 从已知的中点/平行条件里凑出**两条相交直线**分别平行于目标平面。

### 三、存在性问题的两种收尾

- **算出来在范围内** ⟹ 存在（M-T-312-V2 的 $\frac{DM}{DP}=\frac14\in\left(0,1\right)$）
- **推出与已知矛盾** ⟹ 不存在（M-T-315-E1 的 $BM\parallel$ 平面 $PAD$ 只能推出 $M=C$）

> ⚠ 反证法要写清「推出的是什么」，例如 M-T-315-E1 中：平面 $PBC$ 内
> 过 $B$ 且平行于交线的直线**只有** $BC$，故 $M=C$，与「异于 $C$」矛盾。

## 三处原书答案的根号丢失（均已还原并标注）

| 题 | 原书存的 | 实际 | 判据 |
|---|---|---|---|
| M-T-313-E1 | `3/3` | $\frac{\sqrt3}3$ | 直接算得 $\frac13S\cdot h=\frac{\sqrt3}3$ |
| M-T-314-E1 | `21/7` | $\frac{\sqrt{21}}7$ | $\frac{21}7=3>1$ 不可能是余弦值 |
| M-T-314-V1 | `13/13` | $\frac{\sqrt{13}}{13}$ | $\frac{13}{13}=1$ 意味着二面角为 $0$ |
| M-T-314-V2 | `4 21/7` | $\frac{4\sqrt{21}}7$ | 按 $\frac{4\cdot21}7=12$ 超过底面尺寸 |

（本 PDF 文本层吞掉 $\sqrt{}$ 字形是老问题，本批 4 处全部由独立计算还原。）
"""

# ============================================================
# M-T-312-V1
# ============================================================
T312_V1 = {
    'type': '解答',
    'stem_text': (
        r"如图所示，在四棱锥 $P-ABCD$ 中，$PC\perp$ 底面 $ABCD$，"
        r"$AB\perp AD$，$AB\parallel CD$，$AB=2AD=2CD=2$，$E$ 是 $PB$ 的中点．" "\n"
        r"（1）求证：$CE\parallel$ 平面 $PAD$；" "\n"
        r"（2）若 $PC=2$，求三棱锥 $P-ACE$ 的体积．"
    ),
    'opts': [],
    'answer': r"（1）证明见解析；（2）$\dfrac13$",
    'analysis': (
        r"（1）取 $PA$ 的中点 $F$，连接 $EF$、$DF$，由中位线得 "
        r"$EF\parallel AB$ 且 $EF=\frac12AB$，又 $DC\parallel AB$ 且 $DC=\frac12AB$，"
        r"故 $EF\parallel CD$ 且 $EF=CD$，四边形 $EFDC$ 是平行四边形，得 $EC\parallel DF$；" "\n"
        r"（2）用等体积法 $V_{P-ACE}=V_{E-ACP}$，再由 $E$ 是 $PB$ 中点化为 $\frac12V_{P-ABC}$．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"取 $PA$ 的中点 $F$，连接 $EF$、$DF$．" "\n"
        r"因为 $E$、$F$ 分别为 $PB$、$PA$ 的中点，所以 $EF\parallel AB$ 且 $EF=\dfrac12AB$．" "\n"
        r"又 $AB=2CD$，即 $CD=\dfrac12AB$，且 $DC\parallel AB$，" "\n"
        r"所以 $EF\parallel CD$ 且 $EF=CD$，故四边形 $EFDC$ 是平行四边形，得 $EC\parallel DF$．" "\n"
        r"又 $EC\not\subset$ 平面 $PAD$，$DF\subset$ 平面 $PAD$，所以 $CE\parallel$ 平面 $PAD$．" "\n"
        r"**第（2）问**" "\n"
        r"由 $AB=2AD=2CD=2$ 得 $AB=2$，$AD=CD=1$，又 $AB\perp AD$、$AB\parallel CD$，" "\n"
        r"故底面 $ABCD$ 是直角梯形，$S_{\triangle ABC}=\dfrac12\cdot AB\cdot AD=\dfrac12\times2\times1=1$．" "\n"
        r"因 $PC\perp$ 底面 $ABCD$，所以 $V_{P-ABC}=\dfrac13S_{\triangle ABC}\cdot PC=\dfrac13\times1\times2=\dfrac23$．" "\n"
        r"由等体积法 $V_{P-ACE}=V_{E-ACP}$．" "\n"
        r"又 $P$、$E$、$B$ 三点共线且 $E$ 是 $PB$ 的中点，$P$ 在平面 $ACP$ 上，" "\n"
        r"故 $E$ 到平面 $ACP$ 的距离等于 $B$ 到平面 $ACP$ 距离的一半，" "\n"
        r"于是 $V_{E-ACP}=\dfrac12V_{B-ACP}=\dfrac12V_{P-ABC}=\dfrac12\times\dfrac23=\dfrac13$．" "\n"
        r"即 $\boxed{V_{P-ACE}=\dfrac13}$．"
    ),
    'review': (
        r"① 第（1）问的题眼是「$AB=2CD$」——它保证了 $EF=\frac12AB=CD$，"
        r"从而四边形 $EFDC$ 的一组对边**平行且相等**．若只是平行而不相等则只能得梯形，证不出 $EC\parallel DF$．" "\n"
        r"② 第（2）问的换顶点方向很关键：$V_{P-ACE}$ 中 $P$ 是高所在顶点，"
        r"换成 $V_{E-ACP}$ 后才能利用「$E$ 为中点」把距离减半．" "\n"
        r"③ 更一般的结论：**若 $E$ 在 $PB$ 上且 $PE:EB=\lambda:\left(1-\lambda\right)$，"
        r"则 $V_{E-ACP}=\left(1-\lambda\right)V_{B-ACP}$**（因 $P$ 在平面 $ACP$ 上距离为 $0$）．" "\n"
        r"④ 数值复核：$S_{\triangle ABC}=1$、$PC=2$，"
        r"$V_{P-ABC}=\frac23$，$V=\frac12\times\frac23=\frac13\approx0.3333$ ✓"
    ),
    'difficulty': 0.55,
    'topics': ['M-T-312'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-312-V1',
}

# ============================================================
# M-T-312-V2
# ============================================================
T312_V2 = {
    'type': '解答',
    'stem_text': (
        r"如图，在四棱锥 $P-ABCD$ 中，$PA\perp$ 面 $ABCD$，$AB\parallel CD$，且 "
        r"$CD=2$，$AB=1$，$BC=2\sqrt2$，$PA=1$，$AB\perp BC$，$N$ 为 $PD$ 的中点．" "\n"
        r"（1）求证：$AN\parallel$ 平面 $PBC$；" "\n"
        r"（2）求平面 $PAD$ 与平面 $PBC$ 所成二面角的余弦值；" "\n"
        r"（3）在线段 $PD$ 上是否存在一点 $M$，使得直线 $CM$ 与平面 $PBC$ 所成角的正弦值是 "
        r"$\dfrac{3\sqrt{29}}{29}$，若存在求出 $\dfrac{DM}{DP}$ 的值，若不存在说明理由．"
    ),
    'opts': [],
    'answer': r"（1）证明见解析；（2）$\dfrac23$；（3）存在，$\dfrac14$",
    'analysis': (
        r"（1）取 $CP$ 中点 $F$，证四边形 $NABF$ 是平行四边形，得 $AN\parallel BF$；" "\n"
        r"（2）以 $A$ 为原点建系，分别求两平面的法向量，用法向量夹角求二面角；" "\n"
        r"（3）设 $\dfrac{DM}{DP}=s$ 写出 $M$ 的坐标，用 $\sin\theta=\dfrac{\left|\vec{CM}\cdot\vec n\right|}{\left|\vec{CM}\right|\left|\vec n\right|}$ 列方程求解．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"取 $CP$ 中点 $F$，连接 $NF$、$BF$．" "\n"
        r"因为 $F$、$N$ 分别为 $PC$、$PD$ 的中点，所以 $NF\parallel DC$ 且 $NF=\dfrac12DC=1$．" "\n"
        r"又 $AB\parallel CD$ 且 $AB=1=\dfrac12DC$，故 $NF\parallel AB$ 且 $NF=AB$，" "\n"
        r"所以四边形 $NABF$ 是平行四边形，得 $AN\parallel BF$．" "\n"
        r"又 $AN\not\subset$ 面 $PBC$，$BF\subset$ 面 $PBC$，所以 $AN\parallel$ 平面 $PBC$．" "\n"
        r"**第（2）问**" "\n"
        r"以 $A$ 为原点，$AB$、$AD$ 方向分别为 $x$、$y$ 轴，$AP$ 方向为 $z$ 轴建系．" "\n"
        r"由 $AB\perp BC$、$AB\parallel CD$、$BC=2\sqrt2$、$CD=2$、$PA=1$ 得" "\n"
        r"$A\left(0,0,0\right)$、$B\left(1,0,0\right)$、$C\left(1,2\sqrt2,0\right)$、"
        r"$D\left(-1,2\sqrt2,0\right)$、$P\left(0,0,1\right)$．" "\n"
        r"平面 $PAD$：$\vec{AP}=\left(0,0,1\right)$，$\vec{AD}=\left(-1,2\sqrt2,0\right)$，"
        r"法向量 $\vec n_1=\vec{AP}\times\vec{AD}=\left(-2\sqrt2,-1,0\right)\sim\left(2\sqrt2,1,0\right)$．" "\n"
        r"平面 $PBC$：$\vec{BP}=\left(-1,0,1\right)$，$\vec{BC}=\left(0,2\sqrt2,0\right)$，"
        r"法向量 $\vec n_2=\vec{BP}\times\vec{BC}=\left(-2\sqrt2,0,-2\sqrt2\right)\sim\left(1,0,1\right)$．" "\n"
        r"$\cos\theta=\dfrac{\left|\vec n_1\cdot\vec n_2\right|}{\left|\vec n_1\right|\left|\vec n_2\right|}$"
        r"$=\dfrac{2\sqrt2}{3\times\sqrt2}=\dfrac23$，即所求余弦值为 $\boxed{\dfrac23}$．" "\n"
        r"**第（3）问**" "\n"
        r"设 $M$ 在 $PD$ 上且 $\dfrac{PM}{PD}=t\ \left(0\le t\le1\right)$，则 "
        r"$M=P+t\left(D-P\right)=\left(-t,\,2\sqrt2t,\,1-t\right)$．" "\n"
        r"$\vec{CM}=M-C=\left(-\left(t+1\right),\,2\sqrt2\left(t-1\right),\,1-t\right)$，取 $\vec n_2=\left(1,0,1\right)$，" "\n"
        r"$\left|\vec{CM}\cdot\vec n_2\right|=\left|-\left(t+1\right)+\left(1-t\right)\right|=2t$，" "\n"
        r"$\left|\vec{CM}\right|^2=\left(t+1\right)^2+8\left(t-1\right)^2+\left(1-t\right)^2=\left(t+1\right)^2+9\left(t-1\right)^2$．" "\n"
        r"由线面角公式 $\dfrac{2t}{\sqrt2\sqrt{\left(t+1\right)^2+9\left(t-1\right)^2}}=\dfrac3{\sqrt{29}}$，"
        r"平方得 $\dfrac{2t^2}{\left(t+1\right)^2+9\left(t-1\right)^2}=\dfrac9{29}$，" "\n"
        r"即 $58t^2=9\left(10t^2-16t+10\right)$，整理得 $16t^2-72t+45=0$，" "\n"
        r"解得 $t=\dfrac{72\pm48}{32}$，即 $t=\dfrac{15}4$（舍去，$>1$）或 $t=\dfrac34$．" "\n"
        r"于是 $\dfrac{DM}{DP}=1-t=\dfrac14$．" "\n"
        r"故存在，$M$ 满足 $\boxed{\dfrac{DM}{DP}=\dfrac14}$．"
    ),
    'review': (
        r"① 第（2）问建系时 $D$ 的 $x$ 坐标是 $-1$ 而不是 $+1$：因为 $AB\parallel CD$ 且 $CD=2>AB=1$，"
        r"梯形必须向 $A$ 的一侧伸出，**画草图确认 $D$ 在 $y$ 轴正方向一侧**．" "\n"
        r"② 二面角余弦取**绝对值**：法向量夹角可能是钝角，要看清问的是「所成二面角」还是「锐二面角」．" "\n"
        r"③ 第（3）问的参数化技巧：设 $t=\frac{PM}{PD}$（$t=0$ 在 $P$，$t=1$ 在 $D$），"
        r"则 $M=P+t\left(D-P\right)$；题目问的是 $\frac{DM}{DP}=1-t$，**务必回看问的是哪一端**．" "\n"
        r"④ 数值复核：$t=\frac34$ 时 $M=\left(-\frac34,\frac{3\sqrt2}2,\frac14\right)$，"
        r"$\vec{CM}=\left(-\frac74,-\frac{\sqrt2}2,\frac14\right)$，"
        r"$\left|\vec{CM}\cdot\vec n_2\right|=\left|-\frac74+\frac14\right|=\frac32$，"
        r"$\left|\vec{CM}\right|^2=\frac{49}{16}+\frac12+\frac1{16}=\frac{58}{16}$，" "\n"
        r"　 $\sin\theta=\dfrac{3/2}{\sqrt2\cdot\sqrt{58}/4}=\dfrac6{\sqrt{116}}=\dfrac6{2\sqrt{29}}=\dfrac3{\sqrt{29}}$ ✓"
        r"（正是题设的 $\frac{3\sqrt{29}}{29}$）" "\n"
        r"**通法（线段上动点的参数化）**：一律设 $\dfrac{PM}{PD}=t$，则 $M=P+t\left(D-P\right)$，"
        r"$\dfrac{DM}{DP}=1-t$．**先用「从 $P$ 出发」的 $t$ 列式，最后再换算成题目问的比值**，" "\n"
        r"　 可避免分子分母搞反．若直接用 $s=\frac{DM}{DP}$ 写点，则 $\left|\vec{CM}\cdot\vec n_2\right|=2\left(1-s\right)$"
        r"且 $\left|\vec{CM}\right|^2$ 也要同步改写，两处都要改，极易出错——这是本题最大的坑．"
    ),
    'difficulty': 0.7,
    'topics': ['M-T-312'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-312-V2',
}

# ============================================================
# M-T-313-E1
# ============================================================
T313_E1 = {
    'type': '解答',
    'stem_text': (
        r"如图，四棱锥 $P-ABCD$ 中，侧面 $PAD\perp$ 底面 $ABCD$，底面 $ABCD$ 为梯形，"
        r"$AB\parallel DC$，且 $AP=PD=CD=2AB=2\sqrt3$，$\angle APD=\angle ADC=60^\circ$．"
        r"$AC$ 交 $BD$ 于点 $F$，$G$ 为 $\triangle PAD$ 的重心．" "\n"
        r"（1）求证：$GF\parallel$ 平面 $PAB$；" "\n"
        r"（2）求三棱锥 $B-GFC$ 的体积．"
    ),
    'opts': [],
    'answer': r"（1）证明见解析；（2）$\dfrac{\sqrt3}3$",
    'analysis': (
        r"（1）连接 $DG$ 并延长交 $PA$ 于点 $E$，连接 $BE$．由 $AB\parallel CD$、$CD=2AB$ 得 "
        r"$\triangle ABF\backsim\triangle CDF$，故 $\dfrac{DF}{FB}=\dfrac{DC}{AB}=2$；"
        r"又 $G$ 为重心有 $\dfrac{DG}{GE}=2$，于是 $\dfrac{DF}{FB}=\dfrac{DG}{GE}$，得 $GF\parallel EB$；" "\n"
        r"（2）由已知 $\triangle PAD$ 与 $\triangle ADC$ 均为正三角形，取 $AD$ 中点 $M$ 有 $PM\perp AD$，"
        r"再由面面垂直得 $PM\perp$ 底面，从而 $V_{B-GFC}=V_{G-BFC}$，$G$ 到底面的距离为 $\dfrac13PM$．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"连接 $DG$ 并延长交 $PA$ 于点 $E$，连接 $BE$．" "\n"
        r"由底面 $ABCD$ 为梯形，$AB\parallel CD$，$CD=2AB$，得 $\triangle ABF\backsim\triangle CDF$，" "\n"
        r"故 $\dfrac{DF}{FB}=\dfrac{DC}{AB}=\dfrac21=2$．" "\n"
        r"又 $G$ 为 $\triangle PAD$ 的重心，故 $\dfrac{DG}{GE}=\dfrac21=2$．" "\n"
        r"于是 $\dfrac{DF}{FB}=\dfrac{DG}{GE}$，在 $\triangle DBE$ 中得 $GF\parallel EB$．" "\n"
        r"而 $GF\not\subset$ 平面 $PAB$，$EB\subset$ 平面 $PAB$，所以 $GF\parallel$ 平面 $PAB$．" "\n"
        r"**第（2）问**" "\n"
        r"由 $AP=PD=2\sqrt3$ 且 $\angle APD=60^\circ$，得 $AD^2=12+12-2\times12\times\dfrac12=12$，"
        r"即 $AD=2\sqrt3$，故 $\triangle PAD$ 为正三角形；" "\n"
        r"同理 $AD=DC=2\sqrt3$ 且 $\angle ADC=60^\circ$，故 $\triangle ADC$ 也是正三角形．" "\n"
        r"取 $AD$ 中点 $M$，则 $PM\perp AD$，由侧面 $PAD\perp$ 底面 $ABCD$ 得 $PM\perp$ 底面 $ABCD$，" "\n"
        r"且 $PM=\dfrac{\sqrt3}2\times2\sqrt3=3$．" "\n"
        r"因 $G$ 为 $\triangle PAD$ 的重心，故 $G$ 到底面 $ABCD$ 的距离 $=\dfrac13PM=1$．" "\n"
        r"由等体积法 $V_{B-GFC}=V_{G-BFC}=\dfrac13S_{\triangle BFC}\times1$．" "\n"
        r"在底面内以 $D$ 为原点、$DC$ 为 $x$ 轴建系，则" "\n"
        r"$D\left(0,0\right)$、$C\left(2\sqrt3,0\right)$、$A\left(\sqrt3,3\right)$、$B\left(2\sqrt3,3\right)$．" "\n"
        r"由 $\triangle ABF\backsim\triangle CDF$ 且相似比 $1:2$，得 $AF:FC=1:2$，"
        r"即 $F=A+\dfrac13\left(C-A\right)=\left(\dfrac{4\sqrt3}3,2\right)$．" "\n"
        r"于是 $\vec{BF}=\left(-\dfrac{2\sqrt3}3,-1\right)$，$\vec{BC}=\left(0,-3\right)$，" "\n"
        r"$S_{\triangle BFC}=\dfrac12\left|\vec{BF}\times\vec{BC}\right|$"
        r"$=\dfrac12\left|\left(-\dfrac{2\sqrt3}3\right)\times\left(-3\right)-\left(-1\right)\times0\right|=\sqrt3$．" "\n"
        r"故 $V_{B-GFC}=\dfrac13\times\sqrt3\times1=\dfrac{\sqrt3}3$，即 $\boxed{V_{B-GFC}=\dfrac{\sqrt3}3}$．"
    ),
    'review': (
        r"① 第（1）问的核心是**把重心条件翻译成 $\frac{DG}{GE}=2$**，再与相似比配对．"
        r"凡题中出现「重心」，第一反应就是「分中线 $2:1$」．" "\n"
        r"② 第（2）问的两个关键：一是识别出 $\triangle PAD$、$\triangle ADC$ 都是正三角形"
        r"（都满足「两边相等且夹角 $60^\circ$」），二是**重心到底面的距离是高的 $\frac13$**（不是 $\frac23$）．" "\n"
        r"③ 算 $S_{\triangle BFC}$ 最稳的是坐标法：以 $D$ 为原点，$DC$ 为 $x$ 轴建系，"
        r"$D\left(0,0\right)$、$C\left(2\sqrt3,0\right)$、$A\left(\sqrt3,3\right)$、$B\left(2\sqrt3,3\right)$，" "\n"
        r"　 由 $s=\frac13$ 得 $F\left(\dfrac{4\sqrt3}3,2\right)$，"
        r"$S_{\triangle BFC}=\dfrac12\left|\vec{BF}\times\vec{BC}\right|$"
        r"$=\dfrac12\left|\left(-\dfrac{2\sqrt3}3,-1\right)\times\left(0,-3\right)\right|=\dfrac12\times2\sqrt3=\sqrt3$ ✓" "\n"
        r"④ 数值复核：$V=\frac13\times\sqrt3\times1=\frac{\sqrt3}3\approx0.5774$ ✓" "\n"
        r"**通法（面面垂直 ⟹ 线面垂直）**：在两个互相垂直的平面中，"
        r"若一个平面内有一条直线**垂直于交线**，则该直线垂直于另一个平面．"
        r"本题 $PM\perp AD$（交线）且 $PM\subset$ 侧面 $PAD$，故 $PM\perp$ 底面．"
    ),
    'difficulty': 0.7,
    'topics': ['M-T-313'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-313-E1',
}

# ============================================================
# M-T-314-E1
# ============================================================
T314_E1 = {
    'type': '解答',
    'stem_text': (
        r"如图，$C$，$D$ 分别是以 $AB$ 为直径的半圆 $O$ 上的点，满足 "
        r"$\overset{\frown}{BC}=\overset{\frown}{CD}=\overset{\frown}{DA}$，"
        r"$\triangle PAB$ 为等边三角形，且与半圆 $O$ 所成二面角的大小为 $90^\circ$，$E$ 为 $PA$ 的中点．" "\n"
        r"（1）求证：$DE\parallel$ 平面 $PBC$；" "\n"
        r"（2）求二面角 $A-BE-D$ 的余弦值．"
    ),
    'opts': [],
    'answer': r"（1）证明见解析；（2）$\dfrac{\sqrt{21}}7$",
    'analysis': (
        r"（1）由等弧得 $\angle AOD=\angle DOC=\angle COB=60^\circ$，"
        r"于是 $\triangle AOD$、$\triangle DOC$、$\triangle COB$ 均为正三角形，"
        r"四边形 $OBCD$ 是菱形，得 $OD\parallel BC$；又 $OE$ 是 $\triangle PAB$ 的中位线得 $OE\parallel PB$；"
        r"由 $OE\cap OD=O$ 得平面 $ODE\parallel$ 平面 $PBC$，从而 $DE\parallel$ 平面 $PBC$；" "\n"
        r"（2）建系用向量法求二面角 $A-BE-D$ 的余弦值．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"由 $\overset{\frown}{BC}=\overset{\frown}{CD}=\overset{\frown}{DA}$ 得 "
        r"$\angle AOD=\angle DOC=\angle COB=60^\circ$，" "\n"
        r"故 $\triangle AOD$、$\triangle DOC$、$\triangle COB$ 都是正三角形，" "\n"
        r"于是 $OB=BC=CD=OD$，四边形 $OBCD$ 是菱形，得 $OD\parallel BC$．" "\n"
        r"因 $OD\not\subset$ 平面 $PBC$，$BC\subset$ 平面 $PBC$，故 $OD\parallel$ 平面 $PBC$．" "\n"
        r"又 $E$ 是 $PA$ 的中点，$O$ 是 $AB$ 的中点，故 $OE$ 是 $\triangle PAB$ 的中位线，$OE\parallel PB$，" "\n"
        r"同理得 $OE\parallel$ 平面 $PBC$．" "\n"
        r"由 $OE\cap OD=O$，得平面 $ODE\parallel$ 平面 $PBC$，又 $DE\subset$ 平面 $ODE$，" "\n"
        r"所以 $DE\parallel$ 平面 $PBC$．" "\n"
        r"**第（2）问**" "\n"
        r"设半圆半径为 $R$，以 $O$ 为原点，$OB$ 为 $x$ 轴，半圆所在平面为 $xOy$ 面建系，"
        r"则 $A\left(-R,0,0\right)$、$B\left(R,0,0\right)$，" "\n"
        r"$D\left(-\dfrac R2,\dfrac{\sqrt3R}2,0\right)$、$C\left(\dfrac R2,\dfrac{\sqrt3R}2,0\right)$．" "\n"
        r"因 $\triangle PAB$ 为等边三角形且与半圆所在平面垂直，$P$ 在 $AB$ 的中垂线上，" "\n"
        r"取 $P\left(0,0,\sqrt3R\right)$（高为 $\dfrac{\sqrt3}2\times2R=\sqrt3R$）．" "\n"
        r"$E$ 为 $PA$ 中点，故 $E\left(-\dfrac R2,0,\dfrac{\sqrt3R}2\right)$．" "\n"
        r"平面 $ABE$：$A$、$B$ 在 $x$ 轴上，$E$ 在 $y=0$ 平面内，故平面 $ABE$ 即 $xOz$ 面，"
        r"法向量 $\vec n_1=\left(0,1,0\right)$．" "\n"
        r"平面 $BED$：$\vec{BE}=\left(-\dfrac{3R}2,0,\dfrac{\sqrt3R}2\right)$，"
        r"$\vec{BD}=\left(-\dfrac{3R}2,\dfrac{\sqrt3R}2,0\right)$，" "\n"
        r"$\vec n_2=\vec{BE}\times\vec{BD}\sim\left(1,\sqrt3,\sqrt3\right)$．" "\n"
        r"$\cos\theta=\dfrac{\left|\vec n_1\cdot\vec n_2\right|}{\left|\vec n_1\right|\left|\vec n_2\right|}$"
        r"$=\dfrac{\sqrt3}{1\times\sqrt{1+3+3}}=\dfrac{\sqrt3}{\sqrt7}=\dfrac{\sqrt{21}}7$．" "\n"
        r"即所求余弦值为 $\boxed{\dfrac{\sqrt{21}}7}$．"
    ),
    'review': (
        r"① 第（1）问是「做平行平面法」的教科书式范例：**找不到与 $DE$ 平行的现成直线**，"
        r"就证 $DE$ 所在的平面 $ODE\parallel$ 平面 $PBC$．凑这个平面的办法是从已知的中点、等弧条件里"
        r"找两条相交直线（$OE$、$OD$）分别平行于目标平面．" "\n"
        r"② 「$\triangle PAB$ 与半圆所成二面角为 $90^\circ$」等价于**平面 $PAB\perp$ 半圆所在平面**，"
        r"于是 $P$ 必在 $AB$ 的中垂面内，坐标为 $\left(0,0,\sqrt3R\right)$（或其相反数）．" "\n"
        r"③ 第（2）问中平面 $ABE$ 恰好是坐标平面 $xOz$，法向量直接取 $\left(0,1,0\right)$——"
        r"**先观察平面是否为坐标面，可省掉一次叉乘**．" "\n"
        r"④ 结果与 $R$ 无关，说明半径可任取（取 $R=1$ 或 $R=2$ 都一样），这是自检信号．" "\n"
        r"⑤ 数值复核：$\frac{\sqrt3}{\sqrt7}=\frac{1.7320508}{2.6457513}=0.6546537$，"
        r"$\frac{\sqrt{21}}7=\frac{4.5825757}7=0.6546537$ ✓ 完全一致"
    ),
    'difficulty': 0.72,
    'topics': ['M-T-314'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-314-E1',
}

# ============================================================
# M-T-314-V1
# ============================================================
T314_V1 = {
    'type': '解答',
    'stem_text': (
        r"在四棱锥 $P-ABCD$ 中，$BC=BD=DC=2\sqrt3$，$AD=AB=PD=PB=2$．" "\n"
        r"（1）若 $E$ 为 $PC$ 的中点，求证：$BE\parallel$ 平面 $PAD$；" "\n"
        r"（2）当平面 $PBD\perp$ 平面 $ABCD$ 时，求二面角 $C-PD-B$ 的余弦值．"
    ),
    'opts': [],
    'answer': r"（1）证明见解析；（2）$\dfrac{\sqrt{13}}{13}$",
    'analysis': (
        r"（1）取 $CD$ 的中点 $M$，连接 $EM$、$BM$．由 $\triangle BCD$ 为正三角形得 $BM\perp CD$，"
        r"结合 $AD=AB=2$、$BD=2\sqrt3$ 可算出 $\angle ADB=30^\circ$、$\angle ADC=90^\circ$，故 $BM\parallel AD$；"
        r"又 $EM$ 是 $\triangle PCD$ 的中位线得 $EM\parallel PD$；于是平面 $BEM\parallel$ 平面 $PAD$；" "\n"
        r"（2）建系用向量法求二面角 $C-PD-B$ 的余弦值．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"取 $CD$ 的中点 $M$，连接 $EM$、$BM$．" "\n"
        r"由 $BC=BD=DC=2\sqrt3$ 得 $\triangle BCD$ 为正三角形，故 $BM\perp CD$．" "\n"
        r"在 $\triangle ABD$ 中，$AD=AB=2$，$BD=2\sqrt3$，" "\n"
        r"$\cos\angle ADB=\dfrac{AD^2+BD^2-AB^2}{2\cdot AD\cdot BD}=\dfrac{4+12-4}{2\times2\times2\sqrt3}=\dfrac{\sqrt3}2$，"
        r"故 $\angle ADB=30^\circ$．" "\n"
        r"又 $\angle BDC=60^\circ$，故 $\angle ADC=30^\circ+60^\circ=90^\circ$，即 $AD\perp DC$．" "\n"
        r"而 $BM\perp CD$，所以 $BM\parallel AD$，又 $BM\not\subset$ 平面 $PAD$，故 $BM\parallel$ 平面 $PAD$．" "\n"
        r"因 $E$、$M$ 分别为 $PC$、$CD$ 的中点，$EM$ 是 $\triangle PCD$ 的中位线，故 $EM\parallel PD$，"
        r"同理 $EM\parallel$ 平面 $PAD$．" "\n"
        r"由 $EM\cap BM=M$，得平面 $BEM\parallel$ 平面 $PAD$，又 $BE\subset$ 平面 $BEM$，"
        r"所以 $BE\parallel$ 平面 $PAD$．" "\n"
        r"**第（2）问**" "\n"
        r"以 $D$ 为原点，$DC$ 为 $x$ 轴，$DA$ 为 $y$ 轴建系，则" "\n"
        r"$D\left(0,0,0\right)$、$C\left(2\sqrt3,0,0\right)$、$A\left(0,2,0\right)$、$B\left(\sqrt3,3,0\right)$．" "\n"
        r"取 $BD$ 中点 $N\left(\dfrac{\sqrt3}2,\dfrac32,0\right)$，$\left|BD\right|=2\sqrt3$，"
        r"由 $PB=PD=2$ 得 $\triangle PBD$ 的高 $=\sqrt{2^2-\left(\sqrt3\right)^2}=1$．" "\n"
        r"因平面 $PBD\perp$ 平面 $ABCD$，故 $P$ 在过 $N$ 且垂直于 $BD$ 的竖直平面内，"
        r"取 $P\left(\dfrac{\sqrt3}2,\dfrac32,1\right)$．" "\n"
        r"平面 $PDB$：$\vec{DB}=\left(\sqrt3,3,0\right)$，$\vec{DP}=\left(\dfrac{\sqrt3}2,\dfrac32,1\right)$，"
        r"$\vec n_1=\vec{DB}\times\vec{DP}\sim\left(\sqrt3,-1,0\right)$．" "\n"
        r"平面 $PDC$：$\vec{DC}=\left(2\sqrt3,0,0\right)$，$\vec{DP}=\left(\dfrac{\sqrt3}2,\dfrac32,1\right)$，"
        r"$\vec n_2=\vec{DC}\times\vec{DP}\sim\left(0,-2,3\right)$．" "\n"
        r"$\cos\theta=\dfrac{\left|\vec n_1\cdot\vec n_2\right|}{\left|\vec n_1\right|\left|\vec n_2\right|}$"
        r"$=\dfrac{2}{2\times\sqrt{13}}=\dfrac1{\sqrt{13}}=\dfrac{\sqrt{13}}{13}$．" "\n"
        r"即所求余弦值为 $\boxed{\dfrac{\sqrt{13}}{13}}$．"
    ),
    'review': (
        r"① 第（1）问的关键计算是 $\cos\angle ADB=\frac{\sqrt3}2$ ⟹ $\angle ADB=30^\circ$，"
        r"再由 $\angle BDC=60^\circ$ 得 $\angle ADC=90^\circ$．**这一步推出 $AD\perp DC$ 后才能说 $BM\parallel AD$**，" "\n"
        r"　 因为 $BM\perp CD$ 只说明 $BM$ 与 $CD$ 垂直，要得 $BM\parallel AD$ 必须知道 $AD\perp CD$（同一条垂线的两条垂线平行）．" "\n"
        r"② 第（2）问中 $P$ 的坐标：因平面 $PBD\perp$ 底面，$P$ 在 $BD$ 的**中垂面**内且该中垂面垂直于底面，"
        r"所以 $P$ 的 $x,y$ 就是 $BD$ 中点 $N$ 的坐标，$z$ 取高 $1$．" "\n"
        r"③ 注意 $\triangle PBD$ 的高用勾股：半底 $\sqrt3$，腰 $2$，高 $=\sqrt{4-3}=1$．" "\n"
        r"④ 数值复核：$\frac1{\sqrt{13}}=0.2773501$，$\frac{\sqrt{13}}{13}=\frac{3.6055513}{13}=0.2773501$ ✓" "\n"
        r"**通法（等腰三角形的高）**：已知腰长 $l$ 与底 $2d$，则高 $=\sqrt{l^2-d^2}$，"
        r"且高的垂足就是底边中点——这正是「平面 $PBD\perp$ 底面」时能直接写出 $P$ 的 $x,y$ 坐标的原因．"
    ),
    'difficulty': 0.72,
    'topics': ['M-T-314'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-314-V1',
}

# ============================================================
# M-T-314-V2
# ============================================================
T314_V2 = {
    'type': '解答',
    'stem_text': (
        r"如图所示的四棱锥 $P-ABCD$ 的底面 $ABCD$ 是一个等腰梯形，$AD\parallel BC$，且 "
        r"$AD=2AB=2BC=4$，$PO$ 是 $\triangle PAD$ 的中线，点 $E$ 是棱 $PD$ 的中点．" "\n"
        r"（1）证明：$CE\parallel$ 平面 $PAB$；" "\n"
        r"（2）若平面 $PAD\perp$ 平面 $ABCD$，且 $PA=PD$，$PO=AO$，求平面 $PAB$ 与平面 $PCD$ 夹角的余弦值；" "\n"
        r"（3）在（2）条件下，求点 $D$ 到平面 $PAB$ 的距离．"
    ),
    'opts': [],
    'answer': r"（1）证明见解析；（2）$\dfrac17$；（3）$\dfrac{4\sqrt{21}}7$",
    'analysis': (
        r"（1）连接 $OC$、$OE$，由中位线得 $OE\parallel PA$、由平行四边形 $ABCO$ 得 $CO\parallel AB$，"
        r"于是平面 $OCE\parallel$ 平面 $PAB$；" "\n"
        r"（2）取 $BC$ 中点 $M$，证 $PO\perp$ 底面，以 $O$ 为原点建系求两平面法向量；" "\n"
        r"（3）用等体积法 $V_{P-ABD}=V_{D-PAB}$ 求距离．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"连接 $OC$、$OE$．由 $O$、$E$ 分别是 $AD$、$PD$ 的中点，得 $OE\parallel PA$；" "\n"
        r"又 $OE\not\subset$ 平面 $PAB$，$PA\subset$ 平面 $PAB$，故 $OE\parallel$ 平面 $PAB$．" "\n"
        r"由 $AD\parallel BC$ 且 $AD=4$、$BC=2$，得 $AO=2=BC$ 且 $AO\parallel BC$，"
        r"故四边形 $ABCO$ 是平行四边形，$CO\parallel AB$，同理 $CO\parallel$ 平面 $PAB$．" "\n"
        r"由 $CO\cap OE=O$，得平面 $OCE\parallel$ 平面 $PAB$，又 $CE\subset$ 平面 $OCE$，"
        r"所以 $CE\parallel$ 平面 $PAB$．" "\n"
        r"**第（2）问**" "\n"
        r"由 $PA=PD$ 且 $O$ 为 $AD$ 中点，得 $PO\perp AD$；又平面 $PAD\perp$ 平面 $ABCD$，"
        r"故 $PO\perp$ 底面 $ABCD$．" "\n"
        r"由 $AD=4$ 得 $AO=2$，又 $PO=AO=2$．" "\n"
        r"等腰梯形中 $AB=2$，$BC=2$，$AD=4$，高 $=\sqrt{2^2-1^2}=\sqrt3$．" "\n"
        r"以 $O$ 为原点，$OM$（$M$ 为 $BC$ 中点）、$OD$、$OP$ 方向为 $x$、$y$、$z$ 轴建系，则" "\n"
        r"$A\left(0,-2,0\right)$、$D\left(0,2,0\right)$、$B\left(\sqrt3,-1,0\right)$、"
        r"$C\left(\sqrt3,1,0\right)$、$P\left(0,0,2\right)$．" "\n"
        r"平面 $PAB$：$\vec{AP}=\left(0,2,2\right)$，$\vec{AB}=\left(\sqrt3,1,0\right)$，"
        r"$\vec n_1=\vec{AP}\times\vec{AB}\sim\left(1,-\sqrt3,\sqrt3\right)$．" "\n"
        r"平面 $PCD$：$\vec{DP}=\left(0,-2,2\right)$，$\vec{DC}=\left(\sqrt3,-1,0\right)$，"
        r"$\vec n_2=\vec{DP}\times\vec{DC}\sim\left(1,\sqrt3,\sqrt3\right)$．" "\n"
        r"$\cos\theta=\dfrac{\left|\vec n_1\cdot\vec n_2\right|}{\left|\vec n_1\right|\left|\vec n_2\right|}$"
        r"$=\dfrac{\left|1-3+3\right|}{\sqrt7\times\sqrt7}=\dfrac17$．" "\n"
        r"即所求余弦值为 $\boxed{\dfrac17}$．" "\n"
        r"**第（3）问**" "\n"
        r"平面 $PAB$ 的方程为 $x-\sqrt3\left(y+2\right)+\sqrt3z=0$，即 $x-\sqrt3y+\sqrt3z-2\sqrt3=0$．" "\n"
        r"点 $D\left(0,2,0\right)$ 到该平面的距离" "\n"
        r"$d=\dfrac{\left|0-\sqrt3\times2+0-2\sqrt3\right|}{\sqrt{1+3+3}}$"
        r"$=\dfrac{4\sqrt3}{\sqrt7}=\dfrac{4\sqrt{21}}7$．" "\n"
        r"即 $\boxed{d=\dfrac{4\sqrt{21}}7}$．"
    ),
    'review': (
        r"① 第（1）问中「$AD=2BC$」保证了 $AO=BC$，从而 $ABCO$ 是平行四边形（一组对边平行且相等）．"
        r"**若 $AD\ne2BC$，则 $CO$ 不平行 $AB$，第（1）问就不成立**——这说明题设数据是配套的．" "\n"
        r"② 第（2）问的建系：$O$ 为原点，$x$ 轴取 $OM$ 而非 $OA$，这样 $B$、$C$ 的 $x$ 坐标都是 $\sqrt3$（梯形的高）．" "\n"
        r"③ $\cos\theta=\frac17$ 是个很小的余弦值（夹角约 $81.8^\circ$），"
        r"**注意分子 $1-3+3=1$ 是三个项的和，不能算错符号**．" "\n"
        r"④ 第（3）问既可用点到平面距离公式，也可用等体积法 $V_{P-ABD}=V_{D-PAB}$；"
        r"**点到平面距离公式更快**，但要先把平面方程写对（注意常数项 $-2\sqrt3$ 来自代入点 $A$）．" "\n"
        r"⑤ 数值复核：$\frac{4\sqrt3}{\sqrt7}=\frac{6.9282032}{2.6457513}=2.618$? "
        r"实际 $\frac{4\sqrt3}{\sqrt7}=2.618$ 而 $\frac{4\sqrt{21}}7=\frac{18.33}7=2.618$ ✓ 一致" "\n"
        r"**通法（点到平面距离）**：求出法向量 $\vec n$ 后，平面方程为 "
        r"$n_x\left(x-x_0\right)+n_y\left(y-y_0\right)+n_z\left(z-z_0\right)=0$，"
        r"再代入点坐标取绝对值除以 $\left|\vec n\right|$．"
    ),
    'difficulty': 0.75,
    'topics': ['M-T-314'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-314-V2',
}

# ============================================================
# M-T-315-E1
# ============================================================
T315_E1 = {
    'type': '解答',
    'stem_text': (
        r"在四棱锥 $P-ABCD$ 中，底面 $ABCD$ 是菱形，$AC\cap BD=O$．" "\n"
        r"（I）若 $AC\perp PD$，求证：$AC\perp$ 平面 $PBD$；" "\n"
        r"（II）若平面 $PAC\perp$ 平面 $ABCD$，求证：$PB=PD$；" "\n"
        r"（III）在棱 $PC$ 上是否存在点 $M$（异于点 $C$）使得 $BM\parallel$ 平面 $PAD$，"
        r"若存在，求 $\dfrac{PM}{PC}$ 的值；若不存在，说明理由．"
    ),
    'opts': [],
    'answer': r"（I）证明见解析；（II）证明见解析；（III）不存在",
    'analysis': (
        r"（I）由菱形得 $AC\perp BD$，结合 $AC\perp PD$，由线面垂直的判定定理即得；" "\n"
        r"（II）由面面垂直的性质得 $PO\perp$ 底面，再由 $BO=DO$ 得 $PB=PD$；" "\n"
        r"（III）用反证法：由 $BM\parallel$ 平面 $PAD$ 可推出平面 $PBD\parallel$ 平面 $PAD$，矛盾．"
    ),
    'solution': (
        r"**第（I）问**" "\n"
        r"因为 $ABCD$ 是菱形，所以 $AC\perp BD$．" "\n"
        r"又已知 $AC\perp PD$，而 $BD$ 与 $PD$ 是平面 $PBD$ 内的两条相交直线，" "\n"
        r"由线面垂直的判定定理得 $AC\perp$ 平面 $PBD$．" "\n"
        r"**第（II）问**" "\n"
        r"平面 $PAC\cap$ 平面 $ABCD=AC$，且平面 $PAC\perp$ 平面 $ABCD$．" "\n"
        r"在平面 $PAC$ 内作 $PO'\perp AC$ 于 $O'$，由面面垂直的性质定理得 $PO'\perp$ 平面 $ABCD$，"
        r"故 $PO'\perp BD$．" "\n"
        r"又 $ABCD$ 是菱形，$AC\perp BD$．" "\n"
        r"由 $AC\cap PO'=O'$ 且 $AC$、$PO'\subset$ 平面 $PAC$，得 $BD\perp$ 平面 $PAC$．" "\n"
        r"于是 $BD\perp PO$（其中 $O=AC\cap BD$，$PO\subset$ 平面 $PAC$）．" "\n"
        r"又 $O$ 为菱形对角线交点，$OB=OD$，即 $PO$ 是线段 $BD$ 的垂直平分线，" "\n"
        r"故 $PB=PD$．" "\n"
        r"**第（III）问**" "\n"
        r"不存在，理由如下．" "\n"
        r"底面 $ABCD$ 是菱形，故 $AD\parallel BC$；又 $BC\not\subset$ 平面 $PAD$、$AD\subset$ 平面 $PAD$，"
        r"所以 $BC\parallel$ 平面 $PAD$．" "\n"
        r"设平面 $PBC\cap$ 平面 $PAD=l$，则 $l$ 过点 $P$ 且 $l\parallel BC$．" "\n"
        r"假设存在 $M\in PC$（$M\ne C$）使 $BM\parallel$ 平面 $PAD$．" "\n"
        r"因 $BM\subset$ 平面 $PBC$，故 $BM\parallel l$．" "\n"
        r"在平面 $PBC$ 内，过 $B$ 且平行于 $l$ 的直线唯一；而 $BC\parallel l$ 且 $BC$ 过 $B$，"
        r"故该直线就是 $BC$，即 $M$ 为直线 $BC$ 与 $PC$ 的交点，只能是 $M=C$．" "\n"
        r"这与 $M\ne C$ 矛盾，故不存在这样的点 $M$．"
    ),
    'review': (
        r"① 第（I）问是**线面垂直判定定理的直接套用**，关键是把 $BD$、$PD$ 说成「平面 $PBD$ 内两条**相交**直线」——"
        r"若只说「两条直线」而不验证相交，得分点会丢．" "\n"
        r"② 第（II）问的标准流程：**面面垂直 ⟹ 作交线的垂线 ⟹ 线面垂直**．"
        r"这里「在平面 $PAC$ 内作 $AC$ 的垂线」，垂足正是 $O$（因为 $\triangle PAC$ 中 $PO\perp AC$）．" "\n"
        r"③ 第（III）问是**反证法 + 唯一性**：平面 $PBC$ 内过 $B$ 且平行于 $l$ 的直线只有一条，"
        r"而 $BC$ 正好满足，于是 $M$ 被逼到 $C$．这类「存在性」题的结论常常是「不存在」，"
        r"**判据是看动点被约束到区间的端点**．" "\n"
        r"④ 注意 $BC\parallel$ 平面 $PAD$ 这一步：它同时给出「交线 $l\parallel BC$」，"
        r"是后面唯一性论证的前提．" "\n"
        r"**通法（棱上动点的存在性）**：设动点在棱 $PC$ 上，先看端点 $P$、$C$ 处的极端情形，"
        r"若只有端点满足而题目要求「异于端点」，则答案为「不存在」——本题 $M=P$ 时 $BM=BP$（不平行），"
        r"$M=C$ 时 $BM=BC\parallel$ 平面 $PAD$，故仅端点 $C$ 满足，被题目排除．"
    ),
    'difficulty': 0.68,
    'topics': ['M-T-315'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-315-E1',
}

# ============================================================
# M-T-315-V2
# ============================================================
T315_V2 = {
    'type': '解答',
    'stem_text': (
        r"如图，矩形 $ADEF$ 和菱形 $ABCD$ 所在平面互相垂直，已知 $\angle ADC=\dfrac\pi3$，"
        r"点 $N$ 是线段 $AD$ 的中点．" "\n"
        r"（1）求证：$CN\perp AF$；" "\n"
        r"（2）试问在线段 $BE$ 上是否存在点 $M$，使得直线 $AF\parallel$ 平面 $MNC$？"
        r"若存在，请证明 $AF\parallel$ 平面 $MNC$，并求出 $\dfrac{BM}{ME}$ 的值；若不存在，请说明理由．"
    ),
    'opts': [],
    'answer': r"（1）证明见解析；（2）存在，$AF\parallel$ 平面 $MNC$，$\dfrac{BM}{ME}=2$",
    'analysis': (
        r"（1）由 $\angle ADC=\frac\pi3$ 且 $AD=DC$ 得 $\triangle ADC$ 是等边三角形，$N$ 为 $AD$ 中点故 $CN\perp AD$，"
        r"再由面面垂直的性质得 $CN\perp$ 平面 $ADEF$；" "\n"
        r"（2）取 $EF$ 的中点 $P$，由 $NP\parallel AF$ 且 $PE\parallel BC$，"
        r"连接 $CP$ 交 $BE$ 于 $M$，由 $\triangle PEM\backsim\triangle CBM$ 得 $\frac{BM}{ME}=\frac{BC}{PE}=2$．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"在菱形 $ABCD$ 中 $AD=DC$，又 $\angle ADC=\dfrac\pi3$，故 $\triangle ADC$ 是等边三角形．" "\n"
        r"因 $N$ 是 $AD$ 的中点，所以 $CN\perp AD$．" "\n"
        r"又平面 $ABCD\perp$ 平面 $ADEF$，交线为 $AD$，且 $CN\subset$ 平面 $ABCD$、$CN\perp AD$，" "\n"
        r"由面面垂直的性质定理得 $CN\perp$ 平面 $ADEF$．" "\n"
        r"又 $AF\subset$ 平面 $ADEF$，故 $CN\perp AF$．" "\n"
        r"**第（2）问**" "\n"
        r"存在．取 $EF$ 的中点 $P$，连接 $NP$、$CP$，设 $CP$ 交 $BE$ 于点 $M$．" "\n"
        r"在矩形 $ADEF$ 中 $AD\parallel EF$ 且 $AD=EF$，$N$、$P$ 分别为 $AD$、$EF$ 的中点，" "\n"
        r"故 $AN\parallel FP$ 且 $AN=FP$，四边形 $ANPF$ 是平行四边形，得 $NP\parallel AF$．" "\n"
        r"因 $M\in CP$，故平面 $MNC$ 就是平面 $CNP$，于是 $NP\subset$ 平面 $MNC$；" "\n"
        r"又 $AF\not\subset$ 平面 $MNC$，所以 $AF\parallel$ 平面 $MNC$．" "\n"
        r"再求比值：由 $AD\parallel BC$（菱形）与 $AD\parallel EF$ 得 $PE\parallel BC$，" "\n"
        r"故 $\triangle PEM\backsim\triangle CBM$，$\dfrac{BM}{ME}=\dfrac{BC}{PE}$．" "\n"
        r"设菱形边长为 $a$，则 $BC=a$，$AD=a$，$EF=a$，$PE=\dfrac a2$，" "\n"
        r"于是 $\dfrac{BM}{ME}=\dfrac a{a/2}=2$．" "\n"
        r"即存在这样的 $M$（$M$ 为 $BE$ 上靠近 $E$ 的三等分点），$\boxed{\dfrac{BM}{ME}=2}$．"
    ),
    'review': (
        r"① 第（1）问的题眼是「$\angle ADC=\frac\pi3$ + 菱形」⟹ $\triangle ADC$ 等边 ⟹ $CN\perp AD$．"
        r"**凡菱形中出现 $60^\circ$ 角，第一反应就是把它拆成两个等边三角形**．" "\n"
        r"② 第（2）问的关键构造是**取 $EF$ 中点 $P$**：它同时给出 $NP\parallel AF$（用于证平行）"
        r"和 $PE=\frac a2$（用于算比值），一个点起两个作用．" "\n"
        r"③ 「$M\in CP$ ⟹ 平面 $MNC$ = 平面 $CNP$」这个观察很重要："
        r"它把「$M$ 在 $CP$ 上」与「$AF\parallel$ 平面 $MNC$」联系起来．" "\n"
        r"④ 比值 $\frac{BC}{PE}=\frac a{a/2}=2$ 与 $a$ 无关，说明结果与菱形边长无关，可作自检．" "\n"
        r"**通法（面面垂直 ⟹ 线面垂直 ⟹ 线线垂直）**：本题完整链条是 "
        r"「等边三角形 ⟹ $CN\perp AD$」→「面面垂直 + $CN\perp$ 交线 ⟹ $CN\perp$ 平面 $ADEF$」"
        r"→「$CN$ 垂直于平面内任意直线 ⟹ $CN\perp AF$」．"
    ),
    'difficulty': 0.7,
    'topics': ['M-T-315'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-315-V2',
}

# ============================================================
# M-T-316-V1
# ============================================================
T316_V1 = {
    'type': '解答',
    'stem_text': (
        r"（2022·广西·昭平中学高一期末）如图，在圆柱 $O_1O_2$ 中，$AB$、$CD$ 分别是上、下底面圆的直径，"
        r"且 $AB\parallel CD$，$EF$、$GH$ 分别是圆柱轴截面上的母线．" "\n"
        r"（1）若 $CE=DE=2\sqrt6$，圆柱的母线长等于底面圆的直径，求圆柱的表面积；" "\n"
        r"（2）证明：平面 $ABH\parallel$ 平面 $ECD$．"
    ),
    'opts': [],
    'answer': r"（1）$24\pi$；（2）证明见详解",
    'analysis': (
        r"（1）借助母线垂直于底面构造直角三角形，由 $CE=DE$ 推出 $E$ 在上底面与 $CD$ 垂直的直径端点上，"
        r"再由勾股定理求半径，进而得表面积；" "\n"
        r"（2）由 $AB\parallel CD$ 得 $AB\parallel$ 平面 $ECD$，再证 $AH\parallel ED$，由面面平行的判定定理得证．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"设底面圆半径为 $r$，母线长（即圆柱的高）为 $h$，由已知 $h=2r$．" "\n"
        r"以 $O_2$ 为原点，$CD$ 所在直线为 $x$ 轴，轴线为 $z$ 轴建系，则" "\n"
        r"$C\left(r,0,0\right)$、$D\left(-r,0,0\right)$、$O_1\left(0,0,h\right)$．" "\n"
        r"设 $E\left(r\cos\varphi,r\sin\varphi,h\right)$（$E$ 在上底面圆周上），则" "\n"
        r"$CE^2=\left(r\cos\varphi-r\right)^2+r^2\sin^2\varphi+h^2=2r^2-2r^2\cos\varphi+h^2$，" "\n"
        r"$DE^2=\left(r\cos\varphi+r\right)^2+r^2\sin^2\varphi+h^2=2r^2+2r^2\cos\varphi+h^2$．" "\n"
        r"由 $CE=DE$ 得 $\cos\varphi=0$，即 $\varphi=\pm\dfrac\pi2$，故 $E\left(0,\pm r,h\right)$，"
        r"且 $CE^2=2r^2+h^2=\left(2\sqrt6\right)^2=24$．" "\n"
        r"代入 $h=2r$ 得 $2r^2+4r^2=6r^2=24$，故 $r=2$，$h=4$．" "\n"
        r"$S=2\pi r^2+2\pi rh=2\pi\times4+2\pi\times2\times4=8\pi+16\pi=24\pi$．" "\n"
        r"即圆柱的表面积为 $\boxed{24\pi}$．" "\n"
        r"**第（2）问**" "\n"
        r"由（1）可取 $E\left(0,r,h\right)$、$F\left(0,r,0\right)$．" "\n"
        r"因 $EF$、$GH$ 是同一轴截面内的两条母线，故 $G\left(0,-r,h\right)$、$H\left(0,-r,0\right)$．" "\n"
        r"① $AB\parallel CD$（已知），$CD\subset$ 平面 $ECD$，$AB\not\subset$ 平面 $ECD$，"
        r"故 $AB\parallel$ 平面 $ECD$．" "\n"
        r"② $\vec{AH}=H-A=\left(0-r,\,-r-0,\,0-h\right)=\left(-r,-r,-h\right)$，" "\n"
        r"　 $\vec{ED}=D-E=\left(-r-0,\,0-r,\,0-h\right)=\left(-r,-r,-h\right)$，" "\n"
        r"　 故 $\vec{AH}=\vec{ED}$，即 $AH\parallel ED$；又 $ED\subset$ 平面 $ECD$、$AH\not\subset$ 平面 $ECD$，"
        r"故 $AH\parallel$ 平面 $ECD$．" "\n"
        r"③ $AB\cap AH=A$，由面面平行的判定定理得 $\boxed{\text{平面 }ABH\parallel\text{ 平面 }ECD}$．"
    ),
    'review': (
        r"① 第（1）问的关键一步是**由 $CE=DE$ 推出 $\cos\varphi=0$**："
        r"$CE^2$ 与 $DE^2$ 只差一项 $\mp2r^2\cos\varphi$，令其相等即得 $\cos\varphi=0$．"
        r"这比「$E$ 在 $CD$ 的中垂面上」的说法更可直接算出数值．" "\n"
        r"② 「母线长等于底面圆的直径」即 $h=2r$，代入后 $CE^2=6r^2=24$ 一步得 $r=2$，非常干净．" "\n"
        r"③ 第（2）问最漂亮的一步是 $\vec{AH}=\vec{ED}=\left(-r,-r,-h\right)$："
        r"**两条线段的方向向量恰好相同**，说明 $AHED$ 构成平行四边形，比分别证平行更简洁．" "\n"
        r"④ ⚠ 图中 $H$ 的位置依赖「$EF$、$GH$ 在同一轴截面内」这一理解；"
        r"若 $GH$ 在另一个轴截面内，则 $\vec{AH}$ 的 $y$ 分量会变，命题未必成立．已在解中注明．" "\n"
        r"⑤ 数值复核：$r=2$、$h=4$ 时 $CE=\sqrt{2\times4+16}=\sqrt{24}=2\sqrt6$ ✓；"
        r"$S=8\pi+16\pi=24\pi\approx75.3982$ ✓" "\n"
        r"**通法（圆柱中的距离）**：把下底面圆心设为原点、直径所在直线为 $x$ 轴，"
        r"上底面点写成 $\left(r\cos\varphi,r\sin\varphi,h\right)$，距离平方必为 "
        r"$2r^2\mp2r^2\cos\varphi+h^2$——**记住这个式子可以省掉每次重新展开**．"
    ),
    'difficulty': 0.62,
    'topics': ['M-T-316'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-316-V1',
}

# ============================================================
# M-T-317-E1
# ============================================================
T317_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知正四棱锥 $S-ABCD$ 的各条棱长都相等，且点 $E$、$F$ 分别是 $SB$、$SD$ 的中点．" "\n"
        r"（1）求证：$AC\perp SB$；" "\n"
        r"（2）在 $SC$ 上是否存在点 $M$，使平面 $MBD\parallel$ 平面 $AEF$，若存在，求出 $\dfrac{SM}{MC}$ 的值；"
        r"若不存在，说明理由．"
    ),
    'opts': [],
    'answer': r"（1）见解析；（2）存在，$\dfrac{SM}{MC}=2$",
    'analysis': (
        r"（1）设 $AC\cap BD=O$，连 $SO$，由正四棱锥性质得 $SO\perp$ 底面，故 $SO\perp AC$；"
        r"又 $BD\perp AC$，于是 $AC\perp$ 平面 $SBD$，从而 $AC\perp SB$；" "\n"
        r"（2）注意到 $EF\parallel BD$，只需在平面 $SAC$ 内找到 $OM\parallel AK$（$K$ 为 $SO$ 中点）的位置，"
        r"由相似比定出 $M$．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"设 $AC\cap BD=O$，连接 $SO$．由正四棱锥的性质，$SO\perp$ 平面 $ABCD$，故 $SO\perp AC$．" "\n"
        r"又 $ABCD$ 是正方形，$BD\perp AC$．" "\n"
        r"由 $SO\cap BD=O$，$SO$、$BD\subset$ 平面 $SBD$，得 $AC\perp$ 平面 $SBD$．" "\n"
        r"又 $SB\subset$ 平面 $SBD$，故 $AC\perp SB$．" "\n"
        r"**第（2）问**" "\n"
        r"存在．设棱长为 $a$，则 $OA=\dfrac{a}{\sqrt2}$．" "\n"
        r"在 $\mathrm{Rt}\triangle SOA$ 中 $SA=a$、$OA=\dfrac a{\sqrt2}$，"
        r"故 $SO=\sqrt{a^2-\dfrac{a^2}2}=\dfrac a{\sqrt2}$．" "\n"
        r"考虑平面 $SAC$（$A$、$C$、$S$、$O$、$M$ 都在此平面内）．" "\n"
        r"在 $\triangle SBD$ 中，$E$、$F$ 为 $SB$、$SD$ 的中点，故 $EF\parallel BD$，"
        r"且 $EF$ 的中点为 $SO$ 的中点，记 $K=\dfrac{S+O}2$，则 $K\in EF$．" "\n"
        r"于是 平面 $AEF\cap$ 平面 $SAC=AK$；又 $O\in BD$、$M\in SC$，"
        r"平面 $MBD\cap$ 平面 $SAC=OM$．" "\n"
        r"由 平面 $MBD\parallel$ 平面 $AEF$ 得 $OM\parallel AK$．" "\n"
        r"在平面 $SAC$ 内以 $O$ 为原点、$OC$ 为 $x$ 轴建系，则" "\n"
        r"$A\left(-\dfrac a{\sqrt2},0\right)$、$C\left(\dfrac a{\sqrt2},0\right)$、$S\left(0,\dfrac a{\sqrt2}\right)$、" "\n"
        r"$K\left(0,\dfrac a{2\sqrt2}\right)$，故 $\vec{AK}=\left(\dfrac a{\sqrt2},\dfrac a{2\sqrt2}\right)$，方向比 $x:y=1:\dfrac12$．" "\n"
        r"设 $\dfrac{SM}{SC}=t$，则 $M=S+t\left(C-S\right)=\left(\dfrac{ta}{\sqrt2},\dfrac{a\left(1-t\right)}{\sqrt2}\right)$，" "\n"
        r"$\vec{OM}$ 的方向比 $x:y=t:\left(1-t\right)$．" "\n"
        r"由 $OM\parallel AK$ 得 $\dfrac t1=\dfrac{1-t}{1/2}$，即 $t=2\left(1-t\right)$，解得 $t=\dfrac23$．" "\n"
        r"于是 $\dfrac{SM}{MC}=\dfrac t{1-t}=\dfrac{2/3}{1/3}=2$．" "\n"
        r"即存在，$M$ 满足 $\boxed{\dfrac{SM}{MC}=2}$．"
    ),
    'review': (
        r"① 第（1）问是正四棱锥的**标准结论**：$AC\perp$ 平面 $SBD$．"
        r"只要看到「正四棱锥 + $AC$、$SB$」，几乎都要走这条线．" "\n"
        r"② 第（2）问最巧妙的一步是**把面面平行翻译成平面 $SAC$ 内的线线平行 $OM\parallel AK$**．"
        r"这样三维问题降为二维，用一个相似比就解出来了．" "\n"
        r"③ 确定 $K$ 是 $SO$ 中点的理由：$E$、$F$ 是 $SB$、$SD$ 的中点，"
        r"故 $EF$ 的中点 $=\frac{E+F}2=\frac{2S+B+D}4=\frac{S+O}2$（因 $B+D=2O$）——"
        r"**用向量算中点比画图快**．" "\n"
        r"④ 数值复核：取 $a=\sqrt2$，则 $OA=1$、$SO=1$，$A\left(-1,0\right)$、$S\left(0,1\right)$、$C\left(1,0\right)$、" "\n"
        r"　 $K\left(0,0.5\right)$，$\vec{AK}=\left(1,0.5\right)$；$t=\frac23$ 时 $M\left(\frac23,\frac13\right)$，"
        r"$\vec{OM}=\left(\frac23,\frac13\right)$，恰为 $\frac23\vec{AK}$ ✓ 平行成立" "\n"
        r"**通法（平面截平行平面）**：两个平行平面被第三个平面所截，**交线必平行**．"
        r"凡遇到「面面平行」求点的位置，优先找一条同时与两平面相交的「辅助平面」，"
        r"把问题化到该平面内做．"
    ),
    'difficulty': 0.72,
    'topics': ['M-T-317'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-317-E1',
}

# ============================================================
# M-T-317-V1
# ============================================================
T317_V1 = {
    'type': '解答',
    'stem_text': (
        r"（2020·全国·高一课时练习）在正方体 $AC_1$ 中，$E$、$F$ 分别为 $D_1C_1$、$B_1C_1$ 的中点，"
        r"$AC\cap BD=P$，$A_1C_1\cap EF=Q$，如图．" "\n"
        r"（1）若 $A_1C$ 交平面 $EFBD$ 于点 $R$，证明：$P$、$Q$、$R$ 三点共线；" "\n"
        r"（2）线段 $AC$ 上是否存在点 $M$，使得平面 $B_1D_1M\parallel$ 平面 $EFBD$，"
        r"若存在确定 $M$ 的位置，若不存在说明理由．"
    ),
    'opts': [],
    'answer': r"（1）证明见解析；（2）存在，$M$ 为 $AP$ 中点",
    'analysis': (
        r"（1）证明 $P$、$Q$、$R$ 是平面 $EFBD$ 与平面 $ACC_1A_1$ 的公共点，由公理 3 即得；" "\n"
        r"（2）取 $AD$ 中点 $G$、$AB$ 中点 $H$，连 $GH$ 交 $AC$ 于 $M$，"
        r"可证 $M$ 为 $AP$ 中点，且两平面法向量相同．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"记平面 $\alpha=$ 平面 $EFBD$，平面 $\beta=$ 平面 $ACC_1A_1$．" "\n"
        r"① $P=AC\cap BD$：$BD\subset\alpha$，又 $AC\subset\beta$，故 $P\in\alpha$ 且 $P\in\beta$；" "\n"
        r"② $Q=A_1C_1\cap EF$：$EF\subset\alpha$，$A_1C_1\subset\beta$，故 $Q\in\alpha$ 且 $Q\in\beta$；" "\n"
        r"③ $R=A_1C\cap\alpha$：$A_1C\subset\beta$，故 $R\in\beta$，又由定义 $R\in\alpha$．" "\n"
        r"于是 $P$、$Q$、$R$ 都是平面 $\alpha$ 与 $\beta$ 的公共点．" "\n"
        r"由公理 3，两相交平面的公共点都在其交线上，故 $P$、$Q$、$R$ 三点共线．" "\n"
        r"**第（2）问**" "\n"
        r"存在，$M$ 为 $AP$ 的中点．" "\n"
        r"以 $A$ 为原点，$AB$、$AD$、$AA_1$ 为 $x$、$y$、$z$ 轴，设棱长为 $1$，则" "\n"
        r"$A\left(0,0,0\right)$、$B\left(1,0,0\right)$、$D\left(0,1,0\right)$、$P\left(\dfrac12,\dfrac12,0\right)$、" "\n"
        r"$B_1\left(1,0,1\right)$、$D_1\left(0,1,1\right)$、$E\left(\dfrac12,1,1\right)$、$F\left(1,\dfrac12,1\right)$．" "\n"
        r"取 $M$ 为 $AP$ 中点，即 $M\left(\dfrac14,\dfrac14,0\right)$．" "\n"
        r"平面 $EFBD$：$\vec{BD}=\left(-1,1,0\right)$，$\vec{BE}=\left(-\dfrac12,1,1\right)$，" "\n"
        r"$\vec n=\vec{BD}\times\vec{BE}=\left(1,1,-\dfrac12\right)\sim\left(2,2,-1\right)$．" "\n"
        r"平面 $B_1D_1M$：$\vec{B_1D_1}=\left(-1,1,0\right)$，$\vec{B_1M}=\left(-\dfrac34,\dfrac14,-1\right)$，" "\n"
        r"$\vec n'=\vec{B_1D_1}\times\vec{B_1M}=\left(-1,-1,\dfrac12\right)\sim\left(2,2,-1\right)$．" "\n"
        r"故 $\vec n\parallel\vec n'$，两平面平行．" "\n"
        r"又 $M\left(\dfrac14,\dfrac14,0\right)$ 代入平面 $EFBD$ 的方程 $2x+2y-z=2$ 得 $1\ne2$，"
        r"即 $M\notin$ 平面 $EFBD$，故两平面平行而不重合．" "\n"
        r"几何作法：取 $AD$ 中点 $G$、$AB$ 中点 $H$，连 $GH$ 交 $AC$ 于 $M$，"
        r"由 $GH$ 是 $\triangle ABD$ 的中位线可算得 $M$ 为 $AP$ 中点．" "\n"
        r"即 $\boxed{M\text{ 为 }AP\text{ 的中点}}$．"
    ),
    'review': (
        r"① 第（1）问是**公理 3 的典型应用**：要证三点共线，就证它们都是「两个平面的公共点」．"
        r"找这两个平面的办法是——其中一点是「两线交点」，另一点是「线与面交点」．" "\n"
        r"② 第（2）问用坐标法最稳：$\vec n=\left(2,2,-1\right)$ 与 $\vec n'=\left(2,2,-1\right)$ 完全相同，"
        r"**法向量相同是本类题最硬的证据**．" "\n"
        r"③ 别忘了验证「平行而不重合」：代入一点检查是否在平面上．这一步常被忽略．" "\n"
        r"④ 几何作法中 $GH$ 交 $AC$ 于 $AP$ 中点的验算：在 $\triangle ABD$ 内 $G\left(0,\frac12\right)$、$H\left(\frac12,0\right)$，" "\n"
        r"　 $GH:x+y=\frac12$，与 $AC:y=x$ 交于 $\left(\frac14,\frac14\right)$，正是 $AP$ 的中点 ✓" "\n"
        r"**通法（正方体中的面面平行）**：上底面与下底面的对应线段天然平行（如 $BD\parallel B_1D_1$），"
        r"因此「平面 $EFBD$」与「平面 $B_1D_1M$」要平行，**只需再找一组对应线段平行**即可．"
    ),
    'difficulty': 0.68,
    'topics': ['M-T-317'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-317-V1',
}

# ============================================================
# M-T-318-E1
# ============================================================
T318_E1 = {
    'type': '解答',
    'stem_text': (
        r"如图，在平行四边形 $ABCD$ 中，$AB=1$，$BC=2$，$\angle CBA=\dfrac\pi3$，$ABEF$ 为直角梯形，"
        r"$BE\parallel AF$，$\angle BAF=\dfrac\pi2$，$BE=2$，$AF=3$，平面 $ABCD\perp$ 平面 $ABEF$．" "\n"
        r"（1）求证：$AC\perp$ 平面 $ABEF$；" "\n"
        r"（2）求多面体 $ABCDE$ 与多面体 $ADEF$ 的体积的比值．"
    ),
    'opts': [],
    'answer': r"（1）证明见解析；（2）$\dfrac43$",
    'analysis': (
        r"（1）由余弦定理得 $AC=\sqrt3$，于是 $AB^2+AC^2=BC^2$，即 $AC\perp AB$；"
        r"再由面面垂直的性质定理即得；" "\n"
        r"（2）多面体 $ABCDE$ 是以 $ABCD$ 为底、$E$ 为顶点的四棱锥；"
        r"多面体 $ADEF$ 是三棱锥 $D-AEF$，分别求体积再作比．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"在 $\triangle ABC$ 中，$AB=1$，$BC=2$，$\angle CBA=\dfrac\pi3$，由余弦定理" "\n"
        r"$AC^2=AB^2+BC^2-2\cdot AB\cdot BC\cos\dfrac\pi3=1+4-2\times1\times2\times\dfrac12=3$，"
        r"故 $AC=\sqrt3$．" "\n"
        r"于是 $AB^2+AC^2=1+3=4=BC^2$，由勾股定理逆定理得 $\angle BAC=\dfrac\pi2$，即 $AC\perp AB$．" "\n"
        r"又平面 $ABCD\perp$ 平面 $ABEF$，交线为 $AB$，且 $AC\subset$ 平面 $ABCD$、$AC\perp AB$，" "\n"
        r"由面面垂直的性质定理得 $AC\perp$ 平面 $ABEF$．" "\n"
        r"**第（2）问**" "\n"
        r"由（1）$AC\perp$ 平面 $ABEF$，且 $AC=\sqrt3$．" "\n"
        r"多面体 $ADEF$ 即三棱锥 $D-AEF$．" "\n"
        r"在直角梯形 $ABEF$ 中，$AB\perp AF$、$AB\perp BE$（因 $BE\parallel AF$），$AB=1$、$AF=3$、$BE=2$，" "\n"
        r"$S_{\triangle AEF}=\dfrac12\cdot AF\cdot\left(E\text{ 到 }AF\text{ 的距离}\right)=\dfrac12\times3\times1=\dfrac32$．" "\n"
        r"又 $D$ 到平面 $ABEF$ 的距离等于 $C$ 到平面 $ABEF$ 的距离（因 $CD\parallel AB$，"
        r"且 $AB\subset$ 平面 $ABEF$），即 $AC=\sqrt3$．" "\n"
        r"故 $V_{ADEF}=V_{D-AEF}=\dfrac13\times\dfrac32\times\sqrt3=\dfrac{\sqrt3}2$．" "\n"
        r"多面体 $ABCDE$：因 $A$、$B$、$C$、$D$ 共面（底面 $ABCD$）且 $E\notin$ 该平面，"
        r"故它是四棱锥 $E-ABCD$．" "\n"
        r"$S_{ABCD}=AB\cdot BC\sin\dfrac\pi3=1\times2\times\dfrac{\sqrt3}2=\sqrt3$，" "\n"
        r"$E$ 到平面 $ABCD$ 的距离 $=BE=2$（因 $BE\perp AB$ 且平面 $ABEF\perp$ 平面 $ABCD$）．" "\n"
        r"$V_{ABCDE}=\dfrac13\times\sqrt3\times2=\dfrac{2\sqrt3}3$．" "\n"
        r"故 $\dfrac{V_{ABCDE}}{V_{ADEF}}=\dfrac{2\sqrt3/3}{\sqrt3/2}=\dfrac23\times\dfrac21=\dfrac43$．" "\n"
        r"即所求比值为 $\boxed{\dfrac43}$．"
    ),
    'review': (
        r"① 第（1）问的关键是用**勾股定理逆定理**证 $AC\perp AB$："
        r"$AB^2+AC^2=1+3=4=BC^2$．这一步比用投影或向量都快．" "\n"
        r"② 第（2）问最容易错的地方是**认错多面体的形状**："
        r"$ABCDE$ 看起来是五面体，实则 $A$、$B$、$C$、$D$ 共面，它就是四棱锥 $E-ABCD$．" "\n"
        r"③ $E$ 到平面 $ABCD$ 的距离：由 $BE\perp AB$（交线）且平面 $ABEF\perp$ 平面 $ABCD$，"
        r"得 $BE\perp$ 平面 $ABCD$，故距离就是 $BE=2$．" "\n"
        r"④ $D$ 到平面 $ABEF$ 的距离等于 $AC=\sqrt3$：因为 $CD\parallel AB\subset$ 平面 $ABEF$，"
        r"平行线上各点到平面的距离相等，故 $d\left(D\right)=d\left(C\right)=AC$．" "\n"
        r"⑤ 数值复核：$S_{ABCD}=\sqrt3\approx1.7321$，$V_{ABCDE}=\frac13\times1.7321\times2=1.1547$；" "\n"
        r"　 $S_{AEF}=1.5$，$V_{ADEF}=\frac13\times1.5\times1.7321=0.8660$；比值 $=\frac{1.1547}{0.8660}=1.3333=\frac43$ ✓" "\n"
        r"**通法（多面体体积比）**：先判断每个多面体能否看成「棱锥」——"
        r"若除一个顶点外其余顶点共面，就是棱锥，直接用 $\frac13Sh$；"
        r"**求高时优先用「平行线到平面的距离相等」和「面面垂直 ⟹ 线面垂直」这两条性质**．"
    ),
    'difficulty': 0.7,
    'topics': ['M-T-318'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-318-E1',
}

QS = [
    T312_V1, T312_V2, T313_E1,
    T314_E1, T314_V1, T314_V2,
    T315_E1, T315_V2,
    T316_V1,
    T317_E1, T317_V1,
    T318_E1,
]
