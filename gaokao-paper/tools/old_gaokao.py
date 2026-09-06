# -*- coding: utf-8 -*-
r"""老高考内容判定：江苏 2021 年起考新高考，这些内容不再考。

    python3 tools/old_gaokao.py            # 列出全部老高考题与统计
    python3 tools/old_gaokao.py keys       # 只输出 key，供其他脚本消费

**判定依据（两条，任一命中即算）**

1. 小知识点为「不等式选讲」——柯西不等式、绝对值不等式、分析法证明，
   新高考全部删除
2. 题型名里带「(老高考)」——如 T069 线性规划型

**为什么单独建这个文件**

判定规则散落在 make_plan.py 里会难以复用，且改规则要改多处。
集中到一处后，清单生成、录入脚本、审计脚本用同一份判定。

**为什么要"排除"而不是"标为待录"**

标成"待录入"意味着后面还要处理，清单永远清不掉。
直接排除后，待录数才是真正要做的量，批次计划也才有意义。
排除的题另存一张表，想反悔随时能捞回来。
"""
import json, os, sys

sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '..', 'py'))
import kp_catalog as K

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def old_topics():
    """返回老高考题型 ID 集合，附判定理由。"""
    out = {}
    for t, info in K.TOPICS.items():
        if not t.startswith('M-T-'):
            continue
        name = info.get('name', '')
        l1, l2 = info.get('primary') or ('?', '?')
        if l2 == '不等式选讲':
            out[t] = '不等式选讲（柯西/绝对值不等式），新高考不考'
        elif '老高考' in name:
            out[t] = '题型名标注为老高考内容'
    return out


def old_keys(ref=None):
    """返回老高考题目的 ref_bank key 集合。"""
    if ref is None:
        ref = json.load(open(os.path.join(ROOT, 'data', 'ref_bank.json'),
                             encoding='utf-8'))
    ot = old_topics()
    out = {}
    for k, v in ref.items():
        t = v.get('topic') or k.rsplit('-', 1)[0]
        if t in ot:
            out[k] = ot[t]
    return out


def main():
    ref = json.load(open(os.path.join(ROOT, 'data', 'ref_bank.json'),
                         encoding='utf-8'))
    PAGES = {}
    p = os.path.join(ROOT, 'tools', '_toc_pages.json')
    if os.path.exists(p):
        PAGES = json.load(open(p, encoding='utf-8'))
    ok_ = old_keys(ref)
    if len(sys.argv) > 1 and sys.argv[1] == 'keys':
        print('\n'.join(sorted(ok_)))
        return 0
    ot = old_topics()
    print('  老高考题型 %d 个：' % len(ot))
    for t in sorted(ot):
        ks = [k for k in ref
              if (ref[k].get('topic') or k.rsplit('-', 1)[0]) == t]
        print('    %-9s %-38s p%-5s %2d题  %s'
              % (t.replace('M-T-', 'T'), K.TOPICS[t].get('name', '')[:36],
                 PAGES.get(t, '?'), len(ks), ot[t]))
    print('\n  老高考题目共 %d 题（占教辅总数 %d 的 %.1f%%）'
          % (len(ok_), len(ref), 100.0 * len(ok_) / max(1, len(ref))))
    return 0


if __name__ == '__main__':
    sys.exit(main())
