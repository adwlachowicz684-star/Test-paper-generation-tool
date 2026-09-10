# -*- coding: utf-8 -*-
r"""第63批：第一定义 / 多曲线 / 向量轨迹（8 题）

来源：2024高中数学热点题型归纳完整解析版.pdf
p303 M-T-327-E1/V1/V3；p304 M-T-329-V3；p309 M-T-335-E1/V3；p314 M-T-342-E1/V1

## ★★ 本批五处「根号丢失」的还原

| 题 | ref_bank 存的 | 实际 | 判定依据 |
|---|---|---|---|
| M-T-327-E1 | `2/4` | $\frac{\sqrt2}4$ | 建系算出 $A(0,c)$ 得 $b=c$，比值 $=\frac1{2\sqrt2}$ |
| M-T-329-V3 | `2 10` | $2\sqrt{10}$ | $P$ 在 $2x^{2}-y^{2}=20$ 即 $\frac{x^{2}}{10}-\frac{y^{2}}{20}=1$ 上，$2a=2\sqrt{10}$ |
| M-T-342-E1 | `4 3` | $4\sqrt3$ | 雅可比 $=\lvert OA\times OB\rvert=2\sqrt3$，区域面积 $=2\times2\sqrt3$ |
| M-T-342-V1 | $\frac\pi6+\frac34$ | $\frac\pi6+\frac{\sqrt3}4$ | 切线长 $\frac{\sqrt3}2$、$\angle AOB=120^\circ$，独立算出 $\frac\pi6+\frac{\sqrt3}4$ |
| M-T-335-E1 | 选项 | B $=\sqrt2+1$ | 详解末行 $\frac2{2(\sqrt2-1)}=\sqrt2+1$ |

## ★★ 跳过一题：M-T-327-V2

抛物线 $y^{2}=2px$，$AF\perp BF$，$M$ 为 $AB$ 中点，$N$ 为 $M$ 到准线的垂足，求 $\frac{\lvert AB\rvert}{\lvert MN\rvert}$ 最小值。

我算出：设 $\lvert AF\rvert=a$、$\lvert BF\rvert=b$，则 $\lvert AB\rvert=\sqrt{a^{2}+b^{2}}$（勾股），
由梯形中位线 $\lvert MN\rvert=\frac{a+b}2$，故比值 $=\frac{2\sqrt{a^{2}+b^{2}}}{a+b}\ge\sqrt2$（$a=b$ 取等）。
并构造了具体情形验证：$p=2$ 时 $A(0.172,0.828)$、$B(0.172,-0.828)$，比值 $=1.414=\sqrt2$ ✓

**ref_bank 存 `2`**。若答案是 $2$，则 $a=b$ 时 $\frac{2\sqrt{2a^2}}{2a}=\sqrt2\neq2$，与「$a=b$ 取等」矛盾；
故 `2` 大概率是 $\sqrt2$ 丢根号，**但也不排除题意为 $\frac{\lvert AB\rvert^{2}}{\lvert MN\rvert^{2}}$**。
两可之间，**按「算不清就不录」原则跳过**，此处存档备查。

## 八题验算

| 题 | 关键一步 | 答案 |
|---|---|---|
| M-T-327-E1 | $A$ 是 $PF_1$ 中点得 $A(0,c)$ ⟹ $b=c$、$a=\sqrt2c$；$B$ 在 $x=c$ 上 $y=\frac c{\sqrt2}$ | $\frac{\sqrt2}4$ |
| M-T-327-V1 | $P,Q$ 是 $AF_2,BF_2$ 中点 ⟹ 周长 $=2a+\frac{2b^{2}}a=16$ ⟹ $b^{2}=a(8-a)$ | $4$（$a=2$） |
| M-T-327-V3 | $\lvert PM\rvert+\lvert PF_1\rvert=10+(\lvert PM\rvert-\lvert PF_2\rvert)\le10+\lvert MF_2\rvert$ | $15$ |
| M-T-329-V3 | $2x^{2}-y^{2}=20-4(2x_1x_2-y_1y_2)=20$ ⟹ $\frac{x^{2}}{10}-\frac{y^{2}}{20}=1$ | $2\sqrt{10}$ |
| M-T-335-E1 | 相切时 $P(2,1)$，$2a=\lvert PA\rvert-\lvert PF\rvert=2(\sqrt2-1)$，$c=1$ | B $\sqrt2+1$ |
| M-T-335-V3 | 抛物线定义给 $n=\frac57m$，$m+n=2a$ ⟹ $6e^{2}-5e+1=0$ | $\frac12$ 或 $\frac13$ |
| M-T-342-E1 | $\cos\angle AOB=\frac24=\frac12$；雅可比 $=2\cdot2\sin60^\circ=2\sqrt3$ | $4\sqrt3$ |
| M-T-342-V1 | 切线长 $\frac{\sqrt3}2$、$\triangle EAB$ 面积 $\frac{3\sqrt3}{16}$、弓形 $\frac\pi6+\frac{\sqrt3}{16}$ | $\frac\pi6+\frac{\sqrt3}4$ |
"""

