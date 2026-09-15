# -*- coding: utf-8 -*-
r"""第 133 批（补录批·三）：攻「答案存疑」10 题，本批裁定 3 题。  python3 tools/run_batch.py 133  ## 选题依据  跳过清单里 `reason == "答案存疑"` 共 10 题。逐题复核原件后，**只有 3 题能给出可靠裁定**，其余 7 题或依赖图形、或详解本身残缺，维持跳过并已更新判定理由。  ## ★★ 一处 A 类勘误（原书答案错误）  ### M-T-361-V1：原书答「存在，$a=-2$」错，正确为「不存在」  联立得 $(3-a^2)x^2-2ax-2=0$，韦达 $x_1+x_2=\dfrac{2a}{3-a^2}$，$x_1x_2=\dfrac2{a^2-3}$。  **(1)** 圆过原点 $\iff \overrightarrow{OA}\cdot\overrightarrow{OB}=0$。因 $y_1y_2=(ax_1+1)(ax_2+1)$， 其中 $-2a^2+2a^2$ 恰好抵消，得 $y_1y_2=1$，故 $\dfrac2{a^2-3}+1=0\iff a^2=1\iff a=\pm1$（原书此问正确）。  **(2)** 两个条件**各自**都只有唯一解，且互不相容： * $\overrightarrow{OA}+\overrightarrow{OB}=\lambda(2,1)$ ⟹ $\dfrac{y_1+y_2}{x_1+x_2}=\dfrac12$，而由韦达 $y_1+y_2=a(x_1+x_2)+2$ ⟹ $\dfrac{y_1+y_2}{x_1+x_2}=a+\dfrac2{x_1+x_2}=\dfrac3a$，故 $a=6$，但此时 $a^2=36>6$ 使 $\Delta<0$，**无交点**； * $|\overrightarrow{OA}|=|\overrightarrow{OB}|$ ⟹ $(x_1-x_2)\big[(1+a^2)(x_1+x_2)+2a\big]=0$，代入韦达得 $(x_1-x_2)\cdot\dfrac{8a}{3-a^2}=0$，故 $a=0$，此时 $\overrightarrow{OA}+\overrightarrow{OB}=(0,2)$ 与 $(2,1)$ 不共线。  故满足两条件的 $a$ 不存在。  > **原书错在哪**：详解由 $|\overrightarrow{OA}|=|\overrightarrow{OB}|$ 得 $\dfrac{y_1-y_2}{x_1-x_2}=-\dfrac{x_1+x_2}{y_1+y_2}$，  > 又由共线条件得 $\dfrac{x_1+x_2}{y_1+y_2}=2$，于是 $\dfrac{y_1-y_2}{x_1-x_2}=-2$；再认 $\dfrac{y_1-y_2}{x_1-x_2}=a$，  > 便得 $a=-2$。但**它始终没有把韦达关系 $\dfrac{y_1+y_2}{x_1+x_2}=\dfrac3a$ 代回检验** ——  > $a=-2$ 时该比值是 $-\dfrac32\ne\dfrac12$，自相矛盾。  ## ★★ 两处 B 类还原（根号丢失）  ### M-T-303-V2：题干两个数据都丢了根号  提取文本作 $BC=CD=BD=3$、$AB=AC=AD=2$。按此底面外接圆半径 $OB=\sqrt3$、 $AO=\sqrt{4-3}=1$，$\tan\angle APO=\dfrac1{\sqrt3}$ ⟹ 最小角 $\dfrac\pi6$，与答案 $\dfrac\pi4$ 差一档。  **反推**：要 $\angle APO_{\min}=\dfrac\pi4$ 需 $AO=OB$，即 $l^2=\dfrac{2s^2}3$（$s$ 底边、$l$ 侧棱）。 两个数据都补回根号后 $s=\sqrt3$、$l=\sqrt2$ ⟹ $OB=1$、$AO=\sqrt{2-1}=1$，恰好相等 ✓。 **验证**：取 $B(1,0,0)$、$C(-\frac12,\frac{\sqrt3}2,0)$、$D(-\frac12,-\frac{\sqrt3}2,0)$、$A(0,0,1)$， $Q$ 为 $CD$ 中点 $(-\frac12,0,0)$，$P$ 为 $BC$ 靠近 $C$ 的三等分点 $(0,\frac{\sqrt3}3,0)$ ——  $A,O,P$ 的 $x$ 坐标全为 $0$，平面 $AOP$ 即 $x=0$，而 $\overrightarrow{BQ}=(-\frac32,0,0)$ 正是其法向量 ⟹ $BQ\perp AP$ ⟹ 上界 $\dfrac\pi2$ 可取 ✓  ### M-T-306-V1：选项 A 的 $\sqrt2$ 丢成了 $2$  正方形 $ABFE$ 边长为 $2$，$O$ 为中心，$OA'=OA=\sqrt2$、$A'B=AB=2$， 故 $\sin\alpha=\dfrac h{\sqrt2}$、$\sin\beta=\dfrac h2$ ⟹ $\sin\alpha=\sqrt2\sin\beta$，而非 $2\sin\beta$。  """

