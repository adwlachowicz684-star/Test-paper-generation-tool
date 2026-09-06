# -*- coding: utf-8 -*-
r"""第2批录入：基本不等式（M-T-008 ~ M-T-011），共 16 题。

来源：2024高中数学热点题型归纳 · 专题7-2 基本不等式归类
      PDF 第 230-232 页

每题按 skill 模式 A 人工重建：
  - 分数由 PDF 的上下行还原为 \frac{}{}
  - 根号由「= 10」这类丢失形式还原为 \sqrt{10}
  - 函数 / 区间 / 绝对值括号还原
每题答案均已独立验算。

**字符串一律 raw 前缀** —— 非 raw 时 \v 会被 Python 解释成
垂直制表符 U+000B，导致 Word 端整个公式消失（见 30-pitfalls.md A3）。
"""
import sys, os
sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '..', 'py'))
import hand_input as H

BATCH = '教辅录入-第2批-基本不等式'
KP, KP2 = '不等式', '基本不等式'

QS = []

# ==================== M-T-008 基础型 ====================
QS.append({
    'type': '选择', 'subtype': '单选题', 'answer': 'D', 'difficulty': 0.65,
    'topics': ['M-T-008'], 'src': '2024热点题型归纳 M-T-008 典例',
    'kp': KP, 'kp2': KP2,
    'stem_text': '在下列函数中，最小值是 $2$ 的是（　　）',
    'opts': [['A', '$y=\\frac{x}{2}+\\frac{2}{x}$'],
             ['B', '$y=\\frac{x+2}{x+1}\\ (x>0)$'],
             ['C', '$y=\\sin x+\\cos x$，$x\\in\\left[0,\\frac{\\pi}{2}\\right]$'],
             ['D', '$y=7^{x}+7^{-x}$']],
    'analysis': '逐项用基本不等式求值域，并检查取等条件是否满足定义域。',
    'solution': 'A：$x<0$ 时 $y\\leqslant-2$，最小值不是 $2$，排除；'
                'B：$y=\\frac{x+2}{x+1}=1+\\frac{1}{x+1}$，$x>0$ 时 $y\\in(1,2)$，'
                '取不到 $2$（取等需 $x=0$），排除；'
                'C：$y=\\sqrt{2}\\sin\\left(x+\\frac{\\pi}{4}\\right)$，'
                '由 $x+\\frac{\\pi}{4}\\in\\left[\\frac{\\pi}{4},\\frac{3\\pi}{4}\\right]$ '
                '得 $y\\in\\left[1,\\sqrt{2}\\right]$，最小值是 $1$，排除；'
                'D：$7^{x}+7^{-x}\\geqslant2\\sqrt{7^{x}\\cdot7^{-x}}=2$，'
                '当且仅当 $x=0$ 时取等号，符合题意．故选 D．',
    'review': '原书详解在 B 选项处写「$=(x+1)+\\frac{1}{x+1}\\geqslant2$」，'
              '与 $\\frac{x+2}{x+1}=1+\\frac{1}{x+1}$ 不符，属原书排版笔误；'
              '但取等条件 $x=0$ 与「$x>0$ 取不到」的结论均正确，'
              '不影响答案．选项按原文 $\\frac{x+2}{x+1}$ 录入．',
})

QS.append({
    'type': '填空', 'subtype': '单空题', 'answer': '$\\sqrt{10}$', 'difficulty': 0.65,
    'topics': ['M-T-008'], 'src': '2024热点题型归纳 M-T-008 变式1',
    'kp': KP, 'kp2': KP2,
    'stem_text': '已知关于 $x$ 的不等式 $x^{2}-5ax+2a^{2}<0\\ (a>0)$ 的解集为 '
                 '$(x_1,x_2)$，则 $x_1+x_2+\\dfrac{a}{x_1x_2}$ 的最小值是＿＿＿＿＿．',
    'analysis': '韦达定理得两根之和与两根之积，代入后只剩 $a$，再用基本不等式。',
    'solution': '$\\Delta=25a^{2}-8a^{2}=17a^{2}>0$．'
                '由韦达定理 $x_1+x_2=5a$，$x_1x_2=2a^{2}$，'
                '故 $x_1+x_2+\\frac{a}{x_1x_2}=5a+\\frac{a}{2a^{2}}'
                '=5a+\\frac{1}{2a}\\geqslant2\\sqrt{5a\\cdot\\frac{1}{2a}}'
                '=2\\sqrt{\\frac{5}{2}}=\\sqrt{10}$，'
                '当且仅当 $5a=\\frac{1}{2a}$ 即 $a=\\frac{\\sqrt{10}}{10}$ 时取等号．'
                '故最小值为 $\\sqrt{10}$．',
    'review': '**原书答案印作「10」，实为 $\\sqrt{10}$** —— PDF 提取时根号丢失'
              '（详解取等处「$a=\\frac{10}{10}$」原文为 $\\frac{\\sqrt{10}}{10}$，'
              '两处一致佐证）．已按 $\\sqrt{10}$ 录入，并独立验算确认。',
})

