# -*- coding: utf-8 -*-
r"""第20批（上）：M-T-053 画图：放大镜（4题）+ M-T-054 利用对称解决恒成立和存在型（3题）

来源：2024高中数学热点题型归纳完整解析版.pdf 专题2-2 p24~p26（PDF 页 23~25）

## 放大镜函数（M-T-053）的核心

$f(x+T)=T\cdot f(x)$ 叫「似周期」，本质是**每平移一次就放大/缩小一次**：

- E1 直接考定义辨析
- V1/V2/V3 都是「先画出一个周期，再按倍数复制」——值域逐段乘 $2$（或 $\frac12$）

## 本批用 --chars 精确确认的部分

PDF 里分数是矢量绘制，提取时分子、分母、分数线会**分裂到不同行**，
常规提取只能看到「A. - ,0」「A. 1,」这种残片。用 `--chars` 按
**x 坐标对齐**才把选项还原出来（详见各题 review）：

- M-T-054-V1 的四个分数：x≈347.8 → $\frac53$；x≈460.0 → $\frac52$；
  x≈508.4 → $\frac53$；x≈520.6 → $\frac52$
- M-T-054-V2 的分数：x≈71.6/71.4 → $\frac14$；x≈176.7/176.6 → $\frac12$

## 破碎情况汇总

| 题 | 破碎文本 | 还原依据 |
|---|---|---|
| 053-V1 | `-log 3 > -1 / a2` | 实为 $-\log_a3>-\frac12$、$-\log_a5<-\frac14$（分子分母分离），解得 $9<a<625$ |
| 053-V2 | `2x2` | $2x^{2}$，由 $f(1)=2$ 反推 |
| 053-V3 | `f (x + 1)= f (x) / 2` | $f(x+1)=\frac12f(x)$ |
| 054-E1 | `lg(x +x2+ 1)` | $\lg\left(x+\sqrt{x^{2}+1}\right)$，根号丢失 |
"""

