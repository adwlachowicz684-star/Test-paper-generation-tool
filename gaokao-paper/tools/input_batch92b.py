# -*- coding: utf-8 -*-
r"""第 92 批（补充）：数列·累加 / 取倒数 / 累积法（M-T-247，4 题）

本批主体是第 87 批立体几何 12 题的**补录**（见 commit_batch92.py），
这里再补 4 道数列题，凑满 16 题。

## ★★ 4 题全部独立验算（通项回代 / 逐项对拍）

| 题 | 我的验算 | 答案 |
|---|---|---|
| M-T-247-E1 | $b_n=na_n$，$b_n=n^2+12$ ⟹ $a_n=n+\frac{12}n$；$a_1=13$ ✓；$a_2=8$、$a_3=a_4=7$、$a_5=7.4$ ⟹ 最小项 $a_3,a_4$ | **C** |
| M-T-247-V1 | $b_n=\frac{a_n}n$，$b_{n+1}-b_n=\ln\frac{n+1}n$ ⟹ $b_n=2+\ln n$，$a_n=2n+n\ln n$；$a_1=2$ ✓ | **D** |
| M-T-247-V2 | $\frac{a_n}n-\frac{a_{n-1}}{n-1}=-\frac1{2^n}$ ⟹ $\frac{a_n}n=1+\frac1{2^n}$，$a_n=n+\frac n{2^n}$；$a_1=\frac32$ ✓；$S_4=11.625<12<S_5=16.781$ | **$n+\frac n{2^n}$；$\{1,2,3,4\}$** |
| M-T-247-V3 | 同除 $a_na_{n+1}$ ⟹ $\frac1{a_{n+1}}-\frac1{a_n}=\frac1n-\frac1{n+1}$ ⟹ $\frac1{a_{10}}=\frac{19}{10}$ | **$\frac{10}{19}$** |

## 一处选项破碎的补全（M-T-247-V1 的 A 项）

原书 A 项只剩一个字符 `a`（p212 还原版第 65 行 `A. a`），无法还原原式。
相邻三项为 $2+(n-1)\ln n$、$1+n+\ln n$、$2n+n\ln n$，
按「同为 $2n+n\ln(\cdots)$ 型干扰项」的命题惯例补全为 $2n+n\ln(n-1)$，
并在 review 中标注。**答案为 D，不受影响** ✓

## 数值对拍明细（M-T-247-V2 第 (2) 问）

$S_n=\dfrac{n(n+1)}2+\displaystyle\sum_{k=1}^{n}\frac k{2^k}
=\dfrac{n(n+1)}2+2-\frac{n+2}{2^n}$

| $n$ | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| $S_n$ | $1.5$ | $4$ | $7.375$ | $11.625$ | $16.781$ |

逐项累加复核：$a_1=1.5$、$a_2=2.5$、$a_3=3.375$、$a_4=4.25$、$a_5=5.15625$
⟹ $S_1=1.5$、$S_2=4$、$S_3=7.375$、$S_4=11.625$、$S_5=16.781$ ✓ 与公式完全一致。
"""

