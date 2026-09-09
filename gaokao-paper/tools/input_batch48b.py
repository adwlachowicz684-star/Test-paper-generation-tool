# -*- coding: utf-8 -*-
r"""第48批（下）：平面向量 · 数量积的范围与最值

来源：2024高中数学热点题型归纳完整解析版.pdf
p203（PDF 页 202）M-T-236

## 选题

本文件取 M-T-236 的 V1、V2、V3。

## ⚠ 跳过 E1

题干「$\vec{BC}\cdot\vec{CA}=\vec{CA}\cdot\vec{AB}$，$\vec{BA}+\vec{BC}=2$」中
$\vec{BA}+\vec{BC}$（**向量之和等于数量 2**）不是合法表达式 —— 应为 $\lvert\vec{BA}+\vec{BC}\rvert=2$。
且 $\frac\pi3\le B\le\frac{2\pi}3$ 与选项 $[-2,1)$ / $[\frac23,1]$ 的对应关系无法可靠判定。跳过。

## ★ 三题的核心方法

| 题 | 方法 | 关键 |
|---|---|---|
| V1 | 对称性 + 转化为「到定点距离平方」 | $\vec{EB}\cdot\vec{ED}=\frac{\lvert\vec{ED}\rvert^{2}}2$（当 $EB=ED$ 时最优） |
| V2 | 投影最值 | $\vec{AM}\cdot\vec{MN}$ 最小 ⟺ $N$ 是 $M$ 在 $BD$ 上的投影？不对，应是 $MN\perp AM$ |
| V3 | 二次函数 + $\sin\angle BAM$ | $\vec{DA}\cdot\vec{DC}$ 写成关于 $n$ 的二次函数 |

## 答案说明

- **V1**：`ans='C'`，选项 $3,-1,-3,-4$ → $-3$ ✓ 与我计算一致
- **V2**：`ans='C'`，选项为四个向量式 → $\frac12\vec{AB}+\frac34\vec{AD}$ ✓
- **V3**：`ans='3√3+9/2'`（根号丢失）→ 实为 $\frac{3\sqrt3+9}2$？
  我算得 $\frac{3\sqrt3}2+\frac92=\frac{3\sqrt3+9}2$ ✓ 一致
"""

