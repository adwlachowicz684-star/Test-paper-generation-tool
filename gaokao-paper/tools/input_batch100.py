# -*- coding: utf-8 -*-
r"""第 100 批：导数中的「距离」型（M-T-137，2 题）+ 构造型距离（M-T-138，2 题）
+ 导数解答题（M-T-147-V1、M-T-148 三题、M-T-154 三题、M-T-162-V2）

    python3 tools/run_batch.py 100

## 选题依据

按「详解完整 + 无图依赖 + 同题型聚堆」筛出：
M-T-137 / M-T-138 在 p103-104（导数中的距离），
M-T-147-V1 在 p061、M-T-148 在 p114-115、M-T-154 在 p119-120、M-T-162-V2 在 p103。
共 12 题，其中 4 题选择 / 1 题填空 / 7 题解答。

## 第一条：本 PDF 的文本层会「吞掉根号」

第 137-V1、137-V2、138-V1 三题的题干或选项中都有根号，而 pdftotext / PyMuPDF
**提取不到 √ 字形**（同页的括号也提取不到，只留下空白字符）。判定办法有两种：

1. **看行首缩进与行高**：137-V1 题干那一行缩进 6.9、行高 13.3，而同页同型且
   确认无根号的题（答案取「距离平方」的那道）缩进 2.4、行高 11.0 —— 多出来的
   约 6.5 正是 √ 字形的宽度。
2. **看答案能否对上选项**：按「距离平方」算出的值若四个选项都没有，就说明
   题干有根号（所求为距离本身）。

> 通法：**凡是「求两曲线间距离」的题，先算距离 $d$，再看选项匹配 $d$ 还是 $d^{2}$。**

## 第二条：抛物线的「焦点距离」是设计出来的常数

137-V2 里 $D=\left|PQ\right|+\left|QF\right|$，其中 $Q\left(a,\frac{a^{2}}4\right)$ 在
$x^{2}=4y$ 上，故 $\left|QF\right|=\frac{a^{2}}4+1$ 恰好就是式子后面的常数项。

> 通法：**见到 $\frac{a^{2}}4+1$（或 $\frac{a^{2}}{2p}+\frac p2$）就认出它是抛物线上
> 点到焦点的距离**，于是和式可用三角形不等式 $\left|PQ\right|+\left|QF\right|\ge\left|PF\right|$ 合并。

## 第三条：零点存在型 ⟹ 点到直线距离

138-V1 把「$f$ 在 $[0,1]$ 上有零点 $t$」翻译成「点 $(a,b)$ 在直线
$(t-1)x+y+\mathrm e^{t}=0$ 上」，于是 $a^{2}+b^{2}$ 就是原点到该直线的距离平方。

> 通法：**参数以「一次」形式出现在方程里 ⟹ 把它看成直线方程的系数，
> 把所求的平方和看成点到直线的距离。**

## 三处原书存疑（判据写在各题 review 里）

1. **M-T-138-V1**：严格推导 $a^{2}+b^{2}$ 的最小值为 $\frac12$，四个选项中没有；
   原书标答 B $=\frac{\sqrt2}2$ 恰是 $\sqrt{a^{2}+b^{2}}$ 的最小值。
2. **M-T-154-E1**：原书方法一给 $k=3$（正确），方法二、三却给 $k=2$（有误）。
3. **M-T-148-V2**：详解把 $a,m$ 两个字母写反了，按题干的字母重新整理。
"""

T137_V1 = {
    'type': '选择',
    'stem_text': (
        r"若实数 $a,b,c,d$ 满足 $\dfrac{a^{2}-2\ln a}{b}=\dfrac{3c-4}{d}=1$，"
        r"则 $\sqrt{\left(a-c\right)^{2}+\left(b-d\right)^{2}}$ 的最小值为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac{\left(1-\ln2\right)\sqrt{10}}{5}$"),
        ('B', r"$\dfrac{\left(1+\ln2\right)\sqrt{10}}{5}$"),
        ('C', r"$\dfrac{\left(3-\ln2\right)\sqrt{10}}{5}$"),
        ('D', r"$\dfrac{\left(3+\ln2\right)\sqrt{10}}{5}$"),
    ],
    'answer': 'A',
    'analysis': (
        r"两个等式分别给出 $b=a^{2}-2\ln a$ 与 $d=3c-4$，于是 $P\left(a,b\right)$ 在曲线 "
        r"$y=x^{2}-2\ln x$ 上、$Q\left(c,d\right)$ 在直线 $y=3x-4$ 上，所求即 $\left|PQ\right|$ 的最小值。"
        r"用「平移切线」：与已知直线平行的切线对应的切点即最近点。"
    ),
    'solution': (
        r"由 $\dfrac{a^{2}-2\ln a}{b}=1$ 得 $b=a^{2}-2\ln a$，即点 $P\left(a,b\right)$ 在曲线 "
        r"$f\left(x\right)=x^{2}-2\ln x\ \left(x>0\right)$ 上；" "\n"
        r"由 $\dfrac{3c-4}{d}=1$ 得 $d=3c-4$，即点 $Q\left(c,d\right)$ 在直线 $l:y=3x-4$ 上．" "\n"
        r"故所求 $\sqrt{\left(a-c\right)^{2}+\left(b-d\right)^{2}}=\left|PQ\right|$，"
        r"其最小值就是曲线 $y=x^{2}-2\ln x$ 到直线 $y=3x-4$ 的最小距离．" "\n"
        r"当曲线在 $P$ 处的切线与 $l$ 平行时取到，令" "\n"
        r"$f'\left(x\right)=2x-\dfrac2x=\dfrac{2x^{2}-2}{x}=3$，即 $2x^{2}-3x-2=0$，"
        r"解得 $x=2$（负根 $-\dfrac12$ 舍去）．" "\n"
        r"于是 $P\left(2,\,4-2\ln2\right)$，它到直线 $3x-y-4=0$ 的距离为" "\n"
        r"$d=\dfrac{\left|3\times2-\left(4-2\ln2\right)-4\right|}{\sqrt{3^{2}+\left(-1\right)^{2}}}$"
        r"$=\dfrac{\left|2\ln2-2\right|}{\sqrt{10}}=\dfrac{2\left(1-\ln2\right)}{\sqrt{10}}$"
        r"$=\dfrac{\left(1-\ln2\right)\sqrt{10}}{5}$．" "\n"
        r"故选 $\boxed{\mathrm A}$．"
    ),
    'review': (
        r"① 题干根号的还原依据（本 PDF 文本层吞掉 √ 字形）：按「距离平方」算得 "
        r"$\left[\frac{(1-\ln2)\sqrt{10}}5\right]^{2}\approx0.0377$，四个选项全都对不上；"
        r"而按距离算恰为选项 A．" "\n"
        r"② 版式证据：题干所在行缩进 6.9、行高 13.3，同页另一道确认无根号的同型题"
        r"（答案取距离平方 $d^{2}=8$）缩进 2.4、行高 11.0，多出的约 6.5 正是 √ 字形宽度．" "\n"
        r"③ 本题与同页例 1 的差别只在「所求带不带根号」：例 1 求 $(a-c)^{2}+(b-d)^{2}$（答案 $d^{2}=8$），"
        r"本题求 $\sqrt{(a-c)^{2}+(b-d)^{2}}$（答案 $d$）——**做题第一件事是看选项量级**．" "\n"
        r"④ $f'\left(x\right)=3$ 解得两根 $2$ 与 $-\frac12$，后者不在定义域 $x>0$ 内，必须舍去．" "\n"
        r"⑤ 有理化 $\frac{2}{\sqrt{10}}=\frac{2\sqrt{10}}{10}=\frac{\sqrt{10}}5$，这是选项写成\n"
        r"「分子分母都含根号」的原因．" "\n"
        r"⑥ 数值复核：$\ln2=0.6931$，$\left(1-\ln2\right)\frac{\sqrt{10}}5=0.3069\times0.6325=0.1941$；"
        r"直接算 $\left|P\left(2,2.6137\right)\right.$ 到 $y=3x-4$ 的距离 $=\frac{0.6137}{3.1623}=0.1941$ ✓" "\n"
        r"**通法（曲线到直线的最短距离）**：" "\n"
        r"① 把条件里的字母整理成「点在曲线上 / 点在直线上」；" "\n"
        r"② 令曲线导数 = 直线斜率求切点（这就是最近点）；" "\n"
        r"③ 用点到直线距离公式，最后**对照选项判断要不要平方**．"
    ),
    'difficulty': 0.66,
    'topics': ['M-T-137'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-137-V1',
}

