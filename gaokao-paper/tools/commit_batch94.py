# -*- coding: utf-8 -*-
r"""第 94 批入库：圆锥曲线离心率小题 + 圆锥曲线综合 + 非对称韦达与定点定值
+ 绝对值不等式 + 数学文化型几何概型（13 题）。

| 题型 | 题数 | 内容 |
|---|---:|---|
| M-T-329 | 2 | 斜率之积定值（双曲线为正 / 椭圆为负）反求离心率 |
| M-T-353 | 3 | 共高三角形面积比、倾斜角互余型定点、抛物线切线与四点共圆 |
| M-T-357 | 4 | 非对称韦达的「积化和」：轨迹 / 定比 / 截距比 / 定点 |
| M-T-031 | 2 | 绝对值分段、「1」的代换求右端最大值、倒平方和最值 |
| M-T-407 | 2 | 希波克拉底月牙、剪纸小圆（几何概型 + 分母有理化） |

    python3 tools/commit_batch94.py
"""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, 'py'))
sys.path.insert(0, HERE)

from input_batch94a import QS                     # noqa: E402
import hand_input                                 # noqa: E402
import kp_catalog as K                            # noqa: E402

BATCH = '教辅录入-第94批-圆锥曲线综合与绝对值不等式'


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
