# -*- coding: utf-8 -*-
r"""第 108 批：立体几何「垂直 · 翻折 · 体积」12 题（p292–p301）

    python3 tools/run_batch.py 108

## 选题依据

按「详解完整 + 同题型聚堆 + 无图依赖 + 可独立数值验算」筛出。
本批四个题型集中在相邻页码，读 10 页即可录完：

- M-T-320 三题（p292–p293）：垂直证明（线面垂直、棱柱中的垂直、面面垂直推出线线垂直）
- M-T-321 两题（p293–p294）：翻折中的垂直（菱形折起、矩形折成直二面角）
- M-T-322 两题（p294–p295）：体积的常规求法与等体积转化
- M-T-323 一题（p296）：多面体割补型
- M-T-324 两题（p297–p298）：体积比与探索性动点
- M-T-326 两题（p300–p301）：旋转最值、翻折最值

12 题全部由我独立建系/重新推导一遍，关键数值与原书答案对拍吻合后才录入。

## 第一条：面面垂直 ⟹ 线面垂直的「交线垂线」三步（M-T-320-V2，本批最值钱）

已知面 $PAB\perp$ 面 $ABC$、交线 $AB$、$CA\perp AB$、$CA\subset$ 面 $ABC$，则 $CA\perp$ 面 $PAB$。

> ⭐⭐ 这是全批出现 **4 次** 的动作（M-T-320-V2、M-T-321-V1、M-T-322-V1、M-T-326-E1），
> 判据只有三条：① 面面垂直；② 有一直线在其中一个面内；③ 该直线垂直于交线。
> 拿到「$\perp$ 平面」后立刻能连用两次线线垂直，整道题就通了。

## 第二条：翻折题的「不变量 + 一个变量」（M-T-321-E1 / V1 / M-T-326-V2）

翻折中**转轴上的点到被翻折点的距离不变**，所以：

- M-T-321-E1：$A'E=AE=1$、$A'D$ 由题设给出 $=\sqrt2$，于是 $AE^2+ED^2=A'D^2$ 一步得 $DE\perp AE$
- M-T-326-V2：$A'D=AD=1$、$A'E=AE=1$ 恒定，唯一的变量是 $A'$ 到桌面的距离

> ⭐⭐ 凡是翻折题，先把「哪些长度不变」列出来，剩下的只有**一个**自由量。

## 第三条：动点体积最值 ⟹ 找「到定平面的最大距离」（M-T-320-E1 / M-T-326-V2）

底面 $\triangle ABE$ 面积固定时，$V=\frac13S\cdot d$，只需最大化动点到该面的距离。

M-T-320-E1 中面 $ABE\perp$ 面 $ABCD$，故 $d(F,\text{面}ABE)=d(F,\text{直线}AB)$，
在正方形边界上一看就知道 $F$ 在 $CD$ 上时 $d=2$ 最大。

> ⚠ **必须检查最大距离能否取到**：M-T-326-V2 的 $A'$ 到桌面距离最大为 $A'O=\frac{\sqrt2}2$
> （当且仅当面 $A'DE\perp$ 桌面），此时 $F$ 是 $A'C$ 中点，距离再打对折成 $\frac{\sqrt2}4$。
"""

