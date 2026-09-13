# -*- coding: utf-8 -*-
r"""第 104 批：圆锥曲线离心率与几何（12 题）

    python3 tools/run_batch.py 104

## 选题依据

按「详解完整 + 同题型聚堆 + 无图依赖」从 p303 / p306 / p307 / p309 / p351 / p355 / p357
筛出解析几何区 12 道选择填空，全部为离心率与几何结构题：

| 题型 | 题号 | 核心方法 |
|---|---|---|
| M-T-327 | V2 | 抛物线定义 ⟹ 梯形中位线 ⟹ $\sqrt{a^2+b^2}\ge\frac{\sqrt2}2(a+b)$ |
| M-T-330 | V2 | 直角三角形分解焦半径 ⟹ 二次方程有根条件 |
| M-T-334 | V2 | 切线长 $=b$ + 相似比 $2$ ⟹ 解 $\mathrm{Rt}\triangle$ ⟹ 渐近线 |
| M-T-335 | V2 | 抛物线准线恰过 $F_1$ ⟹ 两角余弦相等 |
| M-T-373 | V3 | 直径所对圆周角为直角 ⟹ $\cos\theta=\frac bc$ |
| M-T-365 | E1 | 对角线相等且互相平分 ⟹ 矩形 ⟹ 勾股 |
| M-T-333 | V3、V2 | 共焦点半角公式；柯西取最值 |
| M-T-370 | E1、V2 | $\frac1m=\sin\alpha$ ⟹ 相切；导数求切线 ⟹ 定位焦点 |
| M-T-374 | E1 | 内心分角平分线的比例式 |
| M-T-376 | V1 | 反射 ⟹ 过镜像点；「只有一条」的两种情形 |

## 本批最重要的六条通法

### 一、凡「分母是两段之差、分子是全长」的分式，比值下界都走 $\sqrt{a^2+b^2}\ge\frac{\sqrt2}2(a+b)$

M-T-327-V2 的 $\frac{\lvert AB\rvert}{\lvert MN\rvert}=\frac{2\sqrt{a^2+b^2}}{a+b}\ge\sqrt2$。
⚠ 本册教辅此处把 $\frac{\sqrt2}2$ 印成 $\frac12$，答案印成 $2$（实为 $\sqrt2$）——**根号丢失最高频**。

### 二、切线长与相似比 $2$（M-T-334-V2）

过 $F_1$ 作圆 $x^2+y^2=a^2$ 的切线 ⟹ $\lvert OA\rvert=a$、$\lvert F_1A\rvert=\sqrt{c^2-a^2}=b$。
又 $\triangle OAF_1\backsim\triangle F_2BF_1$（共角 + 直角），相似比 $=\frac{\lvert F_1F_2\rvert}{\lvert OF_1\rvert}=2$，
故 $\lvert F_2B\rvert=2a$、$\lvert F_1B\rvert=2b$。之后全是解直角三角形。

### 三、$MN=F_1F_2$ ⟹ 矩形（M-T-365-E1）

两条对角线相等且互相平分的平行四边形是矩形 ⟹
$\lvert MF_1\rvert^2+\lvert MF_2\rvert^2=4c^2$，配 $\lvert MF_1\rvert+\lvert MF_2\rvert=2a$ 得
$x^2-2ax+2b^2=0$。⚠ **取较小根**（$M$ 在第一象限，$x=\lvert MF_2\rvert<a$）。

### 四、共焦点的半角公式（M-T-333 全组）

记 $2\theta=\angle F_1PF_2$，$m=a_1+a_2$、$n=a_1-a_2$，余弦定理给
$\frac{\sin^2\theta}{e_1^2}+\frac{\cos^2\theta}{e_2^2}=1$。
- $2\theta=\frac\pi3$（$\theta=\frac\pi6$）⟹ $a_1^2+3a_2^2=4c^2$
- $2\theta=\frac{2\pi}3$（$\theta=\frac\pi3$）⟹ $3a_1^2+a_2^2=4c^2$

⚠ **系数 $3$ 落在哪一边，取决于 $\cos2\theta$ 的符号**：$\cos\frac{2\pi}3=-\frac12$ 使交叉项变 $+mn$。

### 五、内心分角平分线：$\frac{\lvert EG\rvert}{\lvert GA\rvert}=\frac{\lvert ED\rvert+\lvert EB\rvert}{\lvert BD\rvert}$（M-T-374-E1）

等腰三角形时化简为 $\frac{\lvert ED\rvert}{\lvert DA\rvert}$。
⚠ $\overrightarrow{DA}=\overrightarrow{AB}$ 是向量等式（$A$ 为 $BD$ 中点），不是长度相等。

### 六、反射问题 ⟹ 过镜像点（M-T-376-V1）

$y$ 轴反射把过 $P$ 的直线族变成过 $P'(-2,-2)$ 的直线族。
「只有一条相切」要分两种情形讨论：**判别式为零**（$P'$ 在椭圆上，被「外一点」排除）
与**二次项系数为零**（$a^2=4$，方程退化成一次）。
⚠ 问的是**切线的斜率** $-k$，不是入射斜率 $k$ —— 两者互为相反数，恰是选项 A 与 D。
"""

