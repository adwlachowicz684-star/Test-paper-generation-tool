# -*- coding: utf-8 -*-
r"""第 110 批：向量「投影与最值 · 旋转轨迹」+ 截面周长 + 空间距离与动点轨迹

    python3 tools/run_batch.py 110

## 选题依据

按「详解完整 + 同题型聚堆 + 无图依赖（图只作示意、条件已全给）+ 可独立数值验算」筛出：

- M-T-245 四题（p210–p211）：向量投影最值、旋转轨迹圆、正方形内等边三角形
- M-T-187 一题（p149）：$|\vec a\cdot\vec c|+|\vec b\cdot\vec c|$ 的三角换元
- M-T-287 三题（p252–p253）：正方体 / 直三棱柱截面周长
- M-T-311 三题（p282–p283）：点到面距离轨迹、平面计数、长方体线面平行

11 题全部由我独立推导一遍并数值对拍（过程写进每题 review）。

## 第一条：投影条件 $\vec a\cdot\vec c=\vec b\cdot\vec c$ ⟺ $\overrightarrow{OC}\perp AB$（M-T-245-E1）

这个等价是整题的枢纽，一行就够：

$$\vec a\cdot\vec c=\vec b\cdot\vec c\ \Longleftrightarrow\ \left(\vec a-\vec b\right)\cdot\vec c=0\ \Longleftrightarrow\ \overrightarrow{BA}\perp\overrightarrow{OC}$$

配上「$\vec c=\lambda\vec a+(1-\lambda)\vec b$（$0<\lambda<1$）⟹ $C$ 在线段 $AB$ 上」，
立刻得到 $|\vec c|=|OC|$ 就是 $O$ 到直线 $AB$ 的距离，于是

$$|\vec c|=\frac{2S_{\triangle AOB}}{|AB|}$$

> ⭐⭐ 凡是「两个数量积相等」，先移项成 $(\vec a-\vec b)\cdot\vec c=0$ 看垂直；
> 凡是「$c$ 是 $a,b$ 的凸组合」，先想到「$C$ 落在线段 $AB$ 上」。
> 这两条一合，长度问题就变成了面积问题。

## 第二条：$x^2+y^2+xy$ 是常数倍 $|\vec c|^2$（M-T-245-E1）

$x=|\vec c|\cos\alpha$、$y=|\vec c|\cos\left(120^\circ-\alpha\right)$，代入得

$$x^2+y^2+xy=\frac34|\vec c|^2$$

**与 $\alpha$ 无关**。$\alpha=0$ 与 $\alpha=60^\circ$ 各代一次都是 $0.75$，可当自检。

> ⭐ 固定夹角为 $120^\circ$ 时，$xy$ 项的系数正好让交叉项配成常数。

## 第三条：轨迹圆的旋转不变性（M-T-245-V2）

$|\vec a|=|\vec b|=|\vec a+\vec b|$ ⟹ $\langle\vec a,\vec b\rangle=120^\circ$ 且 $|\vec a|=|\vec b|$，
即 **$\vec b$ 是 $\vec a$ 绕原点旋转 $\pm120^\circ$ 得到的**。

于是：$\vec a$ 的终点在一个圆上 ⟹ $\vec b$ 的终点在**该圆绕原点旋转 $\pm120^\circ$ 后的圆**上。

$$C(2,0)\ \xrightarrow{\ \text{旋转}\ 120^\circ\ }\ G\left(-1,\sqrt3\right),\qquad |GC|=2\sqrt3$$

> ⭐⭐ **旋转保持圆的形状，圆心跟着转同一个角、半径不变** —— 这是整题唯一需要想通的地方，
> 比逐点算坐标快一个量级。

## 第四条：极化恒等式 $\overrightarrow{PN}\cdot\overrightarrow{PB}=|PE|^2-|BE|^2$（M-T-245-V3）

$E$ 是 $BN$ 中点 ⟹ $\vec{PN}=\vec{PE}+\vec{EN}$、$\vec{PB}=\vec{PE}-\vec{EN}$ ⟹

$$\overrightarrow{PN}\cdot\overrightarrow{PB}=|PE|^2-|EN|^2=|PE|^2-|BE|^2$$

> ⭐⭐ 只要出现「一动点 $P$ 与两定点 $B,N$ 的数量积」，就取 $BN$ 中点 $E$ 化平方差。
> 本题 $|PE|^2$ 要用 $\triangle PEF$ 里的余弦定理算（$F$ 是等边三角形 $PMN$ 底边中点）。

## 第五条：$|\vec c|=R$ ⟹ 圆的参数方程（M-T-187-E1）

$|\vec a\cdot\vec c|+|\vec b\cdot\vec c|$ 带绝对值，必须**按 $\vec c$ 与 $\vec a,\vec b$ 投影的正负分段**，
分界线就是「$\vec c\perp\vec a$」与「$\vec c\perp\vec b$」这两条。

> ⭐⭐ 三段分别化简后都是 $A\cos\theta+B\sin\theta$ 型，直接用辅助角公式。
> 本题三段给的最大值依次是 $16$、$3\sqrt{15}$、$2\sqrt{15}$，最小值依次是 $11$、$2\sqrt{15}$、$11$。

## 第六条：截面周长的通用做法（M-T-287 三题）

1. **写出平面方程**（三点定平面）；
2. **逐棱代入求交点**，一棱不漏；
3. 交点数 = 边数，按序连起来逐段算长度。

> ⭐⭐ 比「延长线找交点 + 相似比」稳得多，而且能自动排出多边形顶点顺序。
> 三题分别对出五边形 $AEGHF$、五边形 $AHFEG$、五边形 $DEF IH$，边数全靠数交点得到。

## 第七条：动点轨迹方程 + 平行线切线（M-T-311-E1）

- $P$ 的轨迹：$P$ 在底面内，到平面 $ABB_1A_1$ 的距离 = 到交线 $AB$ 的距离 ⟹ 抛物线段 $y^2=4-4x$
- $M$ 的轨迹：$MB_1\parallel$ 平面 $EC_1D$ ⟹ $\vec n\cdot\overrightarrow{B_1M}=0$ ⟹ 线段 $2x+y-4=0$

剩下是「曲线上一点到直线的最短距离」，用**与已知直线平行的切线**做：对 $y=\sqrt{4-4x}$ 求导。

> ⭐⭐ 「点到面的距离 = 点到点的距离」「线面平行」这两个条件，本质都是**轨迹方程**。
> 两条轨迹都求出来后，$PM$ 最小值就退化为平面解析几何问题。

## 第八条：长方体侧面展开图是正方形 ⟹ 底面周长 = 高（M-T-311-V3）

展开图宽 = 底面周长 $4a$、高 = 侧棱长 $h$。是边长 $4$ 的正方形 ⟹ $4a=4$、$h=4$ ⟹ $a=1$、$h=4$。

> ⭐ **「侧面展开图是正方形」这句话同时给出底面边长和高**，不要只读出一个。
"""

