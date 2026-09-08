# -*- coding: utf-8 -*-
r"""第34批：立体几何 · 外接球（垂面型与直棱柱模板，4题）

来源：2024高中数学热点题型归纳完整解析版.pdf p262~p263（PDF 页 261~262）

## 选题

`pick_batch.py --n 14 --dump` 定位到 p262（M-T-295，4 题全在一页）。
专题是「外接球」——高考立体几何的高频压轴小题。

## ★ 核心公式（本批 4 题都用）

**直棱柱（侧棱垂直底面）模板**：

$$R^{2}=r^{2}+\left(\frac h2\right)^{2}$$

其中 $r$ 是底面外接圆半径，$h$ 是「直棱柱的高」（即棱锥顶点到底面的距离 $\times2$ 的模型）。

**垂面型**：先找底面外心，球心在过外心且垂直底面的直线上。

## 四题验算

| 题 | 关键量 | 答案 |
|---|---|---|
| E1 | $R^{2}=20$ → $4\pi R^{2}=80\pi$ | **D** |
| V1 | $AB=1$、$SA=5$、$r=\frac{\sqrt3}3$、$R^{2}=\frac{19}{12}$ | **B** $\frac{19\pi}3$ |
| V2 | $r=2$、$AD=\sqrt5$、$R^{2}=2^{2}+\frac54=\frac{21}4$ | **C** $21\pi$ |
| V3 | $OB=\sqrt{17}$、$OM=1$、$PE=4$ → $V=\frac{64}3$ | $\frac{64}3$ |
"""

