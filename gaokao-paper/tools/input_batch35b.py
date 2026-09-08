# -*- coding: utf-8 -*-
r"""第35批（下）：外接球 · 垂面型与三视图（4题）

来源：2024高中数学热点题型归纳完整解析版.pdf p263（PDF 页 262）

## 选题

`pick_batch.py --n 6 --topic M-T-296` → **p263 一页 4 题**。
专题「题型四 垂面型」——面面垂直中隐藏的线面垂直。

## ★ 垂面型的通法

分别取**两个面**的外心，过各自外心作该面的垂线，**交点即球心**。

$$R^{2}=(\text{外心到垂足的距离})^{2}+(\text{外心到顶点的距离})^{2}$$

## 四题全部独立验算通过

| 题 | 我的计算 | 答案 |
|---|---|---|
| E1 | $R=\sqrt5$，$OO_{1}=1$ → $d_{\max}=\sqrt5+1$ | $\sqrt5+1$ ✓ |
| V1 | 建系求得 $R^{2}=\frac{41}4$ → $41\pi$ | **C** ✓ |
| V2 | 建系求得 $O(\frac{\sqrt3}3,0,\frac{\sqrt3}3)$、$R^{2}=\frac53$ → $\frac{20\pi}3$ | **D** ✓ |
| V3 | 建系求得 $R^{2}=\frac{81}{11}$ → $\frac{324\pi}{11}$ | **D** ✓ |

## ⚠ V1 的图缺失，已按详解重建

V1 原题给的是**三视图**（图未提取）。但详解明确写了几何体：
「$PH\perp$ 平面 $ABCD$，$PH=4$，$H$ 为 $AB$ 的中点，
四边形 $ABCD$ 为正方形，其边长为 $4$」——
信息完整，故**改写为自足的文字题干**录入（详见该题 review）。
"""

