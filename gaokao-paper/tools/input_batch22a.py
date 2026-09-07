# -*- coding: utf-8 -*-
r"""第22批（上）：M-T-104 双线法：指数型（4题）

来源：2024高中数学热点题型归纳完整解析版.pdf 专题3 p73（PDF 页 72）

## 双线法（指数型）的核心

导数能分解成**两个因式相乘**：

$$f'(x)=\underbrace{(2x-1)}_{\text{第一线：定根}}\cdot\underbrace{(\mathrm e^{2x}+a)}_{\text{第二线：动根}}$$

- **第一线**：一次式，根固定（如 $x=\frac12$）
- **第二线**：含指数的式子，**可能有根也可能没有**（有渐近线！）
- 关键就是讨论「动根」与「定根」的**大小关系**，从而定出 $f'$ 的正负区间

## 本批最重要的一处推导（E1 第二问）

E1 的详解只给了第一问，**第二问由我独立推导**：

$$f(x)=(x-1)\mathrm e^{2x}+ax^{2}-ax=(x-1)\bigl(\mathrm e^{2x}+ax\bigr)$$

**$x=1$ 恒为零点**——这是破题眼。再令 $h(x)=\mathrm e^{2x}+ax$ 讨论零点个数，
并注意 $h(1)=0$（即 $a=-\mathrm e^{2}$）时 $x=1$ 与 $h$ 的零点**重合**，
此时 $f$ 反而只有 $2$ 个不同零点。答案 $\{-2\mathrm e,-\mathrm e^{2}\}\cup(0,+\infty)$
的三个部分恰好对应三种情形，推导见 E1 的 solution。
"""

