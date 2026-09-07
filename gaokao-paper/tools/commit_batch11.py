# -*- coding: utf-8 -*-
r"""第11批入库：T023 超难压轴小题 / T066 一元二次复合型基础，共 8 题。

    python3 tools/commit_batch6.py

kp / kp2 从 kp_catalog 按 topic 自动查，不再手写 ——
本批跨「不等式」与「函数与导数」两个一级知识点，手写容易出错。
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'py'))
sys.path.insert(0, HERE)

from input_batch11 import QS
import hand_input
import kp_catalog as K

BATCH = '教辅录入-第11批'


def main():
    qs = []
    for d in QS:
        pri = (K.TOPICS.get(d['topic']) or {}).get('primary') or ('数学', '未分类')
        qs.append({
            'subject': '数学',
            'type': d['type'],
            'stem_text': d['stem_text'],
            'opts': [list(o) for o in d['opts']],
            'answer': d['answer'],
            # solution_ext 是为了绕开「raw 字符串里写一半又开新串」的引号坑，
            # 这里合并成完整解析。
            'solution': d['solution'] + (d.get('solution_ext') or ''),
            'analysis': d.get('review') or '',
            'kp': pri[0],
            'kp2': pri[1],
            'topics': [d['topic']],
            'src': '2024高中数学热点题型归纳完整解析版.pdf · %s' % d['key'],
            'review': d.get('review') or '',
        })
    for q in qs:
        print('  %-12s %s / %s' % (q['topics'][0], q['kp'], q['kp2']))
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
