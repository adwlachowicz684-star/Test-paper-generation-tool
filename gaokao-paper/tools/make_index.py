# -*- coding: utf-8 -*-
r"""生成《原件/题型页码索引》：并行录入的分工表。

    python3 tools/make_index.py

## 为什么需要它

多个窗口并行录题时，每个窗口要先知道**自己那几批在 PDF 的第几页**，
否则每开一个窗口都得重新全文搜索一遍，浪费大量 token。

这份索引把每个题型映射到 PDF 页码，并标出**当前待录题数**，
窗口认领时扫一眼就能挑到还没做的题型，不会两个窗口撞车。

## 页码从哪来

`tools/_toc_pages.json` 是目录（TOC）解析结果，422 个题型各有一个起始页。
题型的**结束页**取下一个题型的起始页减 1（最后一个题型取到全书末尾）。

## 状态从哪来

与 `make_plan.py` 同源，避免两处口径不一致：
已录（bank.json 的 src）、重复（按去公式题干+答案签名）、跳过（skipped.json）。
"""
import os
import sys
import json
import re
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')
sys.path.insert(0, os.path.join(ROOT, 'py'))

OUT = os.path.join(ROOT, '原件', '题型页码索引.md')


def build_inverted(flat, k=24, step=4):
    """把每页文本切成 k 字片段建倒排表：片段 → 页码集合。

    直接对 456 页做 `sig in page` 扫描是 422×456 次字符串匹配，太慢；
    倒排后每次查询是 O(1)。步长取 4 是为了让任意起点的片段都能被命中。
    """
    inv = defaultdict(set)
    for p, t in flat.items():
        n = len(t)
        if n < k:
            inv[t].add(p)
            continue
        for i in range(0, n - k + 1, step):
            inv[t[i:i + k]].add(p)
    return inv


def locate(inv, flat, stem, k=24):
    """用题干定位页码：取中文长串优先，失败再用去空白后的开头。"""
    f = re.sub(r'\s+', '', stem or '')
    zh = re.findall(r'[\u4e00-\u9fff，。、（）]{14,}', f)
    zh.sort(key=len, reverse=True)
    cands = []
    if zh:
        cands.append(zh[0][:k])
    if len(f) >= k:
        cands.append(f[:k])
    for c in cands:
        hits = sorted(inv.get(c, ())) if len(c) >= k else []
        if not hits:
            # 倒排只在步长为 step 的位置采样，签名起点可能落在采样间隙里，
            # 所以 miss 时必须回退全表扫描，否则命中率会从 6/10 掉到 3/10。
            hits = [p for p, t in flat.items() if c in t]
        if hits:
            return hits[0]
    return None


