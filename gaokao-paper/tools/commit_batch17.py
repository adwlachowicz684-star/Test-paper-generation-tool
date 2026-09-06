# -*- coding: utf-8 -*-
r"""补录第 8、9 批：T070 / T071 / T072 共 11 题。

    python3 tools/commit_batch17.py

与前面几批的两点不同：
  1. topics 用列表（题目⇄题型本就是多对多），不再用单值 d['topic']
  2. 含一道图题（M-T-071-E1），figs 的 file 依赖入库后生成的 ID，
     故先按预估 ID 切图，入库后再校验实际 ID 是否吻合

kp / kp2 从 kp_catalog 按 topic 自动查，不手写。
"""
import sys
import os
import re
import json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, 'py'))
sys.path.insert(0, HERE)

from input_batch17 import QS                      # noqa: E402
import hand_input                                 # noqa: E402
import kp_catalog as K                            # noqa: E402

BATCH = '教辅录入-第17批-补录'
SLICE = os.path.join(ROOT, 'src', 'slices', '数学')
PDF = '/data/inputs/2024高中数学热点题型归纳完整解析版.pdf'

# 图题在 QS 中的下标与它在 PDF 中的裁切框（页45 右栏两张并排图）
# 边界已校验：外扩 6~14 单位无相邻题目文本混入，图内无文字
FIG_QIDX = 4                       # T071_E1 在 QS 中的位置
FIG_BOXES = [(332, 491, 442, 601), (457, 493, 557, 601)]
FIG_PAGE = 45


def predict_id(qs_index):
    """预估第 n 题（0-based）入库后的 ID。

    hand_input.next_id 取 max(M-H\\d+) + 1，按 QS 顺序递增分配。
    """
    bank = hand_input.load()
    mx = 0
    for q in bank:
        m = re.match(r'^M-H(\d+)$', str(q.get('id') or ''))
        if m:
            mx = max(mx, int(m.group(1)))
    return 'M-H%04d' % (mx + qs_index + 1)


def cut_figs(qid):
    """按预估 ID 切图，返回 figs 列表（含真实像素尺寸与体积）。"""
    import pymupdf
    doc = pymupdf.open(PDF)
    pg = doc[FIG_PAGE]
    os.makedirs(SLICE, exist_ok=True)
    figs = []
    for gi, (x0, y0, x1, y1) in enumerate(FIG_BOXES, 1):
        clip = pymupdf.Rect(x0, y0, x1, y1)
        pix = pg.get_pixmap(clip=clip, dpi=300)
        fn = '%s_fig%d.png' % (qid, gi)
        fp = os.path.join(SLICE, fn)
        pix.save(fp)
        kb = os.path.getsize(fp) // 1024
        figs.append({'file': fn, 'w': pix.width, 'h': pix.height, 'kb': kb})
        print('  切图 %s  %dx%d  %dKB' % (fn, pix.width, pix.height, kb))
    return figs


def main():
    before = len(hand_input.load())
    print('入库前 %d 题' % before)

    # 1. 图题：先按预估 ID 切图
    pred = predict_id(FIG_QIDX)
    print('预估图题 ID: %s' % pred)
    figs = cut_figs(pred)

    # 2. 组装题目
    qs = []
    for idx, d in enumerate(QS):
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
            # 占位 file 替换为实际切出的文件名（顺序一一对应）
            item['figs'] = [dict(fg) for fg in figs]
        qs.append(item)

    for q in qs:
        print('  %-12s %s / %s' % (q['topics'][0], q['kp'], q['kp2']))

    # 3. 整批入库
    ok, res = hand_input.add_many(qs, batch=BATCH)
    if not ok:
        print('校验未通过，整批拒绝：')
        for e in res:
            print('  -', e)
        return 1

    # 4. 校验图题实际 ID 与预估是否吻合
    bank = hand_input.load()
    after = len(bank)
    print('入库成功 %d 题（%d → %d），ID: %s ~ %s'
          % (len(res), before, after, res[0], res[-1]))

    actual = None
    for q in bank:
        if q.get('id') == pred:
            actual = pred
            break
    if actual is None:
        print('!! 图题实际 ID 与预估 %s 不符，需重命名图片' % pred)
        for q in bank:
            if q.get('figs') and q.get('batch') == BATCH:
                real = q['id']
                newfigs = []
                for gi, fg in enumerate(q['figs'], 1):
                    old = os.path.join(SLICE, fg['file'])
                    newfn = '%s_fig%d.png' % (real, gi)
                    new = os.path.join(SLICE, newfn)
                    if os.path.exists(old):
                        os.rename(old, new)
                    fg['file'] = newfn
                    newfigs.append(fg)
                q['figs'] = newfigs
                print('  已重命名 -> %s' % real)
        hand_input.save(bank)
    else:
        print('  图题 ID 校验通过: %s（图片 %s_fig1/2.png）' % (pred, pred))

    return 0


if __name__ == '__main__':
    sys.exit(main())
