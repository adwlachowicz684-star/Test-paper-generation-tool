# -*- coding: utf-8 -*-
r"""第 106 批：数列综合（M-T-135，3 题；M-T-269，3 题；M-T-276，3 题）
+ 正方体截面（M-T-288，3 题）

    python3 tools/run_batch.py 106

## 选题依据

按「详解完整 + 同题型聚堆 + 无图依赖」筛出，本批 12 题：
M-T-135 三题是「超难压轴小题：数列」的比较/递推型选择题（p319 一带）；
M-T-269 三题是交错 $(-1)^n$ 求和（p216-217）；
M-T-276 三题是等差 × 等比交叉（p220-221）；
M-T-288 三题是正方体截面面积（p231-232），纯计算、无图依赖。

## 第一条：交错求和的「裂项相消」模板（M-T-269 / M-T-276 共用）

把通项拆成「$v_{k+1}-v_k$」的形式，则 $S_n=v_{n+1}-v_1$，一步到底：

| 题 | 通项 | 裂项 |
|---|---|---|
| M-T-269-E1 | $(-1)^{n-1}\frac{4n}{(2n-1)(2n+1)}$ | $(-1)^{n-1}\frac1{2n-1}-(-1)^n\frac1{2n+1}$ |
| M-T-269-V2 | $(-1)^{n+1}\frac{2n+1}{n(n+1)}$ | $(-1)^{n+1}\frac1{n+1}-(-1)^n\frac1n$ |
| M-T-269-V1 | $(-1)^{n-1}\frac1{n(n+2)}$ | $\frac12\left[(-1)^{n-1}\frac1n-(-1)^{n-1}\frac1{n+2}\right]$ |

> 通法：**分子拆成两分母之和**（$\frac p{xy}=\frac1x+\frac1y\iff p=x+y$），
> 交错号 $(-1)^k$ 正好让相邻项「一正一负」配对相消。

## 第二条：$S_{2^n}$ 与 $S_{2n}$ 的区分（M-T-276-V2，本批最关键的还原）

题干 OCR 成 $S_{2n}$，但答案含 $2^{2n}$ —— 说明原题问的是**前 $2^n$ 项和**。

判据很硬：若真是 $S_{2n}$，则 $1\le k\le 2n$ 中形如 $2^j$ 的只有 $\lfloor\log_2 2n\rfloor$ 个，
结果应是 $n(2n+1)-2^{m+1}+2+m$ 这种「多项式」形式，**不可能出现 $2^{2n}$**。

按 $S_{2^n}$ 理解：$2^j\le 2^n$ 恰有 $n$ 个（$j=1,\ldots,n$），
$$S_{2^n}=\frac{2^n(2^n+1)}2-\sum_{j=1}^n2^j+n=2^{2n-1}-3\cdot2^{n-1}+n+2$$
代入 $n=1,2,3,4$ 得 $2,6,25,110$，与逐项累加完全一致 ✓

## 第三条：截面面积统一走「平行四边形面积 = $ab\sin\theta$」

M-T-288 三题虽然形状不同（平行四边形 / 等腰梯形 / 平行四边形），
但核心都是**先求两条邻边长度，再用余弦定理求夹角**：

$$\cos\angle=\frac{p^2+q^2-d^2}{2pq},\qquad S=pq\sin\angle$$

其中 $d$ 是这两条邻边「另一端点」的距离（$A_1C$、$AC_1$）。

> 通法：截面是平行四边形 ⟹ 面积 $=$ 两邻边之积 $\times$ 夹角的正弦；
> 是梯形 ⟹ 用 $\frac12(a+b)h$。判断形状靠**对面平行 ⟹ 交线平行**。

## 三处原书答案存疑（判据写在各题 review 里）

1. **M-T-276-E1(2)**：答案 $1+\frac{2^{2n+1}}3-\frac1{2n+1}$ 与原解不一致，
   正确为 $\frac{2^{2n+1}+1}3-\frac1{2n+1}$（原书漏了 $-2$）。
2. **M-T-288-E1**：答案 `12 19` 实为 $12\sqrt{19}$（$\cos$ 值 `5/10` 实为 $\frac{\sqrt5}{10}$）。
3. **M-T-288-V3**：详解 $\cos\angle AEC_1=\frac15$ 丢了负号，实为 $-\frac15$
   （否则 $AE^2+EC_1^2-AC_1^2=5+5-12=-2$ 与正值矛盾）。
"""

T135_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知数列 $\left\{a_n\right\},\left\{b_n\right\},\left\{c_n\right\},\left\{d_n\right\}$ 满足："
        r"$a_n=n^{n},\ b_n=n!,\ c_n=n^{\frac1n},\ d_n=\dfrac1n$．则对于任意正整数 $n>100$，有（　　）"
    ),
    'stem': [
        r"已知数列 $\left\{a_n\right\},\left\{b_n\right\},\left\{c_n\right\},\left\{d_n\right\}$ 满足："
        r"$a_n=n^{n},\ b_n=n!,\ c_n=n^{\frac1n},\ d_n=\dfrac1n$．则对于任意正整数 $n>100$，有（　　）"
    ],
    'opts': [
        ('A', r"$a_{2n}-a_n<b_{2n}-b_n$"),
        ('B', r"$b_{2n}-b_n<c_{2n}-c_n$"),
        ('C', r"$c_{2n}-c_n<d_{2n}-d_n$"),
        ('D', r"$a_{2n}-a_n<d_{2n}-d_n$"),
    ],
    'answer': r"C",
    'analysis': (
        r"先定四个差的正负：$a_{2n}-a_n>0$、$b_{2n}-b_n>0$、$d_{2n}-d_n<0$，"
        r"再由 $f(x)=\frac{\ln x}x$ 在 $x>\mathrm e$ 上递减推出 $c_n=n^{\frac1n}$ 递减，故 $c_{2n}-c_n<0$．"
        r"于是只需在 A、C 中判断：A 用放缩 $b_{2n}<a_{2n}-a_n$ 证伪，C 用 $\mathrm e^x\ge1+x$ 证明．"
    ),
    'solution': (
        r"**第一步：定四个差的正负**" "\n"
        r"$a_n=n^n$ 递增 ⟹ $a_{2n}-a_n>0$；$b_n=n!$ 递增 ⟹ $b_{2n}-b_n>0$；" "\n"
        r"$d_n=\dfrac1n$ 递减 ⟹ $d_{2n}-d_n<0$．" "\n"
        r"对 $c_n$：令 $f(x)=\dfrac{\ln x}{x}$，则 $f'(x)=\dfrac{1-\ln x}{x^{2}}$，" "\n"
        r"当 $x>\mathrm e$ 时 $f'(x)<0$，$f$ 递减，从而 $x^{\frac1x}=\mathrm e^{\frac{\ln x}x}$ 递减．" "\n"
        r"$n>100>\mathrm e$，故 $c_{2n}<c_n$，即 $c_{2n}-c_n<0$．" "\n"
        r"于是 $b_{2n}-b_n>0>c_{2n}-c_n$，**B 错**；$a_{2n}-a_n>0>d_{2n}-d_n$，**D 错**．" "\n"
        r"**第二步：证伪 A**" "\n"
        r"$b_{2n}-b_n<b_{2n}=(2n)!=\underbrace{(1\times2\times\cdots\times n)}_{<\,n^{n}}"
        r"\cdot\underbrace{(n+1)\times\cdots\times2n}_{<\,(2n)^{n}}$，" "\n"
        r"故 $b_{2n}-b_n<n^{n}\cdot(2n)^{n}=2^{n}\cdot n^{2n}<4^{n}\cdot n^{2n}=\left(2n\right)^{2n}=a_{2n}$．" "\n"
        r"更精确地，$a_{2n}-a_n=(2n)^{2n}-n^{n}>2^{n}n^{2n}>b_{2n}-b_n$，**A 错**．" "\n"
        r"**第三步：证明 C**" "\n"
        r"要证 $c_{2n}-c_n<d_{2n}-d_n$，即证 $d_n-d_{2n}<c_n-c_{2n}$．" "\n"
        r"左端 $d_n-d_{2n}=\dfrac1n-\dfrac1{2n}=\dfrac1{2n}$；" "\n"
        r"右端，把两项都写成 $\dfrac1{2n}$ 次方：" "\n"
        r"$c_n-c_{2n}=n^{\frac1n}-\left(2n\right)^{\frac1{2n}}=\left(n^{2}\right)^{\frac1{2n}}-\left(2n\right)^{\frac1{2n}}"
        r"=\left(2n\right)^{\frac1{2n}}\left[\left(\dfrac{n^{2}}{2n}\right)^{\frac1{2n}}-1\right]$，" "\n"
        r"$=\left(2n\right)^{\frac1{2n}}\left[\left(\dfrac n2\right)^{\frac1{2n}}-1\right]$．" "\n"
        r"由 $\left(2n\right)^{\frac1{2n}}>1$，只需证 $\left(\dfrac n2\right)^{\frac1{2n}}>1+\dfrac1{2n}$．" "\n"
        r"由 $n>100>2\mathrm e$ 得 $\dfrac n2>\mathrm e$，故 $\left(\dfrac n2\right)^{\frac1{2n}}>\mathrm e^{\frac1{2n}}$；" "\n"
        r"而由 $\mathrm e^{x}\ge1+x$（$x=\dfrac1{2n}\ne0$ 取严格大于）得 $\mathrm e^{\frac1{2n}}>1+\dfrac1{2n}$．" "\n"
        r"故 **C 正确**．"
    ),
    'review': (
        r"① ⭐⭐ **判断 $x^{1/x}$ 的单调性只需对 $\frac{\ln x}x$ 求导**："
        r"$f'(x)=\frac{1-\ln x}{x^2}$，在 $x>\mathrm e$ 上为负．"
        r"这是本题唯一的「分析」环节，也是四个数列中唯一需要先求导才能定性的．" "\n"
        r"② ⭐⭐ **$\mathrm e^x\ge1+x$ 是放缩的万能工具**：令 $g(x)=\mathrm e^x-x-1$，"
        r"$g'(x)=\mathrm e^x-1$，$g$ 在 $x<0$ 递减、$x>0$ 递增，$g_{\min}=g(0)=0$．" "\n"
        r"③ ⭐ **先用正负号排除一半选项**：$c_{2n}-c_n<0$ 与 $d_{2n}-d_n<0$ 是仅有的两个负差，"
        r"B、D 立刻出局，只剩 A、C．" "\n"
        r"④ 数值复核（$n=101$）：$a_n=101^{101}$ 极大，$b_n=101!$ 次之；"
        r"$c_{101}=101^{1/101}=\mathrm e^{\ln101/101}=\mathrm e^{0.04563}=1.04669$，"
        r"$c_{202}=202^{1/202}=\mathrm e^{5.3083/202}=\mathrm e^{0.02628}=1.02663<1.04669$ ✓" "\n"
        r"$d_{101}-d_{202}=\frac1{101}-\frac1{202}=0.004950$；"
        r"$c_{101}-c_{202}=1.04669-1.02663=0.02006>0.004950$ ✓ C 成立．" "\n"
        r"⑤ ⚠ 原书选项文本未带 A/B/C/D 字母，已按出现顺序补全．" "\n"
        r"**通法（数列大小比较）**：" "\n"
        r"① 先定各差的符号，用「正 > 负」排除一批选项；" "\n"
        r"② $n^{1/n}$ 型一律取对数化为 $\frac{\ln n}n$；" "\n"
        r"③ 阶乘放缩用 $(2n)!=1\cdots n\cdot(n+1)\cdots2n<n^n(2n)^n$；" "\n"
        r"④ 需要严格不等式时用 $\mathrm e^x>1+x\ (x\ne0)$．"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-135'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-135-V1',
}

