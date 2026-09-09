# -*- coding: utf-8 -*-
r"""第58批（一）：共焦点的椭圆与双曲线（4 题） 来源：2024高中数学热点题型归纳完整解析版.pdf　p353（PDF 页 352）M-T-372 ## ★★ 本批最重要的收获：一个通吃公式 设椭圆与双曲线**共焦点** $F_1,F_2$，$P$ 是一个公共交点，$\angle F_1PF_2=\theta$。 记 $|PF_1|=r_1$、$|PF_2|=r_2$，则 $$r_1+r_2=2a\ (\text{椭圆}),\qquad |r_1-r_2|=2m\ (\text{双曲线})$$ 在 $\triangle F_1PF_2$ 中用余弦定理： $$4c^{2}=r_1^{2}+r_2^{2}-2r_1r_2\cos\theta$$ 把 $r_1^{2}+r_2^{2}$ 分别用「和」与「差」表示，可得两条**恒等式**： $$\frac{1}{e_1^{2}}=1+\frac{(2+2\cos\theta)r_1r_2}{4c^{2}}\cdot\frac{1}{\,}\ \Longrightarrow\ \frac{1}{e_1^{2}}-1=\frac{(1+\cos\theta)}{2}\cdot\frac{r_1r_2}{c^{2}}$$ $$1-\frac{1}{e_2^{2}}=\frac{(1-\cos\theta)}{2}\cdot\frac{r_1r_2}{c^{2}}$$ 两式相除消掉 $r_1r_2$： $$\boxed{\frac{\frac1{e_1^{2}}-1}{1-\frac1{e_2^{2}}}=\frac{1+\cos\theta}{1-\cos\theta}=\cot^{2}\frac\theta2}$$ **V2 就是 $\theta=\frac\pi3$ 的情形**（$\cot^2\frac\pi6=3$）。 ## ⭐⭐ 求和最大值的秒杀公式 $$\max\left(\frac1{e_1}+\frac1{e_2}\right)=\frac{2}{\sin\theta}$$ 推导：令 $\frac1{e_1}=2\cos\varphi\cdot\frac{1}{\sqrt{2(1+\cos\theta)/2}}$… 更简洁地， 设 $u=\frac1{e_1}$、$v=\frac1{e_2}$，约束为 $\alpha u^{2}+\beta v^{2}=\text{const}$ 型， 用柯西或三角代换即得振幅 $=\frac2{\sin\theta}$。 | $\theta$ | $\frac{2}{\sin\theta}$ | 题 | |---|---|---| | $\frac\pi3$ | $\frac{4}{\sqrt3}=\frac{4\sqrt3}3$ | **V1** ✓ | | $\frac\pi4$ | $\frac{4}{\sqrt2}=2\sqrt2$ | **V3** ✓ | **两题互相印证**：同一个公式，换 $\theta$ 就出答案。原书 V1 的详解 （$2\cos\varphi+\frac{2}{\sqrt3}\sin\varphi$，振幅 $\sqrt{4+\frac43}=\frac4{\sqrt3}$） 与这个公式一致。 ## 四题验算 | 题 | 我的结果 | 答案 | |---|---|---| | E1 | $e_1e_2=\sqrt{1+\frac1{a^{2}-2a}}\in(1,+\infty)$ | **A** | | V1 | $\frac{2}{\sin\frac\pi3}=\frac{4\sqrt3}3\approx2.3094$ | **A** | | V2 | $\frac1{4e_1^{2}}+\frac3{4e_2^{2}}=1$ | **B** | | V3 | $\frac{2}{\sin\frac\pi4}=2\sqrt2\approx2.8284$ | **B** | """

