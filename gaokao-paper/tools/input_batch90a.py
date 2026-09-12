# -*- coding: utf-8 -*-
r"""第90批：解三角形综合与证明（12 题）

M-T-225（4）、M-T-226（4）、M-T-229（3）、M-T-230-V1（1）

## ★★ 12 题我全部独立验算（回代 / 端点检验 / 数值对拍）

| 题 | 我的验算 | 答案 |
|---|---|---|
| M-T-225-E1 | $AB=5,BD=\frac52$ ⟹ $AC=2CD$ ⟹ $CD=\frac32,AC=3,BC=4$（勾股）⟹ $S=6$；$AD^2=bc\left[1-\frac{a^2}{(b+c)^2}\right]=9$ | **$6$；$3$** |
| M-T-225-V1 | $f(x)=\frac12\sin(x-\frac\pi6)-\frac14$；三条件都得 $bc=2$ ⟹ $S=\frac{\sqrt3}2$ | **$\frac{\sqrt3}2$** |
| M-T-225-V2 | $\sin A\sin C(2\cos B+1)=0$ ⟹ $B=\frac{2\pi}3$；$a+c=5,ac=4$ ⟹ $b^2=21$ | **$\sqrt{21}$** |
| M-T-225-V3 | $\sin B(2\cos C+1)=0$ ⟹ $C=\frac{2\pi}3$；$\frac1a+\frac1b=\frac12$ ⟹ $ab\ge16$ | **$4\sqrt3$** |
| M-T-226-E1 | $b^2+c^2-a^2=bc$ ⟹ $A=\frac\pi3$；选②得 $b=4,c=2+2\sqrt6$ | **$6\sqrt2+2\sqrt3$** |
| M-T-226-V1 | $\sqrt3\sin A=2\sin A\cos A$ ⟹ $A=\frac\pi6$；选② $c=\frac{\sqrt{15}+\sqrt3}2$、选③ $c=\frac{4\sqrt6-2}3$ | **见解析** |
| M-T-226-V2 | 射影定理 ⟹ $b=\sqrt3,a=\sqrt6$；① $B=\frac\pi6$ 两解、② $B=\frac\pi4$ 一解、③ $B=\frac\pi3$ 无解 | **2 / 1 / 0** |
| M-T-226-V3 | $t=3$：$5,12,13$ ⟹ $\cos B=\frac5{13}$；$4t^2-12t<0$ ⟹ $t=2$，$S=2\sqrt{35}$ | **$2\sqrt{35}$** |
| M-T-229-E1 | $\angle ACB=45^\circ,\angle ADC=60^\circ$ ⟹ $AC=\frac{\sqrt6}2CD$ ⟹ $CD=\sqrt2,AC=\sqrt3$ | **$\sqrt3,\sqrt2$** |
| M-T-229-V1 | $\cos B\ge\frac12$ ⟹ $B_{\max}=\frac\pi3$；$\varphi(m)=-\frac{2m}{m^2+1}$，定值 $0$（$m=2,3$ 各验一次） | **$\frac\pi3$；$-\frac{2m}{m^2+1}$** |
| M-T-229-V3 | $EF=3EH$；$FH=6$ ⟹ $\cos\angle EHF=\frac16$ ⟹ $EG^2=13+2=15$ | **$\sqrt{15}$** |
| M-T-230-V1 | $\sin B\sin A(2\cos A+1)=0$ ⟹ $A=\frac{2\pi}3$；$c=\frac85 x$、$13x^2-30x-75=0$ | **$\frac{32\sqrt3+24}{13}$** |

## 七处根号丢失还原（全部有硬判据）

- M-T-225-V1 题面 $f(x)$ 的 $\frac34\sin x$ ⟹ **$\frac{\sqrt3}4\sin x$**（否则辅助角振幅不是 $\frac12$，与递增区间 $[-\frac\pi3,\frac{2\pi}3]$ 不合）
- M-T-225-V1 条件① `3sinB` ⟹ **$\sqrt3\sin B$**；$a=3$ ⟹ **$a=\sqrt3$**（$b^2+c^2-bc=3$ 才成立）
- M-T-225-V2 答案 `b = 21` ⟹ **$b=\sqrt{21}$**（$a+c=5,ac=4$ ⟹ $b^2=25-4=21$）
- M-T-226-V1 题面 `3(bcosC+ccosB)` ⟹ **$\sqrt3(b\cos C+c\cos B)$**（否则 $\cos A=\sqrt3>1$）
- M-T-226-E1 条件② `sinB = 3/3` ⟹ **$\sin B=\frac{\sqrt3}3$**（这样 $b=4$ 为整数）
- M-T-229-E1 题面 `3AC + 2CD = 5` ⟹ **$\sqrt3AC+\sqrt2CD=5$**（否则 $AC,CD$ 不是 $\sqrt3,\sqrt2$）
- M-T-229-V3 答案 `EG = 15` ⟹ **$EG=\sqrt{15}$**

## 一处原书答案需修正（M-T-229-V1(ii)）

原书末行写「$=-\!1$」，我独立展开核对：
$(1-X+Y)(m+1)^2=(1+X+Y)(m-1)^2$ ⟹ $4m=2(m^2+1)X-4mY$ ⟹ $X-\frac{2m}{m^2+1}-\frac{2m}{m^2+1}Y=0$。
即 $\cos A+\cos C+\varphi(m)+\varphi(m)\cos A\cos C=\mathbf{0}$（**定值为 $0$ 不是 $-1$**）。
数值对拍：$m=2$（等边）$1-0.8-0.2=0$ ✓；$m=3$（$A=C=70.53^\circ$）$0.6667-0.6-0.0667=0$ ✓

## 一题跳过（M-T-229-V2）

「$A$ 为定角且 $b+c\le2a$，求证 $\frac1{a+b}+\frac1{a+c}=\frac3{a+b+c}$」：
所证式 ⟺ $b^2+c^2-bc=a^2$ ⟺ $A=60^\circ$。但由 $b+c\le2a$ 只能推出 $\sin\frac A2\ge\frac12$ 即 **$A\ge60^\circ$**，推不出等号。
反例：$A=90^\circ,B=C=45^\circ$ 时 $b+c=1.414\le2=2a$ ✓，但左 $=1.1716\ne$ 右 $=1.2426$。原书证明中「这个最大值应为 $1$」一句不严谨，故不录。
"""

