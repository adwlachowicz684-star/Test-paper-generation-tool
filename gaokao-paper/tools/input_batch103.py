# -*- coding: utf-8 -*-
r"""第 103 批：导数双变量与圆锥曲线定点定值（12 题）

    python3 tools/run_batch.py 103

## 选题依据

按「详解完整 + 同题型聚堆 + 无图依赖」筛出导数区与解析几何区各 6 题：

| 题型 | 题号 | 核心方法 |
|---|---|---|
| M-T-163 | E1, V1, V2 | 双变量代换（$t=\frac1x$、$t=\frac{x_2}{x_1}$）；对称化构造；绝对值分段 |
| M-T-165 | E1, V1, V2 | 极值点偏移的「和差消参」；判别式定号；换元 $x=\ln t$ |
| M-T-347 | V1, V2, V3 | 斜率和/积为定值 ⟹ 直线过定点 |
| M-T-355 | V1, V2, V3 | 焦点弦向量关系；定点 $N$ 的横坐标；向量共线求 $\lambda$ 范围 |

## 本批最重要的六条通法

### 一、双变量问题的「加减消参」三板斧

$f\left(x_1\right)=f\left(x_2\right)$ 型（两个等式）：

1. **相加** ⟹ 得到含 $x_1+x_2$ 与 $x_1x_2$（或 $\ln x_1+\ln x_2$）的式子
2. **相减** ⟹ 得到 $\dfrac{\ln x_2-\ln x_1}{x_2-x_1}$ 型的**对数平均**
3. **相除** ⟹ 消去参数 $a$，只剩 $t=\dfrac{x_2}{x_1}$

M-T-163-V1(3)、M-T-165-E1(2)、M-T-165-V2(2) 全靠这一套。

### 二、对数平均不等式 $\ln t>\dfrac{2\left(t-1\right)}{t+1}$（$t>1$）

令 $h\left(t\right)=\ln t-\dfrac{2\left(t-1\right)}{t+1}$，则

$$h'\left(t\right)=\frac{\left(t-1\right)^2}{t\left(t+1\right)^2}>0$$

**分子是完全平方** —— 这是「对数 vs 帕德分式」的固定结果。
M-T-163-V1(3)、M-T-165-E1(2) 都用它收尾。

### 三、极值点偏移的对称化构造

要证 $t_1+t_2>\dfrac2e$，构造 $\varphi\left(x\right)=h\left(x\right)-h\left(\dfrac2e-x\right)$，
证 $\varphi$ 在 $\left(0,\dfrac1e\right)$ 上**递增**且 $\varphi\left(\dfrac1e\right)=0$。

> ⭐ 关键：证 $\varphi'>0$ 时用「分母大的项缩小」+ AM-GM 夹住 $x\left(\frac2e-x\right)\le\frac1{e^2}$。

### 四、斜率和为定值 ⟹ 直线过定点（M-T-347 全组）

统一算法：设 $l:y=kx+t$，联立后把 $\dfrac{y_1-c}{x_1}+\dfrac{y_2-c}{x_2}$ 全用韦达表示，
整理成 $k,t$ 的**一次关系** $t=\alpha k+\beta$，则 $l:y=k\left(x+\alpha\right)+\beta$ 恒过 $\left(-\alpha,\beta\right)$。

- V1：$t=-2k-1$ ⟹ 定点 $\left(2,-1\right)$
- V3：$t=\dfrac{\sqrt2}2$（与 $k$ 无关）⟹ 定点 $\left(0,\dfrac{\sqrt2}2\right)$

### 五、斜率为负倒数（$AM\perp AN$）⟹ 关于 $m,k$ 的二次齐次式

M-T-347-V2 中 $\overrightarrow{AM}\cdot\overrightarrow{AN}=0$ 化出
$m^2+3\sqrt3km+6k^2=0$ ⟹ $m=-\sqrt3k$（过 $A$，舍）或 $m=-2\sqrt3k$ ⟹ 定点 $\left(2\sqrt3,0\right)$。

> ⭐ **两根中必有一根对应「过已知点」，必须舍** —— 这是定点题的固定陷阱。

### 六、$\overrightarrow{DE}=\lambda\overrightarrow{DF}$ 型求范围（M-T-355-V3）

用 $\lambda$ 表示 $F$ 的横坐标 $x_1$，再由 $x_1\in\left(-\sqrt2,\sqrt2\right)$ 反解 $\lambda$。

> ⚠ 别忘了 $x\ne0$ 的定义域限制 ⟹ $\lambda\ne\dfrac13$。

## 三处还原（判据都是「算出来矛盾」）

| 题 | 原书存的 | 实际 | 判据 |
|---|---|---|---|
| M-T-165-E1 | $f\left(x\right)=x\log_ax-2+\dfrac1{\ln a}x$ | $-\left(2+\dfrac1{\ln a}\right)x$ | 只有这样才能得 $f'\left(x\right)=\log_ax-2$ |
| M-T-163-V2 | $f\left(x\right)=2a-x+\dfrac1x$（$x<a$ 段） | $2a-x-\dfrac1x$ | 按 $+$ 号导数恒负，与「在 $\left(0,1\right)$ 递增」矛盾 |
| M-T-355-V2 | 「使 $A,B,N$ 三点共线」 | $B,C,N$ 三点共线 | $A,B,N$ 共线则 $N=F$，面积比退化 |

## 一处原书小瑕疵

**M-T-163-V2** 详解写「当 $x>-1$ 时，$f\left(x\right)$ 在 $\left(-1,+\infty\right)$ 时**递增**」，
应为**递减**（$f'\left(x\right)=-\left(x+1\right)e^{-x}$）。
"""

# ============================================================
# M-T-163-E1
# ============================================================
T163_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f\left(x\right)=\dfrac mx+\dfrac12\ln x-1$（$m\in\mathbf R$）的两个零点为 $x_1,x_2$（$x_1<x_2$）．" "\n"
        r"（1）求实数 $m$ 的取值范围；" "\n"
        r"（2）求证：$\dfrac1{x_1}+\dfrac1{x_2}>\dfrac2e$．"
    ),
    'opts': [],
    'answer': r"（1）$0<m<\dfrac e2$；（2）证明见解析",
    'analysis': (
        r"（1）求导 $f'\left(x\right)=\dfrac{x-2m}{2x^2}$，分 $m\le0$ 与 $m>0$ 讨论；" "\n"
        r"$m>0$ 时最小值在 $x=2m$ 处，令 $f\left(2m\right)<0$ 即得范围．" "\n"
        r"（2）倒数换元 $t=\dfrac1x$，把两个零点变成 $h\left(t\right)=\dfrac{\ln t+2}{2t}$ 与水平线的两个交点，" "\n"
        r"　 则问题化为「$h$ 的极值点偏移」，用对称化构造 $\varphi\left(x\right)=h\left(x\right)-h\left(\dfrac2e-x\right)$ 完成．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"$f\left(x\right)$ 的定义域为 $\left(0,+\infty\right)$，" "\n"
        r"$f'\left(x\right)=-\dfrac m{x^2}+\dfrac1{2x}=\dfrac{x-2m}{2x^2}$．" "\n"
        r"当 $m\le0$ 时，$x-2m>0$ 恒成立，故 $f'\left(x\right)>0$，$f\left(x\right)$ 在 $\left(0,+\infty\right)$ 上单调递增，" "\n"
        r"至多一个零点，不合题意．" "\n"
        r"当 $m>0$ 时：由 $f'\left(x\right)<0$ 得 $0<x<2m$，由 $f'\left(x\right)>0$ 得 $x>2m$，" "\n"
        r"故 $f\left(x\right)$ 在 $\left(0,2m\right)$ 上递减、在 $\left(2m,+\infty\right)$ 上递增，最小值在 $x=2m$ 处．" "\n"
        r"有两个零点等价于 $f\left(2m\right)<0$，即" "\n"
        r"$\dfrac m{2m}+\dfrac12\ln\left(2m\right)-1=\dfrac12+\dfrac12\ln\left(2m\right)-1<0$，" "\n"
        r"得 $\ln\left(2m\right)<1$，即 $0<m<\dfrac e2$．" "\n"
        r"**第（2）问**" "\n"
        r"令 $t=\dfrac1x$，由 $\ln x=-\ln t$ 得" "\n"
        r"$f\left(x\right)=mt-\dfrac12\ln t-1$，" "\n"
        r"于是 $f\left(x\right)=0$ 等价于 $m=\dfrac{\ln t+2}{2t}$．设 $h\left(t\right)=\dfrac{\ln t+2}{2t}$（$t>0$），" "\n"
        r"$h'\left(t\right)=\dfrac{-\left(\ln t+1\right)}{2t^2}$，" "\n"
        r"故 $h$ 在 $\left(0,\dfrac1e\right)$ 上递增、在 $\left(\dfrac1e,+\infty\right)$ 上递减，$h_{\max}=h\left(\dfrac1e\right)=\dfrac e2$．" "\n"
        r"记 $t_1=\dfrac1{x_1}$，$t_2=\dfrac1{x_2}$．由 $x_1<x_2$ 知 $t_1>t_2$，又 $f\left(e\right)=\dfrac me-\dfrac12<0$（因 $m<\dfrac e2$），" "\n"
        r"而 $f<0$ 只在 $\left(x_1,x_2\right)$ 内成立，故 $x_1<e<x_2$，即 $t_1>\dfrac1e>t_2>0$．" "\n"
        r"要证 $t_1+t_2>\dfrac2e$，即证 $t_1>\dfrac2e-t_2$（注意 $\dfrac2e-t_2>\dfrac1e$）．" "\n"
        r"因 $t_1$ 与 $\dfrac2e-t_2$ 同在 $h$ 的递减区间 $\left(\dfrac1e,+\infty\right)$ 内，只需证 $h\left(t_1\right)<h\left(\dfrac2e-t_2\right)$．" "\n"
        r"又 $h\left(t_1\right)=h\left(t_2\right)=m$，故只需证 $h\left(t_2\right)<h\left(\dfrac2e-t_2\right)$．" "\n"
        r"令 $\varphi\left(x\right)=h\left(x\right)-h\left(\dfrac2e-x\right)$（$0<x<\dfrac1e$），则" "\n"
        r"$\varphi'\left(x\right)=h'\left(x\right)+h'\left(\dfrac2e-x\right)$" "\n"
        r"$=\dfrac{-\left(\ln x+1\right)}{2x^2}+\dfrac{-\left(\ln\left(\frac2e-x\right)+1\right)}{2\left(\frac2e-x\right)^2}$．" "\n"
        r"当 $0<x<\dfrac1e$ 时，$-\left(\ln x+1\right)>0$ 且 $x^2<\left(\dfrac2e-x\right)^2$，故" "\n"
        r"$\varphi'\left(x\right)>\dfrac{-\left(\ln x+1\right)-\left(\ln\left(\frac2e-x\right)+1\right)}{2\left(\frac2e-x\right)^2}$" "\n"
        r"$=\dfrac{-2-\ln\left[x\left(\frac2e-x\right)\right]}{2\left(\frac2e-x\right)^2}$．" "\n"
        r"由 AM-GM，$x\left(\dfrac2e-x\right)\le\left(\dfrac{x+\frac2e-x}{2}\right)^2=\dfrac1{e^2}$，" "\n"
        r"故 $\ln\left[x\left(\dfrac2e-x\right)\right]\le-2$，从而 $\varphi'\left(x\right)>0$．" "\n"
        r"于是 $\varphi$ 在 $\left(0,\dfrac1e\right)$ 上递增，$\varphi\left(x\right)<\varphi\left(\dfrac1e\right)=0$，" "\n"
        r"取 $x=t_2$ 得 $h\left(t_2\right)<h\left(\dfrac2e-t_2\right)$，故 $t_1>\dfrac2e-t_2$，" "\n"
        r"即 $\dfrac1{x_1}+\dfrac1{x_2}>\dfrac2e$．"
    ),
    'review': (
        r"① 第（1）问中 $f\left(2m\right)=\dfrac12+\dfrac12\ln\left(2m\right)-1$ 的化简要注意 $\dfrac m{2m}=\dfrac12$，" "\n"
        r"　 与 $\ln$ 里的 $2m$ **不是同一个结构**，别约错．" "\n"
        r"② 第（2）问的换元 $t=\dfrac1x$ 是本题题眼：$\ln x$ 变成 $-\ln t$，" "\n"
        r"　 于是 $\dfrac1{x_1}+\dfrac1{x_2}>\dfrac2e$ 就变成标准的「两根之和」型极值点偏移．" "\n"
        r"③ 判断 $t_1>\dfrac1e>t_2$ 时，用 $f\left(e\right)=\dfrac me-\dfrac12<0$ 是最快的：" "\n"
        r"　 $f<0$ 只在两零点之间，故 $e\in\left(x_1,x_2\right)$．这一句省掉了繁琐的大小比较．" "\n"
        r"④ $\varphi'\left(x\right)>0$ 的证明用了两次放缩：**先放大分母小的那项**（因 $x^2<\left(\frac2e-x\right)^2$ 且分子为正），" "\n"
        r"　 **再用 AM-GM 夹住 $x\left(\frac2e-x\right)$**．两步缺一不可．" "\n"
        r"⑤ 数值复核：$m=0.3$ 时 $x_1=0.15536$、$x_2=6.76163$，" "\n"
        r"　 $\dfrac1{x_1}+\dfrac1{x_2}=6.58458>\dfrac2e=0.73576$ ✓；" "\n"
        r"　 $m=1.2$ 时 $x_1=1.5139$、$x_2=4.1360$，$\dfrac1{x_1}+\dfrac1{x_2}=0.90233>0.73576$ ✓（贴近界但成立）．" "\n"
        r"**通法（倒数换元 + 极值点偏移）**：当所求式子形如 $\dfrac1{x_1}+\dfrac1{x_2}$ 时，" "\n"
        r"　 令 $t=\dfrac1x$ 把「倒数和」变成「和」，再套对称化构造 $\varphi\left(x\right)=h\left(x\right)-h\left(2t_0-x\right)$．"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-163'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-163-E1',
}

