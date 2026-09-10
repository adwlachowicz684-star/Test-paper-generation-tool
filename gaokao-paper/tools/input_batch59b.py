# -*- coding: utf-8 -*-
r"""第59批（二）：焦点三角形中的垂直与等腰（6 题） 来源：2024高中数学热点题型归纳完整解析版.pdf p346（PDF 页 345）M-T-365｜p303（PDF 页 302）M-T-366 ## ★★ 本批的头号结论：$FA\perp FB$ 且 $A,B$ 关于原点对称 ⟹ $A,B$ 在半径为 $c$ 的圆上 设椭圆 $A(x,y)$、$B(-x,-y)$、$F(c,0)$： $$\overrightarrow{FA}\cdot\overrightarrow{FB}=(x-c)(-x-c)-y^{2}=c^{2}-x^{2}-y^{2}=0 \ \Longrightarrow\ x^{2}+y^{2}=c^{2}$$ **一个方程直接给出「$A$ 在以原点为圆心、$c$ 为半径的圆上」**，配合椭圆方程就能解出坐标， 进而把两个焦半径都表示出来。M-T-365-V2 整题就靠这一步。 ## ★★ 双曲线同支/异支用定义时的符号 | 情形 | 关系 | |---|---| | $P$ 在右支 | $\lvert PF_{\text{左}}\rvert-\lvert PF_{\text{右}}\rvert=2a$ | | $P$ 在左支 | $\lvert PF_{\text{右}}\rvert-\lvert PF_{\text{左}}\rvert=2a$ | **口诀：远的减近的 $=2a$。** 本批 M-T-366-V1/V3 都靠它，写反就得到 $b=0$ 这类荒谬结果。 ## 六题验算 | 题 | 关键 | 答案 | |---|---|---| | M-T-365-V1 | $e=\frac1{\sin\theta+\cos\theta}$，$\theta=\frac\pi6$ 时最小 | $\sqrt3-1$ | | M-T-365-V2 | $x^{2}+y^{2}=c^{2}$，$\lvert y\rvert=\frac{b^{2}}c$，$\frac{\sqrt2}2\le e\le\sqrt3-1$ | $[\frac{\sqrt2}2,\sqrt3-1]$ | | M-T-365-V3 | $Q(0.6c,0.8c)$，$0.36e^{2}+\frac{0.64e^{2}}{1-e^{2}}=1$ | $\frac{\sqrt5}3$ | | M-T-366-E1 | $A(-\frac{a^{2}}c,\frac{ab}c)$，$B$ 为 $AF_1$ 中点，$c^{2}=2a^{2}$ | $\sqrt2$ | | M-T-366-V1 | 等腰直角 ⟹ $d=2\sqrt2a$，$\cos$ 传递 | $\sqrt3$ | | M-T-366-V3 | 与 V1 同构（都是等腰直角 + 同侧差 $4a$） | $\sqrt3$ | """

