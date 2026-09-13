# -*- coding: utf-8 -*-
r"""第 114 批：三角函数「图象与性质」—— 周期、对称轴、辅助角、最值、向量

    python3 tools/run_batch.py 114

## 选题依据

先用「12 字 shingle 倒排索引」给全部剩余题重新定位页码（pick_batch 自带定位有偏差，
例如 M-T-161-E1 实为 p126 而非 p075），发现 **p141–p149 是一整块三角函数**，共 13 题：

- M-T-175-E1、M-T-175-V1（p141）：$\dfrac1{\sin^4x}-1$ 型周期、$\left|1+2\sin2x\right|$ 的周期
- M-T-176-V2、M-T-176-V3（p142）：对称轴间距定 $\omega$、辅助角 + 存在性
- M-T-178-E1（p143）：$\lambda\left|\omega\right|\gea$ 型恒成立
- M-T-183-V1（p148）：柯西求二元线性最大值
- M-T-187-V1（p149）：向量数量积绝对值之和的最大值

**未录（登记 skipped.json）**：
- M-T-174-V3（p141）：题干含「如图」，图象关键数据缺失
- M-T-181-E1（p146）：**原书答案错误**，详见下方「原书笔误」
- M-T-185-V1（p149）：字面最大值为 $24$，与原书答案 $8$ 矛盾（第 82 批已判，此前漏登记）

## 第一条：$\dfrac8{\sin^22x}+1$ 的周期只看 $\sin^22x$（M-T-175-E1）

$$\left(\frac1{\sin^4x}-1\right)\left(\frac1{\cos^4x}-1\right)=\frac{\cos^2x\left(1+\sin^2x\right)}{\sin^4x}\cdot\frac{\sin^2x\left(1+\cos^2x\right)}{\cos^4x}=\frac{2+\sin^2x\cos^2x}{\sin^2x\cos^2x}=\frac8{\sin^22x}+1$$

> ⭐⭐ 判据：**分子展开后 $1+\sin^2x+\cos^2x+\sin^2x\cos^2x=2+\sin^2x\cos^2x$**，恰好能拆成「常数 + 分母同构项」。
> ⭐⭐ $\sin^22x$ 的周期是 $\dfrac\pi2$（不是 $\pi$），故 $T=\dfrac\pi2$。

## 第二条：$\left|f\right|$ 的周期未必减半（M-T-175-V1）

$1+2\sin2x$ 的值域是 $\left[-1,3\right]$，**均值非零**，加绝对值后周期仍是 $\pi$ 而不是 $\dfrac\pi2$。

> ⭐⭐ 判据：**只有「均值为 $0$」的函数加绝对值才会周期减半**（如 $\left|\sin x\right|$）。
> ⭐ 若理解为 $1+2\sin^2x$（恒正），周期同为 $\pi$ —— 两种读法答案一致。

## 第三条：相邻对称轴距离 $=\dfrac T2$（M-T-176-V2）

$\left|x_1-x_2\right|_{\min}=\dfrac\pi2\ \Longrightarrow\ T=\pi\ \Longrightarrow\ \omega=1$，$f\left(x\right)=\sin\left(2x+\dfrac\pi3\right)$。

在 $\left[0,\dfrac\pi4\right]$ 上先增后减（峰值 $1$ 在 $x=\dfrac\pi{12}$），两端值为 $\dfrac{\sqrt3}2$ 与 $\dfrac12$。
$f\left(x\right)=-k$ 有两解 ⟺ $-k\in\left[\dfrac{\sqrt3}2,1\right)$ ⟺ $k\in\left(-1,-\dfrac{\sqrt3}2\right]$。

> ⭐⭐ 「两解」取的是**两支值域的交集**，上端点开（峰值处只交一次）。

## 第四条：存在性用「最小 + 最小 ≤ 最大」（M-T-176-V3）

$\exists x_1,x_2,x_3$ 使 $f\left(x_1\right)+f\left(x_2\right)\lef\left(x_3\right)$ ⟺ $2f_{\min}\lef_{\max}$。

> ⭐⭐ 因为 $f\left(x_1\right),f\left(x_2\right)$ 都可以独立取到最小值 —— **不是** $2f_{\min}\lef_{\min}$。

## 第五条：在 $x=x_0$ 取最大值 ⟹ 相位 $=\dfrac\pi2+2k\pi$（M-T-178-E1）

由此得 $\varphi=\dfrac\pi2+2k\pi-\dfrac{\omega\pi}6$，取正切后与 $\tan\varphi=a$ 联立；
再由 $f\left(\dfrac\pi3\right)=\sqrt3$ 得第二个方程，两式平方和为 $1$ 解出 $a=\sqrt3$。

> ⭐⭐ $\left|\omega\right|$ 在满足 $T<2\pi$ 的前提下取**最小**（$\omega=12k+1$，$k=-1$ 给 $\left|\omega\right|=11$）。
"""

# ==========================================================================
#  M-T-175  求周期
# ==========================================================================

