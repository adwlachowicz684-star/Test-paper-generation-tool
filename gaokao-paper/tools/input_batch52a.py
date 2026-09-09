# -*- coding: utf-8 -*-
r"""第52批（上）：解三角形 · 四边形（4 题全录）

来源：2024高中数学热点题型归纳完整解析版.pdf
p165（E1 详解）、p166（V1/V2/V3 题干+详解）

## ★★ 本批的核心思想（原书「提分秘籍」原文）

> 1. 四边形可以**「劈成」俩三角形**
> 2. 四边形可以**「补成」三角形**

四题正好是这两条的应用：

| 题 | 思路 | 手段 |
|---|---|---|
| E1 | 补成三角形 | 延长 $BA,CD$ 交于 $E$，用**极限位置**定范围端点（开区间！） |
| V1 | 劈成两三角形 + 圆 | 建系 ⟹ $A$ 在圆弧上 ⟹ $AC_{\max}=\lvert CE\rvert+R$ |
| V2 | 劈成两三角形 | 对角互补 ⟹ **四点共圆** ⟹ $\angle CBD=\angle DAC$ ⟹ 分类讨论 $\angle BAC$ |
| V3 | 劈成两三角形 | $\triangle ABC$ 余弦定理 + $\triangle BCD$ 余弦定理，最后**有界性**取最大 |

## 四题验算（全部独立推导，与答案吻合）

| 题 | 我的结果 | 答案 |
|---|---|---|
| E1 | $(\sqrt6-\sqrt2,\ \sqrt6+\sqrt2)\approx(1.035,3.864)$ | **A** |
| V1 | $\lvert CE\rvert=17$、$R=10$ ⟹ $AC_{\max}=27$ | **A** |
| V2 | 情形一 $\frac32+1$，情形二 $<\frac34$ ⟹ 最大 $\frac32+1$ | **B** |
| V3 | $BD^{2}=7+2\sqrt6\sin(\alpha-\frac\pi4)\le7+2\sqrt6$ ⟹ $BD_{\max}=\sqrt6+1$ | **C** |
"""

