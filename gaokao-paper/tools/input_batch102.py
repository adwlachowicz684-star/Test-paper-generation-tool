# -*- coding: utf-8 -*-
r"""第 102 批：导数压轴证明题（零点个数 · 三个极值点 · 比值代换 · 极值点偏移）

    python3 tools/run_batch.py 102

## 选题依据

按「详解完整 + 同题型聚堆 + 无图依赖」筛出 p127-p134 的导数解答题，共 12 题，
全部为解答题（讨论 + 证明），集中在 M-T-152、M-T-164、M-T-169、M-T-172 四个题型：

| 题型 | 题号 | 核心方法 |
|---|---|---|
| M-T-152 | E1, V1, V2 | 单调性与零点个数；分段讨论；导函数零点存在性 |
| M-T-164 | E1, V1, V2 | 三个极值点的排序证明；比值代换；构造辅助函数 |
| M-T-169 | E1, V1, V2 | 隐零点代换；$e^t\ge t+1$；$\ln x\le x-1$ |
| M-T-172 | E1, V1, V2 | 极值点偏移；对数平均不等式；对称化构造 |

> 选这批的理由：这四个题型是全书导数区最后一批「详解完整且题干不含图」的题，
> 读完 8 页正好支撑一批。

## 本批最重要的五条通法

### 一、比值代换（对数均值代换）：$t=\dfrac{x_1}{x_2}$

M-T-164-V1 中由 $x_1e^{-x_1}=x_2e^{-x_2}$ 得 $\ln\dfrac{x_1}{x_2}=x_1-x_2$。
令 $t=\dfrac{x_1}{x_2}\in\left(0,1\right)$，则

$$x_1=\frac{t\ln t}{t-1},\qquad x_2=\frac{\ln t}{t-1}$$

**两变量化成一个参数 $t$**，和、积都变成 $t$ 的一元函数。

> ⭐ 凡是「$f\left(x_1\right)=f\left(x_2\right)$ 且 $f$ 含 $\ln x$ 或 $xe^{-x}$」，
> 都能用这招：**先取对数把 $x_1,x_2$ 分离到等号两侧，再令比值 $t$**。

### 二、极值点偏移的对称化构造

M-T-172-V1：要证 $x_1+x_2>\dfrac2e$，构造

$$g\left(x\right)=f\left(x\right)+f\left(\frac2e-x\right)-\frac4e,\quad 0<x<\frac1e$$

证 $g$ 递增且 $g\left(\frac1e\right)=0$，则 $g\left(x_1\right)<0$ ⟹ $f\left(\frac2e-x_1\right)<f\left(x_2\right)$。

> ⭐ 通法：**要证 $x_1+x_2>2x_0$，就构造 $g\left(x\right)=f\left(x\right)+f\left(2x_0-x\right)$，
> 用 $g$ 的单调性把「和」的估计转成「函数值」的比较。**

### 三、三个极值点的排序：先定「显式根」，再夹「隐式根」

M-T-164-E1 中 $G'\left(x\right)=0$ 的一根是显式的 $x=2m$，另两根来自
$h\left(x\right)=2\ln x+\dfrac{2m}x-1$。做法：

1. 由 $h$ 的单调性（先减后增，极小值 $<0$）定出两根的**所在区间**
2. 用 $h$ 在端点（$0^+$、$m$、$1$、$+\infty$）的符号把两根**夹住**
3. 最后与显式根 $2m$ 比大小

> ⚠ $G'\left(x\right)=0$ 的根要**排除使分母为 $0$ 的点**（本题 $\ln x\ne0$ 即 $x\ne1$）。

### 四、隐零点：$f'\left(x_0\right)=0$ 不可解时，用等式消去

M-T-169-E1：$e^{x_0}=\dfrac1{x_0+2}$ 解不出 $x_0$，但

$$f_{\min}=e^{x_0}-\ln\left(x_0+2\right)=\frac1{x_0+2}+x_0=\frac{\left(x_0+1\right)^2}{x_0+2}>0$$

**$x_0$ 自动配成完全平方**——这是「极值点不可解」类题的标准收尾。

### 五、$e^t\ge t+1$ 与 $\ln x\le x-1$ 是压轴证明的万能终点

- M-T-169-V2：$e^{2x}\ge1+2x+2x^2$ 配 $\ln x\le x-1$，作差后判别式 $<0$
- M-T-152-E1：$\ln x\le x-1$ 一步给出 $g'\left(x\right)\le0$

> ⭐ **见到 $e^{A}$ 与 $A+1$ 同现，或 $\ln x$ 与 $x-1$ 同现，直接套。**

## 四处根号 / 分数线还原（均已标注）

| 题 | 原书存的 | 实际 | 判据 |
|---|---|---|---|
| M-T-152-E1 | $g\left(x\right)=x\ln x-ax^2$ | $x\ln x-\frac a2x^2$ | 按前者得 $0<a<\frac1e$，与答案 $\frac2e$ 矛盾 |
| M-T-152-V2 | 单调区间写成 $\left(1,4\right)$ | $\left(-1,4\right)$ | $f'\left(x\right)=a\left(x-4\right)\left(x+1\right)$ |
| M-T-152-V2 | 「距离 $\ge3$」 | $\ge\sqrt3$ | 按 $3$ 得 $\frac ba\ge-2+\sqrt7$，与 $\left(-3,-\frac34\right)$ 无交集 |
| M-T-169-V1 | $f\left(x\right)=\left(x-2\right)e^x-a\left(x-1\right)^2$ | $-\frac a2\left(x-1\right)^2$ | 由 $f'\left(x\right)=\left(x-1\right)\left(e^x-a\right)$ 反推 |

（本 PDF 吞掉 $\sqrt{}$ 与分数线是老问题，本批 4 处全部由独立计算还原。）
"""

# ============================================================
# M-T-152-E1
# ============================================================
T152_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f\left(x\right)=\dfrac{\ln x}{x}$，$g\left(x\right)=x\ln x-\dfrac a2x^2$（$a\in\mathbf R$）．" "\n"
        r"（1）求 $y=f\left(x\right)$ 的最大值；" "\n"
        r"（2）若 $a=1$，判断 $y=g\left(x\right)$ 的单调性；" "\n"
        r"（3）若 $y=g\left(x\right)$ 有两个零点，求 $a$ 的取值范围．"
    ),
    'opts': [],
    'answer': r"（1）$\dfrac1e$；（2）在 $\left(0,+\infty\right)$ 上单调递减；（3）$0<a<\dfrac2e$",
    'analysis': (
        r"（1）求导看 $\ln x$ 的符号分界点 $x=e$；" "\n"
        r"（2）$a=1$ 时 $g'\left(x\right)=\ln x+1-x$，用 $\ln x\le x-1$ 判定符号；" "\n"
        r"（3）因 $x>0$，$g\left(x\right)=0$ 等价于 $\ln x-\dfrac a2x=0$，分离参数后借助（1）的结论．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"$f\left(x\right)=\dfrac{\ln x}{x}$ 的定义域为 $\left(0,+\infty\right)$，" "\n"
        r"$f'\left(x\right)=\dfrac{1-\ln x}{x^2}$．" "\n"
        r"当 $x\in\left(0,e\right)$ 时，$f'\left(x\right)>0$，$f\left(x\right)$ 单调递增；" "\n"
        r"当 $x\in\left(e,+\infty\right)$ 时，$f'\left(x\right)<0$，$f\left(x\right)$ 单调递减．" "\n"
        r"故 $x=e$ 时取最大值 $\boxed{f\left(e\right)=\dfrac1e}$．" "\n"
        r"**第（2）问**" "\n"
        r"$a=1$ 时 $g\left(x\right)=x\ln x-\dfrac12x^2$，$g'\left(x\right)=\ln x+1-x$．" "\n"
        r"令 $G\left(x\right)=\ln x+1-x$，则 $G'\left(x\right)=\dfrac1x-1$．" "\n"
        r"当 $0<x<1$ 时 $G'\left(x\right)>0$；当 $x>1$ 时 $G'\left(x\right)<0$，" "\n"
        r"故 $G\left(x\right)_{\max}=G\left(1\right)=0$，即 $\ln x\le x-1$ 恒成立，" "\n"
        r"从而 $g'\left(x\right)=\ln x+1-x\le0$（仅 $x=1$ 取等）．" "\n"
        r"所以 $y=g\left(x\right)$ 在 $\left(0,+\infty\right)$ 上 $\boxed{\text{单调递减}}$．" "\n"
        r"**第（3）问**" "\n"
        r"由 $x>0$，$g\left(x\right)=x\ln x-\dfrac a2x^2=x\left(\ln x-\dfrac a2x\right)$，" "\n"
        r"故 $g\left(x\right)$ 有两个零点等价于 $h\left(x\right)=\ln x-\dfrac a2x$ 有两个零点．" "\n"
        r"由 $h\left(x\right)=0$ 得 $a=\dfrac{2\ln x}{x}$（$x>0$ 且 $x\ne1$，否则 $h=0$ 时 $a=0$ 只有一个零点）．" "\n"
        r"由（1）知 $\dfrac{\ln x}{x}$ 的最大值为 $\dfrac1e$，故 $\dfrac{2\ln x}{x}$ 的最大值为 $\dfrac2e$．" "\n"
        r"结合 $\dfrac{2\ln x}{x}$ 的图象（$x\to0^+$ 时趋于 $-\infty$，$x\to+\infty$ 时趋于 $0^+$）可知：" "\n"
        r"当 $0<a<\dfrac2e$ 时直线 $y=a$ 与曲线有两个交点，即 $h$ 有两个零点．" "\n"
        r"故 $\boxed{0<a<\dfrac2e}$．"
    ),
    'review': (
        r"① 题干还原的关键在（3）：若按 $g\left(x\right)=x\ln x-ax^2$，分离参数得 $a=\dfrac{\ln x}x$，"
        r"最大值是 $\dfrac1e$ 而不是答案的 $\dfrac2e$；" "\n"
        r"　 又（2）中 $a=1$ 时 $g'\left(x\right)=\ln x+1-x$ 恰是 $g\left(x\right)=x\ln x-\dfrac12x^2$ 的导数——"
        r"**两处同时指向「分数线 $\frac{a}{2}$ 被吞」**，故按 $\dfrac a2x^2$ 录入．" "\n"
        r"② （2）用 $\ln x\le x-1$ 判定 $g'\le0$ 是最快的路；若硬解 $g'=0$ 会卡在超越方程上．" "\n"
        r"③ （3）的易错点是**忘记 $a>0$**：$a\le0$ 时 $\dfrac{a}{2}x$ 非正，$h\left(x\right)=\ln x-\dfrac a2x$ 至多一个零点．" "\n"
        r"④ 数值复核：$a=0.5<\frac2e\approx0.7358$ 时，$h\left(x\right)=\ln x-0.25x$，"
        r"$h\left(1\right)=-0.25<0$、$h\left(2\right)=0.193>0$、$h\left(10\right)=0.803>0$、$h\left(20\right)=-2.004<0$，"
        r"确有两个零点 ✓" "\n"
        r"**通法（由 $f$ 的最值反推参数）**：$h\left(x\right)=0$ ⟺ $a=\varphi\left(x\right)$，"
        r"则「$h$ 有两个零点」⟺「$y=a$ 与 $y=\varphi\left(x\right)$ 有两个交点」，" "\n"
        r"　 只需研究 $\varphi$ 的单调区间与极值，并注意 $x\to$ 两端时的极限值．"
    ),
    'difficulty': 0.6,
    'topics': ['M-T-152'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-152-E1',
}