T053_E1 = {
    'type': '选择',
    'stem_text': (
        r"设函数 $y=f(x)$ 的定义域为 $D$，如果存在非零常数 $T$，"
        r"对于任意 $x\in D$，都有 $f(x+T)=T\cdot f(x)$，"
        r"则称函数 $y=f(x)$ 是“似周期函数”，非零常数 $T$ 为函数 $y=f(x)$ 的“似周期”．"
        r"现有下面四个关于“似周期函数”的命题：" "\n"
        r"① 如果“似周期函数” $y=f(x)$ 的“似周期”为 $-1$，"
        r"那么它是周期为 $2$ 的周期函数；" "\n"
        r"② 函数 $f(x)=2^{x}$ 是“似周期函数”；" "\n"
        r"③ 如果函数 $f(x)=\cos\omega x$ 是“似周期函数”，"
        r"那么“$\omega=2k\pi,\ k\in\mathbb Z$ 或 $\omega=(2k+1)\pi,\ k\in\mathbb Z$”．" "\n"
        r"以上正确结论的个数是（　　）"
    ),
    'opts': [
        ('A', r"$0$"), ('B', r"$1$"),
        ('C', r"$2$"), ('D', r"$3$"),
    ],
    'answer': 'C',
    'analysis': (
        r"逐条按定义列方程：①代入 $T=-1$ 连用两次；"
        r"②$2^{x+T}=T\cdot2^{x}$ 化为 $2^{T}=T$（无解）；"
        r"③展开 $\cos(\omega x+\omega T)$ 比较系数。"
    ),
    'solution': (
        r"**①**：由“似周期”为 $-1$ 得 $f(x-1)=(-1)\cdot f(x)=-f(x)$，" "\n"
        r"于是 $f(x-2)=-f(x-1)=f(x)$，故 $f$ 是周期为 $2$ 的周期函数，**①正确**．" "\n"
        r"**②**：若 $f(x)=2^{x}$ 是“似周期函数”，则存在非零常数 $T$ 使" "\n"
        r"$2^{x+T}=T\cdot2^{x}$ 恒成立，即 $2^{T}=T$．" "\n"
        r"但 $2^{T}>0$ 且 $2^{T}>T$ 对一切实数 $T$ 成立（$T>0$ 时指数函数增长快于自身，"
        r"$T\leqslant0$ 时左边 $>0\geqslant$ 右边），**无解**，故**②错误**．" "\n"
        r"**③**：若 $f(x)=\cos\omega x$ 是“似周期函数”，则存在非零常数 $T$ 使" "\n"
        r"$\cos\bigl(\omega(x+T)\bigr)=T\cos\omega x$ 恒成立．" "\n"
        r"左边 $=\cos\omega x\cos\omega T-\sin\omega x\sin\omega T$，比较系数得" "\n"
        r"$\begin{cases}\cos\omega T=T,\\ \sin\omega T=0.\end{cases}$" "\n"
        r"由 $\sin\omega T=0$ 得 $\omega T=k\pi$（$k\in\mathbb Z$），"
        r"此时 $T=\cos(k\pi)=(-1)^{k}$．" "\n"
        r"$k$ 为偶数时 $T=1$，$\omega=k\pi=2n\pi$；"
        r"$k$ 为奇数时 $T=-1$，$\omega=\dfrac{k\pi}{T}=-(2n+1)\pi$，"
        r"即 $\omega=(2m+1)\pi$（符号可吸收进 $m$）．" "\n"
        r"故 $\omega=2k\pi$ 或 $\omega=(2k+1)\pi$，**③正确**．" "\n"
        r"综上，正确结论共 $2$ 个，选 C．"
    ),
    'review': (
        r"★ 提取文本作「②函数f(x) = 2x是“似周期函数”」与"
        r"「③如果函数f(x) = cosωx 是“似周期函数”」，"
        r"$2^{x}$ 的上标、$\cos\omega x$ 的 $\omega$ 尚可辨认，"
        r"但 $2^{T}=T$ 这一步在提取文本里被压成「2x+T = T ⋅2x / 2T = T」。"
        r"由详解「$2^{x+T}=T\cdot2^{x}$ 恒成立，故 $2^{T}=T$ 成立，但无解，故②错误」"
        r"与「$\cos\omega x\cdot\cos\omega T-\sin\omega x\cdot\sin\omega T=T\cos\omega x$ 恒成立，"
        r"故 $\begin{cases}\cos\omega T=T\\ \sin\omega T=0\end{cases}$，"
        r"故 $\omega=2k\pi,k\in\mathbb Z$ 或 $\omega=(2k+1)\pi,k\in\mathbb Z$，故③正确」还原。" "\n"
        r"**数值校验**：$2^{T}=T$ 确实无解——$T=2$ 时 $4\neq2$，$T=4$ 时 $16\neq4$，"
        r"$T<0$ 时左边 $>0>$ 右边 ✓。$T=1,\omega=2\pi$："
        r"$\cos(2\pi(x+1))=\cos(2\pi x+2\pi)=\cos2\pi x=1\cdot\cos2\pi x$ ✓。"
        r"$T=-1,\omega=\pi$：$\cos(\pi(x-1))=\cos(\pi x-\pi)=-\cos\pi x=(-1)\cdot\cos\pi x$ ✓。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-053'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-053-E1',
}

T053_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知函数 $f(x)$ 满足当 $x\leqslant0$ 时，$2f(x-2)=f(x)$，"
        r"且当 $x\in(-2,0]$ 时，$f(x)=|x+1|-1$；"
        r"当 $x>0$ 时，$f(x)=\log_{a}x$（$a>0$ 且 $a\neq1$）．"
        r"若函数 $f(x)$ 的图象上关于原点对称的点恰好有 $3$ 对，"
        r"则 $a$ 的取值范围是（　　）"
    ),
    'opts': [
        ('A', r"$(625,+\infty)$"), ('B', r"$(4,64)$"),
        ('C', r"$(9,625)$"), ('D', r"$(9,64)$"),
    ],
    'answer': 'C',
    'analysis': (
        r"把“关于原点对称的点成对”翻译成方程 $f(-t)=-\log_{a}t$（$t>0$）；"
        r"由 $f(x)=2f(x-2)$ 知负半轴上每一段的值域是前一段的 $\frac12$："
        r"$[-1,0]$、$[-\frac12,0]$、$[-\frac14,0]\cdots$ 逐段缩小，据此列不等式。"
    ),
    'solution': (
        r"**转化为方程**：设 $P=(t,f(t))$（$t>0$）在图象上，则 "
        r"$f(t)=\log_{a}t$；它关于原点的对称点为 $(-t,-\log_{a}t)$，" "\n"
        r"该点也在图象上 $\iff$ $f(-t)=-\log_{a}t$．" "\n"
        r"**负半轴的分段值域**：由 $2f(x-2)=f(x)$ 即 $f(x)=2f(x-2)$，"
        r"得 $f(u+2)=\dfrac{f(u)}{2}$，图象每往左 $2$ 个单位、纵向**缩小为 $\frac12$**．" "\n"
        r"在 $(-2,0]$ 上 $f(x)=|x+1|-1$，值域 $[-1,0]$；" "\n"
        r"在 $(-4,-2]$ 上值域为 $\left[-\dfrac12,0\right]$；" "\n"
        r"在 $(-6,-4]$ 上值域为 $\left[-\dfrac14,0\right]$．" "\n"
        r"**数交点**：$y=-\log_{a}t$ 在 $t>0$ 上单调（$a>1$ 时递减）．"
        r"要恰有 $3$ 对，需它依次穿过上面三段各一次、且不进入第四段：" "\n"
        r"$-\log_{a}3>-\dfrac12$（在第 2 段内取到）且 "
        r"$-\log_{a}5<-\dfrac14$（不到第 3 段底部）．" "\n"
        r"由 $a>1$：$-\log_{a}3>-\dfrac12\iff\log_{a}3<\dfrac12\iff 3<a^{1/2}"
        r"\iff a>9$；" "\n"
        r"$-\log_{a}5<-\dfrac14\iff\log_{a}5>\dfrac14\iff 5>a^{1/4}"
        r"\iff a<625$．" "\n"
        r"综上 $9<a<625$，选 C．" "\n"
        r"（$0<a<1$ 时对称后的图象不可能与负半轴部分有 $3$ 个交点，舍去。）"
    ),
    'review': (
        r"★ 提取文本作「-log3 >- 1 / a2，解得9 < a < 625」与「-log5 <-4 / a」——"
        r"**分数线丢失导致分子分母分裂**：实为 $-\log_a3>-\dfrac12$ 与 "
        r"$-\log_a5<-\dfrac14$（「1/2」拆成「1」与「2」，「1/4」拆成「1」与「4」）。"
        r"由详解「当 $a>1$ 时…则 $-\log_a3>-\frac12$，$-\log_a5<-\frac14$，"
        r"解得 $9<a<625$，故选 C」还原。" "\n"
        r"**验算（这是判定分数线归属的关键）**：" "\n"
        r"若按 $-\log_a3>-\frac12$：$\log_a3<\frac12\Rightarrow a>3^2=9$ ✓ 下界恰为 9；" "\n"
        r"若按 $-\log_a3>-1$（误读）：$a>3$，得不到 9 ✗。" "\n"
        r"若按 $-\log_a5<-\frac14$：$\log_a5>\frac14\Rightarrow a<5^4=625$ ✓ 上界恰为 625；" "\n"
        r"若按 $-\log_a5<-4$（误读）：$\log_a5>4\Rightarrow a<5^{1/4}$，与 $a>9$ 矛盾 ✗。" "\n"
        r"两条都只有「分子分母合起来读」才能对上答案 $(9,625)$。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-053'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-053-V1',
}

