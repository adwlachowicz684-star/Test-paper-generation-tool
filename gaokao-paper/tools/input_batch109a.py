# -*- coding: utf-8 -*-
r"""第 109 批：数列「因式分解 · 三阶递推 · 纠缠数列 · 归纳」+ 导数「不等式证明」+ 圆锥曲线「定点定值」

    python3 tools/run_batch.py 109

## 选题依据

按「详解完整 + 同题型聚堆 + 无图依赖 + 可独立数值验算」筛出，三个块集中在相邻页码：

- M-T-260 四题（p218–p219）：因式分解型、三阶递推、纠缠数列、数学归纳型
- M-T-168 三题（p133–p134）：不等式证明之「利用第一问」与「含 e^x 和 lnx 型」
- M-T-362 三题（p343–p344）：椭圆中的定点、定直线、面积最值

10 题全部由我独立推导一遍并与原书答案数值对拍（对拍过程见每题 review）。

## 第一条：二次型递推先「因式分解」再约（M-T-260-E1）

$4a_n^2+2a_n=a_{n+1}^2-a_{n+1}$ 移项后右边是平方差：

$$a_{n+1}^2-4a_n^2=a_{n+1}+2a_n\ \Longrightarrow\ (a_{n+1}-2a_n)(a_{n+1}+2a_n)=a_{n+1}+2a_n$$

正项数列 ⟹ $a_{n+1}+2a_n>0$ ⟹ **两边同除以它**，一步得 $a_{n+1}-2a_n=1$。

> ⭐⭐ 凡是「二次型 $a_{n+1}^2$ 与 $a_n^2$」同现，先凑平方差，再看能不能约掉一个正因式。

## 第二条：三阶递推构造等比的标准动作（M-T-260-V1）

要证 $\{a_{n+1}-a_n-n\}$ 是等比，就把递推式里的 $a_{n+2}$ 写成
$a_{n+2}-a_{n+1}-(n+1)$，再与 $2(a_{n+1}-a_n-n)$ 比对，**常数项自动配平**：
$-n+1-(n+1)=-2n$ 正好是 $2\times(-n)$。

> ⭐ 构造类证明不要猜，把目标式写出来反推一次就够。

## 第三条：「纠缠数列」用「和」「差」解耦（M-T-260-V2）

$4a_{n+1}=3a_n-b_n+4$、$4b_{n+1}=3b_n-a_n-4$ 两式**相加**得 $a_{n+1}+b_{n+1}=\frac12(a_n+b_n)$，
**相减**得 $(a_{n+1}-b_{n+1})-(a_n-b_n)=2$ —— 一个等比、一个等差，然后解二元一次方程组。

> ⭐⭐ 只要两个递推里 $a,b$ 的系数是对称的（$3$ 与 $-1$），和差一定解耦。

## 第四条：导数不等式证明——「第一问的结论是第二问的工具」（M-T-168-E1）

（1）给出 $a=-2$ 时 $f$ 递增且 $f(1)=0$ ⟹ $x>1$ 时 $-2\ln x+x-\frac1x>0$；
（2）把 $x=\sqrt{\frac nm}$ 代进去，恰好把 $\ln$ 换成 $-\frac{m+n}2$，剩下的用 AM-GM 闭合。

> ⭐⭐ 代入点的选取有迹可循：**要让 $\ln x$ 变成已知条件里的量**。
> 已知 $e^{m+n}=\frac nm$（即 $\ln\frac nm=m+n$），所以取 $x=\sqrt{\frac nm}$ 使 $\ln x=\frac{m+n}2$。

## 第五条：椭圆定点问题——「先猜后证」与「韦达代入」（M-T-362）

- V1：直线 $NH$ 过定点 $(\frac32,0)$，关键是韦达给出 $2ty_1y_2=y_1+y_2$，代入后**参数 $t$ 完全消失**
- V2：点 $G$ 在定直线 $x=1$ 上，整理成 $2x_1x_2-5(x_1+x_2)+8=0$，代入韦达**恰好恒为 0**

> ⭐⭐ 两题的收尾都是「整理成只含 $x_1+x_2$ 与 $x_1x_2$ 的式子，代入后分子恒为 0」。
> 若代入后消不干净，说明定点/定直线的位置猜错了。
"""

T260_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知正项数列 $\{a_n\}$ 满足 $a_1=1$，$4a_n^2+2a_n=a_{n+1}^2-a_{n+1}\left(n\in\mathbf N^*\right)$．" "\n"
        r"（1）证明：数列 $\{a_n+1\}$ 是等比数列；" "\n"
        r"（2）证明：$\dfrac1{a_2}+\dfrac1{a_3}+\dfrac1{a_4}+\cdots+\dfrac1{a_{n+1}}<\dfrac23\left(n\in\mathbf N^*\right)$．"
    ),
    'stem': [
        r"已知正项数列 $\{a_n\}$ 满足 $a_1=1$，$4a_n^2+2a_n=a_{n+1}^2-a_{n+1}\left(n\in\mathbf N^*\right)$．",
        r"（1）证明：数列 $\{a_n+1\}$ 是等比数列；",
        r"（2）证明：$\dfrac1{a_2}+\dfrac1{a_3}+\dfrac1{a_4}+\cdots+\dfrac1{a_{n+1}}<\dfrac23\left(n\in\mathbf N^*\right)$．",
    ],
    'opts': [],
    'answer': r"（1）证明见解析；（2）证明见解析",
    'analysis': (
        r"（1）把等式右边看成 $a_{n+1}^2-a_{n+1}$，移项后凑出 $a_{n+1}^2-4a_n^2$ 这个平方差，"
        r"与左边的 $a_{n+1}+2a_n$ 约去（正项保证它不为零），即得 $a_{n+1}=2a_n+1$．" "\n"
        r"（2）$a_n=2^n-1$，对 $n\ge2$ 放缩 $\dfrac1{2^n-1}\le\dfrac13\cdot\dfrac1{2^{n-2}}$，"
        r"化成一个等比数列求和，其极限是 $\dfrac23$ 但取不到．"
    ),
    'solution': (
        r"**（1）证明** 由 $4a_n^2+2a_n=a_{n+1}^2-a_{n+1}$ 得" "\n"
        r"$a_{n+1}^2-4a_n^2=a_{n+1}+2a_n$，即 $\left(a_{n+1}-2a_n\right)\left(a_{n+1}+2a_n\right)=a_{n+1}+2a_n$．" "\n"
        r"因为 $\{a_n\}$ 是正项数列，所以 $a_{n+1}+2a_n>0$，两边同除以它得" "\n"
        r"$a_{n+1}-2a_n=1$，即 $\boxed{a_{n+1}=2a_n+1}$．" "\n"
        r"于是 $\dfrac{a_{n+1}+1}{a_n+1}=\dfrac{2a_n+2}{a_n+1}=2$，又 $a_1+1=2$，" "\n"
        r"故 $\{a_n+1\}$ 是以 $2$ 为首项、$2$ 为公比的等比数列．" "\n"
        r"**（2）证明** 由（1）得 $a_n+1=2\cdot2^{n-1}=2^n$，即 $a_n=2^n-1$．" "\n"
        r"当 $n\ge2$ 时，$2^n-1\ge 3\cdot2^{n-2}$（即 $2^{n-2}\cdot4-1\ge3\cdot2^{n-2}$，亦即 $2^{n-2}\ge1$ 成立），" "\n"
        r"所以 $\dfrac1{a_n}=\dfrac1{2^n-1}\le\dfrac13\cdot\dfrac1{2^{n-2}}$．" "\n"
        r"于是" "\n"
        r"$\dfrac1{a_2}+\dfrac1{a_3}+\cdots+\dfrac1{a_{n+1}}\le\dfrac13\left(1+\dfrac12+\dfrac14+\cdots+\dfrac1{2^{n-1}}\right)$" "\n"
        r"$=\dfrac13\cdot\dfrac{1-\left(\frac12\right)^n}{1-\frac12}=\dfrac23\left(1-\dfrac1{2^n}\right)<\dfrac23$．" "\n"
        r"故 $\boxed{\dfrac1{a_2}+\dfrac1{a_3}+\cdots+\dfrac1{a_{n+1}}<\dfrac23}$ 对一切 $n\in\mathbf N^*$ 成立．"
    ),
    'review': (
        r"① ⭐⭐ **平方差是（1）的唯一入口**：左边是 $4a_n^2+2a_n$，右边是 $a_{n+1}^2-a_{n+1}$，"
        r"移项凑 $a_{n+1}^2-4a_n^2$ 后，右端剩下的 $a_{n+1}+2a_n$ 恰好等于左端的 $2a_n+a_{n+1}$——"
        r"**这个「恰好」是命题人设计好的，看到就要意识到可以约**．" "\n"
        r"② ⚠ **必须说明 $a_{n+1}+2a_n\ne0$**：正项数列保证 $a_{n+1}+2a_n>0$，"
        r"若题目只说「数列」而未说正项，就要另找理由，否则约分不合法．" "\n"
        r"③ ⭐ **（2）的放缩方向**：要得到上界就要把分母**缩小**，$2^n-1\ge3\cdot2^{n-2}$ 是对的；"
        r"反过来写 $2^n-1\le 2^n$ 会得到 $\sum\frac1{2^n}<1$，比 $\frac23$ 松，证不出结论．" "\n"
        r"④ 数值复核：$a_n=1,3,7,15,31,63$，代回原式 $4\cdot1^2+2\cdot1=6=3^2-3$ ✓、"
        r"$4\cdot3^2+2\cdot3=42=7^2-7$ ✓；" "\n"
        r"   $\frac1{a_2}+\cdots+\frac1{a_{11}}=0.6062<\frac23=0.6667$ ✓，且随 $n$ 增大趋近 $\frac23$ 而取不到．" "\n"
        r"**通法（二次型递推）**：" "\n"
        r"① 出现 $a_{n+1}^2$ 与 $a_n^2$ ⟹ 移项凑平方差；" "\n"
        r"② 约去正因式后化为一阶线性递推 $a_{n+1}=pa_n+q$ ⟹ 配成 $a_{n+1}+c=p(a_n+c)$；" "\n"
        r"③ 求和型不等式用等比放缩，注意放缩后的和必须**严格小于**目标值．"
    ),
    'difficulty': 0.63,
    'topics': ['M-T-260'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-260-E1',
}