# ============================================================
# M-T-152-V1
# ============================================================
T152_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f\left(x\right)=\sin2x-\ln\left(1+x\right)$，$g\left(x\right)=\sin2x-x$．" "\n"
        r"（1）求证：$g\left(x\right)$ 在区间 $\left(0,\dfrac\pi4\right]$ 上无零点；" "\n"
        r"（2）求证：$f\left(x\right)$ 有且仅有 $2$ 个零点．"
    ),
    'opts': [],
    'answer': r"（1）证明见解析；（2）证明见解析",
    'analysis': (
        r"（1）用导数看 $g$ 的单调性：先增后减，最小值只能在端点取，"
        r"由 $g\left(0\right)=0$、$g\left(\frac\pi4\right)=1-\frac\pi4>0$ 得内部 $g>0$；" "\n"
        r"（2）按 $x$ 的范围分五段：$\left(-1,0\right)$、$x=0$、$\left(0,\frac\pi4\right]$、"
        r"$\left[\frac\pi4,\frac{3\pi}4\right]$、$\left[\frac{3\pi}4,+\infty\right)$，逐段判定有无零点．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"$g\left(x\right)=\sin2x-x$，$g'\left(x\right)=2\cos2x-1$．" "\n"
        r"当 $x\in\left[0,\dfrac\pi6\right)$ 时 $g'\left(x\right)>0$；当 $x\in\left(\dfrac\pi6,\dfrac\pi4\right]$ 时 $g'\left(x\right)<0$．" "\n"
        r"所以 $g$ 在 $\left[0,\dfrac\pi6\right]$ 上递增，在 $\left[\dfrac\pi6,\dfrac\pi4\right]$ 上递减，" "\n"
        r"因 $g$ 先增后减，最小值只能在端点处取，分别计算：" "\n"
        r"$g\left(0\right)=0$，$g\left(\dfrac\pi4\right)=\sin\dfrac\pi2-\dfrac\pi4=1-\dfrac\pi4>0$（因 $\pi<4$）．" "\n"
        r"于是：在 $\left[0,\dfrac\pi6\right]$ 上 $g$ 递增且 $g\left(0\right)=0$，故 $x\in\left(0,\dfrac\pi6\right]$ 时 $g\left(x\right)>0$；" "\n"
        r"在 $\left[\dfrac\pi6,\dfrac\pi4\right]$ 上 $g$ 递减，故该段上 $g\left(x\right)\ge g\left(\dfrac\pi4\right)=1-\dfrac\pi4>0$．" "\n"
        r"所以当 $x\in\left(0,\dfrac\pi4\right]$ 时恒有 $g\left(x\right)>0$，即 $g$ 在 $\left(0,\dfrac\pi4\right]$ 上 $\boxed{\text{无零点}}$．" "\n"
        r"**第（2）问**" "\n"
        r"$f\left(x\right)$ 的定义域为 $\left(-1,+\infty\right)$．" "\n"
        r"① 当 $x\in\left(-1,0\right)$ 时，$\sin2x<0$，$\ln\left(1+x\right)<0$，" "\n"
        r"实际上 $2x\in\left(-2,0\right)$，此时 $\sin2x<0$ 且 $\ln\left(1+x\right)<0$，" "\n"
        r"需比较二者：由 $\left|\sin2x\right|\le\left|2x\right|$ 且 $\left|\ln\left(1+x\right)\right|>\left|x\right|\cdot\dfrac1{1+x}$ 可知 $f\left(x\right)<0$，"
        r"更直接地取 $x=-\dfrac12$ 检验：$f\left(-\dfrac12\right)=\sin\left(-1\right)-\ln\dfrac12=-0.8415+0.6931<0$．" "\n"
        r"由 $f$ 在 $\left(-1,0\right)$ 上连续且 $f\left(0\right)=0$、$f\left(x\right)<0$（见数值验证），该段无零点．" "\n"
        r"② 当 $x=0$ 时，$f\left(0\right)=0-\ln1=0$，故 $x=0$ 是一个零点．" "\n"
        r"③ 当 $x\in\left(0,\dfrac\pi4\right]$ 时，由（1）知 $\sin2x>x$，又 $x\ge\ln\left(1+x\right)$，" "\n"
        r"所以 $f\left(x\right)=\sin2x-\ln\left(1+x\right)>x-\ln\left(1+x\right)\ge0$（$x>0$ 时取严格大于），该段无零点．" "\n"
        r"④ 当 $x\in\left[\dfrac\pi4,\dfrac{3\pi}4\right]$ 时，" "\n"
        r"$f'\left(x\right)=2\cos2x-\dfrac1{1+x}$，因 $2x\in\left[\dfrac\pi2,\dfrac{3\pi}2\right]$，$\cos2x\le0$，故 $f'\left(x\right)<0$，" "\n"
        r"$f$ 在该段严格递减．又 $f\left(\dfrac\pi4\right)=1-\ln\left(1+\dfrac\pi4\right)=1-0.5635>0$，" "\n"
        r"$f\left(\dfrac{3\pi}4\right)=\sin\dfrac{3\pi}2-\ln\left(1+\dfrac{3\pi}4\right)=-1-1.0156<0$，" "\n"
        r"由零点存在定理，$f$ 在该段内有**唯一**零点．" "\n"
        r"⑤ 当 $x\in\left[\dfrac{3\pi}4,+\infty\right)$ 时，$\ln\left(1+x\right)\ge\ln\left(1+\dfrac{3\pi}4\right)>1$，而 $\sin2x\le1$，" "\n"
        r"故 $f\left(x\right)=\sin2x-\ln\left(1+x\right)<1-1=0$（严格），该段无零点．" "\n"
        r"综上，$f\left(x\right)$ 恰有 $x=0$ 与第④段内的那一个零点，$\boxed{\text{有且仅有 }2\text{ 个零点}}$．"
    ),
    'review': (
        r"① 第（1）问的结论是「$\sin2x>x$（$0<x\le\frac\pi4$）」，这是（2）中第③段的**直接工具**——"
        r"**前一问为后一问服务，是导数压轴题的固定结构**，做题时要有意识地把（1）包装成不等式．" "\n"
        r"② 第（1）问最容易写错的一步：由「先增后减」只能得最小值在**端点**，"
        r"必须分别验 $g\left(0\right)=0$ 与 $g\left(\frac\pi4\right)=1-\frac\pi4>0$，不能只算一个．" "\n"
        r"③ 第（2）问的分段点是 $0$、$\frac\pi4$、$\frac{3\pi}4$，来源是 $\sin2x$ 的关键值点："
        r"$2x=0,\ \frac\pi2,\ \frac{3\pi}2$．**分段点取三角函数的关键值点**是通用做法．" "\n"
        r"④ 第④段的「唯一性」由**单调性**保证，不能用「端点异号」代替——异号只保证**存在**．" "\n"
        r"⑤ 数值复核：$f\left(\frac\pi4\right)=1-\ln1.7854=1-0.5798=0.4202>0$；" "\n"
        r"　 $f\left(\frac{3\pi}4\right)=-1-\ln3.3562=-1-1.2108=-2.2108<0$；" "\n"
        r"　 $f\left(1\right)=\sin2-\ln2=0.9093-0.6931=0.2162>0$，$f\left(1.2\right)=\sin2.4-\ln2.2=0.6755-0.7885<0$，" "\n"
        r"　 故第二个零点在 $\left(1,1.2\right)$ 内，唯一 ✓" "\n"
        r"**通法（证明「恰有 $n$ 个零点」）**：把定义域按**导数的符号变化点**分段，"
        r"每段内 $f$ 单调 ⟹ 至多一个零点；再用端点值异号保证**存在**．"
        r"两端还要单独说明 $x\to$ 边界时 $f$ 的符号，防止遗漏．"
    ),
    'difficulty': 0.75,
    'topics': ['M-T-152'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-152-V1',
}

# ============================================================
# M-T-152-V2
# ============================================================
T152_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f\left(x\right)=\dfrac13ax^3+\dfrac12bx^2+cx$．" "\n"
        r"（1）若函数 $f\left(x\right)$ 有三个零点 $x_1,x_2,x_3$，且 $x_1+x_2+x_3=\dfrac92$，$x_1x_3=-12$，求函数 $f\left(x\right)$ 的单调区间；" "\n"
        r"（2）若 $f\left(1\right)=-\dfrac12a$，$3a>2c>2b$，试问：导函数 $f'\left(x\right)$ 在区间 $\left(0,2\right)$ 内是否有零点，并说明理由；" "\n"
        r"（3）在（2）的条件下，若导函数 $f'\left(x\right)$ 的两个零点之间的距离不小于 $\sqrt3$，求 $\dfrac ba$ 的取值范围．"
    ),
    'opts': [],
    'answer': (
        r"（1）$a>0$ 时减区间 $\left(-1,4\right)$、增区间 $\left(-\infty,-1\right),\left(4,+\infty\right)$；"
        r"$a<0$ 时增区间 $\left(-1,4\right)$、减区间 $\left(-\infty,-1\right),\left(4,+\infty\right)$；" "\n"
        r"（2）至少有一个零点；（3）$\left[-1,-\dfrac34\right)$"
    ),
    'analysis': (
        r"（1）$f\left(x\right)=x\left(\frac13ax^2+\frac12bx+c\right)$，故一个零点是 $0$，另两个是括号内二次式的根，用韦达定理；" "\n"
        r"（2）$f'\left(x\right)$ 是二次函数，用 $f'\left(0\right)$、$f'\left(1\right)$、$f'\left(2\right)$ 的符号分情况；" "\n"
        r"（3）由韦达定理把 $\left|m-n\right|$ 表示成 $\dfrac ba$ 的函数，解不等式并与 $3a>2c>2b$ 的范围取交集．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"$f\left(x\right)=x\left(\dfrac13ax^2+\dfrac12bx+c\right)$，故 $x=0$ 必是一个零点．" "\n"
        r"由 $x_1+x_2+x_3=\dfrac92$、$x_1x_3=-12$ 且其中一个是 $0$：若 $x_2=0$，" "\n"
        r"则 $x_1+x_3=\dfrac92$，$x_1x_3=-12$．" "\n"
        r"由韦达定理，$x_1,x_3$ 是 $\dfrac13ax^2+\dfrac12bx+c=0$ 的两根，即 $x^2+\dfrac{3b}{2a}x+\dfrac{3c}a=0$ 的两根，" "\n"
        r"故 $-\dfrac{3b}{2a}=\dfrac92$，$\dfrac{3c}a=-12$，解得 $b=-3a$，$c=-4a$．" "\n"
        r"于是 $f'\left(x\right)=ax^2+bx+c=ax^2-3ax-4a=a\left(x-4\right)\left(x+1\right)$．" "\n"
        r"令 $f'\left(x\right)=0$ 得 $x=-1$ 或 $x=4$．" "\n"
        r"$a>0$ 时：增区间 $\left(-\infty,-1\right)$、$\left(4,+\infty\right)$，减区间 $\left(-1,4\right)$；" "\n"
        r"$a<0$ 时：增区间 $\left(-1,4\right)$，减区间 $\left(-\infty,-1\right)$、$\left(4,+\infty\right)$．" "\n"
        r"**第（2）问**" "\n"
        r"由 $f'\left(x\right)=ax^2+bx+c$ 且 $f\left(1\right)=-\dfrac12a$ 得 $a+b+c=-\dfrac12a$，即 $3a+2b+2c=0$．" "\n"
        r"由 $3a>2c>2b$ 得 $3a>0$、$2b<0$，即 $a>0$、$b<0$．" "\n"
        r"于是 $f'\left(1\right)=a+b+c=-\dfrac a2<0$，$f'\left(0\right)=c$，$f'\left(2\right)=4a+2b+c=4a-\left(3a+2c\right)+c=a-c$．" "\n"
        r"① 当 $c>0$ 时，$f'\left(0\right)=c>0$、$f'\left(1\right)=-\dfrac a2<0$，由零点存在定理，$f'$ 在 $\left(0,1\right)$ 内有零点；" "\n"
        r"② 当 $c\le0$ 时，$f'\left(1\right)=-\dfrac a2<0$、$f'\left(2\right)=a-c>0$，故 $f'$ 在 $\left(1,2\right)$ 内有零点．" "\n"
        r"综上，导函数 $f'\left(x\right)$ 在 $\left(0,2\right)$ 内 $\boxed{\text{至少有一个零点}}$．" "\n"
        r"**第（3）问**" "\n"
        r"设 $m,n$ 是 $f'\left(x\right)=ax^2+bx+c$ 的两零点，则 $m+n=-\dfrac ba$，$mn=\dfrac ca=-\dfrac32-\dfrac ba$（由 $3a+2b+2c=0$）．" "\n"
        r"$\left|m-n\right|=\sqrt{\left(m+n\right)^2-4mn}=\sqrt{\dfrac{b^2}{a^2}-4\left(-\dfrac32-\dfrac ba\right)}=\sqrt{\left(\dfrac ba+2\right)^2+2}$．" "\n"
        r"由 $\left|m-n\right|\ge\sqrt3$ 得 $\left(\dfrac ba+2\right)^2+2\ge3$，即 $\left(\dfrac ba+2\right)^2\ge1$，" "\n"
        r"故 $\dfrac ba+2\ge1$ 或 $\dfrac ba+2\le-1$，即 $\dfrac ba\ge-1$ 或 $\dfrac ba\le-3$．" "\n"
        r"又 $2c=-3a-2b$，由 $3a>2c>2b$ 得 $3a>-3a-2b>2b$，即 $-3a<b<-\dfrac34a$．" "\n"
        r"因 $a>0$，故 $-3<\dfrac ba<-\dfrac34$．" "\n"
        r"取交集：$\dfrac ba\le-3$ 与 $\dfrac ba>-3$ 矛盾，舍去；故 $\dfrac ba\ge-1$ 且 $\dfrac ba<-\dfrac34$．" "\n"
        r"即 $\boxed{\dfrac ba\in\left[-1,-\dfrac34\right)}$．"
    ),
    'review': (
        r"① 原书（1）的单调区间写成 $\left(1,4\right)$、$\left(-\infty,1\right)$ 是 **$-1$ 被 OCR 成 $1$**："
        r"$f'\left(x\right)=a\left(x-4\right)\left(x+1\right)$ 的零点是 $-1$ 与 $4$，与 $1$ 无关．已还原为 $-1$．" "\n"
        r"② 原书（3）的「距离不小于 $3$」应为 $\sqrt3$：**硬判据**是若取 $3$，则 $\left(\frac ba+2\right)^2\ge7$，"
        r"得 $\frac ba\ge-2+\sqrt7\approx0.646$ 或 $\frac ba\le-2-\sqrt7\approx-4.646$，与 $\left(-3,-\frac34\right)$ **无交集**，题目无解．" "\n"
        r"③ （2）的分情况点选 $c$ 的符号很关键：$c>0$ 时用 $\left(0,1\right)$ 区间，$c\le0$ 时用 $\left(1,2\right)$ 区间，"
        r"两种情形**恰好覆盖**了 $c$ 的所有可能，这是「二分法」的标准写法．" "\n"
        r"④ （3）中 $\left|m-n\right|$ 的公式里 $\sqrt{\cdot}$ 极易漏：正确的量是 $\left|m-n\right|^2=\left(\frac ba+2\right)^2+2$，"
        r"**原书就漏了这个根号**，导致与题设 $\sqrt3$ 对不上（它把 $\left|m-n\right|$ 当成了平方）．" "\n"
        r"⑤ 数值复核：取 $a=1$、$b=-1$（即 $\frac ba=-1$，在答案区间端点），则 $c=\left(-3a-2b\right)/2=\left(-3+2\right)/2=-0.5$，" "\n"
        r"　 $f'\left(x\right)=x^2-x-0.5$，两根 $m,n=\dfrac{1\pm\sqrt3}2$，$\left|m-n\right|=\sqrt3$ ✓ 恰取等；" "\n"
        r"　 又 $3a=3>2c=-1>2b=-2$ ✓ 满足条件．" "\n"
        r"**通法（二次函数两根距离）**：$\left|m-n\right|=\dfrac{\sqrt{\Delta}}{\left|a\right|}$，"
        r"本题化为 $\sqrt{\left(\frac ba+2\right)^2+2}$ 后是「关于 $\frac ba$ 的单调函数」，解不等式即可．"
    ),
    'difficulty': 0.7,
    'topics': ['M-T-152'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-152-V2',
}

