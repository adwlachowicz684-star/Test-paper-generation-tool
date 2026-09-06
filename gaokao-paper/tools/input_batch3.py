# -*- coding: utf-8 -*-
r"""第3批录入数据：T012~T016（不等式 / 基本不等式）。

来源：2024高中数学热点题型归纳完整解析版.pdf p231~p234
      —— 逐题读原文重建，18 题答案全部独立验算通过。

**LaTeX 相关字符串一律用 raw 前缀** —— 这是本文件最重要的纪律。
'\v'、'\b'、'\n' 在普通字符串里是转义字符，会把题目污染成
垂直制表符、退格符、换行符，且完全看不出原因。
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'py'))

# 所有字符串均 raw，避免 \v \b \n 等被 Python 解释
QS = [
# ---------------- T012 构造分母：待定系数 (p231) ----------------
dict(topic='M-T-012', kind='典例', type='选择',
  stem_text=r'已知正实数 $x$、$y$ 满足 $4x+3y=4$，则 $\frac{1}{2x+1}+\frac{1}{3y+2}$ 的最小值为（　　）',
  opts=[('A', r'$\frac{3}{8}+\frac{\sqrt{2}}{4}$'),
        ('B', r'$\frac{1}{2}+\frac{\sqrt{2}}{3}$'),
        ('C', r'$\frac{1}{2}+\frac{\sqrt{2}}{3}$'),
        ('D', r'$\frac{1}{2}+\frac{\sqrt{2}}{2}$')],
  answer='A',
  solution=r'由 $4x+3y=4$ 得 $2(2x+1)+(3y+2)=8$。令 $a=2x+1$，$b=3y+2$，则 $2a+b=8$。'
           r'$\frac{1}{a}+\frac{1}{b}=\left(\frac{1}{a}+\frac{1}{b}\right)\cdot\frac{2a+b}{8}'
           r'=\frac{1}{8}\left(3+\frac{2a}{b}+\frac{b}{a}\right)$'
           r'$\geq\frac{1}{8}\left(3+2\sqrt{\frac{2a}{b}\cdot\frac{b}{a}}\right)=\frac{3+2\sqrt{2}}{8}'
           r'=\frac{3}{8}+\frac{\sqrt{2}}{4}$，'
           r'当且仅当 $2a=b$ 时取等号。故选 A。',
  review='原书选项 B、C 印刷完全相同（均为 $\\frac{1}{2}+\\frac{\\sqrt{2}}{3}$）。'
         '答案 A 不受影响，选项按原样录入。'),

dict(topic='M-T-012', kind='变式1', type='选择',
  stem_text=r'已知正实数 $x$、$y$ 满足 $\frac{1}{x+3y}+\frac{1}{2x+y}=1$，则 $x+y$ 的最小值为（　　）',
  opts=[('A', r'$\frac{3+2\sqrt{2}}{5}$'), ('B', r'$\frac{3+3\sqrt{2}}{5}$'),
        ('C', r'$\frac{2+2\sqrt{2}}{5}$'), ('D', r'$\frac{2+3\sqrt{2}}{5}$')],
  answer='A',
  solution=r'待定系数：设 $x+y=m(x+3y)+n(2x+y)=(m+2n)x+(3m+n)y$，'
           r'由 $\begin{cases}m+2n=1\\3m+n=1\end{cases}$ 解得 $m=\frac{1}{5}$，$n=\frac{2}{5}$。'
           r'故 $x+y=\left[\frac{1}{5}(x+3y)+\frac{2}{5}(2x+y)\right]\cdot 1'
           r'=\left[\frac{1}{5}(x+3y)+\frac{2}{5}(2x+y)\right]\left(\frac{1}{x+3y}+\frac{1}{2x+y}\right)$'
           r'$=\frac{3}{5}+\frac{x+3y}{5(2x+y)}+\frac{2(2x+y)}{5(x+3y)}$'
           r'$\geq\frac{3}{5}+2\sqrt{\frac{1}{5}\cdot\frac{2}{5}}=\frac{3+2\sqrt{2}}{5}$，'
           r'当且仅当 $x+3y=\sqrt{2}(2x+y)$ 时取等号。故选 A。',
  review=''),

dict(topic='M-T-012', kind='变式2', type='填空',
  stem_text=r'已知 $a>0$，$b>0$，$a+2b=1$，则 $\frac{1}{3a+4b}+\frac{1}{a+3b}$ 取得最小值为 ____',
  opts=[],
  answer=r'$\frac{3+2\sqrt{2}}{5}$',
  solution=r'令 $a+2b=\lambda(3a+4b)+\mu(a+3b)=(3\lambda+\mu)a+(4\lambda+3\mu)b$，'
           r'由 $\begin{cases}3\lambda+\mu=1\\4\lambda+3\mu=2\end{cases}$ 解得 $\lambda=\frac{1}{5}$，$\mu=\frac{2}{5}$。'
           r'故原式 $=\left(\frac{1}{3a+4b}+\frac{1}{a+3b}\right)\left[\frac{1}{5}(3a+4b)+\frac{2}{5}(a+3b)\right]$'
           r'$=\frac{3}{5}+\frac{2(a+3b)}{5(3a+4b)}+\frac{3a+4b}{5(a+3b)}$'
           r'$\geq\frac{3}{5}+2\sqrt{\frac{2}{5}\cdot\frac{1}{5}}=\frac{3+2\sqrt{2}}{5}$，'
           r'当且仅当 $2(a+3b)=3a+4b$，即 $a=2b$ 时取等号。',
  review=''),

# ---------------- T013 分子含参型：分离分子 (p232) ----------------
dict(topic='M-T-013', kind='典例', type='填空',
  stem_text=r'若 $4x>y>0$，则 $\frac{y}{4x-y}+\frac{x}{y}$ 的最小值为 ____',
  opts=[],
  answer=r'$\frac{5}{4}$',
  solution=r'由 $4x>y>0$ 知 $4x-y>0$。'
           r'$\frac{y}{4x-y}+\frac{x}{y}=\frac{y}{4x-y}+\frac{4x}{4y}'
           r'=\frac{y}{4x-y}+\frac{(4x-y)+y}{4y}=\frac{y}{4x-y}+\frac{4x-y}{4y}+\frac{1}{4}$'
           r'$\geq 2\sqrt{\frac{y}{4x-y}\cdot\frac{4x-y}{4y}}+\frac{1}{4}=2\times\frac{1}{2}+\frac{1}{4}=\frac{5}{4}$，'
           r'当且仅当 $\frac{y}{4x-y}=\frac{4x-y}{4y}$，即 $3y=4x$ 时取等号。',
  review=''),

dict(topic='M-T-013', kind='变式1', type='选择',
  stem_text=r'已知正实数 $a$、$b$ 满足 $a+2b=2$，则 $\frac{a^{2}+1}{a}+\frac{2b^{2}}{b+1}$ 的最小值是（　　）',
  opts=[('A', r'$\frac{9}{4}$'), ('B', r'$\frac{7}{3}$'),
        ('C', r'$\frac{17}{4}$'), ('D', r'$\frac{13}{3}$')],
  answer='A',
  solution=r'$\frac{a^{2}+1}{a}=a+\frac{1}{a}$；'
           r'$\frac{2b^{2}}{b+1}=\frac{2b(b+1)-2(b+1)+2}{b+1}=2b-2+\frac{2}{b+1}$。'
           r'故原式 $=\left(a+2b\right)+\frac{1}{a}+\frac{2}{b+1}-2=\frac{1}{a}+\frac{2}{b+1}$。'
           r'由 $a+2b=2$ 得 $a+2(b+1)=4$，'
           r'故 $\frac{1}{a}+\frac{2}{b+1}=\frac{1}{4}\left[a+2(b+1)\right]\left(\frac{1}{a}+\frac{2}{b+1}\right)$'
           r'$=\frac{1}{4}\left(5+\frac{2a}{b+1}+\frac{2(b+1)}{a}\right)$'
           r'$\geq\frac{1}{4}\left(5+2\sqrt{\frac{2a}{b+1}\cdot\frac{2(b+1)}{a}}\right)=\frac{9}{4}$，'
           r'当且仅当 $a=b+1$，即 $a=\frac{4}{3}$，$b=\frac{1}{3}$ 时取等号。故选 A。',
  review=''),

dict(topic='M-T-013', kind='变式2', type='填空',
  stem_text=r'若 $x$、$y\in\mathbb{R}^{+}$，且 $x+2y=1$，则 $\frac{x^{2}}{x+1}+\frac{2y^{2}}{y+2}$ 的最小值为 ____',
  opts=[],
  answer=r'$\frac{1}{6}$',
  solution=r'令 $m=x+1$，$n=y+2$，则 $x=m-1$，$y=n-2$，'
           r'由 $x+2y=1$ 得 $m+2n=6$。'
           r'$\frac{x^{2}}{x+1}=\frac{(m-1)^{2}}{m}=m-2+\frac{1}{m}$；'
           r'$\frac{2y^{2}}{y+2}=\frac{2(n-2)^{2}}{n}=2n-8+\frac{8}{n}$。'
           r'故原式 $=m+2n+\frac{1}{m}+\frac{8}{n}-10=\frac{1}{m}+\frac{8}{n}-4$。'
           r'$\frac{1}{m}+\frac{8}{n}=\frac{1}{6}(m+2n)\left(\frac{1}{m}+\frac{8}{n}\right)'
           r'=\frac{1}{6}\left(17+\frac{8m}{n}+\frac{2n}{m}\right)$'
           r'$\geq\frac{1}{6}\left(17+2\sqrt{\frac{8m}{n}\cdot\frac{2n}{m}}\right)=\frac{25}{6}$，'
           r'故原式 $\geq\frac{25}{6}-4=\frac{1}{6}$，当且仅当 $n=2m$，即 $m=\frac{6}{5}$、$n=\frac{12}{5}$ 时取等号。',
  review=''),

dict(topic='M-T-013', kind='变式3', type='填空',
  stem_text=r'若正实数 $x$、$y$ 满足 $2x+y=2$，则 $\frac{4x^{2}}{y+1}+\frac{y^{2}}{2x+2}$ 的最小值是 ____',
  opts=[],
  answer=r'$\frac{4}{5}$',
  solution=r'由 $2x+y=2$ 得 $y+1=3-2x$，$2x+2=4-y$。'
           r'$\frac{4x^{2}}{y+1}=\frac{(y-2)^{2}}{y+1}=\frac{(y+1-3)^{2}}{y+1}=(y+1)-6+\frac{9}{y+1}$；'
           r'$\frac{y^{2}}{2x+2}=\frac{2(x-1)^{2}}{x+1}=2(x+1)-8+\frac{8}{x+1}$。'
           r'故原式 $=2(x+1)+(y+1)+\frac{8}{x+1}+\frac{9}{y+1}-14$。'
           r'令 $A=2(x+1)$，$B=y+1$，则 $A+B=5$，且 $\frac{8}{x+1}=\frac{16}{A}$。'
           r'原式 $=\frac{16}{A}+\frac{9}{B}-9'
           r'=\frac{1}{5}(A+B)\left(\frac{16}{A}+\frac{9}{B}\right)-9'
           r'\geq\frac{1}{5}\left(25+2\sqrt{\frac{9A}{B}\cdot\frac{16B}{A}}\right)-9=\frac{49}{5}-9=\frac{4}{5}$，'
           r'当且仅当 $3A=4B$，即 $x=\frac{3}{7}$、$y=\frac{8}{7}$ 时取等号。',
  review='原书详解此处推导较简略，本解析已补全分离常数的中间步骤。'),

# ---------------- T014 反解代入型：消元法 (p232) ----------------
dict(topic='M-T-014', kind='典例', type='填空',
  stem_text=r'已知正数 $a$、$b$ 满足 $\frac{1}{a}+\frac{1}{b}=2$，则 $\frac{3}{b+1}-a$ 的最大值为 ____',
  opts=[],
  answer=r'$\frac{5-2\sqrt{3}}{3}$',
  solution=r'由 $\frac{1}{a}+\frac{1}{b}=2$ 得 $\frac{1}{b}=\frac{2a-1}{a}$，故 $b=\frac{a}{2a-1}$。'
           r'由 $a>0$、$b>0$ 得 $a>\frac{1}{2}$。'
           r'$\frac{3}{b+1}-a=\frac{3}{\frac{a}{2a-1}+1}-a=\frac{3(2a-1)}{3a-1}-a'
           r'=2-\frac{1}{3a-1}-a=\frac{5}{3}-\left(\frac{1}{3a-1}+\frac{3a-1}{3}\right)$'
           r'$\leq\frac{5}{3}-2\sqrt{\frac{1}{3a-1}\cdot\frac{3a-1}{3}}=\frac{5}{3}-\frac{2\sqrt{3}}{3}'
           r'=\frac{5-2\sqrt{3}}{3}$，'
           r'当且仅当 $\frac{1}{3a-1}=\frac{3a-1}{3}$ 即 $a=\frac{1+\sqrt{3}}{3}$ 时取等号。',
  review='原书详解取等值印作 $a=1+\frac{\\sqrt{3}}{3}\\approx1.577$，实为 $a=\\frac{1+\\sqrt{3}}{3}\\approx0.911$'
         '（数值扫描验证：最大值在 $a\\approx0.9107$ 处取得）。系原书笔误，答案正确。'),

dict(topic='M-T-014', kind='变式1', type='选择',
  stem_text=r'已知 $m>1$，$n>0$，且 $m^{2}+2n=3m$，则 $\frac{2}{m-1}+\frac{m}{4n}$ 的最小值为（　　）',
  opts=[('A', r'$\frac{9}{4}$'), ('B', r'$\frac{9}{2}$'),
        ('C', r'$\frac{3}{2}$'), ('D', r'$2$')],
  answer='A',
  solution=r'由 $m^{2}+2n=3m$ 得 $2n=3m-m^{2}=m(3-m)$，由 $n>0$、$m>1$ 得 $1<m<3$。'
           r'$\frac{2}{m-1}+\frac{m}{4n}=\frac{2}{m-1}+\frac{m}{2m(3-m)}=\frac{2}{m-1}+\frac{1}{2(3-m)}$。'
           r'令 $a=m-1$，$b=3-m$，则 $a+b=2$，$a>0$，$b>0$。'
           r'原式 $=\frac{a+b}{a}+\frac{a+b}{4b}=\frac{5}{4}+\frac{b}{a}+\frac{a}{4b}$'
           r'$\geq\frac{5}{4}+2\sqrt{\frac{b}{a}\cdot\frac{a}{4b}}=\frac{5}{4}+1=\frac{9}{4}$，'
           r'当且仅当 $\frac{b}{a}=\frac{a}{4b}$ 即 $a=2b$，'
           r'亦即 $m=\frac{7}{3}$、$n=\frac{7}{9}$ 时取等号。故选 A。',
  review='原书详解中间式写作「$\\frac{9}{4}+\\frac{b}{a}+\\frac{a}{4b}$」，'
         '常数项应为 $\\frac{5}{4}$（否则与最终结果 $\\frac{9}{4}$ 矛盾）。答案正确。'),

dict(topic='M-T-014', kind='变式2', type='填空',
  stem_text=r'若正数 $a$、$b$ 满足 $a+b+2=ab$，则 $\frac{3}{a-1}+\frac{1}{b-1}$ 的最小值是 ____，此时 $b=$ ____',
  opts=[],
  answer=r'$2$；$2$',
  solution=r'由 $a+b+2=ab$ 得 $a(b-1)=b+2$，即 $a=\frac{b+2}{b-1}$。'
           r'由 $a>0$、$b>0$ 得 $b>1$。'
           r'$a-1=\frac{b+2}{b-1}-1=\frac{3}{b-1}$，'
           r'故 $\frac{3}{a-1}+\frac{1}{b-1}=(b-1)+\frac{1}{b-1}\geq 2$，'
           r'当且仅当 $b-1=\frac{1}{b-1}$ 即 $b=2$（此时 $a=4$）时取等号。',
  review=''),

dict(topic='M-T-014', kind='变式3', type='填空',
  stem_text=r'若正实数 $x$、$y$ 满足 $\frac{1}{x}+\frac{1}{y}+\frac{x}{y}=4$，则 $x+\frac{1}{x}+\frac{1}{y}$ 的最小值为 ____',
  opts=[],
  answer=r'$2\sqrt{5}-1$',
  solution=r'由 $\frac{1}{x}+\frac{1}{y}+\frac{x}{y}=4$ 两边乘 $xy$ 得 $y+x+x^{2}=4xy$，'
           r'整理得 $y(4x-1)=x(1+x)$，故 $y=\frac{x(1+x)}{4x-1}$（由 $y>0$ 知 $x>\frac{1}{4}$）。'
           r'$x+\frac{1}{x}+\frac{1}{y}=x+\frac{1}{x}+\frac{4x-1}{x(1+x)}'
           r'=x+\frac{(x+1)+(4x-1)}{x(x+1)}=x+\frac{5}{x+1}=(x+1)+\frac{5}{x+1}-1$'
           r'$\geq 2\sqrt{5}-1$，'
           r'当且仅当 $x+1=\frac{5}{x+1}$ 即 $x=\sqrt{5}-1$ 时取等号。',
  review='原书详解中间式「$x^{2}+x+\\frac{5}{x+1}$」应为「$x+\\frac{5}{x+1}$」。答案正确。'),

# ---------------- T015 因式分解型 (p233) ----------------
dict(topic='M-T-015', kind='典例', type='填空',
  stem_text=r'非负实数 $x$、$y$ 满足 $2xy+x+6y-6=0$，则 $x+2y$ 的最小值为 ____',
  opts=[],
  answer=r'$2$',
  solution=r'由 $2xy+x+6y-6=0$ 得 $(x+3)(2y+1)=9$。'
           r'由基本不等式 $(x+3)(2y+1)\leq\left[\frac{(x+3)+(2y+1)}{2}\right]^{2}=\frac{(x+2y+4)^{2}}{4}$，'
           r'得 $9\leq\frac{(x+2y+4)^{2}}{4}$，即 $(x+2y+4)^{2}\geq 36$。'
           r'由 $x+2y+4>0$ 得 $x+2y+4\geq 6$，故 $x+2y\geq 2$，'
           r'当且仅当 $x+3=2y+1$ 且 $(x+3)(2y+1)=9$，即 $x=0$、$y=1$ 时取等号。',
  review=''),

dict(topic='M-T-015', kind='变式1', type='填空',
  stem_text=r'已知 $a$、$b\in\mathbb{R}^{+}$，且 $(a+b)(a+2b)+a+b=9$，则 $3a+4b$ 的最小值等于 ____',
  opts=[],
  answer=r'$6\sqrt{2}-1$',
  solution=r'由 $(a+b)(a+2b)+a+b=9$ 得 $(a+b)(a+2b+1)=9$，'
           r'两边乘 $2$ 得 $(2a+2b)(a+2b+1)=18$。'
           r'$(2a+2b)+(a+2b+1)=3a+4b+1\geq 2\sqrt{(2a+2b)(a+2b+1)}=2\sqrt{18}=6\sqrt{2}$，'
           r'故 $3a+4b\geq 6\sqrt{2}-1$，'
           r'当且仅当 $2a+2b=a+2b+1$ 即 $a=1$ 时取等号。',
  review=''),

dict(topic='M-T-015', kind='变式2', type='填空',
  stem_text=r'已知 $x>0$，$y>0$，且 $2x+4y+xy=1$，则 $x+2y$ 的最小值是 ____',
  opts=[],
  answer=r'$6\sqrt{2}-8$',
  solution=r'由 $2x+4y+xy=1$ 得 $(x+4)(y+2)=9$，两边乘 $2$ 得 $(x+4)(2y+4)=18$。'
           r'$(x+4)+(2y+4)=x+2y+8\geq 2\sqrt{(x+4)(2y+4)}=2\sqrt{18}=6\sqrt{2}$，'
           r'故 $x+2y\geq 6\sqrt{2}-8$，'
           r'当且仅当 $x+4=2y+4$ 即 $x=2y$ 时取等号。',
  review='原书详解写作「$3\\sqrt{2}=\\sqrt{(x+4)(2y+4)}\\leq\\cdots$」，'
         '左边应为 $\\sqrt{18}=3\\sqrt{2}$ 是右边乘积的开方而非乘积本身，中间表述有误。答案正确。'),

# ---------------- T016 均值用两次 (p233) ----------------
dict(topic='M-T-016', kind='典例', type='选择',
  stem_text=r'$a$、$b$、$c$ 是不同时为 $0$ 的实数，则 $\frac{ab+bc}{a^{2}+2b^{2}+c^{2}}$ 的最大值为（　　）',
  opts=[('A', r'$\frac{1}{2}$'), ('B', r'$\frac{1}{4}$'),
        ('C', r'$\frac{\sqrt{2}}{2}$'), ('D', r'$\frac{\sqrt{3}}{2}$')],
  answer='A',
  solution=r'$\frac{ab+bc}{a^{2}+2b^{2}+c^{2}}=\frac{b(a+c)}{a^{2}+2b^{2}+c^{2}}'
           r'=\frac{a+c}{\frac{a^{2}+c^{2}}{b}+2b}$（$b\neq 0$）'
           r'$\leq\frac{a+c}{2\sqrt{\frac{a^{2}+c^{2}}{b}\cdot 2b}}=\frac{a+c}{2\sqrt{2(a^{2}+c^{2})}}$'
           r'$=\frac{1}{2}\sqrt{\frac{a^{2}+2ac+c^{2}}{2(a^{2}+c^{2})}}'
           r'=\frac{1}{2}\sqrt{\frac{1}{2}+\frac{ac}{a^{2}+c^{2}}}$'
           r'$\leq\frac{1}{2}\sqrt{\frac{1}{2}+\frac{1}{2}}=\frac{1}{2}$，'
           r'当且仅当 $a^{2}+c^{2}=2b^{2}$ 且 $a=c$ 时取等号。故选 A。',
  review=''),

dict(topic='M-T-016', kind='变式1', type='选择',
  stem_text=r'设正实数 $x$、$y$ 满足 $x>\frac{1}{2}$，$y>1$，不等式 $\frac{4x^{2}}{y-1}+\frac{y^{2}}{2x-1}\geq m$ 恒成立，则 $m$ 的最大值为（　　）',
  opts=[('A', r'$8$'), ('B', r'$16$'), ('C', r'$2\sqrt{2}$'), ('D', r'$4\sqrt{2}$')],
  answer='A',
  solution=r'令 $a=2x-1>0$，$b=y-1>0$，则 $x=\frac{a+1}{2}$，$y=b+1$。'
           r'$\frac{4x^{2}}{y-1}+\frac{y^{2}}{2x-1}=\frac{(a+1)^{2}}{b}+\frac{(b+1)^{2}}{a}$'
           r'$\geq 2\sqrt{\frac{(a+1)^{2}(b+1)^{2}}{ab}}=\frac{2(ab+a+b+1)}{\sqrt{ab}}$'
           r'$=2\left(\sqrt{ab}+\frac{1}{\sqrt{ab}}+\frac{a+b}{\sqrt{ab}}\right)$'
           r'$\geq 2\left(2+2\right)=8$，'
           r'当且仅当 $a=b=1$，即 $x=1$、$y=2$ 时取等号。故 $m$ 的最大值为 $8$。故选 A。',
  review='原书取等值印作「$x=2$，$y=1$」，此时 $y-1=0$ 使原式无意义。'
         '正确取等为 $x=1$、$y=2$（代入验证：$4+4=8$）。系原书笔误，答案正确。'),

dict(topic='M-T-016', kind='变式2', type='填空',
  stem_text=r'已知 $a>0$，$b>0$，则 $\frac{a^{2}+b^{2}+3}{a+\sqrt{2}b}$ 的最小值为 ____',
  opts=[],
  answer=r'$2$',
  solution=r'由基本不等式 $a^{2}+1\geq 2a$，$b^{2}+2\geq 2\sqrt{2}b$，'
           r'得 $a^{2}+b^{2}+3=(a^{2}+1)+(b^{2}+2)\geq 2a+2\sqrt{2}b=2(a+\sqrt{2}b)$。'
           r'故 $\frac{a^{2}+b^{2}+3}{a+\sqrt{2}b}\geq 2$，'
           r'当且仅当 $a=1$、$b=\sqrt{2}$ 时取等号。',
  review=''),

dict(topic='M-T-016', kind='变式3', type='填空',
  stem_text=r'已知正实数 $a$、$b$、$c$ 满足 $a^{2}+4b^{2}=3c^{2}$，则 $\frac{c}{a}+\frac{c}{2b}$ 的最小值为 ____',
  opts=[],
  answer=r'$\frac{2\sqrt{6}}{3}$',
  solution=r'$\frac{c}{a}+\frac{c}{2b}\geq 2\sqrt{\frac{c}{a}\cdot\frac{c}{2b}}'
           r'=\frac{2c}{\sqrt{2ab}}=\frac{\sqrt{2}c}{\sqrt{ab}}$。'
           r'又 $a^{2}+4b^{2}\geq 2\sqrt{a^{2}\cdot 4b^{2}}=4ab$，结合 $a^{2}+4b^{2}=3c^{2}$'
           r'得 $3c^{2}\geq 4ab$，即 $\frac{c}{\sqrt{ab}}\geq\frac{2}{\sqrt{3}}$。'
           r'故原式 $\geq\frac{2\sqrt{2}}{\sqrt{3}}=\frac{2\sqrt{6}}{3}$，'
           r'当且仅当 $a=2b$ 时两个不等式同时取等号。',
  review=''),
]

if __name__ == '__main__':
    print('共 %d 题' % len(QS))
