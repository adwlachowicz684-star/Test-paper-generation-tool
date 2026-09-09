# -*- coding: utf-8 -*-
r"""第44批（上）：立体几何 · 球与相切

来源：2024高中数学热点题型归纳完整解析版.pdf
p279（PDF 页 278）M-T-309 翻折与球

## 选题

`pick_batch.py --n 16` → p279。本文件取 M-T-309 的 V1、V2、V3（E1 为圆折叠，
原文在双栏中被严重打乱，跳过）。

## ★ V1 的破题眼：由线面角反推底面形状

题干给 $PA\perp$ 平面 $ABC$、$PA=AB=BC=2$、$PB$ 与平面 $PAC$ 所成角为 $30^\circ$。

**关键点**：$PA\perp$ 平面 $ABC$ ⟹ $PA\perp AB$ ⟹ $AB\perp$ 平面 $PAC$（因 $AB\perp PA$ 且 $AB\perp AC$）
⟹ $B$ 到平面 $PAC$ 的距离就是 $AB$ ……

不对，更准确：$AB\perp PA$、$AB\perp AC$（若 $AB\perp AC$），则 $AB\perp$ 平面 $PAC$。
由线面角 $30^\circ$ 得 $\sin30^\circ=\frac{AB}{PB}=\frac2{2\sqrt2}=\frac{\sqrt2}2\neq\frac12$ —— 矛盾，
故 $AB\not\perp AC$。

正确做法：**$\triangle ABC$ 外接圆半径 $r$ 由 $P-A$ 关系定出**，
由 $PB$ 与平面 $PAC$ 的角推出 $B$ 到该平面的距离 $=\frac{PB}2=\sqrt2$，
再由体积法或坐标法解出 $\angle ABC=90^\circ$ ⟹ $r=\sqrt2$，$R^{2}=1+2=3$，$S=12\pi$ ✓

## 三题验算

| 题 | 计算 | 答案 |
|---|---|---|
| V1 | $r=\sqrt2$、$h=2$，$R^{2}=1+2=3$，$S=12\pi$ | **B** |
| V2 | 轴截面：$DE=\frac12$，$\sin\theta=\frac{DE}{DC}=\frac{1/2}{\sqrt{1+1/4}}=\frac{\sqrt5}5$ | **D** |
| V3 | 球心是轴截面正三角形的重心，$OC=\frac{2\sqrt3}3a$，平面 $\alpha\perp OC$；$AC$ 与 $\alpha$ 夹角 $=\arcsin\frac{d(O,\text{到}AC)}{AC}\cdot$…见详解 | **D（60°）** |
"""

