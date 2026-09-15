# -*- coding: utf-8 -*-
r"""第 134 批（补录批·五）：攻「提取破碎」27 题，本批裁定 5 题。  python3 tools/run_batch.py 134

## 本批的方法论突破：先回原件，再判破碎

此前把 27 题统一标为「提取破碎」，依据是 `ref_bank` 的提取结果。
本批逐页回查 `原件/按页还原/pXXX.txt` 后发现：**ref_bank 提取失败 ≠ 原题不可录**——
大量详解在原件里是完整的，甚至 ref_bank 自身的 `solution` 字段也有相当多是完整可读的。
真正的「破碎」只占少数。本批据此救回 5 题。

## ★★ 两道选择题的重建

### M-T-374-V3：双曲线离心率（原题完整，此前误判）
选项 `["5/3","5/4","4/3","3/2"]` 在 ref_bank 里是完好的，此前判「选项 OCR 全塌」是误判。
独立推导：$n=|AF_2|=\dfrac{b^2}{2a}$，$m=|AF_1|=n+2a=\dfrac{b^2+4a^2}{2a}$，
$S=\dfrac{b^3}{2a}$，$r=\dfrac Ss=\dfrac{b^3}{a(m+n+2c)}=\dfrac b4$
⟹ $4b^2=b^2+2a^2+2ac$ ⟹ $3c^2-2ac-5a^2=0$ ⟹ $3e^2-2e-5=0$ ⟹ $e=\dfrac53$ ✓ 选 A。

### M-T-303-V3：选项只剩数字碎片，靠独立推导定形
ref_bank 的 opts 是 `["10\n10 ,1","10\n10 ,1","0,\n10\n10","0,\n10\n10"]`——根号与括号全丢。
但题干完整可独立求解：由 $MD=2MA$ 得 $x^2+(y+1)^2=4$，
$\cos\theta=\dfrac y{\sqrt{12-2y}}$ 在 $y\in(0,1)$ 上递增，值域 $\left(0,\dfrac{\sqrt{10}}{10}\right)$。
据此把四项还原为 A.$[\frac{\sqrt{10}}{10},1)$ B.$(\frac{\sqrt{10}}{10},1)$ C.$(0,\frac{\sqrt{10}}{10}]$ D.$(0,\frac{\sqrt{10}}{10})$，选 D。

## ★★ 两道「降级录入」：选项不可还原时改为填空

### M-T-375-V1：椭圆离心率
题干与 808 字详解均完整，唯四选项碎成 `5 5 4 3 / 3 4 3 2` 两行数字且都 $>1$（不可能是离心率），
无法还原。**改为填空**：问离心率，答案 $\dfrac37$。
独立推导：$|PF_1||PF_2|=\dfrac43b^2$，$S=\dfrac{\sqrt3}3b^2$，$r=\dfrac{S}{a+c}$，
由 $|PF_1|=3r\sin\angle F_1F_2P$ 与正弦定理 $\dfrac{|PF_1|}{\sin\angle F_1F_2P}=\dfrac{2c}{\sin\frac\pi3}=\dfrac{4c}{\sqrt3}$
得 $\dfrac{\sqrt3b^2}{a+c}=\dfrac{4c}{\sqrt3}$ ⟹ $3b^2=4c(a+c)$ ⟹ $7e^2+4e-3=0$ ⟹ $e=\dfrac37$ ✓

### M-T-243-V1：向量数量积
opts 四项全部塌成 `ΔABC`，但详解明确：$\overrightarrow{AM}=\dfrac12(\overrightarrow{AB}+\overrightarrow{AC})$，
$\overrightarrow{AB}\cdot\overrightarrow{AO}=\dfrac{AB^2}2=6$，$\overrightarrow{AC}\cdot\overrightarrow{AO}=4$，
故 $\overrightarrow{AM}\cdot\overrightarrow{AO}=\dfrac{6+4}2=5$。**改为填空**，答案 $5$。
（原书答案字段为 C、详解末句写「故选 D」，二者矛盾；改填空后此矛盾自然消解。）
"""

QS = []

