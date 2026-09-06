# -*- coding: utf-8 -*-
r"""第14批（下）：T044 奇偶性单调性综合 / T045 三角函数比较，共 8 题。

来源：2024高中数学热点题型归纳完整解析版.pdf 专题2-1 p16~p17（PDF 页 15~16）

## T044 的统一套路

「去 $f$ 外衣」：把 $a,b,c$ 都写成同一个辅助函数 $g$ 的函数值，
再用 $g$ 的奇偶性 + 单调性比大小。

- 已知 $f$ 奇、$g(x)=xf(x)$ → $g$ 偶；$g$ 在 $(-\infty,0)$ 减 → 在 $(0,+\infty)$ 增
- 已知 $f(x)+xf'(x)<0$（$x<0$）→ 即 $g'(x)<0$，同一套
- 已知 $f(x)=f(2-x)$ → 关于 $x=1$ 对称，$f(-1)=f(3)$

## T045 的统一套路

化到同一个单调区间：$y=\sin x$ 在 $\left[0,\dfrac{\pi}{2}\right]$ 上递增。

- $\cos t=\sin\left(\dfrac{\pi}{2}-t\right)$（化余弦为正弦）
- $\sin t=\sin(\pi-t)$（化钝角到锐角）

## T044-V1 的函数形式是怎么定下来的

原文「f (x)= x -3 - x 」破碎，四个候选里只有 $f(x)=x-3^{-x}$
能同时满足「在给定区间递增」与答案 A，见该题 review。

LaTeX 一律 raw 双引号 r"..."；中文行文用弯引号“”，不用 ASCII 双引号。
"""

T044_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知 $f(x)$ 为 $\mathbb R$ 上的奇函数，$g(x)=xf(x)$，"
        r"若 $g(x)$ 在区间 $(-\infty,0)$ 上单调递减．"
        r"若 $a=g(2\pi)$，$b=g\!\left(2\sqrt3\right)$，$c=g(1)$，"
        r"则 $a,b,c$ 的大小关系为（　　）"
    ),
    'opts': [
        ('A', r"$a<b<c$"), ('B', r"$c<b<a$"),
        ('C', r"$b<a<c$"), ('D', r"$b<c<a$"),
    ],
    'answer': 'B',
    'analysis': (
        r"由 $f$ 奇得 $g$ 偶；偶函数在对称区间上单调性相反，"
        r"故 $g$ 在 $(0,+\infty)$ 上递增，只需比较自变量大小。"
    ),
    'solution': (
        r"因 $f(x)$ 为奇函数，有 $f(-x)=-f(x)$，于是" "\n"
        r"$g(-x)=(-x)f(-x)=(-x)\bigl[-f(x)\bigr]=xf(x)=g(x)$，"
        r"故 $g(x)$ 为偶函数．" "\n"
        r"又 $g(x)$ 在 $(-\infty,0)$ 上单调递减，"
        r"由偶函数的对称性知 $g(x)$ 在 $(0,+\infty)$ 上单调递增．" "\n"
        r"由 $2\pi\approx6.283>2\sqrt3\approx3.464>1$，得" "\n"
        r"$g(2\pi)>g\!\left(2\sqrt3\right)>g(1)$，即 $a>b>c$，亦即 $c<b<a$．" "\n"
        r"故选 B．"
    ),
    'review': (
        r"★ 提取文本作「b = g (2 3)」，$2\sqrt3$ 的根号丢失，"
        r"易误读成 $g(23)$ 或 $g(2^3)$。"
        r"由详解「又 $2\pi>2\sqrt3>1$」确认为 $2\sqrt3$。"
        r"数值校验：$2\pi\approx6.2832$、$2\sqrt3\approx3.4641$、$1$，"
        r"顺序与答案 B 一致。"
        r"**关键陷阱**：偶函数在 $(-\infty,0)$ 递减则在 $(0,+\infty)$ 递增"
        r"（单调性相反），若照搬「递减」会得出完全相反的结论。"
    ),
    'difficulty': 0.6,
    'topics': ['M-T-044'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-044-E1',
}

