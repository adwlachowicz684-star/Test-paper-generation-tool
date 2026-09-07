# -*- coding: utf-8 -*-
r"""第25批（下）：M-T-116 利用sinx与f(x)构造型（2题：V2、V3）
                + M-T-117 利用cosx与f(x)构造型（2题：E1、V1）

来源：2024高中数学热点题型归纳完整解析版.pdf 专题4 p082~p084（PDF 页 82~83）

## 构造函数速查（本专题核心）

| 已知条件 | 构造 |
|---|---|
| $\sin x\,f'(x)+\cos x\,f(x)\gtrless0$ | $g(x)=f(x)\sin x$ |
| $\sin x\,f'(x)-\cos x\,f(x)\gtrless0$ | $g(x)=\dfrac{f(x)}{\sin x}$ |
| $\cos x\,f'(x)-\sin x\,f(x)\gtrless0$ | $g(x)=f(x)\cos x$ |
| $\cos x\,f'(x)+\sin x\,f(x)\gtrless0$ | $g(x)=\dfrac{f(x)}{\cos x}$ |

## 本批跳过（如实标注）

- **M-T-116-E1**（【题型五】例1）：选项 A 提取为「$f(\frac\pi2)>2f(\frac\pi6)$」，
  但题干定义域是 $(0,\frac\pi2)$，$f(\frac\pi2)$ 无定义；
  而详解又列举了 $g(\frac\pi6)<g(\frac\pi2)\Rightarrow2f(\frac\pi6)<f(\frac\pi2)$，
  与单选答案 C 冲突。选项形式无法可靠判定，**跳过**。
- **M-T-116-V1**（第 12 题）：四个选项大量含 $\sqrt2,\sqrt3$，
  根号是矢量绘制、提取时丢失，选项 D 的系数组合无法唯一确定，**跳过**。
"""

T116_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知偶函数 $f(x)$ 是定义在 $[-1,1]$ 上的可导函数，"
        r"当 $x\in[-1,0)$ 时，$f'(x)\cos x+f(x)\sin x>0$；"
        r"若 $\cos(a+1)\,f(a)\geqslant f(a+1)\cos a$，"
        r"则实数 $a$ 的取值范围为（　　）"
    ),
    'opts': [
        ('A', r"$[-2,-1]$"),
        ('B', r"$\left[-1,-\dfrac12\right]$"),
        ('C', r"$\left[-\dfrac12,0\right]$"),
        ('D', r"$\left[-\dfrac12,+\infty\right)$"),
    ],
    'answer': 'C',
    'analysis': (
        r"构造 $F(x)=\dfrac{f(x)}{\cos x}$，它是偶函数；"
        r"由条件知 $F$ 在 $[-1,0)$ 上递增、在 $(0,1]$ 上递减；"
        r"再把不等式化成 $F(|a|)\geqslant F(|a+1|)$ 求解。"
    ),
    'solution': (
        r"**构造**：令 $F(x)=\dfrac{f(x)}{\cos x}$（$x\in[-1,1]$，此处 $\cos x>0$）．" "\n"
        r"$F(-x)=\dfrac{f(-x)}{\cos(-x)}=\dfrac{f(x)}{\cos x}=F(x)$（$f$ 为偶函数），"
        r"故 **$F$ 是偶函数**．" "\n"
        r"**单调性**：$F'(x)=\dfrac{f'(x)\cos x+f(x)\sin x}{\cos^{2}x}$；"
        r"由已知，$x\in[-1,0)$ 时 $F'(x)>0$，故 $F$ 在 $[-1,0)$ 上**递增**，"
        r"由偶性在 $(0,1]$ 上**递减**．" "\n"
        r"**化不等式**：$\cos(a+1)>0$、$\cos a>0$（因 $a,a+1\in[-1,1]$），"
        r"故由 $\cos(a+1)f(a)\geqslant f(a+1)\cos a$ 得" "\n"
        r"$\dfrac{f(a)}{\cos a}\geqslant\dfrac{f(a+1)}{\cos(a+1)}$，即 $F(a)\geqslant F(a+1)$，" "\n"
        r"由偶性即 $F(|a|)\geqslant F(|a+1|)$．" "\n"
        r"$F$ 在 $[0,1]$ 上递减，故 $|a|\leqslant|a+1|$．又需 $a,a+1\in[-1,1]$：" "\n"
        r"$\begin{cases}|a|\leqslant|a+1|\\ -1\leqslanta\leqslant1\\ "
        r"-1\leqslanta+1\leqslant1\end{cases}$"
        r"$\Rightarrow\begin{cases}a\geqslant-\dfrac12\\ -1\leqslanta\leqslant1\\ "
        r"-2\leqslanta\leqslant0\end{cases}\Rightarrow-\dfrac12\leqslanta\leqslant0$．" "\n"
        r"故选 C．"
    ),
    'review': (
        r"★ 提取文本作「当x ∈[-1,0)时，f′(x)cosx + f(x)sinx > 0，"
        r"若cos(a + 1)f(a) ≥f(a + 1)cosa」，题干完整；"
        r"选项「A. [-2,-1]B. -1,- / 2 / C. - ,0D. - ,+∞( / 22」的分数线丢失，"
        r"按 $-\frac12$ 还原。"
        r"由详解「令 $F(x)=\frac{f(x)}{\cos x}$，则 $F(-x)=F(x)$，"
        r"所以函数 $F(x)$ 是定义在 $[-1,1]$ 上的偶函数；"
        r"当 $x\in[-1,0)$ 时，$F'(x)=\frac{f'(x)\cos x+f(x)\sin x}{\cos^2x}>0$，"
        r"所以 $F(x)$ 在 $[-1,0)$ 上单调递增，在 $(0,1]$ 上单调递减；"
        r"由 $\cos(a+1)f(a)\geqslant f(a+1)\cos a$ 可得 $\frac{f(a)}{\cos a}\geqslant\frac{f(a+1)}{\cos(a+1)}$，"
        r"即 $F(a)\geqslant F(a+1)$，所以 $F(|a|)\geqslant F(|a+1|)$，"
        r"所以 $|a|\leqslant|a+1|$、$-1\leqslanta\leqslant1$、$-1\leqslanta+1\leqslant1$，"
        r"解得 $-\frac12\leqslanta\leqslant0$，故选 C」还原。" "\n"
        r"**数值校验**：$|a|\leqslant|a+1|$ 平方得 $a^2\leqslant a^2+2a+1$ ⇒ $a\geqslant-\frac12$ ✓。"
        r"$a\in[-1,1]\cap[-2,0]=[-1,0]$ ✓。三者交集 $[-\frac12,0]$ ✓。" "\n"
        r"**边界**：$a=-\frac12$ 时 $|a|=0.5=|a+1|$ ⇒ $F(|a|)=F(|a+1|)$ ✓ 取等（$\geqslant$）✓；"
        r"$a=0$：$|0|=0<|1|=1$ ✓ 且 $a+1=1\in[-1,1]$ ✓。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-116'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-116-V2',
}

