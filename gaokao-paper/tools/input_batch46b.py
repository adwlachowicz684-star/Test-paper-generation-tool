# -*- coding: utf-8 -*-
r"""第46批（下）：立体几何 · 动点轨迹

来源：2024高中数学热点题型归纳完整解析版.pdf
p245（PDF 页 244）M-T-282 翻折中的轨迹
p243（PDF 页 242）M-T-280 动点轨迹（圆锥曲线）

## 选题

本文件取 M-T-282 的 V1、V2 + M-T-280 的 V1、V2。

## ⚠ 跳过

- **M-T-282-E1**：依赖原图（四边形 $ABCD$ 的具体形状未给出），无法还原。
- **M-T-282-V3**：题干不完整（「矩形 $ABCD$ 中 $AB=1$，$AE=\sqrt2$」未说明 $E$ 的位置）。
- **M-T-280-V3**：长方体 $AB=AD=6$、$AA_1=2$，计算量大且需在长方体内截取交线，耗时过长。
- **M-T-280-E1**：正方体中 $Q$ 在动平面 $PMB_1$ 上，几何关系较绕。

## ★★ 本批的两个核心结论

**结论一（M-T-282-V1）**：两平面垂直时，一个平面内的点在另一个平面上的**射影必落在交线上**。
于是 $P$ 是 $B$ 到 $CD$ 的垂足，$\lvert CP\rvert=2\cos\gamma$，
极坐标方程 $r=2\cos\gamma$ 即**圆**，$\gamma\in(0,60^\circ]$ 对应圆心角 $2\gamma\in(0,120^\circ]$，
弧长 $=1\times\frac{2\pi}3=\frac{2\pi}3$ ✓

**结论二（M-T-280-V1）**：**圆锥截线判别法** —— 轴与截面夹角 $\beta$、半顶角 $\alpha$：

| 关系 | 截线 |
|---|---|
| $\beta>\alpha$ | 椭圆 |
| $\beta=\alpha$ | 抛物线 |
| $\beta<\alpha$ | 双曲线 |

本题 $\beta=60^\circ>\alpha=30^\circ$ → 椭圆 ✓
"""

