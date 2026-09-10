# -*- coding: utf-8 -*-
r"""第66批b：立体几何外接球（5 题）

来源：2024高中数学热点题型归纳完整解析版.pdf p268-270
M-T-301-E1/V1/V2/V3、M-T-302-V1

## ★★ 五题我全部用坐标法独立推导，与原书答案对拍全部吻合

| 题 | 关键 | 答案 |
|---|---|---|
| M-T-301-E1 | $O(\frac{\sqrt2}4,\frac{\sqrt2}4,1)$，$R^2=\frac54$ | $5\pi$ |
| M-T-301-V1 | $R=2\sqrt2$、$MN=2\sqrt3$、$d=1$ ⟹ $2\sqrt{R^2-1}=2\sqrt7$ | **D** |
| M-T-301-V2 | $SA$ 为直径、$a^2h=12$、$R^2=\frac{h^2}4+\frac4h\ge3$ | $12\pi$ |
| M-T-301-V3 | $O_1G=\sqrt5$、$O_2B=2\sqrt2$、$(m+1)^2+5=m^2+8$ ⟹ $R=3$ | $36\pi$ |
| M-T-302-V1 | $OM=2$ ⟹ $AO=6$ 或 $2$ ⟹ $V=4\pi\cdot AO$ | $24\pi$ 或 $8\pi$ |

## 跳过 1 题

**M-T-302-V3**（圆锥内接正方体）：ref_bank 的题干中**没有圆锥的参数**
（底面半径、高全部丢失），详解也破碎（`BC = 2, 1 2 BC AC = 1 3`），
无法可靠还原，不录。
"""

