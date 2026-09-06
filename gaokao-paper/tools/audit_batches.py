# -*- coding: utf-8 -*-
r"""审计：批次脚本是否存在，以及它们声称覆盖的题型在库中有几道题。

    python3 tools/audit_batches.py

**为什么需要这个脚本**

第 8、9、15 批都出过同一种事故：报告写了"已完成 N 题"，
但录入脚本压根不存在，或者脚本存在却没有执行，
题库里一道题都没有。

三次事故的共同点是**用推算代替查证**：
"上一批题数 + 本批计划题数" 看起来合理，但流程被打断时完全不可信。

本脚本做两件静态检查（不需要跑录入）：

1. 录入脚本是否存在（input_batchN.py / commit_batchN.py）
2. 脚本里 `topic='M-T-xxx'` 声称覆盖的题型，在 bank.json 里实际有几道题

**某批声称覆盖的题型在库中为 0 道，就是可疑信号**，必须人工确认。

已知的历史差异（不是 bug）：
  - 第 1 批用 `tools/batch1_input.py`（命名不统一），无 input_batch1.py
  - 第 2 批用 `tools/input_batch2.py`，无 commit_batch2.py（入库走其他入口）
"""
import os, re, json, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def bank_counts():
    p = os.path.join(ROOT, 'data', 'bank.json')
    b = json.load(open(p, encoding='utf-8'))
    c = Counter()
    for q in b:
        m = re.search(r'(M-T-\d+)', q.get('src') or '')
        if m:
            c[m.group(1)] += 1
    return c


def main():
    c = bank_counts()
    names = {}
    for n in range(1, 40):
        for fn in ('input_batch%d.py' % n, 'batch%d_input.py' % n):
            p = os.path.join(HERE, fn)
            if os.path.exists(p):
                names.setdefault(n, []).append(fn)
    if not names:
        print('  未找到任何批次脚本')
        return 0

    print('  %-6s %-26s %-18s %s' % ('批次', '录入脚本', 'commit脚本', '声称题型 → 库内题数'))
    suspicious = []
    for n in sorted(names):
        fis = names[n]
        fc = 'commit_batch%d.py' % n
        has_c = os.path.exists(os.path.join(HERE, fc))
        ts = set()
        for fi in fis:
            src = open(os.path.join(HERE, fi), encoding='utf-8').read()
            # 两种写法都要认：老批次 topic='M-T-001'，新批次 'topics': ['M-T-070']。
            # 只认前者会让用推荐写法（多对多）的新批次静默逃过审计——
            # 表现为「声称题型」一列空着，看不出异常。
            ts |= set(re.findall(
                r"['\"]?topics?['\"]?\s*[:=]\s*\[?\s*['\"](M-T-\d+)['\"]", src))
        detail = ' '.join('%s:%d' % (t.replace('M-T-', 'T'), c.get(t, 0))
                          for t in sorted(ts))
        zero = [t for t in sorted(ts) if c.get(t, 0) == 0]
        flag = ''
        if zero:
            flag = '   ★ 库内 0 道: ' + ','.join(z.replace('M-T-', 'T') for z in zero)
            suspicious.append((n, zero))
        print('  第%02d批 %-26s %-18s %s%s'
              % (n, ','.join(fis), fc if has_c else '—', detail or '—', flag))

    # 批次编号连续性——第 8、9 批是"整个脚本不存在"，
    # 靠"声称题型在库中 0 道"查不出来（没脚本就没声称），
    # 只能靠编号断号发现。
    nums = sorted(names)
    missing = [n for n in range(1, max(nums) + 1) if n not in names]

    print('')
    bad = False
    if missing:
        bad = True
        print('  ★ 批次编号断号（脚本不存在）：第%s批' % '、'.join('%02d' % n for n in missing))
        print('    这些批次的题目可能根本没入库——去《教辅录入任务计划清单.xlsx》')
        print('    的「题目明细」里按状态筛选核对。')
    if suspicious:
        bad = True
        print('  ★ 需人工确认 %d 批：' % len(suspicious))
        for n, zero in suspicious:
            print('     第%02d批：%s 在库中 0 道'
                  % (n, ','.join(z.replace('M-T-', 'T') for z in zero)))
    if not bad:
        print('  批次编号连续，且所有声称覆盖的题型在库中均有题目 OK')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
