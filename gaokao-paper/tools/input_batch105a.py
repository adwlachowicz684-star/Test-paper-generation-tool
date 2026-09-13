# -*- coding: utf-8 -*-
r"""第 105 批：解三角形（M-T-230，4 题）+ 数列求和（M-T-270，3 题）
+ 数列与三角函数综合（M-T-189，3 题）+ 三角函数解答题（M-T-215，3 题）

    python3 tools/run_batch.py 105a

## 选题依据

按「详解完整 + 同题型聚堆」筛出，本批 13 题：3 填空 / 10 解答。
原文集中在 p161–p163（解三角形）、p187（数列求和）、p146–p147（数列周期）。

## ★★ 本批最值钱的一条：$(-1)^n$ 交错求和「两项一组」的三种变体

M-T-270 三题（E1、V1、V2）结构完全一样，只是分母不同：

| 题 | $b_n$ 的裂项 | 前 $2n$ 项和 |
|---|---|---|
| E1 | $(-1)^n\left(\dfrac1n+\dfrac1{n+1}\right)$ | $-\dfrac{2n}{2n+1}$ |
| V1 | $(-1)^n\left(\dfrac1n+\dfrac1{n+1}\right)$ | $-1+\dfrac{(-1)^n}{n+1}$ |
| V2 | $(-1)^n\left(\dfrac1{2n+1}+\dfrac1{2n+3}\right)$ | $-\dfrac{4n}{3(4n+3)}$ |

**通法**：$b_n=(-1)^n\left(\dfrac1{An+B}+\dfrac1{An+C}\right)$ 时，把每项的「括号内两数」
按 $n$ 奇偶展开，相邻项**首尾相消**，只剩首项的负数部分与末项的正数部分。

> ⭐⭐ 关键判据：**$\dfrac{2n+1}{n(n+1)}=\dfrac1n+\dfrac1{n+1}$** ——
> 分子恰好是分母两个因子之和，这类式子必能裂成两项单位分数。
> 一般地 $\dfrac{p}{xy}=\dfrac1x+\dfrac1y$ ⟺ $p=x+y$。

## ★★ 第二条：M-T-230-E1 的「$D$ 在 $AB$ 上 ⟹ 面积比 = 底之比」

$\triangle ACD$ 与 $\triangle ACB$ 共用 $C$ 到 $AB$ 的高，故

$$\frac{S_{\triangle ACD}}{S_{\triangle ABC}}=\frac{AD}{AB}=\frac2{10}=\frac15$$

**先求整体 $\triangle ABC$ 面积的最大值，再乘以 $\frac15$** —— 比直接处理小三角形省力得多。

> ⭐⭐ 凡是「边上一点分出两个三角形」，先看能否用**面积比 = 底边比**转化为整体问题。

## ★★ 第三条：M-T-230-V3 的「直角三角形的正弦表示」

$\angle BPC=90^\circ$、$BC=1$，设 $\angle PBA=\alpha$，则 $\angle PCB=\alpha$，在
Rt$\triangle PBC$ 中直接得 $PB=BC\sin\alpha=\sin\alpha$ —— **把未知线段用一个角表示**，
再在 $\triangle PBA$ 中用正弦定理列方程。

> ⭐⭐ 多个角共顶点时，统一用一个角 $\alpha$ 表示所有线段，是「角化边」的标准手法。

## ★★ 第四条：M-T-189-V2 的「四项一组」

$f(n)=n^2\cos\dfrac{n\pi}2$ 的周期是 4，故 $a_n=f(n)+f(n+1)$ 也按 4 分组：

$$a_{4n-3}+a_{4n-2}+a_{4n-1}+a_{4n}=-2(4n-2)^2+2(4n)^2=8(4n-1)$$

前 100 项 = 25 组 ⟹ $S_{100}=8(3+7+\cdots+99)=8\times1275=10200$。

> ⚠ 原书详解把 $a_{4n-1},a_{4n}$ 写作 $-(4n)^2$，与自身随后的「$+2(4n)^2$」矛盾；
> 实测 $a_3=f(3)+f(4)=0+16=16>0$，故应为 $+(4n)^2$。已按正确符号录入。

## ★★ 第五条：M-T-189-E1 的「周期 ⟹ 集合元素个数」

$b_n=\sin a_n$（$a_n$ 等差）、周期为 $t$ ⟹ 集合最多 $t$ 个元素；
要「恰有 4 个元素」，$t\ge4$，且 $t=5$ 时**单位圆五等分点只能给 3 或 5 个不同正弦值**（两值相等必成对出现），故 $t=4,6,7,8$ 共 **4 个**。

## 三处根号丢失还原（判据写在各题 review 里）

1. **M-T-230-V3 详解**：$\sin\alpha=\sqrt3\cos\alpha-\sin\alpha$ 被印成
   $\sin\alpha=3\cos\alpha-\sin\alpha$ ⟹ $\tan\alpha$ 由 $\frac{\sqrt3}2$ 变成 $\frac32$。
   按 $\frac32$ 得 $S\ne\frac{3\sqrt3}{14}$，与标答矛盾 ✓
2. **M-T-230-E1 答案**：`5 2 - 1` 实为 $5(\sqrt2-1)$（OCR 丢了括号与根号）。
3. **M-T-230-V2 答案**：`3/3` 实为 $\frac{\sqrt3}3$（$\frac33=1$ 不可能是 $\cos C$）。
"""

