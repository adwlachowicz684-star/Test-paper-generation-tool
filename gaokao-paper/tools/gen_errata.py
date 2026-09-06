# -*- coding: utf-8 -*-
r"""从 bank.json 的 review 字段自动汇总「与原书不一致」的处理，生成《原书勘误表.md》。

    python3 tools/gen_errata.py

分类：
  A 类  原书【答案】本身判错并改动   —— 人工审核最不可替代的产出
  B 类  PDF 提取丢符号 → 还原        —— 原书无误，是"假错误"
  C 类  答案未改，仅详解/选项笔误
  D 类  存疑，按原书保留

A 类的「原书答案 / 现录入 / 依据」是人工判断的结论，无法从 review 里
自动解析，集中维护在下面的 A_MANUAL 表里；题号或结论有变动时改这里。
B / C / D 类按题号清单从 review 抽取，新增题目时把题号加进对应列表。
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
BANK = os.path.join(ROOT, 'data', 'bank.json')
OUT = os.path.join(ROOT, '原书勘误表.md')

# ── A 类：人工结论，需手工维护 ────────────────────────
# (题号, 来源, 原书答案, 现录入, 依据)
A_MANUAL = [
    ('M-H0009', 'M-T-003-V1', '原书 C', 'B',
     '详解只列 {1,2,3}、{1,2,4}，遗漏 {1,2,3,4}；真包含要求 A≠{1,2}，'
     '{1,2,3,4} 满足，实为 3 个'),
    ('M-H0069', 'M-T-019-V3', r'$\frac{5\sqrt5}{2}\approx5.590$',
     r'$\sqrt5+\sqrt{10\sqrt5}\approx6.9648$',
     r'错在把 $\frac5{c-2}$ 提出 $\sqrt5$ 后写成 $\frac1t$（应为 $\frac{\sqrt5}t$）。'
     r'取等 a≈0.618、b≈1.382、c≈4.115，数值扫描 6.964776 佐证'),
    ('M-H0081', 'M-T-023-E1', r'$(0,\frac{\sqrt6}6]$',
     r'$(\frac25,\frac{\sqrt6}6]$',
     r'解析把 $t$ 与 $t^2$ 范围混淆：$t^2=1+3xy\in(1,\frac85]$，'
     r'故 $t\to1$ 时原式趋于 $\frac25$ 而非 $0$。扫描值域 [0.400000,0.408248] 吻合'),
    ('M-H0176', 'M-T-098-E1', '单调递增', '单调递减',
     '原书【详解】末尾综述与前文「f′(x)<0，单调递减」矛盾；数值抽查 k=1,2,5 均恒减'),
]

# ── B / C 类：题号清单，说明从 review 抽 ──────────────
B_KEYS = ['M-H0018', 'M-H0023', 'M-H0027', 'M-H0029', 'M-H0080', 'M-H0087',
          'M-H0090', 'M-H0091', 'M-H0106', 'M-H0175', 'M-H0186', 'M-H0194',
          'M-H0195', 'M-H0197', 'M-H0199', 'M-H0070', 'M-H0030', 'M-H0033',
          'M-H0061', 'M-H0064', 'M-H0065']

# 第13批（T037~T040 幂指对比较大小）：上标、下标、分数线在提取时全部塌成平文本，
# 16 题全部靠【详解】反推还原，原书无误 —— 归入 B 类。
B_KEYS += ['M-H%04d' % i for i in range(201, 217)]

# 第14批（T041~T045）：同样全部塌成平文本，21 题靠 pdf2latex.py 的字号/基线
# 重建 + 详解反推，原书无误 —— 归入 B 类。
B_KEYS += ['M-H%04d' % i for i in range(217, 238)]


C_KEYS = ['M-H0003', 'M-H0014', 'M-H0021', 'M-H0022', 'M-H0026',
          'M-H0049', 'M-H0055', 'M-H0057', 'M-H0015', 'M-H0019', 'M-H0025']

D_KEYS = ['M-H0101']

# 第14批 T041-V3：数值验证显示四个命题全真（应为 D），原书答案 C 判②为假，
# 但详解「f(e) < f(π)」不等号写反（1/e 是 f 的最大值，必有 f(e) > f(π)）。
# 因③的上标含矢量绘制的根号、无法百分百确认，按原书 C 录入并留待复核。
D_KEYS += ['M-H0220']


def src_short(q):
    s = (q.get('src') or '').split('·')
    return s[-1].strip() if s else q['id']


def why(q):
    """从 review 里抽最能说明"改了什么"的那一句。"""
    r = (q.get('review') or '')
    segs = [s.strip() for s in re.split(r'[。；]', r) if s.strip()]
    hit = [s for s in segs
           if re.search(r'丢失|丢了|缺|提取|还原|重建|无【答案】|截断|码位|'
                        r'私用区|U\+F|笔误|印作|有误|矛盾|重复', s)]
    return (hit[0] if hit else segs[0] if segs else '')[:120]


def main():
    bank = json.load(open(BANK, encoding='utf-8'))
    idx = {q['id']: q for q in bank}
    L = []
    L.append('# 原书勘误与修正记录')
    L.append('')
    L.append('本表由 `tools/gen_errata.py` 从 `data/bank.json` 的 `review` 字段'
             '自动汇总生成，题库变更后重跑该脚本即可刷新。')
    L.append('')
    L.append('> 逐题的完整推理链仍在每题的 `review` 字段里，本表只作索引与速查。')
    L.append('')

    # A
    L.append('## A 类：原书【答案】本身有误，已按正确答案录入')
    L.append('')
    L.append('| 题号 | 来源 | 原书答案 | 现录入 | 依据 |')
    L.append('|---|---|---|---|---|')
    for qid, src, old, new, reason in A_MANUAL:
        if qid not in idx:
            print('  ! A 类 %s 不在题库，跳过' % qid)
            continue
        L.append('| %s | %s | %s | **%s** | %s |' % (qid, src, old, new, reason))
    na = sum(1 for x in A_MANUAL if x[0] in idx)
    L.append('')
    L.append('**A 类共 %d 题。** 这类是真正发现原书印错，'
             '也是人工审核最不可替代的部分。' % na)
    L.append('')

    # B
    L.append('## B 类：PDF 提取丢符号 → 还原（原书本身无误）')
    L.append('')
    L.append('教辅用 MathType/PMExtra 字体排公式，数学符号落在 Unicode 私用区，'
             '常规提取会吞掉。这类**不是原书印错**，而是提取造成的"假错误"，'
             '还原后与原书一致。')
    L.append('')
    L.append('| 题号 | 来源 | 丢的是什么 | 现答案 |')
    L.append('|---|---|---|---|')
    nb = 0
    for qid in B_KEYS:
        q = idx.get(qid)
        if not q:
            print('  ! B 类 %s 不在题库，跳过' % qid)
            continue
        nb += 1
        L.append('| %s | %s | %s | %s |'
                 % (qid, src_short(q), why(q), str(q.get('answer') or '')[:40]))
    L.append('')
    L.append('**B 类共 %d 题。**' % nb)
    L.append('')

    # C
    L.append('## C 类：答案未改，仅详解/选项有笔误')
    L.append('')
    L.append('| 题号 | 来源 | 原书问题 | 现答案 |')
    L.append('|---|---|---|---|')
    nc = 0
    for qid in C_KEYS:
        q = idx.get(qid)
        if not q:
            print('  ! C 类 %s 不在题库，跳过' % qid)
            continue
        nc += 1
        L.append('| %s | %s | %s | %s |'
                 % (qid, src_short(q), why(q), str(q.get('answer') or '')[:40]))
    L.append('')
    L.append('**C 类共 %d 题。** 答案与原书一致，'
             '只修正了推导过程中的笔误或排版错误。' % nc)
    L.append('')

    # D
    L.append('## D 类：存疑，按原书保留')
    L.append('')
    L.append('| 题号 | 来源 | 疑点 | 现答案（按原书） |')
    L.append('|---|---|---|---|')
    nd = 0
    for qid in D_KEYS:
        q = idx.get(qid)
        if not q:
            continue
        nd += 1
        L.append('| %s | %s | %s | %s |'
                 % (qid, src_short(q), why(q), str(q.get('answer') or '')[:40]))
    L.append('')
    L.append('**D 类共 %d 题。** 发现可疑但证据不足以推翻原书，'
             '按原书录入并把疑点记在 review 里，留待复核。' % nd)

    open(OUT, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print('  已生成 %s' % OUT)
    print('  A 类 %d / B 类 %d / C 类 %d / D 类 %d' % (na, nb, nc, nd))
    return 0


if __name__ == '__main__':
    sys.exit(main())