T044_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知函数 $f(x)=x-3^{-x}$，若 $a=f\!\left(3^{0.2}\right)$，"
        r"$b=f\!\left(0.2^{3}\right)$，$c=f\!\left(\log_{0.2}3\right)$，"
        r"则 $a,b,c$ 的大小关系是（　　）"
    ),
    'opts': [
        ('A', r"$a>b>c$"), ('B', r"$b>a>c$"),
        ('C', r"$c>a>b$"), ('D', r"$c>b>a$"),
    ],
    'answer': 'A',
    'analysis': (
        r"先判定 $f$ 在 $\mathbb R$ 上单调递增，再用指数、对数函数的单调性"
        r"比较三个自变量 $3^{0.2}$、$0.2^{3}$、$\log_{0.2}3$ 的大小。"
    ),
    'solution': (
        r"$f'(x)=1+3^{-x}\ln3>0$ 恒成立，故 $f(x)$ 在 $\mathbb R$ 上单调递增．" "\n"
        r"比较自变量：" "\n"
        r"由 $3^{1}>3^{0.2}>3^{0}=1$，得 $3^{0.2}>1$；" "\n"
        r"由 $0<0.2^{3}<0.2^{0}=1$，得 $0<0.2^{3}<1$；" "\n"
        r"由底数 $0.2\in(0,1)$，对数函数递减，且 $3>1$，"
        r"得 $\log_{0.2}3<\log_{0.2}1=0$．" "\n"
        r"故 $3^{0.2}>0.2^{3}>\log_{0.2}3$．" "\n"
        r"由 $f$ 递增，得 $f\!\left(3^{0.2}\right)>f\!\left(0.2^{3}\right)"
        r">f\!\left(\log_{0.2}3\right)$，即 $a>b>c$．" "\n"
        r"故选 A．"
    ),
    'review': (
        r"★ **函数形式系反推确定，需留意。**"
        r"提取文本作「f (x)= x -3 - x 」，分数/指数全部塌成平文本，"
        r"仅凭文本无法确定 $f$ 究竟是什么。" "\n"
        r"详解给出两条线索：①「函数在 $(-\infty,3]$ 上单调递增」；"
        r"②答案 A（$a>b>c$）。对四个候选逐一数值验证"
        r"（自变量 $3^{0.2}\approx1.24573$、$0.2^{3}=0.008$、"
        r"$\log_{0.2}3\approx-0.68261$）：" "\n"
        r"| 候选 | $a$ | $b$ | $c$ | 顺序 |" "\n"
        r"|---|---|---|---|---|" "\n"
        r"| $x-3^{-x}$ | $0.9913$ | $-0.9832$ | $-2.7994$ | **$a>b>c$ ✓** |" "\n"
        r"| $x^{3}-x$ | $0.6875$ | $-0.0080$ | $0.3645$ | $a>c>b$ ✗ |" "\n"
        r"| $3^{x}-x$ | $2.6840$ | $1.0008$ | $1.1550$ | $a>c>b$ ✗ |" "\n"
        r"| $x^{-3}-x$ | $-0.7284$ | $1.95\times10^{6}$ | $-2.4614$ | $b>a>c$ ✗ |" "\n"
        r"**只有 $f(x)=x-3^{-x}$ 同时满足递增性与答案 A**，据此录入。"
        r"该函数 $f'(x)=1+3^{-x}\ln3>0$ 确实全程递增，与详解描述吻合。"
    ),
    'difficulty': 0.65,
    'topics': ['M-T-044'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-044-V1',
}

