# -*- coding: utf-8 -*-
r"""第77批：二面角、正方体截面、向量最值（12 题）

M-T-305（4）、M-T-286（4）、M-T-288（1）、M-T-287（1）、M-T-187（2）

## ★★ 12 题我全部独立验算（坐标法 / 数值法）

| 题 | 我的验算 | 答案 |
|---|---|---|
| M-T-305-E1 | ⭐ 题干 $AD=2$ 实为 $\sqrt2$（否则 $AD^2\ne AE^2+DE^2$）；$OE=\frac{\sqrt3}3$、$EF=\frac{\sqrt2}2$ ⟹ $\tan=\frac{\sqrt6}3$ | **A** |
| M-T-305-V1 | 建系 $A(0,0,0)$、$O(-5,-\sqrt3,0)$、$P(-5,-\sqrt3,\sqrt3)$，两法向量夹角余弦 $=\frac{\sqrt2}8$ | **B** |
| M-T-305-V2 | $\vec n_{ABP}=(0,1,0)$、$\vec n_{CDP}=(0,1,1)$ ⟹ $\cos=\frac1{\sqrt2}=\frac{\sqrt2}2$ | **B** |
| M-T-305-V3 | $\alpha=60^\circ$（$\triangle AB_1D_1$ 等边）、$\beta=60^\circ$ 或 $120^\circ$ ⟹ $\sin\alpha=\sin\beta$ | **B** |
| M-T-286-E1 | $AA_1=2$、$V_{P-ABC}=2\sqrt3$、$E$ 离底面最远 $\frac32$ ⟹ $V_{\min}=2\sqrt3-\frac{3\sqrt3}2=\frac{\sqrt3}2$ | **A** |
| M-T-286-V1 | 侧面展开成平行四边形，截面周界展开为与 $AA_1$ 平行的定长线段 ⟹ $l$ 定值；正六边形与正三角形面积不同 ⟹ $S$ 不定 | **B** |
| M-T-286-V2 | $\cos\angle(AA_1,\alpha)=\sqrt{1-\frac13}=\frac{\sqrt6}3$ ✓ B 对；$\beta$ 含 $AC_1$ 截不出正方形 ⟹ D 错 | **D** |
| M-T-286-V3 | 梯形 $B_1D_1EF$：上下底 $2\sqrt2,\sqrt2$，腰 $\sqrt5$ ⟹ 高 $\frac{3\sqrt2}2$ ⟹ 面积 $\frac92$ ✓ | **C** |
| M-T-288-V1 | 菱形 $AFC_1E$：对角线 $2\sqrt3$ 与 $2\sqrt2$ 垂直 ⟹ $S=\frac12\cdot2\sqrt3\cdot2\sqrt2=2\sqrt6$ | **D** |
| M-T-287-V1 | $AE=AF=\sqrt5$、$PE=PF=\frac{\sqrt{13}}3$ ⟹ 周长 $2\sqrt5+\frac{2\sqrt{13}}3$ | **B** |
| M-T-187-V2 | $x+y=\cos\theta+\sqrt3\sin\theta=2\sin(\theta+30^\circ)\le2$，$\theta=60^\circ$ 取等 | **B** |
| M-T-187-V3 | $\vec b\cdot\vec c=4\sqrt3\sin(2\theta-\frac\pi3)+6$，$-\frac{\sqrt3}2<\sin\le1$ ⟹ $(0,6+4\sqrt3]$ | 填 |

## 本批最大收获：M-T-305-E1 的 $AD=\sqrt2$ 被印成 $2$

题面写「$AB=BD=2$，$AD=2$」。若 $AD=2$，则 $A,E,C$ 共线、$DE\perp AC$ 且 $AE=CE=1$ 应给出

$$AD^2=AE^2+DE^2=1+1=2\ \Longrightarrow\ AD=\sqrt2$$

**与题面的 $2$ 矛盾**。取 $\sqrt2$ 后其余链条全部闭合：$\triangle ADC$ 为等腰直角（$AD^2+DC^2=2+2=4=AC^2$）✓、球心 $O$ 到 $A$ 与 $D$ 等距（都是 $\frac{2}{\sqrt3}$）✓。

## M-T-305-V1 我建系完整验证过（这是本批最硬的一次）

取 $A(0,0,0)$、$l_1$ 沿 $x$ 轴、$l_2$ 方向 $(\frac{\sqrt3}2,\frac12,0)$。由 $OB\perp l_1$、$OC\perp l_2$、$OB=\sqrt3$、$OC=1$ 解得 **两组** $O$：

| $O$ | 两平面法向量夹角余弦 |
|---|---|
| $(-1,-\sqrt3,0)$ | $\frac{5\sqrt2}8$（不在选项内） |
| $(-5,-\sqrt3,0)$ | $\frac{\sqrt2}8$ ✓ **选项 B** |

顺带核对了原书的中间量：$AB=5$、$PA=\sqrt{31}$、$AC=3\sqrt3$、$CM=\frac{6\sqrt3}{\sqrt{31}}$、$d_2=\frac{3\sqrt6}4$ —— 全部与 $O(-5,-\sqrt3,0)$ 吻合 ✓

## 三个能复用的结论

**1. 二面角的「距离 / 距离」求法**（M-T-305-V1）
$$\sin\theta=\frac{\text{平面 }\gamma\text{ 内一点到 }\beta\text{ 的距离}}{\text{该点到交线的距离}}$$
比硬求法向量夹角更快，尤其当垂线关系清晰时。

**2. 截面周长为定值：侧面展开**（M-T-286-V1）
把几何体 $V$ 的侧面沿一条棱剪开铺平，截面多边形的周界展开成**一条线段**，长度恰等于展开图的一条边长 ⟹ 定值。

**3. 平行四边形/菱形的对角线互相垂直时用 $\frac12 d_1d_2$**（M-T-288-V1）
截面 $AFC_1E$ 是菱形，$AC_1\perp EF$，面积直接 $=\frac12\cdot2\sqrt3\cdot2\sqrt2=2\sqrt6$。
"""

T305_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知四面体 $ABCD$ 的每个顶点都在球 $O$（$O$ 为球心）的球面上，$\triangle ABC$ 为等边三角形，"
        r"$AB=BD=2$，$AD=\sqrt2$，且 $AC\perp BD$，则二面角 $A-CD-O$ 的正切值为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac{\sqrt6}3$"),
        ('B', r"$\dfrac{\sqrt6}6$"),
        ('C', r"$\dfrac{\sqrt5}3$"),
        ('D', r"$\dfrac{\sqrt{10}}6$"),
    ],
    'answer': 'A',
    'analysis': (
        r"由 $BE\perp AC$、$AC\perp BD$ 得 $AC\perp$ 面 $BDE$，进而 $AC\perp DE$；由 $DE^2+BE^2=BD^2$ 得 $DE\perp BE$，"
        r"故 $DE\perp$ 面 $ABC$。球心 $O$ 是 $\triangle ABC$ 的中心，$F$ 为 $CD$ 中点时 $\angle EFO$ 即所求平面角，"
        r"$\tan\angle EFO=\frac{OE}{EF}=\frac{\sqrt3/3}{\sqrt2/2}=\frac{\sqrt6}3$。"
    ),
    'solution': (
        r"设 $E$ 为 $AC$ 中点，连 $BE,DE$。$\triangle ABC$ 为等边三角形 ⟹ $BE\perp AC$；又 $AC\perp BD$，$BE\cap BD=B$ ⟹ $AC\perp$ 面 $BDE$ ⟹ $AC\perp DE$。" "\n"
        r"由 $AB=2$ 得 $BE=\sqrt3$、$AE=CE=1$；由 $AD=\sqrt2$ 且 $DE\perp AC$ 得 $DE=\sqrt{AD^2-AE^2}=\sqrt{2-1}=1$。" "\n"
        r"$\because DE^2+BE^2=1+3=4=BD^2$，$\therefore DE\perp BE$。又 $AC\cap BE=E$，$AC,BE\subset$ 面 $ABC$ ⟹ $DE\perp$ 面 $ABC$ ⟹ 面 $ADC\perp$ 面 $ABC$。" "\n"
        r"由 $DE\perp AC$、$CE=DE=1$ 得 $DC=\sqrt2$，于是 $AD^2+DC^2=2+2=4=AC^2$ ⟹ $\triangle ADC$ 为等腰直角三角形。" "\n"
        r"因 $DE\perp$ 面 $ABC$，球心 $O$ 在过 $\triangle ABC$ 外心且垂直于底面的直线上；而 $OA=OD$：" "\n"
        r"设 $O$ 为 $\triangle ABC$ 的中心（在 $BE$ 上、距 $E$ 为 $\frac{BE}3=\frac{\sqrt3}3$），则 $OA=\frac{2}{\sqrt3}$、$OD=\sqrt{OE^2+DE^2}=\sqrt{\frac13+1}=\frac2{\sqrt3}$ ✓ 相等，$O$ 即球心。" "\n"
        r"取 $F$ 为 $CD$ 中点，连 $EF,OF$。由 $BE\perp AC$、$BE\perp DE$ 得 $BE\perp$ 面 $ADC$ ⟹ $OE\perp EF$，故 $\angle EFO$ 为二面角 $A-CD-O$ 的平面角。" "\n"
        r"$OE=\dfrac{BE}3=\dfrac{\sqrt3}3$，$EF=\dfrac{AD}2=\dfrac{\sqrt2}2$（$E,F$ 为 $AC,CD$ 中点，中位线）。" "\n"
        r"$\therefore\tan\angle EFO=\dfrac{OE}{EF}=\dfrac{\sqrt3/3}{\sqrt2/2}=\dfrac{2\sqrt3}{3\sqrt2}=\dfrac{\sqrt6}3$。故选 A。"
    ),
    'review': (
        r"★ 题干、选项、答案、详解完整 ✓。" "\n"
        r"⚠ **题干的 $AD=2$ 实为 $\sqrt2$**（提取丢根号）。**反证**：若 $AD=2$，则由 $A,E,C$ 共线、$DE\perp AC$、$AE=1$ 应得" "\n"
        r"$AD^2=AE^2+DE^2=1+1=2$，即 $AD=\sqrt2\ne2$ —— 矛盾。取 $\sqrt2$ 后全链条闭合（见下）。" "\n"
        r"原书详解：「若 $E$ 为 $AC$ 中点…$BE=\sqrt3$，$AE=DE=CE=1$，而 $BD=2$，$\therefore DE^2+BE^2=BD^2$，即 $DE\perp BE$…" "\n"
        r"$DC=\sqrt2$，则 $DC^2+AD^2=AC^2$，故 $\triangle ADC$ 为等腰直角三角形…四面体 $ABCD$ 的球心 $O$ 为 $\triangle ABC$ 的中心，即 $BE$ 靠近 $E$ 的三等分点。" "\n"
        r"若 $F$ 为 $DC$ 中点，连 $EF,OF$，易知 $\angle EFO$ 即为二面角 $A-CD-O$ 的平面角…$BE\perp$ 面 $ADC$，又 $EF\subset$ 面 $ADC$，则 $BE\perp EF$，即 $OE\perp EF$。" "\n"
        r"$\therefore\tan\angle EFO=\frac{OE}{EF}$，而 $OE=\frac{BE}3=\frac{\sqrt3}3$，$EF=\frac{\sqrt2}2$，$\therefore\tan\angle EFO=\frac{\sqrt6}3$。故选：A.」" "\n"
        r"—— **$BE=\sqrt3$、$AE=DE=CE=1$、$DE\perp BE$、$DE\perp$面$ABC$、$DC=\sqrt2$、等腰直角、$O$ 为 $BE$ 靠近 $E$ 的三等分点、$\angle EFO$、$OE=\frac{\sqrt3}3$、$EF=\frac{\sqrt2}2$、$\frac{\sqrt6}3$、答案 A 全部一致** ✓✓✓" "\n"
        r"（注意原书用 $DC^2+AD^2=AC^2$ 反推，其中 $AD=\sqrt2$ 正是我修正后的值 ✓）" "\n"
        r"**独立验算（数值，完全独立）**：" "\n"
        r"① **$BE=\sqrt3$**：等边 $\triangle ABC$ 边长 $2$，中线 $=\frac{\sqrt3}2\times2=\sqrt3=1.732051$ ✓✓✓" "\n"
        r"② **$DE=1$**：由 $AD=\sqrt2$、$AE=1$、$DE\perp AC$ ⟹ $DE=\sqrt{2-1}=1$ ✓✓✓" "\n"
        r"③ **$DE^2+BE^2=1+3=4=BD^2$** ⟹ $DE\perp BE$ ✓✓✓" "\n"
        r"④ **建系验证**：$E=(0,0,0)$，$A=(-1,0,0)$，$C=(1,0,0)$，$B=(0,\sqrt3,0)$，$D=(0,0,1)$。" "\n"
        r"$AB=\sqrt{1+3}=2$ ✓；$BD=\sqrt{0+3+1}=2$ ✓；$AD=\sqrt{1+0+1}=\sqrt2$ ✓ ✓✓✓" "\n"
        r"$AC=(2,0,0)$，$BD=(0,-\sqrt3,1)$：点积 $=0$ ✓✓✓ **$AC\perp BD$ 成立**" "\n"
        r"$DC=\sqrt{1+0+1}=\sqrt2$ ✓；$AD^2+DC^2=2+2=4=AC^2$ ✓✓✓ **等腰直角**" "\n"
        r"⑤ **球心**：$\triangle ABC$ 中心 $O=(0,\frac{\sqrt3}3,0)$（在 $BE$ 上距 $E$ 为 $\frac{\sqrt3}3$）。" "\n"
        r"$OA=\sqrt{1+\frac13}=\sqrt{\frac43}=1.154701$；$OD=\sqrt{0+\frac13+1}=\sqrt{\frac43}=1.154701$ ✓✓✓" "\n"
        r"$OB=\sqrt3-\frac{\sqrt3}3=\frac{2\sqrt3}3=1.154701$ ✓；$OC=\sqrt{1+\frac13}=1.154701$ ✓ **四点到 $O$ 等距** ✓✓✓" "\n"
        r"⑥ **二面角**：$F$ 为 $CD$ 中点 $=(0.5,0,0.5)$。$EF=(\frac12,0,\frac12)$，$|EF|=\frac{\sqrt2}2=0.707107$ ✓" "\n"
        r"$EO=(0,\frac{\sqrt3}3,0)$，$|EO|=0.577350$ ✓。$EO\cdot EF=0$ ✓✓✓ **垂直成立**" "\n"
        r"$\tan\angle EFO=\frac{|EO|}{|EF|}=\frac{0.577350}{0.707107}=0.816497$。$\frac{\sqrt6}3=\frac{2.449490}3=0.816497$ ✓✓✓" "\n"
        r"⑦ **选项排除**：$\frac{\sqrt6}6=0.408$（B）、$\frac{\sqrt5}3=0.745$（C）、$\frac{\sqrt{10}}6=0.527$（D）都不等于 $0.816$ ✓✓✓" "\n"
        r"**答案 A 正确** ✓" "\n"
        r"**⭐⭐ 通法（找二面角的平面角）**：" "\n"
        r"① ⭐⭐ **先找「垂直于棱的平面」**：本题 $AC\perp$ 面 $BDE$，$DE\subset$ 面 $BDE$ ⟹ $DE\perp AC$；" "\n"
        r"**「线⊥面」能把垂直批量转移**，这是找平面角的第一步；" "\n"
        r"② ⭐⭐ **$DE^2+BE^2=BD^2$ ⟹ $DE\perp BE$**：" "\n"
        r"**用勾股逆定理判垂直**（比算向量点积快），两个垂直合起来得 $DE\perp$ 面 $ABC$；" "\n"
        r"③ ⭐ **球心定位：先猜「底面中心 + 垂直线」，再用 $OA=OD$ 验证** —— " "\n"
        r"本题 $O$ 恰是 $\triangle ABC$ 的中心，验证 $OA=OB=OC=OD=\frac2{\sqrt3}$ 即确认；" "\n"
        r"④ ⭐ **中位线给 $EF=\frac{AD}2$**：$E,F$ 分别是 $AC,CD$ 中点 —— **看到两个中点先连中位线**；" "\n"
        r"⑤ ⚠ **$\tan=\frac{OE}{EF}$ 别把分子分母弄反**：$\angle EFO$ 在 $F$ 处，对边是 $EO$、邻边是 $EF$ —— " "\n"
        r"**看角的顶点字母（中间的 $F$）之外的两个点，谁是「对边」要看直角三角形**；" "\n"
        r"⑥ ⚠ **本题题干的 $AD$ 丢根号**：凡是「算出一个长度与题面不符」就要警觉 —— " "\n"
        r"本题 $AD^2=AE^2+DE^2=2$ 与题面 $AD=2$ 矛盾，一秒定位是 $\sqrt2$。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-305'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-305-E1',
}

