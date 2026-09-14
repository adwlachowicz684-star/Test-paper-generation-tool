# -*- coding: utf-8 -*-
r"""第 125 批：数列求和/通项 12 + 基本不等式 1，共 13 题。

    python3 tools/run_batch.py 125

## 选题依据

pick_batch.py 的 pages 定位在本批**全部失败**（28 题 0 成功），原因是剩余题的题干提取
普遍缺根号、数字粘连，与还原版对不上。改用「滑动窗口投票」重新定位（题干多个 8 字片段
分别搜索、按命中页数投票），成功定位 24 题，其中 **p216–p230 是唯一成片的数列区**（约 14 题），
本批取其中详解完整的 12 题，外加 p230 的 M-T-009-V1（同页，边际成本近零）。

跳过：M-T-261-E2、M-T-262-V1（题干只剩「(1)(2)」问句，前置条件在上一页且已录）；
M-T-138-V3、M-T-141-V2、M-T-150-V2、M-T-177-V3、M-T-186-E1、M-T-234-E1、M-T-292-E1、
M-T-309-E1、M-T-313-V1、M-T-316-V2、M-T-332-V3、M-T-353-V2、M-T-366-V2（分散在别的页，
本批按 pages 策略不跨页）。

## ★★ 本批最值钱的一条：$a_n=\sqrt{S_n}+\sqrt{S_{n-1}}$ 要「两式相除」（M-T-263-V1）

题面被 OCR 成「$a_n=S_n+S_{n-1}$」，丢了根号。按无根号版 $\sqrt{S_n}$ 根本不会出现，
且答案 $S_n=n^2$ 无从推出。还原后：

$$a_n=S_n-S_{n-1}\quad①,\qquad a_n=\sqrt{S_n}+\sqrt{S_{n-1}}\quad②$$

**①÷② 即得 $\sqrt{S_n}-\sqrt{S_{n-1}}=1$** —— 平方差公式除以和，差就出来了。

> ⭐⭐ 判据：只要 $a_n$ 同时被表示成「差」与「和」两种形式，**相除**就是标准动作。
> $\dfrac{S_n-S_{n-1}}{\sqrt{S_n}+\sqrt{S_{n-1}}}$ 的分子恰好是平方差，一步消掉整个分子。

## ★★ 第二条：从答案反推被 OCR 吃掉的根号（M-T-272-E1）

$b_n$ 被提取成 $\dfrac1{a_na_{n+1}+a_{n+1}a_n}$（分母两项相同，显然失真）。
由答案「使 $T_n>\frac9{20}$ 的最小正整数 $n=50$」反推：

$$\frac12\Bigl(1-\frac1{\sqrt{2n+1}}\Bigr)>\frac9{20}\Rightarrow\sqrt{2n+1}>10\Rightarrow n>49.5\Rightarrow n\ge50$$

若不含根号（如 $\frac12(1-\frac1{2n+1})$）只会得 $n\ge5$。故原式必为

$$b_n=\frac{1}{\sqrt{a_na_{n+1}}\bigl(\sqrt{a_n}+\sqrt{a_{n+1}}\bigr)}
=\frac12\Bigl(\frac1{\sqrt{a_n}}-\frac1{\sqrt{a_{n+1}}}\Bigr)$$

> ⭐⭐ **「答案里的临界值是 50 而不是 5」就是根号存在的铁证。**

## ★★ 第三条：$c_n$ 的裂项靠「待定系数 + 端点」（M-T-271-V1 第 3 问）

$c_n=\dfrac{(-1)^n(n^2+4n+2)}{n(n+1)2^{n+1}}$，先作部分分式

$$\frac{n^2+4n+2}{n(n+1)}=1+\frac2n+\frac1{n+1}$$

再凑 $d_n=\dfrac{(-1)^n(n+3)}{3n\cdot2^n}$，可验证 $c_n=d_n-d_{n+1}$，
于是 $T_n=d_1-d_{n+1}=\dfrac{(-1)^1\cdot4}{3\cdot1\cdot2}-\dfrac{(-1)^{n+1}(n+4)}{3(n+1)2^{n+1}}$。

> ⭐⭐ 含 $(-1)^n$ 的裂项，**先猜 $d_n=\dfrac{(-1)^n(An+B)}{Cn\cdot2^n}$ 再定系数**，
> 比逐项配凑快得多。

## 其余可复用结论（已写入 51-insights.md）

- **M-T-257-V3**：$2a_na_{n+1}=4S_n-3$ 型，作差后 $a_{n+1}$ 是公因子，由 $a_n\ne0$ 约去 ⟹ **隔项等差**
- **M-T-264-V1**：$a_{n+1}-a_n=3\cdot4^n$ 累加法；$b_n=n+a_n$ 分组求和
- **M-T-267-V1**：$a_{n+1}=2+S_n$ ⟹ 作差得 $a_{n+1}=2a_n$（$n\ge2$），**「是等比数列」反推 $a_1$**
- **M-T-268-E1**：$3b_{n+2}-4b_{n+1}+b_n=0$ ⟹ 特征根 $1,\frac13$ ⟹ $\{b_{n+1}-b_n\}$ 等比
- **M-T-269-V1**：$(S_n-1)^2=a_nS_n$ ⟹ $S_n=\dfrac1{2-S_{n-1}}$ ⟹ 归纳得 $S_n=\dfrac n{n+1}$
- **M-T-271-E1**：$b_n=(-1)^n\Bigl(\dfrac1{2^n+1}+\dfrac1{2^{n+1}+1}\Bigr)$ 是**错一位相消**，只剩首末
- **M-T-272-V2**：三选一统一得 $q=2$；$b_n=\dfrac{2^n}{\sqrt{a_n-1}+\sqrt{a_{n+1}-1}}$ 有理化后分母 $2^n$ 恰好约掉
- **M-T-273-E1**：$a_{n+1}=\dfrac{a_n}{1+a_n}$ ⟹ 取倒数成等差；三项积裂项 $\dfrac1{k(k+1)(k+2)}$ 型
- **M-T-275-E1**：$S_n=\dfrac{n-1}{n+1}a_{n+1}+2$ ⟹ 作差得 $\dfrac{a_{n+1}}{n+1}=2\cdot\dfrac{a_n}n$
- **M-T-009-V1**：$2a+3b$ 与 $\dfrac2a+\dfrac3b=1$ **系数对齐**才好用「1」的代换
"""

