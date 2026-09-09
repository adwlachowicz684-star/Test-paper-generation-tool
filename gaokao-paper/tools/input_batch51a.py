# -*- coding: utf-8 -*-
r"""第51批：解三角形 · 角与对边（解答题，4 题全录）

来源：2024高中数学热点题型归纳完整解析版.pdf
题干见 p154（PDF 页 153），**详解在 p183**（PDF 页 182）—— 两处相距 29 页。

⚠ **这是本批最大的坑**：`pick_batch` 把四题都定位到 p154，但 p154 只有题干、
**详解一个字都没有**。我是在全书搜索 `sinA - sinB + sinC` 才找到 p183 的。
**以后遇到「题干完整但详解缺失」，先全书 grep 关键词，别急着自己硬推。**

## ★★ 四题的共同结构

都是「第一问用正余弦定理求角，第二问借助该角求边长/面积」，
破题眼几乎都是同一招：**用 $\sin(B+C)=\sin A$ 把混合项收拢**。

| 题 | 破题眼 | 答案 |
|---|---|---|
| E1 | $b\cos2A$ 移到右边成 $b(1-\cos2A)=2b\sin^{2}A$，与左边约掉 $\sin^{2}A$ | $B=\frac\pi3$；$a=2$ |
| V1 | $5a\cos B=4b\cos C+4c\cos B$ ⟹ 右边 $=4\sin(B+C)=4\sin A$ | $\cos B=\frac45$；$\sin A=\frac{7\sqrt2}{10}$ |
| V2 | ⭐ $a\cos B+b\cos A=c$（**射影定理**）⟹ $2c\cos C=c$ 直接出 $\cos C=\frac12$ | $C=\frac\pi3$；周长 $5+\sqrt7$ |
| V3 | ⭐ 平方差：$\bigl(\sin C+(\sin A-\sin B)\bigr)\bigl(\sin C-(\sin A-\sin B)\bigr)$ | $C=\frac\pi4$；$S=8\sqrt2$ |

## ⚠ 两处原书笔误（详解自身矛盾，已用答案反推修正）

**1. E1 题干**：`2asinAcos B 2` 实为 $2a\sin A\cos\frac B2$。
判据：按 $\cos^{2}B$ 理解得 $\sin B=\frac{\sqrt5-1}2$，$B\approx38.2^\circ\neq\frac\pi3$；
按 $\cos\frac B2$ 理解得 $\cos\frac B2=\sin B$ ⟹ $\sin\frac B2=\frac12$ ⟹ $B=\frac\pi3$ ✓
（p183 详解明确写「$2a\sin A\cos\frac B2=2b\sin^{2}A$」，与后者一致。）

**2. V3 题干**：第二个因子是 $\sin C-\sin A+\sin B$，**不是** $\sin A-\sin B-\sin C$。
按后者会得到 $\cos C=\frac{4-\sqrt2}2\approx1.293>1$ **无解**；
按前者得 $\sin^{2}A+\sin^{2}B-\sin^{2}C=\sqrt2\sin A\sin B$ ⟹ $\cos C=\frac{\sqrt2}2$ ⟹ $C=\frac\pi4$ ✓
（详解里 `(2 - 2)` 是 $2-\sqrt2$ 根号丢失。）
"""

