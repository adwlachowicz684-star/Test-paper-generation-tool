# -*- coding: utf-8 -*-
r"""第52批（下）：解三角形 · 角平分线（4 题全录）

来源：2024高中数学热点题型归纳完整解析版.pdf
p164、p165（PDF 页 163、164）M-T-202

## ★★ 原书「提分秘籍」三条（本批的核心）

> 1. 角平分线，可以借助面积**「和」**构造等量关系
> 2. 角平分线也是两边的**「对称轴」**
> 3. 三角形角平分线定理可以**直接在小题中使用**

四题正好覆盖这三条：

| 题 | 用哪条 | 手段 |
|---|---|---|
| E1 | 角平分线定理 | $AB:AC=BD:DC=2:1$，设 $AC=x$ 则 $AB=2x$，面积转一元函数 |
| V1 | 对称轴（$2$） | 延长 $BP$ 交 $AC$ 延长线，用**等腰**性质 + 割补面积 |
| V2 | 面积和（$1$） | 面积比 $3:2$ ⟹ $AC:CB=3:2$，再配 $A:B=1:2$ |
| V3 | 角平分线定理 | 分别在 $\triangle ABM$、$\triangle CBM$ 中用正弦定理 |

## 四题验算（全部独立推导，与答案吻合）

| 题 | 我的结果 | 答案 |
|---|---|---|
| E1 | $S^{2}=-\frac9{16}[(x^{2}-20)^{2}-256]$，最大 $S=12$ | **C** |
| V1 | $x=2\sqrt3$、$\sin\angle ACB=\frac{2\sqrt2}3$，$S=4\sqrt2$ | **B** |
| V2 | $AC=3x$、$CB=2x$，$\frac{3x}{\sin2\alpha}=\frac{2x}{\sin\alpha}$ ⟹ $\cos\alpha=\frac34$ | **C** |
| V3 | $\frac2{AM}-\frac1{CM}=\sqrt3\sin(A-\frac\pi6)\in(-\frac{\sqrt3}2,\sqrt3)$ | **A** |
"""

