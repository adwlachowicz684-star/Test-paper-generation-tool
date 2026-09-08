# -*- coding: utf-8 -*-
r"""insights.py —— 从题库 review 中抽取「结论/通法/易错点」

## 为什么需要

录入时每题的 review 里都会写 `⭐` 开头的心得（通法、易错点、巧妙构造）。
这些散落在 400+ 道题里，时间一长就找不到了。

本脚本把它们**一次性抽出来**，用于：
1. 检查有没有漏收进 `skill/references/51-insights.md`
2. 新增结论时生成可粘贴的 Markdown 片段

## 用法

    python3 tools/insights.py                    # 全量，按知识点分组
    python3 tools/insights.py --kp 解析几何        # 只看某知识点
    python3 tools/insights.py --kp 计数原理 --md   # 输出可粘贴的 Markdown
    python3 tools/insights.py --topic M-T-374      # 只看某题型
    python3 tools/insights.py --check              # 与 51-insights.md 对账

## 约定

review 里以 `⭐` 开头的段落即视为结论。`⭐` 之后的第一个冒号前是**标题**。
"""

import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DOC = os.path.join(ROOT, 'skill', 'references', '51-insights.md')

STAR = '\u2b50'          # ⭐


def load():
    bank = json.load(open(os.path.join(ROOT, 'data', 'bank.json'), encoding='utf-8'))
    rows = []
    for q in bank:
        rv = q.get('review') or ''
        if STAR not in rv:
            continue
        m = re.search(r'M-T-\d+-[EV]\d+', str(q.get('src', '')))
        key = m.group(0) if m else '?'
        topic = (q.get('topics') or ['?'])[0]
        kp = q.get('kp', '') or '未分类'
        # ⭐ 常写成「**⭐ 标题**：」独占一行，内容在后续几行。
        # 所以不能只取含 ⭐ 的那一行，要把后续行一并收集。
        lines = [x.strip() for x in re.split(r'\n', rv)]
        i = 0
        while i < len(lines):
            if STAR not in lines[i]:
                i += 1
                continue
            block = []
            j = i
            while j < len(lines) and j - i < 8:
                cur = lines[j]
                # 遇到下一条结论 / 新的还原说明段 → 收束
                if j > i and (STAR in cur or cur.startswith('\u2605')):
                    break
                if j > i and re.match(r'^(★|\*\*答案|答案 )', cur):
                    break
                block.append(cur)
                if sum(len(x) for x in block) > 200:
                    break
                j += 1
            p = ' '.join(block)
            p = re.sub(r'^r?"', '', p)
            p = re.sub(r'"\s*$', '', p).strip()
            if len(p) >= 25:
                rows.append({
                    'key': key, 'topic': topic, 'kp': kp, 'text': p,
                    'qid': q.get('id', ''),
                })
            i = j if j > i else i + 1
    return rows


def clean(t):
    """把 ⭐ 段落洗成可读文本（含 **⭐** 包裹、⭐：标题 等写法）"""
    t = re.sub(r'\*+\s*%s\s*\*+\s*[:：]?\s*' % STAR, '', t)   # **⭐**：
    t = re.sub(r'%s\s*[:：]?\s*' % STAR, '', t)                    # ⭐ 或 ⭐：
    t = re.sub(r'\*\s*\*', '', t)                                 # 残留的 ** **
    t = t.strip().strip('*').strip().lstrip('：:').strip()
    return t


def split_title(t):
    """⭐ 之后第一个冒号前视为标题"""
    m = re.match(r'^(.{2,28}?)[：:]', t)
    if m and len(m.group(1)) >= 2:
        return m.group(1).strip('*'), t[m.end():].strip()
    return '', t


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--kp', default=None)
    ap.add_argument('--topic', default=None)
    ap.add_argument('--md', action='store_true', help='输出可粘贴的 Markdown')
    ap.add_argument('--check', action='store_true', help='与 51-insights.md 对账')
    a = ap.parse_args()

    rows = load()
    if a.kp:
        rows = [r for r in rows if a.kp in r['kp']]
    if a.topic:
        rows = [r for r in rows if r['topic'] == a.topic]

    if a.check:
        doc = open(DOC, encoding='utf-8').read() if os.path.exists(DOC) else ''
        miss = []
        for r in rows:
            # 用题号判断是否已收
            if r['key'] not in doc:
                miss.append(r)
        print('题库中结论 %d 条，51-insights.md 已覆盖 %d 条'
              % (len(rows), len(rows) - len(miss)))
        if miss:
            print('\n未收录 %d 条：' % len(miss))
            for r in miss:
                print('  [%s] %s' % (r['key'], clean(r['text'])[:80]))
        return 0

    if not rows:
        print('没有匹配的结论。')
        return 0

    # 按知识点分组
    groups = {}
    for r in rows:
        groups.setdefault(r['kp'], []).append(r)

    total = 0
    for kp in sorted(groups):
        print('\n' + '=' * 70)
        print('【%s】 %d 条' % (kp, len(groups[kp])))
        print('=' * 70)
        for r in groups[kp]:
            total += 1
            body = clean(r['text'])
            title, rest = split_title(body)
            if a.md:
                if title:
                    print('- **%s**（`%s` · %s）：%s' % (title, r['key'], r['topic'], rest))
                else:
                    print('- `%s` · %s：%s' % (r['key'], r['topic'], body))
            else:
                print('\n[%s] %s' % (r['key'], r['topic']))
                print('   %s' % body[:230])
    print('\n' + '-' * 70)
    print('共 %d 条结论' % total)
    print('\n提示：把新结论加进 skill/references/51-insights.md 对应章节')
    return 0


if __name__ == '__main__':
    sys.exit(main())
