# -*- coding: utf-8 -*-
r"""第69批：解三角形范围 + 向量小题 + 立体几何轨迹（12 题）

来源：2024高中数学热点题型归纳完整解析版.pdf p155-156、p200-201、p241-242、p207
M-T-192（4）、M-T-232（2）、M-T-233（2）、M-T-283（2）、M-T-279-V2、M-T-241-E1

## ★★ 12 题我全部独立验算，与原书答案全部吻合

| 题 | 我的验算 | 答案 |
|---|---|---|
| M-T-192-E1 | $B=2A$、$A\in(\frac\pi6,\frac\pi4)$，$\lambda=\frac1{\tan2A}\in(0,\frac{\sqrt3}3)$ | **A** |
| M-T-192-V1 | $A=\frac\pi6$、$B\in(\frac\pi3,\frac\pi2)$，$3\sin$… $=\sqrt3\sin(B+\frac\pi3)\in(\frac{\sqrt3}2,\frac32)$ | **C** |
| M-T-192-V2 | $B\in(\frac\pi6,\frac\pi4)$，$\frac cb=4\cos^2B-1\in(1,2)$ | **D** |
| M-T-192-V3 | ⭐ 题干 `3a` 实为 $\sqrt3a$（否则 $\sin B=\frac32$ 无解）；$B=\frac\pi3$ ⟹ $(\frac{\sqrt3}3,\frac{2\sqrt3}3)$ | **B** |
| M-T-232-V1 | $\vec{BE}=\frac23\vec{AD}-\vec{AB}$，减 $\vec{AB}$ 得 $\frac13\vec{AC}-\frac23\vec{AB}$ | **B** |
| M-T-232-V2 | 建系 $A(0,0),B(2,0),D(0,1),C(1,1)$ ⟹ $F(\frac23,\frac13)$，$\vec{BF}=(-\frac43,\frac13)$ | **C** |
| M-T-233-V1 | 解 $\lambda-\frac\mu2=1$、$\mu+\frac\lambda2=1$ ⟹ $\frac65+\frac25=\frac85$ | **D** |
| M-T-233-V3 | 重心：$\vec{AF}=\frac23\vec{AM}=\frac23\cdot\frac12(\vec{AB}+\vec{AC})=\frac13(\vec a+\vec b)$ | **A** |
| M-T-283-V1 | ⭐ **坐标法穷举 6 面**：截面 6 个顶点确为六边形 | **D** |
| M-T-283-V2 | 平面 $x-2y+2z=0$，代入 $F(1,\frac12,0)$ 成立 | **B** |
| M-T-279-V2 | $FP=\frac12MN=1$，$V=\frac14\cdot\frac43\pi=\frac\pi3$ | **D** |
| M-T-241-E1 | 重心坐标 $O=(\frac78,\frac38)$，$S_{BOC}=\frac18$ ⟹ 比值 $4$ | **D** |

## 最大收获：M-T-283-V1 用坐标法独立确认截面是六边形

设正方体为单位立方体，三点 $M(\frac12,1,1)$、$N(0,0,\frac12)$、$P(1,\frac12,0)$，
解得平面 $x-y+z=\frac12$。逐面求交得 6 个顶点：

| 顶点 | 所在棱 |
|---|---|
| $(\frac12,0,0)$ | $AB$ |
| $(1,\frac12,0)$ | $BC$（即 $P$） |
| $(1,1,\frac12)$ | $CC_1$ |
| $(\frac12,1,1)$ | $C_1D_1$（即 $M$） |
| $(0,\frac12,1)$ | $A_1D_1$ |
| $(0,0,\frac12)$ | $AA_1$（即 $N$） |

**6 个顶点 ⟹ 六边形**，答案 D 确凿（不依赖原书详解的平行四边形论证）。

## 选项还原说明

- M-T-192 四题的选项在 ref_bank 中存成 `3 | 3`、`1 | 2` 这种分数碎片，
  我按「分子 / 分母」还原，并用**解出的取值范围与选项逐一比对**确认（见每题 review）。
- M-T-233-V3 的选项序列 `1 1 2 2 1 1 2 1 / 3 3 3 3 2 2 3 2` 拆成四组：
  A$(\frac13,\frac13)$、B$(\frac23,\frac23)$、C$(\frac12,\frac12)$、D$(\frac23,\frac12)$。
"""

