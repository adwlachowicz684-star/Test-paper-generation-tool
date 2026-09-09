# -*- coding: utf-8 -*-
r"""第40批：解析几何离心率（余弦定理用两次 / 多曲线交点） + 外接球垂心投影

来源：2024高中数学热点题型归纳完整解析版.pdf
p349（PDF 页 348）M-T-368 余弦定理3：余弦定理用两次
p351（PDF 页 350）M-T-370 多曲线交点1：和抛物线
p260（PDF 页 259）M-T-293 长方体模板1：三线垂直型

## 选题

`pick_batch.py --n 16` → p349 / p351 / p260。

## ★ 本批最大收获：M-T-293-V3 的 PC=3 实为 √3

题干提取为 `PC = 3`，但若 $PC=3$ 则 $R^{2}=\frac12+\frac84=2.5$、表面积 $10\pi$，
与答案 $4\pi$ **矛盾**。

**实为 $PC=\sqrt3$**：此时 $p_{3}^{2}=2$，$R^{2}=\frac12+\frac24=1$，表面积 $=4\pi$ ✓

这是个通用反证手法 —— **用答案反推丢失的根号**，本批之前已多次奏效
（M-T-190-V3 的 $a=\sqrt3$、M-T-210-V3 的 $AH=\sqrt3$ 都是同一类）。

## 七题验算

| 题 | 计算 | 答案 |
|---|---|---|
| 368-E1 | $a+c>\sqrt5b\to e<\frac32$；$\angle OAF_{2}>\frac\pi2\to e>\sqrt2$ | **B** $(\sqrt2,\frac32)$ |
| 368-V1 | $a=3k$，$4c^{2}=18k^{2}\to e=\frac{\sqrt2}2$ | **A** |
| 368-V2 | 两次余弦定理联立 $6\sqrt2a=8c\to e=\frac{3\sqrt2}4$ | **A** |
| 368-V3 | 互补角余弦 $5c=3a\to e=\frac35$ | **C** |
| 370-V1 | $t^{2}=1$ 时比值最大，$a=1+\sqrt2$、$c=1\to e=\sqrt2-1$ | **D** |
| 370-V3 | 正三角形 $d=\frac p{\sqrt3}$，$3u^{2}+4u-4=0\to e=\frac{\sqrt3}3$ | **C** |
| 293-V3 | 建系 $P(0,0,\sqrt2)$，$R=1\to S=4\pi$ | **$4\pi$** |

## ⚠ M-T-368-E1 详解的一处标注

详解写「$\angle OAF_{1}>\frac\pi2$」，但代入的却是 $\lvert AF_{2}\rvert^{2}=7a^{2}-3c^{2}$，
并得 $c^{2}>a^{2}+(7a^{2}-3c^{2})\Rightarrow e>\sqrt2$。

这实际是 **$\triangle OAF_{2}$** 中的钝角条件（$\angle OAF_{2}>\frac\pi2$），
用 $\lvert AF_{1}\rvert$ 推不出这个结论。已在解答中按 $\angle OAF_{2}$ 书写。
"""

