#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""ready_topics.py —— 按「题干完整度」筛出可录的待录题

## 与 ready_scan.py 的区别

    ready_scan.py    按**页**评破碎度（宏观，快速圈定范围）
    ready_topics.py  按**题**评完整度（精确，直接给出可录清单）

先跑前者圈页，再跑后者选题 —— 这是推荐顺序。

    python3 tools/ready_topics.py              # 输出可录题清单（按题型分组）
    python3 tools/ready_topics.py --topic M-T-036
    python3 tools/ready_topics.py --level A    # 只要 A 级（最干净）
    python3 tools/ready_topics.py --limit 40   # 最多列 40 题

## 判据：直接看素材题的 stem 有多碎

| 信号 | 含义 |
|---|---|
| `⟨?⟩` | 未识别私用区字符（根号/特殊符号） |
| 疑似分离的分子分母 | 孤立的纯数字短行 |
| **题干过短** | < 25 字，多半提取不全 |
| 括号不配对 | 丢了半边括号 |

**A 级** = 四项全无，**B 级** = 轻微，**C 级** = 需人工补，**D 级** = 跳过。

## 注意

题干完整 ≠ 选项完整。本脚本只判 **stem**，
选项是否可读仍需录题时人工看一眼（选项常带根号，是重灾区）。
"""
import argparse
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RE_UNK = re.compile(r'⟨\?⟩')


def load_todo():
    """从计划清单取待录题的 key 集合。"""
    done = set()
    p = os.path.join(ROOT, 'data', '_done_map.json')
    if os.path.exists(p):
        try:
            d = json.load(open(p, encoding='utf-8'))
            done = set(d.keys()) if isinstance(d, dict) else set(d)
        except Exception:
            pass
    # 题库里已入库的题号
    bank = json.load(open(os.path.join(ROOT, 'data', 'bank.json'),
                          encoding='utf-8'))
    for q in bank:
        src = q.get('src', '') or ''
        m = re.search(r'(M-T-\d+-(?:E\d+|V\d+))', src)
        if m:
            done.add(m.group(1))
    return done


def judge(q):
    """返回 (级别, 说明)。A 最干净。"""
    stem = (q.get('stem') or '')
    if isinstance(stem, list):
        stem = '\n'.join(str(x) for x in stem)
    stem = str(stem)

    prob = []
    n_unk = len(RE_UNK.findall(stem))
    if n_unk:
        prob.append('⟨?⟩×%d' % n_unk)

    # 孤立数字行（分子/分母残留）
    lines = [l.strip() for l in stem.split('\n') if l.strip()]
    n_num = sum(1 for l in lines
                if re.match(r'^[\d\s\.\-−—]+$', l) and len(l) <= 10)
    if n_num:
        prob.append('孤行×%d' % n_num)

    if len(stem.strip()) < 25:
        prob.append('过短(%d字)' % len(stem.strip()))

    d = abs(stem.count('(') - stem.count(')'))
    if d >= 2:
        prob.append('括号差%d' % d)

    if not prob:
        return 'A', ''
    if n_unk == 0 and n_num <= 1 and len(stem.strip()) >= 25:
        return 'B', ' '.join(prob)
    if n_unk <= 2:
        return 'C', ' '.join(prob)
    return 'D', ' '.join(prob)


def main():
    ap = argparse.ArgumentParser(description='按题干完整度筛出可录的待录题')
    ap.add_argument('--keys', nargs='*', default=None,
                    help='直接查指定题号的状态（**录题前必做**）'
                         '，如 --keys M-T-049-V1 M-T-050-V3')
    ap.add_argument('--topic', default=None, help='只看某题型')
    ap.add_argument('--level', default=None,
                    help='只要该级别（A/B/C/D），可逗号分隔如 A,B')
    ap.add_argument('--limit', type=int, default=60, help='最多列多少题')
    a = ap.parse_args()

    rb = json.load(open(os.path.join(ROOT, 'data', 'ref_bank.json'),
                        encoding='utf-8'))
    done = load_todo()

    # --keys：直接查指定题号是否已录（写骨架前必做！）
    if a.keys:
        bank = json.load(open(os.path.join(ROOT, 'data', 'bank.json'),
                              encoding='utf-8'))
        idmap = {}
        for q in bank:
            m = re.search(r'(M-T-\d+-(?:E\d+|V\d+))', q.get('src', '') or '')
            if m:
                idmap[m.group(1)] = q.get('id')
        print('=' * 66)
        print('  题号状态查询（✓=可做  ✗=已录，别写）')
        print('=' * 66)
        n_ok = 0
        for k in a.keys:
            if k in idmap:
                print('    ✗ %-12s 已录为 %s' % (k, idmap[k]))
            elif k not in rb:
                print('    ? %-12s ref_bank 里没有这个 key' % k)
            else:
                lv, why = judge(rb[k])
                prev = (rb[k].get('stem') or '')[:44].replace('\n', ' ')
                print('    ✓ %-12s 待录 [%s] %s' % (k, lv, prev))
                n_ok += 1
        print('  ' + '-' * 62)
        print('  共 %d 个：可做 %d、已录/无效 %d'
              % (len(a.keys), n_ok, len(a.keys) - n_ok))
        return 0

    want = None
    if a.level:
        want = set(x.strip().upper() for x in a.level.split(','))

    rows = []
    for k, q in sorted(rb.items()):
        if k in done:
            continue
        if a.topic and not k.startswith(a.topic):
            continue
        lv, why = judge(q)
        if want and lv not in want:
            continue
        rows.append((lv, k, q.get('orig_num'), why,
                     (q.get('stem') or '')[:38].replace('\n', ' ')))

    order = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    rows.sort(key=lambda r: (order[r[0]], r[1]))

    print('=' * 76)
    print('  待录题完整度筛选   （A 最干净，D 建议跳过）')
    print('=' * 76)
    cur = None
    n = 0
    for lv, k, on, why, prev in rows:
        if n >= a.limit:
            break
        t = k.rsplit('-', 1)[0]
        if t != cur:
            print('  ── %s ──' % t)
            cur = t
        print('    [%s] %-12s orig=%-4s %s%s'
              % (lv, k, on, prev, ('  ⚠ ' + why) if why else ''))
        n += 1

    cnt = {}
    for r in rows:
        cnt[r[0]] = cnt.get(r[0], 0) + 1
    print('  ' + '-' * 72)
    print('  待录共 %d 题：A %d / B %d / C %d / D %d'
          % (len(rows), cnt.get('A', 0), cnt.get('B', 0),
             cnt.get('C', 0), cnt.get('D', 0)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
