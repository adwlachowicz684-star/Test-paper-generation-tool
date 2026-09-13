# -*- coding: utf-8 -*-
r"""第 111 批：基本不等式「和积互消 / 分母为主元 / 柯西配对」+ 向量极化恒等式

    python3 tools/run_batch.py 111

## 选题依据

按「详解完整 + 同题型聚堆 + 无图依赖 + 可独立数值验算」筛出，原文集中在相邻 4 页：

- M-T-010 三题（p230–p231）：和积互消型
- M-T-011 三题（p231）：「1」的代换 / 分母为主元
- M-T-033 三题（p423）：柯西「分母分子配对」型
- M-T-239 三题（p205）：向量极化恒等式

12 题全部由我独立推导一遍并数值对拍（过程写进每题 review）。

## 第一条：有常数 + 有和 + 有积 ⟹ 积换成和的平方（M-T-010-V2）

这是「和积互消」的标准动作。由 $2x+9y+6xy=9$ 得 $6xy=9-\left(2x+9y\right)$，
再用 $6xy=\dfrac13\left(2x\right)\left(9y\right)\le\dfrac1{12}\left(2x+9y\right)^2$，
把「积」换成「和的平方」，就得到关于 $t=2x+9y$ 的一元二次不等式。

> ⭐⭐ 判据：题给等式里**同时出现「和」「积」「常数」**时，就把积放大成和的平方，
> 剩下的全是「和」，解一元二次即可。反之（求积的最值）就把和缩小成 $2\sqrt{积}$。

## 第二条：$x$ 拆成 $\dfrac12\left(x+y\right)+\dfrac12\left(x-y\right)$（M-T-011-V3）

这是「分母为主元」型的核心拆法：

$$x+\frac4{x+y}+\frac1{x-y}=\frac{x+y}2+\frac4{x+y}+\frac{x-y}2+\frac1{x-y}$$

拆完每个分式**只含一个变量**，两组各自用基本不等式。

> ⭐⭐ 凡分母是 $x+y$ 与 $x-y$，就把孤立的 $x$（或 $y$）拆成两分母的线性组合。
> 系数由 $\left(x+y\right)+\left(x-y\right)=2x$ 反解。

## 第三条：柯西「分母分子配对」的取等条件（M-T-033-E1）

$\left(a+2b+c\right)\left(\dfrac1a+\dfrac1b+\dfrac1c\right)$ 用柯西时，
要配成 $\left[\left(\sqrt a\right)^2+\left(\sqrt{2b}\right)^2+\left(\sqrt c\right)^2\right]\cdot\left[\dfrac1a+\dfrac1b+\dfrac1c\right]$，
中间项是 $1+\sqrt2+1$ —— **$\sqrt2$ 来自 $\sqrt{2b}\cdot\dfrac1{\sqrt b}$**。

> ⭐⭐ 系数 $2$ 在根号下变成 $\sqrt2$，这个「$\sqrt{\text{系数}}$」是此类题的通用规律，
> 见到 $\left(a+2b+c\right)\left(\dfrac1a+\dfrac1b+\dfrac1c\right)$ 就该想到答案含 $4\sqrt2$。

## 第四条：极化恒等式（M-T-239 全组）

$$\overrightarrow{PX}\cdot\overrightarrow{PY}=\left|\overrightarrow{PM}\right|^2-\left|\overrightarrow{MX}\right|^2\qquad\left(M\text{ 为 }XY\text{ 中点}\right)$$

三题分别是它的三种用法：

- **E1**：$D,E,F$ 都在 $BC$ 的中线上，三个数量积只差「$P$ 到 $D$ 的距离」，作差即可
- **V1**：$AB$ 是直径 ⟹ $C$ 是中点 ⟹ $\overrightarrow{PA}\cdot\overrightarrow{PB}=\left|PC\right|^2-r^2$
- **V2**：球面上三点，全部用 $\overrightarrow{OP},\overrightarrow{OA},\overrightarrow{OB}$ 表示

> ⭐⭐ 判据：**题目问两个「共起点」向量的数量积，且这两点的中点是已知/易求的**。
"""

# ==========================================================================
#  M-T-010  和积互消型
# ==========================================================================

T010_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知 $x>0$，$y>0$，且 $4x+2y-xy=0$，则 $2x+y$ 的最小值为（　　）"
    ),
    'stem': [
        r"已知 $x>0$，$y>0$，且 $4x+2y-xy=0$，则 $2x+y$ 的最小值为（　　）",
    ],
    'opts': [
        ('A', r"$16$"),
        ('B', r"$8+4\sqrt2$"),
        ('C', r"$12$"),
        ('D', r"$6+4\sqrt2$"),
    ],
    'answer': 'A',
    'analysis': (
        r"等式两边同除以 $xy$ 得 $\dfrac2x+\dfrac4y=1$，这是标准的「$1$ 的代换」结构；" "\n"
        r"再用乘「$1$」法展开，交叉项用基本不等式即可。关键是**先看出怎么化成 $=1$**。"
    ),
    'solution': (
        r"由 $4x+2y-xy=0$ 得 $xy=4x+2y$。因 $x>0$、$y>0$，两边同除以 $xy$：" "\n"
        r"$$\frac4y+\frac2x=1,\quad\text{即}\quad\frac2x+\frac4y=1.$$" "\n"
        r"于是（乘「$1$」法）" "\n"
        r"$$2x+y=\left(2x+y\right)\left(\frac2x+\frac4y\right)=4+\frac{8x}y+\frac{2y}x+4=8+\frac{8x}y+\frac{2y}x.$$" "\n"
        r"由基本不等式" "\n"
        r"$$\frac{8x}y+\frac{2y}x\ge2\sqrt{\frac{8x}y\cdot\frac{2y}x}=2\sqrt{16}=8,$$" "\n"
        r"故 $2x+y\ge8+8=16$。" "\n"
        r"取等条件：$\dfrac{8x}y=\dfrac{2y}x$，即 $y^2=4x^2$，因 $x,y>0$ 得 $y=2x$。" "\n"
        r"代回 $\dfrac2x+\dfrac4y=1$：由 $y=2x$ 得 $\dfrac4y=\dfrac4{2x}=\dfrac2x$，故 $\dfrac2x+\dfrac2x=1$，得 $x=4$、$y=8$。" "\n"
        r"故最小值为 $\boxed{16}$，选 A。"
    ),
    'review': (
        r"① ⭐⭐ **题眼是同除以 $xy$**：$xy=4x+2y$ ⟹ $\dfrac4y+\dfrac2x=1$。" "\n"
        r"   凡「$xy$ 与 $x,y$ 的一次式同现且无常数项」，就同除以 $xy$ 凑出 $=1$。" "\n"
        r"② ⭐ 展开时**别漏常数项**：$\left(2x\right)\cdot\dfrac2x=4$、$y\cdot\dfrac4y=4$，合计 $8$（不是 $0$）。" "\n"
        r"   干扰项 B（$8+4\sqrt2$）正是漏掉/记错常数项的结果。" "\n"
        r"③ 数值复核：$x=4$、$y=8$ 时 $4x+2y-xy=16+16-32=0$ ✓，$2x+y=16$ ✓。" "\n"
        r"   另取 $x=5$：由 $\dfrac4y=1-\dfrac25=0.6$ 得 $y=\dfrac{20}3\approx6.667$，$2x+y\approx16.667>16$ ✓" "\n"
        r"**通法（和积互消 · 求和型）**：" "\n"
        r"① 同除以 $xy$ 凑出 $\dfrac{\alpha}x+\dfrac{\beta}y=1$；" "\n"
        r"② 所求式乘「$1$」展开，常数项 + 两个互为倒数的交叉项；" "\n"
        r"③ 基本不等式 + 回代求取等点（必须验证取等点在定义域内）。"
    ),
    'difficulty': 0.55,
    'topics': ['M-T-010'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-010-V1',
}

