# -*- coding: utf-8 -*-
r"""第71批：导数压轴小题（12 题）

来源：2024高中数学热点题型归纳完整解析版.pdf p090-096
M-T-126（4）、M-T-127（2）、M-T-129-V2（1）、M-T-130（3）、M-T-131（2）

## ★★ 12 题我全部独立验算，与原书答案全部吻合

| 题 | 我的验算 | 答案 |
|---|---|---|
| M-T-126-E1 | $x_2\in(-\sqrt2,0)$，$h(x)=xe^x$ 极小 $h(-1)=-\frac1{\mathrm e}$，$a=3/\mathrm e$ 可达到 | **B** |
| M-T-126-V1 | $a<0$ 且 $f(\frac2a)=1-\frac4{a^2}>0$ ⟹ $a<-2$；$a<-2$ 时负半轴无零点 | **B** |
| M-T-126-V2 | $3t^2+mt-2m^2=0$ 两根 $-m,\frac{2m}3$；$-\frac2{\mathrm e}<\frac{2m}3<0$ ⟹ 值 $-m\in(0,\frac3{\mathrm e})$ | **B** |
| M-T-126-V3 | ⭐ $x_1x_2=a$ 且 $f(x_1)=f(x_2)$，$x_1\ne x_2$ 时乘积取遍 $(\mathrm e^2,+\infty)$ | **D** |
| M-T-127-E1 | ⭐ 同构 $me^x=e^{x+\ln m}$，$\mathrm e^u+u$ 单增 ⟹ $\ln m>\ln(x+1)-x$，最大值 $0$ | **A** |
| M-T-127-V1 | ⭐ 临界点满足 $x_0\mathrm e^{x_0+1}=1$ ⟹ $f_{\min}=1-x_0-\ln x_0=2$，巧！ | **A** |
| M-T-129-V2 | ⭐ 临界点满足 $x_0\mathrm e^{2x_0}=1$ ⟹ $g_{\min}=\frac{2x_0}{x_0}=2$ | **A** |
| M-T-130-E1 | $g(x)=\frac{1-m-2\ln x}{x^2}$ 需单减 ⟹ $m\le2-2\ln x$，最小 $4$ | **B** |
| M-T-130-V1 | ⭐ $t=x\mathrm e^{1-x}$（不是 $e^{-2x}$！），$t_1<0<t_2<1$ ⟹ $-\frac12<a<1$ | **A** |
| M-T-130-V2 | $a\ln x-2x$ 单减 ⟹ $a\le2x$ ⟹ $a\le2$ | **C** |
| M-T-131-E1 | $a<(x+1)^2+\frac{16}{x+1}$，极小在 $x=1$，$g=12$ | **B** |
| M-T-131-V1 | ⭐ $x^{-3}\mathrm e^x=\mathrm e^{x-3\ln x}\ge x-3\ln x+1$ ⟹ 比值 $\ge-3$，且可取等 | **D** |

## 本批最关键的还原：M-T-130-V1 的 $ex$ 是 $e\cdot x$ 不是 $e^x$

题面 OCR 成 `f(x) = (aex + ex)(ex + ex)`。若按 $e^x$ 理解：

$$t=\mathrm e^{-2x}\in(0,+\infty)\ \text{单调}\ \Rightarrow\ \text{每个正根只给 1 个交点，最多 2 个}$$

**与「恰有三个公共点」矛盾**。

按 $f(x)=(a\mathrm e^x+ex)(\mathrm e^x+ex)$ 理解，除以 $\mathrm e^{2x}$ 得 $t=\frac{ex}{\mathrm e^x}=x\mathrm e^{1-x}$，
它在 $(-\infty,1)$ 单增到最大值 $1$、在 $(1,+\infty)$ 单减到 $0$，与详解描述的
「$x<1$ 递增且 $h\in(-\infty,1)$；$x>1$ 递减且 $h\in(0,1)$」**完全吻合** ✓

## 两处漂亮的「极值恰好是整数」

**M-T-127-V1**：临界点满足 $\mathrm e^{x_0+1}=\frac1{x_0}$，即 $\ln x_0=-x_0-1$，于是
$$f_{\min}=x_0\mathrm e^{x_0+1}-x_0-\ln x_0=1-x_0-(-x_0-1)=2$$
**$x_0$ 恰好消掉** —— 这是命题人刻意设计，不用真的解出 $x_0$。

**M-T-129-V2**：同理，临界条件 $2x_0^2\mathrm e^{2x_0}+\ln x_0=0$ 等价于 $x_0\mathrm e^{2x_0}=1$（此时 $2x_0=-\ln x_0$），
$$g_{\min}=\frac{x_0\mathrm e^{2x_0}-\ln x_0-1}{x_0}=\frac{1+2x_0-1}{x_0}=2$$
"""

T126_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知函数 $f(x)=(x^{2}-2x)\mathrm e^{x}$，若方程 $f(x)=a$ 有 $3$ 个不同的实根"
        r"$x_1,x_2,x_3\ (x_1<x_2<x_3)$，则 $\dfrac{a}{x_2-2}$ 的取值范围是（　　）"
    ),
    'opts': [
        ('A', r"$\left(-\dfrac{2}{\mathrm e^{2}},0\right)$"),
        ('B', r"$\left[-\dfrac1{\mathrm e},0\right)$"),
        ('C', r"$\left(-\dfrac{2}{\mathrm e^{2}},2\mathrm e^{2}\right)$"),
        ('D', r"$\left(0,2\mathrm e^{2}\right)$"),
    ],
    'answer': 'B',
    'analysis': (
        r"先由图象定出 $a>0$ 与 $x_2\in(-\sqrt2,0)$，再用 $f(x_2)=a$ 把所求式化成 $x_2\mathrm e^{x_2}$，"
        r"转化为 $h(x)=x\mathrm e^x$ 在 $(-\sqrt2,0)$ 上的值域。"
    ),
    'solution': (
        r"$f'(x)=\mathrm e^{x}(x^{2}-2x)+\mathrm e^{x}(2x-2)=\mathrm e^{x}(x^{2}-2)$，令 $f'(x)=0$ 得 $x=\pm\sqrt2$。" "\n"
        r"$f$ 在 $(-\infty,-\sqrt2)$ 递增、$(-\sqrt2,\sqrt2)$ 递减、$(\sqrt2,+\infty)$ 递增；" "\n"
        r"$f(-\sqrt2)=(2+2\sqrt2)\mathrm e^{-\sqrt2}>0$，$f(\sqrt2)=(2-2\sqrt2)\mathrm e^{\sqrt2}<0$，且 $x\to-\infty$ 时 $f\to0^{+}$。" "\n"
        r"要有 $3$ 个不同实根，需 $a\in\left(0,(2+2\sqrt2)\mathrm e^{-\sqrt2}\right)$，此时 $x_2\in(-\sqrt2,0)$（因 $f(0)=0$ 且 $f$ 递减）。" "\n"
        r"由 $f(x_2)=a$ 得 $a=(x_2^{2}-2x_2)\mathrm e^{x_2}=x_2(x_2-2)\mathrm e^{x_2}$，于是" "\n"
        r"$\dfrac{a}{x_2-2}=x_2\mathrm e^{x_2}$。" "\n"
        r"令 $h(x)=x\mathrm e^{x}$，$x\in(-\sqrt2,0)$，则 $h'(x)=\mathrm e^{x}(x+1)$，驻点 $x=-1$。" "\n"
        r"$h$ 在 $(-\sqrt2,-1)$ 递减、$(-1,0)$ 递增，故 $h_{\min}=h(-1)=-\dfrac1{\mathrm e}$（可取到）；" "\n"
        r"又 $h(-\sqrt2)=-\sqrt2\mathrm e^{-\sqrt2}<h(0)=0$，故 $h(x)<0$。" "\n"
        r"所以 $\dfrac{a}{x_2-2}\in\left[-\dfrac1{\mathrm e},0\right)$。故选 B。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p091 详解：「$f'(x)=\mathrm e^x(x^2-2)$，令 $f'(x)=0$ 解得 $x=\pm\sqrt2$…" "\n"
        r"故若方程 $f(x)=a$ 有 3 个不同的实根，则 $a\in(0,\frac{2+2\sqrt2}{\mathrm e^{\sqrt2}})$，又因为 $f(x_2)=(x_2^2-2x_2)\mathrm e^{x_2}=a$，$x_2\in(-\sqrt2,0)$，" "\n"
        r"故 $\frac a{x_2-2}=x_2\mathrm e^{x_2}$，令 $h(x)=x\mathrm e^x$，$x\in(-\sqrt2,0)$，$h'(x)=\mathrm e^x(x+1)$，令 $h'(x)=0$ 解得 $x=-1$…" "\n"
        r"$h(x)_{\min}=h(-1)=-\frac1{\mathrm e}$，又 $h(-\sqrt2)=-\frac{\sqrt2}{\mathrm e^{\sqrt2}}<h(0)=0$，故 $h(x)<0$，则 $h(x)\in[-\frac1{\mathrm e},0)$，" "\n"
        r"即 $\frac a{x_2-2}\in[-\frac1{\mathrm e},0)$。故选：B」" "\n"
        r"—— **$x=\pm\sqrt2$、$x_2\in(-\sqrt2,0)$、$\frac a{x_2-2}=x_2\mathrm e^{x_2}$、$h(-1)=-\frac1{\mathrm e}$、答案 B 全部与我的推导一致** ✓✓✓" "\n"
        r"（⚠ 选项 B 的 bracket 在提取中丢失，我按详解的 $[-\frac1{\mathrm e},0)$ 录入 —— **左端闭**：$x=-1$ 在区间内且可达到）" "\n"
        r"**独立验算**：" "\n"
        r"① **$f'(x)=\mathrm e^x(x^2-2)$**：$(2x-2)\mathrm e^x+(x^2-2x)\mathrm e^x=\mathrm e^x(x^2-2)$ ✓✓✓" "\n"
        r"② **$f(-\sqrt2)=(2+2\sqrt2)\mathrm e^{-\sqrt2}$**：$(-\sqrt2)^2-2(-\sqrt2)=2+2\sqrt2=4.8284$，$\mathrm e^{-1.4142}=0.24312$，$f=1.1738$ ✓✓✓" "\n"
        r"③ **$a=3/\mathrm e$（对应 $x_2=-1$）可行**：$f(-1)=(1+2)\mathrm e^{-1}=\frac3{\mathrm e}=1.1036<1.1738$ ✓✓✓ **在 $(0,1.1738)$ 内**" "\n"
        r"④ **此时 $x_1,x_3$ 存在**：$f(x)=1.1036$ 在 $(-\infty,-\sqrt2)$ 上（$f$ 从 $0^+$ 增到 $1.1738$）有一根 ✓；" "\n"
        r"在 $(\sqrt2,+\infty)$ 上（$f$ 从 $f(\sqrt2)=(2-2.8284)\mathrm e^{1.4142}=-0.8284(4.1131)=-3.4065$ 增到 $+\infty$）有一根 ✓ ✓✓✓ **共 3 根**" "\n"
        r"⑤ **所求值**：$\frac a{x_2-2}=\frac{1.1036}{-3}=-0.3679=-\frac1{\mathrm e}$ ✓✓✓ **恰为左端点**" "\n"
        r"⑥ **$h(-\sqrt2)$ 与 $h(0)$**：$h(-\sqrt2)=-1.4142(0.24312)=-0.34384$；$h(0)=0$。" "\n"
        r"$-0.34384>-0.3679$ ✓ 故最小值确为 $h(-1)$，且上界 $0$ 取不到 ✓✓✓" "\n"
        r"⑦ **选项排除**：A $(-\frac2{\mathrm e^2},0)=(-0.2707,0)$ **不含 $-\frac1{\mathrm e}=-0.3679$** ✗；" "\n"
        r"C、D 含正数，而 $h(x)<0$ ✗ ✓✓✓" "\n"
        r"**答案 B 正确** ✓" "\n"
        r"**⭐⭐ 通法（三根问题 ⟹ 用根自身表示参数）**：" "\n"
        r"① ⭐⭐ **不要去解 $a$，而是用 $f(x_2)=a$ 把 $a$ 替换掉** —— " "\n"
        r"本题 $\frac a{x_2-2}=\frac{x_2(x_2-2)\mathrm e^{x_2}}{x_2-2}=x_2\mathrm e^{x_2}$，**因式 $(x_2-2)$ 正好约掉**，这是命题人设计好的；" "\n"
        r"② ⭐ **$3$ 个根 ⟹ $a$ 介于极大值与极小值之间**，且 $x_2$ 落在哪个区间要由 $f$ 的符号确定（本题 $f(0)=0$ ⟹ $x_2<0$）；" "\n"
        r"③ ⭐ **$h(x)=x\mathrm e^x$ 的经典值域**：$h'(x)=\mathrm e^x(x+1)$，极小值 $h(-1)=-\frac1{\mathrm e}$ —— **必背**；" "\n"
        r"④ ⚠ **左端闭、右端开**：$x=-1$ 在区间内部故最小值可取（闭），$x\to0$ 是区间端点故 $0$ 取不到（开）；" "\n"
        r"⑤ 检验：**取 $x_2=-1$ 反算出 $a=\frac3{\mathrm e}$，验证它确实产生 3 个根** ✓。"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-126'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-126-E1',
}

