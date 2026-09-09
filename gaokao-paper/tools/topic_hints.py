# -*- coding: utf-8 -*-
"""按知识点（题型）生成 AI 提示：通法 + 陷阱。

用途
────
录题、讲题、出卷时，AI（或人）需要快速知道：

    这个题型「怎么想」   → 通法/价值结论（来自 review 里的 ⭐）
    这个题型「哪里会错」 → 陷阱（来自 review 里的 ⚠ / 易错 / 陷阱）

本脚本把散落在 519 道题 review 里的这两类信息，
按**题型 → 知识点**聚合，输出成结构化数据，供 AI 直接读取。

产出
────
1. `data/topic_hints.json`   机器读（AI 提示的数据源）
2. `skill/references/52-traps.md`  人读（按知识点组织的陷阱速查）

用法
────
    python3 tools/topic_hints.py            # 生成两份产出
    python3 tools/topic_hints.py --show M-T-234   # 看单个题型的提示
    python3 tools/topic_hints.py --stat     # 只看统计

设计说明
────────
**为什么从 review 里抽，而不是手写一份？**
手写会与题库脱节 —— 新录的题有了新陷阱，文档不会自动跟上。
从 review 抽，则每录一批重跑一次即可同步，`--check` 还能查遗漏。

**判据**
- 通法：含 `⭐`（一条 review 可能有多行 ⭐，全部收集）
- 陷阱：含 `⚠`、`陷阱`、`易错`、`别搞`、`注意：`
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
BANK = os.path.join(ROOT, 'data', 'bank.json')
OUT_JSON = os.path.join(ROOT, 'data', 'topic_hints.json')
OUT_MD = os.path.join(ROOT, 'skill', 'references', '52-traps.md')

TRAP_PAT = re.compile(r'⚠|陷阱|易错|别搞|注意[：:]')
STAR = '⭐'


def _load_bank():
    with open(BANK, encoding='utf-8') as f:
        b = json.load(f)
    return b['questions'] if isinstance(b, dict) else b


def _topic_path(tid):
    """题型 ID → (一级知识点, 二级知识点)。查不到给 ('未分类','')。"""
    try:
        sys.path.insert(0, os.path.join(ROOT, 'py'))
        import kp_catalog as K
        t = K.TOPICS.get(tid)
        if t:
            pri = t.get('primary') or ('未分类', '')
            return pri[0], (pri[1] if len(pri) > 1 else '')
    except Exception:
        pass
    return '未分类', ''


def _clean(line):
    """去掉行首的 ⭐ / - / 数字序号和多余空白。"""
    s = line.strip()
    s = re.sub(r'^[⭐\s\-•*]+', '', s)
    s = re.sub(r'^\d+[.、)]\s*', '', s)
    return s.strip()


def _merge_blocks(rv):
    """把「标题独占一行、内容在后面」的写法合并成一行。

    典型：`**⭐ 通法（xxx）**：` 单独一行，正文在下一行。
    若逐行处理，抽出来就是个空壳标题（这在 insights.py 里已经踩过一次）。
    做法：以 ⭐ / ⚠ 开头的行开启一个块，持续吸收后续非空行，
    直到遇到下一个标记行或空行。
    """
    lines = rv.split('\n')
    merged, buf = [], None
    for raw in lines:
        line = raw.strip()
        if not line:
            if buf is not None:
                merged.append(buf)
                buf = None
            continue
        is_head = line.startswith('**' + STAR) or STAR in line[:6] \
            or TRAP_PAT.match(line) or line.startswith('**⚠')
        if is_head:
            if buf is not None:
                merged.append(buf)
            buf = line
        elif buf is not None:
            buf = buf + ' ' + line
            if len(buf) > 400:      # 防止整段被吸进来
                merged.append(buf)
                buf = None
        else:
            merged.append(line)
    if buf is not None:
        merged.append(buf)
    return merged


def collect():
    """返回 {tid: {'name':..,'kp':..,'kp2':..,'methods':[(qid,text)],
                   'traps':[(qid,text)]}}"""
    out = {}
    for q in _load_bank():
        rv = q.get('review') or ''
        if not rv.strip():
            continue
        for tid in (q.get('topics') or []):
            d = out.setdefault(tid, {'name': tid, 'methods': [], 'traps': []})
            qid = q.get('id', '?')
            # 逐块判：⭐ 归通法；陷阱词归陷阱（一块可能两者都有，取更贴的）
            for line in _merge_blocks(rv):
                if not line:
                    continue
                if STAR in line:
                    txt = _clean(line)
                    if len(txt) >= 12:
                        d['methods'].append((qid, txt))
                elif TRAP_PAT.search(line):
                    txt = _clean(line)
                    if len(txt) >= 12:
                        d['traps'].append((qid, txt))
    for tid, d in out.items():
        kp, kp2 = _topic_path(tid)
        d['kp'], d['kp2'] = kp, kp2
    return out


def _dedup(items):
    """同一题号的多条相近文本去重（保留最长的一条）。"""
    seen = {}
    for qid, txt in items:
        key = txt[:24]
        if key not in seen or len(txt) > len(seen[key][1]):
            seen[key] = (qid, txt)
    return list(seen.values())


def build_json(data):
    res = {}
    for tid, d in sorted(data.items()):
        res[tid] = {
            'kp': d['kp'],
            'kp2': d['kp2'],
            'methods': [{'q': q, 't': t} for q, t in _dedup(d['methods'])],
            'traps': [{'q': q, 't': t} for q, t in _dedup(d['traps'])],
        }
    with open(OUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(res, f, ensure_ascii=False, indent=1)
    return res


def build_md(data):
    """按一级知识点 → 二级 → 题型，输出陷阱速查。"""
    tree = {}
    for tid, d in data.items():
        traps = _dedup(d['traps'])
        if not traps:
            continue
        tree.setdefault(d['kp'], {}).setdefault(d['kp2'] or '', []).append(
            (tid, d['name'], traps))

    L = ['# 陷阱速查（按知识点组织）', '',
         '> 由 `tools/topic_hints.py` 从题库 review 自动生成，请勿手工编辑。',
         '> 与 `51-insights.md`（通法速查）配套：**这本讲「哪里会错」。**', '']

    for kp in sorted(tree):
        L.append('## %s' % kp)
        L.append('')
        for kp2 in sorted(tree[kp]):
            if kp2:
                L.append('### %s' % kp2)
                L.append('')
            for tid, name, traps in sorted(tree[kp][kp2]):
                try:
                    sys.path.insert(0, os.path.join(ROOT, 'py'))
                    import kp_catalog as K
                    nm = K.TOPICS.get(tid, {}).get('name', name)
                except Exception:
                    nm = name
                L.append('**%s · %s**' % (tid, nm))
                L.append('')
                for qid, txt in traps:
                    L.append('- `%s` %s' % (qid, txt))
                L.append('')
    with open(OUT_MD, 'w', encoding='utf-8') as f:
        f.write('\n'.join(L))
    return len(L)


def main():
    a = sys.argv[1:]
    data = collect()
    if '--show' in a:
        i = a.index('--show')
        tid = a[i + 1]
        d = data.get(tid)
        if not d:
            print('无此题型：%s' % tid)
            return 1
        print('%s  [%s › %s]' % (tid, d['kp'], d['kp2']))
        print(' 通法 %d 条、陷阱 %d 条' % (len(d['methods']), len(d['traps'])))
        for q, t in _dedup(d['methods'])[:8]:
            print('  ⭐ [%s] %s' % (q, t[:90]))
        for q, t in _dedup(d['traps'])[:8]:
            print('  ⚠ [%s] %s' % (q, t[:90]))
        return 0
    if '--stat' in a:
        print('题型 %d 个；通法 %d 条；陷阱 %d 条' % (
            len(data),
            sum(len(_dedup(d['methods'])) for d in data.values()),
            sum(len(_dedup(d['traps'])) for d in data.values())))
        return 0
    res = build_json(data)
    n = build_md(data)
    print('已生成 %s（%d 个题型）' % (os.path.relpath(OUT_JSON, ROOT), len(res)))
    print('已生成 %s（%d 行）' % (os.path.relpath(OUT_MD, ROOT), n))
    print('题型 %d 个；通法 %d 条；陷阱 %d 条' % (
        len(data),
        sum(len(v['methods']) for v in res.values()),
        sum(len(v['traps']) for v in res.values())))
    return 0


if __name__ == '__main__':
    sys.exit(main())
