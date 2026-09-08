# -*- coding: utf-8 -*-
r"""第37批：正余弦定理与解三角形小题（3题）

来源：2024高中数学热点题型归纳完整解析版.pdf p154（PDF 页 153）

## 选题

`pick_batch.py --n 14` → p154（M-T-190）。

## 跳过 1 题

**M-T-190-V1**：题干 `sin(A+C) cosB b + cosC c = sinA sinC` 无法判定分式结构，
四个选项提取后**完全相同**（都是 `32 , 3`）。无法可靠还原，跳过。

## ★ 三题的关键还原：根号丢失

| 题 | 提取 | 实际 |
|---|---|---|
| E1 | 选项 `32`/`3`/`2 3`/`4` | $\frac{\sqrt3}2$、$\sqrt3$、$2\sqrt3$、$4$ |
| V2 | 选项 `33`/`2 33`/`4 33`/`2 3` | $\frac{\sqrt3}3$、$\frac{2\sqrt3}3$、$\frac{4\sqrt3}3$、$2\sqrt3$ |
| **V3** | 题干 `a = 3` | **$a=\sqrt3$** ← 反证得出 |

## ⚠ V3 的 $a=\sqrt3$ 是反证出来的（本批最关键）

若 $a=3$：$a^{2}=9$，$2R=2\sqrt3$，$bc=6\cos(B-C)+3\in(6,9]$
→ 结果 $(21,27]$，**四选项无一符合**。

取 $a=\sqrt3$：$a^{2}=3$，$2R=2$，$bc=2\cos(B-C)+1\in(2,3]$
→ $3+2bc\in(7,9]$ ✓ **与答案 D 完全吻合**。

## 三题验算

| 题 | 结果 | 答案 |
|---|---|---|
| E1 | $\cos A=\frac12$、$bc\le4$ → $S\le\sqrt3$ | **B** |
| V2 | $\cos B=-\frac12$ → $B=\frac{2\pi}3$；$A=30^\circ$ 时 $S=\frac1{\sqrt3}$ | **A** |
| V3 | $b^{2}+c^{2}+bc=3+2bc$，$bc\in(2,3]$ → $(7,9]$ | **D** |
"""