# ── 1. M-T-374-V3 双曲线离心率（原题完整）──────────────────────────
QS.append({
    'type': '选择',
    'stem_text': (
        r"已知双曲线 $\dfrac{x^2}{a^2}-\dfrac{y^2}{b^2}=1\ (b>a>0)$ 的左、右焦点分别为 $F_1$，$F_2$，"
        r"过右焦点作平行于一条渐近线的直线交双曲线于点 $A$，"
        r"若 $\triangle AF_1F_2$ 的内切圆半径为 $\dfrac b4$，则双曲线的离心率为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac53$"),
        ('B', r"$\dfrac54$"),
        ('C', r"$\dfrac43$"),
        ('D', r"$\dfrac32$"),
    ],
    'answer': 'A',
    'analysis': (
        r"联立过 $F_2$ 的渐近线平行线与双曲线，得 $A$ 点坐标，进而算出 $|AF_2|$、$|AF_1|$；"
        r"再用等面积法 $S=\dfrac12\cdot\dfrac b4\cdot(m+n+2c)$ 建立关于 $a,c$ 的方程。"
    ),
    'solution': (
        r"设 $F_1(-c,0)$，$F_2(c,0)$，则 $c^2=a^2+b^2$；渐近线为 $y=\dfrac bax$，" "\n"
        r"过 $F_2$ 且平行于此渐近线的直线为 $y=\dfrac ba(x-c)$。" "\n"
        r"与双曲线联立：$\dfrac{x^2}{a^2}-\dfrac{(x-c)^2}{a^2}=1$，即 $x^2-(x-c)^2=a^2$，" "\n"
        r"化简得 $2cx=a^2+c^2$，故 $x_A=\dfrac{a^2+c^2}{2c}$；" "\n"
        r"$y_A=\dfrac ba(x_A-c)=\dfrac ba\cdot\dfrac{a^2-c^2}{2c}=-\dfrac{b^3}{2ac}$。" "\n"
        r"**求 $|AF_2|=n$**：$x_A-c=\dfrac{a^2-c^2}{2c}=-\dfrac{b^2}{2c}$，" "\n"
        r"$n=\sqrt{\left(-\dfrac{b^2}{2c}\right)^2+\left(-\dfrac{b^3}{2ac}\right)^2}"
        r"=\dfrac{b^2}{2c}\sqrt{1+\dfrac{b^2}{a^2}}=\dfrac{b^2}{2c}\cdot\dfrac ca=\dfrac{b^2}{2a}$。" "\n"
        r"由双曲线定义（$A$ 在右支，离 $F_1$ 更远）得 $m-n=2a$，" "\n"
        r"故 $m=|AF_1|=\dfrac{b^2}{2a}+2a=\dfrac{b^2+4a^2}{2a}$，" "\n"
        r"$m+n=\dfrac{b^2+2a^2}{a}$。" "\n"
        r"**等面积法**：$\triangle AF_1F_2$ 以 $F_1F_2$ 为底、$|y_A|$ 为高，" "\n"
        r"$S=\dfrac12\cdot 2c\cdot\dfrac{b^3}{2ac}=\dfrac{b^3}{2a}$；" "\n"
        r"又半周长 $s=\dfrac{m+n+2c}2$，故 $r=\dfrac Ss=\dfrac{b^3}{a(m+n+2c)}=\dfrac b4$。" "\n"
        r"即 $4b^3=ab(m+n+2c)$，约去 $b\ne0$ 得 $4b^2=a(m+n+2c)$，" "\n"
        r"代入 $m+n$：$4b^2=b^2+2a^2+2ac$，即 $3b^2-2a^2=2ac$。" "\n"
        r"由 $b^2=c^2-a^2$ 得 $3c^2-3a^2-2a^2=2ac$，即 $3c^2-2ac-5a^2=0$。" "\n"
        r"两边同除以 $a^2$：$3e^2-2e-5=0$，即 $(3e-5)(e+1)=0$，" "\n"
        r"得 $e=\dfrac53$（$e=-1$ 舍去）。故选 $\mathbf{A}$．"
    ),
    'review': (
        r"① ⭐⭐ **平行渐近线的弦长可直接算出**：联立后 $x^2-(x-c)^2=a^2$ 是一次方程，" "\n"
        r"因为二次项恰好抵消，这是「平行渐近线」带来的必然简化，不必硬解二次方程。" "\n"
        r"② ⭐⭐ **$n=\dfrac{b^2}{2a}$ 是固定结果**，可当公式记；再由定义补 $m=n+2a$。" "\n"
        r"③ ⚠ **$A$ 在右支故 $m-n=2a$ 而非 $n-m$**：$A$ 离 $F_1$ 更远，弄反会得 $e<1$ 的荒谬结果。" "\n"
        r"④ ⭐ 内切圆半径一律用 $r=\dfrac Ss$，而 $s=\dfrac{m+n+2c}2$ 中的 $2c$ 是两焦点距离，别漏。" "\n"
        r"⑤ ⚠ 本题 $b>a>0$，故 $e=\sqrt{1+\frac{b^2}{a^2}}>\sqrt2$，选项只有 $\dfrac53\approx1.67$ 满足，"
        r"可作快速排除。"
    ),
    'topics': ['M-T-374'],
    'src': 'M-T-374-V3',
    'difficulty': 0.72,
})