T372_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知有相同焦点 $F_1,F_2$ 的椭圆 $\dfrac{x^{2}}a+y^{2}=1\ (a>1)$ 和双曲线 $\dfrac{x^{2}}m-y^{2}=1\ (m>0)$，"
        r"则椭圆与双曲线的离心率之积的范围为（　　）"
    ),
    'opts': [
        ('A', r"$(1,+\infty)$"),
        ('B', r"$(0,1)$"),
        ('C', r"$\left(0,\dfrac12\right)$"),
        ('D', r"$\left(\dfrac12,1\right)$"),
    ],
    'answer': 'A',
    'analysis': (
        r"相同焦点 ⟹ $a-1=m+1$，即 $m=a-2>0$。$e_1e_2=\sqrt{1+\frac1{a^{2}-2a}}$，"
        r"$a\to2^{+}$ 时趋于 $+\infty$，$a\to+\infty$ 时趋于 $1$，故范围 $(1,+\infty)$。"
    ),
    'solution': (
        r"**第一步：由共焦点得参数关系**" "\n"
        r"椭圆 $\dfrac{x^{2}}a+y^{2}=1$：$a_{\text{椭}}^{2}=a$、$b_{\text{椭}}^{2}=1$，$c^{2}=a-1$。" "\n"
        r"双曲线 $\dfrac{x^{2}}m-y^{2}=1$：$m_{\text{双}}^{2}=m$、$n^{2}=1$，$c^{2}=m+1$。" "\n"
        r"共焦点：$a-1=m+1\Rightarrow m=a-2$，由 $m>0$ 得 $a>2$。" "\n"
        r"**第二步：写出两个离心率**" "\n"
        r"$e_1=\dfrac{c}{\sqrt a}=\sqrt{\dfrac{a-1}a}$，$e_2=\dfrac{c}{\sqrt m}=\sqrt{\dfrac{m+1}m}=\sqrt{\dfrac{a-1}{a-2}}$．" "\n"
        r"**第三步：求积**" "\n"
        r"$e_1e_2=\sqrt{\dfrac{a-1}a\cdot\dfrac{a-1}{a-2}}=\dfrac{a-1}{\sqrt{a(a-2)}}$．" "\n"
        r"平方得 $(e_1e_2)^{2}=\dfrac{(a-1)^{2}}{a^{2}-2a}=\dfrac{a^{2}-2a+1}{a^{2}-2a}=1+\dfrac1{a^{2}-2a}$．" "\n"
        r"**第四步：看范围**" "\n"
        r"$a>2$ 时 $a^{2}-2a=a(a-2)>0$，且随 $a$ 增大而增大：" "\n"
        r"$a\to2^{+}$ 时 $a^{2}-2a\to0^{+}$，$(e_1e_2)^{2}\to+\infty$；" "\n"
        r"$a\to+\infty$ 时 $\dfrac1{a^{2}-2a}\to0^{+}$，$(e_1e_2)^{2}\to1^{+}$．" "\n"
        r"故 $e_1e_2\in(1,+\infty)$．选 A．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**详解未提取**，上述推导为我独立完成）。" "\n"
        r"**独立验算**：" "\n"
        r"① **共焦点**：椭圆 $c^2=a-1$ ✓；双曲线 $c^2=m+1$ ✓；$a-1=m+1\\Rightarrow m=a-2$ ✓✓" "\n"
        r"② **离心率**：$e_1=\\frac{c}{a_{\\text{椭}}}=\\frac{\\sqrt{a-1}}{\\sqrt a}$ ✓；$e_2=\\frac{\\sqrt{m+1}}{\\sqrt m}$ ✓✓" "\n"
        r"③ **代入 $m=a-2$**：$\\frac{m+1}m=\\frac{a-1}{a-2}$ ✓✓" "\n"
        r"④ **乘积平方**：$\\frac{(a-1)^2}{a(a-2)}=\\frac{a^2-2a+1}{a^2-2a}=1+\\frac1{a^2-2a}$ ✓✓✓" "\n"
        r"⑤ **数值扫描**：" "\n"
        r"$a=2.01\\to7.1240$；$a=2.5\\to1.3416$；$a=5\\to1.0328$；$a=100\\to1.0001$ ✓✓" "\n"
        r"**始终 $>1$，且可任意大** ⟹ $(1,+\\infty)$ ✓✓✓ **恰为 A**" "\n"
        r"⑥ **$a\\to\\infty$ 时不取到 $1$**：$1+\\frac1{a^2-2a}>1$ 恒成立 ✓（开区间）" "\n"
        r"⑦ **排除其他**：B $=(0,1)$ 方向反了；C、D 是 $(0,1)$ 的子区间 ✗" "\n"
        r"**答案 A（$(1,+\\infty)$）正确** ✓" "\n"
        r"**⭐ 通法（共焦点曲线）**：" "\n"
        r"① ⭐ **共焦点 ⟹ $c$ 相同**，先把两个 $c^{2}$ 表达式写出来令其相等，得到参数关系（本题 $m=a-2$）；" "\n"
        r"② 注意**定义域约束**（$m>0$ 给出 $a>2$），这往往就是范围的端点；" "\n"
        r"③ 乘积（或和）化成一个参数的函数后，**看两端极限**定范围；" "\n"
        r"④ 本题 $(e_1e_2)^2=1+\\frac1{a^2-2a}$ 的形式很典型：$a\\to2^+$ 爆掉、$a\\to\\infty$ 趋于 $1$。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-372'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-372-E1',
}