T104_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=(x-1)\mathrm e^{2x}+ax^{2}-ax$．" "\n"
        r"（1）讨论函数 $f(x)$ 的单调性；" "\n"
        r"（2）若函数 $f(x)$ 有两个不同的零点，求 $a$ 的取值范围．"
    ),
    'opts': [],
    'answer': (
        r"（1）见解析；（2）$\{-2\mathrm e,\,-\mathrm e^{2}\}\cup(0,+\infty)$"
    ),
    'analysis': (
        r"$f'(x)=(2x-1)(\mathrm e^{2x}+a)$ 是双线结构，按 $a$ 分类讨论；"
        r"第二问的关键是把 $f$ 写成 $f(x)=(x-1)(\mathrm e^{2x}+ax)$，"
        r"看出 $x=1$ 恒为零点，再讨论 $h(x)=\mathrm e^{2x}+ax$ 的零点个数。"
    ),
    'solution': (
        r"**（1）求导与分解**：" "\n"
        r"$f'(x)=\mathrm e^{2x}+2(x-1)\mathrm e^{2x}+2ax-a"
        r"=(2x-1)\mathrm e^{2x}+a(2x-1)=(2x-1)\bigl(\mathrm e^{2x}+a\bigr)$．" "\n"
        r"① 当 $a\geqslant0$ 时，$\mathrm e^{2x}+a>0$ 恒成立，"
        r"故 $f'(x)>0\iff x>\dfrac12$，$f'(x)<0\iff x<\dfrac12$：" "\n"
        r"$f$ 的增区间为 $\left(\dfrac12,+\infty\right)$，减区间为 $\left(-\infty,\dfrac12\right)$．" "\n"
        r"② 当 $a<0$ 时，$\mathrm e^{2x}+a=0\iff x=\dfrac{\ln(-a)}{2}$（记为 $x_{0}$）．" "\n"
        r"（ⅰ）若 $x_{0}>\dfrac12$，即 $\ln(-a)>1$，$a<-\mathrm e$："
        r"$f$ 在 $\left(-\infty,\dfrac12\right)$ 与 $(x_{0},+\infty)$ 上递增，"
        r"在 $\left(\dfrac12,x_{0}\right)$ 上递减；" "\n"
        r"（ⅱ）若 $x_{0}=\dfrac12$，即 $a=-\mathrm e$："
        r"$f'(x)\geqslant0$ 恒成立，$f$ 在 $\mathbb R$ 上递增；" "\n"
        r"（ⅲ）若 $x_{0}<\dfrac12$，即 $-\mathrm e<a<0$："
        r"$f$ 在 $(-\infty,x_{0})$ 与 $\left(\dfrac12,+\infty\right)$ 上递增，"
        r"在 $\left(x_{0},\dfrac12\right)$ 上递减．" "\n"
        r"**（2）因式分解是破题眼**：" "\n"
        r"$f(x)=(x-1)\mathrm e^{2x}+ax(x-1)=(x-1)\bigl(\mathrm e^{2x}+ax\bigr)$，" "\n"
        r"故 **$x=1$ 恒为零点**．设 $h(x)=\mathrm e^{2x}+ax$，"
        r"则 $f$ 的零点由 $\{1\}$ 与 $h$ 的零点合并而成．" "\n"
        r"$h'(x)=2\mathrm e^{2x}+a$．" "\n"
        r"**情形一 $a>0$**：$h'(x)>0$ 恒成立，$h$ 严格递增；"
        r"又 $h(x)\to-\infty\ (x\to-\infty)$、$h(x)\to+\infty\ (x\to+\infty)$，"
        r"故 $h$ 恰有 $1$ 个零点 $x_{1}$，且 $h(0)=1>0$ 说明 $x_{1}<0\neq1$．"
        r"此时 $f$ 有 $2$ 个不同零点 ✓．" "\n"
        r"$a=0$ 时 $h=\mathrm e^{2x}>0$ 无零点，$f$ 只有 $1$ 个零点 ✗．" "\n"
        r"**情形二 $a<0$**：$h$ 在 $x^{*}=\dfrac12\ln\!\left(-\dfrac a2\right)$ 处取最小值" "\n"
        r"$h(x^{*})=-\dfrac a2+a\cdot\dfrac12\ln\!\left(-\dfrac a2\right)"
        r"=\dfrac a2\left[\ln\!\left(-\dfrac a2\right)-1\right]$．" "\n"
        r"因 $\dfrac a2<0$，故 $h(x^{*})<0\iff\ln\!\left(-\dfrac a2\right)>1"
        r"\iff-\dfrac a2>\mathrm e\iff a<-2\mathrm e$；" "\n"
        r"$h(x^{*})=0\iff a=-2\mathrm e$；$h(x^{*})>0\iff-2\mathrm e<a<0$．" "\n"
        r"（ⅰ）$a<-2\mathrm e$：$h$ 有 $2$ 个零点，$f$ 有 $3$ 个零点——"
        r"**除非其中一个零点恰为 $1$**．由 $h(1)=\mathrm e^{2}+a=0$ 得 $a=-\mathrm e^{2}$，"
        r"此时 $-\mathrm e^{2}\approx-7.389<-2\mathrm e\approx-5.437$ 确属本情形，"
        r"$x=1$ 与 $h$ 的零点重合，$f$ 只有 $2$ 个不同零点 ✓．" "\n"
        r"（ⅱ）$a=-2\mathrm e$：$h$ 在 $x^{*}=\dfrac12\ln\mathrm e=\dfrac12$ 处切于 $0$，"
        r"$f$ 的零点为 $1$ 与 $\dfrac12$，共 $2$ 个 ✓．" "\n"
        r"（ⅲ）$-2\mathrm e<a<0$：$h$ 无零点，$f$ 只有 $1$ 个零点 ✗．" "\n"
        r"综上，$a\in\{-2\mathrm e,\,-\mathrm e^{2}\}\cup(0,+\infty)$．"
    ),
    'review': (
        r"★ **详解只给了第一问，第二问由我独立推导**，推导结果与答案完全吻合。" "\n"
        r"★ 提取文本作「f(x) = (x - 1)e2x+ ax2- ax」，$\mathrm e^{2x}$ 的上标与 "
        r"$ax^2$ 的上标全丢；答案「{-2e，-e2} ∪(0,+∞)」里的 $\mathrm e^2$ 上标也丢了。"
        r"由详解「$f'(x)=\mathrm e^{2x}+2(x-1)\mathrm e^{2x}+2ax-a=(2x-1)(\mathrm e^{2x}+a)$」"
        r"与题设答案还原。" "\n"
        r"**第一问的完整性校验**：$f'(x)=(2x-1)(\mathrm e^{2x}+a)$ 独立求导验证 ✓"
        r"（$(x-1)\mathrm e^{2x}$ 的导数 $=(2x-1)\mathrm e^{2x}$，$ax^2-ax$ 的导数 $=a(2x-1)$）。" "\n"
        r"**第二问三部分的逐一验证**（这是全题最精妙处）：" "\n"
        r"1. $a>0$：$h$ 递增、$h(0)=1>0$ ⇒ 零点 $x_1<0$，与 $x=1$ 不重合 ⇒ $2$ 个 ✓" "\n"
        r"2. $a=-2\mathrm e$：$h$ 最小值取在 $x=\frac12$，$f$ 零点 $\{1,\frac12\}$ ⇒ $2$ 个 ✓" "\n"
        r"3. $a=-\mathrm e^2$：$h(1)=0$ 与 $(x-1)$ 因子重合，另一零点 $x_1\neq1$ ⇒ $2$ 个 ✓" "\n"
        r"**数值校验**：$a=1$：$h(x)=\mathrm e^{2x}+x$，$h(0)=1$，$h(-1)=\mathrm e^{-2}-1=-0.865<0$ "
        r"⇒ 零点在 $(-1,0)$ ✓，$f$ 零点 $\{\approx-0.7,\ 1\}$ 共 $2$ 个 ✓。"
        r"$a=-1$（属 $-2\mathrm e<a<0$）：$h(x)=\mathrm e^{2x}-x$ 恒 $>0$"
        r"（最小值在 $x=\frac12\ln\frac12=-0.347$，$h=0.5+0.347=0.847>0$）"
        r"⇒ $f$ 只有 $x=1$ 一个零点 ✗ ✓。"
    ),
    'difficulty': 0.95,
    'topics': ['M-T-104'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-104-E1',
}

