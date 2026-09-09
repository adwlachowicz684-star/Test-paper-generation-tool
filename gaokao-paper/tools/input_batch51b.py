# -*- coding: utf-8 -*-
r"""第51批（下）：解三角形 · 内切圆与形状判断

来源：2024高中数学热点题型归纳完整解析版.pdf
p171（PDF 页 170）M-T-208

## 选题

本文件取 M-T-208 的 E1、V1、V2、V3（4 题，全部可录）。

## ★★ 本批的核心工具：$\tan\frac A2=\dfrac r{s-a}$

**内切圆半径 $r$ 与半周长 $s$ 的关系**，四题里有三题靠它：

$$\tan\frac A2=\frac r{s-a},\qquad S=rs,\qquad r=\frac S s$$

推法：内切圆与 $AB,AC$ 的切点到 $A$ 的距离都是 $s-a$，
在顶点 $A$ 处的小直角三角形中 $\tan\frac A2=\frac r{s-a}$。

| 题 | 用法 | 答案 |
|---|---|---|
| E1 | $A=60^\circ$、$r=1$ ⟹ $s-a=\sqrt3$，配 $(b+c)^2\ge4bc$ 求 $\vec{AB}\cdot\vec{AC}$ 最小 | **A**（$6$） |
| V1 | $A=60^\circ$、$r=3$ ⟹ $s-a=3\sqrt3$，同理求 $S=3s$ 最小 | **D**（$27\sqrt3$） |
| V2 | 半角公式转 $1+\cos A=\sin B+\sin C$，两式相减得 $\sin(A+45^\circ)=\sin(B+45^\circ)$ | **B**（直角三角形） |
| V3 | ⭐ 角平分线到外接圆：$AD\cos\frac A2=R(\sin B+\sin C)$ | **D**（$4$） |

## ⚠ 两处必须注意

**1. E1 问的是向量点积 $\vec{AB}\cdot\vec{AC}$，不是 $|AB|\cdot|AC|$。**
我算出 $bc$ 最小 $=12$，**但 $12$ 是选项 D**；正确答案是 $12\cos60^\circ=6$（选项 A）。
若只读到 `AB ·AC` 就当成边长乘积，会选错。

**2. V2 的答案是「直角三角形」而不是「等腰直角三角形」。**
解得 $A+B=90^\circ$（即 $C=90^\circ$），**任意直角**都满足；$A=B=45^\circ$ 只是其中一个特例。
既然存在非等腰的直角（如 $30^\circ$-$60^\circ$-$90^\circ$），就不能说"一定是等腰直角"。
"""