# ── 2. M-T-303-V3 四棱锥中异面直线夹角（选项重建）──────────────────
QS.append({
    'type': '选择',
    'stem_text': (
        r"在四棱锥 $P-ABCD$ 中，$PA\perp$ 底面 $ABCD$，底面 $ABCD$ 为正方形，$PA=AB=3$，"
        r"点 $M$ 为正方形 $ABCD$ 内部的一点，且 $MD=2MA$，"
        r"则直线 $PM$ 与 $AD$ 所成角的余弦值的取值范围为（　　）"
    ),
    'opts': [
        ('A', r"$\left[\dfrac{\sqrt{10}}{10},1\right)$"),
        ('B', r"$\left(\dfrac{\sqrt{10}}{10},1\right)$"),
        ('C', r"$\left(0,\dfrac{\sqrt{10}}{10}\right]$"),
        ('D', r"$\left(0,\dfrac{\sqrt{10}}{10}\right)$"),
    ],
    'answer': 'D',
    'analysis': (
        r"建系后由 $MD=2MA$ 得 $M$ 的轨迹是圆 $x^2+(y+1)^2=4$ 在正方形内的部分；"
        r"作 $MN\perp AB$ 则 $MN\parallel AD$，$\angle PMN$ 即所求角，其余弦化为 $y$ 的一元函数后单调。"
    ),
    'solution': (
        r"以 $A$ 为原点，分别以 $AB$，$AD$，$AP$ 所在直线为 $x$，$y$，$z$ 轴建系：" "\n"
        r"$A(0,0,0)$，$B(3,0,0)$，$D(0,3,0)$，$P(0,0,3)$。设 $M(x,y,0)$。" "\n"
        r"**定轨迹**：由 $MD=2MA$ 得 $\sqrt{x^2+(y-3)^2}=2\sqrt{x^2+y^2}$，" "\n"
        r"平方：$x^2+(y-3)^2=4(x^2+y^2)$，即 $x^2+y^2-6y+9=4x^2+4y^2$，" "\n"
        r"整理得 $3x^2+3y^2+6y-9=0$，即 $x^2+(y+1)^2=4$。" "\n"
        r"故 $M$ 的轨迹是以 $(0,-1,0)$ 为圆心、$2$ 为半径的圆落在正方形内部的部分。" "\n"
        r"由 $x^2=3-2y-y^2>0$ 且 $M$ 在正方形内（$y>0$）得 $0<y<1$。" "\n"
        r"**求夹角**：过 $M$ 作 $MN\perp AB$ 于 $N(x,0,0)$，则 $MN\parallel AD$，" "\n"
        r"故 $\angle PMN$ 就是直线 $PM$ 与 $AD$ 所成的角。$MN=y$，" "\n"
        r"$PM=\sqrt{x^2+y^2+9}$，而由 $x^2+(y+1)^2=4$ 得 $x^2+y^2=3-2y$，" "\n"
        r"故 $PM=\sqrt{12-2y}$，$\cos\angle PMN=\dfrac{MN}{PM}=\dfrac y{\sqrt{12-2y}}$。" "\n"
        r"令 $f(y)=\dfrac y{\sqrt{12-2y}}$，$y\in(0,1)$，则" "\n"
        r"$f'(y)=\dfrac{\sqrt{12-2y}+\dfrac{y}{\sqrt{12-2y}}}{12-2y}>0$，故 $f$ 严格递增。" "\n"
        r"$y\to0^+$ 时 $f\to0$；$y\to1^-$ 时 $f\to\dfrac1{\sqrt{10}}=\dfrac{\sqrt{10}}{10}$。" "\n"
        r"两端均取不到，故取值范围是 $\left(0,\dfrac{\sqrt{10}}{10}\right)$。故选 $\mathbf{D}$．"
    ),
    'review': (
        r"① ⭐⭐ **$MD=k\cdot MA$ 型条件 ⟹ 阿波罗尼斯圆**：平方后整理必得圆，" "\n"
        r"本题 $x^2+(y+1)^2=4$，圆心被「推」到正方形外，但只有圆落在正方形内的弧可用。" "\n"
        r"② ⭐⭐ **$\cos$ 只含 $y$ 是关键**：$x^2+y^2=3-2y$ 把 $x$ 完全消去，" "\n"
        r"于是二元最值降为一元，这是命题人配好数据的信号。" "\n"
        r"③ ⚠ **两端都开**：$y>0$ 因 $M$ 在正方形「内部」，$y<1$ 因 $x^2>0$（$M$ 不在 $AD$ 上），"
        r"两个端点都取不到，所以选 D 而不是 C。" "\n"
        r"④ ⚠ 原书选项经 OCR 后只剩数字碎片 `10/10 ,1` 与 `0, 10/10`，根号与括号全丢；"
        r"本项由独立推导定形，答案 D 可确认。" "\n"
        r"⑤ ⭐ **作 $MN\perp AB$ 造平行线**是求「与 $AD$ 夹角」的标准手法："
        r"因 $MN\parallel AD$，$\angle PMN$ 即所求，不必用向量夹角公式。"
    ),
    'topics': ['M-T-303'],
    'src': 'M-T-303-V3',
    'difficulty': 0.70,
})

