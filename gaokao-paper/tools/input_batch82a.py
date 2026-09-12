# -*- coding: utf-8 -*-
r"""第82批：圆锥曲线截面（Dandelin）、棱柱截面、值域、数列（13 题）

M-T-291（4）、M-T-290（2）、M-T-185（3）、M-T-254（4）

## ★★ 13 题我全部独立验算（坐标法 / 代数 / 数值）

| 题 | 我的验算 | 答案 |
|---|---|---|
| M-T-291-E1 | $a=\frac R{\cos\theta}$、$b=R$ ⟹ $e=\sqrt{1-\cos^2\theta}=\sin\theta=\frac12$ | **A** |
| M-T-291-V1 | 建系得截面 $x+z=0$，代入锥面得 $t^2=\sqrt2\,s$ ⟹ $2p=\sqrt2$ | **抛物线，$\sqrt2$** |
| M-T-291-V2 | $\sin\alpha=\frac2d$、$\sin\beta=\frac4d$ ⟹ $\frac{1-16/d^2}{1-4/d^2}=\frac12$ ⟹ $d=2\sqrt7$ | **$2\sqrt7$** |
| M-T-291-V3 | $\tan\alpha=\frac23$、直角在 $A_1$ ⟹ $A_2P=13$、$2a=12$、$a-c=2$ ⟹ $e=\frac23$ | **$\frac23$** |
| M-T-290-E1 | 最小 $=a^2=1$、最大 $=a\sqrt{a^2+h^2}=\sqrt{10}$ ⟹ $a=1,h=3$ | **$3$** |
| M-T-290-V1 | 截面积分 $\int_0^2\frac{(2-z/2)^2}2dz=\frac73$ ⟹ $8-\frac73=\frac{17}3$ | **$17:7$** |
| M-T-185-E1 | $x=4+2\sin^2t$ ⟹ $y=2\sqrt2\sin(t+\frac\pi3)$，$t+\frac\pi3\in[\frac\pi3,\frac{5\pi}6]$ | **$[\sqrt2,2\sqrt2]$** |
| M-T-185-V2 | $x=2\cos\theta$ ⟹ $y=2\sqrt2\cos(\theta+\frac\pi4)$ | **$[-2\sqrt2,2]$** |
| M-T-185-V3 | $(\sqrt{r-t}-1)^2+(\sqrt t-1)^2=1$ ⟹ $r=3+2\sqrt2\sin(\alpha+\frac\pi4)$ | **$[3-2\sqrt2,3+2\sqrt2]$** |
| M-T-254-E1 | $\frac{T_{n+1}}{T_n}=2\frac{T_n}{T_{n-1}}$ ⟹ $a_{n+1}=2a_n$ ⟹ $S_{10}=1023$ | **$1023$** |
| M-T-254-V1 | $a_n=\frac{T_n}{T_{n-1}}=\frac{1/(n+1)}{1/n}=\frac n{n+1}$ | **$\frac n{n+1}$** |
| M-T-254-V2 | $a_{2020}>1>a_{2021}>0$ ⟹ $T_{2020}$ 最大 ⟹ C 错 | **C** |
| M-T-254-V3 | $T_n+a_n=1$ ⟹ $\frac1{T_n}-\frac1{T_{n-1}}=1$ ⟹ $T_n=\frac1{n+1}$、$\frac{a_n}{T_n}=n$ | **$\frac1{n+1}$；$\frac{n(n+1)}2$** |

## 三处根号丢失（提取文本）

- **M-T-290-E1**：题面 `10` 实为 $\sqrt{10}$（否则 $a=1$ 时 $h=\sqrt{99}$，体积不是 $3$）
- **M-T-291-V1**：答案 `2` 实为 $\sqrt2$（通径 $=2p=\sqrt2$，我建系代入锥面确认）
- **M-T-185-E1**：答案 `[ 2,2 2]` 实为 $[\sqrt2,2\sqrt2]$

## 一题跳过

**M-T-185-V1**（$|a-b|+|b-c|+2|c-a|$ 最大值，答案 `8`）：按字面取 $a=4,b=c=-4$ 得 $24\neq8$，且原书详解中
$x=z\cos\theta,y=z\sin\theta$ 与 $x+y=z$ 矛盾（需 $\cos\theta+\sin\theta=1$）。判定为失真，不录。

## 两处题干残缺的还原依据

**M-T-291-V1**：题干在「若 M」处被截断。由「$F$ 是 $EO$ 的中点」且焦点满足 $s_F=\frac{\sqrt2}4=\frac p2$
（我算出 $E\to F$ 的 $s$ 位移恰为 $\frac{\sqrt2}4$）⟹ **$F$ 就是焦点**，故补为「$MN$ 过点 $F$」。

**M-T-185-V3**：题干 `r - 2 t - 2 r - t + 1 = 0` 实为 $r-2\sqrt t-2\sqrt{r-t}+1=0$。
还原依据：配方后应为 $(\sqrt{r-t}-1)^2+(\sqrt t-1)^2=1$，代入 $r+1=2\sqrt t+2\sqrt{r-t}$ **恒成立**。
"""

T291_E1 = {
    'type': '选择',
    'stem_text': (
        r"如图，一个底面半径为 $R$ 的圆柱被与其底面所成角为 $\theta$（$0^\circ<\theta<90^\circ$）的平面所截，截面是一个椭圆，"
        r"当 $\theta$ 为 $30^\circ$ 时，这个椭圆的离心率为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac12$"),
        ('B', r"$\dfrac{\sqrt3}2$"),
        ('C', r"$\dfrac13$"),
        ('D', r"$\dfrac{\sqrt3}3$"),
    ],
    'answer': 'A',
    'analysis': (
        r"短半轴 $b=R$（等于圆柱半径），长半轴 $a=\dfrac R{\cos\theta}$（沿斜面方向被拉长 $\frac1{\cos\theta}$ 倍）。"
        r"于是 $e=\sqrt{1-\frac{b^2}{a^2}}=\sqrt{1-\cos^2\theta}=\sin\theta$，代入 $\theta=30^\circ$ 得 $e=\frac12$。"
    ),
    'solution': (
        r"设椭圆的长半轴为 $a$、短半轴为 $b$、半焦距为 $c$。" "\n"
        r"**短半轴**：截面在「垂直于倾斜方向」上的宽度不受影响，等于圆柱的直径 ⟹ $2b=2R$，即 $b=R$。" "\n"
        r"**长半轴**：沿倾斜方向，截面被拉长了 $\dfrac1{\cos\theta}$ 倍 ⟹ $2a=\dfrac{2R}{\cos30^\circ}=\dfrac{2R}{\sqrt3/2}=\dfrac{4\sqrt3R}3$，" "\n"
        r"即 $a=\dfrac{2\sqrt3R}3$。" "\n"
        r"$\therefore c=\sqrt{a^2-b^2}=\sqrt{\dfrac{4\cdot3R^2}9-R^2}=\sqrt{\dfrac{4R^2}3-R^2}=\sqrt{\dfrac{R^2}3}=\dfrac{\sqrt3R}3$。" "\n"
        r"$\therefore e=\dfrac ca=\dfrac{\sqrt3R/3}{2\sqrt3R/3}=\dfrac12$。故选 A。" "\n"
        r"**一般结论**：$e=\sqrt{1-\dfrac{b^2}{a^2}}=\sqrt{1-\dfrac{R^2}{R^2/\cos^2\theta}}=\sqrt{1-\cos^2\theta}=\sin\theta$。"
    ),
    'review': (
        r"★ 题干、选项、答案、详解完整 ✓。原书详解：「设椭圆的长半轴为 $a$，短半轴为 $b$，半焦距为 $c$。根据题意可知，$2b=2R$，$2a=\frac{2R}{\cos30^\circ}=\frac{4\sqrt3R}3$。" "\n"
        r"$\therefore c=\sqrt{a^2-b^2}=\sqrt{\frac{4\cdot3R^2}9-R^2}=\frac{\sqrt3}3R$，所以椭圆的离心率 $e=\frac ca=\frac12$，选项 A 正确。故选：A.」" "\n"
        r"—— **$2b=2R$、$2a=\frac{4\sqrt3R}3$、$c=\frac{\sqrt3}3R$、$e=\frac12$、答案 A 全部一致** ✓✓✓" "\n"
        r"**独立验算（一般公式，完全独立）**：" "\n"
        r"① **建立模型**：设圆柱轴沿 $z$，底面圆 $x^2+y^2=R^2$。截面平面与底面成 $\theta$ 角，" "\n"
        r"取截面沿 $y$ 轴方向（宽度不变），沿 $x$ 方向倾斜。" "\n"
        r"在截面内取坐标：横向 $y\in[-R,R]$（不变），纵向 $s$ 满足 $s\cos\theta=x$ ⟹ $s=\frac x{\cos\theta}$。" "\n"
        r"代入 $x^2+y^2=R^2$：$\left(s\cos\theta\right)^2+y^2=R^2$ ⟹ $\dfrac{s^2}{R^2/\cos^2\theta}+\dfrac{y^2}{R^2}=1$。" "\n"
        r"$\therefore a=\dfrac R{\cos\theta}$、$b=R$ ✓✓✓" "\n"
        r"② **$e$ 的一般公式**：$e=\sqrt{1-\dfrac{b^2}{a^2}}=\sqrt{1-\dfrac{R^2}{R^2/\cos^2\theta}}=\sqrt{1-\cos^2\theta}=\sin\theta$ ✓✓✓" "\n"
        r"**这是本题最大的收获：圆柱斜截椭圆的离心率就等于 $\sin\theta$**" "\n"
        r"③ **代入 $\theta=30^\circ$**：$e=\sin30^\circ=\frac12=0.5$ ✓✓✓" "\n"
        r"④ **边界检验**：" "\n"
        r"· $\theta=0$（截面平行于底面）⟹ $e=\sin0=0$ ⟹ 圆 ✓✓✓" "\n"
        r"· $\theta\to90^\circ$ ⟹ $e\to1$、$a\to\infty$ ✓✓✓ **物理意义自洽**" "\n"
        r"⑤ **数值核对**：$a=\frac{2\sqrt3}3R=1.154701R$、$b=R$、$c=\frac{\sqrt3}3R=0.577350R$。" "\n"
        r"$\sqrt{a^2-b^2}=\sqrt{1.333333-1}R=\sqrt{0.333333}R=0.577350R$ ✓✓✓" "\n"
        r"$e=\frac{0.577350}{1.154701}=0.500000$ ✓✓✓" "\n"
        r"⑥ **选项排除**：$\frac{\sqrt3}2=0.866$、$\frac13=0.333$、$\frac{\sqrt3}3=0.577$ 都不等于 $0.5$ ✓✓✓" "\n"
        r"**答案 A 正确** ✓" "\n"
        r"**⭐⭐ 通法（圆柱斜截 / 圆锥曲截面）**：" "\n"
        r"① ⭐⭐ **圆柱斜截椭圆：$b=R$、$a=\dfrac R{\cos\theta}$、$e=\sin\theta$**（$\theta$ = 截面与底面所成角）。" "\n"
        r"**三个量一起记** —— 记住 $e=\sin\theta$ 就省掉全部计算；" "\n"
        r"② ⭐⭐ **推导口诀：垂直方向不变、倾斜方向放大 $\frac1{\cos\theta}$**：" "\n"
        r"**短轴就是圆柱直径**（不被拉伸），**长轴是拉伸后的直径**；" "\n"
        r"③ ⭐ **用「边界检验」验证公式**：" "\n"
        r"$\theta=0$ ⟹ 圆（$e=0$）；$\theta\to90^\circ$ ⟹ $e\to1$。" "\n"
        r"**任何新推出的离心率公式都该做这两个检验**；" "\n"
        r"④ ⚠ **注意 $\theta$ 是哪个角**：" "\n"
        r"本题明确说「与**底面**所成角」。若给的是「与**轴**所成角」$\gamma$，则 $\theta=90^\circ-\gamma$、$e=\cos\gamma$；" "\n"
        r"⑤ ⭐ **圆锥截线的对应结论**（与本批 V2/V3 呼应）：" "\n"
        r"圆锥半顶角 $\alpha$、截面与轴夹角 $\beta$ ⟹ $e=\dfrac{\cos\beta}{\cos\alpha}$。" "\n"
        r"$\beta>\alpha$ ⟹ 椭圆；$\beta=\alpha$ ⟹ 抛物线；$\beta<\alpha$ ⟹ 双曲线。"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-291'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-291-E1',
}