T116_V3 = {
    'type': '选择',
    'stem_text': (
        r"设 $f(x)$ 是定义在 $\left(-\dfrac\pi2,0\right)\cup\left(0,\dfrac\pi2\right)$ 上的奇函数，"
        r"其导函数为 $f'(x)$．当 $x\in\left(0,\dfrac\pi2\right)$ 时，"
        r"$f'(x)-\dfrac{f(x)\cos x}{\sin x}<0$，"
        r"则不等式 $f(x)<\dfrac{2\sqrt3}{3}f\!\left(\dfrac\pi3\right)\sin x$ 的解集为（　　）"
    ),
    'opts': [
        ('A', r"$\left(-\dfrac\pi3,0\right)\cup\left(0,\dfrac\pi3\right)$"),
        ('B', r"$\left(-\dfrac\pi3,0\right)\cup\left(\dfrac\pi3,\dfrac\pi2\right)$"),
        ('C', r"$\left(-\dfrac\pi2,-\dfrac\pi3\right)\cup\left(\dfrac\pi3,\dfrac\pi2\right)$"),
        ('D', r"$\left(-\dfrac\pi2,-\dfrac\pi3\right)\cup\left(0,\dfrac\pi3\right)$"),
    ],
    'answer': 'B',
    'analysis': (
        r"构造 $h(x)=\dfrac{f(x)}{\sin x}$（偶函数），在 $(0,\frac\pi2)$ 上递减、"
        r"在 $(-\frac\pi2,0)$ 上递增；注意 $\sin x$ 在 $x<0$ 时为负，"
        r"两边同除要**变号**，这是本题最容易错的地方。"
    ),
    'solution': (
        r"**构造**：令 $h(x)=\dfrac{f(x)}{\sin x}$．"
        r"由 $f$ 为奇函数、$\sin x$ 为奇函数，知 **$h$ 为偶函数**．" "\n"
        r"**单调性**：$h'(x)=\dfrac{f'(x)\sin x-f(x)\cos x}{\sin^{2}x}$；" "\n"
        r"$x\in\left(0,\dfrac\pi2\right)$ 时 $\sin x>0$，由 $f'(x)-\dfrac{f(x)\cos x}{\sin x}<0$ "
        r"得 $f'(x)\sin x-f(x)\cos x<0$，故 $h'(x)<0$，"
        r"$h$ 在 $\left(0,\dfrac\pi2\right)$ 上**递减**；由偶性在 $\left(-\dfrac\pi2,0\right)$ 上**递增**．" "\n"
        r"**右半边 $x\in(0,\frac\pi2)$**：$\sin x>0$，原不等式化为" "\n"
        r"$\dfrac{f(x)}{\sin x}<\dfrac{2\sqrt3}{3}f\!\left(\dfrac\pi3\right)"
        r"=\dfrac{f(\frac\pi3)}{\sin\frac\pi3}=h\!\left(\dfrac\pi3\right)$，即 $h(x)<h\!\left(\dfrac\pi3\right)$．" "\n"
        r"$h$ 在 $(0,\frac\pi2)$ 上递减，故 $x>\dfrac\pi3$，得 $x\in\left(\dfrac\pi3,\dfrac\pi2\right)$．" "\n"
        r"**左半边 $x\in(-\frac\pi2,0)$**：$\sin x<0$，两边同除 $\sin x$ **变号**：" "\n"
        r"$\dfrac{f(x)}{\sin x}>\dfrac{2\sqrt3}{3}f\!\left(\dfrac\pi3\right)=h\!\left(\dfrac\pi3\right)=h\!\left(-\dfrac\pi3\right)$，"
        r"即 $h(x)>h\!\left(-\dfrac\pi3\right)$．" "\n"
        r"$h$ 在 $(-\frac\pi2,0)$ 上递增，故 $x>-\dfrac\pi3$，得 $x\in\left(-\dfrac\pi3,0\right)$．" "\n"
        r"综上解集为 $\left(-\dfrac\pi3,0\right)\cup\left(\dfrac\pi3,\dfrac\pi2\right)$，选 B．"
    ),
    'review': (
        r"★ 提取文本作「当x ∈(0,)时，f′(x)- f (x) < 0 / 2 sinx / cosx」与"
        r"「f (x)<f()sinx / 33 / 2 3 π」，"
        r"$f'(x)-\frac{f(x)\cos x}{\sin x}$ 的分数线丢失（分子「f(x)cosx」与分母「sinx」分离），"
        r"$\frac{2\sqrt3}{3}$ 被拆成「2 3」+「3」两处（根号丢失）。"
        r"由详解「当 $x\in(0,\frac\pi2)$ 时，$\sin x>0$，由 $f'(x)-f(x)\frac{\cos x}{\sin x}<0$，"
        r"得 $f'(x)\sin x-f(x)\cos x<0$，"
        r"∴$h'(x)=\frac{f'(x)\sin x-f(x)\cos x}{\sin^2x}<0$；"
        r"将 $f(x)<\frac{2\sqrt3}{3}f(\frac\pi3)\sin x$ 化为 $\frac{f(x)}{\sin x}<\frac{f(\frac\pi3)}{\sin\frac\pi3}$，"
        r"即 $h(x)<h(\frac\pi3)$，则 $\frac\pi3<x<\frac\pi2$；"
        r"当 $x\in(-\frac\pi2,0)$ 时，$\sin x<0$，化为 $\frac{f(x)}{\sin x}>\frac{f(\frac\pi3)}{\sin\frac\pi3}$，"
        r"即 $h(x)>h(\frac\pi3)=h(-\frac\pi3)$，则 $-\frac\pi3<x<0$；"
        r"综上，所求不等式的解集为 $(-\frac\pi3,0)\cup(\frac\pi3,\frac\pi2)$」还原。" "\n"
        r"**系数校验**（关键）：$h(\frac\pi3)=\frac{f(\frac\pi3)}{\sin\frac\pi3}"
        r"=\frac{f(\frac\pi3)}{\sqrt3/2}=\frac{2}{\sqrt3}f(\frac\pi3)=\frac{2\sqrt3}{3}f(\frac\pi3)$ ✓ "
        r"**与详解完全吻合**，反证题干系数的还原无误。" "\n"
        r"**⚠ 本题最易错点**：$x<0$ 时 $\sin x<0$，不等式两边同除负数要变号。"
        r"若不注意会得到 C 或 D。已在 solution 中显式标注。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-116'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-116-V3',
}

T117_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知函数 $f(x)$ 的定义域为 $\left(-\dfrac\pi2,\dfrac\pi2\right)$，"
        r"其导函数是 $f'(x)$，有 $f'(x)\cos x+f(x)\sin x<0$，"
        r"则关于 $x$ 的不等式 $\sqrt3\,f(x)<2f\!\left(\dfrac\pi6\right)\cos x$ 的解集为（　　）"
    ),
    'opts': [
        ('A', r"$\left(\dfrac\pi3,\dfrac\pi2\right)$"),
        ('B', r"$\left(\dfrac\pi6,\dfrac\pi2\right)$"),
        ('C', r"$\left(-\dfrac\pi6,-\dfrac\pi3\right)$"),
        ('D', r"$\left(-\dfrac\pi3,-\dfrac\pi6\right)$"),
    ],
    'answer': 'B',
    'analysis': (
        r"构造 $F(x)=\dfrac{f(x)}{\cos x}$，由条件知 $F'(x)<0$，即 $F$ 递减；"
        r"再把不等式化为 $F(x)<F\!\left(\dfrac\pi6\right)$ 即可。"
    ),
    'solution': (
        r"**构造**：令 $F(x)=\dfrac{f(x)}{\cos x}$．"
        r"在 $\left(-\dfrac\pi2,\dfrac\pi2\right)$ 上 $\cos x>0$，故 $F$ 有定义，" "\n"
        r"$F'(x)=\dfrac{f'(x)\cos x+f(x)\sin x}{\cos^{2}x}<0$，"
        r"故 $F$ 在 $\left(-\dfrac\pi2,\dfrac\pi2\right)$ 上**单调递减**．" "\n"
        r"**化不等式**：由 $\cos x>0$，$\sqrt3\,f(x)<2f\!\left(\dfrac\pi6\right)\cos x$ 化为" "\n"
        r"$\dfrac{f(x)}{\cos x}<\dfrac{2}{\sqrt3}f\!\left(\dfrac\pi6\right)"
        r"=\dfrac{f(\frac\pi6)}{\cos\frac\pi6}$（因 $\cos\dfrac\pi6=\dfrac{\sqrt3}2$），" "\n"
        r"即 $F(x)<F\!\left(\dfrac\pi6\right)$．" "\n"
        r"$F$ 递减，故 $x>\dfrac\pi6$；结合定义域得 $x\in\left(\dfrac\pi6,\dfrac\pi2\right)$．" "\n"
        r"故选 B．"
    ),
    'review': (
        r"★ 提取文本作「有f ′(x)cosx + f (x)sinx < 0 ，则关于x 的不等式3 f (x) < "
        r"2f()cosx」，$\sqrt3$ 的根号丢失（只剩「3」）、$f(\frac\pi6)$ 的参数丢失。"
        r"由详解「令 $F(x)=\frac{f(x)}{\cos x}$，则 $F'(x)=\frac{f'(x)\cos x+f(x)\sin x}{\cos^2x}<0$，"
        r"函数 $F(x)$ 是定义域 $(-\frac\pi2,\frac\pi2)$ 内的单调递减函数，由于 $\cos x>0$，"
        r"关于 $x$ 的不等式 $\sqrt3f(x)<2f(\frac\pi6)\cos x$ 可化为 "
        r"$\frac{f(x)}{\cos x}<\frac{f(\frac\pi6)}{\cos\frac\pi6}$，即 $F(x)<F(\frac\pi6)$，"
        r"所以 $-\frac\pi2<x<\frac\pi2$ 且 $x>\frac\pi6$，解得 $\frac\pi2>x>\frac\pi6$，"
        r"不等式 $\sqrt3f(x)<2f(\frac\pi6)\cos x$ 的解集为 $(\frac\pi6,\frac\pi2)$」还原。" "\n"
        r"**系数校验**：$\frac{2}{\sqrt3}f(\frac\pi6)=\frac{f(\frac\pi6)}{\sqrt3/2}"
        r"=\frac{f(\frac\pi6)}{\cos\frac\pi6}$ ✓ 与详解一致，"
        r"反证题干确为 $\sqrt3 f(x)<2f(\frac\pi6)\cos x$（其中 $\sqrt3$ 为矢量绘制的根号）。"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-117'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-117-E1',
}