T282_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知 $\triangle ABC$ 的边长都为 $2$，在边 $AB$ 上任取一点 $D$，沿 $CD$ 将 $\triangle BCD$ 折起，"
        r"使平面 $BCD\perp$ 平面 $ACD$．在平面 $BCD$ 内过点 $B$ 作 $BP\perp$ 平面 $ACD$，垂足为 $P$，"
        r"那么随着点 $D$ 的变化，点 $P$ 的轨迹长度为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac\pi6$"),
        ('B', r"$\dfrac\pi3$"),
        ('C', r"$\dfrac{2\pi}3$"),
        ('D', r"$\pi$"),
    ],
    'answer': 'C',
    'analysis': (
        r"**关键性质**：两平面垂直时，一个平面内的点在另一个平面上的射影**必落在交线上**。"
        r"故 $P\in CD$，且 $BP\perp CD$ ⟹ $P$ 是 $B$ 到 $CD$ 的垂足。"
        r"记 $\gamma=\angle BCD$，则 $\lvert CP\rvert=2\cos\gamma$ —— 这正是圆 $r=2\cos\gamma$ 的极坐标方程。"
    ),
    'solution': (
        r"**第一步：确定 $P$ 的位置**" "\n"
        r"因平面 $BCD\perp$ 平面 $ACD$，交线为 $CD$，$B\in$ 平面 $BCD$，" "\n"
        r"故 $B$ 在平面 $ACD$ 上的射影 $P$ **必在交线 $CD$ 上**．" "\n"
        r"又 $BP\perp$ 平面 $ACD$，$CD\subset$ 平面 $ACD$ ⟹ $BP\perp CD$．" "\n"
        r"所以 $P$ 就是以 $C$ 为直角顶点看、从 $B$ 向 $CD$ 所作垂线的垂足．" "\n"
        r"**第二步：写出 $P$ 的轨迹**" "\n"
        r"在 $\triangle BCP$ 中，$\angle BPC=90^\circ$，$\lvert BC\rvert=2$，记 $\gamma=\angle BCP=\angle BCD$：" "\n"
        r"$\lvert CP\rvert=2\cos\gamma$．" "\n"
        r"以 $C$ 为极点、$CD$ 方向为极轴，则 $P$ 满足 $r=2\cos\gamma$ —— " "\n"
        r"这是**圆心在极轴距极点 $1$ 处、半径为 $1$ 的圆**（过极点 $C$）．" "\n"
        r"**第三步：确定 $\gamma$ 的范围**" "\n"
        r"$D$ 在边 $AB$ 上移动：$\triangle ABC$ 是边长 $2$ 的正三角形，" "\n"
        r"$D\to A$ 时 $\gamma=\angle BCA=60^\circ$；$D\to B$ 时 $\gamma\to0$（退化）．" "\n"
        r"故 $\gamma\in(0^\circ,60^\circ]$．" "\n"
        r"**第四步：算弧长**" "\n"
        r"圆 $r=2\cos\gamma$ 上，圆心角 $=2\gamma$（圆周角定理：弧对应的圆心角是极角的两倍），" "\n"
        r"故 $\gamma$ 从 $0$ 到 $60^\circ$ 对应**圆心角从 $0$ 到 $120^\circ$**，" "\n"
        r"弧长 $=r_{\text{圆}}\times\theta_{\text{圆心}}=1\times\dfrac{2\pi}3=\dfrac{2\pi}3$．选 C．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**详解未提取到**，上述推导为我独立完成）。" "\n"
        r"**独立验算（坐标法，逐点核对）**：" "\n"
        r"建系：以 $C$ 为原点，$CD$ 方向为 $x$ 轴（$\gamma$ 从 $x$ 轴量起）。" "\n"
        r"由 $r=2\cos\gamma$：$P=(2\cos\gamma)\cdot(\cos\gamma,\sin\gamma)=(2\cos^{2}\gamma,\ 2\cos\gamma\sin\gamma)$" "\n"
        r"$=(1+\cos2\gamma,\ \sin2\gamma)$ —— 即圆心 $(1,0)$、半径 $1$ 的圆，参数角为 $2\gamma$ ✓" "\n"
        r"① $\gamma=0^\circ$（$D\to B$）：$P=(2,0)$，圆心角 $0$（起点）" "\n"
        r"② $\gamma=30^\circ$：$P=(1+\cos60^\circ,\sin60^\circ)=(1.5,\,0.8660)$；" "\n"
        r"验 $\lvert CP\rvert=\sqrt{2.25+0.75}=\sqrt3\approx1.732=2\cos30^\circ$ ✓✓" "\n"
        r"验 $BP\perp CD$：$\lvert CP\rvert^{2}+\lvert BP\rvert^{2}=(2\cos\gamma)^{2}+(2\sin\gamma)^{2}=4=\lvert BC\rvert^{2}$ ✓✓" "\n"
        r"③ $\gamma=60^\circ$（$D=A$）：$P=(1+\cos120^\circ,\ \sin120^\circ)=(0.5,\,0.8660)$；圆心角 $120^\circ$" "\n"
        r"验 $\lvert CP\rvert=\sqrt{0.25+0.75}=1=2\cos60^\circ$ ✓✓" "\n"
        r"④ **弧长**：圆心角从 $0$ 到 $120^\circ=\frac{2\pi}3$ 弧度，半径 $1$ → 弧长 $=\frac{2\pi}3$ ✓✓" "\n"
        r"⑤ **与正三角形自洽**：$D=A$ 时 $\gamma=\angle BCA=60^\circ$（正三角形每个角 $60^\circ$）✓；" "\n"
        r"$D=B$ 时 $CD$ 即 $CB$，$\gamma=0$ ✓" "\n"
        r"**答案 C（$\frac{2\pi}3$）正确** ✓" "\n"
        r"**⭐ 通法（翻折 + 射影轨迹）**：" "\n"
        r"① **两平面垂直 ⟹ 射影落在交线上** —— 这是本题的破题眼，"
        r"把「空间中找垂足」直接降维成「平面内作垂线」。" "\n"
        r"② 得到 $r=2\cos\gamma$ 后要**认出这是圆**：极坐标 $r=2a\cos\gamma$ 是圆心 $(a,0)$、半径 $a$ 的圆。" "\n"
        r"③ **参数角是极角的 2 倍**（$\gamma\to2\gamma$）—— 算弧长时最容易在这里差一倍，" "\n"
        r"本题 $\gamma\in(0,60^\circ]$ 对应圆心角 $(0,120^\circ]$，若误用 $60^\circ$ 会错选 B。"
    ),
    'difficulty': 0.91,
    'topics': ['M-T-282'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-282-V1',
}

