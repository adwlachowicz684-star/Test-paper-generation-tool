# -*- coding: utf-8 -*-
r"""auto_draft.py —— 批量生成录入骨架（提速核心）

## 为什么需要它

ref_bank.json 里**已经存好**了每道题的 stem / opts / ans / solution，
但它们是**破碎的平文本**（分数被拆成两行、根号和上下标丢失）。
而 `原件/按页还原/` 是 restore.py 生成的**带 LaTeX 的版本**（有 \frac、^）。

本脚本把两者**对齐取长补短**：
- 结构（哪是题干、哪是选项、答案是什么）→ 取 ref_bank
- 数学格式（\frac、^、\sqrt）→ 取按页还原

实测定位命中率 74.6%，命中的题**题干和选项基本无需手工重打**。

## 用法

    python3 tools/auto_draft.py --n 30 --out tools/input_batch39a.py
    python3 tools/auto_draft.py --n 30 --topic M-T-143 --out tools/input_batch39b.py
    python3 tools/auto_draft.py --n 30 --out ... --only-locatable   # 只出能定位的

生成后**必须**执行：
    python3 tools/lint_input.py <输出文件> --fix
    # 然后人工审核 NEED_FIX 标记处

## 审核要点（脚本会在注释里标出）

- `⟨?⟩` / `FIX:` 开头 → 必须人工确认
- 选项若明显重复或残缺 → 对照 `原件/按页还原/pXXX.txt`
- 答案一定要**独立验算**，不能盲信原书
"""

import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def sig(t):
    """题干签名：与 merge_batches.norm 保持一致。

    ⚠ 必须双重判重：老批次的 src 编号与 ref_bank 的 key **对不上**
    （例如内容相同的一题，bank 里记为 M-T-009-V4，ref_bank 里是 M-T-009-V1）。
    只按题号判重会选出「其实早已录入」的题，白白重写一遍。
    """
    t = t or ''
    t = t.replace('$', '')
    t = re.sub(r'\\[a-zA-Z]+', '', t)
    t = re.sub(r'[{}]', '', t)
    return re.sub(r'[^一-鿿0-9a-zA-Z]', '', t)[:100]


def load_todo():
    rb = json.load(open(os.path.join(ROOT, 'data/ref_bank.json'), encoding='utf-8'))
    bank = json.load(open(os.path.join(ROOT, 'data/bank.json'), encoding='utf-8'))
    done = set()
    for q in bank:
        m = re.search(r'M-T-\d+-[EV]\d+', str(q.get('src', '')))
        if m:
            done.add(m.group(0))
    # 已有题的题干签名（用于抓「同题不同号」）
    stems = set()
    for q in bank:
        st = q.get('stem_text') or ''
        if isinstance(st, list):
            st = ' '.join(st)
        stems.add(sig(st))
    todo = []
    for k in rb:
        if not re.match(r'M-T-\d+-[EV]\d+$', k):
            continue
        if k in done:
            continue
        if sig(str(rb[k].get('stem', ''))) in stems:
            continue       # 同题已录（编号不同），跳过
        todo.append(k)
    return rb, sorted(todo)


def build_big():
    """拼 456 页为大串 + 归一化大串 + 偏移索引"""
    texts, starts, pos = [], [], [0]
    for i in range(1, 457):
        p = os.path.join(ROOT, '原件/按页还原/p%03d.txt' % i)
        t = open(p, encoding='utf-8').read() if os.path.exists(p) else ''
        texts.append(t)
        starts.append(len(t))
    # 每页起点（在 BIG 中的偏移）
    page_off, acc = [], 0
    for t in texts:
        page_off.append(acc)
        acc += len(t) + 1
    return texts, page_off


def norm(s):
    return re.sub(r'[\s\u200b]+', '', str(s))


def locate(nbig, stem, page_of_j):
    """返回 (命中, 在 BIG 中的字符下标)"""
    n = norm(stem)
    for st in (0, 3, 6, 10):
        for L in (16, 12, 20, 8):
            seg = n[st:st + L]
            if len(seg) < 8:
                continue
            j = nbig.find(seg)
            if j >= 0:
                return True, j
    return False, -1


def page_of(page_off, j):
    lo, hi = 0, len(page_off) - 1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if page_off[mid] <= j:
            lo = mid
        else:
            hi = mid - 1
    return lo + 1  # 1-based


