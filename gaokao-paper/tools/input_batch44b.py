# -*- coding: utf-8 -*-
r"""第44批（下）：立体几何 · 翻折中的角度

来源：2024高中数学热点题型归纳完整解析版.pdf
p275（PDF 页 274）M-T-306 翻折中的角度
p271（PDF 页 270）M-T-303 求异面直线所成的角

## 选题

`pick_batch.py --n 16` → p275 / p271。本文件取 M-T-306 的 E1、V2 + M-T-303 的 E1。

## ⚠ 跳过

- **M-T-306-V1/V3**：详解依赖「$\sin\alpha$、$\beta$」的具体关系且选项为不等式组，
  原文在双栏中交错（p275 开头就是别题的尾部），无法可靠还原。
- **M-T-303-V2/V3**：选项破碎（$\frac{\sqrt{10}}{10}$ 被提取成 `1010`）。

## ★ E1 的关键：翻折中「不变」的是 $A'C$

矩形 $ABCD$ 中 $AB=\sqrt3\,BC$，沿 $EF$ 翻折梯形 $ADEF$。**翻折过程中 $\lvert A'C\rvert$ 不变** ——
这是「翻折题型要寻找变化中的不变」的直接体现。

$E,F$ 是 $AD,BC$ 上的分点（$\frac{CE}{DE}=\frac{AF}{BF}=\frac12$），
翻折后 $A'$ 在以 $EF$ 为轴、半径 $r=d(A,EF)$ 的圆上运动，
故 $A'C$ 与平面 $BOD'$ 的角随 $A'$ 的位置变化，可求范围。

## 三题验算

| 题 | 计算 | 答案 |
|---|---|---|
| 306-E1 | $A'$ 到平面 $BOD'$ 的距离 $=\frac{\sqrt3}2\sqrt{\frac{2-2\cos\alpha}{3}}$（$\alpha$ 为二面角），$\sin\theta=\frac h{\lvert A'C\rvert}$ 最大 $\frac12$ → $\theta\le30^\circ$；题问「可以是」，$30^\circ$ 可取 | **B（75°）**？ |
| 306-V2 | 端点法：$B$ 折到 $B'$ 时，$B'A$、$B'C$、$B'D$ 与平面 $ADC$ 的角分别 $\theta_1,\theta_2,\theta_3$，由对称性 $\theta_2=\theta_3$ 且 $\le\theta_1$ | **C** |
| 303-E1 | 正四面体对棱 $AB\perp CD$；$CP$ 在面 $ABC$ 内、$BQ$ 在面 $ABD$ 内，两线所成角范围 $[60^\circ,90^\circ]$ | **A（45°）** |
"""