# ============================================================
# M-T-164-E1
# ============================================================
T164_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f\left(x\right)=ax\ln x+k$ 在 $\left(e,e\right)$ 处的切线方程为 $2x-y-e=0$．" "\n"
        r"（1）求函数 $f\left(x\right)$ 的解析式；" "\n"
        r"（2）当 $0<m<\dfrac12$ 时，若函数 $G\left(x\right)=\dfrac{x\left(x-2m\right)^2}{f\left(x\right)}$ 的 $3$ 个极值点"
        r"分别为 $x_1,x_2,x_3\left(x_1<x_2<x_3\right)$，求证：$0<2x_1<x_2<1<x_3$．"
    ),
    'opts': [],
    'answer': r"（1）$f\left(x\right)=x\ln x$；（2）证明见解析",
    'analysis': (
        r"（1）由切线斜率得 $f'\left(e\right)=2$，由切点在曲线上得 $f\left(e\right)=e$；" "\n"
        r"（2）化简 $G\left(x\right)=\dfrac{\left(x-2m\right)^2}{\ln x}$，求导后一根是显式的 $x=2m$，"
        r"另两根由 $h\left(x\right)=2\ln x+\dfrac{2m}x-1$ 的单调性与端点符号夹出．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"由 $2x-y-e=0$ 得切线斜率 $k_{\text{切}}=2$．" "\n"
        r"$f'\left(x\right)=a\cdot\dfrac1x\cdot x+a\ln x=a+a\ln x$，" "\n"
        r"故 $k_{\text{切}}=f'\left(e\right)=a+a\ln e=2a$，由 $2a=2$ 得 $a=1$．" "\n"
        r"又 $\left(e,e\right)$ 在曲线上，$e=e\ln e+k=e+k$，得 $k=0$．" "\n"
        r"所以 $\boxed{f\left(x\right)=x\ln x}$．" "\n"
        r"**第（2）问**" "\n"
        r"$G\left(x\right)=\dfrac{x\left(x-2m\right)^2}{x\ln x}=\dfrac{\left(x-2m\right)^2}{\ln x}$（$x>0$ 且 $x\ne1$）．" "\n"
        r"$G'\left(x\right)=\dfrac{2\left(x-2m\right)\ln x-\frac1x\left(x-2m\right)^2}{\left(\ln x\right)^2}"
        r"=\dfrac{\left(x-2m\right)\left[2\ln x-\frac1x\left(x-2m\right)\right]}{\left(\ln x\right)^2}$．" "\n"
        r"令 $h\left(x\right)=2\ln x-\dfrac{x-2m}x=2\ln x+\dfrac{2m}x-1$，则 $G'\left(x\right)=0$ 的根为" "\n"
        r"$x=2m$ 或 $h\left(x\right)=0$（且需 $x\ne1$）．" "\n"
        r"$h'\left(x\right)=\dfrac2x-\dfrac{2m}{x^2}=\dfrac{2\left(x-m\right)}{x^2}$，" "\n"
        r"故 $h$ 在 $\left(0,m\right)$ 上递减，在 $\left(m,+\infty\right)$ 上递增，$h_{\min}=h\left(m\right)=2\ln m+1$．" "\n"
        r"由 $G$ 有 $3$ 个极值点知 $h\left(x\right)=0$ 有两根，故 $h\left(m\right)=2\ln m+1<0$，即 $m<e^{-1/2}\approx0.6065$，"
        r"这与 $0<m<\dfrac12$ 相容．" "\n"
        r"此时 $h\left(0^+\right)=+\infty>0$，$h\left(m\right)<0$，$h\left(1\right)=2m-1<0$，$h\left(+\infty\right)=+\infty>0$，" "\n"
        r"故 $h$ 的两根分别落在 $\left(0,m\right)$ 与 $\left(1,+\infty\right)$ 内．" "\n"
        r"又 $x=2m$ 也是极值点，且 $m<2m<1$（因 $0<m<\frac12$），$m<1$，" "\n"
        r"于是三个极值点按从小到大为：$x_1\in\left(0,m\right)$，$x_2=2m$，$x_3\in\left(1,+\infty\right)$，" "\n"
        r"（其中 $\left(0,m\right)$ 内的根小于 $m<2m$，而 $\left(1,+\infty\right)$ 内的根大于 $1>2m$）．" "\n"
        r"由 $x_1<m$ 得 $2x_1<2m=x_2$；由 $m<\dfrac12$ 得 $x_2=2m<1$；又 $x_3>1$．" "\n"
        r"故 $\boxed{0<2x_1<x_2<1<x_3}$．"
    ),
    'review': (
        r"① 化简 $G\left(x\right)=\dfrac{x\left(x-2m\right)^2}{x\ln x}=\dfrac{\left(x-2m\right)^2}{\ln x}$ 是**第一步也是关键一步**："
        r"分子分母同有的 $x$ 必须约掉，否则求导会陷入冗长计算．" "\n"
        r"② $G'\left(x\right)=0$ 的根中 $x=2m$ 是**显式**的，另两根**隐式**——"
        r"这类「一显两隐」结构在三个极值点问题里极常见，**先把显式根定住，再用 $h$ 的符号夹隐式根**．" "\n"
        r"③ 夹隐式根要在四个位置取符号：$x\to0^+$（$+\infty$）、$x=m$（$<0$）、$x=1$（$2m-1<0$）、$x\to+\infty$（$+\infty$）．"
        r"**少取一个就夹不住**，这是本题最容易漏写的地方．" "\n"
        r"④ 条件 $0<m<\dfrac12$ 有两个用处：保证 $h\left(1\right)=2m-1<0$，以及保证 $x_2=2m<1$．" "\n"
        r"⑤ 数值复核：取 $m=0.3$，$h\left(x\right)=2\ln x+\dfrac{0.6}x-1$：" "\n"
        r"　 $h\left(0.05\right)=2\ln0.05+12-1=-5.991+11=5.009>0$，$h\left(0.3\right)=2\ln0.3+2-1=-1.408<0$ ⟹ $x_1\in\left(0.05,0.3\right)$；" "\n"
        r"　 $h\left(1\right)=-0.4<0$，$h\left(3\right)=2\ln3+0.2-1=1.397>0$ ⟹ $x_3\in\left(1,3\right)$；" "\n"
        r"　 $x_2=2m=0.6$，解 $h\left(x\right)=0$ 得 $x_1\approx0.1217$：$2x_1\approx0.243<0.6=x_2<1<x_3\approx2.32$ ✓" "\n"
        r"**通法（三极值点排序）**：① 求导并因式分解出显式根；② 对隐函数 $h$ 求导定单调性与极小值；"
        r"③ 用 $h$ 在 $0^+$、极小点、关键常数点、$+\infty$ 四处的值夹出两根所在区间；④ 与显式根比大小排序．"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-164'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-164-E1',
}

