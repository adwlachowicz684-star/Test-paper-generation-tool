# -*- coding: utf-8 -*-
r"""第72批：导数压轴小题（12 题）

来源：2024高中数学热点题型归纳完整解析版.pdf p104-111
M-T-139（3）、M-T-140（2）、M-T-141（2）、M-T-142（2）、M-T-143（1）、M-T-145（2）

## ★★ 12 题我全部独立验算，与原书答案全部吻合

| 题 | 我的验算 | 答案 |
|---|---|---|
| M-T-139-E1 | 取 $x_1=-0.5$ 反算 $x_2\approx0.4402$，逐条验 4 个命题 | **B** |
| M-T-139-V1 | ⭐ $\sqrt{x}$ 被提取成 $x$（按 $x$ 则 $f(\mathrm e)=-\frac1{\mathrm e}$ 与详解 $-\frac1{2\mathrm e}$ 矛盾） | **D** |
| M-T-139-V3 | 取 $a=2$ 反算 $b\approx4.2885$：①②③④ 全成立 | **D** |
| M-T-140-E1 | $f$ 递增 ⟹ $f(y)=y$；$g(y)=\ln y+(\mathrm e-1)y-\mathrm e^{y}$ 递减，$g(1)=-1$ | **D** |
| M-T-140-V3 | ⭐ 分段点：$f(x)=1-\frac x2$（非 $\frac{1-x}2$，否则得 $3-2\ln2$ 不在选项）→ $4-2\ln2$ | **A** |
| M-T-141-V1 | 分 $b\le\frac a{\mathrm e}$ 与 $b>\frac a{\mathrm e}$ 两类，合起来 $(\frac13,\frac3{\mathrm e}]$ | 填 |
| M-T-141-V3 | ⭐ AM-GM 给 $3+2\sqrt2=5.828$ —— **正是选项 A/B，是陷阱**；真答案 $6$ | **C** |
| M-T-142-E1 | $n=9$ 时 $0.006683<0.010738$ ✓；$n=10$ 时 $0.005414>0.002255$ ✗ | **C** |
| M-T-142-V1 | 两侧最值都是 $-1$ ⟹ 夹逼出 $m=1,n=0$ ⟹ $x=y=1$ | **A** |
| M-T-143-V2 | ⭐ 答案 `85-9 2` 实为 $\frac{\sqrt{85}-9}2$（根号丢失）；$t$ 在 $a=\frac23$ 处取最小 $\frac92$ | 填 |
| M-T-145-V1 | $G(s)=1-\ln s-\frac2s$，$s=2$ 处最大 $-\ln2$ | **B** |
| M-T-145-V3 | $\varphi(u)$ 驻点 $u\ln u=\mathrm e$ ⟹ $u=\mathrm e$，$a=2\mathrm e$ ⟹ $-\frac1{\mathrm e}$ | **B** |

## 本批最漂亮的一处：M-T-141-V3 的 AM-GM 陷阱

由 $(a-1)(b-1)=1$ 用 AM-GM：$u+2v\ge2\sqrt2$（$u=a-1,v=b-1$），得 $a+2b\ge3+2\sqrt2$。

**但 $3+2\sqrt2=5.828$ 恰好是选项 A/B** —— 命题人专门准备了这个陷阱。

错因：AM-GM 取等需 $u=2v$，即 $u=\sqrt2$、$v=\frac1{\sqrt2}$，但题设有 $v>1$，**取等点根本不在范围内**。

正确做法：在 $v>1$ 上 $\frac1v+2v$ 单调递增，下确界在 $v\to1^+$ 处取到 $3$ ⟹ $a+2b>6$。

## 两个「两侧最值相等 ⟹ 夹逼」的题

**M-T-142-V1**：$\ln m-m\le-1$ 与 $\mathrm e^{n}-n-2\ge-1$，要 $\ln m-m\ge\mathrm e^{n}-n-2$，只能是两边都 $=-1$ ⟹ $m=1,n=0$。

**M-T-142-E1**：$f_{\max}=\frac{4}{n^{2}\mathrm e^{2}}$ 与 $g_{\min}=\left(\frac{2\mathrm e}n\right)^{n}$，要求 $f_{\max}<g_{\min}$，逐一代 $n$ 定出最大正整数 $9$。
"""

T139_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知函数 $f(x)=\dfrac{1-x}{1+x^{2}}\mathrm e^{x}$，若 $f(x_1)=f(x_2)$ 且 $x_1<x_2$，"
        r"关于下列命题：① $f(x_1)>f(-x_2)$；② $f(x_2)>f(-x_1)$；③ $f(x_1)>f(-x_1)$；"
        r"④ $f(x_2)>f(-x_2)$。正确的个数为（　　）"
    ),
    'opts': [
        ('A', r"$1$ 个"),
        ('B', r"$2$ 个"),
        ('C', r"$3$ 个"),
        ('D', r"$4$ 个"),
    ],
    'answer': 'B',
    'analysis': (
        r"求导定出 $f$ 在 $(-\infty,0)$ 增、$(0,+\infty)$ 减，故 $x_1<0<x_2<1$；"
        r"再取具体值比较 $f(x_i)$ 与 $f(-x_i)$ 的大小。"
    ),
    'solution': (
        r"$f'(x)=\dfrac{-\mathrm e^{x}(1+x^{2})-(1-x)\cdot2x\cdot\mathrm e^{x}}{(1+x^{2})^{2}}\cdot(-1)\cdot(-1)"
        r"=\dfrac{-\mathrm e^{x}\left[x^{2}-2x+3\right]x}{(1+x^{2})^{2}}$。" "\n"
        r"（直接给出：$f'(x)=\dfrac{-x(x^{2}-2x+3)\mathrm e^{x}}{(1+x^{2})^{2}}$。）" "\n"
        r"因 $x^{2}-2x+3=(x-1)^{2}+2>0$，故 $f'(x)$ 与 $-x$ 同号：" "\n"
        r"$f$ 在 $(-\infty,0)$ 单调递增，在 $(0,+\infty)$ 单调递减。" "\n"
        r"又 $f(0)=1$、$f(1)=0$，$x<0$ 时 $f(x)>0$，$x>1$ 时 $f(x)<0$。" "\n"
        r"由 $f(x_1)=f(x_2)$ 且 $x_1<x_2$ 知 $x_1<0<x_2<1$。" "\n"
        r"**比较 $f(x_1)$ 与 $f(-x_1)$**：$-x_1>0$，而 $f$ 在正半轴递减且 $x_2\in(0,1)$。" "\n"
        r"取 $x_1=-0.5$ 试算：$f(-0.5)=\dfrac{1.5}{1.25}\mathrm e^{-0.5}=1.2\times0.6065=0.7278$；" "\n"
        r"解得 $x_2\approx0.4402$；$f(-x_2)=f(-0.4402)=\dfrac{1.4402}{1.19382}\mathrm e^{-0.4402}=1.2064\times0.6439=0.7768$。" "\n"
        r"于是 $f(x_1)=0.7278<0.7768=f(-x_2)$，故 **① 错**；" "\n"
        r"又 $f(-x_1)=f(0.5)=\dfrac{0.5}{1.25}\mathrm e^{0.5}=0.4\times1.6487=0.6595$，" "\n"
        r"$f(x_1)=0.7278>0.6595=f(-x_1)$，故 **③ 对**；" "\n"
        r"由 $f(x_2)=f(x_1)$ 得 $f(x_2)=0.7278>0.6595=f(-x_1)$，故 **② 对**；" "\n"
        r"$f(x_2)=0.7278<0.7768=f(-x_2)$，故 **④ 错**。" "\n"
        r"综上 ②③ 正确，共 $2$ 个。故选 B。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p104 详解：「$f'(x)=\frac{-x(x^2-2x+3)\mathrm e^x}{(1+x^2)^2}$，所以函数 $f(x)$ 在 $(-\infty,0)$ 单调递增，" "\n"
        r"在 $(0,+\infty)$ 单调递减。$f(0)=1$，$f(1)=0$，当 $x<0$ 时 $f(x)>0$，所以 $x_1<0<x_2<1$。" "\n"
        r"即 $x$ 轴是函数的渐近线，画出草图如下。由图可知 $f(x_1)=f(x_2)<f(-x_2)$，①④ 错；" "\n"
        r"$f(x_2)=f(x_1)>f(-x_1)$，②③ 对。选 B.」" "\n"
        r"—— **$f'$ 表达式、单调性、$x_1<0<x_2<1$、②③ 对 ①④ 错、答案 B 全部与我的推导一致** ✓✓✓" "\n"
        r"**独立验算（数值，完全独立）**：" "\n"
        r"① **$f'(x)=\frac{-x(x^2-2x+3)\mathrm e^x}{(1+x^2)^2}$**：$[\frac{1-x}{1+x^2}\mathrm e^x]'=\mathrm e^x\left[\frac{1-x}{1+x^2}+\left(\frac{1-x}{1+x^2}\right)'\right]$。" "\n"
        r"$\left(\frac{1-x}{1+x^2}\right)'=\frac{-(1+x^2)-(1-x)2x}{(1+x^2)^2}=\frac{-1-x^2-2x+2x^2}{(1+x^2)^2}=\frac{x^2-2x-1}{(1+x^2)^2}$。" "\n"
        r"和 $=\frac{(1-x)(1+x^2)+x^2-2x-1}{(1+x^2)^2}=\frac{1+x^2-x-x^3+x^2-2x-1}{(1+x^2)^2}=\frac{-x^3+2x^2-3x}{(1+x^2)^2}=\frac{-x(x^2-2x+3)}{(1+x^2)^2}$ ✓✓✓" "\n"
        r"② **$x^2-2x+3=(x-1)^2+2>0$** ✓ ⟹ $f'$ 与 $-x$ 同号 ⟹ 左增右减 ✓✓✓" "\n"
        r"③ **$x_1=-0.5$**：$f(-0.5)=\frac{1-(-0.5)}{1+0.25}\mathrm e^{-0.5}=\frac{1.5}{1.25}(0.60653)=1.2(0.60653)=0.72784$ ✓✓✓" "\n"
        r"④ **反求 $x_2$**：$f(0.44)=\frac{0.56}{1.1936}\mathrm e^{0.44}=0.46917(1.55271)=0.72847$；" "\n"
        r"$f(0.45)=\frac{0.55}{1.2025}\mathrm e^{0.45}=0.45738(1.56831)=0.71730$。插值得 $x_2\approx0.4403$ ✓✓✓" "\n"
        r"⑤ **$f(-x_2)=f(-0.4403)$**：$\frac{1.4403}{1+0.19386}\mathrm e^{-0.4403}=\frac{1.4403}{1.19386}(0.64383)=1.20642(0.64383)=0.77674$ ✓✓✓" "\n"
        r"$f(x_1)=0.72784<0.77674$ ⟹ **① 错、④ 错** ✓✓✓" "\n"
        r"⑥ **$f(-x_1)=f(0.5)$**：$\frac{0.5}{1.25}\mathrm e^{0.5}=0.4(1.64872)=0.65949$。" "\n"
        r"$f(x_1)=0.72784>0.65949$ ⟹ **③ 对**；$f(x_2)=f(x_1)=0.72784>0.65949$ ⟹ **② 对** ✓✓✓" "\n"
        r"⑦ **换一组验证（$x_1=-1$）**：$f(-1)=\frac2{2}\mathrm e^{-1}=0.36788$。" "\n"
        r"$f(x_2)=0.36788$：$f(0.7)=\frac{0.3}{1.49}\mathrm e^{0.7}=0.20134(2.01375)=0.40544>0.36788$；" "\n"
        r"$f(0.8)=\frac{0.2}{1.64}\mathrm e^{0.8}=0.12195(2.22554)=0.27141<0.36788$。" "\n"
        r"$f(0.74)=\frac{0.26}{1.5476}\mathrm e^{0.74}=0.16800(2.09594)=0.35212$；$f(0.72)=\frac{0.28}{1.5184}(2.05443)=0.18440(2.05443)=0.37884$。" "\n"
        r"插值得 $x_2\approx0.729$。" "\n"
        r"$f(-x_2)=f(-0.729)=\frac{1.729}{1.53144}\mathrm e^{-0.729}=1.12899(0.48242)=0.54465>0.36788$ ⟹ ① 错 ✓" "\n"
        r"$f(-x_1)=f(1)=\frac02\mathrm e=0<0.36788$ ⟹ ③ 对 ✓ ✓✓✓ **两组一致**" "\n"
        r"**答案 B 正确** ✓" "\n"
        r"**⭐⭐ 通法（$f(x_1)=f(x_2)$ 型比较 $f(\pm x_i)$）**：" "\n"
        r"① ⭐⭐ **先定出 $x_1,x_2$ 的所在区间**：本题由单调性 + $f(0)=1$、$f(1)=0$ 得 $x_1<0<x_2<1$ —— " "\n"
        r"**这一步不做，后面四个命题都无从判断**；" "\n"
        r"② ⭐⭐ **取一组具体值代入验证** —— 这类「判断几个命题真假」的题，" "\n"
        r"**构造一个具体的 $(x_1,x_2)$ 逐条检验，比抽象推导快且不易错**；" "\n"
        r"③ ⭐ **注意 $f(x_1)=f(x_2)$ 这个条件可以「换着用」**：" "\n"
        r"判断 ② 时用 $f(x_2)=f(x_1)>f(-x_1)$，判断 ④ 时用 $f(x_2)<f(-x_2)$ —— **同一个值两种用法**；" "\n"
        r"④ ⚠ **$f$ 在正半轴递减是关键**：$0<-x_1$ 与 $x_2$ 都在正半轴，比较它们函数值就是比较自变量；" "\n"
        r"⑤ 检验：**至少换一组 $(x_1,x_2)$ 再验一遍**，确认结论不依赖特例。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-139'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-139-E1',
}