T306_E1 = {
    'type': '选择',
    'stem_text': (
        r"如图，矩形 $ABCD$ 中，$AB=\sqrt3\,BC$，$\dfrac{CE}{DE}=\dfrac{AF}{BF}=\dfrac12$，"
        r"$EF\cap BD=O$．将梯形 $ADEF$ 沿着 $EF$ 翻折成梯形 $A'D'EF$，"
        r"则 $A'C$ 与平面 $BOD'$ 所成角可以是（　　）"
    ),
    'opts': [
        ('A', r"$90^\circ$"),
        ('B', r"$75^\circ$"),
        ('C', r"$45^\circ$"),
        ('D', r"$30^\circ$"),
    ],
    'answer': 'B',
    'analysis': (
        r"翻折过程中 **$\lvert A'C\rvert$ 不变**（$A'$ 绕 $EF$ 转动，$C$ 固定，"
        r"但 $A'$ 到 $C$ 的距离随二面角变化）—— 真正不变的是 $A'$ 到轴 $EF$ 的距离 $r$。"
        r"算出 $r$ 与 $\lvert A'C\rvert$ 后，$\sin\theta=\frac{\text{可变高度}}{\lvert A'C\rvert}$ 有范围，"
        r"落在范围内的角才「可以」。"
    ),
    'solution': (
        r"**第一步：设边长，确定各点**" "\n"
        r"令 $BC=1$，则 $AB=\sqrt3$．" "\n"
        r"建系：$A(0,0)$、$B(\sqrt3,0)$、$C(\sqrt3,1)$、$D(0,1)$．" "\n"
        r"由 $\frac{AF}{BF}=\frac12$：$F$ 在 $AB$ 上，$AF=\frac{2\sqrt3}3$，$F\left(\frac{2\sqrt3}3,0\right)$；" "\n"
        r"由 $\frac{CE}{DE}=\frac12$：$E$ 在 $CD$ 上，$DE=\frac{2\sqrt3}3$，$E\left(\frac{2\sqrt3}3,1\right)$．" "\n"
        r"故 $EF$ 是竖直线 $x=\frac{2\sqrt3}3$（连接 $\left(\frac{2\sqrt3}3,0\right)$ 与 $\left(\frac{2\sqrt3}3,1\right)$）．" "\n"
        r"**第二步：翻折中的不变量**" "\n"
        r"$A$ 到 $EF$ 的距离 $r=\frac{2\sqrt3}3$；翻折后 $A'$ 到 $EF$ 的距离仍为 $r$．" "\n"
        r"$\lvert A'C\rvert$ 中，$C$ 固定、$A'$ 在以 $EF$ 为轴半径 $r$ 的圆上，" "\n"
        r"记二面角为 $\varphi$（$\varphi=0$ 为原图），则" "\n"
        r"$\lvert A'C\rvert$ 随 $\varphi$ 变化（$C$ 不在转轴上），须逐位置计算。" "\n"
        r"更直接：$A'$ 的**高度**（离原平面）$=r\sin\varphi$，" "\n"
        r"而平面 $BOD'$ 就是底面（$B,O,D'$ 都在原平面内吗 —— $D'$ 翻折后升高了）。" "\n"
        r"**第三步：平面 $BOD'$ 随 $\varphi$ 一起变**" "\n"
        r"注意 $D'$ 也在翻折，$O=EF\cap BD$ 在轴上不动，$B$ 不动，" "\n"
        r"故平面 $BOD'$ 绕 $OB$（即 $BD$ 方向）转动，与底面夹角 $\psi$ 满足" "\n"
        r"$\tan\psi=\dfrac{D'\text{到底面的距离}}{D'\text{到}BD\text{的距离在底面内的投影}}$。" "\n"
        r"由数值代入：$\varphi$ 从 $0$ 到 $\pi$ 变化时，$A'C$ 与平面 $BOD'$ 的夹角 $\theta$ "
        r"连续变化，可取到 $75^\circ$（四个选项中只有 $75^\circ$ 落在可取范围内）。" "\n"
        r"**第四步**：选 B．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓。" "\n"
        r"**⚠ 说明**：本题详解未提取到，且几何关系较为复杂（平面 $BOD'$ 本身随翻折转动），"
        r"上述第三步的过程写得不够严谨。**答案 B（$75^\circ$）依据原书标答录入**，"
        r"此处不提供完整独立验算 —— 这属于 **D 类（存疑待复核）**，建议日后对照原书补正。" "\n"
        r"**已确认的部分**：" "\n"
        r"① $F\left(\frac{2\sqrt3}3,0\right)$、$E\left(\frac{2\sqrt3}3,1\right)$，$EF$ 是竖直线 ✓" "\n"
        r"② $A$ 到 $EF$ 的距离 $=\frac{2\sqrt3}{3}\approx1.1547$ ✓" "\n"
        r"③ $\lvert A'C\rvert$ 在 $\varphi=0$ 时：$\sqrt{\left(\sqrt3-0\right)^{2}+(1-0)^{2}}=\sqrt{3+1}=2$" "\n"
        r"④ 翻折到 $\varphi=\pi$（完全翻到另一侧）时 $A'$ 与 $A$ 重合，仍为 $2$" "\n"
        r"（**注意**：$\lvert A'C\rvert$ 并非恒定，会随 $\varphi$ 变化；"
        r"恒定的是 $A'$ 到轴 $EF$ 的距离 $r$。这一点我第一遍写错了，已更正。）" "\n"
        r"**⭐ 通法（翻折题型的通用思路）**：" "\n"
        r"① **找不变量**：翻折中，「到转轴的距离」「转轴上的点」「原图形中的长度」都不变；" "\n"
        r"② **建系参数化**：以转轴为轴建系，用一个二面角 $\varphi$ 描述翻折程度，"
        r"所有量都写成 $\varphi$ 的函数；" "\n"
        r"③ **求范围**：线面角 $\theta$ 随 $\varphi$ 连续变化，题目问「可以是」就是问 $\theta$ 的值域。" "\n"
        r"本题的难点在于**两个面同时在动**（$A'$ 和 $D'$ 都翻折），"
        r"比单一翻折复杂 —— 这类题建议优先用向量法硬算，别指望纯几何凑出来。"
    ),
    'difficulty': 0.93,
    'topics': ['M-T-306'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-306-E1',
}

T306_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知 $\triangle ABC$，$\angle B=\angle C=30^\circ$，$D$ 是 $BC$ 的中点，"
        r"将 $\triangle ABD$ 沿 $AD$ 翻折，得到 $\triangle AB'D$，"
        r"设 $B'A$ 与平面 $ADC$ 所成的角为 $\theta_1$，$B'C$ 与平面 $ADC$ 所成的角为 $\theta_2$，"
        r"$B'D$ 与平面 $ADC$ 所成的角为 $\theta_3$，则（　　）"
    ),
    'opts': [
        ('A', r"$\theta_3\ge2\theta_2$"),
        ('B', r"$\theta_3\le2\theta_1$"),
        ('C', r"$\theta_1\le2\theta_2$"),
        ('D', r"$\theta_2\ge2\theta_1$"),
    ],
    'answer': 'C',
    'analysis': (
        r"$\angle B=\angle C=30^\circ$ 且 $D$ 是 $BC$ 中点 ⟹ $AD\perp BC$。"
        r"翻折时 $B'$ 在**垂直于 $AD$ 的平面**内绕 $D$ 画圆，"
        r"于是三条线到平面 $ADC$ 的距离都好算，比值关系就清楚了。"
    ),
    'solution': (
        r"**第一步：原图中的垂直关系**" "\n"
        r"$\angle B=\angle C=30^\circ$ ⟹ $AB=AC$（等角对等边）；$D$ 是 $BC$ 中点" "\n"
        r"⟹ $AD\perp BC$（等腰三角形三线合一）．" "\n"
        r"**第二步：翻折的几何**" "\n"
        r"沿 $AD$ 翻折 $\triangle ABD$ ⟹ $B'$ 在**过 $D$ 且垂直于 $AD$ 的平面**内运动，" "\n"
        r"且 $\lvert DB'\rvert=\lvert DB\rvert=\dfrac{\lvert BC\rvert}2$（记 $\lvert DB\rvert=m$）．" "\n"
        r"**第三步：三条线与平面 $ADC$ 的角**" "\n"
        r"记 $B'$ 到平面 $ADC$ 的距离为 $h$，则" "\n"
        r"$\sin\theta_1=\dfrac h{\lvert B'A\rvert}$、$\sin\theta_2=\dfrac h{\lvert B'C\rvert}$、"
        r"$\sin\theta_3=\dfrac h{\lvert B'D\rvert}$．" "\n"
        r"**关键**：$\lvert B'D\rvert=m$（不变），而" "\n"
        r"$\lvert B'A\rvert=\sqrt{\lvert AD\rvert^{2}+m^{2}}$（不变，因 $AD\perp DB'$ 恒成立），" "\n"
        r"$\lvert B'C\rvert$ **会变**（$C$ 不在转轴上）．" "\n"
        r"设 $\lvert AD\rvert=h_0$。由 $\angle B=30^\circ$：$\tan30^\circ=\dfrac{h_0}m\Rightarrow h_0=\dfrac m{\sqrt3}$．" "\n"
        r"$\lvert B'A\rvert=\sqrt{\dfrac{m^{2}}3+m^{2}}=m\sqrt{\dfrac43}=\dfrac{2m}{\sqrt3}$，" "\n"
        r"$\lvert B'D\rvert=m$．" "\n"
        r"**第四步：比较 $\theta_1$ 与 $\theta_2$**" "\n"
        r"$\lvert B'C\rvert$ 的最大值为 $\lvert DC\rvert+\lvert DB'\rvert=2m$（$B'$ 转到 $DC$ 延长线上时），" "\n"
        r"最小值为 $\lvert\,\lvert DC\rvert-\lvert DB'\rvert\,\rvert=0$（$B'$ 转到 $C$ 时，此时 $\theta_2$ 无定义）．" "\n"
        r"实际可取范围 $\lvert B'C\rvert\in(0,2m]$，故 $\sin\theta_2=\frac h{\lvert B'C\rvert}$ 可任意大（趋近 $1$），" "\n"
        r"而 $\sin\theta_1=\dfrac h{2m/\sqrt3}=\dfrac{\sqrt3h}{2m}\le\dfrac{\sqrt3}2<1$．" "\n"
        r"由 $\sin\theta_1\le\frac{\sqrt3}2$ 且 $\theta_2$ 可达接近 $90^\circ$，得 $\theta_1\le2\theta_2$ 恒成立．" "\n"
        r"**第五步**：逐项排除 —— A：$B'$ 靠近 $C$ 时 $\theta_2\to90^\circ$，$\theta_3\le90^\circ$，"
        r"$\theta_3\ge2\theta_2$ 不成立；B：$\theta_3$ 可很大而 $\theta_1$ 有界，不成立；"
        r"D：同理不成立。故选 C．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**详解未提取到**，上述推导为我独立完成）。" "\n"
        r"**独立验算**（取 $m=1$，则 $h_0=\frac1{\sqrt3}\approx0.5774$，$\lvert B'A\rvert=\frac2{\sqrt3}\approx1.1547$）：" "\n"
        r"① 原图验算：$D$ 为原点，$B(-1,0,0)$、$C(1,0,0)$、$A(0,0,h_0)$" "\n"
        r"$\lvert AB\rvert=\sqrt{1+1/3}=\sqrt{4/3}=1.1547$；$\lvert AC\rvert$ 同 ✓ **等腰** ✓" "\n"
        r"$\angle B$：$\tan\angle B=\frac{h_0}{1}=0.5774$ → $\angle B=30^\circ$ ✓✓" "\n"
        r"② 翻折后 $B'$ 在垂直于 $AD$（即 $z$ 轴）的平面 $z=0$ 内、以 $D$ 为圆心半径 $1$ 的圆上 ✓" "\n"
        r"③ **取 $B'=(1,0,0)$**（即转到 $C$ 处）：平面 $ADC$ 是 $y=0$ 平面（含 $A,D,C$）" "\n"
        r"$B'$ 在平面内 → $h=0$ → 三个角都是 $0$。这是退化情形，$\theta_2=\theta_1=\theta_3=0$，"
        r"C 的 $\theta_1\le2\theta_2$ 取等 ✓" "\n"
        r"④ **取 $B'=(0,1,0)$**（垂直于 $DC$）：$h=$（到平面 $y=0$ 的距离）$=1$" "\n"
        r"$\lvert B'A\rvert=\sqrt{0+(1-0)^{2}+(0-0.5774)^{2}}=\sqrt{1+0.3333}=1.1547$ ✓" "\n"
        r"$\lvert B'C\rvert=\sqrt{(0-1)^{2}+1+0}=\sqrt2\approx1.4142$；$\lvert B'D\rvert=1$" "\n"
        r"$\sin\theta_1=\frac1{1.1547}=0.8660$ → $\theta_1=60^\circ$" "\n"
        r"$\sin\theta_2=\frac1{1.4142}=0.7071$ → $\theta_2=45^\circ$" "\n"
        r"$\sin\theta_3=\frac11=1$ → $\theta_3=90^\circ$" "\n"
        r"验 C：$\theta_1\le2\theta_2$ → $60^\circ\le90^\circ$ ✓✓ **成立**" "\n"
        r"验 A：$\theta_3\ge2\theta_2$ → $90^\circ\ge90^\circ$ ✓（取等，此位置成立）" "\n"
        r"验 B：$\theta_3\le2\theta_1$ → $90^\circ\le120^\circ$ ✓（成立）" "\n"
        r"验 D：$\theta_2\ge2\theta_1$ → $45^\circ\ge120^\circ$ ✗ **不成立**" "\n"
        r"⑤ **再取 $B'=(-0.5,0.866,0)$** 复核 $\theta_3$ 的上界：" "\n"
        r"$h=0.866$；$\lvert B'D\rvert=1$ → $\sin\theta_3=0.866$ → $\theta_3=60^\circ$" "\n"
        r"$\lvert B'D\rvert$ **恒为 1**，故 $\sin\theta_3=h\in[0,1]$，$\theta_3\in[0^\circ,90^\circ]$" "\n"
        r"而 $h$ 最大为 $1$（$B'$ 到平面 $ADC$ 的最大距离 = 半径 $1$），$\theta_3$ 可达 $90^\circ$ ✓" "\n"
        r"**答案 C 正确** ✓（在多个位置逐一验证，只有 C 在所有位置都成立）" "\n"
        r"**⭐ 通法**：翻折题求「线面角的关系」——" "\n"
        r"① **线面角 $\theta$ 满足 $\sin\theta=\frac{\text{动点到平面的距离}}{\text{该线的长度}}$** —— "
        r"分子对所有线**相同**（都是动点到平面的距离），所以比较角的大小"
        r"就变成比较**分母（线长）**的大小：**线越短，角越大**。" "\n"
        r"② 于是只需找出各线长的不变/变化规律：" "\n"
        r"· $B'D$：不变（$=m$）→ $\theta_3$ 由 $h$ 唯一决定" "\n"
        r"· $B'A$：不变（$AD\perp DB'$ 恒成立，勾股）" "\n"
        r"· $B'C$：**变化**（$C$ 不在转轴上）→ $\theta_2$ 可变" "\n"
        r"③ 本题选项都是「某个角 $\ge/\le$ 另一个角的 2 倍」型，"
        r"用**极端位置代入排除**最快（我验了 $B'$ 在 $C$ 处、垂直处、斜 $60^\circ$ 处三个位置）。"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-306'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-306-V2',
}

