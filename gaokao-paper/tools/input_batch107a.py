# -*- coding: utf-8 -*-
r"""第 107 批：圆锥曲线解答题（M-T-350 四题、M-T-351 三题、M-T-348 两题、M-T-361 一题）

    python3 tools/run_batch.py 107

## 选题依据

按「详解完整 + 同题型聚堆 + 无图依赖 + 可独立数值验算」筛出，本批 10 题全是解答题：
M-T-350 四题是「椭圆中的面积/弦长综合」（p258-259 一带）；
M-T-351 三题是「双曲线与椭圆的定点定值」（p260）；
M-T-348 两题是「椭圆中的定点探究」（p257）；
M-T-361 一题是「双曲线中的角平分型定点」（p271）。

10 题**全部由我独立建系/联立推导一遍**，关键结论都与原书答案数值对拍吻合。

## 第一条：焦点三角形的面积拆法（M-T-350-E1，本批最值钱）

过焦点 $F_2$ 的弦 $MN$，则

$$S_{\triangle F_1MN}=S_{\triangle F_1F_2M}+S_{\triangle F_1F_2N}
=\frac12\left|F_1F_2\right|\cdot\left|y_1\right|+\frac12\left|F_1F_2\right|\cdot\left|y_2\right|$$

因 $F_2$ 在椭圆内，$M,N$ 必在 $x$ 轴两侧，故 $\left|y_1\right|+\left|y_2\right|=\left|y_1-y_2\right|$，于是

$$S=\frac12\left|F_1F_2\right|\cdot\left|y_1-y_2\right|$$

> ⭐⭐ **凡是「过焦点的弦 + 另一个焦点」的三角形，一律拆成两个以 $F_1F_2$ 为底的小三角形**，
> 底相同、高就是 $\left|y\right|$，比用 $|MN|\times d$ 快一个量级。

## 第二条：$S=\dfrac{At}{Bt+C}$ 型的值域用对勾函数（M-T-350-V1 / V3 通用）

M-T-350-V1 得 $S=\dfrac{\sqrt{8t}}{t+4}$（$t=2k^2-3>0$），平方后

$$S^2=\frac{8t}{t^2+8t+16}=\frac8{t+\frac{16}t+8}\le\frac8{8+8}=\frac12$$

> ⭐⭐ **平方后出现 $t+\dfrac pt$，立刻用 $t+\dfrac pt\ge2\sqrt p$**。
> 这一步同时给出最大值和取等条件（$t=\sqrt p$），不必求导。

M-T-350-V3 是同一招的另一面：$S=\dfrac{24t}{3t^2+1}=\dfrac{24}{3t+\frac1t}$，
由 $3t+\dfrac1t$ 在 $[1,+\infty)$ 单调递增直接得 $S\le6$。

> ⚠ **开闭端点必须单独验**：M-T-350-E1 的 $S=3$ 只在「$l\perp x$ 轴」时取到，
> 而斜率存在那支只有 $S<3$ —— 漏掉竖直情形就会错写成 $(0,3)$。

## 第三条：$\vec{F_1M}=\vec{F_1A}+\vec{F_1B}$ ⟹ 平行四边形（M-T-350-V2）

向量等式说明 $AMBF_1$ 是以 $F_1A,F_1B$ 为邻边的平行四边形，于是

$$S_{AMBF_1}=2S_{\triangle ABF_1}=\left|F_1F_2\right|\cdot\left|y_1-y_2\right|$$

> ⭐⭐ 见到 $\vec{OP}=\vec{OA}+\vec{OB}$ 形式的条件，第一反应就是**平行四边形**，
> 面积立刻翻倍，省掉一次底高计算。

## 第四条：「以 $PQ$ 为直径的圆过定点」的向量翻译（M-T-348-E1）

设定点 $N\left(x_0,0\right)$，则 $\vec{PN}\cdot\vec{QN}=0$，即

$$x_0^2+\frac{4y_1y_2}{\left(x_1-2\right)\left(x_2-2\right)}=0$$

分子分母**都用韦达表示**后，$k$ 恰好约干净，只剩 $x_0^2-3=0$。

> ⭐⭐ 圆过定点的题一律走「设点 → 数量积为零 → 韦达代入 → 参数消失」四步。
> 若参数没消干净，说明定点设错了位置。

## 第五条：斜率之积为定值（M-T-348-V2）

椭圆 $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$ 上任意点 $P$（非左右顶点）与两顶点连线的斜率积恒为 $-\dfrac{b^2}{a^2}$：

$$k_{PA}k_{PB}=\frac{n^2}{m^2-a^2}=\frac{b^2\left(1-\frac{m^2}{a^2}\right)}{m^2-a^2}=-\frac{b^2}{a^2}$$

## 第六条：$m^2$ 项恒为零是「存在定点」的判据（M-T-348-V2）

代入韦达后整理成 $\left(\cdots\right)m^2+\left(\cdots\right)=0$，其中 $m^2$ 的系数**恒为 $0$**
（与 $t$ 无关），于是只需令常数项为零，解出 $t=-\dfrac{\sqrt3}5$（另一根 $t=-\sqrt3$ 舍去）。

> ⭐⭐ 这类「对任意 $m$ 恒成立」的题，先分离 $m$ 的幂次，系数分别令零。

## 三处原书题干破碎，已还原（判据写在各题 review 里）

1. **M-T-350-V1 题干缺前置条件**（只剩两个小问），由详解「设 $F\left(c,0\right)$，则知 $c=1$，
   离心率 $e=\frac ca=\frac{\sqrt2}2$」反推补全。
2. **M-T-350-V2 题干缺前置条件**，其原文恰好残留在 V1 详解末尾：
   「已知点 $F_1,F_2$ 是椭圆 $C$ 的左、右焦点……当 $\angle PF_1F_2=\frac\pi3$ 时，
   $\triangle PF_1F_2$ 面积达到最大」——与详解的 $bc=\sqrt3,\ b=\sqrt3c$ 完全吻合。
3. **M-T-350-E1 的「圆上某一点 $A$ 刚好与 $A$ 点重合」** 是 $A^{\prime}$ 丢撇号所致，
   已还原为「圆上动点 $A^{\prime}$ 与定点 $A$ 重合」。
"""

T350_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知一张纸上画有半径为 $4$ 的圆 $O$，在圆 $O$ 内有一个定点 $A$，且 $OA=2$，"
        r"折叠纸片，使圆上某一点 $A^{\prime}$ 刚好与 $A$ 点重合，这样的每一种折法，"
        r"都留下一条直线折痕，当 $A^{\prime}$ 取遍圆上所有点时，所有折痕与 $OA$ 的交点"
        r"形成的曲线记为 $C$．" "\n"
        r"（1）求曲线 $C$ 的焦点在 $x$ 轴上的标准方程；" "\n"
        r"（2）过曲线 $C$ 的右焦点 $F_2$（左焦点为 $F_1$）的直线 $l$ 与曲线 $C$ 交于"
        r"不同的两点 $M,N$，记 $\triangle F_1MN$ 的面积为 $S$，试求 $S$ 的取值范围．"
    ),
    'stem': [
        r"已知一张纸上画有半径为 $4$ 的圆 $O$，在圆 $O$ 内有一个定点 $A$，且 $OA=2$，"
        r"折叠纸片，使圆上某一点 $A^{\prime}$ 刚好与 $A$ 点重合，这样的每一种折法，"
        r"都留下一条直线折痕，当 $A^{\prime}$ 取遍圆上所有点时，所有折痕与 $OA$ 的交点"
        r"形成的曲线记为 $C$．",
        r"（1）求曲线 $C$ 的焦点在 $x$ 轴上的标准方程；",
        r"（2）过曲线 $C$ 的右焦点 $F_2$（左焦点为 $F_1$）的直线 $l$ 与曲线 $C$ 交于"
        r"不同的两点 $M,N$，记 $\triangle F_1MN$ 的面积为 $S$，试求 $S$ 的取值范围．",
    ],
    'opts': [],
    'answer': r"（1）$\dfrac{x^2}{4}+\dfrac{y^2}{3}=1$；（2）$\left(0,3\right]$．",
    'solution': (
        r"**第（1）问**" "\n"
        r"以 $OA$ 中点 $G$ 为坐标原点、$OA$ 所在直线为 $x$ 轴建立平面直角坐标系，"
        r"则 $O\left(-1,0\right)$，$A\left(1,0\right)$．" "\n"
        r"设折痕与 $OA$、$AA^{\prime}$ 分别交于 $M$、$N$ 两点，则折痕 $MN$ 垂直平分 $AA^{\prime}$，" "\n"
        r"故 $\left|MA\right|=\left|MA^{\prime}\right|$．又 $A^{\prime}$ 在圆 $O$ 上，$\left|OA^{\prime}\right|=4$，于是" "\n"
        r"$$\left|MO\right|+\left|MA\right|=\left|MO\right|+\left|MA^{\prime}\right|=\left|OA^{\prime}\right|=4>2=\left|OA\right|,$$" "\n"
        r"所以 $M$ 的轨迹是以 $O,A$ 为焦点、长轴长 $2a=4$ 的椭圆．" "\n"
        r"由 $2c=\left|OA\right|=2$ 得 $c=1$，$a=2$，$b^2=a^2-c^2=3$，故" "\n"
        r"$$C:\ \frac{x^2}{4}+\frac{y^2}{3}=1.$$" "\n"
        r"**第（2）问**" "\n"
        r"由（1）知 $F_1\left(-1,0\right)$，$F_2\left(1,0\right)$，$\left|F_1F_2\right|=2$．" "\n"
        r"① 当 $l\perp x$ 轴时，$l:x=1$，代入椭圆得 $y=\pm\dfrac32$，故 $\left|MN\right|=3$，" "\n"
        r"$$S=\frac12\left|MN\right|\cdot\left|F_1F_2\right|=\frac12\times3\times2=3.$$" "\n"
        r"② 当 $l$ 与 $x$ 轴不垂直时，设 $l:y=k\left(x-1\right)\ \left(k\neq0\right)$，代入 $3x^2+4y^2=12$：" "\n"
        r"$$\left(4k^2+3\right)y^2+6ky-9k^2=0,$$" "\n"
        r"$$y_1+y_2=-\frac{6k}{4k^2+3},\qquad y_1y_2=-\frac{9k^2}{4k^2+3}.$$" "\n"
        r"因 $F_2$ 在椭圆内，$M,N$ 分居 $x$ 轴两侧，故" "\n"
        r"$$S=S_{\triangle F_1F_2M}+S_{\triangle F_1F_2N}=\frac12\left|F_1F_2\right|\left(\left|y_1\right|+\left|y_2\right|\right)"
r"=\left|y_1-y_2\right|$$" "\n"
        r"$$=\sqrt{\left(y_1+y_2\right)^2-4y_1y_2}=\frac{12\sqrt{k^2\left(k^2+1\right)}}{4k^2+3}.$$" "\n"
        r"令 $t=4k^2+3>3$，则 $k^2=\dfrac{t-3}4$，$k^2+1=\dfrac{t+1}4$，于是" "\n"
        r"$$S=\frac{3\sqrt{t^2-2t-3}}{t}=3\sqrt{1-\frac2t-\frac3{t^2}}.$$" "\n"
        r"由 $t>3$ 得 $0<\dfrac1t<\dfrac13$，而 $-3u^2-2u+1$ 在 $u\in\left(0,\dfrac13\right)$ 上的值域为 $\left(0,1\right)$，" "\n"
        r"故 $0<S<3$．" "\n"
        r"综上，$S$ 的取值范围是 $\left(0,3\right]$．"
    ),
    'analysis': (
        r"（1）折痕是 $AA^{\prime}$ 的垂直平分线，由此把 $\left|MA\right|$ 换成 $\left|MA^{\prime}\right|$，"
        r"再用 $\left|MO\right|+\left|MA^{\prime}\right|=\left|OA^{\prime}\right|=4$ 凑出椭圆定义；"
        r"（2）把 $\triangle F_1MN$ 拆成两个以 $F_1F_2$ 为底的小三角形，面积化为 $\left|y_1-y_2\right|$，"
        r"用韦达定理表示后换元 $t=4k^2+3$ 求值域，最后补上斜率不存在时的 $S=3$．"
    ),
    'review': (
        r"① ⭐ **题干是 $A^{\prime}$ 与 $A$ 重合**：原文「使圆上某一点 $A$ 刚好与 $A$ 点重合」"
        r"是 $A^{\prime}$ 丢撇号所致，已还原为圆上动点 $A^{\prime}$ 与定点 $A$ 重合，否则逻辑不通．" "\n"
        r"② ⭐⭐ **焦点三角形拆成两个小三角形**（本批最值钱）：" "\n"
        r"$$S_{\triangle F_1MN}=S_{\triangle F_1F_2M}+S_{\triangle F_1F_2N}"
r"=\frac12\left|F_1F_2\right|\cdot\left|y_1-y_2\right|$$" "\n"
        r"   关键点是 $F_2$ 在椭圆内 ⟹ $y_1,y_2$ 异号 ⟹ $\left|y_1\right|+\left|y_2\right|=\left|y_1-y_2\right|$．" "\n"
        r"   凡是「过焦点的弦 + 另一焦点」的面积题，一律这么拆，比 $\frac12\left|MN\right|d$ 快得多．" "\n"
        r"③ **开闭端点**：斜率存在那支只有 $0<S<3$，上界 $3$ 只在 $l\perp x$ 轴时取到，"
        r"所以是 $\left(0,3\right]$ 而不是 $\left(0,3\right)$．漏掉竖直情形是本题最大陷阱．" "\n"
        r"④ **数值复核**：$k=1$ 时 $S=\dfrac{12\sqrt2}{7}=2.4242<3$ ✓；$k\to0$ 时 $S\to0$ ✓；"
        r"$x=1$ 时 $\left|MN\right|=3$、$S=3$ ✓．" "\n"
        r"⑤ 换元后 $S=3\sqrt{1-\frac2t-\frac3{t^2}}$，令 $u=\frac1t\in\left(0,\frac13\right)$，"
        r"$-3u^2-2u+1$ 从 $1$ 单调降到 $0$，故 $S$ 从 $3$ 单调降到 $0$ —— 单调性一目了然．"
    ),
    'difficulty': 0.72,
    'topics': ['M-T-350'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-350-E1',
}

