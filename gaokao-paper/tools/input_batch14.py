# -*- coding: utf-8 -*-
r"""第14批录入数据：T096~T097，共 7 题（导函数含参讨论·分类讨论单调性）。

来源：2024高中数学热点题型归纳完整解析版.pdf p67~p69

**本批的特殊处理：只录第 (1) 问**

教辅在专题 3-2 开头明确写了：

> 本专题围绕研究的是讨论点的寻找和训练，故所选大题，解析答案处
> 大多数把第二问暂时去掉。

核过原文，这 7 道题的【详解】确实**都只有第 (1) 问**，第 (2) 问只有【答案】
和【分析】、没有推导过程。

所以本批每题只录第 (1) 问，做法是：
- 题干 = 原函数定义 + 第 (1) 问（**不写第 (2) 问**，避免"有问无解"）
- 答案 = 第 (1) 问的答案（分类结论，是文本不是单个数值）
- 解析 = 原文【分析】+【详解】合并
- review 注明"原书第 (2) 问无详解，本录只含第 (1) 问"

第 (1) 问本身是完整的独立题（给定含参函数、讨论单调性），拆出来成立。

**原题对应关系（PDF 变式编号 ≠ ref_bank 的 VN 编号）**
- M-T-096-E1 ← 例1   (p67)
- M-T-096-V1 ← 变式1 (p67)
- M-T-096-V2 ← 变式2 (p67)
- M-T-097-E1 ← 例1   (p67)  题型二
- M-T-097-V1 ← 变式3 (p67-68)
- M-T-097-V2 ← 变式4 (p68)
- M-T-097-V3 ← 变式5 (p68)

**书写约束（真踩过的坑）**
1. LaTeX 字符串一律 raw **双**引号 `r"..."`；单引号会被 $f'(x)$ 的撇号终止。
2. 中文行文用弯引号“”，不用 ASCII 双引号（会终止 r"..." 串）。
3. 多行 raw 拼接时逗号只在**最后一行**。

**7 题第一问结论全部独立验算过**（求导 → 判零点是否在定义域内 → 分段定号）。
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'py'))

QS = [
# ---------------- T096 参数在常数位置（单参）(p67) ----------------
dict(topic='M-T-096', key='M-T-096-E1', kind='典例', type='解答',
  stem_text=r"已知函数 $f(x)=a\ln x+x-1$（$a\in\mathbb{R}$）。讨论 $f(x)$ 的单调性。",
  opts=[],
  answer=r"当 $a\geq0$ 时，$f(x)$ 在 $(0,+\infty)$ 上单调递增，无单调递减区间；"
         r"当 $a<0$ 时，$f(x)$ 在 $(0,-a)$ 上单调递减，在 $(-a,+\infty)$ 上单调递增。",
  solution=r"$f(x)$ 的定义域为 $(0,+\infty)$，$f'(x)=\dfrac ax+1=\dfrac{x+a}{x}$。",
  solution_ext=r"① 当 $a\geq0$ 时，$x+a>0$ 且 $x>0$，故 $f'(x)>0$，"
           r"$f(x)$ 在 $(0,+\infty)$ 上单调递增。",
  solution_ext2=r"② 当 $a<0$ 时，令 $f'(x)=0$ 得 $x=-a$（在定义域内）。"
           r"当 $x\in(0,-a)$ 时 $x+a<0$，$f'(x)<0$，$f(x)$ 单调递减；"
           r"当 $x\in(-a,+\infty)$ 时 $x+a>0$，$f'(x)>0$，$f(x)$ 单调递增。"
           r"综上：当 $a\geq0$ 时，$f(x)$ 的单调递增区间为 $(0,+\infty)$，无单调递减区间；"
           r"当 $a<0$ 时，$f(x)$ 的单调递减区间为 $(0,-a)$，单调递增区间为 $(-a,+\infty)$。",
  review=r"原书第 (2) 问为「若函数 $y=f(\mathrm e^{x})-ax+1$ 与 $y=\mathrm e^{a}(\ln x+a)$ 的图象有两个"
         r"不同的公共点，求 $a$ 的取值范围」，答案 $(1,+\infty)$，但原书未给出详解，本录不含。"),

dict(topic='M-T-096', key='M-T-096-V1', kind='变式1', type='解答',
  stem_text=r"已知函数 $f(x)=\ln x+\dfrac ax$，$g(x)=\mathrm e^{x}+\sin x$，其中 $a\in\mathbb{R}$。 "
            r"试讨论函数 $f(x)$ 的单调性。",
  opts=[],
  answer=r"当 $a\leq0$ 时，$f(x)$ 在 $(0,+\infty)$ 上单调递增，无减区间；"
         r"当 $a>0$ 时，$f(x)$ 在 $(0,a)$ 上单调递减，在 $(a,+\infty)$ 上单调递增。",
  solution=r"$f(x)=\ln x+\dfrac ax$ 的定义域为 $(0,+\infty)$，"
           r"$f'(x)=\dfrac1x-\dfrac a{x^{2}}=\dfrac{x-a}{x^{2}}$。因 $x^{2}>0$，$f'(x)$ 的符号由 $x-a$ 决定。",
  solution_ext=r"① 当 $a\leq0$ 时，对一切 $x>0$ 有 $x-a>0$，故 $f'(x)>0$，"
           r"$f(x)$ 在 $(0,+\infty)$ 上单调递增。",
  solution_ext2=r"② 当 $a>0$ 时：令 $f'(x)>0$ 得 $x>a$；令 $f'(x)<0$ 得 $0<x<a$。"
           r"故 $f(x)$ 在 $(0,a)$ 上单调递减，在 $(a,+\infty)$ 上单调递增。"
           r"综上：当 $a\leq0$ 时，$f(x)$ 在 $(0,+\infty)$ 上单调递增，无减区间；"
           r"当 $a>0$ 时，$f(x)$ 在 $(0,a)$ 上单调递减，在 $(a,+\infty)$ 上单调递增。",
  review=r"题干中 $g(x)=\mathrm e^{x}+\sin x$ 是原书第 (2) 问用的函数，第 (1) 问用不到，"
         r"为保持题干完整而保留。原书第 (2) 问为「若 $a=1$，证明 $f(x)<\dfrac{g(x)}x$」，"
         r"未给出详解，本录不含。"),

dict(topic='M-T-096', key='M-T-096-V2', kind='变式2', type='解答',
  stem_text=r"已知函数 $f(x)=(2x-a)\mathrm e^{x}$。求 $f(x)$ 的单调区间。",
  opts=[],
  answer=r"$f(x)$ 的单调递减区间为 $\left(-\infty,\dfrac{a-2}2\right)$，"
         r"单调递增区间为 $\left(\dfrac{a-2}2,+\infty\right)$。",
  solution=r"$f(x)$ 的定义域为 $\mathbb{R}$，"
           r"$f'(x)=2\mathrm e^{x}+(2x-a)\mathrm e^{x}=(2x+2-a)\mathrm e^{x}$。",
  solution_ext=r"因 $\mathrm e^{x}>0$ 恒成立，$f'(x)$ 的符号由 $2x+2-a$ 决定。"
           r"令 $f'(x)=0$ 得 $x=\dfrac{a-2}2$。",
  solution_ext2=r"当 $x\in\left(-\infty,\dfrac{a-2}2\right)$ 时 $2x+2-a<0$，$f'(x)<0$，$f(x)$ 单调递减；"
           r"当 $x\in\left(\dfrac{a-2}2,+\infty\right)$ 时 $2x+2-a>0$，$f'(x)>0$，$f(x)$ 单调递增。"
           r"故 $f(x)$ 的单调递减区间为 $\left(-\infty,\dfrac{a-2}2\right)$，"
           r"单调递增区间为 $\left(\dfrac{a-2}2,+\infty\right)$。",
  review=r"原书第 (2) 问为「若 $f(x)$ 的极值点为 $-\dfrac12$，且 $f(m)=f(n)$（$m\neq n$），"
         r"证明 $-\dfrac3{\mathrm e}<f(m+n)<0$」，未给出详解，本录不含。"),

# ---------------- T097 参数在系数位置（单参）(p67~68) ----------------
dict(topic='M-T-097', key='M-T-097-E1', kind='典例', type='解答',
  stem_text=r"已知函数 $f(x)=2\ln x+a(x+a)$。讨论 $f(x)$ 的单调性。",
  opts=[],
  answer=r"当 $a\geq0$ 时，$f(x)$ 在 $(0,+\infty)$ 上单调递增；"
         r"当 $a<0$ 时，$f(x)$ 在 $\left(0,-\dfrac2a\right)$ 上单调递增，"
         r"在 $\left(-\dfrac2a,+\infty\right)$ 上单调递减。",
  solution=r"$f(x)$ 的定义域为 $(0,+\infty)$，$f(x)=2\ln x+ax+a^{2}$，"
           r"$f'(x)=\dfrac2x+a=\dfrac{ax+2}{x}$。",
  solution_ext=r"① 当 $a\geq0$ 时，$ax+2>0$，故 $f'(x)>0$，$f(x)$ 在 $(0,+\infty)$ 上单调递增。",
  solution_ext2=r"② 当 $a<0$ 时，令 $f'(x)=0$ 得 $x=-\dfrac2a>0$（在定义域内）。"
           r"当 $x\in\left(0,-\dfrac2a\right)$ 时 $ax+2>0$，$f'(x)>0$，$f(x)$ 单调递增；"
           r"当 $x\in\left(-\dfrac2a,+\infty\right)$ 时 $ax+2<0$，$f'(x)<0$，$f(x)$ 单调递减。"
           r"综上：当 $a\geq0$ 时，$f(x)$ 在 $(0,+\infty)$ 上为单调递增函数；"
           r"当 $a<0$ 时，$f(x)$ 在 $\left(0,-\dfrac2a\right)$ 上单调递增，"
           r"在 $\left(-\dfrac2a,+\infty\right)$ 上单调递减。",
  review=r"原书第 (2) 问为「若 $x_{1},x_{2}$（$x_{1}<x_{2}$）是 $g(x)=f(x)+x^{2}+ax$ 的两个极值点，"
         r"证明 $g(x_{2})>x_{1}$」，未给出详解，本录不含。"
         r"注意由 $g(x)=2\ln x+(x+a)^{2}$ 可反推 $f(x)=2\ln x+ax+a^{2}$，即 $2\ln x+a(x+a)$。"),

dict(topic='M-T-097', key='M-T-097-V1', kind='变式3', type='解答',
  stem_text=r"已知函数 $f(x)=a\ln x+\dfrac1x+4$，其中 $a\in\mathbb{R}$。讨论函数 $f(x)$ 的单调性。",
  opts=[],
  answer=r"当 $a\leq0$ 时，$f(x)$ 在 $(0,+\infty)$ 上单调递减；"
         r"当 $a>0$ 时，$f(x)$ 在 $\left(0,\dfrac1a\right)$ 上单调递减，"
         r"在 $\left(\dfrac1a,+\infty\right)$ 上单调递增。",
  solution=r"$f(x)$ 的定义域为 $(0,+\infty)$，"
           r"$f'(x)=\dfrac ax-\dfrac1{x^{2}}=\dfrac{ax-1}{x^{2}}$。因 $x^{2}>0$，$f'(x)$ 的符号由 $ax-1$ 决定。",
  solution_ext=r"① 当 $a\leq0$ 时，对一切 $x>0$ 有 $ax-1<0$，故 $f'(x)<0$，"
           r"$f(x)$ 在 $(0,+\infty)$ 上单调递减。",
  solution_ext2=r"② 当 $a>0$ 时：由 $f'(x)>0$ 得 $x>\dfrac1a$；由 $f'(x)<0$ 得 $0<x<\dfrac1a$。"
           r"故 $f(x)$ 在 $\left(0,\dfrac1a\right)$ 上单调递减，在 $\left(\dfrac1a,+\infty\right)$ 上单调递增。"
           r"综上：当 $a\leq0$ 时，$f(x)$ 在 $(0,+\infty)$ 上单调递减；"
           r"当 $a>0$ 时，$f(x)$ 在 $\left(0,\dfrac1a\right)$ 上单调递减，"
           r"在 $\left(\dfrac1a,+\infty\right)$ 上单调递增。",
  review=r"原书第 (2) 问为「对任意 $x\in[1,\mathrm e]$，不等式 $f(x)\geq\dfrac1x+\dfrac{x+1}2$ 恒成立，"
         r"求实数 $a$ 的取值范围」，答案 $\left[\dfrac{\mathrm e+1}2-4,+\infty\right)$，"
         r"但原书未给出详解，本录不含。"),

dict(topic='M-T-097', key='M-T-097-V2', kind='变式4', type='解答',
  stem_text=r"已知函数 $f(x)=x\mathrm e^{mx}$（其中 $\mathrm e$ 为自然对数的底数）。讨论函数 $f(x)$ 的单调性。",
  opts=[],
  answer=r"当 $m=0$ 时，$f(x)$ 在 $\mathbb{R}$ 上单调递增；"
         r"当 $m>0$ 时，$f(x)$ 在 $\left(-\infty,-\dfrac1m\right)$ 上单调递减，"
         r"在 $\left(-\dfrac1m,+\infty\right)$ 上单调递增；"
         r"当 $m<0$ 时，$f(x)$ 在 $\left(-\infty,-\dfrac1m\right)$ 上单调递增，"
         r"在 $\left(-\dfrac1m,+\infty\right)$ 上单调递减。",
  solution=r"$f'(x)=\mathrm e^{mx}+x\cdot m\mathrm e^{mx}=(mx+1)\mathrm e^{mx}$。"
           r"因 $\mathrm e^{mx}>0$，$f'(x)$ 的符号由 $mx+1$ 决定。",
  solution_ext=r"① 当 $m=0$ 时，$f'(x)=\mathrm e^{0}=1>0$，$f(x)$ 在 $\mathbb{R}$ 上单调递增。"
           r"② 当 $m>0$ 时，令 $f'(x)=0$ 得 $x=-\dfrac1m$。"
           r"$x\in\left(-\infty,-\dfrac1m\right)$ 时 $mx+1<0$，$f'(x)<0$，$f(x)$ 单调递减；"
           r"$x\in\left(-\dfrac1m,+\infty\right)$ 时 $mx+1>0$，$f'(x)>0$，$f(x)$ 单调递增。",
  solution_ext2=r"③ 当 $m<0$ 时，令 $f'(x)=0$ 得 $x=-\dfrac1m$（注意此时 $-\dfrac1m>0$）。"
           r"$x\in\left(-\infty,-\dfrac1m\right)$ 时 $mx+1>0$，$f'(x)>0$，$f(x)$ 单调递增；"
           r"$x\in\left(-\dfrac1m,+\infty\right)$ 时 $mx+1<0$，$f'(x)<0$，$f(x)$ 单调递减。"
           r"综上：当 $m=0$ 时，$f(x)$ 在 $\mathbb{R}$ 上单调递增；"
           r"当 $m>0$ 时，$f(x)$ 在 $\left(-\infty,-\dfrac1m\right)$ 上单调递减、"
           r"在 $\left(-\dfrac1m,+\infty\right)$ 上单调递增；"
           r"当 $m<0$ 时，$f(x)$ 在 $\left(-\infty,-\dfrac1m\right)$ 上单调递增、"
           r"在 $\left(-\dfrac1m,+\infty\right)$ 上单调递减。",
  review=r"原书第 (2) 问为「当 $m=1$ 时，若 $f(x)\geq\ln x+ax+1$ 恒成立，求实数 $a$ 的取值范围」，"
         r"答案 $(-\infty,1]$，但原书未给出详解，本录不含。"),

dict(topic='M-T-097', key='M-T-097-V3', kind='变式5', type='解答',
  stem_text=r"已知函数 $f(x)=\dfrac{\mathrm e^{ax}}x$，$g(x)=\ln x+2x+\dfrac1x$，其中 $a\in\mathbb{R}$。 "
            r"试讨论函数 $f(x)$ 的单调性。",
  opts=[],
  answer=r"当 $a>0$ 时，$f(x)$ 在 $\left(\dfrac1a,+\infty\right)$ 上单调递增，"
         r"在 $(-\infty,0)$ 和 $\left(0,\dfrac1a\right)$ 上单调递减；"
         r"当 $a=0$ 时，$f(x)$ 在 $(-\infty,0)$ 和 $(0,+\infty)$ 上单调递减；"
         r"当 $a<0$ 时，$f(x)$ 在 $\left(-\infty,\dfrac1a\right)$ 上单调递增，"
         r"在 $\left(\dfrac1a,0\right)$ 和 $(0,+\infty)$ 上单调递减。",
  solution=r"$f(x)$ 的定义域为 $(-\infty,0)\cup(0,+\infty)$，"
           r"$f'(x)=\dfrac{a\mathrm e^{ax}\cdot x-\mathrm e^{ax}\cdot1}{x^{2}}"
           r"=\dfrac{\mathrm e^{ax}(ax-1)}{x^{2}}$。"
           r"因 $\mathrm e^{ax}>0$ 且 $x^{2}>0$（$x\neq0$），$f'(x)$ 的符号由 $ax-1$ 决定。",
  solution_ext=r"① 当 $a>0$ 时，$\dfrac1a>0$：由 $f'(x)>0$ 得 $x>\dfrac1a$；"
           r"由 $f'(x)<0$ 得 $x<0$ 或 $0<x<\dfrac1a$。"
           r"故 $f(x)$ 在 $\left(\dfrac1a,+\infty\right)$ 上单调递增，"
           r"在 $(-\infty,0)$ 和 $\left(0,\dfrac1a\right)$ 上单调递减。",
  solution_ext2=r"② 当 $a=0$ 时，$f(x)=\dfrac1x$，$f(x)$ 在 $(-\infty,0)$ 和 $(0,+\infty)$ 上单调递减。"
           r"③ 当 $a<0$ 时，$\dfrac1a<0$：由 $f'(x)>0$ 得 $x<\dfrac1a$；"
           r"由 $f'(x)<0$ 得 $\dfrac1a<x<0$ 或 $x>0$。"
           r"故 $f(x)$ 在 $\left(-\infty,\dfrac1a\right)$ 上单调递增，"
           r"在 $\left(\dfrac1a,0\right)$ 和 $(0,+\infty)$ 上单调递减。"
           r"综上即得答案所述的三种情形。",
  review=r"定义域不含 $x=0$，讨论时必须把 $(-\infty,0)$ 与 $(0,+\infty)$ 分开，"
         r"这是本题最容易漏分的地方。"
         r"原书第 (2) 问为「若 $a=2$，证明 $xf(x)\geq g(x)$」，未给出详解，本录不含。"),
]

if __name__ == '__main__':
    print('共 %d 题' % len(QS))