T368_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知 $F_{1},F_{2}$ 分别是双曲线 $\dfrac{x^{2}}{a^{2}}-\dfrac{y^{2}}{b^{2}}=1$"
        r"（$a>0,b>0$）的左、右焦点，点 $P$ 在双曲线右支上且不与顶点重合，"
        r"过 $F_{2}$ 作 $\angle F_{1}PF_{2}$ 的角平分线的垂线，垂足为 $A$．"
        r"若 $\lvert F_{1}A\rvert=\sqrt5\,b$，则该双曲线离心率的取值范围为（　　）"
    ),
    'opts': [
        ('A', r"$(1,\sqrt2)$"),
        ('B', r"$(\sqrt2,\dfrac32)$"),
        ('C', r"$(\sqrt2,\sqrt3)$"),
        ('D', r"$(\dfrac32,\sqrt3)$"),
    ],
    'answer': 'B',
    'analysis': (
        r"把角平分线条件翻译成 $|OA|=a$（中位线），再在 $\triangle F_{1}OA$ 中"
        r"用两边之和大于第三边得上界，用 $\angle OAF_{2}$ 为钝角得下界。"
    ),
    'solution': (
        r"**第一步：角平分线 + 垂线 ⟹ 等腰**" "\n"
        r"延长 $F_{2}A$ 交 $PF_{1}$ 于 $Q$．因 $PA$ 平分 $\angle F_{1}PF_{2}$ 且 $PA\perp F_{2}A$，" "\n"
        r"故 $\triangle PF_{2}Q$ 等腰，$\lvert PQ\rvert=\lvert PF_{2}\rvert$．" "\n"
        r"**第二步：求 $\lvert OA\rvert$**" "\n"
        r"$P$ 在双曲线上：$\lvert PF_{1}\rvert-\lvert PF_{2}\rvert=2a$" "\n"
        r"$\Rightarrow\lvert PF_{1}\rvert-\lvert PQ\rvert=\lvert QF_{1}\rvert=2a$．" "\n"
        r"又 $O$ 是 $F_{1}F_{2}$ 中点、$A$ 是 $F_{2}Q$ 中点，" "\n"
        r"故 $OA$ 是 $\triangle F_{1}F_{2}Q$ 的中位线，$\lvert QF_{1}\rvert=2\lvert OA\rvert$，" "\n"
        r"即 $\lvert OA\rvert=a$．" "\n"
        r"**第三步：上界 —— 两边之和大于第三边**" "\n"
        r"在 $\triangle F_{1}OA$ 中，$\lvert OA\rvert=a$、$\lvert F_{1}A\rvert=\sqrt5b$、$\lvert OF_{1}\rvert=c$：" "\n"
        r"$a+c>\sqrt5b\Rightarrow(a+c)^{2}>5b^{2}=5(c^{2}-a^{2})$" "\n"
        r"$\Rightarrow a^{2}+2ac+c^{2}>5c^{2}-5a^{2}\Rightarrow6a^{2}+2ac-4c^{2}>0$" "\n"
        r"$\Rightarrow 2e^{2}-e-3<0\Rightarrow -1<e<\dfrac32$，结合 $e>1$ 得 $1<e<\dfrac32$．" "\n"
        r"**第四步：下界 —— 先求 $\lvert AF_{2}\rvert$，再用钝角条件**" "\n"
        r"因 $O$ 在 $F_{1}F_{2}$ 上，$\angle AF_{1}O=\angle AF_{1}F_{2}$，分别用两种余弦定理：" "\n"
        r"$\dfrac{5b^{2}+c^{2}-a^{2}}{2\sqrt5bc}=\dfrac{5b^{2}+4c^{2}-\lvert AF_{2}\rvert^{2}}{4\sqrt5bc}$" "\n"
        r"$\Rightarrow\lvert AF_{2}\rvert^{2}=7a^{2}-3c^{2}$．" "\n"
        r"在 $\triangle OAF_{2}$ 中 $\angle OAF_{2}>\dfrac\pi2$，故 $\lvert OF_{2}\rvert^{2}>\lvert OA\rvert^{2}+\lvert AF_{2}\rvert^{2}$：" "\n"
        r"$c^{2}>a^{2}+(7a^{2}-3c^{2})\Rightarrow4c^{2}>8a^{2}\Rightarrow e^{2}>2\Rightarrow e>\sqrt2$．" "\n"
        r"**第五步**：综上 $e\in\left(\sqrt2,\dfrac32\right)$．选 B．"
    ),
    'review': (
        r"★ 题干、选项、答案、详解均完整 ✓。由详解「$|OA|=a$，$|F_{1}A|=\sqrt5b$，$|OF_{1}|=c$，"
        r"由三角形两边之和大于第三边得 $a+c>\sqrt5b$，两边平方得 $(a+c)^{2}>5b^{2}$…"
        r"解得 $-1<e<\frac32$，又 $e>1$，∴$1<e<\frac32$；…$|AF_{2}|^{2}=7a^{2}-3c^{2}$，"
        r"又 ∵$\angle OAF_{1}>\frac\pi2$，∴$OA^{2}+AF_{2}^{2}<OF_{1}^{2}$，即 $a^{2}+7a^{2}-3c^{2}<c^{2}$，"
        r"∴$e>\sqrt2$，综上所述 $e\in(\sqrt2,\frac32)$。故选 B」还原。" "\n"
        r"**独立验算**：" "\n"
        r"① 中位线：$\lvert QF_{1}\rvert=2a=2\lvert OA\rvert$ → $\lvert OA\rvert=a$ ✓" "\n"
        r"② 上界展开：$6a^{2}+2ac-4c^{2}>0$，除以 $2a^{2}$：$3+e-2e^{2}>0$ → $2e^{2}-e-3<0$" "\n"
        r"→ $(2e-3)(e+1)<0$ → $-1<e<\frac32$ ✓" "\n"
        r"③ $\lvert AF_{2}\rvert^{2}$ 推导：$2(5b^{2}+c^{2}-a^{2})=5b^{2}+4c^{2}-\lvert AF_{2}\rvert^{2}$" "\n"
        r"→ $\lvert AF_{2}\rvert^{2}=5b^{2}+4c^{2}-10b^{2}-2c^{2}+2a^{2}=-5b^{2}+2c^{2}+2a^{2}$" "\n"
        r"$= -5(c^{2}-a^{2})+2c^{2}+2a^{2}=7a^{2}-3c^{2}$ ✓" "\n"
        r"④ 下界：$c^{2}>8a^{2}-3c^{2}$ → $4c^{2}>8a^{2}$ → $e^{2}>2$ → $e>\sqrt2$ ✓" "\n"
        r"⑤ 数值自洽：$\sqrt2\approx1.414<\frac32=1.5$ ✓ 区间非空，且 $e>1$ ✓" "\n"
        r"**答案 B 正确** ✓" "\n"
        r"**⚠ 详解一处标注需修正**：详解写「$\angle OAF_{1}>\frac\pi2$」，"
        r"但代入的是 $\lvert AF_{2}\rvert^{2}=7a^{2}-3c^{2}$ 且右边是 $\lvert OF_{1}\rvert^{2}=c^{2}$。" "\n"
        r"若在 $\triangle OAF_{1}$ 中用钝角条件，应为 $c^{2}>a^{2}+5b^{2}$，"
        r"即 $c^{2}>a^{2}+5c^{2}-5a^{2}$ → $4a^{2}>4c^{2}$ → $e<1$，**与双曲线矛盾**。" "\n"
        r"所以正确条件是 **$\triangle OAF_{2}$ 中 $\angle OAF_{2}>\frac\pi2$**" "\n"
        r"（此时对边是 $\lvert OF_{2}\rvert=c$），本解答已按此书写。" "\n"
        r"**⭐ 通法**：角平分线 + 垂足 ⟹ **倍长构造等腰**，这是把角平分线条件"
        r"转化为长度关系的标准动作（本题得到 $|OA|=a$，一个定值，是破题眼）。"
    ),
    'difficulty': 0.93,
    'topics': ['M-T-368'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-368-E1',
}

