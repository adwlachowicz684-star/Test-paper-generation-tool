# -*- coding: utf-8 -*-
r"""第33批（三）：几何概型 · 长度与角度（4题）

来源：2024高中数学热点题型归纳完整解析版.pdf p397~p398（PDF 页 396~397）

## 选题

`pick_batch.py --n 8 --topic M-T-406` 定位到 p397 + p398 两页。
4 题（E1、V2、V3、V4）题干完整、答案可验算。

## 跳过 1 题

**M-T-406-V1**（两圆相交、阴影面积相等、M 在线段 EF 上）：
详解的 $AB=\frac{\pi r}2$、$EF=2r-\frac{\pi r}2$ 依赖图示中「两块阴影面积相等」
这一几何关系，而**图未提取、纯文本无法复现**，故跳过。
（答案 C $=\frac4\pi-1$ 与 $\frac{EF}{AB}=\frac{2r-\pi r/2}{\pi r/2}$ 一致，
但 EF 的来由需图才能说清。）

## ★ 四题全部独立推导，且全部与答案吻合

| 题 | 我的推导 | 答案 |
|---|---|---|
| E1 | $P=2\sqrt{1-t^{2}}-1=\frac14$（$t=\frac{AD}{AB}$）→ $t=\frac{\sqrt{39}}8$ | **D** |
| V2 | $[0,\frac\pi3]\cup[\frac{3\pi}4,\pi]$，长度 $\frac{7\pi}{12}$ → $\frac7{12}$ | **A** |
| V3 | 弦长 $\ge2\sqrt3$ ⟺ $d\le1$ ⟺ $\lvert k\rvert\le\frac{\sqrt3}3$ → $\frac13$ | **C** |
| V4 | $[7{:}50,8{:}00]\cup[8{:}20,8{:}30]$，共 $20$ 分钟 / $40$ 分钟 → $\frac12$ | **B** |

其中 **E1 的 $\frac{\sqrt{39}}8$ 是我完整推出来的**（详解在双栏排版中被截断），
代回验证概率恰为 $\frac14$ ✓。
"""

T406_E1 = {
    'type': '选择',
    'stem_text': (
        r"在矩形 $ABCD$ 中，$AB>BC$，在 $CD$ 边上随机取一点 $P$，"
        r"若 $AB$ 是 $\triangle ABP$ 最大边的概率为 $\dfrac14$，"
        r"则 $\dfrac{AD}{AB}=$（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac13$"),
        ('B', r"$\dfrac{\sqrt2}2$"),
        ('C', r"$\dfrac{\sqrt{15}}8$"),
        ('D', r"$\dfrac{\sqrt{39}}8$"),
    ],
    'answer': 'D',
    'analysis': (
        r"建系后把「$AB$ 是最大边」转化为 $AP\leqslant AB$ 且 $BP\leqslant AB$，"
        r"解出 $P$ 的允许区间长度，再令其占 $CD$ 全长的比例为 $\frac14$。"
    ),
    'solution': (
        r"**建系**：设 $A(0,0)$、$B(a,0)$、$C(a,b)$、$D(0,b)$（$a=AB$、$b=AD$），"
        r"由 $AB>BC$ 知 $a>b$．" "\n"
        r"设 $P(p,b)$，$p\in[0,a]$．" "\n"
        r"**转化条件**：$AB$ 是 $\triangle ABP$ 的最大边" "\n"
        r"$\iff AP\leqslant AB$ 且 $BP\leqslant AB$（$AB=a$）．" "\n"
        r"$AP=\sqrt{p^{2}+b^{2}}\leqslant a\Rightarrow p^{2}\leqslanta^{2}-b^{2}"
        r"\Rightarrow p\leqslant\sqrt{a^{2}-b^{2}}$；" "\n"
        r"$BP=\sqrt{(p-a)^{2}+b^{2}}\leqslant a\Rightarrow(p-a)^{2}\leqslanta^{2}-b^{2}$" "\n"
        r"$\Rightarrow|p-a|\leqslant\sqrt{a^{2}-b^{2}}\Rightarrow p\geqslanta-\sqrt{a^{2}-b^{2}}$．" "\n"
        r"**允许区间**：$p\in\bigl[a-\sqrt{a^{2}-b^{2}},\ \sqrt{a^{2}-b^{2}}\bigr]$，" "\n"
        r"长度 $=2\sqrt{a^{2}-b^{2}}-a$（需 $\geqslant0$，即 $b\leqslant\frac{\sqrt3}2a$）．" "\n"
        r"**列方程**：概率 $=\dfrac{2\sqrt{a^{2}-b^{2}}-a}{a}=\dfrac14$．" "\n"
        r"令 $t=\dfrac ba=\dfrac{AD}{AB}$，则 $2\sqrt{1-t^{2}}-1=\dfrac14$：" "\n"
        r"$2\sqrt{1-t^{2}}=\dfrac54\Rightarrow\sqrt{1-t^{2}}=\dfrac58"
        r"\Rightarrow1-t^{2}=\dfrac{25}{64}$" "\n"
        r"$\Rightarrow t^{2}=\dfrac{39}{64}\Rightarrow t=\dfrac{\sqrt{39}}8$．" "\n"
        r"故选 D．"
    ),
    'review': (
        r"★ 题干、选项完整；**详解在双栏排版中被截断，上述推导是我独立完成的**。" "\n"
        r"**验算（代回）**：$t=\frac{\sqrt{39}}8\approx0.78062$，" "\n"
        r"$P=2\sqrt{1-0.78062^{2}}-1=2\sqrt{1-0.60937}-1=2\sqrt{0.39063}-1$" "\n"
        r"$=2\times0.625-1=1.25-1=0.25=\frac14$ ✓ **与题设完全吻合**。" "\n"
        r"**排除其他选项**（代入 $P=2\sqrt{1-t^2}-1$）：" "\n"
        r"$t=\frac13$：$P=2\sqrt{1-\frac19}-1=2\times0.94281-1=0.8856\neq\frac14$ ✗" "\n"
        r"$t=\frac{\sqrt2}2$：$P=2\sqrt{0.5}-1=2\times0.70711-1=0.4142\neq\frac14$ ✗" "\n"
        r"$t=\frac{\sqrt{15}}8\approx0.48412$：$P=2\sqrt{1-0.23438}-1=2\times0.875-1=0.75\neq\frac14$ ✗" "\n"
        r"**答案 D 正确** ✓" "\n"
        r"**⭐ 题型套路**：「某边是三角形最大边」⟺ 该边 $\geqslant$ 其余两边，"
        r"建系后化为两个圆内区域取交集，得到一段区间长度。"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-406'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-406-E1',
}