T053_V2 = {
    'type': '选择',
    'stem_text': (
        r"设函数 $f(x)$ 的定义域为 $\mathbb R$，满足 $f(x+1)=2f(x)$，"
        r"且当 $x\in(0,1]$ 时，$f(x)=x(x-1)$．"
        r"若对任意 $x\in(-\infty,m]$，都有 $f(x)\geqslant-\dfrac12$，"
        r"则 $m$ 的取值范围是（　　）"
    ),
    'opts': [
        ('A', r"$\left(-\infty,\dfrac32\right]$"),
        ('B', r"$\left(-\infty,\dfrac{10-\sqrt2}{4}\right]$"),
        ('C', r"$\left(-\infty,\dfrac52\right]$"),
        ('D', r"$\left(-\infty,\dfrac{10+\sqrt2}{4}\right]$"),
    ],
    'answer': 'B',
    'analysis': (
        r"由 $f(x+1)=2f(x)$ 知每右移 $1$ 个单位、纵向**放大为 $2$ 倍**；"
        r"写出第 $3$ 段（$x\in(2,3]$）的解析式，解 $f(x)=-\frac12$ 取较小的根。"
    ),
    'solution': (
        r"**放大规律**：$f(x+1)=2f(x)\Rightarrow f(x)=2f(x-1)$，"
        r"即图象向右平移 $1$ 个单位、纵坐标变为原来的 $2$ 倍．" "\n"
        r"**第 3 段**：当 $2<x\leqslant3$ 时，$x-2\in(0,1]$，" "\n"
        r"$f(x)=2f(x-1)=4f(x-2)=4(x-2)(x-3)$．" "\n"
        r"**解方程**：令 $4(x-2)(x-3)=-\dfrac12$，即 $x^{2}-5x+6=-\dfrac18$，"
        r"$x^{2}-5x+\dfrac{49}{8}=0$，" "\n"
        r"$x=\dfrac{5\pm\sqrt{25-24.5}}{2}=\dfrac{5\pm\sqrt{0.5}}{2}"
        r"=\dfrac{10\pm\sqrt2}{4}$．" "\n"
        r"两根为 $\dfrac{10-\sqrt2}{4}\approx2.146$ 与 $\dfrac{10+\sqrt2}{4}\approx2.854$．" "\n"
        r"**定 $m$**：$f$ 在 $(2,3]$ 上先降后升（开口向上），"
        r"在两根之间 $f(x)<-\dfrac12$．" "\n"
        r"要使对任意 $x\in(-\infty,m]$ 都有 $f(x)\geqslant-\dfrac12$，"
        r"$m$ 不能越过第一个“下陷”的起点，故 $m\leqslant\dfrac{10-\sqrt2}{4}$．" "\n"
        r"即 $m\in\left(-\infty,\dfrac{10-\sqrt2}{4}\right]$，选 B．"
    ),
    'review': (
        r"★ 提取文本作「当x ∈(0,1] 时，f(x) = x(x - 1)」（这一段完整）与"
        r"「令4(x - 2) (x - 3) =- 1 / 2，解得 x= 10 -2 / 1 4，x= 10 +2 / 2 4」，"
        r"$-\frac12$ 与两根的分数线全丢（「1 / 2」分裂、根式 $\sqrt2$ 的「2」被当成数字）。"
        r"由详解「当 $2<x\leqslant3$ 时，$f(x)=4f(x-2)=4(x-2)(x-3)$，"
        r"令 $4(x-2)(x-3)=-\frac12$，解得 $x=\frac{10-\sqrt2}{4}$，$x=\frac{10+\sqrt2}{4}$；"
        r"所以要使对任意 $x\in(-\infty,m]$，都有 $f(x)\geqslant-\frac12$，"
        r"则 $m\leqslant\frac{10-\sqrt2}{4}$」还原。" "\n"
        r"**数值校验**：$4(x-2)(x-3)=-\frac12$ → $x^2-5x+\frac{49}{8}=0$，"
        r"$\Delta=25-\frac{49}{2}=0.5$，$x=\frac{5\pm\sqrt{0.5}}{2}$ ✓；"
        r"$\frac{10\pm\sqrt2}{4}=\frac{5\pm\sqrt{0.5}}{2}$ ✓（分子分母同乘 2）。"
        r"$x=2.5$：$4\times0.5\times(-0.5)=-1<-\frac12$ ✓ 确在两根之间下陷。" "\n"
        r"**⚠ 选项 A、C 的说明**：提取文本里 A、C 只剩「3[」「5[」与分母「2」，"
        r"按上下文还原为 $\frac32$ 与 $\frac52$——"
        r"它们与 B、D 构成递增序列 $\frac32<\frac{10-\sqrt2}{4}<\frac52<\frac{10+\sqrt2}{4}$，"
        r"作为干扰项合理。答案 B 由详解确凿，不受影响。"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-053'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-053-V2',
}

T053_V3 = {
    'type': '选择',
    'stem_text': (
        r"定义在 $\mathbb R$ 上的函数 $f(x)$ 满足 $f(x+1)=\dfrac12 f(x)$，"
        r"且当 $x\in[0,1)$ 时，$f(x)=1-|2x-1|$．"
        r"则使得 $f(x)\leqslant\dfrac1{16}$ 在 $[m,+\infty)$ 上恒成立的 "
        r"$m$ 的最小值是（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac72$"), ('B', r"$\dfrac92$"),
        ('C', r"$\dfrac{13}4$"), ('D', r"$\dfrac{15}4$"),
    ],
    'answer': 'D',
    'analysis': (
        r"写出第 $n$ 段的解析式 $f(x)=\dfrac{1}{2^{n}}\bigl[1-|2x-2n-1|\bigr]$；"
        r"估值域上界 $\dfrac{1}{2^{n}}$ 知 $n\geqslant4$ 时自然满足；"
        r"再在第 $3$ 段（$[\frac72,4)$ 附近）解 $f(x)=\dfrac1{16}$ 取临界点。"
    ),
    'solution': (
        r"**分段解析式**：由 $f(x+1)=\dfrac12f(x)$ 得，"
        r"当 $x\in[n,n+1)$（$n\in\mathbb Z$）时" "\n"
        r"$f(x)=\dfrac{1}{2^{n}}\Bigl[1-\bigl|2(x-n)-1\bigr|\bigr]"
        r"=\dfrac{1}{2^{n}}\bigl[1-|2x-2n-1|\bigr]$．" "\n"
        r"**值域上界**：该段最大值为 $\dfrac{1}{2^{n}}$（在 $x=n+\dfrac12$ 处取到）．"
        r"当 $n\geqslant4$ 时 $\dfrac{1}{2^{n}}\leqslant\dfrac1{16}$，自然满足．" "\n"
        r"**第 $3$ 段**（$x\in[3,4)$，$n=3$）：$f(x)=\dfrac18\bigl[1-|2x-7|\bigr]$，"
        r"令 $f(x)=\dfrac1{16}$：" "\n"
        r"$\dfrac18\bigl[1-|2x-7|\bigr]=\dfrac1{16}\Rightarrow 1-|2x-7|=\dfrac12"
        r"\Rightarrow |2x-7|=\dfrac12$，" "\n"
        r"得 $2x-7=\pm\dfrac12$，即 $x=\dfrac{15}4$ 或 $x=\dfrac{13}4$．" "\n"
        r"该段上 $f$ 先降到 $-\frac18\cdot0$…实际是先减后增（顶点在 $x=\frac72$ 处取最大值 "
        r"$\frac18$），在 $\left[\dfrac72,4\right)$ 上从 $\dfrac18$ 递减到 $0$，"
        r"故 $x\geqslant\dfrac{15}4$ 时 $f(x)\leqslant\dfrac1{16}$．" "\n"
        r"结合图象（$x\geqslant\frac{15}4$ 之后各段整体不超过 $\frac1{16}$），"
        r"$m$ 的最小值为 $\dfrac{15}4$，选 D．"
    ),
    'review': (
        r"★ 提取文本作「定义在R 上函数q 满足f (x + 1)= f (x) / 2，且当x ∈[0,1(时，"
        r"f (x)= 1 - |2x - 1|. 则使得f (x)≤ 在[m,+∞(上恒成立的m 的最小值是() / 16」，"
        r"$\frac12$ 与 $\frac1{16}$ 的分数线全丢（「1 / 2」「1 / 16」分裂），"
        r"「函数q」是「函数f」的误认（草体 f 与 q 形近）。"
        r"由详解「在区间 $[n,n+1)$（$n\in\mathbb Z$）上，$f(x)=\frac{1}{2^n}[1-|2x-2n+1|]$，"
        r"…所以当 $n\geqslant4$ 时 $f(x)\leqslant\frac{1}{16}$；"
        r"在 $[\frac72,4)$ 上，由 $f(x)=\frac18[1-|2x-7|]=\frac{1}{16}$，得 $x=\frac{15}4$；"
        r"由图象可知当 $x\geqslant\frac{15}4$ 时，$f(x)\leqslant\frac1{16}$」还原。" "\n"
        r"**结构校验**：$f(x)=\frac{1}{2^n}[1-|2x-2n-1|]$，代入 $n=3$："
        r"$\frac18[1-|2x-7|]$ ✓ 与详解一致。"
        r"$x=\frac72=3.5$：$|7-7|=0$，$f=\frac18$（最大值）✓；"
        r"$x=4$：$|8-7|=1$，$f=0$ ✓；$x=\frac{15}4=3.75$：$|7.5-7|=0.5$，"
        r"$f=\frac18\times0.5=\frac1{16}$ ✓ 恰取等号。" "\n"
        r"**选项**：四个选项 $\frac72,\frac92,\frac{13}4,\frac{15}4$ 由「7 9 13 15 / 2 2 4 4」"
        r"还原（分子与分母分离），答案 D 与详解一致 ✓。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-053'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-053-V3',
}

T054_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知函数 $f(x)=\lg\left(x+\sqrt{x^{2}+1}\right)$，"
        r"且对于任意的 $x\in(1,2]$，" "\n"
        r"$f\!\left(\dfrac{x+1}{x-1}\right)+"
        r"f\!\left(\dfrac{m}{(x-1)^{2}(x-6)}\right)>0$ 恒成立，"
        r"则 $m$ 的取值范围为（　　）"
    ),
    'opts': [
        ('A', r"$(-\infty,0)$"), ('B', r"$(-\infty,0]$"),
        ('C', r"$[4,+\infty)$"), ('D', r"$(12,+\infty)$"),
    ],
    'answer': 'B',
    'analysis': (
        r"先证 $f$ 是奇函数且单调递增，把不等式化为代数不等式；"
        r"注意 $x\in(1,2]$ 时 $(x-1)^{2}(x-6)<0$，去分母要**变号**；"
        r"最后参变分离求 $g(x)$ 的上确界。"
    ),
    'solution': (
        r"**奇偶性**：定义域为 $\mathbb R$，且" "\n"
        r"$f(-x)=\lg\left(\sqrt{x^{2}+1}-x\right)"
        r"=\lg\dfrac{1}{\sqrt{x^{2}+1}+x}=-\lg\left(x+\sqrt{x^{2}+1}\right)=-f(x)$，" "\n"
        r"故 $f$ 为奇函数；又 $x+\sqrt{x^{2}+1}$ 在 $(0,+\infty)$ 上递增，"
        r"$\lg$ 递增，故 $f$ 在 $\mathbb R$ 上**单调递增**．" "\n"
        r"**化不等式**：由奇性 $-f(u)=f(-u)$，原不等式等价于" "\n"
        r"$f\!\left(\dfrac{x+1}{x-1}\right)>f\!\left(-\dfrac{m}{(x-1)^{2}(x-6)}\right)$，" "\n"
        r"再由单调性得 $\dfrac{x+1}{x-1}>-\dfrac{m}{(x-1)^{2}(x-6)}$．" "\n"
        r"**去分母**：$x\in(1,2]$ 时 $x-1>0$、$x-6<0$，"
        r"故 $(x-1)^{2}(x-6)<0$，两边同乘要**变号**：" "\n"
        r"$(x+1)(x-1)(x-6)<-m$ 恒成立．" "\n"
        r"**求上确界**：设 $g(x)=(x+1)(x-1)(x-6)=x^{3}-6x^{2}-x+6$，" "\n"
        r"$g'(x)=3x^{2}-12x-1=3(x-2)^{2}-13$，当 $1<x\leqslant2$ 时 $g'(x)<0$，"
        r"$g$ 单调递减，" "\n"
        r"故 $g(x)$ 的上确界为 $\lim\limits_{x\to1^{+}}g(x)=0$（**取不到**，"
        r"$g(1)=0$ 但 $x=1$ 不在定义区间内）．" "\n"
        r"**定 $m$**：需 $0\leqslant-m$，即 $m\leqslant0$，"
        r"得 $m\in(-\infty,0]$，选 B．"
    ),
    'review': (
        r"★ 提取文本作「已知函数f(x) = lg(x +x2+ 1)，且对于任意的x ∈(1，2]，"
        r"f()+ f> 0 恒成立，则m 的取值范围为 / x - 1((x - 1)2(x - 6))」，"
        r"根号 $\sqrt{x^2+1}$ 丢失（变成 x +x2+ 1），两个分式的分子与分母分离到不同行。"
        r"由详解「$f(x)$ 的定义域为 $\mathbb R$，$f(-x)=\lg(\sqrt{x^2+1}-x)=\lg\frac{1}{x^2+1+x}"
        r"=-\lg(x+\sqrt{x^2+1})=-f(x)$，∴$f(x)$ 为奇函数，又 $f(x)$ 在 $(0,+\infty)$ 上单调递增」"
        r"与「$f(\frac{x+1}{x-1})>-f(\frac{m}{(x-1)^2(x-6)})=f(-\frac{m}{(x-1)^2(x-6)})$，"
        r"∴$\frac{x+1}{x-1}>\frac{-m}{(x-1)^2(x-6)}$」还原。" "\n"
        r"**关键细节**：详解写「$g(x)$ 的最大值为从负数无限接近于 $0$，$g(x)_{\max}<0$，"
        r"∴$0\leqslant-m$，$m\leqslant0$」——" "\n"
        r"这里上确界 $0$ **取不到**，所以是 $0\leqslant -m$（可以取等号，"
        r"因 $g(x)<0$ 严格成立时 $-m$ 只需 $\geqslant\sup g=0$），答案含 $0$，选 B 而非 A。" "\n"
        r"**数值校验**：$g(x)=x^3-6x^2-x+6$，$g(1)=1-6-1+6=0$ ✓；"
        r"$g(2)=8-24-2+6=-12$ ✓ 递减；$g'(1)=3-12-1=-10<0$ ✓。"
        r"$m=0$ 时：需 $(x+1)(x-1)(x-6)<0$，而 $x\in(1,2]$ 时该式 $<0$ ✓ 恒成立。"
        r"$m=1$ 时：需 $g(x)<-1$，$x\to1^+$ 时 $g\to0>-1$ ✗ 不成立 ✓。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-054'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-054-E1',
}