# ---------------------------------------------------------------- M-T-257-V3
T257_V3 = {
    'type': '解答',
    'stem_text': (
        r"已知数列 $\{a_n\}$ 的前 $n$ 项和为 $S_n$，$a_n\ne0$，$a_1=1$，且 $2a_na_{n+1}=4S_n-3$（$n\in\mathbb N^*$）．" "\n"
        r"（1）求 $a_2$ 的值并证明：$a_{n+2}-a_n=2$；" "\n"
        r"（2）求数列 $\{a_n\}$ 的通项公式．"
    ),
    'answer': r"（1）$a_2=\dfrac12$，证明见解析；（2）$a_n=\begin{cases}n,&n\text{为奇数}\\[2pt]n-\dfrac32,&n\text{为偶数}\end{cases}$",
    'analysis': (
        r"（1）令 $n=1$ 求出 $a_2$，再把 $n$ 换成 $n+1$ 作差，约去非零公因子 $a_{n+1}$；"
        r"（2）由 $a_{n+2}-a_n=2$ 知奇数项、偶数项各自成等差数列，分别求之．"
    ),
    'solution': (
        r"**（1）** 在 $2a_na_{n+1}=4S_n-3$ 中令 $n=1$，得 $2a_1a_2=4S_1-3=4a_1-3$，" "\n"
        r"又 $a_1=1$，所以 $2a_2=1$，即 $a_2=\dfrac12$．" "\n"
        r"由已知 $2a_na_{n+1}=4S_n-3$　①，$2a_{n+1}a_{n+2}=4S_{n+1}-3$　②，" "\n"
        r"②$-$① 得 $2a_{n+1}a_{n+2}-2a_na_{n+1}=4(S_{n+1}-S_n)=4a_{n+1}$，" "\n"
        r"即 $2a_{n+1}(a_{n+2}-a_n)=4a_{n+1}$．" "\n"
        r"因为 $a_{n+1}\ne0$，两边同除以 $2a_{n+1}$ 得 $a_{n+2}-a_n=2$．" "\n"
        r"**（2）** 由（1）知，数列 $a_1,a_3,a_5,\cdots$ 是以 $a_1=1$ 为首项、$2$ 为公差的等差数列，" "\n"
        r"故 $a_{2k-1}=1+2(k-1)=2k-1$，即 $n$ 为奇数时 $a_n=n$；" "\n"
        r"数列 $a_2,a_4,a_6,\cdots$ 是以 $a_2=\dfrac12$ 为首项、$2$ 为公差的等差数列，" "\n"
        r"故 $a_{2k}=\dfrac12+2(k-1)=2k-\dfrac32$，即 $n$ 为偶数时 $a_n=n-\dfrac32$．" "\n"
        r"综上，$a_n=\begin{cases}n,&n\text{为奇数}\\[2pt]n-\dfrac32,&n\text{为偶数}\end{cases}$"
    ),
    'review': (
        r"① ⭐⭐ **作差后 $a_{n+1}$ 是公因子**：$2a_{n+1}a_{n+2}-2a_na_{n+1}=2a_{n+1}(a_{n+2}-a_n)$，" "\n"
        r"题目给的 $a_n\ne0$ **就是为放行这一步的约分而设**，不是可有可无的条件" "\n"
        r"② ⭐⭐ **隔项等差必须分成奇偶两支**，且 $a_2$ 要单独用 $n=1$ 求（$n=1$ 时 $S_1=a_1$）" "\n"
        r"③ 数值复核：$a_1=1,\ a_2=0.5,\ a_3=3,\ a_4=2.5,\ a_5=5$；" "\n"
        r"$2a_1a_2=1$ 而 $4S_1-3=1$ ✓；$2a_2a_3=3$ 而 $4S_2-3=4\times1.5-3=3$ ✓；" "\n"
        r"$2a_3a_4=15$ 而 $4S_3-3=4\times4.5-3=15$ ✓"
    ),
    'difficulty': 0.7,
    'topics': ['M-T-257'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-257-V3',
}

# ---------------------------------------------------------------- M-T-263-V1
T263_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知数列 $\{a_n\}$ 中，$a_1=1$，$a_n>0$，前 $n$ 项和为 $S_n$，若 $a_n=\sqrt{S_n}+\sqrt{S_{n-1}}$（$n\in\mathbb N^*$，且 $n\ge2$）．" "\n"
        r"（1）求数列 $\{a_n\}$ 的通项公式；" "\n"
        r"（2）记 $c_n=\dfrac{3-a_n}{2^{n+1}}$，求数列 $\{c_n\}$ 的前 $n$ 项和 $T_n$．"
    ),
    'answer': r"（1）$a_n=2n-1$；（2）$T_n=\dfrac n{2^n}$",
    'analysis': (
        r"（1）把 $a_n$ 的两种表示相除，得 $\sqrt{S_n}-\sqrt{S_{n-1}}=1$，进而 $S_n=n^2$；"
        r"（2）$c_n=\dfrac{2-n}{2^n}$ 是「等差$\div$等比」型，用错位相减法．"
    ),
    'solution': (
        r"**（1）** 当 $n\ge2$ 时，$a_n=S_n-S_{n-1}$　①，又 $a_n=\sqrt{S_n}+\sqrt{S_{n-1}}$　②，" "\n"
        r"①$\div$② 得 $\dfrac{S_n-S_{n-1}}{\sqrt{S_n}+\sqrt{S_{n-1}}}=1$，即 $\sqrt{S_n}-\sqrt{S_{n-1}}=1$（$n\ge2$）．" "\n"
        r"所以数列 $\{\sqrt{S_n}\}$ 是以 $\sqrt{S_1}=\sqrt{a_1}=1$ 为首项、$1$ 为公差的等差数列，" "\n"
        r"故 $\sqrt{S_n}=n$，即 $S_n=n^2$．" "\n"
        r"于是当 $n\ge2$ 时 $a_n=S_n-S_{n-1}=n^2-(n-1)^2=2n-1$，$n=1$ 时 $a_1=1$ 也符合，" "\n"
        r"所以 $a_n=2n-1$（$n\in\mathbb N^*$）．" "\n"
        r"**（2）** 由（1）得 $c_n=\dfrac{3-(2n-1)}{2^{n+1}}=\dfrac{4-2n}{2^{n+1}}=\dfrac{2-n}{2^n}$．" "\n"
        r"$T_n=\dfrac12+\dfrac0{2^2}+\dfrac{-1}{2^3}+\cdots+\dfrac{2-n}{2^n}$　③，" "\n"
        r"$\dfrac12T_n=\dfrac1{2^2}+\dfrac0{2^3}+\dfrac{-1}{2^4}+\cdots+\dfrac{3-n}{2^n}+\dfrac{2-n}{2^{n+1}}$　④，" "\n"
        r"③$-$④ 得 $\dfrac12T_n=\dfrac12-\left(\dfrac1{2^2}+\dfrac1{2^3}+\cdots+\dfrac1{2^n}\right)-\dfrac{2-n}{2^{n+1}}$" "\n"
        r"$=\dfrac12-\dfrac12\left(1-\dfrac1{2^{n-1}}\right)-\dfrac{2-n}{2^{n+1}}=\dfrac1{2^n}-\dfrac{2-n}{2^{n+1}}=\dfrac{2-(2-n)}{2^{n+1}}=\dfrac n{2^{n+1}}$，" "\n"
        r"所以 $T_n=\dfrac n{2^n}$．"
    ),
    'review': (
        r"① ⭐⭐ **题面根号的还原依据**：原文被 OCR 成「$a_n=S_n+S_{n-1}$」，" "\n"
        r"按无根号版无法出现 $\sqrt{S_n}$，也推不出答案 $S_n=n^2$ 与 $a_n=2n-1$；" "\n"
        r"补上根号后 ①$\div$② 一步得 $\sqrt{S_n}-\sqrt{S_{n-1}}=1$，**答案 $T_n=\frac n{2^n}$ 完全吻合**" "\n"
        r"② ⭐⭐ **「$a_n$ 有两种表示就相除」**是固定套路：分子 $S_n-S_{n-1}$ 恰是平方差，" "\n"
        r"除以 $\sqrt{S_n}+\sqrt{S_{n-1}}$ 后整个分子消掉，只剩差" "\n"
        r"③ ⭐⭐ 错位相减的中间段：③$-$④ 后从第 2 项起每项都是 $-\dfrac1{2^k}$（$k=2,\cdots,n$），" "\n"
        r"构成**纯等比**，而首项 $\dfrac12$ 不属于它 —— 结果恒形如「常数 $-\dfrac{\text{一次式}}{2^n}$」" "\n"
        r"④ 数值复核：$n=1$ 时 $T_1=c_1=\frac12$ 与 $\frac1{2^1}$ 同；$n=3$ 时" "\n"
        r"$T_3=\frac12+0-\frac18=\frac38$ 与 $\frac3{2^3}=\frac38$ 一致 ✓"
    ),
    'difficulty': 0.68,
    'topics': ['M-T-263'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-263-V1',
}