T365_V1 = {
    'type': '选择',
    'stem_text': (
        r"椭圆 $C:\dfrac{x^{2}}{a^{2}}+\dfrac{y^{2}}{b^{2}}=1\ (a>b>0)$ 的左、右焦点分别为 $F_1,F_2$，"
        r"直线 $l:y=kx$ 与 $C$ 交于 $A,B$ 两点，若 $\lvert F_2O\rvert=\dfrac12\lvert AB\rvert$，"
        r"$\angle BAF_2=\theta$，当 $\theta\in\left[\dfrac\pi{12},\dfrac\pi6\right]$ 时，$C$ 的离心率的最小值为（　　）"
    ),
    'opts': [
        ('A', r"$\sqrt2-1$"),
        ('B', r"$\dfrac{\sqrt2}2$"),
        ('C', r"$\dfrac{\sqrt6}3$"),
        ('D', r"$\sqrt3-1$"),
    ],
    'answer': 'D',
    'analysis': (
        r"$A,B$ 关于原点对称 ⟹ $\lvert AB\rvert=2\lvert OA\rvert$，故 $\lvert OA\rvert=\lvert F_2O\rvert=c$。"
        r"于是 $\triangle OAF_2$ 为等腰三角形，$\cos\theta=\sin\frac\varphi2$；推出 $e=\frac1{\sin\theta+\cos\theta}$，$\theta$ 越大 $e$ 越小。"
    ),
    'solution': (
        r"**第一步：把长度条件翻译成 $\lvert OA\rvert=c$**" "\n"
        r"$l:y=kx$ 过原点，$A,B$ 关于 $O$ 对称 ⟹ $\lvert AB\rvert=2\lvert OA\rvert$。" "\n"
        r"由 $\lvert F_2O\rvert=\dfrac12\lvert AB\rvert$ 得 $c=\lvert OA\rvert$．" "\n"
        r"**第二步：设 $A$ 的极坐标**" "\n"
        r"设 $A=c(\cos\varphi,\sin\varphi)$，则 $B=-A$，$\overrightarrow{AB}=-2A$。" "\n"
        r"$\overrightarrow{AF_2}=F_2-A=c(1,0)-c(\cos\varphi,\sin\varphi)=c(1-\cos\varphi,-\sin\varphi)$．" "\n"
        r"**第三步：用 $\angle BAF_2=\theta$**" "\n"
        r"$\cos\theta=\dfrac{\overrightarrow{AB}\cdot\overrightarrow{AF_2}}{\lvert AB\rvert\lvert AF_2\rvert} =\dfrac{-2c^{2}\left[\cos\varphi(1-\cos\varphi)-\sin^{2}\varphi\right]}{2c\cdot c\sqrt{(1-\cos\varphi)^{2}+\sin^{2}\varphi}}$" "\n"
        r"$=\dfrac{-2c^{2}(\cos\varphi-1)}{2c^{2}\sqrt{2-2\cos\varphi}}=\dfrac{2(1-\cos\varphi)}{2\sqrt{2(1-\cos\varphi)}}=\sqrt{\dfrac{1-\cos\varphi}2}=\sin\dfrac\varphi2$．" "\n"
        r"故 $\dfrac\varphi2=\dfrac\pi2-\theta$，即 $\varphi=\pi-2\theta$，$A=c(-\cos2\theta,\ \sin2\theta)$．" "\n"
        r"**第四步：$A$ 在椭圆上**" "\n"
        r"$\dfrac{c^{2}\cos^{2}2\theta}{a^{2}}+\dfrac{c^{2}\sin^{2}2\theta}{b^{2}}=1 \Rightarrow e^{2}\cos^{2}2\theta+\dfrac{e^{2}\sin^{2}2\theta}{1-e^{2}}=1$．" "\n"
        r"整理（记 $u=e^{2}$）：$u^{2}\cos^{2}2\theta-2u+1=0\Rightarrow u=\dfrac{1-\sin2\theta}{\cos^{2}2\theta}=\dfrac1{1+\sin2\theta}$．" "\n"
        r"即 $e=\dfrac1{\sqrt{1+\sin2\theta}}=\dfrac1{\sin\theta+\cos\theta}$．" "\n"
        r"**第五步：取最小值**" "\n"
        r"$\theta\in\left[\dfrac\pi{12},\dfrac\pi6\right]$ 上 $\sin\theta+\cos\theta$ 递增，故 $e$ 递减，" "\n"
        r"$e_{\min}=\dfrac1{\sin\frac\pi6+\cos\frac\pi6}=\dfrac1{\frac12+\frac{\sqrt3}2}=\dfrac2{1+\sqrt3}=\sqrt3-1$．选 D．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓。原书 p346 详解：" "\n"
        r"「连接 $AF_1$，由题知点 $A$、$B$ 关于原点对称，$AF_1=BF_1$…$AB=2\\lvert OF_1\\rvert=2c$，$FA_1\\perpFB_1$，" "\n"
        r"则 $\\lvert FA_1\\rvert=2c\\cos\\theta$，$\\lvert FB_1\\rvert=2c\\sin\\theta$，又 $\\lvert FA_1\\rvert+\\lvert FB_1\\rvert=2a$，" "\n"
        r"即 $2c\\cos\\theta+2c\\sin\\theta=2a$，$e=\\frac{c}{a}=\\frac{1}{\\sin\\theta+\\cos\\theta}=\\frac{1}{\\sqrt2\\sin(\\theta+\\frac\\pi4)}$…" "\n"
        r"所以 $e_{\\min}=\\sqrt3-1$**」**与我的结果完全一致** ✓✓✓" "\n"
        r"（原书用的是「补连另一焦点 + 定义」的路子，我用极坐标直算，**两条路殊途同归**）" "\n"
        r"**⚠ 选项还原**：原文提取为 `2-1 22 63 3-1`，按 A $\\sqrt2-1$、B $\\frac{\\sqrt2}2$、C $\\frac{\\sqrt6}3$、D $\\sqrt3-1$ 还原。" "\n"
        r"**独立验算**：" "\n"
        r"① **两法对照**：我的 $e=\\frac1{\\sqrt{1+\\sin2\\theta}}$ 与原书的 $e=\\frac1{\\sin\\theta+\\cos\\theta}$" "\n"
        r"$(\\sin\\theta+\\cos\\theta)^2=\\sin^2+\\cos^2+2\\sin\\theta\\cos\\theta=1+\\sin2\\theta$ ✓✓✓ **完全相同**" "\n"
        r"② **端点值**：$\\theta=\\frac\\pi6$：$\\sin+\\cos=0.5+0.86603=1.36603$，$e=\\frac1{1.36603}=0.73205$" "\n"
        r"$\\sqrt3-1=1.73205-1=0.73205$ ✓✓✓ **恰为选项 D**" "\n"
        r"③ **另一端**：$\\theta=\\frac\\pi{12}$：$\\sin15^\\circ+\\cos15^\\circ=0.25882+0.96593=1.22474$，$e=0.81650$" "\n"
        r"$\\frac{\\sqrt6}3=\\frac{2.44949}3=0.81650$ ✓✓ **这正是选项 C（$e$ 的最大值）**" "\n"
        r"⟹ $e\\in[\\sqrt3-1,\\ \\frac{\\sqrt6}3]$，**最小值 $\\sqrt3-1$** ✓✓✓" "\n"
        r"（**命题人把最大值 $\\frac{\\sqrt6}3$ 放在 C**，专等「求最小值看成最大值」的人 —— 很好的陷阱）" "\n"
        r"④ **$\\cos\\theta=\\sin\\frac\\varphi2$ 的验证**：分母 $\\sqrt{(1-\\cos\\varphi)^2+\\sin^2\\varphi}=\\sqrt{2-2\\cos\\varphi}$ ✓" "\n"
        r"分子（点积）$=-2c^2[\\cos\\varphi-\\cos^2\\varphi-\\sin^2\\varphi]=-2c^2(\\cos\\varphi-1)=2c^2(1-\\cos\\varphi)$ ✓✓" "\n"
        r"比值 $=\\frac{2c^2(1-\\cos\\varphi)}{2c\\cdot c\\sqrt{2(1-\\cos\\varphi)}}=\\sqrt{\\frac{1-\\cos\\varphi}{2}}=\\sin\\frac\\varphi2$ ✓✓✓" "\n"
        r"⑤ **$u$ 的求解**：$u^2\\cos^2 2\\theta-2u+1=0$，$u=\\frac{2\\pm\\sqrt{4-4\\cos^2 2\\theta}}{2\\cos^2 2\\theta}=\\frac{1\\pm\\sin2\\theta}{\\cos^2 2\\theta}$" "\n"
        r"取 $u<1$：$\\frac{1-\\sin2\\theta}{(1-\\sin2\\theta)(1+\\sin2\\theta)}=\\frac1{1+\\sin2\\theta}$ ✓✓✓" "\n"
        r"⑥ **排除其他**：A $=\\sqrt2-1=0.414$、B $=\\frac{\\sqrt2}2=0.707$、C $=\\frac{\\sqrt6}3=0.816$（这是**最大**值）✗" "\n"
        r"**答案 D（$\\sqrt3-1$）正确** ✓" "\n"
        r"**⭐ 通法（过原点的弦 + 焦点）**：" "\n"
        r"① ⭐⭐ **过原点的直线与中心对称曲线交于 $A,B$ ⟹ $B=-A$** ⟹ " "\n"
        r"$\\lvert AB\\rvert=2\\lvert OA\\rvert$、且 $\\lvert BF_1\\rvert=\\lvert AF_2\\rvert$（**补连另一焦点的依据**）；" "\n"
        r"② ⭐ **「$\\lvert OA\\rvert=c$」这类条件 ⟹ $A$ 在半径为 $c$ 的圆上** ⟹ 直接用极坐标设 $A=c(\\cos\\varphi,\\sin\\varphi)$；" "\n"
        r"③ 求 $\\angle BAF_2$ 这类角，**用向量点积**而不是几何作图，方向不会错；" "\n"
        r"④ ⚠ **看清问的是最小值还是最大值** —— 本题 C 选项就是另一端点，命题人专门备的；" "\n"
        r"⑤ 两条路线（极坐标直算 / 补焦点用定义）**结果必须一致**，不一致说明某处符号错了。"
    ),
    'difficulty': 0.93,
    'topics': ['M-T-365'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-365-V1',
}

T365_V2 = {
    'type': '选择',
    'stem_text': (
        r"设椭圆 $C:\dfrac{x^{2}}{a^{2}}+\dfrac{y^{2}}{b^{2}}=1\ (a>b>0)$ 的右焦点为 $F$，椭圆 $C$ 上的两点 $A,B$ 关于原点对称，"
        r"且满足 $\overrightarrow{FA}\cdot\overrightarrow{FB}=0$，$\lvert FB\rvert\le\lvert FA\rvert\le\sqrt3\,\lvert FB\rvert$，"
        r"则椭圆 $C$ 的离心率的取值范围为（　　）"
    ),
    'opts': [
        ('A', r"$\left[\dfrac{\sqrt2}2,1\right)$"),
        ('B', r"$\left[\dfrac{\sqrt2}2,\sqrt3-1\right]$"),
        ('C', r"$\left[\sqrt3-1,1\right)$"),
        ('D', r"$\left[\dfrac{\sqrt2}2,\dfrac{\sqrt3}2\right]$"),
    ],
    'answer': 'B',
    'analysis': (
        r"点积为 $0$ 给出 $x^{2}+y^{2}=c^{2}$（**关键一步**），联立椭圆方程得 $\lvert y\rvert=\frac{b^{2}}c$、$x^{2}=\frac{c^{4}-b^{4}}{c^{2}}$。"
        r"$\lvert FB\rvert\le\lvert FA\rvert$ 给 $x\le0$，$\lvert FA\rvert\le\sqrt3\lvert FB\rvert$ 给 $x\ge-\frac c2$，解得 $\frac{\sqrt2}2\le e\le\sqrt3-1$。"
    ),
    'solution': (
        r"**第一步：点积条件 ⟹ $A$ 在圆上**" "\n"
        r"设 $A(x,y)$，则 $B(-x,-y)$，$F(c,0)$。" "\n"
        r"$\overrightarrow{FA}=(x-c,y)$，$\overrightarrow{FB}=(-x-c,-y)$，" "\n"
        r"$\overrightarrow{FA}\cdot\overrightarrow{FB}=(x-c)(-x-c)-y^{2}=-(x^{2}-c^{2})-y^{2}=c^{2}-x^{2}-y^{2}=0$，" "\n"
        r"即 $x^{2}+y^{2}=c^{2}$．" "\n"
        r"**第二步：联立椭圆方程**" "\n"
        r"由 $x^{2}=c^{2}-y^{2}$ 代入 $\dfrac{x^{2}}{a^{2}}+\dfrac{y^{2}}{b^{2}}=1$：" "\n"
        r"$\dfrac{c^{2}-y^{2}}{a^{2}}+\dfrac{y^{2}}{b^{2}}=1\Rightarrow y^{2}\left(\dfrac1{b^{2}}-\dfrac1{a^{2}}\right)=1-\dfrac{c^{2}}{a^{2}}=1-e^{2}$" "\n"
        r"$y^{2}\cdot\dfrac{a^{2}-b^{2}}{a^{2}b^{2}}=\dfrac{b^{2}}{a^{2}}\Rightarrow y^{2}\cdot\dfrac{c^{2}}{a^{2}b^{2}}=\dfrac{b^{2}}{a^{2}}\Rightarrow y^{2}=\dfrac{b^{4}}{c^{2}}$，" "\n"
        r"$\lvert y\rvert=\dfrac{b^{2}}c$，$x^{2}=c^{2}-\dfrac{b^{4}}{c^{2}}=\dfrac{c^{4}-b^{4}}{c^{2}}$．" "\n"
        r"**第三步：用长度不等式**" "\n"
        r"$\lvert FA\rvert^{2}=(x-c)^{2}+y^{2}=x^{2}-2cx+c^{2}+y^{2}=2c^{2}-2cx$（因 $x^{2}+y^{2}=c^{2}$）；" "\n"
        r"$\lvert FB\rvert^{2}=(-x-c)^{2}+y^{2}=2c^{2}+2cx$．" "\n"
        r"$\lvert FB\rvert\le\lvert FA\rvert\Rightarrow2c^{2}+2cx\le2c^{2}-2cx\Rightarrow x\le0$；" "\n"
        r"$\lvert FA\rvert\le\sqrt3\lvert FB\rvert\Rightarrow2c^{2}-2cx\le3(2c^{2}+2cx)=6c^{2}+6cx\Rightarrow-4c^{2}\le8cx\Rightarrow x\ge-\dfrac c2$．" "\n"
        r"即 $-\dfrac c2\le x\le0$．" "\n"
        r"**第四步：转成 $e$ 的范围**" "\n"
        r"$x\le0$ 且 $x^{2}=\dfrac{c^{4}-b^{4}}{c^{2}}$ ⟹ $x=-\dfrac{\sqrt{c^{4}-b^{4}}}{c}$，需 $c^{4}\ge b^{4}$ 即 $c\ge b$：" "\n"
        r"$c^{2}\ge b^{2}=a^{2}-c^{2}\Rightarrow2c^{2}\ge a^{2}\Rightarrow e\ge\dfrac{\sqrt2}2$．" "\n"
        r"$x\ge-\dfrac c2\Rightarrow\dfrac{\sqrt{c^{4}-b^{4}}}{c}\le\dfrac c2\Rightarrow c^{4}-b^{4}\le\dfrac{c^{4}}4\Rightarrow b^{4}\ge\dfrac{3c^{4}}4\Rightarrow\dfrac{b^{2}}{c^{2}}\ge\dfrac{\sqrt3}2$；" "\n"
        r"$\dfrac{1-e^{2}}{e^{2}}\ge\dfrac{\sqrt3}2\Rightarrow\dfrac1{e^{2}}\ge\dfrac{2+\sqrt3}2\Rightarrow e^{2}\le\dfrac2{2+\sqrt3}=4-2\sqrt3$．" "\n"
        r"而 $4-2\sqrt3=(\sqrt3-1)^{2}$，故 $e\le\sqrt3-1$．" "\n"
        r"综上 $e\in\left[\dfrac{\sqrt2}2,\ \sqrt3-1\right]$．选 B．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓。原书 p346 详解：" "\n"
        r"「连接 $AF_1$，由题知点 $A$、$B$ 关于原点对称，$AF_1=BF_1$…$FA_1\\perpFB_1$，则 $\\lvert FA_1\\rvert=2c\\cos\\theta$…" "\n"
        r"所以，椭圆的离心率取值范围是 $[\\ ,1)$。故选：**D**」" "\n"
        r"⚠ **原书此处与答案标注不一致**：p346 顶部这段文字的结论写「$[\\ ,1)$，故选 D」，" "\n"
        r"但 p346 下方 M-T-365-V2 的独立答案标注为 **B**。我按下方明确的 $[\\frac{\\sqrt2}2,\\sqrt3-1]$（=B）录入。" "\n"
        r"**独立验算**：" "\n"
        r"① ⭐ **点积 ⟹ 圆**：$(x-c)(-x-c)+y(-y)=-(x^2-c^2)-y^2=c^2-x^2-y^2=0$ ✓✓✓" "\n"
        r"⟹ $x^2+y^2=c^2$ ✓✓ **这是本题的破题眼**" "\n"
        r"② **$\\lvert y\\rvert=\\frac{b^2}{c}$**：$y^2\\frac{a^2-b^2}{a^2b^2}=1-\\frac{c^2}{a^2}=\\frac{b^2}{a^2}$" "\n"
        r"$y^2\\frac{c^2}{a^2b^2}=\\frac{b^2}{a^2}\\Rightarrowy^2=\\frac{b^4}{c^2}$ ✓✓✓" "\n"
        r"③ **$x^2$**：$c^2-\\frac{b^4}{c^2}=\\frac{c^4-b^4}{c^2}$ ✓✓" "\n"
        r"④ **$\\lvert FA\\rvert^2=2c^2-2cx$**：$x^2-2cx+c^2+y^2=(x^2+y^2)+c^2-2cx=2c^2-2cx$ ✓✓✓" "\n"
        r"⑤ **不等式**：$\\lvert FB\\rvert\\le\\lvert FA\\rvert\\Rightarrow2c^2+2cx\\le2c^2-2cx\\Rightarrowx\\le0$ ✓" "\n"
        r"$\\lvert FA\\rvert\\le\\sqrt3\\lvert FB\\rvert\\Rightarrow2c^2-2cx\\le6c^2+6cx\\Rightarrow-4c^2\\le8cx\\Rightarrowx\\ge-\\frac c2$ ✓✓" "\n"
        r"⑥ **下界**：$c\\geb\\Rightarrowc^2\\gea^2-c^2\\Rightarrowe^2\\ge\\frac12\\Rightarrowe\\ge\\frac{\\sqrt2}2=0.70711$ ✓✓" "\n"
        r"⑦ **上界**：$\\frac{1-e^2}{e^2}\\ge\\frac{\\sqrt3}{2}=0.86603\\Rightarrow\\frac1{e^2}\\ge1.86603\\Rightarrowe^2\\le0.53590$" "\n"
        r"$4-2\\sqrt3=4-3.46410=0.53590$ ✓✓$(\\sqrt3-1)^2=3-2\\sqrt3+1=4-2\\sqrt3$ ✓✓✓" "\n"
        r"$e\\le\\sqrt3-1=0.73205$ ✓✓✓" "\n"
        r"⑧ **区间自洽**：$\\frac{\\sqrt2}2=0.70711\\le0.73205=\\sqrt3-1$ ✓ 区间非空 ✓" "\n"
        r"⑨ **端点构造检验**：取 $e=\\sqrt3-1$（$a=1,c=0.73205,b^2=1-0.53590=0.46410,b=0.68125$）" "\n"
        r"$y^2=\\frac{b^4}{c^2}=\\frac{0.21539}{0.53590}=0.40191$，$y=0.63396$" "\n"
        r"$x^2=\\frac{c^4-b^4}{c^2}=\\frac{0.28719-0.21539}{0.53590}=\\frac{0.07180}{0.53590}=0.13398$，$x=-0.36603=-\\frac{c}{2}$ ✓✓ **恰为边界**" "\n"
        r"$\\lvert FA\\rvert^2=2c^2-2cx=2(0.53590)-2(0.73205)(-0.36603)=1.07180+0.53590=1.60770$" "\n"
        r"$\\lvert FB\\rvert^2=2c^2+2cx=1.07180-0.53590=0.53590$" "\n"
        r"$\\frac{\\lvert FA\\rvert^2}{\\lvert FB\\rvert^2}=\\frac{1.60770}{0.53590}=3.000$ ✓✓✓ **$\\lvert FA\\rvert=\\sqrt3\\lvert FB\\rvert$ 恰好取等**" "\n"
        r"⑩ **排除其他**：A $[\\frac{\\sqrt2}2,1)$ 上界过大；C $[\\sqrt3-1,1)$ 下界反了（且 $\\sqrt3-1<1$）；" "\n"
        r"D $[\\frac{\\sqrt2}2,\\frac{\\sqrt3}2]$ 上界 $\\frac{\\sqrt3}2=0.866$ ≠ $\\sqrt3-1$ ✗" "\n"
        r"**答案 B（$[\\frac{\\sqrt2}2,\\sqrt3-1]$）正确** ✓" "\n"
        r"**⭐⭐ 通法（对称两点 + 焦点垂直）**：" "\n"
        r"① ⭐⭐ **$A,B$ 关于原点对称 + $\\overrightarrow{FA}\\cdot\\overrightarrow{FB}=0$ ⟹ $x^{2}+y^{2}=c^{2}$** —— " "\n"
        r"推导只有一行：$c^{2}-x^{2}-y^{2}=0$。**这个结论可直接记**；" "\n"
        r"② 有了 $x^{2}+y^{2}=c^{2}$，联立椭圆方程即可解出 $\\lvert y\\rvert=\\frac{b^{2}}c$，一切迎刃而解；" "\n"
        r"③ ⭐ **$\\lvert FA\\rvert^{2}=2c^{2}\\mp2cx$** 的化简只用了一次 $x^{2}+y^{2}=c^{2}$，别去展开 $(x-c)^{2}+y^{2}$ 后硬算；" "\n"
        r"④ ⚠ **两个不等式分别给出 $x$ 的下界和 $e$ 的上界**，方向别弄混：" "\n"
        r"$\\lvert FB\\rvert\\le\\lvert FA\\rvert$ 定 $x$ 的符号；$\\lvert FA\\rvert\\le\\sqrt3\\lvert FB\\rvert$ 定 $e$ 的上界；" "\n"
        r"⑤ 最后 $\\sqrt{4-2\\sqrt3}=\\sqrt3-1$ 这个配方要熟（$(\\sqrt3-1)^{2}=4-2\\sqrt3$）。"
    ),
    'difficulty': 0.94,
    'topics': ['M-T-365'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-365-V2',
}

T365_V3 = {
    'type': '选择',
    'stem_text': (
        r"设椭圆 $C:\dfrac{x^{2}}{a^{2}}+\dfrac{y^{2}}{b^{2}}=1\ (a>b>0)$ 的左焦点为 $F$，$O$ 为坐标原点．"
        r"过点 $F$ 且斜率为 $\dfrac12$ 的直线与 $C$ 的一个交点为 $Q$（点 $Q$ 在 $x$ 轴上方），"
        r"且 $\lvert OF\rvert=\lvert OQ\rvert$，则 $C$ 的离心率为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac{\sqrt3}2$"),
        ('B', r"$\dfrac13$"),
        ('C', r"$\dfrac23$"),
        ('D', r"$\dfrac{\sqrt5}3$"),
    ],
    'answer': 'D',
    'analysis': (
        r"$\lvert OF\rvert=c$、$\lvert OQ\rvert=c$，$Q$ 在 $y=\frac12(x+c)$ 上 ⟹ 解得 $Q(0.6c,0.8c)$（另一个解是 $F$ 本身）。"
        r"代入椭圆：$0.36e^{2}+\frac{0.64e^{2}}{1-e^{2}}=1\Rightarrow e^{2}=\frac59$。"
    ),
    'solution': (
        r"**第一步：设直线并解 $Q$**" "\n"
        r"$F(-c,0)$，直线 $l:y=\dfrac12(x+c)$．设 $Q=(x,y)$，则 $y=\dfrac12(x+c)$，且 $x^{2}+y^{2}=c^{2}$（由 $\lvert OQ\rvert=\lvert OF\rvert=c$）．" "\n"
        r"代入：$x^{2}+\dfrac{(x+c)^{2}}4=c^{2}\Rightarrow4x^{2}+x^{2}+2cx+c^{2}=4c^{2}\Rightarrow5x^{2}+2cx-3c^{2}=0$" "\n"
        r"$\Rightarrow(5x-3c)(x+c)=0\Rightarrow x=\dfrac{3c}5$ 或 $x=-c$．" "\n"
        r"$x=-c$ 对应 $y=0$（即 $F$ 点，舍）；由 $Q$ 在 $x$ 轴上方取 $x=\dfrac{3c}5$，$y=\dfrac12\left(\dfrac{3c}5+c\right)=\dfrac{4c}5$．" "\n"
        r"即 $Q\left(\dfrac{3c}5,\dfrac{4c}5\right)$（验：$0.36c^{2}+0.64c^{2}=c^{2}$ ✓）．" "\n"
        r"**第二步：代入椭圆方程**" "\n"
        r"$\dfrac{(3c/5)^{2}}{a^{2}}+\dfrac{(4c/5)^{2}}{b^{2}}=1\Rightarrow\dfrac{9c^{2}}{25a^{2}}+\dfrac{16c^{2}}{25b^{2}}=1$．" "\n"
        r"记 $e=\dfrac ca$，$b^{2}=a^{2}(1-e^{2})$：$\dfrac{9e^{2}}{25}+\dfrac{16e^{2}}{25(1-e^{2})}=1$．" "\n"
        r"**第三步：解方程**" "\n"
        r"$9e^{2}(1-e^{2})+16e^{2}=25(1-e^{2})$" "\n"
        r"$9e^{2}-9e^{4}+16e^{2}=25-25e^{2}$" "\n"
        r"$-9e^{4}+50e^{2}-25=0\Rightarrow9e^{4}-50e^{2}+25=0$" "\n"
        r"$e^{2}=\dfrac{50\pm\sqrt{2500-900}}{18}=\dfrac{50\pm40}{18}$ ⟹ $e^{2}=5$（舍，$e<1$）或 $e^{2}=\dfrac{10}{18}=\dfrac59$．" "\n"
        r"$e=\dfrac{\sqrt5}3$．选 D．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**详解未提取**，上述推导为我独立完成）。" "\n"
        r"**⚠ 选项还原**：原文提取为 `32 13 23 53`（根号丢失），按 A $\\frac{\\sqrt3}2$、B $\\frac13$、C $\\frac23$、D $\\frac{\\sqrt5}3$ 还原。" "\n"
        r"**判定依据**：我的推导给出 $e=\\frac{\\sqrt5}3$ 且答案为 D。" "\n"
        r"**独立验算**：" "\n"
        r"① **$Q$ 的求解**：$x^2+\\frac{(x+c)^2}{4}=c^2\\Rightarrow5x^2+2cx-3c^2=0$" "\n"
        r"判别式 $=4c^2+60c^2=64c^2$，$\\sqrt{}=8c$，$x=\\frac{-2c\\pm8c}{10}=\\frac{3c}{5}$ 或 $-c$ ✓✓✓" "\n"
        r"（$(5x-3c)(x+c)=5x^2+5cx-3cx-3c^2=5x^2+2cx-3c^2$ ✓✓）" "\n"
        r"② **$y=\\frac12(\\frac{3c}{5}+c)=\\frac12\\cdot\\frac{8c}{5}=\\frac{4c}{5}$** ✓✓ **$(0.6c,0.8c)$ 是经典的 $3$-$4$-$5$ 勾股点**" "\n"
        r"③ **$\\lvert OQ\\rvert$**：$\\sqrt{0.36c^2+0.64c^2}=c$ ✓✓✓ **恒等于 $\\lvert OF\\rvert$**（说明这个条件只用来定 $Q$ 的位置）" "\n"
        r"④ **代入椭圆**：$\\frac{9c^2}{25a^2}+\\frac{16c^2}{25b^2}=1$ ✓✓" "\n"
        r"⑤ **方程**：$9e^2(1-e^2)+16e^2=25(1-e^2)$" "\n"
        r"$9e^2-9e^4+16e^2=25-25e^2\\Rightarrow-9e^4+50e^2-25=0$ ✓✓✓" "\n"
        r"$e^2=\\frac{50\\pm\\sqrt{2500-4\\cdot9\\cdot25}}{18}=\\frac{50\\pm\\sqrt{2500-900}}{18}=\\frac{50\\pm40}{18}$ ✓✓" "\n"
        r"$e^2=5$（舍）或 $\\frac{10}{18}=\\frac59$ ✓✓✓$e=\\frac{\\sqrt5}{3}=0.74536$ ✓✓✓ **恰为选项 D**" "\n"
        r"⑥ **回代检验**：$e^2=\\frac59$，$1-e^2=\\frac49$，$b^2=\\frac49a^2$" "\n"
        r"$\\frac{9}{25}\\cdot\\frac59+\\frac{16}{25}\\cdot\\frac{5/9}{4/9}=\\frac{45}{225}+\\frac{16}{25}\\cdot\\frac54=\\frac15+\\frac{16}{25}\\cdot\\frac54$" "\n"
        r"$=\\frac15+\\frac{80}{100}=\\frac15+\\frac45=1$ ✓✓✓ **完全成立**" "\n"
        r"⑦ **几何构造检验**：取 $a=1,c=\\frac{\\sqrt5}3=0.74536,b^2=1-\\frac59=\\frac49,b=0.66667$" "\n"
        r"$Q=(0.6\\cdot0.74536,0.8\\cdot0.74536)=(0.44721,0.59628)$" "\n"
        r"验 $\\frac{x^2}{a^2}+\\frac{y^2}{b^2}=\\frac{0.2}{1}+\\frac{0.35556}{0.44444}=0.2+0.8=1$ ✓✓✓ **$Q$ 确在椭圆上**" "\n"
        r"且在 $l$ 上：$\\frac12(0.44721+0.74536)=\\frac12(1.19257)=0.59628$ ✓✓" "\n"
        r"⑧ **排除其他**：A $=\\frac{\\sqrt3}2=0.866$、B $=\\frac13=0.333$、C $=\\frac23=0.667$ ✗" "\n"
        r"**答案 D（$\\frac{\\sqrt5}3$）正确** ✓" "\n"
        r"**⭐ 通法（焦点 + 定长 ⟹ 定位交点）**：" "\n"
        r"① ⭐ **「$\\lvert OQ\\rvert=\\lvert OF\\rvert=c$」⟹ $Q$ 在圆 $x^{2}+y^{2}=c^{2}$ 上**，" "\n"
        r"与过焦点的直线联立即可定出 $Q$ 的坐标（**一个二次方程，两根之一是焦点本身，必舍**）；" "\n"
        r"② ⭐ **斜率 $\\frac12$  ⟹ $Q$ 落在 $(0.6c,0.8c)$**，即 $3$-$4$-$5$ 直角三角形 —— " "\n"
        r"看到斜率 $\\frac12$、$\\frac34$ 这类，可以预判会出现整数勾股比；" "\n"
        r"③ 得到 $Q$ 后**代入椭圆方程**并除以 $a^{2}$，把 $b^{2}$ 换成 $a^{2}(1-e^{2})$，得到只含 $e$ 的方程；" "\n"
        r"④ ⚠ 解出 $e^{2}$ 的**两个根要都检查**：本题 $e^{2}=5$ 因 $e<1$ 舍去，别只取一个就完事。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-365'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-365-V3',
}

T366_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知双曲线 $\dfrac{x^{2}}{a^{2}}-\dfrac{y^{2}}{b^{2}}=1\ (a>0,b>0)$ 的左、右焦点分别为 $F_1,F_2$，"
        r"点 $A$ 是双曲线渐近线上一点，且 $AF_1\perp AO$（其中 $O$ 为坐标原点），"
        r"$AF_1$ 交双曲线于点 $B$，且 $\overrightarrow{AB}=\overrightarrow{BF_1}$，则双曲线的离心率为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac{\sqrt{26}}4$"),
        ('B', r"$\dfrac{\sqrt{34}}4$"),
        ('C', r"$\sqrt2$"),
        ('D', r"$\sqrt3$"),
    ],
    'answer': 'C',
    'analysis': (
        r"$AF_1\perp AO$ ⟹ $A$ 在以 $OF_1$ 为直径的圆上，与渐近线联立得 $A\left(-\frac{a^{2}}c,\frac{ab}c\right)$。"
        r"$\overrightarrow{AB}=\overrightarrow{BF_1}$ 表示 $B$ 是 $AF_1$ 的中点，代入双曲线方程得 $c^{2}=2a^{2}$。"
    ),
    'solution': (
        r"**第一步：翻译垂直条件**" "\n"
        r"$\angle OAF_1=90^\circ$ ⟹ $A$ 在以 $OF_1$ 为直径的圆上。" "\n"
        r"$O(0,0)$、$F_1(-c,0)$，该圆：$\left(x+\dfrac c2\right)^{2}+y^{2}=\dfrac{c^{2}}4\Rightarrow x^{2}+cx+y^{2}=0$．" "\n"
        r"**第二步：与渐近线联立**" "\n"
        r"设 $A$ 在 $y=-\dfrac ba x$ 上，代入圆：$x^{2}+cx+\dfrac{b^{2}}{a^{2}}x^{2}=0\Rightarrow x^{2}\dfrac{c^{2}}{a^{2}}+cx=0$" "\n"
        r"$\Rightarrow x\left(\dfrac{c^{2}}{a^{2}}x+c\right)=0\Rightarrow x=0$（原点，舍）或 $x=-\dfrac{a^{2}}c$．" "\n"
        r"取 $A\left(-\dfrac{a^{2}}c,\dfrac{ab}c\right)$（在第二象限）．" "\n"
        r"**第三步：$B$ 是 $AF_1$ 的中点**" "\n"
        r"$\overrightarrow{AB}=\overrightarrow{BF_1}$ ⟹ $B=\dfrac{A+F_1}2=\left(\dfrac{-\frac{a^{2}}c-c}2,\dfrac{\frac{ab}c}2\right) =\left(-\dfrac{a^{2}+c^{2}}{2c},\dfrac{ab}{2c}\right)$．" "\n"
        r"**第四步：$B$ 在双曲线上**" "\n"
        r"$\dfrac{(a^{2}+c^{2})^{2}}{4c^{2}a^{2}}-\dfrac{a^{2}b^{2}}{4c^{2}b^{2}}=1$" "\n"
        r"$\Rightarrow\dfrac{(a^{2}+c^{2})^{2}}{4c^{2}a^{2}}-\dfrac{a^{2}}{4c^{2}}=1$" "\n"
        r"乘 $4c^{2}a^{2}$：$(a^{2}+c^{2})^{2}-a^{4}=4a^{2}c^{2}$" "\n"
        r"$a^{4}+2a^{2}c^{2}+c^{4}-a^{4}=4a^{2}c^{2}\Rightarrow c^{4}=2a^{2}c^{2}\Rightarrow c^{2}=2a^{2}$．" "\n"
        r"$e^{2}=2\Rightarrow e=\sqrt2$．选 C．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**详解未提取**，上述推导为我独立完成）。" "\n"
        r"**⚠ 选项还原**：原文提取为 `264 344 2 3`（根号丢失），按 A $\\frac{\\sqrt{26}}4$、B $\\frac{\\sqrt{34}}4$、C $\\sqrt2$、D $\\sqrt3$ 还原。" "\n"
        r"**判定依据**：我的推导给出 $e=\\sqrt2$ 且答案为 C。" "\n"
        r"（注：M-T-373-V3 的选项提取完全相同，两题可能同源或为同题的不同录入）" "\n"
        r"**独立验算**：" "\n"
        r"① ⭐ **垂直 ⟹ 直径圆**：$\\angle OAF_1=90^\\circ$ ⟹ $A$ 在以 $OF_1$ 为直径的圆上 ✓✓" "\n"
        r"圆心 $(-\\frac c2,0)$、半径 $\\frac c2$：$(x+\\frac c2)^2+y^2=\\frac{c^2}{4}\\Rightarrowx^2+cx+y^2=0$ ✓✓✓" "\n"
        r"② **联立**：$y=-\\frac ba x$ ⟹ $y^2=\\frac{b^2}{a^2}x^2$" "\n"
        r"$x^2+cx+\\frac{b^2}{a^2}x^2=x^2(1+\\frac{b^2}{a^2})+cx=x^2\\frac{c^2}{a^2}+cx=0$ ✓✓" "\n"
        r"$x(\\frac{c^2}{a^2}x+c)=0\\Rightarrowx=-\\frac{a^2}{c}$ ✓✓✓" "\n"
        r"$y=-\\frac ba(-\\frac{a^2}{c})=\\frac{ab}{c}$ ✓✓" "\n"
        r"③ **$B$ 是中点**：$\\vec{AB}=\\vec{BF_1}\\RightarrowB-A=F_1-B\\Rightarrow2B=A+F_1$ ✓✓✓" "\n"
        r"$B=(\\frac{-a^2/c-c}{2},\\frac{ab/c}{2})=(\\frac{-(a^2+c^2)}{2c},\\frac{ab}{2c})$ ✓✓" "\n"
        r"④ **代入双曲线**：$\\frac{(a^2+c^2)^2}{4c^2a^2}-\\frac{(ab/2c)^2}{b^2}=\\frac{(a^2+c^2)^2}{4c^2a^2}-\\frac{a^2}{4c^2}$ ✓✓" "\n"
        r"通分 $\\frac{(a^2+c^2)^2-a^4}{4c^2a^2}=1\\Rightarrow(a^2+c^2)^2-a^4=4a^2c^2$ ✓✓✓" "\n"
        r"$a^4+2a^2c^2+c^4-a^4=4a^2c^2\\Rightarrowc^4=2a^2c^2\\Rightarrowc^2=2a^2$ ✓✓✓" "\n"
        r"⑤ **$e=\\sqrt2=1.41421$** ✓✓✓ **恰为选项 C**" "\n"
        r"⑥ **数值构造检验**：取 $a=1$ 则 $c=\\sqrt2=1.41421$，$b^2=c^2-a^2=1$，$b=1$" "\n"
        r"$A=(-\\frac{1}{1.41421},\\frac{1}{1.41421})=(-0.70711,0.70711)$" "\n"
        r"验 $A$ 在渐近线 $y=-x$ 上：$0.70711=-(-0.70711)$ ✓✓" "\n"
        r"验 $AF_1\\perpAO$：$\\vec{AO}=(0.70711,-0.70711)$、$\\vec{AF_1}=(-1.41421+0.70711,0-0.70711)=(-0.70711,-0.70711)$" "\n"
        r"点积 $=0.70711(-0.70711)+(-0.70711)(-0.70711)=-0.5+0.5=0$ ✓✓✓ **确为垂直**" "\n"
        r"$B=\\frac{A+F_1}{2}=(\\frac{-0.70711-1.41421}{2},\\frac{0.70711}{2})=(-1.06066,0.35355)$" "\n"
        r"验 $B$ 在双曲线 $x^2-y^2=1$ 上：$1.12500-0.12500=1.0$ ✓✓✓ **完全成立**" "\n"
        r"⑦ **排除其他**：A $=\\frac{\\sqrt{26}}4=1.2748$、B $=\\frac{\\sqrt{34}}4=1.4577$、D $=\\sqrt3=1.732$ ✗" "\n"
        r"**答案 C（$\\sqrt2$）正确** ✓" "\n"
        r"**⭐ 通法（垂直 ⟹ 直径圆）**：" "\n"
        r"① ⭐⭐ **「$PX\\perpPY$」⟹ $P$ 在以 $XY$ 为直径的圆上** —— 本题 $AF_1\\perpAO$ 给出以 $OF_1$ 为直径的圆，" "\n"
        r"圆方程 $x^{2}+cx+y^{2}=0$ 与渐近线联立，$x=0$ 这个根必舍（那是原点）；" "\n"
        r"② ⭐ **$\\overrightarrow{AB}=\\overrightarrow{BF_1}$ ⟺ $B$ 是 $AF_1$ 的中点** —— 见到向量等式先翻译成位置关系，" "\n"
        r"（与 M-T-376-V3 的 $\\overrightarrow{FA}=\\overrightarrow{AC}$ 完全同型）；" "\n"
        r"③ 得到 $B$ 的坐标后代入曲线方程，注意 $\\frac{y_B^{2}}{b^{2}}=\\frac{a^{2}}{4c^{2}}$ 中 **$b^{2}$ 会约掉**，大幅化简；" "\n"
        r"④ ⚠ 本题 $A$ 选在第二象限还是第三象限不影响 $e$（对称），但 $B$ 的 $y$ 坐标符号要与之对应。"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-366'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-366-E1',
}

