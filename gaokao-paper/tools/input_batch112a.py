# -*- coding: utf-8 -*-
r"""第 112 批：数列「因式分解型 / 分组求和」+ 绝对值函数 + 柯西取等 + 三角导数

    python3 tools/run_batch.py 112

## 选题依据

按「详解完整 + 同页聚堆 + 无图依赖 + 可独立数值验算」筛出，原文集中在 p218、p424、p075 三页：

- M-T-259 两题（p218）：因式分解型求通项
- M-T-262-E1、M-T-264-E1（p218）：前 $n$ 项和与分组求和
- M-T-027-V3（p424 附近）：绝对值函数与「存在性」
- M-T-034-E1、M-T-035-E1（p424）：柯西取等与三元最值
- M-T-106-V1、M-T-107-V1（p075）：三角函数导数与切线平行

9 题全部由我独立推导一遍并数值对拍（过程写进每题 review）。

## 第一条：二次型递推 ⟹ 分组分解约去正因式（M-T-259-V1）

$$\left(n+1\right)a_{n+1}^{2}-na_n^{2}+a_{n+1}a_n=0\ \Longrightarrow\ n\left(a_{n+1}^{2}-a_n^{2}\right)+a_{n+1}\left(a_{n+1}+a_n\right)=0$$

关键是把 $\left(n+1\right)a_{n+1}^{2}$ 拆成 $na_{n+1}^{2}+a_{n+1}^{2}$，**凑出 $a_{n+1}^{2}-a_n^{2}$ 与公共因式 $\left(a_{n+1}+a_n\right)$**：

$$\left(a_{n+1}+a_n\right)\left[\left(n+1\right)a_{n+1}-na_n\right]=0$$

> ⭐⭐ 判据：递推式里 $a_{n+1}^2$ 与 $a_n^2$ 同现，就先凑平方差，再看能否约掉一个**恒正**的因式。
> ⚠ 常见错：约完后写成 $a_{n+1}=a_n$（常数数列）。正确的是 $\left(n+1\right)a_{n+1}=na_n$，即 $\left\{na_n\right\}$ 为常数。

## 第二条：$2n^{2}+n$ 写成 $n\left(2n+1\right)$ 才能十字相乘（M-T-259-V2）

$a_n^{2}-\left(n+1\right)a_n-2n^{2}-n=0$ 的常数项是 $-n\left(2n+1\right)$，于是

$$\left(a_n+n\right)\left[a_n-\left(2n+1\right)\right]=0$$

> ⭐⭐ 判据：**二次项系数为 $1$ 时，把常数项拆成两数之积，使两数之差等于一次项系数。**

## 第三条：「存在 $x$ 使 $\le$」用最小值，不是最大值（M-T-027-V3）

这是本批最易错的一处。「存在实数 $x$ 使得 $f\left(x\right)\le\left|x\right|+a$」⟺ $g_{\min}\le a+2$（其中 $g=\left|2x+1\right|-2\left|x\right|$），**不是** $g_{\max}$。

> ⭐⭐ 判据：**「存在」用最值的「有利」一侧（$\le$ 用最小、$\ge$ 用最大）；「恒成立」用另一侧。**

## 第四条：柯西取等 ⟹ 比例式直接给比值（M-T-034-E1）

$$\left(a^2+b^2+c^2\right)\left(x^2+y^2+z^2\right)\ge\left(ax+by+cz\right)^2$$

把已知数代进去正好取等（$10\times40=20^2$），说明 $\dfrac ax=\dfrac by=\dfrac cz=k$，于是 $a+b+c=k\left(x+y+z\right)$，而 $k^2=\dfrac{10}{40}=\dfrac14$ ⟹ $k=\dfrac12$。

> ⭐⭐ 判据：**两个平方和之积恰好等于叉积和的平方 ⟹ 必定取等 ⟹ 立刻写比例式。**
"""

# ==========================================================================
#  M-T-259  因式分解型求通项
# ==========================================================================

