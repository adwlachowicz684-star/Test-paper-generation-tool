# -*- coding: utf-8 -*-
r"""第 138 批（补录批·九）：七道「回原件反推」题。

    python3 tools/run_batch.py 138

## 本批的方法论进展

### 一、新增两类可救信号（此前会被误判为 D 级）

#### (a) 分式排版被 OCR 拆开（M-T-116-E1）
原件 p082 的题干是竖排分式 $\frac{f(x)}{\sin x}<\frac{f'(x)}{\cos x}$，
提取后变成上下两行 `f(x)` / `sinx` 与 `f(x)` / `cosx`，**分子的导数撇号丢失**，
于是看起来像「$f(x)\sin x<f(x)\cos x$」，与详解的 $g'=(\cdots)>0$ 矛盾。

  ⭐ 新判据：**详解的导数分子就是题干的还原蓝本。**
  详解写 $g'(x)=\dfrac{f'(x)\sin x-f(x)\cos x}{\sin^2x}>0$，
  则题设必为 $f'(x)\sin x-f(x)\cos x>0$，即 $\dfrac{f(x)}{\sin x}<\dfrac{f'(x)}{\cos x}$。
  看到「详解分子含 $u'v-uv'$」就应立刻反推题干是**分式不等式**而非乘积不等式。

#### (b) 「定义域开区间」是选项真伪的开关（M-T-116-E1）
我第 135 批判「A、C 同时成立」是**错的**。题干定义在 $(0,\frac\pi2)$，
而 A 选项含 $f(\frac\pi2)$ —— $\frac\pi2$ 不在定义域内，A 无意义。

  ⭐ 新判据：**含参判断类选择题，先扫一遍各选项的自变量是否落在定义域内。**
  开区间端点处的函数值是最经典的排除项，此前被我漏掉。

### 二、回填法第四种形态：三视图 ⟹ 文字几何体（M-T-294-V3）
此前三视图一律判 D 级。但详解写「从边长为 $3$ 的正方体中截取出来的，
三棱锥的外接球就是截取它的正方体的外接球」——**几何体已被完整描述**，可直接回填。

### 三、图形选择题降级的两种落点（M-T-279-V1 / M-T-284-V1 / M-T-284-E1）
选项为图形时，看详解是否给出**可文字化的结论**：
  - 给出轨迹方程（$x=2y$）      ⟹ 降级为「求轨迹」
  - 给出具体数值（$DG=4,GB=8$） ⟹ 降级为「求该量」
  - 给出形状与边长关系          ⟹ 降级为「求截面形状及边长」

### 四、B 级「详解为空」的处理（M-T-210-V2）
题干与选项完整、详解为空 ⟹ 独立推导补全。本题用 $\overrightarrow{AP}\cdot\overrightarrow{BC}=0$
一步定出垂心，并用 $4$ 组随机三角形数值验证 $AP\cdot BC\sim10^{-16}$。

## ⚠ 本批更正我此前的一处误判
  M-T-116-E1：第 135 批登记「A、C 同时成立，原书标答存疑」，本批回原件后确认
  原书答案 C 正确 —— A 因 $f(\frac\pi2)$ 越出定义域而不成立。已从跳过清单移除并录入。
"""

QS = []

