# -*- coding: utf-8 -*-
r"""第70批：解三角形形状判定·最值·范围（12 题）

来源：2024高中数学热点题型归纳完整解析版.pdf p154-157、p176-177
M-T-191（4）、M-T-194（4）、M-T-212（4）

## ★★ 12 题我全部独立验算，与原书答案全部吻合

| 题 | 我的验算 | 答案 |
|---|---|---|
| M-T-191-E1 | 三组等腰各代一组数（$a$=$b$、$b$=$c$、$a$=$c$）都成立；$3,4,5$ 与 $2,3,4$ 不成立 | **A** |
| M-T-191-V1 | 化到 $(a^2-b^2)(a^2+b^2-c^2)=0$，由 $a\ne b$ 得 $C=90^\circ$ | **C** |
| M-T-191-V2 | $c^2=b(a+b)>b^2$；$\sin C=\sin2B$ ⟹ $C=2B$；$A=B=45^\circ$ 时 $a<c$ | **AB** |
| M-T-191-V3 | ⭐ 三边长实为 $\sqrt a,\sqrt b,\sqrt c$；$\sqrt a+\sqrt b>\sqrt{a+b}>\sqrt c$ | **A** |
| M-T-194-E1 | 数值扫描 $A\approx1.22$ 得 $0.08839$，$\frac{\sqrt2}{16}=0.08839$ | **A** |
| M-T-194-V1 | $g(A)=\frac{5-4\cos A}{\sin A}$，导数为零于 $\cos A=\frac45$，$g=3$ ⟹ $BC=\sqrt3$ | **C** |
| M-T-194-V2 | ⭐ $4\sqrt3S=a^2$（`4 3S` 丢根号）；$b^2+c^2=2\sqrt2bc$ | **B** |
| M-T-194-V3 | $t=\sin B+\cos B\in(1,\sqrt2]$，$t-\frac1t\in(0,\frac{\sqrt2}2]$ | **B** |
| M-T-212-E1 | $t=\frac c b=\frac{1+\sqrt3}2$，$k_{\max}=1+\sqrt3$，$\sin C=\frac{\sqrt6+\sqrt2}4$ | **B** |
| M-T-212-V1 | $\frac cb+\frac bc=\sin A+2\cos A\le\sqrt5$；$\frac{bc}{a^2}=\frac1{\sin A}$ 是**最小**值 1 | **C** |
| M-T-212-V2 | $(a^2+b^2-c^2)^2=a^2b^2$、$\cos C=-\frac12$，非等腰 ⟹ 两端都开 | **A** |
| M-T-212-V3 | $d=\frac6{\sqrt{k^2+1}}\le4$ ⟹ $k^2\ge\frac54$ ⟹ $|k|\ge\frac{\sqrt5}2$ | **C** |

## 本批三处根号/条件还原

1. **M-T-191-V3**：题干是「三边长分别为 $\sqrt a,\sqrt b,\sqrt c$」，提取时三个根号全丢。
   若按字面（边长就是 $a,b,c$），则条件 $a^2=b^2+c^2-2bc\cos\theta$ 就是余弦定理本身，**恒成立**，题目无意义。
2. **M-T-194-V2**：`4 3S = a2` 实为 $4\sqrt3S=a^2$。
3. **M-T-212-V2**：由「非等腰」知 $ab<\frac{(a+b)^2}4$ 严格，故 $\frac{a+b}{2c}<\frac{\sqrt3}3$ 取不到，区间两端**都开**。
"""

T191_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知 $\triangle ABC$ 的三条边 $a,b,c$ 和与之对应的三个角 $A,B,C$ 满足等式"
        r"$a\cos B+b\cos C+c\cos A=b\cos A+c\cos B+a\cos C$，则此三角形的形状是（　　）"
    ),
    'opts': [
        ('A', r"等腰三角形"),
        ('B', r"直角三角形"),
        ('C', r"等腰或直角三角形"),
        ('D', r"等腰直角三角形"),
    ],
    'answer': 'A',
    'analysis': (
        r"代入余弦定理 $\cos A=\frac{b^{2}+c^{2}-a^{2}}{2bc}$ 等，注意 $a\cos B=\frac{a^{2}+c^{2}-b^{2}}{2c}$ 这种「边$\times$余弦」"
        r"会约掉一个边，整理后因式分解成 $(a-b)(b-c)(a-c)(a+b+c)=0$。"
    ),
    'solution': (
        r"由余弦定理 $a\cos B=a\cdot\dfrac{a^{2}+c^{2}-b^{2}}{2ac}=\dfrac{a^{2}+c^{2}-b^{2}}{2c}$，同理" "\n"
        r"$b\cos C=\dfrac{a^{2}+b^{2}-c^{2}}{2a}$，$c\cos A=\dfrac{b^{2}+c^{2}-a^{2}}{2b}$，" "\n"
        r"$b\cos A=\dfrac{b^{2}+c^{2}-a^{2}}{2c}$，$c\cos B=\dfrac{a^{2}+c^{2}-b^{2}}{2a}$，$a\cos C=\dfrac{a^{2}+b^{2}-c^{2}}{2b}$。" "\n"
        r"代入原等式，移项合并（把含同一分子的项放在一起）：" "\n"
        r"$(a^{2}+c^{2}-b^{2})\left(\dfrac1{2c}-\dfrac1{2a}\right)+(a^{2}+b^{2}-c^{2})\left(\dfrac1{2a}-\dfrac1{2b}\right)"
        r"+(b^{2}+c^{2}-a^{2})\left(\dfrac1{2b}-\dfrac1{2c}\right)=0$。" "\n"
        r"通分整理得 $\dfrac{a^{2}-b^{2}}c+\dfrac{b^{2}-c^{2}}a+\dfrac{c^{2}-a^{2}}b=0$，" "\n"
        r"进一步分解为 $\dfrac{(a-b)(b-c)(a-c)(a+b+c)}{abc}=0$。" "\n"
        r"因 $a,b,c>0$，故 $a+b+c>0$、$abc>0$，于是 $(a-b)(b-c)(a-c)=0$，" "\n"
        r"即 $a=b$ 或 $b=c$ 或 $a=c$ —— 三角形为**等腰三角形**。故选 A。"
    ),
    'review': (
        r"★ 题干、答案完整 ✓。原书 p154 详解给出分解结果 $(a-b)(b-c)(a-c)\cdot\frac{a+b+c}{abc}=0$，与我的推导一致 ✓✓✓" "\n"
        r"（⚠ 该页提取较乱，详解末尾被截断为「所以 $a=$」，但分解式与答案 A 已足够确认）" "\n"
        r"**独立验算（代入具体边长按选项逐一排除）**：" "\n"
        r"① **等腰 $a=b$**：取 $a=b=1$、$c=1.5$。" "\n"
        r"$\cos A=\cos B=\frac{1+2.25-1}{2\cdot1\cdot1.5}=\frac{2.25}{3}=0.75$；$\cos C=\frac{1+1-2.25}{2}=\frac{-0.25}2=-0.125$。" "\n"
        r"左 $=1(0.75)+1(-0.125)+1.5(0.75)=0.75-0.125+1.125=1.75$；" "\n"
        r"右 $=1(0.75)+1.5(0.75)+1(-0.125)=0.75+1.125-0.125=1.75$ ✓✓✓ **相等**" "\n"
        r"② **等腰 $b=c$**：取 $b=c=2$、$a=1$。" "\n"
        r"$\cos A=\frac{4+4-1}{2\cdot2\cdot2}=\frac78=0.875$；$\cos B=\cos C=\frac{1+4-4}{2\cdot1\cdot2}=0.25$。" "\n"
        r"左 $=1(0.25)+2(0.25)+2(0.875)=0.25+0.5+1.75=2.5$；" "\n"
        r"右 $=2(0.875)+2(0.25)+1(0.25)=1.75+0.5+0.25=2.5$ ✓✓✓ **相等**" "\n"
        r"③ **等腰 $a=c$**：取 $a=c=2$、$b=1$。$\cos A=\cos C=0.25$、$\cos B=0.875$。" "\n"
        r"左 $=2(0.875)+1(0.25)+2(0.25)=1.75+0.25+0.5=2.5$；" "\n"
        r"右 $=1(0.25)+2(0.875)+2(0.25)=0.25+1.75+0.5=2.5$ ✓✓✓ **相等**" "\n"
        r"④ **直角 $3,4,5$（非等腰）**：$\cos A=0.8$、$\cos B=0.6$、$\cos C=0$。" "\n"
        r"左 $=3(0.6)+4(0)+5(0.8)=1.8+4=5.8$；右 $=4(0.8)+5(0.6)+3(0)=3.2+3=6.2$ ✗ **不相等**" "\n"
        r"⑤ **一般斜三角形 $2,3,4$（非等腰非直角）**：$\cos A=0.875$、$\cos B=0.6875$、$\cos C=-0.25$。" "\n"
        r"左 $=2(0.6875)+3(-0.25)+4(0.875)=1.375-0.75+3.5=4.125$；" "\n"
        r"右 $=3(0.875)+4(0.6875)+2(-0.25)=2.625+2.75-0.5=4.875$ ✗ **不相等**" "\n"
        r"⑥ **结论**：等腰（三种都行）必满足；直角但不等边（$3,4,5$）不满足 —— " "\n"
        r"故 B「直角三角形」✗、C「等腰或直角三角形」✗（多含了纯直角）、D「等腰直角三角形」✗（太窄）。**A 正确** ✓" "\n"
        r"**⭐⭐ 通法（边$\times$余弦的化简技巧）**：" "\n"
        r"① ⭐⭐ **$a\cos B=\frac{a^{2}+c^{2}-b^{2}}{2c}$** —— 「边 $\times$ 邻角余弦」代入余弦定理后**会约掉分子里的一条边**，" "\n"
        r"剩下两项除以 $2\times$ 另一条边。记住这个约分，展开六项就不乱了；" "\n"
        r"② ⭐⭐ **射影定理的快捷验证**：$a\cos B+b\cos A=c$ 等三式恒成立，" "\n"
        r"本题等式是**循环错位**的（左 $a\cos B$、$b\cos C$、$c\cos A$；右 $b\cos A$、$c\cos B$、$a\cos C$），" "\n"
        r"所以不是恒等式，才需要条件；" "\n"
        r"③ ⭐ **因式分解的目标**：三个差 $(a-b)$、$(b-c)$、$(a-c)$ —— " "\n"
        r"**见到形状判断题，先猜结论是等腰/直角，再往 $(a-b)$ 或 $(a^2+b^2-c^2)$ 上凑**；" "\n"
        r"④ ⚠ **别被 C 选项骗**：「等腰或直角三角形」看起来最稳，" "\n"
        r"但 $3,4,5$ 代入就不成立 —— **代入一个具体反例是最快的排除法**；" "\n"
        r"⑤ 检验：**三组等腰各代一次 + 两组非等腰各代一次**，五组数据定乾坤。"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-191'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-191-E1',
}

