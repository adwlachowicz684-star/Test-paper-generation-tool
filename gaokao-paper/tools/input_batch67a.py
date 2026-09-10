# -*- coding: utf-8 -*-
r"""第67批：立体几何（6 题）

来源：2024高中数学热点题型归纳完整解析版.pdf p258、p264、p268、p270
M-T-297-E1/V1、M-T-292-V2/V3、M-T-302-E1/V2

## ★★ 六题我全部独立推导并与原书答案对拍，全部吻合

| 题 | 关键 | 答案 |
|---|---|---|
| M-T-297-E1 | 坐标法：球心 $O(0,-\frac{\sqrt3}2,\frac32)$，$R^2=\frac{21}4$、$OE'^2=3$ | $R=\frac{\sqrt{21}}2$，截面 $=\frac{9\pi}4$ |
| M-T-297-V1 | 两外心垂线相交，$O_1O_2^2=21$、$|OO_2|=4$ ⟹ $R^2=13+16=29$ | $116\pi$ |
| M-T-292-V2 | $x^2y^2=48(x^2+y^2)$、$s\ge192$ ⟹ $S=4\sqrt s\ge32\sqrt3$ | **B** |
| M-T-292-V3 | $V=\frac13(30+30)=20$；$f=5-t$，周长 $=2\sqrt{74}$ | $20$；$2\sqrt{74}$ |
| M-T-302-E1 | $R^2=(2\sqrt2r-R)^2+r^2$ ⟹ $9r^2=4\sqrt2rR$ ⟹ $r=1$ | $3\pi$ |
| M-T-302-V2 | $h=\frac{4a}3$、$R=\frac{2a}3$、$r=\frac{7a}6$ ⟹ $7:4$ | **A** |

## 三处「算出来才敢改」的还原

1. **M-T-297-E1**：ref_bank 存 `219 π` / `24`，实为 $R=\frac{\sqrt{21}}2$ 与 $\frac{9\pi}4$。
2. **M-T-297-V1**：答案 `116π` 我独立算出 $R^2=29$ ⟹ $4\pi\cdot29=116\pi$ ✓
3. **M-T-302-E1**：详解「解得 r = 」后破碎，我反解出 $r=1$（验 $R^2=\frac{81}{32}$ ✓）。
"""

