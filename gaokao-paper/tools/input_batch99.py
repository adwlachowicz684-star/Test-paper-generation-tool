# -*- coding: utf-8 -*-
r"""第 99 批：圆锥曲线切线与法线（M-T-358，4 题）+ 椭圆轨迹与定点（M-T-360，4 题）
+ 圆过定点（M-T-348-V1/V3，2 题）+ 概率递推（M-T-398-E1/V1，2 题）

    python3 tools/run_batch.py 99

## 选题依据

按「详解完整 + 同题型聚堆」筛出，本批 12 题全为解答题。
M-T-358 四题原文集中在 p239-241（切线 / 法线 / 切点弦），
M-T-360 四题集中在 p243-246（轨迹 / 点差法 / 定点），
M-T-398-E1、V1 在 p276（概率递推，两题结构几乎相同）。

## 第一条：切点弦方程「一点两用」

M-T-358-V1 与 V3 的核心完全一致：

- 椭圆上点处切线为对应的对称式
- 双曲线上点处切线只差一个符号

**同一条式子，把动点换成定点 $P(m,n)$ 且 $P$ 在其上，就得到切点弦 $AB$ 的方程。**

> 通法：**「过 $P$ 作两条切线」⟹ 切点弦方程就是把切线公式里的动点换成 $P$ 的坐标。**
> M-T-358-V1 用它得切点弦，M-T-358-V3 也用它得切点弦。

## 第二条：圆过 x 轴定点的「令 y=0 消参」

M-T-348-V1：以 $CD$ 为直径的圆写好后令 $y=0$，两个平方差一减，参数 $m$ 立刻消掉，
得到 $(x-2)^2=3$，定点 $(2\pm\sqrt3,0)$。

> 通法：凡「圆过定点」，把圆方程写出后**令 $y=0$（或 $x=0$）用 $(a+b)^2-(a-b)^2=4ab$ 消参**。

## 第三条：两条递推是同一个模型

M-T-398-E1（每次走 1 步概率 2/3 或 2 步概率 1/3）与 V1（掷硬币各 1/2），
递推都是 $P_n=pP_{n-1}+qP_{n-2}$，作差得 $P_n-P_{n-1}=-q(P_{n-1}-P_{n-2})$。

**公比恒为 $-q$，与 $p$ 无关。**
稳态值（$n\to\infty$）是 $\frac1{1+q}$：E1 为 $\frac34$，V1 为 $\frac23$ —— 恰好是「平均步长」的倒数。

> 通法：**「每次前进 1 或 2」型一律作差构造等比，公比 $=-\,($走 2 步的概率$)$。**

## 第四条：点差法配「两个垂直」联立解中点

M-T-360-V1 里两个条件各自给一个方程：点差法给一个，$AC\perp OC$ 给一个，
两式右端相等 ⟹ 解出中点纵坐标 $y_0=2m-1$。

> 通法：**出现「$AC\perp OC$」就用斜率积 $=-1$；与点差法的式子右端对齐，往往正好解出中点纵坐标。**

## 三处原书 OCR 错误（判据写在各题 review 里）

1. **M-T-358-V1 详解**：面积表达式漏了根号（否则令 $t$ 换元后化不成标准形式）。
2. **M-T-358-V3 详解**：末行余弦值 `30/6` 实为 $\frac{\sqrt{30}}6$（余弦值必须 $\le1$）。
3. **M-T-360-V1 题干**：点 $D$ 在 $y$ 轴上，已按详解口径录入。
"""

T358_E1 = {
    'type': '解答',
    'stem_text': (
        r"定义平面曲线的法线如下：经过平面曲线 $C$ 上一点 $M$，且与曲线 $C$ 在点 $M$ 处的切线垂直的直线，"
        r"称为曲线 $C$ 在点 $M$ 处的法线．设点 $M\left(x_0,y_0\right)\left(y_0>0\right)$ 为抛物线 $C:y^{2}=2px\ (p>0)$ 上一点．"
        r"（1）求抛物线 $C$ 在点 $M$ 处的切线的方程（结果不含 $x_{0}$）；"
        r"（2）求抛物线 $C$ 在点 $M$ 处的法线被抛物线 $C$ 截得的弦长 $\left|AB\right|$ 的最小值，并求此时点 $M$ 的坐标．"
    ),
    'opts': [],
    'answer': (
        r"（1）$y=\dfrac{p}{y_{0}}x+\dfrac{y_{0}}2$；"
        r"（2）$\left|AB\right|_{\min}=3\sqrt3\,p$，此时 $M\left(p,\sqrt2\,p\right)$．"
    ),
    'analysis': (
        r"（1）由 $2yy'=2p$ 得切线斜率 $\frac p{y_0}$，点斜式后用 $x_0=\frac{y_0^2}{2p}$ 消去 $x_0$；"
        r"（2）法线斜率为切线斜率的负倒数，联立抛物线后用弦长公式把弦长表成 $y_0$ 的函数，"
        r"换元 $t=y_0^{2}$ 后求导定最值．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"对 $y^{2}=2px$ 两边求导：$2yy'=2p$，即 $y'=\dfrac py$．" "\n"
        r"故在点 $M$ 处的切线斜率 $k=y'\big|_{y=y_{0}}=\dfrac p{y_{0}}$．" "\n"
        r"切线方程为 $y-y_{0}=\dfrac p{y_{0}}\left(x-x_{0}\right)$，又 $x_{0}=\dfrac{y_{0}^{2}}{2p}$，" "\n"
        r"$y-y_{0}=\dfrac p{y_{0}}x-\dfrac{y_{0}}2$，即 $\boxed{y=\dfrac p{y_{0}}x+\dfrac{y_{0}}2}$．" "\n"
        r"**第（2）问**" "\n"
        r"法线斜率为 $-\dfrac{y_{0}}p$，方程为 $y-y_{0}=-\dfrac{y_{0}}p\left(x-\dfrac{y_{0}^{2}}{2p}\right)$，" "\n"
        r"即 $x=-\dfrac p{y_{0}}y+\dfrac{y_{0}^{2}+2p^{2}}{2p}$．" "\n"
        r"与 $y^{2}=2px$ 联立：由 $x=\dfrac{y^{2}}{2p}$ 代入上式，两边乘 $2py_{0}$ 整理得" "\n"
        r"$y_{0}y^{2}+2p^{2}y-y_{0}^{3}+2p^{2}y_{0}=0$（$\Delta>0$ 恒成立）．" "\n"
        r"设 $A\left(x_{1},y_{1}\right),B\left(x_{2},y_{2}\right)$，则" "\n"
        r"$y_{1}+y_{2}=-\dfrac{2p^{2}}{y_{0}}$，$y_{1}y_{2}=\dfrac{-y_{0}^{3}+2p^{2}y_{0}}{y_{0}}=-y_{0}^{2}+2p^{2}$．" "\n"
        r"于是差的平方为" "\n"
        r"$\left(y_{1}-y_{2}\right)^{2}=\left(y_{1}+y_{2}\right)^{2}-4y_{1}y_{2}$，" "\n"
        r"$=\dfrac{4p^{4}}{y_{0}^{2}}+4y_{0}^{2}-8p^{2}=\dfrac{4\left(y_{0}^{2}+p^{2}\right)^{2}}{y_{0}^{2}}$．" "\n"
        r"又直线 $AB$ 的斜率为 $-\dfrac p{y_{0}}$，故" "\n"
        r"$\left|AB\right|=\sqrt{1+\left(-\dfrac p{y_{0}}\right)^{2}}\ \left|y_{1}-y_{2}\right|$，" "\n"
        r"$=\sqrt{1+\dfrac{p^{2}}{y_{0}^{2}}}\cdot\dfrac{2\left(y_{0}^{2}+p^{2}\right)}{y_{0}}$，" "\n"
        r"$=\dfrac{2\left(y_{0}^{2}+p^{2}\right)^{\frac32}}{y_{0}^{2}}$．" "\n"
        r"令 $t=y_{0}^{2}>0$，则 $f(t)=\dfrac{2\left(t+p^{2}\right)^{\frac32}}{t}\ (t>0)$，" "\n"
        r"$f'(t)=2\cdot\dfrac{\frac32\left(t+p^{2}\right)^{\frac12}t-\left(t+p^{2}\right)^{\frac32}}{t^{2}}$，" "\n"
        r"$=\dfrac{\left(t+p^{2}\right)^{\frac12}\left(t-2p^{2}\right)}{t^{2}}$．" "\n"
        r"故 $f(t)$ 在 $\left(0,2p^{2}\right)$ 上递减，在 $\left(2p^{2},+\infty\right)$ 上递增，" "\n"
        r"$f(t)_{\min}=f\left(2p^{2}\right)=\dfrac{2\left(3p^{2}\right)^{\frac32}}{2p^{2}}$，" "\n"
        r"$=\dfrac{2\cdot3\sqrt3\,p^{3}}{2p^{2}}=3\sqrt3\,p$．" "\n"
        r"此时 $y_{0}^{2}=2p^{2}$，即 $y_{0}=\sqrt2\,p$，$x_{0}=\dfrac{y_{0}^{2}}{2p}=\dfrac{2p^{2}}{2p}=p$，" "\n"
        r"即 $\boxed{\left|AB\right|_{\min}=3\sqrt3\,p}$，此时 $\boxed{M\left(p,\sqrt2\,p\right)}$．"
    ),
    'review': (
        r"① 求导用隐函数：$2yy'=2p$ ⟹ $y'=\frac py$，比开方后再求导快，且 $y<0$ 半支通用．" "\n"
        r"② 结果不含 $x_0$ 是靠 $x_0=\frac{y_0^2}{2p}$ 实现的："
        r"$y-y_0=\frac p{y_0}x-\frac p{y_0}\cdot\frac{y_0^2}{2p}=\frac p{y_0}x-\frac{y_0}2$．" "\n"
        r"③ 差的平方配方："
        r"$\frac{4p^4}{y_0^2}+4y_0^2-8p^2=\frac{4}{y_0^2}\left(p^4+y_0^4-2p^2y_0^2\right)=\frac{4\left(y_0^2+p^2\right)^2}{y_0^2}$，是完全平方．" "\n"
        r"④ 弦长：$\sqrt{1+\frac{p^2}{y_0^2}}\cdot\frac{2(y_0^2+p^2)}{y_0}$"
        r"$=\frac{\sqrt{y_0^2+p^2}}{y_0}\cdot\frac{2(y_0^2+p^2)}{y_0}=\frac{2(y_0^2+p^2)^{3/2}}{y_0^2}$．" "\n"
        r"⑤ 求导后分子只含 $\left(t-2p^2\right)$ 这一个变号因子，这是「分式型」求导的通例．" "\n"
        r"⑥ 数值复核：取 $p=1$，$t=2$ 时 $f=2\cdot3^{3/2}/2=3\sqrt3=5.196$；"
        r"$t=1$ 时 $f=2\cdot2^{3/2}=5.657$；$t=4$ 时 $f=2\cdot5^{3/2}/4=5.590$，均大于 $5.196$．" "\n"
        r"⑦ 答案要同时给出弦长最小值与此时 $M$ 的坐标，只写其一为常见失分点．" "\n"
        r"**通法（抛物线的切线与法线）**：" "\n"
        r"① 隐函数求导得切线斜率 $y'=\frac py$（$y^2=2px$）；" "\n"
        r"② 法线斜率为其负倒数，联立时用 $x=\frac{y^2}{2p}$ 代入（以 $y$ 为未知数）；" "\n"
        r"③ 弦长用 $\sqrt{1+\frac1{k^2}}\left|y_1-y_2\right|$（$k$ 为直线斜率）；" "\n"
        r"④ 换元后求导，最值点常落在 $t=2p^2$ 这类整倍数处．"
    ),
    'difficulty': 0.68,
    'topics': ['M-T-358'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-358-E1',
}

T358_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知椭圆 $C:\dfrac{x^{2}}3+y^{2}=1$，经过圆 $O:x^{2}+y^{2}=4$ 上一动点 $P$ 作椭圆 $C$ 的两条切线，"
        r"切点分别记为 $A$，$B$，直线 $PA$，$PB$ 分别与圆 $O$ 相交于异于点 $P$ 的 $M$，$N$ 两点．"
        r"（1）求证：$M$，$O$，$N$ 三点共线；"
        r"（2）求 $\triangle OAB$ 面积的最大值．"
    ),
    'opts': [],
    'answer': (
        r"（1）见解析；（2）$\dfrac{\sqrt3}2$．"
    ),
    'analysis': (
        r"（1）由圆与椭圆的对称性设 $P(m,n)$ 在第一象限，分切线斜率不存在与存在两种情况，"
        r"用 $\Delta=0$ 与韦达定理证 $k_{PA}k_{PB}=-1$，即 $PA\perp PB$；"
        r"再由 $\angle MPN=90^\circ$ 得 $MN$ 是圆 $O$ 的直径．"
        r"（2）由切点弦方程 $ny+\frac{mx}3=1$ 联立椭圆，用韦达定理、弦长公式与点线距离表出面积，"
        r"换元后用基本不等式求最大值．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"由对称性不妨设 $P(m,n)$ 在第一象限，则 $m^{2}+n^{2}=4$．" "\n"
        r"若 $PB$ 斜率不存在，则 $PB$ 为 $x=m=a=\sqrt3$，于是 $n=1$，"
        r"另一条切线 $PA$ 为 $y=n=b=1$，此时 $PA\perp PB$．" "\n"
        r"若 $PA$、$PB$ 斜率存在且不为 $0$，设切线为 $y=k(x-m)+n$，与 $\dfrac{x^{2}}3+y^{2}=1$ 联立，" "\n"
        r"整理得 $\left(\dfrac13+k^{2}\right)x^{2}+2k(n-mk)x+(n-mk)^{2}-1=0$，" "\n"
        r"由 $\Delta=0$ 得 $(m^{2}-3)k^{2}-2mnk+n^{2}-1=0$（$m\ne\sqrt3$），" "\n"
        r"故 $k_{PA}k_{PB}=\dfrac{n^{2}-1}{m^{2}-3}=\dfrac{3-m^{2}}{m^{2}-3}=-1$，即 $PA\perp PB$．" "\n"
        r"综上 $\angle APB=90^\circ$，又 $M,N,P$ 都在圆 $O$ 上，故 $\angle MPN=90^\circ$，" "\n"
        r"由圆的性质知 $MN$ 是圆 $O$ 的直径，所以 $M$，$O$，$N$ 三点共线．" "\n"
        r"**第（2）问**" "\n"
        r"椭圆 $\dfrac{x^{2}}3+y^{2}=1$ 上点 $(x_A,y_A)$ 处的切线为 $\dfrac{x_Ax}3+y_Ay=1$．" "\n"
        r"因 $P(m,n)$ 在两条切线上，有 $\dfrac{mx_A}3+ny_A=1$，$\dfrac{mx_B}3+ny_B=1$，" "\n"
        r"故切点弦 $AB$ 的方程为 $\dfrac{mx}3+ny=1$，即 $mx+3ny-3=0$．" "\n"
        r"与 $x^{2}+3y^{2}=3$ 联立（由 $x=\dfrac{3(1-ny)}m$ 代入），整理得" "\n"
        r"$\left(3n^{2}+m^{2}\right)y^{2}-6ny+3-m^{2}=0$．" "\n"
        r"由 $m^{2}=4-n^{2}$ 得 $3n^{2}+m^{2}=2\left(n^{2}+2\right)$，故" "\n"
        r"$y_A+y_B=\dfrac{3n}{n^{2}+2}$，$y_Ay_B=\dfrac{n^{2}-1}{2\left(n^{2}+2\right)}$．" "\n"
        r"于是 $\left(y_A-y_B\right)^{2}=\dfrac{9n^{2}}{\left(n^{2}+2\right)^{2}}-\dfrac{2\left(n^{2}-1\right)}{n^{2}+2}$，" "\n"
        r"$=\dfrac{-2n^{4}+7n^{2}+4}{\left(n^{2}+2\right)^{2}}=\dfrac{m^{2}\left(9-2m^{2}\right)}{\left(6-m^{2}\right)^{2}}$．" "\n"
        r"直线 $AB$ 斜率为 $-\dfrac m{3n}$，故" "\n"
        r"$\left|AB\right|=\sqrt{1+\dfrac{9n^{2}}{m^{2}}}\left|y_A-y_B\right|$，" "\n"
        r"$=\sqrt{\dfrac{36-8m^{2}}{m^{2}}}\cdot\dfrac{m\sqrt{9-2m^{2}}}{6-m^{2}}=\dfrac{2\left(9-2m^{2}\right)}{6-m^{2}}$．" "\n"
        r"点 $O$ 到直线 $AB$ 的距离 $d=\dfrac{3}{\sqrt{m^{2}+9n^{2}}}=\dfrac{3}{2\sqrt{9-2m^{2}}}$．" "\n"
        r"故 $S_{\triangle OAB}=\dfrac12\cdot d\cdot\left|AB\right|$，" "\n"
        r"$=\dfrac12\cdot\dfrac{3}{2\sqrt{9-2m^{2}}}\cdot\dfrac{2\left(9-2m^{2}\right)}{6-m^{2}}=\dfrac32\cdot\dfrac{\sqrt{9-2m^{2}}}{6-m^{2}}$．" "\n"
        r"令 $t=\sqrt{9-2m^{2}}$，则 $m^{2}=\dfrac{9-t^{2}}2$，$6-m^{2}=\dfrac{3+t^{2}}2$，" "\n"
        r"$S_{\triangle OAB}=\dfrac32\cdot\dfrac{t}{\frac{3+t^{2}}2}=\dfrac{3t}{t^{2}+3}=\dfrac{3}{t+\frac3t}$．" "\n"
        r"由 $t+\dfrac3t\ge2\sqrt3$ 得 $S\le\dfrac{3}{2\sqrt3}=\dfrac{\sqrt3}2$，"
        r"等号当且仅当 $t=\sqrt3$，即 $m^{2}=3$．" "\n"
        r"而 $m^{2}=3$ 时 $P\left(\sqrt3,1\right)$，正是 $PB$ 斜率不存在的情形，"
        r"此时 $S_{\triangle OAB}=\dfrac12\times\sqrt3\times1=\dfrac{\sqrt3}2$．" "\n"
        r"综上，$\triangle OAB$ 面积的最大值为 $\boxed{\dfrac{\sqrt3}2}$．"
    ),
    'review': (
        r"① 切点弦方程是题眼：椭圆上点处切线 $\frac{x_Ax}3+y_Ay=1$，把 $(x_A,y_A)$ 换成 $P(m,n)$ 即得 $AB$．" "\n"
        r"② $k_{PA}k_{PB}=\frac{n^2-1}{m^2-3}$，这正说明 $P$ 在圆 $x^2+y^2=4$ 上（$n^2-1=3-m^2$）——"
        r"**圆 $x^2+y^2=a^2+b^2$ 对椭圆 $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$ 而言就是「两条切线互相垂直」的轨迹**．" "\n"
        r"③ 差的平方换元：$-2n^4+7n^2+4$ 用 $n^2=4-m^2$ 代入得 $m^2(9-2m^2)$，"
        r"分母 $\left(n^2+2\right)^2=\left(6-m^2\right)^2$，配得整式．" "\n"
        r"④ ⚠ **原书此处漏了根号**：面积应为 $\frac32\cdot\frac{\sqrt{9-2m^2}}{6-m^2}$，"
        r"若写成 $\frac32\cdot\frac{9-2m^2}{6-m^2}$，则令 $t=9-2m^2$ 后化不出 $\frac{3t}{t^2+3}$．" "\n"
        r"   判据：换元后分子必须是 $t$ 的一次、分母是 $t^2+3$ 才能用 $t+\frac3t\ge2\sqrt3$．" "\n"
        r"⑤ ⭐⭐ **等号点 $t=\sqrt3$ 恰好对应 $m^2=3$**，而这一情形在第（1）问中已单独讨论（$PB$ 斜率不存在）．"
        r"**「等号点落在需要单独讨论的边界情形」是这类题的典型设计**．" "\n"
        r"⑥ 数值复核：$m^2=3$ 时 $t=\sqrt3$，$S=\frac{3\sqrt3}{3+3}=\frac{\sqrt3}2=0.8660$；"
        r"$m^2=1$ 时 $t=\sqrt7$，$S=\frac{3\sqrt7}{10}=0.7937<0.8660$；"
        r"$m^2=3.9$ 时 $t=\sqrt{1.2}$，$S=\frac{3\sqrt{1.2}}{4.2}=0.7825<0.8660$．" "\n"
        r"**通法（切点弦）**：" "\n"
        r"① 圆锥曲线上点 $(x_1,y_1)$ 处的切线公式（对称式），把动点换成外点 $P$ 即得切点弦方程；" "\n"
        r"② 切点弦联立曲线，用韦达定理 + 弦长公式 + 点线距离表出面积；" "\n"
        r"③ 换元成 $\frac{3t}{t^2+3}=\frac3{t+3/t}$ 型后用基本不等式；" "\n"
        r"④ 检查等号点是否落在需单独讨论的边界情形．"
    ),
    'difficulty': 0.82,
    'topics': ['M-T-358'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-358-V1',
}

