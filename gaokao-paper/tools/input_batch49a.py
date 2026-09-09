# -*- coding: utf-8 -*-
r"""第49批（上）：解三角形 · 四边形与圆内接（解答题）

来源：2024高中数学热点题型归纳完整解析版.pdf
p192（PDF 页 191）M-T-227

## 选题

本文件取 M-T-227 的 E1、V1、V2（3 道解答题）。

## ⚠ 跳过 V3

题干只剩「求 $\sin\angle BCE$ 的值；求 $\triangle CED$ 的周长」—— **点 $E$ 的定义丢失**，无解。

## ★★ 本批的核心：四边形 ⟹ 拆成两个共边三角形

「【提分秘籍】四边形，一般适当的连接对角线，分解为有公共边的两个三角形。
如果是有外接圆，则要充分运用**对角互补**这个隐形条件。」

三题都是这条的应用：

| 题 | 辅助线 | 关键 |
|---|---|---|
| E1 | 连 $BD$ | $AB\parallel CD$ ⟹ $\angle BDC=\angle ABD$（内错角），用它把两个三角形的正弦定理串起来 |
| V1 | 连 $BD$ | 先在 $\triangle BCD$ 中求 $BD$，再回到 $\triangle ABD$ |
| V2 | 用外接圆 | $\angle D=180^\circ-\angle B$（**对角互补**），这是隐藏条件 |

## 三题验算（全部独立推导，与答案完全吻合）

| 题 | 我的结果 | 答案 |
|---|---|---|
| E1(2) | $CD=\sqrt2+\sqrt6$ | ✓ |
| V1 | $\sin\angle ABD=\frac{\sqrt{21}}7$；$AB=3$，$S=\frac{3\sqrt3}2$ | ✓ |
| V2 | $B=60^\circ$；$S_{ABCD}=8\sqrt3$ | ✓ |
"""

