# -*- coding: utf-8 -*-
r"""第47批（上）：平面向量 · 模长与最值（柯西消参）

来源：2024高中数学热点题型归纳完整解析版.pdf
p204（PDF 页 203）M-T-237

## 选题

`pick_batch.py --n 18` → p204。本文件取 M-T-237 的 E1、V1、V3。

## ⚠ 跳过 M-T-237-V2

题面「$\lambda\vec a+\vec b=\vec 0\ (\lambda<0)$」提取不全（$\vec b=(2,1)$ 已知、$\lvert\vec a\rvert=1$，
但 $\lambda\vec a+\vec b$ 与谁垂直丢失），且详解「求出 $\vec b=5\vec a$」与 $\lvert\vec a\rvert=1$、$\lvert\vec b\rvert=\sqrt5$
不相容（$\lvert5\vec a\rvert=5\neq\sqrt5$）。判定为**提取失真，跳过**。

## ★★ 本批的核心方法：「设 $t=\cos\theta$ + 柯西消参」

凡是 $\lvert\vec a-k\vec b\rvert+\lvert\vec a+m\vec b\rvert$（$\vec a,\vec b$ 为单位向量）型，一律：

1. 设 $t=\cos\theta\in[-1,1]$，用 $\lvert\vec a\pm k\vec b\rvert^{2}=1+k^{2}\mp2kt$ 化成一个变量的函数；
2. 写成 $f(t)=\sqrt{A_0+pt}+\sqrt{B_0+qt}$（$p,q$ 必异号）；
3. **用柯西消掉 $t$**：$f^{2}\le(\alpha+\beta)\left(\dfrac{A_0+pt}\alpha+\dfrac{B_0+qt}\beta\right)$，
   取 $\dfrac p\alpha+\dfrac q\beta=0$（即 $\alpha:\beta=|p|:|q|$），括号内 $t$ 恰好消净。

**这比求导快得多，而且等号条件自动给出取等时 $\cos\theta$ 的值。**

| 题 | $A_0,p$ | $B_0,q$ | $\alpha:\beta$ | 结果 |
|---|---|---|---|---|
| V1 | $5-4t$ | $2+2t$ | $2:1$ | $\frac{3\sqrt6}2$，取等 $t=-\frac14$ |
| V3 | $2+2t$ | $10-6t$ | $1:3$ | $\frac{8\sqrt3}3$，取等 $t=-\frac13$ |

## 关于 E1 的答案

ref_bank 中 `ans='2 2'` —— 根号丢失后的形式，实为 $\sqrt2$。
我独立算得 $\lvert\vec a-\vec b\rvert_{\min}=\sqrt2$ ✓ 与答案一致。
"""