# ============================================================
# M-T-163-V1
# ============================================================
T163_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f\left(x\right)=\ln x$．" "\n"
        r"（1）设函数 $g\left(x\right)=\dfrac tx-\ln x$（$t\in\mathbf R$），且 $g\left(x\right)\le f\left(x\right)$ 恒成立，求实数 $t$ 的取值范围；" "\n"
        r"（2）求证：$f\left(x\right)>\dfrac1{e^x}-\dfrac2{ex}$；" "\n"
        r"（3）设函数 $y=f\left(x\right)-ax-\dfrac1x$（$a\in\mathbf R$）的两个零点为 $x_1,x_2$，求证：$x_1x_2>2e^2$．"
    ),
    'opts': [],
    'answer': r"（1）$t\le-\dfrac2e$；（2）证明见解析；（3）证明见解析",
    'analysis': (
        r"（1）不等式化为 $t\le2x\ln x$，求 $h\left(x\right)=2x\ln x$ 的最小值；" "\n"
        r"（2）同乘 $x$ 化为 $x\ln x>\dfrac x{e^x}-\dfrac2e$，左右分别求最小值与最大值，再比较取等条件；" "\n"
        r"（3）两式相加得含 $\ln\left(x_1x_2\right)$ 的式子，两式相减得对数平均，" "\n"
        r"　 用 $\ln t>\dfrac{2\left(t-1\right)}{t+1}$ 放缩后构造 $\varphi\left(x\right)=\ln x-\dfrac2x$．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"由 $g\left(x\right)\le f\left(x\right)$ 得 $\dfrac tx-\ln x\le\ln x$，因 $x>0$，整理为 $t\le2x\ln x$．" "\n"
        r"令 $h\left(x\right)=2x\ln x$，则 $h'\left(x\right)=2\left(1+\ln x\right)$：" "\n"
        r"$0<x<\dfrac1e$ 时 $h'\left(x\right)<0$，$h$ 递减；$x>\dfrac1e$ 时 $h'\left(x\right)>0$，$h$ 递增．" "\n"
        r"故 $h_{\min}=h\left(\dfrac1e\right)=-\dfrac2e$，所以 $t\le-\dfrac2e$．" "\n"
        r"**第（2）问**" "\n"
        r"因 $x>0$，要证 $\ln x>\dfrac1{e^x}-\dfrac2{ex}$，只需证 $x\ln x>\dfrac x{e^x}-\dfrac2e$．" "\n"
        r"由（1）的推导知 $x\ln x\ge-\dfrac1e$，当且仅当 $x=\dfrac1e$ 取等．" "\n"
        r"令 $m\left(x\right)=\dfrac x{e^x}-\dfrac2e=xe^{-x}-\dfrac2e$，则 $m'\left(x\right)=\left(1-x\right)e^{-x}$：" "\n"
        r"$0<x<1$ 时 $m'\left(x\right)>0$，$x>1$ 时 $m'\left(x\right)<0$，故 $m_{\max}=m\left(1\right)=\dfrac1e-\dfrac2e=-\dfrac1e$．" "\n"
        r"于是 $x\ln x\ge-\dfrac1e\ge m\left(x\right)$．" "\n"
        r"但两个等号的条件分别是 $x=\dfrac1e$ 与 $x=1$，**不能同时取到**，" "\n"
        r"故 $x\ln x>\dfrac x{e^x}-\dfrac2e$，即 $f\left(x\right)>\dfrac1{e^x}-\dfrac2{ex}$．" "\n"
        r"**第（3）问**" "\n"
        r"设 $x_1,x_2$ 是 $\ln x-ax-\dfrac1x=0$ 的两根，即" "\n"
        r"$\ln x_1-\dfrac1{x_1}=ax_1$　①，$\ln x_2-\dfrac1{x_2}=ax_2$　②．" "\n"
        r"①+②：$\ln\left(x_1x_2\right)-\dfrac{x_1+x_2}{x_1x_2}=a\left(x_1+x_2\right)$　③；" "\n"
        r"②-①：$\ln\dfrac{x_2}{x_1}+\dfrac{x_2-x_1}{x_1x_2}=a\left(x_2-x_1\right)$　④．" "\n"
        r"③÷④消去 $a$：" "\n"
        r"$\dfrac{\ln\left(x_1x_2\right)-\frac{x_1+x_2}{x_1x_2}}{\ln\frac{x_2}{x_1}+\frac{x_2-x_1}{x_1x_2}}=\dfrac{x_1+x_2}{x_2-x_1}$．" "\n"
        r"不妨设 $0<x_1<x_2$，令 $t=\dfrac{x_2}{x_1}>1$．由对数平均不等式（见下）" "\n"
        r"$\ln t>\dfrac{2\left(t-1\right)}{t+1}$，得 $\dfrac{x_1+x_2}{x_2-x_1}\ln\dfrac{x_2}{x_1}=\dfrac{t+1}{t-1}\ln t>2$，" "\n"
        r"代入上式可得" "\n"
        r"$\ln\left(x_1x_2\right)-\dfrac{2\left(x_1+x_2\right)}{x_1x_2}>2$．" "\n"
        r"又由 AM-GM，$\dfrac{x_1+x_2}{x_1x_2}>\dfrac{2\sqrt{x_1x_2}}{x_1x_2}=\dfrac2{\sqrt{x_1x_2}}$，" "\n"
        r"而 $\ln\left(x_1x_2\right)-\dfrac{2\left(x_1+x_2\right)}{x_1x_2}$" "\n"
        r"$\quad<\ln\left(x_1x_2\right)-\dfrac4{\sqrt{x_1x_2}}=2\left(\ln\sqrt{x_1x_2}-\dfrac2{\sqrt{x_1x_2}}\right)$，" "\n"
        r"故 $2\left(\ln\sqrt{x_1x_2}-\dfrac2{\sqrt{x_1x_2}}\right)>2$，即 $\ln\sqrt{x_1x_2}-\dfrac2{\sqrt{x_1x_2}}>1$．" "\n"
        r"令 $\varphi\left(x\right)=\ln x-\dfrac2x$，则 $\varphi'\left(x\right)=\dfrac1x+\dfrac2{x^2}>0$，$\varphi$ 在 $\left(0,+\infty\right)$ 上递增．" "\n"
        r"又 $\varphi\left(\sqrt2e\right)=\dfrac12\ln2+1-\dfrac2{\sqrt2e}=\dfrac12\ln2+1-\dfrac{\sqrt2}e\approx0.3466+1-0.5203<1$，" "\n"
        r"所以 $\varphi\left(\sqrt{x_1x_2}\right)>1>\varphi\left(\sqrt2e\right)$，由单调性得 $\sqrt{x_1x_2}>\sqrt2e$，" "\n"
        r"即 $x_1x_2>2e^2$．" "\n"
        r"（对数平均不等式的证明：令 $h\left(t\right)=\ln t-\dfrac{2\left(t-1\right)}{t+1}$（$t>1$），" "\n"
        r"　 则 $h'\left(t\right)=\dfrac1t-\dfrac4{\left(t+1\right)^2}=\dfrac{\left(t-1\right)^2}{t\left(t+1\right)^2}>0$，故 $h\left(t\right)>h\left(1\right)=0$．）"
    ),
    'review': (
        r"① 第（1）问是**分离参数**的标准示范：$t\le2x\ln x$ 恒成立 ⟺ $t\le\left(2x\ln x\right)_{\min}$．" "\n"
        r"　 注意 $x>0$ 才敢同乘 $x$（不变号），这一步不能省．" "\n"
        r"② 第（2）问的精髓是**两个不等式的取等条件不同**：" "\n"
        r"　 $x\ln x\ge-\frac1e$（取等 $x=\frac1e$）与 $m\left(x\right)\le-\frac1e$（取等 $x=1$），" "\n"
        r"　 两个等号冲突 ⟹ 严格不等号成立．这是证明严格不等式的常用手法．" "\n"
        r"③ 第（3）问的「两式相加 / 相减 / 相除」三板斧：" "\n"
        r"　 相加拿到 $\ln\left(x_1x_2\right)$，相减拿到 $\dfrac{\ln x_2-\ln x_1}{x_2-x_1}$（对数平均），相除消掉 $a$．" "\n"
        r"④ 从 $\ln\left(x_1x_2\right)-\dfrac{2\left(x_1+x_2\right)}{x_1x_2}>2$ 到 $\ln\left(x_1x_2\right)-\dfrac4{\sqrt{x_1x_2}}>2$ 用的是" "\n"
        r"　 $x_1+x_2>2\sqrt{x_1x_2}$，**方向是「缩小被减项 ⟹ 整体变大」**，别搞反．" "\n"
        r"⑤ 数值复核：取 $a=0.08$，解 $\ln x-0.08x-\dfrac1x=0$ 得 $x_1=1.9514$、$x_2=48.1764$，" "\n"
        r"　 $x_1x_2=94.01>2e^2=14.78$ ✓；取 $a=0.1$ 得 $x_1x_2=71.13>14.78$ ✓．" "\n"
        r"**通法（对数平均不等式）**：$\ln t>\dfrac{2\left(t-1\right)}{t+1}$（$t>1$），" "\n"
        r"　 等价于 $\dfrac{b-a}{\ln b-\ln a}<\dfrac{a+b}2$（$0<a<b$），是处理「$\ln$ 型双变量」的万能工具．"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-163'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-163-V1',
}