T260_V1 = {
    'type': '解答',
    'stem_text': (
        r"在数列 $\{a_n\}$ 中，$a_1=1$，$a_2=3$，$a_{n+2}=3a_{n+1}-2a_n-n+1$．" "\n"
        r"（1）证明 $\{a_{n+1}-a_n-n\}$ 为等比数列；" "\n"
        r"（2）求 $a_n$．"
    ),
    'stem': [
        r"在数列 $\{a_n\}$ 中，$a_1=1$，$a_2=3$，$a_{n+2}=3a_{n+1}-2a_n-n+1$．",
        r"（1）证明 $\{a_{n+1}-a_n-n\}$ 为等比数列；",
        r"（2）求 $a_n$．",
    ],
    'opts': [],
    'answer': r"（1）证明见解析；（2）$a_n=2^{n-1}+\dfrac{n(n-1)}2$",
    'analysis': (
        r"（1）把递推式改写为 $a_{n+2}-a_{n+1}-(n+1)=2\left(a_{n+1}-a_n-n\right)$，"
        r"首项 $a_2-a_1-1=1$，公比为 $2$．" "\n"
        r"（2）由（1）得 $a_{n+1}-a_n=2^{n-1}+n$，用累加法求和，"
        r"等比部分得 $2^{n-1}-1$，等差部分得 $\dfrac{n(n-1)}2$．"
    ),
    'solution': (
        r"**（1）证明** 由 $a_{n+2}=3a_{n+1}-2a_n-n+1$ 得" "\n"
        r"$a_{n+2}-a_{n+1}-\left(n+1\right)=2a_{n+1}-2a_n-n+1-\left(n+1\right)=2\left(a_{n+1}-a_n-n\right)$．" "\n"
        r"又 $a_2-a_1-1=3-1-1=1\ne0$，" "\n"
        r"故 $\{a_{n+1}-a_n-n\}$ 是以 $1$ 为首项、$2$ 为公比的等比数列．" "\n"
        r"**（2）** 由（1）得 $a_{n+1}-a_n-n=2^{n-1}$，即 $a_{n+1}-a_n=2^{n-1}+n$．" "\n"
        r"当 $n\ge2$ 时，累加得" "\n"
        r"$a_n-a_1=\sum\limits_{k=1}^{n-1}\left(a_{k+1}-a_k\right)=\sum\limits_{k=1}^{n-1}\left(2^{k-1}+k\right)$" "\n"
        r"$=\left(2^{n-1}-1\right)+\dfrac{n(n-1)}2$．" "\n"
        r"所以 $a_n=1+2^{n-1}-1+\dfrac{n(n-1)}2=2^{n-1}+\dfrac{n(n-1)}2$．" "\n"
        r"当 $n=1$ 时，上式给出 $a_1=2^0+0=1$，也满足．" "\n"
        r"故 $\boxed{a_n=2^{n-1}+\dfrac{n(n-1)}2}$．"
    ),
    'review': (
        r"① ⭐⭐ **构造式是「写出来的」不是「猜出来的」**：目标是 $\{a_{n+1}-a_n-n\}$，"
        r"就把 $n$ 换成 $n+1$ 写成 $a_{n+2}-a_{n+1}-(n+1)$，代入递推式后常数项 $-n+1-(n+1)=-2n$ 恰好配成 $2\times(-n)$．" "\n"
        r"② ⭐ **首项要单独算**：$a_2-a_1-1=1$，不能想当然写成 $a_1-a_0-0$．" "\n"
        r"③ ⚠ **累加上限是 $n-1$ 不是 $n$**：$a_n-a_1=\sum_{k=1}^{n-1}$，最后必须加回 $a_1=1$．" "\n"
        r"④ ⚠ **务必检验 $n=1$**：由累加得到的式子对 $n\ge2$ 成立，$n=1$ 要单独代入验证（本题恰好成立）．" "\n"
        r"⑤ 数值复核：递推得 $1,3,7,14,26,47,85,156$；公式 $2^{n-1}+\frac{n(n-1)}2$ 给出同组数 ✓；" "\n"
        r"   $a_{n+1}-a_n-n=1,2,4,8,16,32$ 确实是公比 $2$ 的等比 ✓" "\n"
        r"**通法（三阶/二阶线性递推）**：" "\n"
        r"① 形如 $a_{n+2}=pa_{n+1}+qa_n+f(n)$ ⟹ 按 $f$ 的类型构造等差或等比；" "\n"
        r"② 差分为等比 ⟹ 用累加法，等比求和与多项式求和分开算；" "\n"
        r"③ 最后回到 $n=1$ 检验．"
    ),
    'difficulty': 0.58,
    'topics': ['M-T-260'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-260-V1',
}

T260_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知 $\{a_n\}$ 和 $\{b_n\}$ 满足 $a_1=1$，$b_1=0$，$4a_{n+1}=3a_n-b_n+4$，$4b_{n+1}=3b_n-a_n-4$．" "\n"
        r"（1）证明：$\{a_n+b_n\}$ 是等比数列，$\{a_n-b_n\}$ 是等差数列；" "\n"
        r"（2）求 $\{a_n\}$ 和 $\{b_n\}$ 的通项公式．"
    ),
    'stem': [
        r"已知 $\{a_n\}$ 和 $\{b_n\}$ 满足 $a_1=1$，$b_1=0$，$4a_{n+1}=3a_n-b_n+4$，$4b_{n+1}=3b_n-a_n-4$．",
        r"（1）证明：$\{a_n+b_n\}$ 是等比数列，$\{a_n-b_n\}$ 是等差数列；",
        r"（2）求 $\{a_n\}$ 和 $\{b_n\}$ 的通项公式．",
    ],
    'opts': [],
    'answer': (
        r"（1）证明见解析；（2）$a_n=\left(\dfrac12\right)^n+n-\dfrac12$，$b_n=\left(\dfrac12\right)^n-n+\dfrac12$"
    ),
    'analysis': (
        r"（1）两式相加消去常数项 $4$ 与 $-4$，得 $4(a_{n+1}+b_{n+1})=2(a_n+b_n)$；"
        r"两式相减得 $4(a_{n+1}-b_{n+1})=4(a_n-b_n)+8$．" "\n"
        r"（2）由（1）得 $a_n+b_n=\left(\frac12\right)^{n-1}$ 与 $a_n-b_n=2n-1$，两式相加减即得．"
    ),
    'solution': (
        r"**（1）证明** 记 $4a_{n+1}=3a_n-b_n+4$ 为①，$4b_{n+1}=3b_n-a_n-4$ 为②．" "\n"
        r"①+②得 $4\left(a_{n+1}+b_{n+1}\right)=2\left(a_n+b_n\right)$，即 $\dfrac{a_{n+1}+b_{n+1}}{a_n+b_n}=\dfrac12$．" "\n"
        r"又 $a_1+b_1=1+0=1$，故 $\{a_n+b_n\}$ 是以 $1$ 为首项、$\dfrac12$ 为公比的等比数列．" "\n"
        r"①$-$②得 $4\left(a_{n+1}-b_{n+1}\right)=4\left(a_n-b_n\right)+8$，" "\n"
        r"即 $\left(a_{n+1}-b_{n+1}\right)-\left(a_n-b_n\right)=2$．" "\n"
        r"又 $a_1-b_1=1-0=1$，故 $\{a_n-b_n\}$ 是以 $1$ 为首项、$2$ 为公差的等差数列．" "\n"
        r"**（2）** 由（1）得 $a_n+b_n=\left(\dfrac12\right)^{n-1}$ ③，$a_n-b_n=1+2(n-1)=2n-1$ ④．" "\n"
        r"（③+④）$\div2$ 得 $a_n=\dfrac{\left(\frac12\right)^{n-1}+2n-1}2=\left(\dfrac12\right)^n+n-\dfrac12$；" "\n"
        r"（③$-$④）$\div2$ 得 $b_n=\dfrac{\left(\frac12\right)^{n-1}-\left(2n-1\right)}2=\left(\dfrac12\right)^n-n+\dfrac12$．" "\n"
        r"故 $\boxed{a_n=\left(\dfrac12\right)^n+n-\dfrac12,\quad b_n=\left(\dfrac12\right)^n-n+\dfrac12}$．"
    ),
    'review': (
        r"① ⭐⭐ **「和差解耦」是纠缠数列的标准动作**：两个递推中 $a_n$ 的系数都是 $3$、$b_n$ 的系数都是 $-1$（对称），"
        r"于是相加时 $b$ 的贡献是 $-b_n-b_n=-2b_n$、相减时是 $-b_n+b_n=0$ 之外再叠上常数，**加减各消掉一个自由度**．" "\n"
        r"② ⭐ **常数项 $\pm4$ 的设计**：相加时 $+4-4=0$（等比，无常数项），相减时 $+4+4=8$（等差，公差 $2$）．"
        r"看到对称系数 + 反号常数，就能预判「和是等比、差是等差」．" "\n"
        r"③ ⚠ **$\left(\frac12\right)^{n-1}$ 除以 $2$ 是 $\left(\frac12\right)^n$ 不是 $\left(\frac12\right)^{n-2}$**："
        r"这一步极易出错，可代 $n=1$ 检验（$a_1=\frac12+1-\frac12=1$ ✓）．" "\n"
        r"④ 数值复核：逐项递推 $n=2$ 得 $a_2=1.75,\ b_2=-1.25$，公式给出 $\frac14+2-\frac12=1.75$、$\frac14-2+\frac12=-1.25$ ✓；" "\n"
        r"   $n=6$：$a_6=5.515625,\ b_6=-5.484375$，与递推完全一致 ✓" "\n"
        r"**通法（纠缠数列）**：" "\n"
        r"① 系数对称 ⟹ 和差解耦；② 解耦后各算各的；③ 解二元一次方程组还原 $a_n,b_n$；" "\n"
        r"④ 用 $n=1$ 检验通项．"
    ),
    'difficulty': 0.60,
    'topics': ['M-T-260'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-260-V2',
}

