# -*- coding: utf-8 -*-
r"""从 bank.json 的 review 字段自动汇总「与原书不一致」的处理，生成《原书勘误表.md》。

    python3 tools/gen_errata.py

分类：
  A 类  原书【答案】本身判错并改动   —— 人工审核最不可替代的产出
  B 类  PDF 提取丢符号 → 还原        —— 原书无误，是"假错误"
  C 类  答案未改，仅详解/选项笔误
  D 类  存疑，按原书保留

A 类的「原书答案 / 现录入 / 依据」是人工判断的结论，无法从 review 里
自动解析，集中维护在下面的 A_MANUAL 表里；题号或结论有变动时改这里。
B / C / D 类按题号清单从 review 抽取，新增题目时把题号加进对应列表。
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
BANK = os.path.join(ROOT, 'data', 'bank.json')
OUT = os.path.join(ROOT, '原书勘误表.md')

# ── A 类：人工结论，需手工维护 ────────────────────────
# (题号, 来源, 原书答案, 现录入, 依据)
A_MANUAL = [
    ('M-H0220', 'M-T-041-V3', 'C（3 个真命题）', '**D（4 个真命题）**',
     r'四个命题全部为真，真命题个数是 $4$。'
     r'② $\\ln\\pi<\\frac{\\pi}{\\mathrm e}$ 有严格证明：'
     r'$(\\ln x)/x\\le 1/\\mathrm e$（最大值在 $x=\\mathrm e$ 取到），'
     r'故 $\\ln x\\le x/\\mathrm e$，等号仅当 $x=\\mathrm e$；$\\pi\\ne\\mathrm e$ 故严格小于。'
     r'原书据「$\\mathrm e<\\pi$ 且 $f$ 递减得 $f(\\mathrm e)>f(\\pi)$」判②为假，是把不等号方向用反了。'
     r'数值：$\\ln\\pi=1.144729886<\\pi/\\mathrm e=1.155727350$；'
     r'① $\\ln3=1.098612<\\sqrt3\\ln2=1.200566$；'
     r'③ $2^{\\sqrt{15}}=14.651570<15$；'
     r'④ $3\\mathrm e\\ln2=5.652508<4\\sqrt2=5.656854$。四个全真，选 D'),
    ('M-H0101', 'M-T-075-V1', '$(2,3)$', '**$(2,3]$**',
     r'$a=3$ 时确有三个 $t$ 解（$t=0$ 与 $t=\\frac{3\\pm\\sqrt5}2$），'
     r'三解均 $>-1$，各给两个 $x$，共 $6$ 个不同零点，故右端点 $3$ 可以取到。'
     r'数值逐个计数 $g(f(x))=a$ 的不同实根：$a=1.9\\to0$ 个、$a=2.0\\to1$ 个、'
     r'$a=2.5\\to6$ 个、$a=2.99\\to6$ 个、**$a=3.0\\to6$ 个**、$a=3.01\\to4$ 个、$a=3.5\\to4$ 个。'
     r'$a=3$ 时六个零点为 $-2.902113,\\-2.175571,\\-2,\\ 0,\\ 0.175571,\\ 0.902113$。'
     r'$a=3$ 时 $t=0$ 来自 $-t^2+3=3$，另两解来自 $t+\\frac1t=3$；$a>3$ 时 $-t^2+3=a$ 无解，只剩 $4$ 个零点'),
    ('M-H1382', 'M-T-304-E1', r'$\frac{130}{26}$', r'$\frac{\sqrt{130}}{26}$',
     r'$\frac{130}{26}=5>1$，不可能是正弦值。'
     r'详解末行 $\sin\alpha=\frac h{CQ}=\frac{\frac{\sqrt5}2}{\frac{\sqrt{26}}2}'
     r'=\frac{\sqrt5}{\sqrt{26}}$ 有理化后正是 $\frac{\sqrt{130}}{26}\approx0.4385$'
     r'（原书在分子丢了根号）'),
    ('M-H1311', 'M-T-398-V2', r'$E\xi=\frac{19}7$', r'$E\xi=\frac{85}{37}$',
     r'原书把返回 A 点的 7 种结果当成等可能，取 $P(\xi=2)=P(\xi=3)=\frac37$、$P(\xi=4)=\frac17$。'
     r'这 7 种结果分属 2 次、3 次、4 次投掷，概率分别为 $\frac19$、$\frac1{27}$、$\frac1{81}$，并不等可能；'
     r'按条件概率 $P(\xi=k)=\frac{P_k}{P}$ 归一化得 $\frac{27}{37},\frac9{37},\frac1{37}$，'
     r'故 $E\xi=\frac{2\times27+3\times9+4\times1}{37}=\frac{85}{37}\approx2.297$'
     r'（原书值 $\frac{19}7\approx2.714$）'),
    ('M-H0009', 'M-T-003-V1', '原书 C', 'B',
     '详解只列 {1,2,3}、{1,2,4}，遗漏 {1,2,3,4}；真包含要求 A≠{1,2}，'
     '{1,2,3,4} 满足，实为 3 个'),
    ('M-H0069', 'M-T-019-V3', r'$\frac{5\sqrt5}{2}\approx5.590$',
     r'$\sqrt5+\sqrt{10\sqrt5}\approx6.9648$',
     r'错在把 $\frac5{c-2}$ 提出 $\sqrt5$ 后写成 $\frac1t$（应为 $\frac{\sqrt5}t$）。'
     r'取等 a≈0.618、b≈1.382、c≈4.115，数值扫描 6.964776 佐证'),
    ('M-H0081', 'M-T-023-E1', r'$(0,\frac{\sqrt6}6]$',
     r'$(\frac25,\frac{\sqrt6}6]$',
     r'解析把 $t$ 与 $t^2$ 范围混淆：$t^2=1+3xy\in(1,\frac85]$，'
     r'故 $t\to1$ 时原式趋于 $\frac25$ 而非 $0$。扫描值域 [0.400000,0.408248] 吻合'),
    ('M-H0176', 'M-T-098-E1', '单调递增', '单调递减',
     '原书【详解】末尾综述与前文「f′(x)<0，单调递减」矛盾；数值抽查 k=1,2,5 均恒减'),
    ('M-H1289', 'M-T-354-V1', r'$S_{\\triangle ABF_1}=3$',
     r'$S_{\\triangle ABF_1}=\\sqrt3$',
     r'根号丢失。独立验算：$|AB|=\\sqrt2\\cdot\\frac{\\sqrt6}2=\\sqrt3$，'
     r'$F_1$ 到直线 $x-y-\\sqrt2=0$ 的距离 $d=\\frac{2\\sqrt2}{\\sqrt2}=2$，'
     r'故 $S=\\frac12\\cdot\\sqrt3\\cdot2=\\sqrt3$（$\\approx1.732$，不可能是 $3$）'),
    ('M-H1288', 'M-T-352-V2',
     r'$\\left(-\\infty,-\\frac12\\right]\\cup\\left(\\frac12,+\\infty\\right)$',
     r'$\\left(-\\infty,-\\frac12\\right]\\cup\\left[\\frac12,+\\infty\\right)$',
     r'右端漏了斜率不存在的情形：原书自己算出 $l:x=0$ 时 '
     r'$\\vec{EM}\\cdot\\vec{EN}=\\frac12$，故 $+\\frac12$ 能取到，应为闭区间'),
    ('M-H0905', 'M-T-229-V1', r'定值 $-1$', r'定值 $0$',
     r'原书末行写 $\cos A+\cos C+\varphi(m)+\varphi(m)\cos A\cos C=-1$，'
     r'实则交叉相乘得 $4m=2(m^2+1)X-4mY$，即 $X-\frac{2m}{m^2+1}Y=\frac{2m}{m^2+1}$，'
     r'定值为 $0$。数值对拍：m=2（等边）$1-0.8-0.2=0$；m=3（A=C=70.53°）$0.6667-0.6-0.0667=0$'),

    ('M-H1063', 'M-T-327-V2', r'最小值 $2$', r'$\sqrt2$',
     r'详解中「$\sqrt{a^2+b^2}\ge\frac12(a+b)$」漏了根号，正确为 $\frac{\sqrt2}2(a+b)$；'
     r'于是 $\frac{2\sqrt{a^2+b^2}}{a+b}\ge\sqrt2$（非 $2$）。数值：$a=b$ 时 $=1.414214=\sqrt2$，'
     r'$a=1,b=3$ 时 $=1.581139>\sqrt2$'),
    ('M-H1066', 'M-T-335-V2', r'$4+2\sqrt2$', r'$4+\sqrt7$',
     r'详解末行「$c^2+8ac+8a^2=0\Rightarrow e^2-8e+8=0$」三项同号不可能为 $0$；'
     r'由余弦定理严格展开 $64a^2=100a^2+4c^2-32ac$，即 $c^2-8ac+9a^2=0$，$e^2-8e+9=0$。'
     r'数值（a=1）：c=4+\sqrt7=6.645751 时 P(1.354249,6) 同时满足斜率 0.75、抛物线、双曲线三条件；'
     r'c=4+2\sqrt2=6.828427 时第三式 $=1.1032\ne1$；全解扫描仅此一个解'),
    ('M-H0937', 'M-T-249-V1', r'$S_n=\frac{2^{n}+3n^{2}-7n}{2}-1$',
     r'$S_n=\frac{2^{n+1}+3n^{2}-7n}{2}-1$',
     r'原书分子写 $2^{n}$，疑为 $2^{n+1}$ 丢失上标中的 $+1$。'
     r'代入检验：$n=1$ 时该式给 $\frac{2+3-7}{2}-1=-2$，而 $S_1=\frac{a_1}{1}+3-5=-1$。'
     r'按 $2^{n+1}$：$n=1$ 给 $-1$、$n=2$ 给 $2$（$=-1+(2+6-5)$），均与逐项求和一致'),
    ('M-H1112', 'M-T-321-E1', r'（Ⅱ）$\dfrac{3}{6}$（原文根号丢失）',
     r'（Ⅱ）$\dfrac{\sqrt3}{6}$',
     r'详解末段 $V=\frac12\times\frac13\times S_{\triangle BCD}\times AE$ 中的'
     r'$S_{\triangle BCD}=\frac{\sqrt3}4\times2^2=\sqrt3$（等边 $\triangle ABD$ 面积），'
     r'故 $V=\frac16\times\sqrt3\times1=\frac{\sqrt3}6$。'
     r'若按 $\frac36=\frac12$ 则要求 $S_{\triangle BCD}=3$，与 $\sqrt3$ 不符（提取时丢了根号）'),
    ('M-H1120', 'M-T-326-V2', r'（Ⅱ）$\dfrac{2}{12}$（原文根号丢失）',
     r'（Ⅱ）$\dfrac{\sqrt2}{12}$',
     r'详解给出 $A^{\prime}$ 到底面最大距离为 $A^{\prime}O=\frac{\sqrt2}2$，$F$ 是 $A^{\prime}C$ 中点故再减半为 $\frac{\sqrt2}4$，'
     r'$V=\frac13\times1\times\frac{\sqrt2}4=\frac{\sqrt2}{12}$。'
     r'若按 $\frac2{12}=\frac16$ 则要求 $F$ 到底面距离为 $\frac12$，'
     r'而实际最大仅 $\frac{\sqrt2}4\approx0.354<\frac12$，不可能'),
    ('M-H1132', 'M-T-245-V1', r'$\dfrac{4\sqrt3-7}6$', r'$\dfrac{4\sqrt3-\sqrt7}6$',
     r'原书答案根号丢失：按 $\\dfrac{4\\sqrt3-7}6$ 计算得 $-0.011966<0$，而所求是一个模长，'
     r'不可能为负。正确值 $\\dfrac{4\\sqrt3-\\sqrt7}6\\approx0.7137420$。'
     r'推导：换元 $a=2\\lambda_1 u$、$b=3\\lambda_2 v$ 后，投影条件给 $p+q=\\dfrac43$，'
     r'目标式平方 $=\\dfrac34\\left(\\dfrac43-\\lambda_1-\\lambda_2\\right)^2$；拉格朗日给 $\\lambda_1=6\\lambda_2$、'
     r'$\\lambda_1+\\lambda_2=\\dfrac{\\sqrt{21}}9$，代入得 $\\dfrac{4\\sqrt3-\\sqrt7}6$。'
     r'数值复核：直接数值最小化 $0.7137417822$，与解析值 $0.7137419865$ 吻合；'
     r'数值解出 $\\lambda_1=0.43642197$、$\\lambda_2=0.07275335$，与 $\\dfrac6{\\sqrt{189}}=0.4364357805$、'
     r'$\\dfrac1{\\sqrt{189}}=0.0727392967$ 逐位相同'),
    ('M-H1308', 'M-T-313-V2', '（2）直线 $PD$ 与平面 $ACM$ 的距离 $=3$', '（2）该距离 $=\\sqrt3$', '原书答案 $3$ 绝无可能：点到平面的距离不超过该点到平面上已知点的距离，而 $A\\in$ 平面 $ACM$、$|AP|=PA=2$，故 $d\\le2<3$。独立建系算得 $\\sqrt3\\approx1.732<2$。原书是把 $\\sqrt3$ 丢了根号。推导：$A(0,0,0)$、$D(4,0,0)$、$P(0,0,2)$、$B(-1,\\sqrt3,0)$、$C(1,\\sqrt3,0)$、$M=\\frac23B+\\frac13P=(-\\frac23,\\frac{2\\sqrt3}3,\\frac23)$；平面 $ACM$ 法向量 $\\vec n=(\\sqrt3,-1,2\\sqrt3)$，$\\vec{PD}\\cdot\\vec n=4\\sqrt3-4\\sqrt3=0$ 印证（1）的平行结论；$d=\\frac{|\\vec{AP}\\cdot\\vec n|}{|\\vec n|}=\\frac{4\\sqrt3}{4}=\\sqrt3$。另取 $D$ 验算：$|\\vec{AD}\\cdot\\vec n|=4\\sqrt3$，同得 $\\sqrt3$ ✓'),
    ('M-H1166', 'M-T-146-V2', r'（1）所证式右端 $x^{2}+x+e-e^{2}$',
     r'（1）所证式右端 $x^{2}+x+e-e^{x}$',
     r'原书将 $e^{x}$ 印成 $e^{2}$（提取为 `e2`）。判据：详解令 $h(x)=e^{x}+\ln x-e$，'
     r'则 $h(1)=e+0-e=0$ 且 $h$ 递增 ⟹ $x>1$ 时 $h(x)>h(1)=0$，逻辑链完整闭合。'
     r'若按 $e^{2}$，则 $h(x)=e^{2}+\ln x-e$ 恒正但 $h(1)=e^{2}-e\approx4.67\ne0$，'
     r'与详解「$h(x)>h(1)$」的用法矛盾。数值复核：$x=1.01$ 时 $e^{x}+\ln x-e=0.0373>0$，'
     r'$x\to1^{+}$ 时趋于 $0$（取不到），故严格 $>$ 成立'),
    ('M-H1387', 'M-T-181-E1', 'B（最小值为 $-1$）', '**C（最小值为 $-2$）**',
     r'分母 $=3-2\sin x-2\cos x=(1-\sin x)^2+(1-\cos x)^2$，分子 $=-(1-\sin x)$，'
     r'故 $f=-\dfrac u{u^2+v^2}$（$u=1-\sin x,\ v=1-\cos x$）。'
     r'求导令分子为零得 $2-\cos x-2\sin x=0$（$\sin x\cos x$ 项恰好抵消），'
     r'即 $\cos x+2\sin x=2$，与 $\sin^2x+\cos^2x=1$ 联立得 $5\sin^2x-8\sin x+3=0$，'
     r'根为 $\sin x=1$（此时 $f=0$）与 $\sin x=\dfrac35$。'
     r'取 $\sin x=\dfrac35,\ \cos x=\dfrac45$，则 $u=\dfrac25,\ v=\dfrac15,\ u^2+v^2=\dfrac15$，'
     r'$f=-\dfrac{2/5}{1/5}=-2$。'
     r'$2\times10^6$ 点数值扫描得最小值 $-1.99999999999$，取等处 $\sin x=0.600001,\ \cos x=0.800000$ ✓。'
     r'原书详解令 $g=\dfrac{1-\cos x}{1-\sin x}$ 后写 $f=-\dfrac1{1+g^2}$，'
     r'正确应为 $f=-\dfrac1{(1-\sin x)(1+g^2)}$，即**丢了因子 $(1-\sin x)$**；'
     r'在 $x=0$（即 $u=1$）处两者碰巧同为 $-1$，详解遂误判那为最小值'),
    ('M-H1388', 'M-T-190-V1', r'A（$\left(\dfrac{\sqrt3}2,\sqrt3\right)$）',
     r'**B（$\left(\dfrac{\sqrt3}2,\sqrt3\right]$）**',
     r'由射影定理 $c\cos B+b\cos C=a$ 得 $\dfrac{\cos B}b+\dfrac{\cos C}c=\dfrac a{bc}$，'
     r'条件化为 $\sin B\cdot\dfrac a{bc}=\dfrac{\sin A}{\sin C}=\dfrac ac$，'
     r'故 $\dfrac{\sin B}b=1$，即 $b=\dfrac{\sqrt3}2$ 且 $2R=1$。'
     r'于是 $a+c=\sin A+\sin\left(\dfrac{2\pi}3-A\right)=\sqrt3\sin\left(A+\dfrac\pi6\right)$，'
     r'$A\in\left(0,\dfrac{2\pi}3\right)$ ⟹ $a+c\in\left(\dfrac{\sqrt3}2,\sqrt3\right]$。'
     r'**硬判据**：$A=B=C=\dfrac\pi3$（等边）时 $a=b=c=\dfrac{\sqrt3}2$，'
     r'代入条件左边 $=\sin\dfrac{2\pi}3\cdot\dfrac{2\cos(\pi/3)}{\sqrt3/2}=1$、右边 $=1$，'
     r'条件成立且 $a+c=\sqrt3$ 精确取到，右端必闭。'
     r'数值扫描 $2\times10^5$ 点得 $[0.866027,1.732051]$，即 $\left(\dfrac{\sqrt3}2,\sqrt3\right]$ ✓'),
]

# ── B / C 类：题号清单，说明从 review 抽 ──────────────
B_KEYS = ['M-H0018', 'M-H0023', 'M-H0027', 'M-H0029', 'M-H0080', 'M-H0087',
          'M-H0090', 'M-H0091', 'M-H0106', 'M-H0175', 'M-H0186', 'M-H0194',
          'M-H0195', 'M-H0197', 'M-H0199', 'M-H0070', 'M-H0030', 'M-H0033',
          'M-H0061', 'M-H0064', 'M-H0065']

# 第13批（T037~T040 幂指对比较大小）：上标、下标、分数线在提取时全部塌成平文本，
# 16 题全部靠【详解】反推还原，原书无误 —— 归入 B 类。
B_KEYS += ['M-H%04d' % i for i in range(201, 217)]

# 第14批（T041~T045）：同样全部塌成平文本，21 题靠 pdf2latex.py 的字号/基线
# 重建 + 详解反推，原书无误 —— 归入 B 类。
B_KEYS += ['M-H%04d' % i for i in range(217, 238)]

# 第15批（T060~T062）：分段函数大括号全部塌成平文本，
# 12 题靠详解逐段反推 + 数值校验还原，原书无误 —— 归入 B 类。
B_KEYS += ['M-H%04d' % i for i in range(238, 250)]

# 第15批（下）：T063 高斯函数 / T064 与三角结合 / T065 周期性，
# 12 题的分段括号、取整记号、指数全塌，靠详解反推 + 数值校验，
# 原书无误 —— 归入 B 类。
B_KEYS += ['M-H%04d' % i for i in range(250, 262)]

# 第110批：三处 PDF 提取造成的「假错误」，按 原件/按页原文 还原后与原书一致
# - M-H1131（M-T-245-E1）：题面整段丢失，只剩「则正确的判断是（　　）」，
#   按 p210「例1」原文补全夹角 120°、a·b=-2、c=λa+(1-λ)b、两个结论等全部条件
# - M-H1133（M-T-245-V2）：连等式 |c|=2|a-c|=2 易被误读成 |a-c|=2，
#   实为 |c|=2 且 2|a-c|=2，即 |a-c|=1（按 2 算答案会变成 2√3-2，与原书不符）
# - M-H1135（M-T-187-E1）：|a·c|+|b·c| 的绝对值被吞掉，
#   无绝对值时最小值是 -16 而非 2√15，数值对拍可证
B_KEYS += ['M-H1131', 'M-H1133', 'M-H1135']

# 第129批：统计回归块三处 PDF 提取失真，按参考数据与答案反推还原，原书无误
# - M-H1367（M-T-391-E1）：参考数据「Σyᵢ²-10ȳ²≈37.16」实为 1380.9
#   （37.16 是 √1380.9），代入 1380.9 恰得 r≈0.72，与答案完全吻合
# - M-H1369（M-T-393-E1）：W 的表达式提取为「1000 y - lnx」，实为
#   W=1000(y-lnx)；按前者驻点在 x=10000，与答案 x=10 矛盾
# - M-H1371（M-T-147-V2）：题干两处还原，(a) G(x) 应为 (3/2)(2x-1)(x-1)²
#   而非 (3x-1)/2·(x-1)²（判据：G(0)=-3/2<-1、G(2/3)=1/18、G'=3(x-1)(3x-2)
#   三条同时吻合详解）；(b) g 的 x 系数应为 a²-1/2 而非 (a²-1)/2
#   （只有前者能分解成 (x+2)(x-a²)>0）
B_KEYS += ['M-H1367', 'M-H1369', 'M-H1371']



C_KEYS =['M-H0003', 'M-H0014', 'M-H0021', 'M-H0022', 'M-H0026',
          'M-H0049', 'M-H0055', 'M-H0057', 'M-H0015', 'M-H0019', 'M-H0025']

D_KEYS = []

# 第15批 T063-V2：零点实际有无穷多个（±1.7808、±2.6861、…），
# 原书按 ± 配对相消得 -1，该“和”按对称和理解成立、按级数求和并不收敛。
# 按原书答案 A 录入，留待复核。
D_KEYS += ['M-H0252']

# 2026-09 复核裁定：疑点已算清，结论记在下面 D_NOTE 里，答案维持原书。
D_NOTE = {
    'M-H0252': (
        '**2026-09 复核定论（已算清，不再存疑）**：零点集可完全解出'
        r'—— $\{-1\}\cup\{\pm x_n:n=1,2,3,\cdots\}$，'
        r'其中 $x_n=\dfrac{(2n+1)+\sqrt{(2n+1)^{2}+8}}{4}\in(n,n+1)$。'
        '**配对是精确的、有代数证明**：若 $x\\in(n,n+1)$ 为零点则 $2(x-n)=1+\\frac1x$；'
        '取 $y=-x\\in(-n-1,-n)$，则 $[y]=-n-1$、$\\{y\\}=n+1-x$，'
        '故 $2\\{y\\}=2n+2-2x=1-\\frac1x=1+\\frac1y$，$y$ 亦为零点。'
        '即除 $x=-1$ 外全部零点严格成对、互为相反数（$x=-1$ 落单是因为整数点处 '
        '$\\{x\\}$ 跳跃、对称性失效）。'
        '**结论**：零点无穷多，$x_n\\sim n+\\frac12$，'
        '“所有零点之和”作为级数发散、无严格定义——这是原书命题瑕疵；'
        '但在对称和约定下各对恰好抵消、仅余 $-1$，与答案 A 一致。**维持原书答案 A**。'
    ),
}

# 第14批 T041-V3：数值验证显示四个命题全真（应为 D），原书答案 C 判②为假，
# 但详解「f(e) < f(π)」不等号写反（1/e 是 f 的最大值，必有 f(e) > f(π)）。
# 因③的上标含矢量绘制的根号、无法百分百确认，按原书 C 录入并留待复核。
# → 2026-09 已核实：四个命题全真，改为 A 类并更正答案为 D（见 A_MANUAL）。


def src_short(q):
    s = (q.get('src') or '').split('·')
    return s[-1].strip() if s else q['id']


def why(q):
    """从 review 里抽最能说明"改了什么"的那一句。"""
    r = (q.get('review') or '')
    segs = [s.strip() for s in re.split(r'[。；]', r) if s.strip()]
    hit = [s for s in segs
           if re.search(r'丢失|丢了|缺|提取|还原|重建|无【答案】|截断|码位|'
                        r'私用区|U\+F|笔误|印作|有误|矛盾|重复', s)]
    return (hit[0] if hit else segs[0] if segs else '')[:120]


def main():
    bank = json.load(open(BANK, encoding='utf-8'))
    idx = {q['id']: q for q in bank}
    L = []
    L.append('# 原书勘误与修正记录')
    L.append('')
    L.append('本表由 `tools/gen_errata.py` 从 `data/bank.json` 的 `review` 字段'
             '自动汇总生成，题库变更后重跑该脚本即可刷新。')
    L.append('')
    L.append('> 逐题的完整推理链仍在每题的 `review` 字段里，本表只作索引与速查。')
    L.append('')

    # A
    L.append('## A 类：原书【答案】本身有误，已按正确答案录入')
    L.append('')
    L.append('| 题号 | 来源 | 原书答案 | 现录入 | 依据 |')
    L.append('|---|---|---|---|---|')
    for qid, src, old, new, reason in A_MANUAL:
        if qid not in idx:
            print('  ! A 类 %s 不在题库，跳过' % qid)
            continue
        L.append('| %s | %s | %s | **%s** | %s |' % (qid, src, old, new, reason))
    na = sum(1 for x in A_MANUAL if x[0] in idx)
    L.append('')
    L.append('**A 类共 %d 题。** 这类是真正发现原书印错，'
             '也是人工审核最不可替代的部分。' % na)
    L.append('')

    # B
    L.append('## B 类：PDF 提取丢符号 → 还原（原书本身无误）')
    L.append('')
    L.append('教辅用 MathType/PMExtra 字体排公式，数学符号落在 Unicode 私用区，'
             '常规提取会吞掉。这类**不是原书印错**，而是提取造成的"假错误"，'
             '还原后与原书一致。')
    L.append('')
    L.append('| 题号 | 来源 | 丢的是什么 | 现答案 |')
    L.append('|---|---|---|---|')
    nb = 0
    for qid in B_KEYS:
        q = idx.get(qid)
        if not q:
            print('  ! B 类 %s 不在题库，跳过' % qid)
            continue
        nb += 1
        L.append('| %s | %s | %s | %s |'
                 % (qid, src_short(q), why(q), str(q.get('answer') or '')[:40]))
    L.append('')
    L.append('**B 类共 %d 题。**' % nb)
    L.append('')

    # C
    L.append('## C 类：答案未改，仅详解/选项有笔误')
    L.append('')
    L.append('| 题号 | 来源 | 原书问题 | 现答案 |')
    L.append('|---|---|---|---|')
    nc = 0
    for qid in C_KEYS:
        q = idx.get(qid)
        if not q:
            print('  ! C 类 %s 不在题库，跳过' % qid)
            continue
        nc += 1
        L.append('| %s | %s | %s | %s |'
                 % (qid, src_short(q), why(q), str(q.get('answer') or '')[:40]))
    L.append('')
    L.append('**C 类共 %d 题。** 答案与原书一致，'
             '只修正了推导过程中的笔误或排版错误。' % nc)
    L.append('')

    # D
    L.append('## D 类：存疑，按原书保留')
    L.append('')
    L.append('| 题号 | 来源 | 疑点 | 现答案（按原书） |')
    L.append('|---|---|---|---|')
    nd = 0
    for qid in D_KEYS:
        q = idx.get(qid)
        if not q:
            continue
        nd += 1
        L.append('| %s | %s | %s | %s |'
                 % (qid, src_short(q), why(q), str(q.get('answer') or '')[:40]))
    L.append('')
    L.append('**D 类共 %d 题。** 发现可疑但证据不足以推翻原书，'
             '按原书录入并把疑点记在 review 里，留待复核。' % nd)
    for qid in D_KEYS:
        if qid in idx and qid in D_NOTE:
            L.append('')
            L.append('### %s 复核裁定' % qid)
            L.append('')
            L.append(D_NOTE[qid])
    L.append('')
    L.append('## 附：录入与排版修正（E 类）')
    L.append('')
    L.append('这一类**不是原书的问题**，而是录入/排版环节产生的修正'
             '（控制字符错码、命令粘连、`$` 未闭合、字面 `\\n`、区间括号等），'
             '已由 `tools/build_fix_registry.py` 登记。')
    L.append('')
    L.append('完整清单见 **《已修正题目清单.md》**；'
             '题库中这些题带 `fix.cls = "E"` 字段，可按该字段检索复核。')

    open(OUT, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print('  已生成 %s' % OUT)
    print('  A 类 %d / B 类 %d / C 类 %d / D 类 %d' % (na, nb, nc, nd))
    return 0


if __name__ == '__main__':
    sys.exit(main())
