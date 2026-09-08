#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""pick_batch.py —— 一键选题：直接给出「这一批录哪些题 + 原文在哪」

## 为什么需要它

原来选题要三步，来回切换：

```
ready_scan.py --top 80        # ① 按页圈范围
cat 原件/按页还原/pXXX.txt      # ② 读原文确认能不能录
ready_topics.py --keys ...    # ③ 查题号是否已录
```

第 31 批我漏了第 ③ 步，**白写了 6 道已录过的题**。
本脚本把三步合成一条命令，从根上避免重复劳动。

    python3 tools/pick_batch.py                      # 推荐下一批（默认 8 题）
    python3 tools/pick_batch.py --n 16               # 要 16 题
    python3 tools/pick_batch.py --topic M-T-126      # 指定题型
    python3 tools/pick_batch.py --dump               # 顺带把原文存成文件

## 选题策略（按优先级）

1. **只要未录的题** —— 与 bank.json 比对，已录的直接排除
2. **优先 A 级** —— 题干完整度（复用 ready_topics.judge）
3. **同一题型优先凑批** —— 原文集中在几页，不用翻来翻去
4. **跨页越少越好** —— 按 (题型, 起始页) 聚类

## 输出

```
  ✓ M-T-126-E1  [A] p093  已知函数f(x)=x²-2x·eˣ，若方程f(x)=a有3个不同的实根…
  ✓ M-T-126-V1  [A] p093  …
  ────────────────────────────────────────
  共 8 题，跨 2 页：p093 p094
  下一步：cat 原件/按页还原/p093.txt
```

## 定位原理

