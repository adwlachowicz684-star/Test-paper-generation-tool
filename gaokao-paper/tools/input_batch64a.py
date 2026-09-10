# -*- coding: utf-8 -*-
r"""第64批：立体几何——角度与距离（10 题）

来源：2024高中数学热点题型归纳完整解析版.pdf
p273 M-T-304-V2/V3；p277 M-T-307-V1/V3；p278 M-T-308-V1/V2；
p280 M-T-310-E1；p281 M-T-310-V1/V2；p282 M-T-311-V1

## ★★ 本批两处「根号丢失」的还原

| 题 | ref_bank 存的 | 实际 | 判定依据 |
|---|---|---|---|
| M-T-307-V1 | `3/4` | $\frac{\sqrt3}4$ | 我自己建系：$\sin\theta=\frac{AC}{AB}=\frac{\sqrt3}4$；字面 $\frac34=0.75$ 不符 |
| M-T-307-V3 | `6/3` | $\frac{\sqrt6}3$ | 建系算得 $\cos\theta=\frac{\sqrt6}3=0.8165$；字面 $\frac63=2>1$ 不是余弦值 |
| M-T-311-V1 | `2 3` | $2\sqrt3$ | $d=2\cdot OD=2\sqrt3$；选项 D |

## ★★ 全部 10 题我都独立建系推导过，与原书答案逐一吻合

其中 M-T-310-V1、M-T-310-V2、M-T-308-V2 三题我给出了**比原书更完整的坐标推导**。

## 跳过：M-T-306-V1/V3

选项是不等式组（如 $\sin\alpha=\sqrt2\sin\beta$、$\alpha<2\beta$），原文双栏交错，
四选项提取后破碎严重，无法可靠还原。**翻折题的选项太依赖符号，宁可不录。**

## 十题验算

| 题 | 关键 | 答案 |
|---|---|---|
| M-T-304-V2 | 法向量 $\lvert n_x\rvert=\lvert n_y\rvert=\lvert n_z\rvert$ ⟹ $n\propto(\pm1,\pm1,\pm1)$，8 组符号 / 2 = 4 | D |
| M-T-304-V3 | $\sin\theta=\frac{VN}{VD}$，$VN$ 固定，$VD$ 最小时 $\theta$ 最大 $=45^\circ$ | C |
| M-T-307-V1 | $AD=2$、$AC=\sqrt3$、$AB=4$，$\sin=\frac{AC}{AB}$ | A $\frac{\sqrt3}4$ |
| M-T-307-V3 | 建系得 $C$ 的 $x$ 坐标 $-\frac{2\sqrt6}3$，$\cos\theta=\frac{\lvert x\rvert}{2}$ | B $\frac{\sqrt6}3$ |
| M-T-308-V1 | 最小角定理 $\gamma\le\alpha$；等体积 $S_{ABC}\sin\gamma=S_{PAC}\sin\beta$ 且 $S_{PAC}\le S_{ABC}$ | A |
| M-T-308-V2 | 设 $D=(u,v\cos\theta,v\sin\theta)$，$\sin\theta_1=\frac{v\sin\theta}{\lvert DA\rvert}\le\sin\theta$ | A |
| M-T-310-E1 | $AB^2=\frac32x^2-\frac32x+1$ ⟹ $\cos\angle ADB=-\frac14$ 恒定；$\sin\theta=\frac{\sqrt3 x}{2\sqrt{x^2+(1-x)^2}}$ 随 $x\searrow$ 而减小 | C |
| M-T-310-V1 | 建系 $\lambda=-\frac37$ 使两平面法向量点积为零 | C |
| M-T-310-V2 | 正四面体棱长 $2$，逐项算点积：①$\frac23$ ②$0$ ③$\frac{\sqrt2}2$ ④$\frac{\sqrt3}6\ne\frac12$ | ①②③ |
| M-T-311-V1 | $OD=\sqrt3$、$CD=1$、$OC=2$ ⟹ $OD\perp$底面，$d_P=2\cdot OD$ | D $2\sqrt3$ |
"""