T245_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知向量 $\vec a$ 与 $\vec b$ 的夹角为 $120^\circ$，且 $\vec a\cdot\vec b=-2$，向量 $\vec c$ 满足 $\vec c=\lambda\vec a+\left(1-\lambda\right)\vec b\left(0<\lambda<1\right)$，且 $\vec a\cdot\vec c=\vec b\cdot\vec c$，记向量 $\vec c$ 在向量 $\vec a$ 与 $\vec b$ 方向上的投影分别为 $x$、$y$．现有两个结论：①若 $\lambda=\dfrac13$，则 $\left|\vec a\right|=2\left|\vec b\right|$；② $x^2+y^2+xy$ 的最大值为 $\dfrac34$．则正确的判断是（　　）"
    ),
    'stem': [
        r"已知向量 $\vec a$ 与 $\vec b$ 的夹角为 $120^\circ$，且 $\vec a\cdot\vec b=-2$，向量 $\vec c$ 满足 $\vec c=\lambda\vec a+\left(1-\lambda\right)\vec b\left(0<\lambda<1\right)$，且 $\vec a\cdot\vec c=\vec b\cdot\vec c$，记向量 $\vec c$ 在向量 $\vec a$ 与 $\vec b$ 方向上的投影分别为 $x$、$y$．现有两个结论：①若 $\lambda=\dfrac13$，则 $\left|\vec a\right|=2\left|\vec b\right|$；② $x^2+y^2+xy$ 的最大值为 $\dfrac34$．则正确的判断是（　　）",
    ],
    'opts': [
        ('A', r"①成立，②成立"),
        ('B', r"①成立，②不成立"),
        ('C', r"①不成立，②成立"),
        ('D', r"①不成立，②不成立"),
    ],
    'answer': 'C',
    'analysis': (
        r"①由 $\vec a\cdot\vec b=-2$ 与夹角 $120^\circ$ 得 $\left|\vec a\right|\left|\vec b\right|=4$，"
        r"代入 $\lambda=\dfrac13$ 并用 $\vec a\cdot\vec c=\vec b\cdot\vec c$ 推出 $\left|\vec a\right|^2=2+2\left|\vec b\right|^2$，"
        r"与 $\left|\vec a\right|=2\left|\vec b\right|$ 联立即矛盾．" "\n"
        r"②把 $\vec a\cdot\vec c=\vec b\cdot\vec c$ 移项成 $\left(\vec a-\vec b\right)\cdot\vec c=0$，"
        r"得 $\overrightarrow{OC}\perp AB$，于是 $\left|\vec c\right|$ 就是 $O$ 到 $AB$ 的距离，"
        r"再用面积法与基本不等式求其最大值 $1$，配合 $x^2+y^2+xy=\dfrac34\left|\vec c\right|^2$ 即得．"
    ),
    'solution': (
        r"由 $\vec a\cdot\vec b=\left|\vec a\right|\left|\vec b\right|\cos120^\circ=-2$ 得 $\left|\vec a\right|\left|\vec b\right|=4$．" "\n"
        r"**判断①** 当 $\lambda=\dfrac13$ 时 $\vec c=\dfrac13\vec a+\dfrac23\vec b$．若此时 $\left|\vec a\right|=2\left|\vec b\right|$，" "\n"
        r"则由 $\left|\vec a\right|\left|\vec b\right|=4$ 得 $2\left|\vec b\right|^2=4$，即 $\left|\vec b\right|=\sqrt2$、$\left|\vec a\right|=2\sqrt2$．" "\n"
        r"又由 $\vec a\cdot\vec c=\vec b\cdot\vec c$ 得" "\n"
        r"$\vec a\cdot\left(\dfrac13\vec a+\dfrac23\vec b\right)=\vec b\cdot\left(\dfrac13\vec a+\dfrac23\vec b\right)$，" "\n"
        r"即 $\dfrac13\left|\vec a\right|^2+\dfrac23\vec a\cdot\vec b=\dfrac13\vec a\cdot\vec b+\dfrac23\left|\vec b\right|^2$．" "\n"
        r"代入 $\vec a\cdot\vec b=-2$：$\dfrac13\left|\vec a\right|^2-\dfrac43=-\dfrac23+\dfrac23\left|\vec b\right|^2$，" "\n"
        r"即 $\left|\vec a\right|^2=2+2\left|\vec b\right|^2$．" "\n"
        r"而 $\left|\vec a\right|=2\left|\vec b\right|$ 给 $\left|\vec a\right|^2=4\left|\vec b\right|^2$，代入得 $4\left|\vec b\right|^2=2+2\left|\vec b\right|^2$，" "\n"
        r"即 $\left|\vec b\right|^2=1$，$\left|\vec b\right|=1$，与上面 $\left|\vec b\right|=\sqrt2$ 矛盾．故①不成立．" "\n"
        r"（等价看法：$\left|\vec a\right|=2\left|\vec b\right|$ 与 $\left|\vec a\right|\left|\vec b\right|=4$ 给 $\left|\vec b\right|=\sqrt2$，" "\n"
        r"此时 $\left|\vec a\right|^2=8$ 而 $2+2\left|\vec b\right|^2=6$，$8\ne6$．）" "\n"
        r"**判断②** 由 $\vec a\cdot\vec c=\vec b\cdot\vec c$ 得 $\left(\vec a-\vec b\right)\cdot\vec c=0$，即 $\overrightarrow{BA}\perp\overrightarrow{OC}$．" "\n"
        r"设 $\overrightarrow{OA}=\vec a$、$\overrightarrow{OB}=\vec b$、$\overrightarrow{OC}=\vec c$．" "\n"
        r"由 $\vec c=\lambda\vec a+\left(1-\lambda\right)\vec b$ 且 $0<\lambda<1$ 知点 $C$ 在线段 $AB$ 上，" "\n"
        r"结合 $\overrightarrow{OC}\perp AB$ 得 $\left|\vec c\right|=\left|OC\right|$ 就是点 $O$ 到直线 $AB$ 的距离．" "\n"
        r"$S_{\triangle AOB}=\dfrac12\left|\vec a\right|\left|\vec b\right|\sin120^\circ=\dfrac12\times4\times\dfrac{\sqrt3}2=\sqrt3$，" "\n"
        r"$\left|AB\right|^2=\left|\vec a\right|^2+\left|\vec b\right|^2-2\vec a\cdot\vec b=\left|\vec a\right|^2+\left|\vec b\right|^2+4\ge2\left|\vec a\right|\left|\vec b\right|+4=12$，" "\n"
        r"当且仅当 $\left|\vec a\right|=\left|\vec b\right|=2$ 时取等，故 $\left|AB\right|_{\min}=2\sqrt3$．" "\n"
        r"于是 $\left|\vec c\right|_{\max}=\dfrac{2S_{\triangle AOB}}{\left|AB\right|_{\min}}=\dfrac{2\sqrt3}{2\sqrt3}=1$．" "\n"
        r"设 $\langle\vec a,\vec c\rangle=\alpha$，则 $\langle\vec b,\vec c\rangle=120^\circ-\alpha$，" "\n"
        r"$x=\left|\vec c\right|\cos\alpha$、$y=\left|\vec c\right|\cos\left(120^\circ-\alpha\right)$，于是" "\n"
        r"$x^2+y^2+xy=\left|\vec c\right|^2\left[\cos^2\alpha+\cos^2\left(120^\circ-\alpha\right)+\cos\alpha\cos\left(120^\circ-\alpha\right)\right]=\dfrac34\left|\vec c\right|^2$．" "\n"
        r"故 $x^2+y^2+xy$ 的最大值为 $\dfrac34\times1^2=\dfrac34$，②成立．" "\n"
        r"综上，①不成立、②成立，故选 $\boxed{\mathrm C}$．"
    ),
    'review': (
        r"① ⭐⭐ **$\vec a\cdot\vec c=\vec b\cdot\vec c$ 的翻译**：移项成 $\left(\vec a-\vec b\right)\cdot\vec c=0$ 就是 $\overrightarrow{OC}\perp AB$．" "\n"
        r"   这一步想通了，$\left|\vec c\right|$ 立刻变成「$O$ 到 $AB$ 的距离」，不再是一个独立的变量．" "\n"
        r"② ⭐⭐ **$\vec c=\lambda\vec a+(1-\lambda)\vec b$（$0<\lambda<1$）⟹ $C$ 在线段 $AB$ 上** ——" "\n"
        r"   这是向量共线定理的凸组合形式，配合垂直才能说 $\left|\vec c\right|$ 是「距离」而不是「到直线的某条斜线段」．" "\n"
        r"③ ⭐ **$x^2+y^2+xy=\dfrac34\left|\vec c\right|^2$ 与 $\alpha$ 无关**：代 $\alpha=0$ 得 $1+\dfrac14-\dfrac12=\dfrac34$，" "\n"
        r"   代 $\alpha=60^\circ$ 得 $\dfrac14+\dfrac14+\dfrac14=\dfrac34$，两处都成立，可当硬自检．" "\n"
        r"④ ⚠ **①的反证要写完整**：只说「假设不成立」不够，要由 $\left|\vec a\right|=2\left|\vec b\right|$ 与 $\left|\vec a\right|\left|\vec b\right|=4$ " "\n"
        r"   解出 $\left|\vec b\right|=\sqrt2$，再代回 $\left|\vec a\right|^2=2+2\left|\vec b\right|^2$ 发现 $8\ne6$ 才算证完．" "\n"
        r"⑤ ⚠ **原书题干在提取中整段丢失**：ref_bank 里只剩「则正确的判断是（　　）」．" "\n"
        r"   我按 $原件/按页还原/p210.txt$ 的「例1」原文补全了全部前置条件与两个结论，" "\n"
        r"   并用详解里的 $\left|\vec a\right|\left|\vec b\right|=4$、$\lambda=\dfrac13$、$\left|AB\right|_{\min}=2\sqrt3$ 三个中间量反向核对无误．" "\n"
        r"⑥ 数值复核：$\left|\vec a\right|=\left|\vec b\right|=2$ 时 $\left|AB\right|=\sqrt{4+4+4}=3.464102=2\sqrt3$ ✓，" "\n"
        r"   $S_{\triangle AOB}=\sqrt3$ ✓，$\left|\vec c\right|_{\max}=2\sqrt3/2\sqrt3=1$ ✓，" "\n"
        r"   $x^2+y^2+xy$ 最大值 $0.75=\dfrac34$ ✓" "\n"
        r"**通法（数量积条件与投影）**：" "\n"
        r"① 两个数量积相等 ⟹ 移项看垂直；" "\n"
        r"② 凸组合 ⟹ 点在线段上；" "\n"
        r"③ 垂直 + 在线段上 ⟹ 长度即点到直线的距离，用面积法求最值；" "\n"
        r"④ 投影的二次式 ⟹ 代入固定夹角后往往与角无关，退化成 $\left|\vec c\right|^2$ 的常数倍．"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-245'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-245-E1',
}

