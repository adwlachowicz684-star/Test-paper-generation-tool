# -*- coding: utf-8 -*-
r"""第 97 批：解三角形最值范围（M-T-195，4 题）+ 解三角形范围综合（M-T-197，4 题）
+ 导数构造函数（M-T-123，4 题）+ 三角换元求最值（M-T-184，3 题）

    python3 tools/run_batch.py 97

## 选题依据

按「详解完整 + 同题型聚堆 + 无图依赖」筛出，本批 15 题 11 选择 4 填空。
四个题型原文集中在 p87（M-T-123）、p156–p159（M-T-195/197）、p146（M-T-184），
读 5 页即可录完，是近期密度最高的一批。

## ★★ 本批最值钱的一条：$\dfrac{a-c}{a-b}+\dfrac{a-c}{b-c}$ 型恒成立的定式

M-T-195-V2：
$$\frac1{a-b}+\frac1{b-c}\ge\frac{t}{a-c}\ \Longleftrightarrow\ t\le\frac{a-c}{a-b}+\frac{a-c}{b-c}
=2+\frac{b-c}{a-b}+\frac{a-b}{b-c}$$

**题眼是把 $a-c$ 拆成 $(a-b)+(b-c)$** —— 拆开后每一项都变成「两段之比」，
于是两项互为倒数，基本不等式直接给出 $t_{\max}=4$（取等 $a-b=b-c$）。

> ⭐⭐ 凡是分母是「两段之差」、分子是「全长」的分式，先拆全长。

## ★★ 第二条：$2S=a^2-(b-c)^2$ 的化简（M-T-197-E1）

$$2S=a^2-(b-c)^2\ \Longrightarrow\ bc\sin A=2bc(1-\cos A)\ \Longrightarrow\ \sin A+2\cos A=2$$

配方：$\sin A=2(1-\cos A)$，平方后 $1-\cos^2A=4-8\cos A+4\cos^2A$，
即 $5\cos^2A-8\cos A+3=0$ ⟹ $(5\cos A-3)(\cos A-1)=0$ ⟹ $\cos A=\frac35$（$\cos A=1$ 舍）。

**这条「面积 + 平方差」的组合必出确定的角**，可与 M-T-198-E1 的
$2S=a^2-(b-c)^2\Longrightarrow\tan\frac A2=\frac12$ 对照记忆。

## ★★ 第三条：$\sin A+\sin C$ 在 $B=\frac\pi2+A$ 下的配方（M-T-197-V3）

由 $4bS=a(b^2+c^2-a^2)$ 得 $\sin B=\cos A$，钝角 $B$ 配锐角 $A$ 得 $B=\frac\pi2+A$，
于是 $\sin B=\cos A$、$\cos B=-\sin A$，代入

$$\sin A+\sin C=\sin A(1+\cos B)+\cos A\sin B=1-\cos B-2\cos^2B=-2\left(\cos B+\frac14\right)^2+\frac98$$

**一切都化成 $\cos B$ 的二次函数** —— 这是「两角和已知关系」型最值的通法。

## 四处原书 OCR / 排版错误（判据都写在各题 review 里）

1. **M-T-197-V2 题干**：ref_bank 存成分式，PDF 原文是乘法
   $(a-b)\sin B=a(\sin A+2\sin B)-c\sin C$（见 PDF p158 右栏第 22 题）。
2. **M-T-197-E1 详解**：`b/c = 4/5 tanC + 3/5` 实为 **$\frac45\cot C+\frac35$**
   （否则 $C$ 越大 $\frac bc$ 越大，与随后 $\frac1{\tan C}\in(0,\frac43)$ 的用法自相矛盾）。
3. **M-T-123-V3 详解**：$p'(x)=\frac12-\frac1{x-1}$ 实为 **$\frac12+\frac1{x-1}$**
   （按减号 $p'(2)=-\frac12<0$，与「$p$ 在 $[2,+\infty)$ 递增」及 $p(2)=0$、$p(3)=1.193$ 均矛盾）。
4. **M-T-184-E1/V1 的根号**：$2\sqrt2(x+y)$、$4^x+9^y=1$ 在提取中分别丢成
   `2 2(x+y)`、`4x+9y=1`，由详解中的 $6\sin\theta$、$u^2+v^2=1$ 反推确认。
"""