T259_V1 = {
    'type': '填空',
    'stem_text': (
        r"设 $\left\{a_n\right\}$ 是首项为 $1$ 的正项数列，且 $\left(n+1\right)a_{n+1}^{2}-na_n^{2}+a_{n+1}a_n=0\left(n=1,2,3,\cdots\right)$，"
        r"则 $a_4=$ ____，$a_n=$ ____"
    ),
    'stem': [
        r"设 $\left\{a_n\right\}$ 是首项为 $1$ 的正项数列，且 $\left(n+1\right)a_{n+1}^{2}-na_n^{2}+a_{n+1}a_n=0\left(n=1,2,3,\cdots\right)$，"
        r"则 $a_4=$ ____，$a_n=$ ____",
    ],
    'opts': [],
    'answer': r"$\dfrac14$；$\dfrac1n$",
    'analysis': (
        r"递推式是二次齐次的，先凑平方差 $a_{n+1}^{2}-a_n^{2}$，提出公共因式 $\left(a_{n+1}+a_n\right)$；"
        r"由正项数列知该因式恒正，可约去，得到 $\left(n+1\right)a_{n+1}=na_n$。"
    ),
    'solution': (
        r"将 $\left(n+1\right)a_{n+1}^{2}$ 拆成 $na_{n+1}^{2}+a_{n+1}^{2}$，原式化为" "\n"
        r"$$n\left(a_{n+1}^{2}-a_n^{2}\right)+\left(a_{n+1}^{2}+a_{n+1}a_n\right)=0,$$" "\n"
        r"即" "\n"
        r"$$n\left(a_{n+1}-a_n\right)\left(a_{n+1}+a_n\right)+a_{n+1}\left(a_{n+1}+a_n\right)=0,$$" "\n"
        r"$$\left(a_{n+1}+a_n\right)\left[n\left(a_{n+1}-a_n\right)+a_{n+1}\right]=0,$$" "\n"
        r"$$\left(a_{n+1}+a_n\right)\left[\left(n+1\right)a_{n+1}-na_n\right]=0.$$" "\n"
        r"因 $\left\{a_n\right\}$ 是正项数列，$a_{n+1}+a_n>0$，故" "\n"
        r"$$\left(n+1\right)a_{n+1}=na_n.$$" "\n"
        r"于是数列 $\left\{na_n\right\}$ 是常数数列：" "\n"
        r"$$na_n=\left(n-1\right)a_{n-1}=\cdots=2a_2=1\cdot a_1=1,$$" "\n"
        r"所以" "\n"
        r"$$a_n=\frac1n\quad\left(n\in\mathbf N^{\ast}\right),\qquad a_4=\frac14.$$" "\n"
        r"故答案为 $\dfrac14$；$\dfrac1n$。"
    ),
    'review': (
        r"① ⭐⭐ **分组分解是题眼**：把 $\left(n+1\right)a_{n+1}^2$ 拆成 $na_{n+1}^2+a_{n+1}^2$，" "\n"
        r"   才能凑出 $a_{n+1}^2-a_n^2$ 与公共因式 $\left(a_{n+1}+a_n\right)$。" "\n"
        r"② ⚠ **约去的因式必须确认恒正**：这里是正项数列，所以 $a_{n+1}+a_n>0$ 成立；" "\n"
        r"   若只是「非零数列」就不能这么约。" "\n"
        r"③ ⚠ **结论是 $\left(n+1\right)a_{n+1}=na_n$，不是 $a_{n+1}=a_n$** —— " "\n"
        r"   后者会得到常数数列 $a_n=1$，代入 $n=1$ 得 $2\cdot1-1\cdot1+1\cdot1=2\ne0$，矛盾。" "\n"
        r"④ 数值复核：$a_1=1$、$a_2=\dfrac12$、$a_3=\dfrac13$、$a_4=\dfrac14$。" "\n"
        r"   代回 $n=1$：$\left(2\right)\left(\dfrac14\right)-\left(1\right)\left(1\right)+\left(\dfrac12\right)\left(1\right)=0.5-1+0.5=0$ ✓" "\n"
        r"   代回 $n=2$：$\left(3\right)\left(\dfrac19\right)-\left(2\right)\left(\dfrac14\right)+\left(\dfrac13\right)\left(\dfrac12\right)=\dfrac13-\dfrac12+\dfrac16=0$ ✓" "\n"
        r"**通法（二次齐次递推）**：" "\n"
        r"① 拆系数凑平方差，提出公共因式；" "\n"
        r"② 用「正项 / 恒正」约去该因式，得到一阶递推；" "\n"
        r"③ 若得到 $na_n=\left(n-1\right)a_{n-1}$ 型，则 $\left\{na_n\right\}$ 为常数，直接写答案。"
    ),
    'difficulty': 0.60,
    'topics': ['M-T-259'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-259-V1',
}

T259_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知数列 $\left\{a_n\right\}$ 的各项均为正数，且满足 $a_n^{2}-\left(n+1\right)a_n-2n^{2}-n=0$。" "\n"
        r"（1）求 $a_1$，$a_2$ 及 $\left\{a_n\right\}$ 的通项公式；" "\n"
        r"（2）求数列 $\left\{2^{a_n}\right\}$ 的前 $n$ 项和 $S_n$。"
    ),
    'stem': [
        r"已知数列 $\left\{a_n\right\}$ 的各项均为正数，且满足 $a_n^{2}-\left(n+1\right)a_n-2n^{2}-n=0$。",
        r"（1）求 $a_1$，$a_2$ 及 $\left\{a_n\right\}$ 的通项公式；",
        r"（2）求数列 $\left\{2^{a_n}\right\}$ 的前 $n$ 项和 $S_n$。",
    ],
    'opts': [],
    'answer': r"（1）$a_1=3$，$a_2=5$，$a_n=2n+1$；（2）$S_n=\dfrac{8\left(4^{n}-1\right)}{3}$",
    'analysis': (
        r"第（1）问把常数项 $-2n^{2}-n$ 写成 $-n\left(2n+1\right)$，即可十字相乘；" "\n"
        r"第（2）问注意是 $\left\{2^{a_n}\right\}$ 而不是 $\left\{2a_n\right\}$，通项为 $2^{2n+1}=2\cdot4^{n}$，是等比数列。"
    ),
    'solution': (
        r"（1）当 $n=1$ 时，$a_1^{2}-2a_1-3=0$，即 $\left(a_1-3\right)\left(a_1+1\right)=0$，由 $a_1>0$ 得 $a_1=3$；" "\n"
        r"当 $n=2$ 时，$a_2^{2}-3a_2-10=0$，即 $\left(a_2-5\right)\left(a_2+2\right)=0$，由 $a_2>0$ 得 $a_2=5$。" "\n"
        r"一般地，常数项 $-2n^{2}-n=-n\left(2n+1\right)$，故" "\n"
        r"$$a_n^{2}-\left(n+1\right)a_n-n\left(2n+1\right)=0,$$" "\n"
        r"$$\left(a_n+n\right)\left[a_n-\left(2n+1\right)\right]=0.$$" "\n"
        r"（因 $\left(2n+1\right)-n=n+1$，恰为一次项系数的相反数）" "\n"
        r"由 $a_n>0$、$n>0$ 知 $a_n+n>0$，故" "\n"
        r"$$a_n=2n+1.$$" "\n"
        r"（2）由（1）得 $2^{a_n}=2^{2n+1}=2\cdot4^{n}$，所以 $\left\{2^{a_n}\right\}$ 是首项 $2^{3}=8$、公比 $4$ 的等比数列，" "\n"
        r"$$S_n=\frac{8\left(1-4^{n}\right)}{1-4}=\frac{8\left(4^{n}-1\right)}{3}.$$"
    ),
    'review': (
        r"① ⭐⭐ **十字相乘的关键是拆常数项**：$-2n^2-n=-n\left(2n+1\right)$，而" "\n"
        r"   $\left(2n+1\right)-n=n+1$ 恰好等于一次项系数 $\left(n+1\right)$ 的相反数 —— 这是刻意配好的。" "\n"
        r"② ⚠ **第（2）问是 $2^{a_n}$ 不是 $2a_n$**：$2^{2n+1}=2\cdot4^n$，公比是 $4$ 不是 $2$。" "\n"
        r"   若误读成 $2a_n=4n+2$，就成了等差数列，与「前 $n$ 项和」的问法也对不上。" "\n"
        r"③ 数值复核：$n=1$ 时 $S_1=2^{3}=8$，公式给 $\dfrac{8\left(4-1\right)}3=8$ ✓；" "\n"
        r"   $n=2$ 时 $S_2=8+2^{5}=40$，公式给 $\dfrac{8\left(16-1\right)}3=40$ ✓" "\n"
        r"④ 通项验证：$n=3$ 时 $a_3^{2}-4a_3-21=0$ ⟹ $\left(a_3-7\right)\left(a_3+3\right)=0$ ⟹ $a_3=7=2\times3+1$ ✓" "\n"
        r"**通法（二次型求通项）**：" "\n"
        r"① 把常数项拆成两因式之积，使两因式之差等于一次项系数（二次项系数为 $1$）；" "\n"
        r"② 用「各项为正」舍去负根；" "\n"
        r"③ 若第（2）问出现 $2^{a_n}$，先化简指数，判断是等比还是等差。"
    ),
    'difficulty': 0.65,
    'topics': ['M-T-259'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-259-V2',
}

# ==========================================================================
#  M-T-262 / M-T-264  前 n 项和与分组求和
# ==========================================================================

