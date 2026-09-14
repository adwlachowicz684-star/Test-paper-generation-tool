# -*- coding: utf-8 -*-
r"""第 101 批入库：立体几何解答题（平行证明 + 角与距离计算），12 题。

| 题型 | 题数 | 内容 |
|---|---:|---|
| M-T-312 | 2 | 平行四边形与中位线证线面平行；建系求二面角与线面角 |
| M-T-313 | 1 | 相似比配重心性质；等体积转换求体积 |
| M-T-314 | 3 | 做平行平面证线面平行；建系求二面角与点到面距离 |
| M-T-315 | 2 | 线面垂直判定；存在性讨论（唯一性反证） |
| M-T-316 | 1 | 圆柱表面积；向量相等证面面平行 |
| M-T-317 | 2 | 正四棱锥对称性；公理 3 证三点共线 |
| M-T-318 | 1 | 勾股定理逆定理证线面垂直；多面体体积比 |

    python3 tools/commit_batch101.py
"""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, 'py'))
sys.path.insert(0, HERE)

from input_batch101 import QS                     # noqa: E402
import hand_input                                 # noqa: E402
import kp_catalog as K                            # noqa: E402

BATCH = '教辅录入-第101批-立体几何平行与角距离'


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