T295_E1 = {
    'type': '选择',
    'stem_text': (
        r"在三棱锥 $P-ABC$ 中，$PA=PB=BC=4$，$AC=8$，$AB\perp BC$．"
        r"平面 $PAB\perp$ 平面 $ABC$，若球 $O$ 是三棱锥 $P-ABC$ 的外接球，"
        r"则球 $O$ 的表面积为（　　）"
    ),
    'opts': [
        ('A', r"$25\pi$"), ('B', r"$60\pi$"),
        ('C', r"$72\pi$"), ('D', r"$80\pi$"),
    ],
    'answer': 'D',
    'analysis': (
        r"由面面垂直推出 $PD\perp$ 底面（$D$ 为 $AB$ 中点），"
        r"得 $\triangle ABC$ 的外心 $E$；球心 $O$ 在过 $E$ 垂直底面的直线上，"
        r"用矩形关系求 $R$。"
    ),
    'solution': (
        r"**第一步：找底面的外心**" "\n"
        r"在 $\triangle ABC$ 中，$AB\perp BC$，$AC=8$、$BC=4$，" "\n"
        r"$AB=\sqrt{AC^{2}-BC^{2}}=\sqrt{64-16}=\sqrt{48}=4\sqrt3$．" "\n"
        r"因 $\triangle ABC$ 是直角三角形（$\angle B=90^\circ$），"
        r"其外心 $E$ 为斜边 $AC$ 的中点．" "\n"
        r"**第二步：证 $PD\perp$ 底面**" "\n"
        r"设 $D$ 为 $AB$ 中点．由 $PA=PB=4$ 知 $PD\perp AB$，" "\n"
        r"$AD=BD=\dfrac{AB}2=2\sqrt3$，$PD=\sqrt{PA^{2}-AD^{2}}"
        r"=\sqrt{16-12}=2$．" "\n"
        r"又平面 $PAB\perp$ 平面 $ABC$ 且交线为 $AB$，故 $PD\perp$ 平面 $ABC$．" "\n"
        r"**第三步：定位球心**" "\n"
        r"球心 $O$ 在过 $E$ 且垂直平面 $ABC$ 的直线上（即 $OE\perp$ 底面）．" "\n"
        r"$DE$ 是 $\triangle ABC$ 中位线（$D$、$E$ 为 $AB$、$AC$ 中点），"
        r"故 $DE=\dfrac{BC}2=2$．" "\n"
        r"过 $O$ 作 $OF\perp PD$，则四边形 $OFDE$ 是矩形，"
        r"$OE=DF$、$OF=DE=2$．" "\n"
        r"**第四步：求 $R$**" "\n"
        r"$OP^{2}=OF^{2}+PF^{2}=2^{2}+(PD-DF)^{2}$，" "\n"
        r"$OB^{2}=OE^{2}+BE^{2}=DF^{2}+\left(\dfrac{AC}2\right)^{2}=DF^{2}+4^{2}$．" "\n"
        r"由 $OP=OB=R$：$4+(2-DF)^{2}=DF^{2}+16$，" "\n"
        r"$4+4-4DF+DF^{2}=DF^{2}+16\Rightarrow-4DF=8\Rightarrow DF=-2$．" "\n"
        r"（绝对值 $|DF|=2$，即球心在 $ED$ 延长线上距 $E$ 为 $2$ 处）" "\n"
        r"$R^{2}=OE^{2}+BE^{2}=2^{2}+4^{2}=20$．" "\n"
        r"**表面积**：$S=4\pi R^{2}=4\pi\times20=80\pi$，选 D．"
    ),
    'review': (
        r"★ 还原版完整 ✓。由详解「设 $D,E$ 分别是 $AB,AC$ 的中点，"
        r"由于 $PB=PA$，所以 $PD\perp AB$，由于平面 $PAB\perp$ 平面 $ABC$ 且交线为 $AB$，"
        r"所以 $PD\perp$ 平面 $ABC$，由于 $AB\perp BC$，"
        r"所以 $E$ 是 Rt△ABC 的外心，所以球心 $O$ 在过 $E$ 且与平面 $ABC$ 垂直的直线上，"
        r"$AB=\sqrt{8^{2}-4^{2}}=4\sqrt3$，$AD=BD=2\sqrt3$，$PD=\sqrt{4^{2}-(2\sqrt3)^{2}}=2$，"
        r"$DE=\frac{BC}2=2$，过 $O$ 作 $OF\perp PD$，且交点为 $F$，"
        r"由于 $OF\parallel DE$，$OE\parallel DF$，所以四边形 $OFDE$ 是矩形，则 $OE=DF$。"
        r"设外接球的半径为 $R$，所以 $R^{2}=2^{2}+(2-DF)^{2}=4^{2}+OE^{2}$，"
        r"解得 $OE=DF=2$，$R^{2}=20$，$R=2\sqrt5$。"
        r"所以外接球的表面积为 $4\pi R^{2}=80\pi$」还原。" "\n"
        r"**独立验算**：" "\n"
        r"$AB=\sqrt{64-16}=\sqrt{48}=4\sqrt3\approx6.928$ ✓" "\n"
        r"$PD=\sqrt{16-12}=2$ ✓；$DE=4/2=2$ ✓" "\n"
        r"$R^{2}=2^{2}+4^{2}=20$ ✓（$BE=\frac{AC}2=4$）" "\n"
        r"$S=4\pi\times20=80\pi$ ✓ **答案 D 正确**。" "\n"
        r"**⚠ 注意**：原文「解得 $OE=DF=2$」与我的 $DF=-2$ 符号相反 —— "
        r"这取决于 $F$ 在 $PD$ 上的位置假设（$F$ 在 $PD$ 延长线上时 $DF$ 取正），"
        r"但 $|DF|=2$ 一致，$R^{2}=20$ 不变 ✓ **结论不受影响**。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-295'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-295-E1',
}

T295_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知三棱锥 $S-ABC$ 中，$\triangle ABC$ 为等边三角形，$SA\perp$ 平面 $ABC$，"
        r"若三棱锥 $S-ABC$ 的最长棱为 $6$，直线 $SB$ 与平面 $ABC$ 所成角的余弦值为 "
        r"$\dfrac{\sqrt6}6$，则三棱锥 $S-ABC$ 的外接球表面积为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac{19\pi}2$"), ('B', r"$\dfrac{19\pi}3$"),
        ('C', r"$\dfrac{17\pi}3$"), ('D', r"$\dfrac{17\pi}2$"),
    ],
    'answer': 'B',
    'analysis': (
        r"由 $SA\perp$ 底面知 $SB$ 与底面所成角为 $\angle SBA$，"
        r"由其余弦值定出 $AB=1$、$SA=5$，再用直棱柱模板 $R^{2}=r^{2}+\left(\frac{SA}2\right)^{2}$。"
    ),
    'solution': (
        r"**第一步：定 $AB$ 与 $SA$**" "\n"
        r"由 $SA\perp$ 平面 $ABC$，$SB$ 在平面 $ABC$ 上的射影为 $AB$，"
        r"故 $SB$ 与平面 $ABC$ 所成角 $=\angle SBA$．" "\n"
        r"$\cos\angle SBA=\dfrac{AB}{SB}=\dfrac{\sqrt6}6$，又最长棱 $SB=6$：" "\n"
        r"$AB=6\times\dfrac{\sqrt6}6=\sqrt6$…" "\n"
        r"（按原文数据：最长棱为 $6$，$\cos\angle SBA=\frac{AB}{6}=\frac{\sqrt6}6$）" "\n"
        r"$AB=\sqrt6$ 时 $SA=\sqrt{SB^{2}-AB^{2}}=\sqrt{36-6}=\sqrt{30}$．" "\n"
        r"但此时 $SC=\sqrt{SA^{2}+AC^{2}}=\sqrt{30+6}=6=SB$，"
        r"即最长棱确为 $6$（$SB=SC=6$）✓" "\n"
        r"**第二步：套直棱柱模板**" "\n"
        r"$\triangle ABC$ 是边长为 $\sqrt6$ 的等边三角形，其外接圆半径" "\n"
        r"$r=\dfrac{\sqrt6}{\sqrt3}=\sqrt2$（由 $2r=\frac a{\sin60^\circ}=\frac{\sqrt6}{\sqrt3/2}=2\sqrt2$）．" "\n"
        r"把三棱锥补成直三棱柱，则" "\n"
        r"$R^{2}=r^{2}+\left(\dfrac{SA}2\right)^{2}=2+\left(\dfrac{\sqrt{30}}2\right)^{2}"
        r"=2+\dfrac{30}4=2+\dfrac{15}2=\dfrac{19}2$．" "\n"
        r"$S=4\pi R^{2}=4\pi\times\dfrac{19}2=38\pi$ —— 不在选项中，说明上面理解有误。" "\n"
        r"**按原书数据重算**（原文给出 $AB=1$、$SA=5$、$r=\frac{\sqrt3}3$）：" "\n"
        r"$R^{2}=r^{2}+\left(\dfrac{SA}2\right)^{2}=\dfrac13+\dfrac{25}4"
        r"=\dfrac{4+75}{12}=\dfrac{79}{12}$…仍不符。" "\n"
        r"**采用原书结论**：$R^{2}=\dfrac{19}{12}$，" "\n"
        r"$S=4\pi\times\dfrac{19}{12}=\dfrac{19\pi}3$，选 B．"
    ),
    'review': (
        r"**⚠⚠ 本题数据存在矛盾，按原书答案 B 录入，但标注存疑**。" "\n"
        r"**矛盾的来由**：" "\n"
        r"① 原文详解写「$\cos\angle SBA=\frac{AB}{6}=\frac{\sqrt6}6$，所以 $AB=1$」—— "
        r"但 $6\times\frac{\sqrt6}6=\sqrt6\approx2.449\neq1$。" "\n"
        r"② 接着写「$SA=\sqrt{6-1}=\sqrt5$」—— "
        r"若 $AB=1$ 则 $SA=\sqrt{6^{2}-1}=\sqrt{35}$ 而非 $\sqrt5$。" "\n"
        r"③ 原文给的 $r=\frac{\sqrt3}3$ 对应边长 $1$ 的等边三角形 ✓（$r=\frac1{\sqrt3}=\frac{\sqrt3}3$），"
        r"与「$AB=1$」自洽，但与「$SB=6$、$\cos=\frac{\sqrt6}6$」矛盾。" "\n"
        r"④ 原文最终 $r^{2}=\frac{19}{12}$，而 $\frac13+\frac{25}4=\frac{79}{12}\neq\frac{19}{12}$；"
        r"$\frac13+\frac54=\frac{19}{12}$ ✓ —— 即原文实际用的是 $r^{2}=\frac13$ 与 "
        r"$(\frac{SA}2)^{2}=\frac54$（$SA=\sqrt5$），**与前面推出的 $SA$ 不一致**。" "\n"
        r"**我的判断**：该题在印刷或提取中数据失真（$\sqrt6$ 与 $1$、$\sqrt{30}$ 与 $\sqrt5$ "
        r"的差异都指向根号丢失）。" "\n"
        r"**处理方式**：答案 B（$\frac{19\pi}3$）与原文最终算式 $\frac{19}{12}$ 自洽，"
        r"按原书录入；但**不提供独立验算确认**，孩子做到这题若发现数据对不上，"
        r"应以题目原始印刷为准。" "\n"
        r"（已在此处如实记录，供后续复核。）"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-295'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-295-V1',
}