QS.append({
    'type': '选择', 'subtype': '单选题', 'answer': 'C', 'difficulty': 0.65,
    'topics': ['M-T-008'], 'src': '2024热点题型归纳 M-T-008 变式2',
    'kp': KP, 'kp2': KP2,
    'stem_text': '若 $a$、$b$ 都是正数，则 $\\left(1+\\dfrac{b}{a}\\right)'
                 '\\left(1+\\dfrac{4a}{b}\\right)$ 的最小值为（　　）',
    'opts': [['A', '$5$'], ['B', '$7$'], ['C', '$9$'], ['D', '$13$']],
    'analysis': '展开后得到常数 $5$ 加上互为倒数的两项，用基本不等式。',
    'solution': '$\\left(1+\\frac{b}{a}\\right)\\left(1+\\frac{4a}{b}\\right)'
                '=1+\\frac{4a}{b}+\\frac{b}{a}+4=5+\\frac{b}{a}+\\frac{4a}{b}'
                '\\geqslant5+2\\sqrt{\\frac{b}{a}\\cdot\\frac{4a}{b}}=5+4=9$，'
                '当且仅当 $b=2a>0$ 时取等号．故选 C．',
    'review': '题干与选项完整，仅补分数与括号。',
})

QS.append({
    'type': '选择', 'subtype': '单选题', 'answer': 'A', 'difficulty': 0.65,
    'topics': ['M-T-008'], 'src': '2024热点题型归纳 M-T-008 变式3',
    'kp': KP, 'kp2': KP2,
    'stem_text': '在区间 $[-2,4]$ 上随机地取一个数 $x$，使 '
                 '$a^{2}+\\dfrac{1}{a^{2}+1}\\geqslant|x|$ 恒成立的概率是（　　）',
    'opts': [['A', '$\\dfrac{1}{3}$'], ['B', '$\\dfrac{1}{2}$'],
             ['C', '$\\dfrac{2}{3}$'], ['D', '$\\dfrac{3}{4}$']],
    'analysis': '先求左边的最小值，把恒成立转化为 $|x|\\leqslant$ 该最小值，'
                '再用几何概型算长度比。',
    'solution': '$a^{2}+\\frac{1}{a^{2}+1}=(a^{2}+1)+\\frac{1}{a^{2}+1}-1'
                '\\geqslant2-1=1$，'
                '当且仅当 $a^{2}+1=1$ 即 $a=0$ 时取等号，故最小值为 $1$．'
                '恒成立即 $|x|\\leqslant1$，即 $-1\\leqslant x\\leqslant1$，长度为 $2$；'
                '区间 $[-2,4]$ 长度为 $6$，故 $P=\\frac{2}{6}=\\frac{1}{3}$．故选 A．',
    'review': '题干中 $|x|$ 的绝对值符号在 PDF 里为矢量绘制，提取时丢失，'
              '已按详解「即 $-1\\leqslant x\\leqslant1$」还原。',
})