T139_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知方程 $\sqrt{x}\cdot\mathrm e^{kx}=1$ 有两个不同的实数根 $x_1,x_2\ (x_1<x_2)$，"
        r"则下列不等式不成立的是（　　）"
    ),
    'opts': [
        ('A', r"$x_1x_2>\mathrm e^{2}$"),
        ('B', r"$x_1+x_2>2\mathrm e$"),
        ('C', r"$x_1-k<\mathrm e+\dfrac1{\mathrm e}$"),
        ('D', r"$x_2-k>\mathrm e+\dfrac1{\mathrm e}$"),
    ],
    'answer': 'D',
    'analysis': (
        r"方程化为 $k=-\dfrac{\ln x}{2x}$。令 $f(x)=-\frac{\ln x}{2x}$，它极小值为 $f(\mathrm e)=-\frac1{2\mathrm e}$，"
        r"故 $k\in(-\frac1{2\mathrm e},0)$、$1<x_1<\mathrm e<x_2$。用极值点偏移证 A、B，再估计 C、D。"
    ),
    'solution': (
        r"由 $\sqrt{x}\mathrm e^{kx}=1$ 取对数：$\dfrac12\ln x+kx=0$，即 $k=-\dfrac{\ln x}{2x}$。" "\n"
        r"令 $f(x)=-\dfrac{\ln x}{2x}$，则 $f'(x)=\dfrac{\ln x-1}{2x^{2}}$。" "\n"
        r"$0<x<\mathrm e$ 时 $f'<0$（递减），$x>\mathrm e$ 时 $f'>0$（递增），" "\n"
        r"$f$ 的最小值为 $f(\mathrm e)=-\dfrac1{2\mathrm e}$；又 $f(1)=0$，$x\to+\infty$ 时 $f\to0^{-}$。" "\n"
        r"要有两个不同实根，需 $-\dfrac1{2\mathrm e}<k<0$，此时 $1<x_1<\mathrm e<x_2$。" "\n"
        r"**极值点偏移**：令 $1<\mathrm e-x_0<\mathrm e$（$0<x_0<\mathrm e-1$），比较 $f(\mathrm e+x_0)$ 与 $f(\mathrm e-x_0)$。" "\n"
        r"$f(\mathrm e+x_0)-f(\mathrm e-x_0)=-\dfrac{\ln(\mathrm e+x_0)}{2(\mathrm e+x_0)}+\dfrac{\ln(\mathrm e-x_0)}{2(\mathrm e-x_0)}=\dfrac{(\mathrm e+x_0)\ln(\mathrm e-x_0)-(\mathrm e-x_0)\ln(\mathrm e+x_0)}{2(\mathrm e^{2}-x_0^{2})}$。" "\n"
        r"记分子为 $g(x_0)$，$g(0)=0$，$g'(x_0)=\ln(\mathrm e^{2}-x_0^{2})-\dfrac{2(\mathrm e^{2}+x_0^{2})}{\mathrm e^{2}-x_0^{2}}<2-2=0$，" "\n"
        r"故 $g(x_0)<0$，即 $f(\mathrm e+x_0)<f(\mathrm e-x_0)$。" "\n"
        r"这说明右侧下降得更远：$x_2-\mathrm e>\mathrm e-x_1$，故 $x_1+x_2>2\mathrm e$，**B 成立**；" "\n"
        r"进而可验证 $x_1x_2>\mathrm e^{2}$（数值：$k=-0.1$ 时 $x_1\approx1.297$、$x_2\approx12.71$，积 $\approx16.5>7.389$），**A 成立**。" "\n"
        r"**C、D**：因 $k\in(-\frac1{2\mathrm e},0)$，" "\n"
        r"$x_1-k=x_1+|k|<\mathrm e+\dfrac1{2\mathrm e}=2.902<\mathrm e+\dfrac1{\mathrm e}=3.086$，故 **C 恒成立**；" "\n"
        r"$x_2-k=x_2+|k|$，当 $k\to-\frac1{2\mathrm e}^{+}$ 时 $x_2\to\mathrm e$，此时 $x_2+|k|\to\mathrm e+\frac1{2\mathrm e}=2.902<3.086$，" "\n"
        r"故 **D 不恒成立**。选 D。"
    ),
    'review': (
        r"⚠ **题干的 $\sqrt{x}$ 被提取成了 $x$** —— 这是本批最关键的还原。" "\n"
        r"**反证**：若按 $x\mathrm e^{kx}=1$，则 $k=-\frac{\ln x}{x}$，$f(x)=-\frac{\ln x}x$ 的极小值是 $f(\mathrm e)=-\frac1{\mathrm e}$，" "\n"
        r"与详解给出的「$f'(x)=\frac{\ln x-1}{2x^2}$、最小值为 $f(\mathrm e)=-\frac1{2\mathrm e}$」**矛盾**（差一个因子 2）。" "\n"
        r"按 $\sqrt{x}$ 理解则 $k=-\frac{\ln x}{2x}$、$f'=\frac{\ln x-1}{2x^2}$、$f(\mathrm e)=-\frac1{2\mathrm e}$ ✓✓✓ **完全吻合**" "\n"
        r"★ 答案、详解完整 ✓。原书 p104-105 详解：「由题意 $k=-\frac{\ln x}{2x}$，即 $y=k$ 与 $f(x)=-\frac{\ln x}{2x}$ 在 $(0,+\infty)$ 上有两个交点…" "\n"
        r"∵$f'(x)=\frac{\ln x-1}{2x^2}$，而 $f'(\mathrm e)=0$，∴当 $0<x<\mathrm e$ 时 $f(x)$ 单调递减；当 $x>\mathrm e$ 时 $f(x)$ 单调递增；" "\n"
        r"∴$f(x)$ 的极小值也是最小值为 $f(\mathrm e)=-\frac1{2\mathrm e}$，而 $f(1)=0$…" "\n"
        r"∴要使题设成立，则 $-\frac1{2\mathrm e}<k<0$ 且 $1<x_1<\mathrm e<x_2$ 有 $f(x_1)=f(x_2)=k$。…" "\n"
        r"令 $1<\mathrm e-x_0<\mathrm e$，则 $\mathrm e+x_0>\mathrm e$…$g'(x_0)=\ln(\mathrm e^2-x_0^2)-\frac{2(\mathrm e^2+x_0^2)}{\mathrm e^2-x_0^2}$…" "\n"
        r"∵$1<2\mathrm e-1<\mathrm e^2-x_0^2<\mathrm e^2$，$\mathrm e^2<\mathrm e^2+x_0^2<2\mathrm e^2-2\mathrm e+1$，∴$g'(x_0)<\ln\mathrm e^2-\frac{2\mathrm e^2}{\mathrm e^2}=2-2=0$…" "\n"
        r"∴$f(\mathrm e+x_0)<f(\mathrm e-x_0)$ 且当 $x>\mathrm e$ 时 $f(x)$ 单调递增，故在 $\mathrm e+x_0$ 右侧存在 $x_2$ 使 $f(x_2)=f(\mathrm e-x_0)$，即 $x_2>\mathrm e+x_0$…」" "\n"
        r"—— **$k=-\frac{\ln x}{2x}$、$f'=\frac{\ln x-1}{2x^2}$、$f(\mathrm e)=-\frac1{2\mathrm e}$、$1<x_1<\mathrm e<x_2$、极值点偏移的构造 全部与我的推导一致** ✓✓✓" "\n"
        r"（⚠ 选项 C、D 的 $x_i-k$ 中连字符在提取中可能有歧义，但**两种解读下 D 都是不成立的那个**）" "\n"
        r"**独立验算**：" "\n"
        r"① **$k=-\frac{\ln x}{2x}$**：$\sqrt x\mathrm e^{kx}=1$ ⟹ $\frac12\ln x+kx=0$ ⟹ $k=-\frac{\ln x}{2x}$ ✓✓✓" "\n"
        r"② **$f'(x)=\frac{\ln x-1}{2x^2}$**：$[-\frac12\ln x\cdot x^{-1}]'=-\frac12(\frac1x\cdot\frac1x+\ln x\cdot(-\frac1{x^2}))=-\frac12\cdot\frac{1-\ln x}{x^2}=\frac{\ln x-1}{2x^2}$ ✓✓✓" "\n"
        r"③ **$f(\mathrm e)=-\frac1{2\mathrm e}=-0.18394$**、$f(1)=0$、$x\to+\infty$ 时 $f\to0^-$ ✓✓✓" "\n"
        r"④ **两解条件**：$k\in(-\frac1{2\mathrm e},0)$，此时 $x_1\in(1,\mathrm e)$、$x_2\in(\mathrm e,+\infty)$ ✓✓✓" "\n"
        r"⑤ **数值检验 A（$k=-0.1$）**：$\ln x=0.2x$。" "\n"
        r"$x_1$：$x=1.296$ ⟹ $\ln=0.25916$、$0.2x=0.2592$ ✓ ⟹ $x_1\approx1.2966$。" "\n"
        r"$x_2$：$x=12.7$ ⟹ $\ln=2.54160$、$0.2x=2.54$ ✓ ⟹ $x_2\approx12.71$。" "\n"
        r"$x_1x_2=1.2966(12.71)=16.48>\mathrm e^2=7.389$ ✓✓✓ **A 成立**" "\n"
        r"$x_1+x_2=14.01>2\mathrm e=5.437$ ✓✓✓ **B 成立**" "\n"
        r"⑥ **数值检验 A（$k=-0.18$，靠近边界）**：$\ln x=0.36x$。" "\n"
        r"$x=2.25$：$\ln=0.81093$、$0.36x=0.81$ ✓ ⟹ $x_1\approx2.25$。" "\n"
        r"$x=3.403$：$\ln=1.22457$、$0.36x=1.22508$ ✓ ⟹ $x_2\approx3.40$。" "\n"
        r"$x_1x_2=7.65>7.389$ ✓；$x_1+x_2=5.65>5.437$ ✓ ✓✓✓" "\n"
        r"⑦ **C 恒成立**：$x_1<\mathrm e=2.71828$，$|k|<\frac1{2\mathrm e}=0.18394$ ⟹ $x_1+|k|<2.902<\mathrm e+\frac1{\mathrm e}=3.0863$ ✓✓✓" "\n"
        r"⑧ **D 在边界附近失效**：$k\to-\frac1{2\mathrm e}^+$ 时 $x_1,x_2\to\mathrm e$，$x_2-k\to\mathrm e+0.18394=2.902<3.0863$ ✗ ✓✓✓ **D 不恒成立**" "\n"
        r"**答案 D 正确** ✓" "\n"
        r"**⭐⭐ 通法（极值点偏移的标准流程）**：" "\n"
        r"① ⭐⭐ **先把参数分离成 $k=f(x)$，把「方程有两根」翻译成「直线 $y=k$ 与 $f$ 有两个交点」**；" "\n"
        r"② ⭐⭐ **极值点偏移的核心是比较 $f(\mathrm e+x_0)$ 与 $f(\mathrm e-x_0)$** —— " "\n"
        r"构造 $g(x_0)=$ 分子，证 $g$ 在 $(0,\mathrm e-1)$ 上递减且 $g(0)=0$ ⟹ $g<0$ ⟹ **右侧更远** ⟹ $x_1+x_2>2\mathrm e$；" "\n"
        r"③ ⭐ **$\ln(\mathrm e^2-x_0^2)<2$ 这一步用到了 $\mathrm e^2-x_0^2<\mathrm e^2$**，而 $\frac{2(\mathrm e^2+x_0^2)}{\mathrm e^2-x_0^2}>2$ —— **两头夹逼，很巧妙**；" "\n"
        r"④ ⚠ **A（$x_1x_2>\mathrm e^2$）不能由 B 用 AM-GM 推出**（方向相反），要单独证或数值验；" "\n"
        r"⑤ 检验：**取两个 $k$（一个远离边界、一个靠近边界）分别验 A、B**，再看 D 在边界处失效。"
    ),
    'difficulty': 0.95,
    'topics': ['M-T-139'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-139-V1',
}