T218_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知 $\triangle ABC$ 中，角 $A,B,C$ 所对的边分别为 $a,b,c$，"
        r"$2a\sin A\cos\dfrac B2+b\cos2A=b$．" "\n"
        r"（1）求 $B$ 的值；" "\n"
        r"（2）若 $a+c=4$，$\triangle ABC$ 的面积为 $\sqrt3$，求 $a$ 的值．"
    ),
    'opts': [],
    'answer': r"（1）$B=\dfrac\pi3$；（2）$a=2$",
    'analysis': (
        r"把 $b\cos2A$ 移到右边得 $2a\sin A\cos\frac B2=b(1-\cos2A)=2b\sin^{2}A$，"
        r"两边都有 $\sin^{2}A$，约掉后只剩 $\cos\frac B2=\sin B$，再用二倍角解出 $B$。"
    ),
    'solution': (
        r"**（1）求 $B$**" "\n"
        r"由已知：$2a\sin A\cos\dfrac B2=b(1-\cos2A)$．" "\n"
        r"因 $1-\cos2A=2\sin^{2}A$，得 $2a\sin A\cos\dfrac B2=2b\sin^{2}A$．" "\n"
        r"由正弦定理 $a=2R\sin A$、$b=2R\sin B$，代入并约去 $2R$：" "\n"
        r"$2\sin^{2}A\cos\dfrac B2=2\sin B\sin^{2}A$．" "\n"
        r"因 $A\in(0,\pi)$，$\sin A\neq0$，故 $\cos\dfrac B2=\sin B$．" "\n"
        r"又 $\sin B=2\sin\dfrac B2\cos\dfrac B2$，且 $B\in(0,\pi)$ 时 $\cos\dfrac B2\neq0$：" "\n"
        r"$1=2\sin\dfrac B2\Rightarrow\sin\dfrac B2=\dfrac12\Rightarrow\dfrac B2=\dfrac\pi6\Rightarrow B=\dfrac\pi3$．" "\n"
        r"**（2）求 $a$**" "\n"
        r"$S=\dfrac12 ac\sin B=\dfrac12 ac\cdot\dfrac{\sqrt3}2=\sqrt3\Rightarrow ac=4$．" "\n"
        r"又 $a+c=4$，由韦达定理 $a,c$ 是 $t^{2}-4t+4=0$ 的两根，" "\n"
        r"$(t-2)^{2}=0\Rightarrow a=c=2$．故 $a=2$．"
    ),
    'review': (
        r"★ 题干、答案完整 ✓，详解在 **p183**（不在 p154）。" "\n"
        r"由详解「由已知得：$2a\sin A\cos\frac B2=2b\sin^{2}A$。由正弦定理得：" "\n"
        r"$\sin^{2}A\cos\frac B2=\sin B\sin^{2}A$…所以得 $\cos\frac B2=\sin B=2\sin\frac B2\cos\frac B2$…" "\n"
        r"$\sin\frac B2=\frac12$…即 $B=\frac\pi3$」「(2) 由已知得 $\frac12 ac\sin B=\sqrt3$，得 $ac=4$，" "\n"
        r"又因为 $a+c=4$，所以 $a=c=2$」还原，与我的推导**完全一致** ✓。" "\n"
        r"**⚠ 题干还原（根号/分数线丢失）**：ref_bank 存 `2asinAcos B 2 + bcos2A = b`。" "\n"
        r"我试了两种读法：" "\n"
        r"· 按 $\cos^{2}B$：$\cos^{2}B=\sin B$ ⟹ $\sin^{2}B+\sin B-1=0$ ⟹ $\sin B=\frac{\sqrt5-1}2\approx0.618$ ⟹ $B\approx38.2^\circ\neq\frac\pi3$ ✗" "\n"
        r"· 按 $\cos\frac B2$：$\cos\frac B2=\sin B$ ⟹ $\sin\frac B2=\frac12$ ⟹ $B=\frac\pi3$ ✓✓" "\n"
        r"**p183 详解明确写 $\cos\frac B2$**，与后者一致 —— 这就是决定性证据。" "\n"
        r"**独立验算**：" "\n"
        r"① $B=\frac\pi3$ 时 $\cos\frac B2=\cos30^\circ=\frac{\sqrt3}2$；$\sin B=\sin60^\circ=\frac{\sqrt3}2$ ✓✓ **相等**" "\n"
        r"② **代回原式验证**：取 $A=60^\circ$、$B=60^\circ$、$C=60^\circ$（等边），则 $a=b=c$。" "\n"
        r"左边 $=2a\sin60^\circ\cos30^\circ+b\cos120^\circ=2a\cdot\frac{\sqrt3}2\cdot\frac{\sqrt3}2+a\cdot(-\frac12)=\frac32a-\frac12a=a$" "\n"
        r"右边 $=b=a$ ✓✓✓ **原式成立**" "\n"
        r"③ **（2）**：$ac=4$、$a+c=4$ ⟹ $a=c=2$；验 $(t-2)^2=t^2-4t+4$ ⟹ 和 $4$、积 $4$ ✓✓" "\n"
        r"验面积：$\frac12\cdot2\cdot2\cdot\sin60^\circ=2\cdot\frac{\sqrt3}2=\sqrt3$ ✓✓✓" "\n"
        r"**答案（1）$\frac\pi3$、（2）$a=2$ 正确** ✓" "\n"
        r"**⭐ 通法（$b\cos2A$ 型）**：" "\n"
        r"① 看到 $\cos2A$ 与单独的 $b$，**先移项**凑 $1-\cos2A=2\sin^{2}A$；" "\n"
        r"② 两边都出现 $\sin^{2}A$ 时**直接约掉**（因 $\sin A\neq0$），这是题目故意设计的；" "\n"
        r"③ 剩下 $\cos\frac B2=\sin B$ 后，用 $\sin B=2\sin\frac B2\cos\frac B2$ 约去 $\cos\frac B2$（$\frac B2\in(0,\frac\pi2)$ 故不为 $0$）。" "\n"
        r"**⚠ 易错**：$\cos\frac B2\neq0$ 这一步必须说明，否则约分无依据。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-218'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-218-E1',
}

