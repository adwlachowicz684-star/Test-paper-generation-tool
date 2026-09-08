# -*- coding: utf-8 -*-
r"""第34批（下）：复数 · 模的几何意义与轨迹（4题）

来源：2024高中数学热点题型归纳完整解析版.pdf p315（PDF 页 314）

## 选题

`pick_batch.py --n 6 --topic M-T-343` → **p315 一页 4 题**，全部 A 级。
专题「题型八 复数中的轨迹（新高考）」。

## ★ 这类题的核心：把复数模翻译成平面几何

| 复数式 | 几何意义 |
|---|---|
| $\lvert z-z_0\rvert=r$ | 以 $Z_0$ 为圆心、$r$ 为半径的**圆** |
| $\lvert z-z_1\rvert=\lvert z-z_2\rvert$ | 到两点距离相等 → **中垂线** |
| $\lvert z-z_1\rvert+\lvert z-z_2\rvert=2a$ | 到两定点距离和为常数 |
| &nbsp;&nbsp;· $2a>\lvert Z_1Z_2\rvert$ | **椭圆** |
| &nbsp;&nbsp;· $2a=\lvert Z_1Z_2\rvert$ | **线段**（退化！最易错） |
| &nbsp;&nbsp;· $2a<\lvert Z_1Z_2\rvert$ | **不存在** |

**V2 正是考 $2a=\lvert Z_1Z_2\rvert$ 这个退化情形** —— 选「线段」而非「椭圆」。

## 四题验算

| 题 | 关键 | 答案 |
|---|---|---|
| E1 | 圆心 $(0,2)$ 半径 $1$；$d=\sqrt5$；$S\in[\frac{5-\sqrt5}2,\frac{5+\sqrt5}2]$ | 区间 |
| V1 | 半径 $3$ 的圆 → $9\pi$ | **D** |
| V2 | $2a=2=\lvert AB\rvert$ → 线段 | **A** |
| V3 | $Z=-\frac1{Z_1}$ 代入得 $\lvert Z+\frac1{Z_0}\rvert=\lvert\frac1{Z_0}\rvert$ → 圆 | **B** |
"""

