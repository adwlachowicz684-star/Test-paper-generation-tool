# -*- coding: utf-8 -*-
r"""第14批（上）：T041 构造函数 lnx/x 型比较大小，共 6 题。

来源：2024高中数学热点题型归纳完整解析版.pdf 专题2-1 p14（PDF 页 13）

## 这批的核心方法

全部用同一个函数：

    f(x) = lnx/x，f'(x) = (1-lnx)/x²

- 0 < x < e 时 f 递增；x > e 时 f 递减
- x = e 处取最大值 1/e
- 比较 f(m)、f(n) 时，把两边同乘一个正数化成 f 的形式即可

**录入要点**：把 a,b,c 化成 f(某个自变量)，比的是自变量到 e 的距离。
例如 E1 里 a = (4-ln4)/e² = f(e²/2)，因为
ln(e²/2) = 2-ln2，(e²/2) 的分母乘上去正好得原式。

## 破碎情况

这 6 题的分数全部塌成平文本（ref_bank 里是「a = 4 - ln4 e2 」这种），
根号、分数线、上标全靠 pdf2latex.py 的字号/基线重建 + 详解反推。
每题的 review 都记了依据链。

**V3 有原书答案争议**，见该题 review，按原书答案录入并标注存疑。

LaTeX 一律 raw 双引号 r"..."；中文行文用弯引号“”，不用 ASCII 双引号。
"""

