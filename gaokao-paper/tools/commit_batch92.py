# -*- coding: utf-8 -*-
r"""第 92 批入库：补录第 87 批（立体几何·轨迹与截面，12 题）。

## 为什么是「补录」

第 87 批当时只把 `input_batch87a.py` 推上了远端，**bank.json 的合并没有生效**，
所以这 12 题一直留在待录清单里（M-T-279×2、M-T-278×3、M-T-284×2、M-T-283×1、M-T-289×4）。

本批直接复用 `input_batch87a.QS`（内容无需改动，lint 已过），重新走一遍入库，
把丢掉的 12 题补回题库。

    python3 tools/commit_batch92.py
"""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, 'py'))
sys.path.insert(0, HERE)

from input_batch87a import QS                     # noqa: E402
import hand_input                                 # noqa: E402
import kp_catalog as K                            # noqa: E402

BATCH = '教辅录入-第92批-立体几何轨迹与截面补录'


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