T117_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知偶函数 $f(x)$ 的定义域为 $\left(-\dfrac\pi2,\dfrac\pi2\right)$，"
        r"其导函数为 $f'(x)$，当 $0<x<\dfrac\pi2$ 时，"
        r"有 $f'(x)\cos x+f(x)\sin x<0$ 成立，"
        r"则关于 $x$ 的不等式 $f(x)<\sqrt2\,f\!\left(\dfrac\pi4\right)\cos x$ 的解集为（　　）"
    ),
    'opts': [
        ('A', r"$\left(\dfrac\pi4,\dfrac\pi2\right)$"),
        ('B', r"$\left(-\dfrac\pi2,-\dfrac\pi4\right)\cup\left(\dfrac\pi4,\dfrac\pi2\right)$"),
        ('C', r"$\left(-\dfrac\pi4,0\right)\cup\left(0,\dfrac\pi4\right)$"),
        ('D', r"$\left(-\dfrac\pi4,0\right)\cup\left(\dfrac\pi4,\dfrac\pi2\right)$"),
    ],
    'answer': 'B',
    'analysis': (
        r"构造 $g(x)=\dfrac{f(x)}{\cos x}$，它是**偶函数**；"
        r"由条件 $g$ 在 $(0,\frac\pi2)$ 上递减，故 $g(x)<g(\frac\pi4)\iff|x|>\dfrac\pi4$。"
    ),
    'solution': (
        r"**构造**：令 $g(x)=\dfrac{f(x)}{\cos x}$．"
        r"由 $f$ 为偶函数、$\cos x$ 为偶函数，知 **$g$ 为偶函数**．" "\n"
        r"**单调性**：$g'(x)=\dfrac{f'(x)\cos x+f(x)\sin x}{\cos^{2}x}$；"
        r"由已知，当 $0<x<\dfrac\pi2$ 时 $g'(x)<0$，故 $g$ 在 $\left(0,\dfrac\pi2\right)$ 上**递减**"
        r"（由偶性，在 $\left(-\dfrac\pi2,0\right)$ 上递增）．" "\n"
        r"**化不等式**：$\cos x>0$，故 $f(x)<\sqrt2\,f\!\left(\dfrac\pi4\right)\cos x$ 化为" "\n"
        r"$\dfrac{f(x)}{\cos x}<\sqrt2\,f\!\left(\dfrac\pi4\right)"
        r"=\dfrac{f(\frac\pi4)}{\cos\frac\pi4}=g\!\left(\dfrac\pi4\right)$（因 $\cos\dfrac\pi4=\dfrac{\sqrt2}2$），" "\n"
        r"即 $g(x)<g\!\left(\dfrac\pi4\right)$．" "\n"
        r"由偶性 $g(x)=g(|x|)$，且 $g$ 在 $[0,\frac\pi2)$ 上递减，故" "\n"
        r"$g(|x|)<g\!\left(\dfrac\pi4\right)\iff|x|>\dfrac\pi4$；"
        r"结合定义域 $|x|<\dfrac\pi2$，" "\n"
        r"得 $x\in\left(-\dfrac\pi2,-\dfrac\pi4\right)\cup\left(\dfrac\pi4,\dfrac\pi2\right)$．" "\n"
        r"故选 B．"
    ),
    'review': (
        r"★ 提取文本作「当0 < x < 时，有f′(x)cosx + f(x)sinx < 0 成立，"
        r"则关于x 的不等式f(x) <2 f()⋅cosx」，$\sqrt2$ 的根号丢失（只剩「2」）、"
        r"$f(\frac\pi4)$ 的参数丢失。"
        r"由详解「设 $g(x)=\frac{f(x)}{\cos x}$，利用导数求得 $g(x)$ 在 $(0,\frac\pi2)$ 上单调递减，"
        r"$f(x)<\sqrt2f(\frac\pi4)\cos x$ ⇔ $g(x)<g(\frac\pi4)$」与答案 B 还原。" "\n"
        r"**系数校验**：$\sqrt2f(\frac\pi4)=\frac{f(\frac\pi4)}{\sqrt2/2}=\frac{f(\frac\pi4)}{\cos\frac\pi4}=g(\frac\pi4)$ ✓ "
        r"与详解一致，反证题干的 $\sqrt2$ 确为根号（而非系数 2）。" "\n"
        r"**对称性校验**：$f$ 偶 $\Rightarrow$ $g$ 偶 $\Rightarrow$ 解集关于原点对称。"
        r"四个选项中只有 **B** 和 **C** 对称；C 是 $|x|<\frac\pi4$（对应 $g(x)>g(\frac\pi4)$），"
        r"方向相反 ✗；B 是 $|x|>\frac\pi4$ ✓。**这一条就能锁定答案 B**，无需完整计算。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-117'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-117-V1',
}

QS = [T116_V2, T116_V3, T117_E1, T117_V1]