T044_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知函数 $f(x)$ 满足 $f(x)+f(-x)=0$，且当 $x\in(-\infty,0)$ 时，"
        r"$f(x)+xf'(x)<0$ 成立，若 $a=2^{0.6}\cdot f\!\left(2^{0.6}\right)$，"
        r"$b=(\ln2)\cdot f(\ln2)$，$c=\left(\log_{\frac12}8\right)\cdot f\!\left(\log_{\frac12}8\right)$，"
        r"则 $a,b,c$ 的大小关系是（　　）"
    ),
    'opts': [
        ('A', r"$a>b>c$"), ('B', r"$c>b>a$"),
        ('C', r"$a>c>b$"), ('D', r"$c>a>b$"),
    ],
    'answer': 'D',
    'analysis': (
        r"构造 $g(x)=x\cdot f(x)$：由 $f$ 奇得 $g$ 偶；"
        r"由 $g'(x)=f(x)+xf'(x)<0$（$x<0$）得 $g$ 在 $(0,+\infty)$ 上递增。"
    ),
    'solution': (
        r"由 $f(x)+f(-x)=0$ 且 $f$ 在 $\mathbb R$ 上连续，知 $f$ 为奇函数．" "\n"
        r"令 $g(x)=x\cdot f(x)$，则" "\n"
        r"$g(-x)=(-x)\cdot f(-x)=(-x)\cdot\bigl[-f(x)\bigr]=x\cdot f(x)=g(x)$，"
        r"故 $g(x)$ 为偶函数．" "\n"
        r"又 $g'(x)=f(x)+x\cdot f'(x)$，由已知当 $x\in(-\infty,0)$ 时 $g'(x)<0$，"
        r"故 $g(x)$ 在 $(-\infty,0)$ 上单调递减；" "\n"
        r"由 $g$ 连续且为偶函数，得 $g(x)$ 在 $(0,+\infty)$ 上单调递增．" "\n"
        r"于是 $a=g\!\left(2^{0.6}\right)$，$b=g(\ln2)$，"
        r"$c=g\!\left(\log_{\frac12}8\right)=g(-3)=g(3)$（偶函数）．" "\n"
        r"由 $2^{0.6}\approx1.516>1$、$0<\ln2\approx0.693<1$、"
        r"$-\log_{\frac12}8=\log_{2}8=3$，得 $3>2^{0.6}>\ln2>0$．" "\n"
        r"由 $g$ 在 $(0,+\infty)$ 上递增，得 $g(3)>g\!\left(2^{0.6}\right)>g(\ln2)$，"
        r"即 $c>a>b$．" "\n"
        r"故选 D．"
    ),
    'review': (
        r"★ 提取文本作「a = (20.6)⋅f (20.6)，b = (ln2) ⋅f(ln2)，c = (log)⋅f (log)」，"
        r"$2^{0.6}$ 的指数与 $\log_{\frac12}8$ 的底数、真数全丢，"
        r"第三个式子整个塌成「(log)⋅f (log)」。"
        r"由详解「$c=g(\log_{\frac12}8)=g(-\log_2 8)=g(-3)$」"
        r"与「$\ln2<1<2^{0.6}<-\log_{\frac12}8=3$」还原。"
        r"数值校验：自变量 $|{-3}|=3>2^{0.6}\approx1.51572>\ln2\approx0.69315$，"
        r"与答案 D 一致。"
        r"**关键**：$c$ 的自变量是负数，必须先由偶函数化为 $g(3)$ 再比较。"
    ),
    'difficulty': 0.75,
    'topics': ['M-T-044'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-044-V2',
}

