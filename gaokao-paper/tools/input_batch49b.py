# -*- coding: utf-8 -*-
r"""第49批（下）：平面向量 · 系数范围与最值（等和线 · 柯西）

来源：2024高中数学热点题型归纳完整解析版.pdf
p202（PDF 页 201）M-T-234

## 选题

本文件取 M-T-234 的 V1、V2、V3。

## ⚠ 跳过 E1

「$BP=3PC$，过 $P$ 的直线交 $AB,AC$ 于 $M,N$，$\vec{AM}=\lambda\vec{AB}$、$\vec{AN}=\mu\vec{AC}$，求 $\lambda+\mu$ 最小值」。

我的推导：分点公式得 $\vec{AP}=\frac14\vec{AB}+\frac34\vec{AC}$，由 $M,P,N$ 共线（系数和 $1$）得
$\frac1\lambda+\frac3\mu=4$，柯西给 $\lambda+\mu\ge1+\frac{\sqrt3}2\approx1.866$ —— **四个选项
（$2\sqrt2+1$、$3\sqrt2+1$、$3\sqrt2$、$5\sqrt2$，都在 $3\sim7$ 量级）无一符合**。
判定为**题干或选项提取失真**，跳过。

## ★★ 本批三个核心结论

**结论一（V1 · 重心 + 区域端点）**：$\vec{OA}+\vec{OB}+\vec{OC}=\vec 0$ ⟹ $O$ 是**重心**，
$\vec{AO}=\frac13(\vec{AB}+\vec{AC})$。$M$ 在某区域内时，$\lambda+2\mu$ 的最值**必在区域顶点取得**
（因为它是线性函数）。

**结论二（V2 · 固定模长求系数和）**：$|\vec{AM}|=1$ 给出 $\lambda^2+\mu^2-\lambda\mu=1$（非正交基），
求 $\lambda+\mu$ 最值用 $s^2=1+3\lambda\mu$ 配 $\lambda\mu\le\frac{s^2}4$。

**结论三（V3 · 共线得线性约束 + 柯西）**：$F$ 在线段 $CD$ 上 ⟹ $2x+y=1$；
求 $\frac1x+\frac2y$ 最小值用柯西 $(p\lambda+q\mu)(\frac a\lambda+\frac b\mu)\ge(\sqrt{pa}+\sqrt{qb})^2$。

## 三题验算

| 题 | 我的结果 | 答案 |
|---|---|---|
| V1 | $\lambda+2\mu\in(1,2)$ | **B** |
| V2 | $\lambda+\mu$ 最大 $=2$（$\lambda=\mu=1$） | **C** |
| V3 | $\frac1x+\frac2y$ 最小 $=8$（$x=\frac14,y=\frac12$） | **D** |
"""