# ---------------------------------------------------------------- M-T-264-V1
T264_V1 = {
    'type': '解答',
    'stem_text': (
        r"设数列 $\{a_n\}$ 满足 $a_1=2$，$a_{n+1}-a_n=3\cdot4^n$（$n\in\mathbb N^*$）；" "\n"
        r"（1）求数列 $\{a_n\}$ 的通项公式；" "\n"
        r"（2）令 $b_n=n+a_n$，求数列 $\{b_n\}$ 的前 $n$ 项和 $S_n$．"
    ),
    'answer': r"（1）$a_n=4^n-2$；（2）$S_n=\dfrac{n^2-3n}2+\dfrac43\bigl(4^n-1\bigr)$",
    'analysis': (
        r"（1）$a_{n+1}-a_n$ 是等比数列 ⟹ 累加法；"
        r"（2）$b_n$ 是「等差 $+$ 等比」，用分组求和．"
    ),
    'solution': (
        r"**（1）** 由 $a_{n+1}-a_n=3\cdot4^n$，当 $n\ge2$ 时累加得" "\n"
        r"$a_n-a_1=3\left(4^1+4^2+\cdots+4^{n-1}\right)=3\cdot\dfrac{4\left(4^{n-1}-1\right)}{4-1}=4\left(4^{n-1}-1\right)=4^n-4$，" "\n"
        r"所以 $a_n=2+4^n-4=4^n-2$（$n\ge2$）；$n=1$ 时 $a_1=4-2=2$ 也成立，" "\n"
        r"故 $a_n=4^n-2$（$n\in\mathbb N^*$）．" "\n"
        r"**（2）** $b_n=n+a_n=n+4^n-2$，" "\n"
        r"$S_n=(1+2+\cdots+n)+\left(4^1+4^2+\cdots+4^n\right)-2n$" "\n"
        r"$=\dfrac{n(n+1)}2+\dfrac{4\left(4^n-1\right)}3-2n=\dfrac{n^2+n-4n}2+\dfrac43\left(4^n-1\right)$" "\n"
        r"$=\dfrac{n^2-3n}2+\dfrac43\left(4^n-1\right)$．"
    ),
    'review': (
        r"① ⭐⭐ **累加的上限是 $n-1$ 不是 $n$**：求 $a_n$ 时累加 $k=1$ 到 $n-1$，共 $n-1$ 项" "\n"
        r"② ⭐⭐ 等比数列求和 $\sum_{k=1}^{n-1}3\cdot4^k=3\cdot\dfrac{4(4^{n-1}-1)}{3}$，" "\n"
        r"**系数 $3$ 与分母的 $3$ 恰好约掉** —— 这是本题数字设计的结果，可当自检信号" "\n"
        r"③ ⭐⭐ 分组求和时 $-2n$ 要与等差数列部分合并：$\dfrac{n(n+1)}2-2n=\dfrac{n^2-3n}2$" "\n"
        r"④ 数值复核：$n=1$ 时 $S_1=b_1=1+4-2=3$，公式给 $\dfrac{1-3}2+\dfrac43\cdot3=-1+4=3$ ✓；" "\n"
        r"$n=2$ 时 $S_2=3+(2+16-2)=19$，公式给 $\dfrac{4-6}2+\dfrac43\cdot15=-1+20=19$ ✓"
    ),
    'difficulty': 0.6,
    'topics': ['M-T-264'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-264-V1',
}

# ---------------------------------------------------------------- M-T-267-V1
T267_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知数列 $\{a_n\}$ 的前 $n$ 项和为 $S_n$，且 $a_{n+1}=2+S_n$ 对一切正整数 $n$ 恒成立．" "\n"
        r"（1）求当 $a_1$ 为何值时，数列 $\{a_n\}$ 是等比数列，并求出它的通项公式；" "\n"
        r"（2）在（1）的条件下，记数列 $b_n=\dfrac{a_n}{(a_{n+1}+1)(a_n+1)}$ 的前 $n$ 项和为 $T_n$，求 $T_n$．"
    ),
    'answer': r"（1）$a_1=2$，$a_n=2^n$；（2）$T_n=\dfrac13-\dfrac1{2^{n+1}+1}$",
    'analysis': (
        r"（1）退位作差得 $a_{n+1}=2a_n$（$n\ge2$），再由「是等比数列」要求 $a_2=2a_1$ 定出 $a_1$；"
        r"（2）分母两因子之差恰为 $2^n$，正好与分子约掉一部分 ⟹ 裂项相消．"
    ),
    'solution': (
        r"**（1）** 由 $a_{n+1}=2+S_n$，当 $n\ge2$ 时 $a_n=2+S_{n-1}$，" "\n"
        r"两式相减得 $a_{n+1}-a_n=S_n-S_{n-1}=a_n$，即 $a_{n+1}=2a_n$（$n\ge2$）．" "\n"
        r"若 $\{a_n\}$ 是等比数列，则必有 $a_2=2a_1$；" "\n"
        r"又由已知 $a_2=2+S_1=2+a_1$，所以 $2+a_1=2a_1$，解得 $a_1=2$．" "\n"
        r"此时 $a_2=4=2a_1$，故 $a_{n+1}=2a_n$ 对 $n=1$ 也成立，" "\n"
        r"$\{a_n\}$ 确为等比数列，$a_n=2\cdot2^{n-1}=2^n$．" "\n"
        r"**（2）** $b_n=\dfrac{2^n}{(2^{n+1}+1)(2^n+1)}=\dfrac{(2^{n+1}+1)-(2^n+1)}{(2^{n+1}+1)(2^n+1)}\cdot\dfrac{2^n}{2^n}$" "\n"
        r"$=\dfrac1{2^n+1}-\dfrac1{2^{n+1}+1}$，" "\n"
        r"所以 $T_n=\left(\dfrac1{2^1+1}-\dfrac1{2^2+1}\right)+\left(\dfrac1{2^2+1}-\dfrac1{2^3+1}\right)+\cdots+\left(\dfrac1{2^n+1}-\dfrac1{2^{n+1}+1}\right)$" "\n"
        r"$=\dfrac13-\dfrac1{2^{n+1}+1}$．"
    ),
    'review': (
        r"① ⭐⭐ **「求当 $a_1$ 为何值时是等比数列」要反着用条件**：" "\n"
        r"先由递推得 $a_{n+1}=2a_n$（仅 $n\ge2$），再要求 $n=1$ 时也成立，即 $a_2=2a_1$，" "\n"
        r"而 $a_2=2+a_1$，故 $a_1=2$ —— **不是先猜 $a_1$ 再验证**" "\n"
        r"② ⭐⭐ 裂项的关键：分母两因子之差 $(2^{n+1}+1)-(2^n+1)=2^n$ **恰好等于分子**，" "\n"
        r"所以 $b_n$ 直接就是「$\dfrac1{\text{小}}-\dfrac1{\text{大}}$」，系数为 $1$" "\n"
        r"③ ⚠ 首项是 $\dfrac1{2^1+1}=\dfrac13$ 而不是 $\dfrac12$ —— 末项是 $\dfrac1{2^{n+1}+1}$ 不是 $\dfrac1{2^n+1}$" "\n"
        r"④ 数值复核：$n=1$ 时 $T_1=b_1=\dfrac2{5\times3}=\dfrac2{15}$，公式给 $\dfrac13-\dfrac15=\dfrac2{15}$ ✓"
    ),
    'difficulty': 0.66,
    'topics': ['M-T-267'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-267-V1',
}

# ---------------------------------------------------------------- M-T-268-E1
T268_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知数列 $\{a_n\}$ 的前 $n$ 项和为 $S_n$，且 $S_n=n^2$（$n\in\mathbb N^*$），数列 $\{b_n\}$ 满足：$b_1=1$，$b_2=\dfrac13$，且 $3b_{n+2}-4b_{n+1}+b_n=0$（$n\in\mathbb N^*$）．" "\n"
        r"（1）求证：数列 $\{b_{n+1}-b_n\}$ 是等比数列；" "\n"
        r"（2）求数列 $\{a_n\}$，$\{b_n\}$ 的通项公式；" "\n"
        r"（3）设 $c_n=\dfrac{n+1}{a_na_{n+1}}\cdot b_{n+1}$，数列 $\{c_n\}$ 的前 $n$ 项和为 $T_n$，求证：$T_n<\dfrac14$．"
    ),
    'answer': r"（1）见解析；（2）$a_n=2n-1$，$b_n=\dfrac1{3^{n-1}}$；（3）见解析",
    'analysis': (
        r"（1）把递推式改写成 $3(b_{n+2}-b_{n+1})=b_{n+1}-b_n$；"
        r"（2）$\{b_{n+1}-b_n\}$ 等比 ⟹ 累加法求 $b_n$，$S_n$ 已知 ⟹ 退位求 $a_n$；"
        r"（3）$\dfrac{n+1}{(2n-1)(2n+1)}$ 拆成 $\dfrac14\left(\dfrac1{2n-1}-\dfrac1{2n+1}\right)$，与 $\dfrac1{3^n}$ 配对裂项．"
    ),
    'solution': (
        r"**（1）** 由 $3b_{n+2}-4b_{n+1}+b_n=0$ 得 $3b_{n+2}-3b_{n+1}=b_{n+1}-b_n$，" "\n"
        r"即 $3(b_{n+2}-b_{n+1})=b_{n+1}-b_n$，所以 $\dfrac{b_{n+2}-b_{n+1}}{b_{n+1}-b_n}=\dfrac13$．" "\n"
        r"又 $b_2-b_1=\dfrac13-1=-\dfrac23\ne0$，" "\n"
        r"故数列 $\{b_{n+1}-b_n\}$ 是以 $-\dfrac23$ 为首项、$\dfrac13$ 为公比的等比数列．" "\n"
        r"**（2）** 由（1）得 $b_{n+1}-b_n=-\dfrac23\cdot\left(\dfrac13\right)^{n-1}=-\dfrac2{3^n}$．" "\n"
        r"当 $n\ge2$ 时，$b_n=(b_n-b_{n-1})+(b_{n-1}-b_{n-2})+\cdots+(b_2-b_1)+b_1$" "\n"
        r"$=-2\left(\dfrac13+\dfrac1{3^2}+\cdots+\dfrac1{3^{n-1}}\right)+1=-2\cdot\dfrac{\frac13\left(1-\frac1{3^{n-1}}\right)}{1-\frac13}+1$" "\n"
        r"$=-\left(1-\dfrac1{3^{n-1}}\right)+1=\dfrac1{3^{n-1}}$；" "\n"
        r"$n=1$ 时 $b_1=1$ 也满足，故 $b_n=\dfrac1{3^{n-1}}$（$n\in\mathbb N^*$）．" "\n"
        r"当 $n\ge2$ 时 $a_n=S_n-S_{n-1}=n^2-(n-1)^2=2n-1$，$n=1$ 时 $a_1=S_1=1$ 也满足，" "\n"
        r"故 $a_n=2n-1$（$n\in\mathbb N^*$）．" "\n"
        r"**（3）** 由（2）得 $c_n=\dfrac{n+1}{(2n-1)(2n+1)}\cdot\dfrac1{3^n}$．" "\n"
        r"因为 $\dfrac1{2n-1}-\dfrac1{2n+1}=\dfrac2{(2n-1)(2n+1)}$，所以 $\dfrac{n+1}{(2n-1)(2n+1)}=\dfrac{n+1}2\left(\dfrac1{2n-1}-\dfrac1{2n+1}\right)$，" "\n"
        r"于是 $c_n=\dfrac14\left(\dfrac{2n+2}{2n-1}-\dfrac{2n+2}{2n+1}\right)\cdot\dfrac1{3^n}$，" "\n"
        r"更直接地，$\dfrac{n+1}{(2n-1)(2n+1)}\cdot\dfrac1{3^n}=\dfrac14\left(\dfrac1{(2n-1)3^{n-1}}-\dfrac1{(2n+1)3^n}\right)$．" "\n"
        r"（验证：$\dfrac1{(2n-1)3^{n-1}}-\dfrac1{(2n+1)3^n}=\dfrac{3(2n+1)-(2n-1)}{(2n-1)(2n+1)3^n}=\dfrac{4n+4}{(2n-1)(2n+1)3^n}$．）" "\n"
        r"故 $T_n=\dfrac14\left[\left(\dfrac1{1\cdot3^0}-\dfrac1{3\cdot3^1}\right)+\left(\dfrac1{3\cdot3^1}-\dfrac1{5\cdot3^2}\right)+\cdots+\left(\dfrac1{(2n-1)3^{n-1}}-\dfrac1{(2n+1)3^n}\right)\right]$" "\n"
        r"$=\dfrac14\left(1-\dfrac1{(2n+1)3^n}\right)=\dfrac14-\dfrac1{4(2n+1)3^n}<\dfrac14$．"
    ),
    'review': (
        r"① ⭐⭐ **二阶线性递推 $3b_{n+2}-4b_{n+1}+b_n=0$ 的特征根是 $1$ 与 $\dfrac13$**：" "\n"
        r"改写成 $3(b_{n+2}-b_{n+1})=b_{n+1}-b_n$，即 $\{b_{n+1}-b_n\}$ 是公比 $\dfrac13$ 的等比数列 ——" "\n"
        r"**「差分等比」是处理系数和为 $0$（$3-4+1=0$）的递推的标准动作**" "\n"
        r"② ⭐⭐ 得到 $b_n$ 用**累加法**而不是解方程；注意 $n=1$ 要单独检验后再合并" "\n"
        r"③ ⭐⭐ 第（3）问的配对技巧：$\dfrac1{3^n}$ 与 $\dfrac1{3^{n-1}}$ 差一个 $3$，" "\n"
        r"所以要把 $\dfrac{n+1}{(2n-1)(2n+1)}$ 先拆成 $\dfrac14\left(\dfrac{2n+2}{2n-1}-\dfrac{2n+2}{2n+1}\right)$ 再各自乘 $3$ 的幂，" "\n"
        r"写成 $\dfrac14\left(\dfrac1{(2n-1)3^{n-1}}-\dfrac1{(2n+1)3^n}\right)$ 时 $3^{n-1}$ 与 $3^n$ 正好错一位" "\n"
        r"④ 数值复核：$n=1$ 时 $c_1=\dfrac2{1\times3}\times\dfrac13=\dfrac29$，" "\n"
        r"公式给 $\dfrac14\left(1-\dfrac1{3\times3}\right)=\dfrac14\times\dfrac89=\dfrac29$ ✓"
    ),
    'difficulty': 0.74,
    'topics': ['M-T-268'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-268-E1',
}