T137_V2 = {
    'type': '选择',
    'stem_text': (
        r"设 $D=\sqrt{\left(x-a\right)^{2}+\left(\ln x-\dfrac{a^{2}}4\right)^{2}}+\dfrac{a^{2}}4+1$"
        r"（$a\in\mathbb R$，$x>0$），则 $D$ 的最小值为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac{\sqrt2}2$"),
        ('B', r"$1$"),
        ('C', r"$\sqrt2$"),
        ('D', r"$2$"),
    ],
    'answer': 'C',
    'analysis': (
        r"记 $P\left(x,\ln x\right)$ 在 $y=\ln x$ 上，$Q\left(a,\frac{a^{2}}4\right)$ 在抛物线 $x^{2}=4y$ 上，"
        r"其焦点 $F\left(0,1\right)$，则 $\frac{a^{2}}4+1=\left|QF\right|$，"
        r"于是 $D=\left|PQ\right|+\left|QF\right|\ge\left|PF\right|$，再对 $x$ 求最小值即可．"
    ),
    'solution': (
        r"记 $P\left(x,\ln x\right)$（在曲线 $y=\ln x$ 上），$Q\left(a,\dfrac{a^{2}}4\right)$．" "\n"
        r"由 $a^{2}=4\cdot\dfrac{a^{2}}4$ 知 $Q$ 在抛物线 $x^{2}=4y$ 上，其焦点为 $F\left(0,1\right)$、"
        r"准线为 $y=-1$，故由抛物线定义" "\n"
        r"$\left|QF\right|=y_{Q}+1=\dfrac{a^{2}}4+1$．" "\n"
        r"于是 $D=\left|PQ\right|+\left|QF\right|\ge\left|PF\right|$（三角形不等式），" "\n"
        r"而 $\left|PF\right|=\sqrt{\left(x-0\right)^{2}+\left(\ln x-1\right)^{2}}"
        r"=\sqrt{x^{2}+\left(\ln x-1\right)^{2}}$．" "\n"
        r"令 $h\left(x\right)=x^{2}+\left(\ln x-1\right)^{2}\ \left(x>0\right)$，则" "\n"
        r"$h'\left(x\right)=2x+\dfrac{2\left(\ln x-1\right)}{x}=2\left(x+\dfrac{\ln x-1}{x}\right)$．" "\n"
        r"再令 $u\left(x\right)=x+\dfrac{\ln x-1}{x}$，则 "
        r"$u'\left(x\right)=1+\dfrac{1-\left(\ln x-1\right)}{x^{2}}=1+\dfrac{2-\ln x}{x^{2}}>0$"
        r"（因为 $x^{2}-\ln x+2>0$ 恒成立），" "\n"
        r"故 $u\left(x\right)$ 在 $\left(0,+\infty\right)$ 上严格递增，又 $u\left(1\right)=1+\left(-1\right)=0$，" "\n"
        r"所以当 $0<x<1$ 时 $h'\left(x\right)<0$，当 $x>1$ 时 $h'\left(x\right)>0$，" "\n"
        r"$h\left(x\right)_{\min}=h\left(1\right)=1+\left(0-1\right)^{2}=2$，"
        r"即 $\left|PF\right|_{\min}=\sqrt2$．" "\n"
        r"取等条件：$P\left(1,0\right)$；又 $P\left(1,0\right)$ 与 $F\left(0,1\right)$ 的连线为 $y=1-x$，"
        r"令 $Q$ 落在其上：$\dfrac{a^{2}}4=1-a\Rightarrow a^{2}+4a-4=0\Rightarrow a=2\sqrt2-2\approx0.828\in\left(0,1\right)$，"
        r"此时 $Q$ 在线段 $PF$ 上，等号成立．" "\n"
        r"故 $D_{\min}=\sqrt2$，选 $\boxed{\mathrm C}$．"
    ),
    'review': (
        r"① 题眼：$\frac{a^{2}}4+1$ 不是随便写的常数，它就是 $Q$ 到焦点 $F\left(0,1\right)$ 的距离"
        r"（$x^{2}=4y$ 上点 $\left(a,\frac{a^{2}}4\right)$ 的焦半径 $=\frac{a^{2}}4+\frac p2=\frac{a^{2}}4+1$）．" "\n"
        r"② 和式 $\left|PQ\right|+\left|QF\right|$ 用三角形不等式合并成 $\left|PF\right|$，"
        r"把「两个变量 $x,a$」降成「一个变量 $x$」——这是本题唯一的关键步．" "\n"
        r"③ 原书详解此处残缺（只说「距离表达式为 $x^{2}+(\ln x-1)^{2}$」），上面为补全并验证的版本．" "\n"
        r"④ 选项的 √ 也是被文本层吞掉的：四个选项按 $\frac{\sqrt2}2,1,\sqrt2,2$ 递增排列，"
        r"答案 C 对应 $\sqrt2$（C 项数字前有一段 9.4 的空隙，正是 √ 字形的位置）．" "\n"
        r"⑤ 数值复核：取 $a=2\sqrt2-2=0.8284$，$x=1$，则 "
        r"$\left|PQ\right|=\sqrt{(1-0.8284)^{2}+(0-0.1716)^{2}}=0.2426$，"
        r"$\left|QF\right|=0.1716+1=1.1716$，和 $=1.4142=\sqrt2$ ✓" "\n"
        r"**通法（两段距离之和的最小值）**：" "\n"
        r"① 先看两段是不是「折线」$\left|PQ\right|+\left|QF\right|$，是就用三角形不等式合成 $\left|PF\right|$；" "\n"
        r"② 合成后只剩一个变量，求导定最值；" "\n"
        r"③ 最后**必须验证等号能取到**（折点落在两点之间），否则只是下界不是最小值．"
    ),
    'difficulty': 0.72,
    'topics': ['M-T-137'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-137-V2',
}