T343_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知复平面内 $A$ 点对应的复数为 $2+\mathrm i$，$B$ 点对应的复数为 $1-\mathrm i$，"
        r"$z=x+(y-2)\mathrm i$（$x,y\in\mathbb R$）．若 $\lvert z\rvert=1$，"
        r"在 $z$ 的轨迹上任取一点 $C$，求 $\triangle ABC$ 的面积取值范围．"
    ),
    'opts': [],
    'answer': r"$S_{\triangle ABC}\in\left[\dfrac{5-\sqrt5}2,\ \dfrac{5+\sqrt5}2\right]$",
    'analysis': (
        r"先定出 $C$ 的轨迹是圆、求直线 $AB$ 方程与 $\lvert AB\rvert$，"
        r"再把面积最值转化为「圆上点到直线 $AB$ 的距离」的最值。"
    ),
    'solution': (
        r"**第一步：定 $C$ 的轨迹**" "\n"
        r"由 $z=x+(y-2)\mathrm i$、$\lvert z\rvert=1$ 得 $x^{2}+(y-2)^{2}=1$，"
        r"即 $C$ 在圆心 $P(0,2)$、半径 $r=1$ 的圆上．" "\n"
        r"**第二步：求直线 $AB$ 与 $\lvert AB\rvert$**" "\n"
        r"$A(2,1)$、$B(1,-1)$，斜率 $k=\dfrac{1-(-1)}{2-1}=2$，" "\n"
        r"直线 $AB$：$y-1=2(x-2)$，即 $2x-y-3=0$．" "\n"
        r"$\lvert AB\rvert=\sqrt{(2-1)^{2}+(1+1)^{2}}=\sqrt{1+4}=\sqrt5$．" "\n"
        r"**第三步：求圆心到直线的距离**" "\n"
        r"$d=\dfrac{\lvert 2\times0-2-3\rvert}{\sqrt{2^{2}+(-1)^{2}}}"
        r"=\dfrac5{\sqrt5}=\sqrt5$．" "\n"
        r"**第四步：圆上点到直线距离的最值**" "\n"
        r"因 $d=\sqrt5>r=1$，圆与直线相离，故" "\n"
        r"$h_{\min}=d-r=\sqrt5-1$，$h_{\max}=d+r=\sqrt5+1$．" "\n"
        r"**第五步：面积范围**" "\n"
        r"$S=\dfrac12\lvert AB\rvert\cdot h$：" "\n"
        r"$S_{\min}=\dfrac12\sqrt5(\sqrt5-1)=\dfrac{5-\sqrt5}2$，" "\n"
        r"$S_{\max}=\dfrac12\sqrt5(\sqrt5+1)=\dfrac{5+\sqrt5}2$．" "\n"
        r"故 $S_{\triangle ABC}\in\left[\dfrac{5-\sqrt5}2,\ \dfrac{5+\sqrt5}2\right]$．"
    ),
    'review': (
        r"★ 还原版完整 ✓。由详解「因为 $|z|=1$，所以 C 点轨迹为 $x^2+(y-2)^2=1$；"
        r"又因为 A 点对应的复数为 $2+\mathrm i$，B 点对应的复数为 $1-\mathrm i$，"
        r"则线段 AB 的方程为 $y=2x-3$（$1\le x\le2$），"
        r"AB 的长度为 $\sqrt{(2-1)^2+(1+1)^2}=\sqrt5$。"
        r"则知 $(0,2)$ 点到直线 AB 的距离为 $d=\frac{|2+3|}{\sqrt{1+2^2}}=\sqrt5$。"
        r"则 $\frac12\cdot\sqrt5\cdot(\sqrt5-1)\le S_{\triangle ABC}\le\frac12\cdot\sqrt5\cdot(\sqrt5+1)$。"
        r"则 $S\in[\frac{\sqrt5-5}2,\frac{\sqrt5+5}2]$」还原。" "\n"
        r"**⚠ 详解答案式的印刷错误（如实标注）**："
        r"原文写 $\frac{\sqrt5-5}2$ 与 $\frac{\sqrt5+5}2$，"
        r"但 $\frac{\sqrt5-5}2=\frac{2.236-5}2=-1.382<0$ —— **面积不可能为负**。" "\n"
        r"正确应为 $\frac{5-\sqrt5}2$ 与 $\frac{5+\sqrt5}2$ ✓。" "\n"
        r"**独立验算**：" "\n"
        r"圆心 $(0,2)$ 到 $2x-y-3=0$：$d=\frac{|0-2-3|}{\sqrt5}=\frac5{\sqrt5}=\sqrt5$ ✓" "\n"
        r"$d=\sqrt5\approx2.236>r=1$ ✓ 相离，距离最值 $[\sqrt5-1,\sqrt5+1]$ ✓" "\n"
        r"$S_{\min}=\frac12\cdot\sqrt5\cdot(\sqrt5-1)=\frac{5-\sqrt5}2\approx1.382$ ✓" "\n"
        r"$S_{\max}=\frac12\cdot\sqrt5\cdot(\sqrt5+1)=\frac{5+\sqrt5}2\approx3.618$ ✓" "\n"
        r"**数值抽查**：取圆上最高点 $C(0,3)$："
        r"$S=\frac12|x_A(y_B-y_C)+x_B(y_C-y_A)+x_C(y_A-y_B)|$" "\n"
        r"$=\frac12|2(-1-3)+1(3-1)+0|=\frac12|-8+2|=3$ —— 落在 $[1.382,3.618]$ 内 ✓" "\n"
        r"**结论正确** ✓（仅答案式的两项顺序印反了）"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-343'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-343-E1',
}