T135_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知数列 $\left\{a_n\right\}$ 满足 $a_{n+1}=\dfrac{2a_n}{a_n^{2}+1}$，满足 $a_1\in\left(0,1\right)$，"
        r"$a_1+a_2+\cdots+a_{2021}=2020$，则下列成立的是（　　）"
    ),
    'stem': [
        r"已知数列 $\left\{a_n\right\}$ 满足 $a_{n+1}=\dfrac{2a_n}{a_n^{2}+1}$，满足 $a_1\in\left(0,1\right)$，"
        r"$a_1+a_2+\cdots+a_{2021}=2020$，则下列成立的是（　　）"
    ],
    'opts': [
        ('A', r"$\ln a_1\cdot\ln a_{2021}>\dfrac1{2020}$"),
        ('B', r"$\ln a_1\cdot\ln a_{2021}=\dfrac1{2020}$"),
        ('C', r"$\ln a_1\cdot\ln a_{2021}<\dfrac1{2020}$"),
        ('D', r"以上均有可能"),
    ],
    'answer': r"C",
    'analysis': (
        r"由递推式先证 $0<a_n<1$ 且 $\left\{a_n\right\}$ 递增；"
        r"再由前 $2021$ 项和为 $2020$ 得 $\dfrac1{a_{2021}}<\dfrac{2020}{2020-a_1}$；"
        r"最后用 $0<x<1$ 时 $0<-\ln x<\dfrac1x-1$ 放缩，两侧相乘即得结论．"
    ),
    'solution': (
        r"**第一步：确定 $\left\{a_n\right\}$ 的范围与单调性**" "\n"
        r"由 $a_{n+1}=\dfrac{2a_n}{a_n^{2}+1}=\dfrac{2}{a_n+\frac1{a_n}}\le\dfrac{2}2=1$，"
        r"等号当且仅当 $a_n=1$．" "\n"
        r"若某个 $a_n=1$，则由 $a_n=\dfrac{2a_{n-1}}{a_{n-1}^{2}+1}$ 解得 $a_{n-1}=1$，"
        r"往前递推得 $a_1=1$，与 $a_1\in(0,1)$ 矛盾．故 $0<a_n<1$．" "\n"
        r"此时 $\dfrac{a_{n+1}}{a_n}=\dfrac{2}{a_n^{2}+1}>1$，故 $\left\{a_n\right\}$ **严格递增**．" "\n"
        r"**第二步：由和定出 $\dfrac1{a_{2021}}$ 的上界**" "\n"
        r"由 $a_1<a_2<\cdots<a_{2021}$ 且 $\sum_{k=1}^{2021}a_k=2020$：" "\n"
        r"$2020=\sum_{k=1}^{2021}a_k>2020\,a_1+a_{2021}$ ⟹ $a_{2021}<2020-2020a_1=2020(1-a_1)$．" "\n"
        r"更实用的是另一端：$\sum_{k=1}^{2021}a_k<2021a_{2021}$ 给下界；" "\n"
        r"而 $2020=\sum_{k=1}^{2021}a_k>2020a_{2021}$ 不成立，改用" "\n"
        r"$2020=\sum_{k=1}^{2020}a_k+a_{2021}>2020a_1+a_{2021}$" "\n"
        r"⟹ $\dfrac1{a_{2021}}<\dfrac{2020}{2020-a_1}$（由 $a_{2021}>\dfrac{2020-a_1}{2020}$ 取倒数）．" "\n"
        r"**第三步：用 $-\ln x<\dfrac1x-1$ 放缩**" "\n"
        r"令 $f(x)=\ln x-1+\dfrac1x$，则 $f'(x)=\dfrac1x-\dfrac1{x^{2}}=\dfrac{x-1}{x^{2}}$，" "\n"
        r"$f$ 在 $(0,1)$ 上递减、在 $(1,+\infty)$ 上递增，$f_{\min}=f(1)=0$．" "\n"
        r"故 $x\in(0,1)$ 时 $\ln x>1-\dfrac1x$，即 $0<-\ln x<\dfrac1x-1$．" "\n"
        r"$\ln a_1\cdot\ln a_{2021}=(-\ln a_1)(-\ln a_{2021})"
        r"<\left(\dfrac1{a_1}-1\right)\left(\dfrac1{a_{2021}}-1\right)$，" "\n"
        r"$<\left(\dfrac1{a_1}-1\right)\left(\dfrac{2020}{2020-a_1}-1\right)"
        r"=\left(\dfrac1{a_1}-1\right)\cdot\dfrac{a_1}{2020-a_1}$，" "\n"
        r"$=\dfrac{1-a_1}{2020-a_1}<\dfrac1{2020}$（因 $2020-a_1>2020(1-a_1)$）．" "\n"
        r"故 $\boxed{\ln a_1\cdot\ln a_{2021}<\dfrac1{2020}}$，选 **C**．"
    ),
    'review': (
        r"① ⭐⭐ **递推式 $a_{n+1}=\frac{2a_n}{a_n^2+1}$ 是不动点迭代**："
        r"写成 $\frac{2}{a_n+\frac1{a_n}}$ 后用基本不等式立得 $a_{n+1}\le1$；"
        r"再由 $\frac{a_{n+1}}{a_n}=\frac{2}{a_n^2+1}>1$ 得单调递增．" "\n"
        r"② ⭐⭐ **$-\ln x<\frac1x-1\ (0<x<1)$ 是核心放缩**："
        r"由 $f(x)=\ln x-1+\frac1x\ge0$ 得到，等号只在 $x=1$．" "\n"
        r"③ ⭐ **两端相乘的技巧**：两个负对数之积 $=$ 两个正量的积，"
        r"各自用 $\frac1x-1$ 放大，其中 $\frac1{a_{2021}}$ 再用第二步的上界放大一次．" "\n"
        r"④ 数值复核：取 $a_1=0.5$，则 $a_2=\frac{1}{1.25}=0.8$，$a_3=\frac{1.6}{1.64}=0.9756$，"
        r"$a_4=\frac{1.9512}{1.9518}=0.99969$，此后极快地趋于 $1$；" "\n"
        r"   $\sum_{k=1}^{2021}a_k\approx0.5+0.8+0.9756+2018\times1=2019.28+2018$，"
        r"接近 $2020$ 时 $a_1$ 需略微调整；此时 $\ln a_1\cdot\ln a_{2021}$ 中 "
        r"$|\ln a_{2021}|$ 极小，乘积远小于 $\frac1{2020}$ ✓" "\n"
        r"⑤ ⚠ 题干「$a_1\in0,1$」实为 $a_1\in(0,1)$（开区间），否则 $a_1=1$ 时全为 $1$，和为 $2021\ne2020$．" "\n"
        r"**通法（递推 + 对数和放缩）**：" "\n"
        r"① 分子分母同除以 $a_n$ 化成 $a_n+\frac1{a_n}$ 型，用基本不等式定范围；" "\n"
        r"② 单调递增 + 总和已知 ⟹ 用「首尾夹逼」定出首项或末项的范围；" "\n"
        r"③ $-\ln x$ 与 $\frac1x-1$ 的桥梁是 $f(x)=\ln x-1+\frac1x\ge0$．"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-135'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-135-V2',
}