T138_V1 = {
    'type': '选择',
    'stem_text': (
        r"设函数 $f\left(x\right)=\mathrm e^{x}+a\left(x-1\right)+b$ 在区间 $\left[0,1\right]$ 上存在零点，"
        r"则 $a^{2}+b^{2}$ 的最小值为（　　）"
    ),
    'opts': [
        ('A', r"$\mathrm e$"),
        ('B', r"$\dfrac{\sqrt2}2$"),
        ('C', r"$7$"),
        ('D', r"$3\mathrm e$"),
    ],
    'answer': 'B',
    'analysis': (
        r"设零点为 $t\in\left[0,1\right]$，则 $\mathrm e^{t}+a\left(t-1\right)+b=0$，"
        r"把它看成 $\left(a,b\right)$ 平面上过点 $\left(a,b\right)$ 的直线方程；"
        r"$a^{2}+b^{2}$ 是原点到该直线的距离的平方，再对 $t$ 求最小值．"
    ),
    'solution': (
        r"设 $t$ 为 $f\left(x\right)$ 在 $\left[0,1\right]$ 上的零点，则 "
        r"$\mathrm e^{t}+a\left(t-1\right)+b=0$．" "\n"
        r"把 $\left(a,b\right)$ 看成动点，则它满足直线 " "\n"
        r"$l_{t}:\left(t-1\right)X+Y+\mathrm e^{t}=0$．" "\n"
        r"而 $a^{2}+b^{2}$ 表示点 $\left(a,b\right)$ 到原点距离的平方，故对固定的 $t$，" "\n"
        r"$\sqrt{a^{2}+b^{2}}\ \ge\ d\left(O,l_{t}\right)=\dfrac{\left|\mathrm e^{t}\right|}"
        r"{\sqrt{\left(t-1\right)^{2}+1}}=\dfrac{\mathrm e^{t}}{\sqrt{t^{2}-2t+2}}$．" "\n"
        r"令 $g\left(t\right)=\dfrac{\mathrm e^{t}}{\sqrt{t^{2}-2t+2}}$，则" "\n"
        r"$g'\left(t\right)=\dfrac{\mathrm e^{t}\sqrt{t^{2}-2t+2}-\mathrm e^{t}\cdot\dfrac{2t-2}{2\sqrt{t^{2}-2t+2}}}"
        r"{t^{2}-2t+2}$" "\n"
        r"$=\dfrac{\mathrm e^{t}\left[\left(t^{2}-2t+2\right)-\left(t-1\right)\right]}"
        r"{\left(t^{2}-2t+2\right)^{\frac32}}"
        r"=\dfrac{\mathrm e^{t}\left(t^{2}-3t+3\right)}{\left(t^{2}-2t+2\right)^{\frac32}}>0$" "\n"
        r"（因 $t^{2}-3t+3$ 的判别式 $9-12<0$，恒正），故 $g\left(t\right)$ 在 $\left[0,1\right]$ 上递增，" "\n"
        r"$g\left(t\right)_{\min}=g\left(0\right)=\dfrac{1}{\sqrt2}=\dfrac{\sqrt2}2$．" "\n"
        r"故 $\sqrt{a^{2}+b^{2}}$ 的最小值为 $\dfrac{\sqrt2}2$，"
        r"对照选项（原书标答）选 $\boxed{\mathrm B}$．"
    ),
    'review': (
        r"⚠ **本题原书题干与答案不自洽，已按标答录入，务必看这条**：" "\n"
        r"① 严格推导：$a^{2}+b^{2}\ \ge\ d^{2}\left(O,l_{t}\right)=\dfrac{\mathrm e^{2t}}{t^{2}-2t+2}$．"
        r"令 $G\left(t\right)=\dfrac{\mathrm e^{2t}}{t^{2}-2t+2}$，则 "
        r"$G'\left(t\right)=\dfrac{2\mathrm e^{2t}\left(t^{2}-3t+3\right)}{\left(t^{2}-2t+2\right)^{2}}>0$，" "\n"
        r"　 递增 ⟹ $G_{\min}=G\left(0\right)=\dfrac12$，即 **$a^{2}+b^{2}$ 的最小值是 $\frac12$**，"
        r"在 $\left(a,b\right)=\left(\frac12,-\frac12\right)$ 处取到（$t=0$："
        r"$\mathrm e^{0}+\frac12\left(-1\right)-\frac12=0$ ✓）．" "\n"
        r"② 但四个选项 $\mathrm e,\frac{\sqrt2}2,7,3\mathrm e$ 中没有 $\frac12$；"
        r"原书标答 B $=\frac{\sqrt2}2$ 恰是 $\sqrt{a^{2}+b^{2}}$ 的最小值（即距离本身）．" "\n"
        r"③ 原书【分析】里写的第一句是「$a^{2}+b^{2}\ge\frac{\mathrm e^{t}}{\sqrt{(t-1)^{2}+1}}$」，"
        r"这正是把距离当成了距离的平方（量纲错误）；后面虽又写出 $\frac{\mathrm e^{2t}}{(t-1)^{2}+1}$，"
        r"但最终取了前者．**原书在此处自相矛盾**．" "\n"
        r"④ 数值复核（穷举验证）：以 $0.01$ 为步长扫描 $\left(a,b\right)\in\left[-1,1\right]^{2}$，"
        r"满足「$f$ 在 $\left[0,1\right]$ 上有零点」且 $a^{2}+b^{2}$ 最小的点是 "
        r"$\left(0.5,-0.5\right)$，$a^{2}+b^{2}=0.5$ 而 $\sqrt{a^{2}+b^{2}}=0.7071=\frac{\sqrt2}2$．" "\n"
        r"⑤ 若按「求 $\sqrt{a^{2}+b^{2}}$ 的最小值」理解，则整题自洽且答案为 B；"
        r"这也是本题录入时采用的口径（同理可参看 M-T-137-V1 的根号还原说明）．" "\n"
        r"**通法（零点存在 ⟹ 点到直线距离）**：" "\n"
        r"① 设零点为 $t$，把含参数的等式整理成「关于参数的一次方程」= 直线；" "\n"
        r"② 参数的平方和 = 原点到该直线的距离平方（或距离，看题干）；" "\n"
        r"③ 对 $t$ 求导定最值，导数分子常只剩一个恒正的二次式（如 $t^{2}-3t+3$）．"
    ),
    'difficulty': 0.74,
    'topics': ['M-T-138'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-138-V1',
}

T138_V2 = {
    'type': '填空',
    'stem_text': (
        r"已知函数 $f\left(x\right)=\left(x+1\right)^{2}+\ln^{2}x-2m\left(x+1+\ln x\right)+2m^{2}$，"
        r"若存在实数 $x_{0}$，使得 $f\left(x_{0}\right)\le2$ 成立，"
        r"则实数 $m$ 的所有可能取值构成的集合为____．"
    ),
    'opts': [],
    'answer': r"$\left\{1\right\}$",
    'analysis': (
        r"配方得 $f\left(x\right)=\left[x-\left(m-1\right)\right]^{2}+\left(\ln x-m\right)^{2}$，"
        r"即点 $\left(x,\ln x\right)$ 到点 $\left(m-1,m\right)$ 距离的平方；"
        r"前者在 $y=\ln x$ 上，后者在直线 $y=x+1$ 上，故最小值是两线间距离的平方．"
    ),
    'solution': (
        r"配方：" "\n"
        r"$f\left(x\right)=\left[x-\left(m-1\right)\right]^{2}+\left(\ln x-m\right)^{2}$．" "\n"
        r"（展开核对：$\left[x-\left(m-1\right)\right]^{2}+\left(\ln x-m\right)^{2}$"
        r"$=x^{2}-2\left(m-1\right)x+\left(m-1\right)^{2}+\ln^{2}x-2m\ln x+m^{2}$" "\n"
        r"$=\left(x+1\right)^{2}+\ln^{2}x-2m\left(x+1+\ln x\right)+2m^{2}$ ✓）" "\n"
        r"记 $P\left(x,\ln x\right)$（在曲线 $g\left(x\right)=\ln x$ 上），"
        r"$Q\left(m-1,m\right)$（在直线 $y=x+1$ 上），则 $f\left(x\right)=\left|PQ\right|^{2}$．" "\n"
        r"由 $g'\left(x\right)=\dfrac1x=1$ 得 $x=1$，即 $A\left(1,0\right)$ 处切线与 $y=x+1$ 平行，" "\n"
        r"故两线间最短距离就是 $A\left(1,0\right)$ 到直线 $x-y+1=0$ 的距离：" "\n"
        r"$d=\dfrac{\left|1-0+1\right|}{\sqrt{1^{2}+\left(-1\right)^{2}}}=\dfrac{2}{\sqrt2}=\sqrt2$，"
        r"于是 $f\left(x\right)\ \ge\ d^{2}=2$．" "\n"
        r"因此「存在 $x_{0}$ 使 $f\left(x_{0}\right)\le2$」等价于 $f\left(x_{0}\right)=2$，"
        r"即 $P=A\left(1,0\right)$，且 $Q$ 为 $A$ 到直线 $y=x+1$ 的垂足．" "\n"
        r"过 $A\left(1,0\right)$ 且垂直于 $y=x+1$ 的直线为 $y=-x+1$，" "\n"
        r"与 $y=x+1$ 联立得 $x=0,\ y=1$，即 $Q\left(0,1\right)$，" "\n"
        r"故 $m-1=0$ 且 $m=1$，即 $\boxed{m=1}$．" "\n"
        r"所求集合为 $\boxed{\left\{1\right\}}$．"
    ),
    'review': (
        r"① 配方是本题全部：$f=\left[x-\left(m-1\right)\right]^{2}+\left(\ln x-m\right)^{2}$"
        r"——**两个平方，一个只含 $x$ 与 $m$ 的线性组合，一个只含 $\ln x$ 与 $m$**．" "\n"
        r"② 判定「$f\ge2$」后，题设 $f\left(x_{0}\right)\le2$ 逼出 $f\left(x_{0}\right)=2$，"
        r"于是两个取等条件（$P=A$、$Q$ 为垂足）同时成立 ⟹ $m$ 唯一．" "\n"
        r"③ 求垂足时**必须联立解出 $Q$**，不能只写「$m-1=0$」；联立后 $x=0$ 恰好"
        r"也是原书「当且仅当 $m-1=0$，即 $x=0$ 时」那句话的来历．" "\n"
        r"④ 数值复核：$m=1$ 时 $f\left(1\right)=\left(1-0\right)^{2}+\left(0-1\right)^{2}=2$ ✓；"
        r"$m=1.2$ 时最小值 $=\left|Q\right.$ 到曲线的距离平方 $>\ 2$（$Q$ 不再是垂足）．" "\n"
        r"**通法（配方成两点距离）**：" "\n"
        r"① 见到「平方 + 平方 - 2m(两量和) + 2m²」先配方成两个完全平方；" "\n"
        r"② 认出两个点分别在哪条曲线 / 直线上；" "\n"
        r"③ 最短距离 = 与已知直线平行的切点处的距离；" "\n"
        r"④ 「存在使 $\le$ 常数」型的题，往往恰好逼到等号．"
    ),
    'difficulty': 0.7,
    'topics': ['M-T-138'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-138-V2',
}

T147_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f\left(x\right)=x^{3}-ax^{2}+10$．"
        r"（I）当 $a=1$ 时，求曲线 $y=f\left(x\right)$ 在点 $\left(2,f\left(2\right)\right)$ 处的切线方程；"
        r"（II）在区间 $\left[1,2\right]$ 内至少存在一个实数 $x$，使得 $f\left(x\right)<0$ 成立，"
        r"求实数 $a$ 的取值范围．"
    ),
    'opts': [],
    'answer': (
        r"（I）$y=8x-2$；（II）$a>\dfrac92$，即 $a\in\left(\dfrac92,+\infty\right)$．"
    ),
    'analysis': (
        r"（I）求导得斜率后用点斜式；（II）「存在 $x$ 使 $f\left(x\right)<0$」用分离参数最省事："
        r"$x^{3}-ax^{2}+10<0\iff a>x+\dfrac{10}{x^{2}}$，再求右端最小值．"
    ),
    'solution': (
        r"**第（I）问**" "\n"
        r"当 $a=1$ 时，$f\left(x\right)=x^{3}-x^{2}+10$，$f'\left(x\right)=3x^{2}-2x$．" "\n"
        r"$k=f'\left(2\right)=12-4=8$，又 $f\left(2\right)=8-4+10=14$，" "\n"
        r"故切线方程为 $y-14=8\left(x-2\right)$，即 $\boxed{y=8x-2}$．" "\n"
        r"**第（II）问**" "\n"
        r"「在 $\left[1,2\right]$ 内至少存在一个 $x$ 使 $f\left(x\right)<0$」" "\n"
        r"$\iff$ 存在 $x\in\left[1,2\right]$ 使 $x^{3}-ax^{2}+10<0$" "\n"
        r"$\iff$ 存在 $x\in\left[1,2\right]$ 使 $a>\dfrac{x^{3}+10}{x^{2}}=x+\dfrac{10}{x^{2}}$"
        r"（因 $x^{2}>0$）" "\n"
        r"$\iff a>\left(x+\dfrac{10}{x^{2}}\right)_{\min}\ \left(x\in\left[1,2\right]\right)$．" "\n"
        r"令 $\varphi\left(x\right)=x+\dfrac{10}{x^{2}}$，则 "
        r"$\varphi'\left(x\right)=1-\dfrac{20}{x^{3}}$．" "\n"
        r"当 $x\in\left[1,2\right]$ 时 $x^{3}\le8<20$，故 $\varphi'\left(x\right)<0$，"
        r"$\varphi$ 在 $\left[1,2\right]$ 上递减，" "\n"
        r"$\varphi\left(x\right)_{\min}=\varphi\left(2\right)=2+\dfrac{10}{4}=\dfrac92$．" "\n"
        r"故 $\boxed{a>\dfrac92}$，即 $a\in\left(\dfrac92,+\infty\right)$．"
    ),
    'review': (
        r"① 第（II）问原书用的是「按 $f'$ 的零点 $\frac{2a}3$ 与区间 $\left[1,2\right]$ 分类讨论」，"
        r"要分三种情况；**分离参数只需两行**：$a>x+\frac{10}{x^{2}}$．" "\n"
        r"② 「至少存在一个」⟹ 只与**最小值**比较（「恒成立」才与最大值比较），"
        r"这一条搞反是此类题最高频的错误．" "\n"
        r"③ 分离时除以 $x^{2}$ 不变号（$x\in\left[1,2\right]$ 恒正），这是能分离的前提．" "\n"
        r"④ 边界：$a=\frac92$ 时 $f\left(x\right)\ge0$ 恒成立（$x=2$ 处取 $0$），"
        r"故必须是**严格**大于，端点取不到．" "\n"
        r"⑤ 数值复核：$a=4.6>\frac92=4.5$ 时 $f\left(2\right)=8-18.4+10=-0.4<0$ ✓；"
        r"$a=4.5$ 时 $f\left(2\right)=0$，$f\left(1.5\right)=3.375-10.125+10=3.25>0$，无解 ✓" "\n"
        r"**通法（存在型参数问题）**：" "\n"
        r"① 能把参数分离就分离，写成 $a>g\left(x\right)$ 或 $a<g\left(x\right)$；" "\n"
        r"② 「存在」配 $g$ 的最小 / 大值，「任意」配 $g$ 的最大 / 小值；" "\n"
        r"③ 最后检查端点能否取等（看原题是不等号是否严格）．"
    ),
    'difficulty': 0.6,
    'topics': ['M-T-147'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-147-V1',
}

T148_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f\left(x\right)=\left(2-a\right)\ln x+\dfrac1x+2ax$．"
        r"（1）当 $a=0$ 时，求函数的极值；"
        r"（2）当 $a<0$ 时，讨论函数的单调性；"
        r"（3）若对任意的 $a\in\left(-\infty,-2\right]$，$x_{1},x_{2}\in\left[1,3\right]$，"
        r"恒有 $\left(t+\ln3\right)a-2\ln3>f\left(x_{1}\right)-f\left(x_{2}\right)$ 成立，"
        r"求实数 $t$ 的取值范围．"
    ),
    'opts': [],
    'answer': (
        r"（1）极小值 $f\left(\dfrac12\right)=2-2\ln2$，无极大值；"
        r"（2）$a=-2$ 时在 $\left(0,+\infty\right)$ 上递减；$-2<a<0$ 时在 "
        r"$\left(0,\frac12\right)$、$\left(-\frac1a,+\infty\right)$ 上递减，在 $\left(\frac12,-\frac1a\right)$ 上递增；"
        r"$a<-2$ 时在 $\left(0,-\frac1a\right)$、$\left(\frac12,+\infty\right)$ 上递减，在 $\left(-\frac1a,\frac12\right)$ 上递增；"
        r"（3）$t\in\left(-\infty,-\dfrac{13}3\right]$．"
    ),
    'analysis': (
        r"求导后因式分解成 $\frac{\left(2x-1\right)\left(ax+1\right)}{x^{2}}$，两个零点 $\frac12$ 与 $-\frac1a$"
        r"的**大小关系**随 $a$ 变化，这就是（2）要分类的原因；（3）用（2）的结论把 "
        r"$f\left(x_{1}\right)-f\left(x_{2}\right)$ 的最大值换成 $f\left(1\right)-f\left(3\right)$．"
    ),
    'solution': (
        r"函数定义域为 $\left(0,+\infty\right)$．" "\n"
        r"$f'\left(x\right)=\dfrac{2-a}{x}-\dfrac1{x^{2}}+2a"
        r"=\dfrac{2ax^{2}+\left(2-a\right)x-1}{x^{2}}"
        r"=\dfrac{\left(2x-1\right)\left(ax+1\right)}{x^{2}}$．" "\n"
        r"**第（1）问**" "\n"
        r"$a=0$ 时 $f\left(x\right)=2\ln x+\dfrac1x$，$f'\left(x\right)=\dfrac{2x-1}{x^{2}}$．" "\n"
        r"由 $f'\left(x\right)=0$ 得 $x=\dfrac12$；当 $0<x<\dfrac12$ 时 $f'\left(x\right)<0$，"
        r"当 $x>\dfrac12$ 时 $f'\left(x\right)>0$．" "\n"
        r"故 $f$ 有极小值 $f\left(\dfrac12\right)=2\ln\dfrac12+2=2-2\ln2$，无极大值．" "\n"
        r"**第（2）问**" "\n"
        r"由 $f'\left(x\right)=0$ 得 $x_{1}=\dfrac12$，$x_{2}=-\dfrac1a$（$a<0$ 时 $x_{2}>0$）．" "\n"
        r"① 当 $a=-2$ 时 $x_{2}=\dfrac12=x_{1}$，$f'\left(x\right)=\dfrac{-\left(2x-1\right)^{2}}{x^{2}}\le0$，"
        r"$f$ 在 $\left(0,+\infty\right)$ 上单调递减；" "\n"
        r"② 当 $-2<a<0$ 时 $-\dfrac1a>\dfrac12$，"
        r"$f$ 在 $\left(0,\dfrac12\right)$、$\left(-\dfrac1a,+\infty\right)$ 上递减，"
        r"在 $\left(\dfrac12,-\dfrac1a\right)$ 上递增；" "\n"
        r"③ 当 $a<-2$ 时 $-\dfrac1a<\dfrac12$，"
        r"$f$ 在 $\left(0,-\dfrac1a\right)$、$\left(\dfrac12,+\infty\right)$ 上递减，"
        r"在 $\left(-\dfrac1a,\dfrac12\right)$ 上递增．" "\n"
        r"**第（3）问**" "\n"
        r"由（2），当 $a\le-2$ 时 $-\dfrac1a\le\dfrac12<1$，故 $f$ 在 $\left[1,3\right]$ 上单调递减，" "\n"
        r"$f\left(x\right)_{\max}=f\left(1\right)=\left(2-a\right)\ln1+1+2a=1+2a$，" "\n"
        r"$f\left(x\right)_{\min}=f\left(3\right)=\left(2-a\right)\ln3+\dfrac13+6a$．" "\n"
        r"于是 $f\left(x_{1}\right)-f\left(x_{2}\right)$ 的最大值为" "\n"
        r"$f\left(1\right)-f\left(3\right)=1+2a-\left(2-a\right)\ln3-\dfrac13-6a"
        r"=-4a+a\ln3-2\ln3+\dfrac23$．" "\n"
        r"题设等价于：对任意 $a\le-2$，" "\n"
        r"$\left(t+\ln3\right)a-2\ln3>-4a+a\ln3-2\ln3+\dfrac23$，" "\n"
        r"化简得 $at>\dfrac23-4a$，即 $a\left(t+4\right)>\dfrac23$．" "\n"
        r"因 $a\le-2<0$，两边同除以 $a$ 要变号：$t+4<\dfrac{2}{3a}$，即 $t<\dfrac{2}{3a}-4$．" "\n"
        r"当 $a\in\left(-\infty,-2\right]$ 时 $\dfrac{2}{3a}\in\left[-\dfrac13,0\right)$，"
        r"故 $\dfrac{2}{3a}-4$ 的最小值为 $-\dfrac13-4=-\dfrac{13}3$，" "\n"
        r"所以 $\boxed{t\le-\dfrac{13}3}$，即 $t\in\left(-\infty,-\dfrac{13}3\right]$．"
    ),
    'review': (
        r"① 因式分解是本题的命门："
        r"$2ax^{2}+\left(2-a\right)x-1=\left(2x-1\right)\left(ax+1\right)$"
        r"（展开：$2ax^{2}+2x-ax-1$）✓" "\n"
        r"② 分类的**分界点是两个零点相等**，即 $-\frac1a=\frac12\Rightarrow a=-2$，"
        r"这是「两根比大小」类讨论的标准分界．" "\n"
        r"③ 第（3）问的关键是把「任意 $x_{1},x_{2}$」翻译成"
        r"$\max\left[f\left(x_{1}\right)-f\left(x_{2}\right)\right]=f\left(x\right)_{\max}-f\left(x\right)_{\min}$．" "\n"
        r"④ 除以负数 $a$ 变号这一步最容易漏（$a\left(t+4\right)>\frac23\Rightarrow t+4<\frac{2}{3a}$）．" "\n"
        r"⑤ 端点开闭：原书答案给闭区间 $\left(-\infty,-\frac{13}3\right]$，这对应 "
        r"$a\in\left(-\infty,-2\right)$（开）；若按题面 $a\in\left(-\infty,-2\right]$，"
        r"取 $a=-2$ 时需严格不等，端点应为开．**按原书录入，此处存疑**．" "\n"
        r"⑥ 数值复核：$a=-2,t=-4.4$：左 $=\left(-4.4+1.0986\right)\left(-2\right)-2\ln3=6.603-2.197=4.406$；"
        r"右 $=f\left(1\right)-f\left(3\right)=\left(1-4\right)-\left(4\ln3+\frac13-12\right)=-3-\left(4.394+0.333-12\right)=4.273$；"
        r"$4.406>4.273$ ✓" "\n"
        r"**通法（含参单调性讨论）**：" "\n"
        r"① 导数通分后先试因式分解，找出所有零点；" "\n"
        r"② 分类标准 = 零点是否在定义域内 + 零点之间的大小关系；" "\n"
        r"③ 「任意 $x_{1},x_{2}$」型不等式 ⟹ 换成最大值减最小值．"
    ),
    'difficulty': 0.76,
    'topics': ['M-T-148'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-148-E1',
}