T139_V3 = {
    'type': '选择',
    'stem_text': (
        r"设 $a,b\in\mathbf R$ 且 $a<b$，若 $a^{3}\mathrm e^{b}=b^{3}\mathrm e^{a}$，则① $a+b>6$；② $ab<9$；"
        r"③ $a+2b>9$；④ $a<3<b$ 等结论中一定正确的个数是（　　）"
    ),
    'opts': [
        ('A', r"$1$"),
        ('B', r"$2$"),
        ('C', r"$3$"),
        ('D', r"$4$"),
    ],
    'answer': 'D',
    'analysis': (
        r"化为 $3\ln a-a=3\ln b-b$。令 $f(x)=3\ln x-x$，它在 $x=3$ 处取最大值，故 $0<a<3<b$（④）。"
        r"再用 $g(x)=f(x)-f(6-x)$ 证①、$h(x)=f(x)-f(\frac9x)$ 证②，③由①加 $b>3$ 得到。"
    ),
    'solution': (
        r"由 $a^{3}\mathrm e^{b}=b^{3}\mathrm e^{a}$ 得 $\left(\dfrac ab\right)^{3}=\mathrm e^{a-b}$。" "\n"
        r"因 $a-b<0$，故 $0<\mathrm e^{a-b}<1$，即 $0<\left(\dfrac ab\right)^{3}<1$，得 $0<\dfrac ab<1$。" "\n"
        r"结合 $a<b$（同号且比值小于 $1$）知 $0<a<b$。" "\n"
        r"取对数：$3\ln\dfrac ab=a-b$，即 $3\ln a-a=3\ln b-b$。" "\n"
        r"令 $f(x)=3\ln x-x\ (x>0)$，则 $f'(x)=\dfrac3x-1=\dfrac{3-x}x$。" "\n"
        r"$f$ 在 $(0,3)$ 递增、$(3,+\infty)$ 递减，$f(3)=3\ln3-3=3\ln\frac3{\mathrm e}$ 为最大值。" "\n"
        r"由 $f(a)=f(b)$ 且 $a<b$ 得 $0<a<3<b$，**④ 正确**。" "\n"
        r"**证①**：令 $g(x)=f(x)-f(6-x)\ (0<x<6)$，" "\n"
        r"$g'(x)=f'(x)+f'(6-x)=\dfrac{3-x}x+\dfrac{x-3}{6-x}=(3-x)\left(\dfrac1x-\dfrac1{6-x}\right)=\dfrac{2(3-x)^{2}}{x(6-x)}\ge0$。" "\n"
        r"$g$ 递增且 $g(3)=0$，故 $0<a<3$ 时 $g(a)<0$，即 $f(a)<f(6-a)$。" "\n"
        r"由 $f(a)=f(b)$ 得 $f(b)<f(6-a)$；而 $b>3$、$6-a>3$，$f$ 在 $(3,+\infty)$ 递减 ⟹ $b>6-a$，即 $a+b>6$，**① 正确**。" "\n"
        r"**证②**：令 $h(x)=f(x)-f\!\left(\dfrac9x\right)$，" "\n"
        r"$h'(x)=f'(x)+\dfrac9{x^{2}}f'\!\left(\dfrac9x\right)=\dfrac{3-x}x+\dfrac9{x^{2}}\cdot\dfrac{x-3}3=\dfrac{3-x}x-\dfrac{3(3-x)}{x^{2}}=-\dfrac{(x-3)^{2}}{x^{2}}\le0$。" "\n"
        r"$h$ 递减且 $h(3)=0$，故 $0<a<3$ 时 $h(a)>0$，即 $f(a)>f\!\left(\dfrac9a\right)$。" "\n"
        r"由 $f(a)=f(b)$ 得 $f(b)>f(\frac9a)$；而 $b>3$、$\frac9a>3$，$f$ 递减 ⟹ $b<\dfrac9a$，即 $ab<9$，**② 正确**。" "\n"
        r"**证③**：由①$a+b>6$ 与④$b>3$ 得 $a+2b=(a+b)+b>6+3=9$，**③ 正确**。" "\n"
        r"四条全对，选 D。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p105 详解：「$a^3\mathrm e^b=b^3\mathrm e^a\Rightarrow(\frac ab)^3=\mathrm e^{a-b}$，∵$a<b$，∴$a-b<0$，" "\n"
        r"∴$0<\mathrm e^{a-b}<1$，∴$0<\frac ab<1$，即 $0<a<b\Rightarrow3\ln\frac ab=a-b\Rightarrow3\ln a-a=3\ln b-b$。" "\n"
        r"$f(x)=3\ln x-x\ (x>0)$，∵$f'(x)=\frac3x-1=\frac{3-x}x$，令 $f'(x)=0$，∴$x=3$，$f(3)=3\ln3-3=3\ln\frac3{\mathrm e}$，" "\n"
        r"$0<x<3$ 时 $f'(x)>0$，$x>3$ 时 $f'(x)<0$，∵$f(a)=f(b)$，∴$0<a<3<b$，故④对；" "\n"
        r"令 $g(x)=f(x)-f(6-x)$，∴$g'(x)=f'(x)+f'(6-x)=\frac{3-x}x+\frac{-3+x}{6-x}=\frac{2(x-3)^2}{(6-x)x}$，" "\n"
        r"$0<x<3$ 时 $g'(x)>0$，∴$g(x)<g(3)=f(3)-f(3)=0$，$0<a<3$，∴$g(a)=f(a)-f(6-a)<0$，∴$f(a)<f(6-a)$…" "\n"
        r"∴$b>6-a$，∴$a+b>6$，故①对；又 $b>3$，∴$a+2b=a+b+b>9$，故③对；构造 $h(x)=f(x)-f(\frac9x)$，" "\n"
        r"$h'(x)=f'(x)+\frac9{x^2}f'(\frac9x)=\frac{3-x}x+\frac9{x^2}\cdot\frac{3-\frac9x}{\frac9x}=\frac{3-x}x+\frac9{x^2}\cdot\frac{x-3}3=-\frac{(3-x)^2}{x^2}<0$，" "\n"
        r"∴$h(x)$ 递减，$0<x<3$ 时 $h(x)>h(3)=0$，∵$0<a<3$，∴$h(a)=f(a)-f(\frac9a)>0$，∴$f(a)>f(\frac9a)=f(b)$…" "\n"
        r"∴$b<\frac9a$，$b>3>\frac9a$…故②对」" "\n"
        r"—— **$(\frac ab)^3=\mathrm e^{a-b}$、$f=3\ln x-x$、$x=3$ 为极大点、④、$g$ 递增证①、$h$ 递减证②、③、答案 D 全部与我的推导一致** ✓✓✓" "\n"
        r"**独立验算（数值，完全独立）**：" "\n"
        r"① **$f'(x)=\frac{3-x}x$** ✓✓✓；$f(3)=3\ln3-3=3.29584-3=0.29584$（$=3\ln\frac3{\mathrm e}=3(0.09861)=0.29584$ ✓）" "\n"
        r"② **取 $a=2$**：$f(2)=3\ln2-2=2.07944-2=0.07944$。解 $3\ln b-b=0.07944$（$b>3$）：" "\n"
        r"$b=4$：$3(1.38629)-4=4.15888-4=0.15888$；$b=4.5$：$3(1.50408)-4.5=4.51223-4.5=0.01223$。" "\n"
        r"$b=4.2$：$3(1.43508)-4.2=4.30525-4.2=0.10525$；$b=4.3$：$3(1.45862)-4.3=4.37585-4.3=0.07585$。" "\n"
        r"$b=4.28$：$3(1.45395)-4.28=4.36185-4.28=0.08185$；$b=4.29$：$3(1.45629)-4.29=4.36887-4.29=0.07887$。" "\n"
        r"插值得 $b\approx4.2885$ ✓✓✓" "\n"
        r"③ **验四条**：$a+b=6.2885>6$ ✓（①）；$ab=8.577<9$ ✓（②）；" "\n"
        r"$a+2b=2+8.577=10.577>9$ ✓（③）；$2<3<4.2885$ ✓（④）✓✓✓ **四条全对**" "\n"
        r"④ **验原式**：$a^3\mathrm e^b=8\cdot\mathrm e^{4.2885}=8(72.96)=583.7$；$b^3\mathrm e^a=4.2885^3\cdot\mathrm e^2=78.87(7.389)=582.8$。" "\n"
        r"$583.7\approx582.8$ ✓✓✓ **（差值来自 $b$ 的四舍五入）**" "\n"
        r"⑤ **$g'(x)=\frac{2(3-x)^2}{x(6-x)}$**：$\frac{3-x}x+\frac{x-3}{6-x}=(3-x)(\frac1x-\frac1{6-x})=(3-x)\frac{6-2x}{x(6-x)}=\frac{2(3-x)^2}{x(6-x)}$ ✓✓✓" "\n"
        r"数值验（$a=2$）：$g(2)=f(2)-f(4)=0.07944-0.15888=-0.07944<0$ ✓ ⟹ $f(a)<f(6-a)$ ✓" "\n"
        r"$f(b)=f(4.2885)=0.07944$；$f(6-a)=f(4)=0.15888$。$0.07944<0.15888$ ✓✓✓" "\n"
        r"⑥ **$h'(x)=-\frac{(x-3)^2}{x^2}$**：$f'(\frac9x)=\frac{3-\frac9x}{\frac9x}=\frac{3x-9}9=\frac{x-3}3$。" "\n"
        r"$\frac{3-x}x+\frac9{x^2}\cdot\frac{x-3}3=\frac{3-x}x+\frac{3(x-3)}{x^2}=\frac{3-x}x-\frac{3(3-x)}{x^2}=(3-x)(\frac1x-\frac3{x^2})=(3-x)\frac{x-3}{x^2}=-\frac{(x-3)^2}{x^2}$ ✓✓✓" "\n"
        r"数值验（$a=2$）：$h(2)=f(2)-f(4.5)=0.07944-0.01223=0.06721>0$ ✓ ⟹ $f(a)>f(\frac9a)$ ✓" "\n"
        r"$f(b)=0.07944>f(4.5)=0.01223$ ✓✓✓ ⟹ $b<4.5=\frac92$ ✓（$4.2885<4.5$ ✓）" "\n"
        r"**答案 D 正确** ✓" "\n"
        r"**⭐⭐ 通法（$f(a)=f(b)$ 型的多结论判断题）**：" "\n"
        r"① ⭐⭐ **先分离变量成 $f(a)=f(b)$，用单峰性定出 $a,b$ 分居极值点两侧** —— 本题 $0<a<3<b$ 就是第 ④ 条；" "\n"
        r"② ⭐⭐ **对称化构造函数**：要证 $a+b>2x_0$，构造 $g(x)=f(x)-f(2x_0-x)$，证 $g$ 在 $(0,x_0)$ 上的符号；" "\n"
        r"要证 $ab<x_0^2$，构造 $h(x)=f(x)-f(\frac{x_0^2}x)$ —— **两个模板，加号用平移、乘号用倒数**；" "\n"
        r"③ ⭐ **$g'(x)=f'(x)+f'(2x_0-x)$ 与 $h'(x)=f'(x)+\frac{x_0^2}{x^2}f'(\frac{x_0^2}x)$ 都会凑出完全平方**，" "\n"
        r"符号一眼看出 —— **这是它们的相同点**；" "\n"
        r"④ ⚠ **注意方向**：$g$ 递增、$g(3)=0$ ⟹ $a<3$ 时 $g(a)<0$ ⟹ $f(a)<f(6-a)$ ⟹ $f(b)<f(6-a)$ ⟹ **$b>6-a$**（递减区间上小的函数值对应大的自变量）；" "\n"
        r"⑤ 检验：**取 $a=2$ 反算 $b\approx4.2885$，四条逐一代入验** ✓。"
    ),
    'difficulty': 0.95,
    'topics': ['M-T-139'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-139-V3',
}

T140_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知函数 $f(x)=\ln(\ln x+(\mathrm e-1)x-m)$，若曲线 $y=\dfrac{3x^{2}+1}{x^{2}+1}$ 上存在点"
        r"$(x_1,y_1)$，使得 $y_1=f(f(y_1))$，则实数 $m$ 的最大值是（　　）"
    ),
    'opts': [
        ('A', r"$0$"),
        ('B', r"$3$"),
        ('C', r"$-2$"),
        ('D', r"$-1$"),
    ],
    'answer': 'D',
    'analysis': (
        r"曲线值域为 $[1,3)$。因 $f$ 递增，$f(f(y_1))=y_1$ 等价于 $f(y_1)=y_1$，即 $m=\ln y_1+(\mathrm e-1)y_1-\mathrm e^{y_1}$；"
        r"右端在 $[1,3)$ 上递减，最大值在 $y_1=1$ 处取到 $-1$。"
    ),
    'solution': (
        r"先求曲线值域：$y=\dfrac{3x^{2}+1}{x^{2}+1}=3-\dfrac2{x^{2}+1}$。" "\n"
        r"$x=0$ 时 $y=1$；$\lvert x\rvert\to+\infty$ 时 $y\to3$（取不到）。故 $y_1\in[1,3)$。" "\n"
        r"**关键一步**：$f$ 在其定义域上严格递增。设 $f(y_1)=c$。" "\n"
        r"若 $c>y_1$，则 $f(f(y_1))=f(c)>f(y_1)=c>y_1$，与 $f(f(y_1))=y_1$ 矛盾；" "\n"
        r"若 $c<y_1$，则 $f(f(y_1))=f(c)<f(y_1)=c<y_1$，同样矛盾。" "\n"
        r"故必有 $c=y_1$，即 $f(y_1)=y_1$。" "\n"
        r"$\ln(\ln y_1+(\mathrm e-1)y_1-m)=y_1\Rightarrow \ln y_1+(\mathrm e-1)y_1-m=\mathrm e^{y_1}$，" "\n"
        r"即 $m=\ln y_1+(\mathrm e-1)y_1-\mathrm e^{y_1}$。" "\n"
        r"令 $g(y)=\ln y+(\mathrm e-1)y-\mathrm e^{y}$（$y\in[1,3)$），则 $g'(y)=\dfrac1y+(\mathrm e-1)-\mathrm e^{y}$。" "\n"
        r"$g'(1)=1+(\mathrm e-1)-\mathrm e=0$；又 $g''(y)=-\dfrac1{y^{2}}-\mathrm e^{y}<0$，$g'$ 递减，" "\n"
        r"故 $y>1$ 时 $g'(y)<0$，$g$ 在 $[1,3)$ 上递减。" "\n"
        r"所以 $m$ 的最大值为 $g(1)=\ln1+(\mathrm e-1)-\mathrm e=-1$（此时 $y_1=1$，对应 $x_1=0$，可取到）。" "\n"
        r"故选 D。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p105 详解：「由题意，曲线 $y=\frac{3x^2+1}{x^2+1}$ 上存在点 $(x_1,y_1)$ 使得 $y_1=f(f(y_1))$，" "\n"
        r"所以 $y_1\in[1,3)$。记 $f(y_1)=c$，若 $c>y_1$，则 $f(f(y_1))=f(c)>f(y_1)=c>y_1$，不满足 $y_1=f(f(y_1))$，" "\n"
        r"同理 $c<y_1$ 也不满足，所以 $f(y_1)=y_1$，所以 $\ln(\ln y_1+(\mathrm e-1)y_1-m)=y_1$，所以 $\ln y_1+(\mathrm e-1)y_1-m=\mathrm e^{y_1}$，" "\n"
        r"所以 $m=\ln y_1-\mathrm e^{y_1}+(\mathrm e-1)y_1$，$y_1\in[1,3)$。记 $g(x)=\ln x-\mathrm e^x+(\mathrm e-1)x$，则 $g'(x)=\frac1x-\mathrm e^x+\mathrm e-1$，" "\n"
        r"记 $h(x)=\frac1x-\mathrm e^x+\mathrm e-1$，因为 $h'(x)=-\frac1{x^2}-\mathrm e^x<0$，所以 $h(x)$ 在 $[1,3)$ 上单调递减，" "\n"
        r"因为 $g'(1)=0$，所以 $x\in(1,3)$ 时 $g'(x)<0$，因为 $g(1)=-1$，$g(3)=-\mathrm e^3+3\mathrm e-3+\ln3$，" "\n"
        r"所以 $-\mathrm e^3+3\mathrm e-3+\ln3<m\le-1$，所以 $m$ 的最大值为 $-1$。故选：D.」" "\n"
        r"—— **$y_1\in[1,3)$、$f(y_1)=y_1$、$m=\ln y_1-\mathrm e^{y_1}+(\mathrm e-1)y_1$、$g'(1)=0$、$g$ 递减、$g(1)=-1$、答案 D 全部与我的推导一致** ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **曲线值域**：$\frac{3x^2+1}{x^2+1}=3-\frac2{x^2+1}$。$x=0$ ⟹ $3-2=1$ ✓；$x\to\infty$ ⟹ $3$ ✓；单调递增（$x^2+1$ 增）✓✓✓" "\n"
        r"② **$f$ 递增**：$f(x)=\ln(u(x))$，$u(x)=\ln x+(\mathrm e-1)x-m$ 递增，$\ln$ 递增 ⟹ $f$ 递增 ✓✓✓" "\n"
        r"③ **$f(f(y))=y\iff f(y)=y$（$f$ 递增）**：若 $f(y)>y$ 则 $f(f(y))>f(y)>y$ ✓；若 $f(y)<y$ 则 $f(f(y))<f(y)<y$ ✓ ✓✓✓" "\n"
        r"④ **$g(1)=\ln1-\mathrm e+(\mathrm e-1)=0-2.71828+1.71828=-1$** ✓✓✓" "\n"
        r"⑤ **$g'(1)=1-\mathrm e+\mathrm e-1=0$** ✓✓✓；$g''(y)=-\frac1{y^2}-\mathrm e^y<0$ ⟹ $g'$ 递减 ⟹ $y>1$ 时 $g'<0$ ✓✓✓" "\n"
        r"⑥ **数值验（$m=-1$，$y_1=1$）**：$\ln y_1+(\mathrm e-1)y_1-m=0+1.71828+1=2.71828=\mathrm e$ ✓；" "\n"
        r"$\ln(\mathrm e)=1=y_1$ ✓✓✓ **$f(1)=1$，取等成立**" "\n"
        r"⑦ **数值验（$m=0>-1$，应不可行）**：需存在 $y\in[1,3)$ 使 $g(y)=0$。但 $g(1)=-1$ 且 $g$ 递减 ⟹ $g(y)<-1<0$ ✗ ✓✓✓" "\n"
        r"⑧ **选项排除**：$0$、$3$ 都 $>-1$ ✗；$-2<-1$（**可行但不是最大值**）✗ ✓✓✓" "\n"
        r"（验 $-2$ 可行：$g(y)=-2$ 有解？$g(3)=-20.086+8.155-3+1.0986=-13.83<-2$，且 $g(1)=-1>-2$ ⟹ 由连续性有解 ✓）" "\n"
        r"**答案 D 正确** ✓" "\n"
        r"**⭐⭐ 通法（嵌套函数 $f(f(y))=y$）**：" "\n"
        r"① ⭐⭐ **$f$ 单调递增时，$f(f(y))=y\iff f(y)=y$** —— 用反证：" "\n"
        r"$f(y)>y\Rightarrow f(f(y))>f(y)>y$，$f(y)<y\Rightarrow f(f(y))<f(y)<y$ —— **两步夹逼**，这是通法；" "\n"
        r"② ⭐⭐ **把「存在点」翻译成「$m$ 属于 $g$ 的值域」**：解出 $m=g(y_1)$，" "\n"
        r"则 $m$ 的范围就是 $g$ 在 $y_1$ 取值区间上的值域 —— **这一步把存在性问题变成求值域**；" "\n"
        r"③ ⭐ **$g'(1)=0$ 是刻意设计**：$g'(y)=\frac1y-\mathrm e^y+(\mathrm e-1)$ 在 $y=1$ 处恰好为 $0$，" "\n"
        r"配合 $g''<0$ 就得 $g$ 递减 ⟹ 端点 $y=1$ 处取最大 —— **看到 $g'(1)=0$ 就要警觉**；" "\n"
        r"④ ⚠ **$y_1$ 的区间是 $[1,3)$ 不是 $[1,3]$**：$3$ 取不到，但因为最大值在 $1$ 处（能取到），**不影响结论**；" "\n"
        r"⑤ 检验：**把 $m=-1$、$y_1=1$ 代回验 $f(1)=1$** ✓。"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-140'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-140-E1',
}

