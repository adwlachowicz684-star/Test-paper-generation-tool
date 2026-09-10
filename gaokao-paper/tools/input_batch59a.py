# -*- coding: utf-8 -*-
r"""第59批（一）：用定义求离心率（8 题） 来源：2024高中数学热点题型归纳完整解析版.pdf p350（PDF 页 349）M-T-369 中点型｜p348（PDF 页 347）M-T-367 余弦定理2 ## ★★ 本批最重要的一条：别急着套二级结论，先把「定义」写出来 这 8 题看着花样繁多（中点、共圆、垂直、延长线、倾斜角），但**破题的第一步都一样**： $$|PF_{\text{远}}|-|PF_{\text{近}}|=2a\quad\text{（双曲线，同支）}$$ $$|PF_1|+|PF_2|=2a\quad\text{（椭圆）}$$ 把每个焦半径都写成「含一个未知量 + $\pm2a$」的形式，再结合几何条件列方程。 ## ★★ 两个反复出现的几何抓手 **1. 见到「$X$ 是 $AB$ 中点 + $|CA|=|CB|$」⟹ $CX\perp AB$**（等腰三角形三线合一） M-T-367-V1 与 M-T-369-V2 都靠它把「中点」翻译成「直角」。 **2. 见到「过焦点 $F_1$ 的直线交两支于 $A,B$」⟹ $F_1$ 未必在 $A,B$ 之间** - 若 $A$ 在左支、$B$ 在右支，从 $F_1(-c,0)$（$c>a$ 故 $-c<-a$）出发向右，**先遇左支后遇右支** ⟹ **$A,B$ 在 $F_1$ 同侧**，$|AB|=\bigl||BF_1|-|AF_1|\bigr|$。 - 我第一遍按「$F_1$ 在中间」算，得到 $|AB|=2d=d\sqrt2$ 的矛盾式 —— **这个矛盾本身就是提示**。 ## 八题验算 | 题 | 关键量 | 答案 | |---|---|---| | M-T-369-E1 | 点差法 + $M(-\frac{5c}6,\frac{\sqrt3c}6)$ ⟹ $2a^{2}=5c^{2}$ | $\frac{\sqrt{10}}5$ | | M-T-369-V1 | 共圆 ⟹ 等腰梯形 ⟹ $\lvert OM\rvert=\lvert AF\rvert$ ⟹ $c=2b$ | $\frac{2\sqrt3}3$ | | M-T-369-V2 | $\lvert AF_1\rvert=m=8a$，$\lvert BF_2\rvert=2a$，余弦定理 | $2$ | | M-T-369-V3 | 中垂线 ⟹ $\lvert PF_2\rvert=2c$，$a-c\le2c\le a+c$ | $\left[\frac13,1\right)$ | | M-T-367-E1 | 平行四边形 ⟹ 矩形，$m=\frac{4a}3$，$e^{2}=\frac{17}9$ | $\frac{\sqrt{17}}3$ | | M-T-367-V1 | 点积式 ⟹ $PF_2\perp PQ$，$\lvert PF_2\rvert=3a$、$\lvert PF_1\rvert=a$ | $\frac{\sqrt{10}}2$ | | M-T-367-V2 | $PF=2b$、$PF'=2a$，定义给 $b=2a$ | $\sqrt5$ | | M-T-367-V3 | $s_B-s_A=4a$，两个余弦定理消去 $s_A$ | $\sqrt2$ | """

T369_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知椭圆 $C:\dfrac{x^{2}}{a^{2}}+\dfrac{y^{2}}{b^{2}}=1\ (a>b>0)$ 的左焦点为 $F$，"
        r"过 $F$ 作倾斜角为 $60^\circ$ 的直线与椭圆 $C$ 交于 $A,B$ 两点，$M$ 为线段 $AB$ 的中点，"
        r"若 $\lvert OF\rvert=3\lvert FM\rvert$（$O$ 为坐标原点），则椭圆 $C$ 的离心率是（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac12$"),
        ('B', r"$\dfrac{\sqrt{10}}5$"),
        ('C', r"$\dfrac{\sqrt3}2$"),
        ('D', r"$\dfrac34$"),
    ],
    'answer': 'B',
    'analysis': (
        r"$F(-c,0)$，$\angle OFM=60^\circ$、$\lvert FM\rvert=\frac c3$ ⟹ $M\left(-\frac{5c}6,\frac{\sqrt3c}6\right)$。"
        r"再用点差法 $\frac{x_0}{a^{2}}+\sqrt3\frac{y_0}{b^{2}}=0$，得 $2a^{2}=5c^{2}$。"
    ),
    'solution': (
        r"**第一步：确定中点 $M$ 的坐标**" "\n"
        r"$F(-c,0)$，$O(0,0)$，$\lvert OF\rvert=c$，由 $\lvert OF\rvert=3\lvert FM\rvert$ 得 $\lvert FM\rvert=\dfrac c3$。" "\n"
        r"$\overrightarrow{FO}=(c,0)$ 指向 $+x$ 方向，直线 $AB$ 倾斜角 $60^\circ$，故 $\angle OFM=60^\circ$，" "\n"
        r"$\overrightarrow{FM}=\dfrac c3\left(\cos60^\circ,\sin60^\circ\right)=\left(\dfrac c6,\dfrac{\sqrt3c}6\right)$，" "\n"
        r"$M=F+\overrightarrow{FM}=\left(-c+\dfrac c6,\dfrac{\sqrt3c}6\right)=\left(-\dfrac{5c}6,\dfrac{\sqrt3c}6\right)$．" "\n"
        r"**第二步：点差法**" "\n"
        r"$A(x_1,y_1),B(x_2,y_2)$ 在椭圆上，两式相减：" "\n"
        r"$\dfrac{x_1^{2}-x_2^{2}}{a^{2}}+\dfrac{y_1^{2}-y_2^{2}}{b^{2}}=0 \Rightarrow\dfrac{(x_1+x_2)(x_1-x_2)}{a^{2}}+\dfrac{(y_1+y_2)(y_1-y_2)}{b^{2}}=0$．" "\n"
        r"由 $x_1+x_2=2x_0$、$y_1+y_2=2y_0$、$\dfrac{y_1-y_2}{x_1-x_2}=\tan60^\circ=\sqrt3$：" "\n"
        r"$\dfrac{x_0}{a^{2}}+\dfrac{\sqrt3\,y_0}{b^{2}}=0$．" "\n"
        r"**第三步：代入 $M$**" "\n"
        r"$\dfrac{-\frac{5c}6}{a^{2}}+\dfrac{\sqrt3\cdot\frac{\sqrt3c}6}{b^{2}}=0 \Rightarrow-\dfrac{5c}{6a^{2}}+\dfrac{3c}{6b^{2}}=0\Rightarrow\dfrac{3}{b^{2}}=\dfrac{5}{a^{2}}\Rightarrow3a^{2}=5b^{2}$．" "\n"
        r"由 $b^{2}=a^{2}-c^{2}$：$3a^{2}=5a^{2}-5c^{2}\Rightarrow5c^{2}=2a^{2}\Rightarrow e^{2}=\dfrac25$．" "\n"
        r"故 $e=\sqrt{\dfrac25}=\dfrac{\sqrt{10}}5$．选 B．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓。原书 p350 详解给出 $M\left(-\\frac{5c}6,\\frac{\\sqrt3 c}6\\right)$、" "\n"
        r"$\\frac{x_0}{a^{2}}+\\frac{\\sqrt3 y_0}{b^{2}}=0$、以及「$3a^{2}=5b^{2}$，即 $2a^{2}=5c^{2}$」" "\n"
        r"—— **与我的推导完全一致** ✓✓✓" "\n"
        r"**⚠ 一个差点踩的坑**：题干提取为「$OF = 3 FM$」，我一度怀疑 $3$ 是丢失的 $\\sqrt3$。" "\n"
        r"试按 $\\lvert FM\\rvert=\\frac{c}{\\sqrt3}$ 算：$M(-0.7113c,0.5c)$，点差法给 $\\frac{b^{2}}{a^{2}}=1.2176>1$，" "\n"
        r"**与椭圆 $a>b$ 矛盾** ⟹ 确定就是 $3$（无根号）。详见下方验算⑤。" "\n"
        r"**独立验算**：" "\n"
        r"① **$M$ 坐标**：$\\lvert FM\\rvert=c/3$，方向 $60^\\circ$ ⟹ $\\vec{FM}=(\\frac{c}{6},\\frac{\\sqrt3 c}{6})$ ✓✓" "\n"
        r"$M=(-c+\\frac c6,\\frac{\\sqrt3 c}{6})=(-\\frac{5c}6,\\frac{\\sqrt3 c}{6})$ ✓✓✓ **与原书一致**" "\n"
        r"② **点差法**：$2x_0\\frac{x_1-x_2}{a^2}+2y_0\\frac{y_1-y_2}{b^2}=0$，除以 $x_1-x_2$ 得 $\\frac{x_0}{a^2}+\\frac{y_0}{b^2}\\sqrt3=0$ ✓✓" "\n"
        r"③ **代入**：$-\\frac{5c}{6a^2}+\\frac{3c}{6b^2}=0\\Rightarrow\\frac{3}{b^2}=\\frac{5}{a^2}\\Rightarrow3a^2=5b^2$ ✓✓✓" "\n"
        r"④ **离心率**：$b^2=a^2-c^2\\Rightarrow3a^2=5a^2-5c^2\\Rightarrow5c^2=2a^2\\Rightarrowe^2=\\frac25$ ✓" "\n"
        r"$e=\\sqrt{0.4}=0.63246=\\frac{\\sqrt{10}}5$ ✓✓✓ **恰为选项 B**" "\n"
        r"⑤ **数值反推验证**（确认题干是 $3$ 不是 $\\sqrt3$）：" "\n"
        r"取 $a=1,e=\\frac{\\sqrt{10}}5$ 则 $c=0.63246,b^2=0.6$。由点差法与直线方程联立：" "\n"
        r"$x_0=-0.52705$、$y_0=0.18258$，$\\lvert FM\\rvert=\\sqrt{(x_0+c)^2+y_0^2}=0.21085$" "\n"
        r"$\\frac{\\lvert OF\\rvert}{\\lvert FM\\rvert}=\\frac{0.63246}{0.21085}=3.000$ ✓✓✓ **恰好等于 $3$**" "\n"
        r"而若 $\\lvert FM\\rvert=c/\\sqrt3=0.3652$，则 $M=(-0.2673c...)$，与点差法不相容 ⟹ **确定是 $3$**" "\n"
        r"⑥ **排除其他**：A $=0.5$、C $=0.866$、D $=0.75$ ✗" "\n"
        r"**答案 B（$\\frac{\\sqrt{10}}5$）正确** ✓" "\n"
        r"**⭐ 通法（中点型 ⟹ 点差法）**：" "\n"
        r"① ⭐ **见到「弦中点」就用点差法**：$\\frac{x_0}{a^{2}}+\\frac{y_0}{b^{2}}\\cdot k=0$（椭圆，斜率 $k$）；" "\n"
        r"双曲线把 $b^{2}$ 前的加号改减号；" "\n"
        r"② ⭐ **中点的坐标要自己算**，别指望题面给：本题用 $\\lvert OF\\rvert=3\\lvert FM\\rvert$ + 倾斜角定出 $M$；" "\n"
        r"③ ⚠ **提取文本里的「$3$」不要想当然补根号** —— 用「补了以后是否与 $a>b$ 矛盾」来判定，" "\n"
        r"这比猜快而且可靠（本题就是这么排除 $\\sqrt3$ 的）；" "\n"
        r"④ 点差法得到 $a,b$ 关系后，用 $b^{2}=a^{2}-c^{2}$ 转成 $a,c$ 关系即可出 $e$。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-369'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-369-E1',
}

