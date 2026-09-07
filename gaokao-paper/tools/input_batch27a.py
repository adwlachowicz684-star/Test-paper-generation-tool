# -*- coding: utf-8 -*-
r"""第27批（上）：M-T-120 续 + M-T-121 + M-T-122（8题）

来源：2024高中数学热点题型归纳完整解析版.pdf 专题4 p086~p087（PDF 页 85~86）

## ★ 归属以 ref_bank 的 key 为准（这轮的重要修正）

上一批我按「页面顺序」猜 V 编号，**归错了**。
正确做法是直接查 `data/ref_bank.json` 的键名，它是权威归属：

```python
python3 -c "
import json
rb=json.load(open('data/ref_bank.json',encoding='utf-8'))
for k,q in rb.items():
    if str(q.get('orig_num')) in ('24','25','26','27','28','29','30','31'):
        print(k, q.get('orig_num'), (q.get('stem') or '')[:40])
"
```

本批 8 题的 key 全部据此确定。**以后每批都先查 key，不要凭页码猜。**

## 本批题型套路速查

| 题 | 构造 | 关键 |
|---|---|---|
| M-T-120-V2 | $g=\frac{\ln(x+1)}{f(x)}$ | 商的导数，分子是 $\frac{f}{x+1}-f'\ln(x+1)$ |
| M-T-120-V3 | $g=f(x)\ln x$ | 积的导数 |
| M-T-121-V1 | $g=f(x)-\sqrt x$ | 题干根号被吞，实为 $\sqrt x f'(x)<\frac12$ |
| M-T-121-V2 | $g=\frac{xf(x)}{\mathrm e^{x}}$ | 分子 $f(x)-xf(x)+xf'(x)$ |
| M-T-121-V3 | $F=[f(x)-1]\mathrm e^{x}$ | 常数 1 的移项 |
| M-T-121-E1 | 先求解析式 $f=\mathrm e^{-x}+x^{2}+\mathrm e^{x}$ | 待定系数 |
| M-T-122-V1 | $g=xf(x)-x$ | 分 $x<1$、$x>1$、$x=1$ 讨论 |
| M-T-122-E1 | 二次构造 $\frac{f(x)}{\mathrm e^{x}}=x^{2}-x-1$ | 降次 |
"""

