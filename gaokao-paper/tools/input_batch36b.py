# -*- coding: utf-8 -*-
r"""第36批（下）：平面向量与三角形四心 · 垂心（3题）

来源：2024高中数学热点题型归纳完整解析版.pdf p174（PDF 页 173）

## 选题

`pick_batch.py --n 6 --topic M-T-210` → p174 一页 4 题。

## 跳过 1 题

**M-T-210-V2** 与 **V1 数学本质相同**（都是
$\vec{AP}=t\!\left(\frac{\vec{AB}}{|AB|\cos B}+\frac{\vec{AC}}{|AC|\cos C}\right)$ ⟹ 垂心），
只是选项顺序不同（V1 答 C、V2 答 D，都是「垂心」）。已用 `--skip` 标记。

## ★ 通法：判断轨迹过哪个「心」

把 $\vec{AP}$ 与对边 $\vec{BC}$ 点乘，**若结果为 0 则 $AP\perp BC$**，
即 $P$ 在 $A$ 的高线上 ⟹ 轨迹过**垂心**。

$$\vec{AB}\cdot\vec{BC}=|AB||BC|\cos(\pi-B)=-|AB||BC|\cos B$$
$$\vec{AC}\cdot\vec{BC}=|AC||BC|\cos C$$

两式分别除以 $|AB|\cos B$、$|AC|\cos C$ 后正好得 $-|BC|+|BC|=0$ ✓

## 三题验算

| 题 | 结果 | 答案 |
|---|---|---|
| E1 | $\sqrt3\cos B$ 项恰好抵消 → $\sin B=2\sqrt3 m\sin B$ → $m=\frac{\sqrt3}6$ | **D** |
| V1 | $\vec{AP}\cdot\vec{BC}=0$ → 过垂心 | **C** |
| V3 | $AH=\sqrt3$ → $R=1$ → $BC=1$；$\sqrt3BH+CH=2\sin(\alpha+30^\circ)\in(1,\sqrt3)$ | $(1,\sqrt3)$ |

## ⚠ 两处原书根号丢失（已还原并验证）

- **E1**：$\frac{\sqrt3}{6}$ 被提取成 `36`
- **V3**：题干 $AH=\sqrt3$ 被写成 `AH = 3`；详解「$3\sin\alpha$」实为 $\sqrt3\sin\alpha$；
  答案 `(1, 3)` 实为 $(1,\sqrt3)$。
  **反证**：若 $AH=3$ 则 $R=\sqrt3$、$BC=\sqrt3$，结果会是 $(\sqrt3,3)$ 而非 $(1,\sqrt3)$。
"""