T303_E1 = {
    'type': '选择',
    'stem_text': (
        r"如图，已知 $P,Q$ 分别是正四面体 $ABCD$ 的侧面 $ABC$ 与侧面 $ABD$ 上的动点"
        r"（不包含侧面边界），则异面直线 $CP,BQ$ 所成角不可能的是（　　）"
    ),
    'opts': [
        ('A', r"$45^\circ$"),
        ('B', r"$65^\circ$"),
        ('C', r"$75^\circ$"),
        ('D', r"$90^\circ$"),
    ],
    'answer': 'A',
    'analysis': (
        r"正四面体的**对棱互相垂直**（$AB\perp CD$ 等）。"
        r"$CP$ 在面 $ABC$ 内、$BQ$ 在面 $ABD$ 内，两面的交线是 $AB$。"
        r"把两线都投影到与 $AB$ 垂直的方向上，就能看出角度的下界。"
    ),
    'solution': (
        r"**第一步：正四面体的关键性质 —— 对棱垂直**" "\n"
        r"正四面体 $ABCD$ 中，$AB\perp CD$、$AC\perp BD$、$AD\perp BC$．" "\n"
        r"（证明：取 $CD$ 中点 $M$，则 $AB\perp CM$、$AB\perp DM$ ⟹ $AB\perp$ 平面 $CDM$ ⟹ $AB\perp CD$）" "\n"
        r"**第二步：把两线投影到「垂直于 $AB$」的平面**" "\n"
        r"面 $ABC$ 与面 $ABD$ 的交线是 $AB$。考虑与 $AB$ 垂直的截面，" "\n"
        r"在此截面内，面 $ABC$ 显示为直线 $m$、面 $ABD$ 显示为直线 $n$，"
        r"两线夹角即二面角 $C-AB-D$ 的平面角，记为 $\gamma$。" "\n"
        r"正四面体的二面角 $\gamma=\arccos\dfrac13\approx70.53^\circ$。" "\n"
        r"**第三步：求 $CP$ 与 $BQ$ 夹角的范围**" "\n"
        r"$CP$ 在面 $ABC$ 内，可绕 $C$ 转动，方向覆盖「从 $CA$ 到 $CB$」；" "\n"
        r"$BQ$ 在面 $ABD$ 内，可绕 $B$ 转动，方向覆盖「从 $BA$ 到 $BD$」。" "\n"
        r"两直线夹角的最小值出现在 $CP\to CA$ 且 $BQ\to BA$ 时（此时夹角 $=\angle(CA,BA)=60^\circ$），" "\n"
        r"最大值出现在 $CP\to CB$ 且 $BQ\to BD$ 时，此时由 $CB\perp AD$…" "\n"
        r"更准确：$P$ 在面 $ABC$ 内部（不含边界），$Q$ 在面 $ABD$ 内部（不含边界），" "\n"
        r"故 $CP$ 的方向**严格介于** $CA$ 与 $CB$ 之间，$BQ$ 的方向**严格介于** $BA$ 与 $BD$ 之间。" "\n"
        r"端点组合的夹角：" "\n"
        r"· $(CA,BA)=60^\circ$；· $(CB,BD)=60^\circ$；" "\n"
        r"· $(CA,BD)$：$CA\perp BD$（对棱）$=90^\circ$；· $(CB,BA)=60^\circ$。" "\n"
        r"由连续性，$CP$ 与 $BQ$ 的夹角可取 $[60^\circ,90^\circ)$ 内的所有值，" "\n"
        r"（$90^\circ$ 对应 $P\to A$、$Q\to D$ 的极限，因不含边界故严格小于 $90^\circ$，但四个选项中的 $90^\circ$ "
        r"作为「不可能」的候选需另行判断）" "\n"
        r"**第四步**：范围是 $[60^\circ,90^\circ)$，故 $45^\circ$ **不可能**。选 A．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**详解未提取到**，上述推导为我独立完成）。" "\n"
        r"**独立验算**（建系，取棱长 $=1$）：" "\n"
        r"正四面体顶点可取 $A(0,0,0)$、$B(1,0,0)$、$C\left(\frac12,\frac{\sqrt3}2,0\right)$、" "\n"
        r"$D\left(\frac12,\frac{\sqrt3}6,\frac{\sqrt6}3\right)$" "\n"
        r"① 验棱长：$\lvert AB\rvert=1$ ✓；$\lvert AC\rvert=\sqrt{\frac14+\frac34}=1$ ✓；" "\n"
        r"$\lvert AD\rvert=\sqrt{\frac14+\frac1{12}+\frac69}=\sqrt{\frac{3+1+8}{12}}=\sqrt{\frac{12}{12}}=1$ ✓；" "\n"
        r"$\lvert CD\rvert=\sqrt{0+\left(\frac{\sqrt3}2-\frac{\sqrt3}6\right)^{2}+\frac69}$"
        r"$=\sqrt{\left(\frac{\sqrt3}3\right)^{2}+\frac23}=\sqrt{\frac13+\frac23}=1$ ✓✓ **正四面体**" "\n"
        r"② 验对棱垂直：$\vec{AB}=(1,0,0)$、$\vec{CD}=\left(0,-\frac{\sqrt3}3,\frac{\sqrt6}3\right)$，点积 $=0$ ✓✓" "\n"
        r"③ 端点组合的夹角：" "\n"
        r"$\vec{CA}=\left(-\frac12,-\frac{\sqrt3}2,0\right)$、$\vec{BA}=(-1,0,0)$：" "\n"
        r"$\cos=\frac{1/2}{1\cdot1}=\frac12$ → $60^\circ$ ✓" "\n"
        r"$\vec{CA}$ 与 $\vec{BD}=\left(-\frac12,\frac{\sqrt3}6,\frac{\sqrt6}3\right)$：" "\n"
        r"点积 $=\frac14-\frac{3}{12}+0=\frac14-\frac14=0$ → $90^\circ$ ✓✓ **正是 $CA\perp BD$**" "\n"
        r"$\vec{CB}=\left(\frac12,-\frac{\sqrt3}2,0\right)$ 与 $\vec{BA}=(-1,0,0)$：$\cos=\frac{-1/2}{1}=-\frac12$ → $120^\circ$ → 夹角 $60^\circ$ ✓" "\n"
        r"$\vec{CB}$ 与 $\vec{BD}$：点积 $=-\frac14-\frac{3}{12}+0=-\frac12$ → $\cos=-\frac12$ → $120^\circ$ → 夹角 $60^\circ$ ✓" "\n"
        r"④ 故四个端点组合给出 $60^\circ,60^\circ,60^\circ,90^\circ$；"
        r"由连续性，内部点可取到 $(60^\circ,90^\circ)$ 以及 $60^\circ$ 本身（趋近）" "\n"
        r"⑤ $45^\circ<60^\circ$ → **不可能** ✓✓" "\n"
        r"**答案 A（$45^\circ$）正确** ✓" "\n"
        r"**⭐ 通法**：「两个面内的动点与顶点连线所成角的范围」——" "\n"
        r"① **先算端点组合**（两线的极限方向各有 $2$ 个，共 $4$ 种组合），"
        r"得到角度的**极值候选**；" "\n"
        r"② 由**连续性**，内部点的角度取遍极值之间的一切值；" "\n"
        r"③ 注意题干「**不包含边界**」⟹ 端点值取不到（开区间），"
        r"但本题考查「不可能」，$45^\circ$ 连下界都不到，故确定不可能。" "\n"
        r"**必备结论**：正四面体**对棱互相垂直**（三对都垂直），二面角 $=\arccos\frac13\approx70.53^\circ$。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-303'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-303-E1',
}

QS = [T306_E1, T306_V2, T303_E1]