T126_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知 $f(x)=ax^{3}-3x^{2}+1$，若 $f(x)$ 存在唯一的零点 $x_0$，且 $x_0>0$，则 $a$ 的取值范围是（　　）"
    ),
    'opts': [
        ('A', r"$(2,+\infty)$"),
        ('B', r"$(-\infty,-2)$"),
        ('C', r"$(1,+\infty)$"),
        ('D', r"$(-\infty,1)$"),
    ],
    'answer': 'B',
    'analysis': (
        r"分类讨论 $a=0$、$a>0$、$a<0$。$a>0$ 时 $x\to-\infty$ 有 $f\to-\infty$ 而 $f(0)=1>0$，必有负零点，舍去；"
        r"$a<0$ 时极小值 $f(\frac2a)=1-\frac4{a^2}>0$ ⟹ $a<-2$。"
    ),
    'solution': (
        r"**$a=0$**：$f(x)=-3x^{2}+1=0$ 得 $x=\pm\frac{\sqrt3}3$，两个零点，舍去。" "\n"
        r"**$a>0$**：$f'(x)=3ax^{2}-6x=3ax\left(x-\dfrac2a\right)$，驻点 $x=0$ 与 $x=\dfrac2a>0$。" "\n"
        r"$f$ 在 $(-\infty,0)$ 递增、$(0,\frac2a)$ 递减、$(\frac2a,+\infty)$ 递增。" "\n"
        r"因 $x\to-\infty$ 时 $f\to-\infty$，而 $f(0)=1>0$，故存在 $x<0$ 使 $f(x)=0$，" "\n"
        r"与「唯一零点且 $x_0>0$」矛盾，舍去。" "\n"
        r"**$a<0$**：驻点 $x=0$ 与 $x=\dfrac2a<0$。$f$ 在 $(-\infty,\frac2a)$ 递减、$(\frac2a,0)$ 递增、$(0,+\infty)$ 递减。" "\n"
        r"$f(0)=1>0$，$x\to+\infty$ 时 $f\to-\infty$，故在 $(0,+\infty)$ 上**恰有 $1$ 个零点**。" "\n"
        r"要使它是唯一的，需负半轴上无零点，即极小值 $f\left(\dfrac2a\right)>0$：" "\n"
        r"$f\left(\dfrac2a\right)=a\cdot\dfrac8{a^{3}}-3\cdot\dfrac4{a^{2}}+1=\dfrac8{a^{2}}-\dfrac{12}{a^{2}}+1=1-\dfrac4{a^{2}}>0$" "\n"
        r"$\Rightarrow a^{2}>4$，结合 $a<0$ 得 $a<-2$。" "\n"
        r"故选 B。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p091 详解：「当 $a=0$ 时，$f(x)=-3x^2+1=0$，解得 $x=\pm\frac{\sqrt3}3$，函数 $f(x)$ 有两个零点，不符合题意…" "\n"
        r"当 $a>0$ 时…∵$x\to-\infty$，$f(x)\to-\infty$，而 $f(0)=1>0$，∴存在 $x<0$ 使得 $f(x)=0$，不符合条件…应舍去；" "\n"
        r"当 $a<0$ 时…而 $f(0)=1>0$，$x\to+\infty$ 时 $f(x)\to-\infty$，∴存在 $x_0>0$ 使得 $f(x_0)=0$，∵$f(x)$ 存在唯一的零点 $x_0$ 且 $x_0>0$，" "\n"
        r"∴极小值 $f(\frac2a)=a(\frac2a)^3-3(\frac2a)^2+1>0$，化为 $a^2>4$，∵$a<0$，∴$a<-2$，综上 $a$ 的取值范围是 $(-\infty,-2)$。故选:B．」" "\n"
        r"—— **$a=0$ 两零点、$a>0$ 必有负零点、$f(\frac2a)=1-\frac4{a^2}>0$、$a<-2$、答案 B 全部与我的推导一致** ✓✓✓" "\n"
        r"（⚠ 原书首行写「当 $a\ge0$ 时容易判断不符合题意」，但随后仍分 $a=0$、$a>0$ 讨论，以详解正文为准）" "\n"
        r"**独立验算**：" "\n"
        r"① **$f(\frac2a)$**：$a\cdot\frac8{a^3}=\frac8{a^2}$；$3(\frac2a)^2=\frac{12}{a^2}$。故 $f=\frac8{a^2}-\frac{12}{a^2}+1=1-\frac4{a^2}$ ✓✓✓" "\n"
        r"② **$a<-2$ 时负半轴无零点**：极小值 $1-\frac4{a^2}>0$，且 $x\to-\infty$ 时 $f=ax^3\to+\infty$（$a<0$），" "\n"
        r"故 $(-\infty,0)$ 上 $f\ge f(\frac2a)>0$ ✓✓✓ **无零点**" "\n"
        r"③ **$a=-2$ 时**：$f(\frac2a)=f(-1)=1-\frac44=0$，此时 $x=-1$ 是零点（二重），加上正零点共 $2$ 个不同零点 ✗ **故必须严格 $a<-2$** ✓✓✓" "\n"
        r"④ **数值检验（$a=-3$）**：$f(x)=-3x^3-3x^2+1$。" "\n"
        r"$f(-1)=3-3+1=1>0$；$f(-2)=24-12+1=13>0$；$f(0)=1>0$；$f(1)=-3-3+1=-5<0$。" "\n"
        r"极小值点 $x=\frac2a=-0.6667$：$f=-3(-0.2963)-3(0.4444)+1=0.8889-1.3333+1=0.5556>0$ ✓✓✓" "\n"
        r"负半轴恒正 ✓，正半轴由 $f(0)=1$ 递减到 $-\infty$ ⟹ **恰 1 个正零点**（在 $(0,1)$ 内）✓✓✓" "\n"
        r"⑤ **数值检验（$a=-1$，应不满足）**：$f(x)=-x^3-3x^2+1$。$f(\frac2a)=f(-2)=8-12+1=-3<0$。" "\n"
        r"$f(-3)=27-27+1=1>0$，$f(-2)=-3<0$ ⟹ 有负零点 ✗ **不符合** ✓✓✓" "\n"
        r"⑥ **$a>0$ 检验（$a=1$）**：$f(x)=x^3-3x^2+1$，$f(-1)=-1-3+1=-3<0$，$f(0)=1>0$ ⟹ 负零点存在 ✗ ✓✓✓" "\n"
        r"**答案 B 正确** ✓" "\n"
        r"**⭐⭐ 通法（三次函数唯一零点）**：" "\n"
        r"① ⭐⭐ **必须分 $a=0$、$a>0$、$a<0$ 三类** —— $a=0$ 时退化成二次函数，开口向下有两个零点，**不能漏**；" "\n"
        r"② ⭐⭐ **$a>0$ 时用「$x\to-\infty$ 时 $f\to-\infty$ 而 $f(0)=1>0$」秒杀** —— " "\n"
        r"必有负零点，**不用列表**；" "\n"
        r"③ ⭐ **$a<0$ 时关键是极小值 $f(\frac2a)>0$**：因为 $f(0)=1>0$ 且 $x\to+\infty$ 时 $f\to-\infty$，" "\n"
        r"正零点必然存在，**唯一性完全取决于负半轴**；" "\n"
        r"④ ⚠ **端点 $a=-2$ 必须单独排除**：此时极小值 $=0$，$x=-1$ 成为零点，**唯一性被破坏** —— **严格不等号**；" "\n"
        r"⑤ 检验：**取 $a=-3$（满足）与 $a=-1$（不满足）各验一次**，看负半轴有没有零点。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-126'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-126-V1',
}

T126_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知函数 $f(x)=\dfrac{x-2m}{3x^{2}}\ (m<0)$，$g(x)=\dfrac{2\ln(-x)}x$，设方程 $f(g(x))+\dfrac1m=0$ 的 $3$ 个实根"
        r"分别为 $x_1,x_2,x_3$，且 $x_1<x_2<x_3$，则 $g(x_1)+2g(x_2)+3g(x_3)$ 的值可能为（　　）"
    ),
    'opts': [
        ('A', r"$-\dfrac2{\mathrm e}$"),
        ('B', r"$\dfrac2{\mathrm e}$"),
        ('C', r"$-\dfrac3{\mathrm e}$"),
        ('D', r"$\dfrac3{\mathrm e}$"),
    ],
    'answer': 'B',
    'analysis': (
        r"令 $t=g(x)$，方程化为 $3t^{2}+mt-2m^{2}=0$，两根 $t_1=-m>0$、$t_2=\frac{2m}3<0$。"
        r"$g$ 的最小值为 $-\frac2{\mathrm e}$，故需 $-\frac2{\mathrm e}<t_2<0$，得 $-\frac3{\mathrm e}<m<0$，目标式 $=-(m)\in(0,\frac3{\mathrm e})$。"
    ),
    'solution': (
        r"令 $t=g(x)$，由 $f(t)+\dfrac1m=0$ 得 $\dfrac{t-2m}{3t^{2}}+\dfrac1m=0$，" "\n"
        r"去分母：$m(t-2m)+3t^{2}=0$，即 $3t^{2}+mt-2m^{2}=0$。" "\n"
        r"$\Delta=m^{2}+24m^{2}=25m^{2}$，两根 $t=\dfrac{-m\pm5|m|}{6}$。由 $m<0$ 知 $|m|=-m$，" "\n"
        r"$t_1=\dfrac{-m-5m}6=-m>0$，$t_2=\dfrac{-m+5m}6=\dfrac{2m}3<0$。" "\n"
        r"**研究 $g$**：$g(x)=\dfrac{2\ln(-x)}x$，定义域 $(-\infty,0)$。" "\n"
        r"$g'(x)=\dfrac{2\cdot\frac1{-x}\cdot(-1)\cdot x-2\ln(-x)}{x^{2}}=\dfrac{2\left[1-\ln(-x)\right]}{x^{2}}$，" "\n"
        r"驻点 $x=-\mathrm e$。$g$ 在 $(-\infty,-\mathrm e)$ 递减、$(-\mathrm e,0)$ 递增，$g_{\min}=g(-\mathrm e)=-\dfrac2{\mathrm e}$。" "\n"
        r"又 $x\to-\infty$ 时 $g\to0^{-}$，$g(-1)=0$，$x\to0^{-}$ 时 $g\to+\infty$。" "\n"
        r"**计数**：$t_1=-m>0$ 对应 $g(x)=t_1$，在 $(-1,0)$ 上恰 $1$ 根；" "\n"
        r"$t_2=\frac{2m}3<0$ 要给出 $2$ 根，需 $-\dfrac2{\mathrm e}<t_2<0$。" "\n"
        r"（若 $t_2=-\frac2{\mathrm e}$ 只有 $1$ 根，$t_2<-\frac2{\mathrm e}$ 无根。）" "\n"
        r"于是 $-\dfrac2{\mathrm e}<\dfrac{2m}3<0\Rightarrow-\dfrac3{\mathrm e}<m<0$。" "\n"
        r"**目标式**：由 $x_1<x_2<x_3$ 知 $g(x_1)=g(x_2)=t_2$（负的两根较小），$g(x_3)=t_1$。" "\n"
        r"$g(x_1)+2g(x_2)+3g(x_3)=3t_2+3t_1=3\left(\dfrac{2m}3-m\right)=3\left(-\dfrac m3\right)=-m$。" "\n"
        r"由 $-\dfrac3{\mathrm e}<m<0$ 得 $-m\in\left(0,\dfrac3{\mathrm e}\right)$。四个选项中只有 $\dfrac2{\mathrm e}$ 在此区间内。故选 B。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p091-092 详解：「$g'(x)=\frac{2[1-\ln(-x)]}{x^2}$，∴当 $x\in(-\infty,-\mathrm e)$ 时 $g'(x)<0$…" "\n"
        r"当 $x\in(-\mathrm e,0)$ 时 $g'(x)>0$…∴$g(x)\ge g(-\mathrm e)=-\frac2{\mathrm e}$…" "\n"
        r"由 $f(x)+\frac1m=0$ 可得 $3x^2+mx-2m^2=0$ 必有两个不等的实根 $t_1,t_2$ 且 $t_1=-m$、$t_2=\frac{2m}3$（$m<0$），" "\n"
        r"∴令 $t=g(x)$，要使 $f(t)+\frac1m=0$ 有 3 个实根，则 $t_1\in[0,+\infty)$、$t_2\in(-\frac2{\mathrm e},0)$，即 $-\frac2{\mathrm e}<\frac{2m}3<0$，" "\n"
        r"可得 $-\frac3{\mathrm e}<m<0$。∴由 $x_1<x_2<x_3$ 知：$t_2=g(x_1)=g(x_2)$，$t_1=g(x_3)$，∴$g(x_1)+2g(x_2)+3g(x_3)=3(t_1+t_2)=-m\in(0,\frac3{\mathrm e})$。故选：B.」" "\n"
        r"—— **$g_{\min}=-\frac2{\mathrm e}$、$t_1=-m$、$t_2=\frac{2m}3$、$-\frac3{\mathrm e}<m<0$、目标 $=-m\in(0,\frac3{\mathrm e})$、答案 B 全部与我的推导一致** ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **$g'(x)=\frac{2[1-\ln(-x)]}{x^2}$**：$[\frac{2\ln(-x)}x]'=\frac{2\cdot\frac1{-x}\cdot(-1)\cdot x-2\ln(-x)\cdot1}{x^2}=\frac{2-2\ln(-x)}{x^2}$ ✓✓✓" "\n"
        r"② **$g(-\mathrm e)=\frac{2\ln(\mathrm e)}{-\mathrm e}=-\frac2{\mathrm e}$** ✓✓✓" "\n"
        r"③ **两根**：$3t^2+mt-2m^2=0$，$\Delta=m^2+24m^2=25m^2$ ✓；$t=\frac{-m\pm5|m|}{6}$。" "\n"
        r"$m=-1$：$t=\frac{1\pm5}6$ ⟹ $t_1=1$、$t_2=-\frac23$ ✓✓✓（$-m=1$、$\frac{2m}3=-\frac23$ ✓）" "\n"
        r"④ **$m=-1$ 是否可行**：$t_2=-\frac23=-0.6667$，$-\frac2{\mathrm e}=-0.7358$。$-0.7358<-0.6667<0$ ✓✓✓ **可行**" "\n"
        r"目标值 $=-m=1$。区间 $(0,\frac3{\mathrm e})=(0,1.1036)$，$1$ 在其中 ✓✓✓" "\n"
        r"⑤ **计数验（$m=-1$）**：$t_1=1>0$ ⟹ $g(x)=1$：$g$ 在 $(-\mathrm e,0)$ 从 $-\frac2{\mathrm e}$ 增到 $+\infty$，故恰 $1$ 根（在 $(-1,0)$）✓" "\n"
        r"$t_2=-0.6667\in(-\frac2{\mathrm e},0)$ ⟹ $g(x)=-0.6667$：在 $(-\infty,-\mathrm e)$ 上 $g$ 从 $0^-$ 减到 $-\frac2{\mathrm e}$，" "\n"
        r"经过 $-0.6667$ 一次 ✓；在 $(-\mathrm e,0)$ 上从 $-\frac2{\mathrm e}$ 增到 $+\infty$，经过一次 ✓ ⟹ **共 2 根** ✓✓✓ **总计 3 根** ✓" "\n"
        r"⑥ **选项排除**：$-\frac2{\mathrm e}<0$ ✗（目标 $>0$）；$-\frac3{\mathrm e}<0$ ✗；$\frac3{\mathrm e}$ 是**开区间端点取不到** ✗；" "\n"
        r"$\frac2{\mathrm e}=0.7358\in(0,1.1036)$ ✓✓✓" "\n"
        r"（验证 $\frac2{\mathrm e}$ 可达：需 $-m=\frac2{\mathrm e}$ 即 $m=-\frac2{\mathrm e}$，则 $t_2=\frac{2m}3=-\frac4{3\mathrm e}=-0.4905\in(-0.7358,0)$ ✓✓✓）" "\n"
        r"**答案 B 正确** ✓" "\n"
        r"**⭐⭐ 通法（复合方程 $f(g(x))=c$ 的根计数）**：" "\n"
        r"① ⭐⭐ **换元 $t=g(x)$，先解外层方程得 $t_1,t_2$，再数每个 $t_i$ 对应几个 $x$** —— " "\n"
        r"**总根数 = 各 $t_i$ 对应 $x$ 的个数之和**，这是处理复合方程的标准流程；" "\n"
        r"② ⭐⭐ **$g(x)=\frac{\ln(\pm x)}{x}$ 型的值域：$g'(x)=\frac{1-\ln(\pm x)}{x^2}$，极值在 $x=\pm\mathrm e$，极值 $=\pm\frac1{\mathrm e}$** —— " "\n"
        r"本题带系数 $2$，极值 $-\frac2{\mathrm e}$；" "\n"
        r"③ ⭐ **数形结合定区间**：$t$ 落在 $(g_{\min},0)$ 时 $2$ 根、$t=g_{\min}$ 时 $1$ 根、$t>0$ 时 $1$ 根 —— **画草图比算快**；" "\n"
        r"④ ⚠ **目标式里 $x_1,x_2,x_3$ 的归属**：负的 $t_2$ 对应较小的两个根，" "\n"
        r"故 $g(x_1)=g(x_2)=t_2$、$g(x_3)=t_1$，**顺序搞反结果完全不同**；" "\n"
        r"⑤ 检验：**取 $m=-1$ 完整数一遍根的个数**（$1+2=3$ ✓），并**验证 $\frac2{\mathrm e}$ 对应的 $m$ 可行**。"
    ),
    'difficulty': 0.95,
    'topics': ['M-T-126'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-126-V2',
}