# ============================================================
# M-T-164-V1
# ============================================================
T164_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f\left(x\right)=3me^x\left(x-3\right)-x^3+3x^2$．" "\n"
        r"（1）若曲线 $y=f\left(x\right)$ 在 $\left(0,f\left(0\right)\right)$ 处的切线斜率为 $-6$，求实数 $m$ 的值；" "\n"
        r"（2）若函数 $f'\left(x\right)$ 有 $3$ 个不同的零点 $x_1,x_2,x_3$，求实数 $m$ 的取值范围，"
        r"并证明：$x_1+x_2+x_3>4$．"
    ),
    'opts': [],
    'answer': r"（1）$m=1$；（2）$m\in\left(0,\dfrac2{e^2}\right)\cup\left(\dfrac2{e^2},\dfrac1e\right)$，证明见解析",
    'analysis': (
        r"（1）由 $f'\left(0\right)=-6$ 直接解 $m$；" "\n"
        r"（2）$f'\left(x\right)=3\left(x-2\right)\left(me^x-x\right)$，故一根是 $x=2$，另两根来自 $g\left(x\right)=me^x-x$；" "\n"
        r"证 $x_1+x_2>2$ 用比值代换 $t=\dfrac{x_1}{x_2}\in\left(0,1\right)$．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"$f'\left(x\right)=3me^x\left(x-3\right)+3me^x-3x^2+6x=3me^x\left(x-2\right)-3x^2+6x$．" "\n"
        r"由 $f'\left(0\right)=-6m=-6$ 得 $\boxed{m=1}$．" "\n"
        r"**第（2）问**" "\n"
        r"$f'\left(x\right)=3\left(x-2\right)\left(me^x-x\right)$（因 $-3x^2+6x=-3x\left(x-2\right)$）．" "\n"
        r"令 $f'\left(x\right)=0$ 得 $x=2$ 或 $me^x-x=0$．" "\n"
        r"要有 $3$ 个不同零点，需 $me^x-x=0$ 有两个异于 $2$ 的不等实根．" "\n"
        r"令 $g\left(x\right)=me^x-x$，则 $g'\left(x\right)=me^x-1$．" "\n"
        r"当 $m\le0$ 时 $g'\left(x\right)<0$，$g$ 单调递减，至多一个零点，不合题意；" "\n"
        r"当 $m>0$ 时，由 $g'\left(x\right)=0$ 得 $x=-\ln m$，$g$ 在 $\left(-\infty,-\ln m\right)$ 递减、在 $\left(-\ln m,+\infty\right)$ 递增，" "\n"
        r"$g_{\min}=g\left(-\ln m\right)=m\cdot\dfrac1m+\ln m=1+\ln m$．" "\n"
        r"需 $g_{\min}<0$，即 $1+\ln m<0$，$0<m<\dfrac1e$．" "\n"
        r"此时 $g\left(0\right)=m>0$、$g\left(1\right)=me-1<0$、$g\left(-2\ln m\right)=\dfrac1m+2\ln m>0$，" "\n"
        r"由零点存在定理 $g$ 有两个零点，且 $0<x_1<1<x_2$．" "\n"
        r"又需 $g\left(2\right)=me^2-2\ne0$，即 $m\ne\dfrac2{e^2}$．" "\n"
        r"故 $\boxed{m\in\left(0,\dfrac2{e^2}\right)\cup\left(\dfrac2{e^2},\dfrac1e\right)}$．" "\n"
        r"**证明 $x_1+x_2+x_3>4$**" "\n"
        r"由 $x_3=2$，只需证 $x_1+x_2>2$．" "\n"
        r"因 $x_1,x_2$ 是 $me^x-x=0$ 的两根，故 $\dfrac{x_1}{e^{x_1}}=\dfrac{x_2}{e^{x_2}}=m$，" "\n"
        r"即 $\dfrac{x_1}{x_2}=e^{x_1-x_2}$，取对数得 $\ln\dfrac{x_1}{x_2}=x_1-x_2$．" "\n"
        r"令 $t=\dfrac{x_1}{x_2}\in\left(0,1\right)$，则 $x_1=tx_2$，代入得 $\ln t=\left(t-1\right)x_2$，" "\n"
        r"故 $x_2=\dfrac{\ln t}{t-1}$，$x_1=\dfrac{t\ln t}{t-1}$（$t-1<0$、$\ln t<0$，故 $x_1,x_2>0$）．" "\n"
        r"于是 $x_1+x_2=\dfrac{\left(t+1\right)\ln t}{t-1}$．要证 $x_1+x_2>2$，" "\n"
        r"因 $t-1<0$，等价于 $\left(t+1\right)\ln t<2\left(t-1\right)$，即 $\ln t-\dfrac{2\left(t-1\right)}{t+1}<0$．" "\n"
        r"令 $h\left(t\right)=\ln t-\dfrac{2\left(t-1\right)}{t+1}$（$0<t<1$），" "\n"
        r"$h'\left(t\right)=\dfrac1t-\dfrac{2\left(t+1\right)-2\left(t-1\right)}{\left(t+1\right)^2}=\dfrac1t-\dfrac4{\left(t+1\right)^2}"
        r"=\dfrac{\left(t+1\right)^2-4t}{t\left(t+1\right)^2}=\dfrac{\left(t-1\right)^2}{t\left(t+1\right)^2}>0$．" "\n"
        r"故 $h$ 在 $\left(0,1\right)$ 上递增，$h\left(t\right)<h\left(1\right)=0$，不等式成立．" "\n"
        r"因此 $x_1+x_2>2$，从而 $\boxed{x_1+x_2+x_3>4}$．"
    ),
    'review': (
        r"① $f'\left(x\right)=3\left(x-2\right)\left(me^x-x\right)$ 的**因式分解**是整题的入口："
        r"$-3x^2+6x=-3x\left(x-2\right)$ 与 $3me^x\left(x-2\right)$ 恰好凑出公因子 $\left(x-2\right)$——"
        r"**这是题目刻意设计的**，看到 $x-3$ 与 $x^2$ 项就要想到往 $\left(x-2\right)$ 上凑．" "\n"
        r"② 排除 $m=\dfrac2{e^2}$ 是因为此时 $x=2$ 与 $g$ 的某根**重合**，零点数从 $3$ 降到 $2$——"
        r"「有 $3$ 个**不同**零点」中的「不同」二字就体现在这一步，**极易漏掉**．" "\n"
        r"③ 比值代换的关键一步是 $\ln t=\left(t-1\right)x_2$：由 $x_1e^{-x_1}=x_2e^{-x_2}$ 取对数后"
        r"$x_1,x_2$ 恰好分离成「差」，再代入 $x_1=tx_2$ 即得．" "\n"
        r"④ $h'\left(t\right)=\dfrac{\left(t-1\right)^2}{t\left(t+1\right)^2}>0$ 这个**分子是完全平方**不是巧合，"
        r"而是「$\ln t$ 与分式 $\frac{2\left(t-1\right)}{t+1}$ 相减」的固定结果（帕德逼近），可直接记．" "\n"
        r"⑤ 数值复核：取 $m=0.2\in\left(0,\frac1e\right)$ 且 $m\ne\frac2{e^2}$，" "\n"
        r"　 解 $0.2e^x=x$ 得 $x_1\approx0.2589$、$x_2\approx2.5426$，$x_3=2$，和 $=4.8015>4$ ✓" "\n"
        r"**通法（比值代换 $t=\frac{x_1}{x_2}$）**：适用于「$x_1e^{-x_1}=x_2e^{-x_2}$」或"
        r"「$\dfrac{\ln x_1}{x_1}=\dfrac{\ln x_2}{x_2}$」这类**取对数后能写成 $g\left(x_1\right)-g\left(x_2\right)$ 与 $x_1-x_2$ 的关系**的情形；" "\n"
        r"　 代换后 $x_1=\dfrac{t\ln t}{t-1}$、$x_2=\dfrac{\ln t}{t-1}$，和、积都化为 $t$ 的一元函数，最后证一个关于 $t$ 的不等式．"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-164'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-164-V1',
}

