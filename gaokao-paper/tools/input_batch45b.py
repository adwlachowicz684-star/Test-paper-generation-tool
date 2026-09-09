# -*- coding: utf-8 -*-
r"""第45批（下）：外接球（直角模型 + 正四面体向量）

来源：2024高中数学热点题型归纳完整解析版.pdf
p261（PDF 页 260）M-T-294 补形法求外接球
p266（PDF 页 265）M-T-298 球与截面、球心向量表示

## 选题

本文件取 M-T-294 的 V1、V2 + M-T-298 的 V3。

## ★★ 本批最有价值的两个结论

**结论一（V1 推出的通用公式）** —— $BC\perp AB$、$BC\perp CD$，$AB$ 与 $CD$ 夹角 $\theta$：

$$R^{2}=\frac{BC^{2}}4+\frac{AD^{2}-BC^{2}}{4\sin^{2}\theta}$$

**$R$ 只依赖 $BC,AD,\theta$，与 $AB,CD$ 各自多长无关** —— 这个"消干净"值得记住。

**结论二（V3）** —— 正四面体 $ABCD$ 中，以外接球心（= 重心）$O$ 为终点：

$$\vec{AO}=\frac{\vec{AB}+\vec{AC}+\vec{AD}}4$$

因为以 $A$ 为原点时，重心 $=\frac{\vec 0+\vec B+\vec C+\vec D}4=\frac{\vec{AB}+\vec{AC}+\vec{AD}}4$。

## 验算

| 题 | 计算 | 答案 |
|---|---|---|
| 294-V1 | $R^{2}=\frac44+\frac{16-4}{4\cdot3/4}=1+4=5$，$S=20\pi$ | **D** |
| 294-V2 | $AB\perp BD$、$AC\perp CD$，$AD$ 中点即球心，$r=\sqrt3$，$S=12\pi$ | **$12\pi$** |
| 298-V3 | 外心 = 重心，$x=y=z=\frac14$，和 $=\frac34$ | **A** |
"""