T369_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知 $O$ 为坐标原点，双曲线 $C:\dfrac{x^{2}}{a^{2}}-\dfrac{y^{2}}{b^{2}}=1\ (a>0,b>0)$ 的右焦点为 $F(c,0)$，"
        r"直线 $x=c$ 与双曲线 $C$ 的渐近线交于 $A,B$ 两点，其中 $M$ 为线段 $OB$ 的中点．"
        r"$O,A,F,M$ 四点共圆，则双曲线 $C$ 的离心率为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac{2\sqrt3}3$"),
        ('B', r"$\sqrt2$"),
        ('C', r"$\sqrt3$"),
        ('D', r"$2$"),
    ],
    'answer': 'A',
    'analysis': (
        r"$A\left(c,\frac{bc}a\right)$、$B\left(c,-\frac{bc}a\right)$、$M\left(\frac c2,-\frac{bc}{2a}\right)$。"
        r"$MF\parallel OA$ ⟹ $OAMF$ 是梯形；四点共圆 ⟹ 圆内接梯形为等腰梯形 ⟹ $\lvert OM\rvert=\lvert AF\rvert$ ⟹ $c=2b$。"
    ),
    'solution': (
        r"**第一步：写出各点坐标**" "\n"
        r"渐近线 $y=\pm\dfrac ba x$，与 $x=c$ 交于 $A\left(c,\dfrac{bc}a\right)$、$B\left(c,-\dfrac{bc}a\right)$．" "\n"
        r"$M$ 为 $OB$ 中点：$M\left(\dfrac c2,-\dfrac{bc}{2a}\right)$．$F(c,0)$，$O(0,0)$．" "\n"
        r"**第二步：判定四边形形状**" "\n"
        r"$\overrightarrow{MF}=\left(\dfrac c2,\dfrac{bc}{2a}\right)$，$\overrightarrow{OA}=\left(c,\dfrac{bc}a\right)=2\overrightarrow{MF}$，" "\n"
        r"故 $MF\parallel OA$ 且 $\lvert OA\rvert=2\lvert MF\rvert$，四边形 $OAMF$ 是**梯形**．" "\n"
        r"**第三步：共圆 ⟹ 等腰梯形**" "\n"
        r"圆内接四边形对角互补，梯形已有同旁内角互补，故只能是**等腰梯形**，两腰相等：$\lvert OM\rvert=\lvert AF\rvert$．" "\n"
        r"**第四步：算长度**" "\n"
        r"$\lvert AF\rvert=\dfrac{bc}a$（$A$ 在 $F$ 正上方）；" "\n"
        r"$\lvert OM\rvert^{2}=\left(\dfrac c2\right)^{2}+\left(\dfrac{bc}{2a}\right)^{2} =\dfrac{c^{2}}{4}\left(1+\dfrac{b^{2}}{a^{2}}\right)=\dfrac{c^{2}}4\cdot\dfrac{c^{2}}{a^{2}}=\dfrac{c^{4}}{4a^{2}}$，" "\n"
        r"$\lvert OM\rvert=\dfrac{c^{2}}{2a}$．" "\n"
        r"由 $\lvert OM\rvert=\lvert AF\rvert$：$\dfrac{c^{2}}{2a}=\dfrac{bc}a\Rightarrow\dfrac c2=b\Rightarrow c=2b$．" "\n"
        r"**第五步：求离心率**" "\n"
        r"$c^{2}=4b^{2}=4(c^{2}-a^{2})\Rightarrow c^{2}=4c^{2}-4a^{2}\Rightarrow4a^{2}=3c^{2}\Rightarrow e^{2}=\dfrac43$，" "\n"
        r"$e=\dfrac{2}{\sqrt3}=\dfrac{2\sqrt3}3$．选 A．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓。原书 p350 详解：" "\n"
        r"「$O$、$A$、$F$、$M$ 四点共圆，可知四边形 $OAMF$ 为等腰梯形，$\\therefore\\lvert OM\\rvert=\\lvert AF\\rvert$，" "\n"
        r"即 $\\ldots a^{2}=3b^{2}$，$e=\\ldots=\\frac{2\\sqrt3}{3}$，故选 A」**与我的推导一致** ✓✓" "\n"
        r"（原书末步写 $a^2=3b^2$：由 $c=2b$ 得 $c^2=4b^2$，又 $c^2=a^2+b^2$ ⟹ $a^2+b^2=4b^2$ ⟹ $a^2=3b^2$ ✓✓）" "\n"
        r"**独立验算**：" "\n"
        r"① **$A,B$**：$x=c$ 代渐近线 $y=\\pm\\frac ba x$ ⟹ $y=\\pm\\frac{bc}a$ ✓✓" "\n"
        r"② **$M$**：$OB$ 中点 $=(\\frac c2,-\\frac{bc}{2a})$ ✓✓" "\n"
        r"③ **$\\vec{MF}=(c-\\frac c2,0+\\frac{bc}{2a})=(\\frac c2,\\frac{bc}{2a})$** ✓；$\\vec{OA}=(c,\\frac{bc}{a})=2\\vec{MF}$ ✓✓ **确为梯形**" "\n"
        r"④ **$\\lvert OM\\rvert$**：$(\\frac c2)^2+(\\frac{bc}{2a})^2=\\frac{c^2}{4}(1+\\frac{b^2}{a^2})=\\frac{c^2}{4}\\cdot\\frac{a^2+b^2}{a^2}=\\frac{c^2}{4}\\cdot\\frac{c^2}{a^2}=\\frac{c^4}{4a^2}$ ✓✓✓" "\n"
        r"$\\lvert OM\\rvert=\\frac{c^2}{2a}$ ✓✓" "\n"
        r"⑤ **$\\lvert AF\\rvert=\\frac{bc}{a}$** ✓（$A$ 与 $F$ 同横坐标 $c$）" "\n"
        r"⑥ **$c=2b$**：$\\frac{c^2}{2a}=\\frac{bc}{a}\\Rightarrow\\frac c2=b$ ✓✓✓" "\n"
        r"⑦ **$e$**：$c^2=4(c^2-a^2)\\Rightarrow3c^2=4a^2\\Rightarrowe^2=\\frac43$，$e=1.15470$" "\n"
        r"$\\frac{2\\sqrt3}3=\\frac{3.4641}3=1.15470$ ✓✓✓ **恰为选项 A**" "\n"
        r"⑧ **数值构造检验**：取 $b=1$ 则 $c=2$、$a^2=3$、$a=1.7321$，$e=\\frac{2}{1.7321}=1.1547$ ✓" "\n"
        r"$A=(2,\\frac{1\\cdot2}{1.7321})=(2,1.1547)$，$M=(1,-0.5774)$" "\n"
        r"$\\lvert AF\\rvert=1.1547$ ✓；$\\lvert OM\\rvert=\\sqrt{1+0.3333}=\\sqrt{1.3333}=1.1547$ ✓✓ **相等**" "\n"
        r"⑨ **排除其他**：B $=\\sqrt2=1.414$、C $=\\sqrt3=1.732$、D $=2$ ✗" "\n"
        r"**答案 A（$\\frac{2\\sqrt3}3$）正确** ✓" "\n"
        r"**⭐ 通法（四点共圆 + 梯形）**：" "\n"
        r"① ⭐⭐ **「梯形 + 四点共圆」⟹ 等腰梯形** —— 圆内接四边形对角互补，而梯形同旁内角本就互补，" "\n"
        r"两条件叠加只能是等腰梯形，于是**两腰相等**（本题 $\\lvert OM\\rvert=\\lvert AF\\rvert$）；" "\n"
        r"② 判梯形只需证一组对边平行：用**向量倍数**最快（$\\vec{OA}=2\\vec{MF}$）；" "\n"
        r"③ ⭐ **双曲线中 $\\lvert OM\\rvert$ 这类长度常可化简**：$1+\\frac{b^2}{a^2}=\\frac{c^2}{a^2}$ 是关键代换；" "\n"
        r"④ 得到 $c=2b$ 后，$c^2=a^2+b^2$ 两边写法要灵活（$c^2=4b^2\\Rightarrow a^2=3b^2$ 更顺）。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-369'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-369-V1',
}