T406_V2 = {
    'type': '选择',
    'stem_text': (
        r"在区间 $[0,\pi]$ 上随机地取一个数 $x$，"
        r"则事件「$-1\leqslant\tan x\leqslant\sqrt3$」发生的概率为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac7{12}$"), ('B', r"$\dfrac23$"),
        ('C', r"$\dfrac13$"), ('D', r"$\dfrac14$"),
    ],
    'answer': 'A',
    'analysis': (
        r"在 $[0,\pi]$ 上分段解不等式（注意 $x=\frac\pi2$ 处 $\tan x$ 无定义），"
        r"得允许区间 $[0,\frac\pi3]\cup[\frac{3\pi}4,\pi]$，用长度比求概率。"
    ),
    'solution': (
        r"**分段讨论**（$x=\dfrac\pi2$ 处 $\tan x$ 无定义，把 $[0,\pi]$ 分成两段）：" "\n"
        r"**① $x\in\left[0,\dfrac\pi2\right)$**：$\tan x\geqslant0$，" "\n"
        r"$\tan x\geqslant-1$ 自动成立；$\tan x\leqslant\sqrt3\Rightarrow x\leqslant\dfrac\pi3$．" "\n"
        r"得 $x\in\left[0,\dfrac\pi3\right]$．" "\n"
        r"**② $x\in\left(\dfrac\pi2,\pi\right]$**：$\tan x<0$，" "\n"
        r"$\tan x\leqslant\sqrt3$ 自动成立；$\tan x\geqslant-1\Rightarrow x\geqslant\dfrac{3\pi}4$"
        r"（因 $\tan\dfrac{3\pi}4=-1$，且 $\tan$ 在此区间递增）．" "\n"
        r"得 $x\in\left[\dfrac{3\pi}4,\pi\right]$．" "\n"
        r"**求概率**：允许区间总长度" "\n"
        r"$=\dfrac\pi3+\left(\pi-\dfrac{3\pi}4\right)=\dfrac\pi3+\dfrac\pi4=\dfrac{7\pi}{12}$，" "\n"
        r"$P=\dfrac{7\pi/12}{\pi-0}=\dfrac7{12}$．" "\n"
        r"故选 A．"
    ),
    'review': (
        r"★ 还原版完整 ✓。由详解「∵$0\leqslant x\leqslant\pi$，"
        r"∴由 $-1\leqslant\tan x\leqslant\sqrt3$ 得，$0\leqslant x\leqslant\frac\pi3$ 或 "
        r"$\frac{3\pi}4\leqslant x\leqslant\pi$，则事件发生的概率为 "
        r"$P=\frac{\frac\pi3-0+\pi-\frac{3\pi}4}{\pi-0}=\frac7{12}$，故选 A」还原。" "\n"
        r"（题干的 $\sqrt3$ 在提取时丢根号显示为 `3`，按详解的 $\frac\pi3$ 判定为 $\sqrt3$ ✓）" "\n"
        r"**独立验算**：" "\n"
        r"$\tan\frac\pi3=\sqrt3$ ✓；$\tan\frac{3\pi}4=-1$ ✓" "\n"
        r"$\frac\pi3+(\pi-\frac{3\pi}4)=\frac{4\pi}{12}+\frac{3\pi}{12}=\frac{7\pi}{12}$ ✓" "\n"
        r"$P=\frac{7\pi/12}{\pi}=\frac7{12}\approx0.5833$ ✓ **答案 A 正确**。" "\n"
        r"**⭐ 易错点**：$x=\frac\pi2$ 处 $\tan x$ 无定义，必须把区间断开；"
        r"若误认为 $\tan x$ 在 $[0,\pi]$ 上连续递增，会漏掉 $[\frac{3\pi}4,\pi]$ 这段。"
    ),
    'difficulty': 0.78,
    'topics': ['M-T-406'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-406-V2',
}