T262_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知数列 $\left\{a_n\right\}$ 的前 $n$ 项和 $S_n=2^{n+1}-2$。" "\n"
        r"（1）求 $\left\{a_n\right\}$ 的通项公式；" "\n"
        r"（2）记 $b_n=\dfrac{n+1}{a_n}$，求 $\left\{b_n\right\}$ 的前 $n$ 项和 $T_n$。"
    ),
    'stem': [
        r"已知数列 $\left\{a_n\right\}$ 的前 $n$ 项和 $S_n=2^{n+1}-2$。",
        r"（1）求 $\left\{a_n\right\}$ 的通项公式；",
        r"（2）记 $b_n=\dfrac{n+1}{a_n}$，求 $\left\{b_n\right\}$ 的前 $n$ 项和 $T_n$。",
    ],
    'opts': [],
    'answer': r"（1）$a_n=2^{n}$；（2）$T_n=3-\dfrac{n+3}{2^{n}}$",
    'analysis': (
        r"第（1）问用 $a_n=S_n-S_{n-1}$（$n\ge2$）并单独验证 $n=1$；" "\n"
        r"第（2）问 $b_n=\dfrac{n+1}{2^{n}}$ 是「等差 $\times$ 等比」，用错位相减。"
    ),
    'solution': (
        r"（1）当 $n=1$ 时，$a_1=S_1=2^{2}-2=2$；" "\n"
        r"当 $n\ge2$ 时，" "\n"
        r"$$a_n=S_n-S_{n-1}=\left(2^{n+1}-2\right)-\left(2^{n}-2\right)=2^{n+1}-2^{n}=2^{n}\left(2-1\right)=2^{n}.$$" "\n"
        r"当 $n=1$ 时 $2^{1}=2=a_1$ 也成立，故" "\n"
        r"$$a_n=2^{n}\quad\left(n\in\mathbf N^{\ast}\right).$$" "\n"
        r"（2）$b_n=\dfrac{n+1}{2^{n}}$，则" "\n"
        r"$$T_n=\frac22+\frac34+\frac48+\cdots+\frac{n+1}{2^{n}},$$" "\n"
        r"$$\frac12T_n=\frac24+\frac38+\frac4{16}+\cdots+\frac{n}{2^{n}}+\frac{n+1}{2^{n+1}}.$$" "\n"
        r"两式相减：" "\n"
        r"$$\frac12T_n=\frac22+\left(\frac34-\frac24\right)+\left(\frac48-\frac38\right)+\cdots+\left(\frac{n+1}{2^{n}}-\frac{n}{2^{n}}\right)-\frac{n+1}{2^{n+1}}$$" "\n"
        r"$$=1+\left(\frac14+\frac18+\cdots+\frac1{2^{n}}\right)-\frac{n+1}{2^{n+1}}$$" "\n"
        r"$$=1+\frac{\dfrac14\left(1-\dfrac1{2^{n-1}}\right)}{1-\dfrac12}-\frac{n+1}{2^{n+1}}=1+\frac12-\frac1{2^{n}}-\frac{n+1}{2^{n+1}}$$" "\n"
        r"$$=\frac32-\frac{2}{2^{n+1}}-\frac{n+1}{2^{n+1}}=\frac32-\frac{n+3}{2^{n+1}}.$$" "\n"
        r"故" "\n"
        r"$$T_n=3-\frac{n+3}{2^{n}}.$$"
    ),
    'review': (
        r"① ⭐⭐ **必须单独验证 $n=1$**：$S_0$ 未定义，所以 $a_1=S_1=2$，而 $2^1=2$ 恰好吻合，" "\n"
        r"   故可以写成一个式子；若 $S_n$ 带常数项 $c\ne-2$，就会出现分段。" "\n"
        r"② ⭐⭐ **错位相减的对齐**：相减后中间每一项是 $\dfrac{\left(k+1\right)-k}{2^{k}}=\dfrac1{2^{k}}$，" "\n"
        r"   即 $k$ 从 $2$ 到 $n$ 的 $\dfrac1{2^k}$，首项是 $\dfrac22=1$（**不属于那个等比数列**）。" "\n"
        r"③ ⚠ 最后一项是 $-\dfrac{n+1}{2^{n+1}}$，别漏；" "\n"
        r"   分子合并：$\dfrac2{2^{n+1}}+\dfrac{n+1}{2^{n+1}}=\dfrac{n+3}{2^{n+1}}$。" "\n"
        r"④ 数值复核：$n=1$ 时 $T_1=\dfrac22=1$，公式给 $3-\dfrac42=1$ ✓；" "\n"
        r"   $n=2$ 时 $T_2=1+\dfrac34=1.75$，公式给 $3-\dfrac54=1.75$ ✓；" "\n"
        r"   $n=3$ 时 $T_3=1.75+\dfrac48=2.25$，公式给 $3-\dfrac68=2.25$ ✓" "\n"
        r"**通法（等差 $\times$ 等比求和）**：" "\n"
        r"① 写成 $T_n$ 与 $qT_n$（$q$ 为等比的公比）两式，右端错一位；" "\n"
        r"② 相减后中间部分必为**纯等比数列**（公差 $\times$ 公比的部分被消化掉）；" "\n"
        r"③ 结果形如「常数 $-\dfrac{\text{一次式}}{q^{n}}$」，可用 $n=1,2$ 两项快速自检。"
    ),
    'difficulty': 0.60,
    'topics': ['M-T-262'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-262-E1',
}