T126_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知函数 $f(x)=\dfrac{\ln x}x$，对于正实数 $a$，若关于 $t$ 的方程 $f(t)=f\left(\dfrac at\right)$"
        r"恰有三个不同的正实数根，则 $a$ 的取值范围是（　　）"
    ),
    'opts': [
        ('A', r"$(1,8)$"),
        ('B', r"$(\mathrm e^{2},8)$"),
        ('C', r"$(8,+\infty)$"),
        ('D', r"$(\mathrm e^{2},+\infty)$"),
    ],
    'answer': 'D',
    'analysis': (
        r"令 $x_1=t$、$x_2=\frac at$，则 $x_1x_2=a$ 且 $f(x_1)=f(x_2)$。$x_1=x_2$ 时给出 $t=\sqrt a$（恒有 $1$ 根）；"
        r"$x_1\ne x_2$ 时需一在 $(1,\mathrm e)$、一在 $(\mathrm e,+\infty)$，其乘积取遍 $(\mathrm e^{2},+\infty)$。"
    ),
    'solution': (
        r"记 $x_1=t$、$x_2=\dfrac at>0$，则 $x_1x_2=a$，条件为 $f(x_1)=f(x_2)$，即 $\dfrac{\ln x_1}{x_1}=\dfrac{\ln x_2}{x_2}$。" "\n"
        r"$f'(x)=\dfrac{1-\ln x}{x^{2}}$，故 $f$ 在 $(0,\mathrm e)$ 递增、$(\mathrm e,+\infty)$ 递减，$f(\mathrm e)=\dfrac1{\mathrm e}$ 为最大值；" "\n"
        r"$f(1)=0$，$0<x<1$ 时 $f(x)<0$，$x>1$ 时 $f(x)>0$，$x\to+\infty$ 时 $f\to0^{+}$。" "\n"
        r"**情形一：$x_1=x_2$**。此时 $t=\dfrac at$，即 $t=\sqrt a$，恒给出 $1$ 个正根。" "\n"
        r"**情形二：$x_1\ne x_2$**。由 $f$ 的单峰性，两根必分居 $\mathrm e$ 两侧，且都在 $(1,+\infty)$ 内（因 $f>0$）。" "\n"
        r"设 $x_1\in(1,\mathrm e)$、$x_2\in(\mathrm e,+\infty)$，则 $a=x_1x_2$。" "\n"
        r"当 $x_1\to1^{+}$ 时 $f(x_1)\to0^{+}$，对应的 $x_2\to+\infty$，故 $a\to+\infty$；" "\n"
        r"当 $x_1\to\mathrm e^{-}$ 时 $x_2\to\mathrm e^{+}$，故 $a\to\mathrm e^{2}$。由连续性，$a$ 取遍 $(\mathrm e^{2},+\infty)$。" "\n"
        r"对每个这样的 $a$，恰有一对 $\{x_1,x_2\}$，给出 $2$ 个不同的 $t$（$t=x_1$ 与 $t=x_2$）。" "\n"
        r"因此：当 $a\in(\mathrm e^{2},+\infty)$ 时共有 $1+2=3$ 个正根；当 $a\le\mathrm e^{2}$ 时只有 $t=\sqrt a$ 这 $1$ 个根。" "\n"
        r"故 $a\in(\mathrm e^{2},+\infty)$。选 D。"
    ),
    'review': (
        r"★ 题干、答案完整 ✓。原书 p092 详解：「因为 $f(x)=\frac{\ln x}x$，$f'(x)=\frac{1-\ln x}{x^2}$…" "\n"
        r"所以 $f(x)$ 在区间 $(0,\mathrm e)$ 单调递增，在 $(\mathrm e,+\infty)$ 单调递减…" "\n"
        r"令 $x_1=t$，$x_2=\frac at$，则 $f(x_1)=f(x_2)$，且 $x_1,x_2>1$，" "\n"
        r"①当 $x_1=x_2$ 时，$t=\frac at$，$t=\sqrt a$，成立，所以 $\sqrt a$ 是方程的一个实数根；" "\n"
        r"②当 $x_1\ne x_2$ 时…令 $\frac{\ln x_1}{x_1}=\frac{\ln x_2}{x_2}=m$…所以 $\frac{x_1-x_2}{\ln x_1-\ln x_2}=\frac{x_1+x_2}{\ln x_1+\ln x_2}$…」" "\n"
        r"（详解后半段及选项提取破碎，但**答案 D 与我的推导一致** ✓）" "\n"
        r"**独立验算（数值，完全独立）**：" "\n"
        r"① **$f'(x)=\frac{1-\ln x}{x^2}$**：$[\ln x\cdot x^{-1}]'=\frac1x\cdot\frac1x+\ln x\cdot(-\frac1{x^2})=\frac{1-\ln x}{x^2}$ ✓✓✓" "\n"
        r"$f$ 在 $(0,\mathrm e)$ 增、$(\mathrm e,+\infty)$ 减，最大值 $f(\mathrm e)=\frac1{\mathrm e}$ ✓✓✓" "\n"
        r"② **取 $a=\mathrm e^3=20.0855$（应在范围内）**，解 $f(t)=f(a/t)$：" "\n"
        r"显然 $t=\sqrt a=4.4817$ 是一根。找另外两根：需 $x_1x_2=20.0855$ 且 $f(x_1)=f(x_2)$。" "\n"
        r"试 $x_1=2$：$f(2)=\frac{0.6931}2=0.34657$。需 $f(x_2)=0.34657$ 且 $x_2> \mathrm e$：试 $x_2=4$：$f(4)=\frac{1.3863}4=0.34657$ ✓✓✓ **相等！**" "\n"
        r"乘积 $=2\times4=8\ne20.0855$，所以这对对应 $a=8$。" "\n"
        r"验 $a=8$：$t=\sqrt8=2.8284$；$t=2$ ⟹ $\frac at=4$，$f(2)=f(4)$ ✓；$t=4$ ⟹ $\frac at=2$，$f(4)=f(2)$ ✓ ⟹ **共 3 根** ✓✓✓" "\n"
        r"且 $8>\mathrm e^2=7.3891$ ✓✓✓ **与「$a>\mathrm e^2$」吻合**" "\n"
        r"③ **取 $a=20.0855$ 找配对**：需 $x_1x_2=20.0855$、$f(x_1)=f(x_2)$。" "\n"
        r"试 $x_1=1.5$：$f=0.40546/1.5=0.27031$。解 $f(x_2)=0.27031$（$x_2>\mathrm e$）：" "\n"
        r"$x_2=6$：$f=\frac{1.7918}6=0.29863$ 偏大；$x_2=7$：$\frac{1.9459}7=0.27799$；$x_2=8$：$\frac{2.0794}8=0.25993$。" "\n"
        r"插值得 $x_2\approx7.42$：$f=\frac{2.0042}{7.42}=0.27011$ ✓ 接近。乘积 $=1.5\times7.42=11.13$。" "\n"
        r"试 $x_1=1.2$：$f=0.18232/1.2=0.15193$。$x_2$：$x_2=15$：$f=\frac{2.708}{15}=0.18053$；$x_2=20$：$\frac{2.9957}{20}=0.14979$。" "\n"
        r"$x_2\approx19.5$：$f=\frac{2.9704}{19.5}=0.15233$ ✓。乘积 $=1.2\times19.5=23.4$。" "\n"
        r"故 $a=20.0855$ 的配对在 $x_1\in(1.2,1.5)$ 之间，**存在** ✓✓✓ ⟹ $a=20.0855$ 有 3 根 ✓" "\n"
        r"④ **$a=\mathrm e^2=7.3891$（边界，应不取）**：配对需 $x_1=x_2=\mathrm e$，与 $t=\sqrt a=\mathrm e$ 重合 ⟹ **只有 1 根** ✗ ✓✓✓ **故开区间**" "\n"
        r"⑤ **$a=4<\mathrm e^2$**：$t=\sqrt4=2$。需 $x_1x_2=4$ 且 $f(x_1)=f(x_2)$、$x_1\ne x_2$：" "\n"
        r"若 $x_1<\mathrm e<x_2$ 且 $x_1x_2=4$ ⟹ $x_2=4/x_1$，需 $x_1<\mathrm e$ 且 $4/x_1>\mathrm e$ ⟹ $x_1<4/\mathrm e=1.4715$。" "\n"
        r"验 $x_1=1.4715$：$f=0.38629/1.4715=0.26251$；$x_2=\mathrm e$：$f=0.36788$。**不相等** ✗" "\n"
        r"验 $x_1\to1$：$f\to0$，$x_2\to4$，$f(4)=0.34657\ne0$ ✗。故无配对 ⟹ **1 根** ✓✓✓" "\n"
        r"⑥ **选项排除**：A $(1,8)$ 含 $a=4$（只有 1 根）✗；B $(\mathrm e^2,8)$ 上界错（$a=20$ 也行）✗；" "\n"
        r"C $(8,+\infty)$ 下界错（$a=7.5$ 也行）✗ ✓✓✓" "\n"
        r"**答案 D 正确** ✓" "\n"
        r"**⭐⭐ 通法（$f(x_1)=f(x_2)$ 型 ⟹ 转化为乘积范围）**：" "\n"
        r"① ⭐⭐ **设 $x_1=t$、$x_2=\frac at$，则问题变成「$x_1x_2=a$ 且 $f(x_1)=f(x_2)$ 有几组解」** —— " "\n"
        r"**把方程根的个数转化为「满足等值条件的数对个数」**；" "\n"
        r"② ⭐⭐ **单峰函数 $f$ 上 $f(x_1)=f(x_2)$ 的解对：一左一右，参数化后乘积是单调的** —— " "\n"
        r"本题 $x_1\to1^+$ 时 $x_2\to+\infty$（乘积 $\to\infty$），$x_1\to\mathrm e^-$ 时 $x_2\to\mathrm e^+$（乘积 $\to\mathrm e^2$）；" "\n"
        r"③ ⭐ **$x_1=x_2$ 永远给出 $t=\sqrt a$ 这一个根**，所以「恰 3 根」⟺「异根解对恰 1 组」；" "\n"
        r"④ ⚠ **边界 $a=\mathrm e^2$ 要单独看**：此时异根解对退化成 $x_1=x_2=\mathrm e$，与 $\sqrt a$ 重合，**只剩 1 根** ⟹ 开区间；" "\n"
        r"⑤ 检验：**$a=8$ 时 $f(2)=f(4)=0.34657$ 精确相等**，是完美的数值锚点 ✓。"
    ),
    'difficulty': 0.95,
    'topics': ['M-T-126'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-126-V3',
}

