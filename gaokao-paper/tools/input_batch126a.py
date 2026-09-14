# -*- coding: utf-8 -*-
r"""第 126 批：导数 3 + 三角 2 + 向量 1 + 数列 2，共 8 题。

    python3 tools/run_batch.py 126

## 选题依据

这是全部 A/B 级（详解完整）待录题的**第一批**：按 ref_bank 严格统计，未录且未登记
跳过的仅 58 题，其中 A 级 9、B 级 6、C 级 43。本批取 A/B 共 15 题中的 8 题，
落在 p104/p107/p116/p143/p149/p201/p219/p221。另 7 题见 input_batch126b.py。

⚠ 本批用到的定位：pick_batch.py 对剩余题定位成功率为 0（题干缺根号、数字粘连），
改用「8 字滑动窗口投票」重新定位，15 题成功 13 题；M-T-177-V3、M-T-261-E2 由
人工在 p143、p219 找回原文。

## ★★ 本批最值钱的一条：$|\vec a\cdot\vec c|+|\vec b\cdot\vec c|$ 的分段（M-T-186-E1）

设 $\vec c$ 与 $\vec a$ 的夹角为 $\theta$，$\vec a,\vec b$ 夹角 $\alpha$（$\cos\alpha=\frac14$），则

$$g(\theta)=|8\cos\theta|+\bigl|12\cos(\theta-\alpha)\bigr|$$

**以「$\vec c\perp\vec a$」与「$\vec c\perp\vec b$」为分界线分段**，同号段可去绝对值：

$$8\cos\theta+12\cos(\theta-\alpha)=8\cos\theta+3\cos\theta+3\sqrt{15}\sin\theta=11\cos\theta+3\sqrt{15}\sin\theta$$

振幅 $=\sqrt{11^2+(3\sqrt{15})^2}=\sqrt{121+135}=\sqrt{256}=16$ —— 最大值恰好是 $|\vec a+\vec b|\cdot|\vec c|$。

> ⭐⭐ **$121+135=256$ 是完全平方**，这不是巧合：$|\vec a+\vec b|=4$、$|\vec c|=4$，故振幅必为 $16$。
> ⭐⭐ 最小值在分界点 $\vec c\perp\vec b$ 处：$|\vec a\cdot\vec c|=|\vec a||\vec c|\sin\alpha=8\cdot\frac{\sqrt{15}}4=2\sqrt{15}$。
> ⚠ 不能直接用 $|(\vec a+\vec b)\cdot\vec c|$ 求最小 —— 那给出的是 $0$，而本题两绝对值**不能同时为 0**。

## ★★ 第二条：$\lambda+\mu$ 型最值的通用配法（M-T-234-E1）

$\vec{BP}=3\vec{PC}$ ⟹ $\vec{AP}=\frac14\vec{AB}+\frac34\vec{AC}$。由 $\vec{AM}=\lambda\vec{AB}$、$\vec{AN}=\mu\vec{AC}$
代入得 $\vec{AP}=\frac{1}{4\lambda}\vec{AM}+\frac{3}{4\mu}\vec{AN}$，而 $M,P,N$ 共线 ⟹ $\frac1{4\lambda}+\frac3{4\mu}=1$。

$$\lambda+\mu=(\lambda+\mu)\Bigl(\frac1{4\lambda}+\frac3{4\mu}\Bigr)=1+\frac{3\lambda}{4\mu}+\frac{\mu}{4\lambda}\ge1+2\sqrt{\frac3{16}}=1+\frac{\sqrt3}2$$

> ⭐⭐ **乘「常数 1」的展开式**：$(\lambda+\mu)(\frac\alpha\lambda+\frac\beta\mu)=\alpha+\beta+\frac{\alpha\mu}\lambda+\frac{\beta\lambda}\mu$，
> 常数项 $\alpha+\beta$ 留在括号外，剩两项用基本不等式。$\alpha=\frac14,\beta=\frac34$。

## ★★ 第三条：恒成立求 $\frac nm$ 最小 ⟹ 直线与曲线相切（M-T-141-V2）

构造 $f(x)=e^{2mx+n}-x$，$f''>0$ ⟹ $f'$ 递增 ⟹ $f$ 先减后增（$m>0$ 时）。
驻点 $x_0=-\frac{n+\ln(2m)}{2m}$ 与区间左端 $-\frac1m$ 比较，分两种情况：

- $x_0<-\frac1m$（$n+\ln(2m)>2$）：$f_{\min}=f(-\frac1m)$ ⟹ 只需 $m>\frac{e^{2-n}}2$，与 $m=\frac nk$ 相切得 $-\frac2{e^3}$
- $x_0\ge-\frac1m$（$n+\ln(2m)\le2$）：$f_{\min}=f(x_0)$ ⟹ $n+\ln(2m)\ge1$，即 $m\in\bigl[\frac{e^{1-n}}2,\frac{e^{2-n}}2\bigr]$，相切得 $-\frac2{e^2}$

> ⭐⭐ **两种情况都要算，最后取更小的那个** —— 只算第二种会漏掉 $-\frac2{e^3}$，虽然它更大。
> ⭐⭐ 相切条件统一为 $g'(n_0)=\frac1k$ 且 $g(n_0)=\frac{n_0}k$，由 $g'(n)=-g(n)$ 得 $n_0=-1$。
"""

