# -*- coding: utf-8 -*-
r"""第86批：解三角形与向量综合（12 题）

M-T-223（3）、M-T-220（3）、M-T-209（3）、M-T-183（3）

## ★★ 12 题我全部独立验算（回代 / 端点检验 / 数值对拍）

| 题 | 我的验算 | 答案 |
|---|---|---|
| M-T-223-E1 | 正弦定理化边为角 ⟹ $\cos B=-\frac12$ ⟹ $B=\frac{2\pi}3$；$(\sqrt3-1)\cos A+2\cos C=\sqrt6\sin(A+\frac\pi4)$，$A\in(0,\frac\pi3)$ | **$(\sqrt3,\sqrt6]$** |
| M-T-223-V1 | 选①：$\cos\frac{A+B}2=\sin\frac C2$ ⟹ $C=\frac\pi3$；$a+2b=2\sqrt7\sin(A+\varphi)$，最大值可达 | **$2\sqrt7$** |
| M-T-223-V3 | $b^2+c^2=a^2+bc$ ⟹ $\cos A=\frac12$；$2\cos^2B+\cos(B-C)=1+\sin(2B+\frac\pi6)\in(0,2]$ | **$(0,2]$** |
| M-T-220-E1 | 两次正弦定理 ⟹ $\sin\angle BAD=\sin\angle CAD$；$b+c=\sqrt3bc$ 配 $b+c\ge2\sqrt{bc}$ ⟹ $bc\ge\frac43$ | **$\frac{\sqrt3}3$** |
| M-T-220-V2 | $\frac a{\cos A}=\frac{\sqrt3 b}{\sin B}$ 配正弦定理 ⟹ $\tan A=\sqrt3$；$4=b^2+c^2-bc\ge bc$ | **$\sqrt3$** |
| M-T-220-V3 | $\sqrt3 b\cos C=c\sin B$ ⟹ $\tan C=\sqrt3$；$R=2$ ⟹ $c=2\sqrt3$，$ab\le12$ | **$3\sqrt3$** |
| M-T-209-E1 | $AG\perp BG$ ⟹ $DG=\frac c2$、$CD=\frac{3c}2$ ⟹ $a^2+b^2=5c^2$ ⟹ $\cos C=\frac25(\frac ab+\frac ba)>\frac{\sqrt6}3$ | **C** |
| M-T-209-V2 | $BG\perp CG$ ⟹ $b^2+c^2=5a^2$ ⟹ $\cos A=\frac{2a^2}{bc}$ ⟹ $\lambda=\frac12$ | **C** |
| M-T-209-V3 | 三个重心坐标代入行列式 ⟹ $S_{G_1G_2G_3}=\frac19 S_{ABCD}=\frac{2022}9$ | **$\frac{674}3$** |
| M-T-183-E1 | 建系得 $2\lambda+\mu=\frac32-\sin(\theta+\frac\pi6)$，$\theta\in[\pi,2\pi]$ ⟹ 最小值 $\frac32-\frac12=1$ | **$1$** |
| M-T-183-V2 | $d(A,C)=2(1-\cos\alpha)+2\lvert\sin\alpha\rvert$，两段各得最大 $2+2\sqrt2$ | **$4+4\sqrt2$** |
| M-T-183-V3 | $h=\lvert\sin\theta\rvert+\lvert\sin(\theta+120^\circ)\rvert\in[\frac{\sqrt3}2,\sqrt3]$ ⟹ 乘 $\sqrt5$ | **$[\frac{\sqrt{15}}2,\sqrt{15}]$** |

## 五处根号丢失还原（全部有硬判据）

- M-T-223-E1 答案 `3, 6` ⟹ **$(\sqrt3,\sqrt6]$**（值为 $\sqrt6\sin(A+\frac\pi4)$，端点 $\sqrt6\cdot\frac{\sqrt2}2=\sqrt3$）
- M-T-220-E1 答案 `3 / 3` ⟹ **$\frac{\sqrt3}3$**（$\frac{\sqrt3}4\cdot\frac43$）
- M-T-220-V3 答案 `3 3` ⟹ **$3\sqrt3$**（$\frac12\cdot12\cdot\frac{\sqrt3}2$）
- M-T-183-V2 答案 `4 + 4 2` ⟹ **$4+4\sqrt2$**
- M-T-183-V3 答案 `15/2, 15` ⟹ **$[\frac{\sqrt{15}}2,\sqrt{15}]$**（$=\sqrt5\cdot[\frac{\sqrt3}2,\sqrt3]$）

## 一处答案双写法说明

M-T-209-V3 的 ans 为 `674/3 ##224 2/3` —— **两者是同一个数**：$\frac{674}3=224\frac23$。取 $\frac{674}3$。
"""