T327_V2 = {
    'type': '填空',
    'stem_text': (
        r"已知抛物线 $C:y^{2}=2px$（$p>0$）的焦点为 $F$，直线 $l$ 与 $C$ 交于 $A,B$ 两点，" "\n"
        r"$AF\perp BF$，线段 $AB$ 的中点为 $M$，过点 $M$ 作抛物线 $C$ 的准线的垂线，垂足为 $N$，" "\n"
        r"则 $\dfrac{\lvert AB\rvert}{\lvert MN\rvert}$ 的最小值为____．"
    ),
    'opts': [],
    'answer': r"$\sqrt2$",
    'analysis': (
        r"设 $\lvert AF\rvert=a$、$\lvert BF\rvert=b$：由抛物线定义与梯形中位线得 $\lvert MN\rvert=\dfrac{a+b}2$，" "\n"
        r"由 $AF\perp BF$ 得 $\lvert AB\rvert=\sqrt{a^{2}+b^{2}}$，于是比值 $=\dfrac{2\sqrt{a^{2}+b^{2}}}{a+b}\ge\sqrt2$．"
    ),
    'solution': (
        r"设 $\lvert AF\rvert=a$，$\lvert BF\rvert=b$．" "\n"
        r"分别过 $A,B$ 作准线的垂线，垂足为 $A_1,B_1$，由抛物线的定义" "\n"
        r"$\lvert AA_1\rvert=\lvert AF\rvert=a$，$\lvert BB_1\rvert=\lvert BF\rvert=b$．" "\n"
        r"因 $AA_1\parallel BB_1\parallel MN$，且 $M$ 是 $AB$ 的中点，故 $MN$ 是梯形 $AA_1B_1B$ 的中位线，" "\n"
        r"$\lvert MN\rvert=\dfrac{a+b}2$．" "\n"
        r"又由 $AF\perp BF$，在 $\triangle AFB$ 中" "\n"
        r"$\lvert AB\rvert=\sqrt{a^{2}+b^{2}}$．" "\n"
        r"于是" "\n"
        r"$\dfrac{\lvert AB\rvert}{\lvert MN\rvert}=\dfrac{\sqrt{a^{2}+b^{2}}}{\frac{a+b}2}=\dfrac{2\sqrt{a^{2}+b^{2}}}{a+b}$．" "\n"
        r"由 $\left(a-b\right)^{2}\ge0$ 得 $a^{2}+b^{2}\ge\dfrac{\left(a+b\right)^{2}}2$，即 $\sqrt{a^{2}+b^{2}}\ge\dfrac{\sqrt2}2\left(a+b\right)$，" "\n"
        r"故 $\dfrac{2\sqrt{a^{2}+b^{2}}}{a+b}\ge\sqrt2$，当且仅当 $a=b$ 时取等号．" "\n"
        r"所以最小值为 $\sqrt2$．"
    ),
    'review': (
        r"① ⚠ **原书答案处印刷为「最小值为 $2$」，实为 $\sqrt2$**．判据：详解中「$\sqrt{a^2+b^2}\ge\frac12(a+b)$」" "\n"
        r"　 漏了根号，正确是 $\sqrt{a^{2}+b^{2}}\ge\frac{\sqrt2}2(a+b)$（由 $(a-b)^2\ge0$ 直接展开即得）．" "\n"
        r"② 数值复核：取 $a=b$ 时比值 $=\sqrt2=1.414214$；取 $a=1,b=3$ 时 $=\frac{2\sqrt{10}}4=1.581139>\sqrt2$ ✓．" "\n"
        r"③ $a=b$ 可取到：取 $p=2$（$y^2=4x$，$F(1,0)$），令 $A(t^2,2t)$、$B(t^2,-2t)$，则" "\n"
        r"　 $\lvert AF\rvert=\lvert BF\rvert$；由 $(A-F)\cdot(B-F)=(t^2-1)^2-4t^2=0$ 得 $t=1+\sqrt2$，$A(5.828,4.828)$、$B(5.828,-4.828)$ ✓．" "\n"
        r"④ 关键在认出 $MN$ 是**梯形中位线**——$AA_1,BB_1,MN$ 三者平行且 $M$ 为 $AB$ 中点．" "\n"
        r"　 ⚠ 本题 $l$ **不过焦点**，$\triangle AFB$ 的直角在 $F$，不是退化情形．"
    ),
    'difficulty': 0.80,
    'topics': ['M-T-327'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-327-V2',
}

T330_V2 = {
    'type': '填空',
    'stem_text': (
        r"已知双曲线 $\Gamma:\dfrac{x^{2}}{a^{2}}-\dfrac{y^{2}}{b^{2}}=1$（$a>0,b>0$）的左、右焦点分别为 $F_1,F_2$，" "\n"
        r"$P$ 是 $\Gamma$ 右支上的一点，$Q$ 是 $PF_2$ 的延长线上一点，且 $QF_1\perp QF_2$，" "\n"
        r"若 $\sin\angle PF_1Q=\dfrac35$，则 $\Gamma$ 的离心率的取值范围是____．"
    ),
    'opts': [],
    'answer': r"$\left(1,2\right)$",
    'analysis': (
        r"在 $\mathrm{Rt}\triangle PQF_1$ 中用 $\frac35$ 分解出 $\lvert PQ\rvert=\frac35m$、$\lvert QF_1\rvert=\frac45m$，" "\n"
        r"再在 $\mathrm{Rt}\triangle F_1QF_2$ 中列勾股得 $m$ 的二次方程，最后用「方程在区间内有根」定 $e$．"
    ),
    'solution': (
        r"设 $\lvert PF_1\rvert=m$（$m>2a$），则 $\lvert PF_2\rvert=m-2a$（$P$ 在右支）．" "\n"
        r"因 $Q$ 在 $PF_2$ 的延长线上，$P,Q,F_2$ 共线，又 $QF_1\perp QF_2$，故 $\angle PQF_1=90^\circ$．" "\n"
        r"在 $\mathrm{Rt}\triangle PQF_1$ 中，$\sin\angle PF_1Q=\dfrac{\lvert PQ\rvert}{\lvert PF_1\rvert}=\dfrac35$，于是" "\n"
        r"$\lvert PQ\rvert=\dfrac35m$，$\lvert QF_1\rvert=\sqrt{m^{2}-\left(\frac35m\right)^{2}}=\dfrac45m$．" "\n"
        r"又 $Q$ 在 $F_2$ 之外，故" "\n"
        r"$\lvert QF_2\rvert=\lvert PQ\rvert-\lvert PF_2\rvert=\dfrac35m-\left(m-2a\right)=2a-\dfrac25m$．" "\n"
        r"在 $\mathrm{Rt}\triangle F_1QF_2$ 中，$\lvert F_1F_2\rvert=2c$，由勾股定理" "\n"
        r"$4c^{2}=\left(\dfrac45m\right)^{2}+\left(2a-\dfrac25m\right)^{2}$" "\n"
        r"$\Longrightarrow \dfrac{16}{25}m^{2}+4a^{2}-\dfrac85am+\dfrac4{25}m^{2}=4c^{2}$" "\n"
        r"$\Longrightarrow m^{2}-2ma+5a^{2}-5c^{2}=0$．　①" "\n"
        r"$m$ 还要满足两条几何约束：" "\n"
        r"（i）$\lvert QF_2\rvert>0\Longrightarrow m<5a$；" "\n"
        r"（ii）$\triangle F_1QF_2$ 中 $\lvert QF_1\rvert+\lvert QF_2\rvert>\lvert F_1F_2\rvert$，即 $\dfrac45m+2a-\dfrac25m>2c\Longrightarrow m>5\left(c-a\right)$．" "\n"
        r"设 $f\left(m\right)=m^{2}-2ma+5a^{2}-5c^{2}$，开口向上、对称轴 $m=a$；" "\n"
        r"而区间 $\left(5(c-a),5a\right)$ 在 $a$ 的右侧（$c>a$），故 $f$ 在其上递增，" "\n"
        r"① 在该区间内有根 $\iff f\bigl(5(c-a)\bigr)<0<f\left(5a\right)$．" "\n"
        r"$f\bigl(5(c-a)\bigr)=25\left(c-a\right)^{2}-10a\left(c-a\right)+5a^{2}-5c^{2}=20\left(c-a\right)\left(c-2a\right)<0$" "\n"
        r"$\Longrightarrow a<c<2a$；" "\n"
        r"$f\left(5a\right)=25a^{2}-10a^{2}+5a^{2}-5c^{2}=5\left(4a^{2}-c^{2}\right)>0\Longrightarrow c<2a$（与上一致）．" "\n"
        r"综上 $a<c<2a$，即 $1<e<2$，故 $e\in\left(1,2\right)$．"
    ),
    'review': (
        r"① 原书详解只用 $f\bigl(5(c-a)\bigr)<0$ 一步给出 $e<2$，配 $e>1$ 得 $\left(1,2\right)$；" "\n"
        r"　 我补上了 $f(5a)>0$ 与区间非空（$5(c-a)<5a\iff c<2a$）的检验，三者都等价于 $c<2a$，结论一致．" "\n"
        r"② 数值复核（$a=1$）：$e=1.5$ 时 $m=3.6926\in(2.5,5)$ ✓；$e=1.99$ 时 $m=4.9750\in(4.95,5)$ ✓；" "\n"
        r"　 $e=2$ 时 $m=5$ 使 $\lvert QF_2\rvert=0$（退化），无解 ✓ —— 右端开．" "\n"
        r"③ ⚠ 易错点：$Q$ 在 $PF_2$ 的**延长线**上（$P$-$F_2$-$Q$ 顺序），故 $\lvert QF_2\rvert=\lvert PQ\rvert-\lvert PF_2\rvert$ 是**相减**，" "\n"
        r"　 若按相加会得到 $\frac65m+2a$，后面完全走不通．" "\n"
        r"④ 突破口是「两个直角三角形共用斜边 $PF_1=m$」：先用 $\sin$ 分解 $PQ$ 与 $QF_1$，再用勾股接上 $2c$．"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-330'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-330-V2',
}

T334_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知双曲线 $C:\dfrac{x^{2}}{a^{2}}-\dfrac{y^{2}}{b^{2}}=1$（$a>0,b>0$）的左、右焦点分别为 $F_1,F_2$，" "\n"
        r"过 $F_1$ 作圆 $x^{2}+y^{2}=a^{2}$ 的切线，交双曲线右支于点 $M$，若 $\angle F_1MF_2=60^\circ$，" "\n"
        r"则双曲线的渐近线方程为（　　）"
    ),
    'opts': [
        ('A', r"$y=\pm\left(3+\sqrt3\right)x$"),
        ('B', r"$y=\pm2x$"),
        ('C', r"$y=\pm\dfrac{3+\sqrt3}{3}x$"),
        ('D', r"$y=\pm\left(1+\sqrt3\right)x$"),
    ],
    'answer': 'C',
    'analysis': (
        r"切线长 $\lvert F_1A\rvert=b$；由 $\triangle OAF_1\backsim\triangle F_2BF_1$（相似比 $2$）得" "\n"
        r"$\lvert F_2B\rvert=2a$、$\lvert F_1B\rvert=2b$，再在 $\mathrm{Rt}\triangle BMF_2$ 中用 $60^\circ$ 解出 $\lvert BM\rvert$、$\lvert F_2M\rvert$，" "\n"
        r"最后由定义 $\lvert MF_1\rvert-\lvert MF_2\rvert=2a$ 定出 $\dfrac ba$．"
    ),
    'solution': (
        r"设切点为 $A$，则 $OA\perp F_1M$，且 $\lvert OA\rvert=a$（半径）、$\lvert OF_1\rvert=c$，于是" "\n"
        r"$\lvert F_1A\rvert=\sqrt{c^{2}-a^{2}}=b$．" "\n"
        r"作 $F_2B\perp F_1M$ 于 $B$．在 $\triangle OAF_1$ 与 $\triangle F_2BF_1$ 中，" "\n"
        r"$\angle AF_1O=\angle BF_1F_2$（同一个角），且各有一个直角，故两三角形相似；" "\n"
        r"相似比 $=\dfrac{\lvert F_1F_2\rvert}{\lvert OF_1\rvert}=\dfrac{2c}c=2$，于是" "\n"
        r"$\lvert F_2B\rvert=2\lvert OA\rvert=2a$，$\lvert F_1B\rvert=2\lvert F_1A\rvert=2b$．" "\n"
        r"在 $\mathrm{Rt}\triangle BMF_2$ 中，$\angle BMF_2=\angle F_1MF_2=60^\circ$，故" "\n"
        r"$\lvert BM\rvert=\dfrac{\lvert F_2B\rvert}{\tan60^\circ}=\dfrac{2a}{\sqrt3}=\dfrac{2\sqrt3}3a$，" "\n"
        r"$\lvert F_2M\rvert=\dfrac{\lvert F_2B\rvert}{\sin60^\circ}=\dfrac{2a}{\frac{\sqrt3}2}=\dfrac{4\sqrt3}3a$．" "\n"
        r"点 $M$ 在右支上，由双曲线的定义 $\lvert MF_1\rvert-\lvert MF_2\rvert=2a$，而 $\lvert MF_1\rvert=\lvert F_1B\rvert+\lvert BM\rvert$，故" "\n"
        r"$\left(2b+\dfrac{2\sqrt3}3a\right)-\dfrac{4\sqrt3}3a=2a$" "\n"
        r"$\Longrightarrow 2b-\dfrac{2\sqrt3}3a=2a\Longrightarrow b=a+\dfrac{\sqrt3}3a=\dfrac{3+\sqrt3}3a$．" "\n"
        r"于是 $\dfrac ba=\dfrac{3+\sqrt3}3$，渐近线方程为 $y=\pm\dfrac{3+\sqrt3}3x$，故选 C．"
    ),
    'review': (
        r"① 题眼是**相似比 $2$**：$O$ 是 $F_1F_2$ 的中点，故 $F_2$ 到切线 $F_1M$ 的距离是 $O$ 到该直线距离的 $2$ 倍．" "\n"
        r"　 这一步想通后，其余全是解直角三角形．" "\n"
        r"② 数值复核：$a=1$、$b=\frac{3+\sqrt3}3=1.577350$ 时，$c=1.868$，切线斜率 $\frac ab=0.633975$，" "\n"
        r"　 解得 $M$ 后算得 $\angle F_1MF_2=60.000^\circ$ ✓．" "\n"
        r"　 对照：$b=2$ 时该角为 $90.000^\circ$、$b=1+\sqrt3=2.732$ 时为 $120.000^\circ$ ——" "\n"
        r"　 **选项 B、D 正是另外两个特殊角对应的 $\frac ba$**，命题人按此设置干扰项．" "\n"
        r"③ ⚠ $\lvert F_1B\rvert=2b$ 是沿直线的**线段长**，不是 $F_1$ 到直线的距离（$F_1$ 就在直线上，距离为 $0$）；" "\n"
        r"　 $\lvert F_1A\rvert=b$ 才是切线长（由 $\mathrm{Rt}\triangle OAF_1$ 的勾股）．两者别混．" "\n"
        r"④ 选项原文提取为「$3+3$」「$3+3\ 3$」等（根号丢失），按四个选项都是「$3\pm\sqrt3$ 的有理组合」还原．"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-334'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-334-V2',
}

T335_V2 = {
    'type': '填空',
    'stem_text': (
        r"已知双曲线 $C_1:\dfrac{x^{2}}{a^{2}}-\dfrac{y^{2}}{b^{2}}=1$（$a>0,b>0$）的左、右焦点分别为 $F_1,F_2$，" "\n"
        r"其中 $F_2$ 也是抛物线 $C_2:y^{2}=2px$（$p>0$）的焦点，$C_1$ 与 $C_2$ 在第一象限的公共点为 $P$，" "\n"
        r"若直线 $PF_1$ 的斜率为 $\dfrac34$，则双曲线的离心率 $e$（$e>2$）为____．"
    ),
    'opts': [],
    'answer': r"$4+\sqrt7$",
    'analysis': (
        r"$\frac p2=c\Longrightarrow$ 抛物线 $y^2=4cx$，其准线 $x=-c$ **恰过左焦点 $F_1$**；" "\n"
        r"于是 $\lvert PM\rvert$ 与 $\lvert PF_1\rvert$ 共用水平投影 $x_0+c$，两个角的余弦相等，一步得 $\lvert PF_1\rvert=\frac54(x_0+c)$．"
    ),
    'solution': (
        r"因 $F_2\left(c,0\right)$ 是抛物线 $y^{2}=2px$ 的焦点，故 $\dfrac p2=c$，$p=2c$，" "\n"
        r"抛物线方程为 $y^{2}=4cx$，准线为 $x=-c$（**恰好过左焦点 $F_1(-c,0)$**）．" "\n"
        r"设 $P\left(x_0,y_0\right)$（$x_0>0,y_0>0$）．过 $P$ 作准线的垂线，垂足 $M\left(-c,y_0\right)$，则" "\n"
        r"$\lvert PM\rvert=x_0+c$．" "\n"
        r"由抛物线的定义 $\lvert PF_2\rvert=\lvert PM\rvert=x_0+c$．" "\n"
        r"又 $PM\parallel F_1F_2$（都水平），故" "\n"
        r"$\cos\angle MPF_1=\dfrac{x_0+c}{\lvert PF_1\rvert}=\cos\angle PF_1F_2$．" "\n"
        r"由 $k_{PF_1}=\dfrac34$ 得 $\tan\angle PF_1F_2=\dfrac34$，故 $\cos\angle PF_1F_2=\dfrac45$，于是" "\n"
        r"$\lvert PF_1\rvert=\dfrac54\left(x_0+c\right)$．" "\n"
        r"$P$ 在右支上，由双曲线的定义 $\lvert PF_1\rvert-\lvert PF_2\rvert=2a$：" "\n"
        r"$\dfrac54\left(x_0+c\right)-\left(x_0+c\right)=2a\Longrightarrow x_0+c=8a$，" "\n"
        r"即 $\lvert PF_2\rvert=8a$，$\lvert PF_1\rvert=10a$．" "\n"
        r"在 $\triangle PF_1F_2$ 中，$\lvert F_1F_2\rvert=2c$，$\cos\angle PF_1F_2=\dfrac45$，由余弦定理" "\n"
        r"$\lvert PF_2\rvert^{2}=\lvert PF_1\rvert^{2}+\lvert F_1F_2\rvert^{2}-2\lvert PF_1\rvert\lvert F_1F_2\rvert\cos\angle PF_1F_2$" "\n"
        r"$\left(8a\right)^{2}=\left(10a\right)^{2}+\left(2c\right)^{2}-2\cdot10a\cdot2c\cdot\dfrac45$" "\n"
        r"$\Longrightarrow 64a^{2}=100a^{2}+4c^{2}-32ac\Longrightarrow c^{2}-8ac+9a^{2}=0$" "\n"
        r"$\Longrightarrow e^{2}-8e+9=0\Longrightarrow e=4\pm\sqrt7$．" "\n"
        r"由 $e>2$ 得 $e=4+\sqrt7$．"
    ),
    'review': (
        r"① ⚠⚠ **原书答案 $4+2\sqrt2$ 有误，正确为 $4+\sqrt7$**．" "\n"
        r"　 原书详解末行写「$c^{2}+8ac+8a^{2}=0\Rightarrow e^{2}-8e+8=0$」：左边三项同号，不可能等于 $0$；" "\n"
        r"　 由余弦定理严格展开（见详解）得 $c^{2}-8ac+9a^{2}=0$，即 $e^{2}-8e+9=0$，$e=4\pm\sqrt7$．" "\n"
        r"② 数值复核（$a=1$）：取 $c=4+\sqrt7=6.645751$，由「斜率 $\frac34$」与「在抛物线上」解得 $x_0=1.354249$、$y_0=6$，" "\n"
        r"　 逐条检验：$\frac{y_0}{x_0+c}=\frac68=0.75$ ✓；$y_0^{2}=36=4cx_0=4\times6.645751\times1.354249$ ✓；" "\n"
        r"　 $\frac{x_0^{2}}{1}-\frac{y_0^{2}}{c^{2}-1}=0.999998\approx1$ ✓．" "\n"
        r"　 改取 $c=4+2\sqrt2=6.828427$，第三式 $=1.1032\ne1$，**不成立**．" "\n"
        r"③ 全解扫描（$a=1$，$c$ 从 $2$ 扫到 $30$，两个分支都查）只有 $c=4+\sqrt7$ 一个解，另一分支无零点．" "\n"
        r"④ **题眼**：抛物线的准线 $x=-c$ 恰好过左焦点 $F_1$（因 $F_2$ 是公共焦点），" "\n"
        r"　 于是 $\lvert PM\rvert$ 与 $\lvert PF_1\rvert$ 的水平投影都是 $x_0+c$，两个角的余弦自动相等——省掉全部坐标运算．"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-335'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-335-V2',
}

T373_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知双曲线 $\dfrac{x^{2}}{a^{2}}-\dfrac{y^{2}}{b^{2}}=1$（$a>0,b>0$）的左、右焦点分别为 $F_1,F_2$，" "\n"
        r"以 $OF_1$ 为直径的圆与双曲线的一条渐近线交于点 $M$，若线段 $MF_1$ 交双曲线于点 $P$，" "\n"
        r"且 $\lvert PF_2\rvert=5\lvert PF_1\rvert$，则双曲线的离心率为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac{\sqrt{26}}4$"),
        ('B', r"$\dfrac{\sqrt{34}}4$"),
        ('C', r"$\sqrt2$"),
        ('D', r"$\sqrt3$"),
    ],
    'answer': 'C',
    'analysis': (
        r"直径所对圆周角为直角 ⟹ $OM\perp MF_1$ ⟹ $k_{MF_1}=\frac ab$ ⟹ $\cos\theta=\frac bc$（$\theta=\angle MF_1F_2$）；" "\n"
        r"再配 $\lvert PF_2\rvert=5\lvert PF_1\rvert$ 与定义解出 $\lvert PF_1\rvert=\frac a2$，余弦定理收尾．"
    ),
    'solution': (
        r"以 $OF_1$ 为直径的圆方程为 $\left(x+\dfrac c2\right)^{2}+y^{2}=\dfrac{c^{2}}4$，即 $x^{2}+y^{2}+cx=0$．" "\n"
        r"不妨取 $M$ 在第二象限，则 $M$ 在渐近线 $y=-\dfrac ba x$ 上．代入圆方程：" "\n"
        r"$x^{2}+\dfrac{b^{2}}{a^{2}}x^{2}+cx=0\Longrightarrow \dfrac{c^{2}}{a^{2}}x^{2}+cx=0\Longrightarrow x_M=-\dfrac{a^{2}}c$，$y_M=\dfrac{ab}c$．" "\n"
        r"（也可直接用「直径所对圆周角为直角」：$OM\perp MF_1$，故 $k_{MF_1}=-\dfrac1{k_{OM}}=\dfrac ab$．）" "\n"
        r"记 $\theta=\angle MF_1F_2=\angle PF_1F_2$（$P$ 在线段 $MF_1$ 上），则 $\tan\theta=\dfrac ab$，于是" "\n"
        r"$\cos\theta=\dfrac{b}{\sqrt{a^{2}+b^{2}}}=\dfrac bc$．" "\n"
        r"由 $\lvert PF_2\rvert=5\lvert PF_1\rvert$ 及 $P$ 在左支上（$MF_1$ 连的是左焦点，与左支相交）" "\n"
        r"$\lvert PF_2\rvert-\lvert PF_1\rvert=2a\Longrightarrow \lvert PF_1\rvert=\dfrac a2$，$\lvert PF_2\rvert=\dfrac{5a}2$．" "\n"
        r"在 $\triangle PF_1F_2$ 中，由余弦定理" "\n"
        r"$\cos\theta=\dfrac{\lvert PF_1\rvert^{2}+\lvert F_1F_2\rvert^{2}-\lvert PF_2\rvert^{2}}{2\lvert PF_1\rvert\lvert F_1F_2\rvert}" "\n"
        r"=\dfrac{\frac{a^{2}}4+4c^{2}-\frac{25a^{2}}4}{2\cdot\frac a2\cdot2c}=\dfrac{2c^{2}-3a^{2}}{ac}$．" "\n"
        r"于是 $\dfrac bc=\dfrac{2c^{2}-3a^{2}}{ac}\Longrightarrow ab=2c^{2}-3a^{2}=2\left(a^{2}+b^{2}\right)-3a^{2}=2b^{2}-a^{2}$，" "\n"
        r"即 $2b^{2}-ab-a^{2}=0\Longrightarrow \left(2b+a\right)\left(b-a\right)=0\Longrightarrow b=a$．" "\n"
        r"故 $e=\dfrac ca=\dfrac{\sqrt{a^{2}+b^{2}}}a=\sqrt2$，故选 C．"
    ),
    'review': (
        r"① 数值复核：$a=b=1$、$c=\sqrt2$ 时 $M\left(-\frac{\sqrt2}2,\frac{\sqrt2}2\right)$（代回圆方程 $x^2+y^2+cx=0$ 得 $0$ ✓），" "\n"
        r"　 线段 $MF_1$ 与双曲线左支交于参数 $t=0.5$ 处，$P\left(-\frac{3\sqrt2}4,\frac{\sqrt2}4\right)$，" "\n"
        r"　 算得 $\lvert PF_1\rvert=0.5$、$\lvert PF_2\rvert=2.5$，比值恰为 $5$ ✓．" "\n"
        r"② 因式分解 $2b^{2}-ab-a^{2}=\left(2b+a\right)\left(b-a\right)$ 是本题的收口；因 $2b+a>0$，只能 $b=a$．" "\n"
        r"③ ⚠ $P$ 在**左支**（$MF_1$ 连接左焦点，与左支相交），故用 $\lvert PF_2\rvert-\lvert PF_1\rvert=2a$；" "\n"
        r"　 若误用 $\lvert PF_1\rvert-\lvert PF_2\rvert=2a$ 会得 $\lvert PF_1\rvert=-\frac a2<0$，立刻暴露．" "\n"
        r"④ 选项 A、B 原文提取为「$\frac{26}4$」「$\frac{34}4$」（分子被拆行），按 $\frac{\sqrt{26}}4$、$\frac{\sqrt{34}}4$ 还原；答案 C 不受影响．"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-373'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-373-V3',
}