T372_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知 $F_1,F_2$ 是椭圆和双曲线的公共焦点，$P$ 是它们的一个公共交点，"
        r"且 $\angle F_1PF_2=\dfrac\pi3$，则椭圆和双曲线的离心率倒数之和的最大值为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac{4\sqrt3}3$"),
        ('B', r"$\dfrac{3\sqrt3}4$"),
        ('C', r"$2$"),
        ('D', r"$2\sqrt3$"),
    ],
    'answer': 'A',
    'analysis': (
        r"设 $|PF_1|=r_1$、$|PF_2|=r_2$，则 $r_1+r_2=2a$、$|r_1-r_2|=2m$。"
        r"在 $\triangle F_1PF_2$ 中 $4c^{2}=r_1^{2}+r_2^{2}-r_1r_2$（$\cos\frac\pi3=\frac12$）。"
        r"由此得 $\frac1{e_1^{2}}+\frac3{e_2^{2}}=4$，三角代换后最大值 $=\frac2{\sin\frac\pi3}=\frac{4\sqrt3}3$。"
    ),
    'solution': (
        r"**第一步：设量并列定义式**" "\n"
        r"设 $|PF_1|=r_1$、$|PF_2|=r_2$，$|F_1F_2|=2c$。" "\n"
        r"椭圆定义：$r_1+r_2=2a$；双曲线定义：$|r_1-r_2|=2m$。" "\n"
        r"$e_1=\dfrac ca$、$e_2=\dfrac cm$，故 $\dfrac1{e_1}=\dfrac ac$、$\dfrac1{e_2}=\dfrac mc$．" "\n"
        r"**第二步：余弦定理**" "\n"
        r"$4c^{2}=r_1^{2}+r_2^{2}-2r_1r_2\cos\dfrac\pi3=r_1^{2}+r_2^{2}-r_1r_2$．" "\n"
        r"于是 $r_1^{2}+r_2^{2}=4c^{2}+r_1r_2$．" "\n"
        r"**第三步：转成 $a,m$ 的关系**" "\n"
        r"$4a^{2}=(r_1+r_2)^{2}=r_1^{2}+r_2^{2}+2r_1r_2=4c^{2}+3r_1r_2\Rightarrow 3r_1r_2=4a^{2}-4c^{2}$；" "\n"
        r"$4m^{2}=(r_1-r_2)^{2}=r_1^{2}+r_2^{2}-2r_1r_2=4c^{2}-r_1r_2\Rightarrow r_1r_2=4c^{2}-4m^{2}$．" "\n"
        r"消去 $r_1r_2$：$4a^{2}-4c^{2}=3(4c^{2}-4m^{2})\Rightarrow a^{2}+3m^{2}=4c^{2}$．" "\n"
        r"两边除 $c^{2}$：$\dfrac1{e_1^{2}}+\dfrac3{e_2^{2}}=4$．" "\n"
        r"**第四步：三角代换求最大值**" "\n"
        r"令 $\dfrac1{e_1}=2\cos\varphi$、$\dfrac{\sqrt3}{e_2}=2\sin\varphi$（$\varphi\in\left(0,\dfrac\pi2\right)$），" "\n"
        r"则 $\dfrac1{e_1}+\dfrac1{e_2}=2\cos\varphi+\dfrac2{\sqrt3}\sin\varphi =\sqrt{4+\dfrac43}\,\sin(\varphi+\psi)=\dfrac4{\sqrt3}\sin(\varphi+\psi)\le\dfrac4{\sqrt3}=\dfrac{4\sqrt3}3$．" "\n"
        r"选 A．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓。原书 p353 详解：「$|PF_1|+|PF_2|=2a$，$|PF_1|-|PF_2|=2m$，" "\n"
        r"得 $|PF_1|=a+m$、$|PF_2|=a-m$…即 $4c^{2}=a^{2}+3m^{2}$」—— **与我的推导一致** ✓，" "\n"
        r"且原文给出 $\\frac{1}{e_1}+\\frac{1}{e_2}=2\\cos\\theta+\\frac{2}{\\sqrt3}\\sin\\theta=\\frac4{\\sqrt3}\\sin(\\theta+\\frac\\pi3)$，" "\n"
        r"最大值为 $\\frac{4\\sqrt3}{3}$，故选 A ✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **$4c^2=a^2+3m^2$ 直接验证**：$r_1=a+m$、$r_2=a-m$（$a>m$）" "\n"
        r"$r_1^2+r_2^2-r_1r_2=(a+m)^2+(a-m)^2-(a+m)(a-m)=2a^2+2m^2-a^2+m^2=a^2+3m^2$ ✓✓✓" "\n"
        r"② **恒等式**：$\\frac{a^2}{c^2}+\\frac{3m^2}{c^2}=4\\Rightarrow\\frac1{e_1^2}+\\frac3{e_2^2}=4$ ✓✓" "\n"
        r"③ **三角代换振幅**：$\\sqrt{2^2+(\\frac2{\\sqrt3})^2}=\\sqrt{4+\\frac43}=\\sqrt{\\frac{16}3}=\\frac4{\\sqrt3}$ ✓✓✓" "\n"
        r"④ **数值**：$\\frac{4\\sqrt3}3=\\frac{6.9282}3=2.30940$ ✓✓✓ **恰为选项 A**" "\n"
        r"⑤ ⭐ **通式验证**：$\\frac{2}{\\sin(\\pi/3)}=\\frac{2}{0.86603}=2.30940$ ✓✓✓ **完全一致**" "\n"
        r"⑥ **排除其他**：B $=\\frac{3\\sqrt3}4=1.299$（倒数了）；C $=2$；D $=2\\sqrt3=3.464$ ✗" "\n"
        r"**答案 A（$\\frac{4\\sqrt3}3$）正确** ✓" "\n"
        r"**⭐⭐ 通法（共焦点曲线 + 张角）**：" "\n"
        r"① ⭐⭐ **秒杀公式**：$\\max(\\frac1{e_1}+\\frac1{e_2})=\\frac{2}{\\sin\\theta}$，" "\n"
        r"其中 $\\theta=\\angle F_1PF_2$。本题 $\\theta=\\frac\\pi3$ ⟹ $\\frac{4\\sqrt3}3$；" "\n"
        r"M-T-372-V3 的 $\\theta=\\frac\\pi4$ ⟹ $2\\sqrt2$ —— **两题同公式，互相印证**；" "\n"
        r"② 推导核心：$r_1=a+m$、$r_2=a-m$（把和与差解出来），代余弦定理直接得 $a,m,c$ 的齐次关系；" "\n"
        r"③ 一般的恒等式：$\\frac{1/e_1^{2}-1}{1-1/e_2^{2}}=\\cot^{2}\\frac\\theta2$（$\\theta=\\frac\\pi3$ 时 $=3$）；" "\n"
        r"④ 求「$A u+B v$ 在 $\\alpha u^{2}+\\beta v^{2}=$ 常数下的最大值」⟹ **三角代换看振幅**，比求导快。"
    ),
    'difficulty': 0.93,
    'topics': ['M-T-372'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-372-V1',
}

