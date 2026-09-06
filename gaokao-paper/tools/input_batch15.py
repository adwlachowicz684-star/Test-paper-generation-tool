# -*- coding: utf-8 -*-
r"""第15批补录数据：T098~T100，共 10 题（导数含参讨论·单调性与极值）。

**为什么叫"补录"**

第 15 批在上一轮被报告为“已完成 7 题、全库 171 题”，但实际上
`input_batch15.py` / `commit_batch15.py` **根本不存在**，数据没有落盘。
那一轮只做了读原文和验算，没有写库，报告却用了推算的数字。

本脚本是真正的补录。教训已写进 skill：
**汇报前必须跑一次实际计数，禁止用“计划题数”推算。**

来源：2024高中数学热点题型归纳完整解析版.pdf p68~p70

**注意：本批是 10 题，不是上一轮报告的 7 题。**
（T098 有 4 题：E1/V1/V2/V3；T099 有 3 题；T100 有 3 题）

**两处原书问题（均已数值验证）**

1. **T098-E1 原书“综上”有笔误**。前文推导「$k\geq1$ 时 $f'(x)<0$，$f(x)$
   在 $(0,+\infty)$ 上单调递减」是对的，但末尾综述写成
   「当 $k\geq1$ 时，$f(x)$ 在 $(0,+\infty)$ 上单调递增」。
   按正确的（递减）录入，并在 review 注明。

2. **T100-E1 的函数是 $f(x)=x+a\mathrm e^{-x}$，不是 $\dfrac{x+a}{\mathrm e^{x}}$**。
   依据有三：
   - 原书给 $f'(x)=1-a\mathrm e^{-x}$，正是 $x+a\mathrm e^{-x}$ 的导数；
   - 原书极小值 $f(\ln a)=\ln a+1$，与 $x+a\mathrm e^{-x}$ 吻合；
   - 若按 $\frac{x+a}{\mathrm e^{x}}$，则 $f'(x)=\frac{1-x-a}{\mathrm e^{x}}$，
     $a\leq0$ 时符号不定，与原书“当 $a\leq0$ 时 $f'(x)>0$”矛盾。
   数值抽查确认（$a=0.5$、$2$、$5$ 三组，极小值与 $\ln a+1$ 完全相等）。

**书写约束**
1. LaTeX 字符串一律 raw **双**引号 r"..."；单引号会被 $f'(x)$ 的撇号终止。
2. 中文行文用弯引号，不用 ASCII 双引号（会终止 raw 串）。
3. 多行 raw 拼接时逗号只在**最后一行**。
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'py'))

QS = [
# ---------------- T098 双参（p68）----------------
dict(topic='M-T-098', key='M-T-098-E1', kind='典例', type='解答',
  stem_text=r"已知函数 $f(x)=(1-k)x-k\ln x+k-1$，其中 $k\in\mathbb{R}$，$k\neq0$。讨论函数 $f(x)$ 的单调性。",
  opts=[],
  answer=r"当 $k<0$ 时，$f(x)$ 在 $(0,+\infty)$ 上单调递增；"
         r"当 $0<k<1$ 时，$f(x)$ 在 $\left(0,\dfrac k{1-k}\right)$ 上单调递减，"
         r"在 $\left(\dfrac k{1-k},+\infty\right)$ 上单调递增；"
         r"当 $k\geq1$ 时，$f(x)$ 在 $(0,+\infty)$ 上单调递减。",
  solution=r"$f(x)$ 的定义域为 $(0,+\infty)$，"
           r"$f'(x)=(1-k)-\dfrac kx=\dfrac{(1-k)x-k}x$。因 $x>0$，$f'(x)$ 的符号由 $(1-k)x-k$ 决定。",
  solution_ext=r"① 当 $1-k\leq0$ 即 $k\geq1$ 时：$1-k\leq0$ 且 $-k<0$，"
           r"故 $(1-k)x-k<0$ 恒成立，$f'(x)<0$，$f(x)$ 在 $(0,+\infty)$ 上单调递减。"
           r"② 当 $k<0$ 时：$-k>0$ 且 $(1-k)x>0$，故 $(1-k)x-k>0$ 恒成立，"
           r"$f'(x)>0$，$f(x)$ 在 $(0,+\infty)$ 上单调递增。",
  solution_ext2=r"③ 当 $0<k<1$ 时：$f'(x)=\dfrac{(1-k)\left(x-\frac k{1-k}\right)}x$，"
           r"其中 $\dfrac k{1-k}>0$。当 $0<x<\dfrac k{1-k}$ 时 $f'(x)<0$，$f(x)$ 单调递减；"
           r"当 $x>\dfrac k{1-k}$ 时 $f'(x)>0$，$f(x)$ 单调递增。"
           r"综上即得答案所述三种情形。",
  review=r"原书【详解】末尾的综述有笔误，写成「当 $k\geq1$ 时，$f(x)$ 在 $(0,+\infty)$ 上单调递增」，"
         r"与前文「$f'(x)<0$，$f(x)$ 在 $(0,+\infty)$ 上单调递减」矛盾。"
         r"数值抽查证实 $k=1,2,5$ 时均恒减，本录按正确的（递减）录入。"
         r"原书第 (2) 问为「设函数 $f(x)$ 的导函数为 $g(x)$，若函数 $f(x)$ 恰有两个零点 "
         r"$x_{1}$、$x_{2}$（$x_{1}<x_{2}$），证明 $g\!\left(\frac{x_{1}+2x_{2}}3\right)>0$」，"
         r"未给出详解，本录不含。"),

dict(topic='M-T-098', key='M-T-098-V1', kind='变式6', type='解答',
  stem_text=r"已知函数 $f(x)=(ax+1)\mathrm e^{x}$，其中 $\mathrm e$ 为自然对数的底数。求函数 $f(x)$ 的单调区间。",
  opts=[],
  answer=r"当 $a=0$ 时，$f(x)$ 在 $\mathbb{R}$ 上单调递增；"
         r"当 $a>0$ 时，$f(x)$ 在 $\left(-\infty,-1-\dfrac1a\right)$ 上单调递减，"
         r"在 $\left(-1-\dfrac1a,+\infty\right)$ 上单调递增；"
         r"当 $a<0$ 时，$f(x)$ 在 $\left(-\infty,-1-\dfrac1a\right)$ 上单调递增，"
         r"在 $\left(-1-\dfrac1a,+\infty\right)$ 上单调递减。",
  solution=r"由 $f(x)=(ax+1)\mathrm e^{x}$ 求得 "
           r"$f'(x)=a\mathrm e^{x}+(ax+1)\mathrm e^{x}=\mathrm e^{x}(ax+a+1)$，$x\in\mathbb{R}$。",
  solution_ext=r"因 $\mathrm e^{x}>0$，$f'(x)$ 的符号由 $ax+a+1$ 决定。记 $x_{0}=-1-\dfrac1a$（$a\neq0$）。"
           r"① 当 $a=0$ 时，$f'(x)=\mathrm e^{x}>0$，$f(x)$ 在 $\mathbb{R}$ 上单调递增。"
           r"② 当 $a>0$ 时：当 $x<x_{0}$ 时 $ax+a+1<0$，$f'(x)<0$，$f(x)$ 单调递减；"
           r"当 $x>x_{0}$ 时 $f'(x)>0$，$f(x)$ 单调递增。",
  solution_ext2=r"③ 当 $a<0$ 时：当 $x<x_{0}$ 时 $ax+a+1>0$（$a<0$，$x$ 越负则 $ax$ 越大），"
           r"$f'(x)>0$，$f(x)$ 单调递增；当 $x>x_{0}$ 时 $f'(x)<0$，$f(x)$ 单调递减。"
           r"由此即得答案所述三种情形。",
  review=r"$a$ 变号时单调性方向整体翻转，这是本题的关键。"
         r"数值抽查取 $a=1,2,0.5,-1,-2$ 五组，符号全部吻合。"
         r"原书第 (2) 问为「取 $a=0$ 并记此时曲线 $y=f(x)$ 在点 $P\left(x_{0},f\left(x_{0}\right)\right)$"
         r"（其中 $x_{0}<0$）处的切线为 $l$，$l$ 与 $x$ 轴、$y$ 轴所围成的三角形面积为 $S\left(x_{0}\right)$，"
         r"求 $S\left(x_{0}\right)$ 的解析式及最大值」，未给出详解，本录不含。"),

dict(topic='M-T-098', key='M-T-098-V2', kind='变式7', type='解答',
  stem_text=r"函数 $g(x)=ax-1-b\ln x$（$a,b\in\mathbb{R}$，$ab\neq0$）。讨论 $g(x)$ 的单调性。",
  opts=[],
  answer=r"当 $a>0$，$b<0$ 时，$g(x)$ 在 $(0,+\infty)$ 上单调递增；"
         r"当 $a>0$，$b>0$ 时，$g(x)$ 在 $\left(0,\dfrac ba\right)$ 上单调递减，"
         r"在 $\left(\dfrac ba,+\infty\right)$ 上单调递增；"
         r"当 $a<0$，$b>0$ 时，$g(x)$ 在 $(0,+\infty)$ 上单调递减；"
         r"当 $a<0$，$b<0$ 时，$g(x)$ 在 $\left(0,\dfrac ba\right)$ 上单调递增，"
         r"在 $\left(\dfrac ba,+\infty\right)$ 上单调递减。",
  solution=r"$g(x)$ 的定义域为 $(0,+\infty)$，$g'(x)=a-\dfrac bx=\dfrac{ax-b}x$。"
           r"因 $x>0$，$g'(x)$ 的符号由 $ax-b$ 决定。",
  solution_ext=r"① 当 $a>0$，$b<0$ 时，$ax>0$ 且 $-b>0$，故 $ax-b>0$ 恒成立，"
           r"$g(x)$ 在 $(0,+\infty)$ 上单调递增。"
           r"② 当 $a>0$，$b>0$ 时：令 $g'(x)>0$ 得 $x>\dfrac ba$；令 $g'(x)<0$ 得 $0<x<\dfrac ba$。"
           r"故 $g(x)$ 在 $\left(0,\dfrac ba\right)$ 上单调递减，在 $\left(\dfrac ba,+\infty\right)$ 上单调递增。",
  solution_ext2=r"③ 当 $a<0$，$b>0$ 时，$ax<0$ 且 $-b<0$，故 $ax-b<0$ 恒成立，"
           r"$g(x)$ 在 $(0,+\infty)$ 上单调递减。"
           r"④ 当 $a<0$，$b<0$ 时：$\dfrac ba>0$。令 $g'(x)>0$ 得 $0<x<\dfrac ba$；"
           r"令 $g'(x)<0$ 得 $x>\dfrac ba$。"
           r"故 $g(x)$ 在 $\left(0,\dfrac ba\right)$ 上单调递增，在 $\left(\dfrac ba,+\infty\right)$ 上单调递减。",
  review=r"双参题要按 $a$、$b$ 的符号分四种情形，逐一判断。"
         r"注意 $a$、$b$ 同号时 $\frac ba>0$（在定义域内），异号时 $\frac ba<0$（不在定义域内，故恒单调）。"
         r"数值抽查四种情形各取两组参数，符号全部吻合。"),

dict(topic='M-T-098', key='M-T-098-V3', kind='变式8', type='解答',
  stem_text=r"已知 $f(x)=\ln(x+m)-mx$。求 $f(x)$ 的单调区间。",
  opts=[],
  answer=r"当 $m\leq0$ 时，$f(x)$ 的单调递增区间为 $(-m,+\infty)$，无减区间；"
         r"当 $m>0$ 时，$f(x)$ 的单调递增区间为 $\left(-m,-m+\dfrac1m\right)$，"
         r"单调递减区间为 $\left(-m+\dfrac1m,+\infty\right)$。",
  solution=r"$f(x)=\ln(x+m)-mx$ 的定义域为 $x>-m$，$f'(x)=\dfrac1{x+m}-m$。",
  solution_ext=r"① 当 $m\leq0$ 时：$\dfrac1{x+m}>0$ 且 $-m\geq0$，故 $f'(x)>0$，"
           r"$f(x)$ 的单调递增区间为 $(-m,+\infty)$，无减区间。",
  solution_ext2=r"② 当 $m>0$ 时："
           r"$f'(x)=\dfrac{1-m(x+m)}{x+m}=\dfrac{-m\left(x+m-\frac1m\right)}{x+m}$，"
           r"令 $f'(x)=0$ 得 $x=-m+\dfrac1m$，它大于 $-m$，在定义域内。"
           r"当 $x\in\left(-m,-m+\dfrac1m\right)$ 时 $f'(x)>0$，$f(x)$ 单调递增；"
           r"当 $x\in\left(-m+\dfrac1m,+\infty\right)$ 时 $f'(x)<0$，$f(x)$ 单调递减。",
  review=r"注意定义域是 $(-m,+\infty)$ 而非 $(0,+\infty)$——参数 $m$ 同时影响定义域，"
         r"这是本题与前面各题的不同之处。"
         r"原书第 (2) 问为「设 $m>1$，$x_{1}$、$x_{2}$ 为函数 $f(x)$ 的两个零点，"
         r"求证 $x_{1}+x_{2}<0$」，未给出详解，本录不含。"),

# ---------------- T099 反比例型（p69）----------------
dict(topic='M-T-099', key='M-T-099-E1', kind='典例', type='解答',
  stem_text=r"已知函数 $f(x)=2ax+\ln(2-x)$（$a\in\mathbb{R}$）。求 $f(x)$ 的极值。",
  opts=[],
  answer=r"当 $a\leq0$ 时，$f(x)$ 无极值；"
         r"当 $a>0$ 时，$f(x)$ 有极大值 $4a-1-\ln(2a)$，无极小值。",
  solution=r"$f(x)$ 的定义域为 $(-\infty,2)$，$f'(x)=2a-\dfrac1{2-x}$（因 $\dfrac{\mathrm d}{\mathrm dx}\ln(2-x)=-\dfrac1{2-x}$）。",
  solution_ext=r"① 当 $a\leq0$ 时：$2a\leq0$ 且 $-\dfrac1{2-x}<0$，故 $f'(x)<0$，"
           r"$f(x)$ 在 $(-\infty,2)$ 上单调递减，$f(x)$ 无极值。",
  solution_ext2=r"② 当 $a>0$ 时：令 $f'(x)=0$ 得 $2-x=\dfrac1{2a}$，即 $x=2-\dfrac1{2a}$（小于 $2$，在定义域内）。"
           r"当 $x<2-\dfrac1{2a}$ 时 $2-x>\dfrac1{2a}$，故 $\dfrac1{2-x}<2a$，$f'(x)>0$，$f(x)$ 单调递增；"
           r"当 $2-\dfrac1{2a}<x<2$ 时 $f'(x)<0$，$f(x)$ 单调递减。"
           r"故 $f(x)$ 在 $x=2-\dfrac1{2a}$ 处取得极大值，无极小值，"
           r"极大值为 $f\!\left(2-\dfrac1{2a}\right)=2a\left(2-\dfrac1{2a}\right)+\ln\dfrac1{2a}=4a-1-\ln(2a)$。",
  review=r"注意 $\ln(2-x)$ 的导数是 $-\frac1{2-x}$（不是 $+\frac1{2-x}$），"
         r"这是本题最容易出错的一步。数值抽查 $a=0.5,1,2$ 三组，"
         r"极大值实测与公式 $4a-1-\ln(2a)$ 完全相等。"
         r"原书第 (2) 问为「若 $x\leq2-\frac1{\mathrm e}$ 时 $f(x)\leq4a-\frac1{2(2-x)}$ 恒成立，"
         r"求 $a$ 的取值范围」，答案 $\left[\frac{\mathrm e^{2}-2\mathrm e}4,+\infty\right)$，"
         r"但原书未给出详解，本录不含。"),

dict(topic='M-T-099', key='M-T-099-V1', kind='变式9', type='解答',
  stem_text=r"设函数 $f(x)=ax-2-\ln x$（$a\in\mathbb{R}$）。若 $f(x)$ 在点 $\left(\mathrm e,f(\mathrm e)\right)$ "
            r"处的切线为 $x-\mathrm ey+b=0$，求 $a$，$b$ 的值。",
  opts=[],
  answer=r"$a=\dfrac2{\mathrm e}$，$b=-2\mathrm e$。",
  solution=r"$f(x)=ax-2-\ln x$ 的定义域为 $(0,+\infty)$，$f'(x)=a-\dfrac1x$。",
  solution_ext=r"直线 $x-\mathrm ey+b=0$ 即 $y=\dfrac1{\mathrm e}x+\dfrac b{\mathrm e}$，斜率为 $\dfrac1{\mathrm e}$。",
  solution_ext2=r"因为它是 $f(x)$ 在 $x=\mathrm e$ 处的切线，所以 "
           r"$f'(\mathrm e)=a-\dfrac1{\mathrm e}=\dfrac1{\mathrm e}$，解得 $a=\dfrac2{\mathrm e}$。"
           r"于是 $f(\mathrm e)=a\mathrm e-2-\ln\mathrm e=\dfrac2{\mathrm e}\cdot\mathrm e-2-1=-1$，"
           r"切点为 $(\mathrm e,-1)$。把该点代入切线方程："
           r"$\mathrm e-\mathrm e\cdot(-1)+b=0$，解得 $b=-2\mathrm e$。"
           r"故 $a=\dfrac2{\mathrm e}$，$b=-2\mathrm e$。",
  review=r"这是本批唯一一道“已知切线求参数”的题，第 (1) 问本身完整且有详解，可直接录入。"
         r"验证：$a=\frac2{\mathrm e}\approx0.7358$ 时 $f(\mathrm e)=-1.000000$，"
         r"代入切线得 $b=-2\mathrm e\approx-5.4366$。"
         r"原书第 (2) 问为「求 $f(x)$ 的单调区间」，答案“见解析”但未给出详解，本录不含。"),

dict(topic='M-T-099', key='M-T-099-V2', kind='变式10', type='解答',
  stem_text=r"已知 $f(x)=\ln(x+2)-bx+a$，$g(x)=\mathrm e^{x}-1$。讨论 $f(x)$ 的单调性。",
  opts=[],
  answer=r"当 $b\leq0$ 时，$f(x)$ 在 $(-2,+\infty)$ 上单调递增；"
         r"当 $b>0$ 时，$f(x)$ 在 $\left(-2,\dfrac1b-2\right)$ 上单调递增，"
         r"在 $\left(\dfrac1b-2,+\infty\right)$ 上单调递减。",
  solution=r"$f(x)$ 的定义域为 $(-2,+\infty)$，且 $f'(x)=\dfrac1{x+2}-b$。"
           r"（参数 $a$ 是常数项，不影响单调性。）",
  solution_ext=r"① 当 $b\leq0$ 时：$\dfrac1{x+2}>0$ 且 $-b\geq0$，故 $f'(x)>0$，"
           r"$f(x)$ 在定义域 $(-2,+\infty)$ 上单调递增。",
  solution_ext2=r"② 当 $b>0$ 时：令 $f'(x)=0$ 得 $x=\dfrac1b-2$，它大于 $-2$，在定义域内。"
           r"当 $-2<x<\dfrac1b-2$ 时 $x+2<\dfrac1b$，故 $\dfrac1{x+2}>b$，$f'(x)>0$，$f(x)$ 单调递增；"
           r"当 $x>\dfrac1b-2$ 时 $f'(x)<0$，$f(x)$ 单调递减。"
           r"综上即得答案所述两种情形。",
  review=r"注意定义域是 $(-2,+\infty)$，且 $a$ 为常数项、对单调性无影响——"
         r"题干给了 $a$ 和 $g(x)$ 都是为第 (2) 问服务的。"
         r"原书第 (2) 问为「当 $b=0$ 时，对任意 $x\in(-2,+\infty)$ 都有 "
         r"$g(x)\geq\frac{f(x)}{x+2}$ 成立，求实数 $a$ 的最大值」，答案 $-1$，"
         r"但原书未给出详解，本录不含。"),

# ---------------- T100 指数型（p70）----------------
dict(topic='M-T-100', key='M-T-100-E1', kind='典例', type='解答',
  stem_text=r"已知函数 $f(x)=x+a\mathrm e^{-x}$。讨论函数 $f(x)$ 的极值。",
  opts=[],
  answer=r"当 $a\leq0$ 时，函数 $f(x)$ 无极值；"
         r"当 $a>0$ 时，函数 $f(x)$ 的极小值为 $\ln a+1$，无极大值。",
  solution=r"函数 $f(x)=x+a\mathrm e^{-x}$ 的定义域为 $\mathbb{R}$，"
           r"$f'(x)=1-a\mathrm e^{-x}=\dfrac{\mathrm e^{x}-a}{\mathrm e^{x}}$。",
  solution_ext=r"① 当 $a\leq0$ 时：$-a\mathrm e^{-x}\geq0$，故 $f'(x)\geq1>0$，"
           r"$f(x)$ 在 $\mathbb{R}$ 上单调递增，无极值。",
  solution_ext2=r"② 当 $a>0$ 时：令 $f'(x)=0$ 得 $\mathrm e^{x}=a$，即 $x=\ln a$。"
           r"当 $x<\ln a$ 时 $\mathrm e^{x}<a$，故 $f'(x)<0$，$f(x)$ 单调递减；"
           r"当 $x>\ln a$ 时 $f'(x)>0$，$f(x)$ 单调递增。"
           r"所以 $f(x)$ 在 $x=\ln a$ 处取得极小值，"
           r"极小值为 $f(\ln a)=\ln a+a\mathrm e^{-\ln a}=\ln a+a\cdot\dfrac1a=\ln a+1$，无极大值。",
  review=r"函数式的判定（重要）：ref_bank 提取为「$f(x)=\frac{x+a}{\mathrm e^{x}}$」，"
         r"但原书给的导数是 $1-a\mathrm e^{-x}$、极小值是 $\ln a+1$，两者都指向 "
         r"$f(x)=x+a\mathrm e^{-x}$。若按 $\frac{x+a}{\mathrm e^{x}}$，则 "
         r"$f'(x)=\frac{1-x-a}{\mathrm e^{x}}$，$a\leq0$ 时符号不定，"
         r"与原书“当 $a\leq0$ 时 $f'(x)>0$”矛盾。"
         r"数值抽查 $a=0.5,2,5$ 三组，极小值实测与 $\ln a+1$ 完全相等，确认无误。"
         r"原书第 (2) 问为「若函数 $f(x)$ 在 $[0,1]$ 上的最小值是 $\frac43$，求实数 $a$ 的值」，"
         r"答案 $\mathrm e^{\frac13}$，但原书未给出详解，本录不含。"),

dict(topic='M-T-100', key='M-T-100-V1', kind='变式11', type='解答',
  stem_text=r"设函数 $f(x)=x-a\mathrm e^{x}$（$a\in\mathbb{R}$）。求函数 $f(x)$ 的极值。",
  opts=[],
  answer=r"当 $a\leq0$ 时，$f(x)$ 无极值；"
         r"当 $a>0$ 时，$f(x)$ 有极大值 $\ln\dfrac1a-1$（即 $-\ln a-1$），无极小值。",
  solution=r"$f(x)$ 的定义域为 $\mathbb{R}$，$f'(x)=1-a\mathrm e^{x}$。",
  solution_ext=r"① 当 $a\leq0$ 时：$-a\mathrm e^{x}\geq0$，故 $f'(x)\geq1>0$，"
           r"$f(x)$ 在 $\mathbb{R}$ 上单调递增，没有极值。",
  solution_ext2=r"② 当 $a>0$ 时：令 $f'(x)=0$ 得 $\mathrm e^{x}=\dfrac1a$，即 $x=\ln\dfrac1a=-\ln a$。"
           r"当 $x<\ln\frac1a$ 时 $a\mathrm e^{x}<1$，故 $f'(x)>0$，$f(x)$ 单调递增；"
           r"当 $x>\ln\frac1a$ 时 $f'(x)<0$，$f(x)$ 单调递减。"
           r"所以 $f(x)$ 在 $x=\ln\frac1a$ 处取得极大值，"
           r"极大值为 $f\!\left(\ln\dfrac1a\right)=\ln\dfrac1a-a\cdot\dfrac1a=\ln\dfrac1a-1$，没有极小值。",
  review=r"与 T100-E1 对照：一个是 $x+a\mathrm e^{-x}$（极小值），一个是 $x-a\mathrm e^{x}$（极大值），"
         r"指数项的符号与正负决定了极值是极大还是极小。"
         r"数值抽查 $a=0.5,2$ 两组，极大值实测与 $\ln\frac1a-1$ 完全相等。"
         r"原书第 (2) 问为「若 $f(x)\leq ax$ 在 $x\in[0,+\infty)$ 时恒成立，求 $a$ 的取值范围」，"
         r"答案 $\left[\frac1{1+\mathrm e},+\infty\right)$，但原书未给出详解，本录不含。"),

dict(topic='M-T-100', key='M-T-100-V2', kind='变式12', type='解答',
  stem_text=r"设函数 $f(x)=a\mathrm e^{x}+2x+ab+4$（$a,b\in\mathbb{R}$）。求函数 $f(x)$ 的单调区间。",
  opts=[],
  answer=r"当 $a\geq0$ 时，$f(x)$ 的单调递增区间为 $\mathbb{R}$，无单调递减区间；"
         r"当 $a<0$ 时，$f(x)$ 的单调递增区间为 $\left(-\infty,\ln\left(-\dfrac2a\right)\right)$，"
         r"单调递减区间为 $\left(\ln\left(-\dfrac2a\right),+\infty\right)$。",
  solution=r"$f(x)$ 的定义域为 $\mathbb{R}$，$f'(x)=a\mathrm e^{x}+2$。"
           r"（$ab+4$ 是常数项，不影响单调性。）",
  solution_ext=r"① 当 $a\geq0$ 时：$a\mathrm e^{x}\geq0$，故 $f'(x)\geq2>0$，"
           r"$f(x)$ 的单调递增区间为 $\mathbb{R}$，无单调递减区间。",
  solution_ext2=r"② 当 $a<0$ 时：令 $f'(x)=0$ 得 $\mathrm e^{x}=-\dfrac2a$（因 $a<0$，右端为正），"
           r"即 $x=\ln\left(-\dfrac2a\right)$。"
           r"令 $f'(x)>0$ 得 $\mathrm e^{x}<-\dfrac2a$，即 $x<\ln\left(-\dfrac2a\right)$；"
           r"令 $f'(x)<0$ 得 $x>\ln\left(-\dfrac2a\right)$。"
           r"故 $f(x)$ 的单调递增区间为 $\left(-\infty,\ln\left(-\dfrac2a\right)\right)$，"
           r"单调递减区间为 $\left(\ln\left(-\dfrac2a\right),+\infty\right)$。",
  review=r"注意 $a<0$ 时 $-\frac2a>0$，对数才有意义；这也是 $a\geq0$ 与 $a<0$ 的分界原因。"
         r"数值抽查 $a=-1,-2,-0.5$ 三组，符号全部吻合。"
         r"原书第 (2) 问为「若函数 $y=f(x)-ab$ 有两个不同的零点 $x_{1}$、$x_{2}$（$x_{1}<x_{2}$），"
         r"求证 $f'\left(x_{1}\right)f'\left(x_{2}\right)>-1$」，未给出详解，本录不含。"),
]

if __name__ == '__main__':
    print('共 %d 题' % len(QS))
