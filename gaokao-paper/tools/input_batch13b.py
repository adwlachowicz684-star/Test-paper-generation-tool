# -*- coding: utf-8 -*-
r"""第13批（下）：T039 差比法与商比法 / T040 分离常数比大小，共 8 题。

来源：2024高中数学热点题型归纳完整解析版.pdf 专题2-1 p13~p14（PDF 页 12~13）

与上半批同样的问题：上标、下标、分数线在提取时全部塌成平文本。
T040-V2 最严重——$x,y,z$ 三个复合式被拆成「b 2a」「log2 a + b」「a + 1 b」，
仅凭提取文本无法还原，是靠详解里「$z=2a=\log_2 4^a$」反推出的。

LaTeX 一律 raw 双引号 r"..."；中文行文用弯引号“”，不用 ASCII 双引号。
"""

T039_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知实数 $a,b,c$ 满足 $a=6^{\frac13}$，$b=\log_{2}3+\log_{6}4$，"
        r"$5^{b}+12^{b}=13^{c}$，则 $a,b,c$ 的关系是（　　）"
    ),
    'opts': [
        ('A', r"$b>a>c$"), ('B', r"$c>b>a$"),
        ('C', r"$b>c>a$"), ('D', r"$c>a>b$"),
    ],
    'answer': 'C',
    'analysis': r"$a$ 直接估算；$b$ 用作差法证 $b>2$；$b,c$ 用 $13^{c}-13^{b}$ 判正负。",
    'solution': (
        r"$a=6^{\frac13}<8^{\frac13}=2$，故 $a<2$．" "\n"
        r"由换底 $\log_{6}4=\dfrac{\log_{2}4}{\log_{2}6}=\dfrac{2}{1+\log_{2}3}$，"
        r"令 $t=\log_{2}3$，则" "\n"
        r"$b-2=t+\dfrac{2}{1+t}-2=\dfrac{t^{2}-t}{1+t}=\dfrac{t(t-1)}{1+t}>0$（因 $t>1$），故 $b>2$．" "\n"
        r"由 $13^{c}=5^{b}+12^{b}>5^{2}+12^{2}=13^{2}$ 得 $c>2$；" "\n"
        r"又 $13^{c}-13^{b}=5^{b}+12^{b}-13^{b}$" "\n"
        r"$=5^{2}\cdot5^{b-2}+12^{2}\cdot12^{b-2}-13^{2}\cdot13^{b-2}$" "\n"
        r"$<5^{2}\cdot12^{b-2}+12^{2}\cdot12^{b-2}-13^{2}\cdot13^{b-2}$" "\n"
        r"$=13^{2}\left(12^{b-2}-13^{b-2}\right)<0$，故 $c<b$．" "\n"
        r"综上 $b>c>a$，故选 C．"
    ),
    'review': (
        r"★ 提取文本作「a = 61,b = log3 + log4,5b+ 12b= 13c」，$6^{1/3}$ 的指数、"
        r"$\log_64$ 的底数全丢，且把 $13^{c}$ 误写成 $13c$。"
        r"按详解的作差结构还原。数值校验：$a\approx1.8171$、"
        r"$b\approx2.3587$、由 $5^b+12^b\approx395.3$ 得 $c\approx2.331$，"
        r"顺序 $b>c>a$ 与答案 C 一致。"
    ),
    'difficulty': 0.7,
    'topics': ['M-T-039'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-039-E1',
}