T190_E1 = {
    'type': '选择',
    'stem_text': (
        r"$\triangle ABC$ 的内角 $A,B,C$ 的对边分别为 $a,b,c$，"
        r"若 $(\sin B+\sin C)^{2}-\sin^{2}(B+C)=3\sin B\sin C$，且 $a=2$，"
        r"则 $\triangle ABC$ 的面积的最大值是（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac{\sqrt3}2$"),
        ('B', r"$\sqrt3$"),
        ('C', r"$2\sqrt3$"),
        ('D', r"$4$"),
    ],
    'answer': 'B',
    'analysis': (
        r"由 $\sin(B+C)=\sin A$ 化条件为边的等式 $b^{2}+c^{2}-a^{2}=bc$，"
        r"余弦定理得 $\cos A=\frac12$；再用 $a^2\ge bc$ 求面积最值。"
    ),
    'solution': (
        r"**第一步：化简条件**" "\n"
        r"因 $\sin(B+C)=\sin(\pi-A)=\sin A$，条件化为 $(\sin B+\sin C)^{2}-\sin^{2}A=3\sin B\sin C$．" "\n"
        r"展开：$\sin^{2}B+\sin^{2}C+2\sin B\sin C-\sin^{2}A=3\sin B\sin C$．" "\n"
        r"即 $\sin^{2}B+\sin^{2}C-\sin^{2}A=\sin B\sin C$．" "\n"
        r"**第二步：化边（正弦定理）**" "\n"
        r"同乘 $(2R)^{2}$ 得 $b^{2}+c^{2}-a^{2}=bc$，即 $a^{2}=b^{2}+c^{2}-bc$．" "\n"
        r"**第三步：余弦定理求 $A$**" "\n"
        r"$\cos A=\dfrac{b^{2}+c^{2}-a^{2}}{2bc}=\dfrac{bc}{2bc}=\dfrac12$，故 $A=\dfrac\pi3$、$\sin A=\dfrac{\sqrt3}2$．" "\n"
        r"**第四步：基本不等式求最值**" "\n"
        r"$a=2$ 代入：$4=b^{2}+c^{2}-bc\ge 2bc-bc=bc$，即 $bc\le4$（当 $b=c=2$ 时取等）．" "\n"
        r"$S=\dfrac12bc\sin A\le\dfrac12\times4\times\dfrac{\sqrt3}2=\sqrt3$．选 B．"
    ),
    'review': (
        r"★ 由详解「∵$\sin(B+C)=\sin A$，且 $(\sin B+\sin C)^{2}-\sin^{2}(B+C)=3\sin B\sin C$，"
        r"∴$\sin^{2}B+\sin^{2}C-\sin^{2}A=\sin B\sin C$，由正弦定理可得 $a^{2}+b^{2}-c^{2}=bc$…"
        r"由余弦定理可得 $\cos A=\frac{b^2+c^2-a^2}{2bc}=\frac12$，$\sin A=\frac{\sqrt3}2$，"
        r"又∵$a=2$，∴$4=b^{2}+c^{2}-bc\ge2bc-bc=bc$，即 $bc\le4$，"
        r"∴$S=\frac12bc\times\sin A\le\frac12\times4\times\frac{\sqrt3}2=\sqrt3$」还原。" "\n"
        r"（注：详解中间写「$a^{2}+b^{2}-c^{2}=bc$」，但下一步用的是 "
        r"$\cos A=\frac{b^2+c^2-a^2}{2bc}=\frac12$，故**正确的是 $b^{2}+c^{2}-a^{2}=bc$**，按此录入。）" "\n"
        r"**选项还原**（PDF 页 153，y≈126：`A.B.3C. 2 3D. 4`）："
        r"A 的 `3` 带分数线 → $\frac{\sqrt3}2$；B `3`→$\sqrt3$；C `2 3`→$2\sqrt3$；D `4`→$4$。"
        r"四值 $0.866<1.732<3.464<4$ 递增 ✓" "\n"
        r"**独立验算**：" "\n"
        r"① 取等条件 $b=c=2$：$a^2=4+4-4=4$ → $a=2$ ✓ **与题设吻合**" "\n"
        r"② $S=\frac12\times2\times2\times\frac{\sqrt3}2=\sqrt3\approx1.732$ ✓" "\n"
        r"③ 回代原条件（等边三角形，$A=B=C=60^\circ$）：" "\n"
        r"左 $=(\frac{\sqrt3}2+\frac{\sqrt3}2)^2-\sin^2120^\circ=3-\frac34=\frac94$；"
        r"右 $=3\times\frac{\sqrt3}2\times\frac{\sqrt3}2=\frac94$ ✓✓ **条件成立**" "\n"
        r"**答案 B 正确** ✓" "\n"
        r"**⭐ 套路**：见 $(\sin B+\sin C)^2-\sin^2A$ 型，**先换成边**再配余弦定理，"
        r"最后用 $b^2+c^2\ge2bc$ 求最值。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-190'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-190-E1',
}

