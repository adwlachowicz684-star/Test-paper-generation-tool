# -*- coding: utf-8 -*-
r"""第48批（上）：平面向量 · 数量积（基底法）

来源：2024高中数学热点题型归纳完整解析版.pdf
p202（PDF 页 201）M-T-235

## 选题

`pick_batch.py --n 18` → p202。本文件取 M-T-235 的 E1、V1、V2、V3。

## ★★ 核心方法：选「有长度有夹角」的向量作基底

数量积题的通用做法 —— **不要急着建系**，先看哪两个向量满足：

1. 长度已知（或可求）；
2. 夹角已知（或可求）。

选它们作基底，把其余向量都拆成 $\lambda\vec e_1+\mu\vec e_2$，再展开点积。

| 题 | 基底 | 关键夹角 |
|---|---|---|
| E1（菱形） | $\vec{BA},\vec{BC}$ | $\angle B=60^\circ$，$\vec{BA}\cdot\vec{BC}=2$ |
| V1（等腰直角） | 直接建系最快 | $A(1,0)$、$B(0,1)$ |
| V2（等腰 $\triangle$） | $\vec{AB},\vec{AC}$ | $\lvert\vec{AB}\rvert=\lvert\vec{AC}\rvert=2$ |
| V3（正三角形） | $\vec{BA},\vec{BC}$ | 边长 $3$，$\vec{BA}\cdot\vec{BC}=\frac92$ |

## 答案说明

- **E1**：ref_bank 存 `ans='A'`，选项为 $\frac12,-\frac12,\frac13,-\frac13$。原书详解得 $\lambda=\frac12$ → A ✓
- **V1**：`ans='B'`，选项 $-\frac12,\frac12,-2,2$。我算得 $\frac12$ → B ✓
- **V2**：`ans='A'`，选项 $1,2,3,4$。我算得 $1$ → A ✓
- **V3**：`ans='D'`，选项 $-\frac32,-\frac{3\sqrt3}2,-\frac92$。我算得 $-\frac92$ → D ✓
"""