T366_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知双曲线 $C:\dfrac{x^{2}}{a^{2}}-\dfrac{y^{2}}{b^{2}}=1\ (a>0,b>0)$ 的左、右焦点分别为 $F_1,F_2$，"
        r"点 $A$ 在 $C$ 的右支上，$AF_1$ 与 $C$ 交于点 $B$，"
        r"若 $\overrightarrow{F_2A}\cdot\overrightarrow{F_2B}=0$，且 $\lvert F_2A\rvert=\lvert F_2B\rvert$，则 $C$ 的离心率为（　　）"
    ),
    'opts': [
        ('A', r"$\sqrt2$"),
        ('B', r"$\sqrt3$"),
        ('C', r"$\sqrt6$"),
        ('D', r"$\sqrt7$"),
    ],
    'answer': 'B',
    'analysis': (
        r"两个条件合起来 ⟹ $\triangle F_2AB$ 是等腰直角三角形（直角在 $F_2$）。设腰长 $d$，"
        r"则 $\lvert AB\rvert=d\sqrt2$；又 $A,B$ 分居两支且都在 $F_1$ 同侧，用定义得 $\lvert AB\rvert=4a$ ⟹ $d=2\sqrt2a$。"
        r"再用 $F_2$ 到 $AB$ 的距离 $=\frac d{\sqrt2}=2a$ 定出 $\sin\beta=\frac ae$，配合余弦定理解得 $e=\sqrt3$。"
    ),
    'solution': (
        r"**第一步：识别等腰直角三角形**" "\n"
        r"$\overrightarrow{F_2A}\cdot\overrightarrow{F_2B}=0\Rightarrow F_2A\perp F_2B$；又 $\lvert F_2A\rvert=\lvert F_2B\rvert=d$。" "\n"
        r"故 $\triangle F_2AB$ 是等腰直角三角形，$\lvert AB\rvert=d\sqrt2$，斜边上的高 $=\dfrac d{\sqrt2}$．" "\n"
        r"**第二步：用定义求 $d$**" "\n"
        r"$A$ 在右支 $B$ 在左支（因 $AF_1$ 过左焦点后交左支），且二者在 $F_1$ 同侧（$F_1$ 在左支左侧）：" "\n"
        r"$\lvert AF_1\rvert-\lvert AF_2\rvert=2a\Rightarrow\lvert AF_1\rvert=d+2a$；" "\n"
        r"$\lvert BF_2\rvert-\lvert BF_1\rvert=2a\Rightarrow\lvert BF_1\rvert=d-2a$．" "\n"
        r"同侧 ⟹ $\lvert AB\rvert=\lvert AF_1\rvert-\lvert BF_1\rvert=4a=d\sqrt2\Rightarrow d=2\sqrt2a$．" "\n"
        r"**第三步：用「$F_2$ 到 $AB$ 的距离」**" "\n"
        r"设直线 $AB$（即 $AF_1$）与 $F_1F_2$ 的夹角为 $\beta$。" "\n"
        r"$F_2$ 到 $AB$ 的距离 $=\lvert F_1F_2\rvert\sin\beta=2c\sin\beta$；又它等于斜边上的高 $\dfrac d{\sqrt2}=\dfrac{2\sqrt2a}{\sqrt2}=2a$。" "\n"
        r"故 $2c\sin\beta=2a\Rightarrow\sin\beta=\dfrac ae=\dfrac1e$，$\lvert\cos\beta\rvert=\dfrac{\sqrt{c^{2}-a^{2}}}c=\dfrac bc$．" "\n"
        r"**第四步：余弦定理**" "\n"
        r"在 $\triangle F_1AF_2$ 中，$\angle AF_1F_2=\beta$，$\lvert AF_1\rvert=d+2a$，$\lvert AF_2\rvert=d$：" "\n"
        r"$d^{2}=(d+2a)^{2}+4c^{2}-2(d+2a)\cdot2c\cos\beta$" "\n"
        r"$\Rightarrow0=4ad+4a^{2}+4c^{2}-4c(d+2a)\cos\beta\Rightarrow c(d+2a)\cos\beta=a^{2}+c^{2}+ad$．" "\n"
        r"代入 $d=2\sqrt2a$、$a=1$、$\cos\beta=\dfrac bc=\dfrac{\sqrt{c^{2}-1}}c$、$c=e$：" "\n"
        r"$e(2\sqrt2+2)\cdot\dfrac{\sqrt{e^{2}-1}}e=1+e^{2}+2\sqrt2\Rightarrow(2\sqrt2+2)\sqrt{e^{2}-1}=e^{2}+1+2\sqrt2$．" "\n"
        r"记 $t=e^{2}$，两边除以 $2$：$(\sqrt2+1)\sqrt{t-1}=\dfrac{t+1+2\sqrt2}2$．" "\n"
        r"试 $t=3$：左 $=(\sqrt2+1)\sqrt2=2+\sqrt2=3.4142$；右 $=\dfrac{3+1+2\sqrt2}2=\dfrac{4+2\sqrt2}2=2+\sqrt2=3.4142$ ✓" "\n"
        r"故 $e^{2}=3$，$e=\sqrt3$．选 B．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**详解未提取**，上述推导为我独立完成）。" "\n"
        r"**⚠ 选项还原**：原文提取为 `2 3 6 7`（根号丢失），按 A $\\sqrt2$、B $\\sqrt3$、C $\\sqrt6$、D $\\sqrt7$ 还原。" "\n"
        r"**判定依据**：我的推导给出 $e=\\sqrt3$ 且答案为 B。" "\n"
        r"**独立验算**：" "\n"
        r"① **等腰直角**：$\\vec{F_2A}\\cdot\\vec{F_2B}=0$ ⟹ 垂直 ✓；$\\lvert F_2A\\rvert=\\lvert F_2B\\rvert$ ⟹ 等腰 ✓✓" "\n"
        r"$\\lvert AB\\rvert=\\sqrt{d^2+d^2}=d\\sqrt2$ ✓✓✓" "\n"
        r"② ⭐ **同侧判定**：$A$ 右支、$B$ 左支，$F_1(-c,0)$ 且 $-c<-a$（$c>a$）⟹ $F_1$ 在左支左侧" "\n"
        r"⟹ $A,B$ 都在 $F_1$ 的同一侧 ⟹ $\\lvert AB\\rvert=\\lvert AF_1\\rvert-\\lvert BF_1\\rvert$（**差**）✓✓✓" "\n"
        r"（**我第一遍按「和」算得 $\\lvert AB\\rvert=2d=d\\sqrt2$ 无解**，正是这条提示改成差）" "\n"
        r"③ **$d=2\\sqrt2a$**：$\\lvert AB\\rvert=(d+2a)-(d-2a)=4a=d\\sqrt2$ ⟹ $d=\\frac{4a}{\\sqrt2}=2\\sqrt2a$ ✓✓✓" "\n"
        r"④ **距离**：斜边上的高 $=\\frac{d}{\\sqrt2}=\\frac{2\\sqrt2a}{\\sqrt2}=2a$ ✓✓" "\n"
        r"$F_2$ 到直线 $AB$ 的距离 $=\\lvert F_1F_2\\rvert\\sin\\beta=2c\\sin\\beta$ ✓✓ ⟹ $2c\\sin\\beta=2a$ ⟹ $\\sin\\beta=\\frac1e$ ✓✓✓" "\n"
        r"⑤ **余弦定理式**：$\\lvert AF_2\\rvert^2=\\lvert AF_1\\rvert^2+\\lvert F_1F_2\\rvert^2-2\\lvert AF_1\\rvert\\lvert F_1F_2\\rvert\\cos\\beta$" "\n"
        r"$d^2=(d+2a)^2+4c^2-2(d+2a)(2c)\\cos\\beta$" "\n"
        r"$0=4ad+4a^2+4c^2-4c(d+2a)\\cos\\beta$ ✓✓ 整理 $c(d+2a)\\cos\\beta=a^2+c^2+ad$ ✓✓✓" "\n"
        r"⑥ **代入 $t=3$ 验证**：$(\\sqrt2+1)\\sqrt{3-1}=(\\sqrt2+1)\\sqrt2=2+\\sqrt2=3.41421$" "\n"
        r"$\\frac{3+1+2\\sqrt2}{2}=\\frac{4+2.82843}{2}=3.41421$ ✓✓✓ **两边相等**" "\n"
        r"$e=\\sqrt3=1.73205$ ✓✓✓ **恰为选项 B**" "\n"
        r"⑦ **$\\sin\\beta=\\frac1e$ 的合理性**：$e=\\sqrt3$ ⟹ $\\sin\\beta=\\frac1{\\sqrt3}=0.57735$，$\\beta=35.26^\\circ$ ✓ 锐角合理 ✓" "\n"
        r"⑧ **排除其他**：A $=\\sqrt2=1.414$、C $=\\sqrt6=2.449$、D $=\\sqrt7=2.646$ ✗" "\n"
        r"**答案 B（$\\sqrt3$）正确** ✓" "\n"
        r"**⭐⭐ 通法（等腰直角的三个等价用法）**：" "\n"
        r"① ⭐⭐ **$\\vec{u}\\cdot\\vec{v}=0$ 且 $\\lvert\\vec u\\rvert=\\lvert\\vec v\\rvert$ ⟹ 等腰直角三角形** —— " "\n"
        r"立刻可用三件事：斜边 $=\\sqrt2 d$、**斜边上的高 $=\\frac d{\\sqrt2}$**、两锐角 $45^\\circ$；" "\n"
        r"② ⭐ **「斜边上的高」=「焦点到弦所在直线的距离」**：$2c\\sin\\beta=\\frac d{\\sqrt2}$，" "\n"
        r"这一步把**角度 $\\beta$ 与 $e$ 直接挂钩**（$\\sin\\beta=\\frac ae$），是解题的枢纽；" "\n"
        r"③ ⚠ **两支 + 过焦点直线 ⟹ 用「差」不用「和」**（左焦点在左支左侧，右焦点在右支右侧），" "\n"
        r"算出 $2d=d\\sqrt2$ 这类恒不成立时，第一反应就是改「差」；" "\n"
        r"④ 最后解无理方程时，**代入选项试值**比平方求解快，且能顺便验算。"
    ),
    'difficulty': 0.95,
    'topics': ['M-T-366'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-366-V1',
}