# ---------------------------------------------------------------- M-T-269-V1
T269_V1 = {
    'type': '解答',
    'stem_text': (
        r"设数列 $\{a_n\}$ 的前 $n$ 项和为 $S_n$，且 $(S_n-1)^2=a_nS_n$（$n\in\mathbb N^*$）．" "\n"
        r"（1）求 $S_1$、$S_2$、$S_3$ 的值；" "\n"
        r"（2）求出 $S_n$ 及数列 $\{a_n\}$ 的通项公式；" "\n"
        r"（3）设 $b_n=(-1)^{n+1}(n+1)^2a_na_{n+1}$（$n\in\mathbb N^*$），求数列 $\{b_n\}$ 的前 $n$ 项和 $T_n$．"
    ),
    'answer': (
        r"（1）$S_1=\dfrac12$，$S_2=\dfrac23$，$S_3=\dfrac34$；（2）$S_n=\dfrac n{n+1}$，$a_n=\dfrac1{n(n+1)}$；" "\n"
        r"（3）$T_n=\dfrac14+\dfrac{(-1)^{n+1}}{2(n+1)(n+2)}$"
    ),
    'analysis': (
        r"（1）逐次代入 $n=1,2,3$；（2）$n\ge2$ 时把 $a_n$ 换成 $S_n-S_{n-1}$ 得 $S_n=\dfrac1{2-S_{n-1}}$，归纳出 $S_n$；"
        r"（3）$(n+1)^2$ 与 $a_na_{n+1}$ 分母中的 $(n+1)^2$ 恰好约掉，得 $b_n=\dfrac{(-1)^{n+1}}{n(n+2)}$，再裂项．"
    ),
    'solution': (
        r"**（1）** $n=1$ 时 $a_1=S_1$，代入得 $(S_1-1)^2=S_1^2$，即 $-2S_1+1=0$，$S_1=\dfrac12$．" "\n"
        r"$n=2$ 时 $(S_2-1)^2=(S_2-S_1)S_2$，即 $S_2^2-2S_2+1=S_2^2-\dfrac12S_2$，" "\n"
        r"整理得 $\dfrac32S_2=1$，$S_2=\dfrac23$．" "\n"
        r"$n=3$ 时 $(S_3-1)^2=(S_3-S_2)S_3$，即 $S_3^2-2S_3+1=S_3^2-\dfrac23S_3$，" "\n"
        r"整理得 $\dfrac43S_3=1$，$S_3=\dfrac34$．" "\n"
        r"**（2）** 当 $n\ge2$ 时，$(S_n-1)^2=(S_n-S_{n-1})S_n$，" "\n"
        r"展开得 $S_n^2-2S_n+1=S_n^2-S_{n-1}S_n$，即 $S_n(2-S_{n-1})=1$，" "\n"
        r"所以 $S_n=\dfrac1{2-S_{n-1}}$（$n\ge2$）．" "\n"
        r"由 $S_1=\dfrac12=\dfrac1{1+1}$，假设 $S_{n-1}=\dfrac{n-1}n$，则 $S_n=\dfrac1{2-\frac{n-1}n}=\dfrac n{n+1}$，" "\n"
        r"由数学归纳法 $S_n=\dfrac n{n+1}$（$n\in\mathbb N^*$）．" "\n"
        r"于是 $a_n=S_n-S_{n-1}=\dfrac n{n+1}-\dfrac{n-1}n=\dfrac{n^2-(n^2-1)}{n(n+1)}=\dfrac1{n(n+1)}$（$n\ge2$）；" "\n"
        r"$n=1$ 时 $a_1=S_1=\dfrac12=\dfrac1{1\times2}$ 也满足，故 $a_n=\dfrac1{n(n+1)}$（$n\in\mathbb N^*$）．" "\n"
        r"**（3）** $a_n=\dfrac1{n(n+1)}$，$a_{n+1}=\dfrac1{(n+1)(n+2)}$，" "\n"
        r"所以 $b_n=(-1)^{n+1}(n+1)^2\cdot\dfrac1{n(n+1)^2(n+2)}=\dfrac{(-1)^{n+1}}{n(n+2)}=\dfrac{(-1)^{n+1}}2\left(\dfrac1n-\dfrac1{n+2}\right)$．" "\n"
        r"$T_n=\dfrac12\sum_{k=1}^n(-1)^{k+1}\left(\dfrac1k-\dfrac1{k+2}\right)$．" "\n"
        r"当 $n$ 为偶数时，$T_n=\dfrac12\left[\left(1-\dfrac13\right)-\left(\dfrac12-\dfrac14\right)+\cdots+\left(\dfrac1{n-1}-\dfrac1{n+1}\right)-\left(\dfrac1n-\dfrac1{n+2}\right)\right]$" "\n"
        r"$=\dfrac12\left[\left(1-\dfrac1{n+1}\right)-\left(\dfrac12-\dfrac1{n+2}\right)\right]=\dfrac12\left(\dfrac12-\dfrac1{n+1}+\dfrac1{n+2}\right)$；" "\n"
        r"当 $n$ 为奇数时，$T_n=\dfrac12\left[\left(1-\dfrac1{n+2}\right)-\left(\dfrac12-\dfrac1{n+1}\right)\right]=\dfrac12\left(\dfrac12+\dfrac1{n+1}-\dfrac1{n+2}\right)$．" "\n"
        r"两者可统一写成 $T_n=\dfrac14+\dfrac{(-1)^{n+1}}{2(n+1)(n+2)}$．"
    ),
    'review': (
        r"① ⭐⭐ **$S_n=\dfrac1{2-S_{n-1}}$ 是本题的枢纽**：展开 $(S_n-1)^2=(S_n-S_{n-1})S_n$ 后" "\n"
        r"$S_n^2$ 项**完全抵消**，只剩一次式，一步解出 $S_n$ —— 这种「二次项抵消」是刻意设计" "\n"
        r"② ⭐⭐ **$(n+1)^2$ 与 $a_na_{n+1}$ 分母里的 $(n+1)^2$ 恰好约掉**：" "\n"
        r"$a_na_{n+1}=\dfrac1{n(n+1)^2(n+2)}$，乘 $(n+1)^2$ 后只剩 $\dfrac1{n(n+2)}$ —— 这是命题人给的暗示" "\n"
        r"③ ⭐⭐ 含 $(-1)^n$ 的裂项**必须分奇偶**，因为望远镜的两端不同：" "\n"
        r"奇数项链是 $1\to\frac13\to\frac15\to\cdots$，偶数项链是 $\frac12\to\frac14\to\frac16\to\cdots$，" "\n"
        r"末端取决于 $n$ 的奇偶" "\n"
        r"④ ⭐ 统一式 $T_n=\dfrac14+\dfrac{(-1)^{n+1}}{2(n+1)(n+2)}$ 比分段式好看得多，可作自检：" "\n"
        r"$n=1$ 给 $\dfrac14+\dfrac1{12}=\dfrac13$，$n=2$ 给 $\dfrac14-\dfrac1{24}=\dfrac5{24}$" "\n"
        r"⑤ 数值复核：$b_1=\frac13,\ b_2=-\frac18,\ b_3=\frac1{15}$；" "\n"
        r"$T_3=\frac13-\frac18+\frac1{15}=\frac{33}{120}=\frac{11}{40}$，统一式给 $\dfrac14+\dfrac1{2\times4\times5}=\dfrac{10+1}{40}=\dfrac{11}{40}$ ✓"
    ),
    'difficulty': 0.76,
    'topics': ['M-T-269'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-269-V1',
}

# ---------------------------------------------------------------- M-T-271-E1
T271_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知数列 $\{a_n\}$ 满足 $a_{n+1}-2a_n+2=0$，且 $a_1=8$．" "\n"
        r"（1）证明：数列 $\{a_n-2\}$ 为等比数列；" "\n"
        r"（2）设 $b_n=\dfrac{(-1)^na_n}{(2^n+1)(2^{n+1}+1)}$，记数列 $\{b_n\}$ 的前 $n$ 项和为 $T_n$，" "\n"
        r"若对任意的 $n\in\mathbb N^*$，$m\ge T_n$ 恒成立，求 $m$ 的取值范围．"
    ),
    'answer': r"（1）详见解析；（2）$\left[-\dfrac29,+\infty\right)$",
    'analysis': (
        r"（1）$a_{n+1}-2=2(a_n-2)$；（2）把 $a_n=3\cdot2^n+2$ 代入 $b_n$，"
        r"拆成 $(-1)^n\left(\dfrac1{2^n+1}+\dfrac1{2^{n+1}+1}\right)$，两项错一位相消，只剩首末；"
        r"$m\ge T_n$ 恒成立 ⟺ $m\ge\max T_n$．"
    ),
    'solution': (
        r"**（1）** 由 $a_{n+1}-2a_n+2=0$ 得 $a_{n+1}=2a_n-2$，即 $a_{n+1}-2=2(a_n-2)$．" "\n"
        r"又 $a_1-2=6\ne0$，故数列 $\{a_n-2\}$ 是以 $6$ 为首项、$2$ 为公比的等比数列．" "\n"
        r"**（2）** 由（1）得 $a_n-2=6\cdot2^{n-1}=3\cdot2^n$，即 $a_n=3\cdot2^n+2$．" "\n"
        r"因为 $\dfrac1{2^n+1}+\dfrac1{2^{n+1}+1}=\dfrac{2^{n+1}+1+2^n+1}{(2^n+1)(2^{n+1}+1)}=\dfrac{3\cdot2^n+2}{(2^n+1)(2^{n+1}+1)}$，" "\n"
        r"所以 $b_n=(-1)^n\left(\dfrac1{2^n+1}+\dfrac1{2^{n+1}+1}\right)$．" "\n"
        r"于是 $T_n=\sum_{k=1}^n\dfrac{(-1)^k}{2^k+1}+\sum_{k=1}^n\dfrac{(-1)^k}{2^{k+1}+1}$．" "\n"
        r"把两和式展开：$-\dfrac13+\dfrac15-\dfrac19+\cdots$ 与 $-\dfrac15+\dfrac19-\cdots$，" "\n"
        r"**中间项逐项相消**，只剩第一和式的首项 $-\dfrac13$ 与第二和式的末项 $\dfrac{(-1)^n}{2^{n+1}+1}$：" "\n"
        r"$T_n=-\dfrac13+\dfrac{(-1)^n}{2^{n+1}+1}$．" "\n"
        r"当 $n$ 为偶数时 $T_n=-\dfrac13+\dfrac1{2^{n+1}+1}$，随 $n$ 增大而递减，最大值为 $T_2=-\dfrac13+\dfrac19=-\dfrac29$；" "\n"
        r"当 $n$ 为奇数时 $T_n=-\dfrac13-\dfrac1{2^{n+1}+1}<-\dfrac13$，且随 $n$ 增大而递增趋向 $-\dfrac13$．" "\n"
        r"故 $\{T_n\}$ 的最大值为 $T_2=-\dfrac29$．" "\n"
        r"「对任意 $n\in\mathbb N^*$，$m\ge T_n$ 恒成立」等价于 $m\ge (T_n)_{\max}=-\dfrac29$，" "\n"
        r"所以 $m$ 的取值范围是 $\left[-\dfrac29,+\infty\right)$．"
    ),
    'review': (
        r"① ⭐⭐ **$b_n$ 的拆分靠分子凑**：$a_n=3\cdot2^n+2$，而" "\n"
        r"$(2^{n+1}+1)+(2^n+1)=3\cdot2^n+2$ **恰好等于分子**，" "\n"
        r"所以 $b_n=(-1)^n\left(\dfrac1{2^n+1}+\dfrac1{2^{n+1}+1}\right)$ —— 见到分子等于两分母之和，立刻拆" "\n"
        r"② ⭐⭐ **两个和式错一位相消**：$\sum\frac{(-1)^k}{2^k+1}$ 与 $\sum\frac{(-1)^k}{2^{k+1}+1}$" "\n"
        r"下标差 $1$，展开后除首末外全部抵消，这是本题最省力的写法（不必分奇偶逐项写）" "\n"
        r"③ ⚠ **恒成立取最大，不是取最小**：$m\ge T_n$ 对所有 $n$ 成立 ⟺ $m\ge\max T_n$" "\n"
        r"④ ⚠ **最大值在 $n=2$ 而非 $n=1$**：$T_1=-\dfrac13-\dfrac15=-\dfrac8{15}\approx-0.53$ 远小于 $T_2=-\dfrac29\approx-0.22$" "\n"
        r"⑤ 数值复核：$n=2$ 时 $b_1=-\dfrac{8}{3\times5}=-\dfrac8{15}$，$b_2=\dfrac{14}{5\times9}=\dfrac{14}{45}$，" "\n"
        r"$T_2=-\dfrac8{15}+\dfrac{14}{45}=\dfrac{-24+14}{45}=-\dfrac{10}{45}=-\dfrac29$ ✓ 与公式一致"
    ),
    'difficulty': 0.72,
    'topics': ['M-T-271'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-271-E1',
}