# ── 1. M-T-116-E1 sinx 与 f(x) 构造（题干按详解反推还原）────────────────
QS.append({
    'type': '选择',
    'stem_text': (
        r"已知定义在 $\left(0,\dfrac{\pi}{2}\right)$ 上的函数 $f\left(x\right)$，$f'\left(x\right)$ 为其导函数，"
        r"且 $\dfrac{f\left(x\right)}{\sin x}<\dfrac{f'\left(x\right)}{\cos x}$ 恒成立，则（　　）"
    ),
    'opts': [
        ('A', r"$f\left(\dfrac{\pi}{2}\right)>2f\left(\dfrac{\pi}{6}\right)$"),
        ('B', r"$\sqrt{3}f\left(\dfrac{\pi}{4}\right)>2f\left(\dfrac{\pi}{3}\right)$"),
        ('C', r"$\sqrt{3}f\left(\dfrac{\pi}{6}\right)<f\left(\dfrac{\pi}{3}\right)$"),
        ('D', r"$f\left(1\right)<2f\left(\dfrac{\pi}{6}\right)\sin1$"),
    ],
    'answer': r"C",
    'analysis': (
        r"题设两边同乘 $\sin x\cos x>0$ 得 $f\left(x\right)\cos x<f'\left(x\right)\sin x$，"
        r"即 $\left(\dfrac{f\left(x\right)}{\sin x}\right)'>0$，构造 $g\left(x\right)=\dfrac{f\left(x\right)}{\sin x}$，"
        r"由单调性逐一检验四个选项。"
    ),
    'solution': (
        r"在 $\left(0,\dfrac{\pi}{2}\right)$ 上 $\sin x>0,\ \cos x>0$，题设两边同乘 $\sin x\cos x$ 得" "\n"
        r"$f\left(x\right)\cos x<f'\left(x\right)\sin x$，即 $f'\left(x\right)\sin x-f\left(x\right)\cos x>0$。" "\n"
        r"令 $g\left(x\right)=\dfrac{f\left(x\right)}{\sin x}$，则" "\n"
        r"$g'\left(x\right)=\dfrac{f'\left(x\right)\sin x-f\left(x\right)\cos x}{\sin^{2}x}>0$，" "\n"
        r"故 $g\left(x\right)$ 在 $\left(0,\dfrac{\pi}{2}\right)$ 上**单调递增**。" "\n"
        r"**检验 C：** 由 $\dfrac{\pi}{6}<\dfrac{\pi}{3}$ 得 $g\left(\dfrac{\pi}{6}\right)<g\left(\dfrac{\pi}{3}\right)$，即" "\n"
        r"$\dfrac{f\left(\frac{\pi}{6}\right)}{\sin\frac{\pi}{6}}<\dfrac{f\left(\frac{\pi}{3}\right)}{\sin\frac{\pi}{3}}$"
        r"$\Rightarrow 2f\left(\dfrac{\pi}{6}\right)<\dfrac{2}{\sqrt3}f\left(\dfrac{\pi}{3}\right)$"
        r"$\Rightarrow \sqrt3 f\left(\dfrac{\pi}{6}\right)<f\left(\dfrac{\pi}{3}\right)$，C 正确。" "\n"
        r"**检验 B：** 由 $\dfrac{\pi}{4}<\dfrac{\pi}{3}$ 得" "\n"
        r"$\dfrac{f\left(\frac{\pi}{4}\right)}{\sin\frac{\pi}{4}}<\dfrac{f\left(\frac{\pi}{3}\right)}{\sin\frac{\pi}{3}}$"
        r"$\Rightarrow \sqrt2 f\left(\dfrac{\pi}{4}\right)<\dfrac{2}{\sqrt3}f\left(\dfrac{\pi}{3}\right)$，"
        r"与 B 的不等号方向相反，B 错。" "\n"
        r"**检验 D：** 由 $\dfrac{\pi}{6}<1$（因 $\dfrac{\pi}{2}\approx1.571>1$）得" "\n"
        r"$\dfrac{f\left(\frac{\pi}{6}\right)}{\sin\frac{\pi}{6}}<\dfrac{f\left(1\right)}{\sin1}$"
        r"$\Rightarrow 2\sin1\,f\left(\dfrac{\pi}{6}\right)<f\left(1\right)$，与 D 方向相反，D 错。" "\n"
        r"**检验 A：** 定义域是**开区间** $\left(0,\dfrac{\pi}{2}\right)$，$\dfrac{\pi}{2}$ 不在定义域内，"
        r"$f\left(\dfrac{\pi}{2}\right)$ 无定义，A 不成立。" "\n"
        r"故选 $\mathbf{C}$。"
    ),
    'review': (
        r"① ⭐⭐ **题干还原（原式是分式，不是乘积）。** 提取文本作「$f\left(x\right)\sin x<f\left(x\right)\cos x$」，"
        r"与详解 $g'>0$ 矛盾；原件 p082 明确定为 $\dfrac{f\left(x\right)}{\sin x}<\dfrac{f'\left(x\right)}{\cos x}$。" "\n"
        r"　 判据：详解分子为 $f'\left(x\right)\sin x-f\left(x\right)\cos x$，正是 $\left(\dfrac{f}{\sin x}\right)'$ 的分子，"
        r"说明题设必为分式不等式。" "\n"
        r"② ⭐⭐ **更正我第 135 批的误判**：当时判「A、C 同时成立」，漏看了定义域是开区间。"
        r"$\dfrac{\pi}{2}\notin\left(0,\dfrac{\pi}{2}\right)$，故 $f\left(\dfrac{\pi}{2}\right)$ 无定义、A 不成立，原书答案 C 正确。" "\n"
        r"③ ⭐ **通法**：$\sin x\cdot f'\left(x\right)-\cos x\cdot f\left(x\right)$ 型构造 $g=\dfrac{f}{\sin x}$；"
        r"$\sin x\cdot f'\left(x\right)+\cos x\cdot f\left(x\right)$ 型构造 $g=f\cdot\sin x$。两者符号只差一项，务必区分。" "\n"
        r"④ ⭐ **扫定义域是廉价的自检**：含参判断型选择题，先看各选项自变量是否落在定义域内，"
        r"开区间端点是最高频的排除项。" "\n"
        r"⑤ 数值复核：取 $f\left(x\right)=x\sin x$（此时 $\dfrac{f}{\sin x}=x$ 递增，满足题设），"
        r"$\sqrt3 f\left(\dfrac{\pi}{6}\right)=0.4534<0.9069=f\left(\dfrac{\pi}{3}\right)$ ✓"
    ),
    'topics': ['M-T-116'],
    'src': 'M-T-116-E1',
    'difficulty': 0.62,
})