T369_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知双曲线 $C:\dfrac{x^{2}}{a^{2}}-\dfrac{y^{2}}{b^{2}}=1\ (a>0,b>0)$ 的左、右焦点分别为 $F_1,F_2$，"
        r"过 $F_2$ 的直线 $l$ 交双曲线的右支于 $A,B$ 两点．点 $M$ 为线段 $BF_1$ 的中点，且 $\lvert AF_1\rvert=\lvert AB\rvert$．"
        r"若 $\cos\angle AF_1B=\dfrac14$，则双曲线 $C$ 的离心率是（　　）"
    ),
    'opts': [
        ('A', r"$2$"),
        ('B', r"$\sqrt5$"),
        ('C', r"$\dfrac{\sqrt5}2$"),
        ('D', r"$\sqrt3$"),
    ],
    'answer': 'A',
    'analysis': (
        r"$M$ 为 $BF_1$ 中点且 $\lvert AF_1\rvert=\lvert AB\rvert$ ⟹ $AM\perp BF_1$。设 $\lvert AF_1\rvert=m$，"
        r"则 $\lvert F_1M\rvert=\frac m4$、$\lvert BF_1\rvert=\frac m2$。由 $A,B$ 在右支用定义得 $m=8a$。"
    ),
    'solution': (
        r"**第一步：把「中点 + 等腰」翻译成直角**" "\n"
        r"在 $\triangle ABF_1$ 中，$M$ 是 $BF_1$ 的中点，且 $\lvert AF_1\rvert=\lvert AB\rvert$（等腰），" "\n"
        r"故 $AM\perp BF_1$（三线合一），$\triangle AMF_1$ 为直角三角形．" "\n"
        r"**第二步：用 $\cos$ 表示各段**" "\n"
        r"设 $\lvert AF_1\rvert=m$，则 $\lvert AB\rvert=m$。在 Rt$\triangle AMF_1$ 中 $\angle AF_1M=\angle AF_1B$，" "\n"
        r"$\cos\angle AF_1M=\dfrac{\lvert F_1M\rvert}{\lvert AF_1\rvert}=\dfrac14\Rightarrow\lvert F_1M\rvert=\dfrac m4$，" "\n"
        r"$\lvert BF_1\rvert=2\lvert F_1M\rvert=\dfrac m2$．" "\n"
        r"**第三步：用双曲线定义求 $m$**" "\n"
        r"$A,B$ 均在右支：$\lvert AF_1\rvert-\lvert AF_2\rvert=2a$，$\lvert BF_1\rvert-\lvert BF_2\rvert=2a$，" "\n"
        r"$\Rightarrow\lvert AF_2\rvert=m-2a$，$\lvert BF_2\rvert=\dfrac m2-2a$．" "\n"
        r"$A,F_2,B$ 共线且 $F_2$ 在 $A,B$ 之间：$\lvert AB\rvert=\lvert AF_2\rvert+\lvert BF_2\rvert$" "\n"
        r"$\Rightarrow m=(m-2a)+\left(\dfrac m2-2a\right)=\dfrac{3m}2-4a\Rightarrow\dfrac m2=4a\Rightarrow m=8a$．" "\n"
        r"于是 $\lvert BF_1\rvert=4a$，$\lvert BF_2\rvert=4a-2a=2a$．" "\n"
        r"**第四步：在 $\triangle BF_1F_2$ 中用余弦定理**" "\n"
        r"$\triangle ABF_1$ 中 $\lvert AF_1\rvert=\lvert AB\rvert=m$ ⟹ $\angle ABF_1=\angle AF_1B$，" "\n"
        r"又 $A,F_2,B$ 共线 ⟹ $\angle F_1BF_2=\angle ABF_1$，故 $\cos\angle F_1BF_2=\dfrac14$．" "\n"
        r"$\dfrac{\lvert BF_1\rvert^{2}+\lvert BF_2\rvert^{2}-\lvert F_1F_2\rvert^{2}}{2\lvert BF_1\rvert\lvert BF_2\rvert} =\dfrac{16a^{2}+4a^{2}-4c^{2}}{2\cdot4a\cdot2a}=\dfrac14$" "\n"
        r"$\Rightarrow20a^{2}-4c^{2}=4a^{2}\Rightarrow4c^{2}=16a^{2}\Rightarrow c^{2}=4a^{2}\Rightarrow e=2$．选 A．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓。原书 p350 详解：" "\n"
        r"「点 $M$ 为线段 $BF_1$ 的中点，且 $AF_1=AB$，则 $AM\\perp BF_1$…设 $\\lvert AF_1\\rvert=m$，则 $\\lvert AB\\rvert=m$…" "\n"
        r"$\\lvert FM\\rvert=\\frac m4$，$\\lvert FB\\rvert=\\frac m2$…$m=8a$，$\\lvert BF_2\\rvert=2a$…$c^{2}=4a^{2}$，" "\n"
        r"$\\therefore$ 离心率 $e=2$。**故选 A**」**与我的推导完全一致** ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **三线合一**：$M$ 是 $BF_1$ 中点 + $AF_1=AB$ ⟹ $AM\\perp BF_1$ ✓✓" "\n"
        r"② **$\\lvert F_1M\\rvert$**：Rt$\\triangle AMF_1$ 中 $\\cos\\angle AF_1M=\\frac{F_1M}{AF_1}=\\frac14$ ⟹ $F_1M=\\frac m4$ ✓✓" "\n"
        r"③ **$\\lvert BF_1\\rvert=2F_1M=\\frac m2$** ✓✓" "\n"
        r"④ **$m=8a$**：$m=(m-2a)+(\\frac m2-2a)=\\frac{3m}{2}-4a\\Rightarrow\\frac m2=4a\\Rightarrowm=8a$ ✓✓✓" "\n"
        r"**与原书「$m=8a$」一致** ✓" "\n"
        r"⑤ **$\\lvert BF_1\\rvert=4a$、$\\lvert BF_2\\rvert=4a-2a=2a$** ✓✓ **与原书「$BF_2=2a$」一致** ✓" "\n"
        r"⑥ **余弦定理**：$\\frac{16a^2+4a^2-4c^2}{2\\cdot4a\\cdot2a}=\\frac{20a^2-4c^2}{16a^2}=\\frac14$" "\n"
        r"$\\Rightarrow20a^2-4c^2=4a^2\\Rightarrow16a^2=4c^2\\Rightarrowc^2=4a^2\\Rightarrowe=2$ ✓✓✓" "\n"
        r"⑦ **角度传递验证**：$\\triangle ABF_1$ 等腰（$AF_1=AB$）⟹ 底角 $\\angle ABF_1=\\angle AF_1B$ ✓" "\n"
        r"$A,F_2,B$ 共线 ⟹ $\\angle F_1BF_2$ 与 $\\angle ABF_1$ 是同一角 ✓✓" "\n"
        r"⑧ **合理性**：$e=2>1$ ✓；$\\lvert AF_2\\rvert=m-2a=6a>0$ ✓；$\\lvert BF_2\\rvert=2a>0$ ✓" "\n"
        r"⑨ **排除其他**：B $=\\sqrt5=2.236$、C $=\\frac{\\sqrt5}2=1.118$、D $=\\sqrt3=1.732$ ✗" "\n"
        r"**答案 A（$2$）正确** ✓" "\n"
        r"**⭐ 通法（中点 + 等腰 = 直角）**：" "\n"
        r"① ⭐⭐ **「$M$ 是 $XY$ 中点」+「$\\lvert PX\\rvert=\\lvert PY\\rvert$」⟹ $PM\\perp XY$** —— " "\n"
        r"这是把「中点」条件变现的**标准动作**，本题与 M-T-367-V1 都靠它；" "\n"
        r"② 有了直角就能用 $\\cos$ 把各段**用一个未知量 $m$ 表示**，再统一用定义消元；" "\n"
        r"③ ⭐ **双曲线同一支上两点 $A,B$ 且直线过焦点**：$F_2$ 必在 $A,B$ 之间，" "\n"
        r"故 $\\lvert AB\\rvert=\\lvert AF_2\\rvert+\\lvert BF_2\\rvert$（**加**），这是列方程的关键；" "\n"
        r"④ 最后一步余弦定理中，$\\angle F_1BF_2$ 要通过「等腰底角 + 共线」两步传递到已知角。"
    ),
    'difficulty': 0.93,
    'topics': ['M-T-369'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-369-V2',
}