# ============================================================
# M-T-163-V2
# ============================================================
T163_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f\left(x\right)=\lvert x-a\rvert-\dfrac1x+a$，$a\in\mathbf R$．" "\n"
        r"（1）若 $f\left(1\right)=2$，求 $a$ 的值；" "\n"
        r"（2）若存在两个不相等的正实数 $x_1,x_2$，满足 $f\left(x_1\right)=f\left(x_2\right)$，证明：" "\n"
        r"① $2<x_1+x_2<2a$；② $\dfrac{x_2}{x_1}<a^2+1$．"
    ),
    'opts': [],
    'answer': r"（1）$a=2$；（2）证明见解析",
    'analysis': (
        r"（1）代入 $f\left(1\right)=2$ 得 $\lvert1-a\rvert=3-a$，两边平方解出 $a$．" "\n"
        r"（2）先由「存在两解」定出 $a>1$ 且 $f$ 在 $\left(0,1\right)$ 增、$\left(1,a\right)$ 减、$\left(a,+\infty\right)$ 增；" "\n"
        r"　 ① 分「同在 $a$ 左侧」与「分居 $a$ 两侧」两种情况，分别构造 $h\left(x\right)=f\left(x\right)-f\left(2-x\right)$" "\n"
        r"　 与 $g\left(x\right)=f\left(x\right)-f\left(2a-x\right)$；" "\n"
        r"　 ② 同样分两种情况，同侧时由 $f\left(x_1\right)=f\left(x_2\right)$ 直接得 $x_1x_2=1$．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"$f\left(1\right)=\lvert1-a\rvert-1+a=2$，即 $\lvert1-a\rvert=3-a$（需 $3-a\ge0$）．" "\n"
        r"两边平方：$\left(1-a\right)^2=\left(3-a\right)^2$，即 $1-2a+a^2=9-6a+a^2$，" "\n"
        r"得 $4a=8$，$a=2$（满足 $3-a=1\ge0$）．" "\n"
        r"**第（2）问**" "\n"
        r"当 $x\ge a$ 时 $f\left(x\right)=x-\dfrac1x$，在 $\left[a,+\infty\right)$ 上单调递增；" "\n"
        r"当 $x<a$ 时 $f\left(x\right)=2a-x-\dfrac1x$，$f'\left(x\right)=-1+\dfrac1{x^2}$．" "\n"
        r"若 $a\le1$，则 $x<a\le1$ 时 $f'\left(x\right)>0$，$f$ 在 $\left(0,a\right)$ 上递增；" "\n"
        r"结合 $x\ge a$ 段递增且两段在 $x=a$ 处函数值相等，得 $f$ 在 $\left(0,+\infty\right)$ 上递增，无两解，舍．" "\n"
        r"故 $a>1$，此时 $f$ 在 $\left(0,1\right)$ 上递增、在 $\left(1,a\right)$ 上递减、在 $\left(a,+\infty\right)$ 上递增．" "\n"
        r"**① 证 $2<x_1+x_2<2a$**" "\n"
        r"不妨设 $x_1<x_2$．" "\n"
        r"（i）若 $0<x_1<1<x_2<a$：显然 $x_1+x_2<2a$．" "\n"
        r"令 $h\left(x\right)=f\left(x\right)-f\left(2-x\right)$（$0<x<1$），则 $h\left(1\right)=0$，且" "\n"
        r"$h'\left(x\right)=f'\left(x\right)+f'\left(2-x\right)=-2+\dfrac1{x^2}+\dfrac1{\left(2-x\right)^2}$．" "\n"
        r"由 $\dfrac1{x^2}+\dfrac1{\left(2-x\right)^2}>\dfrac2{x\left(2-x\right)}\ge\dfrac2{\left(\frac{x+2-x}{2}\right)^2}=2$，" "\n"
        r"得 $h'\left(x\right)>0$，故 $h$ 在 $\left(0,1\right)$ 上递增，$h\left(x\right)<h\left(1\right)=0$，即 $f\left(x\right)<f\left(2-x\right)$．" "\n"
        r"取 $x=x_1$：$f\left(x_2\right)=f\left(x_1\right)<f\left(2-x_1\right)$．" "\n"
        r"因 $x_2>1$、$2-x_1>1$，且 $f$ 在 $\left(1,+\infty\right)$ 上先减后增——此处 $x_2,2-x_1\in\left(1,a\right)$，" "\n"
        r"而 $f$ 在 $\left(1,a\right)$ 上递减，故 $x_2>2-x_1$，即 $x_1+x_2>2$．" "\n"
        r"（ii）若 $0<1<x_1<a<x_2$：显然 $x_1+x_2>2$．" "\n"
        r"令 $g\left(x\right)=f\left(x\right)-f\left(2a-x\right)$（$1<x<a$），则 $g\left(a\right)=0$，且" "\n"
        r"$g'\left(x\right)=f'\left(x\right)+f'\left(2a-x\right)=\left(-1+\dfrac1{x^2}\right)+\left(1+\dfrac1{\left(2a-x\right)^2}\right)>0$，" "\n"
        r"故 $g$ 在 $\left(1,a\right)$ 上递增，$g\left(x\right)<g\left(a\right)=0$，即 $f\left(x\right)<f\left(2a-x\right)$．" "\n"
        r"取 $x=x_1$：$f\left(x_2\right)=f\left(x_1\right)<f\left(2a-x_1\right)$．" "\n"
        r"因 $x_2>a$、$2a-x_1>a$，而 $f$ 在 $\left(a,+\infty\right)$ 上递增，故 $x_2<2a-x_1$，即 $x_1+x_2<2a$．" "\n"
        r"（iii）若 $0<x_1<1<a<x_2$：由（i）得 $x_1+x_2>2$，由（ii）得 $x_1+x_2<2a$．" "\n"
        r"综上，$2<x_1+x_2<2a$．" "\n"
        r"**② 证 $\dfrac{x_2}{x_1}<a^2+1$**" "\n"
        r"（i）若 $0<x_1<x_2<a$：由 $f\left(x_1\right)=f\left(x_2\right)$ 得" "\n"
        r"$2a-x_1-\dfrac1{x_1}=2a-x_2-\dfrac1{x_2}$，即 $\dfrac{1+x_1^2}{x_1}=\dfrac{1+x_2^2}{x_2}$，" "\n"
        r"整理得 $\dfrac{x_2}{x_1}=\dfrac{1+x_2^2}{1+x_1^2}<\dfrac{1+a^2}{1+x_1^2}<1+a^2$（因 $x_2<a$ 且 $x_1>0$）．" "\n"
        r"（ii）若 $0<x_1<a<x_2$：由 $f\left(x_1\right)=f\left(x_2\right)$ 得" "\n"
        r"$2a-x_1-\dfrac1{x_1}=x_2-\dfrac1{x_2}$，即 $x_1+x_2=2a+\dfrac1{x_2}-\dfrac1{x_1}$．" "\n"
        r"两边同乘 $x_2$：$x_1x_2+x_2^2=2ax_2+1-\dfrac{x_2}{x_1}$，故" "\n"
        r"$\dfrac{x_2}{x_1}=-x_2^2-x_1x_2+2ax_2+1=-\left(x_2-\dfrac{2a-x_1}2\right)^2+\dfrac{\left(2a-x_1\right)^2}4+1$" "\n"
        r"$\le\dfrac{\left(2a-x_1\right)^2}4+1<\dfrac{\left(2a\right)^2}4+1=a^2+1$（因 $0<x_1<a$ 故 $0<2a-x_1<2a$）．" "\n"
        r"综上，$\dfrac{x_2}{x_1}<a^2+1$．"
    ),
    'review': (
        r"① 原书 OCR 把 $x<a$ 段的 $f\left(x\right)=2a-x-\dfrac1x$ 印成了 $2a-x+\dfrac1x$．" "\n"
        r"　 判据：按 $+$ 号则 $f'\left(x\right)=-1-\dfrac1{x^2}<0$ 恒负，与详解「在 $\left(0,1\right)$ 上递增」矛盾；" "\n"
        r"　 按 $-$ 号则 $f'\left(x\right)=-1+\dfrac1{x^2}$，恰在 $x=1$ 处变号，与「三段单调」完全吻合．" "\n"
        r"② 整题的入口是**先由「存在两解」反推出 $a>1$**：$a\le1$ 时 $f$ 全程递增，无解．" "\n"
        r"　 这一步把参数范围锁定，后面所有构造才有意义．" "\n"
        r"③ ①的两个构造 $h\left(x\right)=f\left(x\right)-f\left(2-x\right)$ 与 $g\left(x\right)=f\left(x\right)-f\left(2a-x\right)$ 是**同一招的两面**：" "\n"
        r"　 分别以 $x=1$ 和 $x=a$ 为对称中心，把「和的范围」转成「函数值的比较」．" "\n"
        r"④ ②的（i）中由 $\dfrac{1+x_1^2}{x_1}=\dfrac{1+x_2^2}{x_2}$ 可直接得 $x_1x_2=1$：" "\n"
        r"　 交叉相乘 $x_2+x_1^2x_2=x_1+x_1x_2^2$ ⟹ $x_1x_2\left(x_1-x_2\right)=x_1-x_2$ ⟹ $x_1x_2=1$．" "\n"
        r"　 于是 $\dfrac{x_2}{x_1}=x_2^2$，也可从这条路得到结论．" "\n"
        r"⑤ 数值复核（$a=2$）：同侧取 $x_1=0.8$、$x_2=1.25$（$x_1x_2=1$），" "\n"
        r"　 $f$ 值均为 $1.95$ ✓，$\dfrac{x_2}{x_1}=1.5625<5$ ✓，$x_1+x_2=2.05\in\left(2,4\right)$ ✓；" "\n"
        r"　 异侧取 $x_1=1.5$，解得 $x_2=2.2732$，$\dfrac{x_2}{x_1}=1.5155<5$ ✓，$x_1+x_2=3.7732\in\left(2,4\right)$ ✓．" "\n"
        r"**通法（绝对值函数 + 双解）**：先按绝对值分点把 $f$ 写成分段式并定出各段单调性，" "\n"
        r"　 再由「存在两解」锁定参数范围，最后用「对称中心 ± 差值」的差函数证明和/积的范围．"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-163'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-163-V2',
}

# ============================================================
# M-T-165-E1
# ============================================================
T165_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f\left(x\right)=x\log_ax-\left(2+\dfrac1{\ln a}\right)x$（$a$ 为常数，$a>0$ 且 $a\ne1$）．" "\n"
        r"（1）求函数 $f\left(x\right)$ 的单调区间；" "\n"
        r"（2）当 $a=e$ 时，若 $g\left(x\right)=f\left(x\right)-\dfrac12mx^2+3x$ 有两个极值点 $x_1,x_2$，" "\n"
        r"证明：$\ln x_1+\ln x_2>0$．"
    ),
    'opts': [],
    'answer': (
        r"（1）$a>1$ 时增区间为 $\left(a^2,+\infty\right)$、减区间为 $\left(0,a^2\right)$；" "\n"
        r"$0<a<1$ 时增区间为 $\left(0,a^2\right)$、减区间为 $\left(a^2,+\infty\right)$；（2）证明见解析"
    ),
    'analysis': (
        r"（1）$\dfrac{\mathrm d}{\mathrm dx}\left(x\log_ax\right)=\log_ax+\dfrac1{\ln a}$，" "\n"
        r"　 故 $f'\left(x\right)=\log_ax-2$，再按 $a>1$ 与 $0<a<1$ 分两种情况解不等式；" "\n"
        r"（2）$a=e$ 时 $g'\left(x\right)=\ln x+1-mx$，两式相加减后用 $t=\dfrac{x_2}{x_1}>1$ 化为" "\n"
        r"　 $\ln t>\dfrac{2\left(t-1\right)}{t+1}$．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"$f\left(x\right)$ 的定义域为 $\left(0,+\infty\right)$．由 $\log_ax=\dfrac{\ln x}{\ln a}$ 得" "\n"
        r"$\dfrac{\mathrm d}{\mathrm dx}\left(x\log_ax\right)=\log_ax+x\cdot\dfrac1{x\ln a}=\log_ax+\dfrac1{\ln a}$，" "\n"
        r"故 $f'\left(x\right)=\log_ax+\dfrac1{\ln a}-\left(2+\dfrac1{\ln a}\right)=\log_ax-2=\log_a\dfrac x{a^2}$．" "\n"
        r"当 $a>1$ 时：$f'\left(x\right)>0\iff\dfrac x{a^2}>1\iff x>a^2$，" "\n"
        r"故增区间为 $\left(a^2,+\infty\right)$，减区间为 $\left(0,a^2\right)$．" "\n"
        r"当 $0<a<1$ 时：$\log_a u>0\iff0<u<1$，" "\n"
        r"故 $f'\left(x\right)>0\iff0<\dfrac x{a^2}<1\iff0<x<a^2$，" "\n"
        r"增区间为 $\left(0,a^2\right)$，减区间为 $\left(a^2,+\infty\right)$．" "\n"
        r"**第（2）问**" "\n"
        r"$a=e$ 时 $\ln a=1$，$f\left(x\right)=x\ln x-3x$，于是" "\n"
        r"$g\left(x\right)=x\ln x-3x-\dfrac12mx^2+3x=x\ln x-\dfrac12mx^2$，" "\n"
        r"$g'\left(x\right)=\ln x+1-mx$．" "\n"
        r"$g$ 有两个极值点即 $\ln x+1-mx=0$ 有两个不同的正根 $x_1,x_2$．设 $0<x_1<x_2$，则" "\n"
        r"$\ln x_1+1=mx_1$　①，$\ln x_2+1=mx_2$　②．" "\n"
        r"①+②：$\ln x_1+\ln x_2+2=m\left(x_1+x_2\right)$；" "\n"
        r"②-①：$\ln x_2-\ln x_1=m\left(x_2-x_1\right)$，即 $m=\dfrac{\ln x_2-\ln x_1}{x_2-x_1}$．" "\n"
        r"代入得" "\n"
        r"$\ln x_1+\ln x_2+2=\dfrac{\left(\ln x_2-\ln x_1\right)\left(x_1+x_2\right)}{x_2-x_1}$" "\n"
        r"$=\dfrac{\left(x_2+x_1\right)\ln\frac{x_2}{x_1}}{x_2-x_1}=\dfrac{t+1}{t-1}\ln t$，其中 $t=\dfrac{x_2}{x_1}>1$．" "\n"
        r"要证 $\ln x_1+\ln x_2>0$，即证 $\dfrac{t+1}{t-1}\ln t>2$，即证 $\ln t>\dfrac{2\left(t-1\right)}{t+1}$．" "\n"
        r"令 $h\left(t\right)=\ln t-\dfrac{2\left(t-1\right)}{t+1}$（$t>1$），则" "\n"
        r"$h'\left(t\right)=\dfrac1t-\dfrac4{\left(t+1\right)^2}=\dfrac{\left(t+1\right)^2-4t}{t\left(t+1\right)^2}=\dfrac{\left(t-1\right)^2}{t\left(t+1\right)^2}>0$，" "\n"
        r"故 $h$ 在 $\left(1,+\infty\right)$ 上递增，$h\left(t\right)>h\left(1\right)=0$．" "\n"
        r"于是 $\ln t>\dfrac{2\left(t-1\right)}{t+1}$，从而 $\ln x_1+\ln x_2>0$，即 $x_1x_2>1$．"
    ),
    'review': (
        r"① 原书把 $f\left(x\right)$ 印成 $x\log_ax-2+\dfrac1{\ln a}x$，" "\n"
        r"　 按此 $f'\left(x\right)=\log_ax+\dfrac1{\ln a}-2+\dfrac1{\ln a}\ne\log_ax-2$，与详解首句矛盾；" "\n"
        r"　 实为 $f\left(x\right)=x\log_ax-\left(2+\dfrac1{\ln a}\right)x$．" "\n"
        r"② 求导是本题第一关：$\dfrac{\mathrm d}{\mathrm dx}\left(x\log_ax\right)=\log_ax+\dfrac1{\ln a}$ 中的" "\n"
        r"　 $\dfrac1{\ln a}$ 项极易漏，而题干里那个「多余的」$\dfrac1{\ln a}x$ 正是为了**把它配掉**．" "\n"
        r"③ $f'\left(x\right)=\log_ax-2=\log_a\dfrac x{a^2}$ 这一步化简让分界点一目了然是 $x=a^2$；" "\n"
        r"　 注意 $0<a<1$ 时 $\log_a u$ **递减**，不等号方向要反过来．" "\n"
        r"④ 第（2）问的 $\ln x_1+\ln x_2>0$ 等价于 $x_1x_2>1$，是「积型极值点偏移」．" "\n"
        r"　 收尾的 $h'\left(t\right)=\dfrac{\left(t-1\right)^2}{t\left(t+1\right)^2}>0$ 分子是完全平方，可直接记．" "\n"
        r"⑤ 数值复核：$m=0.2$ 时两驻点 $x_1=0.3984$、$x_2=19.9715$，" "\n"
        r"　 $\ln x_1+\ln x_2=2.0740>0$ ✓；$m=\dfrac1e-10^{-4}$ 时 $x_1=0.4311$、$x_2=8.5557$，" "\n"
        r"　 $\ln x_1+\ln x_2=1.3051>0$ ✓．" "\n"
        r"**通法（积型极值点偏移）**：由 $g'\left(x_i\right)=0$ 两式相加减，" "\n"
        r"　 用 $\dfrac{\ln x_2-\ln x_1}{x_2-x_1}$ 消参，再令 $t=\dfrac{x_2}{x_1}$ 化为对数平均不等式．"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-165'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-165-E1',
}

