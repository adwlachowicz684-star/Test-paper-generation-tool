# -*- coding: utf-8 -*-
r"""第6批录入数据：T023 超难压轴小题(不等式收官) / T066 一元二次复合型基础(函数与导数开局)，共 8 题。

来源：2024高中数学热点题型归纳完整解析版.pdf p237 / p40
      —— 基于 ref_bank 提取文本逐题重建，8 题答案全部独立验算通过。

**LaTeX 相关字符串一律 raw 前缀**：'\v'、'\b'、'\n' 在普通字符串里是
转义字符，会把题目污染成控制字符且完全看不出原因（已踩三次）。

本批发现的问题：
  T023-E1  教辅答案 (0, √6/6] 下界错误，正确为 (2/5, √6/6]
  T066-V2  提取时指数符号丢失（原为 (1/2)^{|x-1|}+1），
           按分段函数值域 (1,2) 重建，否则选项上限 2 无来源
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'py'))

QS = [
# ---------------- T023 超难压轴小题 (p237) ----------------
dict(topic='M-T-023', key='M-T-023-E1', kind='典例', type='填空',
  stem_text=r'设 $x$、$y$ 为正实数，若 $4x^{2}+y^{2}+xy=1$，'
            r'则 $\frac{4x+2y}{20x^{2}+11xy+5y^{2}}$ 的取值范围是 ____',
  opts=[],
  answer=r'$\left(\frac{2}{5},\frac{\sqrt{6}}{6}\right]$',
  solution=r'由 $4x^{2}+y^{2}\geq 4xy$ 得 $1=4x^{2}+y^{2}+xy\geq 5xy$，'
           r'故 $0<xy\leq\frac{1}{5}$。'
           r'记 $s=xy$、$t=2x+y$，则 $t^{2}=4x^{2}+y^{2}+4xy'
           r'=(4x^{2}+y^{2}+xy)+3xy=1+3s$，'
           r'且分母 $20x^{2}+11xy+5y^{2}=5(4x^{2}+y^{2})+11xy=5(1-s)+11s=5+6s$。'
           r'原式 $=\frac{2t}{5+6s}=\frac{2\sqrt{1+3s}}{5+6s}$，记 '
           r'$g(s)=\frac{2\sqrt{1+3s}}{5+6s}$，$s\in\left(0,\frac{1}{5}\right]$。'
           r"$g'(s)=\frac{3(1-6s)}{(5+6s)^{2}\sqrt{1+3s}}$，"
           r'当 $s<\frac{1}{6}$ 时递增、$s>\frac{1}{6}$ 时递减，'
           r'故 $g_{\max}=g\!\left(\frac{1}{6}\right)=\frac{\sqrt{6}}{6}$。'
           r'又 $g(0)=\frac{2}{5}$、$g\!\left(\frac{1}{5}\right)=\frac{2\sqrt{8/5}}{31/5}'
           r'=\frac{4\sqrt{10}}{31}\approx0.408$，'
           r'结合单调性得值域为 $\left(\frac{2}{5},\frac{\sqrt{6}}{6}\right]$。',
  review='**原书答案 $\\left(0,\\frac{\\sqrt6}{6}\\right]$ 的下界有误，正确为 '
         '$\\left(\\frac25,\\frac{\\sqrt6}{6}\\right]$**。'
         '错因：解析写「令 $t=2x+y\\in(0,\\frac85]$」，把 $t$ 与 $t^2$ 的范围混淆了 —— '
         '实际 $t^2=1+3xy\\in(1,\\frac85]$，故 $t\\in(1,\\sqrt{8/5}]$，'
         '从而 $t\\to1$（即 $xy\\to0$）时原式趋于 $\\frac25$ 而非 $0$。'
         '参数化扫描验证：$s\\in(0,\\frac15]$ 上 $g(s)=\\frac{2\\sqrt{1+3s}}{5+6s}$ 的值域为 '
         '$[0.400000,0.408248]$，与 $\\frac25=0.4$、$\\frac{\\sqrt6}{6}=0.408248$ 一致。'),

dict(topic='M-T-023', key='M-T-023-V1', kind='变式1', type='填空',
  stem_text=r'若 $x$、$y$ 均为正实数，则 $\frac{x^{2}+y^{2}+1}{(x+2)y}$ 的最小值为 ____',
  opts=[],
  answer=r'$\frac{2\sqrt{5}}{5}$',
  solution=r'引入参数 $t\in(0,1)$，将 $x^{2}+y^{2}$ 拆为 $x^{2}+ty^{2}+(1-t)y^{2}$：'
           r'$x^{2}+ty^{2}\geq 2\sqrt{t}xy$，$(1-t)y^{2}+1\geq 2\sqrt{1-t}y$。'
           r'故分子 $\geq 2\sqrt{t}xy+2\sqrt{1-t}y$。'
           r'令 $2\sqrt{t}=\frac{1}{2}\cdot 2\sqrt{1-t}$（使各项与分母 $(x+2)y=xy+2y$ 成比例），'
           r'即 $2\sqrt{t}=\sqrt{1-t}$，得 $4t=1-t$，$t=\frac{1}{5}$。'
           r'此时分子 $\geq\frac{2}{\sqrt{5}}xy+\frac{4}{\sqrt{5}}y'
           r'=\frac{2}{\sqrt{5}}(xy+2y)$，故原式 $\geq\frac{2}{\sqrt{5}}=\frac{2\sqrt{5}}{5}$，'
           r'当且仅当 $x=\sqrt{t}y$ 且 $\sqrt{1-t}y=1$ 时取等号。',
  review='数值扫描验证最小值 $0.894428$，与 $\\frac{2\\sqrt5}{5}=0.894427$ 一致。'),

dict(topic='M-T-023', key='M-T-023-V2', kind='变式2', type='填空',
  stem_text=r'已知 $a$、$b\in[0,1]$，则 $S(a,b)=\frac{a}{1+b}+\frac{b}{1+a}+(1-a)(1-b)$ '
            r'的最小值为 ____',
  opts=[],
  answer=r'$\frac{13-5\sqrt{5}}{2}$',
  solution=r'通分得 $S(a,b)=\frac{a(1+a)+b(1+b)+(1-a)(1-b)(1+a)(1+b)}{(1+a)(1+b)}$。'
           r'展开分子：$(a+a^{2})+(b+b^{2})+(1-a-b+ab)(1+a+b+ab)$，'
           r'其中 $(1-a)(1-b)=1-a-b+ab$，$(1+a)(1+b)=1+a+b+ab$，'
           r'两者之积 $=((1+ab)-(a+b))((1+ab)+(a+b))=(1+ab)^{2}-(a+b)^{2}$。'
           r'整理得 $S=1+\frac{a^{2}b^{2}-ab}{(1+a)(1+b)}$。'
           r'记 $x=ab\in[0,1]$，由 $(1+a)(1+b)=1+a+b+ab\geq 1+2\sqrt{ab}+ab=(1+x)^{2}$，'
           r'得 $\frac{ab(1-ab)}{(1+a)(1+b)}\leq\frac{x(1-x^{2})}{(1+x)^{2}}'
           r'=\frac{x^{2}(1-x)}{1+x}\triangleq f(x)$。'
           r"$f'(x)=\frac{-2x(x^{2}+x-1)}{(1+x)^{2}}$，故 $f$ 在 $x=\frac{\sqrt5-1}{2}$ 处取最大值 "
           r'$f_{\max}=\frac{5\sqrt5-11}{2}$。'
           r'所以 $S_{\min}=1-f_{\max}=\frac{13-5\sqrt5}{2}$。',
  review=''),

dict(topic='M-T-023', key='M-T-023-V3', kind='变式3', type='填空',
  stem_text=r'已知 $a>1$，$b>2$，则 $\frac{(a+b)^{2}}{\sqrt{a^{2}-1}+\sqrt{b^{2}-4}}$ 的最小值为 ____',
  opts=[],
  answer=r'$6$',
  solution=r'令 $m=\sqrt{a^{2}-1}$、$n=\sqrt{b^{2}-4}$，则 $a^{2}=m^{2}+1$、$b^{2}=n^{2}+4$，'
           r'且 $a=\sqrt{m^{2}+1}$、$b=\sqrt{n^{2}+4}$。'
           r'$(a+b)^{2}=a^{2}+b^{2}+2ab=m^{2}+n^{2}+5+2\sqrt{(m^{2}+1)(n^{2}+4)}$。'
           r'由 $\sqrt{(m^{2}+1)(n^{2}+4)}\geq\sqrt{m^{2}n^{2}+4mn+4}=mn+2$'
           r'（因 $(m^{2}+1)(n^{2}+4)-(mn+2)^{2}=4m^{2}+n^{2}-4mn=(2m-n)^{2}\geq 0$），'
           r'得 $(a+b)^{2}\geq m^{2}+n^{2}+5+2(mn+2)=(m+n)^{2}+9$。'
           r'故原式 $\geq\frac{(m+n)^{2}+9}{m+n}=(m+n)+\frac{9}{m+n}\geq 2\sqrt{9}=6$，'
           r'当且仅当 $2m=n$ 且 $m+n=3$，即 $m=1$、$n=2$（$a=\sqrt2$、$b=2\sqrt2$）时取等号。',
  review=''),

# ---------------- T066 一元二次复合型：可因式分解 (p40) ----------------
dict(topic='M-T-066', key='M-T-066-E1', kind='典例', type='选择',
  stem_text=r'已知函数 $f(x)=\frac{x}{\ln x}$，若关于 $x$ 的方程 '
            r'$f^{2}(x)+af(x)+a-1=0$ 有且仅有三个不同的实数解，'
            r'则实数 $a$ 的取值范围是（　　）',
  opts=[('A', r'$(-2e,1-e)$'), ('B', r'$(1-e,0)$'),
        ('C', r'$(-\infty,1-e)$'), ('D', r'$(1-e,2e)$')],
  answer='C',
  solution=r'方程化为 $(f(x)+1)(f(x)+a-1)=0$，即 $f(x)=-1$ 或 $f(x)=1-a$。'
           r"$f'(x)=\frac{\ln x-1}{\ln^{2}x}$：在 $(0,1)$ 上 $\ln x<0$，$f'<0$，$f$ 从 $0^{-}$ 递减到 $-\infty$；"
           r"在 $(1,e)$ 上 $f'<0$，$f$ 从 $+\infty$ 递减到 $e$；"
           r"在 $(e,+\infty)$ 上 $f'>0$，$f$ 从 $e$ 递增到 $+\infty$。"
           r'故 $f(x)=-1$ 在 $(0,1)$ 内恰有一解；'
           r'而 $f(x)=1-a$ 有两解当且仅当 $1-a>e$。'
           r'于是 $a<1-e$。故选 C。',
  review=''),

dict(topic='M-T-066', key='M-T-066-V1', kind='变式1', type='选择',
  stem_text=r'已知 $f(x)$ 是定义在 $\mathbb{R}$ 上的偶函数，且满足 '
            r'$f(x)=\begin{cases}-x^{2}+3x,&0\leq x<1\\ x-2\ln x,&x\geq 1\end{cases}$，'
            r'若关于 $x$ 的方程 $[f(x)]^{2}+(a-1)f(x)-a=0$ 有 $10$ 个不同的实数解，'
            r'则实数 $a$ 的取值范围是（　　）',
  opts=[('A', r'$(1,2)$'), ('B', r'$(-2,-1)\cup\{2\ln 2-2\}$'),
        ('C', r'$(-2,2\ln 2-2)$'), ('D', r'$(-2,2\ln 2-2]$')],
  answer='B',
  solution=r'方程化为 $(f(x)-1)(f(x)+a)=0$，即 $f(x)=1$ 或 $f(x)=-a$。'
           r"先看 $x\geq 0$：$x\geq 1$ 时 $f'(x)=1-\frac{2}{x}$，在 $[1,2]$ 递减、$[2,+\infty)$ 递增，"
           r'极小值 $f(2)=2-2\ln 2$，$f(1)=1$，$x\to+\infty$ 时 $f\to+\infty$；'
           r'$0\leq x<1$ 时 $f(x)=-x^{2}+3x$ 单调递增，值域 $[0,2)$。'
           r'于是对值 $c$：$c\in(2-2\ln2,1)$ 有 $3$ 个解，$c=2-2\ln 2$ 有 $2$ 个解，'
           r'$c\in(1,2)$ 有 $2$ 个解，$c=1$ 有 $3$ 个解。'
           r'$f(x)=1$ 在 $[0,+\infty)$ 有 $3$ 解，由偶性在 $\mathbb{R}$ 上有 $6$ 解；'
           r'故需 $f(x)=-a$ 在 $\mathbb{R}$ 上有 $4$ 解，即 $-a=2-2\ln2$ 或 $-a\in(1,2)$。'
           r'解得 $a=2\ln2-2$ 或 $-2<a<-1$。故选 B。',
  review=''),

dict(topic='M-T-066', key='M-T-066-V2', kind='变式2', type='选择',
  stem_text=r'函数 $f(x)=\begin{cases}a,&x=1\\ \left(\frac{1}{2}\right)^{|x-1|}+1,&x\neq 1\end{cases}$，'
            r'若关于 $x$ 的方程 $2f^{2}(x)-(2a+3)f(x)+3a=0$ 有五个不同的实数解，'
            r'则 $a$ 的取值范围是（　　）',
  opts=[('A', r'$(1,2)$'), ('B', r'$\left(1,\frac{3}{2}\right)\cup\left(\frac{3}{2},2\right)$'),
        ('C', r'$\left(\frac{3}{2},2\right)$'), ('D', r'$\left(1,\frac{3}{2}\right)$')],
  answer='B',
  solution=r'方程化为 $(2f(x)-3)(f(x)-a)=0$，即 $f(x)=\frac{3}{2}$ 或 $f(x)=a$。'
           r'当 $x\neq 1$ 时 $f(x)=\left(\frac12\right)^{|x-1|}+1\in(1,2)$，'
           r'且对 $c\in(1,2)$ 方程 $f(x)=c$ 恰有两解 $x=1\pm\log_{\frac12}(c-1)$。'
           r'故 $f(x)=\frac{3}{2}$ 有 $2$ 解；需 $f(x)=a$ 有 $3$ 解，'
           r'即 $x=1$ 处一解、$x\neq1$ 处两解，故 $a\in(1,2)$。'
           r'又 $a\neq\frac{3}{2}$（否则与前一方程的解重合，总解数不足 $5$）。'
           r'所以 $a\in\left(1,\frac32\right)\cup\left(\frac32,2\right)$，选 B。',
  review='PDF 提取时指数符号丢失（原文 $\\left(\\frac12\\right)^{|x-1|}+1$ 被提取成 '
         '"1 2 |x-1|+ 1"），已按选项上限 $2$ 反推重建为指数形式。'
         '若为 $\\frac12|x-1|+1$ 则值域为 $(1,+\\infty)$，选项上限 $2$ 无从产生。'),

dict(topic='M-T-066', key='M-T-066-V3', kind='变式3', type='选择',
  stem_text=r'已知函数 $f(x)=\begin{cases}x^{2}-1,&x<1\\ \frac{\ln x}{x},&x\geq 1\end{cases}$，'
            r'若关于 $x$ 的方程 $f^{2}(x)+(1-2m)f(x)-2m=0$ 有 $4$ 个不同的实数解，'
            r'则实数 $m$ 的取值范围是（　　）',
  opts=[('A', r'$\left(\frac{1}{3},\frac{1}{e}\right)$'), ('B', r'$\left(\frac{1}{3},\frac{1}{2e}\right)$'),
        ('C', r'$\left(0,\frac{1}{e}\right)$'), ('D', r'$\left(0,\frac{1}{2e}\right)$')],
  answer='D',
  solution=r'方程化为 $(f(x)-2m)(f(x)+1)=0$，即 $f(x)=2m$ 或 $f(x)=-1$。'
           r'$x<1$ 时 $f=x^{2}-1$：$c=-1$ 有一解 $x=0$；$c\in(-1,0)$ 有两解；'
           r'$c\geq 0$ 有一解。'
           r"$x\geq1$ 时 $f=\frac{\ln x}{x}$，$f'(x)=\frac{1-\ln x}{x^{2}}$，"
           r'在 $[1,e]$ 递增、$[e,+\infty)$ 递减，值域 $\left(0,\frac1e\right]$：'
           r'$c\in\left(0,\frac1e\right)$ 有两解，$c=\frac1e$ 一解，$c=0$ 一解（$x=1$）。'
           r'$f(x)=-1$ 仅 $x=0$ 一解，故需 $f(x)=2m$ 有 $3$ 解，'
           r'即 $2m\in\left(0,\frac1e\right)$，解得 $0<m<\frac{1}{2e}$。故选 D。',
  review=''),
]

if __name__ == '__main__':
    print('共 %d 题' % len(QS))