T204_E1 = {
    'type': '选择',
    'stem_text': (
        r"在平面四边形 $ABCD$ 中，$\angle A=\angle B=\angle C=75^\circ$，$BC=2$，"
        r"则 $AB$ 的取值范围是（　　）"
    ),
    'opts': [
        ('A', r"$\left(\sqrt6-\sqrt2,\ \sqrt6+\sqrt2\right)$"),
        ('B', r"$\left[\sqrt6-\sqrt2,\ \sqrt6+\sqrt2\right]$"),
        ('C', r"$\left(\dfrac{\sqrt6-\sqrt2}2,\ \dfrac{\sqrt6+\sqrt2}2\right)$"),
        ('D', r"$\left[\dfrac{\sqrt6-\sqrt2}2,\ \dfrac{\sqrt6+\sqrt2}2\right]$"),
    ],
    'answer': 'A',
    'analysis': (
        r"四边形内角和 $360^\circ$ ⟹ $\angle D=360^\circ-3\times75^\circ=135^\circ$。"
        r"延长 $BA,CD$ 交于 $E$，平移 $AD$ —— **用两个极限位置定范围**："
        r"$A,D$ 与 $E$ 重合时 $AB$ 最长，$D$ 与 $C$ 重合时 $AB$ 最短。"
        r"⚠ 两个端点都**取不到**（否则退化成三角形），故为开区间。"
    ),
    'solution': (
        r"**第一步：求 $\angle D$**" "\n"
        r"四边形内角和 $360^\circ$，故 $\angle D=360^\circ-75^\circ\times3=135^\circ$．" "\n"
        r"**第二步：补成三角形**" "\n"
        r"延长 $BA$、$CD$ 交于点 $E$。在 $\triangle BCE$ 中：" "\n"
        r"$\angle EBC=180^\circ-\angle ABC=105^\circ$？——不对，注意 $E$ 在 $BA$ 的延长线上，" "\n"
        r"故 $\angle EBC=\angle ABC=75^\circ$；同理 $\angle BCE=\angle BCD=75^\circ$。" "\n"
        r"于是 $\angle E=180^\circ-75^\circ-75^\circ=30^\circ$．" "\n"
        r"**第三步：最长（$A,D$ 与 $E$ 重合）**" "\n"
        r"此时 $\triangle BEC$ 正弦定理：$\dfrac{BE}{\sin\angle BCE}=\dfrac{BC}{\sin E}$，" "\n"
        r"即 $\dfrac{BE}{\sin75^\circ}=\dfrac2{\sin30^\circ}\Rightarrow BE=2\cdot\dfrac{\sin75^\circ}{\sin30^\circ}$．" "\n"
        r"$\sin75^\circ=\dfrac{\sqrt6+\sqrt2}4$，故 $BE=2\cdot\dfrac{\sqrt6+\sqrt2}4\cdot2=\sqrt6+\sqrt2$．" "\n"
        r"因是极限位置，$AB<\sqrt6+\sqrt2$．" "\n"
        r"**第四步：最短（$D$ 与 $C$ 重合）**" "\n"
        r"$\dfrac{BF}{\sin30^\circ}=\dfrac{BC}{\sin75^\circ}=\dfrac2{\sin75^\circ}$" "\n"
        r"$\Rightarrow BF=\dfrac{2\sin30^\circ}{\sin75^\circ}=\dfrac{2\cdot\frac12}{\frac{\sqrt6+\sqrt2}4}$"
        r"$=\dfrac4{\sqrt6+\sqrt2}=\sqrt6-\sqrt2$．" "\n"
        r"（分母有理化：$\frac4{\sqrt6+\sqrt2}=\frac{4(\sqrt6-\sqrt2)}{6-2}=\sqrt6-\sqrt2$）" "\n"
        r"同理取不到等号：$AB>\sqrt6-\sqrt2$．" "\n"
        r"综上 $AB\in\left(\sqrt6-\sqrt2,\ \sqrt6+\sqrt2\right)$．选 A．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓，由详解「延长 $BA$、$CD$ 交于点 $E$，平移 $AD$…" "\n"
        r"① 当 $A$、$D$ 点与 $E$ 点重合时，$AB$ 最长，∴ $\frac{BE}{\sin30^\circ}=\frac2{\sin75^\circ}$，" "\n"
        r"$BE=\sqrt6+\sqrt2$，则 $AB<\sqrt6+\sqrt2$；② 当 $D$ 点与 $C$ 点重合时，$AB$ 最短，" "\n"
        r"∴ $\frac{BF}{\sin30^\circ}=\frac2{\sin75^\circ}$，$BF=\sqrt6-\sqrt2$…即 $AB\in(\sqrt6-\sqrt2,\sqrt6+\sqrt2)$」" "\n"
        r"还原，与我的推导一致 ✓。" "\n"
        r"**独立验算**：" "\n"
        r"① **$\angle D$**：$360-75\times3=360-225=135^\circ$ ✓" "\n"
        r"② **$\angle E$**：$180-75-75=30^\circ$ ✓" "\n"
        r"③ **数值**：$\sqrt6-\sqrt2=2.449-1.414=1.035$；$\sqrt6+\sqrt2=2.449+1.414=3.864$ ✓" "\n"
        r"④ **验 $BE$**：$\frac{BE}{\sin75^\circ}=\frac2{\sin30^\circ}=\frac2{0.5}=4$ ⟹ $BE=4\sin75^\circ=4(0.9659)=3.864$ ✓✓" "\n"
        r"⑤ **验 $BF$**：$\frac{BF}{\sin30^\circ}=\frac{BC}{\sin75^\circ}$ ⟹ $BF=\frac{2(0.5)}{0.9659}=1.0353$ ✓✓" "\n"
        r"（注意这两个式子**分子分母互换**了，别弄混：$BE$ 对 $\sin75^\circ$、$BF$ 对 $\sin30^\circ$。）" "\n"
        r"⑥ **有理化验证**：$\frac4{\sqrt6+\sqrt2}=\frac{4(2.449-1.414)}{4}=2.449-1.414=1.035$ ✓✓" "\n"
        r"⑦ **取 $AB=2$（区间内）检验可行性**：$\angle E=30^\circ$、$BC=2$、$BE$ 应满足" "\n"
        r"$\frac{BE}{\sin75^\circ}=\frac{BC}{\sin30^\circ}$…实际 $AB<BE$ 即 $2<3.864$ ✓ 在范围内。" "\n"
        r"**答案 A（开区间 $(\sqrt6-\sqrt2,\sqrt6+\sqrt2)$）正确** ✓" "\n"
        r"**⭐ 通法（四边形边长的范围 = 极限位置法）**：" "\n"
        r"① 四边形边长范围题，**几乎都是让某个顶点与另一个顶点重合取到端点**；" "\n"
        r"② 补成三角形后，用正弦定理算出两个极端位置的边长；" "\n"
        r"③ ⚠ **端点是否取到**要看该位置是否退化 —— 本题两个端点都使四边形退化成三角形，" "\n"
        r"故**必为开区间**（选项 A/C 是开、B/D 是闭，这就是命题人的区分点）。"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-204'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-204-E1',
}

T204_V1 = {
    'type': '选择',
    'stem_text': (
        r"在平面四边形 $ABCD$ 中，连接对角线 $BD$，已知 $CD=9$，$BD=16$，$\angle BDC=90^\circ$，"
        r"$\sin A=\dfrac45$，则对角线 $AC$ 的最大值为（　　）"
    ),
    'opts': [
        ('A', r"$27$"),
        ('B', r"$16$"),
        ('C', r"$10$"),
        ('D', r"$25$"),
    ],
    'answer': 'A',
    'analysis': (
        r"$B,D,C$ 三点固定（直角），$A$ 满足 $\angle BAD$ 的对边 $BD$ 固定且 $\sin A$ 固定 ⟹ "
        r"**$A$ 的轨迹是一段圆弧**。建系后用「圆外一点到圆上点的最大距离 $=d+R$」。"
    ),
    'solution': (
        r"**第一步：建系**" "\n"
        r"以 $D$ 为原点，$DB$、$DC$ 分别为 $x$、$y$ 轴：" "\n"
        r"$D(0,0)$、$B(16,0)$、$C(0,9)$．" "\n"
        r"**第二步：求 $A$ 的轨迹圆**" "\n"
        r"在 $\triangle ABD$ 中，$BD=16$、$\sin A=\dfrac45$，由正弦定理：" "\n"
        r"$2R=\dfrac{BD}{\sin A}=\dfrac{16}{4/5}=20\Rightarrow R=10$．" "\n"
        r"故 $A$ 在以 $BD$ 为弦、半径 $10$ 的圆弧上（取第四象限那一段，保证是凸四边形）．" "\n"
        r"圆心 $E$ 在 $BD$ 的垂直平分线 $x=8$ 上，且 $\lvert ED\rvert=R=10$：" "\n"
        r"$ED=\sqrt{8^{2}+y_E^{2}}=10\Rightarrow y_E^{2}=100-64=36\Rightarrow y_E=-6$（取下方）．" "\n"
        r"即 $E(8,-6)$．" "\n"
        r"**第三步：求 $AC$ 最大值**" "\n"
        r"$A$ 在圆 $E$ 上，$C$ 是圆外一点，故" "\n"
        r"$AC_{\max}=\lvert CE\rvert+R$．" "\n"
        r"$\lvert CE\rvert=\sqrt{(8-0)^{2}+(-6-9)^{2}}=\sqrt{64+225}=\sqrt{289}=17$．" "\n"
        r"$AC_{\max}=17+10=27$．选 A．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓，由详解「以 $D$ 为坐标原点，$DB,DC$ 分别为 $x,y$ 轴建立直角坐标系，" "\n"
        r"求出 $A$ 点轨迹方程…则 $D(0,0),B(16,0),C(0,9)$，因为 $\sin A=\frac45$，$\lvert BD\rvert=16$，" "\n"
        r"所以由平面几何知识得 $A$ 点轨迹为圆弧…设圆心为 $E$，则由正弦定理可得圆半径为" "\n"
        r"$\frac12\times\frac{\lvert BD\rvert}{\sin A}=\frac12\times\frac{16}{4/5}=10$。∴ $E(8,-6)$，因此对角线 $AC$ 的" "\n"
        r"最大值为 $\lvert CE\rvert+10=\sqrt{8^{2}+(-6-9)^{2}}+10=27$」还原，**与我的推导完全一致** ✓。" "\n"
        r"**独立验算**：" "\n"
        r"① **半径**：$2R=\frac{BD}{\sin A}=\frac{16}{0.8}=20$ ⟹ $R=10$ ✓" "\n"
        r"② **圆心**：$x=8$（$BD$ 中垂线）；$ED=\sqrt{8^2+6^2}=\sqrt{64+36}=10=R$ ✓✓" "\n"
        r"③ **$\lvert CE\rvert$**：$\sqrt{8^2+(-15)^2}=\sqrt{64+225}=\sqrt{289}=17$ ✓✓" "\n"
        r"④ **$AC_{\max}$**：$17+10=27$ ✓✓✓" "\n"
        r"⑤ **验证 $A$ 确实能在 $CE$ 延长线上取到**：圆心 $E(8,-6)$、$C(0,9)$，" "\n"
        r"$CE$ 方向单位向量 $=\frac{(8,-15)}{17}=(0.4706,-0.8824)$；" "\n"
        r"最远点 $A=E+10\cdot\frac{(8,-15)}{17}=(8+4.706,-6-8.824)=(12.706,-14.824)$" "\n"
        r"$A$ 在第四象限 ✓（符合「取第四象限部分圆弧」的要求）" "\n"
        r"验 $AD$：$AD=\sqrt{12.706^2+14.824^2}=\sqrt{161.4+219.8}=\sqrt{381.2}=19.52$" "\n"
        r"验 $\sin A$：在 $\triangle ABD$ 中 $\frac{BD}{\sin A}=2R$ ⟹ $\sin A=\frac{16}{20}=0.8=\frac45$ ✓✓✓" "\n"
        r"验 $AC$：$AC=\sqrt{(12.706-0)^2+(-14.824-9)^2}=\sqrt{161.4+567.3}=\sqrt{728.7}=26.99\approx27$ ✓✓✓" "\n"
        r"**答案 A（$27$）正确** ✓" "\n"
        r"**⭐ 通法（定弦定角 ⟹ 轨迹圆）**：" "\n"
        r"① **一条边固定 + 其对角固定** ⟹ 对顶点的轨迹是**圆弧**（同弦所对圆周角相等）；" "\n"
        r"② 半径由 $R=\frac{\text{弦长}}{2\sin(\text{圆周角})}$ 直接算，不必求轨迹方程；" "\n"
        r"③ 圆外一点 $P$ 到圆上点的距离范围 $[\,\lvert PE\rvert-R,\ \lvert PE\rvert+R\,]$ —— **共线时取到**；" "\n"
        r"④ ⚠ **注意象限/弧段**：题中说「平面四边形」，可能只取圆的一部分弧，" "\n"
        r"要检查最值点是否落在该弧段上（本题在第四象限 ✓）。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-204'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-204-V1',
}

T204_V2 = {
    'type': '选择',
    'stem_text': (
        r"在平面内，四边形 $ABCD$ 的 $\angle B$ 与 $\angle D$ 互补，$DC=1$，$BC=3$，"
        r"$\angle DAC=30^\circ$，则四边形 $ABCD$ 面积的最大值为（　　）"
    ),
    'opts': [
        ('A', r"$3$"),
        ('B', r"$\dfrac32+1$"),
        ('C', r"$\dfrac{2\sqrt2+1}2$"),
        ('D', r"$2$"),
    ],
    'answer': 'B',
    'analysis': (
        r"对角互补 ⟹ **$A,B,C,D$ 四点共圆** ⟹ $\angle CBD=\angle DAC=30^\circ$（同弧 $CD$）。"
        r"再由正弦定理得 $2R=\frac{DC}{\sin\angle DAC}=2$，即 $R=1$，且 $\sin\angle BAC=\frac{\sqrt3}2$ ⟹ "
        r"$\angle BAC=60^\circ$ 或 $120^\circ$，**必须分类讨论**。"
    ),
    'solution': (
        r"**第一步：识别四点共圆**" "\n"
        r"$\angle B+\angle D=180^\circ$ ⟹ $A,B,C,D$ 四点共圆．" "\n"
        r"于是 $\angle CBD=\angle DAC=30^\circ$（同弧 $CD$ 所对的圆周角）．" "\n"
        r"**第二步：求外接圆半径与 $\angle BAC$**" "\n"
        r"在 $\triangle ADC$ 中：$2R=\dfrac{DC}{\sin\angle DAC}=\dfrac1{\sin30^\circ}=2\Rightarrow R=1$．" "\n"
        r"在 $\triangle ABC$ 中由正弦定理 $\dfrac{AC}{\sin\angle B}=\dfrac{BC}{\sin\angle BAC}$，" "\n"
        r"在 $\triangle ADC$ 中 $\dfrac{AC}{\sin\angle D}=\dfrac{DC}{\sin\angle DAC}$，" "\n"
        r"又 $\sin\angle B=\sin\angle D$（互补），两式相除：" "\n"
        r"$\dfrac{BC}{\sin\angle BAC}=\dfrac{DC}{\sin\angle DAC}$ ⟹ $\sin\angle BAC=\dfrac{\sqrt3}2$" "\n"
        r"由 $\angle B+\angle D=180^\circ$ 得 $\sin B=\sin D$，两式相比即得。" "\n"
        r"（$\angle BAC=60^\circ$ 或 $120^\circ$）．" "\n"
        r"**第三步：分类讨论**" "\n"
        r"**情形一 $\angle BAC=60^\circ$**：则 $\angle BAD=90^\circ$，$\angle BCD=90^\circ$．" "\n"
        r"$S_{\triangle BCD}=\dfrac12\cdot1\cdot3\cdot\sin90^\circ=\dfrac32$，且 $BD=2R=2$．" "\n"
        r"在 $\mathrm{Rt}\triangle ABD$ 中：$4=a^{2}+b^{2}\ge2ab\Rightarrow ab\le2$（$a=AB,b=AD$），" "\n"
        r"$S_{\triangle ABD}=\dfrac12 ab\le1$．故 $S\le\dfrac32+1$，取等时 $a=b=\sqrt2$．" "\n"
        r"**情形二 $\angle BAC=120^\circ$**：则 $\angle BAD=150^\circ$，$\angle BCD=30^\circ$．" "\n"
        r"$S_{\triangle BCD}=\dfrac12\cdot1\cdot3\cdot\sin30^\circ=\dfrac34$，且 $BD=2R\sin30^\circ=1$．" "\n"
        r"在 $\triangle ABD$ 中：$1=a^{2}+b^{2}-2ab\cos150^\circ$ ⟹ $3ab=1-(a^{2}+b^{2})<1$ ⟹ $ab<\dfrac13$．" "\n"
        r"$S_{\triangle ABD}=\dfrac12 ab\sin150^\circ=\dfrac14 ab<\dfrac1{12}$．" "\n"
        r"$S<\dfrac34+\dfrac1{12}=\dfrac56<\dfrac32+1$．" "\n"
        r"**综上**：最大值为 $\dfrac32+1$（情形一）．选 B．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓，由详解「根据正弦定理，可求得 $\sin\angle BAC=\frac{\sqrt3}2$，" "\n"
        r"即 $\angle BAC=60^\circ$ 或 $\angle BAC=120^\circ$，所以分类讨论…" "\n"
        r"(1) 当 $\angle BAC=60^\circ$，则 $\angle BAD=90^\circ$，故 $\angle BCD=90^\circ$，此时 $S_{\triangle BCD}=\frac12\times1\times3\times\sin90^\circ=\frac32$，" "\n"
        r"且 $BD=2$，在 $\mathrm{Rt}\triangle ABD$ 中 $4=a^2+b^2\ge2ab$，所以 $ab\le2$，即 $S_{\triangle ABD}=\frac12 ab\le1$。" "\n"
        r"所以四边形 $ABCD$ 面积 $S=S_{\triangle BCD}+S_{\triangle ABD}\le\frac32+1$…" "\n"
        r"(2) 当 $\angle BAC=120^\circ$…$S_{\triangle ABD}<\frac1{12}$，此时 $S<\frac34+\frac1{12}=\frac56<\frac32+1$。" "\n"
        r"综上，四边形 $ABCD$ 面积的最大值等于 $\frac32+1$，故选 B」还原。" "\n"
        r"**独立验算**：" "\n"
        r"① **四点共圆**：$\angle B+\angle D=180^\circ$ ✓（圆内接四边形判定）" "\n"
        r"② **$\angle CBD=\angle DAC=30^\circ$**：同弧 $CD$ ✓" "\n"
        r"③ **$2R=\frac{DC}{\sin\angle DAC}=\frac1{0.5}=2$** ⟹ $R=1$ ✓" "\n"
        r"④ **情形一取等时**：$a=b=\sqrt2$，则 $a^2+b^2=4=BD^2$ ✓（$\angle BAD=90^\circ$ 勾股）" "\n"
        r"$S_{\triangle ABD}=\frac12(\sqrt2)(\sqrt2)=1$ ✓；$S_{\triangle BCD}=\frac12(1)(3)(1)=\frac32$ ✓" "\n"
        r"总计 $=\frac32+1=2.5$ ✓✓" "\n"
        r"⑤ **验情形一的几何存在性**：$BD=2=2R$ 即 $BD$ 是直径 ⟹ $\angle BAD=\angle BCD=90^\circ$ ✓ 自洽" "\n"
        r"⑥ **验情形二**：$BD=2R\sin\angle BAD=2\sin150^\circ=2(0.5)=1$ ✓" "\n"
        r"$S_{\triangle BCD}=\frac12(1)(3)\sin30^\circ=0.75$ ✓；$ab<\frac13$ ⟹ $S_{\triangle ABD}<\frac1{12}$ ✓" "\n"
        r"总计 $<0.75+0.0833=0.833<2.5$ ✓✓ **情形二确实更小**" "\n"
        r"⑦ **排除其他选项**：A $3>2.5$（不可能）、D $2<2.5$（说明最大值更大）" "\n"
        r"**答案 B（$\frac32+1$）正确** ✓" "\n"
        r"**⭐ 通法（对角互补 ⟹ 四点共圆）**：" "\n"
        r"① 看到「$\angle B$ 与 $\angle D$ 互补」**立刻想到四点共圆**，然后所有同弧圆周角都相等；" "\n"
        r"② 由 $2R=\frac{\text{边}}{\sin(\text{对角})}$ 求半径，再用 $BD=2R\sin\angle BAD$ 关联两个三角形；" "\n"
        r"③ ⚠ **$\sin\angle BAC=\frac{\sqrt3}2$ 有两解**（$60^\circ$ 和 $120^\circ$），**必须分类** —— " "\n"
        r"本题两种情形结果差很多（$2.5$ vs $<0.83$），漏掉情形二虽然不影响最终答案，" "\n"
        r"但漏掉情形一就会选错。" "\n"
        r"④ 面积最值：分割成两个三角形后各自用**均值不等式**（$a^2+b^2\ge2ab$）。"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-204'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-204-V2',
}

T204_V3 = {
    'type': '选择',
    'stem_text': (
        r"凸四边形就是没有角度数大于 $180^\circ$ 的四边形，把四边形任何一边向两方延长，"
        r"其他各边都在延长所得直线的同一旁，这样的四边形叫做凸四边形．"
        r"如图，在凸四边形 $ABCD$ 中，$AB=1$，$BC=\sqrt3$，$AC\perp CD$，$AC=CD$，"
        r"当 $\angle ABC$ 变化时，对角线 $BD$ 的最大值为（　　）"
    ),
    'opts': [
        ('A', r"$3$"),
        ('B', r"$4$"),
        ('C', r"$\sqrt6+1$"),
        ('D', r"$\sqrt7+2\sqrt3$"),
    ],
    'answer': 'C',
    'analysis': (
        r"设 $\angle ABC=\alpha$、$\angle ACB=\beta$。先在 $\triangle ABC$ 中用余弦定理表出 $AC^2$、"
        r"用正弦定理表出 $\sin\beta$；再在 $\triangle BCD$ 中用余弦定理（$AC\perp CD$ 给出夹角 $\beta+90^\circ$）；"
        r"最后化成 $A\sin(\alpha-\frac\pi4)+B$ 用**有界性**取最大。"
    ),
    'solution': (
        r"**第一步：$\triangle ABC$ 中表出 $AC^{2}$ 与 $\sin\beta$**" "\n"
        r"由余弦定理：$AC^{2}=BA^{2}+BC^{2}-2\,BA\cdot BC\cos\alpha$"
        r"$=1+3-2\cdot1\cdot\sqrt3\cos\alpha=4-2\sqrt3\cos\alpha$．" "\n"
        r"由正弦定理 $\dfrac{AB}{\sin\beta}=\dfrac{AC}{\sin\alpha}$：" "\n"
        r"$\sin\beta=\dfrac{AB\sin\alpha}{AC}=\dfrac{\sin\alpha}{AC}$，即 $AC\sin\beta=\sin\alpha$．" "\n"
        r"**第二步：$\triangle BCD$ 中用余弦定理**" "\n"
        r"因 $AC\perp CD$ 且 $AC=CD$，有 $\angle BCD=\beta+90^\circ$、$CD=AC$．" "\n"
        r"$BD^{2}=CB^{2}+CD^{2}-2\,CB\cdot CD\cos(\beta+90^\circ)$" "\n"
        r"$=3+AC^{2}-2\sqrt3\,AC\cdot(-\sin\beta)$"
        r"$=3+AC^{2}+2\sqrt3\,AC\sin\beta$．" "\n"
        r"代入 $AC^{2}=4-2\sqrt3\cos\alpha$ 与 $AC\sin\beta=\sin\alpha$：" "\n"
        r"$BD^{2}=3+(4-2\sqrt3\cos\alpha)+2\sqrt3\sin\alpha=7+2\sqrt3(\sin\alpha-\cos\alpha)$" "\n"
        r"$=7+2\sqrt3\cdot\sqrt2\sin\left(\alpha-\dfrac\pi4\right)$"
        r"$=7+2\sqrt6\sin\left(\alpha-\dfrac\pi4\right)$．" "\n"
        r"**第三步：有界性取最大**" "\n"
        r"当 $\sin\left(\alpha-\frac\pi4\right)=1$，即 $\alpha=\dfrac{3\pi}4=135^\circ$ 时：" "\n"
        r"$BD^{2}_{\max}=7+2\sqrt6$．" "\n"
        r"注意 $(\sqrt6+1)^{2}=6+2\sqrt6+1=7+2\sqrt6$，故" "\n"
        r"$BD_{\max}=\sqrt{7+2\sqrt6}=\sqrt6+1$．选 C．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓，由详解「设 $\angle ABC=\alpha$，$\angle ACB=\beta$，利用余弦定理与正弦定理，" "\n"
        r"表示出 $AC^{2}=4-2\sqrt3\cos\alpha$ 与 $\sin\beta=\frac{\sin\alpha}{4-2\sqrt3\cos\alpha}$…" "\n"
        r"在 $\triangle BCD$ 中，由余弦定理求得 $BD$ 的表达式，根据三角函数值的有界性即可求得最大值…" "\n"
        r"代入化简可得 $BD^{2}=7+2\sqrt6\sin(\alpha-\frac\pi4)$，所以当 $\alpha=\frac{3\pi}4$ 时，" "\n"
        r"$BD^{2}$ 取得最大值 $BD^{2}=7+2\sqrt6$，此时 $BD$ 取得最大值为 $BD=\sqrt6+1$，所以选 C」还原，" "\n"
        r"**我的推导与原书逐字一致** ✓。" "\n"
        r"**⚠⚠ 题干还原（根号丢失 —— 本批最关键的发现）**：" "\n"
        r"ref_bank 存 `BC = 3`，但若按 $BC=3$，则 $AC^{2}=10-6\cos\alpha$（不是原书的 $4-2\sqrt3\cos\alpha$），" "\n"
        r"最终也推不出 $7+2\sqrt6$。**按原书中间结果反推，题干必为 $BC=\sqrt3$**（根号在提取时丢失）。" "\n"
        r"**验证链条**：" "\n"
        r"① $AB=1$、$BC=\sqrt3$ ⟹ $AC^{2}=1+3-2\sqrt3\cos\alpha=4-2\sqrt3\cos\alpha$ ✓✓ **与原书完全一致**" "\n"
        r"② $\sin\beta=\frac{\sin\alpha}{AC}=\frac{\sin\alpha}{\sqrt{4-2\sqrt3\cos\alpha}}$ ✓✓ **与原书完全一致**" "\n"
        r"③ $BD^{2}=7+2\sqrt6\sin(\alpha-\frac\pi4)$ ✓✓ **与原书完全一致**" "\n"
        r"三步中间结果全部吻合 —— 这比任何猜测都可靠。" "\n"
        r"**数值验算**（逐点核对 $AC^{2}$ 与 $BD^{2}$ 两个公式）：" "\n"
        r"· $\alpha=90^\circ$：$AC^{2}=4-0=4$；$BD^{2}=3+4+2\sqrt3(1)=7+3.464=10.464$" "\n"
        r"公式 $7+2\sqrt6\sin45^\circ=7+4.899(0.7071)=7+3.464=10.464$ ✓✓" "\n"
        r"· $\alpha=120^\circ$：$AC^{2}=4-2\sqrt3(-0.5)=4+1.732=5.732$；$BD^{2}=3+5.732+2\sqrt3(0.866)=3+5.732+3=11.732$" "\n"
        r"公式 $7+4.899\sin75^\circ=7+4.899(0.9659)=7+4.732=11.732$ ✓✓" "\n"
        r"· $\alpha=135^\circ$：**取最大**，$BD^{2}=7+2\sqrt6=11.899$，$BD=3.4495$" "\n"
        r"· $\alpha=150^\circ$：$BD^{2}=11.732$（回落）✓ 确为最大值" "\n"
        r"④ **$BD_{\max}$**：$\sqrt{11.899}=3.4495$；$\sqrt6+1=2.4495+1=3.4495$ ✓✓✓" "\n"
        r"$(\sqrt6+1)^{2}=7+2\sqrt6$ ✓✓" "\n"
        r"⑤ **排除其他选项**：A $3$（$<3.4495$，不是最大）、B $4$（$>3.4495$，取不到）、" "\n"
        r"D $\sqrt7+2\sqrt3=2.646+3.464=6.110$（远超）✗" "\n"
        r"**答案 C（$\sqrt6+1$）正确** ✓" "\n"
        r"**⭐ 通法（一个角变化的四边形最值）**：" "\n"
        r"① 设变化角为 $\alpha$，**所有量都用它表示**；" "\n"
        r"② 分两步：先在已知三角形中表出公共边 $AC$ 和中间角 $\beta$，再在第二个三角形中用余弦定理；" "\n"
        r"③ ⚠ **$AC\perp CD$ 这类条件要转成夹角 $\beta+90^\circ$**，" "\n"
        r"$\cos(\beta+90^\circ)=-\sin\beta$ —— **负号极易漏**，漏了 $BD^2$ 会变成减号，最值完全不同；" "\n"
        r"④ 化成 $A\sin(\alpha+\varphi)+B$ 后用**有界性**取最大，比分情况讨论快得多。" "\n"
        r"**⚠ 本题的通用提醒**：当自己推导的中间结果与原书对不上时，" "\n"
        r"**优先怀疑题干有根号丢失**（本项目已出现 N 次），而不是硬凑原书答案。"
    ),
    'difficulty': 0.95,
    'topics': ['M-T-204'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-204-V3',
}

QS = [T204_E1, T204_V1, T204_V2, T204_V3]