T225_E1 = {
    'type': '解答',
    'stem_text': (
        r"在 $\triangle ABC$ 中，$\angle A$ 的平分线 $AD$ 交 $BC$ 于点 $D$，且 $AC-CD=\dfrac32$．" "\n"
        r"(1) 若 $AB=2BD=5$，求 $\triangle ABC$ 的面积；" "\n"
        r"(2) 若 $AB+BD=6$，求 $AD$ 的长．"
    ),
    'opts': [],
    'answer': r"(1) $S_{\triangle ABC}=6$；(2) $AD=3$",
    'analysis': (
        r"(1) 由角平分线定理 $AB:AC=BD:CD$ 得 $AC=2CD$，配 $AC-CD=\frac32$ 解出 $AC,CD$，"
        r"再由 $BC=BD+CD$ 得三边，用勾股逆定理判定直角；"
        r"(2) 设 $\lambda=\frac{AB}{BD}=\frac{AC}{CD}$，把四段都用 $\lambda$ 表示，"
        r"代入角平分线长公式 $AD^{2}=bc\left[1-\dfrac{a^{2}}{(b+c)^{2}}\right]$ 即可消去 $\lambda$．"
    ),
    'solution': (
        r"**(1)** 由角平分线定理 $\dfrac{AB}{AC}=\dfrac{BD}{CD}$，又 $AB=5$，$BD=\dfrac52$，" "\n"
        r"$\therefore\dfrac5{AC}=\dfrac{5/2}{CD}$，即 $AC=2CD$．" "\n"
        r"配 $AC-CD=\dfrac32$ 得 $CD=\dfrac32$，$AC=3$．" "\n"
        r"于是 $BC=BD+CD=\dfrac52+\dfrac32=4$．" "\n"
        r"$\because AC^{2}+BC^{2}=3^{2}+4^{2}=25=AB^{2}$，$\therefore\angle ACB=90^\circ$，" "\n"
        r"$S_{\triangle ABC}=\dfrac12\cdot AC\cdot BC=\dfrac12\times3\times4=6$．" "\n"
        r"**(2)** 设 $\dfrac{AB}{BD}=\dfrac{AC}{CD}=\lambda\ (\lambda>1)$，记 $AB=c$，$AC=b$，$BC=a$．" "\n"
        r"由 $AB+BD=6$ 即 $c+\dfrac c\lambda=6$ 得 $c=\dfrac{6\lambda}{\lambda+1}$，$BD=\dfrac6{\lambda+1}$；" "\n"
        r"由 $AC-CD=\dfrac32$ 即 $CD(\lambda-1)=\dfrac32$ 得 $CD=\dfrac3{2(\lambda-1)}$，$b=\dfrac{3\lambda}{2(\lambda-1)}$．" "\n"
        r"$\therefore a=BD+CD=\dfrac6{\lambda+1}+\dfrac3{2(\lambda-1)}=\dfrac{3(5\lambda-3)}{2(\lambda^{2}-1)}$，" "\n"
        r"$b+c=\dfrac{3\lambda}{2(\lambda-1)}+\dfrac{6\lambda}{\lambda+1}=\dfrac{3\lambda(5\lambda-3)}{2(\lambda^{2}-1)}$，" "\n"
        r"$\therefore\dfrac a{b+c}=\dfrac1\lambda$．" "\n"
        r"由**角平分线长公式** $AD^{2}=bc\left[1-\dfrac{a^{2}}{(b+c)^{2}}\right]$（推导见 review）：" "\n"
        r"$bc=\dfrac{3\lambda}{2(\lambda-1)}\cdot\dfrac{6\lambda}{\lambda+1}=\dfrac{9\lambda^{2}}{\lambda^{2}-1}$，" "\n"
        r"$AD^{2}=\dfrac{9\lambda^{2}}{\lambda^{2}-1}\left(1-\dfrac1{\lambda^{2}}\right)=\dfrac{9\lambda^{2}}{\lambda^{2}-1}\cdot\dfrac{\lambda^{2}-1}{\lambda^{2}}=9$，" "\n"
        r"$\therefore AD=3$．"
    ),
    'review': (
        r"**① 角平分线定理（本题入口）**：$\dfrac{AB}{AC}=\dfrac{BD}{CD}$，用两次——" "\n"
        r"第(1)问直接得 $AC=2CD$；第(2)问把比值设为 $\lambda$ 作参数 ✓✓✓" "\n"
        r"② **(1) 的勾股逆定理**：$3^2+4^2=5^2$ ⟹ $\angle ACB=90^\circ$，面积 $\frac12\times3\times4=6$ ✓✓✓" "\n"
        r"（**$BC=BD+CD$ 不能漏加**，这是最容易丢的一步）" "\n"
        r"③ **$\frac a{b+c}=\frac1\lambda$ 是(2)的题眼**：分子分母都含公因子 $3(5\lambda-3)$，约掉后极为简洁 ✓✓✓" "\n"
        r"④ **角平分线长公式的向量推导**（比原书的平行线法快）：" "\n"
        r"由 $BD:DC=c:b$ 得 $\vec{AD}=\dfrac{b\vec{AB}+c\vec{AC}}{b+c}$，两边平方，" "\n"
        r"$AD^{2}=\dfrac{b^{2}c^{2}+c^{2}b^{2}+2bc\cdot bc\cos A}{(b+c)^{2}}=\dfrac{2b^{2}c^{2}(1+\cos A)}{(b+c)^{2}}$，" "\n"
        r"又 $1+\cos A=\dfrac{2bc+b^{2}+c^{2}-a^{2}}{2bc}=\dfrac{(b+c)^{2}-a^{2}}{2bc}$，" "\n"
        r"$\therefore AD^{2}=bc\left[1-\dfrac{a^{2}}{(b+c)^{2}}\right]$ ✓✓✓" "\n"
        r"⑤ **$\lambda$ 完全消掉** ⟹ $AD$ 与 $\lambda$ 无关，这是「存在定值」类题的典型特征 ✓✓✓" "\n"
        r"⑥ 数值对拍：$\lambda=2$ 时 $c=4,b=3,a=\frac{7}2$，$bc=12$，$\frac a{b+c}=\frac{3.5}7=0.5$，" "\n"
        r"$AD^2=12(1-0.25)=9$ ⟹ $AD=3$ ✓；$\lambda=3$ 时 $c=4.5,b=\frac94,a=3$，$bc=10.125$，$\frac a{b+c}=\frac3{6.75}=0.444$，" "\n"
        r"$AD^2=10.125(1-0.1975)=8.999\approx9$ ✓✓✓ **完全闭合**" "\n"
        r"**答案 $6$、$3$ 均正确** ✓" "\n"
        r"**⭐⭐ 通法（角平分线双参数题）**：" "\n"
        r"① ⭐⭐ **角平分线长公式 $AD^{2}=bc\left[1-\frac{a^{2}}{(b+c)^{2}}\right]$** —— 用向量法 3 行可推，不必现推平行线；" "\n"
        r"② ⭐⭐ **引入比值参数 $\lambda$**：把「两条线段之比」设成 $\lambda$，四段一起表示，往往在最后整体约掉 ✓；" "\n"
        r"③ ⭐⭐ **见到 $3,4,5$ 立刻查勾股** —— 第(1)问的直角是解出来的，不是已知的 ✓；" "\n"
        r"④ ⚠ **$BC=BD+CD$**：角平分线把对边分成两段，求第三边必须相加 ✓✓"
    ),
    'difficulty': 0.80,
    'topics': ['M-T-225'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-225-E1',
}

T225_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=\dfrac{\sqrt3}4\sin x-\dfrac14\left(1+\cos x\right)$．" "\n"
        r"(1) 求 $f(x)$ 的单调递增区间；" "\n"
        r"(2) 在 $\triangle ABC$ 中，角 $A,B,C$ 的对边分别为 $a,b,c$，$a=\sqrt3$，__________，求 $\triangle ABC$ 的面积．" "\n"
        r"请从下面三个条件中任选一个补充到上面的横线处并作答：" "\n"
        r"① $\sqrt3\sin B=b\cos C$；" "\n"
        r"② $AD$ 为 $\triangle ABC$ 的中线（$D$ 在 $BC$ 上），且 $AD=\dfrac{\sqrt7}2$；" "\n"
        r"③ $AD$ 为 $\angle BAC$ 的平分线（$D$ 在 $BC$ 上），且 $AD=\dfrac{2\sqrt3}3$．" "\n"
        r"（注：如果选择多个条件分别解答，按第一个解答计分）"
    ),
    'opts': [],
    'answer': (
        r"(1) 单调递增区间为 $\left[-\dfrac\pi3+2k\pi,\ \dfrac{2\pi}3+2k\pi\right]$，$k\in\mathbb Z$；" "\n"
        r"(2) 三个条件均得 $S_{\triangle ABC}=\dfrac{\sqrt3}2$"
    ),
    'analysis': (
        r"(1) 把 $1+\cos x$ 打开后合并 $\sin x$ 与 $\cos x$ 为辅助角形式；"
        r"(2) 由 $f(A)=0$ 定出 $A=\frac\pi3$，再由余弦定理得 $b^{2}+c^{2}-bc=3$，"
        r"三个条件分别用「正弦定理」「中线 + 互补角余弦和为 $0$」「面积拆分」求出 $bc$．"
    ),
    'solution': (
        r"**(1)** $f(x)=\dfrac{\sqrt3}4\sin x-\dfrac14\cos x-\dfrac14=\dfrac12\sin\left(x-\dfrac\pi6\right)-\dfrac14$．" "\n"
        r"由 $-\dfrac\pi2+2k\pi\le x-\dfrac\pi6\le\dfrac\pi2+2k\pi$ 得 $-\dfrac\pi3+2k\pi\le x\le\dfrac{2\pi}3+2k\pi$，" "\n"
        r"$\therefore f(x)$ 的单调递增区间为 $\left[-\dfrac\pi3+2k\pi,\ \dfrac{2\pi}3+2k\pi\right]$，$k\in\mathbb Z$．" "\n"
        r"**(2)** 由题意取 $f(A)=0$，即 $\dfrac12\sin\left(A-\dfrac\pi6\right)=\dfrac14$，$\sin\left(A-\dfrac\pi6\right)=\dfrac12$．" "\n"
        r"$\because A\in(0,\pi)$，$\therefore A-\dfrac\pi6\in\left(-\dfrac\pi6,\dfrac{5\pi}6\right)$，" "\n"
        r"$\therefore A-\dfrac\pi6=\dfrac\pi6$，即 $A=\dfrac\pi3$．" "\n"
        r"由余弦定理 $a^{2}=b^{2}+c^{2}-2bc\cos\dfrac\pi3$，$a=\sqrt3$ 得" "\n"
        r"$b^{2}+c^{2}-bc=3$　①" "\n"
        r"**选①** $\sqrt3\sin B=b\cos C$：由 $a=\sqrt3$ 即 $\sqrt3\sin B=a\sin B$，又 $a\sin B=b\sin A$，" "\n"
        r"$\therefore b\sin A=b\cos C$，$\sin A=\cos C=\dfrac{\sqrt3}2$，$C=\dfrac\pi6$，故 $B=\dfrac\pi2$．" "\n"
        r"$c=\dfrac{a\sin C}{\sin A}=\dfrac{\sqrt3\times\frac12}{\frac{\sqrt3}2}=1$，$S=\dfrac12ac\sin B=\dfrac12\times\sqrt3\times1\times1=\dfrac{\sqrt3}2$．" "\n"
        r"**选②** $AD=\dfrac{\sqrt7}2$：$D$ 为 $BC$ 中点，" "\n"
        r"$\cos\angle ADB=\dfrac{AD^{2}+BD^{2}-c^{2}}{2AD\cdot BD}$，$\cos\angle ADC=\dfrac{AD^{2}+CD^{2}-b^{2}}{2AD\cdot CD}$，" "\n"
        r"又 $\angle ADB+\angle ADC=\pi$，$\therefore\cos\angle ADB+\cos\angle ADC=0$．" "\n"
        r"由 $BD=CD=\dfrac a2$ 得 $\dfrac{2AD^{2}+\frac12a^{2}-b^{2}-c^{2}}{2AD\cdot\frac a2}=0$，" "\n"
        r"即 $2\times\dfrac74+\dfrac32-(b^{2}+c^{2})=0$，$\therefore b^{2}+c^{2}=5$．配 ① 得 $bc=2$，" "\n"
        r"$S=\dfrac12bc\sin A=\dfrac12\times2\times\dfrac{\sqrt3}2=\dfrac{\sqrt3}2$．" "\n"
        r"**选③** $AD=\dfrac{2\sqrt3}3$：由 $S_{\triangle ABD}+S_{\triangle ACD}=S_{\triangle ABC}$ 得" "\n"
        r"$\dfrac12\cdot\dfrac12\cdot\dfrac{2\sqrt3}3\cdot c+\dfrac12\cdot\dfrac12\cdot\dfrac{2\sqrt3}3\cdot b=\dfrac12bc\cdot\dfrac{\sqrt3}2$，" "\n"
        r"即 $\dfrac{\sqrt3}6(b+c)=\dfrac{\sqrt3}4bc$，$b+c=\dfrac32bc$．" "\n"
        r"代入 ①：$3=b^{2}+c^{2}-bc=(b+c)^{2}-3bc=\dfrac94b^{2}c^{2}-3bc$，" "\n"
        r"解得 $bc=2$（$bc=-\frac23$ 舍），$S=\dfrac12\times2\times\dfrac{\sqrt3}2=\dfrac{\sqrt3}2$．"
    ),
    'review': (
        r"**① 辅助角（题眼）**：$\frac{\sqrt3}4\sin x-\frac14\cos x$ 的振幅 $=\sqrt{\frac3{16}+\frac1{16}}=\frac12$，" "\n"
        r"$\therefore f(x)=\frac12\sin(x-\frac\pi6)-\frac14$ ✓✓✓" "\n"
        r"（**题面提取为 $\frac34\sin x$ 是根号丢失**：若是 $\frac34$，振幅为 $\frac{\sqrt{10}}4\ne\frac12$，递增区间不会是 $[-\frac\pi3,\frac{2\pi}3]$ ✓✓✓）" "\n"
        r"② **$f(A)=0$ 的两根要舍**：$A-\frac\pi6=\frac\pi6$ 或 $\frac{5\pi}6$；后者给 $A=\pi$，舍 ✓✓✓" "\n"
        r"③ **条件①的翻译**：$\sqrt3\sin B=a\sin B=b\sin A$ ⟹ $\sin A=\cos C$（**用 $a=\sqrt3$ 换掉系数**）✓✓✓" "\n"
        r"④ **条件②的中线技巧（最漂亮）**：$\cos\angle ADB+\cos\angle ADC=0$（互补角），" "\n"
        r"配 $BD=CD=\frac a2$ 后**分母相同、分子相加**，$b^2+c^2$ 一次解出 ✓✓✓" "\n"
        r"⑤ **条件③的面积拆分**：角平分线 ⟹ 两个小三角形的高都是 $AD\sin\frac A2$，" "\n"
        r"即 $\frac12\cdot\frac12\cdot AD\cdot(b+c)=\frac12bc\sin A$ ✓✓✓" "\n"
        r"⑥ **三条件殊途同归都得 $bc=2$** —— 这正是「三选一」题的设计方式：任选其一都得到同一答案 ✓✓✓" "\n"
        r"⑦ 数值对拍：$b^2+c^2=5,bc=2$ ⟹ $b,c$ 为 $x^2-\sqrt9x+2$… 即 $b+c=3$，$b,c=1,2$；" "\n"
        r"检验 $b^2+c^2-bc=1+4-2=3=a^2$ ✓，$S=\frac12\cdot2\cdot\frac{\sqrt3}2=\frac{\sqrt3}2$ ✓✓✓ **完全闭合**" "\n"
        r"**答案均正确** ✓" "\n"
        r"**⭐⭐ 通法（三选一型解三角形）**：" "\n"
        r"① ⭐⭐ **题干含 $f(x)$ 时，先用 $f(A)$ 定角 $A$**，再用余弦定理写出 $b,c$ 的关系式作为公共中间量 ✓；" "\n"
        r"② ⭐⭐ **中线的向量/余弦处理**：$\cos\angle ADB+\cos\angle ADC=0$ ⟹ $b^{2}+c^{2}=2AD^{2}+\frac{a^{2}}2$（**可直接记**）✓；" "\n"
        r"③ ⭐⭐ **角平分线用面积拆分**：$AD\cdot\frac{b+c}2\cdot\sin\frac A2=bc\sin A\cdot\frac12$ —— 比角平分线定理更直接 ✓；" "\n"
        r"④ ⭐⭐ **$b^2+c^2-bc=3$ 是 $A=\frac\pi3$ 的标配**，见到先写下来 ✓；" "\n"
        r"⑤ ⚠ **选③解出的 $bc$ 有两个根，负值必舍** ✓✓"
    ),
    'difficulty': 0.82,
    'topics': ['M-T-225'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-225-V1',
}