T369_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知 $F_1,F_2$ 分别是椭圆 $C:\dfrac{x^{2}}{a^{2}}+\dfrac{y^{2}}{b^{2}}=1\ (a>b>0)$ 的左、右焦点．"
        r"若椭圆 $C$ 上存在点 $P$，使得线段 $PF_1$ 的垂直平分线恰好经过焦点 $F_2$，"
        r"则椭圆 $C$ 的离心率的取值范围是（　　）"
    ),
    'opts': [
        ('A', r"$\left[\dfrac23,1\right)$"),
        ('B', r"$\left[\dfrac{\sqrt3}3,\dfrac{\sqrt2}2\right]$"),
        ('C', r"$\left[\dfrac13,1\right)$"),
        ('D', r"$\left(0,\dfrac13\right]$"),
    ],
    'answer': 'C',
    'analysis': (
        r"中垂线的性质：$P$ 在 $PF_1$ 的中垂线上 ⟹ $\lvert PF_2\rvert=\lvert F_1F_2\rvert=2c$。"
        r"而 $\lvert PF_2\rvert\in[a-c,a+c]$（$P$ 在左顶点时最大、右顶点时最小），故 $a-c\le2c\le a+c$。"
    ),
    'solution': (
        r"**第一步：翻译「中垂线」**" "\n"
        r"$F_2$ 在线段 $PF_1$ 的垂直平分线上 ⟹ $\lvert F_2P\rvert=\lvert F_2F_1\rvert=2c$．" "\n"
        r"**第二步：$\lvert PF_2\rvert$ 的取值范围**" "\n"
        r"$P$ 在椭圆上运动时，$\lvert PF_2\rvert=a-ex_P$，而 $x_P\in[-a,a]$。" "\n"
        r"当 $P$ 为左顶点 $(-a,0)$ 时最大：$\lvert PF_2\rvert=a+c$；" "\n"
        r"当 $P$ 为右顶点 $(a,0)$ 时最小：$\lvert PF_2\rvert=a-c$．" "\n"
        r"即 $\lvert PF_2\rvert\in[a-c,\ a+c]$．" "\n"
        r"**第三步：存在性条件**" "\n"
        r"要存在 $P$ 使 $\lvert PF_2\rvert=2c$，需 $2c$ 落在上述区间内：" "\n"
        r"$a-c\le2c\le a+c$．" "\n"
        r"右半：$2c\le a+c\Rightarrow c\le a$，即 $e\le1$（对椭圆恒成立）；" "\n"
        r"左半：$a-c\le2c\Rightarrow a\le3c\Rightarrow e=\dfrac ca\ge\dfrac13$．" "\n"
        r"结合椭圆 $e<1$：$e\in\left[\dfrac13,1\right)$．选 C．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓。原书 p350 详解：" "\n"
        r"「因为线段 $PF_1$ 的垂直平分线恰好经过焦点 $F_2$，所以 $\\lvert PF_2\\rvert=\\lvert F_1F_2\\rvert=2c$，" "\n"
        r"当点 $P$ 位于椭圆的左顶点时，$\\lvert PF_2\\rvert$ 最大为 $a+c$；当点 $P$ 位于椭圆的右顶点时，$\\lvert PF_2\\rvert$ 最小为 $a-c$；" "\n"
        r"所以 $a-c\\le\\lvert PF_2\\rvert=2c\\lea+c$，可得 $c\\lea\\le3c$，所以 $e\\in[\\frac13,1)$」" "\n"
        r"—— **与我的推导完全一致** ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① ⭐ **中垂线性质**：$F_2$ 在 $PF_1$ 中垂线上 ⟹ $\\lvert F_2P\\rvert=\\lvert F_2F_1\\rvert$ ✓✓✓" "\n"
        r"$\\lvert F_1F_2\\rvert=2c$ ✓✓" "\n"
        r"② **$\\lvert PF_2\\rvert$ 范围**：焦半径公式 $\\lvert PF_2\\rvert=a-ex_P$，$x_P\\in[-a,a]$" "\n"
        r"$x_P=-a$：$a+ea=a+c$ ✓（最大）；$x_P=a$：$a-c$ ✓（最小）✓✓✓" "\n"
        r"③ **左半不等式**：$a-c\\le2c\\Rightarrowa\\le3c\\Rightarrowe\\ge\\frac13$ ✓✓✓" "\n"
        r"④ **右半不等式**：$2c\\lea+c\\Rightarrowc\\lea\\Rightarrowe\\le1$ ✓（椭圆本就 $e<1$，不产生新约束）" "\n"
        r"⑤ **端点可达性**：$e=\\frac13$ 时 $a=3c$，$2c=a-c$ 恰为最小值（$P$ 为右顶点）✓ **可取** ⟹ 左端闭 ✓" "\n"
        r"⑥ **数值检验**：取 $a=3,c=1$（$e=\\frac13$）：$\\lvert PF_2\\rvert$ 范围 $[2,4]$，$2c=2$ ✓ 恰在下界，存在 ✓" "\n"
        r"取 $a=1.5,c=1$（$e=\\frac23>\\frac13$）：范围 $[0.5,2.5]$，$2c=2$ ✓ 存在 ✓" "\n"
        r"取 $a=4,c=1$（$e=\\frac14<\\frac13$）：范围 $[3,5]$，$2c=2<3$ ✗ **不存在** ✓✓ **确认下界 $\\frac13$**" "\n"
        r"⑦ **排除其他**：A $[\\frac23,1)$ 下界过大；B 是闭区间且上界 $\\frac{\\sqrt2}2<1$（漏了 $e$ 接近 $1$ 的部分）；" "\n"
        r"D $(0,\\frac13]$ 方向完全反了 ✗✗" "\n"
        r"**答案 C（$[\\frac13,1)$）正确** ✓" "\n"
        r"**⭐ 通法（中垂线 + 存在性）**：" "\n"
        r"① ⭐⭐ **「$Q$ 在 $AB$ 的中垂线上」⟹ $\\lvert QA\\rvert=\\lvert QB\\rvert$** —— 中垂线的定义就是到两端等距；" "\n"
        r"② ⭐ **「存在点 $P$ 使 $\\lvert PF\\rvert=k$」⟹ $k$ 落在 $\\lvert PF\\rvert$ 的值域内** —— " "\n"
        r"先求值域再判存在，比解方程快得多（与 M-T-373-E1 同思路）；" "\n"
        r"③ 椭圆焦半径值域：$\\lvert PF_2\\rvert\\in[a-c,a+c]$（**左顶点最大、右顶点最小**，别记反）；" "\n"
        r"④ ⚠ **端点是否取到**：本题 $e=\\frac13$ 时 $P$ 恰为右顶点，可取 ⟹ 左端闭；" "\n"
        r"⑤ 椭圆 $e<1$ 恒成立，所以「$\\le1$」这类约束通常不产生新信息，别被干扰。"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-369'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-369-V3',
}