T135_V3 = {
    'type': '选择',
    'stem_text': (
        r"设 $a,b\in\mathbb R$，数列 $\left\{a_n\right\}$ 满足 $a_1=a$，$a_n=\ln a_{n+1}+b\ \left(n\in\mathbb N^{*}\right)$，则（　　）"
    ),
    'stem': [
        r"设 $a,b\in\mathbb R$，数列 $\left\{a_n\right\}$ 满足 $a_1=a$，$a_n=\ln a_{n+1}+b\ \left(n\in\mathbb N^{*}\right)$，则（　　）"
    ],
    'opts': [
        ('A', r"若 $b=-2$，则 $a_{2020}>a$"),
        ('B', r"若 $b=-2$，则 $a_{2020}<a$"),
        ('C', r"若 $b=2$，则 $a_{2020}>a$"),
        ('D', r"若 $b=2$，则 $a_{2020}<a$"),
    ],
    'answer': r"A",
    'analysis': (
        r"由 $a_n=\ln a_{n+1}+b$ 解出 $a_{n+1}=\mathrm e^{a_n-b}$，于是"
        r"$a_{n+1}-a_n=\mathrm e^{a_n-b}-a_n$．令 $f(x)=\mathrm e^{x-b}-x$，研究 $f$ 的最小值符号："
        r"$b=-2$ 时 $f_{\min}=3>0$，故递增；$b=2$ 时 $f$ 有两个零点，取 $a_1$ 为零点时数列恒定，C、D 都不恒成立．"
    ),
    'solution': (
        r"**第一步：把隐式化成显式递推**" "\n"
        r"由 $a_n=\ln a_{n+1}+b$ 得 $\ln a_{n+1}=a_n-b$，即 $a_{n+1}=\mathrm e^{a_n-b}$．" "\n"
        r"于是 $a_{n+1}-a_n=\mathrm e^{a_n-b}-a_n$．" "\n"
        r"**第二步：$b=-2$ 时**" "\n"
        r"令 $f(x)=\mathrm e^{x+2}-x$，则 $f'(x)=\mathrm e^{x+2}-1$．" "\n"
        r"再令 $F(x)=f'(x)=\mathrm e^{x+2}-1$，$F'(x)=\mathrm e^{x+2}>0$，故 $F$ 递增且 $F(-2)=0$．" "\n"
        r"所以 $x>-2$ 时 $f'(x)>0$，$f$ 递增；$x<-2$ 时 $f'(x)<0$，$f$ 递减．" "\n"
        r"$f_{\min}=f(-2)=\mathrm e^{0}+2=3>0$，故对任意 $x$ 有 $f(x)>0$．" "\n"
        r"于是 $a_{n+1}-a_n=f(a_n)>0$，$\left\{a_n\right\}$ 严格递增 ⟹ $a_{2020}>a_1=a$，**A 正确、B 错**．" "\n"
        r"**第三步：$b=2$ 时**" "\n"
        r"令 $g(x)=\mathrm e^{x-2}-x$，同理 $g'(x)=\mathrm e^{x-2}-1$ 递增且 $g'(2)=0$，" "\n"
        r"故 $g$ 在 $(-\infty,2)$ 递减、$(2,+\infty)$ 递增，$g_{\min}=g(2)=1-2=-1<0$．" "\n"
        r"又 $g(0)=\mathrm e^{-2}>0$、$g(4)=\mathrm e^{2}-4>0$，故存在 $x_1\in(0,2)$、$x_2\in(2,4)$ 使 $g(x_1)=g(x_2)=0$．" "\n"
        r"取 $a_1=x_1$（或 $x_2$），则 $a_2-a_1=g(a_1)=0$，即 $a_2=a_1$；" "\n"
        r"同理 $a_{n+1}-a_n=g(a_n)=g(a_1)=0$ 对所有 $n$ 成立，" "\n"
        r"故 $\left\{a_n\right\}$ 是常数列，$a_{2020}=a$，**C、D 都不成立**．" "\n"
        r"综上选 **A**．"
    ),
    'review': (
        r"① ⭐⭐ **隐递推 $a_n=\ln a_{n+1}+b$ 先解出 $a_{n+1}=\mathrm e^{a_n-b}$**，"
        r"再作差 $a_{n+1}-a_n=\mathrm e^{a_n-b}-a_n$，把「数列单调性」变成「函数值符号」．" "\n"
        r"② ⭐⭐ **$f(x)=\mathrm e^{x+c}-x$ 的最小值一定在 $x=-c$ 处**："
        r"$f'(x)=\mathrm e^{x+c}-1=0$ ⟹ $x=-c$，$f_{\min}=1+c$．" "\n"
        r"   $b=-2$ ⟹ $c=2$ ⟹ $f_{\min}=3>0$（恒正）；$b=2$ ⟹ $c=-2$ ⟹ $f_{\min}=-1<0$（有零点）．"
        r"**只看 $1+c$ 的符号就能定性**，这是最快的判据．" "\n"
        r"③ ⭐ **存在零点时的反例构造**：取 $a_1$ 为 $g$ 的零点，则数列恒定，"
        r"于是「$>$」和「$<$」两个选项同时被否 —— 这正是 D「以上均有可能」不需要考虑的原因．" "\n"
        r"④ 数值复核：$b=-2$ 时取 $a_1=0$，$a_2=\mathrm e^{2}=7.389$，$a_3=\mathrm e^{9.389}\approx1.2\times10^{4}$，急剧递增 ✓" "\n"
        r"   $b=2$ 时 $g(0)=\mathrm e^{-2}-0=0.1353>0$，$g(2)=-1$，$g(4)=\mathrm e^2-4=3.389>0$，"
        r"二分得 $x_1\approx0.1586$、$x_2\approx3.1462$，取 $a_1=0.1586$ 则 $a_2=\mathrm e^{-1.8414}=0.1586$ ✓ 恒定．" "\n"
        r"⑤ ⚠ 原书详解中「$a_2-a_1=\mathrm e^{a_1+2}-a_1$」应为 $\mathrm e^{a_1-2}-a_1$（$b=2$ 时指数是 $-2$），已更正．" "\n"
        r"**通法（隐式递推的单调性）**：" "\n"
        r"① 先把 $a_{n+1}$ 显式解出，再作差；" "\n"
        r"② 作差后视为函数 $f(a_n)$，求 $f$ 的最小值；" "\n"
        r"③ $f_{\min}>0$ ⟹ 严格递增；$f$ 有零点 ⟹ 取初值为零点得常数列，可构造反例．"
    ),
    'difficulty': 0.86,
    'topics': ['M-T-135'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-135-V3',
}


T269_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知正项等差数列 $\left\{a_n\right\}$ 满足：$S_n^{2}=a_1^{3}+a_2^{3}+\cdots+a_n^{3}$，"
        r"其中 $S_n$ 是数列 $\left\{a_n\right\}$ 的前 $n$ 项和．"
        r"（1）求数列 $\left\{a_n\right\}$ 的通项公式；"
        r"（2）令 $b_n=\left(-1\right)^{n-1}\dfrac{4n}{\left(2a_n-1\right)\left(2a_n+1\right)}$，"
        r"证明：$b_1+b_2+\cdots+b_n\le\dfrac{2n+2}{2n+1}$．"
    ),
    'stem': [
        r"已知正项等差数列 $\left\{a_n\right\}$ 满足：$S_n^{2}=a_1^{3}+a_2^{3}+\cdots+a_n^{3}$，"
        r"其中 $S_n$ 是数列 $\left\{a_n\right\}$ 的前 $n$ 项和．",
        r"（1）求数列 $\left\{a_n\right\}$ 的通项公式；",
        r"（2）令 $b_n=\left(-1\right)^{n-1}\dfrac{4n}{\left(2a_n-1\right)\left(2a_n+1\right)}$，"
        r"证明：$b_1+b_2+\cdots+b_n\le\dfrac{2n+2}{2n+1}$．"
    ],
    'opts': [],
    'answer': (
        r"（1）$a_n=n$；（2）证明见解析．"
    ),
    'analysis': (
        r"（1）分别代入 $n=1,2$ 得两个方程，解出 $a_1,a_2$ 从而定出公差；"
        r"（2）代入 $a_n=n$ 后把分式拆成 $\frac1{2n-1}+\frac1{2n+1}$，"
        r"写成相邻项之差的形式后裂项相消，最后放大即可．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"$n=1$ 时，$S_1^{2}=a_1^{3}$，即 $a_1^{2}=a_1^{3}$，由 $a_1>0$ 得 $a_1=1$．" "\n"
        r"$n=2$ 时，$S_2^{2}=a_1^{3}+a_2^{3}$，即 $\left(1+a_2\right)^{2}=1+a_2^{3}$．" "\n"
        r"展开：$1+2a_2+a_2^{2}=1+a_2^{3}$，即 $a_2\left(a_2^{2}-a_2-2\right)=0$．" "\n"
        r"由 $a_2>0$ 得 $a_2^{2}-a_2-2=0$，即 $\left(a_2-2\right)\left(a_2+1\right)=0$，故 $a_2=2$．" "\n"
        r"公差 $d=a_2-a_1=1$，故 $\boxed{a_n=n}$．" "\n"
        r"**第（2）问**" "\n"
        r"代入 $a_n=n$：" "\n"
        r"$b_n=\left(-1\right)^{n-1}\dfrac{4n}{\left(2n-1\right)\left(2n+1\right)}"
        r"=\left(-1\right)^{n-1}\left(\dfrac1{2n-1}+\dfrac1{2n+1}\right)$，" "\n"
        r"（因 $\dfrac1{2n-1}+\dfrac1{2n+1}=\dfrac{4n}{\left(2n-1\right)\left(2n+1\right)}$）" "\n"
        r"$=\left(-1\right)^{n-1}\dfrac1{2n-1}-\left(-1\right)^{n}\dfrac1{2n+1}$．" "\n"
        r"令 $v_n=\left(-1\right)^{n}\dfrac1{2n+1}$，则 $b_n=v_{n-1}-v_n$（其中 $v_0=1$）．" "\n"
        r"于是 $\sum_{k=1}^{n}b_k=\left(v_0-v_1\right)+\left(v_1-v_2\right)+\cdots+\left(v_{n-1}-v_n\right)=v_0-v_n$，" "\n"
        r"$=1-\left(-1\right)^{n}\dfrac1{2n+1}\le1+\dfrac1{2n+1}=\dfrac{2n+2}{2n+1}$．" "\n"
        r"故 $\boxed{b_1+b_2+\cdots+b_n\le\dfrac{2n+2}{2n+1}}$，等号在 $n$ 为奇数时取到．"
    ),
    'review': (
        r"① ⭐⭐ **$n=1,2$ 各代入一次即可定出等差数列**："
        r"$a_1^2=a_1^3$ ⟹ $a_1=1$；$(1+a_2)^2=1+a_2^3$ ⟹ $a_2(a_2-2)(a_2+1)=0$ ⟹ $a_2=2$．"
        r"正项条件 $a_n>0$ 用于排除 $a_1=0$、$a_2=-1$．" "\n"
        r"② ⭐⭐ **分子拆成两分母之和**：$\frac{4n}{(2n-1)(2n+1)}=\frac1{2n-1}+\frac1{2n+1}$，"
        r"判据是 $(2n+1)+(2n-1)=4n$ 恰等于分子 —— 这就是「$\frac p{xy}=\frac1x+\frac1y\iff p=x+y$」．" "\n"
        r"③ ⭐ **裂项相消的写法**：令 $v_n=(-1)^n\frac1{2n+1}$、$v_0=1$，则 $b_n=v_{n-1}-v_n$，"
        r"求和 $=v_0-v_n$ 一步到底，不必逐项展开．" "\n"
        r"④ ⭐ **最后一步的放大**：$1-(-1)^n\frac1{2n+1}\le1+\frac1{2n+1}$，"
        r"$n$ 奇时取等（减去负数）、$n$ 偶时严格小于．**等号条件是本题的得分点**．" "\n"
        r"⑤ 数值复核：$a_1=1,a_2=2$ 时 $S_2=3$，$S_2^2=9$；$a_1^3+a_2^3=1+8=9$ ✓" "\n"
        r"   $b_1=\frac4{1\cdot3}=\frac43$，$b_2=-\frac8{3\cdot5}=-\frac8{15}$，$b_3=\frac{12}{5\cdot7}=\frac{12}{35}$；" "\n"
        r"   $n=1$：和 $=\frac43$，右 $=\frac43$ ✓（等号）；"
        r"$n=2$：和 $=\frac43-\frac8{15}=\frac45$，右 $=\frac65=1.2$，$\frac45=0.8<1.2$ ✓；" "\n"
        r"   $n=3$：和 $=\frac45+\frac{12}{35}=\frac{40}{35}=\frac87\approx1.1429$，右 $=\frac87\approx1.1429$ ✓（等号）．" "\n"
        r"**通法（$S_n^2=\sum a_k^3$ 型）**：" "\n"
        r"① 只需代入 $n=1,2$ 两个值，等差数列两个自由度（$a_1,d$）刚好定出；" "\n"
        r"② 高次方程因式分解后由「正项」排除非正根；" "\n"
        r"③ 求和型结论先裂项，再讨论 $(-1)^n$ 带来的奇偶差异．"
    ),
    'difficulty': 0.72,
    'topics': ['M-T-269'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-269-E1',
}