T350_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知椭圆 $C:\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1\left(a>b>0\right)$ 的右焦点为 $F\left(1,0\right)$，"
        r"离心率为 $\dfrac{\sqrt2}2$．" "\n"
        r"（1）求椭圆 $C$ 的方程；" "\n"
        r"（2）若 $O$ 为坐标原点，过点 $M\left(0,2\right)$ 作直线 $l$ 交椭圆 $C$ 于 $A,B$ 两点，"
        r"求 $\triangle AOB$ 面积的最大值．"
    ),
    'stem': [
        r"已知椭圆 $C:\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1\left(a>b>0\right)$ 的右焦点为 $F\left(1,0\right)$，"
        r"离心率为 $\dfrac{\sqrt2}2$．",
        r"（1）求椭圆 $C$ 的方程；",
        r"（2）若 $O$ 为坐标原点，过点 $M\left(0,2\right)$ 作直线 $l$ 交椭圆 $C$ 于 $A,B$ 两点，"
        r"求 $\triangle AOB$ 面积的最大值．",
    ],
    'opts': [],
    'answer': r"（1）$\dfrac{x^2}{2}+y^2=1$；（2）$\dfrac{\sqrt2}2$．",
    'solution': (
        r"**第（1）问**" "\n"
        r"由右焦点 $F\left(1,0\right)$ 得 $c=1$，又 $e=\dfrac ca=\dfrac{\sqrt2}2$，故 $a=\sqrt2c=\sqrt2$，" "\n"
        r"$b^2=a^2-c^2=2-1=1$，所以椭圆 $C$ 的方程为" "\n"
        r"$$\frac{x^2}{2}+y^2=1.$$" "\n"
        r"**第（2）问**" "\n"
        r"设 $A\left(x_1,y_1\right)$，$B\left(x_2,y_2\right)$，直线 $l:y=kx+2$，代入 $x^2+2y^2=2$：" "\n"
        r"$$\left(1+2k^2\right)x^2+8kx+6=0,$$" "\n"
        r"由 $\Delta=64k^2-24\left(1+2k^2\right)=16k^2-24>0$ 得 $k^2>\dfrac32$，" "\n"
        r"$$x_1+x_2=-\frac{8k}{1+2k^2},\qquad x_1x_2=\frac6{1+2k^2}.$$" "\n"
        r"原点 $O$ 到直线 $l$ 的距离 $d=\dfrac{2}{\sqrt{1+k^2}}$，" "\n"
        r"$$\left|AB\right|=\sqrt{1+k^2}\cdot\left|x_1-x_2\right|,$$" "\n"
        r"故" "\n"
        r"$$S_{\triangle AOB}=\frac12\left|AB\right|\cdot d=\left|x_1-x_2\right|"
r"=\sqrt{\left(x_1+x_2\right)^2-4x_1x_2}=\frac{\sqrt{8\left(2k^2-3\right)}}{2k^2+1}.$$" "\n"
        r"令 $t=2k^2-3>0$，则 $2k^2+1=t+4$，于是" "\n"
        r"$$S^2=\frac{8t}{\left(t+4\right)^2}=\frac8{t+\dfrac{16}t+8}\le\frac8{8+8}=\frac12,$$" "\n"
        r"等号当且仅当 $t=4$（即 $k^2=\dfrac72$）时成立．" "\n"
        r"所以 $\triangle AOB$ 面积的最大值为 $\dfrac{\sqrt2}2$．"
    ),
    'analysis': (
        r"（1）由焦点坐标定 $c$、由离心率定 $a$，再用 $a^2=b^2+c^2$ 求 $b$；"
        r"（2）设 $l:y=kx+2$ 联立后用韦达定理表示 $\left|AB\right|$，配上原点到直线的距离 $d$ 得面积，"
        r"换元 $t=2k^2-3$ 后分母出现 $t+\dfrac{16}t$，用基本不等式求最大值．"
    ),
    'review': (
        r"① ⚠ **题干前置条件缺失，已还原**：原文只剩两问，前置条件由详解"
        r"「设 $F\left(c,0\right)$，则知 $c=1$，离心率 $e=\frac ca=\frac{\sqrt2}2$」反推补全为"
        r"「右焦点 $F\left(1,0\right)$，离心率 $\frac{\sqrt2}2$」．补完全链条闭合：$a=\sqrt2,b=1$ ✓" "\n"
        r"② ⭐⭐ **$S=\frac12\left|AB\right|\cdot d$ 里的 $\sqrt{1+k^2}$ 恰好约掉**：" "\n"
        r"$$S=\frac12\cdot\sqrt{1+k^2}\left|x_1-x_2\right|\cdot\frac2{\sqrt{1+k^2}}=\left|x_1-x_2\right|$$" "\n"
        r"   凡是「过 $y$ 轴上定点 $\left(0,m\right)$」的弦，用 $d=\frac{\left|m\right|}{\sqrt{1+k^2}}$ 都会发生这个约简．" "\n"
        r"③ ⭐⭐ **平方后用对勾函数**：$S^2=\dfrac{8t}{t^2+8t+16}=\dfrac8{t+\frac{16}t+8}$，" "\n"
        r"   由 $t+\dfrac{16}t\ge8$ 一步得 $S^2\le\dfrac12$．比求导快，且取等条件 $t=4$ 顺手给出．" "\n"
        r"④ **数值复核**：$k^2=\dfrac72$ 时 $t=4$，$S^2=\dfrac{32}{64}=0.5$，$S=0.7071=\dfrac{\sqrt2}2$ ✓" "\n"
        r"⑤ 注意 $k^2>\dfrac32$ 是判别式给出的**存在条件**，换元 $t=2k^2-3>0$ 正好与之等价．"
    ),
    'difficulty': 0.70,
    'topics': ['M-T-350'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-350-V1',
}