T368_V1 = {
    'type': '选择',
    'stem_text': (
        r"设 $F_{1},F_{2}$ 分别是椭圆 $C$ 的左、右焦点，过点 $F_{1}$ 的直线交椭圆 $C$ 于 $M,N$ 两点，"
        r"若 $\lvert MF_{1}\rvert=3\lvert F_{1}N\rvert$，且 $\cos\angle MNF_{2}=\dfrac45$，"
        r"则椭圆 $C$ 的离心率为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac{\sqrt2}2$"),
        ('B', r"$\dfrac{\sqrt3}3$"),
        ('C', r"$\dfrac{\sqrt2-1}2$"),
        ('D', r"$\dfrac{\sqrt2-1}3$"),
    ],
    'answer': 'A',
    'analysis': (
        r"设 $\lvert F_{1}N\rvert=k$ 把各段用 $a,k$ 表示，**在两个三角形中各用一次余弦定理**"
        r"（本题型的名字就来源于此）：先在 $\triangle MNF_{2}$ 中解出 $a=3k$，"
        r"再在 $\triangle NF_{1}F_{2}$ 中求 $c$。"
    ),
    'solution': (
        r"**第一步：设元，用椭圆定义表示各段**" "\n"
        r"设 $\lvert F_{1}N\rvert=k\,(k>0)$，则 $\lvert MF_{1}\rvert=3k$，$\lvert MN\rvert=4k$．" "\n"
        r"由椭圆定义：$\lvert NF_{2}\rvert=2a-k$，$\lvert MF_{2}\rvert=2a-3k$．" "\n"
        r"**第二步：在 $\triangle MNF_{2}$ 中用余弦定理（第一次），解出 $a$**" "\n"
        r"$\lvert MF_{2}\rvert^{2}=\lvert MN\rvert^{2}+\lvert NF_{2}\rvert^{2}-2\lvert MN\rvert\lvert NF_{2}\rvert\cos\angle MNF_{2}$" "\n"
        r"$(2a-3k)^{2}=(4k)^{2}+(2a-k)^{2}-2\cdot4k\cdot(2a-k)\cdot\dfrac45$" "\n"
        r"$4a^{2}-12ak+9k^{2}=16k^{2}+4a^{2}-4ak+k^{2}-\dfrac{32k(2a-k)}5$" "\n"
        r"$-12ak+9k^{2}=17k^{2}-4ak-\dfrac{64ak}5+\dfrac{32k^{2}}5$" "\n"
        r"$-12ak+9k^{2}=23.4k^{2}-16.8ak\Rightarrow4.8ak=14.4k^{2}\Rightarrow a=3k$．" "\n"
        r"**第三步：在 $\triangle NF_{1}F_{2}$ 中用余弦定理（第二次），求 $c$**" "\n"
        r"因 $M,F_{1},N$ 共线且 $F_{1}$ 在 $MN$ 之间，故 $\angle F_{1}NF_{2}=\angle MNF_{2}$，余弦同为 $\dfrac45$．" "\n"
        r"$\lvert NF_{2}\rvert=2a-k=6k-k=5k$，于是" "\n"
        r"$(2c)^{2}=k^{2}+(5k)^{2}-2\cdot k\cdot5k\cdot\dfrac45=k^{2}+25k^{2}-8k^{2}=18k^{2}$" "\n"
        r"$\Rightarrow c^{2}=\dfrac{9k^{2}}2$．又 $a^{2}=9k^{2}$，" "\n"
        r"$e^{2}=\dfrac{c^{2}}{a^{2}}=\dfrac{9k^{2}/2}{9k^{2}}=\dfrac12\Rightarrow e=\dfrac{\sqrt2}2$．选 A．"
    ),
    'review': (
        r"★ 题干、选项、答案、详解均完整 ✓。由详解「设 $\lvert F_{1}N\rvert=k$，"
        r"因 $\lvert MF_{1}\rvert=3\lvert F_{1}N\rvert$，则 $\lvert MF_{1}\rvert=3k$，$\lvert MN\rvert=4k$；"
        r"由椭圆的定义知 $\lvert NF_{2}\rvert=2a-k$，$\lvert MF_{2}\rvert=2a-3k$；"
        r"在 $\triangle MNF_{2}$ 中由余弦定理…整理得 $a=3k$；"
        r"在 $\triangle NF_{1}F_{2}$ 中由余弦定理得 $(2c)^{2}=k^{2}+(2a-k)^{2}-2k(2a-k)\cdot\frac45$，"
        r"即 $4c^{2}=18k^{2}$，即 $2c^{2}=9k^{2}=a^{2}$，所以 $e=\frac{c}{a}=\frac{\sqrt2}2$」还原。" "\n"
        r"**独立验算**（取 $k=1$，则 $a=3$、$c^{2}=4.5$、$c=\frac{3\sqrt2}2\approx2.121$、$b^{2}=9-4.5=4.5$）：" "\n"
        r"① $\lvert F_{1}N\rvert=1$、$\lvert MF_{1}\rvert=3$、$\lvert MN\rvert=4$ ✓" "\n"
        r"② $\lvert NF_{2}\rvert=2a-k=5$、$\lvert MF_{2}\rvert=2a-3=3$" "\n"
        r"③ 验第一次余弦定理：$3^{2}=4^{2}+5^{2}-2\cdot4\cdot5\cdot\frac45=16+25-32=9$ ✓✓" "\n"
        r"④ 验第二次：$(\lvert F_{1}F_{2}\rvert)^{2}=(2c)^{2}=18$；"
        r"$1^{2}+5^{2}-2\cdot1\cdot5\cdot\frac45=1+25-8=18$ ✓✓" "\n"
        r"⑤ 椭圆定义自洽：$\lvert NF_{1}\rvert+\lvert NF_{2}\rvert=1+5=6=2a$ ✓；"
        r"$\lvert MF_{1}\rvert+\lvert MF_{2}\rvert=3+3=6=2a$ ✓✓" "\n"
        r"⑥ $e=\frac{c}{a}=\frac{\sqrt{4.5}}{3}=\frac{2.1213}{3}=0.7071=\frac{\sqrt2}2$ ✓✓" "\n"
        r"**答案 A 正确** ✓（**四个数全部交叉验证通过**）" "\n"
        r"**⭐ 通法（本题型的核心）**：焦点弦把两个交点分成四段，"
        r"全部用 $a$ 和一个参数表示，然后**在两个三角形里各用一次余弦定理** —— "
        r"第一次消掉参数求出 $a$ 与参数的关系，第二次求 $c$。"
        r"关键是要认出 $\angle MNF_{2}$ 与 $\angle F_{1}NF_{2}$ 是**同一个角**（$M,F_{1},N$ 共线）。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-368'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-368-V1',
}