T190_V2 = {
    'type': '选择',
    'stem_text': (
        r"在 $\triangle ABC$ 中，角 $A,B,C$ 的对边分别是 $a,b,c$，"
        r"且 $\sin(B+C)+2\sin A\cos B=0$．若 $b=2$，"
        r"则 $\triangle ABC$ 面积的最大值为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac{\sqrt3}3$"),
        ('B', r"$\dfrac{2\sqrt3}3$"),
        ('C', r"$\dfrac{4\sqrt3}3$"),
        ('D', r"$2\sqrt3$"),
    ],
    'answer': 'A',
    'analysis': (
        r"由 $\sin(B+C)=\sin A$ 得 $\sin A(1+2\cos B)=0$，故 $\cos B=-\frac12$、$B=\frac{2\pi}3$；"
        r"用正弦定理把 $c$ 表成关于 $A$ 的函数，面积化为余弦型函数求最值。"
    ),
    'solution': (
        r"**第一步：求 $B$**" "\n"
        r"$\sin(B+C)=\sin A$，故 $\sin A+2\sin A\cos B=0$，即 $\sin A(1+2\cos B)=0$．" "\n"
        r"因 $\sin A\neq0$，得 $\cos B=-\dfrac12$，即 $B=\dfrac{2\pi}3$．" "\n"
        r"**第二步：正弦定理表示 $c$**" "\n"
        r"$C=\pi-A-B=\dfrac\pi3-A$，且 $\dfrac c{\sin C}=\dfrac b{\sin B}$：" "\n"
        r"$c=\dfrac{2\sin(\frac\pi3-A)}{\sin\frac{2\pi}3}=\dfrac{2\sin(\frac\pi3-A)}{\frac{\sqrt3}2}=\dfrac4{\sqrt3}\sin\!\left(\dfrac\pi3-A\right)$．" "\n"
        r"由 $A>0$、$C>0$ 得 $A\in\left(0,\dfrac\pi3\right)$．" "\n"
        r"**第三步：面积化为关于 $A$ 的函数**" "\n"
        r"$S=\dfrac12bc\sin A=\dfrac4{\sqrt3}\sin\!\left(\dfrac\pi3-A\right)\sin A$．" "\n"
        r"积化和差：$\sin\!\left(\dfrac\pi3-A\right)\sin A=\dfrac12\cos\!\left(2A-\dfrac\pi3\right)-\dfrac14$．" "\n"
        r"$S=\dfrac4{\sqrt3}\left[\dfrac12\cos\!\left(2A-\dfrac\pi3\right)-\dfrac14\right]=\dfrac2{\sqrt3}\cos\!\left(2A-\dfrac\pi3\right)-\dfrac1{\sqrt3}$．" "\n"
        r"**第四步：求最值**" "\n"
        r"$2A-\dfrac\pi3\in\left(-\dfrac\pi3,\dfrac\pi3\right)$，故 $\cos\!\left(2A-\dfrac\pi3\right)\in\left(\dfrac12,1\right]$，" "\n"
        r"最大值为 $1$（当 $A=\dfrac\pi6$ 时取到）．" "\n"
        r"$S_{\max}=\dfrac2{\sqrt3}-\dfrac1{\sqrt3}=\dfrac1{\sqrt3}=\dfrac{\sqrt3}3$．选 A．"
    ),
    'review': (
        r"★ 由详解「由 $\sin(B+C)+2\sin A\cos B=0$，得 $\sin A+2\sin A\cos B=0$，"
        r"∴$\sin A\cdot(1+2\cos B)=0$，又 $\sin A\neq0$，∴$1+2\cos B=0$，即 $\cos B=-\frac12$，"
        r"又 $B\in(0,\pi)$，∴$B=\frac{2\pi}3$，$C=\pi-A-B=\frac\pi3-A$，"
        r"又 $\frac c{\sin C}=\frac b{\sin B}$，∴$c=\frac{2\sin(\frac\pi3-A)}{\sin\frac{2\pi}3}$…"
        r"$S_{\triangle ABC}=\frac12bc\sin A$…由 $0<A<\frac\pi3$，有 $\frac\pi6<2A+\frac\pi6<\frac{5\pi}6$，"
        r"则 $\sin(2A+\frac\pi6)\le1$…即面积的最大值是 $\frac{\sqrt3}3$。故选 A」还原。" "\n"
        r"（$c=\frac{4\sqrt3}3\sin(\frac\pi3-A)$ 与我写的 $\frac4{\sqrt3}\sin(\frac\pi3-A)$ **相同** ✓）" "\n"
        r"**⚠ 详解中间式有系数笔误（如实标注）**：它写 "
        r"$S=\frac{\sqrt3}3\sin(2A+\frac\pi6)-\frac{\sqrt3}6$，代入 $A=30^\circ$ 得 "
        r"$\frac{\sqrt3}3-\frac{\sqrt3}6=\frac{\sqrt3}6\approx0.2887$，**与实际面积 $0.5774$ 差一半**。" "\n"
        r"正确系数应为 $\frac{2\sqrt3}3$ 与 $\frac{\sqrt3}3$（验：$A=30^\circ$ 时 "
        r"$\frac{2\sqrt3}3-\frac{\sqrt3}3=\frac{\sqrt3}3$ ✓）。**详解结论对、中间式子错**，按答案录入。" "\n"
        r"**独立验算**（直接取 $A=30^\circ$ 算）：" "\n"
        r"$B=120^\circ$、$C=30^\circ$、$b=2$；$2R=\frac2{\sin120^\circ}=\frac4{\sqrt3}$；"
        r"$c=\frac4{\sqrt3}\sin30^\circ=\frac2{\sqrt3}$" "\n"
        r"$S=\frac12bc\sin A=\frac12\times2\times\frac2{\sqrt3}\times\frac12=\frac1{\sqrt3}=\frac{\sqrt3}3\approx0.5774$ ✓" "\n"
        r"与我的公式对拍：$\frac2{\sqrt3}\cos0-\frac1{\sqrt3}=\frac1{\sqrt3}$ ✓✓ **一致**" "\n"
        r"**答案 A 正确** ✓"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-190'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-190-V2',
}