T365_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知椭圆 $C:\dfrac{x^{2}}{a^{2}}+\dfrac{y^{2}}{b^{2}}=1$（$a>b>0$）的左、右焦点 $F_1,F_2$，" "\n"
        r"过原点的直线 $l$ 与椭圆 $C$ 相交于 $M,N$ 两点，其中 $M$ 在第一象限，" "\n"
        r"$\lvert MN\rvert=\lvert F_1F_2\rvert$，$\dfrac{\lvert NF_1\rvert}{\lvert MF_1\rvert}\ge\dfrac{\sqrt3}3$，" "\n"
        r"则椭圆 $C$ 的离心率的取值范围为（　　）"
    ),
    'opts': [
        ('A', r"$\left(0,\dfrac{\sqrt6-1}2\right]$"),
        ('B', r"$\left(0,\sqrt6-\sqrt2\right]$"),
        ('C', r"$\left(0,\sqrt3-1\right]$"),
        ('D', r"$\left(\dfrac{\sqrt2}2,\sqrt3-1\right]$"),
    ],
    'answer': 'D',
    'analysis': (
        r"$\lvert MN\rvert=\lvert F_1F_2\rvert$ 且两条对角线互相平分 ⟹ $MF_1NF_2$ 是矩形 ⟹" "\n"
        r"$\lvert MF_1\rvert^2+\lvert MF_2\rvert^2=4c^2$，配 $\lvert MF_1\rvert+\lvert MF_2\rvert=2a$ 得二次方程；" "\n"
        r"$\Delta>0$ 给下界，比值条件给上界．"
    ),
    'solution': (
        r"因 $l$ 过原点且椭圆关于原点中心对称，故 $N=-M$，$\lvert NF_1\rvert=\lvert MF_2\rvert$；" "\n"
        r"又 $MN$ 与 $F_1F_2$ 互相平分，四边形 $MF_1NF_2$ 是平行四边形．" "\n"
        r"由 $\lvert MN\rvert=\lvert F_1F_2\rvert$ 知该平行四边形的两条对角线相等，故它是矩形，于是" "\n"
        r"$\lvert MF_1\rvert^{2}+\lvert MF_2\rvert^{2}=\lvert MN\rvert^{2}=\left(2c\right)^{2}=4c^{2}$．" "\n"
        r"设 $\lvert MF_2\rvert=x$，则 $\lvert MF_1\rvert=2a-x$（椭圆定义）．$M$ 在第一象限离 $F_2$ 更近，故 $0<x<a$．" "\n"
        r"$x^{2}+\left(2a-x\right)^{2}=4c^{2}\Longrightarrow 2x^{2}-4ax+4a^{2}=4c^{2}\Longrightarrow x^{2}-2ax+2b^{2}=0$．　①" "\n"
        r"① 有实根需 $\Delta=4a^{2}-8b^{2}>0$，即 $a^{2}>2b^{2}=2a^{2}-2c^{2}\Longrightarrow 2c^{2}>a^{2}\Longrightarrow e>\dfrac{\sqrt2}2$．" "\n"
        r"① 的两根为 $x=a\pm\sqrt{a^{2}-2b^{2}}$；由 $x<a$ 取**较小根** $x=a-\sqrt{a^{2}-2b^{2}}$．" "\n"
        r"由 $\dfrac{\lvert NF_1\rvert}{\lvert MF_1\rvert}=\dfrac{x}{2a-x}\ge\dfrac{\sqrt3}3$ 得" "\n"
        r"$3x\ge\sqrt3\left(2a-x\right)\Longrightarrow \left(3+\sqrt3\right)x\ge2\sqrt3a\Longrightarrow x\ge\dfrac{2\sqrt3}{3+\sqrt3}a=\left(\sqrt3-1\right)a$．" "\n"
        r"于是 $a-\sqrt{a^{2}-2b^{2}}\ge\left(\sqrt3-1\right)a\Longrightarrow \sqrt{a^{2}-2b^{2}}\le\left(2-\sqrt3\right)a$" "\n"
        r"$\Longrightarrow a^{2}-2b^{2}\le\left(7-4\sqrt3\right)a^{2}\Longrightarrow 2b^{2}\ge\left(4\sqrt3-6\right)a^{2}$" "\n"
        r"$\Longrightarrow 2a^{2}-2c^{2}\ge\left(4\sqrt3-6\right)a^{2}\Longrightarrow 2c^{2}\le\left(8-4\sqrt3\right)a^{2}$" "\n"
        r"$\Longrightarrow c^{2}\le\left(4-2\sqrt3\right)a^{2}=\left(\sqrt3-1\right)^{2}a^{2}\Longrightarrow e\le\sqrt3-1$．" "\n"
        r"综上 $e\in\left(\dfrac{\sqrt2}2,\sqrt3-1\right]$，故选 D．"
    ),
    'review': (
        r"① 数值复核（$a=1$）：$e=0.72$ 时 $x=0.808$、比值 $=0.678>0.577$ ✓ 可取；" "\n"
        r"　 $e=\sqrt3-1=0.732051$ 时 $x=0.732051$、比值 $=0.577350=\frac{\sqrt3}3$ ✓ **恰取等，故右端闭**；" "\n"
        r"　 $e=0.75$ 时 $x=0.646$、比值 $=0.4776<0.577$ ✗ 不可取．" "\n"
        r"② 关键一步是「$\lvert MN\rvert=\lvert F_1F_2\rvert$ ⟹ 矩形」——两条对角线相等且互相平分的平行四边形是矩形．" "\n"
        r"③ ⚠ 两根中必须取**较小**的 $x$（因 $M$ 在第一象限，$\lvert MF_2\rvert<\lvert MF_1\rvert$ 即 $x<a$）；" "\n"
        r"　 取大根 $x=a+\sqrt{a^2-2b^2}>a$，与 $x<a$ 矛盾．" "\n"
        r"④ 选项 A、B 原文提取为「$(0,\frac{\sqrt6-1}2]$」「$(0,\sqrt6-\sqrt2]$」（根号在提取中丢失），按相邻项结构还原；" "\n"
        r"　 答案 D 由严格推导唯一确定，不受干扰项还原影响．" "\n"
        r"⑤ 代数自检：$\left(\sqrt3-1\right)^{2}=4-2\sqrt3$ 与上面 $c^2$ 的系数一致 ✓．"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-365'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-365-E1',
}

