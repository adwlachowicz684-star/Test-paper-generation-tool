#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""并行录入的认领工具：申请一段题型，避免两个窗口撞车。

    python3 tools/claim.py                    # 看当前占用情况
    python3 tools/claim.py 窗口A 4            # 窗口A 认领 4 个题型
    python3 tools/claim.py 窗口A --release    # 完工，释放
    python3 tools/claim.py --reset            # 清空全部认领（慎用）

## 为什么需要

多个窗口并行录题时，如果两个窗口都看上 M-T-060，
两边各录一遍，合并时就重复了。`_claims.json` 就是那块小白板。

## 认领了什么

一次认领**连续的若干题型**（默认 4 个 ≈ 16 题，约 1 个工作量）。
工具从「待录 > 0 且无人认领」的题型里，挑编号最小的一段给你。
"""
import sys
import os
import re
import json
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, 'py'))

STATE = os.path.join(HERE, '_claims.json')


def load_state():
    if os.path.exists(STATE):
        try:
            return json.load(open(STATE, encoding='utf-8'))
        except Exception:      # noqa: BLE001
            pass
    return {}


def save_state(d):
    json.dump(d, open(STATE, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)


def pending_topics():
    """返回 [(题型, 待录题数)]，按编号升序，只含还有题没录的。"""
    ref = json.load(open(os.path.join(ROOT, 'data', 'ref_bank.json'),
                         encoding='utf-8'))
    bank = json.load(open(os.path.join(ROOT, 'data', 'bank.json'),
                          encoding='utf-8'))
    sk = json.load(open(os.path.join(ROOT, 'data', 'skipped.json'),
                        encoding='utf-8'))
    done = set()
    for q in bank:
        m = re.search(r'(M-T-\d+-(?:E\d+|V\d+))', q.get('src') or '')
        if m:
            done.add(m.group(1))
    skip = {x['key'] for x in sk.get('items', [])}

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

    by = defaultdict(int)
    for k in ref:
        m = re.match(r'(M-T-\d+)-', k)
        if not m:
            continue
        if k in done or k in dup or k in skip:
            continue
        by[m.group(1)] += 1
    return sorted(by.items(), key=lambda x: int(x[0].split('-')[2]))


def main():
    a = [x for x in sys.argv[1:] if not x.startswith('-')]
    fl = [x for x in sys.argv[1:] if x.startswith('-')]
    st = load_state()

    if '--reset' in fl:
        save_state({})
        print('  已清空全部认领')
        return 0

    # 释放
    if '--release' in fl and a:
        who = a[0]
        if who in st:
            got = st.pop(who)
            save_state(st)
            print('  %s 已释放：%s' % (who, ', '.join(got)))
        else:
            print('  %s 没有认领记录' % who)
        return 0

    pend = pending_topics()
    taken = set()
    for v in st.values():
        taken.update(v)
    free = [(t, n) for t, n in pend if t not in taken]

    if not a:      # 只看状态
        print('待录题型 %d 个，其中已认领 %d 个，空闲 %d 个'
              % (len(pend), len(taken), len(free)))
        if st:
            print('\n当前占用：')
            for who, ts in sorted(st.items()):
                print('  %-10s %s' % (who, ', '.join(ts)))
        print('\n空闲的前 12 段（题型 待录题数）：')
        for t, n in free[:12]:
            print('  %-10s %2d 题' % (t, n))
        print('\n认领：python3 tools/claim.py <窗口名> [段数]')
        return 0

    # 认领
    who = a[0]
    if who in st:
        print('  %s 已认领过：%s' % (who, ', '.join(st[who])))
        print('  完工后先 --release 再认领新的')
        return 1
    cnt = int(a[1]) if len(a) > 1 else 4
    if not free:
        print('  没有空闲题型段了')
        return 1
    got = [t for t, _ in free[:cnt]]
    st[who] = got
    save_state(st)
    total = dict(pend)
    print('  %s 认领成功：' % who)
    for t in got:
        print('    %-10s %2d 题' % (t, total[t]))
    print('\n  对应页码见 原件/题型页码索引.md')
    print('  录入时只写 tools/input_batchXX.py，**不要执行入库命令**')
    print('  完工后：python3 tools/claim.py %s --release' % who)
    return 0


if __name__ == '__main__':
    sys.exit(main())