# ── 2. M-T-143-V1 嵌套函数求参（题干按详解反推还原）────────────────────
QS.append({
    'type': '选择',
    'stem_text': (
        r"对任意的正数 $x$，都存在两个不同的正数 $y$，使 $\mathrm e^{x}\left(y-x\right)-a\mathrm e^{2y-x}=0$ 成立，"
        r"则实数 $a$ 的取值范围为（　　）"
    ),
    'opts': [
        ('A', r"$\left(0,\dfrac{1}{2\mathrm e}\right)$"),
        ('B', r"$\left(-\infty,\dfrac{1}{2\mathrm e}\right)$"),
        ('C', r"$\left(\dfrac{1}{2\mathrm e},+\infty\right)$"),
        ('D', r"$\left(\dfrac{1}{2\mathrm e},1\right)$"),
    ],
    'answer': r"A",
    'analysis': (
        r"由方程解出 $a=\left(y-x\right)\mathrm e^{2\left(x-y\right)}$，令 $t=2\left(x-y\right)$ 化为 $a=-\dfrac12 t\mathrm e^{t}$，"
        r"再研究 $g\left(t\right)=-\dfrac12 t\mathrm e^{t}$ 的图象与水平线 $y=a$ 的交点个数。"
    ),
    'solution': (
        r"由 $\mathrm e^{x}\left(y-x\right)=a\mathrm e^{2y-x}$ 得" "\n"
        r"$a=\dfrac{\mathrm e^{x}\left(y-x\right)}{\mathrm e^{2y-x}}=\left(y-x\right)\mathrm e^{2x-2y}"
        r"=\left(y-x\right)\mathrm e^{2\left(x-y\right)}=-\left(x-y\right)\mathrm e^{2\left(x-y\right)}$。" "\n"
        r"令 $t=2\left(x-y\right)$，则 $a=-\dfrac{t}{2}\mathrm e^{t}=-\dfrac12 t\mathrm e^{t}$。" "\n"
        r"设 $g\left(t\right)=-\dfrac12 t\mathrm e^{t}$，则 $g'\left(t\right)=-\dfrac12\left(t+1\right)\mathrm e^{t}$：" "\n"
        r"$t<-1$ 时 $g'\left(t\right)>0$，$g$ 递增；$t>-1$ 时 $g'\left(t\right)<0$，$g$ 递减；" "\n"
        r"极大值 $g\left(-1\right)=\dfrac{1}{2\mathrm e}$，且 $t\to-\infty$ 时 $g\left(t\right)\to0^{+}$，$t\to+\infty$ 时 $g\left(t\right)\to-\infty$。" "\n"
        r"**当 $a\in\left(0,\dfrac{1}{2\mathrm e}\right)$ 时**，方程 $a=g\left(t\right)$ 恰有两个实根 $t_{1}<-1<t_{2}<0$，"
        r"两根**均为负**，故对任意 $x>0$ 都有 $y=x-\dfrac{t}{2}>x>0$，两个 $y$ 都是正数且互不相同，满足题意。" "\n"
        r"**当 $a=\dfrac{1}{2\mathrm e}$ 时**只有 $t=-1$ 一根；**当 $a\le0$ 时**至多一根（$a=0$ 仅 $t=0$，"
        r"$a<0$ 仅一根 $t>0$）；**当 $a>\dfrac{1}{2\mathrm e}$ 时**无实根。均不满足「两个不同的正数 $y$」。" "\n"
        r"故 $a\in\left(0,\dfrac{1}{2\mathrm e}\right)$，选 $\mathbf{A}$。"
    ),
    'review': (
        r"① ⭐⭐ **题干还原：原提取的「$x^{2}\ln y-\ln x-ay^{2}=0$」是错位文本。** 原件 p109 变式 21 的详解通篇走"
        r"$\mathrm e^{x}\left(y-x\right)-a\mathrm e^{2y-x}=0$；三个独立锚点互证：换元 $t=2\left(x-y\right)$、"
        r"表达式 $a=-\dfrac12 t\mathrm e^{t}$、$g\left(-1\right)=\dfrac1{2\mathrm e}$ 与单调区间。" "\n"
        r"② ⭐ **「对任意 $x$」的落实是本题的收口**：两根 $t$ 均为负 ⟹ $y=x-\dfrac t2>x>0$ 自动成立，"
        r"这正是答案能取满 $\left(0,\dfrac1{2\mathrm e}\right)$ 的原因；若有一根为正，则大 $x$ 小 $x$ 不能兼顾。" "\n"
        r"③ ⭐ **$t\mathrm e^{t}$ 型的值域**：$g\left(t\right)=-\dfrac12 t\mathrm e^{t}$ 在 $t=-1$ 取极大 $\dfrac1{2\mathrm e}$，"
        r"$t\to-\infty$ 趋于 $0$，$t\to+\infty$ 趋于 $-\infty$ —— 这个「单峰 + 单侧渐近」的图象要能直接画出来。" "\n"
        r"④ 数值复核：$a=0.18$ 时两根 $t_{1}=-1.2228,\ t_{2}=-0.8061$ 均为负 ✓；"
        r"$a=0.2>\dfrac1{2\mathrm e}=0.1839$ 时无解 ✓"
    ),
    'topics': ['M-T-143'],
    'src': 'M-T-143-V1',
    'difficulty': 0.78,
})