T333_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知 $F_1,F_2$ 是椭圆和双曲线的公共焦点，$P$ 是它们的一个公共点，" "\n"
        r"且 $\angle F_1PF_2=\dfrac{2\pi}3$，则椭圆和双曲线的离心率之积的范围是（　　）"
    ),
    'opts': [
        ('A', r"$\left(1,+\infty\right)$"),
        ('B', r"$\left(0,1\right)$"),
        ('C', r"$\left(0,2\right)$"),
        ('D', r"$\left(2,+\infty\right)$"),
    ],
    'answer': 'A',
    'analysis': (
        r"由定义解出 $\lvert PF_1\rvert=a_1+a_2$、$\lvert PF_2\rvert=a_1-a_2$，余弦定理（$\cos\frac{2\pi}3=-\frac12$，交叉项变 $+mn$）" "\n"
        r"给 $3a_1^{2}+a_2^{2}=4c^{2}$，即 $\frac3{e_1^2}+\frac1{e_2^2}=4$；再把它看成 $e_1$ 的函数用单调性取值域．"
    ),
    'solution': (
        r"设椭圆长半轴为 $a_1$、双曲线实半轴为 $a_2$、公共半焦距为 $c$，" "\n"
        r"$\lvert PF_1\rvert=m$、$\lvert PF_2\rvert=n$（不妨 $m>n$）．由两条定义" "\n"
        r"$m+n=2a_1$，$m-n=2a_2\Longrightarrow m=a_1+a_2$，$n=a_1-a_2$．" "\n"
        r"在 $\triangle PF_1F_2$ 中，$\lvert F_1F_2\rvert=2c$，$\cos\dfrac{2\pi}3=-\dfrac12$，由余弦定理" "\n"
        r"$4c^{2}=m^{2}+n^{2}-2mn\cos\dfrac{2\pi}3=m^{2}+n^{2}+mn$" "\n"
        r"$=\left(a_1+a_2\right)^{2}+\left(a_1-a_2\right)^{2}+\left(a_1^{2}-a_2^{2}\right)=3a_1^{2}+a_2^{2}$．" "\n"
        r"两边同除以 $c^{2}$：" "\n"
        r"$\dfrac3{e_1^{2}}+\dfrac1{e_2^{2}}=4$．　①" "\n"
        r"由 ① 解出 $e_2^{2}=\dfrac{e_1^{2}}{4e_1^{2}-3}$（需 $4e_1^{2}-3>0$，即 $e_1>\frac{\sqrt3}2$；" "\n"
        r"又 $e_1<1$，故 $e_1^{2}\in\left(\frac34,1\right)$）．记 $u=e_1e_2$，令 $t=e_1^{2}$，则" "\n"
        r"$u^{2}=e_1^{2}e_2^{2}=\dfrac{t^{2}}{4t-3}$，$t\in\left(\dfrac34,1\right)$．" "\n"
        r"求导：$\dfrac{d}{dt}\left(\dfrac{t^{2}}{4t-3}\right)=\dfrac{2t\left(4t-3\right)-4t^{2}}{\left(4t-3\right)^{2}}=\dfrac{2t\left(2t-3\right)}{\left(4t-3\right)^{2}}<0$（因 $t<1<\frac32$），" "\n"
        r"故 $u^{2}$ 在 $\left(\frac34,1\right)$ 上严格递减：当 $t\to1^{-}$ 时 $u^{2}\to1$；当 $t\to\frac34^{+}$ 时 $u^{2}\to+\infty$．" "\n"
        r"所以 $u=e_1e_2\in\left(1,+\infty\right)$，故选 A．"
    ),
    'review': (
        r"① 原书用「取特殊值排除」：$e_1=\frac67,e_2=2$ 得 $e_1e_2=\frac{12}7$ 排除 B、D；$e_1=\frac9{11},e_2=3$ 得 $\frac{27}{11}$ 排除 C．" "\n"
        r"　 我改用**单调性**给出严格证明：$u^{2}=\frac{t^{2}}{4t-3}$ 在 $t\in\left(\frac34,1\right)$ 上严格递减，值域为 $\left(1,+\infty\right)$．" "\n"
        r"② 数值复核：$e_2=1.01$ 时 $e_1=0.996732$、$e_1e_2=1.006699$；$e_2=100$ 时 $e_1=0.866036$、$e_1e_2=86.6036$ ——" "\n"
        r"　 下界 $1$ 取不到（$e_2\to1^+$ 的极限）、上界无界 ✓．" "\n"
        r"③ ⚠ $\angle F_1PF_2=\frac{2\pi}3$ 时余弦定理的交叉项是 $-2mn\cos\frac{2\pi}3=+mn$，**与 $\frac\pi3$ 型符号相反** ——" "\n"
        r"　 这正是 $3a_1^{2}+a_2^{2}$ 中系数 $3$ 落在 $a_1$ 上的原因（$\frac\pi3$ 型是 $a_1^{2}+3a_2^{2}$，见 M-T-333-V2）．" "\n"
        r"④ 选项 C、D 原文提取为「$(0,2)$」「$(2,+\infty)$」；由 $e_2$ 可任意大知 $e_1e_2$ 无上界，故只能选 A．"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-333'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-333-V3',
}

