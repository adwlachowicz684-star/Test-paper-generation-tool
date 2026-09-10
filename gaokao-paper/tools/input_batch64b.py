# -*- coding: utf-8 -*-
r"""第64批b：三种角度比大小 / 翻折 / 正四面体 / 球（6 题）

来源：2024高中数学热点题型归纳完整解析版.pdf
p278 M-T-308-V1/V2；p280 M-T-310-E1；p281 M-T-310-V1/V2；p282 M-T-311-V1

## ★★ 本批全部 6 题我都独立建系推导，与原书答案逐一吻合

其中 M-T-310-V1、M-T-310-V2 两题原书详解破碎（满是 ⟨?⟩），
**由我完整重建坐标体系并逐项验算**。

## 六题验算

| 题 | 关键 | 答案 |
|---|---|---|
| M-T-308-V1 | 最小角定理 $\gamma\le\alpha$；等体积 + $S_{PAC}\le S_{ABC}$ 得 $\gamma\le\beta$ | A |
| M-T-308-V2 | 设 $D=(u,v\cos\theta,v\sin\theta)$，$\sin\theta_1=\frac{v\sin\theta}{\lvert DA\rvert}\le\sin\theta$ | A |
| M-T-310-E1 | $AB^2=\frac32x^2-\frac32x+1$ ⟹ $\cos\angle ADB=-\frac14$ 恒定；$\sin\theta$ 随 $x\searrow$ 减小 | C |
| M-T-310-V1 | 建系 $\lambda=-\frac37\in[-1,1]$ 使两平面法向量点积为零 | C |
| M-T-310-V2 | 正四面体棱长 2，逐项点积：①$\frac23$ ②$0$ ③$\frac{\sqrt2}2$ ④$\frac{\sqrt3}6\ne\frac12$ | ①②③ |
| M-T-311-V1 | $OD=\sqrt3$、$CD=1$、$OC=2$ ⟹ $OD\perp$ 底面，$d_P=2\cdot OD$ | D $2\sqrt3$ |
"""