T260_V3 = {
    'type': '解答',
    'stem_text': (
        r"设正数数列 $\{a_n\}$ 的前 $n$ 项和为 $S_n$，且 $S_n=\dfrac12\left(a_n+\dfrac1{a_n}\right)\left(n\in\mathbf N^*\right)$，"
        r"试求 $a_n$，并用数学归纳法证明你的结论．"
    ),
    'stem': [
        r"设正数数列 $\{a_n\}$ 的前 $n$ 项和为 $S_n$，且 $S_n=\dfrac12\left(a_n+\dfrac1{a_n}\right)\left(n\in\mathbf N^*\right)$，"
        r"试求 $a_n$，并用数学归纳法证明你的结论．",
    ],
    'opts': [],
    'answer': r"$a_n=\sqrt n-\sqrt{n-1}$；证明见解析",
    'analysis': (
        r"由 $n=1,2,3$ 分别解出 $a_1=1$、$a_2=\sqrt2-1$、$a_3=\sqrt3-\sqrt2$，猜想 $a_n=\sqrt n-\sqrt{n-1}$；" "\n"
        r"归纳递推时用 $a_{k+1}=S_{k+1}-S_k$，所得方程 $a_{k+1}-\dfrac1{a_{k+1}}=-2\sqrt k$ 是关于 $a_{k+1}$ 的二次方程，"
        r"取正根即得．"
    ),
    'solution': (
        r"**求 $a_n$**：当 $n=1$ 时，$a_1=S_1=\dfrac12\left(a_1+\dfrac1{a_1}\right)$，即 $a_1^2=1$，由 $a_1>0$ 得 $a_1=1$．" "\n"
        r"当 $n=2$ 时，$1+a_2=\dfrac12\left(a_2+\dfrac1{a_2}\right)$，即 $a_2^2+2a_2-1=0$，取正根得 $a_2=\sqrt2-1$．" "\n"
        r"当 $n=3$ 时，$\sqrt2+a_3=\dfrac12\left(a_3+\dfrac1{a_3}\right)$，即 $a_3^2+2\sqrt2a_3-1=0$，取正根得 $a_3=\sqrt3-\sqrt2$．" "\n"
        r"猜想 $\boxed{a_n=\sqrt n-\sqrt{n-1}}$．下面用数学归纳法证明．" "\n"
        r"**证明**：（i）当 $n=1$ 时，$a_1=1=\sqrt1-\sqrt0$，成立．" "\n"
        r"（ii）假设当 $n=k\left(k\ge1\right)$ 时成立，即 $a_k=\sqrt k-\sqrt{k-1}$．" "\n"
        r"则当 $n=k+1$ 时，由 $S_{k+1}=\dfrac12\left(a_{k+1}+\dfrac1{a_{k+1}}\right)$ 与 $S_k=\dfrac12\left(a_k+\dfrac1{a_k}\right)$ 相减得" "\n"
        r"$a_{k+1}=\dfrac12\left(a_{k+1}+\dfrac1{a_{k+1}}\right)-\dfrac12\left(a_k+\dfrac1{a_k}\right)$，" "\n"
        r"即 $a_{k+1}-\dfrac1{a_{k+1}}=-\left(a_k+\dfrac1{a_k}\right)$．" "\n"
        r"由归纳假设 $a_k=\sqrt k-\sqrt{k-1}$，则 $\dfrac1{a_k}=\dfrac1{\sqrt k-\sqrt{k-1}}=\sqrt k+\sqrt{k-1}$，" "\n"
        r"故 $a_k+\dfrac1{a_k}=2\sqrt k$，代入得 $a_{k+1}-\dfrac1{a_{k+1}}=-2\sqrt k$．" "\n"
        r"整理为 $a_{k+1}^2+2\sqrt ka_{k+1}-1=0$，解得 $a_{k+1}=\dfrac{-2\sqrt k\pm\sqrt{4k+4}}2=-\sqrt k\pm\sqrt{k+1}$．" "\n"
        r"由 $a_{k+1}>0$ 取正号，得 $a_{k+1}=\sqrt{k+1}-\sqrt k$．" "\n"
        r"故当 $n=k+1$ 时结论也成立．" "\n"
        r"由（i）（ii）知，对任意 $n\in\mathbf N^*$，$a_n=\sqrt n-\sqrt{n-1}$ 成立．"
    ),
    'review': (
        r"① ⭐⭐ **归纳递推的关键变形是 $a_{k+1}-\frac1{a_{k+1}}=-\left(a_k+\frac1{a_k}\right)$**："
        r"由 $S_{k+1}-S_k=a_{k+1}$ 两边各展开一次即得，注意右端是**负号**（因为 $a_{k+1}$ 移到左边）．" "\n"
        r"② ⭐ **$a_k+\frac1{a_k}=2\sqrt k$ 是「裂项相消」的经典结果**：$a_k=\sqrt k-\sqrt{k-1}$ 的倒数是 $\sqrt k+\sqrt{k-1}$，"
        r"两者相加根号部分抵消，只剩 $2\sqrt k$．**这正是命题人把 $S_n$ 写成 $\frac12(a_n+\frac1{a_n})$ 的原因**．" "\n"
        r"③ ⚠ **必须取正根**：二次方程两根为 $-\sqrt k\pm\sqrt{k+1}$，其中 $-\sqrt k-\sqrt{k+1}<0$ 要舍去，"
        r"题设「正数数列」就是为此而设．" "\n"
        r"④ 数值复核：$a_1=1,\ a_2=0.414214,\ a_3=0.317837,\ a_4=0.267949,\ a_5=0.236068$；" "\n"
        r"   $S_1=1,\ S_2=1.414214,\ S_3=1.732051,\ S_4=2.000000,\ S_5=2.236068$，" "\n"
        r"   而 $\frac12(a_n+\frac1{a_n})$ 逐一等于上述 $S_n$ ✓（例如 $n=4$：$a_4=0.267949$，$\frac12(0.267949+3.732051)=2.000000$ ✓）" "\n"
        r"**通法（$S_n$ 与 $a_n$ 混合型）**：" "\n"
        r"① 先算前三项猜通项（分母有理化往往是关键）；" "\n"
        r"② 归纳递推时用 $a_{k+1}=S_{k+1}-S_k$，把 $S$ 的两式相减；" "\n"
        r"③ 正项条件用于取舍根．"
    ),
    'difficulty': 0.66,
    'topics': ['M-T-260'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-260-V3',
}

T168_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=a\ln x+x-\dfrac1x\left(a\in\mathbf R\right)$．" "\n"
        r"（1）当 $a<0$ 时，讨论函数 $f(x)$ 的单调性；" "\n"
        r"（2）若正数 $m$，$n$ 满足 $e^{m+n}=\dfrac nm$，求证 $\dfrac1m-\dfrac1n>2$．"
    ),
    'stem': [
        r"已知函数 $f(x)=a\ln x+x-\dfrac1x\left(a\in\mathbf R\right)$．",
        r"（1）当 $a<0$ 时，讨论函数 $f(x)$ 的单调性；",
        r"（2）若正数 $m$，$n$ 满足 $e^{m+n}=\dfrac nm$，求证 $\dfrac1m-\dfrac1n>2$．",
    ],
    'opts': [],
    'answer': (
        r"（1）当 $-2\le a<0$ 时，$f(x)$ 在 $(0,+\infty)$ 上单调递增；"
        r"当 $a<-2$ 时，$f(x)$ 在 $\left(0,\dfrac{-a-\sqrt{a^2-4}}2\right)$，"
        r"$\left(\dfrac{-a+\sqrt{a^2-4}}2,+\infty\right)$ 上递增，在 $\left(\dfrac{-a-\sqrt{a^2-4}}2,\dfrac{-a+\sqrt{a^2-4}}2\right)$ 上递减；"
        r"（2）证明见解析"
    ),
    'analysis': (
        r"（1）$f'(x)=\dfrac{x^2+ax+1}{x^2}$，分母恒正，只需看分子 $x^2+ax+1$ 在 $(0,+\infty)$ 上的符号，"
        r"按判别式 $\Delta=a^2-4$ 与 $a<0$ 分类．" "\n"
        r"（2）取 $a=-2$，由（1）知 $f$ 在 $(0,+\infty)$ 上递增且 $f(1)=0$，"
        r"故 $x>1$ 时 $-2\ln x+x-\dfrac1x>0$；再把 $x=\sqrt{\dfrac nm}>1$ 代入，用 AM-GM 收口．"
    ),
    'solution': (
        r"**（1）** $f(x)$ 的定义域为 $(0,+\infty)$，" "\n"
        r"$f'(x)=\dfrac ax+1+\dfrac1{x^2}=\dfrac{x^2+ax+1}{x^2}$．" "\n"
        r"因 $x^2>0$，故 $f'(x)$ 的符号由 $g(x)=x^2+ax+1$ 决定，$\Delta=a^2-4$．" "\n"
        r"$\bullet$ 当 $-2\le a<0$ 时，$\Delta\le0$，故 $g(x)\ge0$ 恒成立，$f'(x)\ge0$，" "\n"
        r"$\quad f(x)$ 在 $(0,+\infty)$ 上单调递增；" "\n"
        r"$\bullet$ 当 $a<-2$ 时，$\Delta>0$，$g(x)=0$ 的两根为 $x_1=\dfrac{-a-\sqrt{a^2-4}}2$，$x_2=\dfrac{-a+\sqrt{a^2-4}}2$．" "\n"
        r"$\quad$ 由 $a<0$ 且 $x_1x_2=1>0$、$x_1+x_2=-a>0$ 知 $0<x_1<x_2$，" "\n"
        r"$\quad$ 所以 $x\in(0,x_1)\cup(x_2,+\infty)$ 时 $f'(x)>0$，$x\in(x_1,x_2)$ 时 $f'(x)<0$，" "\n"
        r"$\quad$ 即 $f(x)$ 在 $(0,x_1)$，$(x_2,+\infty)$ 上递增，在 $(x_1,x_2)$ 上递减．" "\n"
        r"**（2）证明** 取 $a=-2$，由（1）知 $f(x)=-2\ln x+x-\dfrac1x$ 在 $(0,+\infty)$ 上单调递增，" "\n"
        r"又 $f(1)=0$，故当 $x>1$ 时 $f(x)>0$，即 $-2\ln x+x-\dfrac1x>0$．" "\n"
        r"由 $e^{m+n}=\dfrac nm$ 且 $m,n>0$ 得 $\dfrac nm>1$，令 $x=\sqrt{\dfrac nm}>1$，则 $\ln x=\dfrac{m+n}2$．" "\n"
        r"于是 $-\left(m+n\right)+\sqrt{\dfrac nm}-\sqrt{\dfrac mn}>0$，即" "\n"
        r"$\dfrac{n-m}{\sqrt{mn}}>m+n$．" "\n"
        r"又由 AM-GM 不等式 $m+n\ge2\sqrt{mn}>0$，故" "\n"
        r"$n-m>\left(m+n\right)\sqrt{mn}\ge2\sqrt{mn}\cdot\sqrt{mn}=2mn$．" "\n"
        r"两边同除以正数 $mn$，得 $\dfrac{n-m}{mn}>2$，即 $\boxed{\dfrac1m-\dfrac1n>2}$．"
    ),
    'review': (
        r"① ⭐⭐ **（2）的代入点不是 $\frac nm$ 而是 $\sqrt{\frac nm}$**："
        r"因为已知条件是 $\ln\frac nm=m+n$，取 $x=\sqrt{\frac nm}$ 才能让 $\ln x$ 变成 $\frac{m+n}2$，" "\n"
        r"   同时 $x-\frac1x$ 变成 $\frac{n-m}{\sqrt{mn}}$，与结论 $\frac{n-m}{mn}>2$ 只差一个 $\sqrt{mn}$ 因子——"
        r"**这个「只差一步」就是选点的依据**．" "\n"
        r"② ⭐⭐ **收口用 AM-GM 的方向**：已知 $\frac{n-m}{\sqrt{mn}}>m+n$，要证 $\frac{n-m}{mn}>2$ 即 $n-m>2mn$，"
        r"只需 $m+n\ge2\sqrt{mn}$，**把左边的 $m+n$ 往小放**才能保持「$>$」传递下去．" "\n"
        r"③ ⭐ **（1）中两根都为正的判定**：$x_1x_2=1>0$、$x_1+x_2=-a>0$（$a<0$），比直接算根的表达式快．" "\n"
        r"④ 数值复核（取 $m=0.1$）：由 $e^{0.1+n}=10n$ 解得 $n=0.12527$，"
        r"$\frac1m-\frac1n=2.01696>2$ ✓；" "\n"
        r"   $x=\sqrt{n/m}=1.11922$，$-2\ln x+x-\frac1x=0.000477>0$ ✓；" "\n"
        r"   $\frac{n-m}{\sqrt{mn}}=0.225742>m+n=0.225266$ ✓ 三处完全闭合．" "\n"
        r"⑤ ⚠ 注意（1）中 $-2\le a<0$ 这一段容易漏掉「等于」："
        r"$a=-2$ 时 $f'(x)=\frac{(x-1)^2}{x^2}\ge0$，仍是递增（不是先增后减）．" "\n"
        r"**通法（用第一问证明第二问）**：" "\n"
        r"① 第一问给的单调性 ⟹ 某区间上 $f(x)>f(x_0)$（常取 $f(1)=0$ 这类特殊值）；" "\n"
        r"② 第二问把要证的不等式整理成「$f$ 在某点的值 $>0$」的形式，从而反推出代入点；" "\n"
        r"③ 余下的常数用基本不等式放缩．"
    ),
    'difficulty': 0.72,
    'topics': ['M-T-168'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-168-E1',
}