T127_E1 = {
    'type': '选择',
    'stem_text': (
        r"定义：设函数 $y=f(x)$ 在 $(a,b)$ 上的导函数为 $f'(x)$，若 $f'(x)$ 在 $(a,b)$ 上可导，则称 $y=f(x)$ 在 $(a,b)$ 上"
        r"存在二阶导函数。若在区间 $(a,b)$ 上 $f''(x)>0$，则称 $y=f(x)$ 在 $(a,b)$ 上为「凹函数」。"
        r"已知 $f(x)=m\mathrm e^{x}+\dfrac{(x+1)^{2}}4\left[1+2\ln m-2\ln(x+1)\right]+x$ 在 $(-1,+\infty)$ 上为「凹函数」，"
        r"则实数 $m$ 的取值范围为（　　）"
    ),
    'opts': [
        ('A', r"$(1,+\infty)$"),
        ('B', r"$(\sqrt{\mathrm e},+\infty)$"),
        ('C', r"$(\mathrm e,+\infty)$"),
        ('D', r"$(\sqrt{\mathrm e},\mathrm e)$"),
    ],
    'answer': 'A',
    'analysis': (
        r"求出 $f''(x)=m\mathrm e^{x}+\ln m-\ln(x+1)-1>0$，同构为 $\mathrm e^{x+\ln m}+(x+\ln m)>\mathrm e^{\ln(x+1)}+\ln(x+1)$，"
        r"利用 $g(u)=\mathrm e^{u}+u$ 单调递增得 $\ln m>\ln(x+1)-x$，而后者最大值是 $0$。"
    ),
    'solution': (
        r"记 $A=\dfrac{(x+1)^{2}}4$、$B=1+2\ln m-2\ln(x+1)$，则 $f(x)=m\mathrm e^{x}+AB+x$。" "\n"
        r"$A'=\dfrac{x+1}2$，$B'=-\dfrac2{x+1}$，于是" "\n"
        r"$A'B=\dfrac{x+1}2\left[1+2\ln m-2\ln(x+1)\right]=(x+1)\left[\dfrac12+\ln m-\ln(x+1)\right]$，$AB'=-\dfrac{x+1}2$。" "\n"
        r"$f'(x)=m\mathrm e^{x}+(x+1)\left[\ln m-\ln(x+1)\right]+1$。" "\n"
        r"$f''(x)=m\mathrm e^{x}+\left[\ln m-\ln(x+1)\right]+(x+1)\cdot\left(-\dfrac1{x+1}\right)=m\mathrm e^{x}+\ln m-\ln(x+1)-1$。" "\n"
        r"条件为 $m\mathrm e^{x}+\ln m>\ln(x+1)+1$ 对一切 $x>-1$ 成立。注意到" "\n"
        r"$m\mathrm e^{x}=\mathrm e^{x+\ln m}$，$\ln(x+1)+1=\ln(x+1)+(x+1)-\ x=\mathrm e^{\ln(x+1)}+\ln(x+1)-x$…" "\n"
        r"更直接地，两边同加 $x$：等价于" "\n"
        r"$\mathrm e^{x+\ln m}+(x+\ln m)>\ln(x+1)+(x+1)=\mathrm e^{\ln(x+1)}+\ln(x+1)$。" "\n"
        r"令 $g(u)=\mathrm e^{u}+u$，则 $g'(u)=\mathrm e^{u}+1>0$，$g$ 严格递增，故" "\n"
        r"$x+\ln m>\ln(x+1)$，即 $\ln m>\ln(x+1)-x$。" "\n"
        r"令 $h(x)=\ln(x+1)-x$（$x>-1$），$h'(x)=\dfrac1{x+1}-1=-\dfrac x{x+1}$。" "\n"
        r"$h$ 在 $(-1,0)$ 递增、$(0,+\infty)$ 递减，$h_{\max}=h(0)=0$。" "\n"
        r"故需 $\ln m>0$，即 $m>1$。故选 A。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p092 详解：「$f'(x)=m\mathrm e^x+(x+1)[\ln m-\ln(x+1)]+1$，$f''(x)=m\mathrm e^x+\ln m-\ln(x+1)-1$，" "\n"
        r"因为 $f(x)$ 在区间 $(-1,+\infty)$ 上为『凹函数』，所以 $f''(x)=m\mathrm e^x+\ln m-\ln(x+1)-1>0$ 对任意 $x\in(-1,+\infty)$ 都成立，" "\n"
        r"因为 $m\mathrm e^x+\ln m-\ln(x+1)-1>0$ ⟺ $m\mathrm e^x+\ln m>\ln(x+1)+1$ ⟺ $\mathrm e^{x+\ln m}+(x+\ln m)>\mathrm e^{\ln(x+1)}+\ln(x+1)$，" "\n"
        r"且 $g(x)=\mathrm e^x+x$ 在 $(-\infty,+\infty)$ 是增函数，所以 … ⟺ $x+\ln m>\ln(x+1)$ ⟺ $\ln m>\ln(x+1)-x$，" "\n"
        r"由题意 $\ln m>h(x)=\ln(x+1)-x$ 的最大值，$g(x)=\ln(x+1)-x$，$g'(x)=\frac1{x+1}-1$，" "\n"
        r"$x\in(-1,0)$ 时 $g'(x)>0$，$g(x)$ 单调递增；$x\in(0,+\infty)$ 时 $g'(x)<0$，$g(x)$ 单调递减，$g(x)\le g(0)=0$，" "\n"
        r"即 $\ln m>0$，所以 $m>1$，故选：A」" "\n"
        r"—— **$f''$ 的表达式、同构 $\mathrm e^{x+\ln m}+(x+\ln m)$、$g$ 单增、$h_{\max}=h(0)=0$、$m>1$、答案 A 全部与我的推导一致** ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **$f'(x)$ 的推导**：$A'B+AB'=(x+1)[\frac12+\ln m-\ln(x+1)]-\frac{x+1}2=(x+1)[\ln m-\ln(x+1)]$ ✓✓✓" "\n"
        r"② **$f''(x)$**：$[(x+1)(\ln m-\ln(x+1))]'=(\ln m-\ln(x+1))+(x+1)(-\frac1{x+1})=\ln m-\ln(x+1)-1$ ✓✓✓" "\n"
        r"$f''=m\mathrm e^x+\ln m-\ln(x+1)-1$ ✓✓✓" "\n"
        r"③ **同构**：$m\mathrm e^x=\mathrm e^{x+\ln m}$ ✓✓✓；$\ln(x+1)+1$ 加 $x$ 后 $=\ln(x+1)+(x+1)=\mathrm e^{\ln(x+1)}+\ln(x+1)$ ✓✓✓" "\n"
        r"故不等式加 $x$ 后为 $\mathrm e^{x+\ln m}+(x+\ln m)>\mathrm e^{\ln(x+1)}+\ln(x+1)$ ✓✓✓" "\n"
        r"④ **$h_{\max}$**：$h'(x)=\frac1{x+1}-1=\frac{-x}{x+1}$，$x\in(-1,0)$ 时 $-x>0$、$x+1>0$ ⟹ $h'>0$ ✓；" "\n"
        r"$x>0$ 时 $h'<0$ ✓。$h(0)=\ln1-0=0$ ✓✓✓" "\n"
        r"⑤ **数值检验（$m=2>1$，应满足）**：$\ln m=0.6931$。需 $f''(x)=2\mathrm e^x+0.6931-\ln(x+1)-1>0$。" "\n"
        r"$x=0$：$2(1)+0.6931-0-1=1.6931>0$ ✓" "\n"
        r"$x=-0.5$：$2(0.6065)+0.6931-\ln(0.5)-1=1.2131+0.6931+0.6931-1=1.5993>0$ ✓" "\n"
        r"$x=2$：$2(7.389)+0.6931-\ln3-1=14.778+0.6931-1.0986-1=13.373>0$ ✓" "\n"
        r"$x=-0.9$：$2(0.4066)+0.6931-\ln(0.1)-1=0.8131+0.6931+2.3026-1=2.8088>0$ ✓✓✓ **恒成立**" "\n"
        r"⑥ **数值检验（$m=0.8<1$，不应满足）**：$\ln m=-0.2231$。" "\n"
        r"$x=0$：$0.8-0.2231-0-1=-0.4231<0$ ✗ ✓✓✓ **确实不成立**" "\n"
        r"⑦ **边界 $m=1$**：$\ln m=0$，$f''(0)=1+0-0-1=0$，**不满足 $>0$** ⟹ **严格 $m>1$** ✓✓✓" "\n"
        r"⑧ **选项**：B $\sqrt{\mathrm e}=1.6487$、C $\mathrm e=2.718$、D $(\sqrt{\mathrm e},\mathrm e)$ 都**漏掉了 $1<m\le\sqrt{\mathrm e}$ 的部分**（如 $m=1.2$ 应可行：验 $x=0$：$1.2+0.1823-0-1=0.3823>0$ ✓）✓✓✓" "\n"
        r"**答案 A 正确** ✓" "\n"
        r"**⭐⭐ 通法（同构法：$m\mathrm e^{x}=\mathrm e^{x+\ln m}$）**：" "\n"
        r"① ⭐⭐ **看到 $m\mathrm e^x$ 且 $m>0$，立刻写成 $\mathrm e^{x+\ln m}$** —— " "\n"
        r"这样就与式子另一边的 $\ln(x+1)$ 形成「$u$ 与 $\mathrm e^u$」的对称结构；" "\n"
        r"② ⭐⭐ **$g(u)=\mathrm e^{u}+u$ 严格递增** 是同构法最常用的「载体函数」，" "\n"
        r"凡是能写成 $g(A)>g(B)$ 的，直接脱去 $g$ 得 $A>B$；" "\n"
        r"③ ⭐ **$\ln(x+1)-x\le0$**（即 $\ln u\le u-1$ 取 $u=x+1$）—— 这是**最基本对数不等式**，最大值在 $x=0$ 取到；" "\n"
        r"④ ⚠ **$f''>0$ 是严格不等**：$m=1$ 时在 $x=0$ 处 $f''=0$，**边界必须排除**；" "\n"
        r"⑤ ⚠ **新定义题不必怕**：「凹函数」只是 $f''>0$ 的马甲，**先翻译成常规条件再动手**。"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-127'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-127-E1',
}

T127_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知不等式 $x\mathrm e^{x+1}-x\ge\ln x+2m+3$ 对 $\forall x\in(0,+\infty)$ 恒成立，则 $m$ 取值范围为（　　）"
    ),
    'opts': [
        ('A', r"$m\le-\dfrac12$"),
        ('B', r"$m\ge-\dfrac12$"),
        ('C', r"$m\le-2$"),
        ('D', r"$m>-2$"),
    ],
    'answer': 'A',
    'analysis': (
        r"移项得 $x\mathrm e^{x+1}-x-\ln x\ge2m+3$，求左边最小值。导数为零处满足 $x_0\mathrm e^{x_0+1}=1$，"
        r"即 $\ln x_0=-x_0-1$，代入得最小值恰好为 $2$（$x_0$ 消掉）。"
    ),
    'solution': (
        r"原不等式等价于 $f(x)=x\mathrm e^{x+1}-x-\ln x\ge2m+3$ 对一切 $x>0$ 成立。" "\n"
        r"$f'(x)=\mathrm e^{x+1}+x\mathrm e^{x+1}-1-\dfrac1x=(x+1)\mathrm e^{x+1}-\dfrac{x+1}x=(x+1)\left(\mathrm e^{x+1}-\dfrac1x\right)$。" "\n"
        r"令 $\varphi(x)=\mathrm e^{x+1}-\dfrac1x$，则 $\varphi'(x)=\mathrm e^{x+1}+\dfrac1{x^{2}}>0$，$\varphi$ 在 $(0,+\infty)$ 严格递增，" "\n"
        r"且 $x\to0^{+}$ 时 $\varphi\to-\infty$、$x\to+\infty$ 时 $\varphi\to+\infty$，故存在唯一 $x_0>0$ 使 $\varphi(x_0)=0$。" "\n"
        r"$x\in(0,x_0)$ 时 $f'<0$、$x\in(x_0,+\infty)$ 时 $f'>0$，故 $f_{\min}=f(x_0)$。" "\n"
        r"由 $\mathrm e^{x_0+1}=\dfrac1{x_0}$ 得 $x_0\mathrm e^{x_0+1}=1$，且取对数得 $x_0+1=-\ln x_0$，即 $\ln x_0=-x_0-1$。" "\n"
        r"$f(x_0)=x_0\mathrm e^{x_0+1}-x_0-\ln x_0=1-x_0-(-x_0-1)=2$。" "\n"
        r"（$x_0$ 恰好消掉！）" "\n"
        r"于是需 $2\ge2m+3$，即 $m\le-\dfrac12$。故选 A。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p092 详解：「令 $f(x)=x\mathrm e^{x+1}-x-\ln x\ (x>0)$，" "\n"
        r"$f'(x)=(x+1)\mathrm e^{x+1}-1-\frac1x=(x+1)\mathrm e^{x+1}-\frac1x-1$…而 $g(x)=\mathrm e^{x+1}-\frac1x$ 在 $(0,+\infty)$ 单调递增（增+增），" "\n"
        r"且 $g(1)=\mathrm e^2-1>0$、$g(\frac1{16})=\mathrm e^{\frac{17}{16}}-16<0$，所以 $\exists x_0\in(\frac1{16},1)$（$x_0$ 唯一）使得 $g(x_0)=\mathrm e^{x_0+1}-\frac1{x_0}=0$。" "\n"
        r"则 $x\in(0,x_0)$ 时 $g(x)<0\Rightarrow f'(x)<0$，$f(x)$ 单调递减；$x\in(x_0,+\infty)$ 时 $g(x)>0\Rightarrow f'(x)>0$，$f(x)$ 单调递增。" "\n"
        r"所以 $f(x)_{\min}=f(x_0)=x_0\mathrm e^{x_0+1}-x_0-\ln x_0$…」" "\n"
        r"—— **$\varphi(x)=\mathrm e^{x+1}-\frac1x$ 单增、唯一 $x_0\in(\frac1{16},1)$、$f_{\min}=f(x_0)$ 与我的推导一致** ✓✓✓" "\n"
        r"（详解末尾破碎，但 $\mathrm e^{x_0+1}=\frac1{x_0}$ 已足够推出最小值 $2$）" "\n"
        r"**独立验算（关键：最小值恰好是 $2$）**：" "\n"
        r"① **$f'(x)=(x+1)(\mathrm e^{x+1}-\frac1x)$**：" "\n"
        r"$(x\mathrm e^{x+1})'=\mathrm e^{x+1}+x\mathrm e^{x+1}=(x+1)\mathrm e^{x+1}$ ✓；$(x+\ln x)'=1+\frac1x=\frac{x+1}x$ ✓" "\n"
        r"$f'=(x+1)\mathrm e^{x+1}-\frac{x+1}x=(x+1)(\mathrm e^{x+1}-\frac1x)$ ✓✓✓" "\n"
        r"② **$x_0$ 定位**：解 $x+\ln x+1=0$（等价于 $\mathrm e^{x+1}=\frac1x$）。" "\n"
        r"$x=0.3$：$0.3+(-1.2040)+1=0.0960>0$；$x=0.25$：$0.25-1.3863+1=-0.1363<0$；" "\n"
        r"$x=0.28$：$0.28-1.2730+1=0.0070>0$；$x=0.278$：$0.278-1.2802+1=-0.0022<0$。" "\n"
        r"故 $x_0\approx0.2785$ ✓✓✓ **在 $(\frac1{16},1)=(0.0625,1)$ 内，与详解一致**" "\n"
        r"③ **$f(x_0)=2$ 的数值验证**：$x_0=0.2785$，$\mathrm e^{x_0+1}=\mathrm e^{1.2785}=3.5913$，$\frac1{x_0}=3.5907$ ✓（吻合）" "\n"
        r"$f=x_0\mathrm e^{x_0+1}-x_0-\ln x_0=0.2785(3.5913)-0.2785-(-1.2802)=1.0002-0.2785+1.2802=2.0019\approx2$ ✓✓✓" "\n"
        r"④ **邻域验（确认是最小值）**：$x=0.2$：$f=0.2\mathrm e^{1.2}-0.2-\ln0.2=0.2(3.3201)-0.2+1.6094=0.6640-0.2+1.6094=2.0734>2$ ✓" "\n"
        r"$x=0.5$：$f=0.5\mathrm e^{1.5}-0.5-\ln0.5=0.5(4.4817)-0.5+0.6931=2.2409-0.5+0.6931=2.4340>2$ ✓" "\n"
        r"$x=1$：$f=\mathrm e^2-1-0=7.389-1=6.389>2$ ✓✓✓ **确为最小值**" "\n"
        r"⑤ **结论**：$2m+3\le2$ ⟹ $m\le-\frac12$ ✓✓✓" "\n"
        r"⑥ **检验 $m=-\frac12$**：需 $x\mathrm e^{x+1}-x\ge\ln x+2$。$x=0.2785$：左 $=1.0002-0.2785=0.7217$；右 $=-1.2802+2=0.7198$。" "\n"
        r"$0.7217\ge0.7198$ ✓✓✓ **取等成立**" "\n"
        r"⑦ **检验 $m=0$（应不成立）**：需 $x\mathrm e^{x+1}-x\ge\ln x+3$。$x=0.2785$：左 $0.7217$，右 $=-1.2802+3=1.7198$ ✗ ✓✓✓" "\n"
        r"**答案 A 正确** ✓" "\n"
        r"**⭐⭐ 通法（极值点无法显式求解时的「消元」技巧）**：" "\n"
        r"① ⭐⭐ **当驻点方程解不出时，先设驻点为 $x_0$，把极值写成含 $x_0$ 的式子，再用驻点条件化简** —— " "\n"
        r"本题 $x_0\mathrm e^{x_0+1}=1$ 与 $\ln x_0=-x_0-1$ 两式一用，$x_0$ 立刻消掉，极值 $=\mathbf{2}$；" "\n"
        r"② ⭐⭐ **导数因式分解出 $(x+1)$**：$f'=(x+1)\mathrm e^{x+1}-\frac{x+1}x=(x+1)(\mathrm e^{x+1}-\frac1x)$ —— " "\n"
        r"**提公因式是判断单调区间的关键一步**，不提出来就看不出符号；" "\n"
        r"③ ⭐ **$\varphi(x)=\mathrm e^{x+1}-\frac1x$ 单增**（增+增），所以驻点唯一，极值即最值；" "\n"
        r"④ ⚠ **最后一步别搞反**：$f_{\min}\ge2m+3$ ⟹ $2m+3\le2$ ⟹ $m\le-\frac12$ —— " "\n"
        r"**若错写成 $2m+3\ge2$ 就选 B 了**（$m\ge-\frac12$，正是干扰项）；" "\n"
        r"⑤ 检验：**数值算出 $f(x_0)\approx2.0019$**（舍入误差），并**验邻域两点都 $>2$**。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-127'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-127-V1',
}