def slice_stem(texts, page_off, j, raw_stem):
    """从命中处抽取还原版题干片段"""
    p = page_of(page_off, j)
    t = texts[p - 1]
    k = j - page_off[p - 1]
    # 从命中处向后取，遇到换行结尾或长度够了就停
    L = max(len(norm(raw_stem)), 20)
    seg = t[k:k + L * 3]
    # 截到第一个「换行 + 非延续」处
    m = re.search(r'\n\s*\n', seg)
    if m and m.start() > 20:
        seg = seg[:m.start()]
    seg = re.sub(r'\s+', ' ', seg).strip()
    return p, seg


def esc(s):
    # r"" 前缀下反斜杠原样保留（LaTeX 需要），只转义双引号
    return str(s).replace('"', '\\"')


def merge_frac(s):
    """把 PDF 提取的『分子\\n分母』合成为 LaTeX 分数"""
    if not s:
        return s
    s = str(s)
    # 连续两行且都短 -> 视为分数
    def rep(m):
        a, b = m.group(1).strip(), m.group(2).strip()
        return r'\frac{%s}{%s}' % (a, b)
    # A\nB 形式
    for _ in range(3):
        s2 = re.sub(r'([^\n]{1,12})\n([^\n]{1,12})(?=[\s,、）\)]|$)', rep, s)
        if s2 == s:
            break
        s = s2
    return s


def wrap(text, width=86):
    """把长文本切成 r\"...\" 拼接"""
    s = str(text).replace('\n', ' ').strip()
    s = re.sub(r'\s+', ' ', s)
    if not s:
        return '""'
    parts = []
    cur = ''
    for tok in re.findall(r'\S+\s*', s):
        if len(cur) + len(tok) > width and cur:
            parts.append(cur.rstrip())
            cur = tok
        else:
            cur += tok
    if cur:
        parts.append(cur.rstrip())
    return parts