T010_V2 = {
    'type': '填空',
    'stem_text': (
        r"已知 $x>0$，$y>0$，且 $2x+9y+6xy=9$，则 $2x+9y$ 的最小值为 ____"
    ),
    'stem': [
        r"已知 $x>0$，$y>0$，且 $2x+9y+6xy=9$，则 $2x+9y$ 的最小值为 ____",
    ],
    'opts': [],
    'answer': r"$6$",
    'analysis': (
        r"把 $6xy$ 写成 $\dfrac13\left(2x\right)\left(9y\right)$，用 $\left(2x\right)\left(9y\right)\le\left(\dfrac{2x+9y}2\right)^2$" "\n"
        r"把「积」换成「和的平方」，得到关于 $2x+9y$ 的一元二次不等式，解之即可。"
    ),
    'solution': (
        r"由 $2x+9y+6xy=9$ 得 $6xy=9-\left(2x+9y\right)$。" "\n"
        r"另一方面，把 $6xy$ 配成 $\left(2x\right)$ 与 $\left(9y\right)$ 的乘积：" "\n"
        r"$$6xy=\frac13\cdot\left(2x\right)\cdot\left(9y\right)\le\frac13\cdot\left(\frac{2x+9y}2\right)^2=\frac1{12}\left(2x+9y\right)^2.$$" "\n"
        r"两式合并：" "\n"
        r"$$9-\left(2x+9y\right)\le\frac1{12}\left(2x+9y\right)^2.$$" "\n"
        r"令 $t=2x+9y>0$，则 $t^2+12t-108\ge0$，即 $\left(t+18\right)\left(t-6\right)\ge0$。" "\n"
        r"因 $t>0$，得 $t\ge6$。" "\n"
        r"取等条件：$2x=9y$，代回 $2x+9y+6xy=9$ 得 $9y+\dfrac{6\cdot9y^2}{2}=9$，" "\n"
        r"即 $2x=9y=3$，所以 $x=\dfrac32$、$y=\dfrac13$。" "\n"
        r"故 $2x+9y$ 的最小值为 $\boxed{6}$。"
    ),
    'review': (
        r"① ⭐⭐ **「有常数 + 有和 + 有积」⟹ 把积放大成和的平方**：" "\n"
        r"   这是求和最值时的标准动作（求积最值时反过来，把和缩小成 $2\sqrt{积}$）。" "\n"
        r"② ⭐ **系数 $\dfrac13$ 是凑出来的**：要出现 $\left(2x\right)\left(9y\right)$ 就得补 $\dfrac13$（因 $\dfrac13\cdot2\cdot9=6$）。" "\n"
        r"   **目的只有一个——让乘积的两个因子恰好是所求式里的那两项 $2x$ 与 $9y$**。" "\n"
        r"③ ⚠ 解出 $t\ge6$ 或 $t\le-18$ 后，**必须用 $t>0$ 舍掉负支**，否则会得错误答案。" "\n"
        r"④ 数值复核：$x=\dfrac32$、$y=\dfrac13$ 时" "\n"
        r"   $2x+9y+6xy=3+3+6\cdot\dfrac32\cdot\dfrac13=3+3+3=9$ ✓，$2x+9y=6$ ✓。" "\n"
        r"**通法（和积互消 · 无 $=1$ 可凑时）**：" "\n"
        r"① 把条件写成「积 = 常数 − 和」；" "\n"
        r"② 用 $uv\le\left(\dfrac{u+v}2\right)^2$ 把左边换成「和的平方」，两因子取所求式的两项；" "\n"
        r"③ 解一元二次不等式，用正性舍支；" "\n"
        r"④ 由取等条件 $u=v$ 回代求具体取值。"
    ),
    'difficulty': 0.60,
    'topics': ['M-T-010'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-010-V2',
}

T010_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知 $x>0$，$y>0$，$x+2y+xy-6=0$，则说法不正确的是（　　）"
    ),
    'stem': [
        r"已知 $x>0$，$y>0$，$x+2y+xy-6=0$，则说法不正确的是（　　）",
    ],
    'opts': [
        ('A', r"$xy$ 的最大值为 $2$"),
        ('B', r"$x+2y$ 的最小值为 $4$"),
        ('C', r"$x+y$ 的最小值为 $3$"),
        ('D', r"$x+y$ 的最小值为 $4\sqrt2-3$"),
    ],
    'answer': 'C',
    'analysis': (
        r"A、B 两问都是「把其中一个量用另一个表示 + 基本不等式」；" "\n"
        r"C、D 则用判别式法：令 $m=x+y$，把 $y=m-x$ 代入原条件得关于 $x$ 的二次方程，$\Delta\ge0$ 给出 $m$ 的范围。" "\n"
        r"**A 与 B 的取等点都是 $x=2,y=1$**，此时 $x+y=3$，但 C、D 说明真正的最小值更小 —— 这是本题的陷阱。"
    ),
    'solution': (
        r"**A 选项**：由 $x+2y\ge2\sqrt{2xy}$，又 $x+2y=6-xy$，故 $6-xy\ge2\sqrt{2xy}$。" "\n"
        r"令 $t=\sqrt{xy}>0$，则 $t^2+2\sqrt2\,t-6\le0$，即 $\left(t+\sqrt2\right)^2\le8$，" "\n"
        r"得 $0<t\le\sqrt2$，即 $xy\le2$。取等 $x=2y$ 且 $x+2y=4$ ⟹ $x=2$、$y=1$，A 正确。" "\n"
        r"**B 选项**：由 $x+2y\ge2\sqrt{2xy}$ 两边平方得 $\dfrac{\left(x+2y\right)^2}8\ge xy$，" "\n"
        r"又 $xy=6-\left(x+2y\right)$，令 $s=x+2y>0$，则 $\dfrac{s^2}8\ge6-s$，" "\n"
        r"即 $s^2+8s-48\ge0$，$\left(s+12\right)\left(s-4\right)\ge0$，得 $s\ge4$。取等 $x=2$、$y=1$，B 正确。" "\n"
        r"**C、D 选项**：令 $m=x+y$（$m>0$），则 $y=m-x$，代入 $x+2y+xy-6=0$：" "\n"
        r"$$x+2\left(m-x\right)+x\left(m-x\right)-6=0\ \Longrightarrow\ x^2+\left(1-m\right)x+6-2m=0.$$" "\n"
        r"此方程有实数解，故" "\n"
        r"$$\Delta=\left(1-m\right)^2-4\left(6-2m\right)=m^2+6m-23\ge0,$$" "\n"
        r"解得 $m\ge-3+4\sqrt2$ 或 $m\le-3-4\sqrt2$（舍）。" "\n"
        r"故 $x+y$ 的最小值为 $4\sqrt2-3$，**C 错误、D 正确**。" "\n"
        r"综上，选 $\boxed{\text{C}}$。"
    ),
    'review': (
        r"① ⭐⭐ **判别式法是求 $x+y$ 型最值的通用武器**：把 $y=m-x$ 代入条件，" "\n"
        r"   得到关于 $x$ 的二次方程，$\Delta\ge0$ 直接给出 $m$ 的范围。比消元配方快。" "\n"
        r"② ⚠ **A、B 的取等点相同（$x=2,y=1$），但 C、D 的取等点不同** —— 这是本题最大的坑：" "\n"
        r"   由 A、B 成立很容易误以为 $x=2,y=1$ 也是 $x+y$ 的最值点，于是选 D 为「不正确」。" "\n"
        r"   实际上 $x+y$ 的最小值 $4\sqrt2-3\approx2.6569<3$，取等点是 $x=2\sqrt2-2$、$y=2\sqrt2-1$。" "\n"
        r"③ 数值复核：$m=4\sqrt2-3\approx2.65685$ 时 $\Delta=0$，$x=\dfrac{m-1}2=2\sqrt2-2\approx0.82843$、" "\n"
        r"   $y=2\sqrt2-1\approx1.82843$，代回 $x+2y+xy=0.82843+3.65685+1.51472=6.00000$ ✓" "\n"
        r"   而 $x=2,y=1$ 时 $x+y=3>2.65685$，可见 $3$ 不是最小值，C 确实错误 ✓" "\n"
        r"**通法（判别式法求二元和/差的最值）**：" "\n"
        r"① 设 $m=x+y$（或 $x-y$、$x+2y$ 等），把 $y$ 用 $m,x$ 表示后代入条件；" "\n"
        r"② 整理成关于 $x$ 的二次方程，令 $\Delta\ge0$；" "\n"
        r"③ 解出 $m$ 的范围，由 $\Delta=0$ 时 $x=-\dfrac b{2a}$ 反求取等点并代回验证。"
    ),
    'difficulty': 0.70,
    'topics': ['M-T-010'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-010-V3',
}

# ==========================================================================
#  M-T-011  「1」的代换 / 分母为主元
# ==========================================================================