T297_E1 = {
    'type': '填空',
    'stem_text': (
        r"已知菱形 $ABCD$ 边长为 $3$，$\angle BAD=60^\circ$，$E$ 为对角线 $AC$ 上一点，$AC=6AE$。"
        r"将 $\triangle ABD$ 沿 $BD$ 翻折到 $\triangle A'BD$ 的位置，$E$ 记为 $E'$，"
        r"且二面角 $A'-BD-C$ 的大小为 $120^\circ$，则三棱锥 $A'-BCD$ 的外接球的半径为 ____；"
        r"过 $E'$ 作平面 $\alpha$ 与该外接球相交，所得截面面积的最小值为 ____。 "
    ),
    'opts': [],
    'answer': r"$\dfrac{\sqrt{21}}2$；$\dfrac{9\pi}4$",
    'analysis': (
        r"两三角形均为边长 $3$ 的等边三角形，外心即重心。球心在二面角平分面上，"
        r"$\angle MO'O=60^\circ$ ⟹ $OM=\frac32$、$O'C=\frac{3\sqrt3}2$ 方向 ⟹ $R^2=\frac{21}4$。"
        r"$OE'^2=3$ ⟹ $r^2=R^2-3=\frac94$ ⟹ $S=\frac{9\pi}4$。"
    ),
    'solution': (
        r"因 $\angle BAD=60^\circ$ 且 $AB=AD=3$，故 $\triangle ABD$ 为等边三角形，$BD=3$；" "\n"
        r"同理 $\triangle CBD$ 为等边三角形（$BC=CD=3$）。于是 $AC=2\cdot\dfrac{3\sqrt3}2=3\sqrt3$。" "\n"
        r"**建系**：以 $BD$ 中点 $O'$ 为原点，$BD$ 为 $x$ 轴，$O'C$ 方向为 $y$ 轴负向，" "\n"
        r"$z$ 轴垂直底面。则 $B\!\left(-\dfrac32,0,0\right)$、$D\!\left(\dfrac32,0,0\right)$、$C\!\left(0,-\dfrac{3\sqrt3}2,0\right)$、" "\n"
        r"$A\!\left(0,\dfrac{3\sqrt3}2,0\right)$。翻折后二面角为 $120^\circ$，即 $A$ 绕 $BD$ 转过 $60^\circ$：" "\n"
        r"$A'=\left(0,\dfrac{3\sqrt3}2\cos60^\circ,\dfrac{3\sqrt3}2\sin60^\circ\right)=\left(0,\dfrac{3\sqrt3}4,\dfrac94\right)$．" "\n"
        r"**球心**：$\triangle CBD$ 与 $\triangle A'BD$ 均为等边三角形，外心即重心，" "\n"
        r"在 $yz$ 平面内距 $O'$ 各 $\dfrac{\sqrt3}2$，方向角分别为 $180^\circ$ 与 $60^\circ$，" "\n"
        r"故球心 $O$ 在角平分线（方向角 $120^\circ$）上，且 $O'O=\sqrt3$：" "\n"
        r"$O=\sqrt3\left(0,\cos120^\circ,\sin120^\circ\right)=\left(0,-\dfrac{\sqrt3}2,\dfrac32\right)$．" "\n"
        r"$R^{2}=\lvert OC\rvert^{2}=\left(-\dfrac{\sqrt3}2+\dfrac{3\sqrt3}2\right)^{2}+\left(\dfrac32\right)^{2}=3+\dfrac94=\dfrac{21}4$，" "\n"
        r"故 $R=\dfrac{\sqrt{21}}2$．" "\n"
        r"**截面**：$AE=\dfrac{AC}6=\dfrac{\sqrt3}2$，故 $E=\left(0,\dfrac{3\sqrt3}2-\dfrac{\sqrt3}2,0\right)=(0,\sqrt3,0)$，" "\n"
        r"翻折后 $E'=\left(0,\sqrt3\cos60^\circ,\sqrt3\sin60^\circ\right)=\left(0,\dfrac{\sqrt3}2,\dfrac32\right)$．" "\n"
        r"$\lvert OE'\rvert^{2}=\left(-\dfrac{\sqrt3}2-\dfrac{\sqrt3}2\right)^{2}+0=3$．" "\n"
        r"截面面积最小时 $OE'\perp\alpha$，截面圆半径 $r_0=\sqrt{R^{2}-OE'^{2}}=\sqrt{\dfrac{21}4-3}=\dfrac32$，" "\n"
        r"$S=\pi r_0^{2}=\dfrac{9\pi}4$。故答案为 $\dfrac{\sqrt{21}}2$，$\dfrac{9\pi}4$。"
    ),
    'review': (
        r"★ 题干、答案完整，详解由我独立推导（原书 p264 详解关键量全部吻合）。" "\n"
        r"原书答案破碎为 `219 π` / `24`，实为 $R=\frac{\sqrt{21}}2$ 与 $\frac{9\pi}4$。" "\n"
        r"原书详解关键句：" "\n"
        r"「记 $AC\cap BD=O'$，连接 $CO',O'O$，因为二面角 $A'-BD-C$ 的大小为 $120^\circ$，且 $A'O'\perp BD$、$CO'\perp BD$，" "\n"
        r"所以二面角 $A'-BD-C$ 的平面角为 $\angle A'O'C=120^\circ$；因为 $O'M=O'N$，所以 $\angle MO'O=\angle NO'O=60^\circ$；" "\n"
        r"又因为 $BC=3$，所以 $CO'=A'O'=3\sin60^\circ=\frac{3\sqrt3}2$，所以 $MO'=NO'=\frac13CO'=\frac{\sqrt3}2$；" "\n"
        r"所以 $OM=O'M\tan60^\circ=\frac32$，又 $CM=\frac23CO'=\sqrt3$，所以 $OC=\sqrt{CM^{2}+OM^{2}}=\sqrt{3+\frac94}=\frac{\sqrt{21}}2$；" "\n"
        r"…$NE'=\ldots$ 且 $ON=OM=\frac32$，所以 $OE'=\sqrt{ON^{2}+NE'^{2}}=\ldots=3$，" "\n"
        r"所以 $r=\sqrt{R^{2}-OE'^{2}}=\sqrt{\frac{21}4-3}=\frac32$，所以此时截面面积为 $S=\pi\cdot(\frac32)^{2}=\frac{9\pi}4$」" "\n"
        r"—— **$CO'=\frac{3\sqrt3}2$、$MO'=\frac{\sqrt3}2$、$\angle MO'O=60^\circ$、$OM=\frac32$、$OC=\frac{\sqrt{21}}2$、$OE'^2=3$、$r=\frac32$、$S=\frac{9\pi}4$ 全部与我的推导一致** ✓✓✓" "\n"
        r"**独立验算（坐标法，完全独立）**：" "\n"
        r"① **$BD=3$**：$\triangle ABD$ 中 $AB=AD=3$、$\angle BAD=60^\circ$ ⟹ 等边 ⟹ $BD=3$ ✓✓✓" "\n"
        r"② **$AC=3\sqrt3$**：菱形对角线 $AC=2\cdot3\sin60^\circ=3\sqrt3$ ✓✓✓（$AE=\frac{AC}6=\frac{\sqrt3}2$ ✓）" "\n"
        r"③ **$A'$ 坐标**：绕 $x$ 轴（$BD$）转 $60^\circ$，$y=\frac{3\sqrt3}2\cos60^\circ=\frac{3\sqrt3}4$、$z=\frac{3\sqrt3}2\sin60^\circ=\frac94$ ✓✓✓" "\n"
        r"验 $|A'B|=\sqrt{\frac94+\frac{81}{16}+\frac94\cdot\frac34}$… 直接算：$A'B^2=(\frac32)^2+(\frac{3\sqrt3}4)^2+(\frac94)^2=\frac94+\frac{27}{16}+\frac{81}{16}=\frac{36+27+81}{16}=\frac{144}{16}=9$ ⟹ $A'B=3$ ✓✓✓" "\n"
        r"④ **球心方向角 $120^\circ$**：两外心方向角 $60^\circ$（$A'$ 侧）与 $180^\circ$（$C$ 侧），平分即 $120^\circ$ ✓✓✓" "\n"
        r"$|O'O|=\sqrt{(\frac{\sqrt3}2)^2+(\frac32)^2}=\sqrt{\frac34+\frac94}=\sqrt3$ ✓✓✓" "\n"
        r"$O=\sqrt3(0,-\frac12,\frac{\sqrt3}2)=(0,-\frac{\sqrt3}2,\frac32)$ ✓✓✓" "\n"
        r"⑤ **$R^2=\frac{21}4$**：$O-C=(0,-\frac{\sqrt3}2+\frac{3\sqrt3}2,\frac32)=(0,\sqrt3,\frac32)$，$R^2=3+\frac94=\frac{21}4$ ✓✓✓" "\n"
        r"验 $|OA'|$：$A'-O=(0,\frac{3\sqrt3}4+\frac{\sqrt3}2,\frac94-\frac32)=(0,\frac{5\sqrt3}4,\frac34)$。" "\n"
        r"$|OA'|^2=\frac{75}{16}+\frac9{16}=\frac{84}{16}=\frac{21}4$ ✓✓✓ **与 $|OC|$ 相等，确为球心**" "\n"
        r"验 $|OB|$：$B-O=(-\frac32,\frac{\sqrt3}2,-\frac32)$，$|OB|^2=\frac94+\frac34+\frac94=\frac{21}4$ ✓✓✓" "\n"
        r"验 $|OD|$：同理 $=\frac{21}4$ ✓✓✓ **四顶点等距**" "\n"
        r"⑥ **$E'=(0,\frac{\sqrt3}2,\frac32)$**、**$|OE'|^2=3$**：$E'-O=(0,\sqrt3,0)$ ✓✓✓" "\n"
        r"⑦ **$r_0^2=\frac{21}4-3=\frac94$ ⟹ $r_0=\frac32$ ⟹ $S=\pi\cdot\frac94=\frac{9\pi}4$** ✓✓✓" "\n"
        r"⑧ **数值检验**：$R=\frac{\sqrt{21}}2=2.2913$，$R^2=5.25$ ✓；$OE'=\sqrt3=1.7321$ ✓；" "\n"
        r"$r_0=\sqrt{5.25-3}=\sqrt{2.25}=1.5$ ✓；$S=\pi(2.25)=7.0686=\frac{9\pi}4$ ✓✓✓" "\n"
        r"**答案 $\frac{\sqrt{21}}2$、$\frac{9\pi}4$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（翻折 + 二面角 ⟹ 外接球）**：" "\n"
        r"① ⭐⭐ **翻折后仍是等边三角形，外心即重心** —— 重心到边中点距离 $=\frac13$ 高 $=\frac{\sqrt3}2$（边长 $3$，高 $\frac{3\sqrt3}2$）；" "\n"
        r"② ⭐⭐ **球心在二面角的平分面上**：两外心 $M,N$ 对 $O'$ 张角 $=$ 二面角 $120^\circ$，平分得 $60^\circ$，" "\n"
        r"于是 $OM=O'M\tan60^\circ$ —— **这是「外心垂线相交型」的标准算法**；" "\n"
        r"③ ⭐ **坐标法更稳**：把 $A'$ 写成绕轴转 $\theta$ 的形式 $(0,r\cos\theta,r\sin\theta)$，" "\n"
        r"球心方向角取两外心方向角的平均 —— **本题 $60^\circ$ 与 $180^\circ$ 的平均是 $120^\circ$**；" "\n"
        r"④ ⭐ **截面面积最小 ⟺ $OE'\perp\alpha$**：$S=\pi(R^{2}-OE'^{2})$，" "\n"
        r"**关键是算出 $OE'$ 而非找球心到平面的距离**；" "\n"
        r"⑤ ⚠ **$E$ 随 $A$ 一起翻折**：$E$ 在线段 $AO'$ 上（$AE=\frac{\sqrt3}2<AO'=\frac{3\sqrt3}2$），属于 $\triangle ABD$ 内部 ✓；" "\n"
        r"⑥ 检验：**算完球心后把四个顶点全验一遍等距**（四个 $\frac{21}4$ ✓）。"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-297'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-297-E1',
}

T297_V1 = {
    'type': '填空',
    'stem_text': (
        r"如图，二面角 $A-BD-C$ 的平面角的大小为 $120^\circ$，$\angle BDA=120^\circ$，$\angle BDC=150^\circ$，"
        r"$AD=BD=2$，$CD=\sqrt3$，则四面体 $ABCD$ 的外接球表面积为 ____。 "
    ),
    'opts': [],
    'answer': r"$116\pi$",
    'analysis': (
        r"两外接圆半径 $r_1=2$、$r_2=\sqrt{13}$，两外心到 $BD$ 中点距离 $\sqrt3$、$2\sqrt3$。"
        r"$O_1O_2^2=21$，解出 $\lvert OO_2\rvert=4$ ⟹ $R^2=13+16=29$ ⟹ $S=116\pi$。"
    ),
    'solution': (
        r"在 $\triangle BDA$ 中，$\angle BDA=120^\circ$，$AD=BD=2$：" "\n"
        r"$AB=\sqrt{4+4-2\cdot2\cdot2\cdot\left(-\tfrac12\right)}=\sqrt{12}=2\sqrt3$．" "\n"
        r"设其外接圆半径 $r_1$，则 $2r_1=\dfrac{AB}{\sin\angle BDA}=\dfrac{2\sqrt3}{\sqrt3/2}=4$，故 $r_1=2$．" "\n"
        r"在 $\triangle BDC$ 中，$\angle BDC=150^\circ$，$BD=2$、$CD=\sqrt3$：" "\n"
        r"$BC=\sqrt{3+4-2\cdot\sqrt3\cdot2\cdot\left(-\tfrac{\sqrt3}2\right)}=\sqrt{3+4+6}=\sqrt{13}$，" "\n"
        r"$2r_2=\dfrac{BC}{\sin150^\circ}=\dfrac{\sqrt{13}}{1/2}=2\sqrt{13}$，故 $r_2=\sqrt{13}$．" "\n"
        r"**外心到 $BD$ 中点的距离**：设 $G$ 为 $BD$ 中点，$O_1,O_2$ 为两外心，" "\n"
        r"$GO_1=\sqrt{r_1^{2}-1}=\sqrt3$，$GO_2=\sqrt{r_2^{2}-1}=\sqrt{12}=2\sqrt3$，" "\n"
        r"且 $\angle O_1GO_2$ 即二面角的平面角 $=120^\circ$．" "\n"
        r"**坐标法**：以 $G$ 为原点，$BD$ 为 $x$ 轴。取 $\triangle BDC$ 所在平面为 $xy$ 平面，" "\n"
        r"则 $O_2=(0,2\sqrt3,0)$；$\triangle BDA$ 的方向与 $y$ 轴负向夹 $60^\circ$（因二面角 $120^\circ$）：" "\n"
        r"$O_1=\sqrt3\left(0,\cos120^\circ,\sin120^\circ\right)=\left(0,-\dfrac{\sqrt3}2,\dfrac32\right)$．" "\n"
        r"球心 $O$ 满足 $OO_1\perp$ 平面 $BDA$、$OO_2\perp$ 平面 $BDC$。后者法向为 $(0,0,1)$：" "\n"
        r"$O=O_2+s(0,0,1)=(0,2\sqrt3,s)$．" "\n"
        r"$OO_1=\left(0,2\sqrt3+\dfrac{\sqrt3}2,s-\dfrac32\right)$ 应与平面 $BDA$ 的法向平行。" "\n"
        r"平面 $BDA$ 含 $x$ 轴与方向 $\left(0,-\tfrac12,\tfrac{\sqrt3}2\right)$，法向 $n=(0,\tfrac{\sqrt3}2,\tfrac12)$。" "\n"
        r"由 $OO_1\parallel n$：$\dfrac{2\sqrt3+\sqrt3/2}{\sqrt3/2}=\dfrac{s-3/2}{1/2}\Rightarrow\dfrac{5\sqrt3/2}{\sqrt3/2}=5=\dfrac{s-3/2}{1/2}$，" "\n"
        r"得 $s-\dfrac32=\dfrac52$，$s=4$．" "\n"
        r"$R^{2}=\lvert OO_2\rvert^{2}+r_2^{2}=16+13=29$（验：$\lvert OO_1\rvert=\sqrt{25}=5$，$r_1^{2}+25=4+25=29$ ✓），" "\n"
        r"$S=4\pi R^{2}=116\pi$。故答案为 $116\pi$。"
    ),
    'review': (
        r"★ 题干、答案完整，详解由我独立推导（原书 p264 详解关键量全部吻合）。" "\n"
        r"原书答案 $116\pi$ ✓，详解：" "\n"
        r"「在 $\triangle BDA$ 中，$\angle BDA=120^\circ$，$AD=BD=2$，所以 $AB=\sqrt{AD^{2}+BD^{2}-2AD\cdot BD\cos\angle BDA}=2\sqrt3$；" "\n"
        r"设 $\triangle BDA$ 的外接圆的半径为 $r_1$，则 $2r_1=\frac{AB}{\sin\angle BDA}=4$，所以 $r_1=2$。" "\n"
        r"在 $\triangle BDC$ 中，$\angle BDC=150^\circ$，$BD=2$，$CD=\sqrt3$，所以 $BC=\sqrt{CD^{2}+BD^{2}-2CD\cdot BD\cos\angle BDC}=\sqrt{13}$；" "\n"
        r"设 $\triangle BDC$ 的外接圆的半径为 $r_2$，则 $2r_2=\frac{BC}{\sin\angle BDC}=2\sqrt{13}$，所以 $r_2=\sqrt{13}$。" "\n"
        r"又作 $OG_1\perp BD$，$OG_2\perp BD$，所以 $\angle O_1GO_2$ 为二面角 $A-BD-C$ 的平面角，即 $\angle O_1GO_2=120^\circ$；" "\n"
        r"所以 $O_1G=\sqrt{r_1^{2}-(\frac{BD}2)^{2}}=\sqrt3$，$O_2G=\sqrt{r_2^{2}-(\frac{BD}2)^{2}}=2\sqrt3$，" "\n"
        r"所以 $O_1O_2=\sqrt{(\sqrt3)^{2}+(2\sqrt3)^{2}-2\times\sqrt3\times2\sqrt3\cos120^\circ}=\sqrt{21}$」" "\n"
        r"—— **$AB=2\sqrt3$、$r_1=2$、$BC=\sqrt{13}$、$r_2=\sqrt{13}$、$O_1G=\sqrt3$、$O_2G=2\sqrt3$、$O_1O_2^2=21$ 全部与我的推导一致** ✓✓✓" "\n"
        r"（⚠ 原书详解到此截断，`OO'=\sqrt{21}` 的记号与 $O_1O_2$ 混用，**但后面的 $R^2$ 未给出**，由我补全）" "\n"
        r"**独立验算（坐标法，完全独立）**：" "\n"
        r"① **$AB=2\sqrt3$**：$4+4-2\cdot2\cdot2\cdot(-0.5)=8+4=12$ ⟹ $\sqrt{12}=2\sqrt3$ ✓✓✓" "\n"
        r"② **$2r_1=4$**：$\frac{2\sqrt3}{\sin120^\circ}=\frac{2\sqrt3}{\sqrt3/2}=4$ ✓✓✓ ⟹ $r_1=2$ ✓✓✓" "\n"
        r"③ **$BC=\sqrt{13}$**：$3+4-2\cdot\sqrt3\cdot2\cdot(-\frac{\sqrt3}2)=3+4+6=13$ ✓✓✓" "\n"
        r"④ **$2r_2=2\sqrt{13}$**：$\frac{\sqrt{13}}{\sin150^\circ}=\frac{\sqrt{13}}{0.5}=2\sqrt{13}$ ✓✓✓ ⟹ $r_2=\sqrt{13}$ ✓✓✓" "\n"
        r"⑤ **$O_1G=\sqrt3$、$O_2G=2\sqrt3$**：$\sqrt{4-1}=\sqrt3$ ✓；$\sqrt{13-1}=\sqrt{12}=2\sqrt3$ ✓ ✓✓✓" "\n"
        r"（$G$ 是 $BD$ 中点，$GD=1$）" "\n"
        r"⑥ **$O_1O_2^2=21$**：$3+12-2\cdot\sqrt3\cdot2\sqrt3\cdot(-0.5)=15+6=21$ ✓✓✓ **与详解一致**" "\n"
        r"⑦ **坐标法求 $s=4$**：$O_2=(0,2\sqrt3,0)$，$O_1=(0,-\frac{\sqrt3}2,\frac32)$。" "\n"
        r"$OO_1=(0,2\sqrt3+\frac{\sqrt3}2,s-\frac32)=(0,\frac{5\sqrt3}2,s-\frac32)$，应与 $n=(0,\frac{\sqrt3}2,\frac12)$ 平行。" "\n"
        r"$\frac{5\sqrt3/2}{\sqrt3/2}=5$ ⟹ $s-\frac32=5\cdot\frac12=\frac52$ ⟹ $s=4$ ✓✓✓" "\n"
        r"⑧ **$R^2=29$**：$|OO_2|=|s|=4$，$R^2=16+13=29$ ✓✓✓" "\n"
        r"验 $|OO_1|=\sqrt{(\frac{5\sqrt3}2)^2+(\frac52)^2}=\sqrt{\frac{75}4+\frac{25}4}=\sqrt{25}=5$，$r_1^2+25=4+25=29$ ✓✓✓ **两路一致**" "\n"
        r"⑨ **$S=4\pi\cdot29=116\pi$** ✓✓✓" "\n"
        r"⑩ **数值检验**：$r_1=2$、$r_2=\sqrt{13}=3.6056$、$|OO_2|=4$、$|OO_1|=5$。" "\n"
        r"$R=\sqrt{29}=5.3852$，$S=4\pi(29)=116\pi=364.42$ ✓✓✓" "\n"
        r"**答案 $116\pi$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（「外心垂线相交型」万能模板）**：" "\n"
        r"① ⭐⭐ **通用于任意两个面夹角已知的四面体**：分别求两面的外接圆半径 $r_1,r_2$ 与外心，" "\n"
        r"过外心作面垂线，交点即球心 —— **本题的解法可直接迁移到所有同型题**；" "\n"
        r"② ⭐⭐ **$R^{2}=\lvert OO_i\rvert^{2}+r_i^{2}$ 对两个面都成立**，" "\n"
        r"**算出 $|OO_1|,|OO_2|$ 后两边必须对上**（本题 $4^2+13=5^2+4=29$ ✓），这是最好的自检；" "\n"
        r"③ ⭐ **外心到公共边中点的距离 $=\sqrt{r^{2}-(\frac{\text{边}}2)^{2}}$**，" "\n"
        r"两垂足与中点构成的角 **就是二面角**（因为两条垂线都垂直公共边）；" "\n"
        r"④ ⚠ **$CD=\sqrt3$ 的根号极易丢失**：若按 $CD=3$ 则 $BC^2=9+4+18=31$，" "\n"
        r"$r_2=\sqrt{31}$，$R^2$ 不是整数 —— **答案 $116\pi$ 要求 $BC=\sqrt{13}$**，反证可靠；" "\n"
        r"⑤ ⭐ **坐标法比「解三角形」更快**：把两外心写成平面内方向角的形式，" "\n"
        r"球心是「两法向直线的交点」，**列一次平行条件就解出**；" "\n"
        r"⑥ 检验：**用两个面各算一次 $R^2$**（$29$ 与 $29$ ✓）。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-297'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-297-V1',
}

T292_V2 = {
    'type': '选择',
    'stem_text': (
        r"在如图所示的直三棱柱 $ABC-A_{1}B_{1}C_{1}$ 中，$AA_{1}=4$，$AB\perp AC$，过点 $A_{1}$ 作平面 $\alpha$ 分别交棱 $AB,AC$ 于点 $D,E$，"
        r"且 $AF\perp DE$，$\angle AA_{1}F=60^\circ$，则截面 $\triangle A_{1}DE$ 面积的最小值为（　　）"
    ),
    'opts': [
        ('A', r"$16\sqrt3$"),
        ('B', r"$32\sqrt3$"),
        ('C', r"$36\sqrt3$"),
        ('D', r"$48\sqrt3$"),
    ],
    'answer': 'B',
    'analysis': (
        r"$\mathrm{Rt}\triangle FAA_1$ 中得 $A_1F=8$、$AF=4\sqrt3$。等面积法 $\frac1{x^2}+\frac1{y^2}=\frac1{48}$ ⟹ "
        r"$x^2y^2=48(x^2+y^2)$。$s=x^2+y^2\ge192$，$S=\frac12\cdot DE\cdot A_1F=4\sqrt s\ge32\sqrt3$。"
    ),
    'solution': (
        r"在 $\mathrm{Rt}\triangle FAA_{1}$ 中，$\angle AA_{1}F=60^\circ$、$AA_{1}=4$：" "\n"
        r"$A_{1}F=\dfrac{AA_{1}}{\cos60^\circ}=8$，$AF=AA_{1}\tan60^\circ=4\sqrt3$．" "\n"
        r"因 $AA_{1}\perp$ 底面，故 $AA_{1}\perp DE$；又 $AF\perp DE$，所以 $DE\perp$ 平面 $AA_{1}F$，得 $DE\perp A_{1}F$．" "\n"
        r"**设 $AD=x$、$AE=y$**。在 $\mathrm{Rt}\triangle ADE$ 中由等面积法：" "\n"
        r"$\dfrac12xy=\dfrac12\cdot DE\cdot AF\Rightarrow\dfrac1{x^{2}}+\dfrac1{y^{2}}=\dfrac1{AF^{2}}=\dfrac1{48}$，" "\n"
        r"即 $\dfrac{x^{2}+y^{2}}{x^{2}y^{2}}=\dfrac1{48}$，故 $x^{2}y^{2}=48\left(x^{2}+y^{2}\right)$．" "\n"
        r"**求 $DE$ 最小**：记 $s=x^{2}+y^{2}$、$p=xy$，则 $p^{2}=48s$，且 $s\ge2p=2\sqrt{48s}$，" "\n"
        r"即 $s^{2}\ge4\cdot48s=192s$，故 $s\ge192$，等号当 $x=y$ 时成立。" "\n"
        r"$S=\dfrac12\cdot DE\cdot A_{1}F=\dfrac12\sqrt{s}\cdot8=4\sqrt s\ge4\sqrt{192}=4\cdot8\sqrt3=32\sqrt3$。故选 B。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p258 详解：" "\n"
        r"「在 $\mathrm{Rt}\triangle FAA_1$ 中，由 $\angle AA_1F=60^\circ$，$AA_1=4$，可得 $A_1F=8$，$AF=4\sqrt3$；" "\n"
        r"设 $AD=x$，$AE=y$，在 $\mathrm{Rt}\triangle ADE$ 中，$AF\perp DE$，由等面积法可知 $\frac1{x^{2}}+\frac1{y^{2}}=\frac1{48}$，" "\n"
        r"因为 $AA_1\perp DE$…」" "\n"
        r"—— **$A_1F=8$、$AF=4\sqrt3$、$\frac1{x^2}+\frac1{y^2}=\frac1{48}$ 全部与我的推导一致** ✓✓✓" "\n"
        r"（详解后半段破碎，最小值由我补全）" "\n"
        r"**独立验算**：" "\n"
        r"① **$A_1F=8$**：$\cos60^\circ=\frac{AA_1}{A_1F}=\frac4{A_1F}$ ⟹ $A_1F=8$ ✓✓✓" "\n"
        r"（$\mathrm{Rt}\triangle$ 直角在 $A$：$AA_1\perp AF$，因 $AF$ 在底面内）" "\n"
        r"② **$AF=4\sqrt3$**：$\tan60^\circ=\frac{AF}{AA_1}$ ⟹ $AF=4\sqrt3=6.9282$ ✓✓✓" "\n"
        r"③ **等面积法**：$\frac12xy=\frac12\cdot DE\cdot AF$，$DE=\sqrt{x^2+y^2}$ ⟹ $\frac{xy}{\sqrt{x^2+y^2}}=AF=4\sqrt3$" "\n"
        r"⟹ $\frac{x^2y^2}{x^2+y^2}=48$ ⟹ $\frac1{x^2}+\frac1{y^2}=\frac1{48}$ ✓✓✓" "\n"
        r"④ **$DE\perp A_1F$**：$AA_1\perp$ 底面 ⟹ $AA_1\perp DE$；又 $AF\perp DE$（已知）；" "\n"
        r"$AA_1\cap AF=A$ ⟹ $DE\perp$ 平面 $AA_1F$ ⟹ $DE\perp A_1F$ ✓✓✓" "\n"
        r"⑤ **$S=\frac12\cdot DE\cdot A_1F=4\cdot DE$** ✓✓✓" "\n"
        r"⑥ **$s\ge192$**：$s\ge2p$、$p=\sqrt{48s}$ ⟹ $s\ge2\sqrt{48s}$ ⟹ $s^2\ge192s$ ⟹ $s\ge192$ ✓✓✓" "\n"
        r"$DE_{min}=\sqrt{192}=13.8564=8\sqrt3$ ✓✓✓" "\n"
        r"$S_{min}=4\cdot8\sqrt3=32\sqrt3=55.426$ ✓✓✓" "\n"
        r"⑦ **等号条件** $x=y$：$x^2=y^2=\frac s2=96$，$x=y=\sqrt{96}=4\sqrt6=9.7980$。" "\n"
        r"验 $\frac1{96}+\frac1{96}=\frac2{96}=\frac1{48}$ ✓✓✓" "\n"
        r"验 $DE=\sqrt{96+96}=\sqrt{192}$ ✓✓✓" "\n"
        r"⑧ **选项排除**：由 $S=4\sqrt s$ ⟹ $s=(\frac S4)^2$。" "\n"
        r"- A $16\sqrt3$ ⟹ $s=\frac{768}{16}=48<192$ ✗" "\n"
        r"- B $32\sqrt3$ ⟹ $s=\frac{3072}{16}=192$ ✓✓✓ **恰为下界**" "\n"
        r"- C $36\sqrt3$ ⟹ $s=\frac{3888}{16}=243>192$（可取但不是最小）" "\n"
        r"- D $48\sqrt3$ ⟹ $s=\frac{6912}{16}=432>192$" "\n"
        r"**答案 B 正确** ✓" "\n"
        r"**⭐⭐ 通法（截面面积最值 · 等面积法 + 基本不等式）**：" "\n"
        r"① ⭐⭐ **$\frac12xy=\frac12\cdot DE\cdot AF$ ⟹ $\frac1{x^{2}}+\frac1{y^{2}}=\frac1{AF^{2}}$** —— " "\n"
        r"直角三角形的斜边高公式，把 $x,y$ 与已知量 $AF$ 直接绑定，**比设角参数快得多**；" "\n"
        r"② ⭐⭐ **$DE\perp$ 平面 $AA_1F$** 是面积公式 $S=\frac12\cdot DE\cdot A_1F$ 的前提 —— " "\n"
        r"两次垂直（$AA_1\perp DE$ 来自线面垂直、$AF\perp DE$ 来自已知）**凑出线面垂直**；" "\n"
        r"③ ⭐ **$s\ge2p$ 与 $p^2=48s$ 联立消元**：$s^2\ge192s$ ⟹ $s\ge192$，" "\n"
        r"**这是处理「倒数和为定值」的标准动作**；" "\n"
        r"④ ⚠ **$\cos60^\circ=\frac{AA_1}{A_1F}$ 别写反**：$\angle AA_1F$ 在 $A_1$ 处，" "\n"
        r"邻边是 $AA_1$、斜边是 $A_1F$ —— 若写反得 $A_1F=2$，后面全错；" "\n"
        r"⑤ 检验：**由选项反查 $s=(\frac S4)^2$**，只有 B 给 $s=192$ 恰为下界 ✓（最快的验算）。"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-292'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-292-V2',
}

T292_V3 = {
    'type': '填空',
    'stem_text': (
        r"如图所示，在长方体 $ABCD-A_{1}B_{1}C_{1}D_{1}$ 中，$AB=3$，$AD=4$，$AA_{1}=5$，点 $E$ 是棱 $CC_{1}$ 上的一个动点，"
        r"若平面 $BED_{1}$ 交棱 $AA_{1}$ 于点 $F$，则四棱锥 $B_{1}-BED_{1}F$ 的体积为 ____，"
        r"截面四边形 $BED_{1}F$ 的周长的最小值为 ____。 "
    ),
    'opts': [],
    'answer': r"$20$；$2\sqrt{74}$",
    'analysis': (
        r"割补：$V=\frac13(30+30)=20$。由 $D_1F\parallel BE$ 得 $f=5-t$，"
        r"周长 $=2\left[\sqrt{16+t^{2}}+\sqrt{9+(5-t)^{2}}\right]$，反射法得最小 $2\sqrt{74}$。"
    ),
    'solution': (
        r"**体积**：四棱锥 $B_{1}-BED_{1}F$ 可拆成两个三棱锥 $B_{1}-BED_{1}$ 与 $B_{1}-BFD_{1}$。" "\n"
        r"换顶点：$V_{B_{1}-BED_{1}}=V_{D_{1}-BEB_{1}}=\dfrac13\cdot\dfrac12\cdot BB_{1}\cdot BC\cdot AB=\dfrac13\cdot\dfrac12\cdot5\cdot4\cdot3=10$；" "\n"
        r"同理 $V_{B_{1}-BFD_{1}}=V_{D_{1}-BFB_{1}}=\dfrac13\cdot\dfrac12\cdot BB_{1}\cdot A_{1}D_{1}\cdot AB=10$。" "\n"
        r"故 $V=20$（与 $E$ 的位置无关）。" "\n"
        r"**周长最小**：建系 $A(0,0,0)$、$B(3,0,0)$、$C(3,4,0)$、$D(0,4,0)$、$A_{1}(0,0,5)$、$B_{1}(3,0,5)$、$D_{1}(0,4,5)$。" "\n"
        r"设 $E=(3,4,t)$（$t\in[0,5]$）、$F=(0,0,f)$。由 $B,E,D_{1},F$ 共面：" "\n"
        r"$\vec{BF}=(-3,0,f)=\alpha(0,4,t)+\beta(-3,4,5)$，比较 $x$ 得 $\beta=1$、比较 $y$ 得 $\alpha=-1$，故 $f=5-t$。" "\n"
        r"于是 $\lvert BE\rvert=\sqrt{4^{2}+t^{2}}=\lvert D_{1}F\rvert$，$\lvert FB\rvert=\sqrt{3^{2}+(5-t)^{2}}=\lvert ED_{1}\rvert$，" "\n"
        r"周长 $L=2\left[\sqrt{16+t^{2}}+\sqrt{9+(5-t)^{2}}\right]$。" "\n"
        r"**反射法**：视 $t$ 为 $x$ 轴上动点 $P(t,0)$，则两项分别是 $P$ 到 $(0,4)$ 与到 $(5,-3)$ 的距离，" "\n"
        r"和的最小值等于 $(0,4)$ 到 $(5,-3)$ 关于 $x$ 轴的对称点 $(5,3)$ 的距离：" "\n"
        r"$\sqrt{(5-0)^{2}+(3-4)^{2}}=\sqrt{25+1}=\sqrt{26}$…" "\n"
        r"（更正：两项为 $\sqrt{t^{2}+4^{2}}$ 与 $\sqrt{(5-t)^{2}+3^{2}}$，即 $P(t,0)$ 到 $(0,-4)$ 与 $(5,3)$ 的距离，" "\n"
        r"最小值为 $(0,-4)$ 到 $(5,3)$ 的距离 $=\sqrt{25+49}=\sqrt{74}$。）" "\n"
        r"故 $L_{\min}=2\sqrt{74}$，此时 $t=\dfrac{20}7$。答案为 $20$，$2\sqrt{74}$。"
    ),
    'review': (
        r"★ 题干、答案完整；体积部分原书详解完整，周长最小值由我用反射法独立推导。" "\n"
        r"原书 p258 详解：「由题意可得 $D_1F\parallel BE$，利用切割法可得" "\n"
        r"$V_{B_1-BED_1F}=V_{B_1-BED_1}+V_{B_1-BFD_1}=V_{D_1-BEB_1}+V_{D_1-BFB_1}=\frac13\times\frac12\cdot BB_1\cdot BC\cdot AB+\frac12BB_1\cdot D_1A_1\cdot AB=\frac13\times\ldots$」" "\n"
        r"—— **$D_1F\parallel BE$、割补法、两个 $\frac12\cdot5\cdot4\cdot3$ 与我的推导一致** ✓✓✓，答案 $20$ ✓" "\n"
        r"答案 `20; 2 74` ⟹ $20$ 与 $2\sqrt{74}$ ✓" "\n"
        r"**独立验算（坐标法 + 反射法）**：" "\n"
        r"① **$V_{D_1-BEB_1}=10$**：$\triangle BEB_1$ 在平面 $BCC_1B_1$ 内，$BB_1=5$、$BC=4$，面积 $\frac12\cdot5\cdot4=10$；" "\n"
        r"$D_1$ 到该平面的距离 $=AB=3$ ⟹ $V=\frac13\cdot10\cdot3=10$ ✓✓✓" "\n"
        r"② **同理第二个也是 $10$** ⟹ $V=20$ ✓✓✓" "\n"
        r"（平面 $ADD_1A_1$ 与平面 $BCC_1B_1$ 平行，距离 $AB=3$ ✓）" "\n"
        r"③ **$f=5-t$**：$\vec{BE}=(0,4,t)$、$\vec{BD_1}=(-3,4,5)$、$\vec{BF}=(-3,0,f)$。" "\n"
        r"$\vec{BF}=\alpha\vec{BE}+\beta\vec{BD_1}$：$x$: $-3=-3\beta$ ⟹ $\beta=1$；$y$: $0=4\alpha+4$ ⟹ $\alpha=-1$；" "\n"
        r"$z$: $f=-t+5$ ✓✓✓" "\n"
        r"④ **$|BE|=\sqrt{16+t^2}$、$|D_1F|=\sqrt{16+t^2}$**：$D_1F$ 差向量 $(0,-4,5-t-5)=(0,-4,-t)$ ⟹ $\sqrt{16+t^2}$ ✓✓✓" "\n"
        r"⑤ **$|FB|=\sqrt{9+(5-t)^2}$、$|ED_1|=\sqrt{9+(5-t)^2}$**：$FB$ 差向量 $(3,0,t-5)$ ✓；$ED_1$ 差向量 $(-3,0,5-t)$ ✓ ✓✓✓" "\n"
        r"⑥ **$L=2[\sqrt{16+t^2}+\sqrt{9+(5-t)^2}]$** ✓✓✓" "\n"
        r"⑦ **反射法**：$\sqrt{t^2+16}$ 是 $P(t,0)$ 到 $Q_1(0,4)$ 的距离（$y$ 差 $4$）✓；" "\n"
        r"$\sqrt{(5-t)^2+9}$ 是 $P(t,0)$ 到 $Q_2(5,3)$ 的距离（$x$ 差 $5-t$、$y$ 差 $3$）✓" "\n"
        r"两定点在 $x$ 轴同侧（$y=4$ 与 $y=3$ 都 $>0$），需反射一个：取 $Q_2'(5,-3)$，" "\n"
        r"$|Q_1Q_2'|=\sqrt{25+49}=\sqrt{74}$ ✓✓✓" "\n"
        r"$L_{min}=2\sqrt{74}=17.2046$ ✓✓✓" "\n"
        r"⑧ **临界点**：$Q_1(0,4)$ 到 $Q_2'(5,-3)$ 的连线与 $x$ 轴交点：$y=4+\frac{-7}{5}t=0$ ⟹ $t=\frac{20}7=2.8571\in[0,5]$ ✓✓✓" "\n"
        r"验 $L(2.8571)=2[\sqrt{16+8.1633}+\sqrt{9+4.5918}]=2[\sqrt{24.1633}+\sqrt{13.5918}]=2[4.9156+3.6869]=2(8.6025)=17.205$ ✓✓✓" "\n"
        r"⑨ **边界比较**：$t=0$：$L=2[4+\sqrt{34}]=2[4+5.8310]=19.662>17.205$ ✓✓✓" "\n"
        r"$t=5$：$L=2[\sqrt{41}+3]=2[6.4031+3]=18.806>17.205$ ✓✓✓ **确为最小**" "\n"
        r"**答案 $20$、$2\sqrt{74}$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（截面的体积与周长最值）**：" "\n"
        r"① ⭐⭐ **体积用割补 + 换顶点**：把四棱锥拆成两个三棱锥，**每个都以「平行平面间的距离」为高**，" "\n"
        r"本题两个都是 $\frac13\cdot\frac12\cdot5\cdot4\cdot3=10$ —— **体积与动点位置无关**，这是命题人设计好的；" "\n"
        r"② ⭐⭐ **共面条件 ⟹ 定比分点**：$F$ 由平面 $BED_1$ 唯一确定，用 $\vec{BF}=\alpha\vec{BE}+\beta\vec{BD_1}$ 解出 $f=5-t$，" "\n"
        r"**比用平面方程快**；" "\n"
        r"③ ⭐ **周长是对称的两对**：$|BE|=|D_1F|$、$|FB|=|ED_1|$，" "\n"
        r"所以 $L=2(\cdots)$ —— **发现这个对称性能省一半计算**；" "\n"
        r"④ ⭐⭐ **$\sqrt{t^2+a^2}+\sqrt{(c-t)^2+b^2}$ 的最小值用反射法**：" "\n"
        r"视为 $x$ 轴上动点到两定点的距离和，最小 $=\sqrt{c^2+(a+b)^2}$ —— " "\n"
        r"**比求导快得多**（本题 $\sqrt{25+49}=\sqrt{74}$）；" "\n"
        r"⑤ ⚠ **两定点在同侧时必须反射**，否则算出的 $\sqrt{25+1}=\sqrt{26}$ 是错的 —— " "\n"
        r"**我第一遍就犯了这个错**，$y=4$ 与 $y=3$ 都在 $x$ 轴上方；" "\n"
        r"⑥ 检验：**反射法要检查交点 $t$ 是否在区间内**（$t=\frac{20}7\in[0,5]$ ✓），并**与两端点比较**（$19.662$、$18.806$ 都更大 ✓）。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-292'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-292-V3',
}

T302_E1 = {
    'type': '填空',
    'stem_text': (
        r"已知球 $O$ 是圆锥 $PO_{1}$ 的外接球，圆锥 $PO_{1}$ 的母线长是底面半径的 $3$ 倍，"
        r"且球 $O$ 的表面积为 $\dfrac{81\pi}8$，则圆锥 $PO_{1}$ 的侧面积为 ____。 "
    ),
    'opts': [],
    'answer': r"$3\pi$",
    'analysis': (
        r"设底面半径 $r$，则 $PB=3r$、$PO_1=2\sqrt2r$。$R^2=\frac{81}{32}$，"
        r"由 $R^2=(PO_1-R)^2+r^2$ 得 $9r^2=4\sqrt2rR$ ⟹ $r=1$，侧面积 $=\pi r\cdot PB=3\pi$。"
    ),
    'solution': (
        r"设底面半径 $O_{1}B=r$，球半径 $R$。由 $4\pi R^{2}=\dfrac{81\pi}8$ 得 $R^{2}=\dfrac{81}{32}$，$R=\dfrac{9\sqrt2}8$。" "\n"
        r"母线 $PB=3r$，故圆锥高 $PO_{1}=\sqrt{PB^{2}-r^{2}}=\sqrt{9r^{2}-r^{2}}=2\sqrt2r$．" "\n"
        r"球心 $O$ 在高 $PO_{1}$ 上，在 $\mathrm{Rt}\triangle OO_{1}B$ 中：" "\n"
        r"$OB^{2}=OO_{1}^{2}+O_{1}B^{2}\Rightarrow R^{2}=(PO_{1}-R)^{2}+r^{2}=\left(2\sqrt2r-R\right)^{2}+r^{2}$，" "\n"
        r"展开：$R^{2}=8r^{2}-4\sqrt2rR+R^{2}+r^{2}$，即 $9r^{2}=4\sqrt2rR$，" "\n"
        r"因 $r>0$，得 $r=\dfrac{4\sqrt2R}9=\dfrac{4\sqrt2}9\cdot\dfrac{9\sqrt2}8=1$．" "\n"
        r"故 $PB=3$，侧面积 $S=\pi r\cdot PB=\pi\cdot1\cdot3=3\pi$。故答案为 $3\pi$。"
    ),
    'review': (
        r"★ 题干、答案完整 ✓。原书 p270 详解：" "\n"
        r"「设 $O_1B=r$，球 $O$ 的半径为 $R$，则 $PB=3r$，球 $O$ 的表面积为 $4\pi R^{2}=\frac{81\pi}8$，得 $R^{2}=\frac{81}{32}$，" "\n"
        r"$PO_1=\sqrt{PB^{2}-r^{2}}=2\sqrt2r$，在 $\mathrm{Rt}\triangle OO_1B$ 中，$R^{2}=(PO_1-R)^{2}+r^{2}$，即 $R^{2}=(2\sqrt2r-R)^{2}+r^{2}$，解得 $r=\ldots$。" "\n"
        r"故圆锥 $PO_1$ 的侧面积为 $\pi r\cdot PB=3\pi$」" "\n"
        r"—— **$R^2=\frac{81}{32}$、$PO_1=2\sqrt2r$、$(2\sqrt2r-R)^2+r^2$、侧面积 $=\pi r\cdot PB=3\pi$ 全部与我的推导一致** ✓✓✓" "\n"
        r"（⚠ 详解中「解得 $r=$」后的数值破碎，由我反解出 $r=1$）" "\n"
        r"**独立验算**：" "\n"
        r"① **$R^2=\frac{81}{32}$**：$4\pi R^2=\frac{81\pi}8$ ⟹ $R^2=\frac{81}{32}=2.53125$ ✓✓✓ ⟹ $R=\frac{9}{4\sqrt2}=\frac{9\sqrt2}8=1.5909$ ✓✓✓" "\n"
        r"② **$PO_1=2\sqrt2r$**：$\sqrt{9r^2-r^2}=\sqrt{8r^2}=2\sqrt2r$ ✓✓✓" "\n"
        r"③ **$R^2=(2\sqrt2r-R)^2+r^2$**：球心在高线上，$OO_1=|PO_1-R|$，$\mathrm{Rt}\triangle OO_1B$ ⟹ $R^2=OO_1^2+r^2$ ✓✓✓" "\n"
        r"④ **$9r^2=4\sqrt2rR$**：$R^2=8r^2-4\sqrt2rR+R^2+r^2$ ⟹ $0=9r^2-4\sqrt2rR$ ✓✓✓" "\n"
        r"⑤ **$r=1$**：$r=\frac{4\sqrt2R}9=\frac{4\sqrt2}9\cdot\frac{9\sqrt2}8=\frac{4\cdot2\cdot9}{9\cdot8}=\frac{72}{72}=1$ ✓✓✓" "\n"
        r"⑥ **验**：$r=1$ ⟹ $PO_1=2\sqrt2=2.8284$，$OO_1=|2.8284-1.5909|=1.2375$。" "\n"
        r"$R^2=1.2375^2+1=1.5314+1=2.5314\approx\frac{81}{32}=2.53125$ ✓✓✓" "\n"
        r"⑦ **侧面积** $=\pi r\cdot PB=\pi\cdot1\cdot3=3\pi=9.4248$ ✓✓✓" "\n"
        r"⑧ **数值检验**：$R=\frac{9\sqrt2}8$，$4\sqrt2R=4\sqrt2\cdot\frac{9\sqrt2}8=\frac{4\cdot9\cdot2}{8}=9$，$r=\frac99=1$ ✓✓✓" "\n"
        r"**答案 $3\pi$ 正确** ✓" "\n"
        r"**⭐⭐ 通法（圆锥外接球 ⟹ 轴截面）**：" "\n"
        r"① ⭐⭐ **圆锥外接球 ⟺ 轴截面等腰三角形的外接圆** —— " "\n"
        r"一切计算压到平面内：$R^{2}=(h-R)^{2}+r^{2}$，其中 $h$ 是圆锥高、$r$ 是底面半径；" "\n"
        r"② ⭐ **展开后 $R^2$ 会抵消**：$R^{2}=h^{2}-2hR+R^{2}+r^{2}$ ⟹ $2hR=h^{2}+r^{2}$，" "\n"
        r"**即 $R=\frac{h^{2}+r^{2}}{2h}$** —— 这是圆锥外接球半径的通用公式（$h^2+r^2=$ 母线 $^2$）；" "\n"
        r"③ ⭐ **侧面积 $=\pi r l$**（$l$ 为母线），**别用成 $\pi r(r+l)$**（那是全面积）；" "\n"
        r"④ ⚠ **本题的 $r$ 出现在方程两边**：$9r^{2}=4\sqrt2rR$ 要" "\n"
        r"**两边同除以 $r$（$r>0$）** 才得到 $r=\frac{4\sqrt2R}9$ —— 若漏掉会得 $r=0$；" "\n"
        r"⑤ 检验：**把 $r=1$ 代回验 $R^2$**（$2.5314\approx\frac{81}{32}$ ✓）。"
    ),
    'difficulty': 0.82,
    'topics': ['M-T-302'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-302-E1',
}

T302_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知圆柱的上底面圆周经过正三棱锥 $P-ABC$ 的三条侧棱的中点，下底面圆心为此三棱锥底面中心 $O$。"
        r"若三棱锥 $P-ABC$ 的高为该圆柱外接球半径的 $2$ 倍，则该三棱锥的外接球与圆柱外接球的半径之比为（　　）"
    ),
    'opts': [
        ('A', r"$7:4$"),
        ('B', r"$2:1$"),
        ('C', r"$3:1$"),
        ('D', r"$5:3$"),
    ],
    'answer': 'A',
    'analysis': (
        r"设底面边长 $2a$、高 $h$。圆柱高 $\frac h2$、底半径 $\frac{\sqrt3}3a$；$R^2=\frac{h^2}{16}+\frac{a^2}3$，$h=2R$ ⟹ $h=\frac{4a}3$、$R=\frac{2a}3$。"
        r"三棱锥 $r^2=(h-r)^2+\frac{4a^2}3$ ⟹ $r=\frac{7a}6$，$r:R=7:4$。"
    ),
    'solution': (
        r"设正三棱锥底面边长为 $2a$、高为 $h$。" "\n"
        r"**圆柱**：上底面过三条侧棱的中点，中点三角形边长为 $a$（原底面边长 $2a$ 的一半），" "\n"
        r"其外接圆半径即圆柱底面半径 $=\dfrac{a}{2\sin60^\circ}=\dfrac{\sqrt3}3a$；圆柱的高 $=\dfrac h2$。" "\n"
        r"故圆柱外接球半径 $R$ 满足 $R^{2}=\left(\dfrac h4\right)^{2}+\left(\dfrac{\sqrt3}3a\right)^{2}=\dfrac{h^{2}}{16}+\dfrac{a^{2}}3$。" "\n"
        r"由 $h=2R$：$\dfrac{h^{2}}4=\dfrac{h^{2}}{16}+\dfrac{a^{2}}3\Rightarrow\dfrac{3h^{2}}{16}=\dfrac{a^{2}}3\Rightarrow h^{2}=\dfrac{16a^{2}}9$，" "\n"
        r"故 $h=\dfrac{4a}3$，$R=\dfrac h2=\dfrac{2a}3$。" "\n"
        r"**三棱锥**：底面外接圆半径 $=\dfrac{2a}{2\sin60^\circ}=\dfrac{2\sqrt3}3a$。设外接球半径为 $r$，" "\n"
        r"球心到底面距离为 $\lvert h-r\rvert$，故" "\n"
        r"$r^{2}=(h-r)^{2}+\left(\dfrac{2\sqrt3}3a\right)^{2}=\left(\dfrac{4a}3-r\right)^{2}+\dfrac{4a^{2}}3$．" "\n"
        r"展开：$r^{2}=\dfrac{16a^{2}}9-\dfrac{8ar}3+r^{2}+\dfrac{4a^{2}}3$，即 $\dfrac{8ar}3=\dfrac{16a^{2}}9+\dfrac{12a^{2}}9=\dfrac{28a^{2}}9$，" "\n"
        r"$r=\dfrac{28a^{2}}9\cdot\dfrac3{8a}=\dfrac{7a}6$。" "\n"
        r"故 $r:R=\dfrac{7a}6:\dfrac{2a}3=\dfrac{7a}6:\dfrac{4a}6=7:4$。故选 A。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p270 详解：" "\n"
        r"「设正三棱锥 $P-ABC$ 的底面边长为 $2a$，高为 $h$，则圆柱的高为 $\frac h2$，底面圆半径为 $\frac{a}{2\sin\frac\pi3}=\frac{\sqrt3}3a$，" "\n"
        r"设圆柱的外接球半径为 $R$，则 $R=\sqrt{\frac{h^{2}}{16}+\frac{a^{2}}3}$。" "\n"
        r"∵ $h=2R=2\sqrt{\frac{h^{2}}{16}+\frac{a^{2}}3}$… 解得 $h=\frac{4a}3$，此时 $R=\frac{2a}3$。设正三棱锥 $P-ABC$ 的外接球的半径为 $r$，" "\n"
        r"则球心到底面距离为 $h-r$，$OA=\frac{2a}{2\sin\frac\pi3}=\frac{2\sqrt3}3a$，由勾股定理得 $r^{2}=(h-r)^{2}+\ldots$，解得 $r=\frac{7a}{6}$，故 $\frac rR=\ldots$」" "\n"
        r"—— **圆柱高 $\frac h2$、底半径 $\frac{\sqrt3}3a$、$R^2=\frac{h^2}{16}+\frac{a^2}3$、$h=\frac{4a}3$、$R=\frac{2a}3$、$r=\frac{7a}6$ 全部与我的推导一致** ✓✓✓" "\n"
        r"（详解末段破碎，比值 $7:4$ 由我补全）" "\n"
        r"**独立验算**：" "\n"
        r"① **中点三角形边长 $=a$**：侧棱中点连线平行于底边且为其一半 ⟹ 边长 $=\frac{2a}2=a$ ✓✓✓" "\n"
        r"② **$\frac{a}{2\sin60^\circ}=\frac{\sqrt3}3a$**：$\frac{a}{2\cdot\frac{\sqrt3}2}=\frac a{\sqrt3}=\frac{\sqrt3}3a$ ✓✓✓" "\n"
        r"③ **$R^2=(\frac h4)^2+(\frac{\sqrt3}3a)^2$**：圆柱外接球，$R^2=(\frac{\text{高}}2)^2+r_{底}^2=(\frac{h/2}2)^2+\frac{a^2}3$ ✓✓✓" "\n"
        r"④ **$h=\frac{4a}3$**：$\frac{h^2}4=\frac{h^2}{16}+\frac{a^2}3$ ⟹ $\frac{3h^2}{16}=\frac{a^2}3$ ⟹ $h^2=\frac{16a^2}{9}$ ⟹ $h=\frac{4a}3$ ✓✓✓" "\n"
        r"⑤ **$R=\frac{2a}3$** ✓✓✓（验：$R^2=\frac{16a^2/9}{16}+\frac{a^2}3=\frac{a^2}9+\frac{a^2}3=\frac{4a^2}9$ ⟹ $R=\frac{2a}3$ ✓）" "\n"
        r"⑥ **$r=\frac{7a}6$**：$\frac{8ar}3=\frac{16a^2}9+\frac{12a^2}9=\frac{28a^2}9$ ⟹ $r=\frac{28a^2}{9}\cdot\frac{3}{8a}=\frac{84a}{72}=\frac{7a}6$ ✓✓✓" "\n"
        r"验：$r^2=\frac{49a^2}{36}$；$(h-r)^2+\frac{4a^2}3=(\frac{4a}3-\frac{7a}6)^2+\frac{4a^2}3=(\frac{8a-7a}6)^2+\frac{4a^2}3=\frac{a^2}{36}+\frac{48a^2}{36}=\frac{49a^2}{36}$ ✓✓✓ **吻合**" "\n"
        r"⑦ **$r:R=\frac{7a}6:\frac{2a}3=\frac76:\frac46=7:4$** ✓✓✓" "\n"
        r"⑧ **选项排除**：$\frac rR=\frac{7/6}{2/3}=\frac{7}{6}\cdot\frac32=\frac{21}{12}=1.75$。" "\n"
        r"- A $7:4=1.75$ ✓✓✓" "\n"
        r"- B $2:1=2$、C $3:1=3$、D $5:3=1.6667$ 均不符" "\n"
        r"**答案 A 正确** ✓" "\n"
        r"**⭐⭐ 通法（两个外接球之比）**：" "\n"
        r"① ⭐⭐ **分别求两个 $R$，每个都用 $R^{2}=(\text{球心到截面距离})^{2}+r_{\text{截面外接圆}}^{2}$** —— " "\n"
        r"圆柱：$\left(\frac{\text{高}}2\right)^{2}+r_{\text{底}}^{2}$；正三棱锥：$\left(h-r\right)^{2}+r_{\text{底面外接圆}}^{2}$；" "\n"
        r"② ⭐⭐ **「侧棱中点」⟹ 相似比 $\frac12$**：中点三角形边长是底面的一半，" "\n"
        r"**外接圆半径也是一半**（$\frac{\sqrt3}3a$ 对 $\frac{2\sqrt3}3a$）—— 别重新算；" "\n"
        r"③ ⭐ **正三角形外接圆半径 $=\frac{\text{边长}}{\sqrt3}$**：边长 $a$ 得 $\frac{\sqrt3}3a$；边长 $2a$ 得 $\frac{2\sqrt3}3a$ ✓；" "\n"
        r"④ ⚠ **圆柱的高是 $\frac h2$ 不是 $h$**：因为上底面在侧棱中点处（高度是三棱锥高的一半）；" "\n"
        r"于是 $R^{2}=(\frac{h/2}{2})^{2}+r_{底}^{2}=(\frac h4)^{2}+r_{底}^{2}$ —— **两个 $\frac12$ 别只算一个**；" "\n"
        r"⑤ ⭐ **$r^{2}=(h-r)^{2}+r_{底}^{2}$ 展开后 $r^{2}$ 抵消**，直接解出 $r$ —— " "\n"
        r"这是求棱锥外接球半径的标准动作（与圆锥的 $R=\frac{h^{2}+r^{2}}{2h}$ 同理）；" "\n"
        r"⑥ 检验：**把 $r$ 代回原式验一次**（$\frac{49a^2}{36}$ 两边相等 ✓）。"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-302'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-302-V2',
}

QS = [T297_E1, T297_V1, T292_V2, T292_V3, T302_E1, T302_V2]
