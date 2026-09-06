# -*- coding: utf-8 -*-
r"""生成一批录入脚本的骨架，只留题目内容等你填。

    python3 tools/new_batch.py 18 -t M-T-073:4 -t M-T-074:3
    python3 tools/new_batch.py 18 -t M-T-080:2 --type 填空
    python3 tools/new_batch.py 18 -t M-T-081:3 --pdf 自定义路径.pdf

含义：第 18 批，M-T-073 出 4 题、M-T-074 出 3 题（共 7 个骨架）。
生成 tools/input_batch18.py，里面每个题的变量名、topics、src、题型都填好，
你只需要补 stem_text / opts / answer / analysis / solution / review。

src 编号按题型内顺序自动编：第一道 E1，之后 V1、V2、V3……
difficulty 给一个常用默认值，按需改。

填完直接跑：python3 tools/run_batch.py 18
"""
import argparse
import os

HERE = os.path.dirname(os.path.abspath(__file__))
PDF_DEFAULT = '/data/inputs/2024高中数学热点题型归纳完整解析版.pdf'

# 题型 → 默认难度
DIFF = {'选择': 0.5, '填空': 0.55, '解答': 0.7}

HEADER = '''# -*- coding: utf-8 -*-
r"""{title}

    python3 tools/run_batch.py {n}

由 tools/new_batch.py 生成骨架，题目内容待填。
书写规范（三条都真踩过）：
  1. LaTeX 一律用 raw 双引号 r"..."，因为 f'(x) 的撇号会截断单引号串
  2. 中文行文用弯引号“”，不用 ASCII 双引号（会提前终止 r"..."）
  3. review 字段写清改了什么、为什么，这是人工录入的全部价值
"""

'''

TPL_CHOICE = '''{var} = {{
    'type': '{type}',
    'stem_text': (
        r""                      # ← 题干
    ),
    'opts': [
        ('A', r""),
        ('B', r""),
        ('C', r""),
        ('D', r""),
    ],
    'answer': '',                # ← 多选写 'ACD'
    'analysis': r"",             # ← 一句思路
    'solution': (
        r""                      # ← 详解，用 "\\n" 换行
    ),
    'review': r"",               # ← 核了什么、改了什么
    'difficulty': {diff},
    'topics': ['{topic}'],
    'src': '{pdfname} · {tag}',
}}

'''

TPL_OPEN = '''{var} = {{
    'type': '{type}',
    'stem_text': (
        r""                      # ← 题干
    ),
    'answer': r"",               # ← 填空/解答的答案
    'analysis': r"",
    'solution': (
        r""                      # ← 详解，用 "\\n" 换行
    ),
    'review': r"",
    'difficulty': {diff},
    'topics': ['{topic}'],
    'src': '{pdfname} · {tag}',
}}

'''


COMMIT_TPL = '''# -*- coding: utf-8 -*-
r"""第{n}批入库：共 {total} 题。

    python3 tools/commit_batch{n}.py

由 tools/new_batch.py 生成。kp / kp2 从 kp_catalog 按 topic 自动查，不手写。

图题做法（本脚本已内置处理，按步骤走即可）：
  1. python3 tools/cut_figs.py <pdf> --list <页码>         看图位
  2. python3 tools/cut_figs.py <pdf> --check <页码> --boxes ...  校验边界
  3. python3 tools/cut_figs.py <pdf> --cut <页码> --qid _tmp_题号 --boxes ...
  4. input 的 figs 里 file 填 '_tmp_题号_fig1.png'
入库后本脚本会按实际 ID 自动改名为 {{ID}}_fig1.png，无需预估 ID。
"""
import sys, os, shutil, json, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, 'py'))
sys.path.insert(0, HERE)

from input_batch{n} import QS
import hand_input
import kp_catalog as K

BATCH = '教辅录入-第{n}批'
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
        pri = (K.TOPICS.get(topic) or {{}}).get('primary') or ('数学', '未分类')
        item = {{
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
        }}
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
'''


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('batch')
    ap.add_argument('-t', '--topic', action='append', required=True,
                    help='题型与题数，格式 M-T-073:4，可重复')
    ap.add_argument('--type', default='选择', help='默认题型：选择/填空/解答')
    ap.add_argument('--pdf', default=PDF_DEFAULT)
    ap.add_argument('--force', action='store_true', help='覆盖已存在的文件')
    a = ap.parse_args()

    plan = []
    for s in a.topic:
        if ':' not in s:
            raise SystemExit('-t 格式应为 M-T-073:4 或 M-T-073:E1,V2，收到 %r' % s)
        t, n = s.rsplit(':', 1)
        t = t.strip()
        # 两种写法：
        #   M-T-073:4        → 前 4 题，编号 E1/V1/V2/V3
        #   M-T-073:E1,V2   → 精确指定（补录漏题时用这个）
        if n.isdigit():
            tags = ['E1'] + ['V%d' % i for i in range(1, int(n))]
        else:
            tags = [x.strip() for x in n.replace(';', ',').split(',') if x.strip()]
        plan.append((t, tags))

    total = sum(len(tags) for _, tags in plan)
    path = os.path.join(HERE, 'input_batch%s.py' % a.batch)
    if os.path.exists(path) and not a.force:
        print('已存在：%s（加 --force 覆盖）' % path)
        return 1

    pdfname = os.path.basename(a.pdf)
    typ = a.type
    diff = DIFF.get(typ, 0.5)
    tpl = TPL_CHOICE if typ == '选择' else TPL_OPEN

    body = [HEADER.format(title='第%s批录入（%d 题，待填）' % (a.batch, total),
                          n=a.batch)]
    varnames = []
    for topic, tags in plan:
        short = topic.replace('M-T-', 'T').replace('-', '')
        for tag in tags:
            var = '%s_%s' % (short, tag)
            varnames.append(var)
            body.append(tpl.format(var=var, type=typ, diff=diff,
                                   topic=topic, tag='%s-%s' % (topic, tag),
                                   pdfname=pdfname))

    body.append('QS = [\n')
    for v in varnames:
        body.append('    %s,\n' % v)
    body.append(']\n')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(''.join(body))

    print('已生成 %s' % path)
    print('  %d 个题骨架，题型 %s' % (total, typ))
    for topic, tags in plan:
        print('    %-10s %d 题  %s' % (topic, len(tags), '、'.join(tags)))

    # 同时生成入库脚本，省得手抄
    cpath = os.path.join(HERE, 'commit_batch%s.py' % a.batch)
    if os.path.exists(cpath) and not a.force:
        print('  入库脚本已存在，跳过：%s' % os.path.basename(cpath))
    else:
        with open(cpath, 'w', encoding='utf-8') as f:
            f.write(COMMIT_TPL.format(n=a.batch, total=total))
        print('  已生成入库脚本 %s' % os.path.basename(cpath))

    print('')
    print('下一步：')
    print('  1. 填内容   python3 tools/dump_pdf.py <pdf> --find \'特征词\'')
    print('  2. 一键跑   python3 tools/run_batch.py %s' % a.batch)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