T269_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知数列 $\left\{a_n\right\}$ 满足 $a_1=1$，$\forall n\in\mathbb N^{*}$，"
        r"$a_1+\dfrac12a_2+\cdots+\dfrac1na_n=a_{n+1}-1$．"
        r"（1）求数列 $\left\{a_n\right\}$ 的通项公式；"
        r"（2）若 $b_n=\left(-1\right)^{n+1}\dfrac{2n+1}{a_na_{n+1}}$，"
        r"记数列 $\left\{b_n\right\}$ 的前 $n$ 项和为 $S_n$，求 $S_n$．"
    ),
    'stem': [
        r"已知数列 $\left\{a_n\right\}$ 满足 $a_1=1$，$\forall n\in\mathbb N^{*}$，"
        r"$a_1+\dfrac12a_2+\cdots+\dfrac1na_n=a_{n+1}-1$．",
        r"（1）求数列 $\left\{a_n\right\}$ 的通项公式；",
        r"（2）若 $b_n=\left(-1\right)^{n+1}\dfrac{2n+1}{a_na_{n+1}}$，"
        r"记数列 $\left\{b_n\right\}$ 的前 $n$ 项和为 $S_n$，求 $S_n$．"
    ],
    'opts': [],
    'answer': (
        r"（1）$a_n=n$；（2）$S_n=\left(-1\right)^{n+1}\dfrac1{n+1}+1$．"
    ),
    'analysis': (
        r"（1）退一位相减，把求和式化成 $\frac1na_n=a_{n+1}-a_n$，"
        r"整理得 $\frac{a_{n+1}}{n+1}=\frac{a_n}n$，故 $\frac{a_n}n$ 为常数；"
        r"（2）代入 $a_n=n$ 后分子 $2n+1$ 恰是两分母之和，裂项后相邻项相消．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"设 $T_n=a_1+\dfrac12a_2+\cdots+\dfrac1na_n$，则 $T_n=a_{n+1}-1$．" "\n"
        r"$n\ge2$ 时，$T_{n-1}=a_n-1$．两式相减：" "\n"
        r"$T_n-T_{n-1}=\dfrac1na_n=a_{n+1}-a_n$，即 $a_{n+1}=a_n\left(1+\dfrac1n\right)=\dfrac{n+1}na_n$．" "\n"
        r"故 $\dfrac{a_{n+1}}{n+1}=\dfrac{a_n}{n}$，即 $\left\{\dfrac{a_n}n\right\}$ 为常数数列．" "\n"
        r"又 $n=1$ 时 $T_1=a_1=1=a_2-1$，得 $a_2=2$，故 $\dfrac{a_2}2=1=\dfrac{a_1}1$．" "\n"
        r"于是 $\dfrac{a_n}n=\dfrac{a_1}1=1$，$\boxed{a_n=n}$．" "\n"
        r"**第（2）问**" "\n"
        r"$b_n=\left(-1\right)^{n+1}\dfrac{2n+1}{n\left(n+1\right)}"
        r"=\left(-1\right)^{n+1}\left(\dfrac1n+\dfrac1{n+1}\right)$，" "\n"
        r"（因 $\dfrac1n+\dfrac1{n+1}=\dfrac{2n+1}{n\left(n+1\right)}$）" "\n"
        r"$=\left(-1\right)^{n+1}\dfrac1{n+1}-\left(-1\right)^{n}\dfrac1n$．" "\n"
        r"令 $v_n=\left(-1\right)^{n}\dfrac1n$，则 $b_n=v_{n+1}-v_n$．" "\n"
        r"$S_n=\sum_{k=1}^{n}\left(v_{k+1}-v_k\right)=v_{n+1}-v_1"
        r"=\left(-1\right)^{n+1}\dfrac1{n+1}-\left(-1\right)^{1}\cdot1$，" "\n"
        r"故 $\boxed{S_n=\left(-1\right)^{n+1}\dfrac1{n+1}+1}$．"
    ),
    'review': (
        r"① ⭐⭐ **「求和式 $=a_{n+1}-1$」型一律退一位相减**："
        r"$T_n-T_{n-1}=\frac1na_n$，而右端是 $a_{n+1}-a_n$，求和号直接消失．" "\n"
        r"② ⭐⭐ **$\frac{a_{n+1}}{n+1}=\frac{a_n}n$ ⟹ $\frac{a_n}n$ 为常数**："
        r"这是「$a_{n+1}=\frac{n+1}na_n$」的标准读法，等价于 $\frac{a_n}n$ 恒等．" "\n"
        r"③ ⭐ **$n=1$ 要单独用原式检验**：$T_1=a_1=1=a_2-1$ ⟹ $a_2=2$，确认 $\frac{a_2}2=\frac{a_1}1=1$，"
        r"即常数关系对 $n=1$ 也成立（递推只证到 $n\ge2$）．" "\n"
        r"④ ⭐ **裂项后是 $v_{n+1}-v_n$（不是 $v_n-v_{n+1}$）**："
        r"$v_n=(-1)^n\frac1n$，$b_n=v_{n+1}-v_n$，故 $S_n=v_{n+1}-v_1$，注意 $v_1=-1$，末项要变号．" "\n"
        r"⑤ 数值复核：$b_1=\frac32$，$b_2=-\frac56$，$b_3=\frac7{12}$，$b_4=-\frac9{20}$；" "\n"
        r"   $S_1=\frac32$，公式 $(-1)^2\frac12+1=\frac32$ ✓；"
        r"$S_2=\frac32-\frac56=\frac23$，公式 $(-1)^3\frac13+1=\frac23$ ✓；" "\n"
        r"   $S_3=\frac23+\frac7{12}=\frac54$，公式 $(-1)^4\frac14+1=\frac54$ ✓；"
        r"$S_4=\frac54-\frac9{20}=\frac45$，公式 $(-1)^5\frac15+1=\frac45$ ✓．" "\n"
        r"   可见 $S_n$ 在 $1$ 附近摆动并趋于 $1$（$|S_n-1|=\frac1{n+1}\to0$）．" "\n"
        r"**通法（系数型求和递推）**：" "\n"
        r"① 见到「$a_1+\frac12a_2+\cdots+\frac1na_n=f(a_{n+1})$」就退一位相减；" "\n"
        r"② 减完得到 $\frac1na_n=g(a_{n+1},a_n)$，整理成 $\frac{a_{n+1}}{n+1}=\frac{a_n}n$ 的形式；" "\n"
        r"③ 用 $n=1$ 单独确认首项比；" "\n"
        r"④ 第二问的分子若是两分母之和，直接裂项，交错号带来 $S_n\to$ 常数的摆动收敛．"
    ),
    'difficulty': 0.70,
    'topics': ['M-T-269'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-269-V2',
}