T308_V1 = {
    'type': '选择',
    'stem_text': (
        r"如图，在三棱锥 $P-ABC$ 中，$AB\perp AC$，$AB=AP$，$D$ 是棱 $BC$ 上一点（不含端点）且 $PD=BD$，"
        r"记 $\angle DAB$ 为 $\alpha$，直线 $AB$ 与平面 $PAC$ 所成角为 $\beta$，"
        r"直线 $PA$ 与平面 $ABC$ 所成角为 $\gamma$，则（　　）"
    ),
    'opts': [
        ('A', r"$\gamma\le\beta,\ \gamma\le\alpha$"),
        ('B', r"$\beta\le\alpha,\ \beta\le\gamma$"),
        ('C', r"$\beta\le\alpha,\ \gamma\le\alpha$"),
        ('D', r"$\alpha\le\beta,\ \gamma\le\beta$"),
    ],
    'answer': 'A',
    'analysis': (
        r"由 $AB=AP$、$PD=BD$、$AD$ 公共得 $\triangle ABD\cong\triangle APD$ ⟹ $\angle DAP=\angle DAB=\alpha$；"
        r"由最小角定理 $\gamma\le\alpha$。再由等体积 $S_{ABC}\cdot PA\sin\gamma=S_{PAC}\cdot AB\sin\beta$，"
        r"结合 $PA=AB$ 与 $S_{PAC}\le S_{ABC}$ 得 $\sin\gamma\le\sin\beta$，即 $\gamma\le\beta$。"
    ),
    'solution': (
        r"**第一步：证 $\gamma\le\alpha$**" "\n"
        r"在 $\triangle ABD$ 与 $\triangle APD$ 中：$AB=AP$、$BD=PD$、$AD$ 公共，" "\n"
        r"故 $\triangle ABD\cong\triangle APD$（SSS），于是 $\angle DAP=\angle DAB=\alpha$．" "\n"
        r"$\gamma$ 是 $PA$ 与平面 $ABC$ 所成的角，$\alpha$ 是 $PA$ 与平面 $ABC$ 内直线 $AD$ 所成的角，" "\n"
        r"由**最小角定理**（线面角不大于斜线与平面内任一直线的夹角）得 $\gamma\le\alpha$．" "\n"
        r"**第二步：证 $\gamma\le\beta$**" "\n"
        r"用等体积法：$V_{P-ABC}=V_{B-PAC}$，即" "\n"
        r"$\dfrac13S_{\triangle ABC}\cdot d(P,ABC)=\dfrac13S_{\triangle PAC}\cdot d(B,PAC)$．" "\n"
        r"而 $d(P,ABC)=PA\sin\gamma$，$d(B,PAC)=AB\sin\beta$，且 $PA=AB$，故" "\n"
        r"$S_{\triangle ABC}\cdot\sin\gamma=S_{\triangle PAC}\cdot\sin\beta$．" "\n"
        r"又 $S_{\triangle ABC}=\dfrac12AB\cdot AC$（$AB\perp AC$），" "\n"
        r"$S_{\triangle PAC}=\dfrac12AC\cdot d(P,AC)\le\dfrac12AC\cdot PA=\dfrac12AC\cdot AB=S_{\triangle ABC}$" "\n"
        r"（用到点到直线的距离不大于该点到直线上某点的距离：$d(P,AC)\le PA$）．" "\n"
        r"于是 $\sin\gamma\le\sin\beta$，两角均为锐角 ⟹ $\gamma\le\beta$．" "\n"
        r"综上 $\gamma\le\beta$ 且 $\gamma\le\alpha$，故选 **A**．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓。原书 p278 详解：" "\n"
        r"「因为 $AB=AP$，$PD=BD$，所以 $\triangle ABD\cong\triangle APD$，所以 $\angle DAB=\angle DAP=\alpha$，" "\n"
        r"因为直线 $PA$ 与平面 $ABC$ 所成角为 $\gamma$，由最小角定理可得 $\gamma\le\alpha$，" "\n"
        r"再由 $V_{P-ABC}=V_{B-PAC}$，$S_{\triangle PAC}\le S_{\triangle ABC}$，进而可比较 $\beta,\gamma$ 的大小」" "\n"
        r"—— **$\triangle ABD\cong\triangle APD$、$\angle DAP=\alpha$、最小角定理 $\gamma\le\alpha$、等体积比较 $\beta$ 与 $\gamma$ 全部与我的推导一致** ✓✓✓" "\n"
        r"（详解在提取中于此处截断，第二步的 $S_{PAC}\le S_{ABC}$ 论证由我补出）" "\n"
        r"**独立验算**：" "\n"
        r"① **$\triangle ABD\cong\triangle APD$**：$AB=AP$、$BD=PD$、$AD=AD$ ⟹ SSS 全等 ✓✓✓" "\n"
        r"⟹ $\angle DAP=\angle DAB=\alpha$ ✓✓✓" "\n"
        r"② **最小角定理**：线面角是斜线与平面内所有直线夹角中**最小**的 ✓✓✓ ⟹ $\gamma\le\alpha$ ✓✓✓" "\n"
        r"③ **等体积**：$V_{P-ABC}=\frac13S_{ABC}\cdot d(P,ABC)$；$V_{B-PAC}=\frac13S_{PAC}\cdot d(B,PAC)$ ✓✓✓" "\n"
        r"④ **$d(P,ABC)=PA\sin\gamma$**：$\gamma$ 是 $PA$ 与平面 $ABC$ 的夹角，$A$ 在平面上 ✓✓✓" "\n"
        r"**$d(B,PAC)=AB\sin\beta$**：$\beta$ 是 $AB$ 与平面 $PAC$ 的夹角，$A$ 在平面 $PAC$ 上 ✓✓✓" "\n"
        r"⑤ **$S_{ABC}=\frac12 AB\cdot AC$**：$AB\perp AC$ ✓✓✓" "\n"
        r"⑥ **$d(P,AC)\le PA$**：$A$ 在直线 $AC$ 上，点到直线距离 $\le$ 到该直线上任一点距离 ✓✓✓" "\n"
        r"⟹ $S_{PAC}\le S_{ABC}$ ✓✓✓ ⟹ $\sin\gamma\le\sin\beta$ ⟹ $\gamma\le\beta$ ✓✓✓" "\n"
        r"⑦ **数值检验**：取 $A=(0,0,0)$、$C=(0,3,0)$、$B=(4,0,0)$（$AB\perp AC$），$AB=AP=4$。" "\n"
        r"取 $P=(1,1,3.742)$：$|AP|=\sqrt{1+1+14}=4$ ✓。" "\n"
        r"$\gamma$：$P$ 到平面 $ABC$（$z=0$）距离 $=3.742$，$\sin\gamma=\frac{3.742}4=0.9355$，$\gamma=69.3^\circ$。" "\n"
        r"$\alpha$：$D$ 在 $BC$ 上，$BC$ 从 $(4,0,0)$ 到 $(0,3,0)$。$D=(4-4t,3t,0)$。$PD=BD$：" "\n"
        r"$PD^2=(3-4t)^2+(1-3t)^2+14$；$BD^2=(4t)^2+(3t)^2=25t^2$。" "\n"
        r"$(9-24t+16t^2)+(1-6t+9t^2)+14=25t^2$ ⟹ $24-30t=0$ ⟹ $t=0.8$，$D=(0.8,2.4,0)$。" "\n"
        r"$\vec{AD}=(0.8,2.4,0)$、$\vec{AP}=(1,1,3.742)$。$\cos\alpha=\frac{0.8+2.4}{\sqrt{6.4}\cdot4}=\frac{3.2}{2.5298\cdot4}=0.3162$，$\alpha=71.6^\circ$。" "\n"
        r"$\gamma=69.3^\circ\le\alpha=71.6^\circ$ ✓✓✓" "\n"
        r"$\beta$：$AB$ 与平面 $PAC$ 的夹角。平面 $PAC$ 法向量 $=\vec{AP}\times\vec{AC}=(1,1,3.742)\times(0,3,0)$" "\n"
        r"$=(1\cdot0-3.742\cdot3,\;3.742\cdot0-1\cdot0,\;1\cdot3-1\cdot0)=(-11.226,\;0,\;3)$。" "\n"
        r"$\sin\beta=\frac{\lvert(4,0,0)\cdot(-11.226,0,3)\rvert}{4\cdot\sqrt{126+9}}=\frac{44.9}{4\cdot11.62}=\frac{44.9}{46.5}=0.9656$，$\beta=75.0^\circ$。" "\n"
        r"$\gamma=69.3^\circ\le\beta=75.0^\circ$ ✓✓✓ **两条不等式同时成立，选 A**" "\n"
        r"**答案 A 正确** ✓" "\n"
        r"**⭐⭐ 通法（三种角比大小）**：" "\n"
        r"① ⭐⭐ **最小角定理：线面角 $\le$ 该斜线与平面内任一直线的夹角** —— " "\n"
        r"看到「$\angle DAP$ 与线面角 $\gamma$」同台出现，第一反应就是它；" "\n"
        r"② ⭐ **比较两个线面角用等体积法**：$S_1\sin\theta_1=S_2\sin\theta_2$，**角的大小与所在面的面积反相关**；" "\n"
        r"③ ⭐ **$S_{PAC}\le S_{ABC}$ 的证明只用「点到直线距离 $\le$ 到该直线上一点的距离」**，是常用放缩；" "\n"
        r"④ ⭐ **全等条件是题眼**：$AB=AP$ 且 $PD=BD$ 配对，把 $\angle DAB$ 复制到 $\angle DAP$，" "\n"
        r"使 $\alpha$ 变成「$PA$ 与平面内直线 $AD$ 的夹角」，才能套最小角定理；" "\n"
        r"⑤ 检验：**建系取一组具体坐标，把三个角都算出来比一比**（$69.3^\circ\le71.6^\circ$、$\le75.0^\circ$ ✓）。"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-308'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-308-V1',
}

T308_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知三棱锥 $D-ABC$，记二面角 $C-AB-D$ 的平面角是 $\theta$，"
        r"直线 $DA$ 与平面 $ABC$ 所成的角是 $\theta_1$，直线 $DA$ 与 $BC$ 所成的角是 $\theta_2$，则（　　）"
    ),
    'opts': [
        ('A', r"$\theta\ge\theta_1$"),
        ('B', r"$\theta\le\theta_1$"),
        ('C', r"$\theta\ge\theta_2$"),
        ('D', r"$\theta\le\theta_2$"),
    ],
    'answer': 'A',
    'analysis': (
        r"以棱 $AB$ 为 $x$ 轴建系，平面 $ABC$ 为 $z=0$，则平面 $ABD$ 由它转过 $\theta$ 得到；"
        r"设 $D=(u,v\cos\theta,v\sin\theta)$，则 $\sin\theta_1=\frac{v\sin\theta}{\lvert DA\rvert}\le\sin\theta$。"
    ),
    'solution': (
        r"**第一步：建系**" "\n"
        r"以 $A$ 为原点，棱 $AB$ 所在直线为 $x$ 轴，平面 $ABC$ 为 $xOy$ 平面（即 $z=0$）．" "\n"
        r"平面 $ABD$ 与平面 $ABC$ 的交线是 $AB$（$x$ 轴），二面角为 $\theta$，" "\n"
        r"故平面 $ABD$ 中垂直于 $x$ 轴的方向为 $(0,\cos\theta,\sin\theta)$．" "\n"
        r"于是可设 $D=(u,\;v\cos\theta,\;v\sin\theta)$，其中 $v>0$（$D$ 在 $z>0$ 一侧）．" "\n"
        r"**第二步：算 $\theta_1$**" "\n"
        r"$\vec{DA}=A-D=(-u,\;-v\cos\theta,\;-v\sin\theta)$，$D$ 到平面 $ABC$ 的距离为 $v\sin\theta$．" "\n"
        r"$\sin\theta_1=\dfrac{\text{$D$ 到平面 }ABC\text{ 的距离}}{\lvert DA\rvert}=\dfrac{v\sin\theta}{\lvert\vec{DA}\rvert}$．" "\n"
        r"**第三步：比较**" "\n"
        r"$\lvert\vec{DA}\rvert=\sqrt{u^{2}+v^{2}}\ge v$，故" "\n"
        r"$\sin\theta_1=\dfrac{v\sin\theta}{\lvert\vec{DA}\rvert}\le\dfrac{v\sin\theta}{v}=\sin\theta$．" "\n"
        r"两角均在 $[0^\circ,90^\circ]$ 内，故 $\theta_1\le\theta$，即 $\theta\ge\theta_1$．" "\n"
        r"故选 **A**．" "\n"
        r"（注：$DA$ 与 $BC$ 的夹角 $\theta_2$ 与此二面角无必然大小关系，故 C、D 均不成立。）"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓。原书 p278 相关段落：「当二面角 $C-AB-D$ 是直二面角时，$\theta\ge\theta_2$，排除 D，故选：A」" "\n"
        r"—— **结论 $\theta\ge\theta_1$（选项 A）与我的推导一致** ✓✓✓" "\n"
        r"（该题详解在提取中较破碎，上述建系推导为我独立给出）" "\n"
        r"**独立验算**：" "\n"
        r"① **平面 $ABD$ 的方向**：由 $x$ 轴和 $(0,\cos\theta,\sin\theta)$ 张成 ✓✓✓" "\n"
        r"（$(0,\cos\theta,\sin\theta)$ 与 $z=0$ 内方向 $(0,1,0)$ 的夹角 $=\theta$ ✓）" "\n"
        r"② **$D=(u,v\cos\theta,v\sin\theta)$** ✓✓✓" "\n"
        r"③ **$D$ 到平面 $ABC$（$z=0$）的距离 $=v\sin\theta$** ✓✓✓" "\n"
        r"④ **$\lvert\vec{DA}\rvert=\sqrt{u^2+v^2\cos^2\theta+v^2\sin^2\theta}=\sqrt{u^2+v^2}$** ✓✓✓" "\n"
        r"⑤ **$\sin\theta_1=\frac{v\sin\theta}{\sqrt{u^2+v^2}}\le\sin\theta$** ✓✓✓（等号当 $u=0$，即 $DA\perp AB$）" "\n"
        r"⑥ **数值检验**：取 $\theta=60^\circ$、$v=1$、$u=0$：$D=(0,0.5,0.866)$，$\lvert\vec{DA}\rvert=1$。" "\n"
        r"$\sin\theta_1=\frac{0.866}1=0.866$ ⟹ $\theta_1=60^\circ=\theta$ ✓✓ **取等**" "\n"
        r"取 $u=1$：$D=(1,0.5,0.866)$，$\lvert\vec{DA}\rvert=\sqrt2=1.414$，$\sin\theta_1=\frac{0.866}{1.414}=0.6124$ ⟹ $\theta_1=37.8^\circ<60^\circ$ ✓✓✓" "\n"
        r"取 $u=3$：$D=(3,0.5,0.866)$，$\lvert\vec{DA}\rvert=\sqrt{10}=3.162$，$\sin\theta_1=0.2739$ ⟹ $\theta_1=15.9^\circ<60^\circ$ ✓✓✓" "\n"
        r"⑦ **$\theta_2$ 无必然关系**：仍取 $\theta=60^\circ$、$D=(0,0.5,0.866)$、$A=(0,0,0)$、$B=(1,0,0)$。" "\n"
        r"情形一 $C=(0.5,1,0)$：$BC$ 方向 $(-0.5,1,0)$，$\vec{DA}=(0,-0.5,-0.866)$。" "\n"
        r"$\cos\theta_2=\frac{\lvert-0.5\rvert}{1\cdot\sqrt{1.25}}=\frac{0.5}{1.118}=0.4472$，$\theta_2=63.4^\circ>\theta=60^\circ$ ⟹ **C 不成立** ✓" "\n"
        r"情形二 $C=(0.5,-3,0)$：$BC$ 方向 $(-0.5,-3,0)$。$\cos\theta_2=\frac{\lvert1.5\rvert}{\sqrt{9.25}}=\frac{1.5}{3.041}=0.4933$，$\theta_2=60.4^\circ>60^\circ$。" "\n"
        r"情形三 $C=(0.5,0.2,0)$：$BC$ 方向 $(-0.5,0.2,0)$。$\cos\theta_2=\frac{\lvert-0.1\rvert}{\sqrt{0.29}}=\frac{0.1}{0.5385}=0.1857$，$\theta_2=79.3^\circ>60^\circ$。" "\n"
        r"再取 $\theta=60^\circ$、$D=(0,0.5,0.866)$、$C=(5,0.1,0)$：$BC$ 方向 $(4,0.1,0)$ 归一化 $\approx(0.9997,0.025,0)$。" "\n"
        r"$\cos\theta_2=\lvert0.5\cdot0.025\rvert=0.0125$，$\theta_2=89.3^\circ>60^\circ$。" "\n"
        r"$\theta_2$ 在多种情形下都 $>\theta$，而 D 声称 $\theta\le\theta_2$ 恒成立 —— " "\n"
        r"但 $\theta_2$ 也可能 $<\theta$（取 $C$ 使 $BC$ 接近 $\vec{DA}$ 在平面内的投影方向即可），故 D 非恒真，" "\n"
        r"而 **A 是严格证明的不等式**，唯一正确 ✓" "\n"
        r"**答案 A（$\theta\ge\theta_1$）正确** ✓" "\n"
        r"**⭐⭐ 通法（二面角 vs 线面角）**：" "\n"
        r"① ⭐⭐ **二面角 $\ge$ 线面角**：沿棱建系后可一行证完 —— $\sin\theta_1=\frac{v\sin\theta}{\lvert DA\rvert}\le\sin\theta$；" "\n"
        r"**等号当且仅当斜线垂直于棱**（$u=0$）；" "\n"
        r"② ⭐ **建系模板**：棱为 $x$ 轴、一个半平面为 $z=0$、另一个半平面转过 $\theta$ ——" "\n"
        r"点坐标直接写成 $(u,v\cos\theta,v\sin\theta)$，所有角度都变成坐标比；" "\n"
        r"③ ⭐ **记忆法**：二面角是「面与面」的张角，线面角是「线与面」的张角，**前者更「大」**；" "\n"
        r"④ ⚠ **$\theta_2$（线与线）与二面角无必然大小关系**，凡出现「异面直线夹角」的选项多半是干扰项；" "\n"
        r"⑤ 检验：**改变 $u$ 看 $\theta_1$ 如何变化**（$u=0$ 取等、$u$ 越大 $\theta_1$ 越小 ✓）。"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-308'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-308-V2',
}