T296_E1 = {
    'type': '填空',
    'stem_text': (
        r"在三棱锥 $P-ABC$ 中，$\triangle ABC$ 和 $\triangle PBC$ 都是边长为 $2\sqrt3$ 的"
        r"正三角形，$PA=3\sqrt2$．若 $M$ 为三棱锥 $P-ABC$ 外接球上的动点，"
        r"则点 $M$ 到平面 $ABC$ 距离的最大值为 ____ ．"
    ),
    'opts': [],
    'answer': r"$\sqrt5+1$",
    'analysis': (
        r"由 $AT^{2}+PT^{2}=PA^{2}$ 得 $PT\perp AT$，进而 $AT\perp$ 面 $PBC$、"
        r"面 $PBC\perp$ 面 $ABC$；球心到平面 $ABC$ 的距离为 $1$、半径 $R=\sqrt5$，"
        r"故最大距离 $=R+1$。"
    ),
    'solution': (
        r"**第一步：证面面垂直**" "\n"
        r"设 $T$ 为 $BC$ 中点．$\triangle ABC$、$\triangle PBC$ 均为边长 $2\sqrt3$ 的正三角形，" "\n"
        r"故 $AT=PT=2\sqrt3\times\dfrac{\sqrt3}2=3$．" "\n"
        r"由 $PA=3\sqrt2$ 得 $PA^{2}=18$，而 $AT^{2}+PT^{2}=9+9=18=PA^{2}$，" "\n"
        r"故 $PT\perp AT$．又 $AT\perp BC$、$BC\cap PT=T$，所以 $AT\perp$ 面 $PBC$，" "\n"
        r"从而面 $PBC\perp$ 面 $ABC$．" "\n"
        r"**第二步：定球心**" "\n"
        r"设 $O_{1}$、$O_{2}$ 分别为 $\triangle ABC$、$\triangle PBC$ 的外心．"
        r"过 $O_{1}$ 作面 $ABC$ 的垂线、过 $O_{2}$ 作面 $PBC$ 的垂线，交点 $O$ 即球心．" "\n"
        r"正三角形边长 $2\sqrt3$：外接圆半径 $=\dfrac{2\sqrt3}{\sqrt3}=2$，"
        r"中心到边的距离 $=\dfrac13\times3=1$．" "\n"
        r"故 $TO_{1}=TO_{2}=1$，四边形 $O_{1}TO_{2}O$ 为**边长 $1$ 的正方形**，$OO_{1}=1$．" "\n"
        r"**第三步：求半径**" "\n"
        r"$O_{2}P=2$（$\triangle PBC$ 外接圆半径），且 $OO_{2}\perp$ 面 $PBC$：" "\n"
        r"$R=OP=\sqrt{OO_{2}^{2}+O_{2}P^{2}}=\sqrt{1+4}=\sqrt5$．" "\n"
        r"**第四步：求最大距离**" "\n"
        r"球心 $O$ 到平面 $ABC$ 的距离 $=OO_{1}=1$．" "\n"
        r"球面上点到该平面的最大距离 $=R+OO_{1}=\sqrt5+1$．" "\n"
        r"故答案为 $\sqrt5+1$．"
    ),
    'review': (
        r"★ 由详解「设 $BC$ 中点为 $T$，$\triangle ABC$ 的外心为 $O_{1}$，"
        r"$\triangle PBC$ 的外心为 $O_{2}$，过点 $O_{1}$ 作面 $ABC$ 的垂线，"
        r"过点 $O_{2}$ 作直线面 $PBC$ 的垂线，两条垂线的交点 $O$ 即为三棱锥 $P-ABC$ "
        r"外接球的球心，因为 $\triangle ABC$ 和 $\triangle PBC$ 都是边长为 $2\sqrt3$ 的正三角形，"
        r"可得 $PT=AT=3$，又 $PA=3\sqrt2$，所以 $AT^{2}+PT^{2}=AP^{2}$，所以 $PT\perp AT$，"
        r"又因为 $AT\perp BC$，$BC\cap PT=T$，所以 $AT\perp$ 面 $PBC$，"
        r"因为 $AT\subset$ 平面 $ABC$，所以平面 $PBC\perp$ 平面 $ABC$，"
        r"且 $TO_{1}=\frac13AT=1$，所以四边形 $O_{1}TO_{2}O$ 是边长为 $1$ 的正方形，"
        r"所以外接球半径 $R=OP=\sqrt{OO_{2}^{2}+O_{2}P^{2}}=\sqrt{1+4}=\sqrt5$，"
        r"$M$ 到平面 $ABC$ 的距离 $d\le R+OO_{1}=\sqrt5+1$，故答案为 $\sqrt5+1$」还原。" "\n"
        r"**独立验算**：" "\n"
        r"$AT=PT=2\sqrt3\cdot\frac{\sqrt3}2=3$ ✓；$AT^2+PT^2=18=PA^2=(3\sqrt2)^2$ ✓ → $PT\perp AT$ ✓" "\n"
        r"正三角形边长 $2\sqrt3$：高 $=3$，外心到顶点 $=\frac23\cdot3=2$ ✓，到边 $=\frac13\cdot3=1$ ✓" "\n"
        r"$TO_1=TO_2=1$ ✓ → 正方形 → $OO_1=OO_2=1$ ✓" "\n"
        r"$R=\sqrt{OO_2^2+O_2P^2}=\sqrt{1+4}=\sqrt5$ ✓（$O_2P=2$）" "\n"
        r"$d_{\max}=R+OO_1=\sqrt5+1$ ✓ **答案正确** ✓" "\n"
        r"**⭐ 题型要点**：「两个共边的正三角形 + 第三边满足勾股」⟹ 面面垂直，"
        r"这是垂面型中最常见的隐藏结构。"
    ),
    'difficulty': 0.93,
    'topics': ['M-T-296'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-296-E1',
}

T296_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知四棱锥 $P-ABCD$ 的底面 $ABCD$ 是边长为 $4$ 的正方形，"
        r"$PH\perp$ 平面 $ABCD$，$PH=4$，$H$ 为 $AB$ 的中点，"
        r"则该四棱锥的外接球表面积为（　　）"
    ),
    'opts': [
        ('A', r"$32\pi$"), ('B', r"$30\sqrt2\pi$"),
        ('C', r"$41\pi$"), ('D', r"$40\sqrt3\pi$"),
    ],
    'answer': 'C',
    'analysis': (
        r"底面中心 $O_{1}$ 与 $\triangle PAB$ 的外心 $O_{2}$ 分别是两个面的外心，"
        r"球心 $O$ 满足 $OO_{1}\perp$ 底面、$OO_{2}\perp$ 面 $PAB$；建系求 $R$ 最便捷。"
    ),
    'solution': (
        r"**建系**：$A(0,0,0)$、$B(4,0,0)$、$C(4,4,0)$、$D(0,4,0)$；"
        r"$H$ 为 $AB$ 中点即 $H(2,0,0)$，由 $PH\perp$ 底面、$PH=4$ 得 $P(2,0,4)$．" "\n"
        r"**定球心的位置**：底面 $ABCD$ 是正方形，其外心为中心 $O_{1}(2,2,0)$；"
        r"球心 $O$ 在过 $O_{1}$ 且垂直底面的直线上，设 $O(2,2,t)$．" "\n"
        r"**列方程**：$|OA|^{2}=|OP|^{2}$" "\n"
        r"$|OA|^{2}=2^{2}+2^{2}+t^{2}=8+t^{2}$，" "\n"
        r"$|OP|^{2}=(2-2)^{2}+(2-0)^{2}+(4-t)^{2}=4+(4-t)^{2}$．" "\n"
        r"$8+t^{2}=4+16-8t+t^{2}\Rightarrow8t=12\Rightarrow t=\dfrac32$．" "\n"
        r"**求表面积**：$R^{2}=8+\left(\dfrac32\right)^{2}=8+\dfrac94=\dfrac{41}4$，" "\n"
        r"$S=4\pi R^{2}=4\pi\times\dfrac{41}4=41\pi$．" "\n"
        r"故选 C．"
    ),
    'review': (
        r"**⚠ 原题是三视图题（图未提取），题干已按详解重建为自足的文字描述**。" "\n"
        r"详解给出几何体：「根据三视图可得原几何体如图所示，且 $PH\perp$ 平面 $ABCD$，"
        r"$PH=4$，$H$ 为 $AB$ 的中点，四边形 $ABCD$ 为正方形，其边长为 $4$。"
        r"设 $O_{1}$ 为正方形 $ABCD$ 的中心，$O_{2}$ 为 $\triangle PAB$ 的外心，"
        r"则外接球的球心 $O$ 满足 $OO_{1}\perp$ 平面 $ABCD$，$OO_{2}\perp$ 平面 $PAB$，"
        r"所以 $HO_{2}\parallel OO_{1}$，所以四边形 $HO_{2}OO_{1}$ 是…"
        r"$(4-PO_{2})^{2}+4=PO_{2}^{2}$，故 $PO_{2}=\frac52$，…"
        r"故外接球半径 $R^{2}=\dots=\frac{41}4$…选 C」" "\n"
        r"**独立验算**（建系法，与详解方法不同）：" "\n"
        r"$O(2,2,1.5)$：$|OA|^2=4+4+2.25=10.25$；"
        r"$|OP|^2=0+4+(4-1.5)^2=4+6.25=10.25$ ✓ **相等**" "\n"
        r"$R^2=10.25=\frac{41}4$ ✓ → $S=41\pi$ ✓ **答案 C 正确**" "\n"
        r"**交叉验证** $\triangle PAB$ 的外接圆半径（详解给的 $PO_2=\frac52$）：" "\n"
        r"$PA=PB=\sqrt{4^2+2^2}=2\sqrt5$、$AB=4$；"
        r"面积 $=\frac12\cdot4\cdot4=8$；" "\n"
        r"$R_c=\frac{PA\cdot PB\cdot AB}{4S}=\frac{2\sqrt5\cdot2\sqrt5\cdot4}{32}=\frac{80}{32}=\frac52$ ✓ **与详解一致**"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-296'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-296-V1',
}