T129_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知函数 $f(x)=x\mathrm e^{2x}-1$，不等式 $f(x)\ge mx+\ln x$ 对任意 $x\in(0,+\infty)$ 恒成立，"
        r"则实数 $m$ 的取值范围是（　　）"
    ),
    'opts': [
        ('A', r"$(-\infty,2]$"),
        ('B', r"$[0,2]$"),
        ('C', r"$\left(-\infty,\mathrm e^{2}-1\right)$"),
        ('D', r"$f(x)<0$"),
    ],
    'answer': 'A',
    'analysis': (
        r"分离参数 $m\le\frac{x\mathrm e^{2x}-\ln x-1}x$，求右端最小值。驻点条件 $2x_0^{2}\mathrm e^{2x_0}+\ln x_0=0$ 等价于"
        r"$x_0\mathrm e^{2x_0}=1$（即 $2x_0=-\ln x_0$），代入得最小值恰好为 $2$。"
    ),
    'solution': (
        r"$x\mathrm e^{2x}-1\ge mx+\ln x$ 对一切 $x>0$ 成立，因 $x>0$，分离参数：" "\n"
        r"$m\le\dfrac{x\mathrm e^{2x}-\ln x-1}{x}$ 对一切 $x>0$ 成立。令 $g(x)=\dfrac{x\mathrm e^{2x}-\ln x-1}x$。" "\n"
        r"$g'(x)=\dfrac{\left(\mathrm e^{2x}+2x\mathrm e^{2x}-\frac1x\right)x-\left(x\mathrm e^{2x}-\ln x-1\right)}{x^{2}}=\dfrac{2x^{2}\mathrm e^{2x}+\ln x}{x^{2}}$。" "\n"
        r"令 $h(x)=2x^{2}\mathrm e^{2x}+\ln x$，则 $h'(x)=4(x^{2}+x)\mathrm e^{2x}+\dfrac1x>0$（$x>0$），$h$ 严格递增。" "\n"
        r"又 $x\to0^{+}$ 时 $h\to-\infty$、$x\to+\infty$ 时 $h\to+\infty$，故存在唯一 $x_0$ 使 $h(x_0)=0$。" "\n"
        r"$g$ 在 $(0,x_0)$ 递减、$(x_0,+\infty)$ 递增，$g_{\min}=g(x_0)$。" "\n"
        r"**关键化简**：条件 $2x_0^{2}\mathrm e^{2x_0}+\ln x_0=0$ 即 $2x_0^{2}\mathrm e^{2x_0}=-\ln x_0$。" "\n"
        r"由 $\ln u\le u-1$ 型结构可验证它等价于 $x_0\mathrm e^{2x_0}=1$（此时 $2x_0=-\ln x_0$，" "\n"
        r"代回：$2x_0^{2}\cdot\frac1{x_0}=2x_0=-\ln x_0$ ✓）。" "\n"
        r"于是 $g(x_0)=\dfrac{x_0\mathrm e^{2x_0}-\ln x_0-1}{x_0}=\dfrac{1+2x_0-1}{x_0}=2$。" "\n"
        r"故 $m\le2$。故选 A。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p095 详解：「等价于 $m\le\frac{x\mathrm e^{2x}-\ln x-1}{x}$ 对任意 $x\in(0,+\infty)$ 恒成立，" "\n"
        r"令 $g(x)=\frac{x\mathrm e^{2x}-\ln x-1}{x}$，则 $g'(x)=\frac{2x^2\mathrm e^{2x}+\ln x}{x^2}$，令 $h(x)=2x^2\mathrm e^{2x}+\ln x$，则 $h'(x)=4(x^2+x)\mathrm e^{2x}+\frac1x>0$，" "\n"
        r"∴$h(x)$ 在 $(0,+\infty)$ 单调递增，∵$h(\frac14)=\frac{\mathrm e}8-2\ln2<0$、$h(\frac12)=\frac{\mathrm e}2-\ln2>0$，∴$h(x)$ 存在唯一零点 $x_0$ 且 $x_0\in(\frac14,\frac12)$…" "\n"
        r"∵$2x_0^2\mathrm e^{2x_0}+\ln x_0=0$，即 $2x_0\mathrm e^{2x_0}=-\frac{\ln x_0}{x_0}=\frac1{x_0}\ln\frac1{x_0}=\ln\frac1{x_0}\cdot\mathrm e^{\ln\frac1{x_0}}$，" "\n"
        r"令 $\varphi(x)=x\mathrm e^x$，显然 $\varphi(x)$ 在 $(0,+\infty)$ 单调递增，则 $2x_0=\ln\frac1{x_0}$，即 $\frac1{x_0}=\mathrm e^{2x_0}$，" "\n"
        r"则 $g(x)_{\min}=g(x_0)=\frac{x_0\cdot x_0+2x_0-1}{x_0}$…$=2$，∴$m\le2$，故选：A」" "\n"
        r"—— **$g'(x)=\frac{2x^2\mathrm e^{2x}+\ln x}{x^2}$、$h$ 单增、$2x_0=\ln\frac1{x_0}$、$\frac1{x_0}=\mathrm e^{2x_0}$、最小值 $2$、$m\le2$、答案 A 全部与我的推导一致** ✓✓✓" "\n"
        r"（⚠ 原书 $h(\frac14)=\frac{\mathrm e}8-2\ln2$ 似有笔误，应为 $\frac{\sqrt{\mathrm e}}8-2\ln2$；但 $x_0\in(\frac14,\frac12)$ 与我的数值一致 ✓）" "\n"
        r"（⚠ D 选项 `f(x) < 0` 是提取错乱，实际应为某个区间；它是干扰项，不影响判定）" "\n"
        r"**独立验算**：" "\n"
        r"① **$g'(x)$ 的分子**：$(x\mathrm e^{2x})'=\mathrm e^{2x}+2x\mathrm e^{2x}$；乘 $x$ 得 $x\mathrm e^{2x}+2x^2\mathrm e^{2x}$。" "\n"
        r"$(\ln x)'=\frac1x$，乘 $x$ 得 $1$；常数 $-1$ 导数为 $0$。分子 $=(x\mathrm e^{2x}+2x^2\mathrm e^{2x}-1)-(x\mathrm e^{2x}-\ln x-1)=2x^2\mathrm e^{2x}+\ln x$ ✓✓✓" "\n"
        r"② **$h$ 单增**：$h'=4x\mathrm e^{2x}+4x^2\mathrm e^{2x}+\frac1x=4(x+x^2)\mathrm e^{2x}+\frac1x>0$（$x>0$）✓✓✓" "\n"
        r"③ **$x_0$ 数值**：解 $2x^2\mathrm e^{2x}+\ln x=0$。" "\n"
        r"$x=0.42$：$2(0.1764)\mathrm e^{0.84}+\ln0.42=0.3528(2.3164)+(-0.8675)=0.8173-0.8675=-0.0502<0$" "\n"
        r"$x=0.43$：$2(0.1849)\mathrm e^{0.86}+\ln0.43=0.3698(2.3632)+(-0.8440)=0.8740-0.8440=0.0300>0$" "\n"
        r"故 $x_0\approx0.4268$ ✓✓✓ **在 $(\frac14,\frac12)$ 内，与详解一致**" "\n"
        r"④ **$x_0\mathrm e^{2x_0}=1$ 验证**：$0.4268\cdot\mathrm e^{0.8536}=0.4268(2.3481)=1.0022\approx1$ ✓✓✓" "\n"
        r"$2x_0=0.8536$；$-\ln x_0=-\ln(0.4268)=0.8514$ ✓✓✓ **吻合**" "\n"
        r"⑤ **$g(x_0)=2$ 验证**：$g=\frac{0.4268(2.3481)-(-0.8514)-1}{0.4268}=\frac{1.0022+0.8514-1}{0.4268}=\frac{0.8536}{0.4268}=2.0000$ ✓✓✓" "\n"
        r"⑥ **邻域验**：$x=0.3$：$\mathrm e^{0.6}=1.8221$，$g=\frac{0.3(1.8221)-(-1.2040)-1}{0.3}=\frac{0.5466+1.2040-1}{0.3}=\frac{0.7506}{0.3}=2.502>2$ ✓" "\n"
        r"$x=0.6$：$\mathrm e^{1.2}=3.3201$，$g=\frac{0.6(3.3201)-(-0.5108)-1}{0.6}=\frac{1.9921+0.5108-1}{0.6}=\frac{1.5029}{0.6}=2.505>2$ ✓✓✓" "\n"
        r"⑦ **检验 $m=2$ 可行**：需 $x\mathrm e^{2x}-1\ge2x+\ln x$。$x=0.4268$：左 $=1.0022-1=0.0022$；右 $=0.8536-0.8514=0.0022$ ✓✓✓ **取等**" "\n"
        r"⑧ **$m=2.1$ 不可行**：$x=0.4268$：右 $=2.1(0.4268)-0.8514=0.8963-0.8514=0.0449>0.0022$ ✗ ✓✓✓" "\n"
        r"**答案 A 正确** ✓" "\n"
        r"**⭐⭐ 通法（分离参数后极值点「隐式」的处理）**：" "\n"
        r"① ⭐⭐ **$m\le g(x)$ 恒成立 ⟺ $m\le g_{\min}$** —— 先看能不能分离参数，能分离就先分离；" "\n"
        r"② ⭐⭐ **驻点方程 $2x^2\mathrm e^{2x}+\ln x=0$ 解不出时，观察它是否等价于某个简洁关系**：" "\n"
        r"本题 $\frac1{x_0}=\mathrm e^{2x_0}$（即 $2x_0=\ln\frac1{x_0}$）—— **这类「$x\mathrm e^{kx}=c$」结构是最常见的隐式驻点**；" "\n"
        r"③ ⭐ **把 $2x_0=-\ln x_0$ 与 $x_0\mathrm e^{2x_0}=1$ 同时代入 $g(x_0)$**，分子化成 $1+2x_0-1=2x_0$，除以 $x_0$ 得 $2$ —— " "\n"
        r"**两个式子缺一不可**；" "\n"
        r"④ ⚠ **B 选项 $[0,2]$ 是陷阱**：$m$ 可以取负值且任意小（$m\to-\infty$ 时不等式更易成立），**没有下界**；" "\n"
        r"⑤ 检验：**算出 $x_0\approx0.4268$ 并验证 $g(x_0)=2.0000$**，再验邻域两点 $>2$。"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-129'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-129-V2',
}

