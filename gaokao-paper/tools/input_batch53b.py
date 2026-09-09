# -*- coding: utf-8 -*-
r"""第53批（二）：解三角形 · 中线问题（3 题全录） 来源：2024高中数学热点题型归纳完整解析版.pdf p163（PDF 页 162）M-T-201 ## ★★ 原书「提分秘籍」三条（本批的核心） > 1. 中线可分三角形得两个三角形，**分别运用余弦定理** > 2. 中线可**延伸补形得平行四边形** > 3. （隐含）**重心**把中线分成 $2:1$ | 题 | 用哪条 | 关键 | |---|---|---| | V1 | 重心 + 余弦定理 | $CD\perp BE$ ⟹ $G$ 是重心 ⟹ $FG=\frac12BC$、$AG=\frac23AF$ ⟹ $b^2+c^2=5a^2$ | | V2 | 分别用余弦定理/面积 | $AD$ 是中线，$CE\perp AD$ ⟹ 面积法求 $CE$、$DE$，再解直角三角 | | V3 | 重心 $2:1$ + 余弦定理 | $OC=3OB$ 与重心比例 $OC:OB=2\sqrt3:2$ 联立 | ## 三题验算（全部独立推导，与答案吻合） | 题 | 我的结果 | 答案 | |---|---|---| | V1 | $\cos A\in\left[\frac45,\frac{\sqrt6}3\right)$ | **D** | | V2 | $CF=\frac{\sqrt5}3$ | **D** | | V3 | $S_{\max}=6\sqrt3$ | **C** | ## ⚠ 共同陷阱 **中线长与三角形存在性**：V1 用锐角三角形条件夹 $b/c$ 的范围； V3 用二次函数取最大后要检验 $t$ 是否可取。**别忘检验。** """