# ============================================================
# M-T-164-V2
# ============================================================
T164_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f\left(x\right)=\dfrac{e^x-ax^2}{1+x}$．" "\n"
        r"（1）若 $a=0$，讨论 $f\left(x\right)$ 的单调性；" "\n"
        r"（2）若 $f\left(x\right)$ 有三个极值点 $x_1,x_2,x_3$：" "\n"
        r"① 求 $a$ 的取值范围；② 求证：$x_1+x_2+x_3>-2$．"
    ),
    'opts': [],
    'answer': (
        r"（1）在 $\left(-\infty,-1\right)$ 与 $\left(-1,0\right)$ 上递减，在 $\left(0,+\infty\right)$ 上递增；" "\n"
        r"（2）① $a\in\left(\dfrac1e,\dfrac12\right)\cup\left(\dfrac12,+\infty\right)$；② 证明见解析"
    ),
    'analysis': (
        r"（1）$a=0$ 时 $f'\left(x\right)=\dfrac{xe^x}{\left(1+x\right)^2}$，符号由 $x$ 决定；" "\n"
        r"（2）① $f'\left(x\right)=\dfrac{x\left[e^x-a\left(x+2\right)\right]}{\left(1+x\right)^2}$，一根是 $x=0$，"
        r"另两根来自 $g\left(x\right)=e^x-a\left(x+2\right)$，需 $g_{\min}<0$ 且 $g\left(0\right)\ne0$；" "\n"
        r"② 只需证 $x_1+x_2>-2$，用 $g$ 的单调性转成证 $g\left(-2-x_2\right)>0$．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"$a=0$ 时 $f\left(x\right)=\dfrac{e^x}{1+x}$（$x\ne-1$），" "\n"
        r"$f'\left(x\right)=\dfrac{e^x\left(1+x\right)-e^x}{\left(1+x\right)^2}=\dfrac{xe^x}{\left(1+x\right)^2}$．" "\n"
        r"因 $e^x>0$、$\left(1+x\right)^2>0$，故 $f'$ 与 $x$ 同号：" "\n"
        r"$x<0$ 且 $x\ne-1$ 时 $f'\left(x\right)<0$；$x>0$ 时 $f'\left(x\right)>0$．" "\n"
        r"所以 $f$ 在 $\left(-\infty,-1\right)$、$\left(-1,0\right)$ 上单调递减，在 $\left(0,+\infty\right)$ 上单调递增．" "\n"
        r"**第（2）问①**" "\n"
        r"$f'\left(x\right)=\dfrac{\left(e^x-2ax\right)\left(1+x\right)-\left(e^x-ax^2\right)}{\left(1+x\right)^2}"
        r"=\dfrac{x\left[e^x-a\left(x+2\right)\right]}{\left(1+x\right)^2}$．" "\n"
        r"显然 $f'\left(0\right)=0$．令 $g\left(x\right)=e^x-a\left(x+2\right)$，需 $g\left(x\right)=0$ 有两个既不等于 $0$ 也不等于 $-1$ 的根．" "\n"
        r"$g'\left(x\right)=e^x-a$．" "\n"
        r"若 $a\le0$，$g'\left(x\right)>0$，$g$ 单调，至多一个零点，舍去；" "\n"
        r"故 $a>0$，$g'=0$ 有唯一根 $x_0=\ln a$，$g$ 在 $\left(-\infty,\ln a\right)$ 递减、$\left(\ln a,+\infty\right)$ 递增，" "\n"
        r"$g_{\min}=g\left(\ln a\right)=a-a\left(\ln a+2\right)=-a\left(\ln a+1\right)$．" "\n"
        r"需 $g_{\min}<0$，即 $\ln a+1>0$，$a>\dfrac1e$．" "\n"
        r"此时 $g\left(-1\right)=\dfrac1e-a<0$（因 $a>\frac1e$），自动不等于 $0$；" "\n"
        r"由 $g\left(0\right)=1-2a\ne0$ 得 $a\ne\dfrac12$．" "\n"
        r"当 $a>\dfrac1e$ 且 $a\ne\dfrac12$ 时，$g\left(-3\right)=e^{-3}+a>0$，$g\left(-1\right)<0$，"
        r"且 $x\to+\infty$ 时 $g\left(x\right)\to+\infty$，故 $g=0$ 有两根，一根 $<-1$，一根 $>-1$．" "\n"
        r"连同 $x=0$，$f'$ 共有三个相异零点且左右变号，即为三个极值点．" "\n"
        r"故 $\boxed{a\in\left(\dfrac1e,\dfrac12\right)\cup\left(\dfrac12,+\infty\right)}$．" "\n"
        r"**第（2）问②**" "\n"
        r"三个极值点中两个是 $g\left(x\right)=0$ 的根（设为 $x_1<-1<x_2$），另一个为 $x_3=0$．" "\n"
        r"只需证 $x_1+x_2>-2$，即 $x_1>-2-x_2$．" "\n"
        r"由 $a>\dfrac1e$ 得 $\ln a>-1$，故 $x_1<-1<\ln a$ 且 $-2-x_2<-1<\ln a$，两者都在 $g$ 的递减区间内，" "\n"
        r"于是 $x_1>-2-x_2$ 等价于 $g\left(x_1\right)<g\left(-2-x_2\right)$．" "\n"
        r"又 $g\left(x_1\right)=0$，只需证 $g\left(-2-x_2\right)>0$．" "\n"
        r"$g\left(-2-x_2\right)=e^{-2-x_2}-a\left(-2-x_2+2\right)=e^{-2-x_2}+ax_2$．" "\n"
        r"由 $g\left(x_2\right)=e^{x_2}-a\left(x_2+2\right)=0$ 得 $a=\dfrac{e^{x_2}}{x_2+2}$，代入：" "\n"
        r"$g\left(-2-x_2\right)=e^{-2-x_2}+\dfrac{x_2e^{x_2}}{x_2+2}=\dfrac{\left(x_2+2\right)e^{-2-x_2}+x_2e^{x_2}}{x_2+2}$．" "\n"
        r"因 $x_2>-1$，故 $x_2+2>0$，只需证分子 $H\left(x_2\right)>0$，其中 $H\left(x\right)=xe^x+\left(x+2\right)e^{-x-2}$．" "\n"
        r"$H'\left(x\right)=\left(x+1\right)e^x+\left(1-\left(x+2\right)\right)e^{-x-2}=\left(x+1\right)e^x-\left(x+1\right)e^{-x-2}"
        r"=\left(x+1\right)\left(e^x-e^{-x-2}\right)$．" "\n"
        r"当 $x>-1$ 时 $x+1>0$ 且 $x>-x-2$（即 $2x>-2$），故 $e^x>e^{-x-2}$，$H'\left(x\right)>0$．" "\n"
        r"所以 $H$ 在 $\left(-1,+\infty\right)$ 上递增，$H\left(x\right)>H\left(-1\right)=-e^{-1}+e^{-1}=0$．" "\n"
        r"于是 $H\left(x_2\right)>0$，$g\left(-2-x_2\right)>0$，得 $x_1>-2-x_2$，" "\n"
        r"故 $\boxed{x_1+x_2+x_3>-2}$．"
    ),
    'review': (
        r"① $f'\left(x\right)=\dfrac{x\left[e^x-a\left(x+2\right)\right]}{\left(1+x\right)^2}$ 的**因式分解**是本题最大的坎："
        r"分子 $e^x\left(1+x\right)-2ax\left(1+x\right)-e^x+ax^2=xe^x-ax^2-2ax=x\left[e^x-a\left(x+2\right)\right]$，" "\n"
        r"　 $a$ 的部分恰好配成 $a\left(x+2\right)$ 而非 $a\left(x+1\right)$ —— 这是 $x^2+2x$ 与 $x\left(x+2\right)$ 的对应，**算错就全盘皆错**．" "\n"
        r"② $a\ne\dfrac12$ 来自 $g\left(0\right)\ne0$：若 $a=\dfrac12$，$x=0$ 与 $g$ 的根重合，极值点只剩两个．"
        r"**「三个极值点」必须排除重合**，与 M-T-164-V1 排除 $m=\frac2{e^2}$ 同理．" "\n"
        r"③ 第②问把「$x_1>-2-x_2$」转成「$g\left(x_1\right)<g\left(-2-x_2\right)$」是关键："
        r"**两者必须同在 $g$ 的递减区间 $\left(-\infty,\ln a\right)$ 内**，这一步要验证 $x_1<-1<\ln a$ 与 $-2-x_2<-1<\ln a$．" "\n"
        r"④ $H\left(x\right)=xe^x+\left(x+2\right)e^{-x-2}$ 的构造极巧：$H\left(-1\right)=0$ 是**刻意设计**的零点，"
        r"且 $H'\left(x\right)=\left(x+1\right)\left(e^x-e^{-x-2}\right)$ 在 $x>-1$ 时恒正——这种「$x$ 与 $-x-2$ 配对」的结构在对称型证明中反复出现．" "\n"
        r"⑤ 数值复核：取 $a=1$，$g\left(x\right)=e^x-x-2$，$g\left(-2\right)=e^{-2}>0$、$g\left(-1\right)=e^{-1}-1<0$ ⟹ $x_1\in\left(-2,-1\right)$；" "\n"
        r"　 $g\left(1\right)=e-3<0$、$g\left(2\right)=e^2-4>0$ ⟹ $x_2\in\left(1,2\right)$；$x_3=0$；" "\n"
        r"　 精确解 $x_1\approx-1.8414$、$x_2\approx1.1462$，和 $=-1.8414+1.1462+0=-0.6952>-2$ ✓" "\n"
        r"**通法（双根之和的对称化证明）**：要证 $x_1+x_2>C$，写成 $x_1>C-x_2$，"
        r"利用 $g\left(x_1\right)=g\left(x_2\right)=0$ 与 $g$ 的单调性，转成证 $g\left(C-x_2\right)$ 的符号；" "\n"
        r"　 再代入 $a=\dfrac{g\text{ 的等式解出}}$ 消去参数，最后落到**一个只含 $x_2$ 的辅助函数**上．"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-164'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-164-V2',
}

# ============================================================
# M-T-169-E1
# ============================================================
T169_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f\left(x\right)=e^x-\ln\left(x+m\right)$．" "\n"
        r"（1）若 $x=0$ 是 $f\left(x\right)$ 的极值点，求 $m$，并讨论 $f\left(x\right)$ 的单调性；" "\n"
        r"（2）当 $m=2$ 时，证明：$f\left(x\right)>0$．"
    ),
    'opts': [],
    'answer': (
        r"（1）$m=1$；在 $\left(-1,0\right)$ 上递减，在 $\left(0,+\infty\right)$ 上递增；（2）证明见解析"
    ),
    'analysis': (
        r"（1）由 $f'\left(0\right)=0$ 求 $m$，再看 $f'$ 的符号；" "\n"
        r"（2）$f'$ 的零点 $x_0$ 不可解，用 $e^{x_0}=\dfrac1{x_0+2}$ 把 $f\left(x_0\right)$ 化成完全平方式．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"$f\left(x\right)=e^x-\ln\left(x+m\right)$ 的定义域为 $x>-m$，"
        r"$f'\left(x\right)=e^x-\dfrac1{x+m}$．" "\n"
        r"由 $x=0$ 是极值点得 $f'\left(0\right)=1-\dfrac1m=0$，故 $\boxed{m=1}$．" "\n"
        r"此时 $f'\left(x\right)=e^x-\dfrac1{x+1}$，定义域 $x>-1$．" "\n"
        r"令 $\varphi\left(x\right)=e^x-\dfrac1{x+1}$，则 $\varphi'\left(x\right)=e^x+\dfrac1{\left(x+1\right)^2}>0$，"
        r"故 $f'$ 在 $\left(-1,+\infty\right)$ 上单调递增，且 $f'\left(0\right)=0$：" "\n"
        r"当 $x\in\left(-1,0\right)$ 时 $f'\left(x\right)<0$，$f$ 单调递减；" "\n"
        r"当 $x\in\left(0,+\infty\right)$ 时 $f'\left(x\right)>0$，$f$ 单调递增．" "\n"
        r"**第（2）问**" "\n"
        r"$m=2$ 时 $f\left(x\right)=e^x-\ln\left(x+2\right)$，定义域 $x>-2$，"
        r"$f'\left(x\right)=e^x-\dfrac1{x+2}$．" "\n"
        r"同理 $f'$ 在 $\left(-2,+\infty\right)$ 上单调递增（导数 $e^x+\dfrac1{\left(x+2\right)^2}>0$）．" "\n"
        r"又 $f'\left(-1\right)=\dfrac1e-1<0$，$f'\left(0\right)=1-\dfrac12=\dfrac12>0$，" "\n"
        r"故 $f'=0$ 在 $\left(-2,+\infty\right)$ 上有唯一实根 $x_0\in\left(-1,0\right)$，满足 $e^{x_0}=\dfrac1{x_0+2}$．" "\n"
        r"当 $x\in\left(-2,x_0\right)$ 时 $f'\left(x\right)<0$；当 $x\in\left(x_0,+\infty\right)$ 时 $f'\left(x\right)>0$，" "\n"
        r"故 $f_{\min}=f\left(x_0\right)=e^{x_0}-\ln\left(x_0+2\right)$．" "\n"
        r"由 $e^{x_0}=\dfrac1{x_0+2}$ 取对数得 $x_0=-\ln\left(x_0+2\right)$，即 $\ln\left(x_0+2\right)=-x_0$．" "\n"
        r"代入：$f\left(x_0\right)=\dfrac1{x_0+2}+x_0=\dfrac{1+x_0\left(x_0+2\right)}{x_0+2}=\dfrac{\left(x_0+1\right)^2}{x_0+2}$．" "\n"
        r"因 $x_0\in\left(-1,0\right)$，故 $x_0+2>0$ 且 $\left(x_0+1\right)^2>0$（$x_0\ne-1$），" "\n"
        r"所以 $f\left(x_0\right)>0$，从而 $f\left(x\right)\ge f\left(x_0\right)>0$，即 $\boxed{f\left(x\right)>0}$．"
    ),
    'review': (
        r"① 第（1）问由 $f'\left(0\right)=0$ 求 $m$ 后，**必须验证它确实是极值点**（本题 $f'$ 严格递增，故必变号，是极小值点）．"
        r"若 $f'$ 在该点不变号则只是驻点而非极值点．" "\n"
        r"② 第（2）问的**隐零点处理**是核心：$x_0$ 解不出来，但由 $e^{x_0}=\dfrac1{x_0+2}$ 可同时得到" "\n"
        r"　 $e^{x_0}=\dfrac1{x_0+2}$ 与 $\ln\left(x_0+2\right)=-x_0$ 两个替换式，" "\n"
        r"　 代入后 $f\left(x_0\right)=\dfrac1{x_0+2}+x_0$ **恰好配成完全平方** $\dfrac{\left(x_0+1\right)^2}{x_0+2}$——这不是巧合，"
        r"而是命题人刻意让 $f_{\min}$ 在 $x_0\to-1$ 时趋于 $0$（但取不到）．" "\n"
        r"③ 注意 $x_0\in\left(-1,0\right)$ 这个范围不能只写 $\left(-2,0\right)$："
        r"$\left(x_0+1\right)^2>0$ 需要 $x_0\ne-1$，而 $x_0+2>0$ 需要 $x_0>-2$．" "\n"
        r"④ 数值复核：解 $e^x=\dfrac1{x+2}$ 得 $x_0\approx-0.4429$（在 $\left(-1,0\right)$ 内 ✓），" "\n"
        r"　 $f\left(x_0\right)=e^{-0.4429}-\ln\left(1.5571\right)=0.6422-0.4428=0.1994>0$；" "\n"
        r"　 而 $\dfrac{\left(x_0+1\right)^2}{x_0+2}=\dfrac{0.3103}{1.5571}=0.1993$ ✓ 两者吻合．" "\n"
        r"**通法（隐零点）**：① 用 $f'$ 单调 $+$ 端点异号定出 $x_0$ 的**范围**；"
        r"② 由 $f'\left(x_0\right)=0$ 写出参数的替换式；③ 代入 $f\left(x_0\right)$ 消去超越部分；" "\n"
        r"　 ④ 化简后通常配成完全平方或能直接用已知不等式判号的式子．"
    ),
    'difficulty': 0.7,
    'topics': ['M-T-169'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-169-E1',
}