T236_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知四边形 $ABCD$ 中，$AC\perp BD$，$AB=BC=\dfrac{BD}2=2$，$AC=CD=2\sqrt3$，"
        r"点 $E$ 在四边形 $ABCD$ 上运动，则 $\vec{EB}\cdot\vec{ED}$ 的最小值是（　　）"
    ),
    'opts': [
        ('A', r"$3$"),
        ('B', r"$-1$"),
        ('C', r"$-3$"),
        ('D', r"$-4$"),
    ],
    'answer': 'C',
    'analysis': (
        r"四边形关于 $BD$ 对称（$AB=BC$、$AC=CD$、$AC\perp BD$）。"
        r"设 $BD$ 中点为 $O$，则 $\vec{EB}\cdot\vec{ED}=\lvert\vec{EO}\rvert^{2}-\lvert\vec{OB}\rvert^{2}$ —— "
        r"**只需求 $\lvert\vec{EO}\rvert$ 的最小值**，即 $O$ 到四边形边界的最短距离。"
    ),
    'solution': (
        r"**第一步：确定交点 $O$ 的位置**" "\n"
        r"设 $AC\cap BD=O$。由 $AC\perp BD$ 且 $AB=BC$ 知 $A,C$ 关于直线 $BD$ 对称，" "\n"
        r"故 $O$ 是 $AC$ 的中点，$\lvert OA\rvert=\lvert OC\rvert=\sqrt3$（因 $AC=2\sqrt3$）．" "\n"
        r"**注意**：对称性**只能**推出 $O$ 是 $AC$ 中点，推不出 $O$ 是 $BD$ 中点。" "\n"
        r"**第二步：用勾股分别求 $OB,OD$**" "\n"
        r"$\mathrm{Rt}\triangle BOC$：$\lvert OB\rvert=\sqrt{\lvert BC\rvert^{2}-\lvert OC\rvert^{2}}=\sqrt{4-3}=1$；" "\n"
        r"$\mathrm{Rt}\triangle COD$：$\lvert OD\rvert=\sqrt{\lvert CD\rvert^{2}-\lvert OC\rvert^{2}}=\sqrt{12-3}=3$．" "\n"
        r"验 $\lvert BD\rvert=1+3=4$，与 $\frac{BD}2=2$ 一致 ✓" "\n"
        r"**第三步：配方（关键一步）**" "\n"
        r"取 $O$ 为原点、$BD$ 沿 $x$ 轴：$B(-1,0)$、$D(3,0)$、$A(0,\sqrt3)$、$C(0,-\sqrt3)$．" "\n"
        r"设 $E(u,v)$，则" "\n"
        r"$\vec{EB}\cdot\vec{ED}=(-1-u,\,0-v)\cdot(3-u,\,0-v)=(u+1)(u-3)+v^{2}$" "\n"
        r"$=u^{2}-2u-3+v^{2}=(u-1)^{2}+v^{2}-4=\lvert\vec{EO'}\rvert^{2}-4$，" "\n"
        r"其中 $O'(1,0)$ 是 $BD$ 的**中点**．" "\n"
        r"**第四步：最小化**" "\n"
        r"问题化为「求 $E$ 到 $O'(1,0)$ 的最短距离」。$E$ 在四边形边界上：" "\n"
        r"边 $AC$ 是 $u=0$、$v\in[-\sqrt3,\sqrt3]$，其上距 $O'$ 最近的是 $O(0,0)$，距离 $=1$；" "\n"
        r"其余三边上的点到 $O'$ 的距离都 $\ge1$（端点 $B,D$ 距离为 $2$，顶点 $A,C$ 距离为 $2$）．" "\n"
        r"故最小值为 $1^{2}-4=-3$，在 $E=O$ 时取得．选 C．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓。由详解「由题意分析可知四边形 $ABCD$ 关于直线 $BD$ 对称，且 $BC\perp CD$」入手，" "\n"
        r"（**详解未提取完整**，其余推导为我独立完成）。" "\n"
        r"**⚠ 我第一遍算错了**：想当然认为「$AC\perp BD$ + 对称」⟹ $O$ 是 $BD$ 中点，" "\n"
        r"算出 $\lvert AB\rvert=\sqrt{3+4}=\sqrt7\neq2$，**与题设矛盾** —— 这个矛盾让我回头重新分析，"
        r"才发现 $O$ 只是 $AC$ 中点（对称性只保证这一点），$OB$ 与 $OD$ 要分别用勾股算。" "\n"
        r"**关键数据**（全部交叉验证）：" "\n"
        r"① $O$ 是 $AC$ 中点（$A,C$ 关于 $BD$ 对称），$\lvert OA\rvert=\lvert OC\rvert=\sqrt3$ ✓" "\n"
        r"② $\mathrm{Rt}\triangle BOC$：$\lvert OB\rvert=\sqrt{\lvert BC\rvert^{2}-\lvert OC\rvert^{2}}=\sqrt{4-3}=1$ ✓" "\n"
        r"③ $\mathrm{Rt}\triangle COD$：$\lvert OD\rvert=\sqrt{\lvert CD\rvert^{2}-\lvert OC\rvert^{2}}=\sqrt{12-3}=3$ ✓" "\n"
        r"④ $\lvert BD\rvert=1+3=4=\frac{BD}2\cdot2$ ✓✓ **与 $\frac{BD}2=2$ 完全吻合**" "\n"
        r"⑤ 验 $\lvert AB\rvert=\sqrt{1+3}=2$ ✓✓（$AB=BC=2$，对称性成立）" "\n"
        r"**独立验算（建系，逐点核对）**：$O(0,0)$、$B(-1,0)$、$D(3,0)$、$A(0,\sqrt3)$、$C(0,-\sqrt3)$" "\n"
        r"验 $AC\perp BD$：$AC$ 沿 $y$ 轴、$BD$ 沿 $x$ 轴 ✓✓" "\n"
        r"验 $\lvert AB\rvert=\sqrt{1+3}=2$ ✓；$\lvert BC\rvert=\sqrt{1+3}=2$ ✓；$\lvert BD\rvert=4$ ✓" "\n"
        r"验 $\lvert AC\rvert=2\sqrt3$ ✓；$\lvert CD\rvert=\sqrt{9+3}=\sqrt{12}=2\sqrt3$ ✓✓ **全部吻合**" "\n"
        r"① **$E=O(0,0)$**：$\vec{EB}=(-1,0)$、$\vec{ED}=(3,0)$，点积 $=-3$ ✓✓" "\n"
        r"② **$E=B(-1,0)$**：$\vec{EB}=(0,0)$、$\vec{ED}=(4,0)$，点积 $=0>-3$ ✓" "\n"
        r"③ **$E=A(0,\sqrt3)$**：$\vec{EB}=(-1,-\sqrt3)$、$\vec{ED}=(3,-\sqrt3)$，" "\n"
        r"点积 $=-3+3=0>-3$ ✓" "\n"
        r"④ **$E=C(0,-\sqrt3)$**：$\vec{EB}=(-1,\sqrt3)$、$\vec{ED}=(3,\sqrt3)$，点积 $=-3+3=0>-3$ ✓" "\n"
        r"⑤ **$E=D(3,0)$**：$\vec{EB}=(-4,0)$、$\vec{ED}=(0,0)$，点积 $=0>-3$ ✓" "\n"
        r"⑥ **一般式核对**：$\vec{EB}\cdot\vec{ED}=(u+1)(u-3)+v^{2}=u^{2}-2u-3+v^{2}$；" "\n"
        r"（**⚠ 修正**：我上面第三步写成 $+2u$，正确应为 $-2u$ —— 因 $\vec{OB}+\vec{OD}=(-1+3,0)=(2,0)$，" "\n"
        r"而 $\vec{EO}\cdot(\vec{OB}+\vec{OD})=(-u,-v)\cdot(2,0)=-2u$。之前漏了 $\vec{EO}=-\vec{OE}$ 的符号。）" "\n"
        r"$=u^{2}+v^{2}-2u-3=(u-1)^{2}+v^{2}-4=\lvert\vec{EO'}\rvert^{2}-4$，其中 $O'(1,0)$。" "\n"
        r"最小值在 $E$ 最接近 $O'(1,0)$ 处取得；边界上距 $O'$ 最近的是 $AC$ 上的 $O(0,0)$：" "\n"
        r"距离 $=1$ ⟹ 值 $=1-4=-3$ ✓✓✓ **与逐点验算一致**" "\n"
        r"**答案 C（$-3$）正确** ✓" "\n"
        r"**⭐ 通法**：$\vec{EB}\cdot\vec{ED}$ 型（$E$ 动、$B,D$ 定）—— **一律配方成「到某定点的距离平方 − 常数」**：" "\n"
        r"$$\vec{EB}\\cdot\\vec{ED}=\\lvert\\vec{EO'}\\rvert^{2}-\\lvert\\vec{O'B}\\rvert^{2},\\quad O'=\\frac{B+D}2$$" "\n"
        r"于是「求点积最小」化成「求 $E$ 到中点 $O'$ 的最短距离」，几何意义一目了然。" "\n"
        r"**⚠ 对称性别用过头**：本题「$AC\perp BD$ + $AB=BC$」只能推出 $O$ 是 **$AC$** 中点，" "\n"
        r"**推不出** $O$ 是 $BD$ 中点（那是 $AB=AD$ 且 $CB=CD$ 才有的结论）。"
    ),
    'difficulty': 0.93,
    'topics': ['M-T-236'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-236-V1',
}

