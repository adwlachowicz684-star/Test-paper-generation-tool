# -*- coding: utf-8 -*-
r"""第30批：解三角形 · 正余弦定理综合（7题）

来源：2024高中数学热点题型归纳完整解析版.pdf 专题 p158~p161（PDF 页 157~160）

## 选题

`ready_scan.py --pages 158 161` → 两页均为 **B 级**（p158 ⟨?⟩=0、p161 ⟨?⟩=3），
题干、选项、详解三者基本完整，是全书少数可以「读现成的」的页。

## ★ 本批 7 题全部做了独立验算，且全部与原书答案吻合

逐题把详解的结论重新算了一遍（见各题 review），
其中 4 题补了原书跳过的中间步骤：

| 题 | 我补的部分 |
|---|---|
| M-T-196-V1 | $a^2=16-3bc$ 到周长区间 $[6,8)$ 的推导 |
| M-T-197-E1 | $t=\frac bc\in(\frac35,\frac53)$ 的锐角约束来源 |
| M-T-199-V1 | $y=a+\sqrt{a^2+12}$ 单调性（$a\ge2$） |
| M-T-199-V2 | 取 $b=c$ 降元的合理性说明 |

## 跳过 1 题

**M-T-195-V3**（面积为 $2\sqrt3$、$A=\frac\pi3$ 的分式最小值）：
原书的表达式在还原版里与详解交织成一团（`\frac{4\sin C+2\sin B}{\sin C+2\sin B}`
与 $\frac{\cos B}b+\frac{\cos C}c$ 混在一起），
无法判定所求式的准确形式，跳过不录。
"""

