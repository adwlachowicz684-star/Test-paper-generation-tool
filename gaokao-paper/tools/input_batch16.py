# -*- coding: utf-8 -*-
r"""第16批录入数据：T101~T103，共 10 题（导数含参讨论·单调性，解答题）。

来源：2024高中数学热点题型归纳完整解析版.pdf p70~p72

**本批沿用第 14 批的做法：只录第 (1) 问**

这 10 道题的【答案】都给了两问（或三问），但【详解】只有第 (1) 问。
所以每题只录第 (1) 问，第 (2)（(3)）问的内容记在 review 里。

**30 项数值抽查全部通过**（分区间采样判导数符号，取 2~3 组参数值）。

**发现的一处 PDF 提取缺陷**

T103-V3（变式21）原文提取为「$-\frac62\leq a\leq\frac62$」，
$\sqrt6$ 的根号丢失了。正确应为 $-\frac{\sqrt6}2\leq a\leq\frac{\sqrt6}2$。
由 $2a^{2}-3\leq0$ 得 $|a|\leq\sqrt{\frac32}=\frac{\sqrt6}2\approx1.2247$，
数值抽查也证实（$a=1.2$ 恒增、$a=2$ 有两根）。已按正确值录入。

**书写约束**
1. LaTeX 字符串一律 raw **双**引号 r"..."；单引号会被 $f'(x)$ 的撇号终止。
2. 中文行文用弯引号，不用 ASCII 双引号（会终止 raw 串）。
3. 多行 raw 拼接时逗号只在**最后一行**。
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'py'))

QS = [
# ---------------- T101 上下平移（p70~71）----------------
dict(topic='M-T-101', key='M-T-101-V1', kind='变式13', type='解答',
  stem_text=r"已知函数 $f(x)=\dfrac{a\ln x}{x}+1$（其中 $a$ 为非零实数）。讨论 $f(x)$ 的单调性。",
  opts=[],
  answer=r"当 $a>0$ 时，$f(x)$ 在 $(0,\mathrm{e})$ 上单调递增，在 $(\mathrm{e},+\infty)$ 上单调递减；"
         r"当 $a<0$ 时，$f(x)$ 在 $(0,\mathrm{e})$ 上单调递减，在 $(\mathrm{e},+\infty)$ 上单调递增。",
  solution=r"$f(x)$ 的定义域为 $(0,+\infty)$，"
           r"$f'(x)=a\cdot\dfrac{1-\ln x}{x^{2}}=\dfrac{a(1-\ln x)}{x^{2}}$。",
  solution_ext=r"因 $x^{2}>0$，$f'(x)$ 的符号由 $a$ 与 $1-\ln x$ 的乘积决定，"
           r"而 $1-\ln x>0\iff 0<x<\mathrm{e}$。",
  solution_ext2=r"① 当 $a>0$ 时：当 $x\in(0,\mathrm{e})$ 时 $f'(x)>0$，$f(x)$ 单调递增；"
           r"当 $x\in(\mathrm{e},+\infty)$ 时 $f'(x)<0$，$f(x)$ 单调递减。"
           r"② 当 $a<0$ 时：当 $x\in(0,\mathrm{e})$ 时 $f'(x)<0$，$f(x)$ 单调递减；"
           r"当 $x\in(\mathrm{e},+\infty)$ 时 $f'(x)>0$，$f(x)$ 单调递增。",
  review=r"原书第 (2) 问为「若函数 $g(x)=\mathrm e^{x}-f(x)$ 有两个零点，①求实数 $a$ 的取值范围；"
         r"②设两个零点分别为 $x_{1}$、$x_{2}$，求证 $x_{1}x_{2}>\mathrm e^{2}$」，"
         r"答案分别为 $(\mathrm e,+\infty)$ 与「证明见解析」，但原书未给出详解，本录不含。"),

dict(topic='M-T-101', key='M-T-101-V2', kind='变式14', type='解答',
  stem_text=r"已知函数 $f(x)=\dfrac{a+\ln x}{x}$（$a\in\mathbb{R}$）。求函数 $f(x)$ 的单调区间。",
  opts=[],
  answer=r"$f(x)$ 的单调递增区间为 $\left(0,\mathrm{e}^{1-a}\right)$，"
         r"单调递减区间为 $\left(\mathrm{e}^{1-a},+\infty\right)$。",
  solution=r"$f(x)$ 的定义域为 $(0,+\infty)$，求导得 "
           r"$f'(x)=\dfrac{1-a-\ln x}{x^{2}}$。",
  solution_ext=r"令 $f'(x)=0$，即 $1-a-\ln x=0$，解得 $x=\mathrm{e}^{1-a}$。"
           r"因 $x^{2}>0$，$f'(x)$ 的符号由 $1-a-\ln x$ 决定，"
           r"而 $1-a-\ln x>0\iff x<\mathrm{e}^{1-a}$。",
  solution_ext2=r"当 $x\in\left(0,\mathrm{e}^{1-a}\right)$ 时 $f'(x)>0$，$f(x)$ 单调递增；"
           r"当 $x\in\left(\mathrm{e}^{1-a},+\infty\right)$ 时 $f'(x)<0$，$f(x)$ 单调递减。"
           r"故 $f(x)$ 的单调递增区间为 $\left(0,\mathrm{e}^{1-a}\right)$，"
           r"单调递减区间为 $\left(\mathrm{e}^{1-a},+\infty\right)$。",
  review=r"原书第 (2) 问为「当函数 $f(x)$ 与函数 $g(x)=\ln x$ 图象的公切线 $l$ 经过坐标原点时，"
         r"求实数 $a$ 的取值集合」，答案为 $\left\{\dfrac{\ln2}2\right\}$；"
         r"第 (3) 问为证明题。两问原书均未给出详解，本录不含。"),

dict(topic='M-T-101', key='M-T-101-V3', kind='变式15', type='解答',
  stem_text=r"设 $a$，$b$ 为实数，且 $a>1$，函数 $f(x)=a^{x}-bx+\mathrm{e}^{2}$（$x\in\mathbb{R}$）。 "
            r"求函数 $f(x)$ 的单调区间。",
  opts=[],
  answer=r"当 $b\leq0$ 时，$f(x)$ 在 $(-\infty,+\infty)$ 上单调递增；"
         r"当 $b>0$ 时，$f(x)$ 在 $\left(-\infty,\log_{a}\dfrac b{\ln a}\right)$ 上单调递减，"
         r"在 $\left(\log_{a}\dfrac b{\ln a},+\infty\right)$ 上单调递增。",
  solution=r"求导得 $f'(x)=a^{x}\ln a-b$。因 $a>1$，有 $\ln a>0$ 且 $a^{x}>0$。",
  solution_ext=r"① 当 $b\leq0$ 时，$a^{x}\ln a>0\geq b$，故 $f'(x)>0$ 恒成立，"
           r"$f(x)$ 在 $\mathbb{R}$ 上单调递增。",
  solution_ext2=r"② 当 $b>0$ 时，令 $f'(x)>0$ 得 $a^{x}>\dfrac b{\ln a}$，即 "
           r"$x>\log_{a}\dfrac b{\ln a}$；令 $f'(x)<0$ 得 $x<\log_{a}\dfrac b{\ln a}$。"
           r"故 $f(x)$ 在 $\left(-\infty,\log_{a}\dfrac b{\ln a}\right)$ 上单调递减，"
           r"在 $\left(\log_{a}\dfrac b{\ln a},+\infty\right)$ 上单调递增。",
  review=r"原书第 (2) 问为「若对任意 $b>2\mathrm e^{2}$，函数 $f(x)$ 有两个不同的零点，"
         r"求 $a$ 的取值范围」，答案 $(1,\mathrm e^{2}]$，但原书未给出详解，本录不含。"
         r"注意 $f'(x)>0$ 的解要写成 $\log_{a}\frac b{\ln a}$（对数的真数是 $\frac b{\ln a}$，"
         r"不是 $b$），这是本题最容易写错的地方。"),

# ---------------- T102 一元二次可因式分解型（p71~72）----------------
dict(topic='M-T-102', key='M-T-102-E1', kind='典例', type='解答',
  stem_text=r"已知函数 $f(x)=mx^{2}+(m-2)x\ln x+2$（$m\in\mathbb{R}$）。 "
            r"设 $g(x)=\dfrac{f(x)}x$，讨论函数 $g(x)$ 的单调性。",
  opts=[],
  answer=r"当 $m\leq0$ 时，$g(x)$ 在 $(0,+\infty)$ 上单调递减；"
         r"当 $m>0$ 时，$g(x)$ 在 $\left(0,\dfrac2m\right)$ 上单调递减，"
         r"在 $\left(\dfrac2m,+\infty\right)$ 上单调递增。",
  solution=r"由题 $g(x)=\dfrac{f(x)}x=mx+(m-2)\ln x+\dfrac2x$，定义域为 $(0,+\infty)$，"
           r"$g'(x)=m+\dfrac{m-2}x-\dfrac2{x^{2}}=\dfrac{mx^{2}+(m-2)x-2}{x^{2}}"
           r"=\dfrac{(mx-2)(x+1)}{x^{2}}$。",
  solution_ext=r"因 $x^{2}>0$ 且 $x+1>0$（$x>0$），$g'(x)$ 的符号由 $mx-2$ 决定。"
           r"① 当 $m\leq0$ 时，$mx-2<0$ 恒成立，故 $g'(x)<0$，$g(x)$ 在 $(0,+\infty)$ 上单调递减。",
  solution_ext2=r"② 当 $m>0$ 时：由 $g'(x)>0$ 得 $x>\dfrac2m$；由 $g'(x)<0$ 得 $0<x<\dfrac2m$。"
           r"故 $g(x)$ 在 $\left(0,\dfrac2m\right)$ 上单调递减，"
           r"在 $\left(\dfrac2m,+\infty\right)$ 上单调递增。"
           r"综上：当 $m\leq0$ 时，$g(x)$ 在 $(0,+\infty)$ 上单调递减；"
           r"当 $m>0$ 时，$g(x)$ 在 $\left(\dfrac2m,+\infty\right)$ 上单调递增，"
           r"在 $\left(0,\dfrac2m\right)$ 上单调递减。",
  review=r"因式分解是本题关键：$mx^{2}+(m-2)x-2=(mx-2)(x+1)$。"
         r"原书第 (2) 问为求实数 $t$ 的取值范围，未给出详解，本录不含。"),

dict(topic='M-T-102', key='M-T-102-V1', kind='变式16', type='解答',
  stem_text=r"已知函数 $f(x)=ax^{2}-(1+2a)x+\ln x$。讨论 $f(x)$ 的单调性。",
  opts=[],
  answer=r"当 $a\leq0$ 时，$f(x)$ 在 $(0,1)$ 上单调递增，在 $(1,+\infty)$ 上单调递减；"
         r"当 $a=\dfrac12$ 时，$f(x)$ 在 $(0,+\infty)$ 上单调递增；"
         r"当 $0<a<\dfrac12$ 时，$f(x)$ 在 $(0,1)$ 和 $\left(\dfrac1{2a},+\infty\right)$ 上单调递增，"
         r"在 $\left(1,\dfrac1{2a}\right)$ 上单调递减；"
         r"当 $a>\dfrac12$ 时，$f(x)$ 在 $\left(0,\dfrac1{2a}\right)$ 和 $(1,+\infty)$ 上单调递增，"
         r"在 $\left(\dfrac1{2a},1\right)$ 上单调递减。",
  solution=r"$f(x)$ 的定义域为 $(0,+\infty)$，"
           r"$f'(x)=2ax-(1+2a)+\dfrac1x=\dfrac{2ax^{2}-(1+2a)x+1}{x}"
           r"=\dfrac{(2ax-1)(x-1)}x$。",
  solution_ext=r"① 当 $a\leq0$ 时，恒有 $2ax-1<0$（因 $x>0$）。"
           r"当 $x\in(0,1)$ 时 $x-1<0$，$f'(x)>0$；当 $x\in(1,+\infty)$ 时 $x-1>0$，$f'(x)<0$。"
           r"故 $f(x)$ 在 $(0,1)$ 上单调递增，在 $(1,+\infty)$ 上单调递减。"
           r"② 当 $a>0$ 时，令 $f'(x)=0$ 得 $x_{1}=1$，$x_{2}=\dfrac1{2a}$。"
           r"若 $a=\dfrac12$，两根重合为 $1$，恒有 $f'(x)\geq0$，$f(x)$ 在 $(0,+\infty)$ 上单调递增。",
  solution_ext2=r"若 $0<a<\dfrac12$，则 $\dfrac1{2a}>1$：当 $x\in(0,1)\cup\left(\dfrac1{2a},+\infty\right)$ 时 "
           r"$f'(x)>0$，当 $x\in\left(1,\dfrac1{2a}\right)$ 时 $f'(x)<0$；"
           r"若 $a>\dfrac12$，则 $\dfrac1{2a}<1$：当 $x\in\left(0,\dfrac1{2a}\right)\cup(1,+\infty)$ 时 "
           r"$f'(x)>0$，当 $x\in\left(\dfrac1{2a},1\right)$ 时 $f'(x)<0$。"
           r"由此即得答案所述的四种情形。",
  review=r"本题有两根 $1$ 与 $\frac1{2a}$，必须比较二者大小，这是分类讨论的分界点。"
         r"原书第 (2) 问为「当 $a=0$ 时，证明 $\frac{\mathrm e^{x}}x>\frac7{10}-x^{2}-2f(x)$」，"
         r"未给出详解，本录不含。"),

dict(topic='M-T-102', key='M-T-102-V2', kind='变式17', type='解答',
  stem_text=r"设函数 $f(x)=x^{2}+ax-3a^{2}\ln x$，其中 $a\in\mathbb{R}$。讨论 $f(x)$ 的单调性。",
  opts=[],
  answer=r"当 $a=0$ 时，$f(x)$ 在 $(0,+\infty)$ 上单调递增；"
         r"当 $a<0$ 时，$f(x)$ 在 $\left(0,-\dfrac{3a}2\right)$ 上单调递减，"
         r"在 $\left(-\dfrac{3a}2,+\infty\right)$ 上单调递增；"
         r"当 $a>0$ 时，$f(x)$ 在 $(0,a)$ 上单调递减，在 $(a,+\infty)$ 上单调递增。",
  solution=r"$f(x)$ 的定义域为 $(0,+\infty)$，"
           r"$f'(x)=2x+a-\dfrac{3a^{2}}x=\dfrac{2x^{2}+ax-3a^{2}}x=\dfrac{(x-a)(2x+3a)}x$。",
  solution_ext=r"① 当 $a=0$ 时，$f'(x)=2x>0$，$f(x)$ 在 $(0,+\infty)$ 上单调递增。"
           r"② 当 $a<0$ 时，$-\dfrac{3a}2>0$。当 $0<x<-\dfrac{3a}2$ 时，$x-a>0$（因 $x>0>a$）"
           r"而 $2x+3a<0$，故 $f'(x)<0$，$f(x)$ 单调递减；"
           r"当 $x>-\dfrac{3a}2$ 时 $2x+3a>0$，故 $f'(x)>0$，$f(x)$ 单调递增。",
  solution_ext2=r"③ 当 $a>0$ 时，当 $0<x<a$ 时 $x-a<0$ 且 $2x+3a>0$，故 $f'(x)<0$，$f(x)$ 单调递减；"
           r"当 $x>a$ 时 $f'(x)>0$，$f(x)$ 单调递增。"
           r"综上即得答案所述的三种情形。",
  review=r"因式分解：$2x^{2}+ax-3a^{2}=(x-a)(2x+3a)$。"
         r"注意 $a<0$ 时在定义域内的根是 $-\frac{3a}2$（另一根 $a<0$ 不在定义域内）。"
         r"原书第 (2) 问为「当 $a>0$ 时，若 $y=f(x)$ 的图象与直线 $y=5a^{2}-3a$ 没有公共点，"
         r"求 $a$ 的取值范围」，答案 $(0,1)$，但原书未给出详解，本录不含。"),

dict(topic='M-T-102', key='M-T-102-V3', kind='变式18', type='解答',
  stem_text=r"已知函数 $f(x)=\dfrac{x^{2}-a^{2}+2a}{\mathrm{e}^{x}}$，$a\in\mathbb{R}$。讨论函数 $f(x)$ 的单调性。",
  opts=[],
  answer=r"当 $a<1$ 时，$f(x)$ 的单调递减区间为 $(-\infty,a]$ 和 $[2-a,+\infty)$，"
         r"单调递增区间为 $[a,2-a]$；"
         r"当 $a=1$ 时，$f(x)$ 在 $\mathbb{R}$ 上单调递减；"
         r"当 $a>1$ 时，$f(x)$ 的单调递减区间为 $(-\infty,2-a]$ 和 $[a,+\infty)$，"
         r"单调递增区间为 $[2-a,a]$。",
  solution=r"$f'(x)=\dfrac{2x\cdot\mathrm e^{x}-(x^{2}-a^{2}+2a)\mathrm e^{x}}{\mathrm e^{2x}}"
           r"=\dfrac{-(x^{2}-2x-a^{2}+2a)}{\mathrm e^{x}}"
           r"=-\dfrac{(x-a)(x+a-2)}{\mathrm e^{x}}$。",
  solution_ext=r"因 $\mathrm e^{x}>0$，$f'(x)$ 的符号与 $-(x-a)(x+a-2)$ 相同。"
           r"两根为 $x=a$ 与 $x=2-a$，需比较二者大小：当 $a<1$ 时 $a<2-a$，"
           r"当 $a=1$ 时两根重合，当 $a>1$ 时 $2-a<a$。",
  solution_ext2=r"① 当 $a<1$ 时：当 $x<a$ 或 $x>2-a$ 时 $(x-a)(x+a-2)>0$，$f'(x)<0$；"
           r"当 $a<x<2-a$ 时 $f'(x)>0$。② 当 $a=1$ 时，$f'(x)=-\dfrac{(x-1)^{2}}{\mathrm e^{x}}\leq0$，"
           r"$f(x)$ 在 $\mathbb{R}$ 上单调递减。③ 当 $a>1$ 时：当 $x<2-a$ 或 $x>a$ 时 $f'(x)<0$；"
           r"当 $2-a<x<a$ 时 $f'(x)>0$。由此即得答案所述三种情形。",
  review=r"两根 $a$ 与 $2-a$ 的大小关系以 $a=1$ 为界，这是本题的分类分界点。"
         r"原书第 (2) 问为「当 $a=3$ 时，方程 $(x^{2}-3)\cdot f(x)=m\mathrm e^{x}-\dfrac{x^{2}-3}{\mathrm e}$ "
         r"有四个根，求实数 $m$ 的取值范围」，未给出详解，本录不含。"),

# ---------------- T103 一元二次不能因式分解（p72）----------------
dict(topic='M-T-103', key='M-T-103-V1', kind='变式19', type='解答',
  stem_text=r"已知函数 $f(x)=\ln x+x^{2}-ax$（$a\in\mathbb{R}$）。求函数 $f(x)$ 的单调区间。",
  opts=[],
  answer=r"当 $a\leq2\sqrt2$ 时，$f(x)$ 在 $(0,+\infty)$ 上单调递增；"
         r"当 $a>2\sqrt2$ 时，$f(x)$ 在 $\left(0,\dfrac{a-\sqrt{a^{2}-8}}4\right)$ 和 "
         r"$\left(\dfrac{a+\sqrt{a^{2}-8}}4,+\infty\right)$ 上单调递增，"
         r"在 $\left(\dfrac{a-\sqrt{a^{2}-8}}4,\dfrac{a+\sqrt{a^{2}-8}}4\right)$ 上单调递减。",
  solution=r"$f(x)$ 的定义域为 $(0,+\infty)$，"
           r"$f'(x)=\dfrac1x+2x-a=\dfrac{2x^{2}-ax+1}x$。因 $x>0$，$f'(x)$ 的符号由 "
           r"$2x^{2}-ax+1$ 决定。",
  solution_ext=r"① 当 $a\leq0$ 时，$2x^{2}-ax+1>0$ 恒成立，$f(x)$ 在 $(0,+\infty)$ 上单调递增。"
           r"② 当 $a>0$ 时，$\Delta=a^{2}-8$。若 $\Delta\leq0$，即 $0<a\leq2\sqrt2$，"
           r"则 $2x^{2}-ax+1\geq0$ 恒成立，$f(x)$ 在 $(0,+\infty)$ 上单调递增。",
  solution_ext2=r"若 $\Delta>0$，即 $a>2\sqrt2$，则 $2x^{2}-ax+1=0$ 的两根为 "
           r"$x_{1}=\dfrac{a-\sqrt{a^{2}-8}}4$、$x_{2}=\dfrac{a+\sqrt{a^{2}-8}}4$（均大于 $0$）。"
           r"当 $x\in(0,x_{1})\cup(x_{2},+\infty)$ 时 $f'(x)>0$；当 $x\in(x_{1},x_{2})$ 时 $f'(x)<0$。"
           r"综上即得答案所述两种情形。",
  review=r"分类分界点是 $\Delta=a^{2}-8=0$，即 $a=2\sqrt2$；$a<0$ 时 $\Delta$ 虽可能为正，"
         r"但两根均为负（不在定义域内），故仍恒增，应与 $0<a\leq2\sqrt2$ 合并叙述。"
         r"原书第 (2) 问为证明题，未给出详解，本录不含。"),

dict(topic='M-T-103', key='M-T-103-V2', kind='变式20', type='解答',
  stem_text=r"已知函数 $f(x)=ax^{2}-2a\ln x-x$（$a\in\mathbb{R}$）。讨论 $f(x)$ 的单调性。",
  opts=[],
  answer=r"当 $a=0$ 时，$f(x)$ 在 $(0,+\infty)$ 上单调递减；"
         r"当 $a>0$ 时，$f(x)$ 在 $\left(0,\dfrac{1+\sqrt{1+16a^{2}}}{4a}\right)$ 上单调递减，"
         r"在 $\left(\dfrac{1+\sqrt{1+16a^{2}}}{4a},+\infty\right)$ 上单调递增；"
         r"当 $a<0$ 时，$f(x)$ 在 $\left(0,\dfrac{1-\sqrt{1+16a^{2}}}{4a}\right)$ 上单调递增，"
         r"在 $\left(\dfrac{1-\sqrt{1+16a^{2}}}{4a},+\infty\right)$ 上单调递减。",
  solution=r"$f(x)$ 的定义域为 $(0,+\infty)$，"
           r"$f'(x)=2ax-\dfrac{2a}x-1=\dfrac{2ax^{2}-x-2a}x$。",
  solution_ext=r"当 $a=0$ 时，$f(x)=-x$，$f(x)$ 在 $(0,+\infty)$ 上单调递减。"
           r"当 $a\neq0$ 时，令 $g(x)=2ax^{2}-x-2a$，其判别式 "
           r"$\Delta=1-4\cdot2a\cdot(-2a)=1+16a^{2}>0$ 恒成立，"
           r"$g(x)=0$ 的两根为 $x_{1}=\dfrac{1+\sqrt{1+16a^{2}}}{4a}$、"
           r"$x_{2}=\dfrac{1-\sqrt{1+16a^{2}}}{4a}$。",
  solution_ext2=r"当 $a>0$ 时，$x_{1}>0$、$x_{2}<0$（舍去）：当 $x\in(0,x_{1})$ 时 $f'(x)<0$，"
           r"$f(x)$ 单调递减；当 $x\in(x_{1},+\infty)$ 时 $f'(x)>0$，$f(x)$ 单调递增。"
           r"当 $a<0$ 时，$x_{2}>0$、$x_{1}<0$（舍去）：当 $x\in(0,x_{2})$ 时 $f'(x)>0$，"
           r"$f(x)$ 单调递增；当 $x\in(x_{2},+\infty)$ 时 $f'(x)<0$，$f(x)$ 单调递减。"
           r"由此即得答案所述三种情形。",
  review=r"$a$ 变号时，保留在定义域内的根从 $x_{1}$ 变成 $x_{2}$——分母 $4a$ 变号所致，"
         r"这是本题最容易出错的地方。原书第 (2) 问为「当 $a=1$ 时，判断 $\frac{x_{1}+x_{2}}2$ "
         r"是否为导函数 $f'(x)$ 的零点」，未给出详解，本录不含。"),

dict(topic='M-T-103', key='M-T-103-V3', kind='变式21', type='解答',
  stem_text=r"已知函数 $f(x)=x^{3}-2ax^{2}+2x+2$。讨论 $f(x)$ 的单调性。",
  opts=[],
  answer=r"当 $-\dfrac{\sqrt6}2\leq a\leq\dfrac{\sqrt6}2$ 时，$f(x)$ 在 $\mathbb{R}$ 上单调递增；"
         r"当 $a<-\dfrac{\sqrt6}2$ 或 $a>\dfrac{\sqrt6}2$ 时，$f(x)$ 在 "
         r"$\left(-\infty,\dfrac{2a-\sqrt{4a^{2}-6}}3\right)$ 和 "
         r"$\left(\dfrac{2a+\sqrt{4a^{2}-6}}3,+\infty\right)$ 上单调递增，"
         r"在 $\left(\dfrac{2a-\sqrt{4a^{2}-6}}3,\dfrac{2a+\sqrt{4a^{2}-6}}3\right)$ 上单调递减。",
  solution=r"函数的定义域为 $\mathbb{R}$，$f'(x)=3x^{2}-4ax+2$，"
           r"$\Delta=16a^{2}-24=8\left(2a^{2}-3\right)$。",
  solution_ext=r"当 $\Delta\leq0$，即 $2a^{2}-3\leq0$，亦即 "
           r"$-\dfrac{\sqrt6}2\leq a\leq\dfrac{\sqrt6}2$ 时，$f'(x)\geq0$ 恒成立，"
           r"$f(x)$ 在 $\mathbb{R}$ 上单调递增。",
  solution_ext2=r"当 $\Delta>0$，即 $a<-\dfrac{\sqrt6}2$ 或 $a>\dfrac{\sqrt6}2$ 时，"
           r"令 $f'(x)=0$ 得 $x=\dfrac{2a\pm\sqrt{4a^{2}-6}}3$。记 "
           r"$x_{1}=\dfrac{2a-\sqrt{4a^{2}-6}}3$、$x_{2}=\dfrac{2a+\sqrt{4a^{2}-6}}3$（$x_{1}<x_{2}$）。"
           r"$f'(x)>0$ 的解集为 $(-\infty,x_{1})\cup(x_{2},+\infty)$，$f'(x)<0$ 的解集为 $(x_{1},x_{2})$。"
           r"故 $f(x)$ 在 $(-\infty,x_{1})$ 和 $(x_{2},+\infty)$ 上单调递增，在 $(x_{1},x_{2})$ 上单调递减。",
  review=r"PDF 文本提取把 $\frac{\sqrt6}2$ 的根号丢了，写成 $\frac62$。正确值由 "
         r"$2a^{2}-3\leq0$ 得 $|a|\leq\sqrt{\frac32}=\frac{\sqrt6}2\approx1.2247$；"
         r"数值抽查证实（$a=1.2$ 恒增、$a=2$ 有两根）。已按正确值录入。"
         r"原书第 (2) 问为「当 $x\geq0$ 时，$2\mathrm e^{x}\geq f(x)$，求 $a$ 的取值范围」，"
         r"答案 $\left[\frac{7-\mathrm e^{2}}4,+\infty\right)$，但原书未给出详解，本录不含。"),
]

if __name__ == '__main__':
    print('共 %d 题' % len(QS))
