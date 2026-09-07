# -*- coding: utf-8 -*-
r"""第4批录入数据：T017 换元型 / T018 和积系数不一致 / T019 均值裂项 / T020 同乘方程。

来源：2024高中数学热点题型归纳完整解析版.pdf p234~p235
      —— 逐题读原文重建，13 题答案全部独立验算通过。

**LaTeX 相关字符串一律 raw 前缀**。'\v'、'\b'、'\n' 在普通字符串里是
转义字符，会把题目污染成控制字符且完全看不出原因（已踩三次）。

本批两处需要标注：
  T019-V3  原书答案 5√5/2 有误，正确答案 √5+√(10√5)（数值+解析双重确认）
  T020-E1  ref_bank 提取时题干前半被截断，已按 PDF 原文补全
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'py'))

QS = [
# ---------------- T017 换元型 (p236) ----------------
dict(topic='M-T-017', key='M-T-017-E1', kind='典例', type='选择',
  stem_text=r'已知实数 $x$、$y$ 满足方程 $x^{2}+y^{2}+2x-2y=0$，则 $|x|+|y|$ 的最大值为（　　）',
  opts=[('A', r'$2$'), ('B', r'$4$'), ('C', r'$3\sqrt{2}$'), ('D', r'$2+\sqrt{2}$')],
  answer='B',
  solution=r'方程化为 $(x+1)^{2}+(y-1)^{2}=2$，令 $x=\sqrt{2}\cos\theta-1$，$y=\sqrt{2}\sin\theta+1$。'
           r'$x^{2}+y^{2}=2\cos^{2}\theta+2\sin^{2}\theta+2\sqrt{2}(\sin\theta-\cos\theta)+2'
           r'=4+4\sin\left(\theta-\frac{\pi}{4}\right)\leq 8$。'
           r'由 $\left(\frac{|x|+|y|}{2}\right)^{2}\leq\frac{x^{2}+y^{2}}{2}$ 得 '
           r'$(|x|+|y|)^{2}\leq 2(x^{2}+y^{2})\leq 16$，故 $|x|+|y|\leq 4$，'
           r'当 $\theta=\frac{3\pi}{4}$ 即 $x=-2$、$y=2$ 时取等号。故选 B。',
  review=''),

# 第28题：原 PDF 无【答案】标记（答案写在详解末尾），ref_bank 提取时被过滤，此处补录
dict(topic='M-T-017', key='M-T-017-V0', kind='变式补录', type='填空',
  stem_text=r'若 $a$、$b\in\mathbb{R}$，且 $a^{2}+2ab-3b^{2}=1$，则 $a^{2}+b^{2}$ 的最小值为 ____',
  opts=[],
  answer=r'$\frac{\sqrt{5}+1}{4}$',
  solution=r'由 $a^{2}+2ab-3b^{2}=1$ 得 $(a+3b)(a-b)=1$。'
           r'令 $x=a+3b$，$y=a-b$，则 $xy=1$，且 $a=\frac{x+3y}{4}$，$b=\frac{x-y}{4}$。'
           r'$a^{2}+b^{2}=\frac{(x+3y)^{2}+(x-y)^{2}}{16}=\frac{2x^{2}+4xy+10y^{2}}{16}'
           r'=\frac{x^{2}+2xy+5y^{2}}{8}$。'
           r'由 $xy=1$ 得 $x^{2}+5y^{2}\geq 2\sqrt{5}xy=2\sqrt{5}$，'
           r'故 $a^{2}+b^{2}\geq\frac{2\sqrt{5}+2}{8}=\frac{\sqrt{5}+1}{4}$，'
           r'当且仅当 $x^{2}=5y^{2}$ 即 $x^{2}=\sqrt{5}$ 时取等号。',
  review='原 PDF 该题答案写在详解末尾、无【答案】标记，ref_bank 提取时被过滤，此为补录。'),

dict(topic='M-T-017', key='M-T-017-V1', kind='变式1', type='填空',
  stem_text=r'已知 $x^{2}-2\sqrt{3}xy+5y^{2}=1$，$x$、$y\in\mathbb{R}$，则 $x^{2}+y^{2}$ 的最小值为 ____',
  opts=[],
  answer=r'$\frac{3-\sqrt{7}}{2}$',
  solution=r'$x^{2}-2\sqrt{3}xy+5y^{2}=(x-\sqrt{3}y)^{2}+2y^{2}=1$，'
           r'令 $x-\sqrt{3}y=\cos\theta$，$\sqrt{2}y=\sin\theta$，'
           r'则 $y=\frac{\sqrt{2}}{2}\sin\theta$，$x=\cos\theta+\frac{\sqrt{6}}{2}\sin\theta$。'
           r'$x^{2}+y^{2}=\left(\cos\theta+\frac{\sqrt{6}}{2}\sin\theta\right)^{2}'
           r'+\frac{1}{2}\sin^{2}\theta'
           r'=\cos^{2}\theta+\sqrt{6}\sin\theta\cos\theta+2\sin^{2}\theta'
           r'=1+\frac{1-\cos 2\theta}{2}+\frac{\sqrt{6}}{2}\sin 2\theta'
           r'=\frac{3}{2}-\frac{1}{2}\cos 2\theta+\frac{\sqrt{6}}{2}\sin 2\theta'
           r'=\frac{3}{2}+\frac{\sqrt{7}}{2}\sin(2\theta-\varphi)$。'
           r'故最小值为 $\frac{3-\sqrt{7}}{2}$。',
  review=''),

dict(topic='M-T-017', key='M-T-017-V2', kind='变式2', type='填空',
  stem_text=r'已知 $x$、$y$ 为正实数，则 $\frac{x}{x+2y}+\frac{2x+y}{x}$ 的最小值为 ____',
  opts=[],
  answer=r'$\frac{3}{2}+\sqrt{2}$',
  solution=r'令 $t=\frac{y}{x}>0$，则 $\frac{x}{x+2y}=\frac{1}{1+2t}$，$\frac{2x+y}{x}=2+t$。'
           r'原式 $=\frac{1}{1+2t}+t+2=\frac{1}{1+2t}+\frac{1+2t}{2}+\frac{3}{2}$'
           r'$\geq 2\sqrt{\frac{1}{1+2t}\cdot\frac{1+2t}{2}}+\frac{3}{2}=\sqrt{2}+\frac{3}{2}$，'
           r'当且仅当 $\frac{1}{1+2t}=\frac{1+2t}{2}$ 即 $t=\frac{\sqrt{2}-1}{2}$ 时取等号。',
  review=''),

# ---------------- T018 和积系数不一致型 (p236) ----------------
# 第32、33题：原 PDF 无【答案】标记，被提取器过滤，补录
# 注：T018-V1（第31题）与 M-T-013-V3 完全重复，跳过
dict(topic='M-T-018', key='M-T-018-V2', kind='变式补录', type='填空',
  stem_text=r'已知正实数 $x$、$y$ 满足 $x^{2}+y^{2}+\frac{1}{x}+\frac{1}{y}=\frac{27}{4}$，'
            r'则 $\frac{15}{x}-\frac{3}{4y}$ 的最小值为 ____',
  opts=[],
  answer=r'$6$',
  solution=r'$\frac{15}{x}-\frac{3}{4y}=\frac{15}{x}-\frac{3}{4y}+\left(x^{2}+y^{2}+\frac{1}{x}+\frac{1}{y}\right)-\frac{27}{4}$'
           r'$=x^{2}+y^{2}+\frac{16}{x}+\frac{1}{4y}-\frac{27}{4}$。'
           r'裂项：$x^{2}+\frac{8}{x}+\frac{8}{x}\geq 3\sqrt[3]{x^{2}\cdot\frac{8}{x}\cdot\frac{8}{x}}=3\sqrt[3]{64}=12$；'
           r'$y^{2}+\frac{1}{8y}+\frac{1}{8y}\geq 3\sqrt[3]{y^{2}\cdot\frac{1}{8y}\cdot\frac{1}{8y}}=3\sqrt[3]{\frac{1}{64}}=\frac{3}{4}$。'
           r'故原式 $\geq 12+\frac{3}{4}-\frac{27}{4}=6$，'
           r'当且仅当 $x=2$、$y=\frac{1}{2}$ 时取等号（代入验证：$4+\frac{1}{4}+\frac{1}{2}+2=\frac{27}{4}$）。',
  review='原 PDF 该题答案写在详解末尾、无【答案】标记，ref_bank 提取时被过滤，此为补录。'),

dict(topic='M-T-018', key='M-T-018-V3', kind='变式补录', type='填空',
  stem_text=r'已知正实数 $x$、$y$ 满足 $x+y+\frac{2}{x}+\frac{6}{y}=8$，则 $x-\frac{2}{y}$ 的最小值为 ____',
  opts=[],
  answer=r'$0$',
  solution=r'$x-\frac{2}{y}=\left(x+y+\frac{2}{x}+\frac{6}{y}\right)+x-\frac{2}{y}-8'
           r'=2x+y+\frac{2}{x}+\frac{4}{y}-8$。'
           r'$\geq 2\sqrt{2x\cdot\frac{2}{x}}+2\sqrt{y\cdot\frac{4}{y}}-8=4+4-8=0$，'
           r'当且仅当 $2x=\frac{2}{x}$ 且 $y=\frac{4}{y}$，即 $x=1$、$y=2$ 时取等号'
           r'（代入验证：$1+2+2+3=8$，满足约束）。',
  review='原 PDF 该题答案写在详解末尾、无【答案】标记，ref_bank 提取时被过滤，此为补录。'),

# ---------------- T019 均值裂项凑配型 (p236) ----------------
dict(topic='M-T-019', key='M-T-019-E1', kind='典例', type='填空',
  stem_text=r'已知实数 $x$、$y$、$z$ 不全为 $0$，则 $w=\frac{y^{2}+2xz}{x^{2}+y^{2}+z^{2}}$ 的最小值是 ____，最大值是 ____',
  opts=[],
  answer=r'$-1$；$1$',
  solution=r'由 $2xz\leq x^{2}+z^{2}$（当且仅当 $x=z$ 时取等号）得 '
           r'$w\leq\frac{y^{2}+x^{2}+z^{2}}{x^{2}+y^{2}+z^{2}}=1$，故最大值为 $1$。'
           r'又 $2xz\geq-(x^{2}+z^{2})$（当且仅当 $x=-z$ 时取等号），'
           r'得 $w\geq\frac{y^{2}-x^{2}-z^{2}}{x^{2}+y^{2}+z^{2}}\geq -1$，'
           r'当 $y=0$ 且 $x=-z$ 时取等号，故最小值为 $-1$。',
  review=''),

dict(topic='M-T-019', key='M-T-019-V1', kind='变式1', type='填空',
  stem_text=r'不等式 $\frac{xy+yz}{x^{2}+2y^{2}+z^{2}}\leq 1+\frac{1}{2}a-a^{2}$ 对任意正数 $x$、$y$、$z$ 恒成立，'
            r'则 $a$ 的最大值是 ____',
  opts=[],
  answer=r'$1$',
  solution=r'$\frac{xy+yz}{x^{2}+2y^{2}+z^{2}}=\frac{y(x+z)}{(x^{2}+y^{2})+(y^{2}+z^{2})}'
           r'\leq\frac{y(x+z)}{2xy+2yz}=\frac{1}{2}$，当且仅当 $x=y=z$ 时取等号。'
           r'故需 $1+\frac{1}{2}a-a^{2}\geq\frac{1}{2}$，即 $2a^{2}-a-1\leq 0$，'
           r'解得 $-\frac{1}{2}\leq a\leq 1$，所以 $a$ 的最大值为 $1$。',
  review=''),

dict(topic='M-T-019', key='M-T-019-V2', kind='变式2', type='填空',
  stem_text=r'已知实数 $a$、$b$、$c$ 满足 $a^{2}-8a-bc+7=0$，$b^{2}+c^{2}+bc-6a+6=0$，'
            r'则实数 $a$ 的取值范围是 ____',
  opts=[],
  answer=r'$[1,9]$',
  solution=r'由 $a^{2}-8a-bc+7=0$ 得 $bc=a^{2}-8a+7$；'
           r'由 $b^{2}+c^{2}+bc-6a+6=0$ 得 $b^{2}+c^{2}+bc=6a-6$。'
           r'$(b+c)^{2}=(b^{2}+c^{2}+bc)+bc=(6a-6)+(a^{2}-8a+7)=a^{2}-2a+1=(a-1)^{2}$。'
           r'由 $(b+c)^{2}\geq 4bc$ 得 $(a-1)^{2}\geq 4(a^{2}-8a+7)$，'
           r'即 $a^{2}-2a+1\geq 4a^{2}-32a+28$，整理得 $3a^{2}-30a+27\leq 0$，'
           r'即 $a^{2}-10a+9\leq 0$，解得 $1\leq a\leq 9$。',
  review=''),

dict(topic='M-T-019', key='M-T-019-V3', kind='变式3', type='填空',
  stem_text=r'已知 $a>0$，$b>0$，$c\geq 4$，且 $a+b=2$，则 $\frac{ac}{b}+\frac{c}{ab}-\frac{c}{2}+\frac{5}{c-2}$ '
            r'的最小值为 ____',
  opts=[],
  answer=r'$\sqrt{5}+\sqrt{10\sqrt{5}}$',
  solution=r'原式 $=c\left(\frac{a}{b}+\frac{1}{ab}-\frac{1}{2}\right)+\frac{5}{c-2}'
           r'=c\cdot\frac{2a^{2}+2-ab}{2ab}+\frac{5}{c-2}$。'
           r'由 $a+b=2$ 得 $2=\frac{(a+b)^{2}}{2}$，故 '
           r'$\frac{2a^{2}+2-ab}{2ab}=\frac{2a^{2}+\frac{(a+b)^{2}}{2}-ab}{2ab}'
           r'=\frac{5a^{2}+b^{2}}{4ab}\geq\frac{2\sqrt{5}ab}{4ab}=\frac{\sqrt{5}}{2}$，'
           r'当且仅当 $b=\sqrt{5}a$ 时取等号。'
           r'令 $t=c-2\geq 2$，则原式 $\geq\frac{\sqrt{5}}{2}(t+2)+\frac{5}{t}'
           r'=\sqrt{5}\left(\frac{t}{2}+\frac{\sqrt{5}}{t}+1\right)$。'
           r'设 $f(t)=\frac{t}{2}+\frac{\sqrt{5}}{t}+1$，由 $f\'(t)=\frac{1}{2}-\frac{\sqrt{5}}{t^{2}}=0$ '
           r'得 $t=\sqrt{2\sqrt{5}}\approx 2.115>2$，此时 $f$ 取最小值 '
           r'$2\sqrt{\frac{\sqrt{5}}{2}}+1$（因 $\frac{t}{2}=\frac{\sqrt{5}}{t}$）。'
           r'故最小值为 $\sqrt{5}\left(2\sqrt{\frac{\sqrt{5}}{2}}+1\right)'
           r'=\sqrt{5}+\sqrt{10\sqrt{5}}\approx 6.9648$。',
  review='**原书答案 $\\frac{5\\sqrt{5}}{2}\\approx5.590$ 有误**。'
         '错在把 $\\frac{5}{c-2}$ 提出 $\\sqrt{5}$ 后写成 $\\frac{1}{t}$（应为 $\\frac{\\sqrt{5}}{t}$，'
         '因 $\\frac{5}{\\sqrt{5}}=\\sqrt{5}$）。正确最小值 $\\sqrt{5}+\\sqrt{10\\sqrt{5}}\\approx6.9648$，'
         '取等 $a=\\frac{2}{1+\\sqrt{5}}\\approx0.618$、$b\\approx1.382$、$c=2+\\sqrt{2\\sqrt{5}}\\approx4.115\\geq4$。'
         '数值扫描与解析推导结果一致（6.964776）。'),

# ---------------- T020 整体化同乘方程型 (p236) ----------------
dict(topic='M-T-020', key='M-T-020-E1', kind='典例', type='填空',
  stem_text=r'已知实数 $x$、$y$ 满足 $x>1$，$y>0$，且 $x+4y+\frac{1}{x-1}+\frac{1}{y}=11$，'
            r'则 $\frac{1}{x-1}+\frac{1}{y}$ 的最大值为 ____',
  opts=[],
  answer=r'$9$',
  solution=r'条件化为 $(x-1)+4y+\frac{1}{x-1}+\frac{1}{y}=10$。'
           r'令 $a=x-1>0$，$b=y>0$，$t=\frac{1}{a}+\frac{1}{b}$，则 $a+4b=10-t$。'
           r'$t(a+4b)=\left(\frac{1}{a}+\frac{1}{b}\right)(a+4b)=5+\frac{4b}{a}+\frac{a}{b}'
           r'\geq 5+2\sqrt{4}=9$，'
           r'即 $t(10-t)\geq 9$，解得 $1\leq t\leq 9$。故 $t$ 的最大值为 $9$，'
           r'当 $\frac{4b}{a}=\frac{a}{b}$ 且 $a+4b=1$，即 $a=\frac{1}{3}$、$b=\frac{1}{6}$ '
           r'（$x=\frac{4}{3}$、$y=\frac{1}{6}$）时取等号。',
  review='ref_bank 提取时题干前半被截断（仅剩「则 $\\frac{1}{x-1}+\\frac{1}{y}$ 的最大值为」），'
         '已按 PDF 原文补全条件部分。'),

dict(topic='M-T-020', key='M-T-020-V1', kind='变式1', type='填空',
  stem_text=r'已知正数 $x$、$y$ 满足 $x+y+\frac{1}{x}+\frac{9}{y}=10$，则 $x+y$ 的最大值为 ____',
  opts=[],
  answer=r'$8$',
  solution=r'令 $s=x+y$，则 $\frac{1}{x}+\frac{9}{y}=10-s$。'
           r'$s(10-s)=(x+y)\left(\frac{1}{x}+\frac{9}{y}\right)=10+\frac{9x}{y}+\frac{y}{x}'
           r'\geq 10+2\sqrt{9}=16$。'
           r'即 $s^{2}-10s+16\leq 0$，解得 $2\leq s\leq 8$。故 $x+y$ 的最大值为 $8$，'
           r'当 $\frac{9x}{y}=\frac{y}{x}$ 且 $x+y=8$，即 $x=2$、$y=6$ 时取等号。',
  review=''),

dict(topic='M-T-020', key='M-T-020-V2', kind='变式2', type='填空',
  stem_text=r'已知 $x$、$y$ 为正数，且 $x+\frac{1}{x}+3y+\frac{3}{y}=10$，则 $x+3y$ 的最大值为 ____',
  opts=[],
  answer=r'$8$',
  solution=r'令 $t=x+3y$，则 $\frac{1}{x}+\frac{3}{y}=10-t$。'
           r'$t(10-t)=(x+3y)\left(\frac{1}{x}+\frac{3}{y}\right)=10+\frac{3x}{y}+\frac{3y}{x}'
           r'\geq 10+2\sqrt{9}=16$。'
           r'即 $t^{2}-10t+16\leq 0$，解得 $2\leq t\leq 8$。故 $x+3y$ 的最大值为 $8$，'
           r'当 $x=y$ 且 $x+3y=8$，即 $x=2$、$y=2$ 时取等号。',
  review=''),
]

if __name__ == '__main__':
    print('共 %d 题' % len(QS))