T168_V1 = {
    'type': '解答',
    'stem_text': (
        r"设函数 $f(x)=\dfrac xa-\ln(ax+1)\left(a\ne0\right)$．" "\n"
        r"（1）讨论函数 $f(x)$ 的单调性；" "\n"
        r"（2）当 $x>0$ 时，证明：$e^x-\dfrac{e^x\sin x}2>x$．"
    ),
    'stem': [
        r"设函数 $f(x)=\dfrac xa-\ln(ax+1)\left(a\ne0\right)$．",
        r"（1）讨论函数 $f(x)$ 的单调性；",
        r"（2）当 $x>0$ 时，证明：$e^x-\dfrac{e^x\sin x}2>x$．",
    ],
    'opts': [],
    'answer': (
        r"（1）当 $a>0$ 时，$f(x)$ 在 $\left(-\dfrac1a,a-\dfrac1a\right)$ 上递减，在 $\left(a-\dfrac1a,+\infty\right)$ 上递增；"
        r"当 $a<0$ 时，$f(x)$ 在 $\left(-\infty,a-\dfrac1a\right)$ 上递减，在 $\left(a-\dfrac1a,-\dfrac1a\right)$ 上递增；"
        r"（2）证明见解析"
    ),
    'analysis': (
        r"（1）$f'(x)=\dfrac{ax+1-a^2}{a(ax+1)}$，令 $f'(x)=0$ 得 $x=a-\dfrac1a$，再按 $a>0$、$a<0$ 分别结合定义域讨论．" "\n"
        r"（2）分两段：$0<x\le1$ 时构造 $g(x)=\dfrac{e^x(\sin x-2)}2$，用单调性得 $g(x)<-1\le-x$；"
        r"$x>1$ 时利用 $2-\sin x\ge1$ 与 $e^x>2x$ 直接放缩．"
    ),
    'solution': (
        r"**（1）** $f'(x)=\dfrac1a-\dfrac a{ax+1}=\dfrac{ax+1-a^2}{a(ax+1)}$，令 $f'(x)=0$ 得 $x=\dfrac{a^2-1}a=a-\dfrac1a$．" "\n"
        r"$\bullet$ 当 $a>0$ 时，定义域为 $\left(-\dfrac1a,+\infty\right)$，且 $a-\dfrac1a>-\dfrac1a$（因 $a>0$）．" "\n"
        r"$\quad$ 此时 $a(ax+1)>0$，分子 $ax+1-a^2$ 关于 $x$ 递增，" "\n"
        r"$\quad$ 故 $x\in\left(-\dfrac1a,a-\dfrac1a\right)$ 时 $f'(x)<0$，$x\in\left(a-\dfrac1a,+\infty\right)$ 时 $f'(x)>0$，" "\n"
        r"$\quad$ 即 $f(x)$ 在 $\left(-\dfrac1a,a-\dfrac1a\right)$ 上递减，在 $\left(a-\dfrac1a,+\infty\right)$ 上递增．" "\n"
        r"$\bullet$ 当 $a<0$ 时，定义域为 $ax+1>0$，即 $\left(-\infty,-\dfrac1a\right)$，且 $a-\dfrac1a<-\dfrac1a$．" "\n"
        r"$\quad$ 此时 $a(ax+1)<0$，分子 $ax+1-a^2$ 关于 $x$ 递减，" "\n"
        r"$\quad$ 故 $x\in\left(-\infty,a-\dfrac1a\right)$ 时分子 $>0$、$f'(x)<0$；" "\n"
        r"$\quad$ $x\in\left(a-\dfrac1a,-\dfrac1a\right)$ 时分子 $<0$、$f'(x)>0$，" "\n"
        r"$\quad$ 即 $f(x)$ 在 $\left(-\infty,a-\dfrac1a\right)$ 上递减，在 $\left(a-\dfrac1a,-\dfrac1a\right)$ 上递增．" "\n"
        r"**（2）证明** 即证 $\dfrac{e^x(2-\sin x)}2>x$．" "\n"
        r"$\bullet$ 当 $0<x\le1$ 时，令 $g(x)=\dfrac{e^x(\sin x-2)}2$，则" "\n"
        r"$\quad g'(x)=\dfrac{e^x(\sin x-2)+e^x\cos x}2=\dfrac{e^x\left(\sqrt2\sin\left(x+\frac\pi4\right)-2\right)}2<0$" "\n"
        r"$\quad$（因 $\sqrt2\sin\left(x+\frac\pi4\right)\le\sqrt2<2$），故 $g(x)$ 在 $(0,+\infty)$ 上递减．" "\n"
        r"$\quad$ 于是 $g(x)<g(0)=\dfrac{1\cdot(0-2)}2=-1\le-x$，即 $-e^x+\dfrac{e^x\sin x}2<-x$，" "\n"
        r"$\quad$ 整理得 $e^x-\dfrac{e^x\sin x}2>x$．" "\n"
        r"$\bullet$ 当 $x>1$ 时，由 $2-\sin x\ge1$ 得 $\dfrac{e^x(2-\sin x)}2\ge\dfrac{e^x}2$．" "\n"
        r"$\quad$ 又令 $\varphi(x)=e^x-2x$，则 $\varphi'(x)=e^x-2>0$（$x>1$），" "\n"
        r"$\quad$ 故 $\varphi(x)>\varphi(1)=e-2>0$，即 $e^x>2x$，从而 $\dfrac{e^x}2>x$．" "\n"
        r"$\quad$ 于是 $\dfrac{e^x(2-\sin x)}2>x$．" "\n"
        r"综上，$\boxed{e^x-\dfrac{e^x\sin x}2>x}$ 对一切 $x>0$ 成立．"
    ),
    'review': (
        r"① ⚠ **（1）中 $a<0$ 时原书详解的单调性写反了**：原书作「$x<a-\frac1a$ 时 $f'(x)>0$（递增）」，"
        r"取 $a=-1$ 检验：$f(x)=-x-\ln(1-x)$，$f'(x)=\frac x{1-x}$，在 $(-\infty,0)$ 上 $f'<0$ 是**递减**．"
        r"本录按正确结论（递减）录入，依据：$a<0$ 时 $a(ax+1)<0$ 且分子递减，故 $x$ 越过零点后 $f'$ 由负变正．" "\n"
        r"② ⭐⭐ **（2）的题干还原**：原文作「$e^x-e^x\sin x_2>x$」，下标/分数线丢失．"
        r"判定为 $e^x-\frac{e^x\sin x}2>x$ 的依据有三：(a) 详解中 $g(0)=-1$，只有 $g(x)=\frac{e^x(\sin x-2)}2$ 才满足；"
        r"(b) 详解导数 $\frac{e^x}2(\sin x+\cos x-2)<0$ 恒成立，与 $g$ 递减一致；(c) 数值检验 $x=1$ 时 $e^x(1-\sin x)=0.43<1$，"
        r"而 $e^x(1-\frac{\sin x}2)=1.575>1$，**只有后者是真命题**．" "\n"
        r"③ ⭐ **（2）必须分 $x\le1$ 与 $x>1$ 两段**：由 $g$ 递减只能得到 $g(x)<-1$，"
        r"而 $-1\le-x$ 仅在 $x\le1$ 时成立；$x>1$ 这一段靠 $e^x>2x$ 补上．原书只写了前一段．" "\n"
        r"④ 数值复核（$h(x)=e^x(1-\frac{\sin x}2)-x$）：$h(0.1)=0.950$，$h(0.5)=0.754$，$h(1)=0.575$，"
        r"$h(1.1)=0.5655$（最小值附近），$h(2)=2.030$，$h(5)=214.6$，全为正 ✓" "\n"
        r"**通法（含 $e^x$ 与三角的不等式）**：" "\n"
        r"① $\sin x+\cos x=\sqrt2\sin\left(x+\frac\pi4\right)$，与常数比较时立刻有界；" "\n"
        r"② $e^x>2x$（$x>1$）、$e^x>x+1$ 是两条常备放缩；" "\n"
        r"③ 分段点常取 $x=1$，因为 $-1\le-x$ 与 $e^x>2x$ 都在此处衔接．"
    ),
    'difficulty': 0.74,
    'topics': ['M-T-168'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-168-V1',
}

T168_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=x\left(e^x-a\right)-a\left(\ln x-a\right)\left(a>0\right)$．" "\n"
        r"（1）若 $a=e$，讨论 $f(x)$ 的单调性；" "\n"
        r"（2）证明：$f(x)\ge2a$．"
    ),
    'stem': [
        r"已知函数 $f(x)=x\left(e^x-a\right)-a\left(\ln x-a\right)\left(a>0\right)$．",
        r"（1）若 $a=e$，讨论 $f(x)$ 的单调性；",
        r"（2）证明：$f(x)\ge2a$．",
    ],
    'opts': [],
    'answer': r"（1）$f(x)$ 在 $(0,1)$ 上单调递减，在 $(1,+\infty)$ 上单调递增；（2）证明见解析",
    'analysis': (
        r"（1）$f'(x)=\dfrac{(x+1)\left(xe^x-a\right)}x$，当 $a=e$ 时由 $y=xe^x-e$ 递增且零点为 $1$ 定号．" "\n"
        r"（2）$g(x)=xe^x-a$ 在 $(0,+\infty)$ 上递增，由 $g(0)=-a<0$、$g(a)>0$ 得唯一零点 $x_0$，"
        r"由 $x_0e^{x_0}=a$ 取对数得 $x_0+\ln x_0=\ln a$，代入 $f(x_0)$ 后化为 $a(a-1-\ln a)\ge0$．"
    ),
    'solution': (
        r"**（1）** $f(x)$ 的定义域为 $(0,+\infty)$，" "\n"
        r"$f'(x)=e^x+xe^x-a-\dfrac ax=\dfrac{x(x+1)e^x-a(x+1)}x=\dfrac{(x+1)\left(xe^x-a\right)}x$．" "\n"
        r"当 $a=e$ 时，$f'(x)=\dfrac{(x+1)\left(xe^x-e\right)}x$．" "\n"
        r"令 $y=xe^x-e$，则 $y'=e^x(x+1)>0$（$x>0$），故 $y$ 在 $(0,+\infty)$ 上递增，且 $x=1$ 时 $y=0$．" "\n"
        r"又 $x+1>0$、$x>0$，所以 $x\in(0,1)$ 时 $f'(x)<0$，$x\in(1,+\infty)$ 时 $f'(x)>0$，" "\n"
        r"即 $\boxed{f(x)\ \text{在}\ (0,1)\ \text{上递减，在}\ (1,+\infty)\ \text{上递增}}$．" "\n"
        r"**（2）证明** $f'(x)=\dfrac{(x+1)\left(xe^x-a\right)}x$，记 $g(x)=xe^x-a$，" "\n"
        r"则 $g'(x)=e^x(x+1)>0$，故 $g(x)$ 在 $(0,+\infty)$ 上递增．" "\n"
        r"由 $g(0)=-a<0$，$g(a)=a\left(e^a-1\right)>0$ 知，存在唯一的 $x_0\in(0,a)$ 使 $g(x_0)=0$，" "\n"
        r"即 $x_0e^{x_0}=a$，两边取对数得 $x_0+\ln x_0=\ln a$．" "\n"
        r"于是 $x\in(0,x_0)$ 时 $f'(x)<0$，$x\in(x_0,+\infty)$ 时 $f'(x)>0$，" "\n"
        r"故 $f(x)\ge f(x_0)=x_0\left(e^{x_0}-a\right)-a\left(\ln x_0-a\right)$" "\n"
        r"$=\left(x_0e^{x_0}-ax_0\right)-a\ln x_0+a^2=a-a\left(x_0+\ln x_0\right)+a^2=a-a\ln a+a^2$．" "\n"
        r"于是 $f(x)-2a\ge a^2-a-a\ln a=a\left(a-1-\ln a\right)$．" "\n"
        r"令 $h(a)=a-1-\ln a$，则 $h'(a)=1-\dfrac1a=\dfrac{a-1}a$，" "\n"
        r"故 $h(a)$ 在 $(0,1)$ 上递减、在 $(1,+\infty)$ 上递增，$h(a)\ge h(1)=0$．" "\n"
        r"所以 $f(x)-2a\ge0$，即 $\boxed{f(x)\ge2a}$．"
    ),
    'review': (
        r"① ⭐⭐ **$f'(x)$ 的因式分解要提出 $(x+1)$**：$f'(x)=(x+1)e^x-a-\frac ax=\frac{(x+1)(xe^x-a)}x$，"
        r"把 $a+\frac ax=a\cdot\frac{x+1}x$ 合成一项，$(x+1)$ 就自然出现了——**这是导数能定号的关键**．" "\n"
        r"② ⭐⭐ **隐零点 $x_0$ 的处理是「取对数」而不是「解出 $x_0$」**：由 $x_0e^{x_0}=a$ 得 $x_0+\ln x_0=\ln a$，"
        r"而 $f(x_0)$ 中恰好出现 $x_0$ 与 $\ln x_0$ 的线性组合 $a(x_0+\ln x_0)$，**整体替换即可，$x_0$ 不用求**．" "\n"
        r"③ ⭐ **区间 $(0,a)$ 的来源**：$g(0)=-a<0$、$g(a)=a(e^a-1)>0$，比「显然」更严谨，也说明 $x_0$ 唯一．" "\n"
        r"④ 数值复核：$a=1$ 时 $x_0=0.567143$（$x_0e^{x_0}=1$），$f(x_0)=2.000000=2a$ ✓ 恰好取等；" "\n"
        r"   $a=0.3$ 时 $f_{\min}=0.751192>0.6=2a$ ✓；$a=2$ 时 $f_{\min}=4.613706>4$ ✓；$a=5$ 时 $21.9528>10$ ✓．" "\n"
        r"   仅 $a=1$ 取等，与 $h(a)\ge h(1)=0$ 完全一致．" "\n"
        r"**通法（$f(x)\ge$ 常数型）**：" "\n"
        r"① 求导并因式分解，找唯一零点 $x_0$（用单调性 + 端点异号）；" "\n"
        r"② 由 $f'(x_0)=0$ 得到替换式，代入 $f(x_0)$ 消去超越部分；" "\n"
        r"③ 余下的关于参数 $a$ 的函数用 $a-1-\ln a\ge0$ 这类基本不等式收口．"
    ),
    'difficulty': 0.75,
    'topics': ['M-T-168'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-168-V2',
}

