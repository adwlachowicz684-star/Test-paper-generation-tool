# -*- coding: utf-8 -*-
r"""第 93 批入库：数列·构造新数列 + 数列·通项与裂项求和 + 绝对值不等式（12 题）。

| 题型 | 题数 | 内容 |
|---|---:|---|
| M-T-249 | 4 | 配常数累乘、同除 $n(n+1)$ 换元、$S_n=n^{2}a_n$ 退位相减 |
| M-T-265 | 4 | 等比中项求公差、分式递推拆整数、$\sqrt{S}$ 型、裂项求和 |
| M-T-029 | 4 | 绝对值分段去符号、分离参数恒成立、$|u|-|v|$ 型 |

    python3 tools/commit_batch93.py
"""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, 'py'))
sys.path.insert(0, HERE)

from input_batch93a import QS                     # noqa: E402
import hand_input                                 # noqa: E402
import kp_catalog as K                            # noqa: E402

BATCH = '教辅录入-第93批-数列构造与绝对值不等式'


def main():
    before = len(hand_input.load())
    print('入库前 %d 题' % before)

    qs = []
    for d in QS:
        topic = d['topics'][0]
        pri = (K.TOPICS.get(topic) or {}).get('primary') or ('数学', '未分类')
        qs.append({
            'subject': '数学',
            'type': d['type'],
            'stem_text': d['stem_text'],
            'opts': [list(o) for o in d.get('opts', [])],
            'answer': d['answer'],
            'solution': d['solution'],
            'analysis': d.get('analysis') or '',
            'kp': pri[0],
            'kp2': pri[1],
            'topics': d['topics'],
            'src': d['src'],
            'review': d.get('review') or '',
            'difficulty': d.get('difficulty', 0.65),
        })

    for q, d in zip(qs, QS):
        print('  %-12s %s / %s  %s'
              % (q['topics'][0], q['kp'], q['kp2'], d['src'].split(' · ')[-1]))

    ok, res = hand_input.add_many(qs, batch=BATCH)
    if not ok:
        print('校验未通过，整批拒绝：')
        for e in res:
            print('  -', e)
        return 1

    after = len(hand_input.load())
    print('入库成功 %d 题（%d → %d），ID: %s ~ %s'
          % (len(res), before, after, res[0], res[-1]))
    return 0


if __name__ == '__main__':
    sys.exit(main())