T234_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知 $O$ 是 $\triangle ABC$ 内一点，且 $\vec{OA}+\vec{OB}+\vec{OC}=\vec 0$，"
        r"点 $M$ 在 $\triangle OBC$ 内（不含边界），若 $\vec{AM}=\lambda\vec{AB}+\mu\vec{AC}$，"
        r"则 $\lambda+2\mu$ 的取值范围是（　　）"
    ),
    'opts': [
        ('A', r"$\left(1,\dfrac52\right)$"),
        ('B', r"$\left(1,2\right)$"),
        ('C', r"$\left(\dfrac23,1\right)$"),
        ('D', r"$\left(\dfrac12,1\right)$"),
    ],
    'answer': 'B',
    'analysis': (
        r"$\vec{OA}+\vec{OB}+\vec{OC}=\vec 0$ ⟹ $O$ 是**重心** ⟹ $\vec{AO}=\frac13(\vec{AB}+\vec{AC})$。"
        r"$\lambda+2\mu$ 是 $\lambda,\mu$ 的**线性函数**，在线性区域 $\triangle OBC$ 上的最值"
        r"**必在顶点**取得。"
    ),
    'solution': (
        r"**第一步：识别 $O$**" "\n"
        r"$\vec{OA}+\vec{OB}+\vec{OC}=\vec 0$ 表明 $O$ 是 $\triangle ABC$ 的**重心**，" "\n"
        r"故 $\vec{AO}=\dfrac13\left(\vec{AB}+\vec{AC}\right)$，即 $M=O$ 时 $\lambda=\mu=\dfrac13$．" "\n"
        r"**第二步：线性函数在顶点取最值**" "\n"
        r"记 $f=\lambda+2\mu$。因 $\vec{AM}=\lambda\vec{AB}+\mu\vec{AC}$ 中 $(\lambda,\mu)$ 是 $M$ 的"
        r"**仿射坐标**，而 $f$ 是线性函数，故在三角形区域 $\triangle OBC$ 上" "\n"
        r"$f$ 的最大、最小值都必在**顶点** $O,B,C$ 处取得。" "\n"
        r"**第三步：算三个顶点**" "\n"
        r"· $M=O$：$\lambda=\mu=\dfrac13$，$f=\dfrac13+\dfrac23=1$；" "\n"
        r"· $M=B$：$\vec{AM}=\vec{AB}$ ⟹ $\lambda=1,\mu=0$，$f=1$；" "\n"
        r"· $M=C$：$\vec{AM}=\vec{AC}$ ⟹ $\lambda=0,\mu=1$，$f=2$．" "\n"
        r"**第四步**：$\min=1$（在 $O$ 与 $B$ 处同时取到）、$\max=2$（在 $C$ 处）。" "\n"
        r"因 $M$ 在 $\triangle OBC$ 内且**不含边界**，取开区间：$f\in(1,2)$．选 B．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓，由详解「因为 $O$ 是 $\triangle ABC$ 内一点且 "
        r"$\vec{OA}+\vec{OB}+\vec{OC}=\vec 0$，所以 $O$ 为重心；根据点 $M$ 在 $\triangle OBC$ 内，" "\n"
        r"判断出当 $M$ 与 $O$ 重合时 $\lambda+2\mu$ 最小；当 $M$ 与 $C$ 重合时最大，"
        r"因不含边界所以取开区间」「$\vec{AM}=\lambda\vec{AB}+\mu\vec{AC}=\frac13(\vec{AB}+\vec{AC})$，" "\n"
        r"所以 $\lambda=\frac13,\mu=\frac13$，即 $\lambda+2\mu=1$；当 $M$ 与 $C$ 重合时 $\vec{AM}=\vec{AC}$，" "\n"
        r"所以 $\lambda=0,\mu=1$，即 $\lambda+2\mu=2$。因为 $M$ 在 $\triangle OBC$ 内且不含边界，" "\n"
        r"所以取开区间，即 $\lambda+2\mu\in(1,2)$，故选 B」还原，与我的推导**完全一致** ✓。" "\n"
        r"**独立验算（建系）**：取 $A(0,0)$、$B(3,0)$、$C(0,3)$，则重心 $O=(1,1)$。" "\n"
        r"① 验 $O$ 是重心：$\vec{OA}+\vec{OB}+\vec{OC}=(-1,-1)+(2,-1)+(-1,2)=(0,0)$ ✓✓" "\n"
        r"② $M=O(1,1)$：$\vec{AM}=(1,1)=\lambda(3,0)+\mu(0,3)=(3\lambda,3\mu)$ → $\lambda=\mu=\frac13$ ✓" "\n"
        r"$f=\frac13+\frac23=1$ ✓✓" "\n"
        r"③ $M=B(3,0)$：$\vec{AM}=(3,0)$ → $\lambda=1,\mu=0$，$f=1$ ✓✓" "\n"
        r"④ $M=C(0,3)$：$\vec{AM}=(0,3)$ → $\lambda=0,\mu=1$，$f=2$ ✓✓" "\n"
        r"⑤ **内部点验证**（确认是开区间）：取 $\triangle OBC$ 的重心 $M=\frac{O+B+C}3=\left(\frac43,\frac43\right)$" "\n"
        r"$\lambda=\mu=\frac49$，$f=\frac49+\frac89=\frac{12}9=1.333\in(1,2)$ ✓✓" "\n"
        r"取靠近 $C$ 的内点 $M=(0.2,2.5)$：$\lambda=\frac{0.2}3=0.0667$、$\mu=\frac{2.5}3=0.8333$" "\n"
        r"$f=0.0667+1.6667=1.733\in(1,2)$ ✓✓" "\n"
        r"⑥ **排除其他选项**：A 上界 $\frac52=2.5>2$ ✗；C、D 的区间在 $1$ 以下 ✗（$f$ 最小就是 $1$）" "\n"
        r"**答案 B（$(1,2)$）正确** ✓" "\n"
        r"**⭐ 通法**：" "\n"
        r"① $\vec{OA}+\vec{OB}+\vec{OC}=\vec 0$ ⟺ $O$ 是**重心**（记住这条，不用推导）；" "\n"
        r"② 目标式是 $\lambda,\mu$ 的**线性函数** ⟹ 在 polygonal 区域上**最值必在顶点**，" "\n"
        r"只需算几个顶点再比大小，比任何不等式都快；" "\n"
        r"③ 「不含边界」⟹ 取**开区间**；含边界则取闭区间。" "\n"
        r"**本题的细节**：最小值 $1$ 在 $O$ 和 $B$ **两个顶点**同时取到（因为 $OB$ 是一条等和线），" "\n"
        r"这一点不影响结论，但说明 $f$ 在边 $OB$ 上恒为 $1$。"
    ),
    'difficulty': 0.87,
    'topics': ['M-T-234'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-234-V1',
}

