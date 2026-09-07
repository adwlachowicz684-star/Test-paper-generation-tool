#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""并行录入的合并入口：把多个窗口产出的 input_batch*.py 一次入库。

    python3 tools/merge_batches.py input_batch15a input_batch15b
    python3 tools/merge_batches.py --all              # 自动扫描所有未入库的
    python3 tools/merge_batches.py --all --batch 18   # 指定批次名
    python3 tools/merge_batches.py --all --dry-run    # 只看会入什么

## 为什么必须有这个工具

`hand_input.add()` 是 **读-改-写**：每次调用都 `load()` 整个 bank、
追加、再 `save()`。两个窗口同时跑，后写的会**整份覆盖**先写的——
先录的那几道题直接消失。

而且 `next_id()` 靠遍历 bank 取最大序号，两个窗口会拿到**同一个 ID**。

本工具把「读一次 → 全部追加 → 写一次」集中到一处，
多个窗口的产物在这里汇合，**ID 由同一次分配，必然不冲突**。

## 各窗口的分工

| 阶段 | 谁做 | 碰 bank.json 吗 |
|---|---|---|
| 认领题型段 | `claim.py` | 否 |
| 写 `input_batchXX.py` | 各窗口独立 | **否**（只写 tools/ 下的 .py） |
| 合并入库 | **本工具** | 是，**唯一入口** |
| 验证导出 | `run_batch.py` | 只读 |

