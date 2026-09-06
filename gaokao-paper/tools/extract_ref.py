# -*- coding: utf-8 -*-
"""从教辅 PDF 提取【典例分析】【变式演练】题目 -> data/ref_bank.json

用法：
    python3 tools/extract_ref.py [PDF路径]

为什么固化为独立工具：
  提取逻辑最初是内联脚本（跑一次就丢），导致修 bug 后无法复现、
  也无法验证"这次改了什么"。固化后可以反复重跑并对比结果。

产出：
    data/ref_bank.json   qid -> 题目正文
    data/_tref.json      题型ID -> {examples, variants}

关键规则见 README「教辅例题提取」章节。
"""
import os
import re
import sys
import json

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'py'))
import kp_catalog as K                                    # noqa: E402

DEFAULT_PDF = '/data/inputs/2024高中数学热点题型归纳完整解析版.pdf'
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_REF = os.path.join(ROOT, 'data', 'ref_bank.json')
OUT_TREF = os.path.join(ROOT, 'data', '_tref.json')

SECT = re.compile(r'【(典例分析|变式演练|提分秘籍|点睛)】\s*')
QNUM = re.compile(r'^(?:例\s*)?(\d{1,3})\s*[.．](?=\s)', re.M)
ANS = re.compile(r'【答案】')
OPT = re.compile(r'^\s*([A-D])\s*[.．、]\s*', re.M)


def norm(s):
    s = re.sub(r'^\s*【题型[一二三四五六七八九十百零\d]+】\s*', '', s or '')
    return re.sub(r'[：:\s]+$', '', s).strip()


def clean(s):
    s = re.sub(r'[\ue000-\uf8ff]', '', s)          # 私有区乱码（公式碎片）
    s = re.sub(r'\n?·\s*\d+\s*·\n?', '\n', s)      # 页码 ·6·
    s = re.sub(r'第\s*\d+\s*页\s*共\s*\d+\s*页', '', s)
    return re.sub(r'\n{3,}', '\n\n', s).strip()


def marker(title):
    """容忍换行的题型标题正则"""
    m = re.match(r'^(【题型[一二三四五六七八九十百零\d]+】)\s*(.*)$', title.strip())
    if not m:
        return None
    core = m.group(2).strip()
    if not core:
        return None
    return re.compile(re.escape(m.group(1)) + r'\s*'
                      + r'\s*'.join(re.escape(c) for c in core))


def sections(text):
    ms = list(SECT.finditer(text))
    out = []
    for i, m in enumerate(ms):
        s = m.end()
        e = ms[i + 1].start() if i + 1 < len(ms) else len(text)
        out.append((m.group(1), text[s:e]))
    return out


def split_questions(block):
    """切题 + 用【答案】反证题号（剔除详解碎片）"""
    idx = [(m.start(), m.end(), int(m.group(1))) for m in QNUM.finditer(block)]
    idx = [(a, b, n) for a, b, n in idx if a == 0 or block[a - 1] == '\n']
    if not idx:
        return []
    while True:
        drop = -1
        for i, (a, b, n) in enumerate(idx):
            e = idx[i + 1][0] if i + 1 < len(idx) else len(block)
            if not ANS.search(block, a, e):
                drop = i
                break
        if drop < 0:
            break
        idx.pop(drop)
        if not idx:
            return []
    return [(n, block[b:(idx[i + 1][0] if i + 1 < len(idx) else len(block))])
            for i, (a, b, n) in enumerate(idx)]


def split_stem_opts(head):
    """拆题干与选项。

    修复的关键点：**选项内容必须跨行累积**。

    早期版本按行扫描，遇到 `A. xxx` 就把这一行当整个选项。
    但教辅里选项常含分数，PDF 中分子分母是上下两行：

        A. (0, 2) ∪ (9
                    2        <- 分母在下一行
        B. (7 ...

    按行扫描会把 `9` 收进 A，剩下的 `2` 以及后续所有内容
    **被当成题干**，而 B/C/D 的内容又跑到下一行没有字母标记 -> 选项变空。

    正确做法：找到所有行首的字母标记，
    每个选项的内容 = 该标记之后到「下一个标记」或「【答案】」之间的全部文本。
    """
    marks = [(m.start(), m.end(), m.group(1)) for m in OPT.finditer(head)]
    marks = [(a, b, L) for a, b, L in marks if a == 0 or head[a - 1] == '\n']
    if not marks:
        return head.strip(), []

    stem = head[:marks[0][0]].strip()
    opts = []
    for i, (a, b, L) in enumerate(marks):
        e = marks[i + 1][0] if i + 1 < len(marks) else len(head)
        body = clean(head[b:e])
        if body:                       # 跳过空选项（PDF 分页造成的碎片）
            opts.append((L, body))
    return stem, opts


