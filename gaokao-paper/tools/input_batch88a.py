# -*- coding: utf-8 -*-
r"""第88批：解三角形综合（12 题）

M-T-219（4）、M-T-221（4）、M-T-222（4）

## ★★ 12 题我全部独立验算（回代 / 端点检验 / 数值对拍）

| 题 | 我的验算 | 答案 |
|---|---|---|
| M-T-219-E1 | $S=\frac{\sqrt3}4(a^2+b^2-c^2)=\frac12ab\sin C$ ⟹ $\tan C=\sqrt3$；$a=2t,b=3t$ ⟹ $c=\sqrt7t$ ⟹ $\sin A=\frac{2t\cdot\frac{\sqrt3}2}{\sqrt7t}$ | **$\frac{\sqrt{21}}7$** |
| M-T-219-V1 | $\cos(B+C)=-\cos A$ ⟹ $\cos A(2bc\sin A-20)=0$ ⟹ $S=5$；$a^2=4S=2bc\sin A$ ⟹ $\frac cb+\frac bc=2\sin A+2\cos A$ | **$2\sqrt2$** |
| M-T-219-V2 | ①⟹$\cos B=-\frac{\sqrt6}3>\cdots$、②⟹$\cos A=\frac12$ ⟹ $A+B>\pi$ 矛盾；①③④：$c=\sqrt6-2$、$S=\sqrt3-\sqrt2$；②③④：$B=\frac\pi2$、$S=\sqrt3$ | **$\sqrt3-\sqrt2$ 或 $\sqrt3$** |
| M-T-219-V3 | $\sin C=\sin(A+B)$ 代入 ⟹ $\sin A(9\cos B-1)=0$；$\cos\frac B2$ 由半角 ⟹ $\sin\angle ABD=\frac23$，面积拆分 $S_1+S_2=S$ | **$\frac{2\sqrt5}3$** |
| M-T-221-E1 | 三条件都给 $\cos A=\frac12$；$2R=2$ ⟹ $b=2\sin B$、$c=2\sin C$ ⟹ 周长 $=2\sqrt3\sin(B+\frac\pi6)+\sqrt3$ | **$(3+\sqrt3,3\sqrt3]$** |
| M-T-221-V1 | $a\cos B=\sin A$ ⟹ $\tan B=b=\sqrt3$；$(a+c)^2=3+3ac$、$ac\in(0,3]$ | **$(2\sqrt3,3\sqrt3]$** |
| M-T-221-V2 | $\sin A-\sqrt3\cos A=\sqrt3$ ⟹ $2\sin(A-\frac\pi3)=\sqrt3$ ⟹ $A=\frac{2\pi}3$；$bc=4$，$L=s+\sqrt{s^2-4}$ 增 | **$4+2\sqrt3$** |
| M-T-221-V3 | 三条件都给 $A=\frac\pi3$；$a=4\sin A=2\sqrt3$；$(b+c)^2-12=3bc\le\frac34(b+c)^2$ ⟹ $b+c\le4\sqrt3$ | **$(4\sqrt3,6\sqrt3]$** |
| M-T-222-E1 | 三条件都给 $\tan B=\sqrt3$；$a=2\sqrt3\cot C+2$，$C\in(\frac\pi6,\frac\pi2)$ | **$(2,8)$** |
| M-T-222-V1 | $2\sin A\cos C=\sin(B+C)=\sin A$ ⟹ $\cos C=\frac12$；$c^2=3(a-1)^2+1$ | **$[1,2)$** |
| M-T-222-V2 | $\sin(B+C)-\sin B=\sin B\cos C$ ⟹ $\cos B\sin C=\sin B$；$b=\frac1{1+\cos C}\in(\frac12,1)$ | **$(\frac12,\sqrt2)$** |
| M-T-222-V3 | $f(x)=\cos(2x+\frac\pi3)+1$ ⟹ 最大 $2$；$f(A)=\frac32$ ⟹ $A=\frac{2\pi}3$；$a^2=4-bc\ge3$ | **$\sqrt3$** |

## 五处根号丢失还原（全部有硬判据）

- M-T-219-E1 答案 `21/7` ⟹ **$\frac{\sqrt{21}}7$**（$=\frac{\sqrt3}{\sqrt7}$，由 $a=2t,c=\sqrt7t$ 得）
- M-T-219-V1 答案 `2 2` ⟹ **$2\sqrt2$**（$2\sin A+2\cos A$ 的振幅）
- M-T-219-V3 答案 `2 5/3` ⟹ **$\frac{2\sqrt5}3$**（$\sin B=\frac{4\sqrt5}9$，$S=\frac{2\sqrt5}9ac$）
- M-T-222-E1 答案 `2,8` ⟹ **$(2,8)$**（$\cot C\in(0,\sqrt3)$）
- M-T-222-V2 答案 `1/2, 2` ⟹ **$(\frac12,\sqrt2)$**（$c^2\in(\frac14,2)$）

## 两处原书详解的笔误

- **M-T-222-V2**：详解写「$f(b)=b^2+2b-1$ 在 $(\frac12,1)$ 上**单调递减**」，实为**递增**（导数 $2b+2>0$）。端点值 $f(\frac12)=\frac14$、$f(1)=2$ 与结论 $c^2\in(\frac14,2)$ 一致，故结论无误。
- **M-T-219-V2**：详解在条件②的推导中分母写作 $\sin C$，应为 $\sin A$（否则约不出 $\cos A=\frac12$）。结果 $\cos A=\frac12$ 正确。

## 一处详解缺失，由我补出（M-T-221-V2）

原书 `solution` 为空。我的独立推导：

$\sqrt3\sin C=\sin A\sin C-\sqrt3\cos A\sin C$ ⟹ $\sqrt3=\sin A-\sqrt3\cos A$ ⟹ $2\sin(A-\frac\pi3)=\sqrt3$。

$A-\frac\pi3=\frac\pi3$ 或 $\frac{2\pi}3$ ⟹ $A=\frac{2\pi}3$ 或 $A=\pi$（舍）。

$S=\frac{\sqrt3}4bc=\sqrt3$ ⟹ $bc=4$；$a^2=b^2+c^2+bc=(b+c)^2-4$。令 $s=b+c\ge4$，
$L=s+\sqrt{s^2-4}$ 单调递增 ⟹ $L_{\min}=4+\sqrt{12}=4+2\sqrt3$ ✓ 与答案吻合。
"""