T294_V1 = {
    'type': '选择',
    'stem_text': (
        r"四面体 $ABCD$ 中，$\angle ABC=\angle BCD=90^\circ$，$AD=4$，$BC=2$，"
        r"且 $AB$ 与 $CD$ 所成角为 $60^\circ$，则该四面体的外接球表面积为（　　）"
    ),
    'opts': [
        ('A', r"$10\pi$"),
        ('B', r"$16\pi$"),
        ('C', r"$18\pi$"),
        ('D', r"$20\pi$"),
    ],
    'answer': 'D',
    'analysis': (
        r"$BC\perp AB$ 且 $BC\perp CD$ ⟹ 取 $BC$ 为轴，把 $A,D$ 分别放在两个垂直于 $BC$ 的平面内。"
        r"设 $\lvert AB\rvert=p$、$\lvert CD\rvert=q$，建系后用「四顶点等距」解出球心，"
        r"会发现 $R^{2}$ 只依赖 $BC,AD,\theta$，与 $p,q$ 无关。"
    ),
    'solution': (
        r"**第一步：建系**" "\n"
        r"由 $\angle ABC=90^\circ$ 得 $AB\perp BC$；由 $\angle BCD=90^\circ$ 得 $CD\perp BC$．" "\n"
        r"取 $B(0,0,0)$、$C(2,0,0)$（$BC$ 沿 $x$ 轴，$\lvert BC\rvert=2$）．" "\n"
        r"由 $AB\perp BC$ 可设 $A(0,p,0)$（$\lvert AB\rvert=p$）；" "\n"
        r"由 $CD\perp BC$ 且 $CD$ 与 $AB$ 夹角为 $60^\circ$，设 $D\left(2,\ q\cos60^\circ,\ q\sin60^\circ\right)$"
        r"$=\left(2,\dfrac q2,\dfrac{q\sqrt3}2\right)$（$\lvert CD\rvert=q$）．" "\n"
        r"**第二步：用 $AD=4$ 建立关系**" "\n"
        r"$\lvert AD\rvert^{2}=4+\left(\dfrac q2-p\right)^{2}+\dfrac{3q^{2}}4=4+p^{2}+q^{2}-pq=16$" "\n"
        r"$\Rightarrow p^{2}+q^{2}-pq=12$　……（*）" "\n"
        r"**第三步：求球心**" "\n"
        r"设球心 $O(1,y,z)$（到 $B,C$ 等距 ⟹ $x=1$）．" "\n"
        r"$\lvert OB\rvert^{2}=1+y^{2}+z^{2}$；$\lvert OA\rvert^{2}=1+(y-p)^{2}+z^{2}$" "\n"
        r"相等 ⟹ $y=\dfrac p2$．" "\n"
        r"$\lvert OD\rvert^{2}=1+\left(\dfrac p2-\dfrac q2\right)^{2}+\left(z-\dfrac{q\sqrt3}2\right)^{2}$"
        r"$=1+\dfrac{(p-q)^{2}}4+z^{2}-zq\sqrt3+\dfrac{3q^{2}}4$" "\n"
        r"令 $\lvert OD\rvert^{2}=\lvert OB\rvert^{2}=1+\dfrac{p^{2}}4+z^{2}$：" "\n"
        r"$\dfrac{(p-q)^{2}}4-zq\sqrt3+\dfrac{3q^{2}}4=\dfrac{p^{2}}4$"
        r"$\Rightarrow zq\sqrt3=q^{2}-\dfrac{pq}2\Rightarrow z=\dfrac{q-\frac p2}{\sqrt3}$．" "\n"
        r"**第四步：算 $R^{2}$（关键：$p,q$ 会消掉）**" "\n"
        r"$R^{2}=1+\dfrac{p^{2}}4+z^{2}=1+\dfrac{p^{2}}4+\dfrac{q^{2}-pq+\frac{p^{2}}4}{3}$"
        r"$=1+\dfrac{p^{2}}3+\dfrac{q^{2}-pq}{3}=1+\dfrac{p^{2}+q^{2}-pq}{3}$" "\n"
        r"代入（*）：$R^{2}=1+\dfrac{12}3=5$．" "\n"
        r"**第五步**：$S=4\pi R^{2}=20\pi$．选 D．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**详解未提取到**，上述推导为我独立完成）。" "\n"
        r"**独立验算**：" "\n"
        r"① **取 $p=q$ 特例**（由（*）：$2p^{2}-p^{2}=12$ → $p=2\sqrt3\approx3.464$）：" "\n"
        r"$A(0,3.464,0)$、$D(2,1.732,3.0)$、$B(0,0,0)$、$C(2,0,0)$" "\n"
        r"验 $\lvert AD\rvert^{2}=4+(1.732-3.464)^{2}+9=4+2.999+9=15.999\approx16$ ✓✓" "\n"
        r"验 $AB$ 与 $CD$ 夹角：$\vec{AB}=(0,-3.464,0)$ 方向 $(0,-1,0)$；$\vec{CD}=(0,1.732,3)$，" "\n"
        r"$\cos=\frac{-1.732}{\sqrt{3+9}}=\frac{-1.732}{3.464}=-0.5$ → 夹角 $60^\circ$ ✓✓" "\n"
        r"球心：$y=p/2=1.732$，$z=\frac{q-p/2}{\sqrt3}=\frac{3.464-1.732}{1.732}=1.0$ → $O(1,1.732,1)$" "\n"
        r"$\lvert OB\rvert^{2}=1+3+1=5$ ✓；$\lvert OA\rvert^{2}=1+(1.732-3.464)^{2}+1=1+3+1=5$ ✓" "\n"
        r"$\lvert OC\rvert^{2}=1+3+1=5$ ✓；$\lvert OD\rvert^{2}=1+(1.732-1.732)^{2}+(1-3)^{2}=1+0+4=5$ ✓✓✓✓" "\n"
        r"$R^{2}=5$，$S=4\pi\times5=20\pi$ ✓✓" "\n"
        r"② **换 $p=2$ 复核**（由（*）：$4+q^{2}-2q=12$ → $q^{2}-2q-8=0$ → $q=4$）：" "\n"
        r"$A(0,2,0)$、$D(2,2,2\sqrt3)=(2,2,3.464)$" "\n"
        r"验 $\lvert AD\rvert^{2}=4+0+12=16$ ✓✓" "\n"
        r"$y=1$，$z=\frac{4-1}{\sqrt3}=\frac3{1.732}=1.732$ → $O(1,1,1.732)$" "\n"
        r"$\lvert OB\rvert^{2}=1+1+3=5$ ✓；$\lvert OA\rvert^{2}=1+1+3=5$ ✓" "\n"
        r"$\lvert OC\rvert^{2}=1+1+3=5$ ✓；$\lvert OD\rvert^{2}=1+(2-1)^{2}+(3.464-1.732)^{2}=1+1+3=5$ ✓✓✓✓" "\n"
        r"$R^{2}=5$ ✓✓ **与 $p=q$ 时完全相同**" "\n"
        r"**答案 D（$20\pi$）正确** ✓（两组不同的 $(p,q)$ 都得到 $R^{2}=5$）" "\n"
        r"**⭐ 通法（通用公式）**：$BC\perp AB$、$BC\perp CD$、对棱 $AB$ 与 $CD$ 夹角 $\theta$ 时，" "\n"
        r"$$R^{2}=\\frac{BC^{2}}4+\\frac{AD^{2}-BC^{2}}{4\\sin^{2}\\theta}$$" "\n"
        r"本题 $BC=2,AD=4,\theta=60^\circ$：$R^{2}=1+\frac{16-4}{4\cdot\frac34}=1+\frac{12}3=5$ ✓" "\n"
        r"**$R$ 与 $AB,CD$ 的长度无关**，这正是题目敢只给 $AD,BC,\theta$ 而不给 $AB,CD$ 的原因。" "\n"
        r"（**$\theta=90^\circ$ 时**退化为 $R^{2}=\frac{BC^{2}}4+\frac{AD^{2}-BC^{2}}4=\frac{AD^{2}}4$，"
        r"即 $AD$ 为直径 —— 与「对棱垂直」的直觉一致。）"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-294'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-294-V1',
}

T294_V2 = {
    'type': '填空',
    'stem_text': (
        r"四面体 $ABCD$ 中，$\angle ABC=\angle BCD=90^\circ$，$AB=BC=CD=2$，$AD=2\sqrt3$，"
        r"则该四面体的外接球表面积为 ____．"
    ),
    'opts': [],
    'answer': r"$12\pi$",
    'analysis': (
        r"两个直角 ⟹ 用勾股算出 $AC,BD$，再验证 $AB\perp BD$、$AC\perp CD$ ⟹ "
        r"$\triangle ABD$ 与 $\triangle ACD$ 都是直角三角形且**共斜边 $AD$** ⟹ "
        r"$AD$ 的中点就是外接球心。"
    ),
    'solution': (
        r"**第一步：算两条未知的面对角线**" "\n"
        r"$\angle ABC=90^\circ$、$AB=BC=2$ ⟹ $AC=\sqrt{4+4}=2\sqrt2$；" "\n"
        r"$\angle BCD=90^\circ$、$BC=CD=2$ ⟹ $BD=\sqrt{4+4}=2\sqrt2$．" "\n"
        r"**第二步：验证两个直角三角形**（关键一步）" "\n"
        r"$AB^{2}+BD^{2}=4+8=12=(2\sqrt3)^{2}=AD^{2}\Rightarrow AB\perp BD$；" "\n"
        r"$AC^{2}+CD^{2}=8+4=12=AD^{2}\Rightarrow AC\perp CD$．" "\n"
        r"**第三步：定球心**" "\n"
        r"$\triangle ABD$ 是直角三角形（斜边 $AD$）⟹ 斜边中点 $O$ 到 $A,B,D$ 等距；" "\n"
        r"$\triangle ACD$ 是直角三角形（斜边 $AD$）⟹ 同一点 $O$ 到 $A,C,D$ 等距．" "\n"
        r"故 $O$ 到 $A,B,C,D$ 四顶点等距，即 $O$ 为外接球球心，且 $AD$ 为球的直径．" "\n"
        r"**第四步**：$R=\dfrac{AD}2=\sqrt3$，$S=4\pi R^{2}=4\pi\times3=12\pi$．"
    ),
    'review': (
        r"★ 题干、答案、详解**全部完整** ✓。由详解「由题意 $\angle ABC=\angle BCD=90^\circ$，"
        r"$AB=BC=CD=2$，$AD=2\sqrt3$，则 $AC=BD=2\sqrt2$，所以 $AB^{2}+BD^{2}=AD^{2}$，$AB\perp BD$，"
        r"同理 $AC\perp CD$，取 $AD$ 中点 $O$，则 $O$ 到 $A,B,C,D$ 四点的距离相等，$O$ 即为 $ABCD$ 外接球的球心，"
        r"所以球半径为 $r=\frac{AD}2=\sqrt3$，球表面积为 $S=4\pi r^{2}=12\pi$」还原，"
        r"与我的推导**逐字一致** ✓。" "\n"
        r"**独立验算**（建系）：" "\n"
        r"① $B(0,0,0)$、$C(2,0,0)$、$A(0,2,0)$（$AB\perp BC$、$AB=BC=2$）" "\n"
        r"$D$ 满足 $CD=2$、$CD\perp BC$、$BD=2\sqrt2$：$D(2,y,z)$ 且 $y^{2}+z^{2}=4$、" "\n"
        r"$(2)^{2}+y^{2}+z^{2}=8$ → $4+4=8$ ✓ 自动满足，取 $D(2,2,0)$？则 $z=0$，$\lvert CD\rvert=2$ ✓" "\n"
        r"但此时 $A(0,2,0)$、$D(2,2,0)$，四点共面（退化为平面图形）✗ —— 需 $D$ 不在底面内。" "\n"
        r"重取：由 $AD=2\sqrt3$，$\lvert AD\rvert^{2}=4+(y-2)^{2}+z^{2}=12$，结合 $y^{2}+z^{2}=4$：" "\n"
        r"$4+y^{2}-4y+4+z^{2}=12$ → $8+4-4y=12$ → $4y=0$ → $y=0$，$z^{2}=4$ → $z=\pm2$" "\n"
        r"取 $D(2,0,2)$：" "\n"
        r"② 验 $\lvert CD\rvert=\sqrt{0+0+4}=2$ ✓；$\lvert BD\rvert=\sqrt{4+0+4}=2\sqrt2$ ✓" "\n"
        r"$\lvert AD\rvert=\sqrt{4+4+4}=\sqrt{12}=2\sqrt3$ ✓✓ **全部吻合**" "\n"
        r"③ 验 $CD\perp BC$：$\vec{CB}=(-2,0,0)$、$\vec{CD}=(0,0,2)$，点积 $=0$ ✓✓" "\n"
        r"④ 验 $AB\perp BD$：$\vec{BA}=(0,2,0)$、$\vec{BD}=(2,0,2)$，点积 $=0$ ✓✓" "\n"
        r"验 $AC\perp CD$：$\vec{CA}=(-2,2,0)$、$\vec{CD}=(0,0,2)$，点积 $=0$ ✓✓" "\n"
        r"⑤ 球心 $O=AD$ 中点 $=\left(\frac{0+2}2,\frac{2+0}2,\frac{0+2}2\right)=(1,1,1)$" "\n"
        r"$\lvert OA\rvert^{2}=1+1+1=3$；$\lvert OB\rvert^{2}=1+1+1=3$ ✓" "\n"
        r"$\lvert OC\rvert^{2}=(2-1)^{2}+1+1=3$ ✓；$\lvert OD\rvert^{2}=1+1+1=3$ ✓✓✓✓ **四顶点等距**" "\n"
        r"$R^{2}=3$，$S=4\pi\times3=12\pi$ ✓✓" "\n"
        r"**答案 $12\pi$ 正确** ✓" "\n"
        r"**⭐ 通法**：「**两个直角三角形共斜边**」是外接球最容易的模型之一 —— " "\n"
        r"若 $\triangle ABD$ 与 $\triangle ACD$ 都是直角三角形且斜边同为 $AD$，"
        r"则 $AD$ 的中点到 $A,B,C,D$ 四点等距 ⟹ **$AD$ 就是球的直径**，$R=\frac{AD}2$。" "\n"
        r"解题关键是**主动去验证**那两个直角（用勾股逆定理），"
        r"本题的两个直角 $AB\perp BD$、$AC\perp CD$ 都是这样「算」出来的，而非题设直接给出。"
    ),
    'difficulty': 0.87,
    'topics': ['M-T-294'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-294-V2',
}

T298_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知正四面体 $ABCD$ 的棱长为 $1$，$O$ 是该正四面体外接球球心，"
        r"且 $\vec{AO}=x\vec{AB}+y\vec{AC}+z\vec{AD}$，$x,y,z\in\mathbb R$，"
        r"则 $x+y+z=$（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac34$"),
        ('B', r"$\dfrac13$"),
        ('C', r"$\dfrac12$"),
        ('D', r"$\dfrac14$"),
    ],
    'answer': 'A',
    'analysis': (
        r"正四面体的**外心 = 重心 = 内心**（所有中心重合）。"
        r"以 $A$ 为原点写出重心的位置向量，与 $\vec{AO}=x\vec{AB}+y\vec{AC}+z\vec{AD}$ 对比即可。"
    ),
    'solution': (
        r"**关键：正四面体的中心重合**" "\n"
        r"正四面体 $ABCD$ 的外接球球心 $O$ 与重心重合（正四面体中外心、重心、内心、垂心四心合一）．" "\n"
        r"**用重心公式**" "\n"
        r"以 $A$ 为原点，记 $B,C,D$ 的位置向量为 $\vec b,\vec c,\vec d$，"
        r"则 $\vec{AB}=\vec b$、$\vec{AC}=\vec c$、$\vec{AD}=\vec d$．" "\n"
        r"重心（四个顶点 $A,B,C,D$ 即 $\vec 0,\vec b,\vec c,\vec d$ 的平均）：" "\n"
        r"$\vec{AO}=\dfrac{\vec 0+\vec b+\vec c+\vec d}4=\dfrac{\vec{AB}+\vec{AC}+\vec{AD}}4$．" "\n"
        r"与 $\vec{AO}=x\vec{AB}+y\vec{AC}+z\vec{AD}$ 对比：" "\n"
        r"由 $\vec{AB},\vec{AC},\vec{AD}$ 不共面（线性无关），得 $x=y=z=\dfrac14$．" "\n"
        r"$x+y+z=\dfrac34$．选 A．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**详解未提取到**，上述推导为我独立完成）。" "\n"
        r"**⚠ 需说明**：棱长 $=1$ 这个条件**实际没用上** —— "
        r"因为重心的向量表示只依赖「四个顶点」这件事，与棱长无关。"
        r"（棱长给 $1$ 是命题习惯，也可能是为了让 $\vec{AO}$ 的长度可算："
        r"$\lvert\vec{AO}\rvert=\frac{\sqrt6}4$，即正四面体外接球半径 $R=\frac{\sqrt6}4 a$。）" "\n"
        r"**独立验算（建系硬算，验证外心确实等于重心）**：" "\n"
        r"取 $A(0,0,0)$、$B(1,0,0)$、$C\left(\frac12,\frac{\sqrt3}2,0\right)$、"
        r"$D\left(\frac12,\frac{\sqrt3}6,\frac{\sqrt6}3\right)$（棱长均为 $1$ 的正四面体）" "\n"
        r"① 重心 $G=\frac{A+B+C+D}4=\left(\frac{1+\frac12+\frac12}4,\frac{0+\frac{\sqrt3}2+\frac{\sqrt3}6}4,"
        r"\frac{0+0+\frac{\sqrt6}3}4\right)=\left(\frac12,\frac{\sqrt3}6,\frac{\sqrt6}{12}\right)$" "\n"
        r"② 验 $G$ 到四顶点等距：" "\n"
        r"$\lvert GA\rvert^{2}=\frac14+\frac3{36}+\frac6{144}=\frac14+\frac1{12}+\frac1{24}$"
        r"$=\frac{6+2+1}{24}=\frac9{24}=\frac38$" "\n"
        r"$\lvert GB\rvert^{2}=\left(1-\frac12\right)^{2}+\frac3{36}+\frac6{144}$"
        r"$=\frac14+\frac1{12}+\frac1{24}=\frac38$ ✓" "\n"
        r"$\lvert GC\rvert^{2}=\left(\frac12-\frac12\right)^{2}+\left(\frac{\sqrt3}2-\frac{\sqrt3}6\right)^{2}+\frac6{144}$"
        r"$=0+\left(\frac{\sqrt3}3\right)^{2}+\frac1{24}=\frac13+\frac1{24}=\frac{8+1}{24}=\frac38$ ✓" "\n"
        r"$\lvert GD\rvert^{2}=0+\left(\frac{\sqrt3}6-\frac{\sqrt3}6\right)^{2}+\left(\frac{\sqrt6}3-\frac{\sqrt6}{12}\right)^{2}$"
        r"$=\left(\frac{3\sqrt6}{12}\right)^{2}=\left(\frac{\sqrt6}4\right)^{2}=\frac6{16}=\frac38$ ✓✓✓✓" "\n"
        r"**四顶点等距，故重心 $G$ 就是外心 $O$** ✓✓" "\n"
        r"③ 验 $\vec{AO}=x\vec{AB}+y\vec{AC}+z\vec{AD}$ 中 $x=y=z=\frac14$：" "\n"
        r"$\frac14(\vec{AB}+\vec{AC}+\vec{AD})$"
        r"$=\frac14\left[(1,0,0)+\left(\frac12,\frac{\sqrt3}2,0\right)+\left(\frac12,\frac{\sqrt3}6,\frac{\sqrt6}3\right)\right]$" "\n"
        r"$=\frac14\left(2,\frac{2\sqrt3}3,\frac{\sqrt6}3\right)$"
        r"$=\left(\frac12,\frac{\sqrt3}6,\frac{\sqrt6}{12}\right)=\vec{AG}$ ✓✓" "\n"
        r"④ $x+y+z=\frac14+\frac14+\frac14=\frac34$ ✓✓" "\n"
        r"⑤ **顺带**：外接球半径 $R=\lvert AO\rvert=\sqrt{\frac38}=\frac{\sqrt6}4\approx0.6124$ ✓"
        r"（与正四面体 $R=\frac{\sqrt6}4a$ 的公式一致，$a=1$）" "\n"
        r"**答案 A（$\frac34$）正确** ✓" "\n"
        r"**⭐ 通法**：" "\n"
        r"① **正四面体四心合一**（外心 = 重心 = 内心 = 垂心）—— 这是解这类题的钥匙。" "\n"
        r"② 一般地，$n$ 个点的重心位置向量 $=\frac{1}n\sum\vec{P_i}$。对四面体（$n=4$），"
        r"以某顶点为原点时 $\vec{AO}=\frac{\vec{AB}+\vec{AC}+\vec{AD}}4$ —— "
        r"**系数分母就是顶点个数 $4$**。" "\n"
        r"③ 遇到「$\vec{AO}=x\vec{AB}+y\vec{AC}+z\vec{AD}$ 求 $x+y+z$」，"
        r"若 $O$ 是**重心**则 $x=y=z=\frac14$、和为 $\frac34$；"
        r"这类题本质是考「重心的向量表示」，不必算任何长度。"
    ),
    'difficulty': 0.86,
    'topics': ['M-T-298'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-298-V3',
}

QS = [T294_V1, T294_V2, T298_V3]