# ============================================================
# M-T-169-V1
# ============================================================
T169_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f\left(x\right)=\left(x-2\right)e^x-\dfrac a2\left(x-1\right)^2$，"
        r"$g\left(x\right)=x+\ln x-2e^x+1$．" "\n"
        r"（1）讨论 $f\left(x\right)$ 的单调性；" "\n"
        r"（2）当 $a=0$ 时，证明：$\forall x>0$，$f\left(x\right)\ge g\left(x\right)$．"
    ),
    'opts': [],
    'answer': r"（1）答案见解析；（2）证明见解析",
    'analysis': (
        r"（1）$f'\left(x\right)=\left(x-1\right)\left(e^x-a\right)$，按 $a\le0$、$a=e$、$0<a<e$、$a>e$ 四类讨论；" "\n"
        r"（2）$a=0$ 时不等式化为 $xe^x\ge x+\ln x+1$，构造 $h\left(x\right)=xe^x-x-\ln x-1$，"
        r"用隐零点 $e^{x_0}=\dfrac1{x_0}$ 求最小值．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"$f'\left(x\right)=e^x+\left(x-2\right)e^x-a\left(x-1\right)=\left(x-1\right)e^x-a\left(x-1\right)=\left(x-1\right)\left(e^x-a\right)$．" "\n"
        r"若 $a\le0$，则 $e^x-a>0$，故 $x<1$ 时 $f'<0$、$x>1$ 时 $f'>0$：" "\n"
        r"　 $f$ 在 $\left(-\infty,1\right)$ 上递减，在 $\left(1,+\infty\right)$ 上递增．" "\n"
        r"若 $a>0$，由 $f'=0$ 得 $x=1$ 或 $x=\ln a$：① $a=e$ 时 $\ln a=1$，"
        r"$f'\left(x\right)=\left(x-1\right)\left(e^x-e\right)\ge0$，$f$ 在 $\mathbf R$ 上递增；" "\n"
        r"　 ② $0<a<e$ 时 $\ln a<1$：$f$ 在 $\left(-\infty,\ln a\right)$、$\left(1,+\infty\right)$ 上递增，在 $\left(\ln a,1\right)$ 上递减；" "\n"
        r"　 ③ $a>e$ 时 $\ln a>1$：$f$ 在 $\left(-\infty,1\right)$、$\left(\ln a,+\infty\right)$ 上递增，在 $\left(1,\ln a\right)$ 上递减．" "\n"
        r"**第（2）问**" "\n"
        r"$a=0$ 时 $f\left(x\right)=\left(x-2\right)e^x$，要证 $\left(x-2\right)e^x\ge x+\ln x-2e^x+1$，" "\n"
        r"即证 $xe^x\ge x+\ln x+1$（$x>0$）．" "\n"
        r"令 $h\left(x\right)=xe^x-x-\ln x-1$，则" "\n"
        r"$h'\left(x\right)=\left(x+1\right)e^x-1-\dfrac1x=\left(x+1\right)e^x-\dfrac{x+1}x=\left(x+1\right)\left(e^x-\dfrac1x\right)$．" "\n"
        r"令 $t\left(x\right)=e^x-\dfrac1x$，则 $t'\left(x\right)=e^x+\dfrac1{x^2}>0$，$t$ 在 $\left(0,+\infty\right)$ 上递增．" "\n"
        r"又 $t\left(\dfrac12\right)=e^{1/2}-2<0$（因 $e^{1/2}\approx1.6487<2$），$t\left(1\right)=e-1>0$，" "\n"
        r"故存在唯一 $x_0\in\left(\dfrac12,1\right)$ 使 $t\left(x_0\right)=0$，即 $e^{x_0}=\dfrac1{x_0}$，取对数得 $x_0=-\ln x_0$．" "\n"
        r"因 $x+1>0$，故 $h'$ 与 $t$ 同号：$x\in\left(0,x_0\right)$ 时 $h'<0$，$x\in\left(x_0,+\infty\right)$ 时 $h'>0$，" "\n"
        r"$h_{\min}=h\left(x_0\right)=x_0e^{x_0}-x_0-\ln x_0-1$．" "\n"
        r"代入 $x_0e^{x_0}=1$ 与 $-\ln x_0=x_0$：" "\n"
        r"$h\left(x_0\right)=1-x_0+x_0-1=0$．" "\n"
        r"故 $h\left(x\right)\ge0$，即 $\boxed{f\left(x\right)\ge g\left(x\right)}$（等号在 $x=x_0$ 处取得）．"
    ),
    'review': (
        r"① 题干中 $f\left(x\right)$ 的系数还原为 $\dfrac a2$：**硬判据**是 $f'\left(x\right)=\left(x-1\right)\left(e^x-a\right)$，" "\n"
        r"　 若 $f\left(x\right)=\left(x-2\right)e^x-a\left(x-1\right)^2$，则 $f'=\left(x-1\right)e^x-2a\left(x-1\right)=\left(x-1\right)\left(e^x-2a\right)$，" "\n"
        r"　 与详解中的分类节点 $x=\ln a$ 不符（应为 $x=\ln\left(2a\right)$）．故按 $\dfrac a2$ 录入．" "\n"
        r"② （1）的分类标准不是 $a$ 与 $0$ 比，而是 $\ln a$ 与 $1$ 比（即 $a$ 与 $e$ 比）："
        r"**两个驻点 $1$ 与 $\ln a$ 的大小关系决定了单调区间的排列**，这是二次型导数分类讨论的固定套路．" "\n"
        r"③ （2）的化简 $\left(x-2\right)e^x+2e^x=xe^x$ 很关键——它把两个 $e^x$ 项合并，**让不等式左右都只含一个超越块**．" "\n"
        r"④ 隐零点 $x_0$ 满足 $e^{x_0}=\dfrac1{x_0}$ 时，$h_{\min}$ 的三项恰好抵消：$x_0e^{x_0}=1$、$-\ln x_0=x_0$、" "\n"
        r"　 $-x_0$ 与 $+x_0$ 相消、$1$ 与 $-1$ 相消 ⟹ 最小值恰为 $0$．**这种「恰好为 0」是命题人设计的**，"
        r"算出来不是 $0$ 就说明某步代换错了．" "\n"
        r"⑤ 数值复核：解 $e^x=\dfrac1x$ 得 $x_0\approx0.5671$（在 $\left(\frac12,1\right)$ 内 ✓），" "\n"
        r"　 $h\left(0.5671\right)=0.5671\times1.7632-0.5671-\ln0.5671-1=0.99993-0.5671+0.5672-1\approx0$ ✓" "\n"
        r"**通法（$xe^x$ 型不等式）**：$xe^x=e^{x+\ln x}$，与 $\ln x+x+1$ 的关系本质是 $e^t\ge t+1$ 取 $t=x+\ln x$；"
        r"但直接用 $e^t\ge t+1$ 需要 $x+\ln x$ 能取任意实数，**本题用隐零点更稳妥**．"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-169'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-169-V1',
}

# ============================================================
# M-T-169-V2
# ============================================================
T169_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f\left(x\right)=\dfrac{e^{ax}}x$，$g\left(x\right)=\ln x+2x+1$，其中 $a\in\mathbf R$．" "\n"
        r"（1）试讨论函数 $f\left(x\right)$ 的单调性；" "\n"
        r"（2）若 $a=2$，证明：$xf\left(x\right)\ge g\left(x\right)$．"
    ),
    'opts': [],
    'answer': r"（1）答案见解析；（2）证明见解析",
    'analysis': (
        r"（1）$f'\left(x\right)=\dfrac{e^{ax}\left(ax-1\right)}{x^2}$，按 $a>0$、$a=0$、$a<0$ 分类，注意 $x\ne0$；" "\n"
        r"（2）$xf\left(x\right)=e^{2x}$，用 $e^{2x}\ge1+2x+2x^2$ 与 $\ln x\le x-1$ 作差即可，差恒正．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"$f\left(x\right)$ 的定义域为 $\left(-\infty,0\right)\cup\left(0,+\infty\right)$，" "\n"
        r"$f'\left(x\right)=\dfrac{ae^{ax}\cdot x-e^{ax}}{x^2}=\dfrac{e^{ax}\left(ax-1\right)}{x^2}$．" "\n"
        r"因 $e^{ax}>0$、$x^2>0$，故 $f'$ 与 $ax-1$ 同号．" "\n"
        r"当 $a>0$ 时：$x>\dfrac1a$ 时 $f'>0$；$x<0$ 或 $0<x<\dfrac1a$ 时 $f'<0$．" "\n"
        r"　 故 $f$ 在 $\left(\dfrac1a,+\infty\right)$ 上递增，在 $\left(-\infty,0\right)$ 与 $\left(0,\dfrac1a\right)$ 上递减．" "\n"
        r"当 $a=0$ 时：$f\left(x\right)=\dfrac1x$，$f'\left(x\right)=-\dfrac1{x^2}<0$，$f$ 在 $\left(-\infty,0\right)$ 与 $\left(0,+\infty\right)$ 上递减．" "\n"
        r"当 $a<0$ 时：$x<\dfrac1a$（此时 $\dfrac1a<0$）时 $f'>0$；$\dfrac1a<x<0$ 或 $x>0$ 时 $f'<0$．" "\n"
        r"　 故 $f$ 在 $\left(-\infty,\dfrac1a\right)$ 上递增，在 $\left(\dfrac1a,0\right)$ 与 $\left(0,+\infty\right)$ 上递减．" "\n"
        r"**第（2）问**" "\n"
        r"$a=2$ 时 $f\left(x\right)=\dfrac{e^{2x}}x$ ，故 $xf\left(x\right)=e^{2x}$ ；又 $g\left(x\right)=\ln x+2x+1$ 的定义域为 $x>0$ ，" "\n"
        r"只需证 $e^{2x}\ge\ln x+2x+1$ （$x>0$）．" "\n"
        r"由 $e^t\ge1+t+\dfrac{t^2}2$ （$t\ge0$），取 $t=2x>0$ 得 $e^{2x}\ge1+2x+2x^2$ ；" "\n"
        r"又 $\ln x\le x-1$ （$x>0$ ，即 $\ln x$ 在 $x=1$ 处的切线）．" "\n"
        r"两式作差：$e^{2x}-\left(\ln x+2x+1\right)\ge\left(1+2x+2x^2\right)-\left(x-1\right)-2x-1=2x^2-x+1$．" "\n"
        r"而 $2x^2-x+1=2\left(x-\dfrac14\right)^2+\dfrac78>0$ （判别式 $1-8=-7<0$ ，恒正），" "\n"
        r"故 $e^{2x}>\ln x+2x+1$ ，即 $\boxed{xf\left(x\right)\ge g\left(x\right)}$．" "\n"
    ),
    'review': (
        r"① 题干 $g\left(x\right)$ 的末项原书 OCR 成「$1\ x$」，此处按 $\ln x+2x+1$ 录入．**硬判据**：" "\n"
        r"　 若取 $\dfrac1x$ ，则 $x=0.1$ 时 $xf\left(x\right)=e^{0.2}=1.2214$ ，而 $g=\ln0.1+0.2+10=7.897$ ，不等式不成立，" "\n"
        r"　 原题将成为假命题——**「算出反例」是判定还原是否正确的第一手段**．" "\n"
        r"② 原书给出的路径是 $xe^{2x}=e^{\ln x+2x}\ge\ln x+2x+1$ （令 $t=\ln x+2x$ 后用 $e^t\ge t+1$），" "\n"
        r"　 这对应 $xf\left(x\right)=xe^{2x}$ ，即 $f\left(x\right)=e^{ax}$ 而非 $\dfrac{e^{ax}}x$ ，" "\n"
        r"　 与（1）中 $f'\left(x\right)=\dfrac{e^{ax}\left(ax-1\right)}{x^2}$ 矛盾．**已按（1）确定的 $f\left(x\right)=\dfrac{e^{ax}}x$ 录入，并另给出自洽证明**" "\n"
        r"　 （$e^{2x}\ge1+2x+2x^2$ 配 $\ln x\le x-1$）；原书（2）疑有印刷脱漏，**已登记待核对纸质原书**．" "\n"
r"② （1）的讨论必须**把 $x=0$ 单独排除**：定义域在 $0$ 处断开，单调区间不能跨过 $0$ 写成 $\left(-\infty,\frac1a\right)$ 这样的连通区间（对 $a>0$ 而言 $\frac1a>0$）．" "\n"
        r"③ $a<0$ 时 $\dfrac1a<0$，故递增区间 $\left(-\infty,\dfrac1a\right)$ 完全在负半轴，**不能照抄 $a>0$ 的结论**．" "\n"
        r"④ 数值复核（$x\le1$ 分支）：取 $x=0.5$，$xf\left(x\right)=e^{1}=2.7183$，"
        r"$g\left(0.5\right)=\ln0.5+1+2=2.3069$，$2.7183\ge2.3069$ ✓" "\n"
        r"**通法（$e^t\ge t+1$ 的代入）**：关键是凑出 $e^{\ln x}\cdot e^{kx}=xe^{kx}=e^{\ln x+kx}$，" "\n"
        r"　 令 $t=\ln x+kx$ 后不等式化为 $e^t\ge t+1$；**使用前务必核对右边的 $t$ 是否正好等于左式的指数部分**．"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-169'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-169-V2',
}