T219_E1 = {
    'type': '解答',
    'stem_text': (
        r"在 $\triangle ABC$ 中，角 $A,B,C$ 的对边分别为 $a,b,c$，$\triangle ABC$ 的面积为 $S$，且 $S=\dfrac{\sqrt3}4\left(a^{2}+b^{2}-c^{2}\right)$．" "\n"
        r"(1) 求角 $C$；" "\n"
        r"(2) 若 $3a=2b$，求 $\sin A$．"
    ),
    'opts': [],
    'answer': r"(1) $C=\dfrac{\pi}3$；(2) $\sin A=\dfrac{\sqrt{21}}7$",
    'analysis': (
        r"(1) 把 $S=\frac12ab\sin C$ 与余弦定理 $a^2+b^2-c^2=2ab\cos C$ 同时代入已知式，"
        r"约去 $ab$ 即得 $\tan C$；(2) 由 $3a=2b$ 设 $a=2t,b=3t$，余弦定理求 $c$，再用正弦定理求 $\sin A$．"
    ),
    'solution': (
        r"**(1)** 由 $S=\dfrac12ab\sin C$ 及余弦定理 $a^{2}+b^{2}-c^{2}=2ab\cos C$，代入已知条件得" "\n"
        r"$\dfrac12ab\sin C=\dfrac{\sqrt3}4\cdot 2ab\cos C=\dfrac{\sqrt3}2ab\cos C$．" "\n"
        r"$\because ab>0$，$\therefore\sin C=\sqrt3\cos C$，即 $\tan C=\sqrt3$．" "\n"
        r"又 $C\in(0,\pi)$，$\therefore C=\dfrac\pi3$．" "\n"
        r"**(2)** 由 $3a=2b$ 可设 $a=2t,\ b=3t\ (t>0)$．" "\n"
        r"由余弦定理：$c^{2}=a^{2}+b^{2}-2ab\cos C=4t^{2}+9t^{2}-2\cdot 2t\cdot 3t\cdot\dfrac12=7t^{2}$，" "\n"
        r"$\therefore c=\sqrt7\,t$．" "\n"
        r"由正弦定理 $\dfrac a{\sin A}=\dfrac c{\sin C}$ 得" "\n"
        r"$\sin A=\dfrac{a\sin C}c=\dfrac{2t\cdot\frac{\sqrt3}2}{\sqrt7\,t}=\dfrac{\sqrt3}{\sqrt7}=\dfrac{\sqrt{21}}7$．"
    ),
    'review': (
        r"**① 面积与余弦定理的联用（题眼）**：" "\n"
        r"$S=\frac{\sqrt3}4(a^2+b^2-c^2)$ 中 $a^2+b^2-c^2$ 正是余弦定理的分子，换成 $2ab\cos C$ 后与 $S=\frac12ab\sin C$ **约去 $ab$**，直接得 $\tan C$ ✓✓✓" "\n"
        r"② **$\tan C=\sqrt3$ ⟹ $C=\frac\pi3$**（$C\in(0,\pi)$ 内唯一）✓✓✓" "\n"
        r"③ **比例设元**：$3a=2b$ ⟹ 设 $a=2t,b=3t$，**避免分数运算** ✓✓✓" "\n"
        r"④ **$c^2$ 的验算**：$4t^2+9t^2-6t^2=7t^2$（交叉项 $2\cdot2t\cdot3t\cdot\frac12=6t^2$）✓✓✓" "\n"
        r"⑤ **$\sin A=\frac{\sqrt3}{\sqrt7}$ 的有理化**：分子分母同乘 $\sqrt7$ 得 $\frac{\sqrt{21}}7$ ✓✓✓" "\n"
        r"（**原书答案 `21/7` 是根号丢失**，$\frac{21}7=3>1$ 不可能是正弦值 ✓✓✓）" "\n"
        r"**答案 $\frac{\sqrt{21}}7\approx0.6547$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（面积式含边平方和 ⟹ 化 $\tan$）**：" "\n"
        r"① ⭐⭐ **见到 $S=k(a^2+b^2-c^2)$ 型条件，立刻用余弦定理把右边换成 $2ab\cos C$**，与 $S=\frac12ab\sin C$ 约去 $ab$ ⟹ 得到 $\tan C$ ✓✓✓；" "\n"
        r"② ⭐⭐ **$\tan$ 型角值在 $(0,\pi)$ 内唯一确定该角**（$\tan>0$ 取锐角、$\tan<0$ 取钝角）✓✓✓；" "\n"
        r"③ ⭐⭐ **已知两边之比求第三量：设 $a=mt,b=nt$，全程用 $t$ 运算，最后 $t$ 自动约去** ✓✓✓；" "\n"
        r"④ ⚠ **正弦定理求角时注意 $\sin A$ 可能对应两解**，本题 $\sin A=\frac{\sqrt{21}}7$ 且 $a<c$（$2t<\sqrt7t$）⟹ $A<C=\frac\pi3$ ⟹ $A$ 为锐角、唯一 ✓✓✓"
    ),
    'difficulty': 0.80,
    'topics': ['M-T-219'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-219-E1',
}

T219_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知 $\triangle ABC$ 中，角 $A,B,C$ 所对的边分别为 $a,b,c$，$A\ne\dfrac\pi2$，且满足 $bc\sin 2A+20\cos(B+C)=0$．" "\n"
        r"(1) 求 $\triangle ABC$ 的面积 $S$；" "\n"
        r"(2) 若 $a^{2}=4S$，求 $\dfrac cb+\dfrac bc$ 的最大值．"
    ),
    'opts': [],
    'answer': r"(1) $S=5$；(2) 最大值为 $2\sqrt2$",
    'analysis': (
        r"(1) 用 $\cos(B+C)=-\cos A$ 与 $\sin2A=2\sin A\cos A$ 把条件化为 $\cos A(2bc\sin A-20)=0$，"
        r"由 $A\ne\frac\pi2$ 得 $bc\sin A=10$；(2) $4S=2bc\sin A$，代入余弦定理后整体除以 $bc$ 即得 $2\sin A+2\cos A$．"
    ),
    'solution': (
        r"**(1)** 在 $\triangle ABC$ 中 $A+B+C=\pi$，$\therefore B+C=\pi-A$，$\cos(B+C)=-\cos A$．" "\n"
        r"由 $bc\sin 2A+20\cos(B+C)=0$ 得 $2bc\sin A\cos A-20\cos A=0$，" "\n"
        r"即 $2\cos A\,(bc\sin A-10)=0$．" "\n"
        r"$\because A\ne\dfrac\pi2$，$\therefore\cos A\ne0$，$\therefore bc\sin A=10$．" "\n"
        r"$\therefore S=\dfrac12bc\sin A=5$．" "\n"
        r"**(2)** 由 $a^{2}=4S$ 及 $S=5$ 得 $a^{2}=20$；又 $4S=4\cdot\dfrac12bc\sin A=2bc\sin A$．" "\n"
        r"由余弦定理 $a^{2}=b^{2}+c^{2}-2bc\cos A$，于是" "\n"
        r"$b^{2}+c^{2}-2bc\cos A=2bc\sin A$，即 $b^{2}+c^{2}=2bc\sin A+2bc\cos A$．" "\n"
        r"两边同除以 $bc>0$：" "\n"
        r"$\dfrac cb+\dfrac bc=\dfrac{b^{2}+c^{2}}{bc}=2\sin A+2\cos A=2\sqrt2\sin\left(A+\dfrac\pi4\right)\le 2\sqrt2$．" "\n"
        r"当 $A+\dfrac\pi4=\dfrac\pi2$ 即 $A=\dfrac\pi4$ 时取等号．" "\n"
        r"（此时 $b^{2}+c^{2}=2\sqrt2\,bc$，即 $\left(\dfrac bc\right)^{2}-2\sqrt2\cdot\dfrac bc+1=0$，解得 $\dfrac bc=\sqrt2+1$ 或 $\sqrt2-1$，均为正数，故可取等）" "\n"
        r"$\therefore\dfrac cb+\dfrac bc$ 的最大值为 $2\sqrt2$．"
    ),
    'review': (
        r"**① $\cos(B+C)=-\cos A$ 是本题第一处关键变形**（内角和定理的余弦版）✓✓✓" "\n"
        r"② **$\sin2A=2\sin A\cos A$ 后整式出现公因式 $\cos A$**，而 $A\ne\frac\pi2$ 正是**为排除 $\cos A=0$ 而设** ✓✓✓" "\n"
        r"（**若忽略该条件，$\cos A=0$ 会给 $S$ 不定 —— 这就是条件的作用**）" "\n"
        r"③ **$a^2=4S$ 的用法很妙**：$4S=2bc\sin A$，与余弦定理 $a^2=b^2+c^2-2bc\cos A$ 联立后，" "\n"
        r"$\cos A$ 项**移到右边变成 $+2bc\cos A$**，于是 $\frac{b^2+c^2}{bc}=2\sin A+2\cos A$ ✓✓✓" "\n"
        r"④ **取等可行性检验（必须做）**：$A=\frac\pi4$ 时要求 $b^2+c^2=2\sqrt2\,bc$，" "\n"
        r"即 $\left(\frac bc\right)^2-2\sqrt2\frac bc+1=0$，判别式 $=8-4=4>0$，两根 $\sqrt2\pm1>0$ ✓✓✓ **确实可取等**" "\n"
        r"⑤ **数值对拍**：取 $\frac bc=\sqrt2+1$。由 $bc\sin A=10$ 且 $A=\frac\pi4$ 得 $bc=10\sqrt2\approx14.142$，" "\n"
        r"于是 $c^2=\frac{14.142}{2.414}=5.858$、$c\approx2.420$、$b\approx5.842$。" "\n"
        r"$a^2=b^2+c^2-2bc\cos\frac\pi4=34.13+5.858-2\times14.142\times0.7071=19.99\approx20$ ✓✓✓ **与 $a^2=4S=20$ 闭合**" "\n"
        r"**答案 $S=5$、最大值 $2\sqrt2$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（$\cos(B+C)$ 与 $\sin2A$ 同现 ⟹ 提公因式）**：" "\n"
        r"① ⭐⭐ **$\cos(B+C)=-\cos A$、$\sin(B+C)=\sin A$** —— 凡见到 $B+C$ 先换成 $\pi-A$ ✓✓✓；" "\n"
        r"② ⭐⭐ **条件含 $\sin2A$ 又含 $\cos A$ ⟹ 展开 $\sin2A$ 后必能提 $\cos A$**，题目给的 $A\ne\frac\pi2$ 就是**放行该约去**的信号 ✓✓✓；" "\n"
        r"③ ⭐⭐ **求 $\frac cb+\frac bc$ 型式子：先通分成 $\frac{b^2+c^2}{bc}$，再整体用余弦定理替换 $b^2+c^2$** ✓✓✓；" "\n"
        r"④ ⭐⭐ **$p\sin A+q\cos A=\sqrt{p^2+q^2}\sin(A+\varphi)$，其中 $\tan\varphi=\frac qp$**（本题 $p=q=2$ ⟹ 振幅 $2\sqrt2$）✓✓✓；" "\n"
        r"⑤ ⚠ **取等必须回代检验是否能构成三角形** —— 光看 $\sin\le1$ 不够，要验证边长有正解 ✓✓✓"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-219'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-219-V1',
}

T219_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知 $a,b,c$ 分别为 $\triangle ABC$ 内角 $A,B,C$ 的对边，若 $\triangle ABC$ 同时满足以下四个条件中的三个：" "\n"
        r"① $\dfrac{b-a}c=\dfrac{2\sqrt6\,a+3c}{3(a+b)}$，② $\dfrac{\cos C}{\cos A}+\dfrac ca=\dfrac{2b}a$，③ $a=\sqrt6$，④ $b=2\sqrt2$．" "\n"
        r"(1) 条件①②能否同时满足，请说明理由；" "\n"
        r"(2) 以上四个条件，请在满足三角形有解的所有组合中任选一组，并求出对应 $\triangle ABC$ 的面积．"
    ),
    'opts': [],
    'answer': r"(1) 不能同时满足①②；(2) 满足①③④时 $S=\sqrt3-\sqrt2$；满足②③④时 $S=\sqrt3$",
    'analysis': (
        r"(1) 由①交叉相乘配余弦定理得 $\cos B=-\frac{\sqrt6}3$，由②配正弦定理得 $\cos A=\frac12$，两者推出 $A+B>\pi$，矛盾；"
        r"(2) 故只能是①③④或②③④，分别用余弦定理、正弦定理求第三边再算面积．"
    ),
    'solution': (
        r"**(1)** 由① $\dfrac{b-a}c=\dfrac{2\sqrt6\,a+3c}{3(a+b)}$ 交叉相乘得" "\n"
        r"$3(a+b)(b-a)=c\left(2\sqrt6\,a+3c\right)$，即 $3\left(b^{2}-a^{2}\right)=2\sqrt6\,ac+3c^{2}$，" "\n"
        r"整理得 $3\left(a^{2}+c^{2}-b^{2}\right)=-2\sqrt6\,ac$，" "\n"
        r"$\therefore\cos B=\dfrac{a^{2}+c^{2}-b^{2}}{2ac}=-\dfrac{\sqrt6}3$．" "\n"
        r"由② $\dfrac{\cos C}{\cos A}+\dfrac ca=\dfrac{2b}a$ 及正弦定理 $\dfrac ca=\dfrac{\sin C}{\sin A}$、$\dfrac ba=\dfrac{\sin B}{\sin A}$，得" "\n"
        r"$\dfrac{\cos C}{\cos A}+\dfrac{\sin C}{\sin A}=\dfrac{2\sin B}{\sin A}$，" "\n"
        r"通分：$\dfrac{\sin A\cos C+\cos A\sin C}{\cos A\sin A}=\dfrac{2\sin B}{\sin A}$，即 $\dfrac{\sin(A+C)}{\cos A\sin A}=\dfrac{2\sin B}{\sin A}$．" "\n"
        r"$\because\sin(A+C)=\sin B\ne0$、$\sin A\ne0$，$\therefore\dfrac1{\cos A}=2$，即 $\cos A=\dfrac12$，$\therefore A=\dfrac\pi3$．" "\n"
        r"$\because\cos B=-\dfrac{\sqrt6}3<-\dfrac12$，且 $B\in(0,\pi)$，$\therefore B>\dfrac{2\pi}3$．" "\n"
        r"于是 $A+B>\dfrac\pi3+\dfrac{2\pi}3=\pi$，与三角形内角和矛盾．" "\n"
        r"$\therefore$ 条件①②不能同时满足．" "\n"
        r"**(2)** 由(1)知满足条件的组合只能是①③④或②③④．" "\n"
        r"**若满足①③④**：$a=\sqrt6$、$b=2\sqrt2$、$\cos B=-\dfrac{\sqrt6}3$．" "\n"
        r"由 $b^{2}=a^{2}+c^{2}-2ac\cos B$ 得 $8=6+c^{2}-2\sqrt6\,c\cdot\left(-\dfrac{\sqrt6}3\right)=6+c^{2}+4c$，" "\n"
        r"即 $c^{2}+4c-2=0$，解得 $c=\sqrt6-2$（负根 $-\sqrt6-2$ 舍去）．" "\n"
        r"$\sin B=\sqrt{1-\cos^{2}B}=\sqrt{1-\dfrac69}=\dfrac{\sqrt3}3$，" "\n"
        r"$S=\dfrac12ac\sin B=\dfrac12\cdot\sqrt6\cdot(\sqrt6-2)\cdot\dfrac{\sqrt3}3=\dfrac{(3-\sqrt6)\sqrt3}3=\sqrt3-\sqrt2$．" "\n"
        r"**若满足②③④**：$a=\sqrt6$、$b=2\sqrt2$、$A=\dfrac\pi3$．" "\n"
        r"由正弦定理 $\dfrac a{\sin A}=\dfrac b{\sin B}$ 得 $\dfrac{\sqrt6}{\frac{\sqrt3}2}=\dfrac{2\sqrt2}{\sin B}$，即 $2\sqrt2=\dfrac{2\sqrt2}{\sin B}$，" "\n"
        r"$\therefore\sin B=1$，$B=\dfrac\pi2$，于是 $c=\sqrt{b^{2}-a^{2}}=\sqrt{8-6}=\sqrt2$．" "\n"
        r"$S=\dfrac12ac=\dfrac12\cdot\sqrt6\cdot\sqrt2=\sqrt3$．"
    ),
    'review': (
        r"**① 条件①的化简是交叉相乘**：$3(a+b)(b-a)=3(b^2-a^2)$，与右边 $3c^2$ 合并 ⟹ 凑出 $a^2+c^2-b^2$ ✓✓✓" "\n"
        r"（**$\cos B=-\frac{\sqrt6}3\approx-0.8165$**，注意 $-\frac{\sqrt6}3<-\frac12$ 是关键比较）" "\n"
        r"② **条件②的化简：先用正弦定理把边比换成正弦比，再通分** ⟹ 分子出现 $\sin(A+C)=\sin B$，与右边约去 ✓✓✓" "\n"
        r"（**原书此处分母写作 $\sin C$，应为 $\sin A$** —— 否则 $\sin B$ 无法约净、得不出 $\cos A=\frac12$）" "\n"
        r"③ **矛盾点在于 $A+B>\pi$**：$A=\frac\pi3$、$B>\frac{2\pi}3$，和为 $>\pi$ ✓✓✓" "\n"
        r"④ **组合只能是①③④或②③④**：四个条件选三个共 $4$ 种，去掉含①②的两种（①②不可同时），剩 $2$ 种 ✓✓✓" "\n"
        r"⑤ **①③④的数值链**：$c^2+4c-2=0$ ⟹ $c=\frac{-4+\sqrt{24}}2=\sqrt6-2\approx0.449$；" "\n"
        r"$S=\frac12\cdot2.449\cdot0.449\cdot0.5774=0.3178$，而 $\sqrt3-\sqrt2=1.732-1.414=0.3178$ ✓✓✓ **完全吻合**" "\n"
        r"⑥ **②③④的数值链**：$\frac a{\sin A}=\frac{2.449}{0.866}=2.828=b$ ⟹ $\sin B=1$ ⟹ $B=\frac\pi2$；" "\n"
        r"$c=\sqrt2=1.414$；$S=\frac12\cdot2.449\cdot1.414=1.732=\sqrt3$ ✓✓✓" "\n"
        r"**答案 $\sqrt3-\sqrt2$ 与 $\sqrt3$ 均正确** ✓" "\n"
        r"**⭐⭐ 通法（四选三 / 条件组合型新定义题）**：" "\n"
        r"① ⭐⭐ **先判哪两个条件互斥**：分别把每个条件化成角（或边）的显式结论，再检查是否矛盾，**比逐个试组合快得多** ✓✓✓；" "\n"
        r"② ⭐⭐ **边角混合条件化角用正弦定理、化边用余弦定理** —— 本题①化边（凑 $a^2+c^2-b^2$）、②化角（凑 $\sin(A+C)$）✓✓✓；" "\n"
        r"③ ⭐⭐ **$\sin(A+C)=\sin B$、$\cos(B+C)=-\cos A$** 是解三角形最高频的两个恒等式 ✓✓✓；" "\n"
        r"④ ⭐ **用 $\cos B<-\frac12$ 判 $B>\frac{2\pi}3$**：$\cos$ 在 $(0,\pi)$ 上递减，比较时**记住几个锚点值 $\cos\frac\pi3=\frac12$、$\cos\frac{2\pi}3=-\frac12$** ✓✓✓；" "\n"
        r"⑤ ⭐ **二次方程两根要舍负**：$c^2+4c-2=0$ 的两根是 $\sqrt6-2$ 与 $-\sqrt6-2$，后者为负舍去 ✓✓✓"
    ),
    'difficulty': 0.90,
    'topics': ['M-T-219'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-219-V2',
}

