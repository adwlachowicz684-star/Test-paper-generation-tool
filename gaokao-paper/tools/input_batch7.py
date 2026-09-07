# -*- coding: utf-8 -*-
r"""第7批录入数据：T067 一元二次复合型(根的分布) / T068 参变分离与判别式，共 7 题。

来源：2024高中数学热点题型归纳完整解析版.pdf p41~p42
      —— 基于 ref_bank 提取文本逐题重建，7 题答案全部独立验算通过。

**LaTeX 相关字符串一律 raw 双引号 `r"..."`**：
单引号会被导数撇号 $f'(x)$ 提前终止（一次坏 7 处，SyntaxError）。

本批的重建说明（PDF 提取丢失了绝对值符号，靠解析的解数特征反推）：
  T067-V1  原文提取为 "1/|x| - 1"，但该形式最多 4 解，与"恰有 6 解"矛盾。
           按解析解数特征（t=0→2解、t∈(0,1)→4解、t≥1→2解）重建为 |1/|x|-1|
  T067-V2  原文提取为 "log4 x"，但 t∈(1,2) 需 3 解，重建为 |log_4 x|
  T068-V1  与 T068-V2 同题（答案存疑且无解析），跳过
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'py'))

QS = [
# ---------------- T067 一元二次复合型：根的分布型 (p41) ----------------
dict(topic='M-T-067', key='M-T-067-E1', kind='典例', type='选择',
  stem_text=r"已知函数 $f(x)=\frac{x}{\mathrm{e}^{x}}$，若关于 $x$ 的方程 "
            r"$f^{2}(x)-mf(x)-2m^{2}=0$ 有三个不同的实数解，则 $m$ 的取值范围是（　　）",
  opts=[('A', r"$\left(0,\frac{1}{2\mathrm{e}}\right)\cup\left(-\frac{1}{\mathrm{e}},0\right)$"),
        ('B', r"$\left(-\frac{1}{\mathrm{e}},\frac{1}{2\mathrm{e}}\right)$"),
        ('C', r"$\left(-\frac{1}{\mathrm{e}},\frac{1}{\mathrm{e}}\right)$"),
        ('D', r"$\left(-\infty,\frac{1}{2\mathrm{e}}\right)$")],
  answer='A',
  solution=r"$f'(x)=\frac{1-x}{\mathrm{e}^{x}}$：在 $(-\infty,1)$ 上 $f'(x)>0$，$f$ 单调递增；"
           r"在 $(1,+\infty)$ 上 $f'(x)<0$，$f$ 单调递减。"
           r"$f(1)=\frac{1}{\mathrm{e}}$ 为最大值，$f(0)=0$，"
           r"$x<0$ 时 $f(x)<0$ 且 $x\to-\infty$ 时 $f(x)\to-\infty$，"
           r"$x\to+\infty$ 时 $f(x)\to 0^{+}$。"
           r"故对值 $t$：$t<0$ 或 $t=0$ 有 $1$ 个解，$0<t<\frac{1}{\mathrm{e}}$ 有 $2$ 个解，"
           r"$t=\frac{1}{\mathrm{e}}$ 有 $1$ 个解，$t>\frac{1}{\mathrm{e}}$ 无解。"
           r"令 $t=f(x)$，方程化为 $t^{2}-mt-2m^{2}=0$。"
           r"$m=0$ 时方程为 $f(x)=0$，仅 $x=0$ 一解，舍去。"
           r"$m\neq 0$ 时 $t_{1}t_{2}=-2m^{2}<0$，两根异号：负根给 $1$ 个解，"
           r"故正根需落在 $\left(0,\frac{1}{\mathrm{e}}\right)$ 才有 $2$ 个解，总计 $3$ 个解。"
           r"记 $\varphi(t)=t^{2}-mt-2m^{2}$，需 "
           r"$\varphi(0)=-2m^{2}<0$ 且 $\varphi\!\left(\frac{1}{\mathrm{e}}\right)"
           r"=\frac{1}{\mathrm{e}^{2}}-\frac{m}{\mathrm{e}}-2m^{2}>0$。"
           r"后者即 $2m^{2}+\frac{m}{\mathrm{e}}-\frac{1}{\mathrm{e}^{2}}<0$，"
           r"解得 $-\frac{1}{\mathrm{e}}<m<\frac{1}{2\mathrm{e}}$。"
           r"又 $m\neq 0$，故 $m\in\left(-\frac{1}{\mathrm{e}},0\right)\cup"
           r"\left(0,\frac{1}{2\mathrm{e}}\right)$。故选 A。",
  review=''),

dict(topic='M-T-067', key='M-T-067-V1', kind='变式1', type='选择',
  stem_text=r"已知函数 $f(x)=\left|\frac{1}{|x|}-1\right|$，若关于 $x$ 的方程 "
            r"$f^{2}(x)+bf(x)+c=0$ 恰有 $6$ 个不同的实数解，"
            r"则 $b$、$c$ 的取值情况不可能的是（　　）",
  opts=[('A', r"$-1<b<0$，$c=0$"),
        ('B', r"$1+b+c>0$，$c>0$"),
        ('C', r"$1+b+c<0$，$c>0$"),
        ('D', r"$1+b+c=0$，$0<c<1$")],
  answer='B',
  solution=r"先看方程 $f(x)=t$ 的解数。由 $f(x)\geq 0$，$t<0$ 无解。"
           r"$t=0$：$\frac{1}{|x|}=1$，$|x|=1$，$2$ 个解。"
           r"$0<t<1$：$\frac{1}{|x|}-1=\pm t$，即 $|x|=\frac{1}{1+t}$ 或 $\frac{1}{1-t}$，"
           r"各给 $2$ 个解，共 $4$ 个解。"
           r"$t\geq 1$：$\frac{1}{|x|}=1+t$（因 $1-t\leq 0$ 舍去），$2$ 个解。"
           r"令 $t=f(x)$，方程化为 $t^{2}+bt+c=0$，两根 $t_{1}$、$t_{2}$，"
           r"$\varphi(t)=t^{2}+bt+c=(t-t_{1})(t-t_{2})$。"
           r"要共 $6$ 个解，只能是一根在 $(0,1)$（$4$ 解）配合另一根为 $0$ 或不小于 $1$（$2$ 解）。"
           r"① $t_{2}=0$：$c=0$，$t_{1}=-b\in(0,1)$，即 $-1<b<0$，对应 A。"
           r"② $t_{2}=1$：$\varphi(1)=1+b+c=0$，$c=t_{1}\in(0,1)$，对应 D。"
           r"③ $t_{2}>1$：$c=t_{1}t_{2}>0$，$\varphi(1)=(1-t_{1})(1-t_{2})<0$"
           r"即 $1+b+c<0$，对应 C。"
           r"再看 B：$c>0$ 说明两根同号，$\varphi(1)>0$ 说明两根同在 $1$ 同侧。"
           r"若都大于 $1$，各 $2$ 解共 $4$ 个；若都在 $(0,1)$，各 $4$ 解共 $8$ 个；"
           r"若都小于 $0$ 则无解。均不等于 $6$，故 B 不可能。选 B。",
  review='PDF 提取为 "1/|x| - 1"，但该形式下 $t>0$ 仅 $2$ 解、$t=0$ 无解，'
         '最多 $4$ 个解，与"恰有 $6$ 个解"矛盾。'
         '按解析的解数特征（$t=0\\to2$ 解、$t\\in(0,1)\\to4$ 解、$t\\geq1\\to2$ 解）'
         '重建为 $\\left|\\frac{1}{|x|}-1\\right|$，与全部四个选项自洽。'),

dict(topic='M-T-067', key='M-T-067-V2', kind='变式2', type='选择',
  stem_text=r"设函数 $f(x)=\begin{cases}3^{x}+1,&x\leq 0\\ |\log_{4}x|,&x>0\end{cases}$，"
            r"若关于 $x$ 的方程 $f^{2}(x)-(a+2)f(x)+3=0$ 恰好有六个不同的实数解，"
            r"则实数 $a$ 的取值范围为（　　）",
  opts=[('A', r"$\left(2\sqrt{3}-2,\frac{3}{2}\right]$"),
        ('B', r"$\left(-2\sqrt{3}-2,2\sqrt{3}-2\right)$"),
        ('C', r"$\left(\frac{3}{2},+\infty\right)$"),
        ('D', r"$\left(2\sqrt{3}-2,+\infty\right)$")],
  answer='A',
  solution=r"$x\leq 0$ 时 $f(x)=3^{x}+1\in(1,2]$ 且单调递增，"
           r"故 $t\in(1,2)$ 有 $1$ 个解、$t=2$ 有 $1$ 个解（$x=0$）。"
           r"$x>0$ 时 $f(x)=|\log_{4}x|$，对任意 $t>0$ 有 "
           r"$x=4^{t}$ 与 $x=4^{-t}$ 两个解。"
           r"故 $t\in(1,2)$ 时方程 $f(x)=t$ 共 $1+2=3$ 个解，$t=2$ 时也是 $3$ 个解，"
           r"$t=1$ 时只有 $x>0$ 段的 $2$ 个解。"
           r"令 $t=f(x)$，方程化为 $t^{2}-(a+2)t+3=0$，记 $\varphi(t)=t^{2}-(a+2)t+3$。"
           r"要共 $6$ 个解，需两根都在 $(1,2]$ 内且不同（各给 $3$ 个解）："
           r"$\Delta=(a+2)^{2}-12>0$，$1<\frac{a+2}{2}<2$，"
           r"$\varphi(1)=2-a>0$，$\varphi(2)=3-2a\geq 0$。"
           r"解得 $a>2\sqrt{3}-2$ 或 $a<-2\sqrt{3}-2$；$0<a<2$；$a<2$；$a\leq\frac{3}{2}$。"
           r"取交集得 $2\sqrt{3}-2<a\leq\frac{3}{2}$。故选 A。",
  review='PDF 提取为 "$\\log_4 x$"（无绝对值），但此时 $t\\in(1,2)$ 只有 $2$ 个解，'
         '两根最多 $4$ 解，凑不出"六个"。加上绝对值后 $t\\in(1,2)$ 有 $3$ 个解，'
         '与"六个"吻合，且 $\\varphi(2)\\geq0$ 允许取等的边界处理也自洽。'),

dict(topic='M-T-067', key='M-T-067-V3', kind='变式3', type='选择',
  stem_text=r"设定义域为 $\mathbb{R}$ 的函数 "
            r"$f(x)=\begin{cases}5^{|x-1|}-1,&x\geq 0\\ x^{2}+4x+4,&x<0\end{cases}$，"
            r"若关于 $x$ 的方程 $f^{2}(x)-(2m+1)f(x)+m^{2}=0$ 有 $7$ 个不同的实数解，"
            r"则 $m=$（　　）",
  opts=[('A', r"$m=6$"), ('B', r"$m=2$"), ('C', r"$m=6$ 或 $2$"), ('D', r"$m=-6$")],
  answer='B',
  solution=r"先看 $f(x)=t$ 的解数。"
           r"$x\geq 0$：$5^{|x-1|}=t+1$ 即 $|x-1|=\log_{5}(t+1)\triangleq L$。"
           r"$t=0$ 时 $L=0$，$x=1$（$1$ 个解）；"
           r"$0<t<4$ 时 $0<L<1$，$x=1\pm L$ 均非负（$2$ 个解）；"
           r"$t=4$ 时 $L=1$，$x=0$ 或 $2$（$2$ 个解）；"
           r"$t>4$ 时 $L>1$，$x=1-L<0$ 舍去（$1$ 个解）。"
           r"$x<0$：$f(x)=(x+2)^{2}\geq 0$，$x=-2\pm\sqrt{t}$，需小于 $0$。"
           r"$t=0$ 时 $x=-2$（$1$ 个解）；$0<t<4$ 时两解均为负（$2$ 个解）；"
           r"$t=4$ 时 $x=-4$（$1$ 个解）；$t>4$ 时仅 $x=-2-\sqrt{t}$（$1$ 个解）。"
           r"合计：$t=0$ 有 $2$ 解，$0<t<4$ 有 $4$ 解，$t=4$ 有 $3$ 解，$t>4$ 有 $2$ 解。"
           r"要共 $7$ 解，只能 $3+4$，即一根 $t_{1}=4$、另一根 $t_{2}\in(0,4)$。"
           r"由 $\varphi(4)=16-4(2m+1)+m^{2}=0$ 得 $m^{2}-8m+12=0$，$m=2$ 或 $6$。"
           r"又 $t_{1}+t_{2}=2m+1\in(4,8)$：$m=2$ 时 $5\in(4,8)$ 且 $t_{2}=\frac{m^{2}}{4}=1\in(0,4)$；"
           r"$m=6$ 时 $13\notin(4,8)$，舍去。故 $m=2$，选 B。",
  review=''),

# ---------------- T068 参变分离与判别式、求根公式型 (p42) ----------------
dict(topic='M-T-068', key='M-T-068-E1', kind='典例', type='选择',
  stem_text=r"已知 $f(x)=\frac{x}{\ln x}$，若关于 $x$ 的方程 "
            r"$[f(x)]^{2}+mf(x)-\mathrm{e}^{2}+1=0$ 恰有 $3$ 个不同的实数解"
            r"（$\mathrm{e}$ 为自然对数的底数），则实数 $m$ 的取值范围是（　　）",
  opts=[('A', r"$m<\frac{1}{\mathrm{e}}$"), ('B', r"$m\geq-\frac{1}{\mathrm{e}}$"),
        ('C', r"$m<-\frac{1}{\mathrm{e}}$"), ('D', r"$m\geq\frac{1}{\mathrm{e}}$")],
  answer='C',
  solution=r"$f'(x)=\frac{\ln x-1}{\ln^{2}x}$，定义域 $(0,1)\cup(1,+\infty)$。"
           r"在 $(0,1)$ 上 $f'(x)<0$，$f$ 从 $0^{-}$ 递减到 $-\infty$，值域 $(-\infty,0)$；"
           r"在 $(1,\mathrm{e})$ 上 $f'(x)<0$，$f$ 从 $+\infty$ 递减到 $\mathrm{e}$；"
           r"在 $(\mathrm{e},+\infty)$ 上 $f'(x)>0$，$f$ 从 $\mathrm{e}$ 递增到 $+\infty$。"
           r"故 $t<0$ 有 $1$ 个解，$t=\mathrm{e}$ 有 $1$ 个解，$t>\mathrm{e}$ 有 $2$ 个解，"
           r"$0<t<\mathrm{e}$ 及 $t=0$ 无解。"
           r"令 $t=f(x)$，方程化为 $t^{2}+mt-\mathrm{e}^{2}+1=0$，"
           r"即 $m=-t+\frac{\mathrm{e}^{2}-1}{t}\triangleq g(t)$，$t<0$ 或 $t\geq\mathrm{e}$。"
           r"$g'(t)=-1-\frac{\mathrm{e}^{2}-1}{t^{2}}<0$，$g$ 在 $(-\infty,0)$ 与 $[\mathrm{e},+\infty)$ 上递减，"
           r"$g(\mathrm{e})=-\mathrm{e}+\frac{\mathrm{e}^{2}-1}{\mathrm{e}}=-\frac{1}{\mathrm{e}}$。"
           r"两根之积为 $1-\mathrm{e}^{2}<0$，一正一负：负根恒给 $1$ 个解，"
           r"要总计 $3$ 个解，正根需大于 $\mathrm{e}$（给 $2$ 个解）。"
           r"由 $g$ 递减，正根 $>\mathrm{e}\iff m=g(t)<g(\mathrm{e})=-\frac{1}{\mathrm{e}}$。"
           r"$m=-\frac{1}{\mathrm{e}}$ 时正根恰为 $\mathrm{e}$ 只给 $1$ 个解，总 $2$ 个，不合。"
           r"故 $m<-\frac{1}{\mathrm{e}}$，选 C。",
  review=''),

# T068-V1 与 V2 同题（问法不同），V1 无解析且答案存疑，跳过

dict(topic='M-T-068', key='M-T-068-V2', kind='变式2', type='填空',
  stem_text=r"已知函数 $f(x)=\frac{x^{2}-3}{\mathrm{e}^{x}}$，若关于 $x$ 的方程 "
            r"$[f(x)]^{2}+tf(x)-\frac{12}{\mathrm{e}^{2}}=0$（$t\in\mathbb{R}$）有 $m$ 个不同的实数解，"
            r"则 $m$ 的所有可能的值构成的集合为 ____",
  opts=[],
  answer=r"$\{3\}$",
  solution=r"$f'(x)=\frac{2x-(x^{2}-3)}{\mathrm{e}^{x}}=-\frac{(x+1)(x-3)}{\mathrm{e}^{x}}$。"
           r"$f$ 在 $(-\infty,-1)$ 递减、$(-1,3)$ 递增、$(3,+\infty)$ 递减，"
           r"极小值 $f(-1)=\frac{1-3}{\mathrm{e}^{-1}}=-2\mathrm{e}$，"
           r"极大值 $f(3)=\frac{9-3}{\mathrm{e}^{3}}=\frac{6}{\mathrm{e}^{3}}$，"
           r"$x\to-\infty$ 时 $f\to+\infty$，$x\to+\infty$ 时 $f\to 0^{+}$。"
           r"按三段计数：$t>\frac{6}{\mathrm{e}^{3}}$ 有 $1$ 解；"
           r"$t=\frac{6}{\mathrm{e}^{3}}$ 有 $2$ 解（$x=3$ 及 $(-\infty,-1)$ 段一个）；"
           r"$0<t<\frac{6}{\mathrm{e}^{3}}$ 有 $3$ 解；$t=0$ 有 $2$ 解（$x=\pm\sqrt{3}$）；"
           r"$-2\mathrm{e}<t<0$ 有 $2$ 解；$t=-2\mathrm{e}$ 有 $1$ 解（$x=-1$）；$t<-2\mathrm{e}$ 无解。"
           r"令 $n=f(x)$，方程化为 $n^{2}+tn-\frac{12}{\mathrm{e}^{2}}=0$，"
           r"判别式 $\Delta=t^{2}+\frac{48}{\mathrm{e}^{2}}>0$，两根 $n_{1}n_{2}=-\frac{12}{\mathrm{e}^{2}}<0$，一正一负。"
           r"注意 $\frac{6}{\mathrm{e}^{3}}\cdot(-2\mathrm{e})=-\frac{12}{\mathrm{e}^{2}}$，"
           r"$n_{1}>\frac{6}{\mathrm{e}^{3}}\iff -2\mathrm{e}<n_{2}<0$，此时 $1+2=3$；"
           r"$n_{1}=\frac{6}{\mathrm{e}^{3}}\iff n_{2}=-2\mathrm{e}$，此时 $2+1=3$；"
           r"$0<n_{1}<\frac{6}{\mathrm{e}^{3}}\iff n_{2}<-2\mathrm{e}$，此时 $3+0=3$。"
           r"三种情形均为 $3$ 个解，故 $m$ 的取值集合为 $\{3\}$。",
  review='ref_bank 中同题的 V1（选择题，问 $n$ 的可能值）标答为 "1 或 3"，'
         '但该形式下不存在 $1$ 个解的情形（正根恒至少给 $1$ 个解，负根不会同时为 $0$ 解之外的情况），'
         '且 V1 无解析可核对。V1 与本题同题，已跳过，避免把存疑答案录进题库。'),

dict(topic='M-T-068', key='M-T-068-V3', kind='变式3', type='填空',
  stem_text=r"已知 $f(x)=\begin{cases}-x^{2}+2x,&x\geq 0\\ |x-1|-1,&x<0\end{cases}$，"
            r"关于 $x$ 的不等式 $[f(x)]^{2}+af(x)-b^{2}<0$ 有且只有一个整数解，"
            r"则实数 $a$ 的最大值是 ____",
  opts=[],
  answer=r"$8$",
  solution=r"先化简：$x<0$ 时 $|x-1|=1-x$，故 $f(x)=1-x-1=-x>0$；"
           r"$x\geq 0$ 时 $f(x)=-x^{2}+2x$，在 $[0,1]$ 增、$[1,+\infty)$ 减，$f(0)=f(2)=0$，$f(1)=1$。"
           r"（1）$b=0$ 时不等式为 $f(x)[f(x)+a]<0$。"
           r"$a=0$ 时 $f^{2}(x)<0$ 无解；"
           r"$a<0$ 时需 $0<f(x)<-a$，由 $x<0$ 时 $f(x)>0$ 知有无限多个负整数满足，不合；"
           r"$a>0$ 时需 $-a<f(x)<0$。由 $f(x)<0$ 得 $x>2$，"
           r"在整数 $x=3,4,5,\ldots$ 上 $f(3)=-3$、$f(4)=-8$、$f(5)=-15$ 递减。"
           r"要恰有一个整数解，只能是 $x=3$：$f(3)=-3>-a$ 且 $f(4)=-8\leq -a$，"
           r"即 $-8\leq -a<-3$，解得 $3<a\leq 8$。"
           r"（2）$b\neq 0$ 时，$[f(x)]^{2}+af(x)-b^{2}<0$ 的解集为 "
           r"$\frac{-a-\sqrt{a^{2}+4b^{2}}}{2}<f(x)<\frac{-a+\sqrt{a^{2}+4b^{2}}}{2}$，"
           r"因 $b^{2}>0$，左端 $<0<$ 右端，故 $f(x)=0$ 的两个整数解 $x=0$、$x=2$ 都落入区间，"
           r"至少两个整数解，不合题意。"
           r"综上 $3<a\leq 8$，$a$ 的最大值为 $8$。",
  review=''),
]

if __name__ == '__main__':
    print('共 %d 题' % len(QS))
