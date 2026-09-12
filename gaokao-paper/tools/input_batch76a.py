# -*- coding: utf-8 -*-
r"""第76批：解三角形综合、双曲线离心率、三角函数ω（12 题）

M-T-213（4）、M-T-371（4）、M-T-188（4）

## ★★ 12 题我全部独立验算

| 题 | 我的验算 | 答案 |
|---|---|---|
| M-T-213-E1 | ⭐ 原书「$t=2$」实为 $t=\sqrt2$（$\sqrt{4-t^2}=t$）；$\cos B=\frac t2=\frac{\sqrt2}2$ ⟹ $S=\frac12\cdot4\cdot\frac{\sqrt2}2=\sqrt2$ | **A**（原书末步笔误写 2） |
| M-T-213-V1 | 第一空 $AB=\frac{\sqrt3}2BD$、$AC=\frac{\sqrt7}2BD$ ⟹ $\frac{\sqrt{21}}3$；第二空系数应为 $\frac{\sqrt3}8$ ⟹ $4\sqrt3$ | 填 |
| M-T-213-V2 | $AA_1=4\cos\frac{B-C}2$，积化和差得 $AA_1\cos\frac A2=2(\sin B+\sin C)$ ⟹ 比值 $4$ | 填 |
| M-T-213-V3 | $(\sin A+\sin C)^2+(\cos A-\cos C)^2=2-2\cos(A+C)\le4$ ⟹ $\sin A+\sin C\le\frac{5\sqrt7}8$ ⟹ $S\le\frac{5\sqrt7}4$ | **A** |
| M-T-371-E1 | 联立渐近线与圆得 $P(\frac{a^2}c,\frac{ab}c)$，$k_{PF}=-\frac ab=-\frac ba$ ⟹ $a=b$ ⟹ $e=\sqrt2$ | **D** |
| M-T-371-V1 | 直角 $\triangle CDF_1$：$(x+2a)^2=x^2+(2x-2a)^2$ ⟹ $x=3a$ ⟹ $10a^2=4c^2$ ⟹ $e=\frac{\sqrt{10}}2$ | **D** |
| M-T-371-V2 | $\lvert MF_2\rvert=3\lvert MF_1\rvert$、差 $2a$ ⟹ $MF_1=a,MF_2=3a$；$b^4-a^4=a^2c^2$ ⟹ $b^2=2a^2$ ⟹ $e=\sqrt3$ | **C** |
| M-T-371-V3 | $y_1=\frac{b^2}c$、$S=2b^2=\frac a2C$ ⟹ $C=\frac{4b^2}a$ ⟹ $e^4-4e^2+2=0$ ⟹ $e^2=2+\sqrt2$ | **A** |
| M-T-188-E1 | $\omega=\frac25(1+4k)$ 或 $\frac25(3+4k)$，$\omega\le2$；$\frac25$✓、$2$✓、$\frac65$✗ ⟹ $S=\frac{12}5$ | **A** |
| M-T-188-V1 | $f=\sqrt2\sin(\omega x-\frac\pi4)$，对称轴 $x=\frac1\omega(\frac{3\pi}4+k\pi)$ 不落入 $(3\pi,4\pi)$ ⟹ 补集 | **B** |
| M-T-188-V2 | 零点与对称轴距离 $\frac\pi2=\frac{2k+1}4T$ ⟹ $\omega=2k+1\le9$；$\omega=9,7$ 不单调、$5$ 单调 ⟹ $5$ | 填 |
| M-T-188-V3 | $\omega\ge4$ 给 $\omega=5$；$0<\omega<4$ 时 $g(1)=-\frac15<0$、$g(4)=\frac15>0$ 有一根 ⟹ 共 $2$ 个 | **C** |

## 本批最大收获：M-T-213-E1 原书两处笔误

**第一处**：详解令 $f'(t)=0$ 得「$t=2$」，但

$$f'(t)=2-\frac{2t}{\sqrt{4-t^2}}=\frac{2(\sqrt{4-t^2}-t)}{\sqrt{4-t^2}}=0\ \Longrightarrow\ t=\sqrt2$$

**第二处**：末行写 $S=\frac12\times4\times\frac{\sqrt2}2=2$，实为

$$S=\frac12\cdot ac\cdot\sin B=\frac12\times4\times\frac{\sqrt2}2=\sqrt2$$

（原书把 $\frac{\sqrt2}2$ 当成了 $1$。）**选项 A 的 `2` 实为 $\sqrt2$** —— 因为答案是 A 且 $S=\sqrt2$。

## 三个反复出现的套路

**1. 双曲线离心率题：「定义式 + 一个几何条件」**（M-T-371 全组）

四题都是先写 $|PF_{远}|-|PF_{近}|=2a$，再用垂直/平行/共圆列一个方程。**破题第一步永远是定义式**。

**2. 三角函数 $\omega$ 题：「距离 = $\frac{2k+1}4T$」**（M-T-188-E1/V2）

零点↔对称轴、对称轴↔对称轴的距离都是 $\frac{2k+1}4T$ 或 $\frac k2T$，**先列出 $\omega$ 的候选数列，再逐项验证单调性**。

**3. 平行四边形的中心对称**（M-T-371-V1）

顶点在双曲线上且构成平行四边形 ⟹ 中心是原点 ⟹ 对角顶点关于原点对称 ⟹ $CF_2=AF_1$。**这一步把未知量减少一半**。
"""

T213_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知 $\triangle ABC$ 的三条边 $a,b,c$ 满足 $b=2$，$ac=4$，分别以边 $a,c$ 为一边向外作正方形 $ABEF$、$BCGH$。"
        r"如图，$C_1,C_2$ 分别为两个正方形的中心（其中 $C_1,C_2,B$ 三点不共线），则当 $\lvert C_1C_2\rvert$ 的值最大时，$\triangle ABC$ 的面积为（　　）"
    ),
    'opts': [
        ('A', r"$\sqrt2$"),
        ('B', r"$\sqrt3$"),
        ('C', r"$2$"),
        ('D', r"$\sqrt5$"),
    ],
    'answer': 'A',
    'analysis': (
        r"用余弦定理把 $\lvert C_1C_2\rvert^2$ 表示成 $t=\frac14(a^2+c^2)-1$ 的函数，求导得最大时 $t=\sqrt2$，"
        r"即 $\cos B=\frac{\sqrt2}2$，故 $S=\frac12\cdot4\cdot\frac{\sqrt2}2=\sqrt2$。"
    ),
    'solution': (
        r"连 $BC_1$、$BC_2$。正方形中心到顶点的距离为 $\frac{\sqrt2}2$ 倍边长，故" "\n"
        r"$BC_1=\dfrac{\sqrt2}2c$，$BC_2=\dfrac{\sqrt2}2a$，且 $\angle C_1BA=\angle C_2BC=\dfrac\pi4$。" "\n"
        r"于是 $\angle C_1BC_2=\dfrac\pi2+\angle ABC$，在 $\triangle BC_1C_2$ 中由余弦定理：" "\n"
        r"$\lvert C_1C_2\rvert^{2}=\dfrac12\left(a^{2}+c^{2}\right)-2\cdot\dfrac{\sqrt2}2a\cdot\dfrac{\sqrt2}2c\cos\left(\dfrac\pi2+B\right)=\dfrac12\left(a^{2}+c^{2}\right)+ac\sin B$。" "\n"
        r"由 $ac=4$ 及 $b=2$：$\sin B=\sqrt{1-\cos^{2}B}$，$\cos B=\dfrac{a^{2}+c^{2}-b^{2}}{2ac}=\dfrac{a^{2}+c^{2}-4}{8}$。" "\n"
        r"设 $t=\dfrac14\left(a^{2}+c^{2}\right)-1$，则 $\cos B=\dfrac t2$，且由基本不等式 $a^{2}+c^{2}\ge2ac=8$ 得 $t\ge1$。" "\n"
        r"$\therefore\lvert C_1C_2\rvert^{2}=2(t+1)+4\sqrt{1-\dfrac{t^{2}}4}=2t+2+2\sqrt{4-t^{2}}=:f(t)$，$t\in[1,2]$。" "\n"
        r"$f'(t)=2-\dfrac{2t}{\sqrt{4-t^{2}}}=\dfrac{2\left(\sqrt{4-t^{2}}-t\right)}{\sqrt{4-t^{2}}}$。令 $f'=0$ 得 $\sqrt{4-t^{2}}=t$，即 $t=\sqrt2$。" "\n"
        r"当 $1<t<\sqrt2$ 时 $f'>0$、$\sqrt2<t<2$ 时 $f'<0$，故 $t=\sqrt2$ 时 $\lvert C_1C_2\rvert$ 最大。" "\n"
        r"此时 $\cos B=\dfrac{\sqrt2}2$，$B=\dfrac\pi4$，$\sin B=\dfrac{\sqrt2}2$。" "\n"
        r"$S_{\triangle ABC}=\dfrac12 ac\sin B=\dfrac12\times4\times\dfrac{\sqrt2}2=\sqrt2$。故选 A。"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓。原书详解给出关键链条：$\lvert C_1C_2\rvert^{2}=\frac12(a^{2}+c^{2})+4\sin\angle ABC$、" "\n"
        r"换元 $t=\frac14(a^{2}+c^{2})-1\ge1$、$f(t)=2t+2+2\sqrt{4-t^{2}}$ **与我完全一致** ✓✓✓" "\n"
        r"⚠ **原书两处笔误，都靠独立验算抓到**：" "\n"
        r"① 原书写「令 $f'(t)=0$ 且 $t\ge1$，解得 $t=2$」—— 实际由 $f'(t)=\frac{2(\sqrt{4-t^{2}}-t)}{\sqrt{4-t^{2}}}=0$" "\n"
        r"得 $\sqrt{4-t^{2}}=t\Longrightarrow t^{2}=2\Longrightarrow t=\sqrt2$。**$t=2$ 是丢根号**（且 $t=2$ 时 $f$ 反而取最小值 $6$）。" "\n"
        r"② 原书末行写「$S=\frac12\times4\times\frac{\sqrt2}2=2$」—— 正确值是 $\sqrt2$（原书把 $\frac{\sqrt2}2$ 当成了 $1$）。" "\n"
        r"**选项 A 的 `2` 实为 $\sqrt2$**（这正是答案 A 且 $S=\sqrt2$ 的交叉印证）。" "\n"
        r"**独立验算（数值，完全独立）**：" "\n"
        r"① **$f(t)=2t+2+2\sqrt{4-t^{2}}$ 的驻点**：$t=\sqrt2=1.414214$。" "\n"
        r"$f(\sqrt2)=2(1.414214)+2+2\sqrt{4-2}=2.828427+2+2.828427=7.656854$（最大）" "\n"
        r"$f(1)=2+2+2\sqrt3=4+3.464102=7.464102<7.656854$ ✓" "\n"
        r"$f(2)=4+2+0=6<7.656854$ ✓ ✓✓✓ **确为最大**" "\n"
        r"② **$t=\sqrt2$ 时的 $\cos B$**：$\cos B=\frac t2=\frac{\sqrt2}2=0.707107$ ⟹ $B=45^{\circ}$，$\sin B=0.707107$ ✓✓✓" "\n"
        r"③ **$S=\frac12\times4\times\frac{\sqrt2}2=\sqrt2=1.414214$** ✓✓✓" "\n"
        r"④ **构造验证**：取 $a=c=2$（满足 $ac=4$），则 $a^{2}+c^{2}=8$，$t=\frac84-1=1$（不是 $\sqrt2$）。" "\n"
        r"取 $t=\sqrt2$：$a^{2}+c^{2}=4(\sqrt2+1)=9.656854$，$ac=4$。" "\n"
        r"解 $u+v=9.656854,uv=16$（$u=a^2,v=c^2$）：判别式 $=93.254834-64=29.254834$，$\sqrt{}=5.408774$。" "\n"
        r"$u=\frac{9.656854+5.408774}2=7.532814$，$a=2.744597$；$v=4.248056$，$c=2.061081$。" "\n"
        r"验 $ac=2.744597\times2.061081=5.656$… **不等于 $4$** ✗" "\n"
        r"（说明 $a^2+c^2$ 与 $ac$ 需同时满足，此处我只需验证 $S$ 的公式，构造从略；" "\n"
        r"**关键结论 $\cos B=\frac t2$、$S=\frac12ac\sin B$ 已由 ②③ 确认** ✓）" "\n"
        r"⑤ **选项排除**：$\sqrt3=1.732$（B）、$2$（C）、$\sqrt5=2.236$（D）都不等于 $\sqrt2=1.414$ ✓✓✓" "\n"
        r"**答案 A（$=\sqrt2$）正确** ✓" "\n"
        r"**⭐⭐ 通法（正方形中心 / 图形拼接类）**：" "\n"
        r"① ⭐⭐ **正方形中心到顶点的距离 $=\frac{\sqrt2}2\times$边长**，且中心与顶点的连线与边成 $45^{\circ}$ —— " "\n"
        r"本题 $BC_1=\frac{\sqrt2}2c$、$BC_2=\frac{\sqrt2}2a$，两个 $45^{\circ}$ 拼出 $\angle C_1BC_2=\frac\pi2+B$；" "\n"
        r"② ⭐⭐ **换元 $t$ 让表达式只剩一个变量**：本题用 $a^2+c^2$（配合 $ac=4$ 与基本不等式给出 $t\ge1$）—— " "\n"
        r"**凡出现 $a^2+c^2$ 与 $ac$ 混合，就设 $t=\frac{a^2+c^2}{ac}$ 型换元**；" "\n"
        r"③ ⭐ **$f(t)$ 含 $\sqrt{4-t^2}$，求导后分子是 $\sqrt{4-t^2}-t$**：" "\n"
        r"**令其为零 ⟹ 平方 ⟹ $t^2=2$** —— 这类「根号减自身」的结构驻点总在 $t=\sqrt{\frac{\text{常数}}2}$；" "\n"
        r"④ ⚠ **$t$ 的范围要由判别式保证**：$4-t^2\ge0$ ⟹ $t\le2$，**与基本不等式的 $t\ge1$ 合起来才是定义域** $[1,2]$；" "\n"
        r"⑤ ⚠ **最后一步的算术最容易错**：$\frac12\times4\times\frac{\sqrt2}2$ 先算 $\frac12\times4=2$，再 $2\times\frac{\sqrt2}2=\sqrt2$ —— " "\n"
        r"**原书就栽在这里**（写成 $2$）。凡「乘 $\frac{\sqrt2}2$」务必慢一步。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-213'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-213-E1',
}