T264_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知数列 $\left\{a_n\right\}$ 的前 $n$ 项和 $S_n=2n^{2}-n$，数列 $\left\{b_n\right\}$ 满足 $4\log_2b_n=a_n+3$。" "\n"
        r"（1）求数列 $\left\{a_n\right\}$、$\left\{b_n\right\}$ 的通项公式；" "\n"
        r"（2）设 $c_n=b_n+\dfrac{4}{a_na_{n+1}}$，求数列 $\left\{c_n\right\}$ 的前 $n$ 项和 $T_n$。"
    ),
    'stem': [
        r"已知数列 $\left\{a_n\right\}$ 的前 $n$ 项和 $S_n=2n^{2}-n$，数列 $\left\{b_n\right\}$ 满足 $4\log_2b_n=a_n+3$。",
        r"（1）求数列 $\left\{a_n\right\}$、$\left\{b_n\right\}$ 的通项公式；",
        r"（2）设 $c_n=b_n+\dfrac{4}{a_na_{n+1}}$，求数列 $\left\{c_n\right\}$ 的前 $n$ 项和 $T_n$。",
    ],
    'opts': [],
    'answer': r"（1）$a_n=4n-3$，$b_n=2^{n}$；（2）$T_n=2^{n+1}-\dfrac{4n+2}{4n+1}$",
    'analysis': (
        r"第（1）问中 $a_n+3=4n$，恰好让 $4\log_2b_n=4n$，即 $b_n=2^{n}$（命题人刻意配好）；" "\n"
        r"第（2）问是「等比 + 裂项」的分组求和，$\dfrac{4}{\left(4n-3\right)\left(4n+1\right)}=\dfrac1{4n-3}-\dfrac1{4n+1}$。"
    ),
    'solution': (
        r"（1）当 $n=1$ 时，$a_1=S_1=2-1=1$；" "\n"
        r"当 $n\ge2$ 时，" "\n"
        r"$$a_n=S_n-S_{n-1}=\left(2n^{2}-n\right)-\left[2\left(n-1\right)^{2}-\left(n-1\right)\right]$$" "\n"
        r"$$=2n^{2}-n-\left(2n^{2}-5n+3\right)=4n-3.$$" "\n"
        r"当 $n=1$ 时 $4\times1-3=1=a_1$ 也成立，故 $a_n=4n-3$。" "\n"
        r"又 $4\log_2b_n=a_n+3=\left(4n-3\right)+3=4n$，所以 $\log_2b_n=n$，即" "\n"
        r"$$b_n=2^{n}.$$" "\n"
        r"（2）因为 $a_{n+1}=4\left(n+1\right)-3=4n+1$，且" "\n"
        r"$$\frac1{4n-3}-\frac1{4n+1}=\frac{\left(4n+1\right)-\left(4n-3\right)}{\left(4n-3\right)\left(4n+1\right)}=\frac4{a_na_{n+1}},$$" "\n"
        r"所以" "\n"
        r"$$c_n=2^{n}+\frac1{4n-3}-\frac1{4n+1}.$$" "\n"
        r"分组求和：" "\n"
        r"$$T_n=\sum_{k=1}^{n}2^{k}+\sum_{k=1}^{n}\left(\frac1{4k-3}-\frac1{4k+1}\right)$$" "\n"
        r"$$=\left(2^{n+1}-2\right)+\left[\left(1-\frac15\right)+\left(\frac15-\frac19\right)+\cdots+\left(\frac1{4n-3}-\frac1{4n+1}\right)\right]$$" "\n"
        r"$$=2^{n+1}-2+1-\frac1{4n+1}=2^{n+1}-1-\frac1{4n+1}=2^{n+1}-\frac{4n+2}{4n+1}.$$"
    ),
    'review': (
        r"① ⭐⭐ **裂项系数 $=\dfrac1{\text{两因子之差}}$**：$a_{n+1}-a_n=4$，而分子是 $4$，" "\n"
        r"   故 $\dfrac4{a_na_{n+1}}=\dfrac1{a_n}-\dfrac1{a_{n+1}}$（系数为 $\dfrac44=1$，恰好不用乘）。" "\n"
        r"   若分子是 $1$，就要乘 $\dfrac14$ —— 这是最高频丢分点。" "\n"
        r"② ⭐ **两组分别求和**：等比部分 $\sum2^k=2^{n+1}-2$（首项 $2$、公比 $2$、$n$ 项），" "\n"
        r"   裂项部分只剩首项的「正部」与末项的「负部」。" "\n"
        r"③ ⚠ 最后合并：$-1-\dfrac1{4n+1}=-\dfrac{4n+1+1}{4n+1}=-\dfrac{4n+2}{4n+1}$。" "\n"
        r"④ 数值复核：$n=1$ 时 $c_1=2+\dfrac4{1\times5}=2.8$，公式给 $4-\dfrac65=2.8$ ✓；" "\n"
        r"   $n=2$ 时 $c_2=4+\dfrac4{5\times9}=4.0889$，$T_2=6.8889$，公式给 $8-\dfrac{10}9=6.8889$ ✓" "\n"
        r"**通法（等比 + 裂项分组求和）**：" "\n"
        r"① 先把通项拆成「等比型」与「可裂项型」两部分；" "\n"
        r"② 裂项时先算 $a_{n+1}-a_n$，再用 $\dfrac{\text{分子}}{a_{n+1}-a_n}$ 定系数；" "\n"
        r"③ 两组各自求和后相加，用 $n=1$、$n=2$ 两项自检。"
    ),
    'difficulty': 0.65,
    'topics': ['M-T-264'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-264-E1',
}

# ==========================================================================
#  M-T-027  绝对值函数
# ==========================================================================

T027_V3 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f\left(x\right)=\left|2x+1\right|-\left|x\right|-2$。" "\n"
        r"（1）解不等式 $f\left(x\right)\ge0$；" "\n"
        r"（2）若存在实数 $x$，使得 $f\left(x\right)\le\left|x\right|+a$，求实数 $a$ 的取值范围。"
    ),
    'stem': [
        r"已知函数 $f\left(x\right)=\left|2x+1\right|-\left|x\right|-2$。",
        r"（1）解不等式 $f\left(x\right)\ge0$；",
        r"（2）若存在实数 $x$，使得 $f\left(x\right)\le\left|x\right|+a$，求实数 $a$ 的取值范围。",
    ],
    'opts': [],
    'answer': r"（1）$\left(-\infty,-3\right]\cup\left[1,+\infty\right)$；（2）$a\ge-3$",
    'analysis': (
        r"第（1）问按零点 $x=-\dfrac12$、$x=0$ 三段去绝对值；" "\n"
        r"第（2）问移项成 $\left|2x+1\right|-2\left|x\right|\lea+2$，再求左边的最小值（注意是「存在」）。"
    ),
    'solution': (
        r"（1）绝对值的零点为 $x=-\dfrac12$ 与 $x=0$，分三段：" "\n"
        r"① 当 $x\le-\dfrac12$ 时，$f\left(x\right)=-\left(2x+1\right)-\left(-x\right)-2=-x-3$。" "\n"
        r"   由 $-x-3\ge0$ 得 $x\le-3$，结合 $x\le-\dfrac12$ 得 $x\le-3$；" "\n"
        r"② 当 $-\dfrac12<x<0$ 时，$f\left(x\right)=\left(2x+1\right)-\left(-x\right)-2=3x-1$。" "\n"
        r"   由 $3x-1\ge0$ 得 $x\ge\dfrac13$，与 $-\dfrac12<x<0$ 矛盾，故此段无解；" "\n"
        r"③ 当 $x\ge0$ 时，$f\left(x\right)=\left(2x+1\right)-x-2=x-1$。由 $x-1\ge0$ 得 $x\ge1$。" "\n"
        r"综上，不等式的解集为 $\left(-\infty,-3\right]\cup\left[1,+\infty\right)$。" "\n"
        r"（2）$f\left(x\right)\le\left|x\right|+a$ 即" "\n"
        r"$$\left|2x+1\right|-\left|x\right|-2\le\left|x\right|+a\ \Longleftrightarrow\ \left|2x+1\right|-2\left|x\right|\lea+2.$$" "\n"
        r"令 $g\left(x\right)=\left|2x+1\right|-2\left|x\right|$，同样分三段：" "\n"
        r"① 当 $x\le-\dfrac12$ 时，$g\left(x\right)=-\left(2x+1\right)+2x=-1$；" "\n"
        r"② 当 $-\dfrac12<x<0$ 时，$g\left(x\right)=\left(2x+1\right)+2x=4x+1\in\left(-1,1\right)$；" "\n"
        r"③ 当 $x\ge0$ 时，$g\left(x\right)=\left(2x+1\right)-2x=1$。" "\n"
        r"故 $g\left(x\right)$ 的值域为 $\left[-1,1\right]$，最小值为 $-1$（在 $x\le-\dfrac12$ 时取到）。" "\n"
        r"「存在实数 $x$ 使得 $g\left(x\right)\lea+2$」等价于 $g_{\min}\lea+2$，即" "\n"
        r"$$-1\lea+2\ \Longrightarrow\ a\ge-3.$$"
    ),
    'review': (
        r"① ⭐⭐ **「存在」用最小值，「恒成立」用最大值** —— 这是本批最易错的一处。" "\n"
        r"   若误用 $g_{\max}=1$ 会得 $1\le a+2$ 即 $a\ge-1$，答案错。" "\n"
        r"② ⭐ **$g\left(x\right)=\left|2x+1\right|-2\left|x\right|$ 的最值可直接看两端**：" "\n"
        r"   $x\to-\infty$ 时 $\left|2x+1\right|\approx-2x$、$2\left|x\right|=-2x$，差趋于 $\dfrac{2x}{-2x}$ 的系数差 $-1$；" "\n"
        r"   $x\to+\infty$ 时趋于 $2x-2x=1$。故值域 $\left[-1,1\right]$。" "\n"
        r"③ ⚠ **第（1）问中间段最容易出错**：$-\dfrac12<x<0$ 时 $\left|x\right|=-x$ 而不是 $x$，" "\n"
        r"   $f=2x+1+x-2=3x-1$，在 $x\ge\dfrac13$ 才非负，与该段无交。" "\n"
        r"④ 数值复核：$x=-3$ 时 $f=\left|-5\right|-3-2=0$ ✓；$x=1$ 时 $f=3-1-2=0$ ✓；" "\n"
        r"   $x=-1$ 时 $f=1-1-2=-2<0$（不在解集内）✓；$x=2$ 时 $f=5-2-2=1\ge0$ ✓" "\n"
        r"   第（2）问：$a=-3$ 时取 $x=-1$，$g\left(-1\right)=1-2=-1\le-1$ ✓ 成立。" "\n"
        r"**通法（绝对值函数）**：" "\n"
        r"① 找所有零点，按零点分段，每段内去掉绝对值写成一次式；" "\n"
        r"② 解不等式时每段的结果要与该段范围取交集；" "\n"
        r"③ 「存在 / 恒成立」问题：先看清楚是哪一侧，再取相应的最值。"
    ),
    'difficulty': 0.60,
    'topics': ['M-T-027'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-027-V3',
}