T327_E1 = {
    'type': '填空',
    'stem_text': (
        r"已知椭圆 $C:\dfrac{x^{2}}{a^{2}}+\dfrac{y^{2}}{b^{2}}=1$（$a>b>0$），$F_1,F_2$ 为其焦点，"
        r"平面内一点 $P$ 满足 $PF_2\perp F_1F_2$，且 $\lvert PF_2\rvert=\lvert F_1F_2\rvert$，"
        r"线段 $PF_1,PF_2$ 分别交椭圆于点 $A,B$，若 $\lvert PA\rvert=\lvert AF_1\rvert$，"
        r"则 $\dfrac{\lvert BF_2\rvert}{\lvert PF_2\rvert}=$ ____"
    ),
    'opts': [],
    'answer': r"$\dfrac{\sqrt2}4$",
    'analysis': (
        r"$\lvert PA\rvert=\lvert AF_1\rvert$ 说明 $A$ 是 $PF_1$ 中点；取 $P(c,2c)$ 得 $A(0,c)$ 在椭圆上 ⟹ $b=c$、$a=\sqrt2c$；"
        r"再求直线 $x=c$ 与椭圆的交点 $B$ 即得比值。"
    ),
    'solution': (
        r"取 $F_1(-c,0)$、$F_2(c,0)$，由 $PF_2\perp F_1F_2$ 且 $\lvert PF_2\rvert=\lvert F_1F_2\rvert=2c$，可设 $P(c,2c)$．" "\n"
        r"**第一步：定 $a,b$**" "\n"
        r"$\lvert PA\rvert=\lvert AF_1\rvert$ 且 $A$ 在 $PF_1$ 上 ⟹ $A$ 是 $PF_1$ 的中点：" "\n"
        r"$A=\left(\dfrac{c-c}2,\dfrac{2c+0}2\right)=(0,c)$．" "\n"
        r"$A$ 在椭圆上：$\dfrac{0}{a^{2}}+\dfrac{c^{2}}{b^{2}}=1\Rightarrow b=c$，于是 $a^{2}=b^{2}+c^{2}=2c^{2}$，$a=\sqrt2c$．" "\n"
        r"**第二步：求 $B$**" "\n"
        r"$PF_2$ 是直线 $x=c$，代入椭圆：$\dfrac{c^{2}}{2c^{2}}+\dfrac{y^{2}}{c^{2}}=1\Rightarrow\dfrac12+\dfrac{y^{2}}{c^{2}}=1\Rightarrow y=\dfrac c{\sqrt2}$．" "\n"
        r"故 $\lvert BF_2\rvert=\dfrac c{\sqrt2}$，而 $\lvert PF_2\rvert=2c$．" "\n"
        r"**第三步：比值**" "\n"
        r"$\dfrac{\lvert BF_2\rvert}{\lvert PF_2\rvert}=\dfrac{c/\sqrt2}{2c}=\dfrac1{2\sqrt2}=\dfrac{\sqrt2}4$．"
    ),
    'review': (
        r"★ 题干、答案完整 ✓（**详解提取不全**，上述为我独立推导）。" "\n"
        r"ref_bank 存 `2/4`，实为 $\frac{\sqrt2}4$（**根号丢失**）。" "\n"
        r"**判定依据**：$\frac{\sqrt2}4=0.3536$；若按字面 $\frac24=0.5$，代入我的坐标体系不成立 ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **$P(c,2c)$**：$PF_2\perp F_1F_2$（$F_1F_2$ 在 $x$ 轴上，$PF_2$ 竖直）✓✓；$\lvert PF_2\rvert=2c=\lvert F_1F_2\rvert$ ✓✓✓" "\n"
        r"② **$A$ 是 $PF_1$ 中点**：$P(c,2c)$、$F_1(-c,0)$ ⟹ 中点 $(0,c)$ ✓✓✓" "\n"
        r"③ **$b=c$**：$\frac{c^{2}}{b^{2}}=1$ ✓✓✓" "\n"
        r"④ **$a=\sqrt2c$**：$a^{2}=b^{2}+c^{2}=2c^{2}$ ✓✓✓" "\n"
        r"⑤ **$B$ 在椭圆上**：取 $c=1$，则 $a=\sqrt2$、$b=1$，椭圆 $\frac{x^{2}}2+y^{2}=1$。" "\n"
        r"$x=1$：$y^{2}=1-\frac12=\frac12$，$y=0.7071$ ✓ **$\lvert BF_2\rvert=\frac1{\sqrt2}=0.7071$** ✓✓✓" "\n"
        r"$\lvert PF_2\rvert=2$ ⟹ 比值 $=\frac{0.7071}2=0.3536=\frac{\sqrt2}4$ ✓✓✓" "\n"
        r"⑥ **检验 $A$ 在线段 $PF_1$ 上**：$A=(0,1)$，$P=(1,2)$、$F_1=(-1,0)$；$A$ 确实是中点且在线段上 ✓✓" "\n"
        r"检验 $B$ 在线段 $PF_2$ 上：$B=(1,0.7071)$，$P=(1,2)$、$F_2=(1,0)$；$0<0.7071<2$ ✓✓✓" "\n"
        r"⑦ **$A,B$ 确在椭圆上**：$A(0,1)$：$0+1=1$ ✓；$B(1,0.7071)$：$\frac12+0.5=1$ ✓✓✓" "\n"
        r"**答案 $\frac{\sqrt2}4$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（第一定义 + 中点条件）**：" "\n"
        r"① ⭐⭐ **「$\lvert PA\rvert=\lvert AF_1\rvert$」就是「$A$ 是 $PF_1$ 中点」** —— " "\n"
        r"看到这种条件立刻取中点坐标代入曲线方程，一步定出 $a,b$ 的关系；" "\n"
        r"② ⭐ **把图形放在最方便的坐标**：$PF_2\perp F_1F_2$ 意味着 $P$ 在 $F_2$ 正上方，取 $P(c,2c)$ 使所有计算变成简单整数比；" "\n"
        r"③ ⭐ **本题的连锁反应**：$A(0,c)$ 在椭圆上 ⟹ $b=c$ ⟹ $a=\sqrt2c$ ⟹ $e=\frac1{\sqrt2}$ —— " "\n"
        r"三个量一次全定，后面 $B$ 只需解一元方程；" "\n"
        r"④ ⚠ **$B$ 必须在「线段」$PF_2$ 上**，解出的 $y$ 要检查落在 $0$ 与 $2c$ 之间（本题 $\frac c{\sqrt2}$ ✓）；" "\n"
        r"⑤ ⚠ **答案 $\frac{\sqrt2}4$ 被提取成 `2/4`** —— 本项目已第 N 次遇到，**凡是分子分母都是小整数，先怀疑根号**。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-327'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-327-E1',
}

T327_V1 = {
    'type': '填空',
    'stem_text': (
        r"已知双曲线 $\dfrac{x^{2}}{a^{2}}-\dfrac{y^{2}}{b^{2}}=1$（$a>0,b>0$）的左、右焦点分别为 $F_1,F_2$，"
        r"过 $F_1$ 且垂直于 $x$ 轴的直线与该双曲线的左支交于 $A,B$ 两点，$AF_2,BF_2$ 分别交 $y$ 轴于 $P,Q$ 两点，"
        r"若 $\triangle PQF_2$ 的周长为 $16$，则 $\dfrac{b^{2}}{a+1}$ 的最大值为 ____"
    ),
    'opts': [],
    'answer': r"$4$",
    'analysis': (
        r"$P,Q$ 恰是 $AF_2,BF_2$ 的中点（$y$ 轴平分 $F_1F_2$ 对应的横坐标），故 $\lvert PQ\rvert=\frac12\lvert AB\rvert$、"
        r"$\lvert PF_2\rvert+\lvert QF_2\rvert=\lvert AF_2\rvert$；又 $\lvert AF_1\rvert=\frac{b^{2}}a$，"
        r"用定义 $\lvert AF_2\rvert=2a+\frac{b^{2}}a$，周长 $=2a+\frac{2b^{2}}a=16$。"
    ),
    'solution': (
        r"过 $F_1(-c,0)$ 作 $x=-c$，与左支交点满足 $\dfrac{c^{2}}{a^{2}}-\dfrac{y^{2}}{b^{2}}=1$：" "\n"
        r"$\dfrac{y^{2}}{b^{2}}=\dfrac{c^{2}-a^{2}}{a^{2}}=\dfrac{b^{2}}{a^{2}}\Rightarrow y=\pm\dfrac{b^{2}}a$，" "\n"
        r"故 $A\!\left(-c,\dfrac{b^{2}}a\right)$、$B\!\left(-c,-\dfrac{b^{2}}a\right)$，$\lvert AB\rvert=\dfrac{2b^{2}}a$．" "\n"
        r"**第一步：$P,Q$ 是中点**" "\n"
        r"$A$ 的横坐标 $-c$、$F_2$ 的横坐标 $c$，$y$ 轴（$x=0$）恰在正中间 ⟹ 交点 $P$ 是 $AF_2$ 的中点；同理 $Q$ 是 $BF_2$ 的中点．" "\n"
        r"于是 $PQ$ 是 $\triangle AF_2B$ 的中位线：$\lvert PQ\rvert=\dfrac12\lvert AB\rvert=\dfrac{b^{2}}a$，" "\n"
        r"且 $\lvert PF_2\rvert+\lvert QF_2\rvert=\dfrac12\lvert AF_2\rvert+\dfrac12\lvert BF_2\rvert=\lvert AF_2\rvert$（由对称性 $\lvert AF_2\rvert=\lvert BF_2\rvert$）．" "\n"
        r"**第二步：用定义求 $\lvert AF_2\rvert$**" "\n"
        r"$\lvert AF_1\rvert$ 是 $A$ 到 $F_1(-c,0)$ 的竖直线段长 $=\dfrac{b^{2}}a$；$A$ 在左支，" "\n"
        r"由定义 $\lvert AF_2\rvert-\lvert AF_1\rvert=2a\Rightarrow\lvert AF_2\rvert=2a+\dfrac{b^{2}}a$．" "\n"
        r"**第三步：周长条件**" "\n"
        r"周长 $=\lvert PQ\rvert+\lvert PF_2\rvert+\lvert QF_2\rvert=\dfrac{b^{2}}a+2a+\dfrac{b^{2}}a=2a+\dfrac{2b^{2}}a=16$，" "\n"
        r"即 $a+\dfrac{b^{2}}a=8\Rightarrow b^{2}=a(8-a)$．（需 $0<a<8$ 且 $b^{2}>0$）" "\n"
        r"**第四步：求最大值**" "\n"
        r"$f(a)=\dfrac{b^{2}}{a+1}=\dfrac{a(8-a)}{a+1}=\dfrac{8a-a^{2}}{a+1}$，" "\n"
        r"$f'(a)=\dfrac{(8-2a)(a+1)-(8a-a^{2})}{(a+1)^{2}}=\dfrac{-a^{2}-2a+8}{(a+1)^{2}}$．" "\n"
        r"令分子为零：$a^{2}+2a-8=0\Rightarrow a=2$（舍 $a=-4$）．" "\n"
        r"$f(2)=\dfrac{16-4}{3}=4$，故最大值为 $4$．"
    ),
    'review': (
        r"★ 题干、答案完整 ✓（**详解未提取**，上述为我独立推导）。答案与原书标注 $4$ 一致 ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **$\lvert AB\rvert=\frac{2b^{2}}a$**：$y=\pm\frac{b^{2}}a$（通径的一半是 $\frac{b^{2}}a$，整条通径 $=\frac{2b^{2}}a$）✓✓✓" "\n"
        r"② **$P$ 是 $AF_2$ 中点**：$x$ 从 $-c$ 到 $c$，$x=0$ 在正中间 ✓✓✓" "\n"
        r"③ **$PQ$ 是中位线**：$P,Q$ 为 $AF_2,BF_2$ 中点 ⟹ $PQ\parallel AB$ 且 $\lvert PQ\rvert=\frac12\lvert AB\rvert$ ✓✓✓" "\n"
        r"④ **$\lvert AF_2\rvert=2a+\frac{b^{2}}a$**：$\lvert AF_1\rvert=\frac{b^{2}}a$（竖直距离）✓✓，左支 $\lvert AF_2\rvert-\lvert AF_1\rvert=2a$ ✓✓✓" "\n"
        r"⑤ **周长 $=2a+\frac{2b^{2}}a$**：$\frac{b^{2}}a+(2a+\frac{b^{2}}a)=2a+\frac{2b^{2}}a$ ✓✓✓" "\n"
        r"⑥ **$f'(a)$**：$\frac{d}{da}\frac{8a-a^{2}}{a+1}=\frac{(8-2a)(a+1)-(8a-a^{2})}{(a+1)^{2}}$" "\n"
        r"$=\frac{8a+8-2a^{2}-2a-8a+a^{2}}{(a+1)^{2}}=\frac{-a^{2}-2a+8}{(a+1)^{2}}$ ✓✓✓" "\n"
        r"⑦ **$a=2$**：$a^{2}+2a-8=(a+4)(a-2)=0$ ⟹ $a=2$ ✓✓✓" "\n"
        r"⑧ **$f(2)=4$**：$\frac{16-4}{3}=\frac{12}3=4$ ✓✓✓" "\n"
        r"⑨ **数值检验**：$a=2$ ⟹ $b^{2}=2\times6=12$、$b=2\sqrt3$、$c^{2}=4+12=16$、$c=4$。" "\n"
        r"通径 $x=-4$：$y=\pm\frac{12}2=\pm6$ ⟹ $A(-4,6)$、$B(-4,-6)$，$\lvert AB\rvert=12$ ✓（$=\frac{2b^{2}}a=\frac{24}2=12$）" "\n"
        r"$P$ 是 $A(-4,6)$ 与 $F_2(4,0)$ 中点 $=(0,3)$；$Q=(0,-3)$；$\lvert PQ\rvert=6$ ✓（$=\frac{b^{2}}a=6$）" "\n"
        r"$\lvert PF_2\rvert=\sqrt{16+9}=5$、$\lvert QF_2\rvert=5$；周长 $=6+5+5=16$ ✓✓✓ **恰为题设**" "\n"
        r"$\frac{b^{2}}{a+1}=\frac{12}3=4$ ✓✓✓" "\n"
        r"取 $a=3$：$b^{2}=3\times5=15$，$\frac{15}4=3.75<4$ ✓ **确为最大**" "\n"
        r"取 $a=1$：$b^{2}=7$，$\frac72=3.5<4$ ✓✓✓" "\n"
        r"**答案 $4$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（通径 + 中点三角形）**：" "\n"
        r"① ⭐⭐ **过焦点且垂直于实轴的弦叫通径，半长 $=\frac{b^{2}}a$** —— 建议直接记住，省一次联立；" "\n"
        r"② ⭐ **「$y$ 轴平分 $[-c,c]$」⟹ 交点是中点** —— 出现「$AF_2$ 交 $y$ 轴于 $P$」这类条件，第一反应就是中点；" "\n"
        r"③ ⭐ **中位线把 $\lvert PQ\rvert$ 变成 $\frac12\lvert AB\rvert$、把两条焦半径之和变成 $\lvert AF_2\rvert$** —— " "\n"
        r"周长因此简化成 $2a+\frac{2b^{2}}a$，一个式子搞定；" "\n"
        r"④ ⭐ **焦半径用定义转**：左支上 $\lvert AF_2\rvert=2a+\lvert AF_1\rvert$，而 $\lvert AF_1\rvert$ 是通径半长，直接可算；" "\n"
        r"⑤ **最后是一元函数求最值**：$b^{2}=a(8-a)$ 代入后求导，$a=2$ 处取 $4$；" "\n"
        r"⑥ 检验：**取 $a=2$ 反算出全部坐标，验证周长恰为 $16$**（$6+5+5=16$ ✓），这是最硬的闭环。"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-327'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-327-V1',
}

T327_V3 = {
    'type': '填空',
    'stem_text': (
        r"设 $F_1,F_2$ 分别是椭圆 $\dfrac{x^{2}}{25}+\dfrac{y^{2}}{16}=1$ 的左、右焦点，$P$ 为椭圆上任意一点，"
        r"点 $M$ 的坐标为 $(6,4)$，则 $\lvert PM\rvert+\lvert PF_1\rvert$ 的最大值为 ____"
    ),
    'opts': [],
    'answer': r"$15$",
    'analysis': (
        r"用定义把 $\lvert PF_1\rvert$ 换成 $2a-\lvert PF_2\rvert=10-\lvert PF_2\rvert$，"
        r"于是原式 $=10+(\lvert PM\rvert-\lvert PF_2\rvert)\le10+\lvert MF_2\rvert$，等号当 $P$ 在 $MF_2$ 延长线上。"
    ),
    'solution': (
        r"由 $a^{2}=25,b^{2}=16$ 得 $a=5$、$c=\sqrt{25-16}=3$，故 $F_1(-3,0)$、$F_2(3,0)$．" "\n"
        r"**第一步：用定义换掉 $\lvert PF_1\rvert$**" "\n"
        r"由椭圆定义 $\lvert PF_1\rvert+\lvert PF_2\rvert=2a=10$，故 $\lvert PF_1\rvert=10-\lvert PF_2\rvert$，" "\n"
        r"$\lvert PM\rvert+\lvert PF_1\rvert=10+\bigl(\lvert PM\rvert-\lvert PF_2\rvert\bigr)$．" "\n"
        r"**第二步：用三角形不等式**" "\n"
        r"由三角形不等式 $\lvert PM\rvert-\lvert PF_2\rvert\le\lvert MF_2\rvert$，" "\n"
        r"$\lvert MF_2\rvert=\sqrt{(6-3)^{2}+(4-0)^{2}}=\sqrt{9+16}=5$，" "\n"
        r"故 $\lvert PM\rvert+\lvert PF_1\rvert\le10+5=15$．" "\n"
        r"**第三步：等号可达**" "\n"
        r"等号成立当且仅当 $P,F_2,M$ 共线且 $F_2$ 在 $P,M$ 之间（即 $P$ 在射线 $MF_2$ 的反向延长线上）；" "\n"
        r"直线 $MF_2$ 与椭圆必相交，故最大值 $15$ 可以取到．"
    ),
    'review': (
        r"★ 题干、答案完整 ✓。原书 p303 详解：" "\n"
        r"「由椭圆方程可得：$a=5,b=4,c=3$。∴ $F_1(-3,0),F_2(3,0)$，由椭圆的定义可得：$\lvert PF_1\rvert+\lvert PF_2\rvert=2a=10$，" "\n"
        r"∴ $\lvert PM\rvert+\lvert PF_1\rvert=\lvert PM\rvert+2a-\lvert PF_2\rvert=10+(\lvert PM\rvert-\lvert PF_2\rvert)\le10+\lvert MF_2\rvert=10+3+4=15$。" "\n"
        r"则 $\lvert PM\rvert+\lvert PF_1\rvert$ 的最大值为 15」" "\n"
        r"—— **$a=5,b=4,c=3$、换元、$\le10+\lvert MF_2\rvert$、结果 $15$ 全部与我的推导一致** ✓✓✓" "\n"
        r"（原书写的「$10+3+4=15$」是把 $\lvert MF_2\rvert=5$ 拆成横纵差 $3,4$，实际 $\lvert MF_2\rvert=\sqrt{3^{2}+4^{2}}=5$，结果相同）" "\n"
        r"**独立验算**：" "\n"
        r"① **$a=5,b=4,c=3$**：$c=\sqrt{25-16}=3$ ✓✓✓" "\n"
        r"② **$\lvert PF_1\rvert=10-\lvert PF_2\rvert$**：定义 ✓✓✓" "\n"
        r"③ **$\lvert MF_2\rvert=5$**：$M(6,4)$、$F_2(3,0)$ ⟹ $\sqrt{9+16}=5$ ✓✓✓" "\n"
        r"④ **三角形不等式方向**：$\lvert PM\rvert\le\lvert PF_2\rvert+\lvert F_2M\rvert$ ⟹ $\lvert PM\rvert-\lvert PF_2\rvert\le\lvert MF_2\rvert$ ✓✓✓" "\n"
        r"⑤ **等号可达性（关键）**：需 $P$ 在直线 $MF_2$ 上且在 $F_2$ 的另一侧。" "\n"
        r"直线 $MF_2$：过 $F_2(3,0)$、$M(6,4)$，方向 $(3,4)$，斜率 $\frac43$。参数式 $(3+3t,4t)$。" "\n"
        r"$t=1$ 给 $M(6,4)$；$t<0$ 给 $F_2$ 另一侧的点。代入椭圆：$\frac{(3+3t)^{2}}{25}+\frac{16t^{2}}{16}=1$" "\n"
        r"⟹ $\frac{9(1+t)^{2}}{25}+t^{2}=1$ ⟹ $9(1+2t+t^{2})+25t^{2}=25$ ⟹ $34t^{2}+18t-16=0$ ⟹ $17t^{2}+9t-8=0$" "\n"
        r"$t=\frac{-9\pm\sqrt{81+544}}{34}=\frac{-9\pm25}{34}$ ⟹ $t=\frac{16}{34}=0.4706$ 或 $t=-1$。" "\n"
        r"$t=-1$ 给 $P=(0,-4)$：检验 $\frac{0}{25}+\frac{16}{16}=1$ ✓✓ **在椭圆上**，且在 $F_2$ 另一侧（$t<0$）✓✓✓" "\n"
        r"此时 $\lvert PM\rvert=\sqrt{36+64}=10$、$\lvert PF_2\rvert=\sqrt{9+16}=5$；$\lvert PM\rvert-\lvert PF_2\rvert=5=\lvert MF_2\rvert$ ✓✓✓ **取等**" "\n"
        r"$\lvert PF_1\rvert=10-5=5$（检验：$P(0,-4)$ 到 $F_1(-3,0)$ $=\sqrt{9+16}=5$ ✓✓✓）" "\n"
        r"$\lvert PM\rvert+\lvert PF_1\rvert=10+5=15$ ✓✓✓ **恰为最大值**" "\n"
        r"⑥ **另取一点对照**：$P=(5,0)$（右顶点）。$\lvert PM\rvert=\sqrt{1+16}=4.123$、$\lvert PF_1\rvert=8$；和 $=12.123<15$ ✓ 非最大" "\n"
        r"**答案 $15$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（到一个焦点距离 ⟷ 到另一焦点距离）**：" "\n"
        r"① ⭐⭐ **椭圆上「$\lvert PF_1\rvert$」随时可以换成「$2a-\lvert PF_2\rvert$」** —— " "\n"
        r"凡是求「$\lvert PM\rvert+\lvert PF_{\text{某}}\rvert$」的最值，**一律先换到「与定点 $M$ 同侧」的那个焦点**，" "\n"
        r"这样才能凑出 $\lvert PM\rvert-\lvert PF_2\rvert$（差）或 $\lvert PM\rvert+\lvert PF_2\rvert$（和）；" "\n"
        r"② ⭐ **差的放大用 $\lvert PM\rvert-\lvert PF_2\rvert\le\lvert MF_2\rvert$；和的缩小用 $\lvert PM\rvert+\lvert PF_2\rvert\ge\lvert MF_2\rvert$** —— " "\n"
        r"记忆法：**求最大用「差 $\le$」，求最小用「和 $\ge$」**；" "\n"
        r"③ ⚠ **必须验证等号可达**：解直线与椭圆的交点，确认参数落在需要的那一侧（本题 $t=-1$ 给出 $P(0,-4)$ ✓）；" "\n"
        r"④ ⭐ **双曲线同理**：$\bigl\lvert\lvert PF_1\rvert-\lvert PF_2\rvert\bigr\rvert=2a$，换成和或差后用同样手法；" "\n"
        r"⑤ **检验**：把取等点代回去算一遍（本题 $10+5=15$ ✓），并另取一点对照（$12.123<15$ ✓）。"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-327'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-327-V3',
}

T329_V3 = {
    'type': '填空',
    'stem_text': (
        r"在平面直角坐标系中，$O$ 为坐标原点，$M,N$ 是双曲线 $\dfrac{x^{2}}2-\dfrac{y^{2}}4=1$ 上的两个动点，"
        r"动点 $P$ 满足 $\vec{OP}=2\vec{OM}-\vec{ON}$，直线 $OM$ 与直线 $ON$ 斜率之积为 $2$，"
        r"已知平面内存在两定点 $F_1,F_2$，使得 $\bigl\lvert\lvert PF_1\rvert-\lvert PF_2\rvert\bigr\rvert$ 为定值，"
        r"则该定值为 ____"
    ),
    'opts': [],
    'answer': r"$2\sqrt{10}$",
    'analysis': (
        r"设 $M(x_1,y_1),N(x_2,y_2)$，由 $k_1k_2=2$ 得 $y_1y_2=2x_1x_2$；"
        r"把 $P(2x_1-x_2,\,2y_1-y_2)$ 的坐标平方组合，消去 $y_1y_2-2x_1x_2=0$ 得 $2x^{2}-y^{2}=20$，即 $a=\sqrt{10}$。"
    ),
    'solution': (
        r"设 $M(x_1,y_1)$、$N(x_2,y_2)$，则 $P(2x_1-x_2,\;2y_1-y_2)$．记 $P=(x,y)$．" "\n"
        r"由 $k_{OM}k_{ON}=2$：$\dfrac{y_1}{x_1}\cdot\dfrac{y_2}{x_2}=2\Rightarrow y_1y_2=2x_1x_2$．" "\n"
        r"$M,N$ 在 $\dfrac{x^{2}}2-\dfrac{y^{2}}4=1$ 上：$2x_1^{2}-y_1^{2}=4$、$2x_2^{2}-y_2^{2}=4$．" "\n"
        r"计算 $2x^{2}-y^{2}$：" "\n"
        r"$2x^{2}=2(2x_1-x_2)^{2}=8x_1^{2}+2x_2^{2}-8x_1x_2$，$\quad y^{2}=(2y_1-y_2)^{2}=4y_1^{2}+y_2^{2}-4y_1y_2$．" "\n"
        r"$2x^{2}-y^{2}=(8x_1^{2}-4y_1^{2})+(2x_2^{2}-y_2^{2})-4(2x_1x_2-y_1y_2)$" "\n"
        r"$=4\cdot4+4-4\cdot0=20$．" "\n"
        r"故 $P$ 在双曲线 $2x^{2}-y^{2}=20$，即 $\dfrac{x^{2}}{10}-\dfrac{y^{2}}{20}=1$ 上，" "\n"
        r"由双曲线定义 $\bigl\lvert\lvert PF_1\rvert-\lvert PF_2\rvert\bigr\rvert=2a=2\sqrt{10}$．"
    ),
    'review': (
        r"★ 题干、答案完整 ✓。原书 p305 详解：" "\n"
        r"「即 $x=2x_1-x_2$，$y=2y_1-y_2$，∵ 点 $M,N$ 在双曲线 $\frac{x^{2}}2-\frac{y^{2}}4=1$ 上，所以 $2x_1^{2}-y_1^{2}=4$，$2x_2^{2}-y_2^{2}=4$，" "\n"
        r"故 $2x^{2}-y^{2}=(8x_1^{2}+2x_2^{2}-8x_1x_2)-(4y_1^{2}+y_2^{2}-4y_1y_2)=20-4(2x_1x_2-y_1y_2)$，" "\n"
        r"设 $k_1,k_2$ 分别为直线 $OM,ON$ 的斜率，根据题意可知 $k_1k_2=2$，∴ $y_1y_2-2x_1x_2=0$，∴ $2x^{2}-y^{2}=20$，" "\n"
        r"所以 $P$ 在双曲线 $2x^{2}-y^{2}=20$ 上；设该双曲线的左、右焦点为 $F_1,F_2$，由双曲线的定义可推断出" "\n"
        r"$\lvert\lvert PF_1\rvert-\lvert PF_2\rvert\rvert$ 为定值，该定值为 $2\sqrt{10}$」" "\n"
        r"—— **$2x^{2}-y^{2}=20-4(2x_1x_2-y_1y_2)$、$k_1k_2=2$、$2x^{2}-y^{2}=20$、定值 $2\sqrt{10}$ 全部与我的推导一致** ✓✓✓" "\n"
        r"**⚠ 答案还原**：ref_bank 存 `2 10`，实为 $2\sqrt{10}$（**根号丢失**）。" "\n"
        r"**判定依据**：$P$ 的轨迹是 $\frac{x^{2}}{10}-\frac{y^{2}}{20}=1$，$a^{2}=10$ ⟹ $2a=2\sqrt{10}=6.325$；" "\n"
        r"若按字面「$210$」或「$2\cdot10=20$」都不可能是这个双曲线的 $2a$ ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **$2x^{2}-y^{2}$ 的展开**：$2(2x_1-x_2)^{2}=2(4x_1^{2}-4x_1x_2+x_2^{2})=8x_1^{2}-8x_1x_2+2x_2^{2}$ ✓✓✓" "\n"
        r"$(2y_1-y_2)^{2}=4y_1^{2}-4y_1y_2+y_2^{2}$ ✓✓✓" "\n"
        r"$2x^{2}-y^{2}=(8x_1^{2}+2x_2^{2}-8x_1x_2)-(4y_1^{2}+y_2^{2}-4y_1y_2)$" "\n"
        r"$=(8x_1^{2}-4y_1^{2})+(2x_2^{2}-y_2^{2})-8x_1x_2+4y_1y_2$" "\n"
        r"$=4(2x_1^{2}-y_1^{2})+(2x_2^{2}-y_2^{2})-4(2x_1x_2-y_1y_2)=4\cdot4+4-0=20$ ✓✓✓" "\n"
        r"（与 p305 原文的 $20-4(2x_1x_2-y_1y_2)$ 完全一致 ✓）" "\n"
        r"② **$k_1k_2=2$ ⟹ $y_1y_2=2x_1x_2$** ✓✓✓ ⟹ $2x_1x_2-y_1y_2=0$ ✓✓✓" "\n"
        r"③ **$a^{2}=10$**：$2x^{2}-y^{2}=20$ ⟹ $\frac{x^{2}}{10}-\frac{y^{2}}{20}=1$ ✓✓；$a=\sqrt{10}$、$b=2\sqrt5$、$c=\sqrt{30}$ ✓✓✓" "\n"
        r"④ **定值 $=2a=2\sqrt{10}$** ✓✓✓" "\n"
        r"⑤ **数值检验**：取 $M$ 使 $x_1=2$：$4-\frac{y_1^{2}}4=1$ ⟹ $y_1^{2}=12$，$y_1=2\sqrt3=3.464$。$k_1=\frac{3.464}2=1.732$。" "\n"
        r"需 $k_2=\frac2{1.732}=1.1547$，且 $N$ 在双曲线上：$\frac{x_2^{2}}2-\frac{y_2^{2}}4=1$、$y_2=1.1547x_2$。" "\n"
        r"$\frac{x_2^{2}}2-\frac{1.3333x_2^{2}}4=1$ ⟹ $0.5x_2^{2}-0.3333x_2^{2}=1$ ⟹ $0.16667x_2^{2}=1$ ⟹ $x_2^{2}=6$，$x_2=2.449$、$y_2=2.828$。" "\n"
        r"$P=(2\cdot2-2.449,\;2\cdot3.464-2.828)=(1.551,\;4.100)$。" "\n"
        r"检验 $2x^{2}-y^{2}=2(2.406)-16.81=4.812-16.81=-11.998$ —— ✗ **不等于 $20$**" "\n"
        r"（⚠ 注意：$k_1k_2=2$ 需 $\frac{y_1y_2}{x_1x_2}=2$，即 $y_1y_2=2x_1x_2$。此处 $y_1y_2=3.464\times2.828=9.798$、$2x_1x_2=2\cdot2\cdot2.449=9.796$ ✓ 满足。" "\n"
        r"但 $2x^{2}-y^{2}$ 算得 $-12$ 而非 $20$，说明**我的展开式用错了 $M,N$ 的方程形式**）" "\n"
        r"**复核**：我上面用的是 $2x_1^{2}-y_1^{2}=4$（即 $\frac{x^{2}}2-\frac{y^{2}}4=1$ 乘 $4$）。" "\n"
        r"$M(2,3.464)$：$2\cdot4-12=-4\neq4$ ✗ —— **$M$ 不在双曲线上！**" "\n"
        r"（$\frac{2^{2}}2-\frac{12}4=2-3=-1\neq1$，我之前解错了：应由 $\frac{4}2-\frac{y^{2}}4=1$ ⟹ $2-\frac{y^{2}}4=1$ ⟹ $y^{2}=4$，$y=2$）" "\n"
        r"**重算**：$M(2,2)$，$k_1=1$。需 $k_2=2$，$N$：$\frac{x_2^{2}}2-\frac{4x_2^{2}}4=1$ ⟹ $0.5x_2^{2}-x_2^{2}=1$ ⟹ $-0.5x_2^{2}=1$ **无实数解** ✗" "\n"
        r"（$k_2=2$ 时 $N$ 不在双曲线上 —— 因为双曲线 $\frac{x^{2}}2-\frac{y^{2}}4=1$ 的渐近线斜率 $\pm\sqrt2\approx1.414$，" "\n"
        r"**斜率 $2>\sqrt2$ 的直线不与该双曲线相交**）" "\n"
        r"改取 $k_1=1.2$：需 $k_2=\frac2{1.2}=1.6667>\sqrt2$ ✗ 同样不行。" "\n"
        r"改取 $k_1=1.6$：$k_2=1.25<\sqrt2$ ✓。$M$：$\frac{x_1^{2}}2-\frac{2.56x_1^{2}}4=1$ ⟹ $0.5x_1^{2}-0.64x_1^{2}=1$ ⟹ $-0.14x_1^{2}=1$ ✗（$k_1=1.6>\sqrt2$ 也不行）" "\n"
        r"⟹ **两根斜率必须一个 $<\sqrt2$、一个 $>\sqrt2$ 才能分别落在双曲线上**，但乘积要为 $2>\sqrt2\cdot\sqrt2=2$…" "\n"
        r"实际上 $k_1k_2=2$ 且 $\lvert k_1\rvert,\lvert k_2\rvert<\sqrt2$ 才都有交点，此时 $\lvert k_1k_2\rvert<2$ —— **取等时两直线都趋于渐近线**。" "\n"
        r"⟹ **题设 $k_1k_2=2$ 恰好是临界值**，与 M-T-329-V3 相邻的 M-T-329 系列中已注明「条件瑕疵」同类；" "\n"
        r"但**代数推导严密**（$2x^{2}-y^{2}=20$ 的每一步都是恒等变形），答案 $2\sqrt{10}$ 确定，**按此录入**。"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-329'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-329-V3',
}

T335_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知点 $A$ 是抛物线 $x^{2}=4y$ 的对称轴与准线的交点，$F$ 为抛物线的焦点，"
        r"点 $P$ 在抛物线上且满足 $\lvert PA\rvert=m\lvert PF\rvert$，若 $m$ 取最大值时，"
        r"点 $P$ 恰好在以 $A,F$ 为焦点的双曲线上，则双曲线的离心率为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac{\sqrt3+1}2$"),
        ('B', r"$\sqrt2+1$"),
        ('C', r"$\dfrac{\sqrt5+1}2$"),
        ('D', r"$\dfrac{\sqrt2+1}2$"),
    ],
    'answer': 'B',
    'analysis': (
        r"由定义 $\lvert PF\rvert=\lvert PN\rvert$（$N$ 为 $P$ 到准线的垂足），故 $m=\frac{\lvert PA\rvert}{\lvert PN\rvert}=\frac1{\sin\alpha}$；"
        r"$m$ 最大 ⟺ $\sin\alpha$ 最小 ⟺ $PA$ 与抛物线相切，解得 $P(2,1)$。"
    ),
    'solution': (
        r"抛物线 $x^{2}=4y$：焦点 $F(0,1)$，准线 $y=-1$，对称轴是 $y$ 轴，故 $A=(0,-1)$．" "\n"
        r"**第一步：把 $m$ 写成角的函数**" "\n"
        r"过 $P$ 作准线的垂线，垂足 $N$。由抛物线定义 $\lvert PF\rvert=\lvert PN\rvert$，" "\n"
        r"故 $\lvert PA\rvert=m\lvert PF\rvert=m\lvert PN\rvert$，即 $\dfrac{\lvert PN\rvert}{\lvert PA\rvert}=\dfrac1m$．" "\n"
        r"因 $PN\perp$ 准线、$A$ 在准线上，$\triangle PNA$ 是直角三角形（直角在 $N$）。设 $\angle PAN=\alpha$，" "\n"
        r"则 $\sin\alpha=\dfrac{\lvert PN\rvert}{\lvert PA\rvert}=\dfrac1m$，即 $m=\dfrac1{\sin\alpha}$．" "\n"
        r"**第二步：$m$ 最大时的 $P$**" "\n"
        r"$m$ 最大 ⟺ $\sin\alpha$ 最小 ⟺ 直线 $PA$ 与抛物线相切。" "\n"
        r"设 $PA$：$y=kx-1$（过 $A$），代入 $x^{2}=4y$：" "\n"
        r"$x^{2}=4(kx-1)\Rightarrow x^{2}-4kx+4=0$，相切 ⟹ $\Delta=16k^{2}-16=0\Rightarrow k=\pm1$．" "\n"
        r"取 $k=1$：$x^{2}-4x+4=0\Rightarrow x=2$，$y=1$，即 $P(2,1)$．" "\n"
        r"**第三步：求双曲线的 $e$**" "\n"
        r"$\lvert PA\rvert=\sqrt{(2-0)^{2}+(1+1)^{2}}=\sqrt{4+4}=2\sqrt2$，$\lvert PF\rvert=\sqrt{4+0}=2$．" "\n"
        r"以 $A,F$ 为焦点的双曲线：焦距 $2c=\lvert AF\rvert=2$，故 $c=1$；" "\n"
        r"实轴长 $2a=\bigl\lvert\lvert PA\rvert-\lvert PF\rvert\bigr\rvert=2\sqrt2-2=2(\sqrt2-1)$，故 $a=\sqrt2-1$．" "\n"
        r"$e=\dfrac ca=\dfrac1{\sqrt2-1}=\sqrt2+1$，故选 **B**．"
    ),
    'review': (
        r"★ 题干、答案完整 ✓。原书 p309 详解：" "\n"
        r"「过 $P$ 作准线的垂线，垂足为 $N$，则由抛物线的定义可得 $\lvert PN\rvert=\lvert PB\rvert$，∵ $\lvert PA\rvert=m\lvert PB\rvert$，" "\n"
        r"∴ $\lvert PA\rvert=m\lvert PN\rvert$ ∴ $\frac1m=\frac{\lvert PN\rvert}{\lvert PA\rvert}$，设 $PA$ 的倾斜角为 $\alpha$，则 $\sin\alpha=\frac1m$，" "\n"
        r"当 $m$ 取得最大值时，$\sin\alpha$ 最小，此时直线 $PA$ 与抛物线相切，设直线 $PA$ 的方程为 $y=kx-1$，代入 $x^{2}=4y$，" "\n"
        r"可得 $x^{2}=4(kx-1)$，即 $x^{2}-4kx+4=0$，∴ $\triangle=16k^{2}-16=0$，∴ $k=\pm1$，∴ $P(2,1)$，" "\n"
        r"∴ 双曲线的实轴长为 $PA-PB=2(\sqrt2-1)$，∴ 双曲线的离心率为 $\frac2{2(\sqrt2-1)}=\sqrt2+1$。故选 B」" "\n"
        r"—— **$\frac1m=\sin\alpha$、相切得 $k=\pm1$、$P(2,1)$、实轴长 $2(\sqrt2-1)$、$e=\sqrt2+1$ 全部与我的推导一致** ✓✓✓" "\n"
        r"（原书把焦点记作 $B$，与本题干的 $F$ 对应；$\frac2{2(\sqrt2-1)}$ 即 $\frac{2c}{2a}$，其中 $2c=\lvert AF\rvert=2$）" "\n"
        r"**⚠ 选项还原**：PDF 提取为 `A.3+1 B.2+1 / C.5+1 2+1 / D.2 2 2`（根号全丢、分式错位）。" "\n"
        r"**判定依据**：详解末行 $\frac2{2(\sqrt2-1)}=\frac1{\sqrt2-1}=\sqrt2+1\approx2.414$，对应选项 B ✓✓✓" "\n"
        r"（选项 C $\frac{\sqrt5+1}2\approx1.618$ 是黄金比，命题人常用的干扰项；A $\frac{\sqrt3+1}2\approx1.366$、D $\frac{\sqrt2+1}2\approx1.207$ 均不符）" "\n"
        r"**独立验算**：" "\n"
        r"① **$A=(0,-1)$、$F=(0,1)$**：$x^{2}=4y$ ⟹ $p=2$、焦点 $(0,1)$、准线 $y=-1$；对称轴 $x=0$ 与准线交于 $(0,-1)$ ✓✓✓" "\n"
        r"② **$\triangle PNA$ 直角在 $N$**：$PN\perp$ 准线（水平线 $y=-1$）⟹ $PN$ 竖直；$A,N$ 都在准线上 ⟹ $AN$ 水平 ✓✓✓" "\n"
        r"③ **$\sin\alpha=\frac{\lvert PN\rvert}{\lvert PA\rvert}$**：$\alpha=\angle PAN$，对边 $PN$、斜边 $PA$ ✓✓✓" "\n"
        r"④ **相切**：$x^{2}-4kx+4=0$，$\Delta=16k^{2}-16=0$ ⟹ $k=\pm1$ ✓✓✓" "\n"
        r"$k=1$：$x^{2}-4x+4=(x-2)^{2}=0$ ⟹ $x=2$、$y=\frac{4}4=1$ ⟹ $P(2,1)$ ✓✓✓" "\n"
        r"⑤ **$\lvert PA\rvert=2\sqrt2$**：$P(2,1)$、$A(0,-1)$ ⟹ $\sqrt{4+4}=2\sqrt2$ ✓✓✓" "\n"
        r"**$\lvert PF\rvert=2$**：$P(2,1)$、$F(0,1)$ ⟹ $\sqrt{4+0}=2$ ✓✓✓" "\n"
        r"（也等于 $\lvert PN\rvert=1-(-1)=2$ ✓ 定义自洽）" "\n"
        r"⑥ **$m$ 的最大值**：$m=\frac{\lvert PA\rvert}{\lvert PF\rvert}=\frac{2\sqrt2}2=\sqrt2\approx1.414$。" "\n"
        r"取另一点 $P(4,4)$ 对照：$\lvert PA\rvert=\sqrt{16+25}=6.403$、$\lvert PF\rvert=\sqrt{16+9}=5$，$m=1.281<1.414$ ✓✓✓ **确为最大**" "\n"
        r"取 $P(1,\frac14)$：$\lvert PA\rvert=\sqrt{1+1.5625}=1.601$、$\lvert PF\rvert=\sqrt{1+0.5625}=1.25$，$m=1.281<1.414$ ✓✓✓" "\n"
        r"⑦ **$e=\sqrt2+1$**：$c=1$、$a=\sqrt2-1$，$e=\frac1{\sqrt2-1}=\frac{\sqrt2+1}{2-1}=\sqrt2+1\approx2.414$ ✓✓✓" "\n"
        r"⑧ **双曲线合法性**：$e>1$ ✓；$c>a$（$1>0.414$）✓✓✓" "\n"
        r"**答案 B（$\sqrt2+1$）正确** ✓" "\n"
        r"**⭐⭐ 通法（$\frac{\lvert PA\rvert}{\lvert PF\rvert}$ 型最值）**：" "\n"
        r"① ⭐⭐ **由抛物线定义 $\lvert PF\rvert=\lvert PN\rvert$，把比值化成 $\frac{\lvert PA\rvert}{\lvert PN\rvert}=\frac1{\sin\alpha}$** —— " "\n"
        r"$\alpha$ 是 $PA$ 与准线的夹角；**求比值最大 ⟺ 求 $\sin\alpha$ 最小 ⟺ 直线与抛物线相切**；" "\n"
        r"② ⭐ **相切条件用 $\Delta=0$**，设过定点 $A$ 的直线 $y=kx+b$ 代入，一次解出 $k$，进而得切点；" "\n"
        r"③ ⭐ **求双曲线 $e$ 只要 $2c$ 与 $2a$**：$2c$ 是两焦点距离（本题 $\lvert AF\rvert=2$）、" "\n"
        r"$2a=\bigl\lvert\lvert PA\rvert-\lvert PF\rvert\bigr\rvert$（到两焦点距离之差的绝对值）；" "\n"
        r"④ ⚠ **注意 $A$ 是准线与对称轴的交点**，它在准线上 —— 这才使 $\triangle PNA$ 成为直角三角形，是解题关键；" "\n"
        r"⑤ 检验：**另取两点算 $m$ 对照**（$1.281<1.414$ ✓），确认相切点确为最大。"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-335'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-335-E1',
}

T335_V3 = {
    'type': '填空',
    'stem_text': (
        r"已知椭圆 $C:\dfrac{x^{2}}{a^{2}}+\dfrac{y^{2}}{b^{2}}=1$（$a>b>0$）的左、右焦点分别为 $F_1,F_2$，"
        r"抛物线 $y^{2}=2px$ 的焦点与 $F_2$ 重合，若点 $P$ 为椭圆和抛物线的一个公共点"
        r"且 $\cos\angle PF_1F_2=\dfrac57$，则椭圆的离心率为 ____"
    ),
    'opts': [],
    'answer': r"$e=\dfrac12$ 或 $e=\dfrac13$",
    'analysis': (
        r"由抛物线定义 $n=\lvert PF_2\rvert=x_P+c$，而 $x_P=-c+m\cos\angle PF_1F_2$，故 $n=\frac57m$；"
        r"与 $m+n=2a$ 联立得 $m=\frac{7a}6,n=\frac{5a}6$，代入余弦定理得 $6e^{2}-5e+1=0$。"
    ),
    'solution': (
        r"由抛物线 $y^{2}=2px$ 的焦点 $\left(\frac p2,0\right)$ 与 $F_2(c,0)$ 重合，得 $p=2c$，准线 $x=-c$．" "\n"
        r"记 $m=\lvert PF_1\rvert$、$n=\lvert PF_2\rvert$、$e=\frac ca$．" "\n"
        r"**第一步：由抛物线定义得 $n=\frac57m$**" "\n"
        r"设 $\theta=\angle PF_1F_2$，则 $P$ 的横坐标 $x_P=-c+m\cos\theta=-c+\frac57m$．" "\n"
        r"由抛物线定义，$n$ 等于 $P$ 到准线 $x=-c$ 的距离：$n=x_P+c=\dfrac57m$．" "\n"
        r"**第二步：与椭圆定义联立**" "\n"
        r"$m+n=2a$，代入 $n=\frac57m$：$m\cdot\frac{12}7=2a\Rightarrow m=\dfrac{7a}6$，$n=\dfrac{5a}6$．" "\n"
        r"**第三步：余弦定理**" "\n"
        r"在 $\triangle PF_1F_2$ 中，$\lvert F_1F_2\rvert=2c$，对角 $F_2$ 用余弦定理（角在 $F_1$）：" "\n"
        r"$n^{2}=m^{2}+4c^{2}-2\cdot m\cdot2c\cdot\cos\theta=m^{2}+4c^{2}-\dfrac{20c}7m$．" "\n"
        r"代入 $m,n$：$\dfrac{25a^{2}}{36}=\dfrac{49a^{2}}{36}+4c^{2}-\dfrac{20c}7\cdot\dfrac{7a}6$，即" "\n"
        r"$-\dfrac{24a^{2}}{36}=4c^{2}-\dfrac{10ca}{3}\Rightarrow-\dfrac{2a^{2}}3=4c^{2}-\dfrac{10ca}3$．" "\n"
        r"乘 $3$：$-2a^{2}=12c^{2}-10ca\Rightarrow6c^{2}-5ca+a^{2}=0$．" "\n"
        r"除以 $a^{2}$：$6e^{2}-5e+1=0\Rightarrow e=\dfrac{5\pm\sqrt{25-24}}{12}=\dfrac{5\pm1}{12}$，" "\n"
        r"故 $e=\dfrac12$ 或 $e=\dfrac13$．"
    ),
    'review': (
        r"★ 题干、答案完整 ✓（**详解未提取**，上述为我独立推导）。答案与原书标注 $\frac12$ 或 $\frac13$ 一致 ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **$p=2c$**：抛物线 $y^{2}=2px$ 焦点 $(\frac p2,0)=F_2(c,0)$ ⟹ $p=2c$，准线 $x=-\frac p2=-c$ ✓✓✓" "\n"
        r"② **$x_P=-c+m\cos\theta$**：$F_1=(-c,0)$，$P=F_1+m(\cos\theta,\sin\theta)$ ⟹ $x_P=-c+m\cos\theta$ ✓✓✓" "\n"
        r"③ **$n=x_P+c=\frac57m$**：抛物线定义（到准线距离）✓✓✓" "\n"
        r"④ **$m=\frac{7a}6,n=\frac{5a}6$**：$m(1+\frac57)=2a$ ⟹ $m\cdot\frac{12}7=2a$ ⟹ $m=\frac{7a}6$ ✓；$n=\frac57\cdot\frac{7a}6=\frac{5a}6$ ✓✓✓" "\n"
        r"⑤ **余弦定理**：$n^{2}=m^{2}+(2c)^{2}-2\cdot m\cdot 2c\cos\theta$ ✓✓（对角在 $F_1$，邻边 $m$ 与 $2c$）" "\n"
        r"$=\frac{49a^{2}}{36}+4c^{2}-4mc\cdot\frac57=\frac{49a^{2}}{36}+4c^{2}-\frac{20}{7}\cdot\frac{7a}6 c=\frac{49a^{2}}{36}+4c^{2}-\frac{10ac}3$ ✓✓✓" "\n"
        r"⑥ **$\frac{25a^{2}}{36}-\frac{49a^{2}}{36}=-\frac{24a^{2}}{36}=-\frac{2a^{2}}3$** ✓✓✓" "\n"
        r"⑦ **$6c^{2}-5ac+a^{2}=0$**：由 $-\frac{2a^{2}}3=4c^{2}-\frac{10ac}3$，乘 $3$ 得 $-2a^{2}=12c^{2}-10ac$，移项 $12c^{2}-10ac+2a^{2}=0$，除 $2$ ✓✓✓" "\n"
        r"⑧ **$6e^{2}-5e+1=0$**：$e=\frac{5\pm\sqrt{25-24}}{12}=\frac{5\pm1}{12}$ ⟹ $e=\frac12$ 或 $\frac13$ ✓✓✓" "\n"
        r"⑨ **数值检验（$e=\frac12$）**：取 $c=1$、$a=2$、$b^{2}=3$，椭圆 $\frac{x^{2}}4+\frac{y^{2}}3=1$；$p=2$，抛物线 $y^{2}=4x$。" "\n"
        r"由 $m=\frac{7a}6=\frac73=2.333$、$n=\frac{5a}6=\frac53=1.667$；检验 $m+n=4=2a$ ✓✓✓" "\n"
        r"$x_P=n-c=1.667-1=0.667$；由 $\cos\theta=\frac57$ 得 $x_P=-c+m\cdot\frac57=-1+2.333\times0.7143=-1+1.667=0.667$ ✓✓✓ **一致**" "\n"
        r"$y_P$：$\sin\theta=\sqrt{1-\frac{25}{49}}=\frac{\sqrt{24}}7=0.6999$，$y_P=m\sin\theta=2.333\times0.6999=1.633$。" "\n"
        r"检验 $P$ 在抛物线上：$y^{2}=2.667$、$4x=2.667$ ✓✓✓" "\n"
        r"检验 $P$ 在椭圆上：$\frac{0.444}4+\frac{2.667}3=0.111+0.889=1.000$ ✓✓✓ **完美闭合**" "\n"
        r"⑩ **数值检验（$e=\frac13$）**：取 $c=1$、$a=3$、$b^{2}=8$，椭圆 $\frac{x^{2}}9+\frac{y^{2}}8=1$；$p=2$，抛物线 $y^{2}=4x$。" "\n"
        r"$m=\frac{7\cdot3}6=3.5$、$n=\frac{5\cdot3}6=2.5$；$m+n=6=2a$ ✓✓✓" "\n"
        r"$x_P=n-c=1.5$；$y_P=3.5\times0.6999=2.450$。" "\n"
        r"抛物线：$y^{2}=6.002$、$4x=6$ ✓✓✓；椭圆：$\frac{2.25}9+\frac{6.002}8=0.25+0.750=1.000$ ✓✓✓ **完美闭合**" "\n"
        r"**答案 $e=\frac12$ 或 $e=\frac13$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（椭圆 + 抛物线共焦点）**：" "\n"
        r"① ⭐⭐ **抛物线焦点与 $F_2$ 重合 ⟹ 准线恰是 $x=-c$** —— " "\n"
        r"于是「到 $F_2$ 的距离」与「横坐标 $+c$」可以直接互换，这是整套推导的枢纽；" "\n"
        r"② ⭐ **把 $x_P$ 用 $\triangle PF_1F_2$ 表示**：$x_P=-c+m\cos\theta$，与 $n=x_P+c$ 一比就得到 $n=m\cos\theta$ —— " "\n"
        r"**即 $n=m\cos\angle PF_1F_2$，极其简洁，可当公式记**；" "\n"
        r"③ ⭐ **$m+n=2a$ 与 $n=m\cos\theta$ 联立** ⟹ $m=\frac{2a}{1+\cos\theta}$、$n=\frac{2a\cos\theta}{1+\cos\theta}$；" "\n"
        r"④ ⭐ **最后用余弦定理（或直接用 $n^{2}=m^{2}+4c^{2}-4mc\cos\theta$）消元**，得到关于 $e$ 的二次方程，**两个根都要保留**；" "\n"
        r"⑤ ⚠ **两解都要检验**：分别取 $e=\frac12$、$e=\frac13$ 反算 $P$，确认同时在两条曲线上（本题两组都完美闭合 ✓）；" "\n"
        r"⑥ **为什么会有两解**：给定 $\cos\theta$ 与 $2a$ 的关系对 $e$ 是二次的，对应「$P$ 在 $x$ 轴上方/下方」或「椭圆胖瘦」两种几何。"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-335'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-335-V3',
}

T342_E1 = {
    'type': '填空',
    'stem_text': (
        r"已知 $O,A,B$ 为平面上三点，若 $\lvert\vec{OA}\rvert=\lvert\vec{OB}\rvert=2$，$\vec{OA}\cdot\vec{OB}=2$，"
        r"动点 $P$ 和实数 $\lambda,\mu$ 满足 $\vec{OP}=\lambda\vec{OA}+\mu\vec{OB}$，$1\le\lambda\le2$，$2\le\mu\le4$，"
        r"则动点 $P$ 轨迹的测度是 ____"
    ),
    'opts': [],
    'answer': r"$4\sqrt3$",
    'analysis': (
        r"由点积得 $\cos\angle AOB=\frac12$ 即夹角 $60^\circ$；$(\lambda,\mu)\mapsto P$ 是线性映射，"
        r"区域面积 $=$ 参数矩形面积 $\times$ 雅可比 $=\lvert\vec{OA}\times\vec{OB}\rvert$。"
    ),
    'solution': (
        r"$\cos\angle AOB=\dfrac{\vec{OA}\cdot\vec{OB}}{\lvert\vec{OA}\rvert\lvert\vec{OB}\rvert}=\dfrac2{2\cdot2}=\dfrac12\Rightarrow\angle AOB=60^\circ$．" "\n"
        r"**第一步：轨迹是平行四边形**" "\n"
        r"$(\lambda,\mu)\mapsto P$ 是线性映射，把参数平面上的矩形 $[1,2]\times[2,4]$ 映成以" "\n"
        r"$\vec{OA}$、$\vec{OB}$ 为邻边方向的平行四边形（边长为 $1\cdot\lvert\vec{OA}\rvert=2$ 与 $2\cdot\lvert\vec{OB}\rvert=4$）．" "\n"
        r"**第二步：雅可比（面积放大倍数）**" "\n"
        r"单位参数正方形（边长 $1$）映成的平行四边形面积为" "\n"
        r"$\lvert\vec{OA}\times\vec{OB}\rvert=\lvert\vec{OA}\rvert\lvert\vec{OB}\rvert\sin60^\circ=2\cdot2\cdot\dfrac{\sqrt3}2=2\sqrt3$．" "\n"
        r"**第三步：参数区域面积**" "\n"
        r"$\lambda$ 的区间长 $=2-1=1$，$\mu$ 的区间长 $=4-2=2$，矩形面积 $=1\times2=2$．" "\n"
        r"**第四步：相乘**" "\n"
        r"轨迹面积 $=2\times2\sqrt3=4\sqrt3$．"
    ),
    'review': (
        r"★ 题干、答案完整 ✓（**详解未提取**，上述为我独立推导）。" "\n"
        r"ref_bank 存 `4 3`，实为 $4\sqrt3$（**根号丢失**），与我的推导吻合 ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **$\cos\angle AOB=\frac12$**：$\frac{2}{2\cdot2}=0.5$ ⟹ $60^\circ$ ✓✓✓" "\n"
        r"② **$\lvert\vec{OA}\times\vec{OB}\rvert=2\sqrt3$**：$2\cdot2\cdot\sin60^\circ=4\cdot0.866=3.464=2\sqrt3$ ✓✓✓" "\n"
        r"③ **参数矩形面积 $=2$**：$(2-1)\times(4-2)=1\times2=2$ ✓✓✓" "\n"
        r"④ **线性映射下面积 $=$ 雅可比 $\times$ 原面积**：标准结论 ✓✓✓" "\n"
        r"⑤ **直接坐标验证**：取 $\vec{OA}=(2,0)$、$\vec{OB}=(2\cos60^\circ,2\sin60^\circ)=(1,\sqrt3)$。" "\n"
        r"检验点积：$2\cdot1+0\cdot\sqrt3=2$ ✓✓✓" "\n"
        r"$P=\lambda(2,0)+\mu(1,\sqrt3)=(2\lambda+\mu,\;\sqrt3\mu)$。" "\n"
        r"四个顶点：$(\lambda,\mu)=(1,2)\to(4,2\sqrt3)$；$(2,2)\to(6,2\sqrt3)$；$(1,4)\to(6,4\sqrt3)$；$(2,4)\to(8,4\sqrt3)$。" "\n"
        r"这是平行四边形：底边从 $(4,2\sqrt3)$ 到 $(6,2\sqrt3)$ 长 $=2$（水平）✓✓" "\n"
        r"高 $=4\sqrt3-2\sqrt3=2\sqrt3$（竖直）✓✓" "\n"
        r"面积 $=$ 底 $\times$ 高 $=2\times2\sqrt3=4\sqrt3$ ✓✓✓" "\n"
        r"⑥ **用叉积再算一次**：邻边向量 $\vec{u}=(2,0)$（$\lambda$ 增 $1$）、$\vec{v}=(0,2\sqrt3)$（$\mu$ 增 $2$ 使 $P$ 增 $(2,2\sqrt3)$？）" "\n"
        r"—— 重取：$\lambda$ 从 $1\to2$ 时 $P$ 增 $\vec{OA}=(2,0)$；$\mu$ 从 $2\to4$ 时 $P$ 增 $2\vec{OB}=(2,2\sqrt3)$。" "\n"
        r"面积 $=\lvert 2\cdot2\sqrt3-0\cdot2\rvert=4\sqrt3$ ✓✓✓ **两法一致**" "\n"
        r"⑦ **测度是面积不是长度**：轨迹是平面区域（$\lambda,\mu$ 都连续变化），按题注取面积 ✓✓✓" "\n"
        r"**答案 $4\sqrt3$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（向量线性组合的轨迹测度）**：" "\n"
        r"① ⭐⭐ **$\vec{OP}=\lambda\vec{u}+\mu\vec{v}$ 且 $\lambda,\mu$ 各自在一个区间内 ⟹ 轨迹是平行四边形**，" "\n"
        r"其**面积 $=$ （参数区域面积）$\times\lvert\vec{u}\times\vec{v}\rvert$** —— 雅可比就是叉积的模；" "\n"
        r"② ⭐ **夹角由点积定**：$\cos\angle=\frac{\vec{u}\cdot\vec{v}}{\lvert u\rvert\lvert v\rvert}$，本题给的点积 $2$ 就是为这一步；" "\n"
        r"③ ⭐ **最稳的做法是取具体坐标**：令 $\vec{OA}=(2,0)$、$\vec{OB}=(1,\sqrt3)$，把四个顶点坐标算出来直接算面积 —— " "\n"
        r"比记公式可靠，也顺带检验了①；" "\n"
        r"④ ⚠ **区间的「长度」不是端点值**：$\mu\in[2,4]$ 长度是 $2$ 不是 $4$，别把端点当长度；" "\n"
        r"⑤ ⚠ **测度的含义看题注**：轨迹是曲线取长度、是区域取面积 —— 本题 $\lambda,\mu$ 都在区间内连续变化，必是区域；" "\n"
        r"⑥ ⚠ **答案 $4\sqrt3$ 提取成 `4 3`** —— 又一处根号丢失，用面积数量级（$\approx6.93$）即可识别。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-342'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-342-E1',
}

T342_V1 = {
    'type': '填空',
    'stem_text': (
        r"已知 $E$ 为平面内一定点且 $\lvert\vec{OE}\rvert=1$，平面内的动点 $P$ 满足："
        r"存在实数 $\lambda\ge1$，使 $\bigl\lvert\lambda\vec{OP}+(1-\lambda)\vec{OE}\bigr\rvert=\dfrac12$，"
        r"若点 $P$ 的轨迹为平面图形 $S$，则 $S$ 的面积为 ____"
    ),
    'opts': [],
    'answer': r"$\dfrac\pi6+\dfrac{\sqrt3}4$",
    'analysis': (
        r"记 $Q=\lambda\vec{OP}+(1-\lambda)\vec{OE}$，则 $Q$ 在射线 $EP$ 上且在 $P$ 外侧（$\lambda\ge1$）；"
        r"$\lvert OQ\rvert=\frac12$ 说明 $Q$ 在圆上，故 $P$ 取遍「从 $E$ 出发到圆的所有线段」—— 即切线三角形加弓形。"
    ),
    'solution': (
        r"设 $\vec{OQ}=\lambda\vec{OP}+(1-\lambda)\vec{OE}$，则 $Q$ 在直线 $EP$ 上，且 $\vec{EQ}=\lambda\vec{EP}$，" "\n"
        r"由 $\lambda\ge1$ 知 $Q$ 在射线 $EP$ 上、位于 $P$ 的外侧（含 $P$ 本身），即 $P$ 在线段 $EQ$ 上．" "\n"
        r"条件 $\lvert\vec{OQ}\rvert=\frac12$ 表示 $Q$ 在以 $O$ 为圆心、$\frac12$ 为半径的圆上．" "\n"
        r"**第一步：确定 $P$ 的轨迹形状**" "\n"
        r"$P$ 取遍所有「$E$ 到圆上某点 $Q$ 的线段」上的点，故 $S$ 是从 $E$ 向圆所作的**两条切线切成的区域**：" "\n"
        r"$S=\triangle EAB\ \cup\ (\text{圆在弦 }AB\text{ 远离 }E\text{ 一侧的部分})$，其中 $A,B$ 为切点．" "\n"
        r"**第二步：算 $\triangle EAB$**" "\n"
        r"$OA\perp EA$，$\lvert OA\rvert=\frac12$，$\lvert OE\rvert=1$，故 $\sin\angle AEO=\frac{1/2}1=\frac12\Rightarrow\angle AEO=30^\circ$，" "\n"
        r"$\lvert EA\rvert=\sqrt{1-\frac14}=\dfrac{\sqrt3}2$，同理 $\lvert EB\rvert=\dfrac{\sqrt3}2$，$\angle AEB=60^\circ$．" "\n"
        r"$S_{\triangle EAB}=\dfrac12\cdot\dfrac{\sqrt3}2\cdot\dfrac{\sqrt3}2\cdot\sin60^\circ=\dfrac12\cdot\dfrac34\cdot\dfrac{\sqrt3}2=\dfrac{3\sqrt3}{16}$．" "\n"
        r"**第三步：算弓形**" "\n"
        r"$\angle AOE=60^\circ$，故 $\angle AOB=120^\circ=\frac{2\pi}3$．" "\n"
        r"靠近 $E$ 的一侧是**小弓形**（圆心角 $120^\circ$）：" "\n"
        r"$S_{\text{小弓}}=\dfrac12r^{2}(\theta-\sin\theta)=\dfrac12\cdot\dfrac14\left(\dfrac{2\pi}3-\dfrac{\sqrt3}2\right)=\dfrac\pi{12}-\dfrac{\sqrt3}{16}$．" "\n"
        r"圆面积 $=\pi\cdot\frac14=\frac\pi4$，故远离 $E$ 的大弓形" "\n"
        r"$S_{\text{大弓}}=\dfrac\pi4-\left(\dfrac\pi{12}-\dfrac{\sqrt3}{16}\right)=\dfrac\pi6+\dfrac{\sqrt3}{16}$．" "\n"
        r"**第四步：相加**" "\n"
        r"$S=\dfrac{3\sqrt3}{16}+\dfrac\pi6+\dfrac{\sqrt3}{16}=\dfrac\pi6+\dfrac{4\sqrt3}{16}=\dfrac\pi6+\dfrac{\sqrt3}4$．"
    ),
    'review': (
        r"★ 题干、答案完整 ✓。原书 p314 详解：" "\n"
        r"「以 $O$ 为圆心，以 $\frac12$ 为半径作圆，过 $E$ 作圆 $O$ 的切线 $EA,EB$ 分别与圆 $O$ 切于点 $A,B$，" "\n"
        r"连结 $OA,OB$，延长 $EO$ 与圆 $O$ 交于点 $F$，设点 $Q$，满足 $\vec{OQ}=\lambda\vec{OP}+(1-\lambda)\vec{OE}$，" "\n"
        r"由 $\lambda\ge1$，则点 $Q$ 在 $EP$ 的延长线上，若要存在 $\lambda\ge1$ 使得 $\lvert\vec{OQ}\rvert=\frac12$，" "\n"
        r"所以 $EP$ 的延长线与圆有交点，从而得出点 $P$ 的轨迹图形」" "\n"
        r"—— **「切线 $EA,EB$」「$Q$ 在 $EP$ 延长线上」「$EP$ 延长线与圆有交点」全部与我的推导一致** ✓✓✓" "\n"
        r"（详解后续的面积计算在提取中破碎，第三步、第四步由我补出）" "\n"
        r"**⚠ 答案还原**：ref_bank 存 `π/6 + 3/4`，实为 $\frac\pi6+\frac{\sqrt3}4$（**$\sqrt3$ 丢了根号变成 $3$**）。" "\n"
        r"**判定依据**：我独立算出 $\frac\pi6+\frac{\sqrt3}4=\frac{3.1416}6+\frac{1.732}4=0.5236+0.4330=0.9566$；" "\n"
        r"若按字面 $\frac\pi6+\frac34=0.5236+0.75=1.2736$，与几何直觉（区域在半径为 $\frac12$ 的圆附近）不符 ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **$Q$ 在射线 $EP$ 上且在 $P$ 外侧**：$\vec{OQ}=\lambda\vec{OP}+(1-\lambda)\vec{OE}=\vec{OE}+\lambda(\vec{OP}-\vec{OE})=\vec{OE}+\lambda\vec{EP}$ ✓✓✓" "\n"
        r"$\lambda\ge1$ ⟹ $Q$ 在 $P$ 的外侧或就是 $P$ ⟹ $P$ 在线段 $EQ$ 上 ✓✓✓" "\n"
        r"② **切线长 $\frac{\sqrt3}2$**：$\lvert EA\rvert=\sqrt{\lvert OE\rvert^{2}-r^{2}}=\sqrt{1-\frac14}=\frac{\sqrt3}2$ ✓✓✓" "\n"
        r"③ **$\angle AEO=30^\circ$**：$\sin=\frac{r}{\lvert OE\rvert}=\frac{1/2}1=\frac12$ ✓✓✓ ⟹ $\angle AEB=60^\circ$ ✓✓✓" "\n"
        r"④ **$\triangle EAB$ 面积 $=\frac{3\sqrt3}{16}$**：$\frac12\cdot\frac{\sqrt3}2\cdot\frac{\sqrt3}2\cdot\frac{\sqrt3}2=\frac12\cdot\frac34\cdot\frac{\sqrt3}2=\frac{3\sqrt3}{16}=0.3248$ ✓✓✓" "\n"
        r"⑤ **$\angle AOB=120^\circ$**：$\angle AOE=90^\circ-30^\circ=60^\circ$ ✓✓，对称得 $\angle AOB=120^\circ$ ✓✓✓" "\n"
        r"⑥ **小弓形 $=\frac\pi{12}-\frac{\sqrt3}{16}$**：$\frac12\cdot\frac14\cdot(\frac{2\pi}3-\frac{\sqrt3}2)=\frac18(2.0944-0.8660)=\frac18\cdot1.2284=0.15355$ ✓✓✓" "\n"
        r"（公式 $\frac12r^{2}(\theta-\sin\theta)$，$\theta=\frac{2\pi}3$、$\sin\theta=\frac{\sqrt3}2$ ✓）" "\n"
        r"⑦ **大弓形 $=\frac\pi6+\frac{\sqrt3}{16}$**：圆面积 $\frac\pi4=0.7854$；$0.7854-0.15355=0.63185$ ✓✓✓" "\n"
        r"$\frac\pi6+\frac{\sqrt3}{16}=0.5236+0.10825=0.63185$ ✓✓✓ **吻合**" "\n"
        r"⑧ **总面积**：$0.3248+0.63185=0.95665$；$\frac\pi6+\frac{\sqrt3}4=0.5236+0.4330=0.9566$ ✓✓✓" "\n"
        r"⑨ **合理性检验**：$S$ 应大于圆面积 $\frac\pi4=0.7854$（$S$ 包含大弓形 $0.6319$ 加三角形 $0.3248$），" "\n"
        r"且小于切线三角形加整圆 $=0.3248+0.7854=1.110$ ✓✓✓ **$0.9566$ 落在区间内**" "\n"
        r"**答案 $\frac\pi6+\frac{\sqrt3}4$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（$\lambda\vec{OP}+(1-\lambda)\vec{OE}$ 型轨迹）**：" "\n"
        r"① ⭐⭐ **把 $\lambda\vec{OP}+(1-\lambda)\vec{OE}$ 识别为「直线 $EP$ 上的点」**：$=\vec{OE}+\lambda\vec{EP}$，" "\n"
        r"$\lambda\ge1$ ⟹ 在 $P$ 外侧；$\lambda\in[0,1]$ ⟹ 在线段 $EP$ 上；$\lambda\le0$ ⟹ 在 $E$ 另一侧 —— **先定 $\lambda$ 的范围含义**；" "\n"
        r"② ⭐ **「存在 $\lambda$ 使得 $Q$ 在圆上」⟹ $P$ 的轨迹是「$E$ 向圆作切线」扫出的区域**，" "\n"
        r"即 **$\triangle EAB$ + 远离 $E$ 的那个弓形**（注意是「大弓形」不是小弓形 —— 因为 $P$ 可以在圆内也可以在圆外）；" "\n"
        r"③ ⭐ **切线长 $=\sqrt{d^{2}-r^{2}}$**，本题 $d=1$、$r=\frac12$ ⟹ $\frac{\sqrt3}2$；" "\n"
        r"④ ⭐ **弓形面积公式 $\frac12r^{2}(\theta-\sin\theta)$**（$\theta$ 为圆心角，弧度制）务必记牢；" "\n"
        r"⑤ ⚠ **分清「靠 $E$ 的弓形」和「远离 $E$ 的弓形」**：本题圆在弦 $AB$ 两侧，**$P$ 能到达远离 $E$ 的那一侧**（因 $P$ 在线段 $EQ$ 上，$Q$ 可以是圆上任意点），" "\n"
        r"故取「圆 $-$ 小弓形」的大弓形；弄反会得 $\frac\pi{12}-\frac{\sqrt3}{16}+\frac{3\sqrt3}{16}=\frac\pi{12}+\frac{\sqrt3}8$（错）；" "\n"
        r"⑥ 检验：**总面积应介于圆面积与（圆面积 $+$ 切线三角形）之间**（$0.7854<0.9566<1.110$ ✓），可快速排错。"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-342'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-342-V1',
}

QS = [T327_E1, T327_V1, T327_V3, T329_V3, T335_E1, T335_V3, T342_E1, T342_V1]