T406_V3 = {
    'type': '选择',
    'stem_text': (
        r"任取 $k\in\left[-\sqrt3,\sqrt3\right]$，直线 $y=k(x+2)$ 与圆 $x^{2}+y^{2}=4$ "
        r"相交于 $A,B$ 两点，则 $|AB|\geqslant2\sqrt3$ 的概率为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac12$"), ('B', r"$\dfrac{\sqrt3}2$"),
        ('C', r"$\dfrac13$"), ('D', r"$\dfrac{\sqrt3}3$"),
    ],
    'answer': 'C',
    'analysis': (
        r"由弦长公式把 $|AB|\geqslant2\sqrt3$ 化为圆心到直线的距离 $d\leqslant1$，"
        r"解出 $|k|\leqslant\frac{\sqrt3}3$，再用区间长度比求概率。"
    ),
    'solution': (
        r"**弦长条件**：圆半径 $r=2$，弦长 $|AB|=2\sqrt{r^{2}-d^{2}}=2\sqrt{4-d^{2}}$，"
        r"其中 $d$ 为圆心到直线的距离．" "\n"
        r"$|AB|\geqslant2\sqrt3\Rightarrow2\sqrt{4-d^{2}}\geqslant2\sqrt3"
        r"\Rightarrow4-d^{2}\geqslant3\Rightarrow d^{2}\leqslant1\Rightarrow d\leqslant1$．" "\n"
        r"**表示 $d$**：直线 $y=k(x+2)$ 即 $kx-y+2k=0$；圆心 $O(0,0)$，" "\n"
        r"$d=\dfrac{|k\cdot0-0+2k|}{\sqrt{k^{2}+1}}=\dfrac{2|k|}{\sqrt{1+k^{2}}}$．" "\n"
        r"**解不等式**：" "\n"
        r"$\dfrac{2|k|}{\sqrt{1+k^{2}}}\leqslant1\Rightarrow4k^{2}\leqslant1+k^{2}"
        r"\Rightarrow3k^{2}\leqslant1\Rightarrow|k|\leqslant\dfrac1{\sqrt3}=\dfrac{\sqrt3}3$．" "\n"
        r"**求概率**：$k$ 的取值区间 $[-\sqrt3,\sqrt3]$ 长度 $=2\sqrt3$；" "\n"
        r"满足条件的区间 $\left[-\dfrac{\sqrt3}3,\dfrac{\sqrt3}3\right]$ 长度 $=\dfrac{2\sqrt3}3$．" "\n"
        r"$P=\dfrac{2\sqrt3/3}{2\sqrt3}=\dfrac13$．" "\n"
        r"故选 C．"
    ),
    'review': (
        r"★ 还原版完整 ✓。由详解「因弦长 $|AB|=2\sqrt{r^{2}-d^{2}}=2\sqrt{4-d^{2}}"
        r"\geqslant2\sqrt3$，故 $4-d^{2}\geqslant3$，即 $d^{2}\leqslant1$，$d\leqslant1$，"
        r"而圆心 $O(0,0)$ 到直线 $kx-y+2k=0$ 的距离 $d=\frac{|2k|}{\sqrt{1+k^{2}}}"
        r"=\frac{2|k|}{\sqrt{1+k^{2}}}$，所以 $\frac{2|k|}{\sqrt{1+k^{2}}}\leqslant1$」还原。" "\n"
        r"（详解在此处被截断，以下为我补全：）" "\n"
        r"$4k^2\le1+k^2\Rightarrow3k^2\le1\Rightarrow|k|\le\frac{\sqrt3}3$ ✓" "\n"
        r"**独立验算**：" "\n"
        r"$k=\frac{\sqrt3}3\approx0.57735$：$d=\frac{2\times0.57735}{\sqrt{1+0.33333}}"
        r"=\frac{1.1547}{1.15470}=1.0$ ✓ **恰好取等**" "\n"
        r"$|AB|=2\sqrt{4-1}=2\sqrt3$ ✓ **恰好等于 $2\sqrt3$**" "\n"
        r"概率：区间 $[-\sqrt3,\sqrt3]$ 长 $2\sqrt3=3.4641$；"
        r"$[-\frac{\sqrt3}3,\frac{\sqrt3}3]$ 长 $\frac{2\sqrt3}3=1.1547$；" "\n"
        r"$P=\frac{1.1547}{3.4641}=\frac13$ ✓ **答案 C 正确**。" "\n"
        r"**干扰项**：D $(\frac{\sqrt3}3)$ 是 $|k|$ 的临界值本身、"
        r"B $(\frac{\sqrt3}2)$ 是 $\frac{\sqrt3}3$ 与 $\sqrt3$ 的混淆 —— "
        r"都是「没做最后的比值」的常见错法。"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-406'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-406-V3',
}