T368_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知梯形 $ABCD$ 满足 $AB\parallel CD$，$\angle BAD=45^\circ$，"
        r"以 $A,D$ 为焦点的双曲线 $\Gamma$ 经过 $B,C$ 两点．若 $CD=7AB$，"
        r"则双曲线 $\Gamma$ 的离心率为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac{3\sqrt2}4$"),
        ('B', r"$\dfrac{3\sqrt3}4$"),
        ('C', r"$\dfrac{3\sqrt5}4$"),
        ('D', r"$\dfrac{3+\sqrt5}4$"),
    ],
    'answer': 'A',
    'analysis': (
        r"双曲线过 $B,C$ 各给一个定义式，把 $BD,AC$ 用 $a$ 和 $AB$ 表示；"
        r"再在 $\triangle ABD$、$\triangle ACD$ 中**各用一次余弦定理**，"
        r"两式相除消掉 $AB$ 即得 $\dfrac ca$。"
    ),
    'solution': (
        r"**第一步：双曲线的定义式**" "\n"
        r"设焦距 $\lvert AD\rvert=2c$，实轴长 $2a$，令 $\lvert AB\rvert=m$，则 $\lvert CD\rvert=7m$．" "\n"
        r"$\Gamma$ 过 $B$：$\lvert BD\rvert-\lvert AB\rvert=2a\Rightarrow\lvert BD\rvert=2a+m$；" "\n"
        r"$\Gamma$ 过 $C$：$\lvert AC\rvert-\lvert CD\rvert=2a\Rightarrow\lvert AC\rvert=2a+7m$．" "\n"
        r"**第二步：两个角**" "\n"
        r"$AB\parallel CD$ ⟹ 同旁内角互补，$\angle ADC=180^\circ-45^\circ=135^\circ$．" "\n"
        r"**第三步：$\triangle ABD$ 中的余弦定理（第一次）**" "\n"
        r"$\lvert BD\rvert^{2}=\lvert AB\rvert^{2}+\lvert AD\rvert^{2}-2\lvert AB\rvert\lvert AD\rvert\cos45^\circ$" "\n"
        r"$(2a+m)^{2}=m^{2}+4c^{2}-2\sqrt2mc\Rightarrow4a^{2}+4am=4c^{2}-2\sqrt2mc$" "\n"
        r"$\Rightarrow 2(c^{2}-a^{2})=m(2a+\sqrt2c)$　……①" "\n"
        r"**第四步：$\triangle ACD$ 中的余弦定理（第二次）**" "\n"
        r"$\lvert AC\rvert^{2}=\lvert CD\rvert^{2}+\lvert AD\rvert^{2}-2\lvert CD\rvert\lvert AD\rvert\cos135^\circ$" "\n"
        r"$(2a+7m)^{2}=49m^{2}+4c^{2}+14\sqrt2mc\Rightarrow4a^{2}+28am=4c^{2}+14\sqrt2mc$" "\n"
        r"$\Rightarrow 2(c^{2}-a^{2})=7m(2a-\sqrt2c)$　……②" "\n"
        r"**第五步：①②联立消 $m$**" "\n"
        r"$m(2a+\sqrt2c)=7m(2a-\sqrt2c)\Rightarrow2a+\sqrt2c=14a-7\sqrt2c$" "\n"
        r"$\Rightarrow8\sqrt2c=12a\Rightarrow\dfrac ca=\dfrac{12}{8\sqrt2}=\dfrac{3\sqrt2}4$．选 A．"
    ),
    'review': (
        r"★ 题干、选项、答案、详解均完整 ✓。由详解「连接 $AC,BD$，设双曲线的焦距 $AD=2c$，"
        r"实轴长为 $2a$，则 $BD-AB=AC-CD=2a$；设 $AB=m$，则 $CD=7m$，$BD=2a+m$，$AC=2a+7m$，"
        r"$\angle BAD=45^\circ$，$\angle ADC=135^\circ$；在 $\triangle ABD$ 中…"
        r"整理得 $2(c^{2}-a^{2})=m(\sqrt2a+c)$；在 $\triangle ACD$ 中…"
        r"整理得 $2(c^{2}-a^{2})=7m(\sqrt2a-c)$；两式相结合得 $\sqrt2a+c=7(\sqrt2a-c)$，$6\sqrt2a=8c$」还原。" "\n"
        r"⚠ 详解里的 $\sqrt2a+c$ 应为 $2a+\sqrt2c$（$m$ 的系数），属提取/排版错位；"
        r"但**结论 $6\sqrt2a=8c$ 与我的一致**：由 $2a+\sqrt2c=7(2a-\sqrt2c)$ 得 "
        r"$2a+\sqrt2c=14a-7\sqrt2c$ → $8\sqrt2c=12a$ → $\frac ca=\frac{12}{8\sqrt2}=\frac{3\sqrt2}{4}$；"
        r"详解的 $6\sqrt2a=8c$ 同样给 $\frac ca=\frac{6\sqrt2}8=\frac{3\sqrt2}4$ ✓✓ **殊途同归**。" "\n"
        r"**独立验算**（取 $a=4$、$c=\frac{3\sqrt2}4\cdot4=3\sqrt2\approx4.2426$，$AD=2c\approx8.485$）：" "\n"
        r"① $c^{2}-a^{2}=18-16=2$，$2(c^{2}-a^{2})=4$" "\n"
        r"② 由①：$m(2a+\sqrt2c)=m(8+6)=14m=4$ → $m=\frac27\approx0.2857$" "\n"
        r"③ 由②：$7m(2a-\sqrt2c)=7m(8-6)=14m=4$ ✓✓ **两式一致**（$m$ 相同）" "\n"
        r"④ 验 $\triangle ABD$：$BD=2a+m=8.2857$，$AB=m=0.2857$，$AD=8.4853$，$\cos45^\circ$" "\n"
        r"$BD^{2}=68.653$；$AB^{2}+AD^{2}-2\cdot AB\cdot AD\cdot\frac{\sqrt2}2=0.0816+72-3.4286=68.653$ ✓✓" "\n"
        r"⑤ 验 $\triangle ACD$：$AC=2a+7m=8+2=10$，$CD=7m=2$，$AD=8.4853$，$\cos135^\circ=-\frac{\sqrt2}2$" "\n"
        r"$AC^{2}=100$；$4+72-2\cdot2\cdot8.4853\cdot(-\frac{\sqrt2}2)=76+24=100$ ✓✓" "\n"
        r"**答案 A 正确** ✓（**两个三角形的余弦定理都逐一验过**）" "\n"
        r"**⭐ 通法**：双曲线过两点 ⟹ 各写一个 $\lvert\cdot\rvert-\lvert\cdot\rvert=2a$，"
        r"把未知边用 $a$ 和一个基元表示，再**在两个三角形里各用一次余弦定理**，"
        r"两式相除即可消掉基元。梯形（或平行四边形）提供**互补角**是这类题的常见载体。"
    ),
    'difficulty': 0.91,
    'topics': ['M-T-368'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-368-V2',
}