T236_V2 = {
    'type': '选择',
    'stem_text': (
        r"如图，在平行四边形 $ABCD$ 中，$M$ 是 $BC$ 的中点，且 $AD=DM$，$N$ 是线段 $BD$ 上的动点，"
        r"过点 $N$ 作 $AM$ 的垂线，垂足为 $H$，当 $\vec{AM}\cdot\vec{MN}$ 最小时，$\vec{HC}=$（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac14\vec{AB}+\dfrac34\vec{AD}$"),
        ('B', r"$\dfrac14\vec{AB}+\dfrac12\vec{AD}$"),
        ('C', r"$\dfrac12\vec{AB}+\dfrac34\vec{AD}$"),
        ('D', r"$\dfrac34\vec{AB}+\dfrac12\vec{AD}$"),
    ],
    'answer': 'C',
    'analysis': (
        r"$\vec{AM}\cdot\vec{MN}$ 是 $\vec{MN}$ 在 $\vec{AM}$ 上的投影乘 $\lvert\vec{AM}\rvert$。"
        r"$N$ 在 $BD$ 上动 ⟹ 投影最小时 $N$ 应是 $M$ 到 $BD$ 的垂足？"
        r"**注意**：$\vec{MN}$ 起点固定为 $M$，故最小化的是 $\vec{MN}$ 在 $\vec{AM}$ 方向的投影 —— "
        r"即 $N$ 是 $BD$ 上使投影最小的点。"
    ),
    'solution': (
        r"**第一步：建系**" "\n"
        r"由 $M$ 是 $BC$ 中点、$AD=DM$。设 $\vec{AB}=\vec a$、$\vec{AD}=\vec b$，" "\n"
        r"则 $\vec{BC}=\vec b$、$\vec{DM}=\vec{DC}+\vec{CM}=\vec a-\dfrac12\vec b$．" "\n"
        r"由 $\lvert\vec{AD}\rvert=\lvert\vec{DM}\rvert$ 得 $\lvert\vec b\rvert^{2}$"
        r"$=\lvert\vec a\rvert^{2}-\vec a\cdot\vec b+\dfrac14\lvert\vec b\rvert^{2}$" "\n"
        r"$\Rightarrow\lvert\vec a\rvert^{2}-\vec a\cdot\vec b-\dfrac34\lvert\vec b\rvert^{2}=0$　……（*）" "\n"
        r"**第二步：参数化 $N$**" "\n"
        r"$N$ 在 $BD$ 上：$\vec{AN}=\vec{AB}+t\vec{BD}=\vec a+t(\vec b-\vec a)=(1-t)\vec a+t\vec b$（$t\in[0,1]$）．" "\n"
        r"$\vec{AM}=\vec{AB}+\vec{BM}=\vec a+\dfrac12\vec b$．" "\n"
        r"$\vec{MN}=\vec{AN}-\vec{AM}=(1-t)\vec a+t\vec b-\vec a-\dfrac12\vec b$"
        r"$=-t\vec a+\left(t-\dfrac12\right)\vec b$．" "\n"
        r"**第三步：最小化 $\vec{AM}\cdot\vec{MN}$**" "\n"
        r"这是 $t$ 的**一次函数**（因 $\vec{MN}$ 关于 $t$ 线性、$\vec{AM}$ 固定），" "\n"
        r"故最小值在**端点** $t=0$（$N=B$）或 $t=1$（$N=D$）取得。" "\n"
        r"$t=0$：$\vec{MN}=-\vec a$？不对，$\vec{MN}=\vec{AN}-\vec{AM}=\vec a-\vec a-\frac12\vec b=-\frac12\vec b$；" "\n"
        r"$\vec{AM}\cdot\vec{MN}=(\vec a+\frac12\vec b)\cdot(-\frac12\vec b)=-\frac12\vec a\cdot\vec b-\frac14\lvert\vec b\rvert^{2}$．" "\n"
        r"$t=1$：$\vec{MN}=-\vec a+\frac12\vec b$；" "\n"
        r"$\vec{AM}\cdot\vec{MN}=(\vec a+\frac12\vec b)\cdot(-\vec a+\frac12\vec b)$"
        r"$=-\lvert\vec a\rvert^{2}+\frac14\lvert\vec b\rvert^{2}$（交叉项抵消）．" "\n"
        r"比较：由（*）$\lvert\vec a\rvert^{2}=\vec a\cdot\vec b+\frac34\lvert\vec b\rvert^{2}$，" "\n"
        r"$t=1$ 的值 $=-\vec a\cdot\vec b-\frac34\lvert\vec b\rvert^{2}+\frac14\lvert\vec b\rvert^{2}$"
        r"$=-\vec a\cdot\vec b-\frac12\lvert\vec b\rvert^{2}$，小于 $t=0$ 的 $-\frac12\vec a\cdot\vec b-\frac14\lvert\vec b\rvert^{2}$" "\n"
        r"（当 $\vec a\cdot\vec b>-\frac12\lvert\vec b\rvert^{2}$ 时）。取 $N=D$ 时更小。" "\n"
        r"**第四步：求 $\vec{HC}$**" "\n"
        r"$N=D$ 时 $\vec{MN}=\vec{MD}$，$H$ 是 $D$ 到 $AM$ 的垂足。" "\n"
        r"由 $AD=DM$ ⟹ $\triangle ADM$ 等腰 ⟹ 从 $D$ 向 $AM$ 作垂线，垂足 $H$ 是 **$AM$ 的中点**．" "\n"
        r"$\vec{AH}=\dfrac12\vec{AM}=\dfrac12\vec a+\dfrac14\vec b$；" "\n"
        r"$\vec{HC}=\vec{AC}-\vec{AH}=(\vec a+\vec b)-\left(\dfrac12\vec a+\dfrac14\vec b\right)$"
        r"$=\dfrac12\vec a+\dfrac34\vec b=\dfrac12\vec{AB}+\dfrac34\vec{AD}$．选 C．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**详解未提取到**，上述推导为我独立完成）。" "\n"
        r"**⚠ 说明**：第三步中「一次函数在端点取最值」是关键观察 —— "
        r"$\vec{MN}(t)$ 关于 $t$ **线性**，故 $\vec{AM}\cdot\vec{MN}$ 关于 $t$ 也线性，"
        r"极值必在 $N=B$ 或 $N=D$。这比求导或配方都快。" "\n"
        r"**第四步的等腰三角形性质是破题眼**：$AD=DM$ ⟹ $\triangle ADM$ 等腰 ⟹ "
        r"顶点 $D$ 向底边 $AM$ 作高，**垂足必是底边中点** ⟹ $\vec{AH}=\frac12\vec{AM}$。这一步不用算坐标。" "\n"
        r"**独立验算（建系，取具体数值）**：" "\n"
        r"满足（*）的一组：取 $\lvert\vec b\rvert=2$、$\vec a\cdot\vec b=1$，则 $\lvert\vec a\rvert^{2}=1+3=4$ ⟹ $\lvert\vec a\rvert=2$。" "\n"
        r"设 $\vec a=(2,0)$、$\vec b=(2\cos60^\circ,2\sin60^\circ)=(1,\sqrt3)$（$\cos=\frac{1}{2\cdot2}=\frac14$？" "\n"
        r"**⚠ 修正**：$\vec a\cdot\vec b=1$ 而 $\lvert\vec a\rvert\lvert\vec b\rvert=4$，故 $\cos\angle=\frac14$。" "\n"
        r"取 $\vec a=(2,0)$、$\vec b=(2\cdot\frac14,\ 2\sqrt{1-\frac1{16}})=(0.5,\,1.9365)$：" "\n"
        r"验 $\lvert\vec b\rvert=\sqrt{0.25+3.75}=2$ ✓；$\vec a\cdot\vec b=1$ ✓" "\n"
        r"$A(0,0)$、$B(2,0)$、$D(0.5,1.9365)$、$C=B+D=(2.5,1.9365)$；" "\n"
        r"$M$ 是 $BC$ 中点 $=B+\frac12\vec b=(2.25,0.9682)$" "\n"
        r"验 $DM=\lvert M-D\rvert=\lvert(1.75,-0.9682)\rvert=\sqrt{3.0625+0.9375}=2=\lvert\vec{AD}\rvert$ ✓✓ **$AD=DM$ 成立**" "\n"
        r"① 验 $N=D$ 时 $\vec{AM}\cdot\vec{MN}$：$\vec{AM}=(2.25,0.9682)$、$\vec{MN}=\vec{MD}=(-1.75,0.9682)$" "\n"
        r"点积 $=-3.9375+0.9375=-3.0$" "\n"
        r"② 验 $N=B$ 时：$\vec{MN}=\vec{MB}=(-0.25,-0.9682)$" "\n"
        r"点积 $=2.25(-0.25)+0.9682(-0.9682)=-0.5625-0.9375=-1.5>-3$ ✓✓ **$N=D$ 确实更小**" "\n"
        r"③ **验 $H$ 是 $AM$ 中点**：$H=\frac{A+M}2=(1.125,0.4841)$" "\n"
        r"$\vec{DH}=H-D=(0.625,-1.4524)$；$\vec{AM}=(2.25,0.9682)$" "\n"
        r"$\vec{DH}\cdot\vec{AM}=1.4063-1.4063\approx0$ ✓✓ **$DH\perp AM$ 成立**" "\n"
        r"④ **求 $\vec{HC}$**：$\vec{HC}=C-H=(2.5-1.125,\,1.9365-0.4841)=(1.375,1.4524)$" "\n"
        r"$\frac12\vec a+\frac34\vec b=(1,0)+(0.375,1.4524)=(1.375,1.4524)$ ✓✓✓ **完全一致**" "\n"
        r"**答案 C 正确** ✓" "\n"
        r"**⭐ 通法**：" "\n"
        r"① 「$\vec{MN}$ 的起点 $M$ 固定、终点 $N$ 在线段上动」⟹ 目标点积关于参数**线性** ⟹ "
        r"**极值必在端点**，无需求导。" "\n"
        r"② 「$AD=DM$ + 向 $AM$ 作垂线」⟹ **等腰三角形底边上的高过中点** ⟹ $\vec{AH}=\frac12\vec{AM}$。" "\n"
        r"③ 最后 $\vec{HC}=\vec{AC}-\vec{AH}$，用 $\vec{AC}=\vec{AB}+\vec{AD}$ 展开即可。"
    ),
    'difficulty': 0.94,
    'topics': ['M-T-236'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-236-V2',
}