# ---------------------------------------------------------------- M-T-271-V1
T271_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知数列 $\{a_n\}$ 满足 $a_1=2$，$a_{n+1}=2a_n+2^{n+1}$．" "\n"
        r"（1）设 $b_n=\dfrac{a_n}{2^n}$，求数列 $\{b_n\}$ 的通项公式；" "\n"
        r"（2）求数列 $\{a_n\}$ 的前 $n$ 项和 $S_n$；" "\n"
        r"（3）记 $c_n=\dfrac{(-1)^n(n^2+4n+2)2^n}{a_na_{n+1}}$，求数列 $\{c_n\}$ 的前 $n$ 项和 $T_n$．"
    ),
    'answer': r"（1）$b_n=n$；（2）$S_n=(n-1)2^{n+1}+2$；（3）$T_n=-\dfrac23-\dfrac{(n+4)(-1)^{n+1}}{3(n+1)\cdot2^{n+1}}$",
    'analysis': (
        r"（1）两边同除以 $2^{n+1}$ 得 $b_{n+1}=b_n+1$；（2）$a_n=n\cdot2^n$ 是「等差$\times$等比」，错位相减；"
        r"（3）先作部分分式 $\dfrac{n^2+4n+2}{n(n+1)}=1+\dfrac2n+\dfrac1{n+1}$，再凑 $d_n=\dfrac{(-1)^n(n+3)}{3n\cdot2^n}$ 使 $c_n=d_n-d_{n+1}$．"
    ),
    'solution': (
        r"**（1）** 由 $a_{n+1}=2a_n+2^{n+1}$，两边同除以 $2^{n+1}$ 得 $\dfrac{a_{n+1}}{2^{n+1}}=\dfrac{a_n}{2^n}+1$，" "\n"
        r"即 $b_{n+1}=b_n+1$．又 $b_1=\dfrac{a_1}{2^1}=1$，故 $\{b_n\}$ 是首项为 $1$、公差为 $1$ 的等差数列，$b_n=n$．" "\n"
        r"**（2）** 由（1）得 $a_n=n\cdot2^n$．" "\n"
        r"$S_n=1\cdot2^1+2\cdot2^2+\cdots+n\cdot2^n$　①，" "\n"
        r"$2S_n=1\cdot2^2+2\cdot2^3+\cdots+n\cdot2^{n+1}$　②，" "\n"
        r"①$-$② 得 $-S_n=2^1+2^2+\cdots+2^n-n\cdot2^{n+1}=2\left(2^n-1\right)-n\cdot2^{n+1}$，" "\n"
        r"所以 $S_n=n\cdot2^{n+1}-2^{n+1}+2=(n-1)2^{n+1}+2$．" "\n"
        r"**（3）** $c_n=\dfrac{(-1)^n(n^2+4n+2)2^n}{n\cdot2^n\cdot(n+1)2^{n+1}}=\dfrac{(-1)^n(n^2+4n+2)}{n(n+1)2^{n+1}}$．" "\n"
        r"令 $d_n=\dfrac{(-1)^n(n+3)}{3n\cdot2^n}$，则" "\n"
        r"$d_n-d_{n+1}=\dfrac{(-1)^n(n+3)}{3n\cdot2^n}-\dfrac{(-1)^{n+1}(n+4)}{3(n+1)2^{n+1}}=\dfrac{(-1)^n}{3\cdot2^{n+1}}\left[\dfrac{2(n+3)}{n}+\dfrac{n+4}{n+1}\right]$" "\n"
        r"$=\dfrac{(-1)^n}{3\cdot2^{n+1}}\cdot\dfrac{2(n+3)(n+1)+n(n+4)}{n(n+1)}=\dfrac{(-1)^n}{3\cdot2^{n+1}}\cdot\dfrac{3n^2+12n+6}{n(n+1)}=\dfrac{(-1)^n(n^2+4n+2)}{n(n+1)2^{n+1}}=c_n$．" "\n"
        r"故 $T_n=\sum_{k=1}^n(d_k-d_{k+1})=d_1-d_{n+1}=\dfrac{(-1)^1\cdot4}{3\cdot1\cdot2^1}-\dfrac{(-1)^{n+1}(n+4)}{3(n+1)2^{n+1}}$" "\n"
        r"$=-\dfrac23-\dfrac{(n+4)(-1)^{n+1}}{3(n+1)\cdot2^{n+1}}$．"
    ),
    'review': (
        r"① ⭐⭐ **同除以 $2^{n+1}$ 而不是 $2^n$**：$a_{n+1}=2a_n+2^{n+1}$ 两边除以 $2^{n+1}$" "\n"
        r"才使左端正好是 $b_{n+1}$、第一项正好是 $b_n$、常数项正好是 $1$" "\n"
        r"② ⭐⭐ **含 $(-1)^n$ 的裂项用待定系数**：猜 $d_n=\dfrac{(-1)^n(An+B)}{Cn\cdot2^n}$，" "\n"
        r"由 $d_n-d_{n+1}=c_n$ 比对系数定出 $A=1,B=3,C=3$，比逐项配凑快得多" "\n"
        r"③ ⭐ 部分分式 $\dfrac{n^2+4n+2}{n(n+1)}=1+\dfrac{3n+2}{n(n+1)}=1+\dfrac2n+\dfrac1{n+1}$ 是凑 $d_n$ 的起点" "\n"
        r"④ ⚠ $d_1=\dfrac{(-1)^1\cdot4}{3\cdot1\cdot2}=-\dfrac23$ —— **这就是 $T_n$ 里的常数项 $-\dfrac23$**，" "\n"
        r"它等于「$d_n$ 在 $n=0$ 处的值」的相反数，可当自检" "\n"
        r"⑤ 数值复核：$n=1$ 时 $c_1=\dfrac{(-1)^1\cdot7\cdot2}{2\cdot8}=-\dfrac78$；" "\n"
        r"公式给 $-\dfrac23-\dfrac{5}{3\cdot2\cdot4}=-\dfrac23-\dfrac5{24}=-\dfrac{16+5}{24}=-\dfrac78$ ✓"
    ),
    'difficulty': 0.78,
    'topics': ['M-T-271'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-271-V1',
}