T367_E1 = {
    'type': '选择',
    'stem_text': (
        r"如图，$O$ 是坐标原点，$P$ 是双曲线 $E:\dfrac{x^{2}}{a^{2}}-\dfrac{y^{2}}{b^{2}}=1\ (a>0,b>0)$ 右支上的一点，"
        r"$F$ 是 $E$ 的右焦点，延长 $PO,PF$ 分别交 $E$ 于 $Q,R$ 两点，"
        r"已知 $QF\perp FR$，且 $\lvert QF\rvert=2\lvert FR\rvert$，则 $E$ 的离心率为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac{\sqrt{17}}4$"),
        ('B', r"$\dfrac{\sqrt{17}}3$"),
        ('C', r"$\dfrac{\sqrt{21}}4$"),
        ('D', r"$\dfrac{\sqrt{21}}3$"),
    ],
    'answer': 'B',
    'analysis': (
        r"$O$ 是 $PQ$ 中点且是 $FF'$ 中点（$F'$ 为左焦点）⟹ $PFQF'$ 是平行四边形；$QF\perp FR$ ⟹ 它是矩形。"
        r"设 $\lvert FR\rvert=m$，则 $\lvert PF'\rvert=\lvert QF\rvert=2m$，$\lvert PF\rvert=2m-2a$，$\lvert RF'\rvert=m+2a$，$\lvert PR\rvert=3m-2a$。"
        r"在 Rt$\triangle F'PR$ 中得 $m=\frac{4a}3$，再在 Rt$\triangle F'PF$ 中得 $e=\frac{\sqrt{17}}3$。"
    ),
    'solution': (
        r"**第一步：补出左焦点，识别平行四边形**" "\n"
        r"设左焦点为 $F'$。$O$ 是 $FF'$ 的中点，又 $O$ 是 $PQ$ 的中点（$Q$ 在 $PO$ 延长线上），" "\n"
        r"故四边形 $PFQF'$ 的对角线互相平分 ⟹ 它是**平行四边形**．" "\n"
        r"**第二步：平行四边形 ⟹ 矩形**" "\n"
        r"$QF\perp FR$，而 $R$ 在 $PF$ 的延长线上（$P,F,R$ 共线），故 $QF\perp PF$。" "\n"
        r"平行四边形中有一个直角 ⟹ $PFQF'$ 是**矩形**，$\lvert PF'\rvert=\lvert QF\rvert$，$\lvert PF\rvert=\lvert QF'\rvert$．" "\n"
        r"**第三步：用定义表示各段**" "\n"
        r"设 $\lvert FR\rvert=m$，则 $\lvert QF\rvert=2m$，故 $\lvert PF'\rvert=2m$．" "\n"
        r"$P$ 在右支：$\lvert PF'\rvert-\lvert PF\rvert=2a\Rightarrow\lvert PF\rvert=2m-2a$．" "\n"
        r"$\lvert PR\rvert=\lvert PF\rvert+\lvert FR\rvert=(2m-2a)+m=3m-2a$．" "\n"
        r"$R$ 在左支（因为 $\lvert RF'\rvert>\lvert RF\rvert$）：$\lvert RF'\rvert-\lvert RF\rvert=2a\Rightarrow\lvert RF'\rvert=m+2a$．" "\n"
        r"**第四步：Rt$\triangle F'PR$（直角在 $P$）**" "\n"
        r"$\lvert PF'\rvert^{2}+\lvert PR\rvert^{2}=\lvert RF'\rvert^{2}$：" "\n"
        r"$(2m)^{2}+(3m-2a)^{2}=(m+2a)^{2}$" "\n"
        r"$4m^{2}+9m^{2}-12am+4a^{2}=m^{2}+4am+4a^{2}$" "\n"
        r"$12m^{2}-16am=0\Rightarrow4m(3m-4a)=0\Rightarrow m=\dfrac{4a}3$．" "\n"
        r"**第五步：Rt$\triangle F'PF$（直角在 $P$）**" "\n"
        r"$\lvert PF'\rvert=2m=\dfrac{8a}3$，$\lvert PF\rvert=2m-2a=\dfrac{2a}3$．" "\n"
        r"$\left(\dfrac{8a}3\right)^{2}+\left(\dfrac{2a}3\right)^{2}=(2c)^{2}\Rightarrow\dfrac{64a^{2}+4a^{2}}9=4c^{2} \Rightarrow\dfrac{68a^{2}}9=4c^{2}\Rightarrow c^{2}=\dfrac{17a^{2}}9$．" "\n"
        r"$e=\dfrac ca=\dfrac{\sqrt{17}}3$．选 B．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓。原书 p348 详解：" "\n"
        r"「由对称性可知，点 $O$ 是线段 $PQ$ 中点，则四边形 $PFQF'$ 是平行四边形，而 $QF\\perp FR$，" "\n"
        r"于是有 $\\square PFQF'$ 是矩形，设 $\\lvert FR\\rvert=m$，则 $\\lvert PF'\\rvert=\\lvert FQ\\rvert=2m$，" "\n"
        r"$\\lvert PF\\rvert=2m-2a$，$\\lvert RF'\\rvert=m+2a$，$\\lvert PR\\rvert=3m-2a$」" "\n"
        r"—— **与我的四个表达式完全一致** ✓✓✓" "\n"
        r"**⚠ 选项还原**：原文提取为 `174 173 214 213`（根号丢失），按" "\n"
        r"A $\\frac{\\sqrt{17}}4$、B $\\frac{\\sqrt{17}}3$、C $\\frac{\\sqrt{21}}4$、D $\\frac{\\sqrt{21}}3$ 还原，" "\n"
        r"**依据是我的推导给出 $\\frac{\\sqrt{17}}3$ 且答案为 B**。" "\n"
        r"**独立验算**：" "\n"
        r"① **平行四边形**：$O$ 是 $PQ$ 中点 ✓、$O$ 是 $FF'$ 中点 ✓ ⟹ 对角线互相平分 ✓✓" "\n"
        r"② **矩形**：$QF\\perp FR$ 且 $P,F,R$ 共线 ⟹ $QF\\perp PF$ ✓✓⟹ 有一个直角的平行四边形是矩形 ✓" "\n"
        r"③ **矩形对边**：$\\lvert PF'\\rvert=\\lvert QF\\rvert=2m$ ✓✓" "\n"
        r"④ **$\\lvert PF\\rvert=2m-2a$**：$P$ 在右支 ⟹ $\\lvert PF'\\rvert-\\lvert PF\\rvert=2a$ ✓✓✓" "\n"
        r"（⚠ 我第一遍写成 $\\lvert PF\\rvert=\\lvert PF'\\rvert+2a$，**方向搞反了** —— 右支点离右焦点近，$\\lvert PF'\\rvert>\\lvert PF\\rvert$）" "\n"
        r"⑤ **$\\lvert RF'\\rvert=m+2a$**：$R$ 在左支 ⟹ $\\lvert RF'\\rvert-\\lvert RF\\rvert=2a$ ✓✓" "\n"
        r"⑥ **求 $m$**：$4m^2+9m^2-12am+4a^2=m^2+4am+4a^2\\Rightarrow12m^2=16am\\Rightarrowm=\\frac{4a}3$ ✓✓✓" "\n"
        r"⑦ **$\\lvert PF'\\rvert=\\frac{8a}3$、$\\lvert PF\\rvert=\\frac{8a}3-\\frac{6a}3=\\frac{2a}3$** ✓✓" "\n"
        r"⑧ **$e$**：$\\frac{64a^2+4a^2}{9}=4c^2\\Rightarrow\\frac{68}{9}a^2=4c^2\\Rightarrowc^2=\\frac{17}{9}a^2\\Rightarrowe=\\frac{\\sqrt{17}}3=1.37437$ ✓✓✓ **恰为选项 B**" "\n"
        r"⑨ **合理性检验**：$\\lvert PF\\rvert=\\frac{2a}3>0$ ✓；$m=\\frac{4a}3$ ⟹ $\\lvert FR\\rvert=\\frac{4a}3>0$ ✓" "\n"
        r"**答案 B（$\\frac{\\sqrt{17}}3$）正确** ✓" "\n"
        r"**⭐ 通法（延长线过中心/焦点）**：" "\n"
        r"① ⭐⭐ **见到「延长 $PO$（$O$ 为中心）交曲线于 $Q$」⟹ $O$ 是 $PQ$ 中点** ⟹ 补上另一焦点 $F'$，" "\n"
        r"立刻得到平行四边形（对角线互相平分）；" "\n"
        r"② 平行四边形 + 一个直角 ⟹ **矩形** ⟹ 对边相等，把 $\\lvert PF'\\rvert$ 换成 $\\lvert QF\\rvert$；" "\n"
        r"③ ⚠ **双曲线定义的方向**（高频错点）：" "\n"
        r"右支点：$\\lvert PF_{\\text{左}}\\rvert-\\lvert PF_{\\text{右}}\\rvert=2a$（**离右焦点近**）；" "\n"
        r"左支点：$\\lvert PF_{\\text{右}}\\rvert-\\lvert PF_{\\text{左}}\\rvert=2a$。" "\n"
        r"即「远的 $-$ 近的 $=2a$」，别死记「左减右」；" "\n"
        r"④ 全部用 $m$ 表示后，在两个直角三角形中**先求 $m$ 再求 $e$**，顺序不能反。"
    ),
    'difficulty': 0.95,
    'topics': ['M-T-367'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-367-E1',
}

