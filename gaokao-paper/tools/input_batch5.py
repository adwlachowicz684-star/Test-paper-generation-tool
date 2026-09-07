# -*- coding: utf-8 -*-
r"""第5批录入数据：T021 三元最值型 / T022 恒成立求参数型，共 8 题。

来源：2024高中数学热点题型归纳完整解析版.pdf p236
      —— 基于 ref_bank 提取文本逐题重建，8 题答案全部独立验算通过。

**LaTeX 相关字符串一律 raw 前缀**：'\v'、'\b'、'\n' 在普通字符串里是
转义字符，会把题目污染成控制字符且完全看不出原因（已踩三次）。

本批发现的三处原书/提取问题：
  T022-V1  原书解析取等坐标写 "x=2,y=1"，实为 x=1、y=2（答案 8 正确）
  T022-V2  选项 C 印刷为 (-∞,6)，严格应为 (-∞,6]（答案 C）
  T022-V3  ref_bank 存的答案 "2." 缺根号，正确为 √2（数值扫描确认 1.414214）
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'py'))

QS = [
# ---------------- T021 三元最值型 (p236) ----------------
dict(topic='M-T-021', key='M-T-021-E1', kind='典例', type='选择',
  stem_text=r'已知实数 $a$、$b$、$c$ 满足 $\frac{1}{4}a^{2}+\frac{1}{4}b^{2}+c^{2}=1$，'
            r'则 $ab+2bc+2ac$ 的取值范围是（　　）',
  opts=[('A', r'$(-\infty,4]$'), ('B', r'$[-4,4]$'), ('C', r'$[-2,4]$'), ('D', r'$[-1,4]$')],
  answer='C',
  solution=r'由 $(a+b+2c)^{2}\geq 0$ 得 $a^{2}+b^{2}+4c^{2}+2ab+4ac+4bc\geq 0$，'
           r'即 $ab+2ac+2bc\geq -\frac{1}{2}(a^{2}+b^{2}+4c^{2})'
           r'=-2\left(\frac{1}{4}a^{2}+\frac{1}{4}b^{2}+c^{2}\right)=-2$，'
           r'当 $a=b=-c$ 且 $c^{2}=\frac{2}{3}$ 时取等号。'
           r'又由 $2ab\leq a^{2}+b^{2}$、$4ac\leq a^{2}+4c^{2}$、$4bc\leq b^{2}+4c^{2}$ 相加得 '
           r'$2ab+4ac+4bc\leq 2a^{2}+2b^{2}+8c^{2}=8\left(\frac{1}{4}a^{2}+\frac{1}{4}b^{2}+c^{2}\right)=8$，'
           r'即 $ab+2ac+2bc\leq 4$，当 $a=b=2c$ 时取等号。'
           r'故取值范围是 $[-2,4]$，选 C。',
  review=''),

dict(topic='M-T-021', key='M-T-021-V1', kind='变式1', type='选择',
  stem_text=r'若实数 $a$、$b$、$c\in\mathbb{R}^{+}$，且 $ab+ac+bc+2\sqrt{5}=6-a^{2}$，'
            r'则 $2a+b+c$ 的最小值为（　　）',
  opts=[('A', r'$\sqrt{5}-1$'), ('B', r'$\sqrt{5}+1$'),
        ('C', r'$2\sqrt{5}+2$'), ('D', r'$2\sqrt{5}-2$')],
  answer='D',
  solution=r'由 $ab+ac+bc+2\sqrt{5}=6-a^{2}$ 得 $ab+a^{2}+ac+bc=6-2\sqrt{5}$，'
           r'即 $a(a+b)+c(a+b)=(a+b)(a+c)=6-2\sqrt{5}=(\sqrt{5}-1)^{2}$。'
           r'于是 $2a+b+c=(a+b)+(a+c)\geq 2\sqrt{(a+b)(a+c)}=2(\sqrt{5}-1)=2\sqrt{5}-2$，'
           r'当且仅当 $a+b=a+c$ 即 $b=c$ 时取等号。故选 D。',
  review=''),

dict(topic='M-T-021', key='M-T-021-V2', kind='变式2', type='填空',
  stem_text=r'已知 $a$、$b$、$c>0$，且 $a^{2}+b^{2}+c^{2}=10$，则 $ab+ac+bc$ 的最大值是 ____，'
            r'$ab+ac+2bc$ 的最大值是 ____',
  opts=[],
  answer=r'$10$；$5\sqrt{3}+5$',
  solution=r'由 $a^{2}+b^{2}\geq 2ab$、$a^{2}+c^{2}\geq 2ac$、$b^{2}+c^{2}\geq 2bc$ 相加得 '
           r'$2(a^{2}+b^{2}+c^{2})\geq 2(ab+ac+bc)$，即 $ab+ac+bc\leq 10$，'
           r'当 $a=b=c$ 时取等号，故第一空为 $10$。'
           r'对第二空，设 $ab+ac+2bc=\frac{1}{2}\boldsymbol{v}^{\mathrm{T}}A\boldsymbol{v}$，'
           r'其中 $\boldsymbol{v}=(a,b,c)^{\mathrm{T}}$，'
           r'$A=\begin{pmatrix}0&1&1\\1&0&2\\1&2&0\end{pmatrix}$。'
           r'$\det(A-\lambda I)=-\lambda^{3}+6\lambda+4=0$，解得特征值 '
           r'$\lambda=-2$、$1-\sqrt{3}$、$1+\sqrt{3}$。'
           r'由 Rayleigh 商，最大值为 $\frac{1}{2}(1+\sqrt{3})\cdot 10=5\sqrt{3}+5\approx 13.660$。',
  review=''),

dict(topic='M-T-021', key='M-T-021-V3', kind='变式3', type='填空',
  stem_text=r'若正实数 $a$、$b$、$c$ 满足 $ab=a+2b$，$abc=a+2b+c$，则 $c$ 的最大值为 ____',
  opts=[],
  answer=r'$\frac{8}{7}$',
  solution=r'由 $abc=a+2b+c$ 得 $c(ab-1)=a+2b=ab$，故 $c=\frac{ab}{ab-1}=1+\frac{1}{ab-1}$。'
           r'由 $ab=a+2b\geq 2\sqrt{2ab}$ 得 $\sqrt{ab}\geq 2\sqrt{2}$，即 $ab\geq 8$，'
           r'当且仅当 $a=2b$ 时取等号。'
           r'因 $c=1+\frac{1}{ab-1}$ 关于 $ab$ 单调递减，故当 $ab=8$ 时 $c$ 取最大值 '
           r'$\frac{8}{7}$，此时 $a=4$、$b=2$。',
  review=''),

# ---------------- T022 恒成立求参数型 (p236) ----------------
dict(topic='M-T-022', key='M-T-022-E1', kind='典例', type='选择',
  stem_text=r'对任意正实数 $a$、$b$，不等式 $\frac{a+b}{2}\lambda+\frac{2ab(1-\lambda)}{a+b}\geq\sqrt{ab}$ '
            r'恒成立，则（　　）',
  opts=[('A', r'实数 $\lambda$ 有最小值 $1$'), ('B', r'实数 $\lambda$ 有最大值 $1$'),
        ('C', r'实数 $\lambda$ 有最小值 $\frac{1}{2}$'),
        ('D', r'实数 $\lambda$ 有最大值 $\frac{1}{2}$')],
  answer='C',
  solution=r'整理得 $\lambda\left(\frac{a+b}{2}-\frac{2ab}{a+b}\right)\geq\sqrt{ab}-\frac{2ab}{a+b}$。'
           r'其中 $\frac{a+b}{2}-\frac{2ab}{a+b}=\frac{(a-b)^{2}}{2(a+b)}\geq 0$。'
           r'当 $a=b$ 时两边均为 $0$，不等式恒成立；'
           r'当 $a\neq b$ 时，$\lambda\geq\frac{2\sqrt{ab}}{(\sqrt{a}+\sqrt{b})^{2}}$。'
           r'由 $(\sqrt{a}+\sqrt{b})^{2}\geq 4\sqrt{ab}$ 得 '
           r'$\frac{2\sqrt{ab}}{(\sqrt{a}+\sqrt{b})^{2}}\leq\frac{1}{2}$，'
           r'且 $a\neq b$ 时严格小于 $\frac{1}{2}$（上确界为 $\frac{1}{2}$）。'
           r'取 $\lambda=\frac{1}{2}$ 直接验证：'
           r'$\frac{a+b}{4}+\frac{ab}{a+b}-\sqrt{ab}=\frac{(a+b-2\sqrt{ab})^{2}}{4(a+b)}\geq 0$ 成立。'
           r'故 $\lambda$ 有最小值 $\frac{1}{2}$，选 C。',
  review=''),

dict(topic='M-T-022', key='M-T-022-V1', kind='变式1', type='选择',
  stem_text=r'设正实数 $x$、$y$ 满足 $x>\frac{1}{2}$，$y>1$，不等式 '
            r'$\frac{4x^{2}}{y-1}+\frac{y^{2}}{2x-1}\geq m$ 恒成立，则 $m$ 的最大值为（　　）',
  opts=[('A', r'$8$'), ('B', r'$16$'), ('C', r'$2\sqrt{2}$'), ('D', r'$4\sqrt{2}$')],
  answer='A',
  solution=r'令 $a=2x-1>0$，$b=y-1>0$，则 $x=\frac{a+1}{2}$，$y=b+1$，'
           r'原式化为 $\frac{(a+1)^{2}}{b}+\frac{(b+1)^{2}}{a}$。'
           r'由柯西不等式 $\frac{(a+1)^{2}}{b}+\frac{(b+1)^{2}}{a}\geq\frac{(a+b+2)^{2}}{a+b}$。'
           r'记 $s=a+b$，则 $\frac{(s+2)^{2}}{s}=s+4+\frac{4}{s}\geq 4+2\sqrt{s\cdot\frac{4}{s}}=8$，'
           r'当且仅当 $s=2$ 且 $\frac{a+1}{b}=\frac{b+1}{a}$，即 $a=b=1$ 时取等号，'
           r'此时 $x=1$、$y=2$。故最小值是 $8$，$m$ 的最大值为 $8$，选 A。',
  review='原书解析取等处写「$x=2$，$y=1$」有误，应为 $x=1$、$y=2$'
         '（由 $a=b=1$ 得 $x=\\frac{a+1}{2}=1$、$y=b+1=2$）。'
         '代入验证：$\\frac{4\\cdot1}{2-1}+\\frac{4}{2-1}=8$，答案 A 不受影响。'),

dict(topic='M-T-022', key='M-T-022-V2', kind='变式2', type='选择',
  stem_text=r'正数 $a$、$b$ 满足 $a+b=1$，若不等式 $\frac{1}{a}+\frac{4}{b}\geq x^{2}+4x+3+m$ '
            r'对 $\forall x\in[-3,0]$，$a,b\in\mathbb{R}^{+}$ 恒成立，'
            r'则实数 $m$ 的取值范围是（　　）',
  opts=[('A', r'$(3,+\infty)$'), ('B', r'$(-\infty,3)$'),
        ('C', r'$(-\infty,6)$'), ('D', r'$(6,+\infty)$')],
  answer='C',
  solution=r'$\frac{1}{a}+\frac{4}{b}=(a+b)\left(\frac{1}{a}+\frac{4}{b}\right)'
           r'=5+\frac{b}{a}+\frac{4a}{b}\geq 5+2\sqrt{4}=9$，'
           r'当 $a=\frac{1}{3}$、$b=\frac{2}{3}$ 时取等号。'
           r'故需 $9\geq x^{2}+4x+3+m$ 对 $\forall x\in[-3,0]$ 恒成立，'
           r'即 $f(x)=x^{2}+4x-6+m\leq 0$ 在 $[-3,0]$ 上恒成立。'
           r'$f$ 的对称轴为 $x=-2$，区间端点处 $f(-3)=m-9$，$f(0)=m-6$，'
           r'最大值为 $f(0)=m-6$，故 $m-6\leq 0$，即 $m\leq 6$。'
           r'所以 $m\in(-\infty,6]$，选 C。',
  review='选项 C 印刷为 $(-\\infty,6)$，严格应为 $(-\\infty,6]$（$m=6$ 时 '
         '$f(0)=0$ 仍满足 $\\leq0$）。答案 C 不受影响。'),

dict(topic='M-T-022', key='M-T-022-V3', kind='变式3', type='解答',
  stem_text=r'设 $x$、$y$ 都是正数，且使 $\sqrt{x}+\sqrt{y}=k\sqrt{x+y}$，求实数 $k$ 的最大值。',
  opts=[],
  answer=r'$\sqrt{2}$',
  solution=r'由题设 $k=\frac{\sqrt{x}+\sqrt{y}}{\sqrt{x+y}}$，两边平方得 '
           r'$k^{2}=\frac{x+y+2\sqrt{xy}}{x+y}=1+\frac{2\sqrt{xy}}{x+y}$。'
           r'由 $x+y\geq 2\sqrt{xy}$ 得 $\frac{2\sqrt{xy}}{x+y}\leq 1$，故 $k^{2}\leq 2$。'
           r'又 $k>0$，所以 $0<k\leq\sqrt{2}$，当且仅当 $x=y$ 时取等号。'
           r'故 $k$ 的最大值为 $\sqrt{2}$。',
  review='PDF 提取时根号丢失（原文 $\\sqrt{x}+\\sqrt{y}=k\\sqrt{x+y}$ 被提取成 '
         '"x + y = k x + y"），ref_bank 中答案存为 "2." 亦缺根号。'
         '已按数学含义重建为 $\\sqrt{2}$（数值扫描确认 1.414214）。'),
]

if __name__ == '__main__':
    print('共 %d 题' % len(QS))