T303_V2 = {
    'type': '填空',
    'stem_text': (
        r"已知正三棱锥 $A-BCD$，$BC=CD=BD=\sqrt3$，$AB=AC=AD=\sqrt2$，"
        r"点 $P$，$Q$ 分别在棱 $BC$，$CD$ 上（不包含端点），"
        r"则直线 $AP$，$BQ$ 所成的角的取值范围是 ____"
    ),
    'answer': r"$\left(\dfrac\pi4,\dfrac\pi2\right]$",
    'analysis': (
        r"$BQ$ 在底面内，故 $AP$ 与 $BQ$ 所成角 $\ge$ $AP$ 与底面所成角 $\angle APO$（$O$ 为底面中心），"
        r"而 $\angle APO$ 在 $OP$ 最大即 $P\to B$ 时取最小；上界 $\dfrac\pi2$ 在 $BQ\perp$ 平面 $AOP$ 时取到。"
        r"由 $OB=1$、$AO=1$ 得 $\tan\angle APO=1$，最小角为 $\dfrac\pi4$（$P$ 不含端点故取不到）。"
    ),
    'solution': (
        r"设 $O$ 为正三角形 $BCD$ 的中心，则 $A$ 在 $O$ 的正上方，且 $AO\perp$ 平面 $BCD$。" "\n"
        r"由 $BC=CD=BD=\sqrt3$ 得 $OB=\dfrac{\sqrt3}{\sqrt3}=1$；"
        r"由 $AB=\sqrt2$ 得 $AO=\sqrt{AB^2-OB^2}=\sqrt{2-1}=1$。" "\n"
        r"**下界**：因为 $Q\in CD$，$B$ 为顶点，所以直线 $BQ\subset$ 平面 $BCD$。"
        r"而 $\angle APO$ 是 $AP$ 与平面 $BCD$ 内**任意**直线所成角的最小值，"
        r"故 $AP$ 与 $BQ$ 所成角 $\ge\angle APO$。" "\n"
        r"在 $\mathrm{Rt}\triangle AOP$ 中 $\tan\angle APO=\dfrac{AO}{OP}=\dfrac1{OP}$，"
        r"$P$ 在棱 $BC$ 上（不含端点）时 $OP$ 在 $P\to B$ 时最大，此时 $OP\to OB=1$，"
        r"故 $\angle APO>\arctan\dfrac11=\dfrac\pi4$（端点取不到，为开区间）。" "\n"
        r"**上界**：取 $Q$ 为 $CD$ 的中点、$P$ 为 $BC$ 上靠近 $C$ 的三等分点。"
        r"建系 $O(0,0,0)$、$B(1,0,0)$、$C\left(-\dfrac12,\dfrac{\sqrt3}2,0\right)$、"
        r"$D\left(-\dfrac12,-\dfrac{\sqrt3}2,0\right)$、$A(0,0,1)$，"
        r"则 $Q\left(-\dfrac12,0,0\right)$，$P=B+\dfrac23(C-B)=\left(0,\dfrac{\sqrt3}3,0\right)$。" "\n"
        r"此时 $A,O,P$ 的 $x$ 坐标皆为 $0$，故平面 $AOP$ 就是平面 $x=0$，法向量为 $(1,0,0)$；"
        r"而 $\overrightarrow{BQ}=\left(-\dfrac32,0,0\right)\parallel(1,0,0)$，"
        r"即 $BQ\perp$ 平面 $AOP$，从而 $BQ\perp AP$，所成角为 $\dfrac\pi2$，上界可取到。" "\n"
        r"综上，所成角的取值范围是 $\left(\dfrac\pi4,\dfrac\pi2\right]$．"
    ),
    'review': (
        r"① ⭐⭐ **异面直线所成角的下界 = 其中一条与另一条所在平面的最小角**："
        r"本题 $BQ$ 恒在底面内，于是「$AP$ 与 $BQ$」的下界就归结为「$AP$ 与底面所成角 $\angle APO$」，"
        r"这是整道题的题眼。" "\n"
        r"② ⭐⭐ **$\angle APO$ 随 $OP$ 增大而减小**（$\tan\angle APO=\dfrac{AO}{OP}$，$AO$ 固定），"
        r"故最小值在 $OP$ 最大处即 $P\to B$ 取得；又 $P$ 不含端点，所以是**开区间**。" "\n"
        r"③ ⭐ **上界 $\dfrac\pi2$ 必须构造出来才算数**：三等分点之所以取「靠近 $C$」，"
        r"正是为了让 $P$ 的 $x$ 坐标恰好为 $0$，使平面 $AOP$ 退化成坐标面 $x=0$，"
        r"于是 $\overrightarrow{BQ}$ 直接平行于法向量。这是命题人刻意配好的数据。" "\n"
        r"④ ⚠ **本题两个数据都被 OCR 丢了根号**：提取文本作 $BC=\cdots=3$、$AB=\cdots=2$，"
        r"按此 $OB=\sqrt3$、$AO=1$，$\tan\angle APO=\dfrac1{\sqrt3}$ 会给 $\dfrac\pi6$，与答案对不上。"
        r"由答案 $\dfrac\pi4$ 反推需 $AO=OB$，即 $l^2=\dfrac{2s^2}3$，还原为 $s=\sqrt3$、$l=\sqrt2$ 后"
        r"$OB=AO=1$，完全自洽（已按 B 类勘误登记）。" "\n"
        r"**通法（动直线夹角的取值范围）**：① 认准哪条直线被限制在某个平面内；"
        r"② 下界用「斜线与平面所成角是最小角」；③ 上界用「垂直于另一条直线所在平面」构造；"
        r"④ 端点是否取得到，看动点是否含端点。"
    ),
    'difficulty': 0.65,
    'topics': ['M-T-303'],
    'kp1': '立体几何',
    'kp2': '空间角范围',
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-303-V2',
}

