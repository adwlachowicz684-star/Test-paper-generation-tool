# -*- coding: utf-8 -*-
r"""第15批入库（下之一）：T063~T064 共 8 题：共 2 题。

    python3 tools/commit_batch15.py

由 tools/new_batch.py 生成。kp / kp2 从 kp_catalog 按 topic 自动查，不手写。

图题做法（本脚本已内置处理，按步骤走即可）：
  1. python3 tools/cut_figs.py <pdf> --list <页码>         看图位
  2. python3 tools/cut_figs.py <pdf> --check <页码> --boxes ...  校验边界
  3. python3 tools/cut_figs.py <pdf> --cut <页码> --qid _tmp_题号 --boxes ...
  4. input 的 figs 里 file 填 '_tmp_题号_fig1.png'
入库后本脚本会按实际 ID 自动改名为 {ID}_fig1.png，无需预估 ID。
"""
import sys, os, shutil, json, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, 'py'))
sys.path.insert(0, HERE)

from input_batch15c import QS
import hand_input
import kp_catalog as K

BATCH = '教辅录入-第15批'
SLICE = os.path.join(ROOT, 'src', 'slices', '数学')


def fix_figs(bank, ids):
    """把 _tmp 开头的临时图名改成实际 ID 名，并同步 bank 里的 figs。"""
    n = 0
    for q in bank:
        if q.get('id') not in ids:
            continue
        figs = q.get('figs') or []
        if not figs:
            continue
        new = []
        for gi, fg in enumerate(figs, 1):
            old = fg.get('file') or ''
            if not old.startswith('_tmp'):
                new.append(fg)
                continue
            newf = '%s_fig%d.png' % (q['id'], gi)
            src, dst = os.path.join(SLICE, old), os.path.join(SLICE, newf)
            if os.path.exists(src):
                shutil.move(src, dst)
                n += 1
            else:
                print('  ! 找不到切好的图：%s' % old)
            fg['file'] = newf
            new.append(fg)
        q['figs'] = new
    if n:
        hand_input.save(bank)
    return n


def main():
    qs = []
    for d in QS:
        topic = d['topics'][0]
        pri = (K.TOPICS.get(topic) or {}).get('primary') or ('数学', '未分类')
        item = {
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
        }
        if d.get('figs'):
            item['figs'] = [dict(f) for f in d['figs']]
        qs.append(item)

    ok, res = hand_input.add_many(qs, batch=BATCH)
    if not ok:
        print('  校验未通过，整批拒绝：')
        for e in res:
            print('    -', e)
        return 1
    print('  入库成功 %d 题，ID: %s ~ %s' % (len(res), res[0], res[-1]))

    ids = set(res)
    nf = fix_figs(hand_input.load(), ids)
    if nf:
        print('  图题改名 %d 张 -> 实际 ID' % nf)
    return 0


if __name__ == '__main__':
    sys.exit(main())