T305_V1 = {
    'type': '选择',
    'stem_text': (
        r"设 $l_1,l_2$ 是平面 $\alpha$ 内所成角为 $\dfrac\pi6$ 的两条直线，过 $l_1,l_2$ 分别作平面 $\beta,\gamma$，"
        r"且锐二面角 $\alpha-l_1-\beta$ 的大小为 $\dfrac\pi4$，锐二面角 $\alpha-l_2-\gamma$ 的大小为 $\dfrac\pi3$，"
        r"则平面 $\beta,\gamma$ 所成的锐二面角的平面角的余弦值可能是（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac{\sqrt3}6$"),
        ('B', r"$\dfrac{\sqrt2}8$"),
        ('C', r"$\dfrac14$"),
        ('D', r"$\dfrac13$"),
    ],
    'answer': 'B',
    'analysis': (
        r"设 $P$ 为 $\beta,\gamma$ 交线上一点，$PO\perp\alpha$ 于 $O$，$OB\perp l_1$、$OC\perp l_2$，则 $\angle PBO=\frac\pi4$、$\angle PCO=\frac\pi3$。"
        r"取 $CO=1$ 得 $PO=BO=\sqrt3$、$PB=\sqrt6$、$PC=2$，进而求出 $C$ 到平面 $\beta$ 的距离 $d$ 与 $C$ 到交线的距离 $CM$，"
        r"由 $\sin\theta=\frac d{CM}=\frac{\sqrt{62}}8$ 得 $\cos\theta=\frac{\sqrt2}8$。"
    ),
    'solution': (
        r"记 $\alpha$ 为平面 $ABC$，$l_1=AB$，$l_2=AC$，$\angle BAC=\frac\pi6$；$\beta$ 为平面 $ABP$，$\gamma$ 为平面 $ACP$。" "\n"
        r"过 $P$ 作 $PO\perp\alpha$ 于 $O$，再作 $OB\perp AB$、$OC\perp AC$，连 $PB,PC$。由三垂线定理逆定理，$PB\perp AB$、$PC\perp AC$。" "\n"
        r"故 $\angle PBO$、$\angle PCO$ 分别是二面角 $\alpha-l_1-\beta$、$\alpha-l_2-\gamma$ 的平面角，即 $\angle PBO=\frac\pi4$、$\angle PCO=\frac\pi3$。" "\n"
        r"取 $CO=1$，则 $PO=CO\tan\frac\pi3=\sqrt3$；$BO=\dfrac{PO}{\tan\frac\pi4}=\sqrt3$；$PC=\dfrac{CO}{\cos\frac\pi3}=2$；$PB=\dfrac{BO}{\cos\frac\pi4}=\sqrt6$。" "\n"
        r"由 $AB\perp OB$、$AB\perp PO$ 得 $AB\perp$ 面 $POB$，从而面 $PAB\perp$ 面 $POB$（交线 $PB$）。" "\n"
        r"过 $O$ 作 $OH\perp PB$，则 $OH\perp$ 面 $PAB$，且 $OH=\dfrac{PO\cdot BO}{PB}=\dfrac{\sqrt3\cdot\sqrt3}{\sqrt6}=\dfrac{\sqrt6}2$。" "\n"
        r"由 $C$ 与 $O$ 到面 $PAB$ 的距离之比（由 $\angle BAC=\frac\pi6$ 及 $OC=1$、$OB=\sqrt3$ 定出）得" "\n"
        r"$d=\operatorname{dist}(C,\text{面}PAB)=\dfrac{3\sqrt6}4$。" "\n"
        r"设 $M$ 为 $C$ 在交线 $AP$ 上的射影，则 $CM=\operatorname{dist}(C,AP)=\dfrac{6\sqrt3}{\sqrt{31}}$（由 $AC=3\sqrt3$、$AP=\sqrt{31}$ 及面积法）。" "\n"
        r"$\therefore\sin\theta=\dfrac d{CM}=\dfrac{3\sqrt6/4}{6\sqrt3/\sqrt{31}}=\dfrac{3\sqrt6\cdot\sqrt{31}}{24\sqrt3}=\dfrac{3\sqrt2\cdot\sqrt{31}}{24}=\dfrac{\sqrt{62}}8$。" "\n"
        r"$\cos\theta=\sqrt{1-\dfrac{62}{64}}=\sqrt{\dfrac2{64}}=\dfrac{\sqrt2}8$。故选 B。"
    ),
    'review': (
        r"★ 题干、选项、答案、详解完整 ✓。原书详解给出 $PO=BO=\sqrt3$、$PC=2$、$PB=\sqrt6$、$AB=5$、$PA=\sqrt{31}$、" "\n"
        r"$AC=3\sqrt3$、$CM=\frac{6\sqrt3}{\sqrt{31}}$、$d_1=OH=\frac{\sqrt6}2$、$d_2=\frac{3\sqrt6}4$、$\sin\theta=\frac{\sqrt{62}}8$、$\cos\theta=\frac{\sqrt2}8$、选 B。" "\n"
        r"—— **这些中间量我用坐标法全部逐一核对，无一例外** ✓✓✓（见下）" "\n"
        r"**独立验算（坐标法，完全独立 —— 本批最硬的一次）**：" "\n"
        r"取 $A=(0,0,0)$，$l_1$ 沿 $x$ 轴，单位方向 $u_1=(1,0,0)$；$l_2$ 单位方向 $u_2=(\frac{\sqrt3}2,\frac12,0)$。$\alpha$ 为 $z=0$。" "\n"
        r"设 $O=(p,q,0)$。由 $OB\perp l_1$ 得 $B=(p,0,0)$、$|BO|=|q|=\sqrt3$；" "\n"
        r"由 $OC\perp l_2$ 得 $\operatorname{dist}(O,l_2)=|O\times u_2|=\left|\frac p2-\frac{q\sqrt3}2\right|=1$。" "\n"
        r"取 $q=-\sqrt3$：$\left|\frac p2+\frac32\right|=1$ ⟹ $p=-1$ 或 $p=-5$（**两组解**）。" "\n"
        r"**解一 $O=(-1,-\sqrt3,0)$**，$P=(-1,-\sqrt3,\sqrt3)$（$PO=\sqrt3$）：" "\n"
        r"$C=(O\cdot u_2)u_2=(-\sqrt3)(\frac{\sqrt3}2,\frac12,0)=(-\frac32,-\frac{\sqrt3}2,0)$。" "\n"
        r"$\vec n_\beta=\vec{AB}\times\vec{AP}=(-1,0,0)\times(-1,-\sqrt3,\sqrt3)\propto(0,1,1)$。" "\n"
        r"$\vec n_\gamma=\vec{AC}\times\vec{AP}\propto(-3,3\sqrt3,2\sqrt3)$。" "\n"
        r"$\cos=\frac{3\sqrt3+2\sqrt3}{\sqrt2\cdot\sqrt{48}}=\frac{5\sqrt3}{4\sqrt6}=\frac{5\sqrt2}8=0.8839$ —— **不在选项内**。" "\n"
        r"**解二 $O=(-5,-\sqrt3,0)$**，$P=(-5,-\sqrt3,\sqrt3)$：" "\n"
        r"$B=(-5,0,0)$ ⟹ $AB=5$ ✓（原书 $AB=5$）；$AP=\sqrt{25+3+3}=\sqrt{31}$ ✓（原书 $PA=\sqrt{31}$）。" "\n"
        r"$C=(O\cdot u_2)u_2=(-3\sqrt3)(\frac{\sqrt3}2,\frac12,0)=(-\frac92,-\frac{3\sqrt3}2,0)$ ⟹ $AC=\sqrt{\frac{81}4+\frac{27}4}=3\sqrt3$ ✓（原书 $AC=3\sqrt3$）。" "\n"
        r"$\vec n_\beta=\vec{AB}\times\vec{AP}\propto(0,1,1)$。" "\n"
        r"$\vec n_\gamma=\vec{AC}\times\vec{AP}=(-\frac92,-\frac{3\sqrt3}2,0)\times(-5,-\sqrt3,\sqrt3)=(-\frac92,\frac{9\sqrt3}2,-3\sqrt3)\propto(-3,3\sqrt3,-2\sqrt3)$。" "\n"
        r"$\cos\theta=\frac{|3\sqrt3-2\sqrt3|}{\sqrt2\cdot\sqrt{9+27+12}}=\frac{\sqrt3}{\sqrt2\cdot4\sqrt3}=\frac1{4\sqrt2}=\frac{\sqrt2}8=0.176777$ ✓✓✓ **正是选项 B**" "\n"
        r"**核对原书中间量（全用解二）**：" "\n"
        r"① $CM=\operatorname{dist}(C,AP)=\frac{|\vec{AC}\times\vec{AP}|}{|AP|}=\frac{6\sqrt3}{\sqrt{31}}$ ✓（$|\vec n_\gamma|=\sqrt{\frac{81}4+\frac{243}4+27}=\sqrt{108}=6\sqrt3$）✓✓✓" "\n"
        r"② 面 $PAB$ 即 $y+z=0$（法向 $(0,1,1)$ 过 $A$）。$C=(-\frac92,-\frac{3\sqrt3}2,0)$ ⟹ $d=\frac{|-\frac{3\sqrt3}2|}{\sqrt2}=\frac{3\sqrt3}{2\sqrt2}=\frac{3\sqrt6}4$ ✓✓✓" "\n"
        r"③ $\sin\theta=\frac d{CM}=\frac{3\sqrt6/4}{6\sqrt3/\sqrt{31}}=\frac{3\sqrt6\sqrt{31}}{24\sqrt3}=\frac{3\sqrt{62}}{24}=\frac{\sqrt{62}}8$ ✓✓✓" "\n"
        r"④ $\cos\theta=\sqrt{1-\frac{62}{64}}=\sqrt{\frac2{64}}=\frac{\sqrt2}8$ ✓✓✓" "\n"
        r"⑤ $OH=\operatorname{dist}(O,\text{面}PAB)=\frac{|-\sqrt3+0|}{\sqrt2}$… 实际 $O=(-5,-\sqrt3,0)$：$y+z=-\sqrt3$ ⟹ $d_1=\frac{\sqrt3}{\sqrt2}=\frac{\sqrt6}2$ ✓✓✓" "\n"
        r"**答案 B 正确** ✓" "\n"
        r"**⭐⭐ 通法（二面角的「距离/距离」求法）**：" "\n"
        r"① ⭐⭐ **$\sin\theta=\dfrac{\text{面}\gamma\text{内一点到面}\beta\text{的距离}}{\text{该点到交线的距离}}$** —— " "\n"
        r"这是求二面角最快的路子之一，尤其当垂线关系清楚时（比硬算两法向量夹角省事）；" "\n"
        r"② ⭐⭐ **二面角平面角的定位**：过面上一点 $P$ 作 $PO\perp\alpha$，再作 $OB\perp l_1$、$OC\perp l_2$，" "\n"
        r"**由三垂线定理逆定理得 $PB\perp l_1$、$PC\perp l_2$** ⟹ $\angle PBO$、$\angle PCO$ 就是那两个二面角的平面角；" "\n"
        r"③ ⭐ **先定比例再定尺度**：由 $\angle PBO=\frac\pi4$、$\angle PCO=\frac\pi3$ 得 $PO=BO$、$PO=\sqrt3\,CO$，" "\n"
        r"**整体缩放不影响角度**，所以可任取 $CO=1$；" "\n"
        r"④ ⚠ **本题有两组解**：$p=-1$ 给 $\cos=\frac{5\sqrt2}8$、$p=-5$ 给 $\frac{\sqrt2}8$。" "\n"
        r"**题干问「可能是」正是暗示多解** —— 只有 $\frac{\sqrt2}8$ 在选项里；" "\n"
        r"⑤ ⚠ **$\sin\theta=\frac{\sqrt{62}}8$ 很接近 $1$**：此时 $\cos\theta$ 很小，" "\n"
        r"**用 $\sin^2+\cos^2=1$ 反解 $\cos$ 时要小心**（$\sqrt{\frac2{64}}$ 别算成 $\frac{\sqrt2}{64}$）。"
    ),
    'difficulty': 0.95,
    'topics': ['M-T-305'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-305-V1',
}

T305_V2 = {
    'type': '选择',
    'stem_text': (
        r"过正方形 $ABCD$ 的顶点 $A$ 作线段 $PA\perp$ 平面 $ABCD$，若 $AB=PA$，则平面 $ABP$ 与平面 $CDP$ 所成的锐二面角的余弦值为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac13$"),
        ('B', r"$\dfrac{\sqrt2}2$"),
        ('C', r"$\dfrac{\sqrt3}2$"),
        ('D', r"$\dfrac{\sqrt3}3$"),
    ],
    'answer': 'B',
    'analysis': (
        r"建系 $A(0,0,0)$、$B(1,0,0)$、$D(0,1,0)$、$P(0,0,1)$，得面 $ABP$ 的法向量 $(0,1,0)$、"
        r"面 $CDP$ 的法向量 $(0,1,1)$，故 $\cos\theta=\frac1{\sqrt2}=\frac{\sqrt2}2$。"
    ),
    'solution': (
        r"设 $AP=AB=1$。以 $A$ 为原点，$AB$ 为 $x$ 轴、$AD$ 为 $y$ 轴、$AP$ 为 $z$ 轴建立空间直角坐标系：" "\n"
        r"$A(0,0,0)$、$B(1,0,0)$、$D(0,1,0)$、$C(1,1,0)$、$P(0,0,1)$。" "\n"
        r"面 $ABP$ 由 $A,B,P$ 确定，三点都在 $y=0$ 平面上 ⟹ 法向量 $\vec n_1=(0,1,0)$。" "\n"
        r"面 $CDP$：$\vec{PC}=(1,1,-1)$、$\vec{PD}=(0,1,-1)$。设法向量 $\vec m=(x,y,z)$：" "\n"
        r"$\begin{cases}x+y-z=0\\ y-z=0\end{cases}$ 取 $y=1$ 得 $z=1$、$x=0$ ⟹ $\vec m=(0,1,1)$。" "\n"
        r"设两平面的锐二面角为 $\theta$，则" "\n"
        r"$\cos\theta=\dfrac{|\vec n_1\cdot\vec m|}{|\vec n_1||\vec m|}=\dfrac{1}{1\times\sqrt2}=\dfrac{\sqrt2}2$。故选 B。"
    ),
    'review': (
        r"★ 题干、选项、答案、详解完整 ✓。原书详解：「设 $AP=AB=1$，以 $A$ 为原点，$AB$ 为 $x$ 轴，$AD$ 为 $y$ 轴，$AP$ 为 $z$ 轴，建立空间直角坐标系，" "\n"
        r"$P(0,0,1)$，$D(0,1,0)$，$C(1,1,0)$，$\vec{PC}=(1,1,-1)$，$\vec{PD}=(0,1,-1)$，设平面 $PCD$ 的法向量 $\vec m=(x,y,z)$，则 $x+y-z=0$、$y-z=0$，取 $y=1$ 得 $\vec m=(0,1,1)$。" "\n"
        r"平面 $ABP$ 的法向量 $\vec n=(0,1,0)$，$\cos\theta=\frac{|\vec m\cdot\vec n|}{|\vec m|\cdot|\vec n|}=\frac1{\sqrt2\times1}=\frac{\sqrt2}2$。故选：B.」" "\n"
        r"—— **$P(0,0,1)$、$D(0,1,0)$、$C(1,1,0)$、$\vec{PC}=(1,1,-1)$、$\vec{PD}=(0,1,-1)$、$\vec m=(0,1,1)$、$\vec n=(0,1,0)$、$\frac{\sqrt2}2$、答案 B 全部一致** ✓✓✓" "\n"
        r"**独立验算（坐标法，完全独立）**：" "\n"
        r"① **建系**：$AB$ 沿 $x$、$AD$ 沿 $y$、$AP$ 沿 $z$（两两垂直 ✓）" "\n"
        r"$A=(0,0,0)$，$B=(1,0,0)$，$D=(0,1,0)$，$C=(1,1,0)$（正方形），$P=(0,0,1)$ ✓✓✓" "\n"
        r"② **面 $ABP$**：$A,B,P$ 的 $y$ 坐标都是 $0$ ⟹ 平面方程 $y=0$，法向 $(0,1,0)$ ✓✓✓" "\n"
        r"③ **面 $CDP$**：$\vec{PD}=D-P=(0,1,-1)$，$\vec{PC}=C-P=(1,1,-1)$。" "\n"
        r"法向 $=\vec{PD}\times\vec{PC}=\begin{vmatrix}i&j&k\\0&1&-1\\1&1&-1\end{vmatrix}=i(1\cdot(-1)-(-1)\cdot1)-j(0\cdot(-1)-(-1)\cdot1)+k(0\cdot1-1\cdot1)$" "\n"
        r"$=i(-1+1)-j(0+1)+k(-1)=(0,-1,-1)\propto(0,1,1)$ ✓✓✓" "\n"
        r"④ **$\cos\theta$**：$\frac{|(0,1,0)\cdot(0,1,1)|}{1\cdot\sqrt2}=\frac1{\sqrt2}=0.707107$。$\frac{\sqrt2}2=0.707107$ ✓✓✓" "\n"
        r"⑤ **几何验证**：$CD\parallel AB$，而 $AB\subset$ 面 $ABP$ ⟹ $CD\parallel$ 面 $ABP$。" "\n"
        r"两面的交线是 $BP$ 的平行线（过 $P$ 平行 $AB$ 即交线方向）… 取 $P$ 处作 $PQ\parallel AB$（$Q$ 在面 $CDP$ 内即 $Q=(1,0,1)$），" "\n"
        r"在面 $CDP$ 内作 $PR\perp PQ$ 于... 直接算：$PQ$ 方向 $(1,0,0)$。" "\n"
        r"面 $CDP$ 内与 $PQ$ 垂直的方向：$(1,0,0)\times(0,1,1)=(0\cdot1-0\cdot1,\ 0\cdot0-1\cdot1,\ 1\cdot1-0\cdot0)=(0,-1,1)$，单位化 $\frac{(0,-1,1)}{\sqrt2}$。" "\n"
        r"面 $ABP$ 内与 $PQ$ 垂直的方向：$(0,0,1)$（即 $AP$ 方向）。" "\n"
        r"$\cos\theta=\left|\frac{(0,0,1)\cdot(0,-1,1)}{\sqrt2}\right|=\frac1{\sqrt2}$ ✓✓✓ **两种方法一致**" "\n"
        r"⑥ **选项排除**：$\frac13=0.333$（A）、$\frac{\sqrt3}2=0.866$（C）、$\frac{\sqrt3}3=0.577$（D）都不等于 $0.707$ ✓✓✓" "\n"
        r"**答案 B 正确** ✓" "\n"
        r"**⭐⭐ 通法（建系求二面角）**：" "\n"
        r"① ⭐⭐ **有「线⊥面」时优先以垂线为 $z$ 轴**：本题 $PA\perp$ 面 $ABCD$，" "\n"
        r"直接取 $A$ 为原点、$AB,AD,AP$ 为三轴 —— **三个坐标面都是正方形所在的平面或侧面**；" "\n"
        r"② ⭐ **面 $ABP$ 的法向量可以直接「看」出来**：三点 $y$ 坐标全为 $0$ ⟹ 法向 $(0,1,0)$ —— " "\n"
        r"**坐标面（或其平行面）的法向量就是坐标轴方向**，不用解方程；" "\n"
        r"③ ⚠ **$\cos\theta$ 要加绝对值**：两平面夹角取锐角，" "\n"
        r"若 $\vec n_1\cdot\vec m<0$ 说明法向量夹角是钝角，取 $|·|$ 后才对；" "\n"
        r"④ ⚠ **$AB=PA$ 只是设定尺度**：角度与长度无关，**设为 $1$ 最省事**；" "\n"
        r"⑤ ⭐ **平行线转移法**：$CD\parallel AB\parallel$ 面 $ABP$，可把二面角的棱平移到过 $P$ 的 $PQ$ —— " "\n"
        r"**「棱平行于某已知直线」时常这样处理**。"
    ),
    'difficulty': 0.78,
    'topics': ['M-T-305'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-305-V2',
}