T201_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知 $\triangle ABC$ 为锐角三角形，$D,E$ 分别为 $AB,AC$ 的中点，且 $CD\perp BE$，"
        r"则 $\cos A$ 的取值范围是（　　）"
    ),
    'opts': [
        ('A', r"$\left(\dfrac12,\ 1\right)$"),
        ('B', r"$\left(\dfrac{\sqrt2}2,\ \dfrac{\sqrt6}3\right)$"),
        ('C', r"$\left[\dfrac45,\ 1\right)$"),
        ('D', r"$\left[\dfrac45,\ \dfrac{\sqrt6}3\right)$"),
    ],
    'answer': 'D',
    'analysis': (
        r"$CD,BE$ 是两条中线，交点 $G$ 是**重心**。由 $CD\perp BE$ 得直角三角形，"
        r"结合重心性质（$FG=\frac12BC$、$AG=\frac23AF$）在 $\triangle ABF$、$\triangle ACF$ 中分别用余弦定理，"
        r"两式**相加**（$\cos\angle AFB+\cos\angle AFC=0$）得 $b^{2}+c^{2}=5a^{2}$，再用锐角条件夹范围。"
    ),
    'solution': (
        r"**第一步：识别重心**" "\n"
        r"$CD$、$BE$ 是中线，交于重心 $G$。连 $AG$ 延长交 $BC$ 于 $F$，则 $F$ 为 $BC$ 中点。" "\n"
        r"由 $CD\perp BE$ 知 $\triangle BGC$ 在 $G$ 处直角，而 $F$ 是斜边 $BC$ 的中点：" "\n"
        r"$FG=\dfrac12BC=\dfrac a2$，且 $AG=\dfrac23AF$、$GF=\dfrac13AF$ ⟹ $GF=\dfrac a2$ ⟹ $AF=\dfrac{3a}2$．" "\n"
        r"（同时 $AG=\frac23\cdot\frac{3a}2=a$。）" "\n"
        r"**第二步：两个余弦定理相加**" "\n"
        r"在 $\triangle ABF$ 中：$c^{2}=AF^{2}+BF^{2}-2\,AF\cdot BF\cos\angle AFB=\dfrac{9a^{2}}4+\dfrac{a^{2}}4-2\cdot\dfrac{3a}2\cdot\dfrac a2\cos\angle AFB$．" "\n"
        r"在 $\triangle ACF$ 中：$b^{2}=\dfrac{9a^{2}}4+\dfrac{a^{2}}4-2\cdot\dfrac{3a}2\cdot\dfrac a2\cos\angle AFC$．" "\n"
        r"因 $\angle AFB+\angle AFC=\pi$，$\cos\angle AFC=-\cos\angle AFB$，两式相加：" "\n"
        r"$b^{2}+c^{2}=2\cdot\dfrac{10a^{2}}4=5a^{2}$．" "\n"
        r"**第三步：锐角条件夹 $b/c$**" "\n"
        r"锐角三角形 ⟹ $a^{2}+b^{2}>c^{2}$、$b^{2}+c^{2}>a^{2}$、$c^{2}+a^{2}>b^{2}$，代入 $b^{2}+c^{2}=5a^{2}$：" "\n"
        r"得 $3b^{2}>2c^{2}$ 且 $3c^{2}>2b^{2}$，即 $\dfrac23<\dfrac{b^{2}}{c^{2}}<\dfrac32$，故 $\sqrt{\dfrac23}<\dfrac bc<\sqrt{\dfrac32}$．" "\n"
        r"**第四步：$\cos A$ 的表达式**" "\n"
        r"$\cos A=\dfrac{b^{2}+c^{2}-a^{2}}{2bc}=\dfrac{b^{2}+c^{2}-\frac{b^{2}+c^{2}}5}{2bc}=\dfrac{4(b^{2}+c^{2})}{10bc}=\dfrac25\left(\dfrac bc+\dfrac cb\right)$．" "\n"
        r"令 $t=\dfrac bc\in\left(\sqrt{\dfrac23},\sqrt{\dfrac32}\right)$，则 $f(t)=t+\dfrac1t$ 在 $t<1$ 递减、$t>1$ 递增，" "\n"
        r"$f\left(\sqrt{\dfrac23}\right)=f\left(\sqrt{\dfrac32}\right)=\sqrt{\dfrac23}+\sqrt{\dfrac32}=\dfrac{\sqrt6}3+\dfrac{\sqrt6}2=\dfrac{5\sqrt6}6$．" "\n"
        r"$\cos A\in\left[\dfrac25\cdot2,\ \dfrac25\cdot\dfrac{5\sqrt6}6\right)=\left[\dfrac45,\ \dfrac{\sqrt6}3\right)$．选 D．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓，由详解「设 $CD,BE$ 交于点 $G$，连接 $AG$，延长交 $BC$ 于 $F$，" "\n"
        r"则 $F$ 为 $BC$ 的中点，由 $CD\perp BE$，可得 $FG=\frac12BC=\frac a2,AG=\frac{2a}3\cdot\frac32=a,AF=\frac{3a}2$…" "\n"
        r"因为 $\angle AFC+\angle AFB=\pi$，所以上面两式相加，得 $c^{2}+b^{2}=5a^{2}$，因为 $\triangle ABC$ 为锐角三角形，" "\n"
        r"可得 $a^{2}+b^{2}>c^{2},b^{2}+c^{2}>a^{2},c^{2}+a^{2}>b^{2}$，可得 $3b^{2}>2c^{2},3c^{2}>2b^{2}$，" "\n"
        r"则 $\frac23<\frac{b^{2}}{c^{2}}<\frac32$…设 $\frac bc=t$…则 $f(t)=t+\frac1t$ 在 $(\frac{\sqrt6}3,1)$ 递减，在 $(1,\frac{\sqrt6}2)$ 递增，" "\n"
        r"因为 $f(\frac{\sqrt6}3)=f(\frac{\sqrt6}2)=\frac{5\sqrt6}6$，则 $\frac45\le\cos A<\frac{\sqrt6}3$，故选 D」还原，" "\n"
        r"**与我的推导一致** ✓。" "\n"
        r"**独立验算**：" "\n"
        r"① **重心比例**：$AG:GF=2:1$，且 $\triangle BGC$ 直角（$G$ 处）、$F$ 是 $BC$ 中点 ⟹ $GF=\frac{BC}2=\frac a2$ ✓" "\n"
        r"$AF=AG+GF=3\cdot\frac a2=\frac{3a}2$ ✓；$AG=2\cdot\frac a2=a$ ✓" "\n"
        r"② **两式相加**：$\frac{9a^2}4+\frac{a^2}4=\frac{10a^2}4=\frac{5a^2}2$，两倍 $=\frac{5a^2}\cdot\frac{2}{2}$…" "\n"
        r"$\frac{5a^2}2\times2=5a^2$ ✓✓" "\n"
        r"③ **$\cos A$ 化简**：$\frac{b^2+c^2-a^2}{2bc}$，$a^2=\frac{b^2+c^2}5$ ⟹ 分子 $=\frac{4(b^2+c^2)}5$ ⟹ $\cos A=\frac{4(b^2+c^2)}{10bc}=\frac25(\frac bc+\frac cb)$ ✓✓" "\n"
        r"④ **端点**：$t=1$ 时 $\cos A=\frac25(2)=\frac45=0.8$ ✓（可取，因 $b=c$ 在范围内）" "\n"
        r"$t=\sqrt{\frac23}=0.8165$ 或 $t=\sqrt{\frac32}=1.2247$：$\cos A=\frac25(0.8165+1.2247)=\frac25(2.0412)=0.8165=\frac{\sqrt6}3$ ✓✓" "\n"
        r"（$\frac{\sqrt6}3=\frac{2.449}3=0.8165$ ✓）" "\n"
        r"⑤ **开闭判断**：下界 $\frac45$ 在 $b=c$ 时取到 ✓ **闭**；上界对应直角三角形（$3b^2=2c^2$ 时 $a^2+b^2=c^2$）⟹ 不是锐角 ⟹ **开** ✓" "\n"
        r"⑥ **取中点验证**：取 $b=c=1$，则 $a^2=\frac{2}5=0.4$、$a=0.6325$" "\n"
        r"验锐角：$a^2+b^2=1.4>1=c^2$ ✓；$b^2+c^2=2>0.4$ ✓；$c^2+a^2=1.4>1$ ✓ **确为锐角**" "\n"
        r"$\cos A=\frac{1+1-0.4}{2}=\frac{1.6}{2}=0.8=\frac45$ ✓✓✓" "\n"
        r"**答案 D（$[\frac45,\frac{\sqrt6}3)$）正确** ✓" "\n"
        r"**⭐ 通法（两中线垂直）**：" "\n"
        r"① 两中线交点即**重心**，**延长补形**：连 $AG$ 交 $BC$ 于中点 $F$；" "\n"
        r"② 若两中线**垂直**，则 $\triangle BGC$ 在 $G$ 处直角，$F$（斜边中点）给出 $GF=\frac a2$ —— " "\n"
        r"这是把「垂直」转成「长度」的关键一步；" "\n"
        r"③ 在 $\triangle ABF$、$\triangle ACF$ 中分别用余弦定理后**相加**，" "\n"
        r"交叉项因 $\cos\angle AFB+\cos\angle AFC=0$ 而抵消 —— **「相加」是这类题的标准动作**；" "\n"
        r"④ ⚠ **锐角三角形**要列三个不等式 $a^2+b^2>c^2$ 等，别只列一个。"
    ),
    'difficulty': 0.94,
    'topics': ['M-T-201'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-201-V1',
}