# ── 3. M-T-210-V2 向量与三角形四心（详解为空，独立推导补全）──────────────
QS.append({
    'type': '选择',
    'stem_text': (
        r"设 $O$ 是平面上一定点，$A,B,C$ 是平面上不共线的三点，动点 $P$ 满足" "\n"
        r"$\overrightarrow{OP}=\overrightarrow{OA}+\lambda\left(\dfrac{\overrightarrow{AB}}{\left|\overrightarrow{AB}\right|\cos B}"
        r"+\dfrac{\overrightarrow{AC}}{\left|\overrightarrow{AC}\right|\cos C}\right),\ \lambda\in\left(0,+\infty\right)$，"
        r"则动点 $P$ 的轨迹一定通过 $\triangle ABC$ 的（　　）"
    ),
    'opts': [
        ('A', r"外心"),
        ('B', r"内心"),
        ('C', r"重心"),
        ('D', r"垂心"),
    ],
    'answer': r"D",
    'analysis': (
        r"移项得 $\overrightarrow{AP}$ 的表达式，只需计算 $\overrightarrow{AP}\cdot\overrightarrow{BC}$："
        r"若恒为 $0$，则 $AP$ 是 $BC$ 边上的高线，必过垂心。"
    ),
    'solution': (
        r"移项得 $\overrightarrow{AP}=\overrightarrow{OP}-\overrightarrow{OA}"
        r"=\lambda\left(\dfrac{\overrightarrow{AB}}{c\cos B}+\dfrac{\overrightarrow{AC}}{b\cos C}\right)$，" "\n"
        r"其中 $a=\left|\overrightarrow{BC}\right|,\ b=\left|\overrightarrow{CA}\right|,\ c=\left|\overrightarrow{AB}\right|$。" "\n"
        r"计算 $\overrightarrow{AP}$ 与 $\overrightarrow{BC}$ 的数量积。注意两个夹角：" "\n"
        r"$\overrightarrow{AB}$ 与 $\overrightarrow{BC}$ 的夹角是 $\pi-B$（不是 $B$），故" "\n"
        r"$\overrightarrow{AB}\cdot\overrightarrow{BC}=ca\cos\left(\pi-B\right)=-ac\cos B$；" "\n"
        r"$\overrightarrow{AC}$ 与 $\overrightarrow{BC}$ 的夹角就是 $C$，故" "\n"
        r"$\overrightarrow{AC}\cdot\overrightarrow{BC}=ba\cos C=ab\cos C$。" "\n"
        r"于是" "\n"
        r"$\overrightarrow{AP}\cdot\overrightarrow{BC}"
        r"=\lambda\left(\dfrac{-ac\cos B}{c\cos B}+\dfrac{ab\cos C}{b\cos C}\right)=\lambda\left(-a+a\right)=0$。" "\n"
        r"即 $\overrightarrow{AP}\perp\overrightarrow{BC}$ 恒成立，故点 $P$ 恒在过 $A$ 且垂直于 $BC$ 的直线上，"
        r"也就是 $BC$ 边上的**高线**所在直线（$\lambda>0$ 时为一条射线）。" "\n"
        r"三角形三条高线交于垂心，故轨迹一定通过 $\triangle ABC$ 的**垂心**，选 $\mathbf{D}$。"
    ),
    'review': (
        r"① ⭐⭐ **原书详解为空，本解为独立推导补全（B 级）。** 题干与选项完整、答案 D 明确，"
        r"由 $\overrightarrow{AP}\cdot\overrightarrow{BC}=0$ 一步定出垂心。" "\n"
        r"② ⭐⭐ **两个夹角是本题唯一的坑**：$\overrightarrow{AB}$ 与 $\overrightarrow{BC}$ 首尾相接于 $B$，"
        r"夹角是 $\pi-B$ 而非 $B$；而 $\overrightarrow{AC}$ 与 $\overrightarrow{BC}$ 同终于 $C$，夹角就是 $C$。"
        r"搞反任何一个都得不到 $\left(-a+a\right)=0$。" "\n"
        r"③ ⭐ **分母 $\cos B,\cos C$ 是抵消的设计**：$c$ 与 $b$ 被 $\left|\overrightarrow{AB}\right|,\left|\overrightarrow{AC}\right|$ 约掉，"
        r"$\cos B,\cos C$ 被分母约掉，最后只剩 $-a+a$。若分母改成 $\sin B,\sin C$ 则结论完全不同。" "\n"
        r"④ 数值复核：随机取 $4$ 组不共线三点，算得 $\overrightarrow{AP}\cdot\overrightarrow{BC}$ 分别为"
        r"$3.5\times10^{-16},\ -7.6\times10^{-16},\ -1.9\times10^{-14},\ -2.4\times10^{-15}$，均为 $0$ ✓" "\n"
        r"⑤ ⚠ 若 $\cos B$ 或 $\cos C$ 为 $0$（直角三角形），表达式无意义，题干隐含 $\triangle ABC$ 非直角。"
    ),
    'topics': ['M-T-210'],
    'src': 'M-T-210-V2',
    'difficulty': 0.68,
})