T208_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知 $\triangle ABC$ 的内角分别为 $A,B,C$，$\cos^{2}\dfrac A2=1-\dfrac{\sqrt3}6\sin A$，"
        r"且 $\triangle ABC$ 的内切圆面积为 $\pi$，则 $\vec{AB}\cdot\vec{AC}$ 的最小值为（　　）"
    ),
    'opts': [
        ('A', r"$6$"),
        ('B', r"$8$"),
        ('C', r"$10$"),
        ('D', r"$12$"),
    ],
    'answer': 'A',
    'analysis': (
        r"先由半角关系解出 $A=60^\circ$；内切圆面积 $\pi$ ⟹ $r=1$。"
        r"用 $\tan\frac A2=\frac r{s-a}$ 得 $s-a=\sqrt3$，"
        r"再用 $(b+c)^{2}\ge4bc$ 夹出 $bc$ 的最小值，最后乘 $\cos A$ 得点积。"
    ),
    'solution': (
        r"**第一步：求角 $A$**" "\n"
        r"$\cos^{2}\dfrac A2=\dfrac{1+\cos A}2=1-\dfrac{\sqrt3}6\sin A$" "\n"
        r"$\Rightarrow1+\cos A=2-\dfrac{\sqrt3}3\sin A\Rightarrow\cos A+\dfrac1{\sqrt3}\sin A=1$" "\n"
        r"$\Rightarrow\dfrac{\sqrt3}2\cos A+\dfrac12\sin A=\dfrac{\sqrt3}2\Rightarrow\sin\left(A+60^\circ\right)=\dfrac{\sqrt3}2$" "\n"
        r"$\Rightarrow A+60^\circ=60^\circ$（舍，$A=0$）或 $120^\circ$，故 $A=60^\circ$．" "\n"
        r"**第二步：由 $r=1$ 建立关系**" "\n"
        r"内切圆面积 $\pi$ ⟹ $r=1$。由 $\tan\dfrac A2=\dfrac r{s-a}$：" "\n"
        r"$\tan30^\circ=\dfrac1{\sqrt3}=\dfrac1{s-a}\Rightarrow s-a=\sqrt3$，即 $a=s-\sqrt3$．" "\n"
        r"又 $S=rs=s$，且 $S=\dfrac12 bc\sin60^\circ=\dfrac{\sqrt3}4bc$，故 $bc=\dfrac{4s}{\sqrt3}$．" "\n"
        r"**第三步：用 $(b+c)^{2}\ge4bc$ 夹逼**" "\n"
        r"$b+c=2s-a=s+\sqrt3$，故 $(s+\sqrt3)^{2}\ge4\cdot\dfrac{4s}{\sqrt3}=\dfrac{16s}{\sqrt3}$．" "\n"
        r"乘 $3$：$3s^{2}+6\sqrt3s+9\ge16\sqrt3 s\Rightarrow3s^{2}-10\sqrt3 s+9\ge0$．" "\n"
        r"方程 $3s^{2}-10\sqrt3 s+9=0$ 的根：$s=\dfrac{10\sqrt3\pm\sqrt{300-108}}6=\dfrac{10\sqrt3\pm8\sqrt3}6$，" "\n"
        r"即 $s=3\sqrt3$ 或 $s=\dfrac{\sqrt3}3$（此时 $a=s-\sqrt3<0$，舍）．故 $s\ge3\sqrt3$．" "\n"
        r"**第四步：求点积**" "\n"
        r"$bc=\dfrac{4s}{\sqrt3}\ge\dfrac{4\cdot3\sqrt3}{\sqrt3}=12$，当 $s=3\sqrt3$ 时取等" "\n"
        r"（此时 $a=2\sqrt3$、$b=c=2\sqrt3$，即等边三角形）．" "\n"
        r"$\vec{AB}\cdot\vec{AC}=\lvert\vec{AB}\rvert\lvert\vec{AC}\rvert\cos A=bc\cos60^\circ\ge12\cdot\dfrac12=6$．选 A．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**详解未提取完整**，上述推导为我独立完成）。" "\n"
        r"**⚠⚠ 本题最大的坑 —— 我第一遍就选错了**：" "\n"
        r"我算出 $bc_{\min}=12$，一看 $12$ 在选项里（**D**），差点选 D。" "\n"
        r"但题干是 $\vec{AB}\cdot\vec{AC}$（**向量点积**），不是边长乘积 $bc$！" "\n"
        r"$\vec{AB}\cdot\vec{AC}=bc\cos A=12\times\frac12=6$ ✓ **选 A**。" "\n"
        r"**命题人把 $12$ 放在选项里，就是为「忘记乘 $\cos A$」准备的陷阱** ✓" "\n"
        r"**独立验算**：" "\n"
        r"① **验 $A=60^\circ$**：$\cos^{2}30^\circ=\frac34=0.75$；$1-\frac{\sqrt3}6\sin60^\circ=1-\frac{1.732}6(0.866)=1-0.25=0.75$ ✓✓" "\n"
        r"② **取等时是等边三角形**：$a=b=c=2\sqrt3$，则 $r=\frac{2\sqrt3}{2\sqrt3}=1$ ✓✓（等边 $r=\frac{a}{2\sqrt3}$）" "\n"
        r"验内切圆面积 $=\pi(1)^{2}=\pi$ ✓✓" "\n"
        r"③ **验 $bc=12$**：$(2\sqrt3)^{2}=12$ ✓；$s=3\sqrt3$、$a=2\sqrt3$、$s-a=\sqrt3$ ✓" "\n"
        r"$\tan30^\circ=\frac1{\sqrt3}=\frac{r}{s-a}=\frac1{\sqrt3}$ ✓✓✓" "\n"
        r"④ **验点积**：$\vec{AB}\cdot\vec{AC}=12\cos60^\circ=6$ ✓✓✓" "\n"
        r"⑤ **确认是最小值**（取另一个满足条件的三角形）：" "\n"
        r"取 $s=6$：$bc=\frac{24}{\sqrt3}=13.856$、$a=6-1.732=4.268$、$b+c=6+1.732=7.732$" "\n"
        r"验 $(b+c)^{2}=59.78\ge4bc=55.43$ ✓（可构成三角形）" "\n"
        r"点积 $=13.856\times0.5=6.928>6$ ✓✓ **确为最小**" "\n"
        r"**答案 A（$6$）正确** ✓" "\n"
        r"**⭐ 通法（内切圆半径参与的最值）**：" "\n"
        r"① **$\tan\frac A2=\frac r{s-a}$** —— 把 $r$ 和边联系起来，是内切圆题的第一工具；" "\n"
        r"（推法：顶点 $A$ 到两切点的距离都是 $s-a$，在角平分线上的小直角三角形中取正切。）" "\n"
        r"② $S=rs$ 与 $S=\frac12 bc\sin A$ 联立，把 $bc$ 用 $s$ 表示；" "\n"
        r"③ **$(b+c)^{2}\ge4bc$** 是夹逼 $s$ 的标准手段，取等时 $b=c$（等腰）。" "\n"
        r"**⚠ 易错**：二次不等式 $3s^{2}-10\sqrt3s+9\ge0$ 取**两侧**，" "\n"
        r"小的那个根要代回 $a=s-\sqrt3$ 检验是否为正 —— 本题 $s=\frac{\sqrt3}3$ 被舍掉。"
    ),
    'difficulty': 0.93,
    'topics': ['M-T-208'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-208-E1',
}