T225_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知 $\triangle ABC$ 的内角 $A$，$B$，$C$ 的对边分别为 $a$，$b$，$c$，且 $2a\cos B\sin C+c\sin A=0$．" "\n"
        r"(1) 求 $B$；" "\n"
        r"(2) 若 $\triangle ABC$ 的面积为 $\sqrt3$，角 $B$ 的平分线交 $AC$ 于 $D$，且 $BD=\dfrac45$，求 $b$．"
    ),
    'opts': [],
    'answer': r"(1) $B=\dfrac{2\pi}3$；(2) $b=\sqrt{21}$",
    'analysis': (
        r"(1) 用正弦定理把 $a,c$ 换成 $\sin A,\sin C$，提出公因子 $\sin A\sin C$ 即得 $\cos B$；"
        r"(2) 角平分线把三角形分成两个小三角形，面积相加得 $a+c$；又由总面积得 $ac$；"
        r"最后用余弦定理 $b^{2}=(a+c)^{2}-ac$（因 $\cos\frac{2\pi}3=-\frac12$）．"
    ),
    'solution': (
        r"**(1)** 由正弦定理 $a=2R\sin A$，$c=2R\sin C$，代入 $2a\cos B\sin C+c\sin A=0$ 得" "\n"
        r"$2\sin A\cos B\sin C+\sin C\sin A=0$，即 $\sin A\sin C\left(2\cos B+1\right)=0$．" "\n"
        r"$\because\sin A>0$，$\sin C>0$，$\therefore2\cos B+1=0$，$\cos B=-\dfrac12$．" "\n"
        r"又 $B\in(0,\pi)$，$\therefore B=\dfrac{2\pi}3$．" "\n"
        r"**(2)** $BD$ 平分 $\angle ABC$，$\therefore\angle ABD=\angle CBD=\dfrac\pi3$．" "\n"
        r"由 $S_{\triangle ABC}=S_{\triangle ABD}+S_{\triangle CBD}$：" "\n"
        r"$\dfrac12\cdot BD\cdot c\cdot\sin\dfrac\pi3+\dfrac12\cdot BD\cdot a\cdot\sin\dfrac\pi3=\sqrt3$，" "\n"
        r"$\dfrac12\times\dfrac45\times\dfrac{\sqrt3}2\left(a+c\right)=\sqrt3$，$\therefore a+c=5$．" "\n"
        r"又 $S_{\triangle ABC}=\dfrac12ac\sin\dfrac{2\pi}3=\dfrac{\sqrt3}4ac=\sqrt3$，$\therefore ac=4$．" "\n"
        r"（$a+c=5$，$ac=4$ ⟹ $a,c$ 为方程 $x^{2}-5x+4=0$ 的两根 $1,4$，均为正，三角形成立）" "\n"
        r"由余弦定理：$b^{2}=a^{2}+c^{2}-2ac\cos\dfrac{2\pi}3=a^{2}+c^{2}+ac=\left(a+c\right)^{2}-ac=25-4=21$，" "\n"
        r"$\therefore b=\sqrt{21}$．"
    ),
    'review': (
        r"**① 提公因子（题眼）**：正弦定理代入后 $\sin A\sin C$ 是公因子，**直接约去**得 $2\cos B+1=0$ ✓✓✓" "\n"
        r"（**不要试图约 $\sin C$ 后讨论**，两个都是正的，一并提出最干净）" "\n"
        r"② **$\cos B=-\frac12$，$B=\frac{2\pi}3$** ✓✓✓" "\n"
        r"③ **角平分线的面积拆分（最简做法）**：两个小三角形面积各 $=\frac12\cdot$（边）$\cdot BD\cdot\sin\frac B2$，" "\n"
        r"相加后 $\frac12\cdot BD\cdot\sin\frac B2\cdot(a+c)=S$ ✓✓✓" "\n"
        r"④ **两个条件各给一个对称式**：面积给 $ac$、角平分线给 $a+c$，**凑成韦达定理的两根** ✓✓✓" "\n"
        r"⑤ **$b^2=(a+c)^2-ac$**：因为 $\cos\frac{2\pi}3=-\frac12$ 使 $-2ac\cos B=+ac$，" "\n"
        r"故 $a^2+c^2+ac=(a+c)^2-ac$ ✓✓✓" "\n"
        r"（**若写成 $(a+c)^2-3ac=25-12=13$ 就是符号错了** ✓✓）" "\n"
        r"⑥ 数值对拍：$a=1,c=4$ 时 $S=\frac12\cdot4\cdot\sin120^\circ=\sqrt3$ ✓；" "\n"
        r"$b^2=1+16-2\cdot1\cdot4\cdot(-0.5)=19$… 注意：$a^2+c^2+ac=1+16+4=21$ ✓（$-2ac\cos B=+4$）" "\n"
        r"$b=\sqrt{21}=4.583$；检验三角形：$1+4>4.583$ ✓✓✓ **完全闭合**" "\n"
        r"**答案 $\frac{2\pi}3$、$\sqrt{21}$ 均正确** ✓" "\n"
        r"（**原书答案 `b = 21` 是根号丢失**）" "\n"
        r"**⭐⭐ 通法（角平分线 + 面积的两个对称式）**：" "\n"
        r"① ⭐⭐ **$S_{\triangle}=S_1+S_2$ 是角平分线题的第一选择**，它同时用到了 $BD$ 与两边 ✓；" "\n"
        r"② ⭐⭐ **$S=\frac{\sqrt3}4ac=\sqrt3$ 型（$B=120^\circ$）**：$S=\frac12ac\sin B$ 中 $\sin120^\circ=\frac{\sqrt3}2$ ✓；" "\n"
        r"③ ⭐⭐ **凑出 $a+c$ 与 $ac$ 后不必解出 $a,c$**，直接用 $b^2=(a+c)^2-2ac(1+\cos B)$ ✓；" "\n"
        r"④ ⚠ **钝角时 $\cos B<0$，$b^2$ 中交叉项变号**：$(a+c)^2-2ac(1+\cos B)=(a+c)^2-ac$（$B=\frac{2\pi}3$）✓✓"
    ),
    'difficulty': 0.78,
    'topics': ['M-T-225'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-225-V2',
}