T044_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知 $f(x)=f(2-x)$，$x\in\mathbb R$，当 $x\in[1,+\infty)$ 时，"
        r"$f(x)$ 为增函数．设 $a=f(1)$，$b=f(2)$，$c=f(-1)$，"
        r"则 $a,b,c$ 的大小关系是（　　）"
    ),
    'opts': [
        ('A', r"$a>b>c$"), ('B', r"$b>a>c$"),
        ('C', r"$c>a>b$"), ('D', r"$c>b>a$"),
    ],
    'answer': 'D',
    'analysis': (
        r"由 $f(x)=f(2-x)$ 知 $f$ 关于直线 $x=1$ 对称，"
        r"于是 $f(-1)=f(3)$，再用 $[1,+\infty)$ 上的单调性比较。"
    ),
    'solution': (
        r"由 $f(x)=f(2-x)$，令 $x=-1$ 得 $f(-1)=f\bigl(2-(-1)\bigr)=f(3)$，"
        r"即 $c=f(3)$．" "\n"
        r"（一般地，$f(x)=f(2-x)$ 表明 $f$ 的图象关于直线 "
        r"$x=\dfrac{x+(2-x)}{2}=1$ 对称．）" "\n"
        r"因 $1<2<3$，且 $f(x)$ 在 $[1,+\infty)$ 上为增函数，得" "\n"
        r"$f(3)>f(2)>f(1)$，即 $c>b>a$．" "\n"
        r"故选 D．"
    ),
    'review': (
        r"★ 提取文本作「f x  = f 2 - x  ，x ∈1,+∞  时，f x  为增函数」，"
        r"函数记号的括号、区间端点全部丢失，"
        r"与「$f(x)=f(2)-x$」或「$f(x)=f(2-x)$」无法区分。"
        r"由详解「∵$f(x)=f(2-x)$，∴$f(-1)=f(3)$」确认为 $f(2-x)$。"
        r"数值关系：$1<2<3$ 且 $f$ 在 $[1,+\infty)$ 递增，"
        r"故 $f(3)>f(2)>f(1)$，与答案 D 一致。"
    ),
    'difficulty': 0.55,
    'topics': ['M-T-044'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-044-V3',
}