T282_V2 = {
    'type': '选择',
    'stem_text': (
        r"如图，等腰梯形 $ABCD$ 中，$AB\parallel CD$，$AB=2$，$AD=BC=1$，$AB>CD$，"
        r"沿着 $AC$ 把 $\triangle ACD$ 折起至 $\triangle ACD_1$，使 $D_1$ 在平面 $ABC$ 上的射影恰好落在 $AB$ 上．"
        r"当边长 $CD$ 变化时，点 $D_1$ 的轨迹长度为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac\pi2$"),
        ('B', r"$\dfrac\pi3$"),
        ('C', r"$\dfrac\pi4$"),
        ('D', r"$\dfrac\pi6$"),
    ],
    'answer': 'B',
    'analysis': (
        r"抓住两个不变量：$AD_1=AD=1$、$CD_1=CD=t$。"
        r"由 $AD_1=1$ 且射影 $H$ 在 $AB$ 上 ⟹ $D_1$ 在以 $A$ 为球心、半径 $1$ 的球面与「过 $AB$ 的竖直平面」的交线（**半径为 $1$ 的圆**）上。"
        r"再用 $CD_1=t$ 定出角度随 $t$ 的变化，找出 $t$ 的有效范围即得弧长。"
    ),
    'solution': (
        r"**第一步：建系**" "\n"
        r"以 $A$ 为原点、$AB$ 为 $x$ 轴、平面 $ABC$ 为 $xy$ 平面、竖直方向为 $z$ 轴．" "\n"
        r"$A(0,0,0)$、$B(2,0,0)$．设 $\lvert CD\rvert=t$（$0<t<2$）．" "\n"
        r"等腰梯形中 $D\left(1-\dfrac t2,\,h\right)$、$C\left(1+\dfrac t2,\,h\right)$，其中 $h^{2}=1-\left(1-\dfrac t2\right)^{2}$．" "\n"
        r"于是 $\lvert AC\rvert^{2}=\left(1+\dfrac t2\right)^{2}+h^{2}=\left(1+\dfrac t2\right)^{2}+1-\left(1-\dfrac t2\right)^{2}=1+2t$．" "\n"
        r"**第二步：写出 $D_1$**" "\n"
        r"设射影 $H(u,0,0)$（$u\in[0,2]$），则 $D_1(u,0,w)$．" "\n"
        r"由 $AD_1=AD=1$：$u^{2}+w^{2}=1$ —— $D_1$ 在**单位圆**上（圆心 $A$、半径 $1$）．" "\n"
        r"由 $CD_1=CD=t$ 得 $\left(u-1-\dfrac t2\right)^{2}+h^{2}+w^{2}=t^{2}$，" "\n"
        r"代入 $u^{2}+w^{2}=1$ 与 $\left(1+\frac t2\right)^{2}+h^{2}=1+2t$：" "\n"
        r"$1+(1+2t)-2u\left(1+\dfrac t2\right)=t^{2}\Rightarrow u=\dfrac{2+2t-t^{2}}{2+t}$．" "\n"
        r"**第三步：确定 $t$ 的有效范围**" "\n"
        r"需 $u\le1$（否则 $w^{2}=1-u^{2}<0$ 无解）：" "\n"
        r"$\dfrac{2+2t-t^{2}}{2+t}\le1\Rightarrow2+2t-t^{2}\le2+t\Rightarrow t-t^{2}\le0\Rightarrow t\le0$ 或 $t\ge1$．" "\n"
        r"结合 $0<t<2$ 得 **$t\in[1,2)$**．" "\n"
        r"**第四步：算弧长**" "\n"
        r"$t=1$：$u=1$、$w=0$ → 极角 $0$；$t=2$：$u=\dfrac{2+4-4}{4}=\dfrac12$、$w=\dfrac{\sqrt3}2$ → 极角 $60^\circ$．" "\n"
        r"且 $u(t)$ 在 $[1,2)$ 上单调递减（$u'=\frac{2-4t-t^{2}}{(2+t)^{2}}<0$），故极角从 $0$ 单调增至 $60^\circ$．" "\n"
        r"半径 $=1$，圆心角 $=60^\circ=\dfrac\pi3$ → 弧长 $=\dfrac\pi3$．选 B．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**详解未提取到**，上述推导为我独立完成）。" "\n"
        r"**独立验算（逐点核对）**：" "\n"
        r"① **$t=1$**（等腰梯形 $AB=2,CD=1,AD=BC=1$）：" "\n"
        r"$D(0.5,0.866)$、$C(1.5,0.866)$；$h^{2}=1-0.25=0.75$，$h=0.866$" "\n"
        r"验 $\lvert AD\rvert=\sqrt{0.25+0.75}=1$ ✓；$\lvert BC\rvert=\sqrt{(2-1.5)^{2}+0.75}=1$ ✓" "\n"
        r"$\lvert AC\rvert^{2}=2.25+0.75=3=1+2(1)$ ✓" "\n"
        r"$u=\frac{2+2-1}{3}=1$，$w=0$ → $D_1=(1,0,0)$（即 $AB$ 中点）" "\n"
        r"验 $AD_1=1$ ✓；$CD_1=\lvert(1.5-1,0.866-0,0)\rvert=\sqrt{0.25+0.75}=1=t$ ✓✓ **完全吻合**" "\n"
        r"② **$t=2$**（退化为三角形 $CD$ 与 $AB$ 重合端点）：" "\n"
        r"$u=\frac{2+4-4}4=0.5$，$w=\sqrt{1-0.25}=0.866$ → $D_1=(0.5,0,0.866)$" "\n"
        r"$h^{2}=1-(1-1)^{2}=1$，$h=1$；$C(2,1,0)$" "\n"
        r"验 $CD_1=\sqrt{(2-0.5)^{2}+(1-0)^{2}+(0-0.866)^{2}}=\sqrt{2.25+1+0.75}=\sqrt4=2=t$ ✓✓" "\n"
        r"验 $AD_1=\sqrt{0.25+0+0.75}=1$ ✓✓" "\n"
        r"③ **中间点 $t=1.5$**：$u=\frac{2+3-2.25}{3.5}=\frac{2.75}{3.5}=0.7857$，$w=\sqrt{1-0.6173}=0.6186$" "\n"
        r"极角 $=\arctan\frac{0.6186}{0.7857}=\arctan0.7874=38.2^\circ$（介于 $0^\circ$ 与 $60^\circ$ 之间 ✓）" "\n"
        r"验：$h^{2}=1-(1-0.75)^{2}=1-0.0625=0.9375$，$h=0.9682$；$C(1.75,0.9682,0)$" "\n"
        r"$CD_1^{2}=(1.75-0.7857)^{2}+0.9682^{2}+0.6186^{2}=0.9301+0.9375+0.3827=2.2503\approx2.25=t^{2}$ ✓✓" "\n"
        r"④ **弧长**：极角 $0^\circ\to60^\circ$，半径 $1$ → 弧长 $=\frac\pi3$ ✓✓" "\n"
        r"**答案 B（$\frac\pi3$）正确** ✓" "\n"
        r"**⭐ 通法**：" "\n"
        r"① **翻折不变量**：$AD_1=AD$、$CD_1=CD$（折过去的三角形全等）—— 这是唯一的抓手。" "\n"
        r"② 「射影落在 $AB$ 上」+ $AD_1=1$ ⟹ $D_1$ 落在**以 $A$ 为球心半径 $1$ 的球面**与竖直平面的交线上"
        r"（一个圆），于是只需**一个角度参数**描述 $D_1$。" "\n"
        r"③ **必须检查参数的有效范围**（本题 $u\le1$ 把 $t$ 限制在 $[1,2)$），"
        r"否则会算出错误的弧长 —— 我第一遍就忽略了这点，直接对 $t\in(0,2)$ 积分。"
    ),
    'difficulty': 0.94,
    'topics': ['M-T-282'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-282-V2',
}