T041_E1 = {
    'type': '选择',
    'stem_text': (
        r"设 $a=\dfrac{4-\ln4}{\mathrm{e}^{2}}$，$b=\dfrac{1}{\mathrm{e}}$，"
        r"$c=\dfrac{\ln2}{2}$，则 $a,b,c$ 的大小关系为（　　）"
    ),
    'opts': [
        ('A', r"$a<c<b$"), ('B', r"$c<a<b$"),
        ('C', r"$a<b<c$"), ('D', r"$b<a<c$"),
    ],
    'answer': 'B',
    'analysis': (
        r"构造 $f(x)=\dfrac{\ln x}{x}$，把三个数都化成 $f$ 的函数值："
        r"$a=f\!\left(\dfrac{\mathrm{e}^{2}}{2}\right)$、$b=f(\mathrm{e})$、"
        r"$c=f(2)=f(4)$，再按单调性比较。"
    ),
    'solution': (
        r"设 $f(x)=\dfrac{\ln x}{x}$，则 $f'(x)=\dfrac{1-\ln x}{x^{2}}$．" "\n"
        r"当 $x\in(1,\mathrm{e})$ 时 $f'(x)>0$，$f(x)$ 单调递增；"
        r"当 $x\in(\mathrm{e},+\infty)$ 时 $f'(x)<0$，$f(x)$ 单调递减．" "\n"
        r"化形：" "\n"
        r"$a=\dfrac{4-\ln4}{\mathrm{e}^{2}}"
        r"=\dfrac{\ln\mathrm{e}^{4}-\ln4}{\mathrm{e}^{2}}"
        r"=\dfrac{\ln\frac{\mathrm{e}^{4}}{4}}{\mathrm{e}^{2}}"
        r"=\dfrac{2\ln\frac{\mathrm{e}^{2}}{2}}{\mathrm{e}^{2}}"
        r"=\dfrac{\ln\frac{\mathrm{e}^{2}}{2}}{\frac{\mathrm{e}^{2}}{2}}"
        r"=f\!\left(\dfrac{\mathrm{e}^{2}}{2}\right)$；" "\n"
        r"$b=\dfrac{1}{\mathrm{e}}=\dfrac{\ln\mathrm{e}}{\mathrm{e}}=f(\mathrm{e})$；" "\n"
        r"$c=\dfrac{\ln2}{2}=f(2)$，又 $\dfrac{\ln4}{4}=\dfrac{2\ln2}{4}=\dfrac{\ln2}{2}$，"
        r"故 $c=f(4)$．" "\n"
        r"由 $\mathrm{e}<\dfrac{\mathrm{e}^{2}}{2}<4$（$\mathrm{e}\approx2.718$，"
        r"$\dfrac{\mathrm{e}^{2}}{2}\approx3.694$），且 $f$ 在 $(\mathrm{e},+\infty)$ 上递减，"
        r"得 $f\!\left(\dfrac{\mathrm{e}^{2}}{2}\right)>f(4)$，即 $a>c$；" "\n"
        r"又 $f(\mathrm{e})$ 为最大值，故 $b>a$．" "\n"
        r"综上 $b>a>c$，故选 B．"
    ),
    'review': (
        r"★ 提取文本作「a = 4 - ln4 e2 」，分数线与 $\mathrm{e}^2$ 的上标全丢。"
        r"由详解「$a=f(\frac{\mathrm{e}^2}{2})$、$b=f(\mathrm{e})$、$c=f(2)=f(4)$」"
        r"与「$\mathrm{e}<\frac{\mathrm{e}^2}{2}<4$」反推确认。"
        r"数值校验：$a\approx0.35373$、$b\approx0.36788$、$c\approx0.34657$，与答案 B 吻合。"
    ),
    'difficulty': 0.7,
    'topics': ['M-T-041'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-041-E1',
}

T041_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知 $a=3\pi\ln2$，$b=2\pi\ln3$，$c=6\ln\pi$，"
        r"则下列选项正确的是（　　）"
    ),
    'opts': [
        ('A', r"$a>b>c$"), ('B', r"$c>a>b$"),
        ('C', r"$c>b>a$"), ('D', r"$b>c>a$"),
    ],
    'answer': 'D',
    'analysis': r"三个数同除以 $6\pi$，转化为比较 $\dfrac{\ln2}{2}$、$\dfrac{\ln3}{3}$、$\dfrac{\ln\pi}{\pi}$。",
    'solution': (
        r"因 $6\pi>0$，比较 $a,b,c$ 等价于比较 $\dfrac{a}{6\pi}$、$\dfrac{b}{6\pi}$、$\dfrac{c}{6\pi}$：" "\n"
        r"$\dfrac{a}{6\pi}=\dfrac{3\pi\ln2}{6\pi}=\dfrac{\ln2}{2}=f(2)$，" "\n"
        r"$\dfrac{b}{6\pi}=\dfrac{2\pi\ln3}{6\pi}=\dfrac{\ln3}{3}=f(3)$，" "\n"
        r"$\dfrac{c}{6\pi}=\dfrac{6\ln\pi}{6\pi}=\dfrac{\ln\pi}{\pi}=f(\pi)$，"
        r"其中 $f(x)=\dfrac{\ln x}{x}$．" "\n"
        r"由 $f'(x)=\dfrac{1-\ln x}{x^{2}}$ 知 $f$ 在 $(\mathrm{e},+\infty)$ 上递减，"
        r"而 $\mathrm{e}<3<\pi$，故 $f(3)>f(\pi)$，即 $b>c$；" "\n"
        r"又 $f(2)=f(4)$（$\dfrac{\ln4}{4}=\dfrac{\ln2}{2}$），且 $4>\pi$，"
        r"故 $f(\pi)>f(4)=f(2)$，即 $c>a$．" "\n"
        r"综上 $b>c>a$，故选 D．"
    ),
    'review': (
        r"★ 提取文本作「a = 3ln2π，b = 2ln3π，c = 3lnπ2」，系数与真数错位，"
        r"极易误读成 $3\ln(2\pi)$、$2\ln(3\pi)$、$3\ln(\pi^2)$。"
        r"由详解「同除 $6\pi$ 后转化为 $\frac{\ln2}{2}$、$\frac{\ln3}{3}$、$\frac{\ln\pi}{\pi}$」"
        r"反推：$a=6\pi\cdot\frac{\ln2}{2}=3\pi\ln2$，$b=6\pi\cdot\frac{\ln3}{3}=2\pi\ln3$，"
        r"$c=6\pi\cdot\frac{\ln\pi}{\pi}=6\ln\pi$。"
        r"数值校验：$a\approx6.5328$、$b\approx6.9028$、$c\approx6.8684$，与答案 D 一致。"
    ),
    'difficulty': 0.7,
    'topics': ['M-T-041'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-041-V1',
}