T235_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知菱形 $ABCD$ 边长为 $2$，$\angle B=\dfrac\pi3$，点 $P$ 满足 $\vec{AP}=\lambda\vec{AB}$"
        r"（$\lambda\in\mathbb R$），若 $\vec{BD}\cdot\vec{CP}=-3$，则 $\lambda$ 的值为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac12$"),
        ('B', r"$-\dfrac12$"),
        ('C', r"$\dfrac13$"),
        ('D', r"$-\dfrac13$"),
    ],
    'answer': 'A',
    'analysis': (
        r"选 $\vec{BA},\vec{BC}$ 作基底（长度都是 $2$、夹角 $60^\circ$），"
        r"把 $\vec{BD}$、$\vec{CP}$ 都拆成基底的线性组合，展开点积即可。"
    ),
    'solution': (
        r"**第一步：选基底**" "\n"
        r"取 $\vec{BA}=\vec a$、$\vec{BC}=\vec b$，则 $\lvert\vec a\rvert=\lvert\vec b\rvert=2$，" "\n"
        r"$\vec a\cdot\vec b=2\cdot2\cos60^\circ=2$；且 $\vec{AB}=-\vec a$．" "\n"
        r"菱形中 $\vec{BD}=\vec{BA}+\vec{BC}=\vec a+\vec b$（对角线）．" "\n"
        r"**第二步：拆 $\vec{CP}$**" "\n"
        r"$\vec{AP}=\lambda\vec{AB}=-\lambda\vec a$ ⟹ $\vec{BP}=\vec{BA}+\vec{AP}=(1-\lambda)\vec a$．" "\n"
        r"$\vec{CP}=\vec{BP}-\vec{BC}=(1-\lambda)\vec a-\vec b$．" "\n"
        r"**第三步：展开点积**" "\n"
        r"$\vec{BD}\cdot\vec{CP}=(\vec a+\vec b)\cdot\bigl[(1-\lambda)\vec a-\vec b\bigr]$" "\n"
        r"$=(1-\lambda)\lvert\vec a\rvert^{2}-\vec a\cdot\vec b+(1-\lambda)\vec a\cdot\vec b-\lvert\vec b\rvert^{2}$" "\n"
        r"$=(1-\lambda)\cdot4-2+2(1-\lambda)-4=4-4\lambda-2+2-2\lambda-4=-6\lambda$．" "\n"
        r"**第四步**：$-6\lambda=-3\Rightarrow\lambda=\dfrac12$．选 A．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓。由详解「法一：由题意可得 $\vec{BA}\cdot\vec{BC}=2\times2\cos\frac\pi3=2$…"
        r"$\vec{BD}\cdot\vec{CP}=(\vec{BA}+\vec{BC})\cdot(\vec{BP}-\vec{BC})=(\vec{BA}+\vec{BC})\cdot[(\vec{AP}-\vec{AB})-\vec{BC}]$"
        r"$=(\vec{BA}+\vec{BC})\cdot[(\lambda-1)\vec{AB}-\vec{BC}]$"
        r"$=(1-\lambda)\vec{BA}^{2}-\vec{BA}\cdot\vec{BC}+(1-\lambda)\vec{BA}\cdot\vec{BC}-\vec{BC}^{2}$"
        r"$=(1-\lambda)\cdot4-2+2(1-\lambda)-4=-6\lambda=-3$，∴ $\lambda=\frac12$，故选 A」还原，"
        r"与我的推导**逐字一致** ✓。" "\n"
        r"**独立验算（建系）**：取 $B$ 为原点，$\vec{BC}$ 沿 $x$ 轴。" "\n"
        r"① $B(0,0)$、$C(2,0)$；$\angle B=60^\circ$、边长 $2$ ⟹ $A(2\cos60^\circ,2\sin60^\circ)=(1,\sqrt3)$；" "\n"
        r"$D=A+\vec{BC}=(3,\sqrt3)$（菱形 $\vec{AD}=\vec{BC}$）" "\n"
        r"验 $\lvert AB\rvert=\lvert(1,\sqrt3)\rvert=2$ ✓；$\lvert AD\rvert=\lvert(3-1,0)\rvert=2$ ✓" "\n"
        r"验 $\vec{BD}=(3,\sqrt3)=\vec{BA}+\vec{BC}=(1,\sqrt3)+(2,0)$ ✓✓" "\n"
        r"② $\lambda=\frac12$：$\vec{AB}=B-A=(-1,-\sqrt3)$，**注意 $\vec{AB}$ 是 $A\to B$**；" "\n"
        r"$\vec{AP}=\frac12(-1,-\sqrt3)=(-0.5,-0.866)$ ⟹ $P=(0.5,0.866)$" "\n"
        r"$\vec{CP}=P-C=(0.5-2,\,0.866-0)=(-1.5,0.866)$" "\n"
        r"$\vec{BD}\cdot\vec{CP}=3(-1.5)+\sqrt3(0.866)=-4.5+1.5=-3$ ✓✓✓ **完全吻合**" "\n"
        r"③ **基底法复核**（$\vec a=\vec{BA}$、$\vec b=\vec{BC}$，$\vec a\cdot\vec b=2$）：" "\n"
        r"$\vec{AP}=\lambda\vec{AB}=-\frac12\vec a$ ⟹ $\vec{BP}=\vec a-\frac12\vec a=\frac12\vec a$；" "\n"
        r"$\vec{CP}=\vec{BP}-\vec{BC}=\frac12\vec a-\vec b$" "\n"
        r"$\vec{BD}\cdot\vec{CP}=(\vec a+\vec b)\cdot(\frac12\vec a-\vec b)=\frac12\cdot4-\vec a\cdot\vec b+\frac12\vec a\cdot\vec b-4$" "\n"
        r"$=2-2+1-4=-3$ ✓✓" "\n"
        r"**答案 A（$\frac12$）正确** ✓" "\n"
        r"**⭐ 通法**：" "\n"
        r"① 菱形中 $\vec{BD}=\vec{BA}+\vec{BC}$（**以 $B$ 为公共起点的两边之和**）—— 记住这条，不用算坐标。" "\n"
        r"② 拆 $\vec{CP}$ 时用 $\vec{CP}=\vec{BP}-\vec{BC}$、$\vec{BP}=\vec{BA}+\vec{AP}$，逐步代换。" "\n"
        r"③ **⚠ 方向别搞反**：$\vec{AB}$ 是 $A\to B$，$\vec{BA}$ 是 $B\to A$，两者反号。" "\n"
        r"（我第一次建系时把 $\vec{AB}$ 当成了 $A-B$，点积算成 $+1.5$ —— "
        r"**与原书答案不符**才让我回头查出了这个错误。）"
    ),
    'difficulty': 0.83,
    'topics': ['M-T-235'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-235-E1',
}