T406_V4 = {
    'type': '选择',
    'stem_text': (
        r"（$2016$ 新课标Ⅰ理）某公司的班车在 $7{:}30$、$8{:}00$、$8{:}30$ 发车，"
        r"小明在 $7{:}50$ 至 $8{:}30$ 之间到达发车站乘坐班车，且到达发车站的时刻是随机的，"
        r"则他等车时间不超过 $10$ 分钟的概率是（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac13$"), ('B', r"$\dfrac12$"),
        ('C', r"$\dfrac23$"), ('D', r"$\dfrac34$"),
    ],
    'answer': 'B',
    'analysis': (
        r"以分钟为尺度，等车时间 $\leqslant10$ 的到达区间为 "
        r"$[7{:}50,8{:}00]$ 与 $[8{:}20,8{:}30]$，共 $20$ 分钟，"
        r"占全部 $40$ 分钟的一半。"
    ),
    'solution': (
        r"**建时间轴**（以 $7{:}00$ 为 $0$，单位：分钟）：" "\n"
        r"发车时刻：$7{:}30\to30$、$8{:}00\to60$、$8{:}30\to90$；"
        r"到达时刻 $t\in[50,90]$，总长度 $40$．" "\n"
        r"**① $t\in[50,60]$**（$7{:}50\sim8{:}00$ 到达）：乘 $8{:}00$ 的车，" "\n"
        r"等车时间 $=60-t\in[0,10]$，**全部 $\leqslant10$** ✓ → 区间长 $10$．" "\n"
        r"**② $t\in[60,90]$**（$8{:}00\sim8{:}30$ 到达）：乘 $8{:}30$ 的车，" "\n"
        r"等车时间 $=90-t$；$\leqslant10\Rightarrow t\geqslant80$，"
        r"即 $t\in[80,90]$（$8{:}20\sim8{:}30$）→ 区间长 $10$．" "\n"
        r"**合计**：满足条件的区间长 $=10+10=20$．" "\n"
        r"**概率**：$P=\dfrac{20}{40}=\dfrac12$，选 B．"
    ),
    'review': (
        r"★ 还原版完整 ✓。由详解「由题意得图…由图得等车时间不超过 10 分钟的概率为 $\frac12$」"
        r"还原 —— 详解依赖配图，**上述分段计算是我补的**。" "\n"
        r"**独立验算**：" "\n"
        r"到达区间 $[7{:}50,8{:}30]$ 长 $40$ 分钟 ✓" "\n"
        r"① $7{:}50\sim8{:}00$ 到达：等 $8{:}00$ 车，等车 $0\sim10$ 分钟 → 全满足 ✓（$10$ 分钟）" "\n"
        r"② $8{:}00\sim8{:}30$ 到达：等 $8{:}30$ 车，等车 $\le10$ → $8{:}20$ 之后到 ✓（$10$ 分钟）" "\n"
        r"③ 边界检查：$8{:}00$ 整到 → 等 $30$ 分钟（乘 $8{:}30$ 车）✗ 不满足 ✓；"
        r"$8{:}20$ 到 → 等 $10$ 分钟 ✓ 满足（含等号）" "\n"
        r"$P=\frac{10+10}{40}=\frac{20}{40}=\frac12$ ✓ **答案 B 正确**。" "\n"
        r"**⭐ 关键**：$8{:}00$ 之后到达的人**只能等 $8{:}30$ 的车**，"
        r"不能直接接 $8{:}00$ 那班（已开走）—— 这是最容易搞错的地方。"
    ),
    'difficulty': 0.75,
    'topics': ['M-T-406'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-406-V4',
}

QS = [T406_E1, T406_V2, T406_V3, T406_V4]