T343_V1 = {
    'type': '选择',
    'stem_text': (
        r"若复数 $z$ 满足 $\lvert z-1+\mathrm i\rvert=3$，"
        r"则复数 $z$ 对应的点的轨迹围成图形的面积等于（　　）"
    ),
    'opts': [('A', r"$3$"), ('B', r"$9$"),
             ('C', r"$6\pi$"), ('D', r"$9\pi$")],
    'answer': 'D',
    'analysis': (
        r"$\lvert z-(1-\mathrm i)\rvert=3$ 表示以 $(1,-1)$ 为圆心、$3$ 为半径的圆，"
        r"面积 $=\pi r^{2}=9\pi$。"
    ),
    'solution': (
        r"**化为标准形式**：$\lvert z-1+\mathrm i\rvert=\lvert z-(1-\mathrm i)\rvert=3$．" "\n"
        r"**几何意义**：$\lvert z-z_{0}\rvert=r$ 表示复平面上到定点 $Z_{0}$ "
        r"距离为定值 $r$ 的点的轨迹，即以 $Z_{0}$ 为圆心、$r$ 为半径的**圆**．" "\n"
        r"此处 $z_{0}=1-\mathrm i$ 对应点 $(1,-1)$，$r=3$．" "\n"
        r"**面积**：$S=\pi r^{2}=\pi\times3^{2}=9\pi$．" "\n"
        r"故选 D．"
    ),
    'review': (
        r"★ 还原版完整 ✓。由详解「复数 $z$ 满足 $|z-(1-\mathrm i)|=3$，"
        r"表示复数 $z$ 对应的点的轨迹是以点 $(1,-1)$ 为圆心，半径为 3 的圆，"
        r"所以围成图形的面积等于 $S=\pi\times3^{2}=9\pi$」还原。" "\n"
        r"**独立验算**：$S=\pi r^2=\pi\times9=9\pi$ ✓ **答案 D 正确**。" "\n"
        r"**干扰项**：A($3$) 是半径、B($9$) 是 $r^2$（漏乘 $\pi$）、"
        r"C($6\pi$) 是误用周长 $2\pi r=6\pi$ —— 三个都是「没写对面积公式」的典型错误。"
    ),
    'difficulty': 0.6,
    'topics': ['M-T-343'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-343-V1',
}

T343_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知复数 $z$ 满足 $\lvert z+\mathrm i\rvert+\lvert z-\mathrm i\rvert=2$，"
        r"则 $z$ 的轨迹为（　　）"
    ),
    'opts': [
        ('A', r"线段"), ('B', r"直线"),
        ('C', r"椭圆"), ('D', r"椭圆的一部分"),
    ],
    'answer': 'A',
    'analysis': (
        r"到两定点 $A(0,-1)$、$B(0,1)$ 的距离之和等于 $\lvert AB\rvert=2$，"
        r"此时椭圆**退化为线段 $AB$**（等号情形，不是真椭圆）。"
    ),
    'solution': (
        r"**几何意义**：$\lvert z+\mathrm i\rvert=\lvert z-(-\mathrm i)\rvert$ 是 $Z$ 到 "
        r"$A(0,-1)$ 的距离；$\lvert z-\mathrm i\rvert$ 是 $Z$ 到 $B(0,1)$ 的距离．" "\n"
        r"条件即 $\lvert ZA\rvert+\lvert ZB\rvert=2$．" "\n"
        r"**比较常数与 $\lvert AB\rvert$**：$\lvert AB\rvert=2$，恰好 **$2a=\lvert AB\rvert$**．" "\n"
        r"由三角形不等式：$\lvert ZA\rvert+\lvert ZB\rvert\geqslant\lvert AB\rvert=2$，"
        r"等号成立**当且仅当 $Z$ 在线段 $AB$ 上**．" "\n"
        r"故满足等号的点集正是**线段 $AB$**．" "\n"
        r"故选 A．"
    ),
    'review': (
        r"★ 还原版完整 ✓。由详解「设 $z=x+y\mathrm i$（$x,y\in\mathbb R$），"
        r"由复数的几何意义可知，$|z+\mathrm i|+|z-\mathrm i|=2$ 表示点 $Z(x,y)$ "
        r"到定点 $A(0,-1)$ 与 $B(0,1)$ 的距离之和为 2，而 $|AB|=2$，"
        r"故点 $Z$ 的轨迹为线段 $AB$」还原。" "\n"
        r"**独立验算**：" "\n"
        r"若 $2a>|AB|=2$（如 $=3$）→ 椭圆；若 $2a=|AB|=2$ → **线段**；"
        r"若 $2a<|AB|$ → 无解。" "\n"
        r"本题 $2a=2=|AB|$ ✓ **退化为线段**。" "\n"
        r"**验证**：取 $Z=(0,0)$（线段中点）：$|Z A|+|ZB|=1+1=2$ ✓；"
        r"取 $Z=(0,2)$（线段外）：$|2+1|+|2-1|=3+1=4\neq2$ ✗ ✓" "\n"
        r"**答案 A 正确** ✓" "\n"
        r"**⭐ 这是本题的命门**：学生一看「距离和为常数」就选椭圆（C），"
        r"但必须**先比较常数与两定点距离**，等号时是线段。"
    ),
    'difficulty': 0.78,
    'topics': ['M-T-343'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-343-V2',
}