T201_V2 = {
    'type': '选择',
    'stem_text': (
        r"如图，在 $\triangle ABC$ 中，$\angle ACB=90^\circ$，$AC=BC$，$AD$ 为中线，"
        r"过点 $C$ 作 $CE\perp AD$ 于点 $E$，延长 $CE$ 交 $AB$ 于点 $F$，若 $AC=1$，则 $CF$ 的值为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac34$"),
        ('B', r"$\dfrac{\sqrt3}2$"),
        ('C', r"$\dfrac23$"),
        ('D', r"$\dfrac{\sqrt5}3$"),
    ],
    'answer': 'D',
    'analysis': (
        r"等腰直角三角形 + 中线 ⟹ 先求 $AD,CD$；由 $CE\perp AD$ 用**面积法**求 $CE$、再由勾股求 $DE$；"
        r"最后过 $F$ 作 $FH\perp CB$，用 $\tan\angle FCB=\frac{DE}{CE}$ 定出 $F$ 的位置。"
    ),
    'solution': (
        r"**第一步：基本量**" "\n"
        r"$\angle ACB=90^\circ$、$AC=BC$，由 $AC=1$ 得 $BC=1$，$AB=\sqrt2$．" "\n"
        r"$AD$ 是 $BC$ 上的中线 ⟹ $CD=BD=\dfrac12$．" "\n"
        r"$AD=\sqrt{AC^{2}+CD^{2}}=\sqrt{1+\dfrac14}=\dfrac{\sqrt5}2$．" "\n"
        r"**第二步：面积法求 $CE$**" "\n"
        r"在 $\triangle ACD$ 中，$CE\perp AD$ ⟹ $\angle CED=90^\circ$，由面积相等：" "\n"
        r"$\dfrac12 AD\cdot CE=\dfrac12 AC\cdot CD\Rightarrow CE=\dfrac{AC\cdot CD}{AD}=\dfrac{1\cdot\frac12}{\frac{\sqrt5}2}=\dfrac1{\sqrt5}=\dfrac{\sqrt5}5$．" "\n"
        r"$DE=\sqrt{CD^{2}-CE^{2}}=\sqrt{\dfrac14-\dfrac15}=\sqrt{\dfrac1{20}}=\dfrac{\sqrt5}{10}$．" "\n"
        r"**第三步：定 $F$ 的位置**" "\n"
        r"过 $F$ 作 $FH\perp CB$ 于 $H$，则 $\angle FHB=90^\circ$．" "\n"
        r"由 $F$ 在 $CE$ 的延长线上，$\angle FCH$ 即 $\angle ECB$ 方向，" "\n"
        r"$\tan\angle FCB=\dfrac{DE}{CE}=\dfrac{\frac{\sqrt5}{10}}{\frac{\sqrt5}5}=\dfrac12$．" "\n"
        r"设 $FH=HB=x$（因 $\angle FCB$ 的对边 $FH$、邻边 $CH$，且 $\triangle ABC$ 中 $\angle B=45^\circ$ ⟹ $\mathrm{Rt}\triangle FHB$ 等腰），" "\n"
        r"则 $CH=1-x$。由 $\tan\angle FCB=\dfrac{FH}{CH}=\dfrac x{1-x}=\dfrac12$ 得 $2x=1-x$ ⟹ $x=\dfrac13$．" "\n"
        r"**第四步：求 $CF$**" "\n"
        r"$CF=\sqrt{CH^{2}+FH^{2}}=\sqrt{\left(1-\dfrac13\right)^{2}+\left(\dfrac13\right)^{2}} =\sqrt{\dfrac49+\dfrac19}=\dfrac{\sqrt5}3$．选 D．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓，由详解「因为 $\angle ACB=90^\circ$，$AC=BC$，所以 $\triangle ABC$ 为等腰直角三角形，" "\n"
        r"又因为 $AC=1$，$AD$ 为中线，所以 $BC=1$，$CD=BD=\frac12$，所以 $AD=\sqrt{AC^{2}+CD^{2}}=\frac{\sqrt5}2$。" "\n"
        r"因为 $CE\perp AD$，所以 $\angle CED=90^\circ$，所以 $AD\cdot CE=AC\cdot CD$，即 $CE=\frac{1\times\frac12}{\frac{\sqrt5}2}=\frac{\sqrt5}5$，" "\n"
        r"所以 $DE=\sqrt{CD^{2}-CE^{2}}=\frac{\sqrt5}{10}$。过点 $F$ 作 $FH\perp CB$ 交 $CB$ 于点 $H$…" "\n"
        r"所以 $\tan\angle FCB=\frac{DE}{CE}=\frac{\frac{\sqrt5}{10}}{\frac{\sqrt5}5}=\frac12$，设 $FH=HB=x$，则 $CH=1-x$，" "\n"
        r"所以 $\frac{x}{1-x}=\frac12$，解得 $x=\frac13$…" "\n"
        r"所以 $CF=\sqrt{CH^{2}+FH^{2}}=\sqrt{(1-\frac13)^{2}+(\frac13)^{2}}=\frac{\sqrt5}3$。故选 D」还原，" "\n"
        r"**与我的推导一致** ✓。" "\n"
        r"**独立验算**：" "\n"
        r"① **$AD$**：$\sqrt{1+\frac14}=\sqrt{1.25}=1.1180$；$\frac{\sqrt5}2=\frac{2.2361}2=1.1180$ ✓✓" "\n"
        r"② **$CE$**：面积法 $\frac12(1.1180)CE=\frac12(1)(0.5)$ ⟹ $CE=\frac{0.5}{1.118}=0.4472=\frac{\sqrt5}5$ ✓✓" "\n"
        r"③ **$DE$**：$\sqrt{0.25-0.2}=\sqrt{0.05}=0.2236$；$\frac{\sqrt5}{10}=\frac{2.2361}{10}=0.2236$ ✓✓" "\n"
        r"④ **$\tan\angle FCB$**：$\frac{0.2236}{0.4472}=0.5$ ✓✓" "\n"
        r"⑤ **$x=\frac13$**：$\frac{1/3}{2/3}=0.5$ ✓✓" "\n"
        r"⑥ **$CF$**：$\sqrt{(\frac23)^2+(\frac13)^2}=\sqrt{\frac49+\frac19}=\sqrt{\frac59}=\frac{\sqrt5}3=\frac{2.2361}3=0.7454$ ✓✓✓" "\n"
        r"⑦ **坐标法交叉验证**：设 $C(0,0)$、$A(1,0)$…" "\n"
        r"实际取 $C(0,0)$、$B(1,0)$、$A(0,1)$（$\angle C=90^\circ$、$AC=BC=1$）" "\n"
        r"$D$ 是 $BC$ 中点 ⟹ $D(0.5,0)$；$AD$ 方向 $(-0.5,1)$，长度 $\sqrt{1.25}=1.1180$ ✓" "\n"
        r"$E$ 是 $C$ 到 $AD$ 的垂足：由 $CE=\frac{\sqrt5}5=0.4472$ 沿垂直 $AD$ 方向 $(1,0.5)/\sqrt{1.25}$" "\n"
        r"$E=C+0.4472\cdot\frac{(1,0.5)}{1.118}=(0.4,0.2)$" "\n"
        r"验 $E$ 在 $AD$ 上：$AD$ 线 $A(0,1)\to D(0.5,0)$，参数式 $(0.5t,1-t)$；取 $t=0.8$ ⟹ $(0.4,0.2)$ ✓✓" "\n"
        r"验 $CE\perp AD$：$\vec{CE}=(0.4,0.2)$、$\vec{AD}=(0.5,-1)$，点积 $=0.2-0.2=0$ ✓✓✓" "\n"
        r"$F$ 在射线 $CE$ 上且在 $AB$ 上：$AB$ 线 $x+y=1$；射线 $C+k(0.4,0.2)$ 代入：$0.4k+0.2k=1$ ⟹ $k=\frac{1}{0.6}=1.6667$" "\n"
        r"$F=(0.6667,0.3333)$；$CF=\sqrt{0.4444+0.1111}=\sqrt{0.5556}=0.7454$ ✓✓✓ **$=\frac{\sqrt5}3$**" "\n"
        r"**答案 D（$\frac{\sqrt5}3$）正确** ✓" "\n"
        r"**⭐ 通法（直角三角形中的垂线连锁）**：" "\n"
        r"① **面积法求高**最快：$AD\cdot CE=AC\cdot CD$（同一个 $\triangle ACD$ 的两种面积算法）；" "\n"
        r"② 由高再用**勾股**求投影段 $DE$；" "\n"
        r"③ $\frac{DE}{CE}$ 给出角度的正切 —— 这是把「位置」转成「比例」的桥梁；" "\n"
        r"④ 设 $FH=HB=x$ 是利用 $\angle B=45^\circ$ 的等腰性质，" "\n"
        r"**这类题坐标法也能解**（我做了交叉验证），但面积法更快。" "\n"
        r"**⚠ 易错**：$CE$ 是 $C$ 到 $AD$ 的高，不是到 $AB$ 的高，别搞混参照线。"
    ),
    'difficulty': 0.93,
    'topics': ['M-T-201'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-201-V2',
}