T247_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知数列 $\{a_n\}$ 满足：$a_1=13$，$(n+1)a_{n+1}-na_n=2n+1$，$n\in\mathbb N^{*}$，" "\n"
        r"则下列说法正确的是（　　）"
    ),
    'opts': [
        ('A', r"$a_{n+1}\ge a_n$"),
        ('B', r"$a_{n+1}\le a_n$"),
        ('C', r"数列 $\{a_n\}$ 的最小项为 $a_3$ 和 $a_4$"),
        ('D', r"数列 $\{a_n\}$ 的最大项为 $a_3$ 和 $a_4$"),
    ],
    'answer': r"C",
    'analysis': (
        r"令 $b_n=na_n$，则递推化为 $b_{n+1}-b_n=2n+1$，用累加法求出 $b_n=n^2+12$，"
        r"于是 $a_n=n+\dfrac{12}n$；再作差 $a_{n+1}-a_n=\dfrac{(n-3)(n+4)}{n(n+1)}$，"
        r"由符号判断单调性，得到 $a_3=a_4$ 为最小项．"
    ),
    'solution': (
        r"令 $b_n=na_n$，则由 $(n+1)a_{n+1}-na_n=2n+1$ 得 $b_{n+1}-b_n=2n+1$，且 $b_1=a_1=13$．" "\n"
        r"当 $n\ge2$ 时，累加得" "\n"
        r"$b_n=b_1+\displaystyle\sum_{k=1}^{n-1}(2k+1)=13+2\cdot\frac{(n-1)n}{2}+(n-1)=13+n(n-1)+n-1=n^{2}+12$．" "\n"
        r"$n=1$ 时 $b_1=13=1^2+12$ 也成立，故 $b_n=n^{2}+12$，即 $a_n=\dfrac{n^{2}+12}{n}=n+\dfrac{12}{n}$．" "\n"
        r"于是 $a_{n+1}-a_n=\left(n+1+\dfrac{12}{n+1}\right)-\left(n+\dfrac{12}{n}\right)$" "\n"
        r"$=1-\dfrac{12}{n(n+1)}=\dfrac{n(n+1)-12}{n(n+1)}=\dfrac{(n-3)(n+4)}{n(n+1)}$．" "\n"
        r"$\because n\in\mathbb N^{*}$，$n(n+1)>0$、$n+4>0$，" "\n"
        r"$\therefore$ 当 $n<3$ 时 $a_{n+1}-a_n<0$；当 $n=3$ 时 $a_{4}=a_3$；当 $n>3$ 时 $a_{n+1}-a_n>0$．" "\n"
        r"即 $a_1>a_2>a_3=a_4<a_5<a_6<\cdots$，故数列 $\{a_n\}$ 的最小项为 $a_3$ 与 $a_4$，无最大项．" "\n"
        r"故选 **C**．"
    ),
    'review': (
        r"① **换元 $b_n=na_n$ 是题眼**：递推式的系数恰好是 $n+1$ 与 $n$，"
        r"换元后左端变成 $b_{n+1}-b_n$，一次累加即可 ✓✓✓" "\n"
        r"② **作差而非求导**：$a_n=n+\frac{12}n$ 是「对勾函数」型，但 $n$ 是正整数，"
        r"作差 $a_{n+1}-a_n$ 比用连续函数求导更严谨，且能直接看出 $n=3$ 处取等 ✓✓✓" "\n"
        r"③ **$a_3=a_4$ 是「相等」而非「相邻一大一小」**：这是选项 C 与 D 的分水岭，"
        r"A、B 都要求单调，被 $a_3=a_4<a_5$ 同时否定 ✓" "\n"
        r"④ 数值对拍：$a_1=13$、$a_2=8$、$a_3=7$、$a_4=7$、$a_5=7.4$、$a_6=8$ ⟹ 最小项确为 $a_3,a_4$ ✓" "\n"
        r"**⭐⭐ 通法（$(n+1)a_{n+1}-na_n=f(n)$ 型）**：" "\n"
        r"① ⭐⭐ **见到 $(n+1)a_{n+1}$ 与 $na_n$ 同现，立刻换元 $b_n=na_n$** ⟹ 化为 $b_{n+1}-b_n=f(n)$ ✓；" "\n"
        r"② ⭐⭐ **换元后先检验 $n=1$**：本题 $b_1=13$ 与公式 $n^2+12$ 一致，故通项对一切 $n$ 成立 ✓；" "\n"
        r"③ ⭐⭐ **判断离散单调性用作差**：结果若能因式分解成 $\frac{(n-a)(n+b)}{n(n+1)}$，符号一目了然 ✓；" "\n"
        r"④ ⚠ **「最小项为 $a_3$ 和 $a_4$」意味着 $a_3=a_4$**，若算出 $a_3\ne a_4$ 说明通项有误 ✓✓"
    ),
    'difficulty': 0.62,
    'topics': ['M-T-247'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-247-E1',
}

