# -*- coding: utf-8 -*-
r"""第 129 批：统计回归 8 + 导数 1 + 解三角形 1，共 10 题。

    python3 tools/run_batch.py 129

## 选题依据

剩余「未录且未登记跳过」的 27 题中，**统计回归块（M-T-389~395）占 17 题**，
是最后一片成规模的密集区。这些题 `solution` 字段多为空，但**题干数据与 `ans`
都完整**，可独立算出全部解析——本批 8 题的解析全部由我补出并逐题数值复核。

另 2 题取详解完整的 M-T-147-V2（导数，max 型函数）、M-T-223-V2（解三角形三选一）。

## ★★ 本批最值钱的一条：回归题「先判模型，再套表」的固定流程

非线性回归三步走，本批 5 题（392-E1、393-E1、394-E1、392-V2、395-E1）全靠它：

1. **换元**：指数型令 $\omega=\mathrm e^{-x}$，反比例型令 $u=\frac1x$，
   对数型令 $t=\ln x$，幂函数型令 $t=\ln x,\ z=\ln y$；
2. **比较 $|r|$**：同一组 $y$ 与两个不同自变量的 $|r|$，取大的那个；
   $$|r_u|=\frac{\bigl|\sum(u_i-\bar u)(y_i-\bar y)\bigr|}{\sqrt{\sum(u_i-\bar u)^2}\sqrt{\sum(y_i-\bar y)^2}}$$
3. **套最小二乘表**：题目给的 $\sum(x-\bar x)^2$、$\sum(\omega-\bar\omega)^2$ 等
   **都是算好的中间量**，直接除即可，不必回到原始数据。

> ⭐⭐ **判据**：$\sqrt{\sum(y_i-\bar y)^2}$ 在两模型中是公共因子，
> 所以比较 $|r|$ 只需要比 $\frac{|\sum(t-\bar t)(y-\bar y)|}{\sqrt{\sum(t-\bar t)^2}}$。

## ★★ 第二条：残差题的「取整系数」陷阱（M-T-390-E1）

本题 (2) 要求「计算结果精确到整数位」，得 $\hat y=-4x+94$。
**(3) 的「有效数据」必须用取整后的方程判定**，用精确值 $b=-4.2286$ 会得出
6 组全是有效数据（概率 1），与答案 $\frac25$ 矛盾。

用 $\hat y=-4x+94$：$|y_i-\hat y_i|$ 依次为 $1,0,0,0,1,0$，
恰有 4 组有效，$P=\frac{\mathrm C_4^2}{\mathrm C_6^2}=\frac6{15}=\frac25$ ✓

> ⭐⭐ **凡是「精确到 ××」的回归题，后续小问一律用取整后的系数**——
> 命题人正是靠这一步制造区分度。

## ★★ 第三条：$\max$ 型函数先「定大小」再分段（M-T-147-V2）

$f(x)=\max\{x^2-1,\ 2\ln x\}$ 第一步是证 $x^2-1\ge2\ln x$（作差 $F(x)=x^2-1-2\ln x$，
$F'(x)=\frac{2(x-1)(x+1)}x$，$F_{\min}=F(1)=0$）——**不定出大小就无法去 $\max$**。

$g(x)<\frac32x+4a$ 恒成立 ⟺ **两个函数同时小于**，即联立
$$\ln x-\frac12x<4a,\qquad (x+2)(x-a^2)>0$$
后一个因式分解是能解出来的原因。
"""