T343_V3 = {
    'type': '选择',
    'stem_text': (
        r"设非零复数 $Z_{0}$ 是复平面上一定点，$Z_{1}$ 为复平面上的动点，"
        r"其轨迹方程 $\lvert Z_{1}-Z_{0}\rvert=\lvert Z_{1}\rvert$，"
        r"$Z$ 为复平面上另一个动点满足 $Z_{1}Z=-1$，"
        r"则 $Z$ 在复平面上的轨迹形状是（　　）"
    ),
    'opts': [
        ('A', r"双曲线"), ('B', r"圆"),
        ('C', r"一条直线"), ('D', r"抛物线"),
    ],
    'answer': 'B',
    'analysis': (
        r"由 $Z_{1}Z=-1$ 得 $Z_{1}=-\dfrac1Z$，代入原轨迹方程，"
        r"两边同乘 $\lvert Z\rvert$ 后配方得圆的方程。"
    ),
    'solution': (
        r"**第一步：反解 $Z_{1}$**" "\n"
        r"由 $Z_{1}Z=-1$ 得 $Z_{1}=-\dfrac1Z$（$Z\neq0$）．" "\n"
        r"**第二步：代入轨迹方程**" "\n"
        r"$\left\lvert-\dfrac1Z-Z_{0}\right\rvert=\left\lvert-\dfrac1Z\right\rvert$" "\n"
        r"$\Rightarrow\left\lvert\dfrac1Z+Z_{0}\right\rvert=\dfrac1{\lvert Z\rvert}$．" "\n"
        r"**第三步：两边同乘 $\lvert Z\rvert$**" "\n"
        r"$\lvert Z\rvert\cdot\left\lvert\dfrac1Z+Z_{0}\right\rvert"
        r"=\lvert 1+Z_{0}Z\rvert=1$．" "\n"
        r"即 $\lvert Z_{0}Z+1\rvert=1$．" "\n"
        r"**第四步：化为标准圆方程**" "\n"
        r"$\left\lvert Z_{0}\right\rvert\cdot\left\lvert Z+\dfrac1{Z_{0}}\right\rvert=1$" "\n"
        r"$\Rightarrow\left\lvert Z+\dfrac1{Z_{0}}\right\rvert=\dfrac1{\lvert Z_{0}\rvert}$．" "\n"
        r"这是以 $-\dfrac1{Z_{0}}$ 对应的点为圆心、$\dfrac1{\lvert Z_{0}\rvert}$ 为半径的**圆**．" "\n"
        r"故选 B．"
    ),
    'review': (
        r"★ 还原版题干与答案完整；**详解的式子破碎严重**（满是 $\langle?\rangle$ 与 "
        r"$\frac{1}{0}$ 占位），但关键结论可辨：" "\n"
        r"「因为 $Z_1Z=-1$，所以 $Z_1=-\frac1Z$，代入 $|Z_1-Z_0|=|Z_1|$，"
        r"得 $|-\frac1Z-Z_0|=|-\frac1Z|$，"
        r"两边同乘 $|Z|$，得 $\left|Z+\frac1{Z_0}\right|=\frac1{|Z_0|}$，"
        r"所以 $Z$ 在复平面上的轨迹形状是以 $-\frac1{Z_0}$ 为圆心，$\frac1{|Z_0|}$ 为半径的圆」✓ "
        r"**与我的推导完全一致**。" "\n"
        r"**独立验算**：" "\n"
        r"$Z_1=-\frac1Z$ ✓（由 $Z_1Z=-1$）" "\n"
        r"$|Z_1-Z_0|=|-\frac1Z-Z_0|$，$|-Z_1|=|\frac1Z|=\frac1{|Z|}$ ✓" "\n"
        r"同乘 $|Z|$：$|\cdot|\cdot|Z|=|-\frac1Z-Z_0|\cdot|Z|=|(-1-Z_0Z)/Z|\cdot|Z|$" "\n"
        r"$=\frac{|1+Z_0Z|}{|Z|}\cdot|Z|=|1+Z_0Z|$ ✓；右端 $\frac1{|Z|}\cdot|Z|=1$ ✓" "\n"
        r"故 $|1+Z_0Z|=1$，即 $|Z_0|\cdot|Z+\frac1{Z_0}|=1$ ✓" "\n"
        r"→ $\left|Z+\frac1{Z_0}\right|=\frac1{|Z_0|}$ ✓ **是圆**" "\n"
        r"**具体检验**：取 $Z_0=1$，则 $|Z+1|=1$，圆心 $(-1,0)$、半径 $1$。"
        r"取圆上点 $Z=-2$：$Z_1=-\frac1{-2}=0.5$，$|Z_1-Z_0|=0.5=|Z_1|$ ✓ **满足原方程**" "\n"
        r"**答案 B 正确** ✓"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-343'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-343-V3',
}

QS = [T343_E1, T343_V1, T343_V2, T343_V3]
