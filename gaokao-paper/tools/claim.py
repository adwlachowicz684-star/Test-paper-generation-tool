#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""并行录入的认领工具：申请一段题型，避免两个窗口撞车。

    python3 tools/claim.py                    # 看当前占用情况
    python3 tools/claim.py 窗口A 4            # 窗口A 认领 4 个题型
    python3 tools/claim.py 窗口A --release    # 完工，释放
    python3 tools/claim.py --reset            # 清空全部认领（慎用）

## 为什么需要

多个窗口并行录题时，如果两个窗口都看上 M-T-060，
两边各录一遍，合并时就重复了。`_claims/` 就是那块小白板。

## 并发安全：每个窗口只写自己的文件

**不要用一个共享的 `_claims.json`**——两个窗口同时认领时，
后写的会整份覆盖先写的，先认领的那段就"消失"了，于是两个窗口撞车。

正确做法是**每个窗口只写自己的文件，读时合并所有人的**：

```
tools/_claims/
├── 窗口A.json     只由窗口A写
├── 窗口B.json     只由窗口B写
└── 窗口C.json     只由窗口C写
```

窗口A写 `窗口A.json` 时永远不会碰到 `窗口B.json`，
所以不存在覆盖。读的时候把目录下所有 json 合并起来看即可。

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

# 认领状态目录：每个窗口一个独立 json，互不覆盖
CLAIM_DIR = os.path.join(HERE, '_claims')
STATE = os.path.join(HERE, '_claims.json')   # 旧版遗留，仅用于迁移


def _safe(name):
    """窗口名 → 安全文件名（防止路径穿越与非法字符）。"""
    return re.sub(r'[^\w\u4e00-\u9fff.-]', '_', name)[:64]


def load_state():
    """合并 _claims/ 下所有窗口的认领文件。

    每个文件只由它自己的窗口写，所以读时合并、不会互相覆盖。
    """
    out = {}
    d = CLAIM_DIR
    if not os.path.isdir(d):
        # 兼容旧版单文件
        if os.path.exists(STATE):
            try:
                old = json.load(open(STATE, encoding='utf-8'))
                if isinstance(old, dict):
                    return old
            except Exception:      # noqa: BLE001
                pass
        return out
    for fn in sorted(os.listdir(d)):
        if not fn.endswith('.json'):
            continue
        who = fn[:-5]
        try:
            v = json.load(open(os.path.join(d, fn), encoding='utf-8'))
        except Exception:          # noqa: BLE001
            continue
        if isinstance(v, list):
            out[who] = v
        elif isinstance(v, dict):
            out[who] = v.get('topics') or []
    return out


def save_state(who, topics):
    """只写自己那一个文件——别的窗口的文件碰都不碰。"""
    os.makedirs(CLAIM_DIR, exist_ok=True)
    p = os.path.join(CLAIM_DIR, _safe(who) + '.json')
    json.dump({'who': who, 'topics': topics,
               'ts': __import__('datetime').date.today().isoformat()},
              open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    # 旧版单文件若还在，一并同步（避免老脚本读到脏数据）
    if os.path.exists(STATE):
        try:
            old = json.load(open(STATE, encoding='utf-8'))
            if isinstance(old, dict):
                old.pop(who, None)
                json.dump(old, open(STATE, 'w', encoding='utf-8'),
                          ensure_ascii=False, indent=1)
        except Exception:          # noqa: BLE001
            pass


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

    # 老高考题型（柯西/绝对值不等式、线性规划）新高考不考，
    # make_plan 把它们归为「不录(老高考)」，不参与分批。
    # **认领时必须同样排除**——否则窗口会领到整段不该录的题，
    # 白白浪费几批工作量（实测第18批就录进去了 8 题）。
    sys.path.insert(0, HERE)
    try:
        import old_gaokao as OG
        old_topics = set(OG.old_topics())
    except Exception:      # noqa: BLE001
        old_topics = set()

    by = defaultdict(int)
    for k in ref:
        m = re.match(r'(M-T-\d+)-', k)
        if not m:
            continue
        if k in done or k in dup or k in skip:
            continue
        if m.group(1) in old_topics:
            continue
        by[m.group(1)] += 1
    return sorted(by.items(), key=lambda x: int(x[0].split('-')[2]))


def collect_skips():
    """汇总 _claims/ 下所有 *_skip.json，返回 {窗口名: [条目]}。"""
    out = {}
    if not os.path.isdir(CLAIM_DIR):
        return out
    for fn in sorted(os.listdir(CLAIM_DIR)):
        if not fn.endswith('_skip.json'):
            continue
        who = fn[:-len('_skip.json')]
        try:
            d = json.load(open(os.path.join(CLAIM_DIR, fn), encoding='utf-8'))
        except Exception:          # noqa: BLE001
            continue
        if d:
            out[who] = d
    return out


def main():
    a = [x for x in sys.argv[1:] if not x.startswith('-')]
    fl = [x for x in sys.argv[1:] if x.startswith('-')]
    st = load_state()

    if '--reset' in fl:
        import shutil
        if os.path.isdir(CLAIM_DIR):
            shutil.rmtree(CLAIM_DIR)
        if os.path.exists(STATE):
            os.remove(STATE)
        print('  已清空全部认领')
        return 0

    # 跳过标记：各窗口写自己的独立文件，避免覆盖共享的 skipped.json
    # 用法：tools/claim.py 窗口A --skip M-T-047-V2 --reason 答案存疑
    if '--skip' in sys.argv:
        i = sys.argv.index('--skip')
        key = sys.argv[i + 1] if i + 1 < len(sys.argv) else None
        rsn = '待核查'
        if '--reason' in sys.argv:
            j = sys.argv.index('--reason')
            if j + 1 < len(sys.argv):
                rsn = sys.argv[j + 1]
        if not key:
            print('  用法：--skip <题号> [--reason <原因>]')
            return 1
        who = a[0] if a else '匿名'
        fp = os.path.join(CLAIM_DIR, _safe(who) + '_skip.json')
        d = []
        if os.path.exists(fp):
            try:
                d = json.load(open(fp, encoding='utf-8'))
            except Exception:      # noqa: BLE001
                d = []
        if any(x.get('key') == key for x in d):
            print('  %s 已标记过' % key)
        else:
            d.append({'key': key, 'reason': rsn, 'by': who})
            os.makedirs(CLAIM_DIR, exist_ok=True)
            json.dump(d, open(fp, 'w', encoding='utf-8'),
                      ensure_ascii=False, indent=1)
            print('  %s 已记入 %s（待合并窗口统一写入 skipped.json）'
                  % (key, os.path.basename(fp)))
        return 0

    # 释放
    if '--release' in fl and a:
        who = a[0]
        if who in st:
            got = st[who]
            fp = os.path.join(CLAIM_DIR, _safe(who) + '.json')
            if os.path.exists(fp):
                os.remove(fp)
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
        pend = collect_skips()
        if pend:
            print('\n待合并的跳过标记（各窗口独立文件，不会互相覆盖）：')
            for who, items in sorted(pend.items()):
                print('  %-10s %s' % (who,
                      ', '.join('%s(%s)' % (x['key'], x['reason'])
                                for x in items)))
            print('  合并：python3 tools/merge_batches.py --apply-skip')
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
    save_state(who, got)
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