T320_E1 = {
    'type': '解答',
    'stem_text': (
        r"（2020·湖北武汉·高二期末）如图，在四棱锥 $P-ABCD$ 中，底面 $ABCD$ 为正方形，"
        r"$PA\perp$ 底面 $ABCD$，$PA=AB$，$E$ 为线段 $PB$ 的中点．" "\n"
        r"（1）若 $F$ 为线段 $BC$ 上的动点，证明：$AE\perp$ 平面 $PBC$；" "\n"
        r"（2）若 $F$ 为线段 $BC$，$CD$，$DA$ 上的动点（不含 $A$，$B$），$PA=2$，"
        r"三棱锥 $A-BEF$ 的体积是否存在最大值？如果存在，求出最大值；如果不存在，请说明理由．"
    ),
    'stem': [
        r"（2020·湖北武汉·高二期末）如图，在四棱锥 $P-ABCD$ 中，底面 $ABCD$ 为正方形，"
        r"$PA\perp$ 底面 $ABCD$，$PA=AB$，$E$ 为线段 $PB$ 的中点．",
        r"（1）若 $F$ 为线段 $BC$ 上的动点，证明：$AE\perp$ 平面 $PBC$；",
        r"（2）若 $F$ 为线段 $BC$，$CD$，$DA$ 上的动点（不含 $A$，$B$），$PA=2$，"
        r"三棱锥 $A-BEF$ 的体积是否存在最大值？如果存在，求出最大值；如果不存在，请说明理由．",
    ],
    'opts': [],
    'answer': r"（1）证明见解析；（2）存在，最大值为 $\dfrac23$",
    'analysis': (
        r"（1）$E$ 是 $PB$ 中点且 $PA=AB$，故等腰 $\triangle PAB$ 中 $AE\perp PB$；"
        r"再由 $BC\perp PA$、$BC\perp AB$ 得 $BC\perp$ 平面 $PAB$，从而 $BC\perp AE$，两条相交直线都垂直即可．" "\n"
        r"（2）$\triangle ABE$ 的面积固定，体积只取决于 $F$ 到平面 $ABE$ 的距离；"
        r"利用面 $ABE\perp$ 面 $ABCD$ 把「到平面」化成「到直线 $AB$」，在正方形边界上找最大．"
    ),
    'solution': (
        r"**（1）证明**" "\n"
        r"在 $\triangle PAB$ 中，$PA=AB$，$E$ 为 $PB$ 的中点，故 $AE\perp PB$．" "\n"
        r"又 $PA\perp$ 底面 $ABCD$，$BC\subset$ 平面 $ABCD$，故 $BC\perp PA$；" "\n"
        r"底面为正方形，故 $BC\perp AB$．而 $PA\cap AB=A$，$PA,AB\subset$ 平面 $PAB$，" "\n"
        r"所以 $BC\perp$ 平面 $PAB$．又 $AE\subset$ 平面 $PAB$，故 $AE\perp BC$．" "\n"
        r"由 $PB\cap BC=B$，$PB,BC\subset$ 平面 $PBC$，得 $\boxed{AE\perp\text{平面 }PBC}$．" "\n"
        r"**（2）** 由 $PA\perp$ 底面 $ABCD$ 得平面 $PAB\perp$ 平面 $ABCD$，且交线为 $AB$．" "\n"
        r"$\triangle ABE\subset$ 平面 $PAB$，故 $F$ 到平面 $ABE$ 的距离等于 $F$ 到直线 $AB$ 的距离．" "\n"
        r"由 $PA=AB=2$ 得 $S_{\triangle ABE}=\dfrac12\times AB\times\dfrac{PA}2"
        r"=\dfrac12\times2\times1=1$（$E$ 到 $AB$ 的距离为 $\dfrac{PA}2=1$）．" "\n"
        r"$F$ 在正方形 $ABCD$ 的边界 $BC\cup CD\cup DA$ 上运动（不含 $A,B$）：" "\n"
        r"$\bullet$ $F\in BC$ 或 $F\in DA$ 时，$d\left(F,AB\right)\le AD=2$；" "\n"
        r"$\bullet$ $F\in CD$ 时，$d\left(F,AB\right)=AD=2$ 恒定．" "\n"
        r"故最大距离为 $2$，在 $F$ 取遍 $CD$（不含 $D$）时取到，于是" "\n"
        r"$V_{A-BEF}=V_{F-ABE}=\dfrac13S_{\triangle ABE}\cdot d"
        r"\le\dfrac13\times1\times2=\boxed{\dfrac23}$．" "\n"
        r"即三棱锥 $A-BEF$ 的体积存在最大值 $\dfrac23$．"
    ),
    'review': (
        r"① ⭐⭐ **等腰三角形底边中点的三线合一**是（1）的入口：$PA=AB$ 而 $E$ 是 $PB$ 中点，"
        r"故 $AE$ 既是中线也是高，$AE\perp PB$ 一句话得到．" "\n"
        r"② ⭐⭐ **（2）的关键是把「到平面的距离」换成「到直线的距离」**："
        r"因为面 $ABE\subset$ 面 $PAB$ 且面 $PAB\perp$ 面 $ABCD$、交线 $AB$，"
        r"对底面内的点 $F$，$d(F,\text{面}ABE)=d(F,AB)$．少了这一步就要算平面的法向量．" "\n"
        r"③ ⭐ **$E$ 到 $AB$ 的距离是 $\frac{PA}2$ 不是 $PA$**：$E$ 是 $PB$ 中点，"
        r"$E$ 到 $AB$ 的距离是 $P$ 到 $AB$ 距离的一半，即 $\frac{PA}2=1$，故 $S_{\triangle ABE}=1$．" "\n"
        r"④ ⚠ **（1）中 $F$ 是多余条件**：$F$ 只在（2）中用到，命题人把两问写在同一个 $F$ 上，"
        r"不要误以为（1）要用到 $F$ 的位置．" "\n"
        r"⑤ 数值复核：$F$ 取 $CD$ 中点时 $d=2$，$V=\frac13\times1\times2=0.6667$；"
        r"$F$ 取 $C$ 点时 $d=2$ 同样成立（$C$ 在 $CD$ 上）；$F$ 取 $BC$ 中点时 $d=1$，$V=\frac13$ ✓" "\n"
        r"**通法（线面垂直 + 动点体积）**：" "\n"
        r"① 证线面垂直：找平面内两条相交直线分别与之垂直，等腰三角形中点、正方形邻边是常用来源；" "\n"
        r"② 动点体积先看底面是否固定，固定则只需最大化高；" "\n"
        r"③ 若高所在平面与底面垂直，把「点到平面」降为「点到交线」．"
    ),
    'difficulty': 0.62,
    'topics': ['M-T-320'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-320-E1',
}

T320_V1 = {
    'type': '解答',
    'stem_text': (
        r"（2018·北京西城·高二期中）如图，在三棱柱 $ABC-A_1B_1C_1$ 中，$CC_1\perp$ 底面 $ABC$，"
        r"$AC\perp CB$，点 $D$ 是 $AB$ 的中点．" "\n"
        r"（Ⅰ）求证：$AC\perp BC_1$；" "\n"
        r"（Ⅱ）求证：$AC_1\parallel$ 平面 $CDB_1$；" "\n"
        r"（Ⅲ）设 $AB=2AA_1$，$AC=BC$，在线段 $A_1B_1$ 上是否存在点 $M$，使得 $BM\perp CB_1$？"
        r"若存在，确定点 $M$ 的位置；若不存在，说明理由．"
    ),
    'stem': [
        r"（2018·北京西城·高二期中）如图，在三棱柱 $ABC-A_1B_1C_1$ 中，$CC_1\perp$ 底面 $ABC$，"
        r"$AC\perp CB$，点 $D$ 是 $AB$ 的中点．",
        r"（Ⅰ）求证：$AC\perp BC_1$；",
        r"（Ⅱ）求证：$AC_1\parallel$ 平面 $CDB_1$；",
        r"（Ⅲ）设 $AB=2AA_1$，$AC=BC$，在线段 $A_1B_1$ 上是否存在点 $M$，使得 $BM\perp CB_1$？"
        r"若存在，确定点 $M$ 的位置；若不存在，说明理由．",
    ],
    'opts': [],
    'answer': r"（Ⅰ）见解析；（Ⅱ）见解析；（Ⅲ）存在，$M$ 为线段 $A_1B_1$ 的中点",
    'analysis': (
        r"（Ⅰ）$CC_1\perp$ 底面又 $AC\perp CB$，故 $AC\perp$ 平面 $BCC_1B_1$，而 $BC_1$ 在该平面内．" "\n"
        r"（Ⅱ）侧面 $BCC_1B_1$ 是平行四边形，其对角线 $CB_1$ 与 $C_1B$ 交于中点 $E$；"
        r"在 $\triangle ABC_1$ 中 $D,E$ 分别是 $AB,BC_1$ 的中点，故 $DE\parallel AC_1$．" "\n"
        r"（Ⅲ）建系用 $AA_1\perp$ 底面、$AA_1=\dfrac{AB}2$ 算出 $M$ 的位置参数．"
    ),
    'solution': (
        r"**（Ⅰ）证明** 因为 $CC_1\perp$ 底面 $ABC$，$AC\subset$ 底面 $ABC$，所以 $CC_1\perp AC$．" "\n"
        r"又 $AC\perp CB$，$CB\cap CC_1=C$，故 $AC\perp$ 平面 $BCC_1B_1$．" "\n"
        r"而 $BC_1\subset$ 平面 $BCC_1B_1$，所以 $\boxed{AC\perp BC_1}$．" "\n"
        r"**（Ⅱ）证明** 设侧面平行四边形 $BCC_1B_1$ 的两条对角线 $CB_1$ 与 $C_1B$ 交于点 $E$，"
        r"则 $E$ 是 $BC_1$ 的中点．" "\n"
        r"在 $\triangle ABC_1$ 中，$D$ 是 $AB$ 的中点，$E$ 是 $BC_1$ 的中点，"
        r"故 $DE$ 是中位线，$DE\parallel AC_1$．" "\n"
        r"又 $DE\subset$ 平面 $CDB_1$，$AC_1\not\subset$ 平面 $CDB_1$，"
        r"所以 $\boxed{AC_1\parallel\text{平面 }CDB_1}$．" "\n"
        r"**（Ⅲ）** 存在，$M$ 为线段 $A_1B_1$ 的中点．证明如下：设 $AC=BC=c$，"
        r"则 $AB=\sqrt2c$，由 $AB=2AA_1$ 得 $AA_1=\dfrac{\sqrt2}2c$．" "\n"
        r"以 $C$ 为原点，$CA,CB,CC_1$ 的方向分别为 $x,y,z$ 轴建系，则" "\n"
        r"$A\left(c,0,0\right)$，$B\left(0,c,0\right)$，$C_1\left(0,0,h\right)$，"
        r"$A_1\left(c,0,h\right)$，$B_1\left(0,c,h\right)$，其中 $h=AA_1=\dfrac{\sqrt2}2c$．" "\n"
        r"设 $M=A_1+t\left(B_1-A_1\right)=\left(c-ct,\ ct,\ h\right)$，$0\le t\le1$，则" "\n"
        r"$\vec{BM}=\left(c\left(1-t\right),\ c\left(t-1\right),\ h\right)$，$\vec{CB_1}=\left(0,c,h\right)$．" "\n"
        r"$BM\perp CB_1\iff\vec{BM}\cdot\vec{CB_1}=c^2\left(t-1\right)+h^2"
        r"=c^2\left(t-1\right)+\dfrac{c^2}2=0\iff t=\dfrac12$．" "\n"
        r"故 $\boxed{M\ \text{为}\ A_1B_1\ \text{的中点}}$．"
    ),
    'review': (
        r"① ⭐⭐ **（Ⅰ）的「两次垂直凑一个线面垂直」**：$CC_1\perp$ 底面给出第一条，"
        r"题设 $AC\perp CB$ 给出第二条，两条相交直线 $CB,CC_1$ 都在平面 $BCC_1B_1$ 内 ⟹ $AC\perp$ 该平面．"
        r"凡是 $BC_1$ 这类「斜着的侧棱/对角线」，都先想它躺在哪个平面里．" "\n"
        r"② ⭐⭐ **（Ⅱ）的平行四边形对角线交点是中点** —— 这是棱柱里找中位线最标准的动作，"
        r"比「在平面内构造平行线」稳得多．" "\n"
        r"③ ⭐⭐ **（Ⅲ）用参数 $t$ 表示 $M$ 再用点积定 $t$** —— 探索性问题的通法，"
        r"且能自动判断解是否落在 $\left[0,1\right]$ 内（本题 $t=\frac12$ 恰好在中点）．" "\n"
        r"④ 数值复核（取 $c=2$）：$h=\sqrt2$，$M=\left(1,1,\sqrt2\right)$，" "\n"
        r"   $\vec{BM}=\left(1,-1,1.4142\right)$，$\vec{CB_1}=\left(0,2,1.4142\right)$" "\n"
        r"   点积 $=0-2+2.0000=0.0000$ ✓（$h^2=2$，$c^2(t-1)=4\times(-0.5)=-2$）" "\n"
        r"⑤ ⚠ 原书详解写「由 $AA_1\perp$ 底面得 $AA_1\perp CD$，再由 $CD\perp AB$ 得 $CD\perp$ 平面 $A_1ABB_1$」，"
        r"走的是纯几何路径；这里改用建系，更短且能直接给出 $t$ 的值．" "\n"
        r"**通法（棱柱中的垂直与平行）**：" "\n"
        r"① 侧棱垂直于底面 ⟹ 侧棱垂直于底面内任意直线；" "\n"
        r"② 平行四边形对角线的交点是两条对角线的公共中点，是找中位线的第一选择；" "\n"
        r"③ 探索性问题设参数 $t\in\left[0,1\right]$，用点积为零解方程，最后验证 $t$ 落在区间内．"
    ),
    'difficulty': 0.66,
    'topics': ['M-T-320'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-320-V1',
}

T320_V2 = {
    'type': '解答',
    'stem_text': (
        r"（2019·福建福州·模拟预测（文））如图，三棱锥 $P-ABC$ 中，$AB=AC=2$，$BC=2\sqrt2$，"
        r"$PA=PB=\sqrt5$，面 $PAB\perp$ 面 $ABC$．" "\n"
        r"（1）求 $PC$ 长；" "\n"
        r"（2）求三棱锥 $P-ABC$ 的体积；" "\n"
        r"（3）$\triangle PAC$ 内（含边界）上是否存在点 $H$，使 $BH\perp$ 面 $PAC$？"
        r"若存在，求出 $H$ 点的位置；若不存在，请说明理由．"
    ),
    'stem': [
        r"（2019·福建福州·模拟预测（文））如图，三棱锥 $P-ABC$ 中，$AB=AC=2$，$BC=2\sqrt2$，"
        r"$PA=PB=\sqrt5$，面 $PAB\perp$ 面 $ABC$．",
        r"（1）求 $PC$ 长；",
        r"（2）求三棱锥 $P-ABC$ 的体积；",
        r"（3）$\triangle PAC$ 内（含边界）上是否存在点 $H$，使 $BH\perp$ 面 $PAC$？"
        r"若存在，求出 $H$ 点的位置；若不存在，请说明理由．",
    ],
    'opts': [],
    'answer': r"（1）$3$；（2）$\dfrac43$；（3）存在，$H$ 在棱 $PA$ 上，且 $AH=\dfrac{2\sqrt5}5$",
    'analysis': (
        r"（1）由 $AB^2+AC^2=BC^2$ 得 $CA\perp AB$，再用面面垂直的性质得 $CA\perp$ 面 $PAB$，"
        r"于是 $\angle CAP=90^\circ$，$PC=\sqrt{CA^2+AP^2}$．" "\n"
        r"（2）$PA=PB$ 故 $AB$ 中点 $M$ 满足 $PM\perp AB$，由面面垂直得 $PM\perp$ 面 $ABC$，即 $PM$ 是高．" "\n"
        r"（3）要使 $BH\perp$ 面 $PAC$，只需 $BH\perp PA$ 且 $BH\perp CA$；后者由 $CA\perp$ 面 $PAB$ 自动给出，"
        r"故 $H$ 就是 $B$ 到 $PA$ 的垂足，用余弦定理算 $AH$．"
    ),
    'solution': (
        r"**（1）** $\because AB^2+AC^2=4+4=8=BC^2$，$\therefore\angle CAB=90^\circ$，即 $CA\perp AB$．" "\n"
        r"又面 $PAB\perp$ 面 $ABC$，交线为 $AB$，$CA\subset$ 面 $ABC$ 且 $CA\perp AB$，" "\n"
        r"$\therefore CA\perp$ 面 $PAB$，从而 $CA\perp PA$，$\angle CAP=90^\circ$．" "\n"
        r"$\therefore PC=\sqrt{CA^2+AP^2}=\sqrt{4+5}=\boxed3$．" "\n"
        r"**（2）** 取 $AB$ 的中点 $M$，连 $PM$．由 $PA=PB=\sqrt5$ 得 $PM\perp AB$，" "\n"
        r"$PM=\sqrt{PA^2-AM^2}=\sqrt{5-1}=2$．由面 $PAB\perp$ 面 $ABC$、交线 $AB$ 得 $PM\perp$ 面 $ABC$．" "\n"
        r"$S_{\triangle ABC}=\dfrac12\times AB\times AC=\dfrac12\times2\times2=2$，" "\n"
        r"$\therefore V=\dfrac13S_{\triangle ABC}\cdot PM=\dfrac13\times2\times2=\boxed{\dfrac43}$．" "\n"
        r"**（3）** 存在．作 $BH\perp PA$ 于 $H$．由（1）$CA\perp$ 面 $PAB$，而 $BH\subset$ 面 $PAB$，" "\n"
        r"故 $CA\perp BH$；又 $BH\perp PA$，$PA\cap CA=A$，所以 $BH\perp$ 面 $PAC$．" "\n"
        r"在 $\triangle PAB$ 中，由余弦定理" "\n"
        r"$\cos\angle BAP=\dfrac{PA^2+AB^2-PB^2}{2\cdot PA\cdot AB}"
        r"=\dfrac{5+4-5}{2\cdot\sqrt5\cdot2}=\dfrac1{\sqrt5}$，" "\n"
        r"$\therefore AH=AB\cos\angle BAP=\dfrac2{\sqrt5}=\boxed{\dfrac{2\sqrt5}5}$．" "\n"
        r"此时 $AH=\dfrac{2\sqrt5}5\approx0.894<PA=\sqrt5\approx2.236$，"
        r"故 $H$ 落在棱 $PA$ 上（在 $\triangle PAC$ 的边界上），满足要求．"
    ),
    'review': (
        r"① ⭐⭐ **$AB^2+AC^2=BC^2$ ⟹ $\angle CAB=90^\circ$ 是本题的题眼**："
        r"$2^2+2^2=8=\left(2\sqrt2\right)^2$，一步给出 $CA\perp AB$，"
        r"再配面面垂直即得 $CA\perp$ 面 $PAB$ —— 后面三问全靠这一条．" "\n"
        r"② ⭐⭐ **（3）的「垂足即所求」思路**：要 $BH\perp$ 面 $PAC$，" "\n"
        r"面 $PAC$ 内有两条相交直线 $PA$ 与 $CA$；$BH\perp CA$ 由 $CA\perp$ 面 $PAB$ 白送，"
        r"所以只需再令 $BH\perp PA$ —— $H$ 就是 $B$ 到 $PA$ 的垂足，不用猜．" "\n"
        r"③ ⭐ **必须验证 $H$ 真的落在 $\triangle PAC$ 内（含边界）**："
        r"$AH=\frac{2\sqrt5}5\approx0.894<\sqrt5$，确实在棱 $PA$ 上；若不检验，探索性问法就丢了得分点．" "\n"
        r"④ 数值复核：$PM=\sqrt{5-1}=2$ ✓；$V=\frac13\times2\times2=1.3333=\frac43$ ✓；" "\n"
        r"   $BH=AB\sin\angle BAP=2\sqrt{1-\frac15}=\frac4{\sqrt5}=1.7889$，"
        r"   检验 $BH\perp PA$：$\vec{AB}\cdot\vec{AP}$ 方向余弦 $=\cos\angle BAP=\frac1{\sqrt5}$，"
        r"   $AH=AB\cos\angle BAP=0.8944=\frac{2\sqrt5}5$ ✓" "\n"
        r"⑤ 原书用 $AH=AB\sin\angle ABH=AB\sin\angle APM$ 计算，"
        r"本质一样（$\angle ABH=90^\circ-\angle BAP=\angle APM$），这里直接用余弦定理更短．" "\n"
        r"**通法（面面垂直 + 探索性垂直）**：" "\n"
        r"① 见到面面垂直，先找「在某一面内且垂直于交线」的直线 ⟹ 线面垂直；" "\n"
        r"② 证 $l\perp$ 面 $\alpha$ 时，若其中一条已由线面垂直白送，只需补另一条；" "\n"
        r"③ 探索性问法最后必须验证点落在指定区域（含边界）内．"
    ),
    'difficulty': 0.68,
    'topics': ['M-T-320'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-320-V2',
}

T321_E1 = {
    'type': '解答',
    'stem_text': (
        r"（2021·河北·衡水市第十四中学高二阶段练习）如图①，在菱形 $ABCD$ 中，$\angle A=60^\circ$ 且 $AB=2$，"
        r"$E$ 为 $AD$ 的中点，将 $\triangle ABE$ 沿 $BE$ 折起使 $A'D=\sqrt2$，"
        r"得到如图②所示的四棱锥 $A'-BCDE$．" "\n"
        r"（Ⅰ）求证：平面 $ABE\perp$ 平面 $ABC$；" "\n"
        r"（Ⅱ）若 $P$ 为 $AC$ 的中点，求三棱锥 $P-ABD$ 的体积．"
    ),
    'stem': [
        r"（2021·河北·衡水市第十四中学高二阶段练习）如图①，在菱形 $ABCD$ 中，$\angle A=60^\circ$ 且 $AB=2$，"
        r"$E$ 为 $AD$ 的中点，将 $\triangle ABE$ 沿 $BE$ 折起使 $A'D=\sqrt2$，"
        r"得到如图②所示的四棱锥 $A'-BCDE$．",
        r"（Ⅰ）求证：平面 $ABE\perp$ 平面 $ABC$；",
        r"（Ⅱ）若 $P$ 为 $AC$ 的中点，求三棱锥 $P-ABD$ 的体积．",
    ],
    'opts': [],
    'answer': r"（Ⅰ）证明见解析；（Ⅱ）$\dfrac{\sqrt3}6$",
    'analysis': (
        r"（Ⅰ）菱形中 $\angle A=60^\circ$ ⟹ $\triangle ABD$ 为等边三角形，$E$ 为 $AD$ 中点 ⟹ $DE\perp BE$；"
        r"折起后 $AE=ED=1$、$A'D=\sqrt2$，由勾股逆定理得 $DE\perp AE$．" "\n"
        r"于是 $DE\perp$ 平面 $ABE$，而 $DE\parallel BC$，故 $BC\perp$ 平面 $ABE$，进而面面垂直．" "\n"
        r"（Ⅱ）$AE\perp$ 平面 $BCDE$ 是高，用中点把 $V_{P-ABD}$ 化为 $\dfrac12V_{A-BCD}$．"
    ),
    'solution': (
        r"**（Ⅰ）证明** 菱形 $ABCD$ 中 $AB=AD=2$ 且 $\angle A=60^\circ$，故 $\triangle ABD$ 为等边三角形．" "\n"
        r"$E$ 为 $AD$ 的中点，所以 $BE\perp AD$，即 $DE\perp BE$．" "\n"
        r"折起后 $AE=ED=1$，题设 $A'D=\sqrt2$，满足 $AE^2+ED^2=1+1=2=\left(A'D\right)^2$，" "\n"
        r"故 $DE\perp AE$．" "\n"
        r"又 $BE\cap AE=E$，$BE,AE\subset$ 平面 $ABE$，所以 $DE\perp$ 平面 $ABE$．" "\n"
        r"菱形中 $BC\parallel AD$，而 $D,E,A$ 共线，故 $BC\parallel DE$，于是 $BC\perp$ 平面 $ABE$．" "\n"
        r"又 $BC\subset$ 平面 $ABC$，所以 $\boxed{\text{平面 }ABC\perp\text{平面 }ABE}$．" "\n"
        r"**（Ⅱ）** 由（Ⅰ）$AE\perp$ 平面 $BCDE$，故 $AE$ 是三棱锥 $A-BCD$ 的高，$AE=1$．" "\n"
        r"$S_{\triangle BCD}=S_{\triangle ABD}=\dfrac{\sqrt3}4\times2^2=\sqrt3$．" "\n"
        r"$P$ 为 $AC$ 的中点，故 $V_{P-ABD}=\dfrac12V_{C-ABD}=\dfrac12V_{A-BCD}$，" "\n"
        r"$V_{A-BCD}=\dfrac13S_{\triangle BCD}\cdot AE=\dfrac13\times\sqrt3\times1=\dfrac{\sqrt3}3$．" "\n"
        r"$\therefore V_{P-ABD}=\dfrac12\times\dfrac{\sqrt3}3=\boxed{\dfrac{\sqrt3}6}$．"
    ),
    'review': (
        r"① ⭐⭐ **翻折中的「不变」与「变」**：$A'E=AE=1$ 不变（$E$ 在转轴 $BE$ 上），"
        r"$A'D$ 由题设给成 $\sqrt2$ 也不变（$D$ 不在被翻折的部分）．" "\n"
        r"两不变长度配上 $ED=1$，恰好凑出 $1^2+1^2=\left(\sqrt2\right)^2$ ⟹ $DE\perp AE$．" "\n"
        r"② ⭐⭐ **$\triangle ABD$ 等边 ⟹ $E$ 为中点 ⟹ $BE\perp AD$**："
        r"这条在翻折前后都成立，是「不变量」的典型用法．" "\n"
        r"③ ⭐ **$BC\parallel DE$ 是连接两个平面的桥**："
        r"由 $DE\perp$ 面 $ABE$ 直接得 $BC\perp$ 面 $ABE$，省掉一次证明．" "\n"
        r"④ ⭐ **换顶点**：$V_{P-ABD}$ 直接算高很麻烦，用 $P$ 是中点换成 $\frac12V_{C-ABD}$，"
        r"再换成 $\frac12V_{A-BCD}$，而 $A-BCD$ 的高就是现成的 $AE=1$．" "\n"
        r"⑤ 数值复核：$S_{\triangle BCD}=\frac{\sqrt3}4\times4=1.7321$，"
        r"$V_{A-BCD}=\frac13\times1.7321=0.5774=\frac{\sqrt3}3$ ✓，"
        r"$V_{P-ABD}=0.2887=\frac{\sqrt3}6=0.2887$ ✓" "\n"
        r"⑥ ⚠ 原书答案写作 `3/6`（根号丢失），实际为 $\frac{\sqrt3}6$；"
        r"判据：$S_{\triangle BCD}=\sqrt3$ 不是 $3$，若按 $3$ 算得 $\frac12$，与详解的 $\frac16\times\sqrt3\times1$ 不符．" "\n"
        r"**通法（翻折中的垂直）**：" "\n"
        r"① 先列出翻折中不变的长度（转轴上点到被翻折点的距离）；" "\n"
        r"② 用勾股逆定理把「两条不变长度 + 一条给定长度」翻译成垂直；" "\n"
        r"③ 线面垂直 ⟹ 找平行线转移到需要的方向 ⟹ 面面垂直．"
    ),
    'difficulty': 0.64,
    'topics': ['M-T-321'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-321-E1',
}

T321_V1 = {
    'type': '解答',
    'stem_text': (
        r"（2020·江西·南昌市第三中学高二阶段练习（理））如图，$ABCD$ 是块矩形硬纸板，"
        r"其中 $AB=2AD=2\sqrt2$，$E$ 为 $DC$ 中点，将它沿 $AE$ 折成直二面角 $D-AE-B$．" "\n"
        r"（1）求证：$AD\perp$ 平面 $BDE$；" "\n"
        r"（2）求四棱锥 $D-ABCE$ 的体积．"
    ),
    'stem': [
        r"（2020·江西·南昌市第三中学高二阶段练习（理））如图，$ABCD$ 是块矩形硬纸板，"
        r"其中 $AB=2AD=2\sqrt2$，$E$ 为 $DC$ 中点，将它沿 $AE$ 折成直二面角 $D-AE-B$．",
        r"（1）求证：$AD\perp$ 平面 $BDE$；",
        r"（2）求四棱锥 $D-ABCE$ 的体积．",
    ],
    'opts': [],
    'answer': r"（1）证明见解析；（2）$1$",
    'analysis': (
        r"先由 $AE=BE=2$ 与 $AB^2=8$ 得 $AE\perp BE$（在折痕两侧都成立）；"
        r"直二面角给出面 $DAE\perp$ 面 $ABE$，配 $BE\perp AE$ 得 $BE\perp$ 面 $ADE$，"
        r"于是 $BE\perp AD$，再加 $AD\perp DE$ 即得线面垂直．" "\n"
        r"（2）取 $AE$ 中点 $M$，$AD=DE$ 故 $DM\perp AE$，由面面垂直得 $DM\perp$ 面 $ABCE$，即 $DM$ 是高．"
    ),
    'solution': (
        r"**（1）证明** 由 $AB=2\sqrt2$、$AD=\sqrt2$、$E$ 为 $DC$ 中点得 $DE=\dfrac{DC}2=\sqrt2$，" "\n"
        r"$AE=BE=\sqrt{AD^2+DE^2}=\sqrt{2+2}=2$．" "\n"
        r"$\because AE^2+BE^2=4+4=8=AB^2$，$\therefore AE\perp BE$．" "\n"
        r"直二面角 $D-AE-B$ 即平面 $DAE\perp$ 平面 $ABE$，交线为 $AE$，"
        r"又 $BE\subset$ 平面 $ABE$ 且 $BE\perp AE$，" "\n"
        r"$\therefore BE\perp$ 平面 $ADE$．而 $AD\subset$ 平面 $ADE$，故 $AD\perp BE$．" "\n"
        r"在 $\mathrm{Rt}\triangle ADE$ 中，$AE=2$，$AD=DE=\sqrt2$，满足 $AD^2+DE^2=AE^2$，"
        r"故 $AD\perp DE$．" "\n"
        r"又 $BE\cap DE=E$，$BE,DE\subset$ 平面 $BDE$，所以 $\boxed{AD\perp\text{平面 }BDE}$．" "\n"
        r"**（2）** 取 $AE$ 的中点 $M$，连 $DM$．由 $AD=DE$ 得 $DM\perp AE$；" "\n"
        r"又平面 $DAE\perp$ 平面 $ABE$、交线 $AE$、$DM\subset$ 平面 $DAE$，"
        r"故 $DM\perp$ 平面 $ABCE$，即 $DM$ 是四棱锥的高．" "\n"
        r"$\mathrm{Rt}\triangle ADE$ 中斜边 $AE=2$，故 $DM=\dfrac{AE}2=1$．" "\n"
        r"底面 $ABCE$ 是梯形，$AB\parallel CE$，$AB=2\sqrt2$，$CE=\sqrt2$，高 $BC=AD=\sqrt2$，" "\n"
        r"$S_{ABCE}=\dfrac{\left(AB+CE\right)\cdot BC}2"
        r"=\dfrac{\left(2\sqrt2+\sqrt2\right)\times\sqrt2}2=3$．" "\n"
        r"$\therefore V_{D-ABCE}=\dfrac13S_{ABCE}\cdot DM=\dfrac13\times3\times1=\boxed1$．"
    ),
    'review': (
        r"① ⭐⭐ **$AE=BE=2$ 且 $AE^2+BE^2=AB^2$ ⟹ $AE\perp BE$**："
        r"这一步在折叠前算、折叠后仍然成立（$BE$ 与 $AE$ 分别在折痕两侧，"
        r"但两者的**长度**都不变，而 $\triangle ABE$ 本身不变形）．" "\n"
        r"② ⭐⭐ **「直二面角」= 两面垂直**：配「在某一面内垂直于交线」的直线即得线面垂直，"
        r"本题连用了两次（$BE\perp$ 面 $ADE$、$DM\perp$ 面 $ABCE$），是整题的主轴．" "\n"
        r"③ ⭐ **$DM=\frac{AE}2$ 是直角三角形斜边中线的性质**："
        r"$\triangle ADE$ 是斜边为 $AE$ 的直角三角形，$M$ 为斜边中点，故 $DM=\frac{AE}2=1$，不用勾股．" "\n"
        r"④ 数值复核：$S_{ABCE}=\frac{\left(2.8284+1.4142\right)\times1.4142}2=\frac{6.0000}2=3$ ✓，"
        r"$V=\frac13\times3\times1=1$ ✓" "\n"
        r"⑤ ⚠ 底面 $ABCE$ 是**梯形**不是矩形：$CE=\frac{DC}2=\sqrt2$ 只有 $AB$ 的一半，"
        r"若误当矩形会得 $S=2\sqrt2\times\sqrt2=4$，$V=\frac43$（错）．" "\n"
        r"**通法（沿一条线折成直二面角）**：" "\n"
        r"① 先算折痕两侧的不变长度，用勾股逆定理找垂直；" "\n"
        r"② 直二面角 ⟹ 「面内垂直于交线的直线 ⟂ 另一面」，通常要用两次；" "\n"
        r"③ 求高时优先找等腰/直角三角形斜边上的中线．"
    ),
    'difficulty': 0.60,
    'topics': ['M-T-321'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-321-V1',
}

T322_E1 = {
    'type': '解答',
    'stem_text': (
        r"（2021·全国·高一课时练习）如图所示，在棱长为 $2$ 的正方体 $ACBD-A_1C_1B_1D_1$ 中，"
        r"$M$ 是线段 $AB$ 上的动点．" "\n"
        r"（1）证明：$AB\parallel$ 平面 $A_1B_1C$；" "\n"
        r"（2）若 $M$ 是 $AB$ 的中点，证明：平面 $MCC_1\perp$ 平面 $ABB_1A_1$；" "\n"
        r"（3）求三棱锥 $M-A_1B_1C$ 的体积．"
    ),
    'stem': [
        r"（2021·全国·高一课时练习）如图所示，在棱长为 $2$ 的正方体 $ACBD-A_1C_1B_1D_1$ 中，"
        r"$M$ 是线段 $AB$ 上的动点．",
        r"（1）证明：$AB\parallel$ 平面 $A_1B_1C$；",
        r"（2）若 $M$ 是 $AB$ 的中点，证明：平面 $MCC_1\perp$ 平面 $ABB_1A_1$；",
        r"（3）求三棱锥 $M-A_1B_1C$ 的体积．",
    ],
    'opts': [],
    'answer': r"（1）证明见解析；（2）证明见解析；（3）$\dfrac43$",
    'analysis': (
        r"（1）正方体中 $AB\parallel A_1B_1$，而 $A_1B_1$ 在平面 $A_1B_1C$ 内．" "\n"
        r"（2）正方形 $ACBD$ 的两条对角线互相垂直，故 $CM\perp AB$；再由 $AA_1\perp$ 底面得 $CM\perp AA_1$，"
        r"于是 $CM\perp$ 平面 $ABB_1A_1$．" "\n"
        r"（3）由（1）$AB\parallel$ 平面 $A_1B_1C$，故 $M$ 与 $A$ 到该平面距离相等，可换顶点为 $A$．"
    ),
    'solution': (
        r"**（1）证明** 在正方体 $ACBD-A_1C_1B_1D_1$ 中，$AB\parallel A_1B_1$．" "\n"
        r"又 $A_1B_1\subset$ 平面 $A_1B_1C$，$AB\not\subset$ 平面 $A_1B_1C$，" "\n"
        r"$\therefore\boxed{AB\parallel\text{平面 }A_1B_1C}$．" "\n"
        r"**（2）证明** 底面 $ACBD$ 是正方形，$AC=BC$，$M$ 是 $AB$ 的中点（即正方形中心），"
        r"故 $CM\perp AB$．" "\n"
        r"$\because AA_1\perp$ 平面 $ACBD$，$CM\subset$ 平面 $ACBD$，$\therefore CM\perp AA_1$．" "\n"
        r"又 $AB\subset$ 平面 $ABB_1A_1$，$AA_1\subset$ 平面 $ABB_1A_1$，$AB\cap AA_1=A$，" "\n"
        r"$\therefore CM\perp$ 平面 $ABB_1A_1$．而 $CM\subset$ 平面 $MCC_1$，" "\n"
        r"$\therefore\boxed{\text{平面 }MCC_1\perp\text{平面 }ABB_1A_1}$．" "\n"
        r"**（3）** 由（1）$AB\parallel$ 平面 $A_1B_1C$，故线段 $AB$ 上任意一点到该平面的距离都相等，"
        r"即 $d\left(M,\text{平面}A_1B_1C\right)=d\left(A,\text{平面}A_1B_1C\right)$．" "\n"
        r"于是 $V_{M-A_1B_1C}=V_{A-A_1B_1C}=V_{B_1-ACA_1}$．" "\n"
        r"在 $\mathrm{Rt}\triangle ACA_1$ 中，$AC=AA_1=2$，故 $S_{\triangle ACA_1}=\dfrac12\times2\times2=2$；" "\n"
        r"平面 $ACA_1$ 即平面 $ACC_1A_1$，$B_1$ 到该平面的距离等于棱长 $2$．" "\n"
        r"$\therefore V_{M-A_1B_1C}=\dfrac13S_{\triangle ACA_1}\times2"
        r"=\dfrac13\times2\times2=\boxed{\dfrac43}$．"
    ),
    'review': (
        r"① ⭐⭐ **（3）的「平行线上点到平面距离相等」**是本题的题眼："
        r"$M$ 在 $AB$ 上动，但 $AB\parallel$ 平面 $A_1B_1C$，所以体积与 $M$ 的位置无关 —— "
        r"这正是「$M$ 是动点」却要求定值的原因．" "\n"
        r"② ⭐⭐ **换顶点是求三棱锥体积的第一手段**：$V_{A-A_1B_1C}$ 直接算要找 $A$ 到平面 $A_1B_1C$ 的距离，"
        r"换成 $V_{B_1-ACA_1}$ 后，底面 $\triangle ACA_1$ 是正方体的一个侧面的一半，高就是棱长，一步出结果．" "\n"
        r"③ ⭐ **正方体的顶点命名要认准**：本题是 $ACBD-A_1C_1B_1D_1$，"
        r"$AB$ 与 $CD$ 是底面正方形的**对角线**而非棱，所以 $AC=BC=2$ 是棱、$AB=2\sqrt2$ 是对角线，"
        r"（2）中 $CM\perp AB$ 用的正是「正方形对角线互相垂直」．" "\n"
        r"④ 数值复核（建系 $A(0,0,0),C(2,0,0),B(2,2,0),D(0,2,0)$）：" "\n"
        r"   $S_{\triangle AA_1B_1}=\frac12\left|\vec{AA_1}\times\vec{AB_1}\right|"
        r"=\frac12\left|\left(-4,4,0\right)\right|=2\sqrt2$；" "\n"
        r"   平面 $AA_1B_1$ 为 $x-y=0$，$d\left(C,\text{该平面}\right)=\frac2{\sqrt2}=\sqrt2$；" "\n"
        r"   $V=\frac13\times2\sqrt2\times\sqrt2=\frac43$ ✓ 与换顶点法一致．" "\n"
        r"**通法（动点体积为定值）**：" "\n"
        r"① 先证动点所在直线平行于底面所在平面 ⟹ 距离相等 ⟹ 体积与动点位置无关；" "\n"
        r"② 换顶点时优先选「底面是侧面的一半、高是棱长」的那种拆法；" "\n"
        r"③ 正方体中对角线与棱要分清，$AB$ 这类跨越两个字母的可能是面对角线．"
    ),
    'difficulty': 0.55,
    'topics': ['M-T-322'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-322-E1',
}

T322_V1 = {
    'type': '解答',
    'stem_text': (
        r"（2020·江西·吉安县立中学高二阶段练习）四棱锥 $P-ABCD$ 中，$AB\parallel CD$，$AB\perp BC$，"
        r"$AB=BC=1$，$PA=CD=2$，$PA\perp$ 底面 $ABCD$，$E$ 在 $PB$ 上．" "\n"
        r"（1）证明：$AC\perp PD$；" "\n"
        r"（2）若 $PE=2BE$，求三棱锥 $P-ACE$ 的体积．"
    ),
    'stem': [
        r"（2020·江西·吉安县立中学高二阶段练习）四棱锥 $P-ABCD$ 中，$AB\parallel CD$，$AB\perp BC$，"
        r"$AB=BC=1$，$PA=CD=2$，$PA\perp$ 底面 $ABCD$，$E$ 在 $PB$ 上．",
        r"（1）证明：$AC\perp PD$；",
        r"（2）若 $PE=2BE$，求三棱锥 $P-ACE$ 的体积．",
    ],
    'opts': [],
    'answer': r"（1）证明见解析；（2）$\dfrac29$",
    'analysis': (
        r"（1）过 $A$ 作 $AF\perp DC$ 于 $F$，由 $AB=BC=1$、$CD=2$ 可得 $CF=DF=AF=1$，"
        r"从而 $\angle DAC=90^\circ$；再由 $PA\perp$ 底面得 $AC\perp PA$，于是 $AC\perp$ 平面 $PAD$．" "\n"
        r"（2）用割补：$V_{P-ACE}=V_{P-ABC}-V_{E-ABC}$，而 $E$ 分 $PB$ 成 $1:2$ 给出高度比．"
    ),
    'solution': (
        r"**（1）证明** 过 $A$ 作 $AF\perp DC$ 于 $F$．" "\n"
        r"由 $AB\parallel CD$、$AB\perp BC$、$AB=BC=1$、$CD=2$，得 $AF=BC=1$，"
        r"且 $F$ 恰为 $DC$ 的中点，即 $CF=DF=1$．" "\n"
        r"在 $\triangle ADC$ 中，$AD=\sqrt{AF^2+DF^2}=\sqrt2$，$AC=\sqrt{AB^2+BC^2}=\sqrt2$，"
        r"$DC=2$，" "\n"
        r"$\because AD^2+AC^2=2+2=4=DC^2$，$\therefore\angle DAC=90^\circ$，即 $AC\perp DA$．" "\n"
        r"又 $PA\perp$ 底面 $ABCD$，$AC\subset$ 底面 $ABCD$，故 $AC\perp PA$．" "\n"
        r"而 $PA\cap AD=A$，$PA,AD\subset$ 平面 $PAD$，所以 $AC\perp$ 平面 $PAD$．" "\n"
        r"又 $PD\subset$ 平面 $PAD$，$\therefore\boxed{AC\perp PD}$．" "\n"
        r"**（2）** 由 $PE=2BE$ 得 $BE=\dfrac{PB}3$，故 $E$ 到平面 $ABC$ 的距离等于"
        r"$P$ 到平面 $ABC$ 距离的 $\dfrac13$．" "\n"
        r"于是 $V_{E-ABC}=\dfrac13V_{P-ABC}$，从而" "\n"
        r"$V_{P-ACE}=V_{P-ABC}-V_{E-ABC}=\dfrac23V_{P-ABC}$．" "\n"
        r"$S_{\triangle ABC}=\dfrac12\times AB\times BC=\dfrac12\times1\times1=\dfrac12$，"
        r"$V_{P-ABC}=\dfrac13S_{\triangle ABC}\cdot PA=\dfrac13\times\dfrac12\times2=\dfrac13$．" "\n"
        r"$\therefore V_{P-ACE}=\dfrac23\times\dfrac13=\boxed{\dfrac29}$．"
    ),
    'review': (
        r"① ⭐⭐ **$F$ 恰为 $DC$ 的中点 ⟹ $AD=AC$ ⟹ $\angle DAC=90^\circ$**："
        r"$AD=AC=\sqrt2$ 而 $DC=2$，勾股逆定理一步定直角，这是（1）的核心．" "\n"
        r"② ⭐⭐ **（2）的割补 $V_{P-ACE}=V_{P-ABC}-V_{E-ABC}$**："
        r"直接求 $P-ACE$ 的高很麻烦，但 $E$ 在 $PB$ 上 ⟹ 两个三棱锥共用底面 $ABC$、"
        r"高成 $1:3$，一步得 $\frac23V_{P-ABC}$．" "\n"
        r"③ ⭐ **「$E$ 分 $PB$ 成 $1:2$」换算成高度比要小心**："
        r"$PE=2BE$ 意味着 $BE:BP=1:3$，所以 $V_{E-ABC}=\frac13V_{P-ABC}$，"
        r"剩下的是 $\frac23$ 不是 $\frac13$．" "\n"
        r"④ 数值复核：$V_{P-ABC}=\frac13\times0.5\times2=0.3333$；"
        r"$V_{E-ABC}=0.1111$；$V_{P-ACE}=0.3333-0.1111=0.2222=\frac29$ ✓" "\n"
        r"⑤ 底面是直角梯形：$AB\parallel CD$、$AB\perp BC$⟹$BC$ 就是两条平行线间的距离，"
        r"故 $AF=BC=1$，$S_{ABCD}=\frac{\left(1+2\right)\times1}2=\frac32$（本题未用到，但可用于验算）．" "\n"
        r"**通法（线线垂直 + 割补求体积）**：" "\n"
        r"① 证 $l_1\perp l_2$ 时，先证 $l_1\perp$ 含 $l_2$ 的平面；" "\n"
        r"② 该平面通常由「题设的垂直」+「勾股逆定理给出的垂直」两条相交直线确定；" "\n"
        r"③ 点在侧棱上时，用「同底面、高成比例」做割补，比为该点到两端的线段比．"
    ),
    'difficulty': 0.58,
    'topics': ['M-T-322'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-322-V1',
}

T323_E1 = {
    'type': '解答',
    'stem_text': (
        r"（2020·安徽省泗县第一中学模拟预测（文））如图，梯形 $ABCD$ 所在的平面与"
        r"等腰梯形 $ABEF$ 所在的平面互相垂直，$G$ 为 $AB$ 的中点，$AB\perp AD$，"
        r"$AB\parallel CD\parallel EF$，$DA=AF=EF=CD=\sqrt3$，$AB=2\sqrt3$．" "\n"
        r"（Ⅰ）求证：$CE\parallel$ 平面 $ADF$；" "\n"
        r"（Ⅱ）求证：平面 $CEG\perp$ 平面 $CFB$；" "\n"
        r"（Ⅲ）求多面体 $AFEBCD$ 的体积．"
    ),
    'stem': [
        r"（2020·安徽省泗县第一中学模拟预测（文））如图，梯形 $ABCD$ 所在的平面与"
        r"等腰梯形 $ABEF$ 所在的平面互相垂直，$G$ 为 $AB$ 的中点，$AB\perp AD$，"
        r"$AB\parallel CD\parallel EF$，$DA=AF=EF=CD=\sqrt3$，$AB=2\sqrt3$．",
        r"（Ⅰ）求证：$CE\parallel$ 平面 $ADF$；",
        r"（Ⅱ）求证：平面 $CEG\perp$ 平面 $CFB$；",
        r"（Ⅲ）求多面体 $AFEBCD$ 的体积．",
    ],
    'opts': [],
    'answer': r"（Ⅰ）证明见解析；（Ⅱ）证明见解析；（Ⅲ）$3$",
    'analysis': (
        r"（Ⅰ）$CD\paralleleq EF$ ⟹ 四边形 $CDFE$ 是平行四边形 ⟹ $DF\parallel CE$．" "\n"
        r"（Ⅱ）$GB\paralleleq EF$ 且 $GB=BE$ ⟹ 菱形 $GBEF$ ⟹ $BF\perp EG$；"
        r"再由 $GC\perp$ 平面 $ABEF$ 得 $GC\perp BF$，故 $BF\perp$ 平面 $CEG$．" "\n"
        r"（Ⅲ）多面体拆成三棱柱 $ADF-GCE$ 与三棱锥 $B-GCE$．"
    ),
    'solution': (
        r"**（Ⅰ）证明** $\because CD\parallel EF$ 且 $CD=EF$，$\therefore$ 四边形 $CDFE$ 为平行四边形，"
        r"故 $DF\parallel CE$．" "\n"
        r"又 $DF\subset$ 平面 $ADF$，$CE\not\subset$ 平面 $ADF$，$\therefore\boxed{CE\parallel\text{平面 }ADF}$．" "\n"
        r"**（Ⅱ）证明** $G$ 为 $AB$ 中点，故 $GB=\dfrac{AB}2=\sqrt3$；"
        r"又 $GB\parallel EF$、$GB=EF$，故四边形 $GBEF$ 为平行四边形；" "\n"
        r"而 $GB=BE=\sqrt3$，故四边形 $GBEF$ 为**菱形**，于是 $BF\perp EG$．" "\n"
        r"在梯形 $ABCD$ 中，$AD\paralleleq GC$（同理可证四边形 $AGCD$ 为平行四边形），"
        r"又 $AD\perp AB$，故 $GC\perp AB$；" "\n"
        r"而平面 $ABEF\perp$ 平面 $ABCD$、交线 $AB$、$GC\subset$ 平面 $ABCD$，"
        r"$\therefore GC\perp$ 平面 $ABEF$，从而 $GC\perp BF$．" "\n"
        r"由 $GC\cap EG=G$，$GC,EG\subset$ 平面 $CEG$，得 $BF\perp$ 平面 $CEG$；" "\n"
        r"又 $BF\subset$ 平面 $BCF$，$\therefore\boxed{\text{平面 }CEG\perp\text{平面 }CFB}$．" "\n"
        r"**（Ⅲ）** 由（Ⅱ）$GC\perp$ 平面 $ABEF$，而 $GE\subset$ 平面 $ABEF$，故 $GC\perp GE$，" "\n"
        r"$S_{\triangle GCE}=\dfrac12\times GC\times GE=\dfrac12\times\sqrt3\times\sqrt3=\dfrac32$"
        r"（菱形 $GBEF$ 中 $\angle GBE=60^\circ$，故 $GE=2\sqrt3\sin30^\circ=\sqrt3$）．" "\n"
        r"多面体 $AFEBCD$ 可拆成三棱柱 $ADF-GCE$ 与三棱锥 $B-GCE$：" "\n"
        r"由 $AF\paralleleq EG$（四边形 $AFEG$ 为平行四边形）且 $AD\paralleleq GC$ 知 $ADF-GCE$ 是三棱柱，"
        r"其高为 $FO=\dfrac{BF}2=\dfrac32$（$BF=2\sqrt3\cos30^\circ=3$，$O$ 为菱形对角线交点）；" "\n"
        r"由（Ⅱ）$BF\perp$ 平面 $GCE$，而 $B$ 在 $BF$ 上，故 $BO=\dfrac32$ 是三棱锥 $B-GCE$ 的高．" "\n"
        r"$V=V_{ADF-GCE}+V_{B-GCE}=S_{\triangle GCE}\cdot FO+\dfrac13S_{\triangle GCE}\cdot BO$" "\n"
        r"$=\dfrac32\times\dfrac32+\dfrac13\times\dfrac32\times\dfrac32=\dfrac94+\dfrac34=\boxed3$．"
    ),
    'review': (
        r"① ⭐⭐ **两个「平行四边形」撑起全题**：$CDFE$ 给出 $CE\parallel DF$（证线面平行），"
        r"$GBEF$ 不仅是平行四边形还是菱形（$GB=BE=\sqrt3$）⟹ $BF\perp EG$（证面面垂直的关键一条）．" "\n"
        r"② ⭐⭐ **$GC\perp$ 平面 $ABEF$ 是第二次使用「面面垂直」**："
        r"先把 $AD\perp AB$ 平移成 $GC\perp AB$，再配两面垂直交线 $AB$ 即得．"
        r"于是 $GC\perp BF$，与 $EG\perp BF$ 凑齐两条相交直线 ⟹ $BF\perp$ 平面 $CEG$．" "\n"
        r"③ ⭐ **（Ⅲ）的拆法是「三棱柱 + 三棱锥」**："
        r"$V_{\text{柱}}=S\cdot FO$（注意三棱柱体积是底面积乘高，不乘 $\frac13$），"
        r"$V_{\text{锥}}=\frac13S\cdot BO$；两者都用同一个 $S_{\triangle GCE}=\frac32$，"
        r"且 $FO=BO=\frac32$（$O$ 是菱形对角线中点）．" "\n"
        r"④ 数值复核（建系 $A(0,0,0),B(2\sqrt3,0,0),D(0,\sqrt3,0),C(\sqrt3,\sqrt3,0)$，"
        r"$F(\frac{\sqrt3}2,0,\frac32),E(\frac{3\sqrt3}2,0,\frac32),G(\sqrt3,0,0)$）：" "\n"
        r"   $S_{\triangle GCE}=\frac12\left|\vec{GC}\times\vec{GE}\right|"
        r"=\frac12\left|\left(\frac{3\sqrt3}2,0,-\frac32\right)\right|=\frac12\times3=1.5$ ✓" "\n"
        r"   $V_{\text{柱}}=\left|\left(\vec{AD}\times\vec{AF}\right)\cdot\vec{AG}\right|"
        r"/2=\frac92/2=2.25$ ✓；$V_{\text{锥}}=\frac{\left|\det\right|}6=\frac{4.5}6=0.75$ ✓；合计 $3$ ✓" "\n"
        r"⑤ ⚠ 原书答案 `3` 无误，但详解中「$S_{\triangle GCE}=\frac12\times\sqrt3\times\sqrt3$」"
        r"的两个 $\sqrt3$ 在提取时都丢了根号（写成 `3`），录入时已还原．" "\n"
        r"**通法（两个互相垂直的平面 + 多面体割补）**：" "\n"
        r"① 平行的两条线段等长 ⟹ 平行四边形；邻边再相等 ⟹ 菱形 ⟹ 对角线垂直；" "\n"
        r"② 两平面垂直时，把某一面内的垂线平移到需要的方向，即可得线面垂直；" "\n"
        r"③ 不规则多面体优先拆成「棱柱 + 棱锥」，并用同一个三角形做底．"
    ),
    'difficulty': 0.78,
    'topics': ['M-T-323'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-323-E1',
}

T324_E1 = {
    'type': '解答',
    'stem_text': (
        r"如图，在四棱锥 $P-ABCD$ 中，底面 $ABCD$ 为菱形，$\triangle PAD$ 为正三角形，"
        r"平面 $PAD\perp$ 平面 $ABCD$，$E$、$F$ 分别是 $AD$、$CD$ 的中点．" "\n"
        r"（1）证明：$BD\perp$ 平面 $PEF$；" "\n"
        r"（2）若 $M$ 是 $PB$ 棱上一点，三棱锥 $M-PAD$ 与三棱锥 $P-DEF$ 的体积相等，"
        r"求 $\dfrac{PM}{MB}$ 的值．"
    ),
    'stem': [
        r"如图，在四棱锥 $P-ABCD$ 中，底面 $ABCD$ 为菱形，$\triangle PAD$ 为正三角形，"
        r"平面 $PAD\perp$ 平面 $ABCD$，$E$、$F$ 分别是 $AD$、$CD$ 的中点．",
        r"（1）证明：$BD\perp$ 平面 $PEF$；",
        r"（2）若 $M$ 是 $PB$ 棱上一点，三棱锥 $M-PAD$ 与三棱锥 $P-DEF$ 的体积相等，"
        r"求 $\dfrac{PM}{MB}$ 的值．",
    ],
    'opts': [],
    'answer': r"（1）证明见解析；（2）$\dfrac{PM}{MB}=\dfrac13$",
    'analysis': (
        r"（1）正三角形 $PAD$ 的中线 $PE\perp AD$，配面面垂直得 $PE\perp$ 底面，故 $BD\perp PE$；"
        r"又 $EF$ 是 $\triangle ACD$ 的中位线，$EF\parallel AC$，而菱形中 $BD\perp AC$，故 $BD\perp EF$．" "\n"
        r"（2）把两个体积都用 $V_{P-ABD}$ 表示：$V_{P-DEF}=\dfrac14V_{P-ABD}$，"
        r"$V_{M-PAD}=\dfrac{PM}{PB}V_{P-ABD}$．"
    ),
    'solution': (
        r"**（1）证明** 连接 $AC$．$\because PA=PD$ 且 $E$ 是 $AD$ 的中点，"
        r"$\therefore PE\perp AD$．" "\n"
        r"又平面 $PAD\perp$ 平面 $ABCD$、交线 $AD$、$PE\subset$ 平面 $PAD$，"
        r"$\therefore PE\perp$ 平面 $ABCD$．" "\n"
        r"而 $BD\subset$ 平面 $ABCD$，故 $BD\perp PE$．" "\n"
        r"在 $\triangle ACD$ 中，$E,F$ 分别是 $AD,CD$ 的中点，故 $EF$ 为中位线，$EF\parallel AC$；" "\n"
        r"底面 $ABCD$ 为菱形，故 $BD\perp AC$，从而 $BD\perp EF$．" "\n"
        r"由 $PE\cap EF=E$，$PE,EF\subset$ 平面 $PEF$，$\therefore\boxed{BD\perp\text{平面 }PEF}$．" "\n"
        r"**（2）** 设 $\dfrac{PM}{MB}=\lambda$，则 $\dfrac{PM}{PB}=\dfrac{\lambda}{\lambda+1}$．" "\n"
        r"$M$ 到平面 $PAD$ 的距离等于 $B$ 到平面 $PAD$ 距离的 $\dfrac{PM}{PB}$ 倍，故" "\n"
        r"$V_{M-PAD}=\dfrac{\lambda}{\lambda+1}V_{B-PAD}=\dfrac{\lambda}{\lambda+1}V_{P-ABD}$．" "\n"
        r"另一方面，$F$ 是 $CD$ 的中点、$E$ 是 $AD$ 的中点，故" "\n"
        r"$S_{\triangle DEF}=\dfrac12\cdot DE\cdot d\left(F,AD\right)"
        r"=\dfrac12\cdot\dfrac{AD}2\cdot\dfrac{d\left(C,AD\right)}2=\dfrac14S_{\triangle ACD}$，" "\n"
        r"于是 $V_{P-DEF}=\dfrac14V_{P-ACD}=\dfrac14V_{P-ABD}$（菱形中 $S_{\triangle ACD}=S_{\triangle ABD}$）．" "\n"
        r"由 $V_{M-PAD}=V_{P-DEF}$ 得 $\dfrac{\lambda}{\lambda+1}=\dfrac14$，"
        r"解得 $\lambda=\boxed{\dfrac13}$，即 $\dfrac{PM}{MB}=\dfrac13$．"
    ),
    'review': (
        r"① ⭐⭐ **正三角形 + 中点 ⟹ $PE\perp AD$**，配面面垂直即 $PE\perp$ 底面 —— "
        r"这一步同时给出（1）的一条垂线和（2）中「$B$ 到平面 $PAD$ 的距离」的可加性．" "\n"
        r"② ⭐⭐ **（2）的核心是「两个体积都化到 $V_{P-ABD}$」**："
        r"$V_{M-PAD}=\frac{\lambda}{\lambda+1}V_{P-ABD}$（同底面 $PAD$，高按 $PM:PB$ 缩放），"
        r"$V_{P-DEF}=\frac14V_{P-ABD}$（底面面积是 $\frac14$，高相同）．"
        r"化到同一个基准后，$V_{P-ABD}$ 直接约掉，完全不用算具体数值．" "\n"
        r"③ ⭐ **面积比 $\frac14$ 的来源是两次「减半」**："
        r"$DE=\frac{AD}2$（$E$ 是中点）与 $d\left(F,AD\right)=\frac12d\left(C,AD\right)$（$F$ 是中点），"
        r"两个 $\frac12$ 相乘得 $\frac14$，不是 $\frac12$．" "\n"
        r"④ ⚠ **$\frac{PM}{PB}=\frac{\lambda}{\lambda+1}$ 不要写成 $\frac{\lambda}{1}$**："
        r"$PM:MB=\lambda:1$，故 $PM:PB=\lambda:\left(\lambda+1\right)$．" "\n"
        r"⑤ 数值复核（取菱形边长 $2$、$\angle BAD=60^\circ$）："
        r"$S_{\triangle ABD}=\sqrt3$，$S_{\triangle ACD}=\sqrt3$；"
        r"$S_{\triangle DEF}=\frac{\sqrt3}4$，即 $\frac14S_{\triangle ACD}$ ✓" "\n"
        r"   $\lambda=\frac13$ 时 $\frac{\lambda}{\lambda+1}=\frac{1/3}{4/3}=\frac14$ ✓ 与 $V_{P-DEF}$ 的系数一致．" "\n"
        r"**通法（体积相等的动点定位）**：" "\n"
        r"① 把两个体积都表示成「某个公共三棱锥 × 系数」，公共量自动约掉；" "\n"
        r"② 系数来自两处：底面面积的比值（用中点/比例线段算）、高的比值（用线段比算）；" "\n"
        r"③ 点在棱上时，$\frac{PM}{MB}=\lambda\iff\frac{PM}{PB}=\frac{\lambda}{\lambda+1}$．"
    ),
    'difficulty': 0.70,
    'topics': ['M-T-324'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-324-E1',
}

T324_V1 = {
    'type': '解答',
    'stem_text': (
        r"（2020·山西·怀仁市大地学校高中部高二阶段练习（理））如图，$ABCD$ 是边长为 $a$ 的正方形，"
        r"$DE\perp$ 平面 $ABCD$，$AF\perp$ 平面 $ABCD$，$DE=3AF=3$．" "\n"
        r"（1）证明：平面 $ABF\parallel$ 平面 $DCE$；" "\n"
        r"（2）在 $DE$ 上是否存在一点 $G$，使平面 $FBG$ 将几何体 $ABCDEF$ 分成上下两部分的"
        r"体积比为 $3:11$？若存在，求出 $G$ 的位置；若不存在，说明理由．"
    ),
    'stem': [
        r"（2020·山西·怀仁市大地学校高中部高二阶段练习（理））如图，$ABCD$ 是边长为 $a$ 的正方形，"
        r"$DE\perp$ 平面 $ABCD$，$AF\perp$ 平面 $ABCD$，$DE=3AF=3$．",
        r"（1）证明：平面 $ABF\parallel$ 平面 $DCE$；",
        r"（2）在 $DE$ 上是否存在一点 $G$，使平面 $FBG$ 将几何体 $ABCDEF$ 分成上下两部分的"
        r"体积比为 $3:11$？若存在，求出 $G$ 的位置；若不存在，说明理由．",
    ],
    'opts': [],
    'answer': r"（1）证明见解析；（2）存在，点 $G$ 满足 $EG=1$",
    'analysis': (
        r"（1）$DE\parallel AF$ 且 $AB\parallel CD$，两组相交直线分别平行即得面面平行．" "\n"
        r"（2）设 $EG=t$，把「上半部分」拆成两个三棱锥 $B-EGM$ 与 $B-EFG$（$M$ 由 $MG\parallel BF$ 定出），"
        r"其体积分别是 $\dfrac{a^2t^2}{12}$ 与 $\dfrac{a^2t}6$；再由总体积 $\dfrac{7a^2}6$ 与比值 $3:11$ 列方程．"
    ),
    'solution': (
        r"**（1）证明** $\because DE\perp$ 平面 $ABCD$，$AF\perp$ 平面 $ABCD$，$\therefore DE\parallel AF$．" "\n"
        r"又 $AF\not\subset$ 平面 $DCE$，$DE\subset$ 平面 $DCE$，故 $AF\parallel$ 平面 $DCE$．" "\n"
        r"$\because ABCD$ 是正方形，$\therefore AB\parallel CD$；同理得 $AB\parallel$ 平面 $DCE$．" "\n"
        r"又 $AB\cap AF=A$，$AB,AF\subset$ 平面 $ABF$，$\therefore\boxed{\text{平面 }ABF\parallel\text{平面 }DCE}$．" "\n"
        r"**（2）** 建系 $A\left(0,0,0\right)$、$B\left(a,0,0\right)$、$C\left(a,a,0\right)$、$D\left(0,a,0\right)$、"
        r"$F\left(0,0,1\right)$、$E\left(0,a,3\right)$．" "\n"
        r"把几何体按「不含 $B$ 的面」拆成三个四面体，算得 $V_{ABCDEF}=\dfrac{7a^2}6$（见复核）．" "\n"
        r"由体积比 $3:11$，上半部分（含 $E$ 的那块）体积为" "\n"
        r"$V_{\text{上}}=\dfrac3{3+11}V_{ABCDEF}=\dfrac3{14}\times\dfrac{7a^2}6=\dfrac{a^2}4$．" "\n"
        r"设 $EG=t$（$0\le t\le3$），则 $G\left(0,a,3-t\right)$．" "\n"
        r"过 $G$ 作 $MG\parallel BF$ 交 $EC$ 于 $M$：由 $\vec{BF}=\left(-a,0,1\right)$ 与"
        r"$M=G+s\vec{BF}=E+u\left(C-E\right)$ 联立得 $s=-\dfrac t2$、$u=\dfrac t2$，" "\n"
        r"故 $M\left(\dfrac{ta}2,\ a,\ 3-\dfrac{3t}2\right)$，且因 $GM\parallel BF$ 知 $M$ 在平面 $BFG$ 内．" "\n"
        r"于是上半部分由两个四面体 $B-EFG$ 与 $B-EGM$ 拼成，用行列式计算：" "\n"
        r"$V_{B-EFG}=\dfrac16\left|\det\left(\vec{BE},\vec{BF},\vec{BG}\right)\right|"
        r"=\dfrac16\left|-a^2t\right|=\dfrac{a^2t}6$；" "\n"
        r"$V_{B-EGM}=\dfrac16\left|\det\left(\vec{BE},\vec{BG},\vec{BM}\right)\right|"
        r"=\dfrac16\left|-\dfrac{a^2t^2}2\right|=\dfrac{a^2t^2}{12}$．" "\n"
        r"故 $\dfrac{a^2t^2}{12}+\dfrac{a^2t}6=\dfrac{a^2}4$，即 $t^2+2t=3$，"
        r"解得 $t=1$ 或 $t=-3$（舍）．" "\n"
        r"$\therefore$ 存在点 $G$，且 $\boxed{EG=1}$（即 $G$ 为 $DE$ 上靠近 $E$ 的三等分点）．"
    ),
    'review': (
        r"① ⭐⭐ **（1）的「两组相交直线分别平行」**：$AF\parallel DE$（同垂直于一个平面）"
        r"与 $AB\parallel CD$（正方形对边），两条相交直线 $AB,AF$ 都在平面 $ABF$ 内，一步得面面平行．" "\n"
        r"② ⭐⭐ **（2）的「总体积 × 比值 = 部分体积」是关键中转**："
        r"$V_{\text{上}}=\frac3{14}\times\frac{7a^2}6=\frac{a^2}4$，数字恰好很整 —— "
        r"$\frac{7a^2}6$ 中的 $7$ 与 $14$ 约成 $2$，$3\times\frac{7}{14}=\frac32$，"
        r"$\frac32\times\frac16=\frac14$．这种「算出来很整」通常是做法正确的信号．" "\n"
        r"③ ⭐ **方程 $t^2+2t=3$ 的两根是 $1$ 与 $-3$**：出现一次项与二次项是因为"
        r"$V_{B-EGM}$ 随 $t$ **二次**增长（$GM$ 与高都随 $t$ 变），而 $V_{B-EFG}$ 随 $t$ **一次**增长．" "\n"
        r"④ 数值复核（取 $a=2$）：$V_{ABCDEF}=\frac{7\times4}6=4.6667$；" "\n"
        r"   直接用三个四面体验证：$V\left(A,C,D,E\right)=\frac{3a^2}6=2$、"
        r"$V\left(A,B,C,E\right)=2$、$V\left(A,B,E,F\right)=\frac{a^2}6=0.6667$，合计 $4.6667$ ✓" "\n"
        r"   $t=1$ 时：$G\left(0,2,2\right)$，$V\left(B,E,F,G\right)=\frac{a^2}6=0.6667$、"
        r"$V\left(B,E,G,M\right)=\frac{a^2}{12}=0.3333$，合计 $1.0000=\frac{a^2}4$ ✓" "\n"
        r"   比值：$1.0000:\left(4.6667-1.0000\right)=1:3.6667=3:11$ ✓" "\n"
        r"⑤ ⚠ 原书答案 `EG = 1` 中的「1」是长度（$DE=3$ 故 $EG=1$ 即 $EG:GD=1:2$），"
        r"不是比例 $1:3$，读题时注意 $DE=3AF=3$ 已经把 $AF$ 定成 $1$、$DE$ 定成 $3$．" "\n"
        r"**通法（探索性「体积比定点的位置」）**：" "\n"
        r"① 先算整体体积（拆成四面体，用行列式最稳）；" "\n"
        r"② 由比值求出目标部分的体积；" "\n"
        r"③ 设参数 $t$，用过该点作平行线把截面补成两个三棱锥，列方程；" "\n"
        r"④ 负根舍去后要确认 $t$ 落在棱长范围内．"
    ),
    'difficulty': 0.80,
    'topics': ['M-T-324'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-324-V1',
}

T326_E1 = {
    'type': '解答',
    'stem_text': (
        r"（2021·黑龙江·哈尔滨三中高一期末）如图，三棱锥 $A-BCD$ 中，侧面 $\triangle ABD$ 是边长为 $2$ 的"
        r"正三角形，$AC=2CD=2$，平面 $ABD\perp$ 平面 $BCD$，把平面 $ACD$ 沿 $CD$ 旋转至平面 $PCD$ 的位置，"
        r"记点 $A$ 旋转后对应的点为 $P$（不在平面 $BCD$ 内），$M$、$N$ 分别是 $BD$、$CD$ 的中点．" "\n"
        r"（1）求证：$CD\perp MN$；" "\n"
        r"（2）求三棱锥 $C-APD$ 的体积的最大值．"
    ),
    'stem': [
        r"（2021·黑龙江·哈尔滨三中高一期末）如图，三棱锥 $A-BCD$ 中，侧面 $\triangle ABD$ 是边长为 $2$ 的"
        r"正三角形，$AC=2CD=2$，平面 $ABD\perp$ 平面 $BCD$，把平面 $ACD$ 沿 $CD$ 旋转至平面 $PCD$ 的位置，"
        r"记点 $A$ 旋转后对应的点为 $P$（不在平面 $BCD$ 内），$M$、$N$ 分别是 $BD$、$CD$ 的中点．",
        r"（1）求证：$CD\perp MN$；",
        r"（2）求三棱锥 $C-APD$ 的体积的最大值．",
    ],
    'opts': [],
    'answer': r"（1）证明见解析；（2）$\dfrac58$",
    'analysis': (
        r"（1）由 $AB=AD$、$M$ 为 $BD$ 中点得 $AM\perp BD$，配面面垂直得 $AM\perp$ 平面 $BCD$；"
        r"由 $AC=2$、$AM=\sqrt3$ 得 $MC=1$，而 $MB=MD=1$，故 $\angle BCD=90^\circ$；"
        r"再由中位线 $MN\parallel BC$ 得 $CD\perp MN$．" "\n"
        r"（2）三棱锥 $C-APD$ 即 $P-ACD$，$\triangle ACD$ 面积固定，故只需最大化 $P$ 到平面 $ACD$ 的距离，"
        r"即旋转角为 $90^\circ$（平面 $PCD\perp$ 平面 $ACD$）时取到．"
    ),
    'solution': (
        r"**（1）证明** 连接 $AM,MC$．$\because AB=AD$ 且 $M$ 是 $BD$ 的中点，$\therefore AM\perp BD$．" "\n"
        r"又平面 $ABD\perp$ 平面 $BCD$、交线 $BD$、$AM\subset$ 平面 $ABD$，"
        r"$\therefore AM\perp$ 平面 $BCD$，从而 $AM\perp MC$．" "\n"
        r"$\triangle ABD$ 是边长为 $2$ 的正三角形，故 $AM=\sqrt3$；又 $AC=2$，"
        r"由勾股定理 $MC=\sqrt{AC^2-AM^2}=\sqrt{4-3}=1$．" "\n"
        r"而 $MB=MD=\dfrac{BD}2=1$，故 $\triangle BCD$ 中 $M$ 是 $BD$ 中点且 $MC=\dfrac{BD}2$，"
        r"$\therefore\angle BCD=90^\circ$，即 $BC\perp CD$．" "\n"
        r"又 $M,N$ 分别是 $BD,CD$ 的中点，故 $MN$ 是 $\triangle DBC$ 的中位线，$MN\parallel BC$．" "\n"
        r"$\therefore\boxed{CD\perp MN}$．" "\n"
        r"**（2）** 三棱锥 $C-APD$ 与三棱锥 $P-ACD$ 是同一个三棱锥，且 $\triangle ACD$ 的面积为定值，"
        r"故体积最大 $\iff$ $P$ 到平面 $ACD$ 的距离最大．" "\n"
        r"$P$ 由 $A$ 绕轴 $CD$ 旋转得到，故 $P$ 到直线 $CD$ 的距离恒等于 $A$ 到 $CD$ 的距离；"
        r"当平面 $PCD\perp$ 平面 $ACD$ 时该距离全部转化为到平面 $ACD$ 的距离，此时最大．" "\n"
        r"取 $CD$ 的中点 $N$，由 $AC=AD=2$ 得 $AN\perp CD$，且" "\n"
        r"$AN=\sqrt{AC^2-CN^2}=\sqrt{4-\dfrac14}=\dfrac{\sqrt{15}}2$．" "\n"
        r"平面 $PCD\perp$ 平面 $ACD$ 时 $PN\perp$ 平面 $ACD$，且 $PN=AN=\dfrac{\sqrt{15}}2$．" "\n"
        r"$S_{\triangle ACD}=\dfrac12\cdot CD\cdot AN=\dfrac12\times1\times\dfrac{\sqrt{15}}2=\dfrac{\sqrt{15}}4$．" "\n"
        r"$\therefore V_{\max}=\dfrac13S_{\triangle ACD}\cdot PN"
        r"=\dfrac13\times\dfrac{\sqrt{15}}4\times\dfrac{\sqrt{15}}2=\dfrac{15}{24}=\boxed{\dfrac58}$．"
    ),
    'review': (
        r"① ⭐⭐ **$MC=1$ 是本题的题眼**：由 $AM=\sqrt3$、$AC=2$ 勾股得 $MC=1$，"
        r"恰好等于 $MB=MD=1$，于是 $M$ 是 $\triangle BCD$ 的外心 ⟹ $\angle BCD=90^\circ$ ⟹ $BC\perp CD$．"
        r"这一串推导把「两平面垂直」和「线线垂直」接了起来．" "\n"
        r"② ⭐⭐ **（2）把「旋转最值」翻译成「点到直线距离全部转化为点到平面距离」**："
        r"$P$ 绕 $CD$ 旋转时到 $CD$ 的距离不变（$=\frac{\sqrt{15}}2$），"
        r"到平面 $ACD$ 的距离 $=$ 该距离 $\times\left|\sin\theta\right|$，$\theta=90^\circ$ 时最大．" "\n"
        r"③ ⭐ **$PN=AN$ 是旋转不变量**（$N$ 在转轴 $CD$ 上），"
        r"而 $PN\perp$ 平面 $ACD$ 只在两面垂直时成立 —— 两个条件要分开说．" "\n"
        r"④ 数值复核（建系 $C(0,0,0),D(1,0,0),B(0,\sqrt3,0)$）："
        r"$M\left(0.5,0.8660,0\right)$，$A=M+\left(0,0,\sqrt3\right)=\left(0.5,0.8660,1.7321\right)$；" "\n"
        r"   $AB^2=0.25+0.75+3=4$ ✓、$AD^2=0.25+0.75+3=4$ ✓、$AC^2=0.25+0.75+3=4$ ✓" "\n"
        r"   $A$ 到 $x$ 轴（即 $CD$）距离 $=\sqrt{0.75+3}=1.9365=\frac{\sqrt{15}}2$ ✓" "\n"
        r"   $S_{\triangle ACD}=0.5\times1\times1.9365=0.9682=\frac{\sqrt{15}}4$ ✓，" "\n"
        r"   $V=\frac13\times0.9682\times1.9365=0.6250=\frac58$ ✓" "\n"
        r"⑤ ⚠ 题干 $AC=2CD=2$ 表示 $AC=2$ 且 $CD=1$，不要读成 $AC=2CD$ 且 $2CD=2$ 之外的意思；"
        r"由此 $AD=AB=BD=2$（正三角形）、$AC=2$、$CD=1$，三边齐全．" "\n"
        r"**通法（旋转体中的体积最值）**：" "\n"
        r"① 先定「旋转轴」，轴上点到被转点的距离不变；" "\n"
        r"② 把所求体积写成「定值底面 × 动高」，动高 $=$ 到轴的距离 $\times\left|\sin\theta\right|$；" "\n"
        r"③ $\theta=90^\circ$（即旋转后的平面垂直于原平面）时取最大值．"
    ),
    'difficulty': 0.76,
    'topics': ['M-T-326'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-326-E1',
}

T326_V2 = {
    'type': '解答',
    'stem_text': (
        r"（2020·重庆·模拟预测（文））如图所示，在矩形 $ABCD$ 中，$AB=2BC=2$，$E$ 为边 $AB$ 的中点，"
        r"将 $\triangle ADE$ 沿直线 $DE$ 翻折为 $\triangle A'DE$，若 $F$ 为线段 $A'C$ 的中点．"
        r"在 $\triangle ADE$ 翻折过程中，" "\n"
        r"（Ⅰ）求证：$BF\parallel$ 平面 $A'DE$；" "\n"
        r"（Ⅱ）求多面体 $CDEF$ 体积的最大值．"
    ),
    'stem': [
        r"（2020·重庆·模拟预测（文））如图所示，在矩形 $ABCD$ 中，$AB=2BC=2$，$E$ 为边 $AB$ 的中点，"
        r"将 $\triangle ADE$ 沿直线 $DE$ 翻折为 $\triangle A'DE$，若 $F$ 为线段 $A'C$ 的中点．"
        r"在 $\triangle ADE$ 翻折过程中，",
        r"（Ⅰ）求证：$BF\parallel$ 平面 $A'DE$；",
        r"（Ⅱ）求多面体 $CDEF$ 体积的最大值．",
    ],
    'opts': [],
    'answer': r"（Ⅰ）证明见解析；（Ⅱ）$\dfrac{\sqrt2}{12}$",
    'analysis': (
        r"（Ⅰ）取 $CD$ 中点 $G$，$GF$ 是 $\triangle CA'D$ 的中位线故 $GF\parallel A'D$；"
        r"又 $DG\paralleleq BE$ 故 $BG\parallel DE$；两组平行推出平面 $BFG\parallel$ 平面 $A'DE$．" "\n"
        r"（Ⅱ）多面体 $CDEF$ 即三棱锥 $F-CDE$，$\triangle CDE$ 面积固定，"
        r"故只需最大化 $F$ 到底面的距离；$F$ 是 $A'C$ 中点，其距离是 $A'$ 的一半，"
        r"而 $A'$ 到底面距离在平面 $A'DE\perp$ 底面时最大，为 $A'O=\dfrac{\sqrt2}2$（$O$ 为 $DE$ 中点）．"
    ),
    'solution': (
        r"**（Ⅰ）证明** 取 $CD$ 的中点 $G$，连接 $FG,BG$．" "\n"
        r"$\because F$ 是 $A'C$ 的中点，$G$ 是 $CD$ 的中点，$\therefore GF$ 是 $\triangle CA'D$ 的中位线，"
        r"$GF\parallel A'D$．" "\n"
        r"又 $GF\not\subset$ 平面 $A'DE$，$A'D\subset$ 平面 $A'DE$，故 $GF\parallel$ 平面 $A'DE$．" "\n"
        r"由 $AB=2$、$E$ 为 $AB$ 中点得 $AE=EB=1$；又 $CD=2$、$G$ 为 $CD$ 中点得 $DG=1$，"
        r"且 $DG\parallel BE$，故四边形 $BEDG$ 为平行四边形，$BG\parallel DE$．" "\n"
        r"同理 $BG\parallel$ 平面 $A'DE$．" "\n"
        r"又 $BG\cap GF=G$，$\therefore$ 平面 $BFG\parallel$ 平面 $A'DE$，"
        r"而 $BF\subset$ 平面 $BFG$，$\therefore\boxed{BF\parallel\text{平面 }A'DE}$．" "\n"
        r"**（Ⅱ）** 多面体 $CDEF$ 只有四个顶点，即三棱锥 $F-CDE$．" "\n"
        r"$S_{\triangle CDE}=\dfrac12\times CD\times BC=\dfrac12\times2\times1=1$（定值）．" "\n"
        r"$F$ 是 $A'C$ 的中点且 $C$ 在底面内，故 $d\left(F,\text{底面}\right)"
        r"=\dfrac12\,d\left(A^{\prime},\text{底面}\right)$．" "\n"
        r"翻折中 $A'D=AD=1$、$A'E=AE=1$ 恒定，$DE=\sqrt{1+1}=\sqrt2$ 也恒定．"
        r"设 $O$ 为 $DE$ 中点，则 $A'O\perp DE$ 且" "\n"
        r"$A'O=\sqrt{A'D^2-\left(\dfrac{DE}2\right)^2}=\sqrt{1-\dfrac12}=\dfrac{\sqrt2}2$（定值）．" "\n"
        r"$A'$ 到底面 $BCD$ 的距离 $=A'O\cdot\left|\sin\theta\right|$，$\theta$ 为平面 $A'DE$ 与底面的二面角，"
        r"当 $\theta=90^\circ$（即平面 $A'DE\perp$ 底面 $BCD$）时最大，最大值为 $\dfrac{\sqrt2}2$．" "\n"
        r"$\therefore V_{\max}=\dfrac13S_{\triangle CDE}\times\dfrac12\times\dfrac{\sqrt2}2"
        r"=\dfrac13\times1\times\dfrac{\sqrt2}4=\boxed{\dfrac{\sqrt2}{12}}$．"
    ),
    'review': (
        r"① ⭐⭐ **（Ⅰ）的「两次中位线 + 面面平行」**：$GF\parallel A'D$（$\triangle CA'D$ 中位线）"
        r"与 $BG\parallel DE$（平行四边形 $BEDG$），两条相交直线都在平面 $BFG$ 内 ⟹ 面面平行 ⟹ 线面平行．"
        r"注意 $G$ 必须取 $CD$ 中点，才能同时满足两个平行关系．" "\n"
        r"② ⭐⭐ **（Ⅱ）的「$F$ 是中点 ⟹ 距离减半」**：$F$ 在 $A'C$ 上且 $C$ 在底面内，"
        r"故 $F$ 到底面的距离恰是 $A'$ 的一半 —— 这一步把动点 $F$ 的距离问题整个归到 $A'$ 上．" "\n"
        r"③ ⭐ **$A'O=\frac{\sqrt2}2$ 是定值不是最大值**：$A'D=A'E=1$ 恒定，"
        r"故 $A'$ 到 $DE$ 的距离 $A'O=\frac{\sqrt2}2$ 恒定；变的只是它「竖起来」的程度，"
        r"$\theta=90^\circ$ 时全部转化为到底面的距离．" "\n"
        r"④ 数值复核（建系 $D(0,0,0),C(2,0,0),B(2,1,0),A(0,1,0),E(1,1,0)$）：" "\n"
        r"   $DE=\sqrt2$，$O\left(0.5,0.5,0\right)$，$A'O=\frac{\sqrt2}2=0.7071$；"
        r"当面 $A'DE\perp$ 底面时 $A'=\left(0.5,0.5,\frac{\sqrt2}2\right)$（在 $DE$ 的中垂面上抬高）；" "\n"
        r"   $F=\frac{A'+C}2=\left(1.25,0.25,\frac{\sqrt2}4\right)$，$d\left(F,\text{底面}\right)=\frac{\sqrt2}4=0.3536$ ✓" "\n"
        r"   $V=\frac13\times1\times0.3536=0.1179=\frac{\sqrt2}{12}=0.1179$ ✓" "\n"
        r"⑤ ⚠ 原书答案 `2/12` 是 $\frac{\sqrt2}{12}$ 丢了根号；"
        r"判据：若按 $\frac2{12}=\frac16$，则要求 $F$ 到底面距离为 $\frac12$，"
        r"而实际最大只有 $\frac{\sqrt2}4\approx0.354<\frac12$，不可能．" "\n"
        r"**通法（翻折过程中的体积最值）**：" "\n"
        r"① 先认准「不变的长度」：$A'D=AD$、$A'E=AE$、$DE$ 都不变；" "\n"
        r"② 由等腰三角形底边中点得「到转轴的距离」为定值；" "\n"
        r"③ 到底面的距离 $=$ 该定值 $\times\left|\sin\theta\right|$，$\theta=90^\circ$ 时最大；" "\n"
        r"④ 若体积涉及中点，善用「距离减半」．"
    ),
    'difficulty': 0.74,
    'topics': ['M-T-326'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-326-V2',
}

QS = [
    T320_E1, T320_V1, T320_V2,
    T321_E1, T321_V1,
    T322_E1, T322_V1,
    T323_E1,
    T324_E1, T324_V1,
    T326_E1, T326_V2,
]