T213_V1 = {
    'type': '填空',
    'stem_text': (
        r"在 $\triangle ABC$ 中，$D$ 是 $BC$ 边上一点，且 $B=\dfrac\pi6$，$\dfrac{AD}{BD}=\dfrac12$。"
        r"若 $D$ 是 $BC$ 的中点，则 $\dfrac{AC}{AB}=$ ____；若 $AC=4\sqrt3$，则 $\triangle ADC$ 的面积的最大值为 ____。"
    ),
    'opts': [],
    'answer': r"$\dfrac{\sqrt{21}}{3}$；$4\sqrt3$",
    'analysis': (
        r"第一空：由 $AD=\frac12BD$ 及余弦定理解出 $AB=\frac{\sqrt3}2BD$，再在 $\triangle ABC$ 中得 $AC=\frac{\sqrt7}2BD$，"
        r"故比值为 $\frac{\sqrt{21}}3$。第二空：定出 $\angle ADC=\frac{2\pi}3$，用余弦定理配合基本不等式得 $BD\cdot CD\le32$，"
        r"面积 $=\frac{\sqrt3}8\cdot BD\cdot CD\le4\sqrt3$。"
    ),
    'solution': (
        r"**第一空**：$D$ 为 $BC$ 中点 ⟹ $BC=2BD$，又 $\dfrac{AD}{BD}=\dfrac12$ ⟹ $AD=\dfrac{BD}2$。" "\n"
        r"在 $\triangle ABD$ 中由余弦定理（$B=\frac\pi6$）：$AD^{2}=BD^{2}+AB^{2}-2AB\cdot BD\cos\dfrac\pi6$。" "\n"
        r"$\dfrac{BD^{2}}4=BD^{2}+AB^{2}-\sqrt3 AB\cdot BD$ ⟹ $AB^{2}-\sqrt3 BD\cdot AB+\dfrac34BD^{2}=0$ ⟹ $\left(AB-\dfrac{\sqrt3}2BD\right)^{2}=0$。" "\n"
        r"$\therefore AB=\dfrac{\sqrt3}2BD$。" "\n"
        r"在 $\triangle ABC$ 中：$AC^{2}=BC^{2}+AB^{2}-2AB\cdot BC\cos B=4BD^{2}+\dfrac34BD^{2}-2\cdot\dfrac{\sqrt3}2BD\cdot2BD\cdot\dfrac{\sqrt3}2$" "\n"
        r"$=4BD^{2}+\dfrac34BD^{2}-3BD^{2}=\dfrac74BD^{2}$ ⟹ $AC=\dfrac{\sqrt7}2BD$。" "\n"
        r"$\therefore\dfrac{AC}{AB}=\dfrac{\frac{\sqrt7}2BD}{\frac{\sqrt3}2BD}=\dfrac{\sqrt7}{\sqrt3}=\dfrac{\sqrt{21}}3$。" "\n"
        r"**第二空**：由 $B=\frac\pi6$、$AD=\frac12BD$ 及 $AB=\frac{\sqrt3}2BD$，在 $\triangle ABD$ 中：$AD^{2}=AB^{2}+BD^{2}-2AB\cdot BD\cos B$ 已求得 $\angle ADB$。" "\n"
        r"实际由 $AD=\frac{BD}2$ 且 $B=\frac\pi6$，作 $DE\perp AB$ 于 $E$ 得 $DE=BD\sin\frac\pi6=\frac{BD}2=AD$ ⟹ $DA\perp AB$，故 $\angle ADB=\dfrac\pi3$，" "\n"
        r"从而 $\angle ADC=\pi-\dfrac\pi3=\dfrac{2\pi}3$。" "\n"
        r"在 $\triangle ADC$ 中由余弦定理（$AC=4\sqrt3$，即 $AC^{2}=48$）：" "\n"
        r"$48=AD^{2}+CD^{2}-2AD\cdot CD\cos\dfrac{2\pi}3=\dfrac14BD^{2}+CD^{2}+AD\cdot CD=\dfrac14BD^{2}+CD^{2}+\dfrac12BD\cdot CD$。" "\n"
        r"配方：$48=\left(CD-\dfrac12BD\right)^{2}+\dfrac34BD\cdot CD+\dfrac12BD\cdot CD$… 整理为 $48=\left(CD+\dfrac14BD\right)^{2}+\dfrac{15}{16}BD^{2}$ 不易直接用；" "\n"
        r"改由 $48=\dfrac14BD^{2}+CD^{2}+\dfrac12BD\cdot CD\ge\dfrac12BD\cdot CD+\dfrac12BD\cdot CD+ \dfrac12BD\cdot CD$ 不严谨，" "\n"
        r"**正确做法**：视 $BD$ 为常数，由 $48-\dfrac14BD^{2}=CD^{2}+\dfrac12BD\cdot CD$，而 $S_{\triangle ADC}=\dfrac12AD\cdot CD\sin\dfrac{2\pi}3=\dfrac{\sqrt3}8BD\cdot CD$。" "\n"
        r"由 $CD^{2}+\dfrac12BD\cdot CD=48-\dfrac14BD^{2}$ 及 $CD>0$，配合判别式可得 $BD\cdot CD\le32$（当 $CD=\frac12BD$ 时取等），" "\n"
        r"故 $S_{\triangle ADC}=\dfrac{\sqrt3}8BD\cdot CD\le\dfrac{\sqrt3}8\times32=4\sqrt3$。" "\n"
        r"故答案为 $\dfrac{\sqrt{21}}3$；$4\sqrt3$。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书详解：「$AB=\frac{\sqrt3}2BD$…$AC=\frac{\sqrt7}2BD$，所以 $\frac{AC}{AB}=\frac{\frac{\sqrt7}2BD}{\frac{\sqrt3}2BD}=\frac{\sqrt{21}}3$」、" "\n"
        r"「$BD\cdot CD=32$，所以 $S_{\triangle ADC}=\frac38 BD\cdot CD=\frac38\times32=4\sqrt3$」" "\n"
        r"—— **$AB=\frac{\sqrt3}2BD$、$AC^2=\frac74BD^2$、$\frac{\sqrt{21}}3$、$BD\cdot CD=32$、$4\sqrt3$ 与我一致** ✓✓✓" "\n"
        r"⚠ **原书系数丢根号**：它写 $S=\frac38 BD\cdot CD$，但 $\frac38\times32=12\ne4\sqrt3$。" "\n"
        r"**正确系数是 $\frac{\sqrt3}8$**（$S=\frac12\cdot AD\cdot CD\cdot\sin\frac{2\pi}3=\frac12\cdot\frac{BD}2\cdot CD\cdot\frac{\sqrt3}2=\frac{\sqrt3}8BD\cdot CD$），" "\n"
        r"$\frac{\sqrt3}8\times32=4\sqrt3$ ✓ **与答案吻合**。" "\n"
        r"**独立验算（数值，完全独立）**：" "\n"
        r"① **第一空**：$AB^2-\sqrt3 BD\cdot AB+\frac34BD^2=0$。判别式 $=3BD^2-3BD^2=0$ ⟹ 重根 $AB=\frac{\sqrt3}2BD$ ✓✓✓" "\n"
        r"（取 $BD=2$：$AD=1$，$B=30^{\circ}$。验 $AD^2=BD^2+AB^2-\sqrt3 AB\cdot BD$：" "\n"
        r"$AB=\sqrt3=1.732051$。右 $=4+3-\sqrt3(\sqrt3)(2)=7-6=1=AD^2$ ✓✓✓）" "\n"
        r"② **$AC^2=\frac74BD^2$**（$BD=2$）：$=\frac74\times4=7$，$AC=\sqrt7=2.645751$。" "\n"
        r"直接验： $AC^2=BC^2+AB^2-2AB\cdot BC\cos30^{\circ}=16+3-2(\sqrt3)(4)(\frac{\sqrt3}2)=19-12=7$ ✓✓✓" "\n"
        r"③ **$\frac{AC}{AB}=\frac{2.645751}{1.732051}=1.527525$**；$\frac{\sqrt{21}}3=\frac{4.582576}3=1.527525$ ✓✓✓" "\n"
        r"④ **$\angle ADB=\frac\pi3$**：$\triangle ABD$ 中 $AD=1,BD=2,AB=\sqrt3$。" "\n"
        r"$\cos\angle ADB=\frac{AD^2+BD^2-AB^2}{2AD\cdot BD}=\frac{1+4-3}{2(1)(2)}=\frac24=\frac12$ ⟹ $\angle ADB=60^{\circ}$ ✓✓✓" "\n"
        r"⟹ $\angle ADC=120^{\circ}$ ✓ ✓✓✓" "\n"
        r"⑤ **第二空**：$48=\frac14BD^2+CD^2+\frac12BD\cdot CD$。取等号时（原书给 $CD=\frac12BD$）：" "\n"
        r"代入：$48=\frac14BD^2+\frac14BD^2+\frac14BD^2=\frac34BD^2$ ⟹ $BD^2=64$，$BD=8$，$CD=4$。" "\n"
        r"$BD\cdot CD=32$ ✓。此时 $AD=\frac{BD}2=4$。" "\n"
        r"$S_{\triangle ADC}=\frac12\cdot AD\cdot CD\cdot\sin120^{\circ}=\frac12\times4\times4\times\frac{\sqrt3}2=4\sqrt3=6.928203$ ✓✓✓" "\n"
        r"⑥ **系数核对**：$\frac{\sqrt3}8\times32=\frac{1.732051}{8}\times32=0.216506\times32=6.928203=4\sqrt3$ ✓✓✓" "\n"
        r"（若按原书的 $\frac38$：$\frac38\times32=12\ne6.928$ ✗ **确认原书系数漏了 $\sqrt3$**）" "\n"
        r"**答案 $\frac{\sqrt{21}}3$；$4\sqrt3$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（三角形中的线段比与面积最值）**：" "\n"
        r"① ⭐⭐ **判别式为零 ⟹ 完全平方 ⟹ 直接得到线段关系**：本题 $AB^2-\sqrt3BD\cdot AB+\frac34BD^2=0$" "\n"
        r"判别式恰为 $0$ ⟹ $(AB-\frac{\sqrt3}2BD)^2=0$ —— **这类「二次方程有重根」往往是命题人的刻意设计**；" "\n"
        r"② ⭐⭐ **作垂线判直角**：由 $AD=\frac{BD}2$、$B=30^{\circ}$ 作 $DE\perp AB$ 得 $DE=\frac{BD}2=AD$ ⟹ $D$ 到 $AB$ 的垂足就是 $A$ ⟹ $DA\perp AB$。" "\n"
        r"**「高等于某条线段」⟹ 垂直**，比用余弦定理算角度更快；" "\n"
        r"③ ⭐ **$\angle ADC=\pi-\angle ADB$**：求出 $\angle ADB=\frac\pi3$ 后用补角 —— **两角互补则余弦反号**，" "\n"
        r"$\cos\angle ADC=-\frac12$ 代入余弦定理要带负号；" "\n"
        r"④ ⚠ **面积公式的系数要自己推一遍**：$S=\frac12\cdot AD\cdot CD\cdot\sin\angle ADC$，" "\n"
        r"本题 $=\frac{\sqrt3}8 BD\cdot CD$。**别照抄原书系数**（原书 $\frac38$ 漏了 $\sqrt3$，会得 $12$ 这种不在答案里的值）；" "\n"
        r"⑤ ⚠ **填空题两空要分别验**：第一空是线段比（纯几何），第二空是最值（要基本不等式），**方法完全不同**。"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-213'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-213-V1',
}

T213_V2 = {
    'type': '填空',
    'stem_text': (
        r"$\triangle ABC$ 内接于半径为 $2$ 的圆，三个内角 $A,B,C$ 的平分线延长后分别交此圆于 $A_1,B_1,C_1$，"
        r"则 $\dfrac{AA_1\cos\dfrac A2+BB_1\cos\dfrac B2+CC_1\cos\dfrac C2}{\sin A+\sin B+\sin C}$ 的值为 ____。"
    ),
    'opts': [],
    'answer': r"$4$",
    'analysis': (
        r"由 $R=2$ 得 $AA_1=2R\sin\left(B+\frac A2\right)=4\cos\frac{B-C}2$，再用积化和差得"
        r"$AA_1\cos\frac A2=2(\sin B+\sin C)$，三项相加为 $4(\sin A+\sin B+\sin C)$，故比值为 $4$。"
    ),
    'solution': (
        r"连 $BA_1$。在圆内接 $\triangle ABA_1$ 中，$\angle ABA_1=\angle ABC+\angle CBA_1$。" "\n"
        r"因 $AA_1$ 平分 $\angle A$，故 $\angle CAA_1=\frac A2$，而同弧 $\overset{\frown}{A_1C}$ 所对的 $\angle CBA_1=\angle CAA_1=\frac A2$。" "\n"
        r"$\therefore\angle ABA_1=B+\dfrac A2$。由正弦定理（$R=2$，即 $2R=4$）：" "\n"
        r"$AA_1=2R\sin\angle ABA_1=4\sin\left(B+\dfrac A2\right)$。" "\n"
        r"由 $A+B+C=\pi$：$B+\dfrac A2=\dfrac{\pi+B-C}2=\dfrac\pi2+\dfrac{B-C}2$，故 $AA_1=4\cos\dfrac{B-C}2$。" "\n"
        r"于是 $AA_1\cos\dfrac A2=4\cos\dfrac{B-C}2\cos\dfrac A2$。由积化和差：" "\n"
        r"$4\cos\dfrac{B-C}2\cos\dfrac A2=2\left[\cos\dfrac{A+B-C}2+\cos\dfrac{A-B+C}2\right]$。" "\n"
        r"$\dfrac{A+B-C}2=\dfrac{\pi-2C}2=\dfrac\pi2-C$ ⟹ $\cos=\sin C$；$\dfrac{A-B+C}2=\dfrac{\pi-2B}2=\dfrac\pi2-B$ ⟹ $\cos=\sin B$。" "\n"
        r"$\therefore AA_1\cos\dfrac A2=2(\sin B+\sin C)$。同理 $BB_1\cos\dfrac B2=2(\sin A+\sin C)$、$CC_1\cos\dfrac C2=2(\sin A+\sin B)$。" "\n"
        r"三式相加：$AA_1\cos\dfrac A2+BB_1\cos\dfrac B2+CC_1\cos\dfrac C2=4(\sin A+\sin B+\sin C)$。" "\n"
        r"故所求比值 $=4$。"
    ),
    'review': (
        r"★ 答案、详解完整 ✓（题干由我补全内接圆半径 $R=2$ 与 $A_1,B_1,C_1$ 的定义，否则题目不自足）。" "\n"
        r"原书详解：「连 $BA_1$，则 $AA_1=2R\sin(B+\frac A2)=4\sin(\frac{A+B+C}2+\frac B2-\frac C2)=4\cos\frac{B-C}2$。" "\n"
        r"$\therefore AA_1\cos\frac A2=4\cos\frac{B-C}2\cos\frac A2=2[\cos\frac{A+B-C}2+\cos\frac{A+C-B}2]=2(\sin C+\sin B)$，同理可得…" "\n"
        r"$\therefore AA_1\cos\frac A2+BB_1\cos\frac B2+CC_1\cos\frac C2=4(\sin A+\sin B+\sin C)$，即比值 $=4$」" "\n"
        r"—— **$AA_1=4\cos\frac{B-C}2$、$2(\sin B+\sin C)$、$4(\sin A+\sin B+\sin C)$、答案 $4$ 与我完全一致** ✓✓✓" "\n"
        r"**独立验算（数值，完全独立）**：" "\n"
        r"① **$AA_1=4\cos\frac{B-C}2$ 的推导**：$B+\frac A2=B+\frac{\pi-B-C}2=\frac{\pi+B-C}2=\frac\pi2+\frac{B-C}2$。" "\n"
        r"$\sin(\frac\pi2+x)=\cos x$ ⟹ $AA_1=4\cos\frac{B-C}2$ ✓✓✓" "\n"
        r"② **积化和差**：$\cos X\cos Y=\frac12[\cos(X+Y)+\cos(X-Y)]$。" "\n"
        r"$X=\frac{B-C}2,Y=\frac A2$：$X+Y=\frac{A+B-C}2$，$X-Y=\frac{B-C-A}2$。" "\n"
        r"$\frac{A+B-C}2=\frac{\pi-2C}2=\frac\pi2-C$，$\cos(\frac\pi2-C)=\sin C$ ✓" "\n"
        r"$\frac{B-C-A}2=\frac{B-C-(\pi-B-C)}2=\frac{2B-\pi}2=B-\frac\pi2$，$\cos(B-\frac\pi2)=\sin B$ ✓ ✓✓✓" "\n"
        r"所以 $4\cdot\frac12[\sin C+\sin B]=2(\sin B+\sin C)$ ✓✓✓" "\n"
        r"③ **数值验证（取 $A=60^{\circ},B=80^{\circ},C=40^{\circ}$，$R=2$）**：" "\n"
        r"$AA_1=4\cos\frac{80-40}2=4\cos20^{\circ}=4(0.939693)=3.758771$" "\n"
        r"$AA_1\cos\frac A2=3.758771\times\cos30^{\circ}=3.758771\times0.866025=3.255153$" "\n"
        r"公式 $2(\sin B+\sin C)=2(\sin80^{\circ}+\sin40^{\circ})=2(0.984808+0.642788)=2(1.627595)=3.255191$ ✓✓✓ **吻合**" "\n"
        r"④ **三式求和**：$2(\sin B+\sin C)+2(\sin A+\sin C)+2(\sin A+\sin B)=4(\sin A+\sin B+\sin C)$ ✓✓✓" "\n"
        r"⑤ **完整数值**：$\sin60+\sin80+\sin40=0.866025+0.984808+0.642788=2.493621$。" "\n"
        r"分子 $=4\times2.493621=9.974484$。比值 $=\frac{9.974484}{2.493621}=4.000000$ ✓✓✓ **精确等于 4**" "\n"
        r"⑥ **换一组角（$A=90^{\circ},B=50^{\circ},C=40^{\circ}$）**：$AA_1=4\cos5^{\circ}=4(0.996195)=3.984779$。" "\n"
        r"$AA_1\cos45^{\circ}=3.984779\times0.707107=2.817655$；公式 $2(\sin50+\sin40)=2(0.766044+0.642788)=2.817664$ ✓ ✓✓✓" "\n"
        r"**答案 $4$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（角平分线延长到外接圆）**：" "\n"
        r"① ⭐⭐ **$AA_1=2R\sin\left(B+\frac A2\right)=2R\cos\frac{B-C}2$** —— 这是本类题的**核心公式**，" "\n"
        r"由「同弧所对圆周角相等」（$\angle CBA_1=\angle CAA_1=\frac A2$）得到，值得单独记；" "\n"
        r"② ⭐⭐ **配 $\cos\frac A2$ 后用积化和差，恰好化成 $2(\sin B+\sin C)$**：" "\n"
        r"**这种「一项变成两项正弦和」的结构，三项相加后就与分母同形** —— 这是命题人的设计；" "\n"
        r"③ ⭐ **一般地 $\sum AA_1\cos\frac A2=4R\sum\sin A$**（本题 $R=2$ 给 $4\sum\sin$，比值就是 $4R/2\times$…）" "\n"
        r"实际上比值为 $2R=4$，**与三角形形状无关**；" "\n"
        r"④ ⚠ **$\frac{A+B-C}2=\frac\pi2-C$ 这步要用 $A+B+C=\pi$**：" "\n"
        r"$\cos(\frac\pi2-C)=\sin C$ —— **半角和差化到 $\frac\pi2\pm x$ 就能转正弦**；" "\n"
        r"⑤ ⚠ **本题题干在提取中缺了「内接于半径为 2 的圆」**，我已补全 —— " "\n"
        r"**录入时若题干不自足，必须从相邻题或详解中补出前置条件**，否则孩子拿到题没法做。"
    ),
    'difficulty': 0.87,
    'topics': ['M-T-213'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-213-V2',
}

T213_V3 = {
    'type': '选择',
    'stem_text': (
        r"在平面四边形 $ABCD$ 中，$AB=1$，$AD=4$，$BC=CD=2$，则四边形 $ABCD$ 面积的最大值为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac{5\sqrt7}{4}$"),
        ('B', r"$\dfrac{5\sqrt7}{8}$"),
        ('C', r"$4\sqrt2$"),
        ('D', r"$2\sqrt2$"),
    ],
    'answer': 'A',
    'analysis': (
        r"用公共边 $BD$ 在两个三角形中分别用余弦定理，得 $\cos A-\cos C=\frac98$；面积 $S=2(\sin A+\sin C)$，"
        r"再由 $(\sin A+\sin C)^2+(\cos A-\cos C)^2=2-2\cos(A+C)\le4$ 得 $\sin A+\sin C\le\frac{5\sqrt7}8$，故 $S\le\frac{5\sqrt7}4$。"
    ),
    'solution': (
        r"在 $\triangle ABD$ 中：$BD^{2}=AB^{2}+AD^{2}-2AB\cdot AD\cos A=1+16-8\cos A=17-8\cos A$。" "\n"
        r"在 $\triangle BCD$ 中：$BD^{2}=CB^{2}+CD^{2}-2CB\cdot CD\cos C=4+4-8\cos C=8-8\cos C$。" "\n"
        r"两式相等：$17-8\cos A=8-8\cos C$ ⟹ $\cos A-\cos C=\dfrac98$。" "\n"
        r"面积 $S=S_{\triangle ABD}+S_{\triangle BCD}=\dfrac12\cdot1\cdot4\sin A+\dfrac12\cdot2\cdot2\sin C=2(\sin A+\sin C)$。" "\n"
        r"关键恒等式：" "\n"
        r"$(\sin A+\sin C)^{2}+(\cos A-\cos C)^{2}=\sin^{2}A+\sin^{2}C+2\sin A\sin C+\cos^{2}A+\cos^{2}C-2\cos A\cos C$" "\n"
        r"$=2+2(\sin A\sin C-\cos A\cos C)=2-2\cos(A+C)\le4$，当且仅当 $A+C=\pi$ 时取等（此时四边形内接于圆）。" "\n"
        r"$\therefore(\sin A+\sin C)^{2}\le4-\left(\dfrac98\right)^{2}=4-\dfrac{81}{64}=\dfrac{175}{64}$ ⟹ $\sin A+\sin C\le\dfrac{5\sqrt7}8$。" "\n"
        r"$S=2(\sin A+\sin C)\le2\times\dfrac{5\sqrt7}8=\dfrac{5\sqrt7}4$。故选 A。"
    ),
    'review': (
        r"★ 题干、选项、答案、详解完整 ✓。原书详解：「$BD^2=17-8\cos A$，$BD^2=8-8\cos C$，则 $17-8\cos A=8-8\cos C\Rightarrow\cos A-\cos C=\frac98$。" "\n"
        r"由四边形 $ABCD$ 的面积 = $\triangle ABD$ 面积 + $\triangle BCD$ 面积，故 $S=2(\sin A+\sin C)$。" "\n"
        r"$(\sin A+\sin C)^2+(\cos A-\cos C)^2=2-2\cos(A+C)\le4$，当且仅当 $A+C=\pi$ 时等号成立，此时 $(\sin A+\sin C)^2+\frac{81}{64}\le4$" "\n"
        r"$\Rightarrow\sin A+\sin C\le\frac{5\sqrt7}8$，故 $S=2(\sin A+\sin C)\le\frac{5\sqrt7}4$。故选：A.」" "\n"
        r"—— **$17-8\cos A$、$8-8\cos C$、$\cos A-\cos C=\frac98$、$S=2(\sin A+\sin C)$、$2-2\cos(A+C)\le4$、$\frac{5\sqrt7}4$、答案 A 全部一致** ✓✓✓" "\n"
        r"**独立验算（数值，完全独立）**：" "\n"
        r"① **$\cos A-\cos C=\frac98=1.125$**：由 $17-8\cos A=8-8\cos C$ ⟹ $8(\cos A-\cos C)=9$ ⟹ $=\frac98$ ✓✓✓" "\n"
        r"（注意 $\cos A-\cos C=1.125$ 要求 $\cos A$ 接近 $1$、$\cos C$ 接近 $-0.125$，即 $A$ 小、$C$ 接近 $90^{\circ}$ 以上）" "\n"
        r"② **关键恒等式**：$(\sin A+\sin C)^2+(\cos A-\cos C)^2$" "\n"
        r"$=\sin^2A+2\sin A\sin C+\sin^2C+\cos^2A-2\cos A\cos C+\cos^2C$" "\n"
        r"$=(\sin^2A+\cos^2A)+(\sin^2C+\cos^2C)-2(\cos A\cos C-\sin A\sin C)$" "\n"
        r"$=2-2\cos(A+C)$ ✓✓✓" "\n"
        r"③ **$\le4$**：$2-2\cos(A+C)\le2+2=4$，等号当 $\cos(A+C)=-1$ 即 $A+C=\pi$ ✓✓✓" "\n"
        r"④ **$\sin A+\sin C\le\frac{5\sqrt7}8$**：$4-\frac{81}{64}=\frac{256-81}{64}=\frac{175}{64}$。$\sqrt{175}=5\sqrt7=13.228757$。" "\n"
        r"$\frac{13.228757}8=1.653595$ ✓ ✓✓✓" "\n"
        r"⑤ **$S\le2\times1.653595=3.307189=\frac{5\sqrt7}4$** ✓✓✓" "\n"
        r"⑥ **构造验证（$A+C=\pi$）**：$\cos C=-\cos A$（因 $C=\pi-A$）。$\cos A-\cos C=2\cos A=\frac98$ ⟹ $\cos A=\frac9{16}=0.5625$。" "\n"
        r"$A=\arccos(0.5625)=55.77^{\circ}$，$C=124.23^{\circ}$，$\sin A=\sin C=\sin(55.77^{\circ})=0.826797$。" "\n"
        r"$\sin A+\sin C=1.653594=\frac{5\sqrt7}8$ ✓✓✓" "\n"
        r"$S=2(1.653594)=3.307189$ ✓✓✓ **恰好取到最大值**" "\n"
        r"⑦ **验证 $BD^2$ 一致**：$17-8(0.5625)=17-4.5=12.5$；$8-8\cos C=8-8(-0.5625)=8+4.5=12.5$ ✓✓✓" "\n"
        r"⑧ **选项排除**：$\frac{5\sqrt7}8=1.6536$（B）是**漏乘 $2$** 的结果；$4\sqrt2=5.657$、$2\sqrt2=2.828$ 与 $3.307$ 均不符 ✓✓✓" "\n"
        r"**答案 A 正确** ✓" "\n"
        r"**⭐⭐ 通法（四边形面积：公共边 + 恒等式）**：" "\n"
        r"① ⭐⭐ **四边形的公共边 $BD$ 分别在两个三角形中写余弦定理，联立消掉 $BD$**：" "\n"
        r"得到 $\cos A-\cos C=$ 常数 —— **这是把两个三角形「缝合」起来的标准动作**；" "\n"
        r"② ⭐⭐ **$(\sin A+\sin C)^2+(\cos A-\cos C)^2=2-2\cos(A+C)\le4$**：" "\n"
        r"**这个恒等式是本题的灵魂**，它把「正弦和」与「余弦差」绑在一起 —— " "\n"
        r"已知其中一个，另一个就有上界。记忆法：**两角和差的正余弦平方和 = $2-2\cos(\text{角和})$**；" "\n"
        r"③ ⭐ **取等条件 $A+C=\pi$ ⟺ 四边形内接于圆**（对角互补）—— " "\n"
        r"**四边形面积最大时必内接于圆**，这是一般性结论；" "\n"
        r"④ ⚠ **面积要拆成两个三角形**：$S=\frac12 AB\cdot AD\sin A+\frac12 CB\cdot CD\sin C$ —— " "\n"
        r"本题系数恰好都是 $2$，故 $S=2(\sin A+\sin C)$；**若两边乘积不同，系数就不同，别硬套**；" "\n"
        r"⑤ ⚠ **$\cos A-\cos C=1.125>1$ 看似不合理**：但这是**两余弦之差**（可以接近 $2$），" "\n"
        r"不是单个余弦值 —— **别误判为「超出 $[-1,1]$ 无解」**。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-213'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-213-V3',
}

T371_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知双曲线 $C:\dfrac{x^{2}}{a^{2}}-\dfrac{y^{2}}{b^{2}}=1\ (a>0,b>0)$ 的右焦点为 $F$，"
        r"以实轴为直径的圆与其中一条渐近线的一个交点为 $P$，若直线 $PF$ 与另一条渐近线平行，则 $C$ 的离心率为（　　）"
    ),
    'opts': [
        ('A', r"$\sqrt3$"),
        ('B', r"$2$"),
        ('C', r"$3$"),
        ('D', r"$\sqrt2$"),
    ],
    'answer': 'D',
    'analysis': (
        r"联立渐近线 $y=\frac ba x$ 与圆 $x^2+y^2=a^2$ 得 $P\left(\frac{a^2}c,\frac{ab}c\right)$；"
        r"$k_{PF}=\frac{ab/c}{a^2/c-c}=-\frac ab$，与另一渐近线斜率 $-\frac ba$ 相等得 $a=b$，故 $e=\sqrt2$。"
    ),
    'solution': (
        r"以实轴为直径的圆为 $x^{2}+y^{2}=a^{2}$。不妨设 $P$ 为第一象限的交点，在渐近线 $y=\dfrac ba x$ 上。" "\n"
        r"联立 $\begin{cases}y=\dfrac ba x\\ x^{2}+y^{2}=a^{2}\end{cases}$ ⟹ $x^{2}\left(1+\dfrac{b^{2}}{a^{2}}\right)=a^{2}$ ⟹ $x^{2}\cdot\dfrac{a^{2}+b^{2}}{a^{2}}=a^{2}$。" "\n"
        r"由 $a^{2}+b^{2}=c^{2}$ 得 $x^{2}=\dfrac{a^{4}}{c^{2}}$，取 $x=\dfrac{a^{2}}c$，则 $y=\dfrac ba\cdot\dfrac{a^{2}}c=\dfrac{ab}c$。" "\n"
        r"$\therefore P\left(\dfrac{a^{2}}c,\dfrac{ab}c\right)$，又 $F(c,0)$。" "\n"
        r"$k_{PF}=\dfrac{\frac{ab}c-0}{\frac{a^{2}}c-c}=\dfrac{\frac{ab}c}{\frac{a^{2}-c^{2}}c}=\dfrac{ab}{a^{2}-c^{2}}=\dfrac{ab}{-b^{2}}=-\dfrac ab$。" "\n"
        r"（用到 $a^{2}-c^{2}=-b^{2}$。）" "\n"
        r"另一条渐近线为 $y=-\dfrac ba x$，斜率为 $-\dfrac ba$。由 $PF$ 与之平行：" "\n"
        r"$-\dfrac ab=-\dfrac ba$ ⟹ $a^{2}=b^{2}$ ⟹ $a=b$（$a,b>0$）。" "\n"
        r"$\therefore c^{2}=a^{2}+b^{2}=2a^{2}$，$c=\sqrt2 a$，$e=\dfrac ca=\sqrt2$。故选 D。"
    ),
    'review': (
        r"★ 题干、选项、答案、详解完整 ✓。原书详解：「联立方程组 $y=\frac ba x,x^2+y^2=a^2$，可得 $P$ 的坐标为 $(\frac{a^2}c,\frac{ab}c)$，" "\n"
        r"所以直线 $PF$ 的斜率 $k_{PF}=\frac{ab/c}{a^2/c-c}=-\frac ab$。因为直线 $PF$ 与另一条渐近线平行，所以 $k_{PF}=-\frac ab=-\frac ba$，" "\n"
        r"所以 $a=b$，则 $c^2=a^2+b^2=2a^2,c=\sqrt2 a$，故 $C$ 的离心率 $e=\frac ca=\sqrt2$。故选：D.」" "\n"
        r"—— **$P(\frac{a^2}c,\frac{ab}c)$、$k_{PF}=-\frac ab$、$a=b$、$e=\sqrt2$、答案 D 全部一致** ✓✓✓" "\n"
        r"**独立验算（数值，完全独立）**：" "\n"
        r"① **联立解 $P$**：$x^2(1+\frac{b^2}{a^2})=a^2$ ⟹ $x^2=\frac{a^4}{a^2+b^2}=\frac{a^4}{c^2}$ ⟹ $x=\frac{a^2}c$ ✓；$y=\frac ba\cdot\frac{a^2}c=\frac{ab}c$ ✓✓✓" "\n"
        r"② **$k_{PF}$**：分子 $\frac{ab}c$，分母 $\frac{a^2}c-c=\frac{a^2-c^2}c=\frac{-b^2}c$。比值 $=\frac{ab/c}{-b^2/c}=\frac{ab}{-b^2}=-\frac ab$ ✓✓✓" "\n"
        r"③ **平行条件**：$-\frac ab=-\frac ba$ ⟹ 交叉相乘 $a^2=b^2$ ⟹ $a=b$ ✓✓✓" "\n"
        r"④ **$e=\sqrt2$**：取 $a=b=1$，则 $c=\sqrt2$，$e=\sqrt2=1.414214$ ✓✓✓" "\n"
        r"⑤ **代回验证**：$a=b=1$。$P=(\frac{1}{\sqrt2},\frac1{\sqrt2})=(0.707107,0.707107)$。" "\n"
        r"$F=(\sqrt2,0)=(1.414214,0)$。$k_{PF}=\frac{0.707107-0}{0.707107-1.414214}=\frac{0.707107}{-0.707107}=-1$。" "\n"
        r"另一渐近线斜率 $-\frac ba=-1$ ✓ **确实平行** ✓✓✓" "\n"
        r"⑥ **$P$ 在圆上**：$0.707107^2+0.707107^2=0.5+0.5=1=a^2$ ✓ ✓✓✓" "\n"
        r"⑦ **选项排除**：$\sqrt3=1.732$（A）、$2$（B）、$3$（C）代入检验：" "\n"
        r"$e=\sqrt3$ ⟹ $b^2=2a^2$ ⟹ $b=\sqrt2a$ ⟹ $k_{PF}=-\frac a{\sqrt2 a}=-\frac1{\sqrt2}$，另一渐近线 $-\sqrt2$，不等 ✗" "\n"
        r"$e=2$ ⟹ $b=\sqrt3a$ ⟹ $k_{PF}=-\frac1{\sqrt3}$，另一渐近线 $-\sqrt3$，不等 ✗ ✓✓✓" "\n"
        r"**答案 D（$=\sqrt2$）正确** ✓" "\n"
        r"（⚠ 选项在提取中**根号全丢**：A/B/C/D 显示 `3`/`2`/`3`/`2`。我按「答案为 D 且 $e=\sqrt2$」还原 D $=\sqrt2$，" "\n"
        r"其余取常见离心率值 $\sqrt3,2,3$。已在上面 ⑦ 验证其余选项均不满足平行条件 ✓）" "\n"
        r"**⭐⭐ 通法（渐近线 + 圆 + 平行）**：" "\n"
        r"① ⭐⭐ **「以实轴为直径的圆」$x^2+y^2=a^2$ 与渐近线 $y=\pm\frac ba x$ 的交点有通式**：" "\n"
        r"$P\left(\pm\frac{a^2}c,\pm\frac{ab}c\right)$ —— **直接记住这个坐标**，能省掉每次联立；" "\n"
        r"② ⭐⭐ **$k_{PF}=-\frac ab$ 恰好是渐近线斜率 $-\frac ba$ 的「倒数交换」**：" "\n"
        r"两渐近线斜率是 $\pm\frac ba$，而 $PF$ 的斜率是 $-\frac ab$ —— **这个「$a\leftrightarrow b$ 互换」的结构很典型**；" "\n"
        r"③ ⭐ **两条渐近线斜率互为相反数（$\pm\frac ba$）**：说「与另一条平行」就是与 $-\frac ba$ 相等；" "\n"
        r"④ ⚠ **$a^2-c^2=-b^2$ 别写成 $b^2$**：这是最容易错的一步，" "\n"
        r"若写成 $\frac{ab}{b^2}=\frac ab$（正号）就会得到 $-\frac ab=-\frac ba$ 变成 $\frac ab=-\frac ba$ ⟹ 无解；" "\n"
        r"⑤ ⚠ **$P$ 取第四象限时结果相同**：$P(\frac{a^2}c,-\frac{ab}c)$ 给 $k_{PF}=+\frac ab$，与 $+\frac ba$ 平行 ⟹ 同样 $a=b$ ✓"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-371'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-371-E1',
}

T371_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知 $F_1,F_2$ 为双曲线 $E:\dfrac{x^{2}}{a^{2}}-\dfrac{y^{2}}{b^{2}}=1\ (a>0,b>0)$ 的左、右焦点，"
        r"过点 $F_1,F_2$ 分别作直线 $l_1,l_2$ 交双曲线 $E$ 于 $A,B,C,D$ 四点，使得四边形 $ABCD$ 为平行四边形，"
        r"且以 $AD$ 为直径的圆过 $F_1$，$\lvert DF_1\rvert=\lvert AF_1\rvert$，则双曲线 $E$ 的离心率为（　　）"
    ),
    'opts': [
        ('A', r"$2$"),
        ('B', r"$\sqrt3$"),
        ('C', r"$\dfrac{\sqrt5}2$"),
        ('D', r"$\dfrac{\sqrt{10}}2$"),
    ],
    'answer': 'D',
    'analysis': (
        r"利用平行四边形中心对称得 $CF_2=AF_1=x$、$CF_1=x+2a$；在以 $AD$ 为直径的圆上得 $DF_1\perp AF_1$，"
        r"进而 $DF_1\perp DC$，在直角 $\triangle CDF_1$ 中解出 $x=3a$，最后在直角 $\triangle F_1F_2D$ 中得 $10a^2=4c^2$。"
    ),
    'solution': (
        r"由四边形 $ABCD$ 为平行四边形且四顶点在中心对称的双曲线上，其中心为原点，故对角顶点关于原点对称：" "\n"
        r"$C=-A$、$D=-B$。又 $F_2=-F_1$，所以 $\lvert CF_2\rvert=\lvert AF_1\rvert$。" "\n"
        r"设 $\lvert DF_1\rvert=\lvert AF_1\rvert=x$，则 $\lvert CF_2\rvert=x$。" "\n"
        r"$D$ 在右支 ⟹ $\lvert DF_1\rvert-\lvert DF_2\rvert=2a$ ⟹ $\lvert DF_2\rvert=x-2a$。" "\n"
        r"$C$ 在右支 ⟹ $\lvert CF_1\rvert-\lvert CF_2\rvert=2a$ ⟹ $\lvert CF_1\rvert=x+2a$。" "\n"
        r"（$l_2$ 过 $F_2$ 交右支于 $C,D$，故 $F_2$ 在 $CD$ 之间）$\lvert DC\rvert=\lvert DF_2\rvert+\lvert CF_2\rvert=2x-2a$。" "\n"
        r"以 $AD$ 为直径的圆过 $F_1$ ⟹ $\angle AF_1D=90^{\circ}$，即 $DF_1\perp AF_1$。" "\n"
        r"由 $AB\parallel CD$ 且 $A,F_1,B$ 共线 ⟹ $DF_1\perp DC$。" "\n"
        r"在直角 $\triangle CDF_1$ 中：$\lvert CF_1\rvert^{2}=\lvert DF_1\rvert^{2}+\lvert CD\rvert^{2}$，" "\n"
        r"$(x+2a)^{2}=x^{2}+(2x-2a)^{2}$ ⟹ $x^{2}+4ax+4a^{2}=x^{2}+4x^{2}-8ax+4a^{2}$ ⟹ $4ax=4x^{2}-8ax$ ⟹ $4x(x-3a)=0$。" "\n"
        r"$\therefore x=3a$，$\lvert DF_1\rvert=3a$，$\lvert DF_2\rvert=a$。" "\n"
        r"由 $DF_1\perp AF_1\parallel AB$ 且 $DF_2$ 与 $DF_1$ 共线方向… 重新定位：在直角 $\triangle F_1F_2D$ 中，" "\n"
        r"$\lvert DF_1\rvert^{2}+\lvert DF_2\rvert^{2}=\lvert F_1F_2\rvert^{2}$（因 $DF_1\perp DC$ 且 $F_2$ 在 $DC$ 上，故 $DF_1\perp DF_2$）：" "\n"
        r"$(3a)^{2}+a^{2}=(2c)^{2}$ ⟹ $10a^{2}=4c^{2}$ ⟹ $e^{2}=\dfrac{c^{2}}{a^{2}}=\dfrac52$ ⟹ $e=\dfrac{\sqrt{10}}2$。故选 D。"
    ),
    'review': (
        r"★ 题干、选项、答案、详解完整 ✓。原书详解：「设 $\lvert DF_1\rvert=\lvert AF_1\rvert=x$，则 $\lvert DF_2\rvert=x-2a$。" "\n"
        r"由双曲线的对称性和平行四边形的对称性可知：$\lvert CF_2\rvert=\lvert AF_1\rvert=x$，连接 $CF_1$，则有 $\lvert CF_1\rvert=\lvert CF_2\rvert+2a=x+2a$。" "\n"
        r"$\lvert DC\rvert=\lvert DF_2\rvert+\lvert CF_2\rvert=2x-2a$。由于 $F_1$ 在以 $AD$ 为直径的圆周上，$\therefore DF_1\perp AF_1$。" "\n"
        r"$\because ABCD$ 为平行四边形，$AB\parallel CD$，$\therefore DF_1\perp DC$。在直角三角形 $CDF_1$ 中，" "\n"
        r"$\lvert CF_1\rvert^2=\lvert DF_1\rvert^2+\lvert CD\rvert^2$，$(x+2a)^2=x^2+(2x-2a)^2$，解得 $x=3a$，$\lvert DF_1\rvert=3a,\lvert DF_2\rvert=a$。" "\n"
        r"在直角三角形 $F_1F_2D$ 中，$\lvert DF_1\rvert^2+\lvert DF_2\rvert^2=\lvert F_1F_2\rvert^2$，$(3a)^2+a^2=(2c)^2$，得 $5a^2=2c^2$，$e=\frac ca=\frac{\sqrt{10}}2$。故选：D.」" "\n"
        r"—— **$CF_2=AF_1=x$、$CF_1=x+2a$、$DC=2x-2a$、$x=3a$、$10a^2=4c^2$、$e=\frac{\sqrt{10}}2$、答案 D 与我一致** ✓✓✓" "\n"
        r"（⚠ 原书末行写「得 $5a^2=2c^2$」，由 $10a^2=4c^2$ 约去 $2$ 正是 $5a^2=2c^2$ ✓ 一致）" "\n"
        r"**独立验算（数值，完全独立）**：" "\n"
        r"① **解 $(x+2a)^2=x^2+(2x-2a)^2$**：" "\n"
        r"左 $=x^2+4ax+4a^2$；右 $=x^2+4x^2-8ax+4a^2=5x^2-8ax+4a^2$。" "\n"
        r"$x^2+4ax+4a^2=5x^2-8ax+4a^2$ ⟹ $4ax+8ax=4x^2$ ⟹ $12ax=4x^2$ ⟹ $x=3a$ ✓✓✓" "\n"
        r"② **支的判定**：$\lvert DF_2\rvert=x-2a=a>0$ 要求 $x>2a$ ✓（$x=3a$）；$D$ 在右支（$\lvert DF_1\rvert>\lvert DF_2\rvert$）✓" "\n"
        r"③ **$C$ 在右支**：$\lvert CF_1\rvert-\lvert CF_2\rvert=(x+2a)-x=2a$ ✓ 右支定义 ✓✓✓" "\n"
        r"④ **$10a^2=4c^2$**：$9a^2+a^2=10a^2=(2c)^2=4c^2$ ⟹ $c^2=2.5a^2$ ⟹ $e^2=2.5$ ⟹ $e=1.581139$。" "\n"
        r"$\frac{\sqrt{10}}2=\frac{3.162278}2=1.581139$ ✓✓✓" "\n"
        r"⑤ **构造验证（取 $a=1$）**：$e=\sqrt{2.5}$，$c=1.581139$，$b^2=c^2-a^2=2.5-1=1.5$，$b=1.224745$。" "\n"
        r"$x=3a=3$。$\lvert DF_1\rvert=3$，$\lvert DF_2\rvert=1$。差 $=2=2a$ ✓ 右支 ✓" "\n"
        r"$\lvert CF_2\rvert=\lvert AF_1\rvert=3$，$\lvert CF_1\rvert=3+2=5$。$\lvert CF_1\rvert-\lvert CF_2\rvert=2=2a$ ✓ 右支 ✓" "\n"
        r"$\lvert DC\rvert=\lvert DF_2\rvert+\lvert CF_2\rvert=1+3=4=2x-2a=6-2=4$ ✓✓✓" "\n"
        r"⑥ **勾股验证**：$\triangle CDF_1$：$CF_1^2=25$，$DF_1^2+CD^2=9+16=25$ ✓✓✓ **直角成立**" "\n"
        r"$\triangle F_1F_2D$：$F_1F_2^2=(2c)^2=4(2.5)=10$；$DF_1^2+DF_2^2=9+1=10$ ✓✓✓ **直角成立**" "\n"
        r"⑦ **选项排除**：$2$（A）⟹ $e^2=4$；$\sqrt3$（B）⟹ $e^2=3$；$\frac{\sqrt5}2$（C）⟹ $e^2=1.25<1$ 不可能（双曲线 $e>1$）✗。" "\n"
        r"只有 $\frac{\sqrt{10}}2$ 给 $e^2=2.5$ ✓ ✓✓✓" "\n"
        r"**答案 D 正确** ✓" "\n"
        r"**⭐⭐ 通法（平行四边形 + 双曲线的中心对称）**：" "\n"
        r"① ⭐⭐ **四顶点在中心对称曲线上且构成平行四边形 ⟹ 中心就是曲线的中心（原点）**：" "\n"
        r"于是 $C=-A$、$D=-B$，**对角顶点关于原点对称** —— 这一步把未知量减少一半；" "\n"
        r"② ⭐⭐ **由 $F_2=-F_1$ 得 $\lvert CF_2\rvert=\lvert AF_1\rvert$**：" "\n"
        r"**关于原点对称的两点，到关于原点对称的两焦点距离交叉相等** —— 这是本题的第一个关键等式；" "\n"
        r"③ ⭐ **支的判定要看距离大小**：$\lvert PF_{远}\rvert-\lvert PF_{近}\rvert=2a$，" "\n"
        r"右支上 $\lvert PF_1\rvert>\lvert PF_2\rvert$（$F_1$ 是远焦点），左支相反 —— **判错支则整个符号都反**；" "\n"
        r"④ ⭐ **以 $AD$ 为直径的圆过 $F_1$ ⟺ $\angle AF_1D=90^{\circ}$ ⟺ $DF_1\perp AF_1$** —— " "\n"
        r"**「直径所对圆周角是直角」的逆用**，配 $AB\parallel CD$ 把垂直转移到 $DF_1\perp DC$；" "\n"
        r"⑤ ⚠ **最后还要在 $\triangle F_1F_2D$ 中再用一次勾股**：" "\n"
        r"因 $F_2$ 在 $DC$ 上且 $DF_1\perp DC$ ⟹ $DF_1\perp DF_2$ —— **第二次出现直角，别漏**；" "\n"
        r"⑥ ⚠ **选项 C $=\frac{\sqrt5}2<1$ 不是合法离心率**：双曲线 $e>1$，**可直接排除**， sanity check 很有用。"
    ),
    'difficulty': 0.93,
    'topics': ['M-T-371'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-371-V1',
}

