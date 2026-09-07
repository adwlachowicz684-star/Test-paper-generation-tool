# -*- coding: utf-8 -*-
r"""第26批（下）：M-T-120 复杂型：与 ln(kx+b) 结合型（2题：E1、V1）

来源：2024高中数学热点题型归纳完整解析版.pdf 专题4 p085（PDF 页 84）

## 题型识别标志

条件形如 $f'(x)\ln(kx+b)+\dfrac{kf(x)}{kx+b}$ 时，
它恰好是 $\bigl[f(x)\ln(kx+b)\bigr]'$ —— 构造 $g(x)=f(x)\ln(kx+b)$。

【提分秘籍】原话：对于 $f'(x)\ln x+\dfrac{f(x)}x>0(<0)$，构造 $g(x)=\ln x\cdot f(x)$。

## 本批只录 2 题（V2、V3 待确认）

M-T-120 的 V2、V3 需再读 p086 确认，本批先做 E1、V1，保证质量。
"""

T120_E1 = {
    'type': '选择',
    'stem_text': (
        r"设函数 $f(x)$ 是定义在 $(-1,+\infty)$ 上的连续函数，"
        r"且在 $x=0$ 处存在导数．若函数 $f(x)$ 及其导函数 $f'(x)$ 满足" "\n"
        r"$f'(x)\ln(x+1)=x-\dfrac{f(x)}{x+1}$，" "\n"
        r"则函数 $f(x)$（　　）"
    ),
    'opts': [
        ('A', r"既有极大值又有极小值"),
        ('B', r"有极大值，无极小值"),
        ('C', r"有极小值，无极大值"),
        ('D', r"既无极大值也无极小值"),
    ],
    'answer': 'C',
    'analysis': (
        r"移项得 $f'(x)\ln(x+1)+\dfrac{f(x)}{x+1}=x$，"
        r"左边正是 $\bigl[f(x)\ln(x+1)\bigr]'$，故 $f(x)\ln(x+1)=\dfrac{x^{2}}2+C$；"
        r"由 $f$ 在 $x=0$ 处可导定出 $C=0$，再求导判极值。"
    ),
    'solution': (
        r"**识别导数结构**：由 $f'(x)\ln(x+1)=x-\dfrac{f(x)}{x+1}$ 移项得" "\n"
        r"$f'(x)\ln(x+1)+\dfrac{f(x)}{x+1}=x$，" "\n"
        r"而 $\bigl[f(x)\ln(x+1)\bigr]'=f'(x)\ln(x+1)+f(x)\cdot\dfrac1{x+1}$，" "\n"
        r"故 $\bigl[f(x)\ln(x+1)\bigr]'=x$，积分得 "
        r"$f(x)\ln(x+1)=\dfrac{x^{2}}2+C$．" "\n"
        r"**定常数**：$f(x)=\dfrac{\frac{x^{2}}2+C}{\ln(x+1)}$．"
        r"当 $x\to0$ 时 $\ln(x+1)\to0$，而 $f$ 在 $x=0$ 处**存在导数**（故连续、有有限极限），"
        r"必有分子 $\to0$，即 $0+C=0$，$C=0$．" "\n"
        r"于是 $f(x)=\dfrac{x^{2}}{2\ln(x+1)}$（$x\neq0$），且 $f(0)=\lim\limits_{x\to0}\dfrac{x^{2}}{2\ln(x+1)}=0$．" "\n"
        r"**求导**：设 $L=\ln(x+1)$，则 $f=\dfrac{x^{2}}{2L}$，" "\n"
        r"$f'=\dfrac{2x\cdot2L-x^{2}\cdot\frac{2}{x+1}}{4L^{2}}"
        r"=\dfrac{x\left(2L-\frac{x}{x+1}\right)}{2L^{2}}$．" "\n"
        r"令 $t=x+1$（$x>-1$，故 $t>0$），$L=\ln t$，则" "\n"
        r"$\varphi(t)=2\ln t+\dfrac1t-1$（分子括号内 $2L-\frac{x}{x+1}=2\ln t-\frac{t-1}t=2\ln t+\frac1t-1$），" "\n"
        r"$\varphi'(t)=\dfrac2t-\dfrac1{t^{2}}=\dfrac{2t-1}{t^{2}}$．" "\n"
        r"**判号**：" "\n"
        r"· $t>1$（$x>0$）时 $\varphi'(t)>0$，$\varphi$ 递增，$\varphi(1)=0$，故 $\varphi(t)>0$，"
        r"又 $x>0$、$2L^{2}>0$ ⇒ **$f'(x)>0$**．" "\n"
        r"· $0<t<1$（$-1<x<0$）时：$\varphi$ 在 $\left(0,\dfrac12\right)$ 递减、"
        r"在 $\left(\dfrac12,1\right)$ 递增；$\varphi\!\left(\dfrac12\right)=-2\ln2+2-1=1-2\ln2<0$，"
        r"$\varphi(1)=0$，故 $\varphi$ 在 $(0,1)$ 内有**唯一零点** $t_{0}$．"
        r"对应 $x_{0}=t_{0}-1\in(-1,0)$：" "\n"
        r"$-1<x<x_{0}$ 时 $f'(x)<0$，$x_{0}<x<0$ 时 **$f'(x)>0$**．" "\n"
        r"**综上**：$f$ 在 $(-1,x_{0})$ 递减、在 $(x_{0},0)$ 递增、在 $(0,+\infty)$ 递增，" "\n"
        r"故 $f$ 有**极小值**（在 $x_{0}$ 处），**无极大值**，选 C．"
    ),
    'review': (
        r"★ 还原版读出题干「f'(x)ln(x + 1) = x - \frac{f(x)}{x + 1}」，"
        r"**分数线自动还原** —— 这正是原来提取时最易丢的部分（`f(x)` 与 `x+1` 会分家）。" "\n"
        r"详解里 $f'(x)$ 的还原较乱：" "\n"
        r"「f'(x) =\frac{x[ 2ln) x + 1(+_{x + 1} - 1]}{2ln^{2}(x +}」" "\n"
        r"分母括号未闭合、$x+1$ 处有下标误判，**按还原版无法直接使用**。"
        r"上面的 $f'(x)$ 是我**独立推导**的：" "\n"
        r"$f=\frac{x^2}{2L}$，$L=\ln(x+1)$ ⇒ "
        r"$f'=\frac{2x\cdot 2L - x^2\cdot\frac{2}{x+1}}{4L^2}=\frac{x(2L-\frac{x}{x+1})}{2L^2}$ ✓" "\n"
        r"**与还原版的对应**：还原版分子里的 `2ln(x+1)`、`-1` 都在；"
        r"`+_{x+1}` 对应我的 $+\frac1{x+1}$ 项（它把 $\frac1{x+1}$ 误判成了下标）—— "
        r"注意 $2L-\frac{x}{x+1}=2\ln t-\frac{t-1}{t}=2\ln t+\frac1t-1$，"
        r"**$\frac1t$ 与 $-\frac{x}{x+1}$ 是等价的**，故还原版与我的推导一致 ✓。" "\n"
        r"**数值校验**：$\varphi(\frac12)=2\ln0.5+2-1=-1.386+1=-0.386<0$ ✓；"
        r"$\varphi(1)=0+1-1=0$ ✓；$\varphi(2)=2\ln2+0.5-1=1.386-0.5=0.886>0$ ✓。"
        r"$t_0\in(0.5,1)$ 存在 ✓，故 $x_0\in(-0.5,0)$ ✓。"
        r"$f$ 在 $x_0$ 处由减转增 → 极小值 ✓；$x=0$ 处左右导数同号（都 $>0$）→ 不是极值 ✓。**答案 C 成立**。"
    ),
    'difficulty': 0.95,
    'topics': ['M-T-120'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-120-E1',
}

T120_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知定义域为 $\mathbb R$ 的函数 $f(x)$ 满足 $f\!\left(\dfrac12\right)=-\dfrac12$，"
        r"$f'(x)-4x>0$，其中 $f'(x)$ 为 $f(x)$ 的导函数．"
        r"则当 $x\in[0,2\pi]$ 时，不等式 $f(\cos x)-\cos2x\geqslant0$ 的解集为（　　）"
    ),
    'opts': [
        ('A', r"$\left[0,\dfrac\pi6\right]$"),
        ('B', r"$\left[0,\dfrac\pi3\right]$"),
        ('C', r"$\left[0,\dfrac\pi6\right]\cup\left[\dfrac{11\pi}6,2\pi\right]$"),
        ('D', r"$\left[0,\dfrac\pi3\right]\cup\left[\dfrac{5\pi}3,2\pi\right]$"),
    ],
    'answer': 'D',
    'analysis': (
        r"构造 $g(x)=f(x)-2x^{2}$，由 $f'(x)-4x>0$ 知 $g$ 递增；"
        r"用 $\cos2x=2\cos^{2}x-1$ 把不等式化成 $g(\cos x)\geqslant g\!\left(\dfrac12\right)$。"
    ),
    'solution': (
        r"**构造**：设 $g(x)=f(x)-2x^{2}$，则 $g'(x)=f'(x)-4x>0$，"
        r"故 $g$ 在 $\mathbb R$ 上**单调递增**．" "\n"
        r"**化不等式**：由 $\cos2x=2\cos^{2}x-1$，" "\n"
        r"$f(\cos x)-\cos2x\geqslant0\iff f(\cos x)-2\cos^{2}x+1\geqslant0$" "\n"
        r"$\iff\bigl[f(\cos x)-2\cos^{2}x\bigr]\geqslant-1\iff g(\cos x)\geqslant-1$．" "\n"
        r"而 $g\!\left(\dfrac12\right)=f\!\left(\dfrac12\right)-2\cdot\dfrac14"
        r"=-\dfrac12-\dfrac12=-1$，" "\n"
        r"故不等式化为 $g(\cos x)\geqslant g\!\left(\dfrac12\right)$．" "\n"
        r"$g$ 递增，故 $\cos x\geqslant\dfrac12$．" "\n"
        r"**解三角不等式**：$x\in[0,2\pi]$ 时 $\cos x\geqslant\dfrac12"
        r"\iff x\in\left[0,\dfrac\pi3\right]\cup\left[\dfrac{5\pi}3,2\pi\right]$．" "\n"
        r"故选 D．"
    ),
    'review': (
        r"★ 还原版读出「f(1/2)=-1/2，f'(x) - 4x > 0」与"
        r"「不等式f(cosx) - cos2x ≥0」，分数 $\frac12$ 已还原 ✓。" "\n"
        r"选项原文：「A. [0,[B. [0,[ / 63」与"
        r"「C. [0,[∪[ ,2π[D. [0,[∪[ ,2π[ / 6633」——"
        r"$\frac\pi6$、$\frac\pi3$ 的分子 π 与分母分离，按上下文归位为 "
        r"A $[0,\frac\pi6]$、B $[0,\frac\pi3]$、"
        r"C $[0,\frac\pi6]\cup[\frac{11\pi}6,2\pi]$、D $[0,\frac\pi3]\cup[\frac{5\pi}3,2\pi]$。" "\n"
        r"**校验**：$\cos\frac\pi3=0.5$ ✓ 与 $\frac12$ 对应，故 B/D 的界是 $\frac\pi3$；"
        r"由对称性 $[0,\frac\pi3]$ 的镜像是 $[2\pi-\frac\pi3,2\pi]=[\frac{5\pi}3,2\pi]$ ✓。"
        r"答案 D ✓ 自洽。" "\n"
        r"**数值校验**：$x=\frac\pi3=1.047$：$\cos=0.5$，$g(0.5)=-1$，等式成立 ✓；"
        r"$x=0$：$\cos=1>0.5$ ✓ 在解集内；"
        r"$x=\frac\pi2$：$\cos=0<0.5$ ✗ 不在解集内 ✓；"
        r"$x=\frac{5\pi}3=5.236$：$\cos=0.5$ ✓ 边界。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-120'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-120-V1',
}

QS = [T120_E1, T120_V1]