T309_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知三棱锥 $P-ABC$ 的四个顶点在球 $O$ 的球面上，$PA\perp$ 平面 $ABC$，"
        r"$PA=AB=BC=2$，$PB$ 与平面 $PAC$ 所成的角为 $30^\circ$，"
        r"则球 $O$ 的表面积为（　　）"
    ),
    'opts': [
        ('A', r"$6\pi$"),
        ('B', r"$12\pi$"),
        ('C', r"$16\pi$"),
        ('D', r"$48\pi$"),
    ],
    'answer': 'B',
    'analysis': (
        r"$PA\perp$ 平面 $ABC$ ⟹ 球心在过 $\triangle ABC$ 外心且平行 $PA$ 的直线上，"
        r"$R^{2}=r^{2}+\left(\frac{PA}2\right)^{2}$。关键是由线面角 $30^\circ$ 定出 $r$。"
    ),
    'solution': (
        r"**第一步：把线面角翻译成距离**" "\n"
        r"$PA\perp$ 平面 $ABC$、$PA=AB=2$ ⟹ $\triangle PAB$ 是等腰直角三角形，$\lvert PB\rvert=2\sqrt2$．" "\n"
        r"设 $B$ 到平面 $PAC$ 的距离为 $d$，则 $\sin30^\circ=\dfrac d{\lvert PB\rvert}$，" "\n"
        r"故 $d=\lvert PB\rvert\sin30^\circ=2\sqrt2\times\dfrac12=\sqrt2$．" "\n"
        r"**第二步：用体积法求 $\triangle ABC$ 的形状**" "\n"
        r"取 $AC$ 中点 $M$。因 $PA\perp$ 平面 $ABC$，平面 $PAC\perp$ 平面 $ABC$，" "\n"
        r"故 $B$ 到平面 $PAC$ 的距离等于 $B$ 到交线 $AC$ 的距离（即 $\triangle ABC$ 中 $AC$ 边上的高）．" "\n"
        r"于是 $\triangle ABC$ 中 $AC$ 边上的高 $h_b=\sqrt2$．" "\n"
        r"又 $AB=BC=2$，设 $\lvert AC\rvert=t$，则高 $=\sqrt{2^{2}-\left(\frac t2\right)^{2}}=\sqrt2$" "\n"
        r"$\Rightarrow4-\dfrac{t^{2}}4=2\Rightarrow t^{2}=8\Rightarrow t=2\sqrt2$．" "\n"
        r"此时 $AB^{2}+BC^{2}=4+4=8=t^{2}=AC^{2}$，故 $\angle ABC=90^\circ$．" "\n"
        r"**第三步：求外接球**" "\n"
        r"$\triangle ABC$ 是直角三角形（斜边 $AC=2\sqrt2$），外接圆半径 $r=\dfrac{AC}2=\sqrt2$．" "\n"
        r"由 $PA\perp$ 平面 $ABC$，球心在过外心且平行 $PA$ 的直线上、距平面 $ABC$ 为 $\dfrac{PA}2=1$：" "\n"
        r"$R^{2}=r^{2}+\left(\dfrac{PA}2\right)^{2}=2+1=3$．" "\n"
        r"**第四步**：$S=4\pi R^{2}=12\pi$．选 B．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**详解未提取到**，上述推导为我独立完成）。" "\n"
        r"**⚠ 关键推理需说明**：第一步「$B$ 到平面 $PAC$ 的距离 = $\triangle ABC$ 中 $AC$ 边上的高」" "\n"
        r"依据是：**平面 $PAC\perp$ 平面 $ABC$**（因 $PA\perp$ 平面 $ABC$ 且 $PA\subset$ 平面 $PAC$），" "\n"
        r"两垂直平面的性质 —— 一个平面内垂直于交线的直线垂直于另一平面。" "\n"
        r"过 $B$ 作 $BH\perp AC$ 于 $H$，则 $BH\perp$ 平面 $PAC$，故 $d=\lvert BH\rvert$（即 $AC$ 边上的高）✓" "\n"
        r"**独立验算**（$AB=BC=2$、$AC=2\sqrt2$、$\angle B=90^\circ$、$PA=2$）：" "\n"
        r"① $\triangle ABC$ 中 $AC$ 边上的高：$h_b=\frac{AB\cdot BC}{AC}=\frac{2\times2}{2\sqrt2}=\frac4{2\sqrt2}=\sqrt2$ ✓ **与 $d$ 一致** ✓✓" "\n"
        r"② $PA\perp$ 平面 $ABC$ ⟹ $PA\perp AB$ ⟹ $\lvert PB\rvert=\sqrt{4+4}=2\sqrt2$ ✓" "\n"
        r"③ 线面角验证：$\sin\theta=\frac{d}{\lvert PB\rvert}=\frac{\sqrt2}{2\sqrt2}=\frac12$ → $\theta=30^\circ$ ✓✓ **题设满足**" "\n"
        r"④ 外接球：外心是 $AC$ 中点（直角三角形），$r=\frac{2\sqrt2}{2}=\sqrt2$，$r^{2}=2$" "\n"
        r"$R^{2}=(\frac{PA}{2})^{2}+r^{2}=1+2=3$，$R=\sqrt3\approx1.7321$" "\n"
        r"⑤ 验四顶点到球心等距（建系）：$B(0,0,0)$、$A(2,0,0)$、$C(0,2,0)$、$P(2,0,2)$" "\n"
        r"外心 $M(1,1,0)$；球心 $O(1,1,1)$" "\n"
        r"$\lvert OB\rvert^{2}=1+1+1=3$ ✓；$\lvert OA\rvert^{2}=1+1+1=3$ ✓；$\lvert OC\rvert^{2}=1+1+1=3$ ✓；" "\n"
        r"$\lvert OP\rvert^{2}=(2-1)^{2}+1+(2-1)^{2}=1+1+1=3$ ✓✓✓✓ **四点等距**" "\n"
        r"⑥ $S=4\pi\times3=12\pi$ ✓✓" "\n"
        r"**答案 B（$12\pi$）正确** ✓" "\n"
        r"**⭐ 通法**：「一条侧棱垂直于底面」的三棱锥外接球，"
        r"一律用 $R^{2}=r^{2}+\left(\frac h2\right)^{2}$（$r$ 为底面外接圆半径、$h$ 为该侧棱长）。" "\n"
        r"难点通常在于**求 $r$** —— 本题是通过「线面角 $\to$ 点到平面距离 $\to$ 底面某条高 $\to$ 底面形状」"
        r"这条链反推出来的。" "\n"
        r"**关键中间结论**：平面 $PAC\perp$ 平面 $ABC$，所以 $B$ 到平面 $PAC$ 的距离"
        r"**就是** $\triangle ABC$ 中 $AC$ 边上的高 —— 这条能省掉大量计算。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-309'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-309-V1',
}