T041_V2 = {
    'type': '选择',
    'stem_text': (
        r"以下四个数中，最大的是（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac{\ln3}{3}$"),
        ('B', r"$\dfrac{1}{\mathrm{e}}$"),
        ('C', r"$\dfrac{\ln\pi}{\pi}$"),
        ('D', r"$\dfrac{\ln15}{15}$"),
    ],
    'answer': 'B',
    'analysis': (
        r"四个数分别是 $f(3)$、$f(\mathrm{e})$、$f(\pi)$、$f(15)$，"
        r"其中 $f(x)=\dfrac{\ln x}{x}$ 在 $x=\mathrm{e}$ 处取最大值。"
    ),
    'solution': (
        r"设 $f(x)=\dfrac{\ln x}{x}$，则 $f'(x)=\dfrac{1-\ln x}{x^{2}}$．" "\n"
        r"当 $0<x<\mathrm{e}$ 时 $f'(x)>0$，$f$ 递增；当 $x>\mathrm{e}$ 时 $f'(x)<0$，$f$ 递减，"
        r"故 $f(\mathrm{e})=\dfrac{1}{\mathrm{e}}$ 为最大值．" "\n"
        r"四个数依次为 $f(3)$、$f(\mathrm{e})$、$f(\pi)$、$f(15)$，"
        r"由 $\mathrm{e}<3<\pi<15$ 及 $f$ 在 $(\mathrm{e},+\infty)$ 上递减，"
        r"得 $f(\mathrm{e})>f(3)>f(\pi)>f(15)$．" "\n"
        r"故最大的是 $\dfrac{1}{\mathrm{e}}$，故选 B．"
    ),
    'review': (
        r"★ 提取文本只剩「以下四个数中，最大的是」，四个选项的分数全部塌成平文本"
        r"（ref_bank 中该题 stem 无选项内容）。"
        r"由详解「$\frac{1}{\mathrm{e}}>\frac{\ln3}{3}>\frac{\ln\pi}{\pi}>\frac{\ln15}{15}$，故选 B」"
        r"还原四个选项。"
        r"数值校验：$\frac{\ln3}{3}\approx0.36620$、$\frac1{\mathrm{e}}\approx0.36788$、"
        r"$\frac{\ln\pi}{\pi}\approx0.36438$、$\frac{\ln15}{15}\approx0.18054$，与答案 B 吻合。"
    ),
    'difficulty': 0.65,
    'topics': ['M-T-041'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-041-V2',
}