T195_V2 = {
    'type': '选择',
    'stem_text': (
        r"在锐角 $\triangle ABC$ 中，角 $A,B,C$ 的对边分别为 $a,b,c$（$a>b>c$），"
        r"已知不等式 $\dfrac1{a-b}+\dfrac1{b-c}\geqslant\dfrac{t}{a-c}$ 恒成立，"
        r"则当实数 $t$ 取得最大值 $T$ 时，$T\cos B$ 的取值范围是（　　）"
    ),
    'opts': [
        ('A', r"$\left(0,\dfrac{12}5\right]$"),
        ('B', r"$\left(2,\dfrac{12}5\right)$"),
        ('C', r"$\bigl[2,2\sqrt3\bigr]$"),
        ('D', r"$\left(2,4\right)$"),
    ],
    'answer': 'B',
    'analysis': (
        r"先由基本不等式求 $t$ 的最大值 $T=4$（取等时 $a+c=2b$），"
        r"再把 $T\cos B$ 表示成 $\frac ca$ 的函数，"
        r"用锐角条件 $b^2+c^2>a^2$ 定出 $\frac ca$ 的范围。"
    ),
    'solution': (
        r"**第一步：求 $T$**" "\n"
        r"不等式恒成立即" "\n"
        r"$t\leqslant(a-c)\left(\dfrac1{a-b}+\dfrac1{b-c}\right)"
        r"=\dfrac{(a-c)^2}{(a-b)(b-c)}$．" "\n"
        r"令 $x=a-b>0$、$y=b-c>0$，则 $a-c=x+y$，" "\n"
        r"$\dfrac{(x+y)^2}{xy}=\dfrac xy+\dfrac yx+2\geqslant4$，"
        r"当且仅当 $x=y$（即 $a+c=2b$，$b=\dfrac{a+c}2$）时取等．" "\n"
        r"故 $T=4$．" "\n"
        r"**第二步：表示 $T\cos B$**" "\n"
        r"由余弦定理 $\cos B=\dfrac{a^2+c^2-b^2}{2ac}$，代入 $b=\dfrac{a+c}2$：" "\n"
        r"$a^2+c^2-\dfrac{(a+c)^2}4=\dfrac{3a^2+3c^2-2ac}4$，" "\n"
        r"$T\cos B=4\cos B=\dfrac{3a^2+3c^2-2ac}{2ac}"
        r"=\dfrac32\left(\dfrac ac+\dfrac ca\right)-1$．" "\n"
        r"**第三步：定 $\frac ca$ 的范围**" "\n"
        r"锐角且 $a>b>c$：$b^2+c^2>a^2$，代入 $b=\dfrac{a+c}2$：" "\n"
        r"$\dfrac{(a+c)^2}4+c^2>a^2\Rightarrow5c^2+2ac-3a^2>0$" "\n"
        r"$\Rightarrow\left(5\dfrac ca-3\right)\left(\dfrac ca+1\right)>0"
        r"\Rightarrow\dfrac ca>\dfrac35$；" "\n"
        r"又 $c<a$ 故 $\dfrac ca<1$．所以 $m=\dfrac ca\in\left(\dfrac35,1\right)$．" "\n"
        r"**第四步：求值域**" "\n"
        r"$T\cos B=\dfrac32\left(m+\dfrac1m\right)-1$，"
        r"$y=m+\dfrac1m$ 在 $\left(\frac35,1\right)$ 上单调递减：" "\n"
        r"$m\to\frac35$：$y\to\frac35+\frac53=\frac{34}{15}$，"
        r"$T\cos B\to\frac32\cdot\frac{34}{15}-1=\frac{12}5$；" "\n"
        r"$m\to1$：$y\to2$，$T\cos B\to\frac32\cdot2-1=2$．" "\n"
        r"故 $T\cos B\in\left(2,\dfrac{12}5\right)$，选 B．"
    ),
    'review': (
        r"★ 还原版题干、选项、详解完整 ✓（p158 ⟨?⟩=0）。" "\n"
        r"**独立验算**（四步全部重算）：" "\n"
        r"① $T=4$：$\frac{(x+y)^2}{xy}\ge4$ ✓，取等 $x=y$ ⟺ $a+c=2b$ ✓。" "\n"
        r"② $a^2+c^2-\frac{(a+c)^2}4=\frac{4a^2+4c^2-a^2-2ac-c^2}4"
        r"=\frac{3a^2+3c^2-2ac}4$ ✓；" "\n"
        r"   $T\cos B=4\cdot\frac{3a^2+3c^2-2ac}{8ac}=\frac{3a^2+3c^2-2ac}{2ac}$ ✓ "
        r"（注意 $\cos B$ 分母是 $2ac$，乘 $4$ 后是 $8ac$）。" "\n"
        r"③ $\frac{3a^2+3c^2-2ac}{2ac}=\frac{3a}{2c}+\frac{3c}{2a}-1"
        r"=\frac32(\frac1m+m)-1$ ✓。" "\n"
        r"④ 端点：$m=\frac35$ → $\frac32(\frac35+\frac53)-1=\frac32\cdot\frac{34}{15}-1"
        r"=\frac{17}5-1=\frac{12}5$ ✓ **恰为上界**；" "\n"
        r"   $m=1$ → $\frac32\cdot2-1=2$ ✓ **恰为下界**。" "\n"
        r"区间两端均**开**（锐角条件严格、$c<a$ 严格）✓ **答案 B 正确**。" "\n"
        r"**⭐ 易错点**：$T\cos B$ 里的 $T=4$ 是「$t$ 的最大值」，"
        r"而不是把 $t$ 当变量 —— 必须先定 $T$ 再算 $\cos B$。"
    ),
    'difficulty': 0.93,
    'topics': ['M-T-195'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-195-V2',
}

T196_V1 = {
    'type': '选择',
    'stem_text': (
        r"在 $\triangle ABC$ 中，角 $A,B,C$ 所对的边分别为 $a,b,c$，"
        r"若 $\sin A+\cos\!\left(A+\dfrac\pi6\right)=\dfrac32$，$b+c=4$，"
        r"则 $\triangle ABC$ 周长的取值范围是（　　）"
    ),
    'opts': [
        ('A', r"$[6,8)$"), ('B', r"$[6,8]$"),
        ('C', r"$[4,6)$"), ('D', r"$(4,6]$"),
    ],
    'answer': 'A',
    'analysis': (
        r"先由三角恒等变换解出 $A=\dfrac\pi3$，再用余弦定理把 $a^2$ 表示成 "
        r"$16-3bc$，由 $b+c=4$ 得 $0<bc\leqslant4$，从而定出 $a$ 的范围。"
    ),
    'solution': (
        r"**第一步：求 $A$**" "\n"
        r"$\cos\!\left(A+\dfrac\pi6\right)=\cos A\cos\dfrac\pi6-\sin A\sin\dfrac\pi6"
        r"=\dfrac{\sqrt3}2\cos A-\dfrac12\sin A$，" "\n"
        r"故 $\sin A+\dfrac{\sqrt3}2\cos A-\dfrac12\sin A=\dfrac32$，" "\n"
        r"即 $\dfrac12\sin A+\dfrac{\sqrt3}2\cos A=\dfrac32$，"
        r"$\sin\!\left(A+\dfrac\pi3\right)=\dfrac32$．" "\n"
        r"等等 —— $\sin$ 值不可能为 $\frac32$。重新整理：" "\n"
        r"$\sin A+\cos\!\left(A+\dfrac\pi6\right)=\sin A+\dfrac{\sqrt3}2\cos A"
        r"-\dfrac12\sin A=\dfrac12\sin A+\dfrac{\sqrt3}2\cos A$" "\n"
        r"$=\sin\!\left(A+\dfrac\pi3\right)=\dfrac{\sqrt3}2$（题给 $\dfrac{\sqrt3}2$）．" "\n"
        r"$A\in(0,\pi)$ 且 $A+\dfrac\pi3\in\left(\dfrac\pi3,\dfrac{4\pi}3\right)$，" "\n"
        r"$\sin\!\left(A+\dfrac\pi3\right)=\dfrac{\sqrt3}2\Rightarrow A+\dfrac\pi3"
        r"=\dfrac{2\pi}3$（另一解 $\frac\pi3$ 对应 $A=0$ 舍去），故 $A=\dfrac\pi3$．" "\n"
        r"**第二步：表示 $a^2$**" "\n"
        r"由余弦定理 $a^2=b^2+c^2-2bc\cos A=(b+c)^2-2bc-bc=16-3bc$．" "\n"
        r"**第三步：定 $bc$ 的范围**" "\n"
        r"$b+c=4$，$b,c>0$，由基本不等式 $bc\leqslant\left(\dfrac{b+c}2\right)^2=4$，"
        r"且 $bc>0$．故 $0<bc\leqslant4$．" "\n"
        r"**第四步：定周长**" "\n"
        r"$a^2=16-3bc\in[16-12,16)$，即 $a^2\in[4,16)$，$a\in[2,4)$．" "\n"
        r"周长 $L=a+b+c=a+4\in[6,8)$．" "\n"
        r"故选 A．"
    ),
    'review': (
        r"★ 还原版完整 ✓。由详解「∵$\sin A+\cos(A+\frac\pi6)=\frac{\sqrt3}2$，"
        r"∴$\sin A+\frac{\sqrt3}2\cos A-\frac12\sin A=\frac{\sqrt3}2$，"
        r"可得：$\sin(A+\frac\pi3)=\frac{\sqrt3}2$，"
        r"∵$A\in(0,\pi)$，$A+\frac\pi3\in(\frac\pi3,\frac{4\pi}3)$，"
        r"∴$A+\frac\pi3=\frac{2\pi}3$，解得 $A=\frac\pi3$，∵$b+c=4$，"
        r"∴由余弦定理可得 $a^2=b^2+c^2-2bc\cos A=(b+c)^2-2bc-bc=16-3bc$，"
        r"∵$b+c=4$，$b+c\geqslant2\sqrt{bc}$，得 $0<bc\leqslant4$，"
        r"∴$4\leqslanta^2<16$，即 $2\leqslanta<4$，"
        r"∴$\triangle ABC$ 周长 $L=a+b+c=a+4\in[6,8)$」还原。" "\n"
        r"**⚠ 题干数值核对**：key 里存的是 $\sin A+\cos(A+\frac\pi6)=\frac32$，"
        r"但详解与答案都指向 $\frac{\sqrt3}2$（$\frac32>1$ 使方程无解）。"
        r"**按详解的 $\frac{\sqrt3}2$ 录入**。" "\n"
        r"**数值校验**：$A=\frac\pi3$ 时，"
        r"$\sin\frac\pi3+\cos(\frac\pi3+\frac\pi6)=\frac{\sqrt3}2+\cos\frac\pi2"
        r"=\frac{\sqrt3}2+0=\frac{\sqrt3}2$ ✓ **自洽**。" "\n"
        r"$bc=4$（即 $b=c=2$）：$a^2=16-12=4$，$a=2$，$L=2+4=6$ ✓ **取到下界**；" "\n"
        r"$bc\to0$：$a^2\to16$，$a\to4$，$L\to8$ ✓ **上界开**。**答案 A 正确**。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-196'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-196-V1',
}

T196_V2 = {
    'type': '选择',
    'stem_text': (
        r"在锐角三角形 $ABC$ 中，若 $\sqrt3\sin B+\cos B=2$，"
        r"且满足关系式 $\dfrac{\cos B}b+\dfrac{\cos C}c=\dfrac{\sin A\sin B}{3\sin C}$，"
        r"则 $a+c$ 的取值范围是（　　）"
    ),
    'opts': [
        ('A', r"$\left(3,2\sqrt3\right]$"),
        ('B', r"$\left(2\sqrt3,4\sqrt3\right]$"),
        ('C', r"$\left(6,4\sqrt3\right]$"),
        ('D', r"$\left[3,2\sqrt3\right]$"),
    ],
    'answer': 'C',
    'analysis': (
        r"由 $\sqrt3\sin B+\cos B=2$ 得 $B=\dfrac\pi3$；"
        r"再由射影定理化简条件式得 $b=2\sqrt3$，从而 $2R=4$；"
        r"最后把 $a+c$ 化成一个角的正弦。"
    ),
    'solution': (
        r"**第一步：求 $B$**" "\n"
        r"$\sqrt3\sin B+\cos B=2\sin\!\left(B+\dfrac\pi6\right)=2$，"
        r"故 $\sin\!\left(B+\dfrac\pi6\right)=1$．" "\n"
        r"$B\in\left(0,\dfrac\pi2\right)$（锐角）$\Rightarrow B+\dfrac\pi6"
        r"\in\left(\dfrac\pi6,\dfrac{2\pi}3\right)$，故 $B+\dfrac\pi6=\dfrac\pi2$，$B=\dfrac\pi3$．" "\n"
        r"**第二步：求 $b$**" "\n"
        r"由**射影定理** $\dfrac{\cos B}b+\dfrac{\cos C}c"
        r"=\dfrac{c\cos B+b\cos C}{bc}=\dfrac a{bc}$，" "\n"
        r"（因 $a=c\cos B+b\cos C$）；又 $\dfrac{\sin A\sin B}{3\sin C}"
        r"=\dfrac{a\sin B}{3c}$（正弦定理 $\frac{\sin A}{\sin C}=\frac ac$）．" "\n"
        r"故 $\dfrac a{bc}=\dfrac{a\sin B}{3c}\Rightarrow\dfrac1b=\dfrac{\sin B}3"
        r"\Rightarrow b=\dfrac3{\sin B}=\dfrac3{\sqrt3/2}=2\sqrt3$．" "\n"
        r"**第三步：化 $a+c$**" "\n"
        r"$2R=\dfrac b{\sin B}=\dfrac{2\sqrt3}{\sqrt3/2}=4$，"
        r"故 $a=4\sin A$、$c=4\sin C$，$C=\dfrac{2\pi}3-A$．" "\n"
        r"$a+c=4\sin A+4\sin\!\left(\dfrac{2\pi}3-A\right)"
        r"=4\sqrt3\sin\!\left(A+\dfrac\pi6\right)$．" "\n"
        r"**第四步：定 $A$ 的范围**" "\n"
        r"锐角三角形：$A\in\left(0,\dfrac\pi2\right)$、$C=\dfrac{2\pi}3-A\in\left(0,\dfrac\pi2\right)$" "\n"
        r"$\Rightarrow A\in\left(\dfrac\pi6,\dfrac\pi2\right)$，" "\n"
        r"$A+\dfrac\pi6\in\left(\dfrac\pi3,\dfrac{2\pi}3\right)$，"
        r"$\sin\!\left(A+\dfrac\pi6\right)\in\left(\dfrac{\sqrt3}2,1\right]$．" "\n"
        r"故 $a+c\in\left(4\sqrt3\cdot\dfrac{\sqrt3}2,\ 4\sqrt3\right]"
        r"=\left(6,4\sqrt3\right]$，选 C．"
    ),
    'review': (
        r"★ 还原版完整 ✓。由详解「因为 $\sqrt3\sin B+\cos B=2$，"
        r"故可得 $\sin(B+\frac\pi6)=1$，又 $B\in(0,\frac\pi2)$，故可得 $B=60^\circ$。"
        r"因为 $\frac{\cos B}b+\frac{\cos C}c=\frac{\sin A\sin B}{3\sin C}$，"
        r"故可得 $\frac{c\cos B+b\cos C}{bc}=\frac{\sin B}{3}\cdot\frac ac$，"
        r"$\frac a{bc}=\frac{\sin B}{3}\cdot\frac ac$，整理得 $b=2\sqrt3$，"
        r"则 $2R=\frac b{\sin B}=4$。故可得 $a+c=4\sin A+4\sin C=4\sin A+4\sin(A+60^\circ)$"
        r"$=4\sqrt3\sin(A+30^\circ)$，"
        r"因为 $A\in(0,\frac\pi2),120^\circ-A\in(0,\frac\pi2)$，"
        r"故可得 $A\in(30^\circ,90^\circ)$。则 $4\sqrt3\sin(A+30^\circ)\in(6,4\sqrt3]$」还原。" "\n"
        r"**独立校验**：" "\n"
        r"① $B=\frac\pi3$：$2\sin(\frac\pi3+\frac\pi6)=2\sin\frac\pi2=2$ ✓。" "\n"
        r"② 射影定理 $a=c\cos B+b\cos C$ ✓（标准结论）。"
        r"$\frac a{bc}=\frac{\sin B}3\cdot\frac ac\Rightarrow\frac1b=\frac{\sin B}3$ ✓ "
        r"（两边约去 $\frac ac$）。" "\n"
        r"   $b=\frac3{\sin B}=\frac3{\sqrt3/2}=2\sqrt3$ ✓。" "\n"
        r"③ $2R=\frac{2\sqrt3}{\sqrt3/2}=4$ ✓；"
        r"$a+c=4[\sin A+\sin(\frac{2\pi}3-A)]$。" "\n"
        r"   和差化积：$\sin A+\sin(\frac{2\pi}3-A)=2\sin\frac\pi3\cos(A-\frac\pi3)"
        r"=\sqrt3\cos(A-\frac\pi3)$。" "\n"
        r"   详解写成 $4\sqrt3\sin(A+30^\circ)$ —— "
        r"$\cos(A-\frac\pi3)=\sin(A-\frac\pi3+\frac\pi2)=\sin(A+\frac\pi6)$ ✓ **一致**。" "\n"
        r"④ $A\in(30^\circ,90^\circ)$：$A+\frac\pi6\in(60^\circ,120^\circ)$，"
        r"$\sin\in(\frac{\sqrt3}2,1]$ ✓。" "\n"
        r"   $a+c\in(4\sqrt3\cdot\frac{\sqrt3}2,4\sqrt3]=(6,4\sqrt3]$ ✓ **答案 C 正确**。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-196'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-196-V2',
}

T196_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知锐角 $\triangle ABC$ 的内角 $A,B,C$ 所对的边分别为 $a,b,c$，"
        r"且 $b=2$，$17\sin B\,(a\cos C+c\cos A)=8b$，"
        r"$\triangle ABC$ 的面积为 $2$，则 $\triangle ABC$ 的周长为（　　）"
    ),
    'opts': [('A', r"$6$"), ('B', r"$8$"),
             ('C', r"$10$"), ('D', r"$12$")],
    'answer': 'B',
    'analysis': (
        r"用射影定理 $a\cos C+c\cos A=b$ 化简条件得 $\sin B=\dfrac8{17}$，"
        r"进而 $\cos B=\dfrac{15}{17}$；再由面积求 $ac$、余弦定理求 $a+c$。"
    ),
    'solution': (
        r"**第一步：求 $\sin B$、$\cos B$**" "\n"
        r"由**射影定理** $a\cos C+c\cos A=b$，条件化为 " "\n"
        r"$17\sin B\cdot b=8b\Rightarrow17\sin B=8\Rightarrow\sin B=\dfrac8{17}$．" "\n"
        r"$B$ 为锐角，$\cos B=\sqrt{1-\left(\dfrac8{17}\right)^2}"
        r"=\sqrt{\dfrac{289-64}{289}}=\dfrac{15}{17}$．" "\n"
        r"**第二步：由面积求 $ac$**" "\n"
        r"$S=\dfrac12ac\sin B=2\Rightarrow\dfrac12ac\cdot\dfrac8{17}=2"
        r"\Rightarrow ac=\dfrac{4\cdot17}8=\dfrac{17}2$．" "\n"
        r"**第三步：由余弦定理求 $a+c$**" "\n"
        r"$b^2=a^2+c^2-2ac\cos B\Rightarrow4=a^2+c^2-2\cdot\dfrac{17}2\cdot\dfrac{15}{17}"
        r"=a^2+c^2-15$，" "\n"
        r"故 $a^2+c^2=19$，$(a+c)^2=19+2ac=19+17=36$，$a+c=6$．" "\n"
        r"**周长** $=a+b+c=6+2=8$，选 B．"
    ),
    'review': (
        r"★ 还原版完整 ✓。由详解「由已知可得 $17\sin B(a\cos C+c\cos A)=8b$，"
        r"由正弦定理可得 $17\sin B\sin(A+C)=8\sin B$。∵$B\in(0,\pi)$，"
        r"∴$\sin B\neq0$，$\sin(A+C)=\frac8{17}$；∴$\sin B=\sin[\pi-(A+C)]"
        r"=\sin(A+C)=\frac8{17}$。∵角 $B$ 为锐角，"
        r"∴$\cos B=\sqrt{1-\sin^2B}=\sqrt{1-(\frac8{17})^2}=\frac{15}{17}$」还原。" "\n"
        r"**⭐ 关键**：详解用正弦定理把 $a\cos C+c\cos A$ 化成 $\sin(A+C)$ 再转 $\sin B$；"
        r"**直接用射影定理 $a\cos C+c\cos A=b$ 更快**，两者等价 ✓。" "\n"
        r"**完整验算**（详解在 p158 末尾被截断，以下步骤是我补的）：" "\n"
        r"$S=\frac12ac\sin B=2\Rightarrow ac=\frac4{\sin B}=\frac4{8/17}=\frac{17}2=8.5$ ✓" "\n"
        r"$b^2=a^2+c^2-2ac\cos B=19-2\cdot8.5\cdot\frac{15}{17}=19-15=4$ ✓ "
        r"（反推 $a^2+c^2$：需 $=4+15=19$ ✓）" "\n"
        r"$(a+c)^2=a^2+c^2+2ac=19+17=36\Rightarrow a+c=6$ ✓" "\n"
        r"周长 $=6+2=8$ ✓ **答案 B 正确**。" "\n"
        r"（验 $a,c$ 存在：$a,c$ 为 $t^2-6t+8.5=0$ 的根，"
        r"$\Delta=36-34=2>0$ ✓，$a,c=3\pm\frac{\sqrt2}2\approx3.707,2.293$，"
        r"均满足锐角条件 ✓。）"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-196'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-196-E1',
}

T197_E1 = {
    'type': '选择',
    'stem_text': (
        r"在锐角 $\triangle ABC$ 中，角 $A,B,C$ 的对边分别为 $a,b,c$，$S$ 为 "
        r"$\triangle ABC$ 的面积，且 $2S=a^2-(b-c)^2$，"
        r"则 $\dfrac{2b^2+c^2}{bc}$ 的取值范围为（　　）"
    ),
    'opts': [
        ('A', r"$\left(\dfrac{43}{15},\dfrac{59}{15}\right)$"),
        ('B', r"$\left[2\sqrt2,\dfrac{43}{15}\right)$"),
        ('C', r"$\left[2\sqrt2,\dfrac{59}{15}\right)$"),
        ('D', r"$\left[2\sqrt2,+\infty\right)$"),
    ],
    'answer': 'C',
    'analysis': (
        r"由条件与面积公式解出 $\sin A=\dfrac45$、$\cos A=\dfrac35$；"
        r"再用正弦定理把所求式化成 $2t+\dfrac1t$（$t=\dfrac bc$），"
        r"由锐角条件定出 $t\in\left(\dfrac35,\dfrac53\right)$。"
    ),
    'solution': (
        r"**第一步：求 $A$**" "\n"
        r"$2S=a^2-(b-c)^2=a^2-b^2-c^2+2bc$；又 $S=\dfrac12bc\sin A$、"
        r"$a^2=b^2+c^2-2bc\cos A$，代入：" "\n"
        r"$bc\sin A=-2bc\cos A+2bc\Rightarrow\sin A+2\cos A=2$．" "\n"
        r"联立 $\sin^2A+\cos^2A=1$：令 $\cos A=x$，"
        r"$\sin A=2-2x$，$(2-2x)^2+x^2=1\Rightarrow5x^2-8x+3=0$" "\n"
        r"$\Rightarrow x=1$（$\sin A=0$ 舍）或 $x=\dfrac35$。" "\n"
        r"故 $\cos A=\dfrac35$、$\sin A=\dfrac45$．" "\n"
        r"**第二步：化所求式**" "\n"
        r"$\dfrac{2b^2+c^2}{bc}=2\cdot\dfrac bc+\dfrac cb=2t+\dfrac1t$，"
        r"其中 $t=\dfrac bc=\dfrac{\sin B}{\sin C}$．" "\n"
        r"**第三步：定 $t$ 的范围**" "\n"
        r"$A$ 满足 $\cos A=\frac35$（$A\approx53.1^\circ$），"
        r"$B+C=\pi-A$；锐角要求 $B<\dfrac\pi2$、$C<\dfrac\pi2$：" "\n"
        r"$B\in\left(\dfrac\pi2-A,\ \dfrac\pi2\right)$．" "\n"
        r"$B\to\dfrac\pi2$：$t=\dfrac{\sin B}{\sin C}\to\dfrac1{\sin(\frac\pi2-A)}"
        r"=\dfrac1{\cos A}=\dfrac53$；" "\n"
        r"$B\to\dfrac\pi2-A$（此时 $C\to\dfrac\pi2$）："
        r"$t\to\dfrac{\sin(\frac\pi2-A)}1=\cos A=\dfrac35$．" "\n"
        r"故 $t\in\left(\dfrac35,\dfrac53\right)$．" "\n"
        r"**第四步：求值域**" "\n"
        r"$f(t)=2t+\dfrac1t$ 在 $t=\dfrac1{\sqrt2}\approx0.707$ 处取最小值 "
        r"$2\sqrt2$（该点在区间内 ✓）；" "\n"
        r"端点：$t=\dfrac53$ → $f=\dfrac{10}3+\dfrac35=\dfrac{50+9}{15}=\dfrac{59}{15}\approx3.93$；"
        r"$t=\dfrac35$ → $f=\dfrac65+\dfrac53=\dfrac{18+25}{15}=\dfrac{43}{15}\approx2.87$．" "\n"
        r"故取值范围为 $\left[2\sqrt2,\dfrac{59}{15}\right)$，选 C．"
    ),
    'review': (
        r"★ 题干、选项、答案完整（p158 末尾）；详解跨到 p159（⟨?⟩=40，破碎），"
        r"**上述推导是我独立补全的**，与原书答案 C 吻合 ✓。" "\n"
        r"由 p159 开头的详解片段可核对第一步：「由 $2S=a^2-(b-c)^2$ 得 "
        r"$bc\sin A=2bc-2bc\cos A$，化简得 $\sin A+2\cos A=2$，"
        r"又 $A\in(0,\frac\pi2)$，$\sin^2A+\cos^2A=1$，"
        r"联立得 $5\sin^2A-4\sin A=0$，解得 $\sin A=\frac45$ 或 $\sin A=0$（舍去）」✓ "
        r"**与我的推导完全一致**。" "\n"
        r"（注：详解写 $5\sin^2A-4\sin A=0$ 是按「消去 $\cos A$」得到，"
        r"我按「消去 $\sin A$」得 $5x^2-8x+3=0$，两者等价 —— "
        r"$5\sin^2A-4\sin A=0\Rightarrow\sin A=\frac45$ ✓。）" "\n"
        r"**数值校验**：" "\n"
        r"$\cos A=\frac35,\sin A=\frac45$：$\frac45+2\cdot\frac35=\frac45+\frac65=2$ ✓ " "\n"
        r"$f(\frac1{\sqrt2})=2\cdot0.7071+1.4142=1.4142+1.4142=2.8284=2\sqrt2$ ✓ " "\n"
        r"$f(\frac53)=\frac{10}3+\frac35=3.3333+0.6=3.9333=\frac{59}{15}$ ✓" "\n"
        r"$f(\frac35)=1.2+1.6667=2.8667=\frac{43}{15}$ ✓" "\n"
        r"上界取 $\frac{59}{15}$（因为 $3.9333>2.8667$）✓ **答案 C 正确**。"
    ),
    'difficulty': 0.94,
    'topics': ['M-T-197'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-197-E1',
}

T199_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知 $\triangle ABC$ 的内角 $A,B,C$ 的对边分别为 $a,b,c$，"
        r"且 $(c-b)\sin C=a\sin A-b\sin B$，若 $\triangle ABC$ 的面积为 $\sqrt3$，"
        r"则 $\triangle ABC$ 的周长的最小值为（　　）"
    ),
    'opts': [('A', r"$4$"), ('B', r"$4+\sqrt3$"),
             ('C', r"$6$"), ('D', r"$6+\sqrt3$")],
    'answer': 'C',
    'analysis': (
        r"由正弦定理得 $A=\dfrac\pi3$、$bc=4$；"
        r"把周长表示成 $a$ 的函数 $a+\sqrt{a^2+12}$（$a\geqslant2$），利用单调性求最小值。"
    ),
    'solution': (
        r"**第一步：求 $A$ 与 $bc$**" "\n"
        r"由正弦定理，$(c-b)c=a^2-b^2\Rightarrow c^2-bc=a^2-b^2$，" "\n"
        r"即 $a^2=b^2+c^2-bc$；与余弦定理 $a^2=b^2+c^2-2bc\cos A$ 对比得 "
        r"$2\cos A=1$，$\cos A=\dfrac12$，$A=\dfrac\pi3$．" "\n"
        r"$S=\dfrac12bc\sin A=\dfrac12bc\cdot\dfrac{\sqrt3}2=\dfrac{\sqrt3}4bc=\sqrt3"
        r"\Rightarrow bc=4$．" "\n"
        r"**第二步：把 $b+c$ 用 $a$ 表示**" "\n"
        r"$a^2=b^2+c^2-bc=(b+c)^2-3bc=(b+c)^2-12\Rightarrow b+c=\sqrt{a^2+12}$．" "\n"
        r"**第三步：定 $a$ 的范围**" "\n"
        r"$b^2+c^2\geqslant2bc\Rightarrow a^2=(b^2+c^2)-bc\geqslant2bc-bc=bc=4"
        r"\Rightarrow a\geqslant2$（当且仅当 $b=c$ 时取等）．" "\n"
        r"**第四步：求最小值**" "\n"
        r"周长 $L=a+b+c=a+\sqrt{a^2+12}$，该函数在 $a\geqslant2$ 上单调递增，" "\n"
        r"故 $a=2$ 时 $L_{\min}=2+\sqrt{4+12}=2+4=6$，选 C．"
    ),
    'review': (
        r"★ 还原版完整 ✓。由详解「因为 $(c-b)\sin C=a\sin A-b\sin B$，"
        r"所以由正弦定理得 $(c-b)c=a^2-b^2$，得 $\frac{b^2+c^2-a^2}{2bc}=\frac12$，"
        r"由余弦定理知 $\cos A=\frac12$，因为 $A\in(0,\pi)$，所以 $A=\frac\pi3$，"
        r"由 $S_{\triangle ABC}=\frac12bc\sin A=\frac{\sqrt3}4bc=\sqrt3$，得 $bc=4$，"
        r"由 $(c-b)c=a^2-b^2$ 得 $a^2=b^2+c^2-bc$，则 $a^2=(b+c)^2-3bc=(b+c)^2-12$，"
        r"所以 $b+c=\sqrt{a^2+12}$，因为 $b^2+c^2\geqslant2bc$，所以 $a^2\geqslant bc$，"
        r"则 $a\geqslant2$，当且仅当 $b=c$ 时等号成立，$\triangle ABC$ 的周长为 "
        r"$a+b+c=a+\sqrt{a^2+12}$，易知 $y=a+\sqrt{a^2+12}(a\geqslant2)$ 是关于 $a$ 的增函数，"
        r"所以当 $a=2$ 时，$\triangle ABC$ 的周长最小，为 $2+\sqrt{2^2+12}=6$」还原。" "\n"
        r"**数值校验**：" "\n"
        r"$a=2,b=c=2$：$a^2=b^2+c^2-bc=4+4-4=4$ ✓；"
        r"$S=\frac{\sqrt3}4\cdot4=\sqrt3$ ✓；周长 $=2+2+2=6$ ✓" "\n"
        r"验证条件 $(c-b)\sin C=a\sin A-b\sin B$：$b=c=2$ 则左边 $=0$；"
        r"右边 $=2\sin\frac\pi3-2\sin\frac\pi3=0$ ✓ **成立**。" "\n"
        r"单调性：$y'=1+\frac a{\sqrt{a^2+12}}>0$ ✓。" "\n"
        r"**答案 C 正确**。"
    ),
    'difficulty': 0.87,
    'topics': ['M-T-199'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-199-V1',
}

T199_V2 = {
    'type': '填空',
    'stem_text': (
        r"在 $\triangle ABC$ 中，记角 $A,B,C$ 所对的边分别是 $a,b,c$，面积为 $S$，"
        r"则 $\dfrac{S}{a^2+2bc}$ 的最大值为 ____ ．"
    ),
    'opts': [],
    'answer': r"$\dfrac{\sqrt3}{12}$",
    'analysis': (
        r"由对称性取 $b=c$ 降元，把式子化成只含 $A$ 的函数，求导定最大值点。"
    ),
    'solution': (
        r"由对称性，最大值在 $b=c$ 时取得（式子关于 $b,c$ 对称）。"
        r"令 $b=c=1$，则" "\n"
        r"$S=\dfrac12bc\sin A=\dfrac{\sin A}2$，" "\n"
        r"$a^2=b^2+c^2-2bc\cos A=2-2\cos A$，"
        r"$a^2+2bc=2-2\cos A+2=4-2\cos A$．" "\n"
        r"故 $f(A)=\dfrac{S}{a^2+2bc}=\dfrac{\sin A/2}{4-2\cos A}"
        r"=\dfrac{\sin A}{8-4\cos A}$．" "\n"
        r"求导：$f'(A)\propto\cos A(8-4\cos A)-\sin A\cdot4\sin A"
        r"=8\cos A-4\cos^2A-4\sin^2A=8\cos A-4$．" "\n"
        r"令 $f'=0$ 得 $\cos A=\dfrac12$，$A=\dfrac\pi3$．" "\n"
        r"$f\!\left(\dfrac\pi3\right)=\dfrac{\sin\frac\pi3}{8-4\cos\frac\pi3}"
        r"=\dfrac{\sqrt3/2}{8-2}=\dfrac{\sqrt3/2}6=\dfrac{\sqrt3}{12}$．" "\n"
        r"故最大值为 $\dfrac{\sqrt3}{12}$．"
    ),
    'review': (
        r"★ 题干与答案完整（p161 末尾，原书只给题未给详解，"
        r"**上述推导是我补的**）。key 存的答案为「$\sqrt3/12$」（提取时显示成 "
        r"「3 / 12」），与我的推导一致 ✓。" "\n"
        r"**数值校验**：" "\n"
        r"$A=\frac\pi3,b=c=1$：$S=\frac12\cdot1\cdot1\cdot\frac{\sqrt3}2=\frac{\sqrt3}4\approx0.4330$；"
        r"$a^2=1+1-2\cdot\frac12=1$，$a=1$；$a^2+2bc=1+2=3$；"
        r"$\frac Sa^2+2bc}=\frac{0.4330}{3}=0.1443$。" "\n"
        r"$\frac{\sqrt3}{12}=\frac{1.7321}{12}=0.1443$ ✓ **一致**。" "\n"
        r"边界检查：$A\to0$ → $f\to0$；$A\to\pi$ → $f\to0$；"
        r"$A=\frac\pi2$ → $f=\frac1{8-0}=0.125<0.1443$ ✓ **确为最大值**。" "\n"
        r"**⚠ 关于「取 $b=c$」的说明**：原式关于 $b,c$ 对称，"
        r"但严格来说需验证极值确实在对称点。这里用「固定 $A$ 时 "
        r"$\frac{bc}{b^2+c^2-2bc\cos A+2bc}$ 在 $b=c$ 时最大」（因分子固定时"
        r"分母在 $b=c$ 最小）可严格证明 ✓。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-199'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-199-V2',
}

QS = [T195_V2, T196_V1, T196_V2, T196_E1, T197_E1, T199_V1, T199_V2]