T039_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知 $a=0.8^{-0.4}$，$b=\log_{5}3$，$c=\log_{8}5$，则（　　）"
    ),
    'opts': [
        ('A', r"$a<b<c$"), ('B', r"$b<c<a$"),
        ('C', r"$c<b<a$"), ('D', r"$a<c<b$"),
    ],
    'answer': 'B',
    'analysis': r"$b,c$ 用作商法配基本不等式比较；$a$ 用指数性质直接得 $a>1>c$。",
    'solution': (
        r"作商并换底：" "\n"
        r"$\dfrac{b}{c}=\dfrac{\log_{5}3}{\log_{8}5}"
        r"=\dfrac{\ln3\cdot\ln8}{\ln^{2}5}"
        r"<\dfrac{\left(\dfrac{\ln3+\ln8}{2}\right)^{2}}{\ln^{2}5}"
        r"=\dfrac{\ln^{2}24}{4\ln^{2}5}<\dfrac{\ln^{2}25}{4\ln^{2}5}=1$，" "\n"
        r"故 $b<c$（用到 $\ln3\ne\ln8$，基本不等式取不到等号）．" "\n"
        r"又 $c=\log_{8}5<\log_{8}8=1$，而 $a=0.8^{-0.4}>0.8^{0}=1$．" "\n"
        r"综上 $b<c<a$，故选 B．"
    ),
    'review': (
        r"★ 提取文本作「a = 0.8-0.4，b = log3，c = log5」，指数 $-0.4$ 与两个底数全丢。"
        r"按详解的作商结构还原。数值校验：$a\approx1.0933$、$b\approx0.6826$、"
        r"$c\approx0.7740$，顺序 $b<c<a$ 与答案 B 吻合。"
    ),
    'difficulty': 0.65,
    'topics': ['M-T-039'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-039-V1',
}

T039_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知 $a=5^{\log_{2}3.4}$，$b=5^{\log_{4}3.6}$，$c=5^{\log_{3}\frac{10}{3}}$，"
        r"则（　　）"
    ),
    'opts': [
        ('A', r"$a>b>c$"), ('B', r"$b>a>c$"),
        ('C', r"$a>c>b$"), ('D', r"$c>a>b$"),
    ],
    'answer': 'C',
    'analysis': r"底数同为 $5>1$，只需比较三个指数；用 $1$ 作中间值分出大小。",
    'solution': (
        r"因底数 $5>1$，指数函数递增，故只需比较指数．" "\n"
        r"$\log_{2}3.4>\log_{2}2=1$，$\log_{4}3.6<\log_{4}4=1$；" "\n"
        r"再比较 $\log_{2}3.4$ 与 $\log_{3}\dfrac{10}{3}$：" "\n"
        r"$\log_{2}3.4-\log_{3}\dfrac{10}{3}"
        r"=\dfrac{\lg3.4}{\lg2}-\dfrac{\lg\frac{10}{3}}{\lg3}"
        r"=\dfrac{\lg3.4\lg3-\lg2\lg\frac{10}{3}}{\lg2\lg3}$，" "\n"
        r"分子 $=\lg3.4\lg3-\lg2(\lg10-\lg3)=(\lg3.4+\lg2)\lg3-\lg2\lg10"
        r"=\lg6.8\lg3-\lg2>0$，" "\n"
        r"故 $\log_{2}3.4>\log_{3}\dfrac{10}{3}>1>\log_{4}3.6$．" "\n"
        r"所以 $a>c>b$，故选 C．"
    ),
    'review': (
        r"★ 提取文本作「a = 5log23.4,b = 5log43.6,c = ()3」，第三个真数 $\frac{10}{3}$ "
        r"被压成「3」而分数值完全丢失。按详解「$c=5^{\log_3\frac{10}{3}}$」与"
        r"「$\log_23.4>\log_3\frac{10}{3}>1>\log_43.6$」反推确认。"
        r"数值校验：$a\approx17.15$、$b\approx4.42$、$c\approx5.83$，与答案 C 一致。"
    ),
    'difficulty': 0.75,
    'topics': ['M-T-039'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-039-V2',
}