T120_V2 = {
    'type': '选择',
    'stem_text': (
        r"设定义在 $[0,+\infty)$ 上的函数 $f(x)\neq0$ 恒成立，其导函数为 $f'(x)$．"
        r"若 $\dfrac{f(x)}{x+1}-f'(x)\ln(x+1)<0$，则（　　）"
    ),
    'opts': [
        ('A', r"$2f(1)>f(3)>0$"),
        ('B', r"$2f(1)<f(3)<0$"),
        ('C', r"$2f(3)>f(1)>0$"),
        ('D', r"$2f(3)<f(1)<0$"),
    ],
    'answer': 'B',
    'analysis': (
        r"构造 $g(x)=\dfrac{\ln(x+1)}{f(x)}$，其导数分子恰是题干左边，故 $g$ 递减；"
        r"又 $g(0)=0$，得 $0>g(1)>g(3)$，解出 $f(1),f(3)$ 均负且 $f(3)>2f(1)$。"
    ),
    'solution': (
        r"**构造**：设 $g(x)=\dfrac{\ln(x+1)}{f(x)}$（$x\geqslant0$，$f(x)\neq0$）．「 」\n"
        r"$g'(x)=\dfrac{\frac1{x+1}\cdot f(x)-\ln(x+1)\cdot f'(x)}{f^{2}(x)}"
        r"=\dfrac{\frac{f(x)}{x+1}-f'(x)\ln(x+1)}{f^{2}(x)}<0$（分子即题干左边），「 」\n"
        r"故 $g$ 在 $[0,+\infty)$ 上**单调递减**．「 」\n"
        r"**定号**：$g(0)=\dfrac{\ln1}{f(0)}=0$，故 $0=g(0)>g(1)>g(3)$．「 」\n"
        r"$g(1)=\dfrac{\ln2}{f(1)}<0$，而 $\ln2>0$，故 **$f(1)<0$**；"
        r"同理 $g(3)=\dfrac{\ln4}{f(3)}<0$，$\ln4>0$，故 **$f(3)<0$**．「 」\n"
        r"**比较**：$g(1)>g(3)$ 即 $\dfrac{\ln2}{f(1)}>\dfrac{\ln4}{f(3)}$．「 」\n"
        r"两边同乘 $f(1)f(3)>0$（负×负为正），不等号不变：「 」\n"
        r"$\ln2\cdot f(3)>\ln4\cdot f(1)=2\ln2\cdot f(1)\Rightarrow f(3)>2f(1)$．「 」\n"
        r"故 $2f(1)<f(3)<0$，选 B．"
    ),
    'review': (
        r"★ 题干提取为「f x- x + 1f′ xln(x + 1)< 0」，分数线丢失；"
        r"由详解「$g'(x)=\frac{\frac{f(x)}{x+1}-f'(x)\ln(x+1)}{f^2(x)}<0$，"
        r"∵$[0,+\infty)$ 上 $\frac{f(x)}{x+1}-f'(x)\ln(x+1)<0$」还原为 "
        r"$\frac{f(x)}{x+1}-f'(x)\ln(x+1)<0$。「 」\n"
        r"**商的导数校验**：$\left(\frac{u}{v}\right)'=\frac{u'v-uv'}{v^2}$，"
        r"$u=\ln(x+1)$、$v=f(x)$ ⇒ $g'=\frac{\frac{f(x)}{x+1}-\ln(x+1)f'(x)}{f^2(x)}$ ✓ **与详解一致**。「 」\n"
        r"**⚠ 本题唯一易错点**：最后一步乘 $f(1)f(3)$。"
        r"必须先由 $g(1),g(3)<0$ 推出 $f(1),f(3)<0$，才能知道 $f(1)f(3)>0$、"
        r"**不等号不变向**。若跳过定号直接乘，会得到 $f(3)<2f(1)$，从而错选 D。"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-120'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-120-V2',
}

T120_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知定义在 $\mathbb R$ 上的连续奇函数 $f(x)$ 的导函数为 $f'(x)$．"
        r"已知 $f(1)\neq0$，且当 $x>0$ 时有 $x\ln x\cdot f'(x)<-f(x)$ 成立，"
        r"则使 $(x^{2}-4)f(x)>0$ 成立的 $x$ 的取值范围是（　　）"
    ),
    'opts': [
        ('A', r"$(-2,0)\cup(0,2)$"),
        ('B', r"$(-\infty,-2)\cup(0,2)$"),
        ('C', r"$(-2,0)\cup(2,+\infty)$"),
        ('D', r"$(-\infty,-2)\cup(2,+\infty)$"),
    ],
    'answer': 'B',
    'analysis': (
        r"构造 $g(x)=f(x)\ln x$（$x>0$），则 $g'(x)=\dfrac{x\ln x\,f'(x)+f(x)}x<0$；"
        r"由 $g(1)=0$ 与 $\ln x$ 的符号可定出 $f(x)$ 在 $(0,+\infty)$ 上恒负，"
        r"再由奇函数得 $x<0$ 时 $f(x)$ 恒正。"
    ),
    'solution': (
        r"**构造**：设 $g(x)=f(x)\ln x$（$x>0$）．「 」\n"
        r"$g'(x)=f'(x)\ln x+f(x)\cdot\dfrac1x=\dfrac{x\ln x\cdot f'(x)+f(x)}x$．「 」\n"
        r"由 $x\ln x\cdot f'(x)<-f(x)$ 得分子 $<0$，又 $x>0$，故 $g'(x)<0$，"
        r"$g$ 在 $(0,+\infty)$ 上**递减**．「 」\n"
        r"**定号**：$g(1)=f(1)\cdot\ln1=0$．「 」\n"
        r"· $0<x<1$：$g(x)>g(1)=0$，即 $f(x)\ln x>0$；此时 $\ln x<0$，故 $f(x)<0$；「 」\n"
        r"· $x>1$：$g(x)<g(1)=0$，即 $f(x)\ln x<0$；此时 $\ln x>0$，故 $f(x)<0$；「 」\n"
        r"· $x=1$：由 $f(1)\neq0$ 及连续性，结合上式得 $f(1)<0$．「 」\n"
        r"故在 $(0,+\infty)$ 上 **$f(x)<0$ 恒成立**．「 」\n"
        r"由 $f$ 为奇函数，在 $(-\infty,0)$ 上 **$f(x)>0$ 恒成立**．「 」\n"
        r"**解不等式** $(x^{2}-4)f(x)>0$：「 」\n"
        r"$\begin{cases}x^{2}-4>0\\ f(x)>0\end{cases}\Rightarrow\begin{cases}|x|>2\\ x<0\end{cases}"
        r"\Rightarrow x<-2$；「 」\n"
        r"$\begin{cases}x^{2}-4<0\\ f(x)<0\end{cases}\Rightarrow\begin{cases}|x|<2\\ x>0\end{cases}"
        r"\Rightarrow 0<x<2$．「 」\n"
        r"故 $x\in(-\infty,-2)\cup(0,2)$，选 B．"
    ),
    'review': (
        r"★ 题干完整（含 $x\ln x\cdot f'(x)<-f(x)$）✓，「 」\n"
        r"详解里 $g'(x)=f'(x)\ln x+\frac{f(x)}x=\frac{x\ln x f'(x)+f(x)}x$ 也完整 ✓。「 」\n"
        r"**两段定号是本题核心**（易漏 $x=1$ 处的讨论）：「 」\n"
        r"$0<x<1$ 与 $x>1$ 时 $\ln x$ 符号相反，但 $g(x)$ 相对 $g(1)=0$ 的大小也相反，"
        r"两个「相反」抵消，**两段都得到 $f(x)<0$** ✓。「 」\n"
        r"$x=1$ 处 $\ln x=0$ 无法直接判定，靠 $f(1)\neq0$ + 连续性：$f$ 在 $x=1$ 附近恒负，"
        r"故 $f(1)<0$ ✓。「 」\n"
        r"**答案校验**：B 是 $(-\infty,-2)\cup(0,2)$。"
        r"$x=-3$：$x^2-4=5>0$、$f(-3)>0$ ⇒ 积 $>0$ ✓；"
        r"$x=1$：$x^2-4=-3<0$、$f(1)<0$ ⇒ 积 $>0$ ✓ 在区间内；"
        r"$x=3$：$x^2-4=5>0$、$f(3)<0$ ⇒ 积 $<0$ ✗ 不在区间内 ✓。**B 正确**。"
    ),
    'difficulty': 0.9,
    'topics': ['M-T-120'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-120-V3',
}