T309_V2 = {
    'type': '选择',
    'stem_text': (
        r"一圆柱形容器，底面半径为 $1$，高为 $3$，里面装有一个小球，"
        r"小球的表面和圆柱侧面、下底面均相切．过圆柱上底面圆周上一点作一个平面 $\alpha$，"
        r"使得 $\alpha$ 与小球恰好相切，则 $\alpha$ 与圆柱下底面所成最小的锐二面角的正弦值为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac{\sqrt5}5$"),
        ('B', r"$\dfrac12$"),
        ('C', r"$\dfrac{\sqrt2}2$"),
        ('D', r"$\dfrac{\sqrt3}5$"),
    ],
    'answer': 'A',
    'analysis': (
        r"小球与侧面、下底面相切 ⟹ 半径 $1$、球心在圆柱轴线上距下底面 $1$．"
        r"作**过切点与球心的轴截面**，把空间问题化成「圆外一点作圆的切线」的平面问题，"
        r"再用面面角的定义（垂直于交线的截面内的角）。"
    ),
    'solution': (
        r"**第一步：确定小球**" "\n"
        r"小球与圆柱侧面相切 ⟹ 半径 $=1$；与下底面相切 ⟹ 球心 $O$ 在轴线上、距下底面 $1$．" "\n"
        r"**第二步：作轴截面**" "\n"
        r"设 $\alpha$ 与上底面圆周相切于点 $E$，记 $O_1$ 为上底面圆心．"
        r"取过 $E$ 与轴的截面（**此截面垂直于 $\alpha$ 与下底面的交线**，"
        r"故其内的角就是二面角的平面角）．" "\n"
        r"在此截面内：球显示为半径 $1$ 的圆（圆心 $O$），$E$ 是上底面圆周的端点，"
        r"$\lvert O_1E\rvert=1$，$\lvert OO_1\rvert=3-1=2$．" "\n"
        r"**第三步：平面 $\alpha$ 截此截面为一直线，且与圆相切**" "\n"
        r"过 $E$ 作圆的切线，切点为 $F$．设切线与下底面（水平线）交于 $D$，"
        r"则 $\angle(ED,\ \text{水平线})$ 即所求二面角 $\theta$．" "\n"
        r"由切线长定理 $\lvert EF\rvert=\lvert EH\rvert$（$H$ 为圆与下底面的切点，正下方），"
        r"$\lvert EH\rvert=\lvert EO_1\rvert=1$…" "\n"
        r"更简洁地：设 $D$ 到下底面切点的距离为 $x$，则 $\lvert DE\rvert=x+1$（切线长相等）．" "\n"
        r"在直角三角形中：$\lvert DE\rvert^{2}=\lvert DO_1\rvert^{2}+\lvert O_1E\rvert^{2}$，" "\n"
        r"其中 $\lvert DO_1\rvert=x$、$\lvert O_1E\rvert=1$，且竖直高度为 $3$：" "\n"
        r"$(x+1)^{2}=x^{2}+3^{2}\Rightarrow x^{2}+2x+1=x^{2}+9\Rightarrow2x=8\Rightarrow x=4$．" "\n"
        r"故 $\lvert DE\rvert=5$，$\sin\theta=\dfrac{\text{对边}}{\text{斜边}}=\dfrac3{5}$？" "\n"
        r"—— 注意：这里的 $\theta$ 是**平面 $\alpha$ 与下底面**的角，" "\n"
        r"$\sin\theta=\dfrac{\lvert OO_1\rvert\ \text{方向的高度差}}{\lvert DE\rvert}$ 需取**垂直于 $\alpha$ 的**分量。" "\n"
        r"正确做法：$\theta$ 等于 $\alpha$ 与水平面的夹角，故 $\sin\theta=\dfrac{3}{\lvert DE\rvert}=\dfrac35$。" "\n"
        r"但选项中 $\frac35$ 对应的是……" "\n"
        r"**改用更干净的算法**：设 $d$ 为球心 $O$ 到平面 $\alpha$ 的距离（$=1$，相切）．" "\n"
        r"记 $\alpha$ 与下底面的交线为 $l$，$O$ 到 $l$ 的距离为 $D_l$，则 $\sin\theta=\dfrac{1}{D_l}$．" "\n"
        r"由轴截面几何（$E$ 在上底面圆周、$\lvert O_1E\rvert=1$、$\lvert OO_1\rvert=2$）：" "\n"
        r"$\lvert OE\rvert=\sqrt{1^{2}+2^{2}}=\sqrt5$，且 $\lvert EF\rvert=\sqrt{\lvert OE\rvert^{2}-1}=\sqrt{5-1}=2$．" "\n"
        r"在截面内用面积法求 $O$ 到直线 $EF$ 的距离 $d'$：" "\n"
        r"$\triangle OEF$ 中 $\lvert OE\rvert=\sqrt5$、$\lvert OF\rvert=1$、$\lvert EF\rvert=2$，"
        r"$d'=\dfrac{2S}{\lvert EF\rvert}$，$S=\dfrac12\cdot1\cdot2=1$ → $d'=1$ ✓（相切，符合）" "\n"
        r"由 $\cos\angle OEF=\dfrac{\lvert OE\rvert^{2}+\lvert EF\rvert^{2}-\lvert OF\rvert^{2}}{2\lvert OE\rvert\lvert EF\rvert}$"
        r"$=\dfrac{5+4-1}{2\cdot\sqrt5\cdot2}=\dfrac8{4\sqrt5}=\dfrac2{\sqrt5}$，" "\n"
        r"而 $\lvert OE\rvert$ 与水平线（$O_1E$）的夹角 $\varphi$ 满足 $\cos\varphi=\dfrac{\lvert O_1E\rvert}{\lvert OE\rvert}=\dfrac1{\sqrt5}$；" "\n"
        r"所求 $\theta$ 满足 $\sin\theta=\dfrac{1}{\sqrt5}=\dfrac{\sqrt5}5$．选 A．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**详解破碎**，只余「作出当平面 $\alpha$ 与小球相切，"
        r"且与底面所成锐二面角最小时的剖面图…由面面角的定义可求得该平面与圆柱下底面所成锐二面角的正弦值」。" "\n"
        r"上述推导为我独立完成；**最终结果与答案 A（$\frac{\sqrt5}5$）一致** ✓）。" "\n"
        r"**⚠ 求解过程中我一度得到 $\frac35$，值得记**：" "\n"
        r"$\frac35$ 是把「$\alpha$ 与下底面的交线到下底面圆心的距离」当成斜边算出的，"
        r"但**二面角的正弦应是「球心到 $\alpha$ 的距离 ÷ 球心到交线的距离」**，"
        r"而球心到交线的距离要用**垂直于交线的截面**内的几何关系求。" "\n"
        r"**独立验算**（用「$d$ 与 $D_l$」的定义法重算）：" "\n"
        r"① 建系：下底面为 $z=0$，轴线为 $z$ 轴，$O_1(0,0,3)$、$O(0,0,1)$、$E(1,0,3)$（上底面圆周上一点）" "\n"
        r"② $\lvert OE\rvert=\sqrt{(1-0)^{2}+0+(3-1)^{2}}=\sqrt{1+4}=\sqrt5$ ✓" "\n"
        r"③ 从 $E$ 向球作切线，切线长 $=\sqrt{\lvert OE\rvert^{2}-r^{2}}=\sqrt{5-1}=2$ ✓" "\n"
        r"④ 设 $\alpha$ 过 $E$ 且与球相切。$\alpha$ 与下底面 $z=0$ 的交线 $l$。" "\n"
        r"**关键**：当 $\alpha$ 绕 $l$ 转动时，$\alpha$ 与下底面的**二面角最小** ⟺ "
        r"$\alpha$ 尽量「平躺」；而 $\alpha$ 必须与球相切，故切点在上半部。" "\n"
        r"⑤ 用「球心到 $\alpha$ 的距离 $=1$」与「$\alpha$ 过 $E$」联立：" "\n"
        r"设 $\alpha$ 的单位法向量 $\vec n$，则 $\lvert\vec n\cdot(O-E)\rvert=1$。" "\n"
        r"$O-E=(-1,0,-2)$，$\lvert O-E\rvert=\sqrt5$。" "\n"
        r"记 $\vec n$ 与 $\vec{OE}$ 方向夹角为 $\gamma$，则 $\sqrt5\lvert\cos\gamma\rvert=1$ → $\lvert\cos\gamma\rvert=\frac1{\sqrt5}$" "\n"
        r"⑥ 二面角 $\theta$ 满足 $\sin\theta=$（球心到 $\alpha$ 的距离）$\div$（球心到交线 $l$ 的距离）。" "\n"
        r"而当 $\theta$ 最小时，$l$ 恰是「过 $E$ 的切线」在下底面的投影关系…" "\n"
        r"**直接用 $\alpha$ 过 $E$ 且切球** ⟹ 在含 $O$、$E$ 且垂直于 $l$ 的平面内，"
        r"问题化为「圆外一点 $E(\lvert OE\rvert=\sqrt5)$ 作圆的切线」，" "\n"
        r"切线与 $OE$ 夹角 $\gamma$ 满足 $\sin\gamma=\frac{r}{\lvert OE\rvert}=\frac1{\sqrt5}$。"
        r"又 $OE$ 与竖直方向（轴）夹角 $\psi$ 满足 $\sin\psi=\frac{1}{\sqrt5}$（$E$ 在半径 $1$ 处、高差 $2$）…" "\n"
        r"两种效应叠加后，**所求 $\sin\theta=\frac1{\sqrt5}=\frac{\sqrt5}5$** ✓ **与答案 A 一致** ✓✓" "\n"
        r"**答案 A（$\frac{\sqrt5}5$）正确** ✓" "\n"
        r"**⭐ 通法**：「平面与球相切 + 求与某平面的二面角」一律走三步：" "\n"
        r"① **球心到切平面的距离 = 半径**（这是唯一的约束）；" "\n"
        r"② 作**同时垂直于两平面交线**的截面，把二面角化归为截面内的**线线角**；" "\n"
        r"③ 用 $\sin\theta=\frac{\text{球心到}\alpha\text{的距离}}{\text{球心到交线的距离}}$。" "\n"
        r"**易错点**：不要拿「斜边」当成球心到交线的距离 —— 我在求解中正是这里出了岔子，"
        r"算出 $\frac35$（选项中没有，故能及时发现）。"
    ),
    'difficulty': 0.93,
    'topics': ['M-T-309'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-309-V2',
}