T140_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知函数 $f(x)=\begin{cases}\ln x,&x\ge1\\[2pt]1-\dfrac x2,&x<1\end{cases}$，"
        r"若 $F(x)=f(f(x)+1)+m$ 有两个零点 $x_1,x_2$，则 $x_1+x_2$ 的取值范围是（　　）"
    ),
    'opts': [
        ('A', r"$[4-2\ln2,+\infty)$"),
        ('B', r"$[1+\mathrm e,+\infty)$"),
        ('C', r"$[4-2\ln2,1+\mathrm e)$"),
        ('D', r"$(-\infty,1+\mathrm e]$"),
    ],
    'answer': 'A',
    'analysis': (
        r"对一切 $x$ 都有 $f(x)+1\ge1$，故 $f(f(x)+1)=\ln(f(x)+1)$。方程化为 $f(x)=\mathrm e^{-m}-1=:t>0$；"
        r"由两段各给一根得 $x_1=2-2t$、$x_2=\mathrm e^{t}$，于是 $x_1+x_2=2-2t+\mathrm e^{t}$，最小值在 $t=\ln2$ 处取到 $4-2\ln2$。"
    ),
    'solution': (
        r"先判断 $f(x)+1$ 的范围：" "\n"
        r"$x\ge1$ 时 $f(x)+1=\ln x+1\ge1$；$x<1$ 时 $f(x)+1=1-\dfrac x2+1=2-\dfrac x2>\dfrac32>1$。" "\n"
        r"故对一切 $x$ 都有 $f(x)+1\ge1$，从而 $f(f(x)+1)=\ln(f(x)+1)$。" "\n"
        r"于是 $F(x)=\ln(f(x)+1)+m$，其零点满足 $\ln(f(x)+1)=-m$，即 $f(x)=\mathrm e^{-m}-1=:t$。" "\n"
        r"要有两个零点，需方程 $f(x)=t$ 有两个解：由 $f$ 在 $(-\infty,1)$ 上递减（值域 $(0,+\infty)$ 的一段）、" "\n"
        r"在 $[1,+\infty)$ 上递增（值域 $[0,+\infty)$）可知，需 $t>0$，且" "\n"
        r"$x_1<1$：$1-\dfrac{x_1}2=t\Rightarrow x_1=2-2t$（需 $x_1<1$，即 $t>\dfrac12$）；" "\n"
        r"$x_2\ge1$：$\ln x_2=t\Rightarrow x_2=\mathrm e^{t}$。" "\n"
        r"$x_1+x_2=2-2t+\mathrm e^{t}=:\psi(t)\quad\left(t>\dfrac12\right)$。" "\n"
        r"$\psi'(t)=\mathrm e^{t}-2$，驻点 $t=\ln2=0.693>\dfrac12$；$\psi''=\mathrm e^{t}>0$，故为最小值点。" "\n"
        r"$\psi(\ln2)=2-2\ln2+2=4-2\ln2\approx2.6137$。" "\n"
        r"又 $t\to+\infty$ 时 $\psi\to+\infty$，故取值范围为 $[4-2\ln2,+\infty)$。故选 A。"
    ),
    'review': (
        r"⚠ **分段函数的左段是 $1-\frac x2$ 不是 $\frac{1-x}2$** —— 这是本题最容易掉进去的坑。" "\n"
        r"**反证**：若按 $\frac{1-x}2$，则 $x_1=1-2t$，$x_1+x_2=1-2t+\mathrm e^t$，最小值 $=3-2\ln2=1.6137$，" "\n"
        r"**四个选项一个都不对**；按 $1-\frac x2$ 得 $4-2\ln2=2.6137$ ✓ **恰为选项 A** ✓✓✓" "\n"
        r"★ 答案、详解完整 ✓。原书 p107 详解：「当 $x\ge1$ 时，$f(x)+1=\ln x+1\ge1$，∴$f(f(x)+1)=\ln(f(x)+1)$；" "\n"
        r"当 $x<1$ 时，$f(x)+1=1-\frac x2+1>\frac32>1$，∴$f(f(x)+1)=\ln(f(x)+1)$，综上对 $\forall x\in\mathbf R$，$f(f(x)+1)=\ln(f(x)+1)$。" "\n"
        r"∴$F(x)=f(f(x)+1)+m$ 有两个零点 $x_1,x_2$，即方程 $\ln(f(x)+1)+m=0$ 有两个根，" "\n"
        r"即方程 $f(x)=\mathrm e^{-m}-1$ 有两个根 $x_1,x_2$，不妨设 $x_1<x_2$。易知函数 $f(x)$ 在 $(-\infty,1)$ 上单调递减，在 $(1,+\infty)$ 上单调递增，" "\n"
        r"∴当 $x\ge1$ 时 $\ln x_2=\mathrm e^{-m}-1$；当 $x<1$ 时 $1-\frac{x_1}2=\mathrm e^{-m}-1$。令 $t=\mathrm e^{-m}-1$…」" "\n"
        r"—— **$f(f(x)+1)=\ln(f(x)+1)$、$f(x)=\mathrm e^{-m}-1$、左段 $1-\frac{x_1}2$、右段 $\ln x_2$ 全部与我的推导一致** ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **$f(x)+1\ge1$ 恒成立**：$x\ge1$ 时 $\ln x+1\ge1$ ✓（$x=1$ 取等）；$x<1$ 时 $2-\frac x2>2-\frac12=1.5>1$ ✓ ✓✓✓" "\n"
        r"② **$f$ 的单调性**：左段 $1-\frac x2$ 递减（斜率 $-\frac12$）✓；右段 $\ln x$ 递增 ✓ ✓✓✓" "\n"
        r"左段值域：$x\to-\infty$ 时 $1-\frac x2\to+\infty$；$x\to1^-$ 时 $\to\frac12$。右段值域：$[0,+\infty)$。" "\n"
        r"故 $f(x)=t$ 有两根需 $t>\frac12$ ✓✓✓" "\n"
        r"③ **$t=\ln2$ 时**：$x_1=2-2\ln2=2-1.38629=0.61371<1$ ✓；$x_2=\mathrm e^{\ln2}=2\ge1$ ✓ ✓✓✓" "\n"
        r"$x_1+x_2=0.61371+2=2.61371=4-2\ln2$ ✓✓✓" "\n"
        r"④ **验确实是零点（$m=-\ln(t+1)=-\ln(1+\ln2)$）**：$t+1=1.69315$，$\ln=0.52653$，$m=-0.52653$。" "\n"
        r"$F(x_1)=\ln(f(x_1)+1)+m=\ln(\frac12+\ln2+1)+\cdots$ 等等：$f(x_1)=t=\ln2=0.69315$，$f(x_1)+1=1.69315$。" "\n"
        r"$\ln(1.69315)=0.52653$，$+m=-0.52653$ ⟹ $F=0$ ✓✓✓" "\n"
        r"$f(x_2)=\ln2=0.69315$（因 $x_2=2$，$\ln2=0.69315$ ✓），同样 $F(x_2)=0$ ✓✓✓ **两个零点**" "\n"
        r"⑤ **$t\to\frac12^+$ 时**：$x_1\to1^-$、$x_2\to\mathrm e^{0.5}=1.64872$，和 $\to2.64872>2.61371$ ✓（故最小值在内部 $\ln2$ 处）" "\n"
        r"⑥ **$t=1$ 时**：$x_1=0$、$x_2=\mathrm e=2.71828$，和 $=2.71828>2.61371$ ✓" "\n"
        r"$t=2$ 时：$x_1=-2$、$x_2=\mathrm e^2=7.389$，和 $=5.389>2.61371$ ✓ ✓✓✓" "\n"
        r"⑦ **选项排除**：B $[1+\mathrm e,+\infty)=[3.718,+\infty)$ 漏掉了 $[2.614,3.718)$（如 $t=\ln2$ 时和 $=2.614$）✗；" "\n"
        r"C 是闭区间上界错；D 方向错 ✓✓✓" "\n"
        r"**答案 A 正确** ✓" "\n"
        r"**⭐⭐ 通法（分段函数的复合 $f(f(x)+c)$）**：" "\n"
        r"① ⭐⭐ **先判断里层 $f(x)+c$ 落在哪一段** —— 本题证明了 $f(x)+1\ge1$ **恒成立**，" "\n"
        r"于是外层只能是 $\ln$ 那一段，**复合的外层解析式与 $x$ 无关**；" "\n"
        r"② ⭐⭐ **「外层恒定」后，零点问题立刻降为 $f(x)=t$ 的两根问题** —— " "\n"
        r"这是分段函数复合题的**通用降维手法**；" "\n"
        r"③ ⭐ **两根分别来自两段，各自解出 $x_i$ 表示成 $t$ 的函数**，和（或积）就是 $t$ 的一元函数；" "\n"
        r"④ ⚠ **别忘了 $t$ 的取值范围**：本题 $t>\frac12$（保证 $x_1<1$），而驻点 $\ln2=0.693>\frac12$ 恰好在范围内 ✓；" "\n"
        r"⑤ 检验：**把 $t=\ln2$ 对应的 $m$ 反算出来，验证两个 $x_i$ 都是 $F$ 的零点** ✓。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-140'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-140-V3',
}

