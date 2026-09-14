# -*- coding: utf-8 -*-
r"""第 103 批入库：导数双变量与圆锥曲线定点定值，12 题。

| 题型 | 题数 | 内容 |
|---|---:|---|
| M-T-163 | 3 | 倒数换元 + 极值点偏移；对数平均；绝对值分段双解 |
| M-T-165 | 3 | 和差消参；判别式定号；换元 $x=\ln t$ |
| M-T-347 | 3 | 斜率和为定值 ⟹ 定点；$AM\perp AN$ 的二次齐次式；倾斜角互补 |
| M-T-355 | 3 | 焦点弦向量关系；对称点型定点；共线向量比求范围 |

    python3 tools/commit_batch103.py
"""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, 'py'))
sys.path.insert(0, HERE)

from input_batch103 import QS                     # noqa: E402
import hand_input                                 # noqa: E402
import kp_catalog as K                            # noqa: E402

BATCH = '教辅录入-第103批-导数双变量与圆锥曲线定点'


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
