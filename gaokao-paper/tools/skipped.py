# -*- coding: utf-8 -*-
r"""跳过题目清单管理（tools/skipped.py）

用途
----
录入过程中会跳过一部分题目：提取破碎、答案存疑、印刷错误、与已录题重复等。
这些题**必须留痕**，等全部录入完成后由人工统一核对原 PDF 裁定。

数据存 `data/skipped.json`，结构：

    {
      "updated": "...",
      "reason_desc": {原因类别: 说明},
      "items": [
        {"key": "M-T-073-E1", "page": 48, "topic": "M-T-073",
         "topic_name": "...", "kp1": "...", "kp2": "...",
         "kind": "典例", "ref_answer": "...",
         "reason": "提取破碎", "note": "...",
         "stem_raw": "...", "has_solution": true}
      ]
    }

用法
----
    python3 tools/skipped.py scan     重新扫描已处理题型内的未录题，合并进清单
    python3 tools/skipped.py add KEY --reason 类别 --note "说明"
    python3 tools/skipped.py show     打印汇总
    python3 tools/skipped.py pending  只列需要人工裁定的（排除"重复"）

设计要点
--------
1. **只扫已处理过的题型**。按"已录题型"过滤，避免把尚未推进的后续
   模块（如不等式选讲）误判成跳过。判断依据是 src 字段能提取出
   合法的 ref_bank key。

2. **已有条目不覆盖**。scan 时若 key 已存在，保留原 reason/note
   （人工填写的分类是宝贵信息，不能被自动扫描冲掉）。

3. **原因分类固定六类**，见 reason_desc。新增分类要同步更新
   reason_desc，否则 show 时显示为空说明。

4. **异步维护**：每次录入批次后跑一次 `scan`，
   新产生的跳过项会以 "待核查" 进入清单，等人工补 reason/note。
"""
import sys, os, json, io, re, collections
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'py'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
PATH = os.path.join(ROOT, 'data', 'skipped.json')

REASON_DESC = {
    '重复':     '与已录题目同题，无需补录（但可核对是否该挂双题型标签）',
    '答案存疑': '原书答案与严格推导不符，需人工裁定',
    '提取破碎': 'PDF 提取丢失关键符号，无法可靠重建原文',
    '解析截断': '解析不完整，答案无法验证',
    '印刷错误': '原书印刷问题（选项重复/符号缺失），需人工裁定',
    '待核查':   '尚未分类，需人工核对',
}


def _load():
    if os.path.exists(PATH):
        return json.load(io.open(PATH, encoding='utf-8'))
    return dict(updated='', reason_desc=REASON_DESC, items=[])


def _save(d):
    tmp = PATH + '.tmp'
    io.open(tmp, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=1))
    os.replace(tmp, PATH)


def _ref_bank():
    return json.load(io.open(os.path.join(ROOT, 'data', 'ref_bank.json'), encoding='utf-8'))


def _bank():
    return json.load(io.open(os.path.join(ROOT, 'data', 'bank.json'), encoding='utf-8'))


def _pages():
    p = os.path.join(ROOT, 'tools', '_toc_pages.json')
    return json.load(io.open(p, encoding='utf-8')) if os.path.exists(p) else {}


def recorded_keys(r):
    """从 bank 的 src 字段提取已录的 ref_bank key。

    src 格式：'2024高中数学热点题型归纳完整解析版.pdf · M-T-001-V1 · 第 1 题'
    必须是 **含 key** 的写法（M-T-001-V1），不能只写 topic（M-T-001）——
    只写 topic 会识别为 0 题，导致待录数虚高（踩过一次）。
    """
    out = set()
    for q in _bank():
        m = re.search(r'(M-T-\d+-(?:E\d|V\d+))', q.get('src') or '')
        if m and m.group(1) in r:
            out.add(m.group(1))
    return out


def scan():
    r = _ref_bank(); pg = _pages()
    import kp_catalog as K
    rec = recorded_keys(r)
    by_topic = collections.defaultdict(list)
    for k in r:
        by_topic[k.rsplit('-', 1)[0]].append(k)
    done_topics = {k.rsplit('-', 1)[0] for k in rec}

    d = _load()
    known = {it['key']: it for it in d['items']}

    added = []
    for t in sorted(done_topics):
        nd = (K.TOPICS.get(t) or {})
        pri = nd.get('primary') or ('?', '?')
        for k in sorted(by_topic[t]):
            if k in rec or k in known:
                continue
            v = r[k]
            it = dict(key=k, page=pg.get(t), topic=t, topic_name=nd.get('name', ''),
                      kp1=pri[0], kp2=pri[1], kind=v.get('kind', ''),
                      ref_answer=(v.get('ans') or '').strip(),
                      reason='待核查', note='需人工核对原 PDF 后决定是否补录',
                      stem_raw=re.sub(r'\s+', ' ', (v.get('stem') or ''))[:200],
                      has_solution=bool((v.get('solution') or '').strip()))
            known[k] = it
            added.append(k)

    d['items'] = [known[k] for k in sorted(known)]
    d['reason_desc'] = REASON_DESC
    _save(d)
    print('  跳过清单：共 %d 条，新增 %d 条 %s' % (len(d['items']), len(added), added))
    return d


def show(only=None):
    d = _load()
    items = [i for i in d['items'] if not only or i['reason'] in only]
    c = collections.Counter(i['reason'] for i in d['items'])
    print('  跳过清单共 %d 条' % len(d['items']))
    for k, n in c.most_common():
        print('    %-6s %d' % (k, n))
    print()
    for i in items:
        print('  %-14s p%-4s [%-4s] %s' % (i['key'], i.get('page'), i['reason'], i['topic_name'][:22]))
        print('      原书答案: %s' % (i.get('ref_answer') or '(无)')[:56])
        print('      原因: %s' % i.get('note', '')[:80])
    return d


def add(key, reason, note):
    d = _load()
    if reason not in REASON_DESC:
        print('  ✗ 未知原因类别 %r，可用：%s' % (reason, ' / '.join(REASON_DESC)))
        return
    for it in d['items']:
        if it['key'] == key:
            it['reason'] = reason; it['note'] = note
            _save(d); print('  已更新 %s' % key); return
    r = _ref_bank(); pg = _pages()
    import kp_catalog as K
    t = key.rsplit('-', 1)[0]
    nd = (K.TOPICS.get(t) or {}); pri = nd.get('primary') or ('?', '?')
    v = r.get(key, {})
    d['items'].append(dict(key=key, page=pg.get(t), topic=t, topic_name=nd.get('name', ''),
                           kp1=pri[0], kp2=pri[1], kind=v.get('kind', ''),
                           ref_answer=(v.get('ans') or '').strip(), reason=reason, note=note,
                           stem_raw=re.sub(r'\s+', ' ', (v.get('stem') or ''))[:200],
                           has_solution=bool((v.get('solution') or '').strip())))
    d['items'].sort(key=lambda x: x['key'])
    _save(d); print('  已新增 %s' % key)


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a or a[0] == 'show':
        show()
    elif a[0] == 'scan':
        scan()
    elif a[0] == 'pending':
        show(only={'答案存疑', '提取破碎', '解析截断', '印刷错误', '待核查'})
    elif a[0] == 'add':
        # add KEY "原因" "说明"
        add(a[1], a[2], a[3] if len(a) > 3 else '')
    else:
        print(__doc__)
