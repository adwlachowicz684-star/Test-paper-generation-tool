# -*- coding: utf-8 -*-
r"""第 126 批（第二组）：立体几何 4 + 圆锥曲线 3，共 7 题。

    python3 tools/run_batch.py 126b

## 选题依据

接续 input_batch126a.py，取剩余 A/B 级可录题，落在 p257/p278/p285/p288/p307/p328/p347。

## ★★ 本批最值钱的一条：三棱台的「补形成锥」坐标法（M-T-313-V1，详解原书缺失）

三棱台给的是**上、下底平行且相似**，所以侧棱延长必交于一点 $S$。由 $\frac{A_1C_1}{AC}=\frac12$ 知
$A_1$ 是 $SA$ 的中点，于是

$$S=2A_1-A,\qquad B_1=\frac{S+B}2$$

**$B_1$ 的坐标不需要另外的条件，直接由棱台性质推出** —— 这是本题能建系求解的关键。

> ⭐⭐ 凡三棱台（棱锥被平行平面所截）求坐标，都用「$S$ 是位似中心」：
> $\vec{CB_1}=\frac12\vec{CB}+\frac12\vec{CS}$，先由已知顶点反求 $S$，再定其余顶点。

## ★★ 第二条：折叠体中「$PD\perp DE$ ⟹ 旋转半径就是 $PD$」（M-T-316-V2，详解原书缺失）

$\triangle PDE$ 中算出 $PD^2+DE^2=PE^2$ ⟹ $\angle PDE=90°$。折起时 $P'$ 绕 $DE$ 旋转，
**旋转半径 $=PD$（不是 $PE$）**，且 $DA$ 也在垂直于 $DE$ 的平面内，故可设 $\phi=\angle P'DA$：

$$h=\sqrt2\sin\phi,\qquad |P'A|=2\sqrt2\sin\frac\phi2,\qquad
\sin30^\circ=\frac h{|P'|A|}=\cos\frac\phi2\ \Longrightarrow\ \phi=120^\circ$$

> ⭐⭐ $\frac{\sqrt2\sin\phi}{2\sqrt2\sin\frac\phi2}=\cos\frac\phi2$ —— 半角公式让方程一步解出。
> ⚠ $h=\sqrt2\sin120^\circ=\frac{\sqrt6}2$ **不是** $\frac{\sqrt6}4$（别把 $DP'=\sqrt2$ 记成 $1$）。

## ★★ 第三条：折叠后「公共边垂直」的连线（M-T-309-E1）

沿直径 $AB$ 折起使两个半圆面垂直，交线为 $AB$。凡要跨两个面算长度，就取
「在一个面内作 $AB$ 的垂线」——$DE\perp AB$ 且 $DE\subset$ 面 $ABD$ ⟹ $DE\perp$ 面 $ABC$ ⟹ $DE\perp CE$。

> ⭐⭐ **所有长度都在图 1（折叠前的平面图）里算出**，折起只改变「跨面」的那一步（用 $\perp$ 造直角）。
> 本题 $CE=\frac{\sqrt7}2r$、$CD=\frac{\sqrt{10}}2r$、$CG=\frac{\sqrt{13}}4r$ 全部来自图 1。
"""

T292_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知长方体 $ABCD-A_1B_1C_1D_1$ 中，$AB=BC=\dfrac{BB_1}2$，点 $E$ 在线段 $CC_1$ 上，"
        r"$\dfrac{EC}{CC_1}=\lambda\ (0\le\lambda\le1)$，平面 $\alpha$ 过线段 $AA_1$ 的中点以及点 $B_1,E$，"
        r"若平面 $\alpha$ 截长方体所得截面为平行四边形，则实数 $\lambda$ 的取值范围是（　　）"
    ),
    'opts': [
        ['A', r"$[0,1]$"],
        ['B', r"$\left[\dfrac14,\dfrac12\right]$"],
        ['C', r"$\left[\dfrac12,\dfrac23\right]$"],
        ['D', r"$\left[\dfrac12,1\right]$"],
    ],
    'answer': r"D",
    'analysis': (
        r"设 $AA_1$ 中点为 $M$，平面 $\alpha$ 与 $DD_1$ 交于 $G$。截面 $MGEB_1$ 是平行四边形"
        r"的充要条件是 $MG\parallel EB_1$；随着 $E$ 沿 $CC_1$ 移动，$G$ 沿 $DD_1$ 移动，"
        r"只需找出 $G$ 仍在线段 $DD_1$ 上时 $E$ 的两个临界位置。"
    ),
    'solution': (
        r"设 $AB=BC=\dfrac{BB_1}2=1$，则 $BB_1=2$。设 $AA_1$ 的中点为 $M$，平面 $\alpha$ 与 $DD_1$ 交于点 $G$，连接 $GE$。" "\n"
        r"因为 $M$ 在平面 $ABB_1A_1$ 内、$G$ 在平面 $DCC_1D_1$ 内，而这两个面平行，" "\n"
        r"且 $B_1,E$ 分别在两面上，故截面为四边形 $MGEB_1$。" "\n"
        r"它为平行四边形的充要条件是 $MG\parallel EB_1$（此时 $MG\parallel$ 面 $BCC_1B_1$ 内的 $EB_1$）。" "\n"
        r"由长方体的平移对称性，$MG\parallel EB_1$ 等价于 $G$ 与 $E$ 在竖直方向上「同步」：" "\n"
        r"记 $M$ 的高度为 $1$（$AA_1$ 中点），$B_1$ 的高度为 $2$。" "\n"
        r"当 $G$ 从 $DD_1$ 的中点（高度 $1$）向下运动到 $D$（高度 $0$）时，" "\n"
        r"对应的 $E$ 从 $C_1$（高度 $2$）运动到 $CC_1$ 的中点（高度 $1$）。" "\n"
        r"于是临界状态为：$E$ 与 $C_1$ 重合时 $\lambda=\dfrac{EC}{CC_1}=\dfrac{CC_1}{CC_1}=1$；" "\n"
        r"$E$ 为 $CC_1$ 中点时 $\lambda=\dfrac{EC}{CC_1}=\dfrac12$。" "\n"
        r"所以 $\lambda\in\left[\dfrac12,1\right]$，选 D。"
    ),
    'review': (
        r"① ⭐⭐ **「对面平行 ⟹ 交线平行」**：面 $ABB_1A_1\parallel$ 面 $DCC_1D_1$，" "\n"
        r"故平面 $\alpha$ 与它们的交线 $MB_1$ 与 $GE$ 必然平行 —— 这是截面能成为平行四边形的前提" "\n"
        r"② ⭐⭐ 平行四边形的判定只用 $MG\parallel EB_1$ 一条（另一组对边 $MB_1\parallel GE$ 自动成立）" "\n"
        r"③ ⭐⭐ **两个临界点都要算**：$E$ 在 $C_1$（$\lambda=1$）与 $E$ 在 $CC_1$ 中点（$\lambda=\frac12$）；" "\n"
        r"只算一个会误选 B 或 C" "\n"
        r"④ 📌 题干还原：ref_bank 中 $AB=BC=\frac{BB_1}2$ 被提取为「$AB=BC=BB_1 2$」，" "\n"
        r"由原书详解「设 $AB=BC=\frac{BB_1}{2}=1$，则 $BB_1=2$」判定为 $AB=BC=\frac{BB_1}2$ ✓"
    ),
    'difficulty': 0.7,
    'topics': ['M-T-292'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-292-E1',
}