T011_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知 $x>1$，$y>0$，且 $\dfrac1{x-1}+\dfrac2y=1$，则 $x+2y-1$ 的最小值为（　　）"
    ),
    'stem': [
        r"已知 $x>1$，$y>0$，且 $\dfrac1{x-1}+\dfrac2y=1$，则 $x+2y-1$ 的最小值为（　　）",
    ],
    'opts': [
        ('A', r"$9$"),
        ('B', r"$10$"),
        ('C', r"$11$"),
        ('D', r"$7+2\sqrt6$"),
    ],
    'answer': 'A',
    'analysis': (
        r"把所求式写成 $\left(x-1\right)+2y$，与条件的两个分母**完全对齐**，" "\n"
        r"于是直接乘「$1$」展开即可。$x>1$ 保证了 $x-1>0$，可以用基本不等式。"
    ),
    'solution': (
        r"由 $x>1$ 得 $x-1>0$，故 $x+2y-1=\left(x-1\right)+2y$，两个加数都为正。" "\n"
        r"乘「$1$」（即乘 $\dfrac1{x-1}+\dfrac2y$）：" "\n"
        r"$$\left(x-1\right)+2y=\left[\left(x-1\right)+2y\right]\left(\frac1{x-1}+\frac2y\right)$$" "\n"
        r"$$=1+\frac{2\left(x-1\right)}y+\frac{2y}{x-1}+4=5+\frac{2\left(x-1\right)}y+\frac{2y}{x-1}.$$" "\n"
        r"由基本不等式" "\n"
        r"$$\frac{2\left(x-1\right)}y+\frac{2y}{x-1}\ge2\sqrt{\frac{2\left(x-1\right)}y\cdot\frac{2y}{x-1}}=2\sqrt4=4,$$" "\n"
        r"故 $x+2y-1\ge5+4=9$。" "\n"
        r"取等条件：$\dfrac{2\left(x-1\right)}y=\dfrac{2y}{x-1}$，即 $\left(x-1\right)^2=y^2$，由正性得 $x-1=y$。" "\n"
        r"代回 $\dfrac1{x-1}+\dfrac2y=1$：$\dfrac1y+\dfrac2y=1$，得 $y=3$、$x=4$。" "\n"
        r"故最小值为 $\boxed9$，选 A。"
    ),
    'review': (
        r"① ⭐⭐ **所求式必须写成与分母对齐的形式**：$x+2y-1=\left(x-1\right)+2y$，" "\n"
        r"   两个加数恰好是条件中两个分母的「分子」。**不对齐就展开不出常数项**。" "\n"
        r"② ⭐ **$x>1$ 这个条件不是装饰**：它保证 $x-1>0$，是基本不等式「一正」的前提，" "\n"
        r"   也是最后取等时 $\left(x-1\right)^2=y^2$ ⟹ $x-1=y$（而非 $x-1=-y$）的依据。" "\n"
        r"③ 数值复核：$x=4$、$y=3$ 时 $\dfrac1{x-1}+\dfrac2y=\dfrac13+\dfrac23=1$ ✓，$x+2y-1=4+6-1=9$ ✓" "\n"
        r"**通法（「$1$」的代换 · 分母带平移）**：" "\n"
        r"① 把所求式凑成「各分母分子之和」的形式；" "\n"
        r"② 乘「$1$」展开成「常数 + 两组互为倒数的项」；" "\n"
        r"③ 基本不等式求下界，由取等条件回代求取值。"
    ),
    'difficulty': 0.55,
    'topics': ['M-T-011'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-011-V1',
}

T011_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知正数 $a$、$b$ 满足 $a+b=1$，则 $\dfrac{4a}{1-a}+\dfrac b{1-b}$ 的最小值是（　　）"
    ),
    'stem': [
        r"已知正数 $a$、$b$ 满足 $a+b=1$，则 $\dfrac{4a}{1-a}+\dfrac b{1-b}$ 的最小值是（　　）",
    ],
    'opts': [
        ('A', r"$1$"),
        ('B', r"$2$"),
        ('C', r"$4$"),
        ('D', r"$8$"),
    ],
    'answer': 'C',
    'analysis': (
        r"由 $a+b=1$ 得 $1-a=b$、$1-b=a$，两个分母**恰好就是另一个字母**，" "\n"
        r"式子立刻化成 $\dfrac{4a}b+\dfrac ba$，一组互为倒数的项，基本不等式一步到位。"
    ),
    'solution': (
        r"由 $a+b=1$ 且 $a,b>0$ 得 $1-a=b$、$1-b=a$，于是" "\n"
        r"$$\frac{4a}{1-a}+\frac b{1-b}=\frac{4a}b+\frac ba.$$" "\n"
        r"由基本不等式" "\n"
        r"$$\frac{4a}b+\frac ba\ge2\sqrt{\frac{4a}b\cdot\frac ba}=2\sqrt4=4.$$" "\n"
        r"取等条件：$\dfrac{4a}b=\dfrac ba$，即 $b^2=4a^2$，由正性得 $b=2a$。" "\n"
        r"结合 $a+b=1$ 得 $a=\dfrac13$、$b=\dfrac23$。" "\n"
        r"故最小值为 $\boxed4$，选 C。" "\n"
        r"（另法：$\dfrac{4a}b+\dfrac ba=\left(\dfrac4b+\dfrac1a\right)\left(a+b\right)-5=\dfrac{4a}b+\dfrac ba$，结果相同。）"
    ),
    'review': (
        r"① ⭐⭐ **题眼是 $1-a=b$、$1-b=a$**：分母在 $a+b=1$ 时恰好等于另一个字母。" "\n"
        r"   凡是分式分母形如 $1-a$、$1-b$，而条件又给了 $a+b=1$，先做这个替换。" "\n"
        r"② ⭐ **替换后是「$k\cdot\dfrac ab+\dfrac ba$」型**，最小值就是 $2\sqrt k$（本题 $k=4$，得 $4$）。" "\n"
        r"   这个结论可直接用于选择填空：$k=4$ ⟹ $2\sqrt4=4$。" "\n"
        r"③ 数值复核：$a=\dfrac13$、$b=\dfrac23$ 时" "\n"
        r"   $\dfrac{4a}{1-a}=\dfrac{4/3}{2/3}=2$，$\dfrac b{1-b}=\dfrac{2/3}{1/3}=2$，和为 $4$ ✓" "\n"
        r"   另取 $a=\dfrac12$、$b=\dfrac12$：$1+1=2$？不对 —— $\dfrac{4\cdot0.5}{0.5}=4$、$\dfrac{0.5}{0.5}=1$，和为 $5>4$ ✓" "\n"
        r"**通法（分母 = 另一个字母）**：" "\n"
        r"① 用条件把分母换成另一个变量；" "\n"
        r"② 化为 $k\cdot\dfrac uv+\dfrac vu$ 型，最小值 $2\sqrt k$；" "\n"
        r"③ 取等 $v=\sqrt k\,u$，回代条件求具体值。"
    ),
    'difficulty': 0.50,
    'topics': ['M-T-011'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-011-V2',
}