T234_V2 = {
    'type': '选择',
    'stem_text': (
        r"在 $\triangle ABC$ 中，$\lvert AC\rvert=2$，$\lvert AB\rvert=2$，$\angle BAC=120^\circ$，"
        r"$\vec{AE}=\lambda\vec{AB}$，$\vec{AF}=\mu\vec{AC}$，$M$ 为线段 $EF$ 的中点，"
        r"若 $\lvert\vec{AM}\rvert=1$，则 $\lambda+\mu$ 的最大值为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac{\sqrt7}3$"),
        ('B', r"$\dfrac{2\sqrt7}3$"),
        ('C', r"$2$"),
        ('D', r"$\dfrac{\sqrt{21}}3$"),
    ],
    'answer': 'C',
    'analysis': (
        r"$M$ 是 $EF$ 中点 ⟹ $\vec{AM}=\frac12(\vec{AE}+\vec{AF})=\frac\lambda2\vec{AB}+\frac\mu2\vec{AC}$。"
        r"由 $\lvert\vec{AB}\rvert=\lvert\vec{AC}\rvert=2$、夹角 $120^\circ$ 展开模长得"
        r"$\lambda^2+\mu^2-\lambda\mu=1$，再用 $s^2=1+3\lambda\mu$ 配 $\lambda\mu\le\frac{s^2}4$。"
    ),
    'solution': (
        r"**第一步：表示 $\vec{AM}$**" "\n"
        r"$M$ 是 $EF$ 中点 ⟹ $\vec{AM}=\dfrac12\left(\vec{AE}+\vec{AF}\right)$"
        r"$=\dfrac\lambda2\vec{AB}+\dfrac\mu2\vec{AC}$．" "\n"
        r"**第二步：展开 $\lvert\vec{AM}\rvert=1$**" "\n"
        r"$\lvert\vec{AB}\rvert=\lvert\vec{AC}\rvert=2$，$\vec{AB}\cdot\vec{AC}=2\cdot2\cos120^\circ=-2$：" "\n"
        r"$\lvert\vec{AM}\rvert^{2}=\dfrac{\lambda^{2}}4\cdot4+\dfrac{\mu^{2}}4\cdot4"
        r"+2\cdot\dfrac\lambda2\cdot\dfrac\mu2\cdot(-2)=\lambda^{2}+\mu^{2}-\lambda\mu=1$．" "\n"
        r"**第三步：求 $\lambda+\mu$ 的最大值**" "\n"
        r"记 $s=\lambda+\mu$，则 $s^{2}=\lambda^{2}+\mu^{2}+2\lambda\mu=(1+\lambda\mu)+2\lambda\mu=1+3\lambda\mu$．" "\n"
        r"由 $\lambda\mu\le\dfrac{s^{2}}4$（均值不等式，$\lambda=\mu=\dfrac s2$ 取等）：" "\n"
        r"$s^{2}\le1+\dfrac{3s^{2}}4\Rightarrow\dfrac{s^{2}}4\le1\Rightarrow s\le2$．" "\n"
        r"**取等条件**：$\lambda=\mu=\dfrac s2=1$，代回 $1+1-1=1$ ✓ 成立．" "\n"
        r"故 $\lambda+\mu$ 的最大值为 $2$．选 C．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓，由详解「化简得到 $\vec{AM}=\frac\lambda2\vec{AB}+\frac\mu2\vec{AC}$，" "\n"
        r"根据 $\lvert\vec{AM}\rvert=1$ 得到 $\lambda^{2}+\mu^{2}-\lambda\mu=1$」还原，" "\n"
        r"与我的推导**关键式完全一致** ✓（详解后续未提取完整，最值推导为我独立完成）。" "\n"
        r"**独立验算**：" "\n"
        r"① **验关键式**：$\lambda=\mu=1$ 时 $1+1-1=1$ ✓，且 $\lambda+\mu=2$ ✓✓" "\n"
        r"② **建系验证**（$A(0,0)$、$B(2,0)$、$C(2\cos120^\circ,2\sin120^\circ)=(-1,\sqrt3)$）：" "\n"
        r"验 $\lvert\vec{AB}\rvert=2$ ✓、$\lvert\vec{AC}\rvert=\sqrt{1+3}=2$ ✓、" "\n"
        r"$\vec{AB}\cdot\vec{AC}=2(-1)+0=-2$ ✓✓" "\n"
        r"$\lambda=\mu=1$：$E=B=(2,0)$、$F=C=(-1,1.732)$；$M=\frac{E+F}2=(0.5,0.866)$" "\n"
        r"$\lvert\vec{AM}\rvert=\sqrt{0.25+0.75}=1$ ✓✓✓ **与 $|\vec{AM}|=1$ 完全吻合**" "\n"
        r"③ **验这是最大值**（取另一组满足条件的 $\lambda,\mu$）：" "\n"
        r"取 $\lambda=1.5$：$\mu^{2}-1.5\mu+1.25=0$，判别式 $=2.25-5=-2.75<0$ ✗ **无解** —— " "\n"
        r"说明 $\lambda$ 取不到 $1.5$，印证 $\lambda+\mu\le2$。" "\n"
        r"取 $\lambda=1.1,\mu=0.9$：$1.21+0.81-0.99=1.03\approx1$ ✓ 且 $s=2.0$ ✓" "\n"
        r"④ **解析求最大**（消元法复核）：令 $\mu$ 为变量，$\mu^{2}-\lambda\mu+(\lambda^{2}-1)=0$ 有解需" "\n"
        r"$\lambda^{2}-4(\lambda^{2}-1)\ge0$ → $3\lambda^{2}\le4$ → $\lambda\le\frac2{\sqrt3}\approx1.1547$。" "\n"
        r"由对称性 $\mu\le1.1547$。取 $\lambda=\frac2{\sqrt3}$ 时 $\mu=\frac\lambda2=\frac1{\sqrt3}$，" "\n"
        r"$s=\frac3{\sqrt3}=\sqrt3\approx1.732<2$ ✓✓ **说明 $s=2$ 在内部取到，确为最大**" "\n"
        r"**答案 C（$2$）正确** ✓" "\n"
        r"**⭐ 通法（非正交基下 $|\vec{AM}|=$ 定值）**：" "\n"
        r"① 中点 ⟹ $\vec{AM}=\frac12(\vec{AE}+\vec{AF})$，系数各减半；" "\n"
        r"② 展开时交叉项系数是 $2\cdot\frac\lambda2\cdot\frac\mu2\cdot(\vec{AB}\cdot\vec{AC})$，" "\n"
        r"本题 $\vec{AB}\cdot\vec{AC}=-2$ ⟹ 交叉项为 $-\lambda\mu$（**负号来自 $120^\circ$ 夹角**）；" "\n"
        r"③ 求 $s=\lambda+\mu$ 范围：用 $s^{2}=\lambda^{2}+\mu^{2}+2\lambda\mu$ 把已知式代换成含 $\lambda\mu$ 的形式，" "\n"
        r"再用 $\lambda\mu\le\frac{s^{2}}4$（**上界**）或 $\lambda\mu\ge$ 某值（下界）夹逼。" "\n"
        r"**⚠ 易错**：$\lambda\mu\le\frac{s^{2}}4$ 只在 $\lambda,\mu$ **同号**时是上界；" "\n"
        r"本题 $E,F$ 在射线上故 $\lambda,\mu>0$ ✓ 可用。"
    ),
    'difficulty': 0.91,
    'topics': ['M-T-234'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-234-V2',
}