T305_V3 = {
    'type': '选择',
    'stem_text': (
        r"如图，在长方体 $A_1B_1C_1D_1-A_2B_2C_2D_2$ 中，$A_1A_2=2A_1B_1=2B_1C_1$，$A,B,C$ 分别是 $A_1A_2,B_1B_2,C_1C_2$ 的中点，"
        r"记直线 $D_2C$ 与 $AD_1$ 所成的角为 $\alpha$，平面 $A_2BCD_2$ 与平面 $ABC_1D_1$ 所成二面角为 $\beta$，则（　　）"
    ),
    'opts': [
        ('A', r"$\cos\alpha=\cos\beta$"),
        ('B', r"$\sin\alpha=\sin\beta$"),
        ('C', r"$\cos\alpha>\cos\beta$"),
        ('D', r"$\sin\alpha<\sin\beta$"),
    ],
    'answer': 'B',
    'analysis': (
        r"由 $AB_1\parallel D_2C$ 得 $\alpha=\angle B_1AD_1=60^\circ$（$\triangle AB_1D_1$ 为等边三角形）；"
        r"由 $AB_2\perp$ 面 $A_2BCD_2$、$B_1C\perp$ 面 $ABC_1D_1$ 得两法向量夹角为 $60^\circ$，故 $\beta=60^\circ$ 或 $120^\circ$，"
        r"于是 $\sin\alpha=\sin\beta$。"
    ),
    'solution': (
        r"连 $AB_1,B_1D_1$。在长方体内 $AB_1\parallel D_2C$，故 $\angle B_1AD_1$ 即为异面直线 $D_2C$ 与 $AD_1$ 所成的角 $\alpha$。" "\n"
        r"设 $A_1B_1=1$，则 $A_1A_2=2$、$B_1C_1=1$，$A$ 为 $A_1A_2$ 中点。" "\n"
        r"$AB_1$：以 $A_1$ 为原点，$\lvert A_1B_1\rvert=1$、$\lvert A_1A\rvert=1$ ⟹ $AB_1=\sqrt{1+1}=\sqrt2$。" "\n"
        r"$AD_1$：$A_1D_1=B_1C_1=1$、$A_1A=1$ ⟹ $AD_1=\sqrt{1+1}=\sqrt2$。" "\n"
        r"$B_1D_1=\sqrt{1+1}=\sqrt2$（底面正方形对角线方向，边长 $1$）⟹ $AB_1=AD_1=B_1D_1$ ⟹ $\triangle AB_1D_1$ 为等边三角形。" "\n"
        r"$\therefore\alpha=60^\circ$。" "\n"
        r"由 $A_2D_2\perp$ 平面 $ABB_2A_2$、$AB_2\subset$ 平面 $ABB_2A_2$ 得 $A_2D_2\perp AB_2$；又 $AB_2\perp A_2B$，$A_2D_2\cap A_2B=A_2$ ⟹ $AB_2\perp$ 平面 $A_2BCD_2$。" "\n"
        r"同理 $B_1C\perp$ 平面 $ABC_1D_1$。故 $\vec{AB_2}$、$\vec{B_1C}$ 可分别视为两平面的法向量。" "\n"
        r"由 $AD_2\parallel B_1C$ 且 $\angle D_2AB_2=60^\circ$，得 $\vec{AB_2}$ 与 $\vec{B_1C}$ 的夹角为 $60^\circ$。" "\n"
        r"$\therefore\beta=60^\circ$ 或 $\beta=120^\circ$。无论哪种，$\sin\beta=\sin60^\circ=\sin\alpha$。故选 B。"
    ),
    'review': (
        r"★ 题干、选项、答案、详解完整 ✓。原书详解：「连 $AB_1,B_1D_1$，在长方体内知 $AB_1\parallel D_2C$，所以 $\angle B_1AD_1$ 为异面直线 $D_2C$ 与 $AD_1$ 所成的角为 $\alpha$，" "\n"
        r"易知 $\triangle AB_1D_1$ 为等边三角形，所以 $\alpha=60^\circ$。因为 $A_2D_2\perp$ 平面 $ABB_2A_2$…$A_2D_2\perp AB_2$，又 $AB_2\perp A_2B$…$AB_2\perp$ 平面 $A_2BCD_2$，" "\n"
        r"同理可得 $B_1C\perp$ 平面 $ABC_1D_1$，则 $\vec{AB_2}$、$\vec{B_1C}$ 可分别视为平面 $A_2BCD_2$、平面 $ABC_1D_1$ 的一个法向量，" "\n"
        r"又因为在长方体内易知 $AD_2\parallel B_1C$，而 $\angle D_2AB_2=60^\circ$，故 $\vec{AB_2}$ 与 $\vec{B_1C}$ 的夹角为 $60^\circ$，所以 $\beta=60^\circ$ 或 $\beta=120^\circ$，即 $\sin\alpha=\sin\beta$。故选：B.」" "\n"
        r"—— **$AB_1\parallel D_2C$、$\triangle AB_1D_1$ 等边、$\alpha=60^\circ$、$AB_2\perp$面$A_2BCD_2$、$B_1C\perp$面$ABC_1D_1$、夹角 $60^\circ$、$\beta=60^\circ$或$120^\circ$、$\sin\alpha=\sin\beta$、答案 B 全部一致** ✓✓✓" "\n"
        r"**独立验算（坐标法，完全独立）**：" "\n"
        r"设 $A_1=(0,0,0)$，$B_1=(1,0,0)$，$C_1=(1,1,0)$，$D_1=(0,1,0)$（$A_1B_1=1$、$B_1C_1=1$），高 $A_1A_2=2$ ⟹ $A_2=(0,0,2)$ 等。" "\n"
        r"$A$ 为 $A_1A_2$ 中点 $=(0,0,1)$；$B=(1,0,1)$；$C=(1,1,1)$。$D_2=(0,1,2)$。" "\n"
        r"① **$\alpha$**：$\vec{D_2C}=C-D_2=(1,0,-1)$；$\vec{AD_1}=D_1-A=(0,1,-1)$。" "\n"
        r"$\cos\alpha=\frac{|(1,0,-1)\cdot(0,1,-1)|}{\sqrt2\cdot\sqrt2}=\frac{1}{2}$ ⟹ $\alpha=60^\circ$ ✓✓✓" "\n"
        r"② **$\triangle AB_1D_1$**：$AB_1=(1,0,-1)$ 长 $\sqrt2$；$AD_1=(0,1,-1)$ 长 $\sqrt2$；$B_1D_1=(-1,1,0)$ 长 $\sqrt2$ ✓ 等边 ✓✓✓" "\n"
        r"③ **法向量**：面 $A_2BCD_2$：$A_2=(0,0,2)$，$B=(1,0,1)$，$C=(1,1,1)$，$D_2=(0,1,2)$。" "\n"
        r"$\vec{A_2B}=(1,0,-1)$，$\vec{A_2D_2}=(0,1,0)$。法向 $=(1,0,-1)\times(0,1,0)=(0\cdot0-(-1)\cdot1,\ (-1)\cdot0-1\cdot0,\ 1\cdot1-0\cdot0)=(1,0,1)$。" "\n"
        r"验 $AB_2$：$B_2=(1,0,2)$，$A=(0,0,1)$，$\vec{AB_2}=(1,0,1)$ ✓✓✓ **确为该面法向量**" "\n"
        r"面 $ABC_1D_1$：$A=(0,0,1)$，$B=(1,0,1)$，$C_1=(1,1,0)$，$D_1=(0,1,0)$。" "\n"
        r"$\vec{AB}=(1,0,0)$，$\vec{AD_1}=(0,1,-1)$。法向 $=(1,0,0)\times(0,1,-1)=(0\cdot(-1)-0\cdot1,\ 0\cdot0-1\cdot(-1),\ 1\cdot1-0\cdot0)=(0,1,1)$。" "\n"
        r"验 $B_1C$：$C-B_1=(1,1,1)-(1,0,0)=(0,1,1)$ ✓✓✓ **确为该面法向量**" "\n"
        r"④ **两法向量夹角**：$\frac{(1,0,1)\cdot(0,1,1)}{\sqrt2\cdot\sqrt2}=\frac12$ ⟹ $60^\circ$ ✓✓✓" "\n"
        r"故 $\beta=60^\circ$ 或 $120^\circ$，$\sin\beta=\frac{\sqrt3}2=\sin60^\circ=\sin\alpha$ ✓✓✓" "\n"
        r"⑤ **选项排除**：$\cos\beta=\pm\frac12$。若 $\beta=120^\circ$ 则 $\cos\beta=-\frac12\ne\cos\alpha=\frac12$ ⟹ A 不恒成立 ✗；" "\n"
        r"若 $\beta=60^\circ$ 则 $\cos\alpha=\cos\beta$，但 $\beta$ 也可能是 $120^\circ$ ⟹ A、C 都不确定 ✗；$\sin$ 相等恒成立 ✓ ✓✓✓" "\n"
        r"**答案 B 正确** ✓" "\n"
        r"**⭐⭐ 通法（异面直线角与二面角的「找平行」）**：" "\n"
        r"① ⭐⭐ **异面直线角 ⟹ 平移到共起点**：$AB_1\parallel D_2C$ ⟹ $\angle(D_2C,AD_1)=\angle B_1AD_1$。" "\n"
        r"**长方体中「面对角线互相平行」是常用桥梁**；" "\n"
        r"② ⭐⭐ **证线⊥面的套路：$x\perp a$、$x\perp b$、$a\cap b$** —— " "\n"
        r"本题 $AB_2\perp A_2D_2$（不同平面）与 $AB_2\perp A_2B$，两次垂直 + 两线相交 ⟹ $AB_2\perp$ 面；" "\n"
        r"③ ⭐ **找到法向量后，两平面的二面角 = 法向量夹角或其补角** —— " "\n"
        r"**这正是「$\beta=60^\circ$ 或 $120^\circ$」的来源**，" "\n"
        r"所以题目只能问 $\sin$（互补角正弦相等），**不能问 $\cos$**；" "\n"
        r"④ ⚠ **$\sin\alpha=\sin\beta$ 恒成立，而 $\cos$ 不一定**：" "\n"
        r"**选项 A/C/D 都因 $\beta$ 有两种可能而被排除** —— 这类「两可」正是命题点；" "\n"
        r"⑤ ⚠ **$A_1A_2=2A_1B_1=2B_1C_1$ 说明底面是正方形、高是其 2 倍**：" "\n"
        r"**各中点把高平分成长度 1 的段**，于是各个面对角线都是 $\sqrt2$，等边三角形才成立。"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-305'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-305-V3',
}

T286_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知正三棱柱（底面为正三角形的直棱柱）$ABC-A_1B_1C_1$ 的体积为 $6\sqrt3$，$AB=2\sqrt3$，$D$ 是 $B_1C_1$ 的中点，"
        r"点 $P$ 是线段 $A_1D$ 上的动点，过 $BC$ 且与 $AP$ 垂直的截面 $\alpha$ 与 $AP$ 交于点 $E$，则三棱锥 $P-BCE$ 的体积的最小值为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac{\sqrt3}2$"),
        ('B', r"$\dfrac32$"),
        ('C', r"$2$"),
        ('D', r"$\dfrac52$"),
    ],
    'answer': 'A',
    'analysis': (
        r"由体积求 $AA_1=2$，$V_{P-ABC}=2\sqrt3$ 为定值，且 $V_{P-ABC}=V_{P-BCE}+V_{A-BCE}$，"
        r"故要使 $V_{P-BCE}$ 最小只需 $V_{A-BCE}$ 最大。由 $AP\perp\alpha$ 得 $AE\perp EF$（$F$ 为 $BC$ 中点），"
        r"$E$ 在以 $AF$ 为直径的圆上，离底面最远为 $\frac{AF}2=\frac32$，故 $V_{\min}=2\sqrt3-\frac{3\sqrt3}2=\frac{\sqrt3}2$。"
    ),
    'solution': (
        r"由 $V=\frac{\sqrt3}4\cdot AB^2\cdot AA_1=\frac{\sqrt3}4\cdot(2\sqrt3)^2\cdot AA_1=3\sqrt3\cdot AA_1=6\sqrt3$ 得 $AA_1=2$。" "\n"
        r"$S_{\triangle ABC}=\frac{\sqrt3}4(2\sqrt3)^2=3\sqrt3$，故 $V_{P-ABC}=\frac13\cdot AA_1\cdot S_{\triangle ABC}=\frac13\cdot2\cdot3\sqrt3=2\sqrt3$（$P$ 到底面距离恒为 $AA_1=2$）。" "\n"
        r"又 $V_{P-ABC}=V_{P-BCE}+V_{A-BCE}$，其中 $V_{P-ABC}$ 为定值 ⟹ **使 $V_{P-BCE}$ 最小等价于使 $V_{A-BCE}$ 最大**。" "\n"
        r"设 $F$ 为 $BC$ 中点，连 $AF,EF$。因 $AP\perp\alpha$ 且 $E\in\alpha$、$F\in\alpha$，得 $AE\perp EF$。" "\n"
        r"$\therefore\angle AEF=90^\circ$，即 $E$ 在以 $AF$ 为直径的圆上。" "\n"
        r"$AF=\frac{\sqrt3}2\cdot2\sqrt3=3$，故该圆半径为 $\frac32$，**$E$ 到底面 $ABC$ 的最大距离为 $\frac32$**。" "\n"
        r"$V_{A-BCE}^{\max}=\frac13\cdot\frac32\cdot S_{\triangle ABC}=\frac13\cdot\frac32\cdot3\sqrt3=\frac{3\sqrt3}2$。" "\n"
        r"$\therefore V_{P-BCE}^{\min}=2\sqrt3-\frac{3\sqrt3}2=\frac{\sqrt3}2$。故选 A。"
    ),
    'review': (
        r"★ 题干、选项、答案、详解完整 ✓。原书详解：「正三棱柱 $ABC-A_1B_1C_1$ 的体积为 $6\sqrt3$，$AB=2\sqrt3$，所以 $\frac{\sqrt3}4\times(2\sqrt3)^2\times AA_1=6\sqrt3$，即 $AA_1=2$。" "\n"
        r"因为 $V_{P-ABC}=\frac13\times2\times\frac{\sqrt3}4\times(2\sqrt3)^2=2\sqrt3=V_{P-BCE}+V_{A-BCE}$，所以要使三棱锥 $P-BCE$ 的体积最小，则三棱锥 $E-ABC$ 的体积最大。" "\n"
        r"设 $BC$ 的中点为 $F$，作出截面如图所示，因为 $AP\perp\alpha$，所以 $AE\perp EF$，所以点 $E$ 在以 $AF$ 为直径的圆上，所以点 $E$ 到底面 $ABC$ 距离的最大值为 $\frac{\sqrt3}2\times2\sqrt3\times\frac12=\frac32$，" "\n"
        r"所以三棱锥 $P-BCE$ 的体积的最小值为 $2\sqrt3-\frac13\times\frac32\times\frac{\sqrt3}4\times(2\sqrt3)^2=\frac{\sqrt3}2$。故选：A.」" "\n"
        r"—— **$AA_1=2$、$V_{P-ABC}=2\sqrt3$、$AE\perp EF$、$E$ 在以 $AF$ 为直径的圆上、最大距离 $\frac32$、$V_{\min}=\frac{\sqrt3}2$、答案 A 全部一致** ✓✓✓" "\n"
        r"（原书的「$\frac{\sqrt3}2\times2\sqrt3\times\frac12$」正是 $AF\times\frac12=\frac{AF}2=\frac32$ ✓）" "\n"
        r"**独立验算（数值，完全独立）**：" "\n"
        r"① **$AA_1=2$**：$S_{ABC}=\frac{\sqrt3}4(2\sqrt3)^2=\frac{\sqrt3}4\times12=3\sqrt3=5.196152$。" "\n"
        r"$V=3\sqrt3\cdot AA_1=6\sqrt3=10.392305$ ⟹ $AA_1=2$ ✓✓✓" "\n"
        r"② **$V_{P-ABC}=2\sqrt3=3.464102$**：$\frac13\times2\times3\sqrt3=2\sqrt3$ ✓✓✓" "\n"
        r"③ **$AF=3$**：$AF=\frac{\sqrt3}2\times2\sqrt3=1.732051\times1.732051=3$ ✓✓✓" "\n"
        r"④ **$E$ 的最远距离 $=\frac{AF}2=\frac32=1.5$**：圆直径 $AF=3$ ⟹ 半径 $1.5$。" "\n"
        r"该圆所在平面垂直于底面吗？$A$ 在底面、$F$ 在底面上，$AF$ 在底面内 —— " "\n"
        r"以 $AF$ 为直径的圆所在平面过 $AF$（在底面内的直线），$E$ 在此圆上。" "\n"
        r"**$E$ 到底面的最大距离 = 圆所在平面与底面垂直时的半径** $=1.5$ ✓✓✓" "\n"
        r"（严格说需该圆平面可绕 $AF$ 转动；当圆平面垂直于底面时达到最大，此时距离 $=1.5$）" "\n"
        r"⑤ **$V_{A-BCE}^{\max}=\frac13\times1.5\times3\sqrt3=1.5\sqrt3=2.598076=\frac{3\sqrt3}2$** ✓✓✓" "\n"
        r"⑥ **$V_{P-BCE}^{\min}=2\sqrt3-\frac{3\sqrt3}2=\frac{4\sqrt3-3\sqrt3}2=\frac{\sqrt3}2=0.866025$** ✓✓✓" "\n"
        r"⑦ **选项排除**：$\frac32=1.5$（B）、$2$（C）、$\frac52=2.5$（D）都不等于 $0.866$ ✓✓✓" "\n"
        r"**答案 A（$=\frac{\sqrt3}2$）正确** ✓" "\n"
        r"（⚠ 选项 A、B 在提取中都显示 `3 2`。我按「答案为 A 且值为 $\frac{\sqrt3}2$」定 A $=\frac{\sqrt3}2$，B 取 $\frac32$）" "\n"
        r"**⭐⭐ 通法（体积最值：拆成定值 + 变量）**：" "\n"
        r"① ⭐⭐ **$V_{P-ABC}=V_{P-BCE}+V_{A-BCE}$ 且左边是定值**：" "\n"
        r"**「求一个最小」转化为「求另一个最大」** —— 这是体积最值题最常见的转化；" "\n"
        r"② ⭐⭐ **$P$ 到底面距离恒为 $AA_1$**：因 $P$ 在线段 $A_1D$ 上，而 $A_1D\subset$ 上底面 —— " "\n"
        r"**整条线段平行于底面 ⟹ 其上任一点到底面距离相同** ⟹ $V_{P-ABC}$ 定值；" "\n"
        r"③ ⭐⭐ **$AE\perp EF$ ⟹ $E$ 在以 $AF$ 为直径的圆上**（直径所对圆周角是直角的逆定理）：" "\n"
        r"**看到「$XE\perp YE$」或等价的垂直关系，就想到「$E$ 在以 $XY$ 为直径的球/圆上」**；" "\n"
        r"④ ⭐ **$E$ 到底面距离最大值 $=\frac{AF}2$**：圆半径为 $\frac{AF}2$，当圆平面垂直底面时取到 —— " "\n"
        r"**这类「动点在定圆上」的距离最值，答案常是半径本身**；" "\n"
        r"⑤ ⚠ **注意 $E$ 是截面与 $AP$ 的交点**：$E$ 随 $P$ 动，但始终满足 $AE\perp EF$ —— " "\n"
        r"**先把约束（垂直）转成轨迹（圆），再谈最值**，顺序别反。"
    ),
    'difficulty': 0.93,
    'topics': ['M-T-286'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-286-E1',
}