T202_E1 = {
    'type': '选择',
    'stem_text': (
        r"在 $\triangle ABC$ 中，$\angle BAC$ 的平分线交 $BC$ 于点 $D$，$BD=2DC$，$BC=6$，"
        r"则 $\triangle ABC$ 的面积的最大值为（　　）"
    ),
    'opts': [
        ('A', r"$6$"),
        ('B', r"$6\sqrt2$"),
        ('C', r"$12$"),
        ('D', r"$12\sqrt2$"),
    ],
    'answer': 'C',
    'analysis': (
        r"由**角平分线定理** $AB:AC=BD:DC=2:1$，设 $AC=x$ 则 $AB=2x$。"
        r"面积 $S=x^{2}\sin\theta$（$\theta=\angle BAC$），再用余弦定理把 $\cos\theta$ 表成 $x$ 的函数，"
        r"得到 $S^{2}$ 关于 $x^{2}$ 的二次函数，配方法取最大。"
    ),
    'solution': (
        r"**第一步：角平分线定理**" "\n"
        r"$\dfrac{AB}{AC}=\dfrac{BD}{DC}=\dfrac21$。设 $AC=x$，则 $AB=2x$．" "\n"
        r"（由 $BD=2DC$ 且 $BD+DC=BC=6$ 得 $DC=2$、$BD=4$，比值确为 $2:1$。）" "\n"
        r"**第二步：面积与 $\theta=\angle BAC$**" "\n"
        r"$S=\dfrac12\,AB\cdot AC\cdot\sin\theta=\dfrac12\cdot2x\cdot x\sin\theta=x^{2}\sin\theta$．" "\n"
        r"**第三步：余弦定理表出 $\cos\theta$**" "\n"
        r"$\cos\theta=\dfrac{AB^{2}+AC^{2}-BC^{2}}{2\,AB\cdot AC}=\dfrac{4x^{2}+x^{2}-36}{2\cdot2x\cdot x}=\dfrac{5x^{2}-36}{4x^{2}}$．" "\n"
        r"**第四步：$S^{2}$ 转二次函数**" "\n"
        r"$S^{2}=x^{4}\sin^{2}\theta=x^{4}(1-\cos^{2}\theta)=x^{4}-x^{4}\cdot\dfrac{(5x^{2}-36)^{2}}{16x^{4}}$" "\n"
        r"$=x^{4}-\dfrac{25x^{4}-360x^{2}+1296}{16}=\dfrac{-9x^{4}+360x^{2}-1296}{16}$" "\n"
        r"$=-\dfrac9{16}\left(x^{4}-40x^{2}+144\right)=-\dfrac9{16}\left[(x^{2}-20)^{2}-256\right]$．" "\n"
        r"当 $x^{2}=20$ 时 $S^{2}$ 取最大值 $\dfrac9{16}\times256=144$，故 $S_{\max}=12$．选 C．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓，由详解「设 $AC=x$，$\angle BAC=\theta$，则由正弦定理可得…" "\n"
        r"则 $AB=2x$，则 $S_{\triangle ABC}=\frac12 AB\cdot AC\cdot\sin\angle BAC=\frac12 x\cdot2x\cdot\sin\theta=x^{2}\sin\theta$…" "\n"
        r"$\cos\angle BAC=\frac{5x^{2}-36}{4x^{2}}$…$S^{2}=x^{4}\sin^{2}\theta=x^{4}(1-\cos^{2}\theta)=x^{4}-\frac{25x^{4}-360x^{2}+36^{2}}{16}$" "\n"
        r"$=-\frac9{16}(9x^{4}-40x^{2}+144)$…当 $x^{2}=20$ 时，$S^{2}$ 有最大值，$(S^{2})_{\max}=\frac9{16}\times256=144$，" "\n"
        r"所以 $S_{\max}=12$，故选 C」还原，**与我的推导完全一致** ✓。" "\n"
        r"**独立验算**：" "\n"
        r"① **角平分线定理**：$AB:AC=BD:DC=2:1$ ⟹ $AB=2x$、$AC=x$ ✓" "\n"
        r"② **$DC,BD$**：$BD+DC=6$、$BD=2DC$ ⟹ $3DC=6$ ⟹ $DC=2$、$BD=4$ ✓" "\n"
        r"③ **配方法**：$x^{4}-40x^{2}+144=(x^{2}-20)^{2}-400+144=(x^{2}-20)^{2}-256$ ✓" "\n"
        r"④ **$S^{2}_{\max}$**：$-\frac9{16}(0-256)=\frac9{16}(256)=9\times16=144$ ⟹ $S=12$ ✓✓" "\n"
        r"⑤ **构造取等时的三角形反验**：$x^{2}=20$ ⟹ $AC=\sqrt{20}=4.472$、$AB=2\sqrt{20}=8.944$" "\n"
        r"$\cos\theta=\frac{5(20)-36}{4(20)}=\frac{100-36}{80}=\frac{64}{80}=0.8$ ⟹ $\sin\theta=0.6$" "\n"
        r"$S=\frac12\cdot8.944\cdot4.472\cdot0.6=\frac12\cdot40\cdot0.6=12$ ✓✓✓" "\n"
        r"⑥ **验 $BC=6$**：$BC^{2}=AB^{2}+AC^{2}-2(AB)(AC)\cos\theta=80+20-2(8.944)(4.472)(0.8)$" "\n"
        r"$=100-2(40)(0.8)=100-64=36$ ⟹ $BC=6$ ✓✓✓ **完全闭合**" "\n"
        r"⑦ **验角平分线**（确认 $D$ 分点比例）：$BD:DC=AB:AC=2:1$ ✓ 且 $BD+DC=6$ ✓" "\n"
        r"**答案 C（$12$）正确** ✓" "\n"
        r"**⭐ 通法（角平分线 + 面积最值）**：" "\n"
        r"① **角平分线定理** $\frac{AB}{AC}=\frac{BD}{DC}$ 可**直接在小题使用**，不必证明；" "\n"
        r"② 设一份为 $x$，把两边都表示成 $x$ 的倍数，面积就成了 $S=kx^{2}\sin\theta$；" "\n"
        r"③ 用余弦定理把 $\cos\theta$ 表成 $x$ 的函数 → $S^{2}$ 是 $x^{2}$ 的**二次函数** → 配方法取最值。" "\n"
        r"**⚠ 关键技巧**：算 $S^{2}$（而不是 $S$）能避开根号，且 $x^{4}\cos^{2}\theta$ 中 $x^{4}$ 与分母 $16x^{4}$ 正好约掉，" "\n"
        r"这是题目刻意设计的 —— **看到这种约分就知道路子走对了**。"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-202'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-202-E1',
}

T202_V2 = {
    'type': '选择',
    'stem_text': (
        r"如图所示，在 $\triangle ABC$ 中，已知 $\angle A:\angle B=1:2$，"
        r"角 $C$ 的平分线 $CD$ 把三角形面积分为 $3:2$ 两部分，则 $\cos A$ 等于（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac13$"),
        ('B', r"$\dfrac12$"),
        ('C', r"$\dfrac34$"),
        ('D', r"$0$"),
    ],
    'answer': 'C',
    'analysis': (
        r"**角平分线的面积性质**：$CD$ 平分 $\angle C$ ⟹ $\angle ACD=\angle BCD$ ⟹ "
        r"两个小三角形面积比 $=\frac{AC\cdot CD\sin\angle ACD}{CB\cdot CD\sin\angle BCD}=\frac{AC}{CB}$。"
        r"故 $\frac{AC}{CB}=\frac32$。再配 $\angle A:\angle B=1:2$ 用正弦定理。"
    ),
    'solution': (
        r"**第一步：面积比转边长比**" "\n"
        r"因 $CD$ 平分 $\angle C$，有 $\angle ACD=\angle BCD$。于是" "\n"
        r"$\dfrac{S_{\triangle ACD}}{S_{\triangle BCD}}=\dfrac{\frac12 AC\cdot CD\sin\angle ACD}{\frac12 CB\cdot CD\sin\angle BCD}=\dfrac{AC}{CB}=\dfrac32$．" "\n"
        r"设 $AC=3x$、$CB=2x$．" "\n"
        r"**第二步：正弦定理**" "\n"
        r"设 $\angle A=\alpha$、$\angle B=2\alpha$。由正弦定理 $\dfrac{BC}{\sin A}=\dfrac{AC}{\sin B}$：" "\n"
        r"$\dfrac{2x}{\sin\alpha}=\dfrac{3x}{\sin2\alpha}=\dfrac{3x}{2\sin\alpha\cos\alpha}$．" "\n"
        r"约去 $x$ 与 $\sin\alpha$（均非零）：$2=\dfrac3{2\cos\alpha}\Rightarrow\cos\alpha=\dfrac34$．" "\n"
        r"即 $\cos A=\dfrac34$．选 C．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓，由详解「∵ 角 $C$ 的平分线 $CD$，∴ $\angle ACD=\angle BCD$，" "\n"
        r"∵ $\frac{S_{\triangle ACD}}{S_{\triangle BCD}}=\frac{\frac12 AC\cdot CD\sin\angle ACD}{\frac12 CB\cdot CD\sin\angle BCD}=\frac{AC}{CB}=\frac32$，" "\n"
        r"∴ 设 $AC=3x,CB=2x$。∵ $\angle A:\angle B=1:2$，设 $\angle A=\alpha,\angle B=2\alpha$，在 $\triangle ABC$ 中" "\n"
        r"利用正弦定理 $\frac{2x}{\sin\alpha}=\frac{3x}{\sin2\alpha}=\frac{3x}{2\sin\alpha\cos\alpha}$，解得 $\cos\alpha=\frac34$」还原，" "\n"
        r"**与我的推导逐字一致** ✓。" "\n"
        r"**独立验算**：" "\n"
        r"① **$\cos A=\frac34$** ⟹ $A=\arccos0.75=41.41^\circ$、$B=2A=82.82^\circ$、$C=180-3A=55.77^\circ$" "\n"
        r"② **验正弦定理**：$\frac{BC}{\sin A}=\frac{2x}{0.6614}=3.024x$；$\frac{AC}{\sin B}=\frac{3x}{0.9921}=3.024x$ ✓✓ **相等**" "\n"
        r"（$\sin A=\sin41.41^\circ=0.6614$、$\sin B=\sin82.82^\circ=0.9921$）" "\n"
        r"③ **验面积比**：$\frac{AC}{CB}=\frac{3x}{2x}=1.5=\frac32$ ✓✓" "\n"
        r"④ **$\sin2\alpha=2\sin\alpha\cos\alpha$ 验证**：$2(0.6614)(0.75)=0.9921$ ✓✓" "\n"
        r"⑤ **排除其他选项**：若 $\cos A=\frac12$ 则 $A=60^\circ$、$B=120^\circ$、$C=0^\circ$ **退化** ✗；" "\n"
        r"若 $\cos A=0$ 则 $A=90^\circ$、$B=180^\circ$ **退化** ✗；$\frac13$ 不满足正弦定理 ✗" "\n"
        r"**答案 C（$\frac34$）正确** ✓" "\n"
        r"**⭐ 通法（角平分线分面积）**：" "\n"
        r"$$\\frac{S_{\\triangle ACD}}{S_{\\triangle BCD}}=\\frac{AC}{CB}$$" "\n"
        r"**角平分线分出的两个小三角形，面积比 = 夹该角的两边之比**（因为高（$CD$）和 $\sin$（半角）都相同）。" "\n"
        r"这条比「角平分线定理 $\frac{AD}{DB}=\frac{AC}{CB}$」更直接 —— **给面积比就用这条，给线段比就用那条**。" "\n"
        r"**⚠ 易错**：$\sin2\alpha=2\sin\alpha\cos\alpha$ 展开后，约分时注意 $\sin\alpha\neq0$（$\alpha\in(0,\pi)$）," "\n"
        r"本题约掉 $\sin\alpha$ 后直接得 $\cos\alpha$，非常快 —— 若展开成 $\sin^2$ 会绕远。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-202'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-202-V2',
}

T202_V3 = {
    'type': '选择',
    'stem_text': (
        r"在 $\triangle ABC$ 中，$B=\dfrac\pi3$，$M$ 为 $AC$ 边上的一点，且 $BM=2$，"
        r"若 $BM$ 为 $\angle ABC$ 的角平分线，则 $\dfrac2{AM}-\dfrac1{CM}$ 的取值范围为（　　）"
    ),
    'opts': [
        ('A', r"$\left(-\dfrac{\sqrt3}2,\ \sqrt3\right)$"),
        ('B', r"$\left[-\dfrac{\sqrt3}2,\ \sqrt3\right]$"),
        ('C', r"$\left(-\dfrac12,\ \sqrt3\right)$"),
        ('D', r"$\left(-\dfrac12,\ \sqrt3\right]$"),
    ],
    'answer': 'A',
    'analysis': (
        r"$\angle ABC=\frac\pi3$ 且 $BM$ 平分 ⟹ $\angle ABM=\angle CBM=\frac\pi6$。"
        r"分别在 $\triangle ABM$、$\triangle CBM$ 中用正弦定理，把 $\frac1{AM}$、$\frac1{CM}$ 表成 $\sin A$、$\sin C$，"
        r"再用 $A+C=\frac{2\pi}3$ 化成一个角的三角函数。"
    ),
    'solution': (
        r"**第一步：两个正弦定理**" "\n"
        r"$\angle ABM=\angle CBM=\dfrac\pi6$．" "\n"
        r"在 $\triangle ABM$ 中：$\dfrac{BM}{\sin A}=\dfrac{AM}{\sin\angle ABM}$，" "\n"
        r"即 $\dfrac2{\sin A}=\dfrac{AM}{\sin\frac\pi6}=\dfrac{AM}{1/2}\Rightarrow AM=\dfrac1{\sin A}$，故 $\dfrac1{AM}=\sin A$．" "\n"
        r"在 $\triangle CBM$ 中：$\dfrac{BM}{\sin C}=\dfrac{CM}{\sin\angle CBM}$，" "\n"
        r"即 $\dfrac2{\sin C}=\dfrac{CM}{1/2}\Rightarrow CM=\dfrac1{\sin C}$，故 $\dfrac1{CM}=\sin C$．" "\n"
        r"**第二步：化一个角**" "\n"
        r"$A+C=\pi-B=\dfrac{2\pi}3$，故 $C=\dfrac{2\pi}3-A$．" "\n"
        r"$\dfrac2{AM}-\dfrac1{CM}=2\sin A-\sin C=2\sin A-\sin\left(\dfrac{2\pi}3-A\right)$" "\n"
        r"$=2\sin A-\left(\dfrac{\sqrt3}2\cos A+\dfrac12\sin A\right)=\dfrac32\sin A-\dfrac{\sqrt3}2\cos A$" "\n"
        r"$=\sqrt3\left(\dfrac{\sqrt3}2\sin A-\dfrac12\cos A\right)=\sqrt3\sin\left(A-\dfrac\pi6\right)$．" "\n"
        r"**第三步：定范围**" "\n"
        r"$A\in\left(0,\dfrac{2\pi}3\right)$ ⟹ $A-\dfrac\pi6\in\left(-\dfrac\pi6,\ \dfrac\pi2\right)$ ⟹ $\sin\left(A-\dfrac\pi6\right)\in\left(-\dfrac12,\ 1\right)$．" "\n"
        r"故 $\dfrac2{AM}-\dfrac1{CM}\in\left(-\dfrac{\sqrt3}2,\ \sqrt3\right)$．选 A．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓，由详解「在 $\triangle ABM$ 中，$\frac{BM}{\sin A}=\frac{AM}{\sin\angle ABM}$，" "\n"
        r"因为 $BM=2$，所以…$AM=2\sin A$…在 $\triangle CBM$ 中…$CM=2\sin C$，所以 $\frac1{CM}=\sin C$，" "\n"
        r"则 $\frac2{AM}-\frac1{CM}=2\sin A-\sin C=2\sin A-\sin(\frac{2\pi}3-A)=\sqrt3\sin(A-\frac\pi6)$，" "\n"
        r"因为 $0<A<\frac{2\pi}3$，所以 $-\frac\pi6<A-\frac\pi6<\frac\pi2$，所以 $-\frac12<\sin(A-\frac\pi6)<1$，" "\n"
        r"则 $\frac2{AM}-\frac1{CM}$ 的取值范围为 $(-\frac{\sqrt3}2,\sqrt3)$。选 A」还原，**与我的推导一致** ✓。" "\n"
        r"**⚠ 详解的 $AM$ 表达式有一处不一致**：详解写「$AM=2\sin A$」，" "\n"
        r"但按 $\frac2{\sin A}=\frac{AM}{\sin(\pi/6)}=2AM$ 应得 $AM=\frac1{\sin A}$。" "\n"
        r"**以我推导的 $\frac1{AM}=\sin A$ 为准** —— 因为后续 $\frac2{AM}-\frac1{CM}=2\sin A-\sin C$ 与之一致，且答案吻合。" "\n"
        r"（若按详解字面 $AM=2\sin A$，则 $\frac1{AM}=\frac1{2\sin A}$，根本凑不出 $2\sin A-\sin C$。）" "\n"
        r"**独立验算**（逐点代入）：" "\n"
        r"① **辅助角变换**：$\frac32\sin A-\frac{\sqrt3}2\cos A$，振幅 $=\sqrt{(\frac32)^2+(\frac{\sqrt3}2)^2}=\sqrt{\frac94+\frac34}=\sqrt3$ ✓" "\n"
        r"$\sqrt3\sin(A-\frac\pi6)=\sqrt3(\sin A\cos\frac\pi6-\cos A\sin\frac\pi6)=\sqrt3(\frac{\sqrt3}2\sin A-\frac12\cos A)=\frac32\sin A-\frac{\sqrt3}2\cos A$ ✓✓" "\n"
        r"② **端点**：$A\to0^+$ 时 $\sqrt3\sin(-\frac\pi6)=-\frac{\sqrt3}2=-0.866$（**开**，因 $A>0$）" "\n"
        r"$A\to\frac{2\pi}3{}^-$ 时 $\sqrt3\sin(\frac\pi2)=\sqrt3=1.732$（**开**，因 $A<\frac{2\pi}3$）" "\n"
        r"③ **逐点验证**（$f(A)=2\sin A-\sin(\frac{2\pi}3-A)$）：" "\n"
        r"· $A=1^\circ$：$f=-0.8397$（接近 $-\frac{\sqrt3}2=-0.866$ ✓ 未取到）" "\n"
        r"· $A=30^\circ$：$f=-0.0000$（$A=\frac\pi6$ 时 $\sin(A-\frac\pi6)=0$ ✓）" "\n"
        r"· $A=60^\circ$：$f=0.8660$；$\sqrt3\sin30^\circ=\sqrt3(0.5)=0.866$ ✓✓" "\n"
        r"· $A=90^\circ$：$f=1.5$；$\sqrt3\sin60^\circ=\sqrt3(0.866)=1.5$ ✓✓" "\n"
        r"· $A=119^\circ$：$f=1.7318$（接近 $\sqrt3=1.732$ ✓ 未取到）" "\n"
        r"④ **验证 $BM=2$ 的可行性**（取 $A=60^\circ$）：$C=60^\circ$，等边三角形。" "\n"
        r"$AM=\frac1{\sin60^\circ}=\frac1{0.866}=1.1547$；$CM=\frac1{\sin60^\circ}=1.1547$" "\n"
        r"$AM+CM=AC=2.309$；而等边三角形中 $BM$ 是角平分线也是中线，$BM=\frac{\sqrt3}2\cdot AC=0.866(2.309)=2.0$ ✓✓✓" "\n"
        r"**完全自洽** —— 说明 $\frac1{AM}=\sin A$、$\frac1{CM}=\sin C$ 正确。" "\n"
        r"⑤ **排除 B/D**：两个端点都取不到（$A=0$ 或 $A=\frac{2\pi}3$ 都会使三角形退化），必为**开区间** ✓" "\n"
        r"**答案 A（$(-\frac{\sqrt3}2,\sqrt3)$）正确** ✓" "\n"
        r"**⭐ 通法（角平分线上的线段 → 倒数的三角函数）**：" "\n"
        r"① 角平分线把顶角分成两半，在**两个小三角形**中各用一次正弦定理；" "\n"
        r"② 由于 $\frac{BM}{\sin(\text{底角})}=\frac{\text{边}}{\sin(\text{半角})}$，而 $\sin(\text{半角})$ 是**常数**，" "\n"
        r"所以 $\frac1{\text{边}}\propto\sin(\text{底角})$ —— **取倒数后形式极简**；" "\n"
        r"③ 用 $A+C=\pi-B$ 消元，再用辅助角公式 $p\sin A+q\cos A$ 合并；" "\n"
        r"④ ⚠ **区间开闭**看端点是否使三角形退化（本题两端都退化 ⟹ 全开）。"
    ),
    'difficulty': 0.91,
    'topics': ['M-T-202'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-202-V3',
}

T202_V1 = {
    'type': '选择',
    'stem_text': (
        r"如图，$\triangle ABC$ 中，$\angle ACB$ 为钝角，$AC=10$，$BC=6$，"
        r"过点 $B$ 向 $\angle ACB$ 的角平分线引垂线交于点 $P$，若 $AP=6\sqrt2$，"
        r"则 $\triangle ABP$ 的面积为（　　）"
    ),
    'opts': [
        ('A', r"$4$"),
        ('B', r"$4\sqrt2$"),
        ('C', r"$6$"),
        ('D', r"$4\sqrt3$"),
    ],
    'answer': 'B',
    'analysis': (
        r"设 $CP=x$、$\angle ACP=\angle BCP=\theta$。在 $\triangle BCP$ 中用余弦表出 $\cos\theta=\frac{BC}{CP}$？" "\n"
        r"—— 正确做法：先由 $\mathrm{Rt}\triangle$ 关系在 $\triangle BCP$ 中得 $\cos\theta=\frac{CP}{BC}$，" "\n"
        r"再在 $\triangle ACP$ 中用余弦定理（含 $AP=6\sqrt2$）解出 $x$，最后 $S_{\triangle ABP}=S_{\triangle ACB}-S_{\triangle ACP}-S_{\triangle BCP}$．"
    ),
    'solution': (
        r"**第一步：设未知量**" "\n"
        r"设 $CP=x$，$\angle ACP=\angle BCP=\theta$（$CP$ 平分 $\angle ACB$）．" "\n"
        r"**第二步：在 $\triangle BCP$ 中**" "\n"
        r"因 $BP\perp CP$，$\triangle BCP$ 在 $P$ 处直角？——注意 $BP\perp CP$ 且 $P$ 在角平分线 $CP$ 上，" "\n"
        r"故 $\angle BPC=90^\circ$。于是 $\cos\theta=\dfrac{CP}{BC}=\dfrac x6$．" "\n"
        r"（同时 $BP=BC\sin\theta=6\sin\theta$。）" "\n"
        r"**第三步：在 $\triangle ACP$ 中用余弦定理**" "\n"
        r"$AP^{2}=CP^{2}+CA^{2}-2\,CP\cdot CA\cos\theta$：" "\n"
        r"$(6\sqrt2)^{2}=x^{2}+10^{2}-2\cdot x\cdot10\cdot\dfrac x6$" "\n"
        r"$72=x^{2}+100-\dfrac{10x^{2}}3\Rightarrow\dfrac{7x^{2}}3=28\Rightarrow x^{2}=12\Rightarrow x=2\sqrt3$．" "\n"
        r"于是 $\cos\theta=\dfrac{2\sqrt3}6=\dfrac{\sqrt3}3$，$\sin\theta=\sqrt{1-\dfrac13}=\sqrt{\dfrac23}=\dfrac{\sqrt6}3$．" "\n"
        r"**第四步：二倍角与面积**" "\n"
        r"$\sin\angle ACB=\sin2\theta=2\sin\theta\cos\theta=2\cdot\dfrac{\sqrt6}3\cdot\dfrac{\sqrt3}3=\dfrac{2\sqrt2}3$．" "\n"
        r"$S_{\triangle ACB}=\dfrac12\cdot CA\cdot CB\cdot\sin2\theta=\dfrac12\cdot10\cdot6\cdot\dfrac{2\sqrt2}3=20\sqrt2$；" "\n"
        r"$S_{\triangle ACP}=\dfrac12\cdot CA\cdot CP\cdot\sin\theta=\dfrac12\cdot10\cdot2\sqrt3\cdot\dfrac{\sqrt6}3=10\sqrt2$；" "\n"
        r"$S_{\triangle BCP}=\dfrac12\cdot CB\cdot CP\cdot\sin\theta=\dfrac12\cdot6\cdot2\sqrt3\cdot\dfrac{\sqrt6}3=6\sqrt2$．" "\n"
        r"$S_{\triangle ABP}=S_{\triangle ACB}-S_{\triangle ACP}-S_{\triangle BCP}=20\sqrt2-10\sqrt2-6\sqrt2=4\sqrt2$．选 B．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓，由详解「设 $CP=x$，$\angle ACP=\angle BCP=\theta$。则在三角形 $BCP$ 中，" "\n"
        r"$\cos\theta=\frac{BC}{CP}$…$=\frac x6$。在三角形 $ACP$ 中，由余弦定理可知 $AP^{2}=CP^{2}+CA^{2}-2CP\times CA\cos\theta$。" "\n"
        r"代入可得 $(6\sqrt2)^{2}=x^{2}+10^{2}-2x\times10\times\frac x6$，化简可得 $x^{2}=12$，解得 $x=2\sqrt3$…" "\n"
        r"由二倍角公式可得 $\sin\angle ACB=\sin2\theta=2\times\frac{\sqrt3}3\times\frac{\sqrt6}3=\frac{2\sqrt2}3$…" "\n"
        r"$S_{\triangle ACB}=\frac12\times CA\times CB\times\sin2\theta=\frac12\times10\times6\times\frac{2\sqrt2}3=20\sqrt2$…" "\n"
        r"$S_{\triangle ACP}=\frac12\times CA\times CP\times\sin\theta=10\sqrt2$…" "\n"
        r"$S_{\triangle BCP}=\frac12\times CB\times CP\times\sin\theta=6\sqrt2$…" "\n"
        r"则 $S_{\triangle ABP}=S_{\triangle ACB}-S_{\triangle ACP}-S_{\triangle BCP}=20\sqrt2-10\sqrt2-6\sqrt2=4\sqrt2$。故选 B」还原。" "\n"
        r"**独立验算**：" "\n"
        r"① **解 $x$**：$72=x^{2}+100-\frac{10x^{2}}3$ ⟹ $72-100=x^{2}(1-\frac{10}3)=x^{2}(-\frac73)$ ⟹ $-28=-\frac73x^{2}$ ⟹ $x^{2}=12$ ✓" "\n"
        r"$x=2\sqrt3=3.464$ ✓" "\n"
        r"② **$\cos\theta=\frac{2\sqrt3}6=\frac{\sqrt3}3=0.5774$** ⟹ $\theta=54.74^\circ$；$\sin\theta=\frac{\sqrt6}3=0.8165$ ✓" "\n"
        r"验 $\cos^2+\sin^2=\frac13+\frac69=\frac13+\frac23=1$ ✓✓" "\n"
        r"③ **$\sin2\theta=2(0.8165)(0.5774)=0.9428$**；$\frac{2\sqrt2}3=\frac{2(1.4142)}3=0.9428$ ✓✓" "\n"
        r"④ **三个面积**：" "\n"
        r"$S_{ACB}=\frac12(10)(6)(0.9428)=28.28$；$20\sqrt2=28.28$ ✓✓" "\n"
        r"$S_{ACP}=\frac12(10)(3.464)(0.8165)=14.14$；$10\sqrt2=14.14$ ✓✓" "\n"
        r"$S_{BCP}=\frac12(6)(3.464)(0.8165)=8.485$；$6\sqrt2=8.485$ ✓✓" "\n"
        r"⑤ **$S_{ABP}=28.28-14.14-8.485=5.657$**；$4\sqrt2=5.657$ ✓✓✓" "\n"
        r"⑥ **验 $AP=6\sqrt2$**：$AP^{2}=12+100-2(3.464)(10)(0.5774)=112-40=72$ ⟹ $AP=8.485=6\sqrt2$ ✓✓✓" "\n"
        r"⑦ **验 $\angle ACB$ 为钝角**：$\angle ACB=2\theta=109.47^\circ>90^\circ$ ✓✓ **符合题意**" "\n"
        r"⑧ **验 $BP\perp CP$**：$\cos\angle BPC=\frac{CP}{BC}=\frac{3.464}6=0.5774\neq0$…" "\n"
        r"⚠ 注意：由 $BP\perp CP$ 应有 $\cos\theta=\frac{CP}{BC}$ 是**在 $\triangle BCP$ 中 $\angle C=\theta$、斜边 $BC$** 的前提下，" "\n"
        r"即 $\triangle BCP$ 以 $C$ 为顶点、$BC$ 为斜边、直角在 $P$ —— 此时 $\cos\angle BCP=\frac{CP}{BC}$ ✓✓ 成立。" "\n"
        r"**答案 B（$4\sqrt2$）正确** ✓" "\n"
        r"**⭐ 通法（向角平分线作垂线）**：" "\n"
        r"① 向角平分线作垂线 ⟹ 出现**直角三角形**，用 $\frac{\text{邻边}}{\text{斜边}}$ 表出半角的余弦；" "\n"
        r"② 另一个三角形中用余弦定理（已知一条边的长度作方程）解出公共量 $CP$；" "\n"
        r"③ **二倍角** $\sin2\theta=2\sin\theta\cos\theta$ 把半角转成整角；" "\n"
        r"④ ⚠ **本题面积是「割」出来的**：$S_{ABP}=S_{ACB}-S_{ACP}-S_{BCP}$，" "\n"
        r"三个三角形都要算，**别漏掉 $S_{BCP}$**（漏了会得 $10\sqrt2$，不在选项里但很接近会让人怀疑自己）。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-202'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-202-V1',
}

QS = [T202_E1, T202_V1, T202_V2, T202_V3]
