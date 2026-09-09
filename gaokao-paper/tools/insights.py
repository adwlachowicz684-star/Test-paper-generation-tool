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


def kind_of(key):
    """M-T-374-V2 -> '变式 V2'；M-T-374-E1 -> '例题 E1'"""
    m = re.search(r'-E(\d+)$', key)
    if m:
        return '例题 E%s' % m.group(1)
    m = re.search(r'-V(\d+)$', key)
    if m:
        return '变式 V%s' % m.group(1)
    return '其他'


def topic_title(tid):
    """带归属的题型标题：M-T-374 · 双曲线特性2：内心（解析几何 › 离心率）"""
    try:
        sys.path.insert(0, os.path.join(ROOT, 'py'))
        import kp_catalog as K
        info = K.TOPICS.get(tid, {})
        name = info.get('name') or '?'
        prim = info.get('primary') or ()
        where = ' › '.join(prim) if prim else ''
        return '%s · %s' % (tid, name), where
    except Exception:      # noqa: BLE001
        return tid, ''


def by_topic(rows, a):
    """按题型分组输出，结构与 51-insights.md 一致"""
    groups = {}
    for r in rows:
        groups.setdefault(r['topic'], []).append(r)
    total = 0
    for tid in sorted(groups):
        title, where = topic_title(tid)
        print('\n' + '=' * 70)
        print('%s%s' % (title, '（%s）' % where if where else ''))
        print('=' * 70)
        if a.md:
            print('| 例题/变式 | 结论 |')
            print('|---|---|')
        for r in sorted(groups[tid], key=lambda x: x['key']):
            total += 1
            body = clean(r['text'])
            title2, rest = split_title(body)
            if a.md:
                print('| %s | %s |' % (kind_of(r['key']), rest or body))
            else:
                print('  [%s] %s' % (kind_of(r['key']), body[:210]))
    print('\n共 %d 条结论 / %d 个题型' % (total, len(groups)))
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--kp', default=None)
    ap.add_argument('--topic', default=None)
    ap.add_argument('--by-topic', action='store_true',
                    help='按题型分组（对齐 51-insights.md 的结构）')
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
        # 文档结构：#### M-T-xxx · 名称 / 表格首列「例题 E1」「变式 V1」
        # 于是「小节标题的题型 ID」+「首列的 E/V 编号」= 完整题号
        covered = set()
        cur_tid = None
        for line in doc.split('\n'):
            m = re.match(r'^####\s+(M-T-\d+)', line)
            if m:
                cur_tid = m.group(1)
                continue
            if cur_tid:
                m2 = re.search(r'\|\s*\*{0,2}(?:例题|变式)\s*([EV]\d+)', line)
                if m2:
                    covered.add('%s-%s' % (cur_tid, m2.group(1)))
        miss = [r for r in rows if r['key'] not in covered]
        print('题库中结论 %d 条，51-insights.md 已覆盖 %d 条'
              % (len(rows), len(rows) - len(miss)))
        if miss:
            print('\n未收录 %d 条：' % len(miss))
            for r in miss:
                print('  [%s] %s' % (r['key'], clean(r['text'])[:90]))
            print('\n提示：在对应题型的 #### 小节表格里加一行「| 例题 E1 | …」或「| 变式 V1 | …」')
        return 0

    if not rows:
        print('没有匹配的结论。')
        return 0

    if a.by_topic:
        return by_topic(rows, a)

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