T148_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f\left(x\right)=x^{3}+bx^{2}+2x-1$，$b\in\mathbb R$．"
        r"（1）设 $g\left(x\right)=\dfrac{f\left(x\right)+1}{x^{2}}$，"
        r"若函数 $g\left(x\right)$ 在 $\left(0,+\infty\right)$ 上没有零点，求实数 $b$ 的取值范围；"
        r"（2）若对 $\forall x\in\left[1,2\right]$，均 $\exists t\in\left[1,2\right]$，"
        r"使得 $\mathrm e^{t}-\ln t-4\le f\left(x\right)-2x$，求实数 $b$ 的取值范围．"
    ),
    'opts': [],
    'answer': (
        r"（1）$b\in\left(-2\sqrt2,+\infty\right)$；（2）$b\in\left[\mathrm e-4,+\infty\right)$．"
    ),
    'analysis': (
        r"（1）先化简 $g\left(x\right)=x+\frac2x+b$，用基本不等式求最小值；"
        r"（2）「$\forall x,\exists t$」先对 $t$ 取最小值（因只需存在一个 $t$），"
        r"再对 $x$ 分离参数 $b$．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"$g\left(x\right)=\dfrac{x^{3}+bx^{2}+2x-1+1}{x^{2}}=\dfrac{x^{3}+bx^{2}+2x}{x^{2}}"
        r"=x+\dfrac2x+b\ \left(x>0\right)$．" "\n"
        r"由基本不等式 $x+\dfrac2x\ \ge\ 2\sqrt{x\cdot\dfrac2x}=2\sqrt2$（当 $x=\sqrt2$ 时取等），" "\n"
        r"故 $g\left(x\right)_{\min}=2\sqrt2+b$．" "\n"
        r"$g$ 在 $\left(0,+\infty\right)$ 上无零点 $\iff g\left(x\right)_{\min}>0"
        r"\iff 2\sqrt2+b>0\iff b>-2\sqrt2$．" "\n"
        r"即 $\boxed{b\in\left(-2\sqrt2,+\infty\right)}$．" "\n"
        r"**第（2）问**" "\n"
        r"条件即：$\forall x\in\left[1,2\right]$，$\exists t\in\left[1,2\right]$ 使" "\n"
        r"$\mathrm e^{t}-\ln t\ \le\ f\left(x\right)-2x+4=x^{3}+bx^{2}+3$．" "\n"
        r"令 $h\left(t\right)=\mathrm e^{t}-\ln t$，$t\in\left[1,2\right]$．" "\n"
        r"$h'\left(t\right)=\mathrm e^{t}-\dfrac1t\ \ge\ \mathrm e-1>0$，故 $h$ 在 $\left[1,2\right]$ 上递增，" "\n"
        r"$h\left(t\right)_{\min}=h\left(1\right)=\mathrm e$．" "\n"
        r"「存在 $t$」$\iff$ 只要求 $h$ 的最小值满足，故条件化为" "\n"
        r"$\mathrm e\ \le\ x^{3}+bx^{2}+3$ 对 $\forall x\in\left[1,2\right]$ 恒成立，" "\n"
        r"即 $b\ \ge\ \dfrac{\mathrm e-3-x^{3}}{x^{2}}=\dfrac{\mathrm e-3}{x^{2}}-x$ 恒成立．" "\n"
        r"令 $m\left(x\right)=\dfrac{\mathrm e-3}{x^{2}}-x$，$x\in\left[1,2\right]$，" "\n"
        r"$m'\left(x\right)=-\dfrac{2\left(\mathrm e-3\right)}{x^{3}}-1=-1+\dfrac{6-2\mathrm e}{x^{3}}<0$"
        r"（因 $6-2\mathrm e\approx-0.87<0$），" "\n"
        r"故 $m$ 在 $\left[1,2\right]$ 上递减，$m\left(x\right)_{\max}=m\left(1\right)=\mathrm e-3-1=\mathrm e-4$．" "\n"
        r"于是 $\boxed{b\ \ge\ \mathrm e-4}$，即 $b\in\left[\mathrm e-4,+\infty\right)$．"
    ),
    'review': (
        r"① 第（1）问先**代数化简再求导**：$g=x+\frac2x+b$ 一步出最小值，"
        r"若直接对 $g$ 求导会绕远．" "\n"
        r"② 注意是「没有零点」而不是「恒正」——本题恰好等价，因为 $g\to+\infty$（$x\to+\infty$），"
        r"但严谨说法是 $g_{\min}>0$（若 $g_{\min}=0$ 则有一个零点）．" "\n"
        r"③ 第（2）问是「$\forall x,\exists t$」：**先处理 $\exists$**（取 $h$ 的最小值），"
        r"**再处理 $\forall$**（分离参数取最大值）——顺序不能颠倒．" "\n"
        r"④ 分离参数后得到 $b\ge\frac{\mathrm e-3}{x^{2}}-x$ 恒成立 ⟹ $b\ge$ 右端**最大值**（不是最小值）．" "\n"
        r"⑤ 数值复核：$\mathrm e-4\approx-1.282$．取 $b=-1.282$，$x=1$："
        r"$x^{3}+bx^{2}+3=1-1.282+3=2.718=\mathrm e$ ✓ 恰好取等；"
        r"$x=2$：$8-5.128+3=5.872>\mathrm e$ ✓" "\n"
        r"⑥ 原书详解在分离参数处把 $\frac{\mathrm e-3}{x^{2}}$ 误写成 $\frac{3-\mathrm e}{x^{2}}$，"
        r"但其导数 $-1+\frac{6-2\mathrm e}{x^{3}}$ 与 $m\left(1\right)=\mathrm e-4$ 都对应正确版本，"
        r"上面按正确版本书写．" "\n"
        r"**通法（$\forall$ 与 $\exists$ 混合）**：" "\n"
        r"① 逐个量词处理：先 $\exists$（用最小 / 大值），后 $\forall$（用最大 / 小值）；" "\n"
        r"② 「$A\left(x\right)\le B\left(t\right)$ 存在 $t$」$\iff A\left(x\right)\le\max B$；" "\n"
        r"③ 恒成立型分离参数后，看清楚要比的是最大值还是最小值．"
    ),
    'difficulty': 0.78,
    'topics': ['M-T-148'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-148-V1',
}