T372_V2 = {
    'type': '选择',
    'stem_text': (
        r"椭圆与双曲线共焦点 $F_1,F_2$，它们的交点 $P$ 对两公共焦点 $F_1,F_2$ 张的角为"
        r"$\angle F_1PF_2=\dfrac\pi3$。椭圆与双曲线的离心率分别为 $e_1,e_2$，则（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac{3}{4e_1^{2}}+\dfrac1{4e_2^{2}}=1$"),
        ('B', r"$\dfrac1{4e_1^{2}}+\dfrac3{4e_2^{2}}=1$"),
        ('C', r"$\dfrac{4e_1^{2}}3+4e_2^{2}=1$"),
        ('D', r"$4e_1^{2}+\dfrac{4e_2^{2}}3=1$"),
    ],
    'answer': 'B',
    'analysis': (
        r"由余弦定理得 $4c^{2}=r_1^{2}+r_2^{2}-r_1r_2$。用 $r_1+r_2=2a$ 得 $\frac{3r_1r_2}{4c^{2}}=\frac1{e_1^{2}}-1$；"
        r"用 $|r_1-r_2|=2m$ 得 $\frac{r_1r_2}{4c^{2}}=1-\frac1{e_2^{2}}$。消去 $r_1r_2$ 即得。"
    ),
    'solution': (
        r"**第一步：余弦定理**" "\n"
        r"设 $|PF_1|=r_1$、$|PF_2|=r_2$，则 $4c^{2}=r_1^{2}+r_2^{2}-2r_1r_2\cos\dfrac\pi3=r_1^{2}+r_2^{2}-r_1r_2$，" "\n"
        r"即 $r_1^{2}+r_2^{2}=4c^{2}+r_1r_2$．" "\n"
        r"**第二步：用椭圆定义**" "\n"
        r"$4a^{2}=(r_1+r_2)^{2}=r_1^{2}+r_2^{2}+2r_1r_2=4c^{2}+3r_1r_2$，" "\n"
        r"$\Rightarrow\dfrac{3r_1r_2}{4c^{2}}=\dfrac{a^{2}}{c^{2}}-1=\dfrac1{e_1^{2}}-1\qquad(1)$" "\n"
        r"**第三步：用双曲线定义**" "\n"
        r"$4m^{2}=(r_1-r_2)^{2}=r_1^{2}+r_2^{2}-2r_1r_2=4c^{2}-r_1r_2$，" "\n"
        r"$\Rightarrow\dfrac{r_1r_2}{4c^{2}}=1-\dfrac{m^{2}}{c^{2}}=1-\dfrac1{e_2^{2}}\qquad(2)$" "\n"
        r"**第四步：消去 $r_1r_2$**" "\n"
        r"由 $(1)(2)$：$\dfrac1{e_1^{2}}-1=3\left(1-\dfrac1{e_2^{2}}\right)$，" "\n"
        r"即 $\dfrac1{e_1^{2}}+\dfrac3{e_2^{2}}=4$，两边除以 $4$ 得 $\dfrac1{4e_1^{2}}+\dfrac3{4e_2^{2}}=1$．选 B．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓。原书 p353 详解明确给出：" "\n"
        r"「$\\frac{3r_1r_2}{4c^{2}}=\\frac1{e_1^{2}}-1$，$\\frac{r_1r_2}{4c^{2}}=1-\\frac1{e_2^{2}}$」" "\n"
        r"—— **与我的 $(1)(2)$ 两式完全一致** ✓✓" "\n"
        r"**独立验算**：" "\n"
        r"① **$(1)$ 式**：$4a^2=4c^2+3r_1r_2\\Rightarrow3r_1r_2=4a^2-4c^2\\Rightarrow\\frac{3r_1r_2}{4c^2}=\\frac{a^2}{c^2}-1=\\frac1{e_1^2}-1$ ✓✓" "\n"
        r"② **$(2)$ 式**：$4m^2=4c^2-r_1r_2\\Rightarrow r_1r_2=4c^2-4m^2\\Rightarrow\\frac{r_1r_2}{4c^2}=1-\\frac{m^2}{c^2}=1-\\frac1{e_2^2}$ ✓✓" "\n"
        r"③ **消元**：$\\frac1{e_1^2}-1=3(1-\\frac1{e_2^2})\\Rightarrow\\frac1{e_1^2}+\\frac3{e_2^2}=4$ ✓✓✓" "\n"
        r"④ **除以 $4$**：$\\frac1{4e_1^2}+\\frac3{4e_2^2}=1$ ✓✓✓ **恰为选项 B**" "\n"
        r"⑤ **与 V1 交叉验证**：V1 由同样条件得 $a^2+3m^2=4c^2$，" "\n"
        r"即 $\\frac1{e_1^2}+\\frac3{e_2^2}=4$ —— **两题同源，结论一致** ✓✓✓" "\n"
        r"⑥ **数值检验**：取 $e_1=\\frac{\\sqrt3}{2}$（即 $\\frac1{e_1^2}=\\frac43$），则 $\\frac3{e_2^2}=4-\\frac43=\\frac83$，$e_2^2=\\frac98$，$e_2=1.0607>1$ ✓ 合理" "\n"
        r"代回 B：$\\frac{1}{4}\\cdot\\frac43+\\frac34\\cdot\\frac89=\\frac13+\\frac23=1$ ✓✓✓" "\n"
        r"⑦ **排除其他**：A 把系数 $1,3$ 放反了；C、D 把 $e$ 放到了分子（$e>1$ 时 $4e_1^2>4$，不可能等于 $1$）✗✗" "\n"
        r"**答案 B 正确** ✓" "\n"
        r"**⭐ 通法（共焦点 + 张角 ⟹ 恒等式）**：" "\n"
        r"① ⭐ 万能套路：**余弦定理写出 $4c^2=r_1^2+r_2^2-2r_1r_2\\cos\\theta$，" "\n"
        r"再用 $(r_1+r_2)^2$ 和 $(r_1-r_2)^2$ 分别消去 $r_1^2+r_2^2$，得到两个关于 $r_1r_2$ 的式子，消去 $r_1r_2$**；" "\n"
        r"② 一般结论：$\\frac{1/e_1^{2}-1}{1-1/e_2^{2}}=\\frac{1+\\cos\\theta}{1-\\cos\\theta}=\\cot^{2}\\frac\\theta2$。" "\n"
        r"本题 $\\theta=\\frac\\pi3$ 时 $\\cot^{2}\\frac\\pi6=3$ ✓ 正是 B 中 $e_2$ 的系数；" "\n"
        r"③ ⚠ **选项里 $e$ 在分母还是分子**要分清：$e_1<1<e_2$，若把 $e$ 放分子（C、D）则 $4e_1^2+...$ 中 $e_2>1$ 使值 $>1$，立刻排除。"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-372'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-372-V2',
}

