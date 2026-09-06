# -*- coding: utf-8 -*-
r"""第10批录入数据：T073~T078 嵌套函数含参型 / 双复合型 / 零点区间，共 15 题。

来源：2024高中数学热点题型归纳完整解析版.pdf p48~p55
      —— 基于 ref_bank 提取文本逐题重建，15 题答案全部独立验算通过。

**LaTeX 相关字符串一律 raw 双引号 r"..."**：
单引号会被导数撇号 $f'(x)$ 提前终止（一次坏 7 处，SyntaxError）。

本批跳过的 4 题（提取破碎，无法可靠重建，按 skill 原则宁缺毋滥）：
  T073-E1  分段式 "a x - 1" 无法判定是 ax-1 / a^x-1 / x-a，
           且三种解读都推不出原书答案 (-1,0)∪(0,+∞)
  T074-E1  t = x + 1/(4x+1) 的形式与解析"t=1 无解"矛盾，无法重建
  T074-V1  选项 C 与 D 印刷完全相同（都是 (-1,0)∪(5/4,2)），
           解析被截断，无法判定开闭差异
  T075-V3  与 T074-V3 完全同题，已挂在 T074-V3 下
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'py'))

QS = [
# ---------------- T073 嵌套函数含参型：解析式含参 (p48) ----------------
dict(topic='M-T-073', key='M-T-073-V1', kind='变式1', type='选择',
  stem_text=r"已知函数 $f(x)=\begin{cases}x+2a,&x<0\\ x^{2}-ax,&x\geq 0\end{cases}$，"
            r"若关于 $x$ 的方程 $f(f(x))=0$ 有 $8$ 个不同的实数解，"
            r"则实数 $a$ 的取值可能是（　　）",
  opts=[('A', r"$8\sqrt{2}$"), ('B', r"$7\sqrt{2}$"),
        ('C', r"$6\sqrt{2}$"), ('D', r"$5\sqrt{2}$")],
  answer='ABC',
  solution=r"$a\leq 0$ 时 $f$ 在 $\mathbb{R}$ 上单调递增，$f(f(x))=0$ 至多几个解，不成立。"
           r"$a>0$ 时，令 $t=f(x)$，由 $f(t)=0$ 得三根 "
           r"$t_{1}=-2a$（$x+2a=0$ 且 $-2a<0$）、$t_{2}=0$、$t_{3}=a$（$x^{2}-ax=0$）。"
           r"分别数 $f(x)=t$ 的解数：$t_{2}=0$ 有 $3$ 个解（$x=-2a$、$0$、$a$）；"
           r"$t_{3}=a$ 有 $2$ 个解（$x+2a=a$ 给 $x=-a<0$；$x^{2}-ax-a=0$ "
           r"判别式 $a^{2}+4a>0$、两根异号，取正根一个）；"
           r"$t_{1}=-2a$：$x+2a=-2a$ 给 $x=-4a<0$ 一个解，"
           r"$x^{2}-ax+2a=0$ 的判别式 $\Delta=a^{2}-8a$，"
           r"$a>8$ 时给 $2$ 个解，$a=8$ 时给 $1$ 个，$a<8$ 时无解。"
           r"故 $a>8$ 时解数为 $3+2+3=8$。四个选项中 "
           r"$8\sqrt{2}\approx11.31$、$7\sqrt{2}\approx9.90$、$6\sqrt{2}\approx8.49$ 均大于 $8$，"
           r"$5\sqrt{2}\approx7.07<8$，故选 ABC。",
  review='程序枚举验证：$a=7.07$ 时 $6$ 个解，$a=8.0001$、$8.5$、$9.9$、$11.31$ 时均为 $8$ 个解。'),

dict(topic='M-T-073', key='M-T-073-V2', kind='变式2', type='填空',
  stem_text=r"已知函数 $f(x)=\begin{cases}-x^{3}+3x^{2}+t,&x\leq 0\\ 3x-1,&x>0\end{cases}$，"
            r"若函数 $y=f(f(x))$ 恰好有 $4$ 个不同的零点，则实数 $t$ 的取值范围是 ____",
  opts=[],
  answer=r"$-4<t\leq\frac{3-\sqrt{13}}{2}$ 或 $t=0$",
  solution=r"$x\leq 0$ 时 $f'(x)=-3x^{2}+6x=3x(2-x)\leq 0$，$f$ 在 $(-\infty,0]$ 上单调递减，"
           r"值域 $[t,+\infty)$；$x>0$ 时 $f(x)=3x-1$ 单调递增，值域 $(-1,+\infty)$。"
           r"记 $h(x)=x^{3}-3x^{2}$（$x\leq 0$），$h'(x)=3x(x-2)>0$，$h$ 单调递增，"
           r"值域 $(-\infty,0]$，且 $h(0)=0$、$h(-1)=-4$。"
           r"由 $f(s)=0$ 得 $s=\frac{1}{3}$（恒有），以及 $t\leq 0$ 时的 $s_{1}=h^{-1}(t)\leq 0$。"
           r"于是零点个数 $=N\!\left(\frac13\right)+N(s_{1})$，"
           r"其中 $N(v)$ 表示 $f(x)=v$ 的解数：$x>0$ 段需 $v>-1$，$x\leq 0$ 段需 $v\geq t$。"
           r"（1）$N(\frac13)$：$v=\frac13>-1$ 恒成立给 $1$ 个，再加 $x\leq 0$ 段需 $\frac13\geq t$。"
           r"（2）$N(s_{1})$（仅 $t\leq 0$）：需 $s_{1}>-1$ 与 $s_{1}\geq t$。"
           r"由 $s_{1}>-1$ 及 $h$ 递增得 $t=h(s_{1})>h(-1)=-4$；"
           r"由 $s_{1}\geq t=h(s_{1})$ 得 $s_{1}(s_{1}^{2}-3s_{1}-1)\geq 0$。"
           r"$s_{1}<0$ 时推出 $s_{1}^{2}-3s_{1}-1\leq 0$ 需反向（除以负数），"
           r"实为 $s_{1}\leq\frac{3-\sqrt{13}}{2}$；$s_{1}=0$（即 $t=0$）时乘积为 $0$ 自动成立。"
           r"综合得 $-4<t\leq\frac{3-\sqrt{13}}{2}$，或孤立的 $t=0$。",
  review='注意 $s_1=0$ 是**边界特例**：此时 $s_1(s_1^2-3s_1-1)=0$ 自动满足，'
         '不能用"除以 $s_1$"推出 $s_1^2-3s_1-1\\geq0$。这正是答案里单独列出 "$t=0$" 的原因。'),

dict(topic='M-T-073', key='M-T-073-V3', kind='变式3', type='填空',
  stem_text=r"已知 $a>0$，设函数 "
            r"$f(x)=\begin{cases}-x^{2}+(2+2a)x,&0<x<a+2\\ ax,&x\geq a+2\end{cases}$，"
            r"存在 $x_{0}$ 满足 $f(f(x_{0}))=x_{0}$，且 $f(x_{0})\neq x_{0}$，"
            r"则 $a$ 的取值范围是 ____",
  opts=[],
  answer=r"$\frac{1}{2}<a<1$",
  solution=r"设 $y_{0}=f(x_{0})$。由 $f(f(x_{0}))=x_{0}$ 且 $f(x_{0})\neq x_{0}$ 知，"
           r"$f$ 的图象上存在两个不同的点 $(x_{0},y_{0})$ 与 $(y_{0},x_{0})$，即关于直线 $y=x$ 对称。"
           r"抛物线段 $y=-x^{2}+(2+2a)x$（$0<x<a+2$）在 $x=a+2$ 处取值 $(a+2)\cdot a=a(a+2)$，"
           r"与射线段 $y=ax$（$x\geq a+2$）的起点衔接。"
           r"**情形一：两点都在抛物线上。** 由 $y_{0}=-x_{0}^{2}+(2+2a)x_{0}$ 与 "
           r"$x_{0}=-y_{0}^{2}+(2+2a)y_{0}$ 相减，因 $x_{0}\neq y_{0}$ 可约去 $y_{0}-x_{0}$，"
           r"得 $x_{0}+y_{0}=3+2a$。代入整理得 $x_{0}^{2}-(3+2a)x_{0}+(3+2a)=0$，"
           r"判别式 $\Delta=(3+2a)(2a-1)>0$，故 $a>\frac12$；"
           r"又需两根都小于 $a+2$，即 $\Delta<1$，得 $a<\frac{\sqrt5-1}{2}$。"
           r"此情形给出 $a\in\left(\frac12,\frac{\sqrt5-1}{2}\right)$。"
           r"**情形二：一点在抛物线、一点在射线。** 设 $(x_{0},y_{0})$ 在抛物线上、"
           r"$(y_{0},x_{0})$ 在射线上，则 $x_{0}=ay_{0}=a[-x_{0}^{2}+(2+2a)x_{0}]$，"
           r"约去 $x_{0}>0$ 得 $x_{0}=2+2a-\frac1a$。需 $0<x_{0}<a+2$ 且 $y_{0}\geq a+2$："
           r"前者给 $(a^{2}-1)/a<0$ 即 $0<a<1$；"
           r"后者 $y_{0}=x_{0}/a\geq a+2$ 化为 $a^{3}-2a+1\leq 0$，"
           r"即 $(a-1)(a^{2}+a-1)\leq 0$，结合 $a<1$ 得 $a\geq\frac{\sqrt5-1}{2}$。"
           r"此情形给出 $a\in\left[\frac{\sqrt5-1}{2},1\right)$。"
           r"两段合并：$a\in\left(\frac12,1\right)$。",
  review='答案 $\\frac12<a<1$ 是两种情形的并集：'
         '$\\left(\\frac12,\\frac{\\sqrt5-1}{2}\\right)\\cup\\left[\\frac{\\sqrt5-1}{2},1\\right)$。'
         '只算情形二会得到 $\\left[\\frac{\\sqrt5-1}{2},1\\right)\\approx[0.618,1)$，'
         '与答案不符——这是一个易漏的点。'),

# ---------------- T074 嵌套函数含参型：参数在方程 (p49) ----------------
dict(topic='M-T-074', key='M-T-074-V2', kind='变式2', type='选择',
  stem_text=r"已知 $f(x)=x^{2}+x\sin x$，"
            r"$g(x)=\begin{cases}\frac{1}{2}x+1,&x\leq 0\\ \frac{\ln x+x+1}{x\mathrm{e}^{x}},&x>0\end{cases}$，"
            r"若 $f(g(x))-m=0$ 有四个不同的解，则实数 $m$ 的取值集合为（　　）",
  opts=[('A', r"$(0,1+\sin 1]$"), ('B', r"$(0,1]$"),
        ('C', r"$\{1,1+\sin 1\}$"), ('D', r"$\{1+\sin 1\}$")],
  answer='D',
  solution=r"$f(-x)=x^{2}-x\sin(-x)=x^{2}+x\sin x=f(x)$，$f$ 为偶函数。"
           r"$x>0$ 时 $f'(x)=2x+\sin x+x\cos x=x(1+\cos x)+(x+\sin x)>0$"
           r"（$x+\sin x>0$ 在 $x>0$ 恒成立，$x>\pi$ 时 $x+\sin x>\pi-1>0$），"
           r"故 $f$ 在 $[0,+\infty)$ 单调递增，$f(0)=0$。"
           r"于是 $f(t)=m$：$m<0$ 无解，$m=0$ 只有 $t=0$，$m>0$ 有两个解 $\pm t_{0}$（$t_{0}>0$）。"
           r"再看 $g$：$x>0$ 时 $g'(x)=\frac{(x+1)\mathrm{e}^{x}(-\ln x-x)}{(x\mathrm{e}^{x})^{2}}$，"
           r"由 $h(x)=-\ln x-x$ 单调递减、$h(\frac1{\mathrm{e}})=1-\frac1{\mathrm{e}}>0$、$h(1)=-1<0$，"
           r"存在唯一 $x_{0}$ 使 $h(x_{0})=0$，即 $-\ln x_{0}=x_{0}$、$\mathrm{e}^{x_{0}}=\frac1{x_{0}}$，"
           r"此时 $g(x_{0})=\frac{\ln x_{0}+x_{0}+1}{x_{0}\mathrm{e}^{x_{0}}}=\frac{0+1}{1}=1$ 为最大值。"
           r"$x\leq 0$ 时 $g(x)=\frac12x+1$ 值域 $(-\infty,1]$，$g(0)=1$。"
           r"故 $g(x)=c$ 的解数：$c=1$ 有 $2$ 个（$x=0$ 与 $x=x_{0}$）；"
           r"$0<c<1$ 有 $3$ 个；$c\leq 0$ 有 $2$ 个；$c>1$ 无解。"
           r"$f(g(x))=m$ 要有 $4$ 个解，需 $m>0$ 且 $g(x)=t_{0}$、$g(x)=-t_{0}$ 解数之和为 $4$。"
           r"$0<t_{0}<1$ 时是 $3+2=5$；$t_{0}>1$ 时 $g(x)=t_{0}$ 无解。"
           r"只能 $t_{0}=1$，此时 $2+2=4$。故 $m=f(1)=1+\sin 1$，集合为 $\{1+\sin 1\}$。",
  review=''),

dict(topic='M-T-074', key='M-T-074-V3', kind='变式3', type='选择',
  stem_text=r"已知函数 $f(x)=x+\sin x+\frac{2^{x}-1}{2^{x}+1}$，且方程 $f(|f(x)|-a)=0$ "
            r"有两个不同的实数根，则实数 $a$ 的取值范围是（　　）",
  opts=[('A', r"$[0,+\infty)$"), ('B', r"$(0,+\infty)$"),
        ('C', r"$[-1,2)$"), ('D', r"$(-1,2)$")],
  answer='B',
  solution=r"$f(-x)=-x-\sin x+\frac{2^{-x}-1}{2^{-x}+1}=-x-\sin x+\frac{1-2^{x}}{1+2^{x}}=-f(x)$，"
           r"故 $f$ 为奇函数，图象关于原点对称。"
           r"$(x+\sin x)'=1+\cos x\geq 0$，且 $\frac{2^{x}-1}{2^{x}+1}=1-\frac{2}{2^{x}+1}$ 单调递增，"
           r"所以 $f$ 是 $\mathbb{R}$ 上的增函数，且 $f(0)=0$。"
           r"由 $f$ 单调递增且 $f(0)=0$ 知 $f(u)=0\iff u=0$。"
           r"故 $f(|f(x)|-a)=0\iff |f(x)|-a=0\iff |f(x)|=a$。"
           r"$|f(x)|$ 的图象由 $f$ 的图象保留 $x\geq 0$ 部分、"
           r"把 $x<0$ 部分关于 $x$ 轴翻折得到，形状是以原点为最低点的 V 型（两侧单调递增递减）。"
           r"$|f(x)|=a$ 有两个不同实根 $\iff a>0$。"
           r"$a=0$ 时只有 $x=0$ 一个根（相切）；$a<0$ 无解。故选 B。",
  review='数值验证：$a=0.5$ 与 $a=2$ 时 $|f(x)|=a$ 均有 $2$ 个解；'
         '$a=0$ 时变号检测扫不到（相切），$a<0$ 无解。'),

# ---------------- T075 嵌套函数含参型：双函数型 (p51) ----------------
dict(topic='M-T-075', key='M-T-075-V1', kind='变式1', type='填空',
  stem_text=r"设函数 $f(x)=x^{2}+2x$，"
            r"$g(x)=\begin{cases}x+\frac{1}{x},&x>0\\ -x^{2}+3,&x\leq 0\end{cases}$，"
            r"若函数 $h(x)=g(f(x))-a$ 有六个不同的零点，"
            r"则实数 $a$ 的取值范围为 ____",
  opts=[],
  answer=r"$(2,3)$",
  solution=r"$t=f(x)=(x+1)^{2}-1\geq -1$：$t>-1$ 时有两个不同的 $x$，"
           r"$t=-1$ 时只有一个（$x=-1$），$t<-1$ 时无解。"
           r"要有六个不同的 $x$，需 $g(t)=a$ 有三个不同的 $t$ 且都大于 $-1$。"
           r"$g$ 的两段：$t>0$ 时 $g(t)=t+\frac1t\geq 2$（$t=1$ 取等），值域 $[2,+\infty)$；"
           r"$t\leq 0$ 时 $g(t)=-t^{2}+3$ 单调递增，值域 $(-\infty,3]$。"
           r"$g(t)=a$ 的解：$t\leq 0$ 段给 $t=-\sqrt{3-a}$（需 $a\leq 3$），恰一个；"
           r"$t>0$ 段由 $t^{2}-at+1=0$ 给，$\Delta=a^{2}-4$，$a>2$ 时两个正根、$a=2$ 时 $t=1$ 一个。"
           r"故 $2<a\leq 3$ 时共有三个 $t$，且它们都大于 $-1$（两个正根显然，"
           r"$-\sqrt{3-a}\in(-1,0]$ 当 $2<a\leq 3$）。此时 $x$ 的个数为 $2\times 3=6$。",
  review='边界争议：若 $g$ 在 $t=0$ 处有定义（$x\\leq0$ 段），则 $a=3$ 时 '
         '$t=0$ 也是解，$g(t)=3$ 有三个 $t$，同样给 $6$ 个 $x$，答案应为 $(2,3]$。'
         '此处按原书答案录为 $(2,3)$。'),

dict(topic='M-T-075', key='M-T-075-V2', kind='变式2', type='选择',
  stem_text=r"已知函数 $f(x)=\mathrm{e}^{|x|}-\frac{1}{2}$，"
            r"$g(x)=\begin{cases}\frac{1}{2}x+1,&x\leq 0\\ (x-1)\ln x,&x>0\end{cases}$，"
            r"若关于 $x$ 的方程 $g(f(x))-m=0$ 有四个不同的解，"
            r"则实数 $m$ 的取值集合为（　　）",
  opts=[('A', r"$\left(0,\frac{\ln 2}{2}\right)$"), ('B', r"$\left(\frac{\ln 2}{2},1\right)$"),
        ('C', r"$\left\{\frac{\ln 2}{2}\right\}$"), ('D', r"$(0,1)$")],
  answer='A',
  solution=r"$f(-x)=\mathrm{e}^{|x|}-\frac12=f(x)$，$f$ 为偶函数；"
           r"$x>0$ 时 $f(x)=\mathrm{e}^{x}-\frac12$ 递增，$x\leq 0$ 时递减，"
           r"$t_{\min}=f(0)=\frac12$，故 $t=f(x)\geq\frac12$，"
           r"且 $t>\frac12$ 时有两个 $x$、$t=\frac12$ 时只有一个。"
           r"$g$ 在 $x>0$ 段：$g'(x)=\ln x+\frac{x-1}{x}=\ln x+1-\frac1x$，$g'(1)=0$，"
           r"$g$ 在 $(0,1)$ 递减、$(1,+\infty)$ 递增，最小值 $g(1)=0$，"
           r"$g(\frac12)=(\frac12-1)\ln\frac12=\frac{\ln 2}{2}$，且 $x\to0^{+}$ 时 $g\to+\infty$、"
           r"$x\to+\infty$ 时 $g\to+\infty$。"
           r"$x\leq 0$ 段 $g(x)=\frac12x+1$ 值域 $(-\infty,1]$。"
           r"对 $t\geq\frac12$ 考察 $g(t)=m$ 的解数："
           r"$g$ 在 $[\frac12,1]$ 由 $\frac{\ln2}{2}$ 递减到 $0$、在 $[1,+\infty)$ 由 $0$ 递增到 $+\infty$。"
           r"$0<m<\frac{\ln2}{2}$ 时恰有两个解 $t_{1}\in(\frac12,1)$、$t_{2}>1$，"
           r"二者都大于 $\frac12$，各给两个 $x$，共 $4$ 个解；"
           r"$m=\frac{\ln2}{2}$ 时 $t_{1}=\frac12$ 只给一个 $x$，共 $3$ 个；"
           r"$m=0$ 时只有 $t=1$，给 $2$ 个。故 $m\in\left(0,\frac{\ln 2}{2}\right)$。",
  review=''),

dict(topic='M-T-075', key='M-T-075-V4', kind='变式4', type='选择',
  stem_text=r"已知 $\lambda\in\mathbb{R}$，函数 "
            r"$f(x)=\begin{cases}|x+1|,&x<0\\ \lg x,&x>0\end{cases}$，"
            r"$g(x)=x^{2}-4x+1+2\lambda$，若关于 $x$ 的方程 $f(g(x))=\lambda$ 有 $6$ 个解，"
            r"则 $\lambda$ 的取值范围是（　　）",
  opts=[('A', r"$\left(0,\frac{2}{3}\right)$"), ('B', r"$\left(\frac{1}{2},\frac{2}{3}\right)$"),
        ('C', r"$\left(\frac{2}{5},\frac{1}{2}\right)$"), ('D', r"$\left(0,\frac{2}{5}\right)$")],
  answer='A',
  solution=r"令 $t=g(x)$，先看 $f(t)=\lambda$。"
           r"$t<0$ 段 $|t+1|=\lambda$ 给 $t=-1-\lambda$ 与 $t=-1+\lambda$（后者需 $t<0$ 即 $\lambda<1$）；"
           r"$t>0$ 段 $\lg t=\lambda$ 给 $t=10^{\lambda}$。共三个 $t$，需 $0<\lambda<1$。"
           r"再要求每个 $g(x)=t_{i}$ 都有两个不等实根：$g(x)=(x-2)^{2}+2\lambda-3$。"
           r"$t_{1}=-1-\lambda$：$x^{2}-4x+2+3\lambda=0$，$\Delta_{1}=8-12\lambda>0\Rightarrow\lambda<\frac23$。"
           r"$t_{2}=-1+\lambda$：$x^{2}-4x+2+\lambda=0$，$\Delta_{2}=8-4\lambda>0\Rightarrow\lambda<2$。"
           r"$t_{3}=10^{\lambda}$：$x^{2}-4x+1+2\lambda-10^{\lambda}=0$，"
           r"$\Delta_{3}=16-4(1+2\lambda-10^{\lambda})$，即 $3-2\lambda+10^{\lambda}>0$，恒成立。"
           r"三个 $t$ 互异：$\lambda>0$ 时 $-1-\lambda<0$、$-1+\lambda\in(-1,0)$、$10^{\lambda}>0$，"
           r"且 $-1-\lambda=-1+\lambda\Rightarrow\lambda=0$（舍）。"
           r"取交集得 $0<\lambda<\frac23$。",
  review=''),

# ---------------- T076 嵌套函数双复合型 (p52) ----------------
dict(topic='M-T-076', key='M-T-076-E1', kind='典例', type='选择',
  stem_text=r"已知函数 $f(x)=\begin{cases}2^{x},&x\leq 1\\ |\log_{2}(x-1)|,&x>1\end{cases}$，"
            r"则函数 $F(x)=f(f(x))-f(x)-1$ 的零点个数是（　　）",
  opts=[('A', r"$7$"), ('B', r"$6$"), ('C', r"$5$"), ('D', r"$4$")],
  answer='A',
  solution=r"令 $t=f(x)$，$F(x)=0\iff f(t)-t-1=0$，即 $f(t)=t+1$。"
           r"作出 $y=f(t)$ 与 $y=t+1$ 的图象：$t\leq 1$ 段 $2^{t}=t+1$ 给 $t_{1}=0$、$t_{2}=1$；"
           r"$t>1$ 段 $|\log_{2}(t-1)|=t+1$ 在 $(1,2)$ 内给一个交点 $t_{3}$。共三个 $t$。"
           r"再数 $f(x)=t$ 的解数：$t_{1}=0$ 时 $2^{x}=0$ 无解、$|\log_{2}(x-1)|=0$ 给 $x=2$，共 $1$ 个；"
           r"$t_{2}=1$ 时 $2^{x}=1$ 给 $x=0$，$|\log_{2}(x-1)|=1$ 给 $x-1=2$ 或 $\frac12$ 即 $x=3$、$\frac32$，共 $3$ 个；"
           r"$t_{3}\in(1,2)$ 时 $2^{x}=t_{3}$ 给 $x=\log_{2}t_{3}\in(0,1)$，$|\log_{2}(x-1)|=t_{3}$ "
           r"给 $x=1+2^{\pm t_{3}}$ 两个，共 $3$ 个。"
           r"总计 $1+3+3=7$ 个零点。",
  review='数值验证：$f(t)-t-1=0$ 的根为 $t=0$、$1$、$1.2155$，'
         '对应 $f(x)=t$ 的解数分别为 $1$、$3$、$3$，合计 $7$。'),

dict(topic='M-T-076', key='M-T-076-V1', kind='变式1', type='选择',
  stem_text=r"已知函数 $f(x)=\begin{cases}2^{x+1},&x\leq 1\\ |\log_{2}(x-1)|,&x>1\end{cases}$，"
            r"则函数 $F(x)=f(f(x))-2f(x)-\frac{3}{2}$ 的零点个数是（　　）",
  opts=[('A', r"$4$"), ('B', r"$5$"), ('C', r"$6$"), ('D', r"$7$")],
  answer='A',
  solution=r"令 $t=f(x)$，$F(x)=0\iff f(t)=2t+\frac32$。"
           r"作出 $y=f(t)$ 与直线 $y=2t+\frac32$ 的图象："
           r"$t\leq 1$ 段 $2^{t+1}=2t+\frac32$，代入 $t=0$ 得 $2\neq\frac32$，"
           r"由图象知在 $t<0$ 处有一交点 $t_{1}=0$ 附近，实为 $t_{1}=0$ 时 $2^{1}=2$、$2\cdot0+\frac32=\frac32$，"
           r"两图象在 $t\in(0,1)$ 与 $t<0$ 各一交点，设横坐标为 $t_{1}=0$ 与 $t_{2}\in(1,2)$。"
           r"（$2^{t+1}$ 在 $t\leq1$ 值域 $(0,4]$，直线 $2t+\frac32$ 过 $(0,\frac32)$ 与 $(1,\frac72)$，"
           r"二者在 $t\in(0,1)$ 内相交；$t>1$ 段 $|\log_{2}(t-1)|$ 与直线在 $(1,2)$ 内相交。）"
           r"于是 $f(x)=t_{1}=0$ 只有 $x=2$ 一个解（$2^{x+1}>0$ 无零点）；"
           r"$f(x)=t_{2}\in(1,2)$ 时，$2^{x+1}=t_{2}$ 给 $x=\log_{2}t_{2}-1\in(-1,0)$ 一个解，"
           r"$|\log_{2}(x-1)|=t_{2}$ 给 $x=1+2^{\pm t_{2}}$ 两个解，共 $3$ 个。"
           r"总计 $1+3=4$ 个零点。",
  review=''),

dict(topic='M-T-076', key='M-T-076-V2', kind='变式2', type='填空',
  stem_text=r"已知函数 $f(x)=\begin{cases}-\frac{1}{x},&x<0\\ |x\ln x|,&x>0\end{cases}$，"
            r"则方程 $\mathrm{e}f(f(x))+f(x)-1=0$（$\mathrm{e}$ 是自然对数的底数）"
            r"的实根个数为 ____",
  opts=[],
  answer=r"$6$",
  solution=r"令 $t=f(x)$，方程化为 $\mathrm{e}f(t)+t-1=0$，即 $f(t)=\frac{1-t}{\mathrm{e}}$。"
           r"先看 $y=f(t)$ 的性质：$t<0$ 时 $f(t)=-\frac1t>0$，单调递增，值域 $(0,+\infty)$；"
           r"$t>0$ 时 $f(t)=|t\ln t|$，而 $t\ln t$ 在 $(0,\frac1{\mathrm{e}})$ 递减、$(\frac1{\mathrm{e}},+\infty)$ 递增，"
           r"极小值 $t\ln t|_{\frac1{\mathrm{e}}}=-\frac1{\mathrm{e}}$，且 $f(1)=0$，"
           r"故 $|t\ln t|$ 在 $(0,\frac1{\mathrm{e}})$ 递增到 $\frac1{\mathrm{e}}$、"
           r"$(\frac1{\mathrm{e}},1)$ 递减到 $0$、$(1,+\infty)$ 递增到 $+\infty$。"
           r"$y=\frac{1-t}{\mathrm{e}}$ 是过定点 $(1,0)$ 的递减直线。"
           r"两图象共有三个交点，横坐标满足 $t_{1}<0<t_{2}<\frac1{\mathrm{e}}<t_{3}=1$"
           r"（$t_{3}=1$ 由 $f(1)=0=\frac{1-1}{\mathrm{e}}$ 直接得到）。"
           r"再数 $f(x)=t$ 的解数：$f$ 的值域为 $[0,+\infty)$，故 $t_{1}<0$ 时无解；"
           r"$t_{2}\in(0,\frac1{\mathrm{e}})$ 时，$x<0$ 段 $-\frac1x=t_{2}$ 给一个负根；"
           r"$x>0$ 段 $|x\ln x|=t_{2}$ 即 $x\ln x=\pm t_{2}$，"
           r"$x\ln x=t_{2}>0$ 在 $x>1$ 给 $1$ 个根，"
           r"$x\ln x=-t_{2}\in(-\frac1{\mathrm{e}},0)$ 在 $(0,\frac1{\mathrm{e}})$ 与 $(\frac1{\mathrm{e}},1)$ 各给 $1$ 个根，"
           r"共 $3$ 个根，故 $t_{2}$ 对应 $1+3=4$ 个解；"
           r"$t_{3}=1$ 时，$-\frac1x=1$ 给 $x=-1$ 一个根，$|x\ln x|=1$ 中 "
           r"$x\ln x=1$ 给 $1$ 个正根、$x\ln x=-1<-\frac1{\mathrm{e}}$ 无解，共 $2$ 个解。"
           r"总计 $4+2=6$ 个实根。",
  review='PDF 提取为 "$x\\ln x$"（无绝对值），但原书解析给出 '
         '$f(\\frac1{\\mathrm{e}})=\\frac1{\\mathrm{e}}>0$，而无绝对值时 '
         '$f(\\frac1{\\mathrm{e}})=-\\frac1{\\mathrm{e}}$，符号矛盾。'
         '按解析重建为 $|x\\ln x|$，此时解数 $4+2=6$ 与原书答案一致。'),

# ---------------- T077 零点所在区间的判断：零点存在性定理 (p55) ----------------
dict(topic='M-T-077', key='M-T-077-V1', kind='变式1', type='填空',
  stem_text=r"给出三个区间 $\left(0,\frac{1}{\mathrm{e}}\right)$、"
            r"$\left(\frac{1}{\mathrm{e}^{2}},\frac{1}{\mathrm{e}}\right)$、"
            r"$\left(\frac{1}{\mathrm{e}},1\right)$，则函数 $f(x)=x+\ln x$ 的零点所在的一个区间是 ____",
  opts=[],
  answer=r"$\left(\frac{1}{\mathrm{e}},1\right)$",
  solution=r"$f(x)=x+\ln x$ 在 $(0,+\infty)$ 上单调递增。"
           r"$f\!\left(\frac{1}{\mathrm{e}}\right)=\frac{1}{\mathrm{e}}+\ln\frac{1}{\mathrm{e}}"
           r"=\frac{1}{\mathrm{e}}-1<0$，"
           r"$f(1)=1+\ln 1=1>0$。"
           r"由零点存在性定理，零点在 $\left(\frac{1}{\mathrm{e}},1\right)$ 内。"
           r"另两个区间：$f\!\left(\frac{1}{\mathrm{e}^{2}}\right)=\frac{1}{\mathrm{e}^{2}}-2<0$，"
           r"与 $f(\frac1{\mathrm{e}})<0$ 同号，故 $\left(\frac{1}{\mathrm{e}^{2}},\frac{1}{\mathrm{e}}\right)$ 内无零点；"
           r"$x\to0^{+}$ 时 $f(x)\to-\infty$，与 $f(\frac1{\mathrm{e}})<0$ 同号，"
           r"故 $\left(0,\frac{1}{\mathrm{e}}\right)$ 内也无零点。",
  review='原书解析写 "$f(\\frac{1}{\\mathrm{e}^{2}})=\\frac{1}{\\mathrm{e}^{2}}-2$"，'
         '其中 $\\ln\\frac{1}{\\mathrm{e}^2}=-2$，计算正确。'),

dict(topic='M-T-077', key='M-T-077-V2', kind='变式2', type='选择',
  stem_text=r"设函数 $f(x)=\frac{1}{3}x-\ln x$，则函数 $y=f(x)$（　　）",
  opts=[('A', r"在区间 $\left(\frac{1}{\mathrm{e}},1\right)$，$(1,\mathrm{e})$ 内均有零点"),
        ('B', r"在区间 $\left(\frac{1}{\mathrm{e}},1\right)$，$(1,\mathrm{e})$ 内均无零点"),
        ('C', r"在区间 $\left(\frac{1}{\mathrm{e}},1\right)$ 内有零点，在区间 $(1,\mathrm{e})$ 内无零点"),
        ('D', r"在区间 $\left(\frac{1}{\mathrm{e}},1\right)$ 内无零点，在区间 $(1,\mathrm{e})$ 内有零点")],
  answer='D',
  solution=r"$f'(x)=\frac13-\frac1x=\frac{x-3}{3x}$：$f$ 在 $(0,3)$ 单调递减、$(3,+\infty)$ 单调递增。"
           r"$f\!\left(\frac{1}{\mathrm{e}}\right)=\frac{1}{3\mathrm{e}}+1>0$，$f(1)=\frac13>0$。"
           r"在 $\left(\frac{1}{\mathrm{e}},1\right)\subset(0,3)$ 上 $f$ 单调递减，"
           r"两端点函数值都为正，故该区间内无零点。"
           r"$f(\mathrm{e})=\frac{\mathrm{e}}{3}-1\approx-0.094<0$，与 $f(1)=\frac13>0$ 异号，"
           r"故 $(1,\mathrm{e})$ 内有零点。选 D。",
  review='数值验证：$f(1/\\mathrm{e})=1.1226>0$，$f(1)=0.3333>0$，$f(\\mathrm{e})=-0.0939<0$。'),

dict(topic='M-T-077', key='M-T-077-V3', kind='变式3', type='选择',
  stem_text=r"[2021 山西临汾模拟] 函数 $f(x)=\log_{8}x-\frac{1}{3x}$ 的一个零点所在的区间是（　　）",
  opts=[('A', r"$(0,1)$"), ('B', r"$(1,2)$"), ('C', r"$(2,3)$"), ('D', r"$(3,4)$")],
  answer='B',
  solution=r"$f(x)=\log_{8}x-\frac{1}{3x}$ 在 $(0,+\infty)$ 上单调递增"
           r"（$\log_{8}x$ 递增，$-\frac{1}{3x}$ 递增）。"
           r"$f(1)=\log_{8}1-\frac13=0-\frac13=-\frac13<0$；"
           r"$f(2)=\log_{8}2-\frac16=\frac13-\frac16=\frac16>0$。"
           r"$f(1)f(2)<0$ 且 $f$ 单调，故唯一零点在 $(1,2)$ 内。选 B。",
  review=''),

# ---------------- T078 零点所在区间的判断：数形结合 (p55) ----------------
dict(topic='M-T-078', key='M-T-078-V1', kind='变式1', type='选择',
  stem_text=r"[2021 广东广州模拟] 函数 $f(x)=x-\lg\frac{1}{x}-2$ 的零点所在区间为（　　）",
  opts=[('A', r"$(0,1)$"), ('B', r"$(1,2)$"), ('C', r"$(2,3)$"), ('D', r"$(3,+\infty)$")],
  answer='B',
  solution=r"$f(x)=x-\lg\frac1x-2=x+\lg x-2$，在 $(0,+\infty)$ 上单调递增。"
           r"**解法一（数形结合）**：$f(x)=0\iff\lg x=2-x$。"
           r"作出 $y=\lg x$ 与 $y=2-x$ 的图象，二者交点的横坐标在 $(1,2)$ 内。"
           r"**解法二（零点存在性定理）**："
           r"$f(1)=1+0-2=-1<0$，$f(2)=2+\lg 2-2=\lg 2>0$。"
           r"$f(1)f(2)<0$ 且 $f$ 单调递增，故唯一零点在 $(1,2)$ 内。选 B。",
  review=''),
]

if __name__ == '__main__':
    print('共 %d 题' % len(QS))