# ==========================================================================
#  M-T-034  柯西取等与「圆系凑配」
# ==========================================================================

T034_E1 = {
    'type': '填空',
    'stem_text': (
        r"设 $a,b,c,x,y,z$ 是正数，且 $a^{2}+b^{2}+c^{2}=10$，$x^{2}+y^{2}+z^{2}=40$，$ax+by+cz=20$，"
        r"则 $\dfrac{a+b+c}{x+y+z}=$ ____"
    ),
    'stem': [
        r"设 $a,b,c,x,y,z$ 是正数，且 $a^{2}+b^{2}+c^{2}=10$，$x^{2}+y^{2}+z^{2}=40$，$ax+by+cz=20$，"
        r"则 $\dfrac{a+b+c}{x+y+z}=$ ____",
    ],
    'opts': [],
    'answer': r"$\dfrac12$",
    'analysis': (
        r"先看柯西不等式是否取等：$10\times40=400=20^{2}$ 恰好相等，说明必定取等，" "\n"
        r"于是 $\dfrac ax=\dfrac by=\dfrac cz=k$，比值就是 $k$，而 $k^{2}=\dfrac{10}{40}=\dfrac14$。"
    ),
    'solution': (
        r"由柯西不等式" "\n"
        r"$$\left(a^{2}+b^{2}+c^{2}\right)\left(x^{2}+y^{2}+z^{2}\right)\ge\left(ax+by+cz\right)^{2},$$" "\n"
        r"代入已知得 $10\times40=400$，而 $\left(ax+by+cz\right)^{2}=20^{2}=400$，**两边恰好相等**，故取等条件成立：" "\n"
        r"$$\frac ax=\frac by=\frac cz=k\quad\left(k>0\right).$$" "\n"
        r"于是 $a=kx$、$b=ky$、$c=kz$，代入 $a^{2}+b^{2}+c^{2}=10$：" "\n"
        r"$$k^{2}\left(x^{2}+y^{2}+z^{2}\right)=40k^{2}=10\ \Longrightarrow\ k^{2}=\frac14\ \Longrightarrow\ k=\frac12.$$" "\n"
        r"故" "\n"
        r"$$\frac{a+b+c}{x+y+z}=\frac{k\left(x+y+z\right)}{x+y+z}=k=\frac12.$$"
    ),
    'review': (
        r"① ⭐⭐ **先算两边是否相等**：$10\times40=20^{2}$ 是本題的全部机关。" "\n"
        r"   一旦相等，就能直接用取等条件写出比例式，不必构造任何辅助量。" "\n"
        r"② ⭐ **取等条件的方向**：柯西 $\left(\sum a^2\right)\left(\sum x^2\right)\ge\left(\sum ax\right)^2$ 取等时" "\n"
        r"   $\dfrac ax=\dfrac by=\dfrac cz$，即**两组变量成比例**（不是 $a=b=c$）。" "\n"
        r"③ ⚠ $k$ 取正值：因 $a,b,c,x,y,z$ 全为正，故 $k=\dfrac12$ 而非 $-\dfrac12$。" "\n"
        r"④ 构造验证：取 $x=y=z=\sqrt{\dfrac{40}3}$，则 $a=b=c=\dfrac12\sqrt{\dfrac{40}3}$，" "\n"
        r"   $a^2+b^2+c^2=3\times\dfrac14\times\dfrac{40}3=10$ ✓，$ax+by+cz=3\times\dfrac12\times\dfrac{40}3=20$ ✓，" "\n"
        r"   比值 $=\dfrac{3\times\frac12\sqrt{40/3}}{3\times\sqrt{40/3}}=\dfrac12$ ✓" "\n"
        r"**通法（柯西取等型）**：" "\n"
        r"① 把已知的两个「平方和」相乘，与「叉积和的平方」比较；" "\n"
        r"② 相等 ⟹ 取等 ⟹ 写比例式 $\dfrac{a_i}{x_i}=k$；" "\n"
        r"③ $k=\sqrt{\dfrac{\sum a^2}{\sum x^2}}$，所求「和之比」往往就是这个 $k$。"
    ),
    'difficulty': 0.55,
    'topics': ['M-T-034'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-034-E1',
}

# ==========================================================================
#  M-T-035  三元不等式证明
# ==========================================================================

T035_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知 $a,b,c$ 都是正数，且 $a^{2}+b^{2}+c^{2}=1$，用 $\max\left\{a,b,c\right\}$ 表示 $a,b,c$ 的最大值，" "\n"
        r"$M=\max\left\{a+\dfrac1b,\ b+\dfrac1c,\ c+\dfrac1a\right\}$。" "\n"
        r"（1）证明 $\dfrac1{a^{2}}+\dfrac1{b^{2}}+\dfrac1{c^{2}}\ge9$；" "\n"
        r"（2）求 $M$ 的最小值。"
    ),
    'stem': [
        r"已知 $a,b,c$ 都是正数，且 $a^{2}+b^{2}+c^{2}=1$，用 $\max\left\{a,b,c\right\}$ 表示 $a,b,c$ 的最大值，",
        r"$M=\max\left\{a+\dfrac1b,\ b+\dfrac1c,\ c+\dfrac1a\right\}$。",
        r"（1）证明 $\dfrac1{a^{2}}+\dfrac1{b^{2}}+\dfrac1{c^{2}}\ge9$；",
        r"（2）求 $M$ 的最小值。",
    ],
    'opts': [],
    'answer': r"（1）证明见解析；（2）$\dfrac{4\sqrt3}{3}$",
    'analysis': (
        r"第（1）问用「$1$ 的代换」把 $a^{2}+b^{2}+c^{2}=1$ 代进每个分式；" "\n"
        r"第（2）问由 $M$ 不小于三者中的任一个，得 $3M^{2}\ge$ 三者的平方和，再用柯西与" "\n"
        r"$\left(a+b+c\right)\left(\dfrac1a+\dfrac1b+\dfrac1c\right)\ge9$ 放缩。"
    ),
    'solution': (
        r"（1）由 $a^{2}+b^{2}+c^{2}=1$ 得" "\n"
        r"$$\frac1{a^{2}}+\frac1{b^{2}}+\frac1{c^{2}}=\frac{a^{2}+b^{2}+c^{2}}{a^{2}}+\frac{a^{2}+b^{2}+c^{2}}{b^{2}}+\frac{a^{2}+b^{2}+c^{2}}{c^{2}}$$" "\n"
        r"$$=3+\left(\frac{b^{2}}{a^{2}}+\frac{a^{2}}{b^{2}}\right)+\left(\frac{c^{2}}{a^{2}}+\frac{a^{2}}{c^{2}}\right)+\left(\frac{c^{2}}{b^{2}}+\frac{b^{2}}{c^{2}}\right)$$" "\n"
        r"$$\ge3+2\sqrt{\frac{b^{2}}{a^{2}}\cdot\frac{a^{2}}{b^{2}}}+2\sqrt{\frac{c^{2}}{a^{2}}\cdot\frac{a^{2}}{c^{2}}}+2\sqrt{\frac{c^{2}}{b^{2}}\cdot\frac{b^{2}}{c^{2}}}=3+2+2+2=9.$$" "\n"
        r"当且仅当 $a=b=c=\dfrac1{\sqrt3}$ 时取等。" "\n"
        r"（2）由 $M$ 的定义，$M\gea+\dfrac1b$，$M\geb+\dfrac1c$，$M\gec+\dfrac1a$，于是" "\n"
        r"$$3M^{2}\ge\left(a+\frac1b\right)^{2}+\left(b+\frac1c\right)^{2}+\left(c+\frac1a\right)^{2}.$$" "\n"
        r"由柯西不等式" "\n"
        r"$$3\left[\left(a+\frac1b\right)^{2}+\left(b+\frac1c\right)^{2}+\left(c+\frac1a\right)^{2}\right]\ge\left[\left(a+\frac1b\right)+\left(b+\frac1c\right)+\left(c+\frac1a\right)\right]^{2},$$" "\n"
        r"故" "\n"
        r"$$9M^{2}\ge\left[\left(a+b+c\right)+\left(\frac1a+\frac1b+\frac1c\right)\right]^{2}.$$" "\n"
        r"又由柯西 $\left(a+b+c\right)^{2}\le3\left(a^{2}+b^{2}+c^{2}\right)=3$，得 $a+b+c\le\sqrt3$；" "\n"
        r"由 $\left(a+b+c\right)\left(\dfrac1a+\dfrac1b+\dfrac1c\right)\ge9$，得 $\dfrac1a+\dfrac1b+\dfrac1c\ge\dfrac9{a+b+c}$。" "\n"
        r"记 $p=a+b+c\in\left(0,\sqrt3\right]$，则" "\n"
        r"$$\left(a+b+c\right)+\left(\frac1a+\frac1b+\frac1c\right)\gep+\frac9p.$$" "\n"
        r"函数 $p+\dfrac9p$ 在 $p\in\left(0,3\right)$ 上单调递减（导数为 $1-\dfrac9{p^{2}}<0$），而 $p\le\sqrt3<3$，" "\n"
        r"故其最小值在 $p=\sqrt3$ 处取到：$\sqrt3+\dfrac9{\sqrt3}=\sqrt3+3\sqrt3=4\sqrt3$。" "\n"
        r"于是 $9M^{2}\ge\left(4\sqrt3\right)^{2}=48$，即 $M^{2}\ge\dfrac{16}3$，$M\ge\dfrac4{\sqrt3}=\dfrac{4\sqrt3}3$。" "\n"
        r"当 $a=b=c=\dfrac1{\sqrt3}$ 时，$a+\dfrac1b=\dfrac1{\sqrt3}+\sqrt3=\dfrac{4\sqrt3}3$，三者相等，取等成立。" "\n"
        r"故 $M$ 的最小值为 $\dfrac{4\sqrt3}3$。"
    ),
    'review': (
        r"① ⭐⭐ **两次柯西的方向不同**：第一次是 $3\sum u_i^2\ge\left(\sum u_i\right)^2$（平方和 ≥ 和²/个数），" "\n"
        r"   第二次是 $\left(a+b+c\right)^2\le3\left(a^2+b^2+c^2\right)$（和² ≤ 个数×平方和）。" "\n"
        r"   方向搞反会导致不等号无法传递。" "\n"
        r"② ⭐ **$p+\dfrac9p$ 的单调性**：导数 $1-\dfrac9{p^2}$，在 $p<3$ 时为负，故递减。" "\n"
        r"   而 $p\le\sqrt3<3$，所以最小值在 $p$ 最大处（$p=\sqrt3$）取到 —— 这一步不能想当然。" "\n"
        r"③ ⚠ **取等必须能同时成立**：$a=b=c=\dfrac1{\sqrt3}$ 同时满足" "\n"
        r"   $a+b+c=\sqrt3$（柯西取等）与 $a=b=c$（倒数不等式取等），故最小值可达。" "\n"
        r"④ 数值复核：$a=b=c=0.57735$ 时 $a+\dfrac1b=0.57735+1.73205=2.30940$，" "\n"
        r"   而 $\dfrac{4\sqrt3}3=2.30940$ ✓ 完全一致。" "\n"
        r"   另取 $a=0.8,b=0.5,c=\sqrt{1-0.64-0.25}=0.33166$：" "\n"
        r"   $a+\dfrac1b=2.8$、$b+\dfrac1c=3.515$、$c+\dfrac1a=1.582$，$M=3.515>2.309$ ✓" "\n"
        r"**通法（$\max$ 型三元最值）**：" "\n"
        r"① 由 $M\ge$ 每一项，得 $3M^2\ge$ 三项平方和；" "\n"
        r"② 用平方和 ≥ 和²/3 化成「和」的下界问题；" "\n"
        r"③ 和的下界常由 $\left(a+b+c\right)\left(\frac1a+\frac1b+\frac1c\right)\ge9$ 给出；" "\n"
        r"④ 最后验证取等点同时满足所有等号条件。"
    ),
    'difficulty': 0.78,
    'topics': ['M-T-035'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-035-E1',
}

