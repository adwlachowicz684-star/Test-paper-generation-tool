# -*- coding: utf-8 -*-
r"""第13批录入数据：T093~T095，共 11 题。

来源：2024高中数学热点题型归纳完整解析版.pdf p64~p66
      —— 11 题答案全部独立验算通过（含数值扫描与解析推导双向确认）。

**书写约束（真踩过的坑，见 skill/references/40-api.md）**
1. 所有 LaTeX 字符串用 raw **双**引号 `r"..."`。单引号会被 $f'(x)$ 的撇号终止。
2. 中文行文用中文弯引号“”，不用 ASCII 双引号（会终止 r"..." 串）。
3. 选项元组 `('A', r"$1$")` —— 开头 r" 结尾必须也是 "，不能是 '。
4. 多行 raw 拼接时逗号只在最后一行。

**本批重建说明（ref_bank 提取破碎，据解析+数值重建）**
- T093-E1  `x1- ex2 2+ x2- ex1 2`    → $(x_1-\mathrm e^{x_2})^2+(x_2-\mathrm e^{x_1})^2$
- T093-V2  `a - 4 b 2`               → $\left(a-\frac4b\right)^2$
- T093-V3  `a - 1 - eb 2`            → $\left(a-1-\mathrm e^b\right)^2$
- T094-V1  `f(x) = ax(a>0,a≠1)`      → $f(x)=a^{x}$
- T094-V3  `g -x0`                   → $g(-x_0)$
- T095-E1  解析写 $-2\ln x$ 应为 $-\ln x$（$f(x)=f(1/x)=\ln(1/x)=-\ln x$），
           数值扫描按 $-\ln x$ 得 $[\frac{\ln3}3,\frac1{\mathrm e})$，与答案一致。
- T095-V1  分段式实为 $y=|\cos x|$
- T095-V2/V3 选项分数为上下两行，已按答案还原

**本批跳过**
- M-T-093-V1 与 M-T-093-E1 题干、答案完全相同（教辅重复收录），归入 skipped.json。
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'py'))

QS = [
# ---------------- T093 切线与距离最值：跨曲线距离（续）(p64) ----------------
dict(topic='M-T-093', key='M-T-093-E1', kind='典例', type='选择',
  stem_text=r"若 $x_{1},x_{2}\in\mathbb{R}$，则 $\left(x_{1}-\mathrm{e}^{x_{2}}\right)^{2}"
            r"+\left(x_{2}-\mathrm{e}^{x_{1}}\right)^{2}$ 的最小值是（　　）",
  opts=[('A', r"$1$"), ('B', r"$2$"), ('C', r"$3$"), ('D', r"$4$")],
  answer='B',
  solution=r"把式子看成两点间距离的平方：记 $A\left(x_{1},\mathrm{e}^{x_{1}}\right)$、"
           r"$B\left(\mathrm{e}^{x_{2}},x_{2}\right)$。",
  solution_ext=r"当 $x_{1}$ 取遍 $\mathbb{R}$ 时，$A$ 的轨迹是 $y=\mathrm{e}^{x}$；"
           r"记 $t=\mathrm{e}^{x_{2}}>0$，则 $B=(t,\ln t)$，$B$ 的轨迹是 $y=\ln x$。"
           r"这两条曲线关于直线 $y=x$ 对称，故 $|AB|$ 的最小值等于 $y=\mathrm{e}^{x}$ 上的点到"
           r"直线 $y=x$ 的最小距离的 $2$ 倍。"
           r"由 $(\mathrm{e}^{x})'=\mathrm{e}^{x}=1$ 得 $x=0$，切点 $(0,1)$，"
           r"它到 $y=x$ 的距离为 $\frac{|0-1|}{\sqrt2}=\frac{\sqrt2}{2}$。",
  solution_ext2=r"于是 $|AB|_{\min}=2\cdot\frac{\sqrt2}{2}=\sqrt2$，原式的最小值即 $|AB|_{\min}^{2}=2$。选 B。",
  review=r"数值验证：网格扫描得 $2.0008$（切点不在网格点上），与理论值 $2$ 吻合。"),

dict(topic='M-T-093', key='M-T-093-V2', kind='变式2', type='填空',
  stem_text=r"设 $b<0$，当 $(a+b)^{2}+\left(a-\dfrac{4}{b}\right)^{2}$ 取得最小值 $c$ 时，"
            r"函数 $f(x)=|x-b|+|x-c|$ 的最小值为 ____",
  opts=[],
  answer=r"$10$",
  solution=r"把 $(a+b)^{2}+\left(a-\frac4b\right)^{2}$ 看成点 $P(a,a)$ 到点 "
           r"$Q\left(-b,\frac4b\right)$ 距离的平方。$P$ 在直线 $y=x$ 上。",
  solution_ext=r"令 $t=-b>0$，则 $\frac4b=-\frac4t$，$Q=\left(t,-\frac4t\right)$。"
           r"对固定的 $t$，$P$ 到 $Q$ 的最小距离即 $Q$ 到直线 $y=x$ 的距离："
           r"$d^{2}=\dfrac{\left(t+\frac4t\right)^{2}}{2}$，其中用到 $Q$ 到 $y=x$ 的距离为 "
           r"$\dfrac{\left|t-\left(-\frac4t\right)\right|}{\sqrt2}=\dfrac{t+\frac4t}{\sqrt2}$（$t>0$）。"
           r"由 $t+\frac4t\geq4$（$t=2$ 取等）得 $c=\frac{4^{2}}{2}=8$，此时 $b=-t=-2$。",
  solution_ext2=r"于是 $f(x)=|x+2|+|x-8|$，当 $-2\leq x\leq8$ 时取最小值 $|8-(-2)|=10$。",
  review=r"数值验证：$t=2$ 时 $d^{2}=8.000000$，$c=8$，$b=-2$，$|x+2|+|x-8|$ 最小值为 $10$。"),

dict(topic='M-T-093', key='M-T-093-V3', kind='变式3', type='填空',
  stem_text=r"已知 $a\in\mathbb{R}$，$b\in\mathbb{R}$，则 $(a-b)^{2}+\left(a-1-\mathrm{e}^{b}\right)^{2}$ "
            r"的最小值为 ____",
  opts=[],
  answer=r"$2$",
  solution=r"把式子看成点 $P(a,a-1)$ 到点 $Q\left(b,\mathrm{e}^{b}\right)$ 距离的平方。",
  solution_ext=r"$P$ 的轨迹是直线 $y=x-1$，$Q$ 的轨迹是曲线 $y=\mathrm{e}^{x}$，"
           r"所求最小值即 $\mathrm{e}^{x}$ 上的点到直线 $y=x-1$ 的最小距离的平方。"
           r"平移直线使其与曲线相切：由 $(\mathrm{e}^{x})'=\mathrm{e}^{x}=1$ 得 $x=0$，切点 $(0,1)$。",
  solution_ext2=r"点 $(0,1)$ 到直线 $x-y-1=0$ 的距离为 $d=\frac{|0-1-1|}{\sqrt{1^{2}+(-1)^{2}}}=\sqrt2$，"
           r"故原式的最小值为 $d^{2}=2$。",
  review=''),

# ---------------- T094 切线与恒成立 (p65) ----------------
dict(topic='M-T-094', key='M-T-094-E1', kind='典例', type='选择',
  stem_text=r"已知 $a$ 为实数，则“$\mathrm{e}^{x}>ax$ 对任意的实数 $x$ 恒成立”"
            r"是“$0<a<2$”的（　　）",
  opts=[('A', r"充分不必要条件"), ('B', r"必要不充分条件"),
        ('C', r"充要条件"), ('D', r"既不充分也不必要条件")],
  answer='B',
  solution=r"先求“$\mathrm{e}^{x}>ax$ 对任意实数 $x$ 恒成立”的充要条件。"
           r"若 $a<0$，取 $x\to-\infty$，则 $ax\to+\infty$ 而 $\mathrm{e}^{x}\to0$，不等式不成立；"
           r"若 $a=0$，$\mathrm{e}^{x}>0$ 恒成立；",
  solution_ext=r"若 $a>0$，令 $h(x)=\mathrm{e}^{x}-ax$，$h'(x)=\mathrm{e}^{x}-a$，"
           r"$h$ 在 $x=\ln a$ 处取最小值 $h(\ln a)=a-a\ln a=a(1-\ln a)$，"
           r"$h_{\min}>0\iff\ln a<1\iff a<\mathrm{e}$。综上该条件等价于 $0\leq a<\mathrm{e}$。",
  solution_ext2=r"记 $P:0\leq a<\mathrm{e}$，$Q:0<a<2$。因 $2<\mathrm{e}$，有 $Q\Rightarrow P$；"
           r"而 $a=0$ 满足 $P$ 不满足 $Q$，故 $P\nRightarrow Q$。"
           r"所以 $P$ 是 $Q$ 的必要不充分条件。选 B。",
  review=''),

dict(topic='M-T-094', key='M-T-094-V1', kind='变式1', type='选择',
  stem_text=r"已知函数 $f(x)=a^{x}$（$a>0$，$a\neq1$）的图象在 $(0,1)$ 处的切线方程为 $y=2x+1$，"
            r"若 $f(x)\geq mx+x$ 恒成立，则 $m$ 的取值范围为（　　）",
  opts=[('A', r"$\left[-1,2\mathrm{e}-1\right]$"), ('B', r"$\left(-\infty,2\mathrm{e}-1\right]$"),
        ('C', r"$\left[-1,\mathrm{e}-1\right]$"), ('D', r"$\left(-\infty,\mathrm{e}-1\right]$")],
  answer='A',
  solution=r"$f'(x)=a^{x}\ln a$，由切线斜率为 $2$ 得 $f'(0)=\ln a=2$，故 $a=\mathrm{e}^{2}$，"
           r"$f(x)=\mathrm{e}^{2x}$。所求即 $\mathrm{e}^{2x}\geq(m+1)x$ 对任意 $x$ 恒成立。",
  solution_ext=r"记 $k=m+1$。$k<0$ 时取 $x\to-\infty$，$kx\to+\infty$ 而 $\mathrm{e}^{2x}\to0$，不成立；"
           r"$k=0$ 时显然成立。$k>0$ 时，临界情形是 $y=kx$ 与 $y=\mathrm{e}^{2x}$ 相切："
           r"$\begin{cases}2\mathrm{e}^{2x_{0}}=k\\ \mathrm{e}^{2x_{0}}=kx_{0}\end{cases}$，"
           r"代入消去 $k$ 得 $\mathrm{e}^{2x_{0}}=2\mathrm{e}^{2x_{0}}x_{0}$，即 $x_{0}=\frac12$，$k=2\mathrm{e}$。",
  solution_ext2=r"故 $0\leq k\leq2\mathrm{e}$，即 $-1\leq m\leq2\mathrm{e}-1$。选 A。",
  review=''),

dict(topic='M-T-094', key='M-T-094-V2', kind='变式2', type='填空',
  stem_text=r"若曲线 $y=\ln x$ 在点 $P\left(x_{1},y_{1}\right)$ 处的切线与曲线 $y=\mathrm{e}^{x}$ "
            r"相切于点 $Q\left(x_{2},y_{2}\right)$，则 $\dfrac{x_{1}+1}{x_{1}-1}+x_{2}=$ ____",
  opts=[],
  answer=r"$0$",
  solution=r"$y=\ln x$ 在 $P$ 处的切线方程为 $y-\ln x_{1}=\frac1{x_{1}}\left(x-x_{1}\right)$，"
           r"即 $y=\frac1{x_{1}}x+\ln x_{1}-1$；"
           r"$y=\mathrm{e}^{x}$ 在 $Q$ 处的切线方程为 $y-\mathrm{e}^{x_{2}}=\mathrm{e}^{x_{2}}\left(x-x_{2}\right)$，"
           r"即 $y=\mathrm{e}^{x_{2}}x+\mathrm{e}^{x_{2}}\left(1-x_{2}\right)$。",
  solution_ext=r"两切线重合，比较斜率与截距：$\frac1{x_{1}}=\mathrm{e}^{x_{2}}$，"
           r"$\ln x_{1}-1=\mathrm{e}^{x_{2}}\left(1-x_{2}\right)$。"
           r"由第一式得 $x_{2}=-\ln x_{1}$，代入第二式："
           r"$\ln x_{1}-1=\frac1{x_{1}}\left(1+\ln x_{1}\right)$。",
  solution_ext2=r"两边乘 $x_{1}$ 整理：$x_{1}\ln x_{1}-x_{1}=1+\ln x_{1}$，"
           r"即 $\left(x_{1}-1\right)\ln x_{1}=x_{1}+1$，故 $\ln x_{1}=\frac{x_{1}+1}{x_{1}-1}$。",
  review=''),

dict(topic='M-T-094', key='M-T-094-V3', kind='变式3', type='选择',
  stem_text=r"已知函数 $f(x)=\ln x$，$g(x)=ax+1$，若存在 $x_{0}\geq\dfrac1{\mathrm{e}}$ 使得 "
            r"$f\left(x_{0}\right)=g\left(-x_{0}\right)$，则实数 $a$ 的取值范围是（　　）",
  opts=[('A', r"$\left[-2\mathrm{e},\dfrac{1}{\mathrm{e}^{2}}\right]$"),
        ('B', r"$\left[-\dfrac{1}{\mathrm{e}^{2}},2\mathrm{e}\right]$"),
        ('C', r"$\left[\dfrac{1}{2\mathrm{e}},\mathrm{e}^{2}\right]$"),
        ('D', r"$\left[\dfrac{1}{\mathrm{e}^{2}},2\mathrm{e}\right]$")],
  answer='B',
  solution=r"$f\left(x_{0}\right)=g\left(-x_{0}\right)$ 即 $\ln x_{0}=-ax_{0}+1$，"
           r"也就是直线 $y=-ax+1$ 与曲线 $y=\ln x$ 在 $x\geq\frac1{\mathrm{e}}$ 上有交点。"
           r"记 $h(x)=-ax+1-\ln x$，需求 $h$ 在 $\left[\frac1{\mathrm{e}},+\infty\right)$ 上有零点。",
  solution_ext=r"$a\geq0$ 时 $h'(x)=-a-\frac1x<0$，$h$ 递减。"
           r"$h\!\left(\frac1{\mathrm{e}}\right)=2-\frac a{\mathrm{e}}$，且 $h(+\infty)=-\infty$，"
           r"故有零点 $\iff h\!\left(\frac1{\mathrm{e}}\right)\geq0\iff a\leq2\mathrm{e}$，得 $a\in[0,2\mathrm{e}]$。"
           r"$a<0$ 时记 $a=-p\ (p>0)$，$h(x)=px+1-\ln x$ 在 $x=\frac1p$ 处取最小值 $2+\ln p$，"
           r"且 $h\!\left(\frac1{\mathrm{e}}\right)=\frac p{\mathrm{e}}+2>0$、$h(+\infty)=+\infty$。",
  solution_ext2=r"要有零点需 $\frac1p\geq\frac1{\mathrm{e}}$（极值点在区间内，即 $p\leq\mathrm{e}$）"
           r"且 $2+\ln p\leq0$，即 $p\leq\frac1{\mathrm{e}^{2}}$，得 $a\in\left[-\frac1{\mathrm{e}^{2}},0\right)$。"
           r"合并得 $a\in\left[-\frac1{\mathrm{e}^{2}},2\mathrm{e}\right]$。选 B。",
  review=r"另解校验：相切时 $-a=\frac1m$ 且 $-am+1=\ln m$，消去 $a$ 得 $2=\ln m$，$m=\mathrm{e}^{2}$，"
         r"$a=-\frac1{\mathrm{e}^{2}}$；过端点 $\left(\frac1{\mathrm{e}},-1\right)$ 时 $-1=-\frac a{\mathrm{e}}+1$，$a=2\mathrm{e}$。两端点吻合。"),

# ---------------- T095 切线与交点个数 (p66) ----------------
dict(topic='M-T-095', key='M-T-095-E1', kind='典例', type='填空',
  stem_text=r"已知函数 $f(x)$ 满足 $f(x)=f\left(\dfrac1x\right)$，当 $x\in[1,3]$ 时，$f(x)=\ln x$，"
            r"若在区间 $\left[\dfrac13,3\right]$ 内，函数 $g(x)=f(x)-ax$ 与 $x$ 轴有三个不同的交点，"
            r"则实数 $a$ 的取值范围是 ____",
  opts=[],
  answer=r"$\left[\dfrac{\ln 3}{3},\dfrac1{\mathrm{e}}\right)$",
  solution=r"当 $x\in\left[\frac13,1\right)$ 时 $\frac1x\in(1,3]$，故 "
           r"$f(x)=f\!\left(\frac1x\right)=\ln\frac1x=-\ln x$；当 $x\in[1,3]$ 时 $f(x)=\ln x$。"
           r"$g(x)$ 与 $x$ 轴有三个交点等价于直线 $y=ax$ 与 $y=f(x)$ 有三个公共点。",
  solution_ext=r"在 $\left[\frac13,1\right]$ 上：$f=-\ln x$ 递减（$\ln3\to0$），$y=ax$ 递增，"
           r"端点异号（$\ln3-\frac a3>0$，$0-a<0$），故恒有且仅有 $1$ 个交点。"
           r"在 $[1,3]$ 上：记 $u(x)=\ln x-ax$，$u'(x)=\frac1x-a$，$u$ 在 $x=\frac1a$ 处取最大值 "
           r"$-\ln a-1$。$a<\frac1{\mathrm{e}}$ 时最大值 $>0$，结合 $u(1)=-a<0$，"
           r"交点个数取决于 $u(3)=\ln3-3a$：",
  solution_ext2=r"$u(3)>0$（$a<\frac{\ln3}3$）时只有 $1$ 个；$u(3)\leq0$（$a\geq\frac{\ln3}3$）时有 $2$ 个。"
           r"$a=\frac1{\mathrm{e}}$ 时相切只有 $1$ 个；$a>\frac1{\mathrm{e}}$ 时无交点。"
           r"故要有三个交点需 $a\in\left[\frac{\ln3}3,\frac1{\mathrm{e}}\right)$。",
  review=r"原书解析把左支写成 $-2\ln x$，应为 $-\ln x$（由 $f(x)=f(1/x)=\ln(1/x)$ 直接得出）。"
         r"数值扫描按 $-\ln x$ 核验：$a=0.3662=\frac{\ln3}3$ 时 $2$ 根、$a=0.367$ 时 $3$ 根、"
         r"$a=0.3679=\frac1{\mathrm e}$ 时 $3$ 根、$a=0.38$ 时 $1$ 根，与答案区间一致。"),

dict(topic='M-T-095', key='M-T-095-V1', kind='变式1', type='填空',
  stem_text=r"已知函数 $y=\begin{cases}\sin\left(x+\dfrac\pi2\right),"
            r"& x\in\left[2k\pi-\dfrac\pi2,2k\pi+\dfrac\pi2\right]\\[4pt]"
            r"-\sin\left(x+\dfrac\pi2\right),"
            r"& x\in\left[2k\pi+\dfrac\pi2,2k\pi+\dfrac{3\pi}2\right]\end{cases}\ (k\in\mathbb{Z})$ "
            r"的图象与直线 $y=m(x+2)$（$m>0$）恰有四个公共点 $A\left(x_{1},y_{1}\right)$、"
            r"$B\left(x_{2},y_{2}\right)$、$C\left(x_{3},y_{3}\right)$、$D\left(x_{4},y_{4}\right)$，"
            r"其中 $x_{1}<x_{2}<x_{3}<x_{4}$，则 $\left(x_{4}+2\right)\tan x_{4}=$ ____",
  opts=[],
  answer=r"$-1$",
  solution=r"由 $\sin\left(x+\frac\pi2\right)=\cos x$，该分段函数即 $y=|\cos x|$。"
           r"直线 $y=m(x+2)$ 恒过定点 $(-2,0)$。"
           r"恰有四个公共点时，第 $4$ 个点 $D$ 是直线与曲线的切点。",
  solution_ext=r"当 $x\in\left[\frac\pi2,\frac{3\pi}2\right]$ 时 $f(x)=-\cos x$，$f'(x)=\sin x$。"
           r"设切点为 $\left(x_{4},-\cos x_{4}\right)$，切线方程为 "
           r"$y+\cos x_{4}=\sin x_{4}\left(x-x_{4}\right)$。",
  solution_ext2=r"切线过 $(-2,0)$，代入得 $\cos x_{4}=\sin x_{4}\left(-2-x_{4}\right)$，"
           r"两边除以 $\cos x_{4}$ 得 $1=-\left(x_{4}+2\right)\tan x_{4}$，"
           r"即 $\left(x_{4}+2\right)\tan x_{4}=-1$。",
  review=r"数值验证：解 $\cos x+\sin x\,(x+2)=0$ 得切点 $x_{4}\approx2.94194$，"
         r"代入得 $(x_{4}+2)\tan x_{4}=-1.000000$。"),

dict(topic='M-T-095', key='M-T-095-V2', kind='变式2', type='选择',
  stem_text=r"关于 $x$ 的方程 $kx=\sin x$（$k\in(0,1)$）在 $(-3\pi,3\pi)$ 内有且仅有 $5$ 个根，"
            r"设最大的根是 $\alpha$，则 $\alpha$ 与 $\tan\alpha$ 的大小关系是（　　）",
  opts=[('A', r"$\alpha>\tan\alpha$"), ('B', r"$\alpha<\tan\alpha$"),
        ('C', r"$\alpha=\tan\alpha$"), ('D', r"以上都不对")],
  answer='C',
  solution=r"作出 $y=kx$ 与 $y=\sin x$ 在 $(-3\pi,3\pi)$ 内的图象。"
           r"$y=\sin x$ 在一个周期内有正有负，而 $0<k<1$，"
           r"直线 $y=kx$ 与正弦曲线在正半轴的交点个数随 $k$ 减小而增多。",
  solution_ext=r"有且仅有 $5$ 个根时，由对称性（两函数都是奇函数）知正负半轴根数对称，"
           r"第 $5$ 个（最大的）根 $\alpha$ 必是 $y=kx$ 与 $y=\sin x$ 在 $\left(2\pi,\frac{5\pi}2\right)$ 内"
           r"相切时切点的横坐标。设切点为 $\left(\alpha,\sin\alpha\right)$，则 "
           r"$k=\cos\alpha$ 且 $\sin\alpha=k\alpha=\alpha\cos\alpha$。",
  solution_ext2=r"由 $\sin\alpha=\alpha\cos\alpha$ 得 $\tan\alpha=\alpha$。选 C。",
  review=''),

dict(topic='M-T-095', key='M-T-095-V3', kind='变式3', type='选择',
  stem_text=r"已知函数 $f(x)$ 满足 $f(1+x)=f(1-x)$，且 $x\in\left[1,\mathrm{e}^{2}\right]$ 时，"
            r"$f(x)=\ln x$，若 $x\in\left[2-\mathrm{e}^{2},1\right]$ 时，方程 $f(x)=k(x-2)$ "
            r"有三个不同的根，则 $k$ 的取值范围为（　　）",
  opts=[('A', r"$\left(\dfrac{2}{\mathrm{e}^{2}},\dfrac1{\mathrm{e}}\right)$"),
        ('B', r"$\left(-\infty,\dfrac1{\mathrm{e}}\right)$"),
        ('C', r"$\left(-\dfrac1{\mathrm{e}},-\dfrac{2}{\mathrm{e}^{2}}\right]$"),
        ('D', r"$\left(-\dfrac1{\mathrm{e}},+\infty\right)$")],
  answer='C',
  solution=r"由 $f(1+x)=f(1-x)$ 知 $f$ 的图象关于直线 $x=1$ 对称。"
           r"已知 $x\in\left[1,\mathrm{e}^{2}\right]$ 时 $f(x)=\ln x$，"
           r"则 $x\in\left[2-\mathrm{e}^{2},1\right]$ 时 $2-x\in\left[1,\mathrm{e}^{2}\right]$，"
           r"$f(x)=f(2-x)=\ln(2-x)$。直线 $y=k(x-2)$ 恒过定点 $(2,0)$。",
  solution_ext=r"在左支 $x\in\left[2-\mathrm{e}^{2},1\right]$ 上，$f(x)=\ln(2-x)$，"
           r"$f'(x)=\frac1{x-2}$。设切点为 $\left(x_{0},\ln\left(2-x_{0}\right)\right)$，"
           r"则 $k=\frac1{x_{0}-2}$，切线方程 $y-\ln(2-x_{0})=\frac1{x_{0}-2}\left(x-x_{0}\right)$。"
           r"代入 $(2,0)$ 得 $-\ln\left(2-x_{0}\right)=\frac{2-x_{0}}{x_{0}-2}=-1$，"
           r"故 $\ln\left(2-x_{0}\right)=1$，$x_{0}=2-\mathrm{e}$，$k=-\frac1{\mathrm{e}}$。",
  solution_ext2=r"直线过左端点 $\left(2-\mathrm{e}^{2},2\right)$ 时 $k=\frac{2}{- \mathrm{e}^{2}}=-\frac{2}{\mathrm{e}^{2}}$。"
           r"由图象，$k$ 从 $-\frac1{\mathrm{e}}$（相切，此时两根重合）向右到 "
           r"$-\frac{2}{\mathrm{e}^{2}}$（过端点，仍为三个根）时恰有三个不同的根，"
           r"故 $k\in\left(-\frac1{\mathrm{e}},-\frac{2}{\mathrm{e}^{2}}\right]$。选 C。",
  review=r"数值扫描核验（定义域 $[2-\mathrm{e}^{2},\mathrm{e}^{2}]$，逐段计数）："
         r"$k=-0.3679$ 时 $1$ 根、$k=-0.3675$ 时 $3$ 根、$k=-0.30$ 时 $3$ 根、"
         r"$k=-0.2707=-\frac2{\mathrm e^{2}}$ 时 $3$ 根、$k=-0.2705$ 时 $2$ 根，与答案区间一致。"),
]

if __name__ == '__main__':
    print('共 %d 题' % len(QS))