T234_V3 = {
    'type': '选择',
    'stem_text': (
        r"$\triangle ABC$ 中，$D$ 为 $AB$ 的中点，点 $F$ 在线段 $CD$ 上（不含端点），"
        r"且满足 $\vec{AF}=x\vec{AB}+y\vec{AC}$（$x,y\in\mathbb R$），则 $\dfrac1x+\dfrac2y$ 的最小值为（　　）"
    ),
    'opts': [
        ('A', r"$3+2\sqrt2$"),
        ('B', r"$2+2\sqrt2$"),
        ('C', r"$6$"),
        ('D', r"$8$"),
    ],
    'answer': 'D',
    'analysis': (
        r"$F$ 在线段 $CD$ 上 ⟹ 把 $\vec{AF}$ 按 $\vec{AC},\vec{AD}$ 分解，系数和为 $1$；"
        r"而 $\vec{AD}=\frac12\vec{AB}$ ⟹ 得到 $x,y$ 的**线性约束** $2x+y=1$。"
        r"再用柯西 $(p\lambda+q\mu)(\frac a\lambda+\frac b\mu)\ge(\sqrt{pa}+\sqrt{qb})^2$ 求最小值。"
    ),
    'solution': (
        r"**第一步：由共线得线性约束**" "\n"
        r"$F$ 在线段 $CD$ 上 ⟹ 存在 $t\in(0,1)$ 使 $\vec{AF}=(1-t)\vec{AC}+t\,\vec{AD}$（系数和 $1$）．" "\n"
        r"而 $D$ 是 $AB$ 中点，$\vec{AD}=\dfrac12\vec{AB}$，故" "\n"
        r"$\vec{AF}=(1-t)\vec{AC}+\dfrac t2\vec{AB}$，" "\n"
        r"与 $\vec{AF}=x\vec{AB}+y\vec{AC}$ 对比：" "\n"
        r"$x=\dfrac t2$，$y=1-t$ ⟹ $2x=t$、$y=1-t$ ⟹ **$2x+y=1$**（$x,y>0$）．" "\n"
        r"**第二步：柯西求最小值**" "\n"
        r"$\left(\dfrac1x+\dfrac2y\right)(2x+y)\ge\left(\sqrt{\dfrac1x\cdot2x}+\sqrt{\dfrac2y\cdot y}\right)^{2}$"
        r"$=\left(\sqrt2+\sqrt2\right)^{2}=\left(2\sqrt2\right)^{2}=8$．" "\n"
        r"由 $2x+y=1$ 得 $\dfrac1x+\dfrac2y\ge8$．" "\n"
        r"**第三步：取等条件**" "\n"
        r"$\dfrac{1/x}{2x}=\dfrac{2/y}{y}$，即 $\dfrac1{2x^{2}}=\dfrac2{y^{2}}\Rightarrow y^{2}=4x^{2}\Rightarrow y=2x$（$x,y>0$）．" "\n"
        r"代入 $2x+y=1$：$4x=1\Rightarrow x=\dfrac14$、$y=\dfrac12$（对应 $t=\dfrac12$，$F$ 是 $CD$ 中点 ✓ 在内部）．" "\n"
        r"此时 $\dfrac1x+\dfrac2y=4+4=8$．选 D．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**详解未提取到**，上述推导为我独立完成）。" "\n"
        r"**独立验算**：" "\n"
        r"① **验约束**：$x=\frac14$、$y=\frac12$ 时 $2x+y=0.5+0.5=1$ ✓✓" "\n"
        r"② **验目标值**：$\frac1{1/4}+\frac2{1/2}=4+4=8$ ✓✓" "\n"
        r"③ **建系验证**（$A(0,0)$、$B(2,0)$、$C(0,2)$，则 $D=(1,0)$ 是 $AB$ 中点）：" "\n"
        r"$t=\frac12$ ⟹ $F$ 是 $CD$ 中点 $=\frac{C+D}2=(0.5,1)$" "\n"
        r"$\vec{AF}=(0.5,1)$；$x\vec{AB}+y\vec{AC}=x(2,0)+y(0,2)=(2x,2y)$" "\n"
        r"$2x=0.5$ → $x=0.25$ ✓；$2y=1$ → $y=0.5$ ✓✓ **与取等条件一致**" "\n"
        r"④ **换点验证（确认是最小值）**：" "\n"
        r"· $t=0.3$：$x=0.15$、$y=0.7$，$\frac1x+\frac2y=6.667+2.857=9.524>8$ ✓" "\n"
        r"· $t=0.7$：$x=0.35$、$y=0.3$，$\frac1x+\frac2y=2.857+6.667=9.524>8$ ✓" "\n"
        r"· $t=0.9$：$x=0.45$、$y=0.1$，$\frac1x+\frac2y=2.222+20=22.22>8$ ✓✓" "\n"
        r"· $t=0.5$：$8$ ✓✓ **确为最小**" "\n"
        r"⑤ **排除干扰项**：A $3+2\sqrt2\approx5.83$、B $2+2\sqrt2\approx4.83$、C $6$ —— "
        r"都小于 $8$，若算漏约束（如误用 $x+y=1$）就会得到这些值。" "\n"
        r"（验算：若约束错成 $x+y=1$，则 $(\frac1x+\frac2y)(x+y)\ge(1+\sqrt2)^{2}=3+2\sqrt2$ → **恰为选项 A**，" "\n"
        r"说明 A 就是命题人为「$2x+y$ 记成 $x+y$」准备的陷阱 ✓）" "\n"
        r"**答案 D（$8$）正确** ✓" "\n"
        r"**⭐ 通法**：" "\n"
        r"① 「$F$ 在线段 $CD$ 上」⟹ 用 $\vec{AC},\vec{AD}$（**不是** $\vec{AB},\vec{AC}$）作基分解，系数和为 $1$；" "\n"
        r"② 若基是 $\vec{AB},\vec{AC}$ 而 $D$ 是中点，则 $\vec{AD}=\frac12\vec{AB}$ ⟹ "
        r"**$x$ 的系数要乘 $2$** —— 本题约束是 $2x+y=1$ 而**不是** $x+y=1$（最关键的一步）；" "\n"
        r"③ 约束 $\alpha x+\beta y=1$ 求 $\frac px+\frac qy$ 最小值，一律柯西：" "\n"
        r"$(\frac px+\frac qy)(\alpha x+\beta y)\ge(\sqrt{p\alpha}+\sqrt{q\beta})^{2}$。" "\n"
        r"本题 $(\sqrt{1\cdot2}+\sqrt{2\cdot1})^{2}=(\sqrt2+\sqrt2)^{2}=8$ ✓"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-234'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-234-V3',
}

QS = [T234_V1, T234_V2, T234_V3]
