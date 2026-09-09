# -*- coding: utf-8 -*-
r"""第43批（上）：轨迹方程（直接法）

来源：2024高中数学热点题型归纳完整解析版.pdf
p310（PDF 页 309）M-T-336 直接法求轨迹

## 选题

`pick_batch.py --n 16` → p310 / p308 / p304 / p339。本文件取 p310 的 M-T-336（3 题）。

## ★ 本批最大的还原：M-T-336-V2 的向量式被提取错了

题干提取为 $\vec{QP}\cdot\vec{QF}=\vec{FP}\cdot\vec{PQ}$，按字面展开：

$$\vec{QP}\cdot\vec{QF}=2(y+1),\quad\vec{FP}\cdot\vec{PQ}=1-y^{2}$$
$$\Rightarrow2y+2=1-y^{2}\Rightarrow(y+1)^{2}=0$$

**退化为一条直线**（$y=-1$），而答案是抛物线 $x^{2}=4y$ —— 说明提取有误。

还原版给出的中间式是「$2(y+1)=x^{2}-2(y-1)$」，右边正是

$$\vec{FP}\cdot\vec{FQ}=x\cdot x+(y-1)(-2)=x^{2}-2(y-1)$$

所以原书是 **$\vec{FP}\cdot\vec{FQ}$**（不是 $\vec{FP}\cdot\vec{PQ}$）。代入即得 $x^{2}=4y$ ✓

## 三题验算

| 题 | 计算 | 答案 |
|---|---|---|
| E1 | $\frac{y}{x+\sqrt3}\cdot\frac{y}{x-\sqrt3}=\frac13\Rightarrow\frac{x^{2}}3-y^{2}=1$ | **C** |
| V1 | 阿波罗尼斯圆：$(x-\frac52)^{2}+y^{2}=4$，$r=2$，$S=4\pi$ | **D** |
| V2 | $2(y+1)=x^{2}-2(y-1)\Rightarrow x^{2}=4y$ | **A** |

## E1 的一个易错点

$k_{AM}\cdot k_{BM}=\frac{y^{2}}{x^{2}-3}=\frac13>0$，故 $x^{2}-3>0$，
轨迹是双曲线的**两支**（不是椭圆）。且 $y\neq0$（否则斜率为 $0$，积为 $0\neq\frac13$），
所以是 $\frac{x^{2}}3-y^{2}=1\ (y\neq0)$ —— 顶点要挖掉。
"""