T362_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知椭圆 $E$ 的中心在坐标原点 $O$，焦点在 $x$ 轴上，左、右焦点分别为 $F_1$、$F_2$，"
        r"离心率 $e=\dfrac{\sqrt2}2$，短轴长为 $2$．" "\n"
        r"（1）求椭圆 $E$ 的标准方程；" "\n"
        r"（2）设过 $F_2$ 且斜率不为零的直线 $l_1$ 与椭圆 $E$ 交于 $M$、$N$ 两点，过 $M$ 作直线 $l_2:x=2$ 的垂线，"
        r"垂足为 $H$，证明：直线 $NH$ 恒过一定点，并求出该定点的坐标；" "\n"
        r"（3）过点 $T\left(0,2\right)$ 作另一直线 $l_3$，与椭圆分别交于 $P$、$Q$ 两点，求 $\dfrac{|TP|}{|TQ|}$ 的取值范围．"
    ),
    'stem': [
        r"已知椭圆 $E$ 的中心在坐标原点 $O$，焦点在 $x$ 轴上，左、右焦点分别为 $F_1$、$F_2$，"
        r"离心率 $e=\dfrac{\sqrt2}2$，短轴长为 $2$．",
        r"（1）求椭圆 $E$ 的标准方程；",
        r"（2）设过 $F_2$ 且斜率不为零的直线 $l_1$ 与椭圆 $E$ 交于 $M$、$N$ 两点，过 $M$ 作直线 $l_2:x=2$ 的垂线，"
        r"垂足为 $H$，证明：直线 $NH$ 恒过一定点，并求出该定点的坐标；",
        r"（3）过点 $T\left(0,2\right)$ 作另一直线 $l_3$，与椭圆分别交于 $P$、$Q$ 两点，求 $\dfrac{|TP|}{|TQ|}$ 的取值范围．",
    ],
    'opts': [],
    'answer': (
        r"（1）$\dfrac{x^2}2+y^2=1$；（2）直线 $NH$ 恒过定点 $\left(\dfrac32,0\right)$；"
        r"（3）$\left[\dfrac13,1\right)\cup\left(1,3\right]$"
    ),
    'analysis': (
        r"（1）由 $2b=2$ 得 $b=1$，由 $e=\frac ca=\frac{\sqrt2}2$ 与 $a^2=b^2+c^2$ 解得 $a=\sqrt2$、$c=1$．" "\n"
        r"（2）设 $l_1:x=ty+1$，联立后用韦达；关键是韦达给出 $2ty_1y_2=y_1+y_2$，"
        r"把直线 $NH$ 的斜率化简后参数 $t$ 完全消失．" "\n"
        r"（3）$\dfrac{|TP|}{|TQ|}=\dfrac{|x_3|}{|x_4|}=u$，用 $\dfrac{(x_3+x_4)^2}{x_3x_4}=u+\dfrac1u$ 化为关于 $k^2$ 的函数，"
        r"再由 $\Delta>0$ 给出 $k^2>\dfrac32$ 定范围；注意斜率不存在时要单独算，它恰好给出闭端点．"
    ),
    'solution': (
        r"**（1）** 设椭圆方程为 $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1\left(a>b>0\right)$．" "\n"
        r"由短轴长为 $2$ 得 $2b=2$，即 $b=1$；由 $e=\dfrac ca=\dfrac{\sqrt2}2$ 得 $c^2=\dfrac{a^2}2$．" "\n"
        r"又 $a^2=b^2+c^2=1+\dfrac{a^2}2$，解得 $a^2=2$，$c^2=1$，即 $c=1$，$F_2\left(1,0\right)$．" "\n"
        r"故 $\boxed{\dfrac{x^2}2+y^2=1}$．" "\n"
        r"**（2）证明** 由 $l_1$ 过 $F_2\left(1,0\right)$ 且斜率不为零，设 $l_1:x=ty+1$．" "\n"
        r"与 $\dfrac{x^2}2+y^2=1$ 联立，化简得 $\left(t^2+2\right)y^2+2ty-1=0$．" "\n"
        r"设 $M\left(x_1,y_1\right)$，$N\left(x_2,y_2\right)$，则 $y_1+y_2=-\dfrac{2t}{t^2+2}$，$y_1y_2=-\dfrac1{t^2+2}$，" "\n"
        r"于是有恒等式 $2ty_1y_2=y_1+y_2$．又 $H\left(2,y_1\right)$，直线 $NH$ 的斜率" "\n"
        r"$k=\dfrac{y_1-y_2}{2-x_2}=\dfrac{y_1-y_2}{2-\left(ty_2+1\right)}=\dfrac{y_1-y_2}{1-ty_2}$．" "\n"
        r"将分子分母同乘 $2y_1$：$k=\dfrac{2y_1\left(y_1-y_2\right)}{2y_1-2ty_1y_2}=\dfrac{2y_1\left(y_1-y_2\right)}{2y_1-\left(y_1+y_2\right)}"
        r"=\dfrac{2y_1\left(y_1-y_2\right)}{y_1-y_2}=2y_1$．" "\n"
        r"故直线 $NH$ 的方程为 $y-y_2=2y_1\left(x-x_2\right)$．" "\n"
        r"又 $y_2=y_1+y_2-y_1$，而 $x_2=ty_2+1$，代入 $x=\dfrac32$ 得" "\n"
        r"$y=y_2+2y_1\left(\dfrac32-ty_2-1\right)=y_2+2y_1\left(\dfrac12-ty_2\right)=y_2+y_1-2ty_1y_2$" "\n"
        r"$=\left(y_1+y_2\right)-\left(y_1+y_2\right)=0$．" "\n"
        r"所以直线 $NH$ 恒过定点 $\boxed{\left(\dfrac32,0\right)}$．" "\n"
        r"**（3）** 若 $l_3$ 的斜率不存在，则 $l_3:x=0$，与椭圆交于 $\left(0,1\right)$、$\left(0,-1\right)$，"
        r"此时 $\dfrac{|TP|}{|TQ|}=\dfrac{2-1}{2-\left(-1\right)}=\dfrac13$ 或 $\dfrac{2-\left(-1\right)}{2-1}=3$．" "\n"
        r"若 $l_3$ 的斜率存在，设 $l_3:y=kx+2$，与椭圆联立得 $\left(2k^2+1\right)x^2+8kx+6=0$．" "\n"
        r"由 $\Delta=64k^2-24\left(2k^2+1\right)=16k^2-24>0$ 得 $k^2>\dfrac32$．" "\n"
        r"设 $P\left(x_3,y_3\right)$，$Q\left(x_4,y_4\right)$，则 $x_3+x_4=-\dfrac{8k}{2k^2+1}$，$x_3x_4=\dfrac6{2k^2+1}>0$．" "\n"
        r"因 $T$ 在 $y$ 轴上，故 $\dfrac{|TP|}{|TQ|}=\dfrac{|x_3|}{|x_4|}$，记 $u=\dfrac{x_3}{x_4}>0$（同号），则" "\n"
        r"$u+\dfrac1u=\dfrac{x_3^2+x_4^2}{x_3x_4}=\dfrac{\left(x_3+x_4\right)^2}{x_3x_4}-2"
        r"=\dfrac{64k^2}{6\left(2k^2+1\right)}-2=\dfrac{20k^2-6}{3\left(2k^2+1\right)}$．" "\n"
        r"令 $\lambda=2k^2+1>4$，则 $k^2=\dfrac{\lambda-1}2$，代入得 $u+\dfrac1u=\dfrac{10\lambda-16}{3\lambda}=\dfrac{10}3-\dfrac{16}{3\lambda}$．" "\n"
        r"当 $\lambda\in\left(4,+\infty\right)$ 时，$u+\dfrac1u\in\left(2,\dfrac{10}3\right)$，" "\n"
        r"其中 $u+\dfrac1u=2$ 给出 $u=1$（取不到），$u+\dfrac1u=\dfrac{10}3$ 给出 $3u^2-10u+3=0$，即 $u=3$ 或 $u=\dfrac13$．" "\n"
        r"故此时 $u\in\left(\dfrac13,1\right)\cup\left(1,3\right)$．综合斜率不存在的情形，" "\n"
        r"$\boxed{\dfrac{|TP|}{|TQ|}\in\left[\dfrac13,1\right)\cup\left(1,3\right]}$．"
    ),
    'review': (
        r"① ⭐⭐ **（2）的灵魂是恒等式 $2ty_1y_2=y_1+y_2$**：由韦达两式相除即得（$\frac{y_1+y_2}{y_1y_2}=2t$），"
        r"它把分母 $1-ty_2$ 中的 $t$ 换成只含 $y$ 的式子，**参数 $t$ 就此消失**．" "\n"
        r"② ⭐ **斜率化简的技巧是「同乘 $2y_1$」**：分母 $1-ty_2$ 乘 $2y_1$ 得 $2y_1-2ty_1y_2=2y_1-(y_1+y_2)=y_1-y_2$，"
        r"与分子的 $y_1-y_2$ 约掉，斜率直接等于 $2y_1$——**比直接代入韦达计算量小一个量级**．" "\n"
        r"③ ⭐⭐ **（3）用 $u+\frac1u$ 而不是直接求 $u$**：比值 $\frac{x_3}{x_4}$ 与 $\frac{x_4}{x_3}$ 对应同一直线的两个方向，"
        r"所以 $u+\frac1u$ 是「对称量」，能由韦达直接表出；最后解方程 $u+\frac1u=c$ 得两个互为倒数的根，正好对应 $P,Q$ 互换．" "\n"
        r"④ ⚠ **斜率不存在的情形不能漏**：$x=0$ 时 $u=\frac13$ 或 $3$，这正是闭区间的两个端点；"
        r"只算斜率存在会得到开区间 $\left(\frac13,1\right)\cup\left(1,3\right)$，答案就错了．" "\n"
        r"⑤ ⚠ **$u\ne1$**：$u=1$ 对应 $|TP|=|TQ|$，即 $T$ 是 $PQ$ 中点，但 $T\left(0,2\right)$ 在椭圆外且不在 $x$ 轴上，"
        r"由 $u+\frac1u>2$（因 $\lambda>4$ 严格）保证 $u\ne1$．" "\n"
        r"⑥ 数值复核（2）：取 $t=0.3,0.7,1.5,-0.4$，分别算出 $N$、$H$ 后求直线在 $x=\frac32$ 处的纵坐标，"
        r"均为 $0.0000000000$ ✓；" "\n"
        r"   数值复核（3）：$k=1.3,1.5,2,3,10$ 对应 $u=0.7128,0.5520,0.4334,0.3732,0.3367$，"
        r"随 $k$ 增大趋近 $\frac13$ ✓，且 $k\to\sqrt{1.5}^{+}$ 时 $u\to1$ ✓" "\n"
        r"**通法（椭圆中的定点与比值范围）**：" "\n"
        r"① 过 $x$ 轴上定点的直线设成 $x=ty+x_0$，可避免斜率不存在的讨论；" "\n"
        r"② 定点问题：把直线方程写成 $y=k(x-x_0)+y_0$ 的形式，令参数的系数恒为零；" "\n"
        r"③ 比值范围：用 $u+\frac1u$ 转化，注意判别式给定义域、端点情形单独算．"
    ),
    'difficulty': 0.78,
    'topics': ['M-T-362'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-362-V1',
}