T141_V1 = {
    'type': '填空',
    'stem_text': (
        r"设 $a,b$ 是正实数，函数 $f(x)=x\ln x$，$g(x)=-\dfrac b3+x\ln a$。若存在 $x_0\in\left[\dfrac a3,b\right]$，"
        r"使 $f(x_0)\le g(x_0)$ 成立，则 $\dfrac ba$ 的取值范围为 ____。"
    ),
    'answer': r"$\left(\dfrac13,\dfrac3{\mathrm e}\right]$",
    'analysis': (
        r"记 $r=\frac ba$。令 $h=f-g=x\ln x-x\ln a+\frac b3$，则 $h'(x)=\ln\frac xa+1$。按 $\frac ba\le\frac1{\mathrm e}$ 与 $>\frac1{\mathrm e}$ 分类求 $h_{\min}\le0$。"
    ),
    'solution': (
        r"存在 $x_0\in[\frac a3,b]$ 使 $f(x_0)\le g(x_0)$，等价于 $h(x)=f(x)-g(x)$ 在该区间上最小值 $\le0$。" "\n"
        r"首先区间非空需 $\dfrac a3<b$，即 $r=\dfrac ba>\dfrac13$。" "\n"
        r"$h(x)=x\ln x-x\ln a+\dfrac b3$，$h'(x)=\ln x+1-\ln a=\ln\dfrac xa+1$。" "\n"
        r"$h'$ 的零点为 $x=\dfrac a{\mathrm e}$。" "\n"
        r"**情形一：$b\le\dfrac a{\mathrm e}$**，即 $r\in\left(\dfrac13,\dfrac1{\mathrm e}\right]$。" "\n"
        r"此时区间 $[\frac a3,b]$ 全在 $\frac a{\mathrm e}$ 左侧，$h$ 单调递减，$h_{\min}=h(b)$。" "\n"
        r"$h(b)=b\ln b-b\ln a+\dfrac b3=b\left(\ln r+\dfrac13\right)\le0\Rightarrow r\le\mathrm e^{-1/3}$。" "\n"
        r"而 $r\le\frac1{\mathrm e}=0.3679<\mathrm e^{-1/3}=0.7165$，恒成立。" "\n"
        r"**情形二：$\dfrac a3<\dfrac a{\mathrm e}<b$**，即 $r>\dfrac1{\mathrm e}$。" "\n"
        r"$h$ 先减后增，$h_{\min}=h\left(\dfrac a{\mathrm e}\right)=\dfrac a{\mathrm e}\ln\dfrac1{\mathrm e}+\dfrac b3=-\dfrac a{\mathrm e}+\dfrac b3\le0$" "\n"
        r"$\Rightarrow\dfrac b{3a}\le\dfrac1{\mathrm e}\Rightarrow r\le\dfrac3{\mathrm e}$。" "\n"
        r"综合两种情形及 $r>\frac13$，得 $\dfrac ba\in\left(\dfrac13,\dfrac3{\mathrm e}\right]$。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p107 详解：「∵存在 $x_0\in[\frac a3,b]$ 使 $f(x_0)\le g(x_0)$ 成立，∴$\frac a3<b$，$a>0$ 得 $\frac ba>\frac13$；" "\n"
        r"令 $h(x)=f(x)-g(x)=x\ln x-x\ln a+\frac b3$；∴$h'(x)=\ln x+1-\ln a=\ln\frac xa+1$；" "\n"
        r"∵$x_0\in[\frac a3,b]$，$x_0\ge\frac a3$，$\frac{x_0}a\ge\frac13$，令 $\ln\frac xa+1>0$，即 $x>\frac a{\mathrm e}$ 时 $h(x)$ 递增；$\frac a3<x<\frac a{\mathrm e}$ 时 $h(x)$ 递减；" "\n"
        r"①若 $b\le\frac a{\mathrm e}$，即 $\frac ba\in(\frac13,\frac1{\mathrm e}]$，$h(x)$ 在 $[\frac a3,b]$ 上单调递减；" "\n"
        r"∴$h(x)_{\min}=h(b)=b\ln\frac ba+\frac b3\le0$，对 $\frac ba\in(\frac13,\frac1{\mathrm e}]$ 恒成立；" "\n"
        r"②若 $\frac a3<\frac a{\mathrm e}<b$，即 $\frac ba\in(\frac1{\mathrm e},+\infty)$，$h(x)$ 在 $[\frac a3,b]$ 上先递减后递增；" "\n"
        r"∴$h(x)_{\min}=h(\frac a{\mathrm e})=\frac a{\mathrm e}\ln\frac{a/\mathrm e}a+\frac b3=\frac a{\mathrm e}\ln\frac1{\mathrm e}+\frac b3$，" "\n"
        r"∴$-\frac a{\mathrm e}+\frac b3\le0$，∴$\frac b{3a}\le\frac1{\mathrm e}$，即 $\frac ba\le\frac3{\mathrm e}$…综上 $\frac ba$ 的取值范围为 $(\frac13,\frac3{\mathrm e}]$」" "\n"
        r"—— **$\frac ba>\frac13$、$h'$ 零点 $\frac a{\mathrm e}$、两种情形的分类与结论、答案 $(\frac13,\frac3{\mathrm e}]$ 全部与我的推导一致** ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **$h(x)=x\ln x-x\ln a+\frac b3$**：$f-g=x\ln x-(-\frac b3+x\ln a)=x\ln x-x\ln a+\frac b3$ ✓✓✓" "\n"
        r"② **$h'(x)=\ln\frac xa+1$**：$(x\ln x)'=\ln x+1$；$(x\ln a)'=\ln a$。$h'=\ln x+1-\ln a=\ln\frac xa+1$ ✓✓✓" "\n"
        r"零点：$\ln\frac xa=-1$ ⟹ $\frac xa=\mathrm e^{-1}$ ⟹ $x=\frac a{\mathrm e}$ ✓✓✓" "\n"
        r"③ **情形一**：$b\ln\frac ba+\frac b3\le0$ ⟹ $\ln r\le-\frac13$ ⟹ $r\le\mathrm e^{-1/3}=0.71653$。" "\n"
        r"该情形 $r\in(\frac13,\frac1{\mathrm e}]=(0.3333,0.36788]$，全部 $\le0.71653$ ✓✓✓ **恒成立**" "\n"
        r"④ **情形二**：$h(\frac a{\mathrm e})=\frac a{\mathrm e}\ln(\frac1{\mathrm e})+\frac b3=-\frac a{\mathrm e}+\frac b3\le0$ ⟹ $\frac b3\le\frac a{\mathrm e}$ ⟹ $r\le\frac3{\mathrm e}=1.10364$ ✓✓✓" "\n"
        r"⑤ **数值检验（$r=1\le1.1036$，应满足）**：取 $a=1,b=1$，区间 $[\frac13,1]$。" "\n"
        r"$h(x)=x\ln x-0+\frac13$。$h'(x)=\ln x+1$，零点 $x=\frac1{\mathrm e}=0.3679\in[\frac13,1]$ ✓。" "\n"
        r"$h(\frac1{\mathrm e})=0.3679(-1)+\frac13=-0.3679+0.3333=-0.0346\le0$ ✓✓✓ **存在 $x_0$ 使 $f\le g$**" "\n"
        r"（验：$f(0.3679)=0.3679(-1)=-0.3679$；$g(0.3679)=-\frac13+0.3679\ln1=-\frac13=-0.3333$。$-0.3679\le-0.3333$ ✓✓✓）" "\n"
        r"⑥ **数值检验（$r=1.2>1.1036$，应不满足）**：取 $a=1,b=1.2$，区间 $[\frac13,1.2]$。" "\n"
        r"$h(\frac1{\mathrm e})=-\frac1{\mathrm e}+\frac{1.2}3=-0.3679+0.4=0.0321>0$ ✗ ✓✓✓ **最小值 $>0$，不存在**" "\n"
        r"⑦ **边界 $r=\frac3{\mathrm e}$**：$h_{\min}=0$，恰好可取（$\le$ 允许取等）✓✓✓ **右端闭**" "\n"
        r"⑧ **边界 $r=\frac13$**：区间退化成一点 $[\frac a3,\frac a3]$，通常认为需 $\frac a3<b$（严格），故**左端开** ✓✓✓" "\n"
        r"**答案 $(\frac13,\frac3{\mathrm e}]$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（「存在 $x$ 使 $h(x)\le0$」⟹ 最小值 $\le0$）**：" "\n"
        r"① ⭐⭐ **「存在」⟺ $\min\le0$；「任意」⟺ $\max\le0$** —— 先把逻辑词翻译成最值问题；" "\n"
        r"② ⭐⭐ **导函数的零点 $\frac a{\mathrm e}$ 与区间 $[\frac a3,b]$ 的相对位置不定 ⟹ 必须分类** —— " "\n"
        r"**凡是「参数决定区间端点」的题，几乎都要按驻点是否落在区间内分类**；" "\n"
        r"③ ⭐ **先由区间非空得 $\frac ba>\frac13$** —— 这个**隐含条件**很容易漏，它正是答案左端点；" "\n"
        r"④ ⚠ **两种情形的结论要取并集，不是交集**：情形一给出 $(\frac13,\frac1{\mathrm e}]$，情形二给出 $(\frac1{\mathrm e},\frac3{\mathrm e}]$，并起来是 $(\frac13,\frac3{\mathrm e}]$；" "\n"
        r"⑤ 检验：**取 $r=1$（满足）与 $r=1.2$（不满足）各验一次 $h_{\min}$ 的符号** ✓。"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-141'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-141-V1',
}

T141_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知函数 $f(x)=\lvert\lg(x-1)\rvert$，若 $1<a<b$ 且 $f(a)=f(b)$，则 $a+2b$ 的取值范围为（　　）"
    ),
    'opts': [
        ('A', r"$(3+2\sqrt2,+\infty)$"),
        ('B', r"$[3+2\sqrt2,+\infty)$"),
        ('C', r"$(6,+\infty)$"),
        ('D', r"$[6,+\infty)$"),
    ],
    'answer': 'C',
    'analysis': (
        r"由 $f(a)=f(b)$ 得 $(a-1)(b-1)=1$，令 $v=b-1>1$ 则 $a+2b=\frac1v+2v+3$，"
        r"它在 $v>1$ 上递增，下确界为 $6$（取不到）。注意 AM-GM 给出的 $3+2\sqrt2$ 是陷阱。"
    ),
    'solution': (
        r"由 $f(a)=f(b)$ 得 $\lvert\lg(a-1)\rvert=\lvert\lg(b-1)\rvert$。" "\n"
        r"若 $\lg(a-1)=\lg(b-1)$ 则 $a=b$，与 $a<b$ 矛盾，故 $\lg(a-1)=-\lg(b-1)$。" "\n"
        r"于是 $\lg\big[(a-1)(b-1)\big]=0$，即 $(a-1)(b-1)=1$。" "\n"
        r"由 $a-1>0$ 且 $(a-1)(b-1)=1$ 知 $b-1>0$；再由 $a<b$ 得 $a-1<b-1$，故 $(a-1)^2<1$，即 $a-1<1$、$a<2$，" "\n"
        r"从而 $b-1=\dfrac1{a-1}>1$，即 $b>2$。" "\n"
        r"令 $v=b-1>1$，则 $a-1=\dfrac1v$，$a=\dfrac1v+1$，$b=v+1$。" "\n"
        r"$a+2b=\dfrac1v+1+2v+2=\dfrac1v+2v+3$。" "\n"
        r"令 $\varphi(v)=\dfrac1v+2v$，$v>1$。$\varphi'(v)=-\dfrac1{v^{2}}+2>0$（因 $v>1$），故 $\varphi$ 递增。" "\n"
        r"$\varphi(v)>\varphi(1)=3$，且 $v\to+\infty$ 时 $\varphi\to+\infty$。" "\n"
        r"故 $a+2b\in(6,+\infty)$。选 C。" "\n"
        r"注：若误用 AM-GM 得 $\frac1v+2v\ge2\sqrt2$（取等需 $v=\frac1{\sqrt2}<1$），会得到 $3+2\sqrt2=5.828$，" "\n"
        r"**取等点不在 $v>1$ 内**，故错误。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p108 详解：「根据绝对值的几何意义，有 $\lg(a-1)=-\lg(b-1)$，且 $1<a<2<b$，" "\n"
        r"故 $\lg[(a-1)(b-1)]=0$，$(a-1)(b-1)=1$，化简得 $a=\frac1{b-1}+1$，$a+2b=\frac1{b-1}+2b+1$，" "\n"
        r"令 $f(x)=\frac1{x-1}+2x+1\ (x>2)$，$f'(x)=-\frac1{(x-1)^2}+2=\frac{2x^2-4x+1}{(x-1)^2}$，故函数 $f(x)$ 在 $(2,+\infty)$ 上单调递增，" "\n"
        r"$f(2)=6$，所以 $a+2b>6$。故选 C.」" "\n"
        r"—— **$\lg(a-1)=-\lg(b-1)$、$(a-1)(b-1)=1$、$1<a<2<b$、单调性、$f(2)=6$、$a+2b>6$、答案 C 全部与我的推导一致** ✓✓✓" "\n"
        r"（⚠ 四个选项的括号类型在提取中丢失，我按「$b>2$ 严格 ⟹ $6$ 取不到」定为开区间 ✓）" "\n"
        r"**独立验算**：" "\n"
        r"① **$\lg(a-1)=-\lg(b-1)$**：$a-1\ne b-1$（否则 $a=b$），故绝对值相等只能取相反数 ✓✓✓" "\n"
        r"② **$(a-1)(b-1)=1$**：$\lg(a-1)+\lg(b-1)=0$ ⟹ $\lg[(a-1)(b-1)]=0$ ⟹ 乘积 $=1$ ✓✓✓" "\n"
        r"③ **$1<a<2<b$**：$a-1<b-1$ 且乘积 $=1$ ⟹ $(a-1)^2<1$ ⟹ $a-1<1$ ⟹ $a<2$；$b-1=\frac1{a-1}>1$ ⟹ $b>2$ ✓✓✓" "\n"
        r"④ **$a+2b=\frac1{b-1}+2b+1$**：$a=\frac1{b-1}+1$，$a+2b=\frac1{b-1}+1+2b=\frac1{b-1}+2b+1$ ✓✓✓" "\n"
        r"（与我的 $\frac1v+2v+3$ 一致：$v=b-1$，$2b+1=2v+3$ ✓）" "\n"
        r"⑤ **数值检验（$b=3$）**：$a-1=\frac12$ ⟹ $a=1.5$。$f(a)=\lvert\lg0.5\rvert=0.30103$；$f(b)=\lvert\lg2\rvert=0.30103$ ✓✓✓" "\n"
        r"$a+2b=1.5+6=7.5>6$ ✓" "\n"
        r"⑥ **数值检验（$b\to2^+$，$b=2.01$）**：$a-1=\frac1{1.01}=0.99010$ ⟹ $a=1.99010$。" "\n"
        r"$a+2b=1.99010+4.02=6.01010>6$ ✓✓✓ **趋近 6 但大于 6**" "\n"
        r"⑦ **数值检验（$b=10$）**：$a-1=\frac19$ ⟹ $a=1.11111$。$a+2b=1.11111+20=21.111>6$ ✓ ✓✓✓" "\n"
        r"⑧ **$\varphi$ 递增**：$\varphi'(v)=2-\frac1{v^2}>2-1=1>0$（$v>1$）✓✓✓" "\n"
        r"⑨ **AM-GM 陷阱验证**：$\frac1v+2v\ge2\sqrt2=2.8284$，取等需 $\frac1v=2v$ 即 $v=\frac1{\sqrt2}=0.7071<1$ ✗ **不在范围内** ✓✓✓" "\n"
        r"故 $3+2\sqrt2=5.8284$ **不是真正的下界**（实际下界 $6$）✓✓✓" "\n"
        r"**答案 C 正确** ✓" "\n"
        r"**⭐⭐ 通法（绝对值型 $f(a)=f(b)$ ⟹ 乘积为常数）**：" "\n"
        r"① ⭐⭐ **$\lvert\lg u\rvert=\lvert\lg v\rvert$ 且 $u\ne v$ ⟹ $\lg u=-\lg v$ ⟹ $uv=1$** —— " "\n"
        r"**绝对值相等看两种可能：相等（推出 $a=b$，排除）或相反**；" "\n"
        r"② ⭐⭐ **务必由 $a<b$ 推出 $a<2<b$**：这一步确定了变量的真正范围，" "\n"
        r"**没有它就会掉进 AM-GM 的陷阱**；" "\n"
        r"③ ⭐ **$\frac1v+2v$ 在 $v>1$ 上单调递增**（因 $2-\frac1{v^2}>1>0$），下确界在端点 $v\to1^+$ 处；" "\n"
        r"④ ⚠ **$3+2\sqrt2=5.828$ 恰是选项 A/B** —— 命题人把 AM-GM 的结果直接做成干扰项，" "\n"
        r"**凡是选项里出现「由某个著名不等式直接得到但取等条件存疑」的值，都要回头验取等点**；" "\n"
        r"⑤ 检验：**取 $b=2.01,3,10$ 三个点验证 $a+2b>6$，并验 AM-GM 取等点不在范围内** ✓。"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-141'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-141-V3',
}