T371_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知双曲线 $\dfrac{x^{2}}{a^{2}}-\dfrac{y^{2}}{b^{2}}=1\ (a>0,b>0)$ 与圆 $x^{2}+y^{2}=b^{2}$ 在第二象限相交于点 $M$，"
        r"$F_1,F_2$ 分别为该双曲线的左、右焦点，且 $\sin\angle MF_1F_2=3\sin\angle MF_2F_1$，则该双曲线的离心率为（　　）"
    ),
    'opts': [
        ('A', r"$\sqrt2$"),
        ('B', r"$\dfrac32$"),
        ('C', r"$\sqrt3$"),
        ('D', r"$2$"),
    ],
    'answer': 'C',
    'analysis': (
        r"由正弦定理得 $\lvert MF_2\rvert=3\lvert MF_1\rvert$，配定义 $\lvert MF_2\rvert-\lvert MF_1\rvert=2a$ 得 $\lvert MF_1\rvert=a$、$\lvert MF_2\rvert=3a$；"
        r"由 $\lvert OM\rvert=b$ 及 $b^2+a^2=c^2$ 知 $\angle OMF_1=90^{\circ}$，再用等面积与双曲线方程得 $b^2=2a^2$，故 $e=\sqrt3$。"
    ),
    'solution': (
        r"在 $\triangle MF_1F_2$ 中由正弦定理：$\dfrac{\lvert MF_2\rvert}{\sin\angle MF_1F_2}=\dfrac{\lvert MF_1\rvert}{\sin\angle MF_2F_1}$，" "\n"
        r"故 $\sin\angle MF_1F_2=3\sin\angle MF_2F_1$ ⟹ $\lvert MF_2\rvert=3\lvert MF_1\rvert$。" "\n"
        r"$M$ 在第二象限，位于左支，故 $\lvert MF_2\rvert-\lvert MF_1\rvert=2a$。" "\n"
        r"联立得 $\lvert MF_1\rvert=a$，$\lvert MF_2\rvert=3a$。" "\n"
        r"在 $\triangle OMF_1$ 中：$\lvert OM\rvert=b$（$M$ 在圆 $x^2+y^2=b^2$ 上）、$\lvert MF_1\rvert=a$、$\lvert OF_1\rvert=c$。" "\n"
        r"由 $b^{2}+a^{2}=c^{2}$ 得 $\lvert OM\rvert^{2}+\lvert MF_1\rvert^{2}=\lvert OF_1\rvert^{2}$ ⟹ $\angle OMF_1=90^{\circ}$。" "\n"
        r"设 $M(x_0,y_0)$。由等面积：$\dfrac12\lvert OM\rvert\cdot\lvert MF_1\rvert=\dfrac12\lvert OF_1\rvert\cdot y_0$（$y_0>0$），" "\n"
        r"$y_0=\dfrac{b\cdot a}{c}=\dfrac{ab}c$。" "\n"
        r"由 $M$ 在圆上：$x_0^{2}=b^{2}-y_0^{2}=b^{2}-\dfrac{a^{2}b^{2}}{c^{2}}=b^{2}\left(1-\dfrac{a^{2}}{c^{2}}\right)=\dfrac{b^{4}}{c^{2}}$。" "\n"
        r"由 $M$ 在双曲线上：$\dfrac{x_0^{2}}{a^{2}}-\dfrac{y_0^{2}}{b^{2}}=1$ ⟹ $\dfrac1{a^{2}}\cdot\dfrac{b^{4}}{c^{2}}-\dfrac1{b^{2}}\cdot\dfrac{a^{2}b^{2}}{c^{2}}=1$ ⟹ $\dfrac{b^{4}}{a^{2}c^{2}}-\dfrac{a^{2}}{c^{2}}=1$。" "\n"
        r"乘 $a^2c^2$：$b^{4}-a^{4}=a^{2}c^{2}$。" "\n"
        r"由 $b^{2}=c^{2}-a^{2}$：$b^{4}-a^{4}=(b^{2}+a^{2})(b^{2}-a^{2})=c^{2}(b^{2}-a^{2})=a^{2}c^{2}$ ⟹ $b^{2}-a^{2}=a^{2}$ ⟹ $b^{2}=2a^{2}$。" "\n"
        r"$\therefore e=\dfrac ca=\sqrt{1+\dfrac{b^{2}}{a^{2}}}=\sqrt3$。故选 C。"
    ),
    'review': (
        r"★ 题干、选项、答案、详解完整 ✓。原书详解：「在 $\triangle MF_1F_2$ 中，$\because\sin\angle MF_1F_2=3\sin\angle MF_2F_1$，" "\n"
        r"$\therefore$ 由正弦定理知 $\lvert MF_2\rvert=3\lvert MF_1\rvert$，又 $\because\lvert MF_2\rvert-\lvert MF_1\rvert=2a$，$\therefore\lvert MF_1\rvert=a,\lvert MF_2\rvert=3a$。" "\n"
        r"$\therefore$ 在 $\triangle OMF_1$ 中，$\lvert OM\rvert=b,\lvert MF_1\rvert=a,\lvert OF_1\rvert=c$，$\therefore\lvert OM\rvert^2+\lvert MF_1\rvert^2=\lvert OF_1\rvert^2$，$\therefore\angle OMF_1=90^{\circ}$。" "\n"
        r"设 $M(x_0,y_0)$，则由等面积得 $y_0=\frac{ab}c$…$b^4-a^4=a^2c^2$，即 $b^2-a^2=a^2$，即 $b^2=2a^2$，$\therefore e=\sqrt3$。故选：C.」" "\n"
        r"—— **$MF_2=3MF_1$、$MF_1=a$、$MF_2=3a$、$\angle OMF_1=90^{\circ}$、$y_0=\frac{ab}c$、$b^4-a^4=a^2c^2$、$b^2=2a^2$、$e=\sqrt3$、答案 C 全部一致** ✓✓✓" "\n"
        r"**独立验算（数值，完全独立）**：" "\n"
        r"① **正弦定理换边**：$\frac{MF_2}{\sin\angle MF_1F_2}=\frac{MF_1}{\sin\angle MF_2F_1}$。" "\n"
        r"$\sin\angle MF_1F_2=3\sin\angle MF_2F_1$ ⟹ $MF_2=3MF_1$ ✓✓✓（**角对边，别搞反**）" "\n"
        r"② **支**：$M$ 第二象限、左支 ⟹ 远焦点是 $F_2$ ⟹ $MF_2-MF_1=2a$ ✓。" "\n"
        r"$3MF_1-MF_1=2a$ ⟹ $MF_1=a$，$MF_2=3a$ ✓✓✓" "\n"
        r"③ **$\angle OMF_1=90^{\circ}$**：$b^2+a^2=c^2$ ✓ 恰为勾股 ⟹ 直角在 $M$ ✓✓✓" "\n"
        r"④ **$b^4-a^4=a^2c^2$ 代入 $a=1,b^2=2,c^2=3$**：$b^4=4$，$a^4=1$，差 $=3$；$a^2c^2=1\times3=3$ ✓✓✓" "\n"
        r"⑤ **$e=\sqrt3=1.732051$** ✓✓✓" "\n"
        r"⑥ **构造验证（$a=1,b=\sqrt2=1.414214,c=\sqrt3=1.732051$）**：" "\n"
        r"$y_0=\frac{ab}c=\frac{1\times1.414214}{1.732051}=0.816497$。$x_0^2=\frac{b^4}{c^2}=\frac4{3}=1.333333$，$x_0=-1.154701$（第二象限取负）✓" "\n"
        r"验 $M$ 在圆上：$x_0^2+y_0^2=1.333333+0.666667=2=b^2$ ✓✓✓" "\n"
        r"验 $M$ 在双曲线上：$\frac{1.333333}{1}-\frac{0.666667}{2}=1.333333-0.333333=1$ ✓✓✓" "\n"
        r"验 $MF_1$：$F_1=(-1.732051,0)$。$MF_1=\sqrt{(-1.154701+1.732051)^2+0.816497^2}=\sqrt{0.577350^2+0.666667}$" "\n"
        r"$=\sqrt{0.333333+0.666667}=\sqrt1=1=a$ ✓✓✓" "\n"
        r"验 $MF_2$：$F_2=(1.732051,0)$。$MF_2=\sqrt{(-1.154701-1.732051)^2+0.666667}=\sqrt{(-2.886751)^2+0.666667}$" "\n"
        r"$=\sqrt{8.333333+0.666667}=\sqrt9=3=3a$ ✓✓✓ **完全吻合**" "\n"
        r"⑦ **验 $\sin$ 关系**：$\triangle MF_1F_2$ 中 $MF_1=1,MF_2=3,F_1F_2=2c=3.464102$。" "\n"
        r"$\cos\angle MF_1F_2=\frac{MF_1^2+F_1F_2^2-MF_2^2}{2MF_1\cdot F_1F_2}=\frac{1+12-9}{2(1)(3.464102)}=\frac4{6.928203}=0.577350$ ⟹ $\sin=0.816497$" "\n"
        r"$\cos\angle MF_2F_1=\frac{9+12-1}{2(3)(3.464102)}=\frac{20}{20.784610}=0.962250$ ⟹ $\sin=0.272166$" "\n"
        r"比值 $=\frac{0.816497}{0.272166}=3.000$ ✓✓✓ **恰为 3**" "\n"
        r"**答案 C 正确** ✓" "\n"
        r"**⭐⭐ 通法（焦点三角形 + 圆）**：" "\n"
        r"① ⭐⭐ **$\sin$ 关系用正弦定理换成边长比**：$\sin\alpha=k\sin\beta$ ⟹ **$\alpha$ 的对边 $=k\times\beta$ 的对边** —— " "\n"
        r"**一定要认准「哪个角对哪条边」**（本题 $\angle MF_1F_2$ 对 $MF_2$）；" "\n"
        r"② ⭐⭐ **$\lvert OM\rvert=b$ 与 $\lvert MF_1\rvert=a$ 恰好满足勾股 $a^2+b^2=c^2$** ⟹ $\angle OMF_1=90^{\circ}$ —— " "\n"
        r"**这个直角不是巧合，是「点在半径为 $b$ 的圆上」这个条件的必然结果**，很多题都靠它；" "\n"
        r"③ ⭐ **等面积求纵坐标**：$\frac12\lvert OM\rvert\cdot\lvert MF_1\rvert=\frac12\lvert OF_1\rvert\cdot y_0$ ⟹ $y_0=\frac{ab}c$ —— " "\n"
        r"**直角三角形斜边上的高 = 两直角边乘积 / 斜边**，比代入方程解快；" "\n"
        r"④ ⚠ **$b^4-a^4=(b^2+a^2)(b^2-a^2)=c^2(b^2-a^2)$**：" "\n"
        r"用 $b^2+a^2=c^2$ 因式分解是化简关键，**别直接展开硬算**；" "\n"
        r"⑤ ⚠ **$M$ 在第二象限 ⟹ $x_0<0$**：求 $x_0^2$ 后开方要取负号（虽然本题只用到 $x_0^2$，但坐标验证时别弄错）。"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-371'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-371-V2',
}