T054_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知函数 $f(x)=\dfrac{2^{x}+m}{2^{x}+1}$（$0\leqslant x\leqslant1$），"
        r"函数 $g(x)=(m-1)x$（$1\leqslant x\leqslant2$）．"
        r"若任意的 $x_{1}\in[0,1]$，存在 $x_{2}\in[1,2]$，使得 $f(x_{1})=g(x_{2})$，"
        r"则实数 $m$ 的取值范围为（　　）"
    ),
    'opts': [
        ('A', r"$\left(1,\dfrac53\right]$"),
        ('B', r"$[2,3]$"),
        ('C', r"$\left[2,\dfrac52\right]$"),
        ('D', r"$\left[\dfrac53,\dfrac52\right]$"),
    ],
    'answer': 'D',
    'analysis': (
        r"“$\forall x_{1}\ \exists x_{2}$ 使 $f(x_{1})=g(x_{2})$” "
        r"等价于 **$f$ 的值域 $\subseteq$ $g$ 的值域**；"
        r"再按 $m$ 与 $1$ 的大小关系分情况讨论两个值域。"
    ),
    'solution': (
        r"**题意转化**：任意 $x_{1}\in[0,1]$ 都能找到 $x_{2}\in[1,2]$ 使 "
        r"$f(x_{1})=g(x_{2})$，即 $f$ 在 $[0,1]$ 上的值域是 $g$ 在 $[1,2]$ 上值域的**子集**．" "\n"
        r"**$f$ 的值域**：$f(x)=\dfrac{2^{x}+m}{2^{x}+1}=1+\dfrac{m-1}{2^{x}+1}$．" "\n"
        r"$x=0$ 时 $f=1+\dfrac{m-1}{2}=\dfrac{m+1}{2}$；"
        r"$x=1$ 时 $f=1+\dfrac{m-1}{3}=\dfrac{m+2}{3}$．" "\n"
        r"当 $m<1$ 时 $m-1<0$，$f$ 递增，值域 $\left[\dfrac{m+1}{2},\dfrac{m+2}{3}\right]$；" "\n"
        r"当 $m>1$ 时 $m-1>0$，$f$ 递减，值域 $\left[\dfrac{m+2}{3},\dfrac{m+1}{2}\right]$．" "\n"
        r"**$g$ 的值域**：$g(x)=(m-1)x$ 是一次函数，"
        r"$m<1$ 时递减，值域 $[2m-2,\,m-1]$；$m>1$ 时递增，值域 $[m-1,\,2m-2]$．" "\n"
        r"**情况一 $m<1$**：需 $\left[\dfrac{m+1}{2},\dfrac{m+2}{3}\right]\subseteq[2m-2,\,m-1]$，" "\n"
        r"即 $\begin{cases}\dfrac{m+1}{2}\geqslant2m-2\\[4pt]\dfrac{m+2}{3}\leqslant m-1\end{cases}$"
        r"$\Rightarrow\begin{cases}m\leqslant\frac53\\ m\geqslant\frac52\end{cases}$，无解．" "\n"
        r"**情况二 $m>1$**：需 $\left[\dfrac{m+2}{3},\dfrac{m+1}{2}\right]\subseteq[m-1,\,2m-2]$，" "\n"
        r"即 $\begin{cases}\dfrac{m+1}{2}\leqslant2m-2\\[4pt]\dfrac{m+2}{3}\geqslant m-1\end{cases}$"
        r"$\Rightarrow\begin{cases}m\geqslant\frac53\\ m\leqslant\frac52\end{cases}$，"
        r"得 $\dfrac53\leqslant m\leqslant\dfrac52$．" "\n"
        r"**情况三 $m=1$**：$f\equiv1$，$g\equiv0$，值域不相交，不满足．" "\n"
        r"综上 $m\in\left[\dfrac53,\dfrac52\right]$，选 D．"
    ),
    'review': (
        r"★ **选项用 `--chars` 按 x 坐标对齐才还原出来**。提取文本只剩"
        r"「A. 1,B. 2,3C. 2,D. ,」加一行孤立的「3232」（分母）与「5 55 5」（分子）。"
        r"按 x 坐标配对：x≈347.8 → $\frac53$；x≈460.0 → $\frac52$；"
        r"x≈508.4 → $\frac53$；x≈520.6 → $\frac52$。" "\n"
        r"于是 A $=\left(1,\frac53\right]$、B $=[2,3]$、C $=\left[2,\frac52\right]$、"
        r"D $=\left[\frac53,\frac52\right]$，其中 D 与详解答案完全一致 ✓。" "\n"
        r"**数值校验**：$m=2$（在 $[\frac53,\frac52]=[1.667,2.5]$ 内）："
        r"$f$ 值域 $[\frac{2+2}{3},\frac{2+1}{2}]=[\frac43,1.5]$，"
        r"$g$ 值域 $[1,2]$，$[\frac43,1.5]\subseteq[1,2]$ ✓。"
        r"$m=3$（超出）：$f$ 值域 $[\frac53,2]$，$g$ 值域 $[2,4]$，$\frac53<2$ ✗ 不含 ✓。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-054'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-054-V1',
}