# ── 4. M-T-294-V3 三视图外接球（回填：从棱长 3 的正方体截得）────────────
QS.append({
    'type': '选择',
    'stem_text': (
        r"某三棱锥是从棱长为 $3$ 的正方体中截得的，其四个顶点恰为正方体的一个顶点"
        r"及与该顶点相邻的三个顶点，则该三棱锥的外接球表面积为（　　）"
    ),
    'opts': [
        ('A', r"$3\pi$"),
        ('B', r"$12\pi$"),
        ('C', r"$18\pi$"),
        ('D', r"$27\pi$"),
    ],
    'answer': r"D",
    'analysis': (
        r"四个顶点都是正方体的顶点，而正方体的八个顶点共球；四点不共面，"
        r"故三棱锥的外接球就是正方体的外接球。"
    ),
    'solution': (
        r"正方体的八个顶点都在其外接球上。取该三棱锥的四个顶点，它们同样是正方体的顶点，"
        r"且**四点不共面**，故这四点确定的唯一球就是正方体的外接球。" "\n"
        r"棱长为 $3$ 的正方体，体对角线长为 $\sqrt{3^{2}+3^{2}+3^{2}}=3\sqrt3$，" "\n"
        r"外接球半径 $R=\dfrac{3\sqrt3}{2}$，" "\n"
        r"表面积 $S=4\pi R^{2}=4\pi\cdot\dfrac{27}{4}=27\pi$。" "\n"
        r"故选 $\mathbf{D}$。"
    ),
    'review': (
        r"① ⭐⭐ **回填依据**：原件 p261 原题为网格纸三视图（粗线条图形），选项为四张图；"
        r"详解明写「它是从一个四棱锥截下的部分……四棱锥又可以看作是从边长为 $3$ 的正方体中截取出来的，"
        r"所以三棱锥的外接球就是截取它的正方体的外接球」——几何体已被文字完整描述，可回填。" "\n"
        r"② ⭐ **四点共球的验证**：建系取 $\left(0,0,0\right),\left(3,0,0\right),\left(0,3,0\right),\left(0,0,3\right)$，"
        r"球心 $\left(1.5,1.5,1.5\right)$，半径 $\dfrac{3\sqrt3}{2}$，四点到球心距离均相等 ✓" "\n"
        r"③ 数值复核：$R=2.598076$，$S=4\pi R^{2}=84.823=27\pi$ ✓" "\n"
        r"④ ⭐ **通法**：从正方体（长方体）顶点中取的几何体，其外接球往往就是原正方体的外接球，"
        r"只要确认各顶点都是原正方体顶点且不共面即可，不必另求球心。"
    ),
    'topics': ['M-T-294'],
    'src': 'M-T-294-V3',
    'difficulty': 0.55,
})

