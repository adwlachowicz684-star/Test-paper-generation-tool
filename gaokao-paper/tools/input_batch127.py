# -*- coding: utf-8 -*-
r"""第 127 批：统计回归（M-T-391 ×2、M-T-389、M-T-395，4 题）
+ 数列（M-T-268-V2、M-T-257-V2、M-T-274-E1，3 题）
+ 绝对值（M-T-031-E1/V2，2 题）
+ 三角（M-T-182-V2，1 题）+ 双曲线（M-T-361-V1，1 题）+ 导数（M-T-145-E1，1 题）

    python3 tools/run_batch.py 127
"""

T391_V1 = {
    'type': '解答',
    'stem_text': (
        r"BMI 指数是用体重公斤数除以身高米数的平方得出的数值，是国际上常用的衡量人体胖瘦程度以及是否健康的一个标准．"
        r"对于高中男体育特长生而言，当 BMI 数值大于或等于 $20.5$ 时，我们说体重较重，当 BMI 数值小于 $20.5$ 时，我们说体重较轻；"
        r"身高大于或等于 $170\rm\,cm$ 时，我们说身高较高，身高小于 $170\rm\,cm$ 时，我们说身高较矮．"
        r"某中小学生成长与发展机构从某市的 $320$ 名高中男体育特长生中随机选取 $8$ 名，其身高和体重的数据如下表所示：" "\n"
        r"编号 $i$：$1,2,3,4,5,6,7,8$；" "\n"
        r"身高 $(\rm cm)\,x_i$：$166,167,160,173,178,169,158,173$；" "\n"
        r"体重 $(\rm kg)\,y_i$：$57,58,53,61,66,57,50,66$．" "\n"
        r"（1）根据最小二乘法的思想与公式求得线性回归方程 $\hat y=0.8x-75.9$．"
        r"利用已经求得的线性回归方程，请完善下列残差表（表中已给出 $e_1=0.1,\ e_2=0.3,\ e_3=0.9,\ e_4=-1.5,\ e_5=-0.5$），"
        r"并求解释变量（身高）对于预报变量（体重）变化的贡献值 $R^2$（保留两位有效数字）；" "\n"
        r"（2）通过残差分析，对于残差的最大（绝对值）的那组数据，需要确认在样本点的采集中是否有人为的错误．"
        r"已知通过重新采集发现，该组数据的体重应该为 $58(\rm kg)$．"
        r"请重新根据最小二乘法的思想与公式，求出男体育特长生的身高与体重的线性回归方程．" "\n"
        r"参考公式：$R^{2}=1-\dfrac{\sum\limits_{i=1}^{n}\left(y_i-\hat y_i\right)^{2}}{\sum\limits_{i=1}^{n}\left(y_i-\bar y\right)^{2}}$．"
    ),
    'opts': [],
    'answer': (
        r"（1）残差表补全为 $e_6=-2.3,\ e_7=-0.5,\ e_8=3.5$；$R^{2}\approx0.90$；"
        r"（2）$\hat y=0.675x-55.9$．"
    ),
    'analysis': (
        r"（1）由 $\hat y=0.8x-75.9$ 逐项算 $e_i=y_i-\hat y_i$ 补全残差表，"
        r"再代入 $R^2$ 公式（分母 $\sum(y_i-\bar y)^2=226$）；"
        r"（2）残差绝对值最大的是第 $8$ 组（$|e_8|=3.5$），把 $y_8$ 由 $66$ 改为 $58$，"
        r"用「修正 $\sum x_iy_i$」的技巧 $\sum x_iy_i^{\ast}=78880-173\times66+173\times58=77496$，再套最小二乘公式．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"由 $\hat y=0.8x-75.9$，得" "\n"
        r"$e_6=57-0.8\times169+75.9=-2.3$，"
        r"$e_7=50-0.8\times158+75.9=-0.5$，"
        r"$e_8=66-0.8\times173+75.9=3.5$．" "\n"
        r"（前五项 $0.1,\,0.3,\,0.9,\,-1.5,\,-0.5$ 题已给出，可核对：$e_1=57-0.8\times166+75.9=0.1$ ✓）" "\n"
        r"又 $\bar y=\dfrac{57+58+53+61+66+57+50+66}{8}=\dfrac{468}{8}=58.5$，" "\n"
        r"$\sum\limits_{i=1}^{8}\left(y_i-\bar y\right)^{2}=0.25+0.25+30.25+6.25+56.25+2.25+72.25+56.25=226$．" "\n"
        r"$\sum\limits_{i=1}^{8}e_i^{2}=0.01+0.09+0.81+2.25+0.25+5.29+0.25+12.25=21.2$．" "\n"
        r"所以 $\boxed{R^{2}=1-\dfrac{21.2}{226}\approx0.90}$．" "\n"
        r"**第（2）问**" "\n"
        r"由残差表知 $|e_8|=3.5$ 最大，故第 $8$ 组数据需重采，修正后 $y_8^{\ast}=58$．" "\n"
        r"由 $\sum\limits_{i=1}^{8}x_i^{2}=226112$，$\bar x=\dfrac{166+167+160+173+178+169+158+173}{8}=168$，" "\n"
        r"原 $\sum\limits_{i=1}^{8}x_iy_i=78880$，故修正后" "\n"
        r"$\sum\limits_{i=1}^{8}x_iy_i^{\ast}=78880-173\times66+173\times58=78880-1384=77496$．" "\n"
        r"又 $\bar y^{\ast}=\dfrac{468-66+58}{8}=\dfrac{460}{8}=57.5$．" "\n"
        r"$\hat b=\dfrac{\sum x_iy_i^{\ast}-8\bar x\bar y^{\ast}}{\sum x_i^{2}-8\bar x^{2}}=\dfrac{77496-8\times168\times57.5}{226112-8\times168^{2}}=\dfrac{77496-77280}{226112-225792}=\dfrac{216}{320}=0.675$．" "\n"
        r"$\hat a=\bar y^{\ast}-\hat b\,\bar x=57.5-0.675\times168=57.5-113.4=-55.9$．" "\n"
        r"所以 $\boxed{\hat y=0.675x-55.9}$．"
    ),
    'review': (
        r"① ⭐⭐ **修正 $\sum x_iy_i$ 的「只改一项」技巧**："
        r"$\sum x_iy_i^{\ast}=\sum x_iy_i-x_8(y_8-y_8^{\ast})=78880-173\times8=77496$，"
        r"**不必把 $8$ 项重算一遍**．同理 $\bar y^{\ast}=\bar y-\frac{66-58}{8}=58.5-1=57.5$ ✓" "\n"
        r"② ⭐⭐ **$R^2$ 的分母是 $\sum(y_i-\bar y)^2$ 不是 $\sum y_i^2$**，"
        r"分子是 $\sum e_i^2=\sum(y_i-\hat y_i)^2$——两个「偏差」的对象不同，最易混．" "\n"
        r"③ 数值复核：$\sum e_i^2=21.2$，$\frac{21.2}{226}=0.0938$，$R^2=0.9062\approx0.90$ ✓；"
        r"$\hat b=\frac{216}{320}=0.675$ 恰为有限小数，说明数据是按此设计的 ✓" "\n"
        r"④ 校验（2）：用 $\hat y=0.675x-55.9$ 预测 $x=168$ 得 $57.5=\bar y^{\ast}$ ✓（回归直线必过 $(\bar x,\bar y)$）" "\n"
        r"**通法（回归 + 残差）**：" "\n"
        r"① 残差 $e_i=y_i-\hat y_i$，补全残差表只需代回归方程；" "\n"
        r"② 数据修正题只改「含该点的那一项」，其余用原统计量；" "\n"
        r"③ 回归直线必过 $(\bar x,\bar y)$，这是检验 $a,b$ 最快的办法；" "\n"
        r"④ $R^2$ 越接近 $1$ 拟合越好，其分子是残差平方和．"
    ),
    'difficulty': 0.62,
    'topics': ['M-T-391'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-391-V1',
}

T391_V2 = {
    'type': '解答',
    'stem_text': (
        r"某手机公司生产某款手机，如果年返修率不超过千分之一，则生产部门当年考核优秀．"
        r"现获得该公司 $2010-2018$ 年的相关数据如下表所示：" "\n"
        r"年份：$2010,2011,2012,2013,2014,2015,2016,2017,2018$；" "\n"
        r"年生产量（万台）$x$：$3,4,5,6,7,7,9,10,12$；" "\n"
        r"产品年利润（千万元）$y$：$3.6,4.1,4.4,5.2,6.2,7.8,7.5,7.9,9.1$；" "\n"
        r"年返修量（台）：$47,42,48,50,92,83,72,87,90$．" "\n"
        r"（1）从该公司 $2010-2018$ 年的相关数据中任意选取 $3$ 年的数据，以 $X$ 表示 $3$ 年中生产部门获得考核优秀的次数，"
        r"求 $X$ 的分布列和数学期望；" "\n"
        r"（2）根据散点图发现 $2015$ 年数据偏差较大，如果去掉该年的数据，"
        r"试用剩下的数据求出年利润 $y$（千万元）关于年生产量 $x$（万台）的线性回归方程（精确到 $0.01$）．" "\n"
        r"部分计算结果：$\bar y=\dfrac19\sum\limits_{i=1}^{9}y_i=6.2$，$\sum\limits_{i=1}^{9}x_i^{2}=509$，$\sum\limits_{i=1}^{9}x_iy_i=434.1$．" "\n"
        r"附：年返修率 $=\dfrac{\text{年返修量（台）}}{\text{年生产量（台）}}$．"
    ),
    'opts': [],
    'answer': (
        r"（1）分布列为 $P(X=0)=\dfrac1{21}$，$P(X=1)=\dfrac5{14}$，$P(X=2)=\dfrac{10}{21}$，$P(X=3)=\dfrac5{42}$；"
        r"$E(X)=\dfrac53$；（2）$\hat y=0.64x+1.52$．"
    ),
    'analysis': (
        r"（1）先由「返修率 $\le\frac1{1000}$」逐年判定是否优秀："
        r"$\frac{47}{30000}=1.57\times10^{-3}>10^{-3}$ 不优秀，$\frac{50}{60000}<10^{-3}$ 优秀……共 $5$ 年优秀、$4$ 年不优秀，"
        r"故 $X$ 服从超几何分布；（2）注意到 $x_6=7=\bar x$、且 $y_6$ 恰是偏差大的那项，"
        r"去掉后 $\sum(x_i-\bar x)(y_i-\bar y)$ 与 $\sum(x_i-\bar x)^2$ 中该项贡献为 $0$，故 $b$ 不变．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"年返修率 $=\dfrac{\text{年返修量}}{\text{年生产量}\times10^4}$，与 $10^{-3}$ 比较即比较「年返修量」与「年生产量$\times10$（万台$\to$台）」：" "\n"
        r"$2010$：$47>30$ 不优秀；$2011$：$42>40$ 不优秀；$2012$：$48<50$ 优秀；"
        r"$2013$：$50<60$ 优秀；$2014$：$92>70$ 不优秀；"
        r"$2015$：$83>70$ 不优秀；$2016$：$72<90$ 优秀；$2017$：$87<100$ 优秀；$2018$：$90<120$ 优秀．" "\n"
        r"故 $9$ 年中优秀 $5$ 年、不优秀 $4$ 年，$X$ 的所有可能取值为 $0,1,2,3$，且" "\n"
        r"$P(X=0)=\dfrac{C_5^{0}C_4^{3}}{C_9^{3}}=\dfrac{4}{84}=\dfrac1{21}$，"
        r"$P(X=1)=\dfrac{C_5^{1}C_4^{2}}{C_9^{3}}=\dfrac{30}{84}=\dfrac5{14}$，" "\n"
        r"$P(X=2)=\dfrac{C_5^{2}C_4^{1}}{C_9^{3}}=\dfrac{40}{84}=\dfrac{10}{21}$，"
        r"$P(X=3)=\dfrac{C_5^{3}C_4^{0}}{C_9^{3}}=\dfrac{10}{84}=\dfrac5{42}$．" "\n"
        r"（校验：$\frac4{84}+\frac{30}{84}+\frac{40}{84}+\frac{10}{84}=\frac{84}{84}=1$ ✓）" "\n"
        r"$E(X)=0\times\dfrac1{21}+1\times\dfrac5{14}+2\times\dfrac{10}{21}+3\times\dfrac5{42}=\dfrac{15+40+15}{42}=\dfrac{70}{42}=\boxed{\dfrac53}$．" "\n"
        r"（超几何分布期望公式校验：$E(X)=3\times\frac59=\frac53$ ✓）" "\n"
        r"**第（2）问**" "\n"
        r"$\bar x=\dfrac{3+4+5+6+7+7+9+10+12}{9}=\dfrac{63}{9}=7$，而 $x_6=7=\bar x$，" "\n"
        r"故去掉 $2015$ 年（第 $6$ 组，$(x_6,y_6)=(7,7.8)$）后，"
        r"该项对 $\sum(x_i-\bar x)(y_i-\bar y)$ 与 $\sum(x_i-\bar x)^{2}$ 的贡献都是 $0$，"
        r"**因而 $\hat b$ 不变**：" "\n"
        r"$\hat b=\dfrac{\sum x_iy_i-9\bar x\bar y}{\sum x_i^{2}-9\bar x^{2}}=\dfrac{434.1-9\times7\times6.2}{509-9\times7^{2}}=\dfrac{434.1-390.6}{509-441}=\dfrac{43.5}{68}\approx0.64$．" "\n"
        r"去掉该年后 $\bar x=7$（不变），$\bar y=\dfrac{9\times6.2-7.8}{8}=\dfrac{55.8-7.8}{8}=6$，" "\n"
        r"$\hat a=\bar y-\hat b\,\bar x=6-\dfrac{43.5}{68}\times7=6-4.4779\approx1.52$．" "\n"
        r"所以 $\boxed{\hat y=0.64x+1.52}$．"
    ),
    'review': (
        r"① ⭐⭐ **本题题眼：$x_6=7=\bar x$** —— 正因为如此，去掉 $2015$ 年数据后 $\hat b$ 才**不变**，"
        r"可以直接沿用 $9$ 个数据算出的 $\hat b=\frac{43.5}{68}$．这是命题人刻意安排的数据．" "\n"
        r"② ⭐⭐ **判定「优秀」只需比「年返修量」与「年生产量（万台）$\times10$」**："
        r"$3$ 万台 $=30000$ 台，千分之一即 $30$ 台，$47>30$ 不优秀 ✓．这样可完全避开小数．" "\n"
        r"③ ⭐⭐ **超几何分布的两个自检**：概率和 $=1$；$E(X)=n\cdot\frac MN=3\times\frac59=\frac53$ ✓" "\n"
        r"④ 数值复核：$C_9^3=84$；$C_5^1C_4^2=5\times6=30$；$C_5^2C_4^1=10\times4=40$；$C_5^3=10$ ✓" "\n"
        r"⑤ $\hat a=6-\frac{43.5\times7}{68}=6-\frac{304.5}{68}=6-4.478=1.522\approx1.52$ ✓" "\n"
        r"**通法（剔除异常点后的回归）**：" "\n"
        r"① 先看被剔除点的 $x$ 是否等于 $\bar x$：若是，则 $\hat b$ 不变，只重算 $\bar y$ 与 $\hat a$；" "\n"
        r"② 若不等于，则需从 $\sum x_iy_i,\sum x_i^2$ 中减去该项再重算；" "\n"
        r"③ 回归直线必过 $(\bar x,\bar y)$（剔除后的），可用来验算 $\hat a$．"
    ),
    'difficulty': 0.60,
    'topics': ['M-T-391'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-391-V2',
}


T389_V1 = {
    'type': '解答',
    'stem_text': (
        r"某商家统计了 $7$ 个月的月广告投入 $x$（单位：万元）与月销量 $y$（单位：万件）的数据如下表所示：" "\n"
        r"月广告投入 $x$（万元）：$1,2,3,4,5,6,7$；" "\n"
        r"月销量 $y$（万件）：$28,32,35,45,49,52,60$．" "\n"
        r"（1）已知可用线性回归模型拟合 $y$ 与 $x$ 的关系，请用相关系数加以说明，并求 $y$ 关于 $x$ 的线性回归方程；" "\n"
        r"（2）根据（1）的结论，预计月广告投入大于多少万元时，月销量能突破 $70$ 万件．" "\n"
        r"参考数据：$\sum\limits_{i=1}^{7}\left(x_i-\bar x\right)\left(y_i-\bar y\right)=150$，"
        r"$\sum\limits_{i=1}^{7}\left(y_i-\bar y\right)^{2}=820$，$\sqrt{1435}\approx37.88$．" "\n"
        r"参考公式：相关系数 $r=\dfrac{\sum\left(x_i-\bar x\right)\left(y_i-\bar y\right)}{\sqrt{\sum\left(x_i-\bar x\right)^{2}}\sqrt{\sum\left(y_i-\bar y\right)^{2}}}$．" "\n"
    ),
    'opts': [],
    'answer': (
        r"（1）$r\approx0.99$，线性相关程度很高，可用线性回归模型拟合；$\hat y=\dfrac{75}{14}x+\dfrac{151}{7}$；"
        r"（2）大于 $9.04$ 万元．"
    ),
    'analysis': (
        r"先算 $\bar x=4$、$\bar y=43$、$\sum(x_i-\bar x)^2=28$，"
        r"再代相关系数公式（注意 $\sqrt{28\times820}=\sqrt{22960}$，需化成 $4\sqrt{1435}$）；"
        r"回归系数 $\hat b=\frac{150}{28}=\frac{75}{14}$，最后解 $\hat y>70$．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"$\bar x=\dfrac{1+2+3+4+5+6+7}{7}=4$，"
        r"$\bar y=\dfrac{28+32+35+45+49+52+60}{7}=\dfrac{301}{7}=43$．" "\n"
        r"$\sum\limits_{i=1}^{7}\left(x_i-\bar x\right)^{2}=9+4+1+0+1+4+9=28$．" "\n"
        r"$r=\dfrac{150}{\sqrt{28}\times\sqrt{820}}=\dfrac{150}{\sqrt{22960}}=\dfrac{150}{4\sqrt{1435}}\approx\dfrac{37.5}{37.88}\approx0.99$．" "\n"
        r"因 $r\approx0.99$ 非常接近 $1$，故 $y$ 与 $x$ 的线性相关程度相当高，可用线性回归模型拟合．" "\n"
        r"$\hat b=\dfrac{\sum\left(x_i-\bar x\right)\left(y_i-\bar y\right)}{\sum\left(x_i-\bar x\right)^{2}}=\dfrac{150}{28}=\dfrac{75}{14}$，" "\n"
        r"$\hat a=\bar y-\hat b\,\bar x=43-\dfrac{75}{14}\times4=43-\dfrac{150}{7}=\dfrac{151}{7}$．" "\n"
        r"所以 $\boxed{\hat y=\dfrac{75}{14}x+\dfrac{151}{7}}$．" "\n"
        r"**第（2）问**" "\n"
        r"令 $\dfrac{75}{14}x+\dfrac{151}{7}>70$，即 $\dfrac{75}{14}x>70-\dfrac{151}{7}=\dfrac{490-151}{7}=\dfrac{339}{7}$，" "\n"
        r"$x>\dfrac{339}{7}\times\dfrac{14}{75}=\dfrac{339\times2}{75}=\dfrac{678}{75}=\dfrac{226}{25}=9.04$．" "\n"
        r"所以 $\boxed{\text{月广告投入大于 }9.04\text{ 万元时，月销量能突破 }70\text{ 万件}}$．"
    ),
    'review': (
        r"① ⭐⭐ **$\sqrt{28\times820}$ 要提出完全平方**：$\sqrt{22960}=\sqrt{16\times1435}=4\sqrt{1435}\approx4\times37.88=151.52$，"
        r"于是 $r=\frac{150}{151.52}\approx0.99$ ✓（若不提 $4$，会误算成 $\frac{150}{151.5}$ 之外的数）" "\n"
        r"② ⭐⭐ **$r$ 的两个等价写法**：$\frac{150}{\sqrt{28}\sqrt{820}}$ 与 $\frac{37.5}{\sqrt{1435}}$ —— "
        r"后者是把分子分母同除 $4$ 得到的，**这正是题目给 $\sqrt{1435}$ 的原因** ✓" "\n"
        r"③ 数值复核：$\hat b=\frac{75}{14}=5.357$，$\hat a=\frac{151}{7}=21.571$；"
        r"$x=4$ 时 $\hat y=21.43+21.57=43=\bar y$ ✓（过 $(\bar x,\bar y)$）" "\n"
        r"④ $x=9.04$ 时 $\hat y=\frac{75}{14}\times9.04+21.571=48.43+21.57=70.00$ ✓ 恰为临界值" "\n"
        r"**通法（相关系数 + 回归）**：" "\n"
        r"① 三个必备量：$\bar x,\bar y,\sum(x_i-\bar x)^2$（若题目未给则手算）；" "\n"
        r"② $r$ 的分母是两个根式之积，先提完全平方再代入题目给的近似值；" "\n"
        r"③ $|r|$ 越接近 $1$ 线性相关性越强；" "\n"
        r"④ 预测类问题直接解不等式即可．"
    ),
    'difficulty': 0.55,
    'topics': ['M-T-389'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-389-V1',
}

T395_V1 = {
    'type': '解答',
    'stem_text': (
        r"某投资公司现从 $20$ 种新产品中选出若干种进行投资．甲、乙两部门分别从这 $20$ 种新产品中随机地选取 $10$ 种产品，"
        r"每种产品被甲、乙两部门是否选中相互独立．" "\n"
        r"（1）求 $20$ 种新产品中产品 $A$ 被甲部门或乙部门选中的概率；" "\n"
        r"（2）甲部门对选取的 $10$ 种产品的年研发经费 $x_i$（单位：万元）和年销售额 $y_i$（$i=1,2,\cdots,10$，单位：十万元）"
        r"数据作了初步处理，得到统计量的值如下表：" "\n"
        r"$\sum\limits_{i=1}^{10}x_i=65$，$\sum\limits_{i=1}^{10}y_i=75$，$\sum\limits_{i=1}^{10}\left(x_i-3\right)^{2}=205$，"
        r"$\sum\limits_{i=1}^{10}\left(x_i-3\right)^{4}=8773$，$\sum\limits_{i=1}^{10}\left(x_i-3\right)^{2}y_i=2016$．" "\n"
        r"根据散点图现拟定 $y$ 关于 $x$ 的回归方程为 $\hat y=b\left(x-3\right)^{2}+a$，求 $a,b$ 的值（结果精确到 $0.1$）；" "\n"
        r"（3）甲、乙两部门同时选中了新产品 $A$，现用掷骰子的方式确定投资金额："
        r"若每次掷骰子点数大于 $2$，则甲部门增加投资 $1$ 万元，乙部门不增加投资；"
        r"若点数小于 $3$，则乙部门增加投资 $2$ 万元，甲部门不增加投资．"
        r"求两部门投资资金总和恰好为 $100$ 万元的概率．"
    ),
    'opts': [],
    'answer': (
        r"（1）$\dfrac34$；（2）$b\approx0.1$，$a\approx5.4$；（3）$\dfrac34+\dfrac14\times\left(\dfrac13\right)^{100}$．"
    ),
    'analysis': (
        r"（1）用对立事件：$A$ 未被甲、乙任一方选中 $\iff$ 两部门都从其余 $19$ 种中选 $10$ 种；"
        r"（2）令 $t=(x-3)^2$，则 $\hat y=bt+a$，用表中 $\sum t_i=205$、$\sum t_i^2=8773$、$\sum t_iy_i=2016$ 套最小二乘；"
        r"（3）设 $P_n$ 为总和恰好 $n$ 万元的概率，得 $P_{n+1}=\frac23P_n+\frac13P_{n-1}$，作差构造等比后累加．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"产品 $A$ 没被甲部门选中且没被乙部门选中的概率为" "\n"
        r"$P_0=\dfrac{C_{19}^{10}}{C_{20}^{10}}\cdot\dfrac{C_{19}^{10}}{C_{20}^{10}}=\left(\dfrac{C_{19}^{10}}{C_{20}^{10}}\right)^{2}=\left(\dfrac{10}{20}\right)^{2}=\dfrac14$．" "\n"
        r"（用了 $C_{19}^{10}=\frac{10}{20}C_{20}^{10}$，即 $C_n^k=\frac{k}{n}C_n^k$ 的变形 $C_{n-1}^{k}=\frac{n-k}{n}C_n^{k}$）" "\n"
        r"故产品 $A$ 被甲部门或乙部门选中的概率为 $\boxed{1-\dfrac14=\dfrac34}$．" "\n"
        r"**第（2）问**" "\n"
        r"令 $t=\left(x-3\right)^{2}$，则回归方程为 $\hat y=bt+a$，且由表得" "\n"
        r"$\bar t=\dfrac1{10}\sum\left(x_i-3\right)^{2}=\dfrac{205}{10}=20.5$，"
        r"$\bar y=\dfrac1{10}\sum y_i=\dfrac{75}{10}=7.5$，" "\n"
        r"$\sum t_iy_i=\sum\left(x_i-3\right)^{2}y_i=2016$，$\sum t_i^{2}=\sum\left(x_i-3\right)^{4}=8773$．" "\n"
        r"$\hat b=\dfrac{\sum t_iy_i-10\bar t\bar y}{\sum t_i^{2}-10\bar t^{2}}=\dfrac{2016-10\times20.5\times7.5}{8773-10\times20.5^{2}}=\dfrac{2016-1537.5}{8773-4202.5}=\dfrac{478.5}{4570.5}\approx0.1047\approx0.1$．" "\n"
        r"$\hat a=\bar y-\hat b\,\bar t=7.5-0.1047\times20.5=7.5-2.146\approx5.4$．" "\n"
        r"所以 $\boxed{b\approx0.1,\ a\approx5.4}$．" "\n"
        r"**第（3）问**" "\n"
        r"每次掷骰子：甲增 $1$ 万（点数 $>2$，概率 $\frac46=\frac23$），或乙增 $2$ 万（点数 $<3$，概率 $\frac26=\frac13$）．" "\n"
        r"设投资资金总和恰好为 $n$ 万元的概率为 $P_n$，则总和达到 $n+1$ 只有两种互斥情形：" "\n"
        r"先到 $n$ 万元再增 $1$ 万，或先到 $n-1$ 万元再增 $2$ 万，故" "\n"
        r"$P_{n+1}=\dfrac23P_n+\dfrac13P_{n-1}\quad\left(n\ge2\right)$．" "\n"
        r"作差：$P_{n+1}-P_n=-\dfrac13\left(P_n-P_{n-1}\right)$，故 $\left\{P_{n+1}-P_n\right\}$ 是等比数列，公比 $-\dfrac13$．" "\n"
        r"又 $P_1=\dfrac23$，$P_2=\dfrac13+\dfrac23\times\dfrac23=\dfrac13+\dfrac49=\dfrac79$，故 $P_2-P_1=\dfrac79-\dfrac23=\dfrac19$．" "\n"
        r"累加：$P_{100}=P_1+\sum\limits_{k=1}^{99}\left(P_{k+1}-P_k\right)=\dfrac23+\dfrac19\cdot\dfrac{1-\left(-\frac13\right)^{99}}{1-\left(-\frac13\right)}=\dfrac23+\dfrac19\times\dfrac34\left[1-\left(-\dfrac13\right)^{99}\right]$" "\n"
        r"$=\dfrac23+\dfrac1{12}\left[1-\left(-\dfrac13\right)^{99}\right]=\dfrac23+\dfrac1{12}+\dfrac1{12}\times\dfrac1{3^{99}}=\dfrac34+\dfrac14\times\dfrac1{3^{100}}$．" "\n"
        r"所以 $\boxed{P_{100}=\dfrac34+\dfrac14\times\left(\dfrac13\right)^{100}}$．"
    ),
    'review': (
        r"① ⭐⭐ **$C_{19}^{10}/C_{20}^{10}=\frac{10}{20}=\frac12$**：由 $C_{n}^{k}=\frac{n}{n-k}C_{n-1}^{k}$ 得 "
        r"$C_{20}^{10}=\frac{20}{10}C_{19}^{10}=2C_{19}^{10}$，故比值为 $\frac12$ ✓" "\n"
        r"② ⭐⭐ **回归换元 $t=(x-3)^2$ 后，表里给的 $\sum(x_i-3)^4$ 就是 $\sum t_i^2$** —— "
        r"这是本题的题眼：**不必回到原始数据**．" "\n"
        r"③ ⭐⭐ **$P_n$ 递推作差，公比恒为 $-\frac13$**（即「走 $2$ 步」的概率的相反数），"
        r"稳态值 $\frac1{1+\frac13}=\frac34$，正是「平均增加量 $1\times\frac23+2\times\frac13=\frac43$」的倒数 ✓✓" "\n"
        r"④ 数值复核：$\hat b=\frac{478.5}{4570.5}=0.1047$，$\hat a=7.5-0.1047\times20.5=5.354\approx5.4$ ✓" "\n"
        r"⑤ $P_{100}\approx\frac34+2.6\times10^{-49}$，几乎就是 $\frac34$ ✓" "\n"
        r"**通法（换元回归 + 概率递推）**：" "\n"
        r"① 回归方程形如 $\hat y=b\varphi(x)+a$ 时，令 $t=\varphi(x)$，把表中对应的和式认成 $\sum t_i,\sum t_i^2,\sum t_iy_i$；" "\n"
        r"② 递推 $P_n=pP_{n-1}+qP_{n-2}$ 一律作差，公比 $-q$，稳态值 $\frac1{1+q}$；" "\n"
        r"③ 求 $P_N$ 用累加：$P_N=P_1+\sum_{k=1}^{N-1}(P_{k+1}-P_k)$．"
    ),
    'difficulty': 0.68,
    'topics': ['M-T-395'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-395-V1',
}


T268_V2 = {
    'type': '解答',
    'stem_text': (
        r"设 $\left\{a_n\right\}$ 是等差数列，$\left\{b_n\right\}$ 是等比数列，公比大于 $0$．"
        r"已知 $b_1=1$，$b_2+2b_3=1$，$\left(a_2+a_6\right)b_4=1$，$a_4b_2=a_5-a_3$．" "\n"
        r"（Ⅰ）求数列 $\left\{a_n\right\}$，$\left\{b_n\right\}$ 的通项公式；" "\n"
        r"（Ⅱ）设 $c_n=1+\dfrac1{n\left(n+2\right)}$，$S_n=c_1\cdot c_2\cdot c_3\cdots c_n$（$n\in\mathbf{N}^{*}$）．" "\n"
        r"（ⅰ）求 $S_n$；（ⅱ）证明 $\sum\limits_{k=1}^{n}\dfrac{b_k-b_{k+1}}{kS_k}=\dfrac12-\dfrac1{\left(n+1\right)\cdot2^{n+1}}$（$n\in\mathbf{N}^{*}$）．"
    ),
    'opts': [],
    'answer': (
        r"（Ⅰ）$a_n=n$，$b_n=\left(\dfrac12\right)^{n-1}$；（Ⅱ）（ⅰ）$S_n=\dfrac{2\left(n+1\right)}{n+2}$；（ⅱ）证明见解析．"
    ),
    'analysis': (
        r"（Ⅰ）由 $q+2q^2=1$ 解出 $q=\frac12$；再由 $\left(a_2+a_6\right)b_4=1$ 与 $a_4b_2=a_5-a_3$ 联立解 $a_1,d$；"
        r"（Ⅱ）（ⅰ）把 $c_n$ 写成 $\frac{\left(n+1\right)^{2}}{n\left(n+2\right)}$ 后连乘约去；"
        r"（ⅱ）代入 $b_k$、$S_k$ 后得 $\frac{k+2}{k\left(k+1\right)2^{k+1}}$，再裂成 $\frac1{k\cdot2^{k}}-\frac1{\left(k+1\right)2^{k+1}}$．"
    ),
    'solution': (
        r"**第（Ⅰ）问**" "\n"
        r"设 $\left\{a_n\right\}$ 首项为 $a_1$、公差为 $d$，$\left\{b_n\right\}$ 公比为 $q\left(q>0\right)$．" "\n"
        r"由 $b_1=1$，$b_2+2b_3=1$ 得 $q+2q^{2}=1$，即 $\left(2q-1\right)\left(q+1\right)=0$，"
        r"因 $q>0$，故 $q=\dfrac12$，$\boxed{b_n=\left(\dfrac12\right)^{n-1}}$．" "\n"
        r"由 $\left(a_2+a_6\right)b_4=1$ 且 $b_4=\left(\frac12\right)^{3}=\frac18$，得 $a_2+a_6=8$，即 $2a_1+6d=8$；" "\n"
        r"由 $a_4b_2=a_5-a_3$ 且 $b_2=\frac12$、$a_5-a_3=2d$，得 $\dfrac12\left(a_1+3d\right)=2d$，即 $a_1=d$．" "\n"
        r"代入得 $2d+6d=8$，$d=1$，故 $a_1=1$，$\boxed{a_n=n}$．" "\n"
        r"**第（Ⅱ）问（ⅰ）**" "\n"
        r"$c_n=1+\dfrac1{n\left(n+2\right)}=\dfrac{n\left(n+2\right)+1}{n\left(n+2\right)}=\dfrac{\left(n+1\right)^{2}}{n\left(n+2\right)}$．" "\n"
        r"$S_n=\prod\limits_{k=1}^{n}\dfrac{\left(k+1\right)^{2}}{k\left(k+2\right)}"
          r"=\dfrac{2\cdot2}{1\cdot3}\times\dfrac{3\cdot3}{2\cdot4}\times\dfrac{4\cdot4}{3\cdot5}\times\cdots\times\dfrac{\left(n+1\right)\left(n+1\right)}{n\left(n+2\right)}$．" "\n"
        r"分子中 $2$ 出现 $2$ 次、$3,4,\cdots,n$ 各出现 $2$ 次、$n+1$ 出现 $2$ 次；"
        r"分母中 $1,2$ 各 $1$ 次、$3,\cdots,n$ 各 $2$ 次、$n+1$ 出现 $1$ 次、$n+2$ 出现 $1$ 次．" "\n"
        r"约去后得 $\boxed{S_n=\dfrac{2\left(n+1\right)}{n+2}}$．" "\n"
        r"（校验：$n=1$ 时 $S_1=c_1=1+\frac13=\frac43$，而 $\frac{2\times2}{3}=\frac43$ ✓）" "\n"
        r"**第（Ⅱ）问（ⅱ）**" "\n"
        r"$b_k-b_{k+1}=\left(\dfrac12\right)^{k-1}-\left(\dfrac12\right)^{k}=\left(\dfrac12\right)^{k}=\dfrac1{2^{k}}$，"
        r"$kS_k=k\cdot\dfrac{2\left(k+1\right)}{k+2}=\dfrac{2k\left(k+1\right)}{k+2}$，" "\n"
        r"故 $\dfrac{b_k-b_{k+1}}{kS_k}=\dfrac{1}{2^{k}}\cdot\dfrac{k+2}{2k\left(k+1\right)}=\dfrac{k+2}{k\left(k+1\right)\cdot2^{k+1}}$．" "\n"
        r"又 $\dfrac1{k\cdot2^{k}}-\dfrac1{\left(k+1\right)\cdot2^{k+1}}=\dfrac{2\left(k+1\right)-k}{k\left(k+1\right)\cdot2^{k+1}}=\dfrac{k+2}{k\left(k+1\right)\cdot2^{k+1}}$，两式相等，故" "\n"
        r"$\sum\limits_{k=1}^{n}\dfrac{b_k-b_{k+1}}{kS_k}=\sum\limits_{k=1}^{n}\left[\dfrac1{k\cdot2^{k}}-\dfrac1{\left(k+1\right)\cdot2^{k+1}}\right]=\dfrac1{1\cdot2^{1}}-\dfrac1{\left(n+1\right)\cdot2^{n+1}}=\dfrac12-\dfrac1{\left(n+1\right)\cdot2^{n+1}}$．" "\n"
        r"证毕．"
    ),
    'review': (
        r"① ⭐⭐ **$c_n=\frac{\left(n+1\right)^{2}}{n\left(n+2\right)}$ 是全题的题眼**："
        r"因为 $n\left(n+2\right)+1=n^{2}+2n+1=\left(n+1\right)^{2}$，**命题人特意让 $+1$ 凑成完全平方**，"
        r"只有这样才能在连乘中错位相消．" "\n"
        r"② ⭐⭐ **裂项的方向由末项倒推**：要凑出末项 $-\frac1{\left(n+1\right)2^{n+1}}$，"
        r"自然应裂成 $\frac1{k\cdot2^{k}}-\frac1{\left(k+1\right)2^{k+1}}$；"
        r"通分验证分子 $2\left(k+1\right)-k=k+2$ 恰好对上 ✓" "\n"
        r"③ ⭐⭐ **$a_1=d$ 这一步最省事**：$a_4b_2=a_5-a_3$ 中 $a_5-a_3=2d$ 是等差数列的性质（隔一项差 $2d$），"
        r"不必展开成 $a_1+4d-\left(a_1+2d\right)$．" "\n"
        r"④ 数值复核：$n=2$ 时 $S_2=\frac43\times\frac98=\frac32$，而 $\frac{2\times3}{4}=\frac32$ ✓；"
        r"左端 $k=1,2$ 两项 $=\frac{3}{1\cdot2\cdot4}+\frac{4}{2\cdot3\cdot8}=\frac38+\frac1{12}=\frac{11}{24}=0.4583$，"
        r"右端 $\frac12-\frac1{3\cdot8}=\frac12-\frac1{24}=\frac{11}{24}$ ✓" "\n"
        r"**通法（连乘型求积 + 裂项）**：" "\n"
        r"① $c_n=1+\frac1{n\left(n+2\right)}$ 型先通分，看分子是否为完全平方；" "\n"
        r"② 连乘时按「每个整数出现几次」统计，不要硬约；" "\n"
        r"③ 裂项待定：由目标末项的形式反推应裂成哪两项之差．"
    ),
    'difficulty': 0.72,
    'topics': ['M-T-268'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-268-V2',
}

T257_V2 = {
    'type': '选择',
    'stem_text': (
        r"在数列 $\left\{a_n\right\}$ 中，$a_1=a$（$a\in\mathbf{N}^{*}$），"
        r"$a_{n+1}=\begin{cases}\dfrac12a_n,& a_n\text{ 为偶数}\\2019+a_n,& a_n\text{ 为奇数}\end{cases}$（$n\in\mathbf{N}^{*}$），则下列结论成立的是（　　）"
    ),
    'opts': [
        ('A', r"存在正整数 $a$，使得 $\left\{a_n\right\}$ 为常数列"),
        ('B', r"存在正整数 $a$，使得 $\left\{a_n\right\}$ 为单调数列"),
        ('C', r"对任意的正整数 $a$，集合 $\left\{a_n\mid n\in\mathbf{N}^{*}\right\}$ 为有限集"),
        ('D', r"存在正整数 $a$，使得任意的 $m,n\in\mathbf{N}^{*}$，当 $m\ne n$ 时，$a_m\ne a_n$"),
    ],
    'answer': r"C",
    'analysis': (
        r"A：常数列要求 $a_{n+1}=a_n$，偶数时得 $a=0$（不合），奇数时 $2019+a=a$ 无解；"
        r"B：无论 $a$ 奇偶，数列都会「一升一降」，不可能单调；"
        r"C：证明数列有界即可（奇数项 $\le t$、偶数项 $\le 2t$，其中 $t=\max\left\{a,2019\right\}$）；"
        r"D：有界且取正整数值，由抽屉原理必有重复，故 D 假．"
    ),
    'solution': (
        r"**A 错**：若 $\left\{a_n\right\}$ 为常数列，则 $a_{n+1}=a_n$ 恒成立．"
        r"当 $a_n$ 为偶数时 $\frac12a_n=a_n\Rightarrow a_n=0$，与 $a\in\mathbf{N}^{*}$ 矛盾；"
        r"当 $a_n$ 为奇数时 $2019+a_n=a_n$，无解．故不存在这样的 $a$．" "\n"
        r"**B 错**：若 $a$ 为偶数，则 $a_2=\frac12a_1<a_1$，若单调则必为递减；"
        r"但 $a_2$ 可能为奇数，此时 $a_3=2019+a_2>a_2$，矛盾．"
        r"若 $a$ 为奇数，则 $a_2=2019+a_1>a_1$，若单调则必为递增；但 $a_3=\frac12a_2<a_2$，矛盾．" "\n"
        r"**C 对**：记 $t=\max\left\{a,2019\right\}$，下证：对一切 $n$，若 $a_n$ 为奇数则 $a_n\le t$，若 $a_n$ 为偶数则 $a_n\le 2t$．" "\n"
        r"① $n=1$ 时，$a_1=a\le t$，成立．" "\n"
        r"② 设 $n=k$ 时成立．若 $a_k$ 为奇数，则 $a_{k+1}=2019+a_k\le 2019+t\le 2t$，且 $a_{k+1}$ 为偶数（奇 $+$ 奇 $=$ 偶），满足 $a_{k+1}\le2t$；"
        r"若 $a_k$ 为偶数，则 $a_{k+1}=\frac12a_k\le\frac12\cdot2t=t\le2t$，成立（且若 $a_{k+1}$ 为奇数还满足 $\le t$）．" "\n"
        r"由数学归纳法，对一切 $n$ 都有 $a_n\le2t$，即 $\left\{a_n\right\}$ 是有界的正整数列．" "\n"
        r"正整数列有界 $\Rightarrow$ 取值个数有限，故集合 $\left\{a_n\mid n\in\mathbf{N}^{*}\right\}$ 为有限集，C 正确．" "\n"
        r"**D 错**：由 C 知 $\left\{a_n\right\}$ 取值有限，而项数无限，由抽屉原理必存在 $m\ne n$ 使 $a_m=a_n$，"
        r"故「任意 $m\ne n$ 都有 $a_m\ne a_n$」不可能成立．" "\n"
        r"故选 $\boxed{\mathrm{C}}$．"
    ),
    'review': (
        r"① ⭐⭐ **本题本质是「有界 $\Rightarrow$ 有限」**：$a_n$ 恒为正整数且有上界 $2t$，"
        r"取值只能在 $\left\{1,2,\cdots,2t\right\}$ 中，故集合必为有限集．" "\n"
        r"② ⭐⭐ **归纳时「奇数 $\Rightarrow$ 下一项是偶数」是关键**："
        r"$2019+a_k$ 中 $2019$ 与 $a_k$ 同为奇数，和为偶数——这保证了下一步会「减半」，"
        r"数列不会无限增长．这是 $3n+1$ 型问题的通用结构．" "\n"
        r"③ ⚠ 上界取 $2t$ 而非 $t$：因为奇数项加 $2019$ 后可达到 $t+2019\le2t$．" "\n"
        r"④ **D 与 C 直接对立**：C 说「必为有限集」，D 说「可以两两不同（无限集）」，"
        r"故证出 C 后 D 自动为假——这类互斥选项可成对排除．" "\n"
        r"**通法（分奇偶递推数列）**：" "\n"
        r"① 讨论「常数列 / 单调」用代入法，先按首项奇偶分两类；" "\n"
        r"② 讨论「有界 / 有限」用数学归纳法，归纳假设要分「奇数项、偶数项」两个上界；" "\n"
        r"③ 正整数列有界即取值有限，可用抽屉原理处理「是否存在重复项」．"
    ),
    'difficulty': 0.78,
    'topics': ['M-T-257'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-257-V2',
}

T274_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知数列 $\left\{a_n\right\}$ 的前 $n$ 项和为 $S_n$，$a_1=2$，且对任意正整数 $n$，都有 $a_{n+1}=3S_n+2$，"
        r"数列 $\left\{b_n\right\}$ 满足 $b_n=\log_2a_n$．" "\n"
        r"（1）求数列 $\left\{a_n\right\}$，$\left\{b_n\right\}$ 的通项公式；" "\n"
        r"（2）求证：$\dfrac1{b_1^{2}}+\dfrac1{b_2^{2}}+\cdots+\dfrac1{b_n^{2}}\le\dfrac{5n-1}{4n}$．"
    ),
    'opts': [],
    'answer': (
        r"（1）$a_n=2^{2n-1}$，$b_n=2n-1$；（2）证明见解析．"
    ),
    'analysis': (
        r"（1）退位相减：$n\ge2$ 时 $a_n=3S_{n-1}+2$，与 $a_{n+1}=3S_n+2$ 相减得 $a_{n+1}-a_n=3a_n$，"
        r"即 $a_{n+1}=4a_n$；再验证 $n=1$ 也成立；"
        r"（2）$b_n=2n-1$，关键放缩 $\frac1{\left(2n-1\right)^{2}}<\frac1{\left(2n-1\right)^{2}-1}=\frac14\left(\frac1{n-1}-\frac1n\right)$（$n\ge2$），首项单独留着．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"由 $a_{n+1}=3S_n+2$，当 $n\ge2$ 时 $a_n=3S_{n-1}+2$，两式相减得" "\n"
        r"$a_{n+1}-a_n=3\left(S_n-S_{n-1}\right)=3a_n$，即 $a_{n+1}=4a_n\left(n\ge2\right)$．" "\n"
        r"当 $n=1$ 时，$a_2=3S_1+2=3\times2+2=8$，$\dfrac{a_2}{a_1}=\dfrac82=4$，也满足．" "\n"
        r"故 $\left\{a_n\right\}$ 是首项为 $2$、公比为 $4$ 的等比数列，"
        r"$\boxed{a_n=2\cdot4^{n-1}=2^{2n-1}}$．" "\n"
        r"于是 $\boxed{b_n=\log_2a_n=\log_22^{2n-1}=2n-1}$．" "\n"
        r"**第（2）问**" "\n"
        r"当 $n=1$ 时，左端 $=1$，右端 $=\dfrac{5-1}{4}=1$，等号成立 ✓" "\n"
        r"当 $n\ge2$ 时，$\dfrac1{\left(2n-1\right)^{2}}<\dfrac1{\left(2n-1\right)^{2}-1}=\dfrac1{4n^{2}-4n}=\dfrac1{4n\left(n-1\right)}=\dfrac14\left(\dfrac1{n-1}-\dfrac1n\right)$．" "\n"
        r"（用了 $\left(2n-1\right)^{2}-1=\left(2n-2\right)\left(2n\right)=4n\left(n-1\right)$）" "\n"
        r"所以 $\sum\limits_{k=1}^{n}\dfrac1{b_k^{2}}=1+\sum\limits_{k=2}^{n}\dfrac1{\left(2k-1\right)^{2}}<1+\dfrac14\sum\limits_{k=2}^{n}\left(\dfrac1{k-1}-\dfrac1k\right)$" "\n"
        r"$=1+\dfrac14\left(1-\dfrac1n\right)=1+\dfrac{n-1}{4n}=\dfrac{4n+n-1}{4n}=\dfrac{5n-1}{4n}$．" "\n"
        r"综上 $\boxed{\dfrac1{b_1^{2}}+\dfrac1{b_2^{2}}+\cdots+\dfrac1{b_n^{2}}\le\dfrac{5n-1}{4n}}$（$n=1$ 时取等号）．"
    ),
    'review': (
        r"① ⭐⭐ **$a_{n+1}=3S_n+2$ 型必须「退一位再相减」**，且**必须单独验证 $n=1$**："
        r"相减只对 $n\ge2$ 成立，而 $\frac{a_2}{a_1}=4$ 恰好也成立，故从 $n=1$ 起就是等比 ✓" "\n"
        r"② ⭐⭐ **放缩的分母要凑平方差**：$\left(2n-1\right)^{2}-1=4n\left(n-1\right)$ 正好裂成 $\frac14\left(\frac1{n-1}-\frac1n\right)$．"
        r"**$n=1$ 时分母为 $0$，故首项必须单独处理**——这正是答案中 $n=1$ 取等号的原因．" "\n"
        r"③ ⭐⭐ **右端 $\frac{5n-1}{4n}$ 的来源**：$1+\frac14\left(1-\frac1n\right)=\frac{5n-1}{4n}$，"
        r"当 $n\to\infty$ 时趋于 $\frac54$（而 $\sum\frac1{\left(2n-1\right)^{2}}$ 收敛到 $\frac{\pi^{2}}8\approx1.2337<\frac54$ ✓）" "\n"
        r"④ 数值复核：$n=2$ 时左端 $=1+\frac19=1.1111$，右端 $=\frac{9}{8}=1.125$ ✓；"
        r"$n=3$ 时左端 $=1+\frac19+\frac1{25}=1.1511$，右端 $=\frac{14}{12}=1.1667$ ✓" "\n"
        r"**通法（$S_n$ 型递推 + 裂项放缩）**：" "\n"
        r"① $a_{n+1}=pS_n+q$ 退位相减得 $a_{n+1}=\left(p+1\right)a_n$（$n\ge2$），再验 $n=1$；" "\n"
        r"② 分母为奇数平方时，减 $1$ 凑平方差是固定手法；" "\n"
        r"③ 裂项起点若使分母为 $0$，把前几项单独留出来．"
    ),
    'difficulty': 0.65,
    'topics': ['M-T-274'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-274-E1',
}


T031_E1 = {
    'type': '解答',
    'stem_text': (
        r"函数 $f\left(x\right)=\left|x-1\right|+\left|x\right|$．" "\n"
        r"（1）求不等式 $f\left(x\right)\ge5$ 的解集；" "\n"
        r"（2）已知函数 $f\left(x\right)$ 的最小值为 $t$，正实数 $a,b,c$ 满足 $a+b+2c=2t$，证明：$\dfrac1{a+c}+\dfrac1{b+c}\ge2$．"
    ),
    'opts': [],
    'answer': (
        r"（1）$\left(-\infty,-2\right]\cup\left[3,+\infty\right)$；（2）证明见解析．"
    ),
    'analysis': (
        r"（1）按零点 $0,1$ 分三段去绝对值，分段解不等式后取并集；"
        r"（2）由 $\left|x-1\right|+\left|x\right|\ge\left|\left(x-1\right)-x\right|=1$ 得 $t=1$，"
        r"于是 $\left(a+c\right)+\left(b+c\right)=2$，把所求式乘上这个「$2$」后用基本不等式．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"$f\left(x\right)=\left|x-1\right|+\left|x\right|=\begin{cases}1-2x,& x\le0\\1,& 0<x<1\\2x-1,& x\ge1\end{cases}$．" "\n"
        r"（当 $x\le0$ 时 $\left|x-1\right|=1-x$、$\left|x\right|=-x$，故 $f=1-2x$；当 $0<x<1$ 时 $f=\left(1-x\right)+x=1$；当 $x\ge1$ 时 $f=\left(x-1\right)+x=2x-1$）" "\n"
        r"$f\left(x\right)\ge5$ 即：" "\n"
        r"$x\le0$ 且 $1-2x\ge5\Rightarrow x\le-2$；或 $0<x<1$ 且 $1\ge5$（无解）；或 $x\ge1$ 且 $2x-1\ge5\Rightarrow x\ge3$．" "\n"
        r"故解集为 $\boxed{\left(-\infty,-2\right]\cup\left[3,+\infty\right)}$．" "\n"
        r"**第（2）问**" "\n"
        r"由绝对值三角不等式 $f\left(x\right)=\left|x-1\right|+\left|x\right|\ge\left|\left(x-1\right)-x\right|=1$，" "\n"
        r"当 $0\le x\le1$ 时取等号，故 $\boxed{t=1}$，于是 $a+b+2c=2$，即 $\left(a+c\right)+\left(b+c\right)=2$．" "\n"
        r"因 $a,b,c>0$，故 $a+c>0$、$b+c>0$，于是" "\n"
        r"$\dfrac1{a+c}+\dfrac1{b+c}=\dfrac12\left(\dfrac1{a+c}+\dfrac1{b+c}\right)\left[\left(a+c\right)+\left(b+c\right)\right]$" "\n"
        r"$=\dfrac12\left[2+\dfrac{b+c}{a+c}+\dfrac{a+c}{b+c}\right]\ge\dfrac12\left(2+2\sqrt{\dfrac{b+c}{a+c}\cdot\dfrac{a+c}{b+c}}\right)=\dfrac12\times4=2$．" "\n"
        r"当且仅当 $a+c=b+c=1$（即 $a=b$ 且 $a+c=1$）时取等号，证毕．"
    ),
    'review': (
        r"① ⭐⭐ **最小值 $t$ 用 $\left|u\right|+\left|v\right|\ge\left|u-v\right|$ 一步得到**：取 $u=x-1,\ v=x$，则 $u-v=-1$ 与 $x$ 无关，"
        r"故 $f\left(x\right)\ge1$，且 $0\le x\le1$ 时取等．**比分段讨论快得多**．" "\n"
        r"② ⭐⭐ **条件 $a+b+2c=2$ 要「拆成两个括号」**：$a+b+2c=\left(a+c\right)+\left(b+c\right)$ —— "
        r"因为所求式是 $\frac1{a+c}+\frac1{b+c}$，**括号必须与所求式的分母一致**．这是第二问唯一的题眼．" "\n"
        r"③ ⭐⭐ **「乘 $1$ 法」**：条件给出两括号之和为 $2$，故乘上 $\frac12\left[\left(a+c\right)+\left(b+c\right)\right]=1$，展开后用基本不等式．" "\n"
        r"④ 原书详解第二段区间写为 $1<x<1$，应为 $0<x<1$（笔误，不影响结果）．" "\n"
        r"⑤ 数值复核：$x=-2$ 时 $f=3+2=5$ ✓；$x=3$ 时 $f=2+3=5$ ✓；$a=b=c=\frac12$ 时 $a+b+2c=2$，"
        r"$\frac1{a+c}+\frac1{b+c}=\frac11+\frac11=2$ 恰取等号 ✓" "\n"
        r"**通法（绝对值最小值 + 条件最值）**：" "\n"
        r"① $\left|x-p\right|+\left|x-q\right|$ 的最小值 $=\left|p-q\right|$（两零点距离），取等区间为 $\left[\min,\max\right]$；" "\n"
        r"② 条件式要按所求式的分母重新分组；" "\n"
        r"③ 用「乘 $1$ 法 + 基本不等式」证明，取等条件要写出来．"
    ),
    'difficulty': 0.58,
    'topics': ['M-T-031'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-031-E1',
}

T031_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知 $f\left(x\right)=\left|x+1\right|+\left|x-3\right|$．" "\n"
        r"（1）求不等式 $f\left(x\right)\le x+3$ 的解集；" "\n"
        r"（2）若 $f\left(x\right)$ 的最小值为 $m$，正实数 $a,b,c$ 满足 $a+b+c=m$，"
        r"求证：$\dfrac1{a+b}+\dfrac1{b+c}+\dfrac1{a+c}\ge\dfrac9{2m}$．"
    ),
    'opts': [],
    'answer': (
        r"（1）$\left\{x\mid1\le x\le5\right\}$（即 $\left[1,5\right]$）；（2）证明见解析（右端 $=\dfrac98$）．"
    ),
    'analysis': (
        r"（1）按零点 $-1,3$ 分三段，注意第三段 $x>3$ 的解是 $3<x\le5$（原书此处误写「无解」）；"
        r"（2）$m=\left|3-\left(-1\right)\right|=4$，且 $\left(a+b\right)+\left(b+c\right)+\left(a+c\right)=2\left(a+b+c\right)=8$，"
        r"所求式乘 $\frac18\times8$ 后用基本不等式（三项两两配对）．"
    ),
    'solution': (
        r"**第（1）问**" "\n"
        r"$f\left(x\right)=\left|x+1\right|+\left|x-3\right|=\begin{cases}-2x+2,& x\le-1\\4,& -1<x\le3\\2x-2,& x>3\end{cases}$．" "\n"
        r"① 当 $x\le-1$ 时：$-2x+2\le x+3\Rightarrow x\ge-\dfrac13$，与 $x\le-1$ 矛盾，无解．" "\n"
        r"② 当 $-1<x\le3$ 时：$4\le x+3\Rightarrow x\ge1$，故 $1\le x\le3$．" "\n"
        r"③ 当 $x>3$ 时：$2x-2\le x+3\Rightarrow x\le5$，故 $3<x\le5$．" "\n"
        r"（原书此处写「无解」是笔误，实际解为 $3<x\le5$）" "\n"
        r"综上，解集为 $\boxed{\left[1,5\right]}$．" "\n"
        r"**第（2）问**" "\n"
        r"由绝对值三角不等式 $f\left(x\right)=\left|x+1\right|+\left|x-3\right|\ge\left|\left(x+1\right)-\left(x-3\right)\right|=4$，" "\n"
        r"当 $-1\le x\le3$ 时取等号，故 $\boxed{m=4}$，于是 $a+b+c=4$，"
        r"$\left(a+b\right)+\left(b+c\right)+\left(a+c\right)=2\left(a+b+c\right)=8$，右端 $\dfrac9{2m}=\dfrac98$．" "\n"
        r"$\dfrac1{a+b}+\dfrac1{b+c}+\dfrac1{a+c}=\dfrac18\left[\left(a+b\right)+\left(b+c\right)+\left(a+c\right)\right]\left(\dfrac1{a+b}+\dfrac1{b+c}+\dfrac1{a+c}\right)$" "\n"
        r"$=\dfrac18\left[3+\left(\dfrac{b+c}{a+b}+\dfrac{a+b}{b+c}\right)+\left(\dfrac{b+c}{a+c}+\dfrac{a+c}{b+c}\right)+\left(\dfrac{a+b}{a+c}+\dfrac{a+c}{a+b}\right)\right]$" "\n"
        r"$\ge\dfrac18\left(3+2+2+2\right)=\dfrac98=\dfrac9{2m}$．" "\n"
        r"当且仅当 $a+b=b+c=a+c$，即 $a=b=c=\dfrac43$ 时取等号，证毕．"
    ),
    'review': (
        r"① ⭐⭐ **原书笔误**：详解第③段写「$2x-2\le x+3\Rightarrow x\le5$，无解」，"
        r"实际解为 $3<x\le5$．若照抄会导致解集变成 $\left[1,3\right]$，与答案 $\left[1,5\right]$ 矛盾——**这是判据**．" "\n"
        r"② ⭐⭐ **$m=\left|3-\left(-1\right)\right|=4$ 是两零点距离**，与 M-T-031-E1 完全同一招："
        r"$\left|u\right|+\left|v\right|\ge\left|u-v\right|$，取 $u=x+1,\ v=x-3$ 使 $x$ 抵消 ✓" "\n"
        r"③ ⭐⭐ **三个括号之和 $=2\left(a+b+c\right)$**：因为每个字母恰好出现两次．"
        r"所求式乘上 $\frac18\times\left[\text{三括号之和}\right]=1$ 后展开，得到 $3$ 个常数 $1$ 加 $6$ 个分式，"
        r"两两配对各用一次基本不等式，共得 $3+2+2+2=9$ ✓" "\n"
        r"④ 数值复核：$a=b=c=\frac43$ 时 $a+b=\frac83$，三项各 $=\frac38$，和 $=\frac98$ ✓ 恰取等号；"
        r"$x=1$ 时 $f=2+2=4=x+3$ ✓；$x=5$ 时 $f=6+2=8=x+3$ ✓（两端点都取到）" "\n"
        r"**通法（三括号型条件最值）**：" "\n"
        r"① $\left|x-p\right|+\left|x-q\right|$ 最小值 $=\left|p-q\right|$；" "\n"
        r"② 条件 $a+b+c=m$ 要写成 $\left(a+b\right)+\left(b+c\right)+\left(a+c\right)=2m$ 与分母对齐；" "\n"
        r"③ 乘 $1$ 法展开后，$n$ 项时分式配成 $\binom n2$ 对，每对贡献 $2$．"
    ),
    'difficulty': 0.60,
    'topics': ['M-T-031'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-031-V2',
}

T182_V2 = {
    'type': '填空',
    'stem_text': (
        r"已知函数 $f\left(x\right)=\cos x$，若对任意实数 $x_1,x_2$，"
        r"方程 $\left|f\left(x\right)-f\left(x_1\right)\right|+\left|f\left(x\right)-f\left(x_2\right)\right|=m$（$m\in\mathbf{R}$）有解，"
        r"方程 $\left|f\left(x\right)-f\left(x_1\right)\right|-\left|f\left(x\right)-f\left(x_2\right)\right|=n$（$n\in\mathbf{R}$）也有解，"
        r"则 $m+n$ 的值的集合为 $\underline{\qquad\qquad}$．"
    ),
    'opts': [],
    'answer': r"$\left\{2\right\}$",
    'analysis': (
        r"令 $t=\cos x\in\left[-1,1\right]$，记 $c_1=\cos x_1\le c_2=\cos x_2$（都在 $\left[-1,1\right]$ 内）．"
        r"$\left|t-c_1\right|+\left|t-c_2\right|$ 的值域是 $\left[c_2-c_1,\ \max\left\{c_1+c_2+2,\ 2-c_1-c_2\right\}\right]$，"
        r"要对任意 $c_1,c_2$ 都有 $m$ 落在值域内，必须 $m\ge2$ 且 $m\le2$，即 $m=2$；"
        r"$\left|t-c_1\right|-\left|t-c_2\right|$ 的值域是 $\left[c_1-c_2,\ c_2-c_1\right]$，对所有 $c_1,c_2$ 取交集得 $n=0$．"
    ),
    'solution': (
        r"令 $t=\cos x\in\left[-1,1\right]$，不妨设 $c_1=\cos x_1\le c_2=\cos x_2$（$c_1,c_2\in\left[-1,1\right]$）．" "\n"
        r"**先求 $m$**：设 $h\left(t\right)=\left|t-c_1\right|+\left|t-c_2\right|$，$t\in\left[-1,1\right]$．" "\n"
        r"当 $t\in\left[c_1,c_2\right]$ 时 $h\left(t\right)=c_2-c_1$（常数）；当 $t<c_1$ 时 $h=c_1+c_2-2t$（递减）；当 $t>c_2$ 时 $h=2t-c_1-c_2$（递增）．" "\n"
        r"故 $h$ 的最小值 $=c_2-c_1$，最大值 $=\max\left\{h\left(-1\right),h\left(1\right)\right\}=\max\left\{c_1+c_2+2,\ 2-c_1-c_2\right\}=2+\left|c_1+c_2\right|\ge2$．" "\n"
        r"「对任意 $x_1,x_2$ 都有解」即 $m$ 必须属于**每一个**值域 $\left[c_2-c_1,\ 2+\left|c_1+c_2\right|\right]$：" "\n"
        r"$m\ge\max\left(c_2-c_1\right)=2$（取 $c_2=1,c_1=-1$）；且 $m\le\min\left(2+\left|c_1+c_2\right|\right)=2$（取 $c_1+c_2=0$）．" "\n"
        r"故 $\boxed{m=2}$．" "\n"
        r"**再求 $n$**：设 $k\left(t\right)=\left|t-c_1\right|-\left|t-c_2\right|$．" "\n"
        r"当 $t\le c_1$ 时 $k=c_1-c_2$；当 $t\ge c_2$ 时 $k=c_2-c_1$；当 $c_1<t<c_2$ 时 $k=2t-c_1-c_2\in\left(c_1-c_2,\ c_2-c_1\right)$．" "\n"
        r"故 $k$ 的值域恰为 $\left[c_1-c_2,\ c_2-c_1\right]$（连续区间）．" "\n"
        r"要对任意 $c_1,c_2$ 都有 $n$ 落在值域内，需 $n\in\bigcap\left[c_1-c_2,\ c_2-c_1\right]$．"
        r"因 $c_2-c_1$ 可任意小（取 $c_1=c_2$），交集只有 $\left\{0\right\}$，故 $\boxed{n=0}$．" "\n"
        r"所以 $m+n=2$，所求集合为 $\boxed{\left\{2\right\}}$．"
    ),
    'review': (
        r"① ⭐⭐ **本题的「对任意 $x_1,x_2$」是关键词**：不是「存在」，所以 $m$ 必须落在**所有**值域的交集里，"
        r"于是要同时用「下界的最大值」和「上界的最小值」两头夹——这正是 $m=2$ 唯一的原因．" "\n"
        r"② ⭐⭐ **$h$ 的最大值 $=2+\left|c_1+c_2\right|$**："
        r"$h\left(-1\right)=c_1+c_2+2$、$h\left(1\right)=2-c_1-c_2$，记 $s=c_1+c_2$，则 $\max\left\{s+2,2-s\right\}=2+\left|s\right|$ ✓" "\n"
        r"③ ⭐⭐ **$k$ 的值域是连续区间 $\left[c_1-c_2,c_2-c_1\right]$**：中间段 $2t-c_1-c_2$ 恰好取遍两端之间的值，"
        r"所以「有解」等价于 $n$ 在这个区间内——这是与 $h$ 的关键区别（$h$ 的最小值在中间平台上）．" "\n"
        r"④ 数值复核：取 $c_1=-1,c_2=1$，则 $h$ 值域 $\left[2,2\right]$（$h\equiv2$），$m=2$ ✓；"
        r"取 $c_1=c_2=0$，则 $k\equiv0$，$n=0$ ✓" "\n"
        r"**通法（「绝对值差/和」的值域）**：" "\n"
        r"① $\left|t-a\right|+\left|t-b\right|$ 是「桶形」：中间平台 $=\left|b-a\right|$，两端上升到 $\max$ 值；" "\n"
        r"② $\left|t-a\right|-\left|t-b\right|$ 是「梯形」：值域恰为 $\left[-\left|a-b\right|,\ \left|a-b\right|\right]$；" "\n"
        r"③ 「对任意参数都有解 $\Rightarrow$ 取所有值域的交集」，用「下确界的最大值」与「上确界的最小值」夹逼．"
    ),
    'difficulty': 0.82,
    'topics': ['M-T-182'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-182-V2',
}


T361_V1 = {
    'type': '解答',
    'stem_text': (
        r"设直线 $l:y=ax+1$ 与双曲线 $C:3x^{2}-y^{2}=1$ 相交于 $A,B$ 两点，$O$ 为坐标原点．" "\n"
        r"（1）$a$ 为何值时，以 $AB$ 为直径的圆过原点？" "\n"
        r"（2）是否存在实数 $a$，使 $\left|\overrightarrow{OA}\right|=\left|\overrightarrow{OB}\right|$ 且 $\overrightarrow{OA}+\overrightarrow{OB}=\lambda\left(2,1\right)$？"
        r"若存在，求 $a$ 的值；若不存在，说明理由．"
    ),
    'opts': [],
    'answer': (
        r"（1）$a=\pm1$；（2）不存在这样的实数 $a$（原书答案 $a=-2$ 有误，见 review）．"
    ),
    'analysis': (
        r"（1）联立得 $\left(3-a^{2}\right)x^{2}-2ax-2=0$，以 $AB$ 为直径的圆过原点 $\iff\overrightarrow{OA}\cdot\overrightarrow{OB}=0$；"
        r"（2）由韦达得 $x_1+x_2=\frac{2a}{3-a^{2}}$、$y_1+y_2=\frac{6}{3-a^{2}}$，两者之比恒为 $\frac3a$（与 $a^{2}$ 无关），"
        r"而 $\overrightarrow{OA}+\overrightarrow{OB}=\lambda\left(2,1\right)$ 要求该比值为 $\frac12$，得 $a=6$，与相交条件 $a^{2}<6$ 矛盾．"
    ),
    'solution': (
        r"联立 $\begin{cases}y=ax+1\\3x^{2}-y^{2}=1\end{cases}$，消去 $y$ 得 $\left(3-a^{2}\right)x^{2}-2ax-2=0$．" "\n"
        r"依题意 $3-a^{2}\ne0$，且 $\Delta=4a^{2}+8\left(3-a^{2}\right)=24-4a^{2}>0$，故 $\boxed{a^{2}<6\ \text{且}\ a^{2}\ne3}$．" "\n"
        r"设 $A\left(x_1,y_1\right)$、$B\left(x_2,y_2\right)$，由韦达定理：" "\n"
        r"$x_1+x_2=\dfrac{2a}{3-a^{2}}$，$x_1x_2=\dfrac{-2}{3-a^{2}}$．" "\n"
        r"又 $y_1+y_2=a\left(x_1+x_2\right)+2=\dfrac{2a^{2}}{3-a^{2}}+2=\dfrac{2a^{2}+6-2a^{2}}{3-a^{2}}=\dfrac{6}{3-a^{2}}$．" "\n"
        r"**第（1）问**" "\n"
        r"以 $AB$ 为直径的圆过原点 $\iff OA\perp OB\iff\overrightarrow{OA}\cdot\overrightarrow{OB}=0\iff x_1x_2+y_1y_2=0$．" "\n"
        r"又 $y_1y_2=\left(ax_1+1\right)\left(ax_2+1\right)=a^{2}x_1x_2+a\left(x_1+x_2\right)+1$，故" "\n"
        r"$\left(a^{2}+1\right)x_1x_2+a\left(x_1+x_2\right)+1=0$．" "\n"
        r"代入韦达（两式同分母 $3-a^{2}$，分子中 $a^{2}$ 项恰好抵消）：" "\n"
        r"$\left(a^{2}+1\right)\cdot\dfrac{-2}{3-a^{2}}+\dfrac{2a^{2}}{3-a^{2}}+1=\dfrac{-2}{3-a^{2}}+1=0$，" "\n"
        r"得 $3-a^{2}=2$，即 $a^{2}=1$，$\boxed{a=\pm1}$（均满足 $a^{2}<6$ 且 $a^{2}\ne3$）．" "\n"
        r"校验 $a=1$：方程 $2x^{2}-2x-2=0$ 即 $x^{2}-x-1=0$，$x_1x_2=-1$、$x_1+x_2=1$；" "\n"
        r"$x_1x_2+y_1y_2=2x_1x_2+\left(x_1+x_2\right)+1=2\left(-1\right)+1+1=0$ ✓" "\n"
        r"**第（2）问**" "\n"
        r"由 $\overrightarrow{OA}+\overrightarrow{OB}=\lambda\left(2,1\right)$ 得 $x_1+x_2=2\lambda$、$y_1+y_2=\lambda$．" "\n"
        r"**情形一**：$\lambda=0$．则 $x_1+x_2=0$，由 $x_1+x_2=\frac{2a}{3-a^{2}}$ 得 $a=0$；" "\n"
        r"此时 $y_1+y_2=\frac{6}{3-0}=2\ne0=\lambda$，矛盾．" "\n"
        r"**情形二**：$\lambda\ne0$．则 $\dfrac{y_1+y_2}{x_1+x_2}=\dfrac{\lambda}{2\lambda}=\dfrac12$．" "\n"
        r"而由韦达 $\dfrac{y_1+y_2}{x_1+x_2}=\dfrac{6/\left(3-a^{2}\right)}{2a/\left(3-a^{2}\right)}=\dfrac{6}{2a}=\dfrac3a$（$a\ne0$），" "\n"
        r"故 $\dfrac3a=\dfrac12$，得 $a=6$．但 $a^{2}=36>6$，$\Delta=24-4\times36=-120<0$，"
        r"**直线与双曲线根本不相交**，与题设矛盾．" "\n"
        r"两种情形均矛盾，故 $\boxed{\text{不存在这样的实数 }a}$．" "\n"
        r"（注：$a=0$ 时确有 $\left|\overrightarrow{OA}\right|=\left|\overrightarrow{OB}\right|$——此时直线 $y=1$ 与双曲线交于 $\left(\pm\sqrt{\tfrac23},1\right)$，"
        r"两点关于 $y$ 轴对称——但 $\overrightarrow{OA}+\overrightarrow{OB}=\left(0,2\right)$ 不是 $\lambda\left(2,1\right)$ 的形式．）"
    ),
    'review': (
        r"① ⭐⭐ **$\frac{y_1+y_2}{x_1+x_2}=\frac3a$ 与 $a^{2}$ 无关** —— 这是本题最关键的发现："
        r"$x_1+x_2=\frac{2a}{3-a^{2}}$、$y_1+y_2=\frac{6}{3-a^{2}}$ 分母相同，一除就把 $3-a^{2}$ 约掉了，"
        r"只剩 $\frac{6}{2a}=\frac3a$．**这使「存在性」立刻变成一个可解的简单方程**．" "\n"
        r"② ⭐⭐ **（1）的化简关键在「同分母」**：$\left(a^{2}+1\right)x_1x_2+a\left(x_1+x_2\right)+1$ 代入后"
        r"分子为 $-2\left(a^{2}+1\right)+2a^{2}=-2$，$a^{2}$ 项完全抵消，一步得 $\frac{-2}{3-a^{2}}+1=0$ ✓" "\n"
        r"③ ⚠ **原书答案 $a=-2$ 有误**（已登记 A 类勘误）．原书的推导是：" "\n"
        r"   由 $\left|\overrightarrow{OA}\right|=\left|\overrightarrow{OB}\right|$ 得 $\left(x_1+x_2\right)+a\left(y_1+y_2\right)=0$，"
        r"即 $\frac{y_1+y_2}{x_1+x_2}=-\frac1a$；再与 $\frac{y_1+y_2}{x_1+x_2}=\frac12$ 联立得 $a=-2$．" "\n"
        r"   **错误在于只推了必要条件、没有回代检验**：$a=-2$ 时由韦达得 $x_1+x_2=4$、$y_1+y_2=-6$，"
        r"比值是 $-\frac32$ 而不是 $\frac12$，且 $\left|\overrightarrow{OA}\right|\approx0.610$、$\left|\overrightarrow{OB}\right|\approx6.755$ 并不相等 ✓（数值已验证）" "\n"
        r"   事实上 $\left(x_1+x_2\right)+a\left(y_1+y_2\right)=\frac{2a}{3-a^{2}}+\frac{6a}{3-a^{2}}=\frac{8a}{3-a^{2}}=0\Rightarrow a=0$，"
        r"与 $\frac3a=\frac12\Rightarrow a=6$ **不能同时成立**——两条路径互不相容，正是「不存在」的根源．" "\n"
        r"④ 数值复核（$a=-2$）：联立得 $-x^{2}+4x-2=0$，$x=2\pm\sqrt2$；" "\n"
        r"   $A\left(3.414,-5.828\right)$、$B\left(0.586,-0.172\right)$；$\overrightarrow{OA}+\overrightarrow{OB}=\left(4,-6\right)$，" "\n"
        r"   若要等于 $\lambda\left(2,1\right)$ 需 $\lambda=2$ 且 $\lambda=-6$，矛盾 ✓" "\n"
        r"**通法（直线与双曲线相交的存在性）**：" "\n"
        r"① 联立后必写 $3-a^{2}\ne0$ 与 $\Delta>0$，得到 $a$ 的**可行域**；" "\n"
        r"② 向量条件一律翻译成坐标关系（和向量 $\Rightarrow$ 坐标之比，等长 $\Rightarrow$ 平方差分解）；" "\n"
        r"③ 由必要条件解出的 $a$ **必须回代检验**，并核对是否落在可行域内——这是「存在性」问题的收尾步骤．"
    ),
    'difficulty': 0.76,
    'topics': ['M-T-361'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-361-V1',
}

T145_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知函数 $f\left(x\right)=\mathrm e^{x}-\dfrac12x^{2}+x^{3}$，若 $x\in\mathbf{R}$ 时，恒有 $f'\left(x\right)\ge3x^{2}+ax+b$，"
        r"则 $ab+b$ 的最大值为（　　）"
    ),
    'opts': [
        ('A', r"$\sqrt{\mathrm e}$"),
        ('B', r"$\dfrac{\sqrt{\mathrm e}}2$"),
        ('C', r"$\dfrac{\mathrm e}2$"),
        ('D', r"$\mathrm e$"),
    ],
    'answer': r"C",
    'analysis': (
        r"$f'\left(x\right)=\mathrm e^{x}-x+3x^{2}$，条件化为 $\mathrm e^{x}-x-ax-b\ge0$ 恒成立．"
        r"令 $g\left(x\right)=\mathrm e^{x}-x-ax$，则 $g_{\min}\ge b$，得 $b\left(1+a\right)\le t^{2}-t^{2}\ln t$（$t=1+a>0$），"
        r"再求 $h\left(t\right)=t^{2}\left(1-\ln t\right)$ 的最大值．"
    ),
    'solution': (
        r"$f'\left(x\right)=\mathrm e^{x}-x+3x^{2}$，条件即 $\mathrm e^{x}-x+3x^{2}\ge3x^{2}+ax+b$ 对一切 $x\in\mathbf{R}$ 成立，" "\n"
        r"也就是 $\mathrm e^{x}-x-ax-b\ge0$ 恒成立．" "\n"
        r"令 $g\left(x\right)=\mathrm e^{x}-x-ax$，则 $g'\left(x\right)=\mathrm e^{x}-1-a$．" "\n"
        r"当 $a<-1$ 时，$1+a<0$，$g'\left(x\right)=\mathrm e^{x}-\left(1+a\right)>0$ 恒成立，$g$ 单调递增；"
        r"而 $x\to-\infty$ 时 $g\left(x\right)\to-\infty$，不可能恒 $\ge b$，故 $a<-1$ 不合．" "\n"
        r"当 $a=-1$ 时，$g\left(x\right)=\mathrm e^{x}$，$g_{\min}\to0$（取不到），$b\le0$，$ab+b=b\left(1+a\right)=0$．" "\n"
        r"当 $a>-1$ 时，令 $g'\left(x\right)=0$ 得 $x=\ln\left(1+a\right)$；"
        r"$g$ 在 $\left(-\infty,\ln\left(1+a\right)\right)$ 递减、在 $\left(\ln\left(1+a\right),+\infty\right)$ 递增，故" "\n"
        r"$g_{\min}=g\left(\ln\left(1+a\right)\right)=\mathrm e^{\ln\left(1+a\right)}-\ln\left(1+a\right)-a\ln\left(1+a\right)=\left(1+a\right)-\left(1+a\right)\ln\left(1+a\right)$．" "\n"
        r"由 $g_{\min}\ge b$ 得 $b\le\left(1+a\right)\left[1-\ln\left(1+a\right)\right]$．" "\n"
        r"因 $1+a>0$，两边同乘 $\left(1+a\right)$：" "\n"
        r"$ab+b=b\left(1+a\right)\le\left(1+a\right)^{2}\left[1-\ln\left(1+a\right)\right]$．" "\n"
        r"令 $t=1+a>0$，$h\left(t\right)=t^{2}\left(1-\ln t\right)$，则" "\n"
        r"$h'\left(t\right)=2t\left(1-\ln t\right)+t^{2}\cdot\left(-\dfrac1t\right)=2t-2t\ln t-t=t\left(1-2\ln t\right)$．" "\n"
        r"当 $0<t<\sqrt{\mathrm e}$ 时 $h'\left(t\right)>0$，$h$ 递增；当 $t>\sqrt{\mathrm e}$ 时 $h'\left(t\right)<0$，$h$ 递减．" "\n"
        r"故 $h_{\max}=h\left(\sqrt{\mathrm e}\right)=\mathrm e\left(1-\ln\sqrt{\mathrm e}\right)=\mathrm e\left(1-\dfrac12\right)=\dfrac{\mathrm e}2$．" "\n"
        r"所以 $ab+b$ 的最大值为 $\boxed{\dfrac{\mathrm e}2}$，选 $\mathrm{C}$．"
    ),
    'review': (
        r"① ⭐⭐ **本题两次换元**：先令 $t=1+a$ 把 $\left(1+a\right)^{2}\left[1-\ln\left(1+a\right)\right]$ 变成 $t^{2}\left(1-\ln t\right)$，"
        r"再求导得 $h'=t\left(1-2\ln t\right)$，最值点 $t=\sqrt{\mathrm e}$．" "\n"
        r"② ⭐⭐ **$ab+b=b\left(1+a\right)$ 要「凑出同一个因式」**："
        r"由 $b\le\left(1+a\right)\left[1-\ln\left(1+a\right)\right]$ 两边同乘 $\left(1+a\right)>0$，"
        r"左边正好是 $ab+b$——**这一步是命题人设计的**，否则无法把 $a,b$ 合成一个变量．" "\n"
        r"③ ⭐⭐ **$a=-1$ 要单独讨论**：此时 $1+a=0$，$g\left(x\right)=\mathrm e^{x}$ 无最小值（下确界 $0$ 取不到），"
        r"$b\le0$，$ab+b=0<\frac{\mathrm e}2$，不影响最大值，但**不能跳过**．" "\n"
        r"④ 选项还原：原书 OCR 把四个选项塌成 `e`、`e/2`、`e/2`、`e` 四个值，"
        r"按「根号常丢失」的规律与答案 C $=\frac{\mathrm e}2$，还原为 $\sqrt{\mathrm e},\frac{\sqrt{\mathrm e}}2,\frac{\mathrm e}2,\mathrm e$ ✓（顺序待纸质书核对）" "\n"
        r"⑤ 原书详解写 $h'=2t-2t\ln t+t$，末项应为 $-t$（笔误），但结果 $t\left(1-2\ln t\right)$ 正确 ✓" "\n"
        r"⑥ 数值复核：$t=\sqrt{\mathrm e}=1.6487$ 时 $h=2.718\times\left(1-0.5\right)=1.359=\frac{\mathrm e}2$ ✓；"
        r"$t=1$ 时 $h=1<1.359$ ✓；$t=2$ 时 $h=4\times\left(1-0.693\right)=1.228<1.359$ ✓" "\n"
        r"**通法（恒成立求双参数之积）**：" "\n"
        r"① $f'\left(x\right)\ge\cdots$ 恒成立 $\Rightarrow$ 移项构造函数 $g$，条件转为 $g_{\min}\ge b$；" "\n"
        r"② $g_{\min}$ 用导数求（注意 $a$ 的范围讨论）；" "\n"
        r"③ 把所求式凑成 $b\cdot\left(1+a\right)$ 的形式，两边同乘正数后换元求最值．"
    ),
    'difficulty': 0.75,
    'topics': ['M-T-145'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-145-E1',
}

QS = [
    T391_V1, T391_V2, T389_V1, T395_V1,
    T268_V2, T257_V2, T274_E1,
    T031_E1, T031_V2,
    T182_V2,
    T361_V1,
    T145_E1,
]