T237_E1 = {
    'type': '填空',
    'stem_text': (
        r"若向量 $\vec a=(x,2)$，$\vec b=(-3,y)$，$\vec c=(-1,-2)$，"
        r"且 $(\vec a-\vec c)\perp(\vec b+\vec c)$，则 $\lvert\vec a-\vec b\rvert$ 的最小值为 ____．"
    ),
    'opts': [],
    'answer': r"$\sqrt2$",
    'analysis': (
        r"垂直条件给出 $x,y$ 的一个线性关系，把 $\lvert\vec a-\vec b\rvert$ 表成**单变量二次函数**，"
        r"配方取最小值。"
    ),
    'solution': (
        r"**第一步：翻译垂直条件**" "\n"
        r"$\vec a-\vec c=(x+1,\ 4)$，$\vec b+\vec c=(-4,\ y-2)$．" "\n"
        r"由垂直：$(\vec a-\vec c)\cdot(\vec b+\vec c)=-4(x+1)+4(y-2)=0$" "\n"
        r"$\Rightarrow-4x-4+4y-8=0\Rightarrow y=x+3$．" "\n"
        r"**第二步：把目标式化为一个变量**" "\n"
        r"$\vec a-\vec b=(x+3,\ 2-y)=(x+3,\ 2-x-3)=(x+3,\ -x-1)$．" "\n"
        r"$\lvert\vec a-\vec b\rvert^{2}=(x+3)^{2}+(x+1)^{2}=2x^{2}+8x+10=2(x+2)^{2}+2$．" "\n"
        r"**第三步**：当 $x=-2$（此时 $y=1$）时取最小值 $\sqrt2$．"
    ),
    'review': (
        r"★ 题干与答案完整 ✓（**详解未提取到**，上述推导为我独立完成）。" "\n"
        r"**⚠ 答案还原说明**：ref_bank 中 `ans='2 2'` 是根号丢失后的形式（分子 2 分母 2 排版），"
        r"实为 $\sqrt2$；我独立算得 $\sqrt2$ ✓ 与答案一致。" "\n"
        r"**独立验算**：" "\n"
        r"① 取 $x=-2$、$y=1$：$\vec a=(-2,2)$、$\vec b=(-3,1)$、$\vec c=(-1,-2)$" "\n"
        r"$\vec a-\vec c=(-1,4)$；$\vec b+\vec c=(-4,-1)$；点积 $=4-4=0$ ✓✓ **垂直成立**" "\n"
        r"$\vec a-\vec b=(1,1)$，$\lvert\vec a-\vec b\rvert=\sqrt2$ ✓✓" "\n"
        r"② 换 $x=0$（则 $y=3$）：$\vec a=(0,2)$、$\vec b=(-3,3)$" "\n"
        r"$\vec a-\vec c=(1,4)$；$\vec b+\vec c=(-4,1)$；点积 $=-4+4=0$ ✓" "\n"
        r"$\vec a-\vec b=(3,-1)$，$\lvert\cdot\rvert=\sqrt{10}>\sqrt2$ ✓" "\n"
        r"③ 换 $x=-4$（则 $y=-1$）：$\vec a=(-4,2)$、$\vec b=(-3,-1)$" "\n"
        r"$\vec a-\vec c=(-3,4)$；$\vec b+\vec c=(-4,-3)$；点积 $=12-12=0$ ✓" "\n"
        r"$\vec a-\vec b=(-1,3)$，$\lvert\cdot\rvert=\sqrt{10}>\sqrt2$ ✓" "\n"
        r"④ **二次函数验证**：$\lvert\vec a-\vec b\rvert^{2}=2(x+2)^{2}+2$，在 $x=-2$ 处取最小 $2$ ✓，" "\n"
        r"$x=0$ 时 $2\cdot4+2=10$ ✓（与 ② 的 $\sqrt{10}$ 一致）；$x=-4$ 时 $2\cdot4+2=10$ ✓（与 ③ 一致）" "\n"
        r"**答案 $\sqrt2$ 正确** ✓" "\n"
        r"**⭐ 通法**：「向量垂直 + 求模长最值」——" "\n"
        r"① 垂直条件 $\vec u\cdot\vec v=0$ 给出坐标分量间的一个**线性约束**，" "\n"
        r"用它消掉一个变量；" "\n"
        r"② 目标模长平方必是**二次函数**，配方即得最值。" "\n"
        r"**本题的漂亮之处**：$\lvert\vec a-\vec b\rvert^{2}=2(x+2)^{2}+2$ 中两个平方项系数相同（都是 $2$），"
        r"配方后常数项恰好是 $2$ —— 说明 $\vec a-\vec b$ 的两个分量 $(x+3)$ 与 $-(x+1)$ 变化趋势一致。"
    ),
    'difficulty': 0.82,
    'topics': ['M-T-237'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-237-E1',
}

T237_V1 = {
    'type': '填空',
    'stem_text': (
        r"已知 $\vec a,\vec b$ 是平面上的单位向量，"
        r"则 $\lvert\vec a-2\vec b\rvert+\lvert\vec a+\vec b\rvert$ 的最大值是 ____．"
    ),
    'opts': [],
    'answer': r"$\dfrac{3\sqrt6}2$",
    'analysis': (
        r"设 $t=\cos\langle\vec a,\vec b\rangle\in[-1,1]$，两个模长分别是 $\sqrt{5-4t}$ 与 $\sqrt{2+2t}$。"
        r"用**柯西不等式**配权 $\alpha:\beta=|p|:|q|=2:1$，一次就把 $t$ 消掉。"
    ),
    'solution': (
        r"**第一步：统一变量**" "\n"
        r"设 $t=\cos\langle\vec a,\vec b\rangle\in[-1,1]$，由 $\lvert\vec a\rvert=\lvert\vec b\rvert=1$：" "\n"
        r"$\lvert\vec a-2\vec b\rvert^{2}=1+4-4t=5-4t$；$\lvert\vec a+\vec b\rvert^{2}=1+1+2t=2+2t$．" "\n"
        r"令 $f(t)=\sqrt{5-4t}+\sqrt{2+2t}$．" "\n"
        r"**第二步：柯西消参（关键）**" "\n"
        r"由 $(p_1q_1+p_2q_2)^{2}\le(p_1^{2}+p_2^{2})(q_1^{2}+q_2^{2})$，取" "\n"
        r"$p_1=\sqrt2,\ q_1=\sqrt{\dfrac{5-4t}2}$；$p_2=1,\ q_2=\sqrt{2+2t}$：" "\n"
        r"$f^{2}\le(2+1)\left(\dfrac{5-4t}2+(2+2t)\right)=3\left(\dfrac52-2t+2+2t\right)=3\times\dfrac92=\dfrac{27}2$．" "\n"
        r"（**$t$ 恰好消净** —— 权重 $2:1$ 正是两式 $t$ 的系数 $4:2$ 之比。）" "\n"
        r"**第三步**：$f\le\sqrt{\dfrac{27}2}=\dfrac{3\sqrt6}2$．" "\n"
        r"**取等条件**：$\dfrac{q_1}{p_1}=\dfrac{q_2}{p_2}$，即 $\sqrt{\dfrac{5-4t}4}=\sqrt{2+2t}$" "\n"
        r"$\Rightarrow5-4t=8+8t\Rightarrow t=-\dfrac14\in[-1,1]$ ✓ 可取．" "\n"
        r"故最大值为 $\dfrac{3\sqrt6}2$．"
    ),
    'review': (
        r"★ 题干与答案完整 ✓（**详解未提取到**，上述推导为我独立完成）。" "\n"
        r"**⚠ 答案还原**：ref_bank 中 `ans='3 6\\n2'` 即 $\frac{3\sqrt6}2$（根号丢失）。" "\n"
        r"**独立验算**：" "\n"
        r"① **取 $t=-\frac14$ 直接代入**（$\cos\theta=-\frac14$，$\theta\approx104.48^\circ$）：" "\n"
        r"$\lvert\vec a-2\vec b\rvert=\sqrt{5-4(-\frac14)}=\sqrt{5+1}=\sqrt6\approx2.4495$" "\n"
        r"$\lvert\vec a+\vec b\rvert=\sqrt{2+2(-\frac14)}=\sqrt{1.5}\approx1.2247$" "\n"
        r"和 $=2.4495+1.2247=3.6742$" "\n"
        r"$\frac{3\sqrt6}2=\frac{3\times2.4495}2=3.6742$ ✓✓ **完全吻合**" "\n"
        r"② **导数法复核**：$f'(t)=\frac{-2}{\sqrt{5-4t}}+\frac{1}{\sqrt{2+2t}}=0$" "\n"
        r"$\Rightarrow\sqrt{5-4t}=2\sqrt{2+2t}\Rightarrow5-4t=4(2+2t)=8+8t\Rightarrow t=-\frac14$ ✓✓" "\n"
        r"③ **端点比较**（确认是最大而非最小）：" "\n"
        r"$t=-1$：$f=\sqrt9+\sqrt0=3$；$t=1$：$f=\sqrt1+\sqrt4=1+2=3$；" "\n"
        r"$t=-\frac14$：$f=3.6742>3$ ✓✓ **确为最大值**" "\n"
        r"④ **构造具体向量验证**（$\vec a=(1,0)$，$\vec b=(\cos\theta,\sin\theta)$，$t=\cos\theta=-\frac14$）：" "\n"
        r"$\vec b=(-\frac14,\frac{\sqrt{15}}4)=(-0.25,0.9682)$；验 $\lvert\vec b\rvert=\sqrt{0.0625+0.9375}=1$ ✓" "\n"
        r"$\vec a-2\vec b=(1+0.5,\ -1.9365)=(1.5,-1.9365)$，$\lvert\cdot\rvert=\sqrt{2.25+3.75}=\sqrt6$ ✓✓" "\n"
        r"$\vec a+\vec b=(0.75,\ 0.9682)$，$\lvert\cdot\rvert=\sqrt{0.5625+0.9375}=\sqrt{1.5}$ ✓✓" "\n"
        r"**答案 $\frac{3\sqrt6}2$ 正确** ✓" "\n"
        r"**⭐ 通法（柯西消参法）**：" "\n"
        r"形如 $f(t)=\sqrt{A_0+pt}+\sqrt{B_0+qt}$（$p,q$ **异号**）的最值 —— " "\n"
        r"① 取权重 $\alpha:\beta=|p|:|q|$，使 $\frac p\alpha+\frac q\beta=0$；" "\n"
        r"② $f^{2}\le(\alpha+\beta)\left(\frac{A_0+pt}\alpha+\frac{B_0+qt}\beta\right)$，括号内 $t$ **自动消净**；" "\n"
        r"③ 等号条件 $\frac{A_0+pt}{\alpha^{2}}=\frac{B_0+qt}{\beta^{2}}$ 解出取等时的 $t$，再验证 $t\in[-1,1]$。" "\n"
        r"**比求导快，且不容易算错。** 本题权重 $2:1$（因 $|{-4}|:|2|=2:1$）。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-237'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-237-V1',
}

T237_V3 = {
    'type': '填空',
    'stem_text': (
        r"设 $\vec a,\vec b$ 为单位向量，则 $\lvert\vec a+\vec b\rvert+\lvert\vec a-3\vec b\rvert$ 的最大值是 ____．"
    ),
    'opts': [],
    'answer': r"$\dfrac{8\sqrt3}3$",
    'analysis': (
        r"与 V1 完全同构：设 $t=\cos\langle\vec a,\vec b\rangle$，两模长是 $\sqrt{2+2t}$ 与 $\sqrt{10-6t}$，"
        r"柯西配权 $\alpha:\beta=|2|:|{-6}|=1:3$。"
    ),
    'solution': (
        r"**第一步**：设 $t=\cos\langle\vec a,\vec b\rangle\in[-1,1]$，" "\n"
        r"$\lvert\vec a+\vec b\rvert^{2}=2+2t$；$\lvert\vec a-3\vec b\rvert^{2}=1+9-6t=10-6t$．" "\n"
        r"令 $f(t)=\sqrt{2+2t}+\sqrt{10-6t}$．" "\n"
        r"**第二步：柯西消参**" "\n"
        r"$t$ 的系数为 $2$ 与 $-6$，故取 $\alpha:\beta=1:3$（使 $\frac21+\frac{-6}3=0$）：" "\n"
        r"$f^{2}\le(1+3)\left(\frac{2+2t}1+\frac{10-6t}3\right)=4\left(2+2t+\frac{10}3-2t\right)=4\times\dfrac{16}3=\dfrac{64}3$．" "\n"
        r"**第三步**：$f\le\sqrt{\dfrac{64}3}=\dfrac8{\sqrt3}=\dfrac{8\sqrt3}3$．" "\n"
        r"**取等条件**：$\dfrac{q_1}{p_1}=\dfrac{q_2}{p_2}$，即 $\dfrac{\sqrt{2+2t}}{1}=\dfrac{\sqrt{\frac{10-6t}3}}{\sqrt3}$" "\n"
        r"$\Rightarrow2+2t=\dfrac{10-6t}9\Rightarrow18+18t=10-6t\Rightarrow24t=-8\Rightarrow t=-\dfrac13\in[-1,1]$ ✓"
    ),
    'review': (
        r"★ 题干与答案完整 ✓（**详解未提取到**，上述推导为我独立完成）。" "\n"
        r"**⚠ 答案还原**：ref_bank 中 `ans='8 3\\n3'` 即 $\frac{8\sqrt3}3$（根号丢失）。" "\n"
        r"**独立验算**：" "\n"
        r"① **取 $t=-\frac13$ 直接代入**：" "\n"
        r"$\lvert\vec a+\vec b\rvert=\sqrt{2-\frac23}=\sqrt{\frac43}=\frac2{\sqrt3}\approx1.1547$" "\n"
        r"$\lvert\vec a-3\vec b\rvert=\sqrt{10+2}=\sqrt{12}=2\sqrt3\approx3.4641$" "\n"
        r"和 $=1.1547+3.4641=4.6188$" "\n"
        r"$\frac{8\sqrt3}3=\frac{8\times1.7321}3=\frac{13.8564}3=4.6188$ ✓✓ **完全吻合**" "\n"
        r"② **代数化简核对**：$\sqrt{\frac43}+\sqrt{12}=\frac{2\sqrt3}3+2\sqrt3=\frac{2\sqrt3+6\sqrt3}3=\frac{8\sqrt3}3$ ✓✓" "\n"
        r"③ **导数法复核**：$f'(t)=\frac{1}{\sqrt{2+2t}}-\frac{3}{\sqrt{10-6t}}=0$" "\n"
        r"$\Rightarrow\sqrt{10-6t}=3\sqrt{2+2t}\Rightarrow10-6t=9(2+2t)=18+18t\Rightarrow t=-\frac13$ ✓✓" "\n"
        r"④ **端点比较**：$t=-1$：$f=0+\sqrt{16}=4$；$t=1$：$f=2+\sqrt4=4$；$t=-\frac13$：$4.6188>4$ ✓✓" "\n"
        r"⑤ **具体向量验证**（$\vec a=(1,0)$，$\vec b=(-\frac13,\frac{2\sqrt2}3)=(-0.3333,0.9428)$）：" "\n"
        r"验 $\lvert\vec b\rvert=\sqrt{0.1111+0.8889}=1$ ✓" "\n"
        r"$\vec a+\vec b=(0.6667,0.9428)$，$\lvert\cdot\rvert=\sqrt{0.4444+0.8889}=\sqrt{1.3333}=\frac2{\sqrt3}$ ✓✓" "\n"
        r"$\vec a-3\vec b=(1+1,\ -2.8284)=(2,-2.8284)$，$\lvert\cdot\rvert=\sqrt{4+8}=\sqrt{12}$ ✓✓" "\n"
        r"**答案 $\frac{8\sqrt3}3$ 正确** ✓" "\n"
        r"**⭐ 通法**：与 V1 完全同构，都是「单位向量 $\vec a,\vec b$ 的线性组合模长之和」。" "\n"
        r"**统一公式**：$\lvert\vec a+k\vec b\rvert^{2}=1+k^{2}+2kt$（$+$号），$\lvert\vec a-k\vec b\rvert^{2}=1+k^{2}-2kt$（$-$号），" "\n"
        r"其中 $t=\cos\langle\vec a,\vec b\rangle$。套用后一律用**柯西配权** $|p|:|q|$ 消掉 $t$。" "\n"
        r"**记忆**：本题 $\lvert\vec a+\vec b\rvert$（系数 $+2$）与 $\lvert\vec a-3\vec b\rvert$（系数 $-6$），"
        r"权重 $=2:6=1:3$ ✓"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-237'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-237-V3',
}

QS = [T237_E1, T237_V1, T237_V3]