# ── 5. M-T-279-V1 动点等距求轨迹（图形选择题降级）──────────────────────
QS.append({
    'type': '解答',
    'stem_text': (
        r"在四棱锥 $P-ABCD$ 中，侧面 $PAD$ 为正三角形，底面 $ABCD$ 为正方形，"
        r"侧面 $PAD\perp$ 底面 $ABCD$，$M$ 为正方形 $ABCD$ 内（包括边界）的一个动点，"
        r"且满足 $MP=MC$。求点 $M$ 在正方形 $ABCD$ 内的轨迹。" "\n"
        r"（原题为图形选择题，四个选项为轨迹图，已降级为解答题）"
    ),
    'opts': [],
    'answer': r"轨迹为一条线段 $y=\dfrac12 x$（$0\le x\le a$），即从点 $D$ 到棱 $AB$ 中点的线段",
    'analysis': (
        r"建系：$D$ 为原点，$DA,DC$ 所在直线为 $x,y$ 轴，写出 $P,C$ 坐标，"
        r"由 $\left|\overrightarrow{MP}\right|=\left|\overrightarrow{MC}\right|$ 平方后化简即得 $x$ 与 $y$ 的关系。"
    ),
    'solution': (
        r"以 $D$ 为坐标原点，$DA,DC$ 所在直线分别为 $x,y$ 轴建立空间直角坐标系。" "\n"
        r"设正方形边长为 $a$，则 $0\le x\le a,\ 0\le y\le a$，$M\left(x,y,0\right)$，$C\left(0,a,0\right)$。" "\n"
        r"侧面 $PAD$ 为正三角形且垂直于底面，故 $P$ 在底面上的射影为 $AD$ 的中点，$P\left(\dfrac a2,0,\dfrac{\sqrt3}2a\right)$。" "\n"
        r"于是" "\n"
        r"$\left|\overrightarrow{MC}\right|^{2}=x^{2}+\left(a-y\right)^{2}=x^{2}+a^{2}-2ay+y^{2}$，" "\n"
        r"$\left|\overrightarrow{MP}\right|^{2}=\left(\dfrac a2-x\right)^{2}+y^{2}+\left(\dfrac{\sqrt3}2a\right)^{2}"
        r"=x^{2}-ax+\dfrac{a^{2}}4+y^{2}+\dfrac{3a^{2}}4=x^{2}-ax+y^{2}+a^{2}$。" "\n"
        r"由 $\left|\overrightarrow{MP}\right|=\left|\overrightarrow{MC}\right|$ 得" "\n"
        r"$x^{2}-ax+y^{2}+a^{2}=x^{2}-2ay+y^{2}+a^{2}\Rightarrow -ax=-2ay\Rightarrow x=2y$。" "\n"
        r"即 $y=\dfrac12 x$，其中 $0\le x\le a$（相应地 $0\le y\le\dfrac a2$，落在正方形内）。" "\n"
        r"故点 $M$ 的轨迹是**从 $D\left(0,0\right)$ 到 $AB$ 中点 $\left(a,\dfrac a2\right)$ 的一条线段**。"
    ),
    'review': (
        r"① ⭐ **降级录入**：原题四个选项均为轨迹图（提取为空），但详解完整给出方程 $x=2y$，"
        r"故改为解答题「求轨迹」，题目脱离原图独立成立。" "\n"
        r"② ⭐ **$P$ 的坐标是题眼**：正三角形 $PAD\perp$ 底面 ⟹ $P$ 的射影是 $AD$ 中点 $\left(\dfrac a2,0\right)$，"
        r"高为 $\dfrac{\sqrt3}2a$。这个「射影落在边上而非顶点」是最易错的一步。" "\n"
        r"③ ⭐ **平方后 $x^{2},y^{2},a^{2}$ 全部抵消**，只剩 $-ax=-2ay$，一次式直接给出直线 —— "
        r"这是等距轨迹题的常态：二次项必消，所以轨迹是直线（段）或圆锥曲线，看剩余项。" "\n"
        r"④ 数值复核（$a=2$）：$y=0,0.2,0.5,0.8,1.0$ 各点代入，$\left|MP\right|^{2}$ 与 $\left|MC\right|^{2}$ 之差"
        r"均 $\le9\times10^{-16}$ ✓" "\n"
        r"⑤ ⚠ 轨迹是**线段**不是整条直线，受 $0\le x\le a$ 与 $0\le y\le a$ 双重限制，端点为 $D$ 与 $AB$ 中点。"
    ),
    'topics': ['M-T-279'],
    'src': 'M-T-279-V1',
    'difficulty': 0.66,
})