T336_E1 = {
    'type': '选择',
    'stem_text': (
        r"设点 $A(-\sqrt3,0)$、$B(\sqrt3,0)$，$M$ 为动点，"
        r"已知直线 $AM$ 与直线 $BM$ 的斜率之积为定值 $\dfrac13$，"
        r"则点 $M$ 的轨迹是（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac{x^{2}}9-y^{2}=1\ (y\neq0)$"),
        ('B', r"$\dfrac{y^{2}}9-x^{2}=1\ (y\neq0)$"),
        ('C', r"$\dfrac{x^{2}}3-y^{2}=1\ (y\neq0)$"),
        ('D', r"$\dfrac{y^{2}}3-x^{2}=1\ (y\neq0)$"),
    ],
    'answer': 'C',
    'analysis': (
        r"直接法：设 $M(x,y)$，写出两个斜率、相乘、化简。"
        r"注意 $x\neq\pm\sqrt3$（斜率存在）与 $y\neq0$（积非零）两个限制。"
    ),
    'solution': (
        r"设 $M(x,y)$．因直线 $AM$、$BM$ 的斜率都存在，故 $x\neq\pm\sqrt3$．" "\n"
        r"$k_{AM}=\dfrac{y-0}{x-(-\sqrt3)}=\dfrac{y}{x+\sqrt3}$，"
        r"$k_{BM}=\dfrac{y-0}{x-\sqrt3}=\dfrac{y}{x-\sqrt3}$．" "\n"
        r"由已知 $k_{AM}\cdot k_{BM}=\dfrac13$：" "\n"
        r"$\dfrac{y}{x+\sqrt3}\cdot\dfrac{y}{x-\sqrt3}=\dfrac13"
        r"\Rightarrow\dfrac{y^{2}}{x^{2}-3}=\dfrac13$" "\n"
        r"$\Rightarrow x^{2}-3=3y^{2}\Rightarrow x^{2}-3y^{2}=3"
        r"\Rightarrow\dfrac{x^{2}}3-y^{2}=1$．" "\n"
        r"又若 $y=0$，则两斜率之积为 $0\neq\dfrac13$，故 $y\neq0$（轨迹要挖掉两个顶点）．" "\n"
        r"所以点 $M$ 的轨迹是 $\dfrac{x^{2}}3-y^{2}=1\ (y\neq0)$．选 C．"
    ),
    'review': (
        r"★ 题干、选项、答案、详解**全部完整** ✓。由详解「设动点 $M(x,y)$，则 $x\neq\pm\sqrt3$，"
        r"$k_{MA}=\frac{y}{x+\sqrt3}$，$k_{MB}=\frac{y}{x-\sqrt3}$（$x\neq\pm\sqrt3$），"
        r"∵ 直线 $AM$ 与 $BM$ 的斜率之积为定值 $\frac13$，∴ $\frac{y}{x+\sqrt3}\cdot\frac{y}{x-\sqrt3}=\frac13$，"
        r"化简可得 $\frac{x^{2}}3-y^{2}=1\ (y\neq0)$」还原，与我的推导**逐字一致** ✓。" "\n"
        r"**独立验算**：" "\n"
        r"① 取轨迹上一点：$y=1$ → $\frac{x^{2}}3=2$ → $x=\pm\sqrt6\approx\pm2.449$" "\n"
        r"验 $\frac{(\pm\sqrt6)^{2}}3-1^{2}=2-1=1$ ✓ 在双曲线上" "\n"
        r"② 验斜率之积（取 $x=\sqrt6,y=1$）：" "\n"
        r"$k_{AM}=\frac{1}{\sqrt6+\sqrt3}=\frac{1}{2.449+1.732}=\frac1{4.181}=0.2392$" "\n"
        r"$k_{BM}=\frac{1}{\sqrt6-\sqrt3}=\frac{1}{2.449-1.732}=\frac1{0.717}=1.3944$" "\n"
        r"积 $=0.2392\times1.3944=0.3335\approx\frac13$ ✓✓" "\n"
        r"③ **再取一点复核**（$y=2$ → $\frac{x^{2}}3=5$ → $x=\sqrt{15}\approx3.873$）：" "\n"
        r"$k_{AM}=\frac2{3.873+1.732}=\frac2{5.605}=0.3568$；$k_{BM}=\frac2{3.873-1.732}=\frac2{2.141}=0.9341$" "\n"
        r"积 $=0.3568\times0.9341=0.3333=\frac13$ ✓✓" "\n"
        r"④ **判别形状**：积 $=\frac13>0$ 而 $x^{2}-3$ 与 $y^{2}$ 同号 → $x^{2}>3$，"
        r"故是**双曲线**（不是椭圆）✓；且 $y\neq0$ → 挖掉 $(\pm\sqrt3,0)$ ✓" "\n"
        r"**答案 C 正确** ✓" "\n"
        r"**⭐ 通法（直接法求轨迹）**：「两定点连线斜率之积为定值 $\lambda$」是经典模型 ——" "\n"
        r"设两定点 $(\pm c,0)$，则 $\frac{y^{2}}{x^{2}-c^{2}}=\lambda$，即 $\frac{x^{2}}{c^{2}}-\frac{y^{2}}{c^{2}/\lambda}\cdot\frac{1}{1}\cdot\lambda$…"
        r"统一写成 $\dfrac{x^{2}}{c^{2}}-\dfrac{y^{2}}{c^{2}/\lambda}=\dfrac{1}{\lambda}\cdot\lambda$ 更清楚的做法是直接记结论：" "\n"
        r"· $\lambda>0$ → **双曲线**（本题 $\lambda=\frac13$，得 $\frac{x^{2}}3-y^{2}=1$）" "\n"
        r"· $\lambda<0$ → **椭圆**（挖掉两定点）" "\n"
        r"· $\lambda=-1$ → **圆**（$A,B$ 为直径端点，即「张直角」）" "\n"
        r"**两种情形都要挖掉使斜率为 $0$ 或不存在**的点。"
    ),
    'difficulty': 0.83,
    'topics': ['M-T-336'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-336-E1',
}