T247_V1 = {
    'type': '选择',
    'stem_text': (
        r"在数列 $\{a_n\}$ 中，$a_1=2$，$\dfrac{a_{n+1}}{n+1}=\dfrac{a_n}{n}+\ln\left(1+\dfrac1n\right)$，" "\n"
        r"则 $a_n=$（　　）"
    ),
    'opts': [
        ('A', r"$a_n=2n+n\ln(n-1)$"),
        ('B', r"$a_n=2+(n-1)\ln n$"),
        ('C', r"$a_n=1+n+\ln n$"),
        ('D', r"$a_n=2n+n\ln n$"),
    ],
    'answer': r"D",
    'analysis': (
        r"令 $b_n=\dfrac{a_n}n$，则 $b_{n+1}-b_n=\ln\dfrac{n+1}n$；累加时对数相加化为真数相乘，"
        r"连锁约去后只剩 $\ln n$，故 $b_n=2+\ln n$．"
    ),
    'solution': (
        r"令 $b_n=\dfrac{a_n}{n}$，则由 $\dfrac{a_{n+1}}{n+1}=\dfrac{a_n}{n}+\ln\left(1+\dfrac1n\right)$ 得" "\n"
        r"$b_{n+1}-b_n=\ln\dfrac{n+1}{n}$，且 $b_1=\dfrac{a_1}{1}=2$．" "\n"
        r"当 $n\ge2$ 时，累加得" "\n"
        r"$b_n=b_1+\displaystyle\sum_{k=1}^{n-1}\ln\frac{k+1}{k}$" "\n"
        r"$=2+\ln\left(\frac21\cdot\frac32\cdot\frac43\cdots\frac n{n-1}\right)=2+\ln n$．" "\n"
        r"$n=1$ 时 $b_1=2=2+\ln1$ 也成立，故 $b_n=2+\ln n$，" "\n"
        r"$\therefore a_n=n\,b_n=n(2+\ln n)=2n+n\ln n$．故选 **D**．"
    ),
    'review': (
        r"① **换元 $b_n=\frac{a_n}n$ 是题眼**：递推式两端都是「$a$ 除以自己的下标」的形式，"
        r"换元后立刻变成 $b_{n+1}-b_n=\ln\frac{n+1}n$ 的累加模型 ✓✓✓" "\n"
        r"② **对数累加用「真数相乘」**：$\sum\ln\frac{k+1}k=\ln\prod\frac{k+1}k$，"
        r"连锁约去后只剩 $\ln n$ —— 这是本题唯一的计算难点 ✓✓✓" "\n"
        r"③ **检验 $n=1$**：$a_1=2\cdot1+1\cdot\ln1=2$ ✓ 与题设吻合；"
        r"干扰项 B 给 $a_1=2$ 也成立，必须再验 $n=2$："
        r"$a_2=4+2\ln2=5.386$，而 B 给 $2+\ln2=2.693$ ✗ ✓" "\n"
        r"④ **⚠ 原书 A 项破碎**：还原版仅剩字符 `a`，此处按相邻干扰项的结构惯例补全为"
        r"$2n+n\ln(n-1)$（同为 $2n+n\ln(\cdots)$ 型）。**答案 D 不受影响** ✓" "\n"
        r"**⭐⭐ 通法（$\frac{a_{n+1}}{n+1}=\frac{a_n}{n}+g(n)$ 型）**：" "\n"
        r"① ⭐⭐ **换元 $b_n=\frac{a_n}n$ 后累加**，若 $g(n)=\ln\frac{n+1}n$ 则用真数相乘 telescoping ✓；" "\n"
        r"② ⭐⭐ **对数 telescoping 的通用式**：$\sum_{k=1}^{n-1}\ln\frac{k+1}k=\ln n$，"
        r"$\sum_{k=2}^{n}\ln\frac{k-1}k=-\ln n$，符号由分子分母大小决定 ✓；" "\n"
        r"③ ⭐⭐ **换元后别忘了乘回 $n$**：$a_n=n\,b_n$，漏乘 $n$ 正落入干扰项 B ✓✓；" "\n"
        r"④ ⚠ **$\ln1=0$ 使 $n=1$ 成为天然检验点**，先用它排除，再验 $n=2$ ✓"
    ),
    'difficulty': 0.60,
    'topics': ['M-T-247'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-247-V1',
}

T247_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知数列 $\{a_n\}$ 满足 $a_1=\dfrac32$，$a_n=\dfrac n{n-1}a_{n-1}-\dfrac n{2^{n}}$（$n\ge2$）．" "\n"
        r"(1) 求数列 $\{a_n\}$ 的通项公式；" "\n"
        r"(2) 设数列 $\{a_n\}$ 的前 $n$ 项和为 $S_n$，求满足 $S_n<12$ 的所有正整数 $n$ 的取值集合．"
    ),
    'opts': [],
    'answer': (
        r"(1) $a_n=n+\dfrac n{2^{n}}$；" "\n"
        r"(2) $\{1,2,3,4\}$"
    ),
    'analysis': (
        r"(1) 两边同除以 $n$，得 $\dfrac{a_n}n-\dfrac{a_{n-1}}{n-1}=-\dfrac1{2^{n}}$，"
        r"累加时右端是等比数列求和；(2) $S_n$ 分成等差数列部分与「等差×等比」部分，"
        r"后者用错位相减，最后逐项检验 $S_n<12$．"
    ),
    'solution': (
        r"**(1)** 由 $a_n=\dfrac n{n-1}a_{n-1}-\dfrac n{2^{n}}$（$n\ge2$），两边同除以 $n$ 得" "\n"
        r"$\dfrac{a_n}{n}-\dfrac{a_{n-1}}{n-1}=-\dfrac1{2^{n}}$．" "\n"
        r"累加（$n\ge2$）：" "\n"
        r"$\dfrac{a_n}n-\dfrac{a_1}1=-\left(\dfrac1{2^{2}}+\dfrac1{2^{3}}+\cdots+\dfrac1{2^{n}}\right)$" "\n"
        r"$=-\dfrac{\frac14\left[1-\left(\frac12\right)^{n-1}\right]}{1-\frac12}=\dfrac1{2^{n}}-\dfrac12$．" "\n"
        r"$\because\dfrac{a_1}1=\dfrac32$，$\therefore\dfrac{a_n}n=\dfrac32+\dfrac1{2^{n}}-\dfrac12=1+\dfrac1{2^{n}}$，" "\n"
        r"$\therefore a_n=n+\dfrac n{2^{n}}$．当 $n=1$ 时 $a_1=1+\dfrac12=\dfrac32$ 也成立，" "\n"
        r"故 $a_n=n+\dfrac n{2^{n}}$（$n\in\mathbb N^{*}$）．" "\n"
        r"**(2)** $S_n=\displaystyle\sum_{k=1}^{n}k+\sum_{k=1}^{n}\frac k{2^{k}}=\frac{n(n+1)}2+T_n$，其中 $T_n=\sum_{k=1}^{n}\dfrac k{2^{k}}$．" "\n"
        r"错位相减：$\dfrac12T_n=\sum\limits_{k=1}^{n}\dfrac k{2^{k+1}}=\dfrac1{2^{2}}+\dfrac2{2^{3}}+\cdots+\dfrac n{2^{n+1}}$，" "\n"
        r"$T_n-\dfrac12T_n=\dfrac12+\dfrac1{2^{2}}+\dfrac1{2^{3}}+\cdots+\dfrac1{2^{n}}-\dfrac n{2^{n+1}}$" "\n"
        r"$=\dfrac{\frac12\left[1-\left(\frac12\right)^{n}\right]}{1-\frac12}-\dfrac n{2^{n+1}}=1-\dfrac1{2^{n}}-\dfrac n{2^{n+1}}$，" "\n"
        r"$\therefore T_n=2-\dfrac2{2^{n}}-\dfrac n{2^{n}}=2-\dfrac{n+2}{2^{n}}$．" "\n"
        r"$\therefore S_n=\dfrac{n(n+1)}2+2-\dfrac{n+2}{2^{n}}$．" "\n"
        r"逐项检验：$S_1=\dfrac32$，$S_2=3+2-\dfrac44=4$，$S_3=6+2-\dfrac58=\dfrac{59}8=7.375$，" "\n"
        r"$S_4=10+2-\dfrac6{16}=\dfrac{93}8=11.625<12$，$S_5=15+2-\dfrac7{32}=16.78>12$．" "\n"
        r"又 $S_n$ 随 $n$ 递增（$S_{n+1}-S_n=a_{n+1}>0$），故满足 $S_n<12$ 的正整数 $n$ 的集合为 $\{1,2,3,4\}$．"
    ),
    'review': (
        r"① **同除以 $n$ 是题眼**：递推式系数是 $\frac n{n-1}$，"
        r"同除以 $n$ 后左端变成 $\frac{a_n}n-\frac{a_{n-1}}{n-1}$ 的标准累加形式 ✓✓✓" "\n"
        r"② **累加右端是等比数列**：$-\sum_{k=2}^n\frac1{2^k}=\frac1{2^n}-\frac12$（注意从 $k=2$ 起，"
        r"首项 $\frac14$），算错首项会全盘皆错 ✓✓" "\n"
        r"③ **$S_n$ 拆成两部分**：$\sum k$ 是等差、$\sum\frac k{2^k}$ 是「等差×等比」用错位相减，"
        r"结果 $T_n=2-\frac{n+2}{2^n}$ 可用 $n=1$ 检验：$T_1=\frac12=2-\frac32$ ✓" "\n"
        r"④ **单调性保证只需找到临界点**：$a_n>0$ ⟹ $S_n$ 严格递增 ⟹ 找到第一个 $S_n\ge12$ 即可收手 ✓" "\n"
        r"⑤ 数值对拍（逐项累加）：$a_1=1.5$、$a_2=2.5$、$a_3=3.375$、$a_4=4.25$、$a_5=5.15625$" "\n"
        r"⟹ $S_1=1.5$、$S_2=4$、$S_3=7.375$、$S_4=11.625$、$S_5=16.781$ ✓ **与公式完全一致**" "\n"
        r"**⭐⭐ 通法（$a_n=\frac n{n-1}a_{n-1}+f(n)$ 型）**：" "\n"
        r"① ⭐⭐ **同除以 $n$ 换元 $b_n=\frac{a_n}n$**，化为 $b_n-b_{n-1}=\frac{f(n)}n$ 再累加 ✓；" "\n"
        r"② ⭐⭐ **累加下标从 $2$ 起**（因递推对 $n\ge2$ 成立），最后单独验证 $n=1$ ✓；" "\n"
        r"③ ⭐⭐ **$\sum\frac k{2^k}=2-\frac{n+2}{2^n}$** 是「等差×等比」的标准结果，可直接记 ✓；" "\n"
        r"④ ⚠ **错位相减时两式右端要错一位对齐**，相减后中间项构成等比数列，$n$ 那一项单独留 ✓✓"
    ),
    'difficulty': 0.68,
    'topics': ['M-T-247'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-247-V2',
}