# ============================================================
# M-T-165-V1
# ============================================================
T165_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f\left(x\right)=x\ln x-\dfrac a2x^2-x+1$，$a\in\mathbf R$．" "\n"
        r"（1）若函数 $y=f\left(x\right)$ 的图象在点 $\left(1,f\left(1\right)\right)$ 处的切线方程为 $y=-2x+1$，求实数 $a$ 的值；" "\n"
        r"（2）若函数 $f\left(x\right)$ 在定义域内有两个不同的极值点 $x_1,x_2$：" "\n"
        r"（i）求实数 $a$ 的取值范围；" "\n"
        r"（ii）当 $0<m\le2$ 时，证明：$x_1+x_2>\dfrac ma$．"
    ),
    'opts': [],
    'answer': r"（1）$a=2$；（2）（i）$0<a<\dfrac1e$；（ii）证明见解析",
    'analysis': (
        r"（1）由 $f'\left(1\right)=-2$ 且 $f\left(1\right)=-1$ 定 $a$；" "\n"
        r"（2）（i）$f'\left(x\right)=\ln x-ax$ 有两个不同零点，研究 $h\left(x\right)=\ln x-ax$ 的最大值；" "\n"
        r"　 （ii）用 $a=\dfrac{\ln x_1-\ln x_2}{x_1-x_2}$ 代入，令 $t=\dfrac{x_1}{x_2}\in\left(0,1\right)$，" "\n"
        r"　 化为 $g\left(t\right)=\ln t-\dfrac{m\left(t-1\right)}{t+1}<0$，再用判别式定 $g'$ 的符号．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"$f'\left(x\right)=\ln x+1-ax-1=\ln x-ax$，故 $f'\left(1\right)=-a$；" "\n"
        r"又 $f\left(1\right)=0-\dfrac a2-1+1=-\dfrac a2$．" "\n"
        r"切线方程：$y+\dfrac a2=-a\left(x-1\right)$，即 $y=-ax+\dfrac a2$．" "\n"
        r"与 $y=-2x+1$ 对比得 $-a=-2$ 且 $\dfrac a2=1$，故 $a=2$．" "\n"
        r"**第（2）（i）问**" "\n"
        r"$f$ 有两个不同极值点等价于 $f'\left(x\right)=\ln x-ax$ 在 $\left(0,+\infty\right)$ 内有两个不同零点．" "\n"
        r"设 $h\left(x\right)=\ln x-ax$，则 $h'\left(x\right)=\dfrac1x-a=\dfrac{1-ax}x$．" "\n"
        r"当 $a\le0$ 时 $h'\left(x\right)>0$，$h$ 递增，至多一个零点，舍；" "\n"
        r"当 $a>0$ 时，$h$ 在 $\left(0,\dfrac1a\right)$ 上递增、在 $\left(\dfrac1a,+\infty\right)$ 上递减，" "\n"
        r"$h_{\max}=h\left(\dfrac1a\right)=\ln\dfrac1a-1=-\ln a-1$．" "\n"
        r"有两个零点需 $h_{\max}>0$，即 $\ln a<-1$，得 $0<a<\dfrac1e$．" "\n"
        r"（此时 $h\left(1\right)=-a<0$，$h\left(\dfrac1{a^2}\right)=2\ln\dfrac1a-\dfrac1a<0$，由 $\ln x<x$ 及零点存在定理知两根确实存在．）" "\n"
        r"**第（2）（ii）问**" "\n"
        r"由 $h\left(x_1\right)=h\left(x_2\right)=0$ 得 $\ln x_1=ax_1$、$\ln x_2=ax_2$，故" "\n"
        r"$a=\dfrac{\ln x_1}{x_1}=\dfrac{\ln x_2}{x_2}=\dfrac{\ln x_1-\ln x_2}{x_1-x_2}$．" "\n"
        r"要证 $x_1+x_2>\dfrac ma$，即证 $\dfrac{\left(x_1+x_2\right)\left(\ln x_1-\ln x_2\right)}{x_1-x_2}>m$．" "\n"
        r"令 $t=\dfrac{x_1}{x_2}\in\left(0,1\right)$（设 $x_1<x_2$），则" "\n"
        r"$\dfrac{\left(x_1+x_2\right)\ln\frac{x_1}{x_2}}{x_1-x_2}=\dfrac{t+1}{t-1}\ln t>m$．" "\n"
        r"因 $t-1<0$，两边同乘 $t-1$ 变号：$\left(t+1\right)\ln t<m\left(t-1\right)$，" "\n"
        r"再除以 $t+1>0$：$\ln t-\dfrac{m\left(t-1\right)}{t+1}<0$．" "\n"
        r"令 $g\left(t\right)=\ln t-\dfrac{m\left(t-1\right)}{t+1}$（$0<t<1$），则" "\n"
        r"$g'\left(t\right)=\dfrac1t-\dfrac{2m}{\left(t+1\right)^2}=\dfrac{t^2-2\left(m-1\right)t+1}{t\left(t+1\right)^2}$．" "\n"
        r"设 $p\left(t\right)=t^2-2\left(m-1\right)t+1$，判别式" "\n"
        r"$\Delta=4\left(m-1\right)^2-4=4m\left(m-2\right)\le0$（因 $0<m\le2$），且二次项系数为正，" "\n"
        r"故 $p\left(t\right)\ge0$，即 $g'\left(t\right)\ge0$，$g$ 在 $\left(0,1\right)$ 上递增．" "\n"
        r"于是 $g\left(t\right)<g\left(1\right)=0$，不等式成立，故 $x_1+x_2>\dfrac ma$．"
    ),
    'review': (
        r"① 第（1）问**不要用「切点在切线上」这一个条件**：" "\n"
        r"　 斜率 $f'\left(1\right)=-a=-2$ 与点 $\left(1,-\frac a2\right)$ 在 $y=-2x+1$ 上（得 $-\frac a2=-1$）" "\n"
        r"　 两个条件都给出 $a=2$，互相印证．" "\n"
        r"② （i）中 $h_{\max}>0$ 只是必要条件，**要补零点存在性的论证**：" "\n"
        r"　 $h\left(1\right)=-a<0$、$h\left(\frac1{a^2}\right)=2\ln\frac1a-\frac1a<0$（用 $\ln x<x$），" "\n"
        r"　 结合 $h_{\max}>0$ 且 $\frac1a\in\left(1,\frac1{a^2}\right)$，两根分别落在 $\left(1,\frac1a\right)$ 与 $\left(\frac1a,\frac1{a^2}\right)$ 内．" "\n"
        r"③ （ii）的换元方向要注意：令 $t=\dfrac{x_1}{x_2}\in\left(0,1\right)$，" "\n"
        r"　 于是 $t-1<0$，**同乘 $t-1$ 时必须变号**——这是本题最容易错的一步．" "\n"
        r"④ $g'\left(t\right)$ 的分子 $t^2-2\left(m-1\right)t+1$ 是**关于 $t$ 的二次式**，" "\n"
        r"　 判别式 $\Delta=4m\left(m-2\right)$ 恰好由题设 $0<m\le2$ 保证 $\le0$——这个条件不是随便给的．" "\n"
        r"⑤ 数值复核：$a=0.1$ 时 $x_1=1.1183$、$x_2=35.7715$，$x_1+x_2=36.89>\dfrac2a=20$ ✓；" "\n"
        r"　 $a=0.3$（接近 $\frac1e$）时 $x_1+x_2=7.5691>\dfrac2{0.3}=6.6667$ ✓（越接近上界越紧）．" "\n"
        r"**通法（和型极值点偏移的参数版）**：把要证的 $x_1+x_2>\dfrac ma$ 先写成" "\n"
        r"　 $\dfrac{\left(x_1+x_2\right)\left(\ln x_1-\ln x_2\right)}{x_1-x_2}>m$，再令 $t=\dfrac{x_1}{x_2}$ 化为单变量不等式．"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-165'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-165-V1',
}