T336_V1 = {
    'type': '选择',
    'stem_text': (
        r"若两定点 $A,B$ 的距离为 $3$，动点 $M$ 满足 $\lvert MA\rvert=2\lvert MB\rvert$，"
        r"则 $M$ 点的轨迹围成区域的面积为（　　）"
    ),
    'opts': [
        ('A', r"$\pi$"),
        ('B', r"$2\pi$"),
        ('C', r"$3\pi$"),
        ('D', r"$4\pi$"),
    ],
    'answer': 'D',
    'analysis': (
        r"「到两定点距离之比为常数 $\lambda\neq1$」的轨迹是**阿波罗尼斯圆**。"
        r"建系设 $A(-\frac32,0)$、$B(\frac32,0)$，列距离等式后配方即得圆心与半径。"
    ),
    'solution': (
        r"以 $AB$ 中点 $O$ 为原点、$AB$ 所在直线为 $x$ 轴建系，" "\n"
        r"则 $A\left(-\dfrac32,0\right)$、$B\left(\dfrac32,0\right)$，$M(x,y)$．" "\n"
        r"由 $\lvert MA\rvert=2\lvert MB\rvert$：" "\n"
        r"$\sqrt{\left(x+\dfrac32\right)^{2}+y^{2}}=2\sqrt{\left(x-\dfrac32\right)^{2}+y^{2}}$" "\n"
        r"两边平方：$\left(x+\dfrac32\right)^{2}+y^{2}=4\left[\left(x-\dfrac32\right)^{2}+y^{2}\right]$" "\n"
        r"$x^{2}+3x+\dfrac94+y^{2}=4\left(x^{2}-3x+\dfrac94+y^{2}\right)=4x^{2}-12x+9+4y^{2}$" "\n"
        r"$\Rightarrow3x^{2}-15x+3y^{2}+\dfrac{27}4=0$" "\n"
        r"$\Rightarrow x^{2}-5x+y^{2}+\dfrac94=0$" "\n"
        r"$\Rightarrow\left(x-\dfrac52\right)^{2}+y^{2}=\dfrac{25}4-\dfrac94=4$．" "\n"
        r"故轨迹是以 $\left(\dfrac52,0\right)$ 为圆心、$r=2$ 的圆，" "\n"
        r"围成区域面积 $S=\pi r^{2}=4\pi$．选 D．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**详解未提取到**，上述推导为我独立完成）。" "\n"
        r"**独立验算**：" "\n"
        r"① 圆心 $C(\frac52,0)$、半径 $r=2$" "\n"
        r"② 取圆上一点 $M(\frac52+2,0)=(\frac92,0)$：" "\n"
        r"$\lvert MA\rvert=\frac92-(-\frac32)=\frac92+\frac32=6$；$\lvert MB\rvert=\frac92-\frac32=3$；$6=2\times3$ ✓✓" "\n"
        r"③ 取圆上另一点 $M(\frac52-2,0)=(\frac12,0)$：" "\n"
        r"$\lvert MA\rvert=\frac12+\frac32=2$；$\lvert MB\rvert=\lvert\frac12-\frac32\rvert=1$；$2=2\times1$ ✓✓" "\n"
        r"④ 取**非直径方向**的点验证：$M(\frac52,2)$（正上方，$y=2$）" "\n"
        r"$\lvert MA\rvert=\sqrt{(\frac52+\frac32)^{2}+4}=\sqrt{16+4}=\sqrt{20}\approx4.4721$" "\n"
        r"$\lvert MB\rvert=\sqrt{(\frac52-\frac32)^{2}+4}=\sqrt{1+4}=\sqrt5\approx2.2361$" "\n"
        r"比值 $=\frac{4.4721}{2.2361}=2.000$ ✓✓ **确为 2**" "\n"
        r"⑤ 面积 $=\pi\cdot2^{2}=4\pi$ ✓✓" "\n"
        r"**答案 D（$4\pi$）正确** ✓" "\n"
        r"**⭐ 通法（阿波罗尼斯圆）**：$\lvert MA\rvert=\lambda\lvert MB\rvert$（$\lambda>0,\lambda\neq1$）"
        r"的轨迹是圆。设 $\lvert AB\rvert=d$，建系后配方得" "\n"
        r"圆心在 $AB$ 延长线上，距 $B$ 为 $\dfrac{\lambda^{2}d}{\lvert\lambda^{2}-1\rvert}$ 的位置；"
        r"半径 $r=\dfrac{\lambda d}{\lvert\lambda^{2}-1\rvert}$。" "\n"
        r"本题 $d=3$、$\lambda=2$：$r=\frac{2\times3}{4-1}=\frac63=2$ ✓ **与配方结果一致**。" "\n"
        r"（$\lambda=1$ 时退化为**中垂线**，不是圆 —— 这是唯一的例外。）"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-336'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-336-V1',
}

T336_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知点 $F(0,1)$，直线 $l:y=-1$，$P$ 为平面上的动点，过点 $P$ 作直线 $l$ 的垂线，"
        r"垂足为 $Q$，且 $\vec{QP}\cdot\vec{QF}=\vec{FP}\cdot\vec{FQ}$，"
        r"则动点 $P$ 的轨迹 $C$ 的方程为（　　）"
    ),
    'opts': [
        ('A', r"$x^{2}=4y$"),
        ('B', r"$y^{2}=3x$"),
        ('C', r"$x^{2}=2y$"),
        ('D', r"$y^{2}=4x$"),
    ],
    'answer': 'A',
    'analysis': (
        r"分别算两个数量积：$\vec{QP}\cdot\vec{QF}=2(y+1)$，"
        r"$\vec{FP}\cdot\vec{FQ}=x^{2}-2(y-1)$，令其相等即得抛物线。"
    ),
    'solution': (
        r"设 $P(x,y)$．因 $l:y=-1$ 是水平线，$PQ\perp l$，故 $Q(x,-1)$（与 $P$ 同横坐标）．" "\n"
        r"又 $F(0,1)$，于是" "\n"
        r"$\vec{QP}=P-Q=(0,\,y+1)$，$\vec{QF}=F-Q=(-x,\,2)$；" "\n"
        r"$\vec{FP}=P-F=(x,\,y-1)$，$\vec{FQ}=Q-F=(x,\,-2)$．" "\n"
        r"**算两个数量积**：" "\n"
        r"$\vec{QP}\cdot\vec{QF}=0\cdot(-x)+(y+1)\cdot2=2(y+1)$；" "\n"
        r"$\vec{FP}\cdot\vec{FQ}=x\cdot x+(y-1)\cdot(-2)=x^{2}-2(y-1)$．" "\n"
        r"**令其相等**：" "\n"
        r"$2(y+1)=x^{2}-2(y-1)\Rightarrow2y+2=x^{2}-2y+2\Rightarrow x^{2}=4y$．" "\n"
        r"故轨迹 $C$ 的方程为 $x^{2}=4y$．选 A．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓。由还原版中间式「即 $2(y+1)=x^{2}-2(y-1)$，"
        r"整理得 $x^{2}=4y$，所以动点 $P$ 的轨迹 $C$ 的方程…」与答案 A 印证。" "\n"
        r"**⚠⚠ 关键的还原：题干第二个向量式被提取错了**" "\n"
        r"提取文本为「$\vec{QP}\cdot\vec{QF}=\vec{FP}\cdot\vec{PQ}$」。按字面展开：" "\n"
        r"$\vec{FP}\cdot\vec{PQ}=(x,y-1)\cdot(0,-1-y)=(y-1)(-1-y)=1-y^{2}$，" "\n"
        r"于是 $2y+2=1-y^{2}\Rightarrow(y+1)^{2}=0$ —— **退化为直线 $y=-1$**，不是曲线，"
        r"与四个选项（均为抛物线）**完全矛盾**。" "\n"
        r"还原版给出的右边是 $x^{2}-2(y-1)$，而这恰是 $\vec{FP}\cdot\vec{FQ}$：" "\n"
        r"$\vec{FP}\cdot\vec{FQ}=(x,y-1)\cdot(x,-2)=x^{2}-2(y-1)$ ✓✓" "\n"
        r"故原书为 **$\vec{FP}\cdot\vec{FQ}$**，录入时已改正，并在本 review 中留痕。" "\n"
        r"（这属于 **B 类**：提取失真，还原后与原书一致，非原书印错。）" "\n"
        r"**独立验算**：" "\n"
        r"① **代数验证**：$2y+2=x^{2}-2y+2\Rightarrow4y=x^{2}$ → $x^{2}=4y$ ✓" "\n"
        r"② **取抛物线上一点验证原条件**：$y=1$ → $x=\pm2$。取 $P(2,1)$、$Q(2,-1)$、$F(0,1)$" "\n"
        r"$\vec{QP}=(0,2)$、$\vec{QF}=(-2,2)$ → 点积 $=0+4=4$" "\n"
        r"$\vec{FP}=(2,0)$、$\vec{FQ}=(2,-2)$ → 点积 $=4+0=4$ ✓✓ **相等**" "\n"
        r"③ 验 $P$ 在抛物线上：$2^{2}=4\times1$ ✓" "\n"
        r"④ **取不在抛物线上的点反证**：$P(2,2)$" "\n"
        r"$\vec{QP}=(0,3)$、$\vec{QF}=(-2,2)$ → 点积 $=6$" "\n"
        r"$\vec{FP}=(2,1)$、$\vec{FQ}=(2,-2)$ → 点积 $=4-2=2$；$6\neq2$ ✓✓ **确不满足**" "\n"
        r"⑤ **几何意义**：$F(0,1)$ 正是抛物线 $x^{2}=4y$ 的**焦点**，$l:y=-1$ 是其**准线**，"
        r"而 $\lvert PQ\rvert$ 就是 $P$ 到准线的距离，$\lvert PF\rvert$ 是到焦点的距离。" "\n"
        r"可以验证该向量条件等价于 $\lvert PF\rvert=\lvert PQ\rvert$ —— "
        r"即**抛物线的定义**，这解释了为什么答案恰好是 $x^{2}=4y$ ✓" "\n"
        r"**答案 A（$x^{2}=4y$）正确** ✓" "\n"
        r"**⭐ 通法**：这类「向量数量积等式」的轨迹题，识别不了就直接**坐标化硬算** —— "
        r"四个向量逐一代入，永远算得出来。" "\n"
        r"更进一步的洞察：若题目给了「一点 $F$ + 一条直线 $l$」且 $F$ 不在 $l$ 上，"
        r"**八成是 conic 的定义**（到焦点距离 = 到准线距离，或成比例 = 离心率）。"
        r"看到这个结构先往定义上想，能省大量计算。"
    ),
    'difficulty': 0.86,
    'topics': ['M-T-336'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-336-V2',
}

QS = [T336_E1, T336_V1, T336_V2]