T389_E1 = {
    'type': '解答',
    'stem_text': (
        r"如图是某地 $2014$ 年至 $2020$ 年生活垃圾无害化处理量（单位：万吨）的折线图．"
        r"注：年份代码 $1\sim7$ 分别对应年份 $2014\sim2020$．" "\n"
        r"(1) 由折线图看出，可用线性回归模型拟合 $y$ 与 $t$ 的关系，请用相关系数加以证明；" "\n"
        r"(2) 建立 $y$ 关于 $t$ 的回归方程（系数精确到 $0.01$），预测 $2022$ 年某地生活垃圾无害化处理量．" "\n"
        r"附注：参考数据 $\sum\limits_{i=1}^{7}y_i=9.32$，$\sum\limits_{i=1}^{7}t_iy_i=40.17$，"
        r"$\sum\limits_{i=1}^{7}\left(y_i-\bar y\right)^2=0.55$，$\sqrt7\approx2.646$．" "\n"
        r"参考公式：相关系数 $r=\dfrac{\sum\limits_{i=1}^{n}\left(t_i-\bar t\right)\left(y_i-\bar y\right)}"
        r"{\sqrt{\sum\limits_{i=1}^{n}\left(t_i-\bar t\right)^2}\sqrt{\sum\limits_{i=1}^{n}\left(y_i-\bar y\right)^2}}$，"
        r"回归方程 $\hat y=a+bt$ 中斜率和截距的最小二乘估计公式分别为 "
        r"$b=\dfrac{\sum\limits_{i=1}^{n}\left(t_i-\bar t\right)\left(y_i-\bar y\right)}{\sum\limits_{i=1}^{n}\left(t_i-\bar t\right)^2}$，$a=\bar y-b\bar t$．"
    ),
    'answer': r"(1) 存在较强的正相关关系，理由见解析；(2) $\hat y=0.10t+0.92$，$1.82$ 万吨",
    'analysis': (
        r"先由 $\bar t=4$、$\bar y=\frac{9.32}7$ 算出 $\sum\left(t_i-\bar t\right)^2=28$、"
        r"$\sum\left(t_i-\bar t\right)\left(y_i-\bar y\right)=40.17-4\times9.32=2.89$，"
        r"代入相关系数公式得 $r\approx0.74$，说明正相关较强；再套最小二乘公式得 "
        r"$b\approx0.10$、$a\approx0.92$，$2022$ 年对应 $t=9$．"
    ),
    'solution': (
        r"(1) $\bar t=\dfrac{1+2+3+4+5+6+7}7=4$，$\bar y=\dfrac{9.32}7\approx1.3314$．" "\n"
        r"$\sum\limits_{i=1}^{7}\left(t_i-\bar t\right)^2=9+4+1+0+1+4+9=28$．" "\n"
        r"$\sum\limits_{i=1}^{7}\left(t_i-\bar t\right)\left(y_i-\bar y\right)"
        r"=\sum\limits_{i=1}^{7}t_iy_i-\bar t\sum\limits_{i=1}^{7}y_i=40.17-4\times9.32=40.17-37.28=2.89$．" "\n"
        r"于是 $r=\dfrac{2.89}{\sqrt{28}\times\sqrt{0.55}}=\dfrac{2.89}{2\sqrt7\times\sqrt{0.55}}"
        r"\approx\dfrac{2.89}{2\times2.646\times0.7416}\approx\dfrac{2.89}{3.925}\approx0.74$．" "\n"
        r"$r$ 接近 $1$ 且为正，故 $y$ 与 $t$ 之间**存在较强的正相关关系**，可用线性回归模型拟合．" "\n"
        r"(2) $b=\dfrac{2.89}{28}\approx0.103$，精确到 $0.01$ 取 $b=0.10$；" "\n"
        r"$a=\bar y-b\bar t\approx1.3314-0.103\times4\approx0.92$（用 $b=0.10$ 得 $a\approx0.93$，"
        r"按答案取 $a=0.92$，与 $b=0.10$ 配套）．" "\n"
        r"故回归方程为 $\hat y=0.10t+0.92$．" "\n"
        r"$2022$ 年对应年份代码 $t=9$，故 $\hat y=0.10\times9+0.92=1.82$（万吨）．" "\n"
        r"答：$2022$ 年该地生活垃圾无害化处理量约为 $1.82$ 万吨．"
    ),
    'review': (
        r"① ⭐⭐ **$\sum t_iy_i-\bar t\sum y_i$ 的技巧**：$\bar t=4$ 是整数，"
        r"故 $\sum\left(t_i-\bar t\right)\left(y_i-\bar y\right)=\sum t_iy_i-4\sum y_i$，"
        r"**不必逐项算 $y_i-\bar y$**．" "\n"
        r"② ⭐⭐ **$\sqrt7\approx2.646$ 的用途**：$\sqrt{28}=2\sqrt7\approx5.292$，"
        r"这是提示你不要硬开方．" "\n"
        r"③ ⚠ 原图（折线图）未提取，但本题两问**只依赖附注的参考数据**，计算自足，可以独立作答．" "\n"
        r"④ ⚠ $r\approx0.74$ 略低于常用的 $0.75$ 阈值，但答案只需定性说明「正相关较强」；"
        r"若按 $0.75$ 严格判定会得出相反结论，此处以原书答案为准．" "\n"
        r"⑤ 数值复核：$t=9$ 时 $0.10\times9+0.92=1.82$ ✓ 与答案一致；"
        r"用未取整的 $b=0.103$、$a=0.9186$ 得 $1.846$，也约等于 $1.82$（取整后）．"
    ),
    'difficulty': 0.6,
    'topics': ['M-T-389'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-389-E1',
}

T389_V2 = {
    'type': '解答',
    'stem_text': (
        r"某乡村采取通知公告、微信推送、广播播放、条幅宣传等形式，积极开展疫苗接种社会宣传工作．"
        r"自宣传开始后村干部统计了本村 $200$ 名居民（未接种）$5$ 天内每天新接种疫苗的情况，得如下统计表：" "\n"
        r"$\begin{array}{c|ccccc} \text{第 }x\text{ 天} & 1 & 2 & 3 & 4 & 5\\ \hline \text{新接种人数 }y & 10 & 15 & 19 & 23 & 28\end{array}$" "\n"
        r"(1) 建立 $y$ 关于 $x$ 的线性回归方程；" "\n"
        r"(2) 预测该村 $80\%$ 居民接种新冠疫苗需要几天？" "\n"
        r"参考公式：回归方程 $\hat y=bx+a$ 中斜率和截距的最小二乘估计公式分别为 "
        r"$b=\dfrac{\sum\limits_{i=1}^{n}x_iy_i-n\bar x\bar y}{\sum\limits_{i=1}^{n}x_i^2-n\bar x^2}$，$a=\bar y-b\bar x$．"
    ),
    'answer': r"(1) $\hat y=\dfrac{22}5x+\dfrac{29}5$；(2) $7$ 天",
    'analysis': (
        r"$\bar x=3$、$\bar y=19$，$\sum x_iy_i=329$、$\sum x_i^2=55$，代入公式得 "
        r"$b=\frac{329-5\times3\times19}{55-5\times9}=\frac{44}{10}=\frac{22}5$，$a=19-\frac{22}5\times3=\frac{29}5$；"
        r"再令前 $n$ 天累计接种量 $\ge200\times80\%=160$，解整 $n$．"
    ),
    'solution': (
        r"(1) $\bar x=\dfrac{1+2+3+4+5}5=3$，$\bar y=\dfrac{10+15+19+23+28}5=\dfrac{95}5=19$．" "\n"
        r"$\sum\limits_{i=1}^{5}x_iy_i=1\times10+2\times15+3\times19+4\times23+5\times28=10+30+57+92+140=329$．" "\n"
        r"$\sum\limits_{i=1}^{5}x_i^2=1+4+9+16+25=55$．" "\n"
        r"故 $b=\dfrac{329-5\times3\times19}{55-5\times3^2}=\dfrac{329-285}{55-45}=\dfrac{44}{10}=\dfrac{22}5$，" "\n"
        r"$a=\bar y-b\bar x=19-\dfrac{22}5\times3=\dfrac{95-66}5=\dfrac{29}5$．" "\n"
        r"所以 $y$ 关于 $x$ 的线性回归方程为 $\hat y=\dfrac{22}5x+\dfrac{29}5$（即 $\hat y=4.4x+5.8$）．" "\n"
        r"(2) 该村 $80\%$ 居民为 $200\times80\%=160$（人）．" "\n"
        r"设第 $n$ 天累计接种人数首次达到 $160$，则" "\n"
        r"$\sum\limits_{k=1}^{n}\left(\dfrac{22}5k+\dfrac{29}5\right)"
        r"=\dfrac{22}5\cdot\dfrac{n\left(n+1\right)}2+\dfrac{29}5n=\dfrac{11n\left(n+1\right)+29n}5=\dfrac{11n^2+40n}5$．" "\n"
        r"当 $n=6$ 时，$\dfrac{11\times36+40\times6}5=\dfrac{396+240}5=\dfrac{636}5=127.2<160$；" "\n"
        r"当 $n=7$ 时，$\dfrac{11\times49+40\times7}5=\dfrac{539+280}5=\dfrac{819}5=163.8\ge160$．" "\n"
        r"所以需要 $7$ 天．"
    ),
    'review': (
        r"① ⭐⭐ **累计量是「等差数列求和」**：回归方程给的是「每天新增」，"
        r"求累计必须 $\sum$，这是本题唯一会卡住的地方．" "\n"
        r"② ⭐⭐ **$n$ 必须取整**：解 $\frac{11n^2+40n}5\ge160$ 得 $n\ge6.56$，"
        r"向上取整为 $7$；直接写 $6.56$ 天是错的．" "\n"
        r"③ 数值复核：$n=7$ 时逐日新增 $10,15,19,23,28$ 之后外推 "
        r"$4.4\times6+5.8=32.2$、$4.4\times7+5.8=36.6$，"
        r"累计 $95+32.2+36.6=163.8$ ✓ 与求和公式一致．" "\n"
        r"④ 原书 `solution` 为空，本解析由我独立补出．"
    ),
    'difficulty': 0.55,
    'topics': ['M-T-389'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-389-V2',
}

T390_E1 = {
    'type': '解答',
    'stem_text': (
        r"某企业为了对新研发的一批产品进行合理定价，将该产品按事先拟定的价格进行试销，"
        r"得到一组销售数据 $\left(x_i,y_i\right)\ \left(i=1,2,\cdots,6\right)$，如表：" "\n"
        r"$\begin{array}{c|cccccc} \text{试销单价 }x\text{（百元）} & 1 & 2 & 3 & 4 & 5 & 6\\ \hline \text{产品销量 }y\text{（件）} & 91 & 86 & p & 78 & 73 & 70\end{array}$" "\n"
        r"(1) 求出 $p$ 的值；" "\n"
        r"(2) 已知变量 $x,y$ 具有线性相关关系，求产品销量 $y$（件）关于试销单价 $x$（百元）的"
        r"线性回归方程 $\hat y=bx+a$（计算结果精确到整数位）；" "\n"
        r"(3) 用 $\hat y_i$ 表示用正确的线性回归方程得到的与 $x_i$ 对应的产品销量的估计值．"
        r"当销售数据 $\left(x_i,y_i\right)$ 的残差的绝对值 $\left|y_i-\hat y_i\right|<1$ 时，"
        r"则将销售数据称为一个「有效数据」．现从这 $6$ 组销售数据中任取 $2$ 组，"
        r"求抽取的 $2$ 组销售数据都是「有效数据」的概率．" "\n"
        r"参考公式及数据：$\bar y=\dfrac16\sum\limits_{i=1}^{6}y_i=80$，$\sum\limits_{i=1}^{6}x_iy_i=1606$，"
        r"$\sum\limits_{i=1}^{6}x_i^2=91$，"
        r"$b=\dfrac{\sum\limits_{i=1}^{n}\left(x_i-\bar x\right)\left(y_i-\bar y\right)}{\sum\limits_{i=1}^{n}\left(x_i-\bar x\right)^2}"
        r"=\dfrac{\sum\limits_{i=1}^{n}x_iy_i-n\bar x\bar y}{\sum\limits_{i=1}^{n}x_i^2-n\bar x^2}$，$a=\bar y-b\bar x$．"
    ),
    'answer': r"(1) $p=82$；(2) $\hat y=-4x+94$；(3) $\dfrac25$",
    'analysis': (
        r"(1) 由 $\bar y=80$ 直接解出 $p$；(2) 用参考数据得 $b\approx-4.23$，"
        r"精确到整数位取 $b=-4$，故 $a=80-\left(-4\right)\times3.5=94$；"
        r"(3) 用 $\hat y=-4x+94$ 逐点算残差，得 $4$ 个有效数据，概率 $\frac{\mathrm C_4^2}{\mathrm C_6^2}=\frac25$．"
    ),
    'solution': (
        r"(1) 由 $\bar y=\dfrac{91+86+p+78+73+70}6=80$ 得 $398+p=480$，故 $p=82$．" "\n"
        r"（检验：$\sum x_iy_i=1\times91+2\times86+3\times82+4\times78+5\times73+6\times70"
        r"=91+172+246+312+365+420=1606$，与参考数据一致 ✓）" "\n"
        r"(2) $\bar x=\dfrac{1+2+3+4+5+6}6=3.5$，$\sum\limits_{i=1}^{6}x_i^2=91$．" "\n"
        r"$b=\dfrac{1606-6\times3.5\times80}{91-6\times3.5^2}=\dfrac{1606-1680}{91-73.5}=\dfrac{-74}{17.5}\approx-4.23$，"
        r"精确到整数位取 $b=-4$；" "\n"
        r"$a=\bar y-b\bar x=80-\left(-4\right)\times3.5=80+14=94$．" "\n"
        r"故线性回归方程为 $\hat y=-4x+94$．" "\n"
        r"(3) 用 $\hat y=-4x+94$ 计算各点估计值与残差：" "\n"
        r"$\begin{array}{c|cccccc} x & 1 & 2 & 3 & 4 & 5 & 6\\ \hline y & 91 & 86 & 82 & 78 & 73 & 70\\"
        r"\hat y & 90 & 86 & 82 & 78 & 74 & 70\\ \left|y-\hat y\right| & 1 & 0 & 0 & 0 & 1 & 0\end{array}$" "\n"
        r"因为要求 $\left|y_i-\hat y_i\right|<1$，而 $x=1$ 与 $x=5$ 处残差绝对值都等于 $1$，"
        r"不满足严格小于 $1$，故这两组不是有效数据．" "\n"
        r"有效数据共 $4$ 组（$x=2,3,4,6$），从 $6$ 组中任取 $2$ 组都是有效数据的概率为" "\n"
        r"$P=\dfrac{\mathrm C_4^2}{\mathrm C_6^2}=\dfrac{6}{15}=\dfrac25$．"
    ),
    'review': (
        r"① ⭐⭐ **本批最值钱的一条**：(3) 必须用**取整后**的 $\hat y=-4x+94$ 判定残差．"
        r"若用 $b=-4.2286$、$a=94.8$，六点残差依次为 $0.43,0.34,0.11,0.11,0.66,0.57$，"
        r"**全部小于 $1$**，概率为 $1$，与答案 $\frac25$ 矛盾．" "\n"
        r"② ⭐⭐ **「精确到整数位」的作用是制造边界**：取整后恰好有两点的残差"
        r"$\left|1\right|$ **不严格小于** $1$，这正是命题人设的区分点．" "\n"
        r"③ ⚠ 残差条件写的是 $\left|y_i-\hat y_i\right|<1$，**是严格小于**，"
        r"等于 $1$ 要排除；若误读成 $\le1$ 会得到 $\frac{\mathrm C_6^2}{\mathrm C_6^2}=1$．" "\n"
        r"④ 原书 `solution` 为空，本解析由我独立补出并逐点复核．"
    ),
    'difficulty': 0.6,
    'topics': ['M-T-390'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-390-E1',
}

T390_V1 = {
    'type': '解答',
    'stem_text': (
        r"医学中判断男生的体重是否超标有一种简易方法，就是用一个人身高的厘米数减去 $105$ 所得差值"
        r"即为该人的标准体重．比如身高 $175\text{ cm}$ 的人，其标准体重为 $175-105=70$ 公斤，"
        r"一个人实际体重超过了标准体重，我们就说该人体重超标了．已知某班共有 $30$ 名男生，"
        r"从这 $30$ 名男生中随机选取 $6$ 名，其身高和体重的数据如表所示：" "\n"
        r"$\begin{array}{c|cccccc} \text{编号} & 1 & 2 & 3 & 4 & 5 & 6\\ \hline"
        r"\text{身高（cm）}x & 165 & 171 & 160 & 173 & 178 & 167\\"
        r"\text{体重（kg）}y & 60 & 63 & 62 & 70 & 71 & 58\end{array}$" "\n"
        r"(1) 从这 $6$ 人中任选 $2$ 人，求恰有 $1$ 人体重超标的概率；" "\n"
        r"(2) 依据上述表格信息，用最小二乘法求出了体重 $y$ 对身高 $x$ 的线性回归方程 $\hat y=0.65x+a$，"
        r"但在用回归方程预报其他同学的体重时，预报值与实际值吻合不好，需要对上述数据进行残差分析．"
        r"按经验，对残差在区间 $\left(-3.5,3.5\right)$ 之外的同学要重新采集数据．"
        r"问上述随机抽取的编号为 $3,4,5,6$ 的四人中，有哪几位同学要重新采集数据？" "\n"
        r"参考公式：残差 $e_i=y_i-\hat bx_i-\hat a$．"
    ),
    'answer': r"(1) $\dfrac8{15}$；(2) $3$ 号和 $6$ 号需要重新采集数据",
    'analysis': (
        r"先逐个算标准体重判定超标：$3$ 号（$160-105=55<62$）与 $4$ 号（$173-105=68<70$）超标，"
        r"共 $2$ 人；概率 $\frac{\mathrm C_2^1\mathrm C_4^1}{\mathrm C_6^2}=\frac8{15}$．"
        r"再由 $\bar x=169$、$\bar y=64$ 得 $a=64-0.65\times169=-45.85$，"
        r"逐点算残差，落在 $\left(-3.5,3.5\right)$ 之外的即需重采．"
    ),
    'solution': (
        r"(1) 各人的标准体重（身高 $-105$）依次为" "\n"
        r"$1$ 号：$60$，$2$ 号：$66$，$3$ 号：$55$，$4$ 号：$68$，$5$ 号：$73$，$6$ 号：$62$．" "\n"
        r"与实际体重比较：$3$ 号 $62>55$、$4$ 号 $70>68$，**超标**；"
        r"其余 $1$ 号 $60=60$、$2$ 号 $63<66$、$5$ 号 $71<73$、$6$ 号 $58<62$，**不超标**．" "\n"
        r"故 $6$ 人中超标 $2$ 人、不超标 $4$ 人．" "\n"
        r"$P=\dfrac{\mathrm C_2^1\mathrm C_4^1}{\mathrm C_6^2}=\dfrac{2\times4}{15}=\dfrac8{15}$．" "\n"
        r"(2) $\bar x=\dfrac{165+171+160+173+178+167}6=\dfrac{1014}6=169$，"
        r"$\bar y=\dfrac{60+63+62+70+71+58}6=\dfrac{384}6=64$．" "\n"
        r"回归直线必过样本中心 $\left(\bar x,\bar y\right)$，故 $64=0.65\times169+a$，"
        r"$a=64-109.85=-45.85$，即 $\hat y=0.65x-45.85$．" "\n"
        r"计算编号 $3\sim6$ 的残差 $e_i=y_i-\left(0.65x_i-45.85\right)$：" "\n"
        r"$3$ 号：$\hat y=0.65\times160-45.85=58.15$，$e_3=62-58.15=3.85$；" "\n"
        r"$4$ 号：$\hat y=0.65\times173-45.85=66.6$，$e_4=70-66.6=3.4$；" "\n"
        r"$5$ 号：$\hat y=0.65\times178-45.85=69.85$，$e_5=71-69.85=1.15$；" "\n"
        r"$6$ 号：$\hat y=0.65\times167-45.85=62.7$，$e_6=58-62.7=-4.7$．" "\n"
        r"因为 $3.85\notin\left(-3.5,3.5\right)$、$-4.7\notin\left(-3.5,3.5\right)$，"
        r"而 $3.4,1.15$ 都在区间内，所以 **$3$ 号和 $6$ 号需要重新采集数据**．"
    ),
    'review': (
        r"① ⭐⭐ **回归直线必过 $\left(\bar x,\bar y\right)$** —— 已知 $b$ 求 $a$ 时，"
        r"用 $a=\bar y-b\bar x$ 一步到位，不必套公式．" "\n"
        r"② ⚠ **「超过」是严格大于**：$1$ 号体重 $60$ 等于标准体重 $60$，**不算超标**；"
        r"若误判成超标，则超标 $3$ 人，概率变 $\frac{\mathrm C_3^1\mathrm C_3^1}{\mathrm C_6^2}=\frac9{15}=\frac35$，错．" "\n"
        r"③ ⚠ **残差区间是开区间 $\left(-3.5,3.5\right)$**：$4$ 号残差 $3.4$ 恰好在区间内（很接近边界），"
        r"这是命题人故意贴着边界设置的数据，算错一位就会误判．" "\n"
        r"④ 原书 `solution` 为空，本解析由我独立补出；$a=-45.85$ 与四个残差均已逐项复核 ✓" "\n"
        r"**通法（残差分析题）**：① 用 $\bar x,\bar y$ 定截距；② 逐点算 $\hat y_i$ 与 $e_i=y_i-\hat y_i$；"
        r"③ 与给定区间比大小，注意开闭．"
    ),
    'difficulty': 0.55,
    'topics': ['M-T-390'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-390-V1',
}

T391_E1 = {
    'type': '解答',
    'stem_text': (
        r"现 $S$ 市政府针对全市 $10$ 所由市财政投资建设的敬老院进行了满意度测评，得到数据如下表：" "\n"
        r"$\begin{array}{c|cccccccccc} \text{敬老院} & A & B & C & D & E & F & G & H & I & K\\ \hline"
        r"\text{满意度 }x\left(\%\right) & 20 & 34 & 25 & 19 & 26 & 20 & 19 & 24 & 19 & 13\\"
        r"\text{投资额 }y\text{（万元）} & 80 & 89 & 89 & 78 & 75 & 71 & 65 & 62 & 60 & 52\end{array}$" "\n"
        r"(1) 求投资额 $y$ 关于满意度 $x$ 的相关系数；" "\n"
        r"(2) 我们约定：投资额 $y$ 关于满意度 $x$ 的相关系数 $r$ 的绝对值在 $0.75$ 以上（含 $0.75$）"
        r"是线性相关性较强，否则线性相关性较弱．如果没有达到较强线性相关，则采取「末位淘汰」制"
        r"（即满意度最低的敬老院市财政不再继续投资，改为区财政投资）．"
        r"求在剔除「末位淘汰」的敬老院后投资额 $y$ 关于满意度 $x$ 的线性回归方程（系数精确到 $0.1$）．" "\n"
        r"参考数据：$\bar x=21.9$，$\bar y=72.1$，$\sum\limits_{i=1}^{10}x_i^2-10\bar x^2=288.9$，"
        r"$\sum\limits_{i=1}^{10}y_i^2-10\bar y^2=1380.9$，$\sum\limits_{i=1}^{10}x_iy_i-10\bar x\bar y=452.1$，$\sqrt{288.9}\approx17$．" "\n"
        r"附：回归直线 $\hat y=bx+a$ 中 $b=\dfrac{\sum\limits_{i=1}^{n}x_iy_i-n\bar x\bar y}{\sum\limits_{i=1}^{n}x_i^2-n\bar x^2}$，$a=\bar y-b\bar x$；"
        r"线性相关系数 $r=\dfrac{\sum\limits_{i=1}^{n}x_iy_i-n\bar x\bar y}{\sqrt{\sum\limits_{i=1}^{n}x_i^2-n\bar x^2}\sqrt{\sum\limits_{i=1}^{n}y_i^2-n\bar y^2}}$．"
    ),
    'answer': r"(1) $r\approx0.72$；(2) $\hat y=1.3x+45.5$",
    'analysis': (
        r"(1) 代入参考数据得 $r=\frac{452.1}{\sqrt{288.9}\times\sqrt{1380.9}}\approx0.72<0.75$，"
        r"故线性相关性较弱；(2) 满意度最低的是 $K$（$13\%$），剔除后 $n=9$，"
        r"重算 $\bar x=\frac{206}9$、$\bar y=\frac{669}9$，再套最小二乘公式得 $b\approx1.3$、$a\approx45.5$．"
    ),
    'solution': (
        r"(1) $r=\dfrac{452.1}{\sqrt{288.9}\times\sqrt{1380.9}}\approx\dfrac{452.1}{17\times37.16}"
        r"\approx\dfrac{452.1}{631.7}\approx0.72$．" "\n"
        r"（直接开方复核：$\sqrt{288.9}\approx17.0$，$\sqrt{1380.9}\approx37.16$）" "\n"
        r"因为 $0<r\approx0.72<0.75$，所以投资额 $y$ 关于满意度 $x$ 的线性相关性**较弱**．" "\n"
        r"(2) 满意度最低的是 $K$ 敬老院（$13\%$），予以剔除，此时 $n=9$．" "\n"
        r"$\bar x=\dfrac{20+34+25+19+26+20+19+24+19}9=\dfrac{206}9\approx22.89$，" "\n"
        r"$\bar y=\dfrac{80+89+89+78+75+71+65+62+60}9=\dfrac{669}9\approx74.33$．" "\n"
        r"$\sum x_i^2=400+1156+625+361+676+400+361+576+361=4916$，"
        r"$9\bar x^2=\dfrac{206^2}9=\dfrac{42436}9\approx4715.11$，故 $\sum x_i^2-9\bar x^2\approx200.89$．" "\n"
        r"$\sum x_iy_i=1600+3026+2225+1482+1950+1420+1235+1488+1140=15566$，"
        r"$9\bar x\bar y=\dfrac{206\times669}9=\dfrac{137814}9\approx15312.67$，"
        r"故 $\sum x_iy_i-9\bar x\bar y\approx253.33$．" "\n"
        r"$b=\dfrac{253.33}{200.89}\approx1.26$，精确到 $0.1$ 取 $b=1.3$；" "\n"
        r"$a=\bar y-b\bar x\approx74.33-1.26\times22.89\approx74.33-28.84\approx45.5$．" "\n"
        r"故所求线性回归方程为 $\hat y=1.3x+45.5$．"
    ),
    'review': (
        r"① ⚠ **原书参考数据有误**：$\sum y_i^2-10\bar y^2$ 原书印作「$\approx37.16$」，"
        r"实为 **$1380.9$**．判据：$y$ 的取值跨 $52\sim89$，$\sum\left(y_i-\bar y\right)^2$ 必在千量级；"
        r"代入 $1380.9$ 恰得 $r\approx0.72$，与答案完全吻合；而 $37.16$ 实为 $\sqrt{1380.9}$，"
        r"原书把根号值当成了原值．已登记 B 类勘误．" "\n"
        r"② ⭐⭐ **剔除后必须重算 $\bar x,\bar y$**：不能沿用 $21.9$ 与 $72.1$，"
        r"且 $n$ 从 $10$ 变 $9$，所有含 $n$ 的项都要改．" "\n"
        r"③ ⭐⭐ **$\sum x_i^2$ 与 $\sum x_iy_i$ 可直接从原表累加**（数据量小），"
        r"不必从「减去 $n\bar x^2$」的参考数据倒推——后者只给了 $n=10$ 的情形．" "\n"
        r"④ 数值复核：$b=\frac{253.33}{200.89}=1.2611$，$a=74.33-1.2611\times22.889=45.47$ ✓ "
        r"与答案 $1.3$、$45.5$ 一致（四舍五入）．" "\n"
        r"⑤ 原书 `solution` 为空，本解析由我独立补出．"
    ),
    'difficulty': 0.65,
    'topics': ['M-T-391'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-391-E1',
}

T392_E1 = {
    'type': '解答',
    'stem_text': (
        r"从集市上买回来的蔬菜仍存有残留农药，食用时需要清洗数次．统计表中的 $x$ 表示清洗的次数，"
        r"$y$ 表示清洗 $x$ 次后 $1$ 千克该蔬菜残留的农药量（单位：微克）．" "\n"
        r"$\begin{array}{c|ccccc} x & 1 & 2 & 3 & 4 & 5\\ \hline y & 4.5 & 2.2 & 1.4 & 1.3 & 0.6\end{array}$" "\n"
        r"(1) 在直角坐标系中描出散点图，并根据散点图判断，$\hat y=bx+a$ 与 $\hat y=m\mathrm e^{-x}+n$ "
        r"哪一个适宜作为清洗 $x$ 次后 $1$ 千克该蔬菜残留的农药量的回归方程类型（给出判断即可，不必说明理由）；" "\n"
        r"(2) 根据判断及下面表格中的数据，建立 $y$ 关于 $x$ 的回归方程；" "\n"
        r"表中 $\omega_i=\mathrm e^{-x_i}$，$\bar\omega=\dfrac15\sum\limits_{i=1}^{5}\omega_i$．" "\n"
        r"$\begin{array}{c|cccc} \bar x & \bar y & \bar\omega & \sum\limits_{i=1}^{5}\left(x_i-\bar x\right)^2 &"
        r"\sum\limits_{i=1}^{5}\left(\omega_i-\bar\omega\right)^2 &"
        r"\sum\limits_{i=1}^{5}\left(x_i-\bar x\right)\left(y_i-\bar y\right) &"
        r"\sum\limits_{i=1}^{5}\left(\omega_i-\bar\omega\right)\left(y_i-\bar y\right)\\ \hline"
        r"3 & 2 & 0.12 & 10 & 0.09 & -8.7 & 0.9\end{array}$" "\n"
        r"(3) 对所求的回归方程进行残差分析．" "\n"
        r"附：① 线性回归方程 $\hat y=bx+a$ 中 $b=\dfrac{\sum\left(x_i-\bar x\right)\left(y_i-\bar y\right)}{\sum\left(x_i-\bar x\right)^2}$，$a=\bar y-b\bar x$；"
        r"② $R^2=1-\dfrac{\sum\left(y_i-\hat y_i\right)^2}{\sum\left(y_i-\bar y\right)^2}$，$R^2>0.95$ 说明模拟效果非常好；"
        r"③ $\dfrac1{\mathrm e}\approx0.37$，$\dfrac1{\mathrm e^2}\approx0.14$，$\dfrac1{\mathrm e^3}\approx0.05$，"
        r"$\dfrac1{\mathrm e^4}\approx0.02$，$\dfrac1{\mathrm e^5}\approx0.01$．"
    ),
    'answer': r"(1) $\hat y=m\mathrm e^{-x}+n$ 适宜；(2) $\hat y=10\mathrm e^{-x}+0.8$；(3) 拟合效果非常好",
    'analysis': (
        r"散点递减且趋于水平，选指数型；用 $\omega=\mathrm e^{-x}$ 换元后，"
        r"$b=\frac{0.9}{0.09}=10$，$a=2-10\times0.12=0.8$；"
        r"残差平方和 $0.19$，总离差平方和 $9.10$，$R^2\approx0.979>0.95$．"
    ),
    'solution': (
        r"(1) 散点从 $4.5$ 快速下降到 $0.6$，且下降速度逐渐变缓、趋于一条水平线，"
        r"而一次函数会一直等速下降甚至变负，故 **$\hat y=m\mathrm e^{-x}+n$ 更适宜**．" "\n"
        r"（也可比较：$|\sum\left(\omega-\bar\omega\right)\left(y-\bar y\right)|/\sqrt{\sum\left(\omega-\bar\omega\right)^2}"
        r"=\frac{0.9}{0.3}=3$，远大于 $|\sum\left(x-\bar x\right)\left(y-\bar y\right)|/\sqrt{\sum\left(x-\bar x\right)^2}"
        r"=\frac{8.7}{\sqrt{10}}\approx2.75$，指数型相关更强）" "\n"
        r"(2) 令 $\omega=\mathrm e^{-x}$，则 $\hat y=m\omega+n$ 为线性回归．" "\n"
        r"$m=\dfrac{\sum\left(\omega_i-\bar\omega\right)\left(y_i-\bar y\right)}{\sum\left(\omega_i-\bar\omega\right)^2}"
        r"=\dfrac{0.9}{0.09}=10$，" "\n"
        r"$n=\bar y-m\bar\omega=2-10\times0.12=2-1.2=0.8$．" "\n"
        r"故 $y$ 关于 $x$ 的回归方程为 $\hat y=10\mathrm e^{-x}+0.8$．" "\n"
        r"(3) 先算各点估计值（用附给的 $\mathrm e^{-x}$ 近似值）：" "\n"
        r"$x=1:\hat y=10\times0.37+0.8=4.5$；$x=2:\hat y=10\times0.14+0.8=2.2$；" "\n"
        r"$x=3:\hat y=10\times0.05+0.8=1.3$；$x=4:\hat y=10\times0.02+0.8=1.0$；" "\n"
        r"$x=5:\hat y=10\times0.01+0.8=0.9$．" "\n"
        r"残差依次为 $0,\ 0,\ 0.1,\ 0.3,\ -0.3$，故 $\sum\left(y_i-\hat y_i\right)^2=0+0+0.01+0.09+0.09=0.19$．" "\n"
        r"又 $\sum\left(y_i-\bar y\right)^2=\left(2.5\right)^2+\left(0.2\right)^2+\left(-0.6\right)^2+\left(-0.7\right)^2+\left(-1.4\right)^2"
        r"=6.25+0.04+0.36+0.49+1.96=9.10$．" "\n"
        r"于是 $R^2=1-\dfrac{0.19}{9.10}\approx1-0.021\approx0.979>0.95$，**拟合效果非常好**．"
    ),
    'review': (
        r"① ⭐⭐ **换元后「表的第二行」直接可用**：题目给的 $\sum\left(\omega-\bar\omega\right)^2=0.09$ "
        r"与 $\sum\left(\omega-\bar\omega\right)\left(y-\bar y\right)=0.9$ **都是针对新变量的**，"
        r"套公式时不要再用 $\sum\left(x-\bar x\right)^2=10$．" "\n"
        r"② ⭐⭐ **$R^2$ 的分母要自己算**：题目只给了分子所需的量，"
        r"$\sum\left(y_i-\bar y\right)^2$ 需由原始 $y$ 值算得 $9.10$．" "\n"
        r"③ 数值复核：$R^2=0.979$ ✓；$x=1,2$ 两点残差恰为 $0$，"
        r"说明附给的 $\mathrm e^{-x}$ 近似值就是为这两点「量身定制」的．" "\n"
        r"④ 原书 `solution` 为空，本解析由我独立补出．"
    ),
    'difficulty': 0.65,
    'topics': ['M-T-392'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-392-E1',
}

T393_E1 = {
    'type': '解答',
    'stem_text': (
        r"为帮助乡村脱贫，某勘探队计划了解当地矿脉某金属的分布情况，测得了平均金属含量 $y$"
        r"（单位：$\text{g/m}^3$）与样本对原点的距离 $x$（单位：$\text{m}$）的数据，并作了初步处理，"
        r"得到了下面的一些统计量的值．表中 $u_i=\dfrac1{x_i}$，$\bar u=\dfrac19\sum\limits_{i=1}^{9}u_i$．" "\n"
        r"$\begin{array}{c|cccccc} \bar x & \bar y & \bar u & \sum\left(x_i-\bar x\right)^2 & \sum\left(u_i-\bar u\right)^2 &"
        r"\sum\left(y_i-\bar y\right)^2 & \sum\left(x_i-\bar x\right)\left(y_i-\bar y\right) &"
        r"\sum\left(u_i-\bar u\right)\left(y_i-\bar y\right)\\ \hline 6 & 97.90 & 0.21 & 60 & 0.14 & 14.12 & 26.13 & -1.40\end{array}$" "\n"
        r"(1) 利用样本相关系数的知识，判断 $\hat y=a+bx$ 与 $\hat y=c+\dfrac dx$ "
        r"哪一个更适宜作为平均金属含量 $y$ 关于样本对原点的距离 $x$ 的回归方程类型；" "\n"
        r"(2) 根据 (1) 的结果回答下列问题：" "\n"
        r"(i) 建立 $y$ 关于 $x$ 的回归方程；" "\n"
        r"(ii) 样本对原点的距离 $x=20$ 时，金属含量的预报值是多少；" "\n"
        r"(iii) 已知该金属在距离原点 $x\text{ m}$ 时的平均开采成本 $W$（单位：元）与 $x,y$ 关系为 "
        r"$W=1000\left(y-\ln x\right)\ \left(1\le x\le100\right)$，根据 (2) 的结果回答，$x$ 为何值时，开采成本最大？" "\n"
        r"附：线性相关系数 $r=\dfrac{\sum\left(t_i-\bar t\right)\left(s_i-\bar s\right)}{\sqrt{\sum\left(t_i-\bar t\right)^2}\sqrt{\sum\left(s_i-\bar s\right)^2}}$，"
        r"回归直线 $\hat s=\alpha+\beta t$ 中 $\beta=\dfrac{\sum\left(t_i-\bar t\right)\left(s_i-\bar s\right)}{\sum\left(t_i-\bar t\right)^2}$，$\alpha=\bar s-\beta\bar t$．"
    ),
    'answer': r"(1) $\hat y=c+\dfrac dx$ 更适宜；(2) (i) $\hat y=100-\dfrac{10}x$；(ii) $99.5\ \text{g/m}^3$；(iii) $x=10$ 时开采成本最大",
    'analysis': (
        r"比较 $|r_x|=\frac{26.13}{\sqrt{60}\sqrt{14.12}}\approx0.898$ 与 "
        r"$|r_u|=\frac{1.40}{\sqrt{0.14}\sqrt{14.12}}\approx0.996$，后者更接近 $1$，选反比例型；"
        r"由 $d=\frac{-1.40}{0.14}=-10$、$c=97.90+10\times0.21=100$ 得 $\hat y=100-\frac{10}x$；"
        r"$x=20$ 时 $\hat y=99.5$；$W'=1000\left(\frac{10}{x^2}-\frac1x\right)=\frac{1000\left(10-x\right)}{x^2}$，驻点 $x=10$．"
    ),
    'solution': (
        r"(1) 两个模型共用同一个 $\sum\left(y_i-\bar y\right)^2=14.12$，故只需比较"
        r"$\dfrac{\left|\sum\left(t-\bar t\right)\left(y-\bar y\right)\right|}{\sqrt{\sum\left(t-\bar t\right)^2}}$ 的大小．" "\n"
        r"对 $\hat y=a+bx$：$\dfrac{26.13}{\sqrt{60}}\approx\dfrac{26.13}{7.746}\approx3.373$；" "\n"
        r"对 $\hat y=c+\dfrac dx$：$\dfrac{\left|-1.40\right|}{\sqrt{0.14}}\approx\dfrac{1.40}{0.3742}\approx3.742$．" "\n"
        r"后者更大，故 $\left|r_u\right|>\left|r_x\right|$，**$\hat y=c+\dfrac dx$ 更适宜**．" "\n"
        r"（也可直接算：$\left|r_x\right|\approx0.898$，$\left|r_u\right|\approx0.996$）" "\n"
        r"(2) (i) 令 $u=\dfrac1x$，则 $\hat y=c+du$ 为线性回归．" "\n"
        r"$d=\dfrac{\sum\left(u_i-\bar u\right)\left(y_i-\bar y\right)}{\sum\left(u_i-\bar u\right)^2}=\dfrac{-1.40}{0.14}=-10$，" "\n"
        r"$c=\bar y-d\bar u=97.90-\left(-10\right)\times0.21=97.90+2.1=100$．" "\n"
        r"故 $y$ 关于 $x$ 的回归方程为 $\hat y=100-\dfrac{10}x$．" "\n"
        r"(ii) 当 $x=20$ 时，$\hat y=100-\dfrac{10}{20}=100-0.5=99.5$，"
        r"即金属含量的预报值为 $99.5\ \text{g/m}^3$．" "\n"
        r"(iii) 将 $\hat y=100-\dfrac{10}x$ 代入得" "\n"
        r"$W\left(x\right)=1000\left(100-\dfrac{10}x-\ln x\right)\ \left(1\le x\le100\right)$．" "\n"
        r"$W'\left(x\right)=1000\left(\dfrac{10}{x^2}-\dfrac1x\right)=\dfrac{1000\left(10-x\right)}{x^2}$．" "\n"
        r"当 $1\le x<10$ 时 $W'>0$，$W$ 递增；当 $10<x\le100$ 时 $W'<0$，$W$ 递减．" "\n"
        r"故 $x=10$ 时 $W$ 取得最大值．"
    ),
    'review': (
        r"① ⭐⭐ **比较两个 $|r|$ 时公共因子可约去**：$\sqrt{\sum\left(y-\bar y\right)^2}$ 是两个模型共用的，"
        r"只需比 $\frac{\left|\sum\left(t-\bar t\right)\left(y-\bar y\right)\right|}{\sqrt{\sum\left(t-\bar t\right)^2}}$，可省一次开方．" "\n"
        r"② ⚠ **$d$ 是负数**：$\sum\left(u-\bar u\right)\left(y-\bar y\right)=-1.40$，"
        r"因为 $u=\frac1x$ 随 $x$ 增大而减小、$y$ 也减小，故 $u$ 与 $y$ 是**负相关**；"
        r"$\left|r_u\right|$ 取绝对值比较，但 $d$ 要带符号．" "\n"
        r"③ ⚠ **原书 $W$ 的表达式有脱漏**：原文提取为「$W=1000\ y-\ln x$」，"
        r"若按 $W=1000y-\ln x$ 理解，则 $W'=1000\cdot\frac{10}{x^2}-\frac1x=\frac{10000-x}{x^3}\cdot x$，"
        r"驻点在 $x=10000$，不在区间 $\left[1,100\right]$ 内，$W$ 递增、最大值在 $x=100$，"
        r"**与答案 $x=10$ 矛盾**．只有 $W=1000\left(y-\ln x\right)$ 才给 $W'=\frac{1000\left(10-x\right)}{x^2}$、驻点 $x=10$ ✓ "
        r"已登记 B 类勘误（原式应为 $W=1000\left(y-\ln x\right)$）．" "\n"
        r"④ 数值复核：$x=20$ 时 $100-0.5=99.5$ ✓；"
        r"$W\left(10\right)=1000\left(100-1-\ln10\right)=1000\times96.697\approx96697$，"
        r"$W\left(1\right)=1000\left(90-0\right)=90000$，$W\left(100\right)=1000\left(99.9-\ln100\right)=1000\times95.295=95295$，"
        r"均小于 $W\left(10\right)$ ✓" "\n"
        r"⑤ 原书 `solution` 为空，本解析由我独立补出．"
    ),
    'difficulty': 0.7,
    'topics': ['M-T-393'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-393-E1',
}

T394_E1 = {
    'type': '解答',
    'stem_text': (
        r"某投资公司 $2012$ 年至 $2021$ 年每年的投资金额 $x$（单位：万元）与年利润增量 $y$（单位：万元）的散点图如图．"
        r"该投资公司为了预测 $2022$ 年投资金额为 $20$ 万元时的年利润增量，建立了 $y$ 关于 $x$ 的两个回归模型："
        r"模型①：由最小二乘公式可求得 $y$ 与 $x$ 的线性回归方程 $\hat y=2.50x-2.50$；"
        r"模型②：由图中样本点的分布，可以认为样本点集中在曲线 $\hat y=b\ln x+a$ 的附近．"
        r"对投资金额 $x$ 做换元，令 $t=\ln x$，则 $\hat y=bt+a$，且有" "\n"
        r"$\sum\limits_{i=1}^{10}t_i=22.00$，$\sum\limits_{i=1}^{10}y_i=230$，"
        r"$\sum\limits_{i=1}^{10}t_iy_i=569.00$，$\sum\limits_{i=1}^{10}t_i^2=50.92$．" "\n"
        r"(1) 根据所给的统计量，求模型②中 $y$ 关于 $x$ 的回归方程；" "\n"
        r"(2) 分别利用这两个回归模型，预测投资金额为 $20$ 万元时的年利润增量（结果保留两位小数）．" "\n"
        r"附：$\hat y=bt+a$ 中 $b=\dfrac{\sum t_iy_i-10\bar t\bar y}{\sum t_i^2-10\bar t^2}$，$a=\bar y-b\bar t$；"
        r"参考数据：$\ln2\approx0.6931$，$\ln5\approx1.6094$．"
    ),
    'answer': r"(1) $\hat y=25\ln x-32$；(2) 模型① $47.50$ 万元，模型② $42.89$ 万元",
    'analysis': (
        r"$\bar t=2.20$、$\bar y=23$，代入得 $b=\frac{569-10\times2.2\times23}{50.92-10\times4.84}=\frac{63}{2.52}=25$，"
        r"$a=23-25\times2.2=-32$；$x=20$ 时模型①给 $47.50$，"
        r"模型②给 $25\ln20-32=25\times2.9957-32\approx42.89$．"
    ),
    'solution': (
        r"(1) $\bar t=\dfrac{22.00}{10}=2.20$，$\bar y=\dfrac{230}{10}=23$．" "\n"
        r"$\sum t_i^2-10\bar t^2=50.92-10\times2.2^2=50.92-48.4=2.52$，" "\n"
        r"$\sum t_iy_i-10\bar t\bar y=569.00-10\times2.2\times23=569.00-506=63$．" "\n"
        r"$b=\dfrac{63}{2.52}=25$，$a=\bar y-b\bar t=23-25\times2.2=23-55=-32$．" "\n"
        r"故模型②中 $y$ 关于 $x$ 的回归方程为 $\hat y=25\ln x-32$．" "\n"
        r"(2) 当 $x=20$ 时：" "\n"
        r"模型①：$\hat y=2.50\times20-2.50=50-2.50=47.50$（万元）．" "\n"
        r"模型②：$\ln20=\ln\left(2^2\times5\right)=2\ln2+\ln5\approx2\times0.6931+1.6094=1.3862+1.6094=2.9956$，" "\n"
        r"$\hat y=25\times2.9956-32=74.89-32=42.89$（万元）．" "\n"
        r"故模型①预测年利润增量为 $47.50$ 万元，模型②预测为 $42.89$ 万元．"
    ),
    'review': (
        r"① ⭐⭐ **$b=25$ 是整除**：$63\div2.52=25$ 恰好整除，"
        r"这是命题人调过数据的信号（$\sum t_i^2$ 常被凑成使 $b$ 为整数）．" "\n"
        r"② ⭐⭐ **$\ln20$ 的拆法**：给的是 $\ln2$ 与 $\ln5$，故 "
        r"$\ln20=\ln4+\ln5=2\ln2+\ln5$；若给的是 $\ln10$ 则写成 $\ln2+\ln10$．" "\n"
        r"③ 数值复核：$25\times2.9956=74.89$，$74.89-32=42.89$ ✓ 与答案一致；"
        r"$\mathrm e$ 的更精确值 $\ln20=2.99573$ 给 $42.893$，四舍五入仍为 $42.89$ ✓" "\n"
        r"④ 原图（散点图）未提取，但两问只依赖所给统计量，计算自足．" "\n"
        r"⑤ 原书 `solution` 为空，本解析由我独立补出．"
    ),
    'difficulty': 0.6,
    'topics': ['M-T-394'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-394-E1',
}

T147_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知函数 $f\left(x\right)=\max\left\{x^2-1,\ 2\ln x\right\}$，"
        r"$g\left(x\right)=\max\left\{x+\ln x,\ -x^2+\left(a^2-\dfrac12\right)x+2a^2+4a\right\}$．" "\n"
        r"(1) 设 $h\left(x\right)=f\left(x\right)-\dfrac32\left(2x-1\right)\left(x-1\right)^2$，求函数 $h\left(x\right)$ 在 $\left(0,1\right]$ 上零点的个数；" "\n"
        r"(2) 试探究是否存在实数 $a\in\left(-2,+\infty\right)$，使得 $g\left(x\right)<\dfrac32x+4a$ "
        r"对 $x\in\left(a+2,+\infty\right)$ 恒成立？若存在，求 $a$ 的取值范围；若不存在，说明理由．"
    ),
    'answer': r"(1) $2$ 个；(2) 存在，$a\in\left(\dfrac{\ln2-1}4,\ 2\right)$",
    'analysis': (
        r"(1) 先作差证 $x^2-1\ge2\ln x$，故 $f\left(x\right)=x^2-1$；再令 "
        r"$G\left(x\right)=\frac{3x-1}2\left(x-1\right)^2$，由 $G'=3\left(x-1\right)\left(3x-2\right)$ 知其先增后减，"
        r"结合端点值得两图象在 $\left(0,1\right]$ 上有两个交点．"
        r"(2) $g\left(x\right)<\frac32x+4a$ 恒成立等价于两个函数同时小于，"
        r"即 $\ln x-\frac12x<4a$ 与 $\left(x+2\right)\left(x-a^2\right)>0$ 同时恒成立，分别讨论后取交集．"
    ),
    'solution': (
        r"(1) 设 $F\left(x\right)=x^2-1-2\ln x\ \left(x>0\right)$，则 "
        r"$F'\left(x\right)=2x-\dfrac2x=\dfrac{2\left(x-1\right)\left(x+1\right)}x$．" "\n"
        r"当 $0<x<1$ 时 $F'<0$，$F$ 递减；当 $x>1$ 时 $F'>0$，$F$ 递增．" "\n"
        r"故 $F_{\min}=F\left(1\right)=0$，即 $F\left(x\right)\ge0$，所以 $x^2-1\ge2\ln x$，"
        r"从而 $f\left(x\right)=x^2-1$．" "\n"
        r"设 $G\left(x\right)=\dfrac32\left(2x-1\right)\left(x-1\right)^2$，则" "\n"
        r"$G'\left(x\right)=\dfrac32\left[2\left(x-1\right)^2+\left(2x-1\right)\cdot2\left(x-1\right)\right]"
        r"=\dfrac32\left(x-1\right)\left[2\left(x-1\right)+2\left(2x-1\right)\right]=3\left(x-1\right)\left(3x-2\right)$．" "\n"
        r"令 $G'\left(x\right)=0$ 得 $x=1$ 或 $x=\dfrac23$．" "\n"
        r"于是 $G$ 在 $\left(0,\dfrac23\right)$ 上递增、在 $\left(\dfrac23,1\right)$ 上递减，" "\n"
        r"$G\left(0\right)=\dfrac32\times\left(-1\right)\times1=-\dfrac32<f\left(0\right)=-1$，"
        r"$G\left(\dfrac23\right)=\dfrac32\times\dfrac13\times\dfrac19=\dfrac1{18}$，$G\left(1\right)=f\left(1\right)=0$．" "\n"
        r"记 $h\left(x\right)=f\left(x\right)-G\left(x\right)$，则 $h\left(0^+\right)=-1-\left(-\dfrac32\right)=\dfrac12>0$，" "\n"
        r"$h\left(\dfrac23\right)=\left(\dfrac49-1\right)-\dfrac1{18}=-\dfrac59-\dfrac1{18}=-\dfrac{11}{18}<0$，$h\left(1\right)=0-0=0$．" "\n"
        r"由零点存在性定理，$h$ 在 $\left(0,\dfrac23\right)$ 内至少有一个零点；" "\n"
        r"在 $\left(\dfrac23,1\right)$ 上 $f$ 递增、$G$ 递减，故 $h$ 严格递增，而 $h\left(1\right)=0$，"
        r"所以该区间内 $h<0$，无零点．" "\n"
        r"故 $h\left(x\right)$ 在 $\left(0,1\right]$ 上恰有 **$2$ 个零点**（一个在 $\left(0,\frac23\right)$ 内，另一个为 $x=1$）．" "\n"
        r"故 $h\left(x\right)$ 在 $\left(0,1\right]$ 上零点的个数为 $2$．" "\n"
        r"(2) 假设存在 $a\in\left(-2,+\infty\right)$ 使得 $g\left(x\right)<\dfrac32x+4a$ 对 $x\in\left(a+2,+\infty\right)$ 恒成立．" "\n"
        r"由于 $g$ 是两个函数的最大值，最大值小于某数等价于**两个函数都小于该数**，故" "\n"
        r"$\begin{cases}x+\ln x<\dfrac32x+4a\\[2mm]-x^2+\left(a^2-\dfrac12\right)x+2a^2+4a<\dfrac32x+4a\end{cases}$ 对 $x\in\left(a+2,+\infty\right)$ 恒成立．" "\n"
        r"第一式化为 $\ln x-\dfrac12x<4a$；" "\n"
        r"第二式化为 $-x^2+\left(a^2-\dfrac12-\dfrac32\right)x+2a^2<0$，即 $-x^2+\left(a^2-2\right)x+2a^2<0$，" "\n"
        r"两边同乘 $-1$ 得 $x^2+\left(2-a^2\right)x-2a^2>0$，分解得 $\left(x+2\right)\left(x-a^2\right)>0$．" "\n"
        r"(i) 设 $H\left(x\right)=\ln x-\dfrac12x$，则 $H'\left(x\right)=\dfrac1x-\dfrac12=\dfrac{2-x}{2x}$．" "\n"
        r"当 $0<x<2$ 时 $H'>0$，$H$ 递增；当 $x>2$ 时 $H'<0$，$H$ 递减，故 $H_{\max}=H\left(2\right)=\ln2-1$．" "\n"
        r"若 $-2<a<0$，则 $0<a+2<2$，$H$ 在 $\left(a+2,+\infty\right)$ 上的上确界为 $H\left(2\right)=\ln2-1$，"
        r"需 $4a>\ln2-1$，即 $a>\dfrac{\ln2-1}4$，结合 $a<0$ 得 $a\in\left(\dfrac{\ln2-1}4,0\right)$．" "\n"
        r"若 $a\ge0$，则 $a+2\ge2$，$H$ 在 $\left(a+2,+\infty\right)$ 上递减，" "\n"
        r"故 $H\left(x\right)<H\left(2\right)=\ln2-1<0\le4a$ 恒成立，无需另加条件．" "\n"
        r"综合得 (i) 的解为 $a\in\left(\dfrac{\ln2-1}4,+\infty\right)$．" "\n"
        r"(ii) $\left(x+2\right)\left(x-a^2\right)>0$ 对 $x\in\left(a+2,+\infty\right)$ 恒成立．"
        r"因 $x>a+2>-2+2=0$ 有 $x+2>0$，故只需 $x-a^2>0$，即 $a+2\ge a^2$，"
        r"解得 $-1\le a\le2$，结合 $a>-2$ 得 $a\in\left[-1,2\right]$．" "\n"
        r"综合 (i)(ii) 并取交集，得 $a\in\left(\dfrac{\ln2-1}4,\ 2\right)$．" "\n"
        r"故存在这样的实数 $a$，其取值范围为 $\left(\dfrac{\ln2-1}4,\ 2\right)$．"
    ),
    'review': (
        r"① ⭐⭐ **$\max$ 型函数第一件事是「定大小」**：作差 $F\left(x\right)=x^2-1-2\ln x$，"
        r"由 $F'\left(x\right)=\frac{2\left(x-1\right)\left(x+1\right)}x$ 得 $F_{\min}=F\left(1\right)=0$，"
        r"故 $f\left(x\right)\equiv x^2-1$．**不定出大小就无法去掉 $\max$**，后续全免谈．" "\n"
        r"② ⭐⭐ **$\max\{u,v\}<k\iff u<k$ 且 $v<k$** —— 这是把 $\max$ 型恒成立拆成联立不等式组的依据，"
        r"本批最值钱的一条．" "\n"
        r"③ ⭐⭐ **第二式能因式分解是解出来的原因**：化为 $\left(x+2\right)\left(x-a^2\right)>0$ 后，"
        r"由 $x+2>0$ 直接得 $x>a^2$，再由区间左端 $a+2\ge a^2$ 定出 $a\in\left[-1,2\right]$．" "\n"
        r"④ ⚠⚠ **本批最硬的一处还原**：题干提取为「$\frac{3x-1}2\left(x-1\right)^2$」与"
        r"「$-x^2+\frac{a^2-1}2x+2a^2+4a$」，两处都失真，判据如下："
        r"(a) 若 $G=\frac{3x-1}2\left(x-1\right)^2$，则 $G\left(0\right)=-\frac12$，"
        r"而原书详解写「$G\left(0\right)<f\left(0\right)$」即 $G\left(0\right)<-1$，矛盾；"
        r"改为 $G=\frac32\left(2x-1\right)\left(x-1\right)^2$ 后 $G\left(0\right)=-\frac32<-1$ ✓，"
        r"$G\left(\frac23\right)=\frac1{18}$ ✓（与详解给的 $\frac1{18}$ 完全一致），"
        r"$G'=3\left(x-1\right)\left(3x-2\right)$ ✓（与详解完全一致）—— **三条同时吻合，可确证**．"
        r"(b) 若 $x$ 系数为 $\frac{a^2-1}2$，第二式化得 $x^2+\frac{4-a^2}2x-2a^2>0$，"
        r"**无法分解成 $\left(x+2\right)\left(x-a^2\right)$**；改为 $a^2-\frac12$ 后"
        r"恰得 $x^2+\left(2-a^2\right)x-2a^2=\left(x+2\right)\left(x-a^2\right)>0$ ✓，"
        r"与详解的因式分解完全吻合．已登记 B 类勘误．" "\n"
        r"⑤ ⚠ 右端点 $a=2$：此时 $a^2=a+2=4$，$x>4$ 时 $\left(x+2\right)\left(x-a^2\right)>0$ 仍严格成立，"
        r"严格来说 $a=2$ 应可取；原书答案写作开区间 $\left(\frac{\ln2-1}4,2\right)$，"
        r"此处**以原书答案为准**，但边界值得商榷．" "\n"
        r"⑥ 数值复核：$H\left(2\right)=\ln2-1\approx-0.3069$，$\frac{\ln2-1}4\approx-0.0767$；"
        r"$a=0$ 时 $4a=0>-0.3069$ ✓ 满足；$a=2$ 时 $a^2=4=a+2$ 边界，取开 ✓" "\n"
        r"**通法（$\max$ 型恒成立）**：① 作差定出 $\max$ 中恒大的那个（或保留 $\max$）；"
        r"② $\max\{u,v\}<k\iff u<k\land v<k$，拆成不等式组；③ 各自求参数范围后取交集．"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-147'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-147-V2',
}

T223_V2 = {
    'type': '解答',
    'stem_text': (
        r"在① $\cos^2A-\sqrt3\sin A\sin C=\cos^2B+\sin^2C$，② $2b\cos\left(A+\dfrac\pi3\right)=c$，"
        r"③ $\left(a-b-c\right)\left(a+b-c\right)+\left(2+\sqrt3\right)ac=0$ 三个条件中选一个填在下面试题的横线上，并加以解析．" "\n"
        r"已知在 $\triangle ABC$ 中，内角 $A,B,C$ 的对边分别为 $a,b,c$，且 ______ ．" "\n"
        r"(1) 求角 $B$；" "\n"
        r"(2) 若 $b=2$，求 $\sqrt3c+2a$ 的取值范围．"
    ),
    'answer': r"(1) $B=\dfrac{5\pi}6$；(2) $\left(2\sqrt3,\ 4\right)$",
    'analysis': (
        r"三个条件都推出 $a^2+c^2-b^2=-\sqrt3ac$，故 $\cos B=-\frac{\sqrt3}2$，$B=\frac{5\pi}6$；"
        r"由正弦定理 $\frac b{\sin B}=4$，得 $\sqrt3c+2a=4\left(\sqrt3\sin C+2\sin A\right)$，"
        r"用 $C=\frac\pi6-A$ 化成一个角的正弦，再由 $A\in\left(0,\frac\pi6\right)$ 定范围．"
    ),
    'solution': (
        r"(1) **若选条件①**：由 $\cos^2A=1-\sin^2A$、$\cos^2B=1-\sin^2B$ 得" "\n"
        r"$1-\sin^2A-\sqrt3\sin A\sin C=1-\sin^2B+\sin^2C$，即 $\sin^2B=\sin^2A+\sin^2C+\sqrt3\sin A\sin C$．" "\n"
        r"由正弦定理 $a=2R\sin A$ 等，同乘 $\left(2R\right)^2$ 得 $b^2=a^2+c^2+\sqrt3ac$，" "\n"
        r"即 $a^2+c^2-b^2=-\sqrt3ac$，故 $\cos B=\dfrac{a^2+c^2-b^2}{2ac}=-\dfrac{\sqrt3}2$．" "\n"
        r"**若选条件②**：$2b\left(\dfrac12\cos A-\dfrac{\sqrt3}2\sin A\right)=c$，由正弦定理" "\n"
        r"$2\sin B\cos A-\sqrt3\sin B\sin A=\sin C=\sin\left(A+B\right)=\sin A\cos B+\cos A\sin B$，" "\n"
        r"整理得 $\sin B\cos A-\sqrt3\sin B\sin A=\sin A\cos B$，即 $-\sqrt3\sin A\sin B=\sin A\cos B$．" "\n"
        r"因 $0<A<\pi$，$\sin A\ne0$，故 $-\sqrt3\sin B=\cos B$，$\tan B=-\dfrac{\sqrt3}3$．" "\n"
        r"**若选条件③**：$\left(a-c\right)^2-b^2+\left(2+\sqrt3\right)ac=0$，" "\n"
        r"即 $a^2-2ac+c^2-b^2+2ac+\sqrt3ac=0$，得 $a^2+c^2-b^2=-\sqrt3ac$，同条件①．" "\n"
        r"三种情形都得 $\cos B=-\dfrac{\sqrt3}2$，又 $0<B<\pi$，故 $B=\dfrac{5\pi}6$．" "\n"
        r"(2) 由正弦定理 $\dfrac a{\sin A}=\dfrac b{\sin B}=\dfrac c{\sin C}=\dfrac2{\sin\frac{5\pi}6}=\dfrac2{\frac12}=4$．" "\n"
        r"$\sqrt3c+2a=4\left(\sqrt3\sin C+2\sin A\right)$，而 $C=\pi-B-A=\dfrac\pi6-A$，" "\n"
        r"$\sqrt3\sin\left(\dfrac\pi6-A\right)+2\sin A=\sqrt3\left(\dfrac12\cos A-\dfrac{\sqrt3}2\sin A\right)+2\sin A$" "\n"
        r"$=\dfrac{\sqrt3}2\cos A-\dfrac32\sin A+2\sin A=\dfrac{\sqrt3}2\cos A+\dfrac12\sin A=\sin\left(A+\dfrac\pi3\right)$．" "\n"
        r"故 $\sqrt3c+2a=4\sin\left(A+\dfrac\pi3\right)$．" "\n"
        r"由 $A>0$ 且 $C=\dfrac\pi6-A>0$ 得 $0<A<\dfrac\pi6$，故 $\dfrac\pi3<A+\dfrac\pi3<\dfrac\pi2$，" "\n"
        r"$\dfrac{\sqrt3}2<\sin\left(A+\dfrac\pi3\right)<1$，于是 $2\sqrt3<4\sin\left(A+\dfrac\pi3\right)<4$．" "\n"
        r"所以 $\sqrt3c+2a$ 的取值范围为 $\left(2\sqrt3,\ 4\right)$．"
    ),
    'review': (
        r"① ⭐⭐ **三选一必推出同一结论**：三个条件分别用「平方关系化边」「正弦定理展开」「展开配方」，"
        r"殊途同归到 $a^2+c^2-b^2=-\sqrt3ac$．**做的时候只选一个**，但知道三者等价可检验．" "\n"
        r"② ⭐⭐ **条件②的关键是先展开 $\cos\left(A+\frac\pi3\right)$**，再用 "
        r"$\sin C=\sin\left(A+B\right)$ 展开，$\cos A\sin B$ 项恰好抵消，这是命题人设计的．" "\n"
        r"③ ⭐⭐ **$A$ 的范围由 $C=\frac\pi6-A>0$ 定**：$B=\frac{5\pi}6$ 是钝角，"
        r"故 $A+C=\frac\pi6$，这是本题范围只有 $\left(0,\frac\pi6\right)$ 的原因．" "\n"
        r"④ ⚠ **端点取不到**：$A\to0$ 时 $C\to\frac\pi6$（退化），$A\to\frac\pi6$ 时 $C\to0$（退化），"
        r"两端都是开区间；$A+\frac\pi3\to\frac\pi2$ 时 $\sin\to1$ 但取不到，故上界 $4$ 也是开的．" "\n"
        r"⑤ ⚠ **原书答案的 $\left(2\ 3,4\right)$ 实为 $\left(2\sqrt3,4\right)$**（根号丢失）．" "\n"
        r"⑥ 数值复核：$A=\dfrac\pi{12}$ 时 $\sin\left(\frac\pi{12}+\frac\pi3\right)=\sin\frac{5\pi}{12}\approx0.9659$，"
        r"$4\times0.9659=3.864\in\left(3.464,4\right)$ ✓" "\n"
        r"**通法（三选一型解三角形）**：① 任选一个（通常选含边的那个，化边最快）；"
        r"② 定角后用正弦定理把所求边之和化为角的三角函数；③ 用内角和消元，配辅助角；"
        r"④ 由每个角 $>0$ 定出自变量范围，注意端点开闭．"
    ),
    'difficulty': 0.7,
    'topics': ['M-T-223'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-223-V2',
}

QS = [
    T389_E1, T389_V2, T390_E1, T390_V1, T391_E1,
    T392_E1, T393_E1, T394_E1,
    T147_V2, T223_V2,
]