# ---------------------------------------------------------------- M-T-272-E1
T272_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知数列 $\{a_n\}$ 的前 $n$ 项和满足 $2S_n-na_n=n$（$n\in\mathbb N^*$），且 $a_2=3$．" "\n"
        r"（1）求证：数列 $\left\{\dfrac{a_n-1}{n-1}\right\}$（$n\ge2$）是常数数列；" "\n"
        r"（2）设 $b_n=\dfrac{1}{\sqrt{a_na_{n+1}}\bigl(\sqrt{a_n}+\sqrt{a_{n+1}}\bigr)}$，$T_n$ 为数列 $\{b_n\}$ 的前 $n$ 项和，" "\n"
        r"求使 $T_n>\dfrac9{20}$ 成立的最小正整数 $n$ 的值．"
    ),
    'answer': r"（1）证明见解析；（2）$50$",
    'analysis': (
        r"（1）把 $n$ 换成 $n+1$ 作差得 $na_n-(n-1)a_{n+1}=1$，改写为 $\dfrac{a_{n+1}-1}n=\dfrac{a_n-1}{n-1}$；"
        r"（2）由 $a_2=3$ 定出常数 $2$，得 $a_n=2n-1$，再对 $b_n$ 分母有理化后裂项．"
    ),
    'solution': (
        r"**（1）** 由 $2S_n-na_n=n$　①，把 $n$ 换成 $n+1$ 得 $2S_{n+1}-(n+1)a_{n+1}=n+1$　②．" "\n"
        r"②$-$① 得 $2a_{n+1}-(n+1)a_{n+1}+na_n=1$，即 $(1-n)a_{n+1}+na_n=1$，" "\n"
        r"整理为 $na_n-(n-1)a_{n+1}=1$，故 $(n-1)a_{n+1}=na_n-1$．" "\n"
        r"于是 $a_{n+1}-1=\dfrac{na_n-1}{n-1}-1=\dfrac{na_n-n}{n-1}=\dfrac{n(a_n-1)}{n-1}$，" "\n"
        r"即 $\dfrac{a_{n+1}-1}{n}=\dfrac{a_n-1}{n-1}$（$n\ge2$），" "\n"
        r"所以数列 $\left\{\dfrac{a_n-1}{n-1}\right\}$（$n\ge2$）是常数数列．" "\n"
        r"**（2）** 由 $a_2=3$ 得 $\dfrac{a_2-1}{2-1}=2$，故 $\dfrac{a_n-1}{n-1}=2$（$n\ge2$），即 $a_n=2n-1$（$n\ge2$）．" "\n"
        r"$n=1$ 时由 ① 得 $2S_1-a_1=1$，即 $a_1=1$，也满足 $a_n=2n-1$，故 $a_n=2n-1$（$n\in\mathbb N^*$）．" "\n"
        r"因为 $a_{n+1}-a_n=2$，对 $b_n$ 的分母有理化：" "\n"
        r"$b_n=\dfrac{\sqrt{a_{n+1}}-\sqrt{a_n}}{\sqrt{a_na_{n+1}}\bigl(\sqrt{a_n}+\sqrt{a_{n+1}}\bigr)\bigl(\sqrt{a_{n+1}}-\sqrt{a_n}\bigr)}=\dfrac{\sqrt{a_{n+1}}-\sqrt{a_n}}{2\sqrt{a_na_{n+1}}}$" "\n"
        r"$=\dfrac12\left(\dfrac1{\sqrt{a_n}}-\dfrac1{\sqrt{a_{n+1}}}\right)=\dfrac12\left(\dfrac1{\sqrt{2n-1}}-\dfrac1{\sqrt{2n+1}}\right)$．" "\n"
        r"所以 $T_n=\dfrac12\left[\left(1-\dfrac1{\sqrt3}\right)+\left(\dfrac1{\sqrt3}-\dfrac1{\sqrt5}\right)+\cdots+\left(\dfrac1{\sqrt{2n-1}}-\dfrac1{\sqrt{2n+1}}\right)\right]$" "\n"
        r"$=\dfrac12\left(1-\dfrac1{\sqrt{2n+1}}\right)$．" "\n"
        r"由 $T_n>\dfrac9{20}$ 得 $1-\dfrac1{\sqrt{2n+1}}>\dfrac9{10}$，即 $\dfrac1{\sqrt{2n+1}}<\dfrac1{10}$，" "\n"
        r"故 $\sqrt{2n+1}>10$，$2n+1>100$，$n>49.5$．又 $n\in\mathbb N^*$，所以 $n$ 的最小值为 $50$．"
    ),
    'review': (
        r"① ⭐⭐ **$b_n$ 的根号是「从答案反推」出来的**：原文被 OCR 成" "\n"
        r"$\dfrac1{a_na_{n+1}+a_{n+1}a_n}$（分母两项相同，显然失真）．" "\n"
        r"由答案「使 $T_n>\frac9{20}$ 的最小正整数 $n=50$」倒推：只有" "\n"
        r"$T_n=\frac12\left(1-\frac1{\sqrt{2n+1}}\right)$ 才给出 $\sqrt{2n+1}>10\Rightarrow n>49.5\Rightarrow n\ge50$；" "\n"
        r"若不含根号（如 $\frac12(1-\frac1{2n+1})$）只会得 $n\ge5$ —— **临界值 50 就是根号存在的铁证**" "\n"
        r"② ⭐⭐ **有理化时分子分母同乘 $(\sqrt{a_{n+1}}-\sqrt{a_n})$**，分母变成 $a_{n+1}-a_n=2$，" "\n"
        r"所以「差为常数」的数列才这么好算 —— 这是 $a_n=2n-1$ 的用意" "\n"
        r"③ ⭐⭐ 第（1）问的变形：由 $na_n-(n-1)a_{n+1}=1$ 推出 $\dfrac{a_{n+1}-1}n=\dfrac{a_n-1}{n-1}$，" "\n"
        r"关键是**两边同时减 $1$ 后凑出 $(a_n-1)$ 的公因子**" "\n"
        r"④ ⚠ $a_1=1$ 要单独由 $n=1$ 代入原式验证，不能直接用「$\frac{a_n-1}{n-1}=2$」（$n=1$ 分母为 $0$）" "\n"
        r"⑤ 数值复核：$n=50$ 时 $T_{50}=\frac12(1-\frac1{\sqrt{101}})=\frac12(1-0.09950)=0.45025>0.45$ ✓；" "\n"
        r"$n=49$ 时 $T_{49}=\frac12(1-\frac1{\sqrt{99}})=\frac12(1-0.10050)=0.44975<0.45$ ✓ —— **恰好卡在 50**"
    ),
    'difficulty': 0.75,
    'topics': ['M-T-272'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-272-E1',
}