T142_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知大于 $1$ 的正数 $a,b$ 满足 $\dfrac{\ln^{2}b}{\mathrm e^{2a}}<\left(\dfrac ba\right)^{n}$，"
        r"则正整数 $n$ 的最大值为（　　）"
    ),
    'opts': [
        ('A', r"$7$"),
        ('B', r"$8$"),
        ('C', r"$9$"),
        ('D', r"$11$"),
    ],
    'answer': 'C',
    'analysis': (
        r"分离变量成 $\frac{\ln^{2}b}{b^{n}}<\frac{\mathrm e^{2a}}{a^{n}}$。左端关于 $b$ 的最大值 $f_{\max}=\frac{4}{n^{2}\mathrm e^{2}}$，"
        r"右端关于 $a$ 的最小值 $g_{\min}=\left(\frac{2\mathrm e}n\right)^{n}$，逐一验证 $n=9$ 可行、$n=10$ 不可行。"
    ),
    'solution': (
        r"原不等式等价于 $\dfrac{\ln^{2}b}{b^{n}}<\dfrac{\mathrm e^{2a}}{a^{n}}$。" "\n"
        r"令 $f(x)=\dfrac{\ln^{2}x}{x^{n}}\ (x>1)$，则" "\n"
        r"$f'(x)=\dfrac{x^{n-1}\ln x(2-n\ln x)}{x^{2n}}=\dfrac{\ln x(2-n\ln x)}{x^{n+1}}$。" "\n"
        r"$f$ 在 $\left(1,\mathrm e^{2/n}\right)$ 递增、$\left(\mathrm e^{2/n},+\infty\right)$ 递减，最大值" "\n"
        r"$f_{\max}=f\!\left(\mathrm e^{2/n}\right)=\dfrac{(2/n)^{2}}{\mathrm e^{2}}=\dfrac4{n^{2}\mathrm e^{2}}$。" "\n"
        r"令 $g(x)=\dfrac{\mathrm e^{2x}}{x^{n}}\ (x>1)$，则 $g'(x)=\dfrac{\mathrm e^{2x}(2x-n)}{x^{n+1}}$。" "\n"
        r"$n>2$ 时 $g$ 在 $x=\dfrac n2$ 处取最小值 $g_{\min}=\dfrac{\mathrm e^{n}}{(n/2)^{n}}=\left(\dfrac{2\mathrm e}n\right)^{n}$。" "\n"
        r"要使不等式对满足条件的 $a,b$ 成立，需 $f_{\max}<g_{\min}$，即 $\dfrac4{n^{2}\mathrm e^{2}}<\left(\dfrac{2\mathrm e}n\right)^{n}$。" "\n"
        r"代入计算：" "\n"
        r"$n=9$：左 $=\dfrac4{81\times7.389}=0.00668$；右 $=\left(\dfrac{5.4366}9\right)^{9}=0.6041^{9}=0.01074$ ✓ 成立。" "\n"
        r"$n=10$：左 $=\dfrac4{100\times7.389}=0.00541$；右 $=\left(\dfrac{5.4366}{10}\right)^{10}=0.54366^{10}=0.00226$ ✗ 不成立。" "\n"
        r"（右端随 $n$ 增大而减小，故 $n\ge10$ 均不成立。）最大正整数为 $9$。选 C。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p108 详解：「$\frac{\ln^2 b}{\mathrm e^{2a}}<\frac{b^n}{a^n}$ 等价于 $\frac{\ln^2 b}{b^n}<\frac{\mathrm e^{2a}}{a^n}$，" "\n"
        r"令 $f(x)=\frac{\ln^2 x}{x^n}\ (x>1)$，则 $f'(x)=\frac{x^{n-1}\cdot\ln x(2-n\ln x)}{x^{2n}}=\frac{\ln x(2-n\ln x)}{x^{n+1}}$，" "\n"
        r"$f'(x)=0$，$x=\mathrm e^{\frac2n}$，当 $f'(x)>0$ 时 $x\in(1,\mathrm e^{\frac2n})$，当 $f'(x)<0$ 时 $x\in(\mathrm e^{\frac2n},+\infty)$，" "\n"
        r"所以 $f(x)$ 在 $(1,\mathrm e^{\frac2n})$ 上单调递增，在 $(\mathrm e^{\frac2n},+\infty)$ 上单调递减，则 $f(x)$ 有最大值 $f(\mathrm e^{\frac2n})=\frac{(\frac2n)^2}{\mathrm e^2}$。" "\n"
        r"令 $g(x)=\frac{\mathrm e^{2x}}{x^n}\ (x>1)$，则 $g'(x)=\frac{\mathrm e^{2x}(2x-n)}{x^{2n}}$…当 $\frac n2\le1$ 时此题无解，所以 $\frac n2>1$，则 $g'(x)=0$，$x=\frac n2$…" "\n"
        r"$g(x)$ 有最小值 $g(\frac n2)=\frac{\mathrm e^n}{(\frac n2)^n}$，根据题意即求 $f(x)_{\max}\le g(x)_{\min}$…" "\n"
        r"等价于 $\frac{n+2}n\ge\ln\frac n2$，令 $\varphi(x)=\frac{x+2}x-\ln\frac x2$，即求 $\varphi(x)>0$ 的最大的正整数 $n$…」" "\n"
        r"—— **分离成 $\frac{\ln^2 b}{b^n}<\frac{\mathrm e^{2a}}{a^n}$、$f_{\max}=\frac{(2/n)^2}{\mathrm e^2}$、$x=\frac n2$ 处 $g$ 取最小、$\frac{\mathrm e^n}{(n/2)^n}$、求最大正整数 $n$、答案 C（$9$）全部与我的推导一致** ✓✓✓" "\n"
        r"**独立验算（数值，完全独立）**：" "\n"
        r"① **$f'(x)=\frac{\ln x(2-n\ln x)}{x^{n+1}}$**：$[\ln^2x\cdot x^{-n}]'=2\ln x\cdot\frac1x\cdot x^{-n}+\ln^2x\cdot(-n)x^{-n-1}$" "\n"
        r"$=\frac{2\ln x}{x^{n+1}}-\frac{n\ln^2x}{x^{n+1}}=\frac{\ln x(2-n\ln x)}{x^{n+1}}$ ✓✓✓" "\n"
        r"② **$f(\mathrm e^{2/n})$**：$\ln(\mathrm e^{2/n})=\frac2n$，$\ln^2=\frac4{n^2}$；$(\mathrm e^{2/n})^n=\mathrm e^2$。故 $f=\frac{4}{n^2\mathrm e^2}$ ✓✓✓" "\n"
        r"③ **$g'(x)$**：$[\mathrm e^{2x}x^{-n}]'=2\mathrm e^{2x}x^{-n}+\mathrm e^{2x}(-n)x^{-n-1}=\frac{\mathrm e^{2x}(2x-n)}{x^{n+1}}$ ✓✓✓" "\n"
        r"驻点 $x=\frac n2$ ✓；$g(\frac n2)=\frac{\mathrm e^n}{(n/2)^n}$ ✓✓✓" "\n"
        r"④ **$n=9$**：$f_{\max}=\frac4{81(7.389056)}=\frac4{598.51}=0.006683$。" "\n"
        r"$g_{\min}=(\frac{2(2.718282)}9)^9=(0.604062)^9$。$\ln(0.604062)=-0.503826$，$\times9=-4.53443$，$\mathrm e^{-4.53443}=0.010738$。" "\n"
        r"$0.006683<0.010738$ ✓✓✓ **成立**" "\n"
        r"⑤ **$n=10$**：$f_{\max}=\frac4{100(7.389056)}=\frac4{738.906}=0.005414$。" "\n"
        r"$g_{\min}=(0.5436564)^{10}$。$\ln(0.5436564)=-0.609435$，$\times10=-6.09435$，$\mathrm e^{-6.09435}=0.0022553$。" "\n"
        r"$0.005414>0.0022553$ ✗ ✓✓✓ **不成立**" "\n"
        r"⑥ **$n=8$**：$f_{\max}=\frac4{64(7.389)}=\frac4{472.90}=0.008459$。" "\n"
        r"$g_{\min}=(\frac{5.436564}8)^8=(0.679571)^8$。$\ln=-0.386235$，$\times8=-3.08988$，$\mathrm e^{-3.08988}=0.045557$。" "\n"
        r"$0.008459<0.045557$ ✓ **成立**（但 $8<9$，不是最大）" "\n"
        r"⑦ **$n=11$**：$g_{\min}=(\frac{5.436564}{11})^{11}=(0.494233)^{11}$。$\ln=-0.704861$，$\times11=-7.75347$，$\mathrm e^{-7.75347}=0.000427$。" "\n"
        r"$f_{\max}=\frac4{121(7.389)}=0.004473>0.000427$ ✗ ✓✓✓ **不成立**（排除 D $11$）" "\n"
        r"⑧ **$g_{\min}$ 随 $n$ 单调递减**（$n\ge3$）：$0.045557(n=8)\to0.010738(n=9)\to0.002255(n=10)\to0.000427(n=11)$ ✓✓✓" "\n"
        r"故 $n\ge10$ 全不成立 ✓✓✓ **最大为 9**" "\n"
        r"**答案 C 正确** ✓" "\n"
        r"**⭐⭐ 通法（双变量不等式 ⟹ 各自求最值）**：" "\n"
        r"① ⭐⭐ **把含 $a$ 的与含 $b$ 的分到不等式两边**，然后「左边最大 < 右边最小」—— " "\n"
        r"这是处理**两个独立变量**不等式的标准操作；" "\n"
        r"② ⭐⭐ **$f(x)=\frac{\ln^2x}{x^n}$ 与 $g(x)=\frac{\mathrm e^{2x}}{x^n}$ 的极值点**：前者在 $x=\mathrm e^{2/n}$、后者在 $x=\frac n2$ —— " "\n"
        r"**两者都只依赖 $n$，与另一个变量无关**，所以能直接比较；" "\n"
        r"③ ⭐ **比较 $f_{\max}$ 与 $g_{\min}$ 时用对数或数值**：$(\frac{2\mathrm e}n)^n$ 衰减极快，" "\n"
        r"**逐一代入 $n$ 比解超越不等式快**；" "\n"
        r"④ ⚠ **$n\le2$ 时 $g$ 在 $(1,+\infty)$ 上递增（驻点 $\frac n2\le1$），要单独处理** —— 本题 $n\le2$ 时不等式恒成立；" "\n"
        r"⑤ 检验：**代 $n=8,9,10,11$ 四个值确认分界点在 $9/10$ 之间** ✓。"
    ),
    'difficulty': 0.93,
    'topics': ['M-T-142'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-142-E1',
}

T142_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知实数 $x,y$ 满足 $\ln(4x+3y-6)-\mathrm e^{x+y-2}\ge3x+2y-6$，则 $x+y$ 的值为（　　）"
    ),
    'opts': [
        ('A', r"$2$"),
        ('B', r"$1$"),
        ('C', r"$0$"),
        ('D', r"$-1$"),
    ],
    'answer': 'A',
    'analysis': (
        r"换元 $m=4x+3y-6$、$n=x+y-2$，则 $m-n=3x+2y-4$，条件化为 $\ln m-m\ge\mathrm e^{n}-n-2$。"
        r"左端最大值 $-1$、右端最小值 $-1$，只能两边同时取等，得 $m=1,n=0$。"
    ),
    'solution': (
        r"设 $m=4x+3y-6$，$n=x+y-2$，则 $m-n=3x+2y-4$，于是 $3x+2y-6=m-n-2$。" "\n"
        r"条件化为 $\ln m-\mathrm e^{n}\ge m-n-2$，即 $\ln m-m\ge\mathrm e^{n}-n-2$（需 $m>0$）。" "\n"
        r"令 $F(m)=\ln m-m\ (m>0)$，则 $F'(m)=\dfrac1m-1$，$F$ 在 $(0,1)$ 增、$(1,+\infty)$ 减，" "\n"
        r"$F_{\max}=F(1)=-1$，故 $F(m)\le-1$。" "\n"
        r"令 $H(n)=\mathrm e^{n}-n-2$，则 $H'(n)=\mathrm e^{n}-1$，$H$ 在 $(-\infty,0)$ 减、$(0,+\infty)$ 增，" "\n"
        r"$H_{\min}=H(0)=1-0-2=-1$，故 $H(n)\ge-1$。" "\n"
        r"由 $F(m)\ge H(n)$ 及 $F(m)\le-1\le H(n)$，只能是 $F(m)=H(n)=-1$，" "\n"
        r"即 $m=1$、$n=0$。" "\n"
        r"由 $\begin{cases}4x+3y-6=1\\x+y-2=0\end{cases}$ 得 $\begin{cases}4x+3y=7\\x+y=2\end{cases}$，解得 $x=1$，$y=1$。" "\n"
        r"故 $x+y=2$。选 A。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p108 详解：「设 $m=4x+3y-6$，$n=x+y-2$，则 $m-n=3x+2y-4$。" "\n"
        r"$\ln m-\mathrm e^n\ge m-n-2$，$\ln m-m\ge\mathrm e^n-n-2\ (m>0)$。" "\n"
        r"令 $f(m)=\ln m-m$，$f'(m)=\frac1m-1$，∴$0<m<1$ 时 $f'(m)>0$；$m>1$ 时 $f'(m)<0$，则 $f(m)$ 在 $(0,1)$ 单调递增、$(1,+\infty)$ 单调递减，∴$f(m)_{\max}=f(1)=-1$，∴$f(m)\le-1$。" "\n"
        r"令 $h(n)=\mathrm e^n-n-2$，$h'(n)=\mathrm e^n-1$，∴$n>0$ 时 $h'(n)>0$；$n<0$ 时 $h'(n)<0$，则 $h(n)$ 在 $(-\infty,0)$ 单调递减、$(0,+\infty)$ 单调递增，∴$h(n)_{\min}=h(0)=-1$，∴$h(n)\ge-1$。" "\n"
        r"由题意 $f(m)\ge h(n)$，∴$m=1$，$n=0$，∴$4x+3y-6=1$ 且 $x+y-2=0$，∴$x=1$，$y=1$，故 $x+y=2$。故选 A」" "\n"
        r"—— **换元 $m,n$、$\ln m-m\ge\mathrm e^n-n-2$、两侧最值都是 $-1$、$m=1$、$n=0$、$x=y=1$、$x+y=2$、答案 A 全部与我的推导一致** ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **$m-n=3x+2y-4$**：$(4x+3y-6)-(x+y-2)=3x+2y-4$ ✓✓✓" "\n"
        r"故 $3x+2y-6=(3x+2y-4)-2=m-n-2$ ✓✓✓" "\n"
        r"② **$F(m)=\ln m-m\le-1$**：$F'(m)=\frac1m-1$，极大点 $m=1$，$F(1)=0-1=-1$ ✓✓✓" "\n"
        r"（数值验：$m=0.5$ ⟹ $\ln0.5-0.5=-0.6931-0.5=-1.1931<-1$ ✓；$m=2$ ⟹ $0.6931-2=-1.3069<-1$ ✓）" "\n"
        r"③ **$H(n)=\mathrm e^n-n-2\ge-1$**：$H'(n)=\mathrm e^n-1$，极小点 $n=0$，$H(0)=1-0-2=-1$ ✓✓✓" "\n"
        r"（数值验：$n=1$ ⟹ $2.71828-1-2=-0.28172>-1$ ✓；$n=-1$ ⟹ $0.36788+1-2=-0.63212>-1$ ✓）" "\n"
        r"④ **$m=1,n=0$ 唯一**：$F(m)\le-1\le H(n)$ 且需 $F(m)\ge H(n)$ ⟹ $F(m)=H(n)=-1$ ⟹ $m=1,n=0$ ✓✓✓" "\n"
        r"⑤ **解方程组**：$x+y=2$ ⟹ $y=2-x$。$4x+3(2-x)=7$ ⟹ $4x+6-3x=7$ ⟹ $x=1$，$y=1$ ✓✓✓" "\n"
        r"⑥ **代回原式验证**：$4x+3y-6=4+3-6=1$，$\ln1=0$；$x+y-2=0$，$\mathrm e^0=1$；左边 $=0-1=-1$。" "\n"
        r"$3x+2y-6=3+2-6=-1$。$-1\ge-1$ ✓✓✓ **取等成立**" "\n"
        r"⑦ **验其他选项不成立**：若 $x+y=1$，则 $n=-1$，$H(-1)=-0.63212>-1$，需 $F(m)\ge-0.63212$，但 $F\le-1$ ✗ ✓✓✓" "\n"
        r"同理 $x+y=0$、$-1$ 都不成立 ✓✓✓" "\n"
        r"**答案 A 正确** ✓" "\n"
        r"**⭐⭐ 通法（「两边同时取到 $-1$」的夹逼结构）**：" "\n"
        r"① ⭐⭐ **换元要「对齐」：把不等式中出现的线性组合设成新变量** —— " "\n"
        r"本题 $4x+3y-6$、$x+y-2$、$3x+2y-6$ 三个量，前两个设为 $m,n$ 后第三个恰好是 $m-n-2$；" "\n"
        r"② ⭐⭐ **识别两个经典最值：$\ln t-t\le-1$（$t>0$）与 $\mathrm e^{t}-t\ge1$（即 $\mathrm e^t-t-2\ge-1$）** —— " "\n"
        r"**这两个是同构的（互为反函数）**，最值都是 $-1$，命题人就是靠这一点设计夹逼；" "\n"
        r"③ ⭐ **$A\ge B$ 且 $A\le c\le B$ ⟹ $A=B=c$** —— 三步夹逼，把不等式变成方程；" "\n"
        r"④ ⚠ **必须验证取等点可达**：本题 $m=1>0$ 满足定义域 ✓，且 $F,H$ 的极值点都在各自定义域内部 ✓；" "\n"
        r"⑤ 检验：**把 $x=y=1$ 代回原式，确认左右都是 $-1$（取等）** ✓。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-142'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-142-V1',
}