T104_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=\dfrac12x^{2}-ax+\dfrac{x-a+1}{\mathrm e^{x}}$，其中 $a\in\mathbb R$．" "\n"
        r"（1）讨论 $f(x)$ 的单调性；" "\n"
        r"（2）若 $a\in(0,1)$，设 $g(x)=f(x)-f(0)$，"
        r"求证：函数 $g(x)$ 在区间 $(0,+\infty)$ 内有唯一的一个零点．"
    ),
    'opts': [],
    'answer': (
        r"（1）$a>0$ 时：$f$ 在 $(-\infty,0)$、$(a,+\infty)$ 上递增，在 $(0,a)$ 上递减；"
        r"$a=0$ 时：$f$ 在 $\mathbb R$ 上递增；"
        r"$a<0$ 时：$f$ 在 $(-\infty,a)$、$(0,+\infty)$ 上递增，在 $(a,0)$ 上递减。"
        r"（2）证明见解析"
    ),
    'analysis': (
        r"求导后分子恰好是 $(x-a)(\mathrm e^{x}-1)$，两个根 $x=0$ 与 $x=a$；"
        r"按 $a$ 与 $0$ 的大小关系分类。"
    ),
    'solution': (
        r"**（1）求导**：" "\n"
        r"$f'(x)=x-a+\dfrac{1\cdot\mathrm e^{x}-(x-a+1)\mathrm e^{x}}{\mathrm e^{2x}}"
        r"=x-a+\dfrac{a-x}{\mathrm e^{x}}=(x-a)\left(1-\dfrac1{\mathrm e^{x}}\right)"
        r"=\dfrac{(x-a)(\mathrm e^{x}-1)}{\mathrm e^{x}}$．" "\n"
        r"因 $\mathrm e^{x}>0$，故 $f'(x)$ 的符号由 $(x-a)(\mathrm e^{x}-1)$ 决定，"
        r"两个零点是 $x=0$ 与 $x=a$．" "\n"
        r"① $a>0$：$f'(x)>0\iff x<0$ 或 $x>a$；$f'(x)<0\iff0<x<a$．"
        r"$f$ 在 $(-\infty,0)$、$(a,+\infty)$ 上递增，在 $(0,a)$ 上递减；" "\n"
        r"② $a=0$：$f'(x)=\dfrac{x(\mathrm e^{x}-1)}{\mathrm e^{x}}$，"
        r"$x\neq0$ 时 $x$ 与 $\mathrm e^{x}-1$ 同号，故 $f'(x)>0$，$f$ 在 $\mathbb R$ 上递增；" "\n"
        r"③ $a<0$：$f'(x)>0\iff x<a$ 或 $x>0$；$f'(x)<0\iff a<x<0$．"
        r"$f$ 在 $(-\infty,a)$、$(0,+\infty)$ 上递增，在 $(a,0)$ 上递减．" "\n"
        r"**（2）证明**：$g(x)=f(x)-f(0)$，故 $g(0)=0$．" "\n"
        r"由（1），当 $a\in(0,1)$ 时 $g$ 与 $f$ 同单调性："
        r"在 $(0,a)$ 上递减、在 $(a,+\infty)$ 上递增．" "\n"
        r"于是 $g(a)<g(0)=0$，即 $g$ 在 $(0,a]$ 上恒负，$x=a$ 不是零点；"
        r"在 $[a,+\infty)$ 上 $g$ 严格递增，且 $x\to+\infty$ 时 "
        r"$f(x)\sim\dfrac12x^{2}\to+\infty$，故 $g(x)\to+\infty$，"
        r"由零点存在性定理，$g$ 在 $(a,+\infty)$ 内恰有 $1$ 个零点．" "\n"
        r"又 $x=0$ 不是区间 $(0,+\infty)$ 的内点，"
        r"故 $g$ 在 $(0,+\infty)$ 内有唯一零点，证毕．"
    ),
    'review': (
        r"★ 提取文本作「f (x)= x2- ax + / x - a + 1 / 2ex」，"
        r"$\frac12x^2$ 的分数线与 $\frac{x-a+1}{\mathrm e^x}$ 的分数线全丢，"
        r"分子分母被拆到不同行（「x - a + 1」与「2ex」分离）。"
        r"由详解「$f(x)=\frac12x^2-ax+\frac{x-a+1}{\mathrm e^x}$，"
        r"∴$f'(x)=(x-a)-\frac{1}{\mathrm e^x}=\frac{(x-a)(\mathrm e^x-1)}{\mathrm e^x}$，"
        r"令 $f'(x)=0$，得 $x=a$ 或 $x=0$」还原。" "\n"
        r"**⚠ 导数的中间式**：详解写 $f'(x)=(x-a)-\frac{1}{\mathrm e^x}$，"
        r"这与我算的 $(x-a)\left(1-\frac{1}{\mathrm e^x}\right)$ 不同——"
        r"**答案的单调区间完全一致**（两种写法零点都是 $x=a$ 与 $x=0$，"
        r"且 $f'(x)$ 的符号分布相同），故按与答案自洽的写法录入。" "\n"
        r"**结构校验**：$\frac{\mathrm d}{\mathrm dx}\frac{x-a+1}{\mathrm e^x}"
        r"=\frac{\mathrm e^x-(x-a+1)\mathrm e^x}{\mathrm e^{2x}}=\frac{a-x}{\mathrm e^x}$ ✓。"
        r"$a=0$ 时 $f'(x)=\frac{x(\mathrm e^x-1)}{\mathrm e^x}\geqslant0$ ✓（$x$ 与 $\mathrm e^x-1$ 同号）。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-104'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-104-V1',
}