def grab(rest, pat):
    m = re.search(pat, rest)
    if not m:
        return ''
    s = m.end()
    nx = re.search(r'【[^】]{1,6}】', rest[s:])
    return clean(rest[s:s + (nx.start() if nx else len(rest[s:]))])


def fields(body):
    m = re.search(r'【(答案|分析|详解)】', body)
    head = body[:m.start()] if m else body
    rest = body[m.start():] if m else ''
    stem, opts = split_stem_opts(head)
    # 题干尾部的孤立 ( ) 是选择题作答位，规范化为全角
    stem = re.sub(r'\n\s*\(\s*\)\s*$', '（　　）', stem).strip()
    return {
        'stem': stem,
        'opts': [t for _, t in opts],
        'opt_letters': [L for L, _ in opts],
        'ans': grab(rest, r'【答案】'),
        'analysis': grab(rest, r'【分析】'),
        'solution': grab(rest, r'【详解】'),
    }


def main(pdf=DEFAULT_PDF):
    import pymupdf
    d = pymupdf.open(pdf)
    toc = d.get_toc()
    FULL = '\n'.join(d[i].get_text() for i in range(d.page_count))

    # 定位每个题型的内容起点（书签页码指向目录页，不能用）
    pos = []
    for lv, t, pg in toc:
        if lv != 2:
            continue
        p = marker(t)
        if not p:
            continue
        floor = pos[-1][0] + 1 if pos else 0
        for m in p.finditer(FULL, floor):
            if '【典例分析】' in FULL[m.end():m.end() + 2000] \
               or '【答案】' in FULL[m.end():m.end() + 2000]:
                pos.append((m.start(), t))
                break
    print('  定位题型内容起点: %d / %d'
          % (len(pos), sum(1 for lv, _, _ in toc if lv == 2)))

    ref, tref = {}, {}
    for i, (st, title) in enumerate(pos):
        en = pos[i + 1][0] if i + 1 < len(pos) else len(FULL)
        text = clean(FULL[st:en])
        nm = norm(title)
        tid = None
        for l1, subs in K.CATALOG['数学']:
            for l2, tops in subs.items():
                if l2 == K.XSECTION:
                    continue
                for t in tops:
                    if norm(t) == nm:
                        tid = K.topic_id('数学', l1, l2, t)
                        break
                if tid:
                    break
            if tid:
                break
        if not tid:
            continue
        slot = tref.setdefault(tid, {'examples': [], 'variants': []})
        for kind, blk in sections(text):
            if kind not in ('典例分析', '变式演练'):
                continue
            tag = {'典例分析': 'E', '变式演练': 'V'}[kind]
            key = 'examples' if tag == 'E' else 'variants'
            for i2, (onum, body) in enumerate(split_questions(blk), 1):
                f = fields(body)
                if len(f['stem']) < 10:
                    continue
                qid = '%s-%s%d' % (tid, tag, i2)
                f.update({'id': qid, 'topic': tid,
                          'kind': '典例' if tag == 'E' else '变式',
                          'num': i2, 'orig_num': onum, 'subject': '数学',
                          'type': '例题',
                          'src': os.path.basename(pdf)})
                ref[qid] = f
                slot[key].append(qid)

    na = sum(1 for v in ref.values() if v['ans'])
    ns = sum(1 for v in ref.values() if v['solution'])
    ne = sum(1 for v in ref.values() if v['kind'] == '典例')
    # 选项质量
    withopt = [v for v in ref.values() if v.get('opts')]
    good = sum(1 for v in withopt if len(v['opts']) == 4)
    emptyopt = sum(1 for v in withopt if any(not o.strip() for o in v['opts']))
    print('  题目 %d（典例 %d / 变式 %d）' % (len(ref), ne, len(ref) - ne))
    print('  带答案 %d (%.0f%%)  带详解 %d (%.0f%%)'
          % (na, na * 100 / max(len(ref), 1), ns, ns * 100 / max(len(ref), 1)))
    print('  有选项 %d，其中四项齐全 %d，含空选项 %d'
          % (len(withopt), good, emptyopt))
    json.dump(ref, open(OUT_REF, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    json.dump(tref, open(OUT_TREF, 'w', encoding='utf-8'), ensure_ascii=False)
    print('  已写入 %s' % OUT_REF)
    return ref, tref


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_PDF)