def main():
    ref = json.load(open(os.path.join(ROOT, 'data', 'ref_bank.json'),
                         encoding='utf-8'))
    bank = json.load(open(os.path.join(ROOT, 'data', 'bank.json'),
                          encoding='utf-8'))
    sk = json.load(open(os.path.join(ROOT, 'data', 'skipped.json'),
                        encoding='utf-8'))

    # 已录：从 bank 的 src 里抽题号
    done = set()
    for q in bank:
        m = re.search(r'(M-T-\d+-(?:E\d+|V\d+))', q.get('src') or '')
        if m:
            done.add(m.group(1))
    skip = {x['key'] for x in sk.get('items', [])}

    # 精确判重（与 make_plan 同口径）
    def norm(t):
        t = re.sub(r'\$[^$]*\$', '#', t or '')
        return re.sub(r'[^一-鿿0-9a-zA-Z]', '', t)[:50]

    seen = defaultdict(list)
    for k, v in ref.items():
        seen[(norm(v.get('stem')), (v.get('ans') or '').strip())].append(k)
    dup = set()
    for ks in seen.values():
        if len(ks) > 1:
            dup.update(ks[1:])

    # 页码：TOC 给个大概，再用题干回原文实测校正
    pages = json.load(open(os.path.join(HERE, '_toc_pages.json'),
                           encoding='utf-8'))
    topics = sorted(pages, key=lambda t: int(t.split('-')[2]))
    total_pages = 456

    src_dir = os.path.join(ROOT, '原件', '按页原文')
    flat = {}
    if os.path.isdir(src_dir):
        for fn in sorted(os.listdir(src_dir)):
            if fn.endswith('.txt'):
                p = int(fn[1:4])
                flat[p] = re.sub(r'\s+', '',
                                 open(os.path.join(src_dir, fn),
                                      encoding='utf-8').read())
    print('  载入 %d 页原文，建倒排索引 ...' % len(flat))
    inv = build_inverted(flat)
    # 逐题型实测页码（取该题型第一题的题干定位）
    real = {}
    for t in topics:
        ks = sorted(k for k in ref if k.startswith(t + '-'))
        for k in ks[:2]:
            p = locate(inv, flat, ref[k].get('stem'))
            if p:
                real[t] = p
                break
    print('  实测命中 %d / %d 个题型' % (len(real), len(topics)))

    # 每题型的题号与状态
    by_topic = defaultdict(list)
    for k in ref:
        m = re.match(r'(M-T-\d+)-', k)
        if m:
            by_topic[m.group(1)].append(k)

    L = ['# 题型 → PDF 页码索引（并行录入分工表）', '',
         '由 `tools/make_index.py` 生成，重跑即刷新。', '',
         '**用法**：新开一个录题窗口时，先扫这份表，'
         '挑一个「待录 > 0」且别人没认领的题型段，',
         '然后只读对应的那几页原文（`原件/按页原文/pXXX.txt`），'
         '不必下载 21MB 的完整 PDF。', '',
         '> **页码基准**：本表是 **1-based**（`p032.txt` = 第 32 页）。',
         '> 而 `dump_pdf.py --pages` 与 `pdf2latex.py --page` 用 **0-based**，'
         '> 所以第 32 页要写成 `--pages 31`。', '',
         '> 有些题型的结束页是「?」——TOC 里下一个题型的页码不递增'
         '> （该题型跨到别处或 TOC 有跳跃），此时只给起始页，用 '
         '> `dump_pdf.py --find` 搜特征词定位。', '',
         '| 状态 | 含义 |', '|---|---|',
         '| 待录 | 还没录入，可以做 |',
         '| 已录 | 已入库 |',
         '| 重复 | 与前面某题同题，跳过 |',
         '| 跳过 | 人工裁定不录 |', '',
         '---', '',
         '## 按题型', '',
         '| 题型 | PDF 页 | 原文文件 | 总题 | 待录 | 明细 |',
         '|---|---:|---|---:|---:|---|']

    n_pending = 0
    for i, t in enumerate(topics):
        p0 = real.get(t) or pages.get(t) or 0
        nxt = topics[i + 1] if i + 1 < len(topics) else None
        # 结束页 = 下一个题型起始页 - 1。
        # 但 TOC 里存在页码回退/跳跃（如 M-T-007 标 10、下一个标 229），
        # 这时猜出来的范围毫无意义，宁可标「?」让人用 --find 搜。
        if nxt:
            cand = (real.get(nxt) or pages.get(nxt) or 0) - 1
            p1 = cand if (cand >= p0 and cand - p0 <= 20) else None
        else:
            p1 = total_pages
        keys = sorted(by_topic.get(t, []))
        if not keys:
            continue
        pend, det = [], []
        for k in keys:
            tag = k.rsplit('-', 1)[1]
            if k in done:
                det.append('%s✓' % tag)
            elif k in dup:
                det.append('%s重' % tag)
            elif k in skip:
                det.append('%s跳' % tag)
            else:
                pend.append(k)
                det.append(tag)
        n_pending += len(pend)
        if p1 is None:
            prange = '%d–?' % p0
            pfile = 'p%03d 起' % p0
        elif p1 == p0:
            prange = '%d' % p0
            pfile = 'p%03d' % p0
        else:
            prange = '%d–%d' % (p0, p1)
            pfile = 'p%03d–p%03d' % (p0, p1)
        L.append('| %s | %s | `%s.txt` | %d | **%d** | %s |'
                 % (t, prange, pfile, len(keys), len(pend),
                    ' '.join(det)))

    L += ['', '---', '',
          '## 汇总', '',
          '- 题型总数：%d' % len(topics),
          '- 待录题数：**%d**' % n_pending,
          '- PDF 总页数：%d' % total_pages, '',
          '## 并行录入的注意事项', '',
          '1. **各窗口认领不同题型段**，同一题型不要两个窗口同时做',
          '2. **`bank.json` 是单文件，必然冲突**——见《交接说明》的并行方案：',
          '   各窗口只产出 `input_batchXX.py`，最后统一合并入库',
          '3. 需要字符级确认（`--chars`）或切图时才下载完整 PDF',
          '4. 录完跑 `python3 tools/run_batch.py <批次>` 一键验证',
          '']
    open(OUT, 'w', encoding='utf-8').write('\n'.join(L))
    print('  已生成 %s' % os.path.relpath(OUT, ROOT))
    print('  %d 个题型 / 待录 %d 题' % (len(topics), n_pending))
    return 0


if __name__ == '__main__':
    sys.exit(main())