T306_V1 = {
    'type': '选择',
    'stem_text': (
        r"矩形 $ABCD$ 中，已知 $AB=2$，$BC=4$，$E$ 为 $AD$ 的中点．"
        r"将 $\triangle ABE$ 沿着 $BE$ 向上翻折至 $\triangle A'BE$，"
        r"记锐二面角 $A'-BE-C$ 的平面角为 $\alpha$，$A'B$ 与平面 $BCDE$ 所成的角为 $\beta$，"
        r"则下列结论不可能成立的是（　　）"
    ),
    'opts': [
        ('A', r"$\sin\alpha=\sqrt2\sin\beta$"),
        ('B', r"$2\cos\alpha=\cos\beta$"),
        ('C', r"$\alpha<2\beta$"),
        ('D', r"$\alpha-\beta>\dfrac\pi4$"),
    ],
    'answer': 'D',
    'analysis': (
        r"取 $BC$ 中点 $F$，则 $ABFE$ 为边长 $2$ 的正方形，$O=AF\cap BE$ 为中心。"
        r"翻折中 $A'O\perp BE$、$OF\perp BE$，故 $\alpha=\angle A'OF$，$\beta=\angle A'BH$（$A'H\perp$ 平面 $BCDE$）。"
        r"由 $OA'=\sqrt2$、$A'B=2$ 得 $\sin\alpha=\sqrt2\sin\beta$，进而 $\cos^2\alpha=\cos2\beta$；"
        r"由此可判 A、B、C 均可能成立，而 $\alpha<2\beta$ 与 $\beta<\dfrac\pi4$ 一起推出 $\alpha-\beta<\dfrac\pi4$，D 不可能。"
    ),
    'solution': (
        r"取 $BC$ 的中点 $F$，连接 $EF$、$AF$，设 $AF\cap BE=O$。"
        r"由 $AE=BF=2$ 且 $AE\parallel BF$ 知 $ABFE$ 是边长为 $2$ 的正方形，$O$ 为其中心，" "\n"
        r"于是 $OA=OF=\sqrt2$，$OB=2$，且 $BE\perp OA$、$BE\perp OF$。" "\n"
        r"翻折过程中 $A'O=OA=\sqrt2$、$A'B=AB=2$、$A'E=AE=2$ 均保持不变，"
        r"且 $BE\perp A'O$、$BE\perp OF$ 仍成立，故 $BE\perp$ 平面 $A'OF$。" "\n"
        r"从而平面 $A'OF\perp$ 平面 $BCDE$，锐二面角 $A'-BE-C$ 的平面角为 $\alpha=\angle A'OF$。" "\n"
        r"过 $A'$ 作 $A'H\perp OF$ 于 $H$，则 $A'H\perp$ 平面 $BCDE$，"
        r"连接 $BF$，得 $A'B$ 与平面 $BCDE$ 所成的角为 $\beta=\angle A'BH$。记 $A'H=h$，则" "\n"
        r"$\sin\alpha=\dfrac{A'H}{A'O}=\dfrac h{\sqrt2}$，$\sin\beta=\dfrac{A'H}{A'B}=\dfrac h2$，"
        r"于是 $\sin\alpha=\sqrt2\sin\beta$ —— **选项 A 成立**。" "\n"
        r"两边平方：$1-\cos^2\alpha=2(1-\cos^2\beta)$，即 $\cos^2\alpha=2\cos^2\beta-1=\cos2\beta$。" "\n"
        r"由 $\cos^2\alpha>0$ 得 $\cos2\beta>0$，故 $\beta<\dfrac\pi4$。" "\n"
        r"又 $\alpha$ 为锐角时 $\cos\alpha=\sqrt{\cos2\beta}$，而 $0<\cos2\beta<1$ 时 $\sqrt{\cos2\beta}>\cos2\beta$，"
        r"即 $\cos\alpha>\cos2\beta$，由余弦函数在 $(0,\pi)$ 上递减得 $\alpha<2\beta$ —— **选项 C 成立**。" "\n"
        r"对选项 B：令 $\cos\beta=c$，则 $\cos\alpha=\sqrt{2c^2-1}$，$2\cos\alpha=\cos\beta$ 化为"
        r"$4(2c^2-1)=c^2$，得 $c^2=\dfrac47$，$c=\dfrac2{\sqrt7}\approx0.756>0.707=\cos\dfrac\pi4$，"
        r"故 $\beta<\dfrac\pi4$ 成立，**选项 B 可能成立**。" "\n"
        r"对选项 D：由 $\alpha<2\beta$ 得 $\alpha-\beta<\beta$，又 $\beta<\dfrac\pi4$，"
        r"故 $\alpha-\beta<\dfrac\pi4$，与 $\alpha-\beta>\dfrac\pi4$ 矛盾，**D 不可能成立**．故选 D。"
    ),
    'review': (
        r"① ⭐⭐ **翻折题先取「不变的中点结构」**：$E$、$F$ 分别是 $AD$、$BC$ 中点，"
        r"于是 $ABFE$ 是正方形，$O$ 是对角线交点 —— 翻折后 $A'O\perp BE$、$OF\perp BE$ 仍成立，"
        r"平面角 $\alpha=\angle A'OF$ 就落在这个正方形里，省掉大量计算。" "\n"
        r"② ⭐⭐ **两个空间角共用同一条垂线段 $A'H$**：$\sin\alpha=\dfrac{A'H}{A'O}$、"
        r"$\sin\beta=\dfrac{A'H}{A'B}$，两者之比就是 $\dfrac{A'B}{A'O}=\dfrac2{\sqrt2}=\sqrt2$。"
        r"凡是「两个角共用一条垂线」，都用这个办法建立联系。" "\n"
        r"③ ⭐ **$\sin\alpha=\sqrt2\sin\beta$ 平方后自然出现 $\cos2\beta$**："
        r"$\cos^2\alpha=2\cos^2\beta-1$ 是二倍角公式，这一步同时给出 $\beta<\dfrac\pi4$ 与 $\cos\alpha>\cos2\beta$，"
        r"是判 C、D 的关键。" "\n"
        r"④ ⚠ **原书选项 A 印作 $\sin\alpha=2\sin\beta$，丢了 $\sqrt2$**："
        r"按 $2\sin\beta$ 则 $\cos^2\alpha=4\cos^2\beta-3$，后续 $\beta<\dfrac\pi3$ 等结论全变，"
        r"与「不可能成立的是 D」不匹配。已按 B 类勘误还原为 $\sqrt2$。" "\n"
        r"⑤ 数值复核：$\beta=40^\circ$ 时 $\cos\beta=0.766$，$\cos\alpha=\sqrt{2\times0.5868-1}=0.4149$，"
        r"$\alpha=65.5^\circ$；$\alpha<2\beta=80^\circ$ ✓，$\alpha-\beta=25.5^\circ<45^\circ$ ✓。" "\n"
        r"**通法（翻折中的双角关系）**：① 找出不变量（长度、垂直关系）；② 确认平面角与线面角各是哪个角；"
        r"③ 用共用的垂线段建立两角正弦的联系；④ 平方后用二倍角公式转成余弦，再比大小。"
    ),
    'difficulty': 0.7,
    'topics': ['M-T-306'],
    'kp1': '立体几何',
    'kp2': '翻折中的角度关系',
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-306-V1',
}

