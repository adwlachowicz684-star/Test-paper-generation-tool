# -*- coding: utf-8 -*-
r"""第60批（二）：含绝对值的不等式（5 题） 来源：2024高中数学热点题型归纳完整解析版.pdf p418（PDF 页 417）M-T-025｜p419（PDF 页 418）M-T-027 ## ★★ 这批的共性：绝对值符号在提取中全丢了 原文 $f(x)=\lvert x-a\rvert+\lvert x+5-a\rvert$ 提取成 `f(x) = x - a + x + 5 - a`。 **还原依据**：题干说「不等式 $f(x)-\lvert x-a\rvert\le2$ 的解集为 $[-5,-1]$」， 若 $f$ 没有绝对值，$f(x)-\lvert x-a\rvert$ 这个写法本身就说不通 —— 减法里凭空出现 $\lvert x-a\rvert$。 ## ★★ 三个反复用的工具 **1. 绝对值三角不等式（求最值）** $$\lvert u\rvert+\lvert v\rvert\ge\lvert u\pm v\rvert,\qquad\bigl\lvert\lvert u\rvert-\lvert v\rvert\bigr\rvert\le\lvert u\pm v\rvert$$ 关键在**把 $x$ 消掉**： - $\lvert x-a\rvert+\lvert x+5-a\rvert\ge\bigl\lvert(x-a)-(x+5-a)\bigr\rvert=5$（取减号消 $x$） - $\lvert x-3\rvert-\lvert x-a\rvert\le\bigl\lvert(x-3)-(x-a)\bigr\rvert=\lvert a-3\rvert$（取减号） **2. 解 $\lvert X\rvert\le c$ 用 $-c\le X\le c$；解 $\lvert X\rvert\ge c$ 用 $X\ge c$ 或 $X\le-c$** **3. 分段去绝对值**（画分段函数、求与 $x$ 轴围成面积时用） ## 五题验算 | 题 | 关键 | 答案 | |---|---|---| | M-T-025-E1 | $\lvert x+5-a\rvert\le2\Rightarrow a-7\le x\le a-3$；$\min f=5$ | $a=2$；$m<-5$ 或 $m>1$ | | M-T-025-V2 | $\lvert x-1\rvert\ge2$；$f(x)\le0\Rightarrow x\le-\frac a2$ | $\{x\mid x\ge3\text{ 或 }x\le-1\}$；$a=2$ | | M-T-025-V3 | $\lvert3x+m\rvert\le9+m$；$S=\frac{4(m+3)^{2}}{15}>60$ | $m=-3$；$m\in(12,+\infty)$ | | M-T-027-E1 | 三段：$\varnothing$、$[\frac{11}4,3)$、$[3,+\infty)$；$\max f=\lvert a-3\rvert$ | $[\frac{11}4,+\infty)$；$a\le\frac32$ | | M-T-027-V2 | 三段：$x\le-3$、$\varnothing$、$x\ge1$；$h(x)=\lvert2x+1\rvert-2\lvert x\rvert$ 最小值 $-1$ | $(-\infty,-3]\cup[1,+\infty)$；$a\ge-3$ | """