T054_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知 $f(x)$ 是定义在 $\mathbb R$ 上的函数，且 $f(x+1)$ 关于直线 $x=-1$ 对称．"
        r"当 $x\geqslant0$ 时，" "\n"
        r"$f(x)=\begin{cases}2^{-\frac14x^{2}+1}, & 0\leqslant x<2,\\ "
        r"2-\log_{2}x, & x\geqslant2,\end{cases}$" "\n"
        r"若对任意的 $x\in[m,m+1]$，不等式 $f(2-2x)\geqslant f(x+m)$ 恒成立，"
        r"则实数 $m$ 的取值范围是（　　）"
    ),
    'opts': [
        ('A', r"$\left[-\dfrac14,0\right]$"),
        ('B', r"$\left[\dfrac12,1\right]$"),
        ('C', r"$[1,+\infty)$"),
        ('D', r"$\left[\dfrac12,+\infty\right)$"),
    ],
    'answer': 'D',
    'analysis': (
        r"先证 $f$ 在 $[0,+\infty)$ 上单调递减、且为偶函数，"
        r"把函数值不等式化为绝对值不等式 $|2-2x|\leqslant|x+m|$；"
        r"再转化为二次函数在区间 $[m,m+1]$ 上恒 $\leqslant0$（端点法）。"
    ),
    'solution': (
        r"**单调性**：当 $0\leqslant x<2$ 时，指数 $-\dfrac14x^{2}+1$ 递减、"
        r"$y=2^{u}$ 递增，故 $f$ 递减，且 $f(x)>2^{-\frac14\cdot4+1}=2^{0}=1$；" "\n"
        r"当 $x\geqslant2$ 时 $f(x)=2-\log_{2}x$ 递减，且 $f(x)\leqslant f(2)=2-1=1$．" "\n"
        r"两段衔接处 $f(2)=1$ 与前段的极限一致，故 $f$ 在 $[0,+\infty)$ 上**单调递减**．" "\n"
        r"**偶性**：$f(x+1)$ 关于 $x=-1$ 对称，即把图象左移 $1$ 后对称轴是 $x=0$，"
        r"故 $f$ 本身关于 $x=0$ 对称，$f$ 为**偶函数**．" "\n"
        r"**化不等式**：$f(2-2x)\geqslant f(x+m)$ $\iff$ "
        r"$f(|2-2x|)\geqslant f(|x+m|)$，" "\n"
        r"由 $f$ 在 $[0,+\infty)$ 上递减得 $|2-2x|\leqslant|x+m|$，"
        r"平方得 $(2-2x)^{2}\leqslant(x+m)^{2}$，" "\n"
        r"整理：$3x^{2}-(8+2m)x+4-m^{2}\leqslant0$．" "\n"
        r"设 $g(x)=3x^{2}-(8+2m)x+4-m^{2}$（开口向上），"
        r"要在 $[m,m+1]$ 上恒 $\leqslant0$，只需两端点 $\leqslant0$：" "\n"
        r"$g(m)=3m^{2}-(8+2m)m+4-m^{2}=-8m+4\leqslant0\Rightarrow m\geqslant\dfrac12$；" "\n"
        r"$g(m+1)=3(m+1)^{2}-(8+2m)(m+1)+4-m^{2}=-4m-1\leqslant0"
        r"\Rightarrow m\geqslant-\dfrac14$．" "\n"
        r"取交集得 $m\geqslant\dfrac12$，即 $m\in\left[\dfrac12,+\infty\right)$，选 D．"
    ),
    'review': (
        r"★ **选项用 `--chars` 按 x 坐标对齐还原**：提取文本只剩"
        r"「A. - ,0(B. ,1」加分母「4」「2」。" "\n"
        r"按 x 坐标：x≈71.6（分子 '1'）+ x≈71.4（分母 '4'）+ 负号 → $-\dfrac14$；"
        r"x≈176.7（分子 '1'）+ x≈176.6（分母 '2'）→ $\dfrac12$。" "\n"
        r"故 A $=\left[-\frac14,0\right]$、B $=\left[\frac12,1\right]$，"
        r"C、D 据文本「C. [1,+∞) D. [?,+∞)」+ 分母 '2' 得 "
        r"C $=[1,+\infty)$、D $=\left[\frac12,+\infty\right)$，与详解答案 D 一致 ✓。" "\n"
        r"**结构校验**：$g(m)=3m^2-8m-2m^2+4-m^2=-8m+4$ ✓；"
        r"$g(m+1)=3(m^2+2m+1)-(8+2m)(m+1)+4-m^2"
        r"=3m^2+6m+3-2m^2-10m-8+4-m^2=-4m-1$ ✓。"
        r"取 $m=\frac12$：$g(\frac12)=-4+4=0$ ✓ 恰为边界。" "\n"
        r"**注意易错点**：$f$ 为**减**函数，所以 $f(a)\geqslant f(b)\Rightarrow a\leqslant b$（"
        r"用绝对值后），方向别搞反。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-054'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-054-V2',
}

QS = [T053_E1, T053_V1, T053_V2, T053_V3,
      T054_E1, T054_V1, T054_V2]
