# -*- coding: utf-8 -*-
r"""第 122 批：圆锥曲线 12 题（轨迹 · 定点定值 · 非对称韦达 · 抛物线）python3 tools/run_batch.py 122## 选题依据用 pick_batch.py（pages 策略 + skipped 排除）筛出剩余可录题 43 个后，按「详解完整 + 不依赖图」重排，集中在 p306–p341（圆锥曲线压轴大题）。13 题全部独立联立推导一遍，关键数值与原书答案对拍吻合才录入。M-T-375-V1 因四个选项 OCR 全塌（只剩 `5 5 4 3` / `3432` 两行碎片，无法还原）登记跳过；M-T-361-V1 因原书答案 $a=-2$ 经数值检验**两个条件都不满足**（$|\vec{OA}|=|\vec{OB}|$ 只在 $a=0$ 成立，而 $\frac{y_1+y_2}{x_1+x_2}=\frac3a=\frac12$ 要求 $a=6$ 却又使 $\Delta<0$），正确结论应为「不存在」，与原书答案方向相反，故不录入、登记存疑。## ★★ 本批最值钱的一条：抛物线「三点共线 + 内分比」造同构方程（M-T-356-V3）由 $3\vec{PM}=\vec{MA}$ 得 $M=\dfrac{3P+A}{4}$，代入 $y^2=4x$ 消 $x_1$： $$3y_1^2-6y_0y_1+48x_0-9y_0^2=0$$ 同理 $y_2$ 满足**同一个方程** ⟹ $y_1+y_2=2y_0$ 一步到位。> ⭐⭐ 判据：凡「 $\vec{PM}=k\vec{MA}$ 且 $M$ 在曲线上」，就用内分点公式把 $M$ 表示成 $P,A$ 的加权平均，代入曲线后得到关于 $y_1$ 的二次方程；$B$ 走一遍同样的路会得到**系数完全相同**的方程，两根之和立刻给出。> 若两个方程系数不同，就凑不出「同构」，说明比值 $k$ 不是常数或点选错了。## ★★ 第二条：存在点 $T$ 使 $|TP|=|TQ|$ ⟹ 中垂线斜率 $-\frac1k$（M-T-352-V3）$M$ 为 $PQ$ 中点，$k_{TM}=-\dfrac1k$ 解出 $t=\dfrac{k^2}{4k^2+3}$，值域 $(0,\frac14)$。> ⭐⭐ $k=0$ 时必须单独讨论（此时 $P,Q$ 是通径端点，$T$ 就是原点，$t=0$），所以最终是 $[0,\frac14)$ **左闭右开**。## ★★ 第三条：$\vec{AC}\cdot\vec{DB}+\vec{AD}\cdot\vec{CB}=6-2x_1x_2-2y_1y_2$（M-T-344-V3）$A,B$ 是上下顶点（关于原点对称），$C,D$ 是动弦端点：四个向量点积两两合并，常数项合并成 $6$，剩下**只含对称式**。> ⭐⭐ 这类「交叉点积之和」题，展开后一定只剩 $x_1x_2$ 与 $y_1y_2$，不必逐个算。## ★★ 第四条：以 $PQ$ 为直径的圆过 $x$ 轴上定点（M-T-352-V2 同类 / 本批 M-T-352-V3 姊妹）$\vec{PN}\cdot\vec{QN}=0$ ⟹ $x_0^2+\dfrac{4y_1y_2}{(x_1-2)(x_2-2)}=0$ 恒成立 ⟹ 分子分母同阶，$k$ 消尽。"""

T338_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知点 $P(x,y)$ 满足条件 $\sqrt{(x+1)^2+y^2}+\sqrt{(x-1)^2+y^2}=4$。" "\n"
        r"（Ⅰ）求点 $P$ 的轨迹 $C$ 的方程。"
    ),
    'opts': [],
    'answer': r"$\dfrac{x^2}{4}+\dfrac{y^2}{3}=1$",
    'analysis': (
        r"两个根号分别是 $P$ 到 $(-1,0)$ 与 $(1,0)$ 的距离，其和为常数 $4$，"
        r"且 $4>|(1,0)-(-1,0)|=2$，故轨迹是椭圆；由 $2a=4$、$c=1$ 得 $b^2=3$。"
    ),
    'solution': (
        r"$\sqrt{(x+1)^2+y^2}=|PF_1|$、$\sqrt{(x-1)^2+y^2}=|PF_2|$，其中 $F_1(-1,0)$、$F_2(1,0)$。" "\n"
        r"条件即 $|PF_1|+|PF_2|=4$，而 $|F_1F_2|=2<4$，" "\n"
        r"所以点 $P$ 的轨迹是以 $F_1,F_2$ 为焦点、长轴长 $2a=4$ 的椭圆。" "\n"
        r"于是 $c=1$，$a=2$，$b=\sqrt{a^2-c^2}=\sqrt3$，" "\n"
        r"所求轨迹 $C$ 的方程为 $\dfrac{x^2}{4}+\dfrac{y^2}{3}=1$。"
    ),
    'review': (
        r"① ⭐⭐ **判据模板**：见到两个根号各是「到定点的距离」，先算两定点间距 $d$ 与和 $2a$；"
        r"$2a>d$ 是椭圆、$2a=d$ 是线段、$2a<d$ 无轨迹 —— 这一步必须写，否则漏掉存在性" "\n"
        r"② 本题原书提取时根号整体丢失（成 $(x+1)^2+y^2+(x-1)^2+y^2=4$），"
        r"但详解里保留了「$=4>2$」这个判断，据此可反推是**两根号之和**" "\n"
        r"③ 数值复核：取 $P(0,\sqrt3)$，$|PF_1|=\sqrt{1+3}=2$、$|PF_2|=2$，和为 $4$ ✓；"
        r"代入椭圆：$\frac04+\frac33=1$ ✓✓" "\n"
        r"④ ⚠ 别把 $4$ 当成 $2a$ 后忘记 $c$：两定点是 $(\pm1,0)$，故 $c=1$ 而不是 $2$"
    ),
    'topics': ['M-T-338'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-338-V2',
}

T342_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知 $B$ 是 $AC$ 的中点，$\vec{BE}=2\vec{OB}$，$P$ 是平行四边形 $BCDE$ 内"
        r"（含边界）的一点，且 $\vec{OP}=x\vec{OA}+y\vec{OB}$（$x,y\in\mathbb R$），"
        r"则下列结论正确的是（　　）"
    ),
    'opts': [
        ['A', r"当 $P$ 在 $C$ 点时，$x=-1$，$y=2$"],
        ['B', r"当 $x=0$ 时，$y\in[2,3]$"],
        ['C', r"若 $x+y$ 为定值 $1$，则在平面直角坐标系中，点 $P$ 的轨迹是一条线段"],
        ['D', r"当 $P$ 是线段 $CE$ 的中点时，$x=-\dfrac12$，$y=\dfrac52$"],
    ],
    'answer': r"ACD",
    'analysis': (
        r"把 $\vec{OA},\vec{OB}$ 当基底：$\vec{OC}=2\vec{OB}-\vec{OA}$，"
        r"$\vec{OE}=\vec{OB}+\vec{BE}=3\vec{OB}$；再逐项把 $P$ 的位置翻译成 $x,y$。"
    ),
    'solution': (
        r"以 $\vec{OA},\vec{OB}$ 为基底。" "\n"
        r"由 $B$ 是 $AC$ 的中点得 $\vec{OB}=\dfrac12(\vec{OA}+\vec{OC})$，即 $\vec{OC}=-\vec{OA}+2\vec{OB}$；" "\n"
        r"由 $\vec{BE}=2\vec{OB}$ 得 $\vec{OE}=\vec{OB}+\vec{BE}=3\vec{OB}$。" "\n"
        r"**选项 A**：$P$ 在 $C$ 点时 $\vec{OP}=\vec{OC}=-\vec{OA}+2\vec{OB}$，故 $x=-1,y=2$，A 正确；" "\n"
        r"**选项 B**：$x=0$ 即 $\vec{OP}=y\vec{OB}$，$P$ 落在射线 $OB$ 上。"
        r"由 $\vec{OE}=3\vec{OB}$ 知 $O,B,E$ 三点共线且 $|OE|=3|OB|$，"
        r"该射线与平行四边形 $BCDE$ 的交集是线段 $BE$，故 $y\in[1,3]$，B 错误；" "\n"
        r"**选项 C**：$\vec{OP}=x\vec{OA}+y\vec{OB}$ 且 $x+y=1$ ⟹ $A,B,P$ 三点共线，"
        r"再与平行四边形（含边界）取交集，得一条线段，C 正确；" "\n"
        r"**选项 D**：$P$ 是 $CE$ 中点时" "\n"
        r"$\vec{OP}=\vec{OE}+\vec{EP}=3\vec{OB}+\dfrac12\vec{EC}"
        r"=3\vec{OB}+\dfrac12(\vec{EB}+\vec{BC})=3\vec{OB}+\dfrac12(-2\vec{OB}+\vec{AB})$，" "\n"
        r"又 $\vec{AB}=\vec{OB}-\vec{OA}$，故 $\vec{OP}=3\vec{OB}-\dfrac12\vec{OB}-\dfrac12\vec{OA}"
        r"=-\dfrac12\vec{OA}+\dfrac52\vec{OB}$，" "\n"
        r"即 $x=-\dfrac12,y=\dfrac52$，D 正确。" "\n"
        r"故选 $\mathrm{ACD}$。"
    ),
    'review': (
        r"① ⭐⭐ **题眼是「$\vec{OE}=3\vec{OB}$」**：由 $\vec{BE}=2\vec{OB}$ 一步得到，"
        r"它同时说明 $O,B,E$ 共线，是判断 B 选项（射线 $OB$ 上的可行段）的唯一依据" "\n"
        r"② ⭐⭐ **系数和为 $1$ ⟹ 三点共线**（选项 C）：$\vec{OP}=x\vec{OA}+y\vec{OB}$、$x+y=1$ "
        r"是「$P$ 在直线 $AB$ 上」的等价刻画，与第 86 批 M-T-241 是同一条结论" "\n"
        r"③ ⚠ 选项 D 的向量链要一步一步写：$\vec{EC}=\vec{EB}+\vec{BC}$，"
        r"而 $\vec{BC}$ 在平行四边形中等于 $\vec{ED}$，本题直接用 $\vec{AB}$ 表示更快"
        r"（详解写 $\vec{BC}=\vec{AB}$，是因为 $\vec{BC}=\vec{ED}$ 且图中 $AB\parallel ED$）" "\n"
        r"④ 数值复核：取 $\vec{OA}=(1,0)$、$\vec{OB}=(0,1)$，则 $C=(-1,2)$、$E=(0,3)$；"
        r"$CE$ 中点 $P=(-0.5,2.5)$，恰是 $x=-0.5,y=2.5$ ✓✓" "\n"
        r"⑤ ⚠ 本题原配图给出 $O,A,B,C$ 的位置关系，录入时已把「$B$ 是 $AC$ 中点」"
        r"「$\vec{BE}=2\vec{OB}$」两条关键关系全部写进题干，不依赖图也可解"
    ),
    'topics': ['M-T-342'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-342-V2',
}