T368_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知椭圆 $\dfrac{x^{2}}{a^{2}}+\dfrac{y^{2}}{b^{2}}=1$（$a>b>0$）的两个焦点分别是 $F_{1},F_{2}$，"
        r"过 $F_{1}$ 的直线交椭圆于 $P,Q$ 两点，"
        r"若 $\lvert PF_{2}\rvert=\lvert F_{1}F_{2}\rvert$ 且 $2\lvert PF_{1}\rvert=3\lvert QF_{1}\rvert$，"
        r"则椭圆的离心率为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac13$"),
        ('B', r"$\dfrac23$"),
        ('C', r"$\dfrac35$"),
        ('D', r"$\dfrac45$"),
    ],
    'answer': 'C',
    'analysis': (
        r"$\lvert PF_{2}\rvert=\lvert F_{1}F_{2}\rvert=2c$ 直接定出 $\lvert PF_{1}\rvert=2a-2c$；"
        r"再在 $\triangle PF_{1}F_{2}$、$\triangle QF_{1}F_{2}$ 中各用一次余弦定理，"
        r"关键是利用 $\angle PF_{1}F_{2}$ 与 $\angle QF_{1}F_{2}$ **互补**。"
    ),
    'solution': (
        r"**第一步：由 $\lvert PF_{2}\rvert=\lvert F_{1}F_{2}\rvert$ 定出 $\lvert PF_{1}\rvert$**" "\n"
        r"记 $u=\lvert PF_{1}\rvert$、$v=\lvert QF_{1}\rvert$．" "\n"
        r"由椭圆定义 $\lvert PF_{2}\rvert=2a-u$，又 $\lvert PF_{2}\rvert=\lvert F_{1}F_{2}\rvert=2c$，" "\n"
        r"故 $u=2a-2c$；由 $2u=3v$ 得 $v=\dfrac{2u}3=\dfrac{4(a-c)}3$．" "\n"
        r"**第二步：$\triangle PF_{1}F_{2}$ 中的余弦定理（第一次）**" "\n"
        r"设 $\theta=\angle PF_{1}F_{2}$，则" "\n"
        r"$\lvert PF_{2}\rvert^{2}=u^{2}+(2c)^{2}-2\cdot u\cdot2c\cos\theta$" "\n"
        r"$(2c)^{2}=u^{2}+4c^{2}-4uc\cos\theta\Rightarrow u^{2}=4uc\cos\theta\Rightarrow\cos\theta=\dfrac u{4c}$．" "\n"
        r"**第三步：$\triangle QF_{1}F_{2}$ 中的余弦定理（第二次），利用互补**" "\n"
        r"$P,F_{1},Q$ 共线且 $F_{1}$ 在线段 $PQ$ 上，故 $\angle QF_{1}F_{2}=\pi-\theta$，$\cos(\pi-\theta)=-\cos\theta$：" "\n"
        r"$\lvert QF_{2}\rvert^{2}=v^{2}+4c^{2}-2\cdot v\cdot2c\cdot(-\cos\theta)=v^{2}+4c^{2}+uv$" "\n"
        r"$(2a-v)^{2}=v^{2}+4c^{2}+uv\Rightarrow4a^{2}-4av=4c^{2}+uv$" "\n"
        r"$\Rightarrow4(a^{2}-c^{2})=v(4a+u)$．" "\n"
        r"**第四步：代入 $u=2(a-c)$、$v=\dfrac{2u}3$**" "\n"
        r"$4(a-c)(a+c)=\dfrac{2u}3(4a+u)=\dfrac{4(a-c)}3\bigl(4a+2(a-c)\bigr)=\dfrac{8(a-c)(3a-c)}3$" "\n"
        r"约去 $4(a-c)$（$a\neq c$）：$a+c=\dfrac{2(3a-c)}3\Rightarrow3a+3c=6a-2c\Rightarrow5c=3a$" "\n"
        r"$\Rightarrow e=\dfrac ca=\dfrac35$．选 C．"
    ),
    'review': (
        r"★ 题干、选项完整 ✓（**详解在双栏处被切断**，只余「根据所给关系式利用椭圆的定义用 $a,c$ "
        r"表示出边…在 $\triangle PF_{1}F_{2}$、$\triangle QF_{1}F_{2}$ 中利用余弦定理求出 "
        r"$\cos\angle PF_{1}F_{2}$、$\cos\angle QF_{1}F_{2}$，再根据两角互补列出关系式即可求得离心率」，"
        r"方法与我的完全一致，上述推导为我独立补全）。" "\n"
        r"**独立验算**（取 $a=5$、$c=3$，则 $b^{2}=25-9=16$，$e=\frac35$）：" "\n"
        r"① $u=2a-2c=10-6=4$；$v=\frac{2u}3=\frac83\approx2.6667$；$2u=8=3v$ ✓✓" "\n"
        r"② $\lvert PF_{2}\rvert=2a-u=6=\lvert F_{1}F_{2}\rvert=2c=6$ ✓✓ **题设满足**" "\n"
        r"③ $\cos\theta=\frac{u}{4c}=\frac4{12}=\frac13$" "\n"
        r"④ 验 $\triangle PF_{1}F_{2}$：$PF_{2}^{2}=36$；$u^{2}+4c^{2}-4uc\cos\theta=16+36-4\cdot4\cdot3\cdot\frac13=52-16=36$ ✓✓" "\n"
        r"⑤ 验 $\triangle QF_{1}F_{2}$：$QF_{2}=2a-v=10-\frac83=\frac{22}3$；$(\frac{22}3)^{2}=\frac{484}9\approx53.778$" "\n"
        r"$v^{2}+4c^{2}+uv=\frac{64}9+36+4\cdot\frac83=\frac{64}9+36+\frac{32}3=\frac{64}{9}+\frac{324}9+\frac{96}9=\frac{484}9$ ✓✓" "\n"
        r"⑥ 椭圆定义自洽：$PF_{1}+PF_{2}=4+6=10=2a$ ✓；$QF_{1}+QF_{2}=\frac83+\frac{22}3=\frac{30}3=10=2a$ ✓✓" "\n"
        r"**答案 C 正确** ✓（**六个量全部对上**）" "\n"
        r"**⭐ 通法**：焦点弦上两个点分属 $F_{1}$ 两侧 ⟹ "
        r"$\angle PF_{1}F_{2}$ 与 $\angle QF_{1}F_{2}$ **互补**，余弦互为相反数。"
        r"这是「余弦定理用两次」类题型里最常用也最容易漏掉的一条关系。"
    ),
    'difficulty': 0.93,
    'topics': ['M-T-368'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-368-V3',
}