T362_V2 = {
    'type': '解答',
    'stem_text': (
        r"（广东华侨中学 2022 届高三上学期 9 月月考数学试题）已知椭圆 $C:\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1\left(a>b>0\right)$ 的"
        r"左、右顶点分别为 $A_1$、$A_2$，右焦点为 $F_2\left(1,0\right)$，点 $B\left(1,\dfrac32\right)$ 在椭圆上．" "\n"
        r"（1）求椭圆 $C$ 的方程；" "\n"
        r"（2）若直线 $l:y=k\left(x-4\right)\left(k\ne0\right)$ 与椭圆 $C$ 交于 $M$、$N$ 两点，"
        r"已知直线 $A_1M$ 与 $A_2N$ 相交于点 $G$，证明：点 $G$ 在定直线上，并求出此定直线的方程．"
    ),
    'stem': [
        r"（广东华侨中学 2022 届高三上学期 9 月月考数学试题）已知椭圆 $C:\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1\left(a>b>0\right)$ 的"
        r"左、右顶点分别为 $A_1$、$A_2$，右焦点为 $F_2\left(1,0\right)$，点 $B\left(1,\dfrac32\right)$ 在椭圆上．",
        r"（1）求椭圆 $C$ 的方程；",
        r"（2）若直线 $l:y=k\left(x-4\right)\left(k\ne0\right)$ 与椭圆 $C$ 交于 $M$、$N$ 两点，"
        r"已知直线 $A_1M$ 与 $A_2N$ 相交于点 $G$，证明：点 $G$ 在定直线上，并求出此定直线的方程．",
    ],
    'opts': [],
    'answer': r"（1）$\dfrac{x^2}4+\dfrac{y^2}3=1$；（2）点 $G$ 在定直线 $x=1$ 上",
    'analysis': (
        r"（1）由 $c=1$ 与 $\dfrac1{a^2}+\dfrac{9}{4b^2}=1$、$a^2=b^2+1$ 解得 $a=2$、$b=\sqrt3$．" "\n"
        r"（2）先由对称性（取 $l$ 过上顶点的特殊位置）猜出定直线为 $x=1$；"
        r"再对一般位置，把「$x=1$ 时两直线纵坐标相等」整理成 $2x_1x_2-5\left(x_1+x_2\right)+8=0$，代入韦达恒为 $0$．"
    ),
    'solution': (
        r"**（1）** 由 $F_2\left(1,0\right)$ 得 $c=1$，故 $a^2=b^2+1$．" "\n"
        r"又 $B\left(1,\dfrac32\right)$ 在椭圆上，$\dfrac1{a^2}+\dfrac{9}{4b^2}=1$．" "\n"
        r"代入 $a^2=b^2+1$ 得 $\dfrac1{b^2+1}+\dfrac9{4b^2}=1$，即 $4b^2+9\left(b^2+1\right)=4b^2\left(b^2+1\right)$，" "\n"
        r"整理得 $4b^4-9b^2-9=0$，解得 $b^2=3$（负根舍去），于是 $a^2=4$．" "\n"
        r"故 $\boxed{\dfrac{x^2}4+\dfrac{y^2}3=1}$．" "\n"
        r"**（2）证明** $A_1\left(-2,0\right)$，$A_2\left(2,0\right)$．" "\n"
        r"设 $M\left(x_1,y_1\right)$，$N\left(x_2,y_2\right)$，由 $\begin{cases}y=k\left(x-4\right)\\[2pt]\dfrac{x^2}4+\dfrac{y^2}3=1\end{cases}$" "\n"
        r"整理得 $\left(3+4k^2\right)x^2-32k^2x+64k^2-12=0$，" "\n"
        r"故 $x_1+x_2=\dfrac{32k^2}{3+4k^2}$，$x_1x_2=\dfrac{64k^2-12}{3+4k^2}$．" "\n"
        r"直线 $A_1M:y=\dfrac{y_1}{x_1+2}\left(x+2\right)$，直线 $A_2N:y=\dfrac{y_2}{x_2-2}\left(x-2\right)$．" "\n"
        r"令 $x=1$，两式分别给出 $y=\dfrac{3y_1}{x_1+2}$ 与 $y=\dfrac{-y_2}{x_2-2}$．" "\n"
        r"只需证 $\dfrac{3y_1}{x_1+2}=\dfrac{-y_2}{x_2-2}$，即 $3y_1\left(x_2-2\right)=-y_2\left(x_1+2\right)$．" "\n"
        r"由 $y_i=k\left(x_i-4\right)$ 且 $k\ne0$，两边约去 $k$ 得" "\n"
        r"$3\left(x_1-4\right)\left(x_2-2\right)=-\left(x_2-4\right)\left(x_1+2\right)$，" "\n"
        r"展开整理得 $4x_1x_2-10\left(x_1+x_2\right)+16=0$，即 $2x_1x_2-5\left(x_1+x_2\right)+8=0$．" "\n"
        r"代入韦达：" "\n"
        r"$2\cdot\dfrac{64k^2-12}{3+4k^2}-5\cdot\dfrac{32k^2}{3+4k^2}+8=\dfrac{128k^2-24-160k^2+8\left(3+4k^2\right)}{3+4k^2}$" "\n"
        r"$=\dfrac{128k^2-24-160k^2+24+32k^2}{3+4k^2}=0$．" "\n"
        r"故两直线在 $x=1$ 处的纵坐标恒相等，即交点 $G$ 恒在定直线 $\boxed{x=1}$ 上．"
    ),
    'review': (
        r"① ⭐⭐ **「先猜后证」是最省力的路线**：取 $l$ 过椭圆上顶点这一特殊位置，"
        r"$M\left(0,\sqrt3\right)$、$N\left(\frac85,\frac{3\sqrt3}5\right)$，两直线交点恰为 $\left(1,\frac{3\sqrt3}2\right)$，"
        r"**横坐标 $1$ 一眼看出**；再对一般位置验证 $x=1$ 时纵坐标相等即可．" "\n"
        r"② ⭐⭐ **验证式的整理要盯住「只含 $x_1+x_2$ 与 $x_1x_2$」**："
        r"$3y_1(x_2-2)+y_2(x_1+2)=0$ 代入 $y_i=k(x_i-4)$ 后展开，$x_1x_2$ 项合并为 $4x_1x_2$、"
        r"$x_1$ 与 $x_2$ 的一次项合并为 $-10(x_1+x_2)$（**系数相同才能合并，这本身就是检验点**）．" "\n"
        r"③ ⭐ **约去 $k$ 前要确认 $k\ne0$**：题设已给 $k\ne0$（否则 $l$ 是 $y=0$，与椭圆交于两顶点，"
        r"此时 $A_1M$ 退化），所以可以放心约．" "\n"
        r"④ 数值复核：取 $k=0.2,0.5,-0.3$，分别解出 $M,N$ 后求 $A_1M$ 与 $A_2N$ 的交点横坐标，"
        r"均为 $1.00000000$ ✓" "\n"
        r"⑤ ⚠ 注意（1）中方程是 $4b^4-9b^2-9=0$，解得 $b^2=3$（另一根 $b^2=-\frac34$ 舍去），"
        r"不要误算成 $b^2=\frac34$——这样会得到 $a^2=\frac74<c^2$，与椭圆矛盾．" "\n"
        r"**通法（两线交点在定直线上）**：" "\n"
        r"① 先取特殊位置（顶点、中点、垂直/水平）猜出定直线；" "\n"
        r"② 一般位置把「交点在 $x=x_0$ 上」翻译成两直线在 $x=x_0$ 处纵坐标相等；" "\n"
        r"③ 用 $y_i=k(x_i-t)$ 代入，整理成对称式后代入韦达，分子恒为零即证．"
    ),
    'difficulty': 0.76,
    'topics': ['M-T-362'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-362-V2',
}

T362_V3 = {
    'type': '解答',
    'stem_text': (
        r"如图，在平面直角坐标系 $xOy$ 中，椭圆 $C:\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1\left(a>b>0\right)$ 的离心率为 $\dfrac{\sqrt3}2$，"
        r"点 $A$、$B$ 分别为椭圆 $C$ 的上顶点、右顶点，过坐标原点的直线交椭圆 $C$ 于 $D$、$E$ 两点，"
        r"交 $AB$ 于 $M$ 点，其中点 $E$ 在第一象限，设直线 $DE$ 的斜率为 $k$．" "\n"
        r"（1）当 $k=\dfrac12$ 时，证明直线 $DE$ 平分线段 $AB$；" "\n"
        r"（2）已知点 $A\left(0,1\right)$，则：" "\n"
        r"①若 $S_{\triangle ADM}=6S_{\triangle AEM}$，求 $k$；" "\n"
        r"②求四边形 $ADBE$ 面积的最大值．"
    ),
    'stem': [
        r"如图，在平面直角坐标系 $xOy$ 中，椭圆 $C:\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1\left(a>b>0\right)$ 的离心率为 $\dfrac{\sqrt3}2$，"
        r"点 $A$、$B$ 分别为椭圆 $C$ 的上顶点、右顶点，过坐标原点的直线交椭圆 $C$ 于 $D$、$E$ 两点，"
        r"交 $AB$ 于 $M$ 点，其中点 $E$ 在第一象限，设直线 $DE$ 的斜率为 $k$．",
        r"（1）当 $k=\dfrac12$ 时，证明直线 $DE$ 平分线段 $AB$；",
        r"（2）已知点 $A\left(0,1\right)$，则：",
        r"①若 $S_{\triangle ADM}=6S_{\triangle AEM}$，求 $k$；",
        r"②求四边形 $ADBE$ 面积的最大值．",
    ],
    'opts': [],
    'answer': r"（1）证明见解析；（2）①$k=\dfrac23$ 或 $k=\dfrac38$；②$2\sqrt2$",
    'analysis': (
        r"（1）由 $e=\frac{\sqrt3}2$ 得 $\frac{b^2}{a^2}=\frac14$ 即 $a=2b$，故 $AB$ 中点 $\left(\frac a2,\frac b2\right)$ 与原点连线的斜率为 $\frac ba=\frac12$，"
        r"与 $k=\frac12$ 一致，即中点在 $DE$ 上．" "\n"
        r"（2）①由面积比得 $DM=6ME$，用横坐标表为 $7x_0=5x_1$，再分别联立 $DE$ 与椭圆、$DE$ 与 $AB$ 解出 $x_1$、$x_0$；" "\n"
        r"②四边形面积 $=\dfrac12|DE|\left(d_A+d_B\right)$，化为 $x_1+2y_1$，用柯西（或基本不等式）得最大 $2\sqrt2$．"
    ),
    'solution': (
        r"**（1）证明** 由 $e=\dfrac ca=\dfrac{\sqrt3}2$ 得 $\dfrac{c^2}{a^2}=\dfrac34$，" "\n"
        r"又 $c^2=a^2-b^2$，故 $\dfrac{b^2}{a^2}=\dfrac14$，即 $a=2b$．" "\n"
        r"于是 $A\left(0,b\right)$、$B\left(a,0\right)$，$AB$ 的中点为 $\left(\dfrac a2,\dfrac b2\right)$．" "\n"
        r"由 $a=2b$ 得 $\dfrac{b/2}{a/2}=\dfrac ba=\dfrac12$，故中点在直线 $y=\dfrac12x$ 上．" "\n"
        r"当 $k=\dfrac12$ 时 $DE$ 就是 $y=\dfrac12x$，它过 $AB$ 的中点，即 $\boxed{DE\ \text{平分线段}\ AB}$．" "\n"
        r"**（2）** 由 $A\left(0,1\right)$ 得 $b=1$，$a=2$，椭圆为 $\dfrac{x^2}4+y^2=1$，$B\left(2,0\right)$，" "\n"
        r"直线 $AB:x+2y=2$，直线 $DE:y=kx\left(k>0\right)$．设 $E\left(x_1,y_1\right)$、$M\left(x_0,y_0\right)$，则 $D\left(-x_1,-y_1\right)$．" "\n"
        r"**①** $\triangle ADM$ 与 $\triangle AEM$ 有公共顶点 $A$ 且底边 $DM$、$ME$ 共线，" "\n"
        r"故 $S_{\triangle ADM}=6S_{\triangle AEM}\iff DM=6ME$．用横坐标表示（三点共线）得" "\n"
        r"$x_0-\left(-x_1\right)=6\left(x_1-x_0\right)$，即 $\boxed{7x_0=5x_1}$．" "\n"
        r"由 $E$ 在椭圆与 $y=kx$ 上：$\dfrac{x_1^2}4+k^2x_1^2=1$，得 $x_1=\dfrac2{\sqrt{1+4k^2}}$；" "\n"
        r"由 $M$ 在 $AB$ 与 $y=kx$ 上：$x_0+2kx_0=2$，得 $x_0=\dfrac2{1+2k}$．" "\n"
        r"代入 $7x_0=5x_1$ 得 $\dfrac{14}{1+2k}=\dfrac{10}{\sqrt{1+4k^2}}$，即 $7\sqrt{1+4k^2}=5\left(1+2k\right)$．" "\n"
        r"两边平方：$49\left(1+4k^2\right)=25\left(1+4k+4k^2\right)$，整理得 $96k^2-100k+24=0$，" "\n"
        r"即 $24k^2-25k+6=0$，亦即 $\left(3k-2\right)\left(8k-3\right)=0$，" "\n"
        r"解得 $\boxed{k=\dfrac23\ \text{或}\ k=\dfrac38}$（均满足 $k>0$ 与平方后的等价性）．" "\n"
        r"**②** 四边形 $ADBE$ 的面积 $S=S_{\triangle ADE}+S_{\triangle DEB}$．" "\n"
        r"$|DE|=2\sqrt{x_1^2+y_1^2}$，直线 $DE:kx-y=0$，" "\n"
        r"$d_A=\dfrac{1}{\sqrt{1+k^2}}$，$d_B=\dfrac{2k}{\sqrt{1+k^2}}$（$k>0$），故" "\n"
        r"$S=\dfrac12\cdot2\sqrt{x_1^2+y_1^2}\cdot\dfrac{1+2k}{\sqrt{1+k^2}}$．" "\n"
        r"由 $x_1=\dfrac2{\sqrt{1+4k^2}}$、$y_1=kx_1$ 得 $\sqrt{x_1^2+y_1^2}=\dfrac{2\sqrt{1+k^2}}{\sqrt{1+4k^2}}$，于是" "\n"
        r"$S=\dfrac{2\left(1+2k\right)}{\sqrt{1+4k^2}}$．" "\n"
        r"（也可写成 $S=x_1+2y_1=\dfrac{2+4k}{\sqrt{1+4k^2}}$，两式恒等．）" "\n"
        r"由柯西不等式 $x_1+2y_1=2\cdot\dfrac{x_1}2+2\cdot y_1\le\sqrt{\left(4+4\right)\left(\dfrac{x_1^2}4+y_1^2\right)}=2\sqrt2$，" "\n"
        r"当且仅当 $\dfrac{x_1}2:y_1=2:2$，即 $x_1=2y_1$ 时取等，此时 $k=\dfrac{y_1}{x_1}=\dfrac12$．" "\n"
        r"故四边形 $ADBE$ 面积的最大值为 $\boxed{2\sqrt2}$．"
    ),
    'review': (
        r"① ⭐⭐ **（1）的本质是 $e=\frac{\sqrt3}2\iff a=2b$**："
        r"于是 $AB$ 中点 $\left(\frac a2,\frac b2\right)$ 与原点的连线斜率恰为 $\frac ba=\frac12$，"
        r"**离心率给出的比例关系直接决定了「平分」的斜率**，不用算坐标．" "\n"
        r"② ⭐⭐ **（2）① 的 $DM=6ME$ 要转成横坐标关系**：三点共线（都在 $DE$ 上），故线段比 = 横坐标差之比，"
        r"$x_0+x_1=6(x_1-x_0)\Rightarrow7x_0=5x_1$．**注意 $D$ 的横坐标是 $-x_1$（中心对称），不是 $x_1$**．" "\n"
        r"③ ⚠ **$x_1=\frac2{\sqrt{1+4k^2}}$ 而不是 $\frac4{1+4k^2}$**：由 $\frac{x_1^2}4+k^2x_1^2=1$ 得 $x_1^2=\frac4{1+4k^2}$，"
        r"还要再开方；原书在分析中把 $x_1^2$ 与 $x_1$ 混写了．" "\n"
        r"④ ⭐ **（2）② 的两种算法要会互推**：距离和法给 $\frac{2(1+2k)}{\sqrt{1+4k^2}}$，"
        r"而 $x_1+2y_1=\frac{2+4k}{\sqrt{1+4k^2}}$ 与之恒等；前者几何意义清楚，后者能直接用柯西取等．" "\n"
        r"⑤ ⭐ **取等条件 $x_1=2y_1$ 即 $k=\frac12$，与（1）的 $k=\frac12$ 是同一个位置** ——"
        r"这是命题人把两问串起来的暗线，也可作为自检信号．" "\n"
        r"⑥ 数值复核：①$k=\frac23$ 时 $7x_0=6.000000$、$5x_1=6.000000$ ✓；$k=\frac38$ 时两者均为 $8.000000$ ✓；" "\n"
        r"   ②$k=0.5$ 时 $S=2.828427=2\sqrt2$ ✓，$k=\frac23$ 与 $\frac38$ 时 $S=2.800000$ ✓，$k=0.2$ 时 $2.599735$ ✓，" "\n"
        r"   两种算法给出的值逐位相同 ✓" "\n"
        r"**通法（过原点的弦与顶点连线）**：" "\n"
        r"① 过原点的弦 ⟹ 两端点关于原点对称，$D=-E$，未知量减半；" "\n"
        r"② 共线的线段比 ⟹ 用横坐标（或纵坐标）之比，避开距离公式；" "\n"
        r"③ 面积最值 ⟹ 拆成两个三角形用「公共底 $\times$ 距离和」，或直接用椭圆的参数/柯西．"
    ),
    'difficulty': 0.80,
    'topics': ['M-T-362'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-362-V3',
}

# 注：T260_V1 与本批一同入库后发现与第 85 批的 M-H0871 重复（同一道题），
# 已从 bank.json 中删除新入库的那条，故此处也从 QS 移除，重跑不会重复入库。
QS = [
    T260_E1, T260_V2, T260_V3,
    T168_E1, T168_V1, T168_V2,
    T362_V1, T362_V2, T362_V3,
]