T130_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知函数 $f(x)=\dfrac{1-2\ln x}{x^{2}}$ 的定义域为 $\left(0,\dfrac1{\mathrm e}\right]$，若对任意的"
        r"$x_1,x_2\in\left(0,\dfrac1{\mathrm e}\right]$，$\dfrac{\lvert f(x_1)-f(x_2)\rvert}{\lvert x_1-x_2\rvert}>"
        r"m\dfrac{x_1+x_2}{x_1^{2}x_2^{2}}$ 恒成立，则实数 $m$ 的取值范围为（　　）"
    ),
    'opts': [
        ('A', r"$(-\infty,3)$"),
        ('B', r"$(-\infty,4]$"),
        ('C', r"$(-\infty,5)$"),
        ('D', r"$(-\infty,6)$"),
    ],
    'answer': 'B',
    'analysis': (
        r"注意到 $\frac{x_1+x_2}{x_1^2x_2^2}\lvert x_1-x_2\rvert=\left\lvert\frac1{x_1^2}-\frac1{x_2^2}\right\rvert$，"
        r"于是条件等价于 $g(x)=f(x)-\frac m{x^2}$ 在 $(0,\frac1{\mathrm e}]$ 上严格递减，求导得 $m\le2-2\ln x$，最小值为 $4$。"
    ),
    'solution': (
        r"先求导：$f'(x)=\dfrac{-\frac2x\cdot x^{2}-(1-2\ln x)\cdot2x}{x^{4}}=\dfrac{-2x-2x+4x\ln x}{x^{4}}=\dfrac{4(\ln x-1)}{x^{3}}$。" "\n"
        r"在 $\left(0,\frac1{\mathrm e}\right]$ 上 $\ln x\le-1$，故 $f'(x)<0$，$f$ 严格递减。" "\n"
        r"关键变形：$\dfrac{x_1+x_2}{x_1^{2}x_2^{2}}\lvert x_1-x_2\rvert=\dfrac{\lvert x_1^{2}-x_2^{2}\rvert}{x_1^{2}x_2^{2}}=\left\lvert\dfrac1{x_2^{2}}-\dfrac1{x_1^{2}}\right\rvert$。" "\n"
        r"故条件等价于 $\lvert f(x_1)-f(x_2)\rvert>m\left\lvert\dfrac1{x_1^{2}}-\dfrac1{x_2^{2}}\right\rvert$。" "\n"
        r"不妨设 $x_1>x_2$，则 $f(x_1)<f(x_2)$ 且 $\frac1{x_1^{2}}<\frac1{x_2^{2}}$，于是" "\n"
        r"$f(x_2)-f(x_1)>m\left(\dfrac1{x_2^{2}}-\dfrac1{x_1^{2}}\right)$，" "\n"
        r"即 $f(x_2)-\dfrac m{x_2^{2}}>f(x_1)-\dfrac m{x_1^{2}}$。" "\n"
        r"令 $g(x)=f(x)-\dfrac m{x^{2}}=\dfrac{1-m-2\ln x}{x^{2}}$，则需 $g$ 在 $\left(0,\frac1{\mathrm e}\right]$ 上严格递减。" "\n"
        r"$g'(x)=\dfrac{-\frac2x\cdot x^{2}-(1-m-2\ln x)\cdot2x}{x^{4}}=\dfrac{-2x-2x+2mx+4x\ln x}{x^{4}}=\dfrac{2m+4\ln x-4}{x^{3}}$。" "\n"
        r"需 $g'(x)\le0$ 恒成立，即 $2m+4\ln x-4\le0$，$m\le2-2\ln x$。" "\n"
        r"在 $\left(0,\frac1{\mathrm e}\right]$ 上 $\ln x\le-1$，故 $2-2\ln x\ge4$，其最小值为 $4$（在 $x=\frac1{\mathrm e}$ 处）。" "\n"
        r"所以 $m\le4$。故选 B。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p095 详解：「$f'(x)=\frac{4(\ln x-1)}{x^3}$，∵函数 $f(x)$ 的定义域为 $(0,\frac1{\mathrm e}]$，∴$f'(x)<0$，" "\n"
        r"即函数 $f(x)$ 在 $(0,\frac1{\mathrm e}]$ 上单调递减…变形为 $\lvert f(x_1)-f(x_2)\rvert>m\lvert\frac1{x_1^2}-\frac1{x_2^2}\rvert$。" "\n"
        r"不妨设 $x_1>x_2$，则 $f(x_1)-\frac m{x_1^2}<f(x_2)-\frac m{x_2^2}$，令 $g(x)=f(x)-\frac m{x^2}=\frac{1-m-2\ln x}{x^2}$，" "\n"
        r"则 $g'(x)=\frac{-4+2m+4\ln x}{x^3}$…则需 $g'(x)\le0$ 在 $(0,\frac1{\mathrm e}]$ 恒成立，则 $-4+2m+4\ln x\le0$ 恒成立，" "\n"
        r"即 $m\le2-2\ln x$ 在 $(0,\frac1{\mathrm e}]$ 恒成立，所以 $m\le(2-2\ln x)_{\min}=2-2\ln\frac1{\mathrm e}=4$。即实数 $m$ 的取值范围为 $(-\infty,4]$」" "\n"
        r"—— **$f'=\frac{4(\ln x-1)}{x^3}$、$g=\frac{1-m-2\ln x}{x^2}$、$g'=\frac{-4+2m+4\ln x}{x^3}$、$m\le2-2\ln x$、$m\le4$、答案 B 全部与我的推导一致** ✓✓✓" "\n"
        r"（⚠ 选项 A、C、D 在提取中括号类型丢失（都是开区间），但只有 B 是 $4$，**答案判定不受影响** ✓）" "\n"
        r"**独立验算**：" "\n"
        r"① **$f'(x)=\frac{4(\ln x-1)}{x^3}$**：$[(1-2\ln x)x^{-2}]'=-\frac2x\cdot x^{-2}+(1-2\ln x)(-2)x^{-3}$" "\n"
        r"$=-2x^{-3}-2(1-2\ln x)x^{-3}=\frac{-2-2+4\ln x}{x^3}=\frac{4\ln x-4}{x^3}$ ✓✓✓" "\n"
        r"② **恒等变形**：$\frac{x_1+x_2}{x_1^2x_2^2}\lvert x_1-x_2\rvert=\frac{(x_1+x_2)\lvert x_1-x_2\rvert}{x_1^2x_2^2}=\frac{\lvert x_1^2-x_2^2\rvert}{x_1^2x_2^2}$ ✓✓✓" "\n"
        r"$=\lvert\frac1{x_2^2}-\frac1{x_1^2}\rvert$ ✓✓✓" "\n"
        r"③ **$g'(x)=\frac{2m+4\ln x-4}{x^3}$**：$[(1-m-2\ln x)x^{-2}]'=-\frac2x x^{-2}+(1-m-2\ln x)(-2)x^{-3}$" "\n"
        r"$=\frac{-2-2(1-m-2\ln x)}{x^3}=\frac{-2-2+2m+4\ln x}{x^3}$ ✓✓✓ **与详解的 $\frac{-4+2m+4\ln x}{x^3}$ 一致**" "\n"
        r"④ **$2-2\ln x$ 的最小值**：$x\in(0,\frac1{\mathrm e}]$ ⟹ $\ln x\le-1$ ⟹ $-2\ln x\ge2$ ⟹ $2-2\ln x\ge4$ ✓✓✓" "\n"
        r"在 $x=\frac1{\mathrm e}$ 处取到 $4$ ✓✓✓" "\n"
        r"⑤ **数值检验（$m=4$，应临界成立）**：取 $x_1=\frac1{\mathrm e}=0.36788$、$x_2=0.2$。" "\n"
        r"$f(x_1)=\frac{1-2(-1)}{(1/\mathrm e)^2}=\frac3{0.13534}=22.167$；$f(x_2)=\frac{1-2\ln0.2}{0.04}=\frac{1+3.2189}{0.04}=\frac{4.2189}{0.04}=105.47$。" "\n"
        r"左 $=\frac{\lvert22.167-105.47\rvert}{\lvert0.36788-0.2\rvert}=\frac{83.306}{0.16788}=496.2$。" "\n"
        r"右 $=4\cdot\frac{0.36788+0.2}{0.13534\cdot0.04}=4\cdot\frac{0.56788}{0.0054135}=4(104.90)=419.6$。" "\n"
        r"$496.2>419.6$ ✓✓✓ **成立**" "\n"
        r"⑥ **数值检验（$m=5$，应不成立）**：右 $=5(104.90)=524.5>496.2$ ✗ ✓✓✓ **确实失败**" "\n"
        r"⑦ **取 $x_1\to x_2=\frac1{\mathrm e}$ 验证临界**：此时左 $\to\lvert f'(\frac1{\mathrm e})\rvert=\frac{4(-1-1)}{(1/\mathrm e)^3}=8\mathrm e^3=160.69$；" "\n"
        r"右 $\to m\cdot\frac{2/\mathrm e}{(1/\mathrm e)^4}=2m\mathrm e^3$。需 $8\mathrm e^3>2m\mathrm e^3$ ⟹ $m<4$… " "\n"
        r"（严格说取极限时是 $\ge$，故 $m\le4$；题干用严格 $>$ 而 $x_1\ne x_2$ 时恒成立 —— 按原书答案取 $(-\infty,4]$ ✓）" "\n"
        r"**答案 B 正确** ✓" "\n"
        r"**⭐⭐ 通法（双变量差商型不等式 ⟹ 构造单调函数）**：" "\n"
        r"① ⭐⭐ **识别 $\frac{x_1+x_2}{x_1^2x_2^2}\lvert x_1-x_2\rvert=\lvert\frac1{x_1^2}-\frac1{x_2^2}\rvert$** —— " "\n"
        r"这一步把「差商 > 某个对称式」变成「两个同构量的差」，**是整道题的命门**；" "\n"
        r"② ⭐⭐ **统一模式：$\lvert f(x_1)-f(x_2)\rvert>m\lvert\varphi(x_1)-\varphi(x_2)\rvert$ ⟺ $f-m\varphi$ 严格单调** —— " "\n"
        r"**凡是含 $\lvert A(x_1)-A(x_2)\rvert$ 型的恒成立问题，都往「构造 $F=f-m\varphi$ 并讨论单调性」上想**；" "\n"
        r"③ ⭐ **$g'(x)\le0$（可以取等）而非 $<0$**：严格单调递减允许有限个点导数为零，" "\n"
        r"所以最后得到的是 $m\le4$ 的**闭**区间；" "\n"
        r"④ ⚠ **$f$ 自身的单调性要先判断**：本题 $f$ 递减，所以 $x_1>x_2$ 时 $f(x_1)<f(x_2)$，**去绝对值符号时方向别搞反**；" "\n"
        r"⑤ 检验：**取 $x_1=\frac1{\mathrm e}$、$x_2=0.2$ 代入 $m=4$（成立）与 $m=5$（失败）** ✓。"
    ),
    'difficulty': 0.93,
    'topics': ['M-T-130'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-130-E1',
}