T291_V1 = {
    'type': '填空',
    'stem_text': (
        r"在底面半径和高均为 $1$ 的圆锥中，$AB$、$CD$ 是底面圆 $O$ 的两条互相垂直的直径，$E$ 是母线 $PB$ 的中点，"
        r"$F$ 是线段 $EO$ 的中点。已知过 $CD$ 与 $E$ 的平面与圆锥侧面的交线是以 $E$ 为顶点的圆锥曲线的一部分，"
        r"则该曲线为 ____；$M,N$ 是该曲线上的两点，$MN\parallel CD$ 且 $MN$ 过点 $F$，则 $\lvert MN\rvert=$ ____。"
    ),
    'opts': [],
    'answer': r"抛物线；$\sqrt2$",
    'analysis': (
        r"建系得截面平面 $x+z=0$，而母线 $PA$ 的方向 $(1,0,-1)$ 与之平行 ⟹ 截线为抛物线。"
        r"在截面内取坐标代入锥面 $x^2+y^2=(1-z)^2$ 得 $t^2=\sqrt2\,s$，故 $2p=\sqrt2$；$F$ 恰为焦点（$s_F=\frac{\sqrt2}4=\frac p2$）⟹ $MN=2p=\sqrt2$。"
    ),
    'solution': (
        r"**建系**：以底面圆心 $O$ 为原点，底面为 $z=0$ 平面，$P(0,0,1)$，$A(1,0,0)$、$B(-1,0,0)$、$C(0,1,0)$、$D(0,-1,0)$。" "\n"
        r"底面半径 $1$、高 $1$ ⟹ 母线 $PA$ 长 $\sqrt2$，锥面方程 $x^2+y^2=(1-z)^2$。" "\n"
        r"$E$ 是 $PB$ 中点 ⟹ $E\left(-\frac12,0,\frac12\right)$。" "\n"
        r"**截面平面**：过 $C(0,1,0)$、$D(0,-1,0)$、$E\left(-\frac12,0,\frac12\right)$。" "\n"
        r"$\vec{CD}=(0,-2,0)$，$\vec{CE}=\left(-\frac12,-1,\frac12\right)$，法向量 $=\vec{CD}\times\vec{CE}=\left(\frac12,0,\frac12\right)\propto(1,0,1)$。" "\n"
        r"平面方程：$x+z=0$（代入 $C$：$0+0=0$ ✓；代入 $E$：$-\frac12+\frac12=0$ ✓）。" "\n"
        r"**判定曲线类型**：母线 $PA$ 的方向 $\vec{PA}=A-P=(1,0,-1)$，与法向量 $(1,0,1)$ 点积 $=1-1=0$" "\n"
        r"⟹ **$PA\parallel$ 截面** ⟹ 由圆锥曲线的定义，截线为**抛物线**。" "\n"
        r"**求参数**：在截面内取正交坐标 $\vec u=\dfrac{(1,0,-1)}{\sqrt2}$（轴向）、$\vec v=(0,1,0)$（即 $CD$ 方向），以 $E$ 为原点：" "\n"
        r"点为 $E+s\vec u+t\vec v$，即 $x=-\frac12+\frac s{\sqrt2}$、$y=t$、$z=\frac12-\frac s{\sqrt2}$。" "\n"
        r"代入锥面 $x^2+y^2=(1-z)^2$：" "\n"
        r"$\left(-\frac12+\frac s{\sqrt2}\right)^2+t^2=\left(\frac12+\frac s{\sqrt2}\right)^2$ ⟹ $\frac14-\frac s{\sqrt2}+\frac{s^2}2+t^2=\frac14+\frac s{\sqrt2}+\frac{s^2}2$" "\n"
        r"⟹ $t^2=\dfrac{2s}{\sqrt2}=\sqrt2\,s$。" "\n"
        r"与标准式 $t^2=2ps$ 对比得 $2p=\sqrt2$，即 $p=\dfrac{\sqrt2}2$。" "\n"
        r"**$F$ 是焦点**：$F$ 为 $EO$ 中点 ⟹ $F\left(-\frac14,0,\frac14\right)$。" "\n"
        r"$\vec{EF}=\left(\frac14,0,-\frac14\right)=\frac{\sqrt2}4\vec u$ ⟹ $s_F=\dfrac{\sqrt2}4=\dfrac p2$ ✓ **$F$ 恰为焦点**。" "\n"
        r"**通径**：$MN\parallel CD$ 即 $MN\perp$ 轴，又过焦点 $F$ ⟹ $MN$ 是**通径**，$\lvert MN\rvert=2p=\sqrt2$。"
    ),
    'review': (
        r"★ 题干在「若 M」处被**截断**，我据详解与 $F$ 的几何意义补为「$MN$ 过点 $F$」；" "\n"
        r"**答案 `2` 实为 $\sqrt2$（根号丢失）** —— 我建系代入锥面独立确认。" "\n"
        r"原书详解：「由已知底面半径和高均为 $1$，得 $AP=\sqrt2$，又 $E$ 为 $PB$ 中点，$OE=\frac12AP=\frac{\sqrt2}2$，且 $OE\parallel AP$，所以 $AP\parallel$ 平面 $CDE$，根据圆锥曲线的定义可知截面与圆锥母线平行时，曲线为抛物线。" "\n"
        r"又 $F$ 为 $OE$ 中点，故 $\frac p2=\frac12OE=\frac{\sqrt2}4$，$p=\frac{\sqrt2}2$，又 $OP\perp$ 底面，故 $OP\perp CD$，由 $CD\perp AB$，$AB\cap AP=A$，故 $CD\perp$ 平面 $PAB$，$CD\perp OE$，又 $MN\parallel CD$，故 $MN$ 为抛物线的通径，$MN=2p=\sqrt2$.」" "\n"
        r"—— **$AP=\sqrt2$、$OE=\frac{\sqrt2}2$、$OE\parallel AP$、$AP\parallel$ 平面 $CDE$、抛物线、$\frac p2=\frac{\sqrt2}4$、$p=\frac{\sqrt2}2$、通径 $MN=2p$ 全部一致** ✓✓✓" "\n"
        r"（原书末行 OCR 成 `$MN=2p=2$`，但 $\frac p2=\frac{\sqrt2}4$ 已确定 $p=\frac{\sqrt2}2$，故 $2p=\sqrt2$ —— **末行的 `2` 漏了根号**）" "\n"
        r"**独立验算（坐标法，完全独立）**：" "\n"
        r"① **平面方程**：$\vec{CD}\times\vec{CE}=(0,-2,0)\times(-\frac12,-1,\frac12)$" "\n"
        r"$=\left((-2)(\frac12)-0\cdot(-1),\ 0\cdot(-\frac12)-0\cdot\frac12,\ 0\cdot(-1)-(-2)(-\frac12)\right)=(-1,0,-1)\propto(1,0,1)$ ✓✓✓" "\n"
        r"② **$AP\parallel$ 平面**：$(1,0,-1)\cdot(1,0,1)=1-1=0$ ✓✓✓ **平行，故为抛物线**" "\n"
        r"③ **代入锥面**：$\left(-\frac12+\frac s{\sqrt2}\right)^2=\frac14-2\cdot\frac12\cdot\frac s{\sqrt2}+\frac{s^2}2=\frac14-\frac s{\sqrt2}+\frac{s^2}2$ ✓" "\n"
        r"$\left(\frac12+\frac s{\sqrt2}\right)^2=\frac14+\frac s{\sqrt2}+\frac{s^2}2$ ✓" "\n"
        r"相减：$t^2=\frac{2s}{\sqrt2}=\sqrt2\,s$ ✓✓✓" "\n"
        r"④ **$p$ 的确定**：标准式 $t^2=2ps$ ⟹ $2p=\sqrt2$ ⟹ $p=\frac{\sqrt2}2=0.707107$ ✓✓✓" "\n"
        r"⑤ **$F$ 是焦点的验证**：$E=(-\frac12,0,\frac12)$、$F=(-\frac14,0,\frac14)$。" "\n"
        r"$\vec{EF}=(\frac14,0,-\frac14)$；$\vec u=\frac{(1,0,-1)}{\sqrt2}$。" "\n"
        r"$s_F=\vec{EF}\cdot\vec u=\frac{\frac14+\frac14}{\sqrt2}=\frac{1/2}{\sqrt2}=\frac{\sqrt2}4=0.353553$。" "\n"
        r"$\frac p2=\frac{\sqrt2}4=0.353553$ ✓✓✓ **$F$ 确为焦点**" "\n"
        r"（顺带：$OE=\frac{\sqrt2}2=0.707107$ ✓，$\frac12OE=\frac{\sqrt2}4$ ✓ 与原书一致）" "\n"
        r"⑥ **通径长**：在 $s=\frac p2=\frac{\sqrt2}4$ 处，$t^2=\sqrt2\cdot\frac{\sqrt2}4=\frac24=\frac12$ ⟹ $t=\pm\frac1{\sqrt2}$。" "\n"
        r"$\lvert MN\rvert=2\cdot\frac1{\sqrt2}=\sqrt2=1.414214$ ✓✓✓" "\n"
        r"⑦ **确认不是 $2$**：若 $MN=2$ 则 $t=\pm1$，需 $t^2=1=\sqrt2 s$ ⟹ $s=\frac1{\sqrt2}=\frac{\sqrt2}2\neq\frac p2$ ✓✓✓ **不过焦点**" "\n"
        r"**答案：抛物线，$\sqrt2$** ✓" "\n"
        r"**⭐⭐ 通法（判断截面截圆锥得什么曲线）**：" "\n"
        r"① ⭐⭐ **坐标法是判定截线类型最稳的办法**：" "\n"
        r"**把平面方程与锥面方程联立，看得到的是 $t^2\propto s$（抛物线）、封闭二次（椭圆）还是双支（双曲线）**。" "\n"
        r"比「想象空间图形」可靠得多；" "\n"
        r"② ⭐⭐ **「母线 $\parallel$ 截面」⟹ 抛物线**：" "\n"
        r"判定只需一步：**母线方向向量 $\cdot$ 平面法向量 $=0$**；" "\n"
        r"③ ⭐⭐ **求 $p$ 的技巧：在截面内建立正交坐标**：" "\n"
        r"取截面内两个正交方向（一个沿对称轴、一个垂直），把点写成 $E+s\vec u+t\vec v$，" "\n"
        r"**代入锥面后 $s^2$ 项会自动抵消**（因为母线平行）⟹ 直接得到 $t^2=2ps$；" "\n"
        r"④ ⭐ **通径 $=2p$，且过焦点且垂直于轴**：" "\n"
        r"**「过焦点 + 垂直于轴」是判定通径的两个条件，缺一不可**；" "\n"
        r"⑤ ⚠ **注意 $p$ 与 $\frac p2$ 的区别**：" "\n"
        r"标准式 $t^2=2ps$ 中，焦点在 $s=\frac p2$ 处，通径长 $=2p$。" "\n"
        r"**本题 $\frac p2=\frac{\sqrt2}4$ 与通径 $2p=\sqrt2$ 相差 $4$ 倍** —— 别混；" "\n"
        r"⑥ ⚠ **答案里的 `2` 常常是 $\sqrt2$ 丢了根号**：" "\n"
        r"**凡是答案对不上，第一反应就是检查根号**。"
    ),
    'difficulty': 0.94,
    'topics': ['M-T-291'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-291-V1',
}

T291_V2 = {
    'type': '填空',
    'stem_text': (
        r"如图，用一个平面去截圆锥，得到的截口曲线是椭圆。在圆锥内放两个大小不同的球，使得它们分别与圆锥的侧面相切。"
        r"椭圆截面与两球相切于椭圆的两个焦点 $F_1,F_2$。过椭圆上一点 $P$ 作圆锥的母线，分别与两个球相切于点 $M,N$。"
        r"由球和圆的几何性质可知，$PN=PF_1$，$PM=PF_2$。已知两球半径分别为 $1$ 和 $3$，椭圆的离心率为 $\dfrac{\sqrt2}2$，则两球的球心距离为 ____。"
    ),
    'opts': [],
    'answer': r"$2\sqrt7$",
    'analysis': (
        r"设圆锥半顶角 $\alpha$、截面与轴夹角 $\beta$，则 $e=\frac{\cos\beta}{\cos\alpha}$。"
        r"内切球半径 $r$ 的球心在轴上距顶点 $\frac r{\sin\alpha}$ ⟹ $d=\frac{3-1}{\sin\alpha}=\frac2{\sin\alpha}$；"
        r"两球分居截面两侧 ⟹ $d\sin\beta=1+3=4$。联立 $\frac{1-16/d^2}{1-4/d^2}=\frac12$ ⟹ $d=2\sqrt7$。"
    ),
    'solution': (
        r"设圆锥的半顶角（轴与母线的夹角）为 $\alpha$，截面与轴的夹角为 $\beta$。" "\n"
        r"由圆锥曲线的统一性质：$e=\dfrac{\cos\beta}{\cos\alpha}$。" "\n"
        r"**第一步：球心位置。** 半径为 $r$ 的球内切于圆锥侧面（球心在轴上），" "\n"
        r"球心到母线的距离 $=r$，而球心到顶点的轴向距离为 $L$ 时该距离 $=L\sin\alpha$ ⟹ $L=\dfrac r{\sin\alpha}$。" "\n"
        r"$\therefore$ 两球心（都在轴上）的轴向距离 $d=\dfrac3{\sin\alpha}-\dfrac1{\sin\alpha}=\dfrac2{\sin\alpha}$，即 $\sin\alpha=\dfrac2d$。" "\n"
        r"**第二步：球到截面的距离。** 设截面与轴交于点 $Q$。轴上距 $Q$ 为 $x$ 的点到截面的距离为 $x\sin\beta$。" "\n"
        r"两球在截面**两侧**（椭圆的两个 Dandelin 球分居截面上下），且球与截面相切：" "\n"
        r"$r_1=1$、$r_2=3$，两段距离之和即两球心的轴向距离 $d$ ⟹ $d\sin\beta=1+3=4$，即 $\sin\beta=\dfrac4d$。" "\n"
        r"**第三步：代入离心率。**" "\n"
        r"$e^2=\dfrac{\cos^2\beta}{\cos^2\alpha}=\dfrac{1-\sin^2\beta}{1-\sin^2\alpha}=\dfrac{1-\frac{16}{d^2}}{1-\frac4{d^2}}=\dfrac{d^2-16}{d^2-4}=\left(\dfrac{\sqrt2}2\right)^2=\dfrac12$。" "\n"
        r"$\therefore 2(d^2-16)=d^2-4$ ⟹ $2d^2-32=d^2-4$ ⟹ $d^2=28$ ⟹ $d=2\sqrt7$。"
    ),
    'review': (
        r"★ 题干完整 ✓；**原书详解在中途被截断**（停在「由已知条件 $PN=PF_1$」），后续由我完整推导并用答案验证 ✓" "\n"
        r"原书已给出的部分：「作出圆锥的轴截面如图所示，圆锥面与两球 $O_1,O_2$ 相切于 $B,A$ 两点，则 $O_1B\perp AB$，$O_2A\perp AB$，过 $O_1$ 作 $O_1D\perp O_2A$，垂足为 $D$，连接 $O_1F_2$、$O_2F_1$，设 $F_1F_2$ 与 $OO_1$ 交于点 $C$，设两球的球心距离为 $d$。" "\n"
        r"在 $\mathrm{Rt}\triangle O_1O_2D$ 中，$DO_2=3-1=2$，$\therefore O_1D=\sqrt{d^2-4}$，$\therefore\cos\angle DO_1O_2=\frac{\sqrt{d^2-4}}d$；" "\n"
        r"$\because\triangle F_1O_2C\sim\triangle F_2O_1C$，$\therefore\frac{CO_2}{O_2F_1}=\frac{CO_1}{O_1F_2}$，$\because CO_2=d-CO_1$，$\therefore\frac{d-CO_1}3=\frac{CO_1}1$，解得 $CO_1=\frac d4$，$\therefore CF_2=\sqrt{O_1C^2-1}=\frac{\sqrt{d^2-16}}4$，$\therefore\cos\angle O_1CF_2=\frac{CF_2}{O_1C}=\frac{\sqrt{d^2-16}}d$」" "\n"
        r"—— 我核对了原书的中间结果：设 $\angle DO_1O_2$ 是轴与母线的夹角 $=\alpha$，则 $\cos\alpha=\frac{\sqrt{d^2-4}}d$ ⟺ $\sin\alpha=\frac2d$ ✓；" "\n"
        r"$\angle O_1CF_2$ 是轴与截面的夹角 $=\beta$，$\cos\beta=\frac{\sqrt{d^2-16}}d$ ⟺ $\sin\beta=\frac4d$ ✓ —— **与原书完全等价** ✓✓✓" "\n"
        r"**独立验算（完全独立）**：" "\n"
        r"① **内切球的球心位置**：轴截面内，球心 $O$ 在轴上，到母线（与轴成 $\alpha$）的距离为 $r$。" "\n"
        r"设顶点到球心的轴向距离 $L$，则距离 $=L\sin\alpha=r$ ⟹ $L=\frac r{\sin\alpha}$ ✓✓✓" "\n"
        r"② **两球心距离**：$d=L_2-L_1=\frac3{\sin\alpha}-\frac1{\sin\alpha}=\frac2{\sin\alpha}$ ✓✓✓" "\n"
        r"③ **球心到截面的距离**：截面与轴交于 $Q$，轴上距 $Q$ 为 $x$ 的点到截面的距离 $=x\sin\beta$（$\beta$ = 轴与截面的夹角）✓✓✓" "\n"
        r"④ **两球分居两侧**：$x_1\sin\beta=1$、$x_2\sin\beta=3$，且 $x_1+x_2=d$ ⟹ $d\sin\beta=4$ ✓✓✓" "\n"
        r"（**这正是 Dandelin 双球的标准构型**：两球在截面两侧，切点即两焦点）" "\n"
        r"⑤ **解 $d$**：$\frac{d^2-16}{d^2-4}=\frac12$ ⟹ $2d^2-32=d^2-4$ ⟹ $d^2=28$ ⟹ $d=\sqrt{28}=2\sqrt7=5.291503$ ✓✓✓" "\n"
        r"⑥ **回代检验**：" "\n"
        r"$\sin\alpha=\frac2{2\sqrt7}=\frac1{\sqrt7}=0.377964$ ⟹ $\alpha=22.2077^\circ$，$\cos\alpha=\sqrt{\frac67}=0.925820$。" "\n"
        r"$\sin\beta=\frac4{2\sqrt7}=\frac2{\sqrt7}=0.755929$ ⟹ $\beta=49.1066^\circ$，$\cos\beta=\sqrt{\frac37}=0.654654$。" "\n"
        r"$e=\frac{0.654654}{0.925820}=0.707107=\frac{\sqrt2}2$ ✓✓✓ **完全吻合**" "\n"
        r"⑦ **椭圆的判定**：$\beta=49.11^\circ>\alpha=22.21^\circ$ ⟹ 椭圆 ✓✓✓ **自洽**" "\n"
        r"⑧ **答案形式**：$2\sqrt7=5.2915$（**注意不是 $\sqrt{28}$ 的简化失误：$2\sqrt7=\sqrt{28}$** ✓）" "\n"
        r"**答案 $2\sqrt7$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（Dandelin 双球）**：" "\n"
        r"① ⭐⭐ **统一离心率公式：$e=\dfrac{\cos\beta}{\cos\alpha}$**（$\alpha$ = 半顶角，$\beta$ = 截面与轴的夹角）。" "\n"
        r"检验：$\beta=90^\circ$（垂直轴）⟹ $e=0$ 圆 ✓；$\beta=\alpha$ ⟹ $e=1$ 抛物线 ✓；$\beta<\alpha$ ⟹ $e>1$ 双曲线 ✓；" "\n"
        r"② ⭐⭐ **内切球半径 $r$ ⟹ 球心在轴上距顶点 $\dfrac r{\sin\alpha}$**：" "\n"
        r"**这是把「球」与「圆锥」联系起来的关键一步**；" "\n"
        r"③ ⭐⭐ **两球球心距 $d$ 与半径和/差的关系**：" "\n"
        r"· 轴向：$d=\dfrac{\lvert r_2-r_1\rvert}{\sin\alpha}$" "\n"
        r"· 垂直截面方向：$d\sin\beta=r_1+r_2$（**两球在截面两侧**）" "\n"
        r"**两个方向用不同的运算（差 vs 和），这是本题的核心**；" "\n"
        r"④ ⭐ **切点即焦点**：这是 Dandelin 定理的核心结论（$PN=PF_1$、$PM=PF_2$ ⟹ $PF_1+PF_2=MN=$ 常数）；" "\n"
        r"⑤ ⚠ **别把 $\alpha$、$\beta$ 搞反**：" "\n"
        r"**$\alpha$ 是轴与母线（越小越尖），$\beta$ 是轴与截面**。" "\n"
        r"椭圆要求 $\beta>\alpha$ —— **算完务必检验这个不等式**；" "\n"
        r"⑥ ⭐ **若详解被截断，用「中间量是否吻合」验证自己的推导**：" "\n"
        r"本题我核对了原书的 $\cos\alpha=\frac{\sqrt{d^2-4}}d$ 与 $\cos\beta=\frac{\sqrt{d^2-16}}d$，" "\n"
        r"**两条都与我独立推出的 $\sin\alpha=\frac2d$、$\sin\beta=\frac4d$ 等价** ⟹ 推导可靠。"
    ),
    'difficulty': 0.96,
    'topics': ['M-T-291'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-291-V2',
}

T291_V3 = {
    'type': '填空',
    'stem_text': (
        r"在圆锥内放一个球，使得它与圆锥的侧面、截面都相切，球与截面相切于点 $F_1$。在截口曲线上任取一点 $A$，过 $A$ 作圆锥的母线，"
        r"与球相切于点 $C$，由球和圆的几何性质可以知道 $AF_1=AC$。已知该球半径为 $2$，截面与圆锥侧面的交线（椭圆）的两个顶点为 $A_1,A_2$，"
        r"$A_1P=5$（$P$ 为圆锥顶点），且球与母线 $A_1P$ 相切于点 $E$ 满足 $EP=3$，则该椭圆的离心率为 ____。"
    ),
    'opts': [],
    'answer': r"$\dfrac23$",
    'analysis': (
        r"球半径 $2$、$EP=3$ ⟹ $\tan\alpha=\frac23$（$\alpha$ 为半顶角）⟹ $\tan2\alpha=\frac{12}5$。"
        r"轴截面中 $\angle PA_1A_2=90^\circ$ ⟹ $A_1A_2=A_1P\tan2\alpha=12=2a$ ⟹ $a=6$；"
        r"切点 $F_1$ 为焦点且 $A_1F_1=2=a-c$ ⟹ $c=4$ ⟹ $e=\frac23$。"
    ),
    'solution': (
        r"**第一步：求半顶角 $\alpha$。** 球心 $O$ 在轴上，$OE\perp A_1P$，$OE=2$（半径），$EP=3$。" "\n"
        r"$\therefore\tan\angle EPO=\dfrac{OE}{EP}=\dfrac23$，其中 $\angle EPO$ 即轴与母线的夹角 $\alpha$ ⟹ $\tan\alpha=\dfrac23$。" "\n"
        r"**第二步：求顶点角。** $\tan\angle A_1PA_2=\tan2\alpha=\dfrac{2\tan\alpha}{1-\tan^2\alpha}=\dfrac{2\cdot\frac23}{1-\frac49}=\dfrac{\frac43}{\frac59}=\dfrac{12}5$。" "\n"
        r"**第三步：求长轴。** 在轴截面内，$\triangle A_1PA_2$ 中 $A_1P\perp A_1A_2$（见 review 中的坐标验证），" "\n"
        r"$\therefore A_1A_2=A_1P\cdot\tan\angle A_1PA_2=5\times\dfrac{12}5=12$。" "\n"
        r"$\therefore 2a=12$，$a=6$。" "\n"
        r"**第四步：求半焦距。** 球与截面相切的切点 $F_1$ 是椭圆的一个焦点，" "\n"
        r"且由切线长性质 $A_1F_1=A_1E=A_1P-EP=5-3=2$。" "\n"
        r"$F_1$ 在长轴 $A_1A_2$ 上，故 $A_1F_1=a-c=2$ ⟹ $c=6-2=4$。" "\n"
        r"$\therefore e=\dfrac ca=\dfrac46=\dfrac23$。"
    ),
    'review': (
        r"★ 答案 $\frac23$ 完整 ✓；**题干在「于是 $AE+AF=$」处被截断**，我据详解补全了条件（球半径 $2$、$A_1P=5$、$EP=3$）；" "\n"
        r"详解完整给出了推导，我**另外用坐标系独立验证了直角关系**（$A_1P\perp A_1A_2$ 且 $A_2P=13$）✓" "\n"
        r"原书详解：「$\odot O$ 切 $A_1A_2$ 于 $F_1$，切 $A_1P$ 于 $E$，$A_1P=5$，球半径为 $2$，所以 $EP=3$，$\tan\angle EPO=\frac23$，" "\n"
        r"$\tan\angle A_1PA_2=\frac{2\times\frac23}{1-\frac49}=\frac{12}5$，$\triangle A_1PA_2$ 中，$A_1P=5$，$\therefore A_1A_2=A_1P\times\frac{12}5=12$，故 $2a=12$，$a=6$，" "\n"
        r"根据椭圆在圆锥中截面与二球相切的切点为椭圆的焦点知：球 $O$ 与 $A_1A_2$ 相切的切点 $F_1$ 为椭圆的一个焦点，且 $A_1F_1=2$，$\therefore a-c=2$，$c=4$，椭圆的离心率为 $e=\frac ca=\frac23$。故答案为：$\frac23$」" "\n"
        r"—— **$EP=3$、$\tan\alpha=\frac23$、$\tan2\alpha=\frac{12}5$、$A_1A_2=12$、$a=6$、$A_1F_1=2$、$c=4$、$e=\frac23$ 全部一致** ✓✓✓" "\n"
        r"**独立验算（坐标系完整验证，完全独立）**：" "\n"
        r"① **重建整个构型**：顶点 $P=(0,0)$，轴沿 $y$ 轴，半顶角 $\alpha$ 满足 $\tan\alpha=\frac23$" "\n"
        r"⟹ $\sin\alpha=\frac2{\sqrt{13}}=0.554700$，$\cos\alpha=\frac3{\sqrt{13}}=0.832050$。" "\n"
        r"球心 $O$ 在轴上，到母线距离 $=2$ ⟹ $L\sin\alpha=2$ ⟹ $L=\frac2{0.554700}=\sqrt{13}=3.605551$。" "\n"
        r"切点 $E$ 在母线上：$PE=L\cos\alpha=\sqrt{13}\cdot\frac3{\sqrt{13}}=3$ ✓✓✓ **与题设 $EP=3$ 吻合**" "\n"
        r"② **$A_1$ 的位置**：$PA_1=5$，沿母线方向 $(\sin\alpha,\cos\alpha)$：" "\n"
        r"$A_1=5(0.554700,0.832050)=(2.773500,4.160251)$。" "\n"
        r"③ **$A_2$ 的位置（由「直角在 $A_1$」推出）**：$A_2$ 在另一条母线方向 $(-\sin\alpha,\cos\alpha)$，" "\n"
        r"设 $PA_2=n$，则 $A_2=n(-0.554700,0.832050)$。" "\n"
        r"$\vec{A_1P}=(-2.773500,-4.160251)$，$\vec{A_1A_2}=(-0.5547n-2.7735,\ 0.83205n-4.160251)$。" "\n"
        r"令点积 $=0$：$(-2.7735)(-0.5547n-2.7735)+(-4.160251)(0.83205n-4.160251)=0$" "\n"
        r"⟹ $1.53816n+7.69230-3.46154n+17.30769=0$ ⟹ $-1.92338n+25.0=0$ ⟹ $n=13.0$ ✓✓✓" "\n"
        r"（**$A_2P=13$，与勾股 $5^2+12^2=169=13^2$ 一致** ✓）" "\n"
        r"④ **$A_1A_2$ 长度**：$A_2=13(-0.554700,0.832050)=(-7.211103,10.816654)$。" "\n"
        r"$\lvert A_1A_2\rvert=\sqrt{(2.7735+7.2111)^2+(4.160251-10.816654)^2}=\sqrt{9.984603^2+(-6.656403)^2}$" "\n"
        r"$=\sqrt{99.692+44.308}=\sqrt{144.000}=12.0$ ✓✓✓ **$2a=12$，$a=6$**" "\n"
        r"⑤ **验证球与截面（直线 $A_1A_2$）相切**：$O=(0,3.605551)$ 到直线 $A_1A_2$ 的距离。" "\n"
        r"方向单位向量 $=\frac{(-9.984603,6.656403)}{12}=(-0.832050,0.554700)$。" "\n"
        r"$\vec{A_1O}=(-2.773500,-0.554700)$。" "\n"
        r"距离 $=\lvert(-2.7735)(0.554700)-(-0.5547)(-0.83205)\rvert=\lvert-1.53816-0.46154\rvert=1.99970\approx2$ ✓✓✓" "\n"
        r"**等于球半径 $2$，相切成立** ✓✓✓" "\n"
        r"⑥ **切点 $F_1$ 与 $A_1F_1$**：投影长度 $=\vec{A_1O}\cdot$单位$=(-2.7735)(-0.83205)+(-0.5547)(0.5547)$" "\n"
        r"$=2.30770-0.30769=2.00001$ ⟹ $A_1F_1=2$ ✓✓✓ **与 $a-c=2$ 一致**" "\n"
        r"⑦ **$e$**：$c=a-2=6-2=4$，$e=\frac46=\frac23=0.666667$ ✓✓✓" "\n"
        r"**答案 $\frac23$ 正确，且整个构型完全自洽** ✓" "\n"
        r"**⭐⭐ 通法（单球 Dandelin：求椭圆的 $a,c$）**：" "\n"
        r"① ⭐⭐ **球半径 $r$ 与 $EP$ 给出半顶角**：$\tan\alpha=\dfrac r{EP}$。" "\n"
        r"由「$O$ 在轴上、$OE\perp$ 母线」得直角三角形 $OEP$ —— **这是唯一的入口**；" "\n"
        r"② ⭐⭐ **长轴 $2a=A_1A_2$，在轴截面内求解**：" "\n"
        r"$\triangle A_1PA_2$ 中已知 $\angle A_1PA_2=2\alpha$ 与 $A_1P$，再用几何关系定 $A_1A_2$。" "\n"
        r"本题的特殊性在于 $\angle PA_1A_2=90^\circ$（我已用坐标验证），故 $A_1A_2=A_1P\tan2\alpha$；" "\n"
        r"③ ⭐⭐ **切点即焦点，且 $A_1F_1=A_1E$（切线长定理）**：" "\n"
        r"**从顶点 $A_1$ 引球的两条切线（沿母线到 $E$、沿截面到 $F_1$）长度相等** —— 这是求 $c$ 的关键；" "\n"
        r"④ ⭐ **$A_1F_1=a-c$**：顶点到最近焦点的距离就是 $a-c$ ✓；" "\n"
        r"⑤ ⚠ **$\tan2\alpha$ 要用倍角公式**：$\frac{2\tan\alpha}{1-\tan^2\alpha}$ —— " "\n"
        r"本题 $\tan\alpha=\frac23<\frac{\sqrt2}2$ 附近，$\tan2\alpha$ 会显著变大（$\frac{12}5$），**别误用 $\sin2\alpha$**；" "\n"
        r"⑥ ⭐ **详解残缺时的最强验证：重建坐标系**：" "\n"
        r"**把顶点、球心、两个顶点、切点全部算出来，检查距离是否等于球半径** —— " "\n"
        r"本题第⑤步算出 $O$ 到 $A_1A_2$ 的距离 $=2.000$，是最硬的证据。"
    ),
    'difficulty': 0.96,
    'topics': ['M-T-291'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-291-V3',
}

T290_E1 = {
    'type': '填空',
    'stem_text': (
        r"已知正四棱柱中 $A_1C_1$、$B_1D_1$ 的交点为 $O_1$，$AC$、$BD$ 的交点为 $O_2$，连接 $O_1O_2$，点 $O$ 为 $O_1O_2$ 的中点。"
        r"过点 $O$ 且与直线 $AB$ 平行的平面截这个正四棱柱所得截面面积的最小值和最大值分别为 $1$ 和 $\sqrt{10}$，"
        r"则正四棱柱 $ABCD-A_1B_1C_1D_1$ 的体积为 ____。"
    ),
    'opts': [],
    'answer': r"$3$",
    'analysis': (
        r"截面是矩形，一边恒为 $a$（$\parallel AB$），另一边 $L$ 在过中心的 $a\times h$ 矩形内。"
        r"$L_{\min}=a$（截面平行底面）、$L_{\max}=\sqrt{a^2+h^2}$（对角面 $A_1B_1CD$）。"
        r"$a^2=1$、$a\sqrt{a^2+h^2}=\sqrt{10}$ ⟹ $a=1$、$h=3$ ⟹ $V=3$。"
    ),
    'solution': (
        r"设正四棱柱底面边长为 $a$、高为 $h$。" "\n"
        r"因截面平面 $\parallel AB$，故它与棱柱的交是一个矩形，其中**一边恒等于 $AB=a$**。" "\n"
        r"另一边的长度等于「该平面与垂直于 $AB$ 的截面」的交线长度。" "\n"
        r"在垂直于 $AB$ 的正方形截面（尺寸 $a\times h$，即 $BC$ 与高的方向）中，" "\n"
        r"平面过中心 $O$，交线是一条过中心的线段，长度 $L$ 满足：" "\n"
        r"· 当交线平行于底面（$L=a$）时最小：$L_{\min}=a$ ⟹ $S_{\min}=a\cdot a=a^2$；" "\n"
        r"· 当交线沿该矩形的对角线时最长：$L_{\max}=\sqrt{a^2+h^2}$ ⟹ $S_{\max}=a\sqrt{a^2+h^2}$。" "\n"
        r"（最大时截面即对角面 $A_1B_1CD$：其一边 $A_1B_1=a$、另一边 $B_1C=\sqrt{a^2+h^2}$，" "\n"
        r"且该平面过中心 $O$：以 $A$ 为原点时平面为 $z+\frac ha y=h$，代入 $O(\frac a2,\frac a2,\frac h2)$ 得 $\frac h2+\frac h2=h$ ✓。）" "\n"
        r"由已知：$a^2=1$ ⟹ $a=1$；$a\sqrt{a^2+h^2}=\sqrt{10}$ ⟹ $\sqrt{1+h^2}=\sqrt{10}$ ⟹ $h^2=9$ ⟹ $h=3$。" "\n"
        r"$\therefore V=a^2h=1\times3=3$。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓；**题面「$10$」实为 $\sqrt{10}$（根号丢失）** —— " "\n"
        r"若按 $10$，则 $a\sqrt{a^2+h^2}=10$ 与 $a=1$ 得 $h=\sqrt{99}$，$V=3\sqrt{11}\ne3$，与答案矛盾。" "\n"
        r"原书详解：「设正四棱柱的底面边长为 $a$，高为 $h$，由题知当截面平行于平面 $ABCD$ 时，截面面积最小；当截面为平面 $A_1B_1CD$ 时，截面面积最大。" "\n"
        r"因为过点 $O$ 且与直线 $AB$ 平行的平面截这个正四棱柱所得截面面积的最小值和最大值分别为 $1$ 和 $\sqrt{10}$，所以 $\begin{cases}a^2=1\\a\sqrt{a^2+h^2}=\sqrt{10}\end{cases}$，解得 $\begin{cases}a=1\\h=3\end{cases}$，" "\n"
        r"于是正四棱柱 $ABCD-A_1B_1C_1D_1$ 的体积为 $a^2h=3$。故答案为：$3$.」" "\n"
        r"—— **最小 $=a^2$、最大 $=a\sqrt{a^2+h^2}$、$a=1$、$h=3$、$V=3$ 全部一致** ✓✓✓" "\n"
        r"（原题面提取为 `1 和 10`，但原书详解的方程组第二式右端是 $\sqrt{10}$，**可反推题面漏了根号**）" "\n"
        r"**独立验算（完全独立）**：" "\n"
        r"① **为什么一边恒为 $a$**：截面 $\parallel AB$，且 $AB$ 是底面的一条边。" "\n"
        r"过棱柱内一点作与 $AB$ 平行的平面，其在 $AB$ 方向上的截线长度恒为 $a$（等于棱长）✓✓✓" "\n"
        r"② **另一边的范围**：垂直于 $AB$ 的方向上，截面退化为 $a\times h$ 矩形内过中心的一条线段。" "\n"
        r"过矩形中心的弦长范围：$\left[a,\sqrt{a^2+h^2}\right]$（**最短是平行于短边 $a$ 的方向，最长是对角线**）✓✓✓" "\n"
        r"③ **对角面过中心的验证**：以 $A$ 为原点，$A_1(0,0,h)$、$B_1(a,0,h)$、$C(a,a,0)$、$D(0,a,0)$。" "\n"
        r"平面 $A_1B_1CD$：由 $A_1$、$B_1$ 知 $y=0$ 时 $z=h$；由 $D$ 知 $y=a$ 时 $z=0$ ⟹ $z=h\left(1-\frac ya\right)$。" "\n"
        r"代入 $O\left(\frac a2,\frac a2,\frac h2\right)$：$\frac h2=h\left(1-\frac12\right)=\frac h2$ ✓✓✓ **$O$ 在平面上**" "\n"
        r"④ **面积**：$S_{\min}=a\cdot a=a^2$；$S_{\max}=a\cdot\sqrt{a^2+h^2}$（$B_1C$ 的长度 $=\sqrt{a^2+h^2}$ ✓）✓✓✓" "\n"
        r"⑤ **解方程**：$a^2=1$ ⟹ $a=1$；$1\cdot\sqrt{1+h^2}=\sqrt{10}$ ⟹ $1+h^2=10$ ⟹ $h=3$ ✓✓✓" "\n"
        r"⑥ **体积**：$V=a^2h=1\times1\times3=3$ ✓✓✓" "\n"
        r"⑦ **检验**：$S_{\max}=1\cdot\sqrt{1+9}=\sqrt{10}=3.1623$ ✓；$S_{\min}=1$ ✓ ✓✓✓" "\n"
        r"**答案 $3$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（过定点的平行截面）**：" "\n"
        r"① ⭐⭐ **「截面 $\parallel$ 某条棱」⟹ 一边恒等于该棱长**：" "\n"
        r"本题一边恒为 $AB=a$ —— **先把「不变的那一维」固定下来，问题立刻降维**；" "\n"
        r"② ⭐⭐ **降维到垂直截面**：" "\n"
        r"剩下的就是在「垂直于该棱的矩形」内，**过中心作一条弦，求弦长范围**。" "\n"
        r"**过矩形中心的弦：最短 $=$ 短边，最长 $=$ 对角线** —— 可直接记；" "\n"
        r"③ ⭐ **最值对应的两个特殊位置**：" "\n"
        r"· 最小 ⟹ 截面 $\parallel$ 底面；· 最大 ⟹ 对角面。" "\n"
        r"**填空题直接代这两个位置即可，不必真的求函数**；" "\n"
        r"④ ⚠ **务必验证「对角面过定点 $O$」**：" "\n"
        r"这是最值能取到的前提（本题恰好成立，因为 $O$ 是棱柱的**中心**）；" "\n"
        r"⑤ ⚠ **答案与题面对不上时，检查题面是否丢了根号**：" "\n"
        r"本题 `10` ⟹ $\sqrt{10}$。**用答案反推题面是很有效的还原手段**；" "\n"
        r"⑥ ⭐ **一般化**：正 $n$ 棱柱、长方体同理，" "\n"
        r"**「过中心、平行于某棱」的截面面积范围 $=\left[\text{棱长}\times\text{短边},\ \text{棱长}\times\text{面对角线}\right]$**。"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-290'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-290-E1',
}

T290_V1 = {
    'type': '填空',
    'stem_text': (
        r"正方体 $ABCD-A_1B_1C_1D_1$ 中，$E,F$ 分别是棱 $B_1C_1$、$C_1D_1$ 的中点，则正方体被截面 $BEFD$ 分成两部分的体积之比为 ____。"
    ),
    'opts': [],
    'answer': r"$17:7$（或 $7:17$）",
    'analysis': (
        r"设棱长 $2$（体积 $8$）。截面平面为 $2x+2y-z=4$，含 $C_1$ 一侧的体积 $=\int_0^2\frac{(2-z/2)^2}2dz=\frac73$，"
        r"另一侧 $=\frac{17}3$，故比为 $17:7$。"
    ),
    'solution': (
        r"设正方体棱长为 $2$，体积 $V=8$。" "\n"
        r"以 $A$ 为原点建系：$A(0,0,0)$、$B(2,0,0)$、$C(2,2,0)$、$D(0,2,0)$、$B_1(2,0,2)$、$C_1(2,2,2)$、$D_1(0,2,2)$。" "\n"
        r"$E$ 为 $B_1C_1$ 中点 ⟹ $E(2,1,2)$；$F$ 为 $C_1D_1$ 中点 ⟹ $F(1,2,2)$。" "\n"
        r"**截面平面**：过 $B(2,0,0)$、$E(2,1,2)$、$F(1,2,2)$。" "\n"
        r"$\vec{BE}=(0,1,2)$、$\vec{BF}=(-1,2,2)$，法向量 $=\vec{BE}\times\vec{BF}=(1\cdot2-2\cdot2,\ 2\cdot(-1)-0\cdot2,\ 0\cdot2-1\cdot(-1))=(-2,-2,1)$。" "\n"
        r"平面方程：$-2(x-2)-2(y-0)+(z-0)=0$ ⟹ $2x+2y-z=4$。" "\n"
        r"（检验 $D(0,2,0)$：$0+4-0=4$ ✓，故 $D$ 确在平面上，截面为四边形 $BEFD$ ✓）" "\n"
        r"**判断分侧**：$C_1(2,2,2)$ 代入得 $4+4-2=6>4$，故 $C_1$ 在 $2x+2y-z>4$ 一侧。" "\n"
        r"**计算含 $C_1$ 的那部分体积**：在高度 $z$ 处（$0\le z\le2$），条件为 $x+y\ge 2+\dfrac z2$，" "\n"
        r"在 $[0,2]^2$ 中这是一直角三角形，两直角边长 $=2-\dfrac z2$，面积 $=\dfrac{\left(2-\frac z2\right)^2}2$。" "\n"
        r"$V_1=\displaystyle\int_0^2\frac{\left(2-\frac z2\right)^2}2\,dz$。令 $u=2-\frac z2$，$dz=-2du$，$z=0\to u=2$、$z=2\to u=1$：" "\n"
        r"$V_1=\dfrac12\int_1^2 u^2\cdot 2\,du=\int_1^2u^2du=\left[\dfrac{u^3}3\right]_1^2=\dfrac{8-1}3=\dfrac73$。" "\n"
        r"$\therefore V_2=8-\dfrac73=\dfrac{17}3$。" "\n"
        r"$\therefore$ 两部分体积之比 $=\dfrac{17}3:\dfrac73=17:7$（或 $7:17$）。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书详解：「设正方体的棱长为 $2$，则正方体的体积为 $8$，因为 $E,F$ 分别是棱 $B_1C_1$、$C_1D_1$ 的中点，" "\n"
        r"所以棱台 $EFC_1$-$BDC$ 的体积为 $\frac13\times2\times\left(\frac12\times2\times2+\frac12\times1\times1+\sqrt{\frac12\times2\times2\times\frac12\times1\times1}\right)=\frac73$，" "\n"
        r"所以另一部分的体积为 $8-\frac73=\frac{17}3$，所以正方体被截面 $BEFD$ 分成两部分的体积之比为 $17:7$ 或 $7:17$，故答案为：$17:7$ 或 $7:17$」" "\n"
        r"—— **棱长 $2$、体积 $8$、棱台 $EFC_1$-$BDC$、$\frac73$、$\frac{17}3$、$17:7$ 全部一致** ✓✓✓" "\n"
        r"**独立验算（积分法，与原书棱台法完全不同）**：" "\n"
        r"① **平面方程**：$\vec{BE}\times\vec{BF}$ 中间分量 $=2\cdot(-1)-0\cdot2=-2$ ✓；" "\n"
        r"第三分量 $=0\cdot2-1\cdot(-1)=1$ ✓ ⟹ $(-2,-2,1)$。" "\n"
        r"代入 $B$：$-2(0)-2(0)+0=0$ ✓ ⟹ $-2x+4-2y+z=0$ ⟹ $2x+2y-z=4$ ✓✓✓" "\n"
        r"② **$D$ 在平面上**：$2\cdot0+2\cdot2-0=4$ ✓✓✓ **四边形 $BEFD$ 成立**" "\n"
        r"③ **截面积分**：高度 $z$ 处，$2x+2y-z\ge4$ ⟹ $x+y\ge 2+\frac z2=t$（$2\le t\le3$）。" "\n"
        r"在 $[0,2]^2$ 中，$x+y\ge t$ 的部分是顶点为 $(t-2,2)$、$(2,t-2)$、$(2,2)$ 的直角三角形，" "\n"
        r"两直角边长 $=2-(t-2)=4-t=2-\frac z2$ ⟹ 面积 $=\frac{(2-z/2)^2}{2}$ ✓✓✓" "\n"
        r"④ **积分值**：$z=0$ 时面积 $=2$（$\triangle BDC$：$B(2,0,0)$、$D(0,2,0)$、$C(2,2,0)$，" "\n"
        r"底 $BD=2\sqrt2$、$C$ 到 $BD$ 的距离 $=\frac{|2+2-2|}{\sqrt2}=\sqrt2$ ⟹ 面积 $=\frac12\cdot2\sqrt2\cdot\sqrt2=2$ ✓）；" "\n"
        r"$z=2$ 时面积 $=0.5$（$\triangle EFC_1$ 直角边 $1,1$ ⟹ $0.5$ ✓）✓✓✓ **与原书棱台的两底面积一致**" "\n"
        r"$\int_0^2\frac{(2-z/2)^2}2dz=\frac73$ ✓✓✓" "\n"
        r"⑤ **棱台公式交叉验证**：$\frac13\times h\times(S_1+S_2+\sqrt{S_1S_2})=\frac13\times2\times(2+0.5+\sqrt{1})=\frac23\times3.5=\frac73$ ✓✓✓" "\n"
        r"**两种方法结果完全一致**" "\n"
        r"⑥ **比值**：$\frac{17}3:\frac73=17:7$ ✓✓✓" "\n"
        r"⑦ **检验总和**：$\frac{17}3+\frac73=\frac{24}3=8$ ✓ 等于正方体体积 ✓✓✓" "\n"
        r"**答案 $17:7$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（截面分体积）**：" "\n"
        r"① ⭐⭐ **建系写平面方程 ⟹ 分层积分**：" "\n"
        r"**求截面以上/以下的体积，分层积分是最稳的办法**（不用猜几何体的形状）；" "\n"
        r"② ⭐⭐ **截面积是 $z$ 的二次函数时，体积可用棱台公式**：" "\n"
        r"若上下底平行且截面积随高度**线性地按平方变化**（相似截面），则 $V=\frac h3(S_1+S_2+\sqrt{S_1S_2})$。" "\n"
        r"**本题截面积 $=\frac{(2-z/2)^2}2$，两底相似 ⟹ 棱台公式适用** ✓；" "\n"
        r"③ ⭐ **先验证第四个点也在平面上**：" "\n"
        r"题称「截面 $BEFD$」是四边形 —— **代入 $D$ 检验**（$2\cdot0+2\cdot2-0=4$ ✓）" "\n"
        r"可确认平面确实切出的是四边形而非三角形/五边形；" "\n"
        r"④ ⭐ **判断哪一侧：代入一个「角」上的点**（如 $C_1$）看符号；" "\n"
        r"⑤ ⚠ **比值要写全**：题目问「两部分的体积之比」，**两种顺序 $17:7$ 与 $7:17$ 都要写**（原书答案即如此）；" "\n"
        r"⑥ ⚠ **棱长设为 $2$ 是为了让中点坐标是整数**：" "\n"
        r"**设参数为 $2$（而不是 $1$）可避开分数** —— 这是一个很实用的小技巧。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-290'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-290-V1',
}

T185_E1 = {
    'type': '填空',
    'stem_text': r"若 $y=\sqrt{x-4}+\sqrt{18-3x}$，则 $y$ 的取值范围是 ____。",
    'opts': [],
    'answer': r"$[\sqrt2,2\sqrt2]$",
    'analysis': (
        r"定义域 $x\in[4,6]$。令 $x=4+2\sin^2t$（$t\in[0,\frac\pi2]$），则 $y=\sqrt2\sin t+\sqrt6\cos t=2\sqrt2\sin\left(t+\frac\pi3\right)$；"
        r"$t+\frac\pi3\in[\frac\pi3,\frac{5\pi}6]$，$\sin\in[\frac12,1]$ ⟹ $y\in[\sqrt2,2\sqrt2]$。"
    ),
    'solution': (
        r"由 $\begin{cases}x-4\ge0\\18-3x\ge0\end{cases}$ 得 $4\le x\le6$。" "\n"
        r"令 $x=4+2\sin^2t$，$t\in\left[0,\dfrac\pi2\right]$（此时 $2\sin^2t\in[0,2]$，恰好覆盖 $[4,6]$）。" "\n"
        r"则 $x-4=2\sin^2t$ ⟹ $\sqrt{x-4}=\sqrt2\sin t$；" "\n"
        r"$18-3x=18-12-6\sin^2t=6\cos^2t$ ⟹ $\sqrt{18-3x}=\sqrt6\cos t$。" "\n"
        r"$\therefore y=\sqrt2\sin t+\sqrt6\cos t=\sqrt{2+6}\cdot\sin(t+\varphi)=2\sqrt2\sin\left(t+\dfrac\pi3\right)$" "\n"
        r"（其中 $\tan\varphi=\dfrac{\sqrt6}{\sqrt2}=\sqrt3$ ⟹ $\varphi=\dfrac\pi3$）。" "\n"
        r"$\because t\in\left[0,\dfrac\pi2\right]$，$\therefore t+\dfrac\pi3\in\left[\dfrac\pi3,\dfrac{5\pi}6\right]$。" "\n"
        r"在该区间上 $\sin$ 的最大值为 $1$（在 $\frac\pi2$ 处，含于区间内），" "\n"
        r"最小值为端点比较：$\sin\frac\pi3=\frac{\sqrt3}2$、$\sin\frac{5\pi}6=\frac12$ ⟹ 最小 $=\dfrac12$。" "\n"
        r"$\therefore y\in\left[2\sqrt2\cdot\dfrac12,\ 2\sqrt2\cdot1\right]=[\sqrt2,2\sqrt2]$。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓（答案提取为 `[ 2,2 2]`，实为 $[\sqrt2,2\sqrt2]$，**根号丢失**）；" "\n"
        r"原书详解：「因为 $y=\sqrt{x-4}+\sqrt{18-3x}$，所以 $\begin{cases}x-4\ge0\\18-3x\ge0\end{cases}$ 解得 $4\le x\le6$，令 $x=4+2\sin^2t$，$t\in[0,\frac\pi2]$，" "\n"
        r"则 $y=\sqrt{4+2\sin^2t-4}+\sqrt{18-3(4+2\sin^2t)}=\sqrt2\sin t+\sqrt6\cos t=2\sqrt2\sin\left(t+\frac\pi3\right)$。" "\n"
        r"因为 $t\in[0,\frac\pi2]$，所以 $t+\frac\pi3\in[\frac\pi3,\frac{5\pi}6]$，所以 $\sin\left(t+\frac\pi3\right)\in[\frac12,1]$，所以 $y\in[\sqrt2,2\sqrt2]$。故答案为：$[\sqrt2,2\sqrt2]$」" "\n"
        r"—— **定义域 $[4,6]$、$x=4+2\sin^2t$、$\sqrt2\sin t+\sqrt6\cos t$、$2\sqrt2\sin(t+\frac\pi3)$、$[\frac12,1]$、$[\sqrt2,2\sqrt2]$ 全部一致** ✓✓✓" "\n"
        r"**独立验算（完全独立）**：" "\n"
        r"① **定义域**：$x\ge4$ 且 $x\le6$ ⟹ $[4,6]$ ✓✓✓" "\n"
        r"② **换元的合理性**：$2\sin^2t$ 在 $t\in[0,\frac\pi2]$ 上取遍 $[0,2]$ ⟹ $x$ 取遍 $[4,6]$ ✓✓✓" "\n"
        r"③ **$\sqrt{18-3x}$**：$18-3(4+2\sin^2t)=18-12-6\sin^2t=6(1-\sin^2t)=6\cos^2t$ ✓" "\n"
        r"（$t\in[0,\frac\pi2]$ ⟹ $\cos t\ge0$ ⟹ $\sqrt{6\cos^2t}=\sqrt6\cos t$ ✓ **开方不带绝对值**）" "\n"
        r"④ **辅助角**：$\sqrt{(\sqrt2)^2+(\sqrt6)^2}=\sqrt{8}=2\sqrt2$ ✓；" "\n"
        r"$2\sqrt2\sin(t+\varphi)=2\sqrt2(\sin t\cos\varphi+\cos t\sin\varphi)$，对比 $\sqrt2\sin t+\sqrt6\cos t$：" "\n"
        r"$2\sqrt2\cos\varphi=\sqrt2$ ⟹ $\cos\varphi=\frac12$；$2\sqrt2\sin\varphi=\sqrt6$ ⟹ $\sin\varphi=\frac{\sqrt3}2$ ⟹ $\varphi=\frac\pi3$ ✓✓✓" "\n"
        r"⑤ **端点值检验（直接代入原式）**：" "\n"
        r"· $x=4$：$y=\sqrt0+\sqrt6=\sqrt6=2.449490$。" "\n"
        r"公式：$t=0$ ⟹ $y=2\sqrt2\sin\frac\pi3=2\sqrt2\cdot\frac{\sqrt3}2=\sqrt6=2.449490$ ✓✓✓" "\n"
        r"· $x=6$：$y=\sqrt2+\sqrt0=\sqrt2=1.414214$。" "\n"
        r"公式：$t=\frac\pi2$ ⟹ $y=2\sqrt2\sin\frac{5\pi}6=2\sqrt2\cdot\frac12=\sqrt2$ ✓✓✓ **最小值在 $x=6$ 处**" "\n"
        r"· 最大：$2x+\frac\pi3=\frac\pi2$ ⟹ $t=\frac\pi6$ ⟹ $x=4+2\cdot\frac14=4.5$。" "\n"
        r"代入原式：$y=\sqrt{0.5}+\sqrt{18-13.5}=\sqrt{0.5}+\sqrt{4.5}=0.707107+2.121320=2.828427=2\sqrt2$ ✓✓✓" "\n"
        r"⑥ **最小值是 $\sqrt2$ 不是 $\sqrt6$**：两个端点中，$x=6$ 给 $\sqrt2\approx1.414$ < $x=4$ 给 $\sqrt6\approx2.449$ ✓✓✓" "\n"
        r"（**这正是三角换元法的价值：端点大小一眼看出，而不必逐个代入**）" "\n"
        r"**答案 $[\sqrt2,2\sqrt2]$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（双根式值域：三角换元）**：" "\n"
        r"① ⭐⭐ **形如 $\sqrt{a+kx}+\sqrt{b-kx}$（$x$ 系数互为相反数）⟹ 三角换元**：" "\n"
        r"令被开方式 $=M\sin^2t$ 与 $N\cos^2t$（**平方和为常数**），一步化为 $A\sin t+B\cos t$；" "\n"
        r"② ⭐⭐ **换元后必须重算 $t$ 的范围**：" "\n"
        r"本题 $t\in[0,\frac\pi2]$，但 $\sin(t+\frac\pi3)$ 的区间是 $[\frac\pi3,\frac{5\pi}6]$ —— " "\n"
        r"**相位区间的端点才是判断最值的依据，不是 $t$ 的区间**；" "\n"
        r"③ ⚠ **在相位区间上，$\sin$ 的最值要「看是否含 $\frac\pi2$，否则比较两端」**：" "\n"
        r"本题含 $\frac\pi2$ ⟹ 最大 $1$；两端 $\frac{\sqrt3}2$ 与 $\frac12$ ⟹ 最小 $\frac12$。" "\n"
        r"**漏看端点就会把最小值错成 $\sqrt6$**；" "\n"
        r"④ ⚠ **开方时要确认 $\cos t\ge0$**：" "\n"
        r"若 $t$ 的范围跨过 $\frac\pi2$，则 $\sqrt{\cos^2t}=|\cos t|$ 需分段 —— **本题 $t\in[0,\frac\pi2]$ 安全**；" "\n"
        r"⑤ ⭐ **验证：把 $t$ 的边界值与极值点代回原式算一遍**：" "\n"
        r"本题三个点（$x=4,4.5,6$）全部吻合 ✓ —— **这是最可靠的检验**；" "\n"
        r"⑥ ⭐ **备选方法（导数）**：$y'=\frac1{2\sqrt{x-4}}-\frac3{2\sqrt{18-3x}}=0$ ⟹ $\sqrt{18-3x}=3\sqrt{x-4}$ ⟹ $18-3x=9x-36$ ⟹ $x=4.5$ ✓ 同解。"
    ),
    'difficulty': 0.82,
    'topics': ['M-T-185'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-185-E1',
}

T185_V2 = {
    'type': '填空',
    'stem_text': r"函数 $y=x-\sqrt{4-x^2}$ 的值域为 ____。",
    'opts': [],
    'answer': r"$[-2\sqrt2,2]$",
    'analysis': (
        r"定义域 $[-2,2]$。令 $x=2\cos\theta$（$\theta\in[0,\pi]$），则 $y=2\cos\theta-2\sin\theta=2\sqrt2\cos\left(\theta+\frac\pi4\right)$；"
        r"$\theta+\frac\pi4\in[\frac\pi4,\frac{5\pi}4]$，$\cos\in[-1,\frac{\sqrt2}2]$ ⟹ $y\in[-2\sqrt2,2]$。"
    ),
    'solution': (
        r"由 $4-x^2\ge0$ 得 $-2\le x\le2$。" "\n"
        r"令 $x=2\cos\theta$，$\theta\in[0,\pi]$（此时 $2\cos\theta$ 取遍 $[-2,2]$）。" "\n"
        r"$\because\theta\in[0,\pi]$，$\therefore\sin\theta\ge0$，故 $\sqrt{4-x^2}=\sqrt{4-4\cos^2\theta}=\sqrt{4\sin^2\theta}=2\sin\theta$。" "\n"
        r"$\therefore y=2\cos\theta-2\sin\theta=2\sqrt2\left(\dfrac{\sqrt2}2\cos\theta-\dfrac{\sqrt2}2\sin\theta\right)=2\sqrt2\cos\left(\theta+\dfrac\pi4\right)$。" "\n"
        r"$\because\theta\in[0,\pi]$，$\therefore\theta+\dfrac\pi4\in\left[\dfrac\pi4,\dfrac{5\pi}4\right]$。" "\n"
        r"在该区间上：$\cos$ 的最大值为 $\cos\dfrac\pi4=\dfrac{\sqrt2}2$（$\theta=0$ 处），最小值为 $-1$（在 $\pi$ 处，而 $\pi\in[\frac\pi4,\frac{5\pi}4]$ ✓）。" "\n"
        r"$\therefore y\in\left[2\sqrt2\cdot(-1),\ 2\sqrt2\cdot\dfrac{\sqrt2}2\right]=[-2\sqrt2,2]$。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓（答案提取为 `-2 2,2`，实为 $[-2\sqrt2,2]$，**根号丢失**）；" "\n"
        r"原书详解：「由 $4-x^2\ge0$ 可得 $-2\le x\le2$，即函数的定义域为 $[-2,2]$。所以设 $x=2\cos\theta$，$\theta\in[0,\pi]$，" "\n"
        r"则 $y=2\cos\theta-\sqrt{4-4\cos^2\theta}=2\cos\theta-2\sin\theta=2\sqrt2\cos\left(\theta+\frac\pi4\right)$，因为 $\theta\in[0,\pi]$，所以 $\theta+\frac\pi4\in[\frac\pi4,\frac{5\pi}4]$，" "\n"
        r"所以 $\cos\left(\theta+\frac\pi4\right)\in[-1,\frac{\sqrt2}2]$，所以 $y\in[-2\sqrt2,2]$，所以函数 $y=x-\sqrt{4-x^2}$ 的值域为 $[-2\sqrt2,2]$，故答案为：$[-2\sqrt2,2]$」" "\n"
        r"—— **定义域 $[-2,2]$、$x=2\cos\theta$、$2\cos\theta-2\sin\theta$、$2\sqrt2\cos(\theta+\frac\pi4)$、$[-1,\frac{\sqrt2}2]$、$[-2\sqrt2,2]$ 全部一致** ✓✓✓" "\n"
        r"**独立验算（完全独立）**：" "\n"
        r"① **定义域**：$4-x^2\ge0$ ⟹ $x\in[-2,2]$ ✓✓✓" "\n"
        r"② **$\sin\theta\ge0$ 的确认**：$\theta\in[0,\pi]$ ⟹ $\sin\theta\ge0$ ⟹ $\sqrt{4\sin^2\theta}=2\sin\theta$ ✓✓✓" "\n"
        r"（**这一步是本题的关键**：若取 $\theta\in[-\pi,\pi]$ 就会出现绝对值，必须分段）" "\n"
        r"③ **辅助角**：$2\cos\theta-2\sin\theta=2\sqrt2\left(\frac1{\sqrt2}\cos\theta-\frac1{\sqrt2}\sin\theta\right)=2\sqrt2\cos\left(\theta+\frac\pi4\right)$ ✓✓✓" "\n"
        r"（用 $\cos(A+B)=\cos A\cos B-\sin A\sin B$ 展开验证：$2\sqrt2(\cos\theta\cos\frac\pi4-\sin\theta\sin\frac\pi4)=2\sqrt2(\frac{\sqrt2}2\cos\theta-\frac{\sqrt2}2\sin\theta)=2\cos\theta-2\sin\theta$ ✓）" "\n"
        r"④ **端点与极值点检验（直接代入原式）**：" "\n"
        r"· $x=2$（$\theta=0$）：$y=2-0=2$。" "\n"
        r"公式：$2\sqrt2\cos\frac\pi4=2\sqrt2\cdot\frac{\sqrt2}2=2$ ✓✓✓ **最大值**" "\n"
        r"· $x=-2$（$\theta=\pi$）：$y=-2-0=-2$。" "\n"
        r"公式：$2\sqrt2\cos\frac{5\pi}4=2\sqrt2\cdot(-\frac{\sqrt2}2)=-2$ ✓✓✓" "\n"
        r"· 最小：$\theta+\frac\pi4=\pi$ ⟹ $\theta=\frac{3\pi}4$ ⟹ $x=2\cos\frac{3\pi}4=-\sqrt2$。" "\n"
        r"代入原式：$y=-\sqrt2-\sqrt{4-2}=-\sqrt2-\sqrt2=-2\sqrt2=-2.828427$ ✓✓✓" "\n"
        r"公式：$2\sqrt2\cos\pi=-2\sqrt2$ ✓✓✓" "\n"
        r"⑤ **端点比较**：$x=2$ 给 $2$、$x=-2$ 给 $-2$、内部极值点给 $-2\sqrt2=-2.828$。" "\n"
        r"$\therefore$ 最大 $=2$、最小 $=-2\sqrt2$ ✓✓✓" "\n"
        r"（**注意：最小不在端点，在内部** —— 这正是换元法的价值）" "\n"
        r"⑥ **几何解释**：$y=x-\sqrt{4-x^2}$ 是「半圆 $y_1=\sqrt{4-x^2}$ 与直线 $y_2=x$ 的纵向差」。" "\n"
        r"最小差出现在与直线 $y=x$ 平行的切点处（斜率 $1$），即 $x=-\sqrt2$ 处 ✓✓✓ **与计算一致**" "\n"
        r"**答案 $[-2\sqrt2,2]$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（$\sqrt{a^2-x^2}$ 型 ⟹ 余弦换元）**：" "\n"
        r"① ⭐⭐ **见到 $\sqrt{a^2-x^2}$ ⟹ 令 $x=a\cos\theta$，$\theta\in[0,\pi]$**：" "\n"
        r"这样 $\sqrt{a^2-x^2}=a\sin\theta$ **且 $\sin\theta\ge0$ 自动成立，无需分段**；" "\n"
        r"（若令 $x=a\sin\theta$ 则取 $\theta\in[-\frac\pi2,\frac\pi2]$，此时 $\cos\theta\ge0$ 也自动成立 —— **两种都可以，关键是选对区间**）" "\n"
        r"② ⭐⭐ **$A\cos\theta+B\sin\theta$ 统一化为 $R\cos(\theta\pm\varphi)$**：" "\n"
        r"$R=\sqrt{A^2+B^2}$。**注意符号**：$A\cos\theta-B\sin\theta=R\cos(\theta+\varphi)$，其中 $\tan\varphi=\frac BA$；" "\n"
        r"③ ⚠ **$\cos$ 在 $[\frac\pi4,\frac{5\pi}4]$ 上的最值**：" "\n"
        r"最大在**左端** $\frac\pi4$（$\cos\frac\pi4=\frac{\sqrt2}2$），最小在 $\pi$（$=-1$，**$\pi$ 在区间内**）。" "\n"
        r"**$\cos$ 不像 $\sin$ 那样在 $\frac\pi2$ 取最大 —— 要按区间逐点比较**；" "\n"
        r"④ ⚠ **最小值可能不在端点**：" "\n"
        r"本题最小 $-2\sqrt2$ 在内点 $x=-\sqrt2$，而两端点是 $2$ 与 $-2$。" "\n"
        r"**只看端点会得出错误的值域 $[-2,2]$** —— 这正是最常见的错误；" "\n"
        r"⑤ ⭐ **几何验证法**：把 $y=x-\sqrt{4-x^2}$ 看成「直线减半圆」，" "\n"
        r"**极值在平行切点处** —— 提供快速的直觉检验。"
    ),
    'difficulty': 0.82,
    'topics': ['M-T-185'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-185-V2',
}

T185_V3 = {
    'type': '填空',
    'stem_text': (
        r"设 $r,t\in\mathbb R$ 满足 $r+1=2\sqrt t+2\sqrt{r-t}$，则 $r$ 的取值范围是 ____。"
    ),
    'opts': [],
    'answer': r"$[3-2\sqrt2,3+2\sqrt2]$",
    'analysis': (
        r"条件等价于 $\left(\sqrt{r-t}-1\right)^2+\left(\sqrt t-1\right)^2=1$。令 $\sqrt{r-t}=1+\cos\alpha$、$\sqrt t=1+\sin\alpha$，"
        r"则 $r=(1+\cos\alpha)^2+(1+\sin\alpha)^2=3+2\sqrt2\sin\left(\alpha+\frac\pi4\right)\in[3-2\sqrt2,3+2\sqrt2]$。"
    ),
    'solution': (
        r"由条件 $r+1=2\sqrt t+2\sqrt{r-t}$（需 $t\ge0$、$r\ge t$），移项配方：" "\n"
        r"$\underbrace{(r-t)}_{\text{视作整体}}-2\sqrt{r-t}+1+t-2\sqrt t+1=1$" "\n"
        r"（注意 $r=(r-t)+t$，把 $r$ 拆成两部分分别配方）" "\n"
        r"$\therefore\left(\sqrt{r-t}-1\right)^2+\left(\sqrt t-1\right)^2=1$。" "\n"
        r"令 $\sqrt{r-t}=1+\cos\alpha$、$\sqrt t=1+\sin\alpha$（$\alpha\in[0,2\pi)$），" "\n"
        r"则 $r-t=(1+\cos\alpha)^2$、$t=(1+\sin\alpha)^2$。" "\n"
        r"$\therefore r=(1+\cos\alpha)^2+(1+\sin\alpha)^2$" "\n"
        r"$=(1+2\cos\alpha+\cos^2\alpha)+(1+2\sin\alpha+\sin^2\alpha)=3+2(\sin\alpha+\cos\alpha)=3+2\sqrt2\sin\left(\alpha+\dfrac\pi4\right)$。" "\n"
        r"$\because\alpha\in[0,2\pi)$，$\therefore\sin\left(\alpha+\dfrac\pi4\right)\in[-1,1]$。" "\n"
        r"$\therefore r\in\left[3-2\sqrt2,\ 3+2\sqrt2\right]$。"
    ),
    'review': (
        r"★ 答案完整 ✓；**题干在提取时丢失了两个根号**（原文 `r - 2 t - 2 r - t + 1 = 0` 实为 $r-2\sqrt t-2\sqrt{r-t}+1=0$）；" "\n"
        r"**我的还原依据**：配方后应为 $(\sqrt{r-t}-1)^2+(\sqrt t-1)^2=1$，展开即 $r+1=2\sqrt t+2\sqrt{r-t}$，" "\n"
        r"与原书详解的「配方得 $(r-t-1)^2+(t-1)^2=1$」（OCR 也丢了根号）一致，且与答案 $[3-2\sqrt2,3+2\sqrt2]$ 完全吻合 ✓" "\n"
        r"原书详解：「将（原式）配方得 $(\sqrt{r-t}-1)^2+(\sqrt t-1)^2=1$，设 $\sqrt{r-t}=1+\cos\alpha$，$\sqrt t=1+\sin\alpha$，$\alpha\in[0,2\pi)$，得：" "\n"
        r"$r=(1+\cos\alpha)^2+(1+\sin\alpha)^2=3+2(\sin\alpha+\cos\alpha)=3+2\sqrt2\sin\left(\alpha+\frac\pi4\right)$。" "\n"
        r"又因为 $-1\le\sin\left(\alpha+\frac\pi4\right)\le1$，所以 $r\in[3-2\sqrt2,3+2\sqrt2]$。故答案为：$[3-2\sqrt2,3+2\sqrt2]$」" "\n"
        r"—— **配方形式、换元、$3+2\sqrt2\sin(\alpha+\frac\pi4)$、$[3-2\sqrt2,3+2\sqrt2]$ 全部一致** ✓✓✓" "\n"
        r"**独立验算（完全独立，含恒等式检验）**：" "\n"
        r"① **配方展开验证**：$\left(\sqrt{r-t}-1\right)^2+\left(\sqrt t-1\right)^2$" "\n"
        r"$=(r-t)-2\sqrt{r-t}+1+t-2\sqrt t+1=r-2\sqrt{r-t}-2\sqrt t+2$。" "\n"
        r"令其 $=1$ ⟹ $r-2\sqrt{r-t}-2\sqrt t+1=0$ ⟹ $r+1=2\sqrt t+2\sqrt{r-t}$ ✓✓✓ **与条件恒等**" "\n"
        r"② **换元的合法性**：$\sqrt{r-t}\ge0$、$\sqrt t\ge0$ 恒成立；" "\n"
        r"$1+\cos\alpha\ge0$、$1+\sin\alpha\ge0$ ✓ ✓✓✓ **完全覆盖**" "\n"
        r"③ **$r$ 的表达式**：$r=(r-t)+t=(1+\cos\alpha)^2+(1+\sin\alpha)^2$" "\n"
        r"$=1+2\cos\alpha+\cos^2\alpha+1+2\sin\alpha+\sin^2\alpha=2+2(\sin\alpha+\cos\alpha)+1=3+2(\sin\alpha+\cos\alpha)$ ✓✓✓" "\n"
        r"④ **辅助角**：$2(\sin\alpha+\cos\alpha)=2\sqrt2\sin\left(\alpha+\frac\pi4\right)$ ✓✓✓" "\n"
        r"⑤ **范围**：$\sin\in[-1,1]$ ⟹ $r\in[3-2\sqrt2,3+2\sqrt2]=[0.171573,5.828427]$ ✓✓✓" "\n"
        r"⑥ **构造性验证（取最大/最小点代回原条件）**：" "\n"
        r"· 最大：$\alpha=\frac\pi4$ ⟹ $\sqrt{r-t}=1+\frac{\sqrt2}2=1.707107$、$\sqrt t=1.707107$。" "\n"
        r"$r-t=t=2.914214$ ⟹ $r=5.828427=3+2\sqrt2$ ✓✓✓" "\n"
        r"验证原条件：$r+1=6.828427$；$2\sqrt t+2\sqrt{r-t}=2(1.707107)+2(1.707107)=6.828427$ ✓✓✓ **恒等**" "\n"
        r"· 最小：$\alpha=\frac{5\pi}4$ ⟹ $\sin\alpha=\cos\alpha=-\frac{\sqrt2}2$ ⟹ $\sqrt{r-t}=\sqrt t=1-\frac{\sqrt2}2=0.292893$。" "\n"
        r"$r-t=t=0.085786$ ⟹ $r=0.171573=3-2\sqrt2$ ✓✓✓" "\n"
        r"验证：$r+1=1.171573$；$2(0.292893)+2(0.292893)=1.171573$ ✓✓✓ **恒等**" "\n"
        r"⑦ **中间点抽查**：$\alpha=0$ ⟹ $\sqrt{r-t}=2$、$\sqrt t=1$ ⟹ $r-t=4$、$t=1$、$r=5$。" "\n"
        r"验证：$r+1=6$；$2\sqrt1+2\sqrt4=2+4=6$ ✓✓✓" "\n"
        r"公式：$3+2\sqrt2\sin\frac\pi4=3+2\sqrt2\cdot\frac{\sqrt2}2=3+2=5$ ✓✓✓" "\n"
        r"**答案 $[3-2\sqrt2,3+2\sqrt2]$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（双根号约束 ⟹ 配方成圆 ⟹ 参数方程）**：" "\n"
        r"① ⭐⭐ **识别「两个根号 + 一个线性变量」⟹ 可配方成圆**：" "\n"
        r"本题关键是看出 $r=(r-t)+t$，**把 $r$ 拆成与两个根号对应的两部分**；" "\n"
        r"② ⭐⭐ **配方技巧：把 $\sqrt{X}$ 当整体**：" "\n"
        r"$X-2\sqrt X+1=(\sqrt X-1)^2$ —— **见到 $X$ 与 $\sqrt X$ 同时出现就该想到配方**；" "\n"
        r"③ ⭐⭐ **圆 ⟹ 参数方程**：$(\cdots)^2+(\cdots)^2=1$ 直接令两项为 $\cos\alpha$、$\sin\alpha$（**加 $1$ 保证非负**）；" "\n"
        r"④ ⭐ **求 $r$ 时把 $r$ 写成两部分的和**：" "\n"
        r"$r=(r-t)+t$ —— **不要试图直接解出 $r$**，用「整体」代替；" "\n"
        r"⑤ ⚠ **$3\pm2\sqrt2=(\sqrt2\pm1)^2$**：" "\n"
        r"**这个数出现时，多半与「$(1\pm\sin\alpha)$ 的平方」有关** —— 可当作自检信号；" "\n"
        r"⑥ ⚠ **本题题干丢失了两个根号**：" "\n"
        r"**凡是「方程看着很怪、配方对不上」时，第一反应是检查根号**；" "\n"
        r"⑦ ⭐ **最强的验证：取极值点代回原条件验算恒等式** —— " "\n"
        r"本题最大点、最小点、中间点全部满足 $r+1=2\sqrt t+2\sqrt{r-t}$ ✓✓✓"
    ),
    'difficulty': 0.93,
    'topics': ['M-T-185'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-185-V3',
}

T254_E1 = {
    'type': '填空',
    'stem_text': (
        r"已知数列 $\{a_n\}$ 的前 $n$ 项积为 $T_n$，若对 $\forall n\ge2$，$n\in\mathbb N^*$，都有 $T_{n+1}\cdot T_{n-1}=2T_n^2$ 成立，"
        r"且 $a_1=1$，$a_2=2$，则数列 $\{a_n\}$ 的前 $10$ 项和为 ____。"
    ),
    'opts': [],
    'answer': r"$1023$",
    'analysis': (
        r"由 $T_{n+1}T_{n-1}=2T_n^2$ 得 $\frac{T_{n+1}}{T_n}=2\cdot\frac{T_n}{T_{n-1}}$，即 $a_{n+1}=2a_n$（$n\ge2$）；"
        r"又 $\frac{a_2}{a_1}=2$ ⟹ $\{a_n\}$ 是首项 $1$、公比 $2$ 的等比数列 ⟹ $S_{10}=2^{10}-1=1023$。"
    ),
    'solution': (
        r"$\because T_{n+1}\cdot T_{n-1}=2T_n^2$，两边同除以 $T_nT_{n-1}$（各项非零）：" "\n"
        r"$\dfrac{T_{n+1}}{T_n}\cdot\dfrac{T_{n-1}}{T_{n-1}}\cdot\dfrac1{1}=2\dfrac{T_n}{T_{n-1}}$，即 $\dfrac{T_{n+1}}{T_n}=2\cdot\dfrac{T_n}{T_{n-1}}$。" "\n"
        r"由 $T_{n+1}/T_n=a_{n+1}$、$T_n/T_{n-1}=a_n$ 得 $a_{n+1}=2a_n$（$n\ge2$）。" "\n"
        r"又 $a_1=1$、$a_2=2$ ⟹ $\dfrac{a_2}{a_1}=2$，同样满足该递推。" "\n"
        r"$\therefore\{a_n\}$ 是首项 $a_1=1$、公比 $q=2$ 的等比数列，$a_n=2^{n-1}$。" "\n"
        r"$\therefore S_{10}=\dfrac{1\cdot(1-2^{10})}{1-2}=2^{10}-1=1024-1=1023$。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书详解：「因为 $T_{n+1}\cdot T_{n-1}=2T_n^2$，故 $\frac{T_{n+1}}{T_n}\cdot\frac{T_n}{T_{n-1}}=2$，即 $\frac{a_{n+1}}{a_n}=2$（$n\ge2$），" "\n"
        r"而 $\frac{a_2}{a_1}=2$，所以 $\{a_n\}$ 为等比数列，故 $a_n=2^{n-1}$，所以 $S_{10}=\frac{1\times(1-2^{10})}{1-2}=1023$，填 $1023$.」" "\n"
        r"—— **$a_{n+1}=2a_n$（$n\ge2$）、$\frac{a_2}{a_1}=2$、等比数列、$a_n=2^{n-1}$、$S_{10}=1023$ 全部一致** ✓✓✓" "\n"
        r"**独立验算（完全独立）**：" "\n"
        r"① **除法的合法性**：$a_1=1$、$a_2=2$ 均非零，且 $a_{n+1}=2a_n$ 保证所有项非零 ⟹ $T_n\ne0$ ✓✓✓" "\n"
        r"② **$T_{n+1}/T_n=a_{n+1}$ 的定义**：$T_{n+1}=T_n\cdot a_{n+1}$ ✓✓✓" "\n"
        r"③ **递推的范围**：题目给的是 $n\ge2$，所以严格说只能推出 $a_{n+1}=2a_n$ 对 $n\ge2$ 成立，" "\n"
        r"即 $a_3=2a_2$、$a_4=2a_3$…… **$a_2=2a_1$ 需单独由 $a_1=1,a_2=2$ 验证** ✓（$2=2\times1$ ✓）✓✓✓" "\n"
        r"（**这正是原书特意写「而 $\frac{a_2}{a_1}=2$」的原因** —— 补上 $n=1$ 的情形）" "\n"
        r"④ **数列**：$1,2,4,8,16,32,64,128,256,512$（前 $10$ 项）。" "\n"
        r"和 $=1+2+4+8+16+32+64+128+256+512=1023$ ✓✓✓" "\n"
        r"（$2^{10}-1=1023$ ✓）" "\n"
        r"⑤ **回代检验原条件**：取 $n=2$：$T_3=a_1a_2a_3=1\cdot2\cdot4=8$、$T_1=1$、$T_2=2$。" "\n"
        r"$T_3\cdot T_1=8$；$2T_2^2=2\cdot4=8$ ✓✓✓ **成立**" "\n"
        r"取 $n=3$：$T_4=1\cdot2\cdot4\cdot8=64$、$T_2=2$、$T_3=8$。" "\n"
        r"$T_4T_2=128$；$2T_3^2=2\cdot64=128$ ✓✓✓ **成立**" "\n"
        r"**答案 $1023$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（前 $n$ 项积 $T_n$）**：" "\n"
        r"① ⭐⭐ **$T_{n+1}T_{n-1}=k\,T_n^2$ ⟹ $\dfrac{a_{n+1}}{a_n}=k$（等比数列）**：" "\n"
        r"**这是「积递推」转「项递推」的标准变形：同除以 $T_nT_{n-1}$**；" "\n"
        r"② ⭐⭐ **$a_n=\dfrac{T_n}{T_{n-1}}$（$n\ge2$），$a_1=T_1$**：" "\n"
        r"**$n=1$ 必须单独处理** —— 这是积数列问题最常见的失分点；" "\n"
        r"③ ⭐⭐ **递推只对 $n\ge2$ 成立时，务必验证 $n=1$**：" "\n"
        r"本题 $a_2=2a_1$ 恰好成立 ⟹ 整体等比。" "\n"
        r"**若不成立则数列要分段写**（从 $a_2$ 起等比）；" "\n"
        r"④ ⭐ **除法前先确认各项非零**：" "\n"
        r"题目隐含 $T_n\ne0$（否则无法相除）。**若某项可能为 $0$，必须单独讨论**；" "\n"
        r"⑤ ⭐ **验证方法：把递推式回代两三个 $n$ 值**：" "\n"
        r"本题 $n=2,3$ 都成立 ✓ —— **比只检查最终答案可靠得多**；" "\n"
        r"⑥ ⚠ **求和别用错项数**：前 $10$ 项 ⟹ $S_{10}=\frac{a_1(1-q^{10})}{1-q}=2^{10}-1$（**指数是 $10$ 不是 $9$**）。"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-254'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-254-E1',
}

T254_V1 = {
    'type': '填空',
    'stem_text': r"若数列 $\{a_n\}$ 的前 $n$ 项的积为 $\dfrac1{n+1}$，则 $a_n=$ ____。",
    'opts': [],
    'answer': r"$a_n=\dfrac n{n+1}$（$n\in\mathbb N^*$）",
    'analysis': (
        r"$T_n=\frac1{n+1}$。$n=1$ 时 $a_1=T_1=\frac12$；$n\ge2$ 时 $a_n=\frac{T_n}{T_{n-1}}=\frac{1/(n+1)}{1/n}=\frac n{n+1}$。"
        r"$n=1$ 代入也成立 ⟹ $a_n=\frac n{n+1}$。"
    ),
    'solution': (
        r"设数列 $\{a_n\}$ 的前 $n$ 项积为 $T_n$，则 $T_n=\dfrac1{n+1}$。" "\n"
        r"当 $n=1$ 时，$a_1=T_1=\dfrac1{1+1}=\dfrac12$。" "\n"
        r"当 $n\ge2$ 时，$a_n=\dfrac{T_n}{T_{n-1}}=\dfrac{\frac1{n+1}}{\frac1n}=\dfrac n{n+1}$。" "\n"
        r"检验 $n=1$：$\dfrac n{n+1}=\dfrac12=a_1$ ✓ 也成立。" "\n"
        r"$\therefore a_n=\dfrac n{n+1}$（$n\in\mathbb N^*$）。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书详解：「设数列 $\{a_n\}$ 的前 $n$ 项积为 $T_n$，则 $T_n=\frac1{n+1}$。当 $n=1$ 时，$a_1=T_1=\frac12$；" "\n"
        r"当 $n\ge2$ 时，$a_n=\frac{T_n}{T_{n-1}}=\frac{\frac1{n+1}}{\frac1n}=\frac n{n+1}$。$a_1=\frac12$ 满足 $a_n=\frac n{n+1}$。综上所述，$a_n=\frac n{n+1}$（$n\in\mathbb N^*$）。故答案为：$\frac n{n+1}$（$n\in\mathbb N^*$）」" "\n"
        r"—— **$T_n=\frac1{n+1}$、$a_1=\frac12$、$\frac{T_n}{T_{n-1}}=\frac n{n+1}$、$n=1$ 也成立、答案 $\frac n{n+1}$ 全部一致** ✓✓✓" "\n"
        r"**独立验算（完全独立）**：" "\n"
        r"① **逐项计算**：$a_1=\frac12$、$a_2=\frac23$、$a_3=\frac34$、$a_4=\frac45$……" "\n"
        r"$T_1=\frac12$ ✓（$=\frac1{1+1}$）；$T_2=\frac12\cdot\frac23=\frac13$ ✓（$=\frac1{2+1}$）；" "\n"
        r"$T_3=\frac13\cdot\frac34=\frac14$ ✓（$=\frac1{3+1}$）；$T_4=\frac14\cdot\frac45=\frac15$ ✓（$=\frac1{4+1}$）✓✓✓" "\n"
        r"**望远镜相消，全部吻合**" "\n"
        r"② **一般证明**：$T_n=\prod_{k=1}^n\frac k{k+1}=\frac12\cdot\frac23\cdot\frac34\cdots\frac n{n+1}=\frac1{n+1}$ ✓✓✓" "\n"
        r"（**中间项全部约掉，只剩首尾** —— 这是典型的裂项相消积）" "\n"
        r"③ **$n=1$ 单独检验**：$\frac{T_1}{T_0}$ 无意义（$T_0$ 未定义），必须用 $a_1=T_1$ ✓✓✓" "\n"
        r"④ **$a_n\in(0,1)$ 的合理性**：$\frac n{n+1}<1$ ✓，且 $a_n\to1$ —— **连乘积 $\to0$**，与 $T_n=\frac1{n+1}\to0$ 一致 ✓✓✓" "\n"
        r"**答案 $a_n=\frac n{n+1}$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（已知 $T_n$ 求 $a_n$）**：" "\n"
        r"① ⭐⭐ **$a_n=\begin{cases}T_1,&n=1\\\dfrac{T_n}{T_{n-1}},&n\ge2\end{cases}$** —— " "\n"
        r"**这是「由积求项」的唯一公式，$n=1$ 必须单独算**；" "\n"
        r"② ⭐⭐ **算完 $n\ge2$ 的式子后，务必代 $n=1$ 检验**：" "\n"
        r"· 若成立 ⟹ 合并成一个式子（如本题）；" "\n"
        r"· 若不成立 ⟹ **必须写成分段形式**（这是高频考点！）；" "\n"
        r"③ ⭐ **望远镜积的识别**：$\frac12\cdot\frac23\cdot\frac34\cdots\frac n{n+1}=\frac1{n+1}$ —— " "\n"
        r"**相邻的分子分母能约掉的连乘积**，$T_n$ 往往形如 $\frac1{n+1}$、$\frac{2}{n(n+1)}$ 等；" "\n"
        r"④ ⭐ **双向检验**：" "\n"
        r"**由 $a_n$ 乘回去看是否等于 $T_n$** —— 本题 $\prod\frac k{k+1}=\frac1{n+1}$ ✓，" "\n"
        r"这是验证「由积求项」最直接的方法；" "\n"
        r"⑤ ⚠ **$T_0$ 没有定义（或约定 $T_0=1$）**：" "\n"
        r"若约定 $T_0=1$，则 $a_n=\frac{T_n}{T_{n-1}}$ 对 $n=1$ 也形式成立 —— " "\n"
        r"**但考试书写仍建议先单独写 $a_1=T_1$，再检验能否合并**。"
    ),
    'difficulty': 0.65,
    'topics': ['M-T-254'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-254-V1',
}

T254_V2 = {
    'type': '选择',
    'stem_text': (
        r"设等比数列 $\{a_n\}$ 的公比为 $q$，其前 $n$ 项和为 $S_n$，前 $n$ 项积为 $T_n$，并满足条件 $a_1>1$，"
        r"且 $a_{2020}a_{2021}>1$，$\left(a_{2020}-1\right)\left(a_{2021}-1\right)<0$，下列结论**不正确**的是（　　）"
    ),
    'opts': [
        ('A', r"$S_{2020}<S_{2021}$"),
        ('B', r"$a_{2020}a_{2022}-1<0$"),
        ('C', r"数列 $\{T_n\}$ 无最大值"),
        ('D', r"$T_{2020}$ 是数列 $\{T_n\}$ 中的最大值"),
    ],
    'answer': 'C',
    'analysis': (
        r"由条件得 $a_{2020}>1>a_{2021}>0$ ⟹ $0<q<1$。"
        r"A：$S_{2021}-S_{2020}=a_{2021}>0$ ✓；B：$a_{2020}a_{2022}=a_{2021}^2<1$ ✓；"
        r"C/D：$T_n$ 在 $n\le2020$ 递增、$n\ge2020$ 递减 ⟹ $T_{2020}$ 最大，故 C 错、D 对。"
    ),
    'solution': (
        r"由 $a_{2020}a_{2021}>1$ 且 $a_1>1$：" "\n"
        r"$a_{2020}a_{2021}=a_1q^{2019}\cdot a_1q^{2020}=a_1^2q^{4039}>1$。" "\n"
        r"因 $a_1>1$，必有 $q>0$，故**数列各项均为正**。" "\n"
        r"由 $\left(a_{2020}-1\right)\left(a_{2021}-1\right)<0$：两因子异号。" "\n"
        r"若 $a_{2020}<1<a_{2021}$，则 $q>1$，与 $a_1>1$ 一起会推出 $a_{2020}>1$（各项递增且 $a_1>1$），矛盾。" "\n"
        r"$\therefore a_{2020}>1$ 且 $0<a_{2021}<1$，从而 $0<q<1$（各项递减）。" "\n"
        r"**逐项判断：**" "\n"
        r"A：$S_{2021}-S_{2020}=a_{2021}>0$ ⟹ $S_{2020}<S_{2021}$，**A 正确**。" "\n"
        r"B：由等比中项 $a_{2020}a_{2022}=a_{2021}^2$，而 $0<a_{2021}<1$ ⟹ $a_{2021}^2-1<0$，**B 正确**。" "\n"
        r"C、D：各项满足 $a_1>a_2>\cdots>a_{2020}>1>a_{2021}>\cdots>0$。" "\n"
        r"当 $n\le2020$ 时 $a_n>1$ ⟹ $T_n=T_{n-1}\cdot a_n>T_{n-1}$（递增）；" "\n"
        r"当 $n\ge2021$ 时 $0<a_n<1$ ⟹ $T_n<T_{n-1}$（递减）。" "\n"
        r"$\therefore T_{2020}$ 是 $\{T_n\}$ 的最大项，**D 正确、C 错误**。" "\n"
        r"故选 C。"
    ),
    'review': (
        r"★ 题干、选项、答案、详解完整 ✓。原书详解：「根据题意，等比数列 $\{a_n\}$ 的公比为 $q$，若 $a_{2020}a_{2021}>1$，则 $a_1q^{2019}\cdot a_1q^{2020}=a_1^2q^{4039}>1$，又由 $a_1>1$，必有 $q>0$，则数列 $\{a_n\}$ 各项均为正值。" "\n"
        r"若 $\left(a_{2020}-1\right)\left(a_{2021}-1\right)<0$，必有 $a_{2020}>1$，$0<a_{2021}<1$，则必有 $0<q<1$，依次分析选项：" "\n"
        r"对于 A，数列 $\{a_n\}$ 各项均为正值，则 $S_{2021}-S_{2020}=a_{2021}>0$，必有 $S_{2020}<S_{2021}$，A 正确；" "\n"
        r"对于 B，若 $0<a_{2021}<1$，则 $a_{2020}a_{2022}-1=a_{2021}^2-1<0$，B 正确；" "\n"
        r"对于 C，根据 $a_1>a_2>\cdots>a_{2020}>1>a_{2021}>\cdots>0$，可知 $T_{2020}$ 是数列 $\{T_n\}$ 中的最大项，C 错误；" "\n"
        r"对于 D，易得 D 正确，故选：C.」" "\n"
        r"—— **$q>0$、各项为正、$a_{2020}>1>a_{2021}>0$、$0<q<1$、A/B/D 正确、C 错误、答案 C 全部一致** ✓✓✓" "\n"
        r"**独立验算（构造具体数列，完全独立）**：" "\n"
        r"① **构造**：取 $a_1=2$、$q$ 使得 $a_{2020}>1>a_{2021}$。" "\n"
        r"$a_{2020}=2q^{2019}>1$、$a_{2021}=2q^{2020}<1$ ⟹ $\frac12<q^{2019}$ 且 $q^{2020}<\frac12$。" "\n"
        r"取 $\ln q=-\frac{0.68}{2019}$ ⟹ $q^{2019}=e^{-0.68}=0.5066$ ✓（$>\frac12$）" "\n"
        r"$q^{2020}=q^{2019}\cdot q\approx0.5066\times0.99982=0.5065$ ✓（$<\frac12$？$0.5065>0.5$ ✗）" "\n"
        r"再调：$\ln q=-\frac{0.694}{2019}$ ⟹ $q^{2019}=e^{-0.694}=0.49959<0.5$ ✗。" "\n"
        r"取 $\ln q=-\frac{0.6925}{2019}$：$q^{2019}=e^{-0.6925}=0.50034>0.5$ ✓；" "\n"
        r"$q^{2020}=0.50034\times e^{-0.000343}=0.50034\times0.999657=0.50017>0.5$ ✗。" "\n"
        r"**改用小规模模拟**：取等价的「$N=3$」版本验证逻辑（$a_1=2$，$a_3>1>a_4$）：" "\n"
        r"取 $q=0.8$：$a_1=2$、$a_2=1.6$、$a_3=1.28>1$、$a_4=1.024>1$、$a_5=0.819<1$。" "\n"
        r"此时「分界」在 $a_4>1>a_5$，$T_4$ 应为最大。" "\n"
        r"$T_1=2$、$T_2=3.2$、$T_3=4.096$、$T_4=4.194304$、$T_5=3.435$、$T_6=2.199$。" "\n"
        r"**$T_4$ 确为最大** ✓✓✓；且 $T_5<T_4$、$T_6<T_5$ ✓✓✓" "\n"
        r"验证 A：$S_5-S_4=a_5=0.819>0$ ⟹ $S_4<S_5$ ✓✓✓" "\n"
        r"验证 B：$a_4a_6=1.024\times0.65536=0.671$；$a_5^2=0.671$ ✓ **相等**（等比中项性质）⟹ $a_4a_6-1<0$ ✓✓✓" "\n"
        r"验证 C：$\{T_n\}$ 有最大值（$T_4$）⟹ **「无最大值」错误** ✓✓✓" "\n"
        r"② **为什么必须有 $q>0$**：若 $q<0$，则 $a_{2020}$ 与 $a_{2021}$ 异号，其乘积 $<0$，与 $a_{2020}a_{2021}>1$ 矛盾 ✓✓✓" "\n"
        r"③ **为什么是 $a_{2020}>1>a_{2021}$ 而不是反过来**：" "\n"
        r"若 $a_{2020}<1<a_{2021}$，则 $q=\frac{a_{2021}}{a_{2020}}>1$，各项递增，$a_{2020}>a_1>1$，与 $a_{2020}<1$ 矛盾 ✓✓✓" "\n"
        r"④ **$T_n$ 单调性的判定**：$T_n=T_{n-1}a_n$ ⟹ " "\n"
        r"$a_n>1$ 时 $T_n$ 递增、$0<a_n<1$ 时 $T_n$ 递减 —— **分界点就是最后一个 $>1$ 的项** ✓✓✓" "\n"
        r"**答案 C 正确** ✓" "\n"
        r"**⭐⭐ 通法（等比数列前 $n$ 项积的最值）**：" "\n"
        r"① ⭐⭐ **核心判据：$T_n=T_{n-1}\cdot a_n$**：" "\n"
        r"**$T_n$ 的单调性完全由 $a_n$ 与 $1$ 的大小决定** —— $a_n>1$ 递增、$0<a_n<1$ 递减；" "\n"
        r"② ⭐⭐ **$\{T_n\}$ 的最大项 = 最后一个「$a_n>1$」的项对应的 $T_n$**：" "\n"
        r"**分界点：$a_k>1\ge a_{k+1}$ ⟹ $T_k$ 最大**（本题 $k=2020$）；" "\n"
        r"③ ⭐⭐ **等比中项：$a_{m}a_{n}=a_pa_q$（$m+n=p+q$）**：" "\n"
        r"本题 $a_{2020}a_{2022}=a_{2021}^2$（$2020+2022=2021+2021$）—— **一步把两项乘积变成平方**；" "\n"
        r"④ ⭐ **由 $(a_m-1)(a_{m+1}-1)<0$ 定分界**：" "\n"
        r"**这个条件就是说「$a_m$ 与 $a_{m+1}$ 分居 $1$ 的两侧」**，是求 $T_n$ 最值的标准给法；" "\n"
        r"⑤ ⚠ **先定 $q$ 的符号**：" "\n"
        r"由 $a_ma_{m+1}>1>0$ ⟹ $q>0$ ⟹ **各项同号（此处为正）** —— " "\n"
        r"**若各项可能为负，$T_n$ 的单调性判据会完全不同**（要讨论正负）；" "\n"
        r"⑥ ⚠ **「不正确的是」别看成「正确的是」**：" "\n"
        r"本题问**不正确**的，选 C。**看到「不正确 / 错误的是」要圈出来**；" "\n"
        r"⑦ ⭐ **大下标（$2020$）的题：换成小下标（$3,4$）构造具体数列验证逻辑** —— " "\n"
        r"本题我用 $N=3$/$4$ 的版本完整跑了一遍，四个选项全部对上 ✓✓✓"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-254'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-254-V2',
}

T254_V3 = {
    'type': '填空',
    'stem_text': (
        r"已知各项均不为零的数列 $\{a_n\}$ 的前 $n$ 项积 $T_n$ 满足 $T_{n+1}+a_na_{n+1}=a_{n+1}$，"
        r"则 $T_n=$ ____；数列 $\left\{\dfrac{a_n}{T_n}\right\}$ 的前 $n$ 项和 $S_n=$ ____。"
    ),
    'opts': [],
    'answer': r"$T_n=\dfrac1{n+1}$；$S_n=\dfrac{n(n+1)}2$",
    'analysis': (
        r"由 $T_{n+1}=T_na_{n+1}$ 代入并除以 $a_{n+1}\ne0$ 得 $T_n+a_n=1$。$n=1$ 时 $2a_1=1$ ⟹ $a_1=T_1=\frac12$；"
        r"$n\ge2$ 时 $a_n=\frac{T_n}{T_{n-1}}$ ⟹ $T_n+\frac{T_n}{T_{n-1}}=1$ ⟹ $\frac1{T_n}-\frac1{T_{n-1}}=1$ ⟹ $T_n=\frac1{n+1}$、$\frac{a_n}{T_n}=n$ ⟹ $S_n=\frac{n(n+1)}2$。"
    ),
    'solution': (
        r"由 $T_{n+1}+a_na_{n+1}=a_{n+1}$，而 $T_{n+1}=T_n\cdot a_{n+1}$，代入：" "\n"
        r"$T_na_{n+1}+a_na_{n+1}=a_{n+1}$。" "\n"
        r"$\because a_{n+1}\ne0$，两边同除以 $a_{n+1}$ 得 $T_n+a_n=1$　(1)" "\n"
        r"**求首项：** $n=1$ 时 $T_1=a_1$，由 (1) 得 $a_1+a_1=1$ ⟹ $a_1=\dfrac12$，故 $T_1=\dfrac12$，$\dfrac1{T_1}=2$。" "\n"
        r"**求递推：** 当 $n\ge2$ 时 $a_n=\dfrac{T_n}{T_{n-1}}$，代入 (1)：" "\n"
        r"$T_n+\dfrac{T_n}{T_{n-1}}=1$，两边同除以 $T_n$：$1+\dfrac1{T_{n-1}}=\dfrac1{T_n}$，即 $\dfrac1{T_n}-\dfrac1{T_{n-1}}=1$。" "\n"
        r"$\therefore\left\{\dfrac1{T_n}\right\}$ 是首项 $2$、公差 $1$ 的等差数列 ⟹ $\dfrac1{T_n}=2+(n-1)=n+1$ ⟹ $T_n=\dfrac1{n+1}$。" "\n"
        r"$n=1$ 时 $\frac1{1+1}=\frac12=T_1$ ✓ 也成立。" "\n"
        r"由 (1)：$a_n=1-T_n=1-\dfrac1{n+1}=\dfrac n{n+1}$。" "\n"
        r"$\therefore\dfrac{a_n}{T_n}=\dfrac{n/(n+1)}{1/(n+1)}=n$。" "\n"
        r"$\therefore S_n=1+2+\cdots+n=\dfrac{n(n+1)}2$。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书详解：「由 $T_{n+1}+a_na_{n+1}=a_{n+1}$，得 $T_na_{n+1}+a_na_{n+1}=a_{n+1}$。因为 $a_{n+1}\ne0$，所以 $T_n+a_n=1$。" "\n"
        r"由题意知，当 $n\ge2$ 时，$a_n=\frac{T_n}{T_{n-1}}$，所以当 $n\ge2$ 时，$T_n+\frac{T_n}{T_{n-1}}=1$，两边同时除以 $T_n$，得 $\frac1{T_n}-\frac1{T_{n-1}}=1$。" "\n"
        r"因为 $T_1=1-a_1=a_1$，所以 $a_1=\frac12$，$\frac1{T_1}=\frac1{a_1}=2$，所以数列 $\left\{\frac1{T_n}\right\}$ 是首项为 $2$、公差为 $1$ 的等差数列，" "\n"
        r"所以 $\frac1{T_n}=n+1$，$T_n=\frac1{n+1}$，从而 $a_n=1-T_n=1-\frac1{n+1}=\frac n{n+1}$，故 $\frac{a_n}{T_n}=n$，所以数列 $\left\{\frac{a_n}{T_n}\right\}$ 的前 $n$ 项和为 $S_n=\frac{n(n+1)}2$。" "\n"
        r"故答案为：$\frac1{n+1}$；$\frac{n(n+1)}2$」" "\n"
        r"—— **$T_n+a_n=1$、$a_1=\frac12$、$\frac1{T_n}-\frac1{T_{n-1}}=1$、$T_n=\frac1{n+1}$、$a_n=\frac n{n+1}$、$\frac{a_n}{T_n}=n$、$S_n=\frac{n(n+1)}2$ 全部一致** ✓✓✓" "\n"
        r"**独立验算（完全独立，逐项验证）**：" "\n"
        r"① **关键变形**：$T_{n+1}=T_n\cdot a_{n+1}$ ✓；代入得 $a_{n+1}(T_n+a_n)=a_{n+1}$ ⟹ 除以 $a_{n+1}\ne0$ 得 $T_n+a_n=1$ ✓✓✓" "\n"
        r"② **首项**：$T_1=a_1$ ⟹ $a_1+a_1=1$ ⟹ $a_1=\frac12$ ✓✓✓" "\n"
        r"③ **递推**：$T_n+\frac{T_n}{T_{n-1}}=1$ ⟹ 除以 $T_n$：$1+\frac1{T_{n-1}}=\frac1{T_n}$ ⟹ $\frac1{T_n}-\frac1{T_{n-1}}=1$ ✓✓✓" "\n"
        r"④ **$T_n$**：$\frac1{T_n}=2+(n-1)\cdot1=n+1$ ⟹ $T_n=\frac1{n+1}$ ✓✓✓" "\n"
        r"⑤ **逐项验证原条件**：" "\n"
        r"$a_1=\frac12$、$a_2=\frac23$、$a_3=\frac34$、$a_4=\frac45$。" "\n"
        r"$T_1=\frac12$、$T_2=\frac13$、$T_3=\frac14$、$T_4=\frac15$。" "\n"
        r"· $n=1$：$T_2+a_1a_2=\frac13+\frac12\cdot\frac23=\frac13+\frac13=\frac23=a_2$ ✓✓✓" "\n"
        r"· $n=2$：$T_3+a_2a_3=\frac14+\frac23\cdot\frac34=\frac14+\frac12=\frac34=a_3$ ✓✓✓" "\n"
        r"· $n=3$：$T_4+a_3a_4=\frac15+\frac34\cdot\frac45=\frac15+\frac35=\frac45=a_4$ ✓✓✓" "\n"
        r"**原条件对多个 $n$ 都成立** ✓✓✓" "\n"
        r"⑥ **$T_n+a_n=1$ 的验证**：$\frac12+\frac12=1$ ✓；$\frac13+\frac23=1$ ✓；$\frac14+\frac34=1$ ✓ ✓✓✓" "\n"
        r"⑦ **$\frac{a_n}{T_n}$**：$\frac{1/2}{1/2}=1$、$\frac{2/3}{1/3}=2$、$\frac{3/4}{1/4}=3$、$\frac{4/5}{1/5}=4$ ⟹ $\frac{a_n}{T_n}=n$ ✓✓✓" "\n"
        r"$S_4=1+2+3+4=10=\frac{4\cdot5}2$ ✓✓✓" "\n"
        r"**答案 $T_n=\frac1{n+1}$、$S_n=\frac{n(n+1)}2$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（$T_n$ 与 $a_n$ 混合的递推）**：" "\n"
        r"① ⭐⭐ **第一步永远是把 $T_{n+1}$ 拆成 $T_n\cdot a_{n+1}$**：" "\n"
        r"**这样整式就出现公因子 $a_{n+1}$**，约去后递推直接降一阶 —— 这是本题的破题眼；" "\n"
        r"② ⭐⭐ **得到 $T_n+a_n=1$ 这类「积与项」的关系后，统一成 $T_n$**：" "\n"
        r"用 $a_n=\frac{T_n}{T_{n-1}}$（$n\ge2$）代入，**式子就只含 $T_n$ 了**；" "\n"
        r"③ ⭐⭐ **两边同除以 $T_n$ 是「取倒数」的信号**：" "\n"
        r"$T_n+\frac{T_n}{T_{n-1}}=1$ ⟹ $\frac1{T_n}-\frac1{T_{n-1}}=1$ —— " "\n"
        r"**见到 $T_n$ 与 $\frac{T_n}{T_{n-1}}$ 相加，就同除以 $T_n$ 凑等差数列**；" "\n"
        r"④ ⭐ **$n=1$ 用 $T_1=a_1$ 单独求**：" "\n"
        r"本题 $T_1+a_1=1$ 且 $T_1=a_1$ ⟹ $a_1=\frac12$ —— **这个「自洽方程」很巧妙**；" "\n"
        r"⑤ ⭐ **$\frac{a_n}{T_n}=n$ 的化简**：" "\n"
        r"$\frac{n/(n+1)}{1/(n+1)}=n$ —— **分子分母的 $(n+1)$ 恰好约掉**，求和变成等差数列求和（**这个设计是刻意的**）；" "\n"
        r"⑥ ⭐ **最强验证：把求出的 $a_n$、$T_n$ 代回原递推，验 $2\sim3$ 个 $n$**：" "\n"
        r"本题 $n=1,2,3$ 全部成立 ✓✓✓；" "\n"
        r"⑦ ⚠ **别忘了「各项均不为零」这个前提**：" "\n"
        r"**它保证了可以除以 $a_{n+1}$ 和 $T_n$** —— 若某项为零，整个推导失效。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-254'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-254-V3',
}

QS = [T291_E1, T291_V1, T291_V2, T291_V3,
      T290_E1, T290_V1,
      T185_E1, T185_V2, T185_V3,
      T254_E1, T254_V1, T254_V2, T254_V3]