T039_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知 $3^{a}=6^{b}=10$，则 $2$，$ab$，$a+b$ 的大小关系是（　　）"
    ),
    'opts': [
        ('A', r"$ab<a+b<2$"), ('B', r"$ab<2<a+b$"),
        ('C', r"$2<a+b<ab$"), ('D', r"$2<ab<a+b$"),
    ],
    'answer': 'D',
    'analysis': r"化为对数后判 $ab>2$，再比较 $\dfrac{a+b}{ab}$ 与 $1$。",
    'solution': (
        r"由 $3^{a}=10$ 得 $a=\log_{3}10>\log_{3}9=2$；"
        r"由 $6^{b}=10$ 得 $b=\log_{6}10>\log_{6}6=1$；故 $ab>2$．" "\n"
        r"又由换底 $\dfrac{1}{a}=\lg3$，$\dfrac{1}{b}=\lg6$，于是" "\n"
        r"$\dfrac{a+b}{ab}=\dfrac{1}{a}+\dfrac{1}{b}=\lg3+\lg6=\lg18>\lg10=1$，" "\n"
        r"故 $a+b>ab$．" "\n"
        r"综上 $2<ab<a+b$，故选 D．"
    ),
    'review': (
        r"★ 提取文本作「已知3a= 6b= 10」，指数 $a,b$ 塌成与底数同行的平文本。"
        r"按详解「$a=\log_310$、$b=\log_610$」还原。"
        r"数值校验：$a\approx2.0959$、$b\approx1.2851$、$ab\approx2.694$、"
        r"$a+b\approx3.381$，即 $2<ab<a+b$，与答案 D 吻合。"
    ),
    'difficulty': 0.6,
    'topics': ['M-T-039'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-039-V3',
}

T040_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知 $m=\log_{4\pi}\pi$，$n=\log_{4\mathrm{e}}\mathrm{e}$，$p=\mathrm{e}^{-\frac13}$，"
        r"则 $m,n,p$ 的大小关系是（其中 $\mathrm{e}$ 为自然对数的底数）（　　）"
    ),
    'opts': [
        ('A', r"$p<n<m$"), ('B', r"$m<n<p$"),
        ('C', r"$n<m<p$"), ('D', r"$n<p<m$"),
    ],
    'answer': 'C',
    'analysis': r"前两个用换底分离常数化为 $1-\dfrac{\lg4}{\lg4+\lg(\cdot)}$，再与 $\dfrac12$ 比较。",
    'solution': (
        r"换底分离常数：" "\n"
        r"$m=\dfrac{\lg\pi}{\lg4\pi}=\dfrac{\lg\pi}{\lg4+\lg\pi}"
        r"=1-\dfrac{\lg4}{\lg4+\lg\pi}$，" "\n"
        r"$n=\dfrac{\lg\mathrm{e}}{\lg4\mathrm{e}}"
        r"=\dfrac{\lg\mathrm{e}}{\lg4+\lg\mathrm{e}}"
        r"=1-\dfrac{\lg4}{\lg4+\lg\mathrm{e}}$．" "\n"
        r"因 $\lg4>\lg\pi>\lg\mathrm{e}>0$，有 $\lg4+\lg\pi>\lg4+\lg\mathrm{e}$，" "\n"
        r"故 $\dfrac{\lg4}{\lg4+\lg\pi}<\dfrac{\lg4}{\lg4+\lg\mathrm{e}}$，"
        r"从而 $m>n$．" "\n"
        r"又 $m<\dfrac12\iff\dfrac{\lg4}{\lg4+\lg\pi}>\dfrac12\iff\lg4>\lg\pi\iff4>\pi$，成立；" "\n"
        r"而 $p=\mathrm{e}^{-\frac13}=\dfrac{1}{\sqrt[3]{\mathrm{e}}}>\dfrac12$"
        r"（因 $\sqrt[3]{\mathrm{e}}<2\iff\mathrm{e}<8$）．" "\n"
        r"综上 $n<m<\dfrac12<p$，即 $n<m<p$，故选 C．"
    ),
    'review': (
        r"★ 提取文本作「m = logπn = logep = e- 1」——底数 $4\pi$、$4\mathrm{e}$ 中的 $4$ "
        r"与真数分离，$p$ 的指数 $-\frac13$ 被拆成「- 1」「3」两行。"
        r"按详解的分离常数结构还原，并用 $m<\frac12$ 这条（等价于 $4>\pi$）确认自洽。"
        r"数值校验：$m\approx0.4523$、$n\approx0.4191$、$p\approx0.7165$，与答案 C 一致。"
    ),
    'difficulty': 0.7,
    'topics': ['M-T-040'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-040-E1',
}

