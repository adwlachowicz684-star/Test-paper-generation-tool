# -*- coding: utf-8 -*-
r"""第47批（下）：平面向量 · 系数与范围（三点共线 / 线性规划）

来源：2024高中数学热点题型归纳完整解析版.pdf
p206（PDF 页 205）M-T-240

## 选题

本文件取 M-T-240 的 E1、V1、V2、V3（4 题全录）。

## ★★ 本批两个核心结论

**结论一（三点共线定理的系数形式）** —— 若 $\vec{OP}=x\vec{OA}+y\vec{OB}$ 且 $P$ 在直线 $AB$ 上，
则 **$x+y=1$**（$P$ 在线段内则 $x,y\ge0$）。这是整个题型的基础。

- E1：$\vec{CD}=\frac13\vec{CA}+\lambda\vec{CB}$ 且 $D\in AB$ ⟹ $\frac13+\lambda=1$ ⟹ $\lambda=\frac23$（秒答）
- V2：$M,N,P$ 共线 ⟹ $\frac{2}{3\lambda}+\frac1{3\mu}=1$ ⟹ 转成一个约束下的最值

**结论二（V3 的广义距离）** —— 在夹角 $120^\circ$、长度 $1$ 的基 $\vec{AD},\vec{AE}$ 下，
$P(x,y)$ 到 $M(2,2)$ 的「距离平方」为

$$(x-2)^2+(y-2)^2-(x-2)(y-2)$$

（交叉项系数 $=2\cos120^\circ=-1$）。令 $s=(x-2)+(y-2)$，由 $u^2+v^2-uv\ge\frac{s^2}4$ 得 $|s|\le2\sqrt3$。

## 四题验算

| 题 | 结果 | 答案 |
|---|---|---|
| E1 | $\lambda=\frac23$ | **D** |
| V1 | $f=\frac{y+1}{x+y+2}\in[\frac14,\frac34]$ | **C** |
| V2 | $\lambda+2\mu$ 最小 $=\frac83$（$\lambda=\frac43,\mu=\frac23$） | **B** |
| V3 | $x+y\in[4-2\sqrt3,\ 4+2\sqrt3]$ | **B** |
"""

