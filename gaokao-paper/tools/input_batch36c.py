# -*- coding: utf-8 -*-
r"""第36批（三）：解析几何中的向量（4题）

来源：2024高中数学热点题型归纳完整解析版.pdf p208（PDF 页 207）

## 选题

`pick_batch.py --n 6 --topic M-T-242` → p208 一页 4 题。

## 四题验算

| 题 | 关键 | 答案 |
|---|---|---|
| E1 | $\vec{MA}\cdot\vec{BA}=\lvert\vec{MA}\rvert^2$（因 $\vec{MA}\cdot\vec{MB}=0$），转成 $\frac34x^2-2x+2$ | **C** $[\frac23,9]$ |
| V1 | $\vec{OA}\cdot\vec{OB}=4-r^2$，代入得 $\frac34r^2=\frac{15}2$ → $r=\sqrt{10}$ | **D** |
| V2 | $\lvert PM\rvert+\lvert QM\rvert=\frac52(\lvert MF_1\rvert+\lvert MF_2\rvert)=10$ | **A** |
| V3 | $N(\frac{x_0+y_0}2,\frac{x_0+y_0}2)$，$\lvert ON\rvert\cdot\lvert MN\rvert=\frac{\lvert x_0^2-y_0^2\rvert}2=\frac12$ | $\frac12$ |

## ⚠ 两处需说明

- **V2**：题干在「D 是椭圆 C 上」处截断；答案 10 的依据是 $\frac52\times4$（详解原文）。
- **V3**：题干的 $\lvert ON\rvert\cdot\lvert MN\rvert$ 被提取成 `ON ⋅ MN`（丢了绝对值）。
  若按**向量点积**理解，因 $ON\perp MN$ 结果恒为 $0$；答案 $\frac12$ 表明是**长度乘积**。
"""

T242_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知点 $M(1,0)$，$A,B$ 是椭圆 $\dfrac{x^{2}}4+y^{2}=1$ 上的动点，"
        r"且 $\vec{MA}\cdot\vec{MB}=0$，则 $\vec{MA}\cdot\vec{BA}$ 的取值范围是（　　）"
    ),
    'opts': [
        ('A', r"$\left[\dfrac23,1\right]$"),
        ('B', r"$[1,9]$"),
        ('C', r"$\left[\dfrac23,9\right]$"),
        ('D', r"$\left[\dfrac63,3\right]$"),
    ],
    'answer': 'C',
    'analysis': (
        r"由 $\vec{BA}=\vec{MA}-\vec{MB}$ 得 "
        r"$\vec{MA}\cdot\vec{BA}=\lvert\vec{MA}\rvert^{2}-\vec{MA}\cdot\vec{MB}"
        r"=\lvert\vec{MA}\rvert^{2}$，问题化为求 $\lvert MA\rvert^{2}$ 的范围。"
    ),
    'solution': (
        r"**第一步：化简所求式**" "\n"
        r"因 $\vec{BA}=\vec A-\vec B=(\vec A-\vec M)-(\vec B-\vec M)=\vec{MA}-\vec{MB}$，" "\n"
        r"$\vec{MA}\cdot\vec{BA}=\vec{MA}\cdot(\vec{MA}-\vec{MB})"
        r"=\lvert\vec{MA}\rvert^{2}-\vec{MA}\cdot\vec{MB}"
        r"=\lvert\vec{MA}\rvert^{2}$（由已知 $\vec{MA}\cdot\vec{MB}=0$）．" "\n"
        r"**第二步：表示为 $x$ 的函数**" "\n"
        r"设 $A(x,y)$ 在椭圆上，则 $y^{2}=1-\dfrac{x^{2}}4$，$x\in[-2,2]$．" "\n"
        r"$\lvert MA\rvert^{2}=(x-1)^{2}+y^{2}=(x-1)^{2}+1-\dfrac{x^{2}}4"
        r"=\dfrac34x^{2}-2x+2$．" "\n"
        r"**第三步：求二次函数最值**" "\n"
        r"开口向上，对称轴 $x=\dfrac{2}{2\times\frac34}=\dfrac43\in[-2,2]$：" "\n"
        r"最小值：$x=\dfrac43$ 时 $\dfrac34\cdot\dfrac{16}9-\dfrac83+2"
        r"=\dfrac43-\dfrac83+2=\dfrac23$；" "\n"
        r"最大值：比较端点，$x=-2$ 时 $3+4+2=9$；$x=2$ 时 $3-4+2=1$．故最大值为 $9$．" "\n"
        r"得 $\vec{MA}\cdot\vec{BA}\in\left[\dfrac23,9\right]$．选 C．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**原书无详解**，上述为我独立完成）。" "\n"
        r"**独立验算**：" "\n"
        r"① $\vec{BA}=\vec{MA}-\vec{MB}$ 的向量恒等式 ✓" "\n"
        r"② 最小值 $x=\frac43$：$y^2=1-\frac{16/9}4=1-\frac49=\frac59$，"
        r"$|MA|^2=(\frac43-1)^2+\frac59=\frac19+\frac59=\frac69=\frac23$ ✓" "\n"
        r"③ 最大值 $x=-2$：$y=0$，$A(-2,0)$，$|MA|^2=9$ ✓" "\n"
        r"**端点可行性检查**（必须存在 $B$ 使 $MA\perp MB$）：" "\n"
        r"· $x=-2$：$A(-2,0)$，$\vec{MA}=(-3,0)$；需 $\vec{MB}\perp(-3,0)$，"
        r"即 $B$ 的横坐标为 $1$。椭圆上 $x=1$ 时 $y=\pm\frac{\sqrt3}2$ ✓ **存在**" "\n"
        r"· $x=\frac43$：$A(\frac43,\pm\frac{\sqrt5}3)$，$\vec{MA}=(\frac13,\pm\frac{\sqrt5}3)$；"
        r"$\vec{MB}\perp\vec{MA}$ 的方向 $(\mp\frac{\sqrt5}3,\frac13)$ 斜率有限，"
        r"从 $M(1,0)$ 出发的该直线必与椭圆有第二交点 ✓" "\n"
        r"**答案 C 正确** ✓" "\n"
        r"**⭐ 解题关键**：看出 $\vec{MA}\cdot\vec{BA}=|MA|^2$ —— "
        r"利用 $\vec{MA}\cdot\vec{MB}=0$ 直接消掉一项，避免引入两个动点。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-242'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-242-E1',
}