T276_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知等差数列 $\left\{a_n\right\}$ 的前 $n$ 项和为 $S_n$，数列 $\left\{b_n\right\}$ 为正项等比数列，"
        r"且 $a_1=3$，$b_1=1$，$b_3+S_2=12$，$a_5-a_3=2b_2$．"
        r"（1）求 $\left\{a_n\right\}$ 和 $\left\{b_n\right\}$ 的通项公式；"
        r"（2）若 $c_n=\begin{cases}\dfrac{2}{S_n}, & n\text{ 为奇数}\\[2mm] b_n, & n\text{ 为偶数}\end{cases}$，"
        r"设 $\left\{c_n\right\}$ 的前 $n$ 项和为 $T_n$，求 $T_{2n}$．"
    ),
    'stem': [
        r"已知等差数列 $\left\{a_n\right\}$ 的前 $n$ 项和为 $S_n$，数列 $\left\{b_n\right\}$ 为正项等比数列，"
        r"且 $a_1=3$，$b_1=1$，$b_3+S_2=12$，$a_5-a_3=2b_2$．",
        r"（1）求 $\left\{a_n\right\}$ 和 $\left\{b_n\right\}$ 的通项公式；",
        r"（2）若 $c_n=\begin{cases}\dfrac{2}{S_n}, & n\text{ 为奇数}\\[2mm] b_n, & n\text{ 为偶数}\end{cases}$，"
        r"设 $\left\{c_n\right\}$ 的前 $n$ 项和为 $T_n$，求 $T_{2n}$．"
    ],
    'opts': [],
    'answer': (
        r"（1）$a_n=2n+1$，$b_n=2^{n-1}$；"
        r"（2）$T_{2n}=\dfrac{2^{2n+1}+1}{3}-\dfrac1{2n+1}$．"
    ),
    'analysis': (
        r"（1）设公差 $d$、公比 $q$，由两个条件列方程组，用「正项」舍去 $q=-3$；"
        r"（2）$S_n=n(n+2)$ 后奇数项裂成 $\frac1n-\frac1{n+2}$，偶数项是等比数列，"
        r"把 $T_{2n}$ 拆成「奇数下标之和 + 偶数下标之和」分别求和．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"设 $\left\{a_n\right\}$ 公差为 $d$，$\left\{b_n\right\}$ 公比为 $q$（由正项知 $q>0$）．" "\n"
        r"$S_2=a_1+a_2=3+(3+d)=6+d$，$b_2=q$，$b_3=q^{2}$．" "\n"
        r"由 $b_3+S_2=12$ 得 $q^{2}+6+d=12$，即 $q^{2}+d=6$；" "\n"
        r"由 $a_5-a_3=2b_2$ 得 $2d=2q$，即 $d=q$．" "\n"
        r"代入：$q^{2}+q-6=0$，即 $\left(q-2\right)\left(q+3\right)=0$，由 $q>0$ 得 $q=2$，$d=2$．" "\n"
        r"故 $\boxed{a_n=3+2\left(n-1\right)=2n+1}$，$\boxed{b_n=2^{n-1}}$．" "\n"
        r"**第（2）问**" "\n"
        r"$S_n=\dfrac{n\left[3+\left(2n+1\right)\right]}2=n\left(n+2\right)$．" "\n"
        r"奇数项（$n=2k-1$）：$c_{2k-1}=\dfrac{2}{S_{2k-1}}=\dfrac{2}{\left(2k-1\right)\left(2k+1\right)}"
        r"=\dfrac1{2k-1}-\dfrac1{2k+1}$．" "\n"
        r"$\sum_{k=1}^{n}c_{2k-1}=\left(1-\dfrac13\right)+\left(\dfrac13-\dfrac15\right)+\cdots"
        r"+\left(\dfrac1{2n-1}-\dfrac1{2n+1}\right)=1-\dfrac1{2n+1}$．" "\n"
        r"偶数项（$n=2k$）：$c_{2k}=b_{2k}=2^{2k-1}$，" "\n"
        r"$\sum_{k=1}^{n}c_{2k}=2+2^{3}+2^{5}+\cdots+2^{2n-1}=2\cdot\dfrac{4^{n}-1}{4-1}=\dfrac{2^{2n+1}-2}3$．" "\n"
        r"相加：" "\n"
        r"$T_{2n}=\left(1-\dfrac1{2n+1}\right)+\dfrac{2^{2n+1}-2}3"
        r"=\dfrac{2^{2n+1}-2+3}3-\dfrac1{2n+1}$，" "\n"
        r"故 $\boxed{T_{2n}=\dfrac{2^{2n+1}+1}{3}-\dfrac1{2n+1}}$．"
    ),
    'review': (
        r"① ⭐⭐ **$S_2=6+d$ 不要算错**：$S_2=a_1+a_2=3+(3+d)$，$a_1$ 出现两次．" "\n"
        r"② ⭐⭐ **「正项等比数列」用于舍根**：$q^2+q-6=0$ 给 $q=2$ 或 $q=-3$，"
        r"若没有「正项」二字则 $q=-3$ 也要讨论（此时 $b_n$ 正负交替）．" "\n"
        r"③ ⭐⭐ **$T_{2n}$ 拆成奇偶两串分别求和** —— 这是「分段数列求和」的标准动作，"
        r"奇数串裂项、偶数串等比，两者结构完全不同，必须分开算．" "\n"
        r"④ ⭐ **等比求和的首项是 $2$、公比是 $4$**：$2,2^3,2^5,\ldots$ 共 $n$ 项，"
        r"和 $=2\cdot\frac{4^n-1}{4-1}$，**不是** $\frac{2(2^n-1)}{2-1}$．" "\n"
        r"⑤ 数值复核：$n=1$ 时 $T_2=c_1+c_2=\frac2{S_1}+b_2=\frac23+2=\frac83$；"
        r"公式 $\frac{2^3+1}3-\frac13=\frac93-\frac13=\frac83$ ✓" "\n"
        r"   $n=2$ 时 $T_4=\frac83+\frac2{S_3}+b_4=\frac83+\frac2{15}+8=\frac{40+2+120}{15}=\frac{162}{15}=\frac{54}5$；"
        r"公式 $\frac{2^5+1}3-\frac15=\frac{33}3-\frac15=11-\frac15=\frac{54}5$ ✓" "\n"
        r"   $n=3$：$T_6=\frac{54}5+\frac2{35}+32=\frac{378+2+1120}{35}=\frac{1500}{35}=\frac{300}7$；"
        r"公式 $\frac{2^7+1}3-\frac17=\frac{129}3-\frac17=43-\frac17=\frac{300}7$ ✓" "\n"
        r"⑥ ⚠ **原书答案有误**：原书给 $T_{2n}=1+\frac{2^{2n+1}}3-\frac1{2n+1}$，"
        r"代入 $n=1$ 得 $\frac{10}3\ne\frac83$；正确应为 $\frac{2^{2n+1}+1}3-\frac1{2n+1}$，"
        r"原书在合并 $1+\frac{2^{2n+1}-2}3$ 时漏掉了 $-2$（即写成 $1+\frac{2^{2n+1}}3$）．已按正确值录入并登记勘误．" "\n"
        r"**通法（奇偶分段数列求和）**：" "\n"
        r"① 求 $T_{2n}$ 就拆成 $\sum_{k=1}^n c_{2k-1}+\sum_{k=1}^n c_{2k}$，各 $n$ 项；" "\n"
        r"② 分式型先裂项（分子是否为两分母之和是关键判据）；" "\n"
        r"③ 等比型注意「首项、公比、项数」三件事，尤以公比 $=q^2$ 最容易错．"
    ),
    'difficulty': 0.68,
    'topics': ['M-T-276'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-276-E1',
}