T333_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知 $F_1,F_2$ 是椭圆和双曲线的公共焦点，$P$ 是它们的一个公共点，且 $\angle F_1PF_2=\dfrac\pi3$，" "\n"
        r"记椭圆和双曲线的离心率分别为 $e_1,e_2$，则 $\dfrac1{e_1}+\dfrac{\sqrt3}{e_2}$ 的最大值为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac{2\sqrt2}3$"),
        ('B', r"$\dfrac{2\sqrt3}3$"),
        ('C', r"$2\sqrt3$"),
        ('D', r"$2\sqrt2$"),
    ],
    'answer': 'D',
    'analysis': (
        r"同 M-T-333-V3 得 $\angle=\frac\pi3$ 型恒等式 $a_1^{2}+3a_2^{2}=4c^{2}$，即 $\frac1{e_1^2}+\frac3{e_2^2}=4$；" "\n"
        r"再用柯西不等式 $\left(\frac1{e_1}+\frac{\sqrt3}{e_2}\right)^{2}\le(1+1)\left(\frac1{e_1^2}+\frac3{e_2^2}\right)=8$．"
    ),
    'solution': (
        r"设 $\lvert PF_1\rvert=m$、$\lvert PF_2\rvert=n$（$m>n$），由两条定义" "\n"
        r"$m+n=2a_1$，$m-n=2a_2\Longrightarrow m=a_1+a_2$，$n=a_1-a_2$．" "\n"
        r"在 $\triangle PF_1F_2$ 中，$\cos\dfrac\pi3=\dfrac12$，由余弦定理" "\n"
        r"$4c^{2}=m^{2}+n^{2}-2mn\cos\dfrac\pi3=m^{2}+n^{2}-mn$" "\n"
        r"$=\left(a_1+a_2\right)^{2}+\left(a_1-a_2\right)^{2}-\left(a_1^{2}-a_2^{2}\right)=a_1^{2}+3a_2^{2}$．" "\n"
        r"两边同除以 $c^{2}$：" "\n"
        r"$\dfrac1{e_1^{2}}+\dfrac3{e_2^{2}}=4$．　①" "\n"
        r"由柯西不等式" "\n"
        r"$\left(\dfrac1{e_1}+\dfrac{\sqrt3}{e_2}\right)^{2}=\left(1\cdot\dfrac1{e_1}+1\cdot\dfrac{\sqrt3}{e_2}\right)^{2}" "\n"
        r"\le\left(1^{2}+1^{2}\right)\left(\dfrac1{e_1^{2}}+\dfrac3{e_2^{2}}\right)=2\times4=8$，" "\n"
        r"故 $\dfrac1{e_1}+\dfrac{\sqrt3}{e_2}\le2\sqrt2$．" "\n"
        r"取等条件为 $\dfrac{1/e_1}{1}=\dfrac{\sqrt3/e_2}{1}$，即 $e_2=\sqrt3e_1$；代入 ① 得" "\n"
        r"$\dfrac1{e_1^{2}}+\dfrac3{3e_1^{2}}=\dfrac2{e_1^{2}}=4\Longrightarrow e_1=\dfrac1{\sqrt2}$（$<1$ ✓），$e_2=\dfrac{\sqrt3}{\sqrt2}$（$>1$ ✓）．" "\n"
        r"故最大值为 $2\sqrt2$，选 D．"
    ),
    'review': (
        r"① 题干中的 $\frac{\sqrt3}{e_2}$ 在提取时被误读为 $\frac3{e_2}$（根号丢失）．判据有二：" "\n"
        r"　 （i）若为 $\frac3{e_2}$，由柯西得 $\left(\frac1{e_1}+\frac3{e_2}\right)^2\le(1+3)\left(\frac1{e_1^2}+\frac3{e_2^2}\right)=16$，最大值应是 $4$，" "\n"
        r"　 与四个选项都不符；（ii）原书详解写「$\le2\left(\frac1{e_1^2}+\frac3{e_2^2}\right)=8$」，左边的系数 $2$ 只能是 $1^2+1^2$，" "\n"
        r"　 对应 $\frac1{e_1}+1\cdot\frac{\sqrt3}{e_2}$ 的配法，故必为 $\frac{\sqrt3}{e_2}$．" "\n"
        r"② 取等核验：$e_1=\frac1{\sqrt2}=0.707107$、$e_2=\frac{\sqrt3}{\sqrt2}=1.224745$ 均合法（$e_1<1<e_2$），" "\n"
        r"　 此时 $\frac1{e_1}+\frac{\sqrt3}{e_2}=1.414214+1.414214=2.828427=2\sqrt2$ ✓．" "\n"
        r"③ 原书详解写「当且仅当 $\frac1{e_1}=\frac3{e_2}$，即 $e_2=3e_1$」——应为 $\frac1{e_1}=\frac{\sqrt3}{e_2}$，即 $e_2=\sqrt3e_1$（同样是根号丢失）．" "\n"
        r"④ 与 M-T-333-V3 对照记忆：$\frac\pi3$ 型得 $a_1^{2}+3a_2^{2}=4c^{2}$，$\frac{2\pi}3$ 型得 $3a_1^{2}+a_2^{2}=4c^{2}$．"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-333'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-333-V2',
}