T210_E1 = {
    'type': '选择',
    'stem_text': (
        r"若 $O$ 是 $\triangle ABC$ 垂心，$\angle A=\dfrac\pi6$，且 "
        r"$\sin B\cos C\,\vec{AB}+\sin C\cos B\,\vec{AC}=2m\sin B\sin C\,\vec{AO}$，"
        r"则 $m=$（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac12$"), ('B', r"$\dfrac{\sqrt3}2$"),
        ('C', r"$\dfrac{\sqrt3}3$"), ('D', r"$\dfrac{\sqrt3}6$"),
    ],
    'answer': 'D',
    'analysis': (
        r"两边除以 $\sin B\sin C$ 后用 $\vec{AO}=\vec{AD}+\vec{DO}$（$D$ 为 $C$ 到 $AB$ 的垂足），"
        r"同乘 $\vec{AB}$ 得数量积等式，再用正弦定理化为关于 $B$ 的三角式 —— "
        r"$\sqrt3\cos B$ 项恰好抵消。"
    ),
    'solution': (
        r"**第一步：两边除以 $\sin B\sin C$**" "\n"
        r"$\dfrac{\cos C}{\sin C}\vec{AB}+\dfrac{\cos B}{\sin B}\vec{AC}=2m\,\vec{AO}$．" "\n"
        r"**第二步：分解 $\vec{AO}$**" "\n"
        r"连接 $CO$ 延长交 $AB$ 于 $D$．因 $O$ 是垂心，$CD\perp AB$，"
        r"且 $\vec{AO}=\vec{AD}+\vec{DO}$．" "\n"
        r"**第三步：两边同乘 $\vec{AB}$（点乘）**" "\n"
        r"$\dfrac{\cos C}{\sin C}\vec{AB}\cdot\vec{AB}"
        r"+\dfrac{\cos B}{\sin B}\vec{AC}\cdot\vec{AB}=2m(\vec{AD}+\vec{DO})\cdot\vec{AB}$．" "\n"
        r"· $\vec{AB}\cdot\vec{AB}=c^{2}$；$\vec{AC}\cdot\vec{AB}=bc\cos A$；" "\n"
        r"· 因 $DO\perp AB$，$\vec{DO}\cdot\vec{AB}=0$，故 "
        r"$(\vec{AD}+\vec{DO})\cdot\vec{AB}=|\vec{AD}|\cdot|\vec{AB}|=b\cos A\cdot c$．" "\n"
        r"得 $\dfrac{\cos C}{\sin C}c^{2}+\dfrac{\cos B}{\sin B}bc\cos A=2m\,bc\cos A$．" "\n"
        r"**第四步：用正弦定理统一**" "\n"
        r"代入 $c=2R\sin C$、$b=2R\sin B$、$\cos A=\dfrac{\sqrt3}2$：" "\n"
        r"$\dfrac{\cos C}{\sin C}\cdot4R^{2}\sin^{2}C"
        r"+\dfrac{\cos B}{\sin B}\cdot4R^{2}\sin B\sin C\cdot\dfrac{\sqrt3}2$" "\n"
        r"$=2m\cdot4R^{2}\sin B\sin C\cdot\dfrac{\sqrt3}2$" "\n"
        r"$\Rightarrow4R^{2}\sin C\cos C+2\sqrt3R^{2}\cos B\sin C$" "\n"
        r"$=4\sqrt3\,mR^{2}\sin B\sin C$．" "\n"
        r"除以 $2R^{2}\sin C$：$2\cos C+\sqrt3\cos B=2\sqrt3\,m\sin B$．" "\n"
        r"**第五步：代入 $C=\dfrac{5\pi}6-B$**" "\n"
        r"$\cos C=\cos\!\left(\dfrac{5\pi}6-B\right)$" "\n"
        r"$=-\dfrac{\sqrt3}2\cos B+\dfrac12\sin B$，" "\n"
        r"故 $2\cos C=-\sqrt3\cos B+\sin B$，" "\n"
        r"$2\cos C+\sqrt3\cos B=\sin B$（**余弦项恰好抵消**）．" "\n"
        r"由 $\sin B=2\sqrt3\,m\sin B$ 且 $\sin B\neq0$：" "\n"
        r"$m=\dfrac1{2\sqrt3}=\dfrac{\sqrt3}6$．选 D．"
    ),
    'review': (
        r"★ 由详解「在 $\triangle ABC$ 中，$\sin B\sin C\neq0$，由 "
        r"$\sin B\cos C\vec{AB}+\sin C\cos B\vec{AC}=2m\sin B\sin C\vec{AO}$ "
        r"得 $\frac{\cos C}{\sin C}\vec{AB}+\frac{\cos B}{\sin B}\vec{AC}=2m\vec{AO}$，"
        r"连接 $CO$ 并延长交 $AB$ 于 $D$，因为 $O$ 是 $\triangle ABC$ 的垂心，"
        r"所以 $CD\perp AB$，$\vec{AO}=\vec{AD}+\vec{DO}$…同乘 $\vec{AB}$ 得，"
        r"$\frac{\cos C}{\sin C}c^{2}+\frac{\cos B}{\sin B}bc\cos A=2m\,b\cos A\cdot c$，"
        r"因为 $A=\frac\pi6$…又 $\sin C\neq0$，所以有 $\cos C+\cos B=3m\sin B$，"
        r"而 $C=\pi-A-B=\frac{5\pi}6-B$，所以 $\cos C=\cos(\frac{5\pi}6-B)$"
        r"=-\frac{\sqrt3}2\cos B+\frac12\sin B$，" "\n"
        r"所以得到 $\frac12\sin B=3m\sin B$，而 $\sin B\neq0$，所以得到 $m=\frac{\sqrt3}6$」还原。" "\n"
        r"**⚠ 详解中间式有笔误**（已用我的推导核对）："
        r"原文的「$\cos C+\cos B=3m\sin B$」与「$\frac12\sin B=3m\sin B$」应为"
        r"$2\cos C+\sqrt3\cos B=2\sqrt3 m\sin B$ 与 $\sin B=2\sqrt3 m\sin B$。" "\n"
        r"（原文两处的 `3` 实为 $\sqrt3$、漏了系数 $2$；"
        r"但最终 $m=\frac{\sqrt3}6$ 与我的推导**一致** ✓）" "\n"
        r"**独立验算**（数值反查，取 $B=40^\circ$）：" "\n"
        r"$A=30^\circ$、$C=\frac{5\pi}6-40^\circ=150^\circ-40^\circ=110^\circ$" "\n"
        r"取 $R=1$：$b=2\sin40^\circ=1.2856$、$c=2\sin110^\circ=1.8794$、$a=2\sin30^\circ=1$" "\n"
        r"左端 $=\sin40^\circ\cos110^\circ\cdot c^2+\sin110^\circ\cos40^\circ\cdot bc\cos30^\circ$" "\n"
        r"$=0.6428\times(-0.3420)\times3.5321+0.9397\times0.7660\times1.2856\times1.8794\times0.8660$" "\n"
        r"$=-0.7766+1.5089=0.7323$" "\n"
        r"右端 $=2m\sin40^\circ\sin110^\circ\cdot b\cos A\cdot c$" "\n"
        r"$=2m\times0.6428\times0.9397\times1.2856\times0.8660\times1.8794=2.3909m$" "\n"
        r"$\frac{0.7323}{2.3909}=0.3063$…（应为 $m$ 与其他因子的比，此处直接代 $m=\frac{\sqrt3}6=0.2887$）" "\n"
        r"**改用 $m$ 反代**：$2\times0.2887\times0.6428\times0.9397\times1.2856\times0.8660\times1.8794$" "\n"
        r"$=0.5774\times0.6428\times0.9397\times1.2856\times0.8660\times1.8794$" "\n"
        r"$=0.3711\times0.9397=0.3487$；$\times1.2856=0.4483$；$\times0.8660=0.3882$；$\times1.8794=0.7296$" "\n"
        r"与左端 $0.7323$ **吻合**（差 $0.4\%$，来自四舍五入）✓" "\n"
        r"**答案 D（$\frac{\sqrt3}6\approx0.2887$）正确** ✓" "\n"
        r"**⭐ 本题精华**：代入 $C=\frac{5\pi}6-B$ 后 $\sqrt3\cos B$ 项**恰好抵消**，"
        r"这是命题人设计好的 —— 否则 $m$ 会依赖 $B$，就不是定值了。"
    ),
    'difficulty': 0.95,
    'topics': ['M-T-210'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-210-E1',
}

