# -*- coding: utf-8 -*-
r"""第 102 批入库：导数压轴证明题（零点个数 · 三个极值点 · 比值代换 · 极值点偏移），12 题。

| 题型 | 题数 | 内容 |
|---|---:|---|
| M-T-152 | 3 | 单调性与零点个数；分段讨论；导函数零点存在性 |
| M-T-164 | 3 | 三个极值点排序；比值代换 $t=\frac{x_1}{x_2}$；对称化辅助函数 |
| M-T-169 | 3 | 隐零点代换；$e^{2x}\ge1+2x+2x^2$ 配 $\ln x\le x-1$；单调性分类 |
| M-T-172 | 3 | 极值点偏移；对数平均不等式；倒数比较法 |

    python3 tools/commit_batch102.py
"""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, 'py'))
sys.path.insert(0, HERE)

from input_batch102 import QS                     # noqa: E402
import hand_input                                 # noqa: E402
import kp_catalog as K                            # noqa: E402

BATCH = '教辅录入-第102批-导数压轴证明'


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