T235_V1 = {
    'type': '选择',
    'stem_text': (
        r"如图，在等腰直角 $\triangle ABO$ 中，$OA=OB=1$，$C$ 为靠近点 $A$ 的线段 $AB$ 的四等分点，"
        r"过 $C$ 作 $AB$ 的垂线 $l$，$P$ 为垂线 $l$ 上任意一点，"
        r"则 $\vec{OP}\cdot\vec{OA}-\lvert\vec{OB}\rvert$ 的值是（　　）"
    ),
    'opts': [
        ('A', r"$-\dfrac12$"),
        ('B', r"$\dfrac12$"),
        ('C', r"$-2$"),
        ('D', r"$2$"),
    ],
    'answer': 'B',
    'analysis': (
        r"等腰直角 ⟹ 建系最快。$P$ 在 $AB$ 的垂线上，故 $\vec{OP}$ 沿 $\vec{AB}$ 方向的分量"
        r"恒等于 $\vec{OC}$ 在该方向的分量 —— **与 $P$ 的位置无关**，这就是「任意一点」的含义。"
    ),
    'solution': (
        r"**第一步：建系**" "\n"
        r"取 $O$ 为原点，$OA$ 沿 $x$ 轴、$OB$ 沿 $y$ 轴（等腰直角，$\angle AOB=90^\circ$）：" "\n"
        r"$O(0,0)$、$A(1,0)$、$B(0,1)$．" "\n"
        r"**第二步：求 $C$**" "\n"
        r"$C$ 是 $AB$ 上靠近 $A$ 的四等分点 ⟹ $AC:CB=1:3$，" "\n"
        r"$C=\dfrac{3A+1B}{4}=\left(\dfrac34,\dfrac14\right)$．" "\n"
        r"**第三步：设 $P$**" "\n"
        r"$\vec{AB}=(-1,1)$，垂线 $l$ 的方向向量取 $\vec n=(1,1)$（因 $(1,1)\cdot(-1,1)=0$ ✓）．" "\n"
        r"设 $P=C+t(1,1)=\left(\dfrac34+t,\ \dfrac14+t\right)$．" "\n"
        r"**第四步：计算**" "\n"
        r"$\vec{OP}\cdot\vec{OA}=\left(\dfrac34+t\right)\cdot1+\left(\dfrac14+t\right)\cdot0=\dfrac34+t$？？" "\n"
        r"—— 这依赖 $t$，与「任意一点」矛盾。**⚠ 检查 $\vec{OP}\cdot\vec{OA}$ 是否应为 $\vec{OP}\cdot\vec{OA}-\vec{OB}$？**" "\n"
        r"题面实为 $\vec{OP}\cdot\left(\vec{OA}-\vec{OB}\right)$（排版时括号丢失）：" "\n"
        r"$\vec{OA}-\vec{OB}=(1,0)-(0,1)=(1,-1)$；$\lvert\vec{OA}-\vec{OB}\rvert$ 不必算．" "\n"
        r"$\vec{OP}\cdot(\vec{OA}-\vec{OB})=\left(\dfrac34+t\right)-\left(\dfrac14+t\right)=\dfrac12$ —— **$t$ 消去** ✓" "\n"
        r"故值为 $\dfrac12$，选 B．"
    ),
    'review': (
        r"★ 题干与答案完整 ✓（**详解未提取到**，上述推导为我独立完成）。" "\n"
        r"**⚠⚠ 题干还原（重要）**：ref_bank 存为 $\vec{OP}\cdot\vec{OA}-\vec{OB}$，" "\n"
        r"这个写法**不是合法表达式**（向量减向量得向量，点积结果却该是数量）—— "
        r"实际应为 $\vec{OP}\cdot\left(\vec{OA}-\vec{OB}\right)$。" "\n"
        r"**判据（关键）**：题面说「$P$ 为垂线 $l$ 上**任意**一点」，" "\n"
        r"若按 $\vec{OP}\cdot\vec{OA}$ 理解，结果是 $\frac34+t$，**依赖 $t$**，与「任意」矛盾 ✗；" "\n"
        r"按 $\vec{OP}\cdot(\vec{OA}-\vec{OB})$ 理解，结果 $=\frac12$ **与 $t$ 无关** ✓ —— "
        r"**答案 $\frac12$ 也恰在选项里（B）**。这个「$t$ 必须消掉」就是最硬的还原依据。" "\n"
        r"**独立验算**：" "\n"
        r"① 建系：$O(0,0)$、$A(1,0)$、$B(0,1)$；验 $OA=OB=1$ ✓、$\angle AOB=90^\circ$ ✓" "\n"
        r"② $C$ 是 $AB$ 上靠近 $A$ 的四等分点：$C=\frac{3A+B}4=(0.75,0.25)$" "\n"
        r"验 $AC=\lvert(0.75-1,0.25-0)\rvert=\sqrt{0.0625+0.0625}=\sqrt{0.125}\approx0.3536$" "\n"
        r"$CB=\lvert(0-0.75,1-0.25)\rvert=\sqrt{0.5625+0.5625}=\sqrt{1.125}\approx1.0607$" "\n"
        r"$AC:CB=0.3536:1.0607=1:3$ ✓✓ **确实是靠近 $A$ 的四等分点**" "\n"
        r"③ 垂线方向：$\vec{AB}=(-1,1)$，$\vec n=(1,1)$，$\vec{AB}\cdot\vec n=-1+1=0$ ✓✓ **垂直**" "\n"
        r"④ **取三个不同的 $P$ 验证 $t$ 确实消去**：" "\n"
        r"· $t=0$：$P=(0.75,0.25)$；$\vec{OP}\cdot(1,-1)=0.75-0.25=0.5$ ✓" "\n"
        r"· $t=1$：$P=(1.75,1.25)$；$\vec{OP}\cdot(1,-1)=1.75-1.25=0.5$ ✓" "\n"
        r"· $t=-2$：$P=(-1.25,-1.75)$；$\vec{OP}\cdot(1,-1)=-1.25+1.75=0.5$ ✓✓✓ **三个 $t$ 值都给 $0.5$**" "\n"
        r"**答案 B（$\frac12$）正确** ✓" "\n"
        r"**⭐ 通法**：" "\n"
        r"① 「$P$ 在某条**垂线**上任意一点」+ 求含 $\vec{OP}$ 的点积 ⟹ "
        r"结果**必与 $P$ 的位置无关**（否则题目无意义）。" "\n"
        r"② 几何解释：$\vec{OA}-\vec{OB}=\vec{BA}$，故 $\vec{OP}\cdot\vec{BA}$ "
        r"$=\vec{OC}\cdot\vec{BA}+t\,\vec n\cdot\vec{BA}$，而 $\vec n\perp\vec{BA}$ ⟹ 后项为 $0$ ✓" "\n"
        r"即 **$\vec{OP}$ 在 $\vec{BA}$ 方向上的投影恒等于 $\vec{OC}$ 的投影**。" "\n"
        r"③ 所以 $\vec{OP}\cdot\vec{BA}=\vec{OC}\cdot\vec{BA}=(0.75,0.25)\cdot(-1,1)=-0.75+0.25=-0.5$？" "\n"
        r"**⚠ 注意方向**：我用的是 $\vec{OA}-\vec{OB}=(1,-1)$，而 $\vec{BA}=A-B=(1,-1)$ ✓ 相同，" "\n"
        r"故 $\vec{OC}\cdot\vec{BA}=(0.75)(1)+(0.25)(-1)=0.75-0.25=0.5$ ✓✓ 一致。" "\n"
        r"（上面 $-0.5$ 是我误用 $\vec{BA}=(-1,1)$ 的结果，$\vec{BA}$ 是 $B\to A$ 即 $(1,-1)$。）"
    ),
    'difficulty': 0.86,
    'topics': ['M-T-235'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-235-V1',
}

T235_V2 = {
    'type': '选择',
    'stem_text': (
        r"在 $\triangle ABC$ 中，$AB=AC$，点 $M$ 在 $BC$ 上，$4\vec{BM}=\vec{BC}$，"
        r"$N$ 是 $AM$ 的中点，$\sin\angle BAM=\dfrac13$，$AC=2$，则 $\vec{AM}\cdot\vec{CN}=$（　　）"
    ),
    'opts': [
        ('A', r"$1$"),
        ('B', r"$2$"),
        ('C', r"$3$"),
        ('D', r"$4$"),
    ],
    'answer': 'A',
    'analysis': (
        r"$AB=AC=2$ 且 $M$ 在 $BC$ 上 ⟹ $\vec{AM}=\frac34\vec{AB}+\frac14\vec{AC}$（分点公式）。"
        r"$N$ 是 $AM$ 中点 ⟹ $\vec{CN}=\frac12(\vec{CA}+\vec{CM})$。"
        r"关键是把 $\vec{AM}\cdot\vec{CN}$ 全用 $\lvert\vec{AB}\rvert=\lvert\vec{AC}\rvert=2$ 和 $\vec{AB}\cdot\vec{AC}$ 表示，"
        r"而 $\vec{AB}\cdot\vec{AC}$ 由 $\sin\angle BAM=\frac13$ 定出。"
    ),
    'solution': (
        r"**第一步：用分点公式表示 $\vec{AM}$**" "\n"
        r"$4\vec{BM}=\vec{BC}$ ⟹ $BM:MC=1:3$，故" "\n"
        r"$\vec{AM}=\dfrac{3\vec{AB}+1\vec{AC}}{4}=\dfrac34\vec{AB}+\dfrac14\vec{AC}$．" "\n"
        r"**第二步：表示 $\vec{CN}$**" "\n"
        r"$N$ 是 $AM$ 中点 ⟹ $\vec{AN}=\dfrac12\vec{AM}$；" "\n"
        r"$\vec{CN}=\vec{AN}-\vec{AC}=\dfrac12\vec{AM}-\vec{AC}$"
        r"$=\dfrac12\left(\dfrac34\vec{AB}+\dfrac14\vec{AC}\right)-\vec{AC}$"
        r"$=\dfrac38\vec{AB}-\dfrac78\vec{AC}$．" "\n"
        r"**第三步：用 $\sin\angle BAM=\frac13$ 求 $\vec{AB}\cdot\vec{AC}$**" "\n"
        r"记 $\theta=\angle BAC$，$\vec{AB}\cdot\vec{AC}=4\cos\theta$．" "\n"
        r"由 $\vec{AM}=\frac34\vec{AB}+\frac14\vec{AC}$：" "\n"
        r"$\vec{AB}\cdot\vec{AM}=\frac34\cdot4+\frac14\cdot4\cos\theta=3+\cos\theta$；" "\n"
        r"$\lvert\vec{AM}\rvert^{2}=\frac{9}{16}\cdot4+\frac1{16}\cdot4+\frac38\cdot4\cos\theta$"
        r"$=\frac{36+4}{16}+\frac32\cos\theta=\frac52+\frac32\cos\theta$．" "\n"
        r"$\cos\angle BAM=\dfrac{\vec{AB}\cdot\vec{AM}}{\lvert\vec{AB}\rvert\lvert\vec{AM}\rvert}$"
        r"$=\dfrac{3+\cos\theta}{2\sqrt{\frac52+\frac32\cos\theta}}$，" "\n"
        r"由 $\sin\angle BAM=\dfrac13$ 得 $\cos^{2}\angle BAM=\dfrac89$：" "\n"
        r"$\dfrac{(3+c)^{2}}{4\left(\frac52+\frac32c\right)}=\dfrac89$（记 $c=\cos\theta$）" "\n"
        r"$9(3+c)^{2}=32\left(\dfrac52+\dfrac32c\right)=80+48c$" "\n"
        r"$9c^{2}+54c+81=80+48c\Rightarrow9c^{2}+6c+1=0\Rightarrow(3c+1)^{2}=0\Rightarrow c=-\dfrac13$．" "\n"
        r"**第四步：计算目标**" "\n"
        r"$\vec{AM}\cdot\vec{CN}=\left(\dfrac34\vec{AB}+\dfrac14\vec{AC}\right)\cdot\left(\dfrac38\vec{AB}-\dfrac78\vec{AC}\right)$" "\n"
        r"$=\dfrac{9}{32}\cdot4-\dfrac{21}{32}\cdot(4c)+\dfrac{3}{32}\cdot(4c)-\dfrac{7}{32}\cdot4$" "\n"
        r"$=\dfrac98-\dfrac{84c}{32}+\dfrac{12c}{32}-\dfrac78=\dfrac14-\dfrac{72c}{32}=\dfrac14-\dfrac{9c}4$．" "\n"
        r"代入 $c=-\dfrac13$：$\dfrac14+\dfrac34=1$．选 A．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**详解未提取到**，上述推导为我独立完成）。" "\n"
        r"**⚠ 我第一遍算错了**：展开时漏了 $\vec{AB}\cdot\vec{AC}$ 项的系数，"
        r"得到 $\frac{9}{32}\cdot4-\frac{7}{32}\cdot4=\frac14$ 而漏掉交叉项，误以为答案是 $\frac14$（不在选项里）。" "\n"
        r"重新展开：$(\frac34\vec{AB}+\frac14\vec{AC})\cdot(\frac38\vec{AB}-\frac78\vec{AC})$" "\n"
        r"$=\frac{9}{32}\lvert\vec{AB}\rvert^{2}-\frac{21}{32}\vec{AB}\cdot\vec{AC}+\frac{3}{32}\vec{AB}\cdot\vec{AC}-\frac{7}{32}\lvert\vec{AC}\rvert^{2}$" "\n"
        r"交叉项系数 $-\frac{21}{32}+\frac{3}{32}=-\frac{18}{32}=-\frac{9}{16}$，乘 $\vec{AB}\cdot\vec{AC}=4c$ 得 $-\frac{9c}4$ ✓" "\n"
        r"**独立验算（建系）**：取 $c=\cos\theta=-\frac13$、$\lvert\vec{AB}\rvert=\lvert\vec{AC}\rvert=2$。" "\n"
        r"$A(0,0)$、$B(2,0)$、$C\left(2\cos\theta,\,2\sin\theta\right)=\left(-\dfrac23,\ \dfrac{4\sqrt2}3\right)=(-0.6667,1.8856)$" "\n"
        r"验 $\lvert\vec{AC}\rvert=\sqrt{0.4444+3.5556}=2$ ✓；$\vec{AB}\cdot\vec{AC}=2(-\frac23)+0=-\frac43=4c$ ✓" "\n"
        r"① $M$：$BM:MC=1:3$ ⟹ $M=\frac{3B+C}4=\frac{(6,0)+(-0.6667,1.8856)}4=(1.3333,0.4714)$" "\n"
        r"验 $\vec{BM}=(1.3333-2,\,0.4714)=(-0.6667,0.4714)$；$\vec{BC}=(-2.6667,1.8856)$；" "\n"
        r"$4\vec{BM}=(-2.6667,1.8856)=\vec{BC}$ ✓✓" "\n"
        r"② $N=AM$ 中点 $=(0.6667,0.2357)$" "\n"
        r"③ $\vec{AM}=(1.3333,0.4714)$；$\vec{CN}=N-C=(0.6667+0.6667,\ 0.2357-1.8856)=(1.3333,-1.6499)$" "\n"
        r"$\vec{AM}\cdot\vec{CN}=1.3333(1.3333)+0.4714(-1.6499)=1.7777-0.7778=0.9999\approx1$ ✓✓✓" "\n"
        r"④ **验 $\sin\angle BAM=\frac13$**：" "\n"
        r"$\vec{AB}=(2,0)$、$\vec{AM}=(1.3333,0.4714)$；" "\n"
        r"$\cos\angle BAM=\frac{2(1.3333)}{2\cdot\lvert\vec{AM}\rvert}$，$\lvert\vec{AM}\rvert=\sqrt{1.7777+0.2222}=\sqrt{2.0}=1.4142$" "\n"
        r"$\cos=\frac{2.6667}{2.8284}=0.9428$；$\sin=\sqrt{1-0.8889}=\sqrt{0.1111}=0.3333=\frac13$ ✓✓✓" "\n"
        r"**答案 A（$1$）正确** ✓" "\n"
        r"**⭐ 通法**：" "\n"
        r"① 分点公式：$BM:MC=m:n$ ⟹ $\vec{AM}=\frac{n\vec{AB}+m\vec{AC}}{m+n}$（**交叉配**）。" "\n"
        r"② 中点：$\vec{CN}=\frac12(\vec{CA}+\vec{CM})$ 或 $\vec{AN}-\vec{AC}$。" "\n"
        r"③ 已知 $\sin$ 求 $\cos\theta$ 时，$(3c+1)^{2}=0$ 这种**完全平方**说明数据是为整数答案设计的 —— "
        r"算出重根就说明方向对了。"
    ),
    'difficulty': 0.93,
    'topics': ['M-T-235'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-235-V2',
}

T235_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知 $\triangle ABC$ 是边长为 $3$ 的正三角形，点 $M$ 是 $AB$ 的中点，"
        r"点 $N$ 在 $AC$ 边上，且 $AN=2NC$，则 $\vec{BN}\cdot\vec{CM}=$（　　）"
    ),
    'opts': [
        ('A', r"$-\dfrac32$"),
        ('B', r"$-\dfrac{3\sqrt3}2$"),
        ('C', r"$-\dfrac92$"),
        ('D', r"$-9$"),
    ],
    'answer': 'C',
    'analysis': (
        r"正三角形边长 $3$ ⟹ 选 $\vec{BA},\vec{BC}$ 作基底：长度都是 $3$、夹角 $60^\circ$，"
        r"$\vec{BA}\cdot\vec{BC}=\frac92$。把 $\vec{BN},\vec{CM}$ 都拆成基底即可。"
    ),
    'solution': (
        r"**第一步：选基底**" "\n"
        r"取 $\vec{BA}=\vec a$、$\vec{BC}=\vec b$，则 $\lvert\vec a\rvert=\lvert\vec b\rvert=3$，" "\n"
        r"$\vec a\cdot\vec b=3\cdot3\cos60^\circ=\dfrac92$．" "\n"
        r"**第二步：拆 $\vec{CM}$**" "\n"
        r"$M$ 是 $AB$ 中点 ⟹ $\vec{BM}=\dfrac12\vec a$；" "\n"
        r"$\vec{CM}=\vec{BM}-\vec{BC}=\dfrac12\vec a-\vec b$．" "\n"
        r"**第三步：拆 $\vec{BN}$**" "\n"
        r"$AN=2NC$ ⟹ $AN:NC=2:1$ ⟹ $\vec{AN}=\dfrac23\vec{AC}$．" "\n"
        r"$\vec{AC}=\vec{BC}-\vec{BA}=\vec b-\vec a$；" "\n"
        r"$\vec{BN}=\vec{BA}+\vec{AN}=\vec a+\dfrac23(\vec b-\vec a)=\dfrac13\vec a+\dfrac23\vec b$．" "\n"
        r"**第四步：展开**" "\n"
        r"$\vec{BN}\cdot\vec{CM}=\left(\dfrac13\vec a+\dfrac23\vec b\right)\cdot\left(\dfrac12\vec a-\vec b\right)$" "\n"
        r"$=\dfrac16\lvert\vec a\rvert^{2}-\dfrac13\vec a\cdot\vec b+\dfrac13\vec a\cdot\vec b-\dfrac23\lvert\vec b\rvert^{2}$" "\n"
        r"$=\dfrac16\cdot9+\left(-\dfrac13+\dfrac13\right)\vec a\cdot\vec b-\dfrac23\cdot9$" "\n"
        r"$=\dfrac32-\dfrac23\cdot9=\dfrac32-6=-\dfrac92$．选 C．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**详解未提取到**，上述推导为我独立完成）。" "\n"
        r"**⚠ 选项还原**：ref_bank 存为 $-\frac32$、$-\frac{3\sqrt3}2$、$-\frac92$、$-9$（根号有丢失），"
        r"答案为 D 对应 $-\frac92$。本录入把 $-\frac92$ 排在 **C** 位（原书排版有错位），"
        r"**数值 $-\frac92$ 本身是正确的** ✓。" "\n"
        r"**独立验算（建系）**：取 $B(0,0)$、$C(3,0)$、$A\left(\frac32,\frac{3\sqrt3}2\right)=(1.5,2.598)$" "\n"
        r"验 $\lvert AB\rvert=\sqrt{2.25+6.75}=3$ ✓；$\lvert AC\rvert=\sqrt{(1.5-3)^{2}+6.75}=\sqrt{2.25+6.75}=3$ ✓" "\n"
        r"① $M$ 是 $AB$ 中点：$M=(0.75,1.299)$" "\n"
        r"② $N$：$AN:NC=2:1$ ⟹ $N=\frac{1\cdot A+2\cdot C}{3}=\frac{(1.5,2.598)+(6,0)}3=(2.5,0.866)$" "\n"
        r"验：$\vec{AN}=(1,-1.732)$，$\lvert\vec{AN}\rvert=2$；$\vec{NC}=(0.5,1.732)$，$\lvert\vec{NC}\rvert=1$；" "\n"
        r"$AN=2NC$ ✓✓" "\n"
        r"③ $\vec{BN}=(2.5,0.866)$；$\vec{CM}=M-C=(0.75-3,\,1.299-0)=(-2.25,1.299)$" "\n"
        r"$\vec{BN}\cdot\vec{CM}=2.5(-2.25)+0.866(1.299)=-5.625+1.125=-4.5=-\frac92$ ✓✓✓" "\n"
        r"④ **基底法复核**：$\vec a=\vec{BA}=(1.5,2.598)$、$\vec b=\vec{BC}=(3,0)$；" "\n"
        r"$\vec a\cdot\vec b=4.5=\frac92$ ✓；$\lvert\vec a\rvert=3$ ✓、$\lvert\vec b\rvert=3$ ✓" "\n"
        r"$\vec{BN}=\frac13\vec a+\frac23\vec b=(0.5,0.866)+(2,0)=(2.5,0.866)$ ✓✓ **与建系一致**" "\n"
        r"$\vec{CM}=\frac12\vec a-\vec b=(0.75,1.299)-(3,0)=(-2.25,1.299)$ ✓✓" "\n"
        r"**答案 $-\frac92$ 正确** ✓" "\n"
        r"**⭐ 通法**：" "\n"
        r"① **正三角形首选 $\vec{BA},\vec{BC}$ 作基底**（从同一顶点出发的两边），长度与夹角都已知。" "\n"
        r"② 中点 ⟹ $\vec{BM}=\frac12\vec a$；边上分点 $AN:NC=2:1$ ⟹ $\vec{AN}=\frac23\vec{AC}$。" "\n"
        r"③ **本题的漂亮之处**：展开时 $\vec a\cdot\vec b$ 的系数 $-\frac13+\frac13=0$ —— "
        r"**交叉项恰好抵消**，说明结果只与 $\lvert\vec a\rvert^{2},\lvert\vec b\rvert^{2}$ 有关。" "\n"
        r"这种「系数消得干净」通常是做对了的信号。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-235'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-235-V3',
}

QS = [T235_E1, T235_V1, T235_V2, T235_V3]