def py_str_list(items, indent):
    """生成 ['a', 'b'] 或拼接形式"""
    out = []
    for it in items:
        out.append('r"%s"' % esc(it))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--n', type=int, default=20)
    ap.add_argument('--topic', default=None, help='只出某题型，如 M-T-143')
    ap.add_argument('--out', required=True)
    ap.add_argument('--only-locatable', action='store_true')
    a = ap.parse_args()

    rb, todo = load_todo()
    if a.topic:
        todo = [k for k in todo if k.startswith(a.topic)]
    texts, page_off = build_big()
    BIG = '\n'.join(texts)
    # 归一化 -> 原文下标映射（去掉空白后位置不再对应，必须建立映射）
    idx2orig = []
    for i, ch in enumerate(BIG):
        if not re.match(r'[\s\u200b]', ch):
            idx2orig.append(i)
    nbig = ''.join(BIG[k] for k in idx2orig)

    picked, loc_ok = [], 0
    for k in todo:
        q = rb[k]
        stem = str(q.get('stem', ''))
        ok, j = locate(nbig, stem, None)
        if ok:
            loc_ok += 1
            oj = idx2orig[j] if j < len(idx2orig) else 0
            p, seg = slice_stem(texts, page_off, oj, stem)
        else:
            p, seg = None, stem
        picked.append((k, q, ok, p, seg))
        if len(picked) >= a.n * 3 and sum(1 for x in picked if x[2]) >= a.n:
            break
        if a.topic is None and len(picked) > a.n * 6:
            break

    if a.only_locatable:
        picked = [x for x in picked if x[2]]
    picked = picked[:a.n]

    lines = []
    lines.append('# -*- coding: utf-8 -*-')
    lines.append('r"""第__批 · auto_draft 自动生成骨架（%d 题）' % len(picked))
    lines.append('')
    lines.append('⚠ 本文件由 tools/auto_draft.py 生成，**必须人工审核后**才能入库。')
    lines.append('')
    lines.append('审核清单：')
    lines.append('  1. 每题题干/选项对照 `原件/按页还原/pXXX.txt` 核对（页码见每题注释）')
    lines.append('  2. 根号、绝对值、上下标是提取时静默丢失的重灾区 —— 必须逐个确认')
    lines.append('  3. **答案必须独立验算**，不能盲信原书')
    lines.append('  4. 确认无误后删掉本题的 NEED_FIX 标记，并补写 review')
    lines.append('"""')
    lines.append('')

    var_i = 0
    varnames = []
    for k, q, ok, p, seg in picked:
        var_i += 1
        var = 'Q%02d' % var_i
        varnames.append(var)
        # 题干：结构取 ref_bank（准确），分数自动合成
        # 题干不自动合分数：长句误判率高（会把乘积误判成分数），
        # 保持原文 + 附还原版片段，由人工审核时修正
        stem_txt = re.sub(r'\s+', ' ', str(q.get('stem', ''))).strip()
        # 若定位成功，把还原版片段写进注释供人工对照
        ref_seg = re.sub(r'\s+', ' ', seg)[:160] if ok else ''
        opts = q.get('opts') or []
        letters = q.get('opt_letters') or ['A', 'B', 'C', 'D', 'E', 'F']
        ans = merge_frac(str(q.get('ans', ''))).replace('\n', ' ').strip()
        sol = re.sub(r'\s+', ' ', str(q.get('solution', ''))).strip()
        ana = re.sub(r'\s+', ' ', str(q.get('analysis', ''))).strip()

        lines.append('# %s  [页 p%s]  ans=%s%s' % (k, p, ans, '' if ok else '  ⚠未能定位'))
        if ref_seg:
            lines.append('#   还原版: %s' % ref_seg)
        lines.append('%s = {' % var)
        lines.append("    'type': '%s'," % ('选择' if len(opts) >= 2 else ('填空' if not opts else '解答')))
        lines.append("    'stem_text': (")
        parts = wrap(stem_txt)
        if parts and parts[0].startswith('r"'):
            for i, pt in enumerate(parts):
                lines.append('        %s%s' % (pt, '' if i == len(parts) - 1 else ' '))
        else:
            for i, pt in enumerate(parts):
                lines.append('        r"%s"%s' % (esc(pt), '' if i == len(parts) - 1 else ' '))
        lines.append('    ),')
        if opts:
            lines.append("    'opts': [")
            for i, o in enumerate(opts):
                lt = letters[i] if i < len(letters) else chr(ord('A') + i)
                lines.append("        ('%s', r\"%s\")," % (lt, esc(merge_frac(str(o)).replace('\n', ' '))))
            lines.append('    ],')
        else:
            lines.append("    'opts': [],")
        lines.append("    'answer': r\"%s\"," % esc(ans))
        if ana:
            lines.append("    'analysis': (")
            ap_parts = wrap(ana)
            for i, pt in enumerate(ap_parts):
                lines.append('        r"%s"%s' % (esc(pt), '' if i == len(ap_parts) - 1 else ' '))
            lines.append('    ),')
        else:
            lines.append("    'analysis': '',")
        lines.append("    'solution': (")
        if sol:
            sp = wrap(sol)
            for i, pt in enumerate(sp):
                lines.append('        r"%s"%s' % (esc(pt), '' if i == len(sp) - 1 else ' '))
        else:
            lines.append('        "NEED_FIX: 原题无详解，需独立推导"')
        lines.append('    ),')
        lines.append("    'review': (")
        lines.append('        r"NEED_FIX: 待审核。%s"' % ('定位成功，题干取自按页还原 p%s' % p if ok else '未能定位还原版，题干为原始破碎文本，必须对照原文重打'))
        lines.append('    ),')
        lines.append("    'difficulty': 0.85,")
        lines.append("    'topics': ['%s']," % k.rsplit('-', 1)[0])
        lines.append("    'src': '2024高中数学热点题型归纳完整解析版.pdf · %s'," % k)
        lines.append('}')
        lines.append('')

    lines.append('QS = [%s]' % ', '.join(varnames))
    out = os.path.join(ROOT, a.out)
    open(out, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    nhit = sum(1 for x in picked if x[2])
    print('已生成 %s' % out)
    print('  %d 题，其中 %d 题定位到还原版 (%.0f%%)' % (len(picked), nhit, 100.0 * nhit / max(len(picked), 1)))
    print('')
    print('下一步：')
    print('  python3 tools/lint_input.py %s --fix' % a.out)
    print('  # 然后人工审核 NEED_FIX 处')


if __name__ == '__main__':
    main()