T361_V1 = {
    'type': '解答',
    'stem_text': (
        r"设直线 $l:y=ax+1$ 与双曲线 $C:3x^2-y^2=1$ 相交于 $A$，$B$ 两点，$O$ 为坐标原点．" "\n"
        r"(1) $a$ 为何值时，以 $AB$ 为直径的圆过原点？" "\n"
        r"(2) 是否存在实数 $a$，使 $|\overrightarrow{OA}|=|\overrightarrow{OB}|$ 且 "
        r"$\overrightarrow{OA}+\overrightarrow{OB}=\lambda(2,1)$？若存在，求 $a$ 的值；若不存在，说明理由．"
    ),
    'answer': r"(1) $a=\pm1$；(2) 不存在",
    'analysis': (
        r"联立得 $(3-a^2)x^2-2ax-2=0$，韦达给出 $x_1+x_2=\dfrac{2a}{3-a^2}$、$x_1x_2=\dfrac2{a^2-3}$。"
        r"(1) 圆过原点 $\iff\overrightarrow{OA}\cdot\overrightarrow{OB}=0$，其中 $y_1y_2$ 的 $a^2$ 项恰好抵消得 $1$，故 $a^2=1$。"
        r"(2) 共线条件给出 $\dfrac{y_1+y_2}{x_1+x_2}=\dfrac12$，而韦达算得该比值恒为 $\dfrac3a$，故 $a=6$（无交点）；"
        r"等长条件化简为 $\dfrac{8a}{3-a^2}=0$，故 $a=0$。两者不能同时成立，故不存在。"
    ),
    'solution': (
        r"由 $\begin{cases}y=ax+1\\3x^2-y^2=1\end{cases}$ 消去 $y$ 整理得" "\n"
        r"$$(3-a^2)x^2-2ax-2=0.$$" "\n"
        r"依题意 $3-a^2\ne0$ 且 $\Delta=4a^2+8(3-a^2)=24-4a^2>0$，故 $a^2<6$ 且 $a^2\ne3$。" "\n"
        r"设 $A(x_1,y_1)$，$B(x_2,y_2)$，由韦达定理" "\n"
        r"$$x_1+x_2=\frac{2a}{3-a^2},\qquad x_1x_2=\frac{-2}{3-a^2}=\frac2{a^2-3}.$$" "\n"
        r"**(1)** 以 $AB$ 为直径的圆过原点 $\iff\overrightarrow{OA}\cdot\overrightarrow{OB}=0$，即 $x_1x_2+y_1y_2=0$。" "\n"
        r"而 $y_1y_2=(ax_1+1)(ax_2+1)=a^2x_1x_2+a(x_1+x_2)+1$" "\n"
        r"$=\dfrac{2a^2}{a^2-3}+\dfrac{2a^2}{3-a^2}+1=\dfrac{2a^2}{a^2-3}-\dfrac{2a^2}{a^2-3}+1=1$（两项恰好抵消）。" "\n"
        r"于是 $\dfrac2{a^2-3}+1=0$，得 $a^2=1$，即 $a=\pm1$（均满足 $a^2<6$）。" "\n"
        r"**(2)** 假设存在这样的实数 $a$。" "\n"
        r"由 $\overrightarrow{OA}+\overrightarrow{OB}=\lambda(2,1)$ 知 $(x_1+x_2,\ y_1+y_2)$ 与 $(2,1)$ 共线，即" "\n"
        r"$$\frac{y_1+y_2}{x_1+x_2}=\frac12.$$" "\n"
        r"另一方面 $y_1+y_2=a(x_1+x_2)+2$，故" "\n"
        r"$$\frac{y_1+y_2}{x_1+x_2}=a+\frac2{x_1+x_2}=a+\frac{3-a^2}{a}=\frac{a^2+3-a^2}{a}=\frac3a.$$" "\n"
        r"于是 $\dfrac3a=\dfrac12$，得 $a=6$。但此时 $a^2=36>6$，与 $a^2<6$ 矛盾，直线与双曲线**不相交**。" "\n"
        r"再由 $|\overrightarrow{OA}|=|\overrightarrow{OB}|$ 得 $x_1^2+y_1^2=x_2^2+y_2^2$，即" "\n"
        r"$$(x_1-x_2)(x_1+x_2)+(y_1-y_2)(y_1+y_2)=0.$$" "\n"
        r"其中 $y_1-y_2=a(x_1-x_2)$，$y_1+y_2=a(x_1+x_2)+2$，代入得" "\n"
        r"$$(x_1-x_2)\big[(1+a^2)(x_1+x_2)+2a\big]=0.$$" "\n"
        r"因 $A\ne B$ 有 $x_1\ne x_2$，故 $(1+a^2)\cdot\dfrac{2a}{3-a^2}+2a=0$，"
        r"即 $2a\left(\dfrac{1+a^2}{3-a^2}+1\right)=2a\cdot\dfrac4{3-a^2}=\dfrac{8a}{3-a^2}=0$，得 $a=0$。" "\n"
        r"可见两个条件分别要求 $a=6$ 与 $a=0$，不能同时满足，故**不存在**这样的实数 $a$．"
    ),
    'review': (
        r"① ⭐⭐ **$y_1y_2$ 的 $a^2$ 项必然抵消**：$(ax_1+1)(ax_2+1)$ 展开后 $a^2x_1x_2$ 与 $a(x_1+x_2)$ "
        r"分子同为 $2a^2$、分母互为相反数，故 $y_1y_2\equiv1$ 与 $a$ 无关。这是「$y=kx+b$ 型联立」的固定现象，"
        r"看到 $y_1y_2$ 是常数不要怀疑算错。" "\n"
        r"② ⭐⭐ **共线条件化为「和向量两分量之比」**：$\overrightarrow{OA}+\overrightarrow{OB}=\lambda(2,1)$ "
        r"等价于 $\dfrac{y_1+y_2}{x_1+x_2}=\dfrac12$（$\lambda$ 是自由的，只要方向对）。" "\n"
        r"③ ⭐ **$\dfrac{y_1+y_2}{x_1+x_2}=a+\dfrac2{x_1+x_2}$ 这一步最省事**："
        r"不必分别求 $y_1+y_2$，直接由 $y=ax+1$ 得和式即可，代入 $x_1+x_2=\dfrac{2a}{3-a^2}$ 后恰好约成 $\dfrac3a$。" "\n"
        r"④ ⭐ **等长条件提取公因子 $(x_1-x_2)$**：$x_1^2-x_2^2$ 与 $y_1^2-y_2^2$ 都含它，"
        r"提出后剩下的整式代入韦达化简为 $\dfrac{8a}{3-a^2}$，一步定号。" "\n"
        r"⑤ ⚠ **必须回验 $\Delta>0$**：$a=6$ 这一步看起来「求出了 $a$」，但 $a^2=36>6$ 使方程无实根，"
        r"直线与双曲线根本不相交。这类「解出来却在定义域外」是解析几何最高频的失分点。" "\n"
        r"⑥ ⚠ **原书答案「存在，$a=-2$」有误**（已按 A 类勘误登记）："
        r"详解由等长得 $\dfrac{y_1-y_2}{x_1-x_2}=-\dfrac{x_1+x_2}{y_1+y_2}$，又由共线得 $\dfrac{x_1+x_2}{y_1+y_2}=2$，"
        r"于是 $a=\dfrac{y_1-y_2}{x_1-x_2}=-2$。但**它从未把 $\dfrac{y_1+y_2}{x_1+x_2}=\dfrac3a$ 代回检验**："
        r"$a=-2$ 时该比值为 $-\dfrac32\ne\dfrac12$。数值验证：$a=-2$ 时 $x=2\pm\sqrt2$，"
        r"$|\overrightarrow{OA}|^2=23+16\sqrt2\approx45.63$、$|\overrightarrow{OB}|^2=23-16\sqrt2\approx0.37$ 不等，"
        r"且 $\overrightarrow{OA}+\overrightarrow{OB}=(4,-6)$ 与 $(2,1)$ 不共线，两个条件均不满足。" "\n"
        r"**通法（直线与圆锥曲线相交的向量条件）**：① 联立后先定 $\Delta>0$ 的参数范围；"
        r"② 数量积型条件用 $\overrightarrow{OA}\cdot\overrightarrow{OB}=x_1x_2+y_1y_2$；"
        r"③ 等长型条件提取 $(x_1-x_2)$；④ 共线型条件化为和向量分量之比；"
        r"⑤ **每个解出的参数都要回验 $\Delta>0$**。"
    ),
    'difficulty': 0.75,
    'topics': ['M-T-361'],
    'kp1': '圆锥曲线',
    'kp2': '双曲线中的向量条件与定点',
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-361-V1',
}

QS = [T303_V2, T306_V1, T361_V1]
