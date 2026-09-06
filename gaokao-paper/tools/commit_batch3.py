# -*- coding: utf-8 -*-
r"""第3批入库：T012~T016（不等式 / 基本不等式），共 18 题。

    python3 tools/commit_batch3.py

**src 格式为什么带 ref_bank key**

前两批 src 写作「2024热点题型归纳 M-T-009 变式4」，
而 ref_bank 的 key 是「M-T-009-V1」（题型内序号）。
PDF 的「变式演练」是跨题型连续编号的 —— 专题7-2 下
变式1~3 属题型一、变式4~6 属题型二、变式7~9 属题型三，
两者对不上，自动映射 41 题只匹配上 17 题，
已录题目被重复计入待录，最后只能手写映射表兜底。

本批起 src 直接写入 ref_bank 的 key：
    '2024热点题型归纳 M-T-012-E1（典例）'
既可读，又能被正则精确提取，无需手写映射。
"""
import sys, os, json, io
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'py'))
sys.path.insert(0, HERE)

from input_batch3 import QS
import hand_input

BATCH = '教辅录入-第3批'
KP, KP2 = '不等式', '基本不等式'


def main():
    qs = []
    for d in QS:
        t = d['topic']
        q = {
            'subject': '数学',
            'type': d['type'],
            'stem_text': d['stem_text'],
            'opts': [list(o) for o in d['opts']],
            'answer': d['answer'],
            'solution': d['solution'],
            'analysis': d.get('review') or '',
            'kp': KP,
            'kp2': KP2,
            'topics': [t],
            'src': '2024热点题型归纳 %s（%s）' % (t, d['kind']),
            'review': d.get('review') or '',
        }
        qs.append(q)

    ok, res = hand_input.add_many(qs, batch=BATCH)
    if not ok:
        print('  校验未通过，整批拒绝：')
        for e in res:
            print('    -', e)
        return 1
    print('  入库成功 %d 题，ID: %s ~ %s' % (len(res), res[0], res[-1]))
    return 0


if __name__ == '__main__':
    sys.exit(main())