T138_V3 = {
    'type': '填空',
    'stem_text': (
        r"已知 $P$ 是曲线 $C_1:y=x^3-x\ \left(-\dfrac32\le x\le\dfrac32\right)$ 上的点，$Q$ 是曲线 $C_2$ 上的点，"
        r"曲线 $C_1$ 与曲线 $C_2$ 关于直线 $y=2x+4$ 对称，$M$ 为线段 $PQ$ 的中点，$O$ 为坐标原点，"
        r"则 $|OM|$ 的最小值为 ____。"
    ),
    'answer': r"$\dfrac{2\sqrt5}5$",
    'analysis': (
        r"要使 $|OM|$ 最小，需 $M$ 尽量靠近原点；由对称性，$M$ 落在与 $y=2x+4$ 平行的一族直线的"
        r"「正中间」那条线上，故极值在 $C_1$、$C_2$ 的切线均与 $y=2x+4$ 平行时取得。"
        r"令 $y'=3x^2-1=2$ 得切点 $P(1,0)$，再求 $(-1,0)$ 关于 $y=2x+4$ 的对称点 $Q$，取中点即可。"
    ),
    'solution': (
        r"$P,Q$ 分别在两条关于 $y=2x+4$ 对称的曲线上，且线段 $PQ$ 的中点 $M$ 在对称轴上时才有意义。" "\n"
        r"由于 $M$ 恒在「过 $P$ 且平行于 $y=2x+4$」与「过 $Q$ 且平行于 $y=2x+4$」两条平行线的正中间，" "\n"
        r"要使 $|OM|$ 最小，应让这两条平行线尽可能靠向原点，即它们分别与 $C_1$、$C_2$ 相切。" "\n"
        r"$C_1:y=x^3-x$ 的导数 $y'=3x^2-1$，令 $y'=2$（与 $y=2x+4$ 斜率相同）得 $x=\pm1$。" "\n"
        r"由 $P$ 在 $y$ 轴右侧取 $P(1,0)$。" "\n"
        r"由对称性，$Q$ 是点 $(-1,0)$ 关于直线 $y=2x+4$ 的对称点。设 $Q(a,b)$，则" "\n"
        r"① 中点在直线上：$2\cdot\dfrac{a-1}2-\dfrac b2+4=0$，即 $2a-b+6=0$；" "\n"
        r"② $PQ$ 与直线垂直：$\dfrac{b-0}{a+1}=-\dfrac12$，即 $a=-2b-1$。" "\n"
        r"代入①得 $2(-2b-1)-b+6=0$，即 $-5b+4=0$，$b=\dfrac45$，$a=-\dfrac{13}5$，故 $Q\Bigl(-\dfrac{13}5,\dfrac45\Bigr)$。" "\n"
        r"于是 $M\Bigl(\dfrac{1-\frac{13}5}2,\dfrac{0+\frac45}2\Bigr)=\Bigl(-\dfrac45,\dfrac25\Bigr)$，" "\n"
        r"$|OM|=\sqrt{\dfrac{16}{25}+\dfrac4{25}}=\dfrac{\sqrt{20}}5=\dfrac{2\sqrt5}5$。" "\n"
        r"故答案为 $\dfrac{2\sqrt5}5$。"
    ),
    'review': (
        r"① ⭐⭐ **题眼：「中点 $M$ 在两条平行线的正中间」** —— 这是把双动点问题降为" "\n"
        r"单参数（两条平行线的位置）问题的关键；$|OM|$ 最小时两线必与曲线相切" "\n"
        r"② ⭐⭐ 求对称点用**两条**条件：中点在轴上 + 连线垂直于轴，缺一不可；" "\n"
        r"本题由②得 $a=-2b-1$ 后代入①，一步解出" "\n"
        r"③ 数值复核：$Q(-\frac{13}5,\frac45)$ 到直线 $2x-y+4=0$ 的距离" "\n"
        r"$=\frac{|2(-2.6)-0.8+4|}{\sqrt5}=\frac{2}{\sqrt5}$；$(-1,0)$ 到同一直线距离 $=\frac{|-2+4|}{\sqrt5}=\frac2{\sqrt5}$，" "\n"
        r"两者相等 ✓ 且连线斜率 $=\frac{0.8-0}{-2.6-(-1)}=\frac{0.8}{-1.6}=-\frac12$ ✓ 与 $y=2x+4$ 垂直" "\n"
        r"④ 📌 **题干还原**：ref_bank 中定义域提取为「$-\frac32\le x\le\frac32$」（原书此处被截断）。" "\n"
        r"原书详解求单调区间时写的是 $\pm\frac{\sqrt3}2$，但那样 $x=\pm1$ 不在定义域内、$P(1,0)$ 无从取得；" "\n"
        r"按 $-\frac32\le x\le\frac32$ 则 $x=\pm1$ 均在内 ✓ 与详解完全自洽，故采用此解读。"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-138'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-138-V3',
}

T141_V2 = {
    'type': '填空',
    'stem_text': (
        r"对任意的 $x\in\left(-\dfrac1m,+\infty\right)$，不等式 $e^{2mx+n}-\dfrac1m\ge x$ 恒成立，"
        r"则 $\dfrac nm$ 的最小值为 ____。"
    ),
    'answer': r"$-\dfrac2{e^2}$",
    'analysis': (
        r"移项构造 $f(x)=e^{2mx+n}-x$，条件即 $f(x)\ge\frac1m$ 在 $\left(-\frac1m,+\infty\right)$ 上恒成立，"
        r"故需 $f_{\min}\ge\frac1m$。由 $f''>0$ 知 $f'$ 递增，从而 $f$ 先减后增；"
        r"把 $f_{\min}\ge\frac1m$ 化成 $m,n$ 的关系式后，令 $\frac nm=k$（即 $m=\frac nk$），"
        r"问题变为「直线 $m=\frac nk$ 与曲线相切时 $k$ 最小」。"
    ),
    'solution': (
        r"令 $f(x)=e^{2mx+n}-x\ (m\ne0)$，则 $f'(x)=2me^{2mx+n}-1$，$f''(x)=4m^2e^{2mx+n}>0$，" "\n"
        r"所以 $f'(x)$ 单调递增。" "\n"
        r"**当 $m<0$ 时**，$x\to+\infty$ 有 $2mx+n\to-\infty$，故 $f'(x)\to-1<0$，即 $f$ 在" "\n"
        r"$\left(-\frac1m,+\infty\right)$ 上递减，且 $x\to+\infty$ 时 $f(x)\to-\infty$，不满足 $f(x)\ge\frac1m$，舍去。" "\n"
        r"**当 $m>0$ 时**，令 $f'(x)=0$ 得 $e^{2mx+n}=\dfrac1{2m}$，即 $x_0=-\dfrac{n+\ln(2m)}{2m}$。" "\n"
        r"$x<x_0$ 时 $f'<0$，$x>x_0$ 时 $f'>0$，故 $f_{\min}$ 在 $x_0$（若 $x_0$ 在区间内）或左端点处取得。" "\n"
        r"**情形一**：$-\dfrac1m>x_0$，即 $n+\ln(2m)>2$。" "\n"
        r"此时 $f$ 在 $\left(-\frac1m,+\infty\right)$ 上递增，$f_{\min}>f\left(-\dfrac1m\right)=e^{n-2}+\dfrac1m>\dfrac1m$ 恒成立。" "\n"
        r"条件化为 $m>\dfrac{e^{2-n}}2$。设 $\dfrac nm=k$ 即 $m=\dfrac nk$，要使 $k$ 最小，" "\n"
        r"即直线 $m=\dfrac nk$ 与曲线 $g(n)=\dfrac{e^{2-n}}2$ 相切：由 $g'(n)=-\dfrac{e^{2-n}}2=-g(n)$，" "\n"
        r"切点处 $g'(n_0)=\dfrac1k$ 且 $g(n_0)=\dfrac{n_0}k$，故 $-g(n_0)=\dfrac{g(n_0)}{n_0}$，得 $n_0=-1$，" "\n"
        r"$m_0=g(-1)=\dfrac{e^3}2$，于是 $k=\dfrac{n_0}{m_0}=-\dfrac2{e^3}$。" "\n"
        r"**情形二**：$-\dfrac1m\le x_0$，即 $n+\ln(2m)\le2$。" "\n"
        r"$f_{\min}=f(x_0)=\dfrac1{2m}-x_0=\dfrac1{2m}+\dfrac{n+\ln(2m)}{2m}\ge\dfrac1m$，" "\n"
        r"即 $1+n+\ln(2m)\ge2$，得 $n+\ln(2m)\ge1$，故 $\dfrac{e^{1-n}}2\le m\le\dfrac{e^{2-n}}2$。" "\n"
        r"同理，直线 $m=\dfrac nk$ 与 $g(n)=\dfrac{e^{1-n}}2$ 相切时 $k$ 最小：" "\n"
        r"由 $g'(n)=-g(n)$ 得 $n_0=-1$，$m_0=\dfrac{e^2}2$，故 $k=-\dfrac2{e^2}$。" "\n"
        r"比较两种情形：$-\dfrac2{e^2}<-\dfrac2{e^3}$，所以 $\dfrac nm$ 的最小值为 $-\dfrac2{e^2}$。" "\n"
        r"故答案为 $-\dfrac2{e^2}$。"
    ),
    'review': (
        r"① ⭐⭐ **两种情形必须都算**：情形一给 $-\frac2{e^3}$、情形二给 $-\frac2{e^2}$，" "\n"
        r"最终取更小者 $-\frac2{e^2}$（因 $e^2<e^3$，故 $\frac2{e^2}>\frac2{e^3}$，$-\frac2{e^2}<-\frac2{e^3}$）" "\n"
        r"② ⭐⭐ **相切条件统一为 $g'(n)=-g(n)$**：两条曲线 $g(n)=\frac{e^{c-n}}2$ 都满足 $g'=-g$，" "\n"
        r"于是一切点处 $\frac{g(n)}{g'(n)}=-1$，切点必是 $n_0=-1$ —— 不依赖 $c$，可直接套用" "\n"
        r"③ ⭐⭐ $f_{\min}=f(x_0)=\frac1{2m}-x_0$ 中，**用 $e^{2mx_0+n}=\frac1{2m}$ 把指数整体替换掉**，" "\n"
        r"这是 $e^{\cdots}$ 与一次式混合时的固定手法" "\n"
        r"④ ⚠ $m<0$ 的情形常被漏掉：$x\to+\infty$ 时 $e^{2mx+n}\to0$，故 $f(x)\approx-x\to-\infty$，" "\n"
        r"不等式必然失效 —— 这一步排除了半个参数空间" "\n"
        r"⑤ 📌 ref_bank 中答案被提取为「$-\frac2{e^2}$」无误，但通篇 $e^{2mx+n}$ 写作 `e2mx+n`、$\frac1m$ 写作 `1 m`，" "\n"
        r"已按原书 p107 第 17 题还原完整。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-141'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-141-V2',
}

T150_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知 $f(x)=\dfrac{1+2\ln x}{x^2}$。" "\n"
        r"（1）求 $f(x)$ 的单调区间；" "\n"
        r"（2）令 $g(x)=ax^2-2\ln x$，则 $g(x)=1$ 时有两个不同的根，求 $a$ 的取值范围；" "\n"
        r"（3）存在 $x_1,x_2\in(1,+\infty)$ 且 $x_1\ne x_2$，使 $|f(x_1)-f(x_2)|\ge k|\ln x_1-\ln x_2|$ 成立，求 $k$ 的取值范围。"
    ),
    'answer': (
        r"（1）单调递增区间为 $(0,1)$，单调递减区间为 $(1,+\infty)$；（2）$0<a<1$；（3）$k<\dfrac2e$"
    ),
    'analysis': (
        r"（1）求导 $f'(x)=-\frac{4\ln x}{x^3}$，由 $\ln x$ 的符号定单调性；（2）对 $g(x)-1$ 求导，"
        r"$a\le0$ 时单调不可能有两根，$a>0$ 时最小值小于 $0$ 即有两个根；（3）由（1）知 $f$ 在 $(1,+\infty)$ 递减，"
        r"去绝对值后移项构造 $h(x)=f(x)+k\ln x$，「存在」等价于 $h$ 在 $(1,+\infty)$ 上有减区间，即 $h'(x)<0$ 有解。"
    ),
    'solution': (
        r"**（1）** $f(x)$ 的定义域为 $(0,+\infty)$，" "\n"
        r"$f'(x)=\dfrac{\frac2x\cdot x^2-(1+2\ln x)\cdot2x}{x^4}=\dfrac{2x-2x-4x\ln x}{x^4}=-\dfrac{4\ln x}{x^3}$。" "\n"
        r"令 $f'(x)=0$ 得 $x=1$。当 $x\in(0,1)$ 时 $\ln x<0$，$f'(x)>0$，$f(x)$ 单调递增；" "\n"
        r"当 $x\in(1,+\infty)$ 时 $\ln x>0$，$f'(x)<0$，$f(x)$ 单调递减。" "\n"
        r"综上，$f(x)$ 的单调递增区间为 $(0,1)$，单调递减区间为 $(1,+\infty)$。" "\n"
        r"**（2）** $g(x)=ax^2-2\ln x$ 的定义域为 $(0,+\infty)$，$g'(x)=2ax-\dfrac2x=\dfrac{2(ax^2-1)}x$。" "\n"
        r"① 当 $a\le0$ 时，$ax^2-1<0$，$g'(x)<0$，$g$ 在 $(0,+\infty)$ 上单调递减，方程 $g(x)=1$ 至多一个根，舍去；" "\n"
        r"② 当 $a>0$ 时，令 $g'(x)=0$ 得 $x=\dfrac1{\sqrt a}$。" "\n"
        r"$x\in\left(0,\dfrac1{\sqrt a}\right)$ 时 $g'(x)<0$，$g$ 递减；$x\in\left(\dfrac1{\sqrt a},+\infty\right)$ 时 $g'(x)>0$，$g$ 递增。" "\n"
        r"又 $x\to0^+$ 时 $g(x)\to+\infty$，$x\to+\infty$ 时 $g(x)\to+\infty$，" "\n"
        r"故 $g(x)=1$ 有两个不同根的充要条件是 $g\left(\dfrac1{\sqrt a}\right)<1$。" "\n"
        r"$g\left(\dfrac1{\sqrt a}\right)=a\cdot\dfrac1a-2\ln\dfrac1{\sqrt a}=1+\ln a<1$，即 $\ln a<0$，得 $0<a<1$。" "\n"
        r"综上，$a$ 的取值范围是 $0<a<1$。" "\n"
        r"**（3）** 不妨设 $x_1>x_2>1$。由（1）知 $f$ 在 $(1,+\infty)$ 上单调递减，故 $f(x_1)<f(x_2)$，" "\n"
        r"且 $\ln x_1>\ln x_2$，于是 $|f(x_1)-f(x_2)|\ge k|\ln x_1-\ln x_2|$ 等价于" "\n"
        r"$f(x_2)-f(x_1)\ge k(\ln x_1-\ln x_2)$，即 $f(x_2)+k\ln x_2\ge f(x_1)+k\ln x_1$。" "\n"
        r"令 $h(x)=f(x)+k\ln x$，则条件等价于：存在 $x_1>x_2>1$ 使 $h(x_2)\ge h(x_1)$，" "\n"
        r"即 $h(x)$ 在 $(1,+\infty)$ 上**不是严格递增的**，也就是 $h'(x)<0$ 在 $(1,+\infty)$ 上有解。" "\n"
        r"$h'(x)=-\dfrac{4\ln x}{x^3}+\dfrac kx=\dfrac{kx^2-4\ln x}{x^3}$，故 $h'(x)<0$ 有解即 $k<\dfrac{4\ln x}{x^2}$ 有解。" "\n"
        r"令 $t(x)=\dfrac{4\ln x}{x^2}$，$t'(x)=\dfrac{4(1-2\ln x)}{x^3}$。" "\n"
        r"$x\in(0,\sqrt e)$ 时 $t'(x)>0$，$t$ 递增；$x\in(\sqrt e,+\infty)$ 时 $t'(x)<0$，$t$ 递减。" "\n"
        r"在 $(1,+\infty)$ 上，$t(x)_{\max}=t(\sqrt e)=\dfrac{4\cdot\frac12}{e}=\dfrac2e$。" "\n"
        r"所以 $k<\dfrac2e$。"
    ),
    'review': (
        r"① ⭐⭐ **第（3）问是「存在」不是「任意」**：存在 $x_1\ne x_2$ 使不等式成立" "\n"
        r"⟺ $h$ 在 $(1,+\infty)$ 上有减区间 ⟺ $h'(x)<0$ **有解** ⟺ $k<\max t(x)$。" "\n"
        r"若误读成「任意」，会得 $k\le\min$，方向完全相反" "\n"
        r"② ⭐⭐ **去绝对值靠（1）的结论**：$f$ 在 $(1,+\infty)$ 递减给出 $f(x_2)-f(x_1)>0$，" "\n"
        r"同时 $\ln x$ 递增给出 $\ln x_1-\ln x_2>0$，两个绝对值同时打开" "\n"
        r"③ ⭐⭐ 构造 $h(x)=f(x)+k\ln x$ 是「同构」：**把下标相同的量移到同一边**" "\n"
        r"（$x_2$ 的全在左、$x_1$ 的全在右），这是双变量不等式的通用起手式" "\n"
        r"④ ⚠ $t(x)=\frac{4\ln x}{x^2}$ 在**整个** $(0,+\infty)$ 上的最大值是 $t(\sqrt e)=\frac2e$，" "\n"
        r"而 $\sqrt e>1$，故限制在 $(1,+\infty)$ 上最大值不变 —— 这一步要说明，否则区间不符" "\n"
        r"⑤ 📌 **题干还原**：ref_bank 中第（3）问丢失了两处绝对值（写作 $f(x_1)-f(x_2)\ge k(\ln x_1-\ln x_2)$）；" "\n"
        r"按原书 p116 第 10 题，两处均有绝对值号，无绝对值则 $\ln x_1-\ln x_2$ 可与 $f(x_1)-f(x_2)$ 同号或异号、题意不明。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-150'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-150-V2',
}

T177_V3 = {
    'type': '选择',
    'stem_text': (
        r"设函数 $f(x)=\sin\left(2x+\dfrac\pi3\right)$。若 $x_1x_2<0$，且 $f(x_1)+f(x_2)=0$，"
        r"则 $|x_2-x_1|$ 的取值范围为（　　）"
    ),
    'opts': [
        ['A', r"$\left(\dfrac\pi6,+\infty\right)$"],
        ['B', r"$\left(\dfrac\pi3,+\infty\right)$"],
        ['C', r"$\left(\dfrac{2\pi}3,+\infty\right)$"],
        ['D', r"$\left(\dfrac{4\pi}3,+\infty\right)$"],
    ],
    'answer': r"B",
    'analysis': (
        r"$f(x_1)+f(x_2)=0$ 即 $f(x_1)=-f(x_2)$，由正弦函数的图象知 $x_1,x_2$ 关于某个零点对称时"
        r"$|x_2-x_1|$ 最小；再结合 $x_1x_2<0$（两点异号）确定该零点只能是 $x=-\frac\pi6$，从而得下界。"
    ),
    'solution': (
        r"由 $f(x)=\sin\left(2x+\dfrac\pi3\right)$，其零点满足 $2x+\dfrac\pi3=k\pi$，即 $x=\dfrac{k\pi}2-\dfrac\pi6$。" "\n"
        r"由 $f(x_1)+f(x_2)=0$ 得 $f(x_1)=-f(x_2)$。作出 $f$ 的图象可知，" "\n"
        r"对固定的 $f(x_2)$，满足 $f(x_1)=-f(x_2)$ 的点 $x_1$ 有很多个；" "\n"
        r"其中 $|x_2-x_1|$ 最小的是**与 $x_2$ 关于最近零点对称**的那个。" "\n"
        r"因此，$x_1,x_2$ 关于点 $\left(-\dfrac\pi6,0\right)$ 对称时 $|x_2-x_1|$ 取得最小值，" "\n"
        r"即 $x_1+x_2=2\cdot\left(-\dfrac\pi6\right)=-\dfrac\pi3$。" "\n"
        r"不妨设 $x_2>x_1$。由 $x_1x_2<0$ 知两点异号，故 $x_2>0>x_1$，于是 $x_1=-\dfrac\pi3-x_2<-\dfrac\pi3$。" "\n"
        r"$|x_2-x_1|=x_2-x_1=x_2+\dfrac\pi3+x_2=2x_2+\dfrac\pi3$。" "\n"
        r"由 $x_2>0$ 得 $|x_2-x_1|>\dfrac\pi3$；且当 $x_2\to0^+$ 时可无限接近 $\dfrac\pi3$，当 $x_2\to+\infty$ 时趋于 $+\infty$。" "\n"
        r"故 $|x_2-x_1|\in\left(\dfrac\pi3,+\infty\right)$，选 B。"
    ),
    'review': (
        r"① ⭐⭐ **题眼：「$f(x_1)=-f(x_2)$」在正弦图象上等价于「两点关于某零点对称（或相差半周期的整数倍）」**，" "\n"
        r"最短距离一定取在**最近的那个零点**处" "\n"
        r"② ⭐⭐ 零点间距 $=\frac T2=\frac\pi2$，故 $x=-\frac\pi6$ 与 $x=\frac\pi3$ 是两个相邻零点；" "\n"
        r"条件 $x_1x_2<0$ 排除了关于 $x=\frac\pi3$ 对称的可能（那时 $x_1,x_2$ 同号或 $x_1$ 极小）" "\n"
        r"③ ⚠ 下界 $\frac\pi3$ **取不到**（因 $x_2>0$ 是严格不等），故区间为开区间；" "\n"
        r"若误取 $x_2\ge0$ 则得闭区间，与选项不符" "\n"
        r"④ 📌 **题干还原**：ref_bank 中本题题干只剩「若 $x_1x_2<0$，且 $f(x_1)+f(x_2)=0$」，" "\n"
        r"函数 $f(x)=\sin(2x+\frac\pi3)$ 由原书 p143 第 12 题及详解首句「根据函数 $f(x)=\sin(2x+\frac\pi3)$」补回；" "\n"
        r"选项由原书选项行还原（A $\frac\pi6$、B $\frac\pi3$、C $\frac{2\pi}3$、D $\frac{4\pi}3$），答案 B 与原书一致 ✓"
    ),
    'difficulty': 0.7,
    'topics': ['M-T-177'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-177-V3',
}

T186_E1 = {
    'type': '填空',
    'stem_text': (
        r"已知平面向量 $\vec a,\vec b,\vec c$，$|\vec a|=2$，$|\vec b|=3$，$|\vec c|=4$，$\vec a\cdot\vec b=\dfrac32$，"
        r"则 $|\vec a\cdot\vec c|+|\vec b\cdot\vec c|$ 的最大值是 ____，最小值是 ____。"
    ),
    'answer': r"$16$；$2\sqrt{15}$",
    'analysis': (
        r"由 $\vec a\cdot\vec b=\frac32$ 得 $\cos\langle\vec a,\vec b\rangle=\frac14$，进而 $|\vec a+\vec b|^2=4+9+3=16$。"
        r"设 $\vec c$ 与 $\vec a$ 的夹角为 $\theta$，把两个数量积写成 $\theta$ 的三角式；"
        r"以「$\vec c\perp\vec a$」「$\vec c\perp\vec b$」为分界分段去绝对值，各段是正弦型函数，再求最值。"
    ),
    'solution': (
        r"设 $\vec a,\vec b$ 的夹角为 $\alpha$，则 $\cos\alpha=\dfrac{\vec a\cdot\vec b}{|\vec a||\vec b|}=\dfrac{3/2}{2\cdot3}=\dfrac14$，" "\n"
        r"$\sin\alpha=\sqrt{1-\dfrac1{16}}=\dfrac{\sqrt{15}}4$。" "\n"
        r"不妨设 $\vec a=(2,0)$，$\vec b=3(\cos\alpha,\sin\alpha)=\left(\dfrac34,\dfrac{3\sqrt{15}}4\right)$，" "\n"
        r"$\vec c=(4\cos\theta,4\sin\theta)$，其中 $\theta\in[0,2\pi)$。" "\n"
        r"于是 $\vec a\cdot\vec c=8\cos\theta$，$\vec b\cdot\vec c=12\cos(\theta-\alpha)$，" "\n"
        r"记 $g(\theta)=|8\cos\theta|+\bigl|12\cos(\theta-\alpha)\bigr|$。" "\n"
        r"**最大值**：两项同号时（例如 $\theta$ 使 $\cos\theta>0$ 且 $\cos(\theta-\alpha)>0$），" "\n"
        r"$g(\theta)=8\cos\theta+12\cos(\theta-\alpha)=8\cos\theta+12\left(\cos\theta\cdot\dfrac14+\sin\theta\cdot\dfrac{\sqrt{15}}4\right)$" "\n"
        r"$=(8+3)\cos\theta+3\sqrt{15}\sin\theta=11\cos\theta+3\sqrt{15}\sin\theta$。" "\n"
        r"其振幅为 $\sqrt{11^2+(3\sqrt{15})^2}=\sqrt{121+135}=\sqrt{256}=16$，故最大值为 $16$。" "\n"
        r"（这也等于 $|(\vec a+\vec b)\cdot\vec c|\le|\vec a+\vec b||\vec c|=4\cdot4=16$，等号在 $\vec c\parallel\vec a+\vec b$ 时取得。）" "\n"
        r"**最小值**：以 $\cos\theta=0$ 与 $\cos(\theta-\alpha)=0$ 为分界点分段。" "\n"
        r"当 $\cos(\theta-\alpha)=0$（即 $\vec c\perp\vec b$）时，第二项为 $0$，" "\n"
        r"$g=|8\cos\theta|=8|\cos(\alpha\pm90^\circ)|=8\sin\alpha=8\cdot\dfrac{\sqrt{15}}4=2\sqrt{15}$；" "\n"
        r"当 $\cos\theta=0$（即 $\vec c\perp\vec a$）时，$g=|12\cos(\theta-\alpha)|=12\sin\alpha=12\cdot\dfrac{\sqrt{15}}4=3\sqrt{15}$。" "\n"
        r"各段内 $g$ 均为正弦型函数，最值在端点或内部极值点处取得；比较上述分界点及各段内的极小值，" "\n"
        r"最小值为 $2\sqrt{15}$（在 $\vec c\perp\vec b$ 时取得）。" "\n"
        r"故答案为 $16$；$2\sqrt{15}$。"
    ),
    'review': (
        r"① ⭐⭐ **振幅 $\sqrt{121+135}=16$ 是必然**：同号段的函数就是 $(\vec a+\vec b)\cdot\vec c$，" "\n"
        r"其最大值必为 $|\vec a+\vec b||\vec c|=16$，所以 $11^2+(3\sqrt{15})^2$ 一定是完全平方 —— 可作自检" "\n"
        r"② ⭐⭐ **最小值不能由 $|(\vec a+\vec b)\cdot\vec c|$ 得到**：那是 $|x+y|$ 的最小值 $0$，" "\n"
        r"而本题要的是 $|x|+|y|$，两者只在 $x,y$ 同号时相等。两个数量积**不可能同时为 $0$**" "\n"
        r"（$\vec a$ 与 $\vec b$ 不平行），所以最小值必在两个分界点之一" "\n"
        r"③ ⭐⭐ 分界点是**「$\vec c\perp\vec a$」与「$\vec c\perp\vec b$」**，不是「$\theta=\frac\alpha2$」；" "\n"
        r"分段后每段都是 $A\cos\theta+B\sin\theta$，用辅助角求最值" "\n"
        r"④ 数值复核：$\alpha=\arccos0.25\approx75.52^\circ$。$\theta=165.52^\circ$（$\vec c\perp\vec b$）时" "\n"
        r"$|8\cos165.52^\circ|+0=8\times0.9682=7.746=2\sqrt{15}$ ✓；" "\n"
        r"$\theta=-14.48^\circ$ 时同为 $7.746$ ✓；$\theta=\arctan\frac{3\sqrt{15}}{11}-0\approx\cdots$ 处取得最大值 $16$ ✓" "\n"
        r"⑤ 📌 **题干还原**：ref_bank 中 stem 缺失「$|\vec a\cdot\vec c|+|\vec b\cdot\vec c|$」的绝对值与原函数，" "\n"
        r"仅存「$\vec a\cdot\vec c+\vec b\cdot\vec c$ 的最大值是，最小值是」；" "\n"
        r"由原书 p149 分析行「进而表示 $|a\cdot c|+|b\cdot c|$」及答案「$16$；$2\sqrt{15}$」判定原题带绝对值，" "\n"
        r"且不加绝对值时最小值应为 $-16$，与所给答案不符 ✓"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-186'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-186-E1',
}

T234_E1 = {
    'type': '选择',
    'stem_text': (
        r"在 $\triangle ABC$ 中，点 $P$ 满足 $\vec{BP}=3\vec{PC}$，过点 $P$ 的直线与 $AB$、$AC$ 所在的直线"
        r"分别交于点 $M$、$N$，若 $\vec{AM}=\lambda\vec{AB}$，$\vec{AN}=\mu\vec{AC}$（$\lambda>0,\mu>0$），"
        r"则 $\lambda+\mu$ 的最小值为（　　）"
    ),
    'opts': [
        ['A', r"$\dfrac{\sqrt2}2+1$"],
        ['B', r"$\dfrac{\sqrt3}2+1$"],
        ['C', r"$\dfrac{\sqrt3}2$"],
        ['D', r"$\dfrac{\sqrt5}2$"],
    ],
    'answer': r"B",
    'analysis': (
        r"由 $\vec{BP}=3\vec{PC}$ 得 $\vec{AP}=\frac14\vec{AB}+\frac34\vec{AC}$；用 $\vec{AM},\vec{AN}$ 反表 $\vec{AB},\vec{AC}$ 代入，"
        r"由 $M,P,N$ 三点共线得系数和为 $1$，即 $\frac1{4\lambda}+\frac3{4\mu}=1$；再把 $\lambda+\mu$ 与该式相乘后用基本不等式。"
    ),
    'solution': (
        r"由 $\vec{BP}=3\vec{PC}$ 得 $\vec{AP}-\vec{AB}=3(\vec{AC}-\vec{AP})$，" "\n"
        r"即 $4\vec{AP}=\vec{AB}+3\vec{AC}$，故 $\vec{AP}=\dfrac14\vec{AB}+\dfrac34\vec{AC}$。" "\n"
        r"由 $\vec{AM}=\lambda\vec{AB}$、$\vec{AN}=\mu\vec{AC}$ 得 $\vec{AB}=\dfrac1\lambda\vec{AM}$，$\vec{AC}=\dfrac1\mu\vec{AN}$，代入上式：" "\n"
        r"$\vec{AP}=\dfrac{1}{4\lambda}\vec{AM}+\dfrac{3}{4\mu}\vec{AN}$。" "\n"
        r"因为 $M,P,N$ 三点共线，所以系数之和为 $1$，即 $\dfrac1{4\lambda}+\dfrac3{4\mu}=1$。" "\n"
        r"于是 $\lambda+\mu=(\lambda+\mu)\left(\dfrac1{4\lambda}+\dfrac3{4\mu}\right)$" "\n"
        r"$=\dfrac{\lambda}{4\lambda}+\dfrac{3\lambda}{4\mu}+\dfrac{\mu}{4\lambda}+\dfrac{3\mu}{4\mu}=\dfrac14+\dfrac34+\dfrac{3\lambda}{4\mu}+\dfrac{\mu}{4\lambda}$" "\n"
        r"$=1+\dfrac{3\lambda}{4\mu}+\dfrac{\mu}{4\lambda}\ge1+2\sqrt{\dfrac{3\lambda}{4\mu}\cdot\dfrac{\mu}{4\lambda}}=1+2\sqrt{\dfrac3{16}}=1+\dfrac{\sqrt3}2$。" "\n"
        r"当且仅当 $\dfrac{3\lambda}{4\mu}=\dfrac{\mu}{4\lambda}$，即 $\mu=\sqrt3\,\lambda$ 时等号成立。" "\n"
        r"故 $\lambda+\mu$ 的最小值为 $1+\dfrac{\sqrt3}2$，选 B。"
    ),
    'review': (
        r"① ⭐⭐ **通用配法**：$(\lambda+\mu)\left(\frac\alpha\lambda+\frac\beta\mu\right)=\alpha+\beta+\frac{\alpha\mu}\lambda+\frac{\beta\lambda}\mu$。" "\n"
        r"常数项 $\alpha+\beta$ 提出来（本题 $\frac14+\frac34=1$），余下两项互为倒数倍，直接基本不等式" "\n"
        r"② ⭐⭐ **三点共线 ⟺ 系数和为 $1$**：$\vec{AP}=x\vec{AM}+y\vec{AN}$ 且 $M,P,N$ 共线 ⟺ $x+y=1$。" "\n"
        r"这是「系数和」类题的统一入口，比用分点公式快" "\n"
        r"③ ⚠ 取等条件 $\mu=\sqrt3\lambda$ 要能同时满足 $\frac1{4\lambda}+\frac3{4\mu}=1$：" "\n"
        r"代入得 $\frac1{4\lambda}+\frac3{4\sqrt3\lambda}=1$，即 $\frac{\sqrt3+3}{4\sqrt3\lambda}=1$，$\lambda=\frac{\sqrt3+3}{4\sqrt3}>0$ ✓ 存在" "\n"
        r"④ 📌 **选项还原**：ref_bank 的四项被提取为 `2/2+1, 3/2+1, 3/2, 5/2`（根号丢失）。" "\n"
        r"由答案值 $1+\frac{\sqrt3}2$ 及原书 p201 选项行判定为" "\n"
        r"A $\frac{\sqrt2}2+1$、B $\frac{\sqrt3}2+1$、C $\frac{\sqrt3}2$、D $\frac{\sqrt5}2$；答案 B 与原书一致 ✓"
    ),
    'difficulty': 0.7,
    'topics': ['M-T-234'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-234-E1',
}

T261_E2 = {
    'type': '填空',
    'stem_text': (
        r"已知数列 $\{a_n\}$ 与 $\{b_n\}$ 满足 $b_{n+1}a_n+b_na_{n+1}=(-2)^n+1$，$b_n=\dfrac{3+(-1)^{n-1}}2$（$n\in\mathbb N^*$），"
        r"且 $a_1=2$，则 $a_{2n}=$ ____。"
    ),
    'answer': r"$\dfrac{1-4^n}2$",
    'analysis': (
        r"$b_n$ 只取两个值（$n$ 偶为 $1$、$n$ 奇为 $2$），故把递推式按 $n=2k+1$ 与 $n=2k$ 分别写出，"
        r"两式相减即消去交叉项 $a_{2k+1}$，得到 $\{a_{2k}\}$ 的差分式，累加即可；"
        r"$a_2$ 由 $n=1$ 时的式子单独给出。"
    ),
    'solution': (
        r"由 $b_n=\dfrac{3+(-1)^{n-1}}2$：" "\n"
        r"当 $n=2k$（$k\in\mathbb N^*$）时 $b_{2k}=\dfrac{3+(-1)^{2k-1}}2=\dfrac{3-1}2=1$；" "\n"
        r"当 $n=2k-1$（$k\in\mathbb N^*$）时 $b_{2k-1}=\dfrac{3+(-1)^{2k-2}}2=\dfrac{3+1}2=2$。" "\n"
        r"在 $b_{n+1}a_n+b_na_{n+1}=(-2)^n+1$ 中取 $n=2k+1$（$k\in\mathbb N$）：" "\n"
        r"$b_{2k+2}a_{2k+1}+b_{2k+1}a_{2k+2}=a_{2k+1}+2a_{2k+2}=(-2)^{2k+1}+1=-2\cdot4^k+1$ ……①" "\n"
        r"取 $n=2k$（$k\in\mathbb N^*$）：" "\n"
        r"$b_{2k+1}a_{2k}+b_{2k}a_{2k+1}=2a_{2k}+a_{2k+1}=(-2)^{2k}+1=4^k+1$ ……②" "\n"
        r"①$-$②得 $2a_{2k+2}-2a_{2k}=(-2\cdot4^k+1)-(4^k+1)=-3\cdot4^k$，" "\n"
        r"即 $a_{2k+2}-a_{2k}=-\dfrac{3\times4^k}2$。" "\n"
        r"于是 $a_4-a_2=-\dfrac{3\times4^1}2$，$a_6-a_4=-\dfrac{3\times4^2}2$，$\cdots$，$a_{2k}-a_{2k-2}=-\dfrac{3\times4^{k-1}}2$。" "\n"
        r"上述 $k-1$ 个式子相加得" "\n"
        r"$a_{2k}-a_2=-\dfrac32\left(4+4^2+\cdots+4^{k-1}\right)=-\dfrac32\cdot\dfrac{4(1-4^{k-1})}{1-4}=2\left(1-4^{k-1}\right)$。" "\n"
        r"再在①中取 $k=0$（即 $n=1$）得 $a_1+2a_2=(-2)^1+1=-1$，结合 $a_1=2$ 得 $a_2=-\dfrac32$。" "\n"
        r"所以 $a_{2k}=2\left(1-4^{k-1}\right)-\dfrac32=\dfrac{4-4^k}2-\dfrac32=\dfrac{1-4^k}2$。" "\n"
        r"故 $a_{2n}=\dfrac{1-4^n}2$。" "\n"
        r"故答案为 $\dfrac{1-4^n}2$。"
    ),
    'review': (
        r"① ⭐⭐ **$b_n=\frac{3+(-1)^{n-1}}2$ 是「奇偶取常数」型**：$b_{2k}=1$、$b_{2k-1}=2$。" "\n"
        r"凡是看到这种结构，立刻按奇偶分成两支分别代入递推式" "\n"
        r"② ⭐⭐ **两式相减消去交叉项**：递推里同时含 $a_n$ 与 $a_{n+1}$，" "\n"
        r"取相邻的两个 $n$ 各写一次，相减后 $a_{2k+1}$ 自动抵消，直接得到 $\{a_{2k}\}$ 的差分 ——" "\n"
        r"这是「求隔项通项」的通法" "\n"
        r"③ ⭐⭐ **$a_2$ 必须由 $n=1$ 单独给出**：累加只给出 $a_{2k}-a_2$，初值 $a_2$ 来自原式取 $n=1$" "\n"
        r"④ 数值复核（全链对拍）：$a_2=-\frac32$；$n=2$ 时 $b_3a_2+b_2a_3=2(-\frac32)+a_3=5$ ⟹ $a_3=8$；" "\n"
        r"$n=3$ 时 $a_3+2a_4=(-2)^3+1=-7$ ⟹ $a_4=-\frac{15}2$，而 $\frac{1-4^2}2=-\frac{15}2$ ✓" "\n"
        r"⑤ 📌 **原书题干勘误（重要）**：ref_bank 把右端提取为 $(-2)^{n+1}$，**但按此两式相减得" "\n"
        r"$a_{2k+2}-a_{2k}=3\cdot4^k$（正号），进而 $a_{2n}$ 为正且与答案 $\frac{1-4^n}2$ 矛盾**。" "\n"
        r"由原书详解「令 $n=2k+1$ 得 $a_{2k+1}+2a_{2k+2}=(-2)^{2k+1}+1$」可知右端实为 $(-2)^n+1$" "\n"
        r"（OCR 把上标 $n$ 后的「$+1$」误并入指数）。按 $(-2)^n+1$ 全链自洽：" "\n"
        r"$n=1$ 时 $b_2a_1+b_1a_2=1\cdot2+2(-\frac32)=-1=(-2)^1+1$ ✓"
    ),
    'difficulty': 0.75,
    'topics': ['M-T-261'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-261-E2',
}

T262_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知数列 $\{a_n\}$ 的前 $n$ 项和为 $S_n$，且满足 $S_n=\dfrac{n^2+n}2$。" "\n"
        r"（1）求数列 $\{a_n\}$ 的通项公式；" "\n"
        r"（2）设数列 $\{b_n\}$ 满足 $b_n=\dfrac{1}{a_na_{n+1}}$，求数列 $\{b_n\}$ 的前 $n$ 项和 $T_n$。"
    ),
    'answer': r"（1）$a_n=n\ (n\in\mathbb N^*)$；（2）$T_n=\dfrac n{n+1}$",
    'analysis': (
        r"（1）用 $a_n=S_n-S_{n-1}\ (n\ge2)$ 求出通项，再验证 $n=1$ 是否也适合；"
        r"（2）代入（1）的结果得 $b_n=\frac1{n(n+1)}$，裂项为 $\frac1n-\frac1{n+1}$ 后相消求和。"
    ),
    'solution': (
        r"**（1）** 当 $n=1$ 时，$a_1=S_1=\dfrac{1^2+1}2=1$；" "\n"
        r"当 $n\ge2$ 且 $n\in\mathbb N^*$ 时，" "\n"
        r"$a_n=S_n-S_{n-1}=\dfrac{n^2+n}2-\dfrac{(n-1)^2+(n-1)}2=\dfrac{n^2+n-(n^2-2n+1+n-1)}2=\dfrac{2n}2=n$。" "\n"
        r"当 $n=1$ 时，$a_1=1$ 也适合上式。" "\n"
        r"所以数列 $\{a_n\}$ 的通项公式为 $a_n=n\ (n\in\mathbb N^*)$。" "\n"
        r"**（2）** 由（1）得 $b_n=\dfrac{1}{a_na_{n+1}}=\dfrac{1}{n(n+1)}=\dfrac1n-\dfrac1{n+1}$。" "\n"
        r"所以 $T_n=\left(1-\dfrac12\right)+\left(\dfrac12-\dfrac13\right)+\cdots+\left(\dfrac1n-\dfrac1{n+1}\right)$" "\n"
        r"$=1-\dfrac1{n+1}=\dfrac n{n+1}$。"
    ),
    'review': (
        r"① ⭐⭐ **必须验证 $n=1$**：$a_n=S_n-S_{n-1}$ 只对 $n\ge2$ 成立，" "\n"
        r"本题 $a_1=S_1=1$ 恰好适合 $a_n=n$，但这是**需要说明**的一步，不能默认" "\n"
        r"② ⭐⭐ 裂项 $\frac1{n(n+1)}=\frac1n-\frac1{n+1}$ 中**两因子之差为 $1$，故系数为 $1$**；" "\n"
        r"若分母是 $n(n+2)$（差为 $2$），则需乘 $\frac12$ —— 这是最高频丢分点" "\n"
        r"③ 数值复核：$T_1=b_1=\frac1{1\cdot2}=\frac12=\frac1{1+1}$ ✓；" "\n"
        r"$T_2=\frac12+\frac16=\frac23=\frac2{2+1}$ ✓；$T_3=\frac23+\frac1{12}=\frac34=\frac3{3+1}$ ✓" "\n"
        r"④ 📌 **题干还原**：ref_bank 中本题题干只剩两问，前置条件「$S_n=\frac{n^2+n}2$」丢失；" "\n"
        r"由原书 p221 第 2 题及详解首行「$a_1=S_1=\frac{1+1}2=1$」「$a_n=S_n-S_{n-1}=\frac{n^2+n}2-\frac{(n-1)^2+(n-1)}2=n$」" "\n"
        r"完整反推得出，与答案 $a_n=n$、$T_n=\frac n{n+1}$ 一致 ✓"
    ),
    'difficulty': 0.45,
    'topics': ['M-T-262'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-262-V1',
}

QS = [
    T138_V3,
    T141_V2,
    T150_V2,
    T177_V3,
    T186_E1,
    T234_E1,
    T261_E2,
    T262_V1,
]