# ---------------------------------------------------------------- M-T-272-V2
T272_V2 = {
    'type': '解答',
    'stem_text': (
        r"在①$a_2$，$a_3$，$a_4-4$ 成等差数列；②$S_1$，$S_2+2$，$S_3$ 成等差数列；③$a_{n+1}=S_n+2$ 中任选一个，" "\n"
        r"补充在下列问题中，并解答．在各项均为正数的等比数列 $\{a_n\}$ 中，前 $n$ 项和为 $S_n$，已知 $a_1=2$，且 ____ ．" "\n"
        r"（1）求数列 $\{a_n\}$ 的通项公式；" "\n"
        r"（2）数列 $\{b_n\}$ 的通项公式 $b_n=\dfrac{2^n}{\sqrt{a_n-1}+\sqrt{a_{n+1}-1}}$（$n\in\mathbb N^*$），求数列 $\{b_n\}$ 的前 $n$ 项和 $T_n$．"
    ),
    'answer': r"（1）$a_n=2^n$（三个条件均给出同一结果）；（2）$T_n=\sqrt{2^{n+1}-1}-1$",
    'analysis': (
        r"（1）设公比 $q>0$，三个条件分别给出 $q=2$；（2）代入 $a_n=2^n$ 后分母有理化，" "\n"
        r"分母之差 $(2^{n+1}-1)-(2^n-1)=2^n$ 恰与分子约掉．"
    ),
    'solution': (
        r"**（1）** 设等比数列 $\{a_n\}$ 的公比为 $q$（$q>0$），则 $a_n=2q^{n-1}$．" "\n"
        r"**选①：** $a_2$，$a_3$，$a_4-4$ 成等差数列，故 $2a_3=a_2+a_4-4$，" "\n"
        r"即 $2\cdot2q^2=2q+2q^3-4$，整理得 $2q^2=q+q^3-2$，即 $2\left(q^2+1\right)=q\left(1+q^2\right)$．" "\n"
        r"因 $q^2+1>0$，两边约去得 $q=2$，故 $a_n=2\cdot2^{n-1}=2^n$．" "\n"
        r"**选②：** $S_1$，$S_2+2$，$S_3$ 成等差数列，故 $2\left(S_2+2\right)=S_1+S_3$，" "\n"
        r"即 $2\left(a_1+a_2+2\right)=a_1+\left(a_1+a_2+a_3\right)$，整理得 $a_2+4=a_3$，" "\n"
        r"即 $2q+4=2q^2$，$q^2-q-2=0$，解得 $q=2$ 或 $q=-1$（舍），故 $a_n=2^n$．" "\n"
        r"**选③：** 由 $a_{n+1}=S_n+2$，取 $n=1$ 得 $a_2=S_1+2=a_1+2=4$，" "\n"
        r"故 $q=\dfrac{a_2}{a_1}=2$，$a_n=2^n$．" "\n"
        r"**（2）** 由（1）得 $a_n=2^n$，故 $a_n-1=2^n-1$，$a_{n+1}-1=2^{n+1}-1$．" "\n"
        r"$b_n=\dfrac{2^n}{\sqrt{2^n-1}+\sqrt{2^{n+1}-1}}$，" "\n"
        r"分母有理化：$b_n=\dfrac{2^n\left(\sqrt{2^{n+1}-1}-\sqrt{2^n-1}\right)}{\left(2^{n+1}-1\right)-\left(2^n-1\right)}=\dfrac{2^n\left(\sqrt{2^{n+1}-1}-\sqrt{2^n-1}\right)}{2^n}$" "\n"
        r"$=\sqrt{2^{n+1}-1}-\sqrt{2^n-1}$．" "\n"
        r"所以 $T_n=\left(\sqrt{2^2-1}-\sqrt{2^1-1}\right)+\left(\sqrt{2^3-1}-\sqrt{2^2-1}\right)+\cdots+\left(\sqrt{2^{n+1}-1}-\sqrt{2^n-1}\right)$" "\n"
        r"$=\sqrt{2^{n+1}-1}-\sqrt{2-1}=\sqrt{2^{n+1}-1}-1$．"
    ),
    'review': (
        r"① ⭐⭐ **有理化后分母之差恰好等于分子 $2^n$**：" "\n"
        r"$(2^{n+1}-1)-(2^n-1)=2^n$，与分子完全约掉 —— 这是本题最漂亮的一步，" "\n"
        r"也是命题人把 $b_n$ 设计成 $\dfrac{2^n}{\sqrt{\cdot}+\sqrt{\cdot}}$ 的原因" "\n"
        r"② ⭐⭐ **三选一的三种解法分别用到不同的工具**：①用通项、②用 $S_n$ 展开、③只用 $n=1$，" "\n"
        r"选③ 最省事（一步得 $a_2=4$），但①②能练到方程变形" "\n"
        r"③ ⚠ 选①时整理到 $2(q^2+1)=q(1+q^2)$ 后**不能直接约去 $(q^2+1)$ 与 $(1+q^2)$ 之外的东西**，" "\n"
        r"它们是同一个式子，约去后得 $q=2$；若误展开成三次方程会多出增根" "\n"
        r"④ ⚠ $T_n$ 的首项是 $\sqrt{2^{n+1}-1}-\sqrt{1}$，减的是 $\sqrt{2^1-1}=1$ 不是 $0$" "\n"
        r"⑤ 数值复核：$n=1$ 时 $b_1=\dfrac2{1+\sqrt3}=\dfrac{2(\sqrt3-1)}{2}=\sqrt3-1\approx0.732$，" "\n"
        r"公式给 $\sqrt3-1$ ✓；$n=2$ 时 $b_2=\dfrac4{\sqrt3+\sqrt7}=4\times\dfrac{\sqrt7-\sqrt3}{4}=\sqrt7-\sqrt3$，" "\n"
        r"$T_2=\sqrt7-1\approx1.6458$，公式给 $\sqrt{2^3-1}-1=\sqrt7-1$ ✓"
    ),
    'difficulty': 0.72,
    'topics': ['M-T-272'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-272-V2',
}

# ---------------------------------------------------------------- M-T-273-E1
T273_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知数列 $\{a_n\}$ 满足 $a_1=\dfrac12$，$a_{n+1}=\dfrac{\lambda a_n}{1+a_n^{\lambda}}$（$n\in\mathbb N^*$）．" "\n"
        r"（1）若 $\lambda=1$：" "\n"
        r"①求数列 $\{a_n\}$ 的通项公式；" "\n"
        r"②证明：对 $\forall n\in\mathbb N^*$，$a_1a_2a_3+a_2a_3a_4+\cdots+a_na_{n+1}a_{n+2}=\dfrac{n(n+5)}{12(n+2)(n+3)}$．"
    ),
    'answer': r"①$a_n=\dfrac1{n+1}$；②证明见解析",
    'analysis': (
        r"①$\lambda=1$ 时 $a_{n+1}=\dfrac{a_n}{1+a_n}$，取倒数得 $\dfrac1{a_{n+1}}=\dfrac1{a_n}+1$；" "\n"
        r"②$a_ka_{k+1}a_{k+2}=\dfrac1{(k+1)(k+2)(k+3)}$，用 $\dfrac1{m(m+1)}=\dfrac1m-\dfrac1{m+1}$ 型裂项．"
    ),
    'solution': (
        r"①当 $\lambda=1$ 时，$a_{n+1}=\dfrac{a_n}{1+a_n}$．" "\n"
        r"因为 $a_1=\dfrac12>0$，由递推式知 $a_n>0$，故可取倒数：" "\n"
        r"$\dfrac1{a_{n+1}}=\dfrac{1+a_n}{a_n}=\dfrac1{a_n}+1$，即 $\dfrac1{a_{n+1}}-\dfrac1{a_n}=1$．" "\n"
        r"所以数列 $\left\{\dfrac1{a_n}\right\}$ 是以 $\dfrac1{a_1}=2$ 为首项、$1$ 为公差的等差数列，" "\n"
        r"$\dfrac1{a_n}=2+(n-1)=n+1$，故 $a_n=\dfrac1{n+1}$．" "\n"
        r"②由①知 $a_k=\dfrac1{k+1}$，故" "\n"
        r"$a_ka_{k+1}a_{k+2}=\dfrac1{(k+1)(k+2)(k+3)}$．" "\n"
        r"因为 $\dfrac1{(k+1)(k+2)}-\dfrac1{(k+2)(k+3)}=\dfrac{(k+3)-(k+1)}{(k+1)(k+2)(k+3)}=\dfrac2{(k+1)(k+2)(k+3)}$，" "\n"
        r"所以 $a_ka_{k+1}a_{k+2}=\dfrac12\left[\dfrac1{(k+1)(k+2)}-\dfrac1{(k+2)(k+3)}\right]$．" "\n"
        r"于是 $a_1a_2a_3+a_2a_3a_4+\cdots+a_na_{n+1}a_{n+2}$" "\n"
        r"$=\dfrac12\left[\left(\dfrac1{2\times3}-\dfrac1{3\times4}\right)+\left(\dfrac1{3\times4}-\dfrac1{4\times5}\right)+\cdots+\left(\dfrac1{(n+1)(n+2)}-\dfrac1{(n+2)(n+3)}\right)\right]$" "\n"
        r"$=\dfrac12\left[\dfrac16-\dfrac1{(n+2)(n+3)}\right]=\dfrac{(n+2)(n+3)-6}{12(n+2)(n+3)}=\dfrac{n^2+5n}{12(n+2)(n+3)}=\dfrac{n(n+5)}{12(n+2)(n+3)}$．"
    ),
    'review': (
        r"① ⭐⭐ **$a_{n+1}=\dfrac{a_n}{1+a_n}$ 型一律取倒数**：$\dfrac1{a_{n+1}}=\dfrac1{a_n}+1$ 一步成等差，" "\n"
        r"这是分式线性递推（$a_{n+1}=\dfrac{a_n}{pa_n+q}$）的标准解法" "\n"
        r"② ⭐⭐ **三项积的裂项**：$\dfrac1{m(m+1)(m+2)}=\dfrac12\left[\dfrac1{m(m+1)}-\dfrac1{(m+1)(m+2)}\right]$，" "\n"
        r"系数 $\dfrac12$ 来自 $(m+2)-m=2$；一般地，$\dfrac1{m(m+d)(m+2d)}$ 的系数是 $\dfrac1{2d}$" "\n"
        r"③ ⚠ 原题答案中还有「（2）证明见解析」，但（2）问的题干与详解在提取文本中缺失" "\n"
        r"（p227 双栏交错，右栏下半被截断），本条只呈现（1）的两小问，未臆造（2）" "\n"
        r"④ 数值复核：$n=1$ 时左式 $=a_1a_2a_3=\dfrac12\times\dfrac13\times\dfrac14=\dfrac1{24}$，" "\n"
        r"右式 $=\dfrac{1\times6}{12\times3\times4}=\dfrac6{144}=\dfrac1{24}$ ✓；" "\n"
        r"$n=2$ 时左式 $=\dfrac1{24}+\dfrac1{3\times4\times5}=\dfrac1{24}+\dfrac1{60}=\dfrac{5+2}{120}=\dfrac7{120}$，" "\n"
        r"右式 $=\dfrac{2\times7}{12\times4\times5}=\dfrac{14}{240}=\dfrac7{120}$ ✓"
    ),
    'difficulty': 0.7,
    'topics': ['M-T-273'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-273-E1',
}