T104_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=ax\mathrm e^{x}-(x+1)^{2}$（其中 $a\in\mathbb R$，"
        r"$\mathrm e$ 为自然对数的底数）．" "\n"
        r"（1）讨论函数 $f(x)$ 的单调性；" "\n"
        r"（2）当 $x>0$ 时，$f(x)>\ln x-x^{2}-x-3$，求 $a$ 的取值范围．"
    ),
    'opts': [],
    'answer': (
        r"（1）见解析；（2）$\left(\dfrac1{\mathrm e^{3}},+\infty\right)$"
    ),
    'analysis': (
        r"$f'(x)=(x+1)(a\mathrm e^{x}-2)$ 是双线结构："
        r"定根 $x=-1$，动根 $x=\ln\dfrac2a$（$a>0$ 时才有）；"
        r"按 $a\leqslant0$、$0<a<2\mathrm e$、$a=2\mathrm e$、$a>2\mathrm e$ 四类讨论。"
    ),
    'solution': (
        r"**（1）求导**：$f'(x)=a(x+1)\mathrm e^{x}-2(x+1)=(x+1)(a\mathrm e^{x}-2)$．" "\n"
        r"① $a\leqslant0$ 时 $a\mathrm e^{x}-2<0$ 恒成立："
        r"$x<-1$ 时 $f'(x)>0$，$x>-1$ 时 $f'(x)<0$；"
        r"$f$ 的增区间 $(-\infty,-1)$，减区间 $(-1,+\infty)$；" "\n"
        r"② $a>0$ 时，$f'(x)=0$ 的两根为 $x=-1$ 与 $x=\ln\dfrac2a$：" "\n"
        r"（ⅰ）$\ln\dfrac2a=-1$，即 $a=2\mathrm e$：两根重合，$f'(x)\geqslant0$，"
        r"$f$ 在 $\mathbb R$ 上递增；" "\n"
        r"（ⅱ）$\ln\dfrac2a<-1$，即 $a>2\mathrm e$："
        r"$f$ 的增区间 $\left(-\infty,\ln\dfrac2a\right)$、$(-1,+\infty)$，"
        r"减区间 $\left(\ln\dfrac2a,-1\right)$；" "\n"
        r"（ⅲ）$\ln\dfrac2a>-1$，即 $0<a<2\mathrm e$："
        r"$f$ 的增区间 $(-\infty,-1)$、$\left(\ln\dfrac2a,+\infty\right)$，"
        r"减区间 $\left(-1,\ln\dfrac2a\right)$．" "\n"
        r"**（2）参变分离**：$x>0$ 时" "\n"
        r"$ax\mathrm e^{x}-(x+1)^{2}>\ln x-x^{2}-x-3$" "\n"
        r"$\iff ax\mathrm e^{x}>\ln x-x^{2}-x-3+x^{2}+2x+1=\ln x+x-2$" "\n"
        r"$\iff a>\dfrac{\ln x+x-2}{x\mathrm e^{x}}$（因 $x\mathrm e^{x}>0$）．" "\n"
        r"设 $\varphi(x)=\dfrac{\ln x+x-2}{x\mathrm e^{x}}$（$x>0$），"
        r"需 $a>\varphi(x)$ 对一切 $x>0$ 成立，即 $a>\max\varphi$．" "\n"
        r"观察分子 $\ln x+x-2$ 在 $x=1$ 处 $=-1<0$、在 $x=\mathrm e^{?}$…"
        r"令分子为 $0$：$\ln x+x-2=0$．注意到 $x=1$ 时 $\ln1+1-2=-1$；"
        r"$x=\mathrm e$ 时 $1+\mathrm e-2>0$，故零点在 $(1,\mathrm e)$ 内；"
        r"而 $x\to0^{+}$ 时分子 $\to-\infty$、分母 $\to0^{+}$，需用导数求最大值．" "\n"
        r"$\varphi'(x)=\dfrac{\left(\frac1x+1\right)x\mathrm e^{x}-(\ln x+x-2)(x+1)\mathrm e^{x}}"
        r"{x^{2}\mathrm e^{2x}}"
        r"=\dfrac{(1+x)-(x+1)(\ln x+x-2)}{x^{2}\mathrm e^{x}}"
        r"=\dfrac{(x+1)(3-x-\ln x)}{x^{2}\mathrm e^{x}}$．" "\n"
        r"$x+1>0$、$x^{2}\mathrm e^{x}>0$，故符号由 $3-x-\ln x$ 决定；"
        r"该函数严格递减，零点即 $x+\ln x=3$ 的根 $x_{0}$．" "\n"
        r"$x_{0}$ 处取最大值，且由 $x_{0}+\ln x_{0}=3$ 可化 "
        r"$\varphi(x_{0})=\dfrac{\ln x_{0}+x_{0}-2}{x_{0}\mathrm e^{x_{0}}}"
        r"=\dfrac{3-2}{x_{0}\mathrm e^{x_{0}}}=\dfrac1{x_{0}\mathrm e^{x_{0}}}$；"
        r"又 $x_{0}\mathrm e^{x_{0}}=\mathrm e^{x_{0}+\ln x_{0}}=\mathrm e^{3}$，" "\n"
        r"故 $\max\varphi=\dfrac1{\mathrm e^{3}}$，得 $a>\dfrac1{\mathrm e^{3}}$，" "\n"
        r"即 $a\in\left(\dfrac1{\mathrm e^{3}},+\infty\right)$．"
    ),
    'review': (
        r"★ 提取文本作「f (x)= axex- (x + 1)2」，$ax\mathrm e^x$ 与 $(x+1)^2$ 的上标全丢；"
        r"答案「(1)(2) 1 ,+∞ / e3」是「(1) 答案见解析；(2) $(\frac{1}{\mathrm e^3},+\infty)$」。"
        r"由详解「$f'(x)=a(x+1)\mathrm e^x-2(x+1)=(x+1)(a\mathrm e^x-2)$，"
        r"分别讨论 $a\leqslant0$、$0<a<2\mathrm e$、$a=2\mathrm e$、$a>2\mathrm e$ 时…」"
        r"与【分析】原文还原。" "\n"
        r"**⚠ 第二问详解缺失**：原书只给了答案 $(\frac{1}{\mathrm e^3},+\infty)$，"
        r"**上面的分离参数推导由我补出**，结果与答案一致 ✓。" "\n"
        r"**推导自检**（关键一步）：$\varphi(x_0)=\frac{1}{x_0\mathrm e^{x_0}}$ 这步用了 "
        r"$x_0+\ln x_0=3$；再由 $x_0\mathrm e^{x_0}=\mathrm e^{x_0+\ln x_0}=\mathrm e^3$ ——"
        r"这一步很漂亮，说明最大值恰为 $\mathrm e^{-3}$，与答案的 $\frac{1}{\mathrm e^3}$ 精确吻合 ✓。" "\n"
        r"**数值校验**：$\mathrm e^3\approx20.086$，$x_0+\ln x_0=3$ 的解约 $x_0\approx2.208$"
        r"（$2.208+0.792=3.000$ ✓）。$\varphi(2.208)=\frac{0.792+2.208-2}{2.208\times9.099}"
        r"=\frac{1.000}{20.09}\approx0.0498$；$\frac{1}{\mathrm e^3}=\frac1{20.086}=0.0498$ ✓。"
    ),
    'difficulty': 0.95,
    'topics': ['M-T-104'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-104-V2',
}