# ==========================================================================
#  M-T-106  三角函数与导数
# ==========================================================================

T106_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f\left(x\right)=\cos^{2}x\cos2x$。" "\n"
        r"（1）讨论函数 $f\left(x\right)$ 在区间 $\left(0,\pi\right)$ 上的单调性；" "\n"
        r"（2）求函数 $f\left(x\right)$ 的最值。"
    ),
    'stem': [
        r"已知函数 $f\left(x\right)=\cos^{2}x\cos2x$。",
        r"（1）讨论函数 $f\left(x\right)$ 在区间 $\left(0,\pi\right)$ 上的单调性；",
        r"（2）求函数 $f\left(x\right)$ 的最值。",
    ],
    'opts': [],
    'answer': (
        r"（1）在 $\left(\dfrac\pi3,\dfrac\pi2\right)$ 和 $\left(\dfrac{2\pi}3,\pi\right)$ 上单调递增，"
        r"在 $\left(0,\dfrac\pi3\right)$ 和 $\left(\dfrac\pi2,\dfrac{2\pi}3\right)$ 上单调递减；"
        r"（2）最大值为 $1$，最小值为 $-\dfrac18$"
    ),
    'analysis': (
        r"求导后用 $2\cos^{2}x=1+\cos2x$ 把导数化成 $-\sin2x\left(2\cos2x+1\right)$，" "\n"
        r"两个因式各自的零点把 $\left(0,\pi\right)$ 分成四段，逐段定号即可。" "\n"
        r"求最值时注意 $f$ 的周期为 $\pi$，只需看 $\left[0,\pi\right]$。"
    ),
    'solution': (
        r"（1）" "\n"
        r"$$f'\left(x\right)=2\cos x\left(-\sin x\right)\cos2x+\cos^{2}x\left(-2\sin2x\right)$$" "\n"
        r"$$=-\sin2x\cos2x-2\cos^{2}x\cdot2\sin x\cos x=-\sin2x\cos2x-2\cos^{2}x\sin2x$$" "\n"
        r"$$=-\sin2x\left(\cos2x+2\cos^{2}x\right).$$" "\n"
        r"由 $2\cos^{2}x=1+\cos2x$ 得 $\cos2x+2\cos^{2}x=2\cos2x+1$，故" "\n"
        r"$$f'\left(x\right)=-\sin2x\left(2\cos2x+1\right).$$" "\n"
        r"在 $x\in\left(0,\pi\right)$ 上，$2x\in\left(0,2\pi\right)$：$\sin2x=0$ 得 $x=\dfrac\pi2$；" "\n"
        r"$2\cos2x+1=0$ 即 $\cos2x=-\dfrac12$ 得 $2x=\dfrac{2\pi}3$ 或 $\dfrac{4\pi}3$，即 $x=\dfrac\pi3$ 或 $\dfrac{2\pi}3$。" "\n"
        r"逐段定号：" "\n"
        r"① $x\in\left(0,\dfrac\pi3\right)$：$2x\in\left(0,\dfrac{2\pi}3\right)$，$\sin2x>0$、$\cos2x>-\dfrac12$，故 $f'<0$，递减；" "\n"
        r"② $x\in\left(\dfrac\pi3,\dfrac\pi2\right)$：$2x\in\left(\dfrac{2\pi}3,\pi\right)$，$\sin2x>0$、$\cos2x<-\dfrac12$，故 $f'>0$，递增；" "\n"
        r"③ $x\in\left(\dfrac\pi2,\dfrac{2\pi}3\right)$：$2x\in\left(\pi,\dfrac{4\pi}3\right)$，$\sin2x<0$、$\cos2x<-\dfrac12$，故 $f'<0$，递减；" "\n"
        r"④ $x\in\left(\dfrac{2\pi}3,\pi\right)$：$2x\in\left(\dfrac{4\pi}3,2\pi\right)$，$\sin2x<0$、$\cos2x>-\dfrac12$，故 $f'>0$，递增。" "\n"
        r"（2）$f\left(x+\pi\right)=\cos^{2}\left(x+\pi\right)\cos\left(2x+2\pi\right)=\cos^{2}x\cos2x=f\left(x\right)$，故 $f$ 的周期为 $\pi$，" "\n"
        r"只需在 $\left[0,\pi\right]$ 上求最值。由（1）知极值点为 $x=\dfrac\pi3$、$\dfrac\pi2$、$\dfrac{2\pi}3$，连同端点：" "\n"
        r"$$f\left(0\right)=1\times1=1,\qquad f\left(\frac\pi3\right)=\frac14\times\left(-\frac12\right)=-\frac18,$$" "\n"
        r"$$f\left(\frac\pi2\right)=0\times\left(-1\right)=0,\qquad f\left(\frac{2\pi}3\right)=\frac14\times\left(-\frac12\right)=-\frac18,\qquad f\left(\pi\right)=1\times1=1.$$" "\n"
        r"故最大值为 $1$，最小值为 $-\dfrac18$。"
    ),
    'review': (
        r"① ⭐⭐ **化简的关键是 $2\cos^{2}x=1+\cos2x$**：不化这一步，导数里同时有 $\cos^2x$ 与 $\sin2x$，" "\n"
        r"   无法因式分解，也就定不了号。" "\n"
        r"② ⭐ **两个零点来源不同**：$\sin2x=0$ 来自一倍角部分，$2\cos2x+1=0$ 来自二倍角部分，" "\n"
        r"   三段变四段，缺一个就会得到错误的单调区间。" "\n"
        r"③ ⚠ **最值要看闭区间**：题（1）限定开区间 $\left(0,\pi\right)$ 只是讨论单调性，" "\n"
        r"   求最值时必须把端点 $x=0,\pi$ 也算上，最大值 $1$ 正是在端点取到。" "\n"
        r"④ ⭐ **先确认周期**：$f$ 周期为 $\pi$，所以「求最值」不必说明区间 —— 这是个隐含提示。" "\n"
        r"⑤ 数值复核：$x=\dfrac\pi3\approx1.0472$ 时 $\cos x=0.5$、$\cos2x=-0.5$，$f=0.25\times\left(-0.5\right)=-0.125$ ✓；" "\n"
        r"   $x=0.8$（在减区间 $\left(0,\frac\pi3\right)$ 外、$\left(\frac\pi3,\frac\pi2\right)$ 内）：$f\approx\cos^2 0.8\times\cos1.6=0.4843\times\left(-0.0292\right)=-0.0141$，" "\n"
        r"   比 $f\left(\frac\pi3\right)=-0.125$ 大，符合「递增」✓" "\n"
        r"**通法（三角函数求导）**：" "\n"
        r"① 用倍角/降幂公式把导数化成「几个因式之积」；" "\n"
        r"② 列出每个因式在给定区间内的全部零点，按大小排序分段；" "\n"
        r"③ 逐段定号；④ 最值 = 极值点 + 区间端点（或先确认周期）。"
    ),
    'difficulty': 0.65,
    'topics': ['M-T-106'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-106-V1',
}