T025_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=\lvert x-a\rvert+\lvert x+5-a\rvert$．"
        "\n（1）若不等式 $f(x)-\lvert x-a\rvert\le2$ 的解集为 $[-5,-1]$，求实数 $a$ 的值；"
        "\n（2）若 $\exists x\in\mathbf R$，使得 $f(x)<4m+m^{2}$，求实数 $m$ 的取值范围．"
    ),
    'opts': [],
    'answer': r"（1）$a=2$；（2）$(-\infty,-5)\cup(1,+\infty)$",
    'analysis': (
        r"（1）$f(x)-\lvert x-a\rvert=\lvert x+5-a\rvert\le2\Rightarrow a-7\le x\le a-3$，与 $[-5,-1]$ 比对端点；"
        r"（2）「存在 $x$ 使 $f(x)<t$」$\Longleftrightarrow$ $t>\min f$，而 $\min f=5$（三角不等式取减号消 $x$）。"
    ),
    'solution': (
        r"**（1）** $f(x)-\lvert x-a\rvert=\lvert x+5-a\rvert$，故所求不等式即 $\lvert x+5-a\rvert\le2$．" "\n"
        r"由 $\lvert X\rvert\le c\Longleftrightarrow-c\le X\le c$：$-2\le x+5-a\le2\Rightarrow a-7\le x\le a-3$．" "\n"
        r"已知解集为 $[-5,-1]$，故 $\begin{cases}a-7=-5\\ a-3=-1\end{cases}\Rightarrow a=2$（两式一致 ✓）．" "\n"
        r"**（2）** 先求 $f$ 的最小值．由绝对值三角不等式（取减号以消去 $x$）：" "\n"
        r"$f(x)=\lvert x-a\rvert+\lvert x+5-a\rvert\ge\bigl\lvert(x-a)-(x+5-a)\bigr\rvert=\lvert-5\rvert=5$．" "\n"
        r"当 $x$ 在 $a$ 与 $a-5$ 之间时取等号，故 $f_{\min}=5$．" "\n"
        r"「$\exists x\in\mathbf R$ 使 $f(x)<4m+m^{2}$」$\Longleftrightarrow$ $4m+m^{2}>f_{\min}=5$" "\n"
        r"（若 $4m+m^2\le5$，则对所有 $x$ 都有 $f(x)\ge5\ge4m+m^2$，不存在这样的 $x$）．" "\n"
        r"解 $m^{2}+4m-5>0\Rightarrow(m+5)(m-1)>0\Rightarrow m<-5$ 或 $m>1$．" "\n"
        r"故 $m\in(-\infty,-5)\cup(1,+\infty)$．"
    ),
    'review': (
        r"★ 题干、答案完整 ✓。原书 p418 详解：" "\n"
        r"「$\lvert x+5-a\rvert\le2$，$\therefore a-7\le x\le a-3$ …$a-7=-5$、$a-3=-1$，$\therefore a=2$」✓✓" "\n"
        r"「$f(x)=\lvert x-a\rvert+\lvert x+5-a\rvert\ge5$ …$4m+m^{2}>5$，解得 $m<-5$ 或 $m>1$」**与我的推导完全一致** ✓✓✓" "\n"
        r"**⚠ 题干还原**：原文提取为 `f(x) = x - a + x + 5 - a`（绝对值符号丢失）。" "\n"
        r"还原依据：题干出现「$f(x)-\lvert x-a\rvert\le2$」—— 若 $f$ 不含 $\lvert x-a\rvert$ 项，" "\n"
        r"这个减法就无从谈起；且详解明确写 $\lvert x+5-a\rvert\le2$ ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **（1）**：$\lvert x+5-a\rvert\le2\Rightarrow-2\lex+5-a\le2\Rightarrow a-7\lex\lea-3$ ✓✓" "\n"
        r"$a=2$：$-5\lex\le-1$ ✓✓✓ **与题设解集 $[-5,-1]$ 一致**" "\n"
        r"② **$\min f=5$**：取 $a=2$，$f(x)=\lvert x-2\rvert+\lvert x+3\rvert$。在 $[-3,2]$ 上 $f(x)=5$（常数）✓" "\n"
        r"如 $x=0$：$\lvert-2\rvert+\lvert3\rvert=2+3=5$ ✓✓；$x=5$：$3+8=11>5$ ✓ **确为最小值**" "\n"
        r"③ **（2）的逻辑**：「$\exists x,f(x)<t$」$\iff t>\min f$（**不是** $t>\max f$）✓✓✓" "\n"
        r"④ **$m^{2}+4m-5>0$**：根 $m=\frac{-4\pm\sqrt{16+20}}2=\frac{-4\pm6}2$，即 $m=1$ 或 $m=-5$ ✓✓" "\n"
        r"开口向上 ⟹ $m<-5$ 或 $m>1$ ✓✓✓" "\n"
        r"⑤ **端点检验**：$m=1$：$4+1=5=f_{\min}$，此时要求 $f(x)<5$，但 $f(x)\ge5$ 恒成立 ⟹ 不存在 ✓ **开区间正确**" "\n"
        r"$m=-5$：$-20+25=5$，同理不存在 ✓✓✓" "\n"
        r"⑥ **取 $m=2$**：$8+4=12>5$，存在 $x$（如 $x=a$）使 $f=5<12$ ✓✓" "\n"
        r"**答案（1）$a=2$、（2）$(-\infty,-5)\cup(1,+\infty)$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（存在/恒成立与最值）**：" "\n"
        r"① ⭐⭐ **$\exists x$ 使 $f(x)<t$ $\iff$ $t>\min f$**；**$\forall x$ 使 $f(x)\ge t$ $\iff$ $t\le\min f$**；" "\n"
        r"记忆法：「存在」比的是**最松**的那个（$\exists\to\min$，$\forall\to\max$）；" "\n"
        r"② ⭐ **求 $\lvert x-p\rvert+\lvert x-q\rvert$ 的最小值用 $\ge\lvert p-q\rvert$**（取减号消 $x$），" "\n"
        r"最小值就是两点距离 $\lvert p-q\rvert$，且在 $[p,q]$ 上恒取到；" "\n"
        r"③ $\lvert X\rvert\le c$ 直接写 $-c\le X\le c$，**别分情况** —— 本题一步就出解集；" "\n"
        r"④ ⚠ **端点是否取到**：本题 $m=\pm$ 端点时 $4m+m^2=5=f_{\min}$，而要求严格小于，" "\n"
        r"故必须**开区间** —— 这类「严格不等号 + 恰好等于最值」的边界是命题人的最爱。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-025'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-025-E1',
}