T121_V1 = {
    'type': '选择',
    'stem_text': (
        r"定义在 $(0,+\infty)$ 上的函数 $f(x)$ 的导函数 $f'(x)$ 满足 "
        r"$\sqrt x\,f'(x)<\dfrac12$，则下列不等式中一定成立的是（　　）"
    ),
    'opts': [
        ('A', r"$f(9)-1<f(4)<f(1)+1$"),
        ('B', r"$f(1)+1<f(4)<f(9)-1$"),
        ('C', r"$f(5)+2<f(4)<f(1)-1$"),
        ('D', r"$f(1)-1<f(4)<f(5)+2$"),
    ],
    'answer': 'A',
    'analysis': (
        r"构造 $g(x)=f(x)-\sqrt x$，则 $g'(x)=f'(x)-\dfrac1{2\sqrt x}<0$，$g$ 递减；"
        r"由 $g(1)>g(4)>g(9)$ 即得。"
    ),
    'solution': (
        r"**构造**：设 $g(x)=f(x)-\sqrt x$（$x>0$）．「 」\n"
        r"$g'(x)=f'(x)-\dfrac1{2\sqrt x}=\dfrac{2\sqrt x\,f'(x)-1}{2\sqrt x}$．「 」\n"
        r"由 $\sqrt x\,f'(x)<\dfrac12$ 得 $2\sqrt x\,f'(x)<1$，分子 $<0$，"
        r"又 $2\sqrt x>0$，故 $g'(x)<0$，$g$ 在 $(0,+\infty)$ 上**递减**．「 」\n"
        r"**取点**：$g(1)>g(4)>g(9)$（注意 $\sqrt1=1$、$\sqrt4=2$、$\sqrt9=3$）：「 」\n"
        r"$f(1)-1>f(4)-2>f(9)-3$．「 」\n"
        r"由左半：$f(4)-2<f(1)-1\Rightarrow f(4)<f(1)+1$；「 」\n"
        r"由右半：$f(9)-3<f(4)-2\Rightarrow f(9)-1<f(4)$．「 」\n"
        r"合并得 $f(9)-1<f(4)<f(1)+1$，选 A．"
    ),
    'review': (
        r"★ **题干的根号是被吞掉的**：提取文本作「xf'(x) < 1/2」，"
        r"若按此读则构造 $f(x)-\frac12\ln x$ 之类，与选项（9,4,1 对应差值 1,2,3）对不上。「 」\n"
        r"由详解「设 $g(x)=f(x)-x$…$g'(x)=f'(x)-\frac1{2\sqrt x}=\frac{2\sqrt x f'(x)-1}{2\sqrt x}<0$，"
        r"故函数 $g(x)$ 在 $(0,+\infty)$ 上递减，所以 $g(1)>g(4)>g(9)$，"
        r"所以 $f(1)-1>f(4)-2>f(9)-3$，即 $f(9)-1<f(4)<f(1)+1$」"
        r"**反推题干必为 $\sqrt x f'(x)<\frac12$**，且构造是 $g(x)=f(x)-\sqrt x$。「 」\n"
        r"（详解里「设 $g(x)=f(x)-x$」是笔误或提取误差，"
        r"从其导数 $f'(x)-\frac1{2\sqrt x}$ 反推，构造只能是 $f(x)-\sqrt x$ ✓）「 」\n"
        r"**数值自洽**：选项用 $x=1,4,9$（$\sqrt x=1,2,3$），差值恰为 $1$，"
        r"与 $f(9)-1<f(4)<f(1)+1$ 中的 $\pm1$ 吻合 ✓。"
        r"若是 $f(x)-x$，则 $g(1)>g(4)>g(9)$ 给出 $f(1)-1>f(4)-4>f(9)-9$，"
        r"得不到选项里的 $\pm1$ ✗。**这条足以锁定构造是 $\sqrt x$**。"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-121'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-121-V1',
}

T121_V2 = {
    'type': '选择',
    'stem_text': (
        r"已知定义在 $(0,+\infty)$ 上的函数 $f(x)$ 的导函数为 $f'(x)$，"
        r"且满足 $(1-x)f(x)+xf'(x)>0$，则关于 $x$ 的不等式 "
        r"$f(2x-1)-\mathrm e^{x-3}f(x+2)<0$ 的解集为（　　）"
    ),
    'opts': [
        ('A', r"$\left(\dfrac12,3\right)$"),
        ('B', r"$(3,+\infty)$"),
        ('C', r"$(1,3)$"),
        ('D', r"$\left(\dfrac12,+\infty\right)$"),
    ],
    'answer': 'A',
    'analysis': (
        r"构造 $g(x)=\dfrac{xf(x)}{\mathrm e^{x}}$，则 "
        r"$g'(x)=\dfrac{f(x)-xf(x)+xf'(x)}{\mathrm e^{x}}>0$，$g$ 递增；"
        r"不等式化为 $g(2x-1)<g(x+2)$，再结合定义域 $2x-1>0$、$x+2>0$。"
    ),
    'solution': (
        r"**构造**：设 $g(x)=\dfrac{xf(x)}{\mathrm e^{x}}$（$x>0$）．「 」\n"
        r"$g'(x)=\dfrac{\bigl[f(x)+xf'(x)\bigr]\mathrm e^{x}-xf(x)\mathrm e^{x}}{\mathrm e^{2x}}"
        r"=\dfrac{f(x)-xf(x)+xf'(x)}{\mathrm e^{x}}$．「 」\n"
        r"题干条件 $(1-x)f(x)+xf'(x)>0$ 即 $f(x)-xf(x)+xf'(x)>0$，"
        r"故 $g'(x)>0$，$g$ 在 $(0,+\infty)$ 上**递增**．「 」\n"
        r"**化不等式**：原不等式化为 $g(2x-1)<g(x+2)$，即「 」\n"
        r"$\dfrac{(2x-1)f(2x-1)}{\mathrm e^{2x-1}}<\dfrac{(x+2)f(x+2)}{\mathrm e^{x+2}}$．「 」\n"
        r"$g$ 递增，故 $2x-1<x+2\Rightarrow x<3$．「 」\n"
        r"**定义域**：需 $2x-1>0$ 且 $x+2>0$，即 $x>\dfrac12$．「 」\n"
        r"综上 $\dfrac12<x<3$，选 A．"
    ),
    'review': (
        r"★ 题干与选项完整 ✓。构造由详解「设 $g(x)=\frac{xf(x)}{\mathrm e^x}$，"
        r"则 $g'(x)=\frac{[f(x)+xf'(x)]\mathrm e^x-xf(x)\mathrm e^x}{\mathrm e^{2x}}"
        r"=\frac{f(x)-xf(x)+xf'(x)}{\mathrm e^x}$，"
        r"∵$(1-x)f(x)+xf'(x)>0$，∴$g'(x)>0$」确认。「 」\n"
        r"**⚠ 题干与构造的衔接存疑（如实标注）**："
        r"由 $f(2x-1)<\mathrm e^{x-3}f(x+2)$ 严格推导，「 」\n"
        r"左边乘 $\frac{2x-1}{\mathrm e^{2x-1}}$ 后右边应为 $\frac{(2x-1)f(x+2)}{\mathrm e^{x+2}}$，"
        r"而非 $\frac{(x+2)f(x+2)}{\mathrm e^{x+2}}$（差一个因子 $\frac{2x-1}{x+2}$）。「 」\n"
        r"详解直接给出 $g(2x-1)<g(x+2)$，据此得 $2x-1<x+2\Rightarrow x<3$，"
        r"加上定义域 $x>\frac12$ 得 $(\frac12,3)$，与答案 A 一致 ✓。「 」\n"
        r"**按详解与答案录入**，此处题干的 $\mathrm e^{x-3}$ 系数可能有印刷/提取误差，"
        r"已在 solution 中按标准思路（比较 $g$ 值 + 定义域）呈现。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-121'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-121-V2',
}

T121_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知函数 $f(x)$ 为 $\mathbb R$ 上的可导函数，其导函数为 $f'(x)$，"
        r"且满足 $f(x)+f'(x)<1$ 恒成立，$f(0)=2019$，"
        r"则不等式 $f(x)<2018\mathrm e^{-x}+1$ 的解集为（　　）"
    ),
    'opts': [
        ('A', r"$(0,+\infty)$"),
        ('B', r"$(-\infty,0)$"),
        ('C', r"$(\mathrm e,+\infty)$"),
        ('D', r"$(-\infty,\mathrm e)$"),
    ],
    'answer': 'A',
    'analysis': (
        r"把常数 $1$ 移进构造：$F(x)=[f(x)-1]\mathrm e^{x}$，"
        r"则 $F'=[f+f'-1]\mathrm e^{x}<0$，$F$ 递减；"
        r"不等式化为 $F(x)<2018=F(0)$。"
    ),
    'solution': (
        r"**构造**：由 $f(x)+f'(x)-1<0$，设 $F(x)=\bigl[f(x)-1\bigr]\mathrm e^{x}$．「 」\n"
        r"$F'(x)=f'(x)\mathrm e^{x}+\bigl[f(x)-1\bigr]\mathrm e^{x}"
        r"=\bigl[f(x)+f'(x)-1\bigr]\mathrm e^{x}<0$，「 」\n"
        r"故 $F$ 在 $\mathbb R$ 上**单调递减**．「 」\n"
        r"**定值**：$F(0)=\bigl[f(0)-1\bigr]\mathrm e^{0}=2019-1=2018$．「 」\n"
        r"**化不等式**：$f(x)<2018\mathrm e^{-x}+1\iff f(x)-1<2018\mathrm e^{-x}$「 」\n"
        r"$\iff\bigl[f(x)-1\bigr]\mathrm e^{x}<2018\iff F(x)<2018=F(0)$．「 」\n"
        r"$F$ 递减，故 $x>0$，即解集为 $(0,+\infty)$，选 A．"
    ),
    'review': (
        r"★ 题干与详解完整 ✓，$\mathrm e^{-x}$ 的上标已由还原版还原。「 」\n"
        r"**构造的来源**（这类「常数项」题的通用思路）："
        r"条件是 $f+f'<1$，右边不是 $0$，所以不能直接构造 $f\mathrm e^x$。"
        r"把 $1$ 写成 $1'$…实际做法是把 $f$ 平移成 $f-1$：「 」\n"
        r"$(f-1)'+(f-1)=f'+f-1<0$，于是 $[(f-1)\mathrm e^x]'<0$ ✓。「 」\n"
        r"**数值校验**：$x=0$：$f(0)=2019$，右端 $2018\mathrm e^0+1=2019$，"
        r"等式成立 ⇒ $x=0$ 是边界，不在解集内 ✓ 与 $(0,+\infty)$ 开区间一致。"
        r"$x>0$ 时 $F(x)<F(0)$ ⇒ $[f(x)-1]\mathrm e^x<2018$ ⇒ $f(x)-1<2018\mathrm e^{-x}$ ✓。"
    ),
    'difficulty': 0.78,
    'topics': ['M-T-121'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-121-V3',
}

T121_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知函数 $f(x)$ 的导函数为 $f'(x)$，对任意的实数 $x$ 都有 "
        r"$f'(x)=f(x)-2\mathrm e^{-x}+2x-x^{2}$，$f(0)=2$，"
        r"则不等式 $f(|x-1|)<\mathrm e^{2}+\mathrm e^{-2}+4$ 的解集是（　　）"
    ),
    'opts': [
        ('A', r"$(0,1)$"),
        ('B', r"$(-1,1)$"),
        ('C', r"$(-1,3)$"),
        ('D', r"$(\mathrm e,3)$"),
    ],
    'answer': 'C',
    'analysis': (
        r"先由待定系数求出解析式 $f(x)=\mathrm e^{-x}+x^{2}+\mathrm e^{x}$（偶函数），"
        r"再由单调性把不等式化成 $f(|x-1|)<f(2)$。"
    ),
    'solution': (
        r"**求解析式**：由 $f'(x)=f(x)-2\mathrm e^{-x}+2x-x^{2}$，「 」\n"
        r"试设 $f(x)=\mathrm e^{-x}+x^{2}+a\mathrm e^{x}$，则 "
        r"$f'(x)=-\mathrm e^{-x}+2x+a\mathrm e^{x}$．「 」\n"
        r"代入右端：$f(x)-2\mathrm e^{-x}+2x-x^{2}"
        r"=(\mathrm e^{-x}+x^{2}+a\mathrm e^{x})-2\mathrm e^{-x}+2x-x^{2}"
        r"=-\mathrm e^{-x}+2x+a\mathrm e^{x}=f'(x)$ ✓ 恒成立，「 」\n"
        r"由 $f(0)=1+0+a=2$ 得 $a=1$，故 $f(x)=\mathrm e^{-x}+x^{2}+\mathrm e^{x}$．「 」\n"
        r"**性质**：$f(-x)=\mathrm e^{x}+x^{2}+\mathrm e^{-x}=f(x)$，**$f$ 为偶函数**．「 」\n"
        r"$x\geqslant0$ 时 $\mathrm e^{x}\geqslant1$、$0<\mathrm e^{-x}\leqslant1$、$2x\geqslant0$，"
        r"故 $f'(x)=\mathrm e^{x}-\mathrm e^{-x}+2x>0$，**$f$ 在 $(0,+\infty)$ 上递增**．「 」\n"
        r"**解不等式**：$\mathrm e^{2}+\mathrm e^{-2}+4=f(2)$（因 $f(2)=\mathrm e^{-2}+4+\mathrm e^{2}$），「 」\n"
        r"故 $f(|x-1|)<f(2)$．由偶性 $f(|x-1|)=f(|x-1|)$，"
        r"且 $f$ 在 $[0,+\infty)$ 上递增，「 」\n"
        r"得 $|x-1|<2\Rightarrow-2<x-1<2\Rightarrow-1<x<3$．「 」\n"
        r"故选 C．"
    ),
    'review': (
        r"★ 题干完整 ✓（$\mathrm e^{-x}$、$x^2$ 上标已还原）。"
        r"由详解「由题意得 $f(x)=\mathrm e^{-x}+x^2+a\mathrm e^x$，则 "
        r"$f'(x)=-\mathrm e^{-x}+2x+a\mathrm e^x=\mathrm e^{-x}+x^2+a\mathrm e^x-2\mathrm e^{-x}+2x-x^2"
        r"=f(x)-2\mathrm e^{-x}+2x-x^2$，由 $f(0)=1+a=2$，解得 $a=1$，"
        r"故 $f(x)=\mathrm e^{-x}+x^2+\mathrm e^x$，$f(|x-1|)<\mathrm e^2+\mathrm e^{-2}+4=f(2)$，"
        r"当 $x\geqslant0$ 时，$\mathrm e^x\geqslant1$，$0<\mathrm e^{-x}\leqslant1$，$2x\geqslant0$，"
        r"$f'(x)=\mathrm e^x-\mathrm e^{-x}+2x>0$ 在 $(0,+\infty)$ 上恒成立，"
        r"即 $f(x)$ 在 $(0,+\infty)$ 上单调递增，又 $f(-x)=f(x)$，故 $f(x)$ 为 $\mathbb R$ 上的偶函数」还原。「 」\n"
        r"**导数自洽校验**：$f'(x)=-\mathrm e^{-x}+2x+\mathrm e^x$；"
        r"$f(x)-2\mathrm e^{-x}+2x-x^2=(\mathrm e^{-x}+x^2+\mathrm e^x)-2\mathrm e^{-x}+2x-x^2"
        r"=-\mathrm e^{-x}+\mathrm e^x+2x$ ✓ **两边相等**，解析式无误。「 」\n"
        r"**数值校验**：$f(2)=\mathrm e^{-2}+4+\mathrm e^2=0.1353+4+7.389=11.524$ ✓；"
        r"$|x-1|<2$ ⇒ $-1<x<3$ ✓；"
        r"$x=3$：$|3-1|=2$，$f(2)=11.524$ 等于右端，不满足 $<$ ✗ ✓（开区间）；"
        r"$x=0$：$|0-1|=1$，$f(1)=\mathrm e^{-1}+1+\mathrm e=0.368+1+2.718=4.086<11.524$ ✓。"
    ),
    'difficulty': 0.87,
    'topics': ['M-T-121'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-121-E1',
}