T310_E1 = {
    'type': '选择',
    'stem_text': (
        r"如图，在等边三角形 $ABC$ 中，$D,E$ 分别是线段 $AB,AC$ 上异于端点的动点，且 $BD=CE$，"
        r"现将三角形 $ADE$ 沿直线 $DE$ 折起，使平面 $ADE\perp$ 平面 $BCED$，"
        r"当 $D$ 从 $B$ 滑动到 $A$ 的过程中，则下列选项中错误的是（　　）"
    ),
    'opts': [
        ('A', r"$\angle ADB$ 的大小不会发生变化"),
        ('B', r"二面角 $A-BD-C$ 的平面角的大小不会发生变化"),
        ('C', r"$BD$ 与平面 $ABC$ 所成的角变大"),
        ('D', r"$AB$ 与 $DE$ 所成的角先变小后变大"),
    ],
    'answer': 'C',
    'analysis': (
        r"设边长 $1$、$AD=x$。$\triangle ADE$ 等边 ⟹ $AH=\frac{\sqrt3}2x$、$HG=\frac{\sqrt3}2(1-x)$；"
        r"$AH\perp$ 平面 $BCED$ ⟹ $AB^2=AH^2+BH^2$ ⟹ $\cos\angle ADB=-\frac14$ 恒定（A 对）；"
        r"$\sin\theta=\frac{d}{BD}=\frac{\sqrt3x}{2\sqrt{x^2+(1-x)^2}}$ 随 $x\searrow$ 而减小（C 错）。"
    ),
    'solution': (
        r"设等边 $\triangle ABC$ 边长为 $1$，$AD=x$（$0<x<1$），则 $BD=1-x$．" "\n"
        r"由 $BD=CE$ 且 $AB=AC$ 得 $AE=AD=x$，故 $DE\parallel BC$，$\triangle ADE$ 为边长 $x$ 的等边三角形．" "\n"
        r"过点 $A$ 作 $AG\perp BC$，交 $DE$ 于 $H$、交 $BC$ 于 $G$，连接 $BH$．" "\n"
        r"**第一步：折起后的垂直关系**" "\n"
        r"$AH\perp DE$，且平面 $ADE\perp$ 平面 $BCED$、交线为 $DE$ ⟹ $AH\perp$ 平面 $BCED$．" "\n"
        r"$\triangle ADE$ 边长 $x$ ⟹ $AH=\dfrac{\sqrt3}2x$；又 $AG=\dfrac{\sqrt3}2$ ⟹ $HG=\dfrac{\sqrt3}2(1-x)$．" "\n"
        r"**第二步：$\angle ADB$ 恒定（A 正确）**" "\n"
        r"$G$ 为 $BC$ 中点，$BG=\dfrac12$；$HG\perp BC$（$HG$ 在 $AG$ 上，$AG\perp BC$），" "\n"
        r"故 $BH^{2}=BG^{2}+HG^{2}=\dfrac14+\dfrac34(1-x)^{2}$．" "\n"
        r"由 $AH\perp$ 平面 $BCED$ 得 $AH\perp BH$，$AB^{2}=AH^{2}+BH^{2}=\dfrac34x^{2}+\dfrac14+\dfrac34(1-x)^{2}$．" "\n"
        r"于是 $\cos\angle ADB=\dfrac{AD^{2}+BD^{2}-AB^{2}}{2\cdot AD\cdot BD}$" "\n"
        r"$=\dfrac{x^{2}+(1-x)^{2}-\frac34x^{2}-\frac14-\frac34(1-x)^{2}}{2x(1-x)}=\dfrac{\frac14x^{2}+\frac14(1-x)^{2}-\frac14}{2x(1-x)}$" "\n"
        r"$=\dfrac{\frac14\bigl[x^{2}+(1-x)^{2}-1\bigr]}{2x(1-x)}=\dfrac{\frac14(-2x+2x^{2})}{2x(1-x)}=-\dfrac14$，" "\n"
        r"为常数，故 $\angle ADB$ 不变，A 正确．" "\n"
        r"**第三步：$BD$ 与平面 $ABC$ 所成的角（C 错误）**" "\n"
        r"用等体积法：$V_{A-BCD}=V_{D-ABC}$．" "\n"
        r"$S_{\triangle BCD}=\dfrac12\cdot BC\cdot HG=\dfrac12\cdot1\cdot\dfrac{\sqrt3}2(1-x)=\dfrac{\sqrt3}4(1-x)$，" "\n"
        r"$3V=S_{\triangle BCD}\cdot AH=\dfrac{\sqrt3}4(1-x)\cdot\dfrac{\sqrt3}2x=\dfrac38x(1-x)$．" "\n"
        r"$A$ 到 $BC$ 的距离（空间）$=\sqrt{AH^{2}+HG^{2}}=\dfrac{\sqrt3}2\sqrt{x^{2}+(1-x)^{2}}$，" "\n"
        r"$S_{\triangle ABC}=\dfrac12\cdot1\cdot\dfrac{\sqrt3}2\sqrt{x^{2}+(1-x)^{2}}=\dfrac{\sqrt3}4\sqrt{x^{2}+(1-x)^{2}}$．" "\n"
        r"设 $D$ 到平面 $ABC$ 的距离为 $d$，则 $d=\dfrac{3V}{S_{\triangle ABC}}=\dfrac{\frac38x(1-x)}{\frac{\sqrt3}4\sqrt{x^{2}+(1-x)^{2}}}=\dfrac{\sqrt3}2\cdot\dfrac{x(1-x)}{\sqrt{x^{2}+(1-x)^{2}}}$．" "\n"
        r"$\sin\theta=\dfrac{d}{BD}=\dfrac{\sqrt3}2\cdot\dfrac{x}{\sqrt{x^{2}+(1-x)^{2}}}=\dfrac{\sqrt3}2\cdot\dfrac{1}{\sqrt{1+\left(\frac1x-1\right)^{2}}}$．" "\n"
        r"$D$ 从 $B$ 滑到 $A$ 时 $x$ 从 $1$ 减到 $0$，$\dfrac1x-1$ 从 $0$ 增到 $+\infty$ ⟹ $\sin\theta$ **变小**，" "\n"
        r"故 $\theta$ 变小，C 说「变大」，**C 错误**．" "\n"
        r"**第四步：$AB$ 与 $DE$ 所成的角（D 正确）**" "\n"
        r"$DE\parallel BC$，故 $AB$ 与 $DE$ 所成角即 $\angle ABC$（或其补角）．" "\n"
        r"$\tan\angle ABC=\dfrac{\sqrt{AH^{2}+HG^{2}}}{BG}=\sqrt3\cdot\sqrt{x^{2}+(1-x)^{2}}$，" "\n"
        r"$x^{2}+(1-x)^{2}=2x^{2}-2x+1$ 在 $x=\dfrac12$ 处取最小，故 $\angle ABC$ 先变小后变大，D 正确．" "\n"
        r"故选 **C**．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓。原书 p280 详解：" "\n"
        r"「设等边三角形 $ABC$ 的边长为 1，$AD=x$（$0<x<1$），则 $BD=1-x$。在 $\triangle ABC$ 中，由 $BD=CE$，则 $DE\parallel BC$。" "\n"
        r"过点 $A$ 作 $AG\perp BC$，交 $DE$ 于点 $H$，交 $BC$ 于点 $G$，连接 $BH$，则 $AH\perp DE$。" "\n"
        r"由平面 $ADE\perp$ 平面 $BCED$，平面 $ADE\cap$ 平面 $BCED=DE$，所以 $AH\perp$ 平面 $BCED$…" "\n"
        r"设 $BD$ 与平面 $ABC$ 所成的角为 $\theta$… 当 $D$ 从 $B$ 滑动到 $A$ 的过程中，$x$ 的值从 1 变小到 0，" "\n"
        r"这一过程中…逐渐变大。所以在这一过程中，$\sin\theta$ 变小，则角 $\theta$ 变小，故选项 C 不正确」" "\n"
        r"—— **$AD=x$、$DE\parallel BC$、$AH\perp$ 平面 $BCED$、$\sin\theta$ 随 $x\searrow$ 变小、C 不正确 全部与我的推导一致** ✓✓✓" "\n"
        r"（原书 $\angle ADB$ 的计算式在提取中破碎，我用 $AB^2=AH^2+BH^2$ 重新算出 $\cos\angle ADB=-\frac14$）" "\n"
        r"**独立验算**：" "\n"
        r"① **$AH=\frac{\sqrt3}2x$**：$\triangle ADE$ 等边边长 $x$，高 $=\frac{\sqrt3}2x$ ✓✓✓" "\n"
        r"**$HG=\frac{\sqrt3}2(1-x)$**：$AG=\frac{\sqrt3}2$（原三角形高）✓✓✓" "\n"
        r"② **$BH^2=\frac14+\frac34(1-x)^2$**：$BG=\frac12$、$HG\perp BC$ ✓✓✓" "\n"
        r"③ **$AB^2=\frac34x^2+\frac14+\frac34(1-x)^2$** ✓✓✓" "\n"
        r"④ **$\cos\angle ADB=-\frac14$ 恒定**：" "\n"
        r"$x=0.5$：$AH=0.433$、$HG=0.433$、$BH^2=0.25+0.1875=0.4375$、$AB^2=0.1875+0.4375=0.625$。" "\n"
        r"$\cos=\frac{0.25+0.25-0.625}{2\cdot0.5\cdot0.5}=\frac{-0.125}{0.5}=-0.25$ ✓✓✓" "\n"
        r"$x=0.8$：$AH=0.6928$、$HG=0.1732$、$BH^2=0.25+0.03=0.28$、$AB^2=0.48+0.28=0.76$。" "\n"
        r"$\cos=\frac{0.64+0.04-0.76}{2\cdot0.8\cdot0.2}=\frac{-0.08}{0.32}=-0.25$ ✓✓✓ **恒定**" "\n"
        r"⑤ **$\sin\theta=\frac{\sqrt3}2\cdot\frac{x}{\sqrt{x^2+(1-x)^2}}$**：" "\n"
        r"$x=1$（$D$ 在 $B$）：$\sin\theta=\frac{\sqrt3}2\cdot\frac1{\sqrt{1}}=\frac{\sqrt3}2=0.866$，$\theta=60^\circ$" "\n"
        r"$x=0.5$：$\frac{\sqrt3}2\cdot\frac{0.5}{\sqrt{0.5}}=0.866\cdot0.7071=0.6124$，$\theta=37.8^\circ$" "\n"
        r"$x\to0$：$\sin\theta\to0$，$\theta\to0$ ✓✓✓ **单调变小，C 说变大，故 C 错**" "\n"
        r"⑥ **$\tan\angle ABC=\sqrt3\sqrt{x^2+(1-x)^2}$**：" "\n"
        r"$x=1$：$\tan=\sqrt3$，$\angle=60^\circ$；$x=0.5$：$\tan=\sqrt3\cdot0.7071=1.2247$，$\angle=50.8^\circ$；$x\to0$：$\to60^\circ$ ✓✓✓" "\n"
        r"**先变小后变大，D 正确** ✓✓✓" "\n"
        r"**答案 C 正确** ✓" "\n"
        r"**⭐⭐ 通法（翻折 + 动点）**：" "\n"
        r"① ⭐⭐ **翻折题第一步永远是找「垂直于交线的线」**：本题 $AH\perp DE$，" "\n"
        r"折起后由面面垂直立刻得 $AH\perp$ 平面 $BCED$ —— 这是把立体问题拆成直角三角形的钥匙；" "\n"
        r"② ⭐ **所有空间距离都归到两个直角三角形**：$AB^2=AH^2+BH^2$（$AH\perp$ 底面）、" "\n"
        r"$BH^2=BG^2+HG^2$（底面内），两步勾股；" "\n"
        r"③ ⭐ **判断「角是否变化」看余弦是否为常数**：算出 $\cos\angle ADB=-\frac14$ 恒定，A 立刻排除；" "\n"
        r"④ ⭐ **判断「角的变化趋势」用等体积法求距离**：$d=\frac{3V}{S}$，再除以 $BD$ 得 $\sin\theta$，" "\n"
        r"最后把 $\sin\theta$ 写成只含 $x$ 的式子看单调性；" "\n"
        r"⑤ ⚠ **「$\sin\theta$ 变小」⟹「$\theta$ 变小」**：线面角 $\theta\in[0^\circ,90^\circ]$，正弦单调 ⟹ 可直接推；" "\n"
        r"⑥ ⚠ **化成 $\frac1{\sqrt{1+(\frac1x-1)^2}}$ 的形式再看趋势**，比直接对 $x$ 求导快得多。"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-310'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-310-E1',
}

T310_V1 = {
    'type': '选择',
    'stem_text': (
        r"在正四面体 $D-ABC$（所有棱长均相等的三棱锥）中，点 $E$ 在棱 $AB$ 上，满足 $AE=2EB$，"
        r"点 $F$ 为线段 $AC$ 上的动点。设直线 $DE$ 与平面 $DBF$ 所成的角为 $\alpha$，则（　　）"
    ),
    'opts': [
        ('A', r"存在某个位置，使得 $DE\perp BF$"),
        ('B', r"存在某个位置，使得 $\angle FDB=\dfrac\pi4$"),
        ('C', r"存在某个位置，使得平面 $DEF\perp$ 平面 $DAC$"),
        ('D', r"存在某个位置，使得 $\alpha=\dfrac\pi6$"),
    ],
    'answer': 'C',
    'analysis': (
        r"建系令棱长 $2$：$A(-\frac{\sqrt3}3,-1,0)$、$B(\frac{2\sqrt3}3,0,0)$、$C(-\frac{\sqrt3}3,1,0)$、$D(0,0,\frac{2\sqrt6}3)$，"
        r"$E(\frac{\sqrt3}3,-\frac13,0)$、$F(-\frac{\sqrt3}3,\lambda,0)$。逐项检验：A 需 $\lambda=-3$（舍），"
        r"B 需 $\lambda^2=-1$（无解），C 需 $\lambda=-\frac37\in[-1,1]$ ✓，D 需 $\sin\alpha=\frac12$ 但最大仅 $\sqrt{\frac2{21}}$。"
    ),
    'solution': (
        r"设正四面体棱长为 $2$。以底面正三角形 $ABC$ 的中心 $O$ 为原点，" "\n"
        r"底面为 $xOy$ 平面，建立空间直角坐标系（外接圆半径 $\frac{2\sqrt3}3$）：" "\n"
        r"$A\!\left(-\dfrac{\sqrt3}3,-1,0\right)$、$B\!\left(\dfrac{2\sqrt3}3,0,0\right)$、$C\!\left(-\dfrac{\sqrt3}3,1,0\right)$、" "\n"
        r"$D\!\left(0,0,\dfrac{2\sqrt6}3\right)$（由 $\lvert DA\rvert=2$ 定出高）．" "\n"
        r"由 $AE=2EB$ 得 $E=\dfrac13A+\dfrac23B=\left(\dfrac{\sqrt3}3,-\dfrac13,0\right)$；" "\n"
        r"设 $F=\left(-\dfrac{\sqrt3}3,\lambda,0\right)$，$-1\le\lambda\le1$．" "\n"
        r"**A：** $\vec{DE}=\left(\dfrac{\sqrt3}3,-\dfrac13,-\dfrac{2\sqrt6}3\right)$，$\vec{BF}=\left(-\sqrt3,\lambda,0\right)$．" "\n"
        r"$\vec{DE}\cdot\vec{BF}=-1-\dfrac\lambda3=0\Rightarrow\lambda=-3\notin[-1,1]$，故 A 错．" "\n"
        r"**B：** $\vec{DF}=\left(-\dfrac{\sqrt3}3,\lambda,-\dfrac{2\sqrt6}3\right)$，$\vec{DB}=\left(\dfrac{2\sqrt3}3,0,-\dfrac{2\sqrt6}3\right)$．" "\n"
        r"$\lvert\vec{DF}\rvert^{2}=3+\lambda^{2}$、$\lvert\vec{DB}\rvert=2$、$\vec{DF}\cdot\vec{DB}=2$，" "\n"
        r"$\cos\angle FDB=\dfrac{2}{2\sqrt{3+\lambda^{2}}}=\dfrac1{\sqrt{3+\lambda^{2}}}\le\dfrac1{\sqrt3}<\dfrac{\sqrt2}2$，故 B 错．" "\n"
        r"**C：** $\vec{DA}=\left(-\dfrac{\sqrt3}3,-1,-\dfrac{2\sqrt6}3\right)$、$\vec{DC}=\left(-\dfrac{\sqrt3}3,1,-\dfrac{2\sqrt6}3\right)$，" "\n"
        r"平面 $DAC$ 的法向量 $\vec m=\vec{DA}\times\vec{DC}\propto(2\sqrt2,0,-1)$；" "\n"
        r"平面 $DEF$ 的法向量 $\vec n=\vec{DE}\times\vec{DF}\propto\left(\dfrac{2\sqrt6}3\left(\lambda+\dfrac13\right),\ \dfrac{4\sqrt2}3,\ \dfrac{\sqrt3}3\left(\lambda-\dfrac13\right)\right)$．" "\n"
        r"$\vec m\cdot\vec n\propto\dfrac{\sqrt3}3(7\lambda+3)=0\Rightarrow\lambda=-\dfrac37\in[-1,1]$，故 C 正确．" "\n"
        r"**D：** 平面 $DBF$ 的法向量 $\vec n_2=\vec{DB}\times\vec{DF}\propto\left(-\dfrac{2\sqrt6}3\lambda,\ \dfrac{4\sqrt2}3,\ -\dfrac{2\sqrt3}3\lambda\right)$，" "\n"
        r"可算得 $\sin^{2}\alpha=\dfrac{(\lambda+1)^{2}}{14(\lambda^{2}+2)}$，其在 $[-1,1]$ 上递增，最大值为 $\dfrac{4/3}{14}=\dfrac2{21}$，" "\n"
        r"$\sin\alpha\le\sqrt{\dfrac2{21}}<\dfrac12$，故 $\alpha\ne\dfrac\pi6$，D 错．" "\n"
        r"故选 **C**．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓。原书 p281 详解：" "\n"
        r"「对于 A 选项，若存在某个位置使得 $DE\perp BF$，$\vec{DE}=(\ldots)$，$\vec{BF}=(-\sqrt3,\lambda,0)$，" "\n"
        r"∴ $\vec{DE}\cdot\vec{BF}=-1-\lambda=0$（应为 $-1-\frac\lambda3=0$），解得 $\lambda=-3$，不合乎题意，A 选项错误；" "\n"
        r"对于 B 选项，…$\cos\langle\vec{DF},\vec{DB}\rangle=\ldots$，B 选项错误；" "\n"
        r"对于 C 选项，设平面 $DAC$ 的一个法向量为 $\vec m=(x,y,z)$，$\vec{DA}=(\ldots)$、$\vec{DC}=(\ldots)$，$\vec m\cdot\vec{DA}=\ldots$…」" "\n"
        r"—— **$E(\frac{\sqrt3}3,-\frac13,0)$、$F(-\frac{\sqrt3}3,\lambda,0)$、A 需 $\lambda=-3$ 舍去、B 错误、C 用平面 $DAC$ 法向量 全部与我的推导一致** ✓✓✓" "\n"
        r"（详解在 C 之后因 ⟨?⟩ 破碎中断，C 的 $\lambda=-\frac37$ 与 D 的 $\sin\alpha$ 上界由我补出）" "\n"
        r"**独立验算**：" "\n"
        r"① **坐标自检**：$\lvert A\rvert=\sqrt{\frac13+1}=\frac2{\sqrt3}$ ✓（外接圆半径）；$\lvert B\rvert=\frac{2\sqrt3}3=\frac2{\sqrt3}$ ✓✓✓" "\n"
        r"$\lvert DA\rvert^2=\frac13+1+\frac{24}9=\frac13+1+\frac83=4$ ⟹ $\lvert DA\rvert=2$ ✓✓✓" "\n"
        r"$\lvert AB\rvert^2=(\frac{2\sqrt3}3+\frac{\sqrt3}3)^2+1=(\sqrt3)^2+1=4$ ⟹ $2$ ✓✓✓" "\n"
        r"② **$E=\frac13A+\frac23B$**：$AE:EB=2:1$ ✓✓✓ $=(\frac{-\sqrt3/3+4\sqrt3/3}{3}? )$ —— 直接算：" "\n"
        r"$x_E=\frac13(-\frac{\sqrt3}3)+\frac23(\frac{2\sqrt3}3)=-\frac{\sqrt3}9+\frac{4\sqrt3}9=\frac{3\sqrt3}9=\frac{\sqrt3}3$ ✓✓✓" "\n"
        r"$y_E=\frac13(-1)+\frac23(0)=-\frac13$ ✓✓✓" "\n"
        r"③ **A 项**：$\vec{DE}\cdot\vec{BF}=\frac{\sqrt3}3(-\sqrt3)+(-\frac13)(\lambda)+(-\frac{2\sqrt6}3)(0)=-1-\frac\lambda3$ ✓✓✓" "\n"
        r"$=0$ ⟹ $\lambda=-3\notin[-1,1]$ ✓✓ **A 错**" "\n"
        r"④ **B 项**：$\vec{DF}\cdot\vec{DB}=(-\frac{\sqrt3}3)(\frac{2\sqrt3}3)+\lambda\cdot0+(-\frac{2\sqrt6}3)(-\frac{2\sqrt6}3)=-\frac{2\cdot3}9+\frac{4\cdot6}9=-\frac69+\frac{24}9=\frac{18}9=2$ ✓✓✓" "\n"
        r"$\lvert\vec{DF}\rvert^2=\frac13+\lambda^2+\frac{24}9=\frac13+\lambda^2+\frac83=3+\lambda^2$ ✓；$\lvert\vec{DB}\rvert^2=\frac{12}9+\frac{24}9=\frac{36}9=4$ ⟹ $2$ ✓✓✓" "\n"
        r"$\cos\angle FDB=\frac2{2\sqrt{3+\lambda^2}}$，最大（$\lambda=0$）$=\frac1{\sqrt3}=0.577<0.707$ ✓✓ **B 错**" "\n"
        r"⑤ **C 项**：$\vec{DA}\times\vec{DC}$ 我算得 $(2b,0,-2a)$ 型 $=\left(\frac{4\sqrt6}3,0,-\frac{2\sqrt3}3\right)\propto(2\sqrt2,0,-1)$ ✓✓✓" "\n"
        r"$\vec n=\vec{DE}\times\vec{DF}$：分量 $\left(\frac{2\sqrt6}3(\lambda+\frac13),\ \frac{4\sqrt2}3,\ \frac{\sqrt3}3(\lambda-\frac13)\right)$" "\n"
        r"$\vec m\cdot\vec n\propto 2\sqrt2\cdot\frac{2\sqrt6}3(\lambda+\frac13)+(-1)\cdot\frac{\sqrt3}3(\lambda-\frac13)$" "\n"
        r"$=\frac{4\sqrt{12}}3(\lambda+\frac13)-\frac{\sqrt3}3(\lambda-\frac13)=\frac{8\sqrt3}3(\lambda+\frac13)-\frac{\sqrt3}3(\lambda-\frac13)$" "\n"
        r"$=\frac{\sqrt3}3\left[8\lambda+\frac83-\lambda+\frac13\right]=\frac{\sqrt3}3(7\lambda+3)$ ✓✓✓ ⟹ $\lambda=-\frac37\approx-0.4286\in[-1,1]$ ✓✓✓ **C 正确**" "\n"
        r"⑥ **D 项**：$\sin^2\alpha=\frac{(\lambda+1)^2}{14(\lambda^2+2)}$，在 $[-1,1]$ 上 $g(\lambda)=\frac{(\lambda+1)^2}{\lambda^2+2}$ 递增（$g'=\frac{2(\lambda+1)(2-\lambda)}{(\lambda^2+2)^2}\ge0$）✓✓✓" "\n"
        r"最大值 $g(1)=\frac43$ ⟹ $\sin^2\alpha\le\frac{4/3}{14}=\frac{2}{21}=0.0952$，$\sin\alpha\le0.3086<0.5$ ✓✓ **D 错**" "\n"
        r"**答案 C 正确** ✓" "\n"
        r"**⭐⭐ 通法（正四面体建系）**：" "\n"
        r"① ⭐⭐ **正四面体的标准坐标**：底面中心为原点、底面为 $z=0$，" "\n"
        r"三个底面顶点在半径 $\frac{a}{\sqrt3}$ 的圆上（$a$ 为棱长），顶点高 $\frac{\sqrt6}3a$ —— " "\n"
        r"取 $a=2$ 时半径 $\frac{2\sqrt3}3$、高 $\frac{2\sqrt6}3$，坐标最整齐；" "\n"
        r"② ⭐ **动点用一个参数表示**：$F$ 在 $AC$ 上，因 $A,C$ 的 $x$ 相同，可直接写 $F=(-\frac{\sqrt3}3,\lambda,0)$ —— " "\n"
        r"**先观察哪一维坐标是常数**，能省很多事；" "\n"
        r"③ ⭐ **「存在某个位置」型选项 ⟹ 解方程看解是否落在参数范围内**：" "\n"
        r"A 得 $\lambda=-3$（越界）、B 无实数解、C 得 $\lambda=-\frac37$（合法 ✓）、D 需 $\sin\alpha=\frac12$ 但上界不到；" "\n"
        r"④ ⭐ **面面垂直 ⟺ 两法向量点积为零** —— 先求平面 $DAC$ 的法向量（固定），再求动平面的法向量，点积令零；" "\n"
        r"⑤ ⚠ **$\vec{DB}$ 与 $\vec{DF}$ 都从 $D$ 出发**，别写成 $\vec{BD}$；**方向搞反点积变号**；" "\n"
        r"⑥ 检验：**算完先自检所有棱长是否为 $2$**（$AB$、$AD$ 都验过 ✓），坐标错了后面全错。"
    ),
    'difficulty': 0.94,
    'topics': ['M-T-310'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-310-V1',
}

T310_V2 = {
    'type': '填空',
    'stem_text': (
        r"如图，在边长为 $4$ 的正三角形 $ABC$ 中，$D,E,F$ 分别为各边的中点，$G,H$ 分别为 $DE,AF$ 的中点，"
        r"将 $\triangle ABC$ 沿 $DE,EF,DF$ 折成正四面体 $P-DEF$，则在此正四面体中，下列说法正确的是 ____" "\n\n"
        r"① 异面直线 $PG$ 与 $DH$ 所成的角的余弦值为 $\dfrac23$；" "\n"
        r"② $DF\perp PE$；" "\n"
        r"③ $GH$ 与 $PD$ 所成的角为 $45^\circ$；" "\n"
        r"④ $PG$ 与 $EF$ 所成角为 $60^\circ$。"
    ),
    'opts': [],
    'answer': r"①②③",
    'analysis': (
        r"折成正四面体 $P-DEF$，棱长为 $2$（原三角形边长 $4$ 的一半）。$G$ 为 $DE$ 中点，$H$ 为 $PF$ 中点（$A$ 折到 $P$）。"
        r"建系后逐项算点积即可。"
    ),
    'solution': (
        r"原正三角形边长 $4$，$D,E,F$ 为各边中点 ⟹ $DE=EF=FD=2$，" "\n"
        r"折成正四面体 $P-DEF$ 后棱长为 $2$，且 $A,B,C$ 三点重合于 $P$．" "\n"
        r"于是 $G$ 为 $DE$ 中点，$H$ 为 $PF$ 中点（$H$ 原为 $AF$ 中点，折后 $A\to P$）．" "\n"
        r"**建系**：以 $\triangle DEF$ 的中心为原点、$\triangle DEF$ 所在平面为 $z=0$，棱长 $2$：" "\n"
        r"$D\!\left(\dfrac{2\sqrt3}3,0,0\right)$、$E\!\left(-\dfrac{\sqrt3}3,1,0\right)$、$F\!\left(-\dfrac{\sqrt3}3,-1,0\right)$、$P\!\left(0,0,\dfrac{2\sqrt6}3\right)$．" "\n"
        r"$G=\dfrac{D+E}2=\left(\dfrac{\sqrt3}6,\dfrac12,0\right)$，$\quad H=\dfrac{P+F}2=\left(-\dfrac{\sqrt3}6,-\dfrac12,\dfrac{\sqrt6}3\right)$．" "\n"
        r"**①** $\vec{PG}=\left(\dfrac{\sqrt3}6,\dfrac12,-\dfrac{2\sqrt6}3\right)$，$\vec{DH}=\left(-\dfrac{5\sqrt3}6,-\dfrac12,\dfrac{\sqrt6}3\right)$：" "\n"
        r"$\lvert\vec{PG}\rvert^{2}=\dfrac1{12}+\dfrac14+\dfrac83=3$，$\lvert\vec{DH}\rvert^{2}=\dfrac{25}{12}+\dfrac14+\dfrac23=3$，" "\n"
        r"$\vec{PG}\cdot\vec{DH}=-\dfrac{15}{36}-\dfrac14-\dfrac{12}9=-2$，$\cos=\dfrac2{\sqrt3\cdot\sqrt3}=\dfrac23$ ✓" "\n"
        r"**②** $\vec{DF}=(-\sqrt3,-1,0)$，$\vec{PE}=\left(-\dfrac{\sqrt3}3,1,-\dfrac{2\sqrt6}3\right)$：" "\n"
        r"$\vec{DF}\cdot\vec{PE}=1-1+0=0$ ⟹ $DF\perp PE$ ✓" "\n"
        r"**③** $\vec{GH}=\left(-\dfrac{\sqrt3}3,-1,\dfrac{\sqrt6}3\right)$，$\vec{PD}=\left(\dfrac{2\sqrt3}3,0,-\dfrac{2\sqrt6}3\right)$：" "\n"
        r"$\lvert\vec{GH}\rvert^{2}=\dfrac13+1+\dfrac23=2$，$\lvert\vec{PD}\rvert=2$，$\vec{GH}\cdot\vec{PD}=-\dfrac23-\dfrac{12}9=-2$，" "\n"
        r"$\cos=\dfrac2{\sqrt2\cdot2}=\dfrac{\sqrt2}2$ ⟹ $45^\circ$ ✓" "\n"
        r"**④** $\vec{EF}=(0,-2,0)$：$\vec{PG}\cdot\vec{EF}=-1$，$\cos=\dfrac1{\sqrt3\cdot2}=\dfrac{\sqrt3}6\ne\dfrac12$ ✗" "\n"
        r"故正确的是 **①②③**．"
    ),
    'review': (
        r"★ 题干、答案完整 ✓。原书 p281 分析：「可证明 $DE\perp$ 平面 $PGE$，可得①正确；连接 $FG$，取中点 $M$，" "\n"
        r"异面直线 $PG$ 与 $DH$ 所成的角为 $\angle DHM$，由余弦定理可证明②正确；连接 $NH$，异面 $GH$ 与 $PD$ 所成的角为 $\angle GHN$，" "\n"
        r"由余弦定理可得③不对；异面 $PG$ 与 $EF$ 所成角的为 $\angle GPN$，由余弦定理可得④不对，从而可得结果」" "\n"
        r"—— **答案 ①②③（③ 正确、④ 不对）与我的推导一致** ✓✓✓" "\n"
        r"（⚠ 原书【分析】中「③不对、④不对」的**编号描述有笔误**：按答案 ①②③，应是**④ 不对**而 ③ 正确；" "\n"
        r"原书把「④ 不对」写在「③」的位置，属编号错位。以答案 ①②③ 与我的四点验算为准）" "\n"
        r"（详解中具体计算因 ⟨?⟩ 破碎，上述坐标推导为我独立给出）" "\n"
        r"**独立验算**：" "\n"
        r"① **正四面体棱长 2**：原三角形边长 4，中位线 $DE=EF=FD=2$ ✓✓✓" "\n"
        r"② **坐标自检**：$\lvert D\rvert=\frac{2\sqrt3}3=\frac2{\sqrt3}$ ✓（底面外接圆半径 $=\frac{a}{\sqrt3}$）；$\lvert E\rvert=\sqrt{\frac13+1}=\frac2{\sqrt3}$ ✓✓✓" "\n"
        r"$\lvert P-D\rvert^2=\frac{12}9+\frac{24}9=\frac{36}9=4$ ⟹ $2$ ✓✓✓；$\lvert D-E\rvert^2=(\sqrt3)^2+1=4$ ⟹ $2$ ✓✓✓" "\n"
        r"③ **$H$ 是 $PF$ 中点**：$A$ 折到 $P$，$F$ 不动，故 $AF$ 中点是 $PF$ 中点 ✓✓✓" "\n"
        r"$H=\frac{P+F}2=(-\frac{\sqrt3}6,-\frac12,\frac{\sqrt6}3)$ ✓✓✓" "\n"
        r"④ **①的余弦 $\frac23$**：$\vec{PG}\cdot\vec{DH}=\frac{\sqrt3}6(-\frac{5\sqrt3}6)+\frac12(-\frac12)+(-\frac{2\sqrt6}3)(\frac{\sqrt6}3)$" "\n"
        r"$=-\frac{15}{36}-\frac14-\frac{12}9=-\frac5{12}-\frac3{12}-\frac43=-\frac8{12}-\frac{16}{12}=-2$ ✓✓✓" "\n"
        r"$\cos=\frac{2}{\sqrt3\sqrt3}=\frac23$ ✓✓✓" "\n"
        r"⑤ **②垂直**：$\vec{DF}\cdot\vec{PE}=(-\sqrt3)(-\frac{\sqrt3}3)+(-1)(1)+0=\frac33-1=0$ ✓✓✓" "\n"
        r"⑥ **③ 45°**：$\vec{GH}\cdot\vec{PD}=(-\frac{\sqrt3}3)(\frac{2\sqrt3}3)+0+(\frac{\sqrt6}3)(-\frac{2\sqrt6}3)=-\frac{2\cdot3}9-\frac{2\cdot6}9=-\frac69-\frac{12}9=-2$ ✓✓✓" "\n"
        r"$\cos=\frac{2}{\sqrt2\cdot2}=\frac{1}{\sqrt2}$ ⟹ $45^\circ$ ✓✓✓" "\n"
        r"⑦ **④ 不是 60°**：$\vec{PG}\cdot\vec{EF}=0+\frac12(-2)+0=-1$；$\cos=\frac{1}{\sqrt3\cdot2}=\frac{\sqrt3}6=0.2887$ ⟹ $73.2^\circ\neq60^\circ$ ✓✓✓ **④ 错**" "\n"
        r"**答案 ①②③ 正确** ✓" "\n"
        r"**⭐⭐ 通法（折叠成正四面体）**：" "\n"
        r"① ⭐⭐ **三个角 $A,B,C$ 折起后重合为一点 $P$** —— " "\n"
        r"所以原图形中「$A$ 与某中点的连线」折后变成「$P$ 与该中点的连线」，**先把所有点重新映射一遍**再动手；" "\n"
        r"② ⭐ **正四面体标准坐标**：底面顶点在半径 $\frac a{\sqrt3}$ 的圆上（$z=0$），顶点 $(0,0,\frac{\sqrt6}3a)$；" "\n"
        r"取 $a=2$ 时坐标最整齐（半径 $\frac{2\sqrt3}3$、高 $\frac{2\sqrt6}3$）；" "\n"
        r"③ ⭐ **异面直线夹角 = 两方向向量夹角（取绝对值）**，$\cos=\frac{\lvert\vec u\cdot\vec v\rvert}{\lvert u\rvert\lvert v\rvert}$ —— **别忘绝对值**；" "\n"
        r"④ ⚠ **中点归属要看折叠后是谁**：$H$ 原为 $AF$ 中点，$A\to P$ 后 $H$ 是 $PF$ 中点，**不是 $AF$ 中点**；" "\n"
        r"⑤ ⚠ **四个论断要逐项算，不能靠「对称」猜** —— 本题①$\frac23$、②垂直、③$45^\circ$、④$73.2^\circ$，四个结论各不相同；" "\n"
        r"⑥ 检验：**算完先自检棱长**（$PD$、$DE$ 都等于 2 ✓），坐标体系错了后面全错。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-310'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-310-V2',
}

T311_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知三棱锥 $P-ABC$ 的所有顶点都在球 $O$ 的球面上，$\triangle ABC$ 满足 $AB=2$，$\angle ACB=90^\circ$，"
        r"$PA$ 为球 $O$ 的直径且 $PA=4$，则点 $P$ 到底面 $ABC$ 的距离为（　　）"
    ),
    'opts': [
        ('A', r"$2$"),
        ('B', r"$2\sqrt2$"),
        ('C', r"$3$"),
        ('D', r"$2\sqrt3$"),
    ],
    'answer': 'D',
    'analysis': (
        r"$PA$ 是直径 ⟹ $O$ 是 $PA$ 中点、$R=2$；取 $AB$ 中点 $D$，$OD=\sqrt{OA^2-1}=\sqrt3$，"
        r"又 $CD=1$（直角三角形斜边中点），$OC^2=OD^2+CD^2$ ⟹ $OD\perp$ 底面，故 $d_P=2\cdot OD=2\sqrt3$。"
    ),
    'solution': (
        r"**第一步：定球心与半径**" "\n"
        r"$PA$ 为球的直径且 $PA=4$ ⟹ 球心 $O$ 是 $PA$ 的中点，半径 $R=2$，$OA=OP=2$．" "\n"
        r"**第二步：证明 $OD\perp$ 平面 $ABC$**" "\n"
        r"取 $AB$ 的中点 $D$，连 $OD$、$CD$．" "\n"
        r"由 $OA=OB=2$（都是半径）得 $OD\perp AB$，且 $OD=\sqrt{OA^{2}-\left(\dfrac{AB}2\right)^{2}}=\sqrt{4-1}=\sqrt3$．" "\n"
        r"由 $\angle ACB=90^\circ$，$D$ 为斜边 $AB$ 的中点得 $CD=\dfrac{AB}2=1$．" "\n"
        r"又 $OC=2$（半径），而 $OC^{2}=4=3+1=OD^{2}+CD^{2}$ ⟹ $\angle ODC=90^\circ$，即 $OD\perp CD$．" "\n"
        r"$AB\cap CD=D$，$AB,CD\subset$ 平面 $ABC$ ⟹ $OD\perp$ 平面 $ABC$．" "\n"
        r"**第三步：求 $P$ 到底面的距离**" "\n"
        r"$A$ 在平面 $ABC$ 上（距离 $0$），$O$ 是 $PA$ 的中点，故 $O$ 到平面 $ABC$ 的距离 $=\dfrac{d(P,ABC)}2$；" "\n"
        r"而 $O$ 到平面的距离就是 $OD=\sqrt3$，故 $d(P,ABC)=2\sqrt3$．" "\n"
        r"故选 **D**．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓。原书 p282 详解：" "\n"
        r"「∵ 三棱锥 $P-ABC$ 的所有顶点都在球 $O$ 的球面上，$PA$ 为球 $O$ 的直径且 $PA=4$，" "\n"
        r"∴ 球心 $O$ 是 $PA$ 的中点，球半径 $R=OC=\frac12PA=2$，取 $AB$ 的中点 $D$，连接 $OD$、$CD$，则 $OD\perp AB$，且" "\n"
        r"$OD=\sqrt{OA^2-(\frac{AB}2)^2}=\sqrt3$，∵ $\triangle ABC$ 满足 $AB=2$，$\angle ACB=90^\circ$，∴ $CD=\frac{AB}2=1$，" "\n"
        r"∴ $OC^2=CD^2+OD^2$，∴ $OD\perp CD$，又 $CD\cap AB=D$，$CD,AB\subset$ 平面 $ABC$，∴ $OD\perp$ 平面 $ABC$，" "\n"
        r"所以点 $P$ 到底面 $ABC$ 的距离为 $d=\ldots$」" "\n"
        r"—— **$O$ 是 $PA$ 中点、$R=2$、$OD=\sqrt3$、$CD=1$、$OC^2=CD^2+OD^2$、$OD\perp$ 平面 $ABC$ 全部与我的推导一致** ✓✓✓" "\n"
        r"（详解末行的 $d$ 值在提取中破碎，由我算出 $d=2\sqrt3$）" "\n"
        r"**⚠ 选项还原**：PDF 提取为 `A.2 B. 2 2 C.3 D. 2 3`（根号丢失）。" "\n"
        r"**判定依据**：$d=2\cdot OD=2\sqrt3=3.464$ ✓；选项 D ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **$O$ 是 $PA$ 中点、$R=2$**：直径 $PA=4$ ⟹ $R=2$ ✓✓✓" "\n"
        r"② **$OD=\sqrt{OA^2-(AB/2)^2}$**：$\triangle OAB$ 等腰（$OA=OB=2$），$D$ 为底边中点 ⟹ $OD\perp AB$ ✓✓✓" "\n"
        r"$=\sqrt{4-1}=\sqrt3$ ✓✓✓" "\n"
        r"③ **$CD=\frac{AB}2=1$**：直角三角形斜边中点到三顶点等距 ✓✓✓" "\n"
        r"④ **$OC^2=OD^2+CD^2$**：$4=3+1$ ✓✓✓ ⟹ $OD\perp CD$ ✓✓✓" "\n"
        r"⑤ **$OD\perp$ 平面 $ABC$**：$OD$ 垂直于平面内两条相交直线 $AB$、$CD$ ✓✓✓" "\n"
        r"⑥ **$d(P,ABC)=2\sqrt3$**：$A$ 在平面上，$O$ 是 $PA$ 中点 ⟹ $d(O)=\frac12 d(P)$ ⟹ $d(P)=2\sqrt3$ ✓✓✓" "\n"
        r"⑦ **建系完整验证**：取 $D$ 为原点，$AB$ 沿 $x$ 轴，$A=(1,0,0)$、$B=(-1,0,0)$。" "\n"
        r"$C$ 在以 $AB$ 为直径的圆上（$\angle ACB=90^\circ$），取 $C=(0,1,0)$，则 $CD=1$ ✓。" "\n"
        r"$OD\perp$ 平面 $ABC$（$z=0$）⟹ $O=(0,0,\sqrt3)$。检验 $OA=\sqrt{1+3}=2$ ✓✓✓；$OC=\sqrt{1+3}=2$ ✓✓✓" "\n"
        r"$P$ 满足 $O$ 是 $PA$ 中点：$P=2O-A=(-1,0,2\sqrt3)$。" "\n"
        r"检验 $OP=\sqrt{1+12}=\sqrt{13}$？ ✗ —— 应为 $2$。" "\n"
        r"**修正**：$P=2O-A=2(0,0,\sqrt3)-(1,0,0)=(-1,0,2\sqrt3)$，则 $\vec{OP}=P-O=(-1,0,\sqrt3)$，$\lvert\vec{OP}\rvert=\sqrt{1+3}=2$ ✓✓✓" "\n"
        r"（$O$ 到 $P$ 的向量才是半径；$P$ 的位置坐标 $(-1,0,2\sqrt3)$ 正确）" "\n"
        r"$P$ 到平面 $ABC$（$z=0$）的距离 $=\lvert2\sqrt3\rvert=2\sqrt3=3.464$ ✓✓✓" "\n"
        r"检验 $PB$：$B=(-1,0,0)$、$P=(-1,0,2\sqrt3)$，$PB=2\sqrt3$；$P$ 在球上需 $OB=2$ ✓（$B$ 在球上），$P$ 在球上：$\lvert OP\rvert=2$ ✓✓✓" "\n"
        r"**答案 D（$2\sqrt3$）正确** ✓" "\n"
        r"**⭐⭐ 通法（球中的距离）**：" "\n"
        r"① ⭐⭐ **「$PA$ 是直径」给两件事**：球心 $O$ 是 $PA$ 中点（距离可折半），且 $\angle PBA=\angle PCA=90^\circ$（直径所对圆周角）；" "\n"
        r"② ⭐ **证明线面垂直凑两条相交直线**：本题 $OD\perp AB$（等腰三角形底边中线）+ $OD\perp CD$（由 $OC^2=OD^2+CD^2$ 反推）—— " "\n"
        r"**用勾股定理的逆定理证垂直**是这类题的常规操作；" "\n"
        r"③ ⭐ **直角三角形斜边中点**：$CD=\frac{AB}2$，这个 $1$ 是凑出 $3+1=4$ 的关键；" "\n"
        r"④ ⭐ **球心到平面的距离 $\times 2$ = 直径端点到平面的距离**（当另一端点在平面上时）—— " "\n"
        r"本题 $A$ 在底面 $ABC$ 上，所以 $d(P)=2\cdot d(O)=2\sqrt3$；" "\n"
        r"⑤ ⚠ **$d(O)=OD$ 而不是别的**：必须先证 $OD\perp$ 平面，才能说 $O$ 到平面的距离是 $OD$；" "\n"
        r"⑥ 检验：**建系把 $O$、$P$、$C$ 的坐标全定出来，验证 $OA=OB=OC=OP=2$**（全部通过 ✓）。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-311'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-311-V1',
}

QS = [T308_V1, T308_V2, T310_E1, T310_V1, T310_V2, T311_V1]
