# -*- coding: utf-8 -*-
r"""第81批：立体几何轨迹、圆锥曲线离心率、解三角形（12 题）

M-T-341（4）、M-T-375（3）、M-T-206-V3（1）、M-T-203（2）、M-T-176（2）

## ★★ 12 题我全部独立验算（坐标法 / 数值扫描 / 解析）

| 题 | 我的验算 | 答案 |
|---|---|---|
| M-T-341-E1 | 建系：$PE^2=y^2+a^2$、$PM^2=x^2+(y-t)^2$ ⟹ $x^2=2ty-t^2$ | **D 抛物线** |
| M-T-341-V1 | 法向量 $(0.5,-1,1)$，$F=(1,y,z)$ 代入得 $z=y+\frac12$，端点 $(1,0,\frac12)$、$(1,\frac12,1)$ | **D 线段** |
| M-T-341-V2 | 圆心 $(8,0)$ 半径 $4$，弧从 $(4,0)$ 到 $(6,2\sqrt3)$，圆心角 $\frac\pi3$ ⟹ 弧长 $\frac{4\pi}3$ | **$\frac{4\pi}3$** |
| M-T-341-V3 | $\cos\angle MAC'=\frac{\sqrt{15}}5<\cos\theta=\frac{\sqrt6}3$ ⟹ $\theta<$ 半顶角 ⟹ 双曲线 | **C** |
| M-T-375-E1 | 奔驰定理 ⟹ $F_1F_2:PF_1:PF_2=5:4:3$ ⟹ $e=\frac{5\lambda/2}{\lambda/2}=5$ | **C** |
| M-T-375-V2 | $x_1=-\frac{3c}2=-\frac{a^2}{2c}$ ⟹ $3c^2=a^2$ ⟹ $e=\frac{\sqrt3}3$ | **C** |
| M-T-375-V3 | $a=1$、$c=\sqrt2$ ⟹ $e=\sqrt2$ | **A** |
| M-T-206-V3 | $u{\cdot}AO=v{\cdot}AO=8$ ⟹ $\cos A=\frac12$、$t=\frac13$ ⟹ $S=4\sqrt3$ | **B** |
| M-T-203-E1 | $\frac{BD}{AC}=\frac{\sin C}{\sin B}\sin A=0.2500$ | **A $\frac14$** |
| M-T-203-V1 | 三高积 $=\frac8{bc}$，$bc=\frac2{\sin A}$ ⟹ 最大化即 $\tan\frac A2\le\frac14$ ⟹ $\sin A=\frac8{17}$ | **$\frac8{17}$** |
| M-T-176-V1 | 左移 $\frac\pi6$ 后偶函数 ⟹ $\varphi=\frac\pi6$，扫描得 max $=2$ | **A** |
| M-T-176-E1 | $t_1+t_2+t_3=3\pi+\alpha$，和 $=\frac{9\pi}8+\frac\alpha2$，$\alpha\in[\frac\pi4,\frac\pi2)$ | **$[\frac{5\pi}4,\frac{11\pi}8)$** |

## 本批最漂亮的一处：M-T-203-V1 用「判别式」定出最值

三高之积 $=\dfrac{8S^3}{abc}=\dfrac8{bc}$（因 $S=1$、$a=1$）。

由 $(1)$ 面积：$bc=\dfrac2{\sin A}$；由 $(2)$ 余弦定理 + $b^2+c^2\ge2bc$：

$$1=b^2+c^2-2bc\cos A\ge2bc(1-\cos A)\ \Longrightarrow\ \frac{4(1-\cos A)}{\sin A}\le1\ \Longrightarrow\ \tan\frac A2\le\frac14$$

**最值在等号处取到（此时 $b=c$，等腰）**，故 $\sin A=2\cdot\frac1{\sqrt{17}}\cdot\frac4{\sqrt{17}}=\dfrac8{17}$。

## M-T-341-V2 我自己算的弧（原书用了另一组记号）

圆 $(x-8)^2+y^2=16$ 与正方形 $[0,6]^2$ 的交：

- $y=0$ 时 $x=4$ ⟹ $E(4,0)$，相对圆心方向角 $180^\circ$
- $x=6$ 时 $y=2\sqrt3$ ⟹ $F(6,2\sqrt3)$，方向角 $120^\circ$

**圆心角 $=\frac\pi3$** ⟹ 弧长 $=4\cdot\frac\pi3=\frac{4\pi}3$ ✓
"""

T341_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知正方体 $ABCD-A_1B_1C_1D_1$ 的棱长为 $a$，定点 $M$ 在棱 $AB$ 上（但不在端点 $A,B$ 上），点 $P$ 是平面 $ABCD$ 内的动点，"
        r"且点 $P$ 到直线 $A_1D_1$ 的距离与点 $P$ 到点 $M$ 的距离的平方差为 $a^2$，则点 $P$ 的轨迹所在曲线为（　　）"
    ),
    'opts': [
        ('A', r"直线"),
        ('B', r"圆"),
        ('C', r"双曲线"),
        ('D', r"抛物线"),
    ],
    'answer': 'D',
    'analysis': (
        r"作 $PF\perp AD$、$PE\perp A_1D_1$。以 $A$ 为原点建系，设 $M(0,t,0)$（$0<t<a$）、$P(x,y,0)$。"
        r"由 $PF\perp$ 平面 $ADD_1A_1$ 得 $PE^2=y^2+a^2$、$PM^2=x^2+(y-t)^2$；"
        r"$PE^2-PM^2=a^2$ ⟹ $x^2=2ty-t^2$，为抛物线。"
    ),
    'solution': (
        r"作 $PF\perp AD$ 于 $F$，$PE\perp A_1D_1$ 于 $E$。以 $A$ 为原点建立空间直角坐标系，" "\n"
        r"设 $M(0,t,0)$（$0<t<a$）、$P(x,y,0)$。" "\n"
        r"由正方体的结构特征可知 $PF\perp$ 平面 $ADD_1A_1$，故 $PF\perp PE$ 且 $PF\perp$ 平面内的直线，" "\n"
        r"易证 $AD\perp$ 平面 $EFP$，于是 $\triangle EFP$ 为直角三角形，得" "\n"
        r"$PE^2=PF^2+EF^2=y^2+a^2$（其中 $EF$ 等于棱长 $a$，即 $P$ 到上底面的竖向距离相关的量）。" "\n"
        r"又 $PM^2=x^2+(y-t)^2$。" "\n"
        r"由条件 $PE^2-PM^2=a^2$：" "\n"
        r"$y^2+a^2-\left[x^2+(y-t)^2\right]=a^2$。" "\n"
        r"展开：$y^2+a^2-x^2-y^2+2ty-t^2=a^2$ ⟹ $-x^2+2ty-t^2=0$ ⟹ $x^2=2ty-t^2$。" "\n"
        r"这是关于 $x,y$ 的二次方程，其中 $x$ 为二次、$y$ 为一次 —— **标准抛物线方程**。" "\n"
        r"$\therefore P$ 的轨迹是抛物线。故选 D。"
    ),
    'review': (
        r"★ 题干、选项、答案、详解完整 ✓。原书详解：「作 $PF\perp AD$，$PE\perp A_1D_1$，垂足分别为 $F,E$。以 $A$ 为原点建立如下图所示的空间直角坐标系：设 $M(0,t,0)$，$0<t<a$，$P(x,y,0)$，由正方体结构特征可知，$PF\perp$ 平面 $ADD_1A_1$，易证 $AD\perp$ 平面 $EFP$，" "\n"
        r"$\therefore PE^2=y^2+a^2$，$PM^2=x^2+(y-t)^2$，$\therefore PE^2-PM^2=y^2+a^2-x^2-(y-t)^2=a^2$，整理得：$x^2=2ty-t^2$，$\therefore P$ 的轨迹是抛物线。故选：D.」" "\n"
        r"—— **坐标设定、$PE^2=y^2+a^2$、$PM^2=x^2+(y-t)^2$、整理得 $x^2=2ty-t^2$、抛物线、答案 D 全部一致** ✓✓✓" "\n"
        r"**独立验算（代数复核，完全独立）**：" "\n"
        r"① **展开验证**：$PE^2-PM^2=y^2+a^2-\left[x^2+(y-t)^2\right]$" "\n"
        r"$=y^2+a^2-x^2-\left(y^2-2ty+t^2\right)=a^2-x^2+2ty-t^2$。" "\n"
        r"令其等于 $a^2$ ⟹ $-x^2+2ty-t^2=0$ ⟹ $x^2=2ty-t^2=2t\left(y-\frac t2\right)$ ✓✓✓" "\n"
        r"② **曲线类型判定**：方程中 $x$ 是二次项、$y$ 是一次项，" "\n"
        r"且 $x^2$ 与 $y$ 的系数同号（$1$ 与 $2t>0$）—— **一个变量二次、另一个一次 ⟹ 抛物线** ✓✓✓" "\n"
        r"（若为椭圆则 $x^2,y^2$ 同号；若为双曲线则 $x^2,y^2$ 异号；**本题根本没有 $y^2$ 项**）" "\n"
        r"③ **几何意义**：这是「到定直线 $A_1D_1$ 的距离」与「到定点 $M$ 的距离」的**平方差**为常数。" "\n"
        r"平方差为定值 ⟹ 移项后恰能消去 $y^2$，剩 $x^2$ 与 $y$ 的一次关系 —— " "\n"
        r"**这正是抛物线的代数特征** ✓✓✓" "\n"
        r"④ **$t$ 的作用**：$0<t<a$ 保证 $2t\ne0$（否则退化为 $x^2=-t^2<0$，无轨迹）。" "\n"
        r"$M$ 不在端点（$t\ne0,a$）保证了 $t$ 严格大于 $0$ ✓✓✓" "\n"
        r"⑤ **选项排除**：轨迹不是直线（有 $x^2$ 项）、不是圆/双曲线（无 $y^2$ 项）✓✓✓" "\n"
        r"**答案 D 正确** ✓" "\n"
        r"**⭐⭐ 通法（动点轨迹：建系 + 消元）**：" "\n"
        r"① ⭐⭐ **「到直线的距离」要先作出垂线段，再用勾股表示**：" "\n"
        r"本题 $PE^2=PF^2+EF^2$，关键在于证明 $PF\perp$ 平面 $ADD_1A_1$（**线面垂直 ⟹ 垂直于面内一切直线**）；" "\n"
        r"② ⭐⭐ **把条件翻译成坐标方程后，看「哪些项被消掉」**：" "\n"
        r"本题 $y^2$ 与 $a^2$ 同时抵消 —— **抵消得越干净，曲线类型越容易判**；" "\n"
        r"③ ⭐⭐ **判定口诀（缺项法）**：" "\n"
        r"· **只有 $x^2$（无 $y^2$）或只有 $y^2$** ⟹ **抛物线**" "\n"
        r"· **$x^2,y^2$ 系数同号** ⟹ 椭圆（相等则圆）" "\n"
        r"· **$x^2,y^2$ 系数异号** ⟹ 双曲线" "\n"
        r"**这是最快的判别法，比记忆标准方程更快**；" "\n"
        r"④ ⚠ **「平方差」与「差」不同**：" "\n"
        r"若条件是「距离之差为常数」则是双曲线的一支；**本题是「平方差」**，化简后是抛物线 —— 别看错；" "\n"
        r"⑤ ⚠ **参数 $t$ 的取值范围决定轨迹是否退化**：" "\n"
        r"$t=0$ 时 $M=A$，方程退化为 $x^2=0$（一条直线）；本题明确排除端点 ✓"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-341'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-341-E1',
}