T367_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知双曲线 $C:\dfrac{x^{2}}{a^{2}}-\dfrac{y^{2}}{b^{2}}=1\ (a>0,b>0)$ 的左、右焦点分别为 $F_1,F_2$，"
        r"过 $F_1$ 的直线交双曲线 $C$ 的左支于 $P,Q$ 两点，若 $\lvert PF_2\rvert^{2}=\overrightarrow{PF_2}\cdot\overrightarrow{QF_2}$，"
        r"且 $\triangle PQF_2$ 的周长为 $12a$，则双曲线 $C$ 的离心率为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac{\sqrt{10}}2$"),
        ('B', r"$\sqrt3$"),
        ('C', r"$\sqrt5$"),
        ('D', r"$2\sqrt2$"),
    ],
    'answer': 'A',
    'analysis': (
        r"点积式化为 $\overrightarrow{PF_2}\cdot\overrightarrow{QP}=0$ ⟹ $PF_2\perp PQ$。周长条件给 $\lvert PF_1\rvert+\lvert QF_1\rvert=4a$；"
        r"勾股给 $\lvert QF_2\rvert^{2}-\lvert PF_2\rvert^{2}=16a^{2}$ ⟹ $\lvert QF_1\rvert-\lvert PF_1\rvert=2a$ ⟹ $\lvert PF_2\rvert=3a$、$\lvert PF_1\rvert=a$。"
    ),
    'solution': (
        r"**第一步：翻译向量条件**" "\n"
        r"$\lvert PF_2\rvert^{2}=\overrightarrow{PF_2}\cdot\overrightarrow{QF_2} \Rightarrow\overrightarrow{PF_2}\cdot\left(\overrightarrow{PF_2}-\overrightarrow{QF_2}\right)=0$．" "\n"
        r"而 $\overrightarrow{PF_2}-\overrightarrow{QF_2}=\overrightarrow{QP}$，故 $\overrightarrow{PF_2}\cdot\overrightarrow{QP}=0$，即 $PF_2\perp PQ$．" "\n"
        r"**第二步：用定义 + 周长**" "\n"
        r"$P,Q$ 同在左支：$\lvert PF_2\rvert-\lvert PF_1\rvert=2a$，$\lvert QF_2\rvert-\lvert QF_1\rvert=2a$．" "\n"
        r"记 $p=\lvert PF_1\rvert$、$q=\lvert QF_1\rvert$，则 $\lvert PQ\rvert=p+q$（$F_1$ 在 $P,Q$ 之间）．" "\n"
        r"周长 $=(p+2a)+(q+2a)+(p+q)=2(p+q)+4a=12a\Rightarrow p+q=4a$，$\lvert PQ\rvert=4a$．" "\n"
        r"**第三步：勾股定理**" "\n"
        r"$\lvert PF_2\rvert^{2}+\lvert PQ\rvert^{2}=\lvert QF_2\rvert^{2}\Rightarrow\lvert QF_2\rvert^{2}-\lvert PF_2\rvert^{2}=16a^{2}$．" "\n"
        r"$(q+2a)^{2}-(p+2a)^{2}=(q-p)(p+q+4a)=(q-p)\cdot8a=16a^{2}\Rightarrow q-p=2a$．" "\n"
        r"联立 $p+q=4a$ 得 $q=3a$、$p=a$．" "\n"
        r"**第四步：Rt$\triangle PF_1F_2$**" "\n"
        r"$\lvert PF_1\rvert=a$、$\lvert PF_2\rvert=p+2a=3a$，$\lvert F_1F_2\rvert=2c$：" "\n"
        r"$a^{2}+9a^{2}=4c^{2}\Rightarrow c^{2}=\dfrac{10a^{2}}4\Rightarrow e^{2}=\dfrac{10}4\Rightarrow e=\dfrac{\sqrt{10}}2$．选 A．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓。原书 p348 详解：" "\n"
        r"「由 $PF_2^{2}=\\overrightarrow{PF_2}\\cdot\\overrightarrow{QF_2}\\Rightarrow\\overrightarrow{PF_2}\\cdot(\\overrightarrow{PF_2}-\\overrightarrow{QF_2})=0" "\n"
        r"\\Rightarrow\\overrightarrow{PF_2}\\cdot\\overrightarrow{PQ}=0\\RightarrowPF_2\\perpPQ$，所以 $\\angle FPQ=90^\\circ$…" "\n"
        r"$\\triangle PQF_2$ 的周长 $=2(\\lvert PF_2\\rvert+\\lvert QF_2\\rvert)-4a=12a$…$\\lvert PQ\\rvert=4a$…" "\n"
        r"$\\lvert QF_2\\rvert-\\lvert PF_2\\rvert=2a$…$\\lvert PF_2\\rvert=3a$，$\\lvert PF_1\\rvert=a$…$e=\\frac{c}{a}=\\frac{\\sqrt{10}}{2}$。**故选 A**」" "\n"
        r"—— **与我的推导完全一致** ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **向量式**：$\\vec{PF_2}\\cdot\\vec{QF_2}=\\lvert PF_2\\rvert^2\\Rightarrow\\vec{PF_2}\\cdot(\\vec{QF_2}-\\vec{PF_2})=0$" "\n"
        r"$\\vec{QF_2}-\\vec{PF_2}=\\vec{P}-\\vec{Q}=\\vec{QP}$ ✓ ⟹ $\\vec{PF_2}\\cdot\\vec{QP}=0$ ⟹ 垂直 ✓✓✓" "\n"
        r"② **周长**：$\\lvert PF_2\\rvert+\\lvert QF_2\\rvert+\\lvert PQ\\rvert=(p+2a)+(q+2a)+(p+q)=2(p+q)+4a=12a$" "\n"
        r"$\\Rightarrowp+q=4a$ ✓✓ **$\\lvert PQ\\rvert=4a$ 与原书一致** ✓" "\n"
        r"③ **勾股**：$\\lvert QF_2\\rvert^2-\\lvert PF_2\\rvert^2=\\lvert PQ\\rvert^2=16a^2$ ✓✓" "\n"
        r"$(q+2a)^2-(p+2a)^2=(q-p)(p+q+4a)=(q-p)(4a+4a)=8a(q-p)=16a^2\\Rightarrowq-p=2a$ ✓✓✓" "\n"
        r"④ **$p=a,q=3a$**；$\\lvert PF_2\\rvert=p+2a=3a$ ✓✓ **与原书「$\\lvert PF_2\\rvert=3a$」一致** ✓" "\n"
        r"⑤ **$e$**：$a^2+(3a)^2=4c^2\\Rightarrow10a^2=4c^2\\Rightarrowe^2=2.5$ ✓$e=\\sqrt{2.5}=1.58114$" "\n"
        r"$\\frac{\\sqrt{10}}2=\\frac{3.16228}2=1.58114$ ✓✓✓ **恰为选项 A**" "\n"
        r"⑥ **合理性**：$e=1.581>1$ ✓；$p=a>0$、$q=3a>0$ ✓；$\\lvert PF_2\\rvert=3a>\\lvert PF_1\\rvert=a$ ✓（左支）✓✓" "\n"
        r"⑦ **排除其他**：B $=\\sqrt3=1.732$、C $=\\sqrt5=2.236$、D $=2\\sqrt2=2.828$ ✗" "\n"
        r"**答案 A（$\\frac{\\sqrt{10}}2$）正确** ✓" "\n"
        r"**⭐ 通法（向量式 ⟹ 垂直）**：" "\n"
        r"① ⭐⭐ **见到 $\\lvert \\vec a\\rvert^{2}=\\vec a\\cdot\\vec b$ ⟹ $\\vec a\\cdot(\\vec a-\\vec b)=0$ ⟹ $\\vec a\\perp(\\vec a-\\vec b)$** —— " "\n"
        r"而 $\\vec a-\\vec b$ 往往就是**两点连线**（本题 $=\\vec{QP}$），于是得到垂直；" "\n"
        r"② 垂直 ⟹ 勾股，配合**周长**条件可解出各焦半径；" "\n"
        r"③ ⭐ **同支两点的弦过焦点**：$F_1$ 在 $P,Q$ 之间 ⟹ $\\lvert PQ\\rvert=\\lvert PF_1\\rvert+\\lvert QF_1\\rvert$（**加**）；" "\n"
        r"（对比 M-T-369-V2 中直线过 $F_2$ 交右支于 $A,B$ 也是加）" "\n"
        r"④ $\\lvert QF_2\\rvert^{2}-\\lvert PF_2\\rvert^{2}=(q-p)(p+q+4a)$ 的**因式分解**是关键一步，" "\n"
        r"把「平方差」转成「和 × 差」，立刻能代入已知的 $p+q$。"
    ),
    'difficulty': 0.94,
    'topics': ['M-T-367'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-367-V1',
}