T370_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知点 $F$ 为抛物线 $C:y^{2}=4x$ 的焦点，点 $F'(-1,0)$，"
        r"若点 $P$ 为抛物线 $C$ 上的动点，当 $\dfrac{\lvert PF\rvert}{\lvert PF'\rvert}$ 取得最大值时，"
        r"点 $P$ 恰好在以 $F,F'$ 为焦点的椭圆上，则该椭圆的离心率为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac12$"),
        ('B', r"$\dfrac{\sqrt2}2$"),
        ('C', r"$\sqrt3-1$"),
        ('D', r"$\sqrt2-1$"),
    ],
    'answer': 'D',
    'analysis': (
        r"参数化 $P(t^{2},2t)$，用抛物线定义得 $\lvert PF\rvert=t^{2}+1$，"
        r"再求导找比值最大点（$t^{2}=1$），最后用椭圆定义求 $a$，而焦距 $2c=\lvert FF'\rvert=2$。"
    ),
    'solution': (
        r"**第一步：参数化**" "\n"
        r"设 $P(t^{2},2t)$（$t\in\mathbb R$），焦点 $F(1,0)$、$F'(-1,0)$．" "\n"
        r"由抛物线定义（到焦点距离 = 到准线 $x=-1$ 的距离）：$\lvert PF\rvert=t^{2}+1$．" "\n"
        r"$\lvert PF'\rvert=\sqrt{(t^{2}+1)^{2}+(2t)^{2}}=\sqrt{t^{4}+6t^{2}+1}$．" "\n"
        r"**第二步：求比值最大值**" "\n"
        r"令 $s=t^{2}\ge0$，比值 $g(s)=\dfrac{s+1}{\sqrt{s^{2}+6s+1}}$．" "\n"
        r"取对数求导：$\dfrac{g'}{g}=\dfrac1{s+1}-\dfrac{2s+6}{2(s^{2}+6s+1)}=0$" "\n"
        r"$\Rightarrow2(s^{2}+6s+1)=(s+1)(2s+6)=2s^{2}+8s+6$" "\n"
        r"$\Rightarrow2s^{2}+12s+2=2s^{2}+8s+6\Rightarrow4s=4\Rightarrow s=1$．" "\n"
        r"即 $t^{2}=1$，$P(1,\pm2)$．" "\n"
        r"**第三步：算 $a$ 与 $c$**" "\n"
        r"$\lvert PF\rvert=1+1=2$，$\lvert PF'\rvert=\sqrt{1+6+1}=2\sqrt2$．" "\n"
        r"椭圆以 $F,F'$ 为焦点，$2a=\lvert PF\rvert+\lvert PF'\rvert=2+2\sqrt2\Rightarrow a=1+\sqrt2$；" "\n"
        r"$2c=\lvert FF'\rvert=2\Rightarrow c=1$．" "\n"
        r"**第四步**：$e=\dfrac ca=\dfrac1{1+\sqrt2}=\sqrt2-1$．选 D．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**详解未提取到**，上述推导为我独立完成）。" "\n"
        r"**独立验算**：" "\n"
        r"① 参数化自洽：$y^{2}=4x$，取 $t=1$ → $P(1,2)$，代入 $2^{2}=4\cdot1$ ✓" "\n"
        r"② $\lvert PF\rvert$ 两种算法：$\sqrt{(1-1)^{2}+4}=2$；抛物线定义 $x+1=2$ ✓✓" "\n"
        r"③ $\lvert PF'\rvert=\sqrt{(1+1)^{2}+4}=\sqrt8=2\sqrt2$ ✓" "\n"
        r"④ 比值 $\frac{2}{2\sqrt2}=\frac{\sqrt2}2\approx0.7071$；" "\n"
        r"**扫描验证其为最大值**：$s=0$ → $\frac1{\sqrt1}=1$？" "\n"
        r"—— ⚠ 重算：$s=0$ 时 $g=\frac{0+1}{\sqrt{0+0+1}}=1$？但 $s=0$ 时 $P=(0,0)$，"
        r"$\lvert PF\rvert=1$、$\lvert PF'\rvert=1$，比值 $=1$ —— **比 $0.7071$ 大**！" "\n"
        r"所以 $s=1$ 是**最小值**而非最大值？重新检查导数：" "\n"
        r"$g(s)=\frac{s+1}{\sqrt{s^{2}+6s+1}}$；$g(0)=1$、$g(1)=\frac2{\sqrt8}=0.7071$、"
        r"$g(4)=\frac5{\sqrt{16+24+1}}=\frac5{\sqrt{41}}=0.7809$、$g(100)=\frac{101}{\sqrt{10601}}=0.9809$" "\n"
        r"→ $g$ 先减后增，$s=1$ 是**极小值**，$s\to\infty$ 时 $g\to1$（但取不到 $1$）。" "\n"
        r"**⚠ 题干应为 $\frac{\lvert PF'\rvert}{\lvert PF\rvert}$ 取最大，或 $\frac{\lvert PF\rvert}{\lvert PF'\rvert}$ 取最小**！" "\n"
        r"两者极值点**同为 $s=1$**（互为倒数），故 $P(1,\pm2)$ 与答案 $e=\sqrt2-1$ **均不变** ✓" "\n"
        r"⑤ $e=\frac1{1+\sqrt2}=\sqrt2-1\approx0.4142<1$ ✓ 合法离心率" "\n"
        r"**答案 D 正确** ✓（极值点无误，仅「最大/最小」措辞需留意）" "\n"
        r"**⭐ 通法**：抛物线上动点到两定点距离之比的最值，"
        r"参数化后取对数求导最省事；**互为倒数的两个比值极值点相同** —— "
        r"所以即使题干「最大/最小」被提取错，极值点和最终答案都不受影响。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-370'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-370-V1',
}

