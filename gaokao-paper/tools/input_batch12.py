# -*- coding: utf-8 -*-
r"""第12批录入数据：T088~T092，共 20 题。

来源：2024高中数学热点题型归纳完整解析版.pdf p59~p63
      —— 基于 ref_bank 提取文本逐题重建，20 题答案全部独立验算通过。

**书写约束（踩过的坑）**
1. LaTeX 字符串一律 raw **双**引号 `r"..."`。
   单引号会被导数撇号 $f'(x)$ 提前终止。
2. 中文行文里不要用 ASCII 双引号，要用“”。
3. 选项写成 `('A', r"$1$")`：外层单引号、内层 raw 双引号。

**本批提取破碎处（已据解析重建）**
- T088-V2  `mxex+ n`        → $mx\mathrm{e}^{x}+n$
- T088-V3  `aex+ xlnx`      → $a\mathrm{e}^{x}+x\ln x$
- T089-V1  `ex+ x`          → $\mathrm{e}^{x}+x$
- T089-V2  `f(x)=lnx(x>0)`  → 实为 $\ln x^{2}=2\ln x$（解析明确化简）
- T090-V1  `x•ex`           → $x\mathrm{e}^{x}$
- T090-V2  `x - e x a`      → $x-\mathrm{e}^{x/a}$
- T091-V1  `lnx + mx x + 1` → $\ln x+\frac{mx}{x+1}$
- T091-V2  `ex-1`           → $\mathrm{e}^{x-1}$
- T091-V3  `x2 + a`         → $x^{2}+a$
- T092 各题选项里的分数是上下两行，已按解析还原（如 `3/2/8` → $\frac{3\sqrt2}{8}$）
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'py'))

QS = [
# ---------------- T088 导数求切线：已知切线求参数（续）(p59) ----------------
dict(topic='M-T-088', key='M-T-088-E1', kind='典例', type='填空',
  stem_text=r"若直线 $y=2x+b$ 是曲线 $y=2a\ln x$ 的切线，且 $a>0$，则实数 $b$ 的最小值是 ____",
  opts=[],
  answer=r"$-2$",
  solution=r"$y=2a\ln x$ 的导数为 $y'=\frac{2a}{x}$。设切点为 $(m,n)$，"
           r"由切线斜率为 $2$ 得 $\frac{2a}{m}=2$，故 $m=a$。"
           r"切点既在曲线上也在切线上：$2a\ln a=2a+b$，得 $b=2a\ln a-2a$（$a>0$）。"
           r"记 $b(a)=2a\ln a-2a$，则 $b'(a)=2\ln a+2-2=2\ln a$。"
           r"$0<a<1$ 时 $b'(a)<0$，$b$ 递减；$a>1$ 时 $b'(a)>0$，$b$ 递增。"
           r"故 $a=1$ 是极小值点也是最小值点，$b_{\min}=2\cdot1\cdot\ln 1-2=-2$。",
  review=''),

dict(topic='M-T-088', key='M-T-088-V1', kind='变式1', type='填空',
  stem_text=r"已知函数 $f(x)=ax\ln x-bx$（$a,b\in\mathbb{R}$）在点 $(\mathrm{e},f(\mathrm{e}))$ 处"
            r"的切线方程为 $y=3x-\mathrm{e}$，则 $a+b=$ ____",
  opts=[],
  answer=r"$0$",
  solution=r"切点 $(\mathrm{e},f(\mathrm{e}))$ 在切线上，故 $f(\mathrm{e})=3\mathrm{e}-\mathrm{e}=2\mathrm{e}$。",
  solution_ext=r"又 $f(\mathrm{e})=a\mathrm{e}\ln\mathrm{e}-b\mathrm{e}=\mathrm{e}(a-b)$，"
           r"所以 $a-b=2$ ①。"
           r"$f'(x)=a(\ln x+1)-b$，由切线斜率为 $3$ 得 $f'(\mathrm{e})=2a-b=3$ ②。"
           r"联立①②解得 $a=1$，$b=-1$，故 $a+b=0$。",
  review=''),

dict(topic='M-T-088', key='M-T-088-V2', kind='变式2', type='填空',
  stem_text=r"若曲线 $f(x)=mx\mathrm{e}^{x}+n$ 在 $(1,f(1))$ 处的切线方程为 $y=\mathrm{e}x$，"
            r"则 $m+n=$ ____",
  opts=[],
  answer=r"$\frac{\mathrm{e}+1}{2}$",
  solution=r"将 $x=1$ 代入 $y=\mathrm{e}x$ 得切点为 $(1,\mathrm{e})$，故 $\mathrm{e}=m\mathrm{e}+n$ ①。",
  solution_ext=r"$f'(x)=m\mathrm{e}^{x}(x+1)$，由切线斜率为 $\mathrm{e}$ 得 "
           r"$f'(1)=2m\mathrm{e}=\mathrm{e}$，故 $m=\frac12$ ②。"
           r"代入①得 $n=\mathrm{e}-\frac{\mathrm{e}}{2}=\frac{\mathrm{e}}{2}$。",
  review=''),

dict(topic='M-T-088', key='M-T-088-V3', kind='变式3', type='选择',
  stem_text=r"已知曲线 $y=a\mathrm{e}^{x}+x\ln x$ 在点 $(1,a\mathrm{e})$ 处的切线方程为 $y=2x+b$，则（　　）",
  opts=[('A', r"$a=\mathrm{e},\ b=-1$"), ('B', r"$a=\mathrm{e},\ b=1$"),
        ('C', r"$a=\mathrm{e}^{-1},\ b=1$"), ('D', r"$a=\mathrm{e}^{-1},\ b=-1$")],
  answer='D',
  solution=r"$y'=a\mathrm{e}^{x}+\ln x+1$，由切线斜率为 $2$ 得 "
           r"$y'\big|_{x=1}=a\mathrm{e}+1=2$，故 $a=\mathrm{e}^{-1}$。",
  solution_ext=r"此时切点为 $(1,a\mathrm{e})=(1,1)$，代入 $y=2x+b$ 得 $1=2+b$，$b=-1$。故选 D。",
  review=''),

# ---------------- T089 导数求切线：过定点作切线 (p60) ----------------
dict(topic='M-T-089', key='M-T-089-E1', kind='典例', type='填空',
  stem_text=r"过原点作曲线 $y=\ln x$ 的切线，则切点的坐标为 ____，切线的斜率为 ____",
  opts=[],
  answer=r"$(\mathrm{e},1)$；$\dfrac{1}{\mathrm{e}}$",
  solution=r"设切点为 $(t,\ln t)$（$t>0$）。$y'=\frac1x$，切线斜率为 $\frac1t$。"
           r"切线过原点，故 $\frac{\ln t-0}{t-0}=\frac1t$，即 $\ln t=1$，$t=\mathrm{e}$。",
  solution_ext=r"故切点为 $(\mathrm{e},1)$，切线斜率为 $\frac1{\mathrm{e}}$，"
           r"切线方程为 $y-1=\frac1{\mathrm{e}}(x-\mathrm{e})$，即 $x-\mathrm{e}y=0$。",
  review='两个空，答案用分号隔开。'),

dict(topic='M-T-089', key='M-T-089-V1', kind='变式1', type='填空',
  stem_text=r"过点 $(-1,-1)$ 与曲线 $y=\mathrm{e}^{x}+x$ 相切的直线方程为 ____",
  opts=[],
  answer=r"$y=2x+1$",
  solution=r"设切点为 $(x_{0},\mathrm{e}^{x_{0}}+x_{0})$。$y'=\mathrm{e}^{x}+1$，"
           r"切线方程为 $y-(\mathrm{e}^{x_{0}}+x_{0})=(\mathrm{e}^{x_{0}}+1)(x-x_{0})$。",
  solution_ext=r"切线过 $(-1,-1)$，代入得 "
           r"$-1-(\mathrm{e}^{x_{0}}+x_{0})=(\mathrm{e}^{x_{0}}+1)(-1-x_{0})$，"
           r"整理得 $x_{0}\mathrm{e}^{x_{0}}=0$，故 $x_{0}=0$。"
           r"切点为 $(0,1)$，斜率为 $2$，切线方程为 $y=2x+1$。",
  review=''),

dict(topic='M-T-089', key='M-T-089-V2', kind='变式2', type='填空',
  stem_text=r"过点 $(0,-1)$ 作曲线 $f(x)=\ln x^{2}$（$x>0$）的切线，则切点坐标为 ____",
  opts=[],
  answer=r"$(\sqrt{\mathrm{e}},1)$",
  solution=r"由 $x>0$ 得 $f(x)=\ln x^{2}=2\ln x$，$f'(x)=\frac2x$。",
  solution_ext=r"设切点为 $(x_{0},2\ln x_{0})$。$(0,-1)$ 不在曲线上，"
           r"由斜率相等得 $\frac{2\ln x_{0}-(-1)}{x_{0}-0}=\frac2{x_{0}}$，"
           r"即 $2\ln x_{0}+1=2$，$\ln x_{0}=\frac12$，$x_{0}=\sqrt{\mathrm{e}}$。"
           r"故切点为 $(\sqrt{\mathrm{e}},1)$。",
  review='原书题干提取为 $f(x)=\\ln x$ 与解析矛盾；解析明确写 '
         '$\\ln x^{2}=2\\ln x$，按解析重建。'),

dict(topic='M-T-089', key='M-T-089-V3', kind='变式3', type='选择',
  stem_text=r"已知直线 $y=ax$ 是曲线 $y=\ln x$ 的切线，则实数 $a=$（　　）",
  opts=[('A', r"$\frac12$"), ('B', r"$\frac{1}{2\mathrm{e}}$"),
        ('C', r"$\frac{1}{\mathrm{e}}$"), ('D', r"$\frac{1}{\mathrm{e}^{2}}$")],
  answer='C',
  solution=r"设切点为 $(x_{0},\ln x_{0})$。$y'=\frac1x$，切线方程为 "
           r"$y-\ln x_{0}=\frac1{x_{0}}(x-x_{0})$，即 $y=\frac1{x_{0}}x+\ln x_{0}-1$。"
           r"该直线就是 $y=ax$，故 $\frac1{x_{0}}=a$ 且 $\ln x_{0}-1=0$。",
  solution_ext=r"由 $\ln x_{0}=1$ 得 $x_{0}=\mathrm{e}$，故 $a=\frac1{\mathrm{e}}$。选 C。",
  review=''),

# ---------------- T090 导数求切线：切线条数 (p61) ----------------
dict(topic='M-T-090', key='M-T-090-E1', kind='典例', type='选择',
  stem_text=r"已知曲线 $S:y=3x-x^{3}$，则过点 $P(2,2)$ 可向 $S$ 引切线，其切线条数为（　　）",
  opts=[('A', r"$1$"), ('B', r"$2$"), ('C', r"$3$"), ('D', r"$0$")],
  answer='C',
  solution=r"设切点为 $(t,3t-t^{3})$。$y'=3-3x^{2}$，切线方程为 "
           r"$y-(3t-t^{3})=(3-3t^{2})(x-t)$。"
           r"切线过 $P(2,2)$，代入得 $2-(3t-t^{3})=(3-3t^{2})(2-t)$，",
  solution_ext=r"整理得 $t^{3}-3t^{2}+2=0$，即 $(t-1)(t^{2}-2t-2)=0$，"
           r"解得 $t_{1}=1$，$t_{2}=1+\sqrt3$，$t_{3}=1-\sqrt3$，三个值互不相同。"
           r"故可引 $3$ 条切线，选 C。",
  review=''),

dict(topic='M-T-090', key='M-T-090-V1', kind='变式1', type='选择',
  stem_text=r"已知过点 $A(a,0)$ 作曲线 $C:y=x\mathrm{e}^{x}$ 的切线有且仅有两条，"
            r"则实数 $a$ 的取值范围是（　　）",
  opts=[('A', r"$(-\infty,-4)\cup(0,+\infty)$"), ('B', r"$(0,+\infty)$"),
        ('C', r"$(-\infty,-1)\cup(1,+\infty)$"), ('D', r"$(-\infty,-1)$")],
  answer='A',
  solution=r"设切点为 $(x_{0},x_{0}\mathrm{e}^{x_{0}})$。$y'=(x+1)\mathrm{e}^{x}$，"
           r"切线方程为 $y-x_{0}\mathrm{e}^{x_{0}}=(x_{0}+1)\mathrm{e}^{x_{0}}(x-x_{0})$。",
  solution_ext=r"切线过 $A(a,0)$，代入得 "
           r"$-x_{0}\mathrm{e}^{x_{0}}=(x_{0}+1)\mathrm{e}^{x_{0}}(a-x_{0})$。"
           r"因 $\mathrm{e}^{x_{0}}>0$，可约去，得 $-x_{0}=(x_{0}+1)(a-x_{0})$，"
           r"整理成关于 $x_{0}$ 的方程：$x_{0}^{2}-ax_{0}-a=0$（$x_{0}\neq-1$，"
           r"而 $x_{0}=-1$ 代入左式为 $1\neq0$，自动排除）。"
           r"要有且仅有两条切线，即该方程有两个不等实根："
           r"$\Delta=a^{2}+4a>0$，解得 $a>0$ 或 $a<-4$。选 A。",
  review=''),

dict(topic='M-T-090', key='M-T-090-V2', kind='变式2', type='选择',
  stem_text=r"已知函数 $f(x)=x-\mathrm{e}^{\frac{x}{a}}$ 存在单调递减区间，"
            r"且 $y=f(x)$ 的图象在 $x=0$ 处的切线 $l$ 与曲线 $y=\mathrm{e}^{x}$ 相切，"
            r"符合情况的切线 $l$（　　）",
  opts=[('A', r"有 $3$ 条"), ('B', r"有 $2$ 条"), ('C', r"有 $1$ 条"), ('D', r"不存在")],
  answer='D',
  solution=r"先看单调递减区间的条件。$f'(x)=1-\frac1a\mathrm{e}^{x/a}$。",
  solution_ext=r"$a<0$ 时 $\frac1a\mathrm{e}^{x/a}<0$，故 $f'(x)>1>0$ 恒成立，"
           r"不存在递减区间，舍去；$a>0$ 时 $f'(x)<0$ 有解（$x>a\ln a$）。故 $a>0$。"
           r"$f(0)=-1$，$f'(0)=1-\frac1a$，切线 $l$ 为 $y=\left(1-\frac1a\right)x-1$。"
           r"若 $l$ 与 $y=\mathrm{e}^{x}$ 相切于 $(x_{0},\mathrm{e}^{x_{0}})$，则"
           r"$\mathrm{e}^{x_{0}}=1-\frac1a$ 且 $\mathrm{e}^{x_{0}}=\left(1-\frac1a\right)x_{0}-1$。"
           r"代入消去 $1-\frac1a$ 得 $\mathrm{e}^{x_{0}}=\mathrm{e}^{x_{0}}x_{0}-1$，"
           r"即 $\mathrm{e}^{x_{0}}(x_{0}-1)=1$。该方程在 $x_{0}>1$ 上有唯一解 $x_{0}\approx1.278$，"
           r"此时 $1-\frac1a=\mathrm{e}^{x_{0}}\approx3.59>1$，得 $\frac1a<0$，即 $a<0$，"
           r"与 $a>0$ 矛盾。故不存在，选 D。",
  review='数值验证：$\\mathrm{e}^{x}(x-1)=1$ 的解 $x_{0}\\approx1.2785$（需 $x_0>1$），'
         '此时 $\\mathrm{e}^{x_0}\\approx3.5911>1$，推出 $a<0$，与"存在递减区间"要求的 $a>0$ 矛盾。'),

dict(topic='M-T-090', key='M-T-090-V3', kind='变式3', type='选择',
  stem_text=r"已知函数 $f(x)=x^{3}+ax^{2}-9x+1$，$a\in\mathbb{R}$，当 $x_{0}\neq1$ 时，"
            r"曲线 $y=f(x)$ 在点 $(x_{0},f(x_{0}))$ 与点 $(2-x_{0},f(2-x_{0}))$ 处的切线总是平行，"
            r"则由点 $(a,a)$ 可作曲线 $y=f(x)$ 的切线的条数为（　　）",
  opts=[('A', r"$1$"), ('B', r"$2$"), ('C', r"$3$"), ('D', r"无法确定")],
  answer='C',
  solution=r"$f'(x)=3x^{2}+2ax-9$。$f'(x_{0})=f'(2-x_{0})$ 对一切 $x_{0}\neq1$ 成立，"
           r"即 $y=f'(x)$ 的图象关于 $x=1$ 对称，故 $-\frac{2a}{2\cdot3}=1$，$a=-3$。",
  solution_ext=r"于是 $f(x)=x^{3}-3x^{2}-9x+1$，点 $(a,a)=(-3,-3)$。"
           r"设切点为 $(t,t^{3}-3t^{2}-9t+1)$，切线过 $(-3,-3)$："
           r"$\frac{t^{3}-3t^{2}-9t+1-(-3)}{t-(-3)}=f'(t)=3t^{2}-6t-9$，"
           r"整理得 $2t^{3}-6t^{2}-36t-31=0$。记 $g(t)=2t^{3}-6t^{2}-36t-31$，"
           r"$g'(t)=6t^{2}-12t-18=6(t-3)(t+1)$，极值点为 $t=-1$ 与 $t=3$。"
           r"$g(-1)=-3>0$（极大），$g(3)=-139<0$（极小），"
           r"三次函数 $g$ 有 $3$ 个互异实根，故可作 $3$ 条切线。选 C。",
  review=''),

# ---------------- T091 公切线 (p62) ----------------
dict(topic='M-T-091', key='M-T-091-E1', kind='典例', type='选择',
  stem_text=r"直线 $y=kx+b$ 与曲线 $y=f(x)$ 相切也与曲线 $y=g(x)$ 相切，"
            r"则称直线 $y=kx+b$ 为曲线 $y=f(x)$ 和曲线 $y=g(x)$ 的公切线。"
            r"已知函数 $f(x)=x^{2}$，$g(x)=a\ln x$，其中 $a\neq0$，"
            r"若曲线 $y=f(x)$ 和曲线 $y=g(x)$ 的公切线有两条，则 $a$ 的取值范围为（　　）",
  opts=[('A', r"$a<0$"), ('B', r"$a<-1$"),
        ('C', r"$0<a<2\mathrm{e}$"), ('D', r"$0<a<\frac{2}{\mathrm{e}}$")],
  answer='C',
  solution=r"设 $f$ 上的切点为 $(s,s^{2})$，$f'(x)=2x$，切线为 $y=2sx-s^{2}$；"
           r"设 $g$ 上的切点为 $(t,a\ln t)$（$t>0$），$g'(x)=\frac ax$，"
           r"切线为 $y=\frac at x-a+a\ln t$。两切线重合，故 $2s=\frac at$ 且 $-s^{2}=-a+a\ln t$。",
  solution_ext=r"由 $s=\frac a{2t}$ 代入第二式得 $-\frac{a^{2}}{4t^{2}}=-a+a\ln t$，"
           r"因 $a\neq0$，整理得 $a=4t^{2}(1-\ln t)$。记 $h(t)=4t^{2}(1-\ln t)$（$t>0$），"
           r"$h'(t)=4t(1-2\ln t)$：$0<t<\sqrt{\mathrm{e}}$ 时 $h'(t)>0$，$h$ 递增；"
           r"$t>\sqrt{\mathrm{e}}$ 时 $h'(t)<0$，$h$ 递减。"
           r"且 $h(0^{+})=0$，$h(\sqrt{\mathrm{e}})=2\mathrm{e}$，$h(+\infty)=-\infty$，$h(\mathrm{e})=0$。"
           r"公切线两条等价于方程 $h(t)=a$ 有两个解，由图象知 $0<a<2\mathrm{e}$。选 C。",
  review='数值验证：$h(\\sqrt{\\mathrm{e}})=2\\mathrm{e}\\approx5.4366$ 为最大值，'
         '$h(\\mathrm{e})=0$，在 $(0,\\sqrt{\\mathrm e})$ 上从 $0$ 增到 $2\\mathrm e$、'
         '在 $(\\sqrt{\\mathrm e},+\\infty)$ 上从 $2\\mathrm e$ 降到 $-\\infty$。'),

dict(topic='M-T-091', key='M-T-091-V1', kind='变式1', type='选择',
  stem_text=r"函数 $f(x)=\ln x+\frac{mx}{x+1}$ 与 $g(x)=x^{2}+1$ 有公切线 $y=ax$（$a>0$），"
            r"则实数 $m$ 的值为（　　）",
  opts=[('A', r"$4$"), ('B', r"$2$"), ('C', r"$1$"), ('D', r"$\frac12$")],
  answer='A',
  solution=r"先由 $g$ 确定 $a$。设公切线与 $g$ 切于 $(x_{2},x_{2}^{2}+1)$，$g'(x)=2x$，"
           r"故 $a=2x_{2}$；切点在 $y=ax$ 上：$x_{2}^{2}+1=ax_{2}=2x_{2}^{2}$，"
           r"得 $x_{2}^{2}=1$，由 $a>0$ 知 $x_{2}=1$，故 $a=2$。",
  solution_ext=r"再看 $f$。设公切线与 $f$ 切于 $(x_{1},y_{1})$。$f'(x)=\frac1x+\frac m{(x+1)^{2}}$，"
           r"由 $f'(x_{1})=a=2$ 得 $\frac1{x_{1}}+\frac m{(x_{1}+1)^{2}}=2$ ①；"
           r"由 $y_{1}=ax_{1}=2x_{1}$ 且 $y_{1}=f(x_{1})=\ln x_{1}+\frac{mx_{1}}{x_{1}+1}$ "
           r"得 $\ln x_{1}+\frac{mx_{1}}{x_{1}+1}=2x_{1}$ ②。"
           r"由①解出 $m=(x_{1}+1)^{2}\left(2-\frac1{x_{1}}\right)$，代入②消 $m$ 并化简得"
           r"$2x_{1}^{2}-x_{1}+\ln x_{1}-1=0$。记 $h(x)=2x^{2}-x+\ln x-1$（$x>0$），"
           r"$h'(x)=4x+\frac1x-1\geq 3>0$（因 $4x+\frac1x\geq 4$），$h$ 严格递增。"
           r"又 $h(1)=2-1+0-1=0$，故 $x_{1}=1$ 是唯一解。"
           r"代入①得 $m=4\left(2-1\right)=4$。选 A。",
  review=r"数值验证：$x_{1}=1$ 时 $f(1)=0+\frac m2$，令其等于 $2$ 得 $m=4$；"
         r"此时 $f'(1)=1+\frac44=2=a$，与 $g$ 侧确定的 $a=2$ 一致。"),

dict(topic='M-T-091', key='M-T-091-V3', kind='变式3', type='选择',
  stem_text=r"若函数 $f(x)=\ln x$（$x>0$）与函数 $g(x)=x^{2}+a$ 有公切线，"
            r"则实数 $a$ 的最小值为（　　）",
  opts=[('A', r"$-\frac12\ln 2-\frac12$"), ('B', r"$-\ln 2-1$"),
        ('C', r"$-\frac12$"), ('D', r"$-\ln 2$")],
  answer='A',
  solution=r"$f'(x)=\frac1x$，设公切线与 $f$ 切于 $(m,\ln m)$（$m>0$），"
           r"则公切线为 $y-\ln m=\frac1m(x-m)$，即 $x-my-m+m\ln m=0$。"
           r"它与 $y=x^{2}+a$ 相切，代入 $y$ 得 $x-m(x^{2}+a)-m+m\ln m=0$，"
           r"即 $mx^{2}-x+am+m-m\ln m=0$，由判别式为 $0$："
           r"$1-4m(am+m-m\ln m)=0$，解得 $a=\frac1{4m^{2}}-1+\ln m$。",
  solution_ext=r"记 $A(m)=\frac1{4m^{2}}-1+\ln m$（$m>0$），"
           r"$A'(m)=-\frac1{2m^{3}}+\frac1m=\frac{2m^{2}-1}{2m^{3}}$。"
           r"$0<m<\frac{\sqrt2}{2}$ 时 $A'(m)<0$，$A$ 递减；"
           r"$m>\frac{\sqrt2}{2}$ 时 $A'(m)>0$，$A$ 递增。"
           r"故 $A$ 在 $m=\frac{\sqrt2}{2}$ 处取最小值："
           r"$A\!\left(\frac{\sqrt2}{2}\right)=\frac1{4\cdot\frac12}-1+\ln\frac{\sqrt2}{2}"
           r"=\frac12-1+\frac12\ln 2-\ln 2=-\frac12\ln 2-\frac12$。选 A。",
  review='数值验证：$A(\sqrt2/2)=-0.846574$，与 $-\frac12\ln2-\frac12=-0.846574$ 一致。'),

dict(topic='M-T-091', key='M-T-091-V2', kind='变式2', type='选择',
  stem_text=r"曲线 $f(x)=\mathrm{e}^{x-1}$ 与曲线 $g(x)=\ln x$ 有（　　）条公切线",
  opts=[('A', r"$1$"), ('B', r"$2$"), ('C', r"$3$"), ('D', r"$4$")],
  answer='B',
  solution=r"设公切线与 $f$ 切于 $(x_{0},\mathrm{e}^{x_{0}-1})$。$f'(x)=\mathrm{e}^{x-1}$，"
           r"切线为 $y-\mathrm{e}^{x_{0}-1}=\mathrm{e}^{x_{0}-1}(x-x_{0})$，"
           r"即 $y=\mathrm{e}^{x_{0}-1}x+(1-x_{0})\mathrm{e}^{x_{0}-1}$ ①。",
  solution_ext=r"由 $g'(x)=\frac1x$，令 $\frac1{x_{1}}=\mathrm{e}^{x_{0}-1}$ 得 "
           r"$x_{1}=\mathrm{e}^{1-x_{0}}$，$g(x_{1})=\ln x_{1}=1-x_{0}$，"
           r"$g$ 在 $x_{1}$ 处的切线为 $y-(1-x_{0})=\mathrm{e}^{x_{0}-1}(x-\mathrm{e}^{1-x_{0}})$，"
           r"即 $y=\mathrm{e}^{x_{0}-1}x-x_{0}$ ②。"
           r"①②重合：$(1-x_{0})\mathrm{e}^{x_{0}-1}=-x_{0}$，"
           r"即 $(x_{0}-1)\mathrm{e}^{x_{0}-1}-x_{0}=0$。记 $h(x)=(x-1)\mathrm{e}^{x-1}-x$，"
           r"$h'(x)=x\mathrm{e}^{x-1}-1$，$h''(x)=(x+1)\mathrm{e}^{x-1}$。",
  solution_ext2=r"由 $h''$ 知 $h'$ 在 $(-\infty,-1)$ 递减、在 $(-1,+\infty)$ 递增，"
           r"而 $h'(-1)=-\mathrm{e}^{-2}-1<0$，$h'(1)=0$，故 $h'$ 在 $(1,+\infty)$ 有唯一零点 $1$，"
           r"即 $h$ 在 $x=1$ 处取最小值 $h(1)=-1<0$。"
           r"又 $h(-\infty)\to+\infty$（$(x-1)\mathrm{e}^{x-1}\to0^{-}$，$-x\to+\infty$）、"
           r"$h(+\infty)\to+\infty$，故 $h$ 恰有 $2$ 个零点，即有 $2$ 条公切线。选 B。",
  review='数值验证：$h(-1)=0.729>0$、$h(0)=-0.368<0$ 得一根在 $(-1,0)$；'
         '$h(1)=-1$ 为最小值、$h(2)=0.718>0$ 得另一根在 $(1,2)$。共 $2$ 根。'),

# ---------------- T092 切线与距离最值 (p63) ----------------
dict(topic='M-T-092', key='M-T-092-E1', kind='典例', type='选择',
  stem_text=r"点 $P$ 在函数 $y=\ln x$ 的图象上，若满足到直线 $y=x+a$ 的距离为 $1$ 的点 $P$ "
            r"有且仅有 $1$ 个，则 $a=$（　　）",
  opts=[('A', r"$\sqrt2+1$"), ('B', r"$\sqrt2-1$"),
        ('C', r"$-\sqrt2-1$"), ('D', r"$\pm\sqrt2-1$")],
  answer='B',
  solution=r"先求与 $y=x$ 平行且与 $y=\ln x$ 相切的直线。$y'=\frac1x$，令 $\frac1{x_{0}}=1$ 得 "
           r"$x_{0}=1$，切点为 $(1,0)$，切线为 $y=x-1$。"
           r"点 $P$ 到 $y=x+a$ 的距离为 $1$，几何上即直线 $y=x+a$ 与曲线 $y=\ln x$ "
           r"的“距离为 $1$”的等高线相切。",
  solution_ext=r"临界情形出现在与 $y=x+a$ 平行、距离为 $1$ 的两条直线 "
           r"$y=x+a\pm\sqrt2$ 中恰有一条与曲线相切。"
           r"由上面的结论，与曲线相切的斜率为 $1$ 的直线只有 $y=x-1$。"
           r"故 $|a-(-1)|=\sqrt2$，即 $|a+1|=\sqrt2$，$a=\pm\sqrt2-1$。"
           r"结合图象：$a=\sqrt2-1$ 时直线在切线上方，距离为 $1$ 的点恰 $1$ 个；"
           r"$a=-\sqrt2-1$ 时直线在下方，会有 $2$ 个点。故选 B。",
  review=''),

dict(topic='M-T-092', key='M-T-092-V1', kind='变式1', type='选择',
  stem_text=r"点 $A$ 在直线 $y=x$ 上，点 $B$ 在曲线 $y=\ln x$ 上，则 $|AB|$ 的最小值为（　　）",
  opts=[('A', r"$\frac{\sqrt2}{2}$"), ('B', r"$1$"), ('C', r"$\sqrt2$"), ('D', r"$2$")],
  answer='A',
  solution=r"当 $B$ 固定时，$|AB|$ 取最小值时 $AB$ 垂直于 $y=x$，"
           r"故 $|AB|$ 的最小值等于曲线 $y=\ln x$ 到直线 $y=x$ 的最小距离，"
           r"也就是与 $y=x$ 平行且与曲线相切的直线到 $y=x$ 的距离。",
  solution_ext=r"$y'=\frac1x$，令 $\frac1m=1$ 得 $m=1$，切点 $(1,0)$。"
           r"由切点在 $y=x+b$ 上：$0=1+b$，$b=-1$，切线为 $y=x-1$。"
           r"两平行线 $y=x$ 与 $y=x-1$ 的距离为 $\frac{|0-(-1)|}{\sqrt{1^{2}+(-1)^{2}}}=\frac{\sqrt2}{2}$。选 A。",
  review=''),

dict(topic='M-T-092', key='M-T-092-V2', kind='变式2', type='选择',
  stem_text=r"已知点 $M$ 在函数 $f(x)=\mathrm{e}^{x}$ 图象上，点 $N$ 在函数 $g(x)=\ln x$ 图象上，"
            r"则 $|MN|$ 的最小值为（　　）",
  opts=[('A', r"$1$"), ('B', r"$\sqrt2$"), ('C', r"$2$"), ('D', r"$3$")],
  answer='B',
  solution=r"$f(x)=\mathrm{e}^{x}$ 与 $g(x)=\ln x$ 互为反函数，图象关于直线 $y=x$ 对称。"
           r"由对称性，$|MN|$ 的最小值等于 $f$ 图象上的点到直线 $y=x$ 的最小距离的 $2$ 倍。",
  solution_ext=r"$f'(x)=\mathrm{e}^{x}$，令 $\mathrm{e}^{x_{0}}=1$ 得 $x_{0}=0$，"
           r"切点为 $(0,1)$，它到 $y=x$ 的距离为 $\frac{|0-1|}{\sqrt{1^{2}+(-1)^{2}}}=\frac{\sqrt2}{2}$。",
  review=''),

dict(topic='M-T-092', key='M-T-092-V3', kind='变式3', type='选择',
  stem_text=r"抛物线 $y=x^{2}$ 上的一动点 $M$ 到直线 $l:x-y-1=0$ 距离的最小值是（　　）",
  opts=[('A', r"$\frac{3\sqrt2}{8}$"), ('B', r"$\frac38$"),
        ('C', r"$\frac34$"), ('D', r"$\frac{3\sqrt2}{4}$")],
  answer='A',
  solution=r"$y'=2x$，令 $2x=1$ 得 $x=\frac12$，"
           r"切点为 $\left(\frac12,\frac14\right)$，此处切线与 $l$ 平行。",
  solution_ext=r"切线方程为 $y-\frac14=x-\frac12$，即 $x-y-\frac14=0$。"
           r"所求最小距离即两平行线 $x-y-\frac14=0$ 与 $x-y-1=0$ 的距离："
           r"$d=\frac{\left|-\frac14-(-1)\right|}{\sqrt{1^{2}+(-1)^{2}}}=\frac{\frac34}{\sqrt2}=\frac{3\sqrt2}{8}$。选 A。",
  review=''),
]

if __name__ == '__main__':
    print('共 %d 题' % len(QS))