# ── 3. M-T-375-V1 椭圆离心率（降级填空）────────────────────────────
QS.append({
    'type': '填空',
    'stem_text': (
        r"已知椭圆 $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1\ (a>b>0)$ 的焦点为 $F_1$，$F_2$，$P$ 是椭圆上一点，"
        r"且 $2\overrightarrow{PF_1}\cdot\overrightarrow{PF_2}=|\overrightarrow{PF_1}|\cdot|\overrightarrow{PF_2}|$，"
        r"若 $\triangle F_1PF_2$ 的内切圆的半径 $r$ 满足 $|PF_1|=3r\sin\angle F_1F_2P$，"
        r"则椭圆的离心率为 ____"
    ),
    'answer': r"$\dfrac37$",
    'analysis': (
        r"由数量积条件定出 $\angle F_1PF_2=\dfrac\pi3$，余弦定理配椭圆定义得 $|PF_1||PF_2|=\dfrac43b^2$；"
        r"再用 $S=(a+c)r$ 与正弦定理把已知条件 $3r$ 换成 $\dfrac{4c}{\sqrt3}$，即可解出 $e$。"
    ),
    'solution': (
        r"由 $2\overrightarrow{PF_1}\cdot\overrightarrow{PF_2}"
        r"=2|PF_1||PF_2|\cos\angle F_1PF_2=|PF_1||PF_2|$" "\n"
        r"得 $\cos\angle F_1PF_2=\dfrac12$，即 $\angle F_1PF_2=\dfrac\pi3$。" "\n"
        r"由椭圆定义 $|PF_1|+|PF_2|=2a$，由余弦定理" "\n"
        r"$\cos\dfrac\pi3=\dfrac{|PF_1|^2+|PF_2|^2-4c^2}{2|PF_1||PF_2|}"
        r"=\dfrac{4a^2-2|PF_1||PF_2|-4c^2}{2|PF_1||PF_2|}=\dfrac{4b^2-2|PF_1||PF_2|}{2|PF_1||PF_2|}=\dfrac12$，" "\n"
        r"整理得 $|PF_1||PF_2|=\dfrac43b^2$。" "\n"
        r"于是 $S_{\triangle F_1PF_2}=\dfrac12|PF_1||PF_2|\sin\dfrac\pi3"
        r"=\dfrac12\cdot\dfrac43b^2\cdot\dfrac{\sqrt3}2=\dfrac{\sqrt3}3b^2$。" "\n"
        r"又由等面积法，$S_{\triangle F_1PF_2}=\dfrac12(2a+2c)r=(a+c)r$，" "\n"
        r"故 $r=\dfrac{S_{\triangle F_1PF_2}}{a+c}=\dfrac{\sqrt3\,b^2}{3(a+c)}$。" "\n"
        r"由已知 $|PF_1|=3r\sin\angle F_1F_2P$ 得 $\dfrac{|PF_1|}{\sin\angle F_1F_2P}=3r=\dfrac{\sqrt3\,b^2}{a+c}$。" "\n"
        r"在 $\triangle F_1PF_2$ 中由正弦定理，" "\n"
        r"$\dfrac{|PF_1|}{\sin\angle F_1F_2P}=\dfrac{|F_1F_2|}{\sin\angle F_1PF_2}"
        r"=\dfrac{2c}{\sin\frac\pi3}=\dfrac{4c}{\sqrt3}$。" "\n"
        r"故 $\dfrac{\sqrt3\,b^2}{a+c}=\dfrac{4c}{\sqrt3}$，即 $3b^2=4c(a+c)$。" "\n"
        r"代入 $b^2=a^2-c^2$：$3a^2-3c^2=4ac+4c^2$，即 $3a^2-4ac-7c^2=0$。" "\n"
        r"两边同除以 $a^2$：$7e^2+4e-3=0$，即 $(7e-3)(e+1)=0$，" "\n"
        r"得 $e=\dfrac37$（$e=-1$ 舍去）。故答案为 $\dfrac37$．"
    ),
    'review': (
        r"① ⭐⭐ **$S_{\triangle F_1PF_2}=(a+c)r$ 是椭圆焦点三角形的固定结论**：" "\n"
        r"周长 $=2a+2c$，半周长 $=a+c$，一步出 $r$，不必逐边相加。" "\n"
        r"② ⭐⭐ **双条件题的「分工」**：数量积定顶角，余弦定理配定义定两腰之积，"
        r"等面积法定 $r$，正弦定理把 $|PF_1|/\sin$ 换成 $\dfrac{2c}{\sin\frac\pi3}$——四步各司其职。" "\n"
        r"③ ⚠ **正弦定理对应要对齐**：$|PF_1|$ 的对角是 $\angle PF_2F_1$，"
        r"即题中的 $\angle F_1F_2P$，两者是同一个角，不要误配成 $\angle PF_1F_2$。" "\n"
        r"④ ⚠ 原书详解此处有笔误：把 $\dfrac{4c}{\sqrt3}$ 印成 $\dfrac{4c}3$、把 $\dfrac{\sqrt3b^2}{a+c}$ 印成 $\dfrac{3b^2}{a+c}$，"
        r"两处 $\sqrt3$ 丢失；但结论 $3b^2=4c(a+c)$ 与答案 $\dfrac37$ 均正确。" "\n"
        r"⑤ ⚠ 原书四个选项经 OCR 后只剩两行数字碎片，且均大于 $1$，不可能是椭圆离心率，"
        r"无法还原，故本项改为填空题录入。"
    ),
    'topics': ['M-T-375'],
    'src': 'M-T-375-V1',
    'difficulty': 0.75,
})