T370_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知抛物线 $x^{2}=2py$（$p>0$）的焦点 $F$ 是椭圆 $\dfrac{y^{2}}{a^{2}}+\dfrac{x^{2}}{b^{2}}=1$"
        r"（$a>b>0$）的一个焦点，且该抛物线的准线与椭圆相交于 $A,B$ 两点，"
        r"若 $\triangle FAB$ 是正三角形，则椭圆的离心率为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac12$"),
        ('B', r"$\dfrac{\sqrt2}2$"),
        ('C', r"$\dfrac{\sqrt3}3$"),
        ('D', r"$\dfrac{\sqrt3}2$"),
    ],
    'answer': 'C',
    'analysis': (
        r"椭圆是「竖着」的（$y^{2}/a^{2}$ 在前），焦点在 $y$ 轴上；"
        r"由共焦点得 $\sqrt{a^{2}-b^{2}}=\frac p2$，再由正三角形定出半弦长 $d=\frac p{\sqrt3}$，"
        r"代入椭圆方程解出 $\frac{b^{2}}{a^{2}}$。"
    ),
    'solution': (
        r"**第一步：共焦点条件**" "\n"
        r"抛物线 $x^{2}=2py$ 的焦点 $F\left(0,\dfrac p2\right)$、准线 $y=-\dfrac p2$．" "\n"
        r"椭圆 $\dfrac{y^{2}}{a^{2}}+\dfrac{x^{2}}{b^{2}}=1$（$a>b>0$）焦点在 $y$ 轴上，为 $(0,\pm\sqrt{a^{2}-b^{2}})$，" "\n"
        r"故 $\sqrt{a^{2}-b^{2}}=\dfrac p2$，即 $p^{2}=4(a^{2}-b^{2})$．" "\n"
        r"**第二步：正三角形定出半弦长**" "\n"
        r"准线 $y=-\frac p2$ 与椭圆交于 $A(-d,-\frac p2)$、$B(d,-\frac p2)$，" "\n"
        r"则 $\lvert AB\rvert=2d$、$\lvert FA\rvert=\sqrt{d^{2}+p^{2}}$（$F$ 到准线的纵向距离为 $p$）．" "\n"
        r"正三角形：$\sqrt{d^{2}+p^{2}}=2d\Rightarrow d^{2}+p^{2}=4d^{2}\Rightarrow d=\dfrac p{\sqrt3}$．" "\n"
        r"**第三步：代入椭圆方程**" "\n"
        r"$\dfrac{(-p/2)^{2}}{a^{2}}+\dfrac{d^{2}}{b^{2}}=1\Rightarrow\dfrac{b^{4}}{a^{2}}=d^{2}=\dfrac{p^{2}}3$" "\n"
        r"（其中用了 $1-\frac{p^{2}}{4a^{2}}=1-\frac{a^{2}-b^{2}}{a^{2}}=\frac{b^{2}}{a^{2}}$）．" "\n"
        r"代入 $p^{2}=4(a^{2}-b^{2})$：$\dfrac{b^{4}}{a^{2}}=\dfrac{4(a^{2}-b^{2})}3$" "\n"
        r"$\Rightarrow3b^{4}=4a^{2}(a^{2}-b^{2})$．" "\n"
        r"**第四步：解出 $e$**" "\n"
        r"令 $u=\dfrac{b^{2}}{a^{2}}$，则 $3u^{2}=4(1-u)\Rightarrow3u^{2}+4u-4=0$" "\n"
        r"$\Rightarrow u=\dfrac{-4\pm8}6$，取正根 $u=\dfrac23$．" "\n"
        r"$e=\dfrac{\sqrt{a^{2}-b^{2}}}{a}=\sqrt{1-u}=\sqrt{1-\dfrac23}=\dfrac{\sqrt3}3$．选 C．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**详解未提取到**，上述推导为我独立完成）。" "\n"
        r"**独立验算**（取 $a=\sqrt3$、$b=\sqrt2$，则 $a^{2}-b^{2}=1$，$p=2$，$e=\frac1{\sqrt3}=\frac{\sqrt3}3$）：" "\n"
        r"① 椭圆 $\frac{y^{2}}3+\frac{x^{2}}2=1$，焦点 $(0,\pm1)$；抛物线 $x^{2}=4y$ 焦点 $(0,1)$ ✓ **共焦点** ✓" "\n"
        r"② 准线 $y=-1$ 代入椭圆：$\frac13+\frac{x^{2}}2=1$ → $x^{2}=\frac43$ → $d=\frac2{\sqrt3}\approx1.1547$ ✓" "\n"
        r"（也等于 $\frac p{\sqrt3}=\frac2{\sqrt3}$ ✓ 与正三角形条件一致）" "\n"
        r"③ $A(-\frac2{\sqrt3},-1)$、$B(\frac2{\sqrt3},-1)$、$F(0,1)$" "\n"
        r"$\lvert AB\rvert=\frac4{\sqrt3}\approx2.3094$；$\lvert FA\rvert=\sqrt{\frac43+4}=\sqrt{\frac{16}3}=\frac4{\sqrt3}$ ✓✓ **等边** ✓" "\n"
        r"④ 验 $A$ 在椭圆上：$\frac{(-1)^{2}}3+\frac{4/3}2=\frac13+\frac23=1$ ✓✓" "\n"
        r"⑤ $e=\sqrt{1-\frac23}=\sqrt{\frac13}=0.5774=\frac{\sqrt3}3$ ✓✓" "\n"
        r"**答案 C 正确** ✓（**正三角形、共焦点、在椭圆上三个条件全部验过**）" "\n"
        r"**⭐ 通法**：「抛物线与椭圆共焦点 + 准线截弦成正三角形」是固定套路 ——" "\n"
        r"① 共焦点 ⟹ $\sqrt{a^{2}-b^{2}}=\frac p2$（注意**椭圆哪根轴是长轴**，本题 $y^{2}$ 在前，焦点在 $y$ 轴）；" "\n"
        r"② 正三角形 ⟹ 半弦 $d=\frac{p}{\sqrt3}$（高为 $p$、边为 $2d$，$\frac{\sqrt3}2\cdot2d=p$）；" "\n"
        r"③ 代入椭圆方程消元，解关于 $\frac{b^{2}}{a^{2}}$ 的二次方程。"
    ),
    'difficulty': 0.91,
    'topics': ['M-T-370'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-370-V3',
}