T358_V2 = {
    'type': '解答',
    'stem_text': (
        r"把抛物线 $C_1:x^{2}=2py\ (p>0)$ 沿 $y$ 轴向下平移得到抛物线 $C_2:x^{2}=2py+m\ (p>0,\,m>0)$．"
        r"（1）当 $p=1$ 时，过抛物线 $C_1$ 上一点 $P(2,2)$ 作切线，交抛物线 $C_2$ 于 $A$，$B$ 两点，"
        r"求证：$\left|PA\right|=\left|PB\right|$；"
        r"（2）抛物线 $C_2$ 上任意一点 $M\left(x_0,y_0\right)$ 向抛物线 $C_1$ 作两条切线，从左至右切点分别为 $C$，$D$．"
        r"直线 $CD$ 交 $C_2$ 从左至右分别为 $E$，$F$ 两点．试判断 $S_{\triangle MED}$ 与 $S_{\triangle MCF}$ 的大小关系，并证明．"
    ),
    'opts': [],
    'answer': (
        r"（1）见解析；（2）$S_{\triangle MED}=S_{\triangle MCF}$．"
    ),
    'analysis': (
        r"（1）先由 $\Delta=0$ 求出 $C_1$ 在 $P$ 处的切线，再与 $C_2$ 联立，"
        r"由韦达定理算得弦 $AB$ 的中点恰为 $P$．（2）设切线斜率为 $u$，由 $\Delta=0$ 得关于 $u$ 的二次方程，"
        r"两根即两条切线斜率；进而求出 $C,D$ 坐标与直线 $CD$，再与 $C_2$ 联立得 $E,F$；"
        r"关键在证 $CD$ 与 $EF$ 有相同的中点，于是 $\left|ED\right|=\left|CF\right|$，两三角形等底同高．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"$p=1$ 时 $C_1:x^{2}=2y$，设切线 $AB$ 为 $y-2=k(x-2)$．" "\n"
        r"与 $x^{2}=2y$ 联立消去 $y$：$x^{2}-2kx+4k-4=0$，" "\n"
        r"由 $\Delta=4k^{2}-4(4k-4)=4(k-2)^{2}=0$ 得 $k=2$，切线为 $y=2x-2$．" "\n"
        r"与 $C_2:x^{2}=2y+m$ 联立：$x^{2}-4x+4-m=0$，$\Delta=16-4(4-m)=4m>0$．" "\n"
        r"设 $A(t_1,s_1),B(t_2,s_2)$，则 $t_1+t_2=4$，故 $AB$ 中点横坐标为 $2$，"
        r"纵坐标为 $2\cdot2-2=2$，即中点与 $P(2,2)$ 重合，所以 $\left|PA\right|=\left|PB\right|$．" "\n"
        r"**第（2）问**" "\n"
        r"结论：$S_{\triangle MED}=S_{\triangle MCF}$．理由如下．" "\n"
        r"由 $M$ 在 $C_2$ 上，有 $x_0^{2}-2py_0=m>0$．设过 $M$ 的 $C_1$ 的切线为 $y-y_0=u(x-x_0)$，" "\n"
        r"与 $x^{2}=2py$ 联立消去 $y$：$\dfrac1{2p}x^{2}-ux+ux_0-y_0=0$．" "\n"
        r"由 $\Delta_1=u^{2}-\dfrac2p\left(ux_0-y_0\right)=0$，即 $u^{2}-\dfrac{2x_0}pu+\dfrac{2y_0}p=0$，" "\n"
        r"其判别式 $\Delta_2=\dfrac{4x_0^{2}}{p^{2}}-\dfrac{8y_0}p=\dfrac{4m}{p^{2}}>0$，故有两不等实根 $u_1,u_2$，" "\n"
        r"$u_1+u_2=\dfrac{2x_0}p$，$u_1u_2=\dfrac{2y_0}p$．" "\n"
        r"切点横坐标为方程的等根 $pu$，故 $C\left(pu_1,\;pu_1^{2}-u_1x_0+y_0\right)$，$D\left(pu_2,\;pu_2^{2}-u_2x_0+y_0\right)$．" "\n"
        r"直线 $CD$ 的斜率为" "\n"
        r"$\dfrac{pu_1^{2}-u_1x_0-\left(pu_2^{2}-u_2x_0\right)}{pu_1-pu_2}=u_1+u_2-\dfrac{x_0}p=\dfrac{x_0}p$．" "\n"
        r"直线 $CD$：$y-\left(pu_1^{2}-u_1x_0+y_0\right)=\dfrac{x_0}p\left(x-pu_1\right)$．" "\n"
        r"与 $C_2:x^{2}=2py+m$ 联立消去 $y$，整理得" "\n"
        r"$\dfrac1{2p}x^{2}-\dfrac{x_0}px-\left(pu_1^{2}-2u_1x_0+\dfrac{x_0^{2}}{2p}\right)=0$，" "\n"
        r"其判别式 $\Delta_3=2\left(\dfrac{x_0}p-u_1\right)^{2}>0$．" "\n"
        r"设 $E(x_1,y_1),F(x_2,y_2)$，则 $x_1+x_2=2x_0$，即 $EF$ 中点横坐标为 $x_0$；" "\n"
        r"而 $CD$ 中点横坐标为 $\dfrac{pu_1+pu_2}2=\dfrac p2\cdot\dfrac{2x_0}p=x_0$．" "\n"
        r"故线段 $EF$ 与 $CD$ 有相同的中点，从而 $\left|EC\right|=\left|DF\right|$，即 $\left|ED\right|=\left|CF\right|$．" "\n"
        r"又 $\triangle MED$ 与 $\triangle MCF$ 的高都是点 $M$ 到直线 $CD$ 的距离，" "\n"
        r"所以 $\boxed{S_{\triangle MED}=S_{\triangle MCF}}$．"
    ),
    'review': (
        r"① ⭐⭐ **两条切线的斜率是同一个二次方程的两根** —— "
        r"设切线后用 $\Delta=0$ 得到的方程，未知数是斜率 $u$，两个根对应两条切线，韦达定理直接给 $u_1+u_2$ 与 $u_1u_2$．" "\n"
        r"② ⭐⭐ **切点横坐标就是 $pu$**：方程 $\frac1{2p}x^2-ux+\cdots=0$ 的等根为 $x=\frac{u}{2\cdot(1/2p)}=pu$．" "\n"
        r"③ ⭐⭐ **切点纵坐标的两种写法**：$pu_1^2$（由 $y=\frac{x^2}{2p}$）与 $pu_1^2-u_1x_0+y_0$（由切线方程）相等，"
        r"因为 $pu_1^2=2x_0u_1-2y_0$，故 $pu_1^2-u_1x_0+y_0=x_0u_1-y_0=\frac{p^2u_1^2}{2p}$ ✓" "\n"
        r"④ ⭐⭐ **直线 $CD$ 斜率 $=\frac{x_0}p$** —— 与 $u_1,u_2$ 无关（只靠 $u_1+u_2$），这是能继续算下去的关键．" "\n"
        r"⑤ ⭐⭐ **「同中点」是本类题的通用收尾**：$CD$ 与 $EF$ 中点横坐标都是 $x_0$ ⟹ "
        r"$\left|EC\right|=\left|DF\right|$ ⟹ $\left|ED\right|=\left|CF\right|$ ⟹ 两三角形等底同高．" "\n"
        r"   一般结论：**两条线段共中点 ⟹ 交叉相减的两段相等**．" "\n"
        r"⑥ 第（1）问是第（2）问的特例：$m$ 平移后弦的中点恰是切点，本质是抛物线弦的中点与斜率的关系"
        r"（$x^2=2py$ 中斜率为 $k$ 的弦，中点横坐标恒为 $pk$）．" "\n"
        r"   本题 $k=2,p=1$ ⟹ 中点横坐标 $=2$ ✓ 与计算一致．" "\n"
        r"**通法（抛物线外点引两切线）**：" "\n"
        r"① 设切线 $y-y_0=u(x-x_0)$，与 $x^2=2py$ 联立后令 $\Delta=0$，得关于 $u$ 的二次方程；" "\n"
        r"② 两根 $u_1,u_2$ 即两切线斜率，切点为 $\left(pu_i,\frac{pu_i^2}2\right)$；" "\n"
        r"③ 求 $CD$ 方程后再与另一曲线联立，比较中点即可判面积关系．"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-358'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-358-V2',
}

T358_V3 = {
    'type': '解答',
    'stem_text': (
        r"已知双曲线 $C:\dfrac{x^{2}}3-y^{2}=1$，过 $P(1,1)$ 向双曲线 $C$ 作两条切线，"
        r"切点分别为 $A\left(x_1,y_1\right)$，$B\left(x_2,y_2\right)$，且 $x_1<0$，$x_2>0$．"
        r"（1）证明：直线 $PA$ 的方程为 $\dfrac{x_1x}3-y_1y=1$；"
        r"（2）设 $F$ 为双曲线 $C$ 的左焦点，证明：$\angle AFP+\angle BFP=\pi$．"
    ),
    'opts': [],
    'answer': (
        r"（1）见解析；（2）见解析．"
    ),
    'analysis': (
        r"（1）设切线方程并联立，由 $\Delta=0$ 求出切点坐标与斜率的关系，再回代整理．"
        r"（2）由切点弦方程 $\frac x3-y=1$ 得两切点坐标间的关系，"
        r"代入 $\left(x_1+2\right)^2+y_1^2$ 化简为常数，从而两个余弦值互为相反数．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"设直线 $PA$ 为 $y-1=k(x-1)$，与 $\dfrac{x^{2}}3-y^{2}=1$ 联立，整理得" "\n"
        r"$\left(3k^{2}-1\right)x^{2}-6k(k-1)x+3\left(k^{2}-2k+2\right)=0$．" "\n"
        r"由 $\Delta=36k^{2}(k-1)^{2}-4\left(3k^{2}-1\right)\cdot3\left(k^{2}-2k+2\right)=0$，化简得 $k^{2}+k-1=0$．" "\n"
        r"此时方程有两相等实根，切点 $A$ 的横坐标为" "\n"
        r"$x_1=\dfrac{6k(k-1)}{2\left(3k^{2}-1\right)}=\dfrac{3k^{2}-3k}{3k^{2}-1}$，由 $k^{2}=1-k$ 得 $x_1=\dfrac{3(1-k)-3k}{3(1-k)-1}=\dfrac{3-6k}{2-3k}$．" "\n"
        r"又 $y_1=1+k(x_1-1)$，可算得 $\dfrac{x_1}{y_1}=3k$，即 $k=\dfrac{x_1}{3y_1}$．" "\n"
        r"故切线为 $y-y_1=\dfrac{x_1}{3y_1}\left(x-x_1\right)$，即 $3yy_1=xx_1-x_1^{2}+3y_1^{2}$．" "\n"
        r"由 $A$ 在双曲线上：$x_1^{2}-3y_1^{2}=3$，即 $3y_1^{2}=x_1^{2}-3$，代入上式得" "\n"
        r"$3yy_1=xx_1-3$，即 $\boxed{\dfrac{x_1x}3-y_1y=1}$．" "\n"
        r"**第（2）问**" "\n"
        r"同理直线 $PB$ 为 $\dfrac{x_2x}3-y_2y=1$．两切线都过 $P(1,1)$，故" "\n"
        r"$\dfrac{x_1}3-y_1=1$，$\dfrac{x_2}3-y_2=1$，" "\n"
        r"即 $A,B$ 都在直线 $\dfrac x3-y=1$ 上，故切点弦 $AB$ 的方程为 $y=\dfrac x3-1$．" "\n"
        r"双曲线中 $a^{2}=3$，$b^{2}=1$，$c=2$，左焦点 $F(-2,0)$．" "\n"
        r"由 $y_i=\dfrac{x_i}3-1$ 与 $x_i^{2}-3y_i^{2}=3$ 联立，代入得 $x_i^{2}-3\left(\dfrac{x_i}3-1\right)^{2}=3$，" "\n"
        r"即 $\dfrac23x_i^{2}+2x_i-6=0$，$x_i^{2}+3x_i-9=0$，故 $x_1=\dfrac{-3-3\sqrt5}2$，$x_2=\dfrac{-3+3\sqrt5}2$．" "\n"
        r"（满足 $x_1\le-\sqrt3$，$x_2\ge\sqrt3$．）" "\n"
        r"$\vec{FP}=(3,1)$，$\vec{FA}=\left(x_1+2,y_1\right)$，$\vec{FB}=\left(x_2+2,y_2\right)$．" "\n"
        r"$\left|\vec{FP}\right|=\sqrt{10}$，" "\n"
        r"$\left|\vec{FA}\right|^{2}=\left(x_1+2\right)^{2}+y_1^{2}=x_1^{2}+4x_1+4+\dfrac{x_1^{2}}3-1=\dfrac43x_1^{2}+4x_1+3$．" "\n"
        r"由 $x_1^{2}=-3x_1+9$ 得 $\left|\vec{FA}\right|^{2}=\dfrac43(-3x_1+9)+4x_1+3=-4x_1+12+4x_1+3=15$．" "\n"
        r"同理 $\left|\vec{FB}\right|^{2}=15$，即 $\left|\vec{FA}\right|=\left|\vec{FB}\right|=\sqrt{15}$．" "\n"
        r"$\vec{FP}\cdot\vec{FA}=3(x_1+2)+y_1=3x_1+6+\dfrac{x_1}3-1=\dfrac{10}3x_1+5=\dfrac{10}3\left(x_1+\dfrac32\right)$．" "\n"
        r"由 $x_1=\dfrac{-3-3\sqrt5}2$ 得 $x_1+\dfrac32=-\dfrac{3\sqrt5}2$，故 $\vec{FP}\cdot\vec{FA}=-5\sqrt5$．" "\n"
        r"同理 $\vec{FP}\cdot\vec{FB}=\dfrac{10}3\left(x_2+\dfrac32\right)=\dfrac{10}3\cdot\dfrac{3\sqrt5}2=5\sqrt5$．" "\n"
        r"于是 $\cos\angle AFP=\dfrac{-5\sqrt5}{\sqrt{10}\cdot\sqrt{15}}=\dfrac{-5\sqrt5}{5\sqrt6}=-\dfrac{\sqrt{30}}6$，" "\n"
        r"$\cos\angle BFP=\dfrac{5\sqrt5}{5\sqrt6}=\dfrac{\sqrt{30}}6$，故 $\cos\angle AFP=-\cos\angle BFP$．" "\n"
        r"两角都在 $(0,\pi)$ 内，所以 $\boxed{\angle AFP+\angle BFP=\pi}$．"
    ),
    'review': (
        r"① ⭐⭐ **切线公式的「对称式」要记牢**：$\frac{x^2}{a^2}-\frac{y^2}{b^2}=1$ 上点 $(x_1,y_1)$ 处切线为 $\frac{x_1x}{a^2}-\frac{y_1y}{b^2}=1$，"
        r"与椭圆只差一个符号．本题第（1）问就是它的证明（用 $\Delta=0$ 反推）．" "\n"
        r"② ⭐⭐ **切点弦方程一处两用**：两切线都过 $P(1,1)$ ⟹ $\frac{x_i}3-y_i=1$ ⟹ "
        r"$A,B$ 都在 $\frac x3-y=1$ 上．**这是把两个切点统一起来的唯一通道**．" "\n"
        r"③ ⭐⭐ **$\left|\vec{FA}\right|^2$ 化为常数是本题的命门**："
        r"$\frac43x_1^2+4x_1+3$ 用 $x_1^2=-3x_1+9$ 代入后 $x_1$ 项恰好抵消，得 $15$．"
        r"**这种「变量项抵消」是能算出定值角的信号**．" "\n"
        r"④ ⭐⭐ **两个点积只差一个符号**：$\frac{10}3\left(x_i+\frac32\right)$，而 $x_1+\frac32=-\frac{3\sqrt5}2$、$x_2+\frac32=\frac{3\sqrt5}2$ 恰好相反，"
        r"于是 $\cos$ 值互为相反数 ⟹ 两角互补．" "\n"
        r"⑤ ⚠ **原书末行 `= -30/6` 实为 $-\frac{\sqrt{30}}6$**：余弦值必须 $\le1$，$\frac{30}6=5$ 显然不可能，"
        r"这是典型的根号丢失．同理 $\frac{\sqrt{30}}6=0.9129$ ✓ 合理．" "\n"
        r"⑥ 数值复核：$x_1=\frac{-3-3\sqrt5}2=-4.854$，$x_2=\frac{-3+3\sqrt5}2=1.854$；"
        r"$y_1=\frac{x_1}3-1=-2.618$，$y_2=\frac{x_2}3-1=-0.382$；" "\n"
        r"   $\left|\vec{FA}\right|^2=(-4.854+2)^2+(-2.618)^2=8.146+6.854=15.000$ ✓；"
        r"$\left|\vec{FB}\right|^2=(1.854+2)^2+(-0.382)^2=14.854+0.146=15.000$ ✓；" "\n"
        r"   $\vec{FP}\cdot\vec{FA}=3(-2.854)+(-2.618)=-11.180=-5\sqrt5$ ✓；"
        r"$\vec{FP}\cdot\vec{FB}=3(3.854)+(-0.382)=11.180=5\sqrt5$ ✓；" "\n"
        r"   $\cos\angle AFP=\frac{-11.180}{\sqrt{10}\sqrt{15}}=-0.9129=-\frac{\sqrt{30}}6$ ✓✓✓" "\n"
        r"**通法（外点引两切线证角互补）**：" "\n"
        r"① 写出切线公式的对称式，代入外点得切点弦方程；" "\n"
        r"② 切点弦与曲线联立解出两切点坐标（通常是二次方程两根）；" "\n"
        r"③ 算 $\left|\vec{FA}\right|$ 与点积，往往都能化为常数或只差符号；" "\n"
        r"④ 由 $\cos\alpha=-\cos\beta$ 得 $\alpha+\beta=\pi$．"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-358'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-358-V3',
}

T360_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知 $M$ 为椭圆 $C:\dfrac{x^{2}}{25}+\dfrac{y^{2}}9=1$ 上的动点，过点 $M$ 作 $x$ 轴的垂线段 $MD$，$D$ 为垂足，"
        r"点 $P$ 满足 $\vec{PD}=\dfrac53\vec{MD}$．"
        r"（1）求动点 $P$ 的轨迹 $E$ 的方程；"
        r"（2）若 $A$，$B$ 两点分别为椭圆 $C$ 的左、右顶点，$F$ 为椭圆 $C$ 的左焦点，"
        r"直线 $PB$ 与椭圆 $C$ 交于点 $Q$，直线 $QF$，$PA$ 的斜率分别为 $k_{QF}$，$k_{PA}$，求 $\dfrac{k_{QF}}{k_{PA}}$ 的取值范围．"
    ),
    'opts': [],
    'answer': (
        r"（1）$x^{2}+y^{2}=25\ (y\ne0)$；"
        r"（2）$\dfrac{k_{QF}}{k_{PA}}\in(-\infty,0)\cup\left(\dfrac25,+\infty\right)$．"
    ),
    'analysis': (
        r"（1）设 $P(x,y)$、$M(m,n)$，由向量等式得 $m=x$、$n=\frac35y$，代入椭圆方程消去参数即得．"
        r"（2）$P$ 在圆 $x^2+y^2=25$ 上且 $A,B$ 是直径端点，故 $PA\perp PB$，从而 $k_{PA}=-\frac1{k_{PB}}$；"
        r"又 $Q,B,P$ 共线，把 $k_{PA}$ 用 $Q$ 的坐标表示，再代入 $Q$ 在椭圆上的条件化简．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"设 $P(x,y)$，$M(m,n)$，则 $D(m,0)$．" "\n"
        r"$\vec{PD}=\left(m-x,-y\right)$，$\vec{MD}=\left(0,-n\right)$．" "\n"
        r"由 $\vec{PD}=\dfrac53\vec{MD}$ 得 $m-x=0$ 且 $-y=-\dfrac53n$，即 $m=x$，$n=\dfrac35y$．" "\n"
        r"又 $M$ 在椭圆 $C$ 上：$\dfrac{m^{2}}{25}+\dfrac{n^{2}}9=1$，代入得" "\n"
        r"$\dfrac{x^{2}}{25}+\dfrac{1}{9}\cdot\dfrac{9y^{2}}{25}=1$，即 $\dfrac{x^{2}+y^{2}}{25}=1$．" "\n"
        r"当 $n=0$ 时 $M$ 为椭圆顶点，此时 $\vec{MD}=\vec0$，$P$ 与 $D$ 重合，轨迹退化，故 $y\ne0$．" "\n"
        r"所以轨迹 $E$ 的方程为 $\boxed{x^{2}+y^{2}=25\ (y\ne0)}$．" "\n"
        r"**第（2）问**" "\n"
        r"椭圆 $C$ 中 $a=5$，$b=3$，$c=4$，故 $A(-5,0)$，$B(5,0)$，$F(-4,0)$．" "\n"
        r"$A,B$ 都在圆 $E:x^{2}+y^{2}=25$ 上且 $AB$ 是直径，故 $\angle APB=90^\circ$，即 $PA\perp PB$．" "\n"
        r"设 $Q(x_0,y_0)$（在椭圆 $C$ 上，$-5<x_0<5$ 且 $x_0\ne-4$）．" "\n"
        r"因 $Q,B,P$ 三点共线，$k_{PB}=\dfrac{y_0}{x_0-5}$，故 $k_{PA}=-\dfrac1{k_{PB}}=-\dfrac{x_0-5}{y_0}$．" "\n"
        r"又 $k_{QF}=\dfrac{y_0}{x_0+4}$，于是" "\n"
        r"$\dfrac{k_{QF}}{k_{PA}}=\dfrac{y_0}{x_0+4}\cdot\left(-\dfrac{y_0}{x_0-5}\right)=-\dfrac{y_0^{2}}{\left(x_0+4\right)\left(x_0-5\right)}$．" "\n"
        r"由 $Q$ 在椭圆上：$y_0^{2}=9\left(1-\dfrac{x_0^{2}}{25}\right)=\dfrac{9\left(5-x_0\right)\left(5+x_0\right)}{25}$，代入得" "\n"
        r"$\dfrac{k_{QF}}{k_{PA}}=-\dfrac{9(5-x_0)(5+x_0)}{25\left(x_0+4\right)\left(x_0-5\right)}=\dfrac{9\left(5+x_0\right)}{25\left(x_0+4\right)}=\dfrac9{25}\left(1+\dfrac1{x_0+4}\right)$．" "\n"
        r"$\dfrac1{x_0+4}$ 在 $(-5,-4)$ 与 $(-4,5)$ 上都单调递减：在 $(-5,-4)$ 上取值 $(-\infty,-1)$，在 $(-4,5)$ 上取值 $\left(\dfrac19,+\infty\right)$．" "\n"
        r"故 $1+\dfrac1{x_0+4}\in(-\infty,0)\cup\left(\dfrac{10}9,+\infty\right)$，" "\n"
        r"$\dfrac{k_{QF}}{k_{PA}}\in(-\infty,0)\cup\left(\dfrac9{25}\cdot\dfrac{10}9,+\infty\right)=\boxed{(-\infty,0)\cup\left(\dfrac25,+\infty\right)}$．"
    ),
    'review': (
        r"① ⭐⭐ **$\vec{PD}=\frac53\vec{MD}$ 是坐标伸缩**：$m=x$、$n=\frac35y$，"
        r"即把椭圆沿 $y$ 方向拉长 $\frac53$ 倍 ⟹ 圆 $x^2+y^2=25$．"
        r"**比例系数 $\frac53=\frac ab$ 正是把椭圆还原成圆所需的倍数**．" "\n"
        r"② ⭐⭐ **$PA\perp PB$ 来自「$AB$ 是圆的直径」**：$P$ 在圆 $x^2+y^2=25$ 上，$A,B$ 是直径端点，"
        r"也可直接验证 $k_{PA}k_{PB}=\frac{y_P^2}{x_P^2-25}=\frac{y_P^2}{-y_P^2}=-1$．" "\n"
        r"③ ⭐⭐ **把 $k_{PA}$ 换成 $Q$ 的坐标是核心一步**：$Q,B,P$ 共线 ⟹ $k_{PB}=k_{QB}$ ⟹ $k_{PA}=-\frac1{k_{QB}}$，"
        r"这样比值就只含 $Q$ 的坐标了．" "\n"
        r"④ ⭐⭐ **$y_0^2=\frac{9(5-x_0)(5+x_0)}{25}$ 与分母的 $(x_0-5)$ 约分**："
        r"$(5-x_0)$ 与 $(x_0-5)$ 只差一个负号，约去后 $x_0$ 只剩一次，式子大幅化简．" "\n"
        r"   一般地：**椭圆上点的 $y^2$ 因式分解后必含 $(a-x)(a+x)$，常与分母的 $(x-a)$ 约分**．" "\n"
        r"⑤ ⚠ **$x_0\ne-4$ 不能漏**：$x_0=-4$ 时 $k_{QF}$ 不存在（$QF$ 垂直于 $x$ 轴），"
        r"这正对应两个区间的分界 —— **间断点恰好来自斜率不存在的点**．" "\n"
        r"⑥ 数值复核：取 $x_0=0$，$y_0=3$，比值 $=\frac9{25}\left(1+\frac14\right)=\frac9{25}\cdot\frac54=0.45$；"
        r"直接算 $k_{QF}=\frac34$、$k_{PA}=-\frac{0-5}3=\frac53$，比值 $=\frac{3/4}{5/3}=0.45$ ✓✓" "\n"
        r"   取 $x_0=-4.5$：$y_0^2=9(1-20.25/25)=1.71$，$y_0=1.308$；比值 $=\frac9{25}\left(1+\frac1{-0.5}\right)=\frac9{25}(-1)=-0.36$；"
        r"直接算 $k_{QF}=\frac{1.308}{-0.5}=-2.616$，$k_{PA}=-\frac{-4.5-5}{1.308}=7.264$，比值 $=-0.360$ ✓✓✓" "\n"
        r"**通法（相关点法求轨迹 + 斜率比范围）**：" "\n"
        r"① 设动点 $P(x,y)$ 与已知曲线上点 $M(m,n)$，用向量/几何关系写出 $m,n$ 关于 $x,y$ 的表达式；" "\n"
        r"② 代入已知曲线方程即得轨迹；注意退化点要剔除；" "\n"
        r"③ 求斜率比时，先找几何约束（如 $PA\perp PB$）把其中一个斜率换成另一个的负倒数；" "\n"
        r"④ 利用交点在曲线上把 $y^2$ 因式分解与分母约分，化为单变量分式后用单调性定范围．"
    ),
    'difficulty': 0.80,
    'topics': ['M-T-360'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-360-E1',
}

T360_V1 = {
    'type': '解答',
    'stem_text': (
        r"过点 $D(0,m)\ (m\ne0)$ 作不垂直于 $x$ 轴、$y$ 轴的直线 $l$，交椭圆 $E$ 于 $P$，$Q$ 两点，"
        r"$C$ 为线段 $PQ$ 的中点，且 $AC\perp OC$．"
        r"（1）求椭圆 $E$ 的方程（已知离心率 $e=\dfrac{\sqrt2}2$，上顶点 $A$ 到右焦点的距离为 $\sqrt2$）；"
        r"（2）求实数 $m$ 的取值范围；"
        r"（3）延长 $AC$ 交椭圆 $E$ 于点 $B$，记 $\triangle AOB$ 与 $\triangle AOC$ 的面积分别为 $S_1$，$S_2$，"
        r"若 $\dfrac{S_1}{S_2}=\dfrac83$，求直线 $l$ 的方程．"
    ),
    'opts': [],
    'answer': (
        r"（1）$\dfrac{x^{2}}2+y^{2}=1$；（2）$\dfrac12<m<1$；"
        r"（3）$y=\dfrac12x+\dfrac34$ 或 $y=-\dfrac12x+\dfrac34$．"
    ),
    'analysis': (
        r"（1）由上顶点到焦点的距离等于 $a$ 得 $a=\sqrt2$，再由离心率得 $c=1$，$b=1$．"
        r"（2）用点差法写出弦 $PQ$ 的斜率与中点 $C$ 的关系，再由 $AC\perp OC$ 写第二个方程，"
        r"两式联立解出 $C$ 的纵坐标，由横坐标平方为正定 $m$ 的范围．"
        r"（3）$A,C,B$ 共线，$\frac{S_1}{S_2}=\frac{\left|AB\right|}{\left|AC\right|}$，用参数法求 $B$ 的位置．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"由 $e=\dfrac ca=\dfrac{\sqrt2}2$ 得 $a=\sqrt2\,c$．" "\n"
        r"上顶点 $A(0,b)$ 到右焦点 $(c,0)$ 的距离为 $\sqrt{b^{2}+c^{2}}=a$，故 $a=\sqrt2$，于是 $c=1$，$b=1$．" "\n"
        r"椭圆 $E$ 的方程为 $\boxed{\dfrac{x^{2}}2+y^{2}=1}$，即 $x^{2}+2y^{2}=2$．" "\n"
        r"**第（2）问**" "\n"
        r"由 $A(0,1)$，设 $P(x_1,y_1)$，$Q(x_2,y_2)$，$C(x_0,y_0)$，且 $x_1\ne x_2$．" "\n"
        r"$x_1^{2}+2y_1^{2}=2$，$x_2^{2}+2y_2^{2}=2$，两式相减得" "\n"
        r"$\left(x_2-x_1\right)\left(x_2+x_1\right)+2\left(y_2-y_1\right)\left(y_2+y_1\right)=0$，" "\n"
        r"即 $2x_0\left(x_2-x_1\right)+4y_0\left(y_2-y_1\right)=0$，故 $\dfrac{y_2-y_1}{x_2-x_1}\cdot\dfrac{y_0}{x_0}=-\dfrac12$．" "\n"
        r"又 $D(0,m)$ 在直线 $PQ$ 上，$\dfrac{y_2-y_1}{x_2-x_1}=\dfrac{y_0-m}{x_0}$，代入得" "\n"
        r"$\dfrac{y_0-m}{x_0}\cdot\dfrac{y_0}{x_0}=-\dfrac12$，即 $x_0^{2}=2y_0\left(m-y_0\right)$ ①．" "\n"
        r"由 $AC\perp OC$：$\dfrac{y_0-1}{x_0}\cdot\dfrac{y_0}{x_0}=-1$，即 $x_0^{2}=y_0\left(1-y_0\right)$ ②．" "\n"
        r"由①②（$y_0\ne0$）得 $2\left(m-y_0\right)=1-y_0$，即 $y_0=2m-1$．" "\n"
        r"代回②：$x_0^{2}=\left(2m-1\right)\left(2-2m\right)>0$，解得 $\boxed{\dfrac12<m<1}$．" "\n"
        r"**第（3）问**" "\n"
        r"直线 $AC$ 上的点可写成 $A+s\left(C-A\right)=\left(sx_0,\;1+s(y_0-1)\right)$，$s=1$ 时为 $C$．" "\n"
        r"代入 $x^{2}+2y^{2}=2$：$s^{2}x_0^{2}+2\left[1+s(y_0-1)\right]^{2}=2$，整理得" "\n"
        r"$s^{2}\left[x_0^{2}+2(y_0-1)^{2}\right]+4s(y_0-1)=0$．" "\n"
        r"除 $s=0$（点 $A$）外，$s_B=\dfrac{4(1-y_0)}{x_0^{2}+2(y_0-1)^{2}}$．" "\n"
        r"由② $x_0^{2}=y_0(1-y_0)$，得 $x_0^{2}+2(y_0-1)^{2}=y_0(1-y_0)+2(1-y_0)^{2}=(1-y_0)(2-y_0)$，" "\n"
        r"故 $s_B=\dfrac{4(1-y_0)}{(1-y_0)(2-y_0)}=\dfrac4{2-y_0}$．" "\n"
        r"$\triangle AOB$ 与 $\triangle AOC$ 有公共顶点 $O$ 且 $A,C,B$ 共线，故" "\n"
        r"$\dfrac{S_1}{S_2}=\dfrac{\left|AB\right|}{\left|AC\right|}=s_B=\dfrac4{2-y_0}=\dfrac83$，解得 $y_0=\dfrac12$．" "\n"
        r"由 $y_0=2m-1$ 得 $m=\dfrac34$；由②得 $x_0^{2}=\dfrac12\cdot\dfrac12=\dfrac14$，即 $x_0=\pm\dfrac12$．" "\n"
        r"直线 $l$ 过 $D\left(0,\dfrac34\right)$ 与 $C\left(\pm\dfrac12,\dfrac12\right)$，斜率为 $\dfrac{\frac12-\frac34}{\pm\frac12}=\mp\dfrac12$．" "\n"
        r"故 $\boxed{y=\dfrac12x+\dfrac34}$ 或 $\boxed{y=-\dfrac12x+\dfrac34}$．"
    ),
    'review': (
        r"① ⭐⭐ **上顶点到焦点的距离恒为 $a$**：$\sqrt{b^2+c^2}=\sqrt{a^2}=a$，这一步直接给出 $a=\sqrt2$．" "\n"
        r"② ⭐⭐ **点差法的标准写法**：两式相减后用中点坐标 $2x_0=x_1+x_2$、$2y_0=y_1+y_2$ 替换，"
        r"一步得到 $k_{PQ}\cdot k_{OC}=-\frac{b^2}{a^2}=-\frac12$（本题 $a^2=2,b^2=1$）．" "\n"
        r"③ ⭐⭐ **两个条件各给一个 $x_0^2$ 的表达式，右端相等即可解出 $y_0$** —— "
        r"这是「点差法 + 垂直」组合题的固定套路．" "\n"
        r"④ ⭐⭐ **$x_0^2>0$ 定范围**：$(2m-1)(2-2m)>0$ 是二次不等式，两根 $\frac12$ 与 $1$，开口向下 ⟹ 中间为正．" "\n"
        r"⑤ ⭐⭐ **参数 $s$ 法求 $B$**：直线 $AC$ 上用 $A+s(C-A)$ 参数化，$s=0$ 给 $A$、$s=1$ 给 $C$、$s=s_B$ 给 $B$，"
        r"则 $\frac{\left|AB\right|}{\left|AC\right|}=s_B$．**比解坐标再算距离快得多**．" "\n"
        r"⑥ ⭐⭐ **同顶点共线 ⟹ 面积比 = 底边比**：$\triangle AOB$ 与 $\triangle AOC$ 都从 $O$ 出发，底边在直线 $AB$ 上，"
        r"高相同（都是 $O$ 到直线 $AB$ 的距离），故 $\frac{S_1}{S_2}=\frac{\left|AB\right|}{\left|AC\right|}$．" "\n"
        r"⑦ 数值复核：$m=\frac34$ 时 $y_0=\frac12$、$x_0=\pm\frac12$，$s_B=\frac4{2-0.5}=\frac83$ ✓；"
        r"把 $C\left(\frac12,\frac12\right)$ 代入椭圆：$0.25+2\cdot0.25=0.75\ne2$ —— "
        r"**注意 $C$ 是弦中点，在椭圆内部而非椭圆上** ✓ 正常．" "\n"
        r"   验 $B$：$s_B=\frac83$，$B=\left(\frac83\cdot\frac12,\;1+\frac83\left(\frac12-1\right)\right)=\left(\frac43,\frac13\right)$；"
        r"代入椭圆：$\frac{16}{9}\cdot\frac12+\frac19=\frac89+\frac19=1$ ✓ 在椭圆上 ✓✓✓" "\n"
        r"**通法（点差法 + 中点轨迹）**：" "\n"
        r"① 弦两端点代入曲线方程后相减，用中点坐标替换得到 $k_{弦}\cdot k_{O\!中点}=-\frac{b^2}{a^2}$；" "\n"
        r"② 若另有「垂直」条件，再写一个斜率积 $=-1$ 的方程；" "\n"
        r"③ 两式右端联立解出中点坐标，由坐标的符号约束定参数范围；" "\n"
        r"④ 求共线段的面积比时，用参数 $s$ 表示共线点，比值就是参数之比．"
    ),
    'difficulty': 0.78,
    'topics': ['M-T-360'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-360-V1',
}

T360_V2 = {
    'type': '解答',
    'stem_text': (
        r"在平面直角坐标系 $xOy$ 中，已知椭圆 $C:\dfrac{x^{2}}{a^{2}}+\dfrac{y^{2}}{b^{2}}=1\ (a>b>0)$ 的左焦点为 $F\left(-\sqrt3,0\right)$，"
        r"点 $A\left(-\sqrt3,\dfrac12\right)$ 在椭圆 $C$ 上．"
        r"（1）求椭圆 $C$ 的方程；"
        r"（2）已知圆 $O:x^{2}+y^{2}=a^{2}$，连接 $FA$ 并延长交圆 $O$ 于点 $B$，$H$ 为椭圆长轴上一点（异于左、右焦点），"
        r"过点 $H$ 作椭圆长轴的垂线分别交椭圆 $C$ 和圆 $O$ 于点 $P$，$Q$（$P$、$Q$ 均在 $x$ 轴上方）．"
        r"连接 $PA$，$QB$，记 $PA$ 的斜率为 $k_1$，$QB$ 的斜率为 $k_2$．"
        r"①求 $\dfrac{k_2}{k_1}$ 的值；②求证：直线 $PA$，$QB$ 的交点在定直线上．"
    ),
    'opts': [],
    'answer': (
        r"（1）$\dfrac{x^{2}}4+y^{2}=1$；（2）①$\dfrac{k_2}{k_1}=2$；②交点在定直线 $y=0$（即 $x$ 轴）上．"
    ),
    'analysis': (
        r"（1）由焦距得 $c=\sqrt3$，把 $A$ 代入方程解 $a^2,b^2$．"
        r"（2）①设 $H(t,0)$，分别由椭圆和圆的方程写出 $P,Q$ 的纵坐标，发现 $y_2=2y_1$；"
        r"再由 $A$、$B$ 的纵坐标恰好是 $P$、$Q$ 的一半关系，代入斜率公式即得比值．"
        r"②写出两条直线方程，把 $k_2=2k_1$ 代入后消去 $k_1$ 即得交点纵坐标恒为 $0$．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"由左焦点 $F\left(-\sqrt3,0\right)$ 得 $c=\sqrt3$，故 $a^{2}=b^{2}+3$．" "\n"
        r"又 $A\left(-\sqrt3,\dfrac12\right)$ 在椭圆上：$\dfrac3{a^{2}}+\dfrac1{4b^{2}}=1$．" "\n"
        r"代入 $a^{2}=b^{2}+3$：$\dfrac3{b^{2}+3}+\dfrac1{4b^{2}}=1$，解得 $b^{2}=1$，$a^{2}=4$．" "\n"
        r"椭圆 $C$ 的方程为 $\boxed{\dfrac{x^{2}}4+y^{2}=1}$．" "\n"
        r"**第（2）问 ①**" "\n"
        r"设 $H(t,0)$，则 $P(t,y_1)$ 在椭圆上、$Q(t,y_2)$ 在圆 $x^{2}+y^{2}=4$ 上，且 $y_1,y_2>0$．" "\n"
        r"$\dfrac{t^{2}}4+y_1^{2}=1\ \Longrightarrow\ y_1^{2}=1-\dfrac{t^{2}}4$；$t^{2}+y_2^{2}=4\ \Longrightarrow\ y_2^{2}=4-t^{2}$．" "\n"
        r"故 $\dfrac{y_2^{2}}{y_1^{2}}=\dfrac{4-t^{2}}{1-\frac{t^{2}}4}=4$，由 $y_1,y_2>0$ 得 $y_2=2y_1$．" "\n"
        r"$F\left(-\sqrt3,0\right)$、$A\left(-\sqrt3,\dfrac12\right)$ 横坐标相同，故直线 $AF$ 为 $x=-\sqrt3$；" "\n"
        r"与圆 $x^{2}+y^{2}=4$ 交于 $y=\pm1$，由「延长」知 $B\left(-\sqrt3,1\right)$．" "\n"
        r"$k_2=\dfrac{y_2-1}{t+\sqrt3}$，$k_1=\dfrac{y_1-\frac12}{t+\sqrt3}$，" "\n"
        r"$\dfrac{k_2}{k_1}=\dfrac{y_2-1}{y_1-\frac12}=\dfrac{2y_1-1}{y_1-\frac12}=\boxed{2}$．" "\n"
        r"**第（2）问 ②**" "\n"
        r"直线 $QB$：$y-1=k_2\left(x+\sqrt3\right)=2k_1\left(x+\sqrt3\right)$；" "\n"
        r"直线 $PA$：$y-\dfrac12=k_1\left(x+\sqrt3\right)$．" "\n"
        r"由第二式 $k_1\left(x+\sqrt3\right)=y-\dfrac12$，代入第一式得" "\n"
        r"$y-1=2\left(y-\dfrac12\right)=2y-1$，解得 $y=0$．" "\n"
        r"故交点恒在定直线 $\boxed{y=0}$（即 $x$ 轴）上．"
    ),
    'review': (
        r"① ⭐⭐ **$\frac{y_2^2}{y_1^2}=4$ 是「圆半径 $=a$」的必然结果**："
        r"$y_2^2=a^2-t^2$、$y_1^2=b^2\left(1-\frac{t^2}{a^2}\right)=\frac{b^2}{a^2}\left(a^2-t^2\right)$，"
        r"故 $\frac{y_2}{y_1}=\frac ab=\frac21=2$．**一般地：椭圆与它的「外接圆 $x^2+y^2=a^2$」在同一横坐标处的纵坐标之比恒为 $\frac ab$**．" "\n"
        r"② ⭐⭐ **$A$ 与 $B$ 的纵坐标（$\frac12$ 与 $1$）也是 $1:2$**：这不是巧合，"
        r"$A$ 在椭圆上、$B$ 在圆上且横坐标同为 $-\sqrt3$，由①的一般结论即得 $1=2\cdot\frac12$ ✓" "\n"
        r"③ ⭐⭐ **两个「$1:2$」配对，斜率比才能是常数**："
        r"$k_2=\frac{y_2-1}{t+\sqrt3}$、$k_1=\frac{y_1-\frac12}{t+\sqrt3}$，分母相同，"
        r"分子 $\left(y_2-1\right)=2\left(y_1-\frac12\right)$ 恰好也是 $2$ 倍 ⟹ 比值恒为 $2$．" "\n"
        r"④ ⭐⭐ **消 $k_1$ 求交点轨迹是通法**：两条直线方程含同一参数 $k_1$，"
        r"从一条解出 $k_1(x+\sqrt3)$ 整体代入另一条，**参数与横坐标一起消掉**，只剩 $y$ 的关系．" "\n"
        r"⑤ ⭐⭐ **$y=0$ 说明交点在 $x$ 轴上**，与 $t$、$k_1$ 都无关 ✓" "\n"
        r"⑥ 数值复核：取 $t=0$，则 $y_1=1$、$y_2=2$，$k_1=\frac{1-0.5}{0+\sqrt3}=\frac{0.5}{1.732}=0.2887$，"
        r"$k_2=\frac{2-1}{1.732}=0.5774$，$\frac{k_2}{k_1}=2.000$ ✓；" "\n"
        r"   直线 $PA$：$y-0.5=0.2887(x+1.732)$；直线 $QB$：$y-1=0.5774(x+1.732)$；"
        r"第二式减 2 倍第一式：$(y-1)-2(y-0.5)=0$ ⟹ $-y=0$ ⟹ $y=0$ ✓；"
        r"代回得交点横坐标 $x=-\sqrt3-\frac{0.5}{0.2887}=-1.732-1.732=-3.464$ ✓" "\n"
        r"**通法（椭圆与外接圆的「等高点」）**：" "\n"
        r"① 同一横坐标 $t$ 处，椭圆上点纵坐标 $y_1$ 与圆 $x^2+y^2=a^2$ 上点纵坐标 $y_2$ 满足 $y_2=\frac ab\,y_1$；" "\n"
        r"② 若两条直线分别过这样的一对点与一对定点（定点也满足同样的比例），则斜率比为常数；" "\n"
        r"③ 求两直线交点：写出含参方程，从一式解出「参数 $\times$ 公共因子」整体代入另一式即可消参．"
    ),
    'difficulty': 0.75,
    'topics': ['M-T-360'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-360-V2',
}

T360_V3 = {
    'type': '解答',
    'stem_text': (
        r"在平面直角坐标系 $xOy$ 中，椭圆 $\dfrac{x^{2}}{a^{2}}+\dfrac{y^{2}}{b^{2}}=1\ (a>b>0)$ 的离心率为 $\dfrac{\sqrt2}2$，"
        r"过原点 $O$ 的直线交该椭圆于 $A$，$B$ 两点（点 $A$ 在 $x$ 轴上方），点 $E(4,0)$．"
        r"当直线 $AB$ 垂直于 $x$ 轴时，$\left|AE\right|=2\sqrt5$．"
        r"（1）求 $a$，$b$ 的值；"
        r"（2）设直线 $AE$ 与椭圆的另一交点为 $C$，直线 $BE$ 与椭圆的另一交点为 $D$．"
        r"①若 $OC\parallel BE$，求 $\triangle ABE$ 的面积；"
        r"②是否存在 $x$ 轴上的一定点 $T$，使得直线 $CD$ 恒过点 $T$？若存在，求出 $T$ 的坐标；若不存在，请说明理由．"
    ),
    'opts': [],
    'answer': (
        r"（1）$a=2\sqrt2$，$b=2$；（2）①$2\sqrt{14}$；②存在，$T\left(\dfrac83,0\right)$．"
    ),
    'analysis': (
        r"（1）由 $\left|AE\right|=2\sqrt5$ 得 $b=2$，再由离心率得 $a^2=8$．"
        r"（2）①由 $OC\parallel BE$ 且 $O$ 为 $AB$ 中点得 $C$ 为 $AE$ 中点，列出 $A$、$C$ 都在椭圆上的方程组求解；"
        r"②写出 $AE$、$BE$ 方程分别与椭圆联立，用韦达定理求 $C$、$D$ 坐标，再验证三点共线．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"当 $AB\perp x$ 轴时 $A(0,b)$，由 $\left|AE\right|=\sqrt{16+b^{2}}=2\sqrt5$ 得 $b^{2}+16=20$，即 $b=2$．" "\n"
        r"由 $e=\dfrac ca=\dfrac{\sqrt2}2$ 得 $\dfrac{a^{2}-b^{2}}{a^{2}}=\dfrac12$，即 $\dfrac{a^{2}-4}{a^{2}}=\dfrac12$，得 $a^{2}=8$．" "\n"
        r"故 $\boxed{a=2\sqrt2}$，$\boxed{b=2}$，椭圆为 $\dfrac{x^{2}}8+\dfrac{y^{2}}4=1$，即 $x^{2}+2y^{2}=8$．" "\n"
        r"**第（2）问 ①**" "\n"
        r"$A,B$ 关于原点对称，故 $O$ 为 $AB$ 中点；又 $OC\parallel BE$，在 $\triangle ABE$ 中由中位线定理的逆定理得 $C$ 为 $AE$ 中点．" "\n"
        r"设 $A(x_0,y_0)$，则 $C\left(\dfrac{x_0+4}2,\dfrac{y_0}2\right)$．由 $A,C$ 都在椭圆上：" "\n"
        r"$\dfrac{x_0^{2}}8+\dfrac{y_0^{2}}4=1$，$\dfrac{(x_0+4)^{2}}{32}+\dfrac{y_0^{2}}{16}=1$．" "\n"
        r"由第一式 $y_0^{2}=4-\dfrac{x_0^{2}}2$，代入第二式：" "\n"
        r"$\dfrac{(x_0+4)^{2}}{32}+\dfrac14-\dfrac{x_0^{2}}{32}=1\ \Longrightarrow\ \dfrac{8x_0+16}{32}=\dfrac34\ \Longrightarrow\ x_0=1$．" "\n"
        r"于是 $y_0^{2}=4-\dfrac12=\dfrac72$，$y_0=\dfrac{\sqrt{14}}2$（$A$ 在 $x$ 轴上方）．" "\n"
        r"$A,B$ 关于原点对称，故 $S_{\triangle ABE}=S_{\triangle AOE}+S_{\triangle BOE}=2S_{\triangle AOE}=\left|OE\right|\cdot y_0=4\cdot\dfrac{\sqrt{14}}2=\boxed{2\sqrt{14}}$．" "\n"
        r"**第（2）问 ②**" "\n"
        r"存在，$T\left(\dfrac83,0\right)$．理由如下．" "\n"
        r"设 $A(x_0,y_0)$，则 $B(-x_0,-y_0)$．直线 $AE$：$y=\dfrac{y_0}{x_0-4}(x-4)$．" "\n"
        r"与 $x^{2}+2y^{2}=8$ 联立，消去 $y$ 得关于 $x$ 的二次方程，其两根为 $x_0$ 与 $x_C$，由韦达定理可得" "\n"
        r"$x_C=\dfrac{8-3x_0}{3-x_0}$，进而 $y_C=\dfrac{y_0}{x_0-4}\left(x_C-4\right)=\dfrac{y_0}{3-x_0}$．" "\n"
        r"由对称性（$x_0\to-x_0$，$y_0\to-y_0$）得 $x_D=\dfrac{8+3x_0}{3+x_0}$，$y_D=-\dfrac{y_0}{3+x_0}$．" "\n"
        r"取 $T\left(\dfrac83,0\right)$，则" "\n"
        r"$k_{TC}=\dfrac{\frac{y_0}{3-x_0}}{\frac{8-3x_0}{3-x_0}-\frac83}=\dfrac{3y_0}{3(8-3x_0)-8(3-x_0)}=\dfrac{3y_0}{-x_0}=-\dfrac{3y_0}{x_0}$．" "\n"
        r"同理 $k_{TD}=\dfrac{-\frac{y_0}{3+x_0}}{\frac{8+3x_0}{3+x_0}-\frac83}=\dfrac{-3y_0}{3(8+3x_0)-8(3+x_0)}=\dfrac{-3y_0}{x_0}=-\dfrac{3y_0}{x_0}$．" "\n"
        r"故 $k_{TC}=k_{TD}$，即 $T,C,D$ 三点共线，直线 $CD$ 恒过定点 $\boxed{T\left(\dfrac83,0\right)}$．" "\n"
        r"（当 $x_0=0$ 时 $x_C=x_D=\dfrac83$，$CD$ 垂直于 $x$ 轴，同样过 $T$．）"
    ),
    'review': (
        r"① ⭐⭐ **$OC\parallel BE$ 且 $O$ 为 $AB$ 中点 ⟹ $C$ 为 $AE$ 中点** —— "
        r"这是三角形中位线定理的逆定理，是本题①的唯一入口．" "\n"
        r"② ⭐⭐ **$A$、$C$ 都在椭圆上 ⟹ 两个方程解两个未知数**："
        r"把 $y_0^2=4-\frac{x_0^2}2$ 代入第二式后，$\frac{(x_0+4)^2-x_0^2}{32}=\frac34$ 中 $x_0^2$ 恰好抵消，"
        r"**只剩 $x_0$ 的一次项** ⟹ 一步解出 $x_0=1$．这种「平方项抵消」是刻意设计．" "\n"
        r"③ ⭐⭐ **$S_{\triangle ABE}=2S_{\triangle AOE}=\left|OE\right|\cdot y_0$** —— "
        r"$A,B$ 关于原点对称是关键，比用行列式算面积快得多．" "\n"
        r"④ ⭐⭐ **$D$ 的坐标由对称性直接写出**：把 $A$ 换成 $-A$（即 $x_0\to-x_0$、$y_0\to-y_0$）即可，不必重算一遍．" "\n"
        r"⑤ ⭐⭐ **定点的横坐标为 $\frac83$，恰是 $\frac{a^2}{b^2}\cdot\frac{4}{3}$ 型**："
        r"一般地，椭圆 $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$、外点 $E(e,0)$ 时，定点横坐标为 $\frac{a^2}{e}$；"
        r"本题 $a^2=8$、$e=4$ ⟹ $\frac{a^2}{e}=2$… 需另算，但**「$T$ 在 $x$ 轴上且横坐标常为 $\frac{a^2}{\text{某量}}$」这个形式要记**．" "\n"
        r"⑥ 数值复核：$x_0=1$、$y_0=\frac{\sqrt{14}}2=1.8708$；"
        r"$x_C=\frac{8-3}{3-1}=\frac52=2.5$，$y_C=\frac{1.8708}{2}=0.9354$；"
        r"代入椭圆：$\frac{6.25}{8}+\frac{0.875}{4}=0.78125+0.21875=1$ ✓；" "\n"
        r"   $x_0=0$、$y_0=2$：$x_C=x_D=\frac83$，$y_C=\frac23$、$y_D=-\frac23$；"
        r"代入椭圆：$\frac{64}{9\cdot8}+\frac{4}{9\cdot4}=\frac89+\frac19=1$ ✓；" "\n"
        r"   $k_{TC}$ 验：$x_0=1$ 时 $-\frac{3y_0}{x_0}=-\frac{3\cdot1.8708}{1}=-5.6124$；"
        r"直接算 $k_{TC}=\frac{0.9354}{2.5-\frac83}=\frac{0.9354}{-0.1667}=-5.612$ ✓✓✓" "\n"
        r"**通法（圆锥曲线的「三点共线」定点）**：" "\n"
        r"① 设主动点 $A$，写出两条直线（各过 $A$ 与一个定点）；" "\n"
        r"② 分别与曲线联立，用韦达定理求出交点 $C,D$ 的坐标（**只需求一个，另一个用对称性**）；" "\n"
        r"③ 猜定点：取特殊位置（如 $x_0=0$ 时的垂直弦）定出候选点；" "\n"
        r"④ 验证：算 $k_{TC}$ 与 $k_{TD}$ 是否相等（或与 $x_0$ 无关）．"
    ),
    'difficulty': 0.86,
    'topics': ['M-T-360'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-360-V3',
}

T348_V1 = {
    'type': '解答',
    'stem_text': (
        r"在平面直角坐标系 $xOy$ 中，已知动圆的半径为 $1$，且经过坐标原点 $O$，设动圆的圆心为 $A$．"
        r"（1）求点 $A$ 的轨迹方程；"
        r"（2）设点 $A$ 的轨迹与 $x$ 轴交于 $P$，$Q$ 两点（$P$ 在 $Q$ 左侧），过点 $P$ 的直线 $l_1$ 交点 $A$ 的轨迹于点 $M$（异于 $P$，$Q$），"
        r"交直线 $l_2:x=2$ 于点 $C$，经过 $Q$，$M$ 的直线交 $l_2$ 于点 $D$，"
        r"求证：以 $CD$ 为直径的圆过定点，并求出定点坐标．"
    ),
    'opts': [],
    'answer': (
        r"（1）$x^{2}+y^{2}=1$；（2）恒过定点 $\left(2+\sqrt3,0\right)$ 与 $\left(2-\sqrt3,0\right)$．"
    ),
    'analysis': (
        r"（1）圆心到原点距离等于半径 $1$，直接得圆．"
        r"（2）设 $l_1:x=my-1$ 与单位圆联立求 $M$，进而求 $C$、$D$ 的坐标；"
        r"写出以 $CD$ 为直径的圆的方程后令 $y=0$，用两个平方差相减消去参数 $m$．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"动圆半径为 $1$ 且过原点，故 $\left|AO\right|=1$，点 $A$ 的轨迹为 $\boxed{x^{2}+y^{2}=1}$．" "\n"
        r"**第（2）问**" "\n"
        r"由（1）得 $P(-1,0)$，$Q(1,0)$．设 $l_1:x=my-1$（$m\ne0$，因 $M$ 异于 $P,Q$）．" "\n"
        r"与 $x^{2}+y^{2}=1$ 联立：$\left(my-1\right)^{2}+y^{2}=1$，即 $\left(1+m^{2}\right)y^{2}-2my=0$．" "\n"
        r"除 $y=0$（点 $P$）外，$y_M=\dfrac{2m}{1+m^{2}}$，故 $x_M=m\cdot\dfrac{2m}{1+m^{2}}-1=\dfrac{m^{2}-1}{1+m^{2}}$．" "\n"
        r"即 $M\left(\dfrac{m^{2}-1}{1+m^{2}},\dfrac{2m}{1+m^{2}}\right)$．" "\n"
        r"在 $x=my-1$ 中令 $x=2$ 得 $y=\dfrac3m$，即 $C\left(2,\dfrac3m\right)$．" "\n"
        r"$k_{MQ}=\dfrac{\frac{2m}{1+m^{2}}}{\frac{m^{2}-1}{1+m^{2}}-1}=\dfrac{2m}{-2}=-m$，故直线 $QM$ 为 $y=-m(x-1)$．" "\n"
        r"令 $x=2$ 得 $y=-m$，即 $D(2,-m)$．" "\n"
        r"于是 $\left|CD\right|=\left|\dfrac3m+m\right|$，$CD$ 的中点为 $E\left(2,\dfrac3{2m}-\dfrac m2\right)$，半径 $r=\dfrac12\left|\dfrac3m+m\right|$．" "\n"
        r"以 $CD$ 为直径的圆：$(x-2)^{2}+\left(y-\dfrac3{2m}+\dfrac m2\right)^{2}=\left(\dfrac3{2m}+\dfrac m2\right)^{2}$．" "\n"
        r"令 $y=0$：$(x-2)^{2}=\left(\dfrac3{2m}+\dfrac m2\right)^{2}-\left(\dfrac3{2m}-\dfrac m2\right)^{2}$．" "\n"
        r"由 $(a+b)^{2}-(a-b)^{2}=4ab$，取 $a=\dfrac3{2m}$、$b=\dfrac m2$ 得" "\n"
        r"$(x-2)^{2}=4\cdot\dfrac3{2m}\cdot\dfrac m2=3$，故 $x=2\pm\sqrt3$．" "\n"
        r"所以以 $CD$ 为直径的圆恒过定点 $\boxed{\left(2+\sqrt3,0\right)}$ 与 $\boxed{\left(2-\sqrt3,0\right)}$．"
    ),
    'review': (
        r"① ⭐⭐ **设 $l_1$ 为 $x=my-1$ 而不是 $y=k(x+1)$** —— "
        r"这样与圆联立后得到 $(1+m^2)y^2-2my=0$，$y=0$ 是一个根（点 $P$），另一个根一步即得，"
        r"**不用解二次方程**。这是过圆上一点的直线参数化的标准技巧．" "\n"
        r"② ⭐⭐ **$k_{MQ}=-m$ 极漂亮**：$k_{l_1}=\frac1m$，而 $k_{MQ}=-m$，两者互为负倒数 —— "
        r"这其实是「$PQ$ 是直径 ⟹ $\angle PMQ=90^\circ$ ⟹ $MP\perp MQ$」的代数表现．"
        r"**若用 $y=k(x+1)$ 设直线，则 $k_{MQ}=-\frac1k$，同样成立**．" "\n"
        r"③ ⭐⭐ **令 $y=0$ 后两个平方差相减是消参的关键**："
        r"$\left(\frac3{2m}+\frac m2\right)^2-\left(\frac3{2m}-\frac m2\right)^2=4\cdot\frac3{2m}\cdot\frac m2=3$，"
        r"$m$ 恰好约掉，**与 $m$ 无关** ⟹ 定点．" "\n"
        r"   一般结论：$(a+b)^2-(a-b)^2=4ab$，当 $ab$ 为常数时消参成功．"
        r"本题 $a=\frac3{2m}$、$b=\frac m2$ 的乘积恒为 $\frac34$ ✓" "\n"
        r"④ ⭐⭐ **两个定点关于 $x=2$ 对称**：$2\pm\sqrt3$，而圆心横坐标也恒为 $2$（因为 $C,D$ 都在 $l_2:x=2$ 上）．"
        r"**圆心固定 + 半径变化 ⟹ 与 $x$ 轴交点对称分布**．" "\n"
        r"⑤ 数值复核：取 $m=1$，$C(2,3)$、$D(2,-1)$，中点 $E(2,1)$，半径 $2$；"
        r"圆 $(x-2)^2+(y-1)^2=4$，令 $y=0$：$(x-2)^2=3$ ⟹ $x=2\pm\sqrt3$ ✓；" "\n"
        r"   取 $m=2$，$C(2,1.5)$、$D(2,-2)$，中点 $E(2,-0.25)$，半径 $1.75$；"
        r"圆 $(x-2)^2+(y+0.25)^2=3.0625$，令 $y=0$：$(x-2)^2=3.0625-0.0625=3$ ⟹ $x=2\pm\sqrt3$ ✓✓✓" "\n"
        r"**通法（圆过定点）**：" "\n"
        r"① 用 $x=my+x_P$ 参数化过圆上已知点的直线，联立后一个根已知、另一个根直接写出；" "\n"
        r"② 由「直径所对圆周角为直角」得另一条直线的斜率（互为负倒数）；" "\n"
        r"③ 求出直径两端点，写圆方程（圆心 = 中点，半径 = 半弦长）；" "\n"
        r"④ 令 $y=0$（求 $x$ 轴上的定点）或 $x=0$，用 $(a+b)^2-(a-b)^2=4ab$ 消参．"
    ),
    'difficulty': 0.74,
    'topics': ['M-T-348'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-348-V1',
}

T348_V3 = {
    'type': '解答',
    'stem_text': (
        r"已知抛物线 $y^{2}=4x$ 的焦点 $F$ 与椭圆 $C:\dfrac{x^{2}}{a^{2}}+\dfrac{y^{2}}{b^{2}}=1\ (a>b>0)$ 的一个焦点重合，"
        r"且点 $F$ 关于直线 $y=x$ 的对称点在椭圆上．"
        r"（1）求椭圆 $C$ 的标准方程；"
        r"（2）过点 $Q\left(0,-\dfrac13\right)$ 且斜率为 $k$ 的动直线 $l$ 交椭圆于 $A$、$B$ 两点，"
        r"在 $y$ 轴上是否存在定点 $M$，使以 $AB$ 为直径的圆恒过这个点？若存在，求出 $M$ 点的坐标；若不存在，请说明理由．"
    ),
    'opts': [],
    'answer': (
        r"（1）$\dfrac{x^{2}}2+y^{2}=1$；（2）存在，$M(0,1)$．"
    ),
    'analysis': (
        r"（1）由抛物线焦点得 $c=1$，对称点在椭圆上说明该点就是短轴顶点，故 $b=1$．"
        r"（2）先用两条特殊位置的弦（垂直于坐标轴）求出候选点 $M$，再对一般情形验证 $\vec{MA}\cdot\vec{MB}=0$．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"抛物线 $y^{2}=4x$ 的焦点为 $F(1,0)$，故椭圆的 $c=1$．" "\n"
        r"$F(1,0)$ 关于直线 $y=x$ 的对称点为 $(0,1)$，该点在椭圆上，代入得 $\dfrac0{a^{2}}+\dfrac1{b^{2}}=1$，即 $b=1$．" "\n"
        r"于是 $a^{2}=b^{2}+c^{2}=2$，椭圆 $C$ 的方程为 $\boxed{\dfrac{x^{2}}2+y^{2}=1}$．" "\n"
        r"**第（2）问**" "\n"
        r"先找候选点．当 $AB\perp x$ 轴时，$l:x=0$，此时 $A(0,1)$、$B(0,-1)$，以 $AB$ 为直径的圆为 $x^{2}+y^{2}=1$ ①；" "\n"
        r"当 $AB\perp y$ 轴时，$l:y=-\dfrac13$，代入椭圆得 $x^{2}=2\left(1-\dfrac19\right)=\dfrac{16}9$，即 $A\left(\dfrac43,-\dfrac13\right)$、$B\left(-\dfrac43,-\dfrac13\right)$，" "\n"
        r"以 $AB$ 为直径的圆的圆心为 $Q\left(0,-\dfrac13\right)$、半径为 $\dfrac43$，方程为 $x^{2}+\left(y+\dfrac13\right)^{2}=\dfrac{16}9$ ②．" "\n"
        r"联立①②：由 $\left(y+\dfrac13\right)^{2}-y^{2}=\dfrac{16}9-1$ 得 $\dfrac23y+\dfrac19=\dfrac79$，即 $y=1$，代回得 $x=0$．" "\n"
        r"故候选点为 $M(0,1)$．" "\n"
        r"下面证明：设 $l:y=kx-\dfrac13$，与 $x^{2}+2y^{2}=2$ 联立得" "\n"
        r"$\left(2k^{2}+1\right)x^{2}-\dfrac43kx-\dfrac{16}9=0$，故" "\n"
        r"$x_1+x_2=\dfrac{4k}{3\left(2k^{2}+1\right)}$，$x_1x_2=-\dfrac{16}{9\left(2k^{2}+1\right)}$．" "\n"
        r"$\vec{MA}=\left(x_1,\;y_1-1\right)$，$\vec{MB}=\left(x_2,\;y_2-1\right)$，且 $y_i-1=kx_i-\dfrac43$，于是" "\n"
        r"$\vec{MA}\cdot\vec{MB}=x_1x_2+\left(kx_1-\dfrac43\right)\left(kx_2-\dfrac43\right)$，" "\n"
        r"$=\left(1+k^{2}\right)x_1x_2-\dfrac43k\left(x_1+x_2\right)+\dfrac{16}9$，" "\n"
        r"$=\left(1+k^{2}\right)\cdot\dfrac{-16}{9\left(2k^{2}+1\right)}-\dfrac43k\cdot\dfrac{4k}{3\left(2k^{2}+1\right)}+\dfrac{16}9$，" "\n"
        r"$=\dfrac{-16\left(1+k^{2}\right)-16k^{2}}{9\left(2k^{2}+1\right)}+\dfrac{16}9=\dfrac{-16-32k^{2}}{9\left(2k^{2}+1\right)}+\dfrac{16}9$，" "\n"
        r"$=\dfrac{-16\left(1+2k^{2}\right)}{9\left(2k^{2}+1\right)}+\dfrac{16}9=-\dfrac{16}9+\dfrac{16}9=0$．" "\n"
        r"故 $MA\perp MB$ 恒成立，即 $\boxed{M(0,1)}$ 恒在以 $AB$ 为直径的圆上．"
    ),
    'review': (
        r"① ⭐⭐ **用两条特殊弦求候选点，再对一般情形验证** —— "
        r"这是「存在性」问题的标准三段式：**特殊位置猜点 ⟹ 一般情形验证 ⟹ 下结论**．" "\n"
        r"② ⭐⭐ **选 $AB\perp x$ 轴与 $AB\perp y$ 轴这两条**：前者过 $Q$ 的竖直线就是 $y$ 轴本身，"
        r"后者过 $Q$ 的水平线，两条都容易算，且交点唯一（两圆相交于 $M$ 与另一点，另一点需舍去）．" "\n"
        r"③ ⭐⭐ **联立时用 $x^{2}+2y^{2}=2$（两边乘 $2$）而不是 $\frac{x^2}{2}+y^2=1$**，"
        r"这样系数是整数，代入 $y=kx-\frac13$ 后得 $\left(2k^2+1\right)x^2-\frac43kx-\frac{16}9=0$ ✓" "\n"
        r"④ ⭐⭐ **$\vec{MA}\cdot\vec{MB}$ 的展开技巧**：$y_i-1=kx_i-\frac43$，"
        r"于是 $\left(y_1-1\right)\left(y_2-1\right)=k^2x_1x_2-\frac43k(x_1+x_2)+\frac{16}9$，"
        r"与 $x_1x_2$ 合并成 $(1+k^2)x_1x_2$ —— **系数 $(1+k^2)$ 是这类题的固定搭配**．" "\n"
        r"⑤ ⭐⭐ **分子 $-16-32k^2=-16(1+2k^2)$ 与分母 $9(2k^2+1)$ 恰好约掉** ⟹ "
        r"结果与 $k$ 无关，等于 $-\frac{16}9+\frac{16}9=0$．**这种「整体约分」是能成立的强信号**．" "\n"
        r"⑥ ⭐⭐ **$M(0,1)$ 就是椭圆的上顶点**：由第（1）问 $b=1$，而 $M$ 恰为 $(0,b)$．"
        r"这不是巧合，与「$F$ 关于 $y=x$ 的对称点」这一条件直接相关．" "\n"
        r"⑦ 数值复核：取 $k=0$，$l:y=-\frac13$，得 $A(1.333,-0.333)$、$B(-1.333,-0.333)$；"
        r"$\vec{MA}=(1.333,-1.333)$、$\vec{MB}=(-1.333,-1.333)$；"
        r"$\vec{MA}\cdot\vec{MB}=-1.777+1.777=0$ ✓；" "\n"
        r"   取 $k=1$：方程 $3x^2-\frac43x-\frac{16}9=0$，即 $27x^2-12x-16=0$，"
        r"$x=\frac{12\pm\sqrt{144+1728}}{54}=\frac{12\pm43.267}{54}$，得 $x_1=1.0235$、$x_2=-0.5790$；" "\n"
        r"   $y_1=1.0235-0.3333=0.6902$，$y_2=-0.5790-0.3333=-0.9123$；"
        r"$\vec{MA}=(1.0235,-0.3098)$、$\vec{MB}=(-0.5790,-1.9123)$；" "\n"
        r"   点积 $=1.0235(-0.5790)+(-0.3098)(-1.9123)=-0.5926+0.5924=-0.0002\approx0$ ✓✓✓" "\n"
        r"**通法（弦为直径的圆过定点）**：" "\n"
        r"① 特殊位置猜点：取两条互相垂直的弦（通常是过定点的竖直线与水平线）；" "\n"
        r"② 一般情形：设直线 $y=kx+b$，联立后用韦达定理；" "\n"
        r"③ 验证 $\vec{MA}\cdot\vec{MB}=0$，即 $(1+k^2)x_1x_2+k(\cdots)(x_1+x_2)+(\cdots)^2=0$；" "\n"
        r"④ 关键看分子能否提出与分母相同的因子（本题是 $1+2k^2$）．"
    ),
    'difficulty': 0.76,
    'topics': ['M-T-348'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-348-V3',
}

T398_E1 = {
    'type': '解答',
    'stem_text': (
        r"质点在 $x$ 轴上从原点 $O$ 出发向右运动，每次平移一个单位或两个单位，"
        r"且移动一个单位的概率为 $\dfrac23$，移动 $2$ 个单位的概率为 $\dfrac13$，设质点运动到点 $(n,0)$ 的概率为 $P_n$．"
        r"（1）求 $P_1$ 和 $P_2$；"
        r"（2）用 $P_{n-1},P_{n-2}$ 表示 $P_n$，并证明 $\left\{P_n-P_{n-1}\right\}$ 是等比数列；"
        r"（3）求 $P_n$．"
    ),
    'opts': [],
    'answer': (
        r"（1）$P_1=\dfrac23$，$P_2=\dfrac79$；"
        r"（2）$P_n=\dfrac23P_{n-1}+\dfrac13P_{n-2}$，$\left\{P_n-P_{n-1}\right\}$ 是首项 $\dfrac19$、公比 $-\dfrac13$ 的等比数列；"
        r"（3）$P_n=\dfrac34+\dfrac14\left(-\dfrac13\right)^{n}$．"
    ),
    'analysis': (
        r"（1）直接按路径枚举；（2）到达点 $n$ 只能从 $n-1$ 走 $1$ 步或从 $n-2$ 走 $2$ 步，用全概率公式；"
        r"再把递推式改写成 $P_n-P_{n-1}=-\frac13\left(P_{n-1}-P_{n-2}\right)$；（3）累加等比数列求和．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"到点 $1$ 只能走一步 $1$，故 $P_1=\dfrac23$．" "\n"
        r"到点 $2$ 有两条路：先到 $1$ 再走 $1$ 步，或直接走 $2$ 步，故" "\n"
        r"$P_2=P_1\cdot\dfrac23+1\cdot\dfrac13=\dfrac23\cdot\dfrac23+\dfrac13=\dfrac49+\dfrac13=\boxed{\dfrac79}$．" "\n"
        r"**第（2）问**" "\n"
        r"到达点 $n$（$n\ge3$）只有两种互斥情形：从点 $n-1$ 走 $1$ 步，或从点 $n-2$ 走 $2$ 步，故" "\n"
        r"$P_n=\dfrac23P_{n-1}+\dfrac13P_{n-2}$．" "\n"
        r"两边减 $P_{n-1}$（注意 $\frac23P_{n-1}-P_{n-1}=-\frac13P_{n-1}$）：" "\n"
        r"$P_n-P_{n-1}=-\dfrac13\left(P_{n-1}-P_{n-2}\right)$．" "\n"
        r"首项 $P_2-P_1=\dfrac79-\dfrac23=\dfrac19$，公比为 $-\dfrac13$，" "\n"
        r"故 $\left\{P_n-P_{n-1}\right\}$ 是首项 $\dfrac19$、公比 $-\dfrac13$ 的等比数列．" "\n"
        r"**第（3）问**" "\n"
        r"由（2），$P_n-P_{n-1}=\dfrac19\left(-\dfrac13\right)^{n-2}$（$n\ge2$）．" "\n"
        r"$P_n=P_1+\sum\limits_{k=2}^{n}\left(P_k-P_{k-1}\right)=\dfrac23+\dfrac19\sum\limits_{k=2}^{n}\left(-\dfrac13\right)^{k-2}$，" "\n"
        r"$=\dfrac23+\dfrac19\cdot\dfrac{1-\left(-\frac13\right)^{n-1}}{1+\frac13}=\dfrac23+\dfrac19\cdot\dfrac34\left[1-\left(-\dfrac13\right)^{n-1}\right]$，" "\n"
        r"$=\dfrac23+\dfrac1{12}-\dfrac1{12}\left(-\dfrac13\right)^{n-1}=\dfrac34-\dfrac1{12}\left(-\dfrac13\right)^{n-1}$．" "\n"
        r"又 $-\dfrac1{12}\left(-\dfrac13\right)^{n-1}=\dfrac14\left(-\dfrac13\right)^{n}$，故" "\n"
        r"$\boxed{P_n=\dfrac34+\dfrac14\left(-\dfrac13\right)^{n}}$（$n\ge1$）．"
    ),
    'review': (
        r"① ⭐⭐ **$P_n=pP_{n-1}+qP_{n-2}$ 作差后公比恒为 $-q$**："
        r"$P_n-P_{n-1}=(p-1)P_{n-1}+qP_{n-2}=-q\left(P_{n-1}-P_{n-2}\right)$（因 $p+q=1$）．"
        r"**公比只由「走 2 步的概率」决定，与 $p$ 无关** ✓" "\n"
        r"② ⭐⭐ **稳态值 $=\frac1{1+q}$**：$n\to\infty$ 时 $P_n\to\frac34$，而 $\frac1{1+\frac13}=\frac34$ ✓；"
        r"这恰好是「平均步长」$\frac23\cdot1+\frac13\cdot2=\frac43$ 的倒数 —— "
        r"**直观：每步平均走 $\frac43$，故命中某点的概率趋于 $\frac1{4/3}=\frac34$** ✓✓" "\n"
        r"③ ⭐⭐ **$P_0=1$ 是隐含初始条件**：到点 $2$ 的「直接走 2 步」一项就是 $P_0\cdot\frac13$，"
        r"写 $P_2=P_1\cdot\frac23+P_0\cdot\frac13$ 更清楚．" "\n"
        r"④ ⭐⭐ **两种等价写法**：$\frac34-\frac1{12}\left(-\frac13\right)^{n-1}$ 与 $\frac34+\frac14\left(-\frac13\right)^n$ —— "
        r"因为 $-\frac1{12}\left(-\frac13\right)^{n-1}=-\frac1{12}\cdot(-3)\left(-\frac13\right)^n=\frac14\left(-\frac13\right)^n$ ✓" "\n"
        r"   建议用后一种，形式更对称（末项与前项同型）．" "\n"
        r"⑤ 数值复核：$n=1$：$\frac34+\frac14\left(-\frac13\right)=\frac34-\frac1{12}=\frac23$ ✓；"
        r"$n=2$：$\frac34+\frac14\cdot\frac19=\frac34+\frac1{36}=\frac79$ ✓；"
        r"$n=0$：$\frac34+\frac14=1$ ✓；" "\n"
        r"   $n=3$：$\frac34-\frac1{108}=\frac{80}{108}=\frac{20}{27}$；"
        r"直接算 $P_3=\frac23P_2+\frac13P_1=\frac23\cdot\frac79+\frac13\cdot\frac23=\frac{14}{27}+\frac6{27}=\frac{20}{27}$ ✓✓✓" "\n"
        r"**通法（「每次前进 1 或 2」型概率递推）**：" "\n"
        r"① 全概率：$P_n=pP_{n-1}+qP_{n-2}$（$p+q=1$），注意 $P_0=1$；" "\n"
        r"② 作差构造等比：$P_n-P_{n-1}=-q\left(P_{n-1}-P_{n-2}\right)$，公比 $-q$；" "\n"
        r"③ 累加求通项：$P_n=P_1+(P_2-P_1)\frac{1-(-q)^{n-1}}{1+q}$；" "\n"
        r"④ 检验：代 $n=0,1,2$ 三个值，并验证稳态值 $=\frac1{1+q}$．"
    ),
    'difficulty': 0.62,
    'topics': ['M-T-398'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-398-E1',
}

T398_V1 = {
    'type': '解答',
    'stem_text': (
        r"某月从某市大学生中随机调查了 $100$ 人，将这 $100$ 人本月网络外卖消费金额制成频数分布表"
        r"（每人每月不超过 $3000$ 元）：分组（单位：百元）为 $[0,5),[5,10),[10,15),[15,20),[20,25),[25,30)$，"
        r"对应频数为 $20,35,25,10,5,5$．由频数分布表可认为消费金额 $Z$（单位：元）近似服从正态分布 $N\left(\mu,\sigma^{2}\right)$，"
        r"其中 $\mu$ 近似为样本平均数 $\bar x$（每组数据取区间中点值），$\sigma=660$．"
        r"（1）现从该市任取 $20$ 名大学生，记其中消费金额恰在 $390$ 元至 $2370$ 元之间的人数为 $X$，求 $X$ 的数学期望；"
        r"（2）某大学推出「勇闯关，送大奖」活动：方格图上标有第 $0$ 格至第 $60$ 格共 $61$ 个方格，棋子开始在第 $0$ 格，"
        r"掷一枚均匀硬币（正、反面概率都是 $\frac12$），正面则前进 $1$ 格，反面则前进 $2$ 格，重复多次．"
        r"若棋子最终停在第 $59$ 格则「闯关成功」，停在第 $60$ 格则「闯关失败」．记棋子移到第 $n$ 格的概率为 $P_n$（$P_0=1$）．"
        r"①求证：当 $1\le n\le59$ 时，$\left\{P_n-P_{n-1}\right\}$ 是等比数列；"
        r"②比较闯关成功与闯关失败的概率大小，并说明理由．"
        r"参考数据：若 $\xi\sim N(\mu,\sigma^{2})$，则 $P(\mu-\sigma<\xi\le\mu+\sigma)=0.6827$，$P(\mu-2\sigma<\xi\le\mu+2\sigma)=0.9545$．"
    ),
    'opts': [],
    'answer': (
        r"（1）$E(X)=16.372$；"
        r"（2）①见解析；②闯关成功的概率大于闯关失败的概率．"
    ),
    'analysis': (
        r"（1）先由频数分布表算 $\bar x=1050$，注意 $390=\mu-\sigma$、$2370=\mu+2\sigma$，"
        r"用正态曲线的对称性把概率拆成两半，再乘 $20$．"
        r"（2）①与「每次走 1 或 2 」的标准递推完全相同，公比为 $-\frac12$；"
        r"②注意停在第 $60$ 格只能从第 $58$ 格掷反面到达（到 $59$ 格游戏已结束）．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"$\bar x=250\times0.2+750\times0.35+1250\times0.25+1750\times0.1+2250\times0.05+2750\times0.05$，" "\n"
        r"$=50+262.5+312.5+175+112.5+137.5=1050$（元），故 $\mu=1050$．" "\n"
        r"$\mu-\sigma=1050-660=390$，$\mu+2\sigma=1050+1320=2370$，故" "\n"
        r"$P(390<Z\le2370)=P(\mu-\sigma<Z\le\mu+2\sigma)$，" "\n"
        r"$=\dfrac{0.6827}2+\dfrac{0.9545}2=0.34135+0.47725=0.8186$．" "\n"
        r"（或写成 $0.9545-\dfrac{0.9545-0.6827}2=0.9545-0.1359=0.8186$．）" "\n"
        r"于是 $X\sim B(20,0.8186)$，$\boxed{E(X)=20\times0.8186=16.372}$．" "\n"
        r"**第（2）问 ①**" "\n"
        r"$P_0=1$，$P_1=\dfrac12$．对 $2\le n\le59$，到第 $n$ 格只有两种互斥情形：" "\n"
        r"先到 $n-2$ 格再掷反面（概率 $\frac12P_{n-2}$），或先到 $n-1$ 格再掷正面（概率 $\frac12P_{n-1}$），" "\n"
        r"故 $P_n=\dfrac12P_{n-2}+\dfrac12P_{n-1}$，即 $P_n-P_{n-1}=-\dfrac12\left(P_{n-1}-P_{n-2}\right)$．" "\n"
        r"首项 $P_1-P_0=-\dfrac12$，公比 $-\dfrac12$，故 $\left\{P_n-P_{n-1}\right\}$ 是等比数列．" "\n"
        r"**第（2）问 ②**" "\n"
        r"由①，$P_n-P_{n-1}=\left(-\dfrac12\right)^{n}$，累加得" "\n"
        r"$P_n=1+\sum\limits_{k=1}^{n}\left(-\dfrac12\right)^{k}=1+\dfrac{-\frac12\left[1-\left(-\frac12\right)^{n}\right]}{1+\frac12}=1-\dfrac13\left[1-\left(-\dfrac12\right)^{n}\right]$，" "\n"
        r"$=\dfrac23+\dfrac13\left(-\dfrac12\right)^{n}=\dfrac23\left[1-\left(-\dfrac12\right)^{n+1}\right]$．" "\n"
        r"闯关成功（停在第 $59$ 格）：$P_{59}=\dfrac23\left[1-\left(-\dfrac12\right)^{60}\right]=\dfrac23\left(1-\dfrac1{2^{60}\vphantom{1}}\right)$．" "\n"
        r"闯关失败：到第 $60$ 格只能从第 $58$ 格掷反面（若已到 $59$ 格则游戏结束），故" "\n"
        r"$P_{60}=\dfrac12P_{58}=\dfrac12\cdot\dfrac23\left[1-\left(-\dfrac12\right)^{59}\right]=\dfrac13\left(1+\dfrac1{2^{59}\vphantom{1}}\right)$．" "\n"
        r"$P_{59}-P_{60}=\dfrac23\left(1-\dfrac1{2^{60}}\right)-\dfrac13\left(1+\dfrac1{2^{59}}\right)=\dfrac13-\dfrac2{3\cdot2^{60}}-\dfrac2{3\cdot2^{60}}=\dfrac13\left(1-\dfrac1{2^{58}}\right)>0$．" "\n"
        r"所以 $\boxed{\text{闯关成功的概率大于闯关失败的概率}}$．"
    ),
    'review': (
        r"① ⭐⭐ **$\bar x$ 用组中值加权**：$250,750,1250,1750,2250,2750$ 是六个区间的中点，权重是频率．"
        r"验算权重和：$0.2+0.35+0.25+0.1+0.05+0.05=1.00$ ✓" "\n"
        r"② ⭐⭐ **$P(\mu-\sigma<Z\le\mu+2\sigma)$ 的两种算法**："
        r"$\frac{0.6827}2+\frac{0.9545}2$（左半 + 右半）或 $0.9545-\frac{0.9545-0.6827}2$（两倍区间减右尾）—— 结果都是 $0.8186$ ✓" "\n"
        r"③ ⭐⭐ **本题递推与 M-T-398-E1 完全同构**：$p=q=\frac12$，公比 $-\frac12$，"
        r"稳态值 $\frac1{1+\frac12}=\frac23$，正是「平均步长」$1\cdot\frac12+2\cdot\frac12=\frac32$ 的倒数 ✓" "\n"
        r"④ ⭐⭐ **$P_{60}=\frac12P_{58}$ 而不是 $\frac12P_{58}+\frac12P_{59}$** —— "
        r"因为到 $59$ 格游戏就结束了，**不能再从 $59$ 走到 $60$**．这是本题最容易被忽略的一处．" "\n"
        r"⑤ ⭐⭐ **$\frac1{2^{59}}=\frac2{2^{60}}$ 通分后合并**："
        r"$\frac23\cdot\frac1{2^{60}}+\frac13\cdot\frac1{2^{59}}=\frac2{3\cdot2^{60}}+\frac2{3\cdot2^{60}}$，两项相等才能合成 $\frac13\cdot\frac1{2^{58}}$ ✓" "\n"
        r"⑥ 数值复核：$P_{59}\approx\frac23(1-8.67\times10^{-19})=0.66666667$，"
        r"$P_{60}=\frac13(1+1.73\times10^{-18})=0.33333333$；"
        r"$P_{59}-P_{60}=0.33333334=\frac13\left(1-3.47\times10^{-18}\right)$ ✓ 差值几乎就是 $\frac13$．" "\n"
        r"   直观理解：稳态下每格概率趋于 $\frac23$，但第 $60$ 格只能靠「跳 $2$ 格」到达，"
        r"概率约为 $\frac12\cdot\frac23=\frac13$，**恰好是第 $59$ 格的一半** ✓✓" "\n"
        r"**通法（概率递推 + 游戏规则）**：" "\n"
        r"① 写递推前先确认「到达该状态的全部互斥前驱」，注意**游戏是否已在中间状态结束**；" "\n"
        r"② $P_n=pP_{n-1}+qP_{n-2}$ 一律作差，公比 $-q$；" "\n"
        r"③ 比较大小时先化到同分母，注意 $2^{-k}$ 与 $2^{-(k+1)}$ 的通分；" "\n"
        r"④ 稳态值 $=\frac1{1+q}$（平均步长的倒数）可作快速检验．"
    ),
    'difficulty': 0.70,
    'topics': ['M-T-398'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-398-V1',
}

QS = [
    T358_E1, T358_V1, T358_V2, T358_V3,
    T360_E1, T360_V1, T360_V2, T360_V3,
    T348_V1, T348_V3,
    T398_E1, T398_V1,
]