T341_V1 = {
    'type': '选择',
    'stem_text': (
        r"如图，在正方体 $ABCD-A_1B_1C_1D_1$ 中，$E$ 是棱 $CC_1$ 的中点，$F$ 是侧面 $B_1BCC_1$ 上的动点，并且 $A_1F\parallel$ 平面 $AED_1$，则动点 $F$ 的轨迹是（　　）"
    ),
    'opts': [
        ('A', r"圆"),
        ('B', r"椭圆"),
        ('C', r"抛物线"),
        ('D', r"线段"),
    ],
    'answer': 'D',
    'analysis': (
        r"以 $A$ 为原点建系（棱长 $1$），平面 $AED_1$ 的法向量为 $(0.5,-1,1)$。设 $F=(1,y,z)$（在面 $x=1$ 上），"
        r"$A_1F\parallel$ 平面 $AED_1$ 即 $\vec{A_1F}\cdot\vec n=0$ ⟹ $z=y+\frac12$，配合 $y\in[0,\frac12]$ 得一条线段。"
    ),
    'solution': (
        r"以 $A$ 为原点建立空间直角坐标系，设棱长为 $1$：" "\n"
        r"$A(0,0,0)$、$B(1,0,0)$、$C(1,1,0)$、$D(0,1,0)$、$A_1(0,0,1)$、$B_1(1,0,1)$、$C_1(1,1,1)$、$D_1(0,1,1)$。" "\n"
        r"$E$ 是 $CC_1$ 的中点 ⟹ $\vec{E}=(1,1,\frac12)$。" "\n"
        r"$\vec{AE}=(1,1,\frac12)$，$\vec{AD_1}=(0,1,1)$。" "\n"
        r"平面 $AED_1$ 的法向量 $\vec n=\vec{AE}\times\vec{AD_1}$" "\n"
        r"$=\left(1\cdot1-\frac12\cdot1,\ \frac12\cdot0-1\cdot1,\ 1\cdot1-1\cdot0\right)=\left(\frac12,-1,1\right)$。" "\n"
        r"（为方便可取 $\vec n=(1,-2,2)$。）" "\n"
        r"侧面 $B_1BCC_1$ 即平面 $x=1$，设 $F=(1,y,z)$（$y,z\in[0,1]$）。" "\n"
        r"$\vec{A_1F}=F-A_1=(1,y,z-1)$。" "\n"
        r"$A_1F\parallel$ 平面 $AED_1$ ⟺ $\vec{A_1F}\perp\vec n$ ⟺ $\vec{A_1F}\cdot\vec n=0$：" "\n"
        r"$1\cdot\frac12+y\cdot(-1)+(z-1)\cdot1=0$ ⟹ $\frac12-y+z-1=0$ ⟹ $z=y+\frac12$。" "\n"
        r"结合 $y\in[0,1]$、$z\in[0,1]$：$z=y+\frac12\in[\frac12,\frac32]\cap[0,1]$ ⟹ $z\in[\frac12,1]$ ⟹ $y\in[0,\frac12]$。" "\n"
        r"$\therefore F$ 的轨迹是从 $\left(1,0,\frac12\right)$ 到 $\left(1,\frac12,1\right)$ 的**线段**" "\n"
        r"（分别是 $BB_1$ 的中点与 $B_1C_1$ 的中点）。故选 D。"
    ),
    'review': (
        r"★ 题干、选项、答案、详解完整 ✓。原书详解：「取棱 $BB_1$ 的中点 $N$，棱 $B_1C_1$ 的中点（记为 $M$），则 $MN\parallel BC_1$，$\because BC_1\parallel AD_1$，$\therefore MN\parallel AD_1$，$\because MN\not\subset$ 平面 $AED_1$，$AD_1\subset$ 平面 $AED_1$，$\therefore MN\parallel$ 平面 $AED_1$，" "\n"
        r"同理，$A_1N\parallel$ 平面 $AED_1$，$\because MN\cap A_1N=N$，$\therefore$ 平面 $A_1NM\parallel$ 平面 $AED_1$，$\because F$ 是侧面 $B_1BCC_1$ 上的动点，$\therefore F$ 是线段 $MN$ 上的点时，$A_1F\parallel$ 平面 $AED_1$，故选：D」" "\n"
        r"—— **取 $BB_1$ 中点 $N$、$B_1C_1$ 中点 $M$、$MN\parallel BC_1\parallel AD_1$、平面 $A_1NM\parallel$ 平面 $AED_1$、$F$ 在线段 $MN$ 上、答案 D 全部一致** ✓✓✓" "\n"
        r"**独立验算（坐标法，完全独立）**：" "\n"
        r"① **法向量计算**：$\vec{AE}\times\vec{AD_1}=\begin{vmatrix}\vec i&\vec j&\vec k\\1&1&\frac12\\0&1&1\end{vmatrix}$" "\n"
        r"$=\vec i\left(1\cdot1-\frac12\cdot1\right)-\vec j\left(1\cdot1-\frac12\cdot0\right)+\vec k\left(1\cdot1-1\cdot0\right)=\left(\frac12,-1,1\right)$ ✓✓✓" "\n"
        r"② **代入验证**：取 $A(0,0,0)$ 代入平面方程 $\frac12x-y+z=0$ ✓；" "\n"
        r"取 $E(1,1,\frac12)$：$\frac12-1+\frac12=0$ ✓；取 $D_1(0,1,1)$：$0-1+1=0$ ✓ ✓✓✓ **三点都在平面上**" "\n"
        r"③ **$F$ 的轨迹方程**：$\vec{A_1F}\cdot\vec n=0$ ⟹ $\frac12-y+(z-1)=0$ ⟹ $z=y+\frac12$ ✓✓✓" "\n"
        r"④ **端点确定**：" "\n"
        r"· $y=0$：$z=\frac12$ ⟹ $F=(1,0,\frac12)$ = **$BB_1$ 的中点**（$B(1,0,0)$、$B_1(1,0,1)$）✓✓✓" "\n"
        r"· $y=\frac12$：$z=1$ ⟹ $F=(1,\frac12,1)$ = **$B_1C_1$ 的中点**（$B_1(1,0,1)$、$C_1(1,1,1)$）✓✓✓" "\n"
        r"（$y>\frac12$ 时 $z>1$，超出侧面范围）" "\n"
        r"⑤ **验证 $N=(1,0,\frac12)$ 确实满足**：$\vec{A_1N}=(1,0,-\frac12)$。" "\n"
        r"$\vec{A_1N}\cdot\vec n=1\cdot\frac12+0\cdot(-1)+(-\frac12)\cdot1=\frac12-\frac12=0$ ✓✓✓ **平行于平面**" "\n"
        r"⑥ **验证 $M=(1,\frac12,1)$ 确实满足**：$\vec{A_1M}=(1,\frac12,0)$。" "\n"
        r"$\vec{A_1M}\cdot\vec n=\frac12-\frac12+0=0$ ✓✓✓ **平行于平面**" "\n"
        r"⑦ **为什么是线段不是直线**：$F$ 被限制在**侧面**（有界区域）上 ⟹ 轨迹是平面与该侧面的交线段 ✓✓✓" "\n"
        r"**答案 D 正确** ✓" "\n"
        r"**⭐⭐ 通法（线面平行 ⟹ 动点轨迹）**：" "\n"
        r"① ⭐⭐ **「线 $\parallel$ 平面」翻译成「方向向量 $\perp$ 法向量」**：" "\n"
        r"$\vec{A_1F}\cdot\vec n=0$ —— **一个方程、两个未知量 ⟹ 轨迹是一条直线**（再与所在面的范围相交得线段）；" "\n"
        r"② ⭐⭐ **坐标法比「找平行平面」更稳**：" "\n"
        r"原书用「构造平面 $A_1NM\parallel$ 平面 $AED_1$」的几何法，需要找到 $M,N$ 两个特殊点；" "\n"
        r"**坐标法直接解出轨迹方程，不依赖几何直觉** —— 尤其当特殊点不容易猜时；" "\n"
        r"③ ⭐ **「平面与有界面的交」必是线段（或线段并）**：" "\n"
        r"**平面是无限的，但动点被限制在面（如正方形侧面）内** ⟹ 答案几乎总是「线段」；" "\n"
        r"④ ⚠ **别忘了求端点**：" "\n"
        r"解出 $z=y+\frac12$ 后必须用 $y,z\in[0,1]$ 截出范围 —— **这一步不做就不知道轨迹有多长**；" "\n"
        r"⑤ ⚠ **法向量叉乘的符号要仔细**：" "\n"
        r"$(a_1,a_2,a_3)\times(b_1,b_2,b_3)=\left(a_2b_3-a_3b_2,\ a_3b_1-a_1b_3,\ a_1b_2-a_2b_1\right)$。" "\n"
        r"**中间分量是 $a_3b_1-a_1b_3$（不是 $a_1b_3-a_3b_1$）** —— 这是叉乘最常见的错误。"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-341'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-341-V1',
}

T341_V2 = {
    'type': '填空',
    'stem_text': (
        r"在棱长为 $6$ 的正方体 $ABCD-A_1B_1C_1D_1$ 中，点 $M$ 是线段 $BC$ 的中点，$P$ 是正方体面 $DCC_1D_1$（包括边界）上的动点，"
        r"且满足 $\angle APD=\angle MPC$，则 $P$ 点的轨迹周长为 ____。"
    ),
    'opts': [],
    'answer': r"$\dfrac{4\pi}3$",
    'analysis': (
        r"由 $AD\perp$ 平面 $DCC_1D_1$、$MC\perp$ 平面 $DCC_1D_1$ 且 $\angle APD=\angle MPC$ 得 $\mathrm{Rt}\triangle ADP\sim\mathrm{Rt}\triangle MCP$ ⟹ $PD=2PC$。"
        r"建系得 $(x-8)^2+y^2=16$，与正方形交得圆心角 $\frac\pi3$ 的弧，弧长 $=\frac{4\pi}3$。"
    ),
    'solution': (
        r"$\because AD\perp$ 平面 $DCC_1D_1$，$MC\perp$ 平面 $DCC_1D_1$，而 $DP,CP$ 都在平面 $DCC_1D_1$ 内，" "\n"
        r"$\therefore AD\perp DP$，$MC\perp CP$。" "\n"
        r"又 $\angle APD=\angle MPC$，$\therefore \mathrm{Rt}\triangle ADP\sim \mathrm{Rt}\triangle MCP$。" "\n"
        r"$\therefore\dfrac{PD}{PC}=\dfrac{AD}{MC}$。其中 $AD=6$（棱长），$MC=\dfrac{BC}2=3$ ⟹ $\dfrac{PD}{PC}=\dfrac63=2$，即 $PD=2PC$。" "\n"
        r"在平面 $DCC_1D_1$ 内，以 $D$ 为原点、$DC$ 为 $x$ 轴、$DD_1$ 为 $y$ 轴建系：" "\n"
        r"$D(0,0)$、$C(6,0)$，设 $P(x,y)$。" "\n"
        r"$PD^2=x^2+y^2$，$PC^2=(x-6)^2+y^2$。由 $PD=2PC$：" "\n"
        r"$x^2+y^2=4\left[(x-6)^2+y^2\right]=4x^2-48x+144+4y^2$。" "\n"
        r"整理：$3x^2-48x+144+3y^2=0$ ⟹ $x^2-16x+48+y^2=0$ ⟹ $(x-8)^2+y^2=16$。" "\n"
        r"即圆心 $(8,0)$、半径 $r=4$ 的圆。$P$ 的轨迹是**该圆与正方形 $DCC_1D_1$（即 $0\le x\le6$、$0\le y\le6$）的交集**。" "\n"
        r"**求交点：**" "\n"
        r"· 在 $y=0$（即 $DC$ 边）上：$(x-8)^2=16$ ⟹ $x=4$ 或 $x=12$（舍），得 $E(4,0)$。" "\n"
        r"· 在 $x=6$（即 $CC_1$ 边）上：$(6-8)^2+y^2=16$ ⟹ $y^2=12$ ⟹ $y=2\sqrt3$，得 $F(6,2\sqrt3)$。" "\n"
        r"**求圆心角：** 圆心 $O(8,0)$。" "\n"
        r"$\vec{OE}=(-4,0)$，方向角 $180^\circ$；$\vec{OF}=(-2,2\sqrt3)$，方向角 $120^\circ$。" "\n"
        r"$\therefore\angle EOF=60^\circ=\dfrac\pi3$。" "\n"
        r"由弧长公式：$\overset{\frown}{EF}=r\cdot\theta=4\cdot\dfrac\pi3=\dfrac{4\pi}3$。" "\n"
        r"$\therefore P$ 点的轨迹周长为 $\dfrac{4\pi}3$。（**注**：轨迹为一段圆弧，其「周长」即该弧的弧长。）"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书详解：「则 $AD\perp$ 平面 $DCC_1D_1$，$MC\perp$ 平面 $DCC_1D_1$，又 $DP,PC$ 在平面 $DCC_1D_1$ 上，$\therefore AD\perp DP$，$MC\perp CP$，又 $\angle APD=\angle MPC$，$\therefore \mathrm{Rt}\triangle ADP\sim\mathrm{Rt}\triangle MCP$，" "\n"
        r"$\therefore\frac{PD}{PC}=\frac{AD}{MC}=2$，即 $PD=2PC$。在平面 $DCC_1D_1$ 中，以 $D$ 为原点，$DC,DD_1$ 分别为 $x,y$ 轴建立平面直角坐标系，则 $D(0,0)$，$C(6,0)$，$P(x,y)$，由 $PD=2PC$，知 $\sqrt{(x-0)^2+(y-0)^2}=2\sqrt{(x-6)^2+(y-0)^2}$，" "\n"
        r"化简整理得 $(x-8)^2+y^2=16$，$0\le x\le6$，圆心 $(8,0)$，半径 $r=4$ 的圆，所以 $P$ 点的轨迹为圆 $(x-8)^2+y^2=16$ 与四边形 $DCC_1D_1$ 的交点，即为图中的 $\overset{\frown}{EF}$。" "\n"
        r"其中，$CM=2$，$FM=4$，则 $\angle FMC=\frac\pi3$，由弧长公式知 $\overset{\frown}{EF}=\frac\pi3\times4=\frac{4\pi}3$。故答案为：$\frac{4\pi}3$.」" "\n"
        r"—— **相似比 $2$、$(x-8)^2+y^2=16$、圆心 $(8,0)$ 半径 $4$、$\frac{4\pi}3$ 全部一致** ✓✓✓" "\n"
        r"（原书用 $CM=2$、$FM=4$、$\angle FMC=\frac\pi3$ 求圆心角；**我用方向角直接算，结果相同**，见下）" "\n"
        r"**独立验算（坐标法，完全独立）**：" "\n"
        r"① **相似比**：$AD=6$（正方体棱长），$M$ 是 $BC$ 中点 ⟹ $MC=3$。$\frac{AD}{MC}=\frac63=2$ ✓✓✓" "\n"
        r"② **$PD=2PC$ 的代数展开**：$x^2+y^2=4[(x-6)^2+y^2]$" "\n"
        r"$x^2+y^2=4x^2-48x+144+4y^2$ ⟹ $0=3x^2-48x+144+3y^2$ ⟹ $x^2-16x+48+y^2=0$。" "\n"
        r"配方：$(x-8)^2-64+48+y^2=0$ ⟹ $(x-8)^2+y^2=16$ ✓✓✓" "\n"
        r"③ **轨迹与正方形的交**：" "\n"
        r"· $y=0$：$(x-8)^2=16$ ⟹ $x=4$（在 $[0,6]$ 内 ✓）或 $x=12$（超出 ✗）⟹ $E(4,0)$ ✓✓✓" "\n"
        r"· $x=6$：$4+y^2=16$ ⟹ $y=\sqrt{12}=2\sqrt3=3.4641$（在 $[0,6]$ 内 ✓）⟹ $F(6,2\sqrt3)$ ✓✓✓" "\n"
        r"· $x=0$：$64+y^2=16$ 无解（圆与 $DD_1$ 边不相交）；$y=6$：$(x-8)^2=16-36<0$ 无解 ✓✓✓" "\n"
        r"**轨迹确实只是从 $E$ 到 $F$ 的一段弧**" "\n"
        r"④ **圆心角（我的算法）**：" "\n"
        r"$\vec{OE}=(4-8,0-0)=(-4,0)$ ⟹ 方向角 $=180^\circ$。" "\n"
        r"$\vec{OF}=(6-8,2\sqrt3-0)=(-2,2\sqrt3)$，$|\vec{OF}|=\sqrt{4+12}=4$ ✓（在圆上），" "\n"
        r"方向角 $=\arctan2(2\sqrt3,-2)=180^\circ-60^\circ=120^\circ$。" "\n"
        r"$\therefore$ 圆心角 $=180^\circ-120^\circ=60^\circ=\frac\pi3$ ✓✓✓" "\n"
        r"⑤ **弧长**：$4\times\frac\pi3=\frac{4\pi}3=4.188790$ ✓✓✓" "\n"
        r"⑥ **数值验证 $PD=2PC$**（取 $F$ 点）：$F=(6,2\sqrt3)$。" "\n"
        r"$PD=\sqrt{36+12}=\sqrt{48}=6.9282$；$PC=\sqrt{0+12}=\sqrt{12}=3.4641$。$PD/PC=2.0000$ ✓✓✓" "\n"
        r"取 $E=(4,0)$：$PD=4$，$PC=2$。$PD/PC=2$ ✓✓✓" "\n"
        r"**答案 $\frac{4\pi}3$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（「两角相等」⟹ 相似 ⟹ 阿波罗尼斯圆）**：" "\n"
        r"① ⭐⭐ **识别「两个直角三角形相似」**：" "\n"
        r"$AD\perp$ 面、$MC\perp$ 面 ⟹ 两个直角；再加一组锐角相等 ⟹ **相似成立**。" "\n"
        r"**「线面垂直 ⟹ 线线垂直」是构造直角的关键**；" "\n"
        r"② ⭐⭐ **$PD=k\,PC$（$k\ne1$）的轨迹是圆（阿波罗尼斯圆）**：" "\n"
        r"本题 $k=2$ ⟹ $(x-8)^2+y^2=16$。**一般地 $PA=k\,PB$ 的轨迹都是圆**，" "\n"
        r"可记住：$A(0,0)$、$B(d,0)$ 时圆心 $\left(\frac{k^2d}{k^2-1},0\right)$、半径 $\frac{kd}{|k^2-1|}$。" "\n"
        r"本题 $d=6,k=2$：圆心 $=\frac{4\cdot6}{3}=8$ ✓、半径 $=\frac{2\cdot6}{3}=4$ ✓ ✓✓✓ **公式完全吻合**" "\n"
        r"③ ⭐⭐ **轨迹要「与面的边界求交」**：" "\n"
        r"**圆是无限的，但 $P$ 被限制在正方形面内** ⟹ 必须逐条边求交点，确定是哪一段弧；" "\n"
        r"④ ⭐ **求圆心角用方向角 $\arctan2$ 最稳**：" "\n"
        r"$\vec{OE}$、$\vec{OF}$ 相对圆心的方向角之差即圆心角 —— **比找几何关系快且不易错**；" "\n"
        r"⑤ ⚠ **「轨迹周长」在此指弧长**（轨迹是一段弧，不是封闭图形）—— 别去加直径；" "\n"
        r"⑥ ⚠ **$AD=6$ 是棱长，$MC=3$ 是半条棱**：" "\n"
        r"**相似比 $=\frac{AD}{MC}=2$** —— 注意两个量来自不同的几何对象，别都用 $6$。"
    ),
    'difficulty': 0.93,
    'topics': ['M-T-341'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-341-V2',
}

T341_V3 = {
    'type': '选择',
    'stem_text': (
        r"如图，正方体 $ABCD-A'B'C'D'$ 中，$M$ 为 $BC$ 边的中点，点 $P$ 在底面 $A'B'C'D'$ 和侧面 $CDD'C'$ 上运动并且使 $\angle MAC'=\angle PAC'$，那么点 $P$ 的轨迹是（　　）"
    ),
    'opts': [
        ('A', r"两段圆弧"),
        ('B', r"两段椭圆弧"),
        ('C', r"两段双曲线弧"),
        ('D', r"两段抛物线弧"),
    ],
    'answer': 'C',
    'analysis': (
        r"$P$ 的轨迹是以 $A$ 为顶点、$AC'$ 为轴、半顶角 $\angle MAC'$ 的正圆锥面与两个平面的交线。"
        r"$\cos\angle MAC'=\frac{\sqrt{15}}5\approx0.7746$，而 $AC'$ 与底面夹角 $\theta$ 满足 $\cos\theta=\frac{\sqrt6}3\approx0.8165>\cos\angle MAC'$ ⟹ $\theta<$ 半顶角 ⟹ 双曲线。"
    ),
    'solution': (
        r"$P$ 点的轨迹实际是一个**正圆锥面**和两个平面的交线；这个正圆锥面的中心轴即为 $AC'$，顶点为 $A$，顶角的一半即为 $\angle MAC'$。" "\n"
        r"以 $A'$ 点为坐标原点建立空间直角坐标系，设正方体棱长为 $1$：" "\n"
        r"$A(0,0,1)$、$C'(1,1,0)$、$M\left(\frac12,1,1\right)$。" "\n"
        r"$\vec{AC'}=(1,1,-1)$，$\vec{AM}=\left(\frac12,1,0\right)$。" "\n"
        r"$\lvert\vec{AC'}\rvert=\sqrt3$，$\lvert\vec{AM}\rvert=\sqrt{\frac14+1}=\dfrac{\sqrt5}2$。" "\n"
        r"$\cos\angle MAC'=\dfrac{\vec{AC'}\cdot\vec{AM}}{\lvert\vec{AC'}\rvert\lvert\vec{AM}\rvert}=\dfrac{1\cdot\frac12+1\cdot1+(-1)\cdot0}{\sqrt3\cdot\frac{\sqrt5}2}=\dfrac{\frac32}{\frac{\sqrt{15}}2}=\dfrac3{\sqrt{15}}=\dfrac{\sqrt{15}}5\approx0.7746$。" "\n"
        r"设 $AC'$ 与底面 $A'B'C'D'$ 所成的角为 $\theta$，则" "\n"
        r"$\cos\theta=\dfrac{\lvert A'C'\rvert}{\lvert AC'\rvert}=\dfrac{\sqrt2}{\sqrt3}=\dfrac{\sqrt6}3\approx0.8165$。" "\n"
        r"$\because\cos\theta=\dfrac{\sqrt6}3>\dfrac{\sqrt{15}}5=\cos\angle MAC'$（比较平方：$\frac69=\frac23>\frac{15}{25}=\frac35$），" "\n"
        r"$\therefore\theta<\angle MAC'$。" "\n"
        r"**即轴与平面的夹角小于半顶角** ⟹ 平面截圆锥面所得交线为**双曲线弧**。" "\n"
        r"同理，$P$ 在平面 $CDD'C'$ 上时，该平面与圆锥面的交线也是双曲线弧。" "\n"
        r"$\therefore$ 点 $P$ 的轨迹是两段双曲线弧。故选 C。"
    ),
    'review': (
        r"★ 题干、选项、答案、详解完整 ✓。原书详解：「$P$ 点的轨迹实际是一个正圆锥面和两个平面的交线；这个正圆锥面的中心轴即为 $AC'$，顶点为 $A$，顶角的一半即为 $\angle MAC'$。" "\n"
        r"以 $A'$ 点为坐标原点建立空间直角坐标系，设正方体的棱长为 $1$，则 $A(0,0,1)$，$C'(1,1,0)$，$M(\frac12,1,1)$，$\therefore\vec{AC'}=(1,1,-1)$，$\vec{AM}=(\frac12,1,0)$，" "\n"
        r"$\because\cos\angle MAC'=\frac{1\times\frac12+1\times1}{\sqrt3\times\sqrt{(\frac12)^2+1}}=\frac{\sqrt{15}}5$，设 $AC'$ 与底面 $A'B'C'D'$ 所成的角为 $\theta$，则 $\cos\theta=\frac{|A'C'|}{|AC'|}=\frac{\sqrt2}{\sqrt3}=\frac{\sqrt6}3>\frac{\sqrt{15}}5$，$\therefore\theta<\angle MAC'$，" "\n"
        r"$\therefore$ 该正圆锥面和底面 $A'B'C'D'$ 的交线是双曲线弧；同理可知，$P$ 点在平面 $CDD'C'$ 的交线是双曲线弧，故选：C.」" "\n"
        r"—— **圆锥面模型、$A(0,0,1)$、$C'(1,1,0)$、$M(\frac12,1,1)$、$\cos\angle MAC'=\frac{\sqrt{15}}5$、$\cos\theta=\frac{\sqrt6}3$、$\theta<\angle MAC'$、双曲线弧、答案 C 全部一致** ✓✓✓" "\n"
        r"（原书 OCR 中 $\frac{\sqrt{15}}5$ 被写成 `15 5`、`135 15` 等碎片，实为 $\frac{\sqrt{15}}5=\frac{\sqrt{135}}{15}$，我已还原）" "\n"
        r"**独立验算（数值比较，完全独立）**：" "\n"
        r"① **$\vec{AC'}\cdot\vec{AM}=1\cdot\frac12+1\cdot1+(-1)\cdot0=\frac32$** ✓✓✓" "\n"
        r"② **$|\vec{AC'}|=\sqrt{1+1+1}=\sqrt3=1.732051$**；**$|\vec{AM}|=\sqrt{\frac14+1}=\sqrt{1.25}=1.118034=\frac{\sqrt5}2$** ✓✓✓" "\n"
        r"③ **$\cos\angle MAC'=\frac{1.5}{1.732051\times1.118034}=\frac{1.5}{1.936492}=0.774597=\frac{\sqrt{15}}5$** ✓✓✓" "\n"
        r"（$\frac{\sqrt{15}}5=\frac{3.872983}5=0.774597$ ✓）" "\n"
        r"④ **$\cos\theta=\frac{|A'C'|}{|AC'|}$**：$A'=(0,0,0)$、$C'=(1,1,0)$ ⟹ $|A'C'|=\sqrt2=1.414214$。" "\n"
        r"$\frac{1.414214}{1.732051}=0.816497=\frac{\sqrt6}3$ ✓✓✓" "\n"
        r"（$\theta$ 是 $AC'$ 与底面 $A'B'C'D'$ 的夹角；$A$ 在底面的投影是 $A'$，故投影长为 $|A'C'|$，夹角余弦 $=\frac{|A'C'|}{|AC'|}$ ✓）" "\n"
        r"⑤ **比较大小（用平方避免误差）**：" "\n"
        r"$\cos^2\theta=\frac{6}9=\frac23=0.666667$；$\cos^2\angle MAC'=\frac{15}{25}=\frac35=0.6$。" "\n"
        r"$0.666667>0.6$ ⟹ $\cos\theta>\cos\angle MAC'$ ⟹ **$\theta<\angle MAC'$**（$\cos$ 在 $[0,\pi]$ 递减）✓✓✓" "\n"
        r"⑥ **圆锥曲线判定的关键定理**：" "\n"
        r"设圆锥半顶角为 $\alpha$、轴与截平面的夹角为 $\beta$：" "\n"
        r"· $\beta>\alpha$ ⟹ **椭圆**；$\beta=\alpha$ ⟹ **抛物线**；$\beta<\alpha$ ⟹ **双曲线**。" "\n"
        r"本题 $\beta=\theta<\alpha=\angle MAC'$ ⟹ **双曲线** ✓✓✓" "\n"
        r"（⚠ 这是我第二次遇到这个判据，第一次曾把它记错成「比较 $\alpha+\beta$ 与 $90^\circ$」—— **正确判据是永远比较 $\beta$ 与 $\alpha$**）" "\n"
        r"⑦ **为什么是「两段」**：$P$ 在**两个**平面（底面 $A'B'C'D'$ 与侧面 $CDD'C'$）上运动 ⟹ 每个面各一段弧 ⟹ 两段 ✓✓✓" "\n"
        r"**答案 C 正确** ✓" "\n"
        r"**⭐⭐ 通法（圆锥面截线：角度判据）**：" "\n"
        r"① ⭐⭐ **「$\angle PAC'=$ 定值」⟹ $P$ 在以 $AC'$ 为轴的正圆锥面上**：" "\n"
        r"**与一条直线成定角的点的轨迹是圆锥面** —— 这是识别模型的关键一步；" "\n"
        r"② ⭐⭐ **半顶角 $\alpha$、轴面夹角 $\beta$ 的判据（务必背准）**：" "\n"
        r"$\beta>\alpha$ ⟹ 椭圆；$\beta=\alpha$ ⟹ 抛物线；$\beta<\alpha$ ⟹ 双曲线。" "\n"
        r"⚠ **是 $\beta$ 与 $\alpha$ 比，不是 $\alpha+\beta$ 与 $90^\circ$ 比** —— 这个错误我犯过一次；" "\n"
        r"③ ⭐ **求 $\beta$（轴与面的夹角）**：" "\n"
        r"$\cos\beta=\dfrac{\text{轴线段在面上的投影长}}{\text{轴线段长}}$ —— **投影长 $\div$ 原长**，不是正弦；" "\n"
        r"④ ⭐ **求 $\alpha$（半顶角）用向量点积**：" "\n"
        r"$\cos\alpha=\dfrac{\vec{AC'}\cdot\vec{AM}}{|\vec{AC'}||\vec{AM}|}$ —— 其中 $M$ 是任一给「定角」的参考点；" "\n"
        r"⑤ ⚠ **比较两个余弦时建议比平方**：" "\n"
        r"$\frac69$ vs $\frac{15}{25}$ ⟹ $0.6667$ vs $0.6$ —— **比平方可以避免开方误差**；" "\n"
        r"⑥ ⚠ **「两段」的来源要看清动点在几个面上**：" "\n"
        r"本题是两个面 ⟹ 两段；若只在一个面上则是一段。"
    ),
    'difficulty': 0.95,
    'topics': ['M-T-341'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-341-V3',
}

T375_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知双曲线 $C:\dfrac{x^2}{a^2}-\dfrac{y^2}{b^2}=1$（$a>0,b>0$）的左、右焦点分别是 $F_1,F_2$，点 $P$ 是双曲线 $C$ 右支上异于顶点的点，"
        r"点 $H$ 在直线 $x=a$ 上，且满足 $\vec{PH}=\lambda\left(\dfrac{\vec{PF_1}}{\lvert\vec{PF_1}\rvert}+\dfrac{\vec{PF_2}}{\lvert\vec{PF_2}\rvert}\right)$，$\lambda\in\mathbb R$。若 $5\vec{HP}+4\vec{HF_2}+3\vec{HF_1}=\vec0$，则双曲线 $C$ 的离心率为（　　）"
    ),
    'opts': [
        ('A', r"$3$"),
        ('B', r"$4$"),
        ('C', r"$5$"),
        ('D', r"$6$"),
    ],
    'answer': 'C',
    'analysis': (
        r"$\vec{PH}$ 沿两单位向量之和 ⟹ $H$ 在 $\angle F_1PF_2$ 的平分线上；又 $H$ 在 $x=a$ 上 ⟹ $H$ 是 $\triangle PF_1F_2$ 的内心。"
        r"由奔驰定理 $5:4:3=S_{\triangle HF_1F_2}:S_{\triangle HF_1P}:S_{\triangle HF_2P}$ ⟹ $|F_1F_2|:|PF_1|:|PF_2|=5:4:3$ ⟹ $e=5$。"
    ),
    'solution': (
        r"由 $\vec{PH}=\lambda\left(\dfrac{\vec{PF_1}}{\lvert\vec{PF_1}\rvert}+\dfrac{\vec{PF_2}}{\lvert\vec{PF_2}\rvert}\right)$，两个单位向量之和的方向即 $\angle F_1PF_2$ 的平分线方向，" "\n"
        r"$\therefore$ 点 $H$ 在 $\angle F_1PF_2$ 的**角平分线**上。" "\n"
        r"又点 $H$ 在直线 $x=a$ 上。对双曲线，$\triangle PF_1F_2$ 中 $\angle F_1PF_2$ 的平分线与直线 $x=a$ 的交点即**旁心/内心**，" "\n"
        r"结合 $H$ 在三角形内部可知 **$H$ 是 $\triangle PF_1F_2$ 的内心**。" "\n"
        r"由 $5\vec{HP}+4\vec{HF_2}+3\vec{HF_1}=\vec0$，套用**奔驰定理**（若 $P$ 为 $\triangle ABC$ 内一点，则 $S_{\triangle PBC}\cdot\vec{PA}+S_{\triangle PAC}\cdot\vec{PB}+S_{\triangle PAB}\cdot\vec{PC}=\vec0$）：" "\n"
        r"$S_{\triangle HF_1F_2}:S_{\triangle HF_2P}:S_{\triangle HF_1P}=5:4:3$。" "\n"
        r"设内切圆半径为 $r$，则" "\n"
        r"$S_{\triangle HF_1F_2}=\frac12\lvert F_1F_2\rvert r$，$S_{\triangle HF_2P}=\frac12\lvert PF_2\rvert r$，$S_{\triangle HF_1P}=\frac12\lvert PF_1\rvert r$。" "\n"
        r"$\therefore\lvert F_1F_2\rvert:\lvert PF_2\rvert:\lvert PF_1\rvert=5:4:3$。" "\n"
        r"设 $\lvert F_1F_2\rvert=5\mu$、$\lvert PF_2\rvert=4\mu$、$\lvert PF_1\rvert=3\mu$ —— **注意这里 $PF_1<PF_2$ 与右支矛盾**，" "\n"
        r"故正确对应为 $\lvert PF_1\rvert=4\mu$、$\lvert PF_2\rvert=3\mu$（$P$ 在右支，$PF_1>PF_2$）。" "\n"
        r"于是 $\lvert F_1F_2\rvert=2c=5\mu$ ⟹ $c=\dfrac{5\mu}2$；" "\n"
        r"由双曲线定义 $\lvert PF_1\rvert-\lvert PF_2\rvert=2a=4\mu-3\mu=\mu$ ⟹ $a=\dfrac\mu2$。" "\n"
        r"$\therefore e=\dfrac ca=\dfrac{5\mu/2}{\mu/2}=5$。故选 C。"
    ),
    'review': (
        r"★ 题干、选项、答案、详解完整 ✓。原书详解：「由 $\vec{PH}=\lambda\left(\frac{\vec{PF_1}}{|\vec{PF_1}|}+\frac{\vec{PF_2}}{|\vec{PF_2}|}\right)$，$\lambda\in\mathbb R$，则点 $H$ 在 $\angle F_1PF_2$ 的角平分线上，由点 $H$ 在直线 $x=a$ 上，则 $H$ 是 $\triangle PF_1F_2$ 的内心。" "\n"
        r"由 $5\vec{HP}+4\vec{HF_2}+3\vec{HF_1}=\vec0$，由奔驰定理（已知 $P$ 为 $\triangle ABC$ 内一点，则有 $S_{\triangle PBC}\cdot\vec{PA}+S_{\triangle PAC}\cdot\vec{PB}+S_{\triangle PAB}\cdot\vec{PC}=\vec0$）知，$S_{\triangle HF_1F_2}:S_{\triangle HF_1P}:S_{\triangle HF_2P}=5:4:3$，" "\n"
        r"即 $\frac12|F_1F_2|\cdot r:\frac12|PF_1|\cdot r:\frac12|PF_2|\cdot r=5:4:3$，则 $|F_1F_2|:|PF_1|:|PF_2|=5:4:3$。设 $|F_1F_2|=5\lambda$，$|PF_1|=4\lambda$，$|PF_2|=3\lambda$，" "\n"
        r"则 $|F_1F_2|=2c=5\lambda\Rightarrow c=\frac{5\lambda}2$，$|PF_1|-|PF_2|=2a=\lambda\Rightarrow a=\frac\lambda2$，则 $e=\frac ca=5$。故选：C」" "\n"
        r"—— **内心判定、奔驰定理、$5:4:3$、$c=\frac{5\lambda}2$、$a=\frac\lambda2$、$e=5$、答案 C 全部一致** ✓✓✓" "\n"
        r"**独立验算（完全独立）**：" "\n"
        r"① **奔驰定理核对系数对应关系**：" "\n"
        r"$5\vec{HP}+4\vec{HF_2}+3\vec{HF_1}=\vec0$ ⟹ $S_{\triangle H F_1F_2}$ 配 $\vec{HP}$（系数 $5$），" "\n"
        r"$S_{\triangle HF_1P}$ 配 $\vec{HF_2}$（系数 $4$），$S_{\triangle HF_2P}$ 配 $\vec{HF_1}$（系数 $3$）✓✓✓" "\n"
        r"（**配 $\vec{HX}$ 的系数对应「去掉 $X$ 的那三个点」构成的三角形面积**）" "\n"
        r"② **面积比 ⟹ 边长比**：三个小三角形的高都是内切圆半径 $r$ ⟹ 面积比 $=$ 底边长比 ✓✓✓" "\n"
        r"③ **$P$ 在右支的自洽性**：$|PF_1|=4\mu>|PF_2|=3\mu$ ✓；$|PF_1|-|PF_2|=\mu=2a>0$ ✓ ✓✓✓" "\n"
        r"④ **$e=5$ 代入完整检查**：取 $\mu=2$ ⟹ $a=1$、$c=5$、$b^2=c^2-a^2=24$。" "\n"
        r"$|PF_1|=8$、$|PF_2|=6$、$|F_1F_2|=10$。检验三角形：$8^2+6^2=64+36=100=10^2$ ⟹ **直角三角形** ✓" "\n"
        r"$P$ 在右支且 $|PF_1|-|PF_2|=2=2a$ ✓ ✓✓✓ **完全自洽**" "\n"
        r"⑤ **选项排除**：$e=3,4,6$ 都不能同时满足这些比例 ✓✓✓" "\n"
        r"**答案 C 正确** ✓" "\n"
        r"**⭐⭐ 通法（奔驰定理 + 内心）**：" "\n"
        r"① ⭐⭐ **识别内心**：" "\n"
        r"$\vec{PH}$ 沿 $\frac{\vec{PF_1}}{|\vec{PF_1}|}+\frac{\vec{PF_2}}{|\vec{PF_2}|}$（**两个单位向量之和**）⟹ 角平分线。" "\n"
        r"**「单位向量之和 = 角平分线方向」是标准结论**；" "\n"
        r"② ⭐⭐ **双曲线中 $\angle F_1PF_2$ 的平分线与 $x=a$ 的交点 ⟹ 内心/旁心**：" "\n"
        r"这是本题的隐含条件，**$x=a$ 这条直线正是内心的横坐标所在**；" "\n"
        r"③ ⭐⭐ **奔驰定理（重心坐标的向量形式）**：" "\n"
        r"$S_{\triangle PBC}\vec{PA}+S_{\triangle PAC}\vec{PB}+S_{\triangle PAB}\vec{PC}=\vec0$。" "\n"
        r"**系数 = 与该顶点相对的三角形面积**。记忆法：**配 $\vec{PX}$ 的系数对应「不含 $X$」的面积**；" "\n"
        r"④ ⭐⭐ **三个小三角形面积比 = 底边比**（高都是 $r$）：" "\n"
        r"**这一步把「向量系数」直接翻译成「三角形边长比」**，是本题的枢纽；" "\n"
        r"⑤ ⚠ **用双曲线定义定 $a$**：$|PF_1|-|PF_2|=2a$ —— " "\n"
        r"**别把 $PF_1,PF_2$ 的对应关系搞反**（$P$ 在右支时 $PF_1>PF_2$）；" "\n"
        r"⑥ ⚠ **$e=\frac ca$ 别漏掉 $2$**：$2c=5\mu$ ⟹ $c=\frac{5\mu}2$，$2a=\mu$ ⟹ $a=\frac\mu2$，比值恰好 $=5$ ✓"
    ),
    'difficulty': 0.94,
    'topics': ['M-T-375'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-375-E1',
}

T375_V2 = {
    'type': '选择',
    'stem_text': (
        r"椭圆 $C:\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$（$a>b>0$）的左、右焦点分别为 $F_1,F_2$，过 $F_1$ 的直线交 $C$ 于 $A,B$ 两点，"
        r"若 $\vec{OA}+2\vec{OB}=3\vec{OF_1}$，$\lvert AB\rvert=\lvert BF_2\rvert$，其中 $O$ 为坐标原点，则椭圆的离心率为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac13$"),
        ('B', r"$\dfrac12$"),
        ('C', r"$\dfrac{\sqrt3}3$"),
        ('D', r"$\dfrac{\sqrt3}2$"),
    ],
    'answer': 'C',
    'analysis': (
        r"$\vec{OF_1}=\frac13\vec{OA}+\frac23\vec{OB}$ ⟹ $F_1$ 内分 $AB$ 且 $BF_1:AF_1=1:2$。"
        r"设 $BF_1=a+ex_1$、$AF_1=a+ex_2$；由 $\lvert AB\rvert=\lvert BF_2\rvert$ 与定义得 $BF_1=\frac a2$ ⟹ $x_1=-\frac{a^2}{2c}$、$x_2=0$；"
        r"再由 $x$ 坐标 $-c=\frac23x_1$ 得 $3c^2=a^2$ ⟹ $e=\frac{\sqrt3}3$。"
    ),
    'solution': (
        r"由 $\vec{OA}+2\vec{OB}=3\vec{OF_1}$ 得 $\vec{OF_1}=\dfrac13\vec{OA}+\dfrac23\vec{OB}$。" "\n"
        r"因系数和 $\frac13+\frac23=1$，故 $F_1$ 在直线 $AB$ 上，且 $F_1$ 分 $AB$ 满足 $\vec{AF_1}=\dfrac23\vec{AB}$，" "\n"
        r"$\therefore\lvert AF_1\rvert:\lvert F_1B\rvert=2:1$，即 $\lvert BF_1\rvert=\dfrac12\lvert AF_1\rvert$。" "\n"
        r"设 $B(x_1,y_1)$、$A(x_2,y_2)$。由椭圆焦半径公式（左焦点）：" "\n"
        r"$\lvert BF_1\rvert=a+ex_1$，$\lvert AF_1\rvert=a+ex_2$。" "\n"
        r"由 $\lvert AF_1\rvert=2\lvert BF_1\rvert$：$a+ex_2=2(a+ex_1)$　(1)" "\n"
        r"由椭圆定义 $\lvert BF_1\rvert+\lvert BF_2\rvert=2a$ ⟹ $\lvert BF_2\rvert=2a-\lvert BF_1\rvert=2a-(a+ex_1)=a-ex_1$。" "\n"
        r"又 $\lvert AB\rvert=\lvert AF_1\rvert+\lvert BF_1\rvert$（$F_1$ 在 $AB$ 之间）$=(a+ex_2)+(a+ex_1)$，且 $\lvert AB\rvert=\lvert BF_2\rvert=a-ex_1$：" "\n"
        r"$2a+e(x_1+x_2)=a-ex_1$ ⟹ $a+ex_2+2ex_1=0$　(2)" "\n"
        r"(1) 代入 (2)：由 (1) $ex_2=a+2ex_1$，代入 (2)：$a+(a+2ex_1)+2ex_1=0$ ⟹ $2a+4ex_1=0$ ⟹ $x_1=-\dfrac a{2e}=-\dfrac{a^2}{2c}$。" "\n"
        r"代回 (1)：$ex_2=a+2e\left(-\dfrac a{2e}\right)=a-a=0$ ⟹ $x_2=0$。" "\n"
        r"**再用 $x$ 坐标关系：** 由 $\vec{OF_1}=\frac13\vec{OA}+\frac23\vec{OB}$ 取 $x$ 分量：" "\n"
        r"$-c=\dfrac13x_2+\dfrac23x_1=\dfrac13\cdot0+\dfrac23\left(-\dfrac{a^2}{2c}\right)=-\dfrac{a^2}{3c}$。" "\n"
        r"$\therefore c=\dfrac{a^2}{3c}$ ⟹ $3c^2=a^2$ ⟹ $e^2=\dfrac{c^2}{a^2}=\dfrac13$ ⟹ $e=\dfrac{\sqrt3}3$。故选 C。"
    ),
    'review': (
        r"★ 题干、选项、答案、详解完整 ✓。原书详解：「由题意，有 $\vec{OA}+2\vec{OB}=3\vec{OF_1}$，即 $\vec{OF_1}=\frac13\vec{OA}+\frac23\vec{OB}$，知 $\frac{BF_1}{AF_1}=\frac12$。" "\n"
        r"过左焦点 $F_1$ 的直线交 $C$ 于 $A,B$ 两点，令 $B(x_1,y_1)$，$A(x_2,y_2)$，有 $BF_1=a+ex_1$，$AF_1=a+ex_2$，且由上知 $AF_1=2BF_1=2(a+ex_1)$ ①。" "\n"
        r"又 $\because|AB|=|BF_2|$，有 $AB=BF_2$，且 $BF_1+BF_2=2a$，知：$AB=BF_2=a-ex_1$。$\therefore$ 由 $AB=BF_1+AF_1$ 知：$AF_1=-2ex_1$ ②，由①、②可知：$x_1=-\frac{a^2}{2c}$，$x_2=0$。" "\n"
        r"$\therefore$ 结合几何图形知：$\frac{OF_1}{|x_1|}=\frac23$，即 $e^2=\frac13$，得 $e=\frac{\sqrt3}3$。故选：C」" "\n"
        r"—— **$\frac{BF_1}{AF_1}=\frac12$、$BF_1=a+ex_1$、$x_1=-\frac{a^2}{2c}$、$x_2=0$、$e=\frac{\sqrt3}3$、答案 C 全部一致** ✓✓✓" "\n"
        r"（原书「$AF_1=-2ex_1$ ②」这一步我独立推出的是 $a+ex_2+2ex_1=0$，两者联立后结果一致，见下；" "\n"
        r"原书「$\frac{OF_1}{|x_1|}=\frac23$」即 $c\cdot\frac{2c}{a^2}=\frac{2c^2}{a^2}=\frac23$ ⟹ $e^2=\frac13$ ✓ 与我的算法等价）" "\n"
        r"**独立验算（代数 + 数值，完全独立）**：" "\n"
        r"① **分点比例**：$\vec{OF_1}=\frac13\vec{OA}+\frac23\vec{OB}$，系数和 $=1$ ⟹ $F_1$ 是 $A,B$ 的**内分点**。" "\n"
        r"$\vec{AF_1}=\vec{OF_1}-\vec{OA}=\frac23(\vec{OB}-\vec{OA})=\frac23\vec{AB}$ ⟹ $|AF_1|=\frac23|AB|$、$|F_1B|=\frac13|AB|$。" "\n"
        r"$\therefore|AF_1|:|F_1B|=2:1$ ⟹ $|BF_1|=\frac12|AF_1|$ ✓✓✓" "\n"
        r"② **联立求解**：" "\n"
        r"由 $AF_1=2BF_1$：$a+ex_2=2(a+ex_1)$ ⟹ $ex_2=a+2ex_1$。" "\n"
        r"由 $|AB|=|BF_2|$：$AB=AF_1+BF_1=3BF_1$（因 $AF_1=2BF_1$），而 $BF_2=2a-BF_1$。" "\n"
        r"$3BF_1=2a-BF_1$ ⟹ $4BF_1=2a$ ⟹ $BF_1=\frac a2$。" "\n"
        r"$\therefore a+ex_1=\frac a2$ ⟹ $ex_1=-\frac a2$ ⟹ $x_1=-\frac a{2e}=-\frac{a^2}{2c}$ ✓✓✓" "\n"
        r"$AF_1=2\cdot\frac a2=a$ ⟹ $a+ex_2=a$ ⟹ $x_2=0$ ✓✓✓" "\n"
        r"（**我的路径比原书更直接**：直接用 $AB=3BF_1$ 与定义联立，不必走 $AF_1=-2ex_1$ 那一步）" "\n"
        r"③ **$e$ 的求解**：由 $x$ 分量 $-c=\frac13x_2+\frac23x_1=\frac23\cdot(-\frac{a^2}{2c})=-\frac{a^2}{3c}$" "\n"
        r"⟹ $c=\frac{a^2}{3c}$ ⟹ $3c^2=a^2$ ⟹ $e^2=\frac13$ ⟹ $e=\frac{\sqrt3}3=0.577350$ ✓✓✓" "\n"
        r"④ **完整构造验证**：取 $a=\sqrt3$、$c=1$（则 $e=\frac1{\sqrt3}=\frac{\sqrt3}3$ ✓），$b^2=a^2-c^2=3-1=2$。" "\n"
        r"$x_1=-\frac{a^2}{2c}=-\frac32$，$x_2=0$。" "\n"
        r"$BF_1=a+ex_1=\sqrt3+\frac1{\sqrt3}(-\frac32)=\sqrt3-\frac{\sqrt3}2=\frac{\sqrt3}2$ ✓（$=\frac a2=\frac{\sqrt3}2$ ✓）" "\n"
        r"$AF_1=a+ex_2=\sqrt3+0=\sqrt3$ ✓（$=a$ ✓）" "\n"
        r"$AB=AF_1+BF_1=\sqrt3+\frac{\sqrt3}2=\frac{3\sqrt3}2$。" "\n"
        r"$BF_2=2a-BF_1=2\sqrt3-\frac{\sqrt3}2=\frac{3\sqrt3}2$ ✓✓✓ **$AB=BF_2$ 成立！**" "\n"
        r"⑤ **$A$ 点坐标**：$x_2=0$ ⟹ $A=(0,\pm b)=(0,\pm\sqrt2)$。" "\n"
        r"验证 $A$ 在椭圆上：$\frac03+\frac22=1$ ✓ ✓✓✓" "\n"
        r"⑥ **$F_1$ 在 $AB$ 上的验证**：$F_1=(-1,0)$。$A=(0,\sqrt2)$、$B=(-\frac32,y_1)$。" "\n"
        r"由 $\vec{OF_1}=\frac13\vec{OA}+\frac23\vec{OB}$：$(-1,0)=\frac13(0,\sqrt2)+\frac23(-\frac32,y_1)$。" "\n"
        r"$x$：$-1=0+\frac23(-\frac32)=-1$ ✓；$y$：$0=\frac{\sqrt2}3+\frac{2y_1}3$ ⟹ $y_1=-\frac{\sqrt2}2$。" "\n"
        r"验证 $B(-\frac32,-\frac{\sqrt2}2)$ 在椭圆上：$\frac{9/4}3+\frac{1/2}2=\frac34+\frac14=1$ ✓✓✓ **完美闭合**" "\n"
        r"**答案 C 正确** ✓" "\n"
        r"**⭐⭐ 通法（向量分点 + 焦半径公式）**：" "\n"
        r"① ⭐⭐ **系数和为 $1$ ⟹ 三点共线且给出分点比**：" "\n"
        r"$\vec{OP}=\alpha\vec{OA}+\beta\vec{OB}$ 且 $\alpha+\beta=1$ ⟹ $P$ 在 $AB$ 上，且 $\frac{|AP|}{|PB|}=\frac{\beta}{\alpha}$。" "\n"
        r"**记忆法：$\vec{OP}$ 中 $A$ 的系数 $\alpha$ 对应「对面的」$|PB|$**；" "\n"
        r"② ⭐⭐ **椭圆焦半径公式（左焦点 $F_1$）：$|PF_1|=a+ex$**；右焦点 $|PF_2|=a-ex$。" "\n"
        r"（$x=a$ 时 $|PF_1|=a+c$ ✓、$|PF_2|=a-c$ ✓）" "\n"
        r"⚠ **双曲线右支**：$|PF_1|=ex+a$、$|PF_2|=ex-a$（**符号与椭圆不同**）；" "\n"
        r"③ ⭐⭐ **把「弦长」拆成两段焦半径**：$AB=AF_1+BF_1$（**仅当 $F_1$ 在 $A,B$ 之间**）—— " "\n"
        r"这是用焦半径处理焦点弦的通用入口；" "\n"
        r"④ ⭐ **求 $e$ 时别忘了「$x$ 分量」这个隐藏方程**：" "\n"
        r"本题最关键的一步是取 $x$ 分量：$-c=\frac13x_2+\frac23x_1$ —— " "\n"
        r"**向量等式可以提供两个标量方程（$x$ 和 $y$），别只用了一个**；" "\n"
        r"⑤ ⚠ **$A,B$ 的命名要与 $x_1,x_2$ 对应好**：" "\n"
        r"原书 $B\to x_1$、$A\to x_2$，**别在代入时搞混**；" "\n"
        r"⑥ ⭐ **验算技巧：取 $a=\sqrt3,c=1$ 构造完整三角形/椭圆**：" "\n"
        r"**代入具体数值把整条链跑通**（$AB=BF_2$ 是否成立、点是否在椭圆上），" "\n"
        r"比只检查 $e$ 的值可靠得多。"
    ),
    'difficulty': 0.93,
    'topics': ['M-T-375'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-375-V2',
}

T375_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知双曲线 $C:\dfrac{x^2}{a^2}-\dfrac{y^2}{b^2}=1$（$a>0,b>0$）的虚轴的一个顶点为 $N(0,1)$，左顶点为 $M$，双曲线 $C$ 的左、右焦点分别为 $F_1,F_2$，"
        r"点 $P$ 为线段 $MN$ 上的动点，当 $\vec{PF_1}\cdot\vec{PF_2}$ 取得最小值和最大值时，$\triangle PF_1F_2$ 的面积分别为 $S_1,S_2$，若 $S_2=2S_1$，则双曲线 $C$ 的离心率为（　　）"
    ),
    'opts': [
        ('A', r"$\sqrt2$"),
        ('B', r"$2$"),
        ('C', r"$2\sqrt3$"),
        ('D', r"$2\sqrt5$"),
    ],
    'answer': 'A',
    'analysis': (
        r"由 $N(0,1)$ 得 $b=1$、$c^2=a^2+1$。设 $P\left(m,\frac{m+a}a\right)$（$m\in[-a,0]$），"
        r"$\vec{PF_1}\cdot\vec{PF_2}=\frac{(a^2+1)m^2+2am-a^4}{a^2}$，顶点 $m_0=-\frac a{a^2+1}\in[-a,0]$。"
        r"$S_1=\frac{a^2c}{a^2+1}$（最小处）、$S_2=c$（$m=0$ 处），由 $S_2=2S_1$ 得 $a=1$ ⟹ $e=\sqrt2$。"
    ),
    'solution': (
        r"由题意 $M(-a,0)$、$b=1$，则直线 $MN$ 的方程为 $y=\dfrac{x+a}a=\dfrac xa+1$。" "\n"
        r"$\because P$ 在线段 $MN$ 上，可设 $P\left(m,\dfrac{m+a}a\right)$，其中 $m\in[-a,0]$。" "\n"
        r"设焦距为 $2c$，则 $c^2=a^2+b^2=a^2+1$，$F_1(-c,0)$、$F_2(c,0)$。" "\n"
        r"$\vec{PF_1}=\left(-c-m,-\dfrac{m+a}a\right)$，$\vec{PF_2}=\left(c-m,-\dfrac{m+a}a\right)$。" "\n"
        r"$\vec{PF_1}\cdot\vec{PF_2}=(-c-m)(c-m)+\left(\dfrac{m+a}a\right)^2=(m^2-c^2)+\dfrac{(m+a)^2}{a^2}$。" "\n"
        r"展开并代入 $c^2=a^2+1$：" "\n"
        r"$=\dfrac{(a^2+1)m^2+2am+a^2}{a^2}-(a^2+1)=\dfrac{(a^2+1)m^2+2am-a^4}{a^2}$。" "\n"
        r"这是关于 $m$ 的开口向上的二次函数，对称轴为 $m_0=-\dfrac{a}{a^2+1}$。" "\n"
        r"$\because a^2+1>1$，$\therefore m_0\in(-a,0)$，故**最小值在 $m_0$ 处取到**。" "\n"
        r"此时 $P$ 的纵坐标 $y_1=\dfrac{m_0+a}a=1-\dfrac1{a^2+1}=\dfrac{a^2}{a^2+1}$，" "\n"
        r"$S_1=\dfrac12\cdot 2c\cdot y_1=\dfrac{a^2c}{a^2+1}$。" "\n"
        r"**最大值：** 端点比较。$m=-a$ 时 $y=0$（面积为 $0$，退化）；$m=0$ 时 $y=1$，$S=\dfrac12\cdot2c\cdot1=c$。" "\n"
        r"（当 $0<a\le1$ 时 $m_0\le-\frac a2$，最大值在 $m=0$ 处；本题解出 $a=1$ 恰满足此条件。）" "\n"
        r"$\therefore S_2=c$。由 $S_2=2S_1$：" "\n"
        r"$c=2\cdot\dfrac{a^2c}{a^2+1}$ ⟹ $a^2+1=2a^2$ ⟹ $a^2=1$ ⟹ $a=1$。" "\n"
        r"$\therefore c^2=a^2+1=2$，$c=\sqrt2$，$e=\dfrac ca=\sqrt2$。故选 A。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓；**选项文本在提取中根号丢失**（原为 `2`、`2 2`、`2 3`、`2 5`），我按推导结果 $e=\sqrt2$ 及常见干扰项还原为 $\sqrt2,2,2\sqrt3,2\sqrt5$。" "\n"
        r"原书详解：「由题意可知 $M(-a,0)$，$b=1$，则直线 $MN$ 所在直线的方程为 $y=\frac1ax+1$，因为点 $P$ 在线段 $MN$ 上，可设 $P(m,\frac{m+a}a)$，其中 $m\in[-a,0]$。" "\n"
        r"设双曲线 $C$ 的焦距为 $2c$，则 $c^2=a^2+1$，$F_1(-c,0)$，$F_2(c,0)$，从而 $\vec{PF_1}=(-c-m,-\frac{m+a}a)$，$\vec{PF_2}=(c-m,-\frac{m+a}a)$，" "\n"
        r"故 $\vec{PF_1}\cdot\vec{PF_2}=m^2-c^2+\frac{m^2+2am+a^2}{a^2}=\frac{a^2+1}{a^2}m^2+2am-a^4\cdot\frac1{a^2}$（提取为 `a2+ 1  m2+ 2am - a4 a2`）。因为 $m\in[-a,0]$，所以当 $m=-\frac a{a^2+1}$ 时，$\vec{PF_1}\cdot\vec{PF_2}$ 取得最小值，此时，$S_1=\frac12\times2c\left(\frac1a-\frac a{a^2+1}\cdot\frac1a\cdot a+1\right)$…（此段 OCR 破碎），$S_1=\frac{a^2c}{a^2+1}$。" "\n"
        r"当 $-\frac a{a^2+1}>-\frac a2$，即 $a>1$ 时，$\vec{PF_1}\cdot\vec{PF_2}$ 无最大值，所以 $a>1$ 不符合题意；当 $-\frac a{a^2+1}\le-\frac a2$，即 $0<a\le1$ 时，$\vec{PF_1}\cdot\vec{PF_2}$ 在 $m=0$ 处取得最大值，此时，$S_2=c$，因为 $S_2=2S_1$，所以 $c=2\times\frac{a^2c}{a^2+1}$…」" "\n"
        r"—— **$M(-a,0)$、$b=1$、$y=\frac xa+1$、$c^2=a^2+1$、点积表达式、$m_0=-\frac a{a^2+1}$、$S_1=\frac{a^2c}{a^2+1}$、$S_2=c$、$a=1$、$e=\sqrt2$、答案 A 全部一致** ✓✓✓" "\n"
        r"（原书「$a>1$ 时无最大值」的表述有误 —— **闭区间上二次函数必有最大值**；" "\n"
        r"其真实意图是排除 $a>1$ 的情形以保证 $S_2$ 落在 $m=0$ 处。我按 $S_2=c$ 计算，结论不变 ✓）" "\n"
        r"**独立验算（完全独立）**：" "\n"
        r"① **点积展开**：$(-c-m)(c-m)=-(c+m)(c-m)=-(c^2-m^2)=m^2-c^2$ ✓✓✓" "\n"
        r"② **合并**：$m^2-c^2+\frac{(m+a)^2}{a^2}=m^2-c^2+\frac{m^2+2am+a^2}{a^2}$" "\n"
        r"$=\frac{a^2m^2+2am+a^2}{a^2}+m^2-c^2=\frac{(a^2+1)m^2+2am+a^2}{a^2}-(a^2+1)$。" "\n"
        r"而 $\frac{a^2}{a^2}-(a^2+1)=1-a^2-1=-a^2=\frac{-a^4}{a^2}$ ✓" "\n"
        r"$\therefore$ 点积 $=\frac{(a^2+1)m^2+2am-a^4}{a^2}$ ✓✓✓ **与原书完全一致**" "\n"
        r"③ **对称轴**：$\frac{d}{dm}\left[(a^2+1)m^2+2am-a^4\right]=2(a^2+1)m+2a=0$ ⟹ $m_0=-\frac a{a^2+1}$ ✓✓✓" "\n"
        r"④ **$m_0\in[-a,0]$ 的验证**：$a^2+1>1$ ⟹ $|m_0|=\frac a{a^2+1}<a$ ⟹ $m_0>-a$ ✓；且 $m_0<0$ ✓ ✓✓✓" "\n"
        r"⑤ **$S_1$ 的纵坐标**：$y_1=\frac{m_0+a}a=\frac{-\frac a{a^2+1}+a}a=-\frac1{a^2+1}+1=\frac{a^2}{a^2+1}$ ✓✓✓" "\n"
        r"$S_1=\frac12\cdot(2c)\cdot y_1=\frac{a^2c}{a^2+1}$ ✓✓✓" "\n"
        r"⑥ **$S_2=c$ 的验证**（$m=0$）：$P=(0,1)$，即点 $N$。$S_2=\frac12\cdot2c\cdot1=c$ ✓✓✓" "\n"
        r"⑦ **解 $a$**：$c=\frac{2a^2c}{a^2+1}$ ⟹ $1=\frac{2a^2}{a^2+1}$ ⟹ $a^2+1=2a^2$ ⟹ $a^2=1$ ⟹ $a=1$ ✓✓✓" "\n"
        r"（满足原书要求的 $0<a\le1$ ✓）" "\n"
        r"⑧ **$e$ 的计算**：$c^2=a^2+1=2$ ⟹ $c=\sqrt2$；$e=\frac ca=\frac{\sqrt2}1=\sqrt2=1.414214$ ✓✓✓" "\n"
        r"⑨ **完整数值验证**（$a=1,b=1,c=\sqrt2$）：" "\n"
        r"$M(-1,0)$、$N(0,1)$、$F_1(-\sqrt2,0)$、$F_2(\sqrt2,0)$。" "\n"
        r"· $m_0=-\frac1{2}=-0.5$：$P=(-0.5,0.5)$。" "\n"
        r"$\vec{PF_1}=(-\sqrt2+0.5,-0.5)=(-0.914214,-0.5)$；$\vec{PF_2}=(\sqrt2+0.5,-0.5)=(1.914214,-0.5)$。" "\n"
        r"点积 $=(-0.914214)(1.914214)+0.25=-1.750000+0.25=-1.500000$。" "\n"
        r"公式：$\frac{(1+1)(0.25)+2(1)(-0.5)-1}{1}=\frac{0.5-1-1}{1}=-1.5$ ✓✓✓ **完全吻合**" "\n"
        r"· $m=0$：$P=(0,1)$。$\vec{PF_1}=(-\sqrt2,-1)$、$\vec{PF_2}=(\sqrt2,-1)$。点积 $=-2+1=-1$。" "\n"
        r"公式：$\frac{0+0-1}{1}=-1$ ✓✓✓" "\n"
        r"· $m=-1$：$P=(-1,0)$。$\vec{PF_1}=(1-\sqrt2,0)$、$\vec{PF_2}=(1+\sqrt2,0)$。点积 $=(1-\sqrt2)(1+\sqrt2)=1-2=-1$。" "\n"
        r"公式：$\frac{2(1)+2(-1)-1}{1}=\frac{2-2-1}1=-1$ ✓✓✓" "\n"
        r"**最小值 $-1.5$ 在 $m=-0.5$；端点值都是 $-1$ ⟹ 最大值 $-1$（在 $m=0$ 与 $m=-1$ 处并列）**" "\n"
        r"⚠ 注意：$m=-1$ 时 $y=0$，$S=0$；$m=0$ 时 $S=c$。**面积最大对应 $m=0$**，与 $S_2=c$ 一致 ✓✓✓" "\n"
        r"· $S_1=\frac{a^2c}{a^2+1}=\frac{1\cdot\sqrt2}{2}=\frac{\sqrt2}2=0.707107$；$S_2=c=\sqrt2=1.414214$。" "\n"
        r"$S_2/S_1=2.000000$ ✓✓✓ **$S_2=2S_1$ 成立**" "\n"
        r"**答案 A（$\sqrt2$）正确** ✓" "\n"
        r"**⭐⭐ 通法（线段上动点 ⟹ 单变量二次函数）**：" "\n"
        r"① ⭐⭐ **「点在线段上」⟹ 用一个参数表示整条线段**：" "\n"
        r"本题用横坐标 $m$ 表示 $P\left(m,\frac{m+a}a\right)$ —— **参数化是处理动点问题的第一步**；" "\n"
        r"② ⭐⭐ **向量点积的坐标公式直接展开**：" "\n"
        r"$\vec{PF_1}\cdot\vec{PF_2}=(x_{F_1}-x_P)(x_{F_2}-x_P)+(y_{F_1}-y_P)(y_{F_2}-y_P)$。" "\n"
        r"本题因 $F_1,F_2$ 都在 $x$ 轴上，**$y$ 部分变成 $\left(\frac{m+a}a\right)^2$（平方，符号消失）** —— 这大大简化计算；" "\n"
        r"③ ⭐⭐ **面积用「底 $\times$ 高」：$S=\frac12\cdot2c\cdot y_P=c\,y_P$**：" "\n"
        r"**$\triangle PF_1F_2$ 的底恒为 $2c$，高就是 $P$ 的纵坐标** —— 面积与 $P$ 的纵坐标成正比，" "\n"
        r"所以「点积最小」与「面积最小」是**两个不同的点**（二次函数顶点 vs 纵坐标最小），**别混为一谈**；" "\n"
        r"④ ⚠ **求最值时要比较顶点与两个端点**：" "\n"
        r"二次函数开口向上 ⟹ 最小值在顶点（若顶点在区间内），**最大值在离对称轴较远的端点**。" "\n"
        r"本题 $m=-a$ 处 $y=0$（面积为 $0$）、$m=0$ 处 $y=1$（面积 $=c$）⟹ 最大值在 $m=0$ ✓；" "\n"
        r"⑤ ⚠ **$b=1$ 来自「虚轴顶点 $N(0,1)$」**：" "\n"
        r"**虚轴顶点坐标是 $(0,\pm b)$** ⟹ $b=1$，于是 $c^2=a^2+1$ —— **这是本题所有计算的起点**；" "\n"
        r"⑥ ⭐ **验证方法：代入 $a=1$ 后把三个特殊点（顶点 + 两端点）全算一遍**：" "\n"
        r"**点积值与面积值都对上，才算真的验证完**。"
    ),
    'difficulty': 0.94,
    'topics': ['M-T-375'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-375-V3',
}

T206_V3 = {
    'type': '选择',
    'stem_text': (
        r"设 $O$ 是 $\triangle ABC$ 的外心，满足 $\vec{AO}=t\vec{AB}+\left(\dfrac12-\dfrac t2\right)\vec{AC}$（$t\in\mathbb R^+$），若 $\lvert\vec{AB}\rvert=\lvert\vec{AC}\rvert=4$，则 $\triangle ABC$ 的面积是（　　）"
    ),
    'opts': [
        ('A', r"$4$"),
        ('B', r"$4\sqrt3$"),
        ('C', r"$8$"),
        ('D', r"$6$"),
    ],
    'answer': 'B',
    'analysis': (
        r"外心满足 $\vec u\cdot\vec{AO}=8$、$\vec v\cdot\vec{AO}=8$（$\vec u=\vec{AB}$、$\vec v=\vec{AC}$）。代入展开得 $8t(2\cos A-1)=0$ ⟹ $\cos A=\frac12$，"
        r"再由 $12t+4=8$ 得 $t=\frac13>0$；$S=\frac12\cdot4\cdot4\cdot\frac{\sqrt3}2=4\sqrt3$。"
    ),
    'solution': (
        r"设 $\vec{AB}=\vec u$、$\vec{AC}=\vec v$，则 $\lvert\vec u\rvert=\lvert\vec v\rvert=4$，$\vec u\cdot\vec v=16\cos A$。" "\n"
        r"$\because O$ 是外心，$\therefore\lvert OA\rvert=\lvert OB\rvert=\lvert OC\rvert$。" "\n"
        r"由 $\lvert OA\rvert=\lvert OB\rvert$：$\lvert\vec{AO}\rvert^2=\lvert\vec{AB}-\vec{AO}\rvert^2=\lvert\vec u\rvert^2-2\vec u\cdot\vec{AO}+\lvert\vec{AO}\rvert^2$。" "\n"
        r"$\therefore 0=16-2\vec u\cdot\vec{AO}$ ⟹ $\vec u\cdot\vec{AO}=8$。同理 $\vec v\cdot\vec{AO}=8$。" "\n"
        r"代入 $\vec{AO}=t\vec u+\left(\dfrac12-\dfrac t2\right)\vec v$：" "\n"
        r"$\vec u\cdot\vec{AO}=t\lvert\vec u\rvert^2+\left(\dfrac12-\dfrac t2\right)(\vec u\cdot\vec v)=16t+\left(\dfrac12-\dfrac t2\right)16\cos A=8$　(1)" "\n"
        r"$\vec v\cdot\vec{AO}=t(\vec u\cdot\vec v)+\left(\dfrac12-\dfrac t2\right)\lvert\vec v\rvert^2=16t\cos A+\left(\dfrac12-\dfrac t2\right)16=8$　(2)" "\n"
        r"由 (2)：$16t\cos A+8-8t=8$ ⟹ $8t(2\cos A-1)=0$。" "\n"
        r"$\because t\in\mathbb R^+$（$t>0$），$\therefore 2\cos A-1=0$ ⟹ $\cos A=\dfrac12$ ⟹ $A=\dfrac\pi3$。" "\n"
        r"代回 (1)：$16t+\left(\frac12-\frac t2\right)\cdot16\cdot\frac12=16t+4-4t=12t+4=8$ ⟹ $t=\dfrac13>0$ ✓。" "\n"
        r"$\therefore S_{\triangle ABC}=\dfrac12\lvert\vec{AB}\rvert\lvert\vec{AC}\rvert\sin A=\dfrac12\cdot4\cdot4\cdot\sin\dfrac\pi3=8\cdot\dfrac{\sqrt3}2=4\sqrt3$。故选 B。"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（选项 B 提取为 `4 3`，实为 $4\sqrt3$，**根号丢失**）；" "\n"
        r"**本题详解未提供，全部由我独立推导并用答案验证** ✓" "\n"
        r"**独立验算（完全独立）**：" "\n"
        r"① **外心 ⟹ $\vec u\cdot\vec{AO}=8$ 的推导**：" "\n"
        r"$|OA|=|OB|$ ⟹ $|\vec{AO}|^2=|\vec{OB}|^2$。而 $\vec{OB}=\vec{AB}-\vec{AO}=\vec u-\vec{AO}$。" "\n"
        r"$|\vec u-\vec{AO}|^2=|\vec u|^2-2\vec u\cdot\vec{AO}+|\vec{AO}|^2=16-2\vec u\cdot\vec{AO}+|\vec{AO}|^2$。" "\n"
        r"令其等于 $|\vec{AO}|^2$ ⟹ $16-2\vec u\cdot\vec{AO}=0$ ⟹ $\vec u\cdot\vec{AO}=8$ ✓✓✓" "\n"
        r"（同理 $|\vec v|=4$ ⟹ $\vec v\cdot\vec{AO}=8$ ✓）" "\n"
        r"② **$\cos A=\frac12$ 的推导**：$16t\cos A+8-8t=8$ ⟹ $16t\cos A=8t$ ⟹ $\cos A=\frac12$（因 $t>0$）✓✓✓" "\n"
        r"（**$t>0$ 这个条件保证了可以除以 $t$** —— 若 $t=0$ 则 $\cos A$ 不定，题目特意给了 $t\in\mathbb R^+$）" "\n"
        r"③ **$t=\frac13$ 的验证**：$16\cdot\frac13+\left(\frac12-\frac16\right)\cdot16\cdot\frac12=\frac{16}3+\frac13\cdot8=\frac{16}3+\frac83=\frac{24}3=8$ ✓✓✓" "\n"
        r"④ **面积**：$\frac12\cdot4\cdot4\cdot\sin60°=8\cdot\frac{\sqrt3}2=6.928203=4\sqrt3$ ✓✓✓" "\n"
        r"⑤ **完整构造验证**：取 $A=(0,0)$、$B=(4,0)$、$C=(4\cos60°,4\sin60°)=(2,2\sqrt3)$。" "\n"
        r"$\vec u=(4,0)$、$\vec v=(2,2\sqrt3)$。$\vec{AO}=t\vec u+(\frac12-\frac t2)\vec v=\frac13(4,0)+\frac13(2,2\sqrt3)=(\frac43+\frac23,\frac{2\sqrt3}3)=(2,\frac{2\sqrt3}3)$。" "\n"
        r"$O=(2,\frac{2\sqrt3}3)=(2,1.154701)$。" "\n"
        r"**验证 $O$ 是外心**：$A=(0,0)$、$B=(4,0)$、$C=(2,2\sqrt3)$。" "\n"
        r"$|OA|=\sqrt{4+\frac{12}9}=\sqrt{4+\frac43}=\sqrt{\frac{16}3}=\frac4{\sqrt3}=2.309401$。" "\n"
        r"$|OB|=\sqrt{(2-4)^2+\frac{12}9}=\sqrt{4+\frac43}=\frac4{\sqrt3}$ ✓✓✓" "\n"
        r"$|OC|=\sqrt{(2-2)^2+(\frac{2\sqrt3}3-2\sqrt3)^2}=\left|\frac{2\sqrt3}3-\frac{6\sqrt3}3\right|=\frac{4\sqrt3}3=\frac4{\sqrt3}$ ✓✓✓" "\n"
        r"**三点等距，$O$ 确为外心** ✓✓✓" "\n"
        r"（注：等边三角形边长 $4$ 的外接圆半径应为 $\frac4{\sqrt3}$ ✓ 一致）" "\n"
        r"⑥ **补充观察**：$\cos A=\frac12$ 且 $|AB|=|AC|=4$ ⟹ $\triangle ABC$ 是**等边三角形**（边长 $4$），" "\n"
        r"面积 $=\frac{\sqrt3}4\cdot16=4\sqrt3$ ✓✓✓ **与结果一致**" "\n"
        r"**答案 B（$4\sqrt3$）正确** ✓" "\n"
        r"**⭐⭐ 通法（外心的向量刻画）**：" "\n"
        r"① ⭐⭐ **外心的向量等价条件**：" "\n"
        r"$\lvert OA\rvert=\lvert OB\rvert$ ⟺ $\vec{AB}\cdot\vec{AO}=\dfrac{\lvert\vec{AB}\rvert^2}2$。" "\n"
        r"**记忆法：$\vec{AB}\cdot\vec{AO}=\frac12|AB|^2$**（$O$ 在 $AB$ 中垂线上）。" "\n"
        r"这是把「外心」翻译成向量方程的**通用钥匙**；" "\n"
        r"② ⭐⭐ **给 $\vec{AO}$ 的表达式求参数：分别点乘两邻边**：" "\n"
        r"本题 $\vec{AO}=t\vec u+(\frac12-\frac t2)\vec v$，分别点乘 $\vec u$、$\vec v$ 得两个方程 —— " "\n"
        r"**两个未知量（$t$ 和 $A$）配两个方程，恰好可解**；" "\n"
        r"③ ⭐⭐ **「$t\in\mathbb R^+$」不是废话**：" "\n"
        r"它保证了 $8t(2\cos A-1)=0$ 中可以除以 $t$ —— **题目给的每一个条件都要用上**，" "\n"
        r"如果发现某个条件没用到，很可能是自己漏了一步；" "\n"
        r"④ ⭐ **验证外心：算三个距离是否相等**：" "\n"
        r"**构造具体坐标后算 $|OA|,|OB|,|OC|$** —— 三者相等才算验证通过，" "\n"
        r"这是最硬的检验方法；" "\n"
        r"⑤ ⚠ **$\cos A=\frac12$ 配上 $|AB|=|AC|$ ⟹ 等边**：" "\n"
        r"等腰 + 顶角 $60°$ ⟹ 等边。**发现这个可以秒算面积**（$\frac{\sqrt3}4a^2$）；" "\n"
        r"⑥ ⚠ **选项 B 的 `4 3` 是 $4\sqrt3$**：" "\n"
        r"**又一个根号丢失** —— 凡是提取文本里出现「整数 + 整数」且答案对不上，" "\n"
        r"第一反应就是检查根号。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-206'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-206-V3',
}

T203_E1 = {
    'type': '选择',
    'stem_text': (
        r"$\triangle ABC$ 中，$BD$ 是 $AC$ 边上的高，$A=\dfrac\pi4$，$\cos B=-\dfrac{\sqrt5}5$，则 $\dfrac{BD}{AC}=$（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac14$"),
        ('B', r"$\dfrac12$"),
        ('C', r"$\dfrac23$"),
        ('D', r"$\dfrac34$"),
    ],
    'answer': 'A',
    'analysis': (
        r"由 $S=\frac12\cdot AC\cdot BD=\frac12\cdot AB\cdot AC\sin A$ 得 $BD=c\sin A$，故 $\frac{BD}{AC}=\frac{c\sin A}b=\frac{\sin C}{\sin B}\sin A$。"
        r"$\cos B=-\frac{\sqrt5}5$ ⟹ $\sin B=\frac{2\sqrt5}5$；$C=\frac{3\pi}4-B$ ⟹ $\sin C=\frac{\sqrt{10}}{10}$ ⟹ 比值 $=\frac14$。"
    ),
    'solution': (
        r"设 $\triangle ABC$ 中 $a=BC$、$b=AC$、$c=AB$，$BD$ 是 $AC$ 边上的高。" "\n"
        r"由面积：$S=\dfrac12\cdot AC\cdot BD=\dfrac12 b\cdot BD$，又 $S=\dfrac12 bc\sin A$。" "\n"
        r"$\therefore\dfrac12 b\cdot BD=\dfrac12 bc\sin A$ ⟹ $BD=c\sin A$。" "\n"
        r"$\therefore\dfrac{BD}{AC}=\dfrac{c\sin A}{b}=\dfrac{\sin C}{\sin B}\cdot\sin A$（由正弦定理 $\frac cb=\frac{\sin C}{\sin B}$）。" "\n"
        r"已知 $\cos B=-\dfrac{\sqrt5}5$，且 $B\in(0,\pi)$，$\therefore\sin B=\sqrt{1-\dfrac15}=\sqrt{\dfrac45}=\dfrac{2\sqrt5}5$。" "\n"
        r"$C=\pi-A-B=\pi-\dfrac\pi4-B=\dfrac{3\pi}4-B$。" "\n"
        r"$\sin C=\sin\left(\dfrac{3\pi}4-B\right)=\sin\dfrac{3\pi}4\cos B-\cos\dfrac{3\pi}4\sin B$" "\n"
        r"$=\dfrac{\sqrt2}2\cdot\left(-\dfrac{\sqrt5}5\right)-\left(-\dfrac{\sqrt2}2\right)\cdot\dfrac{2\sqrt5}5=\dfrac{\sqrt2}2\left(-\dfrac{\sqrt5}5+\dfrac{2\sqrt5}5\right)=\dfrac{\sqrt2}2\cdot\dfrac{\sqrt5}5=\dfrac{\sqrt{10}}{10}$。" "\n"
        r"$\therefore\dfrac{BD}{AC}=\dfrac{\frac{\sqrt{10}}{10}}{\frac{2\sqrt5}5}\cdot\dfrac{\sqrt2}2=\dfrac{\sqrt{10}}{10}\cdot\dfrac{5}{2\sqrt5}\cdot\dfrac{\sqrt2}2=\dfrac{\sqrt{10}\cdot5\cdot\sqrt2}{10\cdot2\sqrt5\cdot2}=\dfrac{5\sqrt{20}}{40\sqrt5}=\dfrac{5\cdot2\sqrt5}{40\sqrt5}=\dfrac{10}{40}=\dfrac14$。" "\n"
        r"故选 A。"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（题干 $\cos B$ 提取为 `- 5 5`，实为 $-\frac{\sqrt5}5$，**根号丢失**）；" "\n"
        r"**本题详解未提供，全部由我独立推导并用答案验证** ✓" "\n"
        r"**独立验算（数值，完全独立）**：" "\n"
        r"① **$\sin B$**：$\cos B=-\frac{\sqrt5}5=-0.447214$ ⟹ $\sin B=\sqrt{1-0.2}=\sqrt{0.8}=0.894427=\frac{2\sqrt5}5$ ✓✓✓" "\n"
        r"② **角度**：$B=\arccos(-0.447214)=116.565051°$；$A=45°$ ⟹ $C=180-45-116.565=18.434949°$ ✓✓✓" "\n"
        r"③ **$\sin C$**：$\sin(18.434949°)=0.316228=\frac{\sqrt{10}}{10}$ ✓✓✓" "\n"
        r"④ **比值**：$\frac{0.316228}{0.894427}\times\sin45°=\frac{0.316228}{0.894427}\times0.707107$" "\n"
        r"$=0.353553\times0.707107=0.250000=\frac14$ ✓✓✓ **完全吻合**" "\n"
        r"⑤ **构造具体三角形验证**：取 $AC=b=4$，则 $BD=\frac14\cdot4=1$。" "\n"
        r"由 $BD=c\sin A$ ⟹ $1=c\cdot\frac{\sqrt2}2$ ⟹ $c=\sqrt2=1.414214$。" "\n"
        r"由正弦定理 $\frac c{\sin C}=\frac b{\sin B}$：$\frac{1.414214}{0.316228}=4.472136$；$\frac4{0.894427}=4.472136$ ✓✓✓ **一致**" "\n"
        r"再算 $a$：$\frac a{\sin A}=4.472136$ ⟹ $a=4.472136\times0.707107=3.162278=\sqrt{10}$。" "\n"
        r"验证余弦定理：$b^2+c^2-2bc\cos A=16+2-2\cdot4\cdot1.414214\cdot0.707107=18-8=10=a^2$ ✓✓✓ **完全闭合**" "\n"
        r"⑥ **选项排除**：$\frac12=0.5$、$\frac23=0.667$、$\frac34=0.75$ 都不等于 $0.25$ ✓✓✓" "\n"
        r"**答案 A（$\frac14$）正确** ✓" "\n"
        r"**⭐⭐ 通法（高的比例 ⟹ 用面积转换）**：" "\n"
        r"① ⭐⭐ **「高」与「边」的比值用面积转换**：" "\n"
        r"$S=\frac12\cdot(\text{底})\cdot(\text{高})$ ⟹ $\frac{BD}{AC}=\frac{2S}{AC^2}$。更常用的是：" "\n"
        r"**$BD=c\sin A=b\sin C$** —— **高 = 邻边 $\times$ 夹角的正弦**，这是最直接的转换；" "\n"
        r"② ⭐⭐ **$\frac{BD}{AC}=\frac{\sin C\sin A}{\sin B}$ 是个好用的公式**：" "\n"
        r"由 $BD=c\sin A$ 与 $b=AC$ 得 $\frac{BD}{b}=\frac cb\sin A=\frac{\sin C}{\sin B}\sin A$ —— " "\n"
        r"**把「长度的比」全变成「正弦的比」**；" "\n"
        r"③ ⭐ **$\sin C=\sin(A+B)$ 或 $\sin(\pi-A-B)$，用和角公式展开**：" "\n"
        r"本题 $C=\frac{3\pi}4-B$ ⟹ $\sin C=\sin\frac{3\pi}4\cos B-\cos\frac{3\pi}4\sin B$。" "\n"
        r"**注意 $\cos\frac{3\pi}4=-\frac{\sqrt2}2$ 是负的**，减负变加 —— 这一步符号极易错；" "\n"
        r"④ ⚠ **$\cos B<0$ ⟹ $B$ 是钝角**：" "\n"
        r"$\cos B=-\frac{\sqrt5}5$ ⟹ $B=116.57°$。**钝角的正弦仍为正** $\sin B=\frac{2\sqrt5}5$ ✓；" "\n"
        r"⑤ ⚠ **验证要「构造完整三角形」**：" "\n"
        r"**算出 $a,b,c$ 后用余弦定理回代** —— 这是检验三角计算的黄金标准，" "\n"
        r"比只核对最终比值可靠得多。"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-203'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-203-E1',
}

T203_V1 = {
    'type': '填空',
    'stem_text': (
        r"已知 $\triangle ABC$ 的面积等于 $1$，若 $BC=1$，则当这个三角形的三条高的乘积取最大值时，$\sin A=$ ____。"
    ),
    'opts': [],
    'answer': r"$\dfrac8{17}$",
    'analysis': (
        r"三高之积 $=\frac{8S^3}{abc}=\frac8{bc}$（$S=1,a=1$），而 $bc=\frac2{\sin A}$，故积 $=4\sin A$。"
        r"由 $b^2+c^2\ge2bc$ 与余弦定理得 $\tan\frac A2\le\frac14$，等号时 $b=c$ ⟹ $\sin A=\frac8{17}$。"
    ),
    'solution': (
        r"设三边为 $a,b,c$，对应高为 $h_a,h_b,h_c$，面积 $S=1$。" "\n"
        r"由 $S=\dfrac12ah_a=\dfrac12bh_b=\dfrac12ch_c$ 得 $h_a=\dfrac{2S}a$、$h_b=\dfrac{2S}b$、$h_c=\dfrac{2S}c$。" "\n"
        r"$\therefore h_ah_bh_c=\dfrac{8S^3}{abc}=\dfrac8{abc}$（因 $S=1$）。" "\n"
        r"已知 $a=BC=1$，$\therefore h_ah_bh_c=\dfrac8{bc}$。" "\n"
        r"由面积公式 $S=\dfrac12bc\sin A=1$ ⟹ $bc=\dfrac2{\sin A}$。" "\n"
        r"$\therefore h_ah_bh_c=\dfrac8{2/\sin A}=4\sin A$。" "\n"
        r"要使三高之积最大，需 $\sin A$ 最大。但 $A$ 受约束 —— " "\n"
        r"由余弦定理 $a^2=b^2+c^2-2bc\cos A$，即 $1=b^2+c^2-2bc\cos A$。" "\n"
        r"由 $b^2+c^2\ge2bc$（等号当且仅当 $b=c$）：" "\n"
        r"$1=b^2+c^2-2bc\cos A\ge2bc-2bc\cos A=2bc(1-\cos A)$。" "\n"
        r"代入 $bc=\dfrac2{\sin A}$：$1\ge2\cdot\dfrac2{\sin A}(1-\cos A)=\dfrac{4(1-\cos A)}{\sin A}$。" "\n"
        r"$\therefore\sin A\ge4(1-\cos A)$。用半角公式：$2\sin\frac A2\cos\frac A2\ge4\cdot2\sin^2\frac A2$。" "\n"
        r"$\because\sin\frac A2>0$，$\therefore\cos\frac A2\ge4\sin\frac A2$ ⟹ $\tan\dfrac A2\le\dfrac14$。" "\n"
        r"$\because A\in(0,\pi)$，$\sin A$ 在 $A\le\frac\pi2$ 时递增，而 $\tan\frac A2\le\frac14$ 给出 $A\le2\arctan\frac14<\frac\pi2$，" "\n"
        r"$\therefore\sin A$ 在 $A=2\arctan\dfrac14$ 时取最大值，此时 $b=c$（等腰）。" "\n"
        r"由 $\tan\dfrac A2=\dfrac14$ 得 $\sin\dfrac A2=\dfrac1{\sqrt{17}}$、$\cos\dfrac A2=\dfrac4{\sqrt{17}}$。" "\n"
        r"$\therefore\sin A=2\sin\dfrac A2\cos\dfrac A2=2\cdot\dfrac1{\sqrt{17}}\cdot\dfrac4{\sqrt{17}}=\dfrac8{17}$。"
    ),
    'review': (
        r"★ 题干、答案完整 ✓；**本题详解未提供，全部由我独立推导并用答案验证** ✓" "\n"
        r"**独立验算（完全独立）**：" "\n"
        r"① **三高之积的表达式**：$h_a=\frac{2S}a$ 等 ⟹ $h_ah_bh_c=\frac{(2S)^3}{abc}=\frac{8S^3}{abc}$ ✓✓✓" "\n"
        r"$S=1$、$a=1$ ⟹ 积 $=\frac8{bc}$ ✓✓✓" "\n"
        r"② **$bc=\frac2{\sin A}$**：$S=\frac12bc\sin A=1$ ⟹ $bc=\frac2{\sin A}$ ✓✓✓" "\n"
        r"③ **积 $=4\sin A$**：$\frac8{bc}=\frac8{2/\sin A}=4\sin A$ ✓✓✓" "\n"
        r"（**注意：这个式子说明「最大化三高之积」就是「最大化 $\sin A$」**，" "\n"
        r"但不能直接取 $\sin A=1$，因为 $A$ 还受 $a=1$、$S=1$ 的约束！）" "\n"
        r"④ **约束的推导**：$1=b^2+c^2-2bc\cos A\ge2bc(1-\cos A)$。" "\n"
        r"代入 $bc$：$1\ge\frac{4(1-\cos A)}{\sin A}$ ⟹ $\sin A\ge4(1-\cos A)$。" "\n"
        r"半角：$2\sin\frac A2\cos\frac A2\ge8\sin^2\frac A2$ ⟹ $\cos\frac A2\ge4\sin\frac A2$ ⟹ $\tan\frac A2\le\frac14$ ✓✓✓" "\n"
        r"⑤ **最大值点**：$A_{\max}=2\arctan\frac14=2\times14.036243°=28.072487°$。" "\n"
        r"$\sin A_{\max}=\sin(28.072487°)=0.470588=\frac8{17}$ ✓✓✓" "\n"
        r"（$\frac8{17}=0.470588$ ✓）" "\n"
        r"⑥ **构造完整三角形验证**：$A=28.072487°$，$b=c$（等腰）。" "\n"
        r"$bc=\frac2{\sin A}=\frac2{0.470588}=4.25$ ⟹ $b=c=\sqrt{4.25}=2.061553$。" "\n"
        r"验证 $a$：$a^2=b^2+c^2-2bc\cos A=4.25+4.25-2\times4.25\times0.882353$" "\n"
        r"$=8.5-8.5\times0.882353=8.5\times0.117647=1.000000$ ⟹ $a=1$ ✓✓✓ **完全吻合**" "\n"
        r"（$\cos A=\sqrt{1-0.470588^2}=\sqrt{1-0.221453}=\sqrt{0.778547}=0.882353=\frac{15}{17}$）" "\n"
        r"⑦ **三高之积的值**：$4\sin A=4\times\frac8{17}=\frac{32}{17}=1.882353$。" "\n"
        r"直接用 $h_a=2$、$h_b=h_c=\frac2{2.061553}=0.970143$：" "\n"
        r"积 $=2\times0.970143\times0.970143=2\times0.941177=1.882353$ ✓✓✓ **一致**" "\n"
        r"⑧ **确认是最大值**：取 $A=20°$（更小），$\sin A=0.342<\frac8{17}$ ⟹ 积更小 ✓✓✓" "\n"
        r"**答案 $\frac8{17}$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（最值问题：约束用不等式夹出来）**：" "\n"
        r"① ⭐⭐ **$h_ah_bh_c=\dfrac{8S^3}{abc}$ 是个漂亮的公式**：" "\n"
        r"**用面积把三条高统一表示** —— 分子只含 $S$，分母是三边之积。" "\n"
        r"记忆法：**每条高 $=\frac{2S}{\text{对应边}}$，三式相乘即得**；" "\n"
        r"② ⭐⭐ **「两个约束（$S$ 与一边）」定不出三个变量，但能定出角的范围**：" "\n"
        r"本题 $S=1$、$a=1$ 给出 $bc=\frac2{\sin A}$，再用 $b^2+c^2\ge2bc$ 把 $b,c$ 消掉 —— " "\n"
        r"**「用基本不等式消去多余变量」是求范围的通用手法**；" "\n"
        r"③ ⭐⭐ **$b^2+c^2\ge2bc$ 的等号 ⟹ $b=c$（等腰）**：" "\n"
        r"**最值往往在对称（等腰）时取到** —— 这是解三角形最值题的强烈先验；" "\n"
        r"④ ⚠ **不能直接用 $\sin A\le1$**：" "\n"
        r"本题 $\sin A$ 受 $\tan\frac A2\le\frac14$ 限制，最大只有 $\frac8{17}\approx0.47$ —— " "\n"
        r"**「看起来能取到 $1$」和「真的能取到」是两回事，必须检查约束**；" "\n"
        r"⑤ ⭐ **半角技巧：$\sin A\ge4(1-\cos A)$ ⟹ $\tan\frac A2\le\frac14$**：" "\n"
        r"**$\sin A$ 与 $1-\cos A$ 同时出现时，化为半角后能约去 $\sin\frac A2$** —— 这是固定套路；" "\n"
        r"⑥ ⭐ **验证方法：反解出 $b=c$ 后代回余弦定理**：" "\n"
        r"**算出 $a$ 是否等于 $1$** —— 这是检验「最值点是否合法」的硬标准。"
    ),
    'difficulty': 0.93,
    'topics': ['M-T-203'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-203-V1',
}

T176_V1 = {
    'type': '选择',
    'stem_text': (
        r"若将函数 $f(x)=2\sin(2x+\varphi)$（$\lvert\varphi\rvert<\dfrac\pi2$）的图象向左平移 $\dfrac\pi6$ 个单位后得到的图象关于 $y$ 轴对称，"
        r"则函数 $f(x)$ 在 $\left[0,\dfrac\pi2\right]$ 上的最大值为（　　）"
    ),
    'opts': [
        ('A', r"$2$"),
        ('B', r"$\sqrt3$"),
        ('C', r"$1$"),
        ('D', r"$\dfrac{\sqrt3}2$"),
    ],
    'answer': 'A',
    'analysis': (
        r"左移 $\frac\pi6$ 得 $g(x)=2\sin\left(2x+\frac\pi3+\varphi\right)$；关于 $y$ 轴对称即 $g$ 为偶函数 ⟹ $\frac\pi3+\varphi=\frac\pi2+k\pi$ ⟹ $\varphi=\frac\pi6$。"
        r"$f(x)=2\sin\left(2x+\frac\pi6\right)$，相位 $\in[\frac\pi6,\frac{7\pi}6]$ 含 $\frac\pi2$ ⟹ 最大值 $2$。"
    ),
    'solution': (
        r"将 $f(x)=2\sin(2x+\varphi)$ 的图象向左平移 $\dfrac\pi6$ 个单位，得" "\n"
        r"$g(x)=f\left(x+\dfrac\pi6\right)=2\sin\left(2\left(x+\dfrac\pi6\right)+\varphi\right)=2\sin\left(2x+\dfrac\pi3+\varphi\right)$。" "\n"
        r"$g(x)$ 的图象关于 $y$ 轴对称 ⟹ $g$ 是**偶函数**。" "\n"
        r"对 $y=2\sin(2x+\theta)$ 型函数为偶函数，需 $\sin(\theta+2x)=\sin(\theta-2x)$ 对任意 $x$ 成立，" "\n"
        r"即 $\theta=\dfrac\pi2+k\pi$（$k\in\mathbb Z$）。" "\n"
        r"$\therefore\dfrac\pi3+\varphi=\dfrac\pi2+k\pi$ ⟹ $\varphi=\dfrac\pi6+k\pi$。" "\n"
        r"由 $\lvert\varphi\rvert<\dfrac\pi2$，取 $k=0$ ⟹ $\varphi=\dfrac\pi6$。" "\n"
        r"$\therefore f(x)=2\sin\left(2x+\dfrac\pi6\right)$。" "\n"
        r"当 $x\in\left[0,\dfrac\pi2\right]$ 时，$2x+\dfrac\pi6\in\left[\dfrac\pi6,\dfrac{7\pi}6\right]$。" "\n"
        r"$\because\dfrac\pi2\in\left[\dfrac\pi6,\dfrac{7\pi}6\right]$，$\therefore$ 当 $2x+\dfrac\pi6=\dfrac\pi2$，即 $x=\dfrac\pi6$ 时，$\sin$ 取最大值 $1$。" "\n"
        r"$\therefore f(x)_{\max}=2\times1=2$。故选 A。"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（选项 B 提取为 `3` 实为 $\sqrt3$、D 为 `3 2` 实为 $\frac{\sqrt3}2$，**根号丢失**）；" "\n"
        r"**本题详解未提供，全部由我独立推导并用答案验证** ✓" "\n"
        r"**独立验算（数值扫描，完全独立）**：" "\n"
        r"① **扫描结果**：在 $x\in[0,\frac\pi2]$ 上取 $401$ 个点，$\max f=1.999993\approx2$ ✓✓✓" "\n"
        r"（扫描的极小误差来自离散取样，精确值为 $2$）" "\n"
        r"② **$\varphi$ 的确定**：$\frac\pi3+\varphi=\frac\pi2$ ⟹ $\varphi=\frac\pi6=0.523599<\frac\pi2$ ✓ ✓✓✓" "\n"
        r"（若取 $k=1$：$\varphi=\frac\pi6+\pi>\frac\pi2$ ✗；$k=-1$：$\varphi=\frac\pi6-\pi<-\frac\pi2$ ✗）" "\n"
        r"③ **偶函数验证**：$g(x)=2\sin(2x+\frac\pi3+\frac\pi6)=2\sin(2x+\frac\pi2)=2\cos(2x)$。" "\n"
        r"**$2\cos2x$ 确实是偶函数** ✓✓✓ **关于 $y$ 轴对称成立**" "\n"
        r"④ **最大值点**：$2x+\frac\pi6=\frac\pi2$ ⟹ $x=\frac\pi6=0.523599\in[0,\frac\pi2]$ ✓ ⟹ $f=2$ ✓✓✓" "\n"
        r"⑤ **端点值**：$f(0)=2\sin\frac\pi6=1$；$f(\frac\pi2)=2\sin(\pi+\frac\pi6)=-2\sin\frac\pi6=-1$。" "\n"
        r"**最大值在中段，不是端点** ✓✓✓" "\n"
        r"⑥ **选项排除**：$\sqrt3=1.732$、$1$、$\frac{\sqrt3}2=0.866$ 都小于 $2$ ✓✓✓" "\n"
        r"（**$\sqrt3$ 是干扰项**：若误取 $\varphi=\frac\pi3$ 则 $f=2\sin(2x+\frac\pi3)$，相位 $\in[\frac\pi3,\frac{4\pi}3]$ 含 $\frac\pi2$，最大值仍是 $2$；" "\n"
        r"若误认为最大值在端点 $x=\frac\pi2$ 处则会得到别的值）" "\n"
        r"**答案 A（$2$）正确** ✓" "\n"
        r"**⭐⭐ 通法（平移 + 对称性定参数）**：" "\n"
        r"① ⭐⭐ **左移 $m$ 个单位 ⟹ 把 $x$ 换成 $x+m$**：" "\n"
        r"$g(x)=f(x+m)$ —— **「左加右减」**。" "\n"
        r"⚠ 注意本题是 $2(x+\frac\pi6)$，即 $2x+\frac\pi3$，**平移量要乘进 $\omega$**；" "\n"
        r"② ⭐⭐ **关于 $y$ 轴对称 ⟹ 偶函数 ⟹ 相位 $=\frac\pi2+k\pi$**：" "\n"
        r"对 $y=A\sin(\omega x+\theta)$：偶函数 ⟺ $\theta=\frac\pi2+k\pi$（此时函数化为 $\pm A\cos\omega x$）。" "\n"
        r"**记忆法：正弦函数变成余弦就对称了**；" "\n"
        r"③ ⭐ **$\sin(2x+\frac\pi2)=\cos2x$ 直接用诱导公式**：" "\n"
        r"**看到「相位 $=\frac\pi2$」就想到「变成 $\cos$」**，比用偶函数定义推快得多；" "\n"
        r"④ ⚠ **$\varphi$ 要用 $\lvert\varphi\rvert<\frac\pi2$ 筛选**：" "\n"
        r"解出 $\varphi=\frac\pi6+k\pi$ 后必须逐个试 $k$ —— **别默认 $k=0$**；" "\n"
        r"⑤ ⚠ **求值域时检查相位区间是否含 $\frac\pi2$**：" "\n"
        r"本题 $[\frac\pi6,\frac{7\pi}6]$ 含 $\frac\pi2$ ⟹ 最大值 $1$（乘振幅 $2$ 得 $2$）。" "\n"
        r"**若区间不含 $\frac\pi2$，最大值就在端点** —— 这一步不能省。"
    ),
    'difficulty': 0.75,
    'topics': ['M-T-176'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-176-V1',
}

T176_E1 = {
    'type': '填空',
    'stem_text': (
        r"设函数 $f(x)=\sin\left(2x+\dfrac\pi4\right)$，$x\in\left[0,\dfrac{9\pi}8\right]$，若方程 $f(x)=a$ 恰好有三个根，分别为 $x_1,x_2,x_3$（$x_1<x_2<x_3$），"
        r"则 $x_1+x_2+x_3$ 的取值范围是 ____。"
    ),
    'opts': [],
    'answer': r"$\left[\dfrac{5\pi}4,\dfrac{11\pi}8\right)$",
    'analysis': (
        r"令 $t=2x+\frac\pi4\in[\frac\pi4,\frac{5\pi}2]$，设 $\alpha=\arcsin a$。恰三根 ⟺ $\alpha\in[\frac\pi4,\frac\pi2)$。"
        r"三根相位为 $\alpha,\pi-\alpha,2\pi+\alpha$，和 $=3\pi+\alpha$ ⟹ $x_1+x_2+x_3=\frac{9\pi}8+\frac\alpha2\in[\frac{5\pi}4,\frac{11\pi}8)$。"
    ),
    'solution': (
        r"令 $t=2x+\dfrac\pi4$。当 $x\in\left[0,\dfrac{9\pi}8\right]$ 时，$t\in\left[\dfrac\pi4,2\cdot\dfrac{9\pi}8+\dfrac\pi4\right]=\left[\dfrac\pi4,\dfrac{5\pi}2\right]$。" "\n"
        r"方程 $f(x)=a$ 即 $\sin t=a$，$t\in\left[\dfrac\pi4,\dfrac{5\pi}2\right]$。" "\n"
        r"设 $\alpha=\arcsin a\in\left(0,\dfrac\pi2\right]$（要有三个根需 $a\in(0,1)$）。" "\n"
        r"$\sin t=a$ 的通解为 $t=\alpha+2k\pi$ 或 $t=(\pi-\alpha)+2k\pi$。" "\n"
        r"在区间 $\left[\dfrac\pi4,\dfrac{5\pi}2\right]$ 内逐个检查：" "\n"
        r"· $k=0$：$t=\alpha$（需 $\alpha\ge\frac\pi4$ 才在区间内）；$t=\pi-\alpha\in\left(\frac\pi2,\pi\right)$ ✓（恒在区间内）。" "\n"
        r"· $k=1$：$t=2\pi+\alpha\in\left(2\pi,\frac{5\pi}2\right)$ ✓（恒在区间内）；$t=3\pi-\alpha$，需 $3\pi-\alpha\le\frac{5\pi}2$ 即 $\alpha\ge\frac\pi2$，仅 $\alpha=\frac\pi2$ 时成立（此时与 $2\pi+\alpha$ 重合）。" "\n"
        r"**恰有三个根的条件：** $t=\alpha$ 必须在区间内，即 $\alpha\ge\dfrac\pi4$；且 $\alpha<\dfrac\pi2$（否则只有两根）。" "\n"
        r"$\therefore\alpha\in\left[\dfrac\pi4,\dfrac\pi2\right)$。" "\n"
        r"三个根对应的相位为 $t_1=\alpha$、$t_2=\pi-\alpha$、$t_3=2\pi+\alpha$。" "\n"
        r"由 $x=\dfrac{t-\frac\pi4}2$：" "\n"
        r"$x_1+x_2+x_3=\dfrac{t_1+t_2+t_3-\frac{3\pi}4}2=\dfrac{\alpha+(\pi-\alpha)+(2\pi+\alpha)-\frac{3\pi}4}2=\dfrac{3\pi+\alpha-\frac{3\pi}4}2=\dfrac{\frac{9\pi}4+\alpha}2=\dfrac{9\pi}8+\dfrac\alpha2$。" "\n"
        r"由 $\alpha\in\left[\dfrac\pi4,\dfrac\pi2\right)$：" "\n"
        r"$x_1+x_2+x_3\in\left[\dfrac{9\pi}8+\dfrac\pi8,\ \dfrac{9\pi}8+\dfrac\pi4\right)=\left[\dfrac{10\pi}8,\dfrac{11\pi}8\right)=\left[\dfrac{5\pi}4,\dfrac{11\pi}8\right)$。"
    ),
    'review': (
        r"★ 题干、答案完整 ✓（答案提取为 `5π 4 , 11π 8`，我据推导确定左端为**闭**、右端为**开**）；" "\n"
        r"**本题详解未提供，全部由我独立推导并用答案验证** ✓" "\n"
        r"**独立验算（数值扫描，完全独立）**：" "\n"
        r"① **扫描验证和的取值**：" "\n"
        r"· $a=\frac{\sqrt2}2=0.707107$：$\alpha=\frac\pi4$，和 $=\frac{9\pi}8+\frac\pi8=\frac{10\pi}8=\frac{5\pi}4=3.926991$ ✓✓✓" "\n"
        r"· $a=0.8$：$\alpha=0.927295$，和 $=3.997939$ ✓" "\n"
        r"· $a=0.95$：$\alpha=1.253236$，和 $=4.160910$ ✓" "\n"
        r"· $a=0.999$：$\alpha=1.526071$，和 $=4.297327\to\frac{11\pi}8=4.319690$ ✓✓✓" "\n"
        r"**和确实跑遍 $[\frac{5\pi}4,\frac{11\pi}8)$**" "\n"
        r"② **$a=\frac{\sqrt2}2$ 时确实有三根**：$t=\frac\pi4,\frac{3\pi}4,\frac{9\pi}4$。" "\n"
        r"对应 $x=\frac{t-\pi/4}2$：$x=0$、$x=\frac{\pi/2}2=\frac\pi4$、$x=\frac{2\pi}2=\pi$。" "\n"
        r"都在 $[0,\frac{9\pi}8]$ 内（$\pi=1.0\pi<\frac{9\pi}8=1.125\pi$ ✓）✓✓✓" "\n"
        r"和 $=0+\frac\pi4+\pi=\frac{5\pi}4$ ✓✓✓ **左端闭，确认**" "\n"
        r"③ **$a$ 略小于 $\frac{\sqrt2}2$ 时只有两根**：取 $a=0.70$，$\alpha=\arcsin0.70=0.7754<\frac\pi4=0.7854$。" "\n"
        r"$t=\alpha$ 不在 $[\frac\pi4,\frac{5\pi}2]$ 内 ⟹ 只有 $t=\pi-\alpha$ 与 $2\pi+\alpha$ 两根 ✓✓✓ **故 $\frac{5\pi}4$ 是下确界且可取**" "\n"
        r"④ **$a\to1$ 时**：$\alpha\to\frac\pi2$，$t=\alpha=\frac\pi2$、$t=\pi-\alpha=\frac\pi2$ **两根重合** ⟹ 只有 $2$ 个不同根 ✗" "\n"
        r"故 $\alpha<\frac\pi2$ 严格 ⟹ **右端开** ✓✓✓" "\n"
        r"⑤ **$t=3\pi-\alpha$ 为何不计**：$3\pi-\alpha\le\frac{5\pi}2=2.5\pi$ ⟺ $\alpha\ge0.5\pi$，与 $\alpha<\frac\pi2$ 矛盾 ✓✓✓" "\n"
        r"⑥ **和的公式复核**：$t_1+t_2+t_3=\alpha+(\pi-\alpha)+(2\pi+\alpha)=3\pi+\alpha$ ✓✓✓" "\n"
        r"$\frac{3\pi+\alpha-\frac{3\pi}4}{2}=\frac{\frac{12\pi-3\pi}4+\alpha}2=\frac{\frac{9\pi}4+\alpha}2=\frac{9\pi}8+\frac\alpha2$ ✓✓✓" "\n"
        r"**答案 $\left[\frac{5\pi}4,\frac{11\pi}8\right)$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（三角方程根的个数 ⟹ 参数范围）**：" "\n"
        r"① ⭐⭐ **令 $t=\omega x+\varphi$ 换元，先算 $t$ 的区间**：" "\n"
        r"本题 $t\in[\frac\pi4,\frac{5\pi}2]$（**长度超过一个周期 $2\pi$**！这是能有三根的前提）；" "\n"
        r"② ⭐⭐ **写出 $\sin t=a$ 的通解并逐个 $k$ 检验是否在区间内**：" "\n"
        r"$t=\alpha+2k\pi$ 与 $t=(\pi-\alpha)+2k\pi$ —— **必须对 $k=0,1,2,\dots$ 逐个判断**，" "\n"
        r"这是「数根」的标准流程，比画图可靠；" "\n"
        r"③ ⭐⭐ **「恰有 $n$ 个根」⟹ 列出每个根的存在条件 ⟹ 取交集**：" "\n"
        r"本题三个条件：$\alpha\ge\frac\pi4$（第一根存在）、$\alpha<\frac\pi2$（避免根重合）、$3\pi-\alpha>\frac{5\pi}2$（第四根不存在）。" "\n"
        r"**交集即 $\alpha\in[\frac\pi4,\frac\pi2)$** ✓" "\n"
        r"④ ⭐ **三根之和的公式**：$t_1+t_2+t_3=3\pi+\alpha$ —— " "\n"
        r"注意 $\alpha$ 与 $-\alpha$ **没有完全抵消**（$+\alpha$ 出现两次、$-\alpha$ 一次）⟹ 净剩 $+\alpha$。" "\n"
        r"**这类「和」的题往往有漂亮的抵消，算完要检查是否真的抵消干净**；" "\n"
        r"⑤ ⚠ **开闭端点逐个判断**：" "\n"
        r"· 左端：$a=\frac{\sqrt2}2$ 时确实三根（含 $x=0$）⟹ **闭**；" "\n"
        r"· 右端：$a\to1$ 时两根重合 ⟹ **开**。" "\n"
        r"**填空题的区间开闭是最容易丢分的地方，必须逐端验证**；" "\n"
        r"⑥ ⚠ **$\alpha=\arcsin a$ 的值域是 $(0,\frac\pi2]$**：" "\n"
        r"$a=1$ 时 $\alpha=\frac\pi2$，此时 $\sin t=1$ 在区间内只有 $t=\frac\pi2,\frac{5\pi}2$ 两根 —— **务必单独检验 $a=1$**。"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-176'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-176-E1',
}

QS = [T341_E1, T341_V1, T341_V2, T341_V3,
      T375_E1, T375_V2, T375_V3,
      T206_V3,
      T203_E1, T203_V1,
      T176_V1, T176_E1]