T242_V1 = {
    'type': '选择',
    'stem_text': (
        r"在平面直角坐标系 $xOy$ 中，设直线 $y=-x+2$ 与圆 $x^{2}+y^{2}=r^{2}$（$r>0$）"
        r"交于 $A,B$ 两点，$O$ 为坐标原点，若圆上一点 $C$ 满足 "
        r"$\vec{OC}=\dfrac54\vec{OA}+\dfrac34\vec{OB}$，则 $r=$（　　）"
    ),
    'opts': [
        ('A', r"$2\sqrt2$"), ('B', r"$\sqrt5$"),
        ('C', r"$\sqrt3$"), ('D', r"$\sqrt{10}$"),
    ],
    'answer': 'D',
    'analysis': (
        r"由 $C$ 在圆上得 $\lvert\vec{OC}\rvert=r$；把 $\lvert\vec{OC}\rvert^{2}$ 展开，"
        r"关键是求出 $\vec{OA}\cdot\vec{OB}$ —— 用弦中点（垂足）分解最简洁。"
    ),
    'solution': (
        r"**第一步：展开 $\lvert\vec{OC}\rvert^{2}$**" "\n"
        r"$r^{2}=\lvert\vec{OC}\rvert^{2}"
        r"=\dfrac{25}{16}\lvert\vec{OA}\rvert^{2}+\dfrac9{16}\lvert\vec{OB}\rvert^{2}"
        r"+2\cdot\dfrac54\cdot\dfrac34\,\vec{OA}\cdot\vec{OB}$" "\n"
        r"$=\dfrac{25}{16}r^{2}+\dfrac9{16}r^{2}+\dfrac{15}8\vec{OA}\cdot\vec{OB}"
        r"=\dfrac{17}8r^{2}+\dfrac{15}8\vec{OA}\cdot\vec{OB}$．" "\n"
        r"**第二步：求 $\vec{OA}\cdot\vec{OB}$**" "\n"
        r"设 $H$ 为弦 $AB$ 的中点，则 $OH\perp AB$。直线为 $x+y-2=0$：" "\n"
        r"$\lvert OH\rvert=\dfrac{\lvert 0+0-2\rvert}{\sqrt2}=\sqrt2$，"
        r"$\lvert AH\rvert=\sqrt{r^{2}-\lvert OH\rvert^{2}}=\sqrt{r^{2}-2}$．" "\n"
        r"$\vec{OA}\cdot\vec{OB}=(\vec{OH}+\vec{HA})\cdot(\vec{OH}+\vec{HB})"
        r"=\lvert\vec{OH}\rvert^{2}+\vec{HA}\cdot\vec{HB}$" "\n"
        r"$=2-\lvert AH\rvert^{2}=2-(r^{2}-2)=4-r^{2}$（因 $\vec{HB}=-\vec{HA}$）．" "\n"
        r"**第三步：解方程**" "\n"
        r"$r^{2}=\dfrac{17}8r^{2}+\dfrac{15}8(4-r^{2})"
        r"=\dfrac{17}8r^{2}+\dfrac{15}2-\dfrac{15}8r^{2}"
        r"=\dfrac14r^{2}+\dfrac{15}2$" "\n"
        r"$\Rightarrow\dfrac34r^{2}=\dfrac{15}2\Rightarrow r^{2}=10\Rightarrow r=\sqrt{10}$．选 D．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**原书无详解**，上述为我独立完成）。" "\n"
        r"**独立验算**：" "\n"
        r"① 垂足 $H$：直线 $x+y-2=0$，$H$ 为 $(1,1)$（$x=y$，$2x=2$），$\lvert OH\rvert=\sqrt2$ ✓" "\n"
        r"② $r=\sqrt{10}$ 时：$\lvert AH\rvert=\sqrt{10-2}=2\sqrt2$；"
        r"$\vec{OA}\cdot\vec{OB}=4-10=-6$ ✓" "\n"
        r"③ 代回：$r^2\stackrel{?}{=}\frac{17}8\times10+\frac{15}8\times(-6)"
        r"=\frac{170}8-\frac{90}8=\frac{80}8=10$ ✓✓ **完全吻合**" "\n"
        r"④ **具体构造验证**：$r=\sqrt{10}$，$H(1,1)$，$\lvert AH\rvert=2\sqrt2$；"
        r"$AB$ 方向 $(1,-1)$，故 $A=H+\sqrt2\cdot\frac{(1,-1)}{\sqrt2}\cdot\ldots$ " "\n"
        r"取 $A=(1+2,1-2)=(3,-1)$：$3^2+1=10$ ✓ 在圆上；"
        r"$B=(1-2,1+2)=(-1,3)$：$1+9=10$ ✓ 在圆上；"
        r"都在 $x+y=2$ 上 ✓（$3-1=2$、$-1+3=2$）" "\n"
        r"$C=\frac54(3,-1)+\frac34(-1,3)=(\frac{15}4-\frac34,-\frac54+\frac94)=(3,1)$；"
        r"$3^2+1^2=10$ ✓ **C 确实在圆上** ✓✓" "\n"
        r"**答案 D 正确** ✓" "\n"
        r"**⭐ 通法**：圆上点的向量线性组合仍在圆上 ⟹ 用「弦中点分解」"
        r"$\vec{OA}\cdot\vec{OB}=\lvert OH\rvert^2-\lvert AH\rvert^2$ 最省事。"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-242'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-242-V1',
}

T242_V2 = {
    'type': '选择',
    'stem_text': (
        r"如图所示，已知椭圆 $C:\dfrac{x^{2}}4+y^{2}=1$ 的左、右焦点分别为 $F_{1},F_{2}$，"
        r"点 $M$ 在椭圆 $C$ 上且与焦点不重合，分别延长 $MF_{1}$、$MF_{2}$ 到 $P$、$Q$，"
        r"使得 $\vec{MF_{1}}=\dfrac23\vec{F_{1}P}$，$\vec{MF_{2}}=\dfrac23\vec{F_{2}Q}$，"
        r"则 $\lvert PM\rvert+\lvert QM\rvert=$（　　）"
    ),
    'opts': [('A', r"$10$"), ('B', r"$5$"),
             ('C', r"$6$"), ('D', r"$3$")],
    'answer': 'A',
    'analysis': (
        r"由 $\vec{MF_{1}}=\frac23\vec{F_{1}P}$ 得 $\vec{F_{1}P}=\frac32\vec{MF_{1}}$，"
        r"故 $\lvert MP\rvert=\lvert MF_{1}\rvert+\lvert F_{1}P\rvert=\frac52\lvert MF_{1}\rvert$；"
        r"同理 $\lvert MQ\rvert=\frac52\lvert MF_{2}\rvert$，再用椭圆定义。"
    ),
    'solution': (
        r"**第一步：由向量比例定长度比**" "\n"
        r"$\vec{MF_{1}}=\dfrac23\vec{F_{1}P}$ 说明 $\vec{MF_{1}}$ 与 $\vec{F_{1}P}$ "
        r"**同向**，即 $M,F_{1},P$ 依次共线．" "\n"
        r"$\lvert F_{1}P\rvert=\dfrac32\lvert MF_{1}\rvert$，故" "\n"
        r"$\lvert MP\rvert=\lvert MF_{1}\rvert+\lvert F_{1}P\rvert"
        r"=\left(1+\dfrac32\right)\lvert MF_{1}\rvert=\dfrac52\lvert MF_{1}\rvert$．" "\n"
        r"同理 $\lvert MQ\rvert=\dfrac52\lvert MF_{2}\rvert$．" "\n"
        r"**第二步：用椭圆定义**" "\n"
        r"椭圆 $\dfrac{x^{2}}4+y^{2}=1$ 中 $a=2$，故 "
        r"$\lvert MF_{1}\rvert+\lvert MF_{2}\rvert=2a=4$．" "\n"
        r"**第三步**：" "\n"
        r"$\lvert PM\rvert+\lvert QM\rvert"
        r"=\dfrac52\left(\lvert MF_{1}\rvert+\lvert MF_{2}\rvert\right)"
        r"=\dfrac52\times4=10$．选 A．"
    ),
    'review': (
        r"★ 由详解「根据椭圆的定义和比例，有 "
        r"$\lvert PM\rvert+\lvert QM\rvert=\frac52(\lvert DF_{1}\rvert+\lvert DF_{2}\rvert)"
        r"=\frac52\times4=10$」还原。" "\n"
        r"**⚠ 题干有截断（如实标注）**：原文在「D 是椭圆 $C$ 上」处断开，"
        r"$\lvert PN\rvert+\lvert QN\rvert$ 中的 $N$（或 $D$）指向不明。" "\n"
        r"**还原依据**：比例系数 $\frac52$ 恰为 $1+\frac32$（由 $\frac23$ 取倒数得到），"
        r"且 $4=2a$ 是椭圆定义 —— 唯一自洽的解读是求 "
        r"$\lvert PM\rvert+\lvert QM\rvert$（即所涉点就是 $M$）。" "\n"
        r"**独立验算**：" "\n"
        r"① $\vec{MF_1}=\frac23\vec{F_1P}$ → $\lvert F_1P\rvert=\frac32\lvert MF_1\rvert$ ✓" "\n"
        r"② $M,F_1,P$ 共线同向 → $\lvert MP\rvert=\lvert MF_1\rvert+\lvert F_1P\rvert$ ✓" "\n"
        r"③ $\lvert MP\rvert=\frac52\lvert MF_1\rvert$，$\lvert MQ\rvert=\frac52\lvert MF_2\rvert$ ✓" "\n"
        r"④ $\frac52\times4=10$ ✓ **答案 A 正确**" "\n"
        r"**数值抽查**：取 $M(0,1)$（在椭圆上 ✓），$F_1(-\sqrt3,0)$、$F_2(\sqrt3,0)$；" "\n"
        r"$\lvert MF_1\rvert=\sqrt{3+1}=2$、$\lvert MF_2\rvert=2$（和为 $4$ ✓）；" "\n"
        r"$\lvert MP\rvert=\frac52\times2=5$、$\lvert MQ\rvert=5$，和为 $10$ ✓" "\n"
        r"（注：$M(0,1)$ 时 $\lvert MF_1\rvert=\lvert MF_2\rvert=2=a$，"
        r"这是短轴端点的特殊情形，但结论对任意 $M$ 成立。）"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-242'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-242-V2',
}

T242_V3 = {
    'type': '填空',
    'stem_text': (
        r"已知点 $O$ 为坐标原点，点 $M$ 在双曲线 $c:x^{2}-y^{2}=1$ 上，"
        r"过点 $M$ 作双曲线 $c$ 的某一条渐近线的垂线，垂足为 $N$，"
        r"则 $\lvert ON\rvert\cdot\lvert MN\rvert$ 的值为 ____ ．"
    ),
    'opts': [],
    'answer': r"$\dfrac12$",
    'analysis': (
        r"取渐近线 $y=x$，投影得 $N\!\left(\frac{x_{0}+y_{0}}2,\frac{x_{0}+y_{0}}2\right)$；"
        r"分别求两段长度后相乘，利用 $x_{0}^{2}-y_{0}^{2}=1$ 即得定值。"
    ),
    'solution': (
        r"**第一步：设点与渐近线**" "\n"
        r"设 $M(x_{0},y_{0})$ 在双曲线上，即 $x_{0}^{2}-y_{0}^{2}=1$．"
        r"渐近线为 $y=\pm x$，取 $y=x$（由对称性，取 $y=-x$ 结果相同）．" "\n"
        r"**第二步：求垂足 $N$**" "\n"
        r"$M$ 到直线 $y=x$ 的投影：" "\n"
        r"$N\!\left(\dfrac{x_{0}+y_{0}}2,\ \dfrac{x_{0}+y_{0}}2\right)$．" "\n"
        r"**第三步：求两段长度**" "\n"
        r"$\lvert ON\rvert=\sqrt{2}\cdot\dfrac{\lvert x_{0}+y_{0}\rvert}2"
        r"=\dfrac{\lvert x_{0}+y_{0}\rvert}{\sqrt2}$；" "\n"
        r"$\vec{MN}=N-M=\left(\dfrac{y_{0}-x_{0}}2,\ \dfrac{x_{0}-y_{0}}2\right)$，" "\n"
        r"$\lvert MN\rvert=\sqrt{\dfrac{(x_{0}-y_{0})^{2}}4+\dfrac{(x_{0}-y_{0})^{2}}4}"
        r"=\dfrac{\lvert x_{0}-y_{0}\rvert}{\sqrt2}$．" "\n"
        r"**第四步：相乘**" "\n"
        r"$\lvert ON\rvert\cdot\lvert MN\rvert"
        r"=\dfrac{\lvert x_{0}+y_{0}\rvert\cdot\lvert x_{0}-y_{0}\rvert}2"
        r"=\dfrac{\lvert x_{0}^{2}-y_{0}^{2}\rvert}2=\dfrac12$．" "\n"
        r"故答案为 $\dfrac12$．"
    ),
    'review': (
        r"★ 由详解「…从而 $\lvert ON\rvert=\frac{\lvert x_{0}+y_{0}\rvert}{\sqrt2}$，"
        r"$\lvert MN\rvert=\frac{\lvert x_{0}-y_{0}\rvert}{\sqrt2}$，"
        r"所以 $\lvert ON\rvert\cdot\lvert MN\rvert"
        r"=\frac{\lvert x_{0}+y_{0}\rvert}{\sqrt2}\cdot\frac{\lvert x_{0}-y_{0}\rvert}{\sqrt2}"
        r"=\frac{\lvert x_{0}^{2}-y_{0}^{2}\rvert}2=\frac12$」还原。" "\n"
        r"**⚠ 题干绝对值符号丢失（关键）**：提取成 `ON ⋅ MN`，"
        r"若按**向量点积**理解，因 $ON$ 在渐近线上、$MN\perp$ 渐近线，"
        r"有 $ON\perp MN$ ⟹ $\vec{ON}\cdot\vec{MN}=0$ 恒成立 —— "
        r"这与答案 $\frac12$ 矛盾。" "\n"
        r"**故题干应为长度乘积 $\lvert ON\rvert\cdot\lvert MN\rvert$**，按此录入。" "\n"
        r"**独立验算**：" "\n"
        r"取 $M(\sqrt2,1)$：$x_0^2-y_0^2=2-1=1$ ✓ 在双曲线上" "\n"
        r"$N(\frac{\sqrt2+1}2,\frac{\sqrt2+1}2)=(1.2071,1.2071)$" "\n"
        r"$\lvert ON\rvert=\sqrt{2\times1.2071^2}=1.7071$；"
        r"$\lvert MN\rvert=\sqrt{(\sqrt2-1.2071)^2+(1-1.2071)^2}"
        r"=\sqrt{0.2071^2+0.2071^2}=0.2929$" "\n"
        r"乘积 $=1.7071\times0.2929=0.5000$ ✓✓ **恰为 $\frac12$**" "\n"
        r"**另一渐近线验证**（取 $y=-x$）：$N(\frac{x_0-y_0}2,\frac{y_0-x_0}2)$，" "\n"
        r"$\lvert ON\rvert=\frac{\lvert x_0-y_0\rvert}{\sqrt2}$、"
        r"$\lvert MN\rvert=\frac{\lvert x_0+y_0\rvert}{\sqrt2}$；乘积同为 $\frac12$ ✓ **结论一致**" "\n"
        r"**答案 $\frac12$ 正确** ✓" "\n"
        r"**⭐ 结论记忆**：双曲线 $x^2-y^2=a^2$ 上任意点到渐近线的距离"
        r"与该垂足到原点距离之积为定值 $\frac{a^2}2$（本题 $a=1$）。"
    ),
    'difficulty': 0.87,
    'topics': ['M-T-242'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-242-V3',
}

QS = [T242_E1, T242_V1, T242_V2, T242_V3]