T350_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知点 $F_1,F_2$ 是椭圆 $C:\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1\left(a>b>0\right)$ 的左、右焦点，"
        r"点 $P$ 在椭圆上，当 $\angle PF_1F_2=\dfrac\pi3$ 时，$\triangle PF_1F_2$ 面积达到最大，"
        r"且最大值为 $\sqrt3$．" "\n"
        r"（1）求椭圆 $C$ 的标准方程；" "\n"
        r"（2）过 $F_2$ 的直线与椭圆 $C$ 交于 $A,B$ 两点，且两点与左右顶点不重合，"
        r"若 $\overrightarrow{F_1M}=\overrightarrow{F_1A}+\overrightarrow{F_1B}$，"
        r"求四边形 $AMBF_1$ 面积的取值范围．"
    ),
    'stem': [
        r"已知点 $F_1,F_2$ 是椭圆 $C:\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1\left(a>b>0\right)$ 的左、右焦点，"
        r"点 $P$ 在椭圆上，当 $\angle PF_1F_2=\dfrac\pi3$ 时，$\triangle PF_1F_2$ 面积达到最大，"
        r"且最大值为 $\sqrt3$．",
        r"（1）求椭圆 $C$ 的标准方程；",
        r"（2）过 $F_2$ 的直线与椭圆 $C$ 交于 $A,B$ 两点，且两点与左右顶点不重合，"
        r"若 $\overrightarrow{F_1M}=\overrightarrow{F_1A}+\overrightarrow{F_1B}$，"
        r"求四边形 $AMBF_1$ 面积的取值范围．",
    ],
    'opts': [],
    'answer': r"（1）$\dfrac{x^2}{4}+\dfrac{y^2}{3}=1$；（2）$\left(0,6\right]$．",
    'solution': (
        r"**第（1）问**" "\n"
        r"$S_{\triangle PF_1F_2}=\dfrac12\left|F_1F_2\right|\cdot\left|y_P\right|=c\left|y_P\right|\le cb$，"
        r"当 $P$ 为短轴端点时取等号，此时 $\left|PF_1\right|=\left|PF_2\right|=a$，$\left|F_1F_2\right|=2c$．" "\n"
        r"由 $\angle PF_1F_2=\dfrac\pi3$ 且 $\triangle PF_1F_2$ 为等腰三角形知它为正三角形，故 $a=2c$．" "\n"
        r"又 $a^2=b^2+c^2$，得 $b^2=3c^2$，即 $b=\sqrt3c$．由 $S_{\max}=bc=\sqrt3c^2=\sqrt3$ 得 $c=1$，" "\n"
        r"于是 $a=2$，$b=\sqrt3$，椭圆 $C$ 的标准方程为" "\n"
        r"$$\frac{x^2}{4}+\frac{y^2}{3}=1.$$" "\n"
        r"**第（2）问**" "\n"
        r"由 $\overrightarrow{F_1M}=\overrightarrow{F_1A}+\overrightarrow{F_1B}$ 知四边形 $AMBF_1$ 是平行四边形，" "\n"
        r"故 $S_{AMBF_1}=2S_{\triangle ABF_1}$．" "\n"
        r"设 $A\left(x_1,y_1\right)$，$B\left(x_2,y_2\right)$，$AB:x=my+1$，代入 $3x^2+4y^2=12$：" "\n"
        r"$$\left(3m^2+4\right)y^2+6my-9=0,\qquad \Delta=144\left(m^2+1\right)>0,$$" "\n"
        r"$$y_1+y_2=-\frac{6m}{3m^2+4},\qquad y_1y_2=-\frac9{3m^2+4}.$$" "\n"
        r"于是" "\n"
        r"$$S=2\cdot\frac12\left|F_1F_2\right|\cdot\left|y_1-y_2\right|=2\left|y_1-y_2\right|"
r"=2\cdot\frac{12\sqrt{m^2+1}}{3m^2+4}=\frac{24\sqrt{m^2+1}}{3m^2+4}.$$" "\n"
        r"令 $t=\sqrt{m^2+1}\ge1$，则 $m^2=t^2-1$，$3m^2+4=3t^2+1$，" "\n"
        r"$$S=\frac{24t}{3t^2+1}=\frac{24}{3t+\dfrac1t}.$$" "\n"
        r"函数 $3t+\dfrac1t$ 在 $\left[1,+\infty\right)$ 上单调递增，最小值为 $3+1=4$，故 $S\le\dfrac{24}4=6$，" "\n"
        r"等号当 $m=0$（即 $AB\perp x$ 轴）时成立；当 $\left|m\right|\to+\infty$ 时 $S\to0$ 但取不到" "\n"
        r"（此时 $A,B$ 趋于左右顶点，与题设不重合矛盾）．" "\n"
        r"所以四边形 $AMBF_1$ 面积的取值范围是 $\left(0,6\right]$．"
    ),
    'analysis': (
        r"（1）由面积公式 $S=c\left|y_P\right|\le cb$ 知最大时 $P$ 在短轴端点，再由 $\angle PF_1F_2=\frac\pi3$"
        r"推出正三角形得 $a=2c$，联立 $S_{\max}=bc=\sqrt3$ 解出 $a,b,c$；"
        r"（2）由向量等式识别平行四边形把面积翻倍，设 $x=my+1$ 联立后用韦达表示 $\left|y_1-y_2\right|$，"
        r"换元 $t=\sqrt{m^2+1}$ 后分母化为 $3t+\frac1t$，用单调性求值域．"
    ),
    'review': (
        r"① ⚠ **题干前置条件缺失，已还原**：原文只剩两问．其原始题干恰好残留在上一题（V1）详解末尾——"
        r"「已知点 $F_1,F_2$ 是椭圆 $C$ 的左、右焦点，点 $P$ 在椭圆上，当 $\angle PF_1F_2=\frac\pi3$ 时，"
        r"$\triangle PF_1F_2$ 面积达到最大」．与详解的 $bc=\sqrt3,\ b=\sqrt3c$ 完全吻合 ✓" "\n"
        r"② ⭐⭐ **$\vec{F_1M}=\vec{F_1A}+\vec{F_1B}$ ⟹ 平行四边形**：面积直接翻倍，" "\n"
        r"$$S_{AMBF_1}=2S_{\triangle ABF_1}=\left|F_1F_2\right|\cdot\left|y_1-y_2\right|=2\left|y_1-y_2\right|.$$" "\n"
        r"   以后见到 $\vec{OP}=\vec{OA}+\vec{OB}$，第一反应就是平行四边形．" "\n"
        r"③ ⭐⭐ **设 $x=my+1$ 而不是 $y=k\left(x-1\right)$**：过 $x$ 轴上定点 $\left(1,0\right)$ 的直线，"
        r"用 $x=my+1$ 可以**自动包含斜率不存在的情形**（$m=0$），而 $y=k\left(x-1\right)$ 会漏掉它——"
        r"本题最大值 $6$ 恰在 $m=0$ 处取到，漏了就得不到上界．" "\n"
        r"④ **数值复核**：$m=0$ 时 $AB:x=1$，$A\left(1,\frac32\right),B\left(1,-\frac32\right)$，"
        r"$\left|y_1-y_2\right|=3$，$S=6$ ✓；$m=1$ 时 $S=\dfrac{24\sqrt2}{7}=4.8497<6$ ✓．" "\n"
        r"⑤ 下界 $0$ 取不到：直线趋于 $x$ 轴时 $A,B$ 趋于左右顶点，与题设「与左右顶点不重合」冲突．"
    ),
    'difficulty': 0.75,
    'topics': ['M-T-350'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-350-V2',
}