# ---------------------------------------------------------------- M-T-275-E1
T275_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知 $S_n$ 为数列 $\{a_n\}$ 的前 $n$ 项和，$S_2=10$，$S_n=\dfrac{n-1}{n+1}a_{n+1}+2$（$n\in\mathbb N^*$）．" "\n"
        r"（1）求数列 $\{a_n\}$ 的通项公式；" "\n"
        r"（2）设 $b_n=\dfrac{a_n}{2^n(n+1)!}$（$n\in\mathbb N^*$），数列 $\{b_n\}$ 的前 $n$ 项和为 $T_n$，求证：$\dfrac12\le T_n<1$．"
    ),
    'answer': r"（1）$a_n=n\cdot2^n$（$n\in\mathbb N^*$）；（2）证明见解析",
    'analysis': (
        r"（1）$n=1$ 得 $a_1=2$，再由 $S_2=10$ 得 $a_2=8$；$n\ge2$ 时退位作差得 $\dfrac{a_{n+1}}{n+1}=2\cdot\dfrac{a_n}n$；" "\n"
        r"（2）$b_n=\dfrac n{(n+1)!}=\dfrac1{n!}-\dfrac1{(n+1)!}$，望远镜求和．"
    ),
    'solution': (
        r"**（1）** 在 $S_n=\dfrac{n-1}{n+1}a_{n+1}+2$ 中令 $n=1$，得 $S_1=a_1=0+2=2$，即 $a_1=2$．" "\n"
        r"又 $S_2=10$，故 $a_2=S_2-a_1=8$．" "\n"
        r"当 $n\ge2$ 时，$S_n=\dfrac{n-1}{n+1}a_{n+1}+2$　①，$S_{n-1}=\dfrac{n-2}na_n+2$　②，" "\n"
        r"①$-$② 得 $a_n=\dfrac{n-1}{n+1}a_{n+1}-\dfrac{n-2}na_n$，" "\n"
        r"即 $a_n+\dfrac{n-2}na_n=\dfrac{n-1}{n+1}a_{n+1}$，$\dfrac{2n-2}na_n=\dfrac{n-1}{n+1}a_{n+1}$．" "\n"
        r"因 $n\ge2$，可约去 $n-1$，得 $\dfrac2n a_n=\dfrac1{n+1}a_{n+1}$，即 $\dfrac{a_{n+1}}{n+1}=2\cdot\dfrac{a_n}n$（$n\ge2$）．" "\n"
        r"所以数列 $\left\{\dfrac{a_n}n\right\}$ 从第二项起是公比为 $2$ 的等比数列，" "\n"
        r"$\dfrac{a_2}2=4$，故 $\dfrac{a_n}n=4\cdot2^{n-2}=2^n$（$n\ge2$），即 $a_n=n\cdot2^n$（$n\ge2$）．" "\n"
        r"$n=1$ 时 $a_1=2=1\cdot2^1$ 也满足，故 $a_n=n\cdot2^n$（$n\in\mathbb N^*$）．" "\n"
        r"**（2）** $b_n=\dfrac{n\cdot2^n}{2^n(n+1)!}=\dfrac n{(n+1)!}=\dfrac{(n+1)-1}{(n+1)!}=\dfrac1{n!}-\dfrac1{(n+1)!}$．" "\n"
        r"所以 $T_n=\left(\dfrac1{1!}-\dfrac1{2!}\right)+\left(\dfrac1{2!}-\dfrac1{3!}\right)+\cdots+\left(\dfrac1{n!}-\dfrac1{(n+1)!}\right)=1-\dfrac1{(n+1)!}$．" "\n"
        r"因为 $\{T_n\}$ 单调递增且 $T_1=\dfrac12$，又 $\dfrac1{(n+1)!}>0$，故 $\dfrac12\le T_n<1$．"
    ),
    'review': (
        r"① ⭐⭐ **退位作差后 $\dfrac{2n-2}na_n=\dfrac{n-1}{n+1}a_{n+1}$ 要「约 $n-1$ 再移项」**：" "\n"
        r"先提出 $n-1$（由 $n\ge2$ 保证非零），再整理成 $\dfrac{a_{n+1}}{n+1}=2\cdot\dfrac{a_n}n$ 的**同构形式**，" "\n"
        r"这样才看得出「$\{\frac{a_n}n\}$ 是等比」，而不是 $a_n$ 本身" "\n"
        r"② ⭐⭐ **$n=1$ 要单独处理**：$n=1$ 时 $\dfrac{n-2}n$ 分母的 $n-2<0$ 且①式给 $a_1=2$，" "\n"
        r"所以递推只从 $n\ge2$ 成立，最后必须验证 $a_1$ 也符合 $n\cdot2^n$" "\n"
        r"③ ⭐⭐ $b_n=\dfrac n{(n+1)!}$ 的裂项用「分子凑分母的第一因子」：" "\n"
        r"$n=(n+1)-1$，故 $\dfrac n{(n+1)!}=\dfrac{n+1}{(n+1)!}-\dfrac1{(n+1)!}=\dfrac1{n!}-\dfrac1{(n+1)!}$" "\n"
        r"④ 数值复核：$n=1$ 时 $T_1=b_1=\dfrac{1\cdot2}{2\times2!}=\dfrac12$ ✓ 与下界一致（下界可取到）；" "\n"
        r"$n=2$ 时 $b_2=\dfrac{2\cdot4}{4\times3!}=\dfrac13$，$T_2=\dfrac12+\dfrac13=\dfrac56$，$1-\dfrac1{3!}=\dfrac56$ ✓"
    ),
    'difficulty': 0.74,
    'topics': ['M-T-275'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-275-E1',
}

# ---------------------------------------------------------------- M-T-009-V1
T009_V1 = {
    'type': '选择',
    'stem_text': r"已知 $a>0$，$b>0$，$\dfrac3b+\dfrac2a=1$，则 $2a+3b$ 的最小值为（　　）",
    'opts': [('A', '20'), ('B', '24'), ('C', '25'), ('D', '28')],
    'answer': 'C',
    'analysis': (
        r"所求式 $2a+3b$ 的两个系数 $2,3$ 与条件 $\dfrac2a+\dfrac3b$ 的分子**恰好对齐**，" "\n"
        r"故用「1 的代换」后交叉项之积为定值，可直接用基本不等式．"
    ),
    'solution': (
        r"由 $\dfrac2a+\dfrac3b=1$，得" "\n"
        r"$2a+3b=(2a+3b)\left(\dfrac2a+\dfrac3b\right)=4+\dfrac{6a}b+\dfrac{6b}a+9=13+\dfrac{6a}b+\dfrac{6b}a$．" "\n"
        r"因为 $a>0,\ b>0$，所以 $\dfrac{6a}b+\dfrac{6b}a\ge2\sqrt{\dfrac{6a}b\cdot\dfrac{6b}a}=2\sqrt{36}=12$，" "\n"
        r"故 $2a+3b\ge13+12=25$，当且仅当 $\dfrac{6a}b=\dfrac{6b}a$ 即 $a=b$ 时取等号．" "\n"
        r"此时由 $\dfrac3a+\dfrac2a=1$ 得 $a=b=5$，故最小值为 $25$，选 C．"
    ),
    'review': (
        r"① ⭐⭐ **系数对齐是「1 的代换」好用的前提**：所求 $2a+3b$ 与条件 $\dfrac2a+\dfrac3b$ 的" "\n"
        r"系数 $2,3$ 位置完全一致（都是「$2$ 配 $a$、$3$ 配 $b$」），" "\n"
        r"展开后交叉项恰为 $\dfrac{6a}b$ 与 $\dfrac{6b}a$，**乘积不含变量** $6\times6=36$ —— 这是能用基本不等式的唯一理由" "\n"
        r"② ⭐⭐ 常数项是 $4+9=13$：**就是所求两系数与条件两分子的交叉乘积之和**" "\n"
        r"（$2\times2+3\times3=13$），可先心算出来再凑 $2\sqrt{36}=12$" "\n"
        r"③ ⚠ 取等条件不能漏：$a=b=5$ 确实满足 $\dfrac35+\dfrac25=1$ ✓，" "\n"
        r"若漏写「当且仅当」则基本不等式用得不完整" "\n"
        r"④ 数值复核：取 $a=b=5$，$2a+3b=10+15=25$；取 $a=4$ 则 $\dfrac3b=\dfrac12$，$b=6$，$2a+3b=8+18=26>25$ ✓"
    ),
    'difficulty': 0.45,
    'topics': ['M-T-009'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-009-V1',
}

QS = [
    T257_V3,
    T263_V1,
    T264_V1,
    T267_V1,
    T268_E1,
    T269_V1,
    T271_E1,
    T271_V1,
    T272_E1,
    T272_V2,
    T273_E1,
    T275_E1,
    T009_V1,
]