# ============================================================
# M-T-165-V2
# ============================================================
T165_V2 = {
    'type': '解答',
    'stem_text': (
        r"$x_1$ 和 $x_2$ 是关于 $x$ 的方程 $x-ae^x+2=0$ 的两个不同的实数根．" "\n"
        r"（1）求实数 $a$ 的取值范围；" "\n"
        r"（2）若 $x_2-x_1\ge\ln2$，求证：$\dfrac{x_2+x_1}2>\ln2-2$．"
    ),
    'opts': [],
    'answer': r"（1）$0<a<e$；（2）证明见解析",
    'analysis': (
        r"（1）分离参数 $a=\dfrac{x+2}{e^x}$，研究 $f\left(x\right)=\left(x+2\right)e^{-x}$ 的图象；" "\n"
        r"（2）换元 $x=\ln t$ 把方程化为 $\ln t-at+2=0$，则 $x_2-x_1\ge\ln2$ 变成 $\dfrac{t_1}{t_2}\le\dfrac12$，" "\n"
        r"　 两式相加减后用 $g\left(m\right)=\dfrac{\left(m+1\right)\ln m}{m-1}$ 的单调性给出 $\ln\left(t_1t_2\right)$ 的下界．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"由 $x-ae^x+2=0$ 得 $a=\dfrac{x+2}{e^x}$．令 $f\left(x\right)=\left(x+2\right)e^{-x}$，则" "\n"
        r"$f'\left(x\right)=e^{-x}-\left(x+2\right)e^{-x}=-\left(x+1\right)e^{-x}$．" "\n"
        r"$x<-1$ 时 $f'\left(x\right)>0$，$f$ 递增；$x>-1$ 时 $f'\left(x\right)<0$，$f$ 递减．" "\n"
        r"故 $f_{\max}=f\left(-1\right)=e$．又 $x\to-\infty$ 时 $f\left(x\right)\to-\infty$；" "\n"
        r"$x>-1$ 时 $f\left(x\right)>0$ 且 $x\to+\infty$ 时 $f\left(x\right)\to0$．" "\n"
        r"结合图象：当 $0<a<e$ 时直线 $y=a$ 与曲线有两个交点（一个在 $\left(-2,-1\right)$ 内，一个在 $\left(-1,+\infty\right)$ 内）；" "\n"
        r"$a\le0$ 或 $a=e$ 时只有一个交点；$a>e$ 时无交点．故 $0<a<e$．" "\n"
        r"**第（2）问**" "\n"
        r"设 $t_1=e^{x_1}$、$t_2=e^{x_2}$（$t_1,t_2>0$，$t_1<t_2$），则方程化为" "\n"
        r"$\ln t-at+2=0$，即 $\ln t_1-at_1+2=0$　①，$\ln t_2-at_2+2=0$　②．" "\n"
        r"由 $x_2-x_1\ge\ln2$ 得 $\ln\dfrac{t_2}{t_1}\ge\ln2$，即 $\dfrac{t_2}{t_1}\ge2$．" "\n"
        r"令 $m=\dfrac{t_1}{t_2}$，则 $m\in\left(0,\dfrac12\right]$．" "\n"
        r"②-①：$a=\dfrac{\ln t_2-\ln t_1}{t_2-t_1}$；" "\n"
        r"①+②：$\ln\left(t_1t_2\right)+4=a\left(t_1+t_2\right)$．" "\n"
        r"代入得" "\n"
        r"$\ln\left(t_1t_2\right)+4=\dfrac{\left(\ln t_2-\ln t_1\right)\left(t_1+t_2\right)}{t_2-t_1}$" "\n"
        r"$=\dfrac{\left(m+1\right)\left(-\ln m\right)}{1-m}=\dfrac{\left(m+1\right)\ln m}{m-1}$．" "\n"
        r"令 $g\left(m\right)=\dfrac{\left(m+1\right)\ln m}{m-1}$（$0<m<1$），则" "\n"
        r"$g'\left(m\right)=\dfrac{m-\frac1m-2\ln m}{\left(m-1\right)^2}$．" "\n"
        r"设 $h\left(m\right)=m-\dfrac1m-2\ln m$，则 $h'\left(m\right)=1+\dfrac1{m^2}-\dfrac2m=\dfrac{\left(m-1\right)^2}{m^2}>0$，" "\n"
        r"又 $h\left(1\right)=0$，故 $0<m<1$ 时 $h\left(m\right)<0$，即 $g'\left(m\right)<0$，$g$ 在 $\left(0,1\right)$ 上递减．" "\n"
        r"于是当 $m\in\left(0,\dfrac12\right]$ 时 $g\left(m\right)\ge g\left(\dfrac12\right)=\dfrac{\frac32\ln\frac12}{-\frac12}=3\ln2=\ln8$．" "\n"
        r"故 $\ln\left(t_1t_2\right)+4\ge\ln8$，即 $x_1+x_2=\ln\left(t_1t_2\right)\ge\ln8-4=3\ln2-4$．" "\n"
        r"于是 $\dfrac{x_1+x_2}2\ge\dfrac{3\ln2-4}2=\dfrac32\ln2-2>\ln2-2$（因 $\ln2>0$）．"
    ),
    'review': (
        r"① 原书详解写「当 $x>-1$ 时 $f\left(x\right)$ 在 $\left(-1,+\infty\right)$ 时递增」，应为**递减**；" "\n"
        r"　 由 $f'\left(x\right)=-\left(x+1\right)e^{-x}$ 直接判定即可，结论 $0<a<e$ 不受影响．" "\n"
        r"② 第（1）问的难点在 $a\le0$ 的情形：$x<-2$ 时 $f\left(x\right)<0$，" "\n"
        r"　 故 $y=a<0$ 只与曲线交于**一点**（在 $\left(-\infty,-2\right)$ 内），不能算「两个根」．" "\n"
        r"③ 换元 $x=\ln t$ 是本题题眼：它把「根的差 $x_2-x_1$」变成「根的比 $\dfrac{t_2}{t_1}$」，" "\n"
        r"　 而范围 $\ge\ln2$ 恰好对应整齐的比值 $\ge2$．" "\n"
        r"④ 最后一步的严格性值得注意：由 $\ln\left(t_1t_2\right)\ge\ln8-4$ 只能得 $\dfrac{x_1+x_2}2\ge\dfrac32\ln2-2$，" "\n"
        r"　 而 $\dfrac32\ln2-2>\ln2-2$（因 $\ln2>0$），所以结论中的**严格大于号是成立的**，" "\n"
        r"　 并不是靠「$\ge$ 推出 $>$」这种错误推理．" "\n"
        r"⑤ 数值复核：取 $a=2.5601$（使 $x_2-x_1\approx\ln2$），得 $x_1=-1.3075$、$x_2=-0.6127$，" "\n"
        r"　 $x_2-x_1=0.6949\approx\ln2$ ✓，$\dfrac{x_1+x_2}2=-0.9601>\ln2-2=-1.3069$ ✓；" "\n"
        r"　 取 $a=0.5$ 得 $\dfrac{x_1+x_2}2=0.0891>-1.3069$ ✓．" "\n"
        r"**通法（换元 $x=\ln t$）**：当方程含 $x$ 与 $e^x$ 且题目给出「根之差」条件时，" "\n"
        r"　 令 $x=\ln t$ 可把「差」化为「比」，从而用比值 $m$ 的单变量函数处理．"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-165'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-165-V2',
}

# ============================================================
# M-T-347-V1
# ============================================================
T347_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知椭圆 $C:\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$（$a>b>0$），$P_1\left(0,1\right)$，$P_2\left(-1,\dfrac{\sqrt3}2\right)$ 两点在椭圆 $C$ 上．" "\n"
        r"（1）求椭圆 $C$ 的方程；" "\n"
        r"（2）设直线 $l$ 不经过 $P_1$ 点且与 $C$ 相交于 $A,B$ 两点．若直线 $P_1A$ 与直线 $P_1B$ 的斜率的和为 $-1$，" "\n"
        r"证明：$l$ 过定点．"
    ),
    'opts': [],
    'answer': r"（1）$\dfrac{x^2}4+y^2=1$；（2）$l$ 过定点 $\left(2,-1\right)$",
    'analysis': (
        r"（1）代入 $P_1$ 得 $b=1$，再代入 $P_2$ 得 $a^2=4$；" "\n"
        r"（2）分 $l$ 斜率存在与不存在讨论：$k_{P_1A}+k_{P_1B}=2k+\left(t-1\right)\dfrac{x_1+x_2}{x_1x_2}$，" "\n"
        r"　 用韦达代入得 $2k-\dfrac{2kt}{t+1}=-1$，解出 $t=-2k-1$，即得定点 $\left(2,-1\right)$．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"由 $P_1\left(0,1\right)$ 在 $C$ 上得 $\dfrac1{b^2}=1$，即 $b=1$．" "\n"
        r"由 $P_2\left(-1,\dfrac{\sqrt3}2\right)$ 在 $C$ 上得 $\dfrac1{a^2}+\dfrac{3}4=1$，故 $a^2=4$．" "\n"
        r"所以椭圆 $C$ 的方程为 $\dfrac{x^2}4+y^2=1$．" "\n"
        r"**第（2）问**" "\n"
        r"当 $l$ 的斜率不存在时，设 $l:x=m$（$m\ne0$）．由对称性，两交点 $A\left(m,y_0\right)$、$B\left(m,-y_0\right)$，" "\n"
        r"$k_{P_1A}+k_{P_1B}=\dfrac{y_0-1}m+\dfrac{-y_0-1}m=\dfrac{-2}m=-1$，得 $m=2$；" "\n"
        r"但 $x=2$ 是椭圆的右切线，与 $C$ 只有一个公共点，不合题意．" "\n"
        r"当 $l$ 的斜率存在时，设 $l:y=kx+t$（$t\ne1$，否则 $l$ 过 $P_1$），$A\left(x_1,y_1\right)$、$B\left(x_2,y_2\right)$．" "\n"
        r"联立 $\begin{cases}y=kx+t\\x^2+4y^2=4\end{cases}$ 消去 $y$ 得" "\n"
        r"$\left(4k^2+1\right)x^2+8ktx+4t^2-4=0$，" "\n"
        r"$\Delta=16\left(4k^2-t^2+1\right)>0$，且 $x_1+x_2=-\dfrac{8kt}{4k^2+1}$，$x_1x_2=\dfrac{4t^2-4}{4k^2+1}$．" "\n"
        r"于是" "\n"
        r"$k_{P_1A}+k_{P_1B}=\dfrac{y_1-1}{x_1}+\dfrac{y_2-1}{x_2}=\dfrac{kx_1+t-1}{x_1}+\dfrac{kx_2+t-1}{x_2}$" "\n"
        r"$=2k+\left(t-1\right)\dfrac{x_1+x_2}{x_1x_2}=2k-\left(t-1\right)\cdot\dfrac{8kt}{4t^2-4}=2k-\dfrac{2kt}{t+1}$．" "\n"
        r"令其等于 $-1$：$2k-\dfrac{2kt}{t+1}=-1$，两边乘 $t+1$ 得" "\n"
        r"$2k\left(t+1\right)-2kt=-\left(t+1\right)$，即 $2k=-t-1$，故 $t=-2k-1$．" "\n"
        r"此时 $\Delta>0$ 化为 $4k^2-\left(2k+1\right)^2+1>0$，即 $-4k>0$，故 $k<0$．" "\n"
        r"于是 $l:y=kx-2k-1=k\left(x-2\right)-1$，恒过定点 $\left(2,-1\right)$．"
    ),
    'review': (
        r"① 斜率不存在时算出 $m=2$ 却要**舍去**——因为 $x=2$ 与椭圆相切，" "\n"
        r"　 不满足「相交于两点」．定点题一定要检验 $\Delta>0$．" "\n"
        r"② 化简 $\left(t-1\right)\dfrac{x_1+x_2}{x_1x_2}$ 时出现了 $\dfrac{8kt}{4t^2-4}=\dfrac{2kt}{t^2-1}$，" "\n"
        r"　 与外面的 $\left(t-1\right)$ 约掉一个 $t-1$，得 $\dfrac{2kt}{t+1}$——这一步约分是整套计算的枢纽．" "\n"
        r"③ 条件 $t\ne1$（$l$ 不过 $P_1$）保证了 $x_1,x_2\ne0$ 时分母不为零，推理才合法．" "\n"
        r"④ 最后 $\Delta>0$ 反过来限制了 $k<0$：**定点不是对任意 $k$ 都有对应的直线**，" "\n"
        r"　 只有 $k<0$ 时直线才真正与椭圆交于两点．这是定点题的标准收尾检查．" "\n"
        r"⑤ 数值复核：取 $k=-1$，则 $t=1$——但 $t\ne1$，故取 $k=-0.5$，$t=0$：" "\n"
        r"　 联立 $y=-0.5x$ 与 $x^2+4y^2=4$ 得 $2x^2=4$，$x=\pm\sqrt2$；" "\n"
        r"　 $k_{P_1A}+k_{P_1B}=\dfrac{-0.5\sqrt2-1}{\sqrt2}+\dfrac{0.5\sqrt2-1}{-\sqrt2}=\left(-0.5-0.7071\right)+\left(-0.5+0.7071\right)=-1$ ✓" "\n"
        r"　 且直线 $y=-0.5x$ 过 $\left(2,-1\right)$ ✓．" "\n"
        r"**通法（斜率和为定值 ⟹ 定点）**：把 $k_{PA}+k_{PB}$ 全用韦达表示后，" "\n"
        r"　 必能整理成 $t=\alpha k+\beta$ 的一次关系，则定点为 $\left(-\alpha,\beta\right)$．"
    ),
    'difficulty': 0.82,
    'topics': ['M-T-347'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-347-V1',
}