T195_E1 = {
    'type': '选择',
    'stem_text': (
        r"在锐角 $\triangle ABC$ 中，角 $A,B,C$ 所对的边分别为 $a,b,c$，"
        r"若 $a^{2}+b^{2}=5c^{2}$，则 $\cos C$ 的取值范围是"
    ),
    'opts': [
        ('A', r"$\left(\dfrac12,\dfrac{\sqrt6}3\right)$"),
        ('B', r"$\left(\dfrac12,1\right)$"),
        ('C', r"$\left[\dfrac45,\dfrac{\sqrt6}3\right)$"),
        ('D', r"$\left[\dfrac45,1\right)$"),
    ],
    'answer': 'C',
    'analysis': (
        r"由 $c^{2}=\frac{a^{2}+b^{2}}5$ 把 $\cos C$ 化为 $\frac25\left(\frac ba+\frac ab\right)$，"
        r"再用锐角三角形的三个不等式定出 $\frac ba$ 的范围，最后按对勾函数求值域。"
    ),
    'solution': (
        r"由余弦定理，" "\n"
        r"$\cos C=\dfrac{a^{2}+b^{2}-c^{2}}{2ab}=\dfrac{a^{2}+b^{2}-\frac{a^{2}+b^{2}}5}{2ab}"
        r"=\dfrac{4(a^{2}+b^{2})}{10ab}=\dfrac25\left(\dfrac ba+\dfrac ab\right)$．" "\n"
        r"由基本不等式 $\cos C\ge\frac25\cdot2=\frac45$，当且仅当 $a=b$ 时取等．" "\n"
        r"再由锐角三角形：" "\n"
        r"$a^{2}+b^{2}>c^{2}$，$b^{2}+c^{2}>a^{2}$，$a^{2}+c^{2}>b^{2}$，" "\n"
        r"代入 $c^{2}=\frac{a^{2}+b^{2}}5$ 得 $\dfrac23<\dfrac{b^{2}}{a^{2}}<\dfrac32$，" "\n"
        r"即 $\dfrac{\sqrt6}3<\dfrac ba<\dfrac{\sqrt6}2$．" "\n"
        r"设 $x=\frac ba$，$f(x)=\frac25\left(x+\frac1x\right)$ 在 $\left(\frac{\sqrt6}3,1\right)$ 上递减、"
        r"在 $\left(1,\frac{\sqrt6}2\right)$ 上递增，" "\n"
        r"故 $f_{\min}=f(1)=\frac45$（可取）；两端 $f\left(\frac{\sqrt6}3\right)=f\left(\frac{\sqrt6}2\right)"
        r"=\frac25\left(\frac{\sqrt6}3+\frac3{\sqrt6}\right)=\frac{\sqrt6}3$（取不到）．" "\n"
        r"所以 $\cos C\in\left[\dfrac45,\dfrac{\sqrt6}3\right)$，故选 C．"
    ),
    'review': (
        r"① ⭐⭐ **题眼是 $c^{2}=\frac{a^{2}+b^{2}}5$ 把三边约束变成两边之比**："
        r"代入余弦定理后 $\cos C$ 只剩 $\frac ba+\frac ab$ 这一个变量 ✓✓✓" "\n"
        r"② ⭐⭐ **锐角条件必须三个不等式都列**：只列 $a^{2}+b^{2}>c^{2}$ 得不到 $\frac ba$ 的上界，" "\n"
        r"  正是 $a^{2}+c^{2}>b^{2}$ 给出 $\frac{b^2}{a^2}<\frac32$ ✓✓" "\n"
        r"③ ⭐⭐ **两端函数值相等不是巧合**：$\frac{\sqrt6}3$ 与 $\frac{\sqrt6}2$ 互为倒数，"
        r"而 $x+\frac1x$ 在互为倒数的两点取值相同 ✓✓ 这是自检的好办法．" "\n"
        r"④ ⚠ **开闭**：$a=b$ 时 $c^{2}=\frac{2a^{2}}5$，三个锐角条件全部满足（$2a^2>0.4a^2$、"
        r"$a^2+0.4a^2>a^2$），故下界 $\frac45$ **闭**；上界对应区间端点，开 ✓" "\n"
        r"⑤ 数值验证：$a=b=1$ 时 $c=\sqrt{0.4}=0.6325$，$\cos C=\frac{1+1-0.4}{2}=0.8=\frac45$ ✓；" "\n"
        r"  $x=\frac{\sqrt6}2=1.2247$ 时 $f=\frac25(1.2247+0.8165)=0.8165=\frac{\sqrt6}3$ ✓" "\n"
        r"**⭐⭐ 通法（$pa^{2}+qb^{2}=kc^{2}$ 型求角的范围）**：" "\n"
        r"① ⭐⭐ 先由该式把 $c^{2}$ 表成 $a,b$，代入余弦定理 ⟹ 只剩 $\frac ba+\frac ab$；" "\n"
        r"② ⭐⭐ 再用锐角（或钝角）条件把 $\frac ba$ 限制在一个区间内；" "\n"
        r"③ ⭐⭐ 对勾函数 $mx+\frac nx$ 在 $\left(\sqrt{\frac nm},+\infty\right)$ 递增，"
        r"最小值 $2\sqrt{mn}$ 在 $x=\sqrt{\frac nm}$ 处取得 ✓✓✓"
    ),
    'difficulty': 0.68,
    'topics': ['M-T-195'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-195-E1',
}

T195_V1 = {
    'type': '选择',
    'stem_text': (
        r"在 $\triangle ABC$ 中，角 $A,B,C$ 的对边分别为 $a,b,c$，"
        r"已知 $B=\dfrac\pi6$ 且 $S_{\triangle ABC}=1$，"
        r"则 $\dfrac{a}{ca+c^{2}}+\dfrac{c}{ac+a^{2}}$ 的最小值为"
    ),
    'opts': [
        ('A', r"$\dfrac12$"),
        ('B', r"$2$"),
        ('C', r"$\dfrac14$"),
        ('D', r"$4$"),
    ],
    'answer': 'A',
    'analysis': (
        r"面积给出 $ac=4$；把两式通分合并成 $\frac{a^{2}+c^{2}}{ac(a+c)}$，"
        r"再用 $(a+c)^{2}-2ac$ 换分子，令 $t=a+c$ 即得关于 $t$ 的单调函数。"
    ),
    'solution': (
        r"由 $S_{\triangle ABC}=\dfrac12 ac\sin B=1$，$B=\dfrac\pi6$ 得" "\n"
        r"$1=\dfrac12 ac\cdot\dfrac12$，即 $ac=4$，于是 $a+c\ge2\sqrt{ac}=4$．" "\n"
        r"$\dfrac{a}{ca+c^{2}}+\dfrac{c}{ac+a^{2}}=\dfrac{a}{c(a+c)}+\dfrac{c}{a(c+a)}"
        r"=\dfrac{a^{2}+c^{2}}{ac(a+c)}=\dfrac{(a+c)^{2}-2ac}{ac(a+c)}$．" "\n"
        r"令 $t=a+c\in[4,+\infty)$，则" "\n"
        r"$f(t)=\dfrac{t^{2}-8}{4t}=\dfrac t4-\dfrac2t$ 在 $[4,+\infty)$ 上单调递增，" "\n"
        r"$f(t)_{\min}=f(4)=1-\dfrac12=\dfrac12$，故选 A．"
    ),
    'review': (
        r"① ⭐⭐ **两个分式分母不同但都含 $(a+c)$** —— 通分后分子恰是 $a^{2}+c^{2}$，"
        r"这是「对称分式相加」的典型结果 ✓✓" "\n"
        r"② ⭐⭐ **换元 $t=a+c$ 是这类题的固定动作**：分子 $(a+c)^2-2ac$、分母 $ac(a+c)$ "
        r"都只依赖 $t$（$ac$ 已知），于是双变量降为单变量 ✓✓✓" "\n"
        r"③ ⚠ **单调性不能用基本不等式代替**：$\frac t4-\frac2t$ 递增（两项一增一增），"
        r"直接对 $t+\frac{k}t$ 用基本不等式会找错方向 ✓" "\n"
        r"④ 取等检验：$a=c=2$ 时 $ac=4$ ✓，原式 $=\frac{2}{2\cdot2+4}+\frac{2}{2\cdot2+4}"
        r"=\frac{2}{8}+\frac{2}{8}=\frac12$ ✓" "\n"
        r"**⭐⭐ 通法（已知两边之积求分式最值）**：" "\n"
        r"① ⭐⭐ 面积 + 已知夹角 ⟹ 直接得 $ac$（$S=\frac12 ac\sin B$）；" "\n"
        r"② ⭐⭐ 对称分式通分后分子化为 $(a+c)^{2}-2ac$、分母化为 $ac(a+c)$；" "\n"
        r"③ ⭐⭐ 换元 $t=a+c\ge2\sqrt{ac}$，转成 $t$ 的对勾（或线性）函数求值域 ✓✓"
    ),
    'difficulty': 0.6,
    'topics': ['M-T-195'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-195-V1',
}

T195_V2 = {
    'type': '选择',
    'stem_text': (
        r"在锐角 $\triangle ABC$ 中，角 $A,B,C$ 的对边分别为 $a,b,c$（$a>b>c$），"
        r"已知不等式 $\dfrac1{a-b}+\dfrac1{b-c}\ge\dfrac{t}{a-c}$ 恒成立，"
        r"则当实数 $t$ 取得最大值 $T$ 时，$T\cos B$ 的取值范围是"
    ),
    'opts': [
        ('A', r"$\left(0,\dfrac{12}5\right)$"),
        ('B', r"$\left(2,\dfrac{12}5\right)$"),
        ('C', r"$[2,2\sqrt3]$"),
        ('D', r"$(2,4)$"),
    ],
    'answer': 'B',
    'analysis': (
        r"同乘 $a-c$ 后把 $a-c$ 拆成 $(a-b)+(b-c)$，得 $t\le2+\frac{b-c}{a-b}+\frac{a-b}{b-c}$，"
        r"基本不等式给 $T=4$；再把 $b=\frac{a+c}2$ 代入余弦定理，"
        r"配合锐角条件定出 $\frac ca$ 的范围。"
    ),
    'solution': (
        r"$\dfrac1{a-b}+\dfrac1{b-c}\ge\dfrac{t}{a-c}\ \Longleftrightarrow\ "
        r"t\le\dfrac{a-c}{a-b}+\dfrac{a-c}{b-c}$．" "\n"
        r"把 $a-c=(a-b)+(b-c)$ 代入：" "\n"
        r"$\dfrac{a-c}{a-b}+\dfrac{a-c}{b-c}=2+\dfrac{b-c}{a-b}+\dfrac{a-b}{b-c}\ge2+2=4$，" "\n"
        r"当且仅当 $a-b=b-c$，即 $b=\dfrac{a+c}2$ 时取等，故 $T=4$．" "\n"
        r"此时 $\cos B=\dfrac{a^{2}+c^{2}-b^{2}}{2ac}=\dfrac{a^{2}+c^{2}-\frac{(a+c)^{2}}4}{2ac}"
        r"=\dfrac{3a^{2}+3c^{2}-2ac}{8ac}$，" "\n"
        r"$T\cos B=4\cos B=\dfrac{3a^{2}+3c^{2}-2ac}{2ac}=\dfrac32\left(\dfrac ac+\dfrac ca\right)-1$．" "\n"
        r"由 $a>b>c$ 且锐角得 $b^{2}+c^{2}>a^{2}$，代入 $b=\dfrac{a+c}2$：" "\n"
        r"$\dfrac{(a+c)^{2}}4+c^{2}>a^{2}\ \Longrightarrow\ 5\left(\dfrac ca\right)^{2}+2\dfrac ca-3>0"
        r"\ \Longrightarrow\ \dfrac35<\dfrac ca<1$．" "\n"
        r"令 $m=\dfrac ca$，$y=m+\dfrac1m$ 在 $\left(\dfrac35,1\right)$ 上单调递减，" "\n"
        r"故 $2<y<\dfrac35+\dfrac53=\dfrac{34}{15}$，于是" "\n"
        r"$T\cos B=\dfrac32y-1\in\left(2,\dfrac32\cdot\dfrac{34}{15}-1\right)=\left(2,\dfrac{12}5\right)$，故选 B．"
    ),
    'review': (
        r"① ⭐⭐ **本批最值钱的一步：$a-c=(a-b)+(b-c)$** —— 拆开后每一项都变成两段之比，"
        r"两项互为倒数，基本不等式一步给 $T=4$ ✓✓✓" "\n"
        r"② ⭐⭐ **「恒成立」要翻译成「$t\le$ 右端的最小值」**，这是分离参数的固定句式 ✓✓" "\n"
        r"③ ⭐⭐ $T=4$ 后 **$b=\frac{a+c}2$ 是取等条件，必须代回** —— "
        r"否则 $\cos B$ 仍含三个变量，无法求范围 ✓✓" "\n"
        r"④ ⚠ **用 $b^2+c^2>a^2$ 而不是 $a^2+c^2>b^2$**：因 $a>b>c$，$B$ 是中间大小的角，"
        r"真正起作用的是「最大角 $A$ 为锐角」⟹ $b^{2}+c^{2}>a^{2}$ ✓" "\n"
        r"⑤ 数值验证：$m\to1^-$ 时 $T\cos B\to\frac32\cdot2-1=2$ ✓；" "\n"
        r"  $m\to\frac35^+$ 时 $T\cos B\to\frac32\cdot\frac{34}{15}-1=\frac{17}5-1=\frac{12}5=2.4$ ✓" "\n"
        r"**⭐⭐ 通法（$\frac1{a-b}+\frac1{b-c}\ge\frac{t}{a-c}$ 型）**：" "\n"
        r"① ⭐⭐ 同乘全长 $a-c$ 并拆成两段之和，化出「互为倒数的两项」；" "\n"
        r"② ⭐⭐ 取条件 $b=\frac{a+c}2$（等差）代入余弦定理，把 $\cos B$ 表成 $\frac ac+\frac ca$；" "\n"
        r"③ ⭐⭐ 由「最大角为锐角」定出比值区间，再按对勾函数单调性得范围 ✓✓✓"
    ),
    'difficulty': 0.72,
    'topics': ['M-T-195'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-195-V2',
}

T195_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知 $\triangle ABC$ 的面积为 $2\sqrt3$，$A=\dfrac\pi3$，"
        r"则 $\dfrac{4\sin C+2\sin B}{\sin C+2\sin B}+\dfrac{\sin B}{\sin C}$ 的最小值为"
    ),
    'opts': [
        ('A', r"$\sqrt6-\dfrac12$"),
        ('B', r"$\sqrt6+\dfrac12$"),
        ('C', r"$\sqrt6-1$"),
        ('D', r"$\sqrt6+1$"),
    ],
    'answer': 'B',
    'analysis': (
        r"分子拆成 $(\sin C+2\sin B)+3\sin C$ 先分离出 $1$，再用正弦定理化边；"
        r"最后把 $1+\frac bc$ 写成 $\frac12+\frac{c+2b}{2c}$，凑出互为倒数的两项。"
    ),
    'solution': (
        r"由 $S=\dfrac12 bc\sin A=2\sqrt3$，$A=\dfrac\pi3$ 得 $\dfrac12 bc\cdot\dfrac{\sqrt3}2=2\sqrt3$，即 $bc=8$．" "\n"
        r"$\dfrac{4\sin C+2\sin B}{\sin C+2\sin B}=1+\dfrac{3\sin C}{\sin C+2\sin B}$，" "\n"
        r"又由正弦定理 $\dfrac{\sin B}{\sin C}=\dfrac bc$、$\dfrac{\sin C}{\sin C+2\sin B}=\dfrac{c}{c+2b}$，" "\n"
        r"故原式 $=1+\dfrac{3c}{c+2b}+\dfrac bc=\dfrac12+\dfrac{3c}{c+2b}+\dfrac{c+2b}{2c}$" "\n"
        r"（用到 $1+\dfrac bc=\dfrac12+\dfrac{c+2b}{2c}$）．" "\n"
        r"由基本不等式 $\dfrac{3c}{c+2b}+\dfrac{c+2b}{2c}\ge2\sqrt{\dfrac{3c}{c+2b}\cdot\dfrac{c+2b}{2c}}"
        r"=2\sqrt{\dfrac32}=\sqrt6$，" "\n"
        r"故原式 $\ge\dfrac12+\sqrt6$，当且仅当 $\dfrac{3c}{c+2b}=\dfrac{c+2b}{2c}$，"
        r"即 $(c+2b)^{2}=6c^{2}$ 时取等，故选 B．"
    ),
    'review': (
        r"① ⚠ **题干分式在提取中丢了分数线**：ref_bank 存成 "
        r"`4sinC + 2sinB sinC + 2sinB + sinB sinC`，已按 PDF p157 第 18 题原文还原为" "\n"
        r"  $\frac{4\sin C+2\sin B}{\sin C+2\sin B}+\frac{\sin B}{\sin C}$ ✓（详解中的 "
        r"$1+\frac{3\sin C}{\sin C+2\sin B}$ 也印证了这一还原）" "\n"
        r"② ⭐⭐ **分子拆出「分母 + 余项」是分离常数的标准写法**："
        r"$4\sin C+2\sin B=(\sin C+2\sin B)+3\sin C$ ⟹ 先得 $1$ ✓✓" "\n"
        r"③ ⭐⭐ **最后一步的变形最见功力**：把 $1+\frac bc$ 写成 $\frac12+\frac{c+2b}{2c}$，"
        r"目的就是让第二项与 $\frac{3c}{c+2b}$ 互为倒数的倍数，好凑基本不等式 ✓✓✓" "\n"
        r"④ 取等检验：$(c+2b)^2=6c^2$ 且 $bc=8$ ⟹ $b=\frac{\sqrt6-1}2c$ ⟹ "
        r"$b^{2}=\frac{\sqrt6-1}2\cdot8\cdot\frac{?}{}$…直接解：$b^2=4\sqrt6-4=5.798$，$b=2.408$、" "\n"
        r"  $c=3.322$，代回 $\frac{3c}{c+2b}=\frac{9.966}{8.138}=1.2247$、"
        r"$\frac{c+2b}{2c}=\frac{8.138}{6.644}=1.2247$ ✓ 相等，取等确凿 ✓✓" "\n"
        r"**⭐⭐ 通法（三角分式的最值）**：" "\n"
        r"① ⭐⭐ 先**分离常数**（分子拆成分母 + 余项），把假分式化真分式；" "\n"
        r"② ⭐⭐ 正弦定理把角化边，出现 $\frac{bc}$ 型时看能否用已知面积定积；" "\n"
        r"③ ⭐⭐ 凑**互为倒数的两项**用基本不等式，注意常数项要一起分配 ✓✓✓"
    ),
    'difficulty': 0.7,
    'topics': ['M-T-195'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-195-V3',
}

T197_E1 = {
    'type': '选择',
    'stem_text': (
        r"在锐角 $\triangle ABC$ 中，角 $A,B,C$ 的对边分别为 $a,b,c$，"
        r"$S$ 为 $\triangle ABC$ 的面积，且 $2S=a^{2}-(b-c)^{2}$，"
        r"则 $\dfrac{2b^{2}+c^{2}}{bc}$ 的取值范围为"
    ),
    'opts': [
        ('A', r"$\left[\dfrac{43}{15},\dfrac{59}{15}\right)$"),
        ('B', r"$\left(2\sqrt2,\dfrac{43}{15}\right]$"),
        ('C', r"$\left[2\sqrt2,\dfrac{59}{15}\right)$"),
        ('D', r"$[2\sqrt2,+\infty)$"),
    ],
    'answer': 'C',
    'analysis': (
        r"由 $2S=a^2-(b-c)^2$ 得 $\sin A=2(1-\cos A)$，解出 $\cos A=\frac35$；"
        r"再把 $\frac bc$ 表成 $\frac45\cot C+\frac35$，用锐角条件定 $C$ 的范围，"
        r"最后对 $2t+\frac1t$ 求值域。"
    ),
    'solution': (
        r"由余弦定理 $a^{2}=b^{2}+c^{2}-2bc\cos A$，且 $S=\dfrac12 bc\sin A$，" "\n"
        r"$a^{2}-(b-c)^{2}=(b^{2}+c^{2}-2bc\cos A)-(b^{2}-2bc+c^{2})=2bc(1-\cos A)$，" "\n"
        r"故 $bc\sin A=2bc(1-\cos A)$，即 $\sin A=2(1-\cos A)$．" "\n"
        r"平方得 $1-\cos^{2}A=4-8\cos A+4\cos^{2}A$，即 $5\cos^{2}A-8\cos A+3=0$，" "\n"
        r"$(5\cos A-3)(\cos A-1)=0$，$\cos A=1$ 舍去，故 $\cos A=\dfrac35$，$\sin A=\dfrac45$．" "\n"
        r"$\dfrac bc=\dfrac{\sin B}{\sin C}=\dfrac{\sin(A+C)}{\sin C}"
        r"=\dfrac{\sin A\cos C+\cos A\sin C}{\sin C}=\dfrac45\cot C+\dfrac35$．" "\n"
        r"锐角三角形：$0<C<\dfrac\pi2$ 且 $B=\pi-A-C<\dfrac\pi2$ ⟹ $C>\dfrac\pi2-A$，" "\n"
        r"故 $\cot C<\cot\left(\dfrac\pi2-A\right)=\tan A=\dfrac43$，又 $\cot C>0$，即 $\cot C\in\left(0,\dfrac43\right)$．" "\n"
        r"于是 $t=\dfrac bc\in\left(\dfrac35,\dfrac45\cdot\dfrac43+\dfrac35\right)"
        r"=\left(\dfrac35,\dfrac53\right)$．" "\n"
        r"$\dfrac{2b^{2}+c^{2}}{bc}=2t+\dfrac1t$，在 $t=\dfrac1{\sqrt2}$ 处取最小值 $2\sqrt2$" "\n"
        r"（$\dfrac1{\sqrt2}=0.707\in\left(0.6,1.667\right)$，可取）；" "\n"
        r"$t=\dfrac35$ 时为 $\dfrac65+\dfrac53=\dfrac{43}{15}$；$t=\dfrac53$ 时为 $\dfrac{10}3+\dfrac35=\dfrac{59}{15}$．" "\n"
        r"故取值范围为 $\left[2\sqrt2,\dfrac{59}{15}\right)$，选 C．"
    ),
    'review': (
        r"① ⭐⭐ **$2S=a^{2}-(b-c)^{2}$ 是本批核心条件**：$a^2-(b-c)^2=2bc(1-\cos A)$，"
        r"与 $\frac12 bc\sin A$ 约去 $bc$ 后直接得 $\sin A=2(1-\cos A)$ ⟹ 确定的角 ✓✓✓" "\n"
        r"② ⚠ **原书详解写 $\frac bc=\frac45\tan C+\frac35$ 是 OCR 错误**，实为 $\frac45\cot C+\frac35$：" "\n"
        r"  按 $\tan C$ 则 $C$ 越大 $\frac bc$ 越大，而详解随后用 $\frac1{\tan C}\in(0,\frac43)$ 得 "
        r"$\frac bc\in(\frac35,\frac53)$ —— 只有 $\cot$ 才自洽 ✓✓" "\n"
        r"③ ⭐⭐ **$\frac{\sin(A+C)}{\sin C}=\sin A\cot C+\cos A$** 是固定展开，"
        r"凡「两角之和的正弦 ÷ 其中一个的正弦」都这么拆 ✓✓" "\n"
        r"④ ⚠ **最小值 $2\sqrt2$ 是闭的**：$t=\frac1{\sqrt2}$ 落在 $(0.6,1.667)$ 内，"
        r"对应 $C=\arctan\sqrt2$ 时的锐角三角形确实存在 ✓" "\n"
        r"⑤ 数值验证：$t=\frac1{\sqrt2}$ 时 $2t+\frac1t=1.4142+1.4142=2.8284=2\sqrt2$ ✓；" "\n"
        r"  $t=\frac53$ 时 $3.3333+0.6=3.9333=\frac{59}{15}$ ✓；$t=\frac35$ 时 $1.2+1.6667=\frac{43}{15}$ ✓" "\n"
        r"**⭐⭐ 通法（$2S=a^2-(b-c)^2$ 型）**：" "\n"
        r"① ⭐⭐ 平方差展开后与 $\frac12 bc\sin A$ 约去 $bc$，得 $\sin A=k(1-\cos A)$ 型；" "\n"
        r"② ⭐⭐ 平方 + $\sin^2+\cos^2=1$ 解二次方程，必舍 $\cos A=1$；" "\n"
        r"③ ⭐⭐ 用 $\frac bc=\sin A\cot C+\cos A$ 把边比表成单角函数，再用锐角条件截区间 ✓✓✓"
    ),
    'difficulty': 0.72,
    'topics': ['M-T-197'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-197-E1',
}

T197_V1 = {
    'type': '选择',
    'stem_text': (
        r"设锐角 $\triangle ABC$ 的三个内角 $A,B,C$ 的对边分别为 $a,b,c$，"
        r"且 $c=1$，$A=2C$，则 $\triangle ABC$ 周长的取值范围为"
    ),
    'opts': [
        ('A', r"$(0,2+\sqrt2]$"),
        ('B', r"$(0,3+\sqrt3]$"),
        ('C', r"$(2+\sqrt2,3+\sqrt3)$"),
        ('D', r"$[2+\sqrt2,3+\sqrt3]$"),
    ],
    'answer': 'C',
    'analysis': (
        r"锐角条件给出 $\frac\pi6<C<\frac\pi4$；由正弦定理把 $a,b$ 都表成 $\cos C$ 的函数"
        r"（用到 $\sin 2C=2\sin C\cos C$、$\sin 3C=\sin C(4\cos^2C-1)$），周长即二次函数。"
    ),
    'solution': (
        r"锐角三角形且 $A=2C$：" "\n"
        r"$0<A=2C<\dfrac\pi2$，$0<B=\pi-3C<\dfrac\pi2$，$0<C<\dfrac\pi2$，" "\n"
        r"即 $0<C<\dfrac\pi4$、$\dfrac\pi6<C<\dfrac\pi3$、$0<C<\dfrac\pi2$，取交集得 $\dfrac\pi6<C<\dfrac\pi4$．" "\n"
        r"故 $\cos C\in\left(\dfrac{\sqrt2}2,\dfrac{\sqrt3}2\right)$．" "\n"
        r"由正弦定理 $\dfrac a{\sin A}=\dfrac c{\sin C}$ 且 $c=1$：" "\n"
        r"$a=\dfrac{\sin2C}{\sin C}=2\cos C$；" "\n"
        r"$b=\dfrac{\sin B}{\sin C}=\dfrac{\sin3C}{\sin C}=\dfrac{\sin C\cos2C+\cos C\sin2C}{\sin C}"
        r"=4\cos^{2}C-1$．" "\n"
        r"周长 $L=a+b+c=2\cos C+4\cos^{2}C-1+1=4t^{2}+2t$（$t=\cos C$）．" "\n"
        r"$y=4t^{2}+2t$ 在 $\left(\dfrac{\sqrt2}2,\dfrac{\sqrt3}2\right)$ 上单调递增，" "\n"
        r"$t=\dfrac{\sqrt2}2$ 时 $L=2+\sqrt2$；$t=\dfrac{\sqrt3}2$ 时 $L=3+\sqrt3$．" "\n"
        r"区间端点取不到，故 $L\in(2+\sqrt2,3+\sqrt3)$，选 C．"
    ),
    'review': (
        r"① ⭐⭐ **锐角条件要三个角都列**：$A=2C<\frac\pi2$ 给 $C<\frac\pi4$，"
        r"$B=\pi-3C<\frac\pi2$ 给 $C>\frac\pi6$ —— 两个条件缺一不可 ✓✓✓" "\n"
        r"② ⭐⭐ **$a=2\cos C$ 来自 $\frac{\sin2C}{\sin C}=2\cos C$**，"
        r"这类「角的倍数关系」几乎总是用倍角公式把正弦约掉 ✓✓" "\n"
        r"③ ⭐⭐ **$\frac{\sin3C}{\sin C}=4\cos^{2}C-1$** 建议直接记（由 $\sin3C=3\sin C-4\sin^3C$ "
        r"或和角展开都得此式），比现场展开快 ✓✓" "\n"
        r"④ ⚠ **开区间**：$C=\frac\pi6$ 时 $B=\frac\pi2$（直角，非锐角），"
        r"$C=\frac\pi4$ 时 $A=\frac\pi2$，两端都不能取 ✓" "\n"
        r"⑤ 数值验证：$C=40^\circ$（在范围内）时 $\cos C=0.766$，$L=4(0.5868)+2(0.766)=3.879$，" "\n"
        r"  落在 $(3.414,4.732)$ 内 ✓" "\n"
        r"**⭐⭐ 通法（角成倍数关系的周长/面积范围）**：" "\n"
        r"① ⭐⭐ 先把锐角（钝角）条件翻译成**第三角的区间**；" "\n"
        r"② ⭐⭐ 正弦定理把各边表成该角的三角函数，倍角/三倍角公式约分；" "\n"
        r"③ ⭐⭐ 周长化为关于 $\cos C$（或 $\sin C$）的二次函数，按单调性算端点 ✓✓✓"
    ),
    'difficulty': 0.65,
    'topics': ['M-T-197'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-197-V1',
}

T197_V2 = {
    'type': '填空',
    'stem_text': (
        r"在 $\triangle ABC$ 中，角 $A,B,C$ 的对边分别为 $a,b,c$，"
        r"且 $(a-b)\sin B=a(\sin A+2\sin B)-c\sin C$，"
        r"$\triangle ABC$ 的外接圆半径为 $2$，若 $a+tb$ 有最大值，"
        r"则实数 $t$ 的取值范围是 ____"
    ),
    'opts': [],
    'answer': r"$\left(\dfrac12,2\right)$",
    'analysis': (
        r"正弦定理把条件化成边，整理出 $c^{2}=a^{2}+ab+b^{2}$ 从而 $C=\frac{2\pi}3$；"
        r"再把 $a+tb$ 用 $B$ 表示成 $R\sin(B+\theta)$，有最大值 ⟺ $B+\theta=\frac\pi2$ 有解。"
    ),
    'solution': (
        r"由正弦定理 $\sin A=\dfrac a{2R}$、$\sin B=\dfrac b{2R}$、$\sin C=\dfrac c{2R}$ 代入：" "\n"
        r"$(a-b)\cdot\dfrac b{2R}=a\left(\dfrac a{2R}+2\cdot\dfrac b{2R}\right)-c\cdot\dfrac c{2R}$，" "\n"
        r"即 $(a-b)b=a(a+2b)-c^{2}$，整理得 $c^{2}=a^{2}+ab+b^{2}$．" "\n"
        r"故 $\cos C=\dfrac{a^{2}+b^{2}-c^{2}}{2ab}=\dfrac{-ab}{2ab}=-\dfrac12$，$C=\dfrac{2\pi}3$．" "\n"
        r"由 $R=2$ 得 $\dfrac a{\sin A}=\dfrac b{\sin B}=4$，且 $A=\dfrac\pi3-B$，$B\in\left(0,\dfrac\pi3\right)$．" "\n"
        r"$a+tb=4\sin A+4t\sin B=4\sin\left(\dfrac\pi3-B\right)+4t\sin B$" "\n"
        r"$=(4t-2)\sin B+2\sqrt3\cos B=\sqrt{(4t-2)^{2}+12}\;\sin(B+\theta)$，" "\n"
        r"其中 $\tan\theta=\dfrac{2\sqrt3}{4t-2}=\dfrac{\sqrt3}{2t-1}$．" "\n"
        r"$a+tb$ 有最大值 ⟺ $B+\theta=\dfrac\pi2$ 在 $B\in\left(0,\dfrac\pi3\right)$ 内有解，" "\n"
        r"即 $\theta\in\left(\dfrac\pi6,\dfrac\pi2\right)$，故 $\tan\theta>\dfrac{\sqrt3}3$ 且 $2t-1>0$：" "\n"
        r"$\dfrac{\sqrt3}{2t-1}>\dfrac{\sqrt3}{3}\ \Longrightarrow\ 2t-1<3\ \Longrightarrow\ t<2$，" "\n"
        r"结合 $t>\dfrac12$ 得 $t\in\left(\dfrac12,2\right)$．"
    ),
    'review': (
        r"① ⚠ **题干在 ref_bank 中被误存成分式**（`a - b / sinB = ...`），"
        r"已按 PDF p158 右栏第 22 题原文还原为乘法 " "\n"
        r"  $(a-b)\sin B=a(\sin A+2\sin B)-c\sin C$ ✓" "\n"
        r"  **判据**：按乘法代入正弦定理恰得详解的 $(a-b)b=a(a+2b)-c^2$ ✓✓" "\n"
        r"② ⭐⭐ **「正弦的线性等式」用正弦定理整体乘 $2R$ 就变成边的等式** —— "
        r"这是边角互化的通用入口，不必逐个代换 ✓✓✓" "\n"
        r"③ ⭐⭐ **整理出 $c^2=a^2+ab+b^2$ 立刻认出 $\cos C=-\frac12$**："
        r"凡出现「完全平方 + 交叉项」的余弦定理结果，都要检查是否是特殊角 ✓✓" "\n"
        r"④ ⭐⭐ **「$a+tb$ 有最大值」的翻译**：$\sin(B+\theta)$ 在 $B\in(0,\frac\pi3)$ 上"
        r"要能取到 $1$，即 $\frac\pi2$ 落在 $(B+\theta)$ 的取值区间内 ✓✓✓" "\n"
        r"⑤ ⚠ **$2t-1>0$ 不能漏**：$2t-1\le0$ 时 $\theta$ 不是锐角，"
        r"$B+\theta=\frac\pi2$ 无解（此时 $a+tb$ 单调，最大值在端点取到但不可取）✓" "\n"
        r"⑥ 数值验证：$t=1$ 时 $a+b=4(\sin A+\sin B)$，$\tan\theta=\sqrt3$，$\theta=\frac\pi3$，"
        r"  $B=\frac\pi6$ 时取最大，$\frac\pi6\in(0,\frac\pi3)$ ✓；" "\n"
        r"  $t=2$ 时 $\tan\theta=\frac{\sqrt3}3$，$\theta=\frac\pi6$，需 $B=\frac\pi3$，但 $B<\frac\pi3$，"
        r"  取不到 ✓ 故右端开 ✓✓" "\n"
        r"**⭐⭐ 通法（$a+tb$ 型线性组合的最值存在性）**：" "\n"
        r"① ⭐⭐ 正弦定理统一成 $2R(\sin A+t\sin B)$，再用 $A+B$ 已知消元；" "\n"
        r"② ⭐⭐ 辅助角合并成 $\sqrt{\cdot}\sin(B+\theta)$，$\tan\theta=\frac{\text{cos 系数}}{\text{sin 系数}}$；" "\n"
        r"③ ⭐⭐ 「有最大值」⟺ $\frac\pi2$ 落在 $B+\theta$ 的区间内，由此列 $\theta$ 的不等式 ✓✓✓"
    ),
    'difficulty': 0.75,
    'topics': ['M-T-197'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-197-V2',
}

T197_V3 = {
    'type': '填空',
    'stem_text': (
        r"已知 $\triangle ABC$ 的内角 $A,B,C$ 的对边分别为 $a,b,c$．角 $B$ 为钝角．"
        r"设 $\triangle ABC$ 的面积为 $S$，若 $4bS=a(b^{2}+c^{2}-a^{2})$，"
        r"则 $\sin A+\sin C$ 的最大值是 ____"
    ),
    'opts': [],
    'answer': r"$\dfrac98$",
    'analysis': (
        r"代入 $S=\frac12 ac\sin B$ 后得 $\sin B=\cos A=\sin(\frac\pi2-A)$，"
        r"由 $B$ 钝角、$A$ 锐角得 $B=\frac\pi2+A$；于是 $\sin B=\cos A$、$\cos B=-\sin A$，"
        r"把 $\sin A+\sin C$ 全部化成 $\cos B$ 的二次函数。"
    ),
    'solution': (
        r"$S=\dfrac12 ac\sin B$，代入 $4bS=a(b^{2}+c^{2}-a^{2})$：" "\n"
        r"$2abc\sin B=a(b^{2}+c^{2}-a^{2})$，即 $\sin B=\dfrac{b^{2}+c^{2}-a^{2}}{2bc}=\cos A=\sin\left(\dfrac\pi2-A\right)$．" "\n"
        r"$B$ 为钝角、$A$ 为锐角，故 $\dfrac\pi2-A$ 为锐角，与钝角 $B$ 互补：" "\n"
        r"$B+\left(\dfrac\pi2-A\right)=\pi\ \Longrightarrow\ B=\dfrac\pi2+A$．" "\n"
        r"于是 $\sin B=\sin\left(\dfrac\pi2+A\right)=\cos A$，$\cos B=\cos\left(\dfrac\pi2+A\right)=-\sin A$．" "\n"
        r"$\sin A+\sin C=\sin A+\sin(A+B)=\sin A(1+\cos B)+\cos A\sin B$" "\n"
        r"$=-\cos B(1+\cos B)+\sin^{2}B=-\cos B-\cos^{2}B+1-\cos^{2}B=1-\cos B-2\cos^{2}B$" "\n"
        r"$=-2\left(\cos B+\dfrac14\right)^{2}+\dfrac98\le\dfrac98$．" "\n"
        r"当 $\cos B=-\dfrac14$（$B$ 为钝角，合理）时取等号，故最大值为 $\dfrac98$．"
    ),
    'review': (
        r"① ⭐⭐ **题眼：把 $b^2+c^2-a^2$ 认成 $2bc\cos A$** —— "
        r"面积公式含 $ac\sin B$、右端含 $2bc\cos A$，约去 $bc$ 后就是 $\sin B=\cos A$ ✓✓✓" "\n"
        r"② ⭐⭐ **$\sin B=\cos A=\sin(\frac\pi2-A)$ 且 $B$ 钝角 ⟹ 两角互补**："
        r"这是「正弦相等」的标准处理，必须靠钝角/锐角排除同角情形 ✓✓" "\n"
        r"③ ⭐⭐ **$\sin A+\sin C=\sin A+\sin(A+B)$ 展开后，把 $\sin A=-\cos B$、"
        r"$\cos A=\sin B$ 代入** —— 一切都变成 $\cos B$ 的一元函数，这是全题的枢纽 ✓✓✓" "\n"
        r"④ 取等检验：$\cos B=-\frac14$ 时 $\sin B=\frac{\sqrt{15}}4$，"
        r"$\sin A=-\cos B=\frac14$、$\cos A=\sin B=\frac{\sqrt{15}}4$；" "\n"
        r"  $\sin A(1+\cos B)+\cos A\sin B=\frac14\cdot\frac34+\frac{\sqrt{15}}4\cdot\frac{\sqrt{15}}4"
        r"=\frac3{16}+\frac{15}{16}=\frac{18}{16}=\frac98$ ✓✓ 完全闭合" "\n"
        r"⑤ ⚠ 最大值不是 $1$：$\sin A+\sin C$ 可达 $\frac98>1$，"
        r"因为 $A+C<\frac\pi2$（$B$ 钝角）时两正弦之和仍可超过 $1$ ✓" "\n"
        r"**⭐⭐ 通法（含面积与余弦定理结构的最值）**：" "\n"
        r"① ⭐⭐ 见 $b^2+c^2-a^2$ 立刻替换为 $2bc\cos A$，见面积立刻写 $\frac12 ac\sin B$；" "\n"
        r"② ⭐⭐ 由「正弦 = 余弦」得两角互余，再由钝/锐角定出互补关系；" "\n"
        r"③ ⭐⭐ 用 $C=\pi-A-B$ 消去 $C$，全部化成一个角的二次函数后配方 ✓✓✓"
    ),
    'difficulty': 0.75,
    'topics': ['M-T-197'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-197-V3',
}

T123_E1 = {
    'type': '选择',
    'stem_text': (
        r"定义在 $\mathbb R$ 上的连续函数 $f(x)$ 的导函数为 $f^{\prime}(x)$，"
        r"且 $\cos x\,f^{\prime}(x)<(\cos x+\sin x)f(x)$ 成立，则下列各式一定成立的是"
    ),
    'opts': [
        ('A', r"$f(0)=0$"),
        ('B', r"$f(0)<0$"),
        ('C', r"$f(\pi)>0$"),
        ('D', r"$f\left(\dfrac\pi2\right)=0$"),
    ],
    'answer': 'C',
    'analysis': (
        r"把不等式看成 $(\cos x f(x))'$ 与 $\cos xf(x)$ 的比较，"
        r"构造 $g(x)=\frac{\cos x f(x)}{\mathrm e^x}$ 判定单调性，再用 $g(\frac\pi2)=0$ 比较三点。"
    ),
    'solution': (
        r"由题设 $\cos xf^{\prime}(x)-\sin xf(x)<\cos xf(x)$，即" "\n"
        r"$(\cos x\,f(x))^{\prime}<\cos x\,f(x)$．" "\n"
        r"设 $g(x)=\dfrac{\cos x\cdot f(x)}{\mathrm e^{x}}$，则" "\n"
        r"$g^{\prime}(x)=\dfrac{(\cos xf(x))^{\prime}-\cos xf(x)}{\mathrm e^{x}}<0$，" "\n"
        r"故 $g(x)$ 在 $\mathbb R$ 上单调递减，且 $g\left(\dfrac\pi2\right)=\dfrac{0\cdot f(\frac\pi2)}{\mathrm e^{\pi/2}}=0$．" "\n"
        r"由 $g(0)>g\left(\dfrac\pi2\right)>g(\pi)$：" "\n"
        r"$g(0)=f(0)>0$，故 A、B 均错；" "\n"
        r"$g(\pi)=\dfrac{-f(\pi)}{\mathrm e^{\pi}}<0\ \Longrightarrow\ f(\pi)>0$，故 C 正确．" "\n"
        r"把 $x=\dfrac\pi2$ 代入原不等式：$0<(0+1)\cdot f\left(\dfrac\pi2\right)$，" "\n"
        r"即 $f\left(\dfrac\pi2\right)>0$，故 D 错．选 C．"
    ),
    'review': (
        r"① ⭐⭐ **构造的线索就在不等式里**：左端 $\cos xf'(x)-\sin xf(x)$ 恰是 $(\cos xf(x))'$，" "\n"
        r"  见到「$\cos x f'(x)$ 与 $\sin x f(x)$ 同现」就要想到乘积求导 ✓✓✓" "\n"
        r"② ⭐⭐ **除以 $\mathrm e^x$ 是标准动作**：$F'<F$ ⟹ $\left(\frac F{\mathrm e^x}\right)'<0$。"
        r"同型还有 $F'<kF$ ⟹ $\frac F{\mathrm e^{kx}}$ 递减 ✓✓" "\n"
        r"③ ⭐⭐ **$g(\frac\pi2)=0$ 是比较三点的支点**：因为 $\cos\frac\pi2=0$，"
        r"$g$ 在此处的值与 $f$ 无关，等于 $0$ —— 这是本题能出结论的关键 ✓✓✓" "\n"
        r"④ ⚠ **D 选项要单独代入原式检验**，不能由单调性推出（单调性只比较 $g$，不给 $f$ 的零点）✓" "\n"
        r"⑤ 符号检查：$g(\pi)=\frac{\cos\pi f(\pi)}{e^\pi}=\frac{-f(\pi)}{e^\pi}<0$ ⟹ $f(\pi)>0$，"
        r"  $\mathrm e^\pi>0$ 不变号 ✓" "\n"
        r"**⭐⭐ 通法（$u(x)f'(x)+v(x)f(x)$ 型不等式）**：" "\n"
        r"① ⭐⭐ 先识别出 $(\text{某函数}\cdot f)'$ 的结构，关键是 $v=u'$ 或差一个倍数；" "\n"
        r"② ⭐⭐ 凑成 $F'<kF$ 后除以 $\mathrm e^{kx}$ 判单调；" "\n"
        r"③ ⭐⭐ 找一个使「某函数」为 $0$ 的特殊点作为比较基准 ✓✓✓"
    ),
    'difficulty': 0.7,
    'topics': ['M-T-123'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-123-E1',
}

T123_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知函数 $f(x)$ 的导函数为 $f^{\prime}(x)$，对任意的实数 $x$ 都有" "\n"
        r"$f^{\prime}(x)=f(x)-2\mathrm e^{-x}+2x-x^{2}$，$f(0)=2$，"
        r"则不等式 $f(x-1)<\mathrm e^{2}+\mathrm e^{-2}+4$ 的解集是"
    ),
    'opts': [
        ('A', r"$(0,1)$"),
        ('B', r"$(-1,1)$"),
        ('C', r"$(-1,3)$"),
        ('D', r"$(\mathrm e,3)$"),
    ],
    'answer': 'C',
    'analysis': (
        r"把等式改写成 $\left(\frac{f(x)-x^2}{\mathrm e^x}\right)'=-2\mathrm e^{-2x}$，"
        r"积分求出 $f(x)$，再用偶函数 + 单调性把不等式化为 $|x-1|<2$。"
    ),
    'solution': (
        r"由 $f^{\prime}(x)=f(x)-2\mathrm e^{-x}+2x-x^{2}$ 得" "\n"
        r"$\dfrac{[f^{\prime}(x)-2x]\mathrm e^{x}-[f(x)-x^{2}]\mathrm e^{x}}{(\mathrm e^{x})^{2}}=-2\mathrm e^{-2x}$，" "\n"
        r"即 $\left(\dfrac{f(x)-x^{2}}{\mathrm e^{x}}\right)^{\prime}=-2\mathrm e^{-2x}$，" "\n"
        r"积分得 $\dfrac{f(x)-x^{2}}{\mathrm e^{x}}=\mathrm e^{-2x}+c$，即 $f(x)=\mathrm e^{-x}+c\,\mathrm e^{x}+x^{2}$．" "\n"
        r"由 $f(0)=2$ 得 $1+c=2$，$c=1$，故 $f(x)=\mathrm e^{-x}+\mathrm e^{x}+x^{2}$，显然是偶函数．" "\n"
        r"当 $x\ge0$ 时 $f^{\prime}(x)=-\mathrm e^{-x}+\mathrm e^{x}+2x=\mathrm e^{-x}(\mathrm e^{2x}-1)+2x>0$，" "\n"
        r"故 $f$ 在 $[0,+\infty)$ 上递增．又 $f(2)=\mathrm e^{2}+\mathrm e^{-2}+4$，于是" "\n"
        r"$f(x-1)<\mathrm e^{2}+\mathrm e^{-2}+4\iff f(|x-1|)<f(2)\iff|x-1|<2\iff-1<x<3$．选 C．"
    ),
    'review': (
        r"① ⭐⭐ **题眼是识别出商的导数**：等式右端含 $f(x)-2\mathrm e^{-x}+2x-x^2$，"
        r"把 $2x-x^2$ 移到左边得 $f'(x)-2x=f(x)-x^2$，立刻看出" "\n"
        r"  $\left(\frac{f(x)-x^2}{\mathrm e^x}\right)'=\frac{f'(x)-2x-(f(x)-x^2)}{\mathrm e^x}=-2\mathrm e^{-2x}$ ✓✓✓" "\n"
        r"② ⭐⭐ **「$f'-g'=f-g$」型一律配 $\mathrm e^{-x}$**：这是解微分方程 $y'-y=h(x)$ 的固定乘法因子 ✓✓" "\n"
        r"③ ⭐⭐ **偶性是白送的**：$f(x)=\mathrm e^{-x}+\mathrm e^{x}+x^2$ 三项都偶，"
        r"所以 $f(x-1)=f(|x-1|)$，把「平移后的值」换成「距离的值」 ✓✓" "\n"
        r"④ ⚠ **必须验证 $\mathrm e^{2}+\mathrm e^{-2}+4=f(2)$** 而不是别的点："
        r"$f(2)=\mathrm e^{-2}+\mathrm e^{2}+4$ ✓ 完全对应，这一步对上才能用单调性 ✓" "\n"
        r"⑤ 选项 D 的 $(\mathrm e,3)$ 是原书印刷（PDF p87 第 32 题原文即如此），"
        r"  疑为 $(0,3)$ 之误，作为干扰项保留原文 ✓" "\n"
        r"**⭐⭐ 通法（由 $f'$ 与 $f$ 的关系式求 $f$）**：" "\n"
        r"① ⭐⭐ 移项凑成 $F'-F=h(x)$ 或 $F'-kF=h(x)$，乘 $\mathrm e^{-kx}$；" "\n"
        r"② ⭐⭐ 积分后由初值定常数 $c$；" "\n"
        r"③ ⭐⭐ 求出的 $f$ 通常带奇偶性，用它把 $f(x-a)$ 化成 $f(|x-a|)$ 再用单调性 ✓✓✓"
    ),
    'difficulty': 0.7,
    'topics': ['M-T-123'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-123-V1',
}

T123_V2 = {
    'type': '选择',
    'stem_text': (
        r"定义在 $\mathbb R$ 上的函数 $f(x)$ 的导函数为 $f^{\prime}(x)$，"
        r"当 $x\in[0,+\infty)$ 时，$2\sin x\cos x-f^{\prime}(x)>0$ "
        r"且 $\forall x\in\mathbb R$，$f(-x)+f(x)+\cos 2x=1$．"
        r"则下列说法一定正确的是"
    ),
    'opts': [
        ('A', r"$\dfrac14-f\left(-\dfrac{5\pi}6\right)>\dfrac34-f\left(-\dfrac{2\pi}3\right)$"),
        ('B', r"$\dfrac14-f\left(-\dfrac{5\pi}6\right)>\dfrac34-f\left(-\dfrac{4\pi}3\right)$"),
        ('C', r"$\dfrac34-f\left(\dfrac\pi3\right)>\dfrac12-f\left(\dfrac{3\pi}4\right)$"),
        ('D', r"$\dfrac12-f\left(-\dfrac{3\pi}4\right)>\dfrac34-f\left(\dfrac\pi3\right)$"),
    ],
    'answer': 'B',
    'analysis': (
        r"条件 $f(-x)+f(x)=1-\cos2x=2\sin^2x$ 提示构造 $F(x)=\sin^2x-f(x)$（奇函数），"
        r"由 $F'=\sin2x-f'>0$ 得 $F$ 递增，再逐项比较。"
    ),
    'solution': (
        r"令 $F(x)=\sin^{2}x-f(x)$．由 $f(-x)+f(x)+\cos2x=1$ 得" "\n"
        r"$f(-x)+f(x)=1-\cos2x=2\sin^{2}x$，于是" "\n"
        r"$F(-x)+F(x)=2\sin^{2}x-[f(-x)+f(x)]=0$，故 $F$ 为 $\mathbb R$ 上的奇函数．" "\n"
        r"$F^{\prime}(x)=2\sin x\cos x-f^{\prime}(x)$，由题设当 $x\ge0$ 时 $F^{\prime}(x)>0$，" "\n"
        r"故 $F$ 在 $[0,+\infty)$ 上递增；由奇函数性质，$F$ 在 $(-\infty,0)$ 上也递增，" "\n"
        r"（且 $F(0)=0$、连续）故 $F$ 在 $\mathbb R$ 上单调递增．" "\n"
        r"A：$-\dfrac{5\pi}6<-\dfrac{2\pi}3$，$F\left(-\dfrac{5\pi}6\right)<F\left(-\dfrac{2\pi}3\right)$，" "\n"
        r"  即 $\dfrac14-f\left(-\dfrac{5\pi}6\right)<\dfrac34-f\left(-\dfrac{2\pi}3\right)$，A 错．" "\n"
        r"B：$-\dfrac{5\pi}6>-\dfrac{4\pi}3$，$F\left(-\dfrac{5\pi}6\right)>F\left(-\dfrac{4\pi}3\right)$，" "\n"
        r"  即 $\dfrac14-f\left(-\dfrac{5\pi}6\right)>\dfrac34-f\left(-\dfrac{4\pi}3\right)$，B 对．" "\n"
        r"C：$\dfrac\pi3<\dfrac{3\pi}4$，$F\left(\dfrac\pi3\right)<F\left(\dfrac{3\pi}4\right)$，"
        r"即 $\dfrac34-f\left(\dfrac\pi3\right)<\dfrac12-f\left(\dfrac{3\pi}4\right)$，C 错．" "\n"
        r"D：$-\dfrac{3\pi}4<\dfrac\pi3$，$F\left(-\dfrac{3\pi}4\right)<F\left(\dfrac\pi3\right)$，"
        r"即 $\dfrac12-f\left(-\dfrac{3\pi}4\right)<\dfrac34-f\left(\dfrac\pi3\right)$，D 错．选 B．"
    ),
    'review': (
        r"① ⭐⭐ **构造 $F(x)=\sin^2x-f(x)$ 的线索来自两个条件**："
        r"导数条件给 $\sin2x-f'$（正好是 $F'$），对称条件给 $f(-x)+f(x)=2\sin^2x$（正好说明 $F$ 奇）✓✓✓" "\n"
        r"② ⭐⭐ **$1-\cos2x=2\sin^2x$ 是必须的变形** —— 它把「余弦」换成「正弦平方」，"
        r"才能与 $\sin^2x$ 对齐造出奇函数 ✓✓" "\n"
        r"③ ⚠ **奇函数 + 在 $[0,+\infty)$ 递增 ⟹ 在 $\mathbb R$ 上递增**，"
        r"这一步要用 $F(0)=0$ 和连续性说明（否则只说明两段各自递增）✓" "\n"
        r"④ ⭐⭐ **逐项比较只需算 $\sin^2$ 的值**："
        r"$\sin^2\frac{5\pi}6=\frac14$、$\sin^2\frac{2\pi}3=\sin^2\frac{4\pi}3=\frac34$、"
        r"$\sin^2\frac\pi3=\frac34$、$\sin^2\frac{3\pi}4=\sin^2(-\frac{3\pi}4)=\frac12$ ✓" "\n"
        r"  B 与 A 只差一个 $-\frac{2\pi}3$ 与 $-\frac{4\pi}3$，"
        r"而 $-\frac{4\pi}3<-\frac{5\pi}6$ 才使不等号方向正确 —— **这是命题人设的区分点** ✓✓" "\n"
        r"**⭐⭐ 通法（$f(-x)+f(x)=g(x)$ 型对称性）**：" "\n"
        r"① ⭐⭐ 把 $g(x)$ 写成 $2h(x)$，则 $F=h-f$ 满足 $F(-x)=-F(x)$（奇）；" "\n"
        r"② ⭐⭐ 导数条件通常直接给出 $F'$ 的符号；" "\n"
        r"③ ⭐⭐ 造出 $F$ 的奇偶性 + 单调性后，所有选项都是「比较两个点的 $F$ 值」✓✓✓"
    ),
    'difficulty': 0.72,
    'topics': ['M-T-123'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-123-V2',
}

T123_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知函数 $f(x)$ 的定义域为 $\mathbb R$，且 $f(x+2)$ 是偶函数，" "\n"
        r"$f^{\prime}(x)>\dfrac12x-1+\ln(x-1)$（$f^{\prime}(x)$ 为 $f(x)$ 的导函数）．"
        r"若对任意的 $x\in(0,+\infty)$，不等式" "\n"
        r"$f(-t^{2}+2t+1)\ge f\left(\left(\dfrac12\right)^{x}-2\right)$ 恒成立，"
        r"则实数 $t$ 的取值范围是"
    ),
    'opts': [
        ('A', r"$[-2,4]$"),
        ('B', r"$(-\infty,-2]\cup[4,+\infty)$"),
        ('C', r"$[-1,3]$"),
        ('D', r"$(-\infty,-1]\cup[3,+\infty)$"),
    ],
    'answer': 'D',
    'analysis': (
        r"$f(x+2)$ 偶 ⟹ $f$ 关于 $x=2$ 对称；由 $f'(x)>p(x)\ge0$（$x\ge2$）得 $f$ 在 $[2,+\infty)$ 递增；"
        r"再比较两点到对称轴的距离。"
    ),
    'solution': (
        r"由 $f(x+2)$ 为偶函数得 $f(2+x)=f(2-x)$，即 $f$ 的图象关于直线 $x=2$ 对称．" "\n"
        r"设 $p(x)=\dfrac12x-1+\ln(x-1)$（$x>1$），则 $p^{\prime}(x)=\dfrac12+\dfrac1{x-1}>0$，" "\n"
        r"故 $p$ 在 $(1,+\infty)$ 上单调递增，且 $p(2)=\dfrac12\cdot2-1+\ln1=0$，" "\n"
        r"于是当 $x\ge2$ 时 $p(x)\ge0$，由 $f^{\prime}(x)>p(x)\ge0$ 知 $f$ 在 $[2,+\infty)$ 上递增，" "\n"
        r"由对称性，$f$ 在 $(-\infty,2]$ 上递减．" "\n"
        r"设 $g(x)=\left(\dfrac12\right)^{x}-2$，当 $x\in(0,+\infty)$ 时 $g(x)\in(-2,-1)$．" "\n"
        r"又 $-t^{2}+2t+1=-(t-1)^{2}+2\le2$．" "\n"
        r"因 $f$ 在 $(-\infty,2]$ 上递减，且 $g(x)\in(-2,-1)\subset(-\infty,2]$，" "\n"
        r"$f(-t^{2}+2t+1)\ge f(g(x))$ 对一切 $x>0$ 成立" "\n"
        r"$\iff f(-t^{2}+2t+1)\ge\max_{g\in(-2,-1)}f(g)=f(-2)$" "\n"
        r"$\iff -t^{2}+2t+1\le-2\iff t^{2}-2t-3\ge0\iff t\le-1$ 或 $t\ge3$．选 D．"
    ),
    'review': (
        r"① ⚠ **原书详解的 $p'(x)=\frac12-\frac1{x-1}$ 是 OCR 错误**，实为 $\frac12+\frac1{x-1}$：" "\n"
        r"  按减号 $p'(2)=-\frac12<0$，与「$p$ 在 $[2,+\infty)$ 递增」矛盾，"
        r"也与 $p(2)=0$、$p(3)=1.193>0$ 不符 ✓✓ 已按加号录入" "\n"
        r"② ⭐⭐ **$f(x+2)$ 偶 ⟹ $f$ 关于 $x=2$ 对称**，这是「平移型偶性」的固定翻译，"
        r"切忌误读成 $f$ 本身是偶函数 ✓✓✓" "\n"
        r"③ ⭐⭐ **$p(2)=0$ 是刻意设计**：$\frac12\cdot2-1+\ln1=0$ 恰好为零，"
        r"于是 $f'(x)>p(x)\ge0$，单调性立刻得到 ✓✓" "\n"
        r"④ ⭐⭐ **比较对称轴同侧两点，直接用单调性**；比较异侧则用「离轴越远值越大」．"
        r"本题两点都在 $2$ 左侧，故只需递减性 ✓✓" "\n"
        r"⑤ ⚠ **$\max_{g\in(-2,-1)}f(g)=f(-2)$ 是上确界**（开区间），"
        r"故条件是 $f(A)\ge f(-2)$ 而非 $>$，端点 $t=\pm$ 处可取等 ✓" "\n"
        r"⑥ 数值验证：$t=-1$ 时 $-t^2+2t+1=-2$，$f(-2)\ge f(g)$ 对 $g\in(-2,-1)$ 成立 ✓；" "\n"
        r"  $t=1$ 时 $-1+2+1=2$，$f(2)$ 是最小值，$f(2)\ge f(g)$ 不成立 ✓ 故排除 ✓✓" "\n"
        r"**⭐⭐ 通法（对称轴 + 恒成立）**：" "\n"
        r"① ⭐⭐ $f(x+a)$ 偶 ⟹ 对称轴 $x=a$；$f(x+a)$ 奇 ⟹ 对称中心 $(a,0)$；" "\n"
        r"② ⭐⭐ 由 $f'>0$（或 $<0$）确定对称轴两侧的单调方向（必然相反）；" "\n"
        r"③ ⭐⭐ 恒成立问题先求右端的**上确界**，再转成「到对称轴距离」的不等式 ✓✓✓"
    ),
    'difficulty': 0.75,
    'topics': ['M-T-123'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-123-V3',
}

T184_E1 = {
    'type': '填空',
    'stem_text': (
        r"已知非负实数 $x,y$ 满足 $2x^{2}+4xy+2y^{2}+x^{2}y^{2}=9$，"
        r"则 $2\sqrt2(x+y)+xy$ 的最大值为 ____"
    ),
    'opts': [],
    'answer': r"$4\sqrt2+1$",
    'analysis': (
        r"识别 $2(x+y)^2+(xy)^2=9$，令 $x+y=\frac3{\sqrt2}\sin\theta$、$xy=3\cos\theta$；"
        r"再由 $(x+y)^2\ge4xy$ 定出 $\cos\theta$ 的范围，最后辅助角求最值。"
    ),
    'solution': (
        r"条件即 $2(x+y)^{2}+(xy)^{2}=9$．" "\n"
        r"令 $x+y=\dfrac3{\sqrt2}\sin\theta$，$xy=3\cos\theta$（由 $x,y\ge0$ 知 $\sin\theta\ge0,\cos\theta\ge0$）．" "\n"
        r"由 $(x+y)^{2}\ge4xy$ 得 $\dfrac92\sin^{2}\theta\ge12\cos\theta$，" "\n"
        r"即 $1-\cos^{2}\theta\ge\dfrac83\cos\theta$，整理得 $\cos^{2}\theta+\dfrac83\cos\theta-1\le0$，" "\n"
        r"解得 $0\le\cos\theta\le\dfrac13$，于是 $\sin\theta\ge\dfrac{2\sqrt2}3$．" "\n"
        r"$2\sqrt2(x+y)+xy=2\sqrt2\cdot\dfrac3{\sqrt2}\sin\theta+3\cos\theta=6\sin\theta+3\cos\theta$" "\n"
        r"$=3\sqrt5\sin(\theta+\varphi)$，其中 $\cos\varphi=\dfrac2{\sqrt5}$，$\sin\varphi=\dfrac1{\sqrt5}$．" "\n"
        r"由 $\cos\theta\le\dfrac13$ 知 $\sin\left(\dfrac\pi2-\theta\right)\le\dfrac13<\dfrac1{\sqrt5}=\sin\varphi$，" "\n"
        r"故 $\dfrac\pi2-\theta>\varphi$，即 $\theta+\varphi<\dfrac\pi2$；又 $\sin$ 在 $\left[0,\dfrac\pi2\right]$ 上递增，" "\n"
        r"所以 $\theta$ 取最大（即 $\cos\theta=\dfrac13$、$\sin\theta=\dfrac{2\sqrt2}3$）时原式最大：" "\n"
        r"$6\cdot\dfrac{2\sqrt2}3+3\cdot\dfrac13=4\sqrt2+1$．"
    ),
    'review': (
        r"① ⚠ **题干根号在提取中丢失**：ref_bank 存成 `2 2(x + y) + xy`，"
        r"由详解中 $2\sqrt2\cdot\frac3{\sqrt2}\sin\theta=6\sin\theta$ 反推确认为 $2\sqrt2(x+y)$ ✓✓" "\n"
        r"② ⭐⭐ **题眼是 $2x^2+4xy+2y^2=2(x+y)^2$** —— 条件立刻变成 "
        r"$2(x+y)^2+(xy)^2=9$，结构与 $\sin^2+\cos^2=1$ 一致，故用三角换元 ✓✓✓" "\n"
        r"③ ⭐⭐ **换元后必须用 $(x+y)^2\ge4xy$ 追加约束**："
        r"否则 $\theta$ 自由取值会得出虚幻的最大值 $3\sqrt5\approx6.708$（实际 $6.657$）✓✓" "\n"
        r"④ ⭐⭐ **$\theta+\varphi<\frac\pi2$ 的判定是关键**：这保证在允许范围内 $\sin$ 递增，"
        r"最值在 $\theta$ 最大处（而非 $\theta+\varphi=\frac\pi2$ 处）取得 ✓✓✓" "\n"
        r"⑤ 数值验证：$\cos\theta=\frac13$、$\sin\theta=\frac{2\sqrt2}3=0.9428$ 时，"
        r"  $6(0.9428)+3(0.3333)=5.657+1=6.657=4\sqrt2+1$ ✓；" "\n"
        r"  而 $3\sqrt5=6.708>6.657$，证实约束确实起作用 ✓✓" "\n"
        r"**⭐⭐ 通法（$A(x+y)^2+B(xy)^2=k$ 型）**：" "\n"
        r"① ⭐⭐ 凑成 $u^2+v^2=k$ 的形状后令 $u=\sqrt{\frac kA}\sin\theta$、$v=\sqrt{\frac kB}\cos\theta$；" "\n"
        r"② ⭐⭐ 换元后**必须补上 $(x+y)^2\ge4xy$**（或 $x,y\ge0$ 自带的符号约束）；" "\n"
        r"③ ⭐⭐ 辅助角合并后，先判断 $\theta+\varphi$ 是否越过 $\frac\pi2$，再定最值位置 ✓✓✓"
    ),
    'difficulty': 0.72,
    'topics': ['M-T-184'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-184-E1',
}

T184_V1 = {
    'type': '填空',
    'stem_text': (
        r"已知实数 $x,y$ 满足 $4^{x}+9^{y}=1$，则 $2^{x+1}+3^{y+1}$ 的取值范围是 ____"
    ),
    'opts': [],
    'answer': r"$\left(2,\sqrt{13}\right]$",
    'analysis': (
        r"换元 $u=2^x$、$v=3^y$ 把条件变成 $u^2+v^2=1$（$u,v>0$），"
        r"再三角换元成 $2\cos\theta+3\sin\theta$，注意 $\theta$ 是开区间。"
    ),
    'solution': (
        r"设 $u=2^{x}>0$，$v=3^{y}>0$，则 $u^{2}+v^{2}=1$．" "\n"
        r"令 $u=\cos\theta$，$v=\sin\theta$，$\theta\in\left(0,\dfrac\pi2\right)$（因 $u,v>0$，端点取不到）．" "\n"
        r"$2^{x+1}+3^{y+1}=2u+3v=2\cos\theta+3\sin\theta=\sqrt{13}\sin(\theta+\varphi)$，" "\n"
        r"其中 $\tan\varphi=\dfrac23$，$\varphi\in\left(0,\dfrac\pi4\right)$．" "\n"
        r"$\theta\in\left(0,\dfrac\pi2\right)\ \Longrightarrow\ \theta+\varphi\in\left(\varphi,\varphi+\dfrac\pi2\right)$，" "\n"
        r"故 $\sin(\theta+\varphi)\in(\sin\varphi,1]$，而 $\sin\varphi=\dfrac2{\sqrt{13}}$．" "\n"
        r"于是 $2u+3v\in\left(\sqrt{13}\cdot\dfrac2{\sqrt{13}},\sqrt{13}\right]=\left(2,\sqrt{13}\right]$．"
    ),
    'review': (
        r"① ⚠ **题干指数在提取中丢失**：ref_bank 存成 `4x + 9y = 1` 与 `2x+1 + 3y+1`，"
        r"由详解中「设 $2^x=u$、$3^y=v$，则 $u^2+v^2=1$」反推确认为 $4^x+9^y=1$ 与" "\n"
        r"  $2^{x+1}+3^{y+1}$ ✓✓（因为 $4^x=u^2$、$9^y=v^2$，$2^{x+1}=2u$、$3^{y+1}=3v$）" "\n"
        r"② ⭐⭐ **$a^x$ 与 $a^{2x}$ 型同时出现 ⟹ 换元 $u=a^x$**，"
        r"条件立刻变成圆 $u^2+v^2=1$ ✓✓✓" "\n"
        r"③ ⭐⭐ **$u,v>0$ 决定 $\theta\in(0,\frac\pi2)$ 是开区间** —— "
        r"因此下界 $2$ 取不到（上界 $\sqrt{13}$ 在内点取到）✓✓" "\n"
        r"④ ⭐⭐ **端点值就是「$\theta\to0$ 时的极限」**：$\sqrt{13}\sin\varphi=2$，"
        r"即 $u\to1,v\to0$ 时 $2u+3v\to2$ ✓ 用这个办法可快速写下界 ✓✓" "\n"
        r"⑤ 数值验证：$\theta=\arctan\frac32$ 时 $\sin(\theta+\varphi)=1$，$2u+3v=\sqrt{13}=3.606$ ✓；" "\n"
        r"  $\theta\to0$ 时 $u\to1,v\to0$，$2u+3v\to2$ ✓✓" "\n"
        r"**⭐⭐ 通法（指数和为定值求指数线性组合的范围）**：" "\n"
        r"① ⭐⭐ 换元把条件变成圆（或椭圆）$u^2+v^2=1$；" "\n"
        r"② ⭐⭐ 由 $u,v>0$ 定出 $\theta$ 的**开**区间，端点值只能逼近；" "\n"
        r"③ ⭐⭐ 辅助角后按 $\theta+\varphi$ 的区间取 $\sin$ 的范围，注意开闭 ✓✓✓"
    ),
    'difficulty': 0.65,
    'topics': ['M-T-184'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-184-V1',
}

T184_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知实数 $x,y$ 满足 $\dfrac{x^{2}}2+y^{2}\le1$，"
        r"则 $\left|x^{2}+y^{2}-2\right|+\left|x^{2}+y^{2}-6x+7\right|$ 的最小值等于"
    ),
    'opts': [
        ('A', r"$6\sqrt2-5$"),
        ('B', r"$6\sqrt2-7$"),
        ('C', r"$6-\sqrt3$"),
        ('D', r"$9-6\sqrt2$"),
    ],
    'answer': 'D',
    'analysis': (
        r"椭圆内点用 $x=\sqrt2\cos\theta$、$y=\sin\theta$ 参数化；两个绝对值内分别是"
        r"$-\sin^2\theta\le0$ 与恒正的二次式，去绝对值后合并成 $9-6\sqrt2\cos\theta$。"
    ),
    'solution': (
        r"由 $\dfrac{x^{2}}2+y^{2}\le1$，设 $x=\sqrt2\cos\theta$，$y=\sin\theta$．" "\n"
        r"第一项：$x^{2}+y^{2}-2=2\cos^{2}\theta+\sin^{2}\theta-2=\cos^{2}\theta-1=-\sin^{2}\theta\le0$，" "\n"
        r"故 $\left|x^{2}+y^{2}-2\right|=\sin^{2}\theta$．" "\n"
        r"第二项：$x^{2}+y^{2}-6x+7=2\cos^{2}\theta+\sin^{2}\theta-6\sqrt2\cos\theta+7$" "\n"
        r"$=\cos^{2}\theta-6\sqrt2\cos\theta+8=(\cos\theta-3\sqrt2)^{2}-10$．" "\n"
        r"因 $\cos\theta\in[-1,1]$，$\cos\theta-3\sqrt2\in[-1-3\sqrt2,1-3\sqrt2]$，" "\n"
        r"最小平方为 $(1-3\sqrt2)^{2}=19-6\sqrt2\approx10.515>10$，故第二项恒正：" "\n"
        r"$\left|x^{2}+y^{2}-6x+7\right|=\cos^{2}\theta-6\sqrt2\cos\theta+8$．" "\n"
        r"原式 $=\sin^{2}\theta+\cos^{2}\theta-6\sqrt2\cos\theta+8=9-6\sqrt2\cos\theta$，" "\n"
        r"当 $\cos\theta=1$（即 $x=\sqrt2,y=0$）时取最小值 $9-6\sqrt2$．选 D．"
    ),
    'review': (
        r"① ⭐⭐ **椭圆内点参数化：$x=a\cos\theta$、$y=b\sin\theta$** 是处理 "
        r"$\frac{x^2}{a^2}+\frac{y^2}{b^2}\le1$ 上最值的首选 ✓✓✓" "\n"
        r"② ⭐⭐ **第一个绝对值化简极漂亮**：$2\cos^2\theta+\sin^2\theta-2=\cos^2\theta-1=-\sin^2\theta$，"
        r"符号恒为负，去绝对值直接加负号 ✓✓" "\n"
        r"③ ⭐⭐ **第二个绝对值要先证恒正**：配方成 $(\cos\theta-3\sqrt2)^2-10$，"
        r"最小值在 $\cos\theta=1$ 处为 $10.515-10=0.515>0$ ✓ 不能想当然 ✓✓" "\n"
        r"④ ⭐⭐ **两项合并时 $\sin^2+\cos^2=1$ 把角度消掉**，只剩 $-6\sqrt2\cos\theta$ —— "
        r"这是「两个绝对值之和」能求出简洁答案的原因 ✓✓✓" "\n"
        r"⑤ 数值验证：$\cos\theta=1$ 时原式 $=9-6\sqrt2=9-8.485=0.515$；"
        r"  直接代 $x=\sqrt2,y=0$：$|2+0-2|+|2+0-6\sqrt2+7|=0+|9-8.485|=0.515$ ✓✓ 完全吻合" "\n"
        r"**⭐⭐ 通法（椭圆域上含绝对值的二次式最值）**：" "\n"
        r"① ⭐⭐ 参数化 $x=a\cos\theta,y=b\sin\theta$（注意 $a$ 是 $x$ 方向半轴）；" "\n"
        r"② ⭐⭐ 逐个判断绝对值内式子的符号（配方法证恒正/恒负）；" "\n"
        r"③ ⭐⭐ 去绝对值后通常能用 $\sin^2+\cos^2=1$ 大幅化简，最后剩一个三角函数 ✓✓✓"
    ),
    'difficulty': 0.68,
    'topics': ['M-T-184'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-184-V2',
}

QS = [
    T195_E1, T195_V1, T195_V2, T195_V3,
    T197_E1, T197_V1, T197_V2, T197_V3,
    T123_E1, T123_V1, T123_V2, T123_V3,
    T184_E1, T184_V1, T184_V2,
]