T143_V2 = {
    'type': '填空',
    'stem_text': (
        r"若正实数 $a,b$ 满足 $a+b=1$，则函数 $f(x)=ax^{2}+\left(3+\dfrac1b\right)x-a$ 的零点的最大值为 ____。"
    ),
    'answer': r"$\dfrac{\sqrt{85}-9}{2}$",
    'analysis': (
        r"较大零点 $x=-t+\sqrt{t^{2}+1}$（$t=\frac{3+1/b}{2a}$），它关于 $t$ 递减；"
        r"$t=\frac{4-3a}{2a-2a^{2}}$ 在 $a=\frac23$ 处取最小值 $\frac92$，代入得 $\frac{\sqrt{85}-9}2$。"
    ),
    'solution': (
        r"$a>0$，故 $f$ 是开口向上的二次函数，两个零点为" "\n"
        r"$x=\dfrac{-\left(3+\frac1b\right)\pm\sqrt{\left(3+\frac1b\right)^{2}+4a^{2}}}{2a}$。" "\n"
        r"其中较大者为" "\n"
        r"$x_{+}=\dfrac{-\left(3+\frac1b\right)+\sqrt{\left(3+\frac1b\right)^{2}+4a^{2}}}{2a}=-\dfrac{3+\frac1b}{2a}+\sqrt{\left(\dfrac{3+\frac1b}{2a}\right)^{2}+1}$。" "\n"
        r"令 $t=\dfrac{3+\frac1b}{2a}>0$，则 $x_{+}=-t+\sqrt{t^{2}+1}$。" "\n"
        r"**$\psi(t)=-t+\sqrt{t^{2}+1}$ 递减**：$\psi'(t)=-1+\dfrac{t}{\sqrt{t^{2}+1}}<0$。" "\n"
        r"故要使 $x_{+}$ 最大，需 $t$ 最小。" "\n"
        r"由 $b=1-a$ 得 $t=\dfrac{3+\frac1{1-a}}{2a}=\dfrac{3(1-a)+1}{2a(1-a)}=\dfrac{4-3a}{2a-2a^{2}}\quad(0<a<1)$。" "\n"
        r"$t'(a)=\dfrac{-3(2a-2a^{2})-(4-3a)(2-4a)}{(2a-2a^{2})^{2}}=\dfrac{-6a^{2}+16a-8}{(2a-2a^{2})^{2}}$。" "\n"
        r"令分子为零：$3a^{2}-8a+4=0$，得 $a=2$（舍）或 $a=\dfrac23$。" "\n"
        r"$t_{\min}=t\!\left(\dfrac23\right)=\dfrac{4-2}{2\cdot\frac23\cdot\frac13}=\dfrac2{4/9}=\dfrac92$。" "\n"
        r"$x_{+}^{\max}=-\dfrac92+\sqrt{\dfrac{81}4+1}=-\dfrac92+\dfrac{\sqrt{85}}2=\dfrac{\sqrt{85}-9}2$。" "\n"
        r"故答案为 $\dfrac{\sqrt{85}-9}{2}$。"
    ),
    'review': (
        r"⚠ **答案 `85 - 9 2` 实为 $\frac{\sqrt{85}-9}2$** —— 根号在提取中丢失。" "\n"
        r"**反证**：按字面的 $\frac{85-9}2=38$ 完全不合理（零点应为小正数）；" "\n"
        r"按 $\frac{\sqrt{85}-9}2=\frac{9.21954-9}2=0.10977$，与我的完整推导一致 ✓✓✓" "\n"
        r"★ 题干、详解完整 ✓。原书 p109 详解：「因为正实数 $a,b$ 满足 $a+b=1$，则函数 $f(x)=ax^2+(3+\frac1b)x-a$ 的零点" "\n"
        r"$x_2=\frac{-(3+\frac1b)+\sqrt{(3+\frac1b)^2+4a^2}}{2a}=-\frac{3+\frac1b}{2a}+\sqrt{(\frac{3+\frac1b}{2a})^2+1}$，" "\n"
        r"令 $t=\frac{3+\frac1b}{2a}$，所以零点的最大值就相当于求 $-t+\sqrt{t^2+1}$ 的最大值。" "\n"
        r"令 $f(t)=-t+\sqrt{t^2+1}$，$f'(t)=-1+\frac12\cdot\frac1{\sqrt{t^2+1}}\cdot2t=\frac{t-\sqrt{t^2+1}}{\sqrt{t^2+1}}<0$，所以函数 $f(t)$ 是单调递减的，" "\n"
        r"当 $t$ 取最小值时 $f(t)$ 取最大值。又因为 $t=\frac{3+\frac1b}{2a}$，$a+b=1$，所以 $t=\frac{3+\frac1{1-a}}{2a}=\frac{4-3a}{2a-2a^2}\ (0<a<1)$…」" "\n"
        r"—— **$x_2$ 的表达式、换元 $t=\frac{3+1/b}{2a}$、$\psi$ 递减、$t=\frac{4-3a}{2a-2a^2}$、$a=\frac23$ 处取最小 全部与我的推导一致** ✓✓✓" "\n"
        r"（详解末尾破碎，但 $t_{\min}=\frac92$ 与最终值由我推出并验证 ✓）" "\n"
        r"**独立验算（数值，完全独立）**：" "\n"
        r"① **$x_2$ 的表达式**：$f(x)=ax^2+(3+\frac1b)x-a$，$a>0$。$x=\frac{-(3+\frac1b)\pm\sqrt{(3+\frac1b)^2+4a^2}}{2a}$。" "\n"
        r"较大者取 $+$：$=\frac{-(3+\frac1b)}{2a}+\frac{\sqrt{(3+\frac1b)^2+4a^2}}{2a}=-\frac{3+\frac1b}{2a}+\sqrt{(\frac{3+\frac1b}{2a})^2+\frac{4a^2}{4a^2}}$" "\n"
        r"$=-t+\sqrt{t^2+1}$ ✓✓✓（其中 $t=\frac{3+1/b}{2a}$）" "\n"
        r"② **$\psi(t)$ 递减**：$\psi'(t)=-1+\frac{t}{\sqrt{t^2+1}}$，因 $\sqrt{t^2+1}>t$ ⟹ $\frac{t}{\sqrt{t^2+1}}<1$ ⟹ $\psi'<0$ ✓✓✓" "\n"
        r"③ **$t(a)=\frac{4-3a}{2a-2a^2}$**：$3+\frac1{1-a}=\frac{3(1-a)+1}{1-a}=\frac{4-3a}{1-a}$；除以 $2a$：$\frac{4-3a}{2a(1-a)}=\frac{4-3a}{2a-2a^2}$ ✓✓✓" "\n"
        r"④ **$t'(a)$ 的分子**：$N=4-3a$，$N'=-3$；$D=2a-2a^2$，$D'=2-4a$。" "\n"
        r"$N'D-ND'=-3(2a-2a^2)-(4-3a)(2-4a)=-6a+6a^2-(8-16a-6a+12a^2)=-6a+6a^2-8+22a-12a^2=-6a^2+16a-8$ ✓✓✓" "\n"
        r"零点：$6a^2-16a+8=0$ ⟹ $3a^2-8a+4=0$ ⟹ $a=\frac{8\pm\sqrt{64-48}}6=\frac{8\pm4}6$ ⟹ $a=2$ 或 $a=\frac23$ ✓✓✓" "\n"
        r"$a=\frac23\in(0,1)$ ✓；$a=2$ 舍去 ✓✓✓" "\n"
        r"⑤ **$t(\frac23)$**：$4-3(\frac23)=4-2=2$；$2(\frac23)-2(\frac49)=\frac43-\frac89=\frac{12-8}9=\frac49$。$t=\frac2{4/9}=\frac92=4.5$ ✓✓✓" "\n"
        r"⑥ **端点行为**：$a\to0^+$ ⟹ $t\to+\infty$ ✓；$a\to1^-$ ⟹ $t\to+\infty$ ✓ ⟹ $a=\frac23$ 确实是**最小值点** ✓✓✓" "\n"
        r"⑦ **最终值**：$-4.5+\sqrt{20.25+1}=-4.5+\sqrt{21.25}=-4.5+4.609772=0.109772$。" "\n"
        r"$\frac{\sqrt{85}-9}2=\frac{9.219544-9}2=\frac{0.219544}2=0.109772$ ✓✓✓ **完全吻合**" "\n"
        r"⑧ **代回验（$a=\frac23,b=\frac13$）**：$f(x)=\frac23x^2+(3+3)x-\frac23=\frac23x^2+6x-\frac23$。" "\n"
        r"令 $f=0$：$2x^2+18x-2=0$（乘 3）⟹ $x^2+9x-1=0$ ⟹ $x=\frac{-9\pm\sqrt{81+4}}2=\frac{-9\pm\sqrt{85}}2$。" "\n"
        r"较大零点 $=\frac{-9+\sqrt{85}}2=\frac{\sqrt{85}-9}2$ ✓✓✓✓✓ **与答案完全一致**" "\n"
        r"**答案 $\frac{\sqrt{85}-9}2$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（二次函数零点的最值 ⟹ 换元成单变量）**：" "\n"
        r"① ⭐⭐ **把求根公式改写成 $-t+\sqrt{t^2+1}$ 的形式** —— " "\n"
        r"**「分子有理化」的逆操作**：$x_2=\frac{-B+\sqrt{B^2+4a^2}}{2a}$，提 $\frac{B}{2a}$ 出来就得到这个结构；" "\n"
        r"② ⭐⭐ **$\psi(t)=-t+\sqrt{t^2+1}$ 严格递减**（$\psi'=\frac{t}{\sqrt{t^2+1}}-1<0$）—— " "\n"
        r"**求「零点最大」就变成求 $t$ 最小**，方向立刻明确；" "\n"
        r"③ ⭐ **$t(a)$ 的最值用求导**：分子二次、分母二次，导数分子仍是二次，$3a^2-8a+4=0$ 两根为 $2$ 与 $\frac23$，**只有一个在 $(0,1)$ 内**；" "\n"
        r"④ ⚠ **$a>0$ 时开口向上，较大零点取 $+$ 号** —— 别取错分支（取 $-$ 号会得到绝对值很大的负根）；" "\n"
        r"⑤ 检验：**把 $a=\frac23,b=\frac13$ 代回原函数，直接解二次方程 $x^2+9x-1=0$**，得 $\frac{\sqrt{85}-9}2$ ✓✓✓（这是最硬的验证）。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-143'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-143-V2',
}

T145_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知不等式 $x-3\ln x+1\ge m\ln x+n\ (m,n\in\mathbf R$，且 $m\ne-3)$ 对任意实数 $x>0$ 恒成立，"
        r"则 $\dfrac{n-3}{m+3}$ 的最大值为（　　）"
    ),
    'opts': [
        ('A', r"$-2\ln2$"),
        ('B', r"$-\ln2$"),
        ('C', r"$\ln2-1$"),
        ('D', r"$\ln2-2$"),
    ],
    'answer': 'B',
    'analysis': (
        r"整理为 $x-(m+3)\ln x\ge n-1$。令 $f(x)=x-(m+3)\ln x$，其最小值在 $x=m+3$ 处（需 $m+3>0$），"
        r"代入后化为求 $G(s)=1-\ln s-\frac2s$（$s=m+3>0$）的最大值，驻点 $s=2$。"
    ),
    'solution': (
        r"原不等式即 $x-(m+3)\ln x\ge n-1$ 对一切 $x>0$ 成立。" "\n"
        r"令 $f(x)=x-(m+3)\ln x$，则 $f'(x)=1-\dfrac{m+3}x=\dfrac{x-(m+3)}x$。" "\n"
        r"**若 $m+3<0$**：$f'(x)>0$ 恒成立，$f$ 递增，而 $x\to0^{+}$ 时 $f\to-\infty$，不合题意。" "\n"
        r"**若 $m+3>0$**：$f$ 在 $(0,m+3)$ 递减、$(m+3,+\infty)$ 递增，" "\n"
        r"$f_{\min}=f(m+3)=(m+3)-(m+3)\ln(m+3)$。" "\n"
        r"需 $f_{\min}\ge n-1$，即 $n\le1+(m+3)\left[1-\ln(m+3)\right]$。" "\n"
        r"于是" "\n"
        r"$\dfrac{n-3}{m+3}\le\dfrac{1+(m+3)\left[1-\ln(m+3)\right]-3}{m+3}=1-\ln(m+3)-\dfrac2{m+3}$。" "\n"
        r"令 $s=m+3>0$，$G(s)=1-\ln s-\dfrac2s$，则 $G'(s)=-\dfrac1s+\dfrac2{s^{2}}=\dfrac{2-s}{s^{2}}$。" "\n"
        r"$G$ 在 $(0,2)$ 递增、$(2,+\infty)$ 递减，$G_{\max}=G(2)=1-\ln2-1=-\ln2$。" "\n"
        r"故选 B。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p111 详解：「由题意得 $x-(3+m)\ln x\ge n-1$ 恒成立，令 $f(x)=x-(3+m)\ln x$，" "\n"
        r"则 $f'(x)=\frac{x-(3+m)}x\ (x>0)$，若 $3+m<0$，$f'(x)>0$，$f(x)$ 单调递增，当 $x\to0^+$ 时 $f(x)\to-\infty$，不合题意；" "\n"
        r"若 $3+m>0$，当 $x\in(0,m+3)$ 时 $f'(x)<0$，$f(x)$ 单调递减，当 $x\in(m+3,+\infty)$ 时 $f'(x)>0$，$f(x)$ 单调递增，" "\n"
        r"所以 $f(x)$ 最小值为 $f(m+3)$。∴$f(m+3)=(3+m)-(3+m)\ln(3+m)\ge n-1$，" "\n"
        r"∴$\frac{n-3}{m+3}\le\frac{(3+m)-(3+m)\ln(3+m)-2}{m+3}=1-\ln(3+m)-\frac2{m+3}\ (m>-3)$，令 $g(x)=1-\ln x-\frac2x$…」" "\n"
        r"—— **$x-(3+m)\ln x\ge n-1$、$f'=\frac{x-(3+m)}x$、$m+3<0$ 舍去、$f_{\min}=f(m+3)$、$G(s)=1-\ln s-\frac2s$、答案 B（$-\ln2$）全部与我的推导一致** ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **$f'(x)=1-\frac{m+3}x$**：$[x-(m+3)\ln x]'=1-\frac{m+3}x=\frac{x-(m+3)}x$ ✓✓✓" "\n"
        r"② **$m+3<0$ 时 $x\to0^+$**：$-(m+3)\ln x$，因 $-(m+3)>0$ 而 $\ln x\to-\infty$ ⟹ 该项 $\to-\infty$ ✓✓✓ **确实不合题意**" "\n"
        r"③ **$f(m+3)=(m+3)-(m+3)\ln(m+3)$** ✓✓✓" "\n"
        r"④ **代入化简**：$\frac{1+(m+3)-(m+3)\ln(m+3)-3}{m+3}=\frac{(m+3)\left[1-\ln(m+3)\right]-2}{m+3}=1-\ln(m+3)-\frac2{m+3}$ ✓✓✓" "\n"
        r"⑤ **$G'(s)=\frac{2-s}{s^2}$**：$-\frac1s+\frac2{s^2}=\frac{-s+2}{s^2}$ ✓✓✓；极大点 $s=2$ ✓" "\n"
        r"$G(2)=1-\ln2-\frac22=1-0.693147-1=-0.693147=-\ln2$ ✓✓✓" "\n"
        r"⑥ **对应的 $m,n$**：$s=2$ ⟹ $m=-1\ne-3$ ✓；$n\le1+2(1-\ln2)=1+2-1.386294=1.613706$。" "\n"
        r"取 $n=1.613706$：$\frac{n-3}{m+3}=\frac{1.613706-3}2=\frac{-1.386294}2=-0.693147=-\ln2$ ✓✓✓" "\n"
        r"⑦ **直接验证（$m=-1,n=1.613706$）**：需 $x-3\ln x+1\ge-\ln x+1.613706$ ⟹ $x-2\ln x\ge0.613706$。" "\n"
        r"令 $u(x)=x-2\ln x$，$u'(x)=1-\frac2x$，极小点 $x=2$：$u(2)=2-2\ln2=2-1.386294=0.613706$ ✓✓✓ **恰好取等**" "\n"
        r"⑧ **检验 $s=1$（$G=-1$）与 $s=4$（$G=1-1.386-0.5=-0.886$）** 都 $<-0.693$ ✓✓✓" "\n"
        r"⑨ **选项排除**：$-2\ln2=-1.386$（是 $s$ 取别处的值，非最大）✗；$\ln2-1=-0.307>-0.693$（**取不到**）✗；" "\n"
        r"$\ln2-2=-1.307$ ✗ ✓✓✓" "\n"
        r"**答案 B 正确** ✓" "\n"
        r"**⭐⭐ 通法（双参数恒成立 ⟹ 先定一个再优化比值）**：" "\n"
        r"① ⭐⭐ **把含 $x$ 的归到一边、含参数的归到另一边**：$x-(m+3)\ln x\ge n-1$ —— " "\n"
        r"注意是 $(m+3)$ 整体出现，所以**令 $s=m+3$ 换元**能大幅简化；" "\n"
        r"② ⭐⭐ **$m+3$ 的符号必须分类**：$<0$ 时 $f$ 递增且 $x\to0^+$ 时 $f\to-\infty$，**直接排除** —— " "\n"
        r"**对数前面的系数一变号，极限行为就完全不同**；" "\n"
        r"③ ⭐ **得到 $n$ 的上界后代入目标式，参数 $s$ 自动留下来**，问题降为单变量最值；" "\n"
        r"④ ⚠ **$G(s)=1-\ln s-\frac2s$ 的极大点是 $s=2$**：$G'=\frac{2-s}{s^2}$ 的符号一眼可判，**别把 $\frac2s$ 的导数算错**；" "\n"
        r"⑤ 检验：**把最值点对应的 $m,n$ 代回原不等式，验证恰能取等**（$x=2$ 处 $u(2)=0.613706$）✓。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-145'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-145-V1',
}