T201_V3 = {
    'type': '选择',
    'stem_text': (
        r"在 $\triangle ABC$ 中，$AB=2$，$D,E$ 分别是边 $AB,AC$ 的中点，$CD$ 与 $BE$ 交于点 $O$，"
        r"若 $OC=\sqrt3\,OB$，则 $\triangle ABC$ 面积的最大值为（　　）"
    ),
    'opts': [
        ('A', r"$\sqrt3$"),
        ('B', r"$3\sqrt3$"),
        ('C', r"$6\sqrt3$"),
        ('D', r"$9\sqrt3$"),
    ],
    'answer': 'C',
    'analysis': (
        r"$CD,BE$ 是中线 ⟹ $O$ 是重心 ⟹ $\frac{BO}{OE}=\frac{CO}{OD}=2$；"
        r"$D,E$ 是中点 ⟹ $DE\parallel BC$ 且 $\frac{DO}{OC}=\frac12$。"
        r"由 $OC=\sqrt3\,OB$ 与这两个比例联立，可把 $OB,OD,OC$ 都表成一个参数 $t$，"
        r"再在 $\triangle DBO$ 中用余弦定理把 $\cos\angle ABO$ 表成 $t$ 的函数，面积转二次函数。"
    ),
    'solution': (
        r"**第一步：重心与中位线的比例**" "\n"
        r"$D,E$ 是 $AB,AC$ 中点 ⟹ $DE\parallel BC$、$DE=\dfrac12BC$，" "\n"
        r"故 $\triangle ODE\sim\triangle OCB$，$\dfrac{DO}{OC}=\dfrac{OE}{OB}=\dfrac{DE}{BC}=\dfrac12$．" "\n"
        r"又 $O$ 是重心 ⟹ $\dfrac{BO}{OE}=2$、$\dfrac{CO}{OD}=2$（与上式一致）．" "\n"
        r"**第二步：设参数**" "\n"
        r"设 $OE=t>0$，则 $OB=2t$；由 $\frac{DO}{OC}=\frac12$ 且 $OC=\sqrt3\,OB=2\sqrt3 t$ ⟹ $DO=\sqrt3 t$．" "\n"
        r"（检验 $OC:OD=2\sqrt3t:\sqrt3 t=2:1$ ✓ 符合重心性质。）" "\n"
        r"**第三步：在 $\triangle DBO$ 中用余弦定理**" "\n"
        r"$AB=2$、$D$ 是中点 ⟹ $DB=1$．设 $\angle ABO=\alpha$：" "\n"
        r"$\cos\alpha=\dfrac{DB^{2}+OB^{2}-DO^{2}}{2\cdot DB\cdot OB}=\dfrac{1+4t^{2}-3t^{2}}{2\cdot1\cdot2t}=\dfrac{t^{2}+1}{4t}$．" "\n"
        r"$\sin\alpha=\sqrt{1-\cos^{2}\alpha}=\sqrt{1-\dfrac{(t^{2}+1)^{2}}{16t^{2}}}=\dfrac{\sqrt{-t^{4}+14t^{2}-1}}{4t}$．" "\n"
        r"**第四步：面积转二次函数**" "\n"
        r"$O$ 是重心 ⟹ $S_{\triangle ABE}=3S_{\triangle ABO}\cdot\frac{1}{?}$…直接用中线的面积性质：" "\n"
        r"$E$ 是 $AC$ 中点 ⟹ $S_{\triangle ABE}=\dfrac12S_{\triangle ABC}$，故 $S_{\triangle ABC}=2S_{\triangle ABE}$．" "\n"
        r"$S_{\triangle ABC}=2\cdot\dfrac12\cdot AB\cdot BE\cdot\sin\angle ABE$，其中 $BE=BO+OE=3t$、$\angle ABE=\alpha$：" "\n"
        r"$S_{\triangle ABC}=2\cdot\dfrac12\cdot2\cdot3t\cdot\dfrac{\sqrt{-t^{4}+14t^{2}-1}}{4t}=\dfrac{3}{2}\sqrt{-t^{4}+14t^{2}-1}$" "\n"
        r"$=\dfrac32\sqrt{48-(t^{2}-7)^{2}}$．" "\n"
        r"当 $t^{2}=7$ 时，$S_{\max}=\dfrac32\sqrt{48}=\dfrac32\cdot4\sqrt3=6\sqrt3$．选 C．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓，由详解「因为 $D,E$ 分别是边 $AB,AC$ 的中点，所以 $DE\parallel BC,DE=\frac12BC$，" "\n"
        r"所以 $\frac{EO}{BO}=\frac{DO}{CO}=\frac12$，又 $OC=\sqrt3OB$，设 $OE=t(t>0)$，则 $OB=2t,OD=\sqrt3t,OC=2\sqrt3t$，" "\n"
        r"又因为 $AB=2$，所以 $DB=1$，设 $\angle ABO=\alpha$，在 $\triangle DBO$ 中，" "\n"
        r"$\cos\alpha=\frac{DB^{2}+OB^{2}-DO^{2}}{2BD\cdot BO}=\frac{1+(2t)^{2}-(\sqrt3t)^{2}}{4t}=\frac{t^{2}+1}{4t}$，" "\n"
        r"所以 $\sin\alpha=\frac{\sqrt{-t^{4}+14t^{2}-1}}{4t}$，由三角形的面积公式表示 $\triangle ABC$ 的面积，" "\n"
        r"根据二次函数的最值可得选项…时，$\triangle ABC$ 面积取得最大值 $6\sqrt3$，故选 C」还原，" "\n"
        r"**与我的推导一致** ✓。" "\n"
        r"**独立验算**：" "\n"
        r"① **比例核对**：$DE:BC=1:2$ ⟹ $\frac{DO}{CO}=\frac{EO}{BO}=\frac12$ ✓；重心 $CO:OD=2:1$ ✓ 自洽" "\n"
        r"② **$OB=2t$**：由 $\frac{EO}{BO}=\frac12$ 且 $EO=t$ ⟹ $BO=2t$ ✓✓" "\n"
        r"③ **$OC=2\sqrt3t$**：由 $OC=\sqrt3 OB=\sqrt3(2t)=2\sqrt3 t$ ✓；$DO=\frac{OC}2=\sqrt3t$ ✓✓" "\n"
        r"④ **$\cos\alpha$**：$\frac{1+4t^2-3t^2}{4t}=\frac{t^2+1}{4t}$ ✓✓" "\n"
        r"⑤ **$\sin\alpha$**：$1-\frac{(t^2+1)^2}{16t^2}=\frac{16t^2-(t^4+2t^2+1)}{16t^2}=\frac{-t^4+14t^2-1}{16t^2}$ ✓✓" "\n"
        r"⑥ **配方**：$-(t^2-7)^2+48=-(t^4-14t^2+49)+48=-t^4+14t^2-1$ ✓✓" "\n"
        r"⑦ **$S_{\max}$**：$t^2=7$ ⟹ $S=\frac32\sqrt{48}=\frac32(6.928)=10.392$；$6\sqrt3=6(1.732)=10.392$ ✓✓✓" "\n"
        r"⑧ **取等时的合法性**（$t=\sqrt7=2.6458$）：" "\n"
        r"$\cos\alpha=\frac{7+1}{4(2.6458)}=\frac8{10.583}=0.7559$ ⟹ $\alpha=40.89^\circ$ ✓ 合法" "\n"
        r"$BE=3t=7.937$、$OB=5.291$、$DO=4.583$、$OC=9.165$" "\n"
        r"验 $\triangle DBO$：$DB=1$、$BO=5.291$、$DO=4.583$；三角关系 $1+4.583=5.583>5.291$ ✓" "\n"
        r"$S_{\triangle ABE}=\frac12\cdot2\cdot7.937\cdot\sin40.89^\circ=7.937(0.6547)=5.196$" "\n"
        r"$S_{\triangle ABC}=2(5.196)=10.392$ ✓✓✓" "\n"
        r"**答案 C（$6\sqrt3$）正确** ✓" "\n"
        r"**⭐ 通法（重心 + 中线交点的线段比例）**：" "\n"
        r"① 两条中线的交点是**重心**，分每条中线为 $2:1$（**顶点到重心 : 重心到中点 $=2:1$**）；" "\n"
        r"② 两中点的连线是**中位线**，$\triangle ODE\sim\triangle OCB$ 给出另一组比例 —— " "\n"
        r"两组比例**必须自洽**（本题都给出 $2:1$），这是验算的好办法；" "\n"
        r"③ 设**最短的那段为 $t$**，把 $OB,OD,OC,OE$ 全表成 $t$ 的倍数；" "\n"
        r"④ 在含已知边的小三角形（本题 $\triangle DBO$，因 $DB=1$ 已知）中用余弦定理；" "\n"
        r"⑤ ⚠ **面积换算**：$S_{ABC}=2S_{ABE}$（$E$ 是中点），别漏这个因子 $2$。"
    ),
    'difficulty': 0.94,
    'topics': ['M-T-201'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-201-V3',
}

QS = [T201_V1, T201_V2, T201_V3]