T350_V3 = {
    'type': '解答',
    'stem_text': (
        r"已知椭圆 $C_1:\dfrac{y^2}{a^2}+\dfrac{x^2}{b^2}=1\left(a>b>0\right)$ 的长轴长为 $4$，"
        r"离心率为 $\dfrac12$，一动圆 $C_2$ 过椭圆 $C_1$ 上焦点 $F$，且与直线 $y=-1$ 相切．" "\n"
        r"（1）求椭圆 $C_1$ 的方程及动圆圆心轨迹 $C_2$ 的方程；" "\n"
        r"（2）过 $F$ 作两条互相垂直的直线 $l_1,l_2$，其中 $l_1$ 交椭圆 $C_1$ 于 $P,Q$ 两点，"
        r"$l_2$ 交曲线 $C_2$ 于 $M,N$ 两点，求四边形 $PMQN$ 面积的最小值．"
    ),
    'stem': [
        r"已知椭圆 $C_1:\dfrac{y^2}{a^2}+\dfrac{x^2}{b^2}=1\left(a>b>0\right)$ 的长轴长为 $4$，"
        r"离心率为 $\dfrac12$，一动圆 $C_2$ 过椭圆 $C_1$ 上焦点 $F$，且与直线 $y=-1$ 相切．",
        r"（1）求椭圆 $C_1$ 的方程及动圆圆心轨迹 $C_2$ 的方程；",
        r"（2）过 $F$ 作两条互相垂直的直线 $l_1,l_2$，其中 $l_1$ 交椭圆 $C_1$ 于 $P,Q$ 两点，"
        r"$l_2$ 交曲线 $C_2$ 于 $M,N$ 两点，求四边形 $PMQN$ 面积的最小值．",
    ],
    'opts': [],
    'answer': r"（1）$C_1:\dfrac{y^2}{4}+\dfrac{x^2}{3}=1$，$C_2:x^2=4y$；（2）$8$．",
    'solution': (
        r"**第（1）问**" "\n"
        r"由 $2a=4$ 得 $a=2$，由 $e=\dfrac ca=\dfrac12$ 得 $c=1$，故 $b^2=a^2-c^2=3$，" "\n"
        r"$$C_1:\ \frac{y^2}{4}+\frac{x^2}{3}=1,\qquad F\left(0,1\right).$$" "\n"
        r"设动圆圆心为 $\left(x,y\right)$．圆过 $F\left(0,1\right)$ 且与 $y=-1$ 相切，"
        r"故圆心到 $F$ 的距离等于到直线 $y=-1$ 的距离，即圆心轨迹是以 $F\left(0,1\right)$ 为焦点、"
        r"$y=-1$ 为准线的抛物线：" "\n"
        r"$$C_2:\ x^2=4y.$$" "\n"
        r"**第（2）问**" "\n"
        r"① 当 $l_1$ 斜率不存在时，$l_1:x=0$，此时 $\left|PQ\right|=4$；$l_2:y=1$，"
        r"由 $x^2=4$ 得 $M\left(-2,1\right),N\left(2,1\right)$，$\left|MN\right|=4$．" "\n"
        r"$$S=\frac12\left|PQ\right|\cdot\left|MN\right|=\frac12\times4\times4=8.$$" "\n"
        r"② 当斜率存在且不为 $0$ 时，设 $l_1:y=kx+1$，则 $l_2:y=-\dfrac1kx+1$．" "\n"
        r"联立 $l_1$ 与 $3y^2+4x^2=12$：$\left(3k^2+4\right)x^2+6kx-9=0$，" "\n"
        r"$$\left|PQ\right|=\sqrt{1+k^2}\cdot\left|x_1-x_2\right|=\frac{12\left(1+k^2\right)}{3k^2+4}.$$" "\n"
        r"联立 $l_2$ 与 $x^2=4y$：由 $x=k\left(1-y\right)$ 得 $k^2y^2-\left(2k^2+4\right)y+k^2=0$，" "\n"
        r"$$y_3+y_4=\frac{2k^2+4}{k^2},$$" "\n"
        r"由抛物线定义 $\left|MN\right|=\left|MF\right|+\left|NF\right|=y_3+y_4+2=4+\dfrac4{k^2}$．" "\n"
        r"于是（对角线互相垂直）" "\n"
        r"$$S=\frac12\left|PQ\right|\cdot\left|MN\right|"
r"=\frac12\cdot\frac{12\left(1+k^2\right)}{3k^2+4}\cdot\frac{4\left(k^2+1\right)}{k^2}"
r"=\frac{24\left(1+k^2\right)^2}{k^2\left(3k^2+4\right)}.$$" "\n"
        r"令 $t=1+k^2>1$，则 $k^2=t-1$，$3k^2+4=3t+1$，" "\n"
        r"$$S=\frac{24t^2}{\left(t-1\right)\left(3t+1\right)}=\frac{24t^2}{3t^2-2t-1}"
r"=\frac{24}{3-\dfrac2t-\dfrac1{t^2}}.$$" "\n"
        r"设 $u=\dfrac1t\in\left(0,1\right)$，则 $3-2u-u^2=4-\left(1+u\right)^2\in\left(0,3\right)$，故 $S>8$．" "\n"
        r"综上，$S\ge8$，四边形 $PMQN$ 面积的最小值为 $8$．"
    ),
    'analysis': (
        r"（1）用长轴长、离心率定 $a,c$，再得 $b$；动圆过定点且与定直线相切，圆心轨迹即抛物线，"
        r"焦点为 $F$、准线为 $y=-1$；（2）对角线互相垂直的四边形面积等于对角线乘积的一半，"
        r"分别用弦长公式与抛物线定义求出 $\left|PQ\right|$、$\left|MN\right|$，换元 $t=1+k^2$ 后求最小值．"
    ),
    'review': (
        r"① ⭐⭐ **对角线垂直的四边形面积 $=\dfrac12 d_1d_2$**：本题 $PQ\perp MN$，"
        r"不必判断四边形形状，直接用这个公式．" "\n"
        r"② ⭐⭐ **$\left|MN\right|$ 用抛物线定义求最快**：$\left|MN\right|=\left|MF\right|+\left|NF\right|=y_3+y_4+2$，"
        r"比弦长公式省一半计算（焦半径 $=y+1$ 是抛物线的固定结论）．" "\n"
        r"③ ⚠ **原书联立方程有两处 OCR 漏字**（我已验算更正）：" "\n"
        r"   · $l_1$ 与椭圆联立应为 $\left(3k^2+4\right)x^2+6k\,x-9=0$（原文写成 $6x$，漏了 $k$）；" "\n"
        r"   · $l_2$ 与抛物线联立应为 $k^2y^2-\left(2k^2+4\right)y+k^2=0$（原文漏了首项系数 $k^2$）．" "\n"
        r"   两处漏字不影响最终表达式，但照抄会导致中间步骤对不上．" "\n"
        r"④ **数值复核**：$k=1$ 时 $\left|PQ\right|=\dfrac{24}{7}=3.4286$，$\left|MN\right|=8$，$S=13.714>8$ ✓；" "\n"
        r"   $k\to\infty$ 时 $t\to\infty$，$S\to\dfrac{24}3=8$ ✓ 与竖直情形一致．" "\n"
        r"⑤ 最小值 $8$ 恰在 $l_1\perp x$ 轴（$k$ 不存在）时取到，与①吻合——"
        r"**这类题的最小值常常落在「斜率不存在」的特殊位置**，别只盯着 $k$ 存在的那支．"
    ),
    'difficulty': 0.78,
    'topics': ['M-T-350'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-350-V3',
}

T351_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知双曲线 $C$ 的中心在原点，$D\left(1,0\right)$ 是它的一个顶点，"
        r"$\vec d=\left(1,\sqrt2\right)$ 是它的一条渐近线的一个方向向量．" "\n"
        r"（1）求双曲线 $C$ 的方程；" "\n"
        r"（2）设 $P\left(0,1\right)$，$M$ 为双曲线右支上动点，当 $\left|PM\right|$ 取得最小时，"
        r"求四边形 $ODMP$ 的面积；" "\n"
        r"（3）若过点 $\left(-3,0\right)$ 任意作一条直线与双曲线 $C$ 交于 $A,B$ 两点"
        r"（$A,B$ 都不同于点 $D$），求证：$\overrightarrow{DA}\cdot\overrightarrow{DB}$ 为定值．"
    ),
    'stem': [
        r"已知双曲线 $C$ 的中心在原点，$D\left(1,0\right)$ 是它的一个顶点，"
        r"$\vec d=\left(1,\sqrt2\right)$ 是它的一条渐近线的一个方向向量．",
        r"（1）求双曲线 $C$ 的方程；",
        r"（2）设 $P\left(0,1\right)$，$M$ 为双曲线右支上动点，当 $\left|PM\right|$ 取得最小时，"
        r"求四边形 $ODMP$ 的面积；",
        r"（3）若过点 $\left(-3,0\right)$ 任意作一条直线与双曲线 $C$ 交于 $A,B$ 两点"
        r"（$A,B$ 都不同于点 $D$），求证：$\overrightarrow{DA}\cdot\overrightarrow{DB}$ 为定值．",
    ],
    'opts': [],
    'answer': r"（1）$x^2-\dfrac{y^2}2=1$；（2）$\dfrac{\sqrt{11}+2}6$；（3）定值为 $0$．",
    'solution': (
        r"**第（1）问**" "\n"
        r"由顶点 $D\left(1,0\right)$ 设 $C:\ x^2-\dfrac{y^2}{b^2}=1\ \left(b>0\right)$，渐近线为 $y=\pm bx$．" "\n"
        r"$\vec d=\left(1,\sqrt2\right)$ 是渐近线 $y=bx$ 的方向向量，故 $b=\sqrt2$，" "\n"
        r"$$C:\ x^2-\frac{y^2}2=1.$$" "\n"
        r"**第（2）问**" "\n"
        r"设 $M\left(x_0,y_0\right)\ \left(x_0\ge1\right)$，则 $x_0^2=1+\dfrac{y_0^2}2$，于是" "\n"
        r"$$\left|PM\right|^2=x_0^2+\left(y_0-1\right)^2=1+\frac{y_0^2}2+y_0^2-2y_0+1"
r"=\frac32y_0^2-2y_0+2=\frac32\left(y_0-\frac23\right)^2+\frac43.$$" "\n"
        r"当 $y_0=\dfrac23$ 时 $\left|PM\right|_{\min}=\dfrac{2\sqrt3}3$，此时 $x_0=\sqrt{1+\dfrac29}=\dfrac{\sqrt{11}}3$，"
        r"即 $M\left(\dfrac{\sqrt{11}}3,\dfrac23\right)$．" "\n"
        r"直线 $DP:\ x+y-1=0$，$\left|DP\right|=\sqrt2$，$M$ 到 $DP$ 的距离" "\n"
        r"$$d=\frac{\left|\dfrac{\sqrt{11}}3+\dfrac23-1\right|}{\sqrt2}=\frac{\sqrt{11}-1}{3\sqrt2}.$$" "\n"
        r"$$S_{ODMP}=S_{\triangle ODP}+S_{\triangle MDP}"
r"=\frac12\left|OD\right|\cdot\left|OP\right|+\frac12\left|DP\right|\cdot d"
r"=\frac12+\frac{\sqrt{11}-1}{6}=\frac{\sqrt{11}+2}6.$$" "\n"
        r"**第（3）问**" "\n"
        r"直线 $AB$ 不垂直于 $y$ 轴，设 $AB:\ x=ty-3$，代入 $2x^2-y^2=2$：" "\n"
        r"$$\left(2t^2-1\right)y^2-12ty+16=0,$$" "\n"
        r"$\Delta=144t^2-64\left(2t^2-1\right)=16\left(t^2+4\right)>0$ 恒成立，且 $2t^2-1\neq0$ 时" "\n"
        r"$$y_1+y_2=\frac{12t}{2t^2-1},\qquad y_1y_2=\frac{16}{2t^2-1}.$$" "\n"
        r"$\overrightarrow{DA}=\left(x_1-1,y_1\right)=\left(ty_1-4,y_1\right)$，同理 $\overrightarrow{DB}=\left(ty_2-4,y_2\right)$，故" "\n"
        r"$$\overrightarrow{DA}\cdot\overrightarrow{DB}=\left(ty_1-4\right)\left(ty_2-4\right)+y_1y_2"
r"=\left(t^2+1\right)y_1y_2-4t\left(y_1+y_2\right)+16$$" "\n"
        r"$$=\frac{16\left(t^2+1\right)}{2t^2-1}-\frac{48t^2}{2t^2-1}+16"
r"=\frac{16t^2+16-48t^2+32t^2-16}{2t^2-1}=0.$$" "\n"
        r"所以 $\overrightarrow{DA}\cdot\overrightarrow{DB}$ 为定值 $0$（即 $DA\perp DB$）．"
    ),
    'analysis': (
        r"（1）由顶点定 $a=1$，由渐近线方向向量定 $\dfrac ba=\sqrt2$；（2）把 $\left|PM\right|^2$ 用 $y_0$ 表示成二次函数"
        r"求最小点，再把四边形拆成 $\triangle ODP$ 与 $\triangle MDP$；（3）设 $x=ty-3$ 联立，" "\n"
        r"把 $\overrightarrow{DA}\cdot\overrightarrow{DB}$ 全部用韦达表示，分子恰好恒为零．"
    ),
    'review': (
        r"① ⭐⭐ **方向向量 $\left(1,k\right)$ ⟹ 斜率就是 $k$**：渐近线 $y=\pm bx$ 的方向向量为 $\left(1,b\right)$"
        r"（或 $\left(1,-b\right)$），故由 $\vec d=\left(1,\sqrt2\right)$ 直接得 $b=\sqrt2$，不用写斜率式．" "\n"
        r"② ⭐⭐ **$\left|PM\right|^2$ 配成 $y_0$ 的二次函数**：关键是用 $x_0^2=1+\frac{y_0^2}2$ 消掉 $x_0$，"
        r"得到 $\frac32\left(y_0-\frac23\right)^2+\frac43$．顶点 $y_0=\frac23$ 必须满足 $x_0\ge1$——"
        r"此处 $x_0=\frac{\sqrt{11}}3=1.1055\ge1$ ✓，若顶点落在右支之外就需改用端点．" "\n"
        r"③ ⭐⭐ **定值 $0$ 的几何意义是 $DA\perp DB$**：这类题算出 $0$ 时，可以反过来用"
        r"「$AB$ 过定点 $\left(-3,0\right)$，而 $-3$ 恰是 $-\dfrac{a^2+c^2}{2a}$ 型的位置」来验证．" "\n"
        r"④ **数值复核**：$y_0=\frac23$ 时 $\left|PM\right|^2=\frac32\cdot\frac49-\frac43+2=\frac23-\frac43+2=\frac43$，"
        r"$\left|PM\right|=1.1547=\frac{2\sqrt3}{3}$ ✓；" "\n"
        r"   $S=\frac12+\frac{\sqrt{11}-1}6=\frac{3+\sqrt{11}-1}6=\frac{\sqrt{11}+2}6=0.8830$ ✓" "\n"
        r"⑤ 第（3）问分子 $16t^2+16-48t^2+32t^2-16=0$ —— **$t^2$ 项与常数项各自抵消**，"
        r"这种「双抵消」是定值为零的标志，可作自检．"
    ),
    'difficulty': 0.76,
    'topics': ['M-T-351'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-351-V1',
}

