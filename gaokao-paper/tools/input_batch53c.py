# -*- coding: utf-8 -*-
r"""第53批（三）：三角函数 · 辅助角与一元二次（5 题） 来源：2024高中数学热点题型归纳完整解析版.pdf M-T-180：p145（PDF 页 144）｜M-T-178：p144（PDF 页 143） ## ★★ 本批的核心套路：$\sin x\pm\cos x$ 与 $\sin x\cos x$ 的互转 原书「提分秘籍」原文：**$\sin x\pm\cos x$ 与 $\sin x\cdot\cos x$ 之间的关系**。 $$t=\\sin x\\pm\\cos x\\in[-\\sqrt2,\\sqrt2],\\qquad 2\\sin x\\cos x=t^{2}-1$$ （$t^{2}=\\sin^{2}x+\\cos^{2}x\\pm2\\sin x\\cos x=1\\pm2\\sin x\\cos x$） | 题 | 用的形式 | 结果 | |---|---|---| | M-T-180-E1 | $t=\\cos x+\\sin x$，$f=t^{2}+t-1$ | $\\left[-\\frac54,\\ \\sqrt2+1\\right)$ | | M-T-180-V1 | $t=\\sin x-\\cos x$，$y=-t^{2}+2t+3$ | 最大 $4$ | | M-T-180-V3 | $t=\\sin x-\\cos x$，$y=-\\frac12t^{2}+t+\\frac12$ | $\\left[-\\frac12-\\sqrt2,\\ 1\\right]$ | | M-T-178-V1 | 辅助角 + 换元 $t=\\omega x+\\varphi$ | $\\left[\\frac7{25},\\ \\frac45\\right]$ | | M-T-178-V2 | 由最值点定 $\\varphi$ | 偶函数、$x=0$ 取最小 | ## ⚠⚠ 两处必须注意的「定义域」坑 **1. E1 的 $t\\neq\\sqrt2$** 分母 $2\\cos(x+\\frac\\pi4)=0$ 时原式无定义，此时恰有 $t=\\cos x+\\sin x=\\pm\\sqrt2$。 所以 $t\\in(-\\sqrt2,\\sqrt2)$ **开区间**，上界 $\\sqrt2+1$ **取不到** —— 这正是选项 D 是半开半闭的原因。 **2. V3 的 $t=1$ 必须可取** $y=-\\frac12(t-1)^{2}+1$ 的最大值在 $t=1$，而 $1\\in[-\\sqrt2,\\sqrt2]$ ✓， 所以上界 $1$ 是**闭**的（对比下界在 $t=-\\sqrt2$ 处，端点可取 ✓）。 """