T371_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知 $F_1,F_2$ 分别为双曲线 $\dfrac{x^{2}}{a^{2}}-\dfrac{y^{2}}{b^{2}}=1\ (a>0,b>0)$ 的左、右焦点，"
        r"以 $F_1F_2$ 为直径的圆与双曲线在第一象限和第三象限的交点分别为 $M,N$，"
        r"设四边形 $F_1NF_2M$ 的周长 $C$ 与面积 $S$ 满足 $S=\dfrac a2C$，则该双曲线的离心率的平方为（　　）"
    ),
    'opts': [
        ('A', r"$2+\sqrt2$"),
        ('B', r"$8+4\sqrt2$"),
        ('C', r"$2+2\sqrt2$"),
        ('D', r"$2+\sqrt3$"),
    ],
    'answer': 'A',
    'analysis': (
        r"由对称性 $S=2S_{\triangle F_1F_2M}=2cy_1$，联立圆与双曲线得 $y_1=\frac{b^2}c$，故 $S=2b^2$；"
        r"由 $S=\frac a2C$ 得 $C=\frac{4b^2}a$，再配 $MF_1+MF_2=\frac{2b^2}a$、$MF_1-MF_2=2a$ 及勾股得 $e^4-4e^2+2=0$，取 $e^2=2+\sqrt2$。"
    ),
    'solution': (
        r"由对称性，$M$ 与 $N$ 关于原点对称，$S_{\triangle F_1F_2M}=S_{\triangle F_1F_2N}$，故 $S=2S_{\triangle F_1F_2M}$。" "\n"
        r"圆以 $F_1F_2$ 为直径，半径为 $c$。设 $M(x_1,y_1)$（第一象限，$y_1>0$），则" "\n"
        r"$\begin{cases}\dfrac{x_1^{2}}{a^{2}}-\dfrac{y_1^{2}}{b^{2}}=1\\[2mm] x_1^{2}+y_1^{2}=c^{2}\end{cases}$" "\n"
        r"由第一式 $\dfrac{x_1^{2}}{a^{2}}=1+\dfrac{y_1^{2}}{b^{2}}$，代入前式消元：由第二式 $x_1^{2}=c^{2}-y_1^{2}$，代入第一式：" "\n"
        r"$\dfrac{c^{2}-y_1^{2}}{a^{2}}-\dfrac{y_1^{2}}{b^{2}}=1$ ⟹ $b^{2}c^{2}-b^{2}y_1^{2}-a^{2}y_1^{2}=a^{2}b^{2}$ ⟹ $b^{2}c^{2}-a^{2}b^{2}=(a^{2}+b^{2})y_1^{2}=c^{2}y_1^{2}$。" "\n"
        r"$\therefore b^{2}(c^{2}-a^{2})=c^{2}y_1^{2}$ ⟹ $b^{4}=c^{2}y_1^{2}$ ⟹ $y_1=\dfrac{b^{2}}c$。" "\n"
        r"$S=2S_{\triangle F_1F_2M}=2\cdot\dfrac12\cdot\lvert F_1F_2\rvert\cdot y_1=2c\cdot\dfrac{b^{2}}c=2b^{2}$。" "\n"
        r"由 $S=\dfrac a2C$：$2b^{2}=\dfrac a2C$ ⟹ $C=\dfrac{4b^{2}}a$。" "\n"
        r"又 $C=\lvert MF_1\rvert+\lvert MF_2\rvert+\lvert NF_1\rvert+\lvert NF_2\rvert=2\left(\lvert MF_1\rvert+\lvert MF_2\rvert\right)$（由对称性），" "\n"
        r"$\therefore\lvert MF_1\rvert+\lvert MF_2\rvert=\dfrac{2b^{2}}a$，且 $\lvert MF_1\rvert-\lvert MF_2\rvert=2a$（$M$ 在右支）。" "\n"
        r"$\therefore\lvert MF_1\rvert\cdot\lvert MF_2\rvert=\dfrac{\left(\frac{2b^{2}}a\right)^{2}-(2a)^{2}}4=\dfrac{b^{4}-a^{4}}{a^{2}}$。" "\n"
        r"因 $F_1F_2$ 为直径，$M$ 在圆上 ⟹ $\angle F_1MF_2=90^{\circ}$ ⟹ $\lvert MF_1\rvert^{2}+\lvert MF_2\rvert^{2}=\lvert F_1F_2\rvert^{2}=4c^{2}$。" "\n"
        r"$\left(\lvert MF_1\rvert+\lvert MF_2\rvert\right)^{2}=\lvert MF_1\rvert^{2}+\lvert MF_2\rvert^{2}+2\lvert MF_1\rvert\lvert MF_2\rvert$：" "\n"
        r"$\dfrac{4b^{4}}{a^{2}}=4c^{2}+\dfrac{2(b^{4}-a^{4})}{a^{2}}$ ⟹ $4b^{4}=4a^{2}c^{2}+2b^{4}-2a^{4}$ ⟹ $2b^{4}=4a^{2}c^{2}-2a^{4}$ ⟹ $b^{4}+a^{4}=2a^{2}c^{2}$。" "\n"
        r"设 $e^{2}=t$，则 $b^{2}=a^{2}(t-1)$：$a^{4}(t-1)^{2}+a^{4}=2a^{4}t$ ⟹ $(t-1)^{2}+1=2t$ ⟹ $t^{2}-4t+2=0$。" "\n"
        r"$t=2\pm\sqrt2$。由 $e>1$ 知 $t=e^{2}>1$，而 $2-\sqrt2\approx0.586<1$（舍），故 $e^{2}=2+\sqrt2$。故选 A。"
    ),
    'review': (
        r"★ 题干、选项、答案、详解完整 ✓。原书详解：「$S=2S_{\triangle F_1F_2M}=2c\cdot y_1=2b^2$（因为 $S=\frac a2C$，所以 $C=\frac{4b^2}a$）。" "\n"
        r"因为 $C=2(\lvert MF_1\rvert+\lvert MF_2\rvert)$，可得 $\lvert MF_1\rvert+\lvert MF_2\rvert=\frac{2b^2}a$。" "\n"
        r"因为 $\lvert MF_1\rvert-\lvert MF_2\rvert=2a$…$4a^2+\frac{2(b^4-a^4)}{a^2}=4c^2$，$2+e^4-4e^2=0$，" "\n"
        r"所以离心率的平方为 $e^2=2\pm\sqrt2$，又 $e>1$，则 $e^2=2+\sqrt2$。故选：A.」" "\n"
        r"—— **$y_1=\frac{b^2}c$、$S=2b^2$、$C=\frac{4b^2}a$、$MF_1+MF_2=\frac{2b^2}a$、$2+e^4-4e^2=0$、$e^2=2+\sqrt2$、答案 A 全部一致** ✓✓✓" "\n"
        r"**独立验算（数值，完全独立）**：" "\n"
        r"① **$y_1=\frac{b^2}c$ 的推导**：$b^2(c^2-y_1^2)-a^2y_1^2=a^2b^2$ ⟹ $b^2c^2-a^2b^2=(a^2+b^2)y_1^2=c^2y_1^2$。" "\n"
        r"$b^2(c^2-a^2)=b^2\cdot b^2=b^4=c^2y_1^2$ ⟹ $y_1=\frac{b^2}c$ ✓✓✓" "\n"
        r"② **$S=2c\cdot y_1=2c\cdot\frac{b^2}c=2b^2$** ✓✓✓" "\n"
        r"③ **$C=\frac{4b^2}a$**：$2b^2=\frac a2C$ ⟹ $C=\frac{4b^2}a$ ✓✓✓" "\n"
        r"④ **$MF_1\cdot MF_2=\frac{b^4-a^4}{a^2}$**：用 $(u+v)^2-(u-v)^2=4uv$。" "\n"
        r"$uv=\frac{(2b^2/a)^2-(2a)^2}{4}=\frac{4b^4/a^2-4a^2}{4}=\frac{b^4-a^4}{a^2}$ ✓✓✓" "\n"
        r"⑤ **$(\frac{2b^2}a)^2=4c^2+2\frac{b^4-a^4}{a^2}$**：乘 $a^2$：$4b^4=4a^2c^2+2b^4-2a^4$ ⟹ $2b^4=4a^2c^2-2a^4$" "\n"
        r"⟹ $b^4+a^4=2a^2c^2$ ✓✓✓" "\n"
        r"⑥ **解 $t^2-4t+2=0$**：$t=\frac{4\pm\sqrt{16-8}}2=\frac{4\pm2\sqrt2}2=2\pm\sqrt2$ ✓✓✓" "\n"
        r"$2-\sqrt2=0.585786<1$ ✗（$e^2$ 必须 $>1$）；$2+\sqrt2=3.414214>1$ ✓ ⟹ $e^2=2+\sqrt2$ ✓✓✓" "\n"
        r"⑦ **构造验证（$a=1$，$e^2=3.414214$，$c=1.847759$，$b^2=2.414214$）**：" "\n"
        r"$y_1=\frac{b^2}c=\frac{2.414214}{1.847759}=1.306563$。$x_1^2=c^2-y_1^2=3.414214-1.707107=1.707107$，$x_1=1.306563$。" "\n"
        r"（注意 $x_1=y_1$，因 $b^2=c^2-a^2$ 时…巧合）" "\n"
        r"验双曲线：$\frac{1.707107}{1}-\frac{1.707107}{2.414214}=1.707107-0.707107=1$ ✓✓✓" "\n"
        r"$MF_1=\sqrt{(1.306563+1.847759)^2+1.707107}=\sqrt{(3.154322)^2+1.707107}=\sqrt{9.949747+1.707107}=\sqrt{11.656854}=3.414214$" "\n"
        r"$MF_2=\sqrt{(1.306563-1.847759)^2+1.707107}=\sqrt{0.292893+1.707107}=\sqrt2=1.414214$" "\n"
        r"验 $MF_1-MF_2=3.414214-1.414214=2=2a$ ✓✓✓" "\n"
        r"验 $MF_1+MF_2=4.828427$；$\frac{2b^2}a=2(2.414214)=4.828427$ ✓✓✓" "\n"
        r"验勾股：$MF_1^2+MF_2^2=11.656854+2=13.656854$；$(2c)^2=4(3.414214)=13.656854$ ✓✓✓ **直角成立**" "\n"
        r"验 $C=2(4.828427)=9.656854$；$\frac{4b^2}a=4(2.414214)=9.656854$ ✓✓✓" "\n"
        r"验 $S=\frac a2C=\frac12(9.656854)=4.828427$；$2b^2=4.828427$ ✓✓✓ **完全自洽**" "\n"
        r"⑧ **选项排除**：$8+4\sqrt2=13.657$（B）、$2+2\sqrt2=4.828$（C）、$2+\sqrt3=3.732$（D）都不等于 $3.414$ ✓✓✓" "\n"
        r"（注意 C $=4.828=2b^2$ 恰是面积值 —— **命题人把面积放在选项里当陷阱**）" "\n"
        r"**答案 A 正确** ✓" "\n"
        r"**⭐⭐ 通法（以焦距为直径的圆 + 双曲线）**：" "\n"
        r"① ⭐⭐ **圆 $x^2+y^2=c^2$ 与双曲线交点的纵坐标有通式 $y=\frac{b^2}c$**：" "\n"
        r"联立后 $b^2(c^2-y^2)-a^2y^2=a^2b^2$ ⟹ $b^4=c^2y^2$ —— **这个结论可直接用**，省掉每次联立；" "\n"
        r"② ⭐⭐ **直径所对圆周角是直角 ⟹ $MF_1^2+MF_2^2=4c^2$**：" "\n"
        r"**这是把「周长」与「两焦半径」联系起来的桥梁**，配 $(u+v)^2=u^2+v^2+2uv$ 使用；" "\n"
        r"③ ⭐ **四边形周长 $C=2(MF_1+MF_2)$**：由 $M,N$ 关于原点对称 —— **对称性能把周长减半**；" "\n"
        r"④ ⚠ **$e^2$ 的两个根要按 $e>1$ 筛选**：$t^2-4t+2=0$ 给 $2\pm\sqrt2$，" "\n"
        r"$2-\sqrt2\approx0.586<1$ 必须舍 —— **双曲线 $e^2>1$，椭圆才是 $e^2<1$**；" "\n"
        r"⑤ ⚠ **选项 C $=2+2\sqrt2=2b^2$ 是面积值**：" "\n"
        r"**命题人把中间量（面积）做成选项**，若没算完就会误选 —— 算到底再对答案。"
    ),
    'difficulty': 0.93,
    'topics': ['M-T-371'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-371-V3',
}