T130_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知函数 $f(x)=(a\mathrm e^{x}+ex)(\mathrm e^{x}+ex)$ 与 $g(x)=\mathrm e^{2x}$ 的图象恰有三个不同的公共点"
        r"（其中 $\mathrm e$ 为自然对数的底数），则实数 $a$ 的取值范围是（　　）"
    ),
    'opts': [
        ('A', r"$\left(-\dfrac12,1\right)$"),
        ('B', r"$\left(-\dfrac12,\dfrac{\sqrt2}2\right)$"),
        ('C', r"$\left(\dfrac{\sqrt2}2,1\right)$"),
        ('D', r"$(1,\sqrt2)$"),
    ],
    'answer': 'A',
    'analysis': (
        r"两边同除以 $\mathrm e^{2x}$ 得 $(a+x\mathrm e^{1-x})(1+x\mathrm e^{1-x})=1$。令 $t=x\mathrm e^{1-x}$，"
        r"则 $t^{2}+(a+1)t+a-1=0$。$t=x\mathrm e^{1-x}$ 在 $x=1$ 处取最大值 $1$，结合根的分布得 $t_1<0<t_2<1$。"
    ),
    'solution': (
        r"由 $f(x)=g(x)$ 得 $(a\mathrm e^{x}+ex)(\mathrm e^{x}+ex)=\mathrm e^{2x}$。两边除以 $\mathrm e^{2x}>0$：" "\n"
        r"$\left(a+\dfrac{ex}{\mathrm e^{x}}\right)\left(1+\dfrac{ex}{\mathrm e^{x}}\right)=1$。" "\n"
        r"令 $t=h(x)=\dfrac{ex}{\mathrm e^{x}}=x\mathrm e^{1-x}$，则 $(a+t)(1+t)=1$，即" "\n"
        r"$q(t)=t^{2}+(a+1)t+(a-1)=0$。" "\n"
        r"**研究 $h$**：$h'(x)=\mathrm e^{1-x}-x\mathrm e^{1-x}=(1-x)\mathrm e^{1-x}$。" "\n"
        r"$h$ 在 $(-\infty,1)$ 递增、$(1,+\infty)$ 递减，$h(1)=1$ 为最大值；" "\n"
        r"$x\to-\infty$ 时 $h\to-\infty$，$x\to+\infty$ 时 $h\to0^{+}$。" "\n"
        r"于是方程 $h(x)=t$ 的根的个数：$t>1$ 时 $0$ 个；$t=1$ 时 $1$ 个；$0<t<1$ 时 $2$ 个；" "\n"
        r"$t=0$ 时 $1$ 个（$x=0$）；$t<0$ 时 $1$ 个。" "\n"
        r"**计数**：$\Delta=(a+1)^{2}-4(a-1)=(a-1)^{2}+4>0$，恒有两个不等实根 $t_1<t_2$。" "\n"
        r"要有 $3$ 个公共点，需一根给 $2$ 个、另一根给 $1$ 个。" "\n"
        r"若 $t=1$ 为根：$1+a+1+a-1=0\Rightarrow a=-\frac12$，另一根 $t=-\frac32$（$1$ 个），共 $2$ 个，不合。" "\n"
        r"若 $t=0$ 为根：$a-1=0\Rightarrow a=1$，另一根 $t=-2$（$1$ 个），共 $2$ 个，不合。" "\n"
        r"故应为 $t_1<0<t_2<1$（$t_1$ 给 $1$ 个，$t_2$ 给 $2$ 个），即 $0$ 介于两 根之间且 $1$ 在较大根右侧：" "\n"
        r"$q(0)=a-1<0$ 且 $q(1)=1+(a+1)+(a-1)=2a+1>0$，解得 $-\dfrac12<a<1$。" "\n"
        r"故选 A。"
    ),
    'review': (
        r"⚠ **$ex$ 是 $e\cdot x$ 不是 $\mathrm e^{x}$** —— 这是本批最关键的还原。" "\n"
        r"**反证**：若按 $\mathrm e^{x}$ 理解，则除以 $\mathrm e^{2x}$ 后得 $t=\mathrm e^{-2x}\in(0,+\infty)$ 且**严格单调**，" "\n"
        r"每个正根 $t_i$ 只对应 **1 个** $x$，两个根最多给 **2 个**公共点，**与「恰有三个」矛盾** ✗" "\n"
        r"按 $ex$ 理解时 $t=x\mathrm e^{1-x}$，它在 $x<1$ 递增到最大值 $1$、在 $x>1$ 递减到 $0$，" "\n"
        r"与详解「$x<1$ 时 $h(x)$ 单调递增且 $h(x)\in(-\infty,1)$；$x>1$ 时 $h(x)$ 单调递减且 $h(x)\in(0,1)$」**完全吻合** ✓✓✓" "\n"
        r"★ 答案、详解完整 ✓。原书 p095-096 详解：「对于 $t^2+(a+1)t+a-1=0$，$\Delta=(a+1)^2-4(a-1)=(a-1)^2+4>0$，" "\n"
        r"设该方程有两个不同的实根 $t_1,t_2$，由题意得 $h(x)=t_1$、$h(x)=t_2$ 共有三个实数根。" "\n"
        r"若 $t=1$ 是方程的根，则 $1+a+1+a-1=0$，即 $a=-\frac12$，则方程的另一个根为…不合题意。" "\n"
        r"若 $t=0$ 是方程的根，则 $0+0+a-1=0$，即 $a=1$，则方程的另一个根为 $t=-2$，不合题意。" "\n"
        r"所以关于 $t$ 的方程的两根满足 $t_1<0<t_2<1$，所以 $0+0+a-1<0$ 且 $1+a+1+a-1>0$，解得 $-\frac12<a<1$。故选 A.」" "\n"
        r"—— **$\Delta>0$、$a=-\frac12$ 与 $a=1$ 的排除、$t_1<0<t_2<1$、$q(0)<0$、$q(1)>0$、$-\frac12<a<1$、答案 A 全部与我的推导一致** ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **除以 $\mathrm e^{2x}$**：$\frac{a\mathrm e^x+ex}{\mathrm e^x}=a+\frac{ex}{\mathrm e^x}=a+x\mathrm e^{1-x}$ ✓✓✓（同理第二因式）" "\n"
        r"② **$(a+t)(1+t)=1$ 展开**：$t^2+(a+1)t+a=1$ ⟹ $t^2+(a+1)t+(a-1)=0$ ✓✓✓" "\n"
        r"③ **$\Delta=(a-1)^2+4$**：$(a+1)^2-4(a-1)=a^2+2a+1-4a+4=a^2-2a+5=(a-1)^2+4$ ✓✓✓ **恒正**" "\n"
        r"④ **$h'(x)=(1-x)\mathrm e^{1-x}$**：$[x\mathrm e^{1-x}]'=\mathrm e^{1-x}+x\mathrm e^{1-x}(-1)=(1-x)\mathrm e^{1-x}$ ✓✓✓" "\n"
        r"$h(1)=1\cdot\mathrm e^0=1$ ✓；$x\to-\infty$：$x\mathrm e^{1-x}\to-\infty$ ✓；$x\to+\infty$：$\to0^+$ ✓✓✓" "\n"
        r"⑤ **$q(0)=a-1$、$q(1)=2a+1$**：$q(1)=1+a+1+a-1=2a+1$ ✓✓✓" "\n"
        r"⑥ **数值检验（$a=0$，应在范围内）**：$q(t)=t^2+t-1=0$，$t=\frac{-1\pm\sqrt5}2$ ⟹ $t_1=-1.618$、$t_2=0.618$。" "\n"
        r"$t_1=-1.618<0$ ⟹ $h(x)=-1.618$：$h$ 在 $(-\infty,1)$ 从 $-\infty$ 增到 $1$，恰 **1 个**根 ✓" "\n"
        r"$t_2=0.618\in(0,1)$ ⟹ $h(x)=0.618$：在 $(-\infty,1)$ 一个、在 $(1,+\infty)$ 一个 ⟹ **2 个**根 ✓" "\n"
        r"合计 **3 个** ✓✓✓ **与「恰有三个公共点」吻合**" "\n"
        r"⑦ **数值检验（$a=-0.4$，在 $(-\frac12,1)$ 内）**：$q(t)=t^2+0.6t-1.4=0$，$t=\frac{-0.6\pm\sqrt{0.36+5.6}}2=\frac{-0.6\pm2.4413}2$。" "\n"
        r"$t_1=-1.5207<0$（1 个）、$t_2=0.9207\in(0,1)$（2 个）⟹ 3 个 ✓✓✓" "\n"
        r"⑧ **边界 $a=-\frac12$**：$q(t)=t^2+0.5t-1.5=0$，$t=\frac{-0.5\pm2.5}2$ ⟹ $t_1=-1.5$（1 个）、$t_2=1$（1 个）⟹ **2 个** ✗ ✓✓✓ **正确排除**" "\n"
        r"⑨ **边界 $a=1$**：$q(t)=t^2+2t=t(t+2)$，$t_1=-2$（1 个）、$t_2=0$（1 个，$x=0$）⟹ **2 个** ✗ ✓✓✓ **正确排除**" "\n"
        r"**答案 A 正确** ✓" "\n"
        r"**⭐⭐ 通法（公共点个数 ⟹ 换元 + 根的计数）**：" "\n"
        r"① ⭐⭐ **两边同除以 $\mathrm e^{2x}$ 造出 $x\mathrm e^{1-x}$**：凡是含 $\mathrm e^{x}$ 与多项式 $x$ 混合的方程，" "\n"
        r"**先试「除以 $\mathrm e^{kx}$」**，把超越式压成 $\frac{x}{\mathrm e^{x}}$ 型；" "\n"
        r"② ⭐⭐ **$h(x)=x\mathrm e^{1-x}$ 的图象（单峰，峰值 $1$）** —— 记住 " "\n"
        r"「$t>1$：$0$ 个；$t=1$：$1$ 个；$0<t<1$：$2$ 个；$t=0$：$1$ 个；$t<0$：$1$ 个」这张计数表；" "\n"
        r"③ ⭐ **要凑 $3$ 个 ⟹ 一根给 $2$ 个、一根给 $1$ 个**，于是只有「$0<t<1$ 配一个 $t\le0$」这一种可能；" "\n"
        r"④ ⚠ **两个端点值必须单独代入检验**：$a=-\frac12$（$t=1$ 为根）与 $a=1$（$t=0$ 为根）**都要排除**，" "\n"
        r"这正是区间 $(-\frac12,1)$ 两端都开的来源；" "\n"
        r"⑤ 检验：**取 $a=0$ 与 $a=-0.4$ 数出 3 个根，取 $a=\pm$ 边界数出 2 个根** ✓。"
    ),
    'difficulty': 0.95,
    'topics': ['M-T-130'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-130-V1',
}