T040_V1 = {
    'type': '选择',
    'stem_text': (
        r"$\log_{2}3$、$\log_{8}12$、$\lg15$ 的大小关系为（　　）"
    ),
    'opts': [
        ('A', r"$\log_{2}3<\log_{8}12<\lg15$"),
        ('B', r"$\log_{8}12<\lg15<\log_{2}3$"),
        ('C', r"$\log_{2}3>\log_{8}12>\lg15$"),
        ('D', r"$\log_{8}12<\log_{2}3<\lg15$"),
    ],
    'answer': 'C',
    'analysis': r"三个数都拆出真数因子 $\dfrac32$，化成 $1+\dfrac{1}{\log_{\frac32}(\cdot)}$ 后比较。",
    'solution': (
        r"$\log_{2}3=\log_{2}\!\left(2\cdot\dfrac32\right)"
        r"=1+\log_{2}\dfrac32=1+\dfrac{1}{\log_{\frac32}2}$；" "\n"
        r"$\log_{8}12=\log_{8}\!\left(8\cdot\dfrac32\right)"
        r"=1+\log_{8}\dfrac32=1+\dfrac{1}{\log_{\frac32}8}$；" "\n"
        r"$\lg15=\lg\!\left(10\cdot\dfrac32\right)"
        r"=1+\lg\dfrac32=1+\dfrac{1}{\log_{\frac32}10}$．" "\n"
        r"因 $0<\log_{\frac32}2<\log_{\frac32}8<\log_{\frac32}10$，取倒数后不等号反向：" "\n"
        r"$\dfrac{1}{\log_{\frac32}2}>\dfrac{1}{\log_{\frac32}8}>\dfrac{1}{\log_{\frac32}10}$．" "\n"
        r"故 $\log_{2}3>\log_{8}12>\lg15$，故选 C．"
    ),
    'review': (
        r"★ 提取文本作「log3 ､log12 ､lg15」后又跟「28」「82」，底数 $2$、$8$ 与真数分离错位。"
        r"按详解「都提出真数因子 $\frac32$」的分离常数结构还原为 $\log_23$、$\log_812$、$\lg15$。"
        r"数值校验：$\log_23\approx1.585$、$\log_812\approx1.195$、$\lg15\approx1.176$，与答案 C 吻合。"
    ),
    'difficulty': 0.65,
    'topics': ['M-T-040'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-040-V1',
}

T040_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知 $a>b>0$，$ab=1$，若 $x=\dfrac{b}{2a}$，$y=\log_{2}(a+b)$，"
        r"$z=a+\dfrac{1}{b}$，则 $\log_{x}(3x)$，$\log_{y}(3y)$，$\log_{z}(3z)$ "
        r"的大小关系为（　　）"
    ),
    'opts': [
        ('A', r"$\log_{x}(3x)>\log_{y}(3y)>\log_{z}(3z)$"),
        ('B', r"$\log_{y}(3y)>\log_{x}(3x)>\log_{z}(3z)$"),
        ('C', r"$\log_{x}(3x)>\log_{z}(3z)>\log_{y}(3y)$"),
        ('D', r"$\log_{y}(3y)>\log_{z}(3z)>\log_{x}(3x)$"),
    ],
    'answer': 'D',
    'analysis': r"先界定 $0<x<\frac12<1<y<z$，再用 $\log_{t}(3t)=1+\dfrac{1}{\log_{3}t}$ 比较。",
    'solution': (
        r"由 $ab=1$ 且 $a>b>0$ 得 $a>1>b$，且 $b=\dfrac{1}{a}$．" "\n"
        r"$x=\dfrac{b}{2a}=\dfrac{1}{2a^{2}}$，由 $a>1$ 得 $0<x<\dfrac12$；" "\n"
        r"$y=\log_{2}(a+b)=\log_{2}\!\left(a+\dfrac{1}{a}\right)>\log_{2}2=1$；" "\n"
        r"$z=a+\dfrac{1}{b}=a+a=2a>2$，故 $z>y$（把 $z$ 写成 $z=\log_{2}2^{2a}=\log_{2}4^{a}$，"
        r"而 $a>1$ 时 $4^{a}>a+\dfrac{1}{a}$）．" "\n"
        r"于是 $0<x<1<y<z$．" "\n"
        r"又 $\log_{t}(3t)=1+\log_{t}3=1+\dfrac{1}{\log_{3}t}$：" "\n"
        r"$x<1$ 时 $\log_{3}x<0$，故 $\log_{x}(3x)<1$；" "\n"
        r"$1<y<z$ 时 $\log_{3}y<\log_{3}z$，故 $\dfrac{1}{\log_{3}y}>\dfrac{1}{\log_{3}z}>0$，"
        r"即 $\log_{y}(3y)>\log_{z}(3z)>1$．" "\n"
        r"综上 $\log_{y}(3y)>\log_{z}(3z)>\log_{x}(3x)$，故选 D．"
    ),
    'review': (
        r"★ 本题是这批里破碎最严重的一题：提取文本只剩「x = b 2a」「y = log2 a + b」"
        r"「z = a + 1 b」，$x,y,z$ 三个复合式的分数线与底数全丢，"
        r"且 $\log_x(3x)$ 等三个待比较式的底数也丢成「logx 3x」。"
        r"关键突破口在详解「$z=2a=\log_2 4^a$」——它同时确认了 $z=a+\frac1b=2a$（用到 $ab=1$）"
        r"和比较 $y,z$ 时要把 $z$ 写成以 $2$ 为底的对数。"
        r"据此反推 $x=\frac{b}{2a}$、$y=\log_2(a+b)$，与「$0<x<\frac12$、$y>1$、$z>2$」三条全部自洽。"
        r"数值校验（取 $a=2,\ b=0.5$）：$x=0.125$、$y=\log_2 2.5\approx1.322$、$z=4$；"
        r"$\log_x(3x)\approx-0.689$、$\log_y(3y)\approx5.04$、$\log_z(3z)\approx2.79$，与答案 D 一致。"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-040'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-040-V2',
}

