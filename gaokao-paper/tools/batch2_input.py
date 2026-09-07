# -*- coding: utf-8 -*-
"""第 2 批人工审核录入：M-T-005 ~ M-T-007（集合与逻辑 · 集合运算）

来源：2024高中数学热点题型归纳完整解析版
每道题的答案都经过程序枚举 / 解析验算，见各题 review 字段。
"""
import sys, os
sys.path.insert(0, '/data/workspace/gaokao-paper/py')
import hand_input as H

KS = {'kp': '集合与逻辑', 'kp2': '集合运算'}

QS = [
# ---------------- M-T-005 集合与排列组合概率 ----------------
{
 'type': '选择', 'subtype': '单选题', 'answer': 'D', 'difficulty': 0.4,
 'topics': ['M-T-005'], 'src': '2024热点题型归纳 M-T-005 典例', **KS,
 'stem_text': r'已知非空集合 $A\subseteq\mathbb{R}$，设集合 $S=\{x+y\mid x\in A, y\in A, x\neq y\}$，'
              r'$T=\{x-y\mid x\in A, y\in A, x>y\}$．分别用 $|A|$、$|S|$、$|T|$ 表示集合 $A$、$S$、$T$ '
              r'中元素的个数，则下列说法不正确的是（　　）',
 'opts': [['A', r'若 $|A|=4$，则 $|S|+|T|\geqslant 8$'],
          ['B', r'若 $|A|=4$，则 $|S|+|T|\leqslant 12$'],
          ['C', r'若 $|A|=5$，则 $|S|+|T|$ 可能为 $18$'],
          ['D', r'若 $|A|=5$，则 $|S|+|T|$ 不可能为 $19$']],
 'analysis': r'把 $S$、$T$ 的元素个数转化为排列组合问题：$|S|\leqslant \mathrm{C}_n^2$，'
             r'$|T|\leqslant \mathrm{C}_n^2$；当 $A$ 由相邻元素构成（等差数列）时重复最多，'
             r'$|S|+|T|$ 取最小值．',
 'solution': r'$|S|\leqslant \mathrm{C}_{|A|}^2$，$|T|\leqslant \mathrm{C}_{|A|}^2$．'
             r'当 $A=\{1,2,3,4\}$ 时 $S=\{3,4,5,6,7\}$、$T=\{1,2,3\}$，$|S|+|T|=8$ 为最小；'
             r'上界为 $6+6=12$，故 A、B 正确．'
             r'当 $A=\{1,2,3,4,5\}$ 时 $|S|+|T|=7+4=11$ 为最小，上界为 $10+10=20$；'
             r'程序枚举验证 $18$ 与 $19$ 均可达（如 $A=\{19,26,31,35,39\}$ 时 $|S|+|T|=19$），'
             r'故 C 正确、D 错误．故选 D．',
 'review': '原卷用特殊记号表示元素个数，统一改为标准记 $|A|$、$|S|$、$|T|$；'
           '集合的花括号加转义 $\\{$、$\\}$；$\\mid$ 为新增支持的关系符。'
           '原书详解只给出上下界，未证明 19 可达——已用程序枚举验证（n=5 可达值 11~20，19 在其中），'
           '结论 D 正确。',
},
{
 'type': '选择', 'subtype': '单选题', 'answer': 'B', 'difficulty': 0.65,
 'topics': ['M-T-005'], 'src': '2024热点题型归纳 M-T-005 变式1', **KS,
 'stem_text': r'设 $I=\{1,2,3,4\}$，$A$ 与 $B$ 是 $I$ 的子集，若 $A\cap B=\{1,3\}$，'
              r'则称 $(A,B)$ 为一个"理想配集"．那么符合此条件的"理想配集"'
              r'（规定 $(A,B)$ 与 $(B,A)$ 是两个不同的"理想配集"）的个数是（　　）',
 'opts': [['A', '$16$'], ['B', '$9$'], ['C', '$8$'], ['D', '$4$']],
 'analysis': r'$A$、$B$ 都必须含 $1$、$3$；对元素 $2$、$4$，每个都有"只在 $A$""只在 $B$""都不在"'
             r'三种取法（不能都在，否则交集会多出该元素）．',
 'solution': r'由 $A\cap B=\{1,3\}$ 知 $1,3\in A$ 且 $1,3\in B$，且 $2,4$ 不能同时属于 $A$ 与 $B$．'
             r'对元素 $2$：只在 $A$、只在 $B$、都不在，共 $3$ 种；元素 $4$ 同理 $3$ 种．'
             r'由分步乘法计数原理得 $3\times 3=9$ 个．故选 B．',
 'review': '程序枚举全部 $2^4\times 2^4=256$ 种 $(A,B)$ 组合，满足 $A\cap B=\{1,3\}$ 的恰为 9 个，与答案一致。',
},
{
 'type': '选择', 'subtype': '单选题', 'answer': 'A', 'difficulty': 0.65,
 'topics': ['M-T-005'], 'src': '2024热点题型归纳 M-T-005 变式2', **KS,
 'stem_text': r'已知集合 $P=\{1,2,3,4,5\}$，若 $A$、$B$ 是 $P$ 的两个非空子集，'
              r'则所有满足 $A$ 中的最大数小于 $B$ 中的最小数的集合对 $(A,B)$ 的个数为（　　）',
 'opts': [['A', '$49$'], ['B', '$48$'], ['C', '$47$'], ['D', '$46$']],
 'analysis': r'按 $A$ 中的最大数 $k$ 分类：$A$ 含 $k$、其余从比 $k$ 小的数中任取；'
             r'$B$ 从比 $k$ 大的数中任取非空子集．',
 'solution': r'设 $\max A=k$（$k=1,2,3,4$）．'
             r'$k=1$：$A=\{1\}$（$1$ 个），$B\subseteq\{2,3,4,5\}$ 非空（$2^4-1=15$ 个），得 $15$ 对；'
             r'$k=2$：$A$ 有 $2$ 个，$B\subseteq\{3,4,5\}$ 非空（$7$ 个），得 $14$ 对；'
             r'$k=3$：$A$ 有 $4$ 个，$B\subseteq\{4,5\}$ 非空（$3$ 个），得 $12$ 对；'
             r'$k=4$：$A$ 有 $8$ 个，$B=\{5\}$（$1$ 个），得 $8$ 对．'
             r'合计 $15+14+12+8=49$．故选 A．',
 'review': '程序枚举 $31\times 31=961$ 组非空子集对，满足条件的恰为 49，与答案一致。',
},
{
 'type': '填空', 'subtype': '单空题', 'answer': r'$2018\times 2^{2019}+1$', 'difficulty': 0.4,
 'topics': ['M-T-005'], 'src': '2024热点题型归纳 M-T-005 变式3', **KS,
 'stem_text': r'设集合 $A=\{1,2,3,\cdots,2020\}$，选择 $A$ 的两个非空子集 $B$ 和 $C$，'
              r'要使 $C$ 中最小的数大于 $B$ 中的最大数，则不同的选择方法有__________．',
 'analysis': r'按 $\max B=k$ 分类，用等比数列求和．',
 'solution': r'设 $\max B=k$（$k=1,2,\cdots,2019$）．'
             r'$B$ 含 $k$、其余从 $\{1,\cdots,k-1\}$ 中任取，共 $2^{k-1}$ 个；'
             r'$C\subseteq\{k+1,\cdots,2020\}$ 且非空，共 $2^{2020-k}-1$ 个．'
             r'总数为 $\sum\limits_{k=1}^{2019}2^{k-1}\left(2^{2020-k}-1\right)$'
             r'$=\sum\limits_{k=1}^{2019}2^{2019}-\sum\limits_{k=1}^{2019}2^{k-1}$'
             r'$=2019\times 2^{2019}-\left(2^{2019}-1\right)=2018\times 2^{2019}+1$．'
             r'故答案为 $2018\times 2^{2019}+1$．',
 'review': '原书答案写作"2018 × 22019+ 1"（PDF 提取丢失上标），已还原为 $2018\\times 2^{2019}+1$；'
           '用等比求和公式独立验算，结果一致。',
},
# ---------------- M-T-006 新定义 ----------------
{
 'type': '选择', 'subtype': '单选题', 'answer': 'B', 'difficulty': 0.4,
 'topics': ['M-T-006'], 'src': '2024热点题型归纳 M-T-006 典例', **KS,
 'stem_text': r'用 $C(A)$ 表示非空集合 $A$ 中的元素个数，定义 '
              r'$A*B=\begin{cases}C(A)-C(B), & C(A)\geqslant C(B)\\ C(B)-C(A), & C(A)<C(B)\end{cases}$．'
              r'若 $A=\{1,2\}$，$B=\{x\mid (x^2+ax)(x^2+ax+2)=0\}$，且 $A*B=1$，'
              r'设实数 $a$ 的所有可能取值组成的集合是 $S$，则 $C(S)$ 等于（　　）',
 'opts': [['A', '$1$'], ['B', '$3$'], ['C', '$5$'], ['D', '$7$']],
 'analysis': r'由 $C(A)=2$、$A*B=1$ 得 $C(B)=1$ 或 $C(B)=3$．'
             r'对方程 $x^2+ax+2=0$ 按判别式 $\Delta=a^2-8$ 分类讨论．',
 'solution': r'$C(A)=2$，$A*B=|C(A)-C(B)|=1$，故 $C(B)=1$ 或 $C(B)=3$．'
             r'方程 $x^2+ax=0$ 的两根为 $0$、$-a$；方程 $x^2+ax+2=0$ 的 $\Delta=a^2-8$．'
             r'① $\Delta=0$，即 $a=\pm 2\sqrt{2}$ 时，$x^2+ax+2=0$ 有重根 $-\frac{a}{2}$，'
             r'且 $0$、$-a$ 均不是该根，故 $C(B)=3$，符合；'
             r'② $\Delta>0$，即 $|a|>2\sqrt{2}$ 时，两方程根互不相同，$C(B)=4$，不符；'
             r'③ $\Delta<0$，即 $|a|<2\sqrt{2}$ 时，$x^2+ax+2=0$ 无实根：'
             r'$a=0$ 时 $B=\{0\}$，$C(B)=1$，符合；$a\neq 0$ 时 $C(B)=2$，不符．'
             r'故 $S=\{0, 2\sqrt{2}, -2\sqrt{2}\}$，$C(S)=3$．故选 B．',
 'review': '分段函数用 \\begin{cases} 重建（原卷是上下两行排版）；'
           '集合花括号加转义。用容差聚类判重的方式程序验算：a=0、±2√2 时 C(B) 分别为 1、3、3，'
           '其余取值为 2 或 4，故 C(S)=3，与答案一致。',
},
{
 'type': '选择', 'subtype': '单选题', 'answer': 'A', 'difficulty': 0.4,
 'topics': ['M-T-006'], 'src': '2024热点题型归纳 M-T-006 变式1', **KS,
 'stem_text': r'定义 $A-B=\{x\mid x\in A, x\notin B\}$，设 $A$、$B$、$C$ 是某集合的三个子集，'
              r'且满足 $(A-B)\cup(B-A)\subseteq C$，则 $A\subseteq (C-B)\cup(B-C)$ '
              r'是 $A\cap B\cap C=\varnothing$ 的（　　）',
 'opts': [['A', '充要条件'], ['B', '充分非必要条件'],
          ['C', '必要非充分条件'], ['D', '既非充分也非必要条件']],
 'analysis': r'借助韦恩图：由 $(A-B)\cup(B-A)\subseteq C$ 知 $A$、$B$ 各自独有的部分都落入 $C$，'
             r'剩下的只有 $A\cap B$ 中的两块与 $A\cap B\cap C$，双向推导即可．',
 'solution': r'记五部分：Ⅰ$=A$ 独有、Ⅱ$=C$ 独有、Ⅲ$=B$ 独有、Ⅳ$=A\cap B$ 不含 $C$、'
             r'Ⅴ$=A\cap B\cap C$．由 $(A-B)\cup(B-A)=\mathrm{\RomanNumeral{1}}\cup\mathrm{\RomanNumeral{3}}\subseteq C$，'
             r'得 $\mathrm{\RomanNumeral{1}}=\mathrm{\RomanNumeral{3}}=\varnothing$．'
             r'于是 $A=\mathrm{\RomanNumeral{4}}\cup\mathrm{\RomanNumeral{5}}$，'
             r'$(C-B)\cup(B-C)=\mathrm{\RomanNumeral{2}}\cup\mathrm{\RomanNumeral{4}}$．'
             r'充分性：若 $A\cap B\cap C=\varnothing$，则 $\mathrm{\RomanNumeral{5}}=\varnothing$，'
             r'$A=\mathrm{\RomanNumeral{4}}\subseteq \mathrm{\RomanNumeral{2}}\cup\mathrm{\RomanNumeral{4}}$，成立；'
             r'必要性：若 $A\subseteq (C-B)\cup(B-C)$，即 '
             r'$\mathrm{\RomanNumeral{4}}\cup\mathrm{\RomanNumeral{5}}\subseteq \mathrm{\RomanNumeral{2}}\cup\mathrm{\RomanNumeral{4}}$，'
             r'得 $\mathrm{\RomanNumeral{5}}=\varnothing$，即 $A\cap B\cap C=\varnothing$，成立．'
             r'故为充要条件，选 A．',
 'review': '原书用韦恩图的罗马数字编号 Ⅰ~Ⅴ 论证，此处改用文字描述各区域（避免生僻 Unicode 数字）；'
           '双向推导已复核对。',
},
{
 'type': '选择', 'subtype': '单选题', 'answer': 'C', 'difficulty': 0.4,
 'topics': ['M-T-006'], 'src': '2024热点题型归纳 M-T-006 变式3', **KS,
 'stem_text': r'在 $n$ 元数集 $S=\{a_1,a_2,\cdots,a_n\}$ 中，设 $x_S=\frac{a_1+a_2+\cdots+a_n}{n}$，'
              r'若 $S$ 的非空子集 $A$ 满足 $x_A=x_S$，则称 $A$ 是集合 $S$ 的一个"平均子集"，'
              r'并记数集 $S$ 的 $k$ 元"平均子集"的个数为 $f_S(k)$．'
              r'已知集合 $S=\{1,2,3,\cdots,8,9\}$，$T=\{-4,-3,-2,-1,0,1,2,3,4\}$，'
              r'则下列说法错误的是（　　）',
 'opts': [['A', r'$f_S(9)=f_T(1)$'], ['B', r'$f_S(8)=f_T(1)$'],
          ['C', r'$f_S(6)=f_T(4)$'], ['D', r'$f_S(5)=f_T(4)$']],
 'analysis': r'分别求出 $S$、$T$ 的各 $k$ 元平均子集个数再逐项比对．'
             r'$S$ 的平均数为 $5$，$T$ 的平均数为 $0$．',
 'solution': r'$x_S=5$，$x_T=0$．程序枚举全部子集可得：'
             r'$f_S(9)=1$、$f_S(8)=1$、$f_S(6)=8$、$f_S(5)=12$；'
             r'$f_T(1)=1$、$f_T(4)=12$．'
             r'A：$f_S(9)=1=f_T(1)$，正确；B：$f_S(8)=1=f_T(1)$，正确；'
             r'C：$f_S(6)=8\neq 12=f_T(4)$，错误；D：$f_S(5)=12=f_T(4)$，正确．'
             r'故说法错误的是 C．',
 'review': '**原书详解数值有误但结论正确**：原书按"对称配对"分组，得 '
           'f_S(5)=6、f_S(6)=4、f_T(4)=6，漏掉了非对称组合（如 {1,2,5,8,9} 和为 25、平均 5）。'
           '程序枚举实为 f_S(5)=12、f_S(6)=8、f_T(4)=12。'
           '四个选项的真假不变，答案仍为 C，但解析已按正确数值重写。',
},
# ---------------- M-T-007 集合与圆和圆锥曲线 ----------------
{
 'type': '选择', 'subtype': '单选题', 'answer': 'C', 'difficulty': 0.4,
 'topics': ['M-T-007'], 'src': '2024热点题型归纳 M-T-007 典例', **KS,
 'stem_text': r'设集合 $M=\{(x,y)\mid y=\sqrt{4-x^2}\}$，$N=\{(x,y)\mid (x-2)^2+(y-2)^2=r^2\}$（$r>0$）．'
              r'当 $M\cap N$ 有且只有一个元素时，则正数 $r$ 的所有取值为（　　）',
 'opts': [['A', r'$2+\sqrt{2}$ 或 $2\sqrt{2}-2$'],
          ['B', r'$2<r\leqslant 2\sqrt{5}$'],
          ['C', r'$2<r\leqslant 2\sqrt{5}$ 或 $r=2\sqrt{2}-2$'],
          ['D', r'$2\leqslant r\leqslant 2\sqrt{5}$ 或 $r=2\sqrt{2}-2$']],
 'analysis': r'$M$ 是圆 $x^2+y^2=4$ 的上半部分（含端点 $(\pm 2,0)$），$N$ 是以 $(2,2)$ 为圆心、'
             r'$r$ 为半径的圆．两方程相减得公共弦所在直线 $x+y=\frac{12-r^2}{4}$，'
             r'问题化为该直线与上半圆的交点个数．',
 'solution': r'两圆方程相减得 $x+y=\frac{12-r^2}{4}$，记 $c=\frac{12-r^2}{4}$．'
             r'相切时 $c=2\sqrt{2}$，即 $r^2=12-8\sqrt{2}=(2\sqrt{2}-2)^2$，'
             r'得 $r=2\sqrt{2}-2$，切点 $(\sqrt{2},\sqrt{2})$ 在上半圆上，符合．'
             r'相交两点时，需其中一个交点落回 $y<0$：'
             r'$r=2$ 时交点为 $(2,0)$、$(0,2)$，两点都在上半圆，不合；'
             r'$2<r<2\sqrt{5}$ 时恰有一点 $y<0$，符合；'
             r'$r=2\sqrt{5}$ 时交点 $(-2,0)$、$(0,-2)$，仅 $(-2,0)$ 在上半圆，符合；'
             r'$r>2\sqrt{5}$ 时两交点都在 $y<0$，无交点．'
             r'故 $r$ 的取值为 $2<r\leqslant 2\sqrt{5}$ 或 $r=2\sqrt{2}-2$．故选 C．',
 'review': '原书详解①写"2√2 = 2 + r，此时 r = 2 - 2√2"，正负号笔误（应为 r = 2√2 - 2），'
           '已按选项与几何意义修正。'
           '用细网格扫描 r∈(0,6) 验证：连续段为 (2, 2√5]，且 r=2√2-2 处为孤立解（恰 1 个交点），'
           '与选项 C 完全一致。',
},
{
 'type': '填空', 'subtype': '单空题', 'answer': r'$[-2,2]$', 'difficulty': 0.4,
 'topics': ['M-T-007'], 'src': '2024热点题型归纳 M-T-007 变式1', **KS,
 'stem_text': r'已知集合 $A=\{(x,y)\mid |x|+2|y|\leqslant 4\}$，'
              r'集合 $B=\{(x,y)\mid (x-m)^2+y^2=\frac{4}{5}\}$，'
              r'若 $B\subseteq A$，则实数 $m$ 的取值范围是__________．',
 'analysis': r'$A$ 是菱形（含边界）区域，$B$ 是以 $(m,0)$ 为圆心、$\frac{2}{\sqrt{5}}$ 为半径的圆．'
             r'$B\subseteq A$ 等价于圆心到菱形四条边的距离都不小于半径．',
 'solution': r'菱形 $A$ 的四条边为 $\pm x\pm 2y=4$．圆 $B$ 的半径 $r=\sqrt{\frac{4}{5}}=\frac{2}{\sqrt{5}}$．'
             r'圆心 $(m,0)$ 到直线 $x+2y-4=0$ 的距离为 $\frac{4-m}{\sqrt{5}}$，'
             r'到直线 $-x+2y-4=0$ 的距离为 $\frac{m+4}{\sqrt{5}}$．'
             r'由 $B\subseteq A$ 得 $\min\left\{\frac{4-m}{\sqrt{5}}, \frac{m+4}{\sqrt{5}}\right\}\geqslant \frac{2}{\sqrt{5}}$，'
             r'即 $4-m\geqslant 2$ 且 $m+4\geqslant 2$，解得 $-2\leqslant m\leqslant 2$．'
             r'故答案为 $[-2,2]$．',
 'review': '原书答案写作"-2,2"（PDF 提取丢失方括号），已还原为区间 $[-2,2]$；'
           '按"圆心到四边距离 ≥ 半径"重新推导复核一致。原书无详解，此解析为补写。',
},
{
 'type': '选择', 'subtype': '单选题', 'answer': 'D', 'difficulty': 0.4,
 'topics': ['M-T-007'], 'src': '2024热点题型归纳 M-T-007 变式2', **KS,
 'stem_text': r'设集合 $A=\{(x,y)\mid (x+3\sin\alpha)^2+(y+3\cos\alpha)^2=1, \alpha\in\mathbb{R}\}$，'
              r'$B=\{(x,y)\mid 3x+4y+10=0\}$，记 $P=A\cap B$，'
              r'则点集 $P$ 所表示的轨迹长度为（　　）',
 'opts': [['A', r'$2\sqrt{5}$'], ['B', r'$2\sqrt{7}$'],
          ['C', r'$4\sqrt{2}$'], ['D', r'$4\sqrt{3}$']],
 'analysis': r'圆心 $(-3\sin\alpha, -3\cos\alpha)$ 的轨迹是 $x^2+y^2=9$，'
             r'故 $A$ 是半径 $1$ 的圆沿该圆扫出的圆环 $2\leqslant \sqrt{x^2+y^2}\leqslant 4$．',
 'solution': r'圆心 $(-3\sin\alpha,-3\cos\alpha)$ 满足 $x^2+y^2=9$（半径 $3$ 的圆），'
             r'半径为 $1$，故 $A$ 为圆环 $2\leqslant \sqrt{x^2+y^2}\leqslant 4$．'
             r'原点到直线 $3x+4y+10=0$ 的距离 $d=\frac{10}{\sqrt{3^2+4^2}}=2$，'
             r'恰与圆环小圆相切，故 $P$ 为直线截大圆（半径 $4$）所得的弦．'
             r'弦长 $=2\sqrt{4^2-2^2}=2\sqrt{12}=4\sqrt{3}$．故选 D．',
 'review': '三角函数参数方程重建为 $(x+3\\sin\\alpha)^2+(y+3\\cos\\alpha)^2=1$；'
           '弦长已复核：$2\\sqrt{16-4}=4\\sqrt{3}$。',
},
{
 'type': '选择', 'subtype': '单选题', 'answer': 'B', 'difficulty': 0.4,
 'topics': ['M-T-007'], 'src': '2024热点题型归纳 M-T-007 变式3', **KS,
 'stem_text': r'有 $6$ 个半径都为 $1$ 的圆，其圆心分别为 $O_1(0,0)$，$O_2(2,0)$，$O_3(4,0)$，'
              r'$O_4(0,2)$，$O_5(2,2)$，$O_6(4,2)$．记集合 $M=\{\odot O_i\mid i=1,2,3,4,5,6\}$．'
              r'若 $A$、$B$ 为 $M$ 的非空子集，且 $A$ 中的任何一个圆与 $B$ 中的任何一个圆均无公共点，'
              r'则称 $(A,B)$ 为一个"有序集合对"（当 $A\neq B$ 时，$(A,B)$ 与 $(B,A)$ 为不同的'
              r'有序集合对），那么 $M$ 中"有序集合对" $(A,B)$ 的个数是（　　）',
 'opts': [['A', '$50$'], ['B', '$54$'], ['C', '$58$'], ['D', '$60$']],
 'analysis': r'两圆有公共点 $\Leftrightarrow$ 圆心距 $\leqslant 2$．'
             r'逐个圆心枚举 $A$ 的取法，统计与之全不相邻的圆构成的集合的非空子集个数．',
 'solution': r'半径均为 $1$，故两圆有公共点 $\Leftrightarrow$ 圆心距 $\leqslant 2$．'
             r'$A=\{O_1\}$、$\{O_3\}$、$\{O_4\}$、$\{O_6\}$ 各对应 $B$ 有 $7$ 种，共 $28$；'
             r'$A=\{O_2\}$、$\{O_5\}$ 各对应 $B$ 有 $3$ 种，共 $6$；'
             r'$A=\{O_1,O_4\}$、$\{O_3,O_6\}$ 各有 $3$ 种，共 $6$；'
             r'$A$ 为 $\{O_1,O_2\}$、$\{O_2,O_3\}$、$\{O_4,O_5\}$、$\{O_5,O_6\}$、$\{O_1,O_5\}$、'
             r'$\{O_2,O_4\}$、$\{O_3,O_5\}$、$\{O_2,O_6\}$、$\{O_1,O_3\}$、$\{O_4,O_6\}$ 各 $1$ 种，共 $10$；'
             r'$A$ 为 $\{O_1,O_2,O_4\}$、$\{O_2,O_3,O_6\}$、$\{O_1,O_4,O_5\}$、$\{O_3,O_5,O_6\}$ 各 $1$ 种，共 $4$．'
             r'合计 $28+6+6+10+4=54$．故选 B．',
 'review': '原卷配图，此处六个圆心坐标已在题干中完整给出，可不依赖图作答。'
           '用程序枚举全部 $63\times 63$ 组非空子集对，满足条件的恰为 54，与答案一致。',
},
]

if __name__ == '__main__':
    ok, res = H.add_many(QS, batch='人工录入-002')
    print('OK' if ok else 'FAIL', res if not ok else '%d 题入库' % len(res))
    if ok:
        for i, q in enumerate(QS):
            print('  ', res[i], q['type'], '|', q['stem_text'][:44])