T366_V3 = {
    'type': '选择',
    'stem_text': (
        r"设双曲线 $C:\dfrac{x^{2}}{a^{2}}-\dfrac{y^{2}}{b^{2}}=1\ (a>b>0)$ 的左、右焦点分别为 $F_1,F_2$，"
        r"过 $F_1$ 的直线 $l$ 与双曲线左、右两支交于 $M,N$ 两点，以 $MN$ 为直径的圆过 $F_2$，"
        r"且 $\lvert MN\rvert^{2}=2\overrightarrow{MF_2}\cdot\overrightarrow{MN}$，则双曲线 $C$ 的离心率为（　　）"
    ),
    'opts': [
        ('A', r"$\sqrt2$"),
        ('B', r"$\sqrt3$"),
        ('C', r"$2$"),
        ('D', r"$\sqrt5$"),
    ],
    'answer': 'B',
    'analysis': (
        r"以 $MN$ 为直径的圆过 $F_2$ ⟹ $\angle MF_2N=90^\circ$。又 $\lvert MN\rvert^{2}=2\vec{MF_2}\cdot\vec{MN}=2\lvert MF_2\rvert^{2}$"
        r"（因 $\vec{MF_2}\perp\vec{NF_2}$），配合勾股得 $\lvert NF_2\rvert=\lvert MF_2\rvert$ ⟹ 等腰直角。此后的结构与 M-T-366-V1 完全相同 ⟹ $e=\sqrt3$。"
    ),
    'solution': (
        r"**第一步：翻译「直径圆过 $F_2$」**" "\n"
        r"以 $MN$ 为直径的圆过 $F_2$ ⟹ $\angle MF_2N=90^\circ$，即 $MF_2\perp NF_2$。" "\n"
        r"**第二步：翻译向量条件**" "\n"
        r"$\overrightarrow{MN}=\overrightarrow{MF_2}-\overrightarrow{NF_2}$，故" "\n"
        r"$\overrightarrow{MF_2}\cdot\overrightarrow{MN}=\overrightarrow{MF_2}\cdot\left(\overrightarrow{MF_2}-\overrightarrow{NF_2}\right) =\lvert MF_2\rvert^{2}-0=\lvert MF_2\rvert^{2}$．" "\n"
        r"由 $\lvert MN\rvert^{2}=2\overrightarrow{MF_2}\cdot\overrightarrow{MN}$ 得 $\lvert MN\rvert^{2}=2\lvert MF_2\rvert^{2}$。" "\n"
        r"又勾股：$\lvert MN\rvert^{2}=\lvert MF_2\rvert^{2}+\lvert NF_2\rvert^{2}$，" "\n"
        r"两式比较得 $\lvert NF_2\rvert^{2}=\lvert MF_2\rvert^{2}$，即 $\lvert NF_2\rvert=\lvert MF_2\rvert=d$。" "\n"
        r"于是 $\triangle MF_2N$ 为**等腰直角三角形**，$\lvert MN\rvert=d\sqrt2$，斜边上的高 $=\dfrac d{\sqrt2}$．" "\n"
        r"**第三步：用定义（$M$ 左支、$N$ 右支，同在 $F_1$ 右侧）**" "\n"
        r"$\lvert MF_2\rvert-\lvert MF_1\rvert=2a\Rightarrow\lvert MF_1\rvert=d-2a$；" "\n"
        r"$\lvert NF_1\rvert-\lvert NF_2\rvert=2a\Rightarrow\lvert NF_1\rvert=d+2a$．" "\n"
        r"$\lvert MN\rvert=\lvert NF_1\rvert-\lvert MF_1\rvert=4a=d\sqrt2\Rightarrow d=2\sqrt2a$．" "\n"
        r"**第四步：与 M-T-366-V1 完全同构**" "\n"
        r"此后与 V1 第三步起完全相同：由 $2c\sin\beta=\dfrac d{\sqrt2}=2a$ 得 $\sin\beta=\dfrac1e$、$\cos\beta=\dfrac bc$，" "\n"
        r"代入 $\triangle F_1NF_2$ 的余弦定理 $\lvert NF_2\rvert^{2}=\lvert NF_1\rvert^{2}+4c^{2}-2\lvert NF_1\rvert\cdot2c\cos\beta$：" "\n"
        r"$c(d+2a)\cos\beta=a^{2}+c^{2}+ad$，代入 $d=2\sqrt2a$、$a=1$ 得 $(\sqrt2+1)\sqrt{e^{2}-1}=\dfrac{e^{2}+1+2\sqrt2}2$，" "\n"
        r"解得 $e^{2}=3$，即 $e=\sqrt3$．选 B．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**详解未提取**，上述推导为我独立完成）。" "\n"
        r"**⚠ 选项还原**：原文提取为 `2 3 2 5`（根号丢失），按 A $\\sqrt2$、B $\\sqrt3$、C $2$、D $\\sqrt5$ 还原。" "\n"
        r"**判定依据**：我的推导给出 $e=\\sqrt3$ 且答案为 B。" "\n"
        r"**独立验算**：" "\n"
        r"① **直径圆**：以 $MN$ 为直径的圆过 $F_2$ ⟹ $\\angle MF_2N=90^\\circ$ ✓✓✓（直径所对圆周角）" "\n"
        r"② ⭐ **$\\vec{MF_2}\\cdot\\vec{MN}$**：$\\vec{MN}=\\vec{MF_2}-\\vec{NF_2}$" "\n"
        r"$\\vec{MF_2}\\cdot(\\vec{MF_2}-\\vec{NF_2})=\\lvert MF_2\\rvert^2-\\underbrace{\\vec{MF_2}\\cdot\\vec{NF_2}}_{=0}=\\lvert MF_2\\rvert^2$ ✓✓✓" "\n"
        r"③ **等腰**：$\\lvert MN\\rvert^2=2\\lvert MF_2\\rvert^2$ 与 $\\lvert MN\\rvert^2=\\lvert MF_2\\rvert^2+\\lvert NF_2\\rvert^2$" "\n"
        r"⟹ $\\lvert NF_2\\rvert^2=\\lvert MF_2\\rvert^2$ ✓✓✓ **确为等腰直角**" "\n"
        r"④ **$d=2\\sqrt2a$**：$\\lvert MN\\rvert=(d+2a)-(d-2a)=4a=d\\sqrt2$ ⟹ $d=2\\sqrt2a$ ✓✓✓" "\n"
        r"（**同侧用差**：$M$ 左支、$N$ 右支，$F_1$ 在左支左侧，两点都在 $F_1$ 右侧 ✓）" "\n"
        r"⑤ **与 V1 同构性核对**：" "\n"
        r"V1：$A$ 右支（远，$d+2a$）、$B$ 左支（近，$d-2a$）、等腰直角、$d=2\\sqrt2a$" "\n"
        r"V3：$N$ 右支（远，$d+2a$）、$M$ 左支（近，$d-2a$）、等腰直角、$d=2\\sqrt2a$" "\n"
        r"**结构逐项对应** ⟹ $e$ 必相同 $=\\sqrt3$ ✓✓✓" "\n"
        r"⑥ **代入验证**：$(\\sqrt2+1)\\sqrt{3-1}=2+\\sqrt2=3.41421$；$\\frac{3+1+2\\sqrt2}{2}=2+\\sqrt2=3.41421$ ✓✓✓" "\n"
        r"⑦ **排除其他**：A $=\\sqrt2=1.414$、C $=2$、D $=\\sqrt5=2.236$ ✗" "\n"
        r"**答案 B（$\\sqrt3$）正确** ✓" "\n"
        r"**⭐⭐ 通法（识别同构，一鱼两吃）**：" "\n"
        r"① ⭐⭐ **「以 $XY$ 为直径的圆过 $Z$」⟹ $\\angle XZY=90^\\circ$** —— 见到这句话立刻写垂直；" "\n"
        r"② ⭐ **$\\lvert MN\\rvert^{2}=2\\vec{MF_2}\\cdot\\vec{MN}$ 这类式子，先用 $\\vec{MN}=\\vec{MF_2}-\\vec{NF_2}$ 拆开**，" "\n"
        r"垂直项归零后立刻看出是「斜边 $^{2}=2\\times$ 直角边 $^{2}$」⟹ 等腰直角；" "\n"
        r"③ ⭐⭐ **做完一题要回头看它和哪题同构** —— 本题与 M-T-366-V1 的「等腰直角 + 两支同侧差 $4a$ + " "\n"
        r"$2c\\sin\\beta=\\frac d{\\sqrt2}$」结构完全一致，**识别出同构后可以直接写答案，省掉全部推导**；" "\n"
        r"④ ⚠ 同构≠同题：两题给的**条件形式**不同（一个给向量点积+等长，一个给直径圆+向量式），" "\n"
        r"但化到「等腰直角」这一步后完全一样 —— **找这个『汇合点』是提速的关键**。"
    ),
    'difficulty': 0.95,
    'topics': ['M-T-366'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-366-V3',
}

QS = [T365_V1, T365_V2, T365_V3, T366_E1, T366_V1, T366_V3]