# ── 4. M-T-109-V1 单调函数求参 ────────────────────────────────────
QS.append({
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=x(x+a)-\ln x$，其中 $a$ 为常数。"
        r"若 $f(x)$ 在区间 $\left(\dfrac12,1\right)$ 上是单调函数，求实数 $a$ 的取值范围．"
    ),
    'answer': r"$(-\infty,-1]\cup[1,+\infty)$",
    'analysis': (
        r"「是单调函数」要分增、减两种情形；各自转化为 $f'(x)\ge0$ 或 $f'(x)\le0$ 恒成立，"
        r"再参变分离。"
    ),
    'solution': (
        r"$f(x)=x^2+ax-\ln x$，定义域 $x>0$，$f'(x)=2x+a-\dfrac1x=\dfrac{2x^2+ax-1}{x}$。" "\n"
        r"因 $x\in\left(\dfrac12,1\right)$ 时 $x>0$，故 $f'(x)$ 的符号由分子 $2x^2+ax-1$ 决定。" "\n"
        r"**① $f(x)$ 是增函数**：$2x^2+ax-1\ge0$ 在 $\left(\dfrac12,1\right)$ 上恒成立，" "\n"
        r"参变分离得 $a\ge\dfrac1x-2x$ 恒成立。设 $y=\dfrac1x-2x$，" "\n"
        r"它在 $\left(\dfrac12,1\right)$ 上单调递减，其上确界为 $x\to\dfrac12^+$ 时的 $2-1=1$，" "\n"
        r"故 $a\ge1$。" "\n"
        r"**② $f(x)$ 是减函数**：$2x^2+ax-1\le0$ 在 $\left(\dfrac12,1\right)$ 上恒成立。" "\n"
        r"设 $g(x)=2x^2+ax-1$，其图象开口向上，故在区间上恒 $\le0$ 等价于两端点均 $\le0$：" "\n"
        r"$g\left(\dfrac12\right)=\dfrac12+\dfrac a2-1=\dfrac{a-1}2\le0$ 且 $g(1)=2+a-1=a+1\le0$，" "\n"
        r"解得 $a\le-1$。" "\n"
        r"综上，$a$ 的取值范围为 $(-\infty,-1]\cup[1,+\infty)$．"
    ),
    'review': (
        r"① ⭐⭐ **「是单调函数」必须分增、减两类**：只讨论递增会漏掉 $a\le-1$ 这支，" "\n"
        r"这是本题最高频的错误。" "\n"
        r"② ⭐⭐ **增函数用参变分离、减函数用端点法**：前者 $a\ge\dfrac1x-2x$ 只需看上确界；"
        r"后者开口向上，区间上恒 $\le0$ 只需两端点 $\le0$，不必讨论对称轴。" "\n"
        r"③ ⚠ **区间开闭不影响结果**：$y=\dfrac1x-2x$ 在 $x=\dfrac12$ 处取到上确界 $1$，"
        r"区间虽开但 $a\ge1$ 不能放松为 $a>1$，因为恒成立要求对一切 $x$ 成立。" "\n"
        r"④ ⭐ $f'(x)=\dfrac{2x^2+ax-1}x$ 先化成整式再分离参数，可避免分式运算出错。"
    ),
    'topics': ['M-T-109'],
    'src': 'M-T-109-V1',
    'difficulty': 0.62,
})