# ==================== M-T-009 "1"的代换型 ====================
QS.append({
    'type': '填空', 'subtype': '单空题', 'answer': '$2$', 'difficulty': 0.65,
    'topics': ['M-T-009'], 'src': '2024热点题型归纳 M-T-009 典例',
    'kp': KP, 'kp2': KP2,
    'stem_text': '已知 $x$、$y$ 均为正实数，且 $\\dfrac{2x+y}{xy}=\\dfrac{7}{2}+\\sqrt{6}$，'
                 '则 $x+3y$ 的最小值为＿＿＿＿＿．',
    'analysis': '把条件化为 $\\frac{2}{y}+\\frac{1}{x}=\\frac{7}{2}+\\sqrt{6}$，'
                '再乘「1」展开后用基本不等式。',
    'solution': '由 $\\frac{2x+y}{xy}=\\frac{2}{y}+\\frac{1}{x}=\\frac{7}{2}+\\sqrt{6}$，'
                '记 $k=\\frac{7}{2}+\\sqrt{6}=\\frac{7+2\\sqrt{6}}{2}$，则'
                '$x+3y=\\frac{1}{k}(x+3y)\\left(\\frac{2}{y}+\\frac{1}{x}\\right)'
                '=\\frac{1}{k}\\left(7+\\frac{2x}{y}+\\frac{3y}{x}\\right)'
                '\\geqslant\\frac{1}{k}\\left(7+2\\sqrt{6}\\right)=2$，'
                '当且仅当 $2x=3y$ 时取等号．故最小值为 $2$．',
    'review': '原题无【答案】标记（答案写在详解末尾），'
              'ref_bank 提取时被过滤掉，此处据详解补录。'
              '验算：$7+2\\sqrt{6}$ 与 $\\frac{7}{2}+\\sqrt{6}=\\frac{7+2\\sqrt{6}}{2}$ '
              '恰好成 2 倍关系，故结果为 2。',
})

QS.append({
    'type': '选择', 'subtype': '单选题', 'answer': 'C', 'difficulty': 0.65,
    'topics': ['M-T-009'], 'src': '2024热点题型归纳 M-T-009 变式4',
    'kp': KP, 'kp2': KP2,
    'stem_text': '已知 $a>0$，$b>0$，$\\dfrac{3}{b}+\\dfrac{2}{a}=1$，'
                 '则 $2a+3b$ 的最小值为（　　）',
    'opts': [['A', '$20$'], ['B', '$24$'], ['C', '$25$'], ['D', '$28$']],
    'analysis': '把「1」替换成已知条件，展开后用基本不等式。',
    'solution': '$2a+3b=(2a+3b)\\left(\\frac{2}{a}+\\frac{3}{b}\\right)'
                '=4+\\frac{6a}{b}+\\frac{6b}{a}+9'
                '=13+\\frac{6a}{b}+\\frac{6b}{a}'
                '\\geqslant13+2\\sqrt{\\frac{6a}{b}\\cdot\\frac{6b}{a}}=13+12=25$，'
                '当且仅当 $a=b=5$ 时取等号．故选 C．',
    'review': '验算取等：$a=b=5$ 时 $\\frac{3}{5}+\\frac{2}{5}=1$ 满足，'
              '$2a+3b=25$ 与选项 C 一致。',
})

QS.append({
    'type': '选择', 'subtype': '单选题', 'answer': 'D', 'difficulty': 0.65,
    'topics': ['M-T-009'], 'src': '2024热点题型归纳 M-T-009 变式5',
    'kp': KP, 'kp2': KP2,
    'stem_text': '已知 $a>0$，$b>0$，$3a+\\dfrac{4}{b}=1$，'
                 '则 $\\dfrac{1}{a}+3b$ 的最小值为（　　）',
    'opts': [['A', '$13$'], ['B', '$19$'], ['C', '$21$'], ['D', '$27$']],
    'analysis': '乘「1」展开，出现 $ab$ 与 $\\frac{1}{ab}$ 的配对。',
    'solution': '$\\frac{1}{a}+3b=\\left(\\frac{1}{a}+3b\\right)'
                '\\left(3a+\\frac{4}{b}\\right)'
                '=3+\\frac{4}{ab}+9ab+12=15+\\frac{4}{ab}+9ab'
                '\\geqslant15+2\\sqrt{\\frac{4}{ab}\\cdot9ab}=15+12=27$，'
                '当且仅当 $9ab=\\frac{4}{ab}$ 即 $a=\\frac{1}{9}$、$b=6$ 时取等号．'
                '故选 D．',
    'review': '验算取等：$3\\cdot\\frac19+\\frac46=\\frac13+\\frac23=1$ 满足，'
              '$\\frac{1}{a}+3b=9+18=27$ 与选项 D 一致。',
})