T296_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知三棱锥 $A-BCD$ 中，平面 $ABD\perp$ 平面 $BCD$，"
        r"且 $\triangle ABD$ 和 $\triangle BCD$ 都是边长为 $2$ 的等边三角形，"
        r"则该三棱锥的外接球表面积为（　　）"
    ),
    'opts': [
        ('A', r"$4\pi$"), ('B', r"$\dfrac{16\pi}3$"),
        ('C', r"$8\pi$"), ('D', r"$\dfrac{20\pi}3$"),
    ],
    'answer': 'D',
    'analysis': (
        r"取 $BD$ 中点 $G$，由面面垂直得 $AG\perp$ 面 $BCD$；"
        r"分别取两面的外心 $E,F$，过 $E,F$ 作各自面的垂线交于球心 $O$，"
        r"由 $R^{2}=OE^{2}+CE^{2}$ 求 $R$。"
    ),
    'solution': (
        r"**建系**（最直白）：令 $G$ 为 $BD$ 中点、置于原点，$BD$ 沿 $y$ 轴，" "\n"
        r"$B(0,1,0)$、$D(0,-1,0)$；$\triangle BCD$ 在 $xy$ 平面内，$C(\sqrt3,0,0)$；" "\n"
        r"由面 $ABD\perp$ 面 $BCD$ 且 $AG\perp BD$，得 $AG\perp$ 面 $BCD$，"
        r"又 $AG=\sqrt3$，故 $A(0,0,\sqrt3)$．" "\n"
        r"**求球心** $O(x,y,z)$：" "\n"
        r"由 $|OB|=|OD|$ 得 $(y-1)^{2}=(y+1)^{2}\Rightarrow y=0$；" "\n"
        r"由 $|OA|=|OB|$ 得 $y^{2}+(z-\sqrt3)^{2}=(y-1)^{2}+z^{2}$，代入 $y=0$：" "\n"
        r"$z^{2}-2\sqrt3z+3=1+z^{2}\Rightarrow z=\dfrac1{\sqrt3}=\dfrac{\sqrt3}3$；" "\n"
        r"由 $|OC|=|OB|$ 得 $(x-\sqrt3)^{2}+y^{2}=x^{2}+(y-1)^{2}$，代入 $y=0$：" "\n"
        r"$x^{2}-2\sqrt3x+3=x^{2}+1\Rightarrow x=\dfrac1{\sqrt3}=\dfrac{\sqrt3}3$．" "\n"
        r"故 $O\!\left(\dfrac{\sqrt3}3,\ 0,\ \dfrac{\sqrt3}3\right)$．" "\n"
        r"**求半径**：$R^{2}=|OB|^{2}=\dfrac13+1+\dfrac13=\dfrac53$．" "\n"
        r"**表面积**：$S=4\pi\times\dfrac53=\dfrac{20\pi}3$，选 D．"
    ),
    'review': (
        r"★ 由详解「取 $BD$ 中点 $G$，连接 $AG$、$CG$，则 $AG\perp BD$，"
        r"∵平面 $ABD\perp$ 平面 $BCD$，则 $AG\perp$ 平面 $BCD$，"
        r"分别取 $\triangle ABD$ 与 $\triangle BCD$ 的外心 $E,F$，"
        r"过 $E,F$ 分别作两面的垂线，相交于 $O$，则 $O$ 为三棱锥 $A-BCD$ 的外接球的球心。"
        r"由 $\triangle ABD$ 与 $\triangle BCD$ 均为边长为 $2$ 的等边三角形，"
        r"可得 $OE=OF=\frac13CG=\frac{\sqrt3}3$，∴$CE=\frac{2\sqrt3}3$，"
        r"∴$R=OC=\sqrt{OE^{2}+CE^{2}}=\sqrt{\frac13+\frac43}$，"
        r"∴三棱锥 $A-BCD$ 的外接球的表面积为 $4\pi\times R^{2}=4\pi\times\frac53=\frac{20\pi}3$」还原。" "\n"
        r"（注：$CE=\frac{2\sqrt3}3$ 即等边三角形（边长 $2$）的外接圆半径 "
        r"$=\frac23\times\sqrt3=\frac{2\sqrt3}3$ ✓）" "\n"
        r"**独立验算**（建系法）：" "\n"
        r"$O(\frac{\sqrt3}3,0,\frac{\sqrt3}3)\approx(0.5774,0,0.5774)$" "\n"
        r"$|OA|^2=0+0+(\sqrt3-0.5774)^2=(1.7321-0.5774)^2=1.1547^2=1.3333$ ✓" "\n"
        r"$|OB|^2=0.5774^2+1+0.5774^2=0.3333+1+0.3333=1.6667$ —— **不相等！**" "\n"
        r"（**更正**：$|OA|^2$ 应为 $x^2+y^2+(z-\sqrt3)^2=0.3333+0+1.3333=1.6667$ ✓ "
        r"—— 上面漏加了 $x^2$ 项，加上后与 $|OB|^2$ 相等 ✓）" "\n"
        r"$|OC|^2=(0.5774-1.7321)^2+0+0.3333=1.3333+0.3333=1.6667$ ✓" "\n"
        r"四点等距 ✓ **确为球心**；$R^2=\frac53$ ✓" "\n"
        r"$S=4\pi\cdot\frac53=\frac{20\pi}3\approx20.944$ ✓ **答案 D 正确**" "\n"
        r"**⭐ 速算**：两个全等的等边三角形（边长 $a$）沿公共边折成直二面角时，"
        r"$R^{2}=\left(\frac{a}{2\sqrt3}\right)^{2}+\left(\frac{a}{\sqrt3}\right)^{2}\times\dots$ —— "
        r"本题 $R^{2}=\frac13+\frac43=\frac53$，其中 $\frac13$ 是外心到棱的距离的平方、"
        r"$\frac43$ 是外接圆半径的平方。"
    ),
    'difficulty': 0.87,
    'topics': ['M-T-296'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-296-V2',
}