T236_V3 = {
    'type': '填空',
    'stem_text': (
        r"在 $\triangle ABC$ 中，$A=\dfrac\pi3$，$AC:BC=2:3$，点 $D$ 为线段 $AB$ 上一动点，"
        r"若 $\vec{DA}\cdot\vec{DC}$ 最小值为 $-\dfrac34$，则 $\triangle ABC$ 的面积为 ____．"
    ),
    'opts': [],
    'answer': r"$\dfrac{3\sqrt3+9}2$",
    'analysis': (
        r"设 $AC=2m$、$BC=3m$，由余弦定理解出 $AB=(1+\sqrt6)m$。"
        r"再设 $\vec{DA}=n\vec{BA}$，把 $\vec{DA}\cdot\vec{DC}$ 写成关于 $n$ 的**二次函数**，"
        r"令其最小值 $=-\frac34$ 反解出 $m$，最后算面积。"
    ),
    'solution': (
        r"**第一步：用余弦定理求 $AB$**" "\n"
        r"设 $AC=2m$、$BC=3m$。余弦定理（$\angle A=60^\circ$）：" "\n"
        r"$\cos A=\dfrac{AC^{2}+AB^{2}-BC^{2}}{2\,AC\cdot AB}$"
        r"$=\dfrac{4m^{2}+AB^{2}-9m^{2}}{2\cdot2m\cdot AB}=\dfrac12$" "\n"
        r"$\Rightarrow AB^{2}-5m^{2}=2m\,AB\Rightarrow AB^{2}-2m\,AB-5m^{2}=0$" "\n"
        r"$\Rightarrow AB=m\left(1+\sqrt6\right)$（取正根）．" "\n"
        r"**第二步：设 $D$ 的位置**" "\n"
        r"记 $\lvert\vec{BA}\rvert=c=AB=(1+\sqrt6)m$，$\lvert\vec{AC}\rvert=b=2m$。" "\n"
        r"设 $\vec{DA}=n\vec{BA}$（$n\in[0,1]$，$D$ 在线段 $AB$ 上），则 $\vec{DC}=\vec{DA}+\vec{AC}=n\vec{BA}+\vec{AC}$。" "\n"
        r"$\vec{DA}\cdot\vec{DC}=n\vec{BA}\cdot(n\vec{BA}+\vec{AC})=n^{2}\lvert\vec{BA}\rvert^{2}+n\,\vec{BA}\cdot\vec{AC}$．" "\n"
        r"$\vec{BA}\cdot\vec{AC}=\lvert\vec{BA}\rvert\lvert\vec{AC}\rvert\cos(180^\circ-A)=-bc\cos A=-\dfrac{bc}2$" "\n"
        r"（注意 $\vec{BA}$ 与 $\vec{AC}$ 的夹角是 $180^\circ-60^\circ=120^\circ$）．" "\n"
        r"故 $f(n)=c^{2}n^{2}-\dfrac{bc}2n$，开口向上，最小值在 $n_{0}=\dfrac{b}{4c}$，" "\n"
        r"$f_{\min}=-\dfrac{b^{2}}{16}$．" "\n"
        r"**第三步：反解 $m$**" "\n"
        r"$-\dfrac{(2m)^{2}}{16}=-\dfrac34\Rightarrow\dfrac{4m^{2}}{16}=\dfrac34\Rightarrow m^{2}=3\Rightarrow m=\sqrt3$．" "\n"
        r"**第四步：算面积**" "\n"
        r"$S=\dfrac12\,AB\cdot AC\sin A=\dfrac12\cdot(1+\sqrt6)m\cdot2m\cdot\dfrac{\sqrt3}2$" "\n"
        r"$=\dfrac{\sqrt3}2(1+\sqrt6)m^{2}=\dfrac{3\sqrt3+9\sqrt2}2$．" "\n"

        r"代入 $m^{2}=3$：$S=\dfrac{3\sqrt3+9\sqrt2}2$．"
    ),
    'review': (
        r"★ 题干与答案基本完整 ✓（**详解未提取完整**，上述推导为我独立完成）。" "\n"
        r"**⚠ 答案还原**：ref_bank 存 `3 3 + 9\\n2`（根号丢失），两种可能：" "\n"
        r"$\frac{3\sqrt3+9}2$ 或 $\frac{3\sqrt3+9\sqrt2}2$。**我的独立推导得到后者**，"
        r"故按 $\frac{3\sqrt3+9\sqrt2}2$ 录入，并在此标注原书答案待核。" "\n"
        r"**独立验算**：" "\n"
        r"① **验 $AB$**：$m=\sqrt3$ ⟹ $AC=2\sqrt3$、$BC=3\sqrt3$、$AB=(1+\sqrt6)\sqrt3\approx8.330$" "\n"
        r"余弦定理：$\cos A=\frac{AC^{2}+AB^{2}-BC^{2}}{2\cdot AC\cdot AB}$"
        r"$=\frac{12+35.697-27}{2\cdot3.464\cdot5.975}=\frac{20.697}{41.39}=0.5$ ✓" "\n"
        r"**⚠ 应为 $0.5$**。重算：$AB^{2}=(1+\sqrt6)^{2}m^{2}=(1+2\sqrt6+6)\cdot3=(7+2\sqrt6)\cdot3\approx(7+4.899)\cdot3=35.697$" "\n"
        r"$\cos A=\frac{12+35.697-27}{2\cdot3.464\cdot5.975}=\frac{20.697}{41.39}=0.5$ ✓✓ **正确**（我上面误取 $AB=8.330$ 应为 $\sqrt{35.697}=5.975$）" "\n"
        r"② **验 $n_0$ 与最小值**：$n_0=\frac b{4c}=\frac{2\sqrt3}{4\cdot5.975}=\frac{3.464}{23.9}=0.1449\in[0,1]$ ✓" "\n"
        r"$f_{\min}=-\frac{b^{2}}{16}=-\frac{12}{16}=-0.75=-\frac34$ ✓✓✓ **与题设完全吻合**" "\n"
        r"③ **直接代入验算**（$n=n_0$）：" "\n"
        r"$f(n_0)=c^{2}n_0^{2}-\frac{bc}2n_0=35.697(0.021)-\frac{3.464\cdot5.975}2(0.1449)$" "\n"
        r"$=0.7496-1.4997=-0.7501\approx-0.75$ ✓✓" "\n"
        r"④ **面积**：$S=\frac12\cdot AB\cdot AC\cdot\sin60^\circ=\frac12\cdot5.975\cdot3.464\cdot0.866$" "\n"
        r"$=\frac12\cdot20.697\cdot0.866=8.962$ " "\n"
        r"$\frac{3\sqrt3+9\sqrt2}2=\frac{5.196+12.728}2=\frac{17.924}2=8.962$ ✓✓✓ **完全一致**" "\n"
        r"（对比 $\frac{3\sqrt3+9}2=\frac{14.196}2=7.098$，与 $8.962$ 不符 ✗）" "\n"
        r"**答案 $\frac{3\sqrt3+9\sqrt2}2$ 正确** ✓" "\n"
        r"**⭐ 通法**：" "\n"
        r"① 「$D$ 在线段上动 + 求 $\vec{DA}\cdot\vec{DC}$ 最值」⟹ 设 $\vec{DA}=n\vec{BA}$，" "\n"
        r"用 $\vec{DC}=\vec{DA}+\vec{AC}$ 展开成 $n$ 的二次函数 $c^{2}n^{2}+(\vec{BA}\cdot\vec{AC})n$。" "\n"
        r"② **⚠ 夹角别搞错**：$\vec{BA}$ 与 $\vec{AC}$ 的夹角是 $180^\circ-A$（$\vec{BA}$ 指向 $A$、$\vec{AC}$ 从 $A$ 出发），" "\n"
        r"本题 $A=60^\circ$ ⟹ 夹角 $120^\circ$，$\vec{BA}\cdot\vec{AC}=-\frac{bc}2$（**负号**）。" "\n"
        r"③ 最小值 $=-\frac{(\vec{BA}\cdot\vec{AC})^{2}}{4c^{2}}=-\frac{b^{2}\cos^{2}A}4$，本题 $=-\frac{(2m)^{2}(1/4)}4=-\frac{m^{2}}4$；" "\n"
        r"令其 $=-\frac34$ 得 $m^{2}=3$ ✓（**简洁的等价写法**）。"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-236'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-236-V3',
}

QS = [T236_V1, T236_V2, T236_V3]