# ── 5. M-T-243-V1 向量数量积（降级填空）────────────────────────────
QS.append({
    'type': '填空',
    'stem_text': (
        r"已知 $\triangle ABC$ 中，$O$ 为外接圆的圆心，且 $\overrightarrow{AB}\cdot\overrightarrow{AO}=6$，"
        r"$\overrightarrow{AC}\cdot\overrightarrow{AO}=4$，$M$ 是 $BC$ 边的中点，"
        r"则 $\overrightarrow{AM}\cdot\overrightarrow{AO}=$ ____"
    ),
    'answer': r"$5$",
    'analysis': (
        r"用中点向量公式把 $\overrightarrow{AM}$ 拆成 $\dfrac12(\overrightarrow{AB}+\overrightarrow{AC})$，"
        r"再分别代入两个已知数量积即可，与三角形形状无关。"
    ),
    'solution': (
        r"因为 $M$ 是 $BC$ 的中点，由中点向量公式" "\n"
        r"$\overrightarrow{AM}=\dfrac12\left(\overrightarrow{AB}+\overrightarrow{AC}\right)$。" "\n"
        r"于是" "\n"
        r"$\overrightarrow{AM}\cdot\overrightarrow{AO}"
        r"=\dfrac12\left(\overrightarrow{AB}+\overrightarrow{AC}\right)\cdot\overrightarrow{AO}"
        r"=\dfrac12\left(\overrightarrow{AB}\cdot\overrightarrow{AO}"
        r"+\overrightarrow{AC}\cdot\overrightarrow{AO}\right)$。" "\n"
        r"代入已知：$\overrightarrow{AM}\cdot\overrightarrow{AO}=\dfrac12(6+4)=5$。" "\n"
        r"故答案为 $5$．"
    ),
    'review': (
        r"① ⭐⭐ **中点的向量式 $\overrightarrow{AM}=\dfrac12(\overrightarrow{AB}+\overrightarrow{AC})$ 是万能钥匙**："
        r"凡出现「$M$ 是 $BC$ 中点」且求与 $\overrightarrow{AM}$ 有关的量，先写这一句。" "\n"
        r"② ⭐⭐ **外心 $O$ 使 $\overrightarrow{AB}\cdot\overrightarrow{AO}=\dfrac{AB^2}2$**："
        r"因 $O$ 在 $AB$ 的中垂线上，$\overrightarrow{AO}$ 在 $\overrightarrow{AB}$ 上的投影恰为 $\dfrac{AB}2$，"
        r"故 $\overrightarrow{AB}\cdot\overrightarrow{AO}=|AB|\cdot\dfrac{|AB|}2=\dfrac{AB^2}2$。"
        r"本题正是据此由 $6$、$4$ 反推出 $AB^2=12$、$AC^2=8$。" "\n"
        r"③ ⚠ **结果与 $\angle A$ 是否为钝角无关**：题目虽给出「$\angle A$ 为钝角」，"
        r"但两个已知数量积已把所需信息给足，该条件在此问中是冗余的。" "\n"
        r"④ ⚠ 原书四个选项经 OCR 后全部塌成 $\triangle ABC$，无法还原；"
        r"且原书答案字段标 C、详解末句写「故选 D」，二者矛盾。改为填空录入后此矛盾自然消解。"
    ),
    'topics': ['M-T-243'],
    'src': 'M-T-243-V1',
    'difficulty': 0.55,
})