T210_V1 = {
    'type': '选择',
    'stem_text': (
        r"点 $P$ 为 $\triangle ABC$ 所在平面内的动点，满足 "
        r"$\vec{AP}=t\!\left(\dfrac{\vec{AB}}{|AB|\cos B}+\dfrac{\vec{AC}}{|AC|\cos C}\right)$，"
        r"$t\in[0,+\infty)$，则点 $P$ 的轨迹通过 $\triangle ABC$ 的（　　）"
    ),
    'opts': [
        ('A', r"外心"), ('B', r"重心"),
        ('C', r"垂心"), ('D', r"内心"),
    ],
    'answer': 'C',
    'analysis': (
        r"把 $\vec{AP}$ 与对边 $\vec{BC}$ 点乘，验证结果为 $0$，"
        r"即 $AP\perp BC$，故 $P$ 在 $A$ 的高线上，轨迹过垂心。"
    ),
    'solution': (
        r"**核心：验证 $\vec{AP}\perp\vec{BC}$**" "\n"
        r"计算 $\vec{AP}\cdot\vec{BC}$：" "\n"
        r"$\vec{AP}\cdot\vec{BC}=t\!\left(\dfrac{\vec{AB}\cdot\vec{BC}}{|AB|\cos B}"
        r"+\dfrac{\vec{AC}\cdot\vec{BC}}{|AC|\cos C}\right)$．" "\n"
        r"**第一项**：$\vec{AB}$ 与 $\vec{BC}$ 的夹角为 $\pi-B$（注意方向），" "\n"
        r"$\vec{AB}\cdot\vec{BC}=|AB|\cdot|BC|\cos(\pi-B)=-|AB||BC|\cos B$，" "\n"
        r"故 $\dfrac{\vec{AB}\cdot\vec{BC}}{|AB|\cos B}=-|BC|$．" "\n"
        r"**第二项**：$\vec{AC}$ 与 $\vec{BC}$ 的夹角为 $C$，" "\n"
        r"$\vec{AC}\cdot\vec{BC}=|AC|\cdot|BC|\cos C$，" "\n"
        r"故 $\dfrac{\vec{AC}\cdot\vec{BC}}{|AC|\cos C}=|BC|$．" "\n"
        r"**相加**：$\vec{AP}\cdot\vec{BC}=t(-|BC|+|BC|)=0$．" "\n"
        r"故 $AP\perp BC$，即 $P$ 恒在过 $A$ 且垂直 $BC$ 的直线（**$A$ 边上的高**）上．" "\n"
        r"由 $t\in[0,+\infty)$，$P$ 的轨迹是这条高线（以 $A$ 为端点的射线方向），"
        r"而三条高交于**垂心**，故轨迹过垂心．选 C．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**原书无详解**，上述证明为我独立完成）。" "\n"
        r"**独立验算**（数值验证 $\vec{AP}\perp\vec{BC}$）：" "\n"
        r"取 $A(0,0)$、$B(4,0)$、$C(1,3)$。" "\n"
        r"$|AB|=4$、$|AC|=\sqrt{10}=3.1623$、$|BC|=\sqrt{9+9}=4.2426$" "\n"
        r"$\cos B=\frac{\vec{BA}\cdot\vec{BC}}{|BA||BC|}=\frac{(-4,0)\cdot(-3,3)}{4\times4.2426}$"
        r"=\frac{12}{16.9706}=0.7071$" "\n"
        r"$\cos C=\frac{\vec{CA}\cdot\vec{CB}}{|CA||CB|}=\frac{(-1,-3)\cdot(3,-3)}{3.1623\times4.2426}$"
        r"=\frac{-3+9}{13.4164}=0.4472$" "\n"
        r"括号内向量 $=\frac{(4,0)}{4\times0.7071}+\frac{(1,3)}{3.1623\times0.4472}$"
        r"=(1.4142,0)+(0.7071,2.1213)=(2.1213,2.1213)$" "\n"
        r"$\vec{AC}$ 方向的高：过 $A$ 垂直 $BC$。$\vec{BC}=(-3,3)$，"
        r"垂线方向 $(3,3)$ 或 $(1,1)$ —— " "\n"
        r"括号内 $(2.1213,2.1213)=2.1213(1,1)$ ✓ **正是 $BC$ 的垂线方向**" "\n"
        r"$\vec{AP}\cdot\vec{BC}=2.1213(1,1)\cdot(-3,3)=2.1213\times0=0$ ✓✓ **完全垂直**" "\n"
        r"**答案 C（垂心）正确** ✓" "\n"
        r"**⭐ 通法总结**：判断轨迹过哪个「心」，就与**对边**点乘：" "\n"
        r"· 结果为 $0$ → 垂直对边 → **垂心**" "\n"
        r"· 若 $\vec{AP}\cdot\vec{BC}$ 与边长有关且满足中垂线性质 → **外心**" "\n"
        r"· 若为 $\frac{\vec{AB}}{|AB|}+\frac{\vec{AC}}{|AC|}$（角平分方向） → **内心**" "\n"
        r"· 若为 $\vec{AB}+\vec{AC}$（中线方向） → **重心**" "\n"
        r"（本题分母多了 $\cos B$、$\cos C$，正是为了凑出「$-|BC|+|BC|=0$」）"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-210'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-210-V1',
}

T210_V3 = {
    'type': '填空',
    'stem_text': (
        r"$\triangle ABC$ 的垂心 $H$ 在其内部，$\angle A=30^\circ$，$AH=\sqrt3$，"
        r"则 $\sqrt3\,BH+CH$ 的取值范围是 ____ ．"
    ),
    'opts': [],
    'answer': r"$\left(1,\ \sqrt3\right)$",
    'analysis': (
        r"由 $AH=2R\cos A$ 定出外接圆半径 $R=1$，进而 $BC=1$；"
        r"在 $\triangle BHC$ 中 $\angle BHC=150^\circ$，用正弦定理把 $BH,CH$ 表成关于 "
        r"$\angle BCH=\alpha$ 的式子，再化简求值域。"
    ),
    'solution': (
        r"**第一步：求 $BC$**" "\n"
        r"垂心性质：$AH=2R\cos A$，故 $\sqrt3=2R\cos30^\circ=2R\cdot\dfrac{\sqrt3}2=R\sqrt3$，"
        r"得 $R=1$．" "\n"
        r"$BC=a=2R\sin A=2\times1\times\dfrac12=1$．" "\n"
        r"**第二步：$\triangle BHC$ 中的角度关系**" "\n"
        r"由垂心性质 $\angle BHC=180^\circ-\angle A=150^\circ$．"
        r"设 $\angle BCH=\alpha$，则 $\angle HBC=180^\circ-150^\circ-\alpha=30^\circ-\alpha$，" "\n"
        r"由 $H$ 在内部知 $0<\alpha<30^\circ$．" "\n"
        r"**第三步：正弦定理**" "\n"
        r"$\dfrac{BC}{\sin\angle BHC}=\dfrac{1}{\sin150^\circ}=\dfrac1{1/2}=2$，" "\n"
        r"故 $BH=2\sin(\angle BCH)=2\sin\alpha$、"
        r"$CH=2\sin(\angle HBC)=2\sin(30^\circ-\alpha)$．" "\n"
        r"**第四步：化简**" "\n"
        r"$\sqrt3\,BH+CH=2\sqrt3\sin\alpha+2\sin(30^\circ-\alpha)$" "\n"
        r"$=2\sqrt3\sin\alpha+2\!\left(\dfrac12\cos\alpha-\dfrac{\sqrt3}2\sin\alpha\right)$" "\n"
        r"$=2\sqrt3\sin\alpha+\cos\alpha-\sqrt3\sin\alpha=\sqrt3\sin\alpha+\cos\alpha$" "\n"
        r"$=2\sin(\alpha+30^\circ)$．" "\n"
        r"**第五步：求值域**" "\n"
        r"$\alpha\in(0,30^\circ)\Rightarrow\alpha+30^\circ\in(30^\circ,60^\circ)$，" "\n"
        r"$\sin(\alpha+30^\circ)\in\left(\dfrac12,\dfrac{\sqrt3}2\right)$（两端均取不到），" "\n"
        r"故 $\sqrt3\,BH+CH\in(1,\sqrt3)$．"
    ),
    'review': (
        r"★ 由详解「设 $AD$、$BE$ 是高，$H$ 就是 $AD$、$BE$ 交点，"
        r"那么 $AD\perp BC$，$\angle DAC+\angle ACD=90^\circ$，$BE\perp AC$，"
        r"$\angle CBE+\angle DCA=90^\circ$，所以 $\angle DAC=\angle CBE$，"
        r"所以 Rt$\triangle AHE\sim$ Rt$\triangle BCE$，所以 $\frac{AH}{BC}=\frac{AE}{BE}$，"
        r"$AH=BC\times\frac{AE}{BE}=BC\times\cot\angle A=BC\times\cot30^\circ=\sqrt3$，"
        r"∴$BC=1$。在 $\triangle BHC$ 中，$\angle BHC=150^\circ$，$BC=1$，"
        r"设 $\angle BCH=\alpha$，由正弦定理可得 "
        r"$\frac{BC}{\sin\angle BHC}=\frac{BH}{\sin\angle BCH}=\frac{CH}{\sin\angle HBC}=2$。"
        r"∴$\sqrt3 BH+CH=\sqrt3\times2\sin\angle BCH+2\sin(\frac\pi6-\angle BCH)$"
        r"$=\sqrt3\sin\alpha+\cos\alpha=2\sin(\alpha+\frac\pi6)$，"
        r"∵$\alpha\in(0,\frac\pi6)$，∴$\sin(\alpha+\frac\pi6)\in(\frac12,\frac{\sqrt3}2)$，"
        r"∴$2\sin(\alpha+\frac\pi6)\in(1,\sqrt3)$」还原。" "\n"
        r"**⚠⚠ 原书三处根号丢失（已还原并反证）**：" "\n"
        r"① 题干 `AH = 3` 实为 **$AH=\sqrt3$**" "\n"
        r"② 详解「$=3\sin\alpha+\cos\alpha$」实为 **$\sqrt3\sin\alpha+\cos\alpha$**" "\n"
        r"③ 答案 `(1, 3)` 实为 **$(1,\sqrt3)$**" "\n"
        r"**反证（关键）**：若按字面 $AH=3$，则由 $AH=2R\cos A$ 得 "
        r"$3=R\sqrt3$ → $R=\sqrt3$ → $BC=2R\sin30^\circ=\sqrt3$ 而非 $1$；" "\n"
        r"进而 $\frac{BC}{\sin150^\circ}=2\sqrt3$，$BH=2\sqrt3\sin\alpha$，"
        r"$\sqrt3BH+CH=3\sin\alpha+\sqrt3\cos\alpha=2\sqrt3\sin(\alpha+30^\circ)\in(\sqrt3,3)$ —— "
        r"**与答案 $(1,\sqrt3)$ 矛盾**。" "\n"
        r"取 $AH=\sqrt3$ 则 $R=1$、$BC=1$，结果 $(1,\sqrt3)$ ✓ **与答案完全吻合**。" "\n"
        r"**独立验算**：" "\n"
        r"① $AH=2R\cos A$：$\sqrt3=2R\cdot\frac{\sqrt3}2$ → $R=1$ ✓；$BC=2\cdot1\cdot\frac12=1$ ✓" "\n"
        r"② $\angle BHC=180^\circ-30^\circ=150^\circ$ ✓" "\n"
        r"③ 端点：$\alpha\to0$ 时 $2\sin30^\circ=1$（取不到，因 $\alpha>0$）✓；"
        r"$\alpha\to30^\circ$ 时 $2\sin60^\circ=\sqrt3$（取不到，因 $\angle HBC>0$）✓" "\n"
        r"④ 中点抽查：$\alpha=15^\circ$ → $2\sin45^\circ=1.4142\in(1,1.732)$ ✓" "\n"
        r"**答案 $(1,\sqrt3)$ 正确** ✓"
    ),
    'difficulty': 0.93,
    'topics': ['M-T-210'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-210-V3',
}

QS = [T210_E1, T210_V1, T210_V3]