T370_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知点 $A$ 是抛物线 $x^{2}=4y$ 的对称轴与准线的交点，点 $F$ 为抛物线的焦点，" "\n"
        r"点 $P$ 在抛物线上且满足 $\lvert PA\rvert=m\lvert PF\rvert$，若 $m$ 取最大值时，" "\n"
        r"点 $P$ 恰好在以 $A,F$ 为焦点的双曲线上，则双曲线的离心率为（　　）"
    ),
    'opts': [
        ('A', r"$\sqrt3+1$"),
        ('B', r"$\sqrt2+1$"),
        ('C', r"$\dfrac{\sqrt5+1}2$"),
        ('D', r"$\dfrac{\sqrt2+1}2$"),
    ],
    'answer': 'B',
    'analysis': (
        r"把 $\frac1m$ 写成 $\sin\alpha$（$\alpha$ 为 $PA$ 的倾斜角），于是 $m$ 最大 ⟺ $\sin\alpha$ 最小 ⟺ $PA$ 与抛物线相切；" "\n"
        r"解出切点 $P(2,1)$ 后，双曲线的 $2a'=\lvert PA\rvert-\lvert PF\rvert$、$2c'=\lvert AF\rvert=2$．"
    ),
    'solution': (
        r"$x^{2}=4y$ 的焦点 $F\left(0,1\right)$、准线 $y=-1$，故 $A\left(0,-1\right)$．" "\n"
        r"过 $P$ 作准线的垂线，垂足为 $N$，则 $\lvert PN\rvert$ 是 $P$ 到水平直线 $y=-1$ 的距离．" "\n"
        r"由抛物线的定义 $\lvert PN\rvert=\lvert PF\rvert$，于是" "\n"
        r"$\dfrac1m=\dfrac{\lvert PF\rvert}{\lvert PA\rvert}=\dfrac{\lvert PN\rvert}{\lvert PA\rvert}$．" "\n"
        r"设 $PA$ 的倾斜角为 $\alpha$，则 $\dfrac{\lvert PN\rvert}{\lvert PA\rvert}=\sin\alpha$，故" "\n"
        r"$m$ 最大 $\iff\sin\alpha$ 最小 $\iff$ 直线 $PA$ 与抛物线相切．" "\n"
        r"设切线方程为 $y=kx-1$（过 $A$），代入 $x^{2}=4y$ 得" "\n"
        r"$x^{2}=4\left(kx-1\right)\Longrightarrow x^{2}-4kx+4=0$，" "\n"
        r"$\Delta=16k^{2}-16=0\Longrightarrow k=\pm1$．取 $k=1$ 得切点 $P\left(2,1\right)$（$k=-1$ 对称）．" "\n"
        r"此时 $\lvert PA\rvert=\sqrt{2^{2}+2^{2}}=2\sqrt2$，$\lvert PF\rvert=\sqrt{2^{2}+0^{2}}=2$．" "\n"
        r"以 $A,F$ 为焦点的双曲线中：" "\n"
        r"$2c'=\lvert AF\rvert=2\Longrightarrow c'=1$；" "\n"
        r"$2a'=\bigl\lvert\lvert PA\rvert-\lvert PF\rvert\bigr\rvert=2\sqrt2-2\Longrightarrow a'=\sqrt2-1$．" "\n"
        r"故 $e'=\dfrac{c'}{a'}=\dfrac1{\sqrt2-1}=\sqrt2+1$，故选 B．"
    ),
    'review': (
        r"① 数值复核：$P(2,1)$ 处 $\lvert PA\rvert=2.828427$、$\lvert PF\rvert=2$，$m=\sqrt2$；" "\n"
        r"　 $e'=\frac1{\sqrt2-1}=2.414214=\sqrt2+1$ ✓（有理化 $\frac1{\sqrt2-1}=\sqrt2+1$ 要熟练）．" "\n"
        r"② 题眼是 $\frac1m=\sin\alpha$：因准线 $y=-1$ 是**水平**的，$\lvert PN\rvert$ 是竖直距离，" "\n"
        r"　 故 $\frac{\lvert PN\rvert}{\lvert PA\rvert}$ 恰是 $PA$ 与水平方向夹角的正弦．" "\n"
        r"③ 原书详解末行写「实轴长为 $PA-PB$」，其中 $B$ 为笔误，应为 $PF$（题中无点 $B$）．" "\n"
        r"④ ⚠ 双曲线的 $a^{\prime},c^{\prime}$ 与抛物线的参数是两套记号，本题抛物线的焦点参数 $p=2$ 全程不参与计算．"
    ),
    'difficulty': 0.82,
    'topics': ['M-T-370'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-370-E1',
}