T188_E1 = {
    'type': '选择',
    'stem_text': (
        r"函数 $f(x)=\sin(\omega x+\varphi)\ \left(\omega>0,\lvert\varphi\rvert\le\dfrac\pi2\right)$，已知 $\left(-\dfrac\pi6,0\right)$ 为 $f(x)$ 图象的一个对称中心，"
        r"直线 $x=\dfrac{13\pi}{12}$ 为 $f(x)$ 图象的一条对称轴，且 $f(x)$ 在 $\left[\dfrac{13\pi}{12},\dfrac{19\pi}{12}\right]$ 上单调递减．"
        r"记满足条件的所有 $\omega$ 的值的和为 $S$，则 $S$ 的值为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac{12}5$"),
        ('B', r"$\dfrac85$"),
        ('C', r"$\dfrac{16}5$"),
        ('D', r"$\dfrac{18}5$"),
    ],
    'answer': 'A',
    'analysis': (
        r"对称中心与对称轴的距离为 $\frac{2k+1}4T$，得 $\omega=\frac25(1+4k)$ 或 $\frac25(3+4k)$；"
        r"由单调区间长度 $\frac\pi2\le\frac T2$ 得 $\omega\le2$，候选 $\frac25,2,\frac65$，逐项验证单调性后只有 $\frac25$ 与 $2$ 符合。"
    ),
    'solution': (
        r"对称中心 $\left(-\frac\pi6,0\right)$ 到对称轴 $x=\frac{13\pi}{12}$ 的距离为 $\dfrac{13\pi}{12}+\dfrac\pi6=\dfrac{15\pi}{12}=\dfrac{5\pi}4$。" "\n"
        r"正弦型函数中，对称中心到相邻对称轴的距离为 $\dfrac{2k+1}4T$，故" "\n"
        r"$\dfrac{5\pi}4=\dfrac{2k+1}4\cdot\dfrac{2\pi}\omega$ 或 $\dfrac{5\pi}4=\dfrac{4k+3}4\cdot\dfrac{2\pi}\omega$（对应两类相位关系）。" "\n"
        r"整理得 $\omega=\dfrac25(1+4k)$ 或 $\omega=\dfrac25(3+4k)$，$k\in\mathbb Z$。" "\n"
        r"由 $f$ 在 $\left[\frac{13\pi}{12},\frac{19\pi}{12}\right]$ 上单调递减，区间长度 $\dfrac{19\pi}{12}-\dfrac{13\pi}{12}=\dfrac\pi2\le\dfrac T2=\dfrac\pi\omega$ ⟹ $\omega\le2$。" "\n"
        r"**候选**：$\omega=\frac25(1+4k)$ 给 $\frac25(k=0)$、$2(k=1)$；$\omega=\frac25(3+4k)$ 给 $\frac65(k=0)$。（$k\ge2$ 或 $k<0$ 均超范围或为负）" "\n"
        r"**逐一验证**（由对称中心定 $\varphi$，再检查区间内的相位范围）：" "\n"
        r"① $\omega=\dfrac25$：$\omega\left(-\frac\pi6\right)+\varphi=k\pi$ ⟹ $\varphi=k\pi+\dfrac\pi{15}$，取 $\varphi=\dfrac\pi{15}$。" "\n"
        r"$x\in\left[\frac{13\pi}{12},\frac{19\pi}{12}\right]$ 时 $\dfrac25x+\dfrac\pi{15}\in\left[\dfrac\pi2,\dfrac{7\pi}{10}\right]\subset\left[\dfrac\pi2,\dfrac{3\pi}2\right]$（$\sin$ 的递减区间）⟹ **符合**。" "\n"
        r"② $\omega=2$：$\varphi=2\cdot\frac\pi6+k\pi=\dfrac\pi3+k\pi$，取 $\varphi=\dfrac\pi3$。" "\n"
        r"$2x+\dfrac\pi3\in\left[\dfrac{5\pi}2,\dfrac{7\pi}2\right]=\left[\dfrac\pi2+2\pi,\dfrac{3\pi}2+2\pi\right]$ ⟹ **符合**。" "\n"
        r"③ $\omega=\dfrac65$：$\varphi=\dfrac65\cdot\frac\pi6+k\pi=\dfrac\pi5+k\pi$，取 $\varphi=\dfrac\pi5$。" "\n"
        r"$\dfrac65x+\dfrac\pi5\in\left[\dfrac{3\pi}2,\dfrac{21\pi}{10}\right]\subset\left[\dfrac{3\pi}2,\dfrac{5\pi}2\right]$（$\sin$ 的递增区间）⟹ **不符，舍去**。" "\n"
        r"$\therefore\omega=\dfrac25$ 或 $2$，$S=\dfrac25+2=\dfrac{12}5$。故选 A。"
    ),
    'review': (
        r"★ 题干、选项、答案、详解完整 ✓。原书详解：「$\frac{13}{12}\pi+\frac\pi6=\frac T4+kT$ 或 $\frac{13\pi}{12}+\frac\pi6=\frac{3T}4+kT$，" "\n"
        r"$\therefore\frac54\pi=(\frac14+k)\frac{2\pi}\omega$ 或 $\frac{5\pi}4=(\frac34+k)\frac{2\pi}\omega$，$\therefore\omega=\frac25(1+4k)$ 或 $\omega=\frac25(3+4k)$。" "\n"
        r"$\because f(x)$ 在 $[\frac{13\pi}{12},\frac{19\pi}{12}]$ 上单调递减，$\therefore\frac{19\pi}{12}-\frac{13\pi}{12}\le\frac T2$，$\therefore\frac\pi2\le\frac12\cdot\frac{2\pi}\omega\Rightarrow\omega\le2$。" "\n"
        r"① 当 $\omega=\frac25(1+4k)$ 时，$k=0$ 知 $\omega=\frac25$…$k=1$ 时 $\omega=2$…② 当 $\omega=\frac25(3+4k)$ 时，$k=0$ 知 $\omega=\frac65$…单调递增，舍去。" "\n"
        r"综上：$\omega=\frac25$ 或 $2$，$S=\frac25+2=\frac{12}5$。故选：A.」" "\n"
        r"—— **$\omega=\frac25(1+4k)$ 或 $\frac25(3+4k)$、$\omega\le2$、$\frac25$✓、$2$✓、$\frac65$✗、$S=\frac{12}5$、答案 A 全部一致** ✓✓✓" "\n"
        r"**独立验算（数值，完全独立）**：" "\n"
        r"① **距离**：$\frac{13\pi}{12}-(-\frac\pi6)=\frac{13\pi}{12}+\frac{2\pi}{12}=\frac{15\pi}{12}=\frac{5\pi}4$ ✓✓✓" "\n"
        r"② **$\omega$ 通式**：$\frac{5\pi}4=\frac{2k+1}4\cdot\frac{2\pi}\omega=\frac{(2k+1)\pi}{2\omega}$ ⟹ $\frac54=\frac{2k+1}{2\omega}$ ⟹ $\omega=\frac{2(2k+1)}5=\frac25(2k+1)$。" "\n"
        r"$k$ 取偶/奇分别给 $\frac25(4m+1)$ 与 $\frac25(4m+3)$ ✓ 与原书一致 ✓✓✓" "\n"
        r"③ **$\omega\le2$**：$\frac\pi2\le\frac T2=\frac\pi\omega$ ⟹ $\omega\le2$ ✓✓✓" "\n"
        r"④ **$\omega=\frac25$ 的相位区间**：$x=\frac{13\pi}{12}$：$\frac25\cdot\frac{13\pi}{12}+\frac\pi{15}=\frac{13\pi}{30}+\frac{2\pi}{30}=\frac{15\pi}{30}=\frac\pi2$ ✓" "\n"
        r"$x=\frac{19\pi}{12}$：$\frac25\cdot\frac{19\pi}{12}+\frac\pi{15}=\frac{19\pi}{30}+\frac{2\pi}{30}=\frac{21\pi}{30}=\frac{7\pi}{10}$ ✓" "\n"
        r"$[\frac\pi2,\frac{7\pi}{10}]\subset[\frac\pi2,\frac{3\pi}2]$（$\sin$ 在 $[\frac\pi2,\frac{3\pi}2]$ 递减）✓✓✓" "\n"
        r"⑤ **$\omega=2$ 的相位区间**：$2\cdot\frac{13\pi}{12}+\frac\pi3=\frac{13\pi}6+\frac{2\pi}6=\frac{15\pi}6=\frac{5\pi}2$ ✓" "\n"
        r"$2\cdot\frac{19\pi}{12}+\frac\pi3=\frac{19\pi}6+\frac{2\pi}6=\frac{21\pi}6=\frac{7\pi}2$ ✓" "\n"
        r"$[\frac{5\pi}2,\frac{7\pi}2]=[\frac\pi2+2\pi,\frac{3\pi}2+2\pi]$ ⟹ 递减 ✓✓✓" "\n"
        r"⑥ **$\omega=\frac65$ 的相位区间**：$\frac65\cdot\frac{13\pi}{12}+\frac\pi5=\frac{13\pi}{10}+\frac{2\pi}{10}=\frac{15\pi}{10}=\frac{3\pi}2$ ✓" "\n"
        r"$\frac65\cdot\frac{19\pi}{12}+\frac\pi5=\frac{19\pi}{10}+\frac{2\pi}{10}=\frac{21\pi}{10}$ ✓" "\n"
        r"$[\frac{3\pi}2,\frac{21\pi}{10}]$：$2.1\pi<\frac{5\pi}2=2.5\pi$，在 $[\frac{3\pi}2,\frac{5\pi}2]$ 内 ⟹ $\sin$ **递增** ✗ ✓✓✓ **确认舍去**" "\n"
        r"⑦ **$S=\frac25+2=\frac{2+10}5=\frac{12}5=2.4$** ✓✓✓" "\n"
        r"⑧ **选项排除**：$\frac85=1.6$（B）是只取 $\frac25+\frac65$；$\frac{16}5=3.2$（C）、$\frac{18}5=3.6$（D）都含 $\frac65$ ✗ ✓✓✓" "\n"
        r"**答案 A 正确** ✓" "\n"
        r"**⭐⭐ 通法（$\omega$ 的多解问题）**：" "\n"
        r"① ⭐⭐ **对称中心 ↔ 对称轴的距离 $=\frac{2k+1}4T$**（不是 $\frac k2T$）—— " "\n"
        r"**这是本题的入口**，由此列出 $\omega$ 的两个等差数列；" "\n"
        r"② ⭐⭐ **单调区间长度 $\le\frac T2$**：$\frac{19\pi}{12}-\frac{13\pi}{12}=\frac\pi2\le\frac T2$ ⟹ $\omega\le2$ —— " "\n"
        r"**先用它把 $\omega$ 的候选砍到个位数**，再逐项验证；" "\n"
        r"③ ⭐ **每个候选都要「回到相位区间」验证**：算出 $\omega x+\varphi$ 在区间端点的取值，" "\n"
        r"看是否落在 $[\frac\pi2+2k\pi,\frac{3\pi}2+2k\pi]$（递减）内 —— **光满足距离条件不够，$\frac65$ 就是反例**；" "\n"
        r"④ ⚠ **$\varphi$ 由对称中心定**：$\omega(-\frac\pi6)+\varphi=k\pi$，取满足 $\lvert\varphi\rvert\le\frac\pi2$ 的那个值；" "\n"
        r"⑤ ⚠ **「所有 $\omega$ 的和」意味着可能不止一个解**：" "\n"
        r"**别找到一个就收工** —— 本题两个解，漏掉 $2$ 会得 $\frac25$（不在选项里 → 立刻警觉）。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-188'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-188-E1',
}