T247_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知数列 $\{a_n\}$ 满足 $a_1=1$，$a_n-a_{n+1}=\dfrac{a_na_{n+1}}{n(n+1)}$（$n\in\mathbb N^{*}$），" "\n"
        r"则 $a_{10}$ 的值是（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac23$"),
        ('B', r"$\dfrac12$"),
        ('C', r"$\dfrac{10}{19}$"),
        ('D', r"$\dfrac52$"),
    ],
    'answer': r"C",
    'analysis': (
        r"两边同除以 $a_na_{n+1}$，得 $\dfrac1{a_{n+1}}-\dfrac1{a_n}=\dfrac1{n(n+1)}=\dfrac1n-\dfrac1{n+1}$，"
        r"对 $\left\{\dfrac1{a_n}\right\}$ 累加即得．"
    ),
    'solution': (
        r"由 $a_n-a_{n+1}=\dfrac{a_na_{n+1}}{n(n+1)}$，两边同除以 $a_na_{n+1}$ 得" "\n"
        r"$\dfrac1{a_{n+1}}-\dfrac1{a_n}=\dfrac1{n(n+1)}=\dfrac1n-\dfrac1{n+1}$．" "\n"
        r"累加（$n$ 从 $1$ 到 $9$）：" "\n"
        r"$\dfrac1{a_{10}}-\dfrac1{a_1}=\left(1-\dfrac12\right)+\left(\dfrac12-\dfrac13\right)+\cdots+\left(\dfrac19-\dfrac1{10}\right)=1-\dfrac1{10}=\dfrac9{10}$．" "\n"
        r"$\because a_1=1$，$\therefore\dfrac1{a_{10}}=1+\dfrac9{10}=\dfrac{19}{10}$，" "\n"
        r"$\therefore a_{10}=\dfrac{10}{19}$．故选 **C**．"
    ),
    'review': (
        r"① **同除以 $a_na_{n+1}$ 是题眼**：凡是「差 = 积 × 分式」，"
        r"同除以这个积就能把左端变成 $\frac1{a_{n+1}}-\frac1{a_n}$ ✓✓✓" "\n"
        r"② **右端 $\frac1{n(n+1)}$ 必须裂项**：$=\frac1n-\frac1{n+1}$，累加后 telescoping 只剩首末 ✓✓✓" "\n"
        r"③ **下标边界**：求 $a_{10}$ 要累加 $n=1$ 到 $9$（共 $9$ 项），"
        r"结果为 $1-\frac1{10}$；若累加到 $n=10$ 会得 $\frac1{a_{11}}$ ✗ ✓" "\n"
        r"④ 数值对拍：$a_1=1$，$a_2$ 由 $1-a_2=\frac{a_2}2$ 得 $a_2=\frac23$，"
        r"而公式 $\frac1{a_2}=1+(\frac11-\frac12)=\frac32$ ⟹ $a_2=\frac23$ ✓ **与递推直接求解一致**" "\n"
        r"**⭐⭐ 通法（$a_n-a_{n+1}=ka_na_{n+1}$ 型）**：" "\n"
        r"① ⭐⭐ **同除以 $a_na_{n+1}$** ⟹ $\frac1{a_{n+1}}-\frac1{a_n}=k$，"
        r"即 $\left\{\frac1{a_n}\right\}$ 是等差数列（$k$ 为常数时）✓；" "\n"
        r"② ⭐⭐ **$k$ 含 $n$ 时（如本题 $\frac1{n(n+1)}$）先裂项再累加**，不要硬算 ✓；" "\n"
        r"③ ⭐⭐ **累加的项数 = 目标下标 $-1$**，求 $a_m$ 累加 $n=1$ 到 $m-1$ ✓；" "\n"
        r"④ ⚠ **最后要取倒数还原**：算出的是 $\frac1{a_m}$，别把 $\frac{19}{10}$ 当成答案 ✓✓"
    ),
    'difficulty': 0.58,
    'topics': ['M-T-247'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-247-V3',
}

QS = [T247_E1, T247_V1, T247_V2, T247_V3]