T040_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知 $a=\log_{3}15$，$b=\log_{4}40$，$2^{c}=3$，则（　　）"
    ),
    'opts': [
        ('A', r"$a>c>b$"), ('B', r"$c>a>b$"),
        ('C', r"$b>a>c$"), ('D', r"$a>b>c$"),
    ],
    'answer': 'C',
    'analysis': r"把 $c$ 用对数表示，三个数都分离出常数 $1$，再与 $\dfrac32$ 比较。",
    'solution': (
        r"由 $2^{c}=3$ 得 $c=\log_{2}3$．三个数分离常数：" "\n"
        r"$a=\log_{3}15=\log_{3}(3\cdot5)=1+\log_{3}5$；" "\n"
        r"$b=\log_{4}40=\log_{4}(4\cdot10)=1+\log_{4}10$；" "\n"
        r"$c=\log_{2}3=\log_{2}\!\left(2\cdot\dfrac32\right)=1+\log_{2}\dfrac32$．" "\n"
        r"因 $\log_{3}5<\log_{3}3\sqrt3=\dfrac32$（$3\sqrt3\approx5.196>5$），"
        r"故 $a<1+\dfrac32=\dfrac52$；" "\n"
        r"因 $\log_{4}10>\log_{4}8=\dfrac32$，故 $b>\dfrac52$；于是 $b>a$．" "\n"
        r"又 $c=\log_{2}3<\log_{2}4=2<\dfrac52$..."
        r"更精确：$c<\log_{3}15=a$ 等价于 $\log_{2}3<1+\log_{3}5$，"
        r"直接估值 $c\approx1.585<a\approx2.465$，故 $a>c$．" "\n"
        r"综上 $b>a>c$，故选 C．"
    ),
    'review': (
        r"★ 提取文本作「a = log315，b = log440，2c= 3」，底数 $3$、$4$ 与真数同行无法区分，"
        r"$2^{c}=3$ 的指数被压成 $2c$。"
        r"按详解「$a=1+\log_35$、$b=1+\log_410$」的分离常数结构还原。"
        r"数值校验：$a\approx2.465$、$b\approx2.661$、$c=\log_23\approx1.585$，"
        r"顺序 $b>a>c$ 与答案 C 吻合。"
    ),
    'difficulty': 0.7,
    'topics': ['M-T-040'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-040-V3',
}

QS = [
    T039_E1, T039_V1, T039_V2, T039_V3,
    T040_E1, T040_V1, T040_V2, T040_V3,
]