T192_E1 = {
    'type': '选择',
    'stem_text': (
        r"锐角 $\triangle ABC$ 的内角 $A,B,C$ 的对边分别为 $a,b,c$，且 $a=1$，$b\cos A-\cos B=1$。"
        r"若 $A,B$ 变化时，$\sin B-2\lambda\sin^{2}A$ 存在最大值，则正数 $\lambda$ 的取值范围是（　　）"
    ),
    'opts': [
        ('A', r"$\left(0,\dfrac{\sqrt3}3\right)$"),
        ('B', r"$\left(0,\dfrac12\right)$"),
        ('C', r"$\left(\dfrac{\sqrt3}3,\dfrac{\sqrt2}2\right)$"),
        ('D', r"$\left(\dfrac12,1\right)$"),
    ],
    'answer': 'A',
    'analysis': (
        r"由 $a=1$ 把条件写成 $b\cos A-a\cos B=a$，正弦定理得 $\sin(B-A)=\sin A$，故 $B=2A$。"
        r"锐角三角形给出 $A\in(\frac\pi6,\frac\pi4)$。原式 $=\sqrt{1+\lambda^{2}}\sin(2A+\varphi)-\lambda$，"
        r"最大值存在的条件是 $\frac\pi2$ 落在 $2A+\varphi$ 的取值区间内。"
    ),
    'solution': (
        r"因为 $a=1$，$b\cos A-\cos B=1$，所以 $b\cos A-a\cos B=a$。" "\n"
        r"由正弦定理：$\sin B\cos A-\sin A\cos B=\sin A$，即 $\sin(B-A)=\sin A$。" "\n"
        r"因 $A,B\in(0,\pi)$ 且 $B>A$（否则 $B-A<0$ 而 $\sin A>0$ 矛盾），故 $B-A=A$，即 $B=2A$。" "\n"
        r"**锐角条件**：" "\n"
        r"$\begin{cases}0<A<\frac\pi2\\[2pt] 0<B=2A<\frac\pi2\\[2pt] 0<C=\pi-3A<\frac\pi2\end{cases}"
        r"\Rightarrow\begin{cases}A<\frac\pi2\\[2pt] A<\frac\pi4\\[2pt] \frac\pi6<A<\frac\pi3\end{cases}"
        r"\Rightarrow \dfrac\pi6<A<\dfrac\pi4$。" "\n"
        r"**化简目标式**：" "\n"
        r"$\sin B-2\lambda\sin^{2}A=\sin2A-\lambda(1-\cos2A)=\sin2A+\lambda\cos2A-\lambda$" "\n"
        r"$=\sqrt{1+\lambda^{2}}\sin(2A+\varphi)-\lambda$，其中 $\tan\varphi=\lambda$（$\varphi\in(0,\frac\pi2)$）。" "\n"
        r"**存在最大值的条件**：$2A\in(\frac\pi3,\frac\pi2)$，故 $2A+\varphi\in(\frac\pi3+\varphi,\frac\pi2+\varphi)$。" "\n"
        r"$\sin$ 在该区间内取到 $1$ 当且仅当 $\frac\pi2\in(\frac\pi3+\varphi,\frac\pi2+\varphi)$，" "\n"
        r"即 $0<\varphi<\frac\pi6$，亦即 $\lambda=\tan\varphi\in(0,\frac{\sqrt3}3)$。故选 A。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p155 详解：「因为 $a=1$，$b\cos A-\cos B=1$，所以 $b\cos A-a\cos B=a$，" "\n"
        r"可得：$\sin B\cos A-\sin A\cos B=\sin A$，即 $\sin(B-A)=\sin A$，∴$B=2A$。因为 $\triangle ABC$ 为锐角三角形…" "\n"
        r"解得：$\frac\pi6<A<\frac\pi4$…$\sin B-2\lambda\sin^{2}A=\sin2A-2\lambda\sin^{2}A=\sin2A-\lambda(1-\cos2A)$" "\n"
        r"$=\sqrt{1+\lambda^{2}}\sin(2A+\varphi)-\lambda$，$\tan\varphi=\lambda$…$\lambda=\tan\varphi=\frac1{\tan2A}$，" "\n"
        r"∵$\frac\pi3<2A<\frac\pi2$，∴$\tan2A>\sqrt3$，即 $0<\frac1{\tan2A}<\frac{\sqrt3}3$，所以 $\lambda\in(0,\frac{\sqrt3}3)$。故选：A。」" "\n"
        r"—— **$B=2A$、$A\in(\frac\pi6,\frac\pi4)$、$\sqrt{1+\lambda^2}\sin(2A+\varphi)-\lambda$、$\lambda=\frac1{\tan2A}$、$\lambda\in(0,\frac{\sqrt3}3)$ 全部与我的推导一致** ✓✓✓" "\n"
        r"（⚠ 详解中间有一句「解得 $\frac\pi6<A<\frac\pi2$」是笔误，由后文 $\frac\pi3<2A<\frac\pi2$ 可知正确为 $\frac\pi6<A<\frac\pi4$）" "\n"
        r"**独立验算**：" "\n"
        r"① **$B=2A$**：$b\cos A-a\cos B=a$ ⟹ $\sin B\cos A-\sin A\cos B=\sin A$ ⟹ $\sin(B-A)=\sin A$。" "\n"
        r"$B-A=A$（$B-A=\pi-A$ 会得 $B=\pi$，舍）✓✓✓" "\n"
        r"② **$A\in(\frac\pi6,\frac\pi4)$**：$2A<\frac\pi2$ ⟹ $A<\frac\pi4$；$\pi-3A<\frac\pi2$ ⟹ $A>\frac\pi6$ ✓✓✓" "\n"
        r"③ **$2A\in(\frac\pi3,\frac\pi2)$、$\tan2A>\sqrt3$** ✓✓✓ ⟹ $\frac1{\tan2A}\in(0,\frac{\sqrt3}3)$ ✓✓✓" "\n"
        r"④ **$\sin2A+\lambda\cos2A=\sqrt{1+\lambda^2}\sin(2A+\varphi)$**：振幅 $\sqrt{1+\lambda^2}$ ✓✓✓" "\n"
        r"⑤ **数值检验**：取 $\lambda=0.3\in(0,0.5774)$，$f(A)=\sin2A+0.3\cos2A$。" "\n"
        r"$A=\frac\pi6$：$f=0.8660+0.15=1.0160$；$A=\frac\pi5$（$2A=72^\circ$）：$f=0.9511+0.0927=1.0438$；" "\n"
        r"$A=0.4\pi$ 内取 $2A=80^\circ$：$f=0.9848+0.0521=1.0369$。" "\n"
        r"振幅 $\sqrt{1.09}=1.0440$，在 $2A+\varphi=\frac\pi2$（$\varphi=\arctan0.3=16.7^\circ$，$2A=73.3^\circ$）处取到 ✓✓✓ **最大值可达**" "\n"
        r"取 $\lambda=0.6>0.5774$：$\varphi=30.96^\circ$，$2A+\varphi\in(90.96^\circ,120.96^\circ)$，$\sin$ 单调递减，**最大值在左端点取不到** ✓✓✓ **无最大值**" "\n"
        r"⑥ **选项排除**：只有 A 的左端为 $0$ 且右端 $\frac{\sqrt3}3$；B $(0,\frac12)$ 漏了 $(\frac12,\frac{\sqrt3}3)$ 这一段；" "\n"
        r"C、D 左端不是 $0$，$\lambda\to0^+$ 时显然有最大值（$\sin2A$ 在 $(\frac\pi3,\frac\pi2)$ 上有最大值 $1$）✗" "\n"
        r"**答案 A 正确** ✓" "\n"
        r"**⭐⭐ 通法（「存在最大值」型参数范围）**：" "\n"
        r"① ⭐⭐ **先由边角关系定出角的范围**：本题 $B=2A$ + 锐角 ⟹ $A\in(\frac\pi6,\frac\pi4)$ —— **锐角三角形的三个不等式一个都不能少**；" "\n"
        r"② ⭐⭐ **$p\sin\theta+q\cos\theta$ 存在最大值 ⟺ 峰值点 $\frac\pi2$ 落在 $\theta+\varphi$ 的区间内**，" "\n"
        r"**不是「求最大值」而是「判断能否取到」** —— 这是本题唯一的考点；" "\n"
        r"③ ⭐ **$\lambda=\frac1{\tan2A}$ 的单调性**：$2A\in(\frac\pi3,\frac\pi2)$ 上 $\tan$ 递增 ⟹ $\frac1{\tan}$ 递减，" "\n"
        r"值域 $(0,\frac{\sqrt3}3)$（**两端都是开的**，因为 $A$ 的范围是开区间）；" "\n"
        r"④ ⚠ **$\sin^{2}A$ 与 $\sin 2A$ 要分清**：提取文本常把 $\sin^2A$ 写成 `sin2A`；" "\n"
        r"由 $\sin B=\sin2A$ 也印证了 $B=2A$ 时目标式首项是 $\sin2A$ ✓；" "\n"
        r"⑤ 检验：**取区间内、外各一个 $\lambda$ 数值扫描**（$0.3$ 有最大值、$0.6$ 无最大值），这是最直观的验证。"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-192'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-192-E1',
}

T192_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知锐角三角形 $\triangle ABC$ 的内角 $A,B,C$ 的对边分别为 $a,b,c$，且 $b=2a\sin B$，"
        r"则 $\cos B+\sin C$ 的取值范围为（　　）"
    ),
    'opts': [
        ('A', r"$\left(0,\sqrt3\right]$"),
        ('B', r"$\left(1,\sqrt3\right]$"),
        ('C', r"$\left(\dfrac{\sqrt3}2,\dfrac32\right)$"),
        ('D', r"$\left(\dfrac12,\dfrac{\sqrt3}2\right)$"),
    ],
    'answer': 'C',
    'analysis': (
        r"由 $b=2a\sin B$ 得 $\sin A=\frac12$，故 $A=\frac\pi6$。锐角 ⟹ $B\in(\frac\pi3,\frac\pi2)$。"
        r"$\cos B+\sin C=\cos B+\sin(\frac{5\pi}6-B)=\frac32\cos B+\frac{\sqrt3}2\sin B=\sqrt3\sin(B+\frac\pi3)$。"
    ),
    'solution': (
        r"由 $b=2a\sin B$ 及正弦定理 $b=2R\sin B$、$a=2R\sin A$：" "\n"
        r"$2R\sin B=2\cdot2R\sin A\sin B\Rightarrow\sin A=\dfrac12$（$\sin B>0$）。" "\n"
        r"因 $\triangle ABC$ 是锐角三角形，$A\in(0,\frac\pi2)$，故 $A=\dfrac\pi6$。" "\n"
        r"**锐角条件**：$A+B>\frac\pi2\Rightarrow B>\frac\pi3$；又 $B<\frac\pi2$。故 $B\in(\frac\pi3,\frac\pi2)$。" "\n"
        r"**化简**：$C=\pi-A-B=\dfrac{5\pi}6-B$，" "\n"
        r"$\cos B+\sin C=\cos B+\sin\left(\dfrac{5\pi}6-B\right)$" "\n"
        r"$=\cos B+\sin\dfrac{5\pi}6\cos B-\cos\dfrac{5\pi}6\sin B=\cos B+\dfrac12\cos B+\dfrac{\sqrt3}2\sin B$" "\n"
        r"$=\dfrac32\cos B+\dfrac{\sqrt3}2\sin B=\sqrt3\left(\dfrac{\sqrt3}2\cos B+\dfrac12\sin B\right)=\sqrt3\sin\left(B+\dfrac\pi3\right)$。" "\n"
        r"因 $B\in(\frac\pi3,\frac\pi2)$，故 $B+\frac\pi3\in(\frac{2\pi}3,\frac{5\pi}6)$。" "\n"
        r"$\sin$ 在 $(\frac{2\pi}3,\frac{5\pi}6)$ 上单调递减，$\sin\frac{2\pi}3=\frac{\sqrt3}2$、$\sin\frac{5\pi}6=\frac12$，" "\n"
        r"故 $\sin(B+\frac\pi3)\in(\frac12,\frac{\sqrt3}2)$，$\sqrt3\sin(B+\frac\pi3)\in(\frac{\sqrt3}2,\frac32)$。故选 C。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p155 详解：「依题意 $b=2a\sin B$，由正弦定理得 $\sin B=2\sin A\sin B$，所以 $\sin A=\frac12$…" "\n"
        r"由于三角形 $ABC$ 是锐角三角形，所以 $A=\frac\pi6$。由 $A+B>\frac\pi2$、$0<B<\frac\pi2$ ⟹ $\frac\pi3<B<\frac\pi2$。" "\n"
        r"所以 $\cos B+\sin C=\cos B+\sin(\frac{5\pi}6-B)=\cos B+\frac12\cos B+\frac{\sqrt3}2\sin B=\frac32\cos B+\frac{\sqrt3}2\sin B=\sqrt3\sin(B+\frac\pi3)$，" "\n"
        r"由于 $\frac{2\pi}3<B+\frac\pi3<\frac{5\pi}6$，所以 $\sin(B+\frac\pi3)\in(\frac12,\frac{\sqrt3}2)$，所以 $\sqrt3\sin(B+\frac\pi3)\in(\frac{\sqrt3}2,\frac32)$。故选：C」" "\n"
        r"—— **$A=\frac\pi6$、$B\in(\frac\pi3,\frac\pi2)$、$\sqrt3\sin(B+\frac\pi3)$、$(\frac{\sqrt3}2,\frac32)$ 全部与我的推导一致** ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **$\sin A=\frac12$**：$b=2a\sin B$ ⟹ $\sin B=2\sin A\sin B$ ⟹ $\sin A=\frac12$ ✓✓✓" "\n"
        r"② **$B\in(\frac\pi3,\frac\pi2)$**：$C=\pi-A-B<\frac\pi2$ ⟹ $A+B>\frac\pi2$ ⟹ $B>\frac\pi2-\frac\pi6=\frac\pi3$ ✓✓✓" "\n"
        r"③ **$\sin(\frac{5\pi}6-B)=\frac12\cos B+\frac{\sqrt3}2\sin B$**：$\sin\frac{5\pi}6=\frac12$、$\cos\frac{5\pi}6=-\frac{\sqrt3}2$ ✓✓✓" "\n"
        r"④ **合成 $\sqrt3\sin(B+\frac\pi3)$**：$\sqrt3(\sin B\cos\frac\pi3+\cos B\sin\frac\pi3)=\sqrt3(\frac12\sin B+\frac{\sqrt3}2\cos B)=\frac{\sqrt3}2\sin B+\frac32\cos B$ ✓✓✓" "\n"
        r"⑤ **$\sin$ 在 $(\frac{2\pi}3,\frac{5\pi}6)$ 递减**：该区间含于 $(\frac\pi2,\pi)$ ✓✓✓" "\n"
        r"$\sin\frac{2\pi}3=\frac{\sqrt3}2=0.8660$、$\sin\frac{5\pi}6=\frac12=0.5$ ⟹ 值域 $(\frac12,\frac{\sqrt3}2)$（开区间）✓✓✓" "\n"
        r"⑥ **$\sqrt3\times$**：下 $\sqrt3\cdot\frac12=\frac{\sqrt3}2=0.8660$；上 $\sqrt3\cdot\frac{\sqrt3}2=\frac32=1.5$ ✓✓✓" "\n"
        r"⑦ **数值检验**：取 $B=70^\circ$（在 $(60^\circ,90^\circ)$ 内），$C=180^\circ-30^\circ-70^\circ=80^\circ$。" "\n"
        r"$\cos70^\circ+\sin80^\circ=0.3420+0.9848=1.3268$。" "\n"
        r"公式：$\sqrt3\sin(70^\circ+60^\circ)=\sqrt3\sin130^\circ=1.7321\times0.7660=1.3268$ ✓✓✓ **完全吻合**" "\n"
        r"⑧ **边界**：$B\to60^\circ$ 时 $C\to90^\circ$（非锐角，取不到），值 $\to\sqrt3\sin120^\circ=\frac32$；" "\n"
        r"$B\to90^\circ$ 时（非锐角，取不到），值 $\to\sqrt3\sin150^\circ=\frac{\sqrt3}2$ ✓✓✓ **两端都开**" "\n"
        r"**答案 C 正确** ✓" "\n"
        r"**⭐⭐ 通法（锐角三角形 + 一角已知 ⟹ 另一角范围）**：" "\n"
        r"① ⭐⭐ **锐角三角形 ⟺ 任意两角和 $>\frac\pi2$**。已知 $A$ 时，$B$ 的范围由" "\n"
        r"$B<\frac\pi2$、$C=\pi-A-B<\frac\pi2$（⟹ $B>\frac\pi2-A$）、$B>0$ 三条夹出来 —— **最容易漏的是 $A+B>\frac\pi2$**；" "\n"
        r"② ⭐ **$\cos B+\sin C$ 这种「两角异名」先统一成单角**：用 $C=\pi-A-B$ 代掉，再用辅助角合成；" "\n"
        r"③ ⭐⭐ **辅助角系数别配错**：$\frac32\cos B+\frac{\sqrt3}2\sin B$ 的振幅 $=\sqrt{(\frac32)^2+(\frac{\sqrt3}2)^2}=\sqrt{3}=\sqrt3$ ✓，" "\n"
        r"提 $\sqrt3$ 后得 $\frac{\sqrt3}2\cos B+\frac12\sin B=\sin(B+\frac\pi3)$ —— **$\cos$ 配 $\sin\frac\pi3$、$\sin$ 配 $\cos\frac\pi3$**；" "\n"
        r"④ ⚠ **端点开闭**：锐角是**严格**不等式，本题两端都取不到 ⟹ 全开区间 $(\frac{\sqrt3}2,\frac32)$。" "\n"
        r"选项 A $(0,\sqrt3]$ 与 B $(1,\sqrt3]$ 都是**闭右端**，是命题人为「忘记锐角取不到端点」准备的陷阱；" "\n"
        r"⑤ 检验：**取区间内一个具体角数值对拍**（$B=70^\circ$ 给出 $1.3268$，公式值同为 $1.3268$ ✓）。"
    ),
    'difficulty': 0.82,
    'topics': ['M-T-192'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-192-V1',
}

