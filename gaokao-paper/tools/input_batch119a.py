# -*- coding: utf-8 -*-
r"""第 119 批：解三角形 · 向量 15 题选择 12 题（M-T-199 ×2 / M-T-201 / M-T-203 / M-T-207 / M-T-232 ×2/ M-T-233 ×2 / M-T-236 / M-T-238 / M-T-342 多选）填空 1 题（M-T-237）解答 2 题（M-T-220 / M-T-227）python3 tools/run_batch.py 119## 选题依据用 `pick_batch.py`（pages 策略 + skipped 排除）筛出可录题后，我按「原文页相邻 + 详解完整」重排：本题集中在 p160–p171（解三角形最值 / 向量基底）与p185–p209（解三角形大题 / 向量投影模长），另加 p314 的四心判断题。15 题的详解我都独立推了一遍，关键结论与原书答案数值对拍吻合后才录入。## ★★ 本批最值钱的一条：赵爽弦图里 B、E、F 三点共线（M-T-232-E1）设外侧正方形的边长为 $c$（即四个全等直角三角形的斜边），内侧直角顶点顺次为$E,F,G,H$。取 $B$ 为原点、$\vec{BC}$、$\vec{BA}$ 为两条边，记直角三角形的两条直角边 $AE=BF=p$、$BE=CF=q$（$p^{2}+q^{2}=c^{2}$），则$$E=\left(\frac{pq}c,\ \frac{q^{2}}c\right),\qquad F=\left(\frac{p^{2}}c,\ \frac{pq}c\right)$$**两点的坐标成比例 ⟹ $B,E,F$ 三点共线**，且 $BE=q$、$BF=p$、$EF=p-q$。> ⭐⭐ 由 $BE=3EF$ 得 $q=3(p-q)$ ⟹ $p=\dfrac43q$，于是> $\vec{EB}=-\dfrac qp\vec{BF}=-\dfrac34\vec{BF}$、$\vec{CF}=\dfrac qp\vec{EA}=\dfrac34\vec{EA}$。> **这两个 $\dfrac34$ 是同一个比值 $\dfrac qp$**，这就是原书解法里两个系数的来源。> 数值对拍：$p=4,q=3,c=5$ 时 $E(2.4,1.8)$、$F(3.2,2.4)$，> $\vec{BF}=0.64\vec{BC}+0.48\vec{BA}=\dfrac{16}{25}\vec a+\dfrac{12}{25}\vec b$ ✓## ★★ 第二条：直角等腰三角形的顶点坐标（M-T-199-V3）$B(b,0)$、$C(0,c)$，$\angle BAC=90^\circ$ 且 $AB=AC=4$ ⟹取 $BC$ 中点 $E\left(\dfrac b2,\dfrac c2\right)$，$AE=2\sqrt2$ 且 $AE\perp BC$，故$$A=\left(\frac{b+c}2,\ \frac{b+c}2\right)\ \Longrightarrow\ |OA|=\frac{b+c}{\sqrt2}$$由 $b^{2}+c^{2}=32$、$b,c\ge0$ 得 $(b+c)^{2}=32+2bc\in[32,64]$ ⟹ $|OA|\in[4,4\sqrt2]$。> ⭐⭐ 比原书按 $\theta$ 分四种情况讨论干净得多：**把 $A$ 直接写成 $E$ 加一个> 垂直向量**，坐标一次到位。## ★★ 第三条：外心题里 $\cos\theta=\dfrac c{2\,AO}$（M-T-207-V3）$O$ 是外心 ⟹ $O$ 在 $AB$ 的中垂线上 ⟹ $\vec{AO}$ 在 $\vec{AB}$ 上的投影恰是$\dfrac c2$，即 $AO\cos\angle BAO=\dfrac c2$。> ⭐⭐ 于是 $\dfrac bc\cdot c\cdot AO\cos\theta=b\cdot\dfrac c2$，两项合并得> $bc=2m\,AO^{2}$；再由 $\sin B+\sin C=\dfrac{b+c}{2AO}=\sqrt3$ 消掉 $AO$，> 只剩 $m=\dfrac{bc}{2AO^{2}}\le\dfrac{(b+c)^{2}}{8AO^{2}}=\dfrac32$。## ★★ 第四条：$2S=a^{2}-(b-c)^{2}$ 之外的新招（M-T-203-V2）给「$BC$ 边上的高」⟹ 用两种面积公式把 $a^{2}$ 写成 $2\sqrt3\,bc\sin A$，再与余弦定理相加即得 $\dfrac bc+\dfrac cb=2\sqrt3\sin A+2\cos A=4\sin\left(A+\dfrac\pi6\right)$。> ⭐⭐ 左边 $\dfrac bc+\dfrac cb=k+\dfrac1k$（因 $k=\dfrac cb=\dfrac{\sin C}{\sin B}$），> 故 $k+\dfrac1k\le4$ ⟹ $k\in[2-\sqrt3,\,2+\sqrt3]$，$k_{\min}=2-\sqrt3$，> 此时必须 $\sin\left(A+\dfrac\pi6\right)=1$ ⟹ $A=\dfrac\pi3$。> ⚠ **「左边 $\ge2$」给下界、「右边 $\le4$」给上界**，两个不等式合起来才锁定 $k$。"""

T199_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知边长为 $2$ 的等边三角形 $ABC$，$D$ 是平面 $ABC$ 内一点，"
        r"且满足 $DB:DC=2:1$，则三角形 $ABD$ 面积的最大值为（　　）"
    ),
    'opts': [
        ['A', r"$\dfrac{2\sqrt3}{3}+\dfrac43$"],
        ['B', r"$\sqrt3$"],
        ['C', r"$\dfrac{4\sqrt3}{3}+\dfrac43$"],
        ['D', r"$\dfrac{4\sqrt3}{3}$"],
    ],
    'answer': 'C',
    'analysis': (
        r"$DB:DC=2:1$ 且 $D$ 在平面内 ⟹ 阿波罗尼斯圆；"
        r"$\triangle ABD$ 的底 $AB$ 固定，故面积最大 ⟺ $D$ 到直线 $AB$ 的距离最大，"
        r"即「圆心到直线的距离 $d$ + 半径 $r$」．"
    ),
    'solution': (
        r"以 $BC$ 的中点 $O$ 为原点建立平面直角坐标系，则" "\n"
        r"$$A\left(0,\sqrt3\right),\quad B(-1,0),\quad C(1,0),\quad |AB|=2.$$" "\n"
        r"设 $D(x,y)$，由 $DB:DC=2:1$ 得 $DB^{2}=4DC^{2}$：" "\n"
        r"$$(x+1)^{2}+y^{2}=4\left[(x-1)^{2}+y^{2}\right]\ \Longrightarrow\ "
        r"x^{2}-\frac{10}{3}x+1+y^{2}=0\ \Longrightarrow\ \left(x-\frac53\right)^{2}+y^{2}=\frac{16}{9}.$$" "\n"
        r"即 $D$ 的轨迹是以 $M\left(\dfrac53,0\right)$ 为圆心、$r=\dfrac43$ 为半径的圆（阿波罗尼斯圆）．" "\n"
        r"直线 $AB$ 过 $A(0,\sqrt3)$、$B(-1,0)$，斜率为 $\sqrt3$，方程为 $\sqrt3x-y+\sqrt3=0$．" "\n"
        r"圆心 $M$ 到该直线的距离为" "\n"
        r"$$d=\frac{\left|\sqrt3\cdot\dfrac53-0+\sqrt3\right|}{\sqrt{3+1}}"
        r"=\frac{\dfrac{8\sqrt3}{3}}{2}=\frac{4\sqrt3}{3}.$$" "\n"
        r"故 $D$ 到直线 $AB$ 的最大距离为 $d+r=\dfrac{4\sqrt3}{3}+\dfrac43$，于是" "\n"
        r"$$S_{\triangle ABD}^{\max}=\frac12\cdot|AB|\cdot(d+r)"
        r"=\frac12\cdot2\cdot\left(\frac{4\sqrt3}{3}+\frac43\right)=\frac{4\sqrt3}{3}+\frac43,$$" "\n"
        r"故选 C．"
    ),
    'review': (
        r"① ⭐⭐ **题眼是「$DB:DC=$ 定值 ⟹ 阿波罗尼斯圆」**："
        r"$k\ne1$ 时轨迹是圆，圆心在直线 $BC$ 上，本题圆心 $\left(\dfrac53,0\right)$ 在 $C$ 的右侧 ✓" "\n"
        r"② 数值复核：在圆上取 $2\times10^{6}$ 个点求 $\triangle ABD$ 面积，"
        r"最大值 $3.6427344$，与 $\dfrac{4\sqrt3}{3}+\dfrac43=3.6427344$ **逐位相同**；"
        r"取到点约 $(2.8214,-0.6667)$ ✓✓" "\n"
        r"③ ⚠ **干扰项的来历**：D 项的 $\dfrac{4\sqrt3}{3}$ 就是 $d$——只算了圆心到直线的距离、"
        r"忘了加半径 $r$；B 项的 $\sqrt3$ 恰是正三角形 $ABC$ 自身的面积；"
        r"A 项则是把 $d$ 误算成 $\dfrac{2\sqrt3}{3}$（漏了 $\left|\sqrt3\cdot\frac53\right|$ 中的 $\frac53$）" "\n"
        r"④ ⚠ **B 项存疑**：原书选项行 OCR 只剩「$3$」，按同页「$\sqrt3x-y+\sqrt3=0$」被提取为"
        r"「$3x-y+3=0$」的规律，根号常丢失，故判定为 $\sqrt3$；答案 C 不受影响 ✓"
    ),
    'topics': ['M-T-199'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-199-E1',
}