T309_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知 $AB$、$CD$ 是圆 $O$ 的两条直径，且 $\angle AOC=60^\circ$，如图 1，沿 $AB$ 折起，"
        r"使两个半圆面所在的平面垂直，折到点 $D$ 位置，如图 2．设直线 $BD$ 与直线 $OC$ 所成的角为 $\theta$，则（　　）"
    ),
    'opts': [
        ['A', r"$\angle BDC=90^\circ$ 且 $\theta>60^\circ$"],
        ['B', r"$\angle BDC=90^\circ$ 且 $\theta\le60^\circ$"],
        ['C', r"$\angle BDC\ne90^\circ$ 且 $\theta>60^\circ$"],
        ['D', r"$\angle BDC\ne90^\circ$ 且 $\theta\le60^\circ$"],
    ],
    'answer': r"C",
    'analysis': (
        r"所有长度都在图 1 的平面图中算出：过 $D$ 作 $DE\perp OB$，求出 $CE$、$DE$、$CD$、$BC$；"
        r"折起后两个半圆面垂直，交线为 $AB$，$DE\perp AB$ 且 $DE\subset$ 面 $ABD$，故 $DE\perp$ 面 $ABC$，$DE\perp CE$。"
        r"求 $\theta$ 时作 $OF\parallel BD$，在 $\triangle COF$ 中用余弦定理。"
    ),
    'solution': (
        r"设圆的半径为 $r$。图 1 中过 $D$ 作 $DE\perp OB$ 于 $E$，连接 $CE,AC$。" "\n"
        r"由 $\angle AOC=60^\circ$ 得 $\angle EAC=60^\circ$（同弧），且 $BE=\dfrac r2$，$AE=\dfrac{3r}2$，$AC=r$。" "\n"
        r"在 $\triangle ACE$ 中，$CE=\sqrt{AC^2+AE^2-2AC\cdot AE\cos\angle EAC}$" "\n"
        r"$=\sqrt{r^2+\dfrac{9r^2}4-2\cdot r\cdot\dfrac{3r}2\cdot\dfrac12}=\sqrt{\dfrac{7r^2}4}=\dfrac{\sqrt7}2r$，而 $DE=\dfrac{\sqrt3}2r$。" "\n"
        r"图 2 中两个半圆面所在平面垂直，交线为 $AB$；$DE\perp AB$ 且 $DE\subset$ 面 $ABD$，" "\n"
        r"故 $DE\perp$ 面 $ABC$。又 $CE\subset$ 面 $ABC$，所以 $DE\perp CE$。" "\n"
        r"在 Rt$\triangle CDE$ 中，$CD=\sqrt{CE^2+DE^2}=\sqrt{\dfrac{7r^2}4+\dfrac{3r^2}4}=\dfrac{\sqrt{10}}2r$。" "\n"
        r"又 $DB=r$，$BC=\sqrt3r$，则 $DB^2+CD^2=r^2+\dfrac{10r^2}4=\dfrac{14r^2}4\ne BC^2=3r^2$，故 $\angle BDC\ne90^\circ$。" "\n"
        r"过 $O$ 作 $OF\parallel DB$ 交 $AD$ 于 $F$，则 $F$ 为 $AD$ 中点，连接 $CF$，" "\n"
        r"直线 $BD$ 与直线 $OC$ 所成的角即 $\angle COF=\theta$，且 $OF=\dfrac{BD}2=\dfrac r2$，$OC=r$。" "\n"
        r"过 $F$ 作 $FG\perp AB$ 于 $G$，连接 $CG$。同理 $FG\perp$ 面 $ABC$，故 $FG\perp CG$。" "\n"
        r"在图 1 中，$FG=\dfrac{DE}2=\dfrac{\sqrt3}4r$，$AG=\dfrac{AE}2=\dfrac{3r}4$，$\angle GAC=60^\circ$。" "\n"
        r"在 $\triangle ACG$ 中，$CG=\sqrt{r^2+\dfrac{9r^2}{16}-2\cdot r\cdot\dfrac{3r}4\cdot\dfrac12}=\sqrt{\dfrac{13r^2}{16}}=\dfrac{\sqrt{13}}4r$。" "\n"
        r"图 2 中，在 Rt$\triangle CGF$ 中，$CF=\sqrt{FG^2+CG^2}=\sqrt{\dfrac{3r^2}{16}+\dfrac{13r^2}{16}}=r$。" "\n"
        r"在 $\triangle COF$ 中，$\cos\angle COF=\dfrac{OF^2+OC^2-CF^2}{2\cdot OF\cdot OC}=\dfrac{\frac{r^2}4+r^2-r^2}{2\cdot\frac r2\cdot r}=\dfrac{\frac{r^2}4}{r^2}=\dfrac14$。" "\n"
        r"由 $\dfrac14<\cos60^\circ=\dfrac12$ 且 $\angle COF\in(0,\pi)$ 得 $\angle COF=\theta>60^\circ$。" "\n"
        r"综上，$\angle BDC\ne90^\circ$ 且 $\theta>60^\circ$，选 C。"
    ),
    'review': (
        r"① ⭐⭐ **所有长度都在图 1（平面图）中算**：折起不改变 $\triangle ACE$、$\triangle ACG$ 的形状，" "\n"
        r"只改变「跨面」的关系 —— 所以先把平面图里的量全部算出，再处理垂直" "\n"
        r"② ⭐⭐ **$DE\perp AB$ + 面面垂直 ⟹ $DE\perp$ 面 $ABC$**：这是折叠题的通用桥梁，" "\n"
        r"拿到它就能在任何「跨面直角三角形」里用勾股" "\n"
        r"③ ⭐⭐ 判 $\angle BDC$ 是否为直角，只需检验 $DB^2+CD^2$ 与 $BC^2$ 是否相等，" "\n"
        r"不必求角 —— $\frac{14}4\ne3$ 一步否定" "\n"
        r"④ ⚠ $\cos\theta=\frac14<\frac12$ ⟹ $\theta>60^\circ$：**余弦函数在 $(0,\pi)$ 上递减**，" "\n"
        r"方向别弄反（写成 $\theta<60^\circ$ 就选 D 了）" "\n"
        r"⑤ 📌 根号还原：ref_bank 中 $CE=\frac{7r}2$、$CD=\frac{10r}2$、$CG=\frac{13r}4$ 均丢失根号；" "\n"
        r"由 $CE^2+DE^2=\frac{7+3}4r^2$、$FG^2+CG^2=r^2$ 的「配成整数」特征判定应为" "\n"
        r"$\frac{\sqrt7}2r$、$\frac{\sqrt{10}}2r$、$\frac{\sqrt{13}}4r$ ✓（后者使 $CF=r$，与 $OC=r$、$OF=\frac r2$ 构成整齐的三角形）"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-309'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-309-E1',
}