T045_E1 = {
    'type': '选择',
    'stem_text': (
        r"三个数 $\cos\dfrac32$，$\sin\dfrac{1}{10}$，$\sin\dfrac74$ 的大小关系是（　　）"
    ),
    'opts': [
        ('A', r"$\cos\dfrac32>\sin\dfrac{1}{10}>\sin\dfrac74$"),
        ('B', r"$\cos\dfrac32>\sin\dfrac74>\sin\dfrac{1}{10}$"),
        ('C', r"$\cos\dfrac32<\sin\dfrac{1}{10}<\sin\dfrac74$"),
        ('D', r"$\sin\dfrac74>\cos\dfrac32>\sin\dfrac{1}{10}$"),
    ],
    'answer': 'C',
    'analysis': (
        r"用诱导公式化为同名函数：$\cos\dfrac32=\sin\left(\dfrac{\pi}{2}-\dfrac32\right)$、"
        r"$\sin\dfrac74=\sin\left(\pi-\dfrac74\right)$，再在 $\left[0,\dfrac{\pi}{2}\right]$ 上比角。"
    ),
    'solution': (
        r"化为正弦：$\cos\dfrac32=\sin\left(\dfrac{\pi}{2}-\dfrac32\right)$，"
        r"$\sin\dfrac74=\sin\left(\pi-\dfrac74\right)$．" "\n"
        r"估算三个角：" "\n"
        r"$\dfrac{\pi}{2}-\dfrac32\approx1.5708-1.5=0.0708$，"
        r"$\dfrac{1}{10}=0.1$，"
        r"$\pi-\dfrac74\approx3.1416-1.75=1.3916$．" "\n"
        r"由 $0<0.0708<0.1<1.3916<\dfrac{\pi}{2}$，"
        r"且 $y=\sin x$ 在 $\left[0,\dfrac{\pi}{2}\right]$ 上单调递增，得" "\n"
        r"$\sin\left(\dfrac{\pi}{2}-\dfrac32\right)<\sin\dfrac{1}{10}<\sin\left(\pi-\dfrac74\right)$，"
        r"即 $\cos\dfrac32<\sin\dfrac{1}{10}<\sin\dfrac74$．" "\n"
        r"故选 C．"
    ),
    'review': (
        r"★ 提取文本作「三个数cos 3 2 ，sin 1 10 ，sin 7 4 的大小关系」，"
        r"三个分数全部塌成「3 2」「1 10」「7 4」，"
        r"与 $\frac32$、$\frac{1}{10}$、$\frac74$ 无法区分。"
        r"由详解「$\cos\frac32=\sin(\frac{\pi}{2}-\frac32)$，"
        r"$\sin\frac74=\sin(\pi-\frac74)$」「$\frac{\pi}{2}-\frac32\approx0.071$、"
        r"$\frac{1}{10}=0.1$、$\pi-\frac74\approx1.39$」还原。"
        r"数值校验：$\cos1.5\approx0.070737$、$\sin0.1\approx0.099833$、"
        r"$\sin1.75\approx0.983986$，与答案 C 吻合。"
    ),
    'difficulty': 0.6,
    'topics': ['M-T-045'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-045-E1',
}

T045_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知 $a=\sin\dfrac45$，$b=\dfrac43\sin\dfrac34$，$c=\dfrac43\cos\dfrac34$，"
        r"则 $a,b,c$ 的大小关系为（　　）"
    ),
    'opts': [
        ('A', r"$a<b<c$"), ('B', r"$b<c<a$"),
        ('C', r"$a<c<b$"), ('D', r"$b<a<c$"),
    ],
    'answer': 'A',
    'analysis': (
        r"$b,c$ 由 $\sin\dfrac34<\cos\dfrac34$ 直接比出；$a,b$ 需构造 "
        r"$f(x)=\dfrac{\sin x}{x}$，用其在 $\left[\dfrac34,1\right]$ 上递减来比。"
    ),
    'solution': (
        r"先比 $b,c$：由 $\dfrac34<\dfrac{\pi}{4}$，且 $y=\sin x$ 在 "
        r"$\left(0,\dfrac{\pi}{2}\right)$ 上递增、$y=\cos x$ 递减，得" "\n"
        r"$\sin\dfrac34<\sin\dfrac{\pi}{4}=\cos\dfrac{\pi}{4}<\cos\dfrac34$，"
        r"故 $b=\dfrac43\sin\dfrac34<\dfrac43\cos\dfrac34=c$．" "\n"
        r"再比 $a,b$：令 $f(x)=\dfrac{\sin x}{x}$，"
        r"则 $f'(x)=\dfrac{x\cos x-\sin x}{x^{2}}$．" "\n"
        r"当 $x\in\left(0,\dfrac{\pi}{2}\right)$ 时 $\tan x>x$，即 $\sin x>x\cos x$，"
        r"故 $f'(x)<0$，$f$ 在 $\left(0,\dfrac{\pi}{2}\right)$ 上递减．" "\n"
        r"由 $\dfrac34<\dfrac45$ 得 $f\!\left(\dfrac45\right)<f\!\left(\dfrac34\right)$，"
        r"即 $\dfrac{\sin\frac45}{\frac45}<\dfrac{\sin\frac34}{\frac34}$，" "\n"
        r"亦即 $\dfrac54\sin\dfrac45<\dfrac43\sin\dfrac34=b$，"
        r"于是 $a=\sin\dfrac45<\dfrac45\,b<b$．" "\n"
        r"综上 $a<b<c$，故选 A．"
    ),
    'review': (
        r"★ 提取文本作「a = sin 4 5 ,b = 4 3 sin 3 4 ,c = 4 3 cos 3 4 」，"
        r"三个分数与系数全部塌成平文本。"
        r"由详解「$\frac12=\sin\frac{\pi}{6}<\sin\frac34<\sin\frac{\pi}{4}"
        r"=\cos\frac{\pi}{4}<\cos\frac34$，所以 $b<c$」"
        r"与「构造 $f(x)=\frac{1}{x}\cdot\sin x$，$f$ 在 $[\frac34,1]$ 递减，"
        r"$f(\frac45)<f(\frac34)$」还原。"
        r"数值校验：$a=\sin0.8\approx0.71736$、$b\approx0.90885$、"
        r"$c\approx0.97559$，与答案 A 吻合。"
    ),
    'difficulty': 0.7,
    'topics': ['M-T-045'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-045-V1',
}

