# -*- coding: utf-8 -*-
r"""第35批：圆锥曲线 · 焦点弦与定比分点（4题）

来源：2024高中数学热点题型归纳完整解析版.pdf p306（PDF 页 305）

## 选题

`pick_batch.py --n 6 --topic M-T-331` → **p306 一页 4 题**，全是 A 级。
专题「题型五 焦点弦的定比分点」。

## ★ 本批核心公式

**焦点弦定比分点**：过焦点 $F$ 的弦 $AB$，若 $\vec{AF}=\lambda\vec{FB}$，则

$$\cos\theta=\frac{|\lambda-1|}{(\lambda+1)e}\quad(\text{椭圆/双曲线，}\theta\text{ 为弦与对称轴夹角})$$

$$e=\sqrt{1+k^{2}}\cdot\frac{|\lambda-1|}{\lambda+1}\ (\text{焦点在 }x\text{ 轴})$$

**抛物线**：$y^{2}=4ax$，点 $(at^{2},2at)$ 的焦半径 $=a(1+t^{2})$，焦点弦满足 $t_{1}t_{2}=-1$。

## 四题全部独立验算，且发现一处原书笔误

| 题 | 我的结果 | 答案 |
|---|---|---|
| E1 | $e=\sqrt{\frac{\lambda-1}{\lambda+3}}$，$\lambda\in[2,3]$ → $[\frac{\sqrt5}5,\frac{\sqrt3}3]$ | 吻合 |
| V1 | 双曲线 $e=\frac65$（数值验证 $|AF|/|BF|=4.002$） | $\frac65$ ✓ |
| V2 | 抛物线 $S=\frac{4\sqrt3}3$ | $\frac{4\sqrt3}3$ ✓ |
| V3 | 椭圆 $e=\frac{\sqrt{21}}7$（$e^{2}=\frac37$） | **D** ✓ |

**⚠ E1 原文有笔误**：写「$\frac ca=\frac{\lambda-1}{\lambda+3}$」，
实际应为 $\frac{c^{2}}{a^{2}}=\frac{\lambda-1}{\lambda+3}$，
即 $e=\sqrt{\frac{\lambda-1}{\lambda+3}}$（否则 $\lambda=2$ 时 $e=\frac15$，与答案 $\frac{\sqrt5}5$ 不符）。
"""