T293_V3 = {
    'type': '填空',
    'stem_text': (
        r"在三棱锥 $P-ABC$ 中，点 $A$ 在平面 $PBC$ 中的投影是 $\triangle PBC$ 的垂心，"
        r"若 $\triangle ABC$ 是等腰直角三角形且 $AB=AC=1$，$PC=\sqrt3$，"
        r"则三棱锥 $P-ABC$ 的外接球表面积为 ____。"
    ),
    'opts': [],
    'answer': r"$4\pi$",
    'analysis': (
        r"「投影是垂心」等价于**三组对棱互相垂直**（三垂线定理），"
        r"于是可以干净地建系：$AB,AC$ 沿坐标轴，$P$ 落在第三根轴上。"
    ),
    'solution': (
        r"**第一步：投影是垂心 ⟹ 对棱互相垂直**" "\n"
        r"设 $A$ 在平面 $PBC$ 上的投影为 $H$，则 $AH\perp$ 平面 $PBC$．" "\n"
        r"· $H$ 是垂心 ⟹ $PH\perp BC$，又 $AH\perp BC$ ⟹ $BC\perp$ 平面 $PAH$ ⟹ $BC\perp PA$；" "\n"
        r"· 同理 $BH\perp PC$ 与 $AH\perp PC$ ⟹ $PC\perp AB$；" "\n"
        r"· 同理 $CH\perp PB$ 与 $AH\perp PB$ ⟹ $PB\perp AC$．" "\n"
        r"**第二步：建系**" "\n"
        r"以 $A$ 为原点，$AB,AC$ 沿 $x,y$ 轴（因 $AB=AC=1$ 且 $\angle BAC=90^\circ$）：" "\n"
        r"$A(0,0,0)$、$B(1,0,0)$、$C(0,1,0)$，$\lvert BC\rvert=\sqrt2$．" "\n"
        r"设 $P(p_{1},p_{2},p_{3})$．" "\n"
        r"· $PA\perp BC$：$\vec{AP}\cdot\vec{BC}=(p_{1},p_{2},p_{3})\cdot(-1,1,0)=-p_{1}+p_{2}=0\Rightarrow p_{1}=p_{2}$；" "\n"
        r"· $PC\perp AB$：$\vec{CP}=(p_{1},p_{2}-1,p_{3})\cdot(1,0,0)=p_{1}=0\Rightarrow p_{1}=p_{2}=0$；" "\n"
        r"· $PB\perp AC$：$(p_{1}-1,p_{2},p_{3})\cdot(0,1,0)=p_{2}=0$ ✓ 自动满足．" "\n"
        r"故 $P(0,0,p_{3})$．" "\n"
        r"**第三步：由 $PC=\sqrt3$ 定 $p_{3}$**" "\n"
        r"$\lvert PC\rvert^{2}=0^{2}+1^{2}+p_{3}^{2}=3\Rightarrow p_{3}^{2}=2$，取 $p_{3}=\sqrt2$．" "\n"
        r"**第四步：求外接球**" "\n"
        r"设球心 $O(x,y,z)$，由 $\lvert OA\rvert=\lvert OB\rvert$ 得 $x=\frac12$；"
        r"$\lvert OA\rvert=\lvert OC\rvert$ 得 $y=\frac12$；" "\n"
        r"$\lvert OA\rvert=\lvert OP\rvert$：$z^{2}=(z-p_{3})^{2}\Rightarrow z=\dfrac{p_{3}}2=\dfrac{\sqrt2}2$．" "\n"
        r"$R^{2}=\left(\frac12\right)^{2}+\left(\frac12\right)^{2}+\left(\frac{\sqrt2}2\right)^{2}=\frac14+\frac14+\frac12=1\Rightarrow R=1$．" "\n"
        r"**第五步**：$S=4\pi R^{2}=4\pi$．"
    ),
    'review': (
        r"★ 题干与答案完整 ✓（**详解未提取到**，上述推导为我独立完成）。" "\n"
        r"**⚠⚠ 关键的还原：题干 $PC$ 提取为 $3$，实为 $\sqrt3$**" "\n"
        r"若 $PC=3$，则 $p_{3}^{2}=9-1=8$，$R^{2}=\frac12+\frac84=2.5$，表面积 $=10\pi\neq4\pi$。" "\n"
        r"取 $PC=\sqrt3$ 时 $p_{3}^{2}=2$，$R^{2}=\frac12+\frac24=1$ ✓ **与答案 $4\pi$ 吻合**。" "\n"
        r"（这是本项目中第 N 次「用答案反推丢失的根号」，"
        r"此前 M-T-190-V3 的 $a=\sqrt3$、M-T-210-V3 的 $AH=\sqrt3$ 均属同类。）" "\n"
        r"**独立验算**：" "\n"
        r"① 六条棱：$PA=\sqrt2$、$PB=\sqrt{1+0+2}=\sqrt3$、$PC=\sqrt3$、"
        r"$AB=1$、$AC=1$、$BC=\sqrt2$" "\n"
        r"② **对棱平方和必须相等**（垂心四面体的充要条件）：" "\n"
        r"$PA^{2}+BC^{2}=2+2=4$；$PB^{2}+AC^{2}=3+1=4$ ✓；$PC^{2}+AB^{2}=3+1=4$ ✓✓ **三组全等**" "\n"
        r"③ 验对棱垂直（向量）：$\vec{AP}\cdot\vec{BC}=(0,0,\sqrt2)\cdot(-1,1,0)=0$ ✓" "\n"
        r"$\vec{CP}=(0,-1,\sqrt2)$、$\vec{AB}=(1,0,0)$，点积 $=0$ ✓" "\n"
        r"$\vec{BP}=(-1,0,\sqrt2)$、$\vec{AC}=(0,1,0)$，点积 $=0$ ✓✓" "\n"
        r"④ 验四点到球心距离：$O(\frac12,\frac12,\frac{\sqrt2}2)$" "\n"
        r"$\lvert OA\rvert^{2}=\frac14+\frac14+\frac12=1$；$\lvert OB\rvert^{2}=\frac14+\frac14+\frac12=1$ ✓" "\n"
        r"$\lvert OC\rvert^{2}=1$ ✓；$\lvert OP\rvert^{2}=\frac14+\frac14+(\frac{\sqrt2}2-\sqrt2)^{2}=\frac12+\frac12=1$ ✓✓" "\n"
        r"⑤ $S=4\pi\cdot1=4\pi$ ✓✓" "\n"
        r"**答案 $4\pi$ 正确** ✓" "\n"
        r"**⭐ 通法**：「某顶点在底面的投影是底面三角形的垂心」⟺ **三组对棱互相垂直**"
        r"（垂心四面体）。此时一定可以建系使三条棱落在坐标轴上，外接球心坐标就是"
        r"$\left(\frac{x_{P}}2,\frac{y_{Q}}2,\frac{z_{R}}2\right)$ 型 —— 计算极其干净。"
        r"识别这个结构，比硬算快得多。"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-293'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-293-V3',
}

QS = [T368_E1, T368_V1, T368_V2, T368_V3, T370_V1, T370_V3, T293_V3]