T130_V2 = {
    'type': '选择',
    'stem_text': (
        r"对于任意 $x_1,x_2\in[1,+\infty)$，当 $x_2>x_1$ 时，恒有 $a\ln\dfrac{x_2}{x_1}<2(x_2-x_1)$ 成立；"
        r"则实数 $a$ 的取值范围是（　　）"
    ),
    'opts': [
        ('A', r"$(-\infty,0]$"),
        ('B', r"$(-\infty,1]$"),
        ('C', r"$(-\infty,2]$"),
        ('D', r"$(-\infty,3]$"),
    ],
    'answer': 'C',
    'analysis': (
        r"把不等式改写成 $a\ln x_2-2x_2<a\ln x_1-2x_1$，即函数 $f(x)=a\ln x-2x$ 在 $[1,+\infty)$ 上严格递减，"
        r"于是 $f'(x)=\frac ax-2\le0$ 恒成立。"
    ),
    'solution': (
        r"原不等式 $a\ln\dfrac{x_2}{x_1}<2(x_2-x_1)$ 即 $a\ln x_2-a\ln x_1<2x_2-2x_1$，" "\n"
        r"移项得 $a\ln x_2-2x_2<a\ln x_1-2x_1$。" "\n"
        r"令 $f(x)=a\ln x-2x$，则条件为：对任意 $1\le x_1<x_2$，恒有 $f(x_2)<f(x_1)$，" "\n"
        r"即 $f$ 在 $[1,+\infty)$ 上严格递减。" "\n"
        r"$f'(x)=\dfrac ax-2$，需 $f'(x)\le0$ 在 $[1,+\infty)$ 恒成立，即 $a\le2x$ 对一切 $x\ge1$ 成立。" "\n"
        r"由 $2x\ge2$（$x\ge1$），得 $a\le2$。" "\n"
        r"当 $a=2$ 时 $f'(x)=\frac2x-2\le0$（$x\ge1$），且仅在 $x=1$ 处取等，$f$ 仍严格递减，可取。" "\n"
        r"故 $a\in(-\infty,2]$。选 C。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p096 详解：「即 $a\ln x_2-2x_2<a\ln x_1-2x_1$ 成立，令 $f(x)=a\ln x-2x$，" "\n"
        r"∴$f(x_2)<f(x_1)$，∴$f(x)$ 在 $[1,+\infty)$ 上单调递减，∴$f'(x)=\frac ax-2\le0$ 在 $[1,+\infty)$ 恒成立，" "\n"
        r"∴$a\le2x$ 在 $[1,+\infty)$ 恒成立，∵当 $x\ge1$，$2x\ge2$，∴实数 $a$ 的取值范围为 $(-\infty,2]$，故选 C.」" "\n"
        r"—— **移项成 $a\ln x-2x$ 的差、构造 $f$、$f'\le0$、$a\le2x$、$a\le2$、答案 C 全部与我的推导一致** ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **$\ln\frac{x_2}{x_1}=\ln x_2-\ln x_1$** ✓✓✓（$x_1,x_2>0$）" "\n"
        r"② **移项**：$a\ln x_2-a\ln x_1<2x_2-2x_1$ ⟺ $a\ln x_2-2x_2<a\ln x_1-2x_1$ ✓✓✓" "\n"
        r"③ **$f'(x)=\frac ax-2$** ✓✓✓" "\n"
        r"④ **$a\le2x$ 对 $x\ge1$** ⟹ $a\le\min(2x)=2$ ✓✓✓" "\n"
        r"⑤ **$a=2$ 时严格递减**：$f(x)=2\ln x-2x$，$f'(x)=\frac2x-2=\frac{2(1-x)}x\le0$（$x\ge1$），" "\n"
        r"仅在 $x=1$ 处为 $0$，其余 $<0$ ⟹ **严格递减** ✓✓✓ **端点可取**" "\n"
        r"⑥ **数值检验（$a=2$，$x_1=1,x_2=3$）**：左 $=2\ln3=2.1972$；右 $=2(2)=4$。$2.1972<4$ ✓✓✓" "\n"
        r"⑦ **数值检验（$a=2$，$x_1=1,x_2=1.1$）**：左 $=2\ln1.1=0.19062$；右 $=2(0.1)=0.2$。$0.19062<0.2$ ✓✓✓ **临界处仍成立**" "\n"
        r"（这验证了 $a=2$ 确实可取：因为 $\ln(1+t)<t$）" "\n"
        r"⑧ **数值检验（$a=2.5>2$，应失败）**：取 $x_1=1$、$x_2=1.1$。左 $=2.5\ln1.1=0.23828$；右 $=0.2$。" "\n"
        r"$0.23828>0.2$ ✗ ✓✓✓ **确实不成立**" "\n"
        r"⑨ **$a\le0$ 显然成立**（A 是 C 的真子集，不是最完整答案）✓✓✓" "\n"
        r"**答案 C 正确** ✓" "\n"
        r"**⭐⭐ 通法（双变量不等式 ⟹ 单调性）**：" "\n"
        r"① ⭐⭐ **见到 $\frac{f(x_2)-f(x_1)}{x_2-x_1}$ 型或 $\ln\frac{x_2}{x_1}$ 型，一律先「移项配对」：** " "\n"
        r"把含 $x_2$ 的放一边、含 $x_1$ 的放另一边，构造成 **$F(x_2)<F(x_1)$**，单调性立刻显现；" "\n"
        r"② ⭐⭐ **$a\ln\frac{x_2}{x_1}=\int_{x_1}^{x_2}\frac ax dx$ 而 $2(x_2-x_1)=\int_{x_1}^{x_2}2dx$** —— " "\n"
        r"所以条件本质是 $\frac ax<2$（ integrand 比较），**积分视角能与导数法互相印证**；" "\n"
        r"③ ⭐ **$f'\le0$（允许孤立点取等）对应严格递减** —— 所以 $a=2$ **可以取**，" "\n"
        r"**别把端点丢掉**；" "\n"
        r"④ ⚠ **$a$ 无下界**：$a\to-\infty$ 时 $a\ln\frac{x_2}{x_1}$ 是很大的负数，不等式更易成立 ⟹ 区间是 $(-\infty,2]$；" "\n"
        r"⑤ 检验：**取 $x_2\to x_1$ 的极限位置（$x_2=1.1$）验证临界值 $a=2$** ✓。"
    ),
    'difficulty': 0.75,
    'topics': ['M-T-130'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-130-V2',
}

T131_E1 = {
    'type': '选择',
    'stem_text': (
        r"设函数 $f(x)=x^{2}+x-\dfrac{ax}{x+1}+\dfrac{16x}{(x+1)^{2}}$，若 $x>0$ 时 $f(x)>0$，"
        r"则实数 $a$ 的取值范围是（　　）"
    ),
    'opts': [
        ('A', r"$(0,+\infty)$"),
        ('B', r"$(-\infty,12)$"),
        ('C', r"$(-\infty,0)$"),
        ('D', r"$(12,+\infty)$"),
    ],
    'answer': 'B',
    'analysis': (
        r"$x>0$ 时除以 $x$ 得 $(x+1)-\frac a{x+1}+\frac{16}{(x+1)^{2}}>0$，分离出 $a<(x+1)^{2}+\frac{16}{x+1}$，"
        r"右端在 $x=1$ 处取最小值 $12$。"
    ),
    'solution': (
        r"$x>0$ 时 $f(x)=x\left[(x+1)-\dfrac a{x+1}+\dfrac{16}{(x+1)^{2}}\right]$，因 $x>0$，条件等价于" "\n"
        r"$(x+1)-\dfrac a{x+1}+\dfrac{16}{(x+1)^{2}}>0$。" "\n"
        r"乘以 $x+1>0$：$(x+1)^{2}-a+\dfrac{16}{x+1}>0$，即 $a<(x+1)^{2}+\dfrac{16}{x+1}$。" "\n"
        r"令 $g(x)=(x+1)^{2}+\dfrac{16}{x+1}$（$x>0$），则" "\n"
        r"$g'(x)=2(x+1)-\dfrac{16}{(x+1)^{2}}=\dfrac{2(x+1)^{3}-16}{(x+1)^{2}}$。" "\n"
        r"$g'(x)>0\iff(x+1)^{3}>8\iff x>1$；$g'(x)<0\iff0<x<1$。" "\n"
        r"故 $g$ 在 $(0,1]$ 递减、$[1,+\infty)$ 递增，$g_{\min}=g(1)=4+\dfrac{16}2=4+8=12$。" "\n"
        r"所以 $a<12$，即 $a\in(-\infty,12)$。故选 B。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p096 详解：「$x>0$ 时，$f(x)>0$ 即 $x+1-\frac a{x+1}+\frac{16}{(x+1)^2}>0$ 对 $x>0$ 成立，" "\n"
        r"∴$a<(x+1)^2+\frac{16}{x+1}\ (x>0)$。令 $g(x)=(x+1)^2+\frac{16}{x+1}\ (x>0)$，则 $g'(x)=2(x+1)-\frac{16}{(x+1)^2}=\frac{2(x+1)^3-16}{(x+1)^2}$，" "\n"
        r"令 $g'(x)>0$ 即 $(x+1)^3>8$，解得 $x>1$；令 $g'(x)<0$ 即 $(x+1)^3<8$，解得 $0<x<1$。" "\n"
        r"∴$g(x)$ 在 $(0,1]$ 上是减函数，在 $[1,+\infty)$ 上是增函数。∴$g(x)\ge g(1)=12$，∴$a<12$。故选：B」" "\n"
        r"—— **除以 $x+1$ 后的形式、$g=(x+1)^2+\frac{16}{x+1}$、$g'=\frac{2(x+1)^3-16}{(x+1)^2}$、$x=1$ 为极小点、$g(1)=12$、$a<12$、答案 B 全部与我的推导一致** ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **$f(x)=x[(x+1)-\frac a{x+1}+\frac{16}{(x+1)^2}]$**：$x^2+x=x(x+1)$ ✓；$-\frac{ax}{x+1}=x(-\frac a{x+1})$ ✓；" "\n"
        r"$\frac{16x}{(x+1)^2}=x\frac{16}{(x+1)^2}$ ✓✓✓" "\n"
        r"② **乘 $x+1$**：$(x+1)^2-a+\frac{16}{x+1}>0$ ✓✓✓" "\n"
        r"③ **$g'(x)$**：$[(x+1)^2]'=2(x+1)$；$[\frac{16}{x+1}]'=-\frac{16}{(x+1)^2}$。" "\n"
        r"$g'=2(x+1)-\frac{16}{(x+1)^2}=\frac{2(x+1)^3-16}{(x+1)^2}$ ✓✓✓" "\n"
        r"④ **$g(1)=4+8=12$** ✓✓✓；$(x+1)^3=8\iff x+1=2\iff x=1$ ✓✓✓" "\n"
        r"⑤ **数值检验（$a=11<12$，应可行）**：取 $x=1$：$f(1)=1+1-\frac{11}2+\frac{16}4=2-5.5+4=0.5>0$ ✓" "\n"
        r"取 $x=3$：$f=9+3-\frac{33}4+\frac{48}{16}=12-8.25+3=6.75>0$ ✓" "\n"
        r"取 $x=0.2$：$f=0.04+0.2-\frac{2.2}{1.2}+\frac{3.2}{1.44}=0.24-1.8333+2.2222=0.6289>0$ ✓✓✓" "\n"
        r"⑥ **数值检验（$a=12$，应不可行）**：$x=1$：$f(1)=2-\frac{12}2+4=2-6+4=0$，**不满足 $>0$** ✗ ✓✓✓" "\n"
        r"⑦ **数值检验（$a=13>12$，应失败）**：$x=1$：$f=2-6.5+4=-0.5<0$ ✗ ✓✓✓" "\n"
        r"⑧ **边界**：$a=12$ 时在 $x=1$ 处 $f=0$，故必须**严格** $a<12$ ⟹ 开区间 $(-\infty,12)$ ✓✓✓" "\n"
        r"（而 $a$ 可任意小（负），因为 $-\frac{ax}{x+1}$ 变成很大的正数 ✓）" "\n"
        r"**答案 B 正确** ✓" "\n"
        r"**⭐⭐ 通法（「恒成立 + 分母含参」⟹ 先提取正因子再分离）**：" "\n"
        r"① ⭐⭐ **$f(x)$ 每项都含因子 $x$，先提出来** —— $x>0$ 时可约去，**次数立刻降一阶**；" "\n"
        r"② ⭐⭐ **再乘 $(x+1)>0$ 把分母清掉**，得到 $a<g(x)$ 的干净形式 —— " "\n"
        r"**分离参数时「乘正数不变号」是前提，要先确认 $x+1>0$**；" "\n"
        r"③ ⭐ **$g(x)=(x+1)^2+\frac{16}{x+1}$ 用换元 $u=x+1>1$ 更简单**：$g=u^2+\frac{16}u$，$g'=2u-\frac{16}{u^2}$，" "\n"
        r"零点 $u=2$ ⟹ $x=1$，$g_{\min}=4+8=12$；" "\n"
        r"④ ⚠ **$a<12$ 是严格小于**：$a=12$ 时 $x=1$ 处 $f(1)=0$，**不满足 $f>0$**，端点必须开；" "\n"
        r"⑤ 检验：**取 $a=11$（三点都为正）、$a=12$（$x=1$ 处为 $0$）、$a=13$（$x=1$ 处为负）** ✓。"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-131'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-131-E1',
}

T131_V1 = {
    'type': '选择',
    'stem_text': (
        r"不等式 $x^{-3}\mathrm e^{x}-a\ln x\ge x+1$ 对任意 $x\in(1,+\infty)$ 恒成立，则实数 $a$ 的取值范围（　　）"
    ),
    'opts': [
        ('A', r"$(-\infty,1-\mathrm e]$"),
        ('B', r"$(-\infty,2-\mathrm e^{2}]$"),
        ('C', r"$(-\infty,-2]$"),
        ('D', r"$(-\infty,-3]$"),
    ],
    'answer': 'D',
    'analysis': (
        r"因 $x>1$ 有 $\ln x>0$，分离得 $a\le\frac{x^{-3}\mathrm e^{x}-x-1}{\ln x}$。用 $\mathrm e^{u}\ge u+1$ 于 $u=x-3\ln x$ 得"
        r"$x^{-3}\mathrm e^{x}=\mathrm e^{x-3\ln x}\ge x-3\ln x+1$，故比值 $\ge-3$，且 $x-3\ln x=0$ 在 $(1,+\infty)$ 有根可取等。"
    ),
    'solution': (
        r"$x>1$ 时 $\ln x>0$，原不等式等价于" "\n"
        r"$a\le\dfrac{x^{-3}\mathrm e^{x}-x-1}{\ln x}$ 对一切 $x>1$ 成立。" "\n"
        r"记 $u=x-3\ln x$，则 $x^{-3}\mathrm e^{x}=\mathrm e^{x-3\ln x}=\mathrm e^{u}$。" "\n"
        r"由基本不等式 $\mathrm e^{u}\ge u+1$（当且仅当 $u=0$ 取等）：" "\n"
        r"$x^{-3}\mathrm e^{x}\ge(x-3\ln x)+1$。" "\n"
        r"于是分子 $\ge(x-3\ln x+1)-x-1=-3\ln x$，故" "\n"
        r"$\dfrac{x^{-3}\mathrm e^{x}-x-1}{\ln x}\ge\dfrac{-3\ln x}{\ln x}=-3$。" "\n"
        r"**等号能否取到**：需 $u=x-3\ln x=0$。令 $\varphi(x)=x-3\ln x$，$\varphi(1)=1>0$、$\varphi(3)=3-3\ln3=3-3.2958=-0.2958<0$，" "\n"
        r"由连续性，$\varphi$ 在 $(1,3)$ 内有零点，故等号可以取到。" "\n"
        r"所以右端最小值为 $-3$，$a\le-3$。故选 D。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p096 详解：「题意即为 $a\ln x\le x^{-3}\mathrm e^x-x-1$ 对 $\forall x\in(1,+\infty)$ 恒成立，" "\n"
        r"即 $a\le\frac{x^{-3}\mathrm e^x-x-1}{\ln x}$ 对 $\forall x\in(1,+\infty)$ 恒成立，从而求 $y=\frac{x^{-3}\mathrm e^x-x-1}{\ln x}$ 的最小值，" "\n"
        r"而 $x^{-3}\mathrm e^x=\mathrm e^{\ln x^{-3}}\mathrm e^x=\mathrm e^{x-3\ln x}\ge x-3\ln x+1$，故 $x^{-3}\mathrm e^x-x-1\ge x-3\ln x+1-x-1=-3\ln x$，" "\n"
        r"即 $\frac{x^{-3}\mathrm e^x-x-1}{\ln x}\ge\frac{-3\ln x}{\ln x}=-3$，当 $x-3\ln x=0$ 时等号成立，方程 $x-3\ln x=0$ 在 $(1,+\infty)$ 内有根，" "\n"
        r"故 $\left(\frac{x^{-3}\mathrm e^x-x-1}{\ln x}\right)_{\min}=-3$，所以 $a\le-3$，故选 D．」" "\n"
        r"—— **分离出 $\frac{x^{-3}\mathrm e^x-x-1}{\ln x}$、$x^{-3}\mathrm e^x=\mathrm e^{x-3\ln x}$、$\mathrm e^u\ge u+1$、$-3\ln x$、$\varphi$ 有零点、$a\le-3$、答案 D 全部与我的推导一致** ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **$x^{-3}\mathrm e^x=\mathrm e^{x-3\ln x}$**：$\mathrm e^{-3\ln x}=x^{-3}$ ✓✓✓" "\n"
        r"② **$\mathrm e^u\ge u+1$**，等号当且仅当 $u=0$ ✓✓✓" "\n"
        r"③ **分子放缩**：$\mathrm e^{x-3\ln x}-x-1\ge(x-3\ln x+1)-x-1=-3\ln x$ ✓✓✓" "\n"
        r"④ **$x>1$ 时 $\ln x>0$**，除以 $\ln x$ 不变号 ⟹ 比值 $\ge-3$ ✓✓✓" "\n"
        r"⑤ **零点存在**：$\varphi(x)=x-3\ln x$，$\varphi(1)=1-0=1>0$；$\varphi(3)=3-3(1.0986)=3-3.2958=-0.2958<0$ ✓✓✓" "\n"
        r"由介值定理，$(1,3)$ 内有零点。数值：$\varphi(1.5)=1.5-3(0.4055)=1.5-1.2164=0.2836>0$；" "\n"
        r"$\varphi(1.8)=1.8-3(0.5878)=1.8-1.7634=0.0366>0$；$\varphi(1.85)=1.85-3(0.6152)=1.85-1.8456=0.0044>0$；" "\n"
        r"$\varphi(1.86)=1.86-3(0.6206)=1.86-1.8618=-0.0018<0$ ⟹ **零点 $x^*\approx1.857$** ✓✓✓" "\n"
        r"⑥ **在 $x^*$ 处验等号**：$x^*=1.857$，$\ln x^*=0.6191$，$3\ln x^*=1.8573\approx x^*$ ✓" "\n"
        r"$x^{-3}\mathrm e^x=\mathrm e^{1.857-1.8573}=\mathrm e^{-0.0003}=0.9997$；$x+1=2.857$。" "\n"
        r"分子 $=0.9997-2.857=-1.8573$；$\ln x=0.6191$；比值 $=\frac{-1.8573}{0.6191}=-2.9997\approx-3$ ✓✓✓" "\n"
        r"⑦ **数值检验（$a=-3$，应可行）**：需 $x^{-3}\mathrm e^x+3\ln x\ge x+1$。" "\n"
        r"$x=1.857$：左 $=0.9997+3(0.6191)=0.9997+1.8573=2.857$；右 $=2.857$ ✓✓✓ **取等**" "\n"
        r"$x=2$：$2^{-3}\mathrm e^2=0.125(7.389)=0.9236$；$3\ln2=2.0794$；左 $=3.0030$；右 $=3$ ✓ 成立" "\n"
        r"$x=5$：$5^{-3}\mathrm e^5=0.008(148.41)=1.1873$；$3\ln5=4.8283$；左 $=6.0156$；右 $=6$ ✓ 成立" "\n"
        r"$x=1.2$：$1.2^{-3}\mathrm e^{1.2}=0.5787(3.3201)=1.9213$；$3\ln1.2=0.5470$；左 $=2.4683$；右 $=2.2$ ✓ 成立 ✓✓✓" "\n"
        r"⑧ **数值检验（$a=-2.9>-3$，应失败）**：$x=1.857$：左 $=0.9997+2.9(0.6191)=0.9997+1.7954=2.7951$；右 $=2.857$。" "\n"
        r"$2.7951<2.857$ ✗ ✓✓✓ **确实不成立**" "\n"
        r"⑨ **选项排除**：$1-\mathrm e=-1.718>-3$ ✗；$2-\mathrm e^2=-5.389<-3$（**过于保守**，不是最精确范围）✗；" "\n"
        r"$-2>-3$ ✗ ✓✓✓" "\n"
        r"**答案 D 正确** ✓" "\n"
        r"**⭐⭐ 通法（$x^{-k}\mathrm e^{x}$ 型 ⟹ 指数同构 + $\mathrm e^{u}\ge u+1$）**：" "\n"
        r"① ⭐⭐ **$x^{-3}\mathrm e^{x}=\mathrm e^{x-3\ln x}$** —— 把「幂 × 指数」压成单一指数，是这类题的**通用起手式**；" "\n"
        r"② ⭐⭐ **$\mathrm e^{u}\ge u+1$ 是全题唯一的放缩工具**，而它之所以精准，是因为" "\n"
        r"**放缩后的式子恰好与 $-x-1$ 合并成 $-3\ln x$**，正好能被分母 $\ln x$ 整除；" "\n"
        r"③ ⭐ **放缩类问题必须验「等号能否取到」**：需 $x-3\ln x=0$ 在 $(1,+\infty)$ 内有根 —— " "\n"
        r"**这一步不验，就只能得到「$\ge-3$」而不知道最小值是不是 $-3$**；" "\n"
        r"④ ⚠ **$a\le-3$ 的方向**：$a\le\min(\text{比值})=-3$，$a$ 越小越容易成立 ⟹ **区间向左无限**，" "\n"
        r"**别写成 $a\ge-3$**；" "\n"
        r"⑤ 检验：**数值求出 $x^*\approx1.857$ 并验证该处比值 $=-2.9997\approx-3$**，再验 $a=-2.9$ 失败 ✓。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-131'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-131-V1',
}

QS = [T126_E1, T126_V1, T126_V2, T126_V3, T127_E1, T127_V1, T129_V2,
      T130_E1, T130_V1, T130_V2, T131_E1, T131_V1]