T351_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知圆 $F_1:\left(x+2\sqrt3\right)^2+y^2=64$，定点 $F_2\left(2\sqrt3,0\right)$，"
        r"$A$ 是圆 $F_1$ 上的一动点，线段 $F_2A$ 的垂直平分线交半径 $F_1A$ 于 $P$ 点．" "\n"
        r"（1）求 $P$ 点的轨迹 $C$ 的方程；" "\n"
        r"（2）设直线 $l$ 过点 $\left(4,-2\right)$ 且与曲线 $C$ 相交于 $M,N$ 两点，$l$ 不经过点 $Q\left(0,2\right)$．"
        r"证明：直线 $MQ$ 的斜率与直线 $NQ$ 的斜率之和为定值．"
    ),
    'stem': [
        r"已知圆 $F_1:\left(x+2\sqrt3\right)^2+y^2=64$，定点 $F_2\left(2\sqrt3,0\right)$，"
        r"$A$ 是圆 $F_1$ 上的一动点，线段 $F_2A$ 的垂直平分线交半径 $F_1A$ 于 $P$ 点．",
        r"（1）求 $P$ 点的轨迹 $C$ 的方程；",
        r"（2）设直线 $l$ 过点 $\left(4,-2\right)$ 且与曲线 $C$ 相交于 $M,N$ 两点，$l$ 不经过点 $Q\left(0,2\right)$．"
        r"证明：直线 $MQ$ 的斜率与直线 $NQ$ 的斜率之和为定值．",
    ],
    'opts': [],
    'answer': r"（1）$\dfrac{x^2}{16}+\dfrac{y^2}4=1$；（2）定值为 $-1$．",
    'solution': (
        r"**第（1）问**" "\n"
        r"圆心 $F_1\left(-2\sqrt3,0\right)$，半径 $8$．$P$ 在 $F_2A$ 的垂直平分线上，故 $\left|PF_2\right|=\left|PA\right|$．" "\n"
        r"又 $P$ 在半径 $F_1A$ 上，$\left|PF_1\right|+\left|PA\right|=\left|F_1A\right|=8$，于是" "\n"
        r"$$\left|PF_1\right|+\left|PF_2\right|=8>4\sqrt3=\left|F_1F_2\right|,$$" "\n"
        r"所以 $P$ 的轨迹是以 $F_1,F_2$ 为焦点、$2a=8$ 的椭圆，$a=4$，$c=2\sqrt3$，$b^2=a^2-c^2=4$，" "\n"
        r"$$C:\ \frac{x^2}{16}+\frac{y^2}4=1.$$" "\n"
        r"**第（2）问**" "\n"
        r"直线 $l$ 过 $\left(4,-2\right)$，斜率存在且不为 $0$；又不经过 $Q\left(0,2\right)$，故斜率 $k\neq-1$．" "\n"
        r"设 $l:\ y+2=k\left(x-4\right)$，即 $y=kx-2\left(2k+1\right)$，代入 $x^2+4y^2=16$：" "\n"
        r"$$\left(4k^2+1\right)x^2-16k\left(2k+1\right)x+16\left(2k+1\right)^2-16=0,$$" "\n"
        r"$$\Delta=-256k>0\ \Longrightarrow\ k<0\ \left(\text{且}\ k\neq-1\right),$$" "\n"
        r"$$x_1+x_2=\frac{16k\left(2k+1\right)}{4k^2+1},\qquad x_1x_2=\frac{16\left[\left(2k+1\right)^2-1\right]}{4k^2+1}.$$" "\n"
        r"于是" "\n"
        r"$$k_{MQ}=\frac{y_1-2}{x_1}=\frac{kx_1-4\left(k+1\right)}{x_1}=k-\frac{4\left(k+1\right)}{x_1},"
r"\qquad k_{NQ}=k-\frac{4\left(k+1\right)}{x_2},$$" "\n"
        r"$$k_{MQ}+k_{NQ}=2k-4\left(k+1\right)\cdot\frac{x_1+x_2}{x_1x_2}"
r"=2k-4\left(k+1\right)\cdot\frac{k\left(2k+1\right)}{\left(2k+1\right)^2-1}$$" "\n"
        r"$$=2k-4\left(k+1\right)\cdot\frac{k\left(2k+1\right)}{4k\left(k+1\right)}"
r"=2k-\left(2k+1\right)=-1.$$" "\n"
        r"所以直线 $MQ$ 与 $NQ$ 的斜率之和为定值 $-1$．"
    ),
    'analysis': (
        r"（1）由垂直平分线得 $\left|PF_2\right|=\left|PA\right|$，再代入 $\left|PF_1\right|+\left|PA\right|=\left|F_1A\right|=8$"
        r"凑出椭圆定义；（2）设 $l$ 的点斜式方程，联立后用韦达表示 $\frac1{x_1}+\frac1{x_2}$，"
        r"代入斜率之和的表达式，分子分母约简后 $k$ 消失．"
    ),
    'review': (
        r"① ⭐⭐ **垂直平分线 + 半径 ⟹ 椭圆定义**（经典构型）：" "\n"
        r"$$\left|PF_2\right|=\left|PA\right|\ \Longrightarrow\ \left|PF_1\right|+\left|PF_2\right|"
r"=\left|PF_1\right|+\left|PA\right|=\left|F_1A\right|=R.$$" "\n"
        r"   凡是「中垂线交点落在半径上」，几乎都是这个套路，关键是**把 $PA$ 换成 $PF_2$**．" "\n"
        r"② ⭐⭐ **$k_{MQ}$ 的化简技巧**：把 $y_1-2$ 写成 $kx_1-4\left(k+1\right)$，是为了"
        r"让分式变成 $k-\dfrac{4\left(k+1\right)}{x_1}$ —— 这样求和时 $\dfrac1{x_1}+\dfrac1{x_2}$ 直接可用韦达．" "\n"
        r"   若不这样拆，$\dfrac{y_1-2}{x_1}+\dfrac{y_2-2}{x_2}$ 会同时出现 $x_1x_2$ 与 $x_1+x_2$ 和 $y$ 的混合，难化简．" "\n"
        r"③ ⚠ **$\Delta=-256k>0$ 推出 $k<0$**：这是个意外收获——直线必须与椭圆真相交，"
        r"故实际 $k\in\left(-\infty,0\right)$ 且 $k\neq-1$．原书未强调，但它是「$k$ 有定义」的前提．" "\n"
        r"④ **数值复核**：取 $k=-2$，则 $x_1+x_2=\frac{16\left(-2\right)\left(-3\right)}{17}=\frac{96}{17}=5.6471$，"
        r"$x_1x_2=\frac{16\left(9-1\right)}{17}=\frac{128}{17}=7.5294$；" "\n"
        r"   $k_{MQ}+k_{NQ}=2\left(-2\right)-4\left(-1\right)\cdot\frac{5.6471}{7.5294}=-4+4\times0.75=-1$ ✓" "\n"
        r"⑤ $\left(2k+1\right)^2-1=4k^2+4k=4k\left(k+1\right)$ 是约简的关键因式分解，"
        r"它恰好与分子的 $4\left(k+1\right)$ 和 $k$ 对上，最后只剩 $2k-\left(2k+1\right)=-1$．"
    ),
    'difficulty': 0.74,
    'topics': ['M-T-351'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-351-V2',
}