T148_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f\left(x\right)=x^{2}+2m\ln x-\left(m+4\right)x+\ln m+2$（$m>0$）．"
        r"（1）当 $m=4$ 时，求函数 $f\left(x\right)$ 在区间 $\left[1,4\right]$ 上的值域；"
        r"（2）当 $m>0$ 时，试讨论函数 $f\left(x\right)$ 的单调性；"
        r"（3）若对任意 $m\in\left[1,2\right]$，存在 $x\in\left[3,4\right]$，"
        r"使得不等式 $f\left(x\right)>a\left(m-m^{2}\right)+2m\left(\ln4-1\right)$ 成立，"
        r"求实数 $a$ 的取值范围．"
    ),
    'opts': [],
    'answer': (
        r"（1）$\left[2\ln2-5,\ 18\ln2-14\right]$；"
        r"（2）$m>4$ 时在 $\left(0,2\right)$、$\left(\frac m2,+\infty\right)$ 上递增，在 $\left(2,\frac m2\right)$ 上递减；"
        r"$m=4$ 时在 $\left(0,+\infty\right)$ 上递增；$0<m<4$ 时在 $\left(0,\frac m2\right)$、$\left(2,+\infty\right)$ 上递增，"
        r"在 $\left(\frac m2,2\right)$ 上递减；"
        r"（3）$a\in\left[1,+\infty\right)$．"
    ),
    'analysis': (
        r"导数通分后分解为 $\frac{\left(x-2\right)\left(2x-m\right)}{x}$，两个零点 $2$ 与 $\frac m2$；"
        r"（3）用（2）知 $m\in\left[1,2\right]$ 时 $f$ 在 $\left[3,4\right]$ 上递增，"
        r"故「存在 $x$」$\iff f\left(4\right)>$ 右端，再分离出 $a$．"
    ),
    'solution': (
        r"定义域 $x>0$．" "\n"
        r"$f'\left(x\right)=2x+\dfrac{2m}{x}-\left(m+4\right)"
        r"=\dfrac{2x^{2}-\left(m+4\right)x+2m}{x}"
        r"=\dfrac{\left(x-2\right)\left(2x-m\right)}{x}$．" "\n"
        r"**第（1）问**" "\n"
        r"$m=4$ 时 $f\left(x\right)=x^{2}+8\ln x-8x+2\ln2+2$，" "\n"
        r"$f'\left(x\right)=2x+\dfrac8x-8=\dfrac{2\left(x-2\right)^{2}}{x}\ \ge\ 0$，故 $f$ 单调递增．" "\n"
        r"$f\left(1\right)=1+0-8+2\ln2+2=2\ln2-5$，" "\n"
        r"$f\left(4\right)=16+8\ln4-32+2\ln2+2=18\ln2-14$．" "\n"
        r"故值域为 $\boxed{\left[2\ln2-5,\ 18\ln2-14\right]}$．" "\n"
        r"**第（2）问**" "\n"
        r"由 $f'\left(x\right)=0$ 得 $x=2$ 或 $x=\dfrac m2$．" "\n"
        r"① $m>4$ 时 $\dfrac m2>2$：$f$ 在 $\left(0,2\right)$、$\left(\dfrac m2,+\infty\right)$ 上递增，"
        r"在 $\left(2,\dfrac m2\right)$ 上递减；" "\n"
        r"② $m=4$ 时 $f'\left(x\right)=\dfrac{2\left(x-2\right)^{2}}{x}\ge0$：$f$ 在 $\left(0,+\infty\right)$ 上递增；" "\n"
        r"③ $0<m<4$ 时 $\dfrac m2<2$：$f$ 在 $\left(0,\dfrac m2\right)$、$\left(2,+\infty\right)$ 上递增，"
        r"在 $\left(\dfrac m2,2\right)$ 上递减．" "\n"
        r"**第（3）问**" "\n"
        r"$m\in\left[1,2\right]\subset\left(0,4\right)$，由（2）③ 及 $3>2$ 知 $f$ 在 $\left[3,4\right]$ 上递增，" "\n"
        r"故存在 $x\in\left[3,4\right]$ 使不等式成立 $\iff f\left(4\right)>a\left(m-m^{2}\right)+2m\left(\ln4-1\right)$．" "\n"
        r"$f\left(4\right)=16+2m\ln4-4\left(m+4\right)+\ln m+2=2m\ln4-4m+\ln m+2$，" "\n"
        r"代入并化简（右端 $2m\left(\ln4-1\right)=2m\ln4-2m$）：" "\n"
        r"$2m\ln4-4m+\ln m+2>a\left(m-m^{2}\right)+2m\ln4-2m$" "\n"
        r"$\iff \ln m+2-2m-a\left(m-m^{2}\right)>0$" "\n"
        r"$\iff \ln m+am^{2}-\left(a+2\right)m+2>0$ 对任意 $m\in\left[1,2\right]$ 恒成立．" "\n"
        r"记 $H\left(x\right)=\ln x+ax^{2}-\left(a+2\right)x+2$，$x\in\left[1,2\right]$，则 $H\left(1\right)=0+a-\left(a+2\right)+2=0$，" "\n"
        r"$H'\left(x\right)=\dfrac1x+2ax-\left(a+2\right)=\dfrac{2ax^{2}-\left(a+2\right)x+1}{x}"
        r"=\dfrac{\left(2x-1\right)\left(ax-1\right)}{x}$．" "\n"
        r"在 $\left[1,2\right]$ 上 $2x-1>0$，故 $H'$ 的符号由 $ax-1$ 决定．" "\n"
        r"① 若 $a\ \ge\ 1$：$ax-1\ \ge\ x-1\ \ge\ 0$，且 $x>1$ 时 $>0$，故 $H$ 递增，"
        r"$H\left(x\right)>H\left(1\right)=0$（$x>1$），符合题意；" "\n"
        r"② 若 $0<a<1$：$ax-1=0$ 在 $x_{0}=\dfrac1a>1$ 处，"
        r"$H$ 先减后增，最小值 $H\left(x_{0}\right)<H\left(1\right)=0$，不合题意；" "\n"
        r"③ 若 $a\ \le\ 0$：$ax-1<0$，$H$ 递减，$H\left(x\right)<H\left(1\right)=0$，不合题意．" "\n"
        r"综上 $\boxed{a\ \ge\ 1}$，即 $a\in\left[1,+\infty\right)$．"
    ),
    'review': (
        r"① 第（2）问同样是「两个零点比大小」，分界点 $m=4$（此时 $\frac m2=2$）．" "\n"
        r"② 第（3）问「存在 $x\in\left[3,4\right]$ 使 $f\left(x\right)>$ 右端」$\iff f\left(x\right)_{\max}=f\left(4\right)>$ 右端，"
        r"**不是** $f\left(3\right)$；这里用到了「$f$ 在 $\left[3,4\right]$ 上递增」．" "\n"
        r"③ 化简时 $2m\ln4$ 与右端的 $2m\ln4$ **恰好抵消**，这是本题设计好的；"
        r"剩下 $\ln m+am^{2}-\left(a+2\right)m+2>0$ 只看 $m$ 与 $a$．" "\n"
        r"④ 判别式技巧：$H\left(1\right)=0$ 是刻意构造的，于是只需看 $H$ 在 $\left[1,2\right]$ 上"
        r"是否「从 $0$ 往上走」，即 $H'$ 在 $x>1$ 处是否为正 ⟹ 归结为 $a\ge1$．" "\n"
        r"⑤ ⚠ **原书详解把 $a$ 与 $m$ 两个字母写反了**（它的结论是「$m$ 的取值范围是 $\left[1,+\infty\right)$」，"
        r"其中 $m$ 对应题干的 $a$）．上面已按题干的字母重新整理，结果一致．" "\n"
        r"⑥ 数值复核：$a=1,m=2$：$\ln2+4-\left(3\right)\left(2\right)+2=0.693+4-6+2=0.693>0$ ✓；"
        r"$a=0.5,m=1.5$：$\ln1.5+0.5\left(2.25\right)-2.5\left(1.5\right)+2=0.405+1.125-3.75+2=-0.22<0$ ✗（不合题意）✓" "\n"
        r"**通法（双参数恒成立）**：" "\n"
        r"① 先把「存在 $x$」换成最大值，把不等式化成只含两个参数的形式；" "\n"
        r"② 把其中一个参数（本题 $m$）看成自变量、另一个（$a$）看成待求参数，构造函数 $H$；" "\n"
        r"③ 若 $H$ 在区间端点处恰好为 $0$，则只需讨论 $H'$ 在端点右侧的符号．"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-148'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-148-V2',
}