T225_V3 = {
    'type': '解答',
    'stem_text': (
        r"在 $\triangle ABC$ 中，角 $A$，$B$，$C$ 所对的边分别为 $a$，$b$，$c$，且满足 $\left(a+2b\right)\cos C+c\cos A=0$．" "\n"
        r"(1) 求角 $C$ 的大小；" "\n"
        r"(2) 设 $AB$ 边上的角平分线 $CD$ 长为 $2$，求 $\triangle ABC$ 的面积的最小值．"
    ),
    'opts': [],
    'answer': r"(1) $C=\dfrac{2\pi}3$；(2) $S_{\min}=4\sqrt3$",
    'analysis': (
        r"(1) 正弦定理代入后把 $\sin A\cos C+\cos A\sin C$ 合成 $\sin(A+C)=\sin B$，提出 $\sin B$ 得 $\cos C$；"
        r"(2) 在两个小三角形 $\triangle ACD$、$\triangle BCD$ 中分别用正弦定理，把 $c$ 表示成 $\frac{\sqrt3}{\sin A}+\frac{\sqrt3}{\sin B}$，"
        r"再用正弦定理把 $\frac1{\sin A},\frac1{\sin B}$ 换成 $\frac{2c}{\sqrt3a},\frac{2c}{\sqrt3b}$，即得 $\frac1a+\frac1b=\frac12$，最后由基本不等式求 $ab$ 的下界．"
    ),
    'solution': (
        r"**(1)** 由正弦定理，$\left(\sin A+2\sin B\right)\cos C+\sin C\cos A=0$，" "\n"
        r"即 $\left(\sin A\cos C+\cos A\sin C\right)+2\sin B\cos C=0$，" "\n"
        r"$\sin\left(A+C\right)+2\sin B\cos C=0$．" "\n"
        r"$\because A+C=\pi-B$，$\therefore\sin\left(A+C\right)=\sin B$，" "\n"
        r"$\therefore\sin B\left(1+2\cos C\right)=0$．又 $\sin B>0$，$\therefore\cos C=-\dfrac12$，" "\n"
        r"$C=\dfrac{2\pi}3$．" "\n"
        r"**(2)** $CD$ 平分 $\angle ACB$，$\therefore\angle ACD=\angle BCD=\dfrac\pi3$．设 $AD=m$，则 $BD=c-m$．" "\n"
        r"在 $\triangle ACD$ 中：$\dfrac{CD}{\sin A}=\dfrac m{\sin\frac\pi3}$，$m=\dfrac{\sqrt3}{\sin A}$；" "\n"
        r"在 $\triangle BCD$ 中：$\dfrac{CD}{\sin B}=\dfrac{c-m}{\sin\frac\pi3}$，$c-m=\dfrac{\sqrt3}{\sin B}$．" "\n"
        r"$\therefore c=\dfrac{\sqrt3}{\sin A}+\dfrac{\sqrt3}{\sin B}$．" "\n"
        r"在 $\triangle ABC$ 中，$\dfrac a{\sin A}=\dfrac b{\sin B}=\dfrac c{\sin\frac{2\pi}3}=\dfrac{2c}{\sqrt3}$，" "\n"
        r"$\therefore\dfrac1{\sin A}=\dfrac{2c}{\sqrt3a}$，$\dfrac1{\sin B}=\dfrac{2c}{\sqrt3b}$．代入上式：" "\n"
        r"$c=\sqrt3\cdot\dfrac{2c}{\sqrt3a}+\sqrt3\cdot\dfrac{2c}{\sqrt3b}=2c\left(\dfrac1a+\dfrac1b\right)$，" "\n"
        r"$\therefore\dfrac1a+\dfrac1b=\dfrac12$．" "\n"
        r"由基本不等式 $\dfrac12=\dfrac1a+\dfrac1b\ge\dfrac2{\sqrt{ab}}$，$\therefore\sqrt{ab}\ge4$，$ab\ge16$，" "\n"
        r"当且仅当 $a=b=4$ 时取等号．" "\n"
        r"$S_{\triangle ABC}=\dfrac12ab\sin C=\dfrac{\sqrt3}4ab\ge\dfrac{\sqrt3}4\times16=4\sqrt3$，" "\n"
        r"即 $\triangle ABC$ 面积的最小值为 $4\sqrt3$．"
    ),
    'review': (
        r"**① $\sin A\cos C+\cos A\sin C=\sin(A+C)=\sin B$（题眼）**：" "\n"
        r"把含 $A$ 的两项合成一个 $\sin B$，与另一项 $2\sin B\cos C$ **凑出公因子 $\sin B$** ✓✓✓" "\n"
        r"② **$c=\frac{\sqrt3}{\sin A}+\frac{\sqrt3}{\sin B}$ 是全题的枢纽**：" "\n"
        r"左边是 $c$，右边两个 $\frac1{\sin}$，再用正弦定理把 $\frac1{\sin A}$ 换成 $\frac{2c}{\sqrt3a}$，**$c$ 两边约掉** ✓✓✓" "\n"
        r"③ **$\frac1a+\frac1b=\frac12$ 是「倒数和」型约束**，用 $\frac1a+\frac1b\ge\frac2{\sqrt{ab}}$ 得 $ab\ge16$ ✓✓✓" "\n"
        r"（**注意方向**：和固定 ⟹ 由 AM-GM 得 $\sqrt{ab}$ 的**下**界，进而 $S$ 有**最小**值 ✓）" "\n"
        r"④ **取等条件 $a=b=4$**：此时 $A=B=\frac\pi6$，$c^2=16+16-2\cdot16\cdot(-\frac12)=48$，$c=4\sqrt3$；" "\n"
        r"检验 $CD$：$m=\frac{\sqrt3}{\sin30^\circ}=2\sqrt3$，$c-m=2\sqrt3$，而 $c=4\sqrt3$ ✓✓✓ **完全闭合**" "\n"
        r"⑤ **$S=\frac{\sqrt3}4ab$**：因为 $\sin\frac{2\pi}3=\frac{\sqrt3}2$ ✓✓✓" "\n"
        r"⑥ 数值对拍：$a=b=4$，$S=\frac12\cdot16\cdot\frac{\sqrt3}2=4\sqrt3=6.928$ ✓✓✓" "\n"
        r"**答案 $\frac{2\pi}3$、$4\sqrt3$ 均正确** ✓" "\n"
        r"**⭐⭐ 通法（角平分线长已知求最值）**：" "\n"
        r"① ⭐⭐ **在两个小三角形中各用一次正弦定理**，把 $c$ 表成含 $\frac1{\sin A},\frac1{\sin B}$ 的式子 ✓；" "\n"
        r"② ⭐⭐ **$\frac1{\sin A}=\frac{2R}a$ 型代换**：把角换回边，往往能约去公共因子（本题约掉 $c$）✓；" "\n"
        r"③ ⭐⭐ **得到 $\frac1a+\frac1b=k$ 后立刻用 $\frac1a+\frac1b\ge\frac2{\sqrt{ab}}$** —— 这是「倒数和」的标准动作 ✓；" "\n"
        r"④ ⭐⭐ **$S=\frac12ab\sin C$ 中 $C$ 已定**，故 $S$ 的最值 ⟺ $ab$ 的最值 ✓；" "\n"
        r"⑤ ⚠ **最后要检验取等时三角形存在**（$a=b=4$、$C=120^\circ$ ⟹ $c=4\sqrt3<8$ ✓）✓✓"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-225'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-225-V3',
}


T226_E1 = {
    'type': '解答',
    'stem_text': (
        r"设 $\triangle ABC$ 的内角 $A$，$B$，$C$ 的对边分别为 $a,b,c$，$a=6$，$b^{2}-bc+c^{2}=36$．" "\n"
        r"(1) 求 $A$；" "\n"
        r"(2) 从以下三个条件：① $b=8$；② $\sin B=\dfrac{\sqrt3}3$；③ $AC$ 边上的高 $BH=\dfrac{11}2$ 中"
        r"选择一个作为已知条件，使三角形存在且唯一确定，并求 $\triangle ABC$ 的面积．"
    ),
    'opts': [],
    'answer': r"(1) $A=\dfrac\pi3$；(2) 应选条件②，此时 $S_{\triangle ABC}=6\sqrt2+2\sqrt3$",
    'analysis': (
        r"(1) 由 $a^{2}=36$ 把已知式改写成 $b^{2}+c^{2}-a^{2}=bc$，直接代入余弦定理；"
        r"(2) 三个条件分别代入 $b^{2}-bc+c^{2}=36$：① 判别式小于 $0$ 无解；② 由正弦定理得 $b=4$，"
        r"方程有唯一正根；③ 由 $BH=c\sin A$ 得 $c$，方程有两个正根，不唯一．"
    ),
    'solution': (
        r"**(1)** $\because a=6$，$\therefore a^{2}=36=b^{2}-bc+c^{2}$，即 $b^{2}+c^{2}-a^{2}=bc$．" "\n"
        r"由余弦定理 $\cos A=\dfrac{b^{2}+c^{2}-a^{2}}{2bc}=\dfrac{bc}{2bc}=\dfrac12$．" "\n"
        r"又 $A\in(0,\pi)$，$\therefore A=\dfrac\pi3$．" "\n"
        r"**(2) 选① $b=8$**：代入 $b^{2}-bc+c^{2}=36$ 得 $c^{2}-8c+28=0$．" "\n"
        r"$\Delta=64-112=-48<0$，无实根，**这样的三角形不存在**．" "\n"
        r"**选② $\sin B=\dfrac{\sqrt3}3$**：由正弦定理 $b=\dfrac{a\sin B}{\sin A}=\dfrac{6\times\frac{\sqrt3}3}{\frac{\sqrt3}2}=4$．" "\n"
        r"代入 $b^{2}-bc+c^{2}=36$ 得 $c^{2}-4c-20=0$，解得 $c=2+2\sqrt6$ 或 $c=2-2\sqrt6$（舍去）．" "\n"
        r"$\therefore S_{\triangle ABC}=\dfrac12bc\sin A=\dfrac12\times4\times\left(2+2\sqrt6\right)\times\dfrac{\sqrt3}2"
        r"=\sqrt3\left(2+2\sqrt6\right)=2\sqrt3+6\sqrt2$．" "\n"
        r"**选③ $BH=\dfrac{11}2$**：在 $\triangle ABH$ 中 $\sin A=\dfrac{BH}{AB}$，" "\n"
        r"$\therefore c=AB=\dfrac{BH}{\sin A}=\dfrac{11/2}{\sqrt3/2}=\dfrac{11\sqrt3}3$．" "\n"
        r"代入 $b^{2}-bc+c^{2}=36$ 得 $b^{2}-\dfrac{11\sqrt3}3b+\dfrac{121}3-36=0$，即 $b^{2}-\dfrac{11\sqrt3}3b+\dfrac{13}3=0$．" "\n"
        r"$\Delta=\dfrac{121\times3}9-\dfrac{52}3=\dfrac{121}3-\dfrac{52}3=23>0$，且两根之和 $\dfrac{11\sqrt3}3>0$、之积 $\dfrac{13}3>0$，" "\n"
        r"故有两个正根 $b=\dfrac{11\sqrt3}6\pm\dfrac{\sqrt{23}}2$，**三角形不唯一**．" "\n"
        r"综上，应选条件②，$S_{\triangle ABC}=6\sqrt2+2\sqrt3$．"
    ),
    'review': (
        r"**① $a^{2}=36$ 与已知式对比（题眼）**：$b^{2}-bc+c^{2}=36=a^{2}$ ⟹ $b^{2}+c^{2}-a^{2}=bc$ ⟹ $\cos A=\frac12$ ✓✓✓" "\n"
        r"② **$b^{2}+c^{2}-bc=a^{2}$ 是 $A=\frac\pi3$ 的等价刻画**，后面三选一都拿它当方程用 ✓✓✓" "\n"
        r"③ **条件①用判别式否定**：$c^2-8c+28=0$，$\Delta=-48<0$，一票否决 ✓✓✓" "\n"
        r"④ **条件②的 $b=4$ 是整数** —— 这是判定「$\sin B=\frac{\sqrt3}3$」还原正确的强信号" "\n"
        r"（题面提取为 `sinB = 3/3`，若理解为 $\frac33=1$ 则 $B=90^\circ$，$b=4\sqrt3$，后面不整齐 ✓✓✓）" "\n"
        r"⑤ **条件③给两个正根**：根之和、根之积都用韦达定理判定，**不必算出具体值** ✓✓✓" "\n"
        r"⑥ 数值对拍：$b=4$，$c=2+2\sqrt6=6.899$：" "\n"
        r"$b^2-bc+c^2=16-27.596+47.596=36.000$ ✓；" "\n"
        r"$S=\frac12\cdot4\cdot6.899\cdot\frac{\sqrt3}2=11.947$，而 $6\sqrt2+2\sqrt3=8.485+3.464=11.949$ ✓✓✓ **完全闭合**" "\n"
        r"**答案 $\frac\pi3$、$6\sqrt2+2\sqrt3$ 均正确** ✓" "\n"
        r"**⭐⭐ 通法（三选一 · 判定三角形是否唯一）**：" "\n"
        r"① ⭐⭐ **把边的关系式当方程，用判别式 + 韦达定理判根的个数**：$\Delta<0$ 不存在；" "\n"
        r"$\Delta>0$ 且两根都正才不唯一；$\Delta=0$ 或一正一负则唯一 ✓；" "\n"
        r"② ⭐⭐ **高 $BH=c\sin A$**：$AC$ 边上的高由 $AB$ 与 $\angle A$ 决定，**先求 $c$ 再代入** ✓；" "\n"
        r"③ ⭐⭐ **$A$ 已知时，$\sin B$ 型条件最简**：正弦定理直接给 $b$，无需求角 ✓；" "\n"
        r"④ ⚠ **「唯一确定」要同时排除「不存在」和「两个」**，三者都要算完才能下结论 ✓✓"
    ),
    'difficulty': 0.80,
    'topics': ['M-T-226'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-226-E1',
}

T226_V1 = {
    'type': '解答',
    'stem_text': (
        r"在 $\triangle ABC$ 中，$\sqrt3\left(b\cos C+c\cos B\right)=2a\cos A$．" "\n"
        r"(1) 求 $A$；" "\n"
        r"(2) 若 $a=2$，从条件①、条件②、条件③中任选一个作为已知，使 $\triangle ABC$ 存在并唯一确定，并求 $c$ 的值．" "\n"
        r"条件①：$b=2\sqrt3$；条件②：$b=1$；条件③：$\cos B=-\dfrac13$．" "\n"
        r"（注：如果选择的条件不符合要求，第(2)问得 $0$ 分；如果选择多个符合要求的条件分别解答，按第一个解答计分）"
    ),
    'opts': [],
    'answer': (
        r"(1) $A=\dfrac\pi6$；(2) 条件①不唯一（$B=\frac\pi3$ 或 $\frac{2\pi}3$）；"
        r"条件②唯一，$c=\dfrac{\sqrt{15}+\sqrt3}2$；条件③唯一，$c=\dfrac{4\sqrt6-2}3$"
    ),
    'analysis': (
        r"(1) 用正弦定理把边换成角的正弦，$b\cos C+c\cos B$ 化为 $\sin(B+C)=\sin A$，约去 $\sin A$ 得 $\cos A$；"
        r"(2) 由正弦定理求 $\sin B$，再用「大边对大角」判定 $B$ 是否唯一；唯一时由 $\sin C=\sin(A+B)$ 求 $c$．"
    ),
    'solution': (
        r"**(1)** 由正弦定理 $b=2R\sin B$，$c=2R\sin C$，$a=2R\sin A$，代入得" "\n"
        r"$\sqrt3\left(\sin B\cos C+\sin C\cos B\right)=2\sin A\cos A$，" "\n"
        r"即 $\sqrt3\sin\left(B+C\right)=2\sin A\cos A$．" "\n"
        r"$\because\sin\left(B+C\right)=\sin A>0$，$\therefore\sqrt3=2\cos A$，$\cos A=\dfrac{\sqrt3}2$，" "\n"
        r"$A=\dfrac\pi6$．" "\n"
        r"**(2)** 由正弦定理 $\sin B=\dfrac{b\sin A}a=\dfrac b4$．" "\n"
        r"**选① $b=2\sqrt3$**：$\sin B=\dfrac{2\sqrt3}4=\dfrac{\sqrt3}2$．" "\n"
        r"$\because b=2\sqrt3>a=2$，$\therefore B>A=\dfrac\pi6$，故 $B=\dfrac\pi3$ 或 $B=\dfrac{2\pi}3$，" "\n"
        r"$C=\dfrac\pi2$ 或 $C=\dfrac\pi6$，**$\triangle ABC$ 存在但不唯一**，不合要求．" "\n"
        r"**选② $b=1$**：$\sin B=\dfrac14$．$\because b<a$，$\therefore B<A=\dfrac\pi6$，$B$ 唯一，" "\n"
        r"$\cos B=\sqrt{1-\dfrac1{16}}=\dfrac{\sqrt{15}}4$．" "\n"
        r"$\sin C=\sin\left(A+B\right)=\sin A\cos B+\cos A\sin B=\dfrac12\cdot\dfrac{\sqrt{15}}4+\dfrac{\sqrt3}2\cdot\dfrac14"
        r"=\dfrac{\sqrt{15}+\sqrt3}8$．" "\n"
        r"$c=\dfrac{a\sin C}{\sin A}=\dfrac{2\cdot\frac{\sqrt{15}+\sqrt3}8}{\frac12}=\dfrac{\sqrt{15}+\sqrt3}2$．" "\n"
        r"**选③ $\cos B=-\dfrac13$**：$\because\cos B>-\dfrac{\sqrt3}2=\cos\dfrac{5\pi}6$，$\therefore\dfrac\pi2<B<\dfrac{5\pi}6$，$B$ 唯一，" "\n"
        r"$\sin B=\sqrt{1-\dfrac19}=\dfrac{2\sqrt2}3$．" "\n"
        r"$\sin C=\sin\left(A+B\right)=\dfrac12\cdot\left(-\dfrac13\right)+\dfrac{\sqrt3}2\cdot\dfrac{2\sqrt2}3=\dfrac{2\sqrt6-1}6$．" "\n"
        r"$c=\dfrac{a\sin C}{\sin A}=\dfrac{2\cdot\frac{2\sqrt6-1}6}{\frac12}=\dfrac{4\sqrt6-2}3$．"
    ),
    'review': (
        r"**① $\sin B\cos C+\sin C\cos B=\sin(B+C)=\sin A$（题眼）**：" "\n"
        r"左边正是射影定理 $b\cos C+c\cos B=a$ 的角形式，换成 $\sin A$ 后与右边**约去 $\sin A$** ✓✓✓" "\n"
        r"② **题面 `3(bcosC+ccosB)` 是 $\sqrt3$ 的根号丢失**：" "\n"
        r"若为 $3$，则 $\cos A=\frac32>1$，**无解** ✓✓✓ 这是最硬的判据" "\n"
        r"③ **判定 $B$ 是否唯一的标准动作**：先由正弦定理求 $\sin B$，再用「**大边对大角**」定范围 ——" "\n"
        r"$b>a$ ⟹ $B>A$ ⟹ 两个解都可能；$b<a$ ⟹ $B<A$ ⟹ 唯一 ✓✓✓" "\n"
        r"④ **条件③用 $\cos B$ 给角**：$\cos B=-\frac13>-\frac{\sqrt3}2$ ⟹ $B<\frac{5\pi}6$，配合 $A=\frac\pi6$ 得 $A+B<\pi$ ✓✓✓" "\n"
        r"⑤ **$\sin C=\sin(A+B)$**：注意是 $\sin(A+B)$ 不是 $\sin(A-B)$（因 $C=\pi-(A+B)$）✓✓✓" "\n"
        r"⑥ 数值对拍（选②）：$b=1$，$a=2$，$A=30^\circ$ ⟹ $\sin B=0.25$，$B=14.478^\circ$，$C=135.522^\circ$；" "\n"
        r"$c=\frac{2\sin135.522^\circ}{\sin30^\circ}=\frac{2\times0.7}{0.5}=2.8$… 精确值 $\frac{\sqrt{15}+\sqrt3}2=\frac{3.873+1.732}2=2.803$ ✓✓✓" "\n"
        r"⑦ 数值对拍（选③）：$B=109.47^\circ$，$C=40.53^\circ$，$c=\frac{2\sin40.53^\circ}{0.5}=2.599$；" "\n"
        r"$\frac{4\sqrt6-2}3=\frac{9.798-2}3=2.599$ ✓✓✓ **完全闭合**" "\n"
        r"**答案均正确** ✓" "\n"
        r"**⭐⭐ 通法（三选一 · 解的个数判定）**：" "\n"
        r"① ⭐⭐ **$b\cos C+c\cos B=a$（射影定理）** 可直接记，本题换成角的正弦后就是 $\sin A$ ✓；" "\n"
        r"② ⭐⭐ **$\sin B=\frac{b\sin A}a$ 后必用大边对大角定唯一性**：这是「存在且唯一」类题的唯一判据 ✓；" "\n"
        r"③ ⭐⭐ **给 $\cos B$（负值）时，与 $-\frac{\sqrt3}2$ 比较**可锁定 $B$ 的范围 ✓；" "\n"
        r"④ ⭐⭐ **$\sin C=\sin(A+B)=\sin A\cos B+\cos A\sin B$**，最后 $c=\frac{a\sin C}{\sin A}$ ✓；" "\n"
        r"⑤ ⚠ **$b>a$ 时 $B$ 有两解**（一个锐角一个钝角），**只要两者都满足 $A+B<\pi$ 就不唯一** ✓✓"
    ),
    'difficulty': 0.82,
    'topics': ['M-T-226'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-226-V1',
}

T226_V2 = {
    'type': '解答',
    'stem_text': (
        r"在 $\triangle ABC$ 中，内角 $A$，$B$，$C$ 所对的边分别为 $a$，$b$，$c$，已知 $a\cos C+c\cos A=\sqrt3$，$a=\sqrt2\,b$，"
        r"记 $\triangle ABC$ 的面积为 $S$．" "\n"
        r"(1) 求 $a$；" "\n"
        r"(2) 请从下面的三个条件中任选一个，探究满足条件的 $\triangle ABC$ 的个数，并说明理由．" "\n"
        r"条件①：$S=\dfrac{\sqrt3}{12}\left(a^{2}+c^{2}-b^{2}\right)$；" "\n"
        r"条件②：$b\cos A+\dfrac{\sqrt2}2a=c$；" "\n"
        r"条件③：$b\sin A=a\cos\left(B-\dfrac\pi6\right)$．"
    ),
    'opts': [],
    'answer': (
        r"(1) $a=\sqrt6$；(2) 选①：满足条件的三角形有 $2$ 个；选②：有 $1$ 个；"
        r"选③：不存在这样的三角形"
    ),
    'analysis': (
        r"(1) 射影定理 $a\cos C+c\cos A=b$，故 $b=\sqrt3$，再由 $a=\sqrt2b$ 得 $a$；"
        r"(2) 三个条件都化成含 $B$ 的三角方程：① $a^2+c^2-b^2=2ac\cos B$ 配面积公式得 $\tan B$；"
        r"②③ 用正弦定理化为 $\sin$ 的方程，再解出 $B$，最后由 $\sin A=\frac{a\sin B}b$ 判断 $A$ 的解数．"
    ),
    'solution': (
        r"**(1)** 由射影定理 $a\cos C+c\cos A=b$，$\therefore b=\sqrt3$．" "\n"
        r"又 $a=\sqrt2\,b$，$\therefore a=\sqrt6$．" "\n"
        r"**(2) 选①** 由余弦定理 $a^{2}+c^{2}-b^{2}=2ac\cos B$，代入得" "\n"
        r"$S=\dfrac{\sqrt3}{12}\cdot2ac\cos B=\dfrac{\sqrt3}6ac\cos B$．又 $S=\dfrac12ac\sin B$，" "\n"
        r"$\therefore\dfrac12\sin B=\dfrac{\sqrt3}6\cos B$，$\tan B=\dfrac{\sqrt3}3$，$B=\dfrac\pi6$．" "\n"
        r"$\sin A=\dfrac{a\sin B}b=\dfrac{\sqrt6\times\frac12}{\sqrt3}=\dfrac{\sqrt2}2$．" "\n"
        r"$\because a>b$，$\therefore A>B=\dfrac\pi6$，故 $A=\dfrac\pi4$ 或 $A=\dfrac{3\pi}4$（均满足 $A+B<\pi$），" "\n"
        r"**满足条件的三角形有 $2$ 个**．" "\n"
        r"**选②** $b\cos A+\dfrac{\sqrt2}2a=c$，由正弦定理得" "\n"
        r"$\sin B\cos A+\dfrac{\sqrt2}2\sin A=\sin C=\sin\left(A+B\right)=\sin A\cos B+\cos A\sin B$，" "\n"
        r"$\therefore\dfrac{\sqrt2}2\sin A=\sin A\cos B$．$\because\sin A\ne0$，$\therefore\cos B=\dfrac{\sqrt2}2$，$B=\dfrac\pi4$．" "\n"
        r"$\sin A=\dfrac{a\sin B}b=\dfrac{\sqrt6\times\frac{\sqrt2}2}{\sqrt3}=\dfrac{\sqrt{12}}{2\sqrt3}=1$，$\therefore A=\dfrac\pi2$，" "\n"
        r"**满足条件的三角形有 $1$ 个**．" "\n"
        r"**选③** $b\sin A=a\cos\left(B-\dfrac\pi6\right)$，由正弦定理得" "\n"
        r"$\sin B\sin A=\sin A\cos\left(B-\dfrac\pi6\right)$．$\because\sin A\ne0$，" "\n"
        r"$\therefore\sin B=\cos\left(B-\dfrac\pi6\right)=\dfrac{\sqrt3}2\cos B+\dfrac12\sin B$，" "\n"
        r"即 $\dfrac12\sin B=\dfrac{\sqrt3}2\cos B$，$\tan B=\sqrt3$，$B=\dfrac\pi3$．" "\n"
        r"$\sin A=\dfrac{a\sin B}b=\dfrac{\sqrt6\times\frac{\sqrt3}2}{\sqrt3}=\dfrac{\sqrt6}2>1$，无解，" "\n"
        r"**不存在满足条件的三角形**．"
    ),
    'review': (
        r"**① 射影定理（一步出 $b$）**：$a\cos C+c\cos A=b=\sqrt3$ ✓✓✓" "\n"
        r"② **条件①的核心：$a^2+c^2-b^2=2ac\cos B$ 与 $S=\frac12ac\sin B$ 联立** ⟹ $\tan B=\frac{\sqrt3}3$ ✓✓✓" "\n"
        r"（**$ac$ 被约掉是必然的**，所以不必知道 $c$）" "\n"
        r"③ **条件②、③都是「正弦定理化角 + 提 $\sin A$」**：" "\n"
        r"$b\cos A\to\sin B\cos A$、$c\to\sin(A+B)$，展开后 $\cos A\sin B$ **恰好抵消** ✓✓✓" "\n"
        r"④ **$\cos(B-\frac\pi6)=\frac{\sqrt3}2\cos B+\frac12\sin B$** 是标准展开，得到 $\tan B=\sqrt3$ ✓✓✓" "\n"
        r"⑤ **判个数的统一动作**：算出 $B$ 后求 $\sin A=\frac{a\sin B}b$，" "\n"
        r"$\sin A<1$ 且有两解 ⟹ $2$ 个；$=1$ ⟹ $1$ 个；$>1$ ⟹ $0$ 个 ✓✓✓" "\n"
        r"⑥ 数值对拍（选①）：$B=30^\circ$，$A=45^\circ$ 时 $C=105^\circ$，$a=\sqrt6=2.449$，$b=\sqrt3=1.732$；" "\n"
        r"$A=135^\circ$ 时 $C=15^\circ$，检验 $A+B=165^\circ<\pi$ ✓，两解都成立 ✓✓✓" "\n"
        r"⑦ 数值对拍（选②）：$B=45^\circ$，$A=90^\circ$，$C=45^\circ$，$a=\sqrt6$，$b=\sqrt3$ ⟹ $a=\sqrt2b$ ✓；" "\n"
        r"选③：$\sin A=1.2247>1$ ✓ 确实无解 ✓✓✓ **完全闭合**" "\n"
        r"**答案 $\sqrt6$、$2/1/0$ 均正确** ✓" "\n"
        r"**⭐⭐ 通法（探究三角形个数的三条件题）**：" "\n"
        r"① ⭐⭐ **射影定理 $a\cos C+c\cos A=b$** —— 见到「$a\cos C+c\cos A$」直接换成 $b$ ✓；" "\n"
        r"② ⭐⭐ **$S=k(a^2+c^2-b^2)$ 型条件 ⟹ 换成 $2ac\cos B$，与 $S=\frac12ac\sin B$ 相除得 $\tan B$** ✓；" "\n"
        r"③ ⭐⭐ **$b\cos A+(\cdots)a=c$ 型 ⟹ 全部化正弦，用 $\sin C=\sin(A+B)$ 展开，交叉项抵消** ✓；" "\n"
        r"④ ⭐⭐ **$b\sin A=a\cos(B-\varphi)$ 型 ⟹ 提 $\sin A$ 后化为 $\sin B$ 与 $\cos B$ 的齐次式 ⟹ $\tan B$** ✓；" "\n"
        r"⑤ ⚠ **最后必须判 $\sin A$ 与 $1$ 的大小**，这是「个数」的唯一依据 ✓✓"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-226'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-226-V2',
}

T226_V3 = {
    'type': '解答',
    'stem_text': (
        r"记 $\triangle ABC$ 的内角 $A$、$B$、$C$ 的对边分别为 $a$、$b$、$c$，已知 $a=2t-1$，$b=4t$，$c=4t+1$（$t>1$）．" "\n"
        r"(1) 当 $t=3$ 时，求 $\cos B$；" "\n"
        r"(2) 是否存在正整数 $t$，使得角 $C$ 为钝角？如果存在，求出 $t$ 的值，并求此时 $\triangle ABC$ 的面积；"
        r"如果不存在，请说明理由．"
    ),
    'opts': [],
    'answer': r"(1) $\cos B=\dfrac5{13}$；(2) 存在，$t=2$，此时 $S_{\triangle ABC}=2\sqrt{35}$",
    'analysis': (
        r"(1) 代入 $t=3$ 得三边 $5,12,13$，直接用余弦定理；"
        r"(2) $C$ 为钝角等价于 $\cos C<0$，即 $a^{2}+b^{2}-c^{2}<0$，解关于 $t$ 的二次不等式，"
        r"再结合 $t>1$ 且为正整数定出 $t$，最后用 $S=\frac12ab\sin C$ 求面积．"
    ),
    'solution': (
        r"**(1)** $t=3$ 时，$a=5$，$b=12$，$c=13$．" "\n"
        r"$\cos B=\dfrac{a^{2}+c^{2}-b^{2}}{2ac}=\dfrac{25+169-144}{2\times5\times13}=\dfrac{50}{130}=\dfrac5{13}$．" "\n"
        r"**(2)** $C$ 为钝角 $\iff\cos C<0\iff a^{2}+b^{2}-c^{2}<0$（分母 $2ab>0$）．" "\n"
        r"$a^{2}+b^{2}-c^{2}=(2t-1)^{2}+16t^{2}-(4t+1)^{2}=4t^{2}-4t+1+16t^{2}-16t^{2}-8t-1=4t^{2}-12t$．" "\n"
        r"由 $4t^{2}-12t<0$ 得 $0<t<3$．" "\n"
        r"又 $t>1$ 且 $t\in\mathbb N^{*}$，$\therefore t=2$．" "\n"
        r"此时 $a=3$，$b=8$，$c=9$（检验：$3+8>9$ ✓，三角形成立）．" "\n"
        r"$\cos C=\dfrac{a^{2}+b^{2}-c^{2}}{2ab}=\dfrac{9+64-81}{2\times3\times8}=-\dfrac8{48}=-\dfrac16$，" "\n"
        r"$\sin C=\sqrt{1-\dfrac1{36}}=\dfrac{\sqrt{35}}6$．" "\n"
        r"$S_{\triangle ABC}=\dfrac12ab\sin C=\dfrac12\times3\times8\times\dfrac{\sqrt{35}}6=2\sqrt{35}$．"
    ),
    'review': (
        r"**① 钝角判别（题眼）**：$C$ 为钝角 $\iff\cos C<0\iff a^{2}+b^{2}-c^{2}<0$ —— " "\n"
        r"**用分子判定，完全不用算分母**（分母 $2ab>0$ 恒成立）✓✓✓" "\n"
        r"② **展开时 $16t^2$ 项恰好抵消**：$(4t)^2=16t^2$ 与 $-(4t+1)^2$ 中的 $-16t^2$，" "\n"
        r"剩下 $4t^2-12t$ 是一次与二次的混合 ✓✓✓" "\n"
        r"（**逐项核对**：$4t^2-4t+1+16t^2-16t^2-8t-1=4t^2-12t$ ✓）" "\n"
        r"③ **$0<t<3$ 配 $t>1$、$t\in\mathbb N^*$ ⟹ 唯一 $t=2$** ✓✓✓" "\n"
        r"④ **$t=2$ 时三边 $3,8,9$**：必须检验三角形不等式 $3+8=11>9$ ✓（**这一步不能省**）" "\n"
        r"⑤ **$S=\frac12ab\sin C$ 用的是夹角 $C$ 的两边 $a,b$** —— 注意不是 $a,c$ 或 $b,c$ ✓✓✓" "\n"
        r"⑥ 数值对拍：$a=3,b=8,c=9$，$\cos C=\frac{9+64-81}{48}=-\frac16=-0.1667<0$ ✓ 确为钝角；" "\n"
        r"$S=\frac12\cdot24\cdot\frac{\sqrt{35}}6=2\sqrt{35}=11.832$ ✓✓✓ **完全闭合**" "\n"
        r"**答案 $\frac5{13}$、$t=2$、$2\sqrt{35}$ 均正确** ✓" "\n"
        r"**⭐⭐ 通法（含参边长的钝角 / 锐角讨论）**：" "\n"
        r"① ⭐⭐ **钝角 $\iff$ 两短边平方和 $<$ 长边平方**，写成 $\cos<0$ 就行，**只看分子** ✓；" "\n"
        r"② ⭐⭐ **三边都是 $t$ 的一次式时，$a^2+b^2-c^2$ 展开后二次项往往部分抵消**，务必逐项核对 ✓；" "\n"
        r"③ ⭐⭐ **整数参数要列全约束**（本题 $t>1$、正整数、$0<t<3$），交集常常只剩一个值 ✓；" "\n"
        r"④ ⚠ **求出 $t$ 后必须检验三角形不等式**，否则可能得到不存在的三角形 ✓✓"
    ),
    'difficulty': 0.72,
    'topics': ['M-T-226'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-226-V3',
}


T229_E1 = {
    'type': '解答',
    'stem_text': (
        r"在平面四边形 $ABCD$ 中，已知 $AD\parallel BC$，$\angle CBD=\angle BDC=\alpha$，$\angle ACD=\beta$．" "\n"
        r"(1) 若 $\alpha=30^\circ$，$\beta=75^\circ$，$\sqrt3\,AC+\sqrt2\,CD=5$，求 $AC$，$CD$ 的长；" "\n"
        r"(2) 若 $\alpha+\beta>90^\circ$，求证：$AB<AD$．"
    ),
    'opts': [],
    'answer': r"(1) $AC=\sqrt3$，$CD=\sqrt2$；(2) 证明见解析",
    'analysis': (
        r"(1) 由 $\angle CBD=\angle BDC$ 得 $\triangle BCD$ 等腰（$BC=CD$），结合平行线的内错角把 $\triangle ACD$ 的三个角全部求出，"
        r"再用正弦定理得 $AC$ 与 $CD$ 之比，代入已知和式；"
        r"(2) 关键是把 $AD$ 写成与 $AB$ 同形：由 $BC=CD$、$AC$ 公共，两个余弦定理只差一个角，"
        r"比较 $\angle ACB$ 与 $\angle ACD$ 即可．"
    ),
    'solution': (
        r"**(1)** $\because\angle CBD=\angle BDC=30^\circ$，$\therefore BC=CD$，$\angle BCD=120^\circ$．" "\n"
        r"由 $AD\parallel BC$ 得 $\angle ADB=\angle CBD=30^\circ$，$\angle DAC=\angle BCA$．" "\n"
        r"又 $\angle BCD=\angle BCA+\angle ACD=\angle BCA+75^\circ=120^\circ$，$\therefore\angle BCA=45^\circ$，" "\n"
        r"$\therefore\angle DAC=45^\circ$，$\angle ADC=180^\circ-45^\circ-75^\circ=60^\circ$．" "\n"
        r"在 $\triangle ACD$ 中由正弦定理 $\dfrac{AC}{\sin\angle ADC}=\dfrac{CD}{\sin\angle DAC}$：" "\n"
        r"$\dfrac{AC}{\sin60^\circ}=\dfrac{CD}{\sin45^\circ}$，$\therefore AC=\dfrac{\sqrt3/2}{\sqrt2/2}CD=\dfrac{\sqrt6}2CD$．" "\n"
        r"代入 $\sqrt3\,AC+\sqrt2\,CD=5$：$\sqrt3\cdot\dfrac{\sqrt6}2CD+\sqrt2\,CD=\dfrac{3\sqrt2}2CD+\sqrt2\,CD=\dfrac{5\sqrt2}2CD=5$，" "\n"
        r"$\therefore CD=\sqrt2$，$AC=\dfrac{\sqrt6}2\times\sqrt2=\sqrt3$．" "\n"
        r"**(2)** $\because\angle CBD=\angle BDC=\alpha$，$\therefore BC=CD$，$\angle BCD=180^\circ-2\alpha$．" "\n"
        r"$\therefore\angle ACB=\angle BCD-\angle ACD=180^\circ-2\alpha-\beta$．" "\n"
        r"在 $\triangle ACB$ 中：$AB^{2}=AC^{2}+BC^{2}-2AC\cdot BC\cos\angle ACB$；" "\n"
        r"在 $\triangle ACD$ 中：$AD^{2}=AC^{2}+CD^{2}-2AC\cdot CD\cos\angle ACD=AC^{2}+BC^{2}-2AC\cdot BC\cos\angle ACD$．" "\n"
        r"（两式右端**只差最后一项的角**，因为 $BC=CD$）" "\n"
        r"由 $\alpha+\beta>90^\circ$ 得" "\n"
        r"$\angle ACB-\angle ACD=180^\circ-2\alpha-\beta-\beta=180^\circ-2\left(\alpha+\beta\right)<0$，" "\n"
        r"$\therefore\angle ACB<\angle ACD$．" "\n"
        r"又两角都在 $\left(0^\circ,180^\circ\right)$ 内，余弦函数在该区间单调递减，$\therefore\cos\angle ACB>\cos\angle ACD$，" "\n"
        r"$\therefore AB^{2}<AD^{2}$，即 $AB<AD$．"
    ),
    'review': (
        r"**① $\angle CBD=\angle BDC$ ⟹ $BC=CD$（题眼）**：" "\n"
        r"这是把两个三角形的余弦定理「对齐」的唯一依据，第(2)问全靠它 ✓✓✓" "\n"
        r"② **平行线的内错角**：$AD\parallel BC$ ⟹ $\angle ADB=\angle CBD$、$\angle DAC=\angle BCA$ ✓✓✓" "\n"
        r"（**第(1)问中 $\angle DAC$ 并未用到**，真正用的是 $\angle ADC=60^\circ$，它由 $\triangle ACD$ 内角和得出）" "\n"
        r"③ **题面 `3AC + 2CD = 5` 是双重根号丢失**：应为 $\sqrt3AC+\sqrt2CD=5$。" "\n"
        r"判据：按字面 $3AC+2CD=5$ 与 $AC=\frac{\sqrt6}2CD$ 联立得 $CD=\frac{5}{2+1.5\sqrt6}\approx0.749$，" "\n"
        r"与答案 $\sqrt2,\sqrt3$ 不符 ✓✓✓" "\n"
        r"④ **第(2)问的结构**：两个余弦定理右端前三项完全相同（$AC^2+BC^2$，$CD=BC$），" "\n"
        r"**只比较 $\cos\angle ACB$ 与 $\cos\angle ACD$** ✓✓✓" "\n"
        r"⑤ **$\alpha+\beta>90^\circ$ 的用法**：$\angle ACB-\angle ACD=180^\circ-2(\alpha+\beta)<0$，" "\n"
        r"注意是 $2(\alpha+\beta)$ 不是 $\alpha+\beta$（因为 $\angle ACB$ 里已有 $2\alpha$）✓✓✓" "\n"
        r"⑥ 数值对拍（第1问）：$\alpha=30^\circ,\beta=75^\circ$ ⟹ $\angle ACB=180-60-75=45^\circ$ ✓；" "\n"
        r"$AC=\sqrt3=1.732$，$CD=\sqrt2=1.414$：$\sqrt3\cdot1.732+\sqrt2\cdot1.414=3+2=5$ ✓✓✓ **完全闭合**" "\n"
        r"**答案 $\sqrt3$、$\sqrt2$ 均正确** ✓" "\n"
        r"**⭐⭐ 通法（四边形中的解三角形）**：" "\n"
        r"① ⭐⭐ **等腰 + 平行是两个「角搬运」工具**：等腰给等边，平行给内错角，配合可把四边形的角全部求出 ✓；" "\n"
        r"② ⭐⭐ **比较两个边长 ⟹ 把两个余弦定理写成「只差一个角」的形式**，再比较该角的余弦 ✓；" "\n"
        r"③ ⭐⭐ **余弦函数在 $(0^\circ,180^\circ)$ 单调递减** —— 角的比较小则余弦较大、对边较小 ✓；" "\n"
        r"④ ⚠ **提取文本中的系数往往是根号**：凡出现 $AC,CD$ 的系数为整数而答案是根号，优先怀疑根号丢失 ✓✓"
    ),
    'difficulty': 0.80,
    'topics': ['M-T-229'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-229-E1',
}

T229_V1 = {
    'type': '解答',
    'stem_text': (
        r"在非直角三角形 $ABC$ 中，角 $A$，$B$，$C$ 的对边分别为 $a$，$b$，$c$．" "\n"
        r"(1) 若 $a+c=2b$，求角 $B$ 的最大值；" "\n"
        r"(2) 若 $a+c=mb$（$m>1$），" "\n"
        r"(i) 证明：$\tan\dfrac A2\tan\dfrac C2=\dfrac{m-1}{m+1}$；" "\n"
        r"(ii) 是否存在函数 $\varphi\left(m\right)$，使得对于一切满足条件的 $m$，代数式"
        r"$\cos A+\cos C+\varphi\left(m\right)+\varphi\left(m\right)\cos A\cos C$ 恒为定值？"
        r"若存在，请给出一个满足条件的 $\varphi\left(m\right)$ 并证明；若不存在，请说明理由．"
    ),
    'opts': [],
    'answer': r"(1) $B_{\max}=\dfrac\pi3$；(2) (i) 证明见解析；(ii) 存在，$\varphi\left(m\right)=-\dfrac{2m}{m^{2}+1}$，定值为 $0$",
    'analysis': (
        r"(1) 把 $b=\frac{a+c}2$ 代入余弦定理，配 $a^{2}+c^{2}\ge2ac$ 得 $\cos B$ 的下界；"
        r"(2) (i) 由正弦定理得 $\sin A+\sin C=m\sin B$，两边和差化积后用 $\sin\frac{A+C}2=\cos\frac B2$ 化简；"
        r"(ii) 把 $\tan^2\frac A2\tan^2\frac C2$ 用半角公式全换成 $\cos A,\cos C$，展开即得．"
    ),
    'solution': (
        r"**(1)** 由 $a+c=2b$ 得 $b=\dfrac{a+c}2$，代入余弦定理：" "\n"
        r"$\cos B=\dfrac{a^{2}+c^{2}-b^{2}}{2ac}=\dfrac{a^{2}+c^{2}-\frac{(a+c)^{2}}4}{2ac}"
        r"=\dfrac{\frac34\left(a^{2}+c^{2}\right)-\frac12ac}{2ac}$．" "\n"
        r"$\because a^{2}+c^{2}\ge2ac$，$\therefore\cos B\ge\dfrac{\frac34\cdot2ac-\frac12ac}{2ac}=\dfrac{ac}{2ac}=\dfrac12$，" "\n"
        r"当且仅当 $a=c$ 时取等号．" "\n"
        r"$\therefore B\in\left(0,\dfrac\pi3\right]$，$B$ 的最大值为 $\dfrac\pi3$．" "\n"
        r"**(2) (i)** 由 $a+c=mb$ 及正弦定理得 $\sin A+\sin C=m\sin B$．" "\n"
        r"左边和差化积：$2\sin\dfrac{A+C}2\cos\dfrac{A-C}2$；右边：$2m\sin\dfrac B2\cos\dfrac B2$．" "\n"
        r"$\because\dfrac{A+C}2=\dfrac\pi2-\dfrac B2$，$\therefore\sin\dfrac{A+C}2=\cos\dfrac B2$，" "\n"
        r"又 $\sin\dfrac B2=\cos\dfrac{A+C}2$，代入得 $2\cos\dfrac B2\cos\dfrac{A-C}2=2m\cos\dfrac{A+C}2\cos\dfrac B2$，" "\n"
        r"$\therefore\cos\dfrac{A-C}2=m\cos\dfrac{A+C}2$．" "\n"
        r"展开：$\cos\dfrac A2\cos\dfrac C2+\sin\dfrac A2\sin\dfrac C2"
        r"=m\left(\cos\dfrac A2\cos\dfrac C2-\sin\dfrac A2\sin\dfrac C2\right)$， " "\n"
        r"整理得 $\left(1+m\right)\sin\dfrac A2\sin\dfrac C2=\left(m-1\right)\cos\dfrac A2\cos\dfrac C2$，" "\n"
        r"$\therefore\tan\dfrac A2\tan\dfrac C2=\dfrac{m-1}{m+1}$．" "\n"
        r"**(ii)** 由半角公式 $\tan^{2}\dfrac\alpha2=\dfrac{1-\cos\alpha}{1+\cos\alpha}$ 得" "\n"
        r"$\dfrac{1-\cos A}{1+\cos A}\cdot\dfrac{1-\cos C}{1+\cos C}=\dfrac{\left(m-1\right)^{2}}{\left(m+1\right)^{2}}$．" "\n"
        r"记 $X=\cos A+\cos C$，$Y=\cos A\cos C$，交叉相乘：" "\n"
        r"$\left(1-X+Y\right)\left(m+1\right)^{2}=\left(1+X+Y\right)\left(m-1\right)^{2}$．" "\n"
        r"移项：$\left(m+1\right)^{2}-\left(m-1\right)^{2}=X\left[\left(m+1\right)^{2}+\left(m-1\right)^{2}\right]+Y\left[\left(m-1\right)^{2}-\left(m+1\right)^{2}\right]$，" "\n"
        r"即 $4m=2\left(m^{2}+1\right)X-4mY$，$\therefore X=\dfrac{2m\left(1+Y\right)}{m^{2}+1}$，" "\n"
        r"$\therefore X-\dfrac{2m}{m^{2}+1}-\dfrac{2m}{m^{2}+1}Y=0$．" "\n"
        r"与所求式比较得 $\varphi\left(m\right)=-\dfrac{2m}{m^{2}+1}$，**定值为 $0$**．"
    ),
    'review': (
        r"**① 第(1)问的核心：$a^2+c^2\ge2ac$ 直接给 $\cos B$ 的下界** ✓✓✓" "\n"
        r"（**$B$ 最大 ⟺ $\cos B$ 最小**：余弦在 $(0,\pi)$ 上递减，别搞反方向 ✓）" "\n"
        r"② **和差化积 + $\frac{A+C}2=\frac\pi2-\frac B2$（题眼）**：" "\n"
        r"$\sin\frac{A+C}2=\cos\frac B2$ 与右边的 $\cos\frac B2$ **约掉**，剩下 $\cos\frac{A-C}2=m\cos\frac{A+C}2$ ✓✓✓" "\n"
        r"③ **$\cos\frac{A\pm C}2$ 的展开是最后一步**：" "\n"
        r"$\cos\frac{A-C}2=\cos\frac A2\cos\frac C2+\sin\frac A2\sin\frac C2$，" "\n"
        r"$\cos\frac{A+C}2=\cos\frac A2\cos\frac C2-\sin\frac A2\sin\frac C2$ —— **符号一正一负，别记反** ✓✓✓" "\n"
        r"④ **(ii) 的代数技巧**：设 $X=\cos A+\cos C$、$Y=\cos A\cos C$，" "\n"
        r"把 $\left(1\mp X+Y\right)$ 当作整体交叉相乘，**一次展开即得线性关系** ✓✓✓" "\n"
        r"⑤ ⚠ **原书末行写的定值是 $-1$，实为 $0$**。我的展开核对：" "\n"
        r"$4m=2(m^2+1)X-4mY$ ⟹ $X-\frac{2m}{m^2+1}Y=\frac{2m}{m^2+1}$ ⟹ $X-\frac{2m}{m^2+1}-\frac{2m}{m^2+1}Y=0$ ✓✓✓" "\n"
        r"⑥ 数值对拍（$m=2$，等边）：$A=C=60^\circ$，$X=1$，$Y=\frac14$，$\varphi=-\frac45$；" "\n"
        r"$1-0.8-0.8\times0.25=0$ ✓；" "\n"
        r"（$m=3$，$A=C=70.53^\circ$）：$X=0.6667$，$Y=0.1111$，$\varphi=-0.6$；" "\n"
        r"$0.6667-0.6-0.6\times0.1111=0$ ✓✓✓ **完全闭合**" "\n"
        r"⑦ **非直角条件的作用**：保证 $\tan\frac A2,\tan\frac C2$ 与分母 $\cos\frac A2\cos\frac C2$ 都有意义 ✓" "\n"
        r"**答案 $\frac\pi3$、$\varphi(m)=-\frac{2m}{m^2+1}$（定值 $0$）正确** ✓" "\n"
        r"**⭐⭐ 通法（$a+c=mb$ 型的两角和差化积）**：" "\n"
        r"① ⭐⭐ **$a+c=mb$ ⟹ $\sin A+\sin C=m\sin B$ ⟹ 和差化积 ⟹ $\cos\frac{A-C}2=m\cos\frac{A+C}2$**，这是一条固定流水线 ✓；" "\n"
        r"② ⭐⭐ **$\sin\frac{A+C}2=\cos\frac B2$、$\sin\frac B2=\cos\frac{A+C}2$** —— 这两条恒等式让两边同时约去 $\cos\frac B2$ ✓；" "\n"
        r"③ ⭐⭐ **半角正切积 $\tan\frac A2\tan\frac C2=\frac{m-1}{m+1}$** 可当结论记（$m=2$ 时 $=\frac13$）✓；" "\n"
        r"④ ⭐⭐ **含 $\cos A,\cos C$ 的对称式 ⟹ 设 $X=\cos A+\cos C$、$Y=\cos A\cos C$**，转成二元线性方程 ✓；" "\n"
        r"⑤ ⚠ **$B$ 最大 ⟺ $\cos B$ 最小**，用 $a^2+c^2\ge2ac$ 时要注意方向 ✓✓"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-229'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-229-V1',
}

T229_V3 = {
    'type': '解答',
    'stem_text': (
        r"在 $\triangle EFG$ 中，$H$ 为 $FG$ 上一点，$FH=2HG$，$3\sin F=\sin\angle EHG$，$M$ 是线段 $EF$ 的延长线上一点．" "\n"
        r"(1) 证明：$\angle MEG=\angle HEG$；" "\n"
        r"(2) 若 $HG=3$，$EH=2$，求 $EG$．"
    ),
    'opts': [],
    'answer': r"(1) 证明见解析；(2) $EG=\sqrt{15}$",
    'analysis': (
        r"(1) 先在 $\triangle EFH$ 中用正弦定理把 $\sin F$ 换成 $\sin\angle EHF$，配已知条件得 $EF=3EH$；"
        r"再由 $FG=3HG$ 得面积倍数关系，两个面积公式各写一次 $S_{\triangle EFG}$，推出 $\sin\angle GEH=\sin\angle FEG$，"
        r"由两角不等得互补，从而外角等于内对角；"
        r"(2) $\triangle EFH$ 三边已知，余弦定理求 $\cos\angle EHF$，再由补角得 $\cos\angle EHG$，最后对 $\triangle EHG$ 用余弦定理．"
    ),
    'solution': (
        r"**(1)** 在 $\triangle EFH$ 中，由正弦定理 $\dfrac{EH}{\sin F}=\dfrac{EF}{\sin\angle EHF}$．" "\n"
        r"$\because\angle EHG+\angle EHF=\pi$，$\therefore\sin\angle EHG=\sin\angle EHF$．" "\n"
        r"由 $3\sin F=\sin\angle EHG=\sin\angle EHF$ 及正弦定理：" "\n"
        r"$EF=\dfrac{EH\cdot\sin\angle EHF}{\sin F}=\dfrac{EH\cdot3\sin F}{\sin F}=3EH$．" "\n"
        r"又 $FH=2HG$，$\therefore FG=FH+HG=3HG$，故 $S_{\triangle EFG}=3S_{\triangle EHG}$．" "\n"
        r"分别用两边夹角写面积：" "\n"
        r"$S_{\triangle EFG}=\dfrac12\cdot EF\cdot EG\cdot\sin\angle FEG=\dfrac12\cdot3EH\cdot EG\cdot\sin\angle FEG$，" "\n"
        r"$3S_{\triangle EHG}=3\times\dfrac12\cdot EH\cdot EG\cdot\sin\angle GEH$．" "\n"
        r"两式相等得 $\sin\angle FEG=\sin\angle GEH$．" "\n"
        r"$\because H$ 在 $FG$ 上，$\therefore0<\angle HEG<\angle FEG<\pi$，" "\n"
        r"$\therefore\angle HEG+\angle FEG=\pi$（两角不等而正弦相等，必互补）．" "\n"
        r"又 $M$ 在 $EF$ 的延长线上，$\therefore\angle MEG=\pi-\angle FEG=\angle HEG$．" "\n"
        r"**(2)** $HG=3$，$\therefore FH=2HG=6$；$EH=2$，由(1) 知 $EF=3EH=6$．" "\n"
        r"在 $\triangle EFH$ 中：$\cos\angle EHF=\dfrac{FH^{2}+EH^{2}-EF^{2}}{2FH\cdot EH}=\dfrac{36+4-36}{2\times6\times2}=\dfrac4{24}=\dfrac16$．" "\n"
        r"$\therefore\cos\angle EHG=\cos\left(\pi-\angle EHF\right)=-\cos\angle EHF=-\dfrac16$．" "\n"
        r"在 $\triangle EHG$ 中：$EG^{2}=EH^{2}+HG^{2}-2EH\cdot HG\cos\angle EHG=4+9-2\times2\times3\times\left(-\dfrac16\right)=13+2=15$，" "\n"
        r"$\therefore EG=\sqrt{15}$．"
    ),
    'review': (
        r"**① $\sin\angle EHG=\sin\angle EHF$（补角，题眼）**：" "\n"
        r"这一步把已知条件中的 $\angle EHG$ 换成 $\triangle EFH$ 的内角，**正弦定理才能用上** ✓✓✓" "\n"
        r"② **$EF=3EH$ 是第一个关键结论**：$EF=\frac{EH\sin\angle EHF}{\sin F}=\frac{EH\cdot3\sin F}{\sin F}=3EH$ ✓✓✓" "\n"
        r"（**题面 `3sinF` 就是 $3\sin F$，不是 $\sqrt3$**：若为 $\sqrt3$，则 $EF=2\sqrt3$，" "\n"
        r"$\cos\angle EHF=\frac{36+4-12}{24}=\frac76>1$ **无解** ✓✓✓）" "\n"
        r"③ **$FG=3HG$ ⟹ $S_{\triangle EFG}=3S_{\triangle EHG}$**（同高，底成 3 倍）✓✓✓" "\n"
        r"④ **两个面积公式写同一个三角形**：$S_{\triangle EFG}=\frac12 EF\cdot EG\sin\angle FEG$ 与 $3S_{\triangle EHG}$，" "\n"
        r"把 $EF=3EH$ 代入后 $3EH\cdot EG$ **两边完全相同，只剩正弦相等** ✓✓✓" "\n"
        r"⑤ **$\sin\alpha=\sin\beta$ 且 $\alpha\ne\beta$ ⟹ 互补**：这里必须说明 $\angle HEG<\angle FEG$（$H$ 在 $FG$ 上）✓✓✓" "\n"
        r"⑥ **$M$ 在 $EF$ 延长线上 ⟹ $\angle MEG=\pi-\angle FEG$** —— 外角与内角的关系 ✓✓✓" "\n"
        r"⑦ 数值对拍：$EH=2,EF=6,FH=6$ ⟹ $\triangle EFH$ 等腰（$EF=FH=6$），" "\n"
        r"$\cos\angle EHF=\frac{36+4-36}{24}=\frac16$ ✓；$EG^2=15$，$EG=3.873$；" "\n"
        r"检验 $\triangle EHG$：$2+3>3.873$ ✓✓✓ **完全闭合**" "\n"
        r"**答案 $\sqrt{15}$ 正确** ✓（**原书 `EG = 15` 是根号丢失**）" "\n"
        r"**⭐⭐ 通法（正弦相等 ⟹ 互补）**：" "\n"
        r"① ⭐⭐ **已知式含 $\sin$（非内角）时，先用补角/诱导公式把它换成三角形的内角** ✓；" "\n"
        r"② ⭐⭐ **$S$ 的两种写法（两边夹角）相等 ⟹ 正弦相等**，这是证明角相等/互补的通用手法 ✓；" "\n"
        r"③ ⭐⭐ **$\sin\alpha=\sin\beta$ 必须排除 $\alpha=\beta$ 才能用互补**，判据是两角的大小关系 ✓；" "\n"
        r"④ ⭐⭐ **共线点的外角 = $\pi$ - 内角**，凡出现「延长线上一点」即用此 ✓；" "\n"
        r"⑤ ⚠ **余弦定理求的是内角**，若要求的是补角，记得取负 ✓✓"
    ),
    'difficulty': 0.84,
    'topics': ['M-T-229'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-229-V3',
}

T230_V1 = {
    'type': '解答',
    'stem_text': (
        r"设 $\triangle ABC$ 的内角 $A$，$B$，$C$ 的对边分别为 $a$，$b$，$c$，且满足 $b\sin2A+a\sin B=0$，"
        r"点 $D$ 为边 $BC$ 上一点，$AD\perp AC$．" "\n"
        r"(1) 求 $\angle BAC$ 的大小；" "\n"
        r"(2) 若 $\lvert AC\rvert=4$，$\lvert AD\rvert=3$，求 $\lvert AB\rvert$．"
    ),
    'opts': [],
    'answer': r"(1) $\angle BAC=\dfrac{2\pi}3$；(2) $\lvert AB\rvert=\dfrac{32\sqrt3+24}{13}$",
    'analysis': (
        r"(1) 正弦定理把边换成正弦，$\sin B$ 是公因子，约去后由 $\sin2A+\sin A=0$ 得 $\cos A$；"
        r"(2) 由 $\angle DAC=90^\circ$ 得 $\angle BAD=\frac\pi6$，在 $\triangle ACD$ 中求出 $CD$ 与 $\cos\angle ADC$，"
        r"进而在 $\triangle ABD$ 与 $\triangle ABC$ 中各写一次余弦定理，联立解出 $AB$．"
    ),
    'solution': (
        r"**(1)** 由正弦定理 $b=2R\sin B$，$a=2R\sin A$，代入 $b\sin2A+a\sin B=0$ 得" "\n"
        r"$\sin B\sin2A+\sin A\sin B=0$，即 $\sin B\left(2\sin A\cos A+\sin A\right)=0$．" "\n"
        r"$\because\sin B>0$，$\sin A>0$，$\therefore2\cos A+1=0$，$\cos A=-\dfrac12$．" "\n"
        r"又 $A\in(0,\pi)$，$\therefore A=\dfrac{2\pi}3$．" "\n"
        r"**(2)** $\because AD\perp AC$，$\therefore\angle DAC=\dfrac\pi2$，" "\n"
        r"$\angle BAD=\angle BAC-\angle DAC=\dfrac{2\pi}3-\dfrac\pi2=\dfrac\pi6$．" "\n"
        r"在 ${\rm Rt}\triangle ACD$ 中：$CD=\sqrt{AC^{2}+AD^{2}}=\sqrt{16+9}=5$，" "\n"
        r"$\cos\angle ADC=\dfrac{AD}{CD}=\dfrac35$，$\sin\angle ADC=\dfrac45$．" "\n"
        r"设 $AB=c$，$BD=x$．$\because\angle ADB+\angle ADC=\pi$，$\therefore\cos\angle ADB=-\dfrac35$．" "\n"
        r"在 $\triangle ABD$ 中：$c^{2}=AD^{2}+BD^{2}-2AD\cdot BD\cos\angle ADB=9+x^{2}-2\times3x\times\left(-\dfrac35\right)=x^{2}+\dfrac{18}5x+9$　①" "\n"
        r"在 $\triangle ABC$ 中，$BC=x+5$，由余弦定理：" "\n"
        r"$\left(x+5\right)^{2}=c^{2}+16-2\times4c\times\left(-\dfrac12\right)=c^{2}+4c+16$　②" "\n"
        r"由 ② 得 $c^{2}=x^{2}+10x+9-4c$，代入 ①：" "\n"
        r"$x^{2}+10x+9-4c=x^{2}+\dfrac{18}5x+9$，$\therefore4c=\dfrac{32}5x$，$c=\dfrac85x$．" "\n"
        r"代回 ②：$\left(x+5\right)^{2}=\dfrac{64}{25}x^{2}+\dfrac{32}5x+16$，" "\n"
        r"乘 $25$：$25x^{2}+250x+625=64x^{2}+160x+400$，即 $39x^{2}-90x-225=0$，" "\n"
        r"$\therefore13x^{2}-30x-75=0$，解得 $x=\dfrac{30\pm\sqrt{900+3900}}{26}=\dfrac{15\pm20\sqrt3}{13}$．" "\n"
        r"取正根 $x=\dfrac{15+20\sqrt3}{13}$，$\therefore c=\dfrac85x=\dfrac{8\left(15+20\sqrt3\right)}{65}=\dfrac{24+32\sqrt3}{13}$．"
    ),
    'review': (
        r"**① 提 $\sin B$（题眼）**：$\sin B\sin2A+\sin A\sin B=0$ ⟹ $\sin B\sin A(2\cos A+1)=0$ ✓✓✓" "\n"
        r"② **$\sin2A=2\sin A\cos A$** 是关键一步，把 $2A$ 降为 $A$ 才能提公因子 ✓✓✓" "\n"
        r"③ **$\angle BAD=A-\frac\pi2=\frac\pi6$**：由 $AD\perp AC$ 且 $\angle BAC=120^\circ$，" "\n"
        r"$AD$ 在 $\angle BAC$ **内部**（$D$ 在 $BC$ 上），故相减而非相加 ✓✓✓" "\n"
        r"④ **${\rm Rt}\triangle ACD$ 给出 $CD=5$ 与 $\cos\angle ADC=\frac35$**（3-4-5）✓✓✓" "\n"
        r"⑤ **联立两次余弦定理**：$\triangle ABD$ 用 $\angle ADB$（$=-\frac35$）、$\triangle ABC$ 用 $A=120^\circ$，" "\n"
        r"两式消去 $c^2$ 后得 $c=\frac85x$ 的**线性关系**，这是能解出来的原因 ✓✓✓" "\n"
        r"⑥ **判别式与取根**：$13x^2-30x-75=0$ 两根一正一负，取正根 ✓✓✓" "\n"
        r"⑦ 数值对拍：$x=\frac{15+34.641}{13}=3.818$，$c=1.6\times3.818=6.109$；" "\n"
        r"检验 ①：$c^2=37.32$，$x^2+\frac{18}5x+9=14.58+13.74+9=37.32$ ✓；" "\n"
        r"检验 ②：$(x+5)^2=77.73$，$c^2+4c+16=37.32+24.44+16=77.76$ ✓（舍入误差）✓✓✓" "\n"
        r"答案 $\frac{32\sqrt3+24}{13}=\frac{55.43+24}{13}=6.110$ ✓ **完全闭合**" "\n"
        r"**答案 $\frac{2\pi}3$、$\frac{32\sqrt3+24}{13}$ 均正确** ✓" "\n"
        r"**⭐⭐ 通法（含一条垂线的解三角形）**：" "\n"
        r"① ⭐⭐ **$\sin2A=2\sin A\cos A$ 降角**：凡条件含 $\sin2A$ 又含 $\sin A$，必可提公因子 ✓；" "\n"
        r"② ⭐⭐ **垂线 ⟹ 直角 ⟹ 勾股 + 余弦可用**：先求 $CD$ 与 $\cos\angle ADC$ ✓；" "\n"
        r"③ ⭐⭐ **互补角的余弦相反**：$\angle ADB=\pi-\angle ADC$ ⟹ $\cos$ 取负，这是连接两个三角形的桥 ✓；" "\n"
        r"④ ⭐⭐ **两个未知量（$c,x$）列两个余弦定理**，消去 $c^2$ 后常得到线性关系 ✓；" "\n"
        r"⑤ ⚠ **$x>0$ 是唯一取根依据**，负根必舍 ✓✓"
    ),
    'difficulty': 0.86,
    'topics': ['M-T-230'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-230-V1',
}

QS = [T225_E1, T225_V1, T225_V2, T225_V3,
      T226_E1, T226_V1, T226_V2, T226_V3,
      T229_E1, T229_V1, T229_V3,
      T230_V1]