T367_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知 $F$ 是双曲线 $\dfrac{x^{2}}{a^{2}}-\dfrac{y^{2}}{b^{2}}=1$ 的左焦点，圆 $O:x^{2}+y^{2}=a^{2}+b^{2}$ 与双曲线"
        r"在第一象限的交点为 $P$，若 $PF$ 的中点在双曲线的渐近线上，则此双曲线的离心率是（　　）"
    ),
    'opts': [
        ('A', r"$\sqrt5$"),
        ('B', r"$\dfrac{\sqrt5}2$"),
        ('C', r"$\sqrt3$"),
        ('D', r"$\sqrt2$"),
    ],
    'answer': 'A',
    'analysis': (
        r"圆半径 $=\sqrt{a^{2}+b^{2}}=c$，故 $P$ 在以焦距为直径的圆上 ⟹ $\angle FPF'=90^\circ$。"
        r"设 $M$ 为 $PF$ 中点，则 $MO$ 是 $\triangle PFF'$ 的中位线 ⟹ $MO\parallel PF'$ 且 $MO\perp PF$。"
        r"$M$ 在渐近线上：$FM=b$、$MO=a$ ⟹ $\lvert PF\rvert=2b$、$\lvert PF'\rvert=2a$。由定义 $2b-2a=2a$ ⟹ $b=2a$ ⟹ $e=\sqrt5$。"
    ),
    'solution': (
        r"**第一步：识别「直径圆」**" "\n"
        r"圆 $O$ 的半径 $=\sqrt{a^{2}+b^{2}}=c$，而 $F,F'$ 到 $O$ 的距离都是 $c$，" "\n"
        r"故 $FF'$ 是圆的直径，$P$ 在圆上 ⟹ $\angle FPF'=90^\circ$．" "\n"
        r"**第二步：中位线**" "\n"
        r"设 $PF$ 的中点为 $M$。在 $\triangle PFF'$ 中，$M$ 是 $PF$ 中点、$O$ 是 $FF'$ 中点，" "\n"
        r"故 $MO\parallel PF'$，$MO=\dfrac12\lvert PF'\rvert$；且 $MO\perp PF$（因 $PF\perp PF'$，$MO\parallel PF'$）．" "\n"
        r"**第三步：用「$M$ 在渐近线上」**" "\n"
        r"在 Rt$\triangle FMO$ 中（直角在 $M$），$\angle MOF$ 等于渐近线倾角，故 $\tan\angle MOF=\dfrac ba$。" "\n"
        r"又 $\tan\angle MOF=\dfrac{FM}{MO}$，且 $FM^{2}+MO^{2}=OF^{2}=c^{2}=a^{2}+b^{2}$，" "\n"
        r"由 $\dfrac{FM}{MO}=\dfrac ba$ 得 $FM=b$、$MO=a$．" "\n"
        r"**第四步：用双曲线定义**" "\n"
        r"$\lvert PF\rvert=2FM=2b$，$\lvert PF'\rvert=2MO=2a$．" "\n"
        r"$P$ 在第一象限（右支）：$\lvert PF'\rvert-\lvert PF\rvert=2a\Rightarrow2b-2a=2a\Rightarrow b=2a$．" "\n"
        r"**第五步：求 $e$**" "\n"
        r"$c^{2}=a^{2}+b^{2}=a^{2}+4a^{2}=5a^{2}\Rightarrow e=\sqrt5$．选 A．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓。原书 p348 详解：" "\n"
        r"「因为 $a^{2}+b^{2}=c^{2}$，且圆 $O:x^{2}+y^{2}=a^{2}+b^{2}$，所以点 $P$ 在以焦距为直径的圆上，" "\n"
        r"则 $\\angle FPF'=90^\\circ$…$MO\\parallel PF'$…$\\tan\\angle MOF=\\frac ba=\\frac{FM}{MO}$，且 $FM^{2}+MO^{2}=OF^{2}$，" "\n"
        r"则 $FM=b$，$MO=a$…在 Rt$\\triangle FPF'$ 中 $4a^{2}+16a^{2}=4c^{2}$，解得 $e^{2}=5$，所以 $e=\\sqrt5$。故选 A」" "\n"
        r"**⚠ 原书有一处笔误**：「所以 $PF=2MO=2a$，所以 $PF=4a$」第一步应为 $PF'=2MO=2a$、" "\n"
        r"第二步应为 $PF=2FM=2b$（配合 $b=2a$ 才得 $4a$）。我的推导已按正确的中位线对应修正。" "\n"
        r"**独立验算（完整代数求解，独立复现 $b=2a$）**：" "\n"
        r"设 $a=1$，联立圆 $x^2+y^2=c^2=1+b^2$ 与双曲线 $x^2-\\frac{y^2}{b^2}=1$：" "\n"
        r"$y^{2}=\\frac{b^{4}}{1+b^{2}}$，$x^{2}=\\frac{1+2b^{2}}{1+b^{2}}$ ⟹ $P\\left(\\frac{\\sqrt{1+2b^{2}}}{c},\\frac{b^{2}}{c}\\right)$" "\n"
        r"$F=(-c,0)$（**左**焦点），$M=\\left(\\frac{x_P-c}{2},\\frac{y_P}{2}\\right)$ 在渐近线 $y=-bx$ 上（$x_M<0$ 支）：" "\n"
        r"$\\frac{b^{2}}{2c}=-b\\cdot\\frac{\\sqrt{1+2b^{2}}/c-c}{2}\\Rightarrowb=\\sqrt{1+2b^{2}}-(1+b^{2})$" "\n"
        r"整理：$\\sqrt{1+2b^{2}}=1+b^{2}-b$，平方 ⟹ $b^{3}-2b^{2}+b-2=0\\Rightarrow(b^{2}+1)(b-2)=0\\Rightarrowb=2$ ✓✓✓" "\n"
        r"$e^{2}=1+b^{2}=5$，$e=\\sqrt5=2.23607$ ✓✓✓ **恰为选项 A**" "\n"
        r"② **构造验证**：$a=1,b=2,c=\\sqrt5=2.23607$。$P=(\\sqrt{1+8}/\\sqrt5,4/\\sqrt5)=(1.34164,1.78885)$" "\n"
        r"$F=(-2.23607,0)$、$F'=(2.23607,0)$" "\n"
        r"$\\lvert PF\\rvert=\\lvert(3.57771,1.78885)\\rvert=\\sqrt{12.8+3.2}=4=2b$ ✓✓" "\n"
        r"$\\lvert PF'\\rvert=\\lvert(-0.89443,1.78885)\\rvert=\\sqrt{0.8+3.2}=2=2a$ ✓✓" "\n"
        r"$\\lvert PF\\rvert-\\lvert PF'\\rvert=4-2=2=2a$ ✓✓✓ **定义成立**" "\n"
        r"$M=\\frac{P+F}{2}=(-0.44721,0.89443)$，渐近线 $y=-2x$：$0.89443=-2(-0.44721)=0.89443$ ✓✓✓ **$M$ 确在渐近线上**" "\n"
        r"③ **$\\angle FPF'$**：$\\vec{PF}=(-3.57771,-1.78885)$、$\\vec{PF'}=(0.89443,-1.78885)$" "\n"
        r"点积 $=-3.2+3.2=0$ ✓✓ **确为直角**" "\n"
        r"④ **排除其他**：B $=\\frac{\\sqrt5}2=1.118$、C $=\\sqrt3=1.732$、D $=\\sqrt2=1.414$ ✗" "\n"
        r"**答案 A（$\\sqrt5$）正确** ✓" "\n"
        r"**⭐ 通法（中点落在特殊直线上）**：" "\n"
        r"① ⭐⭐ **$x^{2}+y^{2}=a^{2}+b^{2}=c^{2}$ 就是以焦距为直径的圆** ⟹ 圆上点对两焦点张 **$90^\\circ$** —— " "\n"
        r"这个识别能省掉大量计算（与 M-T-373-V2 的圆是同一套路）；" "\n"
        r"② ⭐ **三角形中位线**：$M$ 是 $PF$ 中点、$O$ 是 $FF'$ 中点 ⟹ $MO\\overset{\\parallel}{=}\\frac12 PF'$ —— " "\n"
        r"把「$M$ 在渐近线上」翻译成 $MO$ 的方向，进而得到 $FM$ 与 $MO$ 的比；" "\n"
        r"③ ⚠ **中位线对应关系别搞反**：$MO$ 对应的是 **$PF'$**（不是 $PF$），我第一遍搞反后" "\n"
        r"代入定义得 $2a-2b=2a\\Rightarrowb=0$，**这个荒谬结果就是警报**；" "\n"
        r"④ Rt$\\triangle$ 中 $\\tan\\theta=\\frac ba$ 且两直角边平方和 $=c^{2}$ ⟹ 两直角边就是 $b$ 和 $a$（**比例即长度**）。"
    ),
    'difficulty': 0.94,
    'topics': ['M-T-367'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-367-V2',
}

