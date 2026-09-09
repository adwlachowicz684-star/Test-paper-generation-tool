# -*- coding: utf-8 -*-
r"""第53批（一）：解三角形 · 最值与范围2（余弦定理型，4 题全录） 来源：2024高中数学热点题型归纳完整解析版.pdf p156（PDF 页 155）M-T-193 ## ★★ 本批的统一套路 四题都是「余弦定理 + 一个约束 ⟹ 一元函数最值」，区别只在**目标式**： | 题 | 约束 | 目标 | 转化关键 | |---|---|---|---| | E1 | $S=\frac18c^{2}$ | $\frac ab+\frac ba$ | 分子 $a^2+b^2=c^2+2ab\cos C$，把 $c^2$ 换成 $4ab\sin C$ | | V1 | $\sin A=2\sin B\sin C$ | $\frac cb+\frac bc$ | 正弦定理平方得 $a^{2}=2bc\sin A$，反解 $b^2+c^2$ | | V2 | $AB=2,\ AC=\sqrt2\,BC$ | 面积 $S$ | 设 $BC=x$，$\cos B=\frac{4-x^{2}}{4x}$，$S^2$ 配方 | | V3 | $c=2,\ \sin A=\sqrt3\sin B$ | 面积 $S$ | $a=\sqrt3b$，$\cos C$ 表成 $b$ 的函数，$S$ 配方 | **共同点**：都把目标式化成 **$p\sin\theta+q\cos\theta$** 或 **$u$ 的二次函数**， 前者用辅助角、后者用配方法。 ## 四题验算（全部独立推导，与答案吻合） | 题 | 我的结果 | 答案 | |---|---|---| | E1 | $4\sin C+2\cos C=2\sqrt5\sin(C+\varphi)$ ⟹ 最大 $2\sqrt5$ | **C** | | V1 | $2(\sin A+\cos A)=2\sqrt2\sin(A+\frac\pi4)$ ⟹ $A=\frac\pi4$ | **B** | | V2 | $S^{2}=\frac{128-(x^{2}-12)^{2}}{16}$，$x=2\sqrt3$ ⟹ $S=2\sqrt2$ | **D** | | V3 | $S=\frac12\sqrt{-b^{4}+8b^{2}-4}$，$b=2$ ⟹ $S=\sqrt3$ | **B** | """