T104_V3 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=(x-2)\mathrm e^{x}-\dfrac a2(x-1)^{2}$．" "\n"
        r"（1）讨论 $f(x)$ 的单调性；"
    ),
    'opts': [],
    'answer': (
        r"$a\leqslant0$ 时：$f$ 在 $(-\infty,1)$ 上递减，在 $(1,+\infty)$ 上递增；"
        r"$a=\mathrm e$ 时：$f$ 在 $\mathbb R$ 上递增；"
        r"$0<a<\mathrm e$ 时：$f$ 在 $(-\infty,\ln a)$、$(1,+\infty)$ 上递增，"
        r"在 $(\ln a,1)$ 上递减；"
        r"$a>\mathrm e$ 时：$f$ 在 $(-\infty,1)$、$(\ln a,+\infty)$ 上递增，"
        r"在 $(1,\ln a)$ 上递减．"
    ),
    'analysis': (
        r"$f'(x)=(x-1)(\mathrm e^{x}-a)$ 是双线结构：定根 $x=1$，"
        r"动根 $x=\ln a$（$a>0$ 时才有）；比较 $\ln a$ 与 $1$ 的大小即可。"
    ),
    'solution': (
        r"$f'(x)=\mathrm e^{x}+(x-2)\mathrm e^{x}-a(x-1)=(x-1)\mathrm e^{x}-a(x-1)"
        r"=(x-1)(\mathrm e^{x}-a)$．" "\n"
        r"① $a\leqslant0$ 时 $\mathrm e^{x}-a>0$ 恒成立："
        r"$x<1$ 时 $f'(x)<0$，$x>1$ 时 $f'(x)>0$；"
        r"$f$ 在 $(-\infty,1)$ 上递减，在 $(1,+\infty)$ 上递增；" "\n"
        r"② $a>0$ 时，$f'(x)=0$ 的两根为 $x=1$ 与 $x=\ln a$：" "\n"
        r"（ⅰ）$a=\mathrm e$：$\ln a=1$，两根重合，$f'(x)\geqslant0$，$f$ 在 $\mathbb R$ 上递增；" "\n"
        r"（ⅱ）$0<a<\mathrm e$：$\ln a<1$，$f$ 在 $(-\infty,\ln a)$、$(1,+\infty)$ 上递增，"
        r"在 $(\ln a,1)$ 上递减；" "\n"
        r"（ⅲ）$a>\mathrm e$：$\ln a>1$，$f$ 在 $(-\infty,1)$、$(\ln a,+\infty)$ 上递增，"
        r"在 $(1,\ln a)$ 上递减．"
    ),
    'review': (
        r"★ **题干的 $a$ 位置破碎**：提取文本作"
        r"「f(x) = (x - 2) ⋅ex- (x - 1)2,g(x) = m(x + lnx) - / 2 / 2ex」，"
        r"$(x-1)^2$ 的上标丢失，且分数线旁散落着「a」与「m」两个字母——"
        r"后者属于**另一道未收录的 $g(x)$**，是排版串页。" "\n"
        r"**判定 $a$ 归属的依据**：详解通篇用 $f'(x)=(x-1)(\mathrm e^x-a)$，"
        r"并按 $a\leqslant0$、$a=\mathrm e$、$0<a<\mathrm e$、$a>\mathrm e$ 讨论，"
        r"与题干 $f(x)=(x-2)\mathrm e^x-\frac a2(x-1)^2$ 求导结果"
        r"（$=(x-1)(\mathrm e^x-a)$）**完全吻合** ✓，"
        r"故 $a$ 在 $f$ 中、$m$ 属于别题，据此还原。" "\n"
        r"**结构校验**：$\frac{\mathrm d}{\mathrm dx}\left[-\frac a2(x-1)^2\right]=-a(x-1)$ ✓，"
        r"$\frac{\mathrm d}{\mathrm dx}\left[(x-2)\mathrm e^x\right]=(x-1)\mathrm e^x$ ✓，"
        r"合起来 $(x-1)(\mathrm e^x-a)$ ✓。" "\n"
        r"**⚠ 本题只录第一问**：原书第二问含 $F(x)=f(x)-g(x)$ 与极值点 $x_0$，"
        r"但 $g(x)$ 的表达式（含 $m$）无法确定，故只录第一问，"
        r"并在 stem 中只保留第（1）问。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-104'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-104-V3',
}

QS = [T104_E1, T104_V1, T104_V2, T104_V3]