# ── 6. M-T-284-V1 截面与俯视图（图形选择题降级）────────────────────────
QS.append({
    'type': '解答',
    'stem_text': (
        r"正四棱锥 $P-ABCD$ 的高为 $12$，$AB=6\sqrt2$，$E,F$ 分别为 $PA,PC$ 的中点，"
        r"过点 $B,E,F$ 的截面交 $PD$ 于点 $M$，过 $M$ 作 $MG\perp DB$ 于 $G$。求 $DG$ 与 $GB$ 的长。" "\n"
        r"（原题问该几何体的俯视图，四个选项为网格图，已降级为解答题）"
    ),
    'opts': [],
    'answer': r"$DG=4,\quad GB=8$",
    'analysis': (
        r"在平面 $DPB$ 内研究：由 $E,F$ 为中点得 $EF$ 过 $PO$ 中点 $N$，"
        r"算出 $\tan\angle PDB$，再在直角 $\triangle MGB$ 中利用 $\angle NBO=45^{\circ}$ 列方程。"
    ),
    'solution': (
        r"设 $AC\cap BD=O$。底面正方形边长 $6\sqrt2$，故 $BD=6\sqrt2\times\sqrt2=12$，$OB=OD=6$。" "\n"
        r"又高 $PO=12$，故 $\tan\angle PDB=\dfrac{PO}{OD}=\dfrac{12}{6}=2$。" "\n"
        r"**确定 $N$ 的位置：** $E,F$ 为 $PA,PC$ 的中点，故 $EF\parallel AC$，"
        r"且 $EF$ 与 $PO$ 的交点 $N$ 是 $PO$ 的中点（$\triangle PAC$ 中 $EF$ 为中位线）。" "\n"
        r"于是 $ON=\dfrac{PO}{2}=6=OB$，又 $ON\perp OB$，故 $\angle NBO=45^{\circ}$。" "\n"
        r"**列方程：** 点 $M$ 在直线 $BN$ 上，过 $M$ 作 $MG\perp DB$ 于 $G$。设 $GB=x$。" "\n"
        r"在 $\triangle MGB$ 中，$\angle MBG=\angle NBO=45^{\circ}$，故 $MG=GB=x$。" "\n"
        r"又 $DB=12$，故 $DG=12-x$，而 $\tan\angle PDB=\dfrac{MG}{DG}=\dfrac{x}{12-x}=2$。" "\n"
        r"解得 $x=24-2x\Rightarrow 3x=24\Rightarrow x=8$。" "\n"
        r"故 $GB=8$，$DG=12-8=4$。"
    ),
    'review': (
        r"① ⭐ **降级录入**：原题问「俯视图为」，四个选项均为网格纸图形；详解给出了 $DG=4$ 个格、"
        r"$GB=8$ 个格的具体数值，故改为求这两段长度，计算过程完整保留。" "\n"
        r"② ⭐ **$N$ 是 $PO$ 中点**是本题的枢纽：$EF\parallel AC$ 且 $E,F$ 为中点 ⟹ $EF$ 与 $PO$ 交于 $PO$ 中点，"
        r"于是 $ON=OB=6$ ⟹ $\angle NBO=45^{\circ}$ ⟹ $MG=GB$，方程才能一步解出。" "\n"
        r"③ ⭐ **两次用 $\tan\angle PDB=2$**：第一次由 $PO/OD$ 定出这个比值，第二次把它用到 $MG/DG$ 上 —— "
        r"同一个角出现在两个相似位置，是这类题的标准结构。" "\n"
        r"④ 数值复核：$AB=8.485$，$BD=12$，$OD=6$，$\tan\angle PDB=2$，$x=8$ 时 $\dfrac{8}{12-8}=2$ ✓" "\n"
        r"⑤ ⚠ $M$ 在 $PD$ 上，故 $G$ 落在 $DB$ 上且靠近 $B$；若把 $DG$ 与 $GB$ 对调就说明 $x$ 设反了。"
    ),
    'topics': ['M-T-284'],
    'src': 'M-T-284-V1',
    'difficulty': 0.72,
})