T223_E1 = {
    'type': '解答',
    'stem_text': (
        r"在 $\triangle ABC$ 中，$a,b,c$ 分别是角 $A,B,C$ 所对的边，满足 $(2a+c)\cos B+b\cos C=0$。" "\n"
        r"(1) 求角 $B$ 大小；" "\n"
        r"(2) 求 $(\sqrt3-1)\cos A+2\cos C$ 的取值范围．"
    ),
    'opts': [],
    'answer': r"(1) $B=\dfrac{2\pi}3$；(2) $\left(\sqrt3,\sqrt6\right]$",
    'analysis': (
        r"(1) 正弦定理化边为角：$2\sin A\cos B+\sin C\cos B+\sin B\cos C=0$，后两项合成 $\sin(B+C)=\sin A$，"
        r"故 $\sin A(2\cos B+1)=0$，得 $\cos B=-\frac12$；(2) 由 $A+C=\frac\pi3$ 化为 $\sqrt6\sin(A+\frac\pi4)$，"
        r"$A\in(0,\frac\pi3)$ 得 $A+\frac\pi4\in(\frac\pi4,\frac{7\pi}{12})$。"
    ),
    'solution': (
        r"**(1)** 由 $(2a+c)\cos B+b\cos C=0$ 及正弦定理 $a=2R\sin A$ 等，得" "\n"
        r"$2\sin A\cos B+\sin C\cos B+\sin B\cos C=0$。" "\n"
        r"后两项合成为 $\sin(B+C)$，又 $B+C=\pi-A$，故 $\sin(B+C)=\sin A$，于是" "\n"
        r"$2\sin A\cos B+\sin A=0$，即 $\sin A(2\cos B+1)=0$。" "\n"
        r"$\because 0<A<\pi$，$\therefore\sin A\ne0$，$\therefore\cos B=-\dfrac12$。" "\n"
        r"又 $0<B<\pi$，$\therefore B=\dfrac{2\pi}3$。" "\n"
        r"**(2)** 由 $A+B+C=\pi$ 且 $B=\frac{2\pi}3$ 得 $A+C=\dfrac\pi3$，且 $0<A<\dfrac\pi3$、$0<C<\dfrac\pi3$。" "\n"
        r"$\therefore C=\dfrac\pi3-A$，" "\n"
        r"$(\sqrt3-1)\cos A+2\cos C=(\sqrt3-1)\cos A+2\cos\left(\dfrac\pi3-A\right)$" "\n"
        r"$=(\sqrt3-1)\cos A+2\left(\dfrac12\cos A+\dfrac{\sqrt3}2\sin A\right)$" "\n"
        r"$=(\sqrt3-1)\cos A+\cos A+\sqrt3\sin A=\sqrt3\cos A+\sqrt3\sin A=\sqrt6\sin\left(A+\dfrac\pi4\right)$。" "\n"
        r"$\because 0<A<\dfrac\pi3$，$\therefore\dfrac\pi4<A+\dfrac\pi4<\dfrac{7\pi}{12}$。" "\n"
        r"在该区间上 $\sin\left(A+\dfrac\pi4\right)\in\left(\dfrac{\sqrt2}2,1\right]$（左端取不到，右端在 $A+\frac\pi4=\frac\pi2$ 处取到），" "\n"
        r"$\therefore\sqrt6\sin\left(A+\dfrac\pi4\right)\in\left(\sqrt6\cdot\dfrac{\sqrt2}2,\sqrt6\right]=\left(\sqrt3,\sqrt6\right]$。" "\n"
        r"即 $(\sqrt3-1)\cos A+2\cos C$ 的取值范围是 $\left(\sqrt3,\sqrt6\right]$。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书详解：「$\because(2a+c)\cos B+b\cos C=0$，由正弦定理知：$2\sin A\cos B+\sin C\cos B+\sin B\cos C=0$。" "\n"
        r"即：$2\sin A\cos B+\sin(B+C)=2\sin A\cos B+\sin A=0$。$\because0<A<\pi$，$\therefore\sin A\ne0$，$\therefore\cos B=-\frac12$，" "\n"
        r"又 $\because0<B<\pi$，$\therefore B=\frac{2\pi}3$；(2) $\because A+B+C=\pi$，$\therefore A+C=\frac\pi3$，且 $0<A,C<\frac\pi3$。" "\n"
        r"$\therefore(\sqrt3-1)\cos A+2\cos C=(\sqrt3-1)\cos A+2\cos(\frac\pi3-A)=(\sqrt3-1)\cos A+2(\frac12\cos A+\frac{\sqrt3}2\sin A)$" "\n"
        r"$=\sqrt3\cos A+\sqrt3\sin A=\sqrt6\sin(A+\frac\pi4)$。$\because0<A<\frac\pi3$，$\therefore\frac\pi4<A+\frac\pi4<\frac{7\pi}{12}$，" "\n"
        r"$\therefore\frac{\sqrt2}2<\sin(A+\frac\pi4)\le1$，$\therefore\sqrt3<\sqrt6\sin(A+\frac\pi4)\le\sqrt6$，故 $(\sqrt3-1)\cos A+2\cos C$ 的取值范围是 $(\sqrt3,\sqrt6]$」" "\n"
        r"—— **化边为角、$\sin C\cos B+\sin B\cos C=\sin(B+C)$、$\cos B=-\frac12$、$B=\frac{2\pi}3$、" "\n"
        r"$(\sqrt3-1)\cos A+2\cos(\frac\pi3-A)=\sqrt6\sin(A+\frac\pi4)$、范围 $(\sqrt3,\sqrt6]$ 全部一致** ✓✓✓" "\n"
        r"（**答案的根号在提取中丢失**：`3, 6` 实为 $(\sqrt3,\sqrt6]$）" "\n"
        r"**独立验算（完全独立）**：" "\n"
        r"① **化边为角**：$(2a+c)\cos B+b\cos C=0$ ⟹ $2\sin A\cos B+\sin C\cos B+\sin B\cos C=0$ ✓✓✓" "\n"
        r"② **$\sin C\cos B+\sin B\cos C=\sin(B+C)=\sin(\pi-A)=\sin A$** ✓✓✓" "\n"
        r"⟹ $2\sin A\cos B+\sin A=0$ ⟹ $\sin A(2\cos B+1)=0$ ⟹ $\cos B=-\frac12$ ⟹ $B=\frac{2\pi}3$ ✓✓✓" "\n"
        r"③ **$A+C=\frac\pi3$ 且两者都为正** ⟹ $A\in(0,\frac\pi3)$、$C=\frac\pi3-A$ ✓✓✓" "\n"
        r"④ **展开**：$2\cos(\frac\pi3-A)=2(\cos\frac\pi3\cos A+\sin\frac\pi3\sin A)=2(\frac12\cos A+\frac{\sqrt3}2\sin A)=\cos A+\sqrt3\sin A$ ✓✓✓" "\n"
        r"⟹ $(\sqrt3-1)\cos A+\cos A+\sqrt3\sin A=\sqrt3\cos A+\sqrt3\sin A$ ✓✓✓" "\n"
        r"（**$(\sqrt3-1)+1=\sqrt3$ 恰好凑整** —— 这是能合并成辅助角的信号）" "\n"
        r"⑤ **辅助角**：$\sqrt3\cos A+\sqrt3\sin A=\sqrt{3+3}\sin(A+\frac\pi4)$？" "\n"
        r"检验：$\sqrt6\sin(A+\frac\pi4)=\sqrt6(\sin A\cos\frac\pi4+\cos A\sin\frac\pi4)=\sqrt6(\frac{\sqrt2}2\sin A+\frac{\sqrt2}2\cos A)=\sqrt3\sin A+\sqrt3\cos A$ ✓✓✓" "\n"
        r"⑥ **区间端点**：$A\in(0,\frac\pi3)$ ⟹ $A+\frac\pi4\in(\frac\pi4,\frac{7\pi}{12})$。" "\n"
        r"$\frac\pi4=45^\circ$、$\frac{7\pi}{12}=105^\circ$。" "\n"
        r"$\sin$ 在 $[45^\circ,105^\circ]$ 上：最小值在 $45^\circ$ 处 $=\frac{\sqrt2}2$（**取不到，因 $A>0$ 严格**）；" "\n"
        r"最大值在 $90^\circ$ 处 $=1$（**$90^\circ\in(45^\circ,105^\circ)$，取得到**）✓✓✓" "\n"
        r"⟹ $\sin\in(\frac{\sqrt2}2,1]$ ⟹ $\sqrt6\sin\in(\sqrt3,\sqrt6]$ ✓✓✓" "\n"
        r"（$\sqrt6\cdot\frac{\sqrt2}2=\frac{\sqrt{12}}2=\frac{2\sqrt3}2=\sqrt3$ ✓✓✓）" "\n"
        r"⑦ **数值检验**：取 $A=\frac\pi6$（则 $C=\frac\pi6$）：" "\n"
        r"$(\sqrt3-1)\cos30^\circ+2\cos30^\circ=(1.732-1)\cdot0.866+2\cdot0.866=0.634+1.732=2.366$。" "\n"
        r"公式：$\sqrt6\sin(30^\circ+45^\circ)=2.449\cdot\sin75^\circ=2.449\cdot0.966=2.366$ ✓✓✓" "\n"
        r"取 $A\to0^+$：$(\sqrt3-1)\cdot1+2\cos60^\circ=0.732+1=1.732=\sqrt3$ ✓✓✓ **正是下界**" "\n"
        r"取 $A=\frac\pi{12}$（$A+\frac\pi4=\frac\pi3$… 不对，应取 $A+\frac\pi4=\frac\pi2$ 即 $A=\frac\pi4$）：" "\n"
        r"$A=\frac\pi4$ 时 $C=\frac\pi3-\frac\pi4=\frac\pi{12}$。$(\sqrt3-1)\cos45^\circ+2\cos15^\circ=0.732\cdot0.707+2\cdot0.966=0.518+1.932=2.449=\sqrt6$ ✓✓✓ **正是上界**" "\n"
        r"**答案正确** ✓" "\n"
        r"**⭐⭐ 通法（边角混合式 ⟹ 正弦定理化边为角）**：" "\n"
        r"① ⭐⭐ **识别特征：等式各项都是「边 $\times$ 角的余弦」⟹ 正弦定理统一成角**：" "\n"
        r"$(2a+c)\cos B+b\cos C=0$ ⟹ 全部换成 $\sin$，**边就消失了** ✓✓✓；" "\n"
        r"② ⭐⭐ **$\sin C\cos B+\sin B\cos C=\sin(B+C)=\sin A$ 是本题的题眼**：" "\n"
        r"**凡是出现「$\sin X\cos Y+\sin Y\cos X$」就合成 $\sin(X+Y)$，再用 $X+Y=\pi-Z$ 化为 $\sin Z$** ✓✓✓；" "\n"
        r"③ ⭐⭐ **合并后提公因式 $\sin A$**：" "\n"
        r"$\sin A(2\cos B+1)=0$，**由 $\sin A\ne0$ 直接得 $\cos B$** —— 这是标准收尾；" "\n"
        r"④ ⭐⭐ **第 (2) 问用「$A+C=$ 常数」消元**：" "\n"
        r"**把 $C$ 写成 $\frac\pi3-A$，表达式就只剩 $A$ 一个变量** ✓✓✓；" "\n"
        r"⑤ ⭐⭐ **辅助角的配方检验**：" "\n"
        r"$\sqrt3\cos A+\sqrt3\sin A$ 的振幅 $=\sqrt{3+3}=\sqrt6$，初相 $\varphi$ 满足 $\tan\varphi=\frac{\sqrt3}{\sqrt3}=1$ ⟹ $\varphi=\frac\pi4$ ✓✓✓；" "\n"
        r"⑥ ⚠ **开闭端点是这题的考点**：" "\n"
        r"**左端 $\sqrt3$ 对应 $A\to0$（开区间 $A>0$ 使 $A=0$ 取不到）⟹ 开**；" "\n"
        r"**右端 $\sqrt6$ 对应 $A=\frac\pi4\in(0,\frac\pi3)$ ⟹ 闭** ✓✓✓。" "\n"
        r"（**若题设是 $0<A\le\frac\pi3$ 之类，开闭要重新判断**）" "\n"
        r"⑦ ⭐ **验证：代入特殊角数值与公式对照** —— " "\n"
        r"本题 $A=\frac\pi6$ 给 $2.366$、$A\to0$ 给 $\sqrt3$、$A=\frac\pi4$ 给 $\sqrt6$，全部吻合 ✓✓✓"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-223'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-223-E1',
}

T223_V1 = {
    'type': '解答',
    'stem_text': (
        r"在 ① $\sqrt3a\cos\dfrac{A+B}2=c\sin A$，② $\sqrt3a=\sqrt3c\cos B+b\sin C$，"
        r"③ $\cos^2A-\cos^2C=\sin^2B-\sin A\sin B$ 这三个条件中任选一个，补充在下面问题中，并给出解答。" "\n"
        r"问题：已知 $\triangle ABC$ 内角 $A,B,C$ 的对边分别是 $a,b,c$，$c=\sqrt3$，____，求 $a+2b$ 的最大值。" "\n"
        r"注：如果选择多个条件分别解答，按第一个解答计分。"
    ),
    'opts': [],
    'answer': r"$2\sqrt7$",
    'analysis': (
        r"选①：由 $\cos\frac{A+B}2=\sin\frac C2$ 得 $\sqrt3\sin A\sin\frac C2=2\sin\frac C2\cos\frac C2\sin A$，"
        r"故 $\cos\frac C2=\frac{\sqrt3}2$，$C=\frac\pi3$。由正弦定理 $a=2\sin A$、$b=2\sin B$，"
        r"$a+2b=4\sin A+2\sqrt3\cos A=2\sqrt7\sin(A+\varphi)\le2\sqrt7$。"
    ),
    'solution': (
        r"**若选①**：$\because A+B+C=\pi$，$\therefore\dfrac{A+B}2=\dfrac{\pi-C}2$，故 $\cos\dfrac{A+B}2=\cos\left(\dfrac\pi2-\dfrac C2\right)=\sin\dfrac C2$。" "\n"
        r"由 $\sqrt3a\cos\dfrac{A+B}2=c\sin A$ 及正弦定理得 $\sqrt3\sin A\sin\dfrac C2=\sin C\sin A$。" "\n"
        r"$\because\sin A\ne0$，$\therefore\sqrt3\sin\dfrac C2=\sin C=2\sin\dfrac C2\cos\dfrac C2$。" "\n"
        r"又 $\sin\dfrac C2\ne0$，$\therefore\cos\dfrac C2=\dfrac{\sqrt3}2$。$\because C\in(0,\pi)$，$\therefore\dfrac C2=\dfrac\pi6$，即 $C=\dfrac\pi3$。" "\n"
        r"由正弦定理 $\dfrac a{\sin A}=\dfrac b{\sin B}=\dfrac c{\sin C}=\dfrac{\sqrt3}{\sqrt3/2}=2$，故 $a=2\sin A$、$b=2\sin B$。" "\n"
        r"$\therefore a+2b=2\sin A+4\sin B=2\sin A+4\sin\left(A+\dfrac\pi3\right)$" "\n"
        r"$=2\sin A+4\left(\dfrac12\sin A+\dfrac{\sqrt3}2\cos A\right)=4\sin A+2\sqrt3\cos A=2\sqrt7\sin(A+\varphi)$，" "\n"
        r"其中 $\sin\varphi=\dfrac{\sqrt3}{\sqrt7}$、$\cos\varphi=\dfrac2{\sqrt7}$。" "\n"
        r"$\because A\in\left(0,\dfrac{2\pi}3\right)$，$\therefore$ 存在 $A$ 使 $A+\varphi=\dfrac\pi2$，此时 $a+2b$ 取最大值 $2\sqrt7$。" "\n"
        r"**若选②**：由 $\sqrt3a=\sqrt3c\cos B+b\sin C$ 及正弦定理得" "\n"
        r"$\sqrt3\sin A=\sqrt3\sin C\cos B+\sin B\sin C$。又 $\sin A=\sin(B+C)=\sin B\cos C+\cos B\sin C$，" "\n"
        r"$\therefore\sqrt3\sin B\cos C+\sqrt3\cos B\sin C=\sqrt3\sin C\cos B+\sin B\sin C$，化简得 $\sqrt3\sin B\cos C=\sin B\sin C$。" "\n"
        r"由 $\sin B\ne0$ 得 $\tan C=\sqrt3$，$\because C\in(0,\pi)$，$\therefore C=\dfrac\pi3$。下同①。" "\n"
        r"**若选③**：由 $\cos^2A-\cos^2C=\sin^2B-\sin A\sin B$ 得" "\n"
        r"$(1-\sin^2A)-(1-\sin^2C)=\sin^2B-\sin A\sin B$，即 $\sin^2C-\sin^2A=\sin^2B-\sin A\sin B$。" "\n"
        r"由正弦定理得 $c^2-a^2=b^2-ab$，即 $a^2+b^2-c^2=ab$，" "\n"
        r"$\therefore\cos C=\dfrac{a^2+b^2-c^2}{2ab}=\dfrac{ab}{2ab}=\dfrac12$，$\because C\in(0,\pi)$，$\therefore C=\dfrac\pi3$。下同①。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书详解给出三个条件各自的推导，**三者都推出 $C=\frac\pi3$，再统一求 $a+2b$ 的最大值 $2\sqrt7$** ✓✓✓" "\n"
        r"**独立验算（完全独立）**：" "\n"
        r"① **选① 的 $\cos\frac{A+B}2=\sin\frac C2$**：$\frac{A+B}2=\frac{\pi-C}2=\frac\pi2-\frac C2$，$\cos(\frac\pi2-\frac C2)=\sin\frac C2$ ✓✓✓" "\n"
        r"② **$\sqrt3\sin A\sin\frac C2=\sin C\sin A$** ⟹ 约去 $\sin A$ ⟹ $\sqrt3\sin\frac C2=2\sin\frac C2\cos\frac C2$ ⟹ $\cos\frac C2=\frac{\sqrt3}2$ ✓✓✓" "\n"
        r"⟹ $\frac C2=\frac\pi6$ ⟹ $C=\frac\pi3$ ✓✓✓" "\n"
        r"③ **$\frac c{\sin C}=\frac{\sqrt3}{\sqrt3/2}=2$** ✓✓✓ ⟹ $a=2\sin A$、$b=2\sin B$ ✓✓✓" "\n"
        r"④ **$B=A+\frac\pi3$**：由 $A+B=\pi-\frac\pi3=\frac{2\pi}3$ ⟹ $B=\frac{2\pi}3-A$。" "\n"
        r"**注意**：详解写 $\sin(A+\frac\pi3)$，而我由 $B=\frac{2\pi}3-A$ 得 $\sin B=\sin(\frac{2\pi}3-A)$。" "\n"
        r"检验：$\sin(A+\frac\pi3)=\sin(\pi-(A+\frac\pi3))=\sin(\frac{2\pi}3-A)$ ✓✓✓ **两者相等**" "\n"
        r"⑤ **展开**：$4\sin(A+\frac\pi3)=4(\frac12\sin A+\frac{\sqrt3}2\cos A)=2\sin A+2\sqrt3\cos A$ ✓✓✓" "\n"
        r"⟹ $a+2b=2\sin A+2\sin A+2\sqrt3\cos A=4\sin A+2\sqrt3\cos A$ ✓✓✓" "\n"
        r"⑥ **振幅**：$\sqrt{16+12}=\sqrt{28}=2\sqrt7$ ✓✓✓" "\n"
        r"⑦ **辅助角**：$4\sin A+2\sqrt3\cos A=2\sqrt7\sin(A+\varphi)$，$\tan\varphi=\frac{2\sqrt3}4=\frac{\sqrt3}2$。" "\n"
        r"详解写 $\sin\varphi=\frac{\sqrt3}{\sqrt7}$、$\cos\varphi=\frac2{\sqrt7}$ ⟹ $\tan\varphi=\frac{\sqrt3}2$ ✓✓✓" "\n"
        r"检验 $\sin^2+\cos^2=\frac37+\frac47=1$ ✓✓✓" "\n"
        r"⑧ **能否取到最大值**：需 $A+\varphi=\frac\pi2$ 即 $A=\frac\pi2-\varphi$。" "\n"
        r"$\varphi=\arctan\frac{\sqrt3}2\approx40.89^\circ$ ⟹ $A\approx49.11^\circ\in(0,120^\circ)$ ✓✓✓ **在范围内**" "\n"
        r"（同时 $B=\frac{2\pi}3-A\approx70.89^\circ>0$ ✓）" "\n"
        r"⑨ **选② 的化简**：$\sqrt3(\sin B\cos C+\cos B\sin C)=\sqrt3\sin C\cos B+\sin B\sin C$" "\n"
        r"⟹ $\sqrt3\sin B\cos C+\sqrt3\cos B\sin C-\sqrt3\sin C\cos B=\sin B\sin C$" "\n"
        r"⟹ $\sqrt3\sin B\cos C=\sin B\sin C$ ✓✓✓（$\sqrt3\cos B\sin C-\sqrt3\sin C\cos B=0$）" "\n"
        r"⟹ $\tan C=\sqrt3$ ⟹ $C=\frac\pi3$ ✓✓✓" "\n"
        r"⑩ **选③**：$\cos^2A-\cos^2C=(1-\sin^2A)-(1-\sin^2C)=\sin^2C-\sin^2A$ ✓✓✓" "\n"
        r"⟹ $c^2-a^2=b^2-ab$ ⟹ $a^2+b^2-c^2=ab$ ⟹ $\cos C=\frac12$ ⟹ $C=\frac\pi3$ ✓✓✓" "\n"
        r"**答案 $2\sqrt7$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（三选一条件题）**：" "\n"
        r"① ⭐⭐ **三个条件必然推出同一个结论**（否则题目不成立）—— **可以只做一个，但最好验证另一个** ✓✓✓；" "\n"
        r"② ⭐⭐ **条件①：见到 $\cos\frac{A+B}2$ 立刻化为 $\sin\frac C2$**：" "\n"
        r"**$\frac{A+B}2=\frac\pi2-\frac C2$ ⟹ $\cos\frac{A+B}2=\sin\frac C2$** ✓✓✓；" "\n"
        r"③ ⭐⭐ **条件②：化边为角后，$\sin A$ 写成 $\sin(B+C)$ 展开**，与右端对比**消去同类项** ✓✓✓；" "\n"
        r"④ ⭐⭐ **条件③：$\cos^2$ 化为 $1-\sin^2$**，再用正弦定理化为边 ✓✓✓；" "\n"
        r"⑤ ⭐⭐ **求 $pa+qb$ 最大值的标准流程**：" "\n"
        r"正弦定理统一成 $2R(p\sin A+q\sin B)$ ⟹ 用 $A+B=$ 常数消元 ⟹ **辅助角化为 $M\sin(A+\varphi)$** ⟹ **检验 $A+\varphi=\frac\pi2$ 是否有解** ✓✓✓；" "\n"
        r"⑥ ⚠ **必须检验最大值能否取到**：" "\n"
        r"**解出 $A$ 后要确认 $A\in(0,\frac{2\pi}3)$ 且 $B>0$** —— 本题 $A\approx49^\circ$ ✓✓✓。" "\n"
        r"（**若 $\varphi$ 太大导致 $A<0$，最大值就在边界取**）" "\n"
        r"⑦ ⭐ **$\sin B$ 的两种写法**：" "\n"
        r"**$\sin(A+\frac\pi3)=\sin(\frac{2\pi}3-A)$** —— 用 $\sin x=\sin(\pi-x)$ 可互化 ✓✓✓"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-223'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-223-V1',
}

T223_V3 = {
    'type': '解答',
    'stem_text': (
        r"$\triangle ABC$ 中，内角 $A,B,C$ 所对的边长分别为 $a,b,c$，已知 $\sin^2B+\sin^2C=\sin^2A+\sin B\sin C$。" "\n"
        r"(1) 求角 $A$ 的大小；" "\n"
        r"(2) 求 $2\cos^2B+\cos(B-C)$ 的取值范围．"
    ),
    'opts': [],
    'answer': r"(1) $A=\dfrac\pi3$；(2) $(0,2]$",
    'analysis': (
        r"(1) 正弦定理化角成边：$b^2+c^2=a^2+bc$，故 $\cos A=\frac{bc}{2bc}=\frac12$；"
        r"(2) 由 $B+C=\frac{2\pi}3$ 得 $B-C=2B-\frac{2\pi}3$，化为 $1+\sin(2B+\frac\pi6)$，"
        r"$2B+\frac\pi6\in(\frac\pi6,\frac{3\pi}2)$ 得范围为 $(0,2]$。"
    ),
    'solution': (
        r"**(1)** 由正弦定理 $a=2R\sin A$ 等，将 $\sin^2B+\sin^2C=\sin^2A+\sin B\sin C$ 化为" "\n"
        r"$b^2+c^2=a^2+bc$，即 $b^2+c^2-a^2=bc$。" "\n"
        r"$\therefore\cos A=\dfrac{b^2+c^2-a^2}{2bc}=\dfrac{bc}{2bc}=\dfrac12$。" "\n"
        r"$\because A\in(0,\pi)$，$\therefore A=\dfrac\pi3$。" "\n"
        r"**(2)** 由 $A=\dfrac\pi3$ 得 $B+C=\dfrac{2\pi}3$，故 $C=\dfrac{2\pi}3-B$，" "\n"
        r"$B-C=B-\left(\dfrac{2\pi}3-B\right)=2B-\dfrac{2\pi}3$，且 $0<B<\dfrac{2\pi}3$。" "\n"
        r"$2\cos^2B+\cos(B-C)=1+\cos2B+\cos\left(2B-\dfrac{2\pi}3\right)$。" "\n"
        r"展开 $\cos\left(2B-\dfrac{2\pi}3\right)=\cos2B\cos\dfrac{2\pi}3+\sin2B\sin\dfrac{2\pi}3=-\dfrac12\cos2B+\dfrac{\sqrt3}2\sin2B$。" "\n"
        r"$\therefore$ 原式 $=1+\cos2B-\dfrac12\cos2B+\dfrac{\sqrt3}2\sin2B=1+\dfrac12\cos2B+\dfrac{\sqrt3}2\sin2B$" "\n"
        r"$=1+\sin\left(2B+\dfrac\pi6\right)$。" "\n"
        r"$\because 0<B<\dfrac{2\pi}3$，$\therefore\dfrac\pi6<2B+\dfrac\pi6<\dfrac{3\pi}2$。" "\n"
        r"在该区间上 $\sin\left(2B+\dfrac\pi6\right)\in[-1,1]$，其中" "\n"
        r"最大值 $1$ 在 $2B+\frac\pi6=\frac\pi2$（即 $B=\frac\pi6$）处**取到**；" "\n"
        r"最小值 $-1$ 在 $2B+\frac\pi6=\frac{3\pi}2$（即 $B=\frac{2\pi}3$）处**取不到**（$B<\frac{2\pi}3$ 严格）。" "\n"
        r"$\therefore 1+\sin\left(2B+\dfrac\pi6\right)\in(0,2]$。" "\n"
        r"即 $2\cos^2B+\cos(B-C)$ 的取值范围为 $(0,2]$。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书详解：「(1) 由正弦定理得：$b^2+c^2=a^2+bc$，从而 $\cos A=\frac{b^2+c^2-a^2}{2bc}=\frac{bc}{2bc}=\frac12$，因为 $A\in(0,\pi)$，所以 $A=\frac\pi3$；" "\n"
        r"(2) 由 $A=\frac\pi3$ 得：$B+C=\frac{2\pi}3$，所以 $C=\frac{2\pi}3-B$，$B-C=2B-\frac{2\pi}3$，$2\cos^2B+\cos(B-C)=1+\cos2B+\cos(2B-\frac{2\pi}3)$" "\n"
        r"$=\frac12\cos2B+\frac{\sqrt3}2\sin2B+1=\sin(2B+\frac\pi6)+1$。因为 $B\in(0,\frac{2\pi}3)$，所以 $2B+\frac\pi6\in(\frac\pi6,\frac{3\pi}2)$，结合正弦函数图象可得：" "\n"
        r"$\sin(2B+\frac\pi6)\in(-1,1]$，$\sin(2B+\frac\pi6)+1\in(0,2]$，所以 $2\cos^2B+\cos(B-C)$ 的取值范围为 $(0,2]$」" "\n"
        r"—— **化角成边、$\cos A=\frac12$、$A=\frac\pi3$、$1+\sin(2B+\frac\pi6)$、范围 $(0,2]$ 全部一致** ✓✓✓" "\n"
        r"**独立验算（完全独立）**：" "\n"
        r"① **化角成边**：$\sin^2B=\frac{b^2}{4R^2}$ 等，同乘 $4R^2$ 得 $b^2+c^2=a^2+bc$ ✓✓✓" "\n"
        r"② **$\cos A=\frac{b^2+c^2-a^2}{2bc}=\frac{bc}{2bc}=\frac12$** ✓✓✓ ⟹ $A=\frac\pi3$ ✓✓✓" "\n"
        r"③ **$B-C=2B-\frac{2\pi}3$**：$C=\frac{2\pi}3-B$ ⟹ $B-C=B-\frac{2\pi}3+B=2B-\frac{2\pi}3$ ✓✓✓" "\n"
        r"④ **$2\cos^2B=1+\cos2B$** ✓✓✓" "\n"
        r"⑤ **$\cos(2B-\frac{2\pi}3)$ 展开**：$\cos2B\cdot(-\frac12)+\sin2B\cdot\frac{\sqrt3}2$ ✓✓✓" "\n"
        r"（$\cos\frac{2\pi}3=-\frac12$、$\sin\frac{2\pi}3=\frac{\sqrt3}2$）" "\n"
        r"⑥ **合并**：$1+\cos2B-\frac12\cos2B+\frac{\sqrt3}2\sin2B=1+\frac12\cos2B+\frac{\sqrt3}2\sin2B$ ✓✓✓" "\n"
        r"⑦ **辅助角**：$\frac12\cos2B+\frac{\sqrt3}2\sin2B=\sin(2B+\frac\pi6)$？" "\n"
        r"$\sin(2B+\frac\pi6)=\sin2B\cos\frac\pi6+\cos2B\sin\frac\pi6=\frac{\sqrt3}2\sin2B+\frac12\cos2B$ ✓✓✓" "\n"
        r"⑧ **区间**：$B\in(0,\frac{2\pi}3)$ ⟹ $2B\in(0,\frac{4\pi}3)$ ⟹ $2B+\frac\pi6\in(\frac\pi6,\frac{3\pi}2)$ ✓✓✓" "\n"
        r"（$\frac{4\pi}3+\frac\pi6=\frac{8\pi}6+\frac\pi6=\frac{9\pi}6=\frac{3\pi}2$ ✓✓✓）" "\n"
        r"⑨ **开闭端点**：" "\n"
        r"$\sin=1$ 在 $2B+\frac\pi6=\frac\pi2$ ⟹ $B=\frac\pi6\in(0,\frac{2\pi}3)$ ✓ **取得到 ⟹ 上端闭**；" "\n"
        r"$\sin=-1$ 在 $2B+\frac\pi6=\frac{3\pi}2$ ⟹ $B=\frac{2\pi}3$ **不在开区间内 ⟹ 下端开** ✓✓✓" "\n"
        r"（**注意下端 $0$ 是「趋近」而非「取到」，故写 $(0,2]$ 不是 $[0,2]$**）" "\n"
        r"⑩ **数值检验**：取 $B=\frac\pi6$（则 $C=\frac\pi2$）：" "\n"
        r"$2\cos^230^\circ+\cos(30^\circ-90^\circ)=2\cdot0.75+\cos(-60^\circ)=1.5+0.5=2$ ✓✓✓ **正是上界**" "\n"
        r"取 $B\to\frac{2\pi}3$（$C\to0$）：$2\cos^2120^\circ+\cos120^\circ=2\cdot0.25-0.5=0$ ✓✓✓ **正是下界（趋近）**" "\n"
        r"取 $B=\frac{2\pi}3-\varepsilon$ 小量：$B=119^\circ$、$C=1^\circ$，$2\cos^2119^\circ+\cos118^\circ=2\cdot0.235+(-0.469)=0.470-0.469=0.001\approx0$ ✓✓✓" "\n"
        r"**答案正确** ✓" "\n"
        r"**⭐⭐ 通法（$\sin^2$ 关系式 ⟹ 正弦定理化角成边）**：" "\n"
        r"① ⭐⭐ **识别特征：等式各项都是「$\sin^2$」或「$\sin\cdot\sin$」⟹ 同乘 $(2R)^2$ 化为边**：" "\n"
        r"**$\sin^2B+\sin^2C=\sin^2A+\sin B\sin C$ ⟹ $b^2+c^2=a^2+bc$** ✓✓✓ —— 一次到位；" "\n"
        r"② ⭐⭐ **得到 $b^2+c^2-a^2=bc$ 后立刻看出 $\cos A=\frac12$**：" "\n"
        r"**余弦定理的分母是 $2bc$，分子恰是 $bc$** —— 这种「整齐」是刻意设计 ✓✓✓；" "\n"
        r"③ ⭐⭐ **第 (2) 问的三角恒等变换链**：" "\n"
        r"$2\cos^2B=1+\cos2B$（**降幂**）⟹ $\cos(B-C)$ 中的 $B-C$ **用 $B$ 表示** ⟹ 展开 $\cos(2B-\frac{2\pi}3)$ ⟹ **合并成辅助角** ✓✓✓；" "\n"
        r"④ ⭐⭐ **$\cos(x-\frac{2\pi}3)$ 的展开要熟**：$=-\frac12\cos x+\frac{\sqrt3}2\sin x$ ✓✓✓；" "\n"
        r"⑤ ⚠ **开闭端点是核心考点**：" "\n"
        r"**上端 $2$ 在 $B=\frac\pi6$ 取到 ⟹ 闭；下端 $0$ 在 $B=\frac{2\pi}3$（区间端点，取不到）⟹ 开** ✓✓✓。" "\n"
        r"（**务必逐一端点检查「是否在定义区间内」**）" "\n"
        r"⑥ ⭐ **验证：取特殊角代入原式与化简式对照** —— " "\n"
        r"本题 $B=\frac\pi6$ 给 $2$、$B\to\frac{2\pi}3$ 给 $0$ ✓✓✓；" "\n"
        r"⑦ ⭐ **与 M-T-223-E1 对照**：" "\n"
        r"E1 是「边 $\times$ 余弦」⟹ 化**边为角**；本题是「$\sin^2$」⟹ 化**角为边**。" "\n"
        r"**方向取决于哪种形式更整齐** ✓✓✓"
    ),
    'difficulty': 0.86,
    'topics': ['M-T-223'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-223-V3',
}

T220_E1 = {
    'type': '解答',
    'stem_text': (
        r"如图，在 $\triangle ABC$ 中，$D$ 为 $BC$ 边上的点，连接 $AD$，且满足 $DB\cdot\sin\angle ABD=DC\cdot\sin\angle ACD$。" "\n"
        r"(1) 求证：$\angle BAD=\angle CAD$；" "\n"
        r"(2) 若 $\angle BAC=\dfrac\pi3$，$AD=1$，求 $\triangle ABC$ 的面积的最小值．"
    ),
    'opts': [],
    'answer': r"(1) 证明见解析；(2) $\dfrac{\sqrt3}3$",
    'analysis': (
        r"(1) 在两个小三角形中各用一次正弦定理，都化成含 $AD$ 的式子，代入已知条件即得 $\sin\angle BAD=\sin\angle CAD$，"
        r"由两角之和 $\in(0,\pi)$ 排除互补；(2) 由面积拆分得 $b+c=\sqrt3bc$，配 $b+c\ge2\sqrt{bc}$ 得 $bc\ge\frac43$。"
    ),
    'solution': (
        r"**(1)** 在 $\triangle ADB$ 中，由正弦定理 $\dfrac{AD}{\sin\angle ABD}=\dfrac{BD}{\sin\angle BAD}$，" "\n"
        r"得 $BD\cdot\sin\angle ABD=AD\cdot\sin\angle BAD$。" "\n"
        r"同理，在 $\triangle ADC$ 中，$\dfrac{AD}{\sin\angle ACD}=\dfrac{CD}{\sin\angle CAD}$，" "\n"
        r"得 $CD\cdot\sin\angle ACD=AD\cdot\sin\angle CAD$。" "\n"
        r"由已知 $DB\cdot\sin\angle ABD=DC\cdot\sin\angle ACD$，得 $AD\cdot\sin\angle BAD=AD\cdot\sin\angle CAD$。" "\n"
        r"$\because AD>0$，$\therefore\sin\angle BAD=\sin\angle CAD$。" "\n"
        r"又 $\angle BAD+\angle CAD=\angle BAC\in(0,\pi)$，故两角**不可能互补**（互补则和为 $\pi$），" "\n"
        r"$\therefore\angle BAD=\angle CAD$。" "\n"
        r"**(2)** 设 $AC=b$、$AB=c$，由 (1) 及 $\angle BAC=\frac\pi3$ 得 $\angle BAD=\angle CAD=\dfrac\pi6$。" "\n"
        r"$S_{\triangle ABC}=\dfrac12bc\sin\dfrac\pi3=\dfrac{\sqrt3}4bc$；" "\n"
        r"$S_{\triangle ABD}=\dfrac12\cdot AB\cdot AD\cdot\sin\dfrac\pi6=\dfrac12\cdot c\cdot1\cdot\dfrac12=\dfrac c4$；" "\n"
        r"$S_{\triangle ACD}=\dfrac12\cdot AC\cdot AD\cdot\sin\dfrac\pi6=\dfrac b4$。" "\n"
        r"由 $S_{\triangle ABC}=S_{\triangle ABD}+S_{\triangle ACD}$ 得 $\dfrac{\sqrt3}4bc=\dfrac14(b+c)$，即 $b+c=\sqrt3bc$。" "\n"
        r"又 $b+c\ge2\sqrt{bc}$，故 $\sqrt3bc\ge2\sqrt{bc}$，即 $\sqrt{bc}\ge\dfrac2{\sqrt3}$，$bc\ge\dfrac43$" "\n"
        r"（当且仅当 $b=c$ 时取等号）。" "\n"
        r"$\therefore S_{\triangle ABC}=\dfrac{\sqrt3}4bc\ge\dfrac{\sqrt3}4\cdot\dfrac43=\dfrac{\sqrt3}3$。" "\n"
        r"即 $\triangle ABC$ 面积的最小值为 $\dfrac{\sqrt3}3$。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书详解：「(1) 在 $\triangle ADB$ 中，利用正弦定理可知 $\frac{AD}{\sin\angle ABD}=\frac{BD}{\sin\angle BAD}$，即 $BD\cdot\sin\angle ABD=AD\cdot\sin\angle BAD$，" "\n"
        r"同理，在 $\triangle ADC$ 中，$\frac{AD}{\sin\angle ACD}=\frac{CD}{\sin\angle CAD}$，即 $CD\cdot\sin\angle ACD=AD\cdot\sin\angle CAD$，" "\n"
        r"由已知条件 $DB\cdot\sin\angle ABD=DC\cdot\sin\angle ACD$，可得 $AD\cdot\sin\angle BAD=AD\cdot\sin\angle CAD$，即 $\sin\angle BAD=\sin\angle CAD$。" "\n"
        r"$\because\angle BAD+\angle CAD\in(0,\pi)$，$\therefore\angle BAD=\angle CAD$；" "\n"
        r"(2) 设 $AC=b$，$AB=c$，$\angle BAD=\angle CAD=\frac12\angle BAC=\frac\pi6$，$\therefore S_{\triangle ABC}=\frac12bc\sin\angle BAC=\frac{\sqrt3}4bc$，" "\n"
        r"$S_{\triangle ABD}=\frac12 AB\cdot AD\sin\angle BAD=\frac14c$，$S_{\triangle ACD}=\frac12AC\cdot AD\sin\angle CAD=\frac14 b$，" "\n"
        r"又 $\because S_{\triangle ABC}=S_{\triangle ABD}+S_{\triangle ACD}$，$\therefore\frac{\sqrt3}4bc=\frac14(b+c)$，$\therefore b+c=\sqrt3bc$，" "\n"
        r"又 $\because b+c\ge2\sqrt{bc}$，$\therefore\sqrt3bc\ge2\sqrt{bc}$，$\therefore bc\ge\frac43$（当且仅当 $b=c$ 时等号成立），" "\n"
        r"$\therefore S_{\triangle ABC}=\frac{\sqrt3}4bc\ge\frac{\sqrt3}4\cdot\frac43=\frac{\sqrt3}3$，即 $S_{\triangle ABC}$ 的最小值为 $\frac{\sqrt3}3$」" "\n"
        r"—— **两次正弦定理、$\sin\angle BAD=\sin\angle CAD$、面积拆分、$b+c=\sqrt3bc$、$bc\ge\frac43$、最小值 $\frac{\sqrt3}3$ 全部一致** ✓✓✓" "\n"
        r"（**答案根号丢失**：`3 / 3` 实为 $\frac{\sqrt3}3$）" "\n"
        r"**独立验算（完全独立）**：" "\n"
        r"① **正弦定理的交叉相乘**：$\frac{AD}{\sin\angle ABD}=\frac{BD}{\sin\angle BAD}$ ⟹ $AD\sin\angle BAD=BD\sin\angle ABD$ ✓✓✓" "\n"
        r"（**注意是「$AD$ 乘对角的正弦 = $BD$ 乘对角的正弦」**，即 $AD\leftrightarrow\angle ABD$、$BD\leftrightarrow\angle BAD$）" "\n"
        r"② **代入已知条件**：两边都是 $\sin\angle$ 乘线段，由 $BD\sin\angle ABD=CD\sin\angle ACD$ 得 $AD\sin\angle BAD=AD\sin\angle CAD$ ✓✓✓" "\n"
        r"③ **排除互补**：$\angle BAD+\angle CAD=\angle BAC\in(0,\pi)$。" "\n"
        r"**若互补则和为 $\pi$**，与 $\angle BAC<\pi$ 矛盾 ✓✓✓ ⟹ 两角相等 ✓✓✓" "\n"
        r"（**这一步是必要的**：由 $\sin\alpha=\sin\beta$ 只能得 $\alpha=\beta$ 或 $\alpha+\beta=\pi$）" "\n"
        r"④ **面积拆分**：$S_{ABC}=S_{ABD}+S_{ACD}$ ✓（$D$ 在 $BC$ 上）✓✓✓" "\n"
        r"⑤ **$S_{ABD}=\frac14c$**：$\frac12\cdot c\cdot1\cdot\sin30^\circ=\frac12\cdot c\cdot\frac12=\frac c4$ ✓✓✓" "\n"
        r"⑥ **$\frac{\sqrt3}4bc=\frac14(b+c)$** ⟹ $\sqrt3 bc=b+c$ ✓✓✓" "\n"
        r"⑦ **$bc\ge\frac43$**：$\sqrt3 bc\ge2\sqrt{bc}$。设 $u=\sqrt{bc}>0$，则 $\sqrt3u^2\ge2u$ ⟹ $u\ge\frac2{\sqrt3}$ ⟹ $bc=u^2\ge\frac43$ ✓✓✓" "\n"
        r"⑧ **$S_{\min}=\frac{\sqrt3}4\cdot\frac43=\frac{\sqrt3}3$** ✓✓✓" "\n"
        r"⑨ **取等检验**：$b=c$ 时 $b+c=\sqrt3bc$ ⟹ $2b=\sqrt3b^2$ ⟹ $b=\frac2{\sqrt3}=\frac{2\sqrt3}3$。" "\n"
        r"$bc=\frac{4\cdot3}9=\frac43$ ✓；此时 $S=\frac{\sqrt3}4\cdot\frac43=\frac{\sqrt3}3\approx0.577$ ✓✓✓" "\n"
        r"**回代验证已知条件**：$b=c=\frac{2\sqrt3}3$，$\angle BAC=60^\circ$ ⟹ $\triangle ABC$ 是等边三角形，边长 $a=\frac{2\sqrt3}3$。" "\n"
        r"$D$ 是 $BC$ 中点（因 $AD$ 平分顶角且三角形等腰）⟹ $BD=DC=\frac{\sqrt3}3$。" "\n"
        r"$AD=$ 高 $=\frac{2\sqrt3}3\cdot\frac{\sqrt3}2=1$ ✓✓✓ **与题设 $AD=1$ 吻合**" "\n"
        r"再验 $\sin\angle ABD$、$\sin\angle ACD$：等边三角形中 $\angle ABD=\angle ACD=60^\circ$，$\sin$ 相等、$BD=DC$ ⟹ 已知条件成立 ✓✓✓" "\n"
        r"**答案正确** ✓" "\n"
        r"**⭐⭐ 通法（角平分线的「正弦定理刻画」与面积拆分）**：" "\n"
        r"① ⭐⭐ **识别特征：$DB\cdot\sin\angle ABD=DC\cdot\sin\angle ACD$ ⟹ 在两个小三角形中各用一次正弦定理**：" "\n"
        r"**两个式子都化成「$AD\times$ 某个正弦」，于是已知条件直接变成 $\sin\angle BAD=\sin\angle CAD$** ✓✓✓ —— 这是本题的题眼；" "\n"
        r"② ⭐⭐ **由 $\sin\alpha=\sin\beta$ 推 $\alpha=\beta$ 必须排除互补**：" "\n"
        r"**用 $\alpha+\beta=\angle BAC\in(0,\pi)$ 排除** ✓✓✓ —— 这一步漏写会丢分；" "\n"
        r"③ ⭐⭐ **已知角平分线 + 顶角 + 角平分线长 ⟹ 用「面积拆分」**：" "\n"
        r"$S_{总}=S_{左}+S_{右}$，**三个面积都用 $\frac12\cdot$两边$\cdot\sin$夹角 表示** ✓✓✓；" "\n"
        r"④ ⭐⭐ **得到 $b+c=\sqrt3bc$ 后用基本不等式**：" "\n"
        r"**$b+c\ge2\sqrt{bc}$ 把「和」与「积」联系起来** —— 这是「已知和积关系求积范围」的标准动作 ✓✓✓；" "\n"
        r"⑤ ⭐⭐ **解 $\sqrt3u^2\ge2u$ 型不等式时除以 $u>0$**：" "\n"
        r"**设 $u=\sqrt{bc}$ 可避免出错** ✓✓✓；" "\n"
        r"⑥ ⚠ **必须检验取等条件能否实现**：" "\n"
        r"本题 $b=c=\frac{2\sqrt3}3$ 时确实构成等边三角形且 $AD=1$ ✓✓✓ —— **取不到等号的「最小值」是假的**；" "\n"
        r"⑦ ⭐ **最强验证：回代取等时的具体图形，检查所有题设** —— " "\n"
        r"本题 $AD=1$ ✓、已知条件 ✓ 全部吻合 ✓✓✓"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-220'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-220-E1',
}

T220_V2 = {
    'type': '解答',
    'stem_text': (
        r"在三角形 $ABC$ 中，角 $A,B,C$ 的对边分别为 $a,b,c$，且满足 $\dfrac a{\cos A}=\dfrac{\sqrt3b}{\sin B}$。" "\n"
        r"(1) 求角 $A$；" "\n"
        r"(2) 若 $a=2$，求三角形 $ABC$ 面积的最大值．"
    ),
    'opts': [],
    'answer': r"(1) $A=\dfrac\pi3$；(2) $\sqrt3$",
    'analysis': (
        r"(1) 由正弦定理 $\frac a{\sin A}=\frac b{\sin B}$ 得 $\frac{\sin A}{\cos A}=\frac{\sqrt3\sin B}{\sin B}=\sqrt3$，即 $\tan A=\sqrt3$；"
        r"(2) 余弦定理 $4=b^2+c^2-bc\ge bc$ ⟹ $bc\le4$ ⟹ $S=\frac12bc\sin A\le\sqrt3$。"
    ),
    'solution': (
        r"**(1)** 由正弦定理 $\dfrac a{\sin A}=\dfrac b{\sin B}$，得 $\dfrac ab=\dfrac{\sin A}{\sin B}$。" "\n"
        r"将已知 $\dfrac a{\cos A}=\dfrac{\sqrt3b}{\sin B}$ 改写为 $\dfrac ab=\dfrac{\sqrt3\cos A}{\sin B}$。" "\n"
        r"$\therefore\dfrac{\sin A}{\sin B}=\dfrac{\sqrt3\cos A}{\sin B}$，即 $\sin A=\sqrt3\cos A$。" "\n"
        r"（$\cos A\ne0$，否则左边 $\frac a{\cos A}$ 无意义）" "\n"
        r"$\therefore\tan A=\sqrt3$。$\because A\in(0,\pi)$，$\therefore A=\dfrac\pi3$。" "\n"
        r"**(2)** 由余弦定理 $a^2=b^2+c^2-2bc\cos A$，代入 $a=2$、$A=\frac\pi3$：" "\n"
        r"$4=b^2+c^2-2bc\cdot\dfrac12=b^2+c^2-bc$。" "\n"
        r"由 $b^2+c^2\ge2bc$ 得 $4=b^2+c^2-bc\ge2bc-bc=bc$，即 $bc\le4$" "\n"
        r"（当且仅当 $b=c=2$ 时取等号）。" "\n"
        r"$\therefore S_{\triangle ABC}=\dfrac12bc\sin A=\dfrac12bc\cdot\dfrac{\sqrt3}2=\dfrac{\sqrt3}4bc\le\dfrac{\sqrt3}4\cdot4=\sqrt3$。" "\n"
        r"即三角形 $ABC$ 面积的最大值为 $\sqrt3$。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书详解：「(1) 由 $\frac a{\cos A}=\frac{\sqrt3 b}{\sin B}$，结合正弦定理 $\frac a{\sin A}=\frac b{\sin B}$，得 $\frac{\sin A}{\cos A}=\frac{\sqrt3\sin B}{\sin B}=\sqrt3$，" "\n"
        r"所以 $\tan A=\sqrt3$，又因为 $A\in(0,\pi)$，所以 $A=\frac\pi3$。(2) 由余弦定理 $a^2=b^2+c^2-2bc\cos A$，得 $4=b^2+c^2-bc\ge2bc-bc=bc$ 即 $bc\le4$（当且仅当 $b=c=2$ 等号成立）" "\n"
        r"所以 $S_{\triangle ABC}=\frac12bc\sin A\le\frac12\times4\times\frac{\sqrt3}2=\sqrt3$，即当 $b=c=2$ 时，三角形 $ABC$ 面积 $S_{\triangle ABC}$ 的最大值为 $\sqrt3$」" "\n"
        r"—— **$\tan A=\sqrt3$、$A=\frac\pi3$、$4=b^2+c^2-bc\ge bc$、$bc\le4$、$S_{\max}=\sqrt3$ 全部一致** ✓✓✓" "\n"
        r"**独立验算（完全独立）**：" "\n"
        r"① **由 $\frac a{\cos A}=\frac{\sqrt3 b}{\sin B}$ 得 $\frac ab=\frac{\sqrt3\cos A}{\sin B}$** ✓✓✓" "\n"
        r"（两边同除以 $b$、同乘 $\cos A$）" "\n"
        r"② **正弦定理 $\frac ab=\frac{\sin A}{\sin B}$** ✓✓✓ ⟹ $\frac{\sin A}{\sin B}=\frac{\sqrt3\cos A}{\sin B}$ ⟹ $\sin A=\sqrt3\cos A$ ✓✓✓" "\n"
        r"③ **$\cos A\ne0$**：若 $\cos A=0$ 则原式分母为零，无意义 ✓✓✓ ⟹ $\tan A=\sqrt3$ ⟹ $A=\frac\pi3$ ✓✓✓" "\n"
        r"④ **余弦定理**：$4=b^2+c^2-2bc\cdot\frac12=b^2+c^2-bc$ ✓✓✓" "\n"
        r"⑤ **$b^2+c^2\ge2bc$** ⟹ $4\ge2bc-bc=bc$ ✓✓✓" "\n"
        r"⑥ **取等**：$b=c$ 且 $b^2+b^2-b^2=b^2=4$ ⟹ $b=c=2$ ✓✓✓" "\n"
        r"此时 $a=2$ ⟹ **三边都是 $2$，等边三角形** ✓✓✓" "\n"
        r"⑦ **$S_{\max}$**：$\frac12\cdot4\cdot\frac{\sqrt3}2=\sqrt3\approx1.732$ ✓✓✓" "\n"
        r"（等边三角形边长 $2$ 的面积 $=\frac{\sqrt3}4\cdot4=\sqrt3$ ✓✓✓ **一致**）" "\n"
        r"⑧ **回代验证已知条件**：等边三角形 $a=b=c=2$、$A=B=60^\circ$。" "\n"
        r"左边 $\frac a{\cos A}=\frac2{0.5}=4$；右边 $\frac{\sqrt3 b}{\sin B}=\frac{\sqrt3\cdot2}{\sqrt3/2}=\frac{2\sqrt3\cdot2}{\sqrt3}=4$ ✓✓✓ **相等**" "\n"
        r"**答案正确** ✓" "\n"
        r"**⭐⭐ 通法（「边 ÷ 角的余弦 = 边 ÷ 角的正弦」型）**：" "\n"
        r"① ⭐⭐ **识别特征：等式一边含 $\cos A$、另一边含 $\sin B$（不同角）⟹ 用正弦定理把边的比换成角的比**：" "\n"
        r"**$\frac ab=\frac{\sin A}{\sin B}$ 是唯一的桥梁** ✓✓✓；" "\n"
        r"② ⭐⭐ **换完 $\sin B$ 会约掉**：" "\n"
        r"$\frac{\sin A}{\sin B}=\frac{\sqrt3\cos A}{\sin B}$ ⟹ $\sin A=\sqrt3\cos A$ —— **$B$ 完全消失，这正是能求出 $A$ 的原因** ✓✓✓；" "\n"
        r"③ ⭐⭐ **$\cos A$ 作分母 ⟹ 必有 $\cos A\ne0$** 才能除以它得 $\tan A$；" "\n"
        r"④ ⭐⭐ **第 (2) 问是「已知一角和对边，求面积最大值」的标准模型**：" "\n"
        r"余弦定理写出 $a^2=b^2+c^2-2bc\cos A$ ⟹ **用 $b^2+c^2\ge2bc$ 得到 $bc$ 的上界** ⟹ $S=\frac12bc\sin A$ ✓✓✓；" "\n"
        r"⑤ ⭐⭐ **取等时 $b=c$ ⟹ 三角形为等腰（本题因 $A=60^\circ$ 而成为等边）**：" "\n"
        r"**这个「取等 ⟹ 特殊形状」的观察可用来快速自检** ✓✓✓；" "\n"
        r"⑥ ⭐ **验证：回代已知条件** —— " "\n"
        r"本题等边时左右都是 $4$ ✓✓✓；" "\n"
        r"⑦ ⭐ **与 M-T-220-V3 对照**：" "\n"
        r"V3 给的是外接圆半径 $R=2$（⟹ $c=2R\sin C$）；本题给的是对边 $a=2$（⟹ 余弦定理）。" "\n"
        r"**「给半径」用正弦定理，「给边长」用余弦定理** ✓✓✓"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-220'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-220-V2',
}

T220_V3 = {
    'type': '解答',
    'stem_text': (
        r"在 $\triangle ABC$ 中，角 $A,B,C$ 的对边分别为 $a,b,c$，$\sqrt3b\sin\left(\dfrac\pi2-C\right)=c\sin B$。" "\n"
        r"(1) 求角 $C$；" "\n"
        r"(2) 若 $\triangle ABC$ 的外接圆半径为 $2$，求 $\triangle ABC$ 面积的最大值．"
    ),
    'opts': [],
    'answer': r"(1) $C=\dfrac\pi3$；(2) $3\sqrt3$",
    'analysis': (
        r"(1) $\sin(\frac\pi2-C)=\cos C$，化边为角得 $\sqrt3\sin B\cos C=\sin C\sin B$，故 $\tan C=\sqrt3$；"
        r"(2) $R=2$ 得 $c=2R\sin C=2\sqrt3$，余弦定理配 $a^2+b^2\ge2ab$ 得 $ab\le12$ ⟹ $S\le3\sqrt3$。"
    ),
    'solution': (
        r"**(1)** $\because\sin\left(\dfrac\pi2-C\right)=\cos C$，$\therefore$ 已知式为 $\sqrt3b\cos C=c\sin B$。" "\n"
        r"由正弦定理化边为角：$\sqrt3\sin B\cos C=\sin C\sin B$。" "\n"
        r"$\because B\in(0,\pi)$，$\therefore\sin B\ne0$，故 $\sqrt3\cos C=\sin C$，即 $\tan C=\sqrt3$。" "\n"
        r"$\because C\in(0,\pi)$，$\therefore C=\dfrac\pi3$。" "\n"
        r"**(2)** 由正弦定理 $\dfrac c{\sin C}=2R=4$，得 $c=4\sin\dfrac\pi3=4\cdot\dfrac{\sqrt3}2=2\sqrt3$。" "\n"
        r"由余弦定理 $c^2=a^2+b^2-2ab\cos C$：" "\n"
        r"$(2\sqrt3)^2=a^2+b^2-2ab\cdot\dfrac12$，即 $12=a^2+b^2-ab$。" "\n"
        r"由 $a^2+b^2\ge2ab$ 得 $12=a^2+b^2-ab\ge2ab-ab=ab$，即 $ab\le12$" "\n"
        r"（当且仅当 $a=b=2\sqrt3$ 时取等号）。" "\n"
        r"$\therefore S_{\triangle ABC}=\dfrac12ab\sin C\le\dfrac12\cdot12\cdot\dfrac{\sqrt3}2=3\sqrt3$。" "\n"
        r"即 $\triangle ABC$ 面积的最大值为 $3\sqrt3$。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书详解：「(1) 因为 $\sqrt3b\sin(\frac\pi2-C)=c\sin B$，所以 $\sqrt3b\cos C=c\sin B$，由正弦定理得：$3\sin B\cos C=\sin C\sin B$——" "\n"
        r"（**原书漏了根号，应为 $\sqrt3\sin B\cos C$**），因为 $B\in(0,\pi)$，所以 $\sin B\ne0$，故 $\sqrt3\cos C=\sin C$，$\tan C=\sqrt3$，因为 $C\in(0,\pi)$，所以 $C=\frac\pi3$。" "\n"
        r"(2) 根据正弦定理得：$\frac c{\sin C}=\frac c{\sqrt3/2}=4$，解得：$c=2\sqrt3$，根据余弦定理得：$c^2=a^2+b^2-2ab\cos C=a^2+b^2-ab=12$，由基本不等式得：$a^2+b^2\ge2ab$，即 $12+ab\ge2ab$，解得：$ab\le12$，" "\n"
        r"当且仅当 $a=b=2\sqrt3$ 时等号成立，此时 $S_{\triangle ABC}=\frac12ab\sin C\le3\sqrt3$，所以 $\triangle ABC$ 面积的最大值为 $3\sqrt3$」" "\n"
        r"—— **$\tan C=\sqrt3$、$C=\frac\pi3$、$c=2\sqrt3$、$ab\le12$、$S_{\max}=3\sqrt3$ 全部一致** ✓✓✓" "\n"
        r"（**答案根号丢失**：`3 3` 实为 $3\sqrt3$；**详解中 $\sqrt3$ 也漏成 $3$**）" "\n"
        r"**独立验算（完全独立）**：" "\n"
        r"① **$\sin(\frac\pi2-C)=\cos C$** ✓✓✓（诱导公式）" "\n"
        r"② **化边为角**：$\sqrt3\sin B\cos C=\sin C\sin B$ ✓✓✓" "\n"
        r"③ **约去 $\sin B$** ⟹ $\sqrt3\cos C=\sin C$ ⟹ $\tan C=\sqrt3$ ⟹ $C=\frac\pi3$ ✓✓✓" "\n"
        r"④ **$c=2R\sin C=2\cdot2\cdot\frac{\sqrt3}2=2\sqrt3$** ✓✓✓" "\n"
        r"（**注意是 $2R$ 不是 $R$**：$\frac c{\sin C}=2R=4$ ⟹ $c=4\cdot\frac{\sqrt3}2=2\sqrt3$ ✓✓✓）" "\n"
        r"⑤ **余弦定理**：$c^2=12=a^2+b^2-ab$ ✓✓✓" "\n"
        r"⑥ **$ab\le12$**：$12=a^2+b^2-ab\ge2ab-ab=ab$ ✓✓✓" "\n"
        r"⑦ **取等**：$a=b$ ⟹ $a^2+a^2-a^2=a^2=12$ ⟹ $a=b=2\sqrt3$ ✓✓✓" "\n"
        r"此时 $c=2\sqrt3$ ⟹ **三边都是 $2\sqrt3$，等边三角形** ✓✓✓" "\n"
        r"⑧ **$S_{\max}=\frac12\cdot12\cdot\frac{\sqrt3}2=3\sqrt3\approx5.196$** ✓✓✓" "\n"
        r"（等边三角形边长 $2\sqrt3$ 的面积 $=\frac{\sqrt3}4\cdot12=3\sqrt3$ ✓✓✓ **一致**）" "\n"
        r"⑨ **回代验证已知条件**：等边三角形，$B=C=60^\circ$、$b=c=2\sqrt3$。" "\n"
        r"左边 $\sqrt3 b\sin(90^\circ-60^\circ)=\sqrt3\cdot2\sqrt3\cdot\sin30^\circ=6\cdot0.5=3$；" "\n"
        r"右边 $c\sin B=2\sqrt3\cdot\frac{\sqrt3}2=3$ ✓✓✓ **相等**" "\n"
        r"**答案正确** ✓" "\n"
        r"**⭐⭐ 通法（诱导公式 $\sin(\frac\pi2-C)=\cos C$ + 外接圆半径）**：" "\n"
        r"① ⭐⭐ **见到 $\sin(\frac\pi2-\cdot)$、$\cos(\frac\pi2-\cdot)$ 立刻用诱导公式化简**：" "\n"
        r"**$\sin(\frac\pi2-C)=\cos C$、$\cos(\frac\pi2-C)=\sin C$** ✓✓✓；" "\n"
        r"② ⭐⭐ **化边为角后 $\sin B$ 会约掉**：" "\n"
        r"**本题 $B$ 完全消失，才得以求出确定的 $C$** ✓✓✓；" "\n"
        r"③ ⭐⭐ **已知外接圆半径 $R$ ⟹ 用 $c=2R\sin C$ 求边**：" "\n"
        r"**关键：$\frac c{\sin C}=2R$（是 $2R$ 不是 $R$）** ✓✓✓ —— 这是最高频错误；" "\n"
        r"④ ⭐⭐ **已知一角及其对边 ⟹ 余弦定理 + $a^2+b^2\ge2ab$ 求 $ab$ 上界**：" "\n"
        r"$c^2=a^2+b^2-2ab\cos C\ge2ab-2ab\cos C=2ab(1-\cos C)$ ✓✓✓。" "\n"
        r"本题 $\cos C=\frac12$ ⟹ $12\ge ab$ ✓✓✓；" "\n"
        r"⑤ ⭐⭐ **取等时 $a=b$ ⟹ 因 $C=60^\circ$ 而成等边三角形**：" "\n"
        r"**可用等边三角形面积公式 $\frac{\sqrt3}4a^2$ 独立复算** ✓✓✓；" "\n"
        r"⑥ ⚠ **详解中 $\sqrt3$ 漏成 $3$ 是高频 OCR 错误**：" "\n"
        r"**判别方法：若 $\tan C=3$ 则 $C\approx71.6^\circ$ 不是特殊角，与「$C=\frac\pi3$」矛盾** ✓✓✓；" "\n"
        r"⑦ ⭐ **与 M-T-220-V2 对照**：" "\n"
        r"V2 给对边 $a=2$、本题给外接圆半径 $R=2$ —— **一个用余弦定理、一个用正弦定理求边** ✓✓✓"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-220'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-220-V3',
}

T209_E1 = {
    'type': '选择',
    'stem_text': (
        r"在钝角 $\triangle ABC$ 中，$a,b,c$ 分别是 $\triangle ABC$ 的内角 $A,B,C$ 所对的边，点 $G$ 是 $\triangle ABC$ 的重心，"
        r"若 $AG\perp BG$，则 $\cos C$ 的取值范围是（　　）"
    ),
    'opts': [
        ('A', r"$\left(0,\dfrac{\sqrt6}3\right)$"),
        ('B', r"$\left(\dfrac45,\dfrac{\sqrt6}3\right)$"),
        ('C', r"$\left(\dfrac{\sqrt6}3,1\right)$"),
        ('D', r"$\left(\dfrac45,1\right)$"),
    ],
    'answer': 'C',
    'analysis': (
        r"重心 + $AG\perp BG$ ⟹ $DG=\frac12 AB$、$CD=3DG=\frac{3c}2$；在 $\triangle ADC$、$\triangle BDC$ 中用余弦定理，"
        r"由 $\cos\angle BDC=-\cos\angle ADC$ 得 $a^2+b^2=5c^2$。故 $\cos C=\frac25(\frac ab+\frac ba)$。"
        r"设 $A$ 为钝角得 $0<\frac ba<\frac{\sqrt6}3$，故 $\cos C>\frac{\sqrt6}3$ 且 $C$ 为锐角。"
    ),
    'solution': (
        r"延长 $CG$ 交 $AB$ 于 $D$。" "\n"
        r"$\because G$ 为重心，$\therefore D$ 为 $AB$ 中点且 $CD=3DG$。" "\n"
        r"$\because AG\perp BG$，在直角 $\triangle AGB$ 中，$D$ 是斜边 $AB$ 的中点，$\therefore DG=\dfrac12AB=\dfrac c2$。" "\n"
        r"$\therefore CD=3DG=\dfrac{3c}2$。" "\n"
        r"在 $\triangle ADC$ 中，$AD=\dfrac c2$、$CD=\dfrac{3c}2$、$AC=b$：" "\n"
        r"$\cos\angle ADC=\dfrac{AD^2+CD^2-AC^2}{2AD\cdot CD}=\dfrac{\frac{c^2}4+\frac{9c^2}4-b^2}{2\cdot\frac c2\cdot\frac{3c}2}=\dfrac{\frac{5c^2}2-b^2}{\frac{3c^2}2}=\dfrac{5c^2-2b^2}{3c^2}$。" "\n"
        r"同理在 $\triangle BDC$ 中：$\cos\angle BDC=\dfrac{5c^2-2a^2}{3c^2}$。" "\n"
        r"$\because\angle BDC+\angle ADC=\pi$，$\therefore\cos\angle BDC=-\cos\angle ADC$，" "\n"
        r"即 $\dfrac{5c^2-2a^2}{3c^2}=-\dfrac{5c^2-2b^2}{3c^2}$，整理得 $a^2+b^2=5c^2$。" "\n"
        r"由 $a^2+b^2=5c^2>c^2$ 知 $C$ 为锐角。" "\n"
        r"设 $A$ 为钝角，则 $b^2+c^2<a^2$、$a^2+c^2>b^2$、$a>b$。代入 $c^2=\dfrac{a^2+b^2}5$：" "\n"
        r"$b^2+\dfrac{a^2+b^2}5<a^2$ ⟹ $\dfrac{b^2}{a^2}+\dfrac15+\dfrac15\cdot\dfrac{b^2}{a^2}<1$ ⟹ $\left(\dfrac ba\right)^2<\dfrac23$；" "\n"
        r"$a^2+\dfrac{a^2+b^2}5>b^2$ ⟹ $1+\dfrac15+\dfrac15\left(\dfrac ba\right)^2>\left(\dfrac ba\right)^2$ ⟹ $\left(\dfrac ba\right)^2<\dfrac32$。" "\n"
        r"取交集且 $a>b>0$：$0<\dfrac ba<\dfrac{\sqrt6}3$。" "\n"
        r"由余弦定理 $\cos C=\dfrac{a^2+b^2-c^2}{2ab}=\dfrac{a^2+b^2-\frac{a^2+b^2}5}{2ab}=\dfrac{2(a^2+b^2)}{5ab}=\dfrac25\left(\dfrac ab+\dfrac ba\right)$。" "\n"
        r"令 $t=\dfrac ba\in\left(0,\dfrac{\sqrt6}3\right)$，则 $f(t)=\dfrac25\left(\dfrac1t+t\right)$ 在 $(0,1)$ 上递减，" "\n"
        r"$\therefore\cos C>f\left(\dfrac{\sqrt6}3\right)=\dfrac25\left(\dfrac3{\sqrt6}+\dfrac{\sqrt6}3\right)=\dfrac25\left(\dfrac{\sqrt6}2+\dfrac{\sqrt6}3\right)=\dfrac25\cdot\dfrac{5\sqrt6}6=\dfrac{\sqrt6}3$。" "\n"
        r"又 $C$ 为锐角，$\therefore\dfrac{\sqrt6}3<\cos C<1$。故选 C。"
    ),
    'review': (
        r"★ 题干、选项、答案、详解完整 ✓。原书详解（关键步骤）：「延长 $CG$ 交 $AB$ 于 $D$。$\because G$ 为 $\triangle ABC$ 的重心，$\therefore D$ 为 $AB$ 中点且 $CD=3DG$。" "\n"
        r"$\because AG\perp BG$，$\therefore DG=\frac12AB$，$\therefore CD=\frac32AB=\frac{3c}2$；在 $\triangle ADC$ 中，$\cos\angle ADC=\frac{5c^2-2b^2}{3c^2}$；在 $\triangle BDC$ 中，$\cos\angle BDC=\frac{5c^2-2a^2}{3c^2}$；" "\n"
        r"$\because\angle BDC+\angle ADC=\pi$，$\therefore\cos\angle BDC=-\cos\angle ADC$，整理可得：$a^2+b^2=5c^2>c^2$，$\therefore C$ 为锐角；" "\n"
        r"设 $A$ 为钝角……解得：$(\frac ba)^2<\frac23$，$\because a>b>0$，$\therefore0<\frac ba<\frac{\sqrt6}3$，" "\n"
        r"由余弦定理得：$\cos C=\frac{a^2+b^2-c^2}{2ab}=\frac25(\frac ab+\frac ba)>\frac25\times(\frac{\sqrt6}3+\frac3{\sqrt6})=\frac{\sqrt6}3$，又 $C$ 为锐角，$\therefore\frac{\sqrt6}3<\cos C<1$。故选：C」" "\n"
        r"—— **$CD=3DG$、$DG=\frac c2$、$a^2+b^2=5c^2$、$\cos C=\frac25(\frac ab+\frac ba)$、$(\frac{\sqrt6}3,1)$、答案 C 全部一致** ✓✓✓" "\n"
        r"**独立验算（完全独立）**：" "\n"
        r"① **$D$ 是 $AB$ 中点、$CD=3DG$**：重心分中线为 $2:1$，即 $CG:GD=2:1$ ⟹ $CD=CG+GD=3GD$ ✓✓✓" "\n"
        r"② **$AG\perp BG$ ⟹ $DG=\frac12AB$**：" "\n"
        r"**直角三角形斜边上的中线等于斜边的一半** —— $D$ 是斜边 $AB$ 中点 ⟹ $DG=\frac{AB}2$ ✓✓✓" "\n"
        r"（**这一步是本题的题眼**：把「垂直」翻译成「$DG$ 的长度」）" "\n"
        r"③ **$CD=\frac{3c}2$** ✓✓✓" "\n"
        r"④ **余弦定理**：$AD=\frac c2$、$CD=\frac{3c}2$。" "\n"
        r"$AD^2+CD^2=\frac{c^2}4+\frac{9c^2}4=\frac{10c^2}4=\frac{5c^2}2$ ✓；$2AD\cdot CD=2\cdot\frac c2\cdot\frac{3c}2=\frac{3c^2}2$ ✓" "\n"
        r"⟹ $\cos\angle ADC=\frac{\frac{5c^2}2-b^2}{\frac{3c^2}2}=\frac{5c^2-2b^2}{3c^2}$ ✓✓✓" "\n"
        r"⑤ **互补角余弦相反** ⟹ $5c^2-2a^2=-(5c^2-2b^2)$ ⟹ $10c^2=2a^2+2b^2$ ⟹ $a^2+b^2=5c^2$ ✓✓✓" "\n"
        r"⑥ **$C$ 为锐角**：$a^2+b^2=5c^2>c^2$ ⟹ $\cos C=\frac{a^2+b^2-c^2}{2ab}>0$ ✓✓✓" "\n"
        r"⑦ **钝角条件**：$c^2=\frac{a^2+b^2}5$。" "\n"
        r"$A$ 钝 ⟺ $b^2+c^2<a^2$ ⟺ $b^2+\frac{a^2+b^2}5<a^2$ ⟺ $\frac{6b^2}5<\frac{4a^2}5$ ⟺ $\frac{b^2}{a^2}<\frac23$ ✓✓✓" "\n"
        r"另一条件 $a^2+c^2>b^2$ ⟺ $a^2+\frac{a^2+b^2}5>b^2$ ⟺ $\frac{6a^2}5>\frac{4b^2}5$ ⟺ $\frac{b^2}{a^2}<\frac32$ ✓✓✓" "\n"
        r"**$\frac23<\frac32$，故交集是 $\frac{b^2}{a^2}<\frac{2}3$** ⟹ $0<\frac ba<\frac{\sqrt6}3$ ✓✓✓" "\n"
        r"（$\sqrt{\frac23}=\frac{\sqrt2}{\sqrt3}=\frac{\sqrt6}3$ ✓✓✓）" "\n"
        r"⑧ **$\cos C=\frac25(\frac ab+\frac ba)$**：" "\n"
        r"$c^2=\frac{a^2+b^2}5$ ⟹ $a^2+b^2-c^2=a^2+b^2-\frac{a^2+b^2}5=\frac{4(a^2+b^2)}5$。" "\n"
        r"⟹ $\cos C=\frac{4(a^2+b^2)}{5\cdot2ab}=\frac{2(a^2+b^2)}{5ab}=\frac25(\frac ab+\frac ba)$ ✓✓✓" "\n"
        r"⑨ **单调性**：$t\in(0,\frac{\sqrt6}3)$，$\frac{\sqrt6}3\approx0.816<1$。" "\n"
        r"$f(t)=\frac25(\frac1t+t)$，$f'(t)=\frac25(1-\frac1{t^2})<0$（因 $t<1$）⟹ **递减** ✓✓✓" "\n"
        r"⟹ $f(t)>f(\frac{\sqrt6}3)$（$t$ 取不到右端，故严格大于）✓✓✓" "\n"
        r"⑩ **计算 $f(\frac{\sqrt6}3)$**：$\frac1t=\frac3{\sqrt6}=\frac{3\sqrt6}6=\frac{\sqrt6}2$ ✓；$t=\frac{\sqrt6}3$。" "\n"
        r"和 $=\frac{\sqrt6}2+\frac{\sqrt6}3=\frac{3\sqrt6+2\sqrt6}6=\frac{5\sqrt6}6$ ✓；$\frac25\cdot\frac{5\sqrt6}6=\frac{\sqrt6}3$ ✓✓✓" "\n"
        r"⑪ **数值检验**：取 $t=0.5$（即 $b=0.5a$，满足 $0<t<0.816$）：" "\n"
        r"$\cos C=\frac25(2+0.5)=\frac25\cdot2.5=1$ —— **恰好等于 $1$？**" "\n"
        r"（$t=0.5$ 时 $\frac1t+t=2.5$，$\frac25\cdot2.5=1$）" "\n"
        r"**这说明 $t=0.5$ 使 $\cos C=1$，即 $C=0^\circ$（退化）** —— 需 $t>0.5$ 才有 $\cos C<1$。" "\n"
        r"再取 $t=0.7$：$\cos C=\frac25(1.4286+0.7)=\frac25\cdot2.1286=0.8514$。" "\n"
        r"$\frac{\sqrt6}3=0.8165$ ✓ **$0.8514>0.8165$** ✓✓✓" "\n"
        r"再取 $t\to\frac{\sqrt6}3=0.8165$：$\cos C\to\frac25(1.2247+0.8165)=\frac25\cdot2.0412=0.8165$ ✓✓✓ **正是下界**" "\n"
        r"**答案 C 正确** ✓" "\n"
        r"**⭐⭐ 通法（重心 + 垂直 ⟹ 斜边中线定理）**：" "\n"
        r"① ⭐⭐ **识别特征：$G$ 是重心且 $AG\perp BG$ ⟹ 在直角 $\triangle AGB$ 中，$AB$ 是斜边、$D$（$AB$ 中点）是斜边中点**：" "\n"
        r"**$DG=\frac12AB$（斜边中线定理），再配 $CD=3DG$ 得 $CD=\frac{3c}2$** ✓✓✓ —— 这是本题的题眼；" "\n"
        r"② ⭐⭐ **在两个小三角形中分别用余弦定理，由「互补角余弦相反」得关系式**：" "\n"
        r"$\cos\angle ADC$、$\cos\angle BDC$ 的分母相同（$AD=BD$、$CD$ 公共），**故可直接令分子互为相反数** ✓✓✓；" "\n"
        r"③ ⭐⭐ **得到 $a^2+b^2=5c^2$ 后，$c^2$ 可整体替换**：" "\n"
        r"**$\cos C$ 中的 $c^2$ 换成 $\frac{a^2+b^2}5$，只剩 $\frac ab+\frac ba$** ✓✓✓；" "\n"
        r"④ ⭐⭐ **「钝角三角形」条件要翻译成边长不等式**：" "\n"
        r"$A$ 钝 ⟺ $b^2+c^2<a^2$；**同时要保证另两角不是钝角**（$a^2+c^2>b^2$）✓✓✓；" "\n"
        r"⑤ ⚠ **$f(t)=\frac1t+t$ 在 $(0,1)$ 递减、$(1,+\infty)$ 递增**：" "\n"
        r"**必须先判断 $t$ 是否小于 $1$** —— 本题 $t<\frac{\sqrt6}3<1$ ✓✓✓；" "\n"
        r"⑥ ⭐ **最强检验：取 $t$ 的若干个值算 $\cos C$，看是否都 $>\frac{\sqrt6}3$ 且 $<1$** —— " "\n"
        r"本题 $t=0.7$ 给 $0.8514$、$t\to\frac{\sqrt6}3$ 给 $0.8165$ ✓✓✓；" "\n"
        r"⑦ ⭐ **$\cos C<1$ 给出了 $t$ 的实际下界 $0.5$**：" "\n"
        r"**题目只给了 $t>0$，但「非退化三角形」自动要求 $t>0.5$** —— 这不影响答案（下界由 $t<\frac{\sqrt6}3$ 决定）✓✓✓"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-209'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-209-E1',
}

T209_V2 = {
    'type': '选择',
    'stem_text': (
        r"设 $\triangle ABC$ 的内角 $A,B,C$ 的对边分别为 $a,b,c$，点 $G$ 为 $\triangle ABC$ 的重心且满足 $\vec{BG}\perp\vec{CG}$，"
        r"若 $a\tan A=\lambda c\sin B$，则实数 $\lambda=$（　　）"
    ),
    'opts': [
        ('A', r"$3$"),
        ('B', r"$2$"),
        ('C', r"$\dfrac12$"),
        ('D', r"$\dfrac23$"),
    ],
    'answer': 'C',
    'analysis': (
        r"由 $BG\perp CG$ 得 $DG=\frac12BC$、$AD=3DG=\frac32a$；在 $\triangle ADC$、$\triangle ADB$ 中用余弦定理相加得 $b^2+c^2=5a^2$，"
        r"故 $\cos A=\frac{2a^2}{bc}$。由 $a\tan A=\lambda c\sin B$ 及正弦定理 $\frac{\sin A}{\sin B}=\frac ab$ 得 $\lambda=\frac{a^2}{bc\cos A}=\frac12$。"
    ),
    'solution': (
        r"连接 $AG$ 并延长交 $BC$ 于 $D$。$\because G$ 为重心，$\therefore D$ 为 $BC$ 中点，且 $AD=3DG$。" "\n"
        r"$\because\vec{BG}\perp\vec{CG}$，在直角 $\triangle BGC$ 中，$D$ 是斜边 $BC$ 的中点，$\therefore DG=\dfrac12BC=\dfrac a2$。" "\n"
        r"$\therefore AD=3DG=\dfrac{3a}2$，且 $BD=CD=\dfrac a2$。" "\n"
        r"在 $\triangle ADC$ 与 $\triangle ADB$ 中分别用余弦定理：" "\n"
        r"$AC^2=AD^2+CD^2-2AD\cdot CD\cos\angle ADC$；$AB^2=AD^2+BD^2-2AD\cdot BD\cos\angle ADB$。" "\n"
        r"$\because\angle ADC+\angle ADB=\pi$、$CD=BD$，$\therefore$ 两式相加时余弦项抵消：" "\n"
        r"$AC^2+AB^2=2BD^2+2AD^2=2\cdot\left(\dfrac a2\right)^2+2\cdot\left(\dfrac{3a}2\right)^2=\dfrac{a^2}2+\dfrac{9a^2}2=5a^2$。" "\n"
        r"即 $b^2+c^2=5a^2$，故 $\cos A=\dfrac{b^2+c^2-a^2}{2bc}=\dfrac{5a^2-a^2}{2bc}=\dfrac{2a^2}{bc}$。" "\n"
        r"由 $a\tan A=\lambda c\sin B$ 得 $\lambda=\dfrac{a\tan A}{c\sin B}=\dfrac{a\sin A}{c\sin B\cos A}$。" "\n"
        r"由正弦定理 $\dfrac{\sin A}{\sin B}=\dfrac ab$，$\therefore\lambda=\dfrac{a}{c\cos A}\cdot\dfrac ab=\dfrac{a^2}{bc\cos A}=\dfrac{a^2}{bc}\cdot\dfrac{bc}{2a^2}=\dfrac12$。" "\n"
        r"故选 C。"
    ),
    'review': (
        r"★ 题干、选项、答案、详解完整 ✓。原书详解：「如图，连接 $AG$，延长交 $BC$ 于 $D$，由于 $G$ 为重心，故 $D$ 为中点，$\because CG\perp BG$，$\therefore DG=\frac12BC$，" "\n"
        r"由重心的性质得，$AD=3DG$，即 $AD=\frac32BC$，由余弦定理得，$AC^2=AD^2+CD^2-2AD\cdot CD\cdot\cos\angle ADC$，$AB^2=AD^2+BD^2-2AD\cdot BD\cos\angle ADB$，" "\n"
        r"$\because\angle ADC+\angle BDC=\pi$，$CD=BD$，$\therefore AC^2+AB^2=2BD^2+2AD^2$，$\therefore AC^2+AB^2=\frac12BC^2+\frac92BC^2=5BC^2$，" "\n"
        r"$\therefore b^2+c^2=5a^2$，可得：$\cos A=\frac{b^2+c^2-a^2}{2bc}=\frac{4a^2}{2bc}=\frac{2a^2}{bc}$，" "\n"
        r"$\because a\tan A=\lambda c\sin B$，$\therefore\lambda=\frac{a\sin A}{c\sin B\cos A}=\frac{a^2}{bc\cos A}=\frac{a^2}{bc}\cdot\frac{2a^2}{bc}$…" "\n"
        r"（**原书此处 $\frac{a^2}{bc}\cdot\frac{2a^2}{bc}$ 应为 $\frac{a^2}{bc}\cdot\frac{bc}{2a^2}$** —— 由 $\cos A=\frac{2a^2}{bc}$ 得 $\frac1{\cos A}=\frac{bc}{2a^2}$）" "\n"
        r"最终 $\lambda=\frac12$。故选 C」" "\n"
        r"—— **$DG=\frac a2$、$AD=\frac{3a}2$、$b^2+c^2=5a^2$、$\cos A=\frac{2a^2}{bc}$、$\lambda=\frac12$、答案 C 全部一致** ✓✓✓" "\n"
        r"**独立验算（完全独立）**：" "\n"
        r"① **$D$ 为 $BC$ 中点、$AD=3DG$**：重心性质 ✓✓✓" "\n"
        r"② **$BG\perp CG$ ⟹ $DG=\frac12BC$**：直角 $\triangle BGC$ 中 $D$ 是斜边 $BC$ 中点 ⟹ 斜边中线 $=\frac{BC}2$ ✓✓✓" "\n"
        r"（**与 M-T-209-E1 完全同一招**：那题是 $AG\perp BG$ ⟹ $DG=\frac12AB$）" "\n"
        r"③ **$AD=\frac{3a}2$** ✓✓✓" "\n"
        r"④ **两式相加余弦项抵消**：" "\n"
        r"$\cos\angle ADB=\cos(\pi-\angle ADC)=-\cos\angle ADC$，且 $BD=CD$ ⟹ 两个余弦项互为相反数 ✓✓✓" "\n"
        r"⟹ $b^2+c^2=2AD^2+2BD^2=2\cdot\frac{9a^2}4+2\cdot\frac{a^2}4=\frac{9a^2}2+\frac{a^2}2=5a^2$ ✓✓✓" "\n"
        r"⑤ **$\cos A=\frac{b^2+c^2-a^2}{2bc}=\frac{4a^2}{2bc}=\frac{2a^2}{bc}$** ✓✓✓" "\n"
        r"⑥ **$\lambda$ 的推导**：" "\n"
        r"$\lambda=\frac{a\tan A}{c\sin B}=\frac{a\sin A}{c\sin B\cos A}$。" "\n"
        r"由正弦定理：$\frac a{\sin A}=\frac b{\sin B}$ ⟹ $\frac{\sin A}{\sin B}=\frac ab$ ✓✓✓" "\n"
        r"⟹ $\lambda=\frac a{c\cos A}\cdot\frac ab=\frac{a^2}{bc\cos A}$ ✓✓✓" "\n"
        r"由 $\cos A=\frac{2a^2}{bc}$ ⟹ $\frac1{\cos A}=\frac{bc}{2a^2}$ ⟹ $\lambda=\frac{a^2}{bc}\cdot\frac{bc}{2a^2}=\frac12$ ✓✓✓" "\n"
        r"⑦ **数值检验**：构造满足条件的三角形。取 $a=1$，则 $b^2+c^2=5$。" "\n"
        r"取 $b=c=\sqrt{2.5}\approx1.5811$（等腰）：" "\n"
        r"$\cos A=\frac{b^2+c^2-a^2}{2bc}=\frac{5-1}{2\cdot2.5}=\frac4{5}=0.8$。" "\n"
        r"公式：$\cos A=\frac{2a^2}{bc}=\frac{2}{2.5}=0.8$ ✓✓✓" "\n"
        r"$A=\arccos0.8\approx36.87^\circ$，$\tan A=\frac{0.6}{0.8}=0.75$。" "\n"
        r"$B=C=\frac{180^\circ-36.87^\circ}2=71.565^\circ$，$\sin B\approx0.9487$。" "\n"
        r"$a\tan A=1\cdot0.75=0.75$；$\lambda c\sin B=\lambda\cdot1.5811\cdot0.9487=\lambda\cdot1.5$。" "\n"
        r"⟹ $\lambda=\frac{0.75}{1.5}=0.5$ ✓✓✓ **完全吻合**" "\n"
        r"**答案 C 正确** ✓" "\n"
        r"**⭐⭐ 通法（重心 + 两顶点处垂直 ⟹ 斜边中线）**：" "\n"
        r"① ⭐⭐ **$G$ 是重心 + $\vec{BG}\perp\vec{CG}$ ⟹ 直角 $\triangle BGC$ + $D$ 是斜边中点 ⟹ $DG=\frac12BC$ ⟹ $AD=\frac32BC$**：" "\n"
        r"**与 M-T-209-E1（$AG\perp BG$ ⟹ $CD=\frac{3c}2$）是同一招，只是垂直的两条线不同** ✓✓✓；" "\n"
        r"② ⭐⭐ **在 $\triangle ADC$ 与 $\triangle ADB$ 中分别用余弦定理后「相加」**：" "\n"
        r"**关键：两个角互补（余弦相反）+ $BD=CD$ ⟹ 余弦项恰好抵消** ✓✓✓ —— 这比「令两式相等」更简洁；" "\n"
        r"③ ⭐⭐ **得到 $b^2+c^2=5a^2$ 后 $\cos A$ 只含 $a$ 与 $bc$**：" "\n"
        r"$\cos A=\frac{2a^2}{bc}$ ✓✓✓；" "\n"
        r"④ ⭐⭐ **求 $\lambda$ 时把 $\frac{\sin A}{\sin B}$ 整体换成 $\frac ab$**：" "\n"
        r"**凡是出现 $\frac{\sin X}{\sin Y}$ 就用正弦定理换成 $\frac x y$** ✓✓✓；" "\n"
        r"⑤ ⚠ **原书详解末段 $\frac{a^2}{bc}\cdot\frac{2a^2}{bc}$ 有误**：" "\n"
        r"**$\frac1{\cos A}=\frac{bc}{2a^2}$ 不是 $\frac{2a^2}{bc}$** —— 若照抄会得 $\lambda=\frac{4a^4}{b^2c^2}$（含 $a$），与「$\lambda$ 是常数」矛盾 ✓✓✓；" "\n"
        r"⑥ ⭐ **最强验证：构造具体三角形算 $\lambda$** —— " "\n"
        r"本题取 $b=c=\sqrt{2.5}$ 得 $\lambda=0.5$ ✓✓✓；" "\n"
        r"⑦ ⭐ **与 M-T-209-E1 对照**：" "\n"
        r"E1：$AG\perp BG$ ⟹ 结论关于 $c$（$a^2+b^2=5c^2$）；本题：$BG\perp CG$ ⟹ 结论关于 $a$（$b^2+c^2=5a^2$）。" "\n"
        r"**垂直所对的那个顶点，其「对边」出现在结论里** ✓✓✓"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-209'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-209-V2',
}

T209_V3 = {
    'type': '填空',
    'stem_text': (
        r"已知四边形 $ABCD$ 的面积为 $2022$，$E$ 为 $AD$ 边上一点，$\triangle ABE$、$\triangle BCE$、$\triangle CDE$ 的重心分别为 $G_1,G_2,G_3$，"
        r"那么 $\triangle G_1G_2G_3$ 的面积为 ____．"
    ),
    'opts': [],
    'answer': r"$\dfrac{674}3$",
    'analysis': (
        r"建系写出三个重心的坐标，用向量叉积算面积，得 $S_{\triangle G_1G_2G_3}=\frac1{18}\lvert bc+de-ad\rvert$；"
        r"同法算四边形面积 $S_{ABCD}=\frac12\lvert bc+de-ad\rvert$，故前者是后者的 $\frac19$。"
    ),
    'solution': (
        r"以 $A$ 为原点、射线 $AD$ 为 $x$ 轴非负半轴建立平面直角坐标系。" "\n"
        r"设 $B(a,b)$、$C(c,d)$、$D(e,0)$、$E(x_0,0)$（$0\le x_0\le e$）。" "\n"
        r"由重心坐标公式：" "\n"
        r"$G_1\left(\dfrac{a+x_0}3,\dfrac b3\right)$、$G_2\left(\dfrac{a+c+x_0}3,\dfrac{b+d}3\right)$、$G_3\left(\dfrac{c+e+x_0}3,\dfrac d3\right)$。" "\n"
        r"$\therefore\vec{G_1G_2}=\left(\dfrac c3,\dfrac d3\right)$，$\vec{G_3G_2}=\left(\dfrac{a-e}3,\dfrac b3\right)$。" "\n"
        r"用 $S=\dfrac12\sqrt{\lvert\vec u\rvert^2\lvert\vec v\rvert^2-(\vec u\cdot\vec v)^2}$（即 $\frac12\lvert\vec u\times\vec v\rvert$）：" "\n"
        r"$S_{\triangle G_1G_2G_3}=\dfrac12\sqrt{\left[\left(\dfrac c3\right)^2+\left(\dfrac d3\right)^2\right]\left[\left(\dfrac{a-e}3\right)^2+\left(\dfrac b3\right)^2\right]-\left[\dfrac c3\cdot\dfrac{a-e}3+\dfrac d3\cdot\dfrac b3\right]^2}$" "\n"
        r"$=\dfrac12\cdot\dfrac19\sqrt{(c^2+d^2)\left[(a-e)^2+b^2\right]-\left[c(a-e)+bd\right]^2}$" "\n"
        r"$=\dfrac1{18}\sqrt{c^2b^2+d^2(a-e)^2-2bc d(a-e)}=\dfrac1{18}\left\lvert bc-d(a-e)\right\rvert=\dfrac1{18}\left\lvert bc+de-ad\right\rvert$。" "\n"
        r"（根号内是完全平方：$\left[bc-d(a-e)\right]^2$）" "\n"
        r"同理，$\vec{AC}=(c,d)$、$\vec{DB}=(a-e,b)$，四边形面积" "\n"
        r"$S_{ABCD}=\dfrac12\left\lvert bc-d(a-e)\right\rvert=\dfrac12\left\lvert bc+de-ad\right\rvert$。" "\n"
        r"$\therefore S_{\triangle G_1G_2G_3}=\dfrac19S_{ABCD}=\dfrac19\times2022=\dfrac{674}3$。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓（原书 ans 写作 `674/3 ##224 2/3` —— **两者是同一个数**：$\frac{674}3=224\frac23$）。" "\n"
        r"原书详解用同一建系法算出 $S_{\triangle G_1G_2G_3}=\frac1{18}\lvert bc+de-ad\rvert$ 与 $S_{ABCD}=\frac12\lvert bc+de-ad\rvert$，故比值为 $\frac19$ ✓✓✓" "\n"
        r"**独立验算（完全独立）**：" "\n"
        r"① **重心坐标**：三角形三顶点坐标取平均。" "\n"
        r"$G_1$（$\triangle ABE$：$A(0,0)$、$B(a,b)$、$E(x_0,0)$）$=\left(\frac{0+a+x_0}3,\frac{0+b+0}3\right)=\left(\frac{a+x_0}3,\frac b3\right)$ ✓✓✓" "\n"
        r"$G_2$（$\triangle BCE$）$=\left(\frac{a+c+x_0}3,\frac{b+d+0}3\right)$ ✓✓✓" "\n"
        r"$G_3$（$\triangle CDE$：$C(c,d)$、$D(e,0)$、$E(x_0,0)$）$=\left(\frac{c+e+x_0}3,\frac{d+0+0}3\right)$ ✓✓✓" "\n"
        r"② **$\vec{G_1G_2}$**：$G_2-G_1=\left(\frac{a+c+x_0-a-x_0}3,\frac{b+d-b}3\right)=\left(\frac c3,\frac d3\right)$ ✓✓✓" "\n"
        r"**$\vec{G_3G_2}$**：$G_2-G_3=\left(\frac{a+c+x_0-c-e-x_0}3,\frac{b+d-d}3\right)=\left(\frac{a-e}3,\frac b3\right)$ ✓✓✓" "\n"
        r"③ **$x_0$ 完全消去** ✓✓✓ —— **这正说明 $E$ 的位置不影响结果，与题目「$E$ 为 $AD$ 边上一点（任意）」吻合**" "\n"
        r"④ **叉积公式**：$S=\frac12\lvert u_xv_y-u_yv_x\rvert$。" "\n"
        r"$u_xv_y-u_yv_x=\frac c3\cdot\frac b3-\frac d3\cdot\frac{a-e}3=\frac{bc-d(a-e)}9$ ✓✓✓" "\n"
        r"⟹ $S_{\triangle G_1G_2G_3}=\frac12\cdot\frac{\lvert bc-d(a-e)\rvert}9=\frac{\lvert bc+de-ad\rvert}{18}$ ✓✓✓" "\n"
        r"（**用叉积比用「模平方减点积平方」简洁得多**，两种方式我都算过，结果一致）" "\n"
        r"⑤ **四边形面积**：$ABCD$ 用对角线 $\vec{AC}=(c,d)$、$\vec{DB}=(a-e,b)$。" "\n"
        r"$S=\frac12\lvert c\cdot b-d\cdot(a-e)\rvert=\frac12\lvert bc+de-ad\rvert$ ✓✓✓" "\n"
        r"⑥ **比值**：$\frac{1/18}{1/2}=\frac1{18}\cdot2=\frac19$ ✓✓✓" "\n"
        r"⑦ **$\frac{2022}9$**：$2022\div9=224.666\ldots$，$\frac{674}3=224.666\ldots$ ✓✓✓" "\n"
        r"（$2022=3\times674$，$674=2\times337$，$\frac{2022}9=\frac{674}3$ ✓✓✓）" "\n"
        r"⑧ **具体数值检验**：取 $A(0,0)$、$D(6,0)$（$e=6$）、$E(3,0)$（$x_0=3$）、$B(1,4)$（$a=1,b=4$）、$C(5,4)$（$c=5,d=4$）。" "\n"
        r"四边形 $ABCD$ 是梯形（上底 $BC=4$、下底 $AD=6$、高 $4$），面积 $=\frac{(4+6)\cdot4}2=20$。" "\n"
        r"公式：$\frac12\lvert bc+de-ad\rvert=\frac12\lvert 4\cdot5+0\cdot6-1\cdot4\rvert=\frac12\lvert20-4\rvert=8$？" "\n"
        r"**等等，重算**：$b=4$、$c=5$、$d=4$、$e=6$、$a=1$。" "\n"
        r"$bc=20$、$de=4\cdot6=24$、$ad=1\cdot4=4$ ⟹ $bc+de-ad=20+24-4=40$ ⟹ $S=\frac12\cdot40=20$ ✓✓✓ **与梯形面积吻合**" "\n"
        r"（**第一次漏了 $de$ 项**）" "\n"
        r"重心：$G_1=\left(\frac{1+3}3,\frac43\right)=\left(\frac43,\frac43\right)$、$G_2=\left(\frac{1+5+3}3,\frac{4+4}3\right)=\left(3,\frac83\right)$、$G_3=\left(\frac{5+6+3}3,\frac43\right)=\left(\frac{14}3,\frac43\right)$。" "\n"
        r"$\vec{G_1G_2}=\left(\frac53,\frac43\right)$、$\vec{G_3G_2}=\left(3-\frac{14}3,\frac83-\frac43\right)=\left(-\frac53,\frac43\right)$。" "\n"
        r"叉积 $=\frac53\cdot\frac43-\frac43\cdot\left(-\frac53\right)=\frac{20}9+\frac{20}9=\frac{40}9$ ⟹ $S=\frac12\cdot\frac{40}9=\frac{20}9$ ✓✓✓" "\n"
        r"$\frac19 S_{ABCD}=\frac{20}9$ ✓✓✓ **完全吻合**" "\n"
        r"**答案 $\frac{674}3$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（重心坐标 + 叉积算面积）**：" "\n"
        r"① ⭐⭐ **重心坐标 = 三顶点坐标的算术平均**：" "\n"
        r"**这是把「几何条件」翻译成「代数计算」的标准入口** ✓✓✓；" "\n"
        r"② ⭐⭐ **建系时把多边形的一边放在 $x$ 轴上**（本题 $A$ 为原点、$AD$ 为 $x$ 轴）⟹ **该边上的点纵坐标为 $0$，计算量骤减** ✓✓✓；" "\n"
        r"③ ⭐⭐ **$E$ 的坐标 $x_0$ 在差分中完全消去** ⟹ **结果与 $E$ 的位置无关** —— 与题设「$E$ 为 $AD$ 边上一点」吻合，" "\n"
        r"**这种「参数自动消失」是做法正确的强信号** ✓✓✓；" "\n"
        r"④ ⭐⭐ **算三角形面积用叉积 $S=\frac12\lvert u_xv_y-u_yv_x\rvert$，比「模平方减点积平方再开根」简洁**：" "\n"
        r"**后者需展开并认出完全平方，容易出错** ✓✓✓；" "\n"
        r"⑤ ⭐⭐ **四边形面积 = $\frac12\lvert$ 对角线向量的叉积 $\rvert$**：" "\n"
        r"**适用于任意凸四边形** ✓✓✓；" "\n"
        r"⑥ ⚠ **注意符号：$bc-d(a-e)=bc+de-ad$** —— " "\n"
        r"**我第一次漏掉 $de$ 项导致数值检验不吻合** ✓✓✓；" "\n"
        r"⑦ ⭐ **最强验证：取具体坐标，用初等方法（梯形面积公式）与公式对照** —— " "\n"
        r"本题取梯形时两边都是 $20$ ✓✓✓；" "\n"
        r"⑧ ⭐ **结论可推广**：" "\n"
        r"**三个重心构成的三角形面积 = 原四边形面积的 $\frac19$** —— 记住这个比例可秒杀同类题 ✓✓✓"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-209'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-209-V3',
}

T183_E1 = {
    'type': '填空',
    'stem_text': (
        r"如图，已知 $\triangle ABC$ 为边长为 $2$ 的等边三角形，动点 $P$ 在以 $BC$ 为直径的半圆上，"
        r"若 $\vec{AP}=\lambda\vec{AB}+\mu\vec{AC}$，则 $2\lambda+\mu$ 的最小值为 ____．"
    ),
    'opts': [],
    'answer': r"$1$",
    'analysis': (
        r"建系得 $A(0,\sqrt3)$、$B(-1,0)$、$C(1,0)$，设 $P(\cos\theta,\sin\theta)$ 且 $\theta\in[\pi,2\pi]$。"
        r"由 $\vec{AP}=\lambda\vec{AB}+\mu\vec{AC}$ 解出 $\lambda,\mu$，得 $2\lambda+\mu=\frac32-\sin(\theta+\frac\pi6)$，"
        r"$\theta+\frac\pi6\in[\frac{7\pi}6,\frac{13\pi}6]$，$\sin$ 最大值为 $\frac12$，故最小值为 $1$。"
    ),
    'solution': (
        r"取 $BC$ 中点 $O$，以 $O$ 为原点、$OC$、$OA$ 方向为 $x$ 轴、$y$ 轴正方向建系。" "\n"
        r"$\because\triangle ABC$ 边长为 $2$，$\therefore OA=2\sin60^\circ=\sqrt3$、$OB=OC=1$。" "\n"
        r"$A(0,\sqrt3)$、$B(-1,0)$、$C(1,0)$。" "\n"
        r"以 $BC$ 为直径的半圆（与 $A$ 异侧）方程为 $x^2+y^2=1$（$y\le0$），设 $P(\cos\theta,\sin\theta)$，则 $\theta\in[\pi,2\pi]$。" "\n"
        r"$\vec{AP}=(\cos\theta,\sin\theta-\sqrt3)$、$\vec{AB}=(-1,-\sqrt3)$、$\vec{AC}=(1,-\sqrt3)$。" "\n"
        r"由 $\vec{AP}=\lambda\vec{AB}+\mu\vec{AC}$ 得" "\n"
        r"$\begin{cases}\cos\theta=-\lambda+\mu\\ \sin\theta-\sqrt3=-\sqrt3(\lambda+\mu)\end{cases}$" "\n"
        r"由第二式：$\lambda+\mu=1-\dfrac{\sin\theta}{\sqrt3}$；由第一式：$\mu-\lambda=\cos\theta$。" "\n"
        r"$\therefore\lambda=\dfrac{1-\frac{\sin\theta}{\sqrt3}-\cos\theta}2$，$\mu=\dfrac{1-\frac{\sin\theta}{\sqrt3}+\cos\theta}2$。" "\n"
        r"$2\lambda+\mu=\left(1-\dfrac{\sin\theta}{\sqrt3}-\cos\theta\right)+\dfrac{1-\frac{\sin\theta}{\sqrt3}+\cos\theta}2$" "\n"
        r"$=\dfrac32-\dfrac{3\sin\theta}{2\sqrt3}-\dfrac{\cos\theta}2=\dfrac32-\dfrac{\sqrt3}2\sin\theta-\dfrac12\cos\theta$" "\n"
        r"$=\dfrac32-\sin\left(\theta+\dfrac\pi6\right)$。" "\n"
        r"$\because\theta\in[\pi,2\pi]$，$\therefore\theta+\dfrac\pi6\in\left[\dfrac{7\pi}6,\dfrac{13\pi}6\right]$。" "\n"
        r"在该区间上，$\sin\left(\theta+\dfrac\pi6\right)$ 的最大值为 $\dfrac12$（在 $\theta+\frac\pi6=\frac{13\pi}6$ 即 $\theta=2\pi$ 处取到）。" "\n"
        r"$\therefore 2\lambda+\mu$ 的最小值为 $\dfrac32-\dfrac12=1$。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书详解：「取 $BC$ 中点 $O$，以 $O$ 为原点，$OC$、$OA$ 方向为 $x$ 轴、$y$ 轴正方向建系。" "\n"
        r"由题意得：$OA=2\sin60^\circ=\sqrt3$，所以 $A(0,\sqrt3)$、$B(-1,0)$、$C(1,0)$，以 $BC$ 为直径的半圆方程为 $x^2+y^2=1$（$y\le0$），设 $P(\cos\theta,\sin\theta)$，因为 $\sin\theta\le0$，所以 $\theta\in[\pi,2\pi]$，" "\n"
        r"则 $\vec{AP}=(\cos\theta,\sin\theta-\sqrt3)$，$\vec{AB}=(-1,-\sqrt3)$，$\vec{AC}=(1,-\sqrt3)$，因为 $\vec{AP}=\lambda\vec{AB}+\mu\vec{AC}$，所以 $\cos\theta=-\lambda+\mu$，$\sin\theta-\sqrt3=-\sqrt3\lambda-\sqrt3\mu$，" "\n"
        r"整理可得 $\mu=\frac12+\frac12\cos\theta-\frac{\sqrt3}6\sin\theta$，$\lambda=\frac12-\frac{\sqrt3}6\sin\theta-\frac12\cos\theta$，所以 $2\lambda+\mu=\frac32-\sin(\theta+\frac\pi6)$，" "\n"
        r"因为 $\theta\in[\pi,2\pi]$，所以 $\theta+\frac\pi6\in[\frac{7\pi}6,\frac{13\pi}6]$，当 $\theta+\frac\pi6=\frac{13\pi}6$ 时，$\sin(\theta+\frac\pi6)$ 取最大值 $\frac12$，所以 $2\lambda+\mu$ 的最小值为 $\frac32-\frac12=1$。故答案为：$1$」" "\n"
        r"—— **建系坐标、$\lambda$ 与 $\mu$ 的表达式、$2\lambda+\mu=\frac32-\sin(\theta+\frac\pi6)$、最小值 $1$ 全部一致** ✓✓✓" "\n"
        r"**独立验算（完全独立）**：" "\n"
        r"① **坐标**：等边三角形边长 $2$，高 $=2\cdot\frac{\sqrt3}2=\sqrt3$ ✓；$O$ 是 $BC$ 中点 ⟹ $OB=OC=1$ ✓✓✓" "\n"
        r"② **半圆**：以 $BC$ 为直径 ⟹ 半径 $1$、圆心 $O$ ⟹ $x^2+y^2=1$；与 $A$ 异侧 ⟹ $y\le0$ ⟹ $\theta\in[\pi,2\pi]$ ✓✓✓" "\n"
        r"③ **$\lambda+\mu$**：$-\sqrt3(\lambda+\mu)=\sin\theta-\sqrt3$ ⟹ $\lambda+\mu=\frac{\sqrt3-\sin\theta}{\sqrt3}=1-\frac{\sin\theta}{\sqrt3}$ ✓✓✓" "\n"
        r"④ **$\mu-\lambda=\cos\theta$** ✓✓✓" "\n"
        r"⟹ $\lambda=\frac{(\lambda+\mu)-(\mu-\lambda)}2=\frac{1-\frac{\sin\theta}{\sqrt3}-\cos\theta}2$ ✓✓✓" "\n"
        r"$\mu=\frac{1-\frac{\sin\theta}{\sqrt3}+\cos\theta}2$ ✓✓✓" "\n"
        r"⑤ **与原书对照**：原书 $\mu=\frac12+\frac12\cos\theta-\frac{\sqrt3}6\sin\theta$。" "\n"
        r"我的 $\mu=\frac12-\frac{\sin\theta}{2\sqrt3}+\frac{\cos\theta}2$，而 $\frac{\sin\theta}{2\sqrt3}=\frac{\sqrt3\sin\theta}6$ ✓✓✓ **完全一致**" "\n"
        r"⑥ **$2\lambda+\mu$**：" "\n"
        r"$2\lambda=1-\frac{\sin\theta}{\sqrt3}-\cos\theta$；$\mu=\frac12-\frac{\sin\theta}{2\sqrt3}+\frac{\cos\theta}2$。" "\n"
        r"和 $=\frac32-\frac{\sin\theta}{\sqrt3}-\frac{\sin\theta}{2\sqrt3}-\cos\theta+\frac{\cos\theta}2=\frac32-\frac{3\sin\theta}{2\sqrt3}-\frac{\cos\theta}2$" "\n"
        r"$=\frac32-\frac{\sqrt3\sin\theta}{2}-\frac{\cos\theta}2$ ✓✓✓（因 $\frac{3}{2\sqrt3}=\frac{\sqrt3}{2}$）" "\n"
        r"⑦ **辅助角**：$\frac{\sqrt3}2\sin\theta+\frac12\cos\theta=\sin(\theta+\frac\pi6)$？" "\n"
        r"$\sin(\theta+\frac\pi6)=\sin\theta\cos\frac\pi6+\cos\theta\sin\frac\pi6=\frac{\sqrt3}2\sin\theta+\frac12\cos\theta$ ✓✓✓" "\n"
        r"⟹ $2\lambda+\mu=\frac32-\sin(\theta+\frac\pi6)$ ✓✓✓" "\n"
        r"⑧ **区间**：$\theta\in[\pi,2\pi]$ ⟹ $\theta+\frac\pi6\in[\frac{7\pi}6,\frac{13\pi}6]$。" "\n"
        r"$\frac{7\pi}6=210^\circ$、$\frac{13\pi}6=390^\circ=30^\circ$。" "\n"
        r"在 $[210^\circ,390^\circ]$ 上 $\sin$ 的最大值：$390^\circ$ 处 $\sin=\frac12$；$\sin=1$ 需 $270^\circ$… **$270^\circ\in[210^\circ,390^\circ]$！**" "\n"
        r"**等等** —— $270^\circ$ 在区间内，$\sin270^\circ=-1$（**是最小值不是最大值**）✓。" "\n"
        r"$\sin$ 在 $[210^\circ,390^\circ]$ 上：从 $210^\circ$（$-\frac12$）降到 $270^\circ$（$-1$），再升到 $390^\circ$（$\frac12$）。" "\n"
        r"**最大值 $=\frac12$（在 $390^\circ$ 即 $\theta=2\pi$ 处）** ✓✓✓" "\n"
        r"（**$\theta=2\pi$ 对应 $P(1,0)=C$，是半圆的端点，允许**）" "\n"
        r"⑨ **最小值** $=\frac32-\frac12=1$ ✓✓✓" "\n"
        r"⑩ **逐点检验**：" "\n"
        r"$\theta=2\pi$（$P=C$）：$\lambda+\mu=1-0=1$、$\mu-\lambda=1$ ⟹ $\mu=1$、$\lambda=0$。" "\n"
        r"$2\lambda+\mu=0+1=1$ ✓✓✓（**且此时 $\vec{AP}=\vec{AC}$ 即 $\lambda=0,\mu=1$，符合直观**）" "\n"
        r"$\theta=\frac{3\pi}2$（$P=(0,-1)$）：$\lambda+\mu=1-\frac{-1}{\sqrt3}=1+\frac{\sqrt3}3\approx1.577$、$\mu-\lambda=0$ ⟹ $\mu=\lambda\approx0.789$。" "\n"
        r"$2\lambda+\mu\approx2.366$。公式：$\frac32-\sin(\frac{3\pi}2+\frac\pi6)=\frac32-\sin(\frac{5\pi}3)=1.5-(-0.866)=2.366$ ✓✓✓" "\n"
        r"$\theta=\pi$（$P=B$）：$\lambda+\mu=1$、$\mu-\lambda=-1$ ⟹ $\mu=0$、$\lambda=1$。$2\lambda+\mu=2$ ✓✓✓" "\n"
        r"（**此时 $\vec{AP}=\vec{AB}$ 即 $\lambda=1,\mu=0$，符合直观**）" "\n"
        r"**答案 $1$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（向量系数 ⟹ 建系解方程组）**：" "\n"
        r"① ⭐⭐ **识别特征：$\vec{AP}=\lambda\vec{AB}+\mu\vec{AC}$ ⟹ 把三个向量写成坐标，得两个一次方程**：" "\n"
        r"**「和」与「差」分开解最简洁**：本题 $\lambda+\mu$ 来自 $y$ 分量、$\mu-\lambda$ 来自 $x$ 分量 ✓✓✓；" "\n"
        r"② ⭐⭐ **建系时把对称性用足**：" "\n"
        r"**等边三角形 ⟹ 取底边中点为原点、底边为 $x$ 轴 ⟹ 两底点坐标是 $(\pm1,0)$、顶点 $(0,\sqrt3)$** ✓✓✓；" "\n"
        r"③ ⭐⭐ **半圆的参数化**：$P(\cos\theta,\sin\theta)$，**由 $y\le0$ 定出 $\theta\in[\pi,2\pi]$** ✓✓✓；" "\n"
        r"（**注意：是「与 $A$ 异侧的半圆」还是「同侧」决定 $y$ 的符号**）" "\n"
        r"④ ⭐⭐ **辅助角合并后，要在 $\theta$ 的真实区间上求最值**：" "\n"
        r"**务必检查 $\sin=1$（或 $-1$）对应的 $\theta$ 是否在区间内** —— 本题 $\sin=1$ 需 $\theta+\frac\pi6=\frac\pi2$ 即 $\theta=\frac\pi3\notin[\pi,2\pi]$ ✓✓✓，" "\n"
        r"**故最大值只能在端点取得**；" "\n"
        r"⑤ ⭐⭐ **端点检验法（最可靠）**：" "\n"
        r"**把 $\theta=\pi$（$P=B$）、$\theta=2\pi$（$P=C$）代入，直接由几何意义验证 $\lambda,\mu$** —— " "\n"
        r"本题 $P=B$ 时 $(\lambda,\mu)=(1,0)$、$P=C$ 时 $(\lambda,\mu)=(0,1)$ ✓✓✓ **与几何直观完全吻合**；" "\n"
        r"⑥ ⚠ **$2\lambda+\mu$ 是「加权的系数和」**：" "\n"
        r"**不要用「系数和为 $1$」（那只在 $P$ 在直线 $BC$ 上时成立）** —— 本题 $P$ 在半圆上，$\lambda+\mu=1-\frac{\sin\theta}{\sqrt3}\ne1$ ✓✓✓"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-183'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-183-E1',
}

T183_V2 = {
    'type': '填空',
    'stem_text': (
        r"记 $d(A,B)=\lvert x_1-x_2\rvert+2\lvert y_1-y_2\rvert$，其中 $A(x_1,y_1)$、$B(x_2,y_2)$。已知 $A,B$ 是椭圆 $\dfrac{x^2}4+y^2=1$ 上的任意两点，"
        r"$C$ 是椭圆右顶点，则 $d(A,C)+d(B,C)$ 的最大值是 ____．"
    ),
    'opts': [],
    'answer': r"$4+4\sqrt2$",
    'analysis': (
        r"设 $A(2\cos\alpha,\sin\alpha)$，则 $d(A,C)=2(1-\cos\alpha)+2\lvert\sin\alpha\rvert$。"
        r"分 $0\le\alpha<\pi$ 与 $\pi\le\alpha<2\pi$ 两段去掉绝对值，各得最大值 $2+2\sqrt2$，故两点之和最大为 $4+4\sqrt2$。"
    ),
    'solution': (
        r"椭圆 $\dfrac{x^2}4+y^2=1$ 的右顶点为 $C(2,0)$，设 $A(2\cos\alpha,\sin\alpha)$，其中 $0\le\alpha<2\pi$。" "\n"
        r"$d(A,C)=\lvert2\cos\alpha-2\rvert+2\lvert\sin\alpha\rvert$。" "\n"
        r"$\because\cos\alpha\le1$，$\therefore\lvert2\cos\alpha-2\rvert=2-2\cos\alpha=2(1-\cos\alpha)$。" "\n"
        r"$\therefore d(A,C)=2(1-\cos\alpha)+2\lvert\sin\alpha\rvert$。" "\n"
        r"**① 当 $0\le\alpha<\pi$ 时**，$\sin\alpha\ge0$：" "\n"
        r"$d(A,C)=2-2\cos\alpha+2\sin\alpha=2\sqrt2\sin\left(\alpha-\dfrac\pi4\right)+2$。" "\n"
        r"（$-\frac{\sqrt2}2\cdot(-2)$… 检验：$2\sqrt2\sin(\alpha-\frac\pi4)=2\sqrt2(\sin\alpha\cos\frac\pi4-\cos\alpha\sin\frac\pi4)=2\sin\alpha-2\cos\alpha$ ✓）" "\n"
        r"$\because-\dfrac\pi4\le\alpha-\dfrac\pi4<\dfrac{3\pi}4$，当 $\alpha-\dfrac\pi4=\dfrac\pi2$（即 $\alpha=\dfrac{3\pi}4$）时取最大值 $2\sqrt2+2$。" "\n"
        r"**② 当 $\pi\le\alpha<2\pi$ 时**，$\sin\alpha\le0$：" "\n"
        r"$d(A,C)=2-2\cos\alpha-2\sin\alpha=2-2(\cos\alpha+\sin\alpha)=2-2\sqrt2\sin\left(\alpha+\dfrac\pi4\right)$。" "\n"
        r"$\because\dfrac{5\pi}4\le\alpha+\dfrac\pi4<\dfrac{9\pi}4$，当 $\alpha+\dfrac\pi4=\dfrac{3\pi}2$（即 $\alpha=\dfrac{5\pi}4$）时，$\sin=-1$，$d$ 取最大值 $2+2\sqrt2$。" "\n"
        r"综上，$d(A,C)$ 的最大值为 $2+2\sqrt2$。同理 $d(B,C)$ 的最大值也为 $2+2\sqrt2$。" "\n"
        r"$\therefore d(A,C)+d(B,C)$ 的最大值是 $4+4\sqrt2$。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书详解：「设点 $A(2\cos\alpha,\sin\alpha)$，其中 $0\le\alpha<2\pi$，易知点 $C(2,0)$，则 $d(A,C)=\lvert2\cos\alpha-2\rvert+2\lvert\sin\alpha\rvert=2(1-\cos\alpha)+2\lvert\sin\alpha\rvert$。" "\n"
        r"① 当 $0\le\alpha<\pi$ 时，$d(A,C)=2(1-\cos\alpha)+2\sin\alpha=2\sqrt2\sin(\alpha-\frac\pi4)+2$，$\because0\le\alpha<\pi$，则 $-\frac\pi4\le\alpha-\frac\pi4<\frac{3\pi}4$，当 $\alpha-\frac\pi4=\frac\pi2$ 时，$d(A,C)$ 取最大值 $2\sqrt2+2$；" "\n"
        r"② 当 $\pi\le\alpha<2\pi$ 时，$d(A,C)=2(1-\cos\alpha)-2\sin\alpha=2-2\sqrt2\sin(\alpha+\frac\pi4)$，$\because\pi\le\alpha<2\pi$，则 $\frac{5\pi}4\le\alpha+\frac\pi4<\frac{9\pi}4$，当 $\alpha+\frac\pi4=\frac{3\pi}2$ 时，$d(A,C)$ 取最大值 $2\sqrt2+2$。" "\n"
        r"综上所述，$d(A,C)$ 的最大值 $2\sqrt2+2$，同理可知，$d(B,C)$ 的最大值也为 $2\sqrt2+2$。因此，$d(A,C)+d(B,C)$ 的最大值是 $4+4\sqrt2$。故答案为：$4+4\sqrt2$」" "\n"
        r"—— **参数化、$2(1-\cos\alpha)+2\lvert\sin\alpha\rvert$、两段去绝对值、各段最大 $2+2\sqrt2$、答案 $4+4\sqrt2$ 全部一致** ✓✓✓" "\n"
        r"（**答案根号丢失**：`4 + 4 2` 实为 $4+4\sqrt2$）" "\n"
        r"**独立验算（完全独立）**：" "\n"
        r"① **参数化**：椭圆 $\frac{x^2}4+y^2=1$ ⟹ $x=2\cos\alpha$、$y=\sin\alpha$ ✓✓✓" "\n"
        r"② **$\lvert2\cos\alpha-2\rvert=2(1-\cos\alpha)$**：因 $\cos\alpha\le1$ ✓✓✓" "\n"
        r"③ **段①（$0\le\alpha<\pi$，$\sin\alpha\ge0$）**：" "\n"
        r"$2-2\cos\alpha+2\sin\alpha=2+2(\sin\alpha-\cos\alpha)=2+2\sqrt2\sin(\alpha-\frac\pi4)$ ✓✓✓" "\n"
        r"（$\sin\alpha-\cos\alpha=\sqrt2\sin(\alpha-\frac\pi4)$ ✓）" "\n"
        r"最大值：需 $\sin(\alpha-\frac\pi4)=1$ ⟹ $\alpha-\frac\pi4=\frac\pi2$ ⟹ $\alpha=\frac{3\pi}4\in[0,\pi)$ ✓✓✓" "\n"
        r"值 $=2+2\sqrt2\approx4.828$ ✓✓✓" "\n"
        r"④ **段②（$\pi\le\alpha<2\pi$，$\sin\alpha\le0$）**：" "\n"
        r"$2-2\cos\alpha-2\sin\alpha=2-2(\cos\alpha+\sin\alpha)=2-2\sqrt2\sin(\alpha+\frac\pi4)$ ✓✓✓" "\n"
        r"（$\cos\alpha+\sin\alpha=\sqrt2\sin(\alpha+\frac\pi4)$ ✓）" "\n"
        r"最大值：需 $\sin(\alpha+\frac\pi4)$ 最小 $=-1$ ⟹ $\alpha+\frac\pi4=\frac{3\pi}2$ ⟹ $\alpha=\frac{5\pi}4\in[\pi,2\pi)$ ✓✓✓" "\n"
        r"值 $=2+2\sqrt2$ ✓✓✓" "\n"
        r"⑤ **数值检验**：" "\n"
        r"$\alpha=\frac{3\pi}4$：$A=(2\cos135^\circ,\sin135^\circ)=(-1.414,0.707)$。" "\n"
        r"$d(A,C)=\lvert-1.414-2\rvert+2\cdot0.707=3.414+1.414=4.828=2+2\sqrt2$ ✓✓✓" "\n"
        r"$\alpha=\frac{5\pi}4$：$A=(-1.414,-0.707)$。" "\n"
        r"$d(A,C)=3.414+1.414=4.828$ ✓✓✓ **两段对称，值相同**" "\n"
        r"⑥ **$A$、$B$ 是「任意两点」**：" "\n"
        r"**$d(A,C)$ 与 $d(B,C)$ 互相独立**（各自只依赖自己的位置）⟹ **可同时取到最大值** ✓✓✓" "\n"
        r"（**这是关键**：若两点的取值互相制约，就不能简单相加）" "\n"
        r"⑦ **$4+4\sqrt2\approx9.657$** ✓✓✓" "\n"
        r"**答案 $4+4\sqrt2$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（新定义「距离」的极值）**：" "\n"
        r"① ⭐⭐ **新定义 $d$ 含绝对值 ⟹ 先判断每个绝对值内式子的符号，再分段**：" "\n"
        r"**本题 $\lvert2\cos\alpha-2\rvert$ 因 $\cos\alpha\le1$ 而直接去绝对值（无需分段）；$\lvert\sin\alpha\rvert$ 需按 $\alpha$ 分段** ✓✓✓；" "\n"
        r"② ⭐⭐ **椭圆上的点用参数 $(a\cos\alpha,b\sin\alpha)$ 表示** ⟹ 新定义式变成**一个变量 $\alpha$ 的函数** ✓✓✓；" "\n"
        r"③ ⭐⭐ **辅助角合并的标准形式**：" "\n"
        r"$\sin\alpha\pm\cos\alpha=\sqrt2\sin(\alpha\pm\frac\pi4)$ ✓✓✓ —— **记住这个可省大量时间**；" "\n"
        r"④ ⭐⭐ **分段后要检验极值点是否落在该段内**：" "\n"
        r"段①的 $\alpha=\frac{3\pi}4\in[0,\pi)$ ✓、段②的 $\alpha=\frac{5\pi}4\in[\pi,2\pi)$ ✓ ✓✓✓ —— **两段都取得到**；" "\n"
        r"⑤ ⭐⭐ **「两个独立点」的极值可分别取到后相加**：" "\n"
        r"**前提是 $A$、$B$ 的取值互不制约** —— 本题 $A,B$ 是椭圆上任意两点（可重合）✓✓✓；" "\n"
        r"⑥ ⚠ **注意新定义中 $y$ 方向的权重是 $2$**：" "\n"
        r"$d=\lvert\Delta x\rvert+2\lvert\Delta y\rvert$ —— **不是标准的曼哈顿距离**，权重 $2$ 来自题目定义 ✓✓✓；" "\n"
        r"⑦ ⭐ **验证：取具体 $\alpha$ 算 $d$ 与公式对照** —— " "\n"
        r"本题 $\alpha=\frac{3\pi}4$、$\frac{5\pi}4$ 都给 $4.828$ ✓✓✓"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-183'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-183-V2',
}

T183_V3 = {
    'type': '填空',
    'stem_text': (
        r"设圆 $O:x^2+y^2=1$ 上两点 $A(x_1,y_1)$、$B(x_2,y_2)$ 满足 $\vec{OA}\cdot\vec{OB}=-\dfrac12$，"
        r"则 $\lvert x_1-2y_1\rvert+\lvert x_2-2y_2\rvert$ 的取值范围是 ____．"
    ),
    'opts': [],
    'answer': r"$\left[\dfrac{\sqrt{15}}2,\sqrt{15}\right]$",
    'analysis': (
        r"由 $\vec{OA}\cdot\vec{OB}=-\frac12$ 得 $\angle AOB=120^\circ$。$\frac{\lvert x-2y\rvert}{\sqrt5}$ 是点到直线 $x-2y=0$ 的距离，"
        r"换系后 $h=\lvert\sin\theta\rvert+\lvert\sin(\theta+120^\circ)\rvert\in[\frac{\sqrt3}2,\sqrt3]$，乘 $\sqrt5$ 得 $[\frac{\sqrt{15}}2,\sqrt{15}]$。"
    ),
    'solution': (
        r"由 $\vec{OA}\cdot\vec{OB}=\lvert\vec{OA}\rvert\lvert\vec{OB}\rvert\cos\angle AOB=\cos\angle AOB=-\dfrac12$，得 $\angle AOB=120^\circ$。" "\n"
        r"注意到 $\dfrac{\lvert x-2y\rvert}{\sqrt5}$ 正是点 $(x,y)$ 到直线 $x-2y=0$ 的距离。" "\n"
        r"记 $h=\dfrac{\lvert x_1-2y_1\rvert}{\sqrt5}+\dfrac{\lvert x_2-2y_2\rvert}{\sqrt5}$，即两点到该直线的距离之和。" "\n"
        r"取直线 $x-2y=0$ 为新坐标系的 $x$ 轴重新建系（旋转不改变角度关系），则在新系下两点仍满足夹角 $120^\circ$，且 $h$ 是两点到新 $x$ 轴的距离之和。" "\n"
        r"设新系下 $A(\cos\theta,\sin\theta)$、$B\left(\cos(\theta+120^\circ),\sin(\theta+120^\circ)\right)$，则" "\n"
        r"$h=\lvert\sin\theta\rvert+\left\lvert\sin(\theta+120^\circ)\right\rvert$。" "\n"
        r"由对称性，不妨设 $B$ 在 $x$ 轴上或上方，即 $-120^\circ\le\theta\le60^\circ$。" "\n"
        r"**当 $0^\circ\le\theta\le60^\circ$ 时**（此时 $\sin\theta\ge0$、$\sin(\theta+120^\circ)\ge0$）：" "\n"
        r"$h=\sin\theta+\sin(\theta+120^\circ)=2\sin(\theta+60^\circ)\cos60^\circ=\sin(\theta+60^\circ)$。" "\n"
        r"$\because\theta+60^\circ\in[60^\circ,120^\circ]$，$\therefore h\in\left[\dfrac{\sqrt3}2,1\right]$。" "\n"
        r"**当 $-120^\circ\le\theta<0^\circ$ 时**（此时 $\sin\theta\le0$、$\sin(\theta+120^\circ)\ge0$）：" "\n"
        r"$h=-\sin\theta+\sin(\theta+120^\circ)=2\cos(\theta+60^\circ)\sin60^\circ=\sqrt3\cos(\theta+60^\circ)$。" "\n"
        r"$\because\theta+60^\circ\in[-60^\circ,60^\circ)$，$\therefore\cos(\theta+60^\circ)\in\left(\dfrac12,1\right]$，$h\in\left(\dfrac{\sqrt3}2,\sqrt3\right]$。" "\n"
        r"综上，$h\in\left[\dfrac{\sqrt3}2,\sqrt3\right]$。" "\n"
        r"$\therefore\lvert x_1-2y_1\rvert+\lvert x_2-2y_2\rvert=\sqrt5\,h\in\left[\dfrac{\sqrt{15}}2,\sqrt{15}\right]$。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书详解：「由 $\vec{OA}\cdot\vec{OB}=-\frac12$，得 $\angle AOB=120^\circ$。设 $h=\frac{\lvert x_1-2y_1\rvert}{\sqrt5}+\frac{\lvert x_2-2y_2\rvert}{\sqrt5}$ 表示两点 $A$、$B$ 分别到直线 $x-2y=0$ 的距离之和。" "\n"
        r"取直线 $x-2y=0$ 为 $x$ 轴重新建立直角坐标系后，则 $h$ 表示两点 $A$、$B$ 分别到 $x$ 轴的距离之和。在新的直角坐标系下，设 $A(\cos\theta,\sin\theta)$、$B(\cos(\theta+120^\circ),\sin(\theta+120^\circ))$。" "\n"
        r"则有 $h=\lvert\sin\theta\rvert+\lvert\sin(\theta+120^\circ)\rvert$。由对称性，不妨设点 $B$ 在 $x$ 轴上或上方，即 $-120^\circ\le\theta\le60^\circ$。" "\n"
        r"所以 $h=\begin{cases}\sin\theta+\sin(\theta+120^\circ),&0^\circ\le\theta\le60^\circ\\-\sin\theta+\sin(\theta+120^\circ),&-120^\circ\le\theta<0^\circ\end{cases}$，" "\n"
        r"$0^\circ\le\theta\le60^\circ$ 时，$h=\frac12\sin\theta+\frac{\sqrt3}2\cos\theta=\sin(\theta+60^\circ)$，得 $\theta+60^\circ\in[60^\circ,120^\circ]$，则 $h\in[\frac{\sqrt3}2,1]$；" "\n"
        r"当 $-120^\circ\le\theta<0^\circ$ 时，$h=-\frac{\sqrt3}2\sin\theta+\frac{\sqrt3}2\cos\theta$…（原书写作 $-\sqrt3\sin(\theta-30^\circ)$），$\theta-30^\circ\in[-150^\circ,-30^\circ]$，此时 $h\in(\frac{\sqrt3}2,\sqrt3]$。" "\n"
        r"综上得 $\frac{\sqrt3}2\le h\le\sqrt3$，从而得 $\lvert x_1-2y_1\rvert+\lvert x_2-2y_2\rvert=\sqrt5h\in[\frac{\sqrt{15}}2,\sqrt{15}]$」" "\n"
        r"—— **$\angle AOB=120^\circ$、换系、$h=\lvert\sin\theta\rvert+\lvert\sin(\theta+120^\circ)\rvert$、$h\in[\frac{\sqrt3}2,\sqrt3]$、答案 $[\frac{\sqrt{15}}2,\sqrt{15}]$ 全部一致** ✓✓✓" "\n"
        r"（**答案根号在提取中丢失**：`15/2, 15` 实为 $[\frac{\sqrt{15}}2,\sqrt{15}]$）" "\n"
        r"**独立验算（完全独立）**：" "\n"
        r"① **$\angle AOB=120^\circ$**：$\cos\angle AOB=\frac{-\frac12}{1\cdot1}=-\frac12$ ⟹ $120^\circ$ ✓✓✓" "\n"
        r"② **点到直线距离**：$\frac{\lvert x-2y\rvert}{\sqrt{1^2+(-2)^2}}=\frac{\lvert x-2y\rvert}{\sqrt5}$ ✓✓✓" "\n"
        r"③ **旋转不变性**：旋转是正交变换，**保持夹角与距离** ⟹ 换系后仍夹角 $120^\circ$、仍在同一单位圆上 ✓✓✓" "\n"
        r"④ **$h=\lvert\sin\theta\rvert+\lvert\sin(\theta+120^\circ)\rvert$**：新系下 $A(\cos\theta,\sin\theta)$、$B(\cos(\theta+120^\circ),\sin(\theta+120^\circ))$，" "\n"
        r"到 $x$ 轴距离分别是 $\lvert\sin\theta\rvert$、$\lvert\sin(\theta+120^\circ)\rvert$ ✓✓✓" "\n"
        r"⑤ **对称性简化**：$(\theta,\theta+120^\circ)$ 与 $(-\theta-120^\circ,-\theta)$ 关于 $x$ 轴对称，故可限定 $B$ 在上半平面。" "\n"
        r"$B$ 在上半平面 ⟹ $\sin(\theta+120^\circ)\ge0$ ⟹ $\theta+120^\circ\in[0^\circ,180^\circ]$ ⟹ $\theta\in[-120^\circ,60^\circ]$ ✓✓✓" "\n"
        r"⑥ **段①（$0^\circ\le\theta\le60^\circ$）**：$\sin\theta\ge0$、$\sin(\theta+120^\circ)\ge0$。" "\n"
        r"$h=\sin\theta+\sin(\theta+120^\circ)$。和差化积：$\sin X+\sin Y=2\sin\frac{X+Y}2\cos\frac{X-Y}2$。" "\n"
        r"$=2\sin(\theta+60^\circ)\cos(-60^\circ)=2\sin(\theta+60^\circ)\cdot\frac12=\sin(\theta+60^\circ)$ ✓✓✓" "\n"
        r"$\theta+60^\circ\in[60^\circ,120^\circ]$ ⟹ $\sin\in[\frac{\sqrt3}2,1]$ ✓✓✓" "\n"
        r"⑦ **段②（$-120^\circ\le\theta<0^\circ$）**：$\sin\theta\le0$、$\sin(\theta+120^\circ)\ge0$。" "\n"
        r"$h=-\sin\theta+\sin(\theta+120^\circ)$。和差化积：$\sin Y-\sin X=2\cos\frac{X+Y}2\sin\frac{Y-X}2$。" "\n"
        r"$=2\cos(\theta+60^\circ)\sin(60^\circ)=\sqrt3\cos(\theta+60^\circ)$ ✓✓✓" "\n"
        r"$\theta+60^\circ\in[-60^\circ,60^\circ)$ ⟹ $\cos\in(\frac12,1]$ ⟹ $h\in(\frac{\sqrt3}2,\sqrt3]$ ✓✓✓" "\n"
        r"（**原书写作 $-\sqrt3\sin(\theta-30^\circ)$**：$\cos(\theta+60^\circ)=\sin(90^\circ-\theta-60^\circ)=\sin(30^\circ-\theta)=-\sin(\theta-30^\circ)$ ✓✓✓ **一致**）" "\n"
        r"⑧ **合并**：$[\frac{\sqrt3}2,1]\cup(\frac{\sqrt3}2,\sqrt3]=[\frac{\sqrt3}2,\sqrt3]$ ✓✓✓" "\n"
        r"（**左端 $\frac{\sqrt3}2$ 在段①的 $\theta=0^\circ$ 或 $\theta=60^\circ$ 处取到 ⟹ 闭**）" "\n"
        r"⑨ **乘 $\sqrt5$**：$\sqrt5\cdot\frac{\sqrt3}2=\frac{\sqrt{15}}2$；$\sqrt5\cdot\sqrt3=\sqrt{15}$ ✓✓✓" "\n"
        r"⑩ **具体数值检验**：" "\n"
        r"取 $\theta=0^\circ$：$A(1,0)$、$B(\cos120^\circ,\sin120^\circ)=(-0.5,0.866)$（在新系下）。" "\n"
        r"$h=0+0.866=\frac{\sqrt3}2$ ✓✓✓ **正是下界**" "\n"
        r"取 $\theta=-60^\circ$：$A(\cos(-60^\circ),\sin(-60^\circ))=(0.5,-0.866)$、$B(\cos60^\circ,\sin60^\circ)=(0.5,0.866)$。" "\n"
        r"$h=0.866+0.866=1.732=\sqrt3$ ✓✓✓ **正是上界**" "\n"
        r"（此时 $A$、$B$ 关于新 $x$ 轴对称，两点都在距 $x$ 轴最远处）" "\n"
        r"**答案 $[\frac{\sqrt{15}}2,\sqrt{15}]$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（「点到直线的距离和」⟹ 旋转坐标系）**：" "\n"
        r"① ⭐⭐ **识别特征：$\lvert ax+by\rvert$ 出现 ⟹ 除以 $\sqrt{a^2+b^2}$ 就是点到直线 $ax+by=0$ 的距离**：" "\n"
        r"**本题 $\frac{\lvert x-2y\rvert}{\sqrt5}$ 是到 $x-2y=0$ 的距离** ✓✓✓ —— 这是本题的题眼；" "\n"
        r"② ⭐⭐ **旋转坐标系使该直线成为新 $x$ 轴** ⟹ **距离变成 $\lvert y'\rvert=\lvert\sin\theta\rvert$，问题大幅简化** ✓✓✓；" "\n"
        r"（**旋转保持：夹角、距离、圆的形状** —— 所以可以放心旋转）" "\n"
        r"③ ⭐⭐ **圆上两点夹角固定 ⟹ 参数角相差固定值**（本题 $120^\circ$）✓✓✓；" "\n"
        r"④ ⭐⭐ **$\lvert\sin\theta\rvert+\lvert\sin(\theta+\varphi)\rvert$ 的处理：按 $\sin$ 的符号分段，再用和差化积**：" "\n"
        r"$\sin X+\sin Y=2\sin\frac{X+Y}2\cos\frac{X-Y}2$；$\sin Y-\sin X=2\cos\frac{X+Y}2\sin\frac{Y-X}2$ ✓✓✓；" "\n"
        r"⑤ ⭐⭐ **用对称性缩小 $\theta$ 的范围**：" "\n"
        r"**「不妨设 $B$ 在上半平面」把 $\theta$ 从 $[0^\circ,360^\circ)$ 缩到 $[-120^\circ,60^\circ]$** ✓✓✓ —— 这一步省掉一半计算；" "\n"
        r"⑥ ⚠ **分段点由 $\sin\theta=0$ 与 $\sin(\theta+120^\circ)=0$ 决定**：" "\n"
        r"**本题是 $\theta=0^\circ$**（$\theta=-120^\circ$ 与 $60^\circ$ 是区间端点）✓✓✓；" "\n"
        r"⑦ ⭐ **验证：取 $\theta$ 的特殊值算 $h$ 与区间对照** —— " "\n"
        r"本题 $\theta=0^\circ$ 给 $\frac{\sqrt3}2$（下界）、$\theta=-60^\circ$ 给 $\sqrt3$（上界）✓✓✓；" "\n"
        r"⑧ ⭐ **几何意义（最值何时取到）**：" "\n"
        r"**上界：$A$、$B$ 关于新 $x$ 轴对称（一上一下都在最远处）；下界：其中一点在新 $x$ 轴上** ✓✓✓"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-183'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-183-V3',
}

QS = [T223_E1, T223_V1, T223_V3,
      T220_E1, T220_V2, T220_V3,
      T209_E1, T209_V2, T209_V3,
      T183_E1, T183_V2, T183_V3]