T367_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知 $F_1,F_2$ 是双曲线 $C:\dfrac{x^{2}}{a^{2}}-\dfrac{y^{2}}{b^{2}}=1\ (a>0,b>0)$ 的左、右焦点，"
        r"过点 $F_1$ 倾斜角为 $30^\circ$ 的直线与双曲线的左、右两支分别交于点 $A,B$。若 $\lvert AF_2\rvert=\lvert BF_2\rvert$，"
        r"则双曲线 $C$ 的离心率为（　　）"
    ),
    'opts': [
        ('A', r"$\sqrt2$"),
        ('B', r"$\sqrt3$"),
        ('C', r"$2$"),
        ('D', r"$\sqrt5$"),
    ],
    'answer': 'A',
    'analysis': (
        r"⚠ 关键：$A,B$ 在 $F_1$ 的**同侧**（因 $-c<-a$，从左焦点出发向右先遇左支后遇右支），"
        r"故 $\lvert AB\rvert=\lvert BF_1\rvert-\lvert AF_1\rvert=4a$，而非相加。"
        r"再对 $\triangle F_1AF_2$ 与 $\triangle F_1BF_2$ 分别用余弦定理（夹角同为 $30^\circ$），消去 $\lvert AF_1\rvert$ 得 $e^{2}=2$。"
    ),
    'solution': (
        r"**第一步：判断 $A,B$ 与 $F_1$ 的位置关系**" "\n"
        r"$F_1(-c,0)$，$-c<-a$，故 $F_1$ 在左支的**左侧**。直线倾斜角 $30^\circ$，从 $F_1$ 向右上方走，" "\n"
        r"先到左支（$x\le-a$）再到右支（$x\ge a$），所以 $A,B$ 在 $F_1$ 的**同侧**。" "\n"
        r"**第二步：用定义 + $\lvert AF_2\rvert=\lvert BF_2\rvert$**" "\n"
        r"$A$ 在左支：$\lvert AF_2\rvert-\lvert AF_1\rvert=2a$；$B$ 在右支：$\lvert BF_1\rvert-\lvert BF_2\rvert=2a$．" "\n"
        r"设 $\lvert AF_2\rvert=\lvert BF_2\rvert=d$，则 $\lvert AF_1\rvert=d-2a$，$\lvert BF_1\rvert=d+2a$．" "\n"
        r"同侧 ⟹ $\lvert AB\rvert=\lvert BF_1\rvert-\lvert AF_1\rvert=4a$．" "\n"
        r"**第三步：两次余弦定理（$\angle AF_1F_2=\angle BF_1F_2=30^\circ$）**" "\n"
        r"记 $s=\lvert AF_1\rvert$，则 $\lvert BF_1\rvert=s+4a$，$\lvert AF_2\rvert=\lvert BF_2\rvert=s+2a$．" "\n"
        r"$\triangle F_1AF_2$：$(s+2a)^{2}=s^{2}+4c^{2}-2s\cdot2c\cos30^\circ=s^{2}+4c^{2}-2\sqrt3cs$" "\n"
        r"$\Rightarrow4as+4a^{2}=4c^{2}-2\sqrt3cs\Rightarrow s(4a+2\sqrt3c)=4(c^{2}-a^{2})=4b^{2}\quad(1)$" "\n"
        r"$\triangle F_1BF_2$：$(s+2a)^{2}=(s+4a)^{2}+4c^{2}-2(s+4a)\cdot2c\cos30^\circ$" "\n"
        r"$\Rightarrow s^{2}+4as+4a^{2}=s^{2}+8as+16a^{2}+4c^{2}-2\sqrt3c(s+4a)$" "\n"
        r"$\Rightarrow0=s(4a-2\sqrt3c)+12a^{2}+4c^{2}-8\sqrt3ac\quad(2)$" "\n"
        r"**第四步：消去 $s$**" "\n"
        r"取 $a=1$、$c=e$、$b^{2}=e^{2}-1$，由 $(1)$：$s=\dfrac{2(e^{2}-1)}{2+\sqrt3e}$．代入 $(2)$ 并乘 $(2+\sqrt3e)$：" "\n"
        r"$2(e^{2}-1)(4-2\sqrt3e)+(12+4e^{2}-8\sqrt3e)(2+\sqrt3e)=0$" "\n"
        r"展开：$e^{3}$ 项 $-4\sqrt3e^{3}+4\sqrt3e^{3}=0$；$e$ 项 $4\sqrt3e+12\sqrt3e-16\sqrt3e=0$；" "\n"
        r"$e^{2}$ 项 $8e^{2}+8e^{2}-24e^{2}=-8e^{2}$；常数 $-8+24=16$。" "\n"
        r"$\Rightarrow-8e^{2}+16=0\Rightarrow e^{2}=2\Rightarrow e=\sqrt2$．选 A．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**详解未提取**，上述推导为我独立完成）。" "\n"
        r"**⚠ 选项还原**：原文提取为 `2 3 2 5`（根号丢失），按 A $\\sqrt2$、B $\\sqrt3$、C $2$、D $\\sqrt5$ 还原。" "\n"
        r"**判定依据**：我的推导给出 $e=\\sqrt2$ 且答案为 A。" "\n"
        r"**⚠⚠ 本题最大的坑（我第一遍就栽了）**：" "\n"
        r"我按「$F_1$ 在 $A,B$ 之间」算，得 $\\lvert AB\\rvert=\\lvert AF_1\\rvert+\\lvert BF_1\\rvert=2d$，" "\n"
        r"而由 $\\lvert AF_2\\rvert=\\lvert BF_2\\rvert=d$ 与直角关系又得 $\\lvert AB\\rvert=d\\sqrt2$ —— **$2d=d\\sqrt2$ 无解**。" "\n"
        r"**这个矛盾本身就是提示**：$A,B$ 必在 $F_1$ 同侧。原因见下方验算①。" "\n"
        r"**独立验算**：" "\n"
        r"① ⭐ **位置关系**：$-c<-a$（因 $c>a$）⟹ $F_1$ 在左支左边。" "\n"
        r"直线 $(-c,0)+t(\\cos30^\\circ,\\sin30^\\circ)$：右支需 $-c+0.866t\\gea\\Rightarrot\\ge\\frac{a+c}{0.866}>0$；" "\n"
        r"左支需 $-c+0.866t\\le-a\\Rightarrot\\le\\frac{c-a}{0.866}>0$。**两者都要求 $t>0$** ⟹ **同侧** ✓✓✓" "\n"
        r"② **$s_B-s_A=4a$**：$\\lvert AF_1\\rvert=d-2a$、$\\lvert BF_1\\rvert=d+2a$，差 $=4a$ ✓✓" "\n"
        r"③ **$(1)$ 式**：$(s+2a)^2=s^2+4c^2-2\\sqrt3cs\\Rightarrow4as+4a^2=4c^2-2\\sqrt3cs$ ✓✓" "\n"
        r"④ **$(2)$ 式**：验证一次 —— $(s+2a)^2=(s+4a)^2+4c^2-2\\sqrt3c(s+4a)$" "\n"
        r"$s^2+4as+4a^2=s^2+8as+16a^2+4c^2-2\\sqrt3cs-8\\sqrt3ac$" "\n"
        r"$0=4as+12a^2+4c^2-2\\sqrt3cs-8\\sqrt3ac=s(4a-2\\sqrt3c)+12a^2+4c^2-8\\sqrt3ac$ ✓✓✓" "\n"
        r"⑤ **消元结果**：$e^3$ 与 $e$ 的系数**恰好都为 $0$**（不是巧合，说明消元方向正确），" "\n"
        r"只剩 $-8e^2+16=0\\Rightarrowe^2=2$，$e=\\sqrt2=1.41421$ ✓✓✓ **恰为选项 A**" "\n"
        r"⑥ **数值检验**：取 $a=1,e=\\sqrt2$ 则 $c=1.41421,b^2=1$。" "\n"
        r"由 $(1)$：$s=\\frac{2(2-1)}{2+\\sqrt3\\cdot1.41421}=\\frac{2}{2+2.44949}=\\frac{2}{4.44949}=0.44949$" "\n"
        r"$\\lvert AF_2\\rvert=s+2a=2.44949$；$\\lvert BF_1\\rvert=s+4a=4.44949$，$\\lvert BF_2\\rvert=\\lvert BF_1\\rvert-2a=2.44949$ ✓✓ **相等** ✓✓✓" "\n"
        r"验 $(2)$：$s(4a-2\\sqrt3c)+12a^2+4c^2-8\\sqrt3ac=0.44949(4-4.89898)+12+8-8(1.73205)(1.41421)$" "\n"
        r"$=0.44949(-0.89898)+20-19.59592=-0.40407+0.40408\\approx0$ ✓✓✓" "\n"
        r"⑦ **排除其他**：B $=\\sqrt3=1.732$、C $=2$、D $=\\sqrt5=2.236$ ✗" "\n"
        r"**答案 A（$\\sqrt2$）正确** ✓" "\n"
        r"**⭐⭐ 通法（过焦点直线交两支）**：" "\n"
        r"① ⭐⭐ **判断焦点在不在两点之间**：左焦点 $F_1(-c,0)$，$c>a$ ⟹ $-c<-a$，" "\n"
        r"$F_1$ 在**左支左侧**。过 $F_1$ 的直线若交左、右两支，则**两支都在 $t>0$ 侧** ⟹ " "\n"
        r"$\\lvert AB\\rvert=\\bigl\\lvert\\lvert BF_1\\rvert-\\lvert AF_1\\rvert\\bigr\\rvert$（**差**，不是和）；" "\n"
        r"（右焦点 $F_2$ 对称：$F_2$ 在右支右侧，交两支时也是**差**）" "\n"
        r"② ⚠ **若按「和」算出一支矛盾式（如 $2d=d\\sqrt2$），立刻改「差」** —— 这是最快的自检；" "\n"
        r"③ 两支各用一次定义，把四个焦半径都写成 $\\pm2a$ 的形式；" "\n"
        r"④ 对 $\\triangle F_1AF_2$、$\\triangle F_1BF_2$ 各用一次余弦定理（**夹角相同**），" "\n"
        r"两式相减/代入消去 $s$ —— 消元后 $e^{3}$、$e$ 项同时归零是正确性的强信号。"
    ),
    'difficulty': 0.95,
    'topics': ['M-T-367'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-367-V3',
}

QS = [T369_E1, T369_V1, T369_V2, T369_V3, T367_E1, T367_V1, T367_V2, T367_V3]