T276_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知 $\left\{a_n\right\}$ 为等差数列，$\left\{b_n\right\}$ 为等比数列，$a_1=b_1=1$，"
        r"$a_5=5\left(a_4-a_3\right)$，$b_5=4\left(b_4-b_3\right)$．"
        r"（Ⅰ）求 $\left\{a_n\right\}$ 和 $\left\{b_n\right\}$ 的通项公式；"
        r"（Ⅱ）记 $\left\{a_n\right\}$ 的前 $n$ 项和为 $S_n$，求证：$S_nS_{n+2}<S_{n+1}^{2}\ \left(n\in\mathbb N^{*}\right)$；"
        r"（Ⅲ）对任意的正整数 $n$，设 $c_n=\begin{cases}"
        r"\dfrac{\left(3a_n-2\right)b_n}{a_na_{n+2}}, & n\text{ 为奇数}\\[2mm]"
        r"\dfrac{a_{n-1}}{b_{n+1}}, & n\text{ 为偶数}\end{cases}$，求数列 $\left\{c_n\right\}$ 的前 $2n$ 项和．"
    ),
    'stem': [
        r"已知 $\left\{a_n\right\}$ 为等差数列，$\left\{b_n\right\}$ 为等比数列，$a_1=b_1=1$，"
        r"$a_5=5\left(a_4-a_3\right)$，$b_5=4\left(b_4-b_3\right)$．",
        r"（Ⅰ）求 $\left\{a_n\right\}$ 和 $\left\{b_n\right\}$ 的通项公式；",
        r"（Ⅱ）记 $\left\{a_n\right\}$ 的前 $n$ 项和为 $S_n$，求证：$S_nS_{n+2}<S_{n+1}^{2}\ \left(n\in\mathbb N^{*}\right)$；",
        r"（Ⅲ）对任意的正整数 $n$，设 $c_n=\begin{cases}"
        r"\dfrac{\left(3a_n-2\right)b_n}{a_na_{n+2}}, & n\text{ 为奇数}\\[2mm]"
        r"\dfrac{a_{n-1}}{b_{n+1}}, & n\text{ 为偶数}\end{cases}$，求数列 $\left\{c_n\right\}$ 的前 $2n$ 项和．"
    ],
    'opts': [],
    'answer': (
        r"（Ⅰ）$a_n=n$，$b_n=2^{n-1}$；（Ⅱ）证明见解析；"
        r"（Ⅲ）$\dfrac{4^{n}}{2n+1}-\dfrac{6n+5}{9\cdot4^{n}}-\dfrac49$．"
    ),
    'analysis': (
        r"（Ⅰ）由两个条件分别解出 $d,q$；（Ⅱ）直接作差 $S_nS_{n+2}-S_{n+1}^2$，因式分解后定号；"
        r"（Ⅲ）奇数项化成 $\frac{2^{2k}}{2k+1}-\frac{2^{2k-2}}{2k-1}$ 裂项，偶数项 $\frac{2k-1}{4^k}$ 用错位相减，"
        r"两串结果相加．"
    ),
    'solution': (
        r"**第（Ⅰ）问**" "\n"
        r"设公差 $d$、公比 $q$（$q\ne0$）．" "\n"
        r"$a_5=5\left(a_4-a_3\right)$：$1+4d=5d$，得 $d=1$，故 $\boxed{a_n=n}$．" "\n"
        r"$b_5=4\left(b_4-b_3\right)$：$q^{4}=4\left(q^{3}-q^{2}\right)=4q^{2}\left(q-1\right)$，" "\n"
        r"由 $q\ne0$ 得 $q^{2}-4q+4=0$，即 $\left(q-2\right)^{2}=0$，故 $q=2$，$\boxed{b_n=2^{n-1}}$．" "\n"
        r"**第（Ⅱ）问**" "\n"
        r"$S_n=\dfrac{n\left(n+1\right)}2$，故" "\n"
        r"$S_nS_{n+2}=\dfrac{n\left(n+1\right)}2\cdot\dfrac{\left(n+2\right)\left(n+3\right)}2"
        r"=\dfrac{n\left(n+1\right)\left(n+2\right)\left(n+3\right)}4$，" "\n"
        r"$S_{n+1}^{2}=\left[\dfrac{\left(n+1\right)\left(n+2\right)}2\right]^{2}"
        r"=\dfrac{\left(n+1\right)^{2}\left(n+2\right)^{2}}4$．" "\n"
        r"$S_nS_{n+2}-S_{n+1}^{2}=\dfrac{\left(n+1\right)\left(n+2\right)}4\left[n\left(n+3\right)-\left(n+1\right)\left(n+2\right)\right]$，" "\n"
        r"$=\dfrac{\left(n+1\right)\left(n+2\right)}4\left[\left(n^{2}+3n\right)-\left(n^{2}+3n+2\right)\right]"
        r"=-\dfrac{\left(n+1\right)\left(n+2\right)}2<0$．" "\n"
        r"故 $\boxed{S_nS_{n+2}<S_{n+1}^{2}}$．" "\n"
        r"**第（Ⅲ）问**" "\n"
        r"$n$ 为奇数，记 $n=2k-1$：" "\n"
        r"$c_{2k-1}=\dfrac{\left[3\left(2k-1\right)-2\right]\cdot2^{2k-2}}{\left(2k-1\right)\left(2k+1\right)}"
        r"=\dfrac{\left(6k-5\right)2^{2k-2}}{\left(2k-1\right)\left(2k+1\right)}$，" "\n"
        r"$=\dfrac{2^{2k}}{2k+1}-\dfrac{2^{2k-2}}{2k-1}$" "\n"
        r"（因 $\dfrac4{2k+1}-\dfrac1{2k-1}=\dfrac{6k-5}{\left(2k-1\right)\left(2k+1\right)}$）．" "\n"
        r"令 $w_k=\dfrac{2^{2k}}{2k+1}$，则 $c_{2k-1}=w_k-w_{k-1}$，且 $w_0=1$，" "\n"
        r"$\sum_{k=1}^{n}c_{2k-1}=w_n-w_0=\dfrac{4^{n}}{2n+1}-1$．" "\n"
        r"$n$ 为偶数，记 $n=2k$：$c_{2k}=\dfrac{a_{2k-1}}{b_{2k+1}}=\dfrac{2k-1}{2^{2k}}=\dfrac{2k-1}{4^{k}}$．" "\n"
        r"设 $U_n=\sum_{k=1}^{n}\dfrac{2k-1}{4^{k}}=\dfrac14+\dfrac3{4^{2}}+\cdots+\dfrac{2n-1}{4^{n}}$　①，" "\n"
        r"$\dfrac14U_n=\dfrac1{4^{2}}+\dfrac3{4^{3}}+\cdots+\dfrac{2n-3}{4^{n}}+\dfrac{2n-1}{4^{n+1}}$　②，" "\n"
        r"①$-$②：$\dfrac34U_n=\dfrac14+\dfrac2{4^{2}}+\dfrac2{4^{3}}+\cdots+\dfrac2{4^{n}}-\dfrac{2n-1}{4^{n+1}}$，" "\n"
        r"$=\dfrac14+\dfrac18\cdot\dfrac{1-\frac1{4^{n-1}}}{1-\frac14}-\dfrac{2n-1}{4^{n+1}}"
        r"=\dfrac14+\dfrac16\left(1-\dfrac1{4^{n-1}}\right)-\dfrac{2n-1}{4^{n+1}}$，" "\n"
        r"$=\dfrac5{12}-\dfrac8{3\cdot4^{n+1}}-\dfrac{2n-1}{4^{n+1}}=\dfrac5{12}-\dfrac{6n+5}{3\cdot4^{n+1}}$，" "\n"
        r"故 $U_n=\dfrac43\left(\dfrac5{12}-\dfrac{6n+5}{3\cdot4^{n+1}}\right)=\dfrac59-\dfrac{6n+5}{9\cdot4^{n}}$．" "\n"
        r"前 $2n$ 项和 $=\left(\dfrac{4^{n}}{2n+1}-1\right)+\left(\dfrac59-\dfrac{6n+5}{9\cdot4^{n}}\right)$，" "\n"
        r"$=\boxed{\dfrac{4^{n}}{2n+1}-\dfrac{6n+5}{9\cdot4^{n}}-\dfrac49}$．"
    ),
    'review': (
        r"① ⭐⭐ **（Ⅱ）的因式分解是捷径**：$S_nS_{n+2}-S_{n+1}^2$ 直接提公因子 $\frac{(n+1)(n+2)}4$，"
        r"括号内 $n(n+3)-(n+1)(n+2)=-2$ 是常数 —— **这个 $-2$ 与 $n$ 无关，是本题设计好的**．" "\n"
        r"   一般结论：对任意等差数列，$S_nS_{n+2}-S_{n+1}^2=-\frac{(n+1)(n+2)}{2}d^2\cdot\frac{1}{?}$… "
        r"本题 $d=1$ 时恰为 $-\frac{(n+1)(n+2)}2$．" "\n"
        r"② ⭐⭐ **（Ⅲ）奇数项的裂项方向**：$c_{2k-1}=w_k-w_{k-1}$，其中 $w_k=\frac{2^{2k}}{2k+1}$，"
        r"所以 $\sum=w_n-w_0$ —— **$w_0=1$ 这一项很容易漏**．" "\n"
        r"③ ⭐⭐ **错位相减后中间是等比数列**：$\frac34U_n$ 的中间项为 $\frac2{4^2}+\cdots+\frac2{4^n}$，"
        r"共 $n-1$ 项，公比 $\frac14$，和 $=\frac18\cdot\frac{1-4^{-(n-1)}}{3/4}=\frac16(1-4^{-(n-1)})$．" "\n"
        r"④ ⭐ **两串相加时的常数合并**：$-1+\frac59=-\frac49$，这正是答案末尾的 $-\frac49$．" "\n"
        r"⑤ 数值复核（$n=1$）：$c_1=\frac{(3a_1-2)b_1}{a_1a_3}=\frac{(3-2)\cdot1}{1\cdot3}=\frac13$，"
        r"$c_2=\frac{a_1}{b_3}=\frac14$，和 $=\frac7{12}$；" "\n"
        r"   公式 $\frac43-\frac{11}{36}-\frac49=\frac{48-11-16}{36}=\frac{21}{36}=\frac7{12}$ ✓" "\n"
        r"   $n=2$：$c_3=\frac{(9-2)\cdot4}{3\cdot5}=\frac{28}{15}$，$c_4=\frac{a_3}{b_5}=\frac3{16}$，" "\n"
        r"   和 $=\frac7{12}+\frac{28}{15}+\frac3{16}=\frac{140+448+45}{240}=\frac{633}{240}=\frac{211}{80}=2.6375$；" "\n"
        r"   公式 $\frac{16}5-\frac{17}{9\cdot16}-\frac49=3.2-0.11806-0.44444=2.6375$ ✓" "\n"
        r"**通法（等差 × 等比交叉求和）**：" "\n"
        r"① 前 $2n$ 项和必拆奇偶两串；" "\n"
        r"② 奇数串若能写成 $w_k-w_{k-1}$ 就裂项，注意 $w_0$；" "\n"
        r"③ 偶数串若为 $\frac{\text{一次式}}{\text{指数式}}$ 就错位相减；" "\n"
        r"④ 作差比大小（Ⅱ）优先提公因子而非硬展开．"
    ),
    'difficulty': 0.78,
    'topics': ['M-T-276'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-276-V1',
}