T296_V3 = {
    'type': '选择',
    'stem_text': (
        r"在四面体 $P-ABC$ 中，三角形 $ABC$ 为等边三角形，边长为 $3$，"
        r"$PA=3$，$PB=4$，$PC=5$，则四面体 $P-ABC$ 外接球表面积为（　　）"
    ),
    'opts': [
        ('A', r"$12\pi$"), ('B', r"$25\pi$"),
        ('C', r"$\dfrac{80\pi}9$"), ('D', r"$\dfrac{324\pi}{11}$"),
    ],
    'answer': 'D',
    'analysis': (
        r"把 $\triangle ABC$ 放在 $xy$ 平面，用 $PA,PB,PC$ 定出 $P$ 的坐标；"
        r"球心在过 $\triangle ABC$ 外心且垂直底面的直线上，列方程解出高度。"
    ),
    'solution': (
        r"**建系**：$A(0,0,0)$、$B(3,0,0)$、$C\!\left(\dfrac32,\dfrac{3\sqrt3}2,0\right)$，"
        r"设 $P(x,y,z)$．" "\n"
        r"**定 $P$**：" "\n"
        r"$PA^{2}=9$：$x^{2}+y^{2}+z^{2}=9$；" "\n"
        r"$PB^{2}=16$：$(x-3)^{2}+y^{2}+z^{2}=16\Rightarrow-6x+9=7\Rightarrow x=\dfrac13$；" "\n"
        r"$PC^{2}=25$：$\left(x-\dfrac32\right)^{2}+\left(y-\dfrac{3\sqrt3}2\right)^{2}+z^{2}=25$" "\n"
        r"$\Rightarrow x^{2}+y^{2}+z^{2}-3x-3\sqrt3y+9=25$" "\n"
        r"$\Rightarrow9-1-3\sqrt3y+9=25\Rightarrow-3\sqrt3y=8\Rightarrow y=-\dfrac{8\sqrt3}9$；" "\n"
        r"$z^{2}=9-\dfrac19-\dfrac{64}{27}=\dfrac{243-3-64}{27}=\dfrac{176}{27}$．" "\n"
        r"**定球心**：$\triangle ABC$ 为等边三角形，外心即重心" "\n"
        r"$O_{1}\!\left(\dfrac32,\dfrac{\sqrt3}2,0\right)$，外接圆半径 $=\sqrt3$．" "\n"
        r"设球心 $O\!\left(\dfrac32,\dfrac{\sqrt3}2,t\right)$，则 $|OA|^{2}=3+t^{2}$．" "\n"
        r"$|OP|^{2}=\left(\dfrac13-\dfrac32\right)^{2}+\left(-\dfrac{8\sqrt3}9-\dfrac{\sqrt3}2\right)^{2}+(z-t)^{2}$" "\n"
        r"$=\dfrac{49}{36}+\dfrac{625}{108}+(z-t)^{2}=\dfrac{193}{27}+(z-t)^{2}$．" "\n"
        r"由 $|OA|^{2}=|OP|^{2}$：" "\n"
        r"$3+t^{2}=\dfrac{193}{27}+z^{2}-2zt+t^{2}$" "\n"
        r"$\Rightarrow3=\dfrac{193}{27}+\dfrac{176}{27}-2zt=\dfrac{369}{27}-2zt=\dfrac{41}3-2zt$" "\n"
        r"$\Rightarrow2zt=\dfrac{41}3-3=\dfrac{32}3\Rightarrow t=\dfrac{16}{3z}$．" "\n"
        r"**求半径**：" "\n"
        r"$R^{2}=3+t^{2}=3+\dfrac{256}{9z^{2}}=3+\dfrac{256}{9\times\frac{176}{27}}"
        r"=3+\dfrac{256\times3}{176}=3+\dfrac{48}{11}=\dfrac{81}{11}$．" "\n"
        r"**表面积**：$S=4\pi\times\dfrac{81}{11}=\dfrac{324\pi}{11}$，选 D．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**原书只给答案 D，无详解**，" "\n"
        r"上述建系求解为**我独立完成**）。" "\n"
        r"**验算**：" "\n"
        r"① $P$ 的坐标：$x=\frac13$ ✓；" "\n"
        r"$y=-\frac{8\sqrt3}{9}\approx-1.5396$；$z^{2}=\frac{176}{27}\approx6.5185$，$z\approx2.5531$" "\n"
        r"② 回代 $PA$：$\sqrt{\frac19+\frac{64}{27}+\frac{176}{27}}=\sqrt{0.1111+2.3704+6.5185}"
        r"=\sqrt{9}=3$ ✓" "\n"
        r"③ $PB$：$\sqrt{(\frac13-3)^2+\frac{64}{27}+\frac{176}{27}}"
        r"=\sqrt{7.1111+8.8889}=\sqrt{16}=4$ ✓" "\n"
        r"④ $PC$：$(x-\frac32)^2=(\frac13-1.5)^2=(-\frac76)^2=\frac{49}{36}=1.3611$；" "\n"
        r"$(y-\frac{3\sqrt3}2)^2=(-\frac{8\sqrt3}9-\frac{3\sqrt3}2)^2"
        r"=(-\frac{16\sqrt3+27\sqrt3}{18})^2=(-\frac{43\sqrt3}{18})^2=\frac{5547}{324}=17.12$；" "\n"
        r"$z^2=6.5185$ → 合计 $1.3611+17.12+6.5185=25.0$ ✓ **$PC=5$ 成立** ✓" "\n"
        r"⑤ $R^{2}=\frac{81}{11}\approx7.3636$，$S=4\pi\times7.3636=\frac{324\pi}{11}\approx92.52$ ✓" "\n"
        r"**答案 D 正确** ✓" "\n"
        r"（**注**：$3,4,5$ 在这里**不是**直角三角形关系 —— "
        r"$PA=3,PB=4,PC=5$ 是三条侧棱，而底面边长也是 $3$，"
        r"容易误以为 $PA\perp PB$ 而选错。）"
    ),
    'difficulty': 0.95,
    'topics': ['M-T-296'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-296-V3',
}

QS = [T296_E1, T296_V1, T296_V2, T296_V3]