用**题干前 12 个字**在 `原件/按页还原/` 里全文搜索定位页码。
还原版已做过符号还原，所以搜「f(x)」这类能匹配上；
若题干开头是公式（搜不到），会回退到按题型页码范围估算，并标 `?`。
"""
import argparse
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESTORE_DIR = os.path.join(ROOT, '原件', '按页还原')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ready_topics import judge, load_todo   # noqa: E402


def load_restore_pages():
    """读入还原版全部页文本，返回 {页名: 文本}。"""
    pages = {}
    for p in glob.glob(os.path.join(RESTORE_DIR, 'p*.txt')):
        name = os.path.basename(p)[:-4]          # p093
        try:
            pages[name] = open(p, encoding='utf-8').read()
        except Exception:
            pass
    return pages


RE_KEEP = re.compile(r'[^0-9A-Za-z\u4e00-\u9fff]')


def norm(s):
    """归一化：只保留中文/字母/数字，去掉一切空白与标点。"""
    return RE_KEEP.sub('', str(s))


class PageIndex:
    """把 456 页拼成一个大串，一次 find 定位 —— 比逐页 in 快得多。"""

    def __init__(self, pages):
        self.spans = []          # [(start, end, 页名)]
        buf = []
        pos = 0
        for name in sorted(pages.keys()):
            flat = norm(pages[name])
            buf.append(flat)
            self.spans.append((pos, pos + len(flat), name))
            pos += len(flat)
        self.blob = ''.join(buf)
        self.mid = None

    def _bisect(self, p):
        lo, hi = 0, len(self.spans) - 1
        while lo < hi:
            m = (lo + hi) // 2
            if p < self.spans[m][1]:
                hi = m
            else:
                lo = m + 1
        return self.spans[lo][2]

    def find(self, frag):
        p = self.blob.find(frag)
        return self._bisect(p) if p >= 0 else None


def find_page(key, q, pindex):
    """用题干特征定位页码。多位置、多长度尝试。"""
    stem = q.get('stem') or ''
    if isinstance(stem, list):
        stem = '\n'.join(str(x) for x in stem)
    sig = norm(stem)
    if len(sig) < 6:
        return None, '?'
    # 多个起始位置（开头常被题号/「已知」占据，跳过几个再试）
    for start in (0, 4, 8, 14):
        for n in (16, 12, 10, 8):
            if start + n > len(sig):
                continue
            pg = pindex.find(sig[start:start + n])
            if pg:
                return pg, ''
    return None, '?'


def main():
    ap = argparse.ArgumentParser(description='一键选题：给出可录题 + 原文位置')
    ap.add_argument('--n', type=int, default=8, help='这一批要多少题（默认 8）')
    ap.add_argument('--topic', default=None, help='指定题型，如 M-T-126')
    ap.add_argument('--level', default='A,B',
                    help='接受的完整度级别，逗号分隔（默认 A,B）')
    ap.add_argument('--dump', action='store_true',
                    help='把命中页的原文存到 /tmp/pick_batch/ 下')
    ap.add_argument('--all', action='store_true', help='列出全部可录题（忽略 --n）')
    a = ap.parse_args()

    rb = json.load(open(os.path.join(ROOT, 'data', 'ref_bank.json'),
                        encoding='utf-8'))
    done = load_todo()
    levels = set(x.strip().upper() for x in a.level.split(','))

    # 1. 过滤：未录 + 级别符合
    cand = []
    for k, q in rb.items():
        if k in done:
            continue
        if a.topic and not k.startswith(a.topic):
            continue
        lv, why = judge(q)
        if lv not in levels:
            continue
        cand.append((k, q, lv, why))

    if not cand:
        print('  没有符合条件的待录题。可放宽 --level A,B,C 或换 --topic')
        return 0

    print('=' * 70)
    print('  待录且完整的题：%d 个' % len(cand))
    print('=' * 70)

    # 2. 定位页码（一次性建倒排，全库只需几秒）
    pages = load_restore_pages()
    print('  已载入还原版 %d 页，建索引中…' % len(pages))
    pindex = PageIndex(pages)
    located = []
    for k, q, lv, why in cand:
        pg, flag = find_page(k, q, pindex)
        located.append((k, q, lv, why, pg, flag))

    # 3. 按 (题型, 页) 聚类，优先凑同一题型
    #    只收能定位到页码的题 —— 定位不到等于给了也找不到原文
    n_ok = sum(1 for it in located if it[4])
    n_fail = len(located) - n_ok
    print('  定位结果：成功 %d、失败 %d（失败的不进清单）' % (n_ok, n_fail))

    from collections import defaultdict
    by_topic = defaultdict(list)
    for it in located:
        if it[4]:                                  # 只要定位成功的
            by_topic[it[0].rsplit('-', 1)[0]].append(it)

    # 题型内排序：能定位到页码的优先，其次按原题号
    for t in by_topic:
        by_topic[t].sort(key=lambda x: (
            x[4] is None,                                   # 定位失败排后面
            x[4] or '',                                     # 再按页码
            int(x[1].get('orig_num') or 999),               # 再按原题号
        ))

    # 4. 选批：贪心 —— 每次挑「同一页上题最多」的题型，跨页最少
    picked = []
    if a.topic:
        picked = (by_topic.get(a.topic, [])[:a.n] if not a.all
                  else by_topic.get(a.topic, []))
    elif a.all:
        for items in by_topic.values():
            picked.extend(items)
    else:
        # 每个题型按页分组
        from collections import defaultdict as _dd
        topic_pages = {}
        for t, items in by_topic.items():
            g = _dd(list)
            for it in items:
                g[it[4]].append(it)
            topic_pages[t] = g

        used = set()
        while len(picked) < a.n:
            best = None
            for t, g in topic_pages.items():
                # 该题型还剩的、页未被选走的题
                avail = [it for pg, its in g.items()
                         if pg not in used for it in its]
                if not avail:
                    continue
                # 找该题型当前最密集的一页
                best_pg = max((pg for pg in g if pg not in used),
                              key=lambda pg: len(g[pg]))
                score = (len(g[best_pg]), t)
                if best is None or score > best[0]:
                    best = (score, best_pg, t, g)
            if best is None:
                break
            _, pg, t, g = best
            take = g[pg][:a.n - len(picked)]
            picked.extend(take)
            used.add(pg)
            # 同题型同页取完，若还有剩余且仍需要，下一轮会换页/换题型
            if len(g[pg]) > len(take):
                topic_pages[t][pg] = g[pg][len(take):]
            else:
                del topic_pages[t][pg]

    # 5. 输出
    print()
    cur_topic = None
    pgset = []
    for k, q, lv, why, pg, flag in picked:
        t = k.rsplit('-', 1)[0]
        if t != cur_topic:
            print('  ── %s ──' % t)
            cur_topic = t
        stem = q.get('stem') or ''
        if isinstance(stem, list):
            stem = '\n'.join(str(x) for x in stem)
        prev = re.sub(r'\s+', ' ', str(stem))[:44]
        ans = re.sub(r'\s+', '', str(q.get('ans') or ''))[:12]
        print('    %-12s [%s] %-5s ans=%-12s %s'
              % (k, lv, (pg or '??') + flag, ans, prev))
        if pg and pg not in pgset:
            pgset.append(pg)

    print('  ' + '-' * 66)
    n_topic = len(set(x[0].rsplit('-', 1)[0] for x in picked))
    print('  共 %d 题，%d 个题型，跨 %d 页：%s'
          % (len(picked), n_topic, len(pgset), ' '.join(sorted(pgset))))

    # 6. 给下一步命令
    print()
    print('  【下一步】')
    if pgset:
        first = sorted(pgset)[0]
        print('    cat 原件/按页还原/%s.txt' % first)
        if len(pgset) > 1:
            print('    （其他页：%s）' % ' '.join(sorted(pgset)[1:]))
    print('    # 写骨架后先跑：python3 tools/lint_input.py tools/input_batchXX.py')

    # 7. --dump：存原文
    if a.dump and pgset:
        outdir = '/tmp/pick_batch'
        os.makedirs(outdir, exist_ok=True)
        for pg in pgset:
            src = os.path.join(RESTORE_DIR, pg + '.txt')
            if os.path.exists(src):
                dst = os.path.join(outdir, pg + '.txt')
                open(dst, 'w', encoding='utf-8').write(
                    open(src, encoding='utf-8').read())
        print()
        print('  原文已存到 %s/（%d 页）' % (outdir, len(pgset)))

    return 0


if __name__ == '__main__':
    sys.exit(main())