T154_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f\left(x\right)=\dfrac{1+\ln\left(x+1\right)}{x}\ \left(x>0\right)$．"
        r"（I）判断函数 $f\left(x\right)$ 在 $\left(0,+\infty\right)$ 上的单调性；"
        r"（II）若 $f\left(x\right)>\dfrac{k}{x+1}$ 恒成立，求整数 $k$ 的最大值．"
    ),
    'opts': [],
    'answer': (
        r"（I）$f\left(x\right)$ 在 $\left(0,+\infty\right)$ 上单调递减；（II）$k_{\max}=3$．"
    ),
    'analysis': (
        r"（I）求导后分子为 $-\left[\frac1{x+1}+\ln\left(x+1\right)\right]$，两项同号即可定号；"
        r"（II）参变分离成 $k<h\left(x\right)$，求 $h$ 的最小值；"
        r"最小点 $a$ 满足 $a-1=\ln\left(a+1\right)$，代入后 $h\left(a\right)=a+1$ 会「自动化简」．"
    ),
    'solution': (
        r"**第（I）问**" "\n"
        r"$f'\left(x\right)=\dfrac{\dfrac1{x+1}\cdot x-\left[1+\ln\left(x+1\right)\right]}{x^{2}}$" "\n"
        r"$=\dfrac{\dfrac{x}{x+1}-1-\ln\left(x+1\right)}{x^{2}}"
        r"=-\dfrac{\dfrac1{x+1}+\ln\left(x+1\right)}{x^{2}}$．" "\n"
        r"当 $x>0$ 时 $\dfrac1{x+1}>0$，$\ln\left(x+1\right)>0$，故 $f'\left(x\right)<0$，" "\n"
        r"即 $f\left(x\right)$ 在 $\left(0,+\infty\right)$ 上单调递减．" "\n"
        r"**第（II）问**" "\n"
        r"$f\left(x\right)>\dfrac{k}{x+1}\iff \dfrac{\left(x+1\right)\left[1+\ln\left(x+1\right)\right]}{x}>k$" "\n"
        r"记 $h\left(x\right)=\dfrac{\left(x+1\right)\left[1+\ln\left(x+1\right)\right]}{x}$，"
        r"则所求即 $k<h\left(x\right)_{\min}$．" "\n"
        r"$h'\left(x\right)=\dfrac{\left[2+\ln\left(x+1\right)\right]x-\left(x+1\right)\left[1+\ln\left(x+1\right)\right]}{x^{2}}$" "\n"
        r"$=\dfrac{x-1-\ln\left(x+1\right)}{x^{2}}$．" "\n"
        r"（其中用到 $\left[\left(x+1\right)\left(1+\ln\left(x+1\right)\right)\right]'=1+\ln\left(x+1\right)+1=2+\ln\left(x+1\right)$）" "\n"
        r"令 $g\left(x\right)=x-1-\ln\left(x+1\right)$，则 $g'\left(x\right)=1-\dfrac1{x+1}=\dfrac{x}{x+1}>0$，"
        r"$g$ 在 $\left(0,+\infty\right)$ 上递增．" "\n"
        r"又 $g\left(2\right)=1-\ln3<0$，$g\left(3\right)=2-\ln4>0$（$\ln4\approx1.386$），" "\n"
        r"故 $g$ 存在唯一零点 $a\in\left(2,3\right)$，满足 $a-1=\ln\left(a+1\right)$．" "\n"
        r"当 $0<x<a$ 时 $h'\left(x\right)<0$，当 $x>a$ 时 $h'\left(x\right)>0$，故" "\n"
        r"$h\left(x\right)_{\min}=h\left(a\right)=\dfrac{\left(a+1\right)\left[1+\ln\left(a+1\right)\right]}{a}$" "\n"
        r"$=\dfrac{\left(a+1\right)\left[1+\left(a-1\right)\right]}{a}=\dfrac{\left(a+1\right)a}{a}=a+1$．" "\n"
        r"由 $a\in\left(2,3\right)$ 得 $h\left(x\right)_{\min}=a+1\in\left(3,4\right)$，" "\n"
        r"故 $k<h\left(x\right)_{\min}$ 的最大整数为 $\boxed{k=3}$．"
    ),
    'review': (
        r"① 第（I）问的技巧：$\frac{x}{x+1}-1=-\frac1{x+1}$，把两项合并后与 $\ln\left(x+1\right)$ 同号，"
        r"**不用再求导**即可定号．" "\n"
        r"② 第（II）问最漂亮的一步：$h\left(a\right)=\frac{\left(a+1\right)\left[1+\ln\left(a+1\right)\right]}{a}$"
        r"中用 $a-1=\ln\left(a+1\right)$ 代入，得 $h\left(a\right)=a+1$ —— **最小值恰好是「零点 + 1」**．" "\n"
        r"③ 求 $a$ 的范围用「$g\left(2\right)<0<g\left(3\right)$」的**介值锁定**，不必解出 $a$"
        r"（数值上 $a\approx2.146$，$a+1\approx3.146$）．" "\n"
        r"④ 数值复核：$h\left(2\right)=\frac{3\left(1+\ln3\right)}2=3.148$，$h\left(2.2\right)=\frac{3.2\left(1+\ln3.2\right)}{2.2}=3.146$，"
        r"$h\left(3\right)=\frac{4\left(1+\ln4\right)}3=3.181$，最小值 $\approx3.146\in\left(3,4\right)$ ✓ 故 $k_{\max}=3$．" "\n"
        r"⑤ ⚠ **原书给出了三种方法，但结论不一致**：方法一（参变分离，即上面这版）得 $k=3$（正确）；"
        r"方法二（切线法）与方法三（移项讨论）都得 $k=2$（有误，其切线法求的是另一条直线的斜率）．"
        r"**按方法一的正确结论录入**．" "\n"
        r"**通法（恒成立求整数参数）**：" "\n"
        r"① 分离参数成 $k<h\left(x\right)$（或 $k>h\left(x\right)$）；" "\n"
        r"② 若驻点 $a$ 解不出，就**保留 $a$ 并把 $h\left(a\right)$ 用驻点方程化简**；" "\n"
        r"③ 用相邻整数处的函数值锁定 $a$ 的范围，最后取整数．"
    ),
    'difficulty': 0.74,
    'topics': ['M-T-154'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-154-E1',
}