T025_V2 = {
    'type': '解答',
    'stem_text': (
        r"设函数 $f(x)=\lvert x-a\rvert+3x$，其中 $a>0$．"
        "\n（I）当 $a=1$ 时，求不等式 $f(x)\ge3x+2$ 的解集；"
        "\n（II）若不等式 $f(x)\le0$ 的解集为 $\{x\mid x\le-1\}$，求 $a$ 的值．"
    ),
    'opts': [],
    'answer': r"（I）$\{x\mid x\ge3\text{ 或 }x\le-1\}$；（II）$a=2$",
    'analysis': (
        r"（I）代入 $a=1$ 后 $3x$ 恰好抵消，化为 $\lvert x-1\rvert\ge2$；"
        r"（II）分段去绝对值：解集必形如 $x\le-\frac a2$，令 $-\frac a2=-1$ 得 $a=2$。"
    ),
    'solution': (
        r"**（I）** $a=1$ 时 $f(x)=\lvert x-1\rvert+3x$，不等式为 $\lvert x-1\rvert+3x\ge3x+2$，" "\n"
        r"两边的 $3x$ 抵消，得 $\lvert x-1\rvert\ge2$．" "\n"
        r"由 $\lvert X\rvert\ge c\Longleftrightarrow X\ge c$ 或 $X\le-c$：" "\n"
        r"$x-1\ge2\Rightarrow x\ge3$；或 $x-1\le-2\Rightarrow x\le-1$．" "\n"
        r"故解集为 $\{x\mid x\ge3\text{ 或 }x\le-1\}$．" "\n"
        r"**（II）** $f(x)\le0\Longleftrightarrow\lvert x-a\rvert+3x\le0\Longleftrightarrow\lvert x-a\rvert\le-3x$（注意右边须 $\ge0$）．" "\n"
        r"分段去绝对值（$a>0$）：" "\n"
        r"$\bullet\$ 当 $x\ge a$ 时：$\lvert x-a\rvert=x-a$，不等式为 $x-a+3x\le0\Rightarrow4x\le a\Rightarrow x\le\dfrac a4$．" "\n"
        r"但 $\dfrac a4<a\le x$，矛盾，故此段无解．" "\n"
        r"$\bullet\$ 当 $x<a$ 时：$\lvert x-a\rvert=a-x$，不等式为 $a-x+3x\le0\Rightarrow2x\le-a\Rightarrow x\le-\dfrac a2$．" "\n"
        r"因 $a>0$，$-\dfrac a2<a$ 成立，故此段解为 $x\le-\dfrac a2$．" "\n"
        r"故 $f(x)\le0$ 的解集为 $\left\{x\Bigm|x\le-\dfrac a2\right\}$．" "\n"
        r"已知解集为 $\{x\mid x\le-1\}$，故 $-\dfrac a2=-1\Rightarrow a=2$（满足 $a>0$ ✓）．"
    ),
    'review': (
        r"★ 题干、答案完整 ✓。原书 p418 详解：" "\n"
        r"「当 $a=1$ 时，$f(x)\ge3x+2$ 可化为 $\lvert x-1\rvert\ge2$。由此可得 $x\ge3$ 或 $x\le-1$」✓✓" "\n"
        r"「（II）…化为不等式组 …因为 $a>0$，所以不等式组的解集为 $\{x\mid x\le-\frac a2\}$ …" "\n"
        r"由题设可得 $-\frac a2=-1$，故 $a=2$」**与我的推导完全一致** ✓✓✓" "\n"
        r"**⚠ 题干还原**：原文提取为 `f(x) = x - a + 3x`（绝对值丢失），且答案栏只显示 (I)。" "\n"
        r"（II）的题干「若不等式 $f(x)\le0$ 的解集为 $\{x\mid x\le-1\}$」由详解中的不等式组与" "\n"
        r"「$-\frac a2=-1$」反推还原 ✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **（I）$3x$ 抵消**：$\lvert x-1\rvert+3x\ge3x+2\Rightarrow\lvert x-1\rvert\ge2$ ✓✓✓" "\n"
        r"$x\ge3$ 检验：$x=3$：$\lvert2\rvert+9=11$，$3(3)+2=11$，$11\ge11$ ✓（取等）" "\n"
        r"$x\le-1$ 检验：$x=-1$：$\lvert-2\rvert-3=-1$，$3(-1)+2=-1$，$-1\ge-1$ ✓（取等）" "\n"
        r"$x=0$：$\lvert-1\rvert+0=1$，$0+2=2$，$1\ge2$ ✗ **不在解集中** ✓✓✓ **正确**" "\n"
        r"② **（II）分段**：$x\gea$ 段 $4x\lea\Rightarrowx\le\frac a4$，与 $x\gea>0$ 矛盾 ✓ **无解正确**" "\n"
        r"$x<a$ 段 $2x\le-a\Rightarrowx\le-\frac a2$ ✓✓" "\n"
        r"③ **$a=2$ 检验**：$f(x)=\lvert x-2\rvert+3x\le0$。" "\n"
        r"$x=-1$：$\lvert-3\rvert-3=3-3=0\le0$ ✓（边界）" "\n"
        r"$x\le-1$ 如 $x=-2$：$\lvert-4\rvert-6=4-6=-2\le0$ ✓✓" "\n"
        r"$x=0$：$\lvert-2\rvert+0=2>0$ ✗ **不在解集** ✓✓✓" "\n"
        r"$x=-0.9$：$\lvert-2.9\rvert-2.7=2.9-2.7=0.2>0$ ✗ **恰在 $-1$ 右侧就不成立** ✓✓✓" "\n"
        r"⟹ 解集确为 $\{x\mid x\le-1\}$ ✓✓✓ **$a=2$ 正确**" "\n"
        r"**答案（I）$\{x\mid x\ge3\text{ 或 }x\le-1\}$、（II）$a=2$ 正确** ✓" "\n"
        r"**⭐ 通法（含绝对值的「两边同消」与分段）**：" "\n"
        r"① ⭐ **先看看两边有没有可以抵消的项**：本题 $3x$ 在两边同时出现，直接抵消后" "\n"
        r"题目退化成最简的 $\lvert x-1\rvert\ge2$ —— **动手分段前先扫一眼，能省一半计算**；" "\n"
        r"② ⭐ **$f(x)\le0$ 型（右边是 $0$）不必套 $-g\le f\le g$**，直接移项成 $\lvert x-a\rvert\le-3x$，" "\n"
        r"再分 $x\ge a$、$x<a$ 两段；" "\n"
        r"③ ⚠ **分段后要检验解是否落在该段内**：$x\gea$ 段解出 $x\le\frac a4$ 与 $x\gea$ 矛盾，" "\n"
        r"这一步最容易漏，漏了就会多出一段假解；" "\n"
        r"④ 解集含参时，**与已知解集比对端点**即可定参数，不必重新解方程。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-025'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-025-V2',
}

T025_V3 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=\lvert3x+m\rvert$．"
        "\n（1）若不等式 $f(x)-m\le9$ 的解集为 $[-1,3]$，求 $m$ 的值；"
        "\n（2）设 $g(x)=\lvert3x+m\rvert-2\lvert x-1\rvert$，其中 $m>0$，"
        r"若 $g(x)$ 的图象与 $x$ 轴围成的三角形的面积大于 $60$，求 $m$ 的取值范围．"
    ),
    'opts': [],
    'answer': r"（1）$m=-3$；（2）$m\in(12,+\infty)$",
    'analysis': (
        r"（1）$\lvert3x+m\rvert\le9+m\Rightarrow\frac{-9-2m}3\le x\le3$，右端点恒为 $3$，令左端点 $=-1$ 得 $m=-3$；"
        r"（2）$m>0$ 时分界点 $-\frac m3<1$，三段去绝对值得折线，找出两个零点与折点，用 $S=\frac12\lvert AB\rvert\cdot\lvert y_C\rvert$。"
    ),
    'solution': (
        r"**（1）** $f(x)-m\le9\Longleftrightarrow\lvert3x+m\rvert\le9+m$（须 $9+m\ge0$）．" "\n"
        r"$-(9+m)\le3x+m\le9+m\Rightarrow-9-2m\le3x\le9\Rightarrow\dfrac{-9-2m}3\le x\le3$．" "\n"
        r"已知解集为 $[-1,3]$，右端点已是 $3$ ✓，故左端点 $\dfrac{-9-2m}3=-1$" "\n"
        r"$\Rightarrow-9-2m=-3\Rightarrow-2m=6\Rightarrow m=-3$（此时 $9+m=6\ge0$ ✓）．" "\n"
        r"**（2）** 设 $m>0$，则 $-\dfrac m3<0<1$．分段去绝对值：" "\n"
        r"$g(x)=\begin{cases}-(3x+m)-2(1-x)=-x-m-2, & x\le-\dfrac m3\\[2mm]" "\n"
        r"(3x+m)-2(1-x)=5x+m-2, & -\dfrac m3<x<1\\[2mm]" "\n"
        r"(3x+m)-2(x-1)=x+m+2, & x\ge1\end{cases}$" "\n"
        r"**求与 $x$ 轴的交点**：" "\n"
        r"$\bullet\$ 第一段：$-x-m-2=0\Rightarrow x=-m-2$（满足 $x\le-\frac m3$ ✓）；" "\n"
        r"$\bullet\$ 第二段：$5x+m-2=0\Rightarrow x=\dfrac{2-m}5$（可验 $-\frac m3<\frac{2-m}5<1$ ✓）；" "\n"
        r"$\bullet\$ 第三段：$x+m+2=0\Rightarrow x=-m-2$，但 $m>0$ 时 $-m-2<0<1$，不满足 $x\ge1$，舍去．" "\n"
        r"记 $A(-m-2,0)$、$B\left(\dfrac{2-m}5,0\right)$；折点 $C\left(-\dfrac m3,\,g\!\left(-\dfrac m3\right)\right)$，" "\n"
        r"$g\!\left(-\dfrac m3\right)=5\left(-\dfrac m3\right)+m-2=-\dfrac{2m}3-2=-\dfrac{2(m+3)}3$（在 $x$ 轴下方）．" "\n"
        r"**算面积**：$\lvert AB\rvert=\dfrac{2-m}5-(-m-2)=\dfrac{2-m+5m+10}5=\dfrac{4(m+3)}5$，高 $=\dfrac{2(m+3)}3$．" "\n"
        r"$S=\dfrac12\lvert AB\rvert\cdot\dfrac{2(m+3)}3=\dfrac12\cdot\dfrac{4(m+3)}5\cdot\dfrac{2(m+3)}3=\dfrac{4(m+3)^{2}}{15}$．" "\n"
        r"由 $S>60$：$\dfrac{4(m+3)^{2}}{15}>60\Rightarrow(m+3)^{2}>225\Rightarrow m+3>15$（因 $m>0$）$\Rightarrow m>12$．" "\n"
        r"故 $m\in(12,+\infty)$．"
    ),
    'review': (
        r"★ 题干、答案完整 ✓。原书 p418 详解：" "\n"
        r"「②可化为 $-9-m\le3x+m\le9+m$，解得 $\frac{-9-2m}{3}\lex\le3$。$\because$ 不等式 $f(x)$ 的解集为 $[-1,3]$，" "\n"
        r"$\therefore\frac{-9-2m}{3}=-1$，解得 $m=-3$」✓✓" "\n"
        r"「$g(x)=\lvert3x+m\rvert-2\lvert x-1\rvert$。又 $m>0$，$\therefore g(x)=\begin{cases}-x-m-2&(x\le-\frac m3)\\5x+m-2&(-\frac m3<x<1)\\x+m+2&(x\ge1)\end{cases}$ …" "\n"
        r"$B(\frac{2-m}5,0)$，$C(-\frac m3,-\frac{2m}3-2)$ …$S_{\triangle ABC}=\frac12\lvert AB\rvert\cdot y_C=\frac{4(m+3)^2}{15}>60$，解得 $m>12$，为 $(12,+\infty)$」" "\n"
        r"—— **三段表达式、$C$ 点坐标、面积公式、结论全部与我的推导一致** ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **（1）**：$\lvert3x+m\rvert\le9+m\Rightarrow-(9+m)\le3x+m\le9+m$ ✓" "\n"
        r"左：$-9-m-m=-9-2m\le3x$ ⟹ $x\ge\frac{-9-2m}{3}$ ✓；右：$3x\le9+m-m=9$ ⟹ $x\le3$ ✓✓✓" "\n"
        r"$m=-3$：$x\ge\frac{-9+6}{3}=\frac{-3}{3}=-1$ ✓✓✓ **解集 $[-1,3]$ 完全吻合**" "\n"
        r"② **分段表达式**：$x\le-\frac m3$ 时 $3x+m\le0$、$x-1<0$ ⟹ $-(3x+m)-2(1-x)=-3x-m-2+2x=-x-m-2$ ✓✓" "\n"
        r"$-\frac m3<x<1$ 时 $3x+m>0$、$x-1<0$ ⟹ $(3x+m)+2(x-1)=5x+m-2$ ✓✓" "\n"
        r"$x\ge1$ 时 $3x+m>0$、$x-1\ge0$ ⟹ $(3x+m)-2(x-1)=x+m+2$ ✓✓✓" "\n"
        r"③ **$g(-\frac m3)=5(-\frac m3)+m-2=-\frac{5m}3+\frac{3m}3-2=-\frac{2m}3-2$** ✓✓✓" "\n"
        r"④ **$\lvert AB\rvert$**：$\frac{2-m}{5}+m+2=\frac{2-m+5m+10}{5}=\frac{4m+12}{5}=\frac{4(m+3)}{5}$ ✓✓" "\n"
        r"⑤ **面积**：$\frac12\cdot\frac{4(m+3)}{5}\cdot\frac{2(m+3)}{3}=\frac{8(m+3)^2}{30}=\frac{4(m+3)^2}{15}$ ✓✓✓" "\n"
        r"⑥ **数值检验**：取 $m=13$（应 $>12$）：$S=\frac{4(16)^2}{15}=\frac{1024}{15}=68.27>60$ ✓✓" "\n"
        r"取 $m=12$：$S=\frac{4(225)}{15}=60$，**恰好等于 $60$** ⟹ 必须 $m>12$（开区间）✓✓✓" "\n"
        r"取 $m=3$：$S=\frac{4\cdot36}{15}=9.6<60$ ✗ 正确排除 ✓" "\n"
        r"⑦ **折点位置**：$m=13$ 时 $C=(-\frac{13}{3},-\frac{32}{3})=(-4.333,-10.667)$。" "\n"
        r"$A=(-15,0)$、$B=(\frac{-11}{5},0)=(-2.2,0)$。$\lvert AB\rvert=12.8=\frac{4\cdot16}{5}$ ✓✓" "\n"
        r"$S=\frac12\cdot12.8\cdot10.667=68.27$ ✓✓✓ **与公式一致**" "\n"
        r"**答案（1）$m=-3$、（2）$(12,+\infty)$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（折线与 $x$ 轴围成的面积）**：" "\n"
        r"① ⭐⭐ **三段去绝对值的标准流程**：先由参数定出分界点的**大小顺序**（本题 $m>0\Rightarrow-\frac m3<1$），" "\n"
        r"再逐段判断每个绝对值内式子的符号，**符号判错整段就错**；" "\n"
        r"② ⭐ **求零点后必须检验该零点是否落在本段区间内** —— 本题第三段解出 $x=-m-2$ 但要求 $x\ge1$，" "\n"
        r"必须舍去，否则会多出一个零点、面积全错；" "\n"
        r"③ ⭐ **顶点是「折点」不是零点**：三角形第三个顶点 $C$ 是两段直线的交点（即分界点处的函数值），" "\n"
        r"用 $g(-\frac m3)$ 算，千万别去联立两条直线；" "\n"
        r"④ 面积 $=\frac12\lvert AB\rvert\cdot\lvert y_C\rvert$，$A,B$ 是两个零点（底边在 $x$ 轴上）；" "\n"
        r"⑤ ⚠ **「$m=-3$」与「$m>0$」分属两问**，第（2）问是重新设 $m>0$，不要试图让两者统一 —— 教辅常见写法。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-025'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-025-V3',
}