T370_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知抛物线 $M:x^{2}=12y$ 和椭圆 $N:\dfrac{x^{2}}{a^{2}}+\dfrac{y^{2}}{b^{2}}=1$（$a>b>0$），" "\n"
        r"直线 $l$ 与抛物线 $M$ 相切，其倾斜角为 $\dfrac\pi4$，$l$ 过椭圆 $N$ 的右焦点 $F$，与椭圆相交于 $A,B$ 两点，" "\n"
        r"$\lvert AF\rvert=\sqrt2<\lvert BF\rvert$，则椭圆 $N$ 的离心率为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac12$"),
        ('B', r"$\dfrac{\sqrt2}2$"),
        ('C', r"$\dfrac{\sqrt3}3$"),
        ('D', r"$\dfrac{\sqrt3}2$"),
    ],
    'answer': 'B',
    'analysis': (
        r"用导数求切点 ⟹ $l:y=x-3$ ⟹ 右焦点 $F(3,0)$ 即 $c=3$；" "\n"
        r"由 $\lvert AF\rvert=\sqrt2$ 与倾斜角 $45^\circ$ 定位 $A(4,1)$，代入椭圆配 $a^2=b^2+9$ 解出 $a,b$．"
    ),
    'solution': (
        r"由 $x^{2}=12y$ 得 $y=\dfrac{x^{2}}{12}$，$y'=\dfrac x6$．倾斜角 $\dfrac\pi4$ 即斜率为 $1$，" "\n"
        r"令 $\dfrac x6=1$ 得 $x=6$，$y=3$，故切点为 $\left(6,3\right)$，" "\n"
        r"切线 $l:y-3=1\cdot\left(x-6\right)$，即 $y=x-3$．" "\n"
        r"令 $y=0$ 得 $x=3$，故椭圆的右焦点为 $F\left(3,0\right)$，即 $c=3$，$a^{2}=b^{2}+9$．" "\n"
        r"由 $\lvert AF\rvert=\sqrt2$ 且 $l$ 的倾斜角为 $45^\circ$：过 $A$ 作 $x$ 轴的垂线，垂足 $H$，" "\n"
        r"则 $\mathrm{Rt}\triangle AHF$ 为等腰直角三角形，$\lvert FH\rvert=\lvert AH\rvert=1$．" "\n"
        r"取 $A$ 在 $F$ 的右上方，得 $A\left(4,1\right)$（另一交点 $B\left(0,-3\right)$，$\lvert BF\rvert=3\sqrt2>\sqrt2$，符合题意）．" "\n"
        r"把 $A$ 代入椭圆：" "\n"
        r"$\dfrac{16}{a^{2}}+\dfrac1{b^{2}}=1$．令 $b^{2}=u$，则 $a^{2}=u+9$，" "\n"
        r"$\dfrac{16}{u+9}+\dfrac1u=1\Longrightarrow 16u+\left(u+9\right)=u\left(u+9\right)\Longrightarrow u^{2}-8u-9=0$，" "\n"
        r"解得 $u=9$（舍 $u=-1$），故 $b^{2}=9$、$a^{2}=18$，$a=3\sqrt2$．" "\n"
        r"$e=\dfrac ca=\dfrac3{3\sqrt2}=\dfrac{\sqrt2}2$，故选 B．"
    ),
    'review': (
        r"① 代数复核：$b^{2}=9$ 时 $\frac{16}{18}+\frac19=\frac89+\frac19=1$ ✓；另一交点由 $\frac{x^2}{18}+\frac{(x-3)^2}{9}=1$" "\n"
        r"　 得 $3x^{2}-12x=0$，$x=4$ 或 $0$，即 $A(4,1)$、$B(0,-3)$，$\lvert BF\rvert=\sqrt{9+9}=3\sqrt2>\sqrt2$ ✓．" "\n"
        r"② 两点提醒：（i）$x^{2}=12y$ 求导得 $y'=\frac x6$（不是 $\frac x{12}$）；" "\n"
        r"　 （ii）由 $\lvert AF\rvert=\sqrt2$ 定位 $A$ 时，用「倾斜角 $45^\circ$ ⟹ 水平、竖直位移相等」比设坐标快得多．" "\n"
        r"③ 条件 $\lvert AF\rvert=\sqrt2<\lvert BF\rvert$ 用来确定 $A$ 是离 $F$ 较近的那个交点（$A(4,1)$ 而非 $B(0,-3)$），" "\n"
        r"　 若把 $A,B$ 弄反，$\lvert AF\rvert=3\sqrt2$ 会解出完全不同的 $a,b$．" "\n"
        r"④ 原书 $ans$ 字段中混入了【分析】文字（「根据题意，利用导数的几何意义…」），已分离到 $analysis$．"
    ),
    'difficulty': 0.80,
    'topics': ['M-T-370'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-370-V2',
}

T374_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知双曲线 $C:\dfrac{x^{2}}{a^{2}}-\dfrac{y^{2}}{b^{2}}=1$（$a>0,b>0$），直线 $x=2a$ 与 $C$ 交于 $A,B$ 两点" "\n"
        r"（$A$ 在 $B$ 的上方），$\overrightarrow{DA}=\overrightarrow{AB}$，点 $E$ 在 $y$ 轴上，且 $EA\parallel x$ 轴，" "\n"
        r"若 $\triangle BDE$ 的内心到 $y$ 轴的距离为 $\dfrac{4a}3$，则 $C$ 的离心率为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac{\sqrt6}2$"),
        ('B', r"$\dfrac{\sqrt{10}}3$"),
        ('C', r"$\sqrt6$"),
        ('D', r"$\sqrt{10}$"),
    ],
    'answer': 'B',
    'analysis': (
        r"$\overrightarrow{DA}=\overrightarrow{AB}$ ⟹ $A$ 是 $BD$ 中点 ⟹ $D(2a,3\sqrt3b)$、$E(0,\sqrt3b)$ ⟹ $\triangle BDE$ 等腰；" "\n"
        r"用内心分角平分线之比 $\frac{\lvert EG\rvert}{\lvert GA\rvert}=\frac{\lvert ED\rvert}{\lvert DA\rvert}=2$ 得 $\lvert ED\rvert=2\lvert DA\rvert$，再勾股定 $a=3b$．"
    ),
    'solution': (
        r"把 $x=2a$ 代入 $\dfrac{x^{2}}{a^{2}}-\dfrac{y^{2}}{b^{2}}=1$ 得 $4-\dfrac{y^{2}}{b^{2}}=1\Longrightarrow y=\pm\sqrt3b$，" "\n"
        r"故 $A\left(2a,\sqrt3b\right)$、$B\left(2a,-\sqrt3b\right)$，$\lvert AB\rvert=2\sqrt3b$．" "\n"
        r"由 $\overrightarrow{DA}=\overrightarrow{AB}$ 知 $A$ 是线段 $BD$ 的中点，故" "\n"
        r"$D=2A-B=\left(2a,3\sqrt3b\right)$，" "\n"
        r"由 $EA\parallel x$ 轴且 $E$ 在 $y$ 轴上得 $E\left(0,\sqrt3b\right)$．" "\n"
        r"于是 $\lvert ED\rvert=\lvert EB\rvert=\sqrt{4a^{2}+12b^{2}}$，$\triangle BDE$ 是以 $E$ 为顶角的等腰三角形；" "\n"
        r"又 $EA\perp BD$（$BD$ 竖直、$EA$ 水平），故 $EA$ 平分 $\angle BED$，内心 $G$ 在线段 $EA$ 上．" "\n"
        r"由 $G$ 到 $y$ 轴的距离为 $\dfrac{4a}3$ 得 $G\left(\dfrac{4a}3,\sqrt3b\right)$，于是" "\n"
        r"$\lvert EG\rvert=\dfrac{4a}3$，$\lvert GA\rvert=2a-\dfrac{4a}3=\dfrac{2a}3$，$\dfrac{\lvert EG\rvert}{\lvert GA\rvert}=2$．" "\n"
        r"内心分角平分线：$\dfrac{\lvert EG\rvert}{\lvert GA\rvert}=\dfrac{\lvert ED\rvert+\lvert EB\rvert}{\lvert BD\rvert}$；" "\n"
        r"由 $\lvert ED\rvert=\lvert EB\rvert$ 且 $\lvert BD\rvert=4\sqrt3b=2\lvert DA\rvert$（$\lvert DA\rvert=2\sqrt3b$），得" "\n"
        r"$\dfrac{\lvert ED\rvert}{\lvert DA\rvert}=2\Longrightarrow \lvert ED\rvert=2\lvert DA\rvert=4\sqrt3b$．" "\n"
        r"在 $\mathrm{Rt}\triangle EAD$ 中（$\angle EAD=90^\circ$）：" "\n"
        r"$\lvert EA\rvert=\sqrt{\lvert ED\rvert^{2}-\lvert DA\rvert^{2}}=\sqrt3\lvert DA\rvert=\sqrt3\cdot2\sqrt3b=6b$．" "\n"
        r"又 $\lvert EA\rvert=2a$（$E$ 到 $A$ 的水平距离），故 $2a=6b$，即 $a=3b$．" "\n"
        r"$e=\sqrt{1+\dfrac{b^{2}}{a^{2}}}=\sqrt{1+\dfrac19}=\dfrac{\sqrt{10}}3$，故选 B．"
    ),
    'review': (
        r"① 数值复核（$b=1,a=3$）：$\lvert ED\rvert=\lvert EB\rvert=6.928203$ 相等 ✓；" "\n"
        r"　 $\frac{\lvert EG\rvert}{\lvert GA\rvert}=2.000$ 与 $\frac{\lvert ED\rvert}{\lvert DA\rvert}=2.000$ 一致 ✓；$e=\frac{\sqrt{10}}3=1.054093$ ✓．" "\n"
        r"② 内心分角平分线的通式是 $\frac{\lvert EG\rvert}{\lvert GA\rvert}=\frac{\lvert ED\rvert+\lvert EB\rvert}{\lvert BD\rvert}$（$G$ 在从 $E$ 出发的角平分线上）；" "\n"
        r"　 本题因 $\lvert BD\rvert=2\lvert DA\rvert$（$A$ 为中点）恰好化简成 $\frac{\lvert ED\rvert}{\lvert DA\rvert}$．" "\n"
        r"③ 原书详解写「$\frac{\lvert EA\rvert}{\lvert DA\rvert}=3$，即 $a=3b$」——这里的 $3$ 是 $\sqrt3$（根号丢失）；" "\n"
        r"　 按 $3$ 会得 $\lvert EA\rvert=3\lvert DA\rvert=6\sqrt3b$，即 $a=3\sqrt3b$，与正确结果不符．" "\n"
        r"④ ⚠ $\overrightarrow{DA}=\overrightarrow{AB}$ 是**向量**等式（$A$ 为 $BD$ 的中点），不是长度相等；" "\n"
        r"　 按长度相等会多出「$D$ 在 $A$ 下方」的歧义解．" "\n"
        r"⑤ 由 $\lvert ED\rvert=2\lvert DA\rvert$ 也可直接得 $\angle EDA=60^\circ$（$\cos\angle EDA=\frac{\lvert DA\rvert}{\lvert ED\rvert}=\frac12$），" "\n"
        r"　 于是 $\lvert EA\rvert=\sqrt3\lvert DA\rvert$ —— 与勾股法殊途同归．"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-374'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-374-E1',
}

