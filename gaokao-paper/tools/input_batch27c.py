# -*- coding: utf-8 -*-
r"""第27批（下）：M-T-124 技巧计算型构造（1题）

来源：2024高中数学热点题型归纳完整解析版.pdf 专题4 p089（PDF 页 88）

## 本批只录 1 题

p089 上第 35、37 题的选项严重破碎（含大量 ⟨?⟩ 与分离的分子分母），
无法可靠判定，**跳过**。第 36 题题干、选项、详解三者完整，录入。

## ★ 归属仍以 ref_bank 的 key 为准

本批 M-T-124-V2（orig=36）由以下方式查出，可复用：

```python
python3 -c "
import json
rb=json.load(open('data/ref_bank.json',encoding='utf-8'))
for k,q in rb.items():
    s=(q.get('stem') or '').replace(' ','').replace(chr(10),'')
    if 'f(1)=3' in s: print(k, q.get('orig_num'))
"
```

## 题型要点

条件 $f+f'>\text{常数}$ 时，把常数移进构造：
$F(x)=\mathrm e^{x-c}[f(x)-\text{常数}]$，
其导数 $=\mathrm e^{x-c}[f+f'-\text{常数}]$，符号由条件直接给出。
"""

T124_V2 = {
    'type': '选择',
    'stem_text': (
        r"定义在 $\mathbb R$ 上的函数 $f(x)$ 满足 $f(x)+f'(x)>1$、$f(1)=3$，"
        r"$f'(x)$ 是 $f(x)$ 的导函数，"
        r"则不等式 $f(x)>1+\dfrac{2}{\mathrm e^{x-1}}$ 的解集为（　　）"
    ),
    'opts': [
        ('A', r"$(1,+\infty)$"),
        ('B', r"$(-\infty,1)$"),
        ('C', r"$(-\infty,0)\cup(1,+\infty)$"),
        ('D', r"$(0,+\infty)$"),
    ],
    'answer': 'A',
    'analysis': (
        r"构造 $g(x)=\mathrm e^{x-1}f(x)-\mathrm e^{x-1}=\mathrm e^{x-1}[f(x)-1]$，"
        r"则 $g'=\mathrm e^{x-1}[f+f'-1]>0$，$g$ 递增；不等式化为 $g(x)>g(1)$。"
    ),
    'solution': (
        r"**构造**：设 $g(x)=\mathrm e^{x-1}f(x)-\mathrm e^{x-1}"
        r"=\mathrm e^{x-1}\bigl[f(x)-1\bigr]$．" "\n"
        r"$g'(x)=\mathrm e^{x-1}f(x)+\mathrm e^{x-1}f'(x)-\mathrm e^{x-1}"
        r"=\mathrm e^{x-1}\bigl[f(x)+f'(x)-1\bigr]$．" "\n"
        r"由 $f(x)+f'(x)>1$ 得 $g'(x)>0$，故 $g$ 在 $\mathbb R$ 上**单调递增**．" "\n"
        r"**定值**：$g(1)=\mathrm e^{0}f(1)-\mathrm e^{0}=3-1=2$．" "\n"
        r"**化不等式**：$f(x)>1+\dfrac{2}{\mathrm e^{x-1}}$" "\n"
        r"$\iff f(x)-1>\dfrac{2}{\mathrm e^{x-1}}$"
        r"$\iff \mathrm e^{x-1}\bigl[f(x)-1\bigr]>2\iff g(x)>2=g(1)$．" "\n"
        r"$g$ 递增，故 $x>1$，即解集为 $(1,+\infty)$，选 A．"
    ),
    'review': (
        r"★ 题干、选项、详解**三者完整**，"
        r"$\mathrm e^{x-1}$ 的上标与分数线均由还原版自动还原 ✓，无需人工补结构。" "\n"
        r"由详解「设 $g(x)=\mathrm e^{x-1}f(x)-\mathrm e^{x-1}$，"
        r"则 $g'(x)=\mathrm e^{x-1}f(x)+\mathrm e^{x-1}f'(x)-\mathrm e^{x-1}"
        r"=\mathrm e^{x-1}[f(x)+f'(x)-1]$，"
        r"又由 $f(x)+f'(x)>1$，则 $f(x)+f'(x)-1>0$，所以 $g'(x)>0$，"
        r"所以函数 $g(x)$ 为单调递增函数，"
        r"又由 $f(1)=3$，所以 $g(1)=\mathrm e^0f(1)-\mathrm e^0=2$，"
        r"由不等式 $f(x)>1+\frac{2}{\mathrm e^{x-1}}$，即 $\mathrm e^{x-1}f(x)-\mathrm e^{x-1}>2$，"
        r"即 $g(x)>g(1)$，所以不等式的解集为 $(1,+\infty)$」还原。" "\n"
        r"**⭐ 构造为什么带 $\mathrm e^{x-1}$ 而不是 $\mathrm e^{x}$**："
        r"用 $\mathrm e^{x-1}$ 是为了让 $g(1)$ 中的 $\mathrm e^{0}=1$，"
        r"从而 $g(1)=f(1)-1=2$ 计算最简；"
        r"用 $\mathrm e^{x}$ 也可以，此时 $g(1)=\mathrm e\cdot2$，"
        r"不等式化为 $g(x)>\mathrm e\cdot2=g(1)$，结论相同 ✓。" "\n"
        r"**数值校验**：$x=1$：$f(1)=3$，右端 $1+\frac{2}{\mathrm e^0}=3$，等式成立 ⇒ "
        r"$x=1$ 是边界、不在解集内 ✓ 与开区间 $(1,+\infty)$ 一致。"
    ),
    'difficulty': 0.8,
    'topics': ['M-T-124'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-124-V2',
}

QS = [T124_V2]