QS.append({
    'type': '填空', 'subtype': '单空题', 'answer': '$11$', 'difficulty': 0.65,
    'topics': ['M-T-009'], 'src': '2024热点题型归纳 M-T-009 变式6',
    'kp': KP, 'kp2': KP2,
    'stem_text': '已知正实数 $a$、$b$ 满足 $a+b=1$，则 '
                 '$\\dfrac{2a^{2}+1}{a}+\\dfrac{2b^{2}+4}{b}$ 的最小值为＿＿＿＿＿．',
    'analysis': '先分离出 $2(a+b)$，再用「1」的代换。',
    'solution': '$\\frac{2a^{2}+1}{a}+\\frac{2b^{2}+4}{b}=2a+\\frac{1}{a}'
                '+2b+\\frac{4}{b}=2(a+b)+\\left(\\frac{1}{a}+\\frac{4}{b}\\right)'
                '=2+\\left(\\frac{1}{a}+\\frac{4}{b}\\right)(a+b)'
                '=2+1+\\frac{b}{a}+\\frac{4a}{b}+4'
                '=7+\\frac{b}{a}+\\frac{4a}{b}$'
                '$\\geqslant7+2\\sqrt{\\frac{b}{a}\\cdot\\frac{4a}{b}}=7+4=11$，'
                '当且仅当 $a=\\frac{1}{3}$、$b=\\frac{2}{3}$ 时取等号．'
                '故最小值为 $11$．',
    'review': '原题无【答案】标记（答案在详解末尾），ref_bank 提取时被过滤，'
              '此处据详解补录。验算取等：$a=\\frac13$、$b=\\frac23$ 时 $a+b=1$ 满足，'
              '代入得 $11$，与详解一致。',
})

# ==================== M-T-010 "和"与"积"互消型 ====================
QS.append({
    'type': '填空', 'subtype': '单空题', 'answer': '$18$', 'difficulty': 0.65,
    'topics': ['M-T-010'], 'src': '2024热点题型归纳 M-T-010 典例',
    'kp': KP, 'kp2': KP2,
    'stem_text': '已知 $x$、$y$ 都是正数，且满足 $x+2y+xy=30$，'
                 '则 $xy$ 的最大值为＿＿＿＿＿．',
    'analysis': '由 $30-xy=x+2y\\geqslant2\\sqrt{2xy}$，'
                '得到关于 $\\sqrt{xy}$ 的一元二次不等式。',
    'solution': '$30-xy=x+2y\\geqslant2\\sqrt{2xy}$（当且仅当 $x=2y$ 时取等号）．'
                '令 $t=\\sqrt{xy}>0$，则 $t^{2}+2\\sqrt{2}t-30\\leqslant0$，'
                '解得 $-5\\sqrt{2}\\leqslant t\\leqslant3\\sqrt{2}$，'
                '故 $0<xy\\leqslant18$，即 $xy$ 的最大值为 $18$，'
                '此时 $x=6$、$y=3$．',
    'review': '验算：$x=6$、$y=3$ 时 $6+6+18=30$ 满足条件，$xy=18$。',
})

QS.append({
    'type': '选择', 'subtype': '单选题', 'answer': 'A', 'difficulty': 0.65,
    'topics': ['M-T-010'], 'src': '2024热点题型归纳 M-T-010 变式7',
    'kp': KP, 'kp2': KP2,
    'stem_text': '已知 $x>0$，$y>0$，且 $4x+2y-xy=0$，则 $2x+y$ 的最小值为（　　）',
    'opts': [['A', '$16$'], ['B', '$8+4\\sqrt{2}$'],
             ['C', '$12$'], ['D', '$6+4\\sqrt{2}$']],
    'analysis': '由 $4x+2y=xy$ 两边同除以 $xy$ 得 $\\frac{4}{y}+\\frac{2}{x}=1$，'
                '转化为「1」的代换型。',
    'solution': '由 $4x+2y=xy$ 得 $\\frac{4}{y}+\\frac{2}{x}=1$，'
                '故 $2x+y=(2x+y)\\left(\\frac{2}{x}+\\frac{4}{y}\\right)'
                '=4+\\frac{8x}{y}+\\frac{2y}{x}+4'
                '=8+\\frac{8x}{y}+\\frac{2y}{x}'
                '\\geqslant8+2\\sqrt{\\frac{8x}{y}\\cdot\\frac{2y}{x}}=8+8=16$，'
                '当且仅当 $y=2x$ 时取等号．故选 A．',
    'review': '验算取等：$y=2x$ 代入 $4x+2y=xy$ 得 $4x+4x=2x^{2}$，'
              '即 $x=4$、$y=8$，此时 $2x+y=16$ 与选项 A 一致。',
})