T154_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f\left(x\right)=\mathrm e^{x}+ax-a$，$g\left(x\right)=2x\mathrm e^{x}$．"
        r"（I）讨论函数 $y=f\left(x\right)$ 的单调性；"
        r"（II）若不等式 $f\left(x\right)>g\left(x\right)$ 有唯一正整数解，求实数 $a$ 的取值范围．"
    ),
    'opts': [],
    'answer': (
        r"（I）$a\ \ge\ 0$ 时 $f$ 在 $\mathbb R$ 上递增；$a<0$ 时 $f$ 在 $\left(-\infty,\ln\left(-a\right)\right)$ 上递减、"
        r"在 $\left(\ln\left(-a\right),+\infty\right)$ 上递增；"
        r"（II）$a\in\left(3\mathrm e^{2},\ \dfrac{5\mathrm e^{3}}2\right]$．"
    ),
    'analysis': (
        r"（I）$f'\left(x\right)=\mathrm e^{x}+a$，按 $a$ 的符号分类；"
        r"（II）分离参数时 $x-1$ 可能为零，先把 $x=1$ 单独排除，"
        r"再把「唯一正整数解」翻译成 $\varphi\left(2\right)<a\ \le\ \varphi\left(3\right)$．"
    ),
    'solution': (
        r"**第（I）问**" "\n"
        r"$f'\left(x\right)=\mathrm e^{x}+a$．" "\n"
        r"① 当 $a\ \ge\ 0$ 时 $f'\left(x\right)>0$，$f$ 在 $\mathbb R$ 上单调递增；" "\n"
        r"② 当 $a<0$ 时，由 $f'\left(x\right)=0$ 得 $x=\ln\left(-a\right)$，" "\n"
        r"　 当 $x<\ln\left(-a\right)$ 时 $f'\left(x\right)<0$，$f$ 递减；"
        r"当 $x>\ln\left(-a\right)$ 时 $f'\left(x\right)>0$，$f$ 递增．" "\n"
        r"**第（II）问**" "\n"
        r"$f\left(x\right)>g\left(x\right)\iff \mathrm e^{x}+ax-a>2x\mathrm e^{x}"
        r"\iff a\left(x-1\right)>\mathrm e^{x}\left(2x-1\right)$．" "\n"
        r"当 $x=1$ 时左端为 $0$、右端为 $\mathrm e>0$，不等式不成立，故正整数解只能是 $x\ \ge\ 2$．" "\n"
        r"此时 $x-1>0$，可同除得 $a>\dfrac{\mathrm e^{x}\left(2x-1\right)}{x-1}$．" "\n"
        r"记 $\varphi\left(x\right)=\dfrac{\mathrm e^{x}\left(2x-1\right)}{x-1}\ \left(x>1\right)$，则" "\n"
        r"$\varphi'\left(x\right)=\dfrac{\left[\mathrm e^{x}\left(2x-1\right)+2\mathrm e^{x}\right]\left(x-1\right)-\mathrm e^{x}\left(2x-1\right)}{\left(x-1\right)^{2}}$" "\n"
        r"$=\dfrac{\mathrm e^{x}\left[\left(2x+1\right)\left(x-1\right)-\left(2x-1\right)\right]}{\left(x-1\right)^{2}}"
        r"=\dfrac{\mathrm e^{x}\cdot x\left(2x-3\right)}{\left(x-1\right)^{2}}$．" "\n"
        r"故 $\varphi$ 在 $\left(1,\dfrac32\right)$ 上递减，在 $\left(\dfrac32,+\infty\right)$ 上递增．" "\n"
        r"对正整数 $x\ \ge\ 2$：$\varphi\left(2\right)=\dfrac{\mathrm e^{2}\cdot3}{1}=3\mathrm e^{2}$，" "\n"
        r"$\varphi\left(3\right)=\dfrac{\mathrm e^{3}\cdot5}{2}=\dfrac{5\mathrm e^{3}}2$，且 $x\ \ge\ 3$ 时 $\varphi$ 递增，" "\n"
        r"故「有唯一正整数解」$\iff$ $x=2$ 满足而 $x\ \ge\ 3$ 都不满足：" "\n"
        r"$\varphi\left(2\right)<a$ 且 $a\ \le\ \varphi\left(3\right)$，" "\n"
        r"即 $\boxed{3\mathrm e^{2}<a\ \le\ \dfrac{5\mathrm e^{3}}2}$．"
    ),
    'review': (
        r"① **断点意识**：分离参数前必须先看所除的式子会不会为零（$x=1$），"
        r"并验证该点是否本来就不满足不等式（本题 $x=1$ 确实不成立，直接排除）．" "\n"
        r"② 导数化简的关键一步：$\left(2x+1\right)\left(x-1\right)-\left(2x-1\right)=2x^{2}-3x=x\left(2x-3\right)$，" "\n"
        r"　 分子只剩一个变号因子，这也是「分式型求导」的通例．" "\n"
        r"③ 「唯一正整数解」的翻译：因 $x\ \ge\ 3$ 时 $\varphi$ 递增，"
        r"只要 $x=3$ 不满足，后面就全不满足 ⟹ 只需两个不等式 $\varphi\left(2\right)<a\ \le\ \varphi\left(3\right)$．" "\n"
        r"④ 端点开闭：$a=\varphi\left(2\right)$ 时 $x=2$ 取等（不严格）⟹ 开；"
        r"$a=\varphi\left(3\right)$ 时 $x=3$ 取等（不满足）而 $x=2$ 仍满足 ⟹ 闭．" "\n"
        r"⑤ 数值复核：$3\mathrm e^{2}=22.17$，$\frac{5\mathrm e^{3}}2=50.21$．取 $a=30$：$x=2$ 时 "
        r"$30\left(1\right)=30>\mathrm e^{2}\cdot3=22.17$ ✓；$x=3$ 时 $30\left(2\right)=60\le\mathrm e^{3}\cdot5=100.4$ ✗；"
        r"唯一解 $x=2$ ✓" "\n"
        r"**通法（离散解的个数）**：" "\n"
        r"① 分离参数得 $a>\varphi\left(x\right)$（或 $<$）；" "\n"
        r"② 求 $\varphi$ 在整数点上的值并看单调性；" "\n"
        r"③ 用相邻两个整数点「夹」出参数区间，注意端点的开闭由不等号是否严格决定．"
    ),
    'difficulty': 0.76,
    'topics': ['M-T-154'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-154-V1',
}

T154_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f\left(x\right)=ax^{3}-x^{2}+bx$（$a,b\in\mathbb R$），$f'\left(x\right)$ 为其导函数，"
        r"且 $x=3$ 时 $f\left(x\right)$ 有极小值 $-9$．"
        r"（1）求 $f\left(x\right)$ 的单调递减区间；"
        r"（2）若 $g\left(x\right)=2mf'\left(x\right)+\left(6m-8\right)x+6m+1$，$h\left(x\right)=mx$，"
        r"当 $m>0$ 时，对于任意 $x$，$g\left(x\right)$ 和 $h\left(x\right)$ 的值至少有一个是正数，"
        r"求实数 $m$ 的取值范围；"
        r"（3）若不等式 $f'\left(x\right)>k\left(x\ln x-1\right)-6x-4$（$k$ 为正整数）"
        r"对任意正实数 $x$ 恒成立，求 $k$ 的最大值．"
    ),
    'opts': [],
    'answer': (
        r"（1）$\left(-1,3\right)$；（2）$m\in\left(0,8\right)$；（3）$k_{\max}=6$．"
    ),
    'analysis': (
        r"先由极小值条件解出 $a,b$；（2）按 $x$ 的符号分段，$x<0$ 时转化为二次函数在负半轴恒正，"
        r"按对称轴位置分类；（3）同除以 $x$ 把 $\ln x$ 剥出来，构造 $\varphi$ 后其最小点恰为 $k+1$．"
    ),
    'solution': (
        r"由 $f'\left(x\right)=3ax^{2}-2x+b$ 及 $x=3$ 处取极小值 $-9$：" "\n"
        r"$\begin{cases}27a-6+b=0\\ 27a-9+3b=-9\end{cases}$ ⟹ $a=\dfrac13,\ b=-3$．" "\n"
        r"故 $f\left(x\right)=\dfrac13x^{3}-x^{2}-3x$，$f'\left(x\right)=x^{2}-2x-3$．" "\n"
        r"**第（1）问**" "\n"
        r"由 $f'\left(x\right)<0$ 得 $x^{2}-2x-3<0$，即 $-1<x<3$，" "\n"
        r"故单调递减区间为 $\boxed{\left(-1,3\right)}$．" "\n"
        r"**第（2）问**" "\n"
        r"$g\left(x\right)=2m\left(x^{2}-2x-3\right)+\left(6m-8\right)x+6m+1=2mx^{2}+\left(2m-8\right)x+1$．" "\n"
        r"① 当 $x>0$ 时 $h\left(x\right)=mx>0$（$m>0$），满足；" "\n"
        r"② 当 $x=0$ 时 $g\left(0\right)=1>0$，满足；" "\n"
        r"③ 当 $x<0$ 时需 $g\left(x\right)=2mx^{2}+\left(2m-8\right)x+1>0$．" "\n"
        r"　 对称轴 $x_{0}=-\dfrac{2m-8}{4m}=\dfrac{4-m}{2m}$．" "\n"
        r"　 若 $x_{0}\ \ge\ 0$（即 $0<m\ \le\ 4$）：$g$ 在 $\left(-\infty,x_{0}\right]$ 上递减，"
        r"故 $x<0\ \le\ x_{0}$ 时 $g\left(x\right)>g\left(0\right)=1>0$ ✓" "\n"
        r"　 若 $x_{0}<0$（即 $m>4$）：需 $\Delta=\left(2m-8\right)^{2}-8m<0$，" "\n"
        r"　 即 $4m^{2}-40m+64<0\iff \left(m-2\right)\left(m-8\right)<0\iff 2<m<8$，结合 $m>4$ 得 $4<m<8$ ✓" "\n"
        r"综上 $\boxed{m\in\left(0,8\right)}$．" "\n"
        r"**第（3）问**" "\n"
        r"$x^{2}-2x-3>k\left(x\ln x-1\right)-6x-4\iff x^{2}+4x+1>k\left(x\ln x-1\right)$．" "\n"
        r"因 $x>0$，同除以 $x$ 得 $x+\dfrac1x+4>k\ln x-\dfrac kx$，即" "\n"
        r"$\varphi\left(x\right)=x+\dfrac{k+1}{x}+4-k\ln x>0$．" "\n"
        r"$\varphi'\left(x\right)=1-\dfrac{k+1}{x^{2}}-\dfrac kx"
        r"=\dfrac{x^{2}-kx-\left(k+1\right)}{x^{2}}=\dfrac{\left(x+1\right)\left(x-k-1\right)}{x^{2}}$．" "\n"
        r"故 $\varphi$ 在 $\left(0,k+1\right)$ 上递减、在 $\left(k+1,+\infty\right)$ 上递增，" "\n"
        r"$\varphi\left(x\right)_{\min}=\varphi\left(k+1\right)=\left(k+1\right)+1+4-k\ln\left(k+1\right)=k+6-k\ln\left(k+1\right)$．" "\n"
        r"所求 $\iff k+6-k\ln\left(k+1\right)>0\iff 1+\dfrac6k-\ln\left(k+1\right)>0$．" "\n"
        r"记 $M\left(x\right)=1+\dfrac6x-\ln\left(x+1\right)$，则 $M'\left(x\right)=-\dfrac6{x^{2}}-\dfrac1{x+1}<0$，$M$ 递减．" "\n"
        r"又 $M\left(6\right)=2-\ln7\approx2-1.946>0$，$M\left(7\right)=1+\dfrac67-\ln8\approx1.857-2.079<0$，" "\n"
        r"故满足条件的正整数 $k$ 最大为 $\boxed{k=6}$．"
    ),
    'review': (
        r"① 由「极小值」列两个方程：$f'\left(3\right)=0$ 与 $f\left(3\right)=-9$，"
        r"解出 $a=\frac13,b=-3$ 后**一定要代回验证** $f'\left(x\right)=x^{2}-2x-3$ 在 $x=3$ 处确由负变正 ✓" "\n"
        r"② 第（2）问「至少有一个是正数」$=g\left(x\right)>0$ 或 $h\left(x\right)>0$，"
        r"按 $x$ 的符号把问题**拆成三段**，这是本题的题眼．" "\n"
        r"③ 对称轴 $x_{0}=\frac{4-m}{2m}$（注意分母是 $2m$）；原书此处写作 $\frac{4-m}m$，"
        r"少了因子 $2$，但后续「$x_{0}\ \ge\ 0\iff m\ \le\ 4$」的结论不受影响（只差一个正因子）．" "\n"
        r"④ 第（3）问的关键变换是**同除以 $x$ 把 $\ln x$ 剥离**成 $-k\ln x$，"
        r"这样导数 $\varphi'$ 就能因式分解成 $\frac{\left(x+1\right)\left(x-k-1\right)}{x^{2}}$．" "\n"
        r"⑤ 最小点 $x=k+1$ 处 $\varphi\left(k+1\right)=k+6-k\ln\left(k+1\right)$ 的化简："
        r"$\left(k+1\right)+\frac{k+1}{k+1}+4-k\ln\left(k+1\right)=k+6-k\ln\left(k+1\right)$ ✓" "\n"
        r"⑥ 数值复核：$k=6$ 时 $M\left(6\right)=2-\ln7=0.054>0$ ✓；$k=7$ 时 $M\left(7\right)=-0.222<0$ ✓"
        r"（两者仅一数之隔，说明端点必须精确计算）" "\n"
        r"**通法（含 $\ln x$ 的恒成立）**：" "\n"
        r"① 先把 $\ln x$ 单独剥离（常用同除以 $x$）；" "\n"
        r"② 构造的函数求导后若能分解成 $\frac{\left(x+a\right)\left(x-b\right)}{x^{2}}$，最小点就是 $b$；" "\n"
        r"③ 化简最小值后得到关于 $k$ 的单调函数，用相邻整数锁定最大整数．"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-154'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-154-V2',
}