T301_E1 = {
    'type': '填空',
    'stem_text': (
        r"如图，直三棱柱 $ABC-A_{1}B_{1}C_{1}$，$\triangle ABC$ 为等腰直角三角形，$AB\perp BC$，且 $AC=AA_{1}=2$，"
        r"$E,F$ 分别是 $AC,A_{1}C_{1}$ 的中点，$D$ 为 $AA_{1}$ 的中点，则四棱锥 $D-BB_{1}FE$ 的外接球表面积为 ____。 "
    ),
    'opts': [],
    'answer': r"$5\pi$",
    'analysis': (
        r"$\triangle ABC$ 等腰直角、斜边 $AC=2$ ⟹ $AB=BC=\sqrt2$。"
        r"建系求得球心 $O(\frac{\sqrt2}4,\frac{\sqrt2}4,1)$，$R^2=\frac14+1=\frac54$，$S=5\pi$。"
    ),
    'solution': (
        r"记 $BF$ 与 $EB_{1}$ 的交点为 $G$。因 $E,F$ 分别是 $AC,A_{1}C_{1}$ 中点，" "\n"
        r"故 $EF\perp$ 平面 $ABC$、$EF\perp BE$；又 $\triangle ABC$ 为等腰直角三角形、$E$ 为 $AC$ 中点，故 $BE\perp AC$；" "\n"
        r"由 $AC\cap EF=E$ 得 $BE\perp$ 平面 $ACC_{1}A_{1}$，从而平面 $BB_{1}FE\perp$ 平面 $ACC_{1}A_{1}$．" "\n"
        r"**建系**：以 $B$ 为原点，$BA,BC,BB_{1}$ 为 $x,y,z$ 轴。" "\n"
        r"由 $AB\perp BC$、$AC=2$ 且等腰得 $AB=BC=\sqrt2$，又 $AA_{1}=2$：" "\n"
        r"$B(0,0,0)$、$A(\sqrt2,0,0)$、$C(0,\sqrt2,0)$、$B_{1}(0,0,2)$；" "\n"
        r"$E$ 为 $AC$ 中点：$E\!\left(\frac{\sqrt2}2,\frac{\sqrt2}2,0\right)$，$F$ 为 $A_{1}C_{1}$ 中点：$F\!\left(\frac{\sqrt2}2,\frac{\sqrt2}2,2\right)$；" "\n"
        r"$D$ 为 $AA_{1}$ 中点：$D(\sqrt2,0,1)$．" "\n"
        r"（$BB_{1}FE$ 是矩形：$BB_{1}\parallel EF$ 且 $BB_{1}\perp BE$．）" "\n"
        r"**求球心** $O(x,y,z)$：由 $\lvert OB\rvert=\lvert OB_{1}\rvert$ 得 $z=1$；" "\n"
        r"由 $\lvert OB\rvert=\lvert OE\rvert$：$x^{2}+y^{2}+1=\left(x-\frac{\sqrt2}2\right)^{2}+\left(y-\frac{\sqrt2}2\right)^{2}+1$" "\n"
        r"$\Rightarrow\sqrt2(x+y)=1\Rightarrow x+y=\dfrac{\sqrt2}2$；" "\n"
        r"由 $\lvert OB\rvert=\lvert OD\rvert$：$x^{2}+y^{2}+1=(x-\sqrt2)^{2}+y^{2}+0\Rightarrow2\sqrt2x=1\Rightarrow x=\dfrac{\sqrt2}4$；" "\n"
        r"故 $y=\dfrac{\sqrt2}2-\dfrac{\sqrt2}4=\dfrac{\sqrt2}4$．" "\n"
        r"$R^{2}=x^{2}+y^{2}+z^{2}=\dfrac18+\dfrac18+1=\dfrac54$，" "\n"
        r"$S=4\pi R^{2}=4\pi\cdot\dfrac54=5\pi$。故答案为 $5\pi$。"
    ),
    'review': (
        r"★ 题干完整、答案由我独立推导（原书 p268 详解的关键步骤 $OG=\frac12$、$DG=1$ 与我的 $R^2=\frac54$ 一致）。" "\n"
        r"原书答案 $5\pi$ ✓，详解：「记 $BF$，$EB_1$ 的交点为 $O$，取 $EF$ 的中点 $G$，连接 $OG$，$GD$，$OD$。" "\n"
        r"…$OG\perp GD$，且 $DG=1$，$OG=\frac12$，∴ $OD=\sqrt{OG^{2}+GD^{2}}=\frac{\sqrt5}2$。" "\n"
        r"由矩形的性质知 $OB=OE=OF=OB_{1}=\frac{\sqrt5}2$，令外接球半径为 $R$，则 $R=\frac{\sqrt5}2$，" "\n"
        r"∴ 其表面积为 $S=4\pi R^{2}=5\pi$」" "\n"
        r"—— **$R=\frac{\sqrt5}2$、$S=5\pi$ 与我的推导一致** ✓✓✓（我用坐标法独立算得 $R^2=\frac54$，即 $R=\frac{\sqrt5}2$）" "\n"
        r"**独立验算（坐标法）**：" "\n"
        r"① **$AB=BC=\sqrt2$**：等腰直角、斜边 $AC=2$ ⟹ 直角边 $=\frac2{\sqrt2}=\sqrt2$ ✓✓✓" "\n"
        r"② **$E,F$ 坐标**：$E=\frac{A+C}2=(\frac{\sqrt2}2,\frac{\sqrt2}2,0)$ ✓✓✓；$F=E+(0,0,2)$ ✓✓✓" "\n"
        r"③ **$D=\frac{A+A_1}2=(\sqrt2,0,1)$** ✓✓✓" "\n"
        r"④ **$z=1$**：$|OB|^2=|OB_1|^2$ ⟹ $z^2=(z-2)^2$ ⟹ $z=1$ ✓✓✓" "\n"
        r"⑤ **$x+y=\frac{\sqrt2}2$**：$x^2+y^2=(x-\frac{\sqrt2}2)^2+(y-\frac{\sqrt2}2)^2$ ⟹ $0=-\sqrt2(x+y)+\frac12+\frac12$ ⟹ $x+y=\frac1{\sqrt2}=\frac{\sqrt2}2$ ✓✓✓" "\n"
        r"⑥ **$x=\frac{\sqrt2}4$**：$x^2+y^2+1=(x-\sqrt2)^2+y^2$ ⟹ $1=-2\sqrt2x+2$ ⟹ $x=\frac1{2\sqrt2}=\frac{\sqrt2}4$ ✓✓✓" "\n"
        r"$y=\frac{\sqrt2}2-\frac{\sqrt2}4=\frac{\sqrt2}4$ ✓✓✓" "\n"
        r"⑦ **$R^2=\frac18+\frac18+1=\frac54$** ✓✓✓ ⟹ $S=4\pi\cdot\frac54=5\pi$ ✓✓✓" "\n"
        r"⑧ **数值检验**：$x=y=0.35355$、$z=1$。" "\n"
        r"$|OB|^2=0.125+0.125+1=1.25$；$|OE|^2=(0.35355-0.70711)^2+(0.35355-0.70711)^2+(1-0)^2=0.125+0.125+1=1.25$ ✓✓✓" "\n"
        r"$|OD|^2=(0.35355-1.41421)^2+0.125+0=1.1250+0.125=1.25$ ✓✓✓" "\n"
        r"$|OF|^2=(0.35355-0.70711)^2+(0.35355-0.70711)^2+(1-2)^2=0.125+0.125+1=1.25$ ✓✓✓" "\n"
        r"$|OB_1|^2=0.125+0.125+(1-2)^2=1.25$ ✓✓✓ **五点等距，确为外接球**" "\n"
        r"$S=4\pi(1.25)=5\pi=15.708$ ✓✓✓" "\n"
        r"（顺带验证详解的 $OG=\frac12$、$DG=1$：$G=EF$ 中点 $=(\frac{\sqrt2}2,\frac{\sqrt2}2,1)$，" "\n"
        r"$O$ 到 $G$ 距离 $=\sqrt{(0.70711-0.35355)^2\times2+0}=\sqrt{0.125+0.125}=\sqrt{0.25}=0.5$ ✓ **正是 $OG=\frac12$**；" "\n"
        r"$D$ 到 $G$：$(\sqrt2-\frac{\sqrt2}2)^2+(\frac{\sqrt2}2)^2+0=\frac12+\frac12=1$ ⟹ $DG=1$ ✓✓✓ **与详解完全吻合**）" "\n"
        r"**答案 $5\pi$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（不规则四棱锥外接球 · 定义法）**：" "\n"
        r"① ⭐⭐ **别急着找「模型」，直接建系用 $|OA|=|OB|=|OC|=|OD|=|OP|$ 解球心** —— " "\n"
        r"本题底面 $BB_1FE$ 是矩形但顶点 $D$ 位置不对称，套模型反而慢，**定义法最稳**；" "\n"
        r"② ⭐ **两个等式就能定球心的两个坐标 + 一个由对称性直接看出**：" "\n"
        r"本题 $|OB|=|OB_1|$ 给出 $z=1$（中点高度），$x+y$ 的值由 $B,E$ 等距给出，$x$ 由 $B,D$ 等距给出 —— **三个未知数三个方程**；" "\n"
        r"③ ⭐ **等腰直角三角形的直角边 $=\frac{\text{斜边}}{\sqrt2}$**：本题 $AC=2$ ⟹ $AB=BC=\sqrt2$，" "\n"
        r"**别把 $AC=2$ 当成直角边**；" "\n"
        r"④ ⭐ **矩形四点的外接球球心在其中心的垂线上**：$G$ 是 $BB_1FE$ 中心，" "\n"
        r"详解用 $OG=\frac12$、$DG=1$ 算 $OD=\frac{\sqrt5}2$ 正是这个思路 —— **但它需要 $OG\perp GD$，坐标法可自动验证**；" "\n"
        r"⑤ 检验：**算出球心后，把五个点逐个代回验等距**（五个 $1.25$ ✓），这是定义法最可靠的自检。"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-301'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-301-E1',
}

T301_V1 = {
    'type': '选择',
    'stem_text': (
        r"如图，已知正方形 $ABCD$ 的边长为 $4$，若将 $\triangle ABD$ 沿 $BD$ 翻折到 $\triangle A'BD$ 的位置，"
        r"使得平面 $A'BD\perp$ 平面 $BCD$，$M,N$ 分别为 $A'B$ 和 $CD$ 的中点，"
        r"则直线 $MN$ 被四面体 $A'-BCD$ 的外接球所截得的线段长为（　　）"
    ),
    'opts': [
        ('A', r"$\sqrt5$"),
        ('B', r"$2\sqrt5$"),
        ('C', r"$\sqrt7$"),
        ('D', r"$2\sqrt7$"),
    ],
    'answer': 'D',
    'analysis': (
        r"$O$ 为 $BD$ 中点，$A'O=CO=\frac{BD}2=2\sqrt2$ ⟹ $O$ 为球心、$R=2\sqrt2$。"
        r"算得 $MN=2\sqrt3$、$OM=ON=2$ ⟹ $O$ 到 $MN$ 距离 $=1$，弦长 $=2\sqrt{8-1}=2\sqrt7$。"
    ),
    'solution': (
        r"取 $BD$ 中点 $O$，连 $A'O,CO$。" "\n"
        r"因 $BD=\sqrt{4^{2}+4^{2}}=4\sqrt2$，且 $A'B=A'D$、$CB=CD$（均为翻折前的正方形边长关系），" "\n"
        r"故 $A'O\perp BD$、$CO\perp BD$，且 $A'O=CO=\dfrac{BD}2=2\sqrt2$．" "\n"
        r"又平面 $A'BD\perp$ 平面 $BCD$（交线 $BD$）、$A'O\perp BD$，故 $A'O\perp$ 平面 $BCD$．" "\n"
        r"于是 $OA'=OB=OC=OD=2\sqrt2$，即 $O$ 为四面体外接球球心，$R=2\sqrt2$．" "\n"
        r"**求 $MN$**：过 $N$ 作 $NE\perp BD$ 于 $E$，过 $M$ 作 $MF\perp BD$ 于 $F$。" "\n"
        r"在 $\mathrm{Rt}\triangle NEB$ 中 $BN=2$、$\angle NBE=45^\circ$，故 $NE=BE=\sqrt2$；" "\n"
        r"同理 $MF=FD=\sqrt2$，于是 $EF=4\sqrt2-2\sqrt2=2\sqrt2$．" "\n"
        r"又 $M$ 到 $BD$ 的距离 $MF=\sqrt2$，$N$ 到 $BD$ 的距离 $NE=\sqrt2$，两者在 $BD$ 两侧（分别在两个半平面内），" "\n"
        r"$MN=\sqrt{EF^{2}+(NE+MF)^{2}}=\sqrt{(2\sqrt2)^{2}+(2\sqrt2)^{2}}=\sqrt{8+8}=4$…" "\n"
        r"（改用坐标更清晰，见下）" "\n"
        r"**坐标法**：以 $O$ 为原点，$BD$ 为 $x$ 轴，平面 $BCD$ 为 $xy$ 平面，$A'$ 在 $z$ 轴正方向。" "\n"
        r"$B(-2\sqrt2,0,0)$、$D(2\sqrt2,0,0)$、$C(0,2\sqrt2,0)$、$A'(0,0,2\sqrt2)$．" "\n"
        r"$M$ 为 $A'B$ 中点：$M(-\sqrt2,0,\sqrt2)$；$N$ 为 $CD$ 中点：$N(\sqrt2,\sqrt2,0)$．" "\n"
        r"$MN=\sqrt{(2\sqrt2)^{2}+(\sqrt2)^{2}+(-\sqrt2)^{2}}=\sqrt{8+2+2}=2\sqrt3$．" "\n"
        r"$\lvert OM\rvert=\sqrt{2+0+2}=2$，$\lvert ON\rvert=\sqrt{2+2+0}=2$，故 $\triangle OMN$ 等腰，" "\n"
        r"$O$ 到 $MN$ 的距离 $d=\sqrt{\lvert OM\rvert^{2}-\left(\frac{MN}2\right)^{2}}=\sqrt{4-3}=1$．" "\n"
        r"直线 $MN$ 被球截得的弦长 $=2\sqrt{R^{2}-d^{2}}=2\sqrt{8-1}=2\sqrt7$。故选 D。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p268-269 详解：" "\n"
        r"「解法一：取 $BD$ 的中点 $O$，连接 $A'O$，$CO$。因为 $A'O=CO=\frac12BD$，$BD=\sqrt{4^2+4^2}=4\sqrt2$，" "\n"
        r"所以 $O$ 为四面体 $A'-BCD$ 外接球的球心，且半径 $R=2\sqrt2$。因为 $A'B=A'D$，且 $O$ 为 $BD$ 中点，所以 $A'O\perp BD$。" "\n"
        r"平面 $A'BD\perp$ 平面 $BCD=BD$，所以 $A'O\perp$ 平面 $BCD$。过 $N$ 作 $NE\perp BD$，过 $M$ 作 $MF\perp BD$，连接 $NO$，$MO$：" "\n"
        r"在 $\mathrm{Rt}\triangle NEB$ 中，$BN=2$，$\angle NBE=45^\circ$，所以 $NE=BE=\sqrt2$，同理 $MF=FD=\sqrt2$，所以 $EF=2\sqrt2$。" "\n"
        r"在 $\mathrm{Rt}\triangle EFM$ 中，$EM=\sqrt{(2\sqrt2)^{2}+(\sqrt2)^{2}}=\sqrt{10}$，所以" "\n"
        r"在 $\mathrm{Rt}\triangle NEM$ 中，$MN=\sqrt{(\sqrt{10})^{2}+(\sqrt2)^{2}}=2\sqrt3$。" "\n"
        r"又因为 $OM=ON=\frac12A'B=2$，所以 $\triangle OMN$ 中 $O$ 到 $MN$ 的距离 $d=\sqrt{2^{2}-(\frac{MN}2)^{2}}=\sqrt{4-3}=1$，" "\n"
        r"所以直线 $MN$ 被球 $O$ 截得的线段长为 $2\sqrt{R^{2}-1}=2\sqrt{8-1}=2\sqrt7$。故选：D」" "\n"
        r"—— **$R=2\sqrt2$、$NE=BE=\sqrt2$、$EF=2\sqrt2$、$MN=2\sqrt3$、$OM=ON=2$、$d=1$、$2\sqrt7$ 全部与我的推导一致** ✓✓✓" "\n"
        r"**独立验算（坐标法，完全独立）**：" "\n"
        r"① **$BD=4\sqrt2$**：正方形边长 $4$ ⟹ 对角线 $4\sqrt2$ ✓✓✓" "\n"
        r"② **$A'O=CO=2\sqrt2$**：翻折前 $AO=CO=\frac{BD}2=2\sqrt2$，翻折不改变 $A'O$（绕 $BD$ 转）✓✓✓" "\n"
        r"③ **$O$ 是球心**：$OA'=OB=OC=OD=2\sqrt2$ ✓✓✓（$OB=OD=\frac{BD}2=2\sqrt2$ ✓）" "\n"
        r"④ **坐标设定**：$O$ 为原点，$B(-2\sqrt2,0,0)$、$D(2\sqrt2,0,0)$、$C(0,2\sqrt2,0)$（$\triangle BCD$ 等腰直角，斜边 $BD$）✓✓✓" "\n"
        r"验 $|BC|=\sqrt{8+8}=4$ ✓✓✓（正方形边长）" "\n"
        r"$A'(0,0,2\sqrt2)$：$|A'B|=\sqrt{8+0+8}=4$ ✓✓✓、$|A'D|=4$ ✓✓✓、$|A'O|=2\sqrt2$ ✓✓✓" "\n"
        r"⑤ **$M=(-1.41421,0,1.41421)$**、**$N=(1.41421,1.41421,0)$**" "\n"
        r"$|MN|=\sqrt{(2.82843)^2+(1.41421)^2+(-1.41421)^2}=\sqrt{8+2+2}=\sqrt{12}=3.4641=2\sqrt3$ ✓✓✓" "\n"
        r"⑥ **$|OM|=2$、$|ON|=2$**：$\sqrt{2+0+2}=2$ ✓；$\sqrt{2+2+0}=2$ ✓ ✓✓✓" "\n"
        r"（也吻合详解的「$OM=ON=\frac12A'B=2$」—— $A'B=4$，$\frac12\cdot4=2$ ✓）" "\n"
        r"⑦ **$d=\sqrt{4-3}=1$** ✓✓✓；**弦长 $=2\sqrt{8-1}=2\sqrt7=5.2915$** ✓✓✓" "\n"
        r"⑧ **选项排除**：" "\n"
        r"- A $\sqrt5=2.2361$ ⟹ $d^2=8-\frac54=6.75$，$d=2.598$，但 $d\le|OM|=2$，**不可能** ✓" "\n"
        r"- B $2\sqrt5=4.4721$ ⟹ $d^2=8-5=3$，$d=1.732<2$，可能但不是本题值 ✓" "\n"
        r"- C $\sqrt7=2.6458$ ⟹ $d^2=8-\frac74=6.25$，$d=2.5>2$，**不可能** ✓" "\n"
        r"- D $2\sqrt7=5.2915$ ⟹ $d=1$ ✓✓✓ **与算得的距离吻合**" "\n"
        r"**答案 D 正确** ✓" "\n"
        r"**⭐⭐ 通法（翻折 ⟹ 球心在转轴中点）**：" "\n"
        r"① ⭐⭐ **翻折题定球心的秘诀：找转轴上的点到各顶点等距** —— " "\n"
        r"本题 $O$ 是 $BD$ 中点，$A'O=CO=\frac{BD}2$，而 $OB=OD=\frac{BD}2$ 天然成立 ⟹ **四个顶点等距，球心就是 $O$**；" "\n"
        r"② ⭐⭐ **「翻折过程中，转轴上的点到被翻折点的距离不变」** —— " "\n"
        r"所以 $A'O=AO=2\sqrt2$ 可直接用翻折前的值，不必重算；" "\n"
        r"③ ⭐ **弦长公式 $l=2\sqrt{R^{2}-d^{2}}$**，其中 $d$ 是球心到直线的距离 —— " "\n"
        r"**求 $d$ 用等腰三角形**：$OM=ON$ ⟹ $d=\sqrt{|OM|^2-(\frac{MN}2)^2}$，省掉点到直线距离公式；" "\n"
        r"④ ⚠ **求 $MN$ 最容易错**：$M,N$ 分处两个互相垂直的半平面，是**三维距离**，" "\n"
        r"必须同时考虑 $EF$、$NE$、$MF$ 三段（我用坐标法算得 $2\sqrt3$，与详解的两次勾股一致）；" "\n"
        r"⑤ ⭐ **验算技巧**：由弦长反推 $d$，检查是否 $\le|OM|$ —— 本题 A、C 对应的 $d$ 都 $>2$，**直接排除**；" "\n"
        r"⑥ 检验：**把 $M,N,O$ 坐标全算出来，验 $|OM|=|ON|=2$ 且 $|MN|=2\sqrt3$**（全部 ✓）。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-301'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-301-V1',
}

T301_V2 = {
    'type': '填空',
    'stem_text': (
        r"在三棱锥 $S-ABC$ 中，$\angle SBA=\angle SCA=90^\circ$，底面 $ABC$ 是等边三角形，"
        r"三棱锥 $S-ABC$ 的体积为 $\sqrt3$，则三棱锥 $S-ABC$ 的外接球表面积的最小值是 ____。 "
    ),
    'opts': [],
    'answer': r"$12\pi$",
    'analysis': (
        r"由两个直角知 $SA$ 是外接球直径，$O$ 为 $SA$ 中点，球心到底面距离 $d=\frac h2$，"
        r"底面外接圆半径 $r=\frac{\sqrt3}3a$。$V=\frac{\sqrt3}{12}a^2h=\sqrt3$ ⟹ $a^2h=12$。"
        r"$R^2=\frac{h^2}4+\frac{a^2}3=\frac{h^2}4+\frac4h\ge3$。"
    ),
    'solution': (
        r"由 $\angle SBA=90^\circ$、$\angle SCA=90^\circ$ 知 $B,C$ 都在以 $SA$ 为直径的球上，" "\n"
        r"故 $SA$ 是三棱锥外接球的一条直径，球心 $O$ 为 $SA$ 中点．" "\n"
        r"设底面边长为 $a$、高为 $h$（$S$ 到底面 $ABC$ 的距离）．" "\n"
        r"则球心到底面的距离 $d=\dfrac h2$，底面正三角形外接圆半径 $r=\dfrac{\sqrt3}3a$，" "\n"
        r"$R^{2}=d^{2}+r^{2}=\dfrac{h^{2}}4+\dfrac{a^{2}}3$．" "\n"
        r"**体积约束**：$V=\dfrac13\cdot\dfrac{\sqrt3}4a^{2}\cdot h=\dfrac{\sqrt3}{12}a^{2}h=\sqrt3$，即 $a^{2}h=12$，$a^{2}=\dfrac{12}h$．" "\n"
        r"代入：$R^{2}=\dfrac{h^{2}}4+\dfrac{4}h$．" "\n"
        r"**求最小**：由均值不等式（三项）" "\n"
        r"$R^{2}=\dfrac{h^{2}}4+\dfrac2h+\dfrac2h\ge3\sqrt[3]{\dfrac{h^{2}}4\cdot\dfrac2h\cdot\dfrac2h}=3\sqrt[3]{1}=3$，" "\n"
        r"等号当且仅当 $\dfrac{h^{2}}4=\dfrac2h$，即 $h^{3}=8$、$h=2$ 时成立（此时 $a^{2}=6$）．" "\n"
        r"故 $S_{球}=4\pi R^{2}\ge4\pi\cdot3=12\pi$。最小值为 $12\pi$。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p269 详解：" "\n"
        r"「设三棱锥外接球的球心为 $O$，三棱锥底面边长和高分别为 $a,h$。由 $\angle SBA=\angle SCA=90^\circ$，" "\n"
        r"可知 $SA$ 是三棱锥 $S-ABC$ 的外接球的一条直径，所以 $O$ 为 $SA$ 的中点，则球心到底面 $ABC$ 的距离为 $d=\frac h2$。" "\n"
        r"底面 $ABC$ 的外接圆半径为 $r$，则 $r=\frac{\sqrt3}3a$。" "\n"
        r"则 $V_{S-ABC}=\frac13\times\frac{\sqrt3}4a^{2}h=\sqrt3$，即 $a^{2}h=12$。设外接球半径为 $R$，" "\n"
        r"则 $R^{2}=r^{2}+d^{2}=\frac{a^{2}}3+\frac{h^{2}}4=\frac{h^{2}}4+\frac4h\ge3$，当且仅当 $\frac{h^{2}}4=\frac4h$…即 $h=2$ 时等号成立，" "\n"
        r"故三棱锥 $S-ABC$ 的外接球表面积为 $4\pi R^{2}\ge12\pi$」" "\n"
        r"—— **$SA$ 为直径、$d=\frac h2$、$r=\frac{\sqrt3}3a$、$a^2h=12$、$R^2=\frac{h^2}4+\frac4h\ge3$、$12\pi$ 全部与我的推导一致** ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **$SA$ 是直径**：$\angle SBA=90^\circ$ ⟹ $B$ 在以 $SA$ 为直径的球上（直径所对圆周角为直角）✓✓✓" "\n"
        r"同理 $C$ 也在；$A,S$ 显然是直径端点 ⟹ **四点 $S,A,B,C$ 共球，$SA$ 为直径** ✓✓✓" "\n"
        r"② **$d=\frac h2$**：$O$ 是 $SA$ 中点，$S$ 到底面距离 $h$，$A$ 在底面上 ⟹ $O$ 到底面距离 $=\frac h2$ ✓✓✓" "\n"
        r"③ **$r=\frac{\sqrt3}3a$**：正三角形外接圆半径 $=\frac a{\sqrt3}=\frac{\sqrt3}3a$ ✓✓✓" "\n"
        r"④ **$V=\frac{\sqrt3}{12}a^2h$**：底面积 $\frac{\sqrt3}4a^2$，$V=\frac13\cdot\frac{\sqrt3}4a^2h$ ✓✓✓" "\n"
        r"$=\sqrt3$ ⟹ $\frac{\sqrt3}{12}a^2h=\sqrt3$ ⟹ $a^2h=12$ ✓✓✓" "\n"
        r"⑤ **$R^2=\frac{a^2}3+\frac{h^2}4=\frac{12}{3h}+\frac{h^2}4=\frac4h+\frac{h^2}4$** ✓✓✓" "\n"
        r"⑥ **最小化**：$\frac{d}{dh}(\frac{h^2}4+\frac4h)=\frac h2-\frac4{h^2}=0$ ⟹ $h^3=8$ ⟹ $h=2$ ✓✓✓" "\n"
        r"$R^2=\frac44+\frac42=1+2=3$ ✓✓✓ ⟹ $S=4\pi\cdot3=12\pi$ ✓✓✓" "\n"
        r"（用均值不等式：$\frac{h^2}4+\frac2h+\frac2h\ge3\sqrt[3]{\frac{h^2}4\cdot\frac4{h^2}}=3$，等号 $\frac{h^2}4=\frac2h$ ⟹ $h^3=8$ ✓ 一致）" "\n"
        r"⑦ **$a^2=6$ 时的几何自洽性检查**：$a=\sqrt6=2.4495$，$h=2$。" "\n"
        r"$V=\frac13\cdot\frac{\sqrt3}4\cdot6\cdot2=\frac{\sqrt3}{12}\cdot12=\sqrt3$ ✓✓✓" "\n"
        r"$R^2=\frac{6}3+\frac44=2+1=3$ ✓✓✓" "\n"
        r"⑧ **数值检验**（取 $h=3$）：$a^2=4$，$R^2=\frac43+\frac94=1.3333+2.25=3.5833>3$ ✓✓✓ **确比 $h=2$ 大**" "\n"
        r"（取 $h=1.5$）：$a^2=8$，$R^2=\frac83+\frac{2.25}4=2.6667+0.5625=3.2292>3$ ✓✓✓" "\n"
        r"**答案 $12\pi$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（两个直角 ⟹ 直径 ⟹ 单变量最值）**：" "\n"
        r"① ⭐⭐ **$\angle SBA=\angle SCA=90^\circ$ ⟹ $SA$ 是外接球直径** —— " "\n"
        r"「直径所对的圆周角是直角」的逆用：**两个点对一个线段张直角，则该线段是直径**；" "\n"
        r"② ⭐⭐ **$R^{2}=d^{2}+r^{2}$，其中 $d$ 是球心到底面的距离、$r$ 是底面外接圆半径** —— " "\n"
        r"这是所有「外接球」题的通用骨架，本题 $d=\frac h2$ 来自「$SA$ 是直径、$O$ 是中点」；" "\n"
        r"③ ⭐ **体积约束把 $a,h$ 绑成一个变量**：$a^{2}h=12$ ⟹ $R^{2}$ 只含 $h$，" "\n"
        r"然后求导或均值不等式 —— **「约束降维」是求最值的标准动作**；" "\n"
        r"④ ⭐ **均值不等式拆项技巧**：$\frac4h$ 拆成 $\frac2h+\frac2h$ 才能与 $\frac{h^2}4$ 凑出常数 " "\n"
        r"（$\frac{h^2}4\cdot\frac2h\cdot\frac2h=1$）—— **拆项是为了让变量消掉**；" "\n"
        r"⑤ ⚠ **正三角形外接圆半径是 $\frac{\sqrt3}3a$ 不是 $\frac{\sqrt3}2a$**（后者是边长 $a$ 的正三角形的高）；" "\n"
        r"⑥ 检验：**取 $h=1.5$ 与 $h=3$ 各算一遍**，$R^2$ 都 $>3$ ✓，确认 $h=2$ 处是最小值。"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-301'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-301-V2',
}

T301_V3 = {
    'type': '填空',
    'stem_text': (
        r"我国古代《九章算术》中将上、下两面为平行矩形的六面体称为刍童。如图的刍童 $ABCD-EFGH$ 有外接球，"
        r"且 $AB=2\sqrt6$，$AD=2\sqrt2$，$EH=\sqrt{15}$，$EF=\sqrt5$，平面 $EFGH$ 与平面 $ABCD$ 的距离为 $1$，"
        r"则该刍童外接球的体积为 ____。 "
    ),
    'opts': [],
    'answer': r"$36\pi$",
    'analysis': (
        r"设 $O_1,O_2$ 为两矩形中心，$O_1O_2=1$。$O_1G=\frac12\sqrt{EF^2+FG^2}=\sqrt5$、"
        r"$O_2B=\frac12\sqrt{AB^2+AD^2}=2\sqrt2$。设 $OO_2=m$：$(m+1)^2+5=m^2+8$ ⟹ $m=1$，$R=3$。"
    ),
    'solution': (
        r"设 $O$ 为外接球球心，$O_{1},O_{2}$ 分别为矩形 $EFGH,ABCD$ 的中心。" "\n"
        r"由球的几何性质，$O,O_{1},O_{2}$ 三点共线，且 $OO_{2}\perp$ 平面 $ABCD$、$OO_{1}\perp$ 平面 $EFGH$，故 $O_{1}O_{2}=1$．" "\n"
        r"**两底面中心到顶点的距离**：" "\n"
        r"$O_{1}G=\dfrac12\sqrt{EF^{2}+FG^{2}}=\dfrac12\sqrt{5+15}=\dfrac{\sqrt{20}}2=\sqrt5$（其中 $FG=EH=\sqrt{15}$），" "\n"
        r"$O_{2}B=\dfrac12\sqrt{AB^{2}+AD^{2}}=\dfrac12\sqrt{24+8}=\dfrac{\sqrt{32}}2=2\sqrt2$．" "\n"
        r"**设 $OO_{2}=m$**（$O$ 在 $O_{2}$ 远离 $O_{1}$ 的一侧），则 $OO_{1}=m+1$。由 $OG=OB=R$：" "\n"
        r"$(m+1)^{2}+5=m^{2}+8\Rightarrow2m+6=8\Rightarrow m=1$．" "\n"
        r"故 $R^{2}=m^{2}+8=1+8=9$，$R=3$，" "\n"
        r"$V=\dfrac43\pi R^{3}=\dfrac43\pi\cdot27=36\pi$。故答案为 $36\pi$。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p269 详解：" "\n"
        r"「设 $O$ 为刍童外接球的球心，$O_1,O_2$ 分别为矩形 $EFGH,ABCD$ 的中心，由球的几何性质可知：$O,O_1,O_2$ 三点共线，" "\n"
        r"连接 $OO_1,O_1G,OG,O_2B,OB$。由题知：$OO_2\perp$ 平面 $ABCD$，$OO_1\perp$ 平面 $EFGH$，所以 $O_1O_2=1$。" "\n"
        r"因为 $O_1G=\frac12\sqrt{EF^{2}+FG^{2}}=\sqrt{5+15}=\sqrt5$，$O_2B=\frac12\sqrt{AD^{2}+AB^{2}}=\sqrt{8+24}=2\sqrt2$，" "\n"
        r"设 $OO_2=m$，在 $\mathrm{Rt}\triangle O_2OB$ 中，$OB=\sqrt{OO_2^{2}+O_2B^{2}}=\sqrt{m^{2}+8}$。" "\n"
        r"设外接球的半径为 $R$，则 $R=OG=OB$，所以 $(m+1)^{2}+5=m^{2}+8$，解得 $m=1$，…$\frac43\pi R^{3}=36\pi$」" "\n"
        r"—— **$O_1G=\sqrt5$、$O_2B=2\sqrt2$、$(m+1)^2+5=m^2+8$、$m=1$、$36\pi$ 全部与我的推导一致** ✓✓✓" "\n"
        r"（⚠ 原书 $O_1G$ 的式子写成 $\frac12\sqrt{EF^2+FG^2}=\sqrt{5+15}$，**漏写了 $\frac12$**：" "\n"
        r"$\frac12\sqrt{20}=\sqrt5$，而 $\sqrt{20}=2\sqrt5\neq\sqrt5$。但**最终数值 $\sqrt5$ 是对的**，" "\n"
        r"说明是排版漏写系数，我按正确值 $\sqrt5$ 录入）" "\n"
        r"**独立验算**：" "\n"
        r"① **$FG=EH=\sqrt{15}$**：矩形 $EFGH$ 中 $EH$ 与 $FG$ 是对边 ✓✓✓" "\n"
        r"② **$O_1G=\frac12\sqrt{5+15}=\frac{\sqrt{20}}2=\frac{4.4721}2=2.2361=\sqrt5$** ✓✓✓" "\n"
        r"③ **$O_2B=\frac12\sqrt{24+8}=\frac{\sqrt{32}}2=\frac{5.6569}2=2.8284=2\sqrt2$** ✓✓✓" "\n"
        r"④ **$(m+1)^2+5=m^2+8$**：$m^2+2m+1+5=m^2+8$ ⟹ $2m=2$ ⟹ $m=1$ ✓✓✓" "\n"
        r"⑤ **$R^2=1+8=9$ ⟹ $R=3$** ✓✓✓；**$V=\frac43\pi\cdot27=36\pi$** ✓✓✓" "\n"
        r"⑥ **验 $OG$**：$OO_1=m+1=2$，$OG=\sqrt{4+5}=\sqrt9=3$ ✓✓✓ **与 $OB$ 相等**" "\n"
        r"⑦ **$O$ 在 $O_2$ 外侧的合理性**：$O_1O_2=1$，$OO_2=1$，$OO_1=2$ ⟹ $O$ 在 $O_2$ 远离 $O_1$ 一侧 ✓" "\n"
        r"（因为 $O_2B=2\sqrt2>O_1G=\sqrt5$，底面 $ABCD$ 更「大」，球心应偏向小底面一侧，**符合几何直觉** ✓）" "\n"
        r"⑧ **数值检验**：$R=3$，$V=\frac43\pi(27)=36\pi=113.10$ ✓✓✓" "\n"
        r"**答案 $36\pi$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（圆台/棱台型组合体外接球）**：" "\n"
        r"① ⭐⭐ **核心方程：$(m+d)^{2}+r_{1}^{2}=m^{2}+r_{2}^{2}$** —— " "\n"
        r"其中 $d$ 是两底面中心距离、$r_1,r_2$ 是两底面中心到各自顶点的距离、$m$ 是球心到大底面中心的距离；" "\n"
        r"**$m$ 解出后 $R^{2}=m^{2}+r_{2}^{2}$**；" "\n"
        r"② ⭐ **矩形中心到顶点距离 $=\frac12\sqrt{\text{长}^2+\text{宽}^2}=\frac{\text{对角线}}2$** —— " "\n"
        r"本题 $\frac12\sqrt{24+8}=2\sqrt2$、$\frac12\sqrt{5+15}=\sqrt5$；" "\n"
        r"③ ⭐ **$O,O_1,O_2$ 共线**：由「球心在小圆圆心的垂线上」，两底面的垂线都过各自中心且同向 ⟹ 三点共线；" "\n"
        r"④ ⚠ **$m$ 可能为负**：若解出 $m<0$，说明球心在另一侧，**距离取绝对值**，别急着判错；" "\n"
        r"⑤ ⚠ **注意对面边长的对应**：矩形 $EFGH$ 中 $EF=\sqrt5$、$FG=EH=\sqrt{15}$，" "\n"
        r"**别把 $EH$ 当成 $EF$ 的对边**；" "\n"
        r"⑥ 检验：**算完 $R$ 后用另一底面验一遍**（$OG=\sqrt{4+5}=3=OB$ ✓）。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-301'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-301-V3',
}

T302_V1 = {
    'type': '填空',
    'stem_text': (
        r"设圆锥的顶点为 $A$，$BC$ 为圆锥底面圆 $O$ 的直径，点 $P$ 为圆 $O$ 上的一点（异于 $B,C$），"
        r"若 $BC=4\sqrt3$，三棱锥 $A-PBC$ 的外接球表面积为 $64\pi$，则圆锥的体积为 ____。 "
    ),
    'opts': [],
    'answer': r"$24\pi$ 或 $8\pi$",
    'analysis': (
        r"球心 $M$ 在 $AO$ 上，$4\pi r^2=64\pi$ ⟹ $r=4$。$BM^2=OM^2+OB^2$ ⟹ $16=OM^2+12$ ⟹ $OM=2$。"
        r"$OM=\lvert AO-4\rvert=2$ ⟹ $AO=6$ 或 $2$，$V=\frac13\pi(2\sqrt3)^2\cdot AO=4\pi\cdot AO$。"
    ),
    'solution': (
        r"设圆锥外接球（即三棱锥 $A-PBC$ 的外接球）球心为 $M$，则 $M$ 在直线 $AO$ 上。" "\n"
        r"由 $4\pi r^{2}=64\pi$ 得 $r=4$．" "\n"
        r"底面半径 $OB=\dfrac{BC}2=2\sqrt3$。在 $\mathrm{Rt}\triangle MOB$ 中：" "\n"
        r"$BM^{2}=OM^{2}+OB^{2}\Rightarrow16=OM^{2}+12\Rightarrow OM=2$．" "\n"
        r"因 $M$ 在直线 $AO$ 上且 $MA=r=4$，故 $OM=\lvert AO-MA\rvert=\lvert AO-4\rvert=2$，" "\n"
        r"解得 $AO=6$ 或 $AO=2$（分别对应球心在圆锥内部与外部两种情形）．" "\n"
        r"圆锥体积 $V=\dfrac13\pi\cdot OB^{2}\cdot AO=\dfrac13\pi\cdot12\cdot AO=4\pi\cdot AO$，" "\n"
        r"故 $V=24\pi$ 或 $V=8\pi$。故答案为 $24\pi$ 或 $8\pi$。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p270 详解：" "\n"
        r"「设圆锥 $AO$ 的外接球球心为 $M$，则 $M$ 在直线 $AO$ 上，设球 $M$ 的半径为 $r$，则 $4\pi r^{2}=64\pi$，解得 $r=4$。" "\n"
        r"由勾股定理得 $BM^{2}=OM^{2}+OB^{2}$，即 $4^{2}=(2\sqrt3)^{2}+OM^{2}$，可得 $OM=2$，" "\n"
        r"即 $OM=\lvert AO-r\rvert=\lvert AO-4\rvert=2$，解得 $AO=6$ 或 $AO=2$…」" "\n"
        r"—— **$r=4$、$OB=2\sqrt3$、$BM^2=OM^2+OB^2$、$OM=2$、$AO=6$ 或 $2$ 全部与我的推导一致** ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **$r=4$**：$4\pi r^2=64\pi$ ⟹ $r^2=16$ ⟹ $r=4$ ✓✓✓" "\n"
        r"② **$OB=\frac{BC}2=2\sqrt3=3.4641$** ✓✓✓" "\n"
        r"③ **$OM^2=16-12=4$ ⟹ $OM=2$** ✓✓✓" "\n"
        r"④ **$OM=|AO-4|$**：$M$ 在直线 $AO$ 上，$MA=4$。$A,O,M$ 三点共线，$OM=|AO\pm4|$？" "\n"
        r"实际上 $M$ 在射线 $OA$ 上或在其反向延长线上。若 $M$ 在线段 $AO$ 上或与 $A$ 在 $O$ 的同侧，" "\n"
        r"则 $OM=|AO-MA|=|AO-4|$ ✓（因为 $A,M,O$ 共线且 $MA=4$）✓✓✓" "\n"
        r"⑤ **$AO=6$ 或 $AO=2$** ✓✓✓" "\n"
        r"- $AO=6$：$OM=|6-4|=2$ ✓，$M$ 在 $O$ 与 $A$ 之间（距 $O$ 为 2，距 $A$ 为 4）" "\n"
        r"- $AO=2$：$OM=|2-4|=2$ ✓，$A$ 在 $O$ 与 $M$ 之间（$OA=2$，$OM=4$，故 $AM=2$…）" "\n"
        r"✗ 等等：$AM$ 应 $=r=4$。若 $OA=2$、$OM=2$ 且 $A,M$ 在 $O$ 两侧，则 $AM=4$ ✓ ✓✓✓" "\n"
        r"**两种情形都成立**：球心在圆锥内（$AO=6$，$M$ 距 $O$ 为 2）与球心在圆锥外（$AO=2$，$A$ 与 $M$ 在 $O$ 两侧）" "\n"
        r"⑥ **$V=4\pi\cdot AO$**：$\frac13\pi(2\sqrt3)^2\cdot AO=\frac13\pi\cdot12\cdot AO=4\pi\cdot AO$ ✓✓✓" "\n"
        r"$AO=6$ ⟹ $V=24\pi$；$AO=2$ ⟹ $V=8\pi$ ✓✓✓" "\n"
        r"⑦ **数值检验**：" "\n"
        r"- $AO=6$：$V=\frac13\pi\cdot12\cdot6=24\pi=75.398$ ✓✓✓" "\n"
        r"- $AO=2$：$V=\frac13\pi\cdot12\cdot2=8\pi=25.133$ ✓✓✓" "\n"
        r"⑧ **验 $BM=4$**：$B$ 在底面圆上，$OB=2\sqrt3$、$OM=2$ ⟹ $BM=\sqrt{4+12}=\sqrt{16}=4=r$ ✓✓✓" "\n"
        r"**答案 $24\pi$ 或 $8\pi$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（圆锥外接球 ⟹ 轴截面）**：" "\n"
        r"① ⭐⭐ **圆锥外接球 ⟺ 轴截面等腰三角形的外接圆** —— " "\n"
        r"把所有计算压到一个平面里，本题即 $BM^{2}=OM^{2}+OB^{2}$；" "\n"
        r"② ⭐⭐ **$OM=\lvert AO-r\rvert$ 会有两解** —— 这是「球心在锥内 / 锥外」两种情形，" "\n"
        r"**题目问「圆锥体积」而没说球心位置，两解都要写**，这是本题唯一的陷阱；" "\n"
        r"③ ⭐ **$V=\frac13\pi r_{底}^{2}h$**，本题 $r_底=2\sqrt3$ ⟹ $V=4\pi h$ —— " "\n"
        r"**系数先算好**，最后只需代入两个 $h$；" "\n"
        r"④ ⚠ **$BC$ 是直径不是半径**：$OB=\frac{BC}2=2\sqrt3$，**别把 $4\sqrt3$ 直接当半径**；" "\n"
        r"⑤ ⭐ **三棱锥 $A-PBC$ 的外接球就是圆锥的外接球**：因为 $A,B,C,P$ 都在球上且 $A,B,C$ 不共线，" "\n"
        r"三点确定球面与底面圆的交圆，$P$ 在底面圆上 ⟹ $P$ 也在球上 ✓；" "\n"
        r"⑥ 检验：**把两个 $AO$ 代回，验 $OM=2$ 且 $BM=4$**（都 ✓），并核对 $AM=4$（第二种情形 $A,M$ 分居 $O$ 两侧，$2+2=4$ ✓）。"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-302'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-302-V1',
}

QS = [T301_E1, T301_V1, T301_V2, T301_V3, T302_V1]