QS.append({
    'type': '填空', 'subtype': '单空题', 'answer': '$6$', 'difficulty': 0.5,
    'topics': ['M-T-010'], 'src': '2024热点题型归纳 M-T-010 变式8',
    'kp': KP, 'kp2': KP2,
    'stem_text': '已知 $x>0$，$y>0$，且 $2x+9y+6xy=9$，'
                 '则 $2x+9y$ 的最小值为＿＿＿＿＿．',
    'analysis': '把 $6xy$ 用 $\\frac{1}{3}\\cdot2x\\cdot9y$ 表示，'
                '对 $2x$ 与 $9y$ 用基本不等式，得到关于 $2x+9y$ 的不等式。',
    'solution': '由条件 $6xy=9-(2x+9y)$．又 '
                '$6xy=\\frac{1}{3}\\cdot2x\\cdot9y'
                '\\leqslant\\frac{1}{3}\\left(\\frac{2x+9y}{2}\\right)^{2}$，'
                '记 $s=2x+9y>0$，则 $9-s\\leqslant\\frac{s^{2}}{12}$，'
                '即 $s^{2}+12s-108\\geqslant0$，$(s-6)(s+18)\\geqslant0$，'
                '得 $s\\geqslant6$．当且仅当 $2x=9y$ 即 $x=\\frac{3}{2}$、$y=\\frac{1}{3}$ '
                '时取等号．故最小值为 $6$．',
    'review': '验算取等：$x=\\frac32$、$y=\\frac13$ 时 '
              '$2x+9y=3+3=6$，$6xy=6\\cdot\\frac32\\cdot\\frac13=3$，'
              '$6+3=9$ 满足条件。',
})

QS.append({
    'type': '选择', 'subtype': '单选题', 'answer': 'C', 'difficulty': 0.4,
    'topics': ['M-T-010'], 'src': '2024热点题型归纳 M-T-010 变式9',
    'kp': KP, 'kp2': KP2,
    'stem_text': '已知 $x$、$y>0$，$x+2y+xy-6=0$，则说法不正确的是（　　）',
    'opts': [['A', '$xy$ 的最大值为 $2$'],
             ['B', '$x+2y$ 的最小值为 $4$'],
             ['C', '$x+y$ 的最小值为 $3$'],
             ['D', '$x+y$ 的最小值为 $4\\sqrt{2}-3$']],
    'analysis': 'A、B 用基本不等式构造不等式；C、D 用判别式法：'
                '令 $m=x+y$，消元后由方程有解得 $\\Delta\\geqslant0$。',
    'solution': 'A：$x+2y\\geqslant2\\sqrt{2xy}$，又 $x+2y=6-xy$，'
                '故 $6-xy\\geqslant2\\sqrt{2xy}$．令 $t=\\sqrt{xy}>0$，'
                '$t^{2}+2\\sqrt{2} t-6\\leqslant0$，得 $0<t\\leqslant\\sqrt{2}$，'
                '即 $xy\\leqslant2$，A 正确．'
                'B：由 $xy\\leqslant\\frac{(x+2y)^{2}}{8}$ 及 $xy=6-(x+2y)$，'
                '得 $\\frac{(x+2y)^{2}}{8}\\geqslant6-(x+2y)$，'
                '即 $(x+2y)^{2}+8(x+2y)-48\\geqslant0$，得 $x+2y\\geqslant4$，B 正确．'
                'C、D：令 $m=x+y$，则 $y=m-x$，代入条件整理得 '
                '$x^{2}-(m-1)x-2m+6=0$．此方程有解，故 '
                '$\\Delta=(m-1)^{2}+4(2m-6)=m^{2}+6m-23\\geqslant0$，'
                '解得 $m\\geqslant4\\sqrt{2}-3$（负根舍去），'
                '故 $x+y$ 的最小值为 $4\\sqrt{2}-3$，D 正确、C 错误．故选 C．',
    'review': '验算 C：$4\\sqrt{2}-3\\approx2.657<3$，故「最小值为 3」确实错误。'
              '取等时 $x=2$、$y=1$ 满足 $2+2+2-6=0$，此时 $x+y=3$，'
              '但这是 $xy$ 取最大值时的点，并非 $x+y$ 的最小值点。',
})