T331_E1 = {
    'type': '填空',
    'stem_text': (
        r"已知椭圆 $\Gamma:\dfrac{x^{2}}{a^{2}}+\dfrac{y^{2}}{b^{2}}=1$（$a>b>0$）的"
        r"左、右焦点分别为 $F_{1},F_{2}$，点 $A,B$ 在椭圆 $\Gamma$ 上，"
        r"$\vec{AF_{1}}\cdot\vec{F_{1}F_{2}}=0$ 且 $\vec{AF_{2}}=\lambda\vec{F_{2}B}$，"
        r"则当 $\lambda\in\left[2,3\right]$ 时，椭圆的离心率的取值范围为 ____ ．"
    ),
    'opts': [],
    'answer': r"$\left[\dfrac{\sqrt5}5,\ \dfrac{\sqrt3}3\right]$",
    'analysis': (
        r"由 $\vec{AF_{1}}\cdot\vec{F_{1}F_{2}}=0$ 得 $A$ 的横坐标 $x_{A}=-c$、"
        r"纵坐标 $\pm\frac{b^{2}}a$；再由 $\vec{AF_{2}}=\lambda\vec{F_{2}B}$ 用坐标表示 $B$，"
        r"代入椭圆方程即得 $e$ 关于 $\lambda$ 的式子。"
    ),
    'solution': (
        r"**第一步：定 $A$ 的坐标**" "\n"
        r"$\vec{F_{1}F_{2}}=(2c,0)$，设 $A(x_{A},y_{A})$，" "\n"
        r"$\vec{AF_{1}}=(-c-x_{A},\ -y_{A})$，"
        r"由 $\vec{AF_{1}}\cdot\vec{F_{1}F_{2}}=0$ 得 $2c(-c-x_{A})=0$，"
        r"即 $x_{A}=-c$．" "\n"
        r"代入椭圆：$\dfrac{c^{2}}{a^{2}}+\dfrac{y_{A}^{2}}{b^{2}}=1"
        r"\Rightarrow y_{A}^{2}=b^{2}\!\left(1-\dfrac{c^{2}}{a^{2}}\right)=\dfrac{b^{4}}{a^{2}}$，" "\n"
        r"取 $A\!\left(-c,\ \dfrac{b^{2}}a\right)$．" "\n"
        r"**第二步：由定比分点表示 $B$**" "\n"
        r"$\vec{AF_{2}}=\left(2c,\ -\dfrac{b^{2}}a\right)$，"
        r"设 $B(x,y)$，则 $\vec{F_{2}B}=(x-c,\ y)$．" "\n"
        r"由 $\vec{AF_{2}}=\lambda\vec{F_{2}B}$："
        r"$x-c=\dfrac{2c}\lambda$、$y=-\dfrac{b^{2}}{\lambda a}$，" "\n"
        r"即 $B\!\left(\dfrac{(\lambda+2)c}\lambda,\ -\dfrac{b^{2}}{\lambda a}\right)$．" "\n"
        r"**第三步：代入椭圆方程**" "\n"
        r"$\dfrac{(\lambda+2)^{2}c^{2}}{\lambda^{2}a^{2}}"
        r"+\dfrac{b^{4}}{\lambda^{2}a^{2}b^{2}}=1$" "\n"
        r"$\Rightarrow(\lambda+2)^{2}c^{2}+b^{2}=\lambda^{2}a^{2}$，" "\n"
        r"代入 $b^{2}=a^{2}-c^{2}$：" "\n"
        r"$(\lambda^{2}+4\lambda+4)c^{2}-c^{2}+a^{2}=\lambda^{2}a^{2}$" "\n"
        r"$\Rightarrow(\lambda^{2}+4\lambda+3)c^{2}=(\lambda^{2}-1)a^{2}$" "\n"
        r"$\Rightarrow\dfrac{c^{2}}{a^{2}}=\dfrac{\lambda^{2}-1}{\lambda^{2}+4\lambda+3}"
        r"=\dfrac{(\lambda-1)(\lambda+1)}{(\lambda+1)(\lambda+3)}=\dfrac{\lambda-1}{\lambda+3}$．" "\n"
        r"**第四步：求范围**" "\n"
        r"$e^{2}=\dfrac{\lambda-1}{\lambda+3}=1-\dfrac4{\lambda+3}$，"
        r"在 $\lambda\in[2,3]$ 上单调递增．" "\n"
        r"$\lambda=2$：$e^{2}=\dfrac15$，$e=\dfrac{\sqrt5}5$；" "\n"
        r"$\lambda=3$：$e^{2}=\dfrac26=\dfrac13$，$e=\dfrac{\sqrt3}3$．" "\n"
        r"故 $e\in\left[\dfrac{\sqrt5}5,\ \dfrac{\sqrt3}3\right]$．"
    ),
    'review': (
        r"★ 由详解「因为 $\vec{AF_{1}}\cdot\vec{F_{1}F_{2}}=0$，"
        r"所以可设 $A(-c,\frac{b^{2}}a)$，$F_{2}(c,0)$，$B(x,y)$，"
        r"由 $\vec{AF_{2}}=\lambda\vec{F_{2}B}$，得 $(2c,-\frac{b^{2}}a)=\lambda(x-c,y)$，"
        r"即 $B(\frac{\lambda+2}\lambda c,-\frac{b^{2}}{\lambda a})$，"
        r"因为 $B$ 在椭圆上，所以 $\frac{(1+\frac2\lambda)^{2}c^{2}}{a^{2}}"
        r"+\frac{(-\frac{b^{2}}{\lambda a})^{2}}{b^{2}}=1$，"
        r"即 $(\lambda+2)^{2}c^{2}+b^{2}=\lambda^{2}a^{2}$，"
        r"即 $(\lambda^{2}+4\lambda+3)c^{2}=(\lambda^{2}-1)a^{2}$，"
        r"即 $\frac ca=\frac{\lambda^{2}-1}{\lambda^{2}+4\lambda+3}=\frac{\lambda-1}{\lambda+3}"
        r"=1-\frac4{\lambda+3}$ 在区间 $[2,3]$ 上为增函数」还原。" "\n"
        r"**⚠ 原文笔误（如实标注）**：原文写「$\frac ca=\frac{\lambda-1}{\lambda+3}$」"
        r"并直接得 $e\in[\frac{\sqrt5}5,\frac{\sqrt3}3]$ —— "
        r"但按 $\frac ca=\frac{\lambda-1}{\lambda+3}$，$\lambda=2$ 时应得 $e=\frac15\neq\frac{\sqrt5}5$。" "\n"
        r"**正确应为 $\frac{c^{2}}{a^{2}}=\frac{\lambda-1}{\lambda+3}$**，"
        r"即 $e=\sqrt{\frac{\lambda-1}{\lambda+3}}$：" "\n"
        r"$\lambda=2$：$e^{2}=\frac15$ → $e=\frac1{\sqrt5}=\frac{\sqrt5}5$ ✓" "\n"
        r"$\lambda=3$：$e^{2}=\frac13$ → $e=\frac1{\sqrt3}=\frac{\sqrt3}3$ ✓" "\n"
        r"**与答案完全吻合** ✓ 故按 $e^{2}=\frac{\lambda-1}{\lambda+3}$ 录入。" "\n"
        r"**独立验算**（取 $\lambda=2$ 反查）："
        r"$e=\frac{\sqrt5}5\approx0.4472$，$e^{2}=0.2$。"
        r"取 $a=5$、$c=\sqrt5\approx2.236$、$b^{2}=25-5=20$、$b=2\sqrt5$。" "\n"
        r"$A(-c,\frac{b^{2}}a)=(-2.236, 4)$；"
        r"$B(\frac{4}{2}\cdot2.236, -\frac{20}{2\cdot5})=(4.472,-2)$。" "\n"
        r"验 $B$ 在椭圆上：$\frac{4.472^{2}}{25}+\frac{4}{20}=\frac{20}{25}+0.2=0.8+0.2=1$ ✓ **成立**" "\n"
        r"**结论正确** ✓（仅原文 $\frac ca$ 与 $\frac{c^{2}}{a^{2}}$ 的记号笔误）"
    ),
    'difficulty': 0.93,
    'topics': ['M-T-331'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-331-E1',
}

T331_V1 = {
    'type': '填空',
    'stem_text': (
        r"设双曲线 $C:\dfrac{x^{2}}{a^{2}}-\dfrac{y^{2}}{b^{2}}=1$（$a>0,b>0$）的右焦点为 $F$，"
        r"过 $F$ 且斜率为 $\sqrt3$ 的直线交 $C$ 于 $A$、$B$ 两点，"
        r"若 $\vec{AB}=5\vec{FB}$，则 $C$ 的离心率为 ____ ．"
    ),
    'opts': [],
    'answer': r"$\dfrac65$",
    'analysis': (
        r"由 $\vec{AB}=5\vec{FB}$ 化为 $|AF|=4|FB|$；"
        r"用双曲线的**定义**（焦半径 $=\mathrm e\times$ 到准线距离）与"
        r"$\angle BAD=60^\circ$（斜率为 $\sqrt3$）在直角三角形中解出 $\mathrm e$。"
    ),
    'solution': (
        r"**第一步：转化定比关系**" "\n"
        r"$\vec{AB}=5\vec{FB}$：$B-A=5(B-F)\Rightarrow A=5F-4B$" "\n"
        r"$\Rightarrow A-F=4(F-B)$，即 $F$ 在 $A$、$B$ 之间且 $|AF|=4|FB|$．" "\n"
        r"设 $|FB|=m$，则 $|AF|=4m$、$|AB|=5m$．" "\n"
        r"**第二步：用定义转化到准线距离**" "\n"
        r"过 $A,B$ 分别作准线的垂线，垂足 $A_{1},B_{1}$．"
        r"由双曲线定义 $\dfrac{|AF|}{|AA_{1}|}=\mathrm e$：" "\n"
        r"$|AA_{1}|=\dfrac{4m}{\mathrm e}$，$|BB_{1}|=\dfrac{m}{\mathrm e}$．" "\n"
        r"**第三步：构造直角三角形**" "\n"
        r"过 $B$ 作 $BD\perp AA_{1}$ 于 $D$．因直线斜率为 $\sqrt3$，"
        r"与 $x$ 轴（即准线垂线方向）夹角为 $60^\circ$，故 $\angle BAD=60^\circ$．" "\n"
        r"$|AD|=|AA_{1}|-|BB_{1}|=\dfrac{4m}{\mathrm e}-\dfrac{m}{\mathrm e}=\dfrac{3m}{\mathrm e}$，" "\n"
        r"又 $|AD|=|AB|\cos60^\circ=5m\times\dfrac12=\dfrac{5m}2$．" "\n"
        r"**第四步：解 $\mathrm e$**" "\n"
        r"$\dfrac{3m}{\mathrm e}=\dfrac{5m}2\Rightarrow \mathrm e=\dfrac65$．" "\n"
        r"故答案为 $\dfrac65$．"
    ),
    'review': (
        r"★ 由详解「由 $\vec{AB}=5\vec{FB}$ 可得 $AF=4FB$，设 $|AF|=4m$、$|BF|=m$，"
        r"过 $A,B$ 分别做准线的垂线，垂足为 $A_{1},B_{1}$，由双曲线定义得 "
        r"$|AA_{1}|=\frac{4m}{\mathrm e}$，$|BB_{1}|=\frac m{\mathrm e}$，"
        r"过 $B$ 做 $BD$ 垂直于 $AA_{1}$ 垂足 $D$，"
        r"因为 $AB$ 斜率为 $\sqrt3$，所以在 $\triangle ABD$ 中 $\angle BAD=60^\circ$，"
        r"可得 $|AD|=\frac12|AB|$，"
        r"即 $\frac{4m}{\mathrm e}-\frac m{\mathrm e}=\frac{3m}{\mathrm e}=\frac{5m}2$，"
        r"解得 $\mathrm e=\frac65$」还原。" "\n"
        r"**独立数值验证**（取 $a=5$，则 $\mathrm e=\frac65$ → $c=6$、"
        r"$b^{2}=36-25=11$、$b=\sqrt{11}\approx3.3166$）：" "\n"
        r"右焦点 $F(6,0)$，直线 $y=\sqrt3(x-6)$，代入 $\frac{x^{2}}{25}-\frac{y^{2}}{11}=1$：" "\n"
        r"$\frac{x^{2}}{25}-\frac{3(x-6)^{2}}{11}=1$" "\n"
        r"$11x^{2}-75(x^{2}-12x+36)=275$" "\n"
        r"$-64x^{2}+900x-2700=275\Rightarrow64x^{2}-900x+2975=0$" "\n"
        r"$x=\frac{900\pm\sqrt{810000-761600}}{128}=\frac{900\pm220}{128}$" "\n"
        r"→ $x_{A}=8.75$、$x_{B}=5.3125$（均在右支 ✓）" "\n"
        r"右支焦半径 $|PF|=\mathrm e\cdot x-a=\frac65x-5$：" "\n"
        r"$|AF|=1.2\times8.75-5=10.5-5=5.5$" "\n"
        r"$|BF|=1.2\times5.3125-5=6.375-5=1.375$" "\n"
        r"$\frac{|AF|}{|BF|}=\frac{5.5}{1.375}=4.000$ ✓✓ **恰好等于 4**" "\n"
        r"**答案 $\frac65$ 正确** ✓"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-331'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-331-V1',
}

T331_V2 = {
    'type': '填空',
    'stem_text': (
        r"抛物线 $y^{2}=4x$，直线 $l$ 经过抛物线的焦点 $F$，与抛物线交于 $A$、$B$ 两点，"
        r"若 $\vec{BA}=4\vec{BF}$，则 $\triangle OAB$（$O$ 为坐标原点）的面积为 ____ ．"
    ),
    'opts': [],
    'answer': r"$\dfrac{4\sqrt3}3$",
    'analysis': (
        r"由 $\vec{BA}=4\vec{BF}$ 得 $|BF|:|FA|=1:3$；"
        r"用抛物线参数点 $t$ 与焦点弦条件 $t_{1}t_{2}=-1$ 解出两点纵坐标，"
        r"再用 $S=\frac12|OF|\cdot|y_{A}-y_{B}|$ 求面积。"
    ),
    'solution': (
        r"**第一步：转化定比关系**" "\n"
        r"$\vec{BA}=4\vec{BF}$：$A-B=4(F-B)$，即 $F$ 在 $BA$ 上距 $B$ 为 $\frac14$ 处，" "\n"
        r"故 $|BF|:|FA|=1:3$．" "\n"
        r"**第二步：参数化**" "\n"
        r"$y^{2}=4x$ 即 $a=1$，焦点 $F(1,0)$；设 $A(t_{1}^{2},2t_{1})$、$B(t_{2}^{2},2t_{2})$．" "\n"
        r"焦半径 $|FA|=a(1+t_{1}^{2})=1+t_{1}^{2}$、$|FB|=1+t_{2}^{2}$；"
        r"焦点弦条件 $t_{1}t_{2}=-1$．" "\n"
        r"**第三步：解 $t$**" "\n"
        r"由 $|FA|=3|FB|$：$1+t_{1}^{2}=3(1+t_{2}^{2})$，代 $t_{1}=-\dfrac1{t_{2}}$，" "\n"
        r"设 $u=t_{2}^{2}$：$1+\dfrac1u=3+3u\Rightarrow u+1=3u+3u^{2}$" "\n"
        r"$\Rightarrow3u^{2}+2u-1=0\Rightarrow(3u-1)(u+1)=0\Rightarrow u=\dfrac13$．" "\n"
        r"取 $t_{2}=\dfrac1{\sqrt3}$，则 $t_{1}=-\sqrt3$．" "\n"
        r"**第四步：求面积**" "\n"
        r"$y_{A}=2t_{1}=-2\sqrt3$、$y_{B}=2t_{2}=\dfrac2{\sqrt3}=\dfrac{2\sqrt3}3$，" "\n"
        r"$|y_{A}-y_{B}|=2\sqrt3+\dfrac{2\sqrt3}3=\dfrac{8\sqrt3}3$．" "\n"
        r"因 $O$、$F$ 都在 $x$ 轴上，$|OF|=1$，故以 $OF$ 为底：" "\n"
        r"$S=\dfrac12|OF|\cdot|y_{A}-y_{B}|=\dfrac12\times1\times\dfrac{8\sqrt3}3"
        r"=\dfrac{4\sqrt3}3$．" "\n"
        r"故答案为 $\dfrac{4\sqrt3}3$．"
    ),
    'review': (
        r"★ 由详解「联立可得 $y^{2}-4\sqrt3\,y-12=0$…"
        r"则 $|y_{A}-y_{B}|=\frac{8\sqrt3}3$，"
        r"故 $\triangle OAB$ 的面积 $S=\frac12\times|OF|\times|y_{A}-y_{B}|"
        r"=\frac12\times1\times\frac{8\sqrt3}3=\frac{4\sqrt3}3$」还原。" "\n"
        r"（详解的式子破碎，上述推导为**我独立完成**。）" "\n"
        r"**独立验算**：" "\n"
        r"① $t_{2}^{2}=\frac13$ → $B(\frac13,\frac{2}{\sqrt3})$；$t_{1}=-\sqrt3$ → $A(3,-2\sqrt3)$" "\n"
        r"② 验在抛物线上：$(-2\sqrt3)^{2}=12=4\times3$ ✓；$(\frac{2}{\sqrt3})^{2}=\frac43=4\times\frac13$ ✓" "\n"
        r"③ 验 $A,F,B$ 共线：$F(1,0)$、$B(\frac13,\frac{2}{\sqrt3})$，"
        r"斜率 $=\frac{2/\sqrt3-0}{1/3-1}=\frac{2/\sqrt3}{-2/3}=-\frac3{\sqrt3}=-\sqrt3$；"
        r"$A(3,-2\sqrt3)$：斜率 $=\frac{-2\sqrt3-0}{3-1}=-\sqrt3$ ✓ **三点共线** ✓" "\n"
        r"④ $|BF|=\sqrt{(\frac13-1)^{2}+\frac43}=\sqrt{\frac49+\frac43}=\sqrt{\frac{16}{9}}=\frac43$；"
        r"$|FA|=\sqrt{(3-1)^{2}+12}=\sqrt{16}=4$；$\frac{|FA|}{|BF|}=\frac4{4/3}=3$ ✓" "\n"
        r"⑤ $S=\frac12\times1\times\frac{8\sqrt3}3=\frac{4\sqrt3}3\approx2.309$ ✓" "\n"
        r"**另法验证**（行列式）：$S=\frac12|x_{A}y_{B}-x_{B}y_{A}|"
        r"=\frac12|3\cdot\frac{2\sqrt3}3-\frac13\cdot(-2\sqrt3)|=\frac12|2\sqrt3+\frac{2\sqrt3}3|"
        r"=\frac12\cdot\frac{8\sqrt3}3=\frac{4\sqrt3}3$ ✓ **两法一致**" "\n"
        r"**答案 $\frac{4\sqrt3}3$ 正确** ✓"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-331'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-331-V2',
}

T331_V3 = {
    'type': '选择',
    'stem_text': (
        r"直线过椭圆 $\dfrac{x^{2}}{a^{2}}+\dfrac{y^{2}}{b^{2}}=1$（$a>0,b>0$）的左焦点 $F$ 和"
        r"上顶点 $A$，与圆心在原点的圆交于 $P,Q$ 两点，"
        r"若 $PF=3FQ$，$\angle POQ=120^\circ$，则椭圆离心率为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac12$"),
        ('B', r"$\dfrac{\sqrt3}3$"),
        ('C', r"$\dfrac{\sqrt7}3$"),
        ('D', r"$\dfrac{\sqrt{21}}7$"),
    ],
    'answer': 'D',
    'analysis': (
        r"由 $\angle POQ=120^\circ$ 与垂径定理得 $PM=\sqrt3\,OM$；"
        r"由 $PF=3FQ$ 得 $MF=\frac12PM$；"
        r"再由直角 $\triangle OMF$ 中 $MF=\frac{c^{2}}a$、$OM=\frac{bc}a$ 联立解出 $\mathrm e$。"
    ),
    'solution': (
        r"**第一步：定直线 $FA$**" "\n"
        r"$F(-c,0)$、$A(0,b)$，直线 $FA$：$\dfrac x{-c}+\dfrac yb=1$，"
        r"即 $bx-cy+bc=0$，斜率 $k=\dfrac bc$．" "\n"
        r"**第二步：由 $\angle POQ=120^\circ$ 得 $PM$ 与 $OM$ 的关系**" "\n"
        r"设 $M$ 为 $PQ$ 中点，由垂径定理 $OM\perp PQ$，"
        r"且 $OM$ 平分 $\angle POQ$，故 $\angle POM=60^\circ$、$\angle OPM=30^\circ$．" "\n"
        r"在直角 $\triangle OPM$ 中：$\tan30^\circ=\dfrac{OM}{PM}\Rightarrow PM=\sqrt3\,OM$．" "\n"
        r"**第三步：由 $PF=3FQ$ 得 $MF$**" "\n"
        r"$P,F,Q$ 共线，$M$ 为 $PQ$ 中点．设 $PM=QM=s$，"
        r"$F$ 在 $PQ$ 上且 $PF=3FQ$，可得 $MF=\dfrac s2$（$F$ 到近端为 $\frac{s}2$、" "\n"
        r"到远端为 $\frac{3s}2$，比值为 $3$ ✓）．故 $MF=\dfrac{PM}2=\dfrac{\sqrt3}2OM$．" "\n"
        r"**第四步：用 $\triangle OMF$ 的量联立**" "\n"
        r"在直角 $\triangle OMF$ 中，$OF=c$：" "\n"
        r"$OM=\dfrac{|b\cdot0-c\cdot0+bc|}{\sqrt{b^{2}+c^{2}}}=\dfrac{bc}a$，" "\n"
        r"$MF=\sqrt{OF^{2}-OM^{2}}=\sqrt{c^{2}-\dfrac{b^{2}c^{2}}{a^{2}}}"
        r"=c\sqrt{1-\dfrac{b^{2}}{a^{2}}}=c\cdot\dfrac ca=\dfrac{c^{2}}a$．" "\n"
        r"代入 $MF=\dfrac{\sqrt3}2OM$：" "\n"
        r"$\dfrac{c^{2}}a=\dfrac{\sqrt3}2\cdot\dfrac{bc}a\Rightarrow c=\dfrac{\sqrt3}2b"
        r"\Rightarrow b=\dfrac{2c}{\sqrt3}$．" "\n"
        r"**第五步：求离心率**" "\n"
        r"$a^{2}=b^{2}+c^{2}=\dfrac{4c^{2}}3+c^{2}=\dfrac{7c^{2}}3$，" "\n"
        r"$\mathrm e^{2}=\dfrac{c^{2}}{a^{2}}=\dfrac37$，$\mathrm e=\sqrt{\dfrac37}=\dfrac{\sqrt{21}}7$．" "\n"
        r"故选 D．"
    ),
    'review': (
        r"★ 由详解「∵椭圆的焦点在 $x$ 轴上，∴$a>b>0$，∴$F(-c,0)$、$A(0,b)$，"
        r"故直线 $FA$ 的方程为 $\frac x{-c}+\frac yb=1$，即 $bx-cy+bc=0$，"
        r"直线 $FA$（即 $PQ$）…则 $M$ 为 $PQ$ 的中点，"
        r"∵$\angle POQ=120^\circ$，∴$\angle OPM=30^\circ$，"
        r"…$\frac{OM}{PM}=\tan30^\circ$，…$k=\tan\angle MFO=\frac{OM}{MF}$…"
        r"不妨令 $b=2\sqrt3\,t$、$c=3t$，"
        r"则 $a=\sqrt{b^{2}+c^{2}}=\sqrt{21}\,t$，∴椭圆的离心率 $\mathrm e=\frac ca=\frac{\sqrt{21}}7$」还原。" "\n"
        r"**独立验算**：" "\n"
        r"① $b=\frac{2c}{\sqrt3}$ 与原文 $b=2\sqrt3 t$、$c=3t$ → $\frac bc=\frac{2\sqrt3}3=\frac2{\sqrt3}$ ✓ **一致**" "\n"
        r"② $\mathrm e^{2}=\frac37$ → $\mathrm e=\sqrt{\frac37}=\frac{\sqrt3}{\sqrt7}=\frac{\sqrt{21}}7\approx0.6547$ ✓" "\n"
        r"③ **数值反查**（取 $c=3$、$b=2\sqrt3$、$a=\sqrt{21}\approx4.5826$）：" "\n"
        r"直线 $2\sqrt3x-3y+6\sqrt3=0$；"
        r"$OM=\frac{6\sqrt3}{\sqrt{12+9}}=\frac{6\sqrt3}{\sqrt{21}}=2.2678$ ✓（$=\frac{bc}a$）" "\n"
        r"$MF=\frac{c^{2}}a=\frac9{4.5826}=1.9639$ ✓" "\n"
        r"$PM=\sqrt3\cdot OM=3.9279$；$\frac{MF}{PM}=\frac{1.9639}{3.9279}=0.500$ ✓ **恰为一半**" "\n"
        r"$PF=PM+MF=5.8918$、$FQ=PM-MF=1.9640$；$\frac{PF}{FQ}=\frac{5.8918}{1.9640}=3.000$ ✓✓" "\n"
        r"**答案 D 正确** ✓" "\n"
        r"（注：$P$ 取在 $F$ 的另一侧，此时 $PF=3FQ$ 成立；"
        r"若交换 $P,Q$ 命名则变为 $FQ=3PF$，不影响离心率。）"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-331'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-331-V3',
}

QS = [T331_E1, T331_V1, T331_V2, T331_V3]