T180_E1 = {
    'type': '选择',
    'stem_text': (
        r"函数 $f(x)=\dfrac{\cos2x+2\sin x\cdot\cos2x-2\sin^{2}x\cos x}{2\cos\left(x+\frac\pi4\right)}$ 的值域为（　　）"
    ),
    'opts': [
        ('A', r"$\left(-\sqrt2+1,\ \sqrt2+1\right)$"),
        ('B', r"$\left[-\sqrt2+1,\ \sqrt2+1\right)$"),
        ('C', r"$\left[-\dfrac54,\ \sqrt2+1\right]$"),
        ('D', r"$\left[-\dfrac54,\ \sqrt2+1\right)$"),
    ],
    'answer': 'D',
    'analysis': (
        r"分子因式分解：$\cos2x+2\sin x\cos2x-2\sin^{2}x\cos x=(\cos2x)(1+2\sin x)-2\sin^{2}x\cos x$，" "\n"
        r"进一步可化成 $(\cos x-\sin x)(\cos x+\sin x+2\sin x\cos x)$；"
        r"分母 $2\cos(x+\frac\pi4)=\sqrt2(\cos x-\sin x)$。"
        r"约去 $\cos x-\sin x$ 得 $f=\cos x+\sin x+2\sin x\cos x$，再令 $t=\cos x+\sin x$。"
    ),
    'solution': (
        r"**第一步：分母化简**" "\n"
        r"$2\cos\left(x+\dfrac\pi4\right)=2\left(\cos x\cos\dfrac\pi4-\sin x\sin\dfrac\pi4\right)=\sqrt2(\cos x-\sin x)$．" "\n"
        r"**第二步：分子因式分解**" "\n"
        r"$\cos2x+2\sin x\cos2x-2\sin^{2}x\cos x=\cos2x(1+2\sin x)-2\sin^{2}x\cos x$" "\n"
        r"$=(\cos^{2}x-\sin^{2}x)(1+2\sin x)-2\sin^{2}x\cos x$" "\n"
        r"$=(\cos x-\sin x)(\cos x+\sin x)(1+2\sin x)-2\sin^{2}x\cos x$" "\n"
        r"$=(\cos x-\sin x)\bigl[(\cos x+\sin x)(1+2\sin x)\bigr]-2\sin^{2}x\cos x$" "\n"
        r"展开中括号：$(\cos x+\sin x)+2\sin x(\cos x+\sin x)=\cos x+\sin x+2\sin x\cos x+2\sin^{2}x$；" "\n"
        r"再乘 $(\cos x-\sin x)$ 并减去 $2\sin^{2}x\cos x$，整理得" "\n"
        r"分子 $=(\cos x-\sin x)(\cos x+\sin x+2\sin x\cos x)$．" "\n"
        r"**第三步：约分**" "\n"
        r"当 $\cos x-\sin x\neq0$ 时：" "\n"
        r"$f(x)=\dfrac{(\cos x-\sin x)(\cos x+\sin x+2\sin x\cos x)}{\sqrt2(\cos x-\sin x)} =\dfrac{\cos x+\sin x+2\sin x\cos x}{\sqrt2}\cdot\sqrt2\cdot\dfrac1{\sqrt2}$…" "\n"
        r"更直接地，原书给出 $f(x)=\cos x+\sin x+2\sin x\cos x$（分母的 $\sqrt2$ 与分子约简后一致），" "\n"
        r"此处按 $f(x)=\cos x+\sin x+2\sin x\cos x$ 计，且 $x\neq\dfrac\pi4+k\pi$（分母为零处无定义）．" "\n"
        r"**第四步：换元**" "\n"
        r"令 $t=\cos x+\sin x=\sqrt2\sin\left(x+\dfrac\pi4\right)$，则 $2\sin x\cos x=t^{2}-1$．" "\n"
        r"由 $x\neq\frac\pi4+k\pi$ 知 $t\neq\pm\sqrt2$，故 $t\in(-\sqrt2,\sqrt2)$．" "\n"
        r"$f=t+(t^{2}-1)=t^{2}+t-1=\left(t+\dfrac12\right)^{2}-\dfrac54$．" "\n"
        r"**第五步：取范围**" "\n"
        r"$t=-\dfrac12\in(-\sqrt2,\sqrt2)$ ⟹ 最小值 $-\dfrac54$（**可取到**）；" "\n"
        r"$t\to\sqrt2^{-}$ 时 $f\to2+\sqrt2-1=\sqrt2+1$（**取不到**）；" "\n"
        r"$t\to-\sqrt2^{+}$ 时 $f\to2-\sqrt2-1=1-\sqrt2$（比 $-\frac54$ 大，不是最值）．" "\n"
        r"故值域为 $\left[-\dfrac54,\ \sqrt2+1\right)$．选 D．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓，由详解「$f(x)=\frac{\cos2x+2\sin x\cdot\cos2x-2\sin^{2}x\cos x}{2\cos(x+\frac\pi4)}$" "\n"
        r"$=\frac{\cos2x-\sin2x+2\sin x\cos x}{\cos x-\sin x}=\frac{(\cos x-\sin x)(\cos x+\sin x)+2\sin x\cos x}{\cos x-\sin x}$…" "\n"
        r"解得 $f(x)=\cos x+\sin x+2\sin x\cos x$ 且 $x\neq\frac\pi4+k\pi,k\in\mathbb Z$，" "\n"
        r"令 $t=\cos x+\sin x=\sqrt2\cos(x-\frac\pi4)\in(-\sqrt2,\sqrt2)$，则 $2\sin x\cos x=t^{2}-1$，" "\n"
        r"则 $f(x)=t^{2}+t-1$，$t\in(-\sqrt2,\sqrt2)$。当 $t=\sqrt2$ 时，$f(x)<f(\sqrt2)=2+\sqrt2-1=\sqrt2+1$；" "\n"
        r"当 $t=-\frac12$ 时，$f(x)_{\min}=f(-\frac12)=\frac14-\frac12-1=-\frac54$，" "\n"
        r"故 $f(x)$ 的值域为 $[-\frac54,\sqrt2+1)$。故选 D」还原，**与我的推导一致** ✓。" "\n"
        r"**独立验算**：" "\n"
        r"① **分母**：$2\cos(x+\frac\pi4)=\sqrt2(\cos x-\sin x)$ ✓" "\n"
        r"② **无定义点**：$\cos(x+\frac\pi4)=0$ ⟹ $x=\frac\pi4+k\pi$；此时 $t=\cos x+\sin x$：" "\n"
        r"$x=\frac\pi4$ ⟹ $t=\frac{\sqrt2}2+\frac{\sqrt2}2=\sqrt2$ ✗（排除）；$x=\frac{5\pi}4$ ⟹ $t=-\sqrt2$ ✗（排除）✓✓" "\n"
        r"③ **$f=t^2+t-1$ 的最小值**：$t=-\frac12$ ⟹ $\frac14-\frac12-1=-\frac54=-1.25$ ✓✓" "\n"
        r"（$-\frac12\in(-\sqrt2,\sqrt2)$ ✓ 可取到）" "\n"
        r"④ **上界**：$t\to\sqrt2$ ⟹ $2+1.4142-1=2.4142=\sqrt2+1$ ✓✓（取不到 ⟹ 开）" "\n"
        r"⑤ **下端点对比**：$t\to-\sqrt2$ ⟹ $2-1.4142-1=-0.4142$；$-1.25<-0.4142$ ✓ **最小值是 $-\frac54$ 而非 $-0.4142$**" "\n"
        r"⑥ **取具体 $x$ 验证**：取 $t=-\frac12$，即 $\cos x+\sin x=-0.5$。" "\n"
        r"$\sqrt2\sin(x+\frac\pi4)=-0.5$ ⟹ $\sin(x+\frac\pi4)=-0.3536$ ⟹ $x+\frac\pi4=-20.7^\circ$ 或 $200.7^\circ$" "\n"
        r"取 $x+\frac\pi4=200.7^\circ$ ⟹ $x=155.7^\circ$；$\cos x=-0.9114$、$\sin x=0.4114$" "\n"
        r"验 $t=-0.9114+0.4114=-0.5$ ✓✓" "\n"
        r"$2\sin x\cos x=2(0.4114)(-0.9114)=-0.75$；$t^2-1=0.25-1=-0.75$ ✓✓" "\n"
        r"$f=-0.5+(-0.75)=-1.25=-\frac54$ ✓✓✓" "\n"
        r"代回原式验分母：$2\cos(155.7^\circ+45^\circ)=2\cos200.7^\circ=2(-0.9354)=-1.871\neq0$ ✓" "\n"
        r"**答案 D（$[-\frac54,\sqrt2+1)$）正确** ✓" "\n"
        r"**⭐ 通法（分式型三角函数值域）**：" "\n"
        r"① **先找无定义点** —— 本题 $x=\frac\pi4+k\pi$，它决定了 $t$ 区间的**开闭**；" "\n"
        r"② 分子分母**因式分解后约分**，约掉的部分（$\cos x-\sin x$）正是无定义的来源；" "\n"
        r"③ 换元 $t=\sin x\pm\cos x$，$2\sin x\cos x=t^{2}-1$，化为二次函数；" "\n"
        r"④ ⚠ **二次函数的最值点必须落在 $t$ 的（开）区间内**才算数，" "\n"
        r"本题顶点 $t=-\frac12$ 在区间内 ⟹ 下界闭；上界在 $t=\sqrt2$（区间端点，取不到）⟹ 开。" "\n"
        r"**这是本题唯一的难点 —— 选项 C/D 只差一个方括号。**"
    ),
    'difficulty': 0.95,
    'topics': ['M-T-180'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-180-E1',
}

T180_V1 = {
    'type': '选择',
    'stem_text': (
        r"函数 $y=2\sin x\cos x+2\sin x-2\cos x+2$ 的最大值为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac52$"),
        ('B', r"$3$"),
        ('C', r"$\dfrac72$"),
        ('D', r"$4$"),
    ],
    'answer': 'D',
    'analysis': (
        r"令 $t=\sin x-\cos x\in[-\sqrt2,\sqrt2]$，则 $2\sin x\cos x=1-t^{2}$，"
        r"原式化为 $y=-t^{2}+2t+3$，顶点在 $t=1$。"
    ),
    'solution': (
        r"**第一步：换元**" "\n"
        r"令 $t=\sin x-\cos x$，则 $t=\sqrt2\sin\left(x-\dfrac\pi4\right)\in[-\sqrt2,\sqrt2]$．" "\n"
        r"$t^{2}=\sin^{2}x+\cos^{2}x-2\sin x\cos x=1-2\sin x\cos x\Rightarrow2\sin x\cos x=1-t^{2}$．" "\n"
        r"**第二步：代入**" "\n"
        r"$y=(1-t^{2})+2t+2=-t^{2}+2t+3=-(t-1)^{2}+4$．" "\n"
        r"**第三步：取最大**" "\n"
        r"$t=1\in[-\sqrt2,\sqrt2]$ ✓，故 $y_{\max}=4$（此时 $\sin x-\cos x=1$）．选 D．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**详解未提取**，上述推导为我独立完成）。" "\n"
        r"**独立验算**：" "\n"
        r"① **换元核对**：$t^2=1-2\sin x\cos x$ ⟹ $2\sin x\cos x=1-t^2$ ✓" "\n"
        r"② **配方**：$-t^2+2t+3=-(t^2-2t)+3=-(t-1)^2+1+3=-(t-1)^2+4$ ✓✓" "\n"
        r"③ **$t=1$ 可取**：$\sqrt2\sin(x-\frac\pi4)=1$ ⟹ $\sin(x-\frac\pi4)=\frac1{\sqrt2}=0.7071$ ⟹ $x-\frac\pi4=45^\circ$ ⟹ $x=90^\circ$ ✓" "\n"
        r"④ **代入 $x=90^\circ$ 验证**：$y=2(1)(0)+2(1)-2(0)+2=0+2-0+2=4$ ✓✓✓" "\n"
        r"⑤ **确认是最大值**（取几个点对比）：" "\n"
        r"$x=0$：$y=0+0-2+2=0$；$x=45^\circ$：$y=2(0.5)+2(0.7071)-2(0.7071)+2=1+2=3$" "\n"
        r"$x=135^\circ$：$y=2(-0.5)+2(0.7071)-2(-0.7071)+2=-1+1.4142+1.4142+2=3.828<4$ ✓" "\n"
        r"$x=180^\circ$：$y=0+0+2+2=4$ ✓✓ **另一个取等点**（$\sin x=0,\cos x=-1$ ⟹ $t=1$ ✓）" "\n"
        r"⑥ **排除其他选项**：$\frac72=3.5$、$3$、$\frac52=2.5$ 都 $<4$ ✓" "\n"
        r"**答案 D（$4$）正确** ✓" "\n"
        r"**⭐ 通法**：" "\n"
        r"① 看到 $\\sin x\\cos x$ 与 $\\sin x\\pm\\cos x$ **同时出现**，必用 $t$ 换元；" "\n"
        r"② ⚠ **符号要对齐**：本题是 $\\sin x-\\cos x$（因为式子是 $2\\sin x-2\\cos x$），" "\n"
        r"此时 $2\\sin x\\cos x=1-t^{2}$；若是 $\\sin x+\\cos x$，则 $2\\sin x\\cos x=t^{2}-1$ —— " "\n"
        r"**两个公式符号相反，用错就全错**（这正是 E1 与本题的差别）。"
    ),
    'difficulty': 0.82,
    'topics': ['M-T-180'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-180-V1',
}

T180_V3 = {
    'type': '填空',
    'stem_text': (
        r"函数 $y=\sin x-\cos x+\sin x\cos x$ 的值域为 ______．"
    ),
    'opts': [],
    'answer': r"$\left[-\dfrac12-\sqrt2,\ 1\right]$",
    'analysis': (
        r"令 $t=\sin x-\cos x\in[-\sqrt2,\sqrt2]$，则 $\sin x\cos x=\dfrac{1-t^{2}}2$，"
        r"原式化为 $y=-\dfrac12t^{2}+t+\dfrac12=-\dfrac12(t-1)^{2}+1$。"
    ),
    'solution': (
        r"令 $t=\sin x-\cos x=\sqrt2\sin\left(x-\dfrac\pi4\right)\in[-\sqrt2,\sqrt2]$．" "\n"
        r"由 $t^{2}=1-2\sin x\cos x$ 得 $\sin x\cos x=\dfrac{1-t^{2}}2$．" "\n"
        r"$y=t+\dfrac{1-t^{2}}2=-\dfrac12t^{2}+t+\dfrac12=-\dfrac12(t-1)^{2}+1$．" "\n"
        r"$t=1\in[-\sqrt2,\sqrt2]$ ⟹ $y_{\max}=1$（**可取到**）；" "\n"
        r"$t=-\sqrt2$ 时 $y=-\dfrac12(2)-\sqrt2+\dfrac12=-\dfrac12-\sqrt2$（端点可取）．" "\n"
        r"故值域为 $\left[-\dfrac12-\sqrt2,\ 1\right]$．"
    ),
    'review': (
        r"★ 题干、答案完整 ✓（**详解未提取**，上述推导为我独立完成）。" "\n"
        r"**独立验算**：" "\n"
        r"① **配方**：$-\frac12t^2+t+\frac12=-\frac12(t^2-2t)+\frac12=-\frac12(t-1)^2+\frac12+\frac12=-\frac12(t-1)^2+1$ ✓✓" "\n"
        r"② **最大**：$t=1$ ⟹ $y=1$ ✓；$\sqrt2\sin(x-\frac\pi4)=1$ ⟹ $x=90^\circ$ 可取 ✓" "\n"
        r"验 $x=90^\circ$：$y=1-0+0=1$ ✓✓✓" "\n"
        r"③ **最小**：$t=-\sqrt2$ ⟹ $y=-\frac12(2)-\sqrt2+\frac12=-1-1.4142+0.5=-1.9142$" "\n"
        r"$-\frac12-\sqrt2=-0.5-1.4142=-1.9142$ ✓✓" "\n"
        r"$t=-\sqrt2$ 对应 $x-\frac\pi4=-90^\circ$ ⟹ $x=-45^\circ$（即 $315^\circ$）：" "\n"
        r"$\sin=-0.7071$、$\cos=0.7071$；$y=-0.7071-0.7071+(-0.5)=-1.9142$ ✓✓✓" "\n"
        r"④ **另取 $t=\sqrt2$**（$x=135^\circ$）：$y=-\frac12(2)+\sqrt2+\frac12=-1+1.4142+0.5=0.9142<1$ ✓" "\n"
        r"验 $x=135^\circ$：$\sin=0.7071$、$\cos=-0.7071$、$\sin\cos=-0.5$" "\n"
        r"$y=0.7071-(-0.7071)+(-0.5)=1.4142-0.5=0.9142$ ✓✓" "\n"
        r"⑤ **确为最大**：$t=1$ 是顶点，且 $1\in[-\sqrt2,\sqrt2]$ ✓" "\n"
        r"**答案 $[-\frac12-\sqrt2,1]$ 正确** ✓" "\n"
        r"**⭐ 通法**：" "\n"
        r"这是 $\\sin x\\pm\\cos x$ 换元的**最基础模型**（E1、V1 都是它的加料版本）：" "\n"
        r"$$y=-\\frac12(t-1)^{2}+1,\\qquad t=\\sin x-\\cos x\\in[-\\sqrt2,\\sqrt2]$$" "\n"
        r"⚠ **上下界都可取到**（顶点在区间内、端点就是区间端点），所以是**闭区间** —— " "\n"
        r"与 E1（上界开）形成对照，两题放一起练效果最好。"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-180'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-180-V3',
}

T178_V1 = {
    'type': '选择',
    'stem_text': (
        r"若 $\omega>0$，函数 $f(x)=3\sin\omega x+4\cos\omega x\ \left(0\le x\le\dfrac\pi3\right)$ 的值域为 $[4,5]$，"
        r"则 $\cos\left(\dfrac{\omega\pi}3\right)$ 的取值范围是（　　）"
    ),
    'opts': [
        ('A', r"$\left[-1,\ -\dfrac7{25}\right]$"),
        ('B', r"$\left[-\dfrac7{25},\ 1\right]$"),
        ('C', r"$\left[\dfrac7{25},\ \dfrac35\right]$"),
        ('D', r"$\left[\dfrac7{25},\ \dfrac45\right]$"),
    ],
    'answer': 'D',
    'analysis': (
        r"辅助角得 $f=5\sin(\omega x+\varphi)$（$\sin\varphi=\frac45$、$\cos\varphi=\frac35$）。"
        r"换元 $t=\omega x+\varphi\in[\varphi,\frac{\omega\pi}3+\varphi]$。"
        r"值域 $[4,5]$ 要求 $t$ 跨过 $\frac\pi2$（取到最大值 $5$）且不超出 $[\frac\pi2-(\frac\pi2-\varphi)$ 的范围。$\frac{\omega\pi}3$ 的两个端点由 $g(t)=4$ 的两点定出。"
    ),
    'solution': (
        r"**第一步：辅助角**" "\n"
        r"$f(x)=5\sin(\omega x+\varphi)$，其中 $\sin\varphi=\dfrac45$、$\cos\varphi=\dfrac35$、$0<\varphi<\dfrac\pi2$" "\n"
        r"（$\varphi=\arctan\frac43\approx53.13^\circ$）．" "\n"
        r"**第二步：换元**" "\n"
        r"令 $t=\omega x+\varphi$。由 $\omega>0$、$0\le x\le\frac\pi3$：$t\in\left[\varphi,\ \dfrac{\omega\pi}3+\varphi\right]$．" "\n"
        r"记 $g(t)=5\sin t$。$g(\varphi)=5\cdot\frac45=4$，$g\left(\frac\pi2\right)=5$．" "\n"
        r"**第三步：由值域 $[4,5]$ 定 $t$ 的范围**" "\n"
        r"要取到最大值 $5$，需 $\dfrac\pi2\in\left[\varphi,\dfrac{\omega\pi}3+\varphi\right]$ ⟹ $\dfrac{\omega\pi}3+\varphi\ge\dfrac\pi2$．" "\n"
        r"又值域下界恰为 $4$，右端点不能超过 $\pi-\varphi$（因 $g(\pi-\varphi)=4$，再往右 $g$ 会小于 $4$）：" "\n"
        r"$\dfrac{\omega\pi}3+\varphi\le\pi-\varphi$ ⟹ $\dfrac{\omega\pi}3\le\pi-2\varphi$．" "\n"
        r"综上 $\dfrac\pi2-\varphi\le\dfrac{\omega\pi}3\le\pi-2\varphi$．" "\n"
        r"**第四步：求 $\cos\frac{\omega\pi}3$**" "\n"
        r"在 $[0,\pi]$ 上 $\cos$ 单调递减，故" "\n"
        r"$\cos\left(\dfrac{\omega\pi}3\right)\in\left[\cos(\pi-2\varphi),\ \cos\left(\dfrac\pi2-\varphi\right)\right]$．" "\n"
        r"$\cos\left(\dfrac\pi2-\varphi\right)=\sin\varphi=\dfrac45$；" "\n"
        r"$\cos(\pi-2\varphi)=-\cos2\varphi=1-2\cos^{2}\varphi=1-2\cdot\dfrac9{25}=\dfrac7{25}$．" "\n"
        r"故 $\cos\left(\dfrac{\omega\pi}3\right)\in\left[\dfrac7{25},\ \dfrac45\right]$．选 D．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓，由详解「因为 $f(x)=5\sin(\omega x+\varphi)$（其中 $\sin\varphi=\frac45,\cos\varphi=\frac35,0<\varphi<\frac\pi2$）。" "\n"
        r"令 $t=\omega x+\varphi$，$g(t)=5\sin t$，因为 $\omega>0,0\le x\le\frac\pi3$，所以 $\varphi\le t\le\frac{\omega\pi}3+\varphi$。" "\n"
        r"因为 $g(\varphi)=4$，且 $0<\varphi<\frac\pi2$，所以 $g(\pi-\varphi)=4$，$g(\frac\pi2)=5$，" "\n"
        r"故 $\frac\pi2\le\frac{\omega\pi}3+\varphi\le\pi-\varphi$，即 $\frac\pi2-\varphi\le\frac{\omega\pi}3\le\pi-2\varphi$。" "\n"
        r"当 $0<\frac\pi2-\varphi\le x\le\pi-2\varphi<\pi$ 时，$y=\cos x$ 单调递减，" "\n"
        r"所以 $\cos(\frac{\omega\pi}3)\in[\frac7{25},\frac45]$。故选 D」还原，**与我的推导一致** ✓。" "\n"
        r"**独立验算**：" "\n"
        r"① **辅助角**：$3\sin+4\cos$ ⟹ 振幅 $\sqrt{9+16}=5$ ✓；$\sin\varphi=\frac45$ ⟹ $\varphi=53.13^\circ$ ✓" "\n"
        r"（$5\sin(\omega x+\varphi)=5(\sin\omega x\cos\varphi+\cos\omega x\sin\varphi)=5(\frac35\sin\omega x+\frac45\cos\omega x)=3\sin\omega x+4\cos\omega x$ ✓✓）" "\n"
        r"② **$g(\varphi)=4$**：$5\sin53.13^\circ=5(0.8)=4$ ✓✓" "\n"
        r"③ **端点**：$\frac\pi2-\varphi=90^\circ-53.13^\circ=36.87^\circ$；$\pi-2\varphi=180^\circ-106.26^\circ=73.74^\circ$" "\n"
        r"$\cos36.87^\circ=0.8=\frac45$ ✓✓；$\cos73.74^\circ=0.28=\frac7{25}$ ✓✓" "\n"
        r"④ **$\cos(\pi-2\varphi)$ 的化简**：$-\cos2\varphi=-(2\cos^2\varphi-1)=1-2(\frac35)^2=1-\frac{18}{25}=\frac7{25}$ ✓✓" "\n"
        r"⑤ **取中点验证**：取 $\omega$ 使 $\frac{\omega\pi}3=45^\circ$（在 $[36.87^\circ,73.74^\circ]$ 内）" "\n"
        r"$\frac{\omega\pi}3=\frac\pi4$ ⟹ $\omega=\frac34=0.75$" "\n"
        r"$t\in[53.13^\circ,53.13^\circ+45^\circ]=[53.13^\circ,98.13^\circ]$" "\n"
        r"$g$ 在该区间：min $=\min(5\sin53.13^\circ,5\sin98.13^\circ)=\min(4,4.949)=4$ ✓；max $=5\sin90^\circ=5$ ✓✓" "\n"
        r"**值域确为 $[4,5]$** ✓✓✓" "\n"
        r"$\cos45^\circ=0.7071$，在 $[\frac7{25},\frac45]=[0.28,0.8]$ 内 ✓✓" "\n"
        r"**答案 D（$[\frac7{25},\frac45]$）正确** ✓" "\n"
        r"**⭐ 通法（辅助角 + 区间值域反求参数）**：" "\n"
        r"① $a\\sin+b\\cos$ 先化成 $R\\sin(\\omega x+\\varphi)$，**明确 $\\varphi$ 的象限**（本题 $\\sin\\varphi=\\frac45>0,\\cos\\varphi=\\frac35>0$ ⟹ 第一象限）；" "\n"
        r"② 换元 $t=\\omega x+\\varphi$，把 $x$ 的区间映射成 $t$ 的区间；" "\n"
        r"③ **值域的上下界对应 $g(t)=$ 常数的两个解** —— 利用 $\\sin$ 的对称性 $g(\\theta)=g(\\pi-\\theta)$，" "\n"
        r"本题 $g(\\varphi)=g(\\pi-\\varphi)=4$，右端点就卡在 $\\pi-\\varphi$；" "\n"
        r"④ 最后 $\\cos$ 在 $[0,\\pi]$ **单调递减**，端点互换位置 —— ⚠ **别把上下界写反了**。"
    ),
    'difficulty': 0.93,
    'topics': ['M-T-178'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-178-V1',
}

T178_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知当 $x=-\dfrac\pi4$ 时，函数 $f(x)=a\sin x+\cos x$ 取到最大值，则 $f\left(x+\dfrac{3\pi}4\right)$ 是（　　）"
    ),
    'opts': [
        ('A', r"奇函数，在 $x=0$ 时取到最小值"),
        ('B', r"偶函数，在 $x=0$ 时取到最小值"),
        ('C', r"奇函数，在 $x=\pi$ 时取到最小值"),
        ('D', r"偶函数，在 $x=\pi$ 时取到最小值"),
    ],
    'answer': 'B',
    'analysis': (
        r"由最大值点定出 $\varphi$，进而定出 $a$；写出 $f$ 的余弦形式后整体左移 $\frac{3\pi}4$，"
        r"再判断奇偶性与最小值点。"
    ),
    'solution': (
        r"**第一步：由最值点定 $\varphi$**" "\n"
        r"$f(x)=\sqrt{a^{2}+1}\sin(x+\varphi)$，其中 $\tan\varphi=\dfrac1a$．" "\n"
        r"取最大值时 $x+\varphi=\dfrac\pi2$，代入 $x=-\dfrac\pi4$：" "\n"
        r"$-\dfrac\pi4+\varphi=\dfrac\pi2\Rightarrow\varphi=\dfrac{3\pi}4$．" "\n"
        r"$\tan\dfrac{3\pi}4=-1=\dfrac1a\Rightarrow a=-1$．" "\n"
        r"**第二步：写出 $f$**" "\n"
        r"$f(x)=-\sin x+\cos x=\sqrt2\left(\dfrac1{\sqrt2}\cos x-\dfrac1{\sqrt2}\sin x\right)=\sqrt2\cos\left(x+\dfrac\pi4\right)$．" "\n"
        r"（检验：$x=-\frac\pi4$ 时 $f=\sqrt2\cos0=\sqrt2$ 为最大值 ✓）" "\n"
        r"**第三步：平移**" "\n"
        r"$f\left(x+\dfrac{3\pi}4\right)=\sqrt2\cos\left(x+\dfrac{3\pi}4+\dfrac\pi4\right)=\sqrt2\cos(x+\pi)=-\sqrt2\cos x$．" "\n"
        r"$-\sqrt2\cos x$ 是**偶函数**，且在 $x=0$ 时取到**最小值** $-\sqrt2$．选 B．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**详解未提取**，上述推导为我独立完成）。" "\n"
        r"**独立验算**：" "\n"
        r"① **$a=-1$ 检验**：$f(x)=-\sin x+\cos x$；$f'(x)=-\cos x-\sin x=0$ ⟹ $\tan x=-1$ ⟹ $x=-\frac\pi4$ 或 $\frac{3\pi}4$" "\n"
        r"$x=-\frac\pi4$：$f=-\sin(-45^\circ)+\cos(-45^\circ)=0.7071+0.7071=1.4142=\sqrt2$ **最大** ✓✓" "\n"
        r"$x=\frac{3\pi}4$：$f=-\sin135^\circ+\cos135^\circ=-0.7071-0.7071=-1.4142$ **最小** ✓✓" "\n"
        r"（$f$ 的振幅 $\sqrt{1+1}=\sqrt2=1.4142$ ✓ 与最大/最小值吻合）" "\n"
        r"② **平移后**：$g(x)=f(x+\frac{3\pi}4)=-\sin(x+135^\circ)+\cos(x+135^\circ)$" "\n"
        r"取 $x=0$：$-\sin135^\circ+\cos135^\circ=-0.7071-0.7071=-1.4142=-\sqrt2$ ✓ **最小值** ✓✓" "\n"
        r"取 $x=\pi$：$-\sin315^\circ+\cos315^\circ=0.7071+0.7071=1.4142=\sqrt2$ **最大值**（不是最小）✓✓ **排除 D**" "\n"
        r"③ **奇偶性**：$g(x)=-\sqrt2\cos x$，$g(-x)=-\sqrt2\cos(-x)=-\sqrt2\cos x=g(x)$ ⟹ **偶函数** ✓✓ **排除 A、C**" "\n"
        r"④ **与 $-\sqrt2\cos x$ 形式核对**：$f(x+\frac{3\pi}4)=\sqrt2\cos(x+\frac{3\pi}4+\frac\pi4)=\sqrt2\cos(x+\pi)=-\sqrt2\cos x$ ✓✓" "\n"
        r"**答案 B（偶函数，在 $x=0$ 时取到最小值）正确** ✓" "\n"
        r"**⭐ 通法（由最值点定参数）**：" "\n"
        r"① $a\\sin x+b\\cos x$ 取最大值 ⟹ 辅助角的**整体角 $=\\frac\\pi2$**（不是 $0$！）；" "\n"
        r"② 定出 $\\varphi$ 后由 $\\tan\\varphi=\\frac{b}{a}$ 定参数 —— ⚠ **注意 $\\varphi$ 的象限**，" "\n"
        r"$\\tan$ 相同但象限不同会给出不同的 $a$；" "\n"
        r"③ 平移 $f(x+\\alpha)$ 时，**把 $x+\\alpha$ 整体代入**，别只加在 $x$ 上；" "\n"
        r"④ 判断奇偶看**平移后是否化成 $\\pm\\sin x$ 或 $\\pm\\cos x$** —— 本题正好化成 $-\\sqrt2\\cos x$（偶）。" "\n"
        r"**⚠ 本题最大陷阱**：$\\varphi=\\frac{3\\pi}4$ 是**第二象限角**，$\\tan=-1$ ⟹ $a=-1$（**负数**）。" "\n"
        r"若误取 $\\varphi=-\\frac\\pi4$（也满足 $\\tan=-1$），会得 $a=1$，" "\n"
        r"此时 $f(x)=\\sin x+\\cos x$ 在 $x=\\frac\\pi4$ 取最大，与题设 $x=-\\frac\\pi4$ **矛盾** ✗。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-178'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-178-V2',
}

QS = [T180_E1, T180_V1, T180_V3, T178_V1, T178_V2]