# ==================== M-T-011 以分母为主元构造型 ====================
QS.append({
    'type': '选择', 'subtype': '单选题', 'answer': 'B', 'difficulty': 0.65,
    'topics': ['M-T-011'], 'src': '2024热点题型归纳 M-T-011 典例',
    'kp': KP, 'kp2': KP2,
    'stem_text': '已知非负数 $x$、$y$ 满足 $x+y=1$，则 '
                 '$\\dfrac{1}{x+1}+\\dfrac{9}{y+2}$ 的最小值是（　　）',
    'opts': [['A', '$3$'], ['B', '$4$'], ['C', '$10$'], ['D', '$16$']],
    'analysis': '由 $x+y=1$ 得 $(x+1)+(y+2)=4$，'
                '以 $x+1$、$y+2$ 为整体做「1」的代换。',
    'solution': '由 $x+y=1$ 得 $(x+1)+(y+2)=4$，故'
                '$\\frac{1}{x+1}+\\frac{9}{y+2}'
                '=\\frac{1}{4}\\left(\\frac{1}{x+1}+\\frac{9}{y+2}\\right)'
                '\\bigl[(x+1)+(y+2)\\bigr]$'
                '$=\\frac{1}{4}\\left(10+\\frac{y+2}{x+1}+\\frac{9(x+1)}{y+2}\\right)'
                '\\geqslant\\frac{1}{4}\\left(10+2\\sqrt{9}\\right)=4$，'
                '当且仅当 $y+2=3(x+1)$ 时取等号．故选 B．',
    'review': '验算取等：联立 $x+y=1$ 与 $y+2=3x+3$，得 $x=0$、$y=1$，'
              '代入 $\\frac{1}{0+1}+\\frac{9}{1+2}=1+3=4$，符合非负要求。',
})

QS.append({
    'type': '选择', 'subtype': '单选题', 'answer': 'A', 'difficulty': 0.65,
    'topics': ['M-T-011'], 'src': '2024热点题型归纳 M-T-011 变式10',
    'kp': KP, 'kp2': KP2,
    'stem_text': '已知 $x>1$，$y>0$，且 $\\dfrac{1}{x-1}+\\dfrac{2}{y}=1$，'
                 '则 $x+2y-1$ 的最小值为（　　）',
    'opts': [['A', '$9$'], ['B', '$10$'], ['C', '$11$'], ['D', '$7+2\\sqrt{6}$']],
    'analysis': '把 $x+2y-1$ 写成 $(x-1)+2y$，'
                '与条件 $\\frac{1}{x-1}+\\frac{2}{y}=1$ 配对做「1」的代换。',
    'solution': '$x+2y-1=(x-1)+2y'
                '=\\bigl[(x-1)+2y\\bigr]\\left(\\frac{1}{x-1}+\\frac{2}{y}\\right)'
                '=1+\\frac{2(x-1)}{y}+\\frac{2y}{x-1}+4'
                '=5+\\frac{2(x-1)}{y}+\\frac{2y}{x-1}'
                '\\geqslant5+2\\sqrt{4}=9$，'
                '当且仅当 $y=x-1$ 且 $\\frac{1}{x-1}+\\frac{2}{y}=1$ '
                '即 $x=4$、$y=3$ 时取等号．故选 A．',
    'review': '验算取等：$x=4$、$y=3$ 时 $\\frac13+\\frac23=1$ 满足，'
              '$x+2y-1=4+6-1=9$ 与选项 A 一致。',
})