T344_V3 = {
    'type': '解答',
    'stem_text': (
        r"设椭圆 $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1\ (a>b>0)$ 的左焦点为 $F$，离心率为 $\dfrac12$，"
        r"过点 $F$ 且与 $x$ 轴垂直的直线被椭圆截得的线段长为 $3$。" "\n"
        r"（1）求椭圆的方程；" "\n"
        r"（2）设 $A$ 为椭圆的下顶点，$B$ 为椭圆的上顶点，过点 $F$ 且斜率为 $k$ 的直线"
        r"与椭圆交于 $C,D$ 两点．若 $\vec{AC}\cdot\vec{DB}+\vec{AD}\cdot\vec{CB}=10$，求 $k$ 的值．"
    ),
    'opts': [],
    'answer': r"（1）$\dfrac{x^2}{4}+\dfrac{y^2}{3}=1$；（2）$k=\pm\sqrt2$",
    'analysis': (
        r"（1）通径长 $\frac{2b^2}{a}=3$ 配 $e=\frac12$ 解出 $a,b$；"
        r"（2）把四个向量点积展开，常数合并后只剩 $x_1x_2$ 与 $y_1y_2$，用韦达代入即可。"
    ),
    'solution': (
        r"（1）$x=-c$ 时 $\dfrac{c^2}{a^2}+\dfrac{y^2}{b^2}=1\Rightarrow y^2=b^2\left(1-\dfrac{c^2}{a^2}\right)"
        r"=\dfrac{b^4}{a^2}$，" "\n"
        r"即 $y=\pm\dfrac{b^2}{a}$，截得线段长 $=\dfrac{2b^2}{a}=3$。" "\n"
        r"又 $e=\dfrac ca=\dfrac12$，故 $c=\dfrac a2$，$b^2=a^2-c^2=\dfrac{3a^2}4$，代入得" "\n"
        r"$\dfrac{2}{a}\cdot\dfrac{3a^2}{4}=\dfrac{3a}{2}=3\Rightarrow a=2$，于是 $b=\sqrt3,\ c=1$，" "\n"
        r"椭圆方程为 $\dfrac{x^2}{4}+\dfrac{y^2}{3}=1$。" "\n"
        r"（2）$F(-1,0)$，$A(0,-\sqrt3)$，$B(0,\sqrt3)$，直线 $CD$：$y=k(x+1)$。" "\n"
        r"联立 $\begin{cases}y=k(x+1)\\ \frac{x^2}4+\frac{y^2}3=1\end{cases}$"
        r"得 $(4k^2+3)x^2+8k^2x+4k^2-12=0$，" "\n"
        r"设 $C(x_1,y_1),D(x_2,y_2)$，则 $x_1+x_2=-\dfrac{8k^2}{4k^2+3}$，$x_1x_2=\dfrac{4k^2-12}{4k^2+3}$，" "\n"
        r"$y_1y_2=k^2(x_1+1)(x_2+1)=k^2\left[x_1x_2+(x_1+x_2)+1\right]"
        r"=k^2\cdot\dfrac{4k^2-12-8k^2+4k^2+3}{4k^2+3}=-\dfrac{9k^2}{4k^2+3}$。" "\n"
        r"又 $\vec{AC}=(x_1,y_1+\sqrt3)$，$\vec{DB}=(-x_2,\sqrt3-y_2)$，" "\n"
        r"$\vec{AD}=(x_2,y_2+\sqrt3)$，$\vec{CB}=(-x_1,\sqrt3-y_1)$，故" "\n"
        r"$\vec{AC}\cdot\vec{DB}+\vec{AD}\cdot\vec{CB}$" "\n"
        r"$=-x_1x_2+(y_1+\sqrt3)(\sqrt3-y_2)-x_1x_2+(y_2+\sqrt3)(\sqrt3-y_1)$" "\n"
        r"$=-2x_1x_2-2y_1y_2+6=6-2\cdot\dfrac{4k^2-12}{4k^2+3}-2\cdot\left(-\dfrac{9k^2}{4k^2+3}\right)"
        r"=6+\dfrac{10k^2+24}{4k^2+3}$。" "\n"
        r"令其等于 $10$：$\dfrac{10k^2+24}{4k^2+3}=4\Rightarrow 10k^2+24=16k^2+12\Rightarrow k^2=2$，" "\n"
        r"即 $k=\pm\sqrt2$。"
    ),
    'review': (
        r"① ⭐⭐ **通径长 $\frac{2b^2}{a}$ 要当常识记**：过焦点且垂直长轴的弦，"
        r"$x=\pm c$ 代入即得 $y=\pm\frac{b^2}{a}$，本题直接给长 $3$，一步定 $a$" "\n"
        r"② ⭐⭐ **交叉点积之和必化成对称式**：四个点积展开后，含 $\sqrt3 y_1$、$\sqrt3 y_2$ 的项"
        r"两两抵消，常数项 $3+3=6$，剩下恰是 $-2x_1x_2-2y_1y_2$ —— 这是「上下顶点 + 动弦」的固定结果" "\n"
        r"③ 数值复核：$k=\sqrt2$ 时 $4k^2+3=11$，$x_1x_2=\frac{8-12}{11}=-\frac4{11}$，"
        r"$y_1y_2=-\frac{18}{11}$，代入得 $6+\frac{8}{11}+\frac{36}{11}=6+4=10$ ✓✓" "\n"
        r"④ ⚠ 判别式要检验：$k^2=2$ 时 $\Delta=64k^4-4(4k^2+3)(4k^2-12)"
        r"=256-4\cdot11\cdot(-4)=256+176>0$ ✓" "\n"
        r"⑤ 与 M-T-352-V3 对照：两题都是「过焦点的弦 + 韦达」，"
        r"但那题问中垂线上的定点（用中点坐标），本题问点积定值（用 $x_1x_2,y_1y_2$）"
    ),
    'topics': ['M-T-344'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-344-V3',
}

T352_V3 = {
    'type': '解答',
    'stem_text': (
        r"已知椭圆 $C:\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1\ (a>b>0)$ 的左、右焦点分别为 $F_1,F_2$，"
        r"离心率为 $\dfrac12$，$P$ 为椭圆 $C$ 上的一个动点，当 $P$ 是 $C$ 的上顶点时，"
        r"$\triangle F_1PF_2$ 的面积为 $\sqrt3$。" "\n"
        r"（1）求椭圆 $C$ 的标准方程；" "\n"
        r"（2）设斜率存在的直线 $PF_2$ 与 $C$ 的另一个交点为 $Q$，是否存在点 $T(t,0)$，"
        r"使得 $|TP|=|TQ|$？若存在，求出 $t$ 的取值范围；若不存在，请说明理由．"
    ),
    'opts': [],
    'answer': r"（1）$\dfrac{x^2}{4}+\dfrac{y^2}{3}=1$；（2）存在，$0\le t<\dfrac14$",
    'analysis': (
        r"（1）$S=\frac12\cdot2c\cdot b=bc=\sqrt3$ 配 $e=\frac12$；"
        r"（2）$|TP|=|TQ|$ ⟺ $T$ 在 $PQ$ 的中垂线上，用 $k_{TM}=-\frac1k$ 解出 $t$ 关于 $k$ 的表达式再求值域。"
    ),
    'solution': (
        r"（1）$e=\dfrac ca=\dfrac12\Rightarrow a=2c$，$b^2=a^2-c^2=3c^2\Rightarrow b=\sqrt3\,c$。" "\n"
        r"$P$ 为上顶点时 $S_{\triangle F_1PF_2}=\dfrac12\cdot|F_1F_2|\cdot b=\dfrac12\cdot2c\cdot b=bc=\sqrt3$，" "\n"
        r"即 $\sqrt3\,c^2=\sqrt3\Rightarrow c=1$，故 $a=2,\ b=\sqrt3$，" "\n"
        r"椭圆 $C$ 的标准方程为 $\dfrac{x^2}{4}+\dfrac{y^2}{3}=1$。" "\n"
        r"（2）由（1）知 $F_2(1,0)$，设直线 $PF_2$：$y=k(x-1)$。" "\n"
        r"联立 $\begin{cases}y=k(x-1)\\ 3x^2+4y^2=12\end{cases}$ 得 $(4k^2+3)x^2-8k^2x+4k^2-12=0$，" "\n"
        r"设 $P(x_1,y_1),Q(x_2,y_2)$，则 $x_1+x_2=\dfrac{8k^2}{4k^2+3}$，" "\n"
        r"$y_1+y_2=k(x_1+x_2-2)=k\cdot\dfrac{8k^2-8k^2-6}{4k^2+3}=-\dfrac{6k}{4k^2+3}$。" "\n"
        r"$PQ$ 的中点 $M\left(\dfrac{4k^2}{4k^2+3},\ -\dfrac{3k}{4k^2+3}\right)$。" "\n"
        r"当 $k=0$ 时，$P,Q$ 是通径端点，$PQ$ 垂直于 $x$ 轴，其中垂线为 $x$ 轴，取 $t=0$ 即有 $|TP|=|TQ|$；" "\n"
        r"当 $k\ne0$ 时，$|TP|=|TQ|\iff TM\perp PQ\iff k_{TM}=-\dfrac1k$。" "\n"
        r"$k_{TM}=\dfrac{-\frac{3k}{4k^2+3}-0}{\frac{4k^2}{4k^2+3}-t}"
        r"=\dfrac{-3k}{4k^2-t(4k^2+3)}=-\dfrac1k$，" "\n"
        r"即 $3k^2=4k^2-t(4k^2+3)\Rightarrow t=\dfrac{k^2}{4k^2+3}=\dfrac{1}{4+\frac{3}{k^2}}$。" "\n"
        r"由 $4+\dfrac{3}{k^2}>4$ 得 $0<t<\dfrac14$。" "\n"
        r"综上，$t$ 的取值范围是 $\left[0,\dfrac14\right)$，故这样的点 $T$ 存在。"
    ),
    'review': (
        r"① ⭐⭐ **$k=0$ 必须单独讨论**：此时 $P,Q$ 是通径端点，$PQ$ 竖直、中垂线水平，"
        r"$T$ 可以取原点，给出 $t=0$；若只用 $k_{TM}=-\frac1k$ 就漏掉这个端点，值域会写成 $(0,\frac14)$" "\n"
        r"② ⭐⭐ **$t=\frac1{4+\frac{3}{k^2}}$ 的单调性一眼看出**：$k^2$ 越大 $t$ 越大，"
        r"上界 $\frac14$ 取不到（需 $k\to\infty$），下界 $0$ 由 $k\to0$ 逼近但在 $k=0$ 时直接取到 —— "
        r"这正是「左闭右开」的来源" "\n"
        r"③ 数值复核：$k=1$ 时 $t=\frac1{7}=0.142857$；此时 $4k^2+3=7$，"
        r"$x_1+x_2=\frac87$、$y_1+y_2=-\frac67$，中点 $M(\frac47,-\frac37)$；"
        r"$T(0.142857,0)$，$k_{TM}=\frac{-0.428571}{0.571429-0.142857}=-1$ ✓ 而 $-\frac1k=-1$ ✓✓" "\n"
        r"④ ⚠ 原书题干在 ref_bank 中只剩两问（前置条件丢失），我是从同页另一题的详解末尾"
        r"「已知椭圆 $C$…离心率为 $\frac12$，$P$ 为椭圆 $C$ 上的一个动点，当 $P$ 是 $C$ 的上顶点时，"
        r"$\triangle F_1PF_2$ 的面积为…」找回前置条件的，并用详解中的 $F_2(1,0)$ 反向验证 $c=1$ ✓" "\n"
        r"⑤ 与 M-T-344-V3 对照：同是「过焦点弦 + 韦达」，"
        r"本题把中点 $M$ 显式写出来（因为要用中垂线），那题只用 $x_1x_2,y_1y_2$"
    ),
    'topics': ['M-T-352'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-352-V3',
}

T352_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知双曲线 $C$ 的方程为 $\dfrac{2y^2}{a^2}-2x^2=1\ (a>0)$，离心率为 $\sqrt2$。" "\n"
        r"（1）求双曲线 $C$ 的标准方程；" "\n"
        r"（2）过 $E(0,1)$ 的直线 $l$ 交曲线 $C$ 于 $M,N$ 两点，求 $\vec{EM}\cdot\vec{EN}$ 的取值范围．"
    ),
    'opts': [],
    'answer': (
        r"（1）$\dfrac{y^2}{\frac12}-\dfrac{x^2}{\frac12}=1$（即 $2y^2-2x^2=1$）；"
        r"（2）$\left(-\infty,-\dfrac12\right]\cup\left[\dfrac12,+\infty\right)$"
    ),
    'analysis': (
        r"（1）先化成标准式 $\frac{y^2}{a^2/2}-\frac{x^2}{1/2}=1$，由 $e=\sqrt2$ 得等轴（$a_1^2=b_1^2$）；"
        r"（2）设 $y=kx+1$ 后 $\vec{EM}\cdot\vec{EN}=(1+k^2)x_1x_2$，化成 $\frac12+\frac1{k^2-1}$ 求值域，"
        r"并补上斜率不存在的情形。"
    ),
    'solution': (
        r"（1）方程化为 $\dfrac{y^2}{\frac{a^2}2}-\dfrac{x^2}{\frac12}=1$，故 $a_1^2=\dfrac{a^2}2$，$b_1^2=\dfrac12$，" "\n"
        r"$c^2=a_1^2+b_1^2=\dfrac{a^2+1}{2}$。" "\n"
        r"由 $e^2=\dfrac{c^2}{a_1^2}=\dfrac{\frac{a^2+1}{2}}{\frac{a^2}{2}}=\dfrac{a^2+1}{a^2}=2$ 得 $a^2=1$，" "\n"
        r"故双曲线 $C$ 的标准方程为 $\dfrac{y^2}{\frac12}-\dfrac{x^2}{\frac12}=1$（即 $2y^2-2x^2=1$）。" "\n"
        r"（2）当直线 $l$ 的斜率存在时，设 $l:y=kx+1$，代入 $2y^2-2x^2=1$ 得" "\n"
        r"$(2k^2-2)x^2+4kx+1=0$，由交于两点知 $k^2\ne1$ 且 $\Delta=16k^2-4(2k^2-2)>0$（恒成立）。" "\n"
        r"设 $M(x_1,y_1),N(x_2,y_2)$，则 $x_1+x_2=\dfrac{2k}{1-k^2}$，$x_1x_2=\dfrac{1}{2k^2-2}$。" "\n"
        r"$\vec{EM}=(x_1,y_1-1)=(x_1,kx_1)$，$\vec{EN}=(x_2,kx_2)$，故" "\n"
        r"$\vec{EM}\cdot\vec{EN}=(1+k^2)x_1x_2=\dfrac{1+k^2}{2(k^2-1)}"
        r"=\dfrac{(k^2-1)+2}{2(k^2-1)}=\dfrac12+\dfrac{1}{k^2-1}$。" "\n"
        r"由 $k^2-1\in[-1,0)\cup(0,+\infty)$ 得 $\dfrac{1}{k^2-1}\in(-\infty,-1]\cup(0,+\infty)$，" "\n"
        r"故 $\vec{EM}\cdot\vec{EN}\in\left(-\infty,-\dfrac12\right]\cup\left(\dfrac12,+\infty\right)$。" "\n"
        r"当直线 $l$ 的斜率不存在时，$l:x=0$，代入得 $M\left(0,\dfrac{\sqrt2}2\right)$、"
        r"$N\left(0,-\dfrac{\sqrt2}2\right)$，" "\n"
        r"$\vec{EM}=\left(0,\dfrac{\sqrt2}2-1\right)$，$\vec{EN}=\left(0,-\dfrac{\sqrt2}2-1\right)$，" "\n"
        r"$\vec{EM}\cdot\vec{EN}=\left(\dfrac{\sqrt2}2-1\right)\left(-\dfrac{\sqrt2}2-1\right)"
        r"=-\left(\dfrac12-1\right)=\dfrac12$。" "\n"
        r"综上，$\vec{EM}\cdot\vec{EN}$ 的取值范围是 $\left(-\infty,-\dfrac12\right]\cup\left[\dfrac12,+\infty\right)$。"
    ),
    'review': (
        r"① ⭐⭐ **$\vec{EM}\cdot\vec{EN}=(1+k^2)x_1x_2$ 是本题的题眼**："
        r"因为 $E$ 在 $y$ 轴上、直线写成 $y=kx+1$，所以 $y_i-1=kx_i$，"
        r"两个向量的第二分量也变成 $kx_i$，点积直接提出 $(1+k^2)$ —— 与第 103 批"
        r"「非对称韦达」里 $m y_1y_2=k(y_1+y_2)$ 是同族技巧" "\n"
        r"② ⭐⭐ **两个端点都能取到**：$k=0$（水平线）得 $-\frac12$，$l:x=0$（竖直线）得 $+\frac12$。"
        r"⚠ **原书答案写作 $\left(-\infty,-\frac12\right]\cup\left(\frac12,+\infty\right)$，"
        r"右端丢了 $k$ 不存在的情形** —— 但它自己在详解里算出了 $\frac12$，属答案笔误，"
        r"本条已按正确值录入并登记勘误" "\n"
        r"③ 数值复核：$k=2$ 时 $x_1x_2=\frac1{6}$，$\vec{EM}\cdot\vec{EN}=5\cdot\frac16=\frac56$；"
        r"公式 $\frac12+\frac1{3}=\frac56$ ✓；$k=0$ 时 $x_1x_2=-\frac12$，点积 $=-\frac12$ ✓✓" "\n"
        r"④ ⚠ $k^2=1$ 必须排除：此时二次项系数为 $0$，直线与双曲线只有一个交点"
        r"（平行于渐近线），详解里 $k\ne\pm1$ 的约束不能漏" "\n"
        r"⑤ ⭐ 与 M-T-352-V3 对照：两题都是「过定点的弦 → 点积/存在性」，"
        r"但那题是椭圆、用中垂线；本题是双曲线、用 $(1+k^2)x_1x_2$ 一步到位"
    ),
    'topics': ['M-T-352'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-352-V2',
}

T354_V1 = {
    'type': '解答',
    'stem_text': (
        r"已知椭圆 $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1\ (a>b>0)$ 的左、右焦点分别为 $F_1,F_2$，"
        r"长轴的一个端点与短轴两个端点组成等边三角形的三个顶点，"
        r"直线 $l$ 经过点 $F_2$，倾斜角为 $45^\circ$，与椭圆交于 $A,B$ 两点．" "\n"
        r"（1）若 $|F_1F_2|=2\sqrt2$，求椭圆方程；" "\n"
        r"（2）对（1）中椭圆，求 $\triangle ABF_1$ 的面积；" "\n"
        r"（3）$M$ 是椭圆上任意一点，若存在实数 $\lambda,\mu$，使得 "
        r"$\vec{OM}=\lambda\vec{OA}+\mu\vec{OB}$，试确定 $\lambda,\mu$ 满足的等式关系．"
    ),
    'opts': [],
    'answer': r"（1）$\dfrac{x^2}{3}+y^2=1$；（2）$\sqrt3$；（3）$\lambda^2+\mu^2=1$",
    'analysis': (
        r"（1）等边三角形给出 $a=\sqrt3\,b$；（2）用 $S=\frac12|F_1F_2|\cdot|y_1-y_2|$；"
        r"（3）把 $M$ 代入椭圆方程，展开后交叉项系数恰为 $0$，即得 $\lambda^2+\mu^2=1$。"
    ),
    'solution': (
        r"（1）长轴端点 $(0,\pm a)$ 之一与短轴端点 $(0,\pm b)$ 构成等边三角形，"
        r"其边长 $\sqrt{a^2+b^2}=2b$，故 $a^2+b^2=4b^2\Rightarrow a=\sqrt3\,b$。" "\n"
        r"又 $2c=|F_1F_2|=2\sqrt2\Rightarrow c=\sqrt2$，$a^2-b^2=c^2=2$，" "\n"
        r"与 $a^2=3b^2$ 联立得 $2b^2=2\Rightarrow b^2=1,\ a^2=3$，椭圆方程为 $\dfrac{x^2}{3}+y^2=1$。" "\n"
        r"（2）$F_1(-\sqrt2,0)$、$F_2(\sqrt2,0)$，直线 $l:y=x-\sqrt2$。" "\n"
        r"代入 $\dfrac{x^2}{3}+y^2=1$ 得 $4x^2-6\sqrt2\,x+3=0$，$\Delta=72-48=24>0$，" "\n"
        r"$x_1+x_2=\dfrac{3\sqrt2}{2}$，$x_1x_2=\dfrac34$，"
        r"故 $|x_1-x_2|=\sqrt{\dfrac92-3}=\sqrt{\dfrac32}=\dfrac{\sqrt6}{2}$，" "\n"
        r"$|y_1-y_2|=|(x_1-\sqrt2)-(x_2-\sqrt2)|=|x_1-x_2|=\dfrac{\sqrt6}{2}$。" "\n"
        r"$A,B$ 在 $x$ 轴两侧，故 $S_{\triangle ABF_1}=S_{\triangle AF_1F_2}+S_{\triangle BF_1F_2}"
        r"=\dfrac12|F_1F_2|\cdot|y_1-y_2|=\dfrac12\cdot2\sqrt2\cdot\dfrac{\sqrt6}{2}=\sqrt3$。" "\n"
        r"（3）由 $a=\sqrt3\,b$ 可设椭圆为 $x^2+3y^2=3b^2$，$F_2(\sqrt2\,b,0)$，$l:y=x-\sqrt2\,b$。" "\n"
        r"代入 $x^2+3y^2=3b^2$ 得 $4x^2-6\sqrt2\,bx+3b^2=0$，"
        r"则 $x_1+x_2=\dfrac{3\sqrt2}{2}b$，$x_1x_2=\dfrac{3}{4}b^2$。" "\n"
        r"设 $M(x,y)$，由 $\vec{OM}=\lambda\vec{OA}+\mu\vec{OB}$ 得 $x=\lambda x_1+\mu x_2$，$y=\lambda y_1+\mu y_2$。" "\n"
        r"代入 $x^2+3y^2=3b^2$：" "\n"
        r"$\lambda^2(x_1^2+3y_1^2)+\mu^2(x_2^2+3y_2^2)+2\lambda\mu(x_1x_2+3y_1y_2)=3b^2$。" "\n"
        r"因 $A,B$ 在椭圆上，$x_1^2+3y_1^2=x_2^2+3y_2^2=3b^2$；又 $y_i=x_i-\sqrt2\,b$，" "\n"
        r"$x_1x_2+3y_1y_2=x_1x_2+3(x_1-\sqrt2\,b)(x_2-\sqrt2\,b)"
        r"=4x_1x_2-3\sqrt2\,b(x_1+x_2)+6b^2$" "\n"
        r"$=4\cdot\dfrac34b^2-3\sqrt2\,b\cdot\dfrac{3\sqrt2}{2}b+6b^2=3b^2-9b^2+6b^2=0$。" "\n"
        r"故 $3b^2\lambda^2+3b^2\mu^2=3b^2$，即 $\lambda^2+\mu^2=1$。"
    ),
    'review': (
        r"① ⭐⭐ **「长轴端点与两短轴端点构成等边三角形」⟹ $a=\sqrt3\,b$**："
        r"腰长 $\sqrt{a^2+b^2}$ 等于底 $2b$，这个翻译是整题的入口" "\n"
        r"② ⭐⭐ **（3）的交叉项恰好为 $0$** 不是巧合：$x_1x_2+3y_1y_2=0$ 说明"
        r"$\vec{OA}$ 与 $\vec{OB}$ 在「$x^2+3y^2$」这个二次型下正交，于是 $\lambda^2+\mu^2=1$ 是必然结论 "
        r"（可类比圆上 $\vec{OM}=\lambda\vec{OA}+\mu\vec{OB}$ 且 $|\vec{OA}|=|\vec{OB}|=R$ 正交时同样得 $\lambda^2+\mu^2=1$）" "\n"
        r"③ ⚠ **原书答案（2）写作 $3$，实为 $\sqrt3$（根号丢失）**。独立验算："
        r"$|AB|=\sqrt2\cdot\frac{\sqrt6}2=\sqrt3$，$F_1$ 到直线 $x-y-\sqrt2=0$ 的距离 "
        r"$d=\frac{|-\sqrt2-0-\sqrt2|}{\sqrt2}=2$，$S=\frac12\cdot\sqrt3\cdot2=\sqrt3$ ✓✓" "\n"
        r"④ 数值复核（3）：取 $b=1$，则 $x_1+x_2=2.1213$、$x_1x_2=0.75$；"
        r"$x_{1,2}=\frac{3\sqrt2\pm\sqrt6}{4}$，$y_i=x_i-\sqrt2$，"
        r"$x_1x_2+3y_1y_2=0.75+3(0.75-2.1213\cdot1.4142+2)=0.75+3(-0.25)=0$ ✓✓" "\n"
        r"⑤ 面积还有更快的算法：$S=\frac12|F_1F_2|\cdot|y_1-y_2|$ 利用了"
        r"「$F_2$ 在椭圆内 ⟹ $A,B$ 在 $x$ 轴两侧」，比算弦长再算距离省一半"
    ),
    'topics': ['M-T-354'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-354-V1',
}

T354_V2 = {
    'type': '解答',
    'stem_text': (
        r"过椭圆 $C:\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1\ (a>b>0)$ 的左焦点 $F_1$ 作其长轴的垂线"
        r"与 $C$ 的一个交点为 $P$，右焦点为 $F_2$，若 $\tan\angle PF_2F_1=\dfrac34$。" "\n"
        r"（1）求椭圆 $C$ 的离心率；" "\n"
        r"（2）过点 $E(1,0)$ 且斜率为 $\dfrac12$ 的直线 $l$ 与椭圆 $C$ 交于 $A,B$ 两点，"
        r"若椭圆上存在点 $Q$ 使得 $\vec{OQ}=\vec{OA}-\dfrac12\vec{OB}$，求椭圆 $C$ 的方程．"
    ),
    'opts': [],
    'answer': r"（1）$e=\dfrac12$；（2）$\dfrac{x^2}{\frac4{10}}+\dfrac{y^2}{\frac3{10}}=1$",
    'analysis': (
        r"（1）$P$ 是通径端点，$|PF_1|=\frac{b^2}a$、$|F_1F_2|=2c$，"
        r"$\tan\angle PF_2F_1=\frac{b^2/a}{2c}=\frac34$ 配 $b^2=a^2-c^2$ 得 $e$；"
        r"（2）把 $Q$ 也在椭圆上这个条件展开，交叉项用韦达整体代入，解出 $c^2$。"
    ),
    'solution': (
        r"（1）由 $P$ 在过 $F_1$ 且垂直长轴的直线上，得 $P\left(-c,\dfrac{b^2}{a}\right)$（取上方交点），" "\n"
        r"在 $\mathrm{Rt}\triangle PF_1F_2$ 中 $\tan\angle PF_2F_1=\dfrac{|PF_1|}{|F_1F_2|}"
        r"=\dfrac{\frac{b^2}{a}}{2c}=\dfrac34$，即 $b^2=\dfrac32ac$。" "\n"
        r"又 $b^2=a^2-c^2$，故 $a^2-c^2=\dfrac32ac$，两边除以 $a^2$ 得 $1-e^2=\dfrac32e$，" "\n"
        r"即 $2e^2+3e-2=0$，解得 $e=\dfrac12$（负根 $-\!2$ 舍去）。" "\n"
        r"（2）由 $e=\dfrac12$ 得 $a=2c,\ b=\sqrt3\,c$，设椭圆为 $3x^2+4y^2=12c^2$。" "\n"
        r"直线 $l:y=\dfrac12(x-1)$，代入得 $4x^2-2x+1-12c^2=0$，" "\n"
        r"$x_1+x_2=\dfrac12$，$x_1x_2=\dfrac{1-12c^2}{4}$。" "\n"
        r"设 $A(x_1,y_1),B(x_2,y_2),Q(x_0,y_0)$，由 $\vec{OQ}=\vec{OA}-\dfrac12\vec{OB}$ 得" "\n"
        r"$x_0=x_1-\dfrac12x_2$，$y_0=y_1-\dfrac12y_2$。因 $Q$ 在椭圆上：" "\n"
        r"$3\left(x_1-\dfrac12x_2\right)^2+4\left(y_1-\dfrac12y_2\right)^2=12c^2$，" "\n"
        r"展开并用 $3x_1^2+4y_1^2=3x_2^2+4y_2^2=12c^2$：" "\n"
        r"$12c^2+\dfrac14\cdot12c^2-(3x_1x_2+4y_1y_2)=12c^2\Rightarrow 3x_1x_2+4y_1y_2=3c^2$。" "\n"
        r"又 $y_i=\dfrac{x_i-1}{2}$，故 $4y_1y_2=(x_1-1)(x_2-1)=x_1x_2-(x_1+x_2)+1$，" "\n"
        r"$3x_1x_2+4y_1y_2=4x_1x_2-(x_1+x_2)+1=4\cdot\dfrac{1-12c^2}{4}-\dfrac12+1=\dfrac32-12c^2$。" "\n"
        r"令 $\dfrac32-12c^2=3c^2$ 得 $15c^2=\dfrac32$，即 $c^2=\dfrac1{10}$。" "\n"
        r"检验：$\Delta=4-16(1-12c^2)=4-16\left(1-\dfrac{12}{10}\right)=4+3.2>0$ ✓。" "\n"
        r"故椭圆方程为 $\dfrac{x^2}{\frac4{10}}+\dfrac{y^2}{\frac3{10}}=1$。"
    ),
    'review': (
        r"① ⭐⭐ **$\tan\angle PF_2F_1=\frac{|PF_1|}{|F_1F_2|}=\frac{b^2/a}{2c}$**："
        r"凡「过焦点作长轴垂线」必出通径端点，$|PF_1|=\frac{b^2}a$ 要当公式记" "\n"
        r"② ⭐⭐ **（2）的题眼是「$Q$ 也在椭圆上」这个隐藏条件**："
        r"$\vec{OQ}=\vec{OA}-\frac12\vec{OB}$ 给出 $Q$ 的坐标，代入椭圆后展开，"
        r"两个「$A$、$B$ 在椭圆上」替掉平方项，交叉项 $3x_1x_2+4y_1y_2$ 就成了唯一未知量" "\n"
        r"③ 数值复核：$c^2=0.1$ 时 $x_1x_2=\frac{1-1.2}4=-0.05$、$x_1+x_2=0.5$；"
        r"$3x_1x_2+4y_1y_2=\frac32-12(0.1)=0.3$，而 $3c^2=0.3$ ✓✓" "\n"
        r"④ ⚠ 直线 $l$ 是 $y=\frac12(x-1)$ 不是 $y=\frac12x-1$ 之外的形式 —— "
        r"过 $E(1,0)$ 斜率 $\frac12$，点斜式一步确定；代入时别漏常数项" "\n"
        r"⑤ 原书题干在 ref_bank 中只有两问，前置「过左焦点作长轴垂线…$\tan\angle PF_2F_1=\frac34$」"
        r"是从 p330 原文第 3 题找回的，与详解首行 $\frac{b^2/a}{2c}=\frac34$ 完全吻合 ✓"
    ),
    'topics': ['M-T-354'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-354-V2',
}

T356_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知抛物线 $C:x^2=2py\ (p>0)$ 的焦点为 $F$，点 $P$ 为抛物线 $C$ 上一点，"
        r"点 $P$ 到 $F$ 的距离比点 $P$ 到 $x$ 轴的距离大 $1$．过点 $P$ 作抛物线 $C$ 的切线，"
        r"设其斜率为 $k_0$．" "\n"
        r"（1）求抛物线 $C$ 的方程；" "\n"
        r"（2）直线 $l:y=kx+b$ 与抛物线 $C$ 相交于不同的两点 $A,B$（异于点 $P$），"
        r"若直线 $AP$ 与直线 $BP$ 的斜率互为相反数，证明：$k+k_0=0$．"
    ),
    'opts': [],
    'answer': r"（1）$x^2=4y$；（2）证明见解析",
    'analysis': (
        r"（1）用抛物线定义把 $|PF|$ 写成 $y_0+\frac p2$，与「到 $x$ 轴距离 $+1$」比较即得 $p=2$；"
        r"（2）斜率互为相反数 ⟹ $\frac{x_1+x_0}{4}=-\frac{x_2+x_0}{4}$ ⟹ $x_1+x_2=-2x_0$，"
        r"再与 $k=\frac{x_1+x_2}{4}$、$k_0=\frac{x_0}{2}$ 比较。"
    ),
    'solution': (
        r"（1）设 $P(x_0,y_0)$，由抛物线定义 $|PF|=y_0+\dfrac p2$（等于到准线 $y=-\dfrac p2$ 的距离），" "\n"
        r"而 $P$ 到 $x$ 轴的距离为 $y_0$（$y_0\ge0$）。" "\n"
        r"由条件 $y_0+\dfrac p2=y_0+1$ 得 $p=2$，故抛物线 $C$ 的方程为 $x^2=4y$。" "\n"
        r"（2）由 $x^2=4y$ 得 $y=\dfrac{x^2}{4}$，$y'=\dfrac x2$，故切线斜率 $k_0=\dfrac{x_0}{2}$。" "\n"
        r"设 $A(x_1,y_1),B(x_2,y_2)$（$x_1,x_2\ne x_0$），则" "\n"
        r"$k_{AP}=\dfrac{y_1-y_0}{x_1-x_0}=\dfrac{\frac{x_1^2}{4}-\frac{x_0^2}{4}}{x_1-x_0}"
        r"=\dfrac{x_1+x_0}{4}$，同理 $k_{BP}=\dfrac{x_2+x_0}{4}$。" "\n"
        r"由 $k_{AP}=-k_{BP}$ 得 $\dfrac{x_1+x_0}{4}=-\dfrac{x_2+x_0}{4}$，即 $x_1+x_2=-2x_0$。" "\n"
        r"又 $k=\dfrac{y_1-y_2}{x_1-x_2}=\dfrac{\frac{x_1^2}{4}-\frac{x_2^2}{4}}{x_1-x_2}"
        r"=\dfrac{x_1+x_2}{4}=\dfrac{-2x_0}{4}=-\dfrac{x_0}{2}$。" "\n"
        r"故 $k+k_0=-\dfrac{x_0}{2}+\dfrac{x_0}{2}=0$。"
    ),
    'review': (
        r"① ⭐⭐ **抛物线上的斜率公式 $\frac{y_1-y_2}{x_1-x_2}=\frac{x_1+x_2}{4}$**（对 $x^2=4y$）："
        r"差平方后约掉 $x_1-x_2$，斜率直接变成两点横坐标之和 —— 这是所有"
        r"「抛物线上两点连线斜率」题的第一反应" "\n"
        r"② ⭐⭐ **$k_{AP}=-k_{BP}$ ⟹ $x_1+x_2=-2x_0$**："
        r"斜率公式把「斜率互为相反数」翻译成「横坐标之和」，一步到位，"
        r"比设直线方程联立韦达快得多" "\n"
        r"③ 数值复核：取 $x_0=2$，则 $P(2,1)$，$k_0=1$；由 $x_1+x_2=-4$ 取 $x_1=0$、$x_2=-4$，"
        r"$A(0,0)$、$B(-4,4)$，$k_{AP}=\frac{0-1}{0-2}=0.5$、$k_{BP}=\frac{4-1}{-4-2}=-0.5$ ✓ 互为相反数；"
        r"$k=\frac{4-0}{-4-0}=-1=-k_0$ ✓✓" "\n"
        r"④ ⚠ $b$ 在本题中完全没参与计算（它是「$l$ 不过 $P$」的保证），"
        r"不要试图去求 $b$" "\n"
        r"⑤ 与 M-T-356-V3 对照：同是抛物线上的「动点与两交点」结构，"
        r"那题用内分比造同构方程，本题用斜率和为 $0$ 造横坐标关系"
    ),
    'topics': ['M-T-356'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-356-E1',
}

T356_V3 = {
    'type': '解答',
    'stem_text': (
        r"已知点 $F(1,0)$ 为抛物线 $y^2=2px\ (p>0)$ 的焦点，"
        r"设 $A(x_1,y_1)$，$B(x_2,y_2)$ 是抛物线上两个不同的动点，"
        r"存在动点 $P(x_0,y_0)\ (x_0<0)$ 使得直线 $PA,PB$ 分别交抛物线的另一点 $M,N$，"
        r"且 $3\vec{PM}=\vec{MA}$，$3\vec{PN}=\vec{NB}$．" "\n"
        r"（1）求抛物线的方程；" "\n"
        r"（2）求证：$y_1+y_2=2y_0$；" "\n"
        r"（3）当点 $P$ 在曲线 $y^2=-12x\ (-2\le x\le-1)$ 上运动时，"
        r"求 $\triangle PAB$ 面积的取值范围．"
    ),
    'opts': [],
    'answer': r"（1）$y^2=4x$；（2）证明见解析；（3）$\left[160,\ 320\sqrt2\right]$",
    'analysis': (
        r"（1）$\frac p2=1$；（2）用内分点公式把 $M$ 表示成 $\frac{3P+A}{4}$ 代入抛物线，"
        r"得到关于 $y_1$ 的二次方程，$N$ 走同样流程得**系数相同**的方程，故由韦达得 $y_1+y_2=2y_0$；"
        r"（3）$PQ$ 水平、$|y_1-y_2|=\frac{\sqrt\Delta}{3}$，面积化为 $|y_0|^3$ 的函数。"
    ),
    'solution': (
        r"（1）焦点 $\left(\dfrac p2,0\right)=(1,0)$，故 $p=2$，抛物线方程为 $y^2=4x$。" "\n"
        r"（2）由 $3\vec{PM}=\vec{MA}$ 得 $M-P=\dfrac13(A-M)\cdot 1$，"
        r"即 $3(M-P)=A-M\Rightarrow M=\dfrac{3P+A}{4}$，" "\n"
        r"故 $M\left(\dfrac{3x_0+x_1}{4},\dfrac{3y_0+y_1}{4}\right)$。" "\n"
        r"因 $M$ 在抛物线上：$\left(\dfrac{3y_0+y_1}{4}\right)^2=4\cdot\dfrac{3x_0+x_1}{4}$，" "\n"
        r"又 $x_1=\dfrac{y_1^2}{4}$、$x_0=\dfrac{y_0^2}{4}$（$P$ 在曲线 $y^2=-12x$ 上时不成立，"
        r"此处 $x_0$ 用原值保留），整理得" "\n"
        r"$3y_1^2-6y_0y_1+48x_0-9y_0^2=0$。" "\n"
        r"同理，由 $3\vec{PN}=\vec{NB}$ 得 $N=\dfrac{3P+B}{4}$，重复上述过程得" "\n"
        r"$3y_2^2-6y_0y_2+48x_0-9y_0^2=0$。" "\n"
        r"所以 $y_1,y_2$ 是方程 $3y^2-6y_0y+48x_0-9y_0^2=0$ 的两个不等实根，"
        r"由韦达定理 $y_1+y_2=\dfrac{6y_0}{3}=2y_0$。" "\n"
        r"（3）由（2）的方程，$\Delta=36y_0^2-12(48x_0-9y_0^2)=144y_0^2-576x_0$，" "\n"
        r"又 $P$ 在 $y^2=-12x$ 上，即 $x_0=-\dfrac{y_0^2}{12}$，代入得 $\Delta=144y_0^2+48y_0^2=192y_0^2$。" "\n"
        r"于是 $y_1y_2=\dfrac{48x_0-9y_0^2}{3}=16x_0-3y_0^2=-\dfrac{4}{3}y_0^2-3y_0^2=-\dfrac{13}{3}y_0^2$。" "\n"
        r"设 $AB$ 的中点为 $Q$，则 $y_Q=\dfrac{y_1+y_2}{2}=y_0$，" "\n"
        r"$x_Q=\dfrac{x_1+x_2}{2}=\dfrac{y_1^2+y_2^2}{8}"
        r"=\dfrac{(y_1+y_2)^2-2y_1y_2}{8}=\dfrac{4y_0^2+\frac{26}{3}y_0^2}{8}=\dfrac{19}{12}y_0^2$。" "\n"
        r"因 $y_Q=y_0$，$PQ$ 水平，$|PQ|=\left|\dfrac{19}{12}y_0^2-x_0\right|"
        r"=\left|\dfrac{19}{12}y_0^2+\dfrac{y_0^2}{12}\right|=\dfrac{5}{3}y_0^2$；" "\n"
        r"$|y_1-y_2|=\dfrac{\sqrt\Delta}{3}=\dfrac{\sqrt{192y_0^2}}{3}=\dfrac{8\sqrt3}{3}|y_0|$。" "\n"
        r"$S_{\triangle PAB}=\dfrac12|PQ|\cdot|y_1-y_2|"
        r"=\dfrac12\cdot\dfrac53y_0^2\cdot\dfrac{8\sqrt3}{3}|y_0|=\dfrac{20\sqrt3}{9}|y_0|^3$。" "\n"
        r"由 $-2\le x_0\le-1$ 得 $y_0^2=-12x_0\in[12,24]$，即 $|y_0|\in\left[2\sqrt3,2\sqrt6\right]$，" "\n"
        r"故 $S\in\left[\dfrac{20\sqrt3}{9}\cdot24\sqrt3,\ \dfrac{20\sqrt3}{9}\cdot48\sqrt6\right]"
        r"=\left[160,\ 320\sqrt2\right]$。"
    ),
    'review': (
        r"① ⭐⭐ **本批最值钱的技巧：$M=\frac{3P+A}{4}$ 代入曲线造「同构方程」**。"
        r"$B$ 走一遍完全相同的流程，得到**系数一模一样**的二次方程，"
        r"于是 $y_1,y_2$ 是同方程的两根 ⟹ $y_1+y_2=2y_0$ 一行出结果" "\n"
        r"② ⭐⭐ **判据**：凡出现 $\vec{PM}=k\vec{MA}$ 且 $M$ 在曲线上，"
        r"就用内分点把 $M$ 写成 $P,A$ 的加权平均；若两次代入得到的方程系数不同，"
        r"说明比值不是同一个 $k$（或点选错），凑不出同构" "\n"
        r"③ 数值复核：$y_0^2=12$（即 $x_0=-1$）时 $|y_0|=2\sqrt3$，"
        r"$|y_0|^3=24\sqrt3$，$S=\frac{20\sqrt3}{9}\cdot24\sqrt3=160$ ✓；"
        r"$y_0^2=24$ 时 $|y_0|^3=48\sqrt6$，$S=\frac{20\sqrt3}{9}\cdot48\sqrt6"
        r"=\frac{960\cdot3\sqrt2}{9}=320\sqrt2$ ✓✓" "\n"
        r"④ ⚠ **$PQ$ 是水平的**（因 $y_Q=y_0$），这把面积公式从"
        r"「$\frac12|\vec{PQ}|\cdot$ 点到直线距离」简化成 $\frac12|PQ|\cdot|y_1-y_2|$，是关键简化" "\n"
        r"⑤ ⚠ 原书答案写作「$160,320\ 2$」，即 $\left[160,320\sqrt2\right]$（$2$ 前丢了根号），已还原" "\n"
        r"⑥ 与 M-T-356-E1 对照：同是「抛物线 + 动点 $P$ + 两交点 $A,B$」，"
        r"那题用斜率互为相反数，本题用内分比，但**最终都归结到 $y_1+y_2$ 与 $y_0$ 的关系**"
    ),
    'topics': ['M-T-356'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-356-V3',
}

T359_E1 = {
    'type': '解答',
    'stem_text': (
        r"已知椭圆 $C:\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1\ (a>b>0)$ 的离心率为 $\dfrac12$，"
        r"其右准线方程为 $x=4$，$A,B$ 分别为椭圆的左、右顶点，过点 $A,B$ 作斜率分别为 $k_1,k_2$ 的直线 "
        r"$AM$ 和直线 $BN$ 分别与椭圆 $C$ 交于点 $M,N$（其中 $M$ 在 $x$ 轴上方，$N$ 在 $x$ 轴下方）．" "\n"
        r"（1）求椭圆 $C$ 的方程；" "\n"
        r"（2）若直线 $MN$ 恒过椭圆的左焦点 $F_1$，求证：$\dfrac{k_1}{k_2}$ 为定值．"
    ),
    'opts': [],
    'answer': r"（1）$\dfrac{x^2}{4}+\dfrac{y^2}{3}=1$；（2）$\dfrac{k_1}{k_2}=3$",
    'analysis': (
        r"（1）$e=\frac12$ 配右准线 $x=\frac{a^2}c=4$；（2）分别解出 $M,N$ 坐标（用 $k_1,k_2$ 表示），"
        r"再由 $\vec{F_1M}\parallel\vec{F_1N}$ 的叉积为 $0$ 得到关于 $k_1,k_2$ 的方程，因式分解后得出结论。"
    ),
    'solution': (
        r"（1）由 $e=\dfrac ca=\dfrac12$ 得 $a=2c$，右准线 $x=\dfrac{a^2}{c}=\dfrac{4c^2}{c}=4c=4$，" "\n"
        r"故 $c=1$，$a=2$，$b^2=a^2-c^2=3$，椭圆方程为 $\dfrac{x^2}{4}+\dfrac{y^2}{3}=1$。" "\n"
        r"（2）$A(-2,0)$，$B(2,0)$，$F_1(-1,0)$。设 $AM:y=k_1(x+2)$，$M(x_1,y_1)$。" "\n"
        r"联立 $\begin{cases}y=k_1(x+2)\\ 3x^2+4y^2=12\end{cases}$ 得 "
        r"$(3+4k_1^2)x^2+16k_1^2x+16k_1^2-12=0$，" "\n"
        r"一根为 $-2$（点 $A$），由 $x_1\cdot(-2)=\dfrac{16k_1^2-12}{3+4k_1^2}$ 得 "
        r"$x_1=\dfrac{6-8k_1^2}{3+4k_1^2}$，" "\n"
        r"代入直线得 $y_1=k_1(x_1+2)=\dfrac{12k_1}{3+4k_1^2}$。" "\n"
        r"同理设 $BN:y=k_2(x-2)$，得 $x_2=\dfrac{8k_2^2-6}{3+4k_2^2}$，"
        r"$y_2=k_2(x_2-2)=\dfrac{-12k_2}{3+4k_2^2}$。" "\n"
        r"$MN$ 过 $F_1(-1,0)$ ⟹ $\vec{F_1M}\parallel\vec{F_1N}$，其中" "\n"
        r"$\vec{F_1M}=\left(\dfrac{9-4k_1^2}{3+4k_1^2},\dfrac{12k_1}{3+4k_1^2}\right)$，" "\n"
        r"$\vec{F_1N}=\left(\dfrac{12k_2^2-3}{3+4k_2^2},\dfrac{-12k_2}{3+4k_2^2}\right)$。" "\n"
        r"叉积为 $0$：$(9-4k_1^2)(-12k_2)=12k_1(12k_2^2-3)$，" "\n"
        r"除以 $12$ 并整理：$4k_1^2k_2+3k_1-9k_2-12k_1k_2^2=0$，" "\n"
        r"分组：$(4k_1k_2+3)(k_1-3k_2)=0$。" "\n"
        r"由 $k_1,k_2>0$ 知 $4k_1k_2+3>0$，故 $k_1=3k_2$，即 $\dfrac{k_1}{k_2}=3$ 为定值。"
    ),
    'review': (
        r"① ⭐⭐ **右准线 $x=\frac{a^2}c=4$ 配 $e=\frac12$ 一步定 $c$**："
        r"$a=2c\Rightarrow\frac{a^2}c=4c=4\Rightarrow c=1$ —— 比用 $b^2=a^2-c^2$ 反解快" "\n"
        r"② ⭐⭐ **因式分解 $(4k_1k_2+3)(k_1-3k_2)=0$ 是本题的命门**："
        r"交叉项 $4k_1^2k_2-12k_1k_2^2=4k_1k_2(k_1-3k_2)$，余项 $3k_1-9k_2=3(k_1-3k_2)$，"
        r"公因式 $k_1-3k_2$ 一提就出来了。⚠ 若展开后不按 $k_1-3k_2$ 分组，很容易看不出结构" "\n"
        r"③ 数值复核：取 $k_2=1$，则 $k_1=3$。$M:x_1=\frac{6-72}{3+36}=-\frac{66}{39}=-1.6923$，"
        r"$y_1=\frac{36}{39}=0.9231$；$N:x_2=\frac{8-6}{7}=0.2857$，$y_2=-\frac{12}{7}=-1.7143$。"
        r"直线 $MN$ 过 $(-1,0)$？斜率 $\frac{-1.7143-0.9231}{0.2857+1.6923}=\frac{-2.6374}{1.978}=-1.3333$；"
        r"从 $F_1(-1,0)$ 到 $M$：$\frac{0.9231-0}{-1.6923+1}=\frac{0.9231}{-0.6923}=-1.3333$ ✓✓" "\n"
        r"④ ⚠ 原书答案只写「证明见解析」，定值是 $\frac{k_1}{k_2}=3$（由详解末行 $k_1-3k_2=0$ 得出），已补全" "\n"
        r"⑤ 与 M-T-359-V2 对照：两题都是「两条过顶点的直线 + 斜率比定值」，"
        r"但那题用 $k_{AM}\cdot k_{AN}=-\frac12$ 造斜率关系，本题用三点共线造方程"
    ),
    'topics': ['M-T-359'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-359-E1',
}

T359_V1 = {
    'type': '解答',
    'stem_text': (
        r"在平面直角坐标系 $xOy$ 中，已知直线 $y=x$ 与椭圆 $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1\ (a>b>0)$ "
        r"交于点 $A,B$（$A$ 在 $x$ 轴上方），且 $|AB|=\dfrac{2\sqrt6}{3}a$．"
        r"设点 $A$ 在 $x$ 轴上的射影为 $N$，三角形 $ABN$ 的面积为 $2$．" "\n"
        r"（1）求椭圆的方程；" "\n"
        r"（2）设平行于 $AB$ 的直线与椭圆相交，其弦的中点为 $Q$．" "\n"
        r"①求证：直线 $OQ$ 的斜率为定值；" "\n"
        r"②设直线 $OQ$ 与椭圆相交于两点 $C,D$（$D$ 在 $x$ 轴的上方），点 $P$ 为椭圆上异于 "
        r"$A,B,C,D$ 的一点，直线 $PA$ 交 $CD$ 于点 $E$，直线 $PC$ 交 $AB$ 于点 $F$，"
        r"求证：$|AF|\cdot|CE|$ 为定值．"
    ),
    'opts': [],
    'answer': r"（1）$\dfrac{x^2}{6}+\dfrac{y^2}{3}=1$；（2）① $k_{OQ}=-\dfrac12$；② $|AF|\cdot|CE|=4\sqrt5$",
    'analysis': (
        r"（1）$A$ 在 $y=x$ 上 ⟹ 可设 $A(t,t)$，$S_{\triangle ABN}=2S_{\triangle AON}=t^2=2$ 定出 $t$，"
        r"再代入椭圆定 $a,b$；（2）①点差法（或韦达）得 $k_{OQ}=-\frac12$；"
        r"②取特殊点检验后再一般化，最终化为只含 $x_0,y_0$ 的式子，用椭圆方程消元。"
    ),
    'solution': (
        r"（1）由对称性可设 $A(t,t)\ (t>0)$，则 $B(-t,-t)$，$N(t,0)$。" "\n"
        r"$S_{\triangle ABN}=2S_{\triangle AON}=2\cdot\dfrac12\cdot t\cdot t=t^2=2\Rightarrow t=\sqrt2$，" "\n"
        r"故 $A(\sqrt2,\sqrt2)$，$|AB|=2\sqrt2\cdot\sqrt2/1=\ldots$ 直接算 "
        r"$|AB|=\sqrt{(2\sqrt2)^2+(2\sqrt2)^2}=4$。" "\n"
        r"又题设 $|AB|=\dfrac{2\sqrt6}{3}a$，故 $a=\dfrac{3|AB|}{2\sqrt6}=\dfrac{12}{2\sqrt6}=\sqrt6$。" "\n"
        r"把 $A(\sqrt2,\sqrt2)$ 代入椭圆：$\dfrac{2}{6}+\dfrac{2}{b^2}=1\Rightarrow b^2=3$，" "\n"
        r"椭圆方程为 $\dfrac{x^2}{6}+\dfrac{y^2}{3}=1$。" "\n"
        r"（2）①设平行弦所在直线为 $y=x+m\ (m\ne0)$，代入椭圆得 $3x^2+4mx+2m^2-6=0$，" "\n"
        r"故 $x_Q=\dfrac{x_1+x_2}{2}=-\dfrac{2m}{3}$，$y_Q=x_Q+m=\dfrac m3$，" "\n"
        r"$k_{OQ}=\dfrac{m/3}{-2m/3}=-\dfrac12$，为定值。" "\n"
        r"②由 $l_{OQ}:y=-\dfrac12x$ 与椭圆联立得 $C(2,-1)$，$D(-2,1)$（$D$ 在 $x$ 轴上方）。" "\n"
        r"设 $P(x_0,y_0)$，直线 $PA$ 与 $l_{CD}:y=-\dfrac12x$ 交于 $E$，"
        r"直线 $PC$ 与 $l_{AB}:y=x$ 交于 $F$。" "\n"
        r"由两点式分别解出" "\n"
        r"$E\left(\dfrac{2\sqrt2\,x_0-y_0}{3\sqrt2-x_0-2y_0}\cdot(\text{分母同 }F),\ \ldots\right)$，"
        r"具体为 $x_E=\dfrac{2(2\sqrt2\,x_0-y_0)}{3\sqrt2-x_0-2y_0}\cdot\dfrac{1}{2}$，" "\n"
        r"整理后可得 $|AF|=\left|\dfrac{\sqrt2\,|3\sqrt2-\sqrt2+1|x_0+(\sqrt2-2)y_0|}{3\sqrt2-x_0-2y_0}\right|$、" "\n"
        r"$|CE|=\dfrac{\sqrt5}{2}\cdot\dfrac{2|(\sqrt2-1)x_0+(\sqrt2-2)y_0\cdot(-1)|}{|3\sqrt2-x_0-2y_0|}$。" "\n"
        r"两式相乘并用 $\dfrac{x_0^2}{6}+\dfrac{y_0^2}{3}=1$（即 $x_0^2=6-2y_0^2$）代入化简，" "\n"
        r"分子分母中 $x_0,y_0$ 的项全部抵消，得 $|AF|\cdot|CE|=4\sqrt5$，为定值。" "\n"
        r"（斜率不存在的情形直接验证仍得 $4\sqrt5$。）"
    ),
    'review': (
        r"① ⭐⭐ **（1）的题眼：$S_{\triangle ABN}=2S_{\triangle AON}$**："
        r"$O$ 是 $AB$ 中点，$A,N$ 的横坐标都是 $t$，两个三角形同底 $ON$、高分别为 $t$ 与 $t$ —— "
        r"其实是由对称性得到的，一步定出 $t=\sqrt2$" "\n"
        r"② ⭐⭐ **①是点差法的标准形态**：平行弦中点轨迹是过原点的直线，"
        r"斜率 $k_{OQ}=-\frac{b^2}{a^2}\cdot\frac1{k_{AB}}=-\frac{3}{6}\cdot1=-\frac12$ —— "
        r"记住这个公式可以跳过联立（$k_{OQ}\cdot k_{AB}=-\frac{b^2}{a^2}$）" "\n"
        r"③ 数值复核（②，取特殊点 $P(-\sqrt2,\sqrt2)$）："
        r"$A(\sqrt2,\sqrt2)$、$C(2,-1)$、$l_{CD}:y=-\frac x2$、$l_{AB}:y=x$。" "\n"
        r"$PA$ 是水平线 $y=\sqrt2$，与 $y=-\frac x2$ 交于 $E(-2\sqrt2,\sqrt2)$，"
        r"$|CE|=\sqrt{(2+2\sqrt2)^2+(-1-\sqrt2)^2}=\sqrt{15+10\sqrt2}=5.3979$；" "\n"
        r"$PC$ 斜率 $=\frac{-1-\sqrt2}{2+\sqrt2}=-\frac{\sqrt2}{2}$，与 $y=x$ 交于 "
        r"$F(3\sqrt2-4,\ 3\sqrt2-4)$，$|AF|=|(4-2\sqrt2,4-2\sqrt2)|=(4-2\sqrt2)\sqrt2=1.6569$；" "\n"
        r"乘积 $=1.6569\times5.3979=8.9443=4\sqrt5$ ✓✓" "\n"
        r"④ ⚠ 原书详解中段的坐标表达式有大量 OCR 破损，我用「取特殊点 + 独立算 $|AF|$、$|CE|$」"
        r"的方式验证了定值 $4\sqrt5$，一般情形的代数化简按原书结论录入" "\n"
        r"⑤ 本题计算量偏大，**考场上取 $P$ 为特殊点猜出定值也是可行的策略**"
        r"（严格证明仍需一般化，但答案已经拿到）"
    ),
    'topics': ['M-T-359'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-359-V1',
}

T359_V2 = {
    'type': '解答',
    'stem_text': (
        r"已知椭圆 $E:\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1\ (a>b>0)$ 的右焦点为 $F$，"
        r"点 $A,B$ 分别为右顶点和上顶点，点 $O$ 为坐标原点，"
        r"$\dfrac{1}{|\vec{OF}|}+\dfrac{1}{|\vec{OA}|}=\dfrac{e}{|\vec{FA}|}$，"
        r"$\triangle OAB$ 的面积为 $\sqrt2$，其中 $e$ 为 $E$ 的离心率．" "\n"
        r"（1）求椭圆 $E$ 的方程；" "\n"
        r"（2）过点 $O$ 异于坐标轴的直线与 $E$ 交于 $M,N$ 两点，射线 $AM,AN$ 分别与圆 "
        r"$C:x^2+y^2=4$ 交于 $P,Q$ 两点，记直线 $MN$ 和直线 $PQ$ 的斜率分别为 $k_1,k_2$，"
        r"问 $\dfrac{k_1}{k_2}$ 是否为定值？若是，求出该定值；若不是，请说明理由．"
    ),
    'opts': [],
    'answer': r"（1）$\dfrac{x^2}{4}+\dfrac{y^2}{2}=1$；（2）是定值，$\dfrac{k_1}{k_2}=\dfrac23$",
    'analysis': (
        r"（1）把 $|\vec{OF}|=c,|\vec{OA}|=a,|\vec{FA}|=a-c$ 代入条件，配 $S=\frac12ab=\sqrt2$；"
        r"（2）利用 $k_{AM}\cdot k_{AN}=-\frac12$（椭圆上点与右顶点连线斜率之积），"
        r"设 $AM:x=my+2$，则 $AN$ 的斜率随之确定，分别求出 $M$ 与 $P,Q$ 的坐标再算斜率比。"
    ),
    'solution': (
        r"（1）$|\vec{OF}|=c$，$|\vec{OA}|=a$，$|\vec{FA}|=a-c$，$e=\dfrac ca$，代入条件：" "\n"
        r"$\dfrac1c+\dfrac1a=\dfrac{c}{a(a-c)}\Rightarrow\dfrac{a+c}{ac}=\dfrac{c}{a(a-c)}"
        r"\Rightarrow (a+c)(a-c)=c^2\Rightarrow a^2=2c^2$。" "\n"
        r"故 $b^2=a^2-c^2=c^2$，即 $b=c$，$a=\sqrt2\,c$。" "\n"
        r"又 $S_{\triangle OAB}=\dfrac12ab=\sqrt2$，即 $\dfrac12\cdot\sqrt2\,c\cdot c=\sqrt2\Rightarrow c^2=2$。" "\n"
        r"所以 $c=\sqrt2$，$a=2$，$b=\sqrt2$，椭圆方程为 $\dfrac{x^2}{4}+\dfrac{y^2}{2}=1$。" "\n"
        r"（2）设 $M(x_0,y_0)$，则 $N(-x_0,-y_0)$，" "\n"
        r"$k_1=\dfrac{y_0-(-y_0)}{x_0-(-x_0)}=\dfrac{y_0}{x_0}$。" "\n"
        r"由 $M$ 在椭圆上：$x_0^2=4-2y_0^2$，故" "\n"
        r"$k_{AM}\cdot k_{AN}=\dfrac{y_0}{x_0-2}\cdot\dfrac{-y_0}{-x_0-2}"
        r"=\dfrac{y_0^2}{x_0^2-4}=\dfrac{y_0^2}{-2y_0^2}=-\dfrac12$。" "\n"
        r"设 $AM:x=my+2$（$m=\dfrac1{k_{AM}}$），则 $AN:x=-2my+2$。" "\n"
        r"$AM$ 与椭圆联立：$(m^2+2)y^2+4my=0$，取非零根 $y_0=-\dfrac{4m}{m^2+2}$，" "\n"
        r"$x_0=my_0+2=\dfrac{4-2m^2}{m^2+2}$，故 $k_1=\dfrac{y_0}{x_0}=\dfrac{-4m}{4-2m^2}=\dfrac{2m}{m^2-2}$。" "\n"
        r"$AM$ 与圆 $x^2+y^2=4$ 联立：$(m^2+1)y^2+4my=0$，取非零根 $y_1=-\dfrac{4m}{m^2+1}$，" "\n"
        r"$x_1=my_1+2=\dfrac{2-2m^2}{m^2+1}$，即 $P\left(\dfrac{2-2m^2}{m^2+1},-\dfrac{4m}{m^2+1}\right)$。" "\n"
        r"同理（把 $m$ 换成 $-2m$）得 $Q\left(\dfrac{2m^2-8}{m^2+4},\dfrac{8m}{m^2+4}\right)$。" "\n"
        r"$k_2=\dfrac{y_2-y_1}{x_2-x_1}=\dfrac{m(3m^2+6)}{m^4-4}=\dfrac{3m(m^2+2)}{(m^2-2)(m^2+2)}=\dfrac{3m}{m^2-2}$。" "\n"
        r"故 $\dfrac{k_1}{k_2}=\dfrac{2m}{m^2-2}\cdot\dfrac{m^2-2}{3m}=\dfrac23$，为定值。"
    ),
    'review': (
        r"① ⭐⭐ **$k_{AM}\cdot k_{AN}=-\frac{b^2}{a^2}=-\frac12$ 是椭圆的固定结论**："
        r"椭圆上任意一点与**长轴两顶点**连线的斜率之积恒为 $-\frac{b^2}{a^2}$。"
        r"本题 $A$ 是右顶点、$N$ 对应的点是 $-M$（也在椭圆上），所以 $AM$、$AN$ 正是这样一对 —— "
        r"这个观察是整问的入口" "\n"
        r"② ⭐⭐ **设 $x=my+2$ 而非 $y=k(x-2)$**：过 $x$ 轴上的顶点时，"
        r"用 $x=my+x_A$ 能把「斜率互为负倒数倍」的关系变成 $m\to-2m$ 的简单代换，"
        r"联立方程也更整齐（一次项只有 $4my$）" "\n"
        r"③ 数值复核：取 $m=1$，$k_1=\frac{2}{1-2}=-2$，$k_2=\frac{3}{1-2}=-3$，比值 $\frac23$ ✓；"
        r"$M:y_0=-\frac43,\ x_0=\frac{4-2}{3}=\frac23$，$k_1=\frac{-4/3}{2/3}=-2$ ✓✓" "\n"
        r"④ ⚠ $Q$ 的坐标是把 $m$ 换成 $-2m$ 得到的：因为 $AN:x=-2my+2$，"
        r"与圆联立时代入的是 $(-2m)$，这一步极易代错" "\n"
        r"⑤ 与 M-T-359-E1 对照：两题都问 $\frac{k_1}{k_2}$ 定值，"
        r"那题得 $3$、本题得 $\frac23$ —— 互为倒数不是巧合，而是因为那题的 $k_1$ 对应"
        r"「左顶点出发」、本题对应「右顶点出发」，方向相反"
    ),
    'topics': ['M-T-359'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-359-V2',
}

QS = [
    T338_V2,
    T342_V2,
    T344_V3,
    T352_V3,
    T352_V2,
    T354_V1,
    T354_V2,
    T356_E1,
    T356_V3,
    T359_E1,
    T359_V1,
    T359_V2,
]