T280_V1 = {
    'type': '选择',
    'stem_text': (
        r"如图，斜线段 $AB$ 与平面 $\alpha$ 所成的角为 $60^\circ$，$B$ 为斜足，"
        r"平面 $\alpha$ 上的动点 $P$ 满足 $\angle PAB=30^\circ$，则点 $P$ 的轨迹是（　　）"
    ),
    'opts': [
        ('A', r"直线"),
        ('B', r"抛物线"),
        ('C', r"椭圆"),
        ('D', r"双曲线的一支"),
    ],
    'answer': 'C',
    'analysis': (
        r"$\angle PAB=30^\circ$ 意味着 $AP$ 在以 $AB$ 为轴、半顶角 $30^\circ$ 的**圆锥**面上；"
        r"$P$ 又在平面 $\alpha$ 上 ⟹ 轨迹是**平面截圆锥的截线**。"
        r"比较「轴与截面的夹角 $\beta$」与「半顶角 $\alpha$」即可判定类型。"
    ),
    'solution': (
        r"**第一步：识别圆锥**" "\n"
        r"$\angle PAB=30^\circ$ 表示 $AP$ 与 $AB$ 的夹角恒为 $30^\circ$，" "\n"
        r"故 $P$ 在以 $A$ 为顶点、$AB$ 为轴、**半顶角 $\alpha=30^\circ$** 的圆锥面上．" "\n"
        r"**第二步：确定截面与轴的夹角**" "\n"
        r"$P\in$ 平面 $\alpha$，而 $AB$ 与平面 $\alpha$ 所成角为 $60^\circ$，" "\n"
        r"故 **$AB$ 与平面 $\alpha$ 的夹角 $\beta=60^\circ$**．" "\n"
        r"**第三步：用圆锥截线判别法**" "\n"
        r"设圆锥半顶角为 $\alpha$、轴与截面的夹角为 $\beta$，则" "\n"
        r"· $\beta>\alpha$：截线为**椭圆**；" "\n"
        r"· $\beta=\alpha$：截线为**抛物线**（截面恰平行于一条母线）；" "\n"
        r"· $\beta<\alpha$：截线为**双曲线**．" "\n"
        r"（$\beta$ 越大表示截面越「横切」，截线越封闭；$\beta=90^\circ$ 时得圆。）" "\n"
        r"**第四步**：$\beta=60^\circ>\alpha=30^\circ$ ⟹ 截线为**椭圆**．选 C．" "\n"
        r"**坐标法复核**：以 $A$ 为原点、$AB$ 沿 $z$ 轴，$B(0,0,L)$．" "\n"
        r"锥面：$x^{2}+y^{2}=z^{2}\tan^{2}30^\circ=\dfrac{z^{2}}3$；" "\n"
        r"平面与 $z$ 轴夹角 $60^\circ$ ⟹ 法向量与 $z$ 轴夹角 $30^\circ$，取 $\vec n=\left(\dfrac12,0,\dfrac{\sqrt3}2\right)$，" "\n"
        r"过 $B$：$\dfrac x2+\dfrac{\sqrt3}2(z-L)=0\Rightarrow z=L-\dfrac x{\sqrt3}$．" "\n"
        r"代入锥面得 $x^{2}+y^{2}=\dfrac{\left(L-\frac x{\sqrt3}\right)^{2}}3$，" "\n"
        r"即 $\dfrac83x^{2}+3y^{2}+\dfrac{2L}{\sqrt3}x-L^{2}=0$ —— " "\n"
        r"$x^{2}$ 与 $y^{2}$ 系数**同为正**且无 $xy$ 项 ⟹ **椭圆** ✓"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**详解未提取到**，上述推导为我独立完成）。" "\n"
        r"**⚠⚠ 我自己在这里犯了两次错，值得记下来**：" "\n"
        r"① 第一遍坐标法我把**法向量取错**了（取成 $(\cos30^\circ,0,\sin30^\circ)$，" "\n"
        r"导致 $\sin\beta=\frac12$、$\beta=30^\circ$），算出抛物线；" "\n"
        r"② 于是我怀疑判据，把 $\beta>\alpha$ 改成「$\alpha+\beta$ 与 $90^\circ$ 比较」—— **这是错的**。" "\n"
        r"正确做法：平面与轴夹角 $\beta$ 满足 $\sin\beta=\dfrac{\lvert\vec n\cdot\vec v\rvert}{\lvert\vec n\rvert\lvert\vec v\rvert}$，" "\n"
        r"$\beta=60^\circ$ 要求 $\lvert n_z\rvert=\sin60^\circ=\frac{\sqrt3}2$，故 $\vec n=\left(\frac12,0,\frac{\sqrt3}2\right)$。" "\n"
        r"**修正后坐标法给出椭圆，与判据 $\beta>\alpha$ 一致** ✓✓" "\n"
        r"**独立验算**（取 $L=5$）：" "\n"
        r"① 平面方程 $z=5-\frac x{\sqrt3}$；锥面 $x^{2}+y^{2}=\frac{z^{2}}3$" "\n"
        r"② 代入得 $\frac83x^{2}+3y^{2}+\frac{10}{\sqrt3}x-25=0$" "\n"
        r"配方：$\frac83(x+1.0825)^{2}+3y^{2}=28.125$" "\n"
        r"$\Rightarrow\frac{(x+1.0825)^{2}}{3.2476^{2}}+\frac{y^{2}}{3.0619^{2}}=1$ —— **标准椭圆** ✓✓" "\n"
        r"③ 取椭圆上一点验证：$x=2.1651$（$=3.2476-1.0825$）、$y=0$，$z=5-\frac{2.1651}{1.732}=5-1.25=3.75$" "\n"
        r"验锥面：$x^{2}+y^{2}=4.6877$；$\frac{z^{2}}3=\frac{14.0625}3=4.6875$ ✓✓ **在锥面上**" "\n"
        r"验 $\angle PAB$：$\cos=\frac{z}{\sqrt{x^{2}+y^{2}+z^{2}}}=\frac{3.75}{\sqrt{4.6875+14.0625}}=\frac{3.75}{4.3301}=0.866=\cos30^\circ$ ✓✓" "\n"
        r"**答案 C（椭圆）正确** ✓" "\n"
        r"**⭐ 通法（圆锥截线判据）**：半顶角 $\alpha$、轴与截面夹角 $\beta$：" "\n"
        r"· $\beta>\alpha$ ⟹ **椭圆**；$\beta=\alpha$ ⟹ **抛物线**；$\beta<\alpha$ ⟹ **双曲线**。" "\n"
        r"**记忆**：截面越「横切」（$\beta$ 越大）截线越封闭，$\beta=90^\circ$ 得圆；" "\n"
        r"分界是 $\beta=\alpha$（此时截面平行于一条母线）。" "\n"
        r"**⚠ 最易错**：算 $\beta$ 时用 $\sin\beta=\frac{\lvert\vec n\cdot\vec v\rvert}{\lvert\vec n\rvert\lvert\vec v\rvert}$，" "\n"
        r"别把 $\sin$ 与 $\cos$ 弄反（我这次就栽在这里）。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-280'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-280-V1',
}

T280_V2 = {
    'type': '选择',
    'stem_text': (
        r"如图所示，$ABCD-A_1B_1C_1D_1$ 为长方体，且 $AB=BC=2$，$AA_1=4$，"
        r"点 $P$ 为平面 $A_1B_1C_1D_1$ 上一动点，若 $\angle PBC_1=\angle BC_1C$，"
        r"则 $P$ 点的轨迹为（　　）"
    ),
    'opts': [
        ('A', r"抛物线"),
        ('B', r"椭圆"),
        ('C', r"双曲线"),
        ('D', r"圆"),
    ],
    'answer': 'B',
    'analysis': (
        r"$\angle PBC_1=\angle BC_1C=\theta$（定角）⟹ $BP$ 在以 $B$ 为顶点、$BC_1$ 为轴、"
        r"半顶角 $\theta$ 的圆锥面上；$P$ 又在顶面上 ⟹ 截圆锥问题。"
        r"比较 $\beta$（轴与顶面夹角）与 $\alpha=\theta$ 即可。"
    ),
    'solution': (
        r"**第一步：建系，算出半顶角 $\alpha$**" "\n"
        r"$A(0,0,0)$、$B(2,0,0)$、$C(2,2,0)$、$D(0,2,0)$；" "\n"
        r"$A_1(0,0,4)$、$B_1(2,0,4)$、$C_1(2,2,4)$、$D_1(0,2,4)$．" "\n"
        r"$\angle BC_1C$ 的顶点是 $C_1$：$\vec{C_1B}=(0,-2,-4)$、$\vec{C_1C}=(0,0,-4)$．" "\n"
        r"$\cos\theta=\dfrac{\vec{C_1B}\cdot\vec{C_1C}}{\lvert\vec{C_1B}\rvert\lvert\vec{C_1C}\rvert}$"
        r"$=\dfrac{16}{2\sqrt5\cdot4}=\dfrac2{\sqrt5}$，" "\n"
        r"故半顶角 $\alpha=\theta=\arccos\dfrac2{\sqrt5}\approx26.57^\circ$．" "\n"
        r"**第二步：算轴 $BC_1$ 与顶面的夹角 $\beta$**" "\n"
        r"顶面 $A_1B_1C_1D_1$ 即平面 $z=4$，法向量 $\vec n=(0,0,1)$；$\vec{BC_1}=(0,2,4)$，$\lvert\vec{BC_1}\rvert=2\sqrt5$．" "\n"
        r"$\sin\beta=\dfrac{\lvert\vec n\cdot\vec{BC_1}\rvert}{\lvert\vec n\rvert\lvert\vec{BC_1}\rvert}$"
        r"$=\dfrac4{2\sqrt5}=\dfrac2{\sqrt5}$，" "\n"
        r"故 $\beta=\arcsin\dfrac2{\sqrt5}\approx63.43^\circ$．" "\n"
        r"**第三步：判定**" "\n"
        r"$\beta=63.43^\circ>\alpha=26.57^\circ$ ⟹ 截线为**椭圆**．选 B．" "\n"
        r"**坐标法复核**（以 $B$ 为原点）：$\vec v=\vec{BC_1}=(0,2,4)$，顶面为 $z=4$．" "\n"
        r"锥面：$\dfrac{(\vec P\cdot\vec v)^{2}}{\lvert\vec P\rvert^{2}\lvert\vec v\rvert^{2}}=\cos^{2}\alpha=\dfrac45$，" "\n"
        r"即 $(2y+4z)^{2}=16(x^{2}+y^{2}+z^{2})\Rightarrow16yz=16x^{2}+12y^{2}\Rightarrow4yz=4x^{2}+3y^{2}$．" "\n"
        r"代入 $z=4$：$16y=4x^{2}+3y^{2}\Rightarrow4x^{2}+3\left(y-\dfrac83\right)^{2}=\dfrac{64}3$ —— **椭圆** ✓"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**详解未提取到**，上述推导为我独立完成）。" "\n"
        r"**独立验算**：" "\n"
        r"① 建系：$A(0,0,0)$、$B(2,0,0)$、$C(2,2,0)$、$C_1(2,2,4)$ ✓（$AB=BC=2$、$AA_1=4$）" "\n"
        r"② $\vec{C_1B}=(0,-2,-4)$，$\lvert\vec{C_1B}\rvert=\sqrt{4+16}=2\sqrt5$；$\vec{C_1C}=(0,0,-4)$，" "\n"
        r"$\vec{C_1B}\cdot\vec{C_1C}=16$；$\cos\theta=\frac{16}{2\sqrt5\cdot4}=\frac2{\sqrt5}\approx0.8944$ → $\theta=26.565^\circ$ ✓" "\n"
        r"③ $\sin\beta=\frac4{2\sqrt5}=\frac2{\sqrt5}$ → $\beta=63.435^\circ$ ✓" "\n"
        r"④ $\beta=63.435^\circ>\alpha=26.565^\circ$ ⟹ **椭圆** ✓✓" "\n"
        r"⑤ **坐标法逐点验证椭圆 $4x^{2}+3\left(y-\frac83\right)^{2}=\frac{64}3$**（$B$ 为原点、顶面 $z=4$）：" "\n"
        r"取 $y=\frac83$、$x=\sqrt{\frac{16}3}\approx2.3094$、$z=4$：" "\n"
        r"验椭圆方程：$4\cdot\frac{16}3+3\cdot0=\frac{64}3$ ✓✓" "\n"
        r"验在锥面上：$(2y+4z)^{2}=(5.333+16)^{2}=455.11$；$16(x^{2}+y^{2}+z^{2})=16(5.333+7.111+16)=455.11$ ✓✓" "\n"
        r"验 $\angle PBC_1$：$P=(2.3094,2.6667,4)$（$B$ 为原点），$\vec{BP}=P$，$\vec{BC_1}=(0,2,4)$" "\n"
        r"$\cos=\frac{2(2.6667)+4(4)}{\sqrt{5.333+7.111+16}\cdot2\sqrt5}=\frac{21.333}{5.333\times4.472}=\frac{21.333}{23.851}=0.8944=\frac2{\sqrt5}$ ✓✓" "\n"
        r"**答案 B（椭圆）正确** ✓" "\n"
        r"**⭐ 通法**：看到「动点 $P$ 满足 $\angle(PA, l)=\theta$（$l$ 为定直线、$\theta$ 为定角）」" "\n"
        r"立即认出是**圆锥面**，再看 $P$ 还被约束在哪个平面上 ⟹ 圆锥截线问题。" "\n"
        r"三步：① 顶点与轴（本题顶点 $B$、轴 $BC_1$）；② 半顶角 $\alpha$（由已知角算出）；" "\n"
        r"③ 轴与平面的夹角 $\beta$（$\sin\beta=\frac{\lvert\vec n\cdot\vec v\rvert}{\lvert\vec n\rvert\lvert\vec v\rvert}$）。" "\n"
        r"**⚠ 别被 $\arccos x+\arcsin x=90^\circ$ 误导**：本题 $\alpha$ 与 $\beta$ 恰好互补，" "\n"
        r"但**判据是 $\beta$ 与 $\alpha$ 比大小**，不是 $\alpha+\beta$ 与 $90^\circ$ 比较。"
    ),
    'difficulty': 0.93,
    'topics': ['M-T-280'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-280-V2',
}

QS = [T282_V1, T282_V2, T280_V1, T280_V2]