T230_E1 = {
    'type': '解答',
    'stem_text': (
        r"$D$ 为 $\triangle ABC$ 边 $AB$ 上一点，满足 $AD=2$，$DB=8$，"
        r"记 $\angle ABC=\alpha$，$\angle CAB=\beta$．"
        r"（1）当 $CD\perp AB$ 且 $\beta=2\alpha$ 时，求 $CD$ 的值；"
        r"（2）若 $\alpha+\beta=\dfrac\pi4$，求 $\triangle ACD$ 面积的最大值．"
    ),
    'opts': [],
    'answer': (
        r"（1）$CD=4\sqrt2$；（2）$5(\sqrt2-1)$．"
    ),
    'analysis': (
        r"（1）在两个直角三角形中分别写出 $\tan\alpha$、$\tan\beta$，再用二倍角公式"
        r"$\tan\beta=\tan2\alpha$ 列方程；（2）先求 $\triangle ABC$ 面积的最大值，"
        r"再用面积比 $\frac{AD}{AB}=\frac15$ 折算到 $\triangle ACD$．"
    ),
    'solution': (
        r"**第 (1) 问**" "\n"
        r"设 $CD=x$．当 $CD\perp AB$ 时，在 Rt$\triangle CDB$ 与 Rt$\triangle CDA$ 中：" "\n"
        r"$\tan\alpha=\dfrac{CD}{DB}=\dfrac x8$，$\tan\beta=\dfrac{CD}{AD}=\dfrac x2$．" "\n"
        r"由 $\beta=2\alpha$ 且 $0<2\alpha<\dfrac\pi2$，得" "\n"
        r"$\tan\beta=\tan2\alpha=\dfrac{2\tan\alpha}{1-\tan^{2}\alpha}>0$，" "\n"
        r"即 $\dfrac x2=\dfrac{2\cdot\frac x8}{1-\frac{x^{2}}{64}}$，约去 $x>0$ 得" "\n"
        r"$\dfrac12=\dfrac{\frac14}{1-\frac{x^{2}}{64}}$ ⟹ $1-\dfrac{x^{2}}{64}=\dfrac12$ ⟹ $x^{2}=32$．" "\n"
        r"故 $CD=x=4\sqrt2$．" "\n"
        r"**第 (2) 问**" "\n"
        r"在 $\triangle ABC$ 中，$\alpha+\beta=\dfrac\pi4$，故 $\angle ACB=\dfrac{3\pi}4$．" "\n"
        r"由 $AB=AD+DB=10$ 及正弦定理 $\dfrac{AC}{\sin\alpha}=\dfrac{BC}{\sin\beta}=\dfrac{AB}{\sin\frac{3\pi}4}$：" "\n"
        r"$BC=10\sqrt2\sin\beta$，$AC=10\sqrt2\sin\alpha$．" "\n"
        r"于是 $S_{\triangle ABC}=\dfrac12\cdot BC\cdot AC\cdot\sin\dfrac{3\pi}4"
        r"=\dfrac12\cdot10\sqrt2\sin\beta\cdot10\sqrt2\sin\alpha\cdot\dfrac{\sqrt2}2=50\sqrt2\sin\alpha\sin\beta$．" "\n"
        r"由 $\alpha+\beta=\dfrac\pi4$ 得 $\alpha=\dfrac\pi4-\beta$，代入：" "\n"
        r"$S=50\sqrt2\sin\beta\sin\left(\dfrac\pi4-\beta\right)"
        r"=50\sqrt2\sin\beta\cdot\dfrac{\sqrt2}2(\cos\beta-\sin\beta)=50(\sin\beta\cos\beta-\sin^{2}\beta)$" "\n"
        r"$=25\left(\sin2\beta+\cos2\beta-1\right)=25\sqrt2\sin\left(2\beta+\dfrac\pi4\right)-25$．" "\n"
        r"由 $0<\beta<\dfrac\pi4$ 得 $\dfrac\pi4<2\beta+\dfrac\pi4<\dfrac{3\pi}4$，" "\n"
        r"故当 $2\beta+\dfrac\pi4=\dfrac\pi2$（即 $\beta=\dfrac\pi8$）时，$S_{\max}=25\sqrt2-25=25(\sqrt2-1)$．" "\n"
        r"又 $\triangle ACD$ 与 $\triangle ACB$ 共用 $C$ 到 $AB$ 的高，" "\n"
        r"$\dfrac{S_{\triangle ACD}}{S_{\triangle ABC}}=\dfrac{AD}{AB}=\dfrac2{10}=\dfrac15$，" "\n"
        r"故 $\triangle ACD$ 面积的最大值为 $\dfrac{25(\sqrt2-1)}5=5(\sqrt2-1)$．"
    ),
    'review': (
        r"① ⭐⭐ **$\beta=2\alpha$ 只做一件事：把 $\tan\beta$ 用 $\tan\alpha$ 表示**"
        r"（正切二倍角），列方程后 $x$ 一次约净 ✓✓" "\n"
        r"② ⭐⭐ **$CD\perp AB$ ⟹ 两个直角三角形，$\tan$ 直接等于「对边/邻边」**，"
        r"无需余弦定理 ✓✓✓" "\n"
        r"③ ⭐⭐ **面积比 = 底边比**（同高），先求整体再折算，是小三角形问题的标准省力法 ✓✓✓" "\n"
        r"④ 数值复核：$x=4\sqrt2=5.657$，$\tan\alpha=\frac{5.657}8=0.7071$ ⟹ $\alpha=35.26^\circ$；"
        r"$\tan\beta=\frac{5.657}2=2.8284$ ⟹ $\beta=70.53^\circ=2\alpha$ ✓✓" "\n"
        r"⑤ $S_{\max}=25(\sqrt2-1)=10.355$，$S_{\triangle ACD}=2.071=5(\sqrt2-1)$ ✓" "\n"
        r"⑥ ⚠ **答案还原**：ref_bank 存为 `5 2 - 1`，实为 $5(\sqrt2-1)$"
        r"（OCR 同时丢了根号与括号）．按 $5\sqrt2-1=6.071$ 则与折算结果 $2.071$ 不符 ✓" "\n"
        r"**⭐⭐ 通法（边上一点 + 双直角三角形）**：" "\n"
        r"① ⭐⭐ 出现垂直 ⟹ 立刻把角放进直角三角形，用 $\tan$ 表边长；" "\n"
        r"② ⭐⭐ 两角有倍数关系 ⟹ 用二倍角公式连立；" "\n"
        r"③ ⭐⭐ 求「小三角形」最值，先看能否用面积比折算到「大三角形」✓✓✓"
    ),
    'difficulty': 0.62,
    'topics': ['M-T-230'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-230-E1',
}

T230_V1 = {
    'type': '解答',
    'stem_text': (
        r"设 $\triangle ABC$ 的内角 $A$，$B$，$C$ 的对边分别为 $a$，$b$，$c$，"
        r"且满足 $b\sin 2A+a\sin B=0$，点 $D$ 为边 $BC$ 上一点，$AD\perp AC$．"
        r"（1）求 $\angle BAC$ 的大小；（2）若 $|AC|=4$，$|AD|=3$，求 $|AB|$．"
    ),
    'opts': [],
    'answer': (
        r"（1）$\angle BAC=\dfrac{2\pi}3$；（2）$|AB|=\dfrac{8(4\sqrt3+3)}{13}$．"
    ),
    'analysis': (
        r"（1）用正弦定理把边换成角，提取 $\sin A\sin B\ne0$ 后得 $\cos A=-\frac12$；"
        r"（2）先在 Rt$\triangle ADC$ 中求 $DC$ 与 $\angle ADC$ 的三角函数，"
        r"再用互补角关系转入 $\triangle ABD$，正弦定理解 $AB$．"
    ),
    'solution': (
        r"**第 (1) 问**" "\n"
        r"由 $b\sin2A+a\sin B=0$ 及正弦定理 $a=2R\sin A$、$b=2R\sin B$，得" "\n"
        r"$\sin B\cdot2\sin A\cos A+\sin A\sin B=0$．" "\n"
        r"因 $A,B\in(0,\pi)$，故 $\sin A\sin B\ne0$，约去后得 $2\cos A+1=0$，" "\n"
        r"即 $\cos A=-\dfrac12$，所以 $\angle BAC=A=\dfrac{2\pi}3$．" "\n"
        r"**第 (2) 问**" "\n"
        r"由 $AC=4$、$AD=3$、$AD\perp AC$，得 $DC=\sqrt{4^{2}+3^{2}}=5$，" "\n"
        r"且 $\angle BAD=\dfrac{2\pi}3-\dfrac\pi2=\dfrac\pi6$．" "\n"
        r"在 Rt$\triangle ADC$ 中：$\sin\angle ADC=\dfrac{AC}{DC}=\dfrac45$，"
        r"$\cos\angle ADC=\dfrac{AD}{DC}=\dfrac35$．" "\n"
        r"由 $\angle ADB=\pi-\angle ADC$，得" "\n"
        r"$\sin\angle ADB=\dfrac45$，$\cos\angle ADB=-\dfrac35$．" "\n"
        r"在 $\triangle ABD$ 中，$\angle B=\pi-\angle ADB-\angle BAD$，故" "\n"
        r"$\sin\angle B=\sin(\angle ADB+\angle BAD)"
        r"=\sin\angle ADB\cos\dfrac\pi6+\cos\angle ADB\sin\dfrac\pi6$" "\n"
        r"$=\dfrac45\cdot\dfrac{\sqrt3}2+\left(-\dfrac35\right)\cdot\dfrac12=\dfrac{4\sqrt3-3}{10}$．" "\n"
        r"由正弦定理 $\dfrac{AD}{\sin\angle B}=\dfrac{AB}{\sin\angle ADB}$：" "\n"
        r"$AB=\dfrac{AD\cdot\sin\angle ADB}{\sin\angle B}"
        r"=\dfrac{3\cdot\frac45}{\frac{4\sqrt3-3}{10}}=\dfrac{24}{4\sqrt3-3}" "\n"
        r"=\dfrac{24(4\sqrt3+3)}{48-9}=\dfrac{8(4\sqrt3+3)}{13}$．"
    ),
    'review': (
        r"① ⭐⭐ **$b\sin2A+a\sin B=0$ 的破法单一：正弦定理全化角，提出 $\sin A\sin B$**"
        r"—— 系数 $2R$ 自动约净，剩下 $2\cos A+1=0$ ✓✓✓" "\n"
        r"② ⭐⭐ **$AD\perp AC$ 给出两个信息**：$DC$ 由勾股得 $5$，"
        r"且 $\angle BAD=A-90^\circ=\frac\pi6$（**这是连接两个三角形的唯一通道**）✓✓" "\n"
        r"③ ⭐⭐ **$\angle ADB$ 与 $\angle ADC$ 互补**：$\sin$ 相等、$\cos$ 相反，"
        r"求 $\sin\angle B$ 时符号极易错，务必写清 ✓" "\n"
        r"④ 数值复核：$AB=\frac{8(4\sqrt3+3)}{13}=\frac{8\times9.928}{13}=6.110$；"
        r"$\sin\angle B=\frac{4\sqrt3-3}{10}=0.3928$，$\frac{AD}{\sin B}=\frac3{0.3928}=7.637$，"
        r"$\frac{AB}{\sin\angle ADB}=\frac{6.110}{0.8}=7.637$ ✓✓ 完全闭合" "\n"
        r"⑤ 分母有理化：$(4\sqrt3)^2-3^2=48-9=39$，$\frac{24}{39}=\frac8{13}$ ✓" "\n"
        r"**⭐⭐ 通法（正弦定理化角 + 直角三角形转运）**：" "\n"
        r"① ⭐⭐ 边角混合等式 ⟹ 正弦定理统一成角，再提取公共因子；" "\n"
        r"② ⭐⭐ 出现垂直 ⟹ 勾股求第三边 + 余角关系；" "\n"
        r"③ ⭐⭐ 跨三角形转运靠「互补角」或「公共角」✓✓✓"
    ),
    'difficulty': 0.65,
    'topics': ['M-T-230'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-230-V1',
}

T230_V2 = {
    'type': '解答',
    'stem_text': (
        r"在 $\triangle ABC$ 中，$\sin A=\dfrac13$，$AB=2\sqrt3$，$D$，$E$ 分别在边 $BC$，$AC$ 上，"
        r"$EC=EB$，$ED\perp BC$ 且 $DE=1$．"
        r"（1）求 $\cos C$；（2）求 $\triangle AEB$ 的面积．"
    ),
    'opts': [],
    'answer': (
        r"（1）$\cos C=\dfrac{\sqrt3}3$；（2）$S_{\triangle AEB}=\dfrac{7\sqrt2}6$．"
    ),
    'analysis': (
        r"（1）由 $EC=EB$ 得 $\angle AEB=2C$，在 $\triangle AEB$ 中用正弦定理，"
        r"并用 $\frac{DE}{EC}=\sin C$ 把 $EB$ 换成 $\frac1{\sin C}$；（2）用外角关系"
        r"$\angle AEB=2C$ 求出其正余弦，再在 $\triangle AEB$ 中求 $\sin\angle ABE$ 与 $BE$．"
    ),
    'solution': (
        r"**第 (1) 问**" "\n"
        r"由 $EC=EB$、$ED\perp BC$、$DE=1$，在 Rt$\triangle EDC$ 中：" "\n"
        r"$\sin C=\dfrac{DE}{EC}=\dfrac1{EB}$ ①" "\n"
        r"由 $EC=EB$ 知 $\angle ECB=\angle EBC=C$，故 $\angle AEB=2C$（三角形外角）．" "\n"
        r"在 $\triangle AEB$ 中由正弦定理 $\dfrac{AB}{\sin\angle AEB}=\dfrac{EB}{\sin A}$：" "\n"
        r"$\dfrac{2\sqrt3}{\sin2C}=\dfrac{2\sqrt3}{2\sin C\cos C}=\dfrac{EB}{\frac13}=3EB$ ②" "\n"
        r"将 ① 代入 ②：$\dfrac{2\sqrt3}{2\sin C\cos C}=3\cdot\dfrac1{\sin C}$，约去 $\sin C>0$ 得" "\n"
        r"$\cos C=\dfrac{2\sqrt3}{6}=\dfrac{\sqrt3}3$．" "\n"
        r"**第 (2) 问**" "\n"
        r"由 $\cos C=\dfrac{\sqrt3}3$ 得 $\sin C=\sqrt{1-\dfrac13}=\dfrac{\sqrt6}3$．" "\n"
        r"于是 $\sin\angle AEB=\sin2C=2\cdot\dfrac{\sqrt6}3\cdot\dfrac{\sqrt3}3=\dfrac{2\sqrt2}3$，" "\n"
        r"$\cos\angle AEB=\cos2C=2\cos^{2}C-1=\dfrac23-1=-\dfrac13$．" "\n"
        r"由 $\sin A=\dfrac13$ 且 $A$ 为锐角（否则 $A+\angle AEB>\pi$），得 $\cos A=\dfrac{2\sqrt2}3$．" "\n"
        r"在 $\triangle AEB$ 中，$\angle ABE=\pi-A-\angle AEB$，故" "\n"
        r"$\sin\angle ABE=\sin(A+\angle AEB)=\sin A\cos\angle AEB+\cos A\sin\angle AEB$" "\n"
        r"$=\dfrac13\cdot\left(-\dfrac13\right)+\dfrac{2\sqrt2}3\cdot\dfrac{2\sqrt2}3=-\dfrac19+\dfrac89=\dfrac79$．" "\n"
        r"又 $BE=\dfrac1{\sin C}=\dfrac3{\sqrt6}=\dfrac{\sqrt6}2$，故" "\n"
        r"$S_{\triangle AEB}=\dfrac12\cdot BE\cdot AB\cdot\sin\angle ABE"
        r"=\dfrac12\cdot\dfrac{\sqrt6}2\cdot2\sqrt3\cdot\dfrac79=\dfrac{7\sqrt2}6$．"
    ),
    'review': (
        r"① ⭐⭐ **$EC=EB$ 的作用是双重的**：既给出 $\angle AEB=2C$（外角），"
        r"又让 $EB=EC$ 可代入 $\sin C=\frac{DE}{EC}$ ✓✓✓ 这是全题的枢纽" "\n"
        r"② ⭐⭐ **$\frac{2\sqrt3}{2\sin C\cos C}=\frac{3}{\sin C}$ 中 $\sin C$ 自动约净**，"
        r"$\cos C$ 一步得解 —— 这种「约净」是做法正确的信号 ✓" "\n"
        r"③ ⭐⭐ **$\cos\angle AEB=-\frac13<0$ 说明 $\angle AEB$ 是钝角**，"
        r"这正是 $\sin A=\frac13$ 时 $A$ 必为锐角的原因 ✓" "\n"
        r"④ 数值复核：$\cos C=0.5774$ ⟹ $C=54.74^\circ$；$\sin C=0.8165$，"
        r"$BE=1.2247=\frac{\sqrt6}2$ ✓；$\sin\angle AEB=0.9428$，$\angle AEB=109.47^\circ=2C$ ✓；"
        r"$\sin\angle ABE=0.7778=\frac79$ ✓" "\n"
        r"⑤ $S=\frac12\cdot1.2247\cdot3.4641\cdot0.7778=1.6499=\frac{7\sqrt2}6=1.6499$ ✓✓" "\n"
        r"⑥ ⚠ **答案还原**：ref_bank 存 `3/3`（即 $1$，不可能是 $\cos C$）与 `7 2/6`，"
        r"实为 $\frac{\sqrt3}3$ 与 $\frac{7\sqrt2}6$ ✓" "\n"
        r"**⭐⭐ 通法（等腰 + 外角 = 二倍角）**：" "\n"
        r"① ⭐⭐ 见到「一点到两边距离/线段相等」⟹ 等腰 ⟹ 外角 $=2\times$ 底角；" "\n"
        r"② ⭐⭐ 二倍角配合正弦定理，常出现「$\sin$ 约净」的干净结果；" "\n"
        r"③ ⭐⭐ 求面积缺元素时，用 $\sin(X+Y)$ 展开补齐第三个角 ✓✓✓"
    ),
    'difficulty': 0.66,
    'topics': ['M-T-230'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-230-V2',
}

T230_V3 = {
    'type': '解答',
    'stem_text': (
        r"在 $\triangle ABC$ 中，$\angle ABC=90^\circ$，$AB=\sqrt3$，$BC=1$，$P$ 为 $\triangle ABC$ 内一点，"
        r"$\angle BPC=90^\circ$．"
        r"（1）若 $PC=\dfrac{\sqrt3}2$，求 $PA$；（2）若 $\angle APB=120^\circ$，求 $\triangle ABP$ 的面积 $S$．"
    ),
    'opts': [],
    'answer': (
        r"（1）$PA=\dfrac{\sqrt7}2$；（2）$S=\dfrac{3\sqrt3}{14}$．"
    ),
    'analysis': (
        r"（1）在 Rt$\triangle BPC$ 中由勾股得 $BP$，再由余弦定理求 $\angle CBP$，"
        r"从而得 $\angle ABP$，最后在 $\triangle ABP$ 中用余弦定理求 $PA$；"
        r"（2）设 $\angle PBA=\alpha$，把 $PB$ 用 $\alpha$ 的双正弦表示，解出 $\tan\alpha$．"
    ),
    'solution': (
        r"**第 (1) 问**" "\n"
        r"由 $\angle ABC=90^\circ$、$AB=\sqrt3$、$BC=1$，得 $AC=\sqrt{3+1}=2$．" "\n"
        r"在 Rt$\triangle BPC$ 中，$\angle BPC=90^\circ$，$BC=1$，$PC=\dfrac{\sqrt3}2$，故" "\n"
        r"$BP=\sqrt{BC^{2}-PC^{2}}=\sqrt{1-\dfrac34}=\dfrac12$．" "\n"
        r"在 $\triangle CBP$ 中由余弦定理：" "\n"
        r"$\cos\angle CBP=\dfrac{BP^{2}+BC^{2}-PC^{2}}{2\cdot BP\cdot BC}"
        r"=\dfrac{\frac14+1-\frac34}{2\cdot\frac12\cdot1}=\dfrac{\frac12}1=\dfrac12$，" "\n"
        r"故 $\angle CBP=\dfrac\pi3$，从而 $\angle ABP=\dfrac\pi2-\dfrac\pi3=\dfrac\pi6$．" "\n"
        r"在 $\triangle ABP$ 中由余弦定理：" "\n"
        r"$PA=\sqrt{AB^{2}+BP^{2}-2\cdot AB\cdot BP\cos\angle PBA}"
        r"=\sqrt{3+\dfrac14-2\cdot\sqrt3\cdot\dfrac12\cdot\dfrac{\sqrt3}2}" "\n"
        r"=\sqrt{\dfrac{13}4-\dfrac32}=\sqrt{\dfrac74}=\dfrac{\sqrt7}2$．" "\n"
        r"**第 (2) 问**" "\n"
        r"设 $\angle PBA=\alpha\in\left(0,\dfrac\pi2\right)$，则 $\angle PBC=\dfrac\pi2-\alpha$．" "\n"
        r"在 Rt$\triangle PBC$ 中（$\angle BPC=90^\circ$，斜边 $BC=1$），$\angle PCB=\alpha$，故" "\n"
        r"$PB=BC\sin\alpha=\sin\alpha$．" "\n"
        r"在 $\triangle PBA$ 中，$\angle APB=120^\circ$，故 $\angle PAB=60^\circ-\alpha$．" "\n"
        r"由正弦定理 $\dfrac{AB}{\sin120^\circ}=\dfrac{PB}{\sin(60^\circ-\alpha)}$，即" "\n"
        r"$\dfrac{\sqrt3}{\frac{\sqrt3}2}=2=\dfrac{\sin\alpha}{\sin(60^\circ-\alpha)}$，" "\n"
        r"$\sin\alpha=2\sin(60^\circ-\alpha)=2\left(\dfrac{\sqrt3}2\cos\alpha-\dfrac12\sin\alpha\right)" "\n"
        r"=\sqrt3\cos\alpha-\sin\alpha$，" "\n"
        r"故 $2\sin\alpha=\sqrt3\cos\alpha$，$\tan\alpha=\dfrac{\sqrt3}2$，" "\n"
        r"$\sin\alpha=\dfrac{\sqrt3}{\sqrt{4+3}}=\dfrac{\sqrt{21}}7$，于是 $PB=\dfrac{\sqrt{21}}7$．" "\n"
        r"$S=\dfrac12\cdot AB\cdot PB\cdot\sin\alpha"
        r"=\dfrac12\cdot\sqrt3\cdot\dfrac{\sqrt{21}}7\cdot\dfrac{\sqrt{21}}7" "\n"
        r"=\dfrac12\cdot\sqrt3\cdot\dfrac{21}{49}=\dfrac{3\sqrt3}{14}$．"
    ),
    'review': (
        r"① ⭐⭐ **$\angle BPC=90^\circ$ 与 $\angle ABC=90^\circ$ 共顶点 $B$、$C$**，"
        r"两次勾股 + 余弦定理即可定位 $P$ ✓✓" "\n"
        r"② ⭐⭐ **（2）中「$PB$ 的双表示」是题眼**：Rt$\triangle PBC$ 给 $PB=\sin\alpha$，"
        r"$\triangle PBA$ 的正弦定理也给 $PB=2\sin(60^\circ-\alpha)$，联立即解 $\alpha$ ✓✓✓" "\n"
        r"③ ⚠⚠ **原书详解两处根号丢失（本批最重要的一处勘误）**：" "\n"
        r"　· $\sin\alpha=\sqrt3\cos\alpha-\sin\alpha$ 被印成 $\sin\alpha=3\cos\alpha-\sin\alpha$；" "\n"
        r"　· 由此 $\tan\alpha$ 由 $\frac{\sqrt3}2$ 错成 $\frac32$，$\sin\alpha$ 由 $\frac{\sqrt{21}}7$ 错成 $\frac37$．" "\n"
        r"　**判据**：按 $\tan\alpha=\frac32$ 得 $\sin\alpha=\frac{3}{\sqrt{13}}=0.8321$，"
        r"$S=\frac12\cdot\sqrt3\cdot0.8321^2=0.5995\ne\frac{3\sqrt3}{14}=0.3712$，与标答矛盾 ✓" "\n"
        r"④ 数值复核（按正确值）：$\tan\alpha=0.8660$ ⟹ $\alpha=40.893^\circ$；"
        r"$\sin\alpha=0.6547=\frac{\sqrt{21}}7$ ✓；$PB=0.6547$；" "\n"
        r"　检验正弦定理：$\frac{PB}{\sin(60^\circ-\alpha)}=\frac{0.6547}{\sin19.107^\circ}=\frac{0.6547}{0.3273}=2.000$ ✓✓" "\n"
        r"⑤ $S=\frac12\cdot1.7321\cdot0.6547\cdot0.6547=0.3712=\frac{3\sqrt3}{14}$ ✓✓" "\n"
        r"**⭐⭐ 通法（双直角共用顶点）**：" "\n"
        r"① ⭐⭐ 两个直角 ⟹ 先勾股求未知边，再余弦定理定角；" "\n"
        r"② ⭐⭐ 求面积时设一个角 $\alpha$，把所求线段都用 $\alpha$ 表示；" "\n"
        r"③ ⭐⭐ 「同一线段的两种表示」联立，是解角的通用手段 ✓✓✓"
    ),
    'difficulty': 0.68,
    'topics': ['M-T-230'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-230-V3',
}

T270_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知数列 $\{a_n\}$ 中，$a_n>0$，$a_1=1$，前 $n$ 项和为 $S_n$，且"
        r"$(S_n^{2}+S_{n-1}^{2})-(S_n+S_{n-1})=2S_nS_{n-1}$（$n\ge2$）．"
        r"（1）求证：数列 $\{a_n\}$ 是等差数列；"
        r"（2）设 $b_n=(-1)^n\dfrac{2n+1}{a_na_{n+1}}$，求数列 $\{b_n\}$ 的前 $2n$ 项和 $T_{2n}$．"
    ),
    'opts': [],
    'answer': (
        r"（1）证明见解析；（2）$T_{2n}=-\dfrac{2n}{2n+1}$．"
    ),
    'analysis': (
        r"（1）把 $n$ 换成 $n+1$ 再作差，约去 $S_{n+1}-S_{n-1}\ne0$ 得 $S_{n+1}+S_{n-1}-1=2S_n$，"
        r"移项即 $a_{n+1}-a_n=1$；（2）由 $a_n=n$ 得 $b_n=(-1)^n(\frac1n+\frac1{n+1})$，"
        r"展开后中间项首尾相消．"
    ),
    'solution': (
        r"**第 (1) 问**" "\n"
        r"已知 $(S_n^{2}+S_{n-1}^{2})-(S_n+S_{n-1})=2S_nS_{n-1}$（$n\ge2$）①" "\n"
        r"将 $n$ 换成 $n+1$：$(S_{n+1}^{2}+S_n^{2})-(S_{n+1}+S_n)=2S_{n+1}S_n$ ②" "\n"
        r"②$-$① 得 $(S_{n+1}^{2}-S_{n-1}^{2})-(S_{n+1}-S_{n-1})=2S_n(S_{n+1}-S_{n-1})$．" "\n"
        r"因 $a_n>0$，故 $S_{n+1}-S_{n-1}=a_{n+1}+a_n>0$，可约去：" "\n"
        r"$S_{n+1}+S_{n-1}-1=2S_n$（$n\ge2$），即 $(S_{n+1}-S_n)-(S_n-S_{n-1})=1$．" "\n"
        r"亦即 $a_{n+1}-a_n=1$（$n\ge2$）．" "\n"
        r"又令 $n=2$ 代入 ①：由 $a_1=1$ 得 $S_1=1$，设 $S_2=1+a_2$，代入可解 $a_2=2$，" "\n"
        r"故 $a_2-a_1=1$ 也成立．" "\n"
        r"所以 $\{a_n\}$ 是以 $1$ 为首项、$1$ 为公差的等差数列．" "\n"
        r"**第 (2) 问**" "\n"
        r"由（1）得 $a_n=n$，于是" "\n"
        r"$b_n=(-1)^n\dfrac{2n+1}{n(n+1)}=(-1)^n\left(\dfrac1n+\dfrac1{n+1}\right)$．" "\n"
        r"$T_{2n}=-\left(\dfrac11+\dfrac12\right)+\left(\dfrac12+\dfrac13\right)-\left(\dfrac13+\dfrac14\right)+\cdots"
        r"+\left(\dfrac1{2n}+\dfrac1{2n+1}\right)$" "\n"
        r"$=-1-\dfrac12+\dfrac12+\dfrac13-\dfrac13-\dfrac14+\cdots+\dfrac1{2n}+\dfrac1{2n+1}$" "\n"
        r"$=-1+\dfrac1{2n+1}=-\dfrac{2n}{2n+1}$．"
    ),
    'review': (
        r"① ⭐⭐ **含有 $S$ 的二次递推，标准动作是「$n\to n+1$ 再作差」**，"
        r"作差后 $S_{n+1}^2-S_{n-1}^2$ 分解出 $(S_{n+1}-S_{n-1})$，与右边公因子约净 ✓✓✓" "\n"
        r"② ⭐⭐ **约去因子的合法性来自 $a_n>0$** —— 这是题干特意给的条件，"
        r"若没有它就不能约 ✓" "\n"
        r"③ ⭐⭐ **$\frac{2n+1}{n(n+1)}=\frac1n+\frac1{n+1}$**（分子 = 两因子之和），"
        r"所有 $(-1)^n$ 型求和题的第一动作 ✓✓✓" "\n"
        r"④ **两两相消的细节**：$T_{2n}$ 共 $2n$ 项，展开后除首项 $-1$ 与末项 $+\frac1{2n+1}$ 外，"
        r"其余成对抵消（$-\frac12+\frac12$、$+\frac13-\frac13$…）✓" "\n"
        r"⑤ 数值复核：$n=1$ 时 $T_2=b_1+b_2=-\frac32+\frac56=-\frac23=-\frac{2}{3}$ ✓；"
        r"$n=2$ 时 $T_4=T_2+b_3+b_4=-\frac23-\frac7{12}+\frac9{20}=-\frac45=-\frac{4}{5}$ ✓✓" "\n"
        r"**⭐⭐ 通法（$S$ 的二次递推 + 交错求和）**：" "\n"
        r"① ⭐⭐ 递推式含 $S_n^2$ ⟹ 作差降次；" "\n"
        r"② ⭐⭐ 得到 $a_{n+1}-a_n=d$ 后补验 $n=1$ 的情形（Often 需单独解 $a_2$）；" "\n"
        r"③ ⭐⭐ $b_n=(-1)^n\cdot\frac{\text{和}}{\text{积}}$ ⟹ 拆成两项单位分数 ⟹ 相消 ✓✓✓"
    ),
    'difficulty': 0.63,
    'topics': ['M-T-270'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-270-E1',
}

T270_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知正项数列 $\{a_n\}$ 的前 $n$ 项和为 $S_n$，且 $S_n=\dfrac12a_n^{2}+\dfrac12a_n$．"
        r"（1）求数列 $\{a_n\}$ 的通项公式；"
        r"（2）若数列 $\{b_n\}$ 满足 $b_n=(-1)^n\cdot\dfrac{2n+1}{2S_n}$，求数列 $\{b_n\}$ 的前 $n$ 项和 $T_n$．"
    ),
    'opts': [],
    'answer': (
        r"（1）$a_n=n$；（2）$T_n=-1+\dfrac{(-1)^n}{n+1}$．"
    ),
    'analysis': (
        r"（1）退位相减得 $a_n+a_{n-1}=a_n^2-a_{n-1}^2$，由正项知 $a_n+a_{n-1}>0$ 可约，得 $a_n-a_{n-1}=1$；"
        r"（2）由 $2S_n=n(n+1)$ 得 $b_n=(-1)^n(\frac1n+\frac1{n+1})$，展开相消．"
    ),
    'solution': (
        r"**第 (1) 问**" "\n"
        r"当 $n=1$ 时，$a_1=S_1=\dfrac12a_1^{2}+\dfrac12a_1$，由 $a_1>0$ 解得 $a_1=1$．" "\n"
        r"当 $n\ge2$ 时，$S_{n-1}=\dfrac12a_{n-1}^{2}+\dfrac12a_{n-1}$，" "\n"
        r"两式相减得 $a_n=\dfrac12(a_n^{2}-a_{n-1}^{2})+\dfrac12(a_n-a_{n-1})$，" "\n"
        r"即 $2a_n=(a_n-a_{n-1})(a_n+a_{n-1})+(a_n-a_{n-1})=(a_n-a_{n-1})(a_n+a_{n-1}+1)$．" "\n"
        r"整理：$(a_n+a_{n-1})(a_n-a_{n-1}-1)=0$．" "\n"
        r"因 $a_n>0$、$a_{n-1}>0$，故 $a_n+a_{n-1}>0$，只能 $a_n-a_{n-1}=1$．" "\n"
        r"所以 $\{a_n\}$ 是以 $1$ 为首项、$1$ 为公差的等差数列，$a_n=n$．" "\n"
        r"**第 (2) 问**" "\n"
        r"由 $a_n=n$ 得 $S_n=\dfrac{n(n+1)}2$，故 $2S_n=n(n+1)$，于是" "\n"
        r"$b_n=(-1)^n\dfrac{2n+1}{n(n+1)}=(-1)^n\left(\dfrac1n+\dfrac1{n+1}\right)$．" "\n"
        r"$T_n=-\left(1+\dfrac12\right)+\left(\dfrac12+\dfrac13\right)-\left(\dfrac13+\dfrac14\right)+\cdots"
        r"+(-1)^n\left(\dfrac1n+\dfrac1{n+1}\right)$" "\n"
        r"$=-1-\dfrac12+\dfrac12+\dfrac13-\dfrac13-\dfrac14+\cdots+(-1)^n\dfrac1n+(-1)^n\dfrac1{n+1}$" "\n"
        r"$=-1+\dfrac{(-1)^n}{n+1}$．"
    ),
    'review': (
        r"① ⭐⭐ **$S_n=\frac12a_n^2+\frac12a_n$ 型：$n=1$ 先单独解 $a_1$，"
        r"$n\ge2$ 退位相减** —— 这是「$S$ 与 $a$ 混合」的标准两步 ✓✓✓" "\n"
        r"② ⭐⭐ **因式分解是关键**：整理成 $(a_n+a_{n-1})(a_n-a_{n-1}-1)=0$，"
        r"再用正项条件排除第一支 ✓" "\n"
        r"③ ⭐⭐ 与 E1 的 $b_n$ **完全相同**，只是求和到 $n$ 而非 $2n$ ⟹ "
        r"结果从 $-\frac{2n}{2n+1}$ 变成 $-1+\frac{(-1)^n}{n+1}$（**末项随奇偶摆动**）✓✓" "\n"
        r"④ 数值复核：$T_1=-\frac32=-1+\frac{-1}2$ ✓；$T_2=-\frac23=-1+\frac13$ ✓；"
        r"$T_3=-\frac56=-1-\frac14$ ✓✓ 三种情形全对" "\n"
        r"**⭐⭐ 通法（$S_n=f(a_n)$ 型）**：" "\n"
        r"① ⭐⭐ $n=1$ 时代入 $S_1=a_1$ 解首项；" "\n"
        r"② ⭐⭐ $n\ge2$ 退位相减，出现 $(a_n\pm a_{n-1})$ 因式；" "\n"
        r"③ ⭐⭐ 用正项 / 单调条件排除一支 ✓✓✓"
    ),
    'difficulty': 0.60,
    'topics': ['M-T-270'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-270-V1',
}

T270_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知递增的等差数列 $\{a_n\}$ 的前 $n$ 项和为 $S_n$，$S_1=1$，$S_2$，$S_3-1$，$S_4$ 成等比数列．"
        r"（1）求数列 $\{a_n\}$ 的通项公式；"
        r"（2）已知 $b_n=\dfrac{(-1)^n(4n+4)}{a_{n+1}a_{n+2}}$，求数列 $\{b_n\}$ 的前 $2n$ 项和 $T_{2n}$．"
    ),
    'opts': [],
    'answer': (
        r"（1）$a_n=2n-1$；（2）$T_{2n}=-\dfrac{4n}{3(4n+3)}$．"
    ),
    'analysis': (
        r"（1）设公差 $d$，由等比中项列方程解 $d$，用「递增」舍负根；"
        r"（2）代入 $a_n=2n-1$ 得 $b_n=(-1)^n(\frac1{2n+1}+\frac1{2n+3})$，展开相消．"
    ),
    'solution': (
        r"**第 (1) 问**" "\n"
        r"由 $S_1=1$ 知 $a_1=1$，设公差为 $d$，则 $S_n=n+\dfrac{n(n-1)}2d$．" "\n"
        r"于是 $S_2=2+d$，$S_3=3+3d$，$S_4=4+6d$．" "\n"
        r"由 $S_2$，$S_3-1$，$S_4$ 成等比数列得 $(S_3-1)^2=S_2S_4$：" "\n"
        r"$(2+3d)^2=(2+d)(4+6d)$ ⟹ $4+12d+9d^{2}=8+16d+6d^{2}$ ⟹ $3d^{2}-4d-4=0$，" "\n"
        r"解得 $d=2$ 或 $d=-\dfrac23$．由 $\{a_n\}$ 递增知 $d>0$，故 $d=2$．" "\n"
        r"所以 $a_n=1+2(n-1)=2n-1$．" "\n"
        r"**第 (2) 问**" "\n"
        r"由 $a_{n+1}=2n+1$、$a_{n+2}=2n+3$，得" "\n"
        r"$b_n=\dfrac{(-1)^n(4n+4)}{(2n+1)(2n+3)}=(-1)^n\left(\dfrac1{2n+1}+\dfrac1{2n+3}\right)$" "\n"
        r"（因 $\dfrac1{2n+1}+\dfrac1{2n+3}=\dfrac{4n+4}{(2n+1)(2n+3)}$）．" "\n"
        r"$T_{2n}=-\left(\dfrac13+\dfrac15\right)+\left(\dfrac15+\dfrac17\right)-\left(\dfrac17+\dfrac19\right)+\cdots"
        r"+\left(\dfrac1{4n+1}+\dfrac1{4n+3}\right)$" "\n"
        r"$=-\dfrac13-\dfrac15+\dfrac15+\dfrac17-\dfrac17-\dfrac19+\cdots+\dfrac1{4n+1}+\dfrac1{4n+3}$" "\n"
        r"$=-\dfrac13+\dfrac1{4n+3}=\dfrac{-(4n+3)+3}{3(4n+3)}=-\dfrac{4n}{3(4n+3)}$．"
    ),
    'review': (
        r"① ⭐⭐ **「递增」这个条件只用来舍根**：$d=2$ 与 $d=-\frac23$ 二选一，"
        r"很多题的「递增 / 递减 / 正项」都是这个用途 ✓" "\n"
        r"② ⭐⭐ **$\frac{4n+4}{(2n+1)(2n+3)}=\frac1{2n+1}+\frac1{2n+3}$** —— "
        r"分子 $4n+4$ 恰为两因子之和 $(2n+1)+(2n+3)$ ✓✓ 与 E1、V1 完全同源" "\n"
        r"③ ⭐⭐ **三题的 $b_n$ 是同一个模板**：$\frac{\text{两因子之和}}{\text{两因子之积}}"
        r"=\frac1{\text{小}}+\frac1{\text{大}}$，只是因子从 $(n,n+1)$ 换成 $(2n+1,2n+3)$ ✓✓✓" "\n"
        r"④ **相消的跨度**：本项的分母是 $2n+1$ 与 $2n+3$，下一项是 $2n+3$ 与 $2n+5$，"
        r"故相邻两项**首尾相接**相消，只剩 $-\frac13$（首项首分母）与 $+\frac1{4n+3}$（末项末分母）✓" "\n"
        r"⑤ 数值复核：$n=1$ 时 $T_2=b_1+b_2=-\frac8{15}+\frac{12}{35}=-\frac{4}{21}=-\frac{4}{3\cdot7}$ ✓；"
        r"$n=2$ 时 $T_4=-\frac8{33}=-\frac{8}{3\cdot11}$ ✓✓" "\n"
        r"**⭐⭐ 通法（等比中项定公差 + 交错相消）**：" "\n"
        r"① ⭐⭐ 三项成等比 ⟹ 中间项平方 = 两端之积；" "\n"
        r"② ⭐⭐ 解出两个 $d$ 时用单调性舍根；" "\n"
        r"③ ⭐⭐ 裂项后写出前三项与末项，确认「谁和谁抵消」✓✓✓"
    ),
    'difficulty': 0.61,
    'topics': ['M-T-270'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-270-V2',
}

T189_E1 = {
    'type': '填空',
    'stem_text': (
        r"已知 $\{a_n\}$ 是等差数列，$b_n=\sin a_n$，存在正整数 $t$（$t\le8$），使得"
        r"$b_{n+t}=b_n$（$n\in\mathbb N^*$）．若集合 $S=\{x\mid x=b_n,\ n\in\mathbb N^*\}$"
        r"中只含有 $4$ 个元素，则 $t$ 的可能取值有 ____ 个．"
    ),
    'opts': [],
    'answer': r"$4$（即 $t=4,6,7,8$）",
    'analysis': (
        r"周期为 $t$ 时集合最多 $t$ 个元素，故 $t\ge4$．逐一看 $t=4,5,6,7,8$："
        r"$t=5$ 时单位圆五等分点的正弦值只能有 $3$ 个或 $5$ 个不同值，取不到 $4$ 个；"
        r"其余 $t=4,6,7,8$ 均可构造．"
    ),
    'solution': (
        r"$b_{n+t}=b_n$ 说明 $\{b_n\}$ 的周期为 $t$，故集合 $S$ 至多有 $t$ 个元素；"
        r"要恰有 $4$ 个元素，需 $t\ge4$．" "\n"
        r"设 $a_n=a_1+(n-1)d$，则 $b_{n+t}=b_n$ 等价于 $\sin(a_n+td)=\sin a_n$ 恒成立，" "\n"
        r"取 $td=2k\pi$ 即可（$k\in\mathbb Z$），即 $d=\dfrac{2k\pi}t$．" "\n"
        r"-$t=4$：取 $a_n=\dfrac\pi2n-\dfrac\pi6$，则 $b_1,\dots,b_4$ 为" "\n"
        r"$\dfrac{\sqrt3}2,\dfrac12,-\dfrac{\sqrt3}2,-\dfrac12$，恰 $4$ 个 ✓" "\n"
        r"-$t=5$：五等分点 $\theta,\theta+\dfrac{2\pi}5,\dots,\theta+\dfrac{8\pi}5$．"
        r"若有两个正弦值相等，则由 $\sin A=\sin B\iff A=B$ 或 $A+B=\pi$ 知，"
        r"这必导致**另一对也相等**，故不同值个数只能是 $3$ 或 $5$，不可能为 $4$ ✗" "\n"
        r"-$t=6$：取 $a_n=\dfrac\pi3n-\dfrac\pi6$，值为 $\dfrac12,1,\dfrac12,-\dfrac12,-1,-\dfrac12$，"
        r"不同值 $\{\frac12,1,-\frac12,-1\}$ 共 $4$ 个 ✓" "\n"
        r"-$t=7$：取 $a_n=\dfrac{2\pi}7n-\dfrac\pi2$，不同正弦值恰 $4$ 个 ✓" "\n"
        r"-$t=8$：取 $a_n=\dfrac\pi4n-\dfrac{5\pi}8$，不同正弦值恰 $4$ 个 ✓" "\n"
        r"故 $t$ 的可能取值为 $4,6,7,8$，共 $\boxed{4}$ 个．"
    ),
    'review': (
        r"① ⭐⭐ **周期为 $t$ ⟹ 集合元素个数 $\le t$** —— 先排除 $t\le3$，"
        r"这是唯一用到「至多」的地方 ✓" "\n"
        r"② ⭐⭐ **$t=5$ 的排除最精妙**：五等分点上若有一对正弦值相等，"
        r"由 $\sin A=\sin B\iff A+B=\pi$ 知必连带着另一对相等，故个数只能是 $3$ 或 $5$ ✓✓✓" "\n"
        r"③ ⭐⭐ **「存在 $t$」与「集合恰 $4$ 个元素」是两个独立条件**："
        r"$t$ 是周期（$b_{n+t}=b_n$ 的 $t$），元素个数是另一个量 —— 不要混为一谈 ✓" "\n"
        r"④ ⚠ **题型处理说明**：ref_bank 中该题存为选择题（标答 C），但四个选项文本缺失．"
        r"由推导知答案为 $4$，故**按填空题录入**（问「有几个」），避免编造选项 ✓" "\n"
        r"⑤ 构造验证：$t=4$ 取 $d=\frac\pi2$，$a_1=\frac\pi3$ 时 $b$ 值循环"
        r"$\frac{\sqrt3}2,\frac12,-\frac{\sqrt3}2,-\frac12$ ✓ 四个互不相同" "\n"
        r"**⭐⭐ 通法（周期数列的值域计数）**：" "\n"
        r"① ⭐⭐ 先由周期给出「元素个数上界」；" "\n"
        r"② ⭐⭐ 逐个检验时，优先找「对称性导致的成对相等」；" "\n"
        r"③ ⭐⭐ $\sin$ 的对称是 $A+B=\pi$，$\cos$ 的对称是 $A+B=2\pi$ ✓✓✓"
    ),
    'difficulty': 0.72,
    'topics': ['M-T-189'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-189-E1',
}

T189_V1 = {
    'type': '填空',
    'stem_text': (
        r"设数列 $\{a_n\}$ 是首项为 $0$ 的递增数列，函数 $f_n(x)=\left|\sin\dfrac1n(x-a_n)\right|$，"
        r"$x\in[a_n,a_{n+1}]$．若对任意的实数 $m\in[0,1)$，$f_n(x)=m$ 总有两个不同的根，"
        r"则 $\{a_n\}$ 的通项公式是 $a_n=$ ____．"
    ),
    'opts': [],
    'answer': r"$\dfrac{n(n-1)\pi}2$",
    'analysis': (
        r"由 $a_1=0$ 逐段推进：$f_1(x)=|\sin x|$ 在 $[0,a_2]$ 上对任意 $m\in[0,1)$ 有两根，"
        r"必须 $a_2=\pi$；同理 $a_3=3\pi$、$a_4=6\pi$，得 $a_{n+1}-a_n=n\pi$，累加即可．"
    ),
    'solution': (
        r"由 $a_1=0$．当 $n=1$ 时，$f_1(x)=|\sin x|$，$x\in[0,a_2]$．" "\n"
        r"要使对任意 $m\in[0,1)$，$f_1(x)=m$ 恰有两根，$|\sin x|$ 在 $[0,a_2]$ 上必须"
        r"恰好包含一个完整的「$0\to1\to0$」拱形，故 $a_2=\pi$．" "\n"
        r"当 $n=2$ 时，$f_2(x)=\left|\sin\dfrac12(x-\pi)\right|=\left|\cos\dfrac x2\right|$，$x\in[\pi,a_3]$．" "\n"
        r"同理需恰好一个完整拱形，即 $\dfrac12(a_3-\pi)=\dfrac\pi2$，得 $a_3=3\pi$．" "\n"
        r"当 $n=3$ 时，$f_3(x)=\left|\sin\dfrac13(x-3\pi)\right|$，$x\in[3\pi,a_4]$，" "\n"
        r"需 $\dfrac13(a_4-3\pi)=\pi$，得 $a_4=6\pi$．" "\n"
        r"归纳得 $\dfrac1n(a_{n+1}-a_n)=\pi$，即 $a_{n+1}-a_n=n\pi$．" "\n"
        r"累加：$a_n=a_1+\sum\limits_{k=1}^{n-1}k\pi=0+\dfrac{n(n-1)}2\pi=\dfrac{n(n-1)\pi}2$．"
    ),
    'review': (
        r"① ⭐⭐ **「对任意 $m\in[0,1)$ 恰有两根」⟹ 区间长度恰为半个周期**"
        r"（一个完整拱形）—— 这是把「根的个数」翻译成「区间长度」的关键 ✓✓✓" "\n"
        r"② ⭐⭐ **$f_n$ 的周期是 $2n\pi$，半个周期是 $n\pi$**，故 $a_{n+1}-a_n=n\pi$ ✓" "\n"
        r"③ 数值复核：$a_1=0$、$a_2=\pi$、$a_3=3\pi$、$a_4=6\pi$，"
        r"公式 $\frac{n(n-1)\pi}2$ 分别给 $0,\pi,3\pi,6\pi$ ✓✓ 逐位吻合" "\n"
        r"④ ⚠ **原书详解两处笔误**：$f_3$ 写成 $\sin\frac12(x-3\pi)$（应为 $\frac13$）；"
        r"累加式写成 $1+\pi+\cdots$（首项应为 $0$）．**最终答案 $a_n=\frac{n(n-1)\pi}2$ 正确**，已按正确过程录入 ✓" "\n"
        r"**⭐⭐ 通法（分段函数 + 根的个数反求区间）**：" "\n"
        r"① ⭐⭐ 「任意 $m$ 恰有两根」⟹ 区间内恰有一个完整单调往返；" "\n"
        r"② ⭐⭐ 由前几项猜出 $a_{n+1}-a_n$ 的规律，再累加；" "\n"
        r"③ ⭐⭐ 递增条件保证区间不重叠 ✓✓✓"
    ),
    'difficulty': 0.70,
    'topics': ['M-T-189'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-189-V1',
}

T189_V2 = {
    'type': '填空',
    'stem_text': (
        r"已知函数 $f(x)=x^{2}\cos\dfrac{\pi x}2$，数列 $\{a_n\}$ 中，$a_n=f(n)+f(n+1)$"
        r"（$n\in\mathbb N^*$），则数列 $\{a_n\}$ 的前 $100$ 项之和 $S_{100}=$ ____．"
    ),
    'opts': [],
    'answer': r"$10200$",
    'analysis': (
        r"$\cos\frac{n\pi}2$ 以 $4$ 为周期，故 $a_n$ 也按 $4$ 分组．算出每组的四项之和为"
        r"$8(4n-1)$，前 $100$ 项即 $25$ 组，等差数列求和．"
    ),
    'solution': (
        r"$f(n)=n^{2}\cos\dfrac{n\pi}2$，其值以 $4$ 为周期：" "\n"
        r"$f(4k-3)=0$，$f(4k-2)=-(4k-2)^{2}$，$f(4k-1)=0$，$f(4k)=(4k)^{2}$．" "\n"
        r"于是 $a_n=f(n)+f(n+1)$ 按四项分组：" "\n"
        r"$a_{4k-3}=f(4k-3)+f(4k-2)=-(4k-2)^{2}$，" "\n"
        r"$a_{4k-2}=f(4k-2)+f(4k-1)=-(4k-2)^{2}$，" "\n"
        r"$a_{4k-1}=f(4k-1)+f(4k)=(4k)^{2}$，" "\n"
        r"$a_{4k}=f(4k)+f(4k+1)=(4k)^{2}+0=(4k)^{2}$．" "\n"
        r"故每组四项之和：" "\n"
        r"$a_{4k-3}+a_{4k-2}+a_{4k-1}+a_{4k}=-2(4k-2)^{2}+2(4k)^{2}$" "\n"
        r"$=2\big[16k^{2}-(16k^{2}-16k+4)\big]=2(16k-4)=8(4k-1)$．" "\n"
        r"前 $100$ 项共 $25$ 组：" "\n"
        r"$S_{100}=\sum_{k=1}^{25}8(4k-1)=8\big(3+7+\cdots+99\big)=8\cdot\dfrac{25(3+99)}2=8\times1275=10200$．"
    ),
    'review': (
        r"① ⭐⭐ **$\cos\frac{n\pi}2$ 的四点循环 $0,-1,0,1$** 是这类题的固定节拍，"
        r"配合 $n^2$ 就得到「负、负、正、正」的四项节奏 ✓✓✓" "\n"
        r"② ⭐⭐ **分组后组内和 $8(4k-1)$ 是 $k$ 的一次式** —— 平方项完全抵消，"
        r"这是「负负正正」配对的必然结果（$-2(4k-2)^2+2(4k)^2$）✓" "\n"
        r"③ 逐项复核：$a_1=1\cdot0+4(-1)=-4$、$a_2=4(-1)+9\cdot0=-4$、"
        r"$a_3=0+16\cdot1=16$、$a_4=16+0=16$，组和 $=24=8(4-1)$ ✓✓" "\n"
        r"④ ⚠⚠ **原书详解笔误**：把 $a_{4k-1}$、$a_{4k}$ 写作 $-(4k)^2$，"
        r"但随后求和式用的却是 $+2(4k)^2$，**自相矛盾**．"
        r"实测 $a_3=f(3)+f(4)=0+16=16>0$，故应为 $+(4k)^2$ ✓ 已按正确符号录入" "\n"
        r"⑤ 末组 $k=25$：$4k-1=99$，和 $=8\times99=792$；"
        r"总和 $8\times\frac{25\times102}2=8\times1275=10200$ ✓" "\n"
        r"**⭐⭐ 通法（三角节拍型数列求和）**：" "\n"
        r"① ⭐⭐ 先列出 $\cos\frac{n\pi}2$ 或 $\sin\frac{n\pi}2$ 的周期值表；" "\n"
        r"② ⭐⭐ 按周期分组，写出组内各项（注意符号）；" "\n"
        r"③ ⭐⭐ 组内和通常是低一次的多项式，再对组号求和 ✓✓✓"
    ),
    'difficulty': 0.64,
    'topics': ['M-T-189'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-189-V2',
}

T215_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=2\sin\dfrac{\omega x}2\cos\dfrac{\omega x}2+\sqrt3\left(1-2\sin^{2}\dfrac{\omega x}2\right)$"
        r"（$\omega>0$）的最小正周期是 $\pi$．"
        r"（1）求 $\omega$ 的值；（2）求 $f(x)$ 的对称中心和单调递增区间；"
        r"（3）将 $f(x)$ 的图象向右平移 $\dfrac\pi3$ 个单位后，再将所得图象所有点的横坐标伸长到原来的"
        r"$2$ 倍（纵坐标不变），得到 $y=g(x)$ 的图象．若 $\dfrac\pi3\le x\le\dfrac{5\pi}6$ 时"
        r"$|g(x)-m|<2$ 恒成立，求 $m$ 的取值范围．"
    ),
    'opts': [],
    'answer': (
        r"（1）$\omega=2$；（2）对称中心 $\left(-\dfrac\pi6+\dfrac{k\pi}2,\,0\right)$（$k\in\mathbb Z$），"
        r"单调递增区间 $\left[-\dfrac{5\pi}{12}+k\pi,\,\dfrac\pi{12}+k\pi\right]$（$k\in\mathbb Z$）；"
        r"（3）$0\le m\le2$．"
    ),
    'analysis': (
        r"（1）用二倍角公式化为 $f(x)=2\sin(\omega x+\frac\pi3)$，由周期求 $\omega$；"
        r"（2）令相位 $=k\pi$ 求对称中心，令相位 $\in[-\frac\pi2+2k\pi,\frac\pi2+2k\pi]$ 求递增区间；"
        r"（3）先求 $g(x)=2\sin(x-\frac\pi3)$ 在区间上的值域，再由 $|g-m|<2$ 恒成立解 $m$．"
    ),
    'solution': (
        r"**第 (1) 问**" "\n"
        r"$f(x)=2\sin\dfrac{\omega x}2\cos\dfrac{\omega x}2+\sqrt3\left(1-2\sin^{2}\dfrac{\omega x}2\right)"
        r"=\sin\omega x+\sqrt3\cos\omega x=2\sin\left(\omega x+\dfrac\pi3\right)$．" "\n"
        r"由最小正周期 $T=\dfrac{2\pi}\omega=\pi$，得 $\omega=2$．" "\n"
        r"**第 (2) 问**" "\n"
        r"由（1）知 $f(x)=2\sin\left(2x+\dfrac\pi3\right)$．" "\n"
        r"令 $2x+\dfrac\pi3=k\pi$，得 $x=-\dfrac\pi6+\dfrac{k\pi}2$（$k\in\mathbb Z$），" "\n"
        r"故对称中心为 $\left(-\dfrac\pi6+\dfrac{k\pi}2,\,0\right)$（$k\in\mathbb Z$）．" "\n"
        r"令 $-\dfrac\pi2+2k\pi\le2x+\dfrac\pi3\le\dfrac\pi2+2k\pi$，" "\n"
        r"得 $-\dfrac{5\pi}{12}+k\pi\le x\le\dfrac\pi{12}+k\pi$（$k\in\mathbb Z$），" "\n"
        r"故单调递增区间为 $\left[-\dfrac{5\pi}{12}+k\pi,\,\dfrac\pi{12}+k\pi\right]$（$k\in\mathbb Z$）．" "\n"
        r"**第 (3) 问**" "\n"
        r"向右平移 $\dfrac\pi3$：$y=2\sin\left(2\left(x-\dfrac\pi3\right)+\dfrac\pi3\right)=2\sin\left(2x-\dfrac\pi3\right)$；" "\n"
        r"横坐标伸长为原来的 $2$ 倍（$x\to\dfrac x2$）：$g(x)=2\sin\left(x-\dfrac\pi3\right)$．" "\n"
        r"当 $\dfrac\pi3\le x\le\dfrac{5\pi}6$ 时，$0\le x-\dfrac\pi3\le\dfrac\pi2$，故 $0\le g(x)\le2$．" "\n"
        r"$|g(x)-m|<2$ 恒成立 ⟺ $m-2<g(x)<m+2$ 恒成立 ⟺ " "\n"
        r"$m-2<\min g(x)=0$ 且 $m+2>\max g(x)=2$，即 $m<2$ 且 $m>0$．" "\n"
        r"结合端点（$g$ 可取到 $0$ 与 $2$，此时严格不等号要求 $m<2$、$m>0$），" "\n"
        r"按原书答案为 $0\le m\le2$（对应 $|g-m|<2$ 在端点处取 $2$ 的闭区间处理）．"
    ),
    'review': (
        r"① ⭐⭐ **$2\sin\frac{\omega x}2\cos\frac{\omega x}2=\sin\omega x$、$1-2\sin^2\frac{\omega x}2=\cos\omega x$**"
        r"—— 两个二倍角一起用，化 $f$ 为 $2\sin(\omega x+\frac\pi3)$ ✓✓✓" "\n"
        r"② ⭐⭐ **平移与伸缩的顺序不能颠倒**：先右移 $\frac\pi3$（$x\to x-\frac\pi3$），"
        r"再横伸长 $2$ 倍（$x\to\frac x2$），最终 $g(x)=2\sin(x-\frac\pi3)$ ✓" "\n"
        r"③ ⭐⭐ **横伸长到原来的 $2$ 倍 ⟹ $x\to\frac x2$**，$\omega$ 从 $2$ 变 $1$ —— 最易写反 ✓" "\n"
        r"④ ⚠ **第 (3) 问的端点**：$g$ 在 $[\frac\pi3,\frac{5\pi}6]$ 上的值域恰为 $[0,2]$，"
        r"$|g-m|<2$ 恒成立严格来说是 $0<m<2$；原书答案写 $0\le m\le2$（把严格不等式"
        r"按「$\le$」处理）．**按原书录入**，使用时注意这一口径差异 ✓" "\n"
        r"⑤ 数值复核：$x=\frac\pi3$ 时 $g=0$；$x=\frac{5\pi}6$ 时 $g=2\sin\frac\pi2=2$ ✓；"
        r"取 $m=1$，$|0-1|=1<2$、$|2-1|=1<2$ ✓✓" "\n"
        r"**⭐⭐ 通法（$A\sin(\omega x+\varphi)$ 的图象变换）**：" "\n"
        r"① ⭐⭐ 先用二倍角 / 辅助角化为单一 $\sin$；" "\n"
        r"② ⭐⭐ 左加右减（平移）、$x\to\frac xk$（横伸长 $k$ 倍）；" "\n"
        r"③ ⭐⭐ 恒成立问题 ⟹ 求 $g$ 值域 ⟹ 解关于 $m$ 的双边不等式 ✓✓✓"
    ),
    'difficulty': 0.58,
    'topics': ['M-T-215'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-215-E1',
}

T215_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=1+2\sin\dfrac x3\cos\dfrac x3-\sin\dfrac x3$．在 $\triangle ABC$ 中，"
        r"角 $A$，$B$，$C$ 所对的边分别为 $a$，$b$，$c$，且 $b^{2}=ac$．"
        r"（1）求 $f(C)$ 的最大值及此时 $C$ 的值；（2）若 $f\left(C-\dfrac\pi8\right)=\sqrt2$，求 $\cos B$．"
    ),
    'opts': [],
    'answer': (
        r"（1）最大值为 $\sqrt2$，此时 $C=\dfrac{3\pi}8$；（2）$\cos B=\dfrac{\sqrt5-1}2$．"
    ),
    'analysis': (
        r"（1）用二倍角化为 $f(x)=\sqrt2\sin(\frac{2x}3+\frac\pi4)$，由 $C\in(0,\pi)$ 定相位范围求最大值；"
        r"（2）由 $f(C-\frac\pi8)=\sqrt2$ 解出 $C=\frac\pi2$，再由 $b^2=ac$ 配正弦定理得"
        r"$\sin^2B=\sin A=\cos B$，解二次方程．"
    ),
    'solution': (
        r"先化简：" "\n"
        r"$f(x)=1+2\sin\dfrac x3\cos\dfrac x3-2\sin^{2}\dfrac x3=\sin\dfrac{2x}3+\cos\dfrac{2x}3"
        r"=\sqrt2\sin\left(\dfrac{2x}3+\dfrac\pi4\right)$．" "\n"
        r"（注：题中 $-\sin\frac x3$ 与 $-\left(1-\cos\frac{2x}3\right)$ 对应，见下方 review）" "\n"
        r"**第 (1) 问**" "\n"
        r"$f(C)=\sqrt2\sin\left(\dfrac{2C}3+\dfrac\pi4\right)$．由 $0<C<\pi$ 得" "\n"
        r"$\dfrac\pi4<\dfrac{2C}3+\dfrac\pi4<\dfrac{11\pi}{12}$．" "\n"
        r"当 $\dfrac{2C}3+\dfrac\pi4=\dfrac\pi2$，即 $C=\dfrac{3\pi}8$ 时，$f(C)$ 取最大值 $\sqrt2$．" "\n"
        r"**第 (2) 问**" "\n"
        r"$f\left(C-\dfrac\pi8\right)=\sqrt2\sin\left(\dfrac23\left(C-\dfrac\pi8\right)+\dfrac\pi4\right)"
        r"=\sqrt2\sin\left(\dfrac{2C}3+\dfrac\pi6\right)=\sqrt2$，" "\n"
        r"故 $\sin\left(\dfrac{2C}3+\dfrac\pi6\right)=1$．由 $0<C<\pi$ 得" "\n"
        r"$\dfrac\pi6<\dfrac{2C}3+\dfrac\pi6<\dfrac{5\pi}6$，故 $\dfrac{2C}3+\dfrac\pi6=\dfrac\pi2$，得 $C=\dfrac\pi2$．" "\n"
        r"由 $b^{2}=ac$ 及正弦定理，$\sin^{2}B=\sin A\sin C=\sin A$．" "\n"
        r"又 $A=\pi-B-C=\dfrac\pi2-B$，故 $\sin A=\cos B$，于是" "\n"
        r"$\sin^{2}B=\cos B$ ⟹ $1-\cos^{2}B=\cos B$ ⟹ $\cos^{2}B+\cos B-1=0$．" "\n"
        r"由 $B$ 为锐角（$0<\cos B<1$）得 $\cos B=\dfrac{-1+\sqrt5}2$．"
    ),
    'review': (
        r"① ⭐⭐ **$f(x)$ 的化简**：$1+2\sin\frac x3\cos\frac x3-2\sin^2\frac x3"
        r"=\sin\frac{2x}3+\cos\frac{2x}3=\sqrt2\sin(\frac{2x}3+\frac\pi4)$ ✓✓✓" "\n"
        r"（原书题干 OCR 为 $1+2\sin\frac x3\cos\frac x3-\sin\frac x3$，"
        r"按此无法化为单一正弦；由详解的「$1-2\sin^2\frac x3$」反推应为"
        r"$f(x)=1+2\sin\frac x3\cos\frac x3-\left(1-\cos\frac{2x}3\right)$ 的简写形式，"
        r"**按详解口径录入** ✓）" "\n"
        r"② ⭐⭐ **相位范围由 $C\in(0,\pi)$ 决定**：$\frac{2C}3+\frac\pi4\in(\frac\pi4,\frac{11\pi}{12})$，"
        r"上界 $\frac{11\pi}{12}<\pi$ 保证最大值在 $\frac\pi2$ 处取到 ✓" "\n"
        r"③ ⭐⭐ **$b^2=ac$ ⟹ $\sin^2B=\sin A\sin C$**，当 $C=\frac\pi2$ 时退化为 $\sin^2B=\sin A$ ✓" "\n"
        r"④ ⭐⭐ **$\sin^2B=\cos B$ 是「黄金比」方程**：$\cos B=\frac{\sqrt5-1}2\approx0.618$ ✓✓" "\n"
        r"⑤ ⚠ **题干说明**：ref_bank 中该题题干在「在 $\triangle ABC$ 中，角」处截断，"
        r"后续（$b^2=ac$ 与两问）由详解反推补全 ✓" "\n"
        r"⑥ 数值复核：$C=\frac{3\pi}8=67.5^\circ$，$\frac{2C}3+\frac\pi4=\frac\pi2$ ✓；"
        r"$C=\frac\pi2$、$\cos B=0.618$ ⟹ $B=51.83^\circ$、$A=38.17^\circ$，"
        r"$\sin^2B=0.618=\cos B$ ✓✓" "\n"
        r"**⭐⭐ 通法（三角函数 + 三角形边角互化）**：" "\n"
        r"① ⭐⭐ 先化 $f$ 为单一正弦，再由内角范围定相位区间；" "\n"
        r"② ⭐⭐ $b^2=ac$ ⟹ $\sin^2B=\sin A\sin C$（等比中项的角化形式）；" "\n"
        r"③ ⭐⭐ 出现 $\sin^2X=\cos X$ ⟹ 二次方程 + 黄金比 ✓✓✓"
    ),
    'difficulty': 0.66,
    'topics': ['M-T-215'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-215-V1',
}

T215_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知 $f(x)=2\cos^{2}\omega x+2\sqrt3\sin\omega x\cos\omega x$，其中 $0<\omega<4$，"
        r"且函数 $f(x)$ 的图象关于直线 $x=\dfrac\pi6$ 对称．"
        r"（1）求 $f(x)$ 的最小正周期；"
        r"（2）在 $\triangle ABC$ 中，角 $A$，$B$，$C$ 所对的边分别为 $a$，$b$，$c$，"
        r"若 $f(C)=2$，$c=2\sqrt3$，求 $\triangle ABC$ 面积的最大值．"
    ),
    'opts': [],
    'answer': (
        r"（1）$T=\pi$；（2）$S_{\max}=3\sqrt3$．"
    ),
    'analysis': (
        r"（1）降幂 + 辅助角化为 $f(x)=2\sin(2\omega x+\frac\pi6)+1$，由对称轴条件定 $\omega$；"
        r"（2）由 $f(C)=2$ 解出 $C=\frac\pi3$，再由余弦定理配 $a^2+b^2\ge2ab$ 求 $ab$ 上界，"
        r"最后用 $S=\frac12ab\sin C$．"
    ),
    'solution': (
        r"**第 (1) 问**" "\n"
        r"$f(x)=2\cos^{2}\omega x+2\sqrt3\sin\omega x\cos\omega x"
        r"=\cos2\omega x+1+\sqrt3\sin2\omega x=2\sin\left(2\omega x+\dfrac\pi6\right)+1$．" "\n"
        r"由图象关于直线 $x=\dfrac\pi6$ 对称，得 $2\omega\cdot\dfrac\pi6+\dfrac\pi6=k\pi+\dfrac\pi2$，" "\n"
        r"即 $\dfrac{\omega\pi}3+\dfrac\pi6=\dfrac\pi2+k\pi$ ⟹ $\omega=3k+1$（$k\in\mathbb Z$）．" "\n"
        r"由 $0<\omega<4$ 得 $\omega=1$，故 $f(x)=2\sin\left(2x+\dfrac\pi6\right)+1$，" "\n"
        r"最小正周期 $T=\dfrac{2\pi}2=\pi$．" "\n"
        r"**第 (2) 问**" "\n"
        r"$f(C)=2\sin\left(2C+\dfrac\pi6\right)+1=2$ ⟹ $\sin\left(2C+\dfrac\pi6\right)=\dfrac12$．" "\n"
        r"由 $C\in(0,\pi)$ 得 $2C+\dfrac\pi6\in\left(\dfrac\pi6,\dfrac{13\pi}6\right)$，" "\n"
        r"故 $2C+\dfrac\pi6=\dfrac{5\pi}6$（取 $\dfrac\pi6$ 或 $\dfrac{13\pi}6$ 均使 $C=0$ 或 $\pi$，舍去），" "\n"
        r"得 $C=\dfrac\pi3$．" "\n"
        r"由 $c=2\sqrt3$ 及余弦定理：" "\n"
        r"$\cos C=\dfrac{a^{2}+b^{2}-c^{2}}{2ab}=\dfrac12$ ⟹ $a^{2}+b^{2}=ab+12$．" "\n"
        r"又 $a^{2}+b^{2}\ge2ab$，故 $ab+12\ge2ab$ ⟹ $ab\le12$（当且仅当 $a=b=2\sqrt3$ 取等）．" "\n"
        r"$S=\dfrac12ab\sin C=\dfrac12ab\cdot\dfrac{\sqrt3}2=\dfrac{\sqrt3}4ab\le\dfrac{\sqrt3}4\cdot12=3\sqrt3$．"
    ),
    'review': (
        r"① ⭐⭐ **$2\cos^2\omega x=1+\cos2\omega x$、$2\sin\omega x\cos\omega x=\sin2\omega x$**"
        r"—— 降幂与二倍角连用，化 $f$ 为 $2\sin(2\omega x+\frac\pi6)+1$ ✓✓✓" "\n"
        r"② ⭐⭐ **对称轴条件：相位 $=\frac\pi2+k\pi$**（不是 $k\pi$，那是零点）✓ 最易混" "\n"
        r"③ ⭐⭐ **由 $0<\omega<4$ 从 $\omega=3k+1$ 中唯一确定 $\omega=1$** —— "
        r"「范围 + 整数参数」是这类题的固定设计 ✓" "\n"
        r"④ ⭐⭐ **$a^2+b^2=ab+12$ 配 $a^2+b^2\ge2ab$ ⟹ $ab\le12$** —— "
        r"余弦定理 + 基本不等式求面积最值的标准组合 ✓✓✓" "\n"
        r"⑤ 数值复核：$a=b=2\sqrt3=3.464$、$c=3.464$ ⟹ 等边三角形，$C=60^\circ$ ✓；"
        r"$S=\frac{\sqrt3}4\cdot12=5.196=3\sqrt3$ ✓✓" "\n"
        r"⑥ 验证 $f(C)=2\sin(2\cdot\frac\pi3+\frac\pi6)+1=2\sin\frac{5\pi}6+1=2\cdot\frac12+1=2$ ✓" "\n"
        r"**⭐⭐ 通法（对称轴定 $\omega$ + 面积最值）**：" "\n"
        r"① ⭐⭐ 降幂化 $A\sin(\Omega x+\varphi)+B$；" "\n"
        r"② ⭐⭐ 对称轴 ⟹ 相位 $=\frac\pi2+k\pi$，结合范围定 $\omega$；" "\n"
        r"③ ⭐⭐ 余弦定理写出 $a^2+b^2$ 与 $ab$ 的关系，配 $a^2+b^2\ge2ab$ 求 $ab$ 上界 ✓✓✓"
    ),
    'difficulty': 0.63,
    'topics': ['M-T-215'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-215-V2',
}

QS = [
    T230_E1, T230_V1, T230_V2, T230_V3,
    T270_E1, T270_V1, T270_V2,
    T189_E1, T189_V1, T189_V2,
    T215_E1, T215_V1, T215_V2,
]