T218_V1 = {
    'type': '解答',
    'stem_text': (
        r"在 $\triangle ABC$ 中，角 $A,B,C$ 的对边分别为 $a,b,c$，"
        r"已知 $(5a-4c)\cos B=4b\cos C$．" "\n"
        r"（1）求 $\cos B$ 的值；" "\n"
        r"（2）若 $C=\dfrac\pi4$，$b=6$，求 $\sin A$ 的值．"
    ),
    'opts': [],
    'answer': r"（1）$\cos B=\dfrac45$；（2）$\sin A=\dfrac{7\sqrt2}{10}$",
    'analysis': (
        r"展开并把含 $\cos B$ 的项放一边：$5a\cos B=4c\cos B+4b\cos C$，"
        r"边化角后右边两项正好凑成 $4\sin(B+C)=4\sin A$，与左边的 $\sin A$ 约掉。"
    ),
    'solution': (
        r"**（1）求 $\cos B$**" "\n"
        r"由 $(5a-4c)\cos B=4b\cos C$ 展开：$5a\cos B=4c\cos B+4b\cos C$．" "\n"
        r"由正弦定理边化角（同除以 $2R$）：$5\sin A\cos B=4\sin C\cos B+4\sin B\cos C$．" "\n"
        r"右边 $=4(\sin C\cos B+\cos C\sin B)=4\sin(B+C)=4\sin(\pi-A)=4\sin A$．" "\n"
        r"故 $5\sin A\cos B=4\sin A$．因 $A\in(0,\pi)$，$\sin A\neq0$，得 $\cos B=\dfrac45$．" "\n"
        r"**（2）求 $\sin A$**" "\n"
        r"由 $\cos B=\dfrac45$ 且 $B\in(0,\pi)$：$\sin B=\sqrt{1-\dfrac{16}{25}}=\dfrac35$．" "\n"
        r"$\sin A=\sin(B+C)=\sin B\cos C+\cos B\sin C$" "\n"
        r"$=\dfrac35\cdot\dfrac{\sqrt2}2+\dfrac45\cdot\dfrac{\sqrt2}2=\dfrac{7}{5}\cdot\dfrac{\sqrt2}2=\dfrac{7\sqrt2}{10}$．"
    ),
    'review': (
        r"★ 题干、答案完整 ✓，由 p183 详解「因为 $(5a-4c)\cos B=4b\cos C$，所以由正弦定理得" "\n"
        r"$(5\sin A-4\sin C)\cos B=4\sin B\cos C$…所以 $5\sin A\cos B=4(\sin B\cos C+\sin C\cos B)=4\sin(B+C)$，" "\n"
        r"所以 $5\sin A\cos B=4\sin A$，又 $A\in(0,\pi),\sin A\neq0$，所以 $\cos B=\frac45$」还原，" "\n"
        r"与我的推导**逐字一致** ✓。" "\n"
        r"**独立验算**：" "\n"
        r"① **验 $\cos B=\frac45$ 满足原式**：$\sin B=\frac35$。" "\n"
        r"取 $B=\arccos\frac45\approx36.87^\circ$、$C=45^\circ$，则 $A=180^\circ-36.87^\circ-45^\circ=98.13^\circ$" "\n"
        r"$\sin A=\sin98.13^\circ\approx0.9899$；$\sin B=0.6$；$\sin C=0.7071$" "\n"
        r"左边 $=(5\sin A-4\sin C)\cos B=(4.9495-2.8284)(0.8)=2.1211\times0.8=1.6969$" "\n"
        r"右边 $=4\sin B\cos C=4(0.6)(0.7071)=1.6970$ ✓✓ **两边相等**" "\n"
        r"② **（2）验 $\sin A$**：$\sin B\cos C+\cos B\sin C=0.6(0.7071)+0.8(0.7071)=0.4243+0.5657=0.9899$" "\n"
        r"$\frac{7\sqrt2}{10}=\frac{7(1.4142)}{10}=\frac{9.8995}{10}=0.98995$ ✓✓✓" "\n"
        r"③ **用 $\sin A=\sin(B+C)$ 交叉验证第一问的值**：$\sin A\approx0.9899$，" "\n"
        r"与上面由角度算出的 $\sin98.13^\circ$ 一致 ✓✓" "\n"
        r"**答案（1）$\frac45$、（2）$\frac{7\sqrt2}{10}$ 正确** ✓" "\n"
        r"**⭐ 通法（$(\alpha a-\beta c)\cos B=\gamma b\cos C$ 型）**：" "\n"
        r"① **移项**：把含 $\cos B$ 的都放左边，含 $\cos C$ 的放右边 —— 目的是凑 $\sin C\cos B+\cos C\sin B$；" "\n"
        r"② 边化角后识别 $\sin(B+C)$，**它恒等于 $\sin A$**；" "\n"
        r"③ 左右都含 $\sin A$，约掉即得 $\cos B$ 的常数值。" "\n"
        r"**这个「凑 $\sin(B+C)=\sin A$」是本类题的通用收尾动作。**"
    ),
    'difficulty': 0.83,
    'topics': ['M-T-218'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-218-V1',
}

T218_V2 = {
    'type': '解答',
    'stem_text': (
        r"$\triangle ABC$ 的内角 $A,B,C$ 的对边分别为 $a,b,c$，"
        r"已知 $2\cos C\,(a\cos B+b\cos A)=c$．" "\n"
        r"（1）求角 $C$ 的大小；" "\n"
        r"（2）若 $c=\sqrt7$，$\triangle ABC$ 的面积为 $\dfrac{3\sqrt3}2$，求 $\triangle ABC$ 的周长．"
    ),
    'opts': [],
    'answer': r"（1）$C=\dfrac\pi3$；（2）$5+\sqrt7$",
    'analysis': (
        r"**射影定理**：$a\cos B+b\cos A=c$（这是本题的秒杀点，括号里的整块直接等于 $c$）。"
        r"于是 $2c\cos C=c$ ⟹ $\cos C=\frac12$。第二问用 $S$ 求 $ab$、余弦定理求 $a+b$。"
    ),
    'solution': (
        r"**（1）求 $C$**" "\n"
        r"由**射影定理** $a\cos B+b\cos A=c$（可自行验证：边化角后" "\n"
        r"$\sin A\cos B+\sin B\cos A=\sin(A+B)=\sin C$，再乘 $2R$ 即 $c$）．" "\n"
        r"代入已知：$2\cos C\cdot c=c$．因 $c>0$，得 $\cos C=\dfrac12$，故 $C=\dfrac\pi3$．" "\n"
        r"**（2）求周长**" "\n"
        r"$S=\dfrac12 ab\sin C=\dfrac12 ab\cdot\dfrac{\sqrt3}2=\dfrac{3\sqrt3}2\Rightarrow ab=6$．" "\n"
        r"由余弦定理：$c^{2}=a^{2}+b^{2}-2ab\cos C=a^{2}+b^{2}-ab$．" "\n"
        r"$7=a^{2}+b^{2}-6\Rightarrow a^{2}+b^{2}=13$．" "\n"
        r"$(a+b)^{2}=a^{2}+b^{2}+2ab=13+12=25\Rightarrow a+b=5$．" "\n"
        r"周长 $=a+b+c=5+\sqrt7$．"
    ),
    'review': (
        r"★ 题干、答案完整 ✓，由 p183 详解「(2) 由余弦定理得 $7=a^{2}+b^{2}-2ab\cdot\frac12$，" "\n"
        r"∴ $(a+b)^{2}-3ab=7$，∵ $S=\frac12 ab\sin C=\frac{3\sqrt3}2$，∴ $ab=6$，" "\n"
        r"∴ $(a+b)^{2}-18=7$，∴ $a+b=5$，∴ $\triangle ABC$ 的周长为 $5+\sqrt7$」还原，" "\n"
        r"与我的推导**完全一致** ✓。" "\n"
        r"**独立验算**：" "\n"
        r"① **射影定理验证**：$a\cos B+b\cos A=c$" "\n"
        r"边化角：$2R\sin A\cos B+2R\sin B\cos A=2R\sin(A+B)=2R\sin C=c$ ✓✓" "\n"
        r"② **（1）**：$2\cos C\cdot c=c$ ⟹ $\cos C=\frac12$ ⟹ $C=60^\circ$ ✓" "\n"
        r"③ **（2）求 $ab$**：$\frac12 ab\cdot\frac{\sqrt3}2=\frac{3\sqrt3}2$ ⟹ $ab\cdot\frac{\sqrt3}4=\frac{3\sqrt3}2$ ⟹ $ab=6$ ✓" "\n"
        r"④ **求 $a+b$**：$a^2+b^2=7+ab=13$；$(a+b)^2=13+12=25$ ⟹ $a+b=5$ ✓" "\n"
        r"⑤ **反解 $a,b$ 验证存在性**：$t^2-5t+6=0$ ⟹ $(t-2)(t-3)=0$ ⟹ $\{a,b\}=\{2,3\}$" "\n"
        r"验：$2+3=5$ ✓、$2\times3=6$ ✓" "\n"
        r"验 $c$：$c^2=4+9-2(2)(3)(0.5)=13-6=7$ ⟹ $c=\sqrt7$ ✓✓✓ **完全闭合**" "\n"
        r"验面积：$\frac12\cdot2\cdot3\cdot\sin60^\circ=3\cdot\frac{\sqrt3}2=\frac{3\sqrt3}2$ ✓✓✓" "\n"
        r"周长 $=2+3+\sqrt7=5+\sqrt7$ ✓✓✓" "\n"
        r"**答案（1）$\frac\pi3$、（2）$5+\sqrt7$ 正确** ✓" "\n"
        r"**⭐ 通法（射影定理）**：" "\n"
        r"$$a\\cos B+b\\cos A=c,\\quad b\\cos C+c\\cos B=a,\\quad c\\cos A+a\\cos C=b$$" "\n"
        r"**看到 $a\cos B+b\cos A$ 这种「两边乘另一边邻角余弦之和」，直接换成第三边** —— " "\n"
        r"比展开成 $\sin$ 再化简快得多，也是命题人设的「送分入口」。" "\n"
        r"**⚠ 记忆法**：$a\cos B+b\cos A$ 中，$a$ 配 $\cos B$、$b$ 配 $\cos A$（**交叉配**），结果是 $c$。" "\n"
        r"（配错成 $a\cos A+b\cos B$ 就没有这个结论了。）"
    ),
    'difficulty': 0.83,
    'topics': ['M-T-218'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-218-V2',
}

T218_V3 = {
    'type': '解答',
    'stem_text': (
        r"$\triangle ABC$ 的内角 $A,B,C$ 的对边分别为 $a,b,c$，已知" "\n"
        r"$(\sin A-\sin B+\sin C)(\sin C-\sin A+\sin B)=(2-\sqrt2)\sin A\sin B$．" "\n"
        r"（1）求角 $C$；" "\n"
        r"（2）若 $b=4$，$\sin A\,(1-2\cos C)=2\cos A\sin C$，求 $\triangle ABC$ 的面积．"
    ),
    'opts': [],
    'answer': r"（1）$C=\dfrac\pi4$；（2）$8\sqrt2$",
    'analysis': (
        r"（1）把两个因子看成 $\bigl(\sin C+(\sin A-\sin B)\bigr)\bigl(\sin C-(\sin A-\sin B)\bigr)$，" "\n"
        r"用**平方差**得 $\sin^{2}C-(\sin A-\sin B)^{2}$，整理出 $\sin^{2}A+\sin^{2}B-\sin^{2}C$ ⟹ 余弦定理。" "\n"
        r"（2）把 $2\cos A\sin C$ 移到左边凑 $2(\sin A\cos C+\cos A\sin C)=2\sin(A+C)=2\sin B$ ⟹ $a=2b$。"
    ),
    'solution': (
        r"**（1）求 $C$**" "\n"
        r"记 $u=\sin A-\sin B$，则原式左边 $=(\sin C+u)(\sin C-u)=\sin^{2}C-u^{2}$：" "\n"
        r"$\sin^{2}C-(\sin A-\sin B)^{2}=(2-\sqrt2)\sin A\sin B$" "\n"
        r"$\sin^{2}C-\sin^{2}A+2\sin A\sin B-\sin^{2}B=(2-\sqrt2)\sin A\sin B$" "\n"
        r"$\Rightarrow\sin^{2}A+\sin^{2}B-\sin^{2}C=2\sin A\sin B-(2-\sqrt2)\sin A\sin B=\sqrt2\sin A\sin B$．" "\n"
        r"由正弦定理（同乘 $(2R)^{2}$）：$a^{2}+b^{2}-c^{2}=\sqrt2\,ab$．" "\n"
        r"由余弦定理：$\cos C=\dfrac{a^{2}+b^{2}-c^{2}}{2ab}=\dfrac{\sqrt2\,ab}{2ab}=\dfrac{\sqrt2}2$．" "\n"
        r"因 $C\in(0,\pi)$，得 $C=\dfrac\pi4$．" "\n"
        r"**（2）求面积**" "\n"
        r"由 $\sin A(1-2\cos C)=2\cos A\sin C$ 展开：" "\n"
        r"$\sin A=2\sin A\cos C+2\cos A\sin C=2\sin(A+C)=2\sin(\pi-B)=2\sin B$．" "\n"
        r"由正弦定理：$a=2b=8$．" "\n"
        r"$S=\dfrac12 ab\sin C=\dfrac12\cdot8\cdot4\cdot\dfrac{\sqrt2}2=8\sqrt2$．"
    ),
    'review': (
        r"★ 题干与答案基本完整 ✓，详解在 **p183**。" "\n"
        r"**⚠⚠ 题干还原（本批最关键的一处）**：ref_bank 把第二个因子存成 $\sin A-\sin B-\sin C$。" "\n"
        r"**按这个读会推出 $\cos C=\frac{4-\sqrt2}2\approx1.293>1$，无解** ✗。" "\n"
        r"正确应为 $\sin C-\sin A+\sin B$（即 $-(\sin A-\sin B-\sin C)$，**提取时丢了负号**）。" "\n"
        r"修正后：$\sin^{2}A+\sin^{2}B-\sin^{2}C=\sqrt2\sin A\sin B$ ⟹ $\cos C=\frac{\sqrt2}2$ ⟹ $C=\frac\pi4$ ✓ " "\n"
        r"与答案完全吻合。**「按字面推会得出 $\cos C>1$」就是最硬的修正依据。**" "\n"
        r"（另：详解里的 `(2 - 2)` 是 $2-\sqrt2$ 的根号丢失。）" "\n"
        r"**独立验算**：" "\n"
        r"① **构造一个满足条件的三角形反验**：取 $C=45^\circ$、$a=8$、$b=4$（第 2 问的结果）" "\n"
        r"$c^{2}=64+16-2(8)(4)\cos45^\circ=80-64(0.7071)=80-45.255=34.745$ ⟹ $c=5.894$" "\n"
        r"$\sin A=\frac{a}{2R}$、$\sin B=\frac{b}{2R}$、$\sin C=\frac{c}{2R}$（令 $2R=\frac{c}{\sin C}=\frac{5.894}{0.7071}=8.335$）" "\n"
        r"$\sin A=\frac8{8.335}=0.9598$、$\sin B=\frac4{8.335}=0.4799$、$\sin C=0.7071$" "\n"
        r"$u=\sin A-\sin B=0.4799$" "\n"
        r"左边 $=(\sin C+u)(\sin C-u)=(0.7071+0.4799)(0.7071-0.4799)=1.1870\times0.2272=0.2697$" "\n"
        r"右边 $=(2-\sqrt2)\sin A\sin B=(0.5858)(0.9598)(0.4799)=0.5858\times0.4606=0.2698$ ✓✓✓ **相等**" "\n"
        r"② **（2）验 $\sin A=2\sin B$**：$A=\arcsin(0.9598)\approx73.7^\circ$、$B=180^\circ-45^\circ-73.7^\circ=61.3^\circ$" "\n"
        r"$\sin B=\sin61.3^\circ=0.8771$；$2\sin B=1.7542\neq0.9598$？？" "\n"
        r"**⚠ 检查**：由 $a=2b$ 应得 $\sin A=2\sin B$，但 $\sin A=0.9598$、$\sin B=0.4799$ → 比值 $=2.0$ ✓" "\n"
        r"（我上面算 $B$ 时用了 $73.7^\circ$ 但 $\sin73.7^\circ$ 与 $\sin106.3^\circ$ 相同 —— " "\n"
        r"$A$ 也可能是 $106.3^\circ$，此时 $B=180^\circ-45^\circ-106.3^\circ=28.7^\circ$，$\sin B=0.4801$ ✓✓" "\n"
        r"**取 $A=106.3^\circ$ 才自洽**（因 $a=8>b=4$，故 $A>B$，且 $a$ 最大 ⟹ $A$ 最大）。）" "\n"
        r"③ **面积**：$\frac12\cdot8\cdot4\cdot\sin45^\circ=16\cdot0.7071=11.314$；$8\sqrt2=11.3137$ ✓✓✓" "\n"
        r"**答案（1）$\frac\pi4$、（2）$8\sqrt2$ 正确** ✓" "\n"
        r"**⭐ 通法（两个三项正弦式相乘）**：" "\n"
        r"① **先找公共部分**：本题两个因子是 $\sin C+u$ 与 $\sin C-u$（$u=\sin A-\sin B$），" "\n"
        r"识别出来就能用平方差，比逐项展开（9 项）省事得多；" "\n"
        r"② 目标是把式子化成 $\sin^{2}A+\sin^{2}B-\sin^{2}C$ —— **这个组合正好对应余弦定理的分子**；" "\n"
        r"③ 边化角后 $a^{2}+b^{2}-c^{2}=k\,ab$ ⟹ $\cos C=\frac k2$，一步出角。" "\n"
        r"**⚠ 易错**：第二问 $\sin A=2\sin B$ ⟹ $a=2b$ 后，" "\n"
        r"**别直接用 $A=2B$**（$\sin$ 相等不代表角相等，本题 $A\approx106^\circ$、$B\approx29^\circ$ 就不是 2 倍关系）。"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-218'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-218-V3',
}

QS = [T218_E1, T218_V1, T218_V2, T218_V3]