T011_V3 = {
    'type': '选择',
    'stem_text': (
        r"设 $x>y>0$，则 $x+\dfrac4{x+y}+\dfrac1{x-y}$ 的最小值为（　　）"
    ),
    'stem': [
        r"设 $x>y>0$，则 $x+\dfrac4{x+y}+\dfrac1{x-y}$ 的最小值为（　　）",
    ],
    'opts': [
        ('A', r"$3\sqrt2$"),
        ('B', r"$2\sqrt3$"),
        ('C', r"$4$"),
        ('D', r"$\dfrac{3\sqrt{10}}2$"),
    ],
    'answer': 'A',
    'analysis': (
        r"两个分母是 $x+y$ 与 $x-y$，而 $\left(x+y\right)+\left(x-y\right)=2x$，" "\n"
        r"故把孤立的 $x$ 拆成 $\dfrac12\left(x+y\right)+\dfrac12\left(x-y\right)$，每个分式只含一个变量。"
    ),
    'solution': (
        r"由 $\left(x+y\right)+\left(x-y\right)=2x$ 得 $x=\dfrac{x+y}2+\dfrac{x-y}2$，于是" "\n"
        r"$$x+\frac4{x+y}+\frac1{x-y}=\underbrace{\frac{x+y}2+\frac4{x+y}}_{\text{只含 }x+y}+\underbrace{\frac{x-y}2+\frac1{x-y}}_{\text{只含 }x-y}.$$" "\n"
        r"由 $x>y>0$ 得 $x+y>0$、$x-y>0$，两组分别用基本不等式：" "\n"
        r"$$\frac{x+y}2+\frac4{x+y}\ge2\sqrt{\frac{x+y}2\cdot\frac4{x+y}}=2\sqrt2,$$" "\n"
        r"$$\frac{x-y}2+\frac1{x-y}\ge2\sqrt{\frac{x-y}2\cdot\frac1{x-y}}=\sqrt2.$$" "\n"
        r"故原式 $\ge2\sqrt2+\sqrt2=3\sqrt2$。" "\n"
        r"取等条件：$\dfrac{x+y}2=\dfrac4{x+y}$ 且 $\dfrac{x-y}2=\dfrac1{x-y}$，" "\n"
        r"即 $\left(x+y\right)^2=8$、$\left(x-y\right)^2=2$，由正性得 $x+y=2\sqrt2$、$x-y=\sqrt2$，" "\n"
        r"解得 $x=\dfrac{3\sqrt2}2$、$y=\dfrac{\sqrt2}2$（满足 $x>y>0$）。" "\n"
        r"故最小值为 $\boxed{3\sqrt2}$，选 A。"
    ),
    'review': (
        r"① ⭐⭐ **核心拆法：$x=\dfrac12\left(x+y\right)+\dfrac12\left(x-y\right)$**。" "\n"
        r"   这是「分母为主元」型的通用技巧：让每个分式只含一个变量，才能分别用基本不等式。" "\n"
        r"   系数由 $\left(x+y\right)+\left(x-y\right)=2x$ 反解。若所求式是 $y$，则用 $\left(x+y\right)-\left(x-y\right)=2y$。" "\n"
        r"② ⭐ **拆完两组可以分别取等**：因为 $x+y$ 与 $x-y$ 只要满足 $x>y>0$ 就可独立取值" "\n"
        r"   （给定任意正数 $u=x+y$、$v=x-y$，总有 $x=\dfrac{u+v}2$、$y=\dfrac{u-v}2$，只需 $u>v$）。" "\n"
        r"   本题取等时 $u=2\sqrt2$、$v=\sqrt2$，确实 $u>v$ ✓" "\n"
        r"③ ⚠ **干扰项 D**：$\dfrac{3\sqrt{10}}2\approx4.743$ 比正确答案 $3\sqrt2\approx4.243$ 大，" "\n"
        r"   是「把 $x$ 当作独立变量、只对两个分式的和用基本不等式」的错误结果。" "\n"
        r"④ 数值复核：$x=\dfrac{3\sqrt2}2\approx2.12132$、$y=\dfrac{\sqrt2}2\approx0.70711$ 时" "\n"
        r"   $x+y=2.82843=2\sqrt2$ ✓、$x-y=1.41421=\sqrt2$ ✓，" "\n"
        r"   原式 $=2.12132+\dfrac4{2.82843}+\dfrac1{1.41421}=2.12132+1.41421+0.70711=4.24264=3\sqrt2$ ✓" "\n"
        r"**通法（分母为 $x\pm y$ 型）**：" "\n"
        r"① 用 $x=\dfrac{\left(x+y\right)+\left(x-y\right)}2$（或 $y=\dfrac{\left(x+y\right)-\left(x-y\right)}2$）拆孤立项；" "\n"
        r"② 按 $x+y$、$x-y$ 分组，每组化成 $at+\dfrac bt$ 型；" "\n"
        r"③ 分别取最小，最后验证两组取等点可同时满足（本题自动满足）。"
    ),
    'difficulty': 0.65,
    'topics': ['M-T-011'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-011-V3',
}

# ==========================================================================
#  M-T-033  柯西「分母分子配对」型
# ==========================================================================

T033_E1 = {
    'type': '填空',
    'stem_text': (
        r"已知 $a,b,c$ 都是正数，且 $a+2b+c=1$，则 $\dfrac1a+\dfrac1b+\dfrac1c$ 的最小值是 ____"
    ),
    'stem': [
        r"已知 $a,b,c$ 都是正数，且 $a+2b+c=1$，则 $\dfrac1a+\dfrac1b+\dfrac1c$ 的最小值是 ____",
    ],
    'opts': [],
    'answer': r"$6+4\sqrt2$",
    'analysis': (
        r"把所求式乘上等于 $1$ 的 $a+2b+c$，再用柯西不等式（或展开后用均值不等式）。" "\n"
        r"柯西配凑时中间项是 $1+\sqrt2+1$，其中 $\sqrt2$ 来自 $\sqrt{2b}\cdot\dfrac1{\sqrt b}$。"
    ),
    'solution': (
        r"**方法一（柯西不等式）**：因 $a+2b+c=1$，" "\n"
        r"$$\frac1a+\frac1b+\frac1c=\left(a+2b+c\right)\left(\frac1a+\frac1b+\frac1c\right)$$" "\n"
        r"$$=\left[\left(\sqrt a\right)^2+\left(\sqrt{2b}\right)^2+\left(\sqrt c\right)^2\right]\left[\left(\frac1{\sqrt a}\right)^2+\left(\frac1{\sqrt b}\right)^2+\left(\frac1{\sqrt c}\right)^2\right]$$" "\n"
        r"$$\ge\left(\sqrt a\cdot\frac1{\sqrt a}+\sqrt{2b}\cdot\frac1{\sqrt b}+\sqrt c\cdot\frac1{\sqrt c}\right)^2=\left(1+\sqrt2+1\right)^2=\left(2+\sqrt2\right)^2=6+4\sqrt2.$$" "\n"
        r"**方法二（展开 + 均值不等式）**：" "\n"
        r"$$\left(a+2b+c\right)\left(\frac1a+\frac1b+\frac1c\right)=1+\frac ab+\frac ac+\frac{2b}a+2+\frac{2b}c+\frac ca+\frac cb+1$$" "\n"
        r"$$=4+\left(\frac ab+\frac{2b}a\right)+\left(\frac ac+\frac ca\right)+\left(\frac{2b}c+\frac cb\right)$$" "\n"
        r"$$\ge4+2\sqrt2+2+2\sqrt2=6+4\sqrt2.$$" "\n"
        r"取等条件：$\dfrac ab=\dfrac{2b}a$、$\dfrac ac=\dfrac ca$、$\dfrac{2b}c=\dfrac cb$，" "\n"
        r"即 $a=c=\sqrt2\,b$。代回 $a+2b+c=1$ 得 $2\sqrt2\,b+2b=1$，" "\n"
        r"$b=\dfrac1{2\left(1+\sqrt2\right)}=\dfrac{\sqrt2-1}2$，$a=c=\dfrac{2-\sqrt2}2$。" "\n"
        r"故最小值为 $\boxed{6+4\sqrt2}$。"
    ),
    'review': (
        r"① ⭐⭐ **系数在根号下开方**：$\sqrt{2b}\cdot\dfrac1{\sqrt b}=\sqrt2$，这是此类题的固定规律。" "\n"
        r"   见到 $\left(a+kb+c\right)\left(\dfrac1a+\dfrac1b+\dfrac1c\right)$，柯西中间项就是 $1+\sqrt k+1$，" "\n"
        r"   答案 $\left(2+\sqrt k\right)^2$。本题 $k=2$ ⟹ $\left(2+\sqrt2\right)^2=6+4\sqrt2$。" "\n"
        r"② ⭐ **方法二的三组分法有讲究**：展开的 $9$ 项里，$2$ 个 $1$ 先提出来，剩下 $6$ 项" "\n"
        r"   **按「互为倒数」配成三组**，每组用均值。随意配对会得到更弱的下界。" "\n"
        r"③ ⚠ **取等条件必须三组相容**：本题 $a=c=\sqrt2\,b$ 三组同时满足，故能取到。" "\n"
        r"   若遇到三元以上的题，取等条件不相容时，用均值法得到的下界是**取不到的**。" "\n"
        r"④ 数值复核：$b=\dfrac{\sqrt2-1}2\approx0.20711$、$a=c=\dfrac{2-\sqrt2}2\approx0.29289$，" "\n"
        r"   $a+2b+c=0.29289+0.41421+0.29289=1.00000$ ✓，" "\n"
        r"   $\dfrac1a+\dfrac1b+\dfrac1c=3.41421+4.82843+3.41421=11.65685=6+4\sqrt2$ ✓" "\n"
        r"**通法（柯西「分母分子配对」型）**：" "\n"
        r"① 所求式是倒数和，条件是各字母的一次和 ⟹ 乘「$1$」（即乘条件左边）；" "\n"
        r"② 配成 $\left[\left(\sqrt{\cdot}\right)^2+\cdots\right]\left[\left(\dfrac1{\sqrt{\cdot}}\right)^2+\cdots\right]$ 用柯西；" "\n"
        r"③ 中间项的 $\sqrt{\text{系数}}$ 是答案里根号的来源；" "\n"
        r"④ 也可用展开 + 均值（方法二），两者互为验证。"
    ),
    'difficulty': 0.65,
    'topics': ['M-T-033'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-033-E1',
}

T033_V2 = {
    'type': '填空',
    'stem_text': (
        r"已知 $x>0$，$y>0$，$z>0$，$x+2y+3z=3$，则 $\left(x+\dfrac1{4y}\right)^2+\left(2y+\dfrac1{6z}\right)^2+\left(3z+\dfrac1{2x}\right)^2$ 的最小值为 ____"
    ),
    'stem': [
        r"已知 $x>0$，$y>0$，$z>0$，$x+2y+3z=3$，则 $\left(x+\dfrac1{4y}\right)^2+\left(2y+\dfrac1{6z}\right)^2+\left(3z+\dfrac1{2x}\right)^2$ 的最小值为 ____",
    ],
    'opts': [],
    'answer': r"$\dfrac{27}4$",
    'analysis': (
        r"平方和用柯西 $\left(\sum a_i^2\right)\left(\sum 1^2\right)\ge\left(\sum a_i\right)^2$，" "\n"
        r"关键是把 $\sum a_i$ 里的 $\dfrac1{4y}+\dfrac1{6z}+\dfrac1{2x}$ 用 $x+2y+3z=3$ 整体代换，" "\n"
        r"化成 $\dfrac12\left(\dfrac1x+\dfrac1{2y}+\dfrac1{3z}\right)$ 后再用一次均值。"
    ),
    'solution': (
        r"记 $S=\left(x+\dfrac1{4y}\right)^2+\left(2y+\dfrac1{6z}\right)^2+\left(3z+\dfrac1{2x}\right)^2$。" "\n"
        r"**第一步（柯西配 $1+1+1$）**：" "\n"
        r"$$S\cdot3\ge\left[\left(x+\frac1{4y}\right)+\left(2y+\frac1{6z}\right)+\left(3z+\frac1{2x}\right)\right]^2.$$" "\n"
        r"**第二步（处理括号内）**：" "\n"
        r"$$\left(x+2y+3z\right)+\left(\frac1{4y}+\frac1{6z}+\frac1{2x}\right)=3+\frac12\left(\frac1x+\frac1{2y}+\frac1{3z}\right).$$" "\n"
        r"**第三步（用 $x+2y+3z=3$ 整体代换）**：" "\n"
        r"$$\frac3x=\frac{x+2y+3z}x=1+\frac{2y}x+\frac{3z}x,\quad\frac3{2y}=\frac{x+2y+3z}{2y}=\frac x{2y}+1+\frac{3z}{2y},\quad\frac3{3z}=\frac{x+2y+3z}{3z}=\frac x{3z}+\frac{2y}{3z}+1.$$" "\n"
        r"三式相加并除以 $3$：" "\n"
        r"$$\frac1x+\frac1{2y}+\frac1{3z}=\frac13\left(3+\frac{2y}x+\frac x{2y}+\frac x{3z}+\frac{3z}x+\frac{3z}{2y}+\frac{2y}{3z}\right)\ge\frac13\left(3+2+2+2\right)=3.$$" "\n"
        r"**第四步（合并）**：括号内 $\ge3+\dfrac12\cdot3=\dfrac92$，故" "\n"
        r"$$3S\ge\left(\frac92\right)^2=\frac{81}4\ \Longrightarrow\ S\ge\frac{27}4.$$" "\n"
        r"取等条件：$\dfrac{2y}x=\dfrac x{2y}$、$\dfrac x{3z}=\dfrac{3z}x$、$\dfrac{3z}{2y}=\dfrac{2y}{3z}$，" "\n"
        r"即 $x=2y=3z$。由 $x+2y+3z=3$ 得 $x=1$、$y=\dfrac12$、$z=\dfrac13$。" "\n"
        r"故最小值为 $\boxed{\dfrac{27}4}$。"
    ),
    'review': (
        r"① ⭐⭐ **平方和 ⟹ 柯西配 $\left(1,1,1\right)$**：这是把三个平方「压成一个和」的标准动作，" "\n"
        r"   代价是除以 $3$，收益是问题从「三个量」降到「一个和」。" "\n"
        r"② ⭐ **第三步的整体代换是题眼**：$\dfrac3x=\dfrac{x+2y+3z}x$，" "\n"
        r"   把「倒数」写成「条件/字母」，展开后自然出现 $\dfrac{2y}x$ 与 $\dfrac x{2y}$ 这样的倒数对。" "\n"
        r"   这一步不做，$\dfrac1x+\dfrac1{2y}+\dfrac1{3z}$ 无法与条件挂钩。" "\n"
        r"③ ⚠ **原书该条的详解字段为空，答案串进了 ans 字段**，我按上述四步重新整理；" "\n"
        r"   原书在第二步写的是 $\dfrac12\left(\dfrac1x+\dfrac1{2y}+\dfrac1{3z}\right)$，与我的推导一致 ✓" "\n"
        r"④ 数值复核：$x=1$、$y=\dfrac12$、$z=\dfrac13$ 时 $x+2y+3z=1+1+1=3$ ✓，" "\n"
        r"   三个括号依次为 $1+\dfrac12=\dfrac32$、$1+\dfrac12=\dfrac32$、$1+\dfrac12=\dfrac32$，" "\n"
        r"   $S=3\times\left(\dfrac32\right)^2=\dfrac{27}4=6.75$ ✓" "\n"
        r"**通法（平方和型柯西 + 倒数整体代换）**：" "\n"
        r"① $\sum a_i^2$ ⟹ 乘 $\sum 1^2=n$ 用柯西；" "\n"
        r"② 把和式里的倒数项用「条件 ÷ 字母」展开，凑出倒数对；" "\n"
        r"③ 每组倒数对 $\ge2$，数一数有几组；" "\n"
        r"④ 取等条件串成一条链（本题 $x=2y=3z$），回代条件求值。"
    ),
    'difficulty': 0.80,
    'topics': ['M-T-033'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-033-V2',
}

T033_V3 = {
    'type': '解答',
    'stem_text': (
        r"若关于 $x$ 的不等式 $\left|2x+2\right|-\left|2x-1\right|-t\ge0$ 在实数范围内有解．" "\n"
        r"（1）求实数 $t$ 的取值范围；" "\n"
        r"（2）若实数 $t$ 的最大值为 $a$，且正实数 $m,n,p$ 满足 $m+2n+3p=a$，求证：$\dfrac1{m+p}+\dfrac2{n+p}\ge3$．"
    ),
    'stem': [
        r"若关于 $x$ 的不等式 $\left|2x+2\right|-\left|2x-1\right|-t\ge0$ 在实数范围内有解．",
        r"（1）求实数 $t$ 的取值范围；",
        r"（2）若实数 $t$ 的最大值为 $a$，且正实数 $m,n,p$ 满足 $m+2n+3p=a$，求证：$\dfrac1{m+p}+\dfrac2{n+p}\ge3$．",
    ],
    'opts': [],
    'answer': r"（1）$t\le3$；（2）证明见解析",
    'analysis': (
        r"（1）「有解」⟺ $t\le\max\left(\left|2x+2\right|-\left|2x-1\right|\right)$，用 $\left|A\right|-\left|B\right|\le\left|A-B\right|$ 求最大值；" "\n"
        r"（2）关键是把 $m+2n+3p$ 写成 $\left(m+p\right)+2\left(n+p\right)$，与所求的两个分母对齐，再用乘「$1$」法或柯西。"
    ),
    'solution': (
        r"**（1）** 不等式 $\left|2x+2\right|-\left|2x-1\right|-t\ge0$ 有解" "\n"
        r"$\iff$ 存在 $x$ 使 $\left|2x+2\right|-\left|2x-1\right|\ge t$" "\n"
        r"$\iff t\le\max\limits_{x\in\mathbb R}\left(\left|2x+2\right|-\left|2x-1\right|\right)$。" "\n"
        r"由绝对值三角不等式 $\left|A\right|-\left|B\right|\le\left|A-B\right|$（取 $A=2x+2$、$B=2x-1$）：" "\n"
        r"$$\left|2x+2\right|-\left|2x-1\right|\le\left|\left(2x+2\right)-\left(2x-1\right)\right|=3.$$" "\n"
        r"又当 $x\ge\dfrac12$ 时 $2x+2>0$、$2x-1\ge0$，此时 $\left|2x+2\right|-\left|2x-1\right|=\left(2x+2\right)-\left(2x-1\right)=3$，" "\n"
        r"故最大值确为 $3$。所以 $\boxed{t\le3}$。" "\n"
        r"**（2）** 由（1）知 $a=3$，即 $m+2n+3p=3$。" "\n"
        r"注意到 $\left(m+p\right)+2\left(n+p\right)=m+2n+3p=3$，两个括号恰好是所求式的分母，" "\n"
        r"于是乘「$1$」（把 $3$ 写成 $\left(m+p\right)+2\left(n+p\right)$，并把 $\dfrac2{n+p}$ 写成 $\dfrac4{2n+2p}$）：" "\n"
        r"$$\frac1{m+p}+\frac2{n+p}=\frac13\left(\frac1{m+p}+\frac4{2n+2p}\right)\left[\left(m+p\right)+\left(2n+2p\right)\right]$$" "\n"
        r"$$=\frac13\left(1+4+\frac{2n+2p}{m+p}+\frac{4\left(m+p\right)}{2n+2p}\right)\ge\frac13\left(5+2\sqrt4\right)=\frac13\cdot9=3.$$" "\n"
        r"（用柯西更直接：$\dfrac13\left(\dfrac1{m+p}+\dfrac4{2n+2p}\right)\left[\left(m+p\right)+\left(2n+2p\right)\right]\ge\dfrac13\left(1+2\right)^2=3$。）" "\n"
        r"取等条件：$2n+2p=2\left(m+p\right)$，即 $m=n$，且 $m+p=1$。" "\n"
        r"故 $\dfrac1{m+p}+\dfrac2{n+p}\ge3$ 成立。"
    ),
    'review': (
        r"① ⭐⭐ **（1）的判据：「有解」⟺ $t\le$ 最大值，「恒成立」⟺ $t\le$ 最小值** ——" "\n"
        r"   这两个方向极易记反。本题是「在实数范围内**有解**」，故求最大值。" "\n"
        r"② ⭐ **$\left|A\right|-\left|B\right|\le\left|A-B\right|$ 是求此类最大值最快的路**，且必须验证等号可取到" "\n"
        r"   （本题 $x\ge\dfrac12$ 时两个绝对值内都非负，等号成立）。不验证就只能得到上界而非最大值。" "\n"
        r"③ ⭐⭐ **（2）的题眼：$m+2n+3p=\left(m+p\right)+2\left(n+p\right)$** ——" "\n"
        r"   把 $3p$ 拆成 $p+2p$，与所求的两个分母 $m+p$、$n+p$ 对齐。" "\n"
        r"   **凡是所求分母形如「字母 + 公共量」，先在条件里拆出这个结构**。" "\n"
        r"④ ⚠ **$\dfrac2{n+p}$ 要改写成 $\dfrac4{2n+2p}$**：这样两个分子 $1,4$ 与两个分母 $m+p,2n+2p$" "\n"
        r"   才能配成柯西的 $\left(1+2\right)^2$。不改写的話展开后是 $5+\dfrac{2\left(n+p\right)}{m+p}+\dfrac{2\left(m+p\right)}{n+p}$，" "\n"
        r"   最小值 $\dfrac13\left(5+4\right)=3$ 相同，但柯西形式不明显。" "\n"
        r"⑤ 数值复核：取 $p=0.2$、$m=n=0.8$，则 $m+2n+3p=0.8+1.6+0.6=3$ ✓，" "\n"
        r"   $\dfrac1{m+p}+\dfrac2{n+p}=\dfrac11+\dfrac21=3$ ✓（恰为取等点）。" "\n"
        r"   另取 $m=1$、$n=0.5$、$p=1/3$：$m+2n+3p=1+1+1=3$ ✓，左式 $=\dfrac1{4/3}+\dfrac2{5/6}=0.75+2.4=3.15>3$ ✓" "\n"
        r"**通法（绝对值差最大值 + 分母对齐型证明）**：" "\n"
        r"① 「有解」用最大值、「恒成立」用最小值；" "\n"
        r"② $\left|A\right|-\left|B\right|\le\left|A-B\right|$ 并验证等号；" "\n"
        r"③ 把条件拆成与所求分母一致的形式（$3p\to p+2p$）；" "\n"
        r"④ 统一分子分母后乘「$1$」展开，或直接柯西。"
    ),
    'difficulty': 0.75,
    'topics': ['M-T-033'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-033-V3',
}

# ==========================================================================
#  M-T-239  向量极化恒等式
# ==========================================================================

T239_E1 = {
    'type': '填空',
    'stem_text': (
        r"在 $\triangle ABC$ 中，$D$ 是 $BC$ 的中点，$E$、$F$ 是 $AD$ 上的两个三等分点，" "\n"
        r"$\overrightarrow{BA}\cdot\overrightarrow{CA}=4$，$\overrightarrow{BF}\cdot\overrightarrow{CF}=-1$，则 $\overrightarrow{BE}\cdot\overrightarrow{CE}$ 的值是 ____"
    ),
    'stem': [
        r"在 $\triangle ABC$ 中，$D$ 是 $BC$ 的中点，$E$、$F$ 是 $AD$ 上的两个三等分点，$\overrightarrow{BA}\cdot\overrightarrow{CA}=4$，$\overrightarrow{BF}\cdot\overrightarrow{CF}=-1$，则 $\overrightarrow{BE}\cdot\overrightarrow{CE}$ 的值是 ____",
    ],
    'opts': [],
    'answer': r"$\dfrac78$",
    'analysis': (
        r"三个数量积的两个因子都是「从 $B$、$C$ 出发指向 $AD$ 上某点」，" "\n"
        r"而 $\overrightarrow{BX}\cdot\overrightarrow{CX}=\overrightarrow{XB}\cdot\overrightarrow{XC}$，用极化恒等式（$D$ 为 $BC$ 中点）" "\n"
        r"可全部化为 $\left|XD\right|^2-\left|DB\right|^2$，三个式子只差 $\left|XD\right|^2$，作差即可。"
    ),
    'solution': (
        r"**解法一（基底法）**：令 $\overrightarrow{DF}=\vec a$、$\overrightarrow{DB}=\vec b$，" "\n"
        r"则 $\overrightarrow{DC}=-\vec b$，由 $E,F$ 为 $AD$ 的三等分点得 $\overrightarrow{DE}=2\vec a$、$\overrightarrow{DA}=3\vec a$。" "\n"
        r"于是 $\overrightarrow{BA}=\overrightarrow{BD}+\overrightarrow{DA}=3\vec a-\vec b$、$\overrightarrow{CA}=3\vec a+\vec b$，" "\n"
        r"$$\overrightarrow{BA}\cdot\overrightarrow{CA}=\left(3\vec a-\vec b\right)\cdot\left(3\vec a+\vec b\right)=9\left|\vec a\right|^2-\left|\vec b\right|^2=4;$$" "\n"
        r"$\overrightarrow{BF}=\vec a-\vec b$、$\overrightarrow{CF}=\vec a+\vec b$，" "\n"
        r"$$\overrightarrow{BF}\cdot\overrightarrow{CF}=\left|\vec a\right|^2-\left|\vec b\right|^2=-1.$$" "\n"
        r"两式相减：$8\left|\vec a\right|^2=5$，得 $\left|\vec a\right|^2=\dfrac58$、$\left|\vec b\right|^2=\dfrac{13}8$。" "\n"
        r"又 $\overrightarrow{BE}=2\vec a-\vec b$、$\overrightarrow{CE}=2\vec a+\vec b$，" "\n"
        r"$$\overrightarrow{BE}\cdot\overrightarrow{CE}=4\left|\vec a\right|^2-\left|\vec b\right|^2=\frac{20}8-\frac{13}8=\boxed{\frac78}.$$" "\n"
        r"**解法二（极化恒等式）**：$D$ 为 $BC$ 中点，由极化恒等式" "\n"
        r"$$\overrightarrow{XB}\cdot\overrightarrow{XC}=\left|\overrightarrow{XD}\right|^2-\left|\overrightarrow{DB}\right|^2\quad\left(X\text{ 为 }AD\text{ 上任意一点}\right).$$" "\n"
        r"注意到 $\overrightarrow{BA}\cdot\overrightarrow{CA}=\overrightarrow{AB}\cdot\overrightarrow{AC}$（两因子同时变号），故" "\n"
        r"$$\left|\overrightarrow{AD}\right|^2-\left|\overrightarrow{DB}\right|^2=4,\qquad\left|\overrightarrow{FD}\right|^2-\left|\overrightarrow{DB}\right|^2=-1.$$" "\n"
        r"由 $FD=\dfrac13AD$ 得 $\dfrac19\left|\overrightarrow{AD}\right|^2-\left|\overrightarrow{DB}\right|^2=-1$，与第一式相减：" "\n"
        r"$$\frac89\left|\overrightarrow{AD}\right|^2=5\ \Longrightarrow\ \left|\overrightarrow{AD}\right|^2=\frac{45}8,\quad\left|\overrightarrow{DB}\right|^2=\frac{13}8.$$" "\n"
        r"由 $ED=\dfrac23AD$ 得 $\left|\overrightarrow{ED}\right|^2=\dfrac49\cdot\dfrac{45}8=\dfrac52$，" "\n"
        r"$$\overrightarrow{BE}\cdot\overrightarrow{CE}=\overrightarrow{EB}\cdot\overrightarrow{EC}=\left|\overrightarrow{ED}\right|^2-\left|\overrightarrow{DB}\right|^2=\frac52-\frac{13}8=\boxed{\frac78}.$$"
    ),
    'review': (
        r"① ⭐⭐ **极化恒等式是本题的题眼**：$\overrightarrow{XB}\cdot\overrightarrow{XC}=\left|XD\right|^2-\left|DB\right|^2$（$D$ 为 $BC$ 中点）。" "\n"
        r"   三个数量积的公共部分是 $-\left|\overrightarrow{DB}\right|^2$，**作差即可消去它**。" "\n"
        r"② ⚠ **$\overrightarrow{BA}\cdot\overrightarrow{CA}=\overrightarrow{AB}\cdot\overrightarrow{AC}$**：两个因子同时取反，数量积不变。" "\n"
        r"   极化恒等式的标准形是 $\overrightarrow{AB}\cdot\overrightarrow{AC}$，必须先做这个转换。" "\n"
        r"③ ⚠ **原书 p205 详解有两处笔误**：" "\n"
        r"   「$\overrightarrow{BF}\cdot\overrightarrow{CA}=9\vec a^2-\vec b^2$」应为 $\overrightarrow{BA}\cdot\overrightarrow{CA}$；" "\n"
        r"   「由 $\overrightarrow{BC}\cdot\overrightarrow{CA}=4$，$\overrightarrow{BF}\cdot\overrightarrow{CF}=-1$」中的 $\overrightarrow{BC}\cdot\overrightarrow{CA}$ 应为 $\overrightarrow{BA}\cdot\overrightarrow{CA}$。" "\n"
        r"   按 $\overrightarrow{BC}\cdot\overrightarrow{CA}$ 或 $\overrightarrow{BF}\cdot\overrightarrow{CA}$ 均无法推出后续结果，已按正确形式录入。" "\n"
        r"④ ⭐ **$E$、$F$ 谁离 $D$ 近**：由 $\left|DF\right|=\left|\vec a\right|$、$\left|DE\right|=2\left|\vec a\right|$ 知 $F$ 近 $D$、$E$ 远 $D$，" "\n"
        r"   故 $ED=\dfrac23AD$（不是 $\dfrac13AD$）。若搞反会得到 $\dfrac19\cdot\dfrac{45}8-\dfrac{13}8<0$ 的错误结果。" "\n"
        r"⑤ 数值复核：$\left|\overrightarrow{AD}\right|^2=\dfrac{45}8=5.625$、$\left|\overrightarrow{DB}\right|^2=\dfrac{13}8=1.625$、" "\n"
        r"   $\left|\overrightarrow{ED}\right|^2=2.5$，$2.5-1.625=0.875=\dfrac78$ ✓" "\n"
        r"   用解法一交叉验证：$\left|\vec a\right|^2=\dfrac58=0.625$、$\left|\vec b\right|^2=\dfrac{13}8=1.625$、" "\n"
        r"   $4\times0.625-1.625=0.875$ ✓ 两法一致。" "\n"
        r"**通法（极化恒等式）**：" "\n"
        r"① 判据：数量积的两个向量**共起点**，且终点的中点已知或易求；" "\n"
        r"② $\overrightarrow{XA}\cdot\overrightarrow{XB}=\left|XM\right|^2-\left|MA\right|^2$（$M$ 为 $AB$ 中点）；" "\n"
        r"③ 多个数量积共线排列时（如本题 $A,E,F,D$ 共线），作差消去公共项；" "\n"
        r"④ 注意 $\overrightarrow{BA}\cdot\overrightarrow{CA}=\overrightarrow{AB}\cdot\overrightarrow{AC}$ 的等价转换。"
    ),
    'difficulty': 0.70,
    'topics': ['M-T-239'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-239-E1',
}

T239_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知圆 $C$ 的方程为 $\left(x-1\right)^2+\left(y-1\right)^2=2$，点 $P$ 在直线 $y=x+3$ 上，" "\n"
        r"线段 $AB$ 为圆 $C$ 的直径，则 $\overrightarrow{PA}\cdot\overrightarrow{PB}$ 的最小值为（　　）"
    ),
    'stem': [
        r"已知圆 $C$ 的方程为 $\left(x-1\right)^2+\left(y-1\right)^2=2$，点 $P$ 在直线 $y=x+3$ 上，线段 $AB$ 为圆 $C$ 的直径，则 $\overrightarrow{PA}\cdot\overrightarrow{PB}$ 的最小值为（　　）",
    ],
    'opts': [
        ('A', r"$2$"),
        ('B', r"$\dfrac52$"),
        ('C', r"$3$"),
        ('D', r"$\dfrac72$"),
    ],
    'answer': 'B',
    'analysis': (
        r"$AB$ 是直径 ⟹ 圆心 $C$ 是 $AB$ 中点，且 $\overrightarrow{CB}=-\overrightarrow{CA}$。" "\n"
        r"用极化恒等式（或直接用 $\overrightarrow{PA}=\overrightarrow{PC}+\overrightarrow{CA}$、$\overrightarrow{PB}=\overrightarrow{PC}-\overrightarrow{CA}$ 展开）" "\n"
        r"得 $\overrightarrow{PA}\cdot\overrightarrow{PB}=\left|PC\right|^2-r^2$，只剩下求 $\left|PC\right|$ 的最小值。"
    ),
    'solution': (
        r"圆心 $C\left(1,1\right)$，半径 $r=\sqrt2$。因 $AB$ 为直径，故 $C$ 是 $AB$ 中点且 $\overrightarrow{CB}=-\overrightarrow{CA}$。" "\n"
        r"于是" "\n"
        r"$$\overrightarrow{PA}\cdot\overrightarrow{PB}=\left(\overrightarrow{PC}+\overrightarrow{CA}\right)\cdot\left(\overrightarrow{PC}+\overrightarrow{CB}\right)=\left(\overrightarrow{PC}+\overrightarrow{CA}\right)\cdot\left(\overrightarrow{PC}-\overrightarrow{CA}\right)=\left|\overrightarrow{PC}\right|^2-\left|\overrightarrow{CA}\right|^2.$$" "\n"
        r"而 $\left|\overrightarrow{CA}\right|=r=\sqrt2$，故 $\left|\overrightarrow{CA}\right|^2=2$，" "\n"
        r"$$\overrightarrow{PA}\cdot\overrightarrow{PB}=\left|\overrightarrow{PC}\right|^2-2.$$" "\n"
        r"点 $P$ 在直线 $x-y+3=0$ 上，故 $\left|\overrightarrow{PC}\right|$ 的最小值就是圆心 $C\left(1,1\right)$ 到该直线的距离：" "\n"
        r"$$d=\frac{\left|1-1+3\right|}{\sqrt{1^2+\left(-1\right)^2}}=\frac3{\sqrt2}.$$" "\n"
        r"因此 $\overrightarrow{PA}\cdot\overrightarrow{PB}$ 的最小值为" "\n"
        r"$$d^2-2=\frac92-2=\boxed{\frac52}.$$" "\n"
        r"选 B。"
    ),
    'review': (
        r"① ⭐⭐ **「$AB$ 是圆 $C$ 的直径」⟹ $\overrightarrow{PA}\cdot\overrightarrow{PB}=\left|PC\right|^2-r^2$**：" "\n"
        r"   这是极化恒等式在圆上的直接推论，把 $A,B$ 两个动端点完全消掉，" "\n"
        r"   问题退化成「圆心到已知直线的距离」。可当二级结论直接记。" "\n"
        r"② ⭐ **展开时 $\overrightarrow{CB}=-\overrightarrow{CA}$ 是关键**：这才出现平方差。" "\n"
        r"   若写成 $\overrightarrow{PC}+\overrightarrow{CB}$ 而忘了 $\overrightarrow{CB}=-\overrightarrow{CA}$，就得不出平方差。" "\n"
        r"③ ⚠ **别忘了减 $r^2$**：$\left|PC\right|_{\min}^2=\dfrac92=4.5$，减 $2$ 才是 $\dfrac52=2.5$。" "\n"
        r"   干扰项 D（$\dfrac72=3.5$）是减了 $1$ 的结果，A（$2$）是 $\left|PC\right|_{\min}^2-\dfrac52$ 之类的误算。" "\n"
        r"④ 数值复核：$d=\dfrac3{\sqrt2}\approx2.12132$，$d^2=4.5$，$4.5-2=2.5=\dfrac52$ ✓" "\n"
        r"   垂足验证：直线 $y=x+3$ 方向 $\left(1,1\right)$，过 $C\left(1,1\right)$ 的垂线 $y=-x+2$，" "\n"
        r"   联立得垂足 $\left(-\dfrac12,\dfrac52\right)$，$\left|PC\right|^2=\left(\dfrac32\right)^2+\left(\dfrac32\right)^2=\dfrac92$ ✓" "\n"
        r"**通法（直径型数量积）**：" "\n"
        r"① 「$AB$ 是圆 $C$ 的直径」⟹ $C$ 为中点、$\overrightarrow{CB}=-\overrightarrow{CA}$、$\left|\overrightarrow{CA}\right|=r$；" "\n"
        r"② $\overrightarrow{PA}\cdot\overrightarrow{PB}=\left(\overrightarrow{PC}+\overrightarrow{CA}\right)\cdot\left(\overrightarrow{PC}-\overrightarrow{CA}\right)=\left|PC\right|^2-r^2$；" "\n"
        r"③ 求 $\left|PC\right|$ 的最值（点到直线距离 / 点到圆上点距离）。"
    ),
    'difficulty': 0.60,
    'topics': ['M-T-239'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-239-V1',
}

T239_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知球 $O$ 的半径为 $1$，$A$、$B$ 是球面上的两点，且 $AB=\sqrt3$，若点 $P$ 是球面上任意一点，" "\n"
        r"则 $\overrightarrow{PA}\cdot\overrightarrow{PB}$ 的取值范围是（　　）"
    ),
    'stem': [
        r"已知球 $O$ 的半径为 $1$，$A$、$B$ 是球面上的两点，且 $AB=\sqrt3$，若点 $P$ 是球面上任意一点，则 $\overrightarrow{PA}\cdot\overrightarrow{PB}$ 的取值范围是（　　）",
    ],
    'opts': [
        ('A', r"$\left[-\dfrac32,\dfrac12\right]$"),
        ('B', r"$\left[-\dfrac12,\dfrac32\right]$"),
        ('C', r"$\left[0,\dfrac12\right]$"),
        ('D', r"$\left[0,\dfrac32\right]$"),
    ],
    'answer': 'B',
    'analysis': (
        r"三个点都在球面上 ⟹ 全部用 $\overrightarrow{OP}$、$\overrightarrow{OA}$、$\overrightarrow{OB}$ 表示，" "\n"
        r"三者模长都是 $1$，只剩 $\overrightarrow{OA}\cdot\overrightarrow{OB}$ 一个未知量，由 $AB=\sqrt3$ 定出。" "\n"
        r"展开后唯一可变的部分是 $\left(\overrightarrow{OA}+\overrightarrow{OB}\right)\cdot\overrightarrow{OP}$，其模长也可算出。"
    ),
    'solution': (
        r"由 $\left|\overrightarrow{OA}\right|=\left|\overrightarrow{OB}\right|=\left|\overrightarrow{OP}\right|=1$（半径），" "\n"
        r"$$\left|\overrightarrow{AB}\right|^2=\left|\overrightarrow{OB}-\overrightarrow{OA}\right|^2=\left|\overrightarrow{OA}\right|^2+\left|\overrightarrow{OB}\right|^2-2\overrightarrow{OA}\cdot\overrightarrow{OB}=2-2\overrightarrow{OA}\cdot\overrightarrow{OB}=3,$$" "\n"
        r"得 $\overrightarrow{OA}\cdot\overrightarrow{OB}=-\dfrac12$。于是" "\n"
        r"$$\left|\overrightarrow{OA}+\overrightarrow{OB}\right|^2=1+1+2\left(-\frac12\right)=1,\quad\text{即}\quad\left|\overrightarrow{OA}+\overrightarrow{OB}\right|=1.$$" "\n"
        r"展开所求式：" "\n"
        r"$$\overrightarrow{PA}\cdot\overrightarrow{PB}=\left(\overrightarrow{OA}-\overrightarrow{OP}\right)\cdot\left(\overrightarrow{OB}-\overrightarrow{OP}\right)$$" "\n"
        r"$$=\overrightarrow{OA}\cdot\overrightarrow{OB}-\left(\overrightarrow{OA}+\overrightarrow{OB}\right)\cdot\overrightarrow{OP}+\left|\overrightarrow{OP}\right|^2=-\frac12-\left(\overrightarrow{OA}+\overrightarrow{OB}\right)\cdot\overrightarrow{OP}+1$$" "\n"
        r"$$=\frac12-\left(\overrightarrow{OA}+\overrightarrow{OB}\right)\cdot\overrightarrow{OP}.$$" "\n"
        r"记 $\vec u=\overrightarrow{OA}+\overrightarrow{OB}$（$\left|\vec u\right|=1$），则 $\vec u\cdot\overrightarrow{OP}=\left|\vec u\right|\cdot\left|\overrightarrow{OP}\right|\cos\theta=\cos\theta$。" "\n"
        r"$P$ 在球面上任意取值，$\overrightarrow{OP}$ 可取遍所有方向的单位向量，故 $\cos\theta\in\left[-1,1\right]$，" "\n"
        r"（$\overrightarrow{OP}$ 与 $\vec u$ 同向时取 $1$，反向时取 $-1$，这两个方向都在球面上）。" "\n"
        r"因此 $\overrightarrow{PA}\cdot\overrightarrow{PB}\in\left[\dfrac12-1,\dfrac12+1\right]=\left[-\dfrac12,\dfrac32\right]$。" "\n"
        r"选 $\boxed{\text{B}}$。"
    ),
    'review': (
        r"① ⭐⭐ **球面上三点 ⟹ 全部用 $\overrightarrow{OP}$、$\overrightarrow{OA}$、$\overrightarrow{OB}$ 表示**：" "\n"
        r"   三者模长都是 $1$，展开后只剩 $\overrightarrow{OA}\cdot\overrightarrow{OB}$（由 $AB$ 定出）" "\n"
        r"   与 $\left(\overrightarrow{OA}+\overrightarrow{OB}\right)\cdot\overrightarrow{OP}$（由方向定出）两项。" "\n"
        r"② ⭐ **$\left|\overrightarrow{OA}+\overrightarrow{OB}\right|=1$ 是关键中间量**：" "\n"
        r"   由 $\overrightarrow{OA}\cdot\overrightarrow{OB}=-\dfrac12$ 得 $\left|\vec u\right|^2=2+2\left(-\dfrac12\right)=1$。" "\n"
        r"   若 $\left|\vec u\right|$ 算错，整个范围都会错。" "\n"
        r"③ ⚠ **端点能否取到**：$\overrightarrow{OP}=\pm\dfrac{\vec u}{\left|\vec u\right|}$ 都是单位向量，" "\n"
        r"   对应的点确实在球面上，故两端点都能取到，区间是闭的。" "\n"
        r"④ ⚠ **干扰项 A** 是把 $\overrightarrow{OA}\cdot\overrightarrow{OB}$ 的符号搞反（得 $+\dfrac12$）后" "\n"
        r"   再算 $\left|\vec u\right|=\sqrt3$ 的结果；C、D 则是漏掉了 $-\dfrac12$ 或把范围算成非负。" "\n"
        r"⑤ 数值复核：$\overrightarrow{OP}$ 与 $\vec u$ 同向时 $\dfrac12-1=-\dfrac12$ ✓，反向时 $\dfrac12+1=\dfrac32$ ✓" "\n"
        r"   构造验证：取 $\overrightarrow{OA}=\left(1,0,0\right)$、$\overrightarrow{OB}=\left(-\dfrac12,\dfrac{\sqrt3}2,0\right)$，" "\n"
        r"   则 $AB=\sqrt{\left(\dfrac32\right)^2+\left(\dfrac{\sqrt3}2\right)^2}=\sqrt{\dfrac94+\dfrac34}=\sqrt3$ ✓，$\vec u=\left(\dfrac12,\dfrac{\sqrt3}2,0\right)$、$\left|\vec u\right|=1$ ✓" "\n"
        r"**通法（球面上的数量积）**：" "\n"
        r"① 所有点用球心出发的向量表示，模长均为 $R$；" "\n"
        r"② $\overrightarrow{PA}\cdot\overrightarrow{PB}=\overrightarrow{OA}\cdot\overrightarrow{OB}-\left(\overrightarrow{OA}+\overrightarrow{OB}\right)\cdot\overrightarrow{OP}+R^2$；" "\n"
        r"③ $\overrightarrow{OA}\cdot\overrightarrow{OB}=R^2-\dfrac{AB^2}2$，$\left|\overrightarrow{OA}+\overrightarrow{OB}\right|=\sqrt{2R^2+2\overrightarrow{OA}\cdot\overrightarrow{OB}}$；" "\n"
        r"④ 只剩一个方向余弦在 $\left[-1,1\right]$ 内变化 ⟹ 范围即 $\left[\text{const}-M,\ \text{const}+M\right]$。"
    ),
    'difficulty': 0.70,
    'topics': ['M-T-239'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-239-V2',
}

QS = [
    T010_V1, T010_V2, T010_V3,
    T011_V1, T011_V2, T011_V3,
    T033_E1, T033_V2, T033_V3,
    T239_E1, T239_V1, T239_V2,
]