T175_E1 = {
    'type': '选择',
    'stem_text': r"已知函数 $f\left(x\right)=\left(\dfrac{1}{\sin^{4}x}-1\right)\left(\dfrac{1}{\cos^{4}x}-1\right)$，则 $f\left(x\right)$ 的最小正周期为（　　）",
    'stem': [r"已知函数 $f\left(x\right)=\left(\dfrac{1}{\sin^{4}x}-1\right)\left(\dfrac{1}{\cos^{4}x}-1\right)$，则 $f\left(x\right)$ 的最小正周期为（　　）"],
    'opts': [['A', r"$2\pi$"], ['B', r"$\pi$"], ['C', r"$\dfrac{\pi}{2}$"], ['D', r"$\dfrac{\pi}{4}$"]],
    'answer': 'C',
    'analysis': (
        r"先把两个括号分别通分，约去 $\sin^2x\cos^2x$ 后化成 $\dfrac8{\sin^22x}+1$，" "\n"
        r"再由 $\sin^22x$ 的周期 $\dfrac\pi2$ 得结论。"
    ),
    'solution': (
        r"由题意 $\sin x\ne0$ 且 $\cos x\ne0$。分别通分：" "\n"
        r"$$\frac1{\sin^4x}-1=\frac{1-\sin^4x}{\sin^4x}=\frac{\left(1-\sin^2x\right)\left(1+\sin^2x\right)}{\sin^4x}=\frac{\cos^2x\left(1+\sin^2x\right)}{\sin^4x},$$" "\n"
        r"$$\frac1{\cos^4x}-1=\frac{1-\cos^4x}{\cos^4x}=\frac{\left(1-\cos^2x\right)\left(1+\cos^2x\right)}{\cos^4x}=\frac{\sin^2x\left(1+\cos^2x\right)}{\cos^4x}.$$" "\n"
        r"两式相乘，$\sin^2x$ 与 $\cos^2x$ 各约去一次：" "\n"
        r"$$f\left(x\right)=\frac{\left(1+\sin^2x\right)\left(1+\cos^2x\right)}{\sin^2x\cos^2x}.$$" "\n"
        r"展开分子：$\left(1+\sin^2x\right)\left(1+\cos^2x\right)=1+\sin^2x+\cos^2x+\sin^2x\cos^2x=2+\sin^2x\cos^2x$，" "\n"
        r"于是" "\n"
        r"$$f\left(x\right)=\frac{2+\sin^2x\cos^2x}{\sin^2x\cos^2x}=\frac2{\sin^2x\cos^2x}+1=\frac8{\left(2\sin x\cos x\right)^2}+1=\frac8{\sin^22x}+1.$$" "\n"
        r"因为 $\sin^22x=\dfrac{1-\cos4x}2$，其最小正周期为 $\dfrac{2\pi}4=\dfrac\pi2$，故 $f\left(x\right)$ 的最小正周期为 $\dfrac\pi2$。" "\n"
        r"故选 C。"
    ),
    'review': (
        r"① ⭐⭐ **关键一步是约分**：分子分母同有 $\sin^2x\cos^2x$，必须先约再展开，" "\n"
        r"   否则分子是四次式，看不出周期。" "\n"
        r"② ⭐⭐ **$\sin^22x$ 的周期是 $\dfrac\pi2$ 不是 $\pi$** —— 降幂后角频率翻倍为 $4$，周期 $\dfrac{2\pi}4$。" "\n"
        r"   误按 $\sin^2x$ 处理会得 $\pi$，选错 B。" "\n"
        r"③ ⭐ 「常数 $+1$」不影响周期，只需看 $\dfrac8{\sin^22x}$。" "\n"
        r"④ 数值复核：$x=\dfrac\pi8$ 时 $\sin^22x=\sin^2\dfrac\pi4=\dfrac12$，$f=16+1=17$；" "\n"
        r"   $x=\dfrac\pi8+\dfrac\pi2=\dfrac{5\pi}8$ 时 $\sin^22x=\sin^2\dfrac{5\pi}4=\dfrac12$，$f=17$ ✓ 周期 $\dfrac\pi2$ 成立；" "\n"
        r"   再取 $x=\dfrac\pi8+\dfrac\pi4=\dfrac{3\pi}8$，$\sin^22x=\sin^2\dfrac{3\pi}4=\dfrac12$ ——" "\n"
        r"   注意此点也相等，是因为 $\sin^22x$ 在 $\dfrac\pi4$ 平移下也对称，但最小正周期仍为 $\dfrac\pi2$" "\n"
        r"   （取 $x=\dfrac\pi{12}$：$\sin^2\dfrac\pi6=\dfrac14$，$f=33$；$x=\dfrac\pi{12}+\dfrac\pi4=\dfrac\pi3$，$\sin^2\dfrac{2\pi}3=\dfrac34$，$f=\dfrac83+1\ne33$ ✓ 说明 $\dfrac\pi4$ 不是周期）。" "\n"
        r"**通法（分式型三角周期）**：" "\n"
        r"① 括号内先通分，用 $1-\sin^4x=\cos^2x\left(1+\sin^2x\right)$ 这类分解；" "\n"
        r"② 相乘后约去公共因子，把式子化成「常数 $+$ 单个三角函数的简单分式」；" "\n"
        r"③ 用降幂公式确定角频率，再算 $T=\dfrac{2\pi}{\left|\omega\right|}$。"
    ),
    'difficulty': 0.58,
    'topics': ['M-T-175'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-175-E1',
}

T175_V1 = {
    'type': '选择',
    'stem_text': r"函数 $f\left(x\right)=\left|1+2\sin2x\right|$ 的最小正周期为（　　）",
    'stem': [r"函数 $f\left(x\right)=\left|1+2\sin2x\right|$ 的最小正周期为（　　）"],
    'opts': [['A', r"$\dfrac{\pi}{2}$"], ['B', r"$\pi$"], ['C', r"$\dfrac{3\pi}{2}$"], ['D', r"$2\pi$"]],
    'answer': 'B',
    'analysis': (
        r"$1+2\sin2x$ 的周期是 $\pi$，值域 $\left[-1,3\right]$ 跨越 $0$，" "\n"
        r"但**均值非零**，故加绝对值后周期不减半，仍为 $\pi$。"
    ),
    'solution': (
        r"令 $g\left(x\right)=1+2\sin2x$。因为 $\sin2x$ 的最小正周期为 $\dfrac{2\pi}2=\pi$，" "\n"
        r"所以 $g\left(x\right)$ 的最小正周期为 $\pi$，值域为 $\left[1-2,1+2\right]=\left[-1,3\right]$。" "\n"
        r"设 $f\left(x\right)=\left|g\left(x\right)\right|$ 的周期为 $T$，则 $f\left(x+T\right)=f\left(x\right)$。" "\n"
        r"先看 $T=\dfrac\pi2$ 是否可行：" "\n"
        r"$$f\left(x+\frac\pi2\right)=\left|1+2\sin\left(2x+\pi\right)\right|=\left|1-2\sin2x\right|.$$" "\n"
        r"取 $x=\dfrac\pi4$，则 $\sin2x=1$，此时 $f\left(x+\dfrac\pi2\right)=\left|1-2\right|=1$，而 $f\left(x\right)=\left|1+2\right|=3$，两者不等，" "\n"
        r"故 $\dfrac\pi2$ 不是周期。" "\n"
        r"再看 $T=\pi$：$f\left(x+\pi\right)=\left|1+2\sin\left(2x+2\pi\right)\right|=\left|1+2\sin2x\right|=f\left(x\right)$ 恒成立，" "\n"
        r"故 $\pi$ 是周期，结合 $\dfrac\pi2$ 不是周期且周期必为 $\pi$ 的整数分之一，最小正周期为 $\pi$。" "\n"
        r"故选 B。"
    ),
    'review': (
        r"① ⭐⭐ **本批最易错的一处**：见到绝对值就想当然「周期减半」。" "\n"
        r"   $\left|\sin x\right|$ 周期减半，是因为 $\sin x$ 关于 $x$ 轴对称（均值为 $0$）；" "\n"
        r"   $1+2\sin2x$ 的均值是 $1\ne0$，加绝对值后**只把 $x$ 轴下方的部分翻上去**，周期不变。" "\n"
        r"② ⭐ 判据：**$g$ 的周期 $T$ 已知时，$\left|g\right|$ 的周期是 $T$ 或 $\dfrac T2$**，" "\n"
        r"   只需代一个特殊点检验 $\dfrac T2$ 即可（本题取 $\sin2x=1$ 处最快）。" "\n"
        r"③ ⭐ 数值复核：$f\left(0\right)=1$；$f\left(\dfrac\pi2\right)=\left|1+2\sin\pi\right|=1$ ✓；" "\n"
        r"   $f\left(\dfrac\pi4\right)=3$，而 $f\left(\dfrac\pi4+\dfrac\pi2\right)=f\left(\dfrac{3\pi}4\right)=\left|1+2\sin\dfrac{3\pi}2\right|=\left|1-2\right|=1\ne3$ ✓ 排除 $\dfrac\pi2$。" "\n"
        r"④ 📌 题干 OCR 为 `|1 + 2sin2x|`。若原意是 $1+2\sin^2x$（恒正），绝对值不起作用，" "\n"
        r"   周期同为 $\pi$ —— **两种读法答案一致，不影响作答**。" "\n"
        r"**通法（带绝对值的三角周期）**：" "\n"
        r"① 先求内层 $g\left(x\right)$ 的周期 $T$ 与值域；" "\n"
        r"② 若 $g$ 恒非负或恒非正，周期就是 $T$；" "\n"
        r"③ 若 $g$ 变号，再检验 $\dfrac T2$：代一个使 $\left|g\right|$ 取到最值附近的点，看两端是否相等。"
    ),
    'difficulty': 0.50,
    'topics': ['M-T-175'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-175-V1',
}

# ==========================================================================
#  M-T-176  对称轴 / 辅助角
# ==========================================================================

T176_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知函数 $f\left(x\right)=\sin\omega x\cdot\cos\omega x+\sqrt{3}\cos^{2}\omega x-\dfrac{\sqrt{3}}{2}\ \left(\omega>0\right)$，" "\n"
        r"直线 $x=x_{1}$，$x=x_{2}$ 是 $y=f\left(x\right)$ 图象的任意两条对称轴，且 $\left|x_{1}-x_{2}\right|$ 的最小值为 $\dfrac{\pi}{2}$。" "\n"
        r"若关于 $x$ 的方程 $f\left(x\right)+k=0$ 在区间 $\left[0,\dfrac{\pi}{4}\right]$ 上有两个不同的实数解，则实数 $k$ 的取值范围为（　　）"
    ),
    'stem': [
        r"已知函数 $f\left(x\right)=\sin\omega x\cdot\cos\omega x+\sqrt{3}\cos^{2}\omega x-\dfrac{\sqrt{3}}{2}\ \left(\omega>0\right)$，直线 $x=x_{1}$，$x=x_{2}$ 是 $y=f\left(x\right)$ 图象的任意两条对称轴，且 $\left|x_{1}-x_{2}\right|$ 的最小值为 $\dfrac{\pi}{2}$。",
        r"若关于 $x$ 的方程 $f\left(x\right)+k=0$ 在区间 $\left[0,\dfrac{\pi}{4}\right]$ 上有两个不同的实数解，则实数 $k$ 的取值范围为（　　）",
    ],
    'opts': [['A', r"$\left(-1,1\right)$"], ['B', r"$\left[\dfrac{\sqrt{3}}{2},1\right)$"], ['C', r"$\left(-1,-\dfrac{\sqrt{3}}{2}\right]$"], ['D', r"$\left(-1,\dfrac{\sqrt{3}}{2}\right]$"]],
    'answer': 'C',
    'analysis': (
        r"先化一：$f\left(x\right)=\sin\left(2\omega x+\dfrac\pi3\right)$。相邻对称轴距离为 $\dfrac T2=\dfrac\pi2$ ⟹ $T=\pi$ ⟹ $\omega=1$。" "\n"
        r"再在 $\left[0,\dfrac\pi4\right]$ 上作 $f$ 的图象，看 $f\left(x\right)=-k$ 与曲线交两次的条件。"
    ),
    'solution': (
        r"先化简：" "\n"
        r"$$\sin\omega x\cos\omega x=\frac12\sin2\omega x,\qquad \sqrt3\cos^2\omega x=\sqrt3\cdot\frac{1+\cos2\omega x}2=\frac{\sqrt3}2+\frac{\sqrt3}2\cos2\omega x.$$" "\n"
        r"所以" "\n"
        r"$$f\left(x\right)=\frac12\sin2\omega x+\frac{\sqrt3}2\cos2\omega x+\frac{\sqrt3}2-\frac{\sqrt3}2=\sin\left(2\omega x+\frac\pi3\right).$$" "\n"
        r"相邻两条对称轴之间的距离为 $\dfrac T2$。由 $\left|x_1-x_2\right|_{\min}=\dfrac\pi2$ 得 $\dfrac T2=\dfrac\pi2$，即 $T=\pi$。" "\n"
        r"又 $T=\dfrac{2\pi}{2\omega}=\dfrac\pi\omega$，故 $\omega=1$，$f\left(x\right)=\sin\left(2x+\dfrac\pi3\right)$。" "\n"
        r"当 $x\in\left[0,\dfrac\pi4\right]$ 时，$2x+\dfrac\pi3\in\left[\dfrac\pi3,\dfrac{5\pi}6\right]$。$f$ 在该区间上先增后减：" "\n"
        r"① $x=0$ 时 $f=\sin\dfrac\pi3=\dfrac{\sqrt3}2$；" "\n"
        r"② 当 $2x+\dfrac\pi3=\dfrac\pi2$ 即 $x=\dfrac\pi{12}$ 时取最大值 $f=1$；" "\n"
        r"③ $x=\dfrac\pi4$ 时 $f=\sin\dfrac{5\pi}6=\dfrac12$。" "\n"
        r"方程 $f\left(x\right)+k=0$ 即 $f\left(x\right)=-k$。要使它在 $\left[0,\dfrac\pi4\right]$ 上有两个不同实根，" "\n"
        r"水平线 $y=-k$ 必须同时穿过递增段 $\left[0,\dfrac\pi{12}\right]$（值域 $\left[\dfrac{\sqrt3}2,1\right]$）" "\n"
        r"与递减段 $\left[\dfrac\pi{12},\dfrac\pi4\right]$（值域 $\left[\dfrac12,1\right]$），故" "\n"
        r"$$-k\in\left[\frac{\sqrt3}2,1\right)\ \Longrightarrow\ k\in\left(-1,-\frac{\sqrt3}2\right].$$" "\n"
        r"（右端取开是因为 $-k=1$ 时只交于峰值点 $x=\dfrac\pi{12}$ 一个点。）故选 C。"
    ),
    'review': (
        r"① ⭐⭐ **$\cos^2\omega x$ 的降幂是本题入口**：$\sqrt3\cos^2\omega x=\dfrac{\sqrt3}2+\dfrac{\sqrt3}2\cos2\omega x$，" "\n"
        r"   其中 $\dfrac{\sqrt3}2$ 恰好与式末的 $-\dfrac{\sqrt3}2$ 抵消 —— 这是命题人刻意设计的，看到抵消就知道化对了。" "\n"
        r"② ⭐⭐ **相邻对称轴距离 $=\dfrac T2$，不是 $T$**；由此 $T=\pi$、$\omega=1$。" "\n"
        r"   ⚠ 原书 OCR 在这步给出 $\omega=2$、$f=\sin\left(4x+\dfrac\pi3\right)$，与题设 $\dfrac\pi2$ 矛盾" "\n"
        r"   （$\omega=2$ 时 $\dfrac T2=\dfrac\pi4$）。但**两种取法算出的 $k$ 范围相同**，结论不受影响。" "\n"
        r"③ ⭐⭐ **「两解」取两支值域的交集**：递增段 $\left[\dfrac{\sqrt3}2,1\right]$、递减段 $\left[\dfrac12,1\right]$，" "\n"
        r"   交集 $\left[\dfrac{\sqrt3}2,1\right)$，由「较小的下端、较大的上端」决定。" "\n"
        r"④ ⚠ **上端点必须开**：$-k=1$ 时水平线只过峰值一个点，是一解不是两解。" "\n"
        r"⑤ 数值复核：$k=-\dfrac{\sqrt3}2\approx-0.8660$ 时 $-k=0.8660$，" "\n"
        r"   $x=0$ 与 $x=\dfrac\pi{12}+\left(\dfrac\pi{12}-0\right)\cdot$ … 直接验证 $f\left(0\right)=0.8660$ ✓ 且递减段上亦有一解 ✓；" "\n"
        r"   $k=-1$ 时 $-k=1$，只有 $x=\dfrac\pi{12}$ 一解 ✗（故 $-1$ 处开）✓。" "\n"
        r"**通法（对称轴间距 + 方程解个数）**：" "\n"
        r"① 化一为 $A\sin\left(\omega x+\varphi\right)$；" "\n"
        r"② 由相邻轴（或相邻中心）距离 $=\dfrac T2$ 定 $\omega$；" "\n"
        r"③ 在给定区间上按极值点分段，写出各段值域并取交集；" "\n"
        r"④ 峰值对应的一端取开区间。"
    ),
    'difficulty': 0.66,
    'topics': ['M-T-176'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-176-V2',
}

T176_V3 = {
    'type': '填空',
    'stem_text': (
        r"已知函数 $f\left(x\right)=a\sin\omega x+2\sin\left(\omega x+\dfrac{\pi}{3}\right)+b$ 的图象的相邻两个对称轴之间的距离为 $\dfrac{\pi}{2}$，" "\n"
        r"且 $\forall x\in\mathbb{R}$ 恒有 $f\left(x\right)\leqslant f\left(\dfrac{\pi}{6}\right)$。" "\n"
        r"若存在 $x_{1},x_{2},x_{3}\in\left[0,\dfrac{\pi}{2}\right]$，使得 $f\left(x_{1}\right)+f\left(x_{2}\right)\leqslant f\left(x_{3}\right)$ 成立，则 $b$ 的取值范围为 ____。"
    ),
    'stem': [
        r"已知函数 $f\left(x\right)=a\sin\omega x+2\sin\left(\omega x+\dfrac{\pi}{3}\right)+b$ 的图象的相邻两个对称轴之间的距离为 $\dfrac{\pi}{2}$，且 $\forall x\in\mathbb{R}$ 恒有 $f\left(x\right)\leqslant f\left(\dfrac{\pi}{6}\right)$。",
        r"若存在 $x_{1},x_{2},x_{3}\in\left[0,\dfrac{\pi}{2}\right]$，使得 $f\left(x_{1}\right)+f\left(x_{2}\right)\leqslant f\left(x_{3}\right)$ 成立，则 $b$ 的取值范围为 ____。",
    ],
    'opts': [],
    'answer': r"$\left(-\infty,4\sqrt{3}\right]$",
    'analysis': (
        r"展开化一得 $R=\sqrt{\left(a+1\right)^2+3}$；由相邻轴距离定 $\omega=2$，由 $x=\dfrac\pi6$ 为最大值点定 $\varphi=\dfrac\pi6$ ⟹ $a=2$。" "\n"
        r"存在性问题化为 $2f_{\min}\leqslant f_{\max}$。"
    ),
    'solution': (
        r"展开：$2\sin\left(\omega x+\dfrac\pi3\right)=2\left(\sin\omega x\cos\dfrac\pi3+\cos\omega x\sin\dfrac\pi3\right)=\sin\omega x+\sqrt3\cos\omega x$，" "\n"
        r"所以 $f\left(x\right)=\left(a+1\right)\sin\omega x+\sqrt3\cos\omega x+b=R\sin\left(\omega x+\varphi\right)+b$，" "\n"
        r"其中 $R=\sqrt{\left(a+1\right)^2+3}$，$\tan\varphi=\dfrac{\sqrt3}{a+1}$。" "\n"
        r"相邻两个对称轴之间的距离为 $\dfrac T2=\dfrac\pi2$，故 $T=\pi$，$\omega=\dfrac{2\pi}T=2$。" "\n"
        r"又 $\forall x$ 恒有 $f\left(x\right)\leqslant f\left(\dfrac\pi6\right)$，说明 $x=\dfrac\pi6$ 是最大值点：" "\n"
        r"$$2\cdot\frac\pi6+\varphi=\frac\pi2+2k\pi\ \Longrightarrow\ \varphi=\frac\pi6+2k\pi.$$" "\n"
        r"于是 $\tan\varphi=\tan\dfrac\pi6=\dfrac1{\sqrt3}=\dfrac{\sqrt3}{a+1}$，得 $a+1=3$，即 $a=2$，$R=\sqrt{9+3}=2\sqrt3$。" "\n"
        r"故 $f\left(x\right)=2\sqrt3\sin\left(2x+\dfrac\pi6\right)+b$。" "\n"
        r"当 $x\in\left[0,\dfrac\pi2\right]$ 时，$2x+\dfrac\pi6\in\left[\dfrac\pi6,\dfrac{7\pi}6\right]$，$\sin$ 取值于 $\left[-\dfrac12,1\right]$，" "\n"
        r"所以 $f_{\max}=2\sqrt3+b$，$f_{\min}=-\sqrt3+b$。" "\n"
        r"「存在 $x_1,x_2,x_3$ 使 $f\left(x_1\right)+f\left(x_2\right)\leqslant f\left(x_3\right)$」" "\n"
        r"等价于 $2f_{\min}\leqslant f_{\max}$（$x_1,x_2$ 都取最小值点、$x_3$ 取最大值点即可）：" "\n"
        r"$$2\left(-\sqrt3+b\right)\leqslant 2\sqrt3+b\ \Longrightarrow\ b\leqslant 4\sqrt3.$$" "\n"
        r"故 $b$ 的取值范围为 $\left(-\infty,4\sqrt3\right]$。"
    ),
    'review': (
        r"① ⭐⭐ **「存在 $x_1,x_2,x_3$」化为 $2f_{\min}\leqslant f_{\max}$** —— 三个点可独立取值，" "\n"
        r"   左边取两个最小、右边取最大即最有利。切勿写成 $2f_{\min}\leqslant f_{\min}$。" "\n"
        r"② ⭐⭐ **恒有 $f\left(x\right)\leqslant f\left(x_0\right)$ ⟹ $x_0$ 是最大值点 ⟹ 相位 $=\dfrac\pi2+2k\pi$**，" "\n"
        r"   这一步直接定出 $\varphi$，进而定 $a$。" "\n"
        r"③ ⭐ $\sin$ 在 $\left[\dfrac\pi6,\dfrac{7\pi}6\right]$ 上的最小值是 $-\dfrac12$（在右端 $\dfrac{7\pi}6$ 处），不是 $-1$ —— " "\n"
        r"   **区间端点要单独算**，不能默认取到 $\pm1$。" "\n"
        r"④ 数值复核：$b=4\sqrt3\approx6.9282$ 时 $f_{\min}=-1.7321+6.9282=5.1961$，$f_{\max}=3.4641+6.9282=10.3923$，" "\n"
        r"   $2f_{\min}=10.3923=f_{\max}$ ✓ 恰好取等；$b=7$ 时 $2f_{\min}=2\left(5.2679\right)=10.5359>f_{\max}=10.4641$ ✗ 不成立 ✓。" "\n"
        r"**通法（辅助角 + 存在性）**：" "\n"
        r"① 展开并合并为 $R\sin\left(\omega x+\varphi\right)+b$，写清 $R$ 与 $\tan\varphi$；" "\n"
        r"② 由轴间距定 $\omega$，由最值点位置定 $\varphi$ 再定参数；" "\n"
        r"③ 在闭区间上求 $f_{\min},f_{\max}$（端点别忘）；" "\n"
        r"④ 存在性用「最有利取法」转化为最值之间的不等式。"
    ),
    'difficulty': 0.72,
    'topics': ['M-T-176'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-176-V3',
}

# ==========================================================================
#  M-T-178  恒成立与参数
# ==========================================================================

T178_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知函数 $f\left(x\right)=\sin\omega x+a\cos\omega x$，周期 $T<2\pi$，$f\left(\dfrac{\pi}{3}\right)=\sqrt{3}$，" "\n"
        r"且在 $x=\dfrac{\pi}{6}$ 处取得最大值，则使得不等式 $\lambda\left|\omega\right|\geqslant a$ 恒成立的实数 $\lambda$ 的最小值为（　　）"
    ),
    'stem': [
        r"已知函数 $f\left(x\right)=\sin\omega x+a\cos\omega x$，周期 $T<2\pi$，$f\left(\dfrac{\pi}{3}\right)=\sqrt{3}$，且在 $x=\dfrac{\pi}{6}$ 处取得最大值，",
        r"则使得不等式 $\lambda\left|\omega\right|\geqslant a$ 恒成立的实数 $\lambda$ 的最小值为（　　）",
    ],
    'opts': [['A', r"$\dfrac{\sqrt{3}}{10}$"], ['B', r"$\dfrac{\sqrt{3}}{11}$"], ['C', r"$\dfrac{\sqrt{3}}{12}$"], ['D', r"$\dfrac{\sqrt{3}}{13}$"]],
    'answer': 'B',
    'analysis': (
        r"化一后由「$x=\dfrac\pi6$ 取最大值」得 $\varphi$ 与 $\omega$ 的关系，取正切得 $a=\dfrac1{\tan\dfrac{\omega\pi}6}$；" "\n"
        r"再由 $f\left(\dfrac\pi3\right)=\sqrt3$ 得 $\cos\dfrac{\omega\pi}6=\dfrac{\sqrt3}{\sqrt{a^2+1}}$。" "\n"
        r"两式平方和为 $1$ 解出 $a$，最后由 $T<2\pi$ 取 $\left|\omega\right|$ 的最小值。"
    ),
    'solution': (
        r"设 $f\left(x\right)=\sqrt{a^2+1}\sin\left(\omega x+\varphi\right)$，其中 $\tan\varphi=a$。" "\n"
        r"由 $x=\dfrac\pi6$ 处取得最大值：" "\n"
        r"$$\frac{\omega\pi}6+\varphi=\frac\pi2+2k\pi\ \Longrightarrow\ \varphi=\frac\pi2+2k\pi-\frac{\omega\pi}6.$$" "\n"
        r"取正切：$\tan\varphi=\tan\left(\dfrac\pi2-\dfrac{\omega\pi}6\right)=\dfrac1{\tan\dfrac{\omega\pi}6}=a$，即" "\n"
        r"$$\tan\frac{\omega\pi}6=\frac1a.\qquad\text{①}$$" "\n"
        r"又 $f\left(\dfrac\pi3\right)=\sqrt{a^2+1}\sin\left(\dfrac{\omega\pi}3+\varphi\right)=\sqrt{a^2+1}\sin\left(\dfrac{\omega\pi}3+\dfrac\pi2-\dfrac{\omega\pi}6+2k\pi\right)$" "\n"
        r"$=\sqrt{a^2+1}\sin\left(\dfrac{\omega\pi}6+\dfrac\pi2\right)=\sqrt{a^2+1}\cos\dfrac{\omega\pi}6=\sqrt3$，故" "\n"
        r"$$\cos\frac{\omega\pi}6=\frac{\sqrt3}{\sqrt{a^2+1}}.\qquad\text{②}$$" "\n"
        r"由 ① 得 $\sin\dfrac{\omega\pi}6=\dfrac1a\cos\dfrac{\omega\pi}6=\dfrac{\sqrt3}{a\sqrt{a^2+1}}$。" "\n"
        r"代入 $\sin^2+\cos^2=1$：" "\n"
        r"$$\frac3{a^2\left(a^2+1\right)}+\frac3{a^2+1}=1\ \Longrightarrow\ \frac{3+3a^2}{a^2\left(a^2+1\right)}=1\ \Longrightarrow\ a^4-2a^2-3=0,$$" "\n"
        r"即 $\left(a^2-3\right)\left(a^2+1\right)=0$，得 $a^2=3$，又需 $a>0$（由 ① 与 $\cos>0$ 知 $\dfrac{\omega\pi}6$ 在第一象限），故 $a=\sqrt3$。" "\n"
        r"由 ①：$\tan\dfrac{\omega\pi}6=\dfrac1{\sqrt3}$，故 $\dfrac{\omega\pi}6=\dfrac\pi6+k\pi$，即 $\omega=6k+1$。" "\n"
        r"又由 ② 及 $a=\sqrt3$ 得 $\cos\dfrac{\omega\pi}6=\dfrac{\sqrt3}{\sqrt{a^2+1}}=\dfrac{\sqrt3}2>0$，故 $k$ 必为偶数。" "\n"
        r"记 $k=2m$，则 $\omega=12m+1$。由 $T=\dfrac{2\pi}{\left|\omega\right|}<2\pi$ 得 $\left|\omega\right|>1$，" "\n"
        r"于是 $\left|\omega\right|$ 的最小可取值为 $11$（$m=-1$，$\omega=-11$；此时 $\dfrac{\omega\pi}6=-\dfrac{11\pi}6$，" "\n"
        r"$\cos\left(-\dfrac{11\pi}6\right)=\dfrac{\sqrt3}2>0$ ✓）。" "\n"
        r"由 $\lambda\left|\omega\right|\geqslant a$ 恒成立得 $\lambda\geqslant\dfrac a{\left|\omega\right|}$，" "\n"
        r"为使它对一切可能的 $\left|\omega\right|$ 都成立，取 $\dfrac a{\left|\omega\right|}$ 的最大值，即 $\left|\omega\right|$ 最小时：" "\n"
        r"$$\lambda_{\min}=\frac{\sqrt3}{11}.$$" "\n"
        r"故选 B。"
    ),
    'review': (
        r"① ⭐⭐ **核心方程是「两式平方和为 $1$」**：由最大值点得 $\tan$、由函数值得 $\cos$，" "\n"
        r"   $\sin^2+\cos^2=1$ 自动消去 $\omega$ 只剩 $a$ —— 这是处理「角度未知」问题的固定套路。" "\n"
        r"② ⭐ **$f\left(\dfrac\pi3\right)$ 的相位要合并**：$\dfrac{\omega\pi}3+\varphi=\dfrac{\omega\pi}6+\dfrac\pi2+2k\pi$，" "\n"
        r"   用 $\sin\left(\theta+\dfrac\pi2\right)=\cos\theta$ 换掉，才能与 ① 配对。" "\n"
        r"③ ⭐⭐ **$\lambda\left|\omega\right|\geqslant a$ 恒成立 ⟹ $\lambda\geqslant\max\dfrac a{\left|\omega\right|}$**，" "\n"
        r"   而 $\dfrac a{\left|\omega\right|}$ 在 $\left|\omega\right|$ 最小时最大 —— 别把方向搞反。" "\n"
        r"④ ⚠ 原书选项 OCR 为 `3/10, 3/11, 3/12, 3/13`，**根号丢失**，实为 $\dfrac{\sqrt3}{10},\dfrac{\sqrt3}{11},\dfrac{\sqrt3}{12},\dfrac{\sqrt3}{13}$。" "\n"
        r"   判据：$a=\sqrt3$，若选项是 $\dfrac3{11}$ 则与 $a$ 明显不匹配，且 $\dfrac{\sqrt3}{11}$ 恰好是 $\dfrac a{\left|\omega\right|}$。" "\n"
        r"⑤ 数值复核：$a=\sqrt3\approx1.7321$，$\left|\omega\right|=11$ 时 $\lambda_{\min}=0.15746$；" "\n"
        r"   $\omega=-11$ 时 $f\left(\dfrac\pi3\right)=\sin\left(-\dfrac{11\pi}3\right)+\sqrt3\cos\left(-\dfrac{11\pi}3\right)$" "\n"
        r"   $=\sin\left(\dfrac\pi3\right)+\sqrt3\cos\left(\dfrac\pi3\right)=\dfrac{\sqrt3}2+\sqrt3\cdot\dfrac12=\sqrt3$ ✓；" "\n"
        r"   $x=\dfrac\pi6$ 处相位 $=-\dfrac{11\pi}6+\dfrac\pi3=-\dfrac{3\pi}2$，$\sin\left(-\dfrac{3\pi}2\right)=1$ ✓ 确为最大值点。" "\n"
        r"**通法（辅助角 + 两条件定参）**：" "\n"
        r"① 化为 $R\sin\left(\omega x+\varphi\right)$，写出 $R$ 与 $\tan\varphi$；" "\n"
        r"② 最值点给相位方程（取正切）、函数值给另一个三角方程；" "\n"
        r"③ 用 $\sin^2+\cos^2=1$ 消去角度；" "\n"
        r"④ 恒成立问题找「最不利」的那个参数取值。"
    ),
    'difficulty': 0.78,
    'topics': ['M-T-178'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-178-E1',
}

# ==========================================================================
#  M-T-183 / M-T-187  柯西与向量最值
# ==========================================================================

T183_V1 = {
    'type': '填空',
    'stem_text': r"若 $x^{2}+y^{2}=2$，那么 $2x-3y$ 的最大值为 ____。",
    'stem': [r"若 $x^{2}+y^{2}=2$，那么 $2x-3y$ 的最大值为 ____。"],
    'opts': [],
    'answer': r"$\sqrt{26}$",
    'analysis': r"柯西不等式：$\left(2x-3y\right)^2\leqslant\left(2^2+3^2\right)\left(x^2+y^2\right)=13\times2=26$。",
    'solution': (
        r"由柯西不等式" "\n"
        r"$$\left(2x-3y\right)^2=\left(2\cdot x+\left(-3\right)\cdot y\right)^2\leqslant\left(2^2+\left(-3\right)^2\right)\left(x^2+y^2\right)=13\times2=26,$$" "\n"
        r"故 $2x-3y\leqslant\sqrt{26}$。" "\n"
        r"当且仅当 $\dfrac x2=\dfrac y{-3}$，即 $\left(x,y\right)=\lambda\left(2,-3\right)$ 时取等。" "\n"
        r"代入 $x^2+y^2=2$ 得 $\lambda^2\left(4+9\right)=2$，$\lambda=\sqrt{\dfrac2{13}}$，" "\n"
        r"此时 $x=2\sqrt{\dfrac2{13}}$，$y=-3\sqrt{\dfrac2{13}}$，$2x-3y=4\lambda+9\lambda=13\lambda=\sqrt{26}$。" "\n"
        r"故最大值为 $\sqrt{26}$。"
    ),
    'review': (
        r"① ⭐⭐ **二元线性式在圆上的最值直接用柯西**：$\left(ax+by\right)^2\leqslant\left(a^2+b^2\right)\left(x^2+y^2\right)$，" "\n"
        r"   最大值为 $\sqrt{\left(a^2+b^2\right)r^2}$，其中 $r^2=x^2+y^2$。" "\n"
        r"② ⭐ 取等方向是 $\left(x,y\right)\parallel\left(a,b\right)$ —— 与系数**同向**取最大，反向取最小。" "\n"
        r"③ ⚠ 原书答案 OCR 为 `26`，**丢了根号**；由 $\left(2x-3y\right)^2\leqslant26$ 只能得 $\leqslant\sqrt{26}$，" "\n"
        r"   且 $26$ 显然太大（$\left|x\right|,\left|y\right|\leqslant\sqrt2$ 时 $2x-3y\leqslant2\sqrt2+3\sqrt2\approx7.07$，而 $26$ 远超）。" "\n"
        r"④ 数值复核：$x=2\sqrt{2/13}\approx0.7845$，$y=-3\sqrt{2/13}\approx-1.1767$，" "\n"
        r"   $x^2+y^2=0.6154+1.3846=2.0000$ ✓，$2x-3y=1.5690+3.5301=5.0991=\sqrt{26}$ ✓。" "\n"
        r"**通法（圆上的线性最值）**：柯西一步到位，取等方向平行系数向量；" "\n"
        r"若带常数项（$2x-3y+c$）则先平移再用同法。"
    ),
    'difficulty': 0.42,
    'topics': ['M-T-183'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-183-V1',
}

T187_V1 = {
    'type': '填空',
    'stem_text': (
        r"已知平面向量 $\vec{a},\vec{b},\vec{c}$ 满足 $\left|\vec{a}\right|=2$，$\left|\vec{b}\right|=3$，$\left|\vec{c}\right|=4$，$\vec{a}\cdot\vec{b}=\dfrac{3}{2}$，" "\n"
        r"则 $\left|\vec{a}\cdot\vec{c}\right|+\left|\vec{b}\cdot\vec{c}\right|$ 的最大值为 ____。"
    ),
    'stem': [
        r"已知平面向量 $\vec{a},\vec{b},\vec{c}$ 满足 $\left|\vec{a}\right|=2$，$\left|\vec{b}\right|=3$，$\left|\vec{c}\right|=4$，$\vec{a}\cdot\vec{b}=\dfrac{3}{2}$，",
        r"则 $\left|\vec{a}\cdot\vec{c}\right|+\left|\vec{b}\cdot\vec{c}\right|$ 的最大值为 ____。",
    ],
    'opts': [],
    'answer': r"$16$",
    'analysis': (
        r"由 $\vec a\cdot\vec b$ 定出 $\vec a,\vec b$ 的夹角，再把 $\vec c$ 的方向设为唯一变量 $\theta$，" "\n"
        r"目标式化为 $\left|A\cos\theta\right|+\left|B\cos\theta+C\sin\theta\right|$，按 $\vec a\cdot\vec c$、$\vec b\cdot\vec c$ 的零点分段。"
    ),
    'solution': (
        r"设 $\vec a=\left(2,0\right)$。由 $\vec a\cdot\vec b=\left|\vec a\right|\left|\vec b\right|\cos\alpha=6\cos\alpha=\dfrac32$ 得 $\cos\alpha=\dfrac14$，" "\n"
        r"$\sin\alpha=\dfrac{\sqrt{15}}4$，故 $\vec b=3\left(\dfrac14,\dfrac{\sqrt{15}}4\right)=\left(\dfrac34,\dfrac{3\sqrt{15}}4\right)$。" "\n"
        r"设 $\vec c=4\left(\cos\theta,\sin\theta\right)$，则" "\n"
        r"$$\vec a\cdot\vec c=8\cos\theta,\qquad \vec b\cdot\vec c=4\left(\frac34\cos\theta+\frac{3\sqrt{15}}4\sin\theta\right)=3\cos\theta+3\sqrt{15}\sin\theta.$$" "\n"
        r"记 $u=\vec a\cdot\vec c=8\cos\theta$，$v=\vec b\cdot\vec c$。注意" "\n"
        r"$$v=3\cos\theta+3\sqrt{15}\sin\theta=\frac38u+3\sqrt{15}\sin\theta,$$" "\n"
        r"且 $\sin^2\theta=1-\left(\dfrac u8\right)^2$，故 $v=\dfrac38u\pm3\sqrt{15}\sqrt{1-\dfrac{u^2}{64}}$。" "\n"
        r"目标是 $\left|u\right|+\left|v\right|$ 的最大值。分两段看：" "\n"
        r"① 当 $\vec a\cdot\vec c$ 与 $\vec b\cdot\vec c$ 同号时，" "\n"
        r"$$\left|u\right|+\left|v\right|=\left|u+v\right|=\left|11\cos\theta+3\sqrt{15}\sin\theta\right|\leqslant\sqrt{11^2+\left(3\sqrt{15}\right)^2}=\sqrt{121+135}=\sqrt{256}=16.$$" "\n"
        r"② 当两者异号时，$\left|u\right|+\left|v\right|=\left|u-v\right|=\left|5\cos\theta-3\sqrt{15}\sin\theta\right|\leqslant\sqrt{25+135}=\sqrt{160}=4\sqrt{10}\approx12.65<16$。" "\n"
        r"故最大值为 $16$，当 $11\cos\theta+3\sqrt{15}\sin\theta=16$ 时取到（此时两者同号，与分段前提一致）。"
    ),
    'review': (
        r"① ⭐⭐ **本批最值钱的一条**：$\left|u\right|+\left|v\right|$ 要**按 $u,v$ 是否同号分段**。" "\n"
        r"   同号时 $=\left|u+v\right|$，异号时 $=\left|u-v\right|$，各自用辅助角求最大再比较。" "\n"
        r"   ⚠ 不分段直接对 $\left|u\right|+\left|v\right|$ 用辅助角是错的。" "\n"
        r"② ⭐⭐ **$\left|u\pm v\right|$ 的最大值 $=\sqrt{\text{两系数平方和}}$**，因为 $u\pm v$ 本身仍是" "\n"
        r"   $A\cos\theta+B\sin\theta$ 的形式。本题 $u+v=11\cos\theta+3\sqrt{15}\sin\theta$ 给 $16$，" "\n"
        r"   $u-v=5\cos\theta-3\sqrt{15}\sin\theta$ 给 $4\sqrt{10}$。" "\n"
        r"③ ⭐ **$\cos\alpha=\dfrac{\vec a\cdot\vec b}{\left|\vec a\right|\left|\vec b\right|}=\dfrac{3/2}6=\dfrac14$**，$\sin\alpha=\dfrac{\sqrt{15}}4$ ——" "\n"
        r"   $\sqrt{15}$ 出现是 $\vec b$ 坐标变复杂的原因，但最终平方和恰好配成 $256=16^2$，非常整齐。" "\n"
        r"④ 数值复核：取 $\theta$ 使 $11\cos\theta+3\sqrt{15}\sin\theta=16$，" "\n"
        r"   即 $\cos\theta=\dfrac{11}{16}$，$\sin\theta=\dfrac{3\sqrt{15}}{16}$，此时" "\n"
        r"   $u=8\cdot\dfrac{11}{16}=5.5$，$v=3\cdot\dfrac{11}{16}+3\sqrt{15}\cdot\dfrac{3\sqrt{15}}{16}=2.0625+8.4375=10.5$，" "\n"
        r"   $\left|u\right|+\left|v\right|=16$ ✓ 且两者同为正 ✓ 与分段前提一致。" "\n"
        r"   另取 $\theta=\pi$：$u=-8$，$v=-3$，和为 $11<16$ ✓。" "\n"
        r"**通法（两个数量积的绝对值之和）**：" "\n"
        r"① 建系，把 $\vec a$ 放在 $x$ 轴上，用 $\vec a\cdot\vec b$ 定出 $\vec b$ 的夹角；" "\n"
        r"② 设 $\vec c=\left|\vec c\right|\left(\cos\theta,\sin\theta\right)$，把两个数量积都写成 $\theta$ 的一次齐次式；" "\n"
        r"③ 按同号 / 异号分成 $\left|u+v\right|$ 与 $\left|u-v\right|$ 两种情形；" "\n"
        r"④ 各用辅助角求最大值，取较大者并**回代验证符号前提**。"
    ),
    'difficulty': 0.74,
    'topics': ['M-T-187'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-187-V1',
}

QS = [
    T175_E1, T175_V1,
    T176_V2, T176_V3,
    T178_E1,
    T183_V1, T187_V1,
]