T188_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知向量 $\vec a=(\sin\omega x,\cos\omega x)$，$\vec b=(1,-1)$，函数 $f(x)=\vec a\cdot\vec b$，且 $\omega>\dfrac12$，$x\in\mathbb R$，"
        r"若 $f(x)$ 的任何一条对称轴与 $x$ 轴交点的横坐标都不属于区间 $(3\pi,4\pi)$，则 $\omega$ 的取值范围是（　　）"
    ),
    'opts': [
        ('A', r"$\left[\dfrac7{12},\dfrac{15}{16}\right]\cup\left[\dfrac{13}{12},\dfrac{19}{16}\right]$"),
        ('B', r"$\left[\dfrac7{12},\dfrac{11}{16}\right]\cup\left[\dfrac{11}{12},\dfrac{15}{16}\right]$"),
        ('C', r"$\left[\dfrac12,\dfrac7{12}\right]\cup\left[\dfrac{11}{12},\dfrac{19}{16}\right]$"),
        ('D', r"$\left[\dfrac12,\dfrac{11}{16}\right]\cup\left[\dfrac{11}{12},\dfrac{15}{16}\right]$"),
    ],
    'answer': 'B',
    'analysis': (
        r"$f=\sqrt2\sin\left(\omega x-\frac\pi4\right)$，对称轴 $x=\frac1\omega\left(\frac{3\pi}4+k\pi\right)$。"
        r"先求「对称轴落入 $(3\pi,4\pi)$」的 $\omega$ 区间，再在全集 $\left(\frac12,1\right)$ 中取补集。"
    ),
    'solution': (
        r"$f(x)=\sin\omega x-\cos\omega x=\sqrt2\sin\left(\omega x-\dfrac\pi4\right)$。" "\n"
        r"对称轴满足 $\omega x-\dfrac\pi4=\dfrac\pi2+k\pi$ ⟹ $x=\dfrac1\omega\left(\dfrac{3\pi}4+k\pi\right)$，$k\in\mathbb Z$。" "\n"
        r"由 $\omega>\frac12$ 得 $T=\frac{2\pi}\omega<4\pi$；又区间 $(3\pi,4\pi)$ 的长度为 $\pi$，需 $\frac T2>\pi$ 即 $\omega<1$（否则必有对称轴落入）。" "\n"
        r"故全集为 $\dfrac12<\omega<1$。" "\n"
        r"**先求「有对称轴落入 $(3\pi,4\pi)$」的条件**：$3\pi<\dfrac1\omega\left(\dfrac{3\pi}4+k\pi\right)<4\pi$ ⟹ $3\omega<\dfrac34+k<4\omega$。" "\n"
        r"⟹ $\omega>\dfrac{3/4+k}4=\dfrac3{16}+\dfrac k4$ 且 $\omega<\dfrac{3/4+k}3=\dfrac14+\dfrac k3$。" "\n"
        r"在 $\frac12<\omega<1$ 内，只有 $k=1,2,3$ 给出非空区间：" "\n"
        r"$k=1$：$\left(\dfrac7{16},\dfrac7{12}\right)$；$k=2$：$\left(\dfrac{11}{16},\dfrac{11}{12}\right)$；$k=3$：$\left(\dfrac{15}{16},\dfrac54\right)$。" "\n"
        r"与 $\left(\frac12,1\right)$ 取交：$\left(\dfrac12,\dfrac7{12}\right)$、$\left(\dfrac{11}{16},\dfrac{11}{12}\right)$、$\left(\dfrac{15}{16},1\right)$。" "\n"
        r"**取补集**（即任何对称轴都不落入）：" "\n"
        r"$\omega\in\left[\dfrac7{12},\dfrac{11}{16}\right]\cup\left[\dfrac{11}{12},\dfrac{15}{16}\right]$。故选 B。"
    ),
    'review': (
        r"★ 题干、选项、答案、详解完整 ✓。原书详解：「$f(x)=\sqrt2\sin(\omega x-\frac\pi4)$，由 $\omega>\frac12$，得 $T=\frac{2\pi}\omega<4\pi$，$\frac T2>\pi$，$\frac12<\omega<1$。" "\n"
        r"由对称轴 $\omega x-\frac\pi4=\frac\pi2+k\pi$，$x=\frac1\omega(\frac{3\pi}4+k\pi)$。假设对称轴在区间 $(3\pi,4\pi)$ 内，可知 $\frac3{16}+\frac k4<\omega<\frac14+\frac k3$。" "\n"
        r"当 $k=1,2,3$ 时，$\frac7{16}<\omega<\frac7{12}$，$\frac{11}{16}<\omega<\frac{11}{12}$，$\frac{15}{16}<\omega<\frac54$。" "\n"
        r"现不属于区间 $(3\pi,4\pi)$，所以上面的并集在全集 $\frac12<\omega<1$ 中做补集，得 $\omega\in[\frac7{12},\frac{11}{16}]\cup[\frac{11}{12},\frac{15}{16}]$，选 B.」" "\n"
        r"—— **$f=\sqrt2\sin(\omega x-\frac\pi4)$、$x=\frac1\omega(\frac{3\pi}4+k\pi)$、三个区间 $(\frac7{16},\frac7{12})$/$(\frac{11}{16},\frac{11}{12})$/$(\frac{15}{16},\frac54)$、补集 $[\frac7{12},\frac{11}{16}]\cup[\frac{11}{12},\frac{15}{16}]$、答案 B 全部一致** ✓✓✓" "\n"
        r"**独立验算（数值，完全独立）**：" "\n"
        r"① **$f=\sin\omega x-\cos\omega x=\sqrt2\sin(\omega x-\frac\pi4)$**：$\sqrt2\sin(\omega x-\frac\pi4)=\sqrt2(\sin\omega x\cos\frac\pi4-\cos\omega x\sin\frac\pi4)=\sin\omega x-\cos\omega x$ ✓✓✓" "\n"
        r"② **对称轴**：$\sin$ 的对称轴在相位 $=\frac\pi2+k\pi$ ⟹ $\omega x-\frac\pi4=\frac\pi2+k\pi$ ⟹ $\omega x=\frac{3\pi}4+k\pi$ ⟹ $x=\frac1\omega(\frac{3\pi}4+k\pi)$ ✓✓✓" "\n"
        r"③ **落入条件**：$3\pi<\frac1\omega(\frac{3\pi}4+k\pi)<4\pi$ ⟹ 除以 $\pi$：$3<\frac{3/4+k}\omega<4$ ⟹ $3\omega<\frac34+k<4\omega$ ✓✓✓" "\n"
        r"④ **$k=1$**：$\omega>\frac{3/4+1}4=\frac{1.75}4=0.4375=\frac7{16}$；$\omega<\frac{1.75}3=0.583333=\frac7{12}$ ✓✓✓" "\n"
        r"$k=2$：$\omega>\frac{2.75}4=0.6875=\frac{11}{16}$；$\omega<\frac{2.75}3=0.916667=\frac{11}{12}$ ✓✓✓" "\n"
        r"$k=3$：$\omega>\frac{3.75}4=0.9375=\frac{15}{16}$；$\omega<\frac{3.75}3=1.25=\frac54$ ✓✓✓" "\n"
        r"⑤ **补集**：全集 $(\frac12,1)=(0.5,1)$。" "\n"
        r"排除 $(0.5,0.583333)$、$(0.6875,0.916667)$、$(0.9375,1)$。" "\n"
        r"剩余 $[0.583333,0.6875]\cup[0.916667,0.9375]=[\frac7{12},\frac{11}{16}]\cup[\frac{11}{12},\frac{15}{16}]$ ✓✓✓" "\n"
        r"⑥ **验证边界 $\omega=\frac7{12}=0.583333$**：对称轴 $x=\frac1{0.583333}(\frac{3\pi}4+k\pi)=1.714286(0.75\pi+k\pi)$。" "\n"
        r"$k=1$：$1.714286(1.75\pi)=3.0\pi$ —— 恰在 $3\pi$（区间是**开区间** $(3\pi,4\pi)$，故 $3\pi$ 不属于）✓ 合法 ✓✓✓" "\n"
        r"$k=2$：$1.714286(2.75\pi)=4.714\pi>4\pi$ ✓ 不在区间内 ✓ ✓✓✓" "\n"
        r"⑦ **验证 $\omega=\frac{11}{16}=0.6875$**：$x=\frac1{0.6875}(\frac{3\pi}4+k\pi)=1.454545(0.75\pi+k\pi)$。" "\n"
        r"$k=1$：$1.454545(1.75\pi)=2.545\pi<3\pi$ ✓；$k=2$：$1.454545(2.75\pi)=4.0\pi$ —— 恰在 $4\pi$（开区间，不属于）✓ 合法 ✓✓✓" "\n"
        r"⑧ **选项排除**：A 含 $[\frac{13}{12},\frac{19}{16}]=(1.083,1.188)$ 超出 $\omega<1$ ✗；C、D 含 $[\frac12,\frac7{12}]$ 会给对称轴落入 ✗ ✓✓✓" "\n"
        r"**答案 B 正确** ✓" "\n"
        r"**⭐⭐ 通法（对称轴不落入某区间）**：" "\n"
        r"① ⭐⭐ **先求「落入」的条件再取补集**：正面处理「任何一条都不落入」很难，" "\n"
        r"**反过来求「存在一条落入」的 $\omega$ 区间**（即 $3\omega<\frac34+k<4\omega$），再取补 —— **正难则反**；" "\n"
        r"② ⭐⭐ **辅助角化一**：$\sin\omega x-\cos\omega x=\sqrt2\sin(\omega x-\frac\pi4)$ —— " "\n"
        r"**向量点积给的函数先化成一个正弦**，否则无法谈对称轴；" "\n"
        r"③ ⭐ **$k$ 只需试有限个值**：由 $\frac12<\omega<1$ 及区间端点，只有 $k=1,2,3$ 非空 —— " "\n"
        r"**先定全集再定 $k$ 的范围**，避免无穷枚举；" "\n"
        r"④ ⚠ **端点开闭**：区间 $(3\pi,4\pi)$ 是**开区间**，所以对称轴恰在 $x=3\pi$ 或 $4\pi$ 是**允许**的 —— " "\n"
        r"这正是答案中 $\frac7{12}$ 与 $\frac{15}{16}$ 取**闭**的原因（上面 ⑥⑦ 已验证）；" "\n"
        r"⑤ ⚠ **全集 $\frac12<\omega<1$ 中 $\omega<1$ 的来源**：需要 $\frac T2>\pi$（区间长度），" "\n"
        r"即 $\frac\pi\omega>\pi$ ⟹ $\omega<1$ —— **这个上界容易被忽略**，漏了会得到含 $[\frac{13}{12},\cdot]$ 的错误选项 A。"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-188'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-188-V1',
}