T208_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知 $\triangle ABC$ 的内角 $A,B,C$ 所对的边分别为 $a,b,c$，"
        r"若 $b\sin\dfrac{B+C}2=a\sin B$，且 $\triangle ABC$ 内切圆面积为 $9\pi$，"
        r"则 $\triangle ABC$ 面积的最小值为（　　）"
    ),
    'opts': [
        ('A', r"$3$"),
        ('B', r"$3\sqrt3$"),
        ('C', r"$9\sqrt3$"),
        ('D', r"$27\sqrt3$"),
    ],
    'answer': 'D',
    'analysis': (
        r"$\sin\frac{B+C}2=\sin\left(\frac\pi2-\frac A2\right)=\cos\frac A2$，"
        r"边化角后约去 $\sin B$ 得 $\cos\frac A2=\sin A$ ⟹ $A=60^\circ$。"
        r"内切圆面积 $9\pi$ ⟹ $r=3$ ⟹ $s-a=3\sqrt3$，再用 $(b+c)^2\ge4bc$ 夹出 $s\ge9\sqrt3$，$S=3s$。"
    ),
    'solution': (
        r"**第一步：求角 $A$**" "\n"
        r"$\dfrac{B+C}2=\dfrac{\pi-A}2=\dfrac\pi2-\dfrac A2$，故 $\sin\dfrac{B+C}2=\cos\dfrac A2$．" "\n"
        r"由正弦定理边化角：$\sin B\cos\dfrac A2=\sin A\sin B$．" "\n"
        r"因 $\sin B\neq0$：$\cos\dfrac A2=\sin A=2\sin\dfrac A2\cos\dfrac A2$．" "\n"
        r"由 $\cos\dfrac A2\neq0$：$1=2\sin\dfrac A2\Rightarrow\sin\dfrac A2=\dfrac12\Rightarrow A=60^\circ$．" "\n"
        r"**第二步：由 $r=3$ 建立关系**" "\n"
        r"内切圆面积 $9\pi$ ⟹ $r=3$。$\tan30^\circ=\dfrac1{\sqrt3}=\dfrac3{s-a}\Rightarrow s-a=3\sqrt3$，" "\n"
        r"即 $a=s-3\sqrt3$；$b+c=2s-a=s+3\sqrt3$．" "\n"
        r"$S=rs=3s$，又 $S=\dfrac12 bc\sin60^\circ=\dfrac{\sqrt3}4bc$，故 $bc=\dfrac{12s}{\sqrt3}=4\sqrt3\,s$．" "\n"
        r"**第三步：夹逼**" "\n"
        r"$(b+c)^{2}\ge4bc$：$(s+3\sqrt3)^{2}\ge16\sqrt3 s$" "\n"
        r"$\Rightarrow s^{2}+6\sqrt3 s+27\ge16\sqrt3 s\Rightarrow s^{2}-10\sqrt3 s+27\ge0$" "\n"
        r"根：$s=\dfrac{10\sqrt3\pm\sqrt{300-108}}2=\dfrac{10\sqrt3\pm8\sqrt3}2$，即 $s=9\sqrt3$ 或 $s=\sqrt3$" "\n"
        r"（$s=\sqrt3$ 时 $a=\sqrt3-3\sqrt3<0$，舍）．故 $s\ge9\sqrt3$．" "\n"
        r"$S=3s\ge27\sqrt3$．选 D．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**详解未提取完整**，上述推导为我独立完成）。" "\n"
        r"**这题与 E1 完全同构**（都是 $A=60^\circ$ + 内切圆半径 + $(b+c)^{2}\ge4bc$），" "\n"
        r"只是 $r$ 从 $1$ 变成 $3$，问的从「点积」变成「面积」。" "\n"
        r"**独立验算**：" "\n"
        r"① **验 $A=60^\circ$**：$b\cos30^\circ=a\sin B$，等边时 $b\cdot0.866=a\cdot0.866$ ✓" "\n"
        r"② **取等时**：$s=9\sqrt3$ ⟹ $bc=4\sqrt3(9\sqrt3)=4\cdot9\cdot3=108$；$b+c=s+3\sqrt3=12\sqrt3$" "\n"
        r"$t^{2}-12\sqrt3 t+108=0$，判别式 $=432-432=0$ ⟹ $b=c=6\sqrt3$；$a=s-3\sqrt3=6\sqrt3$" "\n"
        r"**等边三角形，边长 $6\sqrt3$** ✓" "\n"
        r"③ **验 $r$**：等边 $r=\frac{a}{2\sqrt3}=\frac{6\sqrt3}{2\sqrt3}=3$ ✓✓ **内切圆面积 $9\pi$ ✓✓**" "\n"
        r"④ **验面积**：$S=\frac12(6\sqrt3)^{2}\sin60^\circ=\frac12\cdot108\cdot\frac{\sqrt3}2=27\sqrt3$ ✓✓✓" "\n"
        r"$3s=3(9\sqrt3)=27\sqrt3$ ✓✓ **两法一致**" "\n"
        r"⑤ **确认是最小值**（取 $s=18$）：$bc=4\sqrt3(18)=72\sqrt3=124.7$；$b+c=18+5.196=23.196$" "\n"
        r"验 $(b+c)^{2}=538\ge4bc=498.8$ ✓；$S=3(18)=54>27\sqrt3=46.77$ ✓✓ **确为最小**" "\n"
        r"**答案 D（$27\sqrt3$）正确** ✓" "\n"
        r"**⭐ 通法**：" "\n"
        r"① $\sin\frac{B+C}2=\cos\frac A2$（**半角和公式**，看到 $\frac{B+C}2$ 就换掉）；" "\n"
        r"② 本题与 E1 是**同一个模型**，可对照练习：" "\n"
        r"$r=1$ ⟹ $s_{\min}=3\sqrt3$、$S_{\min}=3\sqrt3$；$r=3$ ⟹ $s_{\min}=9\sqrt3$、$S_{\min}=27\sqrt3$。" "\n"
        r"③ **一般地**：$A=60^\circ$ 时 $s-a=r\sqrt3$，$S=rs$，夹逼得 $s_{\min}=3\sqrt3\,r$、" "\n"
        r"$S_{\min}=3\sqrt3\,r^{2}$ —— 取等时必为**等边三角形**（因为 $b=c$ 且 $a=b$）。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-208'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-208-V1',
}