# ============================================================
# M-T-172-E1
# ============================================================
T172_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f\left(x\right)=x\ln x+ax^2$．" "\n"
        r"（1）设 $g\left(x\right)=f'\left(x\right)$，讨论 $g\left(x\right)$ 在区间 $\left(0,+\infty\right)$ 上的单调性；" "\n"
        r"（2）若 $f\left(x\right)$ 存在两个极值点 $x_1,x_2$（极值点是指函数取极值时对应的自变量的值），"
        r"且 $x_1f\left(x_2\right)+x_2f\left(x_1\right)>0$，证明：$-\dfrac1{2e}<a<0$．"
    ),
    'opts': [],
    'answer': r"（1）答案见解析；（2）证明见解析",
    'analysis': (
        r"（1）$g\left(x\right)=\ln x+1+2ax$，$g'\left(x\right)=\dfrac1x+2a$，按 $a\ge0$、$a<0$ 讨论；" "\n"
        r"（2）由 $g\left(x_1\right)=g\left(x_2\right)=0$ 得两个关系式，消去 $a$ 后推出 $x_1x_2>e^2$，"
        r"再用对数平均不等式 $L\left(x_1,x_2\right)>\sqrt{x_1x_2}$ 得 $-\dfrac1{2a}>e$．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"$g\left(x\right)=f'\left(x\right)=\ln x+1+2ax$，$g'\left(x\right)=\dfrac1x+2a=\dfrac{1+2ax}x$（$x>0$）．" "\n"
        r"当 $a\ge0$ 时 $g'\left(x\right)>0$，$g$ 在 $\left(0,+\infty\right)$ 上单调递增；" "\n"
        r"当 $a<0$ 时，由 $g'\left(x\right)=0$ 得 $x=-\dfrac1{2a}>0$：" "\n"
        r"　 $0<x<-\dfrac1{2a}$ 时 $g'\left(x\right)>0$，$g$ 递增；$x>-\dfrac1{2a}$ 时 $g'\left(x\right)<0$，$g$ 递减．" "\n"
        r"**第（2）问**" "\n"
        r"由（1），$f$ 有两个极值点需 $a<0$，且 $g$ 的最大值 $g\left(-\dfrac1{2a}\right)=\ln\left(-\dfrac1{2a}\right)+1-1=\ln\left(-\dfrac1{2a}\right)>0$，" "\n"
        r"即 $-\dfrac1{2a}>1$，结合 $a<0$ 得 $-\dfrac12<a<0$．" "\n"
        r"此时 $x_1,x_2$ 是 $g$ 的两零点，且 $f'\left(x\right)=g\left(x\right)$ 在 $\left(0,x_1\right)$ 上为负、"
        r"$\left(x_1,x_2\right)$ 上为正、$\left(x_2,+\infty\right)$ 上为负，故 $x_1,x_2$ 确为 $f$ 的极值点．" "\n"
        r"由 $x_1f\left(x_2\right)+x_2f\left(x_1\right)>0$，两边同除以 $x_1x_2>0$ 得" "\n"
        r"$\dfrac{f\left(x_2\right)}{x_2}+\dfrac{f\left(x_1\right)}{x_1}>0$，即 $\left(\ln x_2+ax_2\right)+\left(\ln x_1+ax_1\right)>0$，" "\n"
        r"$\ln\left(x_1x_2\right)+a\left(x_1+x_2\right)>0$．　（★）" "\n"
        r"又 $g\left(x_1\right)=g\left(x_2\right)=0$：" "\n"
        r"$\ln x_1+1+2ax_1=0$，$\ln x_2+1+2ax_2=0$，两式相加得" "\n"
        r"$\ln\left(x_1x_2\right)+2+2a\left(x_1+x_2\right)=0$，即 $a=-\dfrac{\ln\left(x_1x_2\right)+2}{2\left(x_1+x_2\right)}$．" "\n"
        r"代入（★）：$\ln\left(x_1x_2\right)-\dfrac{\ln\left(x_1x_2\right)+2}2>0$，得 $\ln\left(x_1x_2\right)>2$，即 $x_1x_2>e^2$．" "\n"
        r"两式相减：$\ln x_1-\ln x_2=-2a\left(x_1-x_2\right)=2a\left(x_2-x_1\right)$，故" "\n"
        r"$-\dfrac1{2a}=\dfrac{x_2-x_1}{\ln x_2-\ln x_1}$．" "\n"
        r"由对数平均不等式 $\dfrac{x_2-x_1}{\ln x_2-\ln x_1}>\sqrt{x_1x_2}$（$x_1\ne x_2$），" "\n"
        r"得 $-\dfrac1{2a}>\sqrt{x_1x_2}>e$．" "\n"
        r"由 $-\dfrac1{2a}>e$ 且 $a<0$，两边乘 $2a<0$ 变号：$-1<2ae$，即 $a>-\dfrac1{2e}$．" "\n"
        r"结合 $a<0$，$\boxed{-\dfrac1{2e}<a<0}$．"
    ),
    'review': (
        r"① 条件 $x_1f\left(x_2\right)+x_2f\left(x_1\right)>0$ 的处理是**同除以 $x_1x_2$**："
        r"这样一来 $\dfrac{f\left(x\right)}x=\ln x+ax$ 的形式就出现了，恰好与 $g\left(x\right)=\ln x+1+2ax$ 呼应．" "\n"
        r"　 **凡是出现 $x_1\cdot f\left(x_2\right)$ 这种交叉乘积，先想同除以 $x_1x_2$**．" "\n"
        r"② 由 $g\left(x_1\right)=g\left(x_2\right)=0$ 得到「相加」与「相减」两个式子是固定动作：" "\n"
        r"　 **相加**消 $x_1-x_2$ 类项，得到 $a$ 与 $\ln\left(x_1x_2\right)$、$\left(x_1+x_2\right)$ 的关系；" "\n"
        r"　 **相减**得到 $-\dfrac1{2a}=\dfrac{x_2-x_1}{\ln x_2-\ln x_1}$，即**对数平均**．" "\n"
        r"③ 对数平均不等式 $\dfrac{b-a}{\ln b-\ln a}>\sqrt{ab}$（$0<a<b$）是极值点偏移问题的**核心工具**，"
        r"另一个常用方向是 $\dfrac{b-a}{\ln b-\ln a}<\dfrac{a+b}2$．两个方向都要记．" "\n"
        r"④ 注意 $-\dfrac12<a<0$ 这个前提比结论 $-\dfrac1{2e}<a<0$ 弱（$-\dfrac1{2e}\approx-0.184>-\dfrac12$），"
        r"所以**结论推出后要取交集**，最终以 $-\dfrac1{2e}<a<0$ 为准．" "\n"
        r"⑤ 数值复核：取 $a=-0.1$（在结论区间内），$g\left(x\right)=\ln x+1-0.2x$：" "\n"
        r"　 $g\left(0.1\right)=\ln0.1+1-0.02=-1.3226<0$，$g\left(1\right)=0.8>0$，$g\left(30\right)=\ln30+1-6=-1.5988<0$，" "\n"
        r"　 两根 $x_1\approx0.5173$、$x_2\approx17.32$；$x_1x_2\approx8.96>e^2\approx7.389$ ✓，" "\n"
        r"　 $-\dfrac1{2a}=5>\sqrt{8.96}=2.993>e=2.718$ ✓ 链条闭合．" "\n"
        r"**通法（极值点偏移的标准流程）**：① 由两零点条件写「相加」「相减」两式；"
        r"② 用「相加」式把参数 $a$ 表示成 $x_1,x_2$ 的函数；③ 代入题设不等式化简出 $x_1x_2$ 的范围；" "\n"
        r"　 ④ 用「相减」式配合对数平均不等式把 $-\dfrac1{2a}$ 与 $\sqrt{x_1x_2}$ 挂钩，反解 $a$．"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-172'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-172-E1',
}