T045_V2 = {
    'type': '选择',
    'stem_text': (
        r"设 $x,y\in(0,\pi)$，若 $\sin(\sin x)=\cos(\cos y)$，"
        r"则 $\cos(\sin x)$ 与 $\sin(\cos y)$ 的大小关系为（　　）"
    ),
    'opts': [
        ('A', r"$\cos(\sin x)=\sin(\cos y)$"),
        ('B', r"$\cos(\sin x)>\sin(\cos y)$"),
        ('C', r"$\cos(\sin x)<\sin(\cos y)$"),
        ('D', r"以上均不对"),
    ],
    'answer': 'D',
    'analysis': (
        r"设 $\alpha=\sin x$、$\beta=\cos y$，由条件得 $\sin\alpha=\cos\beta"
        r"=\sin\left(\dfrac{\pi}{2}-\beta\right)$，据此分两类讨论 $\alpha$ 与 $\beta$ 的关系。"
    ),
    'solution': (
        r"设 $\alpha=\sin x$，$\beta=\cos y$．因 $x,y\in(0,\pi)$，"
        r"故 $\alpha\in(0,1]$，$\beta\in(-1,1)$．" "\n"
        r"由 $\sin(\sin x)=\cos(\cos y)$ 得 $\sin\alpha=\cos\beta"
        r"=\sin\left(\dfrac{\pi}{2}-\beta\right)$，"
        r"而 $\dfrac{\pi}{2}-\beta\in\left(\dfrac{\pi}{2}-1,\dfrac{\pi}{2}+1\right)$．" "\n"
        r"故 $\alpha=\dfrac{\pi}{2}-\beta$ 或 "
        r"$\alpha=\pi-\left(\dfrac{\pi}{2}-\beta\right)=\dfrac{\pi}{2}+\beta$．" "\n"
        r"**情形一**　$\alpha=\dfrac{\pi}{2}-\beta$：" "\n"
        r"$\cos(\sin x)=\cos\alpha=\cos\left(\dfrac{\pi}{2}-\beta\right)=\sin\beta"
        r"=\sin(\cos y)$，两者相等．" "\n"
        r"**情形二**　$\alpha=\dfrac{\pi}{2}+\beta$：" "\n"
        r"$\cos(\sin x)=\cos\alpha=\cos\left(\dfrac{\pi}{2}+\beta\right)=-\sin\beta$，"
        r"而 $\sin(\cos y)=\sin\beta$，于是" "\n"
        r"① $\beta\in(-1,0)$ 时，$-\sin\beta>\sin\beta$，故 $\cos(\sin x)>\sin(\cos y)$；" "\n"
        r"② $\beta=0$ 时，$-\sin\beta=\sin\beta=0$，故 $\cos(\sin x)=\sin(\cos y)$；" "\n"
        r"③ $\beta\in(0,1)$ 时，$-\sin\beta<\sin\beta$，故 $\cos(\sin x)<\sin(\cos y)$．" "\n"
        r"三种结果都可能出现，故大小关系不确定，选 D．"
    ),
    'review': (
        r"★ 提取文本作「sin sinx  = cos cosy  ，则cos sinx  与 sin cosy  的大小关系」，"
        r"函数记号的括号全部丢失，与 $\sin x\cdot\sin$ 之类的乘积形式无法区分。"
        r"由详解「设 $\alpha=\sin x$，$\beta=\cos y$，"
        r"$\sin\alpha=\cos\beta=\sin(\frac{\pi}{2}-\beta)$」确认为复合函数。"
        r"详解明确列出三种情形（$>$、$=$、$<$ 均可能），故选 D。"
        r"**这题的考点是分类讨论的完备性** —— 只解出 $\alpha=\frac{\pi}{2}-\beta$ "
        r"而漏掉 $\alpha=\frac{\pi}{2}+\beta$，就会错选 A。"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-045'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-045-V2',
}

T045_V3 = {
    'type': '选择',
    'stem_text': (
        r"$\sin3$，$\cos(\sin2)$，$\tan(\cos3)$ 的大小关系是（　　）"
    ),
    'opts': [
        ('A', r"$\cos(\sin2)>\sin3>\tan(\cos3)$"),
        ('B', r"$\cos(\sin2)>\tan(\cos3)>\sin3$"),
        ('C', r"$\sin3>\cos(\sin2)>\tan(\cos3)$"),
        ('D', r"$\tan(\cos3)>\sin3>\cos(\sin2)$"),
    ],
    'answer': 'A',
    'analysis': (
        r"先判符号得 $\tan(\cos3)<0$；再把 $\sin3=\sin(\pi-3)$、"
        r"$\cos(\sin2)=\sin\left(\dfrac{\pi}{2}-\sin2\right)$ 化同名后比角。"
    ),
    'solution': (
        r"先判 $\tan(\cos3)$ 的符号：由 $\dfrac{\pi}{2}<3<\pi$ 得 "
        r"$-1<\cos3<0$，故 $\tan(\cos3)<0$．" "\n"
        r"再化同名：由 $\dfrac{\pi}{2}<2<\dfrac{3\pi}{4}$ 得 "
        r"$\dfrac{\sqrt2}{2}<\sin2<1$，于是" "\n"
        r"$\cos(\sin2)=\sin\left(\dfrac{\pi}{2}-\sin2\right)$，"
        r"$\sin3=\sin(\pi-3)$．" "\n"
        r"比较三个角：" "\n"
        r"$\pi-3\approx0.1416$，$\dfrac{\pi}{2}-\sin2\approx1.5708-0.9093=0.6615$，"
        r"且 $\dfrac{\pi}{2}-1\approx0.5708$．" "\n"
        r"由 $0<\pi-3<\dfrac{\pi}{2}-1<\dfrac{\pi}{2}-\sin2<\dfrac{\pi}{2}$，"
        r"且 $y=\sin x$ 在 $\left[0,\dfrac{\pi}{2}\right]$ 上递增，得" "\n"
        r"$\sin(\pi-3)<\sin\left(\dfrac{\pi}{2}-\sin2\right)$，"
        r"即 $\sin3<\cos(\sin2)$．" "\n"
        r"又 $\sin3=\sin(\pi-3)>0>\tan(\cos3)$，故" "\n"
        r"$\tan(\cos3)<0<\sin3<\cos(\sin2)$，即 $\cos(\sin2)>\sin3>\tan(\cos3)$．" "\n"
        r"故选 A．"
    ),
    'review': (
        r"★ 提取文本作「sin3，cos sin2  ，tan cos3  的大小关系」，"
        r"复合函数的括号丢失。"
        r"由详解「$\frac{\pi}{2}<3<\pi$，$-1<\cos3<0$，$\tan(\cos3)<0$」"
        r"「$\cos(\sin2)=\sin(\frac{\pi}{2}-\sin2)$，$\sin3=\sin(\pi-3)$」"
        r"与「$0<\frac{\pi}{2}-3<\frac{\pi}{2}-1<\frac{\pi}{2}-\sin2<\frac{\pi}{2}$」还原。"
        r"数值校验：$\cos(\sin2)\approx0.614300$、$\sin3\approx0.141120$、"
        r"$\tan(\cos3)\approx-1.523652$，与答案 A 吻合。"
        r"**关键**：$\tan(\cos3)$ 的自变量 $\cos3\in(-1,0)$ 是负数，"
        r"这直接决定了它是三个数里唯一的负值、必定最小。"
    ),
    'difficulty': 0.7,
    'topics': ['M-T-045'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-045-V3',
}

QS = [
    T044_E1, T044_V1, T044_V2, T044_V3,
    T045_E1, T045_V1, T045_V2, T045_V3,
]