# ── 7. M-T-284-E1 正四面体截面（图形选择题降级）────────────────────────
QS.append({
    'type': '解答',
    'stem_text': (
        r"正四面体 $ABCD$ 的棱长为 $a$，过侧棱 $AB$ 与对棱 $CD$ 的中点 $E$ 作截面，"
        r"求所得截面的形状，并求截面三角形各边的长。" "\n"
        r"（原题为图形选择题，四个选项为截面图，已降级为解答题）"
    ),
    'opts': [],
    'answer': (
        r"截面为等腰三角形 $ABE$：$AE=BE=\dfrac{\sqrt3}{2}a$，$AB=a$（底边 $AB$ 比腰长）"
    ),
    'analysis': (
        r"截面即平面 $ABE$ 截正四面体所得的三角形；$E$ 为 $CD$ 中点，"
        r"在正三角形 $ACD$ 与 $BCD$ 中分别求 $AE,BE$ 即可。"
    ),
    'solution': (
        r"平面 $ABE$ 与棱 $CD$ 交于其中点 $E$，与面 $ABC,ABD$ 分别交于 $AB$，"
        r"与面 $ACD,BCD$ 分别交于 $AE,BE$，故截面为 $\triangle ABE$。" "\n"
        r"$\triangle ACD$ 与 $\triangle BCD$ 都是棱长为 $a$ 的正三角形，$E$ 为 $CD$ 中点，"
        r"故 $AE,BE$ 分别是这两个正三角形的高：" "\n"
        r"$AE=BE=\dfrac{\sqrt3}{2}a$，而 $AB=a$。" "\n"
        r"所以截面 $\triangle ABE$ 是**等腰三角形**（$AE=BE$），且" "\n"
        r"$\cos\angle AEB=\dfrac{AE^{2}+BE^{2}-AB^{2}}{2\cdot AE\cdot BE}"
        r"=\dfrac{\frac34a^{2}+\frac34a^{2}-a^{2}}{2\cdot\frac34a^{2}}=\dfrac{\frac12a^{2}}{\frac32a^{2}}=\dfrac13>0$。" "\n"
        r"$\angle AEB\approx70.5^{\circ}$ 为锐角，故这是一个**锐角等腰三角形**，"
        r"且因 $\dfrac{\sqrt3}{2}a\approx0.866a<a$，腰比底边短。"
    ),
    'review': (
        r"① ⭐ **降级录入**：原题四个选项均为截面图形（提取为空），详解只说「是（图）」；"
        r"但正四面体是完全确定的几何体，截面形状可由计算独立定出，故改为解答题。" "\n"
        r"② ⭐ **题干中「内切球」的描述与截面无关**，原书提到内切球只是铺垫（切点为各面中心）；"
        r"降级后该条件冗余，已在题干中精简，不影响结论。" "\n"
        r"③ ⭐ **$\cos\angle AEB=\dfrac13$ 是正四面体的特征常数**（相邻面的二面角余弦也是 $\dfrac13$ 的相关值），"
        r"可作自检：算得别的值说明边长代错了。" "\n"
        r"④ 数值复核（$a=1$）：$AE=BE=0.866025$，$AB=1$，$\cos\angle AEB=0.33333=\dfrac13$ ✓" "\n"
        r"⑤ ⚠ 易错点：误以为腰 $\dfrac{\sqrt3}{2}a$ 大于底 $a$ —— 实际 $\dfrac{\sqrt3}{2}\approx0.866<1$，底边更长。"
    ),
    'topics': ['M-T-284'],
    'src': 'M-T-284-E1',
    'difficulty': 0.58,
})