**关键纪律：录题窗口绝不执行入库命令。**
只产出 `tools/input_batchXX.py`（纯 Python 数据文件），
由合并窗口统一入库。
"""
import sys
import os
import re
import json
import shutil
import importlib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, 'py'))
sys.path.insert(0, HERE)

import hand_input              # noqa: E402
import kp_catalog as K         # noqa: E402

SLICE = os.path.join(ROOT, 'src', 'slices', '数学')
STATE = os.path.join(HERE, '_merged.json')


def list_inputs():
    """扫描 tools/ 下所有 input_batch*.py，返回模块名列表。"""
    out = []
    for fn in sorted(os.listdir(HERE)):
        m = re.match(r'^(input_batch[\w]*)\.py$', fn)
        if m:
            out.append(m.group(1))
    return out


def load_merged():
    if os.path.exists(STATE):
        try:
            return json.load(open(STATE, encoding='utf-8'))
        except Exception:       # noqa: BLE001
            pass
    return {}


def save_merged(d):
    json.dump(d, open(STATE, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)


def norm(t):
    """题干签名：去公式、去非字母数字汉字，用于判断是否已入库。"""
    t = re.sub(r'\$[^$]*\$', '#', t or '')
    return re.sub(r'[^一-鿿0-9a-zA-Z]', '', t)[:60]


def apply_skips(dry=False):
    r"""把各窗口 _claims/*_skip.json 里的跳过标记并入 data/skipped.json。

    各窗口写自己的独立文件，这里统一汇总——
    **这是 skipped.json 的唯一写者**，避免多窗口互相覆盖。
    """
    sys.path.insert(0, os.path.join(HERE))
    try:
        import claim as C
    except Exception:      # noqa: BLE001
        return 0
    pend = C.collect_skips()
    if not pend:
        return 0
    sp = os.path.join(ROOT, 'data', 'skipped.json')
    d = json.load(open(sp, encoding='utf-8'))
    have = {x['key'] for x in d['items']}
    legal = set(d.get('reason_desc') or {})
    n = 0
    for who, items in sorted(pend.items()):
        for x in items:
            if x['key'] in have:
                continue
            rsn = x.get('reason') or '待核查'
            if rsn not in legal:
                rsn = '待核查'
            d['items'].append({
                'key': x['key'], 'page': 0, 'topic': x['key'].rsplit('-', 1)[0],
                'topic_name': '', 'kp1': '', 'kp2': '', 'kind': '',
                'ref_answer': '', 'reason': rsn, 'note': x.get('by', ''),
            })
            have.add(x['key'])
            n += 1
            print('  + 跳过 %s（%s，来自 %s）' % (x['key'], rsn, who))
    if n and not dry:
        json.dump(d, open(sp, 'w', encoding='utf-8'),
                  ensure_ascii=False, indent=1)
        # 合并后清空各窗口的独立文件
        for who in pend:
            fp = os.path.join(C.CLAIM_DIR, C._safe(who) + '_skip.json')
            if os.path.exists(fp):
                os.remove(fp)
    return n


def build_items(qs):
    """把 input 模块的 QS 转成 hand_input 能吃的 item 列表。

    兼容两种历史格式：
      新：`topics`(list) / `src` / `analysis` / `difficulty`
      老：`topic`(str) / `kind` —— 第 2~7 批的骨架是这种
    """
    items = []
    for d in qs:
        if d.get('topics'):
            topic = d['topics'][0]
            topics = list(d['topics'])
        else:
            topic = d.get('topic') or ''
            topics = [topic] if topic else []
        pri = (K.TOPICS.get(topic) or {}).get('primary') or ('数学', '未分类')
        it = {
            'subject': '数学',
            'type': d['type'],
            'stem_text': d['stem_text'],
            'opts': [list(o) for o in d.get('opts', [])],
            'answer': d['answer'],
            'solution': d.get('solution') or '',
            'analysis': d.get('analysis') or '',
            'kp': pri[0],
            'kp2': pri[1],
            'topics': topics,
            'src': d.get('src') or '',
            'review': d.get('review') or '',
            'difficulty': d.get('difficulty', 0.65),
        }
        if d.get('figs'):
            it['figs'] = [dict(f) for f in d['figs']]
        items.append(it)
    return items


def fix_figs(bank, ids):
    """把 _tmp 开头的临时图名改成实际 ID 名，并同步 bank。"""
    n = 0
    for q in bank:
        if q.get('id') not in ids:
            continue
        figs = q.get('figs') or []
        if not figs:
            continue
        new = []
        for gi, fg in enumerate(figs, 1):
            old = fg.get('file') or ''
            if not old.startswith('_tmp'):
                new.append(fg)
                continue
            newf = '%s_fig%d.png' % (q['id'], gi)
            src, dst = os.path.join(SLICE, old), os.path.join(SLICE, newf)
            if os.path.exists(src):
                shutil.move(src, dst)
                n += 1
            else:
                print('  ! 找不到切好的图：%s' % old)
            fg['file'] = newf
            new.append(fg)
        q['figs'] = new
    return n


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('-')]
    flags = [a for a in sys.argv[1:] if a.startswith('-')]
    dry = '--dry-run' in flags
    # 批次名：默认「合并」，但验收(run_batch)靠 batch 字段定位本批题目，
    # 并行录入时必须能指定成「第18批」之类，否则 run_batch 找不到题。
    bn = '教辅录入-合并'
    if '--batch' in sys.argv:
        i = sys.argv.index('--batch')
        if i + 1 < len(sys.argv):
            v = sys.argv[i + 1]
            bn = v if v.startswith('教辅录入') else '教辅录入-第%s批' % v

    if '--apply-skip' in flags:
        n = apply_skips(dry='--dry-run' in flags)
        print('\n  跳过标记合并完成：%d 条' % n if n else '\n  没有待合并的跳过标记')
        return 0

    if '--all' in flags:
        mods = list_inputs()
    elif args:
        mods = args
    else:
        print(__doc__)
        print('当前可合并的 input 模块：')
        for m in list_inputs():
            print('  %s' % m)
        return 1

    if not mods:
        print('  没有找到 input_batch*.py')
        return 1

    merged = load_merged()
    # 已入库的题号：从 bank 的 src 抽 M-T-xxx-En/Vn
    # **这道检查不能省**——历史 input_batch*.py 全都还在 tools/ 下，
    # 而它们的题早已入库。只看 _merged.json 的话（首次运行为空），
    # 一次 --all 就会把 208 题重复录一遍。
    bank = hand_input.load()
    have = set()          # 题号（新格式能抽到）
    stems = set()         # 题干签名（老格式没有题号，靠这个兜底）
    for q in bank:
        m = re.search(r'(M-T-\d+-(?:E\d+|V\d+))', q.get('src') or '')
        if m:
            have.add(m.group(1))
        s = norm(q.get('stem_text'))
        if s:
            stems.add(s)

    todo = []
    print('扫描 %d 个 input 模块：' % len(mods))
    for m in mods:
        try:
            mod = importlib.import_module(m)
        except Exception as e:      # noqa: BLE001
            print('  ✗ %s 导入失败：%s' % (m, e))
            continue
        qs = getattr(mod, 'QS', None)
        if not qs:
            print('  - %-22s 无 QS' % m)
            continue
        sig = '%d:%s' % (len(qs), (qs[0].get('src') or '')[:40])
        # 逐题过滤：已入库的跳过；空骨架（没填内容）单独标记
        fresh, dupn, empt = [], 0, 0
        for d in qs:
            if not (d.get('stem_text') or '').strip():
                empt += 1
                continue
            mm = re.search(r'(M-T-\d+-(?:E\d+|V\d+))', d.get('src') or '')
            # 双轨判重：先按题号（精确），再按题干签名（老格式没题号）
            if (mm and mm.group(1) in have) or norm(d['stem_text']) in stems:
                dupn += 1
            else:
                fresh.append(d)
        if empt:
            print('  ○ %-22s %2d 题  空骨架待填' % (m, empt))
        if not fresh:
            if dupn:
                print('  - %-22s       （%d 题已入库，跳过）' % (m, dupn))
            if merged.get(m) != sig:
                merged[m] = sig
            continue
        print('  + %-22s %2d 题  待入库%s'
              % (m, len(fresh),
                 '（另 %d 题已入库，跳过）' % dupn if dupn else ''))
        todo.append((m, fresh, sig))
    save_merged(merged)

    if not todo:
        print('\n没有待入库的内容。')
        return 0

    total = sum(len(qs) for _, qs, _ in todo)
    print('\n合计 %d 题待入库' % total)
    if dry:
        print('（--dry-run，未实际入库）')
        return 0

    # ── 核心：一次 load、全部追加、一次 save ──────────────
    # bank 在扫描阶段已 load 过，这里复用，保证 ID 分配基于最新状态
    all_items, owner = [], {}
    for m, qs, _ in todo:
        items = build_items(qs)
        for it in items:
            owner[id(it)] = m
        all_items.extend(items)

    ok, res = hand_input.add_many(all_items, batch=bn)
    if not ok:
        print('  校验未通过，整批拒绝：')
        for e in res:
            print('    -', e)
        return 1

    print('  入库成功 %d 题，ID: %s ~ %s' % (len(res), res[0], res[-1]))

    # ⚠ 必须重新 load：add_many 内部自己 load+save 过，
    # 这里那个 bank 是扫描阶段的旧快照，不含刚入的题。
    # 直接 save(bank) 会把新题整份覆盖掉（实测把 bank.json 写坏了）。
    bank = hand_input.load()
    nf = fix_figs(bank, set(res))
    if nf:
        hand_input.save(bank)
        print('  图题改名 %d 张 -> 实际 ID' % nf)

    for m, qs, sig in todo:
        merged[m] = sig
    save_merged(merged)
    print('  已记录合并状态 -> %s' % os.path.basename(STATE))
    print('\n下一步：python3 tools/run_batch.py <批次号> --no-commit')
    return 0


if __name__ == '__main__':
    sys.exit(main())