T199_V3 = {
    'type': '选择',
    'stem_text': (
        r"如图所示，在平面直角坐标系 $xOy$ 中，点 $B$、$C$ 分别在 $x$ 轴和 $y$ 轴的非负半轴上，"
        r"点 $A$ 在第一象限，且 $\angle BAC=90^\circ$，$AB=AC=4$，那么 $O$、$A$ 两点间距离的（　　）"
    ),
    'opts': [
        ['A', r"最大值是 $4\sqrt2$，最小值是 $4$"],
        ['B', r"最大值是 $8$，最小值是 $4$"],
        ['C', r"最大值是 $4\sqrt2$，最小值是 $2$"],
        ['D', r"最大值是 $8$，最小值是 $2$"],
    ],
    'answer': 'A',
    'analysis': (
        r"把 $A$ 用 $BC$ 的中点 $E$ 表示：由 $AB=AC$ 且 $\angle BAC=90^\circ$ 知 "
        r"$AE\perp BC$ 且 $AE=\dfrac{|BC|}{2}=2\sqrt2$，于是 $A$ 的坐标一次写出，"
        r"$|OA|$ 化为 $b+c$ 的一元函数．"
    ),
    'solution': (
        r"设 $B(b,0)$、$C(0,c)$，其中 $b,c\ge0$．由 $\angle BAC=90^\circ$、$AB=AC=4$ 得" "\n"
        r"$$|BC|=\sqrt{AB^{2}+AC^{2}}=4\sqrt2\ \Longrightarrow\ b^{2}+c^{2}=|BC|^{2}=32.$$" "\n"
        r"设 $E$ 为 $BC$ 的中点，则 $E\left(\dfrac b2,\dfrac c2\right)$．"
        r"因 $\triangle ABC$ 是等腰直角三角形（$A$ 为直角顶点），故 $AE\perp BC$ 且 $AE=\dfrac{|BC|}{2}=2\sqrt2$．" "\n"
        r"$\vec{BC}=(-b,c)$，与其垂直且模为 $4\sqrt2$ 的向量为 $\pm(c,b)$，"
        r"故 $\vec{EA}=\pm\dfrac{2\sqrt2}{4\sqrt2}(c,b)=\pm\left(\dfrac c2,\dfrac b2\right)$，即" "\n"
        r"$$A=\left(\frac b2,\frac c2\right)\pm\left(\frac c2,\frac b2\right)." "\n"
        r"取「$-$」号时两坐标异号（$b\ne c$ 时必有一个为负），与 $A$ 在第一象限矛盾，故取「$+$」号：" "\n"
        r"$$A=\left(\frac{b+c}2,\ \frac{b+c}2\right)\ \Longrightarrow\ |OA|=\sqrt2\cdot\frac{b+c}2=\frac{b+c}{\sqrt2}.$$" "\n"
        r"由 $b^{2}+c^{2}=32$ 且 $b,c\ge0$，有 $0\le bc\le\dfrac{b^{2}+c^{2}}2=16$，于是" "\n"
        r"$$(b+c)^{2}=b^{2}+c^{2}+2bc=32+2bc\in[32,\,64]\ \Longrightarrow\ b+c\in\left[4\sqrt2,\,8\right],$$" "\n"
        r"从而 $|OA|=\dfrac{b+c}{\sqrt2}\in\left[4,\,4\sqrt2\right]$．" "\n"
        r"下界在 $bc=0$（即 $B$ 或 $C$ 与 $O$ 重合）时取到，上界在 $b=c=4$（$ABOC$ 为正方形）时取到，"
        r"故最大值是 $4\sqrt2$、最小值是 $4$．故选 A．"
    ),
    'review': (
        r"① ⭐⭐ **核心是「$A=E\pm$ 垂直向量」**：$A$ 的坐标一次成型，"
        r"比原书按 $BC$ 与 $x$ 轴夹角 $\theta$ 分 $\theta=0$、$0<\theta<\dfrac\pi4$、"
        r"$\theta=\dfrac\pi4$、$\dfrac\pi4<\theta<\pi$、$\theta=\pi$ 五种情况讨论简洁得多 ✓✓" "\n"
        r"② 数值复核：在 $b^{2}+c^{2}=32$ 上取 $2\times10^{5}$ 个点，"
        r"$|OA|$ 的范围恰为 $[4.000000,\ 5.656854]=[4,\ 4\sqrt2]$ ✓✓" "\n"
        r"③ 取 $b=3$、$c=\sqrt{23}$ 验证：$A=\left(\dfrac{3+\sqrt{23}}2,\dfrac{3+\sqrt{23}}2\right)$，"
        r"$|AB|=|AC|=4.000000$、$\angle BAC=90.0^\circ$ ✓" "\n"
        r"④ ⭐ **$|OA|=\dfrac{b+c}{\sqrt2}$ 与 $b^{2}+c^{2}$ 固定** ⟹ 本质是「和方 = 平方和 + 2 倍积」；" "\n"
        r"   $bc$ 取两端时 $|OA|$ 取两端，而 $bc\in[0,16]$ 由 $b,c\ge0$ 保证（若允许负半轴则 $bc$ 可为负）" "\n"
        r"⑤ ⚠ 干扰项 B、D 的「$8$」来自把 $|OA|$ 当成 $b+c$（忘了除以 $\sqrt2$）；"
        r"C 的「$2$」来自 $b+c$ 的最小值误取 $2\sqrt2$"
    ),
    'topics': ['M-T-199'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-199-V3',
}

T201_E1 = {
    'type': '选择',
    'stem_text': (
        r"以 $BC$ 为底边的等腰三角形 $ABC$ 中，腰 $AC$ 边上的中线长为 $9$，"
        r"当 $\triangle ABC$ 面积取最大时，腰 $AB$ 长为（　　）"
    ),
    'opts': [
        ['A', r"$2\sqrt5$"],
        ['B', r"$4\sqrt5$"],
        ['C', r"$6\sqrt5$"],
        ['D', r"前三个答案都不对"],
    ],
    'answer': 'C',
    'analysis': (
        r"设腰 $AB=AC=b$、底 $BC=a$，在 $\triangle ABD$（$D$ 为 $AC$ 中点）中用余弦定理"
        r"把 $b$ 消去一个，得 $b^{2}+2a^{2}=324$；再把面积写成 $a$ 的一元函数求最值．"
    ),
    'solution': (
        r"设 $AB=AC=b$、$BC=a$，$D$ 为 $AC$ 的中点，则 $BD=9$，$AD=\dfrac b2$．" "\n"
        r"在 $\triangle ABC$ 中由余弦定理：" "\n"
        r"$$\cos A=\frac{b^{2}+c^{2}-a^{2}}{2bc}\bigg|_{c=b}=\frac{2b^{2}-a^{2}}{2b^{2}}.$$" "\n"
        r"在 $\triangle ABD$ 中再用余弦定理：" "\n"
        r"$$BD^{2}=AB^{2}+AD^{2}-2\cdot AB\cdot AD\cos A=b^{2}+\frac{b^{2}}4-2\cdot b\cdot\frac b2\cdot\frac{2b^{2}-a^{2}}{2b^{2}}=\frac{5b^{2}}4-\frac{2b^{2}-a^{2}}2=\frac{b^{2}}4+\frac{a^{2}}2,$$" "\n"
        r"即 $\dfrac{b^{2}}4+\dfrac{a^{2}}2=81$，亦即 $b^{2}+2a^{2}=324$．" "\n"
        r"$\triangle ABC$ 底边 $BC$ 上的高 $h=\sqrt{b^{2}-\dfrac{a^{2}}4}$，故" "\n"
        r"$$S=\frac12ah=\frac12a\sqrt{b^{2}-\frac{a^{2}}4}=\frac12a\sqrt{324-2a^{2}-\frac{a^{2}}4}=\frac12a\sqrt{324-\frac94a^{2}},$$" "\n"
        r"$$S^{2}=\frac14a^{2}\left(324-\frac94a^{2}\right)=-\frac9{16}a^{4}+81a^{2},$$" "\n"
        r"这是关于 $a^{2}$ 的二次函数，当 $a^{2}=\dfrac{81}{2\cdot\frac9{16}}=72$ 时取最大值．" "\n"
        r"此时 $b^{2}=324-2a^{2}=324-144=180$，故 $b=6\sqrt5$，即腰 $AB=6\sqrt5$．故选 C．"
    ),
    'review': (
        r"① ⭐⭐ **中线题的固定动作：在「半个三角形」里再写一次余弦定理**，"
        r"角 $A$ 的余弦由原三角形给出，代入后 $b^{2}$ 与 $a^{2}$ 的系数恰好凑成 $b^2+2a^2$ ✓" "\n"
        r"② 数值复核：扫 $a^{2}\in(0,162)$，$S$ 的最大值 $54.000$ 在 $a^{2}=72$ 处取到，"
        r"此时 $b^{2}=180$、$b=13.4164=6\sqrt5$ ✓✓" "\n"
        r"③ ⭐ **最值的「巧合」可供自检**：$a^{2}=72$、$b^{2}=180$ 时 $S_{\max}=54$，"
        r"而 $b=\sqrt{180}$ 与 $a=\sqrt{72}=6\sqrt2$ 满足 $b^{2}+2a^{2}=180+144=324$ ✓" "\n"
        r"④ ⚠ **别把「以 $BC$ 为底边的等腰三角形」读成 $AB=BC$**："
        r"底边是 $BC$ ⟹ 两腰是 $AB=AC=b$，这是列式的起点" "\n"
        r"⑤ 干扰项 A、B 分别是 $2\sqrt5$、$4\sqrt5$——若把 $b^{2}+2a^{2}=324$ 错记成"
        r"$2b^{2}+a^{2}=324$，最值点会移到 $a^{2}=36$、$b^{2}=144$（得 $b=12$，不在选项中）"
    ),
    'topics': ['M-T-201'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-201-E1',
}

T233_E1 = {
    'type': '选择',
    'stem_text': (
        r"如图，在 $\triangle ABC$ 中，$\overrightarrow{AN}=\dfrac13\overrightarrow{NC}$，"
        r"$P$ 是 $BN$ 上的一点，若 $\overrightarrow{AP}=\left(m+\dfrac29\right)\overrightarrow{AB}+\dfrac29\overrightarrow{BC}$，则实数 $m$ 的值为（　　）"
    ),
    'opts': [
        ['A', r"$\dfrac19$"],
        ['B', r"$\dfrac13$"],
        ['C', r"$1$"],
        ['D', r"$3$"],
    ],
    'answer': 'A',
    'analysis': (
        r"把 $\vec{AP}$ 用「$\vec{AB}$＋$t\vec{BN}$」表示（$P$ 在 $BN$ 上），"
        r"再与题给的 $\vec{AB}$、$\vec{AC}$ 表达式比对系数．"
    ),
    'solution': (
        r"由 $\overrightarrow{AN}=\dfrac13\overrightarrow{NC}$ 且 $N$ 在线段 $AC$ 上，得" "\n"
        r"$$\overrightarrow{AN}=\frac14\overrightarrow{AC},\qquad "
        r"\overrightarrow{CN}=-\frac34\overrightarrow{AC}.$$" "\n"
        r"**第一步：把题设化成 $\vec{AB}$、$\vec{AC}$ 的表达式．**" "\n"
        r"因 $\overrightarrow{BC}=\overrightarrow{AC}-\overrightarrow{AB}$，故" "\n"
        r"$$\overrightarrow{AP}=\left(m+\frac29\right)\overrightarrow{AB}+\frac29\overrightarrow{BC}=\left(m+\frac29\right)\overrightarrow{AB}+\frac29\left(\overrightarrow{AC}-\overrightarrow{AB}\right)=m\overrightarrow{AB}+\frac29\overrightarrow{AC}.\qquad(\ast)$$" "\n"
        r"**第二步：用 $P\in BN$ 再写一次 $\vec{AP}$．**" "\n"
        r"设 $\overrightarrow{BP}=t\overrightarrow{BN}$（$0\le t\le1$），则" "\n"
        r"$$\overrightarrow{AP}=\overrightarrow{AB}+\overrightarrow{BP}=\overrightarrow{AB}+t\left(\overrightarrow{BC}+\overrightarrow{CN}\right)=\overrightarrow{AB}+t\left(\overrightarrow{AC}-\overrightarrow{AB}-\frac34\overrightarrow{AC}\right)=(1-t)\overrightarrow{AB}+\frac t4\overrightarrow{AC}.$$" "\n"
        r"**第三步：比对系数．** 与 $(\ast)$ 比较（$\vec{AB}$、$\vec{AC}$ 不共线）得" "\n"
        r"$$\frac t4=\frac29\ \Longrightarrow\ t=\frac89,\qquad m=1-t=1-\frac89=\frac19.$$" "\n"
        r"故选 A．"
    ),
    'review': (
        r"① ⭐⭐ **通法：先用 $\vec{BC}=\vec{AC}-\vec{AB}$ 把题设统一成 $\vec{AB}$、$\vec{AC}$ 的线性组合**，"
        r"再用「点在 $BN$ 上」写出 $\vec{AP}=\vec{AB}+t\vec{BN}$，两次比对系数即可；"
        r"全程不需要坐标 ✓✓" "\n"
        r"② ⚠ **$\overrightarrow{AN}=\dfrac13\overrightarrow{NC}$ 是向量等式（同向）**，"
        r"所以 $AN:NC=1:3$，即 $\overrightarrow{AN}=\dfrac14\overrightarrow{AC}$——"
        r"误读成 $\dfrac13\overrightarrow{AC}$ 会得 $t=\dfrac{8}{9}$ 之外的错值" "\n"
        r"③ 数值复核：$t=\dfrac89\in[0,1]$，故 $P$ 确实在线段 $BN$ 上 ✓；"
        r"代回得 $\vec{AP}=\dfrac19\vec{AB}+\dfrac29\vec{AC}$，而题设 "
        r"$\left(\dfrac19+\dfrac29\right)\vec{AB}+\dfrac29\vec{BC}=\dfrac13\vec{AB}+\dfrac29(\vec{AC}-\vec{AB})=\dfrac19\vec{AB}+\dfrac29\vec{AC}$ ✓✓" "\n"
        r"④ ⭐ **干扰项 B 的 $\dfrac13$ 恰是 $m+\dfrac29$**："
        r"若忘了把 $\dfrac29\vec{BC}$ 拆开、直接令 $m+\dfrac29=1-t$ 就会选 B"
    ),
    'topics': ['M-T-233'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-233-E1',
}

T203_V2 = {
    'type': '选择',
    'stem_text': (
        r"在 $\triangle ABC$ 中，内角 $A$、$B$、$C$ 的对边分别是 $a$、$b$、$c$，"
        r"且 $BC$ 边上的高为 $\dfrac{\sqrt3}{6}a$．若 $\sin C=k\sin B$，"
        r"则当 $k$ 取最小值时，内角 $A$ 的大小为（　　）"
    ),
    'opts': [
        ['A', r"$\dfrac\pi2$"],
        ['B', r"$\dfrac\pi6$"],
        ['C', r"$\dfrac\pi3$"],
        ['D', r"$\dfrac{2\pi}3$"],
    ],
    'answer': 'C',
    'analysis': (
        r"用两种面积公式把「高」翻译成 $a^{2}=2\sqrt3\,bc\sin A$，与余弦定理相加得"
        r"$\dfrac bc+\dfrac cb=4\sin\left(A+\dfrac\pi6\right)$；左边是 $k+\dfrac1k$，"
        r"由「$\ge2$」与「$\le4$」两头夹出 $k$ 的范围．"
    ),
    'solution': (
        r"**第一步：把「高」翻译成边角关系．** 由 $S=\dfrac12a\cdot\dfrac{\sqrt3}{6}a=\dfrac{\sqrt3}{12}a^{2}$ 及 $S=\dfrac12bc\sin A$ 得" "\n"
        r"$$\frac12bc\sin A=\frac{\sqrt3}{12}a^{2}\ \Longrightarrow\ a^{2}=2\sqrt3\,bc\sin A.$$" "\n"
        r"又由余弦定理 $a^{2}=b^{2}+c^{2}-2bc\cos A$，两式相加消去 $a^{2}$：" "\n"
        r"$$b^{2}+c^{2}=2\sqrt3\,bc\sin A+2bc\cos A\ \Longrightarrow\ "
        r"\frac bc+\frac cb=2\sqrt3\sin A+2\cos A=4\sin\left(A+\frac\pi6\right).\qquad(\ast)$$" "\n"
        r"**第二步：把左边换成 $k$．** 由正弦定理 $\dfrac cb=\dfrac{\sin C}{\sin B}=k$，故 $(\ast)$ 为" "\n"
        r"$$k+\frac1k=4\sin\left(A+\frac\pi6\right).$$" "\n"
        r"**第三步：两头夹．** 一方面 $k+\dfrac1k\ge2$；另一方面 $\sin\left(A+\dfrac\pi6\right)\le1$ 给出 $k+\dfrac1k\le4$，即" "\n"
        r"$$k^{2}-4k+1\le0\ \Longrightarrow\ 2-\sqrt3\le k\le2+\sqrt3,$$" "\n"
        r"故 $k_{\min}=2-\sqrt3$（此时 $k+\dfrac1k=4$）．" "\n"
        r"**第四步：求此时的 $A$．** $k_{\min}$ 对应 $4\sin\left(A+\dfrac\pi6\right)=4$，即"
        r"$\sin\left(A+\dfrac\pi6\right)=1$．因 $0<A<\pi$ 时 $\dfrac\pi6<A+\dfrac\pi6<\dfrac{7\pi}6$，故" "\n"
        r"$$A+\frac\pi6=\frac\pi2\ \Longrightarrow\ A=\frac\pi3.$$" "\n"
        r"故选 C．"
    ),
    'review': (
        r"① ⭐⭐ **题眼是「给高」而不是「给角」**：把高代入 $S=\dfrac12ah_a$ 与 $S=\dfrac12bc\sin A$ 相等，"
        r"$a^{2}$ 就带上了 $\sin A$，再与余弦定理相加才能凑出 $\dfrac bc+\dfrac cb$ ✓✓" "\n"
        r"② ⭐⭐ **「$\ge2$」与「$\le4$」必须合用**：只用 $k+\dfrac1k\ge2$ 得不出上界，"
        r"只用 $\le4$ 又给不出最小值——$k$ 的范围是两者之交 ✓" "\n"
        r"③ 数值复核：$k=2-\sqrt3=0.267949$ 时 $k+\dfrac1k=0.267949+3.732051=4.000000$ ✓；"
        r"取 $A=\dfrac\pi3$，则 $2\sqrt3\sin A+2\cos A=3+1=4$ ✓✓" "\n"
        r"④ ⚠ **干扰项 A（$\dfrac\pi2$）**：此时 $2\sqrt3\sin A+2\cos A=2\sqrt3\approx3.46$，"
        r"对应 $k+\dfrac1k=3.46$ 的两个根都不等于 $2-\sqrt3$；"
        r"B（$\dfrac\pi6$）得 $1+\sqrt3\approx2.73$，D（$\dfrac{2\pi}3$）得 $3-1=2$（即 $k=1$，"
        r"是 $k$ 能取到的「等边」情形，不是最小值）"
    ),
    'topics': ['M-T-203'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-203-V2',
}

T232_V3 = {
    'type': '选择',
    'stem_text': (
        r"$D$、$E$、$F$ 为 $\triangle ABC$ 所在平面内三点，且 $\overrightarrow{BD}=\overrightarrow{DC}$，"
        r"$\overrightarrow{AE}=2\overrightarrow{EC}$，$\overrightarrow{AF}=\overrightarrow{FD}$，"
        r"则 $\overrightarrow{EF}=$（　　）"
    ),
    'opts': [
        ['A', r"$\dfrac12\overrightarrow{AB}-\dfrac16\overrightarrow{AC}$"],
        ['B', r"$\dfrac12\overrightarrow{AB}-\dfrac13\overrightarrow{AC}$"],
        ['C', r"$\dfrac14\overrightarrow{AB}-\dfrac13\overrightarrow{AC}$"],
        ['D', r"$\dfrac14\overrightarrow{AB}-\dfrac5{12}\overrightarrow{AC}$"],
    ],
    'answer': 'D',
    'analysis': (
        r"先把三个条件翻译成「谁是谁的中点／几等分点」，再统一用 "
        r"$\vec{EF}=\vec{AF}-\vec{AE}$ 拆到 $\vec{AB}$、$\vec{AC}$ 上．"
    ),
    'solution': (
        r"由 $\overrightarrow{BD}=\overrightarrow{DC}$ 知 $D$ 为 $BC$ 的中点；" "\n"
        r"由 $\overrightarrow{AE}=2\overrightarrow{EC}$（同向）知 $E$ 在 $AC$ 上且 $AE:EC=2:1$；" "\n"
        r"由 $\overrightarrow{AF}=\overrightarrow{FD}$ 知 $F$ 为 $AD$ 的中点．" "\n"
        r"于是" "\n"
        r"$$\overrightarrow{AD}=\frac12\left(\overrightarrow{AB}+\overrightarrow{AC}\right),\qquad "
        r"\overrightarrow{AF}=\frac12\overrightarrow{AD}=\frac14\left(\overrightarrow{AB}+\overrightarrow{AC}\right),\qquad "
        r"\overrightarrow{AE}=\frac23\overrightarrow{AC}.$$" "\n"
        r"故" "\n"
        r"$$\overrightarrow{EF}=\overrightarrow{AF}-\overrightarrow{AE}=\frac14\overrightarrow{AB}+\frac14\overrightarrow{AC}-\frac23\overrightarrow{AC}=\frac14\overrightarrow{AB}-\frac5{12}\overrightarrow{AC}.$$" "\n"
        r"（其中 $\dfrac14-\dfrac23=\dfrac3{12}-\dfrac8{12}=-\dfrac5{12}$．）故选 D．"
    ),
    'review': (
        r"① ⭐⭐ **统一到「从 $A$ 出发」**：$\vec{EF}=\vec{AF}-\vec{AE}$，避免用 "
        r"$\vec{EF}=\vec{EA}+\vec{AF}$ 时符号出错；三个点都用 $\vec{AB}$、$\vec{AC}$ 表示后" "\n"
        r"   只剩一次合并同类项 ✓" "\n"
        r"② ⚠ **$\overrightarrow{AE}=2\overrightarrow{EC}$ 是向量等式**：同向 ⟹ "
        r"$\vec{AE}=\dfrac23\vec{AC}$（不是 $\dfrac12$ 也不是 $2\vec{AC}$）——"
        r"误读成 $AE=\dfrac12AC$ 得 $-\dfrac14\vec{AC}$，不在选项中" "\n"
        r"③ 数值复核：取 $A(0,0)$、$B(4,0)$、$C(0,6)$，则 $D(2,3)$、$E(0,4)$、$F(1,1.5)$，"
        r"$\vec{EF}=(1,-2.5)$；而 $\dfrac14\vec{AB}-\dfrac5{12}\vec{AC}=(1,0)-(0,2.5)=(1,-2.5)$ ✓✓" "\n"
        r"④ ⭐ **干扰项 A、B 的 $\dfrac12\vec{AB}$** 来自把 $F$ 当成 $BC$ 中点"
        r"（即 $\vec{AF}=\dfrac12(\vec{AB}+\vec{AC})$）——漏了 $F$ 是 $AD$ 中点这一层；"
        r"C 项的 $-\dfrac13\vec{AC}$ 则是 $\dfrac14-\dfrac23$ 算成 $\dfrac14-\dfrac7{12}$ 之类的通分错误"
    ),
    'topics': ['M-T-232'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-232-V3',
}

T233_V2 = {
    'type': '选择',
    'stem_text': (
        r"在平行四边形 $ABCD$ 中，点 $E$、$F$ 分别满足 $\overrightarrow{BE}=\dfrac12\overrightarrow{BC}$，"
        r"$\overrightarrow{DF}=\dfrac13\overrightarrow{DC}$．若 $\overrightarrow{BD}=\lambda\overrightarrow{AE}+\mu\overrightarrow{AF}$，则实数 $\lambda+\mu$ 的值为（　　）"
    ),
    'opts': [
        ['A', r"$-\dfrac15$"],
        ['B', r"$\dfrac15$"],
        ['C', r"$-\dfrac75$"],
        ['D', r"$\dfrac75$"],
    ],
    'answer': 'B',
    'analysis': (
        r"取 $\vec{AB}=\vec a$、$\vec{AD}=\vec b$ 为基底，把 $\vec{AE}$、$\vec{AF}$、$\vec{BD}$ "
        r"都写成 $\vec a$、$\vec b$ 的线性组合，比对系数得二元一次方程组．"
    ),
    'solution': (
        r"设 $\overrightarrow{AB}=\vec a$，$\overrightarrow{AD}=\vec b$，则 $\overrightarrow{DC}=\vec a$、"
        r"$\overrightarrow{BC}=\vec b$．" "\n"
        r"由 $\overrightarrow{BE}=\dfrac12\overrightarrow{BC}=\dfrac12\vec b$ 得 $\overrightarrow{AE}=\vec a+\dfrac12\vec b$；" "\n"
        r"由 $\overrightarrow{DF}=\dfrac13\overrightarrow{DC}=\dfrac13\vec a$ 得 "
        r"$\overrightarrow{AF}=\vec b+\dfrac13\vec a=\dfrac13\vec a+\vec b$；" "\n"
        r"又 $\overrightarrow{BD}=\overrightarrow{AD}-\overrightarrow{AB}=\vec b-\vec a$．" "\n"
        r"代入 $\overrightarrow{BD}=\lambda\overrightarrow{AE}+\mu\overrightarrow{AF}$：" "\n"
        r"$$-\vec a+\vec b=\lambda\left(\vec a+\frac12\vec b\right)+\mu\left(\frac13\vec a+\vec b\right)=\left(\lambda+\frac{\mu}3\right)\vec a+\left(\frac{\lambda}2+\mu\right)\vec b.$$" "\n"
        r"由 $\vec a$、$\vec b$ 不共线得" "\n"
        r"$$\begin{cases}\lambda+\dfrac{\mu}3=-1,\\[2mm]\dfrac{\lambda}2+\mu=1,\end{cases}$$" "\n"
        r"由第一式 $\lambda=-1-\dfrac{\mu}3$ 代入第二式：$-\dfrac12-\dfrac{\mu}6+\mu=1$，"
        r"即 $\dfrac56\mu=\dfrac32$，$\mu=\dfrac95$，从而 $\lambda=-1-\dfrac35=-\dfrac85$．" "\n"
        r"故 $\lambda+\mu=-\dfrac85+\dfrac95=\dfrac15$．故选 B．"
    ),
    'review': (
        r"① ⭐⭐ **平行四边形的标准基底**：$\vec{AB}=\vec a$、$\vec{AD}=\vec b$，"
        r"则 $\vec{DC}=\vec a$、$\vec{BC}=\vec b$、$\vec{BD}=\vec b-\vec a$——"
        r"这三条是全部起点，必须一次写对 ✓✓" "\n"
        r"② 数值复核：$\lambda=-\dfrac85=-1.6$、$\mu=\dfrac95=1.8$；"
        r"$-1.6+\dfrac{1.8}3=-1.6+0.6=-1$ ✓，$-\dfrac{1.6}2+1.8=-0.8+1.8=1$ ✓✓" "\n"
        r"③ ⭐ **$\lambda$、$\mu$ 异号是这类题的常态**（$\vec{BD}$ 落在 $\vec{AE}$、$\vec{AF}$ 夹角之外），"
        r"而它们的和却是一个很小的正数 $\dfrac15$——干扰项 A（$-\dfrac15$）就是符号弄反的结果" "\n"
        r"④ ⚠ **$\overrightarrow{DF}=\dfrac13\overrightarrow{DC}$ 意味着 $CF=\dfrac23DC$**："
        r"若误取 $\vec{AF}=\vec b+\dfrac23\vec a$ 会得 $\lambda=-\dfrac{21}{10}$、$\mu=\dfrac{16}{10}$，"
        r"$\lambda+\mu=-\dfrac12$，不在选项中" "\n"
        r"⑤ C、D 两项的 $\pm\dfrac75$ 是 $|\lambda|+|\mu|$ 型的干扰值"
        r"（$\dfrac85+\dfrac95\ne\dfrac75$，但 $\left|\dfrac85-\dfrac95\right|$ 之类的算法容易凑出 $7$）"
    ),
    'topics': ['M-T-233'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-233-V2',
}

T207_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知 $O$ 是三角形 $ABC$ 的外心，若 $\dfrac{AC}{AB}\overrightarrow{AB}\cdot\overrightarrow{AO}+\dfrac{AB}{AC}\overrightarrow{AC}\cdot\overrightarrow{AO}=2m\overrightarrow{AO}^{2}$，"
        r"且 $\sin B+\sin C=\sqrt3$，则实数 $m$ 的最大值为（　　）"
    ),
    'opts': [
        ['A', r"$3$"],
        ['B', r"$\dfrac35$"],
        ['C', r"$\dfrac75$"],
        ['D', r"$\dfrac32$"],
    ],
    'answer': 'D',
    'analysis': (
        r"外心在边的中垂线上 ⟹ $\vec{AO}$ 在 $\vec{AB}$ 上的投影是 $\dfrac c2$，"
        r"代入即把数量积化成 $bc=2m\,AO^{2}$；再用正弦定理把 $\sin B+\sin C$ 化成 "
        r"$\dfrac{b+c}{2AO}$，最后用基本不等式．"
    ),
    'solution': (
        r"记 $AB=c$、$AC=b$、$\angle BAO=\theta$、$\angle CAO=\alpha$．" "\n"
        r"**第一步：化简已知等式．** 由 $\dfrac{AC}{AB}=\dfrac bc$、$\dfrac{AB}{AC}=\dfrac cb$ 得" "\n"
        r"$$\frac bc\cdot\overrightarrow{AB}\cdot\overrightarrow{AO}+\frac cb\cdot"
        r"\overrightarrow{AC}\cdot\overrightarrow{AO}=\frac bc\cdot c\cdot AO\cos\theta+\frac cb\cdot b\cdot AO\cos\alpha=b\,AO\cos\theta+c\,AO\cos\alpha=2m\,AO^{2}.\qquad(\ast)$$" "\n"
        r"**第二步：用外心求 $\cos\theta$、$\cos\alpha$．** "
        r"$O$ 在 $AB$ 的中垂线上 ⟹ $\vec{AO}$ 在 $\vec{AB}$ 方向上的投影等于 $\dfrac c2$，即 "
        r"$AO\cos\theta=\dfrac c2$，$\cos\theta=\dfrac c{2AO}$；同理 $\cos\alpha=\dfrac b{2AO}$．" "\n"
        r"代入 $(\ast)$：" "\n"
        r"$$b\cdot\frac c2+c\cdot\frac b2=2m\,AO^{2}\ \Longrightarrow\ bc=2m\,AO^{2}\ \Longrightarrow\ m=\frac{bc}{2AO^{2}}.$$" "\n"
        r"**第三步：处理 $\sin B+\sin C$．** $AO$ 是外接圆半径，由正弦定理" "\n"
        r"$$\sin B=\frac b{2AO},\qquad \sin C=\frac c{2AO}\ \Longrightarrow\ "
        r"\sin B+\sin C=\frac{b+c}{2AO}=\sqrt3\ \Longrightarrow\ b+c=2\sqrt3\,AO.$$" "\n"
        r"**第四步：基本不等式．**" "\n"
        r"$$m=\frac{bc}{2AO^{2}}\le\frac{\left(\dfrac{b+c}2\right)^{2}}{2AO^{2}}=\frac{(b+c)^{2}}{8AO^{2}}=\frac{\left(2\sqrt3\,AO\right)^{2}}{8AO^{2}}=\frac{12}{8}=\frac32,$$" "\n"
        r"当且仅当 $b=c$ 时取等号（此时 $AO=\dfrac{b+c}{2\sqrt3}=\dfrac{2b}{2\sqrt3}=\dfrac b{\sqrt3}$，"
        r"确有解）．故 $m$ 的最大值为 $\dfrac32$，选 D．"
    ),
    'review': (
        r"① ⭐⭐ **核心一步是「外心 ⟹ 投影 $=\dfrac c2$」**："
        r"$O$ 在 $AB$ 的中垂线上，$\vec{AO}$ 在 $\vec{AB}$ 上的投影就是 $A$ 到垂足（$AB$ 中点）的距离 ✓✓" "\n"
        r"② 第二步代入后 $\dfrac bc\cdot c$ 与 $\dfrac cb\cdot b$ **恰好约成 $b$ 与 $c$**——"
        r"这正是题面把系数写成 $\dfrac{AC}{AB}$、$\dfrac{AB}{AC}$ 的原因（若写成 $\dfrac{AB}{AC}$、"
        r"$\dfrac{AC}{AB}$ 就约不干净）✓" "\n"
        r"③ 取等验证：$b=c$ 时 $b+c=2b=2\sqrt3 AO$ ⟹ $AO=\dfrac b{\sqrt3}$；"
        r"由 $AO$ 是外接圆半径，$b=2AO\sin B$ ⟹ $\sin B=\dfrac b{2AO}=\dfrac{\sqrt3}2$ ⟹ $B=60^\circ$；" "\n"
        r"  同理 $C=60^\circ$、$A=60^\circ$（等边），此时 $m=\dfrac{b^{2}}{2AO^{2}}=\dfrac{b^2}{2b^2/3}=\dfrac32$ ✓✓" "\n"
        r"④ ⚠ **$m=\dfrac{bc}{2AO^{2}}$ 中 $AO$ 也是变量**：不能把 $AO$ 当常数，"
        r"必须靠 $b+c=2\sqrt3 AO$ 把它换成 $b+c$ 后才能用基本不等式 ✓" "\n"
        r"⑤ 干扰项 A（$3$）是漏了分母的 $2$；B（$\dfrac35$）、C（$\dfrac75$）来自 "
        r"$\sin B+\sin C=\sqrt3$ 被误读成 $\sin B\cdot\sin C$ 或 $\cos B+\cos C$"
    ),
    'topics': ['M-T-207'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-207-V3',
}

T232_E1 = {
    'type': '选择',
    'stem_text': (
        r"“赵爽弦图”是由四个全等的直角三角形与一个小正方形拼成的一个大正方形，如图所示．"
        r"在“赵爽弦图”中，若 $\overrightarrow{BC}=\vec a$，$\overrightarrow{BA}=\vec b$，"
        r"$BE=3EF$，则 $\overrightarrow{BF}=$（　　）"
    ),
    'opts': [
        ['A', r"$\dfrac{12}{25}\vec a+\dfrac{9}{25}\vec b$"],
        ['B', r"$\dfrac{16}{25}\vec a+\dfrac{12}{25}\vec b$"],
        ['C', r"$\dfrac45\vec a+\dfrac35\vec b$"],
        ['D', r"$\dfrac35\vec a+\dfrac45\vec b$"],
    ],
    'answer': 'B',
    'analysis': (
        r"弦图中 $B$、$E$、$F$ 三点共线，且 $BE=q$、$BF=p$、$EF=p-q$（$p$、$q$ 为直角边），"
        r"由 $BE=3EF$ 得 $p=\dfrac43q$；再用 $\vec{BF}=\vec{BC}+\vec{CF}$、"
        r"$\vec{CF}=\dfrac qp\vec{EA}$、$\vec{EA}=\vec{EB}+\vec{BA}$ 自解出 $\vec{BF}$．"
    ),
    'solution': (
        r"设四个全等直角三角形的斜边（即大正方形边长）为 $c$，$AE=p$、$BE=q$，"
        r"则 $p^{2}+q^{2}=c^{2}$，小正方形边长 $EF=p-q$（设 $p>q$）．" "\n"
        r"**第一步：确定 $p:q$．** 由 $BE=3EF$ 得 $q=3(p-q)$，即 $4q=3p$，$p=\dfrac43q$．" "\n"
        r"**第二步：找出两条比例关系（弦图的关键结构）．**" "\n"
        r"（i）由四个三角形全等且绕中心旋转 $90^\circ$ 重合，有 $BF=AE=p$、$CF=BE=q$，"
        r"且 $\vec{EB}$ 与 $\vec{BF}$ 反向共线，故" "\n"
        r"$$\overrightarrow{EB}=-\frac qp\overrightarrow{BF}=-\frac34\overrightarrow{BF};$$" "\n"
        r"（ii）同理 $\vec{CF}\parallel\vec{EA}$ 且同向，$\left|\vec{CF}\right|:\left|\vec{EA}\right|=q:p$，即" "\n"
        r"$$\overrightarrow{CF}=\frac qp\overrightarrow{EA}=\frac34\overrightarrow{EA}.$$" "\n"
        r"**第三步：解出 $\vec{BF}$．**" "\n"
        r"$$\overrightarrow{BF}=\overrightarrow{BC}+\overrightarrow{CF}=\overrightarrow{BC}+\frac34\overrightarrow{EA}=\overrightarrow{BC}+\frac34\left(\overrightarrow{EB}+\overrightarrow{BA}\right)=\overrightarrow{BC}+\frac34\left(-\frac34\overrightarrow{BF}+\overrightarrow{BA}\right),$$" "\n"
        r"即 $\left(1+\dfrac9{16}\right)\overrightarrow{BF}=\overrightarrow{BC}+\dfrac34\overrightarrow{BA}$，" "\n"
        r"$$\overrightarrow{BF}=\frac{16}{25}\overrightarrow{BC}+\frac{12}{25}\overrightarrow{BA}=\frac{16}{25}\vec a+\frac{12}{25}\vec b.$$" "\n"
        r"故选 B．"
    ),
    'review': (
        r"① ⭐⭐ **本批最漂亮的一题**：$\vec{BF}$ 出现在等式两边，"
        r"「自己解自己」——这类「绕一圈回到自身」的方程在弦图、螺旋相似类题里反复出现 ✓✓" "\n"
        r"② 坐标化独立验证（$p=4,q=3,c=5$）：取 $B(0,0)$、$C(5,0)$、$A(0,5)$，则" "\n"
        r"   $E=\left(\dfrac{pq}c,\dfrac{q^{2}}c\right)=(2.4,1.8)$、$F=\left(\dfrac{p^{2}}c,\dfrac{pq}c\right)=(3.2,2.4)$；" "\n"
        r"   $BE=3$、$EF=1$ ⟹ $BE=3EF$ ✓；$\vec{EB}=(-2.4,-1.8)=-\dfrac34(3.2,2.4)=-\dfrac34\vec{BF}$ ✓；" "\n"
        r"   $\vec{CF}=(-1.8,2.4)=\dfrac34(-2.4,3.2)=\dfrac34\vec{EA}$ ✓；" "\n"
        r"   $\vec{BF}=\dfrac{3.2}5\vec{BC}+\dfrac{2.4}5\vec{BA}=0.64\vec a+0.48\vec b=\dfrac{16}{25}\vec a+\dfrac{12}{25}\vec b$ ✓✓✓" "\n"
        r"③ ⭐⭐ **可复用结论**：弦图里 $E=\left(\dfrac{pq}c,\dfrac{q^{2}}c\right)$、"
        r"$F=\left(\dfrac{p^{2}}c,\dfrac{pq}c\right)$（以 $B$ 为原点），**两坐标成比例 ⟹ $B,E,F$ 共线**，"
        r"且 $BE=q$、$BF=p$、$EF=p-q$，$BF=AE$、$CF=BE$" "\n"
        r"④ ⚠ **$p$、$q$ 的对应别弄反**：题给 $BE=3EF$，"
        r"若取 $q>p$ 则 $q=3(q-p)$ ⟹ $p=\dfrac23q$，此时 $\vec{BF}=\dfrac4{13}\vec a+\dfrac6{13}\vec b$（不在选项内）；" "\n"
        r"   由选项反推可知应取 $p>q$（即 $AE>BE$，$EF=AE-BE$）" "\n"
        r"⑤ 干扰项 C（$\dfrac45\vec a+\dfrac35\vec b$）是只取 $\dfrac{16}{25}\to\dfrac45$、"
        r"$\dfrac{12}{25}\to\dfrac35$ 的开方；A 项是 $\left(\dfrac45\right)^{2}$、$\left(\dfrac35\right)^{2}$ 型"
    ),
    'topics': ['M-T-232'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-232-E1',
}

T236_E1 = {
    'type': '选择',
    'stem_text': (
        r"在 $\triangle ABC$ 中，$\overrightarrow{BC}\cdot\overrightarrow{CA}=\overrightarrow{CA}\cdot\overrightarrow{AB}$，"
        r"$\left|\overrightarrow{BA}+\overrightarrow{BC}\right|=2$，且 $\dfrac\pi3\le B\le\dfrac{2\pi}3$，"
        r"则 $\overrightarrow{BA}\cdot\overrightarrow{BC}$ 的取值范围是（　　）"
    ),
    'opts': [
        ['A', r"$[-2,1)$"],
        ['B', r"$\left[\dfrac23,1\right)$"],
        ['C', r"$\left[-2,\dfrac23\right)$"],
        ['D', r"$\left[-2,\dfrac23\right]$"],
    ],
    'answer': 'D',
    'analysis': (
        r"移项得 $\vec{CA}\cdot(\vec{BC}+\vec{BA})=0$，即菱形 $BCDA$ 的对角线 $CA\perp BD$；"
        r"由 $\left|\vec{BA}+\vec{BC}\right|=|BD|=2$ 定出腰长，再把数量积写成 $\cos B$ 的一元函数．"
    ),
    'solution': (
        r"**第一步：识别图形．**" "\n"
        r"$$\overrightarrow{BC}\cdot\overrightarrow{CA}=\overrightarrow{CA}\cdot\overrightarrow{AB}\ \Longrightarrow\ \overrightarrow{CA}\cdot\left(\overrightarrow{BC}-\overrightarrow{AB}\right)=0\ \Longrightarrow\ \overrightarrow{CA}\cdot\left(\overrightarrow{BC}+\overrightarrow{BA}\right)=0.$$" "\n"
        r"以 $BC$、$BA$ 为邻边作平行四边形 $BCDA$，则 $\overrightarrow{BC}+\overrightarrow{BA}=\overrightarrow{BD}$，"
        r"故 $\vec{CA}\cdot\vec{BD}=0$，即两条对角线 $CA\perp BD$——**该平行四边形是菱形**．" "\n"
        r"设 $CA\cap BD=O$，则 $O$ 是 $BD$ 的中点，且菱形边长 $AB=BC=x$．" "\n"
        r"**第二步：用 $\left|\vec{BA}+\vec{BC}\right|=2$ 定 $x$．** 由上式 $\left|\vec{BD}\right|=2$，"
        r"故 $BO=1$．在 $\mathrm{Rt}\triangle BOA$ 中，菱形对角线平分顶角，$\angle ABO=\dfrac B2$，于是" "\n"
        r"$$\cos\frac B2=\frac{BO}{AB}=\frac1x\ \Longrightarrow\ x=\frac1{\cos\dfrac B2}.$$" "\n"
        r"**第三步：写成 $\cos B$ 的函数．**" "\n"
        r"$$y=\overrightarrow{BA}\cdot\overrightarrow{BC}=x^{2}\cos B=\frac{\cos B}{\cos^{2}\dfrac B2}=\frac{\cos B}{\dfrac{1+\cos B}2}=\frac{2\cos B}{1+\cos B}.$$" "\n"
        r"令 $t=\cos B$．由 $\dfrac\pi3\le B\le\dfrac{2\pi}3$ 得 $t\in\left[-\dfrac12,\dfrac12\right]$，且" "\n"
        r"$$y'=\frac{2}{(1+t)^{2}}>0,$$" "\n"
        r"故 $y=\dfrac{2t}{1+t}$ 在该区间上单调递增：" "\n"
        r"$$t=-\frac12\Rightarrow y=\frac{-1}{\frac12}=-2,\qquad "
        r"t=\frac12\Rightarrow y=\frac{1}{\frac32}=\frac23.$$" "\n"
        r"两端都能取到（$B=\dfrac{2\pi}3$ 与 $B=\dfrac\pi3$ 均在允许范围内），"
        r"故取值范围是 $\left[-2,\dfrac23\right]$．故选 D．"
    ),
    'review': (
        r"① ⭐⭐ **「$\vec{CA}\perp(\vec{BC}+\vec{BA})$ ⟹ 菱形」**：平行四边形对角线垂直即菱形，"
        r"这一步把三个条件压缩成一个几何对象，是本类题的标准入口 ✓✓" "\n"
        r"② 数值复核：$B=\dfrac\pi3$ 时 $\cos B=\dfrac12$，$y=\dfrac{1}{1.5}=0.666667=\dfrac23$ ✓；" "\n"
        r"   $B=\dfrac{2\pi}3$ 时 $\cos B=-\dfrac12$，$y=\dfrac{-1}{0.5}=-2$ ✓；"
        r"单调性由 $y'=\dfrac2{(1+t)^2}>0$ 保证 ✓✓" "\n"
        r"③ ⚠ **两端都是闭的**：$B$ 的取值范围是闭区间 $\left[\dfrac\pi3,\dfrac{2\pi}3\right]$，"
        r"且 $\cos\dfrac B2\in\left[\cos\dfrac\pi3,\cos\dfrac\pi6\right]=\left[\dfrac12,\dfrac{\sqrt3}2\right]\ne0$，"
        r"$x$ 有限，故 $-2$ 与 $\dfrac23$ 都能取到——**C 项（右端开）是本题唯一的陷阱** ✓" "\n"
        r"④ ⭐ **干扰项 A 的 $[-2,1)$**：上界 $1$ 来自 $\cos B\to1$（即 $B\to0$），"
        r"但题设 $B\ge\dfrac\pi3$，取不到；B 项则是只算了 $B\in\left[\dfrac\pi3,\dfrac\pi2\right]$ 的部分" "\n"
        r"⑤ ⚠ 原书 OCR 把选项 C、D 都提取成「$-2,\dfrac23$」，靠**闭区间判定**才能定 D"
    ),
    'topics': ['M-T-236'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-236-E1',
}

T238_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知向量 $\vec a$、$\vec b$ 的夹角为 $120^\circ$，且 $|\vec a|=2$、$|\vec b|=3$，"
        r"则向量 $2\vec a+3\vec b$ 在向量 $2\vec a+\vec b$ 方向上的投影为（　　）"
    ),
    'opts': [
        ['A', r"$\dfrac{8\sqrt3}{13}$"],
        ['B', r"$\dfrac{6\sqrt{13}}{13}$"],
        ['C', r"$\dfrac{5\sqrt6}{6}$"],
        ['D', r"$\dfrac{19\sqrt{13}}{13}$"],
    ],
    'answer': 'D',
    'analysis': (
        r"投影 $=\dfrac{(2\vec a+3\vec b)\cdot(2\vec a+\vec b)}{|2\vec a+\vec b|}$："
        r"先算 $\vec a\cdot\vec b=|\vec a||\vec b|\cos120^\circ=-3$，再展开两个模和一个数量积．"
    ),
    'solution': (
        r"由 $|\vec a|=2$、$|\vec b|=3$、夹角 $120^\circ$ 得" "\n"
        r"$$\vec a\cdot\vec b=2\times3\times\cos120^\circ=-3,\qquad "
        r"\vec a^{2}=4,\qquad \vec b^{2}=9.$$" "\n"
        r"分别求出所需的两个模与一个数量积：" "\n"
        r"$$|2\vec a+\vec b|^{2}=4\vec a^{2}+4\vec a\cdot\vec b+\vec b^{2}=16-12+9=13\ \Longrightarrow\ |2\vec a+\vec b|=\sqrt{13};$$" "\n"
        r"$$|2\vec a+3\vec b|^{2}=4\vec a^{2}+12\vec a\cdot\vec b+9\vec b^{2}=16-36+81=61\ \Longrightarrow\ |2\vec a+3\vec b|=\sqrt{61};$$" "\n"
        r"$$(2\vec a+3\vec b)\cdot(2\vec a+\vec b)=4\vec a^{2}+2\vec a\cdot\vec b+6\vec a\cdot\vec b+3\vec b^{2}=16+8(-3)+27=19.$$" "\n"
        r"故所求投影为" "\n"
        r"$$\frac{(2\vec a+3\vec b)\cdot(2\vec a+\vec b)}{|2\vec a+\vec b|}=\frac{19}{\sqrt{13}}=\frac{19\sqrt{13}}{13}.$$" "\n"
        r"故选 D．"
    ),
    'review': (
        r"① ⭐⭐ **投影公式的分母是「被投影的那个向量」的模** $|2\vec a+\vec b|$，"
        r"不是 $|2\vec a+3\vec b|$——这是投影题最高频的错 ✓" "\n"
        r"② 更快的算法：投影 $=\dfrac{(2\vec a+3\vec b)\cdot(2\vec a+\vec b)}{|2\vec a+\vec b|}$，"
        r"**分子一次展开即可，完全不必先算 $|2\vec a+3\vec b|=\sqrt{61}$**；" "\n"
        r"   原书先算 $\sqrt{61}$ 再乘 $\cos$ 是绕了远路（还多一次开方）" "\n"
        r"③ 数值复核：$\dfrac{19}{\sqrt{13}}=\dfrac{19}{3.605551}=5.269652$，"
        r"$\dfrac{19\sqrt{13}}{13}=\dfrac{68.466}{13}=5.269652$ ✓✓" "\n"
        r"④ ⚠ **交叉项系数别漏**：$(2\vec a+3\vec b)\cdot(2\vec a+\vec b)$ 展开有四项，"
        r"两个交叉项合并为 $8\vec a\cdot\vec b=-24$（若只算一次 $\vec a\cdot\vec b$ 得 $16-3+27=40$）" "\n"
        r"⑤ 干扰项 B（$\dfrac{6\sqrt{13}}{13}$）对应分子 $6$；C（$\dfrac{5\sqrt6}6$）与 A（$\dfrac{8\sqrt3}{13}$）"
        r"是分母取 $|2\vec a+3\vec b|$ 或分子算错的结果"
    ),
    'topics': ['M-T-238'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-238-V3',
}

T342_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知 $O$ 是 $\triangle ABC$ 所在平面内一点，以下说法正确的是（　　）"
    ),
    'opts': [
        ['A', r"若动点 $P$ 满足 $\overrightarrow{OP}=\overrightarrow{OA}+\lambda\left(\dfrac{|\overrightarrow{AB}|\cdot\overrightarrow{AB}}{\sin C}+\dfrac{|\overrightarrow{AC}|\cdot\overrightarrow{AC}}{\sin B}\right)$（$\lambda\in\mathbb R$），"
              r"则 $P$ 点的轨迹一定通过 $\triangle ABC$ 的重心．"],
        ['B', r"若点 $O$ 满足 $\dfrac{\overrightarrow{AO}\cdot\overrightarrow{AB}}{|\overrightarrow{AB}|}=\dfrac{\overrightarrow{AO}\cdot\overrightarrow{AC}}{|\overrightarrow{AC}|}$，"
              r"$\dfrac{\overrightarrow{CO}\cdot\overrightarrow{CA}}{|\overrightarrow{CA}|}=\dfrac{\overrightarrow{CO}\cdot\overrightarrow{CB}}{|\overrightarrow{CB}|}$，"
              r"则点 $O$ 是 $\triangle ABC$ 的垂心．"],
        ['C', r"若 $O$ 为 $\triangle ABC$ 的外心，且 $\overrightarrow{OA}+\overrightarrow{OB}+\overrightarrow{OC}=\overrightarrow{OM}$，则 $M$ 是 $\triangle ABC$ 的内心．"],
        ['D', r"若 $(\overrightarrow{OA}+\overrightarrow{OB})\cdot\overrightarrow{AB}=(\overrightarrow{OB}+\overrightarrow{OC})\cdot\overrightarrow{BC}=0$，"
              r"则点 $O$ 为 $\triangle ABC$ 的外心．"],
    ],
    'answer': 'AD',
    'analysis': (
        r"A：由正弦定理 $|\vec{AB}|/\sin C=|\vec{AC}|/\sin B=2R$，括号内正比于 $\vec{AB}+\vec{AC}=2\vec{AE}$（$\vec{AE}$ 为中线）；"
        r"B：单位向量之差垂直于内角平分线，故 $AO$ 是角平分线 ⟹ 内心；"
        r"C：$\vec{CM}=2\vec{OD}$ 且 $OD\perp AB$ ⟹ $CM\perp AB$ ⟹ 垂心；"
        r"D：展开得 $|\vec{OB}|^{2}-|\vec{OA}|^{2}=0$ ⟹ $OA=OB=OC$．"
    ),
    'solution': (
        r"**A 正确．** 设外接圆半径为 $R$，由正弦定理 $\dfrac{|\vec{AB}|}{\sin C}=\dfrac{|\vec{AC}|}{\sin B}=2R$．"
        r"设 $E$ 为 $BC$ 的中点，则 $\overrightarrow{AB}+\overrightarrow{AC}=2\overrightarrow{AE}$，于是" "\n"
        r"$$\overrightarrow{AP}=\lambda\cdot2R\left(\overrightarrow{AB}+\overrightarrow{AC}\right)=4\lambda R\,\overrightarrow{AE},$$" "\n"
        r"即 $\vec{AP}\parallel\vec{AE}$，$P$ 的轨迹是中线 $AE$ 所在的直线，必过重心．" "\n"
        r"**B 错误．** $\dfrac{\vec{AB}}{|\vec{AB}|}$、$\dfrac{\vec{AC}}{|\vec{AC}|}$ 是沿 $AB$、$AC$ 的单位向量，"
        r"而单位向量之和沿内角平分线、**之差垂直于内角平分线**（因 $(\vec u+\vec v)\cdot(\vec u-\vec v)=|\vec u|^{2}-|\vec v|^{2}=0$）．" "\n"
        r"由 $\vec{AO}\cdot\left(\dfrac{\vec{AB}}{|\vec{AB}|}-\dfrac{\vec{AC}}{|\vec{AC}|}\right)=0$ 知 $AO$ 平行于 $\angle CAB$ 的平分线；"
        r"同理 $CO$ 平分 $\angle BCA$．故 $O$ 是**内心**而非垂心．" "\n"
        r"**C 错误．** 设 $D$ 为 $AB$ 的中点，则 $\vec{OA}+\vec{OB}=2\vec{OD}$，故" "\n"
        r"$$\overrightarrow{CM}=\overrightarrow{OM}-\overrightarrow{OC}=\overrightarrow{OA}+\overrightarrow{OB}=2\overrightarrow{OD},$$" "\n"
        r"即 $CM\parallel OD$．$O$ 是外心 ⟹ $OD\perp AB$，故 $CM\perp AB$；同理 $BM\perp AC$．"
        r"所以 $M$ 是**垂心**而非内心．" "\n"
        r"**D 正确．**" "\n"
        r"$$(\overrightarrow{OA}+\overrightarrow{OB})\cdot\overrightarrow{AB}=(\overrightarrow{OA}+\overrightarrow{OB})\cdot(\overrightarrow{OB}-\overrightarrow{OA})=|\overrightarrow{OB}|^{2}-|\overrightarrow{OA}|^{2}=0\ \Longrightarrow\ OB=OA.$$" "\n"
        r"同理 $(\vec{OB}+\vec{OC})\cdot\vec{BC}=0$ 给出 $OB=OC$．故 $OA=OB=OC$，$O$ 为外心．" "\n"
        r"综上，选 AD．"
    ),
    'review': (
        r"① ⭐⭐ **四个选项覆盖了「四心」的四种向量刻画**，可当公式表背：" "\n"
        r"   · 重心：$\vec{AP}\parallel(\vec{AB}+\vec{AC})$，即中线方向；" "\n"
        r"   · 内心：$\vec{AO}\cdot\left(\dfrac{\vec{AB}}{|\vec{AB}|}-\dfrac{\vec{AC}}{|\vec{AC}|}\right)=0$，即沿角平分线；" "\n"
        r"   · 垂心：$\vec{OA}+\vec{OB}+\vec{OC}=\vec{OM}$ 时 $M$ 为垂心；" "\n"
        r"   · 外心：$(\vec{OA}+\vec{OB})\cdot\vec{AB}=0$，即到两端等距 ✓✓" "\n"
        r"② ⭐ **D 项的恒等式要记住**：$(\vec{OA}+\vec{OB})\cdot(\vec{OB}-\vec{OA})=|\vec{OB}|^{2}-|\vec{OA}|^{2}$，"
        r"「和向量 · 差向量 = 模方之差」，这是判断等距的最快写法" "\n"
        r"③ ⚠ **A 项里是 $|\vec{AB}|\cdot\vec{AB}$（带模长）不是 $\dfrac{\vec{AB}}{|\vec{AB}|}$**："
        r"正因为带了模长，才能用正弦定理约成同一个 $2R$，两项合并为中线；"
        r"若都改成单位向量，两项之和沿角平分线，结论就变成内心了" "\n"
        r"④ 数值复核：取 $A(0,0)$、$B(4,0)$、$C(1,3)$，外心 $O(2,0.667)$；"
        r"由 C 算得 $M=A+B+C-2O=(5,3)-(4,1.333)=(1,1.667)$，"
        r"$\vec{CM}=(0,-1.333)\perp\vec{AB}=(4,0)$ ✓ 确为垂线" "\n"
        r"⑤ ⚠ 原书在 p314（选题工具定位成 p207，已核对更正）"
    ),
    'topics': ['M-T-342'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-342-V3',
}

T237_V2 = {
    'type': '填空',
    'stem_text': (
        r"已知向量 $\vec a$、$\vec b$ 满足 $|\vec a|=1$，$\vec b=(2,1)$，"
        r"且 $\lambda\vec a+\vec b=\vec 0$（$\lambda<0$），则 $\left|\sqrt5\,\vec a+\vec b\right|=$ ____．"
    ),
    'answer': r"$2\sqrt5$",
    'analysis': (
        r"由 $\lambda\vec a=-\vec b$ 取模得 $|\lambda|=\dfrac{|\vec b|}{|\vec a|}=\sqrt5$，"
        r"结合 $\lambda<0$ 得 $\lambda=-\sqrt5$，于是 $\vec b=\sqrt5\,\vec a$．"
    ),
    'solution': (
        r"由 $\lambda\vec a+\vec b=\vec 0$ 得 $\lambda\vec a=-\vec b$，两边取模：" "\n"
        r"$$|\lambda|\cdot|\vec a|=|\vec b|\ \Longrightarrow\ |\lambda|=\frac{\sqrt{2^{2}+1^{2}}}{1}=\sqrt5.$$" "\n"
        r"又 $\lambda<0$，故 $\lambda=-\sqrt5$，代入 $\lambda\vec a+\vec b=\vec0$ 得 $\vec b=\sqrt5\,\vec a$．" "\n"
        r"于是" "\n"
        r"$$\left|\sqrt5\,\vec a+\vec b\right|=\left|\vec b+\vec b\right|=2|\vec b|=2\sqrt5.$$" "\n"
        r"故答案为 $2\sqrt5$．"
    ),
    'review': (
        r"① ⭐⭐ **「$\lambda\vec a+\vec b=\vec0$」的本质是 $\vec a\parallel\vec b$**："
        r"取模直接定 $|\lambda|$，符号由 $\lambda<0$ 定——**完全不需要设 $\vec a=(x,y)$ 解方程组** ✓✓" "\n"
        r"② 原书做法是设 $\vec a=(x,y)$ 联立 $x^{2}+y^{2}=1$、$\lambda x+2=0$、$\lambda y+1=0$，"
        r"算出 $\lambda^{2}=5$ 后再回代；取模法一步到位" "\n"
        r"③ 数值复核：$\vec b=(2,1)$、$|\vec b|=\sqrt5$，$\vec a=\dfrac{\vec b}{\sqrt5}=\left(\dfrac2{\sqrt5},\dfrac1{\sqrt5}\right)$，"
        r"$|\vec a|=1$ ✓；$\sqrt5\vec a+\vec b=(2,1)+(2,1)=(4,2)$，模 $=\sqrt{20}=2\sqrt5=4.4721$ ✓✓" "\n"
        r"④ ⚠ **$\lambda<0$ 不可省**：若 $\lambda=+\sqrt5$ 则 $\vec b=-\sqrt5\vec a$，"
        r"此时 $\sqrt5\vec a+\vec b=\vec0$，答案会是 $0$——符号决定一切"
    ),
    'topics': ['M-T-237'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-237-V2',
}

T220_V1 = {
    'type': '解答',
    'stem_text': (
        r"在 $\triangle ABC$ 中，三个内角 $A$、$B$、$C$ 的对边分别为 $a$、$b$、$c$，"
        r"且 $B=\dfrac{2\pi}3$，$b=\sqrt6$．" "\n"
        r"（1）若 $b=2\sqrt3\,c\cos C$，求 $C$；" "\n"
        r"（2）求 $\triangle ABC$ 的面积 $S$ 的取值范围．"
    ),
    'answer': r"（1）$C=\dfrac{\pi}{12}$；（2）$S\in\left(0,\dfrac{\sqrt3}{2}\right]$",
    'analysis': (
        r"（1）正弦定理把 $b=2\sqrt3c\cos C$ 化成 $\sin B=\sqrt3\sin2C$，代入 $B=\dfrac{2\pi}3$ 得 "
        r"$\sin2C=\dfrac12$，再用 $C\in\left(0,\dfrac\pi3\right)$ 取舍；" "\n"
        r"（2）余弦定理给出 $a^{2}+c^{2}+ac=6$，配 $a^{2}+c^{2}\ge2ac$ 得 $ac\le2$．"
    ),
    'solution': (
        r"**（1）** 由正弦定理，$b=2\sqrt3\,c\cos C$ 化为" "\n"
        r"$$\sin B=2\sqrt3\sin C\cos C=\sqrt3\sin2C.$$" "\n"
        r"又 $B=\dfrac{2\pi}3$，$\sin B=\dfrac{\sqrt3}2$，故 $\sqrt3\sin2C=\dfrac{\sqrt3}2$，即 $\sin2C=\dfrac12$．" "\n"
        r"由 $A+C=\pi-B=\dfrac\pi3$ 知 $C\in\left(0,\dfrac\pi3\right)$，故 $2C\in\left(0,\dfrac{2\pi}3\right)$，"
        r"在该区间内 $\sin2C=\dfrac12$ 只有一解 $2C=\dfrac\pi6$（另一解 $2C=\dfrac{5\pi}6>\dfrac{2\pi}3$，舍）" "\n"
        r"$$\therefore\ C=\frac\pi{12}.$$" "\n"
        r"**（2）方法一（余弦定理 + 基本不等式）** 由余弦定理" "\n"
        r"$$b^{2}=a^{2}+c^{2}-2ac\cos B=a^{2}+c^{2}+ac=6.$$" "\n"
        r"又 $a^{2}+c^{2}\ge2ac$，故 $6=a^{2}+c^{2}+ac\ge3ac$，即 $ac\le2$，"
        r"当且仅当 $a=c=\sqrt2$ 时取等号．于是" "\n"
        r"$$S=\frac12ac\sin B=\frac12ac\cdot\frac{\sqrt3}2=\frac{\sqrt3}4ac\le\frac{\sqrt3}4\times2=\frac{\sqrt3}2.$$" "\n"
        r"又 $a,c>0$ 时 $S>0$，且当 $A\to0$（即 $c\to0$）时 $S\to0$，故 $S\in\left(0,\dfrac{\sqrt3}2\right]$．" "\n"
        r"**方法二（正弦定理边化角）** 由 $\dfrac a{\sin A}=\dfrac c{\sin C}=\dfrac b{\sin B}=\dfrac{\sqrt6}{\sqrt3/2}=2\sqrt2$，得 $a=2\sqrt2\sin A$、$c=2\sqrt2\sin C$，于是" "\n"
        r"$$S=\frac12ac\sin B=\frac12\cdot2\sqrt2\sin A\cdot2\sqrt2\sin C\cdot\frac{\sqrt3}2=2\sqrt3\sin A\sin\left(\frac\pi3-A\right)$$" "\n"
        r"$$=2\sqrt3\sin A\left(\frac{\sqrt3}2\cos A-\frac12\sin A\right)=3\sin A\cos A-\sqrt3\sin^{2}A=\frac32\sin2A-\frac{\sqrt3}2(1-\cos2A)=\sqrt3\sin\left(2A+\frac\pi6\right)-\frac{\sqrt3}2.$$" "\n"
        r"由 $A\in\left(0,\dfrac\pi3\right)$ 得 $2A+\dfrac\pi6\in\left(\dfrac\pi6,\dfrac{5\pi}6\right)$，"
        r"$\sin\left(2A+\dfrac\pi6\right)\in\left(\dfrac12,1\right]$，故 $S\in\left(0,\dfrac{\sqrt3}2\right]$．"
    ),
    'review': (
        r"① ⭐⭐ **（1）与（2）是同一条件的两种用法**：（1）把 $b$ 用 $c$、$C$ 表示求角，"
        r"（2）把 $b$ 当定值求面积范围；注意（1）的结论 $C=\dfrac\pi{12}$ 与 $b=\sqrt6$ 完全自洽：" "\n"
        r"   由正弦定理 $c=\dfrac{b\sin C}{\sin B}=\dfrac{\sqrt6\sin15^\circ}{\sqrt3/2}=0.732$，"
        r"而 $2\sqrt3c\cos C=2\sqrt3\times0.732\times0.966=2.449=\sqrt6=b$ ✓✓" "\n"
        r"② 数值复核（2）：取 $a=c=\sqrt2$，则 $a^{2}+c^{2}+ac=2+2+2=6=b^{2}$ ✓，"
        r"$S=\dfrac{\sqrt3}4\times2=\dfrac{\sqrt3}2=0.866$ ✓；取 $A\to0$ 时 $S\to0$ ✓" "\n"
        r"③ ⭐ **两种方法的分工**：方法一（余弦 + 均值）只需三步，适合选择填空；"
        r"方法二（边化角）能给出 $S$ 随 $A$ 的完整变化，适合解答题写" "\n"
        r"④ ⚠ **$S$ 的下界是开的**：$ac>0$ 但可任意接近 $0$，故写 $(0,\dfrac{\sqrt3}2]$ 不能写成 $[0,\cdot]$ ✓" "\n"
        r"⑤ ⚠ 方法二中 $2A+\dfrac\pi6\in\left(\dfrac\pi6,\dfrac{5\pi}6\right)$ 的 $\sin$ 值域是 $\left(\dfrac12,1\right]$，"
        r"代入得 $S\in\left(\sqrt3\cdot\dfrac12-\dfrac{\sqrt3}2,\ \sqrt3-\dfrac{\sqrt3}2\right]=\left(0,\dfrac{\sqrt3}2\right]$ ✓"
    ),
    'topics': ['M-T-220'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-220-V1',
}

T227_V3 = {
    'type': '解答',
    'stem_text': (
        r"如图，在平面四边形 $ABCD$ 中，已知 $\angle A=\dfrac\pi2$，$\angle B=\dfrac{2\pi}3$，$AB=6$，"
        r"点 $E$ 在 $AB$ 上且 $AE=2BE$，$\angle CED=\dfrac{2\pi}3$，$EC=\sqrt7$．" "\n"
        r"（1）求 $\sin\angle BCE$ 的值；" "\n"
        r"（2）求 $\triangle CED$ 的周长．"
    ),
    'answer': r"（1）$\dfrac{\sqrt{21}}{7}$；（2）$7+3\sqrt7$",
    'analysis': (
        r"（1）在 $\triangle BCE$ 中用正弦定理；（2）由 $\angle B=\angle CED=\dfrac{2\pi}3$ "
        r"且 $A,E,B$ 共线得 $\angle DEA=\angle BCE$，于是 $\triangle AED$ 中可求 $ED$，"
        r"再用余弦定理求 $CD$．"
    ),
    'solution': (
        r"由 $AB=6$、$AE=2BE$ 得 $AE=4$、$BE=2$．" "\n"
        r"**（1）** 在 $\triangle BCE$ 中，$\angle B=\dfrac{2\pi}3$，$BE=2$，$CE=\sqrt7$，由正弦定理" "\n"
        r"$$\frac{BE}{\sin\angle BCE}=\frac{CE}{\sin B}\ \Longrightarrow\ "
        r"\sin\angle BCE=\frac{BE\cdot\sin B}{CE}=\frac{2\times\dfrac{\sqrt3}2}{\sqrt7}=\frac{\sqrt3}{\sqrt7}=\frac{\sqrt{21}}7.$$" "\n"
        r"**（2）第一步：证 $\angle DEA=\angle BCE$．** 因 $A$、$E$、$B$ 共线，" "\n"
        r"$$\angle DEA+\angle DEC+\angle CEB=\pi\ \Longrightarrow\ \angle DEA+\angle CEB=\pi-\frac{2\pi}3=\frac\pi3;$$" "\n"
        r"而在 $\triangle BCE$ 中 $\angle BCE+\angle CEB=\pi-\dfrac{2\pi}3=\dfrac\pi3$，故" "\n"
        r"$$\angle DEA=\angle BCE,\qquad \cos\angle DEA=\sqrt{1-\sin^{2}\angle BCE}=\sqrt{1-\frac{21}{49}}=\sqrt{\frac{28}{49}}=\frac{2\sqrt7}7.$$" "\n"
        r"**第二步：求 $ED$．** 在 $\mathrm{Rt}\triangle AED$ 中 $\angle A=\dfrac\pi2$、$AE=4$，故" "\n"
        r"$$\cos\angle DEA=\frac{AE}{ED}\ \Longrightarrow\ ED=\frac{4}{\dfrac{2\sqrt7}7}=\frac{28}{2\sqrt7}=2\sqrt7.$$" "\n"
        r"**第三步：求 $CD$．** 在 $\triangle CED$ 中，由余弦定理" "\n"
        r"$$CD^{2}=CE^{2}+DE^{2}-2\cdot CE\cdot DE\cos\angle CED=7+28-2\times\sqrt7\times2\sqrt7\times\left(-\frac12\right)=35+14=49,$$" "\n"
        r"故 $CD=7$，$\triangle CED$ 的周长为" "\n"
        r"$$CE+DE+CD=\sqrt7+2\sqrt7+7=7+3\sqrt7.$$"
    ),
    'review': (
        r"① ⭐⭐ **题眼是「$\angle B=\angle CED$」**：两个相等的角分布在两个三角形里，"
        r"配上 $A,E,B$ 共线，就能把 $\angle DEA$ 与 $\angle BCE$ 拉到一起——"
        r"这是四边形中「等角转移」的标准套路 ✓✓" "\n"
        r"② 数值复核：$CE=\sqrt7=2.6458$、$DE=2\sqrt7=5.2915$、$CD=7$，"
        r"$\cos\angle CED=\dfrac{7+28-49}{2\times2.6458\times5.2915}=\dfrac{-14}{28}=-0.5$ ✓ 即 $120^\circ$ ✓；" "\n"
        r"   周长 $=2.6458+5.2915+7=14.9373=7+3\sqrt7$ ✓✓" "\n"
        r"③ ⭐ **$\cos\angle DEA=\dfrac{AE}{ED}$ 用的是直角三角形中「邻边/斜边」**，"
        r"比用正弦定理快；$\angle A=\dfrac\pi2$ 这个条件只在这里用上" "\n"
        r"④ ⚠ **$\angle DEA$ 与 $\angle BCE$ 相等不是互补**：两者都是锐角"
        r"（$\sin\angle BCE=\dfrac{\sqrt{21}}7\approx0.655$ ⟹ 约 $40.9^\circ<\dfrac\pi3$ ✓），"
        r"取正号 $\cos=\dfrac{2\sqrt7}7$ 正确" "\n"
        r"⑤ ⚠ 题干里 $AE=2BE$（**不是** $BE=2AE$）：前者给 $AE=4$、$BE=2$，"
        r"后者会给 $BE=4$、$AE=2$，$\sin\angle BCE$ 变 $\dfrac{2\sqrt{21}}7>1$，无解 ✓ 可反推"
    ),
    'topics': ['M-T-227'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-227-V3',
}

QS = [
    T199_E1,
    T199_V3,
    T201_E1,
    T233_E1,
    T203_V2,
    T232_V3,
    T233_V2,
    T207_V3,
    T232_E1,
    T236_E1,
    T238_V3,
    T342_V3,
    T237_V2,
    T220_V1,
    T227_V3,
]