T192_V2 = {
    'type': '选择',
    'stem_text': (
        r"在锐角 $\triangle ABC$ 中，$A=2B$，则 $\dfrac{AB}{AC}$ 的取值范围是（　　）"
    ),
    'opts': [
        ('A', r"$(-1,3)$"),
        ('B', r"$(1,3)$"),
        ('C', r"$(\sqrt2,\sqrt3)$"),
        ('D', r"$(1,2)$"),
    ],
    'answer': 'D',
    'analysis': (
        r"锐角给出 $B\in(\frac\pi6,\frac\pi4)$。$\dfrac{AB}{AC}=\dfrac cb=\dfrac{\sin C}{\sin B}=\dfrac{\sin3B}{\sin B}"
        r"=3-4\sin^{2}B=4\cos^{2}B-1$。"
    ),
    'solution': (
        r"**锐角条件**：$A=2B$，故" "\n"
        r"$\begin{cases}0<A=2B<\frac\pi2\\[2pt] 0<B<\frac\pi2\\[2pt] 0<C=\pi-3B<\frac\pi2\end{cases}"
        r"\Rightarrow\begin{cases}B<\frac\pi4\\[2pt] B<\frac\pi2\\[2pt] \frac\pi6<B<\frac\pi3\end{cases}"
        r"\Rightarrow \dfrac\pi6<B<\dfrac\pi4$。" "\n"
        r"**化简比值**：由正弦定理 $\dfrac{AB}{AC}=\dfrac cb=\dfrac{\sin C}{\sin B}=\dfrac{\sin(\pi-3B)}{\sin B}=\dfrac{\sin3B}{\sin B}$。" "\n"
        r"由三倍角公式 $\sin3B=3\sin B-4\sin^{3}B$，故" "\n"
        r"$\dfrac{\sin3B}{\sin B}=3-4\sin^{2}B=3-4(1-\cos^{2}B)=4\cos^{2}B-1$。" "\n"
        r"因 $B\in(\frac\pi6,\frac\pi4)$，$\cos B\in(\frac{\sqrt2}2,\frac{\sqrt3}2)$，$\cos^{2}B\in(\frac12,\frac34)$，" "\n"
        r"故 $4\cos^{2}B-1\in(1,2)$。故选 D。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p156 详解：「在锐角 $\triangle ABC$ 中，$0<2\angle B<\frac\pi2$、" "\n"
        r"$0<\angle B<\frac\pi2$、$0<\pi-3\angle B<\frac\pi2$，可得 $\frac\pi6<\angle B<\frac\pi4$，$\cos B\in(\frac{\sqrt2}2,\frac{\sqrt3}2)$，$\cos^2B\in(\frac12,\frac34)$，" "\n"
        r"所以由正弦定理可知 $\frac{AB}{AC}=\frac cb=\frac{\sin C}{\sin B}=\frac{\sin3B}{\sin B}=\frac{3\sin B-4\sin^3B}{\sin B}=3-4\sin^2B=4\cos^2B-1\in(1,2)$，故选 D。」" "\n"
        r"—— **$B\in(\frac\pi6,\frac\pi4)$、$\cos^2B\in(\frac12,\frac34)$、$4\cos^2B-1\in(1,2)$ 全部与我的推导一致** ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **$B\in(\frac\pi6,\frac\pi4)$**：$2B<\frac\pi2$ ⟹ $B<\frac\pi4$；$\pi-3B<\frac\pi2$ ⟹ $B>\frac\pi6$ ✓✓✓" "\n"
        r"② **$\frac cb=\frac{\sin C}{\sin B}$**：$c$ 对 $C$、$b$ 对 $B$ ✓✓✓；$C=\pi-A-B=\pi-3B$ ⟹ $\sin C=\sin3B$ ✓✓✓" "\n"
        r"③ **$3-4\sin^2B=4\cos^2B-1$**：$3-4(1-\cos^2B)=4\cos^2B-1$ ✓✓✓" "\n"
        r"④ **数值检验**：取 $B=40^\circ$（在 $(30^\circ,45^\circ)$ 内），则 $A=80^\circ$、$C=60^\circ$。" "\n"
        r"$\frac{\sin60^\circ}{\sin40^\circ}=\frac{0.8660}{0.6428}=1.3473$。" "\n"
        r"公式：$4\cos^240^\circ-1=4(0.7660)^2-1=4(0.5868)-1=2.3473-1=1.3473$ ✓✓✓ **完全吻合**" "\n"
        r"⑤ **边界**：$B\to30^\circ$：$4\cos^230^\circ-1=4\cdot\frac34-1=2$（$C\to90^\circ$，非锐角，取不到）；" "\n"
        r"$B\to45^\circ$：$4\cos^245^\circ-1=4\cdot\frac12-1=1$（$A\to90^\circ$，非锐角，取不到）✓✓✓ **两端都开**" "\n"
        r"⑥ **单调性**：$B$ 增大 ⟹ $\cos B$ 减小 ⟹ 比值减小，**在 $(\frac\pi6,\frac\pi4)$ 上严格递减**，" "\n"
        r"故值域恰为 $(1,2)$，无内部极值 ✓✓✓" "\n"
        r"⑦ **选项排除**：A $(-1,3)$ 含负数，边长之比必为正 ✗；B $(1,3)$ 上界错；C $(\sqrt2,\sqrt3)\approx(1.414,1.732)$ 只是其中一段 ✗" "\n"
        r"**答案 D 正确** ✓" "\n"
        r"**⭐⭐ 通法（含 $A=2B$ 的比值范围）**：" "\n"
        r"① ⭐⭐ **$\frac{\sin3B}{\sin B}=3-4\sin^{2}B=4\cos^{2}B-1$** —— 这是 $A=2B$ 题型的核心恒等式，" "\n"
        r"把比值化成 $\cos^2B$ 的一次式，**范围一眼看出**；" "\n"
        r"② ⭐ **锐角 ⟹ $B\in(\frac\pi6,\frac\pi4)$**：两个约束分别来自 $A=2B<\frac\pi2$ 与 $C=\pi-3B<\frac\pi2$，" "\n"
        r"**$\pi-3B>0$ 给出 $B<\frac\pi3$ 是冗余的**（比 $\frac\pi4$ 松）；" "\n"
        r"③ ⭐ **先判单调再定端点**：$4\cos^2B-1$ 在 $B\in(0,\frac\pi2)$ 上递减，" "\n"
        r"所以值域就是两端点值的开区间 —— **不用再找最值**；" "\n"
        r"④ ⚠ **$AB$、$AC$ 谁是分子**：$AB=c$（对 $C$）、$AC=b$（对 $B$），" "\n"
        r"$\frac{AB}{AC}=\frac cb=\frac{\sin C}{\sin B}$ —— **别写反成 $\frac{\sin B}{\sin C}$**；" "\n"
        r"⑤ 检验：**取区间内一个角数值对拍**（$B=40^\circ$ 给 $1.3473$，公式同为 $1.3473$ ✓），并**查两端点**（$1$ 与 $2$）。"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-192'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-192-V2',
}

T192_V3 = {
    'type': '选择',
    'stem_text': (
        r"锐角 $\triangle ABC$ 中，角 $A,B,C$ 所对的边分别为 $a,b,c$，若 $2\sin A(a\cos C+c\cos A)=\sqrt3\,a$，"
        r"则 $\dfrac cb$ 的取值范围是（　　）"
    ),
    'opts': [
        ('A', r"$\left(\dfrac12,2\right)$"),
        ('B', r"$\left(\dfrac{\sqrt3}3,\dfrac{2\sqrt3}3\right)$"),
        ('C', r"$(1,2)$"),
        ('D', r"$\left(\dfrac{\sqrt3}2,1\right)$"),
    ],
    'answer': 'B',
    'analysis': (
        r"射影定理 $a\cos C+c\cos A=b$，故 $2\sin A\cdot b=\sqrt3 a$，正弦定理得 $\sin B=\frac{\sqrt3}2$，"
        r"$B=\frac\pi3$。$\frac cb=\frac{\sin C}{\sin B}=\frac{2\sqrt3}3\sin C$，$C\in(\frac\pi6,\frac\pi2)$。"
    ),
    'solution': (
        r"由射影定理：$a\cos C+c\cos A=b$，代入条件得 $2\sin A\cdot b=\sqrt3\,a$。" "\n"
        r"由正弦定理 $a=2R\sin A$、$b=2R\sin B$：" "\n"
        r"$2\sin A\cdot2R\sin B=\sqrt3\cdot2R\sin A\Rightarrow \sin B=\dfrac{\sqrt3}2$（$\sin A>0$）。" "\n"
        r"因 $\triangle ABC$ 是锐角三角形，$B=\dfrac\pi3$（$B=\frac{2\pi}3$ 为钝角，舍）。" "\n"
        r"**锐角条件**：$A=\pi-B-C=\dfrac{2\pi}3-C<\dfrac\pi2\Rightarrow C>\dfrac\pi6$；又 $C<\dfrac\pi2$。" "\n"
        r"故 $C\in(\frac\pi6,\frac\pi2)$，$\sin C\in(\frac12,1)$。" "\n"
        r"$\dfrac cb=\dfrac{\sin C}{\sin B}=\dfrac{\sin C}{\sqrt3/2}=\dfrac{2\sqrt3}3\sin C\in\left(\dfrac{\sqrt3}3,\dfrac{2\sqrt3}3\right)$。故选 B。"
    ),
    'review': (
        r"★ 题干的系数 **$\sqrt3$ 是我还原的**：ref_bank 提取为 `3a`，原书详解也写「$\sin(A+C)=\frac32$」——" "\n"
        r"**反证**：若右边是 $3a$，则由射影定理 $a\cos C+c\cos A=b$ 得 $2\sin A\cdot b=3a$ ⟹ $\sin B=\frac32>1$，" "\n"
        r"**无解**；取 $\sqrt3$ 则 $\sin B=\frac{\sqrt3}2$ ⟹ $B=\frac\pi3$，与答案 B 完全吻合 ✓✓✓" "\n"
        r"原书 p156 详解：「由正弦定理得，$2\sin A(\sin A\cos C+\sin C\cos A)=\sqrt3\sin A$ ⟹ $\sin(A+C)=\frac{\sqrt3}2$ ⟹ $B=\frac\pi3$。" "\n"
        r"又∵$A,C\in(0,\frac\pi2)$ ∴$\frac\pi6<C<\frac\pi2$ ⟹ $\frac12<\sin C<1$ ⟹ $\frac cb=\frac{\sin C}{\sin B}=\frac{2\sqrt3}3\sin C\in(\frac{\sqrt3}3,\frac{2\sqrt3}3)$。故选 B。」" "\n"
        r"（详解里 $\sin(A+C)=\frac32$ 是 $\frac{\sqrt3}2$ 丢失根号所致，结论 $B=\frac\pi3$ 正确）" "\n"
        r"**独立验算**：" "\n"
        r"① **射影定理** $a\cos C+c\cos A=b$：标准结论 ✓✓✓（也可由 $a\cos C+c\cos A=2R(\sin A\cos C+\sin C\cos A)=2R\sin(A+C)=2R\sin B=b$ 推出）" "\n"
        r"② **$\sin B=\frac{\sqrt3}2$**：$2\sin A\cdot b=\sqrt3 a$ ⟹ $2\sin A\cdot\sin B=\sqrt3\sin A$ ⟹ $\sin B=\frac{\sqrt3}2$ ✓✓✓" "\n"
        r"③ **$B=\frac\pi3$**（锐角，舍去 $\frac{2\pi}3$）✓✓✓" "\n"
        r"④ **$C\in(\frac\pi6,\frac\pi2)$**：$A=\frac{2\pi}3-C<\frac\pi2$ ⟹ $C>\frac\pi6$ ✓✓✓" "\n"
        r"⑤ **$\frac cb=\frac{\sin C}{\sin B}$** ✓✓✓；$\frac1{\sin(\pi/3)}=\frac2{\sqrt3}=\frac{2\sqrt3}3=1.1547$ ✓✓✓" "\n"
        r"⑥ **值域**：$1.1547\times0.5=0.5774=\frac{\sqrt3}3$；$1.1547\times1=1.1547=\frac{2\sqrt3}3$ ✓✓✓" "\n"
        r"⑦ **数值检验**：取 $C=45^\circ$，则 $A=180^\circ-60^\circ-45^\circ=75^\circ$（锐角 ✓）。" "\n"
        r"$\frac cb=\frac{\sin45^\circ}{\sin60^\circ}=\frac{0.7071}{0.8660}=0.8165$。" "\n"
        r"公式：$\frac{2\sqrt3}3\sin45^\circ=1.1547\times0.7071=0.8165$ ✓✓✓ **完全吻合**" "\n"
        r"⑧ **边界**：$C\to\frac\pi6$ 时 $A\to\frac\pi2$（非锐角，取不到），值 $\to\frac{2\sqrt3}3\cdot\frac12=\frac{\sqrt3}3$；" "\n"
        r"$C\to\frac\pi2$ 时（非锐角，取不到），值 $\to\frac{2\sqrt3}3$ ✓✓✓ **两端都开**" "\n"
        r"**答案 B 正确** ✓" "\n"
        r"**⭐⭐ 通法（射影定理秒化简）**：" "\n"
        r"① ⭐⭐ **$a\cos C+c\cos A=b$**（射影定理）—— 看到 $a\cos C+c\cos A$ 这种「交叉配」直接换成 $b$，" "\n"
        r"**比展开成正弦和角公式快得多**；同理 $a\cos B+b\cos A=c$、$b\cos C+c\cos B=a$；" "\n"
        r"② ⭐⭐ **「$\sin x=\frac32$」这种超过 $1$ 的等式 = 根号丢失的警报** —— " "\n"
        r"本项目已多次靠它定位还原错误（本题把 `3` 还原为 $\sqrt3$）；" "\n"
        r"③ ⭐ **已知 $B$ 求 $\frac cb$ 的范围**：$\frac cb=\frac{\sin C}{\sin B}$，只需定 $C$ 的范围，" "\n"
        r"而 $C$ 由「$A<\frac\pi2$」和「$C<\frac\pi2$」两条夹出；" "\n"
        r"④ ⚠ **别漏了锐角对 $A$ 的约束**：只写 $C<\frac\pi2$ 会得到 $C\in(0,\frac\pi2)$、值域 $(0,\frac{2\sqrt3}3)$ —— " "\n"
        r"**选项里没有这个**，此时就该回头检查锐角条件；" "\n"
        r"⑤ 检验：**取区间内一个角数值对拍**（$C=45^\circ$ 给 $0.8165$，公式同为 $0.8165$ ✓）。"
    ),
    'difficulty': 0.83,
    'topics': ['M-T-192'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-192-V3',
}

T232_V1 = {
    'type': '选择',
    'stem_text': (
        r"如图，在 $\triangle ABC$ 中，$D$ 为 $BC$ 中点，$E$ 在线段 $AD$ 上，且 $AE=2ED$，则 $\vec{BE}=$（　　）"
    ),
    'opts': [
        ('A', r"$-\dfrac13\vec{AC}+\dfrac23\vec{AB}$"),
        ('B', r"$\dfrac13\vec{AC}-\dfrac23\vec{AB}$"),
        ('C', r"$\dfrac23\vec{AC}-\dfrac13\vec{AB}$"),
        ('D', r"$\dfrac23\vec{AC}+\dfrac13\vec{AB}$"),
    ],
    'answer': 'B',
    'analysis': (
        r"$\vec{AD}=\frac12(\vec{AB}+\vec{AC})$；$\vec{AE}=\frac23\vec{AD}$；"
        r"$\vec{BE}=\vec{AE}-\vec{AB}=\frac13(\vec{AB}+\vec{AC})-\vec{AB}=\frac13\vec{AC}-\frac23\vec{AB}$。"
    ),
    'solution': (
        r"因 $D$ 为 $BC$ 的中点，由中点向量公式：" "\n"
        r"$\vec{AD}=\dfrac12\left(\vec{AB}+\vec{AC}\right)$。" "\n"
        r"由 $AE=2ED$ 且 $E$ 在线段 $AD$ 上，得 $AE=\dfrac23AD$，即 $\vec{AE}=\dfrac23\vec{AD}$。" "\n"
        r"故 $\vec{BE}=\vec{AE}-\vec{AB}=\dfrac23\vec{AD}-\vec{AB}=\dfrac23\cdot\dfrac12\left(\vec{AB}+\vec{AC}\right)-\vec{AB}$" "\n"
        r"$=\dfrac13\vec{AB}+\dfrac13\vec{AC}-\vec{AB}=\dfrac13\vec{AC}-\dfrac23\vec{AB}$。故选 B。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p200 详解：「∵$D$ 为 $BC$ 的中点，则 $\vec{AD}=\vec{AB}+\vec{BD}=\vec{AB}+\frac12\vec{BC}$" "\n"
        r"$=\vec{AB}+\frac12(\vec{AC}-\vec{AB})=\frac12(\vec{AB}+\vec{AC})$；∵$AE=2ED$，∴$\vec{AE}=\frac23\vec{AD}$；" "\n"
        r"∴$\vec{BE}=\vec{AE}-\vec{AB}=\frac23\vec{AD}-\vec{AB}=\frac13(\vec{AB}+\vec{AC})-\vec{AB}=\frac13\vec{AC}-\frac23\vec{AB}$。故选：B。」" "\n"
        r"—— **$\vec{AD}=\frac12(\vec{AB}+\vec{AC})$、$\vec{AE}=\frac23\vec{AD}$、$\frac13\vec{AC}-\frac23\vec{AB}$ 全部与我的推导一致** ✓✓✓" "\n"
        r"**独立验算（建系）**：" "\n"
        r"取 $A=(0,0)$、$B=(2,0)$、$C=(0,2)$。则 $D$ 为 $BC$ 中点 $=(1,1)$。" "\n"
        r"$AE=2ED$ ⟹ $E$ 在 $AD$ 上且 $AE:ED=2:1$ ⟹ $E=\frac23 D=( \frac23,\frac23)$。" "\n"
        r"$\vec{BE}=E-B=(\frac23-2,\frac23)=(-\frac43,\frac23)$。" "\n"
        r"$\vec{AB}=(2,0)$、$\vec{AC}=(0,2)$。" "\n"
        r"$x\vec{AC}+y\vec{AB}=(2y,2x)=(-\frac43,\frac23)$ ⟹ $x=\frac13$、$y=-\frac23$ ✓✓✓" "\n"
        r"即 $\vec{BE}=\frac13\vec{AC}-\frac23\vec{AB}$ ✓✓✓ **与选项 B 一致**" "\n"
        r"验其余选项：A $-\frac13\vec{AC}+\frac23\vec{AB}=(\frac43,-\frac23)$ ✗；" "\n"
        r"C $\frac23\vec{AC}-\frac13\vec{AB}=(-\frac23,\frac43)$ ✗；D $\frac23\vec{AC}+\frac13\vec{AB}=(\frac23,\frac43)$ ✗" "\n"
        r"**答案 B 正确** ✓" "\n"
        r"**⭐⭐ 通法（中点 + 定比分点 ⟹ 「绕三角形」）**：" "\n"
        r"① ⭐⭐ **$\vec{AD}=\frac12(\vec{AB}+\vec{AC})$**（$D$ 为 $BC$ 中点）—— 一切中点题的起点；" "\n"
        r"② ⭐⭐ **「绕三角形」的核心：$\vec{BE}=\vec{AE}-\vec{AB}$** —— " "\n"
        r"把起点不统一的向量**统一到同一个起点 $A$**，再代入已知；" "\n"
        r"③ ⭐ **$AE=2ED$ ⟹ $\vec{AE}=\frac23\vec{AD}$**：注意是 $\frac{AE}{AD}=\frac{2}{2+1}=\frac23$，" "\n"
        r"**不是 $\frac12$** —— 这是最高频的错误；" "\n"
        r"④ ⚠ **$\vec{AB}$ 的系数是 $-\frac23$ 而非 $-\frac13$**：$\frac13\vec{AB}-\vec{AB}=-\frac23\vec{AB}$，" "\n"
        r"选项 A $(-\frac13\vec{AC}+\frac23\vec{AB})$ 是**符号全反**的结果，" "\n"
        r"选项 C 则是把 $\frac23$ 与 $\frac13$ 的位置放反 —— **两个陷阱都备好了**；" "\n"
        r"⑤ 检验：**建系代入比向量推导更快也更可靠**（本题 5 行出结果）。"
    ),
    'difficulty': 0.68,
    'topics': ['M-T-232'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-232-V1',
}

T232_V2 = {
    'type': '选择',
    'stem_text': (
        r"如图，在直角梯形 $ABCD$ 中，$AB=2AD=2DC$，$E$ 为 $BC$ 边上一点，$\vec{BC}=3\vec{EC}$，"
        r"$F$ 为 $AE$ 的中点，则 $\vec{BF}=$（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac23\vec{AB}-\dfrac13\vec{AD}$"),
        ('B', r"$\dfrac13\vec{AB}-\dfrac23\vec{AD}$"),
        ('C', r"$-\dfrac23\vec{AB}+\dfrac13\vec{AD}$"),
        ('D', r"$-\dfrac13\vec{AB}+\dfrac23\vec{AD}$"),
    ],
    'answer': 'C',
    'analysis': (
        r"以 $\vec{AB},\vec{AD}$ 为基底。$\vec{BF}=\vec{BA}+\vec{AF}=-\vec{AB}+\frac12\vec{AE}$，"
        r"而 $\vec{AE}=\vec{AD}+\vec{DE}$ 且 $\vec{DE}=\frac12\vec{AB}+\frac13\vec{CB}$，整理得 $-\frac23\vec{AB}+\frac13\vec{AD}$。"
    ),
    'solution': (
        r"由 $AB=2AD=2DC$，得 $AD=DC=\dfrac12AB$，且 $AB\parallel DC$、$AD\perp AB$。" "\n"
        r"$F$ 为 $AE$ 的中点：" "\n"
        r"$\vec{BF}=\vec{BA}+\vec{AF}=-\vec{AB}+\dfrac12\vec{AE}$。" "\n"
        r"又 $\vec{AE}=\vec{AD}+\vec{DE}$，且因 $AB\parallel DC$、$DC=\frac12AB$ 得 $\vec{DC}=\dfrac12\vec{AB}$，" "\n"
        r"故 $D$ 到 $E$ 的向量中 $\vec{DE}=\dfrac12\left(\vec{AB}+\vec{CE}\right)$（$E$ 在 $BC$ 上，$F$ 为中点展开）" "\n"
        r"更直接：由 $\vec{BC}=3\vec{EC}$ 得 $\vec{CE}=\dfrac13\vec{CB}$，" "\n"
        r"$\vec{AE}=\vec{AD}+\vec{DC}+\vec{CE}=\vec{AD}+\dfrac12\vec{AB}+\dfrac13\vec{CB}$，" "\n"
        r"而 $\vec{CB}=\vec{CD}+\vec{DA}+\vec{AB}=-\dfrac12\vec{AB}-\vec{AD}+\vec{AB}=\dfrac12\vec{AB}-\vec{AD}$。" "\n"
        r"代入：$\vec{AE}=\vec{AD}+\dfrac12\vec{AB}+\dfrac13\left(\dfrac12\vec{AB}-\vec{AD}\right)=\dfrac23\vec{AD}+\dfrac23\vec{AB}$。" "\n"
        r"故 $\vec{BF}=-\vec{AB}+\dfrac12\vec{AE}=-\vec{AB}+\dfrac13\vec{AD}+\dfrac13\vec{AB}=-\dfrac23\vec{AB}+\dfrac13\vec{AD}$。故选 C。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p200 详解：「$\vec{BF}=\vec{BA}+\vec{AF}=\vec{BA}+\frac12\vec{AE}=-\vec{AB}+\frac12(\vec{AD}+\frac12\vec{AB}+\vec{CE})$" "\n"
        r"$=-\vec{AB}+\frac12\vec{AD}+\frac14\vec{AB}+\frac16\vec{CB}=-\vec{AB}+\frac12\vec{AD}+\frac14\vec{AB}+\frac16(\vec{CD}+\vec{DA}+\vec{AB})$" "\n"
        r"$=-\vec{AB}+\frac12\vec{AD}+\frac14\vec{AB}+\frac16(-\frac12\vec{AB}-\vec{AD}+\vec{AB})=-\vec{AB}+\frac12\vec{AD}+\frac14\vec{AB}+\frac1{12}\vec{AB}-\frac16\vec{AD}$" "\n"
        r"$=-\frac23\vec{AB}+\frac13\vec{AD}$。故选：C。」" "\n"
        r"—— **$\vec{CE}=\frac13\vec{CB}$、$\vec{CD}=-\frac12\vec{AB}$、最终 $-\frac23\vec{AB}+\frac13\vec{AD}$ 全部与我的推导一致** ✓✓✓" "\n"
        r"**独立验算（建系，完全独立）**：" "\n"
        r"取 $AB=2$，则 $AD=DC=1$。建系 $A=(0,0)$、$B=(2,0)$、$D=(0,1)$、$C=(1,1)$。" "\n"
        r"（验：$AB=2$ ✓、$AD=1$ ✓、$DC=1$ ✓、$AB\parallel DC$ ✓、$AD\perp AB$ ✓）" "\n"
        r"由 $\vec{BC}=3\vec{EC}$ 得 $\vec{EC}=\frac13\vec{BC}$ ⟹ $E=C+\frac13(B-C)=(1,1)+\frac13(1,-1)=(\frac43,\frac23)$。" "\n"
        r"$F$ 为 $AE$ 中点：$F=(\frac23,\frac13)$。" "\n"
        r"$\vec{BF}=F-B=(\frac23-2,\frac13-0)=(-\frac43,\frac13)$。" "\n"
        r"$\vec{AB}=(2,0)$、$\vec{AD}=(0,1)$。" "\n"
        r"$x\vec{AB}+y\vec{AD}=(2x,y)=(-\frac43,\frac13)$ ⟹ $x=-\frac23$、$y=\frac13$ ✓✓✓" "\n"
        r"即 $\vec{BF}=-\frac23\vec{AB}+\frac13\vec{AD}$ ✓✓✓ **与选项 C 完全一致**" "\n"
        r"验其余：A $\frac23\vec{AB}-\frac13\vec{AD}=(\frac43,-\frac13)$ ✗；B $\frac13\vec{AB}-\frac23\vec{AD}=(\frac23,-\frac23)$ ✗；" "\n"
        r"D $-\frac13\vec{AB}+\frac23\vec{AD}=(-\frac23,\frac23)$ ✗" "\n"
        r"**答案 C 正确** ✓" "\n"
        r"**⭐⭐ 通法（梯形 + 定比分点 ⟹ 建系最快）**：" "\n"
        r"① ⭐⭐ **直角梯形给的是「现成的坐标系」**：$AD\perp AB$ 且 $AB\parallel DC$ ⟹ " "\n"
        r"直接以 $A$ 为原点、$AB$ 为 $x$ 轴、$AD$ 为 $y$ 轴 —— **比向量绕行快 3 倍且不会错**；" "\n"
        r"② ⭐ **$\vec{BC}=3\vec{EC}$ 读成分点**：$E=C+\frac13(B-C)$，$E$ 距 $C$ 为 $BC$ 的 $\frac13$；" "\n"
        r"③ ⭐ **$\vec{BF}=\vec{BA}+\vec{AF}$** —— 「绕」到 $A$ 点，再用中点公式 $\vec{AF}=\frac12\vec{AE}$；" "\n"
        r"④ ⚠ **$\vec{CD}=-\frac12\vec{AB}$ 别写成 $+\frac12$**：$\vec{DC}=+\frac12\vec{AB}$ 但 $\vec{CD}$ 反向。" "\n"
        r"本题中间要的是 $\vec{CB}$ 而非 $\vec{BC}$，**方向搞反系数就全错**；" "\n"
        r"⑤ ⚠ **选项设计**：A 与 C 互为相反数，B 与 D 也互为相反数 —— " "\n"
        r"**命题人用「符号相反」筛掉了一半考生**，所以最后一步的正负号必须验；" "\n"
        r"⑥ 检验：**建系算出坐标后，把四个选项都代入比一比**（只有 C 给 $(-\frac43,\frac13)$ ✓）。"
    ),
    'difficulty': 0.72,
    'topics': ['M-T-232'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-232-V2',
}

T233_V1 = {
    'type': '选择',
    'stem_text': (
        r"如图，正方形 $ABCD$ 中，$M$、$N$ 分别是 $BC$、$CD$ 的中点，若 $\vec{AC}=\lambda\vec{AM}+\mu\vec{BN}$，则 $\lambda+\mu=$（　　）"
    ),
    'opts': [
        ('A', r"$2$"),
        ('B', r"$\dfrac83$"),
        ('C', r"$\dfrac65$"),
        ('D', r"$\dfrac85$"),
    ],
    'answer': 'D',
    'analysis': (
        r"以 $\vec{AB},\vec{BC}$ 为基底：$\vec{AM}=\vec{AB}+\frac12\vec{BC}$，$\vec{BN}=\vec{BC}-\frac12\vec{AB}$。"
        r"比较系数得 $\lambda-\frac\mu2=1$、$\mu+\frac\lambda2=1$，解出 $\lambda=\frac65$、$\mu=\frac25$，和为 $\frac85$。"
    ),
    'solution': (
        r"取 $\vec{AB},\vec{BC}$ 为一组基底。" "\n"
        r"$M$ 为 $BC$ 中点：$\vec{AM}=\vec{AB}+\vec{BM}=\vec{AB}+\dfrac12\vec{BC}$。" "\n"
        r"$N$ 为 $CD$ 中点，且 $\vec{CD}=-\vec{AB}$：" "\n"
        r"$\vec{BN}=\vec{BC}+\vec{CN}=\vec{BC}+\dfrac12\vec{CD}=\vec{BC}-\dfrac12\vec{AB}$。" "\n"
        r"于是" "\n"
        r"$\vec{AC}=\lambda\vec{AM}+\mu\vec{BN}=\lambda\left(\vec{AB}+\dfrac12\vec{BC}\right)+\mu\left(\vec{BC}-\dfrac12\vec{AB}\right)$" "\n"
        r"$=\left(\lambda-\dfrac\mu2\right)\vec{AB}+\left(\dfrac\lambda2+\mu\right)\vec{BC}$。" "\n"
        r"又 $\vec{AC}=\vec{AB}+\vec{BC}$，且 $\vec{AB},\vec{BC}$ 不共线，比较系数：" "\n"
        r"$\begin{cases}\lambda-\dfrac\mu2=1\\[6pt] \dfrac\lambda2+\mu=1\end{cases}\Rightarrow\begin{cases}2\lambda-\mu=2\\[2pt] \lambda+2\mu=2\end{cases}"
        r"\Rightarrow\lambda=\dfrac65,\ \mu=\dfrac25$。" "\n"
        r"故 $\lambda+\mu=\dfrac65+\dfrac25=\dfrac85$。故选 D。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p201 详解：「取向量 $\vec{AB},\vec{BC}$ 作为一组基底，则有 $\vec{AM}=\vec{AB}+\vec{BM}=\vec{AB}+\frac12\vec{BC}$，" "\n"
        r"$\vec{BN}=\vec{BC}+\vec{CN}=\vec{BC}-\frac12\vec{AB}$，所以 $\vec{AC}=\lambda\vec{AM}+\mu\vec{BN}=(\lambda-\frac\mu2)\vec{AB}+(\mu+\frac\lambda2)\vec{BC}$，" "\n"
        r"又 $\vec{AC}=\vec{AB}+\vec{BC}$，所以 $\lambda-\frac\mu2=1$，$\mu+\frac\lambda2=1$，即 $\lambda=\frac65$，$\mu=\frac25$，$\lambda+\mu=\frac85$。」" "\n"
        r"—— **$\vec{AM}=\vec{AB}+\frac12\vec{BC}$、$\vec{BN}=\vec{BC}-\frac12\vec{AB}$、$\lambda=\frac65$、$\mu=\frac25$、$\lambda+\mu=\frac85$ 全部与我的推导一致** ✓✓✓" "\n"
        r"**独立验算（建系，完全独立）**：" "\n"
        r"取正方形边长 $2$，$A=(0,0)$、$B=(2,0)$、$C=(2,2)$、$D=(0,2)$。" "\n"
        r"$M$ 为 $BC$ 中点 $=(2,1)$；$N$ 为 $CD$ 中点 $=(1,2)$。" "\n"
        r"$\vec{AC}=(2,2)$、$\vec{AM}=(2,1)$、$\vec{BN}=N-B=(-1,2)$。" "\n"
        r"$\lambda(2,1)+\mu(-1,2)=(2,2)$ ⟹ $2\lambda-\mu=2$、$\lambda+2\mu=2$。" "\n"
        r"解：第一式 $\times2$ 加第二式：$5\lambda=6$ ⟹ $\lambda=\frac65$；代回 $\mu=2\lambda-2=\frac{12}5-2=\frac25$ ✓✓✓" "\n"
        r"验：$\frac65(2,1)+\frac25(-1,2)=(\frac{12}5-\frac25,\frac65+\frac45)=(\frac{10}5,\frac{10}5)=(2,2)$ ✓✓✓ **恰为 $\vec{AC}$**" "\n"
        r"$\lambda+\mu=\frac65+\frac25=\frac85=1.6$ ✓✓✓" "\n"
        r"**答案 D 正确** ✓" "\n"
        r"**⭐⭐ 通法（平面向量基本定理 ⟹ 比较系数）**：" "\n"
        r"① ⭐⭐ **选基底的原则：让所有向量都能「绕」出来**。本题选 $\vec{AB},\vec{BC}$（不共线）而非 $\vec{AB},\vec{AD}$，" "\n"
        r"因为 $\vec{BN}$ 用 $\vec{BC}$ 表达只需一步；" "\n"
        r"② ⭐⭐ **关键一步是 $\vec{CN}=-\frac12\vec{AB}$**：$N$ 是 $CD$ 中点，而 $\vec{CD}=-\vec{AB}$（正方形对边反向）——" "\n"
        r"**写成 $+\frac12\vec{AB}$ 就会解出 $\lambda=\frac25,\mu=\frac65$**，和仍是 $\frac85$，但" "\n"
        r"若题目问 $\lambda$ 或 $\mu$ 单独的值就会错；" "\n"
        r"③ ⭐ **比较系数 ⟹ 二元一次方程组**：基底不共线是使用前提，" "\n"
        r"本题中 $\vec{AB}\perp\vec{BC}$ 更强，直接**建系当坐标算**也完全等价；" "\n"
        r"④ ⚠ **选项 B $\frac83$ 与 C $\frac65$ 是干扰**：$\frac65$ 恰是 $\lambda$ 的值 —— " "\n"
        r"**命题人把中间量放进选项**，若题目问的是 $\lambda$ 就会有人误选 C；" "\n"
        r"⑤ 检验：**解完把 $\lambda,\mu$ 代回原式验一次**（得 $(2,2)=\vec{AC}$ ✓）。"
    ),
    'difficulty': 0.7,
    'topics': ['M-T-233'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-233-V1',
}

T233_V3 = {
    'type': '选择',
    'stem_text': (
        r"如图，$\triangle ABC$ 中，$AD=DB$，$AE=EC$，$CD$ 与 $BE$ 交于 $F$，设 $\vec{AB}=\vec a$，$\vec{AC}=\vec b$，"
        r"$\vec{AF}=x\vec a+y\vec b$，则 $(x,y)$ 为（　　）"
    ),
    'opts': [
        ('A', r"$\left(\dfrac13,\dfrac13\right)$"),
        ('B', r"$\left(\dfrac23,\dfrac23\right)$"),
        ('C', r"$\left(\dfrac12,\dfrac12\right)$"),
        ('D', r"$\left(\dfrac23,\dfrac12\right)$"),
    ],
    'answer': 'A',
    'analysis': (
        r"$CD$、$BE$ 是两条中线，交点 $F$ 即重心。$\vec{AF}=\frac23\vec{AM}=\frac23\cdot\frac12(\vec{AB}+\vec{AC})=\frac13(\vec a+\vec b)$。"
    ),
    'solution': (
        r"因 $AD=DB$、$AE=EC$，故 $CD$ 与 $BE$ 是 $\triangle ABC$ 的**两条中线**，其交点 $F$ 即 $\triangle ABC$ 的**重心**。" "\n"
        r"延长 $AF$ 交 $BC$ 于 $M$，则 $M$ 为 $BC$ 中点，且重心分中线为 $AF:FM=2:1$，故" "\n"
        r"$\vec{AF}=\dfrac23\vec{AM}$。" "\n"
        r"又由中点向量公式 $\vec{AM}=\dfrac12\left(\vec{AB}+\vec{AC}\right)=\dfrac12(\vec a+\vec b)$，于是" "\n"
        r"$\vec{AF}=\dfrac23\cdot\dfrac12(\vec a+\vec b)=\dfrac13\vec a+\dfrac13\vec b$。" "\n"
        r"与 $\vec{AF}=x\vec a+y\vec b$ 比较得 $x=\dfrac13$、$y=\dfrac13$。故选 A。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p201 详解：「延长 $AF$ 交 $BC$ 于点 $M$；" "\n"
        r"∵$AD=DB$，$AE=EC$，$CD$ 与 $BE$ 交于 $F$，∴点 $F$ 是 $\triangle ABC$ 的重心，∴$\vec{AF}=\frac23\vec{AM}$，" "\n"
        r"$\vec{AM}=\frac12(\vec{AB}+\vec{AC})$，∴$\vec{AF}=\frac23\vec{AM}=\frac23\times\frac12(\vec{AB}+\vec{AC})=\frac13(\vec{AB}+\vec{AC})=\frac13\vec a+\frac13\vec b$。" "\n"
        r"又∵$\vec{AF}=x\vec a+y\vec b$ ∴$x=\frac13$，$y=\frac13$；故答案选 A」" "\n"
        r"—— **$F$ 是重心、$\vec{AF}=\frac23\vec{AM}$、$\vec{AM}=\frac12(\vec{AB}+\vec{AC})$、$(\frac13,\frac13)$ 全部与我的推导一致** ✓✓✓" "\n"
        r"**独立验算（建系 + 求交点，完全独立）**：" "\n"
        r"取 $A=(0,0)$、$B=(2,0)$、$C=(0,2)$。" "\n"
        r"$D$ 为 $AB$ 中点 $=(1,0)$；$E$ 为 $AC$ 中点 $=(0,1)$。" "\n"
        r"直线 $CD$：过 $(0,2)$ 与 $(1,0)$，参数式 $(t,2-2t)$。" "\n"
        r"直线 $BE$：过 $(2,0)$ 与 $(0,1)$，参数式 $(2-2s,s)$。" "\n"
        r"联立：$t=2-2s$、$2-2t=s$ ⟹ 代入 $t$：$2-2(2-2s)=s$ ⟹ $2-4+4s=s$ ⟹ $3s=2$ ⟹ $s=\frac23$、$t=\frac23$。" "\n"
        r"$F=(\frac23,2-\frac43)=(\frac23,\frac23)$ ✓✓✓" "\n"
        r"$\vec{AF}=(\frac23,\frac23)$；$\vec a=\vec{AB}=(2,0)$、$\vec b=\vec{AC}=(0,2)$。" "\n"
        r"$x\vec a+y\vec b=(2x,2y)=(\frac23,\frac23)$ ⟹ $x=y=\frac13$ ✓✓✓" "\n"
        r"验重心性质：$\vec{AF}=(\frac23,\frac23)$，重心应为 $\frac{A+B+C}3=(\frac23,\frac23)$ ✓✓✓ **完全一致**" "\n"
        r"验其余选项：B $(\frac23,\frac23)$ 给 $\vec{AF}=(\frac43,\frac43)$ ✗（那是 $2\vec{AF}$）；" "\n"
        r"C $(\frac12,\frac12)$ 给 $(1,1)$ ✗（那是 $M$ 点）；D $(\frac23,\frac12)$ 给 $(\frac43,1)$ ✗" "\n"
        r"**答案 A 正确** ✓" "\n"
        r"**⭐⭐ 通法（重心 ⟹ 系数各 $\frac13$）**：" "\n"
        r"① ⭐⭐ **重心向量式 $\vec{OG}=\frac13(\vec{OA}+\vec{OB}+\vec{OC})$**（$O$ 任意）。取 $O=A$ 即" "\n"
        r"$\vec{AG}=\frac13(\vec{AB}+\vec{AC})$ —— **系数各 $\frac13$，与三角形形状无关**；" "\n"
        r"② ⭐ 推导链：**两条中线交点 = 重心** ⟹ $\vec{AF}=\frac23\vec{AM}$ ⟹ $\vec{AM}=\frac12(\vec{AB}+\vec{AC})$ ⟹ $\frac13(\vec a+\vec b)$；" "\n"
        r"③ ⭐⭐ **$\frac23\times\frac12=\frac13$** 这个乘积是本题全部计算 —— 记住「重心 = $\frac13,\frac13,\frac13$」可秒答同类题；" "\n"
        r"④ ⚠ **选项 B $(\frac23,\frac23)$ 是最大的坑**：$\frac23$ 是「重心分中线的比」，" "\n"
        r"**不是** $\vec{AF}$ 在基底 $\vec{AB},\vec{AC}$ 下的系数 —— 两者差一个 $\frac12$；" "\n"
        r"⑤ ⚠ **选项 C $(\frac12,\frac12)$ 是 $M$（$BC$ 中点）**，若把 $F$ 误当 $M$ 就会选它；" "\n"
        r"⑥ 检验：**建系求两直线交点**是最硬的验证（本题得 $F=(\frac23,\frac23)=$ 重心 ✓）。"
    ),
    'difficulty': 0.7,
    'topics': ['M-T-233'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-233-V3',
}

T283_V1 = {
    'type': '选择',
    'stem_text': (
        r"如图，在正方体 $ABCD-A_{1}B_{1}C_{1}D_{1}$ 中，$M$、$N$、$P$ 分别是棱 $C_{1}D_{1}$、$AA_{1}$、$BC$ 的中点，"
        r"则经过 $M$、$N$、$P$ 的平面与正方体 $ABCD-A_{1}B_{1}C_{1}D_{1}$ 相交形成的截面是一个（　　）"
    ),
    'opts': [
        ('A', r"三角形"),
        ('B', r"平面四边形"),
        ('C', r"平面五边形"),
        ('D', r"平面六边形"),
    ],
    'answer': 'D',
    'analysis': (
        r"建系求得平面 $x-y+z=\frac12$，逐面求交得 6 个顶点（分别在 $AB$、$BC$、$CC_1$、$C_1D_1$、$A_1D_1$、$AA_1$ 上），故为六边形。"
    ),
    'solution': (
        r"以 $A$ 为原点，$\vec{AB},\vec{AD},\vec{AA_{1}}$ 为 $x,y,z$ 轴，取棱长为 $1$。" "\n"
        r"则 $M\left(\dfrac12,1,1\right)$、$N\left(0,0,\dfrac12\right)$、$P\left(1,\dfrac12,0\right)$。" "\n"
        r"设平面方程 $ax+by+cz=d$，代入三点：" "\n"
        r"$\begin{cases}\frac12a+b+c=d\\[2pt] \frac12c=d\\[2pt] a+\frac12b=d\end{cases}$，取 $c=2$ 得 $d=1$、$b=-2$、$a=2$，" "\n"
        r"即平面为 $2x-2y+2z=1$，化简 $x-y+z=\dfrac12$。" "\n"
        r"**逐面求交**（$f=x-y+z-\frac12$）：" "\n"
        r"| 面 | 交线端点 | 所在棱 |" "\n"
        r"|---|---|---|" "\n"
        r"| $z=0$ | $(\frac12,0,0)$、$(1,\frac12,0)$ | $AB$、$BC$（$P$） |" "\n"
        r"| $x=1$ | $(1,\frac12,0)$、$(1,1,\frac12)$ | $BC$（$P$）、$CC_{1}$ |" "\n"
        r"| $y=1$ | $(1,1,\frac12)$、$(\frac12,1,1)$ | $CC_{1}$、$C_{1}D_{1}$（$M$） |" "\n"
        r"| $z=1$ | $(\frac12,1,1)$、$(0,\frac12,1)$ | $C_{1}D_{1}$（$M$）、$A_{1}D_{1}$ |" "\n"
        r"| $x=0$ | $(0,\frac12,1)$、$(0,0,\frac12)$ | $A_{1}D_{1}$、$AA_{1}$（$N$） |" "\n"
        r"| $y=0$ | $(0,0,\frac12)$、$(\frac12,0,0)$ | $AA_{1}$（$N$）、$AB$ |" "\n"
        r"共得 **$6$ 个顶点**：$(\frac12,0,0)$、$(1,\frac12,0)$、$(1,1,\frac12)$、$(\frac12,1,1)$、$(0,\frac12,1)$、$(0,0,\frac12)$，" "\n"
        r"顺次连接即为**平面六边形**。故选 D。"
    ),
    'review': (
        r"★ 题干、答案完整 ✓。**详解由我独立用坐标法重建**（原书详解用平行四边形论证，较繁）：" "\n"
        r"原书 p241 详解：「如图，分别取 $A_1D_1$、$AB$、$C_1C$ 的中点 $F$、$H$、$E$，连接 $MF$、$FN$、$NH$、$HP$、$PE$、$EM$…" "\n"
        r"所以 $H$、$P$、$E$、$M$、$F$、$N$ 六点共面，平面六边形 $HPEMFN$ 即为…截面，故选：D。」" "\n"
        r"—— **六个顶点、六边形、答案 D 与我的坐标法结论一致** ✓✓✓" "\n"
        r"**独立验算（坐标法穷举 6 个面，完全独立）**：" "\n"
        r"① **平面方程**：验三点。" "\n"
        r"$M(\frac12,1,1)$：$\frac12-1+1=\frac12$ ✓；$N(0,0,\frac12)$：$0-0+\frac12=\frac12$ ✓；$P(1,\frac12,0)$：$1-\frac12+0=\frac12$ ✓ ✓✓✓" "\n"
        r"② **$z=0$ 面**：$x-y=\frac12$ ⟹ 线段从 $(\frac12,0,0)$ 到 $(1,\frac12,0)$。" "\n"
        r"验 $(\frac12,0,0)$ 在棱 $AB$（$y=0,z=0$）上 ✓；$(1,\frac12,0)$ 即 $P$ 在棱 $BC$（$x=1,z=0$）上 ✓✓✓" "\n"
        r"③ **$x=1$ 面**：$1-y+z=\frac12$ ⟹ $z=y-\frac12$。$y$ 从 $\frac12$ 到 $1$ ⟹ 从 $(1,\frac12,0)$ 到 $(1,1,\frac12)$。" "\n"
        r"验 $(1,1,\frac12)$ 在棱 $CC_1$（$x=1,y=1$）上，且 $z=\frac12\in[0,1]$ ✓✓✓" "\n"
        r"④ **$y=1$ 面**：$x-1+z=\frac12$ ⟹ $x+z=\frac32$。从 $(1,1,\frac12)$ 到 $(\frac12,1,1)$。" "\n"
        r"验 $(\frac12,1,1)$ 即 $M$ 在棱 $C_1D_1$（$y=1,z=1$）上 ✓✓✓" "\n"
        r"⑤ **$z=1$ 面**：$x-y+1=\frac12$ ⟹ $y=x+\frac12$。$x$ 从 $0$ 到 $\frac12$ ⟹ 从 $(0,\frac12,1)$ 到 $(\frac12,1,1)$。" "\n"
        r"验 $(0,\frac12,1)$ 在棱 $A_1D_1$（$x=0,z=1$）上 ✓✓✓" "\n"
        r"⑥ **$x=0$ 面**：$-y+z=\frac12$ ⟹ $z=y+\frac12$。$y$ 从 $0$ 到 $\frac12$ ⟹ 从 $(0,0,\frac12)$ 到 $(0,\frac12,1)$。" "\n"
        r"验 $(0,0,\frac12)$ 即 $N$ 在棱 $AA_1$（$x=0,y=0$）上 ✓✓✓" "\n"
        r"⑦ **$y=0$ 面**：$x+z=\frac12$。从 $(\frac12,0,0)$ 到 $(0,0,\frac12)$ ✓✓✓ **闭合**" "\n"
        r"⑧ **六个顶点互不相同且顺次共面** ⟹ **六边形** ✓✓✓" "\n"
        r"⑨ **排除其他选项**：截面不是三角形/四边形/五边形 —— 由上面穷举，六个面都有交线段，" "\n"
        r"且 $6$ 个顶点两两不同，故必为六边形 ✓✓✓" "\n"
        r"**答案 D 正确** ✓" "\n"
        r"**⭐⭐ 通法（截面形状 ⟹ 坐标法穷举 6 面）**：" "\n"
        r"① ⭐⭐ **建系 → 平面方程 → 逐面求交**，是判断截面边数的**万能且可验证**的方法，" "\n"
        r"**比「找平行线、证共面」的纯几何论证可靠得多**；" "\n"
        r"② ⭐⭐ **每个面至多贡献一条线段**，截面边数 = 与平面相交的面的个数（扣除退化情形）；" "\n"
        r"③ ⭐ **求交线端点时固定一个坐标为 $0$ 或 $1$**，解二元一次方程，" "\n"
        r"再检查另一坐标是否落在 $[0,1]$ 内 —— **这一步是判断是否真与棱相交的关键**；" "\n"
        r"④ ⚠ **交点可能落在棱的延长线上**：必须验证坐标在 $[0,1]$，**越界则该面无交点**；" "\n"
        r"⑤ ⚠ **顶点可能重合**（平面过顶点时），本题 6 个顶点互异，若重合边数会减少；" "\n"
        r"⑥ 检验：**把求出的每个顶点代回平面方程**（本题 6 个都给 $\frac12$ ✓），并**检查闭合**（首尾相接 ✓）。"
    ),
    'difficulty': 0.82,
    'topics': ['M-T-283'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-283-V1',
}

T283_V2 = {
    'type': '选择',
    'stem_text': (
        r"如图，在正方体 $ABCD-A_{1}B_{1}C_{1}D_{1}$ 中，$E$ 是棱 $CC_{1}$ 的中点，则过 $A$、$D_{1}$、$E$ 三点的截面过（　　）"
    ),
    'opts': [
        ('A', r"$AB$ 中点"),
        ('B', r"$BC$ 中点"),
        ('C', r"$CD$ 中点"),
        ('D', r"$BB_{1}$ 中点"),
    ],
    'answer': 'B',
    'analysis': (
        r"建系得平面 $-x+2y-2z=0$。$BC$ 中点 $(1,\frac12,0)$ 代入成立；其余三个中点代入均不成立。"
    ),
    'solution': (
        r"以 $A$ 为原点，$\vec{AB},\vec{AD},\vec{AA_{1}}$ 为 $x,y,z$ 轴，取棱长为 $1$。" "\n"
        r"$A(0,0,0)$、$D_{1}(0,1,1)$、$E\left(1,1,\dfrac12\right)$。" "\n"
        r"法向量 $\vec{n}=\vec{AD_{1}}\times\vec{AE}=(0,1,1)\times\left(1,1,\dfrac12\right)$" "\n"
        r"$=\left(1\cdot\dfrac12-1\cdot1,\;1\cdot1-0\cdot\dfrac12,\;0\cdot1-1\cdot1\right)=\left(-\dfrac12,1,-1\right)$。" "\n"
        r"取 $\vec n=(-1,2,-2)$，平面过原点 $A$，故方程为 $-x+2y-2z=0$。" "\n"
        r"**逐项检验**：" "\n"
        r"$AB$ 中点 $\left(\dfrac12,0,0\right)$：$-\dfrac12+0-0=-\dfrac12\ne0$ ✗" "\n"
        r"$BC$ 中点 $\left(1,\dfrac12,0\right)$：$-1+1-0=0$ ✓" "\n"
        r"$CD$ 中点 $\left(\dfrac12,1,0\right)$：$-\dfrac12+2-0=\dfrac32\ne0$ ✗" "\n"
        r"$BB_{1}$ 中点 $\left(1,0,\dfrac12\right)$：$-1+0-1=-2\ne0$ ✗" "\n"
        r"故选 B。"
    ),
    'review': (
        r"★ 题干、答案完整 ✓，原书详解极简：「取 $BC$ 的中点 $F$，连接 $EF$、$AF$，则 $EF\parallel AD_1$，所以 $F$ 在截面上，故选：B」" "\n"
        r"—— **$EF\parallel AD_1$ ⟹ $F$ 在截面上** ✓，我用坐标法独立验证如下。" "\n"
        r"**独立验算（坐标法，完全独立）**：" "\n"
        r"① **$E=(1,1,\frac12)$**：$E$ 是 $CC_1$ 中点，$C=(1,1,0)$、$C_1=(1,1,1)$ ⟹ $E=(1,1,\frac12)$ ✓✓✓" "\n"
        r"② **法向量**：$\vec{AD_1}=(0,1,1)$、$\vec{AE}=(1,1,\frac12)$。" "\n"
        r"叉积 $=(1\cdot\frac12-1\cdot1,\;1\cdot1-0\cdot\frac12,\;0\cdot1-1\cdot1)=(-\frac12,1,-1)$ ✓✓✓" "\n"
        r"③ **平面方程**：过 $A(0,0,0)$ ⟹ $-\frac12x+y-z=0$，即 $-x+2y-2z=0$ ✓✓✓" "\n"
        r"验 $D_1(0,1,1)$：$0+2-2=0$ ✓；验 $E(1,1,\frac12)$：$-1+2-1=0$ ✓ ✓✓✓" "\n"
        r"④ **$BC$ 中点 $F=(1,\frac12,0)$**：$-1+2\cdot\frac12-0=-1+1=0$ ✓✓✓ **在平面上**" "\n"
        r"⑤ **平行验证**（详解的思路）：$\vec{EF}=F-E=(0,-\frac12,-\frac12)$；$\vec{AD_1}=(0,1,1)$。" "\n"
        r"$\vec{EF}=-\frac12\vec{AD_1}$ ✓✓✓ **确为平行**，故 $F$ 在平面 $AD_1E$ 上" "\n"
        r"⑥ **其余三个中点全部排除**：" "\n"
        r"$AB$ 中点 $(\frac12,0,0)$：$-\frac12\ne0$ ✗；$CD$ 中点 $(\frac12,1,0)$：$\frac32\ne0$ ✗；" "\n"
        r"$BB_1$ 中点 $(1,0,\frac12)$：$-2\ne0$ ✗ ✓✓✓" "\n"
        r"**答案 B 正确** ✓" "\n"
        r"**⭐⭐ 通法（判断某点是否在截面上）**：" "\n"
        r"① ⭐⭐ **两条等价思路**：（a）建系求平面方程，代入点检验；（b）证明该点与平面上两点连线**平行于**平面内某条线。" "\n"
        r"**坐标法更机械、更不容易错**，特别适合四个选项逐个排除；" "\n"
        r"② ⭐ **「$EF\parallel AD_1$」这一类证法的本质是**：$E$、$F$ 都在平面上 ⟺ $\vec{EF}$ 与平面内两方向共面。" "\n"
        r"本题因 $E$ 已知在平面上，只需 $\vec{EF}\parallel\vec{AD_1}$ 即可；" "\n"
        r"③ ⚠ **叉积的分量顺序别搞错**：$\vec u\times\vec v=(u_2v_3-u_3v_2,\;u_3v_1-u_1v_3,\;u_1v_2-u_2v_1)$，" "\n"
        r"**中间项是 $u_3v_1-u_1v_3$（不是 $u_1v_3-u_3v_1$）** —— 弄反法向量就全反（不过判「是否为 $0$」不受影响）；" "\n"
        r"④ ⭐ **选项设计很有规律**：四个中点分布在 $AB$、$BC$、$CD$、$BB_1$ 四条不同棱上，" "\n"
        r"**坐标法四个代入一次全判完**，比几何论证省事；" "\n"
        r"⑤ 检验：**把三个已知点都代回平面方程验一次**（$A$、$D_1$、$E$ 都给 $0$ ✓）。"
    ),
    'difficulty': 0.7,
    'topics': ['M-T-283'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-283-V2',
}

T279_V2 = {
    'type': '选择',
    'stem_text': (
        r"如图，在棱长为 $4$ 的正方体 $ABCD-A'B'C'D'$ 中，$E$、$F$ 分别是 $AD$、$A'D'$ 的中点，"
        r"长为 $2$ 的线段 $MN$ 的一个端点 $M$ 在线段 $EF$ 上运动，另一个端点 $N$ 在底面 $A'B'C'D'$ 上运动，"
        r"则线段 $MN$ 的中点 $P$ 的轨迹（曲面）与正方体（各个面）所围成的几何体的体积为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac{4\pi}3$"),
        ('B', r"$\dfrac{2\pi}3$"),
        ('C', r"$\dfrac\pi6$"),
        ('D', r"$\dfrac\pi3$"),
    ],
    'answer': 'D',
    'analysis': (
        r"$EF\perp$ 底面，$MF\perp FN$，故 $\mathrm{Rt}\triangle MFN$ 中 $FP=\frac12MN=1$，"
        r"$P$ 的轨迹是以 $F$ 为球心、半径 $1$ 的球面，在正方体内只取 $\frac14$，体积 $=\frac14\cdot\frac43\pi=\frac\pi3$。"
    ),
    'solution': (
        r"因 $AD\parallel A'D'$ 且 $AD=A'D'$，$E$、$F$ 分别为 $AD$、$A'D'$ 的中点，" "\n"
        r"故 $AE\parallel A'F$ 且 $AE=A'F$，四边形 $AA'FE$ 为平行四边形，于是 $EF\parallel AA'$ 且 $EF=AA'=4$。" "\n"
        r"因 $AA'\perp$ 平面 $A'B'C'D'$，故 $EF\perp$ 平面 $A'B'C'D'$。" "\n"
        r"又 $M\in EF$，所以 $MF\perp$ 平面 $A'B'C'D'$，而 $FN\subset$ 平面 $A'B'C'D'$，故 $MF\perp FN$。" "\n"
        r"在 $\mathrm{Rt}\triangle MFN$ 中，$P$ 为斜边 $MN$ 的中点，故" "\n"
        r"$FP=\dfrac12MN=\dfrac12\times2=1$。" "\n"
        r"因此 $P$ 的轨迹是以 $F$ 为球心、半径 $1$ 的球面。" "\n"
        r"因 $F$ 在正方体的棱 $A'D'$ 上（该棱处两个面夹角为 $90^\circ$），球面在正方体内的部分为整个球的 $\dfrac14$，" "\n"
        r"故所围几何体体积 $V=\dfrac14\times\dfrac43\pi\times1^{3}=\dfrac\pi3$。故选 D。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p242 详解：「连接 $PF$、$NF$，因为 $AD\parallel A'D'$，$AD=A'D'$，且 $E$、$F$ 分别为 $AD$、$A'D'$ 的中点，" "\n"
        r"故 $AE\parallel A'F$ 且 $AE=A'F$，所以四边形 $AA'FE$ 为平行四边形，故 $EF\parallel AA'$ 且 $EF=AA'=4$，" "\n"
        r"∵$AA'\perp$ 平面 $A'B'C'D'$，则 $EF\perp$ 平面 $A'B'C'D'$，因为 $FN\subset$ 平面 $A'B'C'D'$，所以 $EF\perp FN$，" "\n"
        r"∵$P$ 为 $MN$ 的中点，故 $FP=\frac12MN=1$，所以点 $P$ 的轨迹是以点 $F$ 为球心，半径长为 $1$ 的球面，" "\n"
        r"所以…所围成的几何体为球 $F$ 的 $\frac14$，故所求几何体的体积为 $V=\frac14\times\frac43\pi\times1^{3}=\frac\pi3$。故选：D。」" "\n"
        r"—— **$EF=4$、$EF\perp$ 底面、$FP=\frac12MN=1$、球心 $F$ 半径 $1$、取 $\frac14$、$V=\frac\pi3$ 全部与我的推导一致** ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **$EF\parallel AA'$ 且 $EF=4$**：$E$、$F$ 是两条平行且相等线段 $AD$、$A'D'$ 的中点，" "\n"
        r"故 $AE\parallel A'F$、$AE=A'F=\frac{AD}2=2$ ⟹ $AA'FE$ 是平行四边形 ⟹ $EF=AA'=4$ ✓✓✓" "\n"
        r"② **$EF\perp$ 底面 $A'B'C'D'$**：$AA'\perp$ 底面，$EF\parallel AA'$ ✓✓✓" "\n"
        r"③ **$MF\perp FN$**：$M\in EF$ ⟹ $MF$ 在直线 $EF$ 上 ⟹ $MF\perp$ 底面；$N$ 在底面上 ⟹ $FN\subset$ 底面 ✓✓✓" "\n"
        r"④ **$FP=\frac12MN=1$**：直角三角形斜边中点到三顶点等距 ⟹ $FP=FM'?$" "\n"
        r"严谨说：$\mathrm{Rt}\triangle MFN$ 中 $\angle MFN=90^\circ$，$P$ 为斜边 $MN$ 中点 ⟹ $FP=\frac12MN=\frac12\cdot2=1$ ✓✓✓" "\n"
        r"⑤ **轨迹是球面**：$FP$ 恒为 $1$，$F$ 固定 ⟹ $P$ 在半径 $1$ 的球面上 ✓✓✓" "\n"
        r"（反之球面上每点都能取到吗？$M$ 在线段 $EF$ 上、$N$ 在底面上，这限制了范围 —— " "\n"
        r"但 $F$ 是 $A'D'$ 中点，位于底面边界上，故只有**朝向正方体内部的 $\frac14$ 球**可达 ✓✓✓）" "\n"
        r"⑥ **$V=\frac14\cdot\frac43\pi\cdot1^3=\frac\pi3\approx1.0472$** ✓✓✓" "\n"
        r"⑦ **选项排除**：A $\frac{4\pi}3$ 是**整球**；B $\frac{2\pi}3$ 是半球；C $\frac\pi6$ 是 $\frac18$ 球 —— " "\n"
        r"**三个干扰项分别对应 $\frac11$、$\frac12$、$\frac18$**，命题人把「取几分之几」作为唯一考点 ✓✓✓" "\n"
        r"**答案 D 正确** ✓" "\n"
        r"**⭐⭐ 通法（动点轨迹 ⟹ 球面）**：" "\n"
        r"① ⭐⭐ **识别「定长 + 中点到定点」模型**：一条定长线段两端各在一条垂直（或一般）直线上滑动时，" "\n"
        r"**直角三角形斜边中点到直角顶点距离恒为定长的一半** ⟹ 轨迹是球面/圆弧；" "\n"
        r"② ⭐⭐ **关键一步是证 $MF\perp FN$**：由「$EF\perp$ 底面」+「$N$ 在底面上」得到，" "\n"
        r"**线面垂直 ⟹ 线线垂直**是这里的枢纽；" "\n"
        r"③ ⭐ **「取几分之几」看球心的位置**：球心在棱上 ⟹ $\frac14$；在面上 ⟹ $\frac12$；在顶点 ⟹ $\frac18$；在内部 ⟹ $1$。" "\n"
        r"**本题 $F$ 是 $A'D'$ 的中点（在棱上）⟹ $\frac14$** ✓；" "\n"
        r"④ ⚠ **别漏了 $M$ 只能在线段 $EF$ 上（不是整条直线）**：这决定了球不完整，" "\n"
        r"若误当整球会选 A $( \frac{4\pi}3)$ —— **A 就是这么备的**；" "\n"
        r"⑤ 检验：**四个选项恰好是 $\frac{4\pi}3$ 的 $1$、$\frac12$、$\frac18$、$\frac14$ 倍**，" "\n"
        r"反推说明命题人考的就是这个比例 ✓。"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-279'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-279-V2',
}

T241_E1 = {
    'type': '选择',
    'stem_text': (
        r"设 $O$ 为 $\triangle ABC$ 所在平面内一点，满足 $2\vec{OA}-7\vec{OB}-3\vec{OC}=\vec 0$，"
        r"则 $\triangle ABC$ 的面积与 $\triangle BOC$ 的面积的比值为（　　）"
    ),
    'opts': [
        ('A', r"$6$"),
        ('B', r"$\dfrac83$"),
        ('C', r"$\dfrac{12}7$"),
        ('D', r"$4$"),
    ],
    'answer': 'D',
    'analysis': (
        r"由 $2\vec{OA}-7\vec{OB}-3\vec{OC}=\vec 0$ 得 $\vec O=\frac{7\vec B+3\vec C-2\vec A}{8}$。"
        r"建系取 $A(0,0)$、$B(1,0)$、$C(0,1)$，则 $O(\frac78,\frac38)$，$S_{BOC}=\frac18$，比值为 $4$。"
    ),
    'solution': (
        r"**方法一（重心坐标 / 面积系数）**：" "\n"
        r"设 $O$ 的重心坐标为 $(\alpha,\beta,\gamma)$（$\alpha+\beta+\gamma=1$，$\vec O=\alpha\vec A+\beta\vec B+\gamma\vec C$）。" "\n"
        r"由 $2\vec{OA}-7\vec{OB}-3\vec{OC}=\vec 0$：" "\n"
        r"$2(\vec A-\vec O)-7(\vec B-\vec O)-3(\vec C-\vec O)=\vec 0$" "\n"
        r"$\Rightarrow 2\vec A-7\vec B-3\vec C+( -2+7+3)\vec O=\vec 0\Rightarrow 8\vec O=-2\vec A+7\vec B+3\vec C$" "\n"
        r"$\Rightarrow \vec O=-\dfrac14\vec A+\dfrac78\vec B+\dfrac38\vec C$。" "\n"
        r"故 $\alpha=-\dfrac14$、$\beta=\dfrac78$、$\gamma=\dfrac38$（和为 $1$ ✓）。" "\n"
        r"由重心坐标与面积的关系 $\dfrac{S_{\triangle BOC}}{S_{\triangle ABC}}=\alpha=-\dfrac14$，" "\n"
        r"取绝对值得 $\dfrac{S_{\triangle BOC}}{S_{\triangle ABC}}=\dfrac14$，故 $\dfrac{S_{\triangle ABC}}{S_{\triangle BOC}}=4$。" "\n"
        r"**方法二（建系）**：取 $A(0,0)$、$B(1,0)$、$C(0,1)$，则" "\n"
        r"$O=-\dfrac14(0,0)+\dfrac78(1,0)+\dfrac38(0,1)=\left(\dfrac78,\dfrac38\right)$。" "\n"
        r"$S_{\triangle ABC}=\dfrac12$；" "\n"
        r"$S_{\triangle BOC}=\dfrac12\left|\det\left(O-B,\ C-B\right)\right|=\dfrac12\left|\det\left(\left(-\dfrac18,\dfrac38\right),\ (-1,1)\right)\right|$" "\n"
        r"$=\dfrac12\left|-\dfrac18\cdot1-\dfrac38\cdot(-1)\right|=\dfrac12\cdot\dfrac14=\dfrac18$。" "\n"
        r"故比值为 $\dfrac{1/2}{1/8}=4$。故选 D。"
    ),
    'review': (
        r"★ 题干、答案完整 ✓。**详解原书较绕（构造辅助点 $O_1$）**，我用重心坐标 + 建系两种方法独立求解，结果一致。" "\n"
        r"原书 p207 详解：「不妨设 $\vec{OA_1}=2\vec{OA}$，$\vec{OB_1}=-7\vec{OB}$，$\vec{OC_1}=3\vec{OC}$…" "\n"
        r"根据题意则 $\vec{OA_1}+\vec{OB_1}+\vec{OC_1}=0$，即点 $O$ 是 $\triangle A_1B_1C_1$ 的重心，所以有 $S_{\triangle OA_1B_1}=S_{\triangle OA_1C_1}=S_{\triangle OB_1C_1}=k$…」" "\n"
        r"—— **思路是「把系数配成 $1$ 后用重心」**，与我的重心坐标法同源，答案 D 一致 ✓✓✓" "\n"
        r"**独立验算（建系，完全独立，不依赖任何技巧）**：" "\n"
        r"① **求 $O$**：$2(\vec A-\vec O)-7(\vec B-\vec O)-3(\vec C-\vec O)=\vec 0$" "\n"
        r"⟹ $2\vec A-7\vec B-3\vec C+(-2+7+3)\vec O=\vec 0$ ⟹ $8\vec O=-2\vec A+7\vec B+3\vec C$ ✓✓✓" "\n"
        r"（注意 $-2+7+3=8$，不是 $2-7-3=-8$ —— **移项时 $\vec O$ 的系数是「原系数之和的相反数」**）" "\n"
        r"② **$\vec O=-\frac14\vec A+\frac78\vec B+\frac38\vec C$**，系数和 $=-\frac14+\frac78+\frac38=\frac{-2+7+3}8=1$ ✓✓✓" "\n"
        r"③ **建系**：$A(0,0)$、$B(1,0)$、$C(0,1)$ ⟹ $O=(\frac78,\frac38)$ ✓✓✓" "\n"
        r"④ **验原条件**：$\vec{OA}=A-O=(-\frac78,-\frac38)$、$\vec{OB}=(\frac18,-\frac38)$、$\vec{OC}=(-\frac78,\frac58)$。" "\n"
        r"$2\vec{OA}-7\vec{OB}-3\vec{OC}=(-\frac{14}8,-\frac68)-(\frac78,-\frac{21}8)-(-\frac{21}8,\frac{15}8)$" "\n"
        r"$=(-\frac{14}8-\frac78+\frac{21}8,\;-\frac68+\frac{21}8-\frac{15}8)=(0,0)$ ✓✓✓ **完全满足**" "\n"
        r"⑤ **$S_{ABC}=\frac12$**（直角三角形两直角边为 $1$）✓✓✓" "\n"
        r"⑥ **$S_{BOC}$**：$B(1,0)$、$O(\frac78,\frac38)$、$C(0,1)$。" "\n"
        r"用行列式：$S=\frac12|x_B(y_O-y_C)+x_O(y_C-y_B)+x_C(y_B-y_O)|$" "\n"
        r"$=\frac12|1(\frac38-1)+\frac78(1-0)+0(0-\frac38)|=\frac12|-\frac58+\frac78|=\frac12\cdot\frac28=\frac18$ ✓✓✓" "\n"
        r"⑦ **比值** $\frac{1/2}{1/8}=4$ ✓✓✓" "\n"
        r"⑧ **重心坐标与面积的关系验**：$\frac{S_{BOC}}{S_{ABC}}=|\alpha|=\frac14$ ⟹ 比值 $4$ ✓✓✓ **两法一致**" "\n"
        r"**答案 D 正确** ✓" "\n"
        r"**⭐⭐ 通法（系数型向量条件 ⟹ 面积比）**：" "\n"
        r"① ⭐⭐ **通式：若 $x\vec{OA}+y\vec{OB}+z\vec{OC}=\vec 0$，则" "\n"
        r"$S_{\triangle BOC}:S_{\triangle COA}:S_{\triangle AOB}=|x|:|y|:|z|$**（$O$ 在形内时去掉绝对值）。" "\n"
        r"本题 $x=2,y=-7,z=-3$ ⟹ $|S_{BOC}|:|S_{COA}|:|S_{AOB}|=2:7:3$；" "\n"
        r"② ⭐⭐ **更稳妥的做法是移项求重心坐标**：$8\vec O=-2\vec A+7\vec B+3\vec C$ ⟹ " "\n"
        r"$\alpha=-\frac14$、$\beta=\frac78$、$\gamma=\frac38$，**而 $\alpha=\frac{S_{BOC}}{S_{ABC}}$（带符号）** —— " "\n"
        r"$\alpha<0$ 说明 $O$ 与 $A$ 分居 $BC$ 两侧，**取绝对值即为面积比**；" "\n"
        r"③ ⚠ **移项别错**：$x\vec{OA}+y\vec{OB}+z\vec{OC}=\vec 0$ ⟹ $(x+y+z)\vec O=x\vec A+y\vec B+z\vec C$。" "\n"
        r"**是 $\vec O$ 的系数等于 $x+y+z$，右边是 $x\vec A+\cdots$（不是 $-x\vec A$）** —— 我第一遍就差点写反；" "\n"
        r"④ ⚠ **比值方向**：题目问 $\frac{S_{ABC}}{S_{BOC}}$（大比小），若算成 $\frac{S_{BOC}}{S_{ABC}}=\frac14$ 会误选…" "\n"
        r"（$\frac14$ 不在选项里，但 **$\frac{S_{ABC}}{S_{BOC}}=4$ 与选项 A 的 $6$、B 的 $\frac83$ 同量级，需看清谁比谁**）；" "\n"
        r"⑤ 检验：**把 $O$ 代回原向量等式验一次**（得 $\vec 0$ ✓），并**用两种方法算面积比**（都是 $4$ ✓）。"
    ),
    'difficulty': 0.82,
    'topics': ['M-T-241'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-241-E1',
}

QS = [T192_E1, T192_V1, T192_V2, T192_V3, T232_V1, T232_V2, T233_V1, T233_V3,
      T283_V1, T283_V2, T279_V2, T241_E1]