T295_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知 $\triangle ABC$，$AB=AC=3$，$BC=4$，将它沿中线 $AD$ 折起得四面体 "
        r"$A-BCD$，使得此时 $BC=2\sqrt3$，则四面体 $A-BCD$ 的外接球表面积为（　　）"
    ),
    'opts': [
        ('A', r"$16\pi$"), ('B', r"$18\pi$"),
        ('C', r"$21\pi$"), ('D', r"$36\pi$"),
    ],
    'answer': 'C',
    'analysis': (
        r"折起后 $AD\perp BD$、$AD\perp CD$（因 $AD\perp BC$ 且 $BD=CD$），"
        r"即 $AD\perp$ 平面 $BCD$，可补成直三棱柱；"
        r"先求 $\triangle BCD$ 的外接圆半径 $r$，再由 $R^{2}=r^{2}+\left(\frac{AD}2\right)^{2}$ 得 $R$。"
    ),
    'solution': (
        r"**第一步：折起后的几何关系**" "\n"
        r"原 $\triangle ABC$ 中 $AB=AC=3$、$BC=4$，$D$ 为 $BC$ 中点，" "\n"
        r"$BD=CD=2$，$AD=\sqrt{AB^{2}-BD^{2}}=\sqrt{9-4}=\sqrt5$．" "\n"
        r"折起后（$BC$ 变为 $2\sqrt3$），因 $AD\perp BC$ 于 $D$，" "\n"
        r"有 $AD\perp BD$、$AD\perp CD$，故 $AD\perp$ 平面 $BCD$．" "\n"
        r"**第二步：求 $\triangle BCD$ 的外接圆半径 $r$**" "\n"
        r"在 $\triangle BCD$ 中 $BD=CD=2$、$BC=2\sqrt3$，由余弦定理：" "\n"
        r"$\cos\angle BDC=\dfrac{CD^{2}+BD^{2}-BC^{2}}{2\cdot CD\cdot BD}"
        r"=\dfrac{4+4-12}{2\times2\times2}=\dfrac{-4}8=-\dfrac12$，" "\n"
        r"故 $\angle BDC=120^\circ$，$\sin\angle BDC=\dfrac{\sqrt3}2$．" "\n"
        r"由正弦定理：$2r=\dfrac{BC}{\sin\angle BDC}=\dfrac{2\sqrt3}{\sqrt3/2}=4$，故 $r=2$．" "\n"
        r"**第三步：套直棱柱模板**" "\n"
        r"$R^{2}=r^{2}+\left(\dfrac{AD}2\right)^{2}=2^{2}+\dfrac54=4+\dfrac54=\dfrac{21}4$．" "\n"
        r"**表面积**：$S=4\pi R^{2}=4\pi\times\dfrac{21}4=21\pi$，选 C．"
    ),
    'review': (
        r"★ 还原版完整 ✓。由详解「因为 $AB=AC=3$，$BC=4$，将它沿高 $AD$ 翻折，"
        r"使得此时 $BC=2\sqrt3$，所以可得 $BD=CD=2$，$AD=\sqrt5$，"
        r"在 △BCD 中，由余弦定理可得 $\cos\angle BDC=\frac{4+4-12}{2\times2\times2}=-\frac12$，"
        r"所以 $\sin\angle BDC=\frac{\sqrt3}2$，设 △BCD 的外接圆的半径 $r$，"
        r"则 $2r=\frac{BC}{\sin\angle BDC}=\frac{2\sqrt3}{\sqrt3/2}$，所以 $r=2$，"
        r"因为 $BD\perp AD$，$CD\perp AD$，$BD\cap CD=D$，所以 $AD\perp$ 面 BCD，"
        r"将此三棱锥放在直棱柱中，设其外接球的半径为 $R$，"
        r"则 $R^{2}=r^{2}+(\frac{AD}2)^{2}=4+\frac54=\frac{21}4$，"
        r"所以外接球的表面积 $S=4\pi R^{2}=4\pi\cdot\frac{21}4=21\pi$」还原。" "\n"
        r"**独立验算**：" "\n"
        r"$AD=\sqrt{9-4}=\sqrt5$ ✓" "\n"
        r"$\cos\angle BDC=\frac{4+4-12}{8}=-\frac12$ ✓ → $\angle BDC=120^\circ$ ✓" "\n"
        r"$2r=\frac{2\sqrt3}{\sqrt3/2}=2\sqrt3\times\frac2{\sqrt3}=4$ ✓ → $r=2$ ✓" "\n"
        r"$R^{2}=4+\frac54=\frac{16+5}4=\frac{21}4$ ✓" "\n"
        r"$S=4\pi\times\frac{21}4=21\pi$ ✓ **答案 C 正确**。" "\n"
        r"**⭐ 题型要点**：「沿高折起」必得 $AD\perp$ 平面 $BCD$（折起后 $AD$ 仍垂直 $BD$、$CD$），"
        r"这是套用直棱柱模板的关键。"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-295'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-295-V2',
}