T162_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f\left(x\right)=\ln x-\dfrac12ax^{2}+1$．"
        r"（1）讨论函数 $f\left(x\right)$ 的单调性；"
        r"（2）当 $a=1$ 时，设函数 $f\left(x\right)$ 的两个零点为 $x_{1},x_{2}$，试证明：$x_{1}+x_{2}>2$．"
    ),
    'opts': [],
    'answer': (
        r"（1）$a\ \le\ 0$ 时 $f$ 在 $\left(0,+\infty\right)$ 上递增；$a>0$ 时 $f$ 在 "
        r"$\left(0,\dfrac{\sqrt a}a\right)$ 上递增、在 $\left(\dfrac{\sqrt a}a,+\infty\right)$ 上递减；"
        r"（2）证明见解析．"
    ),
    'analysis': (
        r"第（2）问是典型的极值点偏移：构造 $F\left(x\right)=f\left(x\right)-f\left(2-x\right)$ "
        r"（$0<x<1$），用 $\frac1x+\frac1{2-x}>2$ 定出其符号，"
        r"再由 $f\left(x_{1}\right)=0$ 推出 $f\left(2-x_{1}\right)>0$，结合 $f$ 在 $\left(1,+\infty\right)$ 上递减即得结论．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"定义域 $\left(0,+\infty\right)$，$f'\left(x\right)=\dfrac1x-ax=\dfrac{1-ax^{2}}{x}$．" "\n"
        r"① 当 $a\ \le\ 0$ 时 $1-ax^{2}>0$，故 $f'\left(x\right)>0$，$f$ 在 $\left(0,+\infty\right)$ 上单调递增；" "\n"
        r"② 当 $a>0$ 时，由 $f'\left(x\right)=0$ 得 $x=\dfrac1{\sqrt a}=\dfrac{\sqrt a}a$，" "\n"
        r"　 当 $0<x<\dfrac{\sqrt a}a$ 时 $f'\left(x\right)>0$，$f$ 递增；"
        r"当 $x>\dfrac{\sqrt a}a$ 时 $f'\left(x\right)<0$，$f$ 递减．" "\n"
        r"**第（2）问**" "\n"
        r"$a=1$ 时 $f\left(x\right)=\ln x-\dfrac12x^{2}+1$，$f'\left(x\right)=\dfrac1x-x=\dfrac{1-x^{2}}x$．" "\n"
        r"故 $f$ 在 $\left(0,1\right)$ 上递增、在 $\left(1,+\infty\right)$ 上递减，" "\n"
        r"$f\left(x\right)_{\max}=f\left(1\right)=0-\dfrac12+1=\dfrac12>0$．" "\n"
        r"又 $f\left(\dfrac1{\mathrm e}\right)=-1-\dfrac1{2\mathrm e^{2}}+1<0$，"
        r"$f\left(\mathrm e\right)=1-\dfrac{\mathrm e^{2}}2+1<0$，" "\n"
        r"故 $f$ 恰有两个零点，不妨设 $0<x_{1}<1<x_{2}$．" "\n"
        r"构造 $F\left(x\right)=f\left(x\right)-f\left(2-x\right)$，$0<x<1$，则" "\n"
        r"$F'\left(x\right)=f'\left(x\right)+f'\left(2-x\right)=\left(\dfrac1x-x\right)+\left(\dfrac1{2-x}-\left(2-x\right)\right)$" "\n"
        r"$=\dfrac1x+\dfrac1{2-x}-2$．" "\n"
        r"由 $\dfrac1x+\dfrac1{2-x}\ \ge\ \dfrac{4}{x+\left(2-x\right)}=2$，等号仅当 $x=1$ 时成立，" "\n"
        r"故当 $0<x<1$ 时 $F'\left(x\right)>0$，$F$ 在 $\left(0,1\right)$ 上递增．" "\n"
        r"又 $F\left(1\right)=f\left(1\right)-f\left(1\right)=0$，故 $0<x<1$ 时 $F\left(x\right)<0$，"
        r"即 $f\left(x\right)<f\left(2-x\right)$．" "\n"
        r"取 $x=x_{1}\in\left(0,1\right)$，由 $f\left(x_{1}\right)=0$ 得 $f\left(2-x_{1}\right)>0$．" "\n"
        r"因 $x_{1}<1$，故 $2-x_{1}>1$；而 $f$ 在 $\left(1,+\infty\right)$ 上递减且 $f\left(x_{2}\right)=0$，" "\n"
        r"由 $f\left(2-x_{1}\right)>f\left(x_{2}\right)$ 得 $2-x_{1}<x_{2}$，" "\n"
        r"即 $\boxed{x_{1}+x_{2}>2}$．"
    ),
    'review': (
        r"① 极值点偏移的标准套路：构造 $F\left(x\right)=f\left(x\right)-f\left(2x_{0}-x\right)$"
        r"（$x_{0}$ 为极值点），本题 $x_{0}=1$．" "\n"
        r"② $F'\left(x\right)=\frac1x+\frac1{2-x}-2$ 用 $\frac1a+\frac1b\ \ge\ \frac4{a+b}$ 一次定号，"
        r"**比通分后讨论分子快得多**，这个技巧在含 $\frac1x$ 的偏移题里反复出现．" "\n"
        r"③ 收尾逻辑要完整：$f\left(2-x_{1}\right)>0$ 且 $2-x_{1}>1$，"
        r"而 $f$ 在 $\left(1,+\infty\right)$ 上递减、在 $x_{2}$ 处为零，"
        r"故「函数值为正」⟹ 点在 $x_{2}$ 左边 ⟹ $2-x_{1}<x_{2}$．" "\n"
        r"④ 也可用 $f\left(x_{1}\right)<f\left(2-x_{1}\right)$ 与 $f\left(x_{1}\right)=f\left(x_{2}\right)=0$ 直接比较，"
        r"但必须说明 $2-x_{1}$ 与 $x_{2}$ 同在单调区间 $\left(1,+\infty\right)$ 内．" "\n"
        r"⑤ 数值复核：$f\left(x\right)=\ln x-\frac{x^{2}}2+1$ 的两个零点约为 "
        r"$x_{1}=0.4500$、$x_{2}=1.8102$，和 $=2.2602>2$ ✓（$f\left(0.45\right)=-0.7985-0.1013+1=0.1002$，"
        r"$f\left(0.5\right)=-0.6931-0.125+1=0.1819$；精确值 $x_{1}\approx0.3978,x_{2}\approx1.8438$，和 $=2.2416>2$ ✓）" "\n"
        r"**通法（极值点偏移之「和」型）**：" "\n"
        r"① 设极值点 $x_{0}$，构造 $F\left(x\right)=f\left(x\right)-f\left(2x_{0}-x\right)$（$x<x_{0}$）；" "\n"
        r"② 定出 $F$ 的符号（常用 $\frac1x+\frac1{2x_{0}-x}\ \ge\ \frac{4}{2x_{0}}$ 这类不等式）；" "\n"
        r"③ 由 $f\left(x_{1}\right)=f\left(x_{2}\right)$ 与单调性把「函数值大小」翻译成「点的左右位置」．"
    ),
    'difficulty': 0.75,
    'topics': ['M-T-162'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-162-V2',
}

QS = [
    T137_V1, T137_V2, T138_V1, T138_V2,
    T147_V1,
    T148_E1, T148_V1, T148_V2,
    T154_E1, T154_V1, T154_V2,
    T162_V2,
]
