# -*- coding: utf-8 -*-
r"""第4批入库：T017 / T018 / T019 / T020（基本不等式后半），共 13 题。

    python3 tools/commit_batch4.py

沿用第3批的 src 规范：直接写 ref_bank 的 key，
让 _done_map.done_keys() 能用一条正则自动提取，无需手写映射表。
补录题（原 PDF 无【答案】标记被过滤）也按 M-T-XXX-VN 编号，
这些 key 不在 ref_bank 里，不影响待录清单的核算。
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'py'))
sys.path.insert(0, HERE)

from input_batch4 import QS
import hand_input

BATCH = '教辅录入-第4批'
KP, KP2 = '不等式', '基本不等式'


def main():
    qs = []
    for d in QS:
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
            'topics': [d['topic']],
            'src': '2024热点题型归纳 %s（%s）' % (d['key'], d['kind']),
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