# ==========================================================================
#  M-T-107  切线平行与构造新函数
# ==========================================================================

T107_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f\left(x\right)=\ln x-\ln a$，$g\left(x\right)=ae^{x}$，其中 $a$ 为常数，" "\n"
        r"函数 $y=f\left(x\right)$ 与 $x$ 轴的交点为 $A$，函数 $y=g\left(x\right)$ 的图象与 $y$ 轴的交点为 $B$，" "\n"
        r"函数 $y=f\left(x\right)$ 在 $A$ 点的切线与函数 $y=g\left(x\right)$ 在点 $B$ 处的切线互相平行。" "\n"
        r"（1）求 $a$ 的值；" "\n"
        r"（2）求函数 $F\left(x\right)=f\left(x\right)-g\left(x-1\right)$ 的单调区间。"
    ),
    'stem': [
        r"已知函数 $f\left(x\right)=\ln x-\ln a$，$g\left(x\right)=ae^{x}$，其中 $a$ 为常数，",
        r"函数 $y=f\left(x\right)$ 与 $x$ 轴的交点为 $A$，函数 $y=g\left(x\right)$ 的图象与 $y$ 轴的交点为 $B$，",
        r"函数 $y=f\left(x\right)$ 在 $A$ 点的切线与函数 $y=g\left(x\right)$ 在点 $B$ 处的切线互相平行。",
        r"（1）求 $a$ 的值；",
        r"（2）求函数 $F\left(x\right)=f\left(x\right)-g\left(x-1\right)$ 的单调区间。",
    ],
    'opts': [],
    'answer': r"（1）$a=1$；（2）单调递增区间为 $\left(0,1\right)$，单调递减区间为 $\left(1,+\infty\right)$",
    'analysis': (
        r"「与 $x$ 轴的交点」令 $y=0$，「与 $y$ 轴的交点」令 $x=0$，分别定出 $A$、$B$；" "\n"
        r"切线平行即两点处导数值相等。第（2）问注意 $g\left(x-1\right)=ae^{x-1}$，" "\n"
        r"导数 $F'\left(x\right)=\dfrac1x-e^{x-1}$ 的符号由 $xe^{x-1}$ 与 $1$ 的大小决定。"
    ),
    'solution': (
        r"（1）由 $f\left(x\right)=\ln x-\ln a=0$ 得 $\ln x=\ln a$，即 $x=a$，故 $A\left(a,0\right)$。" "\n"
        r"由 $x=0$ 得 $g\left(0\right)=ae^{0}=a$，故 $B\left(0,a\right)$。" "\n"
        r"又 $f'\left(x\right)=\dfrac1x$、$g'\left(x\right)=ae^{x}$，所以" "\n"
        r"$$f'\left(a\right)=\frac1a,\qquad g'\left(0\right)=a.$$" "\n"
        r"两条切线平行，故 $\dfrac1a=a$，即 $a^{2}=1$。由 $\ln a$ 有意义知 $a>0$，故" "\n"
        r"$$a=1.$$" "\n"
        r"（2）由（1）知 $f\left(x\right)=\ln x$、$g\left(x\right)=e^{x}$，于是" "\n"
        r"$$F\left(x\right)=f\left(x\right)-g\left(x-1\right)=\ln x-e^{x-1},\qquad x>0,$$" "\n"
        r"$$F'\left(x\right)=\frac1x-e^{x-1}=\frac{1-xe^{x-1}}x.$$" "\n"
        r"令 $h\left(x\right)=1-xe^{x-1}$（$x>0$），则" "\n"
        r"$$h'\left(x\right)=-e^{x-1}-xe^{x-1}=-\left(1+x\right)e^{x-1}<0,$$" "\n"
        r"故 $h\left(x\right)$ 在 $\left(0,+\infty\right)$ 上单调递减。又 $h\left(1\right)=1-1\times e^{0}=0$，所以" "\n"
        r"当 $0<x<1$ 时 $h\left(x\right)>0$，即 $F'\left(x\right)>0$，$F\left(x\right)$ 单调递增；" "\n"
        r"当 $x>1$ 时 $h\left(x\right)<0$，即 $F'\left(x\right)<0$，$F\left(x\right)$ 单调递减。" "\n"
        r"故 $F\left(x\right)$ 的单调递增区间为 $\left(0,1\right)$，单调递减区间为 $\left(1,+\infty\right)$。"
    ),
    'review': (
        r"① ⭐⭐ **两个交点的求法不同**：$A$ 是与 $x$ 轴交点 ⟹ 令 $f=0$；$B$ 是与 $y$ 轴交点 ⟹ 令 $x=0$。" "\n"
        r"   混淆两者会得到 $A\left(0,\cdot\right)$ 这类不存在的点（$f$ 在 $x=0$ 处无定义）。" "\n"
        r"② ⚠ **$a^{2}=1$ 要取正根**：由 $\ln a$ 知 $a>0$，故 $a=1$（不是 $\pm1$）。" "\n"
        r"③ ⚠ **$F\left(x\right)$ 中第二项是 $g\left(x-1\right)$ 不是 $g\left(x\right)$**：" "\n"
        r"   $g\left(x-1\right)=e^{x-1}$，若误写成 $e^{x}$，导数变成 $\dfrac1x-e^x$，零点就不是 $x=1$ 了。" "\n"
        r"④ ⭐ **判断 $\dfrac1x-e^{x-1}$ 的符号用 $h\left(x\right)=1-xe^{x-1}$**：" "\n"
        r"   $h$ 严格递减且 $h\left(1\right)=0$，符号一目了然 —— 比直接比较 $\dfrac1x$ 与 $e^{x-1}$ 清楚得多。" "\n"
        r"⑤ 数值复核：$x=1$ 时 $F'\left(1\right)=1-1=0$ ✓；$x=0.5$ 时 $F'=2-e^{-0.5}=2-0.6065=1.3935>0$ ✓；" "\n"
        r"   $x=2$ 时 $F'=0.5-e^{1}=0.5-2.7183=-2.2183<0$ ✓" "\n"
        r"**通法（切线平行 + 新函数单调性）**：" "\n"
        r"① 由交点坐标定出切点横坐标，导数值相等即方程；" "\n"
        r"② 代入参数后写出新函数，求导并通分；" "\n"
        r"③ 分子若是「$1-$ 单调函数」型，用该函数的单调性与特殊点（如 $x=1$）定号。"
    ),
    'difficulty': 0.62,
    'topics': ['M-T-107'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-107-V1',
}

QS = [
    T259_V1, T259_V2,
    T262_E1, T264_E1,
    T027_V3,
    T034_E1, T035_E1,
    T106_V1, T107_V1,
]