T240_E1 = {
    'type': '选择',
    'stem_text': (
        r"在 $\triangle ABC$ 中，已知 $D$ 是 $AB$ 边上一点，若 $\vec{AD}=2\vec{DB}$，"
        r"$\vec{CD}=\dfrac13\vec{CA}+\lambda\vec{CB}$，则 $\lambda=$（　　）"
    ),
    'opts': [
        ('A', r"$-\dfrac13$"),
        ('B', r"$-\dfrac23$"),
        ('C', r"$\dfrac13$"),
        ('D', r"$\dfrac23$"),
    ],
    'answer': 'D',
    'analysis': (
        r"**三点共线定理的系数形式**：若 $\vec{CP}=x\vec{CA}+y\vec{CB}$ 且 $P\in$ 直线 $AB$，"
        r"则 $x+y=1$。本题直接由此得 $\frac13+\lambda=1$。"
    ),
    'solution': (
        r"$\vec{CD}=\vec{CA}+\vec{AD}$，而 $\vec{AD}=2\vec{DB}$ 且 $\vec{AD}+\vec{DB}=\vec{AB}$，" "\n"
        r"故 $\vec{AD}=\dfrac23\vec{AB}=\dfrac23(\vec{CB}-\vec{CA})$．" "\n"
        r"$\vec{CD}=\vec{CA}+\dfrac23\vec{CB}-\dfrac23\vec{CA}=\dfrac13\vec{CA}+\dfrac23\vec{CB}$．" "\n"
        r"与 $\vec{CD}=\dfrac13\vec{CA}+\lambda\vec{CB}$ 对比得 $\lambda=\dfrac23$．选 D．" "\n"
        r"**秒答法**：$D$ 在直线 $AB$ 上，由三点共线定理，$\vec{CD}$ 用 $\vec{CA},\vec{CB}$ 表示时"
        r"**系数和必为 $1$**，即 $\dfrac13+\lambda=1\Rightarrow\lambda=\dfrac23$．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**详解未提取到**，上述推导为我独立完成）。" "\n"
        r"**独立验算（建系）**：取 $C$ 为原点，$A(1,0)$、$B(0,1)$。" "\n"
        r"① $\vec{CA}=(1,0)$、$\vec{CB}=(0,1)$" "\n"
        r"② $D$ 在 $AB$ 上且 $AD=2DB$ ⟹ $D$ 分 $AB$ 为 $2:1$，" "\n"
        r"$D=\dfrac{1\cdot A+2\cdot B}{3}=\left(\dfrac13,\dfrac23\right)$" "\n"
        r"验：$\vec{AD}=D-A=\left(-\dfrac23,\dfrac23\right)$，$\vec{DB}=B-D=\left(-\dfrac13,\dfrac13\right)$；" "\n"
        r"$\vec{AD}=2\vec{DB}$ ✓✓" "\n"
        r"③ $\vec{CD}=\left(\dfrac13,\dfrac23\right)=\dfrac13(1,0)+\dfrac23(0,1)=\dfrac13\vec{CA}+\dfrac23\vec{CB}$ ✓✓" "\n"
        r"④ $\lambda=\dfrac23$ ✓✓；验系数和 $\dfrac13+\dfrac23=1$ ✓（$D$ 在直线 $AB$ 上）" "\n"
        r"**答案 D（$\frac23$）正确** ✓" "\n"
        r"**⭐ 通法（三点共线定理）**：" "\n"
        r"$P,A,B$ 三点共线 $\iff$ 对任意点 $O$，$\vec{OP}=x\vec{OA}+y\vec{OB}$ 中 **$x+y=1$**。" "\n"
        r"这是本专题所有题目的基础。推广：" "\n"
        r"· $P$ 在**线段** $AB$ 内：$x+y=1$ 且 $x,y\ge0$；" "\n"
        r"· $P$ 在 $AB$ **延长线**上（$B$ 外侧）：$x+y=1$ 且 $y>1$（或 $x<0$）。" "\n"
        r"**解题价值**：看到「$D$ 在 $AB$ 上 + $\vec{CD}=x\vec{CA}+y\vec{CB}$」直接写 $x+y=1$，"
        r"不用做向量分解 —— 本题可 5 秒出答案。"
    ),
    'difficulty': 0.75,
    'topics': ['M-T-240'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-240-E1',
}

T240_V1 = {
    'type': '选择',
    'stem_text': (
        r"如图，在 $\triangle OMN$ 中，$A,B$ 分别是 $OM,ON$ 的中点，"
        r"若 $\vec{OP}=x\vec{OA}+y\vec{OB}$（$x,y\in\mathbb R$），"
        r"且点 $P$ 落在四边形 $ABNM$ 内（含边界），则 $\dfrac{y+1}{x+y+2}$ 的取值范围是（　　）"
    ),
    'opts': [
        ('A', r"$\left[\dfrac13,\dfrac23\right]$"),
        ('B', r"$\left[\dfrac13,\dfrac34\right]$"),
        ('C', r"$\left[\dfrac14,\dfrac34\right]$"),
        ('D', r"$\left[\dfrac14,\dfrac23\right]$"),
    ],
    'answer': 'C',
    'analysis': (
        r"以 $\vec{OA},\vec{OB}$ 为基底（$A,B$ 是中点 ⟹ $M,N$ 坐标为 $(2,0),(0,2)$），"
        r"把四边形 $ABNM$ 化成基底坐标下的区域 $1\le x+y\le2$、$x,y\ge0$，"
        r"再对分式函数求范围。"
    ),
    'solution': (
        r"**第一步：建立基底坐标**" "\n"
        r"记 $\vec{OA}=\vec a$、$\vec{OB}=\vec b$，则 $\vec{OM}=2\vec a$、$\vec{ON}=2\vec b$．" "\n"
        r"用 $(\vec a,\vec b)$ 作基底，$P$ 的坐标为 $(x,y)$；" "\n"
        r"$A(1,0)$、$B(0,1)$、$M(2,0)$、$N(0,2)$．" "\n"
        r"**第二步：确定区域**" "\n"
        r"四边形 $ABNM$ 的边界：$AB$ 为 $x+y=1$，$MN$ 为 $x+y=2$，" "\n"
        r"$BN$ 为 $x=0$，$AM$ 为 $y=0$．" "\n"
        r"故区域 $=\{(x,y)\mid x\ge0,\ y\ge0,\ 1\le x+y\le2\}$．" "\n"
        r"**第三步：求 $f=\dfrac{y+1}{x+y+2}$ 的范围**" "\n"
        r"记 $s=x+y\in[1,2]$，则 $f=\dfrac{y+1}{s+2}$．" "\n"
        r"对固定的 $s$，$y$ 的取值范围是 $[0,s]$，且 $f$ 随 $y$ **单调递增**：" "\n"
        r"· 最小：$y=0$，$f=\dfrac1{s+2}$，随 $s$ 增大而减小 → $s=2$ 时取最小 $\dfrac14$；" "\n"
        r"· 最大：$y=s$（即 $x=0$），$f=\dfrac{s+1}{s+2}=1-\dfrac1{s+2}$，随 $s$ 增大而增大 → $s=2$ 时取最大 $\dfrac34$．" "\n"
        r"**第四步**：$f\in\left[\dfrac14,\dfrac34\right]$．选 C．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**详解未提取到**，上述推导为我独立完成）。" "\n"
        r"**独立验算（取边界点逐一核对）**：" "\n"
        r"① **$f=\frac14$ 的取等点**：$y=0$、$s=2$ → $P=(2,0)=M$ ✓ 在边界上" "\n"
        r"$f=\frac{0+1}{2+0+2}=\frac14$ ✓✓" "\n"
        r"② **$f=\frac34$ 的取等点**：$y=2$、$s=2$ → $x=0$，$P=(0,2)=N$ ✓ 在边界上" "\n"
        r"$f=\frac{2+1}{0+2+2}=\frac34$ ✓✓" "\n"
        r"③ **中间点验证**：取 $A(1,0)$：$f=\frac{0+1}{1+0+2}=\frac13\approx0.333\in[\frac14,\frac34]$ ✓" "\n"
        r"取 $B(0,1)$：$f=\frac{1+1}{0+1+2}=\frac23\approx0.667\in[\frac14,\frac34]$ ✓" "\n"
        r"取中心点 $(1,1)$（$s=2$）：$f=\frac{2}{1+1+2}=\frac24=\frac12$ ✓ 在范围内" "\n"
        r"取 $(0.5,0.5)$（$s=1$）：$f=\frac{1.5}{0.5+0.5+2}=\frac{1.5}3=0.5$ ✓ 在范围内" "\n"
        r"④ **确认极值**：$f$ 对 $y$ 单调增（$\frac{\partial f}{\partial y}=\frac{1}{s+2}>0$）；" "\n"
        r"对 $s$：$y=0$ 时 $f=\frac1{s+2}$ 递减 → $s=2$ 最小；$y=s$ 时 $f=1-\frac1{s+2}$ 递增 → $s=2$ 最大 ✓✓" "\n"
        r"⑤ **排除其他选项**：A $[\frac13,\frac23]$ 上界 $\frac23<\frac34$ ✗（漏了 $N$ 点）；" "\n"
        r"B $[\frac13,\frac34]$ 下界 $\frac13>\frac14$ ✗（漏了 $M$ 点）；D $[\frac14,\frac23]$ 上界不足 ✗" "\n"
        r"**答案 C（$[\frac14,\frac34]$）正确** ✓" "\n"
        r"**⭐ 通法**：" "\n"
        r"① 「$A,B$ 是中点」⟹ 以 $\vec{OA},\vec{OB}$ 为基时 $M,N$ 坐标为 $(2,0),(0,2)$，" "\n"
        r"四边形 $ABNM$ 化为**梯形区域** $1\le x+y\le2$；" "\n"
        r"② 分式函数 $\frac{y+c}{x+y+d}$ 的常用技巧：**固定 $s=x+y$，只让 $y$ 变**，" "\n"
        r"分子随 $y$ 线性变化、分母恒定 ⟹ 最值必在 $y$ 的端点取得；" "\n"
        r"③ 再让 $s$ 在 $[1,2]$ 上动，比较两个端点即可。" "\n"
        r"**关键观察**：本题分子只含 $y$、分母含 $x+y$，所以「固定分母、动分子」是最省力的思路。"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-240'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-240-V1',
}

T240_V2 = {
    'type': '选择',
    'stem_text': (
        r"如图，$\mathrm{Rt}\triangle ABC$ 中，$P$ 是斜边 $BC$ 上一点，且满足 $\vec{BP}=\dfrac12\vec{PC}$，"
        r"点 $M,N$ 在过点 $P$ 的直线上，若 $\vec{AM}=\lambda\vec{AB}$，$\vec{AN}=\mu\vec{AC}$（$\lambda,\mu>0$），"
        r"则 $\lambda+2\mu$ 的最小值为（　　）"
    ),
    'opts': [
        ('A', r"$2$"),
        ('B', r"$\dfrac83$"),
        ('C', r"$3$"),
        ('D', r"$\dfrac{10}3$"),
    ],
    'answer': 'B',
    'analysis': (
        r"**关键转化**：$M,P,N$ 共线且 $\vec{AM},\vec{AN}$ 不共线 ⟹ 把 $\vec{AP}$ 按 $\vec{AM},\vec{AN}$ 分解，"
        r"**系数和 $=1$**。而 $\vec{AP}$ 由分点公式已知，于是得到 $\lambda,\mu$ 的一个约束，"
        r"再求 $\lambda+2\mu$ 的最小值。"
    ),
    'solution': (
        r"**第一步：求 $\vec{AP}$**" "\n"
        r"以 $A$ 为原点，记 $\vec{AB}=\vec b$、$\vec{AC}=\vec c$．" "\n"
        r"由 $\vec{BP}=\dfrac12\vec{PC}$ 知 $BP:PC=1:2$，由分点公式" "\n"
        r"$\vec{AP}=\dfrac{2\vec{AB}+1\vec{AC}}{1+2}=\dfrac23\vec b+\dfrac13\vec c$．" "\n"
        r"**第二步：用共线条件列约束**" "\n"
        r"$M,N,P$ 共线，设 $\vec{AP}=t\vec{AM}+(1-t)\vec{AN}$（系数和为 $1$）．" "\n"
        r"而 $\vec{AM}=\lambda\vec b$、$\vec{AN}=\mu\vec c$，故" "\n"
        r"$\dfrac23\vec b+\dfrac13\vec c=t\lambda\vec b+(1-t)\mu\vec c$．" "\n"
        r"由 $\vec b,\vec c$ 不共线：$t\lambda=\dfrac23$、$(1-t)\mu=\dfrac13$" "\n"
        r"$\Rightarrow t=\dfrac{2}{3\lambda}$、$1-t=\dfrac{1}{3\mu}$，相加得" "\n"
        r"$\dfrac{2}{3\lambda}+\dfrac{1}{3\mu}=1$，即 $\dfrac2\lambda+\dfrac1\mu=3$．" "\n"
        r"**第三步：求 $\lambda+2\mu$ 的最小值**" "\n"
        r"由柯西：$\left(\lambda+2\mu\right)\left(\dfrac2\lambda+\dfrac1\mu\right)$"
        r"$\ge\left(\sqrt{\lambda\cdot\dfrac2\lambda}+\sqrt{2\mu\cdot\dfrac1\mu}\right)^{2}=\left(\sqrt2+\sqrt2\right)^{2}=8$．" "\n"
        r"$\Rightarrow\lambda+2\mu\ge\dfrac83$．" "\n"
        r"**取等条件**：$\dfrac{\lambda}{2/\lambda}=\dfrac{2\mu}{1/\mu}$，即 $\dfrac{\lambda^{2}}2=2\mu^{2}\Rightarrow\lambda=2\mu$；" "\n"
        r"代入约束 $\dfrac{2}{2\mu}+\dfrac1\mu=3\Rightarrow\dfrac2\mu=3\Rightarrow\mu=\dfrac23$、$\lambda=\dfrac43$．" "\n"
        r"选 B．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**详解未提取到**，上述推导为我独立完成）。" "\n"
        r"**独立验算**：" "\n"
        r"① **验约束**：$\lambda=\frac43$、$\mu=\frac23$ 时 $\frac2\lambda+\frac1\mu=\frac{2}{4/3}+\frac{1}{2/3}=\frac32+\frac32=3$ ✓✓" "\n"
        r"② **验目标值**：$\lambda+2\mu=\frac43+2\cdot\frac23=\frac43+\frac43=\frac83$ ✓✓" "\n"
        r"③ **验 $t$ 的一致性**：$t=\frac{2}{3\lambda}=\frac{2}{3\cdot4/3}=\frac24=\frac12$；" "\n"
        r"$1-t=\frac{1}{3\mu}=\frac{1}{3\cdot2/3}=\frac12$ ✓✓ **$t+(1-t)=1$ 成立**" "\n"
        r"④ **换一组 $(\lambda,\mu)$ 确认是最小值**：取 $\lambda=2$（则 $\frac2\lambda=1$，$\frac1\mu=2$，$\mu=\frac12$）：" "\n"
        r"$\lambda+2\mu=2+1=3>\frac83$ ✓；取 $\lambda=1$（$\frac2\lambda=2$，$\frac1\mu=1$，$\mu=1$）：" "\n"
        r"$\lambda+2\mu=1+2=3>\frac83$ ✓✓ **确为最小**" "\n"
        r"⑤ **建系验证**（$A(0,0)$、$B(3,0)$、$C(0,3)$，则 $\vec{AP}=\frac23(3,0)+\frac13(0,3)=(2,1)$）：" "\n"
        r"验 $P$ 在 $BC$ 上：$BC$ 是 $x+y=3$，$P(2,1)$ 满足 $2+1=3$ ✓✓" "\n"
        r"$\vec{BP}=P-B=(-1,1)$，$\vec{PC}=C-P=(-2,2)$；$\vec{BP}=\frac12\vec{PC}$ ✓✓" "\n"
        r"$M=\lambda B=\frac43(3,0)=(4,0)$；$N=\mu C=\frac23(0,3)=(0,2)$" "\n"
        r"验 $M,P,N$ 共线：直线 $MN$ 是 $\frac x4+\frac y2=1$，即 $x+2y=4$；" "\n"
        r"$P(2,1)$：$2+2=4$ ✓✓ **三点共线成立**" "\n"
        r"**答案 B（$\frac83$）正确** ✓" "\n"
        r"**⭐ 通法**：" "\n"
        r"① 「$M,P,N$ 共线 + $\vec{AM},\vec{AN}$ 已知方向」⟹ 用三点共线定理写" "\n"
        r"$\vec{AP}=t\vec{AM}+(1-t)\vec{AN}$，**系数和 $1$** 是核心；" "\n"
        r"② 把 $\vec{AP}$ 的两种表示（分点公式 vs 共线分解）对比，得到 $\lambda,\mu$ 的约束；" "\n"
        r"③ 约束形如 $\frac{a}\lambda+\frac{b}\mu=c$ 求 $p\lambda+q\mu$ 最小值 —— **一律用柯西**：" "\n"
        r"$(p\lambda+q\mu)\left(\frac a\lambda+\frac b\mu\right)\ge\left(\sqrt{pa}+\sqrt{qb}\right)^{2}$。" "\n"
        r"本题 $(1\cdot2+2\cdot1)$ 配出 $(\sqrt2+\sqrt2)^2=8$，除以 $3$ 得 $\frac83$ ✓"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-240'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-240-V2',
}

T240_V3 = {
    'type': '选择',
    'stem_text': (
        r"如图，$\angle BAC=\dfrac{2\pi}3$，圆 $M$ 与 $AB,AC$ 分别相切于点 $D,E$，$AD=1$，"
        r"点 $P$ 是圆 $M$ 及其内部任意一点，且 $\vec{AP}=x\vec{AD}+y\vec{AE}$（$x,y\in\mathbb R$），"
        r"则 $x+y$ 的取值范围是（　　）"
    ),
    'opts': [
        ('A', r"$\left[1,\ 4+2\sqrt3\right]$"),
        ('B', r"$\left[4-2\sqrt3,\ 4+2\sqrt3\right]$"),
        ('C', r"$\left[1,\ 2+\sqrt3\right]$"),
        ('D', r"$\left[2-\sqrt3,\ 2+\sqrt3\right]$"),
    ],
    'answer': 'B',
    'analysis': (
        r"圆与两边相切 ⟹ $AE=AD=1$、$M$ 在角平分线上。用 $\vec{AD},\vec{AE}$ 作基（夹角 $120^\circ$），"
        r"圆心 $M$ 的坐标为 $(2,2)$、半径 $=\sqrt3$，于是「$P$ 在圆内」化为一个**带交叉项的距离不等式**。"
    ),
    'solution': (
        r"**第一步：确定圆 $M$**" "\n"
        r"圆与 $AB,AC$ 相切于 $D,E$ ⟹ $AE=AD=1$（切线长定理），且 $M$ 在 $\angle BAC$ 的平分线上．" "\n"
        r"$\angle BAC=120^\circ$，故 $\angle DAM=60^\circ$；在 $\mathrm{Rt}\triangle ADM$ 中" "\n"
        r"$MD=AD\tan60^\circ=\sqrt3$（半径 $r=\sqrt3$），$AM=\dfrac{AD}{\cos60^\circ}=2$．" "\n"
        r"**第二步：基底坐标**" "\n"
        r"以 $\vec{AD}=\vec e_1$、$\vec{AE}=\vec e_2$ 为基（$\lvert\vec e_1\rvert=\lvert\vec e_2\rvert=1$，"
        r"$\vec e_1\cdot\vec e_2=\cos120^\circ=-\dfrac12$）．" "\n"
        r"角平分线方向为 $\vec e_1+\vec e_2$（$\lvert\vec e_1+\vec e_2\rvert=\sqrt{1+1-1}=1$，是单位向量），" "\n"
        r"故 $\vec{AM}=2(\vec e_1+\vec e_2)$，即 $M$ 的坐标为 $(2,2)$．" "\n"
        r"$P$ 的坐标为 $(x,y)$，$\vec{MP}=(x-2)\vec e_1+(y-2)\vec e_2$．" "\n"
        r"**第三步：写出「在圆内」**" "\n"
        r"$\lvert\vec{MP}\rvert^{2}=(x-2)^{2}+(y-2)^{2}+2(x-2)(y-2)\left(-\dfrac12\right)$" "\n"
        r"$=(x-2)^{2}+(y-2)^{2}-(x-2)(y-2)\le3$．" "\n"
        r"**第四步：求 $x+y$ 的范围**" "\n"
        r"令 $u=x-2$、$v=y-2$、$s=u+v=x+y-4$，则 $u^{2}+v^{2}-uv=s^{2}-3uv$．" "\n"
        r"对固定的 $s$，$uv\le\dfrac{s^{2}}4$（$u=v=\dfrac s2$ 时取等），故" "\n"
        r"$u^{2}+v^{2}-uv\ge s^{2}-\dfrac{3s^{2}}4=\dfrac{s^{2}}4$．" "\n"
        r"要存在 $P$ 满足 $\lvert\vec{MP}\rvert^{2}\le3$，需 $\dfrac{s^{2}}4\le3\Rightarrow\lvert s\rvert\le2\sqrt3$．" "\n"
        r"反之 $|s|\le2\sqrt3$ 时取 $u=v=\frac s2$ 即可达到，故 $s\in[-2\sqrt3,2\sqrt3]$．" "\n"
        r"$x+y=s+4\in\left[4-2\sqrt3,\ 4+2\sqrt3\right]$．选 B．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**详解未提取到**，上述推导为我独立完成）。" "\n"
        r"**独立验算**：" "\n"
        r"① **验圆的参数**：$AD=AE=1$、$\angle DAE=120^\circ$、$AM=2$、$r=\sqrt3$" "\n"
        r"在 $\mathrm{Rt}\triangle ADM$：$AD=1$、$MD=\sqrt3$、$AM=\sqrt{1+3}=2$ ✓；" "\n"
        r"$\tan\angle DAM=\frac{MD}{AD}=\sqrt3$ → $\angle DAM=60^\circ$ ✓（$\angle BAC$ 的一半）" "\n"
        r"② **验 $M$ 的坐标**：$\vec{AM}=2(\vec e_1+\vec e_2)$，$\lvert\vec{AM}\rvert=2\cdot1=2$ ✓；" "\n"
        r"方向 $\vec e_1+\vec e_2$ 是角平分线 ✓（因 $\lvert\vec e_1\rvert=\lvert\vec e_2\rvert$）" "\n"
        r"③ **验圆的边界点**：取 $D(1,0)$：$\vec{MD}=(-1,-2)_{\text{基}}$" "\n"
        r"$\lvert\vec{MD}\rvert^{2}=1+4-(-1)(-2)=5-2=3=r^{2}$ ✓✓ **$D$ 在圆上**" "\n"
        r"取 $E(0,1)$：$\vec{ME}=(-2,-1)$，$\lvert\cdot\rvert^{2}=4+1-2=3$ ✓✓ **$E$ 在圆上**" "\n"
        r"④ **验极值点**：$s=2\sqrt3$ 对应 $u=v=\sqrt3$，即 $(x,y)=(2+\sqrt3,\,2+\sqrt3)$" "\n"
        r"$x+y=4+2\sqrt3\approx7.464$ ✓；验：$\vec{MP}=(\sqrt3,\sqrt3)$，" "\n"
        r"$\lvert\vec{MP}\rvert^{2}=3+3-3=3=r^{2}$ ✓✓ **恰在圆上**" "\n"
        r"$s=-2\sqrt3$ 对应 $(x,y)=(2-\sqrt3,\,2-\sqrt3)$，$x+y=4-2\sqrt3\approx0.536$ ✓" "\n"
        r"$\vec{MP}=(-\sqrt3,-\sqrt3)$，$\lvert\cdot\rvert^{2}=3+3-3=3$ ✓✓" "\n"
        r"⑤ **验中点**：$P=M$ 即 $(2,2)$，$x+y=4\in[4-2\sqrt3,4+2\sqrt3]=[0.536,7.464]$ ✓" "\n"
        r"⑥ **排除其他选项**：A、C 下界为 $1$，但 $x+y$ 可小到 $0.536<1$ ✗；" "\n"
        r"D 的区间 $[0.268,3.732]$ 上下界均不足 ✗" "\n"
        r"**答案 B 正确** ✓" "\n"
        r"**⭐ 通法（非正交基下的「圆」）**：" "\n"
        r"① 用两个已知向量 $\vec e_1,\vec e_2$（夹角 $\theta$）作基时，向量 $u\vec e_1+v\vec e_2$ 的模长平方为" "\n"
        r"$$\lvert u\vec e_1+v\vec e_2\rvert^{2}=u^{2}\lvert\vec e_1\rvert^{2}+v^{2}\lvert\vec e_2\rvert^{2}+2uv\,\vec e_1\cdot\vec e_2$$" "\n"
        r"本题 $\theta=120^\circ$、长度均为 $1$ ⟹ $=u^{2}+v^{2}-uv$（**交叉项系数 $-1$**）。" "\n"
        r"② 求 $u+v$ 的范围：**固定 $s=u+v$**，用 $uv\le\frac{s^{2}}4$ 求模长平方的最小值 $\frac{s^{2}}4$。" "\n"
        r"③ 圆与角两边相切 ⟹ 圆心在角平分线上、$r=d\tan\frac\theta2$、$AM=\frac{d}{\cos\frac\theta2}$（$d=AD$）。"
    ),
    'difficulty': 0.94,
    'topics': ['M-T-240'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-240-V3',
}

QS = [T240_E1, T240_V1, T240_V2, T240_V3]