T208_V2 = {
    'type': '选择',
    'stem_text': (
        r"设 $\triangle ABC$ 的三边长为 $BC=a$，$CA=b$，$AB=c$，"
        r"若 $\tan\dfrac A2=\dfrac a{b+c}$，$\tan\dfrac B2=\dfrac b{a+c}$，则 $\triangle ABC$ 是（　　）"
    ),
    'opts': [
        ('A', r"等腰三角形"),
        ('B', r"直角三角形"),
        ('C', r"等腰三角形或直角三角形"),
        ('D', r"等腰直角三角形"),
    ],
    'answer': 'B',
    'analysis': (
        r"用 $\tan\frac A2=\frac{\sin A}{1+\cos A}$ 与正弦定理把右边边化角，"
        r"化简得 $1+\cos A=\sin B+\sin C$。对 $B$ 同理。"
        r"两式**相减**得 $\cos A+\sin A=\cos B+\sin B$，即 $\sin(A+45^\circ)=\sin(B+45^\circ)$。"
    ),
    'solution': (
        r"**第一步：化简条件**" "\n"
        r"$\tan\dfrac A2=\dfrac{\sin A}{1+\cos A}$；由正弦定理 $\dfrac a{b+c}=\dfrac{\sin A}{\sin B+\sin C}$．" "\n"
        r"两式相等且 $\sin A\neq0$：$1+\cos A=\sin B+\sin C$　①" "\n"
        r"同理由第二个条件：$1+\cos B=\sin A+\sin C$　②" "\n"
        r"**第二步：两式相减**" "\n"
        r"①$-$②：$\cos A-\cos B=\sin B-\sin A\Rightarrow\sin A+\cos A=\sin B+\cos B$" "\n"
        r"$\Rightarrow\sqrt2\sin\left(A+45^\circ\right)=\sqrt2\sin\left(B+45^\circ\right)$．" "\n"
        r"因 $A,B\in(0,\pi)$ 且 $A+B<\pi$：" "\n"
        r"· 若 $A+45^\circ=B+45^\circ$，则 $A=B$；" "\n"
        r"· 若 $(A+45^\circ)+(B+45^\circ)=180^\circ$，则 $A+B=90^\circ$，即 $C=90^\circ$．" "\n"
        r"**第三步：判断**" "\n"
        r"情形一 $C=90^\circ$：代回 ①，$1+\cos A=\sin(90^\circ-A)+1=\cos A+1$ ✓ **恒成立**，" "\n"
        r"即**任意直角三角形**都满足条件（如 $A=30^\circ,B=60^\circ,C=90^\circ$）．" "\n"
        r"情形二 $A=B$：代入 ① 需 $1+\cos A=\sin A+\sin2A$，数值解出 $A=45^\circ$，" "\n"
        r"此时 $C=90^\circ$，**是情形一的特例**（等腰直角）．" "\n"
        r"综上，所有解都满足 $C=90^\circ$，但**并非都是等腰的**，故选「直角三角形」．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**详解未提取完整**，上述推导为我独立完成）。" "\n"
        r"**⚠ 本题的陷阱在选项 D**：" "\n"
        r"解出 $A=B$ 时若只算 $A=B=45^\circ$，会以为答案是「等腰直角」（D）。" "\n"
        r"但 $A+B=90^\circ$ 这一支给出的是**任意直角三角形** —— " "\n"
        r"比如 $A=30^\circ,B=60^\circ,C=90^\circ$ 也满足条件，**它不是等腰的** ✗。" "\n"
        r"既然存在非等腰的解，就不能选 D，只能选 B ✓" "\n"
        r"**独立验算**（逐项代入原式）：" "\n"
        r"① **验 $30^\circ$-$60^\circ$-$90^\circ$**（$a=\sin30^\circ=0.5$、$b=\sin60^\circ=0.866$、$c=1$）：" "\n"
        r"$\tan\frac A2=\tan15^\circ=0.2679$；$\frac a{b+c}=\frac{0.5}{0.866+1}=\frac{0.5}{1.866}=0.2679$ ✓✓" "\n"
        r"$\tan\frac B2=\tan30^\circ=0.5774$；$\frac b{a+c}=\frac{0.866}{0.5+1}=\frac{0.866}{1.5}=0.5773$ ✓✓ **成立**" "\n"
        r"② **验 $20^\circ$-$70^\circ$-$90^\circ$**（非等腰、非特殊角）：" "\n"
        r"$a=\sin20^\circ=0.342$、$b=\sin70^\circ=0.940$、$c=1$" "\n"
        r"$\tan10^\circ=0.1763$；$\frac{0.342}{0.940+1}=\frac{0.342}{1.940}=0.1763$ ✓✓" "\n"
        r"$\tan35^\circ=0.7002$；$\frac{0.940}{0.342+1}=\frac{0.940}{1.342}=0.7004$ ✓✓ **也成立**" "\n"
        r"→ **确实任意直角三角形都满足**，与「等腰直角」不符 ✗ → 排除 D ✓" "\n"
        r"③ **验非直角不成立**（取等边 $A=B=C=60^\circ$）：" "\n"
        r"$\tan30^\circ=0.5774$；$\frac a{b+c}=\frac1{1+1}=0.5$ ✗ **不相等** ✓ 排除 A、C" "\n"
        r"④ **验等腰直角 $45^\circ$-$45^\circ$-$90^\circ$**：$a=b=0.7071$、$c=1$" "\n"
        r"$\tan22.5^\circ=0.4142$；$\frac{0.7071}{0.7071+1}=\frac{0.7071}{1.7071}=0.4142$ ✓✓（是特例）" "\n"
        r"**答案 B（直角三角形）正确** ✓" "\n"
        r"**⭐ 通法**：" "\n"
        r"① $\tan\frac x2=\frac{\sin x}{1+\cos x}$（半角公式的**正弦形式**，比 $\frac{1-\cos x}{\sin x}$ 好用，" "\n"
        r"因为右边分母正好是 $\sin B+\sin C$ 能约）；" "\n"
        r"② 得到两个对称的式子后，**相减**往往比各自处理更快 —— " "\n"
        r"本题相减直接给出 $\sin(A+45^\circ)=\sin(B+45^\circ)$；" "\n"
        r"③ **⚠ 判断形状题要选「最弱且必然成立」的那个结论**：" "\n"
        r"若解集 $=\{$所有直角三角形$\}$，则「直角三角形」对，「等腰直角」错（不都是）、" "\n"
        r"「等腰」错（不都是）。**举一个反例就能排除一个选项**，这是最快的验证法。"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-208'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-208-V2',
}

T208_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知 $\triangle ABC$ 内接于半径为 $2$ 的 $\odot O$，内角 $A,B,C$ 的角平分线分别与 $\odot O$ "
        r"相交于 $D,E,F$ 三点，若" "\n"
        r"$AD\cdot\cos\dfrac A2+BE\cdot\cos\dfrac B2+CF\cdot\cos\dfrac C2=\lambda\left(\sin A+\sin B+\sin C\right)$，" "\n"
        r"则 $\lambda=$（　　）"
    ),
    'opts': [
        ('A', r"$1$"),
        ('B', r"$2$"),
        ('C', r"$3$"),
        ('D', r"$4$"),
    ],
    'answer': 'D',
    'analysis': (
        r"**核心结论**：若角平分线 $AD$ 交外接圆于 $D$，则 $AD\cos\frac A2=R(\sin B+\sin C)$。"
        r"三项相加得 $2R(\sin A+\sin B+\sin C)$，故 $\lambda=2R=4$。"
    ),
    'solution': (
        r"**第一步：求 $AD$ 的长**" "\n"
        r"$AD$ 是 $\angle A$ 的平分线，$D$ 在弧 $BC$（不含 $A$）的**中点**上．" "\n"
        r"在圆中看弦 $AD$，它所对的圆周角是 $\angle ABD$．" "\n"
        r"$\angle ABD=\angle ABC+\angle CBD$，其中 $\angle CBD$ 对弧 $CD$，" "\n"
        r"而弧 $CD=$ 弧 $BD$（$D$ 是中点），$\angle CBD=\angle BAD=\dfrac A2$．" "\n"
        r"故 $\angle ABD=B+\dfrac A2$，由正弦定理（弦长 $=2R\sin$ 圆周角）：" "\n"
        r"$AD=2R\sin\left(B+\dfrac A2\right)$．" "\n"
        r"**第二步：乘 $\cos\frac A2$ 化简**" "\n"
        r"$AD\cos\dfrac A2=2R\sin\left(B+\dfrac A2\right)\cos\dfrac A2$" "\n"
        r"$=R\left[\sin\left(B+\dfrac A2+\dfrac A2\right)+\sin\left(B+\dfrac A2-\dfrac A2\right)\right]$" "\n"
        r"$=R\left[\sin(A+B)+\sin B\right]=R\left(\sin C+\sin B\right)$（因 $\sin(A+B)=\sin C$）．" "\n"
        r"**第三步：三项相加**" "\n"
        r"同理 $BE\cos\dfrac B2=R(\sin A+\sin C)$，$CF\cos\dfrac C2=R(\sin A+\sin B)$．" "\n"
        r"和 $=R\cdot2(\sin A+\sin B+\sin C)=2R(\sin A+\sin B+\sin C)$．" "\n"
        r"故 $\lambda=2R=2\times2=4$．选 D．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**详解未提取完整**，上述推导为我独立完成）。" "\n"
        r"**独立验算**（构造具体三角形逐项核对）：取 $R=2$、$A=60^\circ$、$B=80^\circ$、$C=40^\circ$" "\n"
        r"$a=2R\sin A=4\sin60^\circ=3.464$；$b=4\sin80^\circ=3.939$；$c=4\sin40^\circ=2.571$" "\n"
        r"① **算 $AD$**：$\angle ABD=B+\frac A2=80^\circ+30^\circ=110^\circ$；" "\n"
        r"$AD=2R\sin110^\circ=4(0.9397)=3.7588$" "\n"
        r"验（用角平分线长公式 $AD_{\text{到边}}=\frac{2bc\cos(A/2)}{b+c}$ 再延长）：" "\n"
        r"角平分线到 $BC$ 的长度 $=\frac{2(3.939)(2.571)\cos30^\circ}{3.939+2.571}=\frac{20.254(0.866)}{6.510}=\frac{17.540}{6.510}=2.694$" "\n"
        r"延长到圆上的全长 $AD$ 应 $>2.694$ ✓（$3.7588$）" "\n"
        r"② **验恒等式 $AD\cos\frac A2=R(\sin B+\sin C)$**：" "\n"
        r"左 $=3.7588\times\cos30^\circ=3.7588\times0.8660=3.2552$" "\n"
        r"右 $=2(\sin80^\circ+\sin40^\circ)=2(0.9848+0.6428)=2(1.6276)=3.2552$ ✓✓✓ **完全相等**" "\n"
        r"③ **三项求和**：" "\n"
        r"$BE$：$\angle BCE$… 同理 $BE=2R\sin(C+\frac B2)=4\sin(40^\circ+40^\circ)=4\sin80^\circ=3.939$" "\n"
        r"$BE\cos\frac B2=3.939\cos40^\circ=3.939(0.766)=3.017$；右 $=2(\sin A+\sin C)=2(0.866+0.6428)=3.0176$ ✓✓" "\n"
        r"$CF=2R\sin(A+\frac C2)=4\sin(60^\circ+20^\circ)=4\sin80^\circ=3.939$" "\n"
        r"$CF\cos\frac C2=3.939\cos20^\circ=3.939(0.9397)=3.701$；右 $=2(\sin A+\sin B)=2(0.866+0.9848)=3.7016$ ✓✓" "\n"
        r"三项和 $=3.2552+3.017+3.701=9.973$" "\n"
        r"$2R(\sin A+\sin B+\sin C)=4(0.866+0.9848+0.6428)=4(2.4936)=9.974$ ✓✓✓" "\n"
        r"$\lambda=\frac{9.973}{2.4936}=3.9998\approx4$ ✓✓✓" "\n"
        r"**答案 D（$4$）正确** ✓" "\n"
        r"**⭐ 通法（角平分线延长到外接圆）**：" "\n"
        r"$$AD=2R\\sin\\left(B+\\frac A2\\right),\\qquad AD\\cos\\frac A2=R(\\sin B+\\sin C)$$" "\n"
        r"① $D$ 是**弧 $BC$ 的中点**（角平分线的性质）—— 由此 $\angle CBD=\frac A2$；" "\n"
        r"② 弦长 $=2R\sin(\text{所对圆周角})$，取 $\angle ABD$ 作为圆周角；" "\n"
        r"③ 乘 $\cos\frac A2$ 后用**积化和差** $2\sin X\cos Y=\sin(X+Y)+\sin(X-Y)$，" "\n"
        r"两项正好变成 $\sin(A+B)=\sin C$ 与 $\sin B$ —— **结构极干净**。" "\n"
        r"**结论**：三项之和恒为 $2R(\sin A+\sin B+\sin C)$，故 $\lambda=2R$ 与三角形形状无关。"
    ),
    'difficulty': 0.94,
    'topics': ['M-T-208'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-208-V3',
}

QS = [T208_E1, T208_V1, T208_V2, T208_V3]