T193_E1 = {
    'type': '选择',
    'stem_text': (
        r"在 $\triangle ABC$ 中，内角 $A,B,C$ 的对边分别为 $a,b,c$，"
        r"若 $\triangle ABC$ 的面积为 $\dfrac18c^{2}$，则 $\dfrac ab+\dfrac ba$ 的最大值为（　　）"
    ),
    'opts': [
        ('A', r"$2$"),
        ('B', r"$4$"),
        ('C', r"$2\sqrt5$"),
        ('D', r"$4\sqrt2$"),
    ],
    'answer': 'C',
    'analysis': (
        r"面积条件给 $c^{2}=4ab\sin C$，余弦定理给 $a^{2}+b^{2}=c^{2}+2ab\cos C$。"
        r"目标式通分后分子正是 $a^{2}+b^{2}$，两式代入即得 $4\sin C+2\cos C$。"
    ),
    'solution': (
        r"**第一步：由面积条件表出 $c^{2}$**" "\n"
        r"$S=\dfrac12 ab\sin C=\dfrac18c^{2}\Rightarrow c^{2}=4ab\sin C$．" "\n"
        r"**第二步：余弦定理表出 $a^{2}+b^{2}$**" "\n"
        r"$c^{2}=a^{2}+b^{2}-2ab\cos C\Rightarrow a^{2}+b^{2}=c^{2}+2ab\cos C$．" "\n"
        r"**第三步：代入目标式**" "\n"
        r"$\dfrac ab+\dfrac ba=\dfrac{a^{2}+b^{2}}{ab}=\dfrac{c^{2}+2ab\cos C}{ab}$" "\n"
        r"$=\dfrac{4ab\sin C+2ab\cos C}{ab}=4\sin C+2\cos C$．" "\n"
        r"**第四步：辅助角**" "\n"
        r"$4\sin C+2\cos C=\sqrt{16+4}\,\sin(C+\varphi)=2\sqrt5\sin(C+\varphi)$（$\tan\varphi=\dfrac12$）．" "\n"
        r"当 $\sin(C+\varphi)=1$ 时取最大值 $2\sqrt5$（此时 $C+\varphi=\frac\pi2$，" "\n"
        r"$C\in(0,\pi)$ 内可取到，因 $\varphi=\arctan\frac12\approx26.6^\circ$ ⟹ $C\approx63.4^\circ$）．选 C．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓，由详解「$S=\frac12 ab\sin C=\frac18c^{2}$，∴ $c^{2}=4ab\sin C$，" "\n"
        r"又 $c^{2}=a^{2}+b^{2}-2ab\cos C$，∴ $a^{2}+b^{2}=c^{2}+2ab\cos C$，" "\n"
        r"∴ $\frac ab+\frac ba=\frac{a^{2}+b^{2}}{ab}=\frac{c^{2}+2ab\cos C}{ab}=\frac{4ab\sin C+2ab\cos C}{ab}=4\sin C+2\cos C$" "\n"
        r"$=2\sqrt5\sin(C+\varphi)$，则 $\frac ab+\frac ba$ 的最大值为 $2\sqrt5$，故选 C」还原，" "\n"
        r"**与我的推导逐字一致** ✓。" "\n"
        r"**独立验算**：" "\n"
        r"① **辅助角振幅**：$\sqrt{4^2+2^2}=\sqrt{20}=2\sqrt5=4.472$ ✓" "\n"
        r"② **构造取等时的三角形反验**：$C\approx63.43^\circ$（$\tan\varphi=\frac12$ ⟹ $\varphi=26.57^\circ$，$C=90^\circ-26.57^\circ=63.43^\circ$）" "\n"
        r"$\sin C=0.8944=\frac2{\sqrt5}$、$\cos C=0.4472=\frac1{\sqrt5}$" "\n"
        r"验 $4\sin C+2\cos C=4(0.8944)+2(0.4472)=3.5777+0.8944=4.472=2\sqrt5$ ✓✓✓" "\n"
        r"③ **验面积条件**（取 $a=b=1$）：$S=\frac12(1)(1)(0.8944)=0.4472$" "\n"
        r"$c^{2}=a^{2}+b^{2}-2ab\cos C=2-2(0.4472)=1.1056$；$\frac18c^{2}=0.1382$" "\n"
        r"⚠ $0.4472\neq0.1382$ —— 说明 **$a=b$ 时不满足面积条件**，" "\n"
        r"必须取特定的 $a:b$。反解：$c^2=4ab\sin C$ 且 $c^2=a^2+b^2-2ab\cos C$ ⟹ " "\n"
        r"$a^{2}+b^{2}=4ab\sin C+2ab\cos C=ab(4\times0.8944+2\times0.4472)=ab(4.472)$" "\n"
        r"设 $t=\frac ab$：$t+\frac1t=4.472$ ⟹ $t^{2}-4.472t+1=0$ ⟹ $t=\frac{4.472\pm\sqrt{20-4}}2=\frac{4.472\pm4}2$" "\n"
        r"$t=4.236$ 或 $t=0.236$（互为倒数 ✓）" "\n"
        r"取 $a=4.236$、$b=1$：$a^{2}+b^{2}=17.944+1=18.944$；$ab(4.472)=4.236(4.472)=18.943$ ✓✓ **闭合**" "\n"
        r"验 $c$：$c^{2}=18.944-2(4.236)(0.4472)=18.944-3.788=15.156$，$c=3.893$" "\n"
        r"验面积：$\frac12(4.236)(1)(0.8944)=1.894$；$\frac18c^{2}=\frac{15.156}8=1.8945$ ✓✓✓ **完全自洽**" "\n"
        r"**答案 C（$2\sqrt5$）正确** ✓" "\n"
        r"**⭐ 通法（$\frac ab+\frac ba$ 型）**：" "\n"
        r"① **通分**：$\frac ab+\frac ba=\frac{a^{2}+b^{2}}{ab}$，分子是平方和 —— 立刻想到余弦定理；" "\n"
        r"② 用 $a^{2}+b^{2}=c^{2}+2ab\cos C$ 把分子换成 $c^{2}$，再用题设把 $c^{2}$ 换成 $ab$ 的倍数；" "\n"
        r"③ ⚠ **$ab$ 必须能约掉** —— 这是题目设计的必然结果，" "\n"
        r"如果约不掉，说明前两步走错了（或遗漏了某个条件）。"
    ),
    'difficulty': 0.87,
    'topics': ['M-T-193'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-193-E1',
}

T193_V1 = {
    'type': '选择',
    'stem_text': (
        r"在 $\triangle ABC$ 中，内角 $A,B,C$ 所对的边分别为 $a,b,c$，且 $\sin A=2\sin B\sin C$，"
        r"则 $\dfrac cb+\dfrac bc$ 取得最大值时，内角 $A$ 的值为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac\pi6$"),
        ('B', r"$\dfrac\pi4$"),
        ('C', r"$\dfrac\pi3$"),
        ('D', r"$\dfrac\pi2$"),
    ],
    'answer': 'B',
    'analysis': (
        r"把 $\sin A=2\sin B\sin C$ **平方处理**，用正弦定理换成 $a^{2}=2bc\sin A$；"
        r"再由余弦定理反解 $b^{2}+c^{2}=2bc(\cos A+\sin A)$，代入目标式即得 $2(\sin A+\cos A)$。"
    ),
    'solution': (
        r"**第一步：平方 + 正弦定理**" "\n"
        r"由 $\sin A=2\sin B\sin C$ 及正弦定理 $\dfrac a{\sin A}=\dfrac b{\sin B}=\dfrac c{\sin C}=2R$：" "\n"
        r"$\dfrac{a^{2}}{\sin^{2}A}=\dfrac{bc}{\sin B\sin C}=\dfrac{bc}{\sin A/2}=\dfrac{2bc}{\sin A}$" "\n"
        r"$\Rightarrow a^{2}=2bc\sin A$．" "\n"
        r"**第二步：余弦定理反解 $b^{2}+c^{2}$**" "\n"
        r"$\cos A=\dfrac{b^{2}+c^{2}-a^{2}}{2bc}\Rightarrow b^{2}+c^{2}=2bc\cos A+a^{2}=2bc(\cos A+\sin A)$．" "\n"
        r"**第三步：代入目标式**" "\n"
        r"$\dfrac cb+\dfrac bc=\dfrac{b^{2}+c^{2}}{bc}=\dfrac{2bc(\cos A+\sin A)}{bc}=2(\sin A+\cos A)$" "\n"
        r"$=2\sqrt2\sin\left(A+\dfrac\pi4\right)$．" "\n"
        r"当 $A+\dfrac\pi4=\dfrac\pi2$，即 $A=\dfrac\pi4$ 时取最大值 $2\sqrt2$．选 B．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓，由详解「由 $\sin A=2\sin B\sin C$，根据正弦定理，" "\n"
        r"$\frac{a^{2}}{\sin^{2}A}=\frac{bc}{\sin B\sin C}$，可得 $a^{2}=2bc\sin A$，再由 $\cos A=\frac{b^{2}+c^{2}-a^{2}}{2bc}$，" "\n"
        r"得 $b^{2}+c^{2}=2bc(\cos A+\sin A)$，所以 $\frac cb+\frac bc=\frac{b^{2}+c^{2}}{bc}=\frac{2bc(\cos A+\sin A)}{bc}$" "\n"
        r"$=2(\sin A+\cos A)=2\sqrt2\sin(A+\frac\pi4)$，所以当 $A=\frac\pi4$ 时，$\frac cb+\frac bc$ 取得最大值 $2\sqrt2$，" "\n"
        r"答案为 B」还原，**与我的推导完全一致** ✓。" "\n"
        r"**独立验算**：" "\n"
        r"① **$a^{2}=2bc\sin A$ 的推法核对**：" "\n"
        r"$\sin B=\frac b{2R}$、$\sin C=\frac c{2R}$、$\sin A=\frac a{2R}$" "\n"
        r"代入 $\sin A=2\sin B\sin C$：$\frac a{2R}=2\cdot\frac b{2R}\cdot\frac c{2R}=\frac{bc}{2R^{2}}$ ⟹ $a=\frac{bc}R$" "\n"
        r"另一路径：$a^{2}=2bc\sin A=2bc\cdot\frac a{2R}=\frac{abc}R$ ⟹ $a=\frac{bc}R$ ✓✓ **两法一致**" "\n"
        r"② **取 $A=\frac\pi4$ 构造三角形反验**：" "\n"
        r"$\sin A=\frac{\sqrt2}2=0.7071$。由 $a=\frac{bc}R$ 且 $a=2R\sin A=2R(0.7071)=1.4142R$" "\n"
        r"⟹ $\frac{bc}R=1.4142R$ ⟹ $bc=1.4142R^{2}$" "\n"
        r"取 $R=1$：$a=1.4142$、$bc=1.4142$；再取 $b=1$ ⟹ $c=1.4142$" "\n"
        r"验 $A$：$\cos A=\frac{b^{2}+c^{2}-a^{2}}{2bc}=\frac{1+2-2}{2(1.4142)}=\frac1{2.8284}=0.3536$" "\n"
        r"⚠ $\arccos(0.3536)=69.3^\circ\neq45^\circ$ —— 说明 $b=1,c=1.4142$ 这组不是解。" "\n"
        r"**反解正确的 $b,c$**：需同时满足 $bc=1.4142R^{2}$ 与 $\cos A=\frac{\sqrt2}2$：" "\n"
        r"$b^{2}+c^{2}=2bc\cos A+a^{2}=2(1.4142)(0.7071)+2=2+2=4$（取 $R=1$，$a^{2}=2$）" "\n"
        r"⟹ $b^{2}+c^{2}=4$、$bc=1.4142$ ⟹ $(b+c)^{2}=4+2.828=6.828$ ⟹ $b+c=2.613$" "\n"
        r"$t^{2}-2.613t+1.4142=0$，判别式 $=6.828-5.657=1.171$ ⟹ $t=\frac{2.613\pm1.082}2$" "\n"
        r"$b=1.848$、$c=0.766$（或互换）" "\n"
        r"验 $a$：$a^{2}=2bc\sin A=2(1.4142)(0.7071)=2$ ⟹ $a=1.4142$ ✓" "\n"
        r"验 $\cos A$：$\frac{1.848^{2}+0.766^{2}-2}{2(1.848)(0.766)}=\frac{3.415+0.587-2}{2.831}=\frac{2.002}{2.831}=0.7072$ ✓✓ **$A=45^\circ$**" "\n"
        r"验目标式：$\frac cb+\frac bc=\frac{0.766}{1.848}+\frac{1.848}{0.766}=0.4145+2.4125=2.827\approx2\sqrt2=2.828$ ✓✓✓" "\n"
        r"**答案 B（$\frac\pi4$）正确** ✓" "\n"
        r"**⭐ 通法（$\sin A=2\sin B\sin C$ 型）**：" "\n"
        r"① **正弦定理平方处理**：$\frac{a^{2}}{\sin^{2}A}=\frac{bc}{\sin B\sin C}$，" "\n"
        r"把两个 $\sin$ 的乘积整体换成边，得到 $a^{2}=2bc\sin A$；" "\n"
        r"② 由余弦定理**反解平方和**：$b^{2}+c^{2}=a^{2}+2bc\cos A$；" "\n"
        r"③ 目标式 $\frac cb+\frac bc=\frac{b^{2}+c^{2}}{bc}$ 正好用上平方和 ⟹ $bc$ 约掉。" "\n"
        r"**⚠ 关键**：这类题 $b,c$ 的**具体值不重要**（会被约掉），" "\n"
        r"所以不要试图解出 $b,c$ —— 只要确认存在性即可（本题我验证了确实存在）。"
    ),
    'difficulty': 0.89,
    'topics': ['M-T-193'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-193-V1',
}

T193_V2 = {
    'type': '选择',
    'stem_text': (
        r"满足条件 $AB=2$，$AC=\sqrt2\,BC$ 的三角形 $ABC$ 的面积的最大值是（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac{3\sqrt2}2$"),
        ('B', r"$4$"),
        ('C', r"$2$"),
        ('D', r"$2\sqrt2$"),
    ],
    'answer': 'D',
    'analysis': (
        r"设 $BC=x$（则 $AC=\sqrt2\,x$），用余弦定理把 $\cos B$ 表成 $x$ 的函数，"
        r"再由 $S=\frac12\cdot AB\cdot BC\cdot\sin B$ 得 $S^{2}$ 关于 $x^{2}$ 的二次函数，配方法取最大。"
        r"⚠ 最后要**用三边关系检验**取等时的 $x$ 是否合法。"
    ),
    'solution': (
        r"**第一步：设元**" "\n"
        r"设 $BC=x>0$，则 $AC=\sqrt2\,x$，$AB=2$．" "\n"
        r"**第二步：余弦定理表出 $\cos B$**" "\n"
        r"$\cos B=\dfrac{AB^{2}+BC^{2}-AC^{2}}{2\cdot AB\cdot BC}=\dfrac{4+x^{2}-2x^{2}}{2\cdot2\cdot x}=\dfrac{4-x^{2}}{4x}$．" "\n"
        r"**第三步：$S^{2}$ 配方**" "\n"
        r"$S=\dfrac12\cdot AB\cdot BC\cdot\sin B=\dfrac12\cdot2\cdot x\sin B=x\sin B$．" "\n"
        r"$S^{2}=x^{2}(1-\cos^{2}B)=x^{2}-x^{2}\cdot\dfrac{(4-x^{2})^{2}}{16x^{2}}=x^{2}-\dfrac{(4-x^{2})^{2}}{16}$" "\n"
        r"$=\dfrac{16x^{2}-(16-8x^{2}+x^{4})}{16}=\dfrac{-x^{4}+24x^{2}-16}{16}=\dfrac{128-(x^{2}-12)^{2}}{16}$．" "\n"
        r"当 $x^{2}=12$（即 $x=2\sqrt3$）时，$S^{2}_{\max}=\dfrac{128}{16}=8$，$S_{\max}=2\sqrt2$．" "\n"
        r"**第四步：三边关系检验**" "\n"
        r"$\begin{cases}x+2>\sqrt2\,x\\ \sqrt2\,x+x>2\end{cases}\Rightarrow \begin{cases}2>(\sqrt2-1)x\\ (\sqrt2+1)x>2\end{cases}\Rightarrow 2(\sqrt2-1)<x<2(\sqrt2+1)$" "\n"
        r"即 $0.828<x<4.828$。而 $x=2\sqrt3\approx3.464$ **落在区间内** ✓ 合法。选 D．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓，由详解「设 $BC=x$，则 $AC=\sqrt2x$，" "\n"
        r"根据余弦定理得 $\cos B=\frac{AB^{2}+BC^{2}-AC^{2}}{2\cdot AB\cdot BC}=\frac{4+x^{2}-(\sqrt2x)^{2}}{4x}=\frac{4-x^{2}}{4x}$，" "\n"
        r"代入上式，得 $S_{\triangle ABC}=\frac12 AB\cdot BC\sin B=\frac12\cdot2x\cdot\sqrt{1-(\frac{4-x^{2}}{4x})^{2}}$" "\n"
        r"$=\frac{\sqrt{128-(x^{2}-12)^{2}}}{16}$…由三角形的三边关系可得…解得 $2\sqrt2-2<x<2\sqrt2+2$，" "\n"
        r"故当 $x=2\sqrt3$ 时，$S_{\triangle ABC}$ 取得最大值，故选 D」还原，**与我的推导一致** ✓。" "\n"
        r"**独立验算**：" "\n"
        r"① **配方核对**：$-(x^{2}-12)^{2}+128=-(x^{4}-24x^{2}+144)+128=-x^{4}+24x^{2}-16$ ✓✓" "\n"
        r"② **$S^{2}_{\max}$**：$x^{2}=12$ 时 $S^{2}=\frac{128}{16}=8$ ⟹ $S=2\sqrt2=2.828$ ✓✓" "\n"
        r"③ **构造取等时的三角形反验**：$x=2\sqrt3=3.464$、$AC=\sqrt2(3.464)=4.899$、$AB=2$" "\n"
        r"三边关系：$2+3.464=5.464>4.899$ ✓；$2+4.899=6.899>3.464$ ✓；$3.464+4.899=8.363>2$ ✓" "\n"
        r"$\cos B=\frac{4-12}{4(3.464)}=\frac{-8}{13.856}=-0.5774$ ⟹ $\sin B=\sqrt{1-\frac13}=0.8165$" "\n"
        r"$S=\frac12(2)(3.464)(0.8165)=2.828$ ✓✓✓ **$=2\sqrt2$**" "\n"
        r"④ **确认是最大值**（取 $x=3$ 和 $x=4$ 对比）：" "\n"
        r"$x=3$：$\cos B=\frac{4-9}{12}=-0.4167$、$\sin B=0.9091$、$S=3(0.9091)=2.727<2.828$ ✓" "\n"
        r"$x=4$：$\cos B=\frac{4-16}{16}=-0.75$、$\sin B=0.6614$、$S=4(0.6614)=2.646<2.828$ ✓✓ **确为最大**" "\n"
        r"⑤ **区间检验**：$2(\sqrt2-1)=0.828<3.464<4.828=2(\sqrt2+1)$ ✓✓" "\n"
        r"**答案 D（$2\sqrt2$）正确** ✓" "\n"
        r"**⭐ 通法（两边成比例的三角形面积最值）**：" "\n"
        r"① **设短的那份为 $x$**，把所有边用 $x$ 表示；" "\n"
        r"② 选**已知两边的夹角**（本题 $\angle B$ 夹在 $AB$ 与 $BC$ 之间，两者都含 $x$ 或为常数）用余弦定理；" "\n"
        r"③ $S=\frac12\cdot(\text{两边})\cdot\sin$ ⟹ **算 $S^{2}$ 避开根号** ⟹ 配方取最值；" "\n"
        r"④ ⚠ **必须检验三边关系** —— 本题取等点 $x=2\sqrt3$ 在区间内，但若取等点落在区间外，" "\n"
        r"最大值就要改在边界附近取（或不存在最大值）。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-193'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-193-V2',
}

T193_V3 = {
    'type': '选择',
    'stem_text': (
        r"在 $\triangle ABC$ 中，角 $A,B,C$ 所对的边分别为 $a,b,c$，$c=2$，$\sin A=\sqrt3\sin B$，"
        r"则 $\triangle ABC$ 的最大面积为（　　）"
    ),
    'opts': [
        ('A', r"$\sqrt3$"),
        ('B', r"$\sqrt3$"),
        ('C', r"$2$"),
        ('D', r"无法确定"),
    ],
    'answer': 'B',
    'analysis': (
        r"由正弦定理 $a=\sqrt3\,b$；余弦定理把 $\cos C$ 表成 $b$ 的函数，"
        r"$\sin C=\sqrt{1-\cos^{2}C}$，代入 $S=\frac12 ab\sin C$ 后**根号内是 $b^{2}$ 的二次函数**，配方法取最大。"
    ),
    'solution': (
        r"**第一步：边化**" "\n"
        r"由 $\sin A=\sqrt3\sin B$ 及正弦定理：$a=\sqrt3\,b$．" "\n"
        r"**第二步：$\cos C$ 表成 $b$ 的函数**" "\n"
        r"$\cos C=\dfrac{a^{2}+b^{2}-c^{2}}{2ab}=\dfrac{3b^{2}+b^{2}-4}{2\cdot\sqrt3 b\cdot b}=\dfrac{4b^{2}-4}{2\sqrt3\,b^{2}}=\dfrac{2b^{2}-2}{\sqrt3\,b^{2}}$．" "\n"
        r"**第三步：$\sin C$**" "\n"
        r"$\sin^{2}C=1-\cos^{2}C=1-\dfrac{4(b^{2}-1)^{2}}{3b^{4}}=\dfrac{3b^{4}-4(b^{4}-2b^{2}+1)}{3b^{4}}=\dfrac{-b^{4}+8b^{2}-4}{3b^{4}}$．" "\n"
        r"$\sin C=\dfrac{\sqrt{-b^{4}+8b^{2}-4}}{\sqrt3\,b^{2}}$．" "\n"
        r"**第四步：面积配方**" "\n"
        r"$S=\dfrac12 ab\sin C=\dfrac12\cdot\sqrt3 b\cdot b\cdot\dfrac{\sqrt{-b^{4}+8b^{2}-4}}{\sqrt3\,b^{2}} =\dfrac12\sqrt{-b^{4}+8b^{2}-4}$" "\n"
        r"$=\dfrac12\sqrt{-(b^{2}-4)^{2}+12}$．" "\n"
        r"当 $b^{2}=4$（即 $b=2$）时，$S_{\max}=\dfrac12\sqrt{12}=\sqrt3$．选 B．"
    ),
    'review': (
        r"★ 题干、答案完整 ✓，由详解「∵ $\sin A=\sqrt3\sin B$，∴ $a=\sqrt3b$，由余弦定理及 $c=2$ 得，" "\n"
        r"$\cos C=\frac{a^{2}+b^{2}-c^{2}}{2ab}=\frac{a^{2}+b^{2}-4}{2ab}$…" "\n"
        r"$S_{\triangle ABC}=\frac12 ab\sin C=\frac12\sqrt{-b^{4}+8b^{2}-4}$…当 $b^{2}=4$ 时，即 $b=2$，" "\n"
        r"$\triangle ABC$ 的面积 $S$ 有最大值，∴ $\triangle ABC$ 的最大面积是 $\frac12\times\sqrt{12}=\sqrt3$，故选 B」还原。" "\n"
        r"**⚠ 选项录入说明**：ref_bank 存的选项 A 与 B 都是 `3`（根号丢失后同形）。" "\n"
        r"按原书排版应为 A $\sqrt3$、B $\sqrt3$ 中一个是 $\frac{3\sqrt2}2$ 之类的干扰项，" "\n"
        r"但因提取丢失无法判定，**按可识别形式录入，以答案 B $=\sqrt3$ 为准**。" "\n"
        r"（推导与验算都确认最大值确为 $\sqrt3$，这一点无争议。）" "\n"
        r"**独立验算**：" "\n"
        r"① **配方核对**：$-(b^{2}-4)^{2}+12=-(b^{4}-8b^{2}+16)+12=-b^{4}+8b^{2}-4$ ✓✓" "\n"
        r"② **$S_{\max}$**：$b^{2}=4$ 时 $S=\frac12\sqrt{12}=\frac12(3.464)=1.732=\sqrt3$ ✓✓" "\n"
        r"③ **构造取等时的三角形反验**：$b=2$、$a=\sqrt3(2)=3.464$、$c=2$" "\n"
        r"三边关系：$2+2=4>3.464$ ✓；$2+3.464>2$ ✓ ✓" "\n"
        r"$\cos C=\frac{12+4-4}{2(3.464)(2)}=\frac{12}{13.856}=0.8661$ ⟹ $C=30^\circ$ ✓" "\n"
        r"$\sin C=0.5$" "\n"
        r"$S=\frac12(3.464)(2)(0.5)=1.732$ ✓✓✓ **$=\sqrt3$**" "\n"
        r"④ **验 $a=\sqrt3b$ 与 $c=2$ 相容**：由 $\cos C=\frac{2b^{2}-2}{\sqrt3b^{2}}$，$b=2$ ⟹ $\frac{8-2}{\sqrt3\cdot4}=\frac6{6.928}=0.866$ ✓✓" "\n"
        r"⑤ **确认是最大值**（取 $b=1.5$ 和 $b=3$ 对比）：" "\n"
        r"$b=1.5$：$S=\frac12\sqrt{-5.0625+18-4}=\frac12\sqrt{8.9375}=\frac12(2.990)=1.495<1.732$ ✓" "\n"
        r"$b=3$：$S=\frac12\sqrt{-81+72-4}=\frac12\sqrt{-13}$ ✗ **无意义**（说明 $b$ 有范围限制）" "\n"
        r"$b$ 的合法范围：$-b^{4}+8b^{2}-4\ge0$ ⟹ $b^{2}\in[4-2\sqrt3,4+2\sqrt3]=[0.536,7.464]$ ⟹ $b\in[0.732,2.732]$" "\n"
        r"结合三边关系 $a+c>b$（恒成立）、$b+c>a$ ⟹ $b+2>\sqrt3b$ ⟹ $b<\frac2{\sqrt3-1}=2.732$ ✓ **恰好一致**" "\n"
        r"$a+b>c$ ⟹ $\sqrt3b+b>2$ ⟹ $b>\frac2{\sqrt3+1}=0.732$ ✓✓ **完全吻合**" "\n"
        r"**答案 B（$\sqrt3$）正确** ✓" "\n"
        r"**⭐ 通法（已知一边 + 两边比例的面积最值）**：" "\n"
        r"① 正弦定理把比例转成边的关系（$a=kb$）；" "\n"
        r"② 余弦定理把**已知边的对角**的余弦表成 $b$ 的函数 —— " "\n"
        r"注意**选哪条边作「已知边」很关键**：本题 $c=2$ 已知，所以表 $\cos C$，" "\n"
        r"分子的 $c^{2}=4$ 是常数，化简才干净；" "\n"
        r"③ ⚠ **$\sin C$ 的分母 $b^{2}$ 会与面积式中的 $b^{2}$ 约掉** —— 看到这个约分就对了；" "\n"
        r"④ 根号内是 $b^{2}$ 的二次函数，配方法取最大，" "\n"
        r"**取等点要用三边关系检验**（本题 $b=2$ 恰好在合法区间内 ✓）。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-193'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-193-V3',
}

QS = [T193_E1, T193_V1, T193_V2, T193_V3]