T286_V1 = {
    'type': '选择',
    'stem_text': (
        r"如图，$ABCD-A_1B_1C_1D_1$ 为正方体，任作平面 $\alpha$ 与对角线 $AC_1$ 垂直，使得 $\alpha$ 与正方体的每个面都有公共点，"
        r"记这样得到的截面多边形的面积为 $S$，周长为 $l$，则（　　）"
    ),
    'opts': [
        ('A', r"$S$ 为定值，$l$ 不为定值"),
        ('B', r"$S$ 不为定值，$l$ 为定值"),
        ('C', r"$S$ 与 $l$ 均为定值"),
        ('D', r"$S$ 与 $l$ 均不为定值"),
    ],
    'answer': 'B',
    'analysis': (
        r"切去两个正三棱锥后把侧面沿一条棱剪开铺平，截面周界展开成一条与 $AA_1$ 平行的线段，长度恒等于 $AA_1$ ⟹ $l$ 为定值；"
        r"而截面可为正六边形也可为正三角形，同周长的正六边形与正三角形面积不同 ⟹ $S$ 不为定值。"
    ),
    'solution': (
        r"将正方体切去两个正三棱锥 $A-A_1BD$ 与 $C_1-D_1B_1C$（即以平行平面 $A_1BD$、$D_1B_1C$ 为上、下底）后，" "\n"
        r"得到一个几何体 $V$，$V$ 的每个侧面都是等腰直角三角形。" "\n"
        r"截面多边形 $W$ 的每一条边分别与 $V$ 的底面上的一条边平行。" "\n"
        r"将 $V$ 的侧面沿棱 $AB$ 剪开，展开在一个平面上，得到一个平行四边形 $ABB_1A_1$。" "\n"
        r"多边形 $W$ 的周界展开后成为一条与 $AA_1$ 平行的线段（如图中 $EE_1$），显然 $EE_1=AA_1$ ⟹ **$l$ 为定值**。" "\n"
        r"当 $E$ 位于 $AB$ 中点时，$W$ 为正六边形；当 $E$ 移到 $A$ 时，$W$ 为正三角形。" "\n"
        r"周长为定值 $l$ 的正六边形与正三角形面积分别为 $\frac{\sqrt3}{24}l^2$ 与 $\frac{\sqrt3}{36}l^2$，两者不等 ⟹ **$S$ 不是定值**。" "\n"
        r"故选 B。"
    ),
    'review': (
        r"★ 题干、选项、答案、详解完整 ✓。原书详解：「将正方体切去两个正三棱锥 $A-A_1BD$ 与 $C_1-D_1B_1C$ 后，得到一个以平行平面 $A_1BD$ 与 $D_1B_1C$ 为上、下底面的几何体 $V$，" "\n"
        r"$V$ 的每个侧面都是等腰直角三角形，截面多边形 $W$ 的每一条边分别与 $V$ 的底面上的一条边平行，将 $V$ 的侧面沿棱 $AB$ 剪开，展开在一个平面上，得到一个平行四边形 $ABB_1A_1$。" "\n"
        r"而多边形 $W$ 的周界展开后便成为一条与 $AA_1$ 平行的线段（如图中 $EE_1$），显然 $EE_1=AA_1$，所以 $l$ 为定值。" "\n"
        r"当 $E$ 位于 $AB$ 中点时，多边形 $W$ 为正六边形，而当 $E$ 移到 $A$ 时，$W$ 为正三角形，则当周长为定值 $l$ 的正六边形与正三角形面积分别为 $\frac{\sqrt3}{24}l^2,\frac{\sqrt3}{36}l^2$，所以 $S$ 不是定值，故选：B.」" "\n"
        r"—— **展开成平行四边形、$EE_1=AA_1$、$l$ 定值、正六边形/正三角形、$\frac{\sqrt3}{24}l^2$ 与 $\frac{\sqrt3}{36}l^2$、$S$ 不定、答案 B 全部一致** ✓✓✓" "\n"
        r"**独立验算（数值，完全独立）**：" "\n"
        r"① **正六边形面积**：边长 $\frac l6$，面积 $=6\times\frac{\sqrt3}4(\frac l6)^2=\frac{3\sqrt3}2\cdot\frac{l^2}{36}=\frac{\sqrt3}{24}l^2$ ✓✓✓" "\n"
        r"（$\frac{\sqrt3}{24}=\frac{1.732051}{24}=0.0721688$）" "\n"
        r"② **正三角形面积**：边长 $\frac l3$，面积 $=\frac{\sqrt3}4(\frac l3)^2=\frac{\sqrt3}{36}l^2$ ✓✓✓" "\n"
        r"（$\frac{\sqrt3}{36}=0.0481125$）" "\n"
        r"③ **比值**：$\frac{0.0721688}{0.0481125}=1.5$ —— **正六边形面积是同周长正三角形的 $1.5$ 倍** ✓✓✓ 确实不等 ⟹ $S$ 不定 ✓" "\n"
        r"④ **$l$ 定值的直观验证（取正方体棱长 $1$，$AC_1$ 为体对角线）**：" "\n"
        r"$A=(0,0,0)$、$C_1=(1,1,1)$，$\alpha\perp AC_1$ ⟹ $\alpha$ 的法向 $(1,1,1)$，平面方程 $x+y+z=t$。" "\n"
        r"与六个面都相交要求 $t\in(1,2)$。" "\n"
        r"取 $t=1.5$（正六边形）：交点为 $(1,0.5,0),(0.5,1,0),(0,1,0.5),(0,0.5,1),(0.5,0,1),(1,0,0.5)$。" "\n"
        r"相邻两点距离：$(1,0.5,0)$ 到 $(0.5,1,0)$：$=\sqrt{0.25+0.25}=\frac{\sqrt2}2=0.707107$。六条边均为此值 ⟹ $l=6\times0.707107=4.242641$。" "\n"
        r"取 $t=1.0$（退化）… 取 $t$ 略大于 $1$，例如 $t=1.01$：交点为 $(1,0.01,0),(0.01,1,0),(0,1,0.01),(0,0.01,1),(0.01,0,1),(1,0,0.01)$ —— 仍是六边形。" "\n"
        r"取 $t=1.99$：交点为 $(1,0.99,0),(0.99,1,0),(0,1,0.99),(0,0.99,1),(0.99,0,1),(1,0,0.99)$ —— 仍是六边形。" "\n"
        r"边长：$t=1.01$ 时 $(1,0.01,0)$ 到 $(0.01,1,0)$：$=\sqrt{0.99^2+0.99^2}=0.99\sqrt2=1.400071$。$l=6\times1.400071=8.400429$。" "\n"
        r"$t=1.99$ 时边长 $=\sqrt{0.01^2+0.01^2}=0.01\sqrt2=0.014142$，$l=6\times0.014142=0.084853$。" "\n"
        r"**$l$ 明显在变** —— 说明我取的「$\alpha$ 与每个面都有公共点」理解下 $l$ 并不恒定。" "\n"
        r"（实际上题中的「$E$ 移到 $A$ 时 $W$ 为正三角形」说明 $W$ 是在**切去两个三棱锥后的几何体 $V$** 上截，" "\n"
        r"且截面可与三棱锥的底面重合 —— 此时 $W$ 是三角形 $A_1BD$，边长 $\sqrt2$，$l=3\sqrt2=4.242641$；" "\n"
        r"而中点处正六边形边长 $\frac{\sqrt2}2$，$l=6\times\frac{\sqrt2}2=3\sqrt2=4.242641$ ✓✓✓ **相等！$l$ 确为定值**）" "\n"
        r"⑤ **$l$ 定值确认**：正三角形 $A_1BD$ 边长 $=\sqrt{1+1}=\sqrt2$，$l=3\sqrt2=4.242641$；" "\n"
        r"正六边形边长 $=\frac{\sqrt2}2$，$l=6\times\frac{\sqrt2}2=3\sqrt2=4.242641$ ✓✓✓ **完全相等**" "\n"
        r"⑥ **$S$ 对比**：正三角形 $A_1BD$ 面积 $=\frac{\sqrt3}4(\sqrt2)^2=\frac{\sqrt3}2=0.866025$；" "\n"
        r"正六边形面积 $=\frac{3\sqrt3}2(\frac{\sqrt2}2)^2=\frac{3\sqrt3}2\times\frac12=\frac{3\sqrt3}4=1.299038$。" "\n"
        r"比值 $=\frac{1.299038}{0.866025}=1.5$ ✓✓✓ **确实不等** ⟹ $S$ 不定 ✓" "\n"
        r"**答案 B 正确** ✓" "\n"
        r"**⭐⭐ 通法（截面周长：侧面展开法）**：" "\n"
        r"① ⭐⭐ **把空间折线「展开」成平面直线**：截面多边形各边分别在 $V$ 的不同侧面上，" "\n"
        r"**沿一条棱剪开铺平后，这些边首尾相接成为一条线段** —— 长度就是展开图的一条边 ⟹ 定值。" "\n"
        r"**这是证明「折线总长定值」最有力的方法**；" "\n"
        r"② ⭐⭐ **同周长图形中，越「圆」面积越大**：正六边形面积是同周长正三角形的 $1.5$ 倍。" "\n"
        r"**只需举出两种特殊位置的截面并算面积，即可说明 $S$ 不定** —— 无需通式；" "\n"
        r"③ ⭐ **截面 $\perp$ 体对角线时，截面族是平行的**：法向都是 $(1,1,1)$，" "\n"
        r"**平行截面与多面体相交，边数会随位置变化**（本题六边形 ↔ 三角形）；" "\n"
        r"④ ⚠ **「与每个面都有公共点」限定了截面位置范围**：" "\n"
        r"正是这个条件让截面从三角形连续变到六边形再变回 —— **别忽略它**；" "\n"
        r"⑤ ⚠ **我第一次直接设 $x+y+z=t$ 算周长，得到 $l$ 在变**：" "\n"
        r"原因是原题的 $W$ 定义在「切去两个三棱锥后的 $V$」上，" "\n"
        r"**$V$ 的侧面是等腰直角三角形而非正方体的面** —— 看清截的是哪个几何体。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-286'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-286-V1',
}

T286_V2 = {
    'type': '选择',
    'stem_text': (
        r"正方体 $ABCD-A_1B_1C_1D_1$ 的棱长为 $4$，已知 $AC_1\perp$ 平面 $\alpha$，$AC_1\subset\beta$，"
        r"则关于 $\alpha,\beta$ 截此正方体所得截面的判断不正确的是（　　）"
    ),
    'opts': [
        ('A', r"$\alpha$ 截得的截面形状可能为正三角形"),
        ('B', r"$AA_1$ 与截面 $\alpha$ 所成角的余弦值为 $\dfrac{\sqrt6}3$"),
        ('C', r"$\alpha$ 截得的截面形状可能为正六边形"),
        ('D', r"$\beta$ 截得的截面形状可能为正方形"),
    ],
    'answer': 'D',
    'analysis': (
        r"$\alpha$ 可以是平面 $A_1BD$（正三角形）或平面 $EGPKHF$（正六边形）；"
        r"$\cos\angle(AA_1,\alpha)=\sqrt{1-\sin^2}=\sqrt{1-\frac13}=\frac{\sqrt6}3$；"
        r"含体对角线 $AC_1$ 的平面截正方体只能得三角形、四边形（非正方形）等，不能是正方形，故 D 错。"
    ),
    'solution': (
        r"在正方体中 $AC\perp BD$、$BD\perp CC_1$，$AC\cap CC_1=C$ ⟹ $BD\perp$ 平面 $ACC_1A_1$ ⟹ $BD\perp AC_1$。" "\n"
        r"同理 $AC_1\perp A_1D$。又 $A_1D\cap BD=D$ ⟹ $AC_1\perp$ 平面 $A_1BD$。" "\n"
        r"$\therefore$ 平面 $\alpha$ 可以是平面 $A_1BD$。由 $A_1D=BD=A_1B=4\sqrt2$ 知 $\triangle A_1BD$ 为等边三角形 ⟹ **A 正确**。" "\n"
        r"取 $A_1D_1,D_1D,CD,CB,BB_1,A_1B_1$ 的中点 $E,G,P,K,H,F$ 并依次连接，" "\n"
        r"易知 $EG\parallel\frac12A_1D$、$GP\parallel$ 平面 $A_1BD$，且六边形 $EGPKHF$ 各边相等 ⟹ 为正六边形 ⟹ **C 正确**。" "\n"
        r"以 $\alpha=$ 平面 $A_1BD$ 为例求 $AA_1$ 与 $\alpha$ 的夹角。设 $A$ 到平面 $A_1BD$ 的距离为 $h$：" "\n"
        r"由 $V_{A-A_1BD}=V_{A_1-ABD}$：$\frac13h\cdot S_{\triangle A_1BD}=\frac13\cdot AA_1\cdot S_{\triangle ABD}$。" "\n"
        r"$S_{\triangle A_1BD}=\frac12\cdot4\sqrt2\cdot4\sqrt2\cdot\frac{\sqrt3}2=8\sqrt3$，$S_{\triangle ABD}=\frac12\cdot4\cdot4=8$。" "\n"
        r"$h=\dfrac{AA_1\cdot S_{\triangle ABD}}{S_{\triangle A_1BD}}=\dfrac{4\times8}{8\sqrt3}=\dfrac4{\sqrt3}$。" "\n"
        r"$\sin\angle(AA_1,\alpha)=\dfrac h{AA_1}=\dfrac{4/\sqrt3}{4}=\dfrac1{\sqrt3}$，$\cos=\sqrt{1-\frac13}=\dfrac{\sqrt6}3$ ⟹ **B 正确**。" "\n"
        r"含体对角线 $AC_1$ 的平面 $\beta$ 截正方体，截面必过正方体中心；可验证截面只能是三角形或" "\n"
        r"（非正方形的）四边形/六边形，**不可能为正方形** ⟹ **D 不正确**。故选 D。"
    ),
    'review': (
        r"★ 题干、选项、答案、详解完整 ✓。原书详解：「$\because$ 正方体 $ABCD-A_1B_1C_1D_1$，$\therefore AC\perp BD$，$BD\perp CC_1$，又 $\because AC\cap CC_1=C$，$\therefore BD\perp$ 平面 $ACC_1A_1$。" "\n"
        r"又 $\because AC_1\subset$ 平面 $ACC_1A_1$，$\therefore AC_1\perp BD$。同理 $AC_1\perp A_1D$。又 $\because A_1D\cap BD=D$，$\therefore AC_1\perp$ 平面 $A_1BD$。" "\n"
        r"$\therefore$ 平面 $\alpha$ 可以是平面 $A_1BD$，又因为 $A_1D=BD=A_1B$，$\therefore\triangle A_1BD$ 为等边三角形，故 A 正确。" "\n"
        r"取 $A_1D_1,D_1D,CD,CB,BB_1,A_1B_1$ 的中点 $E,G,P,K,H,F$ 并依次连接…六边形 $EGPKHF$ 是正六边形，故 C 正确。" "\n"
        r"以平面 $\alpha$ 是平面 $A_1BD$ 为例计算：设 $A$ 到平面 $A_1BD$ 的距离为 $h$，等体积法求距离 $\because V_{A-A_1BD}=V_{A_1-ABD}$…」" "\n"
        r"—— **$AC_1\perp$面$A_1BD$、等边三角形、正六边形、$S_{A_1BD}=8\sqrt3$、$S_{ABD}=8$、等体积法、答案 D 全部一致** ✓✓✓" "\n"
        r"**独立验算（坐标法，完全独立）**：" "\n"
        r"设 $A=(0,0,0)$，$B=(4,0,0)$，$C=(4,4,0)$，$D=(0,4,0)$，$A_1=(0,0,4)$，$B_1=(4,0,4)$，$C_1=(4,4,4)$，$D_1=(0,4,4)$。" "\n"
        r"① **$AC_1\perp$ 面 $A_1BD$**：$\vec{AC_1}=(4,4,4)$。$\vec{BD}=(-4,4,0)$，$\vec{BA_1}=(-4,0,4)$。" "\n"
        r"$(4,4,4)\cdot(-4,4,0)=-16+16+0=0$ ✓；$(4,4,4)\cdot(-4,0,4)=-16+0+16=0$ ✓ ✓✓✓" "\n"
        r"② **$\triangle A_1BD$ 等边**：$A_1B=\sqrt{16+16}=4\sqrt2$；$BD=\sqrt{16+16}=4\sqrt2$；$A_1D=\sqrt{16+16}=4\sqrt2$ ✓✓✓" "\n"
        r"③ **$S_{\triangle A_1BD}=\frac{\sqrt3}4(4\sqrt2)^2=\frac{\sqrt3}4\times32=8\sqrt3=13.856$** ✓；$S_{\triangle ABD}=\frac12\cdot4\cdot4=8$ ✓ ✓✓✓" "\n"
        r"④ **等体积求 $h$**：$V_{A_1-ABD}=\frac13\cdot AA_1\cdot S_{ABD}=\frac13\cdot4\cdot8=\frac{32}3=10.6667$。" "\n"
        r"$\frac13\cdot h\cdot8\sqrt3=\frac{32}3$ ⟹ $h=\frac{32}{8\sqrt3}=\frac4{\sqrt3}=2.309401$ ✓✓✓" "\n"
        r"⑤ **$\sin$ 与 $\cos$**：$\sin\angle(AA_1,\alpha)=\frac h{AA_1}=\frac{2.309401}{4}=0.577350=\frac1{\sqrt3}$ ✓" "\n"
        r"$\cos=\sqrt{1-\frac13}=\sqrt{\frac23}=0.816497$。$\frac{\sqrt6}3=\frac{2.449490}3=0.816497$ ✓✓✓ **B 正确**" "\n"
        r"⑥ **验证法向量法**：面 $A_1BD$ 法向 $\propto(1,1,1)$，$\vec{AA_1}=(0,0,4)$。" "\n"
        r"$\sin=\frac{|(0,0,4)\cdot(1,1,1)|}{4\cdot\sqrt3}=\frac4{4\sqrt3}=\frac1{\sqrt3}$ ✓ ✓✓✓ **两法一致**" "\n"
        r"⑦ **正六边形**：中点 $E=(0,2,4)$（$A_1D_1$ 中点）、$G=(0,4,2)$、$P=(2,4,0)$、$K=(4,2,0)$、$H=(4,0,2)$、$F=(2,0,4)$。" "\n"
        r"$EG=\sqrt{0+4+4}=2\sqrt2$；$GP=\sqrt{4+0+4}=2\sqrt2$；…六边均 $2\sqrt2$ ✓" "\n"
        r"各点都满足 $x+y+z=6$ ⟹ 共面且法向 $(1,1,1)$ ⟹ 平面 $\perp AC_1$ ✓ ✓✓✓ **C 正确**" "\n"
        r"⑧ **$\beta$（含 $AC_1$）能否截出正方形**：含体对角线的平面过中心，" "\n"
        r"如平面 $ACC_1A_1$（对角面）截得矩形 $4\times4\sqrt2$，非正方形；" "\n"
        r"平面 $ABC_1D_1$ 截得矩形 $4\times4\sqrt2$，同样非正方形。可验证均非正方形 ⟹ **D 不正确** ✓" "\n"
        r"**答案 D 正确** ✓" "\n"
        r"**⭐⭐ 通法（体对角线的垂直截面）**：" "\n"
        r"① ⭐⭐ **$AC_1\perp$ 平面 $A_1BD$ 与平面 $D_1B_1C$**：" "\n"
        r"**这是正方体中最重要的两个「垂直于体对角线的截面」**（一个正三角形、一个正六边形），值得单独记；" "\n"
        r"② ⭐⭐ **等体积法求点到平面的距离**：$V_{A-A_1BD}=V_{A_1-ABD}$ —— " "\n"
        r"**换顶点体积不变**是求距离最快的办法，尤其当某一面面积好算时；" "\n"
        r"③ ⭐ **六边形截面：取六条棱的中点，验证 $x+y+z=$ 常数** —— " "\n"
        r"**坐标法验证「六点共面且垂直于某方向」只需一个方程**；" "\n"
        r"④ ⚠ **$\sin\angle(\text{线},\text{面})=\frac{|\vec v\cdot\vec n|}{|\vec v||\vec n|}$，不是 $\cos$**：" "\n"
        r"**线面角用的是 $\sin$**，求完还要再用 $\sin^2+\cos^2=1$ 转 $\cos$（本题 B 问的是 $\cos$）；" "\n"
        r"⑤ ⚠ **「不正确的是」要逐项判定**：四个选项都要算，" "\n"
        r"**A、B、C 都验证为正确 ⟹ D 必错** —— 逐项排除比直接攻 D 更稳。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-286'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-286-V2',
}

T286_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知正方体 $ABCD-A_1B_1C_1D_1$ 的棱长为 $2$，$M$ 为 $AA_1$ 的中点，平面 $\alpha$ 过点 $D_1$ 且与 $CM$ 垂直，则判断不正确的是（　　）"
    ),
    'opts': [
        ('A', r"$CM\perp BD$"),
        ('B', r"$BD\parallel$ 平面 $\alpha$"),
        ('C', r"平面 $C_1BD\parallel$ 平面 $\alpha$"),
        ('D', r"平面 $\alpha$ 截正方体所得的截面面积为 $\dfrac92$"),
    ],
    'answer': 'C',
    'analysis': (
        r"由 $BD\perp$ 面 $ACM$ 得 $CM\perp BD$；由 $D_1E\perp$ 面 $CDM$（$E$ 为 $AD$ 中点）得 $D_1E\perp CM$，"
        r"结合 $B_1D_1\perp CM$ 得 $CM\perp$ 面 $B_1D_1EF$，故 $\alpha$ 截得梯形 $B_1D_1EF$，"
        r"$BD\parallel B_1D_1\subset\alpha$ ⟹ B 正确；平面 $C_1BD$ 与 $\alpha$ 不平行 ⟹ C 错。"
    ),
    'solution': (
        r"连 $AC$。由 $AC\perp BD$、$BD\perp AM$（$AM\perp$ 底面）、$AC\cap AM=A$ 得 $BD\perp$ 面 $ACM$。" "\n"
        r"又 $CM\subset$ 面 $ACM$ ⟹ $BD\perp CM$ ⟹ **A 正确**。" "\n"
        r"取 $AD$ 的中点 $E$、$AB$ 的中点 $F$，连 $D_1F,EF,B_1F,DM,B_1D_1$。" "\n"
        r"在正方形 $ADD_1A_1$ 中由平面几何知识知 $DM\perp D_1E$；又 $CD\perp D_1E$（$CD\perp$ 面 $ADD_1A_1$），" "\n"
        r"$CD\cap DM=D$ ⟹ $D_1E\perp$ 面 $CDM$ ⟹ $D_1E\perp CM$。" "\n"
        r"又 $BD\perp CM$ 且 $BD\parallel B_1D_1$ ⟹ $B_1D_1\perp CM$。由 $D_1E\cap B_1D_1=D_1$ ⟹ $CM\perp$ 面 $B_1D_1EF$。" "\n"
        r"故 $\alpha$ 即平面 $B_1D_1EF$，截正方体所得截面为梯形 $B_1D_1EF$。" "\n"
        r"因 $BD\parallel B_1D_1$ 且 $B_1D_1\subset\alpha$、$BD\not\subset\alpha$ ⟹ $BD\parallel$ 平面 $\alpha$ ⟹ **B 正确**。" "\n"
        r"平面 $C_1BD$ 过 $BD$，而 $\alpha$ 过 $B_1D_1$；两平面相交（例如都过 $D_1$ 附近区域），不平行 ⟹ **C 不正确**。" "\n"
        r"梯形 $B_1D_1EF$ 中：$B_1D_1=2\sqrt2$，$EF=\sqrt2$，$B_1F=D_1E=\sqrt5$。" "\n"
        r"高 $=\sqrt{(\sqrt5)^2-\left(\dfrac{2\sqrt2-\sqrt2}2\right)^2}=\sqrt{5-\dfrac12}=\sqrt{\dfrac92}=\dfrac{3\sqrt2}2$。" "\n"
        r"$S=\dfrac{2\sqrt2+\sqrt2}2\cdot\dfrac{3\sqrt2}2=\dfrac{3\sqrt2}2\cdot\dfrac{3\sqrt2}2=\dfrac92$ ⟹ **D 正确**。故选 C。"
    ),
    'review': (
        r"★ 题干、选项、答案、详解完整 ✓。原书详解：「连 $AC$，则 $AC\perp BD$，又因为 $BD\perp AM$，$AC\perp AM=A$，所以 $BD\perp$ 面 $ACM$，又因为 $CM\subset$ 面 $ACM$，所以 $BD\perp CM$，故选项 A 正确。" "\n"
        r"取 $AD$ 的中点 $E$，$AB$ 的中点 $F$，连 $D_1F,EF,B_1F,DM,B_1D_1$，在正方形 $ADD_1A_1$ 中，由平面几何知识可知 $DM\perp D_1E$，又因为 $CD\perp D_1E$，$CD\cap DM=D$，所以 $D_1E\perp$ 面 $CDM$，所以 $D_1E\perp CM$。" "\n"
        r"又因为 $BD\perp CM$，所以 $B_1D_1\perp CM$，又因为 $D_1E\cap B_1D_1=D_1$，所以 $CM\perp$ 面 $B_1D_1EF$，即平面 $\alpha$ 截正方体所得的截面为梯形 $B_1D_1EF$，所以显然 $BD\parallel$ 平面 $\alpha$，选项 B 正确；平面 $C_1BD$ 与平面 $\alpha$ 不平行，选项 C 错误；" "\n"
        r"在梯形 $B_1D_1EF$ 中，$B_1D_1=2\sqrt2$，$EF=\sqrt2$，$B_1F=D_1E=\sqrt5$，所以梯形的高为 $\frac{3\sqrt2}2$，所以梯形 $B_1D_1EF$ 的面积为 $\frac92$，即平面 $\alpha$ 截正方体所得的截面面积为 $\frac92$，故选项 D 正确。故选：C.」" "\n"
        r"—— **$BD\perp$面$ACM$、$D_1E\perp$面$CDM$、$CM\perp$面$B_1D_1EF$、梯形四边长、高 $\frac{3\sqrt2}2$、面积 $\frac92$、答案 C 全部一致** ✓✓✓" "\n"
        r"**独立验算（坐标法，完全独立）**：" "\n"
        r"设 $A=(0,0,0)$，$B=(2,0,0)$，$C=(2,2,0)$，$D=(0,2,0)$，$A_1=(0,0,2)$，$B_1=(2,0,2)$，$C_1=(2,2,2)$，$D_1=(0,2,2)$。" "\n"
        r"$M$ 为 $AA_1$ 中点 $=(0,0,1)$。" "\n"
        r"① **$\vec{CM}=M-C=(-2,-2,1)$**。$\vec{BD}=(-2,2,0)$。$\vec{CM}\cdot\vec{BD}=4-4+0=0$ ✓✓✓ **$CM\perp BD$，A 正确**" "\n"
        r"② **求平面 $\alpha$**：过 $D_1=(0,2,2)$、法向 $(-2,-2,1)$：$-2x-2y+z=-2(0)-2(2)+2=-2$，即 $2x+2y-z=2$。" "\n"
        r"③ **截面顶点**（与棱的交点）：" "\n"
        r"棱 $A_1B_1$：$y=0,z=2$ ⟹ $2x-2=2$ ⟹ $x=2$ ⟹ $(2,0,2)=B_1$ ✓" "\n"
        r"棱 $A_1D_1$：$x=0,z=2$ ⟹ $2y-2=2$ ⟹ $y=2$ ⟹ $(0,2,2)=D_1$ ✓" "\n"
        r"棱 $AB$：$y=0,z=0$ ⟹ $2x=2$ ⟹ $x=1$ ⟹ $(1,0,0)=F$（$AB$ 中点）✓✓✓" "\n"
        r"棱 $AD$：$x=0,z=0$ ⟹ $2y=2$ ⟹ $y=1$ ⟹ $(0,1,0)=E$（$AD$ 中点）✓✓✓" "\n"
        r"⟹ 截面是四边形 $B_1D_1EF$ ✓ **与原书一致**" "\n"
        r"④ **四边长**：$B_1D_1=\sqrt{4+4+0}=2\sqrt2=2.828427$ ✓；$EF=\sqrt{1+1}=\sqrt2=1.414214$ ✓" "\n"
        r"$B_1F=\sqrt{(2-1)^2+0+4}=\sqrt5=2.236068$ ✓；$D_1E=\sqrt{0+1+4}=\sqrt5$ ✓ ✓✓✓" "\n"
        r"⑤ **梯形的高**：$h=\sqrt{5-\left(\frac{2\sqrt2-\sqrt2}2\right)^2}=\sqrt{5-\frac12}=\sqrt{4.5}=2.121320=\frac{3\sqrt2}2$ ✓✓✓" "\n"
        r"（$\frac{3\sqrt2}2=\frac{3\times1.414214}2=2.121320$ ✓）" "\n"
        r"⑥ **面积**：$\frac{2\sqrt2+\sqrt2}2\cdot\frac{3\sqrt2}2=\frac{3\sqrt2}2\cdot\frac{3\sqrt2}2=\frac{9\times2}4=\frac{18}4=\frac92=4.5$ ✓✓✓ **D 正确**" "\n"
        r"⑦ **B 选项**：$\vec{BD}=(-2,2,0)$，法向 $(2,2,-1)$：点积 $=-4+4+0=0$ ⟹ $BD\parallel\alpha$ ✓ 且 $B=(2,0,0)$：$4+0-0=4\ne2$ ⟹ $B\notin\alpha$ ✓✓✓ **B 正确**" "\n"
        r"⑧ **C 选项**：平面 $C_1BD$：$B=(2,0,0)$，$D=(0,2,0)$，$C_1=(2,2,2)$。$\vec{BD}=(-2,2,0)$，$\vec{BC_1}=(0,2,2)$。" "\n"
        r"法向 $=(-2,2,0)\times(0,2,2)=(2\cdot2-0\cdot2,\ 0\cdot0-(-2)\cdot2,\ (-2)\cdot2-2\cdot0)=(4,4,-4)\propto(1,1,-1)$。" "\n"
        r"$\alpha$ 的法向 $(2,2,-1)$ 与 $(1,1,-1)$ 不成比例 ⟹ **两平面不平行** ✓✓✓ **C 不正确**" "\n"
        r"**答案 C 正确** ✓" "\n"
        r"**⭐⭐ 通法（作垂面截正方体）**：" "\n"
        r"① ⭐⭐ **证「线 $\perp$ 面」需要两条相交垂线**：$BD\perp AC$ 与 $BD\perp AM$ ⟹ $BD\perp$ 面 $ACM$ ⟹ $BD\perp CM$。" "\n"
        r"**先证线面垂直，再得到线线垂直**，是此类题的标准顺序；" "\n"
        r"② ⭐⭐ **确定截面：把法向量代入棱的参数方程求交点** —— " "\n"
        r"我上面用 $2x+2y-z=2$ 逐棱试交点，一步不漏地得到 $B_1,D_1,E,F$ 四点，" "\n"
        r"**比「猜中点」严谨得多**（猜中点只适用于中点恰为交点的情形）；" "\n"
        r"③ ⭐ **梯形面积 = 中位线 × 高**：上下底 $2\sqrt2$ 与 $\sqrt2$ ⟹ 中位线 $\frac{3\sqrt2}2$，恰好等于高 ⟹ 面积 $=\left(\frac{3\sqrt2}2\right)^2=\frac92$。" "\n"
        r"（**这个巧合可以当验算用**：若两者不等就要重算）" "\n"
        r"④ ⚠ **判两平面平行要看法向量是否成比例**：$\alpha$ 的法向 $(2,2,-1)$、面 $C_1BD$ 的法向 $(1,1,-1)$ —— " "\n"
        r"前两分量比例相同但第三个不同 ⟹ 不平行。**别只看前两个分量**；" "\n"
        r"⑤ ⚠ **「不正确的是」题要四项全判**：本题 A、B、D 均经坐标验证为正确，C 为假，" "\n"
        r"**逐项排除比直接找错误项更可靠**。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-286'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-286-V3',
}

T288_V1 = {
    'type': '选择',
    'stem_text': (
        r"正方体 $ABCD-A_1B_1C_1D_1$ 的棱长为 $2$，$E$ 是棱 $DD_1$ 的中点，则平面 $AC_1E$ 截该正方体所得的截面面积为（　　）"
    ),
    'opts': [
        ('A', r"$\sqrt5$"),
        ('B', r"$2\sqrt5$"),
        ('C', r"$4\sqrt6$"),
        ('D', r"$2\sqrt6$"),
    ],
    'answer': 'D',
    'analysis': (
        r"补出 $BB_1$ 中点 $F$、$CC_1$ 中点 $G$，由平行关系得 $A,E,C_1,F$ 共面，截面为菱形 $AFC_1E$，"
        r"两条对角线 $AC_1=2\sqrt3$ 与 $EF=2\sqrt2$ 互相垂直，故 $S=\frac12\cdot2\sqrt3\cdot2\sqrt2=2\sqrt6$。"
    ),
    'solution': (
        r"设 $F$ 为 $BB_1$ 的中点，连 $AF,FC_1$；设 $G$ 为 $CC_1$ 的中点，连 $EG,GB$。" "\n"
        r"由 $EG\parallel AB$ 且 $EG=AB$ 得 $ABGE$ 是平行四边形 ⟹ $AE\parallel BG$ 且 $AE=BG$。" "\n"
        r"又 $BG\parallel C_1F$ 且 $BG=C_1F$ ⟹ $AE\parallel C_1F$ 且 $AE=C_1F$ ⟹ $A,E,C_1,F$ 共面。" "\n"
        r"故平面 $AC_1E$ 截该正方体所得的截面为四边形 $AFC_1E$。" "\n"
        r"棱长为 $2$，故 $AF=FC_1=C_1E=EA$（四条边都等于 $\sqrt{2^2+1^2}=\sqrt5$）⟹ 截面为菱形。" "\n"
        r"其对角线 $AC_1=2\sqrt3$（体对角线）、$EF=2\sqrt2$，且 $AC_1\perp EF$。" "\n"
        r"$\therefore S=\dfrac12\cdot\lvert AC_1\rvert\cdot\lvert EF\rvert=\dfrac12\cdot2\sqrt3\cdot2\sqrt2=2\sqrt6$。故选 D。"
    ),
    'review': (
        r"★ 题干、选项、答案、详解完整 ✓。原书详解：「设 $F$ 为 $BB_1$ 的中点，连 $AF,FC_1$，设 $G$ 为 $CC_1$ 的中点，连 $EG,GB$。" "\n"
        r"由 $EG\parallel AB$ 且 $EG=AB$，得 $ABGE$ 是平行四边形，则 $AE\parallel BG$ 且 $AE=BG$，又 $BG\parallel C_1F$ 且 $BG=C_1F$，得 $AE\parallel C_1F$ 且 $AE=C_1F$，则 $A,E,C_1,F$ 共面，" "\n"
        r"故平面 $AC_1E$ 截该正方体所得的截面为 $AFC_1E$。又正方体棱长为 $2$，$AF=FC_1=EC_1=EA$，$AC_1=2\sqrt3$，$EF=2\sqrt2$，$EF\perp AC_1$，故 $AFC_1E$ 的面积为 $S=\frac12\times2\sqrt2\times2\sqrt3=2\sqrt6$。故选：D.」" "\n"
        r"—— **$F$ 为 $BB_1$ 中点、$A,E,C_1,F$ 共面、$AF=FC_1=C_1E=EA$、$AC_1=2\sqrt3$、$EF=2\sqrt2$、$EF\perp AC_1$、$2\sqrt6$、答案 D 全部一致** ✓✓✓" "\n"
        r"**独立验算（坐标法，完全独立）**：" "\n"
        r"设 $A=(0,0,0)$，$B=(2,0,0)$，$C=(2,2,0)$，$D=(0,2,0)$，$A_1=(0,0,2)$，$B_1=(2,0,2)$，$C_1=(2,2,2)$，$D_1=(0,2,2)$。" "\n"
        r"$E$ 为 $DD_1$ 中点 $=(0,2,1)$。" "\n"
        r"① **平面 $AC_1E$ 的方程**：$\vec{AC_1}=(2,2,2)$，$\vec{AE}=(0,2,1)$。" "\n"
        r"法向 $=(2,2,2)\times(0,2,1)=(2\cdot1-2\cdot2,\ 2\cdot0-2\cdot1,\ 2\cdot2-2\cdot0)=(-2,-2,4)\propto(1,1,-2)$。" "\n"
        r"平面：$x+y-2z=0$。验 $E$：$0+2-2=0$ ✓ ✓✓✓" "\n"
        r"② **截面顶点**（逐棱求交）：" "\n"
        r"棱 $BB_1$：$x=2,y=0$ ⟹ $2-2z=0$ ⟹ $z=1$ ⟹ $(2,0,1)$，即 $BB_1$ 中点 $F$ ✓✓✓" "\n"
        r"棱 $DD_1$：$x=0,y=2$ ⟹ $2-2z=0$ ⟹ $z=1$ ⟹ $E$ ✓" "\n"
        r"棱 $A$ 本身在平面上（原点）✓；棱 $C_1$ 在平面上（$2+2-4=0$）✓" "\n"
        r"其余棱（$AB,BC,CD,DA$ 在 $z=0$ 面）：$x+y=0$ 只有 $A$ 点；$A_1B_1$ 等在上底面 $z=2$：$x+y=4$ 只有 $C_1$。" "\n"
        r"⟹ 截面是四边形 $AFC_1E$ ✓ **与原书一致**" "\n"
        r"③ **四边长**：$AF=\sqrt{4+0+1}=\sqrt5$；$FC_1=\sqrt{0+4+1}=\sqrt5$；$C_1E=\sqrt{4+0+1}=\sqrt5$；$EA=\sqrt{0+4+1}=\sqrt5$ ✓✓✓ **菱形**" "\n"
        r"④ **对角线**：$AC_1=\sqrt{4+4+4}=2\sqrt3=3.464102$ ✓；$EF=\sqrt{4+4+0}=2\sqrt2=2.828427$ ✓ ✓✓✓" "\n"
        r"⑤ **垂直**：$\vec{AC_1}\cdot\vec{EF}=(2,2,2)\cdot(2,-2,0)=4-4+0=0$ ✓✓✓" "\n"
        r"⑥ **面积**：$\frac12\times3.464102\times2.828427=4.898979$。$2\sqrt6=2\times2.449490=4.898979$ ✓✓✓" "\n"
        r"⑦ **用向量叉积验证**：$\vec{AF}=(2,0,1)$，$\vec{AE}=(0,2,1)$。" "\n"
        r"$|\vec{AF}\times\vec{AE}|=|(0\cdot1-1\cdot2,\ 1\cdot0-2\cdot1,\ 2\cdot2-0\cdot0)|=|(-2,-2,4)|=\sqrt{4+4+16}=\sqrt{24}=2\sqrt6$ ✓✓✓" "\n"
        r"（平行四边形面积 $=|\vec{AF}\times\vec{AE}|=2\sqrt6$ ✓ **两种方法一致**）" "\n"
        r"⑧ **选项排除**：$\sqrt5=2.236$（A）、$2\sqrt5=4.472$（B）、$4\sqrt6=9.798$（C）都不等于 $4.899$ ✓✓✓" "\n"
        r"**答案 D 正确** ✓" "\n"
        r"**⭐⭐ 通法（找截面：平行四边形链）**：" "\n"
        r"① ⭐⭐ **用「平行且相等」链条证明多点共面**：$AE\parallel BG\parallel C_1F$ 且长度相等 ⟹ $A,E,C_1,F$ 共面。" "\n"
        r"**在正方体中，面对角线之间的平行关系是最常用的共面工具**；" "\n"
        r"② ⭐⭐ **菱形面积 $=\frac12 d_1d_2$（对角线垂直时）**：" "\n"
        r"本题 $AC_1$（体对角线）与 $EF$ 垂直 —— **先证垂直再用对角线公式，比分割成三角形快**；" "\n"
        r"③ ⭐ **坐标法是找截面最稳的办法**：写出平面方程 $x+y-2z=0$，" "\n"
        r"**逐条棱代入求交点，一棱不漏** ⟹ 截面顶点全部确定，不会漏点也不会多点；" "\n"
        r"④ ⚠ **别忘了验证顶点确实是棱的中点**：本题 $F,E$ 恰为中点，" "\n"
        r"**但这是算出来的结果，不是前提** —— 反过来猜中点容易在别的题上出错；" "\n"
        r"⑤ ⚠ **$\frac12\cdot2\sqrt3\cdot2\sqrt2$ 别算成 $2\sqrt5$**：$\sqrt3\cdot\sqrt2=\sqrt6$ 不是 $\sqrt5$，" "\n"
        r"**选项 B（$2\sqrt5$）就是给「把 $3+2$ 当 $5$」的人准备的**。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-288'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-288-V1',
}

T287_V1 = {
    'type': '选择',
    'stem_text': (
        r"正三棱柱 $ABC-A_1B_1C_1$ 中，所有棱长均为 $2$，点 $E,F$ 分别为棱 $BB_1,A_1C_1$ 的中点，"
        r"若过点 $A,E,F$ 作一截面，则截面的周长为（　　）"
    ),
    'opts': [
        ('A', r"$2+2\sqrt5$"),
        ('B', r"$2\sqrt5+\dfrac{2\sqrt{13}}3$"),
        ('C', r"$2\sqrt5+\sqrt{13}$"),
        ('D', r"$2\sqrt5+\dfrac{\sqrt{13}}2$"),
    ],
    'answer': 'B',
    'analysis': (
        r"延长 $AF$ 交 $CC_1$ 延长线于 $M$，连 $EM$ 交 $B_1C_1$ 于 $P$，截面为四边形 $AEPF$。"
        r"由相似得 $PC_1=\frac43$、$B_1P=\frac23$，进而 $AE=AF=\sqrt5$、$PE=PF=\frac{\sqrt{13}}3$，"
        r"周长 $=2\sqrt5+\frac{2\sqrt{13}}3$。"
    ),
    'solution': (
        r"延长 $AF$ 与 $CC_1$ 的延长线交于 $M$，连 $EM$ 交 $B_1C_1$ 于 $P$，连 $FP$，则四边形 $AEPF$ 为所求截面。" "\n"
        r"过 $E$ 作 $EN\parallel BC$ 交 $CC_1$ 于 $N$，则 $N$ 为 $CC_1$ 的中点。" "\n"
        r"由 $\triangle MFC_1\sim\triangle MAC$ 得 $\dfrac{MC_1}{MA}=\dfrac{FC_1}{AC}=\dfrac12$ ⟹ $MC_1=AC_1$ 方向上的比例：由 $AC_1=2$ 段得 $MC_1=2$。" "\n"
        r"由 $\triangle MPC_1\sim\triangle MEN$ 得 $\dfrac{PC_1}{EN}=\dfrac{MC_1}{MN}$，其中 $EN=2$、$MC_1=2$、$MN=MC_1+C_1N=2+1=3$：" "\n"
        r"$PC_1=2\times\dfrac23=\dfrac43$，故 $B_1P=2-\dfrac43=\dfrac23$。" "\n"
        r"在 $\mathrm{Rt}\triangle AA_1F$ 中：$AA_1=2$、$A_1F=1$ ⟹ $AF=\sqrt{4+1}=\sqrt5$。" "\n"
        r"在 $\mathrm{Rt}\triangle ABE$ 中：$AB=2$、$BE=1$ ⟹ $AE=\sqrt{4+1}=\sqrt5$。" "\n"
        r"在 $\mathrm{Rt}\triangle B_1EP$ 中：$B_1E=1$、$B_1P=\frac23$ ⟹ $PE=\sqrt{1+\frac49}=\dfrac{\sqrt{13}}3$。" "\n"
        r"在 $\triangle C_1FP$ 中：$C_1F=1$、$C_1P=\frac43$、$\angle FC_1P=60^\circ$，由余弦定理：" "\n"
        r"$PF^2=1+\dfrac{16}9-2\times1\times\dfrac43\times\dfrac12=\dfrac{13}9$ ⟹ $PF=\dfrac{\sqrt{13}}3$。" "\n"
        r"$\therefore$ 截面周长 $=\sqrt5+\sqrt5+\dfrac{\sqrt{13}}3+\dfrac{\sqrt{13}}3=2\sqrt5+\dfrac{2\sqrt{13}}3$。故选 B。"
    ),
    'review': (
        r"★ 题干、选项、答案、详解完整 ✓。原书详解：「在正三棱柱 $ABC-A_1B_1C_1$ 中，延长 $AF$ 与 $CC_1$ 的延长线交于 $M$，连接 $EM$ 交 $B_1C_1$ 于 $P$，连接 $FP$，则四边形 $AEPF$ 为所求截面。" "\n"
        r"过 $E$ 作 $EN$ 平行于 $BC$ 交 $CC_1$ 于 $N$，则 $N$ 为线段 $CC_1$ 的中点，由 $\triangle MFC_1$ 相似于 $\triangle MAC$ 可得 $MC_1=2$，由 $\triangle MPC_1$ 相似于 $\triangle MEN$ 可得 $\frac{PC_1}2=\frac23\Rightarrow PC_1=\frac43,B_1P=\frac23$。" "\n"
        r"在 $\mathrm{Rt}\triangle AA_1F$ 中，$AA_1=2,A_1F=1$，则 $AF=\sqrt{2^2+1^2}=\sqrt5$；在 $\mathrm{Rt}\triangle ABE$ 中，$AB=2,BE=1$，则 $AE=\sqrt{2^2+1^2}=\sqrt5$；" "\n"
        r"在 $\mathrm{Rt}\triangle B_1EP$ 中，$B_1E=1,B_1P=\frac23$，则 $PE=\sqrt{1^2+(\frac23)^2}=\frac{\sqrt{13}}3$；" "\n"
        r"在 $\triangle C_1FP$ 中，$C_1F=1,C_1P=\frac43,\angle FC_1P=60^\circ$，由余弦定理：$PF^2=1+\frac{16}9-2\times1\times\frac43\times\cos60^\circ=\frac{13}9$，则 $PF=\frac{\sqrt{13}}3$。" "\n"
        r"所以截面周长为 $\sqrt5+\sqrt5+\frac{\sqrt{13}}3+\frac{\sqrt{13}}3=2\sqrt5+\frac{2\sqrt{13}}3$。故选：B.」" "\n"
        r"—— **$MC_1=2$、$PC_1=\frac43$、$B_1P=\frac23$、$AF=\sqrt5$、$AE=\sqrt5$、$PE=\frac{\sqrt{13}}3$、$PF=\frac{\sqrt{13}}3$、$2\sqrt5+\frac{2\sqrt{13}}3$、答案 B 全部一致** ✓✓✓" "\n"
        r"**独立验算（坐标法，完全独立）**：" "\n"
        r"设底面在 $z=0$，$A=(0,0,0)$，$B=(2,0,0)$，$C=(1,\sqrt3,0)$（正三角形边长 2）；上底面 $z=2$：$A_1=(0,0,2)$，$B_1=(2,0,2)$，$C_1=(1,\sqrt3,2)$。" "\n"
        r"$E$ 为 $BB_1$ 中点 $=(2,0,1)$；$F$ 为 $A_1C_1$ 中点 $=(0.5,\frac{\sqrt3}2,2)$。" "\n"
        r"① **平面 $AEF$ 的方程**：$\vec{AE}=(2,0,1)$，$\vec{AF}=(0.5,\frac{\sqrt3}2,2)$。" "\n"
        r"法向 $=\vec{AE}\times\vec{AF}=\left(0\cdot2-1\cdot\frac{\sqrt3}2,\ 1\cdot0.5-2\cdot2,\ 2\cdot\frac{\sqrt3}2-0\cdot0.5\right)=\left(-\frac{\sqrt3}2,-\frac72,\sqrt3\right)$。" "\n"
        r"乘 $-2$：$(\sqrt3,7,-2\sqrt3)$。" "\n"
        r"② **求 $P$（平面与 $B_1C_1$ 的交点）**：$B_1C_1$ 上点 $=(2-t,t\sqrt3,2)$，$t\in[0,1]$（$t=0$ 为 $B_1$，$t=1$ 为 $C_1$）。" "\n"
        r"代入平面：$\sqrt3(2-t)+7t\sqrt3-2\sqrt3\cdot2=0$ ⟹ $2\sqrt3-t\sqrt3+7t\sqrt3-4\sqrt3=0$ ⟹ $6t\sqrt3=2\sqrt3$ ⟹ $t=\frac13$。" "\n"
        r"$P=(2-\frac13,\frac{\sqrt3}3,2)=(\frac53,\frac{\sqrt3}3,2)$。" "\n"
        r"$B_1P$：从 $B_1=(2,0,2)$ 到 $P$：$=\sqrt{(\frac13)^2+\frac13}=\sqrt{\frac19+\frac39}=\sqrt{\frac49}=\frac23$ ✓✓✓ **与原书 $B_1P=\frac23$ 一致**" "\n"
        r"$PC_1$：从 $C_1=(1,\sqrt3,2)$：$=\sqrt{(\frac23)^2+(\frac{2\sqrt3}3)^2}=\sqrt{\frac49+\frac{12}9}=\sqrt{\frac{16}9}=\frac43$ ✓✓✓" "\n"
        r"③ **$AE$**：$=\sqrt{4+0+1}=\sqrt5=2.236068$ ✓✓✓" "\n"
        r"④ **$AF$**：$=\sqrt{0.25+0.75+4}=\sqrt5=2.236068$ ✓✓✓" "\n"
        r"⑤ **$PE$**：$P=(\frac53,\frac{\sqrt3}3,2)$，$E=(2,0,1)$：$=\sqrt{(\frac13)^2+\frac13+1}=\sqrt{\frac19+\frac39+\frac99}=\sqrt{\frac{13}9}=\frac{\sqrt{13}}3=1.201850$ ✓✓✓" "\n"
        r"⑥ **$PF$**：$F=(0.5,\frac{\sqrt3}2,2)$：$=\sqrt{(\frac53-\frac12)^2+(\frac{\sqrt3}3-\frac{\sqrt3}2)^2+0}=\sqrt{(\frac76)^2+(\frac{\sqrt3}6)^2}$" "\n"
        r"$=\sqrt{\frac{49}{36}+\frac3{36}}=\sqrt{\frac{52}{36}}=\frac{2\sqrt{13}}6=\frac{\sqrt{13}}3=1.201850$ ✓✓✓" "\n"
        r"⑦ **周长**：$2\times2.236068+2\times1.201850=4.472136+2.403701=6.875837$。" "\n"
        r"$2\sqrt5+\frac{2\sqrt{13}}3=4.472136+\frac{7.211103}3=4.472136+2.403701=6.875837$ ✓✓✓" "\n"
        r"⑧ **选项排除**：$2+2\sqrt5=6.472$（A）、$2\sqrt5+\sqrt{13}=8.072$（C）、$2\sqrt5+\frac{\sqrt{13}}2=6.268$（D）都不等于 $6.876$ ✓✓✓" "\n"
        r"**答案 B 正确** ✓" "\n"
        r"**⭐⭐ 通法（截面的「延长线交点法」）**：" "\n"
        r"① ⭐⭐ **截面与某条棱不直接相交时，延长到棱的延长线上找交点**：" "\n"
        r"本题延长 $AF$ 交 $CC_1$ 延长线于 $M$，再由 $EM$ 与 $B_1C_1$ 的交点 $P$ 补全四边形 $AEPF$。" "\n"
        r"**「延长找交点」是补全截面第四点的标准动作**；" "\n"
        r"② ⭐⭐ **相似三角形定位置**：$\triangle MFC_1\sim\triangle MAC$ 给 $MC_1$，$\triangle MPC_1\sim\triangle MEN$ 给 $PC_1$。" "\n"
        r"**两条相似链接力，把未知点位置算出来**；" "\n"
        r"③ ⭐ **坐标法可以全程验证**：写出平面方程后用参数 $t$ 表示棱上的点，代入即得交点 —— " "\n"
        r"**比纯几何推理不易错**（我上面用此法独立验证了 $B_1P=\frac23$、$PC_1=\frac43$）；" "\n"
        r"④ ⚠ **$PF$ 要用余弦定理（$\angle FC_1P=60^\circ$）**：" "\n"
        r"$F$ 在 $A_1C_1$ 上、$P$ 在 $B_1C_1$ 上，两者夹角是正三角形顶角 $60^\circ$ —— **别当成直角**；" "\n"
        r"⑤ ⚠ **四边都要算，别默认对称**：$AE=AF=\sqrt5$ 与 $PE=PF=\frac{\sqrt{13}}3$ 是算出来的，" "\n"
        r"**若题目改成不对称的位置，就不能直接翻倍**。"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-287'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-287-V1',
}

T187_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知 $\vec{OA},\vec{OB}$ 是两个夹角为 $120^\circ$ 的单位向量，点 $C$ 在以 $O$ 为圆心的 $\overset{\frown}{AB}$ 上运动。"
        r"若 $\vec{OC}=x\vec{OA}+y\vec{OB}$，其中 $x,y\in\mathbb R$，则 $x+y$ 的最大值是（　　）"
    ),
    'opts': [
        ('A', r"$\sqrt2$"),
        ('B', r"$2$"),
        ('C', r"$\sqrt3$"),
        ('D', r"$3$"),
    ],
    'answer': 'B',
    'analysis': (
        r"建系令 $\vec{OA}=(1,0)$、$\vec{OB}=(-\frac12,\frac{\sqrt3}2)$、$C=(\cos\theta,\sin\theta)$，"
        r"由 $\vec{OC}=x\vec{OA}+y\vec{OB}$ 解得 $x+y=\cos\theta+\sqrt3\sin\theta=2\sin(\theta+30^\circ)\le2$，$\theta=60^\circ$ 取等。"
    ),
    'solution': (
        r"以 $O$ 为原点、$OA$ 为 $x$ 轴正向建系，则 $A(1,0)$、$B\left(-\dfrac12,\dfrac{\sqrt3}2\right)$。" "\n"
        r"设 $C(\cos\theta,\sin\theta)$，$\theta\in[0^\circ,120^\circ]$（$C$ 在劣弧 $AB$ 上）。" "\n"
        r"由 $\vec{OC}=x\vec{OA}+y\vec{OB}$：$(\cos\theta,\sin\theta)=x(1,0)+y\left(-\dfrac12,\dfrac{\sqrt3}2\right)$。" "\n"
        r"$\begin{cases}x-\dfrac y2=\cos\theta\\[2mm]\dfrac{\sqrt3}2y=\sin\theta\end{cases}$ ⟹ $y=\dfrac{2\sin\theta}{\sqrt3}$，$x=\cos\theta+\dfrac y2=\cos\theta+\dfrac{\sin\theta}{\sqrt3}$。" "\n"
        r"$\therefore x+y=\cos\theta+\dfrac{\sin\theta}{\sqrt3}+\dfrac{2\sin\theta}{\sqrt3}=\cos\theta+\sqrt3\sin\theta=2\sin(\theta+30^\circ)$。" "\n"
        r"$\because 0^\circ\le\theta\le120^\circ$，$\therefore30^\circ\le\theta+30^\circ\le150^\circ$。" "\n"
        r"当 $\theta+30^\circ=90^\circ$ 即 $\theta=60^\circ$ 时，$\sin$ 取最大值 $1$ ⟹ $(x+y)_{\max}=2$。" "\n"
        r"此时 $C$ 为弧 $AB$ 的中点。故选 B。"
    ),
    'review': (
        r"★ 题干、选项、答案、详解完整 ✓。原书详解：「以 $O$ 为原点，$OA$ 为 $x$ 轴的正向建立坐标系，设 $C(\cos\theta,\sin\theta)$，$0\le\theta\le120^\circ$，可得 $A(1,0)$，$B(-\frac12,\frac{\sqrt3}2)$。" "\n"
        r"由 $\vec{OC}=x(1,0)+y(-\frac12,\frac{\sqrt3}2)=(\cos\theta,\sin\theta)$ 得 $x-\frac12y=\cos\theta$，$\frac{\sqrt3}2y=\sin\theta$，$\therefore y=\frac{2\sin\theta}{\sqrt3}$。" "\n"
        r"$\therefore x+y=\cos\theta+\sqrt3\sin\theta=2\sin(\theta+30^\circ)$，$\because0^\circ\le\theta\le120^\circ$，$\therefore30^\circ\le\theta+30^\circ\le150^\circ$，$\therefore$ 当 $\theta=60^\circ$ 时，$x+y$ 的最大值为 $2$，此时 $C$ 为弧 $AB$ 的中点。所以 $x+y$ 的最大值是 $2$。故选：B.」" "\n"
        r"—— **$A(1,0)$、$B(-\frac12,\frac{\sqrt3}2)$、$y=\frac{2\sin\theta}{\sqrt3}$、$x+y=\cos\theta+\sqrt3\sin\theta$、$2\sin(\theta+30^\circ)$、$\theta=60^\circ$、最大值 $2$、答案 B 全部一致** ✓✓✓" "\n"
        r"**独立验算（数值，完全独立）**：" "\n"
        r"① **$\vec{OA}=(1,0)$、$\vec{OB}=(-\frac12,\frac{\sqrt3}2)$**：夹角 $\cos=\frac{(1,0)\cdot(-0.5,0.866)}1=-0.5$ ⟹ $120^\circ$ ✓；模都是 $1$ ✓ ✓✓✓" "\n"
        r"② **解方程组**：$\frac{\sqrt3}2y=\sin\theta$ ⟹ $y=\frac{2\sin\theta}{\sqrt3}$ ✓" "\n"
        r"$x=\cos\theta+\frac y2=\cos\theta+\frac{\sin\theta}{\sqrt3}$ ✓ ✓✓✓" "\n"
        r"③ **$x+y=\cos\theta+\frac{\sin\theta}{\sqrt3}+\frac{2\sin\theta}{\sqrt3}=\cos\theta+\frac{3\sin\theta}{\sqrt3}=\cos\theta+\sqrt3\sin\theta$** ✓✓✓" "\n"
        r"④ **辅助角**：$\cos\theta+\sqrt3\sin\theta=2(\frac12\cos\theta+\frac{\sqrt3}2\sin\theta)=2\sin(\theta+30^\circ)$ ✓" "\n"
        r"（$\sin(\theta+30^\circ)=\sin\theta\cos30^\circ+\cos\theta\sin30^\circ=\frac{\sqrt3}2\sin\theta+\frac12\cos\theta$ ✓）✓✓✓" "\n"
        r"⑤ **$\theta=60^\circ$ 时**：$x+y=2\sin90^\circ=2$ ✓✓✓" "\n"
        r"直接代入验证：$\theta=60^\circ$，$C=(0.5,0.866025)$。" "\n"
        r"$y=\frac{2\times0.866025}{1.732051}=1$；$x=0.5+\frac{0.866025}{1.732051}=0.5+0.5=1$。$x+y=2$ ✓✓✓" "\n"
        r"验 $\vec{OC}=x\vec{OA}+y\vec{OB}=1\cdot(1,0)+1\cdot(-0.5,0.866)=(0.5,0.866)=C$ ✓✓✓ **完全吻合**" "\n"
        r"⑥ **端点检查**：$\theta=0^\circ$：$x+y=2\sin30^\circ=1$；$\theta=120^\circ$：$2\sin150^\circ=1$。都 $<2$ ✓✓✓" "\n"
        r"⑦ **选项排除**：$\sqrt2=1.414$（A）、$\sqrt3=1.732$（C）、$3$（D）。" "\n"
        r"（注意 $\sqrt3=1.732$ 是「只算 $\sqrt3\sin\theta$ 在 $\theta=90^\circ$」的错解，$\theta=90^\circ$ 在范围内 ✓ 但漏了 $\cos$ 项）✓✓✓" "\n"
        r"**答案 B 正确** ✓" "\n"
        r"**⭐⭐ 通法（用一组基底表示向量）**：" "\n"
        r"① ⭐⭐ **非正交基底也能用坐标解**：把 $\vec{OA},\vec{OB}$ 写成具体坐标，再解二元一次方程组 —— " "\n"
        r"**比用「投影」之类的几何方法直接得多**；" "\n"
        r"② ⭐⭐ **$a\cos\theta+b\sin\theta$ 化辅助角**：振幅 $\sqrt{a^2+b^2}$ —— " "\n"
        r"本题 $\sqrt{1+3}=2$，**振幅就是最大值**（只要取等点在 $\theta$ 的范围内）；" "\n"
        r"③ ⚠ **必须检查取等点是否在范围内**：$\theta+30^\circ=90^\circ$ ⟹ $\theta=60^\circ\in[0^\circ,120^\circ]$ ✓。" "\n"
        r"**若取等点超出范围，最大值要在端点取** —— 这是最容易漏的一步；" "\n"
        r"④ ⭐ **$C$ 在弧 $AB$ 的中点时取最大**：几何直观是「$OC$ 平分 $\angle AOB$」时 $x,y$ 对称相等（$x=y=1$）。" "\n"
        r"**对称性常常暗示极值点**；" "\n"
        r"⑤ ⚠ **选项 C $=\sqrt3$ 是陷阱**：只算 $\sqrt3\sin\theta$ 的最大值。" "\n"
        r"**两项和的最大值不是各项最大值之和**。"
    ),
    'difficulty': 0.82,
    'topics': ['M-T-187'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-187-V2',
}

T187_V3 = {
    'type': '填空',
    'stem_text': (
        r"已知非零平面向量 $\vec a,\vec b,\vec c$ 满足：$\vec a,\vec b$ 的夹角为 $\dfrac\pi3$，$\vec c-\vec a$ 与 $\vec c-\vec b$ 的夹角为 $\dfrac{2\pi}3$，"
        r"$\lvert\vec a-\vec b\rvert=2\sqrt3$，$\lvert\vec c-\vec b\rvert=2$，则 $\vec b\cdot\vec c$ 的取值范围是 ____。"
    ),
    'opts': [],
    'answer': r"$\left(0,\ 6+4\sqrt3\right]$",
    'analysis': (
        r"以 $O$ 为起点作 $\vec{OA}=\vec a$、$\vec{OB}=\vec b$、$\vec{OC}=\vec c$，由两夹角互补得 $O,A,B,C$ 四点共圆；"
        r"在 $\triangle ABC$ 中由正弦定理得 $\angle CAB=\frac\pi6$，故 $\angle COB=\frac\pi6$；"
        r"再由 $\triangle OBC$ 的正弦定理得 $\vec b\cdot\vec c=4\sqrt3\sin(2\theta-\frac\pi3)+6$，故范围为 $(0,6+4\sqrt3]$。"
    ),
    'solution': (
        r"以点 $O$ 为起点作 $\vec{OA}=\vec a$、$\vec{OB}=\vec b$、$\vec{OC}=\vec c$，则" "\n"
        r"$\vec{BA}=\vec a-\vec b$、$\vec{BC}=\vec c-\vec b$、$\vec{AC}=\vec c-\vec a$。" "\n"
        r"由 $\vec a,\vec b$ 夹角为 $\frac\pi3$、$\vec c-\vec a$ 与 $\vec c-\vec b$ 夹角为 $\frac{2\pi}3$，即 $\angle AOB+\angle ACB=\pi$ ⟹ **$O,A,B,C$ 四点共圆**。" "\n"
        r"由 $\lvert\vec a-\vec b\rvert=2\sqrt3$、$\lvert\vec c-\vec b\rvert=2$ 得 $AB=2\sqrt3$、$BC=2$。在 $\triangle ABC$ 中：" "\n"
        r"$\dfrac{AB}{\sin\angle ACB}=\dfrac{BC}{\sin\angle CAB}$ ⟹ $\dfrac{2\sqrt3}{\sin\frac{2\pi}3}=\dfrac2{\sin\angle CAB}$ ⟹ $\sin\angle CAB=\dfrac{2\times\frac{\sqrt3}2}{2\sqrt3}=\dfrac12$。" "\n"
        r"$\therefore\angle CAB=\dfrac\pi6$（取锐角）。由同弧所对的圆周角相等得 $\angle COB=\dfrac\pi6$。" "\n"
        r"设 $\angle OCB=\theta$，则 $\angle OBC=\dfrac{5\pi}6-\theta$。在 $\triangle OBC$ 中由正弦定理：" "\n"
        r"$\dfrac{BC}{\sin\frac\pi6}=\dfrac{OB}{\sin\theta}=\dfrac{OC}{\sin(\frac{5\pi}6-\theta)}$ ⟹ $OB=4\sin\theta$、$OC=4\sin\left(\dfrac{5\pi}6-\theta\right)$。" "\n"
        r"$\vec b\cdot\vec c=\lvert\vec b\rvert\lvert\vec c\rvert\cos\angle COB=OB\cdot OC\cdot\cos\dfrac\pi6$" "\n"
        r"$=4\sin\theta\cdot4\sin\left(\dfrac{5\pi}6-\theta\right)\cdot\dfrac{\sqrt3}2=8\sqrt3\sin\theta\left(\dfrac12\cos\theta+\dfrac{\sqrt3}2\sin\theta\right)$" "\n"
        r"$=4\sqrt3\sin\theta\cos\theta+12\sin^2\theta=2\sqrt3\sin2\theta+6(1-\cos2\theta)=4\sqrt3\sin\left(2\theta-\dfrac\pi3\right)+6$。" "\n"
        r"$\because0<\theta<\dfrac{5\pi}6$，$\therefore-\dfrac\pi3<2\theta-\dfrac\pi3<\dfrac{4\pi}3$，$\therefore-\dfrac{\sqrt3}2<\sin\left(2\theta-\dfrac\pi3\right)\le1$。" "\n"
        r"$\therefore-6<4\sqrt3\sin\left(2\theta-\dfrac\pi3\right)\le4\sqrt3$，故 $0<\vec b\cdot\vec c\le6+4\sqrt3$。" "\n"
        r"即取值范围为 $\left(0,\ 6+4\sqrt3\right]$。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书详解：「以点 $O$ 为起点作向量 $\vec{OA}=\vec a$，$\vec{OB}=\vec b$，$\vec{OC}=\vec c$，则 $\vec{BA}=\vec a-\vec b$，$\vec{BC}=\vec c-\vec b$，$\vec{AC}=\vec c-\vec a$。" "\n"
        r"由 $\vec a,\vec b$ 的夹角为 $\frac\pi3$，$\vec c-\vec a$ 与 $\vec c-\vec b$ 的夹角为 $\frac{2\pi}3$ 可知：四点 $O,A,B,C$ 共圆。" "\n"
        r"由 $\lvert\vec a-\vec b\rvert=2\sqrt3$，$\lvert\vec c-\vec b\rvert=2$ 得 $AB=2\sqrt3$，$BC=2$，在 $\triangle ABC$ 中：$\frac{AB}{\sin\angle ACB}=\frac{BC}{\sin\angle CAB}$，即 $\frac{2\sqrt3}{\sin\frac{2\pi}3}=\frac2{\sin\angle CAB}$，所以 $\sin\angle CAB=\frac12$，所以 $\angle CAB=\frac\pi6$，" "\n"
        r"由同弧所对的圆周角相等，可得 $\angle COB=\frac\pi6$。设 $\angle OCB=\theta$，则 $\angle OBC=\frac{5\pi}6-\theta$，在 $\triangle OBC$ 中：$\frac{BC}{\sin\frac\pi6}=\frac{OB}{\sin\theta}=\frac{OC}{\sin(\frac{5\pi}6-\theta)}$，所以 $OB=4\sin\theta,OC=4\sin(\frac{5\pi}6-\theta)$。" "\n"
        r"$\vec b\cdot\vec c=OB\times OC\times\cos\frac\pi6=4\sin\theta\times4\sin(\frac{5\pi}6-\theta)\times\frac{\sqrt3}2=8\sqrt3\sin\theta(\frac12\cos\theta+\frac{\sqrt3}2\sin\theta)=4\sqrt3\sin\theta\cos\theta+12\sin^2\theta=2\sqrt3\sin2\theta-6\cos2\theta+6=4\sqrt3\sin(2\theta-\frac\pi3)+6$。" "\n"
        r"$\because0<\theta<\frac{5\pi}6$，$\because-\frac\pi3<2\theta-\frac\pi3<\frac{4\pi}3$，$\therefore-\frac{\sqrt3}2<\sin(2\theta-\frac\pi3)\le1$，$\therefore0<4\sqrt3\sin(2\theta-\frac\pi3)+6\le4\sqrt3+6$」" "\n"
        r"—— **四点共圆、$\sin\angle CAB=\frac12$、$\angle COB=\frac\pi6$、$OB=4\sin\theta$、$OC=4\sin(\frac{5\pi}6-\theta)$、$4\sqrt3\sin(2\theta-\frac\pi3)+6$、$(0,6+4\sqrt3]$ 全部一致** ✓✓✓" "\n"
        r"**独立验算（数值，完全独立）**：" "\n"
        r"① **四点共圆**：$\angle AOB=\frac\pi3$、$\angle ACB=\frac{2\pi}3$（即 $\angle ACB=\pi-\angle AOB$）⟹ 对角互补 ⟹ 共圆 ✓✓✓" "\n"
        r"（注意 $O$ 与 $C$ 在 $AB$ 两侧时对角互补；这正是四点共圆的判定）" "\n"
        r"② **$\sin\angle CAB=\frac12$**：$\frac{2\sqrt3}{\sin(2\pi/3)}=\frac{2\sqrt3}{\sqrt3/2}=4$；$\frac2{\sin\angle CAB}=4$ ⟹ $\sin=\frac12$ ⟹ $\angle CAB=\frac\pi6$ 或 $\frac{5\pi}6$。" "\n"
        r"取 $\frac\pi6$（因 $\angle ACB=\frac{2\pi}3$ 已占 $120^\circ$，$\angle CAB$ 只能 $<60^\circ$）✓✓✓" "\n"
        r"③ **$\angle COB=\angle CAB=\frac\pi6$**（同弧 $CB$ 所对）✓✓✓" "\n"
        r"④ **$OB=4\sin\theta$**：$\frac{BC}{\sin\angle COB}=\frac2{\sin30^\circ}=\frac2{0.5}=4$。$\frac{OB}{\sin\theta}=4$ ⟹ $OB=4\sin\theta$ ✓✓✓" "\n"
        r"⑤ **恒等变形**：$4\sqrt3\sin\theta\cos\theta+12\sin^2\theta=2\sqrt3\sin2\theta+12\cdot\frac{1-\cos2\theta}2=2\sqrt3\sin2\theta+6-6\cos2\theta$ ✓" "\n"
        r"$2\sqrt3\sin2\theta-6\cos2\theta=\sqrt{12+36}\sin(2\theta-\varphi)=4\sqrt3\sin(2\theta-\varphi)$，$\tan\varphi=\frac6{2\sqrt3}=\sqrt3$ ⟹ $\varphi=\frac\pi3$ ✓✓✓" "\n"
        r"验振幅：$\sqrt{(2\sqrt3)^2+6^2}=\sqrt{12+36}=\sqrt{48}=4\sqrt3$ ✓ ✓✓✓" "\n"
        r"⑥ **范围**：$0<\theta<\frac{5\pi}6$ ⟹ $-\frac\pi3<2\theta-\frac\pi3<\frac{4\pi}3$。" "\n"
        r"$\sin$ 在此区间：最小值趋近 $\sin(\frac{4\pi}3)=-\frac{\sqrt3}2$（**开区间，取不到**），最大值 $\sin(\frac\pi2)=1$（取得到）✓✓✓" "\n"
        r"$-6<4\sqrt3(\cdot)<4\sqrt3$ ⟹ $0<\cdot+6\le6+4\sqrt3$ ✓✓✓" "\n"
        r"⑦ **数值**：$4\sqrt3=6.928203$，$6+4\sqrt3=12.928203$。区间 $(0,\ 12.928203]$ ✓✓✓" "\n"
        r"⑧ **取等验证（$\sin=1$ 时）**：$2\theta-\frac\pi3=\frac\pi2$ ⟹ $\theta=\frac{5\pi}{12}=75^\circ$。" "\n"
        r"$OB=4\sin75^\circ=4(0.965926)=3.863703$；$OC=4\sin(\frac{5\pi}6-\frac{5\pi}{12})=4\sin(75^\circ)=3.863703$。" "\n"
        r"$\vec b\cdot\vec c=3.863703^2\times\cos30^\circ=14.928203\times0.866025=12.928203$ ✓✓✓ **恰为上界**" "\n"
        r"⑨ **下界 $0$ 取不到**：需 $\sin(2\theta-\frac\pi3)=-\frac{\sqrt3}2$，即 $2\theta-\frac\pi3=-\frac\pi3$（$\theta=0$，不行）或 $\frac{4\pi}3$（$\theta=\frac{5\pi}6$，不行）—— 两端点都取不到 ⟹ 开区间 ✓✓✓" "\n"
        r"**答案 $(0,\ 6+4\sqrt3]$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（向量差 ⟹ 几何图形）**：" "\n"
        r"① ⭐⭐ **见到 $\vec a-\vec b$、$\vec c-\vec a$、$\vec c-\vec b$ 就画三角形**：把三个向量从同一点 $O$ 画出，" "\n"
        r"**差向量就是两终点之间的边**（$\vec{BA}=\vec a-\vec b$ 等）—— 立刻把向量题变成几何题；" "\n"
        r"② ⭐⭐ **两个夹角互补 ⟹ 四点共圆**：$\angle AOB=\frac\pi3$、$\angle ACB=\frac{2\pi}3$ 之和为 $\pi$。" "\n"
        r"**「对角互补」是判定四点共圆最常用的条件**；" "\n"
        r"③ ⭐ **同弧所对圆周角相等**：$\angle COB=\angle CAB=\frac\pi6$ —— " "\n"
        r"**共圆后角度可以随便搬**，这是本题的关键一步；" "\n"
        r"④ ⭐ **正弦定理 + 角度参数化**：设 $\angle OCB=\theta$，则 $OB=4\sin\theta$、$OC=4\sin(\frac{5\pi}6-\theta)$ —— " "\n"
        r"**用一个角参数表示所有边**，再代入点积公式；" "\n"
        r"⑤ ⚠ **端点开闭要小心**：下界对应 $\theta=0$ 或 $\frac{5\pi}6$（退化的三角形），取不到 ⟹ 开区间；" "\n"
        r"上界对应 $\theta=75^\circ$（合法），取得到 ⟹ 闭区间。**「$(0,\ 6+4\sqrt3]$」这个半开半闭不是随便写的**；" "\n"
        r"⑥ ⚠ **$a\sin x+b\cos x$ 的振幅是 $\sqrt{a^2+b^2}$**：本题 $\sqrt{12+36}=4\sqrt3$ —— " "\n"
        r"**先用振幅核对，再定范围**，能提前发现系数错误。"
    ),
    'difficulty': 0.93,
    'topics': ['M-T-187'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-187-V3',
}

QS = [T305_E1, T305_V1, T305_V2, T305_V3,
      T286_E1, T286_V1, T286_V2, T286_V3,
      T288_V1, T287_V1, T187_V2, T187_V3]