T027_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=\lvert x-3\rvert-\lvert x-a\rvert$．"
        "\n（1）当 $a=2$ 时，解不等式 $f(x)\le-\dfrac12$；"
        "\n（2）若存在实数 $x$，使得不等式 $f(x)\ge a$ 成立，求实数 $a$ 的取值范围．"
    ),
    'opts': [],
    'answer': r"（1）$\left[\dfrac{11}4,+\infty\right)$；（2）$\left(-\infty,\dfrac32\right]$",
    'analysis': (
        r"（1）$a=2$ 时分 $x\le2$、$2<x<3$、$x\ge3$ 三段，第一、三段为常数 $\pm1$；"
        r"（2）$\max f=\lvert a-3\rvert$（三角不等式），「存在 $x$ 使 $f(x)\ge a$」$\Longleftrightarrow\lvert a-3\rvert\ge a$。"
    ),
    'solution': (
        r"**（1）** $a=2$ 时 $f(x)=\lvert x-3\rvert-\lvert x-2\rvert$．分界点为 $2,3$：" "\n"
        r"$\bullet\$ 当 $x\le2$ 时：$f(x)=(3-x)-(2-x)=1$，要求 $1\le-\dfrac12$，无解；" "\n"
        r"$\bullet\$ 当 $2<x<3$ 时：$f(x)=(3-x)-(x-2)=5-2x$，要求 $5-2x\le-\dfrac12\Rightarrow2x\ge\dfrac{11}2\Rightarrow x\ge\dfrac{11}4$；" "\n"
        r"结合 $2<x<3$ 得 $\dfrac{11}4\le x<3$；" "\n"
        r"$\bullet\$ 当 $x\ge3$ 时：$f(x)=(x-3)-(x-2)=-1$，要求 $-1\le-\dfrac12$，恒成立，得 $x\ge3$．" "\n"
        r"综上，解集为 $\left[\dfrac{11}4,3\right)\cup[3,+\infty)=\left[\dfrac{11}4,+\infty\right)$．" "\n"
        r"**（2）** 先求 $f$ 的最大值．由绝对值三角不等式：" "\n"
        r"$f(x)=\lvert x-3\rvert-\lvert x-a\rvert\le\bigl\lvert(x-3)-(x-a)\bigr\rvert=\lvert a-3\rvert$，" "\n"
        r"且当 $x$ 取在 $a$ 与 $3$ 之外（与较大者同侧）时可取到等号，故 $f_{\max}=\lvert a-3\rvert$．" "\n"
        r"「存在实数 $x$ 使 $f(x)\ge a$」$\Longleftrightarrow f_{\max}\ge a\Longleftrightarrow\lvert a-3\rvert\ge a$．" "\n"
        r"$\bullet\$ 若 $a\ge3$：$\lvert a-3\rvert=a-3\ge a\Rightarrow-3\ge0$，矛盾，无解；" "\n"
        r"$\bullet\$ 若 $a<3$：$\lvert a-3\rvert=3-a\ge a\Rightarrow3\ge2a\Rightarrow a\le\dfrac32$（满足 $a<3$ ✓）．" "\n"
        r"故 $a\in\left(-\infty,\dfrac32\right]$．"
    ),
    'review': (
        r"★ 题干、答案完整 ✓。原书 p419 详解：" "\n"
        r"「当 $x\ge3$ 时 …$-1\le-\frac12$ 成立，则有 $x\ge3$；当 $x\le2$ 时 …$1\le-\frac12$，解得 $x\in\varnothing$；" "\n"
        r"当 $2<x<3$ 时 …$5-2x\le-\frac12$，解得 $x\ge\frac{11}4$，则有 $\frac{11}4\lex<3$ …" "\n"
        r"则原不等式的解集为 $[\frac{11}4,3)\cup[3,+\infty)$ 即为 $[\frac{11}4,+\infty)$」✓✓✓" "\n"
        r"「由绝对值不等式的性质可得 $\bigl\lvert\lvert x-3\rvert-\lvert x-a\rvert\bigr\rvert\le\lvert a-3\rvert$，即有 $f(x)$ 的最大值为 $\lvert a-3\rvert$。" "\n"
        r"若存在实数 $x$，使得不等式 $f(x)\gea$ 成立，则有 $\lvert a-3\rvert\gea$ …即 $a\in\varnothing$ 或 $a\le\frac32$。所以 $a$ 的取值范围是 $(-\infty,\frac32]$」" "\n"
        r"—— **与我的推导完全一致** ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **（1）第一段**：$x\le2$ 时 $\lvert x-3\rvert=3-x$、$\lvert x-2\rvert=2-x$，$f=(3-x)-(2-x)=1$ ✓✓" "\n"
        r"$1\le-\frac12$ 不成立 ⟹ 无解 ✓✓" "\n"
        r"② **第二段**：$2<x<3$ 时 $f=(3-x)-(x-2)=5-2x$ ✓；$5-2x\le-\frac12\Rightarrow-2x\le-5.5\Rightarrowx\ge2.75=\frac{11}4$ ✓✓✓" "\n"
        r"③ **第三段**：$x\ge3$ 时 $f=(x-3)-(x-2)=-1$ ✓；$-1\le-0.5$ 恒成立 ✓✓" "\n"
        r"④ **合并**：$[\frac{11}4,3)\cup[3,+\infty)=[\frac{11}4,+\infty)$ ✓✓✓" "\n"
        r"（$x=3$ 时 $f=-1\le-\frac12$ ✓，两段可以合并）" "\n"
        r"⑤ **（2）$f_{\max}=\lvert a-3\rvert$**：取 $a=0$，$f(x)=\lvert x-3\rvert-\lvert x\rvert$。" "\n"
        r"$x\le0$：$f=3-x+x=3=\lvert0-3\rvert$ ✓✓ **取到最大值**" "\n"
        r"$x\ge3$：$f=x-3-x=-3$（最小值 $-\lvert a-3\rvert$）✓ 合理" "\n"
        r"⑥ **$\lvert a-3\rvert\gea$ 分两类**：" "\n"
        r"$a\ge3$：$a-3\gea\Rightarrow-3\ge0$ ✗ **无解正确** ✓✓" "\n"
        r"$a<3$：$3-a\gea\Rightarrowa\le\frac32$ ✓✓✓" "\n"
        r"⑦ **端点检验**：$a=\frac32$：$f_{\max}=\lvert1.5-3\rvert=1.5=a$ ✓ 恰好取等 ⟹ **闭区间正确** ✓✓" "\n"
        r"$a=2$（$>\frac32$）：$f_{\max}=\lvert-1\rvert=1<2$ ✗ 不存在这样的 $x$ ✓✓ **排除正确**" "\n"
        r"⑧ **$a=0$ 检验**：$f_{\max}=3\ge0$ ✓ 存在（如 $x\le0$ 时 $f=3\ge0$）✓✓" "\n"
        r"**答案（1）$[\frac{11}4,+\infty)$、（2）$(-\infty,\frac32]$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（差的绝对值）**：" "\n"
        r"① ⭐⭐ **$\bigl\lvert\lvert u\rvert-\lvert v\rvert\bigr\rvert\le\lvert u-v\rvert$** —— 求 $f=\lvert x-p\rvert-\lvert x-q\rvert$ 的**最值**用它：" "\n"
        r"$f_{\max}=\lvert p-q\rvert$，$f_{\min}=-\lvert p-q\rvert$，且都在 $x$ 取到 $p,q$ 之外的区间时达到；" "\n"
        r"（对照 M-T-025-E1 的 $\lvert u\rvert+\lvert v\rvert\ge\lvert u-v\rvert$ 求**最小值**，两者是孪生工具）" "\n"
        r"② ⭐ **分段时先算两端区间**：本题 $x\le2$ 与 $x\ge3$ 两段 $f$ 分别是常数 $1$ 和 $-1$，" "\n"
        r"只有中间段含 $x$ —— 先算常数段能快速排除一半情形；" "\n"
        r"③ ⚠ **解集要合并**：$[\frac{11}4,3)$ 与 $[3,+\infty)$ 在 $x=3$ 处相接，必须并成 $[\frac{11}4,+\infty)$；" "\n"
        r"④ ⚠ **「存在 $x$ 使 $f(x)\gea$」是 $f_{\max}\gea$，不是 $f_{\min}\gea$** —— 与 M-T-025-E1(2) 对照记忆；" "\n"
        r"⑤ 解 $\lvert a-3\rvert\gea$ 这类含参绝对值不等式，**按绝对值内部符号分两类**，别两边平方（会引入增根）。"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-027'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-027-E1',
}