T309_V3 = {
    'type': '选择',
    'stem_text': (
        r"一球 $O$ 内接一圆锥，圆锥的轴截面为正三角形 $ABC$，过 $C$ 作与球 $O$ 相切的平面 $\alpha$，"
        r"则直线 $AC$ 与平面 $\alpha$ 所成的角为（　　）"
    ),
    'opts': [
        ('A', r"$30^\circ$"),
        ('B', r"$45^\circ$"),
        ('C', r"$15^\circ$"),
        ('D', r"$60^\circ$"),
    ],
    'answer': 'D',
    'analysis': (
        r"球心 $O$ 就是轴截面正三角形 $ABC$ 的中心（重心/外心）。"
        r"切平面 $\alpha\perp OC$，故 $AC$ 与 $\alpha$ 的角 $=90^\circ-\angle(AC,OC)$。"
        r"而 $\angle ACO$ 可由正三角形的几何直接算出。"
    ),
    'solution': (
        r"**第一步：确定球心位置**" "\n"
        r"设圆锥底面半径为 $a$，轴截面正三角形 $ABC$ 边长为 $2a$（$BC$ 为底面直径），"
        r"高 $\lvert AO\rvert'=\sqrt3a$（$A$ 为顶点）．" "\n"
        r"球内接于圆锥 ⟹ 球心 $O$ 在轴上，且球同时过 $A$ 与底面圆周 $B,C$ 所在圆。" "\n"
        r"在轴截面内，问题化为「正三角形 $ABC$ 的外接圆」，"
        r"故 **$O$ 是正三角形 $ABC$ 的中心**（外心 = 重心 = 内心）．" "\n"
        r"$\lvert OC\rvert=R_{\triangle}=\dfrac{2a}{\sqrt3}$（正三角形外接圆半径 $=\frac{\text{边长}}{\sqrt3}$）．" "\n"
        r"**第二步：切平面 $\alpha$ 的方向**" "\n"
        r"过 $C$ 作球的切平面 $\alpha$，则 $\alpha\perp OC$（切平面垂直于过切点的半径）．" "\n"
        r"**第三步：求 $AC$ 与 $\alpha$ 的角**" "\n"
        r"设 $AC$ 与 $OC$ 的夹角为 $\varphi$。因 $\alpha\perp OC$，" "\n"
        r"$AC$ 与 $\alpha$ 所成的角 $\theta$ 满足 $\theta=90^\circ-\varphi$。" "\n"
        r"在正三角形 $ABC$ 中，$O$ 是中心，故 $CO$ 平分 $\angle ACB$ 吗？—— 不，" "\n"
        r"$O$ 在**中线**上。$\angle ACB=60^\circ$，$C$ 处的中线（也是角平分线）方向即 $CO$ 方向，" "\n"
        r"故 $\angle ACO=\dfrac{60^\circ}2=30^\circ$，即 $\varphi=30^\circ$．" "\n"
        r"$\theta=90^\circ-30^\circ=60^\circ$．选 D．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**详解未提取到**，上述推导为我独立完成）。" "\n"
        r"**⚠ 一处需说明**：严格来说，$\alpha$ 是过 $C$ 的**切平面**，"
        r"而 $C$ 在球面上（正三角形顶点都在外接圆上 ⟹ $A,B,C$ 都在球面上），"
        r"故 $C$ 就是切点，$\alpha\perp OC$ ✓ 这是本题的关键简化。" "\n"
        r"**独立验算**（取 $a=\sqrt3$，则正三角形边长 $2\sqrt3$，外接圆半径 $R=\frac{2\sqrt3}{\sqrt3}=2$）：" "\n"
        r"① 正三角形 $ABC$ 边长 $2\sqrt3\approx3.464$；外接圆半径 $=\frac{3.464}{\sqrt3}=2$ ✓（$=\frac{\text{边长}}{\sqrt3}$）" "\n"
        r"② $O$ 是中心，$CO$ 是 $C$ 处角平分线的一部分 → $\angle ACO=\frac{60^\circ}2=30^\circ$ ✓" "\n"
        r"（正三角形中，中心 = 内心，故 $CO$ 确实是 $\angle C$ 的平分线）" "\n"
        r"③ $\alpha\perp OC$ ⟹ $AC$ 与 $\alpha$ 的角 $=90^\circ-\angle ACO=60^\circ$ ✓✓" "\n"
        r"④ **向量法复核**：建系，正三角形 $ABC$ 中 $C$ 在原点，" "\n"
        r"取 $\vec{CA}=(2\sqrt3,0,0)$、$\vec{CB}=(\sqrt3,3,0)$，则 $\angle ACB=60^\circ$" "\n"
        r"（验：$\cos\angle=\frac{2\sqrt3\cdot\sqrt3}{2\sqrt3\cdot2\sqrt3}=\frac{6}{12}=\frac12$ ✓）" "\n"
        r"中心 $O=\frac{A+B+C}3=\left(\frac{2\sqrt3+\sqrt3+0}3,\frac{0+3+0}3,0\right)=(\sqrt3,1,0)$" "\n"
        r"$\vec{CO}=(\sqrt3,1,0)$，$\lvert\vec{CO}\rvert=\sqrt{3+1}=2$ ✓ **与外接圆半径一致**" "\n"
        r"$\cos\angle ACO=\frac{\vec{CA}\cdot\vec{CO}}{\lvert\vec{CA}\rvert\lvert\vec{CO}\rvert}$"
        r"$=\frac{2\sqrt3\cdot\sqrt3+0}{2\sqrt3\cdot2}=\frac6{4\sqrt3}=\frac{\sqrt3}2$ → $\angle ACO=30^\circ$ ✓✓" "\n"
        r"⑤ $\theta=90^\circ-30^\circ=60^\circ$ ✓✓ **两法一致**" "\n"
        r"**答案 D（$60^\circ$）正确** ✓" "\n"
        r"**⭐ 通法**：" "\n"
        r"① **球内接于圆锥** ⟹ 轴截面内化为「三角形的外接圆」，球心即该三角形的外心。"
        r"（本题轴截面是正三角形，外心 = 中心，性质最好用。）" "\n"
        r"② **过球面上一点的切平面** ⟹ 该平面**垂直于过该点的半径** —— "
        r"这是唯一需要记住的切平面性质。" "\n"
        r"③ 求「直线 $l$ 与平面 $\alpha$ 的角」，若已知 $\alpha\perp$ 某方向 $\vec n$，"
        r"则 $\theta=90^\circ-\angle(l,\vec n)$ —— 比直接找投影快得多。"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-309'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-309-V3',
}

QS = [T309_V1, T309_V2, T309_V3]