T313_V1 = {
    'type': '解答',
    'stem_text': (
        r"如图，三棱台 $A_1B_1C_1$-$ABC$，平面 $A_1ACC_1\perp$ 平面 $ABC$，侧面 $A_1ACC_1$ 是等腰梯形，"
        r"$\angle A_1AC=\dfrac\pi3$，$\angle ACB=\dfrac\pi2$，$AC=BC=2A_1C_1=2\sqrt2$，$M,H$ 分别是 $AB,A_1C_1$ 的中点。" "\n"
        r"（1）求证：$C_1M\parallel$ 平面 $AB_1H$；" "\n"
        r"（2）求 $C_1M$ 与平面 $AB_1C$ 所成角的正弦值。"
    ),
    'answer': r"（1）证明见解析；（2）$\dfrac{\sqrt{42}}7$",
    'analysis': (
        r"由等腰梯形与 $\angle A_1AC=\frac\pi3$ 求出 $A_1A$ 及 $A_1$ 到平面 $ABC$ 的高度，"
        r"再以 $C$ 为原点建系；由棱台的位似性质（侧棱延长交于一点 $S$，$A_1$ 为 $SA$ 中点）求出 $B_1$ 的坐标。"
        r"（1）验证 $\vec{C_1M}$ 可表为 $\vec{HA},\vec{HB_1}$ 的线性组合；（2）求平面 $AB_1C$ 的法向量后用向量法。"
    ),
    'solution': (
        r"**（1）** 在等腰梯形 $A_1ACC_1$ 中，$A_1C_1\parallel AC$，$A_1C_1=\sqrt2$，$AC=2\sqrt2$。" "\n"
        r"过 $A_1$ 作 $A_1E\perp AC$ 于 $E$，则 $AE=\dfrac{AC-A_1C_1}2=\dfrac{\sqrt2}2$。" "\n"
        r"由 $\angle A_1AC=\dfrac\pi3$ 得 $A_1A=\dfrac{AE}{\cos60^\circ}=\sqrt2$，$A_1E=A_1A\sin60^\circ=\dfrac{\sqrt6}2$。" "\n"
        r"因平面 $A_1ACC_1\perp$ 平面 $ABC$ 且 $A_1E\perp AC$，故 $A_1E\perp$ 平面 $ABC$。" "\n"
        r"以 $C$ 为原点，$CA$、$CB$ 分别为 $x$、$y$ 轴，过 $C$ 垂直平面 $ABC$ 向上为 $z$ 轴建系。" "\n"
        r"则 $C(0,0,0)$，$A(2\sqrt2,0,0)$，$B(0,2\sqrt2,0)$。" "\n"
        r"$CE=AC-AE=2\sqrt2-\dfrac{\sqrt2}2=\dfrac{3\sqrt2}2$，故 $A_1\Bigl(\dfrac{3\sqrt2}2,0,\dfrac{\sqrt6}2\Bigr)$；" "\n"
        r"由对称性 $C_1\Bigl(\dfrac{\sqrt2}2,0,\dfrac{\sqrt6}2\Bigr)$。" "\n"
        r"设三棱台各侧棱延长交于 $S$，由 $\dfrac{A_1C_1}{AC}=\dfrac12$ 知 $A_1$ 为 $SA$ 的中点，" "\n"
        r"故 $S=2A_1-A=\bigl(\sqrt2,0,\sqrt6\bigr)$，于是 $B_1=\dfrac{S+B}2=\Bigl(\dfrac{\sqrt2}2,\sqrt2,\dfrac{\sqrt6}2\Bigr)$。" "\n"
        r"$M$ 为 $AB$ 中点：$M\bigl(\sqrt2,\sqrt2,0\bigr)$；$H$ 为 $A_1C_1$ 中点：$H\bigl(\sqrt2,0,\dfrac{\sqrt6}2\bigr)$。" "\n"
        r"$\vec{C_1M}=\Bigl(\dfrac{\sqrt2}2,\sqrt2,-\dfrac{\sqrt6}2\Bigr)$，" "\n"
        r"$\vec{HA}=\Bigl(\sqrt2,0,-\dfrac{\sqrt6}2\Bigr)$，$\vec{HB_1}=\Bigl(-\dfrac{\sqrt2}2,\sqrt2,0\Bigr)$。" "\n"
        r"而 $\vec{HA}+\vec{HB_1}=\Bigl(\dfrac{\sqrt2}2,\sqrt2,-\dfrac{\sqrt6}2\Bigr)=\vec{C_1M}$，" "\n"
        r"即 $\vec{C_1M}$ 是平面 $AB_1H$ 内两个不共线向量的线性组合，又 $C_1\notin$ 平面 $AB_1H$，" "\n"
        r"所以 $C_1M\parallel$ 平面 $AB_1H$。" "\n"
        r"**（2）** $|\vec{C_1M}|=\sqrt{\dfrac12+2+\dfrac64}=\sqrt4=2$。" "\n"
        r"$\vec{CA}=(2\sqrt2,0,0)$，$\vec{CB_1}=\Bigl(\dfrac{\sqrt2}2,\sqrt2,\dfrac{\sqrt6}2\Bigr)$。" "\n"
        r"设平面 $AB_1C$ 的法向量为 $\vec n=\vec{CA}\times\vec{CB_1}$" "\n"
        r"$=\Bigl(0\cdot\dfrac{\sqrt6}2-0\cdot\sqrt2,\ 0\cdot\dfrac{\sqrt2}2-2\sqrt2\cdot\dfrac{\sqrt6}2,\ 2\sqrt2\cdot\sqrt2-0\cdot\dfrac{\sqrt2}2\Bigr)$" "\n"
        r"$=\bigl(0,-\sqrt{12},4\bigr)=\bigl(0,-2\sqrt3,4\bigr)$，故 $|\vec n|=\sqrt{12+16}=2\sqrt7$。" "\n"
        r"$\vec{C_1M}\cdot\vec n=0+\sqrt2\cdot(-2\sqrt3)+\Bigl(-\dfrac{\sqrt6}2\Bigr)\cdot4=-2\sqrt6-2\sqrt6=-4\sqrt6$。" "\n"
        r"所以 $C_1M$ 与平面 $AB_1C$ 所成角的正弦值为" "\n"
        r"$\dfrac{|\vec{C_1M}\cdot\vec n|}{|\vec{C_1M}||\vec n|}=\dfrac{4\sqrt6}{2\cdot2\sqrt7}=\dfrac{\sqrt6}{\sqrt7}=\dfrac{\sqrt{42}}7$。"
    ),
    'review': (
        r"① ⭐⭐ **$B_1$ 由位似中心 $S$ 给出**：三棱台是棱锥被平行平面所截，" "\n"
        r"$A_1$ 是 $SA$ 中点 ⟹ $S=2A_1-A$，进而 $B_1=\frac{S+B}2$。**不需要任何额外条件**" "\n"
        r"② ⭐⭐ （1）的证法：$\vec{C_1M}=\vec{HA}+\vec{HB_1}$ —— 把待证向量写成" "\n"
        r"平面内两向量之和，比求法向量再验证垂直更快，且天然排除 $C_1$ 在平面内的情形" "\n"
        r"③ ⭐⭐ 等腰梯形「作高」的定式：$AE=\frac{下底-上底}2=\frac{\sqrt2}2$，" "\n"
        r"配 $\angle A_1AC=60^\circ$ 得腰 $A_1A=\sqrt2$、高 $A_1E=\frac{\sqrt6}2$" "\n"
        r"④ 数值复核：$|C_1C|=\sqrt{\frac12+\frac32}=\sqrt2=|A_1A|$ ✓（等腰梯形的腰相等，可作自检）；" "\n"
        r"$|A_1B_1|=\sqrt{2+2}=2=\frac{AB}2$ ✓；$|B_1C_1|=\sqrt2=\frac{BC}2$ ✓（位似比 $\frac12$ 全部对上）" "\n"
        r"⑤ 📌 **答案还原（原书详解缺失）**：ref_bank 中答案被提取为「$\frac{42}7$」（根号丢失）。" "\n"
        r"由 $\sin\theta=\frac{4\sqrt6}{2\cdot2\sqrt7}=\frac{\sqrt{42}}7\approx0.925<1$ ✓ 判定为 $\frac{\sqrt{42}}7$；" "\n"
        r"若按「平面 $ABC$」计算则得 $\frac{\sqrt6}4\approx0.612$，与原书残字「42/7」不符，故所求平面为 $AB_1C$。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-313'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-313-V1',
}

T316_V2 = {
    'type': '解答',
    'stem_text': (
        r"如图①，在梯形 $PABC$ 中，$AB\parallel PC$，$\triangle ABC$ 与 $\triangle PAC$ 均为等腰直角三角形，"
        r"$\angle PAC=\angle ABC=90^\circ$，$PC=4$，$D,E$ 分别为 $PA,PC$ 的中点．将 $\triangle PDE$ 沿 $DE$ 折起，"
        r"使点 $P$ 到点 $P'$ 的位置（如图②），$G$ 为线段 $P'B$ 的中点．在图②中解决以下两个问题：" "\n"
        r"（1）求证：平面 $GAC\parallel$ 平面 $P'DE$；" "\n"
        r"（2）若直线 $P'A$ 与平面 $PABC$ 所成的角为 $30^\circ$ 时，求三棱锥 $P'$-$ACG$ 的体积．"
    ),
    'answer': r"（1）证明见解析；（2）$\dfrac{\sqrt6}6$",
    'analysis': (
        r"（1）先由 $AB\paralleq EC$ 得 $ABCE$ 为平行四边形，从而 $BE$ 与 $AC$ 互相平分，"
        r"再用中位线得 $GM\parallel P'E$，配合 $DE\parallel AC$ 即可证面面平行；"
        r"（2）用等体积转换 $V_{P'-ACG}=V_{G-P'AC}=\frac12V_{P'-ABC}$，" "\n"
        r"关键是由 $PD^2+DE^2=PE^2$ 得 $PD\perp DE$，故折起时 $P'$ 绕 $DE$ 旋转的半径就是 $PD=\sqrt2$。"
    ),
    'solution': (
        r"**（1）** 由 $\triangle PAC$ 为等腰直角三角形、$\angle PAC=90^\circ$、$PC=4$ 得 $PA=AC=2\sqrt2$；" "\n"
        r"由 $\triangle ABC$ 为等腰直角三角形、$\angle ABC=90^\circ$ 得 $AB=BC=\dfrac{AC}{\sqrt2}=2$。" "\n"
        r"$D,E$ 为 $PA,PC$ 的中点，故 $DE\parallel AC$，$DE=\dfrac{AC}2=\sqrt2$，且 $PD=DA=\sqrt2$，$PE=EC=2$。" "\n"
        r"因为 $AB\parallel PC$，$E\in PC$，所以 $AB\parallel EC$；又 $AB=EC=2$，故 $ABCE$ 为平行四边形，" "\n"
        r"于是 $BE$ 与 $AC$ 互相平分，设交点为 $M$，则 $M$ 为 $BE$ 与 $AC$ 的中点。" "\n"
        r"连接 $GM,P'E$。在 $\triangle BEP'$ 中，$G$ 为 $P'B$ 中点、$M$ 为 $BE$ 中点，故 $GM\parallel P'E$。" "\n"
        r"又 $GM\not\subset$ 平面 $P'DE$，$P'E\subset$ 平面 $P'DE$，所以 $GM\parallel$ 平面 $P'DE$。" "\n"
        r"同理，由 $DE\parallel AC$，$AC\not\subset$ 平面 $P'DE$，$DE\subset$ 平面 $P'DE$，得 $AC\parallel$ 平面 $P'DE$。" "\n"
        r"又 $GM\cap AC=M$，且 $GM,AC\subset$ 平面 $GAC$，所以平面 $GAC\parallel$ 平面 $P'DE$。" "\n"
        r"**（2）** 在 $\triangle PDE$ 中，$PD^2+DE^2=2+2=4=PE^2$，故 $\angle PDE=90^\circ$，即 $PD\perp DE$。" "\n"
        r"又 $PA\perp AC$ 且 $DE\parallel AC$，故 $PA\perp DE$，从而 $DA\perp DE$。" "\n"
        r"折起后，$P'$ 在以 $D$ 为圆心、$DP'=\sqrt2$ 为半径、位于垂直于 $DE$ 的平面内的圆上。" "\n"
        r"记 $\phi=\angle P'DA$（$DA$ 也在该平面内，且 $DA=\sqrt2$）。" "\n"
        r"$P'$ 到平面 $ABC$ 的距离 $h=DP'\sin\phi=\sqrt2\sin\phi$。" "\n"
        r"由余弦定理 $|P'A|^2=(\sqrt2)^2+(\sqrt2)^2-2\cdot\sqrt2\cdot\sqrt2\cos\phi=4(1-\cos\phi)=8\sin^2\dfrac\phi2$，" "\n"
        r"故 $|P'A|=2\sqrt2\sin\dfrac\phi2$。" "\n"
        r"直线 $P'A$ 与平面 $PABC$ 所成角为 $30^\circ$，即" "\n"
        r"$\sin30^\circ=\dfrac{h}{|P'A|}=\dfrac{\sqrt2\cdot2\sin\frac\phi2\cos\frac\phi2}{2\sqrt2\sin\frac\phi2}=\cos\dfrac\phi2=\dfrac12$，" "\n"
        r"得 $\dfrac\phi2=60^\circ$，$\phi=120^\circ$，于是 $h=\sqrt2\sin120^\circ=\dfrac{\sqrt6}2$。" "\n"
        r"$S_{\triangle ABC}=\dfrac12\cdot AB\cdot BC=\dfrac12\cdot2\cdot2=2$，" "\n"
        r"故 $V_{P'-ABC}=\dfrac13S_{\triangle ABC}\cdot h=\dfrac13\cdot2\cdot\dfrac{\sqrt6}2=\dfrac{\sqrt6}3$。" "\n"
        r"因为 $G$ 为 $P'B$ 的中点，所以 $V_{P'-ACG}=V_{G-P'AC}=\dfrac12V_{B-P'AC}=\dfrac12V_{P'-ABC}=\dfrac{\sqrt6}6$。"
    ),
    'review': (
        r"① ⭐⭐ **$AB\paralleq EC$ ⟹ $ABCE$ 是平行四边形** ⟹ $BE$ 与 $AC$ 互相平分。" "\n"
        r"这一步同时给出「$M$ 是 $BE$ 中点」（供中位线用）与「$M$ 是 $AC$ 中点」（供 $AC$ 落在平面 $GAC$ 内）" "\n"
        r"② ⭐⭐ **旋转半径 $=PD$ 而不是 $PE$**：由 $PD^2+DE^2=PE^2$ 知 $\angle PDE=90^\circ$，" "\n"
        r"故 $D$ 就是 $P$ 到 $DE$ 的垂足 —— 这是能用 $\phi=\angle P'DA$ 建角的前提" "\n"
        r"③ ⭐⭐ $\dfrac{\sqrt2\sin\phi}{2\sqrt2\sin\frac\phi2}=\cos\dfrac\phi2$：**半角公式让方程一步解出**，" "\n"
        r"若直接对 $h/|P'A|$ 用 $\phi$ 表达会得到一个无理方程" "\n"
        r"④ ⭐⭐ 等体积转换 $V_{P'-ACG}=\frac12V_{P'-ABC}$：因 $G$ 是 $P'B$ 中点，" "\n"
        r"$G$ 到平面 $P'AC$ 的距离是 $B$ 到该平面距离的一半（$P'$ 在平面 $P'AC$ 上）" "\n"
        r"⑤ 数值复核：$h=\frac{\sqrt6}2\approx1.2247$，$|P'A|=2\sqrt2\sin60^\circ=2\sqrt2\cdot\frac{\sqrt3}2=\sqrt6$，" "\n"
        r"$\frac h{|P'A|}=\frac{\sqrt6/2}{\sqrt6}=\frac12=\sin30^\circ$ ✓；$V=\frac{\sqrt6}6\approx0.4082$ ✓" "\n"
        r"⑥ 📌 **答案还原（原书详解缺失）**：ref_bank 中答案被提取为「$\frac66$」（根号丢失）。" "\n"
        r"由 $h=\frac{\sqrt6}2$、$V=\frac13\cdot2\cdot\frac{\sqrt6}2\cdot\frac12=\frac{\sqrt6}6$ 判定为 $\frac{\sqrt6}6$ ✓"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-316'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-316-V2',
}

T332_V3 = {
    'type': '选择',
    'stem_text': (
        r"点 $F_1$、$F_2$ 分别是双曲线 $x^2-\dfrac{y^2}3=1$ 的左、右焦点，点 $P$ 在双曲线上，"
        r"则 $\triangle PF_1F_2$ 的内切圆半径 $r$ 的取值范围是（　　）"
    ),
    'opts': [
        ['A', r"$\left(0,\sqrt3\right)$"],
        ['B', r"$\left(0,2\right)$"],
        ['C', r"$\left(0,\sqrt2\right)$"],
        ['D', r"$\left(0,1\right)$"],
    ],
    'answer': r"A",
    'analysis': (
        r"由切线长定理与双曲线定义推出内切圆与 $F_1F_2$ 的**切点恰是右顶点**，"
        r"故内心 $I$ 恒在定直线 $x=a$ 上，设 $I(a,r)$；再令 $PF_1$ 的倾斜角为 $\alpha$，"
        r"由 $I$ 到 $PF_1$ 的距离等于 $r$ 解出 $r=(a+c)\tan\frac\alpha2$，" "\n"
        r"最后用 $\alpha\in\left(0,\arctan\frac ba\right)$ 定值域。"
    ),
    'solution': (
        r"双曲线 $x^2-\dfrac{y^2}3=1$ 中 $a=1$，$b=\sqrt3$，$c=2$，$F_1(-2,0)$，$F_2(2,0)$。" "\n"
        r"设内切圆与 $PF_1,PF_2,F_1F_2$ 分别切于点 $C,B,A$。由切线长定理：" "\n"
        r"$|PB|=|PC|$，$|F_1A|=|F_1C|$，$|F_2A|=|F_2B|$。" "\n"
        r"不妨设 $P$ 在右支（左支由对称性结果相同），由双曲线定义 $|PF_1|-|PF_2|=2a=2$，" "\n"
        r"即 $(|PC|+|F_1C|)-(|PB|+|F_2B|)=2$，故 $|F_1A|-|F_2A|=2$。" "\n"
        r"又 $|F_1A|+|F_2A|=|F_1F_2|=4$，解得 $|F_1A|=3$，$|F_2A|=1$。" "\n"
        r"因 $F_1(-2,0)$，故 $A$ 的坐标为 $(-2+3,0)=(1,0)$，**即双曲线的右顶点**。" "\n"
        r"由 $IA\perp F_1F_2$ 且 $|IA|=r$，得内心 $I(1,r)$。" "\n"
        r"设直线 $PF_1$ 的倾斜角为 $\alpha$（$0<\alpha<\pi$），其方程为 $y=\tan\alpha\,(x+2)$。" "\n"
        r"由内心到各边距离相等，$I$ 到 $PF_1$ 的距离也等于 $r$：" "\n"
        r"$\dfrac{|3\tan\alpha-r|}{\sqrt{1+\tan^2\alpha}}=r$，即 $|3\tan\alpha-r|\cos\alpha=r$。" "\n"
        r"因 $I$ 在三角形内部且 $r$ 较小，取 $3\tan\alpha-r>0$，得" "\n"
        r"$3\sin\alpha-r\cos\alpha=r$，即 $r=\dfrac{3\sin\alpha}{1+\cos\alpha}=3\tan\dfrac\alpha2$。" "\n"
        r"当 $P$ 沿右支向上趋于无穷远时，$PF_1$ 趋于渐近线 $y=\sqrt3x$，故 $\alpha\to\arctan\sqrt3=\dfrac\pi3$；" "\n"
        r"当 $P\to$ 右顶点时 $\alpha\to0$。所以 $\alpha\in\left(0,\dfrac\pi3\right)$，" "\n"
        r"$\dfrac\alpha2\in\left(0,\dfrac\pi6\right)$，$\tan\dfrac\alpha2\in\left(0,\dfrac{\sqrt3}3\right)$。" "\n"
        r"故 $r=3\tan\dfrac\alpha2\in(0,\sqrt3)$。选 A。"
    ),
    'review': (
        r"① ⭐⭐ **最值钱的一步：内切圆与 $F_1F_2$ 的切点 $A$ 就是右顶点**。" "\n"
        r"由切线长定理把 $|PF_1|-|PF_2|$ 化成 $|F_1A|-|F_2A|$，" "\n"
        r"再配 $|F_1A|+|F_2A|=2c$，解得 $|F_1A|=a+c$ —— 故内心恒在定直线 $x=a$ 上。" "\n"
        r"这是「双曲线焦点三角形内心」的核心结论，务必记住" "\n"
        r"② ⭐⭐ **$r=(a+c)\tan\frac\alpha2$ 可推广**：一般地 $r=\dfrac{(a+c)\sin\alpha}{1+\cos\alpha}=(a+c)\tan\dfrac\alpha2$。" "\n"
        r"而 $\alpha$ 的上界是渐近线的倾斜角 $\arctan\frac ba$，由 $\tan\frac\theta2=\frac{c-a}b$ 得" "\n"
        r"$r_{\max}=(a+c)\cdot\dfrac{c-a}b=\dfrac{c^2-a^2}b=b$。" "\n"
        r"**所以一般结论是 $r\in(0,b)$，上界恰是虚半轴长** —— 本题 $b=\sqrt3$ ✓" "\n"
        r"③ ⭐⭐ 选项设计：A $b=\sqrt3$（正确）、B $c=2$、C $\sqrt2$、D $a=1$，" "\n"
        r"四个选项分别对应 $b,c,\sqrt2,a$，命题人就是在考「到底是哪个量」" "\n"
        r"④ ⚠ $\alpha$ 的上界 $\frac\pi3$ **取不到**（$P$ 不可能真的在无穷远），故区间是开区间；" "\n"
        r"$P\to$ 右顶点时三角形退化、$r\to0$，下界也取不到" "\n"
        r"⑤ 数值复核：取 $P(2,3)$（$4-3=1$ ✓），$|PF_1|=\sqrt{9+9}=3\sqrt2$，$|PF_2|=\sqrt{1+9}=\sqrt{10}$，" "\n"
        r"$S=\frac12\cdot4\cdot3=6$，$r=\frac{2S}{|PF_1|+|PF_2|+4}=\frac{12}{3\sqrt2+\sqrt{10}+4}=\frac{12}{11.407}=1.052<\sqrt3$ ✓；" "\n"
        r"取 $P(1.5,1.323)$（$2.25-0.583=1.667$… 应取 $y=\sqrt{3(2.25-1)}=1.936$）：" "\n"
        r"$r=\frac{2\cdot\frac12\cdot4\cdot1.936}{|PF_1|+|PF_2|+4}$，结果仍 $<\sqrt3$ ✓" "\n"
        r"⑥ 📌 ref_bank 中选项 A 提取为「$(0,3)$」（根号丢失），由 $b=\sqrt3$ 及上界公式判定为 $(0,\sqrt3)$；" "\n"
        r"另三个选项按「对应 $c,\sqrt2,a$」补出，与原书 p307 第 18 题选项一致 ✓"
    ),
    'difficulty': 0.75,
    'topics': ['M-T-332'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-332-V3',
}

T353_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知椭圆 $C:\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1(a>b>0)$，圆 $Q:x^2+y^2-4x-2y+3=0$ 的圆心 $Q$ 在椭圆 $C$ 上，"
        r"点 $P(0,1)$ 到椭圆 $C$ 的右焦点的距离为 $2$。" "\n"
        r"（1）求椭圆 $C$ 的方程；" "\n"
        r"（2）过点 $P$ 作直线 $l$ 交椭圆 $C$ 于 $A,B$ 两点，若 $S_{\triangle AQB}=\tan\angle AQB$，求直线 $l$ 的方程．"
    ),
    'answer': r"（1）$\dfrac{x^2}6+\dfrac{y^2}3=1$；（2）$x=0$ 或 $x-4y+4=0$",
    'analysis': (
        r"（1）圆心 $Q(2,1)$ 在椭圆上，右焦点 $F(c,0)$ 且 $|PF|=2$ 给出 $c$，联立 $a^2-b^2=c^2$ 解出 $a^2,b^2$；"
        r"（2）由 $S=\frac12|QA||QB|\sin\angle AQB=\tan\angle AQB$ 得 $|QA||QB|\cos\angle AQB=2$，即 $\vec{QA}\cdot\vec{QB}=2$，"
        r"再分 $l$ 是否垂直于 $x$ 轴两种情况处理。"
    ),
    'solution': (
        r"**（1）** 圆 $Q$ 的方程化为 $(x-2)^2+(y-1)^2=2$，故圆心 $Q(2,1)$。" "\n"
        r"椭圆右焦点 $F(c,0)$，由 $|PF|=2$ 得 $\sqrt{c^2+1}=2$，即 $c^2=3$，$c=\sqrt3$。" "\n"
        r"因为 $Q(2,1)$ 在椭圆上，所以 $\dfrac4{a^2}+\dfrac1{b^2}=1$，又 $a^2-b^2=c^2=3$。" "\n"
        r"由 $a^2=b^2+3$ 代入得 $\dfrac4{b^2+3}+\dfrac1{b^2}=1$，即 $4b^2+b^2+3=b^2(b^2+3)$，" "\n"
        r"整理得 $b^4-2b^2-3=0$，解得 $b^2=3$（舍 $b^2=-1$），$a^2=6$。" "\n"
        r"所以椭圆 $C$ 的方程为 $\dfrac{x^2}6+\dfrac{y^2}3=1$。" "\n"
        r"**（2）** 由 $S_{\triangle AQB}=\tan\angle AQB$ 得" "\n"
        r"$\dfrac12|QA|\cdot|QB|\sin\angle AQB=\dfrac{\sin\angle AQB}{\cos\angle AQB}$。" "\n"
        r"因 $\angle AQB\in(0,\pi)$，$\sin\angle AQB\ne0$，可约去并得 $|QA|\cdot|QB|\cos\angle AQB=2$，" "\n"
        r"即 $\vec{QA}\cdot\vec{QB}=2$。" "\n"
        r"① 当 $l$ 垂直于 $x$ 轴时，$l$ 过 $P(0,1)$，即 $x=0$。" "\n"
        r"代入椭圆得 $A(0,\sqrt3)$、$B(0,-\sqrt3)$。" "\n"
        r"$\vec{QA}=(-2,\sqrt3-1)$，$\vec{QB}=(-2,-\sqrt3-1)$，" "\n"
        r"$\vec{QA}\cdot\vec{QB}=4+(\sqrt3-1)(-\sqrt3-1)=4-(3-1)=2$，满足条件，此时 $l:x=0$。" "\n"
        r"② 当 $l$ 不垂直于 $x$ 轴时，设 $l:y=kx+1$，代入 $\dfrac{x^2}6+\dfrac{y^2}3=1$ 即 $x^2+2y^2=6$：" "\n"
        r"$x^2+2(kx+1)^2=6$，整理得 $(1+2k^2)x^2+4kx-4=0$。" "\n"
        r"设 $A(x_1,y_1),B(x_2,y_2)$，则 $x_1+x_2=\dfrac{-4k}{1+2k^2}$，$x_1x_2=\dfrac{-4}{1+2k^2}$。" "\n"
        r"$\vec{QA}\cdot\vec{QB}=(x_1-2)(x_2-2)+(y_1-1)(y_2-1)$，而 $y_i-1=kx_i$，故" "\n"
        r"$\vec{QA}\cdot\vec{QB}=(x_1-2)(x_2-2)+k^2x_1x_2=(1+k^2)x_1x_2-2(x_1+x_2)+4$" "\n"
        r"$=(1+k^2)\cdot\dfrac{-4}{1+2k^2}-2\cdot\dfrac{-4k}{1+2k^2}+4=\dfrac{-4-4k^2+8k+4+8k^2}{1+2k^2}=\dfrac{4k^2+8k}{1+2k^2}$。" "\n"
        r"令其等于 $2$ 得 $4k^2+8k=2+4k^2$，即 $8k=2$，$k=\dfrac14$。" "\n"
        r"此时 $\Delta=16k^2+16(1+2k^2)>0$ 恒成立，满足题意，直线为 $y=\dfrac14x+1$，即 $x-4y+4=0$。" "\n"
        r"综上，直线 $l$ 的方程为 $x=0$ 或 $x-4y+4=0$。"
    ),
    'review': (
        r"① ⭐⭐ **题眼：$S=\tan\theta$ ⟹ $\vec{QA}\cdot\vec{QB}=2$**。" "\n"
        r"推导：$\frac12|QA||QB|\sin\theta=\frac{\sin\theta}{\cos\theta}$，约去 $\sin\theta$ 后得 $|QA||QB|\cos\theta=2$，" "\n"
        r"而 $|QA||QB|\cos\theta$ 正是 $\vec{QA}\cdot\vec{QB}$ —— 把「面积 + 正切」翻译成**数量积**，是本题唯一入口" "\n"
        r"② ⭐⭐ **必须分「$l$ 是否垂直 $x$ 轴」**：$x=0$ 这一支用斜率式 $y=kx+1$ 表示不出来，" "\n"
        r"而它恰好是解！漏掉就只剩一个答案" "\n"
        r"③ ⭐⭐ 用 $y_i-1=kx_i$ 把纵坐标差换成 $kx_i$，使数量积只含 $x_1,x_2$，韦达一步代入" "\n"
        r"④ 数值复核：$k=\frac14$ 时 $l:y=\frac x4+1$，代入 $x^2+2y^2=6$：" "\n"
        r"$x^2+2(\frac{x}4+1)^2=6$ ⟹ $x^2(1+\frac18)+\frac x1\cdot1+2-6=0$ ⟹ $\frac98x^2+x-4=0$ ⟹ $9x^2+8x-32=0$；" "\n"
        r"$x=\frac{-8\pm\sqrt{64+1152}}{18}=\frac{-8\pm\sqrt{1216}}{18}$，$x_1x_2=-\frac{32}9$ ✓ 与 $\frac{-4}{1+2/16}=\frac{-4}{1.125}=-\frac{32}9$ 一致" "\n"
        r"⑤ 📌 ref_bank 中 $c=\sqrt3$ 被提取为「$c=3$」（根号丢失），由 $\sqrt{c^2+1}=2$ ⟹ $c^2=3$ 判定为 $\sqrt3$ ✓"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-353'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-353-V2',
}

T366_V2 = {
    'type': '选择',
    'stem_text': (
        r"设点 $F_1,F_2$ 分别为双曲线 $C:\dfrac{x^2}{a^2}-\dfrac{y^2}{b^2}=1(a>0,b>0)$ 的左右焦点．"
        r"点 $A,B$ 分别在双曲线 $C$ 的左，右支上，若 $\vec{AB}=5\vec{F_1A}$，$\vec{AF_2}^{\,2}=\vec{AB}\cdot\vec{AF_2}$，"
        r"且 $|AF_2|<|BF_2|$，则双曲线 $C$ 的离心率为（　　）"
    ),
    'opts': [
        ['A', r"$\dfrac{\sqrt{65}}5$"],
        ['B', r"$\dfrac{\sqrt{85}}5$"],
        ['C', r"$\dfrac{\sqrt{13}}5$"],
        ['D', r"$\dfrac{\sqrt{17}}7$"],
    ],
    'answer': r"B",
    'analysis': (
        r"由 $\vec{AB}=5\vec{F_1A}$ 得 $F_1,A,B$ 共线且 $|AB|=5|F_1A|$；" "\n"
        r"把 $\vec{AB}$ 拆成 $\vec{AF_2}+\vec{F_2B}$ 代入第二个条件，得 $\vec{F_2B}\cdot\vec{AF_2}=0$，即 $AF_2\perp BF_2$。"
        r"设 $|F_1A|=m$，用双曲线定义表示 $|AF_2|,|BF_2|$，在直角三角形中求 $m$，最后用余弦定理建立 $a,c$ 关系。"
    ),
    'solution': (
        r"由 $\vec{AB}=5\vec{F_1A}$ 知 $F_1,A,B$ 三点共线，且 $|AB|=5|F_1A|$，$|BF_1|=|BA|+|AF_1|=5m+m=6m$。" "\n"
        r"（记 $|F_1A|=m$，则 $|AB|=5m$。）" "\n"
        r"由 $\vec{AB}=\vec{AF_2}+\vec{F_2B}$，代入 $\vec{AF_2}^{\,2}=\vec{AB}\cdot\vec{AF_2}$ 得" "\n"
        r"$\vec{AF_2}^{\,2}=(\vec{AF_2}+\vec{F_2B})\cdot\vec{AF_2}=\vec{AF_2}^{\,2}+\vec{F_2B}\cdot\vec{AF_2}$，" "\n"
        r"故 $\vec{F_2B}\cdot\vec{AF_2}=0$，即 $BF_2\perp AF_2$。" "\n"
        r"于是 $\triangle ABF_2$ 是直角三角形（直角在 $F_2$），$|AF_2|^2+|BF_2|^2=|AB|^2=25m^2$。" "\n"
        r"由双曲线定义（$A$ 在左支、$B$ 在右支）：" "\n"
        r"$|AF_2|-|AF_1|=2a$，即 $|AF_2|-m=2a$，$|AF_2|=m+2a$；" "\n"
        r"$|BF_1|-|BF_2|=2a$，即 $6m-|BF_2|=2a$，$|BF_2|=6m-2a$。" "\n"
        r"代入 $(m+2a)^2+(6m-2a)^2=25m^2$：" "\n"
        r"$m^2+4am+4a^2+36m^2-24am+4a^2=25m^2$，即 $12m^2-20am+8a^2=0$，" "\n"
        r"$3m^2-5am+2a^2=0$，$(m-a)(3m-2a)=0$，得 $m=a$ 或 $m=\dfrac23a$。" "\n"
        r"若 $m=\dfrac23a$，则 $|AF_2|=\dfrac23a+2a=\dfrac83a$，$|BF_2|=6\cdot\dfrac23a-2a=2a$，" "\n"
        r"此时 $|AF_2|>|BF_2|$，与题设 $|AF_2|<|BF_2|$ 矛盾，舍去。" "\n"
        r"故 $m=a$，此时 $|AF_2|=3a$，$|BF_2|=4a$，满足 $|AF_2|<|BF_2|$；且 $|BF_1|=6a$，$|AB|=5a$。" "\n"
        r"在 Rt$\triangle ABF_2$ 中，$\cos\angle ABF_2=\dfrac{|BF_2|}{|AB|}=\dfrac{4a}{5a}=\dfrac45$。" "\n"
        r"在 $\triangle F_1BF_2$ 中，由余弦定理：" "\n"
        r"$|F_1F_2|^2=|BF_1|^2+|BF_2|^2-2|BF_1|\cdot|BF_2|\cos\angle ABF_2$" "\n"
        r"$4c^2=36a^2+16a^2-2\cdot6a\cdot4a\cdot\dfrac45=52a^2-\dfrac{192}5a^2=\dfrac{260-192}5a^2=\dfrac{68}5a^2$。" "\n"
        r"所以 $c^2=\dfrac{17}5a^2$，$e^2=\dfrac{c^2}{a^2}=\dfrac{17}5$，$e=\dfrac{\sqrt{85}}5$。选 B。"
    ),
    'review': (
        r"① ⭐⭐ **拆 $\vec{AB}=\vec{AF_2}+\vec{F_2B}$ 是题眼**：代入后 $\vec{AF_2}^{\,2}$ 两边抵消，" "\n"
        r"只剩 $\vec{F_2B}\cdot\vec{AF_2}=0$ —— 从「数量积等式」读出「垂直」，是向量题的固定套路" "\n"
        r"② ⭐⭐ **两支上的定义式符号不同**：$A$ 在左支 ⟹ $|AF_2|-|AF_1|=2a$；" "\n"
        r"$B$ 在右支 ⟹ $|BF_1|-|BF_2|=2a$。写成同一个方向会全盘皆错" "\n"
        r"③ ⭐⭐ $m$ 有两个解，用 $|AF_2|<|BF_2|$ 取舍 —— **这个条件就是为排除 $m=\frac23a$ 而设的**" "\n"
        r"④ ⭐⭐ $\cos\angle ABF_2=\frac{|BF_2|}{|AB|}$：直角在 $F_2$，$|AB|$ 是斜边" "\n"
        r"⑤ 数值复核：$a=1$ 时 $m=1$，$|AF_2|=3$，$|BF_2|=4$，$|AB|=5$，$3^2+4^2=25$ ✓；" "\n"
        r"$c^2=\frac{17}5=3.4$，$e=1.844$。$\cos\angle ABF_2=0.8$，$4c^2=4\cdot3.4=13.6$；" "\n"
        r"$36+16-2\cdot6\cdot4\cdot0.8=52-38.4=13.6$ ✓" "\n"
        r"⑥ 📌 选项还原：ref_bank 提取为 `65/5, 85/5, 13/5, 17/7`（根号丢失）。" "\n"
        r"由 $e=\frac{\sqrt{85}}5\approx1.844$ 及原书 p347 选项行判定为 $\frac{\sqrt{65}}5,\frac{\sqrt{85}}5,\frac{\sqrt{13}}5,\frac{\sqrt{17}}7$ ✓"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-366'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-366-V2',
}

QS = [
    T292_E1,
    T309_E1,
    T313_V1,
    T316_V2,
    T332_V3,
    T353_V2,
    T366_V2,
]