T351_V3 = {
    'type': '解答',
    'stem_text': (
        r"已知椭圆 $C:\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1\left(a>b>0\right)$ 的离心率为 $\dfrac12$，"
        r"右焦点为 $F$，点 $A\left(2,0\right)$ 在椭圆上．" "\n"
        r"（1）求椭圆 $C$ 的方程；" "\n"
        r"（2）过点 $F$ 的直线 $l$（不与 $x$ 轴重合）交椭圆 $C$ 于点 $M,N$，"
        r"直线 $MA,NA$ 分别与直线 $x=4$ 交于点 $P,Q$．"
        r"求证：以线段 $PQ$ 为直径的圆被 $x$ 轴截得的弦长为定值．"
    ),
    'stem': [
        r"已知椭圆 $C:\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1\left(a>b>0\right)$ 的离心率为 $\dfrac12$，"
        r"右焦点为 $F$，点 $A\left(2,0\right)$ 在椭圆上．",
        r"（1）求椭圆 $C$ 的方程；",
        r"（2）过点 $F$ 的直线 $l$（不与 $x$ 轴重合）交椭圆 $C$ 于点 $M,N$，"
        r"直线 $MA,NA$ 分别与直线 $x=4$ 交于点 $P,Q$．"
        r"求证：以线段 $PQ$ 为直径的圆被 $x$ 轴截得的弦长为定值．",
    ],
    'opts': [],
    'answer': r"（1）$\dfrac{x^2}4+\dfrac{y^2}3=1$；（2）定值为 $6$．",
    'solution': (
        r"**第（1）问**" "\n"
        r"点 $A\left(2,0\right)$ 在椭圆上且在 $x$ 轴正半轴，故 $a=2$；由 $e=\dfrac ca=\dfrac12$ 得 $c=1$，"
        r"$b=\sqrt{a^2-c^2}=\sqrt3$，" "\n"
        r"$$C:\ \frac{x^2}4+\frac{y^2}3=1,\qquad F\left(1,0\right).$$" "\n"
        r"**第（2）问**" "\n"
        r"设 $l:\ x=my+1$，$M\left(x_1,y_1\right)$，$N\left(x_2,y_2\right)$，代入 $3x^2+4y^2=12$：" "\n"
        r"$$\left(3m^2+4\right)y^2+6my-9=0,\qquad"
r"y_1+y_2=-\frac{6m}{3m^2+4},\quad y_1y_2=-\frac9{3m^2+4}.$$" "\n"
        r"直线 $MA$ 的方程为 $y=\dfrac{y_1}{x_1-2}\left(x-2\right)$，其中 $x_1-2=my_1-1$．" "\n"
        r"令 $x=4$ 得 $P\left(4,\dfrac{2y_1}{my_1-1}\right)$，同理 $Q\left(4,\dfrac{2y_2}{my_2-1}\right)$．" "\n"
        r"分母：$\left(my_1-1\right)\left(my_2-1\right)=m^2y_1y_2-m\left(y_1+y_2\right)+1"
r"=\dfrac{-9m^2+6m^2}{3m^2+4}+1=\dfrac4{3m^2+4}$，" "\n"
        r"分子：$2y_1\left(my_2-1\right)-2y_2\left(my_1-1\right)=2\left(y_2-y_1\right)$，故" "\n"
        r"$$\left|PQ\right|=\frac{2\left|y_1-y_2\right|\left(3m^2+4\right)}4"
r"=\frac{3m^2+4}2\cdot\frac{12\sqrt{m^2+1}}{3m^2+4}=6\sqrt{m^2+1}.$$" "\n"
        r"$PQ$ 中点的纵坐标为" "\n"
        r"$$\frac{y_1}{my_1-1}+\frac{y_2}{my_2-1}=\frac{2my_1y_2-\left(y_1+y_2\right)}{\left(my_1-1\right)\left(my_2-1\right)}"
r"=\frac{\dfrac{-18m+6m}{3m^2+4}}{\dfrac4{3m^2+4}}=-3m.$$" "\n"
        r"以 $PQ$ 为直径的圆，圆心 $\left(4,-3m\right)$，半径 $r=3\sqrt{m^2+1}$，被 $x$ 轴截得的弦长为" "\n"
        r"$$2\sqrt{r^2-\left(-3m\right)^2}=2\sqrt{9\left(m^2+1\right)-9m^2}=2\sqrt9=6.$$" "\n"
        r"所以弦长为定值 $6$．"
    ),
    'analysis': (
        r"（1）由 $A\left(2,0\right)$ 在椭圆上定 $a=2$，离心率定 $c=1$；（2）设 $x=my+1$ 联立，"
        r"写出 $P,Q$ 的纵坐标表达式，用韦达分别求出 $\left|PQ\right|$ 与中点纵坐标，"
        r"最后用 $2\sqrt{r^2-d^2}$ 算 $x$ 轴截得的弦长，此时 $m$ 恰好完全抵消．"
    ),
    'review': (
        r"① ⭐⭐ **$x=my+1$ 优于 $y=k\left(x-1\right)$**：本题 $l$ 不与 $x$ 轴重合但**可以垂直于 $x$ 轴**，"
        r"用 $x=my+1$ 时 $m=0$ 正好对应竖直情形，一个参数覆盖全部情况．" "\n"
        r"② ⭐⭐ **分母 $\left(my_1-1\right)\left(my_2-1\right)$ 的化简是本题关键**，算出 $\dfrac4{3m^2+4}$ 后"
        r"分子只含 $y_2-y_1$，于是 $\left|PQ\right|$ 直接正比于 $\left|y_1-y_2\right|$．" "\n"
        r"③ ⭐⭐ **中点纵坐标恰好是 $-3m$**：与 $m$ 成线性，而半径平方是 $9\left(m^2+1\right)$，" "\n"
        r"$$r^2-d^2=9\left(m^2+1\right)-9m^2=9$$" "\n"
        r"   **$m^2$ 项精确抵消** —— 这正是「弦长为定值」的代数机制．" "\n"
        r"④ **数值复核**：$m=0$ 时 $l:x=1$，$M\left(1,\frac32\right),N\left(1,-\frac32\right)$；"
        r"$MA$ 斜率 $=\frac{3/2}{-1}=-\frac32$，$P\left(4,-3\right)$；同理 $Q\left(4,3\right)$；" "\n"
        r"   $\left|PQ\right|=6$，圆心 $\left(4,0\right)$，半径 $3$，被 $x$ 轴截得弦长 $=2\cdot3=6$ ✓" "\n"
        r"   $m=1$ 时 $\left|PQ\right|=6\sqrt2=8.4853$，中点纵坐标 $-3$，$r=3\sqrt2$；"
        r"$\sqrt{r^2-9}=\sqrt{18-9}=3$，弦长 $=6$ ✓" "\n"
        r"⑤ 本题与 M-T-348-E1 同属「直线 $x=t$ 上的截线段」构型，区别是本题问**被 $x$ 轴截得的弦长**，"
        r"需用到圆心到 $x$ 轴的距离，多一步 $2\sqrt{r^2-d^2}$．"
    ),
    'difficulty': 0.77,
    'topics': ['M-T-351'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-351-V3',
}

T348_E1 = {
    'type': '解答',
    'stem_text': (
        r"在平面直角坐标系中，已知椭圆 $C:\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1\left(a>b>0\right)$ 的左、右焦点"
        r"分别为 $F_1,F_2$，点 $P$ 为椭圆 $C$ 上的动点，当点 $P$ 为短轴顶点时，"
        r"$\triangle F_1PF_2$ 的面积为 $\sqrt3$，椭圆短轴长为 $2$．" "\n"
        r"（1）求椭圆 $C$ 的方程；" "\n"
        r"（2）若直线 $l$ 过定点 $\left(1,0\right)$ 且与椭圆 $C$ 交于不同的两点 $A,B$，"
        r"点 $M$ 是椭圆 $C$ 的右顶点，直线 $AM,BM$ 分别与 $y$ 轴交于 $P,Q$ 两点，"
        r"试问：以线段 $PQ$ 为直径的圆是否过 $x$ 轴上的定点？若是，求出定点坐标；若不是，说明理由．"
    ),
    'stem': [
        r"在平面直角坐标系中，已知椭圆 $C:\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1\left(a>b>0\right)$ 的左、右焦点"
        r"分别为 $F_1,F_2$，点 $P$ 为椭圆 $C$ 上的动点，当点 $P$ 为短轴顶点时，"
        r"$\triangle F_1PF_2$ 的面积为 $\sqrt3$，椭圆短轴长为 $2$．",
        r"（1）求椭圆 $C$ 的方程；",
        r"（2）若直线 $l$ 过定点 $\left(1,0\right)$ 且与椭圆 $C$ 交于不同的两点 $A,B$，"
        r"点 $M$ 是椭圆 $C$ 的右顶点，直线 $AM,BM$ 分别与 $y$ 轴交于 $P,Q$ 两点，"
        r"试问：以线段 $PQ$ 为直径的圆是否过 $x$ 轴上的定点？若是，求出定点坐标；若不是，说明理由．",
    ],
    'opts': [],
    'answer': r"（1）$\dfrac{x^2}4+y^2=1$；（2）过定点，定点为 $\left(\pm\sqrt3,0\right)$．",
    'solution': (
        r"**第（1）问**" "\n"
        r"短轴长 $2b=2$，故 $b=1$；$P$ 为短轴顶点时 $S_{\triangle F_1PF_2}=\dfrac12\left|F_1F_2\right|\cdot b=bc=\sqrt3$，"
        r"得 $c=\sqrt3$，$a^2=b^2+c^2=4$，" "\n"
        r"$$C:\ \frac{x^2}4+y^2=1.$$" "\n"
        r"**第（2）问**" "\n"
        r"右顶点 $M\left(2,0\right)$．当 $l$ 斜率存在时，设 $l:\ y=k\left(x-1\right)$，$A\left(x_1,y_1\right)$，$B\left(x_2,y_2\right)$，" "\n"
        r"代入 $x^2+4y^2=4$ 得 $\left(1+4k^2\right)x^2-8k^2x+4k^2-4=0$，于是" "\n"
        r"$$x_1+x_2=\frac{8k^2}{1+4k^2},\qquad x_1x_2=\frac{4k^2-4}{1+4k^2},$$" "\n"
        r"$$y_1y_2=k^2\left(x_1-1\right)\left(x_2-1\right)=k^2\left[x_1x_2-\left(x_1+x_2\right)+1\right]"
r"=-\frac{3k^2}{1+4k^2}.$$" "\n"
        r"直线 $AM:\ y=\dfrac{y_1}{x_1-2}\left(x-2\right)$，令 $x=0$ 得 $P\left(0,-\dfrac{2y_1}{x_1-2}\right)$；"
        r"同理 $Q\left(0,-\dfrac{2y_2}{x_2-2}\right)$．" "\n"
        r"设 $x$ 轴上的定点为 $N\left(x_0,0\right)$．若以 $PQ$ 为直径的圆过 $N$，则 $\overrightarrow{PN}\cdot\overrightarrow{QN}=0$，即" "\n"
        r"$$x_0^2+\frac{4y_1y_2}{\left(x_1-2\right)\left(x_2-2\right)}=0"
r"\quad\Longrightarrow\quad x_0^2+\frac{4y_1y_2}{x_1x_2-2\left(x_1+x_2\right)+4}=0.$$" "\n"
        r"而 $x_1x_2-2\left(x_1+x_2\right)+4=\dfrac{4k^2-4-16k^2+4+16k^2}{1+4k^2}=\dfrac{4k^2}{1+4k^2}$，故" "\n"
        r"$$x_0^2+\frac{4\cdot\left(-\dfrac{3k^2}{1+4k^2}\right)}{\dfrac{4k^2}{1+4k^2}}=x_0^2-3=0"
r"\quad\Longrightarrow\quad x_0=\pm\sqrt3.$$" "\n"
        r"当 $l$ 斜率不存在时，$l:x=1$，$A\left(1,\frac{\sqrt3}2\right)$，$B\left(1,-\frac{\sqrt3}2\right)$，" "\n"
        r"算得 $P\left(0,\sqrt3\right)$，$Q\left(0,-\sqrt3\right)$，圆为 $x^2+y^2=3$，同样过 $\left(\pm\sqrt3,0\right)$．" "\n"
        r"所以以 $PQ$ 为直径的圆过 $x$ 轴上的定点 $\left(\pm\sqrt3,0\right)$．"
    ),
    'analysis': (
        r"（1）由短轴长定 $b$、由短轴顶点处三角形面积 $bc$ 定 $c$；（2）设 $l$ 方程联立得韦达，"
        r"写出 $P,Q$ 坐标后设 $x$ 轴上定点 $N\left(x_0,0\right)$，用 $\overrightarrow{PN}\cdot\overrightarrow{QN}=0$ 列方程，"
        r"代入韦达后 $k$ 全部约掉，解出 $x_0=\pm\sqrt3$，最后补验斜率不存在的情形．"
    ),
    'review': (
        r"① ⭐⭐ **「圆过定点」一律翻译成数量积为零**：设 $N\left(x_0,0\right)$，则 $\overrightarrow{PN}\cdot\overrightarrow{QN}=0$．"
        r"因为 $P,Q$ 都在 $y$ 轴上，$\overrightarrow{PN}=\left(x_0,\frac{2y_1}{x_1-2}\right)$，"
        r"$\overrightarrow{QN}=\left(x_0,\frac{2y_2}{x_2-2}\right)$，点积只有两项，极简．" "\n"
        r"② ⭐⭐ **分母 $x_1x_2-2\left(x_1+x_2\right)+4$ 化简后是 $\dfrac{4k^2}{1+4k^2}$**，"
        r"分子 $4y_1y_2=-\dfrac{12k^2}{1+4k^2}$，两者之比恰为 $-3$ —— **$k$ 精确抵消**，这就是定点存在的证据．" "\n"
        r"③ ⚠ **必须补验斜率不存在的情形**：$l:x=1$ 时圆为 $x^2+y^2=3$（圆心原点、半径 $\sqrt3$），"
        r"同样过 $\left(\pm\sqrt3,0\right)$ ✓．若不补验，答案不完整．" "\n"
        r"④ **数值复核**：$k=1$ 时 $x_1+x_2=\frac8{5}=1.6$，$x_1x_2=0$，$y_1y_2=-\frac35=-0.6$；" "\n"
        r"   分母 $=0-3.2+4=0.8$，$\frac{4\left(-0.6\right)}{0.8}=-3$，$x_0^2=3$ ✓" "\n"
        r"⑤ 定点 $\left(\pm\sqrt3,0\right)$ 与椭圆的 $c=\sqrt3$ 一致 —— 这类题的定点常常就是焦点或准线与 $x$ 轴的交点，"
        r"可作为猜测定点的 shortcuts（但必须严格证明）．"
    ),
    'difficulty': 0.75,
    'topics': ['M-T-348'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-348-E1',
}

T348_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知椭圆 $E:\dfrac{x^2}3+\dfrac{y^2}2=1$ 的左右顶点分别为 $A,B$，点 $P$ 为椭圆上异于 $A,B$ 的任意一点．" "\n"
        r"（1）证明：直线 $PA$ 与直线 $PB$ 的斜率乘积为定值；" "\n"
        r"（2）设 $Q\left(t,0\right)\ \left(t\neq-\sqrt3\right)$，过点 $Q$ 作与 $x$ 轴不重合的任意直线交椭圆 $E$ 于 $M,N$ 两点．"
        r"问：是否存在实数 $t$，使得以 $MN$ 为直径的圆恒过定点 $A$？若存在，求出 $t$ 的值；若不存在，请说明理由．"
    ),
    'stem': [
        r"已知椭圆 $E:\dfrac{x^2}3+\dfrac{y^2}2=1$ 的左右顶点分别为 $A,B$，点 $P$ 为椭圆上异于 $A,B$ 的任意一点．",
        r"（1）证明：直线 $PA$ 与直线 $PB$ 的斜率乘积为定值；",
        r"（2）设 $Q\left(t,0\right)\ \left(t\neq-\sqrt3\right)$，过点 $Q$ 作与 $x$ 轴不重合的任意直线交椭圆 $E$ 于 $M,N$ 两点．"
        r"问：是否存在实数 $t$，使得以 $MN$ 为直径的圆恒过定点 $A$？若存在，求出 $t$ 的值；若不存在，请说明理由．",
    ],
    'opts': [],
    'answer': r"（1）$k_{PA}\cdot k_{PB}=-\dfrac23$；（2）存在，$t=-\dfrac{\sqrt3}5$．",
    'solution': (
        r"**第（1）问**" "\n"
        r"$A\left(-\sqrt3,0\right)$，$B\left(\sqrt3,0\right)$．设 $P\left(m,n\right)$，由 $\dfrac{m^2}3+\dfrac{n^2}2=1$ 得"
        r"$n^2=2\left(1-\dfrac{m^2}3\right)=\dfrac{2\left(3-m^2\right)}3$，于是" "\n"
        r"$$k_{PA}\cdot k_{PB}=\frac n{m+\sqrt3}\cdot\frac n{m-\sqrt3}"
r"=\frac{n^2}{m^2-3}=\frac{\dfrac{2\left(3-m^2\right)}3}{m^2-3}=-\frac23.$$" "\n"
        r"**第（2）问**" "\n"
        r"设 $M\left(x_1,y_1\right)$，$N\left(x_2,y_2\right)$，直线 $MN:\ x=my+t$，代入 $2x^2+3y^2=6$：" "\n"
        r"$$\left(2m^2+3\right)y^2+4mty+2t^2-6=0,$$" "\n"
        r"$$y_1+y_2=-\frac{4mt}{2m^2+3},\qquad y_1y_2=\frac{2t^2-6}{2m^2+3}.$$" "\n"
        r"以 $MN$ 为直径的圆过点 $A\left(-\sqrt3,0\right)$ $\iff$ $\overrightarrow{AM}\cdot\overrightarrow{AN}=0$，即" "\n"
        r"$$\left(x_1+\sqrt3\right)\left(x_2+\sqrt3\right)+y_1y_2=0.$$" "\n"
        r"代入 $x_i=my_i+t$ 整理得" "\n"
        r"$$\left(1+m^2\right)y_1y_2+\left(mt+\sqrt3m\right)\left(y_1+y_2\right)+t^2+2\sqrt3t+3=0.$$" "\n"
        r"代入韦达并乘以 $2m^2+3$：" "\n"
        r"$$\left(1+m^2\right)\left(2t^2-6\right)-4m^2t\left(t+\sqrt3\right)+\left(2m^2+3\right)\left(t+\sqrt3\right)^2=0.$$" "\n"
        r"其中 $m^2$ 的系数为" "\n"
        r"$$\left(2t^2-6\right)-4t\left(t+\sqrt3\right)+2\left(t+\sqrt3\right)^2"
r"=2t^2-6-4t^2-4\sqrt3t+2t^2+4\sqrt3t+6=0,$$" "\n"
        r"恒成立！故只需常数项为零：" "\n"
        r"$$\left(2t^2-6\right)+3\left(t+\sqrt3\right)^2=0"
r"\ \Longrightarrow\ 5t^2+6\sqrt3t+3=0,$$" "\n"
        r"解得 $t=-\dfrac{\sqrt3}5$ 或 $t=-\sqrt3$（舍去）．" "\n"
        r"此时 $\Delta=24\left[-\left(t^2-3\right)+2m^2\right]>0$ 恒成立，故存在 $Q\left(-\dfrac{\sqrt3}5,0\right)$ 满足题意．"
    ),
    'analysis': (
        r"（1）设 $P\left(m,n\right)$ 后用椭圆方程把 $n^2$ 表示成 $m$ 的函数，代入斜率之积即得常数；"
        r"（2）把「圆过 $A$」翻译成 $\overrightarrow{AM}\cdot\overrightarrow{AN}=0$，设 $x=my+t$ 联立，"
        r"代入韦达后按 $m$ 的幂次整理，令 $m^2$ 的系数与常数项分别为零解出 $t$．"
    ),
    'review': (
        r"① ⭐⭐ **椭圆上点与两顶点连线的斜率积恒为 $-\dfrac{b^2}{a^2}$**（一般结论）：" "\n"
        r"$$k_{PA}k_{PB}=\frac{n^2}{m^2-a^2}=\frac{b^2\left(1-\frac{m^2}{a^2}\right)}{m^2-a^2}=-\frac{b^2}{a^2}=-\frac23.$$" "\n"
        r"   本题 $a^2=3,b^2=2$，故 $-\frac23$ ✓．这个结论可直接背下来用于填空选择．" "\n"
        r"② ⭐⭐ **$m^2$ 的系数恒为零是本题的题眼**：展开后 $2t^2-6-4t^2-4\sqrt3t+2t^2+4\sqrt3t+6=0$，" "\n"
        r"   $t^2$ 项、$\sqrt3t$ 项、常数项**三者各自抵消** —— 说明「对任意 $m$ 恒成立」自动满足，"
        r"只剩常数项方程决定 $t$．这类「分离参数的幂次」做法是存在性问题的通法．" "\n"
        r"③ ⚠ **$t=-\sqrt3$ 必须舍去**：题设 $t\neq-\sqrt3$（否则 $Q$ 就是 $A$，圆退化）．" "\n"
        r"④ **数值复核**：$t=-\frac{\sqrt3}{5}=-0.3464$ 时，$5t^2+6\sqrt3t+3=\frac{15}{25}-\frac{18}5+3=0.6-3.6+3=0$ ✓" "\n"
        r"   取 $m=0$（$MN$ 为竖直线 $x=t$）：$2t^2+3y^2=6$ ⟹ $y^2=\frac{6-2t^2}3=\frac{6-0.24}3=1.92$；"
        r"$M\left(t,\sqrt{1.92}\right)$、$N\left(t,-\sqrt{1.92}\right)$；" "\n"
        r"   $\overrightarrow{AM}=\left(t+\sqrt3,\sqrt{1.92}\right)$，$\overrightarrow{AN}=\left(t+\sqrt3,-\sqrt{1.92}\right)$；"
        r"点积 $=\left(t+\sqrt3\right)^2-1.92=\left(1.3856\right)^2-1.92=1.92-1.92=0$ ✓" "\n"
        r"⑤ 第（2）问与第（1）问在结构上呼应：都是「$x$ 轴上的特殊点（$A$）与椭圆上点的连线」的垂直关系，"
        r"只是第（1）问是斜率积为定值，第（2）问是数量积为零．"
    ),
    'difficulty': 0.76,
    'topics': ['M-T-348'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-348-V2',
}

T361_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知双曲线 $\Omega:\dfrac{x^2}{a^2}-\dfrac{y^2}{b^2}=1\ \left(a>0,b>0\right)$，"
        r"$A\left(2,0\right)$，$B\left(-\dfrac32,-\dfrac{\sqrt{15}}2\right)$，$C\left(\dfrac32,\dfrac{\sqrt{15}}2\right)$，"
        r"$D\left(-1,0\right)$，$E\left(4,0\right)$ 五点中恰有三点在 $\Omega$ 上．" "\n"
        r"（1）求 $\Omega$ 的方程；" "\n"
        r"（2）设 $P$ 是 $\Omega$ 上位于第一象限内的一动点，则是否存在定点 $Q\left(m,0\right)\ \left(m<0\right)$，"
        r"使得 $\angle PQA+\dfrac12\angle PAE=\dfrac\pi2$？若存在，求出点 $Q$ 的坐标；若不存在，请说明理由．"
    ),
    'stem': [
        r"已知双曲线 $\Omega:\dfrac{x^2}{a^2}-\dfrac{y^2}{b^2}=1\ \left(a>0,b>0\right)$，"
        r"$A\left(2,0\right)$，$B\left(-\dfrac32,-\dfrac{\sqrt{15}}2\right)$，$C\left(\dfrac32,\dfrac{\sqrt{15}}2\right)$，"
        r"$D\left(-1,0\right)$，$E\left(4,0\right)$ 五点中恰有三点在 $\Omega$ 上．",
        r"（1）求 $\Omega$ 的方程；",
        r"（2）设 $P$ 是 $\Omega$ 上位于第一象限内的一动点，则是否存在定点 $Q\left(m,0\right)\ \left(m<0\right)$，"
        r"使得 $\angle PQA+\dfrac12\angle PAE=\dfrac\pi2$？若存在，求出点 $Q$ 的坐标；若不存在，请说明理由．",
    ],
    'opts': [],
    'answer': r"（1）$x^2-\dfrac{y^2}3=1$；（2）存在，$Q\left(-1,0\right)$．",
    'solution': (
        r"**第（1）问**" "\n"
        r"双曲线与其 $x$ 轴的交点只能是顶点 $\left(\pm a,0\right)$，因此在 $x$ 轴上的三点 $A\left(2,0\right)$、"
        r"$D\left(-1,0\right)$、$E\left(4,0\right)$ 中至多有一个在 $\Omega$ 上（三者横坐标两两不互为相反数）．" "\n"
        r"要凑足三点，只能是 $B,C$ 都在 $\Omega$ 上，再加上 $A,D,E$ 中的某一个．" "\n"
        r"$B,C$ 关于原点对称，双曲线也关于原点对称，二者可同时在 $\Omega$ 上．" "\n"
        r"由 $B\left(-\dfrac32,-\dfrac{\sqrt{15}}2\right)$ 在 $\Omega$ 上得 $\dfrac{9}{4a^2}-\dfrac{15}{4b^2}=1$．" "\n"
        r"若 $a^2=4$ 或 $a^2=16$（即 $A$ 或 $E$ 是顶点），则该式左边"
        r"$\dfrac{9}{4a^2}-\dfrac{15}{4b^2}<\dfrac{9}{16}<1$，无解．故 $a^2=1$，即 $D\left(-1,0\right)$ 在 $\Omega$ 上，" "\n"
        r"$$\frac1{a^2}=1\ \Longrightarrow\ a^2=1,\qquad \frac94-\frac{15}{4b^2}=1\ \Longrightarrow\ b^2=3.$$" "\n"
        r"验证：$D\left(-1,0\right)$ 满足 $1-0=1$ ✓；$B,C$ 满足 $\dfrac94-\dfrac{15}{12}=\dfrac94-\dfrac54=1$ ✓；"
        r"$A\left(2,0\right)$：$4\neq1$ ✗；$E\left(4,0\right)$：$16\neq1$ ✗．恰有三点 $B,C,D$ 在 $\Omega$ 上 ✓" "\n"
        r"$$\Omega:\ x^2-\frac{y^2}3=1.$$" "\n"
        r"**第（2）问**" "\n"
        r"因 $A\left(2,0\right)$、$E\left(4,0\right)$、$Q\left(m,0\right)$ 都在 $x$ 轴上且 $m<0<2<4$，"
        r"射线 $AE$ 与 $AQ$ 方向相反，故 $\angle PAE=\pi-\angle PAQ$．条件化为" "\n"
        r"$$\angle PQA+\frac12\left(\pi-\angle PAQ\right)=\frac\pi2"
r"\ \Longrightarrow\ 2\angle PQA=\angle PAQ.$$" "\n"
        r"① 当 $PA\perp x$ 轴时，$P\left(2,3\right)$（由 $4-\dfrac{y^2}3=1$ 得 $y=3$）．" "\n"
        r"此时 $\angle PAQ=\dfrac\pi2$，故 $\angle PQA=\dfrac\pi4$，于是 $\left|QA\right|=\left|PA\right|=3$，" "\n"
        r"$$3=2-m\ \Longrightarrow\ m=-1,\qquad Q\left(-1,0\right).$$" "\n"
        r"② 当 $PA$ 不与 $x$ 轴垂直时，验证 $Q\left(-1,0\right)$ 满足 $2\angle PQA=\angle PAQ$．" "\n"
        r"设 $P\left(x_0,y_0\right)$（$x_0>1,\ y_0>0$），则 $y_0^2=3x_0^2-3$，" "\n"
        r"$$\tan\angle PQA=\frac{y_0}{x_0+1},$$" "\n"
        r"$$\tan2\angle PQA=\frac{2\cdot\dfrac{y_0}{x_0+1}}{1-\left(\dfrac{y_0}{x_0+1}\right)^2}"
r"=\frac{2y_0\left(x_0+1\right)}{\left(x_0+1\right)^2-y_0^2}"
r"=\frac{2y_0\left(x_0+1\right)}{x_0^2+2x_0+1-3x_0^2+3}$$" "\n"
        r"$$=\frac{2y_0\left(x_0+1\right)}{-2\left(x_0^2-x_0-2\right)}"
r"=\frac{y_0\left(x_0+1\right)}{-\left(x_0-2\right)\left(x_0+1\right)}=\frac{y_0}{2-x_0}.$$" "\n"
        r"另一方面，$\overrightarrow{AP}=\left(x_0-2,y_0\right)$，$\overrightarrow{AQ}=\left(-3,0\right)$，" "\n"
        r"$$\cos\angle PAQ=\frac{2-x_0}{\left|AP\right|},\qquad \sin\angle PAQ=\frac{y_0}{\left|AP\right|}"
r"\ \Longrightarrow\ \tan\angle PAQ=\frac{y_0}{2-x_0}.$$" "\n"
        r"故 $\tan2\angle PQA=\tan\angle PAQ$．又 $2\angle PQA\in\left(0,\pi\right)$、$\angle PAQ\in\left(0,\pi\right)$，"
        r"所以 $2\angle PQA=\angle PAQ$ 成立．" "\n"
        r"综上，存在定点 $Q\left(-1,0\right)$．"
    ),
    'analysis': (
        r"（1）利用「$x$ 轴上的点只有顶点在双曲线上」排除 $A,E$，再由 $B,C$ 关于原点对称推出二者同在，"
        r"代入坐标解出 $a^2=1,b^2=3$；（2）先把 $\angle PAE$ 换成 $\pi-\angle PAQ$ 把条件化为 $2\angle PQA=\angle PAQ$，"
        r"用特殊位置（$PA\perp x$ 轴）猜出 $Q\left(-1,0\right)$，再用正切的二倍角公式验证一般情形成立．"
    ),
    'review': (
        r"① ⭐⭐ **「五点中恰有三点在双曲线上」的突破口是 $x$ 轴上的点**：$x$ 轴与双曲线 $\frac{x^2}{a^2}-\frac{y^2}{b^2}=1$"
        r"的交点只有顶点 $\left(\pm a,0\right)$，所以 $A\left(2,0\right)$、$D\left(-1,0\right)$、$E\left(4,0\right)$ 中至多一个在曲线上——"
        r"因为 $2,-1,4$ 两两不互为相反数，不可能同时出现两个顶点．" "\n"
        r"② ⭐⭐ **$B,C$ 关于原点对称 ⟹ 同时在或同时不在**，这是凑够三点数的关键．" "\n"
        r"③ ⭐⭐ **特殊位置猜点、一般位置验证**（本批最漂亮的思路）：" "\n"
        r"   先取 $PA\perp x$ 轴这一特殊位置，由 $2\angle PQA=\angle PAQ=\frac\pi2$ 得 $\angle PQA=\frac\pi4$，"
        r"   $\left|QA\right|=\left|PA\right|=3$ ⟹ $m=-1$；再对一般点验证 $\tan2\angle PQA=\tan\angle PAQ$．" "\n"
        r"   凡「是否存在定点」的探究题，**先用特殊位置猜出定点，再验证**，比正面推导高效得多．" "\n"
        r"④ ⭐ **$\angle PAE=\pi-\angle PAQ$ 是转换关键**：因为 $E$ 在 $A$ 右侧、$Q$ 在 $A$ 左侧，"
        r"两条射线 $AE$ 与 $AQ$ 方向相反，所成的两个角互补．漏掉这一步就化不出 $2\angle PQA=\angle PAQ$．" "\n"
        r"⑤ **数值复核**：$a^2=1,b^2=3$ 时 $B:\frac94-\frac{15}{12}=2.25-1.25=1$ ✓，$D:1-0=1$ ✓，$A:4\neq1$ ✓，$E:16\neq1$ ✓；" "\n"
        r"   取 $P\left(2,3\right)$，$\tan\angle PQA=\frac3{2+1}=1$ ⟹ $\angle PQA=\frac\pi4$，"
        r"$\tan\angle PAQ=\frac3{2-2}\to\infty$ ⟹ $\angle PAQ=\frac\pi2$，满足 $2\cdot\frac\pi4=\frac\pi2$ ✓" "\n"
        r"   取 $P\left(\sqrt2,\sqrt3\right)$（$x_0=1.4142,y_0=1.7321$）：$\tan\angle PQA=\frac{1.7321}{2.4142}=0.7174$ ⟹ "
        r"$\angle PQA=35.66^\circ$；$\tan2\angle PQA=\frac{1.7321}{2-1.4142}=2.9619$ ⟹ $2\angle PQA=71.35^\circ$；" "\n"
        r"   $\tan\angle PAQ=\frac{1.7321}{0.5858}=2.9563$ ⟹ $\angle PAQ=71.32^\circ$，两者吻合 ✓（舍入误差内）" "\n"
        r"⑥ 注意 $\tan$ 相等 ⟹ 角相等需要限定区间：这里 $2\angle PQA,\angle PAQ\in\left(0,\pi\right)$，故成立．"
    ),
    'difficulty': 0.80,
    'topics': ['M-T-361'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-361-E1',
}

QS = [
    T350_E1, T350_V1, T350_V2, T350_V3,
    T351_V1, T351_V2, T351_V3,
    T348_E1, T348_V2,
    T361_E1,
]