T027_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=\lvert2x+1\rvert-\lvert x\rvert-2$．"
        "\n（1）解不等式 $f(x)\ge0$；"
        "\n（2）若存在实数 $x$，使得 $f(x)\le\lvert x\rvert+a$，求实数 $a$ 的取值范围．"
    ),
    'opts': [],
    'answer': r"（1）$(-\infty,-3]\cup[1,+\infty)$；（2）$a\ge-3$",
    'analysis': (
        r"（1）移项成 $\lvert2x+1\rvert-\lvert x\rvert\ge2$，按 $x=-\frac12,0$ 分三段；"
        r"（2）移项成 $\lvert2x+1\rvert-2\lvert x\rvert\le a+2$，令 $h(x)=\lvert2x+1\rvert-2\lvert x\rvert$，"
        r"「存在 $x$」$\Longleftrightarrow\min h\le a+2$，而 $\min h=-1$。"
    ),
    'solution': (
        r"**（1）** $f(x)\ge0\Longleftrightarrow\lvert2x+1\rvert-\lvert x\rvert\ge2$．分界点为 $-\dfrac12,0$：" "\n"
        r"$\bullet\$ 当 $x\le-\dfrac12$ 时：$\lvert2x+1\rvert=-(2x+1)$、$\lvert x\rvert=-x$，" "\n"
        r"左边 $=-(2x+1)+x=-x-1\ge2\Rightarrow x\le-3$（满足 $x\le-\frac12$ ✓）；" "\n"
        r"$\bullet\$ 当 $-\dfrac12<x<0$ 时：$\lvert2x+1\rvert=2x+1$、$\lvert x\rvert=-x$，" "\n"
        r"左边 $=2x+1+x=3x+1\ge2\Rightarrow x\ge\dfrac13$，与 $-\dfrac12<x<0$ 矛盾，无解；" "\n"
        r"$\bullet\$ 当 $x\ge0$ 时：$\lvert2x+1\rvert=2x+1$、$\lvert x\rvert=x$，" "\n"
        r"左边 $=2x+1-x=x+1\ge2\Rightarrow x\ge1$（满足 $x\ge0$ ✓）．" "\n"
        r"综上，解集为 $(-\infty,-3]\cup[1,+\infty)$．" "\n"
        r"**（2）** $f(x)\le\lvert x\rvert+a\Longleftrightarrow\lvert2x+1\rvert-\lvert x\rvert-2\le\lvert x\rvert+a \Longleftrightarrow\lvert2x+1\rvert-2\lvert x\rvert\le a+2$．" "\n"
        r"令 $h(x)=\lvert2x+1\rvert-2\lvert x\rvert$，同（1）分三段：" "\n"
        r"$h(x)=\begin{cases}-(2x+1)+2x=-1, & x\le-\dfrac12\\[2mm]" "\n"
        r"(2x+1)+2x=4x+1, & -\dfrac12<x<0\\[2mm]" "\n"
        r"(2x+1)-2x=1, & x\ge0\end{cases}$" "\n"
        r"第一段恒为 $-1$；第二段 $4x+1\in(-1,1)$；第三段恒为 $1$．故 $h_{\min}=-1$（在 $x\le-\frac12$ 时取到）．" "\n"
        r"「存在实数 $x$ 使 $h(x)\lea+2$」$\Longleftrightarrow h_{\min}\lea+2\Longleftrightarrow-1\lea+2\Rightarrowa\ge-3$．"
    ),
    'review': (
        r"★ 题干、答案完整 ✓（**详解未提取**，上述推导为我独立完成）。" "\n"
        r"答案与原书标注一致：（1）$(-\infty,-3]\cup\ [1,+\infty)$；（2）$a\ge-3$ ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **（1）第一段**：$x\le-\frac12$：$-(2x+1)-(-x)=-2x-1+x=-x-1\ge2\Rightarrowx\le-3$ ✓✓" "\n"
        r"$x=-3$：$\lvert-5\rvert-3-2=5-5=0\ge0$ ✓（边界取等）" "\n"
        r"$x=-4$：$\lvert-7\rvert-4-2=7-6=1\ge0$ ✓✓" "\n"
        r"② **第二段**：$-\frac12<x<0$：$(2x+1)-(-x)=3x+1\ge2\Rightarrowx\ge\frac13$ ✗ 与区间矛盾 ✓ **无解正确**" "\n"
        r"$x=-0.25$：$\lvert0.5\rvert-0.25-2=0.5-2.25=-1.75<0$ ✓ **确实不满足**" "\n"
        r"③ **第三段**：$x\ge0$：$(2x+1)-x=x+1\ge2\Rightarrowx\ge1$ ✓✓" "\n"
        r"$x=1$：$3-1-2=0\ge0$ ✓（边界取等）；$x=0$：$1-0-2=-1<0$ ✗ **不在解集** ✓✓✓" "\n"
        r"④ **（2）$h(x)$ 分段**：" "\n"
        r"$x\le-\frac12$：$-(2x+1)-2(-x)=-2x-1+2x=-1$ ✓✓ **恒为 $-1$**" "\n"
        r"$-\frac12<x<0$：$(2x+1)-2(-x)=4x+1$，$x\in(-\frac12,0)\Rightarrow4x+1\in(-1,1)$ ✓✓" "\n"
        r"$x\ge0$：$(2x+1)-2x=1$ ✓✓ **恒为 $1$**" "\n"
        r"⟹ $h_{\min}=-1$ ✓✓✓" "\n"
        r"⑤ **$a\ge-3$ 检验**：$a=-3$ 时需 $h(x)\le-1$，取 $x=-1$（$\le-\frac12$）：$h=-1\le-1$ ✓ **恰好存在** ⟹ 闭 ✓✓" "\n"
        r"$a=-4$：需 $h(x)\le-2$，但 $h\ge-1$ 恒成立 ✗ **不存在** ✓✓✓ **边界正确**" "\n"
        r"$a=0$：需 $h(x)\le2$，$h\le1<2$ 恒成立 ✓ 存在 ✓" "\n"
        r"⑥ **与（1）的联系**：（1）是 $h(x)-2\ge0$ 即 $h(x)\ge2$ 解集为空的部分…" "\n"
        r"（实际（1）解集 $(-\infty,-3]\cup[1,+\infty)$ 对应 $f\ge0$，与（2）是独立两问，各自成立）✓" "\n"
        r"**答案（1）$(-\infty,-3]\cup[1,+\infty)$、（2）$a\ge-3$ 正确** ✓" "\n"
        r"**⭐ 通法（移项构造 + 存在性）**：" "\n"
        r"① ⭐⭐ **（2）的关键是把 $a$ 单独留在右边**：把 $\lvert x\rvert$ 移到左边与 $f$ 中的 $-\lvert x\rvert$ 合并成 $-2\lvert x\rvert$，" "\n"
        r"于是左边变成一个**与 $a$ 无关的函数 $h(x)$**，问题化为「$\min h\lea+2$」—— " "\n"
        r"**凡是求参数范围，第一步都是「分离参数」**；" "\n"
        r"② ⭐ **分段后先找「常数段」**：本题第一段恒 $-1$、第三段恒 $1$，一眼就看出最小值在常数段，" "\n"
        r"中间那段只需确认它不超出 $[-1,1]$；" "\n"
        r"③ ⚠ **「存在 $x$ 使 $h(x)\let$」$\iff\min h\let$**（存在 ⟹ 最松），别记成 $\max$；" "\n"
        r"④ 分界点是**每个绝对值内部为零的点**（本题 $-\frac12$ 与 $0$），不是 $\pm2$ 之类；" "\n"
        r"⑤ 检验时**代入边界值**（$a=-3$ 恰好取等、$a=-4$ 不存在）能同时确认闭开与方向。"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-027'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-027-V2',
}

QS = [T025_E1, T025_V2, T025_V3, T027_E1, T027_V2]