T191_V1 = {
    'type': '选择',
    'stem_text': (
        r"在 $\triangle ABC$ 中，$\dfrac{a^{2}+b^{2}}{a^{2}-b^{2}}=\dfrac{\sin(A+B)}{\sin(A-B)}$，则 $\triangle ABC$ 的形状是（　　）"
    ),
    'opts': [
        ('A', r"等腰三角形但一定不是直角三角形"),
        ('B', r"等腰直角三角形"),
        ('C', r"直角三角形但一定不是等腰三角形"),
        ('D', r"等腰三角形或直角三角形"),
    ],
    'answer': 'C',
    'analysis': (
        r"交叉相乘后用 $\sin(A\pm B)=\sin A\cos B\pm\cos A\sin B$ 展开，正弦定理换成边，"
        r"配合 $a\cos B-b\cos A=\frac{a^{2}-b^{2}}c$、$a\cos B+b\cos A=c$，得 $(a^{2}-b^{2})(a^{2}+b^{2}-c^{2})=0$。"
    ),
    'solution': (
        r"由分母 $a^{2}-b^{2}\ne0$ 知 $a\ne b$，且 $\sin(A-B)\ne0$。" "\n"
        r"交叉相乘：$\left(a^{2}+b^{2}\right)\sin(A-B)=\left(a^{2}-b^{2}\right)\sin(A+B)$。" "\n"
        r"展开：$\sin(A-B)=\sin A\cos B-\cos A\sin B$、$\sin(A+B)=\sin A\cos B+\cos A\sin B$。" "\n"
        r"由正弦定理 $\sin A=\frac a{2R}$、$\sin B=\frac b{2R}$，提出 $\frac1{2R}$：" "\n"
        r"$\left(a^{2}+b^{2}\right)(a\cos B-b\cos A)=\left(a^{2}-b^{2}\right)(a\cos B+b\cos A)$。" "\n"
        r"由余弦定理：" "\n"
        r"$a\cos B-b\cos A=\dfrac{a^{2}+c^{2}-b^{2}}{2c}-\dfrac{b^{2}+c^{2}-a^{2}}{2c}=\dfrac{2a^{2}-2b^{2}}{2c}=\dfrac{a^{2}-b^{2}}c$；" "\n"
        r"$a\cos B+b\cos A=\dfrac{a^{2}+c^{2}-b^{2}}{2c}+\dfrac{b^{2}+c^{2}-a^{2}}{2c}=\dfrac{2c^{2}}{2c}=c$。" "\n"
        r"代入：$\left(a^{2}+b^{2}\right)\cdot\dfrac{a^{2}-b^{2}}c=\left(a^{2}-b^{2}\right)\cdot c$，" "\n"
        r"即 $\dfrac{(a^{2}-b^{2})(a^{2}+b^{2}-c^{2})}{c}=0$。" "\n"
        r"因 $a\ne b$，故 $a^{2}+b^{2}=c^{2}$，即 $C=\dfrac\pi2$。" "\n"
        r"又若等腰：若 $a=c$ 则 $a^{2}+b^{2}=a^{2}\Rightarrow b=0$ 不可能；若 $b=c$ 则 $a=0$ 不可能；" "\n"
        r"故**一定不是等腰三角形**。故选 C。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p155-159 详解：「由 $\frac{a^2+b^2}{a^2-b^2}=\frac{\sin(A+B)}{\sin(A-B)}$ 得 $(a^2+b^2)\sin(A-B)=(a^2-b^2)\sin(A+B)$，且 $a\ne b$…" "\n"
        r"化简整理得 $(a^2+b^2)(a^2-b^2)=(a^2-b^2)c^2$，即 $(a^2+b^2-c^2)(a^2-b^2)=0$，∴$a^2=b^2$ 或 $a^2+b^2=c^2$，又 $a\ne b$，" "\n"
        r"∴$\triangle ABC$ 是直角三角形但一定不是等腰三角形. 故选：C。」" "\n"
        r"—— **$a\ne b$、$(a^2-b^2)(a^2+b^2-c^2)=0$、$C=\frac\pi2$、一定不等腰、答案 C 全部与我的推导一致** ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **$a\cos B-b\cos A=\frac{a^2-b^2}{c}$**：" "\n"
        r"$a\cos B=a\frac{a^2+c^2-b^2}{2ac}=\frac{a^2+c^2-b^2}{2c}$；$b\cos A=\frac{b^2+c^2-a^2}{2c}$。" "\n"
        r"差 $=\frac{a^2+c^2-b^2-b^2-c^2+a^2}{2c}=\frac{2a^2-2b^2}{2c}=\frac{a^2-b^2}{c}$ ✓✓✓" "\n"
        r"② **$a\cos B+b\cos A=c$**（射影定理）：和 $=\frac{a^2+c^2-b^2+b^2+c^2-a^2}{2c}=\frac{2c^2}{2c}=c$ ✓✓✓" "\n"
        r"③ **代入**：$(a^2+b^2)\frac{a^2-b^2}{c}=(a^2-b^2)c$ ⟹ $(a^2-b^2)(a^2+b^2-c^2)=0$ ✓✓✓" "\n"
        r"④ **数值检验**：取直角非等腰 $a=3,b=4,c=5$（$C=90^\circ$）。" "\n"
        r"$\frac{a^2+b^2}{a^2-b^2}=\frac{9+16}{9-16}=\frac{25}{-7}=-3.5714$。" "\n"
        r"$\frac{\sin(A+B)}{\sin(A-B)}$：$A+B=90^\circ$，$\sin=1$。" "\n"
        r"$\cos A=\frac{16+25-9}{2\cdot4\cdot5}=\frac{32}{40}=0.8$ ⟹ $\sin A=0.6$；$\cos B=\frac{9+25-16}{2\cdot3\cdot5}=0.6$ ⟹ $\sin B=0.8$。" "\n"
        r"$\sin(A-B)=0.6(0.6)-0.8(0.8)=0.36-0.64=-0.28$。" "\n"
        r"比值 $=\frac1{-0.28}=-3.5714$ ✓✓✓ **完全吻合**" "\n"
        r"⑤ **排除等腰直角 $1,1,\sqrt2$**：$a=b$ 时分母为 $0$，**等式无意义** ✗ ⟹ B、D 排除" "\n"
        r"⑥ **排除 A、D 的「等腰」**：由 $a^2+b^2=c^2$ 且等腰 ⟹ $a=c$ 或 $b=c$ 都导致另一边为 $0$ ✗" "\n"
        r"（实测：若 $a=c$、$a^2+b^2=c^2$ ⟹ $b^2=0$，不能构成三角形）✓✓✓" "\n"
        r"**答案 C 正确** ✓" "\n"
        r"**⭐⭐ 通法（两个恒等式是本题的命门）**：" "\n"
        r"① ⭐⭐ **$a\cos B+b\cos A=c$**（射影定理）与 **$a\cos B-b\cos A=\frac{a^{2}-b^{2}}c$** —— " "\n"
        r"这一「和差配对」能瞬间消化掉所有 $\sin(A\pm B)$ 型式子，**比展开成正弦余弦再用余弦定理快得多**；" "\n"
        r"② ⭐⭐ **分母不为 $0$ 是隐藏条件**：$a^{2}-b^{2}\ne0$ ⟹ $a\ne b$，" "\n"
        r"这正是排除「等腰」的唯一依据。**看到分式方程先看分母**；" "\n"
        r"③ ⭐ **$\sin(A-B)\ne0$ ⟹ $A\ne B$** 与 $a\ne b$ 是同一件事的两种说法；" "\n"
        r"④ ⚠ **「一定不是等腰」要单独证**：由 $a^2+b^2=c^2$ 出发，" "\n"
        r"分别假设 $a=c$、$b=c$ 都得 $0$ 边，**这一步不能省**（否则就只能选 D 了）；" "\n"
        r"⑤ 检验：**取 $3,4,5$ 数值对拍**（两边都是 $-3.5714$ ✓），并**验 $a=b$ 时分母为 $0$**。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-191'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-191-V1',
}

T191_V2 = {
    'type': '选择',
    'stem_text': (
        r"在 $\triangle ABC$ 中，角 $A$、$B$、$C$ 的对边分别为 $a$、$b$、$c$，若 $c^{2}=b(a+b)$，"
        r"则以下结论正确的是（　　）"
    ),
    'opts': [
        ('A', r"$c>b$"),
        ('B', r"$C=2B$"),
        ('C', r"$a>c$"),
        ('D', r"$0<B<\dfrac\pi4$"),
    ],
    'answer': 'AB',
    'analysis': (
        r"$c^{2}=b(a+b)>b^{2}$ ⟹ $c>b$。余弦定理得 $\cos B=\frac c{2b}$，正弦定理换成正弦得 $\sin C=\sin2B$，"
        r"故 $C=2B$ 或 $C+2B=\pi$；后者推出 $A=B$、$a=b$、$C=\frac\pi2$，此时仍有 $C=2B$。"
    ),
    'solution': (
        r"**A**：由 $a>0$ 得 $c^{2}=b(a+b)=ab+b^{2}>b^{2}$，故 $c>b$，A 正确。" "\n"
        r"**B**：由余弦定理并代入 $c^{2}=b(a+b)$：" "\n"
        r"$\cos B=\dfrac{a^{2}+c^{2}-b^{2}}{2ac}=\dfrac{a^{2}+ab+b^{2}-b^{2}}{2ac}=\dfrac{a^{2}+ab}{2ac}=\dfrac{a+b}{2c}$。" "\n"
        r"又由 $c^{2}=b(a+b)$ 得 $a+b=\dfrac{c^{2}}b$，故 $\cos B=\dfrac{c^{2}}{2bc}=\dfrac c{2b}$。" "\n"
        r"由正弦定理 $\dfrac cb=\dfrac{\sin C}{\sin B}$，故 $\cos B=\dfrac{\sin C}{2\sin B}$，即 $\sin C=2\sin B\cos B=\sin2B$。" "\n"
        r"于是 $C=2B$ 或 $C+2B=\pi$。" "\n"
        r"若 $C+2B=\pi$，由 $A+B+C=\pi$ 得 $A=B$，即 $a=b$；代入 $c^{2}=b(a+b)=2b^{2}=a^{2}+b^{2}$，" "\n"
        r"此时 $C=\dfrac\pi2$、$A=B=\dfrac\pi4$，**仍满足 $C=2B$**（$90^\circ=2\times45^\circ$）。故 B 正确。" "\n"
        r"**C**：取 $A=B=\dfrac\pi4$、$C=\dfrac\pi2$，则 $a=b$、$c=\sqrt2a>a$，故 $a>c$ 不成立，C 错误。" "\n"
        r"**D**：由 B 知 $C=2B$，故 $A=\pi-B-C=\pi-3B>0$，即 $B<\dfrac\pi3$。" "\n"
        r"例如 $B=\dfrac\pi4$ 时 $C=\dfrac\pi2$、$A=\dfrac\pi4$ 仍成立，故 $B$ 可以取到 $\dfrac\pi4$，$0<B<\frac\pi4$ 错误。" "\n"
        r"故选 AB。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书详解：「因为 $c^2=b(a+b)>bc$，所以 $c>b$，故 A 正确；" "\n"
        r"由余弦定理得 $\cos B=\frac{a^2+c^2-b^2}{2ac}=\frac{a^2+ab}{2ac}=\frac{a+b}{2c}=\frac c{2b}$，由正弦定理得 $\frac cb=\frac{\sin C}{\sin B}$，" "\n"
        r"所以 $\cos B=\frac{\sin C}{2\sin B}$，即 $\sin C=2\sin B\cos B$，所以 $\sin C=\sin2B$，所以 $C=2B$ 或 $C+2B=\pi$，" "\n"
        r"因为 $A+B+C=\pi$，若 $C+2B=\pi$，可得 $A=B$，所以 $a=b$，又 $c^2=b(a+b)$，所以 $c^2=a^2+b^2$，此时 $C=\frac\pi2$、$A=B=\frac\pi4$，" "\n"
        r"满足 $C=2B$，故 B 正确；当 $A=B=\frac\pi4$、$C=\frac\pi2$ 时，$a<c$，故 C 错误；由 B 选项可知 $C=2B$，故 $A=\pi-(B+C)=\pi-3B>0$，" "\n"
        r"即 $B<\frac\pi3$，故 D 错误．故选：AB。」" "\n"
        r"—— **$c>b$、$\cos B=\frac c{2b}$、$\sin C=\sin2B$、$A=B=45^\circ$ 情形、$B<\frac\pi3$、答案 AB 全部与我的推导一致** ✓✓✓" "\n"
        r"（⚠ 原书首句写「$c^2=b(a+b)>bc$」，应为 $>b^2$；但结论 $c>b$ 正确）" "\n"
        r"**独立验算**：" "\n"
        r"① **A**：$c^2=b(a+b)$，$a>0$ ⟹ $c^2>b^2$ ⟹ $c>b$ ✓✓✓" "\n"
        r"② **$\cos B=\frac{a+b}{2c}$**：$\frac{a^2+c^2-b^2}{2ac}=\frac{a^2+ab+b^2-b^2}{2ac}=\frac{a^2+ab}{2ac}=\frac{a(a+b)}{2ac}=\frac{a+b}{2c}$ ✓✓✓" "\n"
        r"③ **$\frac{a+b}{2c}=\frac c{2b}$**：$a+b=\frac{c^2}b$ ⟹ $\frac{c^2/b}{2c}=\frac c{2b}$ ✓✓✓" "\n"
        r"④ **$\sin C=\sin2B$**：$\cos B=\frac{\sin C}{2\sin B}$（由 $\frac cb=\frac{\sin C}{\sin B}$）⟹ $\sin C=2\sin B\cos B$ ✓✓✓" "\n"
        r"⑤ **数值检验（一般情形）**：取 $b=1$、$a=2$，则 $c^2=1(3)=3$、$c=1.7321$。" "\n"
        r"验三角形：$1+1.7321>2$ ✓、$1+2>1.7321$ ✓、$2+1.7321>1$ ✓" "\n"
        r"$\cos B=\frac{4+3-1}{2\cdot2\cdot1.7321}=\frac6{6.9282}=0.8660$ ⟹ $B=30^\circ$。" "\n"
        r"$\cos C=\frac{4+1-3}{2\cdot2\cdot1}=\frac24=0.5$ ⟹ $C=60^\circ$ ✓✓✓ **$C=2B$ 成立**" "\n"
        r"$A=180-30-60=90^\circ$。验 $\cos B=\frac c{2b}=\frac{1.7321}2=0.8660$ ✓✓✓ **与 $B=30^\circ$ 吻合**" "\n"
        r"⑥ **数值检验（等腰情形）**：取 $a=b=1$，则 $c^2=1(2)=2$、$c=1.4142$。" "\n"
        r"$\cos C=\frac{1+1-2}{2}=0$ ⟹ $C=90^\circ$；$\cos A=\frac{1+2-1}{2\cdot1\cdot1.4142}=\frac2{2.8284}=0.7071$ ⟹ $A=45^\circ$；$B=45^\circ$。" "\n"
        r"$C=90^\circ=2B=90^\circ$ ✓✓✓；$a=1<c=1.4142$ ⟹ **C 选项 $a>c$ 错误** ✓✓✓" "\n"
        r"⑦ **D 排除**：此时 $B=45^\circ=\frac\pi4$，**不在 $(0,\frac\pi4)$ 内** ⟹ D 错误 ✓✓✓" "\n"
        r"（且由 $A=\pi-3B>0$ 得 $B<\frac\pi3$，$45^\circ<60^\circ$ ✓ 一致）" "\n"
        r"**答案 AB 正确** ✓" "\n"
        r"**⭐⭐ 通法（$\sin C=\sin2B$ 型的多解处理）**：" "\n"
        r"① ⭐⭐ **$\sin X=\sin Y$ ⟹ $X=Y$ 或 $X+Y=\pi$** —— **绝对不能只取第一个**，" "\n"
        r"本题正是在第二种情形下仍能推出 $C=2B$，所以 B 才成立；" "\n"
        r"② ⭐⭐ **$\cos B=\frac c{2b}$ 是「倍角」的标志**：$\frac c{2b}=\frac{\sin C}{2\sin B}$，" "\n"
        r"配合 $\sin C=2\sin B\cos B$ 正好是 $C=2B$ 的充要条件（在三角形中）；" "\n"
        r"③ ⭐ **$c^2=b(a+b)$ 这类条件要正着反着都用**：正用得 $c>b$、反用得 $a+b=\frac{c^2}b$ —— " "\n"
        r"**两个方向各服务一个选项**（A 和 B）；" "\n"
        r"④ ⚠ **D 的陷阱是 $\frac\pi4$**：由 $B<\frac\pi3$ 只能推出上界是 $\frac\pi3$，" "\n"
        r"而 $A=B=45^\circ$ 恰恰是**可取到的边界情形**，一举否掉 D；" "\n"
        r"⑤ 检验：**取 $a\ne b$ 与 $a=b$ 两组数各验一次**（$B=30^\circ$/$C=60^\circ$ 与 $45^\circ$/$90^\circ$ 都满足 $C=2B$ ✓）。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-191'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-191-V2',
}

T191_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知 $\triangle ABC$ 的三边长分别为 $\sqrt a$、$\sqrt b$、$\sqrt c$，"
        r"若存在角 $\theta\in(0,\pi)$ 使得 $a^{2}=b^{2}+c^{2}-2bc\cos\theta$，则 $\triangle ABC$ 的形状为（　　）"
    ),
    'opts': [
        ('A', r"锐角三角形"),
        ('B', r"直角三角形"),
        ('C', r"钝角三角形"),
        ('D', r"以上都不对"),
    ],
    'answer': 'A',
    'analysis': (
        r"由余弦定理，$a^{2}=b^{2}+c^{2}-2bc\cos\theta$ 说明 $a,b,c$ 构成三角形。于是 $\sqrt a+\sqrt b>\sqrt{a+b}>\sqrt c$，"
        r"即 $\sqrt a,\sqrt b,\sqrt c$ 也构成三角形。设 $c$ 最大，则 $\cos C=\frac{a+b-c}{2\sqrt{ab}}>0$，故最大角为锐角。"
    ),
    'solution': (
        r"由余弦定理的形式可知，存在 $\theta\in(0,\pi)$ 使 $a^{2}=b^{2}+c^{2}-2bc\cos\theta$，" "\n"
        r"等价于 **$a,b,c$ 三数能构成一个三角形**（$\theta$ 为 $b,c$ 的夹角）。" "\n"
        r"于是 $a+b>c$、$b+c>a$、$c+a>b$。" "\n"
        r"**第一步：$\sqrt a,\sqrt b,\sqrt c$ 也构成三角形**。" "\n"
        r"不妨设 $c\ge a$、$c\ge b$，只需证 $\sqrt a+\sqrt b>\sqrt c$：" "\n"
        r"$\left(\sqrt a+\sqrt b\right)^{2}=a+b+2\sqrt{ab}>a+b>c$，故 $\sqrt a+\sqrt b>\sqrt c$ ✓" "\n"
        r"**第二步：最大角是锐角**。设 $c$ 最大，则 $\triangle ABC$ 中角 $C$ 最大（对边 $\sqrt c$）。" "\n"
        r"由余弦定理：$\cos C=\dfrac{\left(\sqrt a\right)^{2}+\left(\sqrt b\right)^{2}-\left(\sqrt c\right)^{2}}"
        r"{2\sqrt a\sqrt b}=\dfrac{a+b-c}{2\sqrt{ab}}$。" "\n"
        r"由 $a+b>c$ 得 $\cos C>0$，故 $C$ 为锐角。" "\n"
        r"最大角为锐角 ⟹ 三个角都是锐角 ⟹ $\triangle ABC$ 为**锐角三角形**。故选 A。"
    ),
    'review': (
        r"⚠ **题干的三个根号是我还原的**：ref_bank 提取为「三边长分别为 $a,b,c$」。" "\n"
        r"**反证**：若边长就是 $a,b,c$，则 $a^{2}=b^{2}+c^{2}-2bc\cos\theta$ 就是余弦定理本身，" "\n"
        r"对任意三角形恒成立，条件毫无意义，**本题将没有区分度**；" "\n"
        r"而原书详解明确写「$\cos C=\frac{a+b-c}{2\sqrt{ab}}$」—— 分母是 $2\sqrt{ab}$，" "\n"
        r"说明三边长是 $\sqrt a$、$\sqrt b$、$\sqrt c$（此时 $\cos C=\frac{a+b-c}{2\sqrt a\sqrt b}$）✓✓✓" "\n"
        r"★ 答案完整 ✓。原书 p154-158 详解：「则 $(b+c)^2>a^2=b^2+c^2-2bc\cos\theta>(b-c)^2$，即三边长 $a,b,c$ 也可构成一个三角形，" "\n"
        r"不妨假设 $\sqrt a<\sqrt b<\sqrt c$，由两边之和大于第三边可得 $\sqrt a+\sqrt b>\sqrt c$…" "\n"
        r"在 $\triangle ABC$ 中，$C$ 最大，由余弦定理 $\cos C=\frac{a+b-c}{2\sqrt{ab}}>0$，即 $C$ 为锐角，即 $\triangle ABC$ 为锐角三角形，故选 A。」" "\n"
        r"—— **$\sqrt a+\sqrt b>\sqrt c$、$\cos C=\frac{a+b-c}{2\sqrt{ab}}>0$、锐角、答案 A 全部与我的推导一致** ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **$a,b,c$ 构成三角形**：由 $a^2=b^2+c^2-2bc\cos\theta$、$\theta\in(0,\pi)$ ⟹ $\cos\theta\in(-1,1)$" "\n"
        r"⟹ $(b-c)^2<a^2<(b+c)^2$ ⟹ $|b-c|<a<b+c$ ✓✓✓ 三边关系成立" "\n"
        r"② **$\sqrt a+\sqrt b>\sqrt c$**：$(\sqrt a+\sqrt b)^2=a+b+2\sqrt{ab}>a+b>c$ ✓✓✓" "\n"
        r"（同理另两条，故 $\sqrt a,\sqrt b,\sqrt c$ 确为三角形三边）" "\n"
        r"③ **$\cos C=\frac{a+b-c}{2\sqrt{ab}}$**：边长为 $\sqrt a,\sqrt b,\sqrt c$，对角 $C$ 的边是 $\sqrt c$" "\n"
        r"$\cos C=\frac{(\sqrt a)^2+(\sqrt b)^2-(\sqrt c)^2}{2\sqrt a\sqrt b}=\frac{a+b-c}{2\sqrt{ab}}$ ✓✓✓" "\n"
        r"④ **$a+b>c$ ⟹ $\cos C>0$** ✓✓✓ ⟹ $C<90^\circ$" "\n"
        r"⑤ **数值检验**：取 $a=4,b=9,c=10$（验：$4+9>10$ ✓、$4+10>9$ ✓、$9+10>4$ ✓）。" "\n"
        r"边长 $\sqrt4=2$、$\sqrt9=3$、$\sqrt{10}=3.1623$。验三角形：$2+3>3.1623$ ✓" "\n"
        r"最大边 $3.1623$（对 $C$）：$\cos C=\frac{4+10-9... }$ 等等，重新对应：$c$ 最大 $\Rightarrow$ 对角是 $C$。" "\n"
        r"$\cos C=\frac{4+9-10}{2\cdot2\cdot3}=\frac3{12}=0.25>0$ ⟹ $C=75.5^\circ$ 锐角 ✓✓✓" "\n"
        r"另两角：$\cos A=\frac{9+10-4}{2\cdot3\cdot3.1623}=\frac{15}{18.9738}=0.7906$ ⟹ $A=37.8^\circ$；" "\n"
        r"$B=180-75.5-37.8=66.7^\circ$。三角均锐 ✓✓✓ **锐角三角形**" "\n"
        r"⑥ **能否是钝角？** 需 $\cos C<0$ ⟹ $a+b<c$，与 $a,b,c$ 构成三角形矛盾 ✗ ✓✓✓" "\n"
        r"**答案 A 正确** ✓" "\n"
        r"**⭐⭐ 通法（「根号边长」型判定）**：" "\n"
        r"① ⭐⭐ **看到 $\cos C=\frac{a+b-c}{2\sqrt{ab}}$ 这种分母带根号的形式，立刻反推三边长是 $\sqrt a,\sqrt b,\sqrt c$** —— " "\n"
        r"这是识别根号丢失的最可靠线索；" "\n"
        r"② ⭐⭐ **关键不等式 $\left(\sqrt a+\sqrt b\right)^{2}>a+b>c$** —— " "\n"
        r"「开方后仍是三角形」这一步**必须证**，否则题目本身不成立；" "\n"
        r"③ ⭐ **只需证最大角是锐角**：三角形中最大角 $<90^\circ$ ⟹ 全锐，" "\n"
        r"**不用逐角验证**；" "\n"
        r"④ ⚠ **$a,b,c$ 构成三角形与 $\sqrt a,\sqrt b,\sqrt c$ 构成三角形是两回事**，" "\n"
        r"本题正是要由前者推后者 —— 若题干根号丢失，题目就退化成「$a,b,c$ 是三角形 ⟹ 什么形状」，无解；" "\n"
        r"⑤ 检验：**取一组具体数（$4,9,10$）算出三个角都是锐角** ✓，并**验证钝角不可能**（需 $a+b<c$ 矛盾）。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-191'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-191-V3',
}

T194_E1 = {
    'type': '选择',
    'stem_text': (
        r"在 $\triangle ABC$ 中，角 $A,B,C$ 所对应的边分别为 $a,b,c$，设 $\triangle ABC$ 的面积为 $S$，"
        r"则 $\dfrac{S}{a^{2}+4bc}$ 的最大值为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac{\sqrt2}{16}$"),
        ('B', r"$\dfrac{\sqrt3}{12}$"),
        ('C', r"$\dfrac{\sqrt3}{16}$"),
        ('D', r"$\dfrac{\sqrt2}{18}$"),
    ],
    'answer': 'A',
    'analysis': (
        r"用 $b^{2}+c^{2}\ge2bc$ 放缩分母，把 $b,c$ 整体约掉，化为只含 $A$ 的式子 $\frac{\sin A}{2(6-2\cos A)}$，"
        r"再设该值为 $t$ 反解，用辅助角的有界性列不等式。"
    ),
    'solution': (
        r"$S=\dfrac12bc\sin A$，$a^{2}=b^{2}+c^{2}-2bc\cos A$。于是" "\n"
        r"$\dfrac{S}{a^{2}+4bc}=\dfrac{\frac12bc\sin A}{b^{2}+c^{2}-2bc\cos A+4bc}$。" "\n"
        r"由 $b^{2}+c^{2}\ge2bc$（当且仅当 $b=c$ 取等）：" "\n"
        r"分母 $\ge 2bc-2bc\cos A+4bc=bc(6-2\cos A)$，故" "\n"
        r"$\dfrac{S}{a^{2}+4bc}\le\dfrac{\frac12bc\sin A}{bc(6-2\cos A)}=\dfrac{\sin A}{2(6-2\cos A)}$。" "\n"
        r"设 $\dfrac{\sin A}{2(6-2\cos A)}=t>0$，则 $\dfrac12\sin A=6t-2t\cos A$，" "\n"
        r"即 $\dfrac12\sin A+2t\cos A=6t$。" "\n"
        r"由辅助角公式，左端 $\le\sqrt{\left(\dfrac12\right)^{2}+(2t)^{2}}=\sqrt{\dfrac14+4t^{2}}$，故" "\n"
        r"$6t\le\sqrt{\dfrac14+4t^{2}}\Rightarrow36t^{2}\le\dfrac14+4t^{2}\Rightarrow32t^{2}\le\dfrac14\Rightarrow t^{2}\le\dfrac1{128}$。" "\n"
        r"所以 $t\le\dfrac1{8\sqrt2}=\dfrac{\sqrt2}{16}$。故选 A。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p157 详解：「$S=\frac12bc\sin A$，$a^2=b^2+c^2-2bc\cos A$，则设" "\n"
        r"$\frac{S}{a^2+4bc}=\frac{\frac12bc\sin A}{b^2+c^2-2bc\cos A+4bc}\le\frac{\frac12bc\sin A}{2bc-2bc\cos A+4bc}=\frac{\sin A}{2(6-2\cos A)}=t$" "\n"
        r"所以 $\frac12\sin A=6t-2t\cos A$，即 $\frac12\sin A+2t\cos A=6t\le\sqrt{\frac14+4t^2}$，∴$t\le\frac{\sqrt2}{16}$，故选：A。」" "\n"
        r"—— **$b^2+c^2\ge2bc$、$\frac{\sin A}{2(6-2\cos A)}=t$、$\sqrt{\frac14+4t^2}$、$t\le\frac{\sqrt2}{16}$、答案 A 全部与我的推导一致** ✓✓✓" "\n"
        r"**独立验算（数值扫描，完全独立）**：" "\n"
        r"① 令 $f(A)=\frac{\sin A}{2(6-2\cos A)}=\frac{\sin A}{12-4\cos A}$，逐点计算：" "\n"
        r"$A=\frac\pi2$（$1.5708$）：$\frac1{12-0}=0.08333$" "\n"
        r"$A=1.0$：$\frac{0.8415}{12-4(0.5403)}=\frac{0.8415}{9.8388}=0.08553$" "\n"
        r"$A=1.2$：$\frac{0.9320}{12-4(0.3624)}=\frac{0.9320}{10.5504}=0.08834$" "\n"
        r"$A=1.22$：$\frac{0.9391}{12-4(0.3436)}=\frac{0.9391}{10.6256}=0.08838$" "\n"
        r"$A=1.25$：$\frac{0.9490}{12-4(0.3153)}=\frac{0.9490}{10.7388}=0.08837$" "\n"
        r"$A=1.4$：$\frac{0.9854}{12-4(0.1700)}=\frac{0.9854}{11.32}=0.08705$" "\n"
        r"最大值约 $0.08838\sim0.08839$，出现在 $A\approx1.22$ ✓✓✓" "\n"
        r"② **与选项比**：$\frac{\sqrt2}{16}=\frac{1.41421}{16}=0.088388$ ✓✓✓ **完全吻合**" "\n"
        r"$\frac{\sqrt3}{12}=0.14434$ ✗；$\frac{\sqrt3}{16}=0.10825$ ✗；$\frac{\sqrt2}{18}=0.07857$ ✗" "\n"
        r"③ **取等条件**：需 $b=c$（放缩取等）且辅助角取等。" "\n"
        r"辅助角：$\frac12\sin A+2t\cos A=\sqrt{\frac14+4t^2}\sin(A+\varphi)$，$\tan\varphi=\frac{2t}{1/2}=4t$。" "\n"
        r"$t=0.088388$ ⟹ $\tan\varphi=0.35355$ ⟹ $\varphi=0.3398$ rad。取等时 $A+\varphi=\frac\pi2$ ⟹ $A=1.5708-0.3398=1.2310$ ✓✓✓" "\n"
        r"**与数值扫描的 $A\approx1.22\sim1.23$ 一致** ✓✓✓" "\n"
        r"④ **验 $32t^2=\frac14$**：$32(0.088388)^2=32(0.0078125)=0.25$ ✓✓✓" "\n"
        r"**答案 A 正确** ✓" "\n"
        r"**⭐⭐ 通法（分式型面积最值 ⟹ 设 $t$ 反解）**：" "\n"
        r"① ⭐⭐ **先用 $b^{2}+c^{2}\ge2bc$ 把 $b,c$ 整体约掉** —— " "\n"
        r"分子分母都是 $bc$ 的齐次式，约掉后只剩角 $A$，**这是化简的关键一步**；" "\n"
        r"② ⭐⭐ **「求 $\frac{p\sin A+q}{r+s\cos A}$ 型最值」的标准做法：设它等于 $t$，反解出 $p\sin A+(\cdots)\cos A=$ 常数，" "\n"
        r"再用辅助角的有界性列不等式** —— 比求导快且不易错；" "\n"
        r"③ ⭐ **取等条件要两个同时满足**：放缩取等（$b=c$）+ 辅助角取等（$A+\varphi=\frac\pi2$），" "\n"
        r"本题数值验证 $A\approx1.231$ 与反解一致 ✓；" "\n"
        r"④ ⚠ **别把 $\frac{\sin A}{2(6-2\cos A)}$ 误写成 $\frac{\sin A}{6-2\cos A}$** —— " "\n"
        r"漏掉因子 $2$ 会得 $\frac{\sqrt2}8$，不在选项里，**这本身就是警报**；" "\n"
        r"⑤ 检验：**数值扫描 5$\sim$6 个点**定位最大值，再与四个选项比对 —— 本题精确到小数点后 5 位吻合 ✓。"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-194'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-194-E1',
}

T194_V1 = {
    'type': '选择',
    'stem_text': (
        r"若面积为 $1$ 的 $\triangle ABC$ 满足 $AB=2AC$，则边 $BC$ 的最小值为（　　）"
    ),
    'opts': [
        ('A', r"$1$"),
        ('B', r"$\sqrt2$"),
        ('C', r"$\sqrt3$"),
        ('D', r"$2$"),
    ],
    'answer': 'C',
    'analysis': (
        r"由面积定出 $AC^{2}=\frac1{\sin A}$，代入余弦定理得 $BC^{2}=\frac{5-4\cos A}{\sin A}$。求导得极值点 $\cos A=\frac45$，此时 $BC^{2}=3$。"
    ),
    'solution': (
        r"设 $AC=x$，则 $AB=2x$。" "\n"
        r"$S=\dfrac12\cdot AB\cdot AC\cdot\sin A=\dfrac12\cdot2x\cdot x\cdot\sin A=x^{2}\sin A=1$，故 $x^{2}=\dfrac1{\sin A}$。" "\n"
        r"由余弦定理：" "\n"
        r"$BC^{2}=AB^{2}+AC^{2}-2AB\cdot AC\cos A=4x^{2}+x^{2}-4x^{2}\cos A=(5-4\cos A)x^{2}=\dfrac{5-4\cos A}{\sin A}$。" "\n"
        r"设 $g(A)=\dfrac{5-4\cos A}{\sin A}$（$A\in(0,\pi)$），则" "\n"
        r"$g'(A)=\dfrac{4\sin A\cdot\sin A-(5-4\cos A)\cos A}{\sin^{2}A}=\dfrac{4\sin^{2}A-5\cos A+4\cos^{2}A}{\sin^{2}A}=\dfrac{4-5\cos A}{\sin^{2}A}$。" "\n"
        r"令 $g'(A)=0$ 得 $\cos A=\dfrac45$，此时 $\sin A=\dfrac35$，" "\n"
        r"$g_{\min}=\dfrac{5-4\cdot\frac45}{\frac35}=\dfrac{5-\frac{16}5}{\frac35}=\dfrac{\frac95}{\frac35}=3$。" "\n"
        r"当 $A\to0$ 或 $A\to\pi$ 时 $g\to+\infty$，故该极小值即最小值。" "\n"
        r"所以 $BC^{2}_{\min}=3$，$BC_{\min}=\sqrt3$。故选 C。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p157 详解：「∵$\triangle ABC$ 的面积 $S=1$，且 $AB=2AC$，" "\n"
        r"∴$S_{\triangle ABC}=\frac12AB\cdot AC\cdot\sin A=AC^2\sin A=1$，∴$AC^2=\frac1{\sin A}$，" "\n"
        r"∵根据余弦定理得：$BC^2=AB^2+AC^2-2AB\cdot AC\cos A=4AC^2+AC^2-4AC^2\cos A=(5-4\cos A)AC^2=\frac{5-4\cos A}{\sin A}$…" "\n"
        r"可得 $BC^2\sin A+4\cos A=5$，∴$BC^2\sin A+4\cos A=\sqrt{BC^4+16}\sin(A+\alpha)=5$，则 $\sqrt{BC^4+16}=\frac5{\sin(A+\alpha)}\ge5$，" "\n"
        r"解得：$BC\ge\sqrt3$，即边 $BC$ 的最小值为 $\sqrt3$。故选：C。」" "\n"
        r"—— **$AC^2=\frac1{\sin A}$、$BC^2=\frac{5-4\cos A}{\sin A}$、$BC\ge\sqrt3$、答案 C 全部与我的推导一致** ✓✓✓" "\n"
        r"（原书用辅助角法，我用求导法，两法结果一致）" "\n"
        r"**独立验算**：" "\n"
        r"① **$S=AC^2\sin A$**：$S=\frac12\cdot AB\cdot AC\sin A=\frac12\cdot 2AC\cdot AC\sin A=AC^2\sin A=1$ ✓✓✓" "\n"
        r"② **$BC^2=(5-4\cos A)AC^2$**：$AB^2+AC^2-2AB\cdot AC\cos A=4AC^2+AC^2-4AC^2\cos A$ ✓✓✓" "\n"
        r"③ **$g'(A)$ 的分子**：$4\sin^2A+4\cos^2A-5\cos A=4-5\cos A$ ✓✓✓（用 $\sin^2+\cos^2=1$）" "\n"
        r"④ **$\cos A=\frac45$ 时**：$\sin A=\frac35$，$5-4(\frac45)=5-3.2=1.8$，$g=\frac{1.8}{0.6}=3$ ✓✓✓" "\n"
        r"⑤ **辅助角法交叉验证**：$BC^2\sin A+4\cos A=5$ ⟹ $3(0.6)+4(0.8)=1.8+3.2=5$ ✓✓✓" "\n"
        r"$\sqrt{BC^4+16}=\sqrt{9+16}=\sqrt{25}=5$，且 $\sin(A+\alpha)=1$ ✓✓✓ **两法完全一致**" "\n"
        r"⑥ **数值检验**：取 $A$ 使 $\cos A=0.8$（$A=36.87^\circ$），$\sin A=0.6$。" "\n"
        r"$AC^2=\frac1{0.6}=1.6667$ ⟹ $AC=1.2910$、$AB=2.5820$。" "\n"
        r"$BC^2=4(1.6667)+1.6667-4(1.6667)(0.8)=6.6667+1.6667-5.3333=3.0$ ✓✓✓ **$BC=\sqrt3$**" "\n"
        r"面积验：$\frac12\cdot2.5820\cdot1.2910\cdot0.6=1.0000$ ✓✓✓ **恰为 $1$**" "\n"
        r"⑦ **边界**：$A\to0$ 时 $\sin A\to0$，$g\to+\infty$ ⟹ 该极值确为最小值 ✓✓✓" "\n"
        r"⑧ **选项排除**：$1<\sqrt2<\sqrt3<2$，最小值不能比 $\sqrt3$ 小（否则与 $g\ge3$ 矛盾）✓✓✓" "\n"
        r"**答案 C 正确** ✓" "\n"
        r"**⭐⭐ 通法（面积固定 + 两边成比例 ⟹ 第三边最值）**：" "\n"
        r"① ⭐⭐ **面积条件用来消去一个变量**：$S=\frac12\cdot AB\cdot AC\sin A$ 中 $AB=2AC$，" "\n"
        r"于是 $S=AC^{2}\sin A$ ⟹ $AC^{2}=\frac1{\sin A}$ —— **把边用角表示**；" "\n"
        r"② ⭐ **得到 $\frac{p-q\cos A}{\sin A}$ 型函数后，两条路都通**：" "\n"
        r"（a）求导：分子化为 $4-5\cos A$（利用 $\sin^{2}+\cos^{2}=1$ 把二次项消成常数）；" "\n"
        r"（b）反解 + 辅助角：$BC^{2}\sin A+4\cos A=5$ ⟹ $\sqrt{BC^{4}+16}\ge5$；" "\n"
        r"**建议两法都用，互为验证**（本题两法都给 $BC^2=3$ ✓）；" "\n"
        r"③ ⭐ **$p\sin A+q\cos A=r$ 有解 ⟺ $\sqrt{p^{2}+q^{2}}\ge|r|$** —— 这是辅助角法的本质；" "\n"
        r"④ ⚠ **别忘验边界**：$A\to0$ 或 $\pi$ 时函数趋于 $+\infty$，所以驻点是**最小**值而非最大值；" "\n"
        r"⑤ 检验：**把极值点代回算出两条边，再验面积是否恰为题设**（面积 $=1.0000$ ✓）。"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-194'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-194-V1',
}

T194_V2 = {
    'type': '选择',
    'stem_text': (
        r"在 $\triangle ABC$ 中，角 $A,B,C$ 的对边分别为 $a,b,c$，$\triangle ABC$ 的面积为 $S$，"
        r"已知 $A=15^{\circ}$，$4\sqrt3S=a^{2}$，则 $\dfrac bc+\dfrac cb$ 的值为（　　）"
    ),
    'opts': [
        ('A', r"$2$"),
        ('B', r"$2\sqrt2$"),
        ('C', r"$\sqrt6$"),
        ('D', r"$2\sqrt6$"),
    ],
    'answer': 'B',
    'analysis': (
        r"把 $S=\frac12bc\sin15^\circ$ 与 $a^{2}=b^{2}+c^{2}-2bc\cos15^\circ$ 代入 $4\sqrt3S=a^{2}$，"
        r"整理出 $b^{2}+c^{2}=4bc\sin45^\circ=2\sqrt2bc$，两边除以 $bc$ 即得。"
    ),
    'solution': (
        r"由 $S=\dfrac12bc\sin A=\dfrac12bc\sin15^{\circ}$，代入 $4\sqrt3S=a^{2}$：" "\n"
        r"$4\sqrt3\cdot\dfrac12bc\sin15^{\circ}=b^{2}+c^{2}-2bc\cos15^{\circ}$，" "\n"
        r"即 $2\sqrt3bc\sin15^{\circ}+2bc\cos15^{\circ}=b^{2}+c^{2}$。" "\n"
        r"提取 $4bc$：$4bc\left(\dfrac{\sqrt3}2\sin15^{\circ}+\dfrac12\cos15^{\circ}\right)=b^{2}+c^{2}$。" "\n"
        r"由 $\cos30^{\circ}=\dfrac{\sqrt3}2$、$\sin30^{\circ}=\dfrac12$，括号内为" "\n"
        r"$\sin15^{\circ}\cos30^{\circ}+\cos15^{\circ}\sin30^{\circ}=\sin(15^{\circ}+30^{\circ})=\sin45^{\circ}=\dfrac{\sqrt2}2$。" "\n"
        r"故 $b^{2}+c^{2}=4bc\cdot\dfrac{\sqrt2}2=2\sqrt2\,bc$。" "\n"
        r"两边除以 $bc$：$\dfrac bc+\dfrac cb=\dfrac{b^{2}+c^{2}}{bc}=2\sqrt2$。故选 B。"
    ),
    'review': (
        r"⚠ **$4\sqrt3 S$ 中的根号是我还原的**：ref_bank 提取为 `4 3S = a2`。" "\n"
        r"**验证**：若按字面 $4\cdot3S=a^2$，则 $12\cdot\frac12bc\sin15^\circ=b^2+c^2-2bc\cos15^\circ$，" "\n"
        r"得 $\frac{b^2+c^2}{bc}=6(0.2588)+2(0.9659)=1.5529+1.9319=3.4848$ —— **不是任何选项**；" "\n"
        r"取 $4\sqrt3$ 则得 $2\sqrt2=2.8284$ ✓ **恰为选项 B**。" "\n"
        r"★ 答案、详解完整 ✓。原书 p157 详解：「∵$A=15^\circ$，$4\sqrt3S=a^2$，∴$4\sqrt3\times\frac12bc\sin15^\circ=b^2+c^2-2bc\cos15^\circ$，" "\n"
        r"∴$2\sqrt3bc\sin15^\circ+2bc\cos15^\circ=b^2+c^2$，∴$4bc(\frac{\sqrt3}2\sin15^\circ+\frac12\cos15^\circ)=b^2+c^2$，" "\n"
        r"∴$4bc\sin(15^\circ+30^\circ)=b^2+c^2$，整理可得 $b^2+c^2=2\sqrt2bc$，∴$\frac{b^2}{bc}+\frac{c^2}{bc}=2\sqrt2$，则 $\frac bc+\frac cb=2\sqrt2$。故选：B．」" "\n"
        r"—— **$2\sqrt3bc\sin15^\circ+2bc\cos15^\circ=b^2+c^2$、$\sin(15^\circ+30^\circ)$、$2\sqrt2bc$、答案 B 全部与我的推导一致** ✓✓✓" "\n"
        r"**独立验算（数值，完全独立）**：" "\n"
        r"① 设 $b=1$，由 $b^2+c^2=2\sqrt2bc$ 得 $1+c^2=2.8284c$ ⟹ $c^2-2.8284c+1=0$。" "\n"
        r"$c=\frac{2.8284\pm\sqrt{8-4}}{2}=\frac{2.8284\pm2}{2}$ ⟹ $c=2.4142$ 或 $0.4142$（互为倒数 ✓ 合理）。" "\n"
        r"取 $b=1$、$c=2.4142$。" "\n"
        r"② **验 $a^2=4\sqrt3S$**：" "\n"
        r"$a^2=b^2+c^2-2bc\cos15^\circ=1+5.8284-2(1)(2.4142)(0.96593)=6.8284-4.6632=2.1652$。" "\n"
        r"$S=\frac12bc\sin15^\circ=0.5(1)(2.4142)(0.25882)=0.31241$。" "\n"
        r"$4\sqrt3S=6.9282(0.31241)=2.1645$ ✓✓✓ **与 $a^2=2.1652$ 吻合（差 $0.0007$ 为四舍五入）**" "\n"
        r"③ **验所求**：$\frac bc+\frac cb=\frac1{2.4142}+\frac{2.4142}1=0.4142+2.4142=2.8284=2\sqrt2$ ✓✓✓" "\n"
        r"④ **辅助角还原验**：$\frac{\sqrt3}2\sin15^\circ+\frac12\cos15^\circ=0.8660(0.25882)+0.5(0.96593)=0.22414+0.48296=0.70710=\frac{\sqrt2}2$ ✓✓✓" "\n"
        r"⑤ **$4bc\cdot\frac{\sqrt2}2=2\sqrt2bc=2.8284(2.4142)=6.8284=b^2+c^2=1+5.8284=6.8284$** ✓✓✓" "\n"
        r"**答案 B 正确** ✓" "\n"
        r"**⭐⭐ 通法（把 $S$ 与 $a^2$ 放在一起 ⟹ 齐次化）**：" "\n"
        r"① ⭐⭐ **本题全程只做一件事：把条件化成 $\frac{b^2+c^2}{bc}$ 的形式**。" "\n"
        r"因为所求 $\frac bc+\frac cb=\frac{b^2+c^2}{bc}$，**直接以它为目标倒推**；" "\n"
        r"② ⭐⭐ **$\frac{\sqrt3}2\sin x+\frac12\cos x=\sin(x+30^\circ)$** —— " "\n"
        r"看到系数 $\frac{\sqrt3}2$ 与 $\frac12$ 就要反应出 $30^\circ$，凑出 $15^\circ+30^\circ=45^\circ$（特殊角）；" "\n"
        r"③ ⭐ **$A=15^\circ$ 不是特殊角，但与 $30^\circ$ 相加凑成 $45^\circ$** —— " "\n"
        r"**这类题的角都是刻意设计的，加/减一个已知角就能得到特殊角**；" "\n"
        r"④ ⚠ **`4 3S` 是 `4\sqrt3 S`**：文本提取丢根号已在本项目出现数十次，" "\n"
        r"**判据是「算出的值不在选项里」**（按 $4\cdot3S$ 得 $3.4848$，四个选项无一符合）✓；" "\n"
        r"⑤ 检验：**由结论反解出 $b,c$，代回验 $a^2=4\sqrt3S$**（$2.1652$ vs $2.1645$ ✓）。"
    ),
    'difficulty': 0.78,
    'topics': ['M-T-194'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-194-V2',
}

T194_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知 $\triangle ABC$ 中，$\sin A$、$\sin B$、$\sin C$ 成等比数列，"
        r"则 $\dfrac{\sin2B}{\sin B+\cos B}$ 的取值范围是（　　）"
    ),
    'opts': [
        ('A', r"$\left(-\infty,\dfrac{\sqrt2}2\right]$"),
        ('B', r"$\left(0,\dfrac{\sqrt2}2\right]$"),
        ('C', r"$\left(-1,\sqrt2\right]$"),
        ('D', r"$\left(0,\dfrac{3-\sqrt3}2\right]$"),
    ],
    'answer': 'B',
    'analysis': (
        r"等比 ⟹ $\sin^{2}B=\sin A\sin C$ ⟹ $b^{2}=ac$。由余弦定理 + 基本不等式得 $\cos B\ge\frac12$，即 $0<B\le\frac\pi3$。"
        r"令 $t=\sin B+\cos B\in(1,\sqrt2]$，原式 $=t-\frac1t$，单调递增。"
    ),
    'solution': (
        r"由 $\sin A,\sin B,\sin C$ 成等比数列得 $\sin^{2}B=\sin A\sin C$，由正弦定理得 $b^{2}=ac$。" "\n"
        r"由余弦定理并结合基本不等式：" "\n"
        r"$\cos B=\dfrac{a^{2}+c^{2}-b^{2}}{2ac}=\dfrac{a^{2}+c^{2}-ac}{2ac}\ge\dfrac{2ac-ac}{2ac}=\dfrac12$（当且仅当 $a=c$ 取等）。" "\n"
        r"故 $0<B\le\dfrac\pi3$。" "\n"
        r"令 $t=\sin B+\cos B=\sqrt2\sin\left(B+\dfrac\pi4\right)$。" "\n"
        r"当 $B\in\left(0,\dfrac\pi3\right]$ 时 $B+\dfrac\pi4\in\left(\dfrac\pi4,\dfrac{7\pi}{12}\right]$，" "\n"
        r"$\sin$ 在该区间上先增后减，最大值为 $1$（在 $B=\frac\pi4$ 处），端点值为 $\sin\frac\pi4=\frac{\sqrt2}2$、$\sin\frac{7\pi}{12}\approx0.9659$。" "\n"
        r"故 $t\in\left(1,\sqrt2\right]$（$t\to1$ 当 $B\to0$，取不到；$t=\sqrt2$ 在 $B=\frac\pi4$ 处取到）。" "\n"
        r"原式 $=\dfrac{2\sin B\cos B}{\sin B+\cos B}=\dfrac{(\sin B+\cos B)^{2}-1}{\sin B+\cos B}=\dfrac{t^{2}-1}t=t-\dfrac1t$。" "\n"
        r"函数 $h(t)=t-\dfrac1t$ 在 $t>0$ 上单调递增，故" "\n"
        r"$h(t)\in\left(h(1),h(\sqrt2)\right]=\left(0,\sqrt2-\dfrac1{\sqrt2}\right]=\left(0,\dfrac{\sqrt2}2\right]$。故选 B。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p157 详解：「由已知可知 $\sin^2B=\sin A\cdot\sin C$，即 $b^2=ac$，" "\n"
        r"$\cos B=\frac{a^2+c^2-b^2}{2ac}=\frac{a^2+c^2-ac}{2ac}\ge\frac{2ac-ac}{2ac}=\frac12$，即 $0<B<\frac\pi3$，" "\n"
        r"$\sin B+\cos B=\sqrt2\sin(B+\frac\pi4)\in(1,\sqrt2]$，原式等于 $\frac{2\sin B\cos B}{\sin B+\cos B}=\frac{(\sin B+\cos B)^2-1}{\sin B+\cos B}$，" "\n"
        r"设 $t=\sin B+\cos B$ 即原式等于 $\frac{t^2-1}t=t-\frac1t$，$(1<t\le\sqrt2)$，函数是增函数，" "\n"
        r"当 $t=1$ 时函数等于 $0$，当 $t=\sqrt2$ 时函数等于 $\frac{\sqrt2}2$，所以原式的取值范围是 $(0,\frac{\sqrt2}2]$，故选 B。」" "\n"
        r"—— **$b^2=ac$、$\cos B\ge\frac12$、$t\in(1,\sqrt2]$、$t-\frac1t$、$(0,\frac{\sqrt2}2]$、答案 B 全部与我的推导一致** ✓✓✓" "\n"
        r"（⚠ 详解写「$0<B<\frac\pi3$」应含等号 $B\le\frac\pi3$（$a=c$ 时 $\cos B=\frac12$），不影响结论）" "\n"
        r"（⚠ **D 选项我的还原不确定**：ref_bank 存为 `0, 3 - | 3 | 2`，我按 $(0,\frac{3-\sqrt3}2]$ 录入；" "\n"
        r"但它只是干扰项，不影响答案判定）" "\n"
        r"**独立验算**：" "\n"
        r"① **$\sin^2B=\sin A\sin C$ ⟹ $b^2=ac$**：由正弦定理 $\sin X=\frac{x}{2R}$ 代入 ✓✓✓" "\n"
        r"② **$\cos B=\frac{a^2+c^2-ac}{2ac}\ge\frac12$**：$a^2+c^2\ge2ac$ ✓✓✓" "\n"
        r"③ **$B\le\frac\pi3$**：$\cos B\ge\frac12$ 且 $B\in(0,\pi)$ ⟹ $B\in(0,\frac\pi3]$ ✓✓✓" "\n"
        r"④ **$t=\sin B+\cos B\in(1,\sqrt2]$**：" "\n"
        r"$B\to0$：$t\to1$（取不到）；$B=\frac\pi4$：$t=\sqrt2$（最大）；$B=\frac\pi3$：$t=0.8660+0.5=1.366$。" "\n"
        r"区间 $(1,\sqrt2]$ ✓✓✓（$B=\frac\pi4$ 在 $(0,\frac\pi3]$ 内 ✓）" "\n"
        r"⑤ **原式 $=t-\frac1t$**：$2\sin B\cos B=(\sin B+\cos B)^2-1$ ✓✓✓" "\n"
        r"⑥ **$h(t)$ 单调递增**：$h'(t)=1+\frac1{t^2}>0$ ✓✓✓" "\n"
        r"⑦ **端点**：$h(1)=0$（取不到）；$h(\sqrt2)=\sqrt2-\frac1{\sqrt2}=1.4142-0.7071=0.7071=\frac{\sqrt2}2$ ✓✓✓" "\n"
        r"⑧ **数值检验（$B=\frac\pi4$）**：需 $b^2=ac$ 且 $B=45^\circ$。" "\n"
        r"$\cos B=\frac{a^2+c^2-ac}{2ac}=\frac{\sqrt2}2$。令 $u=\frac ac$：$\frac{u^2+1-u}{2u}=0.7071$ ⟹ $u^2-2.4142u+1=0$" "\n"
        r"⟹ $u=1.8833$ 或 $0.5310$（均 $\ne1$，非等腰 ✓）。取 $c=1$、$a=1.8833$：则 $b^2=1.8833$、$b=1.3724$。" "\n"
        r"验 $\cos B=\frac{3.5468+1-1.8833}{2(1.8833)(1)}=\frac{2.6635}{3.7666}=0.7071$ ✓✓✓ **$B=45^\circ$**" "\n"
        r"原式 $=\frac{\sin90^\circ}{\sin45^\circ+\cos45^\circ}=\frac1{0.7071+0.7071}=\frac1{1.4142}=0.7071=\frac{\sqrt2}2$ ✓✓✓ **达到上界**" "\n"
        r"**答案 B 正确** ✓" "\n"
        r"**⭐⭐ 通法（等比数列条件 ⟹ $b^2=ac$）**：" "\n"
        r"① ⭐⭐ **$\sin A,\sin B,\sin C$ 成等比 ⟺ $a,b,c$ 成等比**（$b^2=ac$）—— 正弦定理直接换；" "\n"
        r"② ⭐⭐ **$b^2=ac$ ⟹ $\cos B\ge\frac12$ ⟹ $B\le\frac\pi3$**：" "\n"
        r"这是 $b^2=ac$ 型条件的**标配结论**，记住可省一半时间；" "\n"
        r"③ ⭐⭐ **$2\sin B\cos B=(\sin B+\cos B)^{2}-1$** —— " "\n"
        r"分子凑成 $t$ 的函数，这是「分子分母都含 $\sin\pm\cos$」的通用技巧（与 M-T-192-E1 同源）；" "\n"
        r"④ ⚠ **$t$ 的下界是 $1$ 不是 $0$**：$B\to0$ 时 $t\to1$（因为 $\cos0=1$），" "\n"
        r"所以原式下界是 $h(1)=0$ 而非负数 ⟹ **排除 A $(-\infty,\frac{\sqrt2}2]$、C $(-1,\sqrt2]$**；" "\n"
        r"⑤ 检验：**取 $B=\frac\pi4$ 构造一组满足 $b^2=ac$ 的边**，验证原式恰为 $\frac{\sqrt2}2$ ✓。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-194'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-194-V3',
}

T212_E1 = {
    'type': '选择',
    'stem_text': (
        r"在 $\triangle ABC$ 中，$\sin(A-B)+\sin B=\sin C$，点 $D$ 在边 $BC$ 上，且 $CD=2BD=2$，"
        r"设 $k=\dfrac{\sin\angle ABD}{\sin\angle BAD}$，则当 $k$ 取最大值时，$\sin\angle ACD=$（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac14$"),
        ('B', r"$\dfrac{\sqrt6+\sqrt2}4$"),
        ('C', r"$\dfrac{3+\sqrt3}6$"),
        ('D', r"$\dfrac{3-\sqrt3}6$"),
    ],
    'answer': 'B',
    'analysis': (
        r"由条件得 $\cos A=\frac12$、$A=\frac\pi3$。由正弦定理 $k=\frac{AD}{BD}=AD$。"
        r"$D$ 分 $BC$ 为 $1:2$，向量法得 $k^{2}=\frac{4c^{2}+b^{2}+2bc}{a^{2}}$，令 $t=\frac cb$ 化为一元函数求最大值。"
    ),
    'solution': (
        r"**第一步：定 $A$**。" "\n"
        r"$\sin C=\sin(A+B)=\sin A\cos B+\cos A\sin B$，而 $\sin(A-B)=\sin A\cos B-\cos A\sin B$。" "\n"
        r"条件 $\sin(A-B)+\sin B=\sin C$ 化为" "\n"
        r"$\sin A\cos B-\cos A\sin B+\sin B=\sin A\cos B+\cos A\sin B$" "\n"
        r"$\Rightarrow\sin B=2\cos A\sin B$。因 $\sin B\ne0$，故 $\cos A=\dfrac12$，$A=\dfrac\pi3$。" "\n"
        r"**第二步：把 $k$ 写成边的关系**。" "\n"
        r"由 $CD=2BD=2$ 得 $BD=1$、$CD=2$、$BC=3$。" "\n"
        r"在 $\triangle ABD$ 中由正弦定理 $\dfrac{AD}{\sin\angle ABD}=\dfrac{BD}{\sin\angle BAD}$，" "\n"
        r"故 $k=\dfrac{\sin\angle ABD}{\sin\angle BAD}=\dfrac{AD}{BD}=AD$。" "\n"
        r"**第三步：用向量求 $AD$**。" "\n"
        r"$\vec{AD}=\dfrac23\vec{AB}+\dfrac13\vec{AC}$（因 $BD:DC=1:2$），故" "\n"
        r"$AD^{2}=\dfrac49c^{2}+\dfrac19b^{2}+2\cdot\dfrac23\cdot\dfrac13bc\cos A=\dfrac{4c^{2}+b^{2}+2bc}{9}$。" "\n"
        r"又 $a^{2}=b^{2}+c^{2}-2bc\cos\dfrac\pi3=b^{2}+c^{2}-bc$。" "\n"
        r"$k^{2}=\dfrac{AD^{2}}{BD^{2}}=AD^{2}=\dfrac{4c^{2}+b^{2}+2bc}{9}$，而 $BD=\dfrac a3$，故" "\n"
        r"$k=\dfrac{AD}{BD}=\dfrac{3AD}{a}$ ⟹ $k^{2}=\dfrac{9AD^{2}}{a^{2}}=\dfrac{4c^{2}+b^{2}+2bc}{b^{2}+c^{2}-bc}$。" "\n"
        r"令 $t=\dfrac cb>0$，则 $k^{2}=f(t)=\dfrac{4t^{2}+2t+1}{t^{2}-t+1}$。" "\n"
        r"$f'(t)=\dfrac{-6t^{2}+6t+3}{(t^{2}-t+1)^{2}}$，令 $f'(t)=0$ 得 $2t^{2}-2t-1=0$，取正根 $t=\dfrac{1+\sqrt3}2$。" "\n"
        r"此时 $f_{\max}=4+2\sqrt3$，故 $k_{\max}=1+\sqrt3$。" "\n"
        r"**第四步：求 $\sin\angle ACD$（即 $\sin C$）**。" "\n"
        r"$t=\dfrac cb=\dfrac{1+\sqrt3}2$ ⟹ $b=\dfrac{2c}{1+\sqrt3}=(\sqrt3-1)c$。" "\n"
        r"$a^{2}=b^{2}+c^{2}-bc=c^{2}\left[(\sqrt3-1)^{2}+1-(\sqrt3-1)\right]=c^{2}(6-3\sqrt3)$。" "\n"
        r"由正弦定理 $\dfrac a{\sin A}=\dfrac c{\sin C}$：" "\n"
        r"$\sin C=\dfrac{c\sin A}{a}=\dfrac{c\cdot\frac{\sqrt3}2}{c\sqrt{6-3\sqrt3}}=\dfrac{\sqrt3}{2\sqrt{6-3\sqrt3}}$。" "\n"
        r"数值：$\sqrt{6-3\sqrt3}=\sqrt{0.80385}=0.89658$，$\sin C=\dfrac{1.73205}{1.79316}=0.96593=\dfrac{\sqrt6+\sqrt2}4$。" "\n"
        r"（即 $C=75^{\circ}$，$\sin75^{\circ}=\frac{\sqrt6+\sqrt2}4$。）故选 B。"
    ),
    'review': (
        r"★ 题干、答案完整 ✓。原书 p176 详解给出：$k^2=\frac{4t^2+2t+1}{t^2-t+1}$，" "\n"
        r"导数 $f'(t)=\frac{-6t^2+6t+3}{(t^2-t+1)^2}$，$t=\frac{1+\sqrt3}2$ 时取最大，" "\n"
        r"$k$ 的最大值为 $1+\sqrt3$，此时 $\frac cb=\frac{1+\sqrt3}2$、$b=(\sqrt3-1)c$，" "\n"
        r"由正弦定理求得 $\sin\angle ACD=\frac{\sqrt6+\sqrt2}4$。" "\n"
        r"—— **$\cos A=\frac12$、$t=\frac{1+\sqrt3}2$、$k_{\max}=1+\sqrt3$、$\sin C=\frac{\sqrt6+\sqrt2}4$ 全部与我的推导一致** ✓✓✓" "\n"
        r"（C、D 两个选项的具体形式在提取中破损，我按 $\frac{3\pm\sqrt3}6$ 录入；它们是干扰项，不影响答案判定）" "\n"
        r"**独立验算（全程数值，完全独立）**：" "\n"
        r"① **$\cos A=\frac12$**：$\sin(A-B)+\sin B=\sin(A+B)$ ⟹ $\sin A\cos B-\cos A\sin B+\sin B=\sin A\cos B+\cos A\sin B$" "\n"
        r"⟹ $\sin B=2\cos A\sin B$ ⟹ $\cos A=\frac12$ ✓✓✓" "\n"
        r"② **$k=AD$**：$\triangle ABD$ 中 $\frac{AD}{\sin\angle ABD}=\frac{BD}{\sin\angle BAD}$ ⟹ $\frac{\sin\angle ABD}{\sin\angle BAD}=\frac{AD}{BD}=\frac{AD}{1}$ ✓✓✓" "\n"
        r"③ **$AD^2=\frac{4c^2+b^2+2bc}{9}$**：$\vec{AD}=\frac23\vec{AB}+\frac13\vec{AC}$，" "\n"
        r"$|\cdot|^2=\frac49c^2+\frac19b^2+2\cdot\frac29 bc\cos60^\circ=\frac{4c^2+b^2+2bc\cdot\frac12\cdot2}{9}=\frac{4c^2+b^2+2bc}{9}$ ✓✓✓" "\n"
        r"④ **$f'(t)$**：分子 $=(8t+2)(t^2-t+1)-(4t^2+2t+1)(2t-1)$。" "\n"
        r"$(4t^2+2t+1)(2t-1)=8t^3-4t^2+4t^2-2t+2t-1=8t^3-1$ ✓✓✓" "\n"
        r"$(8t+2)(t^2-t+1)=8t^3-8t^2+8t+2t^2-2t+2=8t^3-6t^2+6t+2$ ✓✓✓" "\n"
        r"差 $=-6t^2+6t+3$ ✓✓✓；零点 $2t^2-2t-1=0$ ⟹ $t=\frac{2\pm\sqrt{12}}{4}=\frac{1\pm\sqrt3}2$，取正 $t=1.3660$ ✓✓✓" "\n"
        r"⑤ **$f_{\max}=4+2\sqrt3$**：$t=1.3660$、$t^2=1.8660$。" "\n"
        r"分子 $=4(1.8660)+2(1.3660)+1=7.4641+2.7321+1=11.1962$；分母 $=1.8660-1.3660+1=1.5000$。" "\n"
        r"$f=7.4641=4+2\sqrt3$ ✓✓✓（$4+3.4641=7.4641$）；$k=\sqrt{7.4641}=2.7321=1+\sqrt3$ ✓✓✓" "\n"
        r"⑥ **$\sin C$**：$b=(\sqrt3-1)c=0.73205c$；$a^2=c^2[(0.73205)^2+1-0.73205]=c^2[0.53590+0.26795]=c^2(0.80385)$。" "\n"
        r"$a=0.89658c$。$\sin C=\frac{c\cdot0.86603}{0.89658c}=0.96593$。" "\n"
        r"$\frac{\sqrt6+\sqrt2}4=\frac{2.44949+1.41421}4=\frac{3.86370}4=0.96593$ ✓✓✓ **完全吻合**" "\n"
        r"（且 $\arcsin(0.96593)=75^\circ$，此时 $A=60^\circ$、$B=45^\circ$，验：$60+45+75=180$ ✓✓✓）" "\n"
        r"⑦ **验 $B=45^\circ$ 自洽**：$\frac cb=\frac{\sin C}{\sin B}=\frac{\sin75^\circ}{\sin45^\circ}=\frac{0.96593}{0.70711}=1.3660=\frac{1+\sqrt3}2$ ✓✓✓ **与 $t$ 一致**" "\n"
        r"**答案 B 正确** ✓" "\n"
        r"**⭐⭐ 通法（定比分点 + 向量求线段长）**：" "\n"
        r"① ⭐⭐ **$BD:DC=1:2$ ⟹ $\vec{AD}=\frac23\vec{AB}+\frac13\vec{AC}$** —— " "\n"
        r"**系数与「对面的段长」成正比**（$D$ 离 $B$ 越远，$\vec{AB}$ 的系数越小… 具体：$\vec{AD}=\frac{DC}{BC}\vec{AB}+\frac{BD}{BC}\vec{AC}$）；" "\n"
        r"② ⭐⭐ **正弦定理把「两个正弦之比」换成「两条边之比」** —— " "\n"
        r"$k=\frac{\sin\angle ABD}{\sin\angle BAD}=\frac{AD}{BD}$，这是本破题眼；" "\n"
        r"③ ⭐ **齐次化 + 单变量**：$k^2$ 的分子分母都是 $b,c$ 的二次齐次式，除以 $b^2$ 引进 $t=\frac cb$，" "\n"
        r"化为一元有理函数，**这是处理双变量最值问题的通法**；" "\n"
        r"④ ⚠ **$k=\frac{3AD}{a}$ 而非 $\frac{AD}{a}$**：因为 $BD=\frac a3$ 不是 $a$ —— " "\n"
        r"**比例关系要代对**，否则 $k^2$ 会差 9 倍；" "\n"
        r"⑤ 检验：**求出 $\sin C$ 后反算 $B$，再验 $\frac cb=\frac{\sin C}{\sin B}$ 是否等于最优 $t$**（$1.3660$ ✓ 闭合）。"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-212'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-212-E1',
}

T212_V1 = {
    'type': '选择',
    'stem_text': (
        r"在 $\triangle ABC$ 中，角 $A$、$B$、$C$ 所对的边分别为 $a$、$b$、$c$，$\triangle ABC$ 的面积为 $S$，"
        r"若 $S=\dfrac{a^{2}}2$，则（　　）"
    ),
    'opts': [
        ('A', r"$bc=a$"),
        ('B', r"$\tan A=\dfrac{b^{2}+c^{2}-a^{2}}{2a^{2}}$"),
        ('C', r"$\dfrac cb+\dfrac bc$ 的最大值为 $\sqrt5$"),
        ('D', r"$\dfrac{bc}{a^{2}}$ 的最大值为 $1$"),
    ],
    'answer': 'C',
    'analysis': (
        r"$S=\frac12bc\sin A=\frac{a^{2}}2$ ⟹ $a^{2}=bc\sin A$。结合余弦定理得 $b^{2}+c^{2}=bc(\sin A+2\cos A)$，" "\n"
        r"故 $\frac cb+\frac bc=\sin A+2\cos A\le\sqrt5$。而 $\frac{bc}{a^{2}}=\frac1{\sin A}\ge1$，是最小值。"
    ),
    'solution': (
        r"由 $S=\dfrac12bc\sin A=\dfrac{a^{2}}2$ 得 $a^{2}=bc\sin A$ ①。" "\n"
        r"**A**：由① $bc=\dfrac{a^{2}}{\sin A}$，一般不等于 $a$，A 错误。" "\n"
        r"**B**：由余弦定理 $b^{2}+c^{2}-a^{2}=2bc\cos A$，故" "\n"
        r"$\dfrac{b^{2}+c^{2}-a^{2}}{2a^{2}}=\dfrac{2bc\cos A}{2bc\sin A}=\cot A$，即 $\tan A=\dfrac{2a^{2}}{b^{2}+c^{2}-a^{2}}$，B 错误。" "\n"
        r"**C**：由余弦定理 $a^{2}=b^{2}+c^{2}-2bc\cos A$，与①联立：" "\n"
        r"$bc\sin A=b^{2}+c^{2}-2bc\cos A\Rightarrow b^{2}+c^{2}=bc(\sin A+2\cos A)$。" "\n"
        r"两边除以 $bc$：$\dfrac cb+\dfrac bc=\sin A+2\cos A=\sqrt5\sin(A+\varphi)$（$\tan\varphi=2$）。" "\n"
        r"当 $A+\varphi=\dfrac\pi2$ 时取最大值 $\sqrt5$，C 正确。" "\n"
        r"**D**：$\dfrac{bc}{a^{2}}=\dfrac{bc}{bc\sin A}=\dfrac1{\sin A}$，由 $\sin A\in(0,1]$ 得 $\dfrac1{\sin A}\in[1,+\infty)$，" "\n"
        r"即**最小**值为 $1$（无最大值），D 错误。" "\n"
        r"故选 C。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p177 详解：「在 $\triangle ABC$ 中，$S=\frac{a^2}2=\frac12bc\sin A$ ⟹ $a^2=bc\sin A$，" "\n"
        r"∵$\sin A\ne0$，∴$bc=\frac{a^2}{\sin A}$，故 A 错误；由余弦定理知 $a^2=b^2+c^2-2bc\cos A=bc\sin A$ ①，" "\n"
        r"则 $b^2+c^2-a^2=2bc\cos A$，所以 $\frac{b^2+c^2-a^2}{2a^2}=\frac{2bc\cos A}{2bc\sin A}=\frac1{\tan A}$ ⟹ $\tan A=\frac{2a^2}{b^2+c^2-a^2}$，故 B 错误；" "\n"
        r"由①可知 $bc(\sin A+2\cos A)=b^2+c^2$ ⟹ $\frac{b^2+c^2}{bc}=\sin A+2\cos A$，即 $\frac cb+\frac bc=\sqrt5\sin(A+\varphi)$，其中 $\tan\varphi=2$，" "\n"
        r"当 $A+\varphi=\frac\pi2$ 时，$\frac cb+\frac bc$ 取得最大值 $\sqrt5$，C 正确；$\frac{bc}{a^2}=\frac{bc}{bc\sin A}=\frac1{\sin A}$，" "\n"
        r"∵$A\in(0,\pi)$，∴$\sin A\in(0,1]$，则 $\frac{bc}{a^2}=\frac1{\sin A}\in[1,+\infty)$，所以 $\frac{bc}{a^2}$ 的最小值为 $1$，D 错误. 故选：C」" "\n"
        r"—— **$a^2=bc\sin A$、$\tan A=\frac{2a^2}{b^2+c^2-a^2}$、$\sqrt5\sin(A+\varphi)$、$\frac{bc}{a^2}$ 最小值为 $1$、答案 C 全部与我的推导一致** ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **$a^2=bc\sin A$**：$S=\frac12bc\sin A=\frac{a^2}2$ ⟹ $bc\sin A=a^2$ ✓✓✓" "\n"
        r"② **B 错误**：$\tan A$ 应为 $\frac{2a^2}{b^2+c^2-a^2}$，而选项是 $\frac{b^2+c^2-a^2}{2a^2}$ —— " "\n"
        r"**两者互为倒数** ✓✓✓ 故 B 必错" "\n"
        r"③ **$\frac cb+\frac bc=\sin A+2\cos A$**：由 $b^2+c^2=bc\sin A+2bc\cos A$，除以 $bc$ ✓✓✓" "\n"
        r"④ **最大值 $\sqrt5$**：$\sin A+2\cos A$ 的振幅 $=\sqrt{1+4}=\sqrt5=2.2361$ ✓✓✓" "\n"
        r"取等时 $\tan A=\frac{\sin A}{\cos A}$ 满足 $A+\varphi=\frac\pi2$（$\tan\varphi=2$）⟹ $\tan A=\frac12$，$A\approx26.57^\circ$（在 $(0,\pi)$ 内 ✓ 可达）" "\n"
        r"⑤ **D 错误**：$\frac1{\sin A}\ge1$，**最小**值 $1$；且 $\sin A\to0$ 时无上界 ✓✓✓" "\n"
        r"⑥ **数值检验**：取 $A$ 使 $\tan A=\frac12$，则 $\sin A=\frac1{\sqrt5}=0.4472$、$\cos A=\frac2{\sqrt5}=0.8944$。" "\n"
        r"取 $b=1$，则 $b^2+c^2=bc(\sin A+2\cos A)=c(0.4472+1.7889)=2.2361c$ ⟹ $1+c^2=2.2361c$" "\n"
        r"⟹ $c^2-2.2361c+1=0$ ⟹ $c=\frac{2.2361\pm\sqrt5-4}{2}=\frac{2.2361\pm1}{2}$ ⟹ $c=1.6180$ 或 $0.6180$（互为倒数 ✓）。" "\n"
        r"取 $c=1.6180$：$a^2=bc\sin A=1.6180(0.4472)=0.7236$，$a=0.8506$。" "\n"
        r"验余弦定理：$b^2+c^2-2bc\cos A=1+2.6180-2(1.6180)(0.8944)=3.6180-2.8944=0.7236$ ✓✓✓ **等于 $a^2$**" "\n"
        r"$\frac cb+\frac bc=1.6180+0.6180=2.2361=\sqrt5$ ✓✓✓ **达到最大值**" "\n"
        r"$\frac{bc}{a^2}=\frac{1.6180}{0.7236}=2.2361>1$，验 $\frac1{\sin A}=\frac1{0.4472}=2.2361$ ✓✓✓" "\n"
        r"**答案 C 正确** ✓" "\n"
        r"**⭐⭐ 通法（$S=\frac{a^2}2$ 型 ⟹ 全部用 $\sin A,\cos A$ 表达）**：" "\n"
        r"① ⭐⭐ **$a^2=bc\sin A$ 与 $a^2=b^2+c^2-2bc\cos A$ 联立**，消去 $a^2$ 得 $b^2+c^2=bc(\sin A+2\cos A)$ —— " "\n"
        r"**这一式是后面所有选项的源头**；" "\n"
        r"② ⭐⭐ **$\frac cb+\frac bc=\frac{b^2+c^2}{bc}$** —— 看到所求就应想到要把条件化成 $\frac{b^2+c^2}{bc}$，" "\n"
        r"这与 M-T-194-V2 是**完全相同的套路**；" "\n"
        r"③ ⭐ **「最大」还是「最小」要看清**：$\frac1{\sin A}\ge1$ 有下界无上界，" "\n"
        r"**选项 D 把「最小」写成「最大」，是命题人最爱的偷换**；" "\n"
        r"④ ⚠ **选项 B 是倒数陷阱**：正确式与选项互为倒数，**不必重算，看一眼就知道错**；" "\n"
        r"⑤ 检验：**由结论反解出 $b,c$，代回验余弦定理**（$0.7236=0.7236$ ✓）并**验最大值确实达到**（$2.2361$ ✓）。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-212'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-212-V1',
}

T212_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知非等腰 $\triangle ABC$ 的内角 $A$、$B$、$C$ 的对边分别是 $a$、$b$、$c$，且"
        r"$\dfrac{a^{4}+b^{4}+c^{4}+a^{2}b^{2}}{a^{2}+b^{2}}=2c^{2}$，若 $c$ 为最大边，则 $\dfrac{a+b}{2c}$ 的取值范围是（　　）"
    ),
    'opts': [
        ('A', r"$\left(\dfrac12,\dfrac{\sqrt3}3\right)$"),
        ('B', r"$\left(\dfrac12,\sqrt3\right)$"),
        ('C', r"$\left(\dfrac12,\dfrac{\sqrt3}3\right]$"),
        ('D', r"$\left(\dfrac12,\sqrt3\right]$"),
    ],
    'answer': 'A',
    'analysis': (
        r"条件化为 $(a^{2}+b^{2}-c^{2})^{2}=a^{2}b^{2}$，由 $c$ 最大得 $\cos C=-\frac12$、$C=120^\circ$。非等腰 ⟹ $ab<\frac{(a+b)^{2}}4$ 严格，两端都取不到。"
    ),
    'solution': (
        r"由条件去分母：$a^{4}+b^{4}+c^{4}+a^{2}b^{2}=2c^{2}(a^{2}+b^{2})$。" "\n"
        r"整理：$(a^{2}+b^{2})^{2}-2a^{2}b^{2}+c^{4}+a^{2}b^{2}=2c^{2}(a^{2}+b^{2})$，" "\n"
        r"即 $(a^{2}+b^{2})^{2}+c^{4}-2c^{2}(a^{2}+b^{2})=a^{2}b^{2}$，" "\n"
        r"即 $(a^{2}+b^{2}-c^{2})^{2}=a^{2}b^{2}$。" "\n"
        r"故 $\dfrac{a^{2}+b^{2}-c^{2}}{2ab}=\pm\dfrac12$。因 $c$ 为最大边，$\cos C=\dfrac{a^{2}+b^{2}-c^{2}}{2ab}<0$，" "\n"
        r"故 $\cos C=-\dfrac12$，$C=\dfrac{2\pi}3$。" "\n"
        r"由余弦定理：$c^{2}=a^{2}+b^{2}-2ab\cos C=a^{2}+b^{2}+ab=(a+b)^{2}-ab$。" "\n"
        r"因 $\triangle ABC$ **非等腰**，故 $a\ne b$，于是 $ab<\dfrac{(a+b)^{2}}4$（严格），" "\n"
        r"$c^{2}>(a+b)^{2}-\dfrac{(a+b)^{2}}4=\dfrac34(a+b)^{2}$，" "\n"
        r"即 $c>\dfrac{\sqrt3}2(a+b)$，故 $\dfrac{a+b}{2c}<\dfrac{\sqrt3}3$。" "\n"
        r"又由三角形两边之和大于第三边：$a+b>c$，故 $\dfrac{a+b}{2c}>\dfrac12$。" "\n"
        r"所以 $\dfrac{a+b}{2c}\in\left(\dfrac12,\dfrac{\sqrt3}3\right)$（**两端均为开区间**）。故选 A。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p177 详解：「$(a^2+b^2)^2+c^4-a^2b^2=2c^2(a^2+b^2)$，" "\n"
        r"即 $(a^2+b^2)^2+c^4-2c^2(a^2+b^2)=a^2b^2$ 即 $(a^2+b^2-c^2)^2=a^2b^2$，所以 $\frac{a^2+b^2-c^2}{2ab}=\pm\frac12$，因为 $c$ 为最大边，" "\n"
        r"所以 $\cos C=-\frac12$，由余弦定理得 $c^2=a^2+b^2+ab=(a+b)^2-ab>(a+b)^2-\frac{(a+b)^2}4=\frac34(a+b)^2$，" "\n"
        r"所以 $c>\frac{\sqrt3}2(a+b)$，即 $\frac{a+b}c<\frac{2\sqrt3}3$，又 $a+b>c$，所以 $1<\frac{a+b}c<\frac{2\sqrt3}3$，" "\n"
        r"所以 $\frac12<\frac{a+b}{2c}<\frac{\sqrt3}3$。故选：A。」" "\n"
        r"—— **$(a^2+b^2-c^2)^2=a^2b^2$、$\cos C=-\frac12$、$c^2=(a+b)^2-ab$、$(\frac12,\frac{\sqrt3}3)$、答案 A 全部与我的推导一致** ✓✓✓" "\n"
        r"（⚠ **A、C 两选项在提取中都只剩数字 $\frac12,\frac{\sqrt3}3$，括号类型丢失**。" "\n"
        r"我按数学正确性把 **A 设为两端都开**、C 设为右端闭 —— 因为「非等腰」使上界取不到、" "\n"
        r"三角形不等式使下界取不到。若实际印刷相反，以原书为准；此处记录我的判定依据。）" "\n"
        r"**独立验算**：" "\n"
        r"① **$(a^2+b^2-c^2)^2=a^2b^2$ 的推导**：" "\n"
        r"$(a^2+b^2)^2 = a^4+2a^2b^2+b^4$。原式移项：$a^4+b^4+c^4+a^2b^2-2c^2(a^2+b^2)=0$。" "\n"
        r"$= (a^2+b^2)^2 - a^2b^2 + c^4 - 2c^2(a^2+b^2)$（因为 $a^4+b^4+a^2b^2=(a^2+b^2)^2-a^2b^2$）" "\n"
        r"$= [(a^2+b^2)-c^2]^2 - a^2b^2 = 0$ ✓✓✓" "\n"
        r"② **$\cos C=-\frac12$（取负号）**：$c$ 为最大边 ⟹ $C$ 为最大角 ⟹ $C>\frac\pi3$，故 $\cos C<\frac12$；" "\n"
        r"又 $\cos C=\pm\frac12$，故只能取 $-\frac12$ ⟹ $C=120^\circ$ ✓✓✓" "\n"
        r"③ **$c^2=a^2+b^2+ab$**：$\cos C=-\frac12$ ⟹ $c^2=a^2+b^2-2ab(-\frac12)=a^2+b^2+ab$ ✓✓✓" "\n"
        r"④ **上界**：$c^2=(a+b)^2-ab$，非等腰 $a\ne b$ ⟹ $ab<\frac{(a+b)^2}{4}$ ⟹ $c^2>\frac34(a+b)^2$ ⟹ $\frac{a+b}{2c}<\frac1{\sqrt3}=\frac{\sqrt3}3$ ✓✓✓" "\n"
        r"⑤ **下界**：$a+b>c$ ⟹ $\frac{a+b}{2c}>\frac12$ ✓✓✓" "\n"
        r"⑥ **数值检验（$a=1,b=2$）**：$c^2=1+4+2=7$、$c=2.6458$。" "\n"
        r"验 $c$ 是最大边：$2.6458>2>1$ ✓；验三角形：$1+2>2.6458$ ✓" "\n"
        r"$\frac{a+b}{2c}=\frac3{5.2915}=0.5669$。" "\n"
        r"区间 $(\frac12,\frac{\sqrt3}3)=(0.5,0.5774)$，$0.5669$ 在其中 ✓✓✓" "\n"
        r"验原条件：$\frac{a^4+b^4+c^4+a^2b^2}{a^2+b^2}=\frac{1+16+49+4}{1+4}=\frac{70}5=14$；$2c^2=2(7)=14$ ✓✓✓ **完全吻合**" "\n"
        r"⑦ **上界逼近**：取 $a=1,b=1.01$（几乎等腰），$c^2=1+1.0201+1.01=3.0301$、$c=1.7407$。" "\n"
        r"$\frac{a+b}{2c}=\frac{2.01}{3.4814}=0.5774$ ✓✓✓ **逼近 $\frac{\sqrt3}3=0.57735$ 但取不到（因 $a\ne b$）**" "\n"
        r"**答案 A 正确** ✓" "\n"
        r"**⭐⭐ 通法（四次式条件 ⟹ 配成完全平方）**：" "\n"
        r"① ⭐⭐ **看到 $a^4+b^4+c^4$ 就要往 $(a^2+b^2-c^2)^2$ 上凑**：" "\n"
        r"$(a^2+b^2-c^2)^2=a^4+b^4+c^4+2a^2b^2-2a^2c^2-2b^2c^2$ —— " "\n"
        r"**交叉项正好是 $-2c^2(a^2+b^2)$，与去分母后的式子匹配**；" "\n"
        r"② ⭐ **$c$ 最大 ⟹ $\cos C$ 取负**：$(a^2+b^2-c^2)^2=a^2b^2$ 给出 $\cos C=\pm\frac12$，**必须靠「最大边」定号**；" "\n"
        r"③ ⭐⭐ **「非等腰」这个词不是废话**：它把 $ab\le\frac{(a+b)^2}4$ 变成严格小于，" "\n"
        r"从而**区间右端由闭变开** —— 这正是 A 与 C 的区别；" "\n"
        r"④ ⭐ **两条边界的来源要分清**：上界来自基本不等式（非等腰），下界来自三角形不等式 $a+b>c$；" "\n"
        r"⑤ 检验：**取 $a=1,b=2$ 验原条件成立**（$14=14$ ✓），**取 $a\approx b$ 看上界逼近**（$0.5774$ ✓）。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-212'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-212-V2',
}

T212_V3 = {
    'type': '选择',
    'stem_text': (
        r"设 $A(-2,0)$、$B(2,0)$，$O$ 为坐标原点，点 $P$ 满足 $\lvert PA\rvert^{2}+\lvert PB\rvert^{2}\le16$，"
        r"若直线 $kx-y+6=0$ 上存在点 $Q$ 使得 $\angle PQO=\dfrac\pi6$，则实数 $k$ 的取值范围为（　　）"
    ),
    'opts': [
        ('A', r"$\left[-4\sqrt2,4\sqrt2\right]$"),
        ('B', r"$\left(-\infty,-4\sqrt2\right]\cup\left[4\sqrt2,+\infty\right)$"),
        ('C', r"$\left(-\infty,-\dfrac{\sqrt5}2\right]\cup\left[\dfrac{\sqrt5}2,+\infty\right)$"),
        ('D', r"$\left[-\dfrac{\sqrt5}2,\dfrac{\sqrt5}2\right]$"),
    ],
    'answer': 'C',
    'analysis': (
        r"由 $\lvert PA\rvert^{2}+\lvert PB\rvert^{2}\le16$ 得 $\lvert OP\rvert\le2$。在 $\triangle PQO$ 中用正弦定理得"
        r"$\lvert OQ\rvert=2\lvert OP\rvert\sin\angle QPO\le4$。故只需原点到直线的距离 $\le4$。"
    ),
    'solution': (
        r"设 $P(x,y)$，则" "\n"
        r"$\lvert PA\rvert^{2}+\lvert PB\rvert^{2}=(x+2)^{2}+y^{2}+(x-2)^{2}+y^{2}=2x^{2}+8+2y^{2}\le16$，" "\n"
        r"即 $x^{2}+y^{2}\le4$，故 $\lvert OP\rvert\le2$。" "\n"
        r"在 $\triangle PQO$ 中，由正弦定理 $\dfrac{\lvert OQ\rvert}{\sin\angle QPO}=\dfrac{\lvert OP\rvert}{\sin\angle PQO}$：" "\n"
        r"$\lvert OQ\rvert=\dfrac{\lvert OP\rvert\sin\angle QPO}{\sin\frac\pi6}=2\lvert OP\rvert\sin\angle QPO\le2\times2\times1=4$。" "\n"
        r"（当 $\lvert OP\rvert=2$ 且 $\angle QPO=\frac\pi2$ 时取到 $4$。）" "\n"
        r"因此「直线上存在点 $Q$ 使 $\angle PQO=\frac\pi6$」等价于「存在 $Q$ 使 $\lvert OQ\rvert\le4$」" "\n"
        r"（$\lvert OQ\rvert$ 可连续取到 $\ge d$ 的一切值，其中 $d$ 为原点到直线的距离）。" "\n"
        r"故只需 $d\le4$。" "\n"
        r"原点到直线 $kx-y+6=0$ 的距离 $d=\dfrac{\lvert6\rvert}{\sqrt{k^{2}+1}}$，于是" "\n"
        r"$\dfrac6{\sqrt{k^{2}+1}}\le4\Rightarrow\sqrt{k^{2}+1}\ge\dfrac32\Rightarrow k^{2}+1\ge\dfrac94\Rightarrow k^{2}\ge\dfrac54$。" "\n"
        r"所以 $k\le-\dfrac{\sqrt5}2$ 或 $k\ge\dfrac{\sqrt5}2$。故选 C。"
    ),
    'review': (
        r"★ 题干、答案、详解完整 ✓。原书 p177 详解：「设 $P(x,y)$，则 $|PA|^2+|PB|^2=(x+2)^2+y^2+(x-2)^2+y^2\le16$，整理可得 $x^2+y^2\le4$，" "\n"
        r"故 $|OP|\le2$，在 $\triangle PQO$ 中，$\frac{|OQ|}{\sin\angle QPO}=\frac{|OP|}{\sin\angle PQO}$，" "\n"
        r"则 $|OQ|=\frac{|OP|\sin\angle QPO}{\sin\angle PQO}=2|OP|\sin\angle QPO\le2\times2\times1=4$，设原点到直线的距离为 $d$，则需满足 $d\le4$，" "\n"
        r"∴$d=\frac6{\sqrt{k^2+1}}\le4$，解得 $k\le-\frac{\sqrt5}2$ 或 $k\ge\frac{\sqrt5}2$. 故选：C.」" "\n"
        r"—— **$x^2+y^2\le4$、$|OP|\le2$、$|OQ|\le4$、$d=\frac6{\sqrt{k^2+1}}\le4$、$k^2\ge\frac54$、答案 C 全部与我的推导一致** ✓✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **$|PA|^2+|PB|^2=2x^2+2y^2+8$**：$(x+2)^2+(x-2)^2=x^2+4x+4+x^2-4x+4=2x^2+8$ ✓✓✓" "\n"
        r"$\le16$ ⟹ $2x^2+2y^2\le8$ ⟹ $x^2+y^2\le4$ ✓✓✓ **$|OP|\le2$**" "\n"
        r"② **正弦定理**：$\triangle PQO$ 中 $\frac{|OQ|}{\sin\angle QPO}=\frac{|OP|}{\sin\angle PQO}$ ✓✓✓（$|OQ|$ 对 $\angle QPO$，$|OP|$ 对 $\angle PQO$）" "\n"
        r"$|OQ|=\frac{|OP|\sin\angle QPO}{\sin(\pi/6)}=2|OP|\sin\angle QPO\le 2\cdot2\cdot1=4$ ✓✓✓" "\n"
        r"③ **距离公式**：点 $(0,0)$ 到 $kx-y+6=0$ 的距离 $=\frac{|k\cdot0-0+6|}{\sqrt{k^2+1}}=\frac6{\sqrt{k^2+1}}$ ✓✓✓" "\n"
        r"④ **解不等式**：$\frac6{\sqrt{k^2+1}}\le4$ ⟹ $\sqrt{k^2+1}\ge1.5$ ⟹ $k^2\ge1.25$ ⟹ $|k|\ge1.1180=\frac{\sqrt5}2$ ✓✓✓" "\n"
        r"⑤ **数值检验（$k=2$，应满足）**：$d=\frac6{\sqrt5}=\frac6{2.2361}=2.6833\le4$ ✓。" "\n"
        r"直线 $2x-y+6=0$。取 $Q$ 使 $|OQ|$ 尽量小：垂足方向。垂足 $=\frac{-6}{k^2+1}(k,-1)=\frac{-6}5(2,-1)=(-2.4,1.2)$。" "\n"
        r"$|OQ|=\sqrt{5.76+1.44}=\sqrt{7.2}=2.6833$ ✓ 与 $d$ 一致。" "\n"
        r"需在此直线上找 $Q$ 使 $|OQ|\le4$ 且能与某个 $P$（$|OP|\le2$）构成 $\angle PQO=30^\circ$。" "\n"
        r"沿直线从垂足移动可让 $|OQ|$ 取遍 $[2.6833,+\infty)$，故可取 $|OQ|=4$ ✓✓✓ **可行**" "\n"
        r"⑥ **数值检验（$k=1$，不应满足）**：$d=\frac6{\sqrt2}=4.2426>4$ ✗。" "\n"
        r"直线上所有点 $|OQ|\ge4.2426>4$，而需要 $|OQ|\le4$ ⟹ **不可行** ✓✓✓" "\n"
        r"⑦ **边界 $k=\frac{\sqrt5}2=1.1180$**：$d=\frac6{\sqrt{1.25+1}}=\frac6{1.5}=4$ ✓ **恰为临界，取等（闭区间）** ✓✓✓" "\n"
        r"⑧ **选项排除**：A、D 是「中间闭区间」（方向反了）；B 用 $4\sqrt2=5.657$ 作临界（那是把 $d\le\frac{6}{4\sqrt2}$ 之类的错误代入）✗" "\n"
        r"**答案 C 正确** ✓" "\n"
        r"**⭐⭐ 通法（「直线上存在点满足角度条件」⟹ 距离条件）**：" "\n"
        r"① ⭐⭐ **$\lvert PA\rvert^{2}+\lvert PB\rvert^{2}=2\lvert PO\rvert^{2}+\frac{\lvert AB\rvert^{2}}2$**（中线定理/阿波罗尼斯）：" "\n"
        r"本题给出 $2(x^2+y^2)+8\le16$ ⟹ $|OP|\le2$，**这是把动点限制在一个圆内的标准手法**；" "\n"
        r"② ⭐⭐ **「$\angle PQO=\frac\pi6$」用正弦定理转化成 $\lvert OQ\rvert$ 的上界** —— " "\n"
        r"固定一个角，把未知的边（$OQ$）用已知量（$OP$）和另一个角的正弦表示，**取 $\sin\le1$ 得上界**；" "\n"
        r"③ ⭐⭐ **「直线上存在点 $Q$ 使 $|OQ|\le r$」⟺ 原点到直线的距离 $d\le r$** —— " "\n"
        r"因为 $|OQ|$ 沿直线从 $d$ 连续增大到 $+\infty$，**可取值范围是 $[d,+\infty)$**；" "\n"
        r"④ ⚠ **方向别搞反**：条件给出的是 $|OQ|\le4$，要求直线**离原点足够近**（$d\le4$），" "\n"
        r"于是 $k$ 要**足够大**（$|k|\ge\frac{\sqrt5}2$），对应**两侧区间**而非中间区间 —— " "\n"
        r"**A、D 就是为「方向搞反」准备的**；" "\n"
        r"⑤ 检验：**取 $k=2$（可行）与 $k=1$（不可行）各验一次**，并**验边界 $k=\frac{\sqrt5}2$ 时 $d$ 恰为 $4$** ✓。"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-212'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-212-V3',
}

QS = [T191_E1, T191_V1, T191_V2, T191_V3, T194_E1, T194_V1, T194_V2, T194_V3,
      T212_E1, T212_V1, T212_V2, T212_V3]