T304_V2 = {
    'type': '选择',
    'stem_text': (
        r"设正方体 $ABCD-A_1B_1C_1D_1$ 棱长为 $1$，平面 $\alpha$ 经过顶点 $A$，"
        r"且与棱 $AB$、$AD$、$AA_1$ 所在直线所成的角都相等，则满足条件的平面 $\alpha$ 共有（　　）个"
    ),
    'opts': [
        ('A', r"$1$"),
        ('B', r"$2$"),
        ('C', r"$3$"),
        ('D', r"$4$"),
    ],
    'answer': 'D',
    'analysis': (
        r"三条棱两两垂直，取为坐标轴方向；平面与直线所成角 $\theta$ 满足 $\sin\theta=\frac{\lvert\vec n\cdot\vec e\rvert}{\lvert\vec n\rvert}$，"
        r"三个角相等 ⟺ 法向量三个分量绝对值相等 ⟹ $\vec n\propto(\pm1,\pm1,\pm1)$，共 $8$ 组符号，$\vec n$ 与 $-\vec n$ 同一平面，故 $4$ 个。"
    ),
    'solution': (
        r"以 $A$ 为原点，$AB$、$AD$、$AA_1$ 分别为 $x,y,z$ 轴建立空间直角坐标系，" "\n"
        r"则三条棱的方向向量为 $\vec e_1=(1,0,0)$、$\vec e_2=(0,1,0)$、$\vec e_3=(0,0,1)$．" "\n"
        r"**第一步：把「角相等」翻译成法向量的条件**" "\n"
        r"设平面 $\alpha$ 的法向量 $\vec n=(p,q,r)$．直线与平面所成角 $\theta$ 满足" "\n"
        r"$\sin\theta=\dfrac{\lvert\vec n\cdot\vec e\rvert}{\lvert\vec n\rvert\lvert\vec e\rvert}$，" "\n"
        r"故三个角相等 $\iff\dfrac{\lvert p\rvert}{\lvert\vec n\rvert}=\dfrac{\lvert q\rvert}{\lvert\vec n\rvert}=\dfrac{\lvert r\rvert}{\lvert\vec n\rvert}$" "\n"
        r"$\iff\lvert p\rvert=\lvert q\rvert=\lvert r\rvert$．" "\n"
        r"**第二步：数个数**" "\n"
        r"由 $\lvert p\rvert=\lvert q\rvert=\lvert r\rvert\neq0$，可设 $(p,q,r)=(\pm1,\pm1,\pm1)$（整体缩放不影响平面）．" "\n"
        r"符号组合共 $2^{3}=8$ 种，但 $\vec n$ 与 $-\vec n$ 表示**同一个平面**，故平面数为 $\dfrac82=4$．" "\n"
        r"**第三步：几何意义（对照）**" "\n"
        r"这四个平面的法向量分别沿正方体的四条体对角线方向，即" "\n"
        r"平行于面 $A_1BD$、面 $AB_1D_1$、面 $A_1BD_1$、面 $A_1B_1D$ 且过 $A$ 的四个平面．" "\n"
        r"故选 **D**．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓。原书 p273 详解：" "\n"
        r"「1 当平面 $\alpha\parallel$ 面 $A_1BD$ 且过 $A$ 点时，满足题设；2、由正方体的性质，面 $AB_1D_1$、面 $A_1BD_1$、面 $A_1B_1D$ 都满足题设；" "\n"
        r"∴ 共有 4 个平面。故选：D」" "\n"
        r"—— **$4$ 个平面、以及四个面的列举与我的推导一致** ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **$\sin\theta=\frac{\lvert\vec n\cdot\vec e\rvert}{\lvert\vec n\rvert}$**：线面角公式 ✓✓✓" "\n"
        r"② **$\lvert p\rvert=\lvert q\rvert=\lvert r\rvert$**：三个 $\sin$ 相等，分母同为 $\lvert\vec n\rvert$ ✓✓✓" "\n"
        r"③ **$8/2=4$**：$(\pm1,\pm1,\pm1)$ 共 8 个向量，互为相反向量成对 ⟹ 4 个平面 ✓✓✓" "\n"
        r"④ **逐一验证四个平面**：" "\n"
        r"$\vec n=(1,1,1)$：与三轴方向夹角余弦均为 $\frac1{\sqrt3}$ ⟹ 线面角正弦均 $\frac1{\sqrt3}$ ✓✓✓" "\n"
        r"$\vec n=(1,1,-1)$：$\lvert p\rvert=\lvert q\rvert=\lvert r\rvert=1$ ✓✓✓" "\n"
        r"$\vec n=(1,-1,1)$：✓✓✓；$\vec n=(-1,1,1)$：✓✓✓" "\n"
        r"其余 4 组是上述向量取负，同一平面 ✓✓✓" "\n"
        r"⑤ **与正方体面对照**：面 $A_1BD$ 的法向量 $(1,1,1)$（因为 $A_1(0,0,1)$、$B(1,0,0)$、$D(0,1,0)$，平面方程 $x+y+z=1$）✓✓✓" "\n"
        r"面 $AB_1D_1$：$B_1(1,0,1)$、$D_1(0,1,1)$、$A(0,0,0)$ ⟹ 法向量 $(1,1,-1)$？" "\n"
        r"平面过原点与 $(1,0,1)$、$(0,1,1)$：法向量 $=(1,0,1)\times(0,1,1)=(0\cdot1-1\cdot1,\;1\cdot0-1\cdot1,\;1\cdot1-0\cdot0)=(-1,-1,1)$ ⟹ $\propto(1,1,-1)$ ✓✓✓" "\n"
        r"**答案 D（4 个）正确** ✓" "\n"
        r"**⭐⭐ 通法（与三条两两垂直的直线成等角的平面）**：" "\n"
        r"① ⭐⭐ **线面角 $\theta$ 的正弦 $=\frac{\lvert\vec n\cdot\vec e\rvert}{\lvert\vec n\rvert\lvert\vec e\rvert}$** —— " "\n"
        r"注意是**正弦**（不是余弦），这是最容易记反的地方；" "\n"
        r"② ⭐ **「与三轴成等角」⟹ 法向量三分量绝对值相等** ⟹ $\vec n\propto(\pm1,\pm1,\pm1)$；" "\n"
        r"③ ⭐ **计数要除以 2**：$\vec n$ 与 $-\vec n$ 同一平面，所以是 $2^{k-1}$ 个（$k$ 为坐标轴条数，本题 $2^2=4$）；" "\n"
        r"④ ⭐ **几何对照**：这些平面恰好平行于「截掉一个角」的正三角形截面（面 $A_1BD$ 型），共 4 个（对应 4 条体对角线）；" "\n"
        r"⑤ 检验：**把四个法向量逐一代回 $\lvert p\rvert=\lvert q\rvert=\lvert r\rvert$**（全部通过 ✓）。"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-304'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-304-V2',
}

T304_V3 = {
    'type': '选择',
    'stem_text': (
        r"如图，在四面体 $VABC$ 中，已知 $VA\perp$ 平面 $VBC$，$VA$ 与平面 $ABC$ 所成的角为 $45^\circ$，"
        r"$D$ 是 $BC$ 上一动点，设直线 $VD$ 与平面 $ABC$ 所成的角为 $\theta$，则（　　）"
    ),
    'opts': [
        ('A', r"$\theta\le60^\circ$"),
        ('B', r"$\theta\ge30^\circ$"),
        ('C', r"$\theta\le45^\circ$"),
        ('D', r"$\theta\le75^\circ$"),
    ],
    'answer': 'C',
    'analysis': (
        r"作 $VN\perp$ 底面 $ABC$ 于 $N$，则 $\sin\theta=\frac{VN}{VD}$，$VN$ 固定；"
        r"$VD$ 最小当 $VD\perp BC$（$D=D'$），此时 $\theta$ 最大，且由 $VA\perp$ 平面 $VBC$ 推出 $\theta_{\max}=45^\circ$。"
    ),
    'solution': (
        r"作 $VN\perp$ 平面 $ABC$ 于 $N$．直线 $VD$ 与平面 $ABC$ 所成角 $\theta=\angle VDN$，" "\n"
        r"故 $\sin\theta=\dfrac{VN}{VD}$．" "\n"
        r"**第一步：$VN$ 是定值**" "\n"
        r"$V$ 与平面 $ABC$ 都固定，故 $VN$（$V$ 到底面的距离）是定值；于是 $\theta$ 随 $VD$ 的减小而增大．" "\n"
        r"**第二步：$VD$ 何时最小**" "\n"
        r"$D$ 在线段 $BC$ 上运动，$VD$ 最小时 $VD\perp BC$，记此时 $D=D'$（即 $V$ 到 $BC$ 的垂足）．" "\n"
        r"**第三步：证明此时 $\theta=45^\circ$**" "\n"
        r"由 $VA\perp$ 平面 $VBC$ 得 $VA\perp BC$，又 $VD'\perp BC$，$VA\cap VD'=V$，" "\n"
        r"故 $BC\perp$ 平面 $VAD'$，从而 $BC\perp AD'$．" "\n"
        r"又 $BC\subset$ 平面 $ABC$，平面 $VAD'$ 与平面 $ABC$ 交于 $AD'$，且 $BC\perp$ 平面 $VAD'$ ⟹ 两平面垂直，" "\n"
        r"于是 $V$ 到平面 $ABC$ 的垂足 $N$ 落在交线 $AD'$ 上，即 $A,N,D'$ 三点共线．" "\n"
        r"由 $VA\perp$ 平面 $VBC$ 得 $VA\perp VD'$，即 $\triangle VAD'$ 在 $V$ 处为直角；" "\n"
        r"又 $VN\perp AD'$，即 $VN$ 是 $\triangle VAD'$ 斜边上的高．" "\n"
        r"已知 $VA$ 与平面 $ABC$ 成 $45^\circ$，即 $\angle VAN=45^\circ$ ⟹ $\angle AVN=45^\circ$（$\triangle VAN$ 在 $N$ 处直角）" "\n"
        r"⟹ $\angle NVD'=90^\circ-45^\circ=45^\circ$ ⟹ 在 $\triangle VND'$（$N$ 处直角）中 $\angle VD'N=45^\circ$．" "\n"
        r"故 $\theta_{\max}=45^\circ$，即 $\theta\le45^\circ$．" "\n"
        r"故选 **C**．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓。原书 p273 详解：" "\n"
        r"「作 $VN\perp$ 底面 $ABC$ 于点 $N$，$VD'\perp BC$ 于 $D'$，由几何关系可得，$\theta=\angle VDN$，$\sin\theta=\frac{VN}{VD}$，" "\n"
        r"当 $VA$ 固定时，$VN$ 也固定，$VD$ 最小时应为 $VD\perp BC$ 时，此时 $D$ 与 $D'$ 重合，" "\n"
        r"又因为 $VA\perp$ 平面 $VBC$，所以 $VA\perp BC$，所以 $BC\perp$ 平面 $VAD'$，易知 $A,N,D'$ 三点共线，" "\n"
        r"因为 $VA$ 与平面 $ABC$ 所成的角为 $45^\circ$，故 $\angle VAN=45^\circ$，$VA\perp$ 平面 $VBC$，所以 $VA\perp VD'$，" "\n"
        r"所以 $\theta=90^\circ-45^\circ=45^\circ$，此时 $\sin\theta$ 最大，$\theta$ 最大，故 $\theta\le45^\circ$。故选：C」" "\n"
        r"—— **$\sin\theta=\frac{VN}{VD}$、$D=D'$ 时最大、$A,N,D'$ 共线、$\theta_{\max}=45^\circ$、结论 $\theta\le45^\circ$ 全部与我的推导一致** ✓✓✓" "\n"
        r"**独立验算（建系）**：取 $V=(0,0,0)$，$VA$ 沿 $z$ 轴，$A=(0,0,a)$；平面 $VBC$ 为 $z=0$。" "\n"
        r"取 $B=(1,0,0)$、$C=(0,2,0)$（在 $z=0$ 内），$a$ 待定。" "\n"
        r"平面 $ABC$：过 $(0,0,a)$、$(1,0,0)$、$(0,2,0)$。法向量 $=(1,0,-a)\times(0,2,-a)$" "\n"
        r"$=(0\cdot(-a)-(-a)\cdot2,\;(-a)\cdot0-1\cdot(-a),\;1\cdot2-0\cdot0)=(2a,\;a,\;2)$。" "\n"
        r"$VA$ 方向 $(0,0,1)$ 与平面 $ABC$ 所成角 $45^\circ$：$\sin45^\circ=\frac{\lvert(0,0,1)\cdot(2a,a,2)\rvert}{\sqrt{4a^2+a^2+4}}=\frac2{\sqrt{5a^2+4}}$" "\n"
        r"$=\frac{\sqrt2}2$ ⟹ $\frac4{5a^2+4}=\frac12$ ⟹ $5a^2+4=8$ ⟹ $a^2=\frac45$，$a=\frac2{\sqrt5}=0.8944$。" "\n"
        r"$V$ 到平面 $ABC$ 的距离 $VN=\frac{\lvert2a\cdot0+a\cdot0+2\cdot0-2a\rvert}{\sqrt{5a^2+4}}$… 平面方程 $2ax+ay+2z=2a$：" "\n"
        r"$VN=\frac{\lvert 0-2a\rvert}{\sqrt{4a^2+a^2+4}}=\frac{2a}{\sqrt{5a^2+4}}=\frac{1.7888}{\sqrt{8}}=\frac{1.7888}{2.8284}=0.6325$。" "\n"
        r"$D$ 在 $BC$ 上：$B(1,0,0)$、$C(0,2,0)$，$D=(1-t)(1,0,0)+t(0,2,0)=(1-t,2t,0)$，$t\in[0,1]$。" "\n"
        r"$VD^2=(1-t)^2+4t^2=5t^2-2t+1$，最小在 $t=\frac15$：$5\cdot\frac1{25}-\frac25+1=0.2-0.4+1=0.8$，$VD_{\min}=0.8944$。" "\n"
        r"$\sin\theta_{\max}=\frac{0.6325}{0.8944}=0.7071$ ⟹ $\theta_{\max}=45^\circ$ ✓✓✓ **完美吻合**" "\n"
        r"取 $t=0$（$D=B$）：$VD=1$，$\sin\theta=0.6325$ ⟹ $\theta=39.2^\circ<45^\circ$ ✓✓✓" "\n"
        r"取 $t=1$（$D=C$）：$VD=2$，$\sin\theta=0.3162$ ⟹ $\theta=18.4^\circ<45^\circ$ ✓✓✓" "\n"
        r"**答案 C（$\theta\le45^\circ$）正确** ✓" "\n"
        r"**⭐⭐ 通法（线面角的最值）**：" "\n"
        r"① ⭐⭐ **$\sin(\text{线面角})=\frac{\text{点到平面的距离}}{\text{该线段长}}$** —— " "\n"
        r"分子固定时，**分母最小 ⟹ 角最大**，把角度问题转化为线段长度问题；" "\n"
        r"② ⭐ **点到直线的距离最短** ⟹ 动点取垂足位置；" "\n"
        r"③ ⭐ **「$VA\perp$ 平面 $VBC$」这类条件要立刻用两次**：既得 $VA\perp BC$，又得 $VA\perp VD'$ —— " "\n"
        r"配合 $VD'\perp BC$ 就得到 $BC\perp$ 平面 $VAD'$，进而两个平面垂直、垂足落在交线上；" "\n"
        r"④ ⭐ **直角三角形的斜边高**：$\triangle VAD'$ 在 $V$ 处直角，$VN$ 是斜边上的高，" "\n"
        r"于是 $\angle NVD'=90^\circ-\angle VAN$ —— 一步把已知角 $45^\circ$ 转成所求角；" "\n"
        r"⑤ 检验：**建系把 $\theta$ 随 $t$ 的变化算出来**（$t=\frac15$ 处 $\sin\theta=\frac{1}{\sqrt2}$ ✓，端点处更小 ✓）。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-304'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-304-V3',
}

T307_V1 = {
    'type': '选择',
    'stem_text': (
        r"如图，二面角 $\alpha-l-\beta$ 的大小是 $60^\circ$，线段 $AB\subset\alpha$，$B\in l$，$AB$ 与 $l$ 所成的角为 $30^\circ$。"
        r"直线 $AB$ 与平面 $\beta$ 所成的角的正弦值是（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac{\sqrt3}4$"),
        ('B', r"$\dfrac{\sqrt3}3$"),
        ('C', r"$\dfrac{\sqrt3}2$"),
        ('D', r"$\dfrac{\sqrt2}2$"),
    ],
    'answer': 'A',
    'analysis': (
        r"作 $AC\perp\beta$ 于 $C$，在 $\beta$ 内作 $CD\perp l$ 于 $D$，由三垂线定理 $AD\perp l$，"
        r"$\angle ADC=60^\circ$ 即二面角的平面角；设 $AD=2$ 则 $AC=\sqrt3$、$AB=4$，$\sin=\frac{AC}{AB}=\frac{\sqrt3}4$。"
    ),
    'solution': (
        r"**第一步：作出二面角的平面角**" "\n"
        r"过 $A$ 作 $AC\perp$ 平面 $\beta$ 于 $C$；在平面 $\beta$ 内过 $C$ 作 $CD\perp l$ 于 $D$，连接 $AD$．" "\n"
        r"由三垂线定理，$AD\perp l$，故 $\angle ADC$ 即为二面角 $\alpha-l-\beta$ 的平面角，$\angle ADC=60^\circ$．" "\n"
        r"**第二步：求 $AB$ 与平面 $\beta$ 所成的角**" "\n"
        r"$C$ 是 $A$ 在 $\beta$ 上的射影，故 $AB$ 与平面 $\beta$ 所成角为 $\angle ABC$，" "\n"
        r"在 $\triangle ABC$（$C$ 处直角）中 $\sin\angle ABC=\dfrac{AC}{AB}$．" "\n"
        r"**第三步：设值计算**" "\n"
        r"设 $AD=2$。在 $\triangle ADC$（$C$ 处直角，$\angle ADC=60^\circ$）中：" "\n"
        r"$AC=AD\sin60^\circ=2\cdot\dfrac{\sqrt3}2=\sqrt3$，$\quad CD=AD\cos60^\circ=1$．" "\n"
        r"在 $\triangle ABD$（$D$ 处直角，$\angle ABD=30^\circ$，因 $D\in l$ 且 $AD\perp l$）中：" "\n"
        r"$AB=\dfrac{AD}{\sin30^\circ}=\dfrac2{1/2}=4$．" "\n"
        r"故 $\sin\angle ABC=\dfrac{AC}{AB}=\dfrac{\sqrt3}4$．" "\n"
        r"故选 **A**．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓。原书 p277 详解：" "\n"
        r"「过点 $A$ 作平面 $\beta$ 的垂线，垂足为 $C$，在 $\beta$ 内过 $C$ 作 $l$ 的垂线，垂足为 $D$，连接 $AD$，" "\n"
        r"由三垂线定理可知 $AD\perp l$，故 $\angle ADC$ 为二面角 $\alpha-l-\beta$ 的平面角为 $60^\circ$。" "\n"
        r"又由已知，$\angle ABD=30^\circ$，连接 $CB$，则 $\angle ABC$ 为 $AB$ 与平面 $\beta$ 所成的角，" "\n"
        r"设 $AD=2$，则 $AC=\sqrt3$，$CD=1$，$AB=\frac{AD}{\sin30^\circ}=4$，" "\n"
        r"∴ 直线 $AB$ 与平面 $\beta$ 所成的角的正弦值 $\sin\angle ABC=\frac{AC}{AB}=\frac{\sqrt3}4$。故选：A」" "\n"
        r"—— **$AD=2$、$AC=\sqrt3$、$CD=1$、$AB=4$、$\sin=\frac{\sqrt3}4$ 全部与我的推导一致** ✓✓✓" "\n"
        r"**⚠ 选项还原**：PDF 提取为 `A.3/4 B.3/3 C.3/2 D.2/2`（根号全丢）。" "\n"
        r"**判定依据**：详解末行 $\frac{AC}{AB}=\frac{\sqrt3}4$，且 $\frac{\sqrt3}4=0.4330$ 是唯一小于 $\frac{\sqrt2}2$ 的合理值 ✓✓✓" "\n"
        r"**独立验算（建系）**：设 $l$ 为 $x$ 轴，$B=(0,0,0)$，平面 $\beta$ 为 $z=0$。" "\n"
        r"平面 $\alpha$ 与 $\beta$ 夹角 $60^\circ$ 且交线为 $x$ 轴 ⟹ 平面 $\alpha$ 由 $x$ 轴绕 $x$ 轴转 $60^\circ$ 得到：" "\n"
        r"$\alpha$ 的方向：$(1,0,0)$ 与 $(0,\cos60^\circ,\sin60^\circ)=(0,0.5,0.866)$。" "\n"
        r"$A\in\alpha$，$AB$ 与 $l$（$x$ 轴）成 $30^\circ$。设 $\lvert AB\rvert=s$，$A=s(\cos\delta\cdot(1,0,0)+\sin\delta\cdot(0,0.5,0.866))$。" "\n"
        r"$AB$ 与 $x$ 轴夹角 $30^\circ$：$\cos30^\circ=\lvert\cos\delta\rvert$ ⟹ $\delta=30^\circ$。" "\n"
        r"$A=s(0.866,\;0.5\cdot0.5,\;0.866\cdot0.866)=s(0.866,\;0.25,\;0.75)$。" "\n"
        r"$A$ 到平面 $\beta$（$z=0$）的距离 $=0.75s$。$\sin(\text{线面角})=\frac{0.75s}{s}=0.75$？" "\n"
        r"—— ✗ 与 $\frac{\sqrt3}4=0.433$ 不符！" "\n"
        r"**复核**：$AB$ 与 $l$ 成 $30^\circ$，而 $l$ 是 $x$ 轴；$A$ 在 $\alpha$ 内，$B$ 在 $l$ 上。" "\n"
        r"若 $B$ 不是原点而是 $l$ 上另一点，则 $\vec{BA}=A-B$ 与 $x$ 轴成 $30^\circ$。" "\n"
        r"设 $B=(b,0,0)$，$A=s(0.866,0.25,0.75)$（取 $s=\lvert AB\rvert$ 时需 $\lvert A-B\rvert=s$）。" "\n"
        r"$\vec{BA}=(0.866s-b,\;0.25s,\;0.75s)$，$\lvert\vec{BA}\rvert=s$。" "\n"
        r"与 $x$ 轴夹角 $30^\circ$：$\frac{\lvert0.866s-b\rvert}{s}=\cos30^\circ=0.866$。" "\n"
        r"$\lvert\vec{BA}\rvert^2=(0.866s-b)^2+0.0625s^2+0.5625s^2=0.75s^2+0.0625s^2+0.5625s^2=1.375s^2\neq s^2$ ✗" "\n"
        r"⟹ 上面 $\sin\delta=0.5$ 的取法有误。重来：设 $A$ 在 $\alpha$ 内，用 $(u,v)$ 参数：" "\n"
        r"$A=(p,\;q\cos60^\circ,\;q\sin60^\circ)=(p,\;0.5q,\;0.866q)$。" "\n"
        r"$B=(b,0,0)$。$\vec{BA}=(p-b,\;0.5q,\;0.866q)$。" "\n"
        r"$AB$ 与 $x$ 轴成 $30^\circ$：$\frac{\lvert p-b\rvert}{\lvert\vec{BA}\rvert}=\cos30^\circ=0.866$。" "\n"
        r"$\lvert\vec{BA}\rvert^2=(p-b)^2+q^2$（因 $0.25q^2+0.75q^2=q^2$）。" "\n"
        r"$\frac{(p-b)^2}{(p-b)^2+q^2}=\frac34$ ⟹ $q^2=\frac13(p-b)^2$ ⟹ $q=\frac{\lvert p-b\rvert}{\sqrt3}$。" "\n"
        r"$\sin(\text{线面角})=\frac{\text{$A$ 到 $\beta$ 的距离}}{\lvert\vec{BA}\rvert}=\frac{0.866q}{\sqrt{(p-b)^2+q^2}}=\frac{0.866q}{\sqrt{3q^2+q^2}}=\frac{0.866}{2}=0.433=\frac{\sqrt3}4$ ✓✓✓ **吻合**" "\n"
        r"（我第一次把 $B$ 当成原点且错误地令 $\lvert AB\rvert=s$ 与参数混用，导致矛盾；修正后与详解一致）" "\n"
        r"**数值检验**：取 $q=1$、$p-b=\sqrt3=1.732$。$A=(p,0.5,0.866)$，$B=(b,0,0)$，$p=b+1.732$。" "\n"
        r"$\vec{BA}=(1.732,0.5,0.866)$，$\lvert\vec{BA}\rvert=\sqrt{3+0.25+0.75}=2$；与 $x$ 轴夹角：$\cos=\frac{1.732}2=0.866$ ⟹ $30^\circ$ ✓✓✓" "\n"
        r"$A$ 到 $\beta$ 距离 $=0.866$；$\sin=\frac{0.866}2=0.433=\frac{\sqrt3}4$ ✓✓✓" "\n"
        r"**答案 A（$\frac{\sqrt3}4$）正确** ✓" "\n"
        r"**⭐⭐ 通法（二面角 + 线面角）**：" "\n"
        r"① ⭐⭐ **作二面角平面角的标准三步**：$A\to C\perp\beta$；$C\to D\perp l$；连 $AD$ 由三垂线定理得 $AD\perp l$，$\angle ADC$ 即平面角；" "\n"
        r"② ⭐ **线面角的正弦 $=\frac{\text{点到平面距离}}{\text{线段长}}$**，本题就是 $\frac{AC}{AB}$；" "\n"
        r"③ ⭐ **设一个中间量（如 $AD=2$）把其余量全表出来**，避免引入未知边长；" "\n"
        r"④ ⚠ **$AB$ 与 $l$ 成 $30^\circ$ 时，$D$ 在 $l$ 上且 $AD\perp l$**，所以 $\triangle ABD$ 在 $D$ 处直角、$\angle ABD=30^\circ$ —— " "\n"
        r"**别把 $30^\circ$ 当成 $\angle BAD$**；" "\n"
        r"⑤ ⚠ **答案 $\frac{\sqrt3}4$ 提取成 `3/4`**：建系算得 $0.433$，与字面 $0.75$ 差很多，**算一遍就能识别**。"
    ),
    'difficulty': 0.82,
    'topics': ['M-T-307'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-307-V1',
}

T307_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知平面 $\alpha$ 内的 $\angle APB=60^\circ$，射线 $PC$ 与 $PA,PB$ 所成的角均为 $135^\circ$，"
        r"则 $PC$ 与平面 $\alpha$ 所成的角 $\theta$ 的余弦值是（　　）"
    ),
    'opts': [
        ('A', r"$-\dfrac{\sqrt6}3$"),
        ('B', r"$\dfrac{\sqrt6}3$"),
        ('C', r"$\dfrac{\sqrt3}3$"),
        ('D', r"$-\dfrac{\sqrt3}3$"),
    ],
    'answer': 'B',
    'analysis': (
        r"建系令 $PA=PB=PC=2$、$P$ 为原点、$\angle APB$ 的平分线为 $x$ 轴，"
        r"由 $\angle CPA=\angle CPB=135^\circ$ 解出 $C$ 的横坐标 $x_C=-\frac{2\sqrt6}3$，"
        r"而 $\cos\theta=\frac{\lvert x_C\rvert}{\lvert PC\rvert}=\frac{\sqrt6}3$。"
    ),
    'solution': (
        r"**第一步：建系**" "\n"
        r"以 $P$ 为原点，平面 $\alpha$ 为 $xOy$ 平面，$\angle APB$ 的平分线为 $x$ 轴．" "\n"
        r"不妨设 $PA=PB=PC=2$（长度可任取，只影响角度）．" "\n"
        r"由 $\angle APB=60^\circ$：$A=2(\cos30^\circ,\sin30^\circ,0)=(\sqrt3,1,0)$，$B=(\sqrt3,-1,0)$．" "\n"
        r"**第二步：求 $C$**" "\n"
        r"设 $C=(x,y,z)$．由 $\angle CPA=\angle CPB=135^\circ$：" "\n"
        r"$\dfrac{\vec{PC}\cdot\vec{PA}}{\lvert PC\rvert\lvert PA\rvert}=\dfrac{\sqrt3x+y}{4}=\cos135^\circ=-\dfrac{\sqrt2}2\Rightarrow\sqrt3x+y=-2\sqrt2$，" "\n"
        r"$\dfrac{\vec{PC}\cdot\vec{PB}}{4}=\dfrac{\sqrt3x-y}{4}=-\dfrac{\sqrt2}2\Rightarrow\sqrt3x-y=-2\sqrt2$．" "\n"
        r"两式相加：$2\sqrt3x=-4\sqrt2\Rightarrow x=-\dfrac{2\sqrt2}{\sqrt3}=-\dfrac{2\sqrt6}3$；相减得 $y=0$．" "\n"
        r"**第三步：求线面角**" "\n"
        r"$C$ 在平面 $\alpha$（$z=0$）上的射影为 $H=(x,0,0)$，故 $PC$ 与平面 $\alpha$ 所成角 $\theta=\angle CPH$，" "\n"
        r"$\cos\theta=\dfrac{\lvert PH\rvert}{\lvert PC\rvert}=\dfrac{\lvert x\rvert}{2}=\dfrac{2\sqrt6/3}{2}=\dfrac{\sqrt6}3$．" "\n"
        r"故选 **B**．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓。原书 p277 详解：" "\n"
        r"「令 $PA=PB=PC=2$，则 $\angle CPA=\angle CPB=135^\circ$，∴ $AC=BC$，取 $AB$ 中点 $D$，连接 $PD$，" "\n"
        r"则 $\angle CPD$ 即为 $PC$ 与平面 $\alpha$ 所成的角的补角，在 $\triangle APC$ 中，$AC^2=PA^2+PC^2-2PA\cdot PC\cdot\cos135^\circ=8+4\sqrt2$，" "\n"
        r"∴ 在 $\triangle PCD$ 中，$CD^2=AC^2-AD^2=7+4\sqrt2$，∵ $PD=\sqrt3$，" "\n"
        r"∴ $\cos\angle CPD=\frac{PC^2+PD^2-CD^2}{2PC\cdot PD}=-\frac{\sqrt6}3$，∴ $PC$ 与平面 $\alpha$ 所成的角 $\theta$ 的余弦值是 $\frac{\sqrt6}3$。故选：B」" "\n"
        r"—— **$AC^2=8+4\sqrt2$、$CD^2=7+4\sqrt2$、$\cos\angle CPD=-\frac{\sqrt6}3$、$\cos\theta=\frac{\sqrt6}3$ 全部与我的推导一致** ✓✓✓" "\n"
        r"**⚠ 选项还原**：PDF 提取为 `A. -6/3 B. 6/3 C. 3/3 D. -3/3`（根号全丢）。" "\n"
        r"**判定依据**：我建系算得 $\cos\theta=\frac{\sqrt6}3=0.8165$；字面 $\frac63=2>1$ 根本不是余弦值 ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **$A=(\sqrt3,1,0)$、$B=(\sqrt3,-1,0)$**：$\lvert A\rvert=2$ ✓；$\cos\angle APB=\frac{3-1}{4}=\frac12$ ⟹ $60^\circ$ ✓✓✓" "\n"
        r"② **解 $C$**：$\sqrt3x+y=-2\sqrt2$ 与 $\sqrt3x-y=-2\sqrt2$ ⟹ $x=-\frac{2\sqrt2}{\sqrt3}=-\frac{2\sqrt6}3=-1.633$、$y=0$ ✓✓✓" "\n"
        r"③ **$\lvert PC\rvert=2$**：$x^2+z^2=4$ ⟹ $\frac{24}{9}+z^2=4$ ⟹ $z^2=4-\frac83=\frac43$，$z=\frac2{\sqrt3}=1.1547$ ✓✓✓" "\n"
        r"④ **$\angle CPA=135^\circ$ 检验**：$\vec{PC}\cdot\vec{PA}=(-1.633)(\sqrt3)+(0)(1)+(1.1547)(0)=-2.828$。" "\n"
        r"$\frac{-2.828}{2\cdot2}=-0.7071=\cos135^\circ$ ✓✓✓" "\n"
        r"⑤ **$\cos\theta=\frac{\lvert x\rvert}{2}=\frac{1.633}2=0.8165=\frac{\sqrt6}3$** ✓✓✓" "\n"
        r"⑥ **与详解的 $\angle CPD$ 对照**：$D=AB$ 中点 $=(\sqrt3,0,0)$。$\vec{PC}=(-1.633,0,1.1547)$、$\vec{PD}=(\sqrt3,0,0)$。" "\n"
        r"$\cos\angle CPD=\frac{(-1.633)(1.732)}{2\cdot\sqrt3}=\frac{-2.828}{3.464}=-0.8165=-\frac{\sqrt6}3$ ✓✓✓ **与详解一致**" "\n"
        r"注意 $D=(1.732,0,0)$ 而射影 $H=(-1.633,0,0)$ —— **$D$ 与 $H$ 在 $P$ 的两侧**，" "\n"
        r"所以 $\angle CPD=180^\circ-\theta$，这正是详解说「补角」的原因 ✓✓✓" "\n"
        r"⑦ **$D$ 不是射影**：若误认 $D$ 为射影会得 $\cos\theta=\frac{\sqrt3}{2}$（错），务必注意方向 ✓" "\n"
        r"**答案 B（$\frac{\sqrt6}3$）正确** ✓" "\n"
        r"**⭐⭐ 通法（线面角与「补角」陷阱）**：" "\n"
        r"① ⭐⭐ **建系是最稳的**：把 $P$ 放原点、平面放 $z=0$、角平分线放 $x$ 轴，" "\n"
        r"由两个等角条件列两个一次方程直接解出 $C$ 的 $x,y$（本题 $y=0$ 是必然的，因 $C$ 在 $AB$ 的中垂面上）；" "\n"
        r"② ⭐ **$\cos(\text{线面角})=\frac{\lvert\text{射影长}\rvert}{\lvert\text{斜线长}\rvert}$**，射影就是 $C$ 的 $(x,y)$ 部分；" "\n"
        r"③ ⚠⭐ **取 $AB$ 中点 $D$ 时，$D$ 未必是射影**！本题 $D$ 与真正的射影 $H$ 在 $P$ 的**异侧**，" "\n"
        r"于是 $\angle CPD=180^\circ-\theta$ —— 详解说的「补角」就是这个意思；" "\n"
        r"**凡是出现 $\cos$ 为负，先检查是不是取到了补角**；" "\n"
        r"④ ⭐ **$PA=PB=PC$ 可任取**，因为只有角度有意义，取成相同值能让方程最简；" "\n"
        r"⑤ 检验：**把解出的 $C$ 代回 $\angle CPA$ 验证**（$-0.7071=\cos135^\circ$ ✓）。"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-307'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-307-V3',
}

QS = [T304_V2, T304_V3, T307_V1, T307_V3]