T227_E1 = {
    'type': '解答',
    'stem_text': (
        r"（2022·山东青岛·高三期末）如图，在四边形 $ABCD$ 中，$AB\parallel CD$，"
        r"$AD\cdot\sin\angle ADC=AB\cdot\sin\angle ABC$．" "\n"
        r"（1）求证：$AB=BC$；" "\n"
        r"（2）若 $AD=BD=2$，$\angle ADB=90^\circ$，求 $CD$ 的长．"
    ),
    'opts': [],
    'answer': r"（1）证明见解析；（2）$CD=\sqrt2+\sqrt6$",
    'analysis': (
        r"（1）**连对角线 $BD$**，把四边形拆成 $\triangle ABD$ 与 $\triangle CBD$。"
        r"由 $AB\parallel CD$ 得 $\angle BDC=\angle ABD$（内错角），"
        r"再在两个三角形中分别用正弦定理，把已知条件转化成 $AB\cdot\sin\angle C=BC\cdot\sin\angle C$。" "\n"
        r"（2）$\triangle ABD$ 是等腰直角三角形，得 $AB=BC=2\sqrt2$、$\angle ABD=45^\circ$，"
        r"于是 $\angle CDB=45^\circ$，在 $\triangle CBD$ 中用余弦定理解 $CD$。"
    ),
    'solution': (
        r"**（1）证明**" "\n"
        r"连接 $BD$．因为 $AB\parallel CD$，所以" "\n"
        r"$\angle ADC+\angle A=\pi$，$\angle ABC+\angle C=\pi$，且 $\angle BDC=\angle ABD$（内错角）．" "\n"
        r"由已知 $AD\cdot\sin\angle ADC=AB\cdot\sin\angle ABC$：" "\n"
        r"$AD\cdot\sin(\pi-\angle A)=AB\cdot\sin(\pi-\angle C)\Rightarrow AD\cdot\sin\angle A=AB\cdot\sin\angle C$　①" "\n"
        r"在 $\triangle ABD$ 中，由正弦定理 $\dfrac{BD}{\sin\angle A}=\dfrac{AD}{\sin\angle ABD}$：" "\n"
        r"$BD\cdot\sin\angle ABD=AD\cdot\sin\angle A$　②" "\n"
        r"在 $\triangle CBD$ 中，由正弦定理 $\dfrac{BD}{\sin\angle C}=\dfrac{BC}{\sin\angle BDC}$：" "\n"
        r"$BD\cdot\sin\angle BDC=BC\cdot\sin\angle C$　③" "\n"
        r"由 $\angle BDC=\angle ABD$，比较 ②③ 得 $AD\cdot\sin\angle A=BC\cdot\sin\angle C$．" "\n"
        r"与 ① 对比：$AB\cdot\sin\angle C=BC\cdot\sin\angle C$．" "\n"
        r"因 $\sin\angle C\neq0$，故 $AB=BC$．证毕．" "\n"
        r"**（2）求解**" "\n"
        r"$\triangle ABD$ 中 $AD=BD=2$、$\angle ADB=90^\circ$，故" "\n"
        r"$AB=\sqrt{2^{2}+2^{2}}=2\sqrt2$，且 $\angle ABD=45^\circ$．" "\n"
        r"由（1）$AB=BC$ 得 $BC=2\sqrt2$；由 $\angle BDC=\angle ABD$ 得 $\angle CDB=45^\circ$．" "\n"
        r"在 $\triangle CBD$ 中，由余弦定理：" "\n"
        r"$BC^{2}=CD^{2}+BD^{2}-2\,CD\cdot BD\cos\angle CDB$" "\n"
        r"$8=CD^{2}+4-2\cdot CD\cdot2\cdot\dfrac{\sqrt2}2=CD^{2}+4-2\sqrt2\,CD$" "\n"
        r"$\Rightarrow CD^{2}-2\sqrt2\,CD-4=0$" "\n"
        r"$\Rightarrow CD=\dfrac{2\sqrt2\pm\sqrt{8+16}}2=\dfrac{2\sqrt2\pm2\sqrt6}2=\sqrt2\pm\sqrt6$．" "\n"
        r"取正根：$CD=\sqrt2+\sqrt6$（$\sqrt2-\sqrt6<0$ 舍去）．"
    ),
    'review': (
        r"★ 题干与答案完整 ✓，由详解「(1) 因为 $AB\parallel CD$，所以 $\angle ADC+\angle A=\pi$、"
        r"$\angle ABC+\angle C=\pi$、$\angle BDC=\angle ABD$…」还原，与我的推导**逐字一致** ✓。" "\n"
        r"**独立验算**：" "\n"
        r"① **（2）等腰直角**：$AD=BD=2$、$\angle ADB=90^\circ$ ⟹ $AB=\sqrt{4+4}=2\sqrt2\approx2.828$ ✓" "\n"
        r"$\angle ABD=45^\circ$（等腰直角）✓" "\n"
        r"② **解 $CD$**：$CD^{2}-2\sqrt2\,CD-4=0$，判别式 $=8+16=24$，" "\n"
        r"$CD=\frac{2.828+\sqrt{24}}2=\frac{2.828+4.899}2=3.864$" "\n"
        r"$\sqrt2+\sqrt6=1.414+2.449=3.863$ ✓✓ **完全吻合**" "\n"
        r"③ **代回验证余弦定理**：$CD=3.8637$、$BD=2$、$\angle CDB=45^\circ$" "\n"
        r"$BC^{2}=3.8637^{2}+4-2(3.8637)(2)(0.7071)=14.928+4-10.928=8.0$ ✓✓ **$BC=2\sqrt2$ 成立**" "\n"
        r"④ **验 $\angle BDC=\angle ABD$ 的一致性**：由 $CD=3.8637$、$BD=2$、$BC=2.828$，" "\n"
        r"$\cos\angle CDB=\frac{CD^{2}+BD^{2}-BC^{2}}{2\cdot CD\cdot BD}=\frac{14.928+4-8}{2(3.8637)(2)}=\frac{10.928}{15.455}=0.7071$ ✓ → $45^\circ$ ✓✓" "\n"
        r"**答案 $CD=\sqrt2+\sqrt6$ 正确** ✓" "\n"
        r"**⭐ 通法（四边形 ⟹ 拆两个共边三角形）**：" "\n"
        r"① **连对角线 $BD$**，把四边形拆成 $\triangle ABD$ 与 $\triangle CBD$（公共边 $BD$）；" "\n"
        r"② 在两个三角形中分别写**正弦定理**，形式统一为「$BD\cdot\sin(\text{对角})=\text{边}\cdot\sin(\text{已知角})$」；" "\n"
        r"③ 若有一组内错角相等（平行线）或公共角，就能把两式**串起来**。" "\n"
        r"**本题的题眼**：$AB\parallel CD$ ⟹ $\angle BDC=\angle ABD$ —— 这组内错角让 ②③ 两式的左边相等，" "\n"
        r"于是右边的 $AD\sin A$ 与 $BC\sin C$ 相等，再结合已知条件就消掉了 $\sin\angle C$。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-227'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-227-E1',
}

T227_V1 = {
    'type': '解答',
    'stem_text': (
        r"（2022·全国·高三专题练习）如图，在平面四边形 $ABCD$ 中，$\angle BAD=60^\circ$，"
        r"$BC=1$，$AD=CD=2$，$\angle DCB=120^\circ$．" "\n"
        r"（1）求 $\angle ABD$ 的正弦值；" "\n"
        r"（2）求 $AB$ 的长及 $\triangle ABD$ 的面积．"
    ),
    'opts': [],
    'answer': r"（1）$\dfrac{\sqrt{21}}7$；（2）$AB=3$，$S_{\triangle ABD}=\dfrac{3\sqrt3}2$",
    'analysis': (
        r"**先在 $\triangle BCD$ 中求 $BD$**（$BC,CD$ 及夹角都已知），"
        r"再回到 $\triangle ABD$：$BD$、$AD$、$\angle BAD$ 已知，用正弦定理求角、余弦定理求边。"
    ),
    'solution': (
        r"**（1）先求 $BD$**" "\n"
        r"在 $\triangle BCD$ 中，$BC=1$、$CD=2$、$\angle DCB=120^\circ$，由余弦定理：" "\n"
        r"$BD^{2}=BC^{2}+CD^{2}-2\,BC\cdot CD\cos120^\circ=1+4-2\cdot1\cdot2\cdot\left(-\dfrac12\right)=1+4+2=7$" "\n"
        r"$\Rightarrow BD=\sqrt7$．" "\n"
        r"在 $\triangle ABD$ 中，由正弦定理 $\dfrac{BD}{\sin\angle BAD}=\dfrac{AD}{\sin\angle ABD}$：" "\n"
        r"$\sin\angle ABD=\dfrac{AD\cdot\sin\angle BAD}{BD}=\dfrac{2\cdot\sin60^\circ}{\sqrt7}$"
        r"$=\dfrac{2\cdot\frac{\sqrt3}2}{\sqrt7}=\dfrac{\sqrt3}{\sqrt7}=\dfrac{\sqrt{21}}7$．" "\n"
        r"**（2）求 $AB$ 与面积**" "\n"
        r"在 $\triangle ABD$ 中，由余弦定理 $BD^{2}=AD^{2}+AB^{2}-2\,AD\cdot AB\cos\angle BAD$：" "\n"
        r"$7=4+AB^{2}-2\cdot2\cdot AB\cdot\dfrac12=4+AB^{2}-2AB$" "\n"
        r"$\Rightarrow AB^{2}-2AB-3=0\Rightarrow(AB-3)(AB+1)=0\Rightarrow AB=3$（舍去 $-1$）．" "\n"
        r"$S_{\triangle ABD}=\dfrac12\,AB\cdot AD\cdot\sin\angle BAD=\dfrac12\cdot3\cdot2\cdot\dfrac{\sqrt3}2=\dfrac{3\sqrt3}2$．"
    ),
    'review': (
        r"★ 题干与答案完整 ✓，由详解「(1) 先由余弦定理求出 $BD$，再由正弦定理求出 $\angle ABD$ 的正弦值；" "\n"
        r"(2) 在 $\triangle ABD$ 中由余弦定理…$\frac{7}{2\sqrt3}=\frac{2}{\sin\angle ABD}$，∴ $\sin\angle ABD=\frac{\sqrt{21}}7$…" "\n"
        r"$7=2^{2}+AB^{2}-2\cdot2\cdot AB\cdot\frac12$，解得 $AB=3$ 或 $AB=-1$（舍去）…" "\n"
        r"$S_{\triangle ABD}=\frac12 AB\cdot AD\sin\angle BAD=\frac12\cdot3\cdot2\cdot\frac{\sqrt3}2=\frac{3\sqrt3}2$」还原，" "\n"
        r"与我的推导**完全一致** ✓。" "\n"
        r"**独立验算**：" "\n"
        r"① **求 $BD$**：$BD^{2}=1+4-2(1)(2)\cos120^\circ=1+4+2=7$ ✓，$BD=\sqrt7\approx2.6458$" "\n"
        r"② **求 $\sin\angle ABD$**：$\frac{2\sin60^\circ}{\sqrt7}=\frac{1.7321}{2.6458}=0.6547$" "\n"
        r"$\frac{\sqrt{21}}7=\frac{4.5826}7=0.6547$ ✓✓" "\n"
        r"③ **求 $AB$**：$AB^{2}-2AB-3=0$ → $AB=3$ ✓；代回：$4+9-2(2)(3)(0.5)=13-6=7=BD^{2}$ ✓✓" "\n"
        r"④ **面积**：$\frac12\cdot3\cdot2\cdot\frac{\sqrt3}2=1.5\sqrt3=2.598$；$\frac{3\sqrt3}2=2.598$ ✓✓" "\n"
        r"⑤ **用另一法验面积**（$S=\frac12 AB\cdot BD\sin\angle ABD$）：" "\n"
        r"$\frac12\cdot3\cdot2.6458\cdot0.6547=2.598$ ✓✓ **两法一致**" "\n"
        r"⑥ **验 $\angle BAD=60^\circ$ 自洽**：由余弦定理" "\n"
        r"$\cos\angle BAD=\frac{AB^{2}+AD^{2}-BD^{2}}{2\cdot AB\cdot AD}=\frac{9+4-7}{2(3)(2)}=\frac6{12}=0.5$ ✓ → $60^\circ$ ✓✓" "\n"
        r"**答案正确** ✓" "\n"
        r"**⭐ 通法**：" "\n"
        r"① 四边形中**哪条对角线两边都已知，就先连哪条** —— 本题 $\triangle BCD$ 中 $BC,CD$ 及夹角全已知，" "\n"
        r"故先连 $BD$ 把它解出来。" "\n"
        r"② 已知两边及夹角求第三边：余弦定理；已知两边一对角求另一角：正弦定理。" "\n"
        r"③ **求 $AB$ 时会出现两次**：$AB^{2}-2AB-3=0$ 给 $3$ 和 $-1$，负根必舍（边长 $>0$）。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-227'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-227-V1',
}

T227_V2 = {
    'type': '解答',
    'stem_text': (
        r"（2022·全国·高三专题练习）如图，在 $\triangle ABC$ 中，$\angle BAC$、$\angle B$、$\angle ACB$ "
        r"的对边分别为 $a,b,c$，且 $c+c\cos B=\sqrt3\,b\sin C$．" "\n"
        r"（1）求角 $B$ 的大小；" "\n"
        r"（2）已知 $b=2\sqrt7$，$a+c=10$，若 $D$ 为 $\triangle ABC$ 外接圆劣弧 $AC$ 上一点，"
        r"且 $2AD=DC$，求四边形 $ABCD$ 的面积．"
    ),
    'opts': [],
    'answer': r"（1）$B=60^\circ$；（2）$8\sqrt3$",
    'analysis': (
        r"（1）用正弦定理把边换成角：$c=2R\sin C$、$b=2R\sin B$，约去 $\sin C$ 得 "
        r"$\sqrt3\sin B-\cos B=1$，即 $2\sin(B-\frac\pi6)=1$。" "\n"
        r"（2）$a+c$ 与 $ac$ 都可得，先求 $S_{\triangle ABC}$；"
        r"再用**圆内接四边形对角互补**得 $\angle D=120^\circ$，在 $\triangle ACD$ 中解出 $AD,DC$。"
    ),
    'solution': (
        r"**（1）求角 $B$**" "\n"
        r"由正弦定理 $\dfrac b{\sin B}=\dfrac c{\sin C}=2R$，即 $b=2R\sin B$、$c=2R\sin C$，代入：" "\n"
        r"$2R\sin C+2R\sin C\cos B=\sqrt3\cdot2R\sin B\sin C$" "\n"
        r"$\Rightarrow\sin C\,(1+\cos B)=\sqrt3\sin B\sin C$" "\n"
        r"因 $\sin C\neq0$：$1+\cos B=\sqrt3\sin B\Rightarrow\sqrt3\sin B-\cos B=1$" "\n"
        r"$\Rightarrow2\sin\left(B-\dfrac\pi6\right)=1$ ⟹ $\sin\left(B-\dfrac\pi6\right)=\dfrac12$" "\n"
        r"⟹ $B-\dfrac\pi6=\dfrac\pi6$ 或 $\dfrac{5\pi}6$，即 $B=\dfrac\pi3$ 或 $B=\pi$（舍）．" "\n"
        r"故 $B=60^\circ$．" "\n"
        r"**（2）求面积**" "\n"
        r"由余弦定理 $b^{2}=a^{2}+c^{2}-2ac\cos B=a^{2}+c^{2}-ac=(a+c)^{2}-3ac$：" "\n"
        r"$28=100-3ac\Rightarrow ac=24$．" "\n"
        r"$S_{\triangle ABC}=\dfrac12 ac\sin B=\dfrac12\cdot24\cdot\dfrac{\sqrt3}2=6\sqrt3$．" "\n"
        r"因为 $A,B,C,D$ 四点共圆，且 $D$ 在**劣弧** $AC$ 上（$D$ 与 $B$ 分居 $AC$ 两侧），" "\n"
        r"由圆内接四边形对角互补：$\angle ADC=180^\circ-\angle B=120^\circ$．" "\n"
        r"设 $AD=t$，则 $DC=2t$。在 $\triangle ACD$ 中由余弦定理：" "\n"
        r"$AC^{2}=AD^{2}+DC^{2}-2\,AD\cdot DC\cos120^\circ$"
        r"$=t^{2}+4t^{2}-2\cdot t\cdot2t\left(-\dfrac12\right)=5t^{2}+2t^{2}=7t^{2}$" "\n"
        r"而 $AC=b=2\sqrt7$，故 $28=7t^{2}\Rightarrow t^{2}=4\Rightarrow t=2$，即 $AD=2$、$DC=4$．" "\n"
        r"$S_{\triangle ACD}=\dfrac12\,AD\cdot DC\sin120^\circ=\dfrac12\cdot2\cdot4\cdot\dfrac{\sqrt3}2=2\sqrt3$．" "\n"
        r"$S_{ABCD}=S_{\triangle ABC}+S_{\triangle ACD}=6\sqrt3+2\sqrt3=8\sqrt3$．"
    ),
    'review': (
        r"★ 题干与答案完整 ✓（**详解未提取完整**，上述推导为我独立完成）。" "\n"
        r"**独立验算**：" "\n"
        r"① **验 $B=60^\circ$ 满足原式**：$c+c\cos60^\circ=1.5c$；$\sqrt3 b\sin C$" "\n"
        r"由 $\frac b{\sin B}=\frac c{\sin C}$ 得 $b\sin C=c\sin B=c\cdot\frac{\sqrt3}2$，" "\n"
        r"故 $\sqrt3 b\sin C=\sqrt3\cdot c\cdot\frac{\sqrt3}2=1.5c$ ✓✓ **两边相等**" "\n"
        r"② **求 $ac$**：$b^{2}=(a+c)^{2}-3ac$ → $28=100-3ac$ → $ac=24$ ✓" "\n"
        r"$a+c=10$、$ac=24$ ⟹ $a,c$ 为 $t^{2}-10t+24=0$ 的根 → $\{4,6\}$" "\n"
        r"验：$4+6=10$ ✓、$4\times6=24$ ✓" "\n"
        r"③ **$S_{\triangle ABC}$**：$\frac12\cdot24\cdot\frac{\sqrt3}2=6\sqrt3\approx10.392$ ✓" "\n"
        r"④ **求 $t$**：$7t^{2}=b^{2}=28$ → $t=2$ ✓；$AD=2$、$DC=4$" "\n"
        r"验 $2AD=DC$：$2(2)=4$ ✓✓" "\n"
        r"验 $AC$：$AC^{2}=4+16-2(2)(4)(-0.5)=20+8=28$ → $AC=2\sqrt7$ ✓✓ **与 $b$ 一致**" "\n"
        r"⑤ **$S_{\triangle ACD}$**：$\frac12\cdot2\cdot4\cdot\frac{\sqrt3}2=2\sqrt3\approx3.464$ ✓" "\n"
        r"⑥ **总面积**：$6\sqrt3+2\sqrt3=8\sqrt3\approx13.856$；答案 $8\sqrt3$ ✓✓✓" "\n"
        r"⑦ **验「$D$ 在劣弧」的必要性**：若 $D$ 与 $B$ 在 $AC$ **同侧**，则" "\n"
        r"$\angle ADC=\angle B=60^\circ$（同弧所对圆周角），此时" "\n"
        r"$28=t^{2}+4t^{2}-2(t)(2t)(0.5)=5t^{2}-2t^{2}=3t^{2}$ → $t^{2}=\frac{28}3$，$S_{\triangle ACD}=\frac12 t\cdot2t\cdot\frac{\sqrt3}2=\frac{\sqrt3}2t^{2}=\frac{14\sqrt3}3$" "\n"
        r"总面积 $=6\sqrt3+\frac{14\sqrt3}3\approx20.78\neq8\sqrt3$ ✗ —— "
        r"**说明「劣弧」=「$D$ 与 $B$ 异侧」这个理解是唯一与答案吻合的** ✓" "\n"
        r"**答案（1）$60^\circ$、（2）$8\sqrt3$ 正确** ✓" "\n"
        r"**⭐ 通法（圆内接四边形）**：" "\n"
        r"① **对角互补**是隐藏条件：$\angle D+\angle B=180^\circ$（当 $D$ 在**不含 $B$ 的弧**上时）。" "\n"
        r"⚠ **方向要分清**：$D$ 在**劣弧** $AC$ 上 ⟹ $D$ 与 $B$ **异侧** ⟹ $\angle D=180^\circ-\angle B$；" "\n"
        r"$D$ 在**优弧** $AC$ 上 ⟹ $D$ 与 $B$ **同侧** ⟹ $\angle D=\angle B$。" "\n"
        r"（本题我特意算了两种情形：只有「异侧」给出 $8\sqrt3$，与答案一致 —— 这也是验证手段。）" "\n"
        r"② 面积拆成 $S_{\triangle ABC}+S_{\triangle ACD}$（$D$ 异侧）或差的绝对值（同侧）。" "\n"
        r"③ **$1+\cos B=\sqrt3\sin B$ 型**方程：一律化 $A\sin x+B\cos x$ 成一个角，"
        r"$\sqrt3\sin B-\cos B=2\sin(B-\frac\pi6)$ —— 比平方好用（平方会引入增根）。"
    ),
    'difficulty': 0.93,
    'topics': ['M-T-227'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-227-V2',
}

QS = [T227_E1, T227_V1, T227_V2]