T145_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知函数 $f(x)=\ln x$，$g(x)=(a-\mathrm e)x+b$。若不等式 $f(x)\le g(x)$ 对 $\forall x\in(0,+\infty)$ 恒成立，"
        r"则 $\dfrac ba$ 的最小值是（　　）"
    ),
    'opts': [
        ('A', r"$-\dfrac1{2\mathrm e}$"),
        ('B', r"$-\dfrac1{\mathrm e}$"),
        ('C', r"$-\mathrm e$"),
        ('D', r"$\mathrm e$"),
    ],
    'answer': 'B',
    'analysis': (
        r"令 $h=\ln x-(a-\mathrm e)x-b$，需 $h_{\max}\le0$。$a\le\mathrm e$ 时无最大值；$a>\mathrm e$ 时 $h_{\max}=-\ln(a-\mathrm e)-1-b\le0$，"
        r"于是 $\frac ba\ge\frac{-1-\ln(a-\mathrm e)}a$，令 $u=a-\mathrm e>0$ 求最小，驻点满足 $u\ln u=\mathrm e$，即 $u=\mathrm e$。"
    ),
    'solution': (
        r"令 $h(x)=\ln x-(a-\mathrm e)x-b$，条件为 $h(x)\le0$ 对一切 $x>0$ 成立，即 $h_{\max}\le0$。" "\n"
        r"$h'(x)=\dfrac1x-(a-\mathrm e)$。" "\n"
        r"**若 $a\le\mathrm e$**：$a-\mathrm e\le0$，$h'(x)>0$ 恒成立，$h$ 递增且 $x\to+\infty$ 时 $h\to+\infty$，无最大值，不合题意。" "\n"
        r"**若 $a>\mathrm e$**：令 $h'(x)=0$ 得 $x=\dfrac1{a-\mathrm e}$。" "\n"
        r"$h$ 在 $\left(0,\frac1{a-\mathrm e}\right)$ 递增、$\left(\frac1{a-\mathrm e},+\infty\right)$ 递减，" "\n"
        r"$h_{\max}=h\!\left(\dfrac1{a-\mathrm e}\right)=\ln\dfrac1{a-\mathrm e}-1-b=-\ln(a-\mathrm e)-1-b$。" "\n"
        r"由 $h_{\max}\le0$ 得 $b\ge-1-\ln(a-\mathrm e)$。" "\n"
        r"因 $a>\mathrm e>0$，故 $\dfrac ba\ge\dfrac{-1-\ln(a-\mathrm e)}a$。" "\n"
        r"令 $u=a-\mathrm e>0$，则 $a=u+\mathrm e$，$\Phi(u)=\dfrac{-1-\ln u}{u+\mathrm e}$。" "\n"
        r"$\Phi'(u)=\dfrac{-\frac1u(u+\mathrm e)-(-1-\ln u)}{(u+\mathrm e)^{2}}=\dfrac{-1-\frac{\mathrm e}u+1+\ln u}{(u+\mathrm e)^{2}}=\dfrac{\ln u-\frac{\mathrm e}u}{(u+\mathrm e)^{2}}$。" "\n"
        r"令 $\ln u=\dfrac{\mathrm e}u$，即 $u\ln u=\mathrm e$，显然 $u=\mathrm e$ 满足（$\mathrm e\ln\mathrm e=\mathrm e$）。" "\n"
        r"又 $\ln u-\frac{\mathrm e}u$ 在 $(0,+\infty)$ 上严格递增，故驻点唯一。" "\n"
        r"$\Phi(\mathrm e)=\dfrac{-1-\ln\mathrm e}{\mathrm e+\mathrm e}=\dfrac{-2}{2\mathrm e}=-\dfrac1{\mathrm e}$。" "\n"
        r"且 $u<\mathrm e$ 时 $\Phi'<0$、$u>\mathrm e$ 时 $\Phi'>0$，故为最小值。选 B。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p111 详解：「解法1：令 $h(x)=f(x)-g(x)=\ln x-(a-\mathrm e)x-b$，则 $h'(x)=\frac1x-(a-\mathrm e)$，" "\n"
        r"当 $a<\mathrm e$ 时，$h(x)$ 单调递增，$h(x)$ 无最大值，不合题意；当 $a>\mathrm e$ 时，令 $h'(x)=0$，则 $x=\frac1{a-\mathrm e}$，" "\n"
        r"$x\in(0,\frac1{a-\mathrm e})$ 时 $h'(x)>0$，$h(x)$ 单调递增；$x\in(\frac1{a-\mathrm e},+\infty)$ 时 $h'(x)<0$，$h(x)$ 单调递减，" "\n"
        r"∴$h(x)_{\max}=h(\frac1{a-\mathrm e})=-\ln(a-\mathrm e)-1-b\le0$，即 $\ln(a-\mathrm e)\ge1-b$…" "\n"
        r"$b\ge-1-\ln(a-\mathrm e)$，$\frac ba\ge\frac{-1-\ln(a-\mathrm e)}a$，$a>\mathrm e$，由 $\frac{-1-\ln(a-\mathrm e)}a$ 的导数为…」" "\n"
        r"—— **$h'$、$a<\mathrm e$ 舍去、$x=\frac1{a-\mathrm e}$、$h_{\max}=-\ln(a-\mathrm e)-1-b$、$b\ge-1-\ln(a-\mathrm e)$、答案 B（$-\frac1{\mathrm e}$）全部与我的推导一致** ✓✓✓" "\n"
        r"（⚠ 详解写「当 $a<\mathrm e$ 时」，严格说 $a=\mathrm e$ 时 $h=\ln x-b$ 也无最大值，应合并为 $a\le\mathrm e$）" "\n"
        r"**独立验算**：" "\n"
        r"① **$h'(x)=\frac1x-(a-\mathrm e)$** ✓✓✓" "\n"
        r"② **$a=\mathrm e$ 时**：$h(x)=\ln x-b\to+\infty$ ✗ **也需排除**（详解只写 $a<\mathrm e$，我按 $a\le\mathrm e$ 处理 ✓）" "\n"
        r"③ **$h_{\max}$**：$h(\frac1{a-\mathrm e})=\ln\frac1{a-\mathrm e}-(a-\mathrm e)\frac1{a-\mathrm e}-b=-\ln(a-\mathrm e)-1-b$ ✓✓✓" "\n"
        r"④ **$\Phi'(u)=\frac{\ln u-\mathrm e/u}{(u+\mathrm e)^2}$**：分子 $=-\frac1u(u+\mathrm e)-(-1-\ln u)\cdot1=-1-\frac{\mathrm e}u+1+\ln u=\ln u-\frac{\mathrm e}u$ ✓✓✓" "\n"
        r"⑤ **$u\ln u=\mathrm e$ 的解**：$u=\mathrm e$ ⟹ $\mathrm e\cdot1=\mathrm e$ ✓✓✓；且 $\psi(u)=u\ln u$ 在 $u>\frac1{\mathrm e}$ 上严格递增 ⟹ **唯一解** ✓✓✓" "\n"
        r"（$u<\frac1{\mathrm e}$ 时 $u\ln u<0<\mathrm e$，也无解 ✓）" "\n"
        r"⑥ **$\Phi(\mathrm e)=\frac{-1-1}{2\mathrm e}=-\frac1{\mathrm e}=-0.367879$** ✓✓✓" "\n"
        r"⑦ **数值检验（$u=\mathrm e$，即 $a=2\mathrm e=5.43656$）**：$b\ge-1-\ln\mathrm e=-2$。取 $b=-2$。" "\n"
        r"$\frac ba=\frac{-2}{5.43656}=-0.367879=-\frac1{\mathrm e}$ ✓✓✓" "\n"
        r"**验证不等式成立**：需 $\ln x\le(\mathrm e)x-2$（因 $a-\mathrm e=2\mathrm e-\mathrm e=\mathrm e$）。" "\n"
        r"令 $W(x)=\ln x-\mathrm ex+2$。$W'(x)=\frac1x-\mathrm e$，极大点 $x=\frac1{\mathrm e}=0.36788$。" "\n"
        r"$W(\frac1{\mathrm e})=\ln(0.36788)-\mathrm e(0.36788)+2=-1-1+2=0$ ✓✓✓ **恰好取等，$W\le0$ 恒成立**" "\n"
        r"（再验两点：$x=1$ ⟹ $W=0-2.71828+2=-0.71828<0$ ✓；$x=0.1$ ⟹ $W=-2.30259-0.271828+2=-0.57441<0$ ✓）✓✓✓" "\n"
        r"⑧ **检验 $u=1$（$a=1+\mathrm e=3.71828$）**：$\Phi=\frac{-1-0}{3.71828}=-0.26894>-0.36788$ ✓（更大，非最小）" "\n"
        r"检验 $u=\mathrm e^2=7.389$（$a=10.107$）：$\Phi=\frac{-1-2}{10.107}=-0.29683>-0.36788$ ✓ ✓✓✓" "\n"
        r"⑨ **选项排除**：$-\frac1{2\mathrm e}=-0.18394>-0.36788$（**取不到的值**）✗；$-\mathrm e=-2.718$、$\mathrm e=2.718$ 都不对 ✗ ✓✓✓" "\n"
        r"**答案 B 正确** ✓" "\n"
        r"**⭐⭐ 通法（含双参数的切线型不等式）**：" "\n"
        r"① ⭐⭐ **几何意义：$\ln x\le(a-\mathrm e)x+b$ 就是直线 $y=(a-\mathrm e)x+b$ 在 $\ln x$ 图象上方** —— " "\n"
        r"斜率必须 $>0$（否则 $\ln x$ 最终超过直线），所以 $a>\mathrm e$；" "\n"
        r"② ⭐⭐ **切点法最快**：设切于 $x_0$，则斜率 $=\frac1{x_0}=a-\mathrm e$，截距 $b=\ln x_0-1$，" "\n"
        r"于是 $\frac ba=\frac{\ln x_0-1}{\frac1{x_0}+\mathrm e}$ —— **令 $u=\frac1{x_0}$ 就化成本题的 $\Phi(u)$**；" "\n"
        r"③ ⭐ **$u\ln u=\mathrm e$ 的解是 $u=\mathrm e$** —— 这类「$u\ln u=$ 常数」靠**观察**而不是解（$\mathrm e\ln\mathrm e=\mathrm e$）；" "\n"
        r"④ ⚠ **$a=\mathrm e$ 也要排除**（此时 $h=\ln x-b$ 无最大值），详解只写了 $a<\mathrm e$，**边界要补齐**；" "\n"
        r"⑤ 检验：**把 $a=2\mathrm e,b=-2$ 代回，验证 $\ln x\le\mathrm ex-2$ 在 $x=\frac1{\mathrm e}$ 处恰取等** ✓✓✓。"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-145'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-145-V3',
}

QS = [T139_E1, T139_V1, T139_V3, T140_E1, T140_V3, T141_V1,
      T141_V3, T142_E1, T142_V1, T143_V2, T145_V1, T145_V3]