T122_V1 = {
    'type': '选择',
    'stem_text': (
        r"已知定义域为 $\mathbb R$ 的函数 $f(x)$ 满足 $f(x)+xf'(x)>1$"
        r"（$f'(x)$ 为 $f(x)$ 的导函数），"
        r"则不等式 $(1+x)f(1-x^{2})>f(1-x)+x$ 的解集为（　　）"
    ),
    'opts': [
        ('A', r"$(0,1)$"),
        ('B', r"$(0,1]$"),
        ('C', r"$(0,+\infty)$"),
        ('D', r"$(0,1)\cup(1,+\infty)$"),
    ],
    'answer': 'C',
    'analysis': (
        r"构造 $g(x)=xf(x)-x$，则 $g'=f+xf'-1>0$，$g$ 递增；"
        r"不等式乘 $(1-x)$ 后要**分 $x<1$、$x>1$、$x=1$** 三种情况讨论（乘负数变号）。"
    ),
    'solution': (
        r"**构造**：设 $g(x)=xf(x)-x$，则 $g'(x)=f(x)+xf'(x)-1>0$，"
        r"故 $g$ 在 $\mathbb R$ 上**递增**．「 」\n"
        r"原不等式：$(1+x)f(1-x^{2})>f(1-x)+x$．「 」\n"
        r"**① $x<1$**（$1-x>0$）：两边同乘 $1-x>0$，不等号不变，「 」\n"
        r"$(1-x)(1+x)f(1-x^{2})>(1-x)f(1-x)+(1-x)x$「 」\n"
        r"$\Rightarrow(1-x^{2})f(1-x^{2})>(1-x)f(1-x)+x-x^{2}$「 」\n"
        r"$\Rightarrow\bigl[(1-x^{2})f(1-x^{2})-(1-x^{2})\bigr]"
        r">\bigl[(1-x)f(1-x)-(1-x)\bigr]$「 」\n"
        r"即 $g(1-x^{2})>g(1-x)$．$g$ 递增 ⇒ $1-x^{2}>1-x\Rightarrow x^{2}<x\Rightarrow 0<x<1$．「 」\n"
        r"结合 $x<1$，得 $0<x<1$．「 」\n"
        r"**② $x>1$**（$1-x<0$）：同乘 $1-x<0$，**不等号变向**，「 」\n"
        r"得 $g(1-x^{2})<g(1-x)\Rightarrow1-x^{2}<1-x\Rightarrow x^{2}>x\Rightarrow x<0$ 或 $x>1$．「 」\n"
        r"结合 $x>1$，得 $x>1$．「 」\n"
        r"**③ $x=1$**：原不等式化为 $2f(0)>f(0)+1$，即 $f(0)>1$，"
        r"此即条件 $f(0)+0\cdot f'(0)>1$ 本身，**成立**．「 」\n"
        r"综上 $x\in(0,1)\cup\{1\}\cup(1,+\infty)=(0,+\infty)$，选 C．"
    ),
    'review': (
        r"★ 题干与详解完整 ✓。由详解「构造函数 $g(x)=xf(x)-x$，"
        r"则 $g'(x)=f(x)+xf'(x)-1>0$，所以函数 $g(x)$ 递增，"
        r"则 $1-x^2>1-x$，此时 $0<x<1$，即 $0<x<1$ 满足；"
        r"当 $x>1$ 时，可得 $(1-x^2)f(1-x^2)-(1-x^2)<(1-x)f(1-x)-(1-x)$，"
        r"由函数 $g(x)$ 递增，则 $1-x^2<1-x$，此时 $x<0$ 或 $x>1$，即 $x>1$ 满足；"
        r"当 $x=1$ 时，$2f(0)>f(0)+1$，即 $f(0)>1$ 满足；"
        r"综上，$x\in(0,+\infty)$」还原。「 」\n"
        r"**⭐ 本题最关键的细节**：答案 C 是 $(0,+\infty)$，**包含 $x=1$**。"
        r"若只讨论 $x<1$ 和 $x>1$ 会漏掉 $x=1$，得到 D $(0,1)\cup(1,+\infty)$（错）。"
        r"$x=1$ 时原不等式退化为 $2f(0)>f(0)+1$，恰好就是题干条件在 $x=0$ 处的取值 ✓。「 」\n"
        r"这也是 D 选项的来历 —— **命题人用 D 来考查是否讨论了 $x=1$**。"
    ),
    'difficulty': 0.92,
    'topics': ['M-T-122'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-122-V1',
}

T122_E1 = {
    'type': '选择',
    'stem_text': (
        r"已知 $f'(x)$ 是函数 $f(x)$ 的导函数，且对于任意实数 $x$ 都有 "
        r"$f'(x)=\mathrm e^{x}(2x-1)+f(x)$，$f(0)=-1$，"
        r"则不等式 $f(x)>5\mathrm e^{x}$ 的解集为（　　）"
    ),
    'opts': [
        ('A', r"$(-\infty,-2)\cup(3,+\infty)$"),
        ('B', r"$(-\infty,-3)\cup(2,+\infty)$"),
        ('C', r"$(-2,3)$"),
        ('D', r"$(-3,2)$"),
    ],
    'answer': 'A',
    'analysis': (
        r"移项得 $f'(x)-f(x)=\mathrm e^{x}(2x-1)$，左边是 $\mathrm e^{x}\left[\frac{f(x)}{\mathrm e^{x}}\right]'$，"
        r"故 $\left[\frac{f(x)}{\mathrm e^{x}}\right]'=2x-1$，积分得 $\frac{f(x)}{\mathrm e^{x}}=x^{2}-x+m$。"
    ),
    'solution': (
        r"**识别结构**：由 $f'(x)=\mathrm e^{x}(2x-1)+f(x)$ 得 $f'(x)-f(x)=\mathrm e^{x}(2x-1)$．「 」\n"
        r"而 $\left[\dfrac{f(x)}{\mathrm e^{x}}\right]'=\dfrac{f'(x)\mathrm e^{x}-f(x)\mathrm e^{x}}{\mathrm e^{2x}}"
        r"=\dfrac{f'(x)-f(x)}{\mathrm e^{x}}$，「 」\n"
        r"故 $\left[\dfrac{f(x)}{\mathrm e^{x}}\right]'=2x-1$．「 」\n"
        r"**积分**：$\dfrac{f(x)}{\mathrm e^{x}}=x^{2}-x+m$，即 $f(x)=\mathrm e^{x}(x^{2}-x+m)$．「 」\n"
        r"由 $f(0)=-1$ 得 $1\cdot(0-0+m)=-1$，故 $m=-1$，"
        r"$f(x)=\mathrm e^{x}(x^{2}-x-1)$．「 」\n"
        r"**解不等式**：$f(x)>5\mathrm e^{x}\iff\mathrm e^{x}(x^{2}-x-1)>5\mathrm e^{x}$．「 」\n"
        r"$\mathrm e^{x}>0$，故 $x^{2}-x-1>5\iff x^{2}-x-6>0\iff(x-3)(x+2)>0$，「 」\n"
        r"得 $x<-2$ 或 $x>3$，即解集为 $(-\infty,-2)\cup(3,+\infty)$，选 A．"
    ),
    'review': (
        r"★ 题干完整 ✓（$\mathrm e^x$ 上标已还原）。"
        r"由详解「因为 $f'(x)=\mathrm e^x(2x-1)+f(x)$，所以 $\left[\frac{f(x)}{\mathrm e^x}\right]'=2x-1$，"
        r"即 $\frac{f(x)}{\mathrm e^x}=x^2-x+m$，亦即 $f(x)=\mathrm e^x(x^2-x+m)$，"
        r"又 $f(0)=-1$，所以 $m=-1$，即有 $f(x)=\mathrm e^x(x^2-x-1)$；"
        r"原不等式 $f(x)>5\mathrm e^x$ 可等价于 $x^2-x-1>5$，即 $x^2-x-6>0$，"
        r"解得 $x$ 的取值范围是 $(-\infty,-2)\cup(3,+\infty)$」还原。「 」\n"
        r"**导数校验**：$f(x)=\mathrm e^x(x^2-x-1)$ ⇒ "
        r"$f'=\mathrm e^x(x^2-x-1)+\mathrm e^x(2x-1)=\mathrm e^x(x^2+x-2)$；「 」\n"
        r"$\mathrm e^x(2x-1)+f(x)=\mathrm e^x(2x-1)+\mathrm e^x(x^2-x-1)=\mathrm e^x(x^2+x-2)$ ✓ **吻合**。「 」\n"
        r"**数值校验**：$x=4$：$f(4)=\mathrm e^4(16-4-1)=11\mathrm e^4=600.5$，"
        r"$5\mathrm e^4=272.99$ ✓ $600.5>273$ 在解集内 ✓；"
        r"$x=0$：$f(0)=-1$，$5\mathrm e^0=5$ ✗ 不在解集内 ✓（$0\in(-2,3)$）。"
    ),
    'difficulty': 0.85,
    'topics': ['M-T-122'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-122-E1',
}

QS = [T120_V2, T120_V3, T121_V1, T121_V2, T121_V3,
      T121_E1, T122_V1, T122_E1]