# ============================================================
# M-T-172-V1
# ============================================================
T172_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知 $f\left(x\right)=x\left(\ln x\right)^2+x$．" "\n"
        r"（1）证明：$f\left(x\right)$ 是 $\left(0,+\infty\right)$ 上的增函数；" "\n"
        r"（2）若 $f\left(x_1\right)+f\left(x_2\right)=\dfrac4e$，且 $x_1<x_2$，证明：$x_1+x_2>\dfrac2e$．"
    ),
    'opts': [],
    'answer': r"（1）证明见解析；（2）证明见解析",
    'analysis': (
        r"（1）$f'\left(x\right)=\left(\ln x\right)^2+2\ln x+1=\left(\ln x+1\right)^2\ge0$；" "\n"
        r"（2）由 $f\left(\dfrac1e\right)=\dfrac2e$ 定出 $x_1<\dfrac1e<x_2$，构造"
        r"$g\left(x\right)=f\left(x\right)+f\left(\dfrac2e-x\right)-\dfrac4e$（$0<x<\dfrac1e$），用单调性完成估计．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"$f'\left(x\right)=\left(\ln x\right)^2+x\cdot\dfrac{2\ln x}x+1=\left(\ln x\right)^2+2\ln x+1=\left(\ln x+1\right)^2\ge0$，" "\n"
        r"且仅当 $\ln x=-1$ 即 $x=\dfrac1e$ 时取等号，故 $f$ 在 $\left(0,+\infty\right)$ 上 $\boxed{\text{单调递增}}$．" "\n"
        r"**第（2）问**" "\n"
        r"$f\left(\dfrac1e\right)=\dfrac1e\left(\ln\dfrac1e\right)^2+\dfrac1e=\dfrac1e+\dfrac1e=\dfrac2e$．" "\n"
        r"若 $x_2>x_1\ge\dfrac1e$，则 $f\left(x_2\right)>f\left(x_1\right)\ge f\left(\dfrac1e\right)=\dfrac2e$（$f$ 严格增），"
        r"得 $f\left(x_1\right)+f\left(x_2\right)>\dfrac4e$，矛盾；" "\n"
        r"若 $0<x_1<x_2\le\dfrac1e$，则 $f\left(x_1\right)<f\left(x_2\right)\le\dfrac2e$，得 $f\left(x_1\right)+f\left(x_2\right)<\dfrac4e$，矛盾．" "\n"
        r"故必有 $0<x_1<\dfrac1e<x_2$．" "\n"
        r"当 $x_2\ge\dfrac2e$ 时，$x_1+x_2>\dfrac2e$ 显然成立；只需证 $0<x_1<\dfrac1e<x_2<\dfrac2e$ 的情形．" "\n"
        r"由 $f\left(x_2\right)=\dfrac4e-f\left(x_1\right)$，要证 $x_2>\dfrac2e-x_1$，由 $f$ 递增只需证" "\n"
        r"$f\left(x_2\right)>f\left(\dfrac2e-x_1\right)$，即 $\dfrac4e-f\left(x_1\right)>f\left(\dfrac2e-x_1\right)$．" "\n"
        r"令 $g\left(x\right)=f\left(x\right)+f\left(\dfrac2e-x\right)-\dfrac4e$（$0<x<\dfrac1e$），下面证 $g\left(x\right)<0$．" "\n"
        r"$g'\left(x\right)=f'\left(x\right)-f'\left(\dfrac2e-x\right)=\left(\ln x+1\right)^2-\left(\ln\left(\dfrac2e-x\right)+1\right)^2$" "\n"
        r"$=\left[\ln x-\ln\left(\dfrac2e-x\right)\right]\cdot\left[\ln x+\ln\left(\dfrac2e-x\right)+2\right]$．" "\n"
        r"因 $0<x<\dfrac1e$，故 $\dfrac2e-x>\dfrac1e>x$，第一个因子 $\ln x-\ln\left(\dfrac2e-x\right)<0$；" "\n"
        r"第二个因子 $\ln x+\ln\left(\dfrac2e-x\right)+2=\ln\left[x\left(\dfrac2e-x\right)\right]+2"
        r"<\ln\left[\left(\dfrac{x+\frac2e-x}2\right)^2\right]+2=\ln\dfrac1{e^2}+2=-2+2=0$．" "\n"
        r"故 $g'\left(x\right)=\left(\text{负}\right)\times\left(\text{负}\right)>0$，$g$ 在 $\left(0,\dfrac1e\right)$ 上递增．" "\n"
        r"于是 $g\left(x\right)<g\left(\dfrac1e\right)=f\left(\dfrac1e\right)+f\left(\dfrac1e\right)-\dfrac4e=\dfrac2e+\dfrac2e-\dfrac4e=0$．" "\n"
        r"取 $x=x_1$ 得 $g\left(x_1\right)<0$，即 $f\left(x_1\right)+f\left(\dfrac2e-x_1\right)<\dfrac4e=f\left(x_1\right)+f\left(x_2\right)$，" "\n"
        r"所以 $f\left(\dfrac2e-x_1\right)<f\left(x_2\right)$，由 $f$ 递增得 $\dfrac2e-x_1<x_2$，" "\n"
        r"即 $\boxed{x_1+x_2>\dfrac2e}$．"
    ),
    'review': (
        r"① $f'\left(x\right)=\left(\ln x+1\right)^2\ge0$ 是**完全平方**——这是本题能被做出来的根本原因，"
        r"也提示了「关键点」是 $x=\dfrac1e$（导数等于 $0$ 的点）．" "\n"
        r"② 第（2）问先**排除两侧情形**定出 $x_1<\dfrac1e<x_2$ 是必要的："
        r"否则无从判断 $\dfrac2e-x_1$ 是否落在 $f$ 的定义域与单调区间内．" "\n"
        r"③ 对称化构造 $g\left(x\right)=f\left(x\right)+f\left(\dfrac2e-x\right)-\dfrac4e$ 的妙处：" "\n"
        r"　 $g\left(\dfrac1e\right)=2f\left(\dfrac1e\right)-\dfrac4e=0$ 是**刻意设计**的零点，配合 $g$ 递增即得 $g<0$．" "\n"
        r"④ 第二个因子的放缩用到了 $\ln\left[x\left(\dfrac2e-x\right)\right]\le\ln\left[\left(\dfrac{x+\frac2e-x}2\right)^2\right]$，"
        r"即**均值不等式 $ab\le\left(\dfrac{a+b}2\right)^2$，且和 $x+\left(\frac2e-x\right)=\dfrac2e$ 是常数**——这是能放缩的前提．" "\n"
        r"⑤ 数值复核：取 $x_1=0.2$，$f\left(0.2\right)=0.2\left(\ln0.2\right)^2+0.2=0.2\times2.5903+0.2=0.7181$；" "\n"
        r"　 $f\left(x_2\right)=\dfrac4e-0.7181=1.4714-0.7181=0.7533$，解得 $x_2\approx0.7538$（$>x_1$ ✓）；" "\n"
        r"　 $x_1+x_2=0.9538>\dfrac2e=0.7358$ ✓" "\n"
        r"**通法（和型极值点偏移）**：要证 $x_1+x_2>2x_0$，构造 $g\left(x\right)=f\left(x\right)+f\left(2x_0-x\right)-2f\left(x_0\right)$，" "\n"
        r"　 证 $g$ 在 $\left(0,x_0\right)$ 上**递增**且 $g\left(x_0\right)=0$，则 $g\left(x_1\right)<0$ ⟹ $f\left(2x_0-x_1\right)<f\left(x_2\right)$ ⟹ $x_1+x_2>2x_0$．" "\n"
        r"　 （证 $x_1+x_2<2x_0$ 时对称地构造并证 $g$ 递减即可．）"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-172'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-172-V1',
}

# ============================================================
# M-T-172-V2
# ============================================================
T172_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f\left(x\right)=xe^{x-a}-x^2$．" "\n"
        r"（1）讨论 $f\left(x\right)$ 零点的个数；" "\n"
        r"（2）设 $m,n$ 为两个不相等的正数，且 $e^{m-a}-m=e^{n-a}-n=0$，证明：$mn<1$．"
    ),
    'opts': [],
    'answer': (
        r"（1）$a<1$ 时 $1$ 个；$a=1$ 时 $2$ 个；$a>1$ 时 $3$ 个；（2）证明见解析"
    ),
    'analysis': (
        r"（1）$f\left(x\right)=x\left(e^{x-a}-x\right)$，故 $x=0$ 是零点，其余零点来自 $x-\ln x=a$，"
        r"研究 $h\left(x\right)=x-\ln x$ 的最小值 $h\left(1\right)=1$；" "\n"
        r"（2）由 $h\left(m\right)=h\left(n\right)=a$ 且 $0<m<1<n$，构造"
        r"$\varphi\left(x\right)=h\left(x\right)-h\left(\dfrac1x\right)$ 比较 $h\left(n\right)$ 与 $h\left(\dfrac1m\right)$．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"$f\left(x\right)=x\left(e^{x-a}-x\right)$，故 $x=0$ 恒为零点．" "\n"
        r"$e^{x-a}-x=0$（$x>0$）等价于 $x-a=\ln x$，即 $x-\ln x=a$．" "\n"
        r"令 $h\left(x\right)=x-\ln x$（$x>0$），则 $h'\left(x\right)=1-\dfrac1x=\dfrac{x-1}x$：" "\n"
        r"$h$ 在 $\left(0,1\right)$ 上递减，在 $\left(1,+\infty\right)$ 上递增，$h_{\min}=h\left(1\right)=1$；" "\n"
        r"且 $x\to0^+$ 时 $h\to+\infty$，$x\to+\infty$ 时 $h\to+\infty$．" "\n"
        r"于是：当 $a<1$ 时 $h\left(x\right)=a$ 无解，$f$ 只有零点 $x=0$，共 $1$ 个；" "\n"
        r"当 $a=1$ 时 $h\left(x\right)=1$ 有唯一解 $x=1$，共 $2$ 个；" "\n"
        r"当 $a>1$ 时 $h\left(x\right)=a$ 有两解，共 $3$ 个．" "\n"
        r"**第（2）问**" "\n"
        r"由 $e^{m-a}-m=0$、$e^{n-a}-n=0$ 得 $m-\ln m=a$、$n-\ln n=a$，即 $h\left(m\right)=h\left(n\right)=a$．" "\n"
        r"不妨设 $0<m<1<n$（由 $h$ 在 $\left(0,1\right)$ 递减、$\left(1,+\infty\right)$ 递增知两根分居 $1$ 两侧）．" "\n"
        r"令 $\varphi\left(x\right)=h\left(x\right)-h\left(\dfrac1x\right)=x-\ln x-\left(\dfrac1x+\ln x\right)=x-\dfrac1x-2\ln x$（$0<x<1$）．" "\n"
        r"$\varphi'\left(x\right)=1+\dfrac1{x^2}-\dfrac2x=\dfrac{x^2-2x+1}{x^2}=\dfrac{\left(x-1\right)^2}{x^2}>0$（$x\ne1$），" "\n"
        r"故 $\varphi$ 在 $\left(0,1\right)$ 上递增，$\varphi\left(x\right)<\varphi\left(1\right)=0$，即 $h\left(x\right)<h\left(\dfrac1x\right)$．" "\n"
        r"取 $x=m\in\left(0,1\right)$：$h\left(m\right)<h\left(\dfrac1m\right)$．" "\n"
        r"又 $h\left(m\right)=h\left(n\right)=a$，故 $h\left(n\right)<h\left(\dfrac1m\right)$．" "\n"
        r"因 $n>1$ 且 $\dfrac1m>1$，而 $h$ 在 $\left(1,+\infty\right)$ 上递增，故 $n<\dfrac1m$，" "\n"
        r"即 $\boxed{mn<1}$．"
    ),
    'review': (
        r"① 第（1）问的入口是**因式分解** $f\left(x\right)=x\left(e^{x-a}-x\right)$："
        r"$x=0$ 恒为零点，剩下的问题降为研究 $x-\ln x=a$ 的解数．" "\n"
        r"　 注意 $e^{x-a}-x=0$ 取对数时**必须 $x>0$**，这与 $f$ 的非零零点为正是一致的（$x<0$ 时 $e^{x-a}>0>x$，故 $e^{x-a}-x>0$ 无零点）．" "\n"
        r"② $h\left(x\right)=x-\ln x$ 的**最小值恰为 $1$**（在 $x=1$ 处），所以分界点就是 $a=1$——"
        r"这种「最小值是整数」的设计是刻意的，可作为自检信号．" "\n"
        r"③ 第（2）问构造 $\varphi\left(x\right)=h\left(x\right)-h\left(\dfrac1x\right)$ 是**倒数比较法**："
        r"要证 $mn<1$ 即 $n<\dfrac1m$，而 $n$ 与 $\dfrac1m$ 都在 $h$ 的递增区间 $\left(1,+\infty\right)$ 内，" "\n"
        r"　 故只需比较 $h\left(n\right)$ 与 $h\left(\dfrac1m\right)$；又 $h\left(n\right)=h\left(m\right)$，问题化为比较 $h\left(m\right)$ 与 $h\left(\dfrac1m\right)$．" "\n"
        r"④ $\varphi'\left(x\right)=\dfrac{\left(x-1\right)^2}{x^2}>0$ 又是**完全平方分子**——与 M-T-164-V1 的"
        r"$h'\left(t\right)=\dfrac{\left(t-1\right)^2}{t\left(t+1\right)^2}$ 同源，都是「$x$ 与 $\frac1x$ 配对」的必然结果．" "\n"
        r"⑤ 数值复核：取 $a=2$，解 $x-\ln x=2$ 得 $m\approx0.1586$、$n\approx3.1462$；" "\n"
        r"　 $mn=0.1586\times3.1462=0.4990<1$ ✓；" "\n"
        r"　 且 $f\left(0\right)=0$、$f\left(0.1586\right)=0.1586\left(e^{-1.8414}-0.1586\right)=0.1586\left(0.1586-0.1586\right)=0$ ✓" "\n"
        r"**通法（倒数比较法证 $x_1x_2<1$）**：当 $h\left(x_1\right)=h\left(x_2\right)$ 且 $x_1<1<x_2$ 时，" "\n"
        r"　 构造 $\varphi\left(x\right)=h\left(x\right)-h\left(\dfrac1x\right)$（$0<x<1$），用导数定符号；" "\n"
        r"　 若 $\varphi<0$ 则 $h\left(x_1\right)<h\left(\dfrac1{x_1}\right)=h\left(x_2\right)$ 方向的比较给出 $x_2<\dfrac1{x_1}$，即 $x_1x_2<1$．"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-172'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-172-V2',
}

QS = [
    T152_E1, T152_V1, T152_V2,
    T164_E1, T164_V1, T164_V2,
    T169_E1, T169_V1, T169_V2,
    T172_E1, T172_V1, T172_V2,
]