T376_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知 $P\left(2,-2\right)$ 是离心率为 $\dfrac12$ 的椭圆 $\dfrac{x^{2}}{a^{2}}+\dfrac{y^{2}}{b^{2}}=1$（$a>b>0$）外一点，" "\n"
        r"经过点 $P$ 的光线被 $y$ 轴反射后，所有反射光线所在直线中只有一条与椭圆相切，" "\n"
        r"则此条切线的斜率是（　　）"
    ),
    'opts': [
        ('A', r"$-\dfrac18$"),
        ('B', r"$-\dfrac12$"),
        ('C', r"$1$"),
        ('D', r"$\dfrac18$"),
    ],
    'answer': 'D',
    'analysis': (
        r"反射 ⟹ 反射光线都过 $P$ 关于 $y$ 轴的镜像点 $P'(-2,-2)$；" "\n"
        r"令判别式为 $0$ 得关于 $k$ 的方程，「只有一条」要分「判别式为零」与「二次项系数为零」两种情形讨论．"
    ),
    'solution': (
        r"由 $e=\dfrac ca=\dfrac12$ 得 $b^{2}=a^{2}-c^{2}=\dfrac34a^{2}$，椭圆方程可写成" "\n"
        r"$3x^{2}+4y^{2}=3a^{2}$．" "\n"
        r"设入射光线的斜率为 $k$，方程为 $y+2=k\left(x-2\right)$，即 $y=kx-2k-2$；" "\n"
        r"被 $y$ 轴反射（$x\to-x$）后，反射光线方程为" "\n"
        r"$y=-kx-2k-2$（它过 $P$ 的镜像点 $P'\left(-2,-2\right)$）．" "\n"
        r"代入椭圆：$3x^{2}+4\left(-kx-2k-2\right)^{2}=3a^{2}$，整理得" "\n"
        r"$\left(3+4k^{2}\right)x^{2}+16k\left(k+1\right)x+16k^{2}+32k+16-3a^{2}=0$．" "\n"
        r"相切 $\iff\Delta=0$：" "\n"
        r"$256k^{2}\left(k+1\right)^{2}-4\left(3+4k^{2}\right)\left(16k^{2}+32k+16-3a^{2}\right)=0$，" "\n"
        r"两边同除以 $4$，并把 $16k^{2}+32k+16$ 写成 $16\left(k+1\right)^{2}$：" "\n"
        r"$64k^{2}\left(k+1\right)^{2}-\left(3+4k^{2}\right)\left(16\left(k+1\right)^{2}-3a^{2}\right)=0$" "\n"
        r"$\Longrightarrow 64k^{2}\left(k+1\right)^{2}-48\left(k+1\right)^{2}+9a^{2}-64k^{2}\left(k+1\right)^{2}+12a^{2}k^{2}=0$" "\n"
        r"$\Longrightarrow \left(k+1\right)^{2}\bigl[64k^{2}-48-64k^{2}\bigr]+3a^{2}\left(3+4k^{2}\right)=0$" "\n"
        r"$\Longrightarrow 3a^{2}\left(3+4k^{2}\right)=48\left(k+1\right)^{2}，即\ a^{2}\left(3+4k^{2}\right)=16\left(k+1\right)^{2}$" "\n"
        r"$\Longrightarrow 3a^{2}+4a^{2}k^{2}=16k^{2}+32k+16$" "\n"
        r"$\Longrightarrow \left(4a^{2}-16\right)k^{2}-32k+\left(3a^{2}-16\right)=0$．　①" "\n"
        r"**「所有反射光线中只有一条相切」即 ① 关于 $k$ 恰有一个实根**，有两种可能：" "\n"
        r"（i）$4a^{2}-16\ne0$ 且 $\Delta_k=0$：" "\n"
        r"　 $1024-4\left(4a^{2}-16\right)\left(3a^{2}-16\right)=0\Longrightarrow 12a^{4}-112a^{2}=0\Longrightarrow a^{2}=\dfrac{28}3$．" "\n"
        r"　 此时 $\dfrac4{a^{2}}+\dfrac4{b^{2}}=\dfrac{12}{28}+\dfrac47=1$，即 $P'\left(-2,-2\right)$ 落在椭圆上，" "\n"
        r"　 与题设「$P$ 是椭圆**外**一点」矛盾，舍去．" "\n"
        r"（ii）$4a^{2}-16=0$，即 $a^{2}=4$：① 退化为一次方程 $-32k-4=0$，$k=-\dfrac18$（唯一）．" "\n"
        r"　 此时 $b^{2}=3$，$P\left(2,-2\right)$ 满足 $\dfrac44+\dfrac43>1$，确为外一点 ✓．" "\n"
        r"所求**切线**（即反射光线 $y=-kx-2k-2$）的斜率为 $-k=\dfrac18$，故选 D．"
    ),
    'review': (
        r"① ⚠ 题目问的是**切线（反射光线）的斜率** $-k=\frac18$，不是入射光线的斜率 $k=-\frac18$（后者恰是选项 A）．" "\n"
        r"　 原书详解末行写「解得 $a^{2}=4$，$k=\frac18$」——由 $-32k-4=0$ 应得 $k=-\frac18$，详解漏了负号；" "\n"
        r"　 但答案 $\frac18$ 正确，因为它指的是切线斜率 $-k$．" "\n"
        r"② 代入检验（$a^{2}=4$、$b^{2}=3$，椭圆 $3x^{2}+4y^{2}=12$）：" "\n"
        r"　 直线 $y=\frac18x-\frac74$（斜率 $\frac18$）代入得 $49x^{2}-28x+4=0$，$\Delta=784-784=0$ ✓ 确为切线；" "\n"
        r"　 改取斜率 $-\frac18$（即 $y=-\frac18x-\frac94$）则 $\Delta<0$，与椭圆无交点，不相切．" "\n"
        r"③ **「只有一条」的两种情形都要讨论**是本題题眼：判别式为零对应 $P'$ 恰在椭圆上（被「外一点」排除），" "\n"
        r"　 故只能走「二次项系数为零」这条路 —— 原书未说明这一点，直接令 $4a^{2}=16$．" "\n"
        r"④ 反射的本质：反射光线所在直线是入射直线关于 $y$ 轴的镜像，整族直线都过镜像点 $P'(-2,-2)$．"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-376'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-376-V1',
}

QS = [
    T327_V2, T330_V2, T334_V2, T335_V2, T373_V3, T365_E1,
    T333_V3, T333_V2, T370_E1, T370_V2, T374_E1, T376_V1,
]