# ============================================================
# M-T-347-V2
# ============================================================
T347_V2 = {
    'type': '解答',
    'stem_text': (
        r"在平面直角坐标系 $xOy$ 中，动点 $P$ 与定点 $F\left(2,0\right)$ 的距离和它到定直线 $l:x=\dfrac32$ 的距离之比是常数 $\dfrac{2\sqrt3}3$，记 $P$ 的轨迹为曲线 $E$．" "\n"
        r"（1）求曲线 $E$ 的方程；" "\n"
        r"（2）设过点 $A\left(\sqrt3,0\right)$ 的两条互相垂直的直线分别与曲线 $E$ 交于点 $M,N$（异于点 $A$），" "\n"
        r"求证：直线 $MN$ 过定点．"
    ),
    'opts': [],
    'answer': r"（1）$\dfrac{x^2}3-y^2=1$；（2）直线 $MN$ 过定点 $\left(2\sqrt3,0\right)$",
    'analysis': (
        r"（1）直接用距离比列方程 $\dfrac{\sqrt{\left(x-2\right)^2+y^2}}{\left\lvert x-\frac32\right\rvert}=\dfrac{2\sqrt3}3$ 化简；" "\n"
        r"　 （也可由 $e=\dfrac ca=\dfrac2{\sqrt3}$、准线 $x=\dfrac{a^2}c=\dfrac32$ 反推 $a=\sqrt3$、$c=2$．）" "\n"
        r"（2）设 $MN:y=kx+m$，由 $\overrightarrow{AM}\cdot\overrightarrow{AN}=0$ 得关于 $k,m$ 的二次齐次式" "\n"
        r"　 $m^2+3\sqrt3km+6k^2=0$，两根中 $m=-\sqrt3k$ 对应过 $A$ 的直线（舍）．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"设 $P\left(x,y\right)$，由题意" "\n"
        r"$\dfrac{\sqrt{\left(x-2\right)^2+y^2}}{\left\lvert x-\frac32\right\rvert}=\dfrac{2\sqrt3}3$．" "\n"
        r"两边平方并整理：$3\left[\left(x-2\right)^2+y^2\right]=4\left(x-\dfrac32\right)^2$，" "\n"
        r"$3x^2-12x+12+3y^2=4x^2-12x+9$，" "\n"
        r"得 $3y^2-x^2=-3$，即 $\dfrac{x^2}3-y^2=1$．" "\n"
        r"**第（2）问**" "\n"
        r"设 $M\left(x_1,y_1\right)$、$N\left(x_2,y_2\right)$，注意 $A\left(\sqrt3,0\right)$ 是双曲线的右顶点．" "\n"
        r"当 $MN$ 斜率不存在时，由 $AM\perp AN$ 且对称性可设 $AM:y=x-\sqrt3$、$AN:y=-x+\sqrt3$；" "\n"
        r"分别与 $\dfrac{x^2}3-y^2=1$ 联立解得 $M\left(2\sqrt3,3\right)$、$N\left(2\sqrt3,-3\right)$，" "\n"
        r"此时 $MN:x=2\sqrt3$ 过点 $\left(2\sqrt3,0\right)$．" "\n"
        r"当 $MN$ 斜率存在时，设 $MN:y=kx+m$（$k\ne\pm\dfrac{\sqrt3}3$）．" "\n"
        r"联立 $\begin{cases}y=kx+m\\x^2-3y^2=3\end{cases}$ 消去 $y$ 得" "\n"
        r"$\left(1-3k^2\right)x^2-6kmx-3m^2-3=0$，" "\n"
        r"$x_1+x_2=\dfrac{6km}{1-3k^2}$，$x_1x_2=\dfrac{-3m^2-3}{1-3k^2}$．" "\n"
        r"由 $AM\perp AN$ 得 $\overrightarrow{AM}\cdot\overrightarrow{AN}=0$，即" "\n"
        r"$y_1y_2=-\left(x_1-\sqrt3\right)\left(x_2-\sqrt3\right)$．" "\n"
        r"左边 $=\left(kx_1+m\right)\left(kx_2+m\right)=k^2x_1x_2+km\left(x_1+x_2\right)+m^2$；" "\n"
        r"右边 $=-x_1x_2+\sqrt3\left(x_1+x_2\right)-3$．" "\n"
        r"移项得 $\left(k^2+1\right)x_1x_2+\left(km-\sqrt3\right)\left(x_1+x_2\right)+m^2+3=0$．" "\n"
        r"代入韦达并同乘 $\left(1-3k^2\right)$：" "\n"
        r"$-3\left(k^2+1\right)\left(m^2+1\right)+6km\left(km-\sqrt3\right)+\left(m^2+3\right)\left(1-3k^2\right)=0$，" "\n"
        r"展开合并得 $-2\left(m^2+3\sqrt3km+6k^2\right)=0$，即" "\n"
        r"$m^2+3\sqrt3km+6k^2=0$．" "\n"
        r"解得 $m=\dfrac{-3\sqrt3k\pm\sqrt{27k^2-24k^2}}2$，即 $m=-\sqrt3k$ 或 $m=-2\sqrt3k$．" "\n"
        r"当 $m=-\sqrt3k$ 时，$MN:y=k\left(x-\sqrt3\right)$ 过点 $A$，与 $M,N$ 异于 $A$ 矛盾，舍去；" "\n"
        r"当 $m=-2\sqrt3k$ 时，$MN:y=k\left(x-2\sqrt3\right)$，恒过定点 $\left(2\sqrt3,0\right)$．" "\n"
        r"综上，直线 $MN$ 过定点 $\left(2\sqrt3,0\right)$．"
    ),
    'review': (
        r"① 第（1）问的常数 $\dfrac{2\sqrt3}3=\dfrac2{\sqrt3}$ 就是**离心率** $e=\dfrac ca$：" "\n"
        r"　 $F\left(2,0\right)$ 是焦点 ⟹ $c=2$；准线 $x=\dfrac32=\dfrac{a^2}c$ ⟹ $a^2=3$．" "\n"
        r"　 认出这一点可跳过平方化简直接写方程，但**距离比是双曲线的第二定义**，值得写全．" "\n"
        r"② 展开 $-3\left(k^2+1\right)\left(m^2+1\right)+6km\left(km-\sqrt3\right)+\left(m^2+3\right)\left(1-3k^2\right)$ 时，" "\n"
        r"　 $k^2m^2$ 项：$-3+6-3=0$ **恰好抵消**——这不是巧合，是 $AM\perp AN$ 的必然结果．" "\n"
        r"　 若你的 $k^2m^2$ 没消掉，一定算错了，可当自检信号．" "\n"
        r"③ 得到的 $m^2+3\sqrt3km+6k^2=0$ 是**二次齐次式**，两根必有其一对应「过 $A$」的退化情形，" "\n"
        r"　 这是垂直型定点题的固定结构．" "\n"
        r"④ 数值复核：取 $k=1$，则 $m=-2\sqrt3\approx-3.4641$，$MN:y=x-3.4641$；" "\n"
        r"　 与 $\dfrac{x^2}3-y^2=1$ 联立得 $x^2-10.3923x+19.5=0$，$x_1=7.9348$、$x_2=2.4575$；" "\n"
        r"　 $y_1=4.4707$、$y_2=-1.0066$；" "\n"
        r"　 $k_{AM}=\dfrac{4.4707}{7.9348-1.7321}=0.7207$，$k_{AN}=\dfrac{-1.0066}{2.4575-1.7321}=-1.3875$，" "\n"
        r"　 乘积 $=-1.0000$ ✓，且直线过 $\left(3.4641,0\right)$ ✓．" "\n"
        r"**通法（垂直型定点）**：$\overrightarrow{AM}\cdot\overrightarrow{AN}=0$ 化为 $\left(k^2+1\right)x_1x_2+\left(km-x_A\right)\left(x_1+x_2\right)+m^2+x_A^2=0$ 型，" "\n"
        r"　 代入韦达后 $k^2m^2$ 必抵消，得到关于 $m,k$ 的二次齐次式，分解因式即得两根．"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-347'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-347-V2',
}

# ============================================================
# M-T-347-V3
# ============================================================
T347_V3 = {
    'type': '解答',
    'stem_text': (
        r"已知椭圆 $C:\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$（$a>b>0$）的上顶点与右焦点连线的斜率为 $-\dfrac{\sqrt2}2$，" "\n"
        r"$C$ 的短轴的两个端点与左、右焦点的连线所构成的四边形的面积为 $2\sqrt2$．" "\n"
        r"（1）求椭圆 $C$ 的标准方程；" "\n"
        r"（2）已知点 $P\left(0,\sqrt2\right)$，若斜率为 $k$（$k\ne0$）的直线 $l$ 与椭圆 $C$ 交于不同的两点 $A,B$，" "\n"
        r"当直线 $AP,BP$ 的倾斜角互补时，试问直线 $l$ 是否过定点？若过定点，求出该定点的坐标；若不过定点，说明理由．"
    ),
    'opts': [],
    'answer': r"（1）$\dfrac{x^2}3+y^2=1$；（2）直线 $l$ 过定点 $\left(0,\dfrac{\sqrt2}2\right)$",
    'analysis': (
        r"（1）由上顶点 $M\left(0,b\right)$、右焦点 $F_2\left(c,0\right)$ 得 $k_{MF_2}=-\dfrac bc=-\dfrac{\sqrt2}2$；" "\n"
        r"　 四边形面积 $=2S_{\triangle MF_1F_2}=2bc=2\sqrt2$；" "\n"
        r"（2）「倾斜角互补」即 $k_{AP}+k_{BP}=0$，设 $l:y=kx+t$ 用韦达代入，" "\n"
        r"　 整理得 $\dfrac{2\sqrt2kt-2k}{t^2-1}=0$，由 $k\ne0$ 得 $t=\dfrac{\sqrt2}2$（与 $k$ 无关）．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"设上顶点 $M\left(0,b\right)$，左、右焦点 $F_1\left(-c,0\right)$、$F_2\left(c,0\right)$．" "\n"
        r"由 $k_{MF_2}=\dfrac{0-b}{c-0}=-\dfrac bc=-\dfrac{\sqrt2}2$ 得 $c=\sqrt2b$．" "\n"
        r"短轴两端点与两焦点构成的四边形面积 $=2S_{\triangle MF_1F_2}=2\times\dfrac12\times2c\times b=2bc=2\sqrt2$，" "\n"
        r"故 $bc=\sqrt2$．与 $c=\sqrt2b$ 联立得 $\sqrt2b^2=\sqrt2$，$b=1$，$c=\sqrt2$，" "\n"
        r"$a=\sqrt{b^2+c^2}=\sqrt3$．所以椭圆 $C$ 的标准方程为 $\dfrac{x^2}3+y^2=1$．" "\n"
        r"**第（2）问**" "\n"
        r"设 $l:y=kx+t$（$k\ne0$），$A\left(x_1,y_1\right)$、$B\left(x_2,y_2\right)$．" "\n"
        r"联立 $\begin{cases}y=kx+t\\x^2+3y^2=3\end{cases}$ 消去 $y$ 得" "\n"
        r"$\left(1+3k^2\right)x^2+6ktx+3t^2-3=0$，" "\n"
        r"$x_1+x_2=-\dfrac{6kt}{1+3k^2}$，$x_1x_2=\dfrac{3t^2-3}{1+3k^2}$．" "\n"
        r"由 $AP,BP$ 的倾斜角互补得 $k_{AP}+k_{BP}=0$，即" "\n"
        r"$\dfrac{y_1-\sqrt2}{x_1}+\dfrac{y_2-\sqrt2}{x_2}=0$．" "\n"
        r"通分：$\dfrac{\left(kx_1+t-\sqrt2\right)x_2+\left(kx_2+t-\sqrt2\right)x_1}{x_1x_2}=0$，" "\n"
        r"分子 $=2kx_1x_2+\left(t-\sqrt2\right)\left(x_1+x_2\right)$，故" "\n"
        r"$2k+\left(t-\sqrt2\right)\dfrac{x_1+x_2}{x_1x_2}=2k-\left(t-\sqrt2\right)\cdot\dfrac{6kt}{3t^2-3}$" "\n"
        r"$=2k-\dfrac{2kt\left(t-\sqrt2\right)}{t^2-1}=\dfrac{2k\left(t^2-1\right)-2kt\left(t-\sqrt2\right)}{t^2-1}=\dfrac{2\sqrt2kt-2k}{t^2-1}$．" "\n"
        r"令其为 $0$：$2\sqrt2kt-2k=0$，由 $k\ne0$ 得 $t=\dfrac{2k}{2\sqrt2k}=\dfrac1{\sqrt2}=\dfrac{\sqrt2}2$．" "\n"
        r"于是 $l:y=kx+\dfrac{\sqrt2}2$，恒过定点 $\left(0,\dfrac{\sqrt2}2\right)$．"
    ),
    'review': (
        r"① 第（1）问的「四边形面积」要认出是**两个全等三角形之和**：" "\n"
        r"　 四个顶点是 $\left(0,b\right)$、$\left(-c,0\right)$、$\left(0,-b\right)$、$\left(c,0\right)$，是对角线长 $2b$ 与 $2c$ 的菱形，" "\n"
        r"　 面积 $=\dfrac12\cdot2b\cdot2c=2bc$．" "\n"
        r"② 「倾斜角互补」的翻译是本题第一关：两角 $\alpha,\beta$ 互补 ⟹ $\tan\alpha+\tan\beta=0$，" "\n"
        r"　 即 $k_{AP}+k_{BP}=0$（注意**不是** $k_{AP}=k_{BP}$，那是平行/重合）．" "\n"
        r"③ 分子化简 $2k\left(t^2-1\right)-2kt\left(t-\sqrt2\right)=2kt^2-2k-2kt^2+2\sqrt2kt=2\sqrt2kt-2k$ 中，" "\n"
        r"　 $kt^2$ 项**恰好抵消**——这是「倾斜角互补」条件的结构性特征，可作自检．" "\n"
        r"④ 本题定点是 $\left(0,\frac{\sqrt2}2\right)$，恰好在 $y$ 轴上，与 $P\left(0,\sqrt2\right)$ 同一条竖直线；" "\n"
        r"　 而 $\frac{\sqrt2}2=\frac12\cdot\sqrt2$，即定点是 $OP$ 的中点，这个巧合可作记忆锚点．" "\n"
        r"⑤ 数值复核：$k=0.5,1,2,-0.7$ 时分别解出两交点，" "\n"
        r"　 计算 $k_{AP}+k_{BP}$ 均为 $0$（误差 $<10^{-12}$）✓．" "\n"
        r"**通法（倾斜角互补 ⟹ 定点）**：$k_{AP}+k_{BP}=0$ 与 $k_{AP}+k_{BP}=$ 常数是同一套路，" "\n"
        r"　 都是把 $\dfrac{y_1-y_P}{x_1}+\dfrac{y_2-y_P}{x_2}$ 全用韦达表示后解出 $t$ 与 $k$ 的关系．"
    ),
    'difficulty': 0.83,
    'topics': ['M-T-347'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-347-V3',
}

# ============================================================
# M-T-355-V1
# ============================================================
T355_V1 = {
    'type': '解答',
    'stem_text': (
        r"抛物线 $C:y^2=4x$，$F$ 是 $C$ 的焦点，过点 $F$ 的直线 $l$ 与 $C$ 相交于 $A,B$ 两点，$O$ 为坐标原点．" "\n"
        r"（1）设 $l$ 的斜率为 $1$，求以 $AB$ 为直径的圆的方程；" "\n"
        r"（2）若 $\overrightarrow{FA}=2\overrightarrow{BF}$，求直线 $l$ 的方程．"
    ),
    'opts': [],
    'answer': (
        r"（1）$\left(x-3\right)^2+\left(y-2\right)^2=16$；" "\n"
        r"（2）$2\sqrt2x-y-2\sqrt2=0$ 或 $2\sqrt2x+y-2\sqrt2=0$"
    ),
    'analysis': (
        r"（1）$l:y=x-1$，联立后用 $x_1+x_2=6$ 求中点与弦长；" "\n"
        r"　 注意焦点弦弦长 $\lvert AB\rvert=x_1+x_2+p$，故半径 $r=\dfrac{x_1+x_2+p}2$．" "\n"
        r"（2）设 $l:y=k\left(x-1\right)$，联立时**以 $y$ 为未知数**得 $ky^2-4y-4k=0$，" "\n"
        r"　 由 $\overrightarrow{FA}=2\overrightarrow{BF}$ 得 $y_1=-2y_2$，结合 $y_1y_2=-4$ 定出 $k$．"
    ),
    'solution': (
        r"抛物线 $y^2=4x$ 中 $p=2$，焦点 $F\left(1,0\right)$．" "\n"
        r"**第（1）问**" "\n"
        r"$l$ 的斜率为 $1$ 且过 $F\left(1,0\right)$，故 $l:y=x-1$．" "\n"
        r"联立 $\begin{cases}y=x-1\\y^2=4x\end{cases}$ 消去 $y$ 得 $\left(x-1\right)^2=4x$，即 $x^2-6x+1=0$．" "\n"
        r"$\Delta=36-4=32>0$，$x_1+x_2=6$，$x_1x_2=1$．" "\n"
        r"$y_1+y_2=\left(x_1-1\right)+\left(x_2-1\right)=x_1+x_2-2=4$，" "\n"
        r"故圆心为 $\left(\dfrac{x_1+x_2}2,\dfrac{y_1+y_2}2\right)=\left(3,2\right)$．" "\n"
        r"由焦点弦公式 $\lvert AB\rvert=x_1+x_2+p=6+2=8$，半径 $r=4$．" "\n"
        r"所求圆的方程为 $\left(x-3\right)^2+\left(y-2\right)^2=16$．" "\n"
        r"**第（2）问**" "\n"
        r"由 $\overrightarrow{FA}=2\overrightarrow{BF}$ 知 $A,F,B$ 三点共线且 $F$ 在 $A,B$ 之间，" "\n"
        r"故 $l$ 的斜率存在，设为 $k$，则 $l:y=k\left(x-1\right)$．" "\n"
        r"由 $x=\dfrac{y^2}4$ 代入直线方程：$\dfrac{ky^2}4=y+k$，即 $ky^2-4y-4k=0$．" "\n"
        r"设 $A\left(x_1,y_1\right)$、$B\left(x_2,y_2\right)$，则 $y_1+y_2=\dfrac4k$，$y_1y_2=-4$．" "\n"
        r"由 $\overrightarrow{FA}=2\overrightarrow{BF}$ 得 $\left(x_1-1,y_1\right)=2\left(1-x_2,-y_2\right)$，比较纵坐标：" "\n"
        r"$y_1=-2y_2$．" "\n"
        r"代入 $y_1y_2=-4$：$-2y_2^2=-4$，故 $y_2^2=2$，$y_2=\pm\sqrt2$．" "\n"
        r"又 $y_1+y_2=-y_2=\dfrac4k$，故 $k=-\dfrac4{y_2}=\mp\dfrac4{\sqrt2}=\mp2\sqrt2$．" "\n"
        r"所以 $k=\pm2\sqrt2$，直线 $l$ 的方程为 $y=\pm2\sqrt2\left(x-1\right)$，" "\n"
        r"即 $2\sqrt2x-y-2\sqrt2=0$ 或 $2\sqrt2x+y-2\sqrt2=0$．"
    ),
    'review': (
        r"① 第（1）问的 $y_1+y_2=x_1+x_2-2$ 用到了「$A,B$ 在直线 $y=x-1$ 上」，" "\n"
        r"　 比逐项解出 $y$ 坐标快得多．" "\n"
        r"② 焦点弦弦长公式 $\lvert AB\rvert=x_1+x_2+p$ **只在直线过焦点时成立**；" "\n"
        r"　 本题 $l$ 过 $F$，故可用，得 $6+2=8$．" "\n"
        r"　 也可直接用 $r=\dfrac{x_1+x_2}2+1=4$（半径 $=$ 中点到准线距离）．" "\n"
        r"③ 第（2）问**以 $y$ 为未知数**联立是关键：得到 $ky^2-4y-4k=0$，" "\n"
        r"　 韦达直接给出 $y_1+y_2$ 与 $y_1y_2$，而条件 $\overrightarrow{FA}=2\overrightarrow{BF}$ 也只涉及 $y$．" "\n"
        r"　 若以 $x$ 为未知数，条件会变成关于 $x$ 的复杂式子，费力不讨好．" "\n"
        r"④ $\overrightarrow{FA}=2\overrightarrow{BF}$ 的纵坐标关系是 $y_1=-2y_2$（**注意是负号**），" "\n"
        r"　 因为 $\overrightarrow{BF}=\left(1-x_2,-y_2\right)$，其纵坐标是 $-y_2$ 而非 $y_2$．" "\n"
        r"⑤ 数值复核：$k=2\sqrt2$ 时 $y_2=-\sqrt2$、$y_1=2\sqrt2$（由 $y_2=-\dfrac4k$ 定号），" "\n"
        r"　 $x_1=\dfrac{y_1^2}4=2$、$x_2=\dfrac{y_2^2}4=\dfrac12$；" "\n"
        r"　 $\overrightarrow{FA}=\left(x_1-1,y_1\right)=\left(1,2\sqrt2\right)$，" "\n"
        r"　 $2\overrightarrow{BF}=2\left(1-x_2,-y_2\right)=2\left(\dfrac12,\sqrt2\right)=\left(1,2\sqrt2\right)$ ✓ 完全一致．" "\n"
        r"**通法（焦点弦上的向量关系）**：$\overrightarrow{FA}=\lambda\overrightarrow{BF}$ ⟹ $y_1=-\lambda y_2$ ⟹ $y_1+y_2=\left(1-\lambda\right)y_2$、$y_1y_2=-\lambda y_2^2=-p^2$；" "\n"
        r"　 由 $y_1y_2=-p^2$ 定出 $y_2$，再由 $y_1+y_2=\dfrac{2p}k$（对 $y^2=2px$）定出 $k$．"
    ),
    'difficulty': 0.72,
    'topics': ['M-T-355'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-355-V1',
}

# ============================================================
# M-T-355-V2
# ============================================================
T355_V2 = {
    'type': '解答',
    'stem_text': (
        r"在圆 $x^2+y^2=4$ 上任取一点 $P$，过点 $P$ 作 $x$ 轴的垂线 $PD$，$D$ 是垂足，" "\n"
        r"点 $M$ 满足 $\overrightarrow{DM}=\lambda\overrightarrow{DP}$（$\lambda>0$）．" "\n"
        r"（1）求点 $M$ 的轨迹方程；" "\n"
        r"（2）若 $\lambda=\dfrac12$，过点 $F\left(\sqrt3,0\right)$ 作与坐标轴不垂直的直线 $l$ 与点 $M$ 的轨迹交于 $A,B$ 两点，" "\n"
        r"点 $C$ 是点 $A$ 关于 $x$ 轴的对称点，试在 $x$ 轴上找一定点 $N$，使 $B,C,N$ 三点共线，" "\n"
        r"并求 $\triangle AFN$ 与 $\triangle BFN$ 面积之比的取值范围．"
    ),
    'opts': [],
    'answer': (
        r"（1）$\dfrac{x^2}4+\dfrac{y^2}{4\lambda^2}=1$；（2）$N\left(\dfrac{4\sqrt3}3,0\right)$，" "\n"
        r"面积比的范围为 $\left(7-4\sqrt3,1\right)\cup\left(1,7+4\sqrt3\right)$"
    ),
    'analysis': (
        r"（1）设 $M\left(x,y\right)$、$P\left(x_0,y_0\right)$，由 $\overrightarrow{DM}=\lambda\overrightarrow{DP}$ 得 $x=x_0$、$y=\lambda y_0$，代入圆方程．" "\n"
        r"（2）$\lambda=\dfrac12$ 时轨迹为椭圆 $\dfrac{x^2}4+y^2=1$．设 $l:y=k\left(x-\sqrt3\right)$，写出 $BC$ 的方程并令 $y=0$，" "\n"
        r"　 得 $x_N=\dfrac{2x_1x_2-\sqrt3\left(x_1+x_2\right)}{x_1+x_2-2\sqrt3}$，代入韦达后恰为常数 $\dfrac{4\sqrt3}3$；" "\n"
        r"　 面积比 $t=-\dfrac{y_1}{y_2}$，由 $\dfrac{\left(y_1+y_2\right)^2}{y_1y_2}=-\left(t+\dfrac1t\right)+2$ 定范围．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"设 $M\left(x,y\right)$、$P\left(x_0,y_0\right)$，则 $D\left(x_0,0\right)$．" "\n"
        r"$\overrightarrow{DM}=\left(x-x_0,y\right)$，$\overrightarrow{DP}=\left(0,y_0\right)$．" "\n"
        r"由 $\overrightarrow{DM}=\lambda\overrightarrow{DP}$ 得 $x-x_0=0$ 且 $y=\lambda y_0$，即 $x_0=x$、$y_0=\dfrac y\lambda$．" "\n"
        r"代入 $x_0^2+y_0^2=4$：$x^2+\dfrac{y^2}{\lambda^2}=4$，即 $\dfrac{x^2}4+\dfrac{y^2}{4\lambda^2}=1$．" "\n"
        r"**第（2）问**" "\n"
        r"$\lambda=\dfrac12$ 时轨迹为椭圆 $\dfrac{x^2}4+y^2=1$．" "\n"
        r"设 $l:y=k\left(x-\sqrt3\right)$（$k\ne0$），$A\left(x_1,y_1\right)$、$B\left(x_2,y_2\right)$，则 $C\left(x_1,-y_1\right)$．" "\n"
        r"联立 $\begin{cases}y=k\left(x-\sqrt3\right)\\x^2+4y^2=4\end{cases}$ 消去 $y$ 得" "\n"
        r"$\left(1+4k^2\right)x^2-8\sqrt3k^2x+12k^2-4=0$，" "\n"
        r"$\Delta=16k^2+16>0$，$x_1+x_2=\dfrac{8\sqrt3k^2}{1+4k^2}$，$x_1x_2=\dfrac{12k^2-4}{1+4k^2}$．" "\n"
        r"直线 $BC$ 的方程：$y+y_1=\dfrac{y_2+y_1}{x_2-x_1}\left(x-x_1\right)$．令 $y=0$ 得交点横坐标" "\n"
        r"$x=\dfrac{y_1x_2+y_2x_1}{y_1+y_2}$" "\n"
        r"$=\dfrac{k\left(x_1-\sqrt3\right)x_2+k\left(x_2-\sqrt3\right)x_1}{k\left(x_1+x_2-2\sqrt3\right)}$" "\n"
        r"$=\dfrac{2x_1x_2-\sqrt3\left(x_1+x_2\right)}{x_1+x_2-2\sqrt3}$" "\n"
        r"$=\dfrac{\frac{2\left(12k^2-4\right)}{1+4k^2}-\frac{\sqrt3\cdot8\sqrt3k^2}{1+4k^2}}{\frac{8\sqrt3k^2}{1+4k^2}-2\sqrt3}$" "\n"
        r"$=\dfrac{24k^2-8-24k^2}{8\sqrt3k^2-2\sqrt3\left(1+4k^2\right)}=\dfrac{-8}{-2\sqrt3}=\dfrac4{\sqrt3}=\dfrac{4\sqrt3}3$．" "\n"
        r"故在 $x$ 轴上存在定点 $N\left(\dfrac{4\sqrt3}3,0\right)$，使 $B,C,N$ 三点共线．" "\n"
        r"再求面积比：$\triangle AFN$ 与 $\triangle BFN$ 有公共底边 $FN$，故" "\n"
        r"$\dfrac{S_{\triangle AFN}}{S_{\triangle BFN}}=\dfrac{\lvert y_1\rvert}{\lvert y_2\rvert}$．" "\n"
        r"由 $y_1y_2=k^2\left(x_1-\sqrt3\right)\left(x_2-\sqrt3\right)=k^2\left[x_1x_2-\sqrt3\left(x_1+x_2\right)+3\right]$" "\n"
        r"$=k^2\left[\dfrac{12k^2-4-24k^2+3\left(1+4k^2\right)}{1+4k^2}\right]=-\dfrac{k^2}{1+4k^2}<0$，" "\n"
        r"故 $y_1,y_2$ 异号，设 $t=-\dfrac{y_1}{y_2}>0$（$t\ne1$，否则 $\lvert y_1\rvert=\lvert y_2\rvert$ 使 $l$ 水平，$k=0$ 被排除）．" "\n"
        r"又 $y_1+y_2=k\left(x_1+x_2\right)-2\sqrt3k=\dfrac{8\sqrt3k^3}{1+4k^2}-2\sqrt3k=-\dfrac{2\sqrt3k}{1+4k^2}$，" "\n"
        r"于是 $\dfrac{\left(y_1+y_2\right)^2}{y_1y_2}=\dfrac{\frac{12k^2}{\left(1+4k^2\right)^2}}{-\frac{k^2}{1+4k^2}}=-\dfrac{12}{1+4k^2}\in\left(-12,0\right)$．" "\n"
        r"另一方面 $\dfrac{\left(y_1+y_2\right)^2}{y_1y_2}=\dfrac{y_1}{y_2}+\dfrac{y_2}{y_1}+2=-\left(t+\dfrac1t\right)+2$．" "\n"
        r"故 $-\left(t+\dfrac1t\right)+2\in\left(-12,0\right)$，即 $2<t+\dfrac1t<14$．" "\n"
        r"由 $t+\dfrac1t>2$ 得 $t\ne1$；由 $t+\dfrac1t<14$ 得 $t^2-14t+1<0$，即 $7-4\sqrt3<t<7+4\sqrt3$．" "\n"
        r"所以 $t\in\left(7-4\sqrt3,1\right)\cup\left(1,7+4\sqrt3\right)$．"
    ),
    'review': (
        r"① 原书题干写「使 $A,B,N$ 三点共线」，应为 **$B,C,N$ 三点共线**：" "\n"
        r"　 若 $A,B,N$ 共线，则 $N$ 必在 $l$ 上，而 $l\cap x$ 轴 $=\left(\sqrt3,0\right)=F$，" "\n"
        r"　 此时 $\triangle AFN$ 退化，面积比无意义．详解全文都在算 $BC$ 与 $x$ 轴的交点，可确信为 $B,C,N$．" "\n"
        r"② 求 $x_N$ 的关键一步是把 $y_i$ 全部换成 $k\left(x_i-\sqrt3\right)$，" "\n"
        r"　 于是分子 $y_1x_2+y_2x_1=k\left[2x_1x_2-\sqrt3\left(x_1+x_2\right)\right]$，" "\n"
        r"　 分母 $y_1+y_2=k\left(x_1+x_2-2\sqrt3\right)$，$k$ **完全约掉** ⟹ 与 $k$ 无关 ⟹ 定点．" "\n"
        r"③ 代入韦达后分子分母都出现 $\dfrac1{1+4k^2}$，约掉后只剩常数，" "\n"
        r"　 且分子 $24k^2-8-24k^2=-8$、分母 $8\sqrt3k^2-2\sqrt3-8\sqrt3k^2=-2\sqrt3$，$k^2$ **全部抵消**——这是定点的必然特征．" "\n"
        r"④ 面积比的处理用了 $\dfrac{\left(y_1+y_2\right)^2}{y_1y_2}=\dfrac{y_1}{y_2}+\dfrac{y_2}{y_1}+2$：" "\n"
        r"　 「和方除以积」把两个变量压成一个 $t$，是求比值范围的**标准动作**．" "\n"
        r"⑤ 数值复核：$k=0.5,1,2,3$ 时算得 $x_N=2.3094010768$，与 $\dfrac{4\sqrt3}3=2.3094010768$ 完全一致 ✓；" "\n"
        r"　 对应的 $t$ 分别为 $0.1270$、$0.2404$、$0.4417$、$0.5700$，均落在" "\n"
        r"　 $\left(7-4\sqrt3,1\right)=\left(0.0718,1\right)$ 内 ✓．" "\n"
        r"**通法（对称点型定点）**：作 $A$ 关于 $x$ 轴的对称点 $C$，则 $BC$ 与 $x$ 轴的交点横坐标" "\n"
        r"　 $x_N=\dfrac{y_1x_2+y_2x_1}{y_1+y_2}$，把 $y_i$ 用直线方程换成 $x_i$ 后全部代入韦达，若为常数即得定点．"
    ),
    'difficulty': 0.86,
    'topics': ['M-T-355'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-355-V2',
}

# ============================================================
# M-T-355-V3
# ============================================================
T355_V3 = {
    'type': '解答',
    'stem_text': (
        r"已知点 $A,B$ 的坐标分别是 $\left(0,-1\right),\left(0,1\right)$，直线 $AM,BM$ 相交于点 $M$，" "\n"
        r"且它们的斜率之积为 $-\dfrac12$．" "\n"
        r"（1）求点 $M$ 轨迹 $C$ 的方程；" "\n"
        r"（2）若过点 $D\left(2,0\right)$ 的直线 $l$ 与（1）中的轨迹 $C$ 交于不同的两点 $E,F$（$E$ 在 $D,F$ 之间），" "\n"
        r"$\overrightarrow{DE}=\lambda\overrightarrow{DF}$，试求 $\lambda$ 的取值范围．"
    ),
    'opts': [],
    'answer': r"（1）$\dfrac{x^2}2+y^2=1$（$x\ne0$）；（2）$3-2\sqrt2<\lambda<1$ 且 $\lambda\ne\dfrac13$",
    'analysis': (
        r"（1）直接写 $\dfrac{y+1}x\cdot\dfrac{y-1}x=-\dfrac12$（$x\ne0$）并化简；" "\n"
        r"（2）由 $\overrightarrow{DE}=\lambda\overrightarrow{DF}$ 把 $E$ 的坐标用 $F$ 与 $\lambda$ 表示，" "\n"
        r"　 代入椭圆方程解出 $x_F=\dfrac{3\lambda-1}{2\lambda}$，再由 $x_F\in\left(-\sqrt2,\sqrt2\right)$ 与 $x_F\ne0$ 反解 $\lambda$．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"设 $M\left(x,y\right)$，则 $k_{AM}=\dfrac{y+1}x$、$k_{BM}=\dfrac{y-1}x$（$x\ne0$）．" "\n"
        r"由 $k_{AM}\cdot k_{BM}=-\dfrac12$ 得 $\dfrac{y^2-1}{x^2}=-\dfrac12$，即 $2\left(y^2-1\right)=-x^2$，" "\n"
        r"整理得 $x^2+2y^2=2$，即 $\dfrac{x^2}2+y^2=1$（$x\ne0$）．" "\n"
        r"**第（2）问**" "\n"
        r"设 $F\left(x_1,y_1\right)$、$E\left(x_2,y_2\right)$，由 $\overrightarrow{DE}=\lambda\overrightarrow{DF}$ 且 $D\left(2,0\right)$ 得" "\n"
        r"$\left(x_2-2,y_2\right)=\lambda\left(x_1-2,y_1\right)$，即 $x_2=\lambda x_1-2\lambda+2$、$y_2=\lambda y_1$．" "\n"
        r"因 $F$ 在椭圆上：$\dfrac{x_1^2}2+y_1^2=1$，即 $y_1^2=1-\dfrac{x_1^2}2$．" "\n"
        r"因 $E$ 在椭圆上：$\dfrac{\left(\lambda x_1-2\lambda+2\right)^2}2+\lambda^2y_1^2=1$．" "\n"
        r"代入 $y_1^2$ 并同乘 $2$：" "\n"
        r"$\left(\lambda x_1-2\lambda+2\right)^2+2\lambda^2-\lambda^2x_1^2=2$．" "\n"
        r"展开：$\lambda^2x_1^2-2\lambda\left(2\lambda-2\right)x_1+\left(2\lambda-2\right)^2+2\lambda^2-\lambda^2x_1^2=2$．" "\n"
        r"$\lambda^2x_1^2$ 项抵消，得 $-4\lambda\left(\lambda-1\right)x_1+4\left(\lambda-1\right)^2+2\lambda^2-2=0$，" "\n"
        r"即 $4\lambda\left(\lambda-1\right)x_1=4\left(\lambda-1\right)^2+2\lambda^2-2=6\lambda^2-8\lambda+2=2\left(3\lambda-1\right)\left(\lambda-1\right)$，" "\n"
        r"故 $x_1=\dfrac{2\left(3\lambda-1\right)\left(\lambda-1\right)}{4\lambda\left(\lambda-1\right)}=\dfrac{3\lambda-1}{2\lambda}$（$\lambda\ne1$）．" "\n"
        r"由 $F$ 在椭圆上且 $x_1\ne0$（否则 $F$ 是 $\left(0,\pm1\right)$，即 $A$ 或 $B$，不在轨迹上）得" "\n"
        r"$-\sqrt2<x_1<\sqrt2$ 且 $x_1\ne0$．" "\n"
        r"又 $E$ 在 $D,F$ 之间，故 $0<\lambda<1$，从而 $2\lambda>0$：" "\n"
        r"由 $\dfrac{3\lambda-1}{2\lambda}<\sqrt2$ 得 $3\lambda-1<2\sqrt2\lambda$，即 $\lambda\left(3-2\sqrt2\right)<1$，" "\n"
        r"$\lambda<\dfrac1{3-2\sqrt2}=3+2\sqrt2$，结合 $\lambda<1$ 得 $\lambda<1$；" "\n"
        r"由 $\dfrac{3\lambda-1}{2\lambda}>-\sqrt2$ 得 $3\lambda-1>-2\sqrt2\lambda$，即 $\lambda\left(3+2\sqrt2\right)>1$，" "\n"
        r"$\lambda>\dfrac1{3+2\sqrt2}=3-2\sqrt2$；" "\n"
        r"由 $x_1\ne0$ 得 $3\lambda-1\ne0$，即 $\lambda\ne\dfrac13$．" "\n"
        r"综上，$3-2\sqrt2<\lambda<1$ 且 $\lambda\ne\dfrac13$．"
    ),
    'review': (
        r"① 原书把题干首句「已知点 $A,B$ 的坐标分别是 $\left(0,-1\right),\left(0,1\right)$，直线 $AM,BM$ 相交于点 $M$，" "\n"
        r"　 且它们的斜率之积为 $-\dfrac12$」挤到了上一题详解的末尾，本题 stem 只剩「（1）求点 $M$ 轨迹 $C$ 的方程」．" "\n"
        r"　 已按详解首句「设 $M\left(x,y\right)$，则 $\dfrac{y+1}x\cdot\dfrac{y-1}x=-\dfrac12$」还原并补全．" "\n"
        r"② 轨迹方程必须**注明 $x\ne0$**：$x=0$ 时斜率不存在，对应的 $\left(0,\pm1\right)$ 恰是 $A,B$ 本身，要挖掉．" "\n"
        r"　 这个 $x\ne0$ 在第（2）问直接变成 $\lambda\ne\dfrac13$，是本题最容易漏的一个点．" "\n"
        r"③ 第（2）问的代数核心：把 $E$ 用 $F$ 和 $\lambda$ 表示后代回椭圆，" "\n"
        r"　 **$x_1^2$ 项必然抵消**（因为 $E,F$ 都在同一条过 $D$ 的直线上，两个交点受同一约束），" "\n"
        r"　 于是剩下关于 $x_1$ 的一次方程，直接解出 $x_1=\dfrac{3\lambda-1}{2\lambda}$．" "\n"
        r"④ 解出 $x_1$ 后**不要解 $\lambda$ 的二次方程**，而用 $x_1\in\left(-\sqrt2,\sqrt2\right)$ 反解——" "\n"
        r"　 这样得到的区间更直接，也不容易漏掉 $\lambda\ne\dfrac13$．" "\n"
        r"⑤ 数值复核：$\lambda=0.2$ 时 $x_1=\dfrac{0.6-1}{0.4}=-1\in\left(-\sqrt2,\sqrt2\right)$ ✓；" "\n"
        r"　 $\lambda=\dfrac13$ 时 $x_1=0$（应排除）✓；$\lambda=0.95$ 时 $x_1=0.9737\in\left(-\sqrt2,\sqrt2\right)$ ✓；" "\n"
        r"　 $\lambda=3-2\sqrt2\approx0.1716$ 时 $x_1=-\sqrt2$（端点，取不到）✓．" "\n"
        r"**通法（共线向量比 ⟹ 范围）**：$\overrightarrow{DE}=\lambda\overrightarrow{DF}$ 型，" "\n"
        r"　 用 $\lambda$ 表示其中一个交点的坐标，再由「该点在曲线上」的坐标范围反解 $\lambda$．"
    ),
    'difficulty': 0.84,
    'topics': ['M-T-355'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-355-V3',
}

QS = [
    T163_E1, T163_V1, T163_V2,
    T165_E1, T165_V1, T165_V2,
    T347_V1, T347_V2, T347_V3,
    T355_V1, T355_V2, T355_V3,
]