T245_V1 = {
    'type': '填空',
    'stem_text': (
        r"已知平面向量 $\vec a$，$\vec b$ 的夹角为 $\dfrac\pi3$，满足 $\left|\vec a+\vec b\right|=1$．平面向量 $\vec c$ 在 $\vec a$，$\vec b$ 上的投影之和为 $2$，则 $\left|\vec c-\dfrac12\vec a-\dfrac13\vec b\right|$ 的最小值是 ____"
    ),
    'stem': [
        r"已知平面向量 $\vec a$，$\vec b$ 的夹角为 $\dfrac\pi3$，满足 $\left|\vec a+\vec b\right|=1$．平面向量 $\vec c$ 在 $\vec a$，$\vec b$ 上的投影之和为 $2$，则 $\left|\vec c-\dfrac12\vec a-\dfrac13\vec b\right|$ 的最小值是 ____",
    ],
    'opts': [],
    'answer': r"$\dfrac{4\sqrt3-\sqrt7}6$",
    'analysis': (
        r"作代换 $\vec a=2\lambda_1\vec u$、$\vec b=3\lambda_2\vec v$（$\vec u,\vec v$ 分别是 $\vec a,\vec b$ 方向的单位向量，$\langle\vec u,\vec v\rangle=60^\circ$），" "\n"
        r"这样 $\dfrac12\vec a=\lambda_1\vec u$、$\dfrac13\vec b=\lambda_2\vec v$，目标式与约束都大幅简化；" "\n"
        r"再把 $\vec c$ 也用 $\vec u,\vec v$ 表示，投影条件变成两个系数之和为 $\dfrac43$，" "\n"
        r"于是问题化为「在 $4\lambda_1^2+9\lambda_2^2+6\lambda_1\lambda_2=1$ 下求 $\lambda_1+\lambda_2$ 的最大值」．"
    ),
    'solution': (
        r"设 $\vec u,\vec v$ 分别是与 $\vec a,\vec b$ 同向的单位向量（$\langle\vec u,\vec v\rangle=60^\circ$），" "\n"
        r"令 $\vec a=2\lambda_1\vec u$、$\vec b=3\lambda_2\vec v$（$\lambda_1,\lambda_2>0$），则 $\dfrac12\vec a=\lambda_1\vec u$、$\dfrac13\vec b=\lambda_2\vec v$．" "\n"
        r"由 $\left|\vec a+\vec b\right|=1$：" "\n"
        r"$\left|2\lambda_1\vec u+3\lambda_2\vec v\right|^2=4\lambda_1^2+9\lambda_2^2+2\cdot2\lambda_1\cdot3\lambda_2\cos60^\circ=4\lambda_1^2+9\lambda_2^2+6\lambda_1\lambda_2=1$．" "\n"
        r"设 $\vec c=p\vec u+q\vec v$，则 $\vec c$ 在 $\vec a$ 上的投影为 $\vec c\cdot\vec u=p+\dfrac q2$，" "\n"
        r"在 $\vec b$ 上的投影为 $\vec c\cdot\vec v=\dfrac p2+q$，两者之和为 $\dfrac32\left(p+q\right)=2$，故 $\boxed{p+q=\dfrac43}$．" "\n"
        r"于是" "\n"
        r"$\left|\vec c-\dfrac12\vec a-\dfrac13\vec b\right|=\left|\left(p-\lambda_1\right)\vec u+\left(q-\lambda_2\right)\vec v\right|$，" "\n"
        r"记 $s=p-\lambda_1$、$t=q-\lambda_2$，则 $s+t=\dfrac43-\lambda_1-\lambda_2$，且" "\n"
        r"$\left|s\vec u+t\vec v\right|^2=s^2+t^2+2st\cos60^\circ=s^2+t^2+st=\left(s+t\right)^2-st$．" "\n"
        r"$s+t$ 固定时，$st\le\dfrac{\left(s+t\right)^2}4$（$s=t$ 取等），故" "\n"
        r"$\left|s\vec u+t\vec v\right|^2_{\min}=\left(s+t\right)^2-\dfrac{\left(s+t\right)^2}4=\dfrac34\left(s+t\right)^2=\dfrac34\left(\dfrac43-\lambda_1-\lambda_2\right)^2$．" "\n"
        r"接下来只需**在约束下最大化 $\lambda_1+\lambda_2$**．用拉格朗日乘数法：" "\n"
        r"$L=\lambda_1+\lambda_2-\mu\left(4\lambda_1^2+9\lambda_2^2+6\lambda_1\lambda_2-1\right)$，" "\n"
        r"$\dfrac{\partial L}{\partial\lambda_1}=1-\mu\left(8\lambda_1+6\lambda_2\right)=0$，$\dfrac{\partial L}{\partial\lambda_2}=1-\mu\left(18\lambda_2+6\lambda_1\right)=0$，" "\n"
        r"两式相减得 $2\lambda_1=12\lambda_2$，即 $\lambda_1=6\lambda_2$．" "\n"
        r"代入约束：$\left(4\times36+9+6\times6\right)\lambda_2^2=189\lambda_2^2=1$，得 $\lambda_2=\dfrac1{\sqrt{189}}$、$\lambda_1=\dfrac6{\sqrt{189}}$．" "\n"
        r"故 $\lambda_1+\lambda_2=\dfrac7{\sqrt{189}}=\dfrac7{3\sqrt{21}}=\dfrac{\sqrt{21}}9$，" "\n"
        r"$s+t=\dfrac43-\dfrac{\sqrt{21}}9=\dfrac{12-\sqrt{21}}9$．" "\n"
        r"于是 $\left|\vec c-\dfrac12\vec a-\dfrac13\vec b\right|_{\min}=\dfrac{\sqrt3}2\cdot\dfrac{12-\sqrt{21}}9=\dfrac{12\sqrt3-\sqrt{63}}{18}=\dfrac{12\sqrt3-3\sqrt7}{18}=\boxed{\dfrac{4\sqrt3-\sqrt7}6}$．"
    ),
    'review': (
        r"① ⭐⭐ **换元 $\vec a=2\lambda_1\vec u$、$\vec b=3\lambda_2\vec v$ 是本题的题眼**：" "\n"
        r"   系数 $2,3$ 是照着目标式 $\left|\vec c-\dfrac12\vec a-\dfrac13\vec b\right|$ 里的 $\dfrac12,\dfrac13$ 倒推出来的，" "\n"
        r"   换元后目标式里不再出现分数系数，$\left|\vec a+\vec b\right|=1$ 也变成整系数二次型．" "\n"
        r"② ⭐⭐ **投影之和 ⟹ 系数之和**：$\vec c\cdot\vec u+\vec c\cdot\vec v=\dfrac32(p+q)=2$，" "\n"
        r"   因为 $\vec u,\vec v$ 夹角 $60^\circ$，交叉项各贡献 $\dfrac12$，合起来正好是 $\dfrac32$ 倍．" "\n"
        r"③ ⭐ **$s^2+t^2+st=(s+t)^2-st$ 配 $st\le\dfrac{(s+t)^2}4$**：" "\n"
        r"   这一步把「两个自由量」压成「一个和」，是最值能求出来的关键．" "\n"
        r"④ ⭐ **拉格朗日结果 $\lambda_1=6\lambda_2$ 可自检**：代回约束 $4\times36+9+36=189$ 恰好等于 $189$ ✓" "\n"
        r"⑤ ⚠ **原书答案有根号丢失**：ref_bank 存的是 $\dfrac{4\sqrt3-7}6$，这个值是 $-0.011966<0$，" "\n"
        r"   而所求是一个模长，不可能为负 —— 这就是「算出来矛盾」的警报．" "\n"
        r"   正确答案是 $\dfrac{4\sqrt3-\sqrt7}6$，已按此录入并登记 A 类勘误．" "\n"
        r"⑥ 数值复核：直接数值最小化得 $0.7137417822264296$，而 $\dfrac{4\sqrt3-\sqrt7}6=0.713741986535153$ ✓；" "\n"
        r"   同时数值解出的 $\lambda_1=0.43642197$、$\lambda_2=0.07275335$，" "\n"
        r"   与 $\dfrac6{\sqrt{189}}=0.4364357805$、$\dfrac1{\sqrt{189}}=0.0727392967$ 逐位吻合 ✓" "\n"
        r"**通法（多向量最值）**：" "\n"
        r"① 按目标式里的分数系数倒设换元，把系数化整；" "\n"
        r"② 投影、模长条件都写成系数的二次型；" "\n"
        r"③ 用「和固定 ⟹ 积最大」把一个自由度压掉；" "\n"
        r"④ 剩一个二次型约束，拉格朗日乘数法一步出比例关系．"
    ),
    'difficulty': 0.90,
    'topics': ['M-T-245'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-245-V1',
}

T245_V2 = {
    'type': '填空',
    'stem_text': (
        r"已知平面向量 $\vec a$，$\vec b$，$\vec c$ 满足：$\left|\vec a\right|=\left|\vec b\right|=\left|\vec a+\vec b\right|$，$\left|\vec c\right|=2\left|\vec a-\vec c\right|=2$，则 $\left|\vec b-\vec c\right|$ 的最小值是 ____"
    ),
    'stem': [
        r"已知平面向量 $\vec a$，$\vec b$，$\vec c$ 满足：$\left|\vec a\right|=\left|\vec b\right|=\left|\vec a+\vec b\right|$，$\left|\vec c\right|=2\left|\vec a-\vec c\right|=2$，则 $\left|\vec b-\vec c\right|$ 的最小值是 ____",
    ],
    'opts': [],
    'answer': r"$2\sqrt3-1$",
    'analysis': (
        r"$\left|\vec a\right|=\left|\vec b\right|=\left|\vec a+\vec b\right|$ ⟹ $\langle\vec a,\vec b\rangle=120^\circ$ 且 $\left|\vec a\right|=\left|\vec b\right|$，" "\n"
        r"即 $\vec b$ 由 $\vec a$ 绕原点旋转 $\pm120^\circ$ 得到；" "\n"
        r"又 $\left|\vec c\right|=2$、$\left|\vec a-\vec c\right|=1$ ⟹ $\vec a$ 的终点 $A$ 在以 $C$ 为圆心、$1$ 为半径的圆上．" "\n"
        r"整体旋转即得 $\vec b$ 终点 $B$ 的轨迹圆，所求就是定点 $C$ 到该圆的最小距离．"
    ),
    'solution': (
        r"由 $\left|\vec a\right|=\left|\vec b\right|=\left|\vec a+\vec b\right|$：" "\n"
        r"$\left|\vec a+\vec b\right|^2=\left|\vec a\right|^2+\left|\vec b\right|^2+2\vec a\cdot\vec b=\left|\vec a\right|^2$ 给出 $\vec a\cdot\vec b=-\dfrac12\left|\vec a\right|^2$，" "\n"
        r"结合 $\left|\vec a\right|=\left|\vec b\right|$ 得 $\cos\langle\vec a,\vec b\rangle=-\dfrac12$，即 $\langle\vec a,\vec b\rangle=120^\circ$．" "\n"
        r"因此 $\vec b$ 是 $\vec a$ 绕原点旋转 $\pm120^\circ$ 得到的．" "\n"
        r"设 $\overrightarrow{OC}=\vec c$、$\overrightarrow{OA}=\vec a$、$\overrightarrow{OB}=\vec b$．" "\n"
        r"由 $\left|\vec c\right|=2$ 可取 $C\left(2,0\right)$；由 $\left|\vec a-\vec c\right|=\left|\overrightarrow{CA}\right|=1$ 知" "\n"
        r"$A$ 的轨迹是以 $C$ 为圆心、$1$ 为半径的圆．" "\n"
        r"旋转保持圆的形状，故 $B$ 的轨迹是该圆绕原点旋转 $\pm120^\circ$ 所得的圆：" "\n"
        r"圆心 $C\left(2,0\right)\longrightarrow G\left(2\cos120^\circ,2\sin120^\circ\right)=\left(-1,\sqrt3\right)$，半径仍是 $1$．" "\n"
        r"于是 $\left|\vec b-\vec c\right|=\left|CB\right|$，而 $B$ 在以 $G$ 为圆心、$1$ 为半径的圆上，" "\n"
        r"$\left|GC\right|=\sqrt{\left(2+1\right)^2+\left(0-\sqrt3\right)^2}=\sqrt{9+3}=2\sqrt3>1$（点 $C$ 在圆外），" "\n"
        r"故 $\left|CB\right|_{\min}=\left|GC\right|-1=\boxed{2\sqrt3-1}$．"
    ),
    'review': (
        r"① ⭐⭐ **旋转不变性是本题唯一需要想通的地方**：" "\n"
        r"   $A$ 在一个圆上 ⟹ 绕原点旋转 $\pm120^\circ$ ⟹ $B$ 在「圆心也转了 $\pm120^\circ$、半径不变」的圆上．" "\n"
        r"   不用算 $B$ 的坐标，圆心直接由 $C(2,0)$ 转过去得 $(-1,\sqrt3)$．" "\n"
        r"② ⭐ **$\left|\vec a\right|=\left|\vec b\right|=\left|\vec a+\vec b\right|$ 是一个完整条件组**：" "\n"
        r"   它同时给出「夹角 $120^\circ$」和「模长相等」，缺一个都定不出旋转角．" "\n"
        r"③ ⚠ **题干 $\left|\vec c\right|=2\left|\vec a-\vec c\right|=2$ 是连等式**：$|\vec c|=2$ 且 $2\left|\vec a-\vec c\right|=2$，" "\n"
        r"   即 $\left|\vec a-\vec c\right|=1$，**不是** $\left|\vec a-\vec c\right|=2$．" "\n"
        r"   若按 $2$ 算，轨迹圆半径变 $2$，答案会变成 $2\sqrt3-2$，与原书答案不符 —— 这是还原的硬判据．" "\n"
        r"④ ⭐ **必须验证 $C$ 在圆外**：$\left|GC\right|=2\sqrt3\approx3.464>1$，故最小距离是 $\left|GC\right|-1$ 而不是 $1-\left|GC\right|$．" "\n"
        r"⑤ 数值复核：参数化 $A=(2-\cos\theta,\sin\theta)$，旋转 $\pm120^\circ$ 后取 $\left|B-C\right|$ 的最小值，" "\n"
        r"   数值结果为 $2.4641016151570247$，$2\sqrt3-1=2.4641016151377544$ ✓（两个方向旋转结果一致）" "\n"
        r"**通法（旋转型轨迹）**：" "\n"
        r"① 把「模长 + 和向量模长」条件翻译成「定夹角 + 等模长」⟹ 旋转关系；" "\n"
        r"② 把一个向量的轨迹圆整体旋转，圆心转同一个角、半径不变；" "\n"
        r"③ 所求距离化为「定点到圆的最远距离/最近距离」，用 $\left|GC\right|\mp r$．"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-245'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-245-V2',
}

T245_V3 = {
    'type': '填空',
    'stem_text': (
        r"如图，在边长为 $2$ 的正方形 $ABCD$ 中，$M$，$N$ 分别为边 $BC$，$CD$ 上的动点，以 $MN$ 为边作等边 $\triangle PMN$，使得点 $A$，$P$ 位于直线 $MN$ 的两侧，则 $\overrightarrow{PN}\cdot\overrightarrow{PB}$ 的最小值为 ____"
    ),
    'stem': [
        r"如图，在边长为 $2$ 的正方形 $ABCD$ 中，$M$，$N$ 分别为边 $BC$，$CD$ 上的动点，以 $MN$ 为边作等边 $\triangle PMN$，使得点 $A$，$P$ 位于直线 $MN$ 的两侧，则 $\overrightarrow{PN}\cdot\overrightarrow{PB}$ 的最小值为 ____",
    ],
    'opts': [],
    'answer': r"$-\dfrac14$",
    'analysis': (
        r"取 $BN$ 中点 $E$，由极化恒等式 $\overrightarrow{PN}\cdot\overrightarrow{PB}=\left|PE\right|^2-\left|BE\right|^2$；" "\n"
        r"$\left|BE\right|$ 由 $\mathrm{Rt}\triangle BCN$ 的勾股定理直接得，$\left|PE\right|$ 在 $\triangle PEF$ 中用余弦定理算" "\n"
        r"（$F$ 为 $MN$ 中点，$EF$ 是 $\triangle BMN$ 的中位线）；最后化成关于两个动点参数的二次函数求最值．" "\n"
        r"关键一步是 $\angle PFE$ 的余弦：$PF\perp MN$ 而 $\angle EFM$ 与 $\angle CMN$ 互补，故 $\cos\angle PFE=-\sin\angle CMN=-\dfrac b{\sqrt{a^2+b^2}}$．"
    ),
    'solution': (
        r"建立坐标系：$A\left(0,0\right)$、$B\left(2,0\right)$、$C\left(2,2\right)$、$D\left(0,2\right)$．" "\n"
        r"设 $CM=a$、$CN=b$（$0\le a\le2$，$0\le b\le2$），则 $M\left(2,2-a\right)$、$N\left(2-b,2\right)$，" "\n"
        r"$\left|MN\right|=\sqrt{a^2+b^2}$．" "\n"
        r"连接 $BN$，设 $BN$ 的中点为 $E$、$MN$ 的中点为 $F$，连接 $PE$、$PF$、$EF$．" "\n"
        r"由极化恒等式（$E$ 是 $BN$ 中点，$\overrightarrow{PN}=\overrightarrow{PE}+\overrightarrow{EN}$、$\overrightarrow{PB}=\overrightarrow{PE}-\overrightarrow{EN}$）：" "\n"
        r"$\overrightarrow{PN}\cdot\overrightarrow{PB}=\left|PE\right|^2-\left|EN\right|^2=\left|PE\right|^2-\left|BE\right|^2$．" "\n"
        r"**求 $\left|BE\right|$**：在 $\mathrm{Rt}\triangle BCN$ 中 $BN^2=BC^2+CN^2=4+b^2$，" "\n"
        r"故 $\left|BE\right|^2=\dfrac{BN^2}4=1+\dfrac{b^2}4$．" "\n"
        r"**求 $\left|PE\right|$**：$EF$ 是 $\triangle BMN$ 的中位线，故 $EF\parallel BM$ 且 $EF=\dfrac12BM=\dfrac{2-a}2=1-\dfrac a2$；" "\n"
        r"在等边 $\triangle PMN$ 中 $PF\perp MN$ 且 $PF=\dfrac{\sqrt3}2\left|MN\right|=\dfrac{\sqrt3}2\sqrt{a^2+b^2}$．" "\n"
        r"由 $EF\parallel BM\parallel MC$ 得 $\angle EFM$ 与 $\angle CMN$ 互补，故 $\sin\angle EFM=\sin\angle CMN$．" "\n"
        r"在 $\mathrm{Rt}\triangle CMN$ 中 $\sin\angle CMN=\dfrac{CN}{MN}=\dfrac b{\sqrt{a^2+b^2}}$，" "\n"
        r"又 $PF\perp MN$ 且 $PF$ 与 $FE$ 分处 $MN$ 两侧，故 $\cos\angle PFE=-\sin\angle EFM=-\dfrac b{\sqrt{a^2+b^2}}$．" "\n"
        r"在 $\triangle PEF$ 中由余弦定理：" "\n"
        r"$\left|PE\right|^2=EF^2+PF^2-2\cdot EF\cdot PF\cdot\cos\angle PFE$" "\n"
        r"$=\left(1-\dfrac a2\right)^2+\dfrac34\left(a^2+b^2\right)+2\left(1-\dfrac a2\right)\cdot\dfrac{\sqrt3}2\sqrt{a^2+b^2}\cdot\dfrac b{\sqrt{a^2+b^2}}$" "\n"
        r"$=\left(1-\dfrac a2\right)^2+\dfrac34\left(a^2+b^2\right)+\sqrt3\left(1-\dfrac a2\right)b$．" "\n"
        r"（注意最后一项里 $\sqrt{a^2+b^2}$ 已被约掉，只剩 $b$．）" "\n"
        r"于是 $\overrightarrow{PN}\cdot\overrightarrow{PB}=\left|PE\right|^2-\left|BE\right|^2$" "\n"
        r"$=\left(1-\dfrac a2\right)^2+\dfrac34\left(a^2+b^2\right)+\sqrt3\left(1-\dfrac a2\right)b-1-\dfrac{b^2}4$" "\n"
        r"$=\left(1-a+\dfrac{a^2}4\right)+\dfrac34a^2+\dfrac34b^2+\sqrt3\left(1-\dfrac a2\right)b-1-\dfrac{b^2}4$" "\n"
        r"$=\boxed{a^2-a+\dfrac{b^2}2+\sqrt3\left(1-\dfrac a2\right)b}=:f\left(a,b\right)$．" "\n"
        r"**求最小值**：$\dfrac{\partial f}{\partial b}=b+\sqrt3\left(1-\dfrac a2\right)$．" "\n"
        r"由 $0\le a\le2$ 得 $1-\dfrac a2\ge0$，故对 $b\in\left[0,2\right]$ 恒有 $\dfrac{\partial f}{\partial b}\ge0$，" "\n"
        r"即 $f$ 关于 $b$ 单调递增，最小值在 $\boxed{b=0}$ 处取得（此时 $N$ 与 $C$ 重合）．" "\n"
        r"$f\left(a,0\right)=a^2-a$，在 $a\in\left[0,2\right]$ 上的最小值于 $a=\dfrac12$ 处取得：" "\n"
        r"$f\left(\dfrac12,0\right)=\dfrac14-\dfrac12=\boxed{-\dfrac14}$．" "\n"
        r"（$a=\dfrac12$ 表示 $M$ 在 $BC$ 上、距 $C$ 为 $\dfrac12$，构型存在；" "\n"
        r"$b=0$ 时 $\triangle CMN$ 退化，但上述表达式按极限理解依然成立，见 review ③．）"
    ),
    'review': (
        r"① ⭐⭐ **极化恒等式 $\overrightarrow{PN}\cdot\overrightarrow{PB}=\left|PE\right|^2-\left|BE\right|^2$（$E$ 为 $BN$ 中点）**：" "\n"
        r"   凡「一动点与两定点的数量积」，取两定点连线的中点化成平方差，" "\n"
        r"   比直接设 $P$ 坐标算快得多，而且 $P$ 的自由度被吸收进 $\left|PE\right|$．" "\n"
        r"② ⭐⭐ **$F$ 取 $MN$ 中点、$EF$ 是 $\triangle BMN$ 的中位线**：" "\n"
        r"   $EF=\dfrac12BM=1-\dfrac a2$ 且 $EF\parallel BM$；又 $B,M,C$ 共线，故 $EF\parallel MC$．" "\n"
        r"   于是 $\angle EFM$ 与 $\angle CMN$ **互补**，两者正弦相等：$\sin\angle EFM=\dfrac b{\sqrt{a^2+b^2}}$．" "\n"
        r"③ ⚠ **$\cos\angle PFE=-\sin\angle EFM$ 里的 $\sqrt{a^2+b^2}$ 会被约掉**：" "\n"
        r"   $-2\cdot EF\cdot PF\cdot\cos\angle PFE=2\left(1-\dfrac a2\right)\cdot\dfrac{\sqrt3}2\sqrt{a^2+b^2}\cdot\dfrac b{\sqrt{a^2+b^2}}=\sqrt3\left(1-\dfrac a2\right)b$．" "\n"
        r"   我第一遍推导时误把分子写成 $BN=\sqrt{4+b^2}$，得到 $f(a,0)=a^2-a+2\sqrt3-\sqrt3a$（最小值约 $1.598$），" "\n"
        r"   与答案 $-\dfrac14$ 矛盾 —— 正是这个矛盾逼我回头查出了错处．**「算出来矛盾」是最可靠的警报**．" "\n"
        r"④ ⭐ **最值落在边界 $b=0$（$N$ 与 $C$ 重合）**：由 $\dfrac{\partial f}{\partial b}=b+\sqrt3\left(1-\dfrac a2\right)\ge0$ 直接判定，" "\n"
        r"   不需要讨论内点．原书也注明「当 $N$ 与 $C$ 重合时 $\triangle BCN$、$\triangle CMN$、$\triangle PEF$ 不存在，" "\n"
        r"   但可验证上述等式依然成立」—— 即把它理解为 $b\to0^+$ 的极限．" "\n"
        r"⑤ 数值复核（双重）：" "\n"
        r"   （a）解析式 $f(a,b)=a^2-a+\dfrac{b^2}2+\sqrt3\left(1-\dfrac a2\right)b$ 与**直接构型计算**逐点比对：" "\n"
        r"       $(a,b)=(0.5,0)$ 两者都是 $-0.250000000$；$(0.5,1)$ 都是 $1.549038106$；" "\n"
        r"       $(1.2,0.7)$ 都是 $0.969974226$；$(0,2)$ 都是 $5.464101615$；$(2,2)$ 都是 $4.000000000$ ✓" "\n"
        r"   （b）对 $a,b\in[0,2]$ 做 $801\times801$ 网格穷举，$f$ 的最小值 $=-0.25$，在 $(0.5,0)$ 处取到 ✓" "\n"
        r"**通法（含等边三角形的数量积最值）**：" "\n"
        r"① 两定点连线的中点 ⟹ 极化恒等式，数量积变平方差；" "\n"
        r"② 等边三角形取底边中点，高 $=\dfrac{\sqrt3}2\times$ 边长且垂直；" "\n"
        r"③ 中位线转移角，把未知角换成直角三角形的已知角（注意可能是**互补**而非相等）；" "\n"
        r"④ 余弦定理代入后先检查有没有可约的公因子（本题 $\sqrt{a^2+b^2}$ 恰好约净）；" "\n"
        r"⑤ 得到二元函数后先求偏导判单调，往往一个变量直接取边界，剩一元二次函数配方即可．"
    ),
    'difficulty': 0.90,
    'topics': ['M-T-245'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-245-V3',
}

T187_E1 = {
    'type': '填空',
    'stem_text': (
        r"已知平面向量 $\vec a$，$\vec b$，$\vec c$，$\left|\vec a\right|=2$，$\left|\vec b\right|=3$，$\left|\vec c\right|=4$，$\vec a\cdot\vec b=\dfrac32$，则 $\left|\vec a\cdot\vec c\right|+\left|\vec b\cdot\vec c\right|$ 的最大值是 ____，最小值是 ____"
    ),
    'stem': [
        r"已知平面向量 $\vec a$，$\vec b$，$\vec c$，$\left|\vec a\right|=2$，$\left|\vec b\right|=3$，$\left|\vec c\right|=4$，$\vec a\cdot\vec b=\dfrac32$，则 $\left|\vec a\cdot\vec c\right|+\left|\vec b\cdot\vec c\right|$ 的最大值是 ____，最小值是 ____",
    ],
    'opts': [],
    'answer': r"$16$；$2\sqrt{15}$",
    'analysis': (
        r"$\left|\vec c\right|=4$ 说明 $\vec c$ 的终点在半径为 $4$ 的圆上，用圆的参数方程 $\vec c=\left(4\cos\theta,4\sin\theta\right)$；" "\n"
        r"由 $\vec a\cdot\vec b=\dfrac32$ 得 $\cos\langle\vec a,\vec b\rangle=\dfrac14$．" "\n"
        r"因为外层有绝对值，必须按 $\vec c$ 在 $\vec a,\vec b$ 上投影的正负分三段，分界线是 $\vec c\perp\vec a$ 与 $\vec c\perp\vec b$．"
    ),
    'solution': (
        r"取 $\vec a=\left(2,0\right)$、$\vec c=\left(4\cos\theta,4\sin\theta\right)$，设 $\langle\vec a,\vec b\rangle=\alpha$，" "\n"
        r"则 $\cos\alpha=\dfrac{\vec a\cdot\vec b}{\left|\vec a\right|\left|\vec b\right|}=\dfrac{3/2}{6}=\dfrac14$，$\sin\alpha=\dfrac{\sqrt{15}}4$．" "\n"
        r"$\vec b=\left(3\cos\alpha,3\sin\alpha\right)$，于是" "\n"
        r"$\vec a\cdot\vec c=8\cos\theta$，$\vec b\cdot\vec c=12\cos\left(\alpha-\theta\right)=12\left(\cos\alpha\cos\theta+\sin\alpha\sin\theta\right)=3\cos\theta+3\sqrt{15}\sin\theta$．" "\n"
        r"记 $F\left(\theta\right)=\left|8\cos\theta\right|+\left|3\cos\theta+3\sqrt{15}\sin\theta\right|$．" "\n"
        r"注意 $F\left(\theta+\pi\right)=F\left(\theta\right)$，故只需讨论 $\theta\in\left[0^\circ,180^\circ\right]$，" "\n"
        r"分界线为 $\vec c\perp\vec a$（$\theta=90^\circ$）与 $\vec c\perp\vec b$（$\theta=90^\circ+\alpha$）．" "\n"
        r"**① $0^\circ\le\theta\le90^\circ$（两个投影均非负）**" "\n"
        r"$F=11\cos\theta+3\sqrt{15}\sin\theta=16\sin\left(\theta+\varphi\right)$，$\sin\varphi=\dfrac{11}{16}$、$\cos\varphi=\dfrac{3\sqrt{15}}{16}$．" "\n"
        r"由 $\sin^2\varphi=\dfrac{121}{256}<\dfrac12=\sin^245^\circ$ 知 $0^\circ<\varphi<45^\circ$．" "\n"
        r"$\theta+\varphi\in\left[\varphi,90^\circ+\varphi\right]\subset\left(0^\circ,135^\circ\right)$，故 $\sin\left(\theta+\varphi\right)\in\left[\dfrac{11}{16},1\right]$，" "\n"
        r"$F\in\left[11,16\right]$．" "\n"
        r"**② $90^\circ<\theta\le90^\circ+\alpha$（与 $\vec a$ 的投影为负、与 $\vec b$ 的投影为正）**" "\n"
        r"$F=-8\cos\theta+3\cos\theta+3\sqrt{15}\sin\theta=-5\cos\theta+3\sqrt{15}\sin\theta=4\sqrt{10}\sin\left(\theta-\beta\right)$，" "\n"
        r"$\sin\beta=-\dfrac{\sqrt{10}}8$、$\cos\beta=\dfrac{3\sqrt6}8$（$\beta$ 在第四象限，$-45^\circ<\beta<0^\circ$）．" "\n"
        r"$\theta-\beta\in\left(90^\circ-\beta,\ 90^\circ-\beta+\alpha\right]\subset\left(90^\circ,225^\circ\right)$，$F$ 在该区间递减，" "\n"
        r"$F_{\min}=4\sqrt{10}\sin\left(90^\circ-\beta+\alpha\right)=4\sqrt{10}\cos\left(\alpha-\beta\right)$" "\n"
        r"$=4\sqrt{10}\left(\dfrac14\cdot\dfrac{3\sqrt6}8+\dfrac{\sqrt{15}}4\cdot\dfrac{\sqrt{10}}8\right)=4\sqrt{10}\cdot\dfrac{3\sqrt6+5\sqrt6}{32}=4\sqrt{10}\cdot\dfrac{8\sqrt6}{32}=\sqrt{60}=2\sqrt{15}$，" "\n"
        r"$F_{\max}=4\sqrt{10}\cos\beta=4\sqrt{10}\cdot\dfrac{3\sqrt6}8=3\sqrt{15}$．" "\n"
        r"**③ $90^\circ+\alpha<\theta\le180^\circ$（两个投影均为负）**" "\n"
        r"$F=-11\cos\theta-3\sqrt{15}\sin\theta=-16\sin\left(\theta+\varphi\right)$．" "\n"
        r"$\theta+\varphi\in\left(90^\circ+\alpha+\varphi,\ 180^\circ+\varphi\right]\subset\left(90^\circ,225^\circ\right)$，$F$ 递减，" "\n"
        r"$F_{\min}=-16\sin\left(180^\circ+\varphi\right)=16\sin\varphi=11$，" "\n"
        r"$F_{\max}=-16\sin\left(90^\circ+\alpha+\varphi\right)=-16\cos\left(\alpha+\varphi\right)$" "\n"
        r"$=-16\left(\dfrac14\cdot\dfrac{3\sqrt{15}}{16}-\dfrac{\sqrt{15}}4\cdot\dfrac{11}{16}\right)=-16\cdot\dfrac{3\sqrt{15}-11\sqrt{15}}{64}=2\sqrt{15}$．" "\n"
        r"**汇总**：三段的最大值依次为 $16$、$3\sqrt{15}$、$2\sqrt{15}$，最小值依次为 $11$、$2\sqrt{15}$、$11$．" "\n"
        r"故全局最大值为 $\boxed{16}$，全局最小值为 $\boxed{2\sqrt{15}}$．"
    ),
    'review': (
        r"① ⭐⭐ **题干必须带绝对值**：ref_bank 提取时把 $\left|\vec a\cdot\vec c\right|+\left|\vec b\cdot\vec c\right|$ 的绝对值号丢了，" "\n"
        r"   只剩「$\vec a\cdot\vec c+\vec b\cdot\vec c$」．**数值对拍证实绝对值不可省**：" "\n"
        r"   带绝对值时 $\max=16$、$\min=7.745967=2\sqrt{15}$；" "\n"
        r"   不带绝对值时 $\vec a\cdot\vec c+\vec b\cdot\vec c=11\cos\theta+3\sqrt{15}\sin\theta$，最小值是 $-16$ 而非 $2\sqrt{15}$．" "\n"
        r"   按 $原件/按页还原/p149.txt$ 的原文（含【分析】里的写法）确认为带绝对值，已按此录入．" "\n"
        r"② ⭐⭐ **分界线是「$\vec c\perp\vec a$」与「$\vec c\perp\vec b$」**：" "\n"
        r"   绝对值拆段的关键就是找里层变号的位置，共两条分界线 ⟹ 三段，不多不少．" "\n"
        r"③ ⭐ **$F\left(\theta+\pi\right)=F\left(\theta\right)$ 省一半讨论**：两个绝对值同时变号，和不变．" "\n"
        r"④ ⭐ **辅助角后要先定 $\varphi$ 的范围**：由 $\sin^2\varphi=\dfrac{121}{256}<\dfrac12$ 得 $0^\circ<\varphi<45^\circ$，" "\n"
        r"   进而 $\theta+\varphi$ 的区间落在 $\left(0^\circ,135^\circ\right)$，才能判断 $\sin$ 的单调性并取到 $1$．" "\n"
        r"⑤ ⭐ **第②段的 $F_{\min}=2\sqrt{15}$ 就是全局最小值**：第①③段的最小值都是 $11>2\sqrt{15}\approx7.746$．" "\n"
        r"⑥ 数值复核：对 $\theta\in[0,2\pi)$ 取 $2\times10^6$ 个点，" "\n"
        r"   $\max=15.999999999998662\approx16$ ✓，$\min=7.745978528197\approx2\sqrt{15}=7.745966692$ ✓" "\n"
        r"⑦ 注：M-T-187-V1 与本 E1 是同一道题（p150 第 37 题与 p149 例 1 逐字相同），" "\n"
        r"   只在 ref_bank 里重复收录，本批只录 E1，V1 记为重复不录．" "\n"
        r"**通法（模定值的向量用圆的参数方程）**：" "\n"
        r"① $\left|\vec c\right|=R$ ⟹ $\vec c=\left(R\cos\theta,R\sin\theta\right)$，把向量问题变成三角函数问题；" "\n"
        r"② 外层有绝对值时，按每个里层的零点分段；" "\n"
        r"③ 每段都是 $A\cos\theta+B\sin\theta$，用辅助角 + 区间单调性取最值；" "\n"
        r"④ 各段最值再取全局 max / min．"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-187'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-187-E1',
}

T287_E1 = {
    'type': '填空',
    'stem_text': (
        r"如图，在正方体 $ABCD-A_1B_1C_1D_1$ 中，$AB=4$，$E$ 为棱 $BC$ 的中点，$F$ 为棱 $A_1D_1$ 的四等分点（靠近点 $D_1$），过点 $A$，$E$，$F$ 作该正方体的截面，则该截面的周长是 ____"
    ),
    'stem': [
        r"如图，在正方体 $ABCD-A_1B_1C_1D_1$ 中，$AB=4$，$E$ 为棱 $BC$ 的中点，$F$ 为棱 $A_1D_1$ 的四等分点（靠近点 $D_1$），过点 $A$，$E$，$F$ 作该正方体的截面，则该截面的周长是 ____",
    ],
    'opts': [],
    'answer': r"$\dfrac{9\sqrt5+25+2\sqrt{13}}3$",
    'analysis': (
        r"建系写出过 $A,E,F$ 的平面方程，再逐条棱代入求交点，交点数即边数；" "\n"
        r"本题得到五个交点（五边形 $AEGHF$），逐段用距离公式求边长后相加．"
    ),
    'solution': (
        r"以 $A$ 为原点建系：$A\left(0,0,0\right)$、$B\left(4,0,0\right)$、$C\left(4,4,0\right)$、$D\left(0,4,0\right)$、" "\n"
        r"$A_1\left(0,0,4\right)$、$B_1\left(4,0,4\right)$、$C_1\left(4,4,4\right)$、$D_1\left(0,4,4\right)$．" "\n"
        r"则 $E\left(4,2,0\right)$（$BC$ 中点），$F\left(0,3,4\right)$（$A_1D_1$ 上靠近 $D_1$ 的四等分点，$A_1F=3$、$FD_1=1$）．" "\n"
        r"平面 $AEF$ 的法向量 $\vec n=\overrightarrow{AE}\times\overrightarrow{AF}=\left(4,2,0\right)\times\left(0,3,4\right)=\left(8,-16,12\right)\parallel\left(2,-4,3\right)$，" "\n"
        r"平面方程为 $2x-4y+3z=0$．" "\n"
        r"逐棱代入求交点（坐标限制在 $[0,4]$ 内才有效）：" "\n"
        r"· $AB\ (x,0,0)$：$2x=0\Rightarrow x=0$，得 $A\left(0,0,0\right)$；" "\n"
        r"· $BC\ (4,y,0)$：$8-4y=0\Rightarrow y=2$，得 $E\left(4,2,0\right)$；" "\n"
        r"· $CC_1\ (4,4,z)$：$8-16+3z=0\Rightarrow z=\dfrac83$，得 $G\left(4,4,\dfrac83\right)$；" "\n"
        r"· $C_1D_1\ (x,4,4)$：$2x-16+12=0\Rightarrow x=2$，得 $H\left(2,4,4\right)$；" "\n"
        r"· $D_1A_1\ (0,y,4)$：$-4y+12=0\Rightarrow y=3$，得 $F\left(0,3,4\right)$；" "\n"
        r"其余七条棱（$CD$、$DA$、$A_1B_1$、$B_1C_1$、$AA_1$、$BB_1$、$DD_1$）解出的参数均超出 $[0,4]$，无交点．" "\n"
        r"故截面为五边形 $AEGHF$．逐段求边长：" "\n"
        r"$\left|AE\right|=\sqrt{16+4}=2\sqrt5$；" "\n"
        r"$\left|EG\right|=\sqrt{0+4+\dfrac{64}9}=\sqrt{\dfrac{100}9}=\dfrac{10}3$；" "\n"
        r"$\left|GH\right|=\sqrt{4+0+\left(4-\dfrac83\right)^2}=\sqrt{4+\dfrac{16}9}=\dfrac{2\sqrt{13}}3$；" "\n"
        r"$\left|HF\right|=\sqrt{4+1+0}=\sqrt5$；" "\n"
        r"$\left|FA\right|=\sqrt{0+9+16}=5$．" "\n"
        r"周长 $=2\sqrt5+\dfrac{10}3+\dfrac{2\sqrt{13}}3+\sqrt5+5=3\sqrt5+\dfrac{25}3+\dfrac{2\sqrt{13}}3=\boxed{\dfrac{9\sqrt5+25+2\sqrt{13}}3}$．"
    ),
    'review': (
        r"① ⭐⭐ **「写平面方程 + 逐棱代入」是求截面最稳的办法**：" "\n"
        r"   12 条棱一棱不漏地代进去，解出的参数在 $[0,4]$ 内才算交点；交点数 = 边数，顺带排出顶点顺序．" "\n"
        r"   比「延长线找交点 + 相似比」严谨，也不依赖图形直觉．" "\n"
        r"② ⚠ **$F$ 是 $A_1D_1$ 的四等分点且靠近 $D_1$**：故 $A_1F=3$、$FD_1=1$，坐标是 $\left(0,3,4\right)$ 而不是 $\left(0,1,4\right)$．" "\n"
        r"   取反会得到完全不同的截面．" "\n"
        r"③ ⭐ **$\left|FA\right|=5$ 是一个好用的自检**：$F\left(0,3,4\right)$ 在侧面 $AA_1D_1D$ 内，$\left|FA\right|=\sqrt{3^2+4^2}=5$ 恰好是勾股数．" "\n"
        r"④ ⚠ **周长的三个部分要分别算对**：$\left|EG\right|=\dfrac{10}3$ 与 $\left|GH\right|=\dfrac{2\sqrt{13}}3$ 都带分母 $3$，" "\n"
        r"   最后通分时 $3\sqrt5=\dfrac{9\sqrt5}3$、$5=\dfrac{15}3$，与 $\dfrac{10}3$ 合并得 $\dfrac{25}3$ ——" "\n"
        r"   **这个 $25$ 不是 $2\sqrt5$，原书 OCR 里「9 5 + 25 + 2 13」的 $25$ 是整数**．" "\n"
        r"⑤ 数值复核：五段边长依次为 $4.472135955$、$3.333333333$、$2.403700850$、$2.236067977$、$5.0$，" "\n"
        r"   合计 $17.44523811614203$，而 $\dfrac{9\sqrt5+25+2\sqrt{13}}3=17.445238116142026$ ✓ 完全吻合" "\n"
        r"**通法（截面周长）**：" "\n"
        r"① 建系写平面方程（三点定平面，法向量叉乘后取最简整数比）；" "\n"
        r"② 12 条棱逐一代入，参数在范围内才算交点；" "\n"
        r"③ 交点按空间顺序连成多边形，逐段用距离公式；" "\n"
        r"④ 最后通分合并同类项，注意整数项与带根号项不能混．"
    ),
    'difficulty': 0.80,
    'topics': ['M-T-287'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-287-E1',
}

T287_V2 = {
    'type': '填空',
    'stem_text': (
        r"已知在棱长为 $6$ 的正方体 $ABCD-A_1B_1C_1D_1$ 中，点 $E$，$F$ 分别是棱 $C_1D_1$，$B_1C_1$ 的中点，过 $A$，$E$，$F$ 三点作该正方体的截面，则截面的周长为 ____"
    ),
    'stem': [
        r"已知在棱长为 $6$ 的正方体 $ABCD-A_1B_1C_1D_1$ 中，点 $E$，$F$ 分别是棱 $C_1D_1$，$B_1C_1$ 的中点，过 $A$，$E$，$F$ 三点作该正方体的截面，则截面的周长为 ____",
    ],
    'opts': [],
    'answer': r"$6\sqrt{13}+3\sqrt2$",
    'analysis': (
        r"同 E1 的做法：写平面方程后逐棱求交点，得五边形 $AHFEG$，逐段求边长．" "\n"
        r"本题的数据更整齐——由中位线定理直接得 $EF=3\sqrt2$，由勾股定理得 $\left|AH\right|=\left|AG\right|=2\sqrt{13}$、$\left|HF\right|=\left|EG\right|=\sqrt{13}$．"
    ),
    'solution': (
        r"以 $A$ 为原点建系：$A\left(0,0,0\right)$、$B\left(6,0,0\right)$、$C\left(6,6,0\right)$、$D\left(0,6,0\right)$、" "\n"
        r"$A_1\left(0,0,6\right)$、$B_1\left(6,0,6\right)$、$C_1\left(6,6,6\right)$、$D_1\left(0,6,6\right)$．" "\n"
        r"$E$ 为 $C_1D_1$ 中点 ⟹ $E\left(3,6,6\right)$；$F$ 为 $B_1C_1$ 中点 ⟹ $F\left(6,3,6\right)$．" "\n"
        r"法向量 $\vec n=\overrightarrow{AE}\times\overrightarrow{AF}=\left(3,6,6\right)\times\left(6,3,6\right)=\left(18,18,-27\right)\parallel\left(2,2,-3\right)$，" "\n"
        r"平面方程为 $2x+2y-3z=0$．" "\n"
        r"逐棱代入：" "\n"
        r"· $AB\ (x,0,0)$：$x=0$，得 $A$；· $BB_1\ (6,0,z)$：$12-3z=0\Rightarrow z=4$，得 $H\left(6,0,4\right)$；" "\n"
        r"· $B_1C_1\ (6,y,6)$：$12+2y-18=0\Rightarrow y=3$，得 $F$；" "\n"
        r"· $C_1D_1\ (x,6,6)$：$2x+12-18=0\Rightarrow x=3$，得 $E$；" "\n"
        r"· $DD_1\ (0,6,z)$：$12-3z=0\Rightarrow z=4$，得 $G\left(0,6,4\right)$；" "\n"
        r"其余七条棱无有效交点．故截面为五边形 $AHFEG$．" "\n"
        r"逐段求边长：" "\n"
        r"$\left|AH\right|=\sqrt{36+16}=2\sqrt{13}$；$\left|HF\right|=\sqrt{0+9+4}=\sqrt{13}$；" "\n"
        r"$\left|FE\right|=\sqrt{9+9+0}=3\sqrt2$；$\left|EG\right|=\sqrt{9+0+4}=\sqrt{13}$；$\left|GA\right|=\sqrt{0+36+16}=2\sqrt{13}$．" "\n"
        r"周长 $=2\sqrt{13}+\sqrt{13}+3\sqrt2+\sqrt{13}+2\sqrt{13}=\boxed{6\sqrt{13}+3\sqrt2}$．"
    ),
    'review': (
        r"① ⭐⭐ **与 E1 完全同法**：写平面方程 $2x+2y-3z=0$ 后逐棱代入，五条棱有交点 ⟹ 五边形 $AHFEG$．" "\n"
        r"② ⭐ **对称性省一半计算**：平面方程关于 $x,y$ 对称（$E,F$ 关于平面 $x=y$ 对称），" "\n"
        r"   故 $\left|AH\right|=\left|AG\right|$、$\left|HF\right|=\left|EG\right|$，只需算两段．" "\n"
        r"③ ⭐ **$\left|FE\right|=3\sqrt2$ 可用中位线定理直接看**：$E,F$ 分别是 $C_1D_1$、$B_1C_1$ 中点，" "\n"
        r"   故 $EF$ 是 $\triangle C_1D_1B_1$ 的中位线，$EF=\dfrac12D_1B_1=\dfrac12\times6\sqrt2=3\sqrt2$ ✓" "\n"
        r"④ ⚠ **别把 $\left|AH\right|$ 算成 $\sqrt{36+16}=\sqrt{52}$ 之后忘记化简**：$\sqrt{52}=2\sqrt{13}$，两项合并才得 $6\sqrt{13}$．" "\n"
        r"⑤ 数值复核：$2\sqrt{13}=7.211102551$、$\sqrt{13}=3.605551275$、$3\sqrt2=4.242640687$，" "\n"
        r"   五段合计 $25.875948339903218$，而 $6\sqrt{13}+3\sqrt2=25.875948339903218$ ✓ 逐位相同" "\n"
        r"**通法（截面周长）**：见 M-T-287-E1 的 review；" "\n"
        r"另外，若平面方程关于某两个坐标对称，可直接断言对应边相等，省一半计算．"
    ),
    'difficulty': 0.75,
    'topics': ['M-T-287'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-287-V2',
}

T287_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知直三棱柱 $ABC-A_1B_1C_1$ 的侧棱长为 $2$，$AB\perp BC$，$AB=BC=2$．过 $AB$、$BB_1$ 的中点 $E$、$F$ 作平面 $\alpha$ 与平面 $AA_1C_1C$ 垂直，则所得截面周长为（　　）"
    ),
    'stem': [
        r"已知直三棱柱 $ABC-A_1B_1C_1$ 的侧棱长为 $2$，$AB\perp BC$，$AB=BC=2$．过 $AB$、$BB_1$ 的中点 $E$、$F$ 作平面 $\alpha$ 与平面 $AA_1C_1C$ 垂直，则所得截面周长为（　　）",
    ],
    'opts': [
        ('A', r"$2\sqrt2+\sqrt6$"),
        ('B', r"$2+2\sqrt6$"),
        ('C', r"$3\sqrt2+\sqrt6$"),
        ('D', r"$3\sqrt2+2\sqrt6$"),
    ],
    'answer': 'C',
    'analysis': (
        r"先定平面 $\alpha$：$\alpha$ 过 $E,F$，故其法向量垂直于 $\overrightarrow{EF}$；" "\n"
        r"又 $\alpha\perp$ 平面 $AA_1C_1C$，故其法向量垂直于平面 $AA_1C_1C$ 的法向量．" "\n"
        r"两个垂直条件联立即可定出 $\alpha$，再逐棱求交点得五边形，逐段求边长．"
    ),
    'solution': (
        r"以 $B$ 为原点建系：$B\left(0,0,0\right)$、$A\left(2,0,0\right)$、$C\left(0,2,0\right)$（由 $AB\perp BC$、$AB=BC=2$），" "\n"
        r"$A_1\left(2,0,2\right)$、$B_1\left(0,0,2\right)$、$C_1\left(0,2,2\right)$（侧棱长 $2$）．" "\n"
        r"$E$ 为 $AB$ 中点 ⟹ $E\left(1,0,0\right)$；$F$ 为 $BB_1$ 中点 ⟹ $F\left(0,0,1\right)$．" "\n"
        r"**定平面 $\alpha$**：设其法向量为 $\vec n=\left(p,q,r\right)$．" "\n"
        r"由 $E,F\in\alpha$：$\vec n\cdot\overrightarrow{EF}=0$，$\overrightarrow{EF}=\left(-1,0,1\right)$，得 $-p+r=0$，即 $r=p$．" "\n"
        r"平面 $AA_1C_1C$ 过 $A\left(2,0,0\right)$、$C\left(0,2,0\right)$ 且含竖直方向，方程为 $x+y=2$，法向量 $\vec m=\left(1,1,0\right)$．" "\n"
        r"由 $\alpha\perp$ 平面 $AA_1C_1C$：$\vec n\cdot\vec m=0$，得 $p+q=0$，即 $q=-p$．" "\n"
        r"取 $p=1$ 得 $\vec n=\left(1,-1,1\right)$，平面 $\alpha$ 过 $E\left(1,0,0\right)$，方程为 $\boxed{x-y+z=1}$．" "\n"
        r"**逐棱求交点**（棱柱 $=\{(x,y,z):x\ge0,y\ge0,x+y\le2,0\le z\le2\}$）：" "\n"
        r"· 底面 $z=0$：$x-y=1$，与 $x+y\le2$ 联立得线段 $ED$，其中 $D\left(\dfrac32,\dfrac12,0\right)$ 在 $AC$ 上；" "\n"
        r"· 侧面 $ABB_1A_1\ (y=0)$：$x+z=1$，得线段 $EF$；" "\n"
        r"· 侧面 $BCC_1B_1\ (x=0)$：$-y+z=1$，得 $FI$，其中 $I\left(0,1,2\right)$ 在 $B_1C_1$ 上；" "\n"
        r"· 顶面 $z=2$：$x-y=-1$，即 $y=x+1$，得 $IH$，其中 $H\left(\dfrac12,\dfrac32,2\right)$ 在 $A_1C_1$ 上；" "\n"
        r"· 侧面 $ACC_1A_1\ (x+y=2)$：$z=3-2x$，得 $HD$．" "\n"
        r"故截面为五边形 $DEF IH$（顶点 $D,E,F,I,H$）．逐段求边长：" "\n"
        r"$\left|DE\right|=\sqrt{\dfrac14+\dfrac14}=\dfrac{\sqrt2}2$；$\left|EF\right|=\sqrt{1+1}=\sqrt2$；" "\n"
        r"$\left|FI\right|=\sqrt{0+1+1}=\sqrt2$；$\left|IH\right|=\sqrt{\dfrac14+\dfrac14}=\dfrac{\sqrt2}2$；" "\n"
        r"$\left|HD\right|=\sqrt{1+1+4}=\sqrt6$．" "\n"
        r"周长 $=\dfrac{\sqrt2}2+\sqrt2+\sqrt2+\dfrac{\sqrt2}2+\sqrt6=3\sqrt2+\sqrt6$，故选 $\boxed{\mathrm C}$．"
    ),
    'review': (
        r"① ⭐⭐ **两个垂直条件定平面**：$\alpha$ 过 $E,F$ ⟹ $\vec n\perp\overrightarrow{EF}$；$\alpha\perp$ 平面 $AA_1C_1C$ ⟹ $\vec n\perp\vec m$．" "\n"
        r"   两个条件联立得 $r=p$、$q=-p$，平面方程一步到位，**完全不需要作辅助线找垂线**．" "\n"
        r"② ⭐ **原题的辅助线思路（取 $AC$ 中点 $J$、$AJ$ 中点 $D$，用 $BJ\perp$ 平面 $AA_1C_1C$）**" "\n"
        r"   与向量法给出的点 $D\left(\dfrac32,\dfrac12,0\right)$ 完全一致：$J\left(1,1,0\right)$ 是 $AC$ 中点，$D$ 是 $AJ$ 中点，" "\n"
        r"   $D=\dfrac{A+J}2=\left(\dfrac32,\dfrac12,0\right)$ ✓ 两种做法互相印证．" "\n"
        r"③ ⚠ **是五边形不是四边形**：很多同学默认「过三点作截面」是三角形，" "\n"
        r"   但本题平面还额外交出 $I,H$ 两个顶点（分别在上底的 $B_1C_1$ 与 $A_1C_1$ 上），共五个顶点．" "\n"
        r"   **逐棱代入是唯一可靠的计数办法**．" "\n"
        r"④ ⭐ **$\left|DE\right|=\left|IH\right|=\dfrac{\sqrt2}2$、$\left|EF\right|=\left|FI\right|=\sqrt2$**：" "\n"
        r"   各出现两次，合起来是 $3\sqrt2$；只剩 $\left|HD\right|=\sqrt6$ 一次，故总长 $3\sqrt2+\sqrt6$．" "\n"
        r"   选项 A（$2\sqrt2+\sqrt6$）正是漏掉一段 $\sqrt2$ 的结果，选项 D 是多算一段 $\sqrt6$ 的结果．" "\n"
        r"⑤ 数值复核：五段依次为 $0.707106781$、$1.414213562$、$1.414213562$、$0.707106781$、$2.449489743$，" "\n"
        r"   合计 $6.6921304299024635$，而 $3\sqrt2+\sqrt6=6.6921304299024635$ ✓ 逐位相同" "\n"
        r"**通法（已知垂直条件求截面）**：" "\n"
        r"① 建系，把「平面过两点」翻译成 $\vec n\perp\overrightarrow{PQ}$；" "\n"
        r"② 把「两平面垂直」翻译成 $\vec n\perp\vec m$（$\vec m$ 是已知平面的法向量）；" "\n"
        r"③ 两个线性条件定出 $\vec n$ 的比例，写平面方程；" "\n"
        r"④ 逐棱（含上、下底面）代入求交点，数出边数后逐段求长．"
    ),
    'difficulty': 0.80,
    'topics': ['M-T-287'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-287-V3',
}

T311_E1 = {
    'type': '填空',
    'stem_text': (
        r"已知正方体 $ABCD-A_1B_1C_1D_1$ 的棱长为 $2$，点 $E$ 为 $A_1D_1$ 中点，点 $P$、$M$ 在四边形 $ABCD$ 内（包括边界），点 $P$ 到平面 $ABB_1A_1$ 的距离等于它到点 $D$ 的距离，直线 $MB_1\parallel$ 平面 $EC_1D$，则 $PM$ 的最小值为 ____"
    ),
    'stem': [
        r"已知正方体 $ABCD-A_1B_1C_1D_1$ 的棱长为 $2$，点 $E$ 为 $A_1D_1$ 中点，点 $P$、$M$ 在四边形 $ABCD$ 内（包括边界），点 $P$ 到平面 $ABB_1A_1$ 的距离等于它到点 $D$ 的距离，直线 $MB_1\parallel$ 平面 $EC_1D$，则 $PM$ 的最小值为 ____",
    ],
    'opts': [],
    'answer': r"$\dfrac{3\sqrt5}{10}$",
    'analysis': (
        r"两个条件分别给出 $P$、$M$ 在底面内的轨迹方程：" "\n"
        r"$P$ 到平面 $ABB_1A_1$ 的距离就是 $P$ 到交线 $AB$ 的距离，等于 $\left|PD\right|$ ⟹ 抛物线段；" "\n"
        r"$MB_1\parallel$ 平面 $EC_1D$ ⟹ $\vec n\cdot\overrightarrow{B_1M}=0$ ⟹ 直线段．" "\n"
        r"剩下是「曲线上一点到直线的最短距离」，用与已知直线平行的切线做．"
    ),
    'solution': (
        r"以 $D$ 为原点建系：$D\left(0,0,0\right)$、$A\left(2,0,0\right)$、$B\left(2,2,0\right)$、$C\left(0,2,0\right)$、" "\n"
        r"$A_1\left(2,0,2\right)$、$B_1\left(2,2,2\right)$、$C_1\left(0,2,2\right)$、$D_1\left(0,0,2\right)$．" "\n"
        r"$E$ 为 $A_1D_1$ 中点 ⟹ $E\left(1,0,2\right)$．设 $P\left(x_1,y_1,0\right)$、$M\left(x_2,y_2,0\right)$．" "\n"
        r"**$P$ 的轨迹**：平面 $ABB_1A_1$ 即 $y=0$，与底面 $ABCD$ 的交线是 $AB$（即 $x=2$）．" "\n"
        r"因 $P$ 在底面内，$P$ 到平面 $ABB_1A_1$ 的距离 = $P$ 到直线 $AB$ 的距离 $=2-x_1$．" "\n"
        r"由条件 $2-x_1=\left|PD\right|=\sqrt{x_1^2+y_1^2}$，平方得 $4-4x_1+x_1^2=x_1^2+y_1^2$，" "\n"
        r"即 $\boxed{y_1^2=4-4x_1}$（$0\le x_1\le1$，取 $y_1=\sqrt{4-4x_1}$ 一支即可）．" "\n"
        r"**$M$ 的轨迹**：平面 $EC_1D$ 中 $\overrightarrow{DE}=\left(1,0,2\right)$、$\overrightarrow{DC_1}=\left(0,2,2\right)$，" "\n"
        r"法向量 $\vec n=\overrightarrow{DE}\times\overrightarrow{DC_1}=\left(-4,-2,2\right)\parallel\left(-2,-1,1\right)$．" "\n"
        r"由 $MB_1\parallel$ 平面 $EC_1D$ 得 $\vec n\cdot\overrightarrow{B_1M}=0$，$\overrightarrow{B_1M}=\left(x_2-2,y_2-2,-2\right)$：" "\n"
        r"$-2\left(x_2-2\right)-\left(y_2-2\right)-2=0$，即 $\boxed{2x_2+y_2-4=0}$（$1\le x_2\le2$）．" "\n"
        r"**求最短距离**：$M$ 在直线 $l:2x+y-4=0$ 上，$P$ 在曲线 $y=\sqrt{4-4x}$ 上．" "\n"
        r"$P$ 到 $l$ 的距离为 $d\left(x\right)=\dfrac{\left|2x+\sqrt{4-4x}-4\right|}{\sqrt5}$．" "\n"
        r"令 $u=\sqrt{4-4x}\in\left[0,2\right]$，则 $x=1-\dfrac{u^2}4$，" "\n"
        r"$2x+u-4=2-\dfrac{u^2}2+u-4=-\dfrac{u^2}2+u-2<0$（恒负），" "\n"
        r"故 $d=\dfrac{\dfrac{u^2}2-u+2}{\sqrt5}$，当 $u=1$ 时取最小值 $\dfrac{\dfrac12-1+2}{\sqrt5}=\dfrac{3}{2\sqrt5}=\dfrac{3\sqrt5}{10}$．" "\n"
        r"此时 $u=1$ ⟹ $y=\sqrt{4-4x}=1$ ⟹ $x=\dfrac34$，即 $P\left(\dfrac34,1,0\right)$．" "\n"
        r"验证：过 $P$ 作 $l$ 的垂线（方向 $\left(2,1\right)$）得垂足 $\left(\dfrac{27}{20},\dfrac{13}{10}\right)$，$x=\dfrac{27}{20}\in\left[1,2\right]$ 且 $y=\dfrac{13}{10}\in\left[0,2\right]$，" "\n"
        r"确实在 $M$ 的可取范围内，故 $PM$ 的最小值为 $\boxed{\dfrac{3\sqrt5}{10}}$．"
    ),
    'review': (
        r"① ⭐⭐ **「点到平面的距离」在动点位于另一平面内时，等于「点到交线的距离」**：" "\n"
        r"   $P\in$ 底面 $ABCD$，平面 $ABB_1A_1\perp$ 底面且交线为 $AB$，故 $d\left(P,\text{平面 }ABB_1A_1\right)=d\left(P,AB\right)=2-x_1$．" "\n"
        r"   这一步把三维距离降到二维，是本题的入口．" "\n"
        r"② ⭐⭐ **「线面平行」⟹ $\vec n\cdot\overrightarrow{B_1M}=0$**：注意向量要取 $B_1$ 到 $M$（直线上一点到平面外一点），" "\n"
        r"   且 $M$ 的 $z$ 坐标为 $0$（在底面内），故 $\overrightarrow{B_1M}$ 的第三分量恒为 $-2$．" "\n"
        r"③ ⭐ **$M$ 的轨迹是线段不是整条直线**：由 $M$ 在正方形 $ABCD$ 内且 $2x_2+y_2=4$ 得 $1\le x_2\le2$，" "\n"
        r"   最后必须验证垂足落在这段上（本题垂足 $x=\dfrac{27}{20}=1.35\in[1,2]$ ✓）．" "\n"
        r"④ ⭐ **换元 $u=\sqrt{4-4x}$ 后分子恒负**：$-\dfrac{u^2}2+u-2$ 的最大值是 $-1.5$（$u=1$），" "\n"
        r"   所以绝对值可以直接去掉，不必讨论符号．" "\n"
        r"⑤ ⭐ **与 $l$ 平行的切线切点即最近点**：$l$ 斜率 $-2$，曲线 $y=\sqrt{4-4x}$ 的导数 $y'=\dfrac{-2}{\sqrt{4-4x}}$，" "\n"
        r"   令 $y'=-2$ 得 $x=\dfrac34$、$y=1$，与换元法结果完全一致（两种算法互证）．" "\n"
        r"⑥ 数值复核：$\dfrac{3\sqrt5}{10}=0.6708203932499369$；" "\n"
        r"   直接计算 $P\left(\dfrac34,1\right)$ 到直线 $2x+y-4=0$ 的距离 $=\dfrac{\left|1.5+1-4\right|}{\sqrt5}=\dfrac{1.5}{\sqrt5}=0.6708204$ ✓" "\n"
        r"**通法（动点 + 距离/平行条件）**：" "\n"
        r"① 把每个条件翻译成动点所在平面内的一个方程（轨迹）；" "\n"
        r"② 两条轨迹都求出后，问题退化为平面解析几何；" "\n"
        r"③ 「曲线上一点到直线的最短距离」⟹ 求与已知直线平行的切线（导数法）或换元配方；" "\n"
        r"④ 最后务必验证垂足/最近点落在轨迹的有效范围内．"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-311'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-311-E1',
}

T311_V2 = {
    'type': '填空',
    'stem_text': (
        r"空间给定不共面的 $A$，$B$，$C$，$D$ 四个点，其中任意两点间的距离都不相同，考虑具有如下性质的平面 $\alpha$：$A$，$B$，$C$，$D$ 中有三个点到 $\alpha$ 的距离相同，另一个点到 $\alpha$ 的距离是前三个点到 $\alpha$ 的距离的 $2$ 倍，这样的平面 $\alpha$ 的个数是 ____ 个"
    ),
    'stem': [
        r"空间给定不共面的 $A$，$B$，$C$，$D$ 四个点，其中任意两点间的距离都不相同，考虑具有如下性质的平面 $\alpha$：$A$，$B$，$C$，$D$ 中有三个点到 $\alpha$ 的距离相同，另一个点到 $\alpha$ 的距离是前三个点到 $\alpha$ 的距离的 $2$ 倍，这样的平面 $\alpha$ 的个数是 ____ 个",
    ],
    'opts': [],
    'answer': r"$32$",
    'analysis': (
        r"先选出「距离不同的那一个点」（$4$ 种取法），再对余下三个点分两类：" "\n"
        r"三个点全在 $\alpha$ 同侧（$2$ 个平面），或两同一异（$\mathrm C_3^1=3$ 种分法 $\times$ 各 $2$ 种 = $6$ 个平面）．" "\n"
        r"故每个「特殊点」对应 $8$ 个平面，共 $4\times8=32$ 个．"
    ),
    'solution': (
        r"分两步计数．" "\n"
        r"**第一步：选「距离是别人 $2$ 倍」的那个点**，有 $4$ 种取法．以下固定这个点为 $D$，" "\n"
        r"其余三点 $A,B,C$ 到 $\alpha$ 的距离相等（记为 $h$），$D$ 到 $\alpha$ 的距离为 $2h$．" "\n"
        r"（$h\ne0$，否则四个点共面，与题设矛盾．）" "\n"
        r"**第二步：对 $A,B,C$ 三点分类**" "\n"
        r"（1）**$A,B,C$ 在 $\alpha$ 同侧**：此时 $\alpha\parallel$ 平面 $ABC$，" "\n"
        r"$\alpha$ 位于平面 $ABC$ 的两侧各有一个（分别对应 $D$ 与 $A,B,C$ 同侧、异侧两种情形），共 $2$ 个．" "\n"
        r"（2）**$A,B,C$ 不同侧**：必为「$2$ 个点在一侧、另 $1$ 个点在另一侧」，" "\n"
        r"选单独一侧的那个点有 $\mathrm C_3^1=3$ 种取法．" "\n"
        r"对每一种取法，$\alpha$ 必过 $\triangle ABC$ 的一条中位线（该中位线连接「同侧两点」与「异侧点」所在两边的中点），" "\n"
        r"再由「$D$ 到 $\alpha$ 的距离是 $A,B,C$ 到 $\alpha$ 距离的 $2$ 倍」确定 $\alpha$ 绕该中位线转到哪一侧 —— " "\n"
        r"「$D$ 与单侧点同侧」或「$D$ 与单侧点异侧」各唯一确定一个平面，共 $2$ 个．" "\n"
        r"故本类共 $3\times2=6$ 个．" "\n"
        r"综上，对每个「特殊点」有 $2+6=8$ 个平面，总数为 $4\times8=\boxed{32}$．"
    ),
    'review': (
        r"① ⭐⭐ **计数分两步：先选「特殊点」，再按同侧/异侧分类** ——" "\n"
        r"   顺序反了会重复计数（同一个平面可能被不同的「特殊点」各算一次，但本题因距离比为 $2:1$ 而不会）．" "\n"
        r"② ⭐ **「三个点距离相等」的几何含义**：同侧 ⟹ $\alpha\parallel$ 该三点确定的平面；" "\n"
        r"   异侧 ⟹ $\alpha$ 过该三角形的一条中位线．这两句话是整个分类的根据．" "\n"
        r"③ ⚠ **「任意两点间距离都不相同」这个条件的作用**：保证各平面互不重合（否则某些中位线平面会退化或重合）．" "\n"
        r"   计数时不必逐个验证，但要知道它是命题人为了「答案唯一」加的保险．" "\n"
        r"④ ⭐ **$4\times\left(2+6\right)=32$**：两个括号里的数分别是「同侧 $2$」与「异侧 $3\times2=6$」，不要漏乘 $4$．" "\n"
        r"   常见错答 $8$（只算了一个特殊点）与 $24$（把异侧算成 $4$ 个）．" "\n"
        r"⑤ 说明：本题为纯计数题，无数值可验算；推导依据原书【详解】的分类框架，" "\n"
        r"   并把「$3$ 个点的取法有 $3$ 种」明确写成 $\mathrm C_3^1$、「每种 $2$ 个」明确为「$D$ 与单侧点同侧/异侧」．" "\n"
        r"**通法（空间平面计数）**：" "\n"
        r"① 先确定「距离特殊」的那个点（乘点数）；" "\n"
        r"② 对余下的点按「在平面同侧 / 异侧」分类；" "\n"
        r"③ 同侧 ⟹ 平行平面（$2$ 个）；异侧 ⟹ 过中位线（$2$ 个点一组，$\mathrm C_n^1$ 种分组，每组再乘 $2$）；" "\n"
        r"④ 逐类相乘后求和．"
    ),
    'difficulty': 0.80,
    'topics': ['M-T-311'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-311-V2',
}

T311_V3 = {
    'type': '填空',
    'stem_text': (
        r"如图，长方体 $ABCD-A_1B_1C_1D_1$ 的底面 $ABCD$ 是正方形，其侧面展开图是边长为 $4$ 的正方形，$E$、$F$ 分别是侧棱 $AA_1$、$CC_1$ 上的动点，$AE+CF=4$，点 $P$ 在棱 $AA_1$ 上，且 $AP=1$，若 $EF\parallel$ 平面 $PBD$，则 $CF=$ ____"
    ),
    'stem': [
        r"如图，长方体 $ABCD-A_1B_1C_1D_1$ 的底面 $ABCD$ 是正方形，其侧面展开图是边长为 $4$ 的正方形，$E$、$F$ 分别是侧棱 $AA_1$、$CC_1$ 上的动点，$AE+CF=4$，点 $P$ 在棱 $AA_1$ 上，且 $AP=1$，若 $EF\parallel$ 平面 $PBD$，则 $CF=$ ____",
    ],
    'opts': [],
    'answer': r"$1$",
    'analysis': (
        r"侧面展开图是边长 $4$ 的正方形 ⟹ 底面周长 $=4$、高 $=4$ ⟹ 底面边长 $=1$．" "\n"
        r"建系后由 $EF\parallel$ 平面 $PBD$ 得 $\overrightarrow{EF}\cdot\vec n=0$（$\vec n$ 是平面 $PBD$ 的法向量），" "\n"
        r"这是一次方程，与 $AE+CF=4$ 联立即解．"
    ),
    'solution': (
        r"侧面展开图中，宽 = 底面周长 $=4a$（$a$ 为底面边长），高 = 侧棱长 $h$．" "\n"
        r"它是边长为 $4$ 的正方形，故 $4a=4$、$h=4$，即 $\boxed{a=1}$、$\boxed{h=4}$．" "\n"
        r"建系：$A\left(0,0,0\right)$、$B\left(1,0,0\right)$、$C\left(1,1,0\right)$、$D\left(0,1,0\right)$、" "\n"
        r"$A_1\left(0,0,4\right)$、$B_1\left(1,0,4\right)$、$C_1\left(1,1,4\right)$、$D_1\left(0,1,4\right)$．" "\n"
        r"设 $AE=e$、$CF=f$，则 $E\left(0,0,e\right)$、$F\left(1,1,f\right)$，且 $e+f=4$．" "\n"
        r"由 $AP=1$ 得 $P\left(0,0,1\right)$．" "\n"
        r"平面 $PBD$：$\overrightarrow{PB}=\left(1,0,-1\right)$、$\overrightarrow{PD}=\left(0,1,-1\right)$，" "\n"
        r"法向量 $\vec n=\overrightarrow{PB}\times\overrightarrow{PD}=\left(1,1,1\right)$，平面方程为 $x+y+z=1$．" "\n"
        r"由 $EF\parallel$ 平面 $PBD$ 得 $\overrightarrow{EF}\cdot\vec n=0$，而 $\overrightarrow{EF}=\left(1,1,f-e\right)$：" "\n"
        r"$1+1+\left(f-e\right)=0$，即 $e-f=2$．" "\n"
        r"与 $e+f=4$ 联立：$2e=6$、$2f=2$，得 $e=3$、$f=1$．" "\n"
        r"故 $\boxed{CF=1}$．"
    ),
    'review': (
        r"① ⭐⭐ **「侧面展开图是正方形」同时给出底面边长和高**：宽 $=4a$（底面周长）、高 $=h$，" "\n"
        r"   两者都等于 $4$ ⟹ $a=1$、$h=4$．**只读出一个是本题最常见的失误**" "\n"
        r"   （若只取 $a=1$ 而不知道 $h=4$，$E,F$ 的坐标就写不出来）．" "\n"
        r"② ⭐ **线面平行 ⟹ 方向向量与法向量点积为零**：$\overrightarrow{EF}=\left(1,1,f-e\right)$、$\vec n=\left(1,1,1\right)$，" "\n"
        r"   一步得 $e-f=2$，与 $e+f=4$ 联立即可，不必作辅助线．" "\n"
        r"③ ⭐ **原书的辅助线思路（在 $PA$ 上截取 $PQ=PA_1=1$，证 $QC\parallel PO$，得平行四边形 $EQCF$）**" "\n"
        r"   与向量法结果一致：$QE=CF$ 且 $AE+AE_1=4$，最终同样得 $CF=1$．" "\n"
        r"   向量法更短，几何法更直观，两者可互证．" "\n"
        r"④ ⚠ **$E,F$ 的坐标别写错**：$E$ 在 $AA_1$ 上（$x=y=0$），$F$ 在 $CC_1$ 上（$x=y=1$），" "\n"
        r"   $\overrightarrow{EF}$ 的前两个分量都是 $1$（不是 $0$），这正是 $1+1+\left(f-e\right)=0$ 里前两项的来源．" "\n"
        r"⑤ 数值复核：$e=3$、$f=1$ 时 $e+f=4$ ✓；$\overrightarrow{EF}=\left(1,1,-2\right)$，$\vec n\cdot\overrightarrow{EF}=1+1-2=0$ ✓；" "\n"
        r"   $E\left(0,0,3\right)$、$F\left(1,1,1\right)$ 分别在 $AA_1$、$CC_1$ 上（第三分量在 $[0,4]$ 内）✓" "\n"
        r"**通法（长方体中的线面平行）**：" "\n"
        r"① 展开图是正方形 ⟹ 底面周长 = 高 = 正方形边长；" "\n"
        r"② 建系写三点平面方程，法向量取最简整数比；" "\n"
        r"③ 线面平行 ⟹ 方向 $\cdot$ 法向量 $=0$；" "\n"
        r"④ 与题给的线段和/差条件联立解方程．"
    ),
    'difficulty': 0.70,
    'topics': ['M-T-311'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-311-V3',
}

QS = [
    T245_E1, T245_V1, T245_V2, T245_V3,
    T187_E1,
    T287_E1, T287_V2, T287_V3,
    T311_E1, T311_V2, T311_V3,
]