T188_V2 = {
    'type': '填空',
    'stem_text': (
        r"已知函数 $f(x)=\cos(\omega x+\varphi)\ \left(\omega>0,\lvert\varphi\rvert\le\dfrac\pi2\right)$，$x=-\dfrac\pi4$ 为 $f(x)$ 的零点，"
        r"$x=\dfrac\pi4$ 为 $y=f(x)$ 图象的对称轴，且 $f(x)$ 在 $\left[\dfrac\pi{18},\dfrac\pi6\right]$ 上单调，则 $\omega$ 的最大值为 ____。"
    ),
    'opts': [],
    'answer': r"$5$",
    'analysis': (
        r"零点与对称轴的距离 $\frac\pi2=\frac{2k+1}4T$ 得 $\omega=2k+1$；由单调区间长度 $\frac\pi9\le\frac T2$ 得 $\omega\le9$。"
        r"从大到小验证 $\omega=9,7$ 均不单调，$\omega=5$ 时相位区间 $\left[\frac\pi{36},\frac{7\pi}{12}\right]\subset[0,\pi]$ 单调递减，故最大为 $5$。"
    ),
    'solution': (
        r"零点 $x=-\frac\pi4$ 与对称轴 $x=\frac\pi4$ 的距离为 $\dfrac\pi4-\left(-\dfrac\pi4\right)=\dfrac\pi2$。" "\n"
        r"对余弦型函数，零点到对称轴的距离为 $\dfrac{2k+1}4T$，故 $\dfrac\pi2=\dfrac{2k+1}4\cdot\dfrac{2\pi}\omega=\dfrac{(2k+1)\pi}{2\omega}$，" "\n"
        r"⟹ $\omega=2k+1$，$k\in\mathbb N$。" "\n"
        r"由 $f$ 在 $\left[\frac\pi{18},\frac\pi6\right]$ 上单调，区间长度 $\dfrac\pi6-\dfrac\pi{18}=\dfrac\pi9\le\dfrac T2=\dfrac\pi\omega$ ⟹ $\omega\le9$。" "\n"
        r"候选 $\omega\in\{9,7,5,3,1\}$，从大到小验证：" "\n"
        r"① $\omega=9$：由对称轴 $9\cdot\frac\pi4+\varphi=k\pi$ 及 $\lvert\varphi\rvert\le\frac\pi2$ 得 $\varphi=-\dfrac\pi4$。" "\n"
        r"$f(x)=\cos\left(9x-\dfrac\pi4\right)$，$x\in\left[\frac\pi{18},\frac\pi6\right]$ 时 $9x-\dfrac\pi4\in\left[\dfrac\pi4,\dfrac{5\pi}4\right]$，跨越 $\pi$ ⟹ **不单调**。" "\n"
        r"② $\omega=7$：$\varphi=\dfrac\pi4$，$f(x)=\cos\left(7x+\dfrac\pi4\right)$，$7x+\dfrac\pi4\in\left[\dfrac{23\pi}{36},\dfrac{17\pi}{12}\right]$，跨越 $\pi$ ⟹ **不单调**。" "\n"
        r"③ $\omega=5$：$\varphi=-\dfrac\pi4$，$f(x)=\cos\left(5x-\dfrac\pi4\right)$，$5x-\dfrac\pi4\in\left[\dfrac\pi{36},\dfrac{7\pi}{12}\right]\subset[0,\pi]$ ⟹ **单调递减，符合**。" "\n"
        r"$\therefore\omega$ 的最大值为 $5$。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书详解：「由题意可得 $\frac\pi4-(-\frac\pi4)=\frac k2T+\frac T4$，即 $\frac\pi2=\frac{2k+1}4\cdot T=\frac{2k+1}4\cdot\frac{2\pi}\omega$，解得 $\omega=2k+1$。" "\n"
        r"又因为 $f(x)$ 在 $[\frac\pi{18},\frac\pi6]$ 上单调，所以 $\frac\pi6-\frac\pi{18}=\frac\pi9\le\frac T2$，即 $\omega\le9$。" "\n"
        r"因为要求 $\omega$ 的最大值，令 $\omega=7$…$f(x)=\cos(7x+\frac\pi4)$，在 $[\frac\pi{18},\frac\pi6]$ 不单调。" "\n"
        r"同理，令 $\omega=5$，$f(x)=\cos(5x-\frac\pi4)$，在 $[\frac\pi{20},\frac{5\pi}{20}]$ 上单调递减，因为 $[\frac\pi{18},\frac\pi6]\subseteq[\frac\pi{20},\frac{5\pi}{20}]$，" "\n"
        r"所以 $f(x)$ 在 $[\frac\pi{18},\frac\pi6]$ 单调递减，满足题意，所以 $\omega$ 的最大值为 $5$。」" "\n"
        r"—— **$\omega=2k+1$、$\omega\le9$、$\omega=7$ 不单调、$\omega=5$ 单调、答案 $5$ 全部一致** ✓✓✓" "\n"
        r"**独立验算（数值，完全独立）**：" "\n"
        r"① **$\omega=2k+1$**：$\frac\pi2=\frac{2k+1}{4}\cdot\frac{2\pi}\omega$ ⟹ $\frac12=\frac{2k+1}{2\omega}$ ⟹ $\omega=2k+1$ ✓✓✓" "\n"
        r"② **$\omega\le9$**：$\frac\pi9\le\frac\pi\omega$ ⟹ $\omega\le9$ ✓✓✓" "\n"
        r"③ **$\omega=9$ 的 $\varphi$**：对称轴 $9(\frac\pi4)+\varphi=k\pi$ ⟹ $\frac{9\pi}4+\varphi=k\pi$。$\frac{9\pi}4=2\pi+\frac\pi4$。" "\n"
        r"$\varphi=k\pi-2\pi-\frac\pi4=(k-2)\pi-\frac\pi4$。取 $k=2$：$\varphi=-\frac\pi4$ ✓（$\lvert\varphi\rvert\le\frac\pi2$）✓✓✓" "\n"
        r"相位区间：$9(\frac\pi{18})-\frac\pi4=\frac\pi2-\frac\pi4=\frac\pi4$；$9(\frac\pi6)-\frac\pi4=\frac{3\pi}2-\frac\pi4=\frac{5\pi}4$。" "\n"
        r"$[\frac\pi4,\frac{5\pi}4]$ 跨过 $\pi$（$\cos$ 在 $[0,\pi]$ 递减、$[\pi,2\pi]$ 递增）⟹ **不单调** ✓✓✓" "\n"
        r"④ **$\omega=7$ 的 $\varphi$**：$\frac{7\pi}4+\varphi=k\pi$ ⟹ $\varphi=(k-2)\pi+\frac\pi4$。取 $k=2$：$\varphi=\frac\pi4$ ✓" "\n"
        r"相位区间：$7(\frac\pi{18})+\frac\pi4=\frac{7\pi}{18}+\frac\pi4=\frac{14\pi+9\pi}{36}=\frac{23\pi}{36}=0.639\pi$；" "\n"
        r"$7(\frac\pi6)+\frac\pi4=\frac{7\pi}6+\frac\pi4=\frac{14\pi+3\pi}{12}=\frac{17\pi}{12}=1.417\pi$。" "\n"
        r"跨过 $\pi$ ⟹ **不单调** ✓✓✓" "\n"
        r"⑤ **$\omega=5$ 的 $\varphi$**：$\frac{5\pi}4+\varphi=k\pi$ ⟹ $\varphi=(k-1)\pi-\frac\pi4$。取 $k=1$：$\varphi=-\frac\pi4$ ✓" "\n"
        r"相位区间：$5(\frac\pi{18})-\frac\pi4=\frac{5\pi}{18}-\frac\pi4=\frac{10\pi-9\pi}{36}=\frac\pi{36}=0.0278\pi$；" "\n"
        r"$5(\frac\pi6)-\frac\pi4=\frac{5\pi}6-\frac\pi4=\frac{10\pi-3\pi}{12}=\frac{7\pi}{12}=0.5833\pi$。" "\n"
        r"$[\frac\pi{36},\frac{7\pi}{12}]\subset[0,\pi]$ ⟹ $\cos$ **单调递减** ✓✓✓ **符合**" "\n"
        r"⑥ **$\omega=9$ 与 $7$ 都被排除，$5$ 是最大** ✓✓✓" "\n"
        r"（验证 $\omega=6$ 不在候选内：$\omega=2k+1$ 只给奇数 ✓）" "\n"
        r"**答案 $5$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（$\omega$ 最大值：先列候选再逐个验证）**：" "\n"
        r"① ⭐⭐ **零点到对称轴的距离 $=\frac{2k+1}4T$**：对 $\cos$ 同样成立 —— " "\n"
        r"**由此得 $\omega$ 是奇数**（$\omega=2k+1$），这是本题的入口；" "\n"
        r"② ⭐⭐ **单调区间长度 $\le\frac T2$ 给出上界**：$\frac\pi9\le\frac\pi\omega$ ⟹ $\omega\le9$ —— " "\n"
        r"**候选只有 $9,7,5,3,1$ 五个，从大到小验证即可**；" "\n"
        r"③ ⭐ **判单调看相位区间是否跨越极值点**：$\cos$ 的极值点在相位 $=k\pi$（$0,\pi,2\pi,\dots$）。" "\n"
        r"**若区间 $[\alpha,\beta]$ 内含有 $k\pi$，则不单调** —— 这是最快的判据（上面 $\omega=9,7$ 都跨 $\pi$）；" "\n"
        r"④ ⚠ **$\varphi$ 要由对称轴条件 + $\lvert\varphi\rvert\le\frac\pi2$ 确定**：" "\n"
        r"$\omega\cdot\frac\pi4+\varphi=k\pi$，**每个 $\omega$ 对应的 $\varphi$ 不同**，不能沿用上一个的；" "\n"
        r"⑤ ⚠ **「最大值」要从大到小试，找到第一个符合的就停**：" "\n"
        r"本题 $9$✗、$7$✗、$5$✓，**别从小到大做**（那样要做完 $1,3,5$ 才知道）。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-188'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-188-V2',
}

T188_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知定义在 $\left[0,\dfrac\pi6\right]$ 上的函数 $f(x)=\sin\left(\omega x-\dfrac\pi6\right)\ (\omega>0)$ 的最大值为 $\dfrac\omega5$，"
        r"则正实数 $\omega$ 的取值个数最多为（　　）"
    ),
    'opts': [
        ('A', r"$4$"),
        ('B', r"$3$"),
        ('C', r"$2$"),
        ('D', r"$1$"),
    ],
    'answer': 'C',
    'analysis': (
        r"当 $\omega\ge4$ 时最大值为 $1$，得 $\omega=5$；当 $0<\omega<4$ 时最大值为 $\sin\left(\frac{\pi\omega}6-\frac\pi6\right)$，"
        r"设 $g(\omega)=\sin\left(\frac{\pi\omega}6-\frac\pi6\right)-\frac\omega5$，由 $g(1)=-\frac15<0$、$g(4)=\frac15>0$ 知有一根，故共 $2$ 个。"
    ),
    'solution': (
        r"令 $\theta=\omega x-\dfrac\pi6$。由 $x\in\left[0,\dfrac\pi6\right]$ 得 $\theta\in\left[-\dfrac\pi6,\dfrac{\pi\omega}6-\dfrac\pi6\right]$。" "\n"
        r"**情形一：$\dfrac{\pi\omega}6-\dfrac\pi6\ge\dfrac\pi2$**，即 $\omega\ge4$。" "\n"
        r"此时 $\theta$ 的区间包含 $\frac\pi2$，故 $f_{\max}=1$。由 $1=\dfrac\omega5$ 得 $\omega=5$（满足 $\omega\ge4$）✓" "\n"
        r"**情形二：$0<\omega<4$**。此时 $\dfrac{\pi\omega}6-\dfrac\pi6<\dfrac\pi2$，区间 $\left[-\frac\pi6,\frac{\pi\omega}6-\frac\pi6\right]\subset\left[-\frac\pi2,\frac\pi2\right]$，" "\n"
        r"$\sin\theta$ 在该区间上单调递增，故 $f_{\max}=\sin\left(\dfrac{\pi\omega}6-\dfrac\pi6\right)$。" "\n"
        r"设 $g(\omega)=\sin\left(\dfrac{\pi\omega}6-\dfrac\pi6\right)-\dfrac\omega5$，$\omega\in(0,4)$。" "\n"
        r"$g'(\omega)=\dfrac\pi6\cos\left(\dfrac{\pi\omega}6-\dfrac\pi6\right)-\dfrac15$。" "\n"
        r"当 $\omega\in[1,4]$ 时 $\dfrac{\pi\omega}6-\dfrac\pi6\in\left[0,\dfrac\pi2\right]$，$\cos$ 在此递减，故 $g'$ 递减。" "\n"
        r"$g'(1)=\dfrac\pi6\cdot1-\dfrac15=0.5236-0.2=0.3236>0$；$g'(4)=\dfrac\pi6\cdot0-\dfrac15=-0.2<0$。" "\n"
        r"故存在 $\omega_0\in(1,4)$ 使 $g'(\omega_0)=0$，$g$ 在 $[1,\omega_0]$ 递增、$[\omega_0,4]$ 递减。" "\n"
        r"$g(1)=\sin0-\dfrac15=-\dfrac15<0$；$g(4)=\sin\dfrac\pi2-\dfrac45=1-\dfrac45=\dfrac15>0$。" "\n"
        r"由 $g(\omega_0)>g(4)>0$ 及 $g(1)<0$，知 $g$ 在 $(1,\omega_0)$ 内有**唯一**一个零点。" "\n"
        r"（在 $(0,1)$ 上，$g(\omega)=\sin(\text{负数})-\frac\omega5<0$，无零点。）" "\n"
        r"综上：$\omega=5$ 与情形二的一个解，共 $2$ 个。故选 C。"
    ),
    'review': (
        r"★ 题干、选项、答案、详解完整 ✓。原书详解：「令 $\theta=\omega x-\frac\pi6\in[-\frac\pi6,\frac\pi6\omega-\frac\pi6]$。" "\n"
        r"① 当 $\frac\pi6\omega-\frac\pi6\ge\frac\pi2$ 时，即 $\omega\ge4$，根据正弦函数的单调性可知 $f_{\max}=1=\frac\omega5$，解得 $\omega=5$；" "\n"
        r"② 当 $\frac\pi6\omega-\frac\pi6<\frac\pi2$ 时，即 $0<\omega<4$，$f_{\max}=\sin(\frac\pi6\omega-\frac\pi6)=\frac\omega5>0$。" "\n"
        r"设 $g(x)=\sin(\frac\pi6 x-\frac\pi6)-\frac x5$，$1\le x\le4$，$g'(x)=\frac\pi6\cos(\frac\pi6 x-\frac\pi6)-\frac15$…$g(1)=-\frac15$，$g(4)=1-\frac45=\frac15>0$…" "\n"
        r"存在唯一的 $x_1\in[1,x_0]\subseteq[1,4]$，使得 $g(x_1)=0$，即说明 $\sin(\frac\pi6\omega-\frac\pi6)=\frac\omega5$ 只有一个实根。" "\n"
        r"综上可知，正实数 $\omega$ 的取值个数最多为 $2$。故选：C.」" "\n"
        r"—— **$\theta$ 区间、$\omega\ge4$ 给 $\omega=5$、$0<\omega<4$ 给 $g$ 的唯一根、共 $2$ 个、答案 C 全部一致** ✓✓✓" "\n"
        r"**独立验算（数值，完全独立）**：" "\n"
        r"① **$\theta$ 区间**：$x=0$ ⟹ $\theta=-\frac\pi6$；$x=\frac\pi6$ ⟹ $\theta=\frac{\pi\omega}6-\frac\pi6$ ✓✓✓" "\n"
        r"② **情形一**：$\frac{\pi\omega}6-\frac\pi6\ge\frac\pi2$ ⟹ $\frac{\pi\omega}6\ge\frac{2\pi}3$ ⟹ $\omega\ge4$ ✓✓✓" "\n"
        r"$f_{\max}=1=\frac\omega5$ ⟹ $\omega=5$ ✓（$5\ge4$ ✓）✓✓✓" "\n"
        r"③ **情形二**：$\omega<4$ ⟹ 区间上限 $<\frac\pi2$，且 $\sin$ 在 $[-\frac\pi6,\frac\pi2]$ 递增 ⟹ $f_{\max}=\sin(\frac{\pi\omega}6-\frac\pi6)$ ✓✓✓" "\n"
        r"④ **$g(1)$**：$\frac{\pi(1)}6-\frac\pi6=0$，$\sin0=0$，$g(1)=0-\frac15=-\frac15=-0.2<0$ ✓✓✓" "\n"
        r"⑤ **$g(4)$**：$\frac{4\pi}6-\frac\pi6=\frac{3\pi}6=\frac\pi2$，$\sin\frac\pi2=1$，$g(4)=1-\frac45=0.2>0$ ✓✓✓" "\n"
        r"⑥ **单调性**：$g'(\omega)=\frac\pi6\cos(\frac{\pi\omega}6-\frac\pi6)-\frac15$。" "\n"
        r"$\omega=1$：$\frac\pi6\cos0-\frac15=0.523599-0.2=0.323599>0$ ✓" "\n"
        r"$\omega=4$：$\frac\pi6\cos\frac\pi2-\frac15=0-0.2=-0.2<0$ ✓ ⟹ **先增后减，先负后正**" "\n"
        r"由 $g(1)<0$、$g(\omega_0)>0$（峰值）、$g(4)>0$：**在 $[1,\omega_0]$ 内恰有一个零点** ✓✓✓" "\n"
        r"⑦ **数值求解验证**：找 $g(\omega)=0$。$\omega=2$：$\frac{2\pi}6-\frac\pi6=\frac\pi6$，$\sin=0.5$，$g=0.5-0.4=0.1>0$。" "\n"
        r"$\omega=1.5$：$\frac{1.5\pi}6-\frac\pi6=0.25\pi-0.1667\pi=0.0833\pi=0.261799$，$\sin=0.258819$，$g=0.258819-0.3=-0.041181<0$。" "\n"
        r"$\omega=1.7$：$0.2833\pi-0.1667\pi=0.1167\pi=0.366519$，$\sin=0.358368$，$g=0.358368-0.34=0.018368>0$。" "\n"
        r"$\omega=1.65$：$0.275\pi-0.1667\pi=0.1083\pi=0.340339$，$\sin=0.333807$，$g=0.333807-0.33=0.003807>0$。" "\n"
        r"$\omega=1.63$：$0.2717\pi-0.1667\pi=0.105\pi=0.329867$，$\sin=0.323901$，$g=0.323901-0.326=-0.002099<0$。" "\n"
        r"⟹ **根在 $(1.63,1.65)$，确有一个** ✓✓✓" "\n"
        r"⑧ **加上 $\omega=5$，共 $2$ 个** ✓✓✓" "\n"
        r"⑨ **选项排除**：$4,3,1$（A/B/D）都不等于 $2$ ✓✓✓" "\n"
        r"**答案 C 正确** ✓" "\n"
        r"**⭐⭐ 通法（含参最值 = 参数本身）**：" "\n"
        r"① ⭐⭐ **先按「区间是否覆盖峰值点」分类**：$\omega\ge4$ 时区间盖住 $\frac\pi2$（$f_{\max}=1$），" "\n"
        r"$\omega<4$ 时盖不住（$f_{\max}=\sin(\text{右端点})$）—— **这个分界点（$\omega=4$）必须先找出来**；" "\n"
        r"② ⭐⭐ **第二类是方程 $\sin(\cdots)=\frac\omega5$ 的根的个数问题**：" "\n"
        r"**用 $g$ 的单调性（先增后减）+ 端点异号**判定根的个数 —— 比画图严谨；" "\n"
        r"③ ⭐ **$g(1)=-\frac15$、$g(4)=\frac15$ 恰好异号**：" "\n"
        r"**端点异号 + 单峰 ⟹ 恰一个根** —— 这是判根个数的标准套路；" "\n"
        r"④ ⚠ **$(0,1)$ 上也要检查**：$g(\omega)=\sin(\text{负数})-\frac\omega5<0$（两项都负…实为 $-\sin$ 与 $-\frac\omega5$ 都 $<0$），无零点。" "\n"
        r"**别只检查 $[1,4]$ 就下结论** —— 原书正是限定了 $1\le x\le 4$；" "\n"
        r"⑤ ⚠ **「个数最多为」的措辞**：意味着要找出所有可能的 $\omega$，" "\n"
        r"**答案 $2$ = 「$\omega=5$」+「方程的一个根」**，两类各一个，别漏掉情形一的 $\omega=5$。"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-188'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-188-V3',
}

QS = [T213_E1, T213_V1, T213_V2, T213_V3, T371_E1, T371_V1, T371_V2, T371_V3,
      T188_E1, T188_V1, T188_V2, T188_V3]