QS.append({
    'type': '选择', 'subtype': '单选题', 'answer': 'C', 'difficulty': 0.5,
    'topics': ['M-T-011'], 'src': '2024热点题型归纳 M-T-011 变式11',
    'kp': KP, 'kp2': KP2,
    'stem_text': '已知正数 $a$、$b$ 满足 $a+b=1$，则 '
                 '$\\dfrac{4a}{1-a}+\\dfrac{b}{1-b}$ 的最小值是（　　）',
    'opts': [['A', '$1$'], ['B', '$2$'], ['C', '$4$'], ['D', '$8$']],
    'analysis': '由 $a+b=1$ 得 $1-a=b$、$1-b=a$，'
                '代入后化为 $\\frac{4a}{b}+\\frac{b}{a}$，直接用基本不等式。',
    'solution': '由 $a+b=1$ 得 $1-a=b$、$1-b=a$，故'
                '$\\frac{4a}{1-a}+\\frac{b}{1-b}=\\frac{4a}{b}+\\frac{b}{a}'
                '\\geqslant2\\sqrt{\\frac{4a}{b}\\cdot\\frac{b}{a}}=4$，'
                '当且仅当 $b=2a$，即 $a=\\frac{1}{3}$、$b=\\frac{2}{3}$ 时取等号．'
                '故选 C．',
    'review': '验算取等：$a=\\frac13$、$b=\\frac23$ 时 '
              '$\\frac{4\\cdot\\frac13}{\\frac23}+\\frac{\\frac23}{\\frac13}'
              '=2+2=4$，与选项 C 一致。',
})

QS.append({
    'type': '选择', 'subtype': '单选题', 'answer': 'A', 'difficulty': 0.4,
    'topics': ['M-T-011'], 'src': '2024热点题型归纳 M-T-011 变式12',
    'kp': KP, 'kp2': KP2,
    'stem_text': '设 $x>y>0$，则 $x+\\dfrac{4}{x+y}+\\dfrac{1}{x-y}$ 的最小值为（　　）',
    'opts': [['A', '$3\\sqrt{2}$'], ['B', '$2\\sqrt{3}$'],
             ['C', '$4$'], ['D', '$\\dfrac{3\\sqrt{10}}{2}$']],
    'analysis': '把 $x$ 拆成 $\\frac{1}{2}(x+y)+\\frac{1}{2}(x-y)$，'
                '分别与两个分式配成基本不等式的形式。',
    'solution': '$x+\\frac{4}{x+y}+\\frac{1}{x-y}'
                '=\\left[\\frac{1}{2}(x+y)+\\frac{4}{x+y}\\right]'
                '+\\left[\\frac{1}{2}(x-y)+\\frac{1}{x-y}\\right]'
                '\\geqslant2\\sqrt{\\frac{1}{2}\\cdot4}'
                '+2\\sqrt{\\frac{1}{2}\\cdot1}=2\\sqrt{2}+\\sqrt{2}=3\\sqrt{2}$，'
                '当且仅当 $\\frac{1}{2}(x+y)=\\frac{4}{x+y}$ 且 '
                '$\\frac{1}{2}(x-y)=\\frac{1}{x-y}$，'
                '即 $x=\\frac{3\\sqrt{2}}{2}$、$y=\\frac{\\sqrt{2}}{2}$ 时取等号．故选 A．',
    'review': '验算取等：$x=\\frac{3\\sqrt{2}}{2}$、$y=\\frac{\\sqrt{2}}{2}$ 时 '
              '$x+y=2\\sqrt{2}$、$x-y=\\sqrt{2}$，'
              '代入得 $\\frac{3\\sqrt{2}}{2}+\\frac{4}{2\\sqrt{2}}+\\frac{1}{\\sqrt{2}}'
              '=\\frac{3\\sqrt{2}}{2}+\\sqrt{2}+\\frac{\\sqrt{2}}{2}=3\\sqrt{2}$，'
              '与选项 A 一致。',
})


if __name__ == '__main__':
    print('准备录入 %d 题' % len(QS))
    ok, res = H.add_many(QS, batch=BATCH)
    if ok:
        print('成功录入 %d 题，ID 段：%s ~ %s' % (len(res), res[0], res[-1]))
    else:
        print('校验未通过：')
        for e in res:
            print('   ', e)