T041_V3 = {
    'type': '选择',
    'stem_text': (
        r"下列命题为真命题的个数是（　　）" "\n"
        r"① $\ln3<\sqrt{3}\ln2$； ② $\ln\pi<\dfrac{\pi}{\mathrm{e}}$；"
        r" ③ $2^{\sqrt{15}}<15$； ④ $3\mathrm{e}\ln2<4\sqrt{2}$"
    ),
    'opts': [
        ('A', r"$1$ 个"), ('B', r"$2$ 个"),
        ('C', r"$3$ 个"), ('D', r"$4$ 个"),
    ],
    'answer': 'C',
    'analysis': (
        r"统一用 $f(x)=\dfrac{\ln x}{x}$ 处理："
        r"① 化为 $f(\sqrt3)<f(2)$；② 化为 $f(\pi)<f(\mathrm{e})$；"
        r"③ 化为比较 $\dfrac{\ln2}{?}$ 与 $\dfrac{\ln15}{?}$；④ 利用 $f$ 的最大值 $\dfrac1{\mathrm{e}}$。"
    ),
    'solution': (
        r"设 $f(x)=\dfrac{\ln x}{x}$，则 $f'(x)=\dfrac{1-\ln x}{x^{2}}$．" "\n"
        r"当 $0<x<\mathrm{e}$ 时 $f'(x)>0$，$f$ 递增；当 $x>\mathrm{e}$ 时 $f'(x)<0$，$f$ 递减，"
        r"当 $x=\mathrm{e}$ 时 $f$ 取最大值 $\dfrac{1}{\mathrm{e}}$．" "\n"
        r"① $\ln3<\sqrt3\ln2\iff\dfrac{\ln3}{\sqrt3}<\ln2"
        r"\iff\dfrac{\ln\sqrt3}{\sqrt3}<\dfrac{\ln2}{2}"
        r"\iff f(\sqrt3)<f(2)$；" "\n"
        r"由 $\sqrt3<2<\mathrm{e}$ 且 $f$ 在 $(0,\mathrm{e})$ 上递增，得 $f(\sqrt3)<f(2)$，故①为真；" "\n"
        r"② $\ln\pi<\dfrac{\pi}{\mathrm{e}}\iff\dfrac{\ln\pi}{\pi}<\dfrac{1}{\mathrm{e}}"
        r"\iff f(\pi)<f(\mathrm{e})$；" "\n"
        r"由 $\mathrm{e}<\pi$ 且 $f$ 在 $(\mathrm{e},+\infty)$ 上递减，得 $f(\pi)<f(\mathrm{e})$，故②为真；" "\n"
        r"③ $2^{\sqrt{15}}<15\iff\sqrt{15}\ln2<\ln15"
        r"\iff\dfrac{\ln2}{\sqrt{15}}<\dfrac{\ln15}{15}$，"
        r"由 $f(16)<f(15)$（$15<16$ 且均在 $(\mathrm{e},+\infty)$ 上）"
        r"得 $\dfrac{\ln2}{4}<\dfrac{\ln15}{15}$，而 $\dfrac{\ln2}{\sqrt{15}}<\dfrac{\ln2}{4}$"
        r"（因 $\sqrt{15}<4$），故③为真；" "\n"
        r"④ $3\mathrm{e}\ln2<4\sqrt2\iff\dfrac{\ln8}{4\sqrt2}<\dfrac{1}{\mathrm{e}}$，"
        r"而 $\dfrac{\ln8}{4\sqrt2}=\dfrac{\ln\sqrt8}{\sqrt8}\cdot\dfrac{\sqrt8}{4\sqrt2}\cdot 2"
        r"<\dfrac{1}{\mathrm{e}}$（用到 $f(x)\leqslant\dfrac1{\mathrm{e}}$），故④为真．" "\n"
        r"**原书判定②为假、共 $3$ 个真命题，故选 C。**"
    ),
    'review': (
        r"★ **本题存在原书答案争议，按原书 C 录入，标记为存疑。**" "\n"
        r"数值验证四个命题分别为：" "\n"
        r"① $\ln3\approx1.098612<\sqrt3\ln2\approx1.200566$ → 真；" "\n"
        r"② $\ln\pi\approx1.144730<\pi/\mathrm{e}\approx1.155727$ → **真**；" "\n"
        r"③ $2^{\sqrt{15}}\approx14.6516<15$ → 真；" "\n"
        r"④ $3\mathrm{e}\ln2\approx5.652508<4\sqrt2\approx5.656854$ → 真．" "\n"
        r"四个命题数值上全部成立，真命题应为 $4$ 个（选 D），与原书答案 C（$3$ 个）矛盾。" "\n"
        r"原书详解判②为假，依据是「由 $\mathrm{e}<\pi$ 可得 $f(\mathrm{e})<f(\pi)$」，"
        r"但 $f(\mathrm{e})=\frac1{\mathrm{e}}$ 是 $f$ 的最大值，必有 $f(\mathrm{e})>f(\pi)$，"
        r"**该处不等号方向写反了**，据此得出的「②为假」不成立。" "\n"
        r"另注：详解中「由 $f(16)<f(15)$ 可得 $f(2)<f(15)$」同样写反"
        r"（实际 $f(2)\approx0.3466>f(15)\approx0.1805$）。" "\n"
        r"因③的具体形式（$2^{\sqrt{15}}$ 的上标含矢量绘制的根号）无法从破碎文本"
        r"百分百确认（若实为 $2^{15}<15$ 则③为假，此时真命题恰为 $3$ 个、答案 C 自洽），"
        r"故此处按原书答案 C 录入，留待复核。"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-041'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-041-V3',
}

T041_V4 = {
    'type': '选择',
    'stem_text': (
        r"（$2022$·天津三中三模）设 $a=\dfrac{3(2-\ln3)}{\mathrm{e}^{2}}$，"
        r"$b=\dfrac{1}{\mathrm{e}}$，$c=\dfrac{\ln2}{2}$，"
        r"则 $a,b,c$ 的大小顺序为（　　）"
    ),
    'opts': [
        ('A', r"$a<c<b$"), ('B', r"$c<a<b$"),
        ('C', r"$a<b<c$"), ('D', r"$b<a<c$"),
    ],
    'answer': 'B',
    'analysis': (
        r"构造 $f(x)=\dfrac{\ln x}{x}$，化得 $a=f\!\left(\dfrac{\mathrm{e}^{2}}{3}\right)$、"
        r"$b=f(\mathrm{e})$、$c=f(2)$，再比较自变量。"
    ),
    'solution': (
        r"设 $f(x)=\dfrac{\ln x}{x}$，则 $f'(x)=\dfrac{1-\ln x}{x^{2}}$．" "\n"
        r"当 $0<x<\mathrm{e}$ 时 $f'(x)>0$，$f$ 递增；当 $x>\mathrm{e}$ 时 $f'(x)<0$，$f$ 递减．" "\n"
        r"化形：$a=\dfrac{3(2-\ln3)}{\mathrm{e}^{2}}"
        r"=\dfrac{3(\ln\mathrm{e}^{2}-\ln3)}{\mathrm{e}^{2}}"
        r"=\dfrac{3\ln\frac{\mathrm{e}^{2}}{3}}{\mathrm{e}^{2}}"
        r"=\dfrac{\ln\frac{\mathrm{e}^{2}}{3}}{\frac{\mathrm{e}^{2}}{3}}"
        r"=f\!\left(\dfrac{\mathrm{e}^{2}}{3}\right)$；" "\n"
        r"$b=\dfrac{1}{\mathrm{e}}=f(\mathrm{e})$，$c=\dfrac{\ln2}{2}=f(2)$．" "\n"
        r"由 $2<\dfrac{\mathrm{e}^{2}}{3}<\mathrm{e}$（$\dfrac{\mathrm{e}^{2}}{3}\approx2.463$），"
        r"且 $f$ 在 $(0,\mathrm{e})$ 上递增，得 $f(2)<f\!\left(\dfrac{\mathrm{e}^{2}}{3}\right)<f(\mathrm{e})$．" "\n"
        r"故 $c<a<b$，故选 B．"
    ),
    'review': (
        r"★ 提取文本作「a = 3 2 - ln3  e2 」，分子是 $3(2-\ln3)$ 还是 $\frac32-\ln3$ 无法分辨。"
        r"由详解「$a=f(\frac{\mathrm{e}^2}{3})=\frac{3\ln(\mathrm{e}^2/3)}{\mathrm{e}^2}$」"
        r"确认为 $3(2-\ln3)$：$\ln(\mathrm{e}^2/3)=2-\ln3$，乘 $3$ 再除 $\mathrm{e}^2$ 正好还原。"
        r"数值校验：$a\approx0.36597$、$b\approx0.36788$、$c\approx0.34657$，与答案 B 吻合。"
        r"注意与 V5 的区别：V4 的 $c=\frac{\ln2}{2}$，V5 的 $c=\frac{\ln3}{3}$，其余相同。"
    ),
    'difficulty': 0.7,
    'topics': ['M-T-041'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-041-V4',
}

T041_V5 = {
    'type': '选择',
    'stem_text': (
        r"（$2022$·江苏·扬州中学高二期中）$a=\dfrac{3(2-\ln3)}{\mathrm{e}^{2}}$，"
        r"$b=\dfrac{1}{\mathrm{e}}$，$c=\dfrac{\ln3}{3}$，"
        r"则 $a,b,c$ 的大小顺序为（　　）"
    ),
    'opts': [
        ('A', r"$a<c<b$"), ('B', r"$c<a<b$"),
        ('C', r"$a<b<c$"), ('D', r"$b<a<c$"),
    ],
    'answer': 'A',
    'analysis': (
        r"$a=f\!\left(\dfrac{\mathrm{e}^{2}}{3}\right)$、$b=f(\mathrm{e})$、$c=f(3)$；"
        r"$b$ 最大无疑，$a$ 与 $c$ 需用「$f(x)=t$ 两解」的结论细比。"
    ),
    'solution': (
        r"设 $f(x)=\dfrac{\ln x}{x}$，则 $f'(x)=\dfrac{1-\ln x}{x^{2}}$，"
        r"$f$ 在 $(0,\mathrm{e})$ 上递增、在 $(\mathrm{e},+\infty)$ 上递减，"
        r"$x=\mathrm{e}$ 时取最大值 $\dfrac{1}{\mathrm{e}}$．" "\n"
        r"同 V4 化形得 $a=f\!\left(\dfrac{\mathrm{e}^{2}}{3}\right)$，"
        r"$b=f(\mathrm{e})=\dfrac{1}{\mathrm{e}}$，$c=f(3)=\dfrac{\ln3}{3}$．" "\n"
        r"因 $\dfrac{\mathrm{e}^{2}}{3}\approx2.463<\mathrm{e}<3$，且 $b=f(\mathrm{e})$ 为最大值，"
        r"故 $b$ 最大．" "\n"
        r"比较 $a$ 与 $c$：设 $f(x)=t$ 有两个解 $x_{1}<x_{2}$，则 $x_{1}<\mathrm{e}<x_{2}$．"
        r"构造 $g(x)=\ln x-\dfrac{2(x-1)}{x+1}$（$x>1$），由导数可得 $g(x)>0$，"
        r"从而 $\dfrac{\ln x_{2}-\ln x_{1}}{x_{2}-x_{1}}>\dfrac{2}{x_{1}+x_{2}}$，"
        r"取 $x_{1}=\dfrac{\mathrm{e}^{2}}{3}$、$x_{2}=3$ 即可判得 $f\!\left(\dfrac{\mathrm{e}^{2}}{3}\right)<f(3)$，"
        r"即 $a<c$．" "\n"
        r"综上 $a<c<b$，故选 A．"
    ),
    'review': (
        r"★ 与 V4 同型，仅 $c$ 不同（V4 是 $\frac{\ln2}{2}$，本题是 $\frac{\ln3}{3}$），"
        r"但答案从 B 变为 A —— 因为 $f(3)>f(2)$（$2<\mathrm{e}<3$，且 $3$ 离 $\mathrm{e}$ 更近）。"
        r"提取文本作「a = 3(2 - ln3) e2 ,b = 1 e ,c = ln3 3 」，分数全塌。"
        r"由详解「$a=f(\frac{\mathrm{e}^2}{3})$、$b=f(\mathrm{e})$、$c=f(3)$」还原。"
        r"数值校验：$a\approx0.365969$、$c\approx0.366204$、$b\approx0.367879$，"
        r"三者极接近（$a$ 与 $c$ 仅差 $0.00024$），普通估值无法分辨，"
        r"必须靠详解给出的 $g(x)=\ln x-\frac{2(x-1)}{x+1}$ 技巧，与答案 A 一致。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-041'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-041-V5',
}

QS = [
    T041_E1, T041_V1, T041_V2, T041_V3, T041_V4, T041_V5,
]
