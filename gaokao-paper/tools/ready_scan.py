#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""ready_scan.py —— 扫还原版，找出「可录的完整题」

## 为什么需要它

还原版 456 页里，有些页公式完整、有些页满是 `⟨?⟩`（未识别的私用区字符）
和分离的分子分母。以前是**翻到哪录到哪**，遇到破碎页才跳过，来回折腾。

本脚本反过来：**先扫全书算出每页的「破碎度」，按页排优先级**，
录题时直接从最干净的页开始，破碎页整体跳过。

    python3 tools/ready_scan.py                    # 全书扫描，输出 TOP 50
    python3 tools/ready_scan.py --pages 84 85 86   # 只看指定页
    python3 tools/ready_scan.py --topic M-T-125    # 看某个题型所在页
    python3 tools/ready_scan.py --top 100          # TOP 100

## 破碎度怎么算

| 信号 | 权重 | 说明 |
|---|---|---|
| `⟨?⟩` | ×3 | 未识别私用区字符，最硬的伤（根号、特殊符号） |
| 纯数字孤行 | ×2 | 分子/分母与分数线分离后残留的碎片行 |
| 括号不配对 | ×2 | `(` 与 `)` 数量不等，多半丢了半边 |
| 结构占比 | ×1 | 含 `\frac`/`^`/`_` 的行越多越可能是公式密集页 |

**分数越低越干净**。0 分 = 完全干净，可以放心录。

## 输出解读

    p234  分=0    frac=12 ^=8  ⟨?⟩=0   ← 最干净，优先录
    p086  分=14   frac=8  ^=3   ⟨?⟩=3   ← 有伤，谨慎
    p090  分=41   frac=5  ^=2   ⟨?⟩=11  ← 破碎严重，跳过

## 与 restore_all.py 的关系

    restore_all.py  产出还原文本（前置步骤，全书跑一次）
    ready_scan.py   评估哪些页可以录（本脚本，可随时重跑）
"""
import argparse
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(ROOT, '原件', '按页还原')
INDEX = os.path.join(ROOT, '原件', '按页还原', '_index.json')

RE_UNK = re.compile(r'⟨\?⟩')
RE_NUMONLY = re.compile(r'^\s*[\d\s\.\-−—]+\s*$')
RE_FRAC = re.compile(r'\\frac')
RE_SCRIPT = re.compile(r'[\^_]')


def score_page(txt):
    """返回 (破碎分, n_frac, n_script, n_unk, 行数)。越低越干净。"""
    lines = [l for l in txt.split('\n') if l.strip()]
    if not lines:
        return 999, 0, 0, 0, 0

    n_unk = len(RE_UNK.findall(txt))
    # 纯数字孤行：分子/分母残留
    n_numonly = sum(1 for l in lines if RE_NUMONLY.match(l) and len(l.strip()) <= 12)
    # 括号不配对
    n_paren = abs(txt.count('(') - txt.count(')')) + abs(txt.count('[') - txt.count(']'))
    n_frac = len(RE_FRAC.findall(txt))
    n_script = len(RE_SCRIPT.findall(txt))

    s = n_unk * 3 + n_numonly * 2 + n_paren * 2
    return s, n_frac, n_script, n_unk, len(lines)


def main():
    ap = argparse.ArgumentParser(description='扫还原版，找出可录的完整题')
    ap.add_argument('--pages', nargs='*', type=int, default=None,
                    help='只看指定页（1-based，如 --pages 84 85）')
    ap.add_argument('--topic', default=None, help='只看某题型所在页（如 M-T-125）')
    ap.add_argument('--top', type=int, default=50, help='输出前 N 页')
    ap.add_argument('--minlines', type=int, default=40,
                    help='过滤掉行数少于该值的页（目录/过渡页，默认 40）')
    ap.add_argument('--max', type=int, default=0,
                    help='只输出破碎分 <= 该值的页（0 表示不限）')
    a = ap.parse_args()

    pages = None
    if a.topic:
        idx = os.path.join(ROOT, '原件', '题型页码索引.md')
        pat = re.compile(r'\|\s*' + re.escape(a.topic) + r'\s*\|\s*([\d–\-?]+)')
        hit = set()
        for line in open(idx, encoding='utf-8'):
            m = pat.search(line)
            if m:
                raw = m.group(1)
                for part in re.findall(r'\d+', raw):
                    hit.add(int(part))
        pages = sorted(hit)
        if not pages:
            sys.exit('索引里没找到 %s' % a.topic)
        print('  %s 所在页：%s' % (a.topic, pages))
    elif a.pages:
        pages = a.pages

    files = sorted(f for f in os.listdir(DIR) if f.endswith('.txt'))
    if pages:
        want = set('p%03d.txt' % p for p in pages)
        files = [f for f in files if f in want]

    rows = []
    for f in files:
        pno = int(f[1:4])
        txt = open(os.path.join(DIR, f), encoding='utf-8').read()
        s, nf, ns, nu, nl = score_page(txt)
        # 目录页/过渡页（行数太少）不参与：它们天然 0 分，会挤占 TOP
        if nl < a.minlines:
            continue
        # 归一化：按行平均，避免长页天然分数高
        norm_s = s * 100.0 / max(nl, 1)
        rows.append((norm_s, s, pno, nf, ns, nu, nl))

    rows.sort()
    if a.max:
        rows = [r for r in rows if r[1] <= a.max]

    def grade(v):
        if v <= 15:
            return 'A'      # 干净，直接录
        if v <= 40:
            return 'B'      # 可录，个别处需人工补
        if v <= 80:
            return 'C'      # 有伤，谨慎
        return 'D'          # 破碎严重，跳过

    print('=' * 70)
    print('  还原版完整度扫描   %d 页（已过滤行数<%d 的目录/过渡页）'
          % (len(rows), a.minlines))
    print('  norm = 破碎分×100/行数（消除页长差异）；评级越低越干净')
    print('=' * 70)
    print('  %-8s %-4s %-6s %-7s %-7s %-6s %s'
          % ('页', '级', 'norm', 'frac', '上下标', '⟨?⟩', '行数'))
    print('  ' + '-' * 64)
    for nrm, s, pno, nf, ns, nu, nl in rows[:a.top]:
        print('  p%-7d %-5s %-7.1f %-8d %-8d %-7d %d'
              % (pno, grade(nrm), nrm, nf, ns, nu, nl))

    g = [grade(r[0]) for r in rows]
    print('  ' + '-' * 64)
    print('  A级(直接录) %d 页    B级(可录) %d 页    C级 %d 页    D级(跳过) %d 页'
          % (g.count('A'), g.count('B'), g.count('C'), g.count('D')))
    return 0


if __name__ == '__main__':
    sys.exit(main())