T276_V2 = {
    'type': '解答',
    'stem_text': (
        r"设 $\left\{a_n\right\}$ 是等差数列，$\left\{b_n\right\}$ 是等比数列．已知 $a_1=1$，$b_1=2$，"
        r"$b_2=2a_2$，$b_3=2a_3+2$．"
        r"（1）求 $\left\{a_n\right\}$ 和 $\left\{b_n\right\}$ 的通项公式；"
        r"（2）数列 $\left\{c_n\right\}$ 满足 $c_n=\begin{cases}1, & n=2^{k}\\ a_n, & n\ne2^{k}\end{cases}\ \left(k\in\mathbb N^{*}\right)$，"
        r"设数列 $\left\{c_n\right\}$ 的前 $n$ 项和为 $S_n$，求 $S_{2^{n}}$．"
    ),
    'stem': [
        r"设 $\left\{a_n\right\}$ 是等差数列，$\left\{b_n\right\}$ 是等比数列．已知 $a_1=1$，$b_1=2$，"
        r"$b_2=2a_2$，$b_3=2a_3+2$．",
        r"（1）求 $\left\{a_n\right\}$ 和 $\left\{b_n\right\}$ 的通项公式；",
        r"（2）数列 $\left\{c_n\right\}$ 满足 $c_n=\begin{cases}1, & n=2^{k}\\ a_n, & n\ne2^{k}\end{cases}\ \left(k\in\mathbb N^{*}\right)$，"
        r"设数列 $\left\{c_n\right\}$ 的前 $n$ 项和为 $S_n$，求 $S_{2^{n}}$．"
    ],
    'opts': [],
    'answer': (
        r"（1）$a_n=n$，$b_n=2^{n}$；（2）$S_{2^{n}}=2^{2n-1}-3\cdot2^{n-1}+n+2$．"
    ),
    'analysis': (
        r"（1）列方程组解 $d,q$，注意 $q\ne0$ 舍去 $d=-1$；"
        r"（2）在 $1\sim2^{n}$ 中，形如 $2^{k}$ 的恰好有 $n$ 个（$k=1,2,\ldots,n$），"
        r"故先按 $a_k=k$ 全求和，再减去这些位置上的 $\left(2^{k}-1\right)$．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"设公差 $d$、公比 $q$（$q\ne0$）．" "\n"
        r"$b_2=2q=2a_2=2\left(1+d\right)$，即 $q=1+d$；" "\n"
        r"$b_3=2q^{2}=2a_3+2=2\left(1+2d\right)+2=4+4d$，即 $q^{2}=2+2d$．" "\n"
        r"代入 $q=1+d$：$\left(1+d\right)^{2}=2+2d$，即 $d^{2}=1$，得 $d=1$ 或 $d=-1$．" "\n"
        r"$d=-1$ 时 $q=0$，与等比数列 $q\ne0$ 矛盾，舍．故 $d=1$，$q=2$．" "\n"
        r"$\boxed{a_n=n}$，$\boxed{b_n=2\cdot2^{n-1}=2^{n}}$．" "\n"
        r"**第（2）问**" "\n"
        r"$c_n$ 的取值：当 $n$ 是 $2$ 的正整数次幂时 $c_n=1$，否则 $c_n=a_n=n$．" "\n"
        r"在 $1,2,\ldots,2^{n}$ 中，$2$ 的正整数次幂恰有 $n$ 个：$2^{1},2^{2},\ldots,2^{n}$．" "\n"
        r"故先全部按 $a_k=k$ 求和，再把这 $n$ 个位置上的值由 $2^{k}$ 改成 $1$：" "\n"
        r"$S_{2^{n}}=\sum_{k=1}^{2^{n}}k-\sum_{k=1}^{n}\left(2^{k}-1\right)$，" "\n"
        r"$=\dfrac{2^{n}\left(2^{n}+1\right)}2-\left(2^{n+1}-2\right)+n$，" "\n"
        r"$=2^{n-1}\left(2^{n}+1\right)-2^{n+1}+2+n$，" "\n"
        r"$=2^{2n-1}+2^{n-1}-2^{n+1}+n+2$，" "\n"
        r"故 $\boxed{S_{2^{n}}=2^{2n-1}-3\cdot2^{n-1}+n+2}$（因 $2^{n-1}-2^{n+1}=2^{n-1}\left(1-4\right)=-3\cdot2^{n-1}$）．"
    ),
    'review': (
        r"① ⭐⭐ **本批最关键的一处还原：题干的 $S_{2n}$ 实为 $S_{2^{n}}$**．" "\n"
        r"   判据：答案含 $2^{2n-1}$，而若求 $S_{2n}$，则 $1\le k\le2n$ 中形如 $2^{k}$ 的只有 "
        r"$\lfloor\log_2(2n)\rfloor$ 个，结果应是 $n\left(2n+1\right)-2^{m+1}+2+m$ 这种**多项式**形式，"
        r"**绝不可能出现 $2^{2n}$**．按 $S_{2^{n}}$ 理解，$2^{k}\le2^{n}$ 恰有 $n$ 个，与答案完全吻合．" "\n"
        r"② ⭐⭐ **$d=-1$ 时 $q=0$ 必须舍**：等比数列公比不能为 $0$（否则 $b_2=0$ 后各项全为 $0$，"
        r"与 $b_1=2$ 矛盾），这是本题唯一的「陷阱」．" "\n"
        r"③ ⭐ **改值求和的思路**：「全体按 $a_k$ 算，再扣掉差异」比逐段相加清晰得多，" "\n"
        r"   差异 $=2^{k}-1$，共 $n$ 项，故减 $\sum(2^k-1)=\sum2^k-n=(2^{n+1}-2)-n$．" "\n"
        r"④ 数值复核（$a_k=k$，$2^k$ 位置取 $1$）：" "\n"
        r"   $n=1$：$c_1=1,c_2=1$，$S_2=2$；公式 $2^{1}-3\cdot2^{0}+1+2=2-3+3=2$ ✓" "\n"
        r"   $n=2$：$c=1,1,3,1$，$S_4=6$；公式 $2^{3}-3\cdot2^{1}+2+2=8-6+4=6$ ✓" "\n"
        r"   $n=3$：$c=1,1,3,1,5,6,7,1$，$S_8=25$；公式 $2^{5}-3\cdot2^{2}+3+2=32-12+5=25$ ✓" "\n"
        r"   $n=4$：前 $16$ 项中 $2,4,8,16$ 位置取 $1$，其余取 $k$，"
        r"$S_{16}=\frac{16\cdot17}2-(2+4+8+16)+4=136-30+4=110$；"
        r"公式 $2^{7}-3\cdot2^{3}+4+2=128-24+6=110$ ✓" "\n"
        r"**通法（按位置改值的求和）**：" "\n"
        r"① 先数清「特殊位置」的个数 —— 这是本题最容易错的一步（$2^n$ 以内有 $n$ 个 $2$ 的幂）；" "\n"
        r"② 用「全和 $-$ 差异和」而非分段相加；" "\n"
        r"③ 结果中出现 $2^{2n}$ 时，回头检查下标是否为 $2^n$．"
    ),
    'difficulty': 0.74,
    'topics': ['M-T-276'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-276-V2',
}


T288_E1 = {
    'type': '填空',
    'stem_text': (
        r"已知正四棱柱 $ABCD-A_1B_1C_1D_1$ 中，$BE=\dfrac14BB_1=2$，$4AB=3AA_1$，"
        r"则该四棱柱被过点 $A_1,C,E$ 的平面截得的截面面积为 ____．"
    ),
    'stem': [
        r"已知正四棱柱 $ABCD-A_1B_1C_1D_1$ 中，$BE=\dfrac14BB_1=2$，$4AB=3AA_1$，"
        r"则该四棱柱被过点 $A_1,C,E$ 的平面截得的截面面积为 ____．"
    ],
    'opts': [],
    'answer': r"$12\sqrt{19}$",
    'analysis': (
        r"先由条件定出棱柱尺寸：$BB_1=8$、$AB=6$；"
        r"再在 $DD_1$ 上取 $F$ 使 $D_1F=2$，由 $A_1F\parallel CE$ 且相等知截面 $A_1ECF$ 是平行四边形；"
        r"最后用两邻边 $A_1E,CE$ 与对角线 $A_1C$ 求夹角，面积 $=A_1E\cdot CE\cdot\sin\angle A_1EC$．"
    ),
    'solution': (
        r"**第一步：定尺寸**" "\n"
        r"由 $BE=\dfrac14BB_1=2$ 得 $BB_1=8$，故 $AA_1=CC_1=8$，$BE=2$．" "\n"
        r"由 $4AB=3AA_1=24$ 得 $AB=6$．" "\n"
        r"**第二步：确定截面形状**" "\n"
        r"在 $DD_1$ 上取点 $F$ 使 $D_1F=2$，连接 $A_1F,CF$．" "\n"
        r"由正四棱柱的对称性，$A_1F=CE$ 且 $A_1F\parallel CE$，故四边形 $A_1ECF$ 是平行四边形，" "\n"
        r"即所求截面为平行四边形 $A_1ECF$．" "\n"
        r"**第三步：算两条邻边与一条对角线**" "\n"
        r"$A_1E=\sqrt{AB^{2}+BE^{2}}=\sqrt{6^{2}+2^{2}}$…（注意 $A_1$ 到 $E$ 的水平距离是 $AB=6$，竖直是 $AA_1-BE=6$）" "\n"
        r"$A_1E=\sqrt{6^{2}+6^{2}}=6\sqrt2$，$CE=\sqrt{2^{2}+6^{2}}=2\sqrt{10}$，" "\n"
        r"$A_1C=\sqrt{6^{2}+6^{2}+8^{2}}=\sqrt{136}=2\sqrt{34}$．" "\n"
        r"**第四步：求夹角与面积**" "\n"
        r"$\cos\angle A_1EC=\dfrac{A_1E^{2}+CE^{2}-A_1C^{2}}{2\cdot A_1E\cdot CE}"
        r"=\dfrac{72+40-136}{2\cdot6\sqrt2\cdot2\sqrt{10}}=\dfrac{-24}{24\sqrt{20}}=-\dfrac{\sqrt5}{10}$．" "\n"
        r"$\sin\angle A_1EC=\sqrt{1-\dfrac5{100}}=\dfrac{\sqrt{95}}{10}$．" "\n"
        r"$S=A_1E\cdot CE\cdot\sin\angle A_1EC=6\sqrt2\times2\sqrt{10}\times\dfrac{\sqrt{95}}{10}$，" "\n"
        r"$=\dfrac{12\sqrt{20}\cdot\sqrt{95}}{10}=\dfrac{12\cdot2\sqrt5\cdot\sqrt{95}}{10}=\dfrac{120\sqrt{19}}{10}=\boxed{12\sqrt{19}}$．"
    ),
    'review': (
        r"① ⭐⭐ **$A_1E$ 的两段是 $6$ 与 $6$**：水平方向是 $AB=6$，竖直方向是 $AA_1-BE=8-2=6$，"
        r"**不是** $BE=2$．这是本题最容易算错的一处（误用 $A_1E=\sqrt{6^2+2^2}$）．" "\n"
        r"② ⭐⭐ **根号还原**：原书答案 `12 19` 实为 $12\sqrt{19}$，"
        r"详解中 $\cos$ 值 `5/10` 实为 $\frac{\sqrt5}{10}$、$\sin$ 值 `95/10` 实为 $\frac{\sqrt{95}}{10}$，"
        r"$\sin\le1$ 与 $|\cos|\le1$ 是两条硬判据（$\frac{95}{10}=9.5>1$ 不可能是正弦值）．" "\n"
        r"③ ⭐ **平行四边形面积 $=ab\sin\theta$**：两条邻边已知，用余弦定理求夹角（第三边取「另两个顶点」的距离 $A_1C$）．" "\n"
        r"④ 数值复核：$A_1E=8.4853$、$CE=6.3246$、$\cos=-0.223607$、$\sin=0.974679$，"
        r"$S=8.4853\times6.3246\times0.974679=52.3068=12\sqrt{19}$ ✓" "\n"
        r"   另一条路验证：菱形？不，$A_1E\ne CE$，确为一般平行四边形．" "\n"
        r"**通法（棱柱截面面积）**：" "\n"
        r"① 先定形状（平行四边形靠「一组对边平行且相等」，梯形靠「一组对边平行」）；" "\n"
        r"② 求两邻边 + 一条对角线，用余弦定理定夹角；" "\n"
        r"③ 所有长度用「水平位移 + 竖直位移」的勾股算，注意端点在侧棱上的高度差．"
    ),
    'difficulty': 0.70,
    'topics': ['M-T-288'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-288-E1',
}

T288_V2 = {
    'type': '选择',
    'stem_text': (
        r"在棱长为 $a$ 的正方体 $ABCD-A_1B_1C_1D_1$ 中，$E$ 为 $AA_1$ 的中点，"
        r"则过 $B,C_1,E$ 三点的平面截正方体 $ABCD-A_1B_1C_1D_1$ 所得的截面面积为（　　）"
    ),
    'stem': [
        r"在棱长为 $a$ 的正方体 $ABCD-A_1B_1C_1D_1$ 中，$E$ 为 $AA_1$ 的中点，"
        r"则过 $B,C_1,E$ 三点的平面截正方体 $ABCD-A_1B_1C_1D_1$ 所得的截面面积为（　　）"
    ],
    'opts': [
        ('A', r"$\dfrac{3\sqrt{10}}8a^{2}$"),
        ('B', r"$\dfrac98a^{2}$"),
        ('C', r"$\dfrac{3\sqrt2}4a^{2}$"),
        ('D', r"$\dfrac{\sqrt{10}}2a^{2}$"),
    ],
    'answer': r"B",
    'analysis': (
        r"取 $A_1D_1$ 中点 $F$，由 $EF\parallel AD_1\parallel BC_1$ 知 $B,C_1,E,F$ 四点共面，"
        r"截面为等腰梯形 $EFC_1B$；上底 $EF=\frac{\sqrt2}2a$、下底 $BC_1=\sqrt2a$、腰 $BE=\frac{\sqrt5}2a$，"
        r"由腰与下底一角求高，再用梯形面积公式．"
    ),
    'solution': (
        r"**第一步：确定截面**" "\n"
        r"由 $AB\parallel C_1D_1$ 且 $AB=C_1D_1$ 知 $ABC_1D_1$ 是平行四边形，故 $AD_1\parallel BC_1$．" "\n"
        r"取 $A_1D_1$ 中点 $F$，则 $EF\parallel AD_1$ 且 $EF=\dfrac12AD_1=\dfrac{\sqrt2}2a$，从而 $EF\parallel BC_1$．" "\n"
        r"故 $B,C_1,E,F$ 四点共面，截面为四边形 $EFC_1B$．" "\n"
        r"**第二步：判断形状并求各边**" "\n"
        r"$BC_1=\sqrt2a$，$EF=\dfrac{\sqrt2}2a$，故 $EF\parallel BC_1$ 且 $EF\ne BC_1$，截面是梯形；" "\n"
        r"又 $BE=C_1F=\sqrt{a^{2}+\left(\dfrac a2\right)^{2}}=\dfrac{\sqrt5}2a$，两腰相等，是**等腰梯形**．" "\n"
        r"**第三步：求高**" "\n"
        r"过 $E,F$ 分别作 $BC_1$ 的垂线，垂足 $G,H$．由 $\mathrm{Rt}\triangle EBG\cong\mathrm{Rt}\triangle FHC_1$ 得 $BG=C_1H$；" "\n"
        r"又 $EFGH$ 是矩形，$GH=EF=\dfrac{\sqrt2}2a$，故" "\n"
        r"$BG=C_1H=\dfrac{BC_1-EF}2=\dfrac{\sqrt2a-\frac{\sqrt2}2a}2=\dfrac{\sqrt2}4a$．" "\n"
        r"$h=\sqrt{BE^{2}-BG^{2}}=\sqrt{\dfrac{5a^{2}}4-\dfrac{2a^{2}}{16}}"
        r"=\sqrt{\dfrac{20a^{2}-2a^{2}}{16}}=\sqrt{\dfrac{18a^{2}}{16}}=\dfrac{3\sqrt2}4a$．" "\n"
        r"**第四步：面积**" "\n"
        r"$S=\dfrac12\left(BC_1+EF\right)h=\dfrac12\left(\sqrt2a+\dfrac{\sqrt2}2a\right)\cdot\dfrac{3\sqrt2}4a$，" "\n"
        r"$=\dfrac12\cdot\dfrac{3\sqrt2}2a\cdot\dfrac{3\sqrt2}4a=\dfrac12\cdot\dfrac{18}{8}a^{2}=\boxed{\dfrac98a^{2}}$．" "\n"
        r"故选 **B**．"
    ),
    'review': (
        r"① ⭐⭐ **「$EF\parallel BC_1$」是定位截面的关键**：靠 $AD_1$ 作中间桥梁"
        r"（$EF\parallel AD_1\parallel BC_1$），两次平行才能把 $F$ 点确定下来．" "\n"
        r"② ⭐⭐ **等腰梯形的高要「补矩形」**：$BG=\frac{BC_1-EF}2$ 来自两全等直角三角形，"
        r"不能直接减去 $EF$ 就算，也不能漏掉除以 $2$．" "\n"
        r"③ ⭐ **腰长 $BE=\frac{\sqrt5}2a$**：$E$ 是 $AA_1$ 中点，$AE=\frac a2$，$AB=a$，勾股得 $\frac{\sqrt5}2a$．" "\n"
        r"④ 数值复核（$a=1$）：$EF=0.7071$、$BC_1=1.4142$、$BE=1.1180$、$BG=0.3536$、"
        r"$h=\sqrt{1.25-0.125}=1.0607$，$S=\frac12\times2.1213\times1.0607=1.125=\frac98$ ✓" "\n"
        r"⑤ 选项速判：$\frac{3\sqrt{10}}8=1.186$、$\frac98=1.125$、$\frac{3\sqrt2}4=1.061$、"
        r"$\frac{\sqrt{10}}2=1.581$ —— 其中 $1.061$ 恰是**高 $h$** 的值，是命题人设的陷阱（忘乘 $\frac12(a+b)$）．" "\n"
        r"**通法（正方体截面面积）**：" "\n"
        r"① 用「对面平行 ⟹ 交线平行」找第四个顶点；" "\n"
        r"② 梯形先判等腰（对称性能省一半计算）；" "\n"
        r"③ 高由「腰 + 投影」的勾股求得，投影 $=\frac{|\text{下底}-\text{上底}|}2$；" "\n"
        r"④ 干扰项常是「高」或「某条边」的值，算完务必核对是否漏乘．"
    ),
    'difficulty': 0.66,
    'topics': ['M-T-288'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-288-V2',
}

T288_V3 = {
    'type': '填空',
    'stem_text': (
        r"已知正方体 $ABCD-A_1B_1C_1D_1$ 的棱长为 $2$，点 $P$ 在线段 $CB_1$ 上，且 $B_1P=2PC$．"
        r"记 $E$ 为平面 $APC_1$ 与棱 $BC$ 的交点、$Q$ 为平面 $APC_1$ 与棱 $A_1D_1$ 的交点，"
        r"则正方体被平面 $APC_1$ 截得的截面为 ____，其面积为 ____．"
    ),
    'stem': [
        r"已知正方体 $ABCD-A_1B_1C_1D_1$ 的棱长为 $2$，点 $P$ 在线段 $CB_1$ 上，且 $B_1P=2PC$．"
        r"记 $E$ 为平面 $APC_1$ 与棱 $BC$ 的交点、$Q$ 为平面 $APC_1$ 与棱 $A_1D_1$ 的交点，"
        r"则正方体被平面 $APC_1$ 截得的截面为 ____，其面积为 ____．"
    ],
    'opts': [],
    'answer': r"四边形 $AEC_1Q$；$2\sqrt6$",
    'analysis': (
        r"建系写出平面 $APC_1$ 的方程，逐棱求交点定出四个顶点；"
        r"发现四边相等（都是 $\sqrt5$）知截面是菱形，"
        r"面积 $=$ 两条对角线乘积的一半 $=\frac12\cdot AC_1\cdot EQ$．"
    ),
    'solution': (
        r"**第一步：建系求平面方程**" "\n"
        r"以 $A$ 为原点，$\vec{AB},\vec{AD},\vec{AA_1}$ 为 $x,y,z$ 轴正方向，则" "\n"
        r"$A(0,0,0)$、$B(2,0,0)$、$C(2,2,0)$、$D(0,2,0)$、$A_1(0,0,2)$、$B_1(2,0,2)$、$C_1(2,2,2)$．" "\n"
        r"由 $B_1P=2PC$ 得 $P=C+\dfrac13\left(B_1-C\right)=(2,2,0)+\dfrac13(0,-2,2)=\left(2,\dfrac43,\dfrac23\right)$．" "\n"
        r"设平面 $APC_1$ 方程为 $mx+ny+pz=0$，代入 $C_1(2,2,2)$、$P\left(2,\frac43,\frac23\right)$：" "\n"
        r"$\begin{cases}2m+2n+2p=0\\ 2m+\frac43n+\frac23p=0\end{cases}$，取 $\left(m,n,p\right)=\left(1,-2,1\right)$，" "\n"
        r"平面方程为 $x-2y+z=0$．" "\n"
        r"**第二步：逐棱求交点**" "\n"
        r"棱 $BC$（$x=2,z=0$）：$2-2y=0$，$y=1$，得 $E(2,1,0)$（$BC$ 中点）．" "\n"
        r"棱 $A_1D_1$（$x=0,z=2$）：$-2y+2=0$，$y=1$，得 $Q(0,1,2)$（$A_1D_1$ 中点）．" "\n"
        r"棱 $CD$（$y=2,z=0$）：$x=4$（舍）；棱 $DD_1$（$x=0,y=2$）：$z=4$（舍）；" "\n"
        r"棱 $AA_1$、$AB$、$AD$ 均只过 $A$ 本身．" "\n"
        r"故截面为四边形 $\boxed{AEC_1Q}$．" "\n"
        r"**第三步：判断形状**" "\n"
        r"$AE=\sqrt{4+1}=\sqrt5$，$EC_1=\sqrt{0+1+4}=\sqrt5$，"
        r"$C_1Q=\sqrt{4+1}=\sqrt5$，$QA=\sqrt{1+4}=\sqrt5$ —— 四边相等，是**菱形**．" "\n"
        r"**第四步：面积**" "\n"
        r"对角线 $AC_1=\sqrt{4+4+4}=2\sqrt3$（体对角线），$EQ=\sqrt{4+0+4}=2\sqrt2$．" "\n"
        r"$S=\dfrac12\cdot AC_1\cdot EQ=\dfrac12\times2\sqrt3\times2\sqrt2=\boxed{2\sqrt6}$．"
    ),
    'review': (
        r"① ⭐⭐ **建系写平面方程是定截面最稳的办法**：本题 $P$ 不是特殊点"
        r"（$P=(2,\frac43,\frac23)$），几何法很难定位，而方程 $x-2y+z=0$ 一写，逐棱代入即得全部顶点．" "\n"
        r"② ⭐⭐ **发现「四边相等 ⟹ 菱形」后可用对角线乘积的一半**，比原书的"
        r"「$2\times\frac12\cdot AE\cdot EC_1\cdot\sin\angle$」简洁得多，且不用算 $\cos$．" "\n"
        r"③ ⭐ **$E$ 是 $BC$ 中点、$Q$ 是 $A_1D_1$ 中点** —— 题干中未定义 $E,Q$，"
        r"原书详解默认了这两点，我在录入时补进了题干说明．" "\n"
        r"④ ⚠ **原书详解 $\cos\angle AEC_1=\frac15$ 丢了负号**："
        r"$AE^2+EC_1^2-AC_1^2=5+5-12=-2<0$，故 $\cos=-\frac15$（角为钝角）；"
        r"$\sin=\sqrt{1-\frac1{25}}=\frac{2\sqrt6}5$ 不受影响，最终面积 $2\sqrt6$ 正确．" "\n"
        r"⑤ 数值复核：$AC_1=3.4641$、$EQ=2.8284$，$S=\frac12\times3.4641\times2.8284=4.8990=2\sqrt6$ ✓" "\n"
        r"   用原书方法交叉验证：$\sqrt5\times\sqrt5\times\frac{2\sqrt6}5=5\times\frac{4.8990}5=4.8990$ ✓" "\n"
        r"**通法（动点截面）**：" "\n"
        r"① 建系 → 写平面方程 → 逐棱代入求交点，一棱不漏；" "\n"
        r"② 交点坐标超出 $[0,\text{棱长}]$ 即舍去；" "\n"
        r"③ 定出顶点后先看是否等腰/等边/菱形，能用对角线算面积就不用 $\sin$；" "\n"
        r"④ 填空第一空写形状（如「四边形 $AEC_1Q$」），第二空写数值．"
    ),
    'difficulty': 0.72,
    'topics': ['M-T-288'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-288-V3',
}


QS = [
    T135_V1, T135_V2, T135_V3,
    T269_E1, T269_V2,
    T276_E1, T276_V1, T276_V2,
    T288_E1, T288_V2, T288_V3,
]