T219_V3 = {
    'type': '解答',
    'stem_text': (
        r"已知 $\triangle ABC$ 的内角 $A,B,C$ 的对边分别为 $a,b,c$，且 $9c-a=9b\cos A$．" "\n"
        r"(1) 求 $\cos B$；" "\n"
        r"(2) 若角 $B$ 的平分线与 $AC$ 交于点 $D$，且 $BD=1$，求 $\dfrac1a+\dfrac1c$ 的值．"
    ),
    'opts': [],
    'answer': r"(1) $\cos B=\dfrac19$；(2) $\dfrac1a+\dfrac1c=\dfrac{2\sqrt5}3$",
    'analysis': (
        r"(1) 用正弦定理化边为角，再用 $\sin C=\sin(A+B)$ 展开，约去 $\sin A$ 即得 $\cos B$；"
        r"(2) 由半角公式得 $\sin\angle ABD=\frac23$，把 $\triangle ABC$ 拆成 $\triangle ABD$ 与 $\triangle CBD$，用 $S_1+S_2=S$ 列方程．"
    ),
    'solution': (
        r"**(1)** 由 $9c-a=9b\cos A$ 及正弦定理得 $9\sin C-\sin A=9\sin B\cos A$．" "\n"
        r"$\because\sin C=\sin(A+B)=\sin A\cos B+\cos A\sin B$，代入得" "\n"
        r"$9\sin A\cos B+9\cos A\sin B-\sin A=9\sin B\cos A$，" "\n"
        r"即 $9\sin A\cos B-\sin A=0$，$\sin A(9\cos B-1)=0$．" "\n"
        r"$\because A\in(0,\pi)$，$\sin A\ne0$，$\therefore\cos B=\dfrac19$．" "\n"
        r"**(2)** 设 $\angle ABD=\angle CBD=\dfrac B2$．由 $\cos B=1-2\sin^{2}\dfrac B2=\dfrac19$ 且 $\sin\dfrac B2>0$ 得" "\n"
        r"$\sin\dfrac B2=\sqrt{\dfrac{1-\frac19}2}=\dfrac23$．" "\n"
        r"又 $\sin B=\sqrt{1-\cos^{2}B}=\sqrt{1-\dfrac1{81}}=\dfrac{4\sqrt5}9$．" "\n"
        r"记 $\triangle ABC,\triangle ABD,\triangle CBD$ 的面积分别为 $S,S_1,S_2$，则" "\n"
        r"$S=\dfrac12ac\sin B=\dfrac12ac\cdot\dfrac{4\sqrt5}9=\dfrac{2\sqrt5}9ac$，" "\n"
        r"$S_1=\dfrac12\cdot c\cdot BD\cdot\sin\dfrac B2=\dfrac12\cdot c\cdot1\cdot\dfrac23=\dfrac c3$，" "\n"
        r"$S_2=\dfrac12\cdot a\cdot BD\cdot\sin\dfrac B2=\dfrac a3$．" "\n"
        r"由 $S_1+S_2=S$ 得 $\dfrac{a+c}3=\dfrac{2\sqrt5}9ac$，两边同除以 $ac$： " "\n"
        r"$\dfrac1a+\dfrac1c=\dfrac{a+c}{ac}=\dfrac{2\sqrt5}3$．"
    ),
    'review': (
        r"**① 方法一（余弦定理）也通**：$9c-a=9b\cdot\frac{b^2+c^2-a^2}{2bc}$ ⟹ 整理得 $a^2+c^2-b^2=\frac29ac$ ⟹ $\cos B=\frac{a^2+c^2-b^2}{2ac}=\frac19$ ✓✓✓ **两法一致**" "\n"
        r"（**正弦定理法更简洁**，因为 $\sin C=\sin(A+B)$ 展开后 $9\cos A\sin B$ 项恰好抵消）" "\n"
        r"② **$\sin A\ne0$ 是约去的依据**（$A\in(0,\pi)$）✓✓✓" "\n"
        r"③ **半角公式的方向**：$\cos B=1-2\sin^2\frac B2$ ⟹ $\sin\frac B2=\sqrt{\frac{1-\cos B}2}=\sqrt{\frac{4}{9}}=\frac23$ ✓✓✓" "\n"
        r"（注意 $\frac B2\in(0,\frac\pi2)$，故取正根）" "\n"
        r"④ **面积拆分法（本题题眼）**：角平分线把 $\triangle ABC$ 分成两个小三角形，" "\n"
        r"$S_1+S_2=S$，其中 $S_1=\frac12 c\cdot BD\sin\frac B2$、$S_2=\frac12 a\cdot BD\sin\frac B2$ ✓✓✓" "\n"
        r"⑤ **最后一步同除以 $ac$ 即得 $\frac1a+\frac1c$** —— 这正是题目所求的形式，**无需解出 $a,c$** ✓✓✓" "\n"
        r"⑥ **数值对拍**：$\frac{2\sqrt5}3=\frac{2\times2.2361}3=1.4907$。" "\n"
        r"取 $a=c$（等腰）检验：$S=\frac{2\sqrt5}9a^2$、$S_1+S_2=\frac{2a}3$ ⟹ $\frac{2a}{3}=\frac{2\sqrt5}{9}a^2$ ⟹ $a=\frac3{\sqrt5}=1.3416$。" "\n"
        r"此时 $\frac1a+\frac1c=\frac2{1.3416}=1.4907$ ✓✓✓ **完全吻合**" "\n"
        r"**答案 $\frac19$ 与 $\frac{2\sqrt5}3$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（角平分线 + 面积拆分）**：" "\n"
        r"① ⭐⭐ **角平分线把大三角形拆成两个小三角形，$S_1+S_2=S$** —— 这比角平分线定理更直接，因为它**把 $BD$ 的长度用上了** ✓✓✓；" "\n"
        r"② ⭐⭐ **两个小三角形的面积都含 $\sin\frac B2$**，而大三角形含 $\sin B=2\sin\frac B2\cos\frac B2$ ⟹ 约去 $\sin\frac B2$ 后只剩 $\cos\frac B2$ ✓✓✓；" "\n"
        r"③ ⭐⭐ **所求为 $\frac1a+\frac1c$ 型（倒数和）时：把等式写成 $\frac{a+c}{ac}$ 的形式，直接整体除 $ac$**，不必解出 $a,c$ ✓✓✓；" "\n"
        r"④ ⭐⭐ **半角公式 $\sin\frac B2=\sqrt{\frac{1-\cos B}2}$、$\cos\frac B2=\sqrt{\frac{1+\cos B}2}$** 在 $\frac B2\in(0,\frac\pi2)$ 时均取正 ✓✓✓；" "\n"
        r"⑤ ⭐ **正弦定理法 vs 余弦定理法的选择**：条件形如「边 = 边 × cos（角）」时，**正弦定理 + $\sin C=\sin(A+B)$ 往往一步抵消**，优先试它 ✓✓✓"
    ),
    'difficulty': 0.90,
    'topics': ['M-T-219'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-219-V3',
}

T221_E1 = {
    'type': '解答',
    'stem_text': (
        r"在① $\dfrac cb$ 是 $1$ 和 $\dfrac{\tan A}{\tan B}$ 的等差中项；② $2b-c-2a\cos C=0$；③ $\cos^{2}B+\cos^{2}C+\sin B\sin C=1+\cos^{2}A$．" "\n"
        r"这三个条件中任选一个，补充在下面的问题中，并解答问题．" "\n"
        r"在 $\triangle ABC$ 中，角 $A,B,C$ 所对的边分别为 $a,b,c$，且满足条件 ____（填写所选条件的序号）．" "\n"
        r"(1) 求角 $A$；" "\n"
        r"(2) 若 $a=\sqrt3$，求锐角 $\triangle ABC$ 的周长的取值范围．"
    ),
    'opts': [],
    'answer': r"(1) 条件选择见解析，$A=\dfrac\pi3$；(2) 周长的取值范围为 $\left(3+\sqrt3,\ 3\sqrt3\right]$",
    'analysis': (
        r"(1) 选①用正弦定理配 $1+\frac{\tan A}{\tan B}$ 通分；选②用 $\sin C=2\sin(A+C)-2\sin A\cos C$；选③把 $\cos^2$ 换成 $1-\sin^2$ 再用正弦定理化边；(2) 由 $2R=2$ 得 $b=2\sin B$、$c=2\sin C$，化成辅助角后按锐角条件定 $B$ 的范围．"
    ),
    'solution': (
        r"**(1)** 三个条件都给出 $A=\dfrac\pi3$，下面分别说明．" "\n"
        r"**选①**：由 $\dfrac cb$ 是 $1$ 与 $\dfrac{\tan A}{\tan B}$ 的等差中项得 $1+\dfrac{\tan A}{\tan B}=\dfrac{2c}b$．" "\n"
        r"由正弦定理 $\dfrac cb=\dfrac{\sin C}{\sin B}$，且 $\dfrac{\tan A}{\tan B}=\dfrac{\sin A\cos B}{\cos A\sin B}$，于是" "\n"
        r"$\dfrac{2\sin C}{\sin B}=1+\dfrac{\sin A\cos B}{\cos A\sin B}=\dfrac{\cos A\sin B+\sin A\cos B}{\cos A\sin B}=\dfrac{\sin(A+B)}{\cos A\sin B}=\dfrac{\sin C}{\cos A\sin B}$．" "\n"
        r"$\because\sin B>0$、$\sin C>0$，$\therefore \dfrac2{\sin B}=\dfrac1{\cos A\sin B}$，即 $\cos A=\dfrac12$，$\therefore A=\dfrac\pi3$．" "\n"
        r"**选②**：由 $2b-c-2a\cos C=0$ 及正弦定理得 $2\sin B-2\sin A\cos C=\sin C$．" "\n"
        r"$\therefore\sin C=2\sin(A+C)-2\sin A\cos C=2(\sin A\cos C+\cos A\sin C)-2\sin A\cos C=2\cos A\sin C$．" "\n"
        r"$\because\sin C>0$，$\therefore\cos A=\dfrac12$，$\therefore A=\dfrac\pi3$．" "\n"
        r"**选③**：由 $\cos^{2}B+\cos^{2}C+\sin B\sin C=1+\cos^{2}A$ 得" "\n"
        r"$(1-\sin^{2}B)+(1-\sin^{2}C)+\sin B\sin C=1+(1-\sin^{2}A)$，" "\n"
        r"即 $\sin^{2}B+\sin^{2}C-\sin^{2}A=\sin B\sin C$．" "\n"
        r"由正弦定理得 $b^{2}+c^{2}-a^{2}=bc$，故 $\cos A=\dfrac{b^{2}+c^{2}-a^{2}}{2bc}=\dfrac12$，$\therefore A=\dfrac\pi3$．" "\n"
        r"**(2)** 由 $A=\dfrac\pi3$、$a=\sqrt3$ 及正弦定理 $\dfrac a{\sin A}=2R$ 得 $2R=\dfrac{\sqrt3}{\frac{\sqrt3}2}=2$，" "\n"
        r"$\therefore b=2\sin B$、$c=2\sin C$，且 $C=\pi-A-B=\dfrac{2\pi}3-B$．" "\n"
        r"$a+b+c=\sqrt3+2\sin B+2\sin\left(\dfrac{2\pi}3-B\right)$" "\n"
        r"$=\sqrt3+2\sin B+2\left(\dfrac{\sqrt3}2\cos B+\dfrac12\sin B\right)=\sqrt3+3\sin B+\sqrt3\cos B$" "\n"
        r"$=\sqrt3+2\sqrt3\sin\left(B+\dfrac\pi6\right)$．" "\n"
        r"$\because\triangle ABC$ 为锐角三角形，$\therefore 0<B<\dfrac\pi2$ 且 $0<C=\dfrac{2\pi}3-B<\dfrac\pi2$，" "\n"
        r"解得 $\dfrac\pi6<B<\dfrac\pi2$，于是 $B+\dfrac\pi6\in\left(\dfrac\pi3,\dfrac{2\pi}3\right)$，$\sin\left(B+\dfrac\pi6\right)\in\left(\dfrac{\sqrt3}2,1\right]$．" "\n"
        r"$\therefore a+b+c\in\left(\sqrt3+2\sqrt3\cdot\dfrac{\sqrt3}2,\ \sqrt3+2\sqrt3\right]=\left(3+\sqrt3,\ 3\sqrt3\right]$．"
    ),
    'review': (
        r"**① 三个条件殊途同归 —— 这是三选一题的通用特征**（命题人保证任选其一都能做）✓✓✓" "\n"
        r"② **选①的关键变形**：$1+\frac{\tan A}{\tan B}$ 通分后分子是 $\cos A\sin B+\sin A\cos B=\sin(A+B)=\sin C$，" "\n"
        r"与左边的 $2\sin C$ 约去 ⟹ 得 $\cos A=\frac12$ ✓✓✓" "\n"
        r"③ **选②的关键变形**：$\sin B=\sin(A+C)$ 展开后 $2\sin A\cos C$ 项**恰好抵消** ✓✓✓" "\n"
        r"④ **选③的关键变形**：$\cos^2$ 全部换成 $1-\sin^2$，两边的 $2$ 抵消，剩下 $\sin^2$ 用正弦定理化成边 ✓✓✓" "\n"
        r"⑤ **$2R=2$ 使 $b=2\sin B$、$c=2\sin C$** —— 把周长问题**完全转化为单变量 $B$ 的三角函数** ✓✓✓" "\n"
        r"⑥ **锐角条件给出 $B\in(\frac\pi6,\frac\pi2)$**：除 $B<\frac\pi2$ 外，还要 $C=\frac{2\pi}3-B<\frac\pi2$ ⟹ $B>\frac\pi6$ ✓✓✓" "\n"
        r"（**只写 $B\in(0,\frac\pi2)$ 会错**，这是本题最主要陷阱）" "\n"
        r"⑦ **端点的开闭**：$\sin(B+\frac\pi6)\in(\frac{\sqrt3}2,1]$，右端在 $B+\frac\pi6=\frac\pi2$ 即 $B=\frac\pi3$ 取到（此时 $C=\frac\pi3$，是锐角 ⟹ **闭**）；" "\n"
        r"左端 $B\to\frac\pi6$ 或 $B\to\frac\pi2$ 时 $C\to\frac\pi2$ 或 $B\to\frac\pi2$（非锐角）⟹ **开** ✓✓✓" "\n"
        r"⑧ **数值对拍**：取 $B=\frac\pi3$（正三角形）：周长 $=3\sqrt3=5.196$ ✓；取 $B=\frac\pi6+\varepsilon$：$C\to\frac\pi2$，$b\to1$、$c\to2$，周长 $\to\sqrt3+3=4.732=3+\sqrt3$ ✓✓✓" "\n"
        r"**答案 $(3+\sqrt3,3\sqrt3]$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（三选一型 + 锐角三角形范围）**：" "\n"
        r"① ⭐⭐ **三选一题的三个条件必然推出同一结论**，考试时选最有把握的一个即可，**不必三个都做** ✓✓✓；" "\n"
        r"② ⭐⭐ **化角三板斧**：$\sin(A+B)=\sin C$、$\sin(A+C)=\sin B$、$\cos(B+C)=-\cos A$ ✓✓✓；" "\n"
        r"③ ⭐⭐ **$a$ 与 $A$ 已知 ⟹ 先求 $2R=\frac a{\sin A}$，再用 $b=2R\sin B$、$c=2R\sin C$ 把所有边化为角的函数** ✓✓✓；" "\n"
        r"④ ⭐⭐ **锐角三角形的完整条件：三个角都 $<\frac\pi2$**，即 $B<\frac\pi2$、$C<\frac\pi2$（以及 $A<\frac\pi2$），**必须全部列出再取交集** ✓✓✓；" "\n"
        r"⑤ ⭐⭐ **$p\sin B+q\cos B$ 化辅助角：$\sqrt{p^2+q^2}\sin(B+\varphi)$，$\tan\varphi=\frac qp$**（本题 $p=3,q=\sqrt3$ ⟹ 振幅 $2\sqrt3$、$\varphi=\frac\pi6$）✓✓✓；" "\n"
        r"⑥ ⚠ **端点开闭要代回检验该点是否为锐角三角形** —— 本题右端 $B=\frac\pi3$ 是正三角形（锐角，闭），左端是直角三角形（开）✓✓✓"
    ),
    'difficulty': 0.90,
    'topics': ['M-T-221'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-221-E1',
}

T221_V1 = {
    'type': '解答',
    'stem_text': (
        r"在 $\triangle ABC$ 中，角 $A,B,C$ 的对边分别为 $a,b,c$，其中 $b=\sqrt3$，且 $(a-\sin C)\cos B=\sin B\cos C$．" "\n"
        r"(1) 求角 $B$ 的大小；" "\n"
        r"(2) 求 $\triangle ABC$ 周长的取值范围．"
    ),
    'opts': [],
    'answer': r"(1) $B=\dfrac\pi3$；(2) 周长的取值范围为 $\left(2\sqrt3,\ 3\sqrt3\right]$",
    'analysis': (
        r"(1) 展开后右端 $\sin C\cos B+\sin B\cos C=\sin(B+C)=\sin A$，得 $a\cos B=\sin A$，再用 $\frac a{\sin A}=\frac b{\sin B}$ 得 $\tan B=b$；"
        r"(2) 由余弦定理 $3=a^2+c^2-ac$ 与基本不等式定出 $ac$ 的范围，再算 $(a+c)^2=3+3ac$．"
    ),
    'solution': (
        r"**(1)** 由 $(a-\sin C)\cos B=\sin B\cos C$ 得 $a\cos B-\sin C\cos B=\sin B\cos C$，" "\n"
        r"即 $a\cos B=\sin C\cos B+\sin B\cos C=\sin(B+C)=\sin A$．" "\n"
        r"$\therefore\dfrac a{\sin A}=\dfrac1{\cos B}$（$\cos B\ne0$，否则 $\sin A=0$ 矛盾）．" "\n"
        r"又由正弦定理 $\dfrac a{\sin A}=\dfrac b{\sin B}$，且 $b=\sqrt3$，$\therefore\dfrac{\sqrt3}{\sin B}=\dfrac1{\cos B}$，" "\n"
        r"即 $\tan B=\dfrac{\sin B}{\cos B}=\sqrt3$．$\because B\in(0,\pi)$，$\therefore B=\dfrac\pi3$．" "\n"
        r"**(2)** 由 $B=\dfrac\pi3$、$b=\sqrt3$ 及余弦定理 $b^{2}=a^{2}+c^{2}-2ac\cos B$ 得" "\n"
        r"$3=a^{2}+c^{2}-ac$，即 $a^{2}+c^{2}=3+ac$．" "\n"
        r"由基本不等式 $a^{2}+c^{2}\ge 2ac$ 得 $3+ac\ge2ac$，$\therefore ac\le3$（当且仅当 $a=c=\sqrt3$ 时取等）；" "\n"
        r"又 $a>0,c>0$，$\therefore 0<ac\le3$．" "\n"
        r"于是 $(a+c)^{2}=a^{2}+c^{2}+2ac=3+3ac\in(3,12]$，$\therefore a+c\in\left(\sqrt3,2\sqrt3\right]$．" "\n"
        r"$\therefore$ 周长 $a+b+c\in\left(\sqrt3+\sqrt3,\ 2\sqrt3+\sqrt3\right]=\left(2\sqrt3,\ 3\sqrt3\right]$．"
    ),
    'review': (
        r"**① 本题题眼：$\sin C\cos B+\sin B\cos C=\sin(B+C)=\sin A$** —— 右边两项直接合成 ✓✓✓" "\n"
        r"② **$a\cos B=\sin A$ ⟹ $\frac a{\sin A}=\frac1{\cos B}$**：把「边/角」比与 $\cos B$ 联系起来，再与正弦定理的 $\frac b{\sin B}$ 对接 ✓✓✓" "\n"
        r"③ **$\tan B=b=\sqrt3$**：注意这里 $\tan B$ 直接等于边长 $b$ 的数值，**量纲上是巧合**（因为 $b=\sqrt3$ 而 $\frac a{\sin A}$ 是 $2R$）✓✓✓" "\n"
        r"（严格说由 $\frac a{\sin A}=\frac1{\cos B}$ 与 $\frac a{\sin A}=\frac b{\sin B}$ 得 $\frac b{\sin B}=\frac1{\cos B}$ ⟹ $\tan B=b$，只在 $b=\sqrt3$ 时如此）" "\n"
        r"④ **$ac\le3$ 的取等点 $a=c=\sqrt3$**：此时 $a^2+c^2-ac=3+3-3=3=b^2$ ✓ **是正三角形** ✓✓✓" "\n"
        r"⑤ **$ac>0$ 而非 $ac\ge0$**：三角形边长严格为正，故 $ac$ 只可趋近 $0$（退化），**左端开** ✓✓✓" "\n"
        r"⑥ **数值对拍**：" "\n"
        r"$a=c=\sqrt3$：周长 $=3\sqrt3=5.196$ ✓（上界，闭）" "\n"
        r"$a\to0$ 时 $c\to\sqrt3$（由 $3=a^2+c^2-ac$）：周长 $\to0+\sqrt3+\sqrt3=2\sqrt3=3.464$ ✓（下界，开）" "\n"
        r"$a=1$：$c^2-c-2=0$ ⟹ $c=2$，$ac=2$，$(a+c)^2=9$，$a+c=3$，周长 $=3+1.732=4.732\in(3.464,5.196]$ ✓✓✓" "\n"
        r"**答案 $(2\sqrt3,3\sqrt3]$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（已知一角及其对边 ⟹ 用余弦定理 + 基本不等式定范围）**：" "\n"
        r"① ⭐⭐ **已知 $B$ 与 $b$ ⟹ 余弦定理给出 $a,c$ 的一个二次约束 $b^2=a^2+c^2-2ac\cos B$**，这就是范围的来源 ✓✓✓；" "\n"
        r"② ⭐⭐ **配 $a^2+c^2\ge2ac$ 得 $ac$ 的上界；配 $a,c>0$ 得 $ac$ 的下界 $0$** ✓✓✓；" "\n"
        r"③ ⭐⭐ **求 $a+c$ 用 $(a+c)^2=a^2+c^2+2ac$**，把约束式中的 $a^2+c^2$ 换掉即可 ✓✓✓；" "\n"
        r"④ ⭐⭐ **取等条件必须代回原约束检验**（本题 $a=c$ 时确实是正三角形）✓✓✓；" "\n"
        r"⑤ ⚠ **退化情形（$a\to0$）对应开区间端点**：三角形要求边长严格为正，**「趋近」不等于「取到」** ✓✓✓；" "\n"
        r"⑥ ⚠ **$\cos B\ne0$ 要说明**：由 $a\cos B=\sin A$ 且 $\sin A>0$、$a>0$ 知 $\cos B>0$，不仅 $\ne0$，还可断定 $B$ 为锐角 ✓✓✓"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-221'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-221-V1',
}

T221_V2 = {
    'type': '解答',
    'stem_text': (
        r"在 $\triangle ABC$ 中，角 $A,B,C$ 所对的边分别为 $a,b,c$，且 $\sqrt3\,c=a\sin C-\sqrt3\,c\cos A$．" "\n"
        r"(1) 求 $A$；" "\n"
        r"(2) 若 $\triangle ABC$ 的面积 $S=\sqrt3$，求 $\triangle ABC$ 周长的最小值．"
    ),
    'opts': [],
    'answer': r"(1) $A=\dfrac{2\pi}3$；(2) 周长的最小值为 $4+2\sqrt3$",
    'analysis': (
        r"(1) 正弦定理化边为角，约去 $\sin C$ 得 $\sin A-\sqrt3\cos A=\sqrt3$，即 $2\sin(A-\frac\pi3)=\sqrt3$；"
        r"(2) 由 $S=\frac{\sqrt3}4bc=\sqrt3$ 得 $bc=4$，再用余弦定理把 $a$ 表成 $b+c$ 的函数，最后对周长函数判单调．"
    ),
    'solution': (
        r"**(1)** 由 $\sqrt3\,c=a\sin C-\sqrt3\,c\cos A$ 及正弦定理 $a=2R\sin A$、$c=2R\sin C$ 得" "\n"
        r"$\sqrt3\cdot 2R\sin C=2R\sin A\sin C-\sqrt3\cdot 2R\sin C\cos A$．" "\n"
        r"$\because\sin C>0$，两边同除以 $2R\sin C$ 得 $\sqrt3=\sin A-\sqrt3\cos A$．" "\n"
        r"$\therefore 2\left(\dfrac12\sin A-\dfrac{\sqrt3}2\cos A\right)=\sqrt3$，即 $2\sin\left(A-\dfrac\pi3\right)=\sqrt3$．" "\n"
        r"$\because A\in(0,\pi)$，$\therefore A-\dfrac\pi3\in\left(-\dfrac\pi3,\dfrac{2\pi}3\right)$．" "\n"
        r"由 $\sin\left(A-\dfrac\pi3\right)=\dfrac{\sqrt3}2$ 得 $A-\dfrac\pi3=\dfrac\pi3$ 或 $\dfrac{2\pi}3$，" "\n"
        r"即 $A=\dfrac{2\pi}3$ 或 $A=\pi$（舍去）．$\therefore A=\dfrac{2\pi}3$．" "\n"
        r"**(2)** $S=\dfrac12bc\sin A=\dfrac12bc\cdot\dfrac{\sqrt3}2=\dfrac{\sqrt3}4bc=\sqrt3$，$\therefore bc=4$．" "\n"
        r"由余弦定理 $a^{2}=b^{2}+c^{2}-2bc\cos\dfrac{2\pi}3=b^{2}+c^{2}+bc=(b+c)^{2}-bc=(b+c)^{2}-4$．" "\n"
        r"设 $s=b+c$，则 $a=\sqrt{s^{2}-4}$，周长 $L=a+b+c=\sqrt{s^{2}-4}+s$．" "\n"
        r"由基本不等式 $s=b+c\ge2\sqrt{bc}=4$（当且仅当 $b=c=2$ 时取等）．" "\n"
        r"$\because L'(s)=1+\dfrac{s}{\sqrt{s^{2}-4}}>0$（$s>2$），$\therefore L$ 在 $[4,+\infty)$ 上单调递增，" "\n"
        r"$L_{\min}=L(4)=\sqrt{16-4}+4=2\sqrt3+4$．" "\n"
        r"$\therefore\triangle ABC$ 周长的最小值为 $4+2\sqrt3$．"
    ),
    'review': (
        r"**⚠ 本题原书 `solution` 为空，以下推导由我独立完成并用答案验证**" "\n"
        r"**① 约去 $2R\sin C$ 需要 $\sin C\ne0$**（$C\in(0,\pi)$ 保证）✓✓✓" "\n"
        r"② **辅助角的方向**：$\sin A-\sqrt3\cos A=2(\frac12\sin A-\frac{\sqrt3}2\cos A)=2\sin(A-\frac\pi3)$ ✓✓✓" "\n"
        r"（**注意是 $A-\frac\pi3$ 不是 $A+\frac\pi3$**，因为 $\cos$ 项系数为负）" "\n"
        r"③ **两根要检验**：$A-\frac\pi3=\frac\pi3$ ⟹ $A=\frac{2\pi}3$ ✓；$A-\frac\pi3=\frac{2\pi}3$ ⟹ $A=\pi$ ✗（退化，舍）✓✓✓" "\n"
        r"（**这是本题唯一会丢分的地方** —— 若只写 $\frac{2\pi}3$ 而不说明舍去 $\pi$，过程不完整）" "\n"
        r"④ **$A=\frac{2\pi}3$ 是钝角 ⟹ $\cos A=-\frac12$**，于是余弦定理中 $-2bc\cos A=+bc$ ✓✓✓" "\n"
        r"⑤ **关键换元：$a^2=(b+c)^2-bc=(b+c)^2-4$** —— 因为 $bc=4$ 已定，**$a$ 只依赖 $s=b+c$** ✓✓✓" "\n"
        r"⑥ **$L(s)=s+\sqrt{s^2-4}$ 单调递增**：导数 $1+\frac s{\sqrt{s^2-4}}>0$ ✓（也可直接看：$s$ 增大时两项都增大）" "\n"
        r"⑦ **数值对拍**：$b=c=2$ ⟹ $bc=4$ ✓；$a^2=16-4=12$ ⟹ $a=2\sqrt3=3.464$；" "\n"
        r"周长 $=2+2+3.464=7.464$，而 $4+2\sqrt3=4+3.464=7.464$ ✓✓✓ **完全吻合**" "\n"
        r"另取 $b=1,c=4$（$bc=4$）：$a^2=25-4=21$ ⟹ $a=4.583$，周长 $=9.583>7.464$ ✓ **确是最小值**" "\n"
        r"**答案 $\frac{2\pi}3$ 与 $4+2\sqrt3$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（面积定值 + 求周长最值 ⟹ 单变量化）**：" "\n"
        r"① ⭐⭐ **$S$ 与 $A$ 都已知 ⟹ $bc$ 立即确定**：$S=\frac12bc\sin A$ ⟹ $bc=\frac{2S}{\sin A}$ ✓✓✓；" "\n"
        r"② ⭐⭐ **余弦定理改写成 $a^2=(b+c)^2-2bc(1+\cos A)$ 的形式**，这样 $a$ 只含 $b+c$ 与已知的 $bc$ ✓✓✓；" "\n"
        r"（本题 $\cos A=-\frac12$ ⟹ $2bc(1+\cos A)=bc$，故 $a^2=(b+c)^2-bc$）" "\n"
        r"③ ⭐⭐ **令 $s=b+c$，则 $s\ge2\sqrt{bc}$（下界已知），且周长 $=s+\sqrt{s^2-\text{常数}}$ 单调增** ⟹ **最值在 $b=c$ 时取到** ✓✓✓；" "\n"
        r"④ ⭐⭐ **「面积定 + 夹角定」型最值，极值几乎总在 $b=c$（等腰）处** —— 可作为快速预判 ✓✓✓；" "\n"
        r"⑤ ⚠ **辅助角的符号**：$\sin A-\sqrt3\cos A=2\sin(A-\frac\pi3)$ 而 $\sin A+\sqrt3\cos A=2\sin(A+\frac\pi3)$，**符号不同结果完全不同** ✓✓✓；" "\n"
        r"⑥ ⚠ **$\sin\theta=k$ 在 $(-\frac\pi3,\frac{2\pi}3)$ 内可能两解，务必逐个人代回检验是否为合法内角** ✓✓✓"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-221'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-221-V2',
}

T221_V3 = {
    'type': '解答',
    'stem_text': (
        r"在① $\dfrac a{\cos A}=\dfrac{b+c}{\cos B+\cos C}$，② 向量 $\vec m=(a+c,b)$ 与 $\vec n=(c-a,b-c)$，且 $\vec m\perp\vec n$，③ $\dfrac a{\cos A}=\dfrac{\sqrt3\,b}{\sin B}$，" "\n"
        r"三个条件中选一个填在下面试题的横线上，并加以解析．" "\n"
        r"在 $\triangle ABC$ 中，内角 $A,B,C$ 所对的边分别为 $a,b,c$，已知 ____．" "\n"
        r"(1) 求角 $A$ 的大小；" "\n"
        r"(2) 若 $\triangle ABC$ 的面积为 $\dfrac18abc$，求 $\triangle ABC$ 周长的取值范围．"
    ),
    'opts': [],
    'answer': r"(1) $A=\dfrac\pi3$；(2) 周长的取值范围为 $\left(4\sqrt3,\ 6\sqrt3\right]$",
    'analysis': (
        r"(1) 选①用正弦定理后交叉相乘配两角和差的正弦；选②由 $\vec m\cdot\vec n=0$ 得 $b^2+c^2-a^2=bc$；选③直接得 $\tan A=\sqrt3$；"
        r"(2) 由 $S=\frac12bc\sin A=\frac18abc$ 定出 $a=4\sin A=2\sqrt3$，再用余弦定理配基本不等式定 $b+c$ 的范围．"
    ),
    'solution': (
        r"**(1)** 三个条件都给出 $A=\dfrac\pi3$．" "\n"
        r"**选①**：由正弦定理 $\dfrac a{\cos A}=\dfrac{b+c}{\cos B+\cos C}$ 化为 $\dfrac{\sin A}{\cos A}=\dfrac{\sin B+\sin C}{\cos B+\cos C}$，" "\n"
        r"交叉相乘：$\sin A\cos B+\sin A\cos C=\sin B\cos A+\sin C\cos A$，" "\n"
        r"移项：$\sin A\cos B-\sin B\cos A=\sin C\cos A-\sin A\cos C$，" "\n"
        r"即 $\sin(A-B)=\sin(C-A)$．" "\n"
        r"$\because A,B,C\in(0,\pi)$，且 $A-B,\ C-A\in(-\pi,\pi)$，只可能 $A-B=C-A$，" "\n"
        r"$\therefore 2A=B+C=\pi-A$，$3A=\pi$，$A=\dfrac\pi3$．" "\n"
        r"**选②**：由 $\vec m\perp\vec n$ 得 $\vec m\cdot\vec n=(a+c)(c-a)+b(b-c)=c^{2}-a^{2}+b^{2}-bc=0$，" "\n"
        r"即 $b^{2}+c^{2}-a^{2}=bc$，$\therefore\cos A=\dfrac{b^{2}+c^{2}-a^{2}}{2bc}=\dfrac12$，$A=\dfrac\pi3$．" "\n"
        r"**选③**：由正弦定理 $\dfrac a{\cos A}=\dfrac{\sqrt3\,b}{\sin B}$ 化为 $\dfrac{\sin A}{\cos A}=\dfrac{\sqrt3\sin B}{\sin B}=\sqrt3$，" "\n"
        r"即 $\tan A=\sqrt3$．$\because A\in(0,\pi)$，$\therefore A=\dfrac\pi3$．" "\n"
        r"**(2)** $S=\dfrac12bc\sin A=\dfrac18abc$，$\therefore a=4\sin A=4\cdot\dfrac{\sqrt3}2=2\sqrt3$．" "\n"
        r"由三角形两边之和大于第三边：$b+c>a=2\sqrt3$，$\therefore$ 周长 $a+b+c>2a=4\sqrt3$（**开区间**）．" "\n"
        r"另一方面，由余弦定理 $a^{2}=b^{2}+c^{2}-2bc\cos\dfrac\pi3=b^{2}+c^{2}-bc$，即 $12=(b+c)^{2}-3bc$．" "\n"
        r"由基本不等式 $bc\le\dfrac{(b+c)^{2}}4$ 得 $12=(b+c)^{2}-3bc\ge(b+c)^{2}-\dfrac{3(b+c)^{2}}4=\dfrac{(b+c)^{2}}4$，" "\n"
        r"$\therefore(b+c)^{2}\le48$，即 $b+c\le4\sqrt3$（当且仅当 $b=c=2\sqrt3$ 时取等）．" "\n"
        r"$\therefore$ 周长 $a+b+c\le2\sqrt3+4\sqrt3=6\sqrt3$（**闭区间**）．" "\n"
        r"综上，周长的取值范围是 $\left(4\sqrt3,\ 6\sqrt3\right]$．"
    ),
    'review': (
        r"**① 选①的技巧：交叉相乘后**「同侧交叉项相减」**配出 $\sin(A-B)=\sin(C-A)$** ✓✓✓" "\n"
        r"（若只是把 $\sin A\cos B$ 与 $\sin B\cos A$ 放一起，不易看出）" "\n"
        r"② **$\sin(A-B)=\sin(C-A)$ ⟹ $A-B=C-A$**：因 $A-B$ 与 $C-A$ 都在 $(-\pi,\pi)$，" "\n"
        r"由 $\sin X=\sin Y$ 得 $X=Y$ 或 $X+Y=\pi$；后者 $(A-B)+(C-A)=C-B=\pi$ 不可能（$B,C\in(0,\pi)$）✓✓✓" "\n"
        r"③ **选②的展开**：$(a+c)(c-a)=c^2-a^2$（平方差），加 $b(b-c)$ 得 $b^2+c^2-a^2-bc=0$ ✓✓✓" "\n"
        r"④ **$S=\frac18abc$ 的用法**：与 $S=\frac12bc\sin A$ 对比，**约去 $bc$ 得 $a=4\sin A$** ✓✓✓ —— 这一步很漂亮，" "\n"
        r"它把「面积条件」直接变成了「边长 $a$ 已知」" "\n"
        r"⑤ **两个方向的界来源不同**：" "\n"
        r"**下界来自三角形两边和大于第三边**（$b+c>a$）⟹ 严格不等 ⟹ **开** ✓✓✓" "\n"
        r"**上界来自余弦定理 + 基本不等式**（$bc\le\frac{(b+c)^2}4$）⟹ 可取等（$b=c$）⟹ **闭** ✓✓✓" "\n"
        r"⑥ **取等检验**：$b=c=2\sqrt3$ 时 $a^2=12+12-12=12$ ⟹ $a=2\sqrt3$ ✓ 三边为 $2\sqrt3,2\sqrt3,2\sqrt3$？" "\n"
        r"不对：$b=c=2\sqrt3$，$a^2=b^2+c^2-bc=12+12-12=12$ ⟹ $a=2\sqrt3$ ✓ **是正三角形**，周长 $=6\sqrt3$ ✓✓✓" "\n"
        r"（**正三角形的 $b+c=4\sqrt3$、$a=2\sqrt3$，满足 $b+c>a$**，故上界可达）" "\n"
        r"⑦ **数值对拍**：$4\sqrt3=6.928$、$6\sqrt3=10.392$。" "\n"
        r"退化工况 $b+c\to2\sqrt3=3.464$：周长 $\to 3.464+3.464=6.928$ ✓（开）" "\n"
        r"$b=c=2\sqrt3$：周长 $=10.392$ ✓（闭）" "\n"
        r"**答案 $(4\sqrt3,6\sqrt3]$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（面积 = $k\cdot abc$ 型条件）**：" "\n"
        r"① ⭐⭐ **$S=k\,abc$ 与 $S=\frac12bc\sin A$ 对比 ⟹ 约去 $bc$ ⟹ $a=\frac{\sin A}{2k}$** —— 面积条件**直接给出边长 $a$** ✓✓✓；" "\n"
        r"② ⭐⭐ **两边和的范围：下界用 $b+c>a$（三角形不等式，开）；上界用余弦定理 + $bc\le\frac{(b+c)^2}4$（闭）** ✓✓✓；" "\n"
        r"③ ⭐⭐ **$\sin X=\sin Y$ 的处理：$X=Y$ 或 $X+Y=\pi$，必须逐一检验可行性** ✓✓✓；" "\n"
        r"④ ⭐⭐ **向量垂直（$\vec m\cdot\vec n=0$）常用来给出边的二次关系**，展开后往往恰是余弦定理的分子 ✓✓✓；" "\n"
        r"⑤ ⚠ **上下界开闭不同是常态**：下界来自「严格不等式」（三角形不等式），上界来自「可取等的不等式」（基本不等式）✓✓✓"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-221'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-221-V3',
}

T222_E1 = {
    'type': '解答',
    'stem_text': (
        r"在① $b\cos\left(\dfrac\pi2-C\right)=\sqrt3\,c\cos B$；② $2S_{\triangle ABC}=\sqrt3\,\vec{BA}\cdot\vec{BC}$；③ $\tan A+\tan C+\sqrt3=\sqrt3\tan A\tan C$．" "\n"
        r"这三个条件中任选一个，补充在下面的问题中，并进行解答．" "\n"
        r"问题：在 $\triangle ABC$ 中，内角 $A,B,C$ 的对边分别为 $a,b,c$，且 ____．" "\n"
        r"(1) 求角 $B$；" "\n"
        r"(2) 若 $\triangle ABC$ 是锐角三角形，且 $c=4$，求 $a$ 的取值范围．" "\n"
        r"注：如果选择多个条件分别解答，按第一个解答计分．"
    ),
    'opts': [],
    'answer': r"(1) 答案见解析，$B=\dfrac\pi3$；(2) $a$ 的取值范围为 $(2,8)$",
    'analysis': (
        r"(1) 选①用诱导公式 $\cos(\frac\pi2-C)=\sin C$ 配正弦定理；选②把面积与数量积都写成 $ac$ 的表达式；选③移项后配正切的和角公式；"
        r"(2) 由正弦定理把 $a$ 表成 $\cot C$ 的函数，再由锐角条件定 $C$ 的范围．"
    ),
    'solution': (
        r"**(1)** 三个条件都给出 $B=\dfrac\pi3$．" "\n"
        r"**选①**：$\cos\left(\dfrac\pi2-C\right)=\sin C$，条件即 $b\sin C=\sqrt3\,c\cos B$．" "\n"
        r"由正弦定理得 $\sin B\sin C=\sqrt3\sin C\cos B$．" "\n"
        r"$\because C\in(0,\pi)$，$\sin C\ne0$，$\therefore\sin B=\sqrt3\cos B$，且 $\cos B\ne0$（否则 $\sin B=0$ 矛盾），" "\n"
        r"$\therefore\tan B=\sqrt3$，$B=\dfrac\pi3$．" "\n"
        r"**选②**：$2S_{\triangle ABC}=2\cdot\dfrac12ac\sin B=ac\sin B$，$\vec{BA}\cdot\vec{BC}=ca\cos B$，" "\n"
        r"条件即 $ac\sin B=\sqrt3\,ca\cos B$，即 $\sin B=\sqrt3\cos B$，$\therefore\tan B=\sqrt3$，$B=\dfrac\pi3$．" "\n"
        r"**选③**：条件即 $\tan A+\tan C=\sqrt3(\tan A\tan C-1)$，$\therefore\dfrac{\tan A+\tan C}{1-\tan A\tan C}=-\sqrt3$．" "\n"
        r"由正切的和角公式 $\tan(A+C)=\dfrac{\tan A+\tan C}{1-\tan A\tan C}=-\sqrt3$，" "\n"
        r"$\therefore\tan B=-\tan(A+C)=\sqrt3$，$\because B\in(0,\pi)$，$\therefore B=\dfrac\pi3$．" "\n"
        r"**(2)** 由 $B=\dfrac\pi3$ 得 $A=\pi-B-C=\dfrac{2\pi}3-C$．" "\n"
        r"由正弦定理 $a=\dfrac{c\sin A}{\sin C}=\dfrac{4\sin\left(\frac{2\pi}3-C\right)}{\sin C}$" "\n"
        r"$=\dfrac{4\left(\frac{\sqrt3}2\cos C+\frac12\sin C\right)}{\sin C}=2\sqrt3\cot C+2$．" "\n"
        r"$\because\triangle ABC$ 是锐角三角形，$\therefore\begin{cases}0<C<\dfrac\pi2\\[2pt]0<A=\dfrac{2\pi}3-C<\dfrac\pi2\end{cases}$，解得 $\dfrac\pi6<C<\dfrac\pi2$．" "\n"
        r"$\therefore\tan C>\dfrac{\sqrt3}3$，$\cot C\in(0,\sqrt3)$，" "\n"
        r"$\therefore a=2\sqrt3\cot C+2\in(2,\ 2\sqrt3\cdot\sqrt3+2)=(2,8)$．"
    ),
    'review': (
        r"**① 选①的核心是诱导公式 $\cos(\frac\pi2-C)=\sin C$**，配正弦定理约去 $\sin C$ 即得 $\tan B$ ✓✓✓" "\n"
        r"② **选②的核心是两个面积式**：$2S=ac\sin B$、$\vec{BA}\cdot\vec{BC}=ac\cos B$（注意 $\vec{BA}$ 与 $\vec{BC}$ 的夹角就是 $B$）✓✓✓" "\n"
        r"（**$\vec{BA}\cdot\vec{BC}=|\vec{BA}||\vec{BC}|\cos B=ca\cos B$**，夹角为 $B$ 不是 $\pi-B$，因为两向量都以 $B$ 为起点）" "\n"
        r"③ **选③的核心：$\tan(A+C)=\frac{\tan A+\tan C}{1-\tan A\tan C}$**，且 $\tan B=-\tan(A+C)$ ✓✓✓" "\n"
        r"（注意 $\tan(A+C)=\tan(\pi-B)=-\tan B$，故 $\tan B=-\tan(A+C)$）" "\n"
        r"④ **$a=2\sqrt3\cot C+2$ 的推导**：$\sin(\frac{2\pi}3-C)=\sin\frac{2\pi}3\cos C-\cos\frac{2\pi}3\sin C=\frac{\sqrt3}2\cos C+\frac12\sin C$ ✓✓✓" "\n"
        r"⑤ **锐角条件定 $C\in(\frac\pi6,\frac\pi2)$**：$C<\frac\pi2$ 且 $A=\frac{2\pi}3-C<\frac\pi2$ ⟹ $C>\frac\pi6$ ✓✓✓" "\n"
        r"（**若漏掉 $A<\frac\pi2$ 会得 $C\in(0,\frac\pi2)$，从而 $a\in(2,+\infty)$，全错**）" "\n"
        r"⑥ **两端都是开区间**：$C\to\frac\pi2$ 时 $\cot C\to0$ ⟹ $a\to2$（但 $C=\frac\pi2$ 非锐角）；" "\n"
        r"$C\to\frac\pi6$ 时 $\cot C\to\sqrt3$ ⟹ $a\to8$（但 $C=\frac\pi6$ 时 $A=\frac\pi2$，非锐角）✓✓✓" "\n"
        r"⑦ **数值对拍**：取 $C=\frac\pi3$（正三角形）：$\cot\frac\pi3=\frac{\sqrt3}3$，$a=2\sqrt3\cdot\frac{\sqrt3}3+2=2+2=4$ ✓（此时 $c=4$、$a=4$ 确实相等）" "\n"
        r"取 $C=80^\circ$：$\cot80^\circ=0.1763$，$a=2\times1.732\times0.1763+2=2.611\in(2,8)$ ✓✓✓" "\n"
        r"**答案 $(2,8)$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（已知一角 + 一边 ⟹ 把所求边表成 $\cot$ 的函数）**：" "\n"
        r"① ⭐⭐ **已知 $B$ 与 $c$，求 $a$：用正弦定理 $a=\frac{c\sin A}{\sin C}$ 且 $A=\pi-B-C$，化成 $C$ 的函数** ✓✓✓；" "\n"
        r"② ⭐⭐ **$\sin(\alpha-C)$ 展开后除以 $\sin C$ ⟹ 出现 $\cot C$**，于是问题变成「$\cot C$ 的范围」✓✓✓；" "\n"
        r"③ ⭐⭐ **锐角三角形的三个不等式必须列全**：$A<\frac\pi2$、$B<\frac\pi2$、$C<\frac\pi2$，**已知角是否满足要单独确认** ✓✓✓；" "\n"
        r"④ ⭐⭐ **三个「诱导/和角」高频式：$\cos(\frac\pi2-C)=\sin C$、$\tan(A+C)=-\tan B$、$\sin(A+C)=\sin B$** ✓✓✓；" "\n"
        r"⑤ ⭐⭐ **$\vec{BA}\cdot\vec{BC}=ac\cos B$ 而 $\vec{AB}\cdot\vec{AC}=bc\cos A$** —— 「公共起点的两向量」夹角就是该顶点的角 ✓✓✓；" "\n"
        r"⑥ ⚠ **答案两端是否取到，取决于该处三角形是否仍为锐角** —— 本题两端分别对应 $C=\frac\pi2$ 与 $A=\frac\pi2$，均非锐角 ⟹ **双开** ✓✓✓"
    ),
    'difficulty': 0.90,
    'topics': ['M-T-222'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-222-E1',
}

T222_V1 = {
    'type': '解答',
    'stem_text': (
        r"在 $\triangle ABC$ 中，$a,b,c$ 分别是角 $A,B,C$ 的对边，且 $2a\cos C-b\cos C=c\cos B$．" "\n"
        r"(1) 求角 $C$；" "\n"
        r"(2) 若 $a+b=2$，求 $c$ 的取值范围．"
    ),
    'opts': [],
    'answer': r"(1) $C=\dfrac\pi3$；(2) $c$ 的取值范围为 $[1,2)$",
    'analysis': (
        r"(1) 正弦定理化边为角后，右边 $\sin B\cos C+\sin C\cos B=\sin(B+C)=\sin A$，约去 $\sin A$ 得 $\cos C$；"
        r"(2) 由余弦定理把 $c^2$ 写成关于 $a$ 的二次函数，配方法求值域．"
    ),
    'solution': (
        r"**(1)** 由 $2a\cos C-b\cos C=c\cos B$ 及正弦定理得 $2\sin A\cos C-\sin B\cos C=\sin C\cos B$，" "\n"
        r"即 $2\sin A\cos C=\sin B\cos C+\sin C\cos B=\sin(B+C)$．" "\n"
        r"$\because B+C=\pi-A$，$\therefore\sin(B+C)=\sin A$．" "\n"
        r"于是 $2\sin A\cos C=\sin A$．$\because A\in(0,\pi)$，$\sin A\ne0$，$\therefore\cos C=\dfrac12$．" "\n"
        r"又 $C\in(0,\pi)$，$\therefore C=\dfrac\pi3$．" "\n"
        r"**(2)** 由 $a+b=2$ 得 $b=2-a$，且 $0<a<2$．" "\n"
        r"由余弦定理及 $C=\dfrac\pi3$：" "\n"
        r"$c^{2}=a^{2}+b^{2}-2ab\cos\dfrac\pi3=a^{2}+(2-a)^{2}-a(2-a)$" "\n"
        r"$=a^{2}+4-4a+a^{2}-2a+a^{2}=3a^{2}-6a+4=3(a-1)^{2}+1$．" "\n"
        r"$\because 0<a<2$，$\therefore a-1\in(-1,1)$，$(a-1)^{2}\in[0,1)$，" "\n"
        r"$\therefore c^{2}\in[1,4)$，即 $1\le c<2$．" "\n"
        r"（当 $a=1$ 时 $b=1$，$c=1$，为等边三角形，下界可取）" "\n"
        r"$\therefore c$ 的取值范围为 $[1,2)$．"
    ),
    'review': (
        r"**① $\sin B\cos C+\sin C\cos B=\sin(B+C)=\sin A$** —— 与前面多题同一手法 ✓✓✓" "\n"
        r"② **$2\sin A\cos C=\sin A$ ⟹ $\cos C=\frac12$**，关键是约去 $\sin A\ne0$ ✓✓✓" "\n"
        r"③ **$c^2=3(a-1)^2+1$ 的配方要仔细**：" "\n"
        r"$a^2+(2-a)^2-a(2-a)=a^2+(4-4a+a^2)-(2a-a^2)=a^2+4-4a+a^2-2a+a^2=3a^2-6a+4$ ✓✓✓" "\n"
        r"（**交叉项 $-2ab\cos\frac\pi3=-ab$**，不要漏）" "\n"
        r"④ **$a-1\in(-1,1)$ ⟹ $(a-1)^2\in[0,1)$**：左端 $0$ 可取（$a=1$），右端 $1$ 不可取（$a\to0$ 或 $a\to2$ 时退化）✓✓✓" "\n"
        r"⑤ **$c^2\in[1,4)$ ⟹ $c\in[1,2)$**（$c>0$，开方保序）✓✓✓" "\n"
        r"⑥ **数值对拍**：" "\n"
        r"$a=b=1$：$c^2=1+1-1=1$ ⟹ $c=1$ ✓（下界，闭，等边三角形）" "\n"
        r"$a=0.5,b=1.5$：$c^2=0.25+2.25-0.75=1.75$ ⟹ $c=1.323\in[1,2)$ ✓" "\n"
        r"$a\to0,b\to2$：$c^2\to4$ ⟹ $c\to2$ ✓（上界，开，退化）" "\n"
        r"**答案 $[1,2)$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（两边和定 ⟹ 第三边范围）**：" "\n"
        r"① ⭐⭐ **$a+b$ 为定值 ⟹ 令 $b=s-a$，把 $c^2$ 化为 $a$ 的二次函数，配方法求值域** ✓✓✓；" "\n"
        r"② ⭐⭐ **$c^2=(a+b)^2-2ab(1+\cos C)$ 是更快的写法**：本题 $(a+b)^2=4$、$2(1+\frac12)=3$ ⟹ $c^2=4-3ab$，" "\n"
        r"由 $ab\in(0,1]$ 得 $c^2\in[1,4)$ ✓✓✓ **与配方法一致，且省一半计算**；" "\n"
        r"③ ⭐⭐ **$ab$ 的范围由 $a+b=s$ 与基本不等式给出：$0<ab\le\frac{s^2}4$**，上界在 $a=b$ 取到 ✓✓✓；" "\n"
        r"④ ⭐⭐ **$c$ 的范围要对 $c^2$ 开方，且 $c>0$ 保序** ✓✓✓；" "\n"
        r"⑤ ⚠ **退化端点（$a\to0$ 或 $b\to0$）对应开区间**，而 $a=b$ 对应闭区间 ✓✓✓"
    ),
    'difficulty': 0.82,
    'topics': ['M-T-222'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-222-V1',
}

T222_V2 = {
    'type': '解答',
    'stem_text': (
        r"在 $\triangle ABC$ 中，角 $A,B,C$ 所对应的边分别为 $a,b,c$，$a-b=b\cos C$．" "\n"
        r"(1) 求证：$\sin C=\tan B$；" "\n"
        r"(2) 若 $a=1$，$C$ 为锐角，求 $c$ 的取值范围．"
    ),
    'opts': [],
    'answer': r"(1) 证明见解析；(2) $c$ 的取值范围为 $\left(\dfrac12,\ \sqrt2\right)$",
    'analysis': (
        r"(1) 正弦定理化边为角后用 $\sin A=\sin(B+C)$ 展开，抵消 $\sin B\cos C$ 即得；(2) 由条件解出 $b=\frac a{1+\cos C}$，"
        r"再把 $c^2$ 表成 $b$ 的函数，由 $b$ 的范围定值域．"
    ),
    'solution': (
        r"**(1)** 由 $a-b=b\cos C$ 及正弦定理得 $\sin A-\sin B=\sin B\cos C$．" "\n"
        r"$\because\sin A=\sin(B+C)=\sin B\cos C+\cos B\sin C$，代入得" "\n"
        r"$\sin B\cos C+\cos B\sin C-\sin B=\sin B\cos C$，" "\n"
        r"$\therefore\cos B\sin C=\sin B$．" "\n"
        r"$\because\sin B>0$，$\therefore\cos B>0$，即 $B$ 为锐角，可同除以 $\cos B$：" "\n"
        r"$\sin C=\dfrac{\sin B}{\cos B}=\tan B$．证毕．" "\n"
        r"**(2)** 由 $a-b=b\cos C$ 得 $b(1+\cos C)=a=1$，$\therefore b=\dfrac1{1+\cos C}$．" "\n"
        r"$\because C$ 为锐角，$\therefore 0<\cos C<1$，$\therefore\dfrac12<b<1$．" "\n"
        r"又由余弦定理及 $\cos C=\dfrac{a-b}b=\dfrac1b-1$：" "\n"
        r"$c^{2}=a^{2}+b^{2}-2ab\cos C=1+b^{2}-2b\left(\dfrac1b-1\right)=1+b^{2}-2+2b=b^{2}+2b-1$．" "\n"
        r"设 $f(b)=b^{2}+2b-1$，则 $f'(b)=2b+2>0$（$b>\frac12$），$\therefore f$ 在 $\left(\dfrac12,1\right)$ 上**单调递增**，" "\n"
        r"$f\left(\dfrac12\right)=\dfrac14+1-1=\dfrac14$，$f(1)=1+2-1=2$，" "\n"
        r"$\therefore c^{2}\in\left(\dfrac14,2\right)$，即 $c\in\left(\dfrac12,\ \sqrt2\right)$．"
    ),
    'review': (
        r"**① (1) 的核心是 $\sin A=\sin(B+C)$ 展开后与右边 $\sin B\cos C$ 抵消** ✓✓✓" "\n"
        r"② **$\cos B\sin C=\sin B$ ⟹ $\sin C=\frac{\sin B}{\cos B}$** 需要 $\cos B\ne0$；" "\n"
        r"由 $\sin B>0$ 且 $\cos B\sin C=\sin B$ 知 $\cos B>0$（因 $\sin C>0$），故 $B$ 为锐角 ✓✓✓" "\n"
        r"③ **(2) 的关键变形：$\cos C=\frac{a-b}b=\frac1b-1$** —— 由原条件解出 $\cos C$ 用 $b$ 表示，代回余弦定理 ✓✓✓" "\n"
        r"（**这样就不用引入 $C$ 做中间变量**，计算量大减）" "\n"
        r"④ **$c^2=b^2+2b-1$ 的化简**：$1+b^2-2b(\frac1b-1)=1+b^2-2+2b=b^2+2b-1$ ✓✓✓" "\n"
        r"⑤ ⚠ **原书详解写「$f(b)=b^2+2b-1$ 在 $(\frac12,1)$ 上单调递减」，这是笔误**：" "\n"
        r"$f'(b)=2b+2>0$，$f$ 在 $(\frac12,1)$ 上**递增**，故 $f(\frac12)=\frac14$ 是下界、$f(1)=2$ 是上界。" "\n"
        r"（**结论 $c^2\in(\frac14,2)$ 与原书一致**，只是单调性的描述写反了）" "\n"
        r"⑥ **数值对拍**：" "\n"
        r"$b\to\frac12$（$C\to0$）：$c^2\to\frac14$ ⟹ $c\to\frac12$ ✓（开，$C$ 为锐角不含 $0$）" "\n"
        r"$b\to1$（$C\to\frac\pi2$）：$c^2\to2$ ⟹ $c\to\sqrt2=1.414$ ✓（开，$C$ 为锐角不含 $\frac\pi2$）" "\n"
        r"$b=0.8$：$\cos C=\frac1{0.8}-1=0.25$，$C=75.5^\circ$ 锐角 ✓；$c^2=0.64+1.6-1=1.24$ ⟹ $c=1.114\in(0.5,1.414)$ ✓✓✓" "\n"
        r"**答案 $(\frac12,\sqrt2)$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（条件形如「边 = 边 × cos」⟹ 解出 $\cos$）**：" "\n"
        r"① ⭐⭐ **$a-b=b\cos C$ ⟹ $\cos C=\frac{a-b}b$，直接代回余弦定理消去角变量** ✓✓✓ —— 本题最省力的做法；" "\n"
        r"② ⭐⭐ **同一条件有两种用法：(1) 用它证角的关系（正弦定理）；(2) 用它解出 $\cos C$（代数变形）** ✓✓✓；" "\n"
        r"③ ⭐⭐ **$\cos B\sin C=\sin B$ 型等式 ⟹ 同除以 $\cos B$ 得 $\sin C=\tan B$**，**先由符号确认 $\cos B>0$** ✓✓✓；" "\n"
        r"④ ⭐⭐ **「$C$ 为锐角」⟹ $\cos C\in(0,1)$ ⟹ $b=\frac1{1+\cos C}\in(\frac12,1)$** —— 把角的条件翻译成变量范围 ✓✓✓；" "\n"
        r"⑤ ⚠ **单调性描述要与导数一致**，原书此处笔误为「递减」，实为递增（$f'=2b+2>0$）✓✓✓"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-222'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-222-V2',
}

T222_V3 = {
    'type': '解答',
    'stem_text': (
        r"设函数 $f(x)=\cos\left(2x+\dfrac{2\pi}3\right)+2\cos^{2}x$．" "\n"
        r"(1) 求 $f(x)$ 的最大值，并写出使 $f(x)$ 取最大值时 $x$ 的集合；" "\n"
        r"(2) 已知 $\triangle ABC$ 中，角 $A,B,C$ 的对边分别为 $a,b,c$，若 $f(A)=\dfrac32$，$b+c=2$，求 $a$ 的最小值．"
    ),
    'opts': [],
    'answer': r"(1) 最大值为 $2$，此时 $x$ 的集合为 $\left\{x\ \middle|\ x=k\pi-\dfrac\pi6,\ k\in\mathbb Z\right\}$；(2) $a$ 的最小值为 $\sqrt3$",
    'analysis': (
        r"(1) 用两角和的余弦展开 $\cos(2x+\frac{2\pi}3)$，再用 $2\cos^2x=1+\cos2x$ 统一成关于 $2x$ 的式子，配成辅助角；"
        r"(2) 由 $f(A)=\frac32$ 解出 $A=\frac{2\pi}3$，再用余弦定理把 $a^2$ 表成 $(b+c)$ 与 $bc$ 的式子，配基本不等式．"
    ),
    'solution': (
        r"**(1)** $\cos\left(2x+\dfrac{2\pi}3\right)=\cos 2x\cos\dfrac{2\pi}3-\sin 2x\sin\dfrac{2\pi}3=-\dfrac12\cos 2x-\dfrac{\sqrt3}2\sin 2x$，" "\n"
        r"又 $2\cos^{2}x=1+\cos 2x$，于是" "\n"
        r"$f(x)=-\dfrac12\cos 2x-\dfrac{\sqrt3}2\sin 2x+1+\cos 2x=\dfrac12\cos 2x-\dfrac{\sqrt3}2\sin 2x+1$" "\n"
        r"$=\cos\left(2x+\dfrac\pi3\right)+1$．" "\n"
        r"$\because -1\le\cos\left(2x+\dfrac\pi3\right)\le1$，$\therefore f(x)_{\max}=2$，" "\n"
        r"当且仅当 $\cos\left(2x+\dfrac\pi3\right)=1$，即 $2x+\dfrac\pi3=2k\pi\ (k\in\mathbb Z)$，" "\n"
        r"$\therefore x=k\pi-\dfrac\pi6\ (k\in\mathbb Z)$．" "\n"
        r"即使 $f(x)$ 取最大值的 $x$ 的集合为 $\left\{x\ \middle|\ x=k\pi-\dfrac\pi6,\ k\in\mathbb Z\right\}$．" "\n"
        r"**(2)** $f(A)=\cos\left(2A+\dfrac\pi3\right)+1=\dfrac32$，$\therefore\cos\left(2A+\dfrac\pi3\right)=\dfrac12$．" "\n"
        r"$\because A\in(0,\pi)$，$\therefore 2A+\dfrac\pi3\in\left(\dfrac\pi3,\dfrac{7\pi}3\right)$．" "\n"
        r"在该区间内 $\cos\theta=\dfrac12$ 的解为 $\theta=\dfrac{5\pi}3$（$\theta=\dfrac\pi3$ 是区间端点，对应 $A=0$，舍去），" "\n"
        r"$\therefore 2A+\dfrac\pi3=\dfrac{5\pi}3$，$A=\dfrac{2\pi}3$．" "\n"
        r"由余弦定理及 $\cos A=-\dfrac12$：" "\n"
        r"$a^{2}=b^{2}+c^{2}-2bc\cos\dfrac{2\pi}3=b^{2}+c^{2}+bc=(b+c)^{2}-bc=4-bc$．" "\n"
        r"由基本不等式 $bc\le\dfrac{(b+c)^{2}}4=1$，$\therefore a^{2}=4-bc\ge4-1=3$，" "\n"
        r"当且仅当 $b=c=1$ 时取等号，此时 $a=\sqrt3$．" "\n"
        r"$\therefore a$ 的最小值为 $\sqrt3$．"
    ),
    'review': (
        r"**① 降幂 + 辅助角（本题第一处关键）**：$2\cos^2x=1+\cos2x$ 把二次降为一次，与 $\cos(2x+\frac{2\pi}3)$ 展开式合并 ✓✓✓" "\n"
        r"$\left(-\frac12+1\right)\cos2x-\frac{\sqrt3}2\sin2x=\frac12\cos2x-\frac{\sqrt3}2\sin2x=\cos(2x+\frac\pi3)$ ✓✓✓" "\n"
        r"② **最大值 $2$ 的取等条件**：$\cos(2x+\frac\pi3)=1$ ⟹ $2x+\frac\pi3=2k\pi$ ⟹ $x=k\pi-\frac\pi6$ ✓✓✓" "\n"
        r"（**$k\in\mathbb Z$ 必须写**，且注意是 $k\pi$ 不是 $2k\pi$，因为 $2x=2k\pi-\frac\pi3$ ⟹ $x=k\pi-\frac\pi6$）" "\n"
        r"③ **$f(A)=\frac32$ ⟹ $\cos(2A+\frac\pi3)=\frac12$ 的两根要检验**：" "\n"
        r"$2A+\frac\pi3\in(\frac\pi3,\frac{7\pi}3)$。$\cos\theta=\frac12$ 在该区间的解：$\theta=\frac{5\pi}3$（还有 $\theta=\frac\pi3,\frac{7\pi}3$ 是端点，对应 $A=0,\pi$，舍）✓✓✓" "\n"
        r"$\theta=\frac{5\pi}3$ ⟹ $2A=\frac{4\pi}3$ ⟹ $A=\frac{2\pi}3$ ✓✓✓" "\n"
        r"④ **$a^2=(b+c)^2-bc=4-bc$**：因为 $\cos A=-\frac12$ 使 $-2bc\cos A=+bc$ ✓✓✓" "\n"
        r"⑤ **$bc\le1$ 当且仅当 $b=c=1$**：此时 $a^2=4-1=3$，$a=\sqrt3$；检验三角形：$b+c=2>a=\sqrt3=1.732$ ✓ ✓✓✓" "\n"
        r"⑥ **数值对拍**：$b=c=1$、$A=120^\circ$：$a^2=1+1-2\cdot1\cdot1\cdot(-0.5)=3$ ⟹ $a=1.732=\sqrt3$ ✓；" "\n"
        r"$f(\frac{2\pi}3)=\cos(\frac{4\pi}3+\frac{2\pi}3)+2\cos^2\frac{2\pi}3=\cos(2\pi)+2\cdot\frac14=1+0.5=1.5=\frac32$ ✓✓✓ **完全闭合**" "\n"
        r"**答案 $2$、$\{x\mid x=k\pi-\frac\pi6\}$、$\sqrt3$ 全部正确** ✓" "\n"
        r"**⭐⭐ 通法（三角函数化简 + 解三角形衔接题）**：" "\n"
        r"① ⭐⭐ **降幂公式 $2\cos^2x=1+\cos2x$、$2\sin^2x=1-\cos2x$** —— 凡出现 $\cos^2x$ 先降幂，与 $\cos(2x+\varphi)$ 同频才好合并 ✓✓✓；" "\n"
        r"② ⭐⭐ **$p\cos\theta+q\sin\theta=\sqrt{p^2+q^2}\cos(\theta-\varphi)$，$\tan\varphi=\frac qp$**：" "\n"
        r"本题 $p=\frac12,q=-\frac{\sqrt3}2$ ⟹ 振幅 $1$、$\varphi=-\frac\pi3$，即 $\cos(2x+\frac\pi3)$ ✓✓✓；" "\n"
        r"③ ⭐⭐ **由 $f(A)=$ 常数解 $A$ 时，先写出整体角 $2A+\varphi$ 的范围再挑解**，端点值（对应 $A=0$ 或 $\pi$）必须舍去 ✓✓✓；" "\n"
        r"④ ⭐⭐ **$b+c$ 已知、求 $a$ ⟹ 余弦定理改写成 $a^2=(b+c)^2-2bc(1+\cos A)$，再用 $bc\le\frac{(b+c)^2}4$** ✓✓✓；" "\n"
        r"⑤ ⭐⭐ **$A$ 为钝角时 $\cos A<0$，$a^2=(b+c)^2+|\text{正项}|$，此时 $a$ 的**最小值**在 $b=c$ 取到**（因 $-bc$ 项要最大）** ✓✓✓；" "\n"
        r"⑥ ⚠ **最后要检验三角形存在**：$b+c>a$（本题 $2>1.732$ ✓）✓✓✓"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-222'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-222-V3',
}

QS = [T219_E1, T219_V1, T219_V2, T219_V3,
      T221_E1, T221_V1, T221_V2, T221_V3,
      T222_E1, T222_V1, T222_V2, T222_V3]