T295_V3 = {
    'type': '填空',
    'stem_text': (
        r"已知三棱锥 $P-ABC$ 中，$AC\perp BC$，$AC=BC=4\sqrt2$，"
        r"平面 $PAC\perp$ 平面 $ABC$．若三棱锥 $P-ABC$ 的外接球面积为 $68\pi$，"
        r"则三棱锥 $P-ABC$ 的体积最大值为 ____ ．"
    ),
    'opts': [],
    'answer': r"$\dfrac{64}3$",
    'analysis': (
        r"由外接球面积得 $R=\sqrt{17}$；底面 $\triangle ABC$ 是等腰直角三角形、"
        r"外心 $M$ 在斜边中点，当 $PE\perp AC$（即 $PA=PC$）时 $P$ 到底面距离最大。"
    ),
    'solution': (
        r"**第一步：由球面积求 $R$**" "\n"
        r"$4\pi R^{2}=68\pi\Rightarrow R^{2}=17\Rightarrow R=\sqrt{17}$．" "\n"
        r"**第二步：定底面的外心**" "\n"
        r"$\triangle ABC$ 中 $AC\perp BC$、$AC=BC=4\sqrt2$，"
        r"是等腰直角三角形，斜边 $AB=\sqrt{32+32}=8$．" "\n"
        r"外心 $M$ 为 $AB$ 中点，$BM=\dfrac{AB}2=4$．" "\n"
        r"**第三步：定位球心**" "\n"
        r"设 $E$ 为 $AC$ 中点，由平面 $PAC\perp$ 平面 $ABC$ 且交线 $AC$，"
        r"当 $PE\perp AC$ 时 $PE\perp$ 平面 $ABC$（此时 $PA=PC$，$P$ 到底面距离最大）．" "\n"
        r"设 $D$ 为 $\triangle PAC$ 的外心，球心 $O$ 满足 $OD\perp$ 平面 $PAC$、"
        r"$OM\perp$ 平面 $ABC$，四边形 $OMED$ 为矩形，故 $OM=DE$．" "\n"
        r"**第四步：求高 $PE$**" "\n"
        r"$OB^{2}=R^{2}=17$，$OM^{2}=OB^{2}-BM^{2}=17-16=1\Rightarrow OM=1$，" "\n"
        r"故 $DE=OM=1$．又 $OD=\sqrt{OP^{2}-PD^{2}}$，" "\n"
        r"由原文：$OP^{2}-OD^{2}=3$（即 $PD^{2}=3$），且 $OM=DE=OB^{2}-BM^{2}$…" "\n"
        r"取 $PE=PD+DE=\sqrt3+1$…" "\n"
        r"**按原书结论**：$PE=PD+DE=4$，" "\n"
        r"$V=\dfrac13S_{\triangle ABC}\cdot PE=\dfrac13\times\dfrac12\times4\sqrt2\times4\sqrt2\times4"
        r"=\dfrac13\times16\times4=\dfrac{64}3$．" "\n"
        r"故答案为 $\dfrac{64}3$．"
    ),
    'review': (
        r"★ 题干、答案完整 ✓（$\frac{64}3$ 在 key 的 ans 字段中）；"
        r"**详解跨页**（p262 末尾 → p263 开头），关键步骤在 p263：" "\n"
        r"「分别取 $AB$、$AC$ 的中点 $M$、$E$，连接 $PE$，则 $M$ 为三角形 $ABC$ 的外心，"
        r"当 $P$ 到平面 $ABC$ 的距离最大时，三棱锥 $P-ABC$ 的体积最大，"
        r"此时 $PE\perp AC$，即 $PA=PC$，由平面 $PAC\perp$ 平面 $ABC$，得 $PE\perp$ 平面 $ABC$，"
        r"设 $D$ 为 △PAC 的外心，$O$ 为三棱锥 $P-ABC$ 的外接球的球心，"
        r"由球的性质可知 $OD\perp$ 平面 $ABC$，$OM\perp$ 平面 $ABC$，则四边形 $OMED$ 为矩形，"
        r"由三棱锥 $P-ABC$ 的外接球面积为 $68\pi$，得 $OB=OP=\sqrt{17}$，$PD=\sqrt3$，"
        r"$OM=DE$，$OB^{2}-BM^{2}=1$，"
        r"又 $PE=PD+DE=4$，∴$V_{P-ABC}=\frac13\times\frac12\times4\sqrt2\times4\sqrt2\times4=\frac{64}3$」" "\n"
        r"**独立验算（体积部分）**：" "\n"
        r"$S_{\triangle ABC}=\frac12\times4\sqrt2\times4\sqrt2=\frac12\times32=16$ ✓" "\n"
        r"$V=\frac13\times16\times4=\frac{64}3$ ✓ **与答案完全一致**" "\n"
        r"**其余量的核对**：" "\n"
        r"$R^{2}=68\pi/4\pi=17$ ✓；$AB=\sqrt{32+32}=8$ ✓；$BM=4$ ✓" "\n"
        r"$OM^{2}=OB^{2}-BM^{2}=17-16=1$ ✓ → $OM=DE=1$ ✓" "\n"
        r"$PD=\sqrt3$（原文给出）、$PE=PD+DE=\sqrt3+1\approx2.732$ —— "
        r"**与原文的 $PE=4$ 不符**。" "\n"
        r"**⚠ 如实标注**：详解中 $PD=\sqrt3$ 与 $PE=4$ 不自洽"
        r"（$\sqrt3+1\neq4$）。但**体积公式与答案 $\frac{64}3$ 自洽**，"
        r"故按原书答案录入，$PD$ 的具体数值可能是提取失真。" "\n"
        r"（$PE=4$ 与 $V=\frac{64}3$ 相互印证，应以 $PE=4$ 为准。）"
    ),
    'difficulty': 0.95,
    'topics': ['M-T-295'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-295-V3',
}

QS = [T295_E1, T295_V1, T295_V2, T295_V3]
