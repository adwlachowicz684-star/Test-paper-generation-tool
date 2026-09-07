#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""全书批量还原 —— 一次性把整本教辅还原成带结构的 LaTeX 文本

    python3 tools/restore_all.py                 # 全本 456 页，约 3.5 分钟
    python3 tools/restore_all.py --start 70 --end 80
    python3 tools/restore_all.py --force         # 忽略缓存重跑

## 为什么这么做

以前是「录一批 → 跑一次 restore」，
现在改成「**先把全书还原好 → 分批从还原文本里抄**」。

实测单页 0.46 秒，456 页约 3.5 分钟，**一次跑完永久受益**：
后面每一批都直接读现成的还原文本，不用再临时跑还原。

## 产出

    原件/按页还原/p001.txt … p456.txt     # 带 LaTeX 结构（录题首选读这个）
    原件/按页还原/_index.json             # 页 → 检出结构数

与已有的 `原件/按页原文/`（未还原的平文本）并列。
**录题时优先读「按页还原」，原文只作对照。**

## 索引怎么用

`_index.json` 记了每页检出多少 \frac / ^ / _，
可以据此快速判断哪些页值得优先处理：

```python
import json
idx = json.load(open('原件/按页还原/_index.json', encoding='utf-8'))
hot = sorted(idx.items(), key=lambda x: -x[1]['n_struct'])[:20]
```

结构数多的页 = 公式密集 = 原来最容易破碎的页。
"""
import argparse
import json
import os
import sys
import time

import pymupdf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from restore import collect, collect_lines, run, _dedup_sqrt  # noqa: E402

PDF = '/data/inputs/2024高中数学热点题型归纳完整解析版.pdf'
OUT = '原件/按页还原'


def main():
    ap = argparse.ArgumentParser(description='全书批量还原')
    ap.add_argument('--pdf', default=PDF)
    ap.add_argument('--start', type=int, default=0, help='起始页(0-based)')
    ap.add_argument('--end', type=int, default=None, help='结束页(不含)')
    ap.add_argument('--force', action='store_true', help='忽略已有文件重跑')
    a = ap.parse_args()

    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    outdir = os.path.join(root, OUT)
    os.makedirs(outdir, exist_ok=True)

    doc = pymupdf.open(a.pdf)
    end = a.end if a.end is not None else len(doc)
    total = end - a.start
    print('  还原 %d ~ %d（共 %d 页）→ %s' % (a.start, end, total, OUT))

    idx, t0, done, skip = {}, time.time(), 0, 0
    for pno in range(a.start, end):
        fp = os.path.join(outdir, 'p%03d.txt' % (pno + 1))
        if os.path.exists(fp) and not a.force:
            skip += 1
            continue
        try:
            page = doc[pno]
            chars = collect(page)
            lines = collect_lines(page)
            rows = run(chars, lines)
            body = []
            for y, txt in rows:
                if txt.strip():
                    body.append(_dedup_sqrt(txt))
            open(fp, 'w', encoding='utf-8').write('\n'.join(body))
            idx['p%03d' % (pno + 1)] = {
                'pdf_page': pno,
                'n_frac': sum(t.count('\\frac') for _, t in rows),
                'n_super': sum(t.count('^') for _, t in rows),
                'n_struct': sum(1 for _, t in rows
                                if '^' in t or '_' in t or '\\frac' in t),
            }
            done += 1
        except Exception as e:
            print('  ! 页 %d 失败：%s' % (pno + 1, e))
            continue
        if done % 50 == 0:
            el = time.time() - t0
            print('    已处理 %d 页，用时 %.0fs，预计还需 %.0fs'
                  % (done, el, el / max(done, 1) * (total - done - skip)))

    # 合并已有索引（--force 只重跑部分页时，别丢掉其它页的记录）
    idxf = os.path.join(outdir, '_index.json')
    old = {}
    if os.path.exists(idxf):
        try:
            old = json.load(open(idxf, encoding='utf-8'))
        except Exception:
            old = {}
    old.update(idx)
    json.dump(old, open(idxf, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)

    print('  完成：新还原 %d 页，跳过 %d 页，用时 %.0fs'
          % (done, skip, time.time() - t0))
    print('  产出：%s/' % OUT)
    return 0


if __name__ == '__main__':
    sys.exit(main())