T190_V3 = {
    'type': '选择',
    'stem_text': (
        r"设锐角 $\triangle ABC$ 的内角 $A,B,C$ 所对的边分别为 $a,b,c$，"
        r"若 $A=\dfrac\pi3$，$a=\sqrt3$，则 $b^{2}+c^{2}+bc$ 的取值范围为（　　）"
    ),
    'opts': [
        ('A', r"$(1,9]$"),
        ('B', r"$(3,9]$"),
        ('C', r"$(5,9]$"),
        ('D', r"$(7,9]$"),
    ],
    'answer': 'D',
    'analysis': (
        r"由余弦定理 $a^{2}=b^{2}+c^{2}-bc$ 把所求化为 $a^{2}+2bc$；"
        r"再用正弦定理把 $bc$ 表成 $\cos(B-C)$ 的函数，由「锐角」条件定出 $B-C$ 的范围。"
    ),
    'solution': (
        r"**第一步：余弦定理转化所求**" "\n"
        r"$a^{2}=b^{2}+c^{2}-2bc\cos\dfrac\pi3=b^{2}+c^{2}-bc$，故 $b^{2}+c^{2}+bc=a^{2}+2bc=3+2bc$．" "\n"
        r"**第二步：把 $bc$ 表成角的函数**" "\n"
        r"$2R=\dfrac a{\sin A}=\dfrac{\sqrt3}{\sqrt3/2}=2$，故 $b=2\sin B$、$c=2\sin C$．" "\n"
        r"$bc=4\sin B\sin C=2\bigl[\cos(B-C)-\cos(B+C)\bigr]$．" "\n"
        r"由 $B+C=\dfrac{2\pi}3$ 得 $\cos(B+C)=-\dfrac12$，故 $bc=2\cos(B-C)+1$．" "\n"
        r"**第三步：锐角条件定范围（关键）**" "\n"
        r"锐角要求 $B<\dfrac\pi2$ 且 $C=\dfrac{2\pi}3-B<\dfrac\pi2$，后者得 $B>\dfrac\pi6$．" "\n"
        r"故 $B\in\left(\dfrac\pi6,\dfrac\pi2\right)$，$B-C=2B-\dfrac{2\pi}3\in\left(-\dfrac\pi3,\dfrac\pi3\right)$．" "\n"
        r"$\cos(B-C)\in\left(\dfrac12,1\right]$（上界在 $B=C=\dfrac\pi3$ 时取到），故 $bc\in(2,3]$．" "\n"
        r"**第四步**：$b^{2}+c^{2}+bc=3+2bc\in(7,9]$．选 D．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**原书无详解**，上述为我独立完成）。" "\n"
        r"**⚠⚠ 题干 $a=\sqrt3$ 是反证出来的（本批最关键）**：提取文本为 `a = 3`（根号丢失），"
        r"两种取值结果完全不同：" "\n"
        r"· 若 $a=3$：$a^{2}=9$，$2R=2\sqrt3$，$bc=6\cos(B-C)+3\in(6,9]$ → $9+2bc\in(21,27]$ "
        r"**四选项无一符合** ✗" "\n"
        r"· 若 $a=\sqrt3$：$a^{2}=3$，$2R=2$，$bc=2\cos(B-C)+1\in(2,3]$ → $3+2bc\in(7,9]$ ✓✓ "
        r"**与答案 D 完全吻合**" "\n"
        r"**故题干应为 $a=\sqrt3$，按此录入。**" "\n"
        r"**独立验算**：" "\n"
        r"① 上界（$B=C=\frac\pi3$，正三角形）：$a=b=c=\sqrt3$，$b^2+c^2+bc=3+3+3=9$ ✓ 恰为 $9$；"
        r"三角均为 $60^\circ$ 锐角 ✓ 可取" "\n"
        r"② 下界（$B\to\frac\pi2$，$C\to\frac\pi6$）：$b\to2$、$c\to1$，$b^2+c^2+bc\to4+1+2=7$ ✓ "
        r"恰为 $7$；取不到（$B=\frac\pi2$ 非锐角）✓" "\n"
        r"③ 中点抽查 $B=50^\circ$、$C=70^\circ$：$b=1.5321$、$c=1.8794$；"
        r"$2.3473+3.5321+2.8794=8.7588\in(7,9]$ ✓" "\n"
        r"**答案 D 正确** ✓" "\n"
        r"**⭐ 易错点**：「锐角」条件**不能漏**。若只用 $B+C=\frac{2\pi}3$ 而不加锐角限制，"
        r"会得到 $B\in(0,\frac{2\pi}3)$、$bc$ 范围变大，答案就错了。"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-190'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-190-V3',
}

QS = [T190_E1, T190_V2, T190_V3]