T372_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知椭圆与双曲线有公共焦点 $F_1,F_2$，$F_1$ 为左焦点，$F_2$ 为右焦点，"
        r"$P$ 点为它们在第一象限的一个交点，且 $\angle F_1PF_2=\dfrac\pi4$，"
        r"设 $e_1,e_2$ 分别为椭圆、双曲线的离心率，则 $\dfrac1{e_1}+\dfrac1{e_2}$ 的最大值为（　　）"
    ),
    'opts': [
        ('A', r"$\sqrt2$"),
        ('B', r"$2\sqrt2$"),
        ('C', r"$\dfrac{3\sqrt2}2$"),
        ('D', r"$\dfrac{\sqrt2}4$"),
    ],
    'answer': 'B',
    'analysis': (
        r"套用通式 $\max(\frac1{e_1}+\frac1{e_2})=\frac2{\sin\theta}$，$\theta=\frac\pi4$ 得 $\frac{2}{\sqrt2/2}=2\sqrt2$。"
        r"也可由 $\frac1{e_1^{2}}+k\cdot\frac1{e_2^{2}}$ 型约束（$k=\cot^{2}\frac\pi8=3-2\sqrt2$）三角代换求得。"
    ),
    'solution': (
        r"**第一步：套用共焦点张角的一般结论**" "\n"
        r"设 $|PF_1|=r_1$、$|PF_2|=r_2$。由 $\triangle F_1PF_2$ 的余弦定理（$\cos\frac\pi4=\frac{\sqrt2}2$）：" "\n"
        r"$4c^{2}=r_1^{2}+r_2^{2}-\sqrt2\,r_1r_2$．" "\n"
        r"**第二步：分别用两个定义**" "\n"
        r"$4a^{2}=(r_1+r_2)^{2}=4c^{2}+(2+\sqrt2)r_1r_2$；" "\n"
        r"$4m^{2}=(r_1-r_2)^{2}=4c^{2}-(2-\sqrt2)r_1r_2$．" "\n"
        r"消去 $r_1r_2$，记 $k=\dfrac{2-\sqrt2}{2+\sqrt2}=\dfrac{(2-\sqrt2)^{2}}{2}=3-2\sqrt2=(\sqrt2-1)^{2}$：" "\n"
        r"$\dfrac{4a^{2}-4c^{2}}{2+\sqrt2}=r_1r_2=\dfrac{4c^{2}-4m^{2}}{2-\sqrt2}\Rightarrow a^{2}-c^{2}=\dfrac{4c^{2}-4m^{2}}{2-\sqrt2}\cdot\dfrac{2+\sqrt2}{4}$，" "\n"
        r"整理为 $m^{2}=c^{2}-k(a^{2}-c^{2})$．" "\n"
        r"**第三步：三角代换**" "\n"
        r"两边除 $c^{2}$，记 $u=\dfrac1{e_1}=\dfrac ac$、$v=\dfrac1{e_2}=\dfrac mc$：" "\n"
        r"$v^{2}=1-k(u^{2}-1)=1+k-ku^{2}\Rightarrow ku^{2}+v^{2}=1+k$．" "\n"
        r"令 $u=\sqrt{\frac{1+k}k}\cos\varphi$、$v=\sqrt{1+k}\sin\varphi$，则" "\n"
        r"$u+v$ 的最大值为 $\sqrt{\dfrac{1+k}k+(1+k)}=\sqrt{\dfrac{(1+k)^{2}}k}=\dfrac{1+k}{\sqrt k}=\dfrac1{\sqrt k}+\sqrt k$．" "\n"
        r"**第四步：代入 $k=(\sqrt2-1)^{2}$**" "\n"
        r"$\sqrt k=\sqrt2-1$，$\dfrac1{\sqrt k}=\sqrt2+1$，故最大值 $=(\sqrt2+1)+(\sqrt2-1)=2\sqrt2$．选 B．" "\n"
        r"（等价地，直接用通式 $\dfrac2{\sin\frac\pi4}=\dfrac{2}{\sqrt2/2}=2\sqrt2$ ✓）"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓（**详解未提取**，上述推导为我独立完成）。" "\n"
        r"**独立验算**：" "\n"
        r"① **$k$ 的值**：$\\frac{2-\\sqrt2}{2+\\sqrt2}=\\frac{(2-\\sqrt2)^2}{4-2}=\\frac{6-4\\sqrt2}{2}=3-2\\sqrt2=0.17157$ ✓✓" "\n"
        r"$(\\sqrt2-1)^2=2-2\\sqrt2+1=3-2\\sqrt2$ ✓✓✓ **一致**" "\n"
        r"② **$\\sqrt k$**：$\\sqrt2-1=0.41421$；$\\frac1{\\sqrt k}=\\frac1{\\sqrt2-1}=\\sqrt2+1=2.41421$ ✓✓" "\n"
        r"③ **最大值**：$2.41421+0.41421=2.82843$；$2\\sqrt2=2.82843$ ✓✓✓ **恰为选项 B**" "\n"
        r"④ ⭐⭐ **通式交叉验证**：$\\frac{2}{\\sin(\\pi/4)}=\\frac{2}{0.70711}=2.82843$ ✓✓✓ **完全一致**" "\n"
        r"⑤ **与 V1 互相印证**：V1 中 $\\theta=\\frac\\pi3$ ⟹ $\\frac{2}{\\sin(\\pi/3)}=2.30940=\\frac{4\\sqrt3}3$ ✓；" "\n"
        r"本题 $\\theta=\\frac\\pi4$ ⟹ $2.82843=2\\sqrt2$ ✓ **同一公式的两个特例**" "\n"
        r"⑥ **约束式验证**：取 $k=0.17157$，$u=\\frac{1}{\\sqrt k}=\\frac{1}{0.41421}=2.41421$、$v=\\sqrt k=0.41421$：" "\n"
        r"$ku^2+v^2=0.17157(5.8284)+0.17157=1.0+0.17157=1.17157=1+k$ ✓✓✓ **满足约束**" "\n"
        r"⑦ **合理性**：$e_1=\\frac1u=0.41421<1$ ✓（椭圆）；$e_2=\\frac1v=2.41421>1$ ✓（双曲线）" "\n"
        r"⑧ **排除其他**：A $=\\sqrt2=1.414$（只有一半）；C $=\\frac{3\\sqrt2}2=2.121$；D $=\\frac{\\sqrt2}4=0.354$ ✗" "\n"
        r"**答案 B（$2\\sqrt2$）正确** ✓" "\n"
        r"**⭐⭐ 通法（背诵级结论）**：" "\n"
        r"① ⭐⭐ **共焦点椭圆+双曲线，交点对焦点张角 $\\theta$ 时**：" "\n"
        r"$$\\max\\left(\\frac1{e_1}+\\frac1{e_2}\\right)=\\frac{2}{\\sin\\theta}$$" "\n"
        r"$\\theta=\\frac\\pi3\\to\\frac{4\\sqrt3}3$（V1）；$\\theta=\\frac\\pi4\\to2\\sqrt2$（V3）；$\\theta=\\frac\\pi2\\to2$。" "\n"
        r"② 推导的一般形式：令 $k=\\frac{1-\\cos\\theta}{1+\\cos\\theta}=\\tan^{2}\\frac\\theta2$ ，" "\n"
        r"则约束为 $ku^{2}+v^{2}=1+k$，最大值 $=\\frac1{\\sqrt k}+\\sqrt k=\\tan\\frac\\theta2+\\cot\\frac\\theta2=\\frac{2}{\\sin\\theta}$ ✓ " "\n"
        r"（最后一步用了 $\\tan\\frac\\theta2+\\cot\\frac\\theta2=\\frac{\\sin^2+\\cos^2}{\\sin\\frac\\theta2\\cos\\frac\\theta2}=\\frac{2}{\\sin\\theta}$）；" "\n"
        r"③ ⚠ 这类题**不必每次重新推导**，记住通式后代入 $\\theta$ 即可，但**必须验证 $\\theta=\\frac\\pi3$ 与 $\\frac\\pi4$ 两种情形**（本题与 V1 互为印证）。"
    ),
    'difficulty': 0.94,
    'topics': ['M-T-372'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-372-V3',
}

QS = [T372_E1, T372_V1, T372_V2, T372_V3]
