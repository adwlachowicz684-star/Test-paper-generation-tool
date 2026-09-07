#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""restore.py —— PDF 公式统一还原器

把 pdf2latex.py（上下标）与 frac_scan.py（分数线）**合并成一个入口**，
按「先切分数块、再递归重建上下标」的顺序一次性还原整条公式。

    python3 tools/restore.py <pdf> --page 76
    python3 tools/restore.py <pdf> --page 76 --y0 640 --y1 700
    python3 tools/restore.py <pdf> --find 'lnx - x + a'
    python3 tools/restore.py <pdf> --page 0 --stats

## 实测效果（PDF 页 76，M-T-111-E1 所在页）

    \frac{1 + x}{e^{x}}                  ← 原提取：1 + x / ex
    \frac{\ln x - x + a}{x^{2}}          ← 原提取：lnx-x+a / x2
    \frac{x - 2\ln x + 1 - 2a}{x^{3}}    ← 原提取：x-2lnx+1-2a / x3

后两条是上一批**手工推了很久**的 $g(x)$ 与 $g'(x)$，现在自动出结果。

## 三段还原，各管一类破碎

| 破碎类型 | 来源 | 本工具的做法 |
|---|---|---|
| **上下标** | 字号/基线被压平 | 字号 < 主字号×0.85；方向用 **bottom** 判 |
| **分数线** | 矢量绘制，文本层没有 | 扫绘图指令里的水平线段，按坐标配对分子分母 |
| **特殊符号** | 私用区码位 | GLYPH 表映射（括号/竖线/撇号/根号…） |

## 两个关键判据（都踩过坑，别改反）

1. **判上下标必须用 bottom 不能用 top**。
   实测正文 top=203.83 / 上标 top=203.86（几乎相等），
   但 bottom 差 3.6 —— 用 top 会全部判反。
2. **主字号只在数学字符里取众数**。
   中英混排时中文与数学字号不同（Word 转的 PDF：中文 10.5、数学 11.99），
   整行取众数会被中文带偏，导致相对数学主字号的上标判不出来。

## 已知限制（遇到别硬调参数）

- **根号**：U+F0E8/E9/EA 三段拼的字符，本工具合并输出 `√`；
  但根号**覆盖的范围**无法确定，需人工补 —— 这是唯一必须人工的部分。
- **嵌套分数**：只出内层，外层线因找不到完整分母会被跳过，
  输出形如「分子在上、\frac{…}{…} 在下」，人工一眼能看出是嵌套。
- 分数线宽度默认 2~80pt，过宽/过窄的用 --minw/--maxw 调。
"""
import argparse
import collections
import sys

import pymupdf

# ── 私用区符号 → 可读字符（与 dump_pdf.py 保持一致）──
GLYPH = {
    0xF0EE: ('(', ')'),   # 圆括号，左右同码位，靠 x 定左右
    0xF0F6: ('[', ']'),   # 方括号
    0xF0F4: '|',          # 绝对值竖线
    0xF00A: "'",          # 导数撇号
    0xF001: '·',
    0xF026: '‾',
    0xF0E8: '√',          # 根号三段（上/中/下），连续出现只输出一个 √
    0xF0E9: '√',
    0xF0EA: '√',
}

RATIO = 0.85        # 字号 < 主字号 × RATIO 判为上下标
ROW_TOL = 3.0       # 同一视觉行的 top 容差
BASE_TOL = 1.5      # bottom 高出主线多少算上标
FRAC_TOL = 8.0      # 分子/分母与分数线的紧贴距离
FRAC_MINW = 2.0
FRAC_MAXW = 80.0
MATH_FONT_KW = ('Math', 'Symbol', 'MT', 'Cambria', 'Extra')

CJK_PUNCT = '，。；：、（）【】“”‘’？！．､　'


def is_math_char(c):
    """数学字符 = 非 CJK、非中文标点。中文正文原样输出，不参与上下标判定。"""
    if not c:
        return False
    o = ord(c)
    if '一' <= c <= '龥':
        return False
    if c in CJK_PUNCT:
        return False
    if o in (0x3000, 0x3001, 0x3002, 0xFF08, 0xFF09,
             0xFF0C, 0xFF0E, 0xFF1A, 0xFF1B):
        return False
    return True


# ── 采集 ──────────────────────────────────────────────

def collect(page, x0=None, x1=None, y0=None, y1=None):
    """取字符。必须带 bottom(y1)、size、font —— 三个判据都要用。"""
    rd = page.get_text('rawdict')
    out, n = [], 0
    for b in rd.get('blocks', []):
        if b.get('type') != 0:
            continue
        for ln in b.get('lines', []):
            for sp in ln.get('spans', []):
                f = sp.get('font', '').split(',')[0]
                sz = round(sp.get('size', 0), 2)
                for ch in sp.get('chars', []):
                    bb = ch['bbox']
                    cx = (bb[0] + bb[2]) / 2
                    if x0 is not None and not (x0 <= cx <= x1):
                        continue
                    if y0 is not None and not (y0 <= bb[1] <= y1):
                        continue
                    out.append({'id': n, 'x0': bb[0], 'y0': bb[1],
                                'x1': bb[2], 'y1': bb[3], 'cx': cx,
                                'c': ch['c'], 'font': f, 'size': sz})
                    n += 1
    return out


def collect_lines(page, minw=FRAC_MINW, maxw=FRAC_MAXW):
    """分数线 = 绘图指令中「高度≈0、宽度适中」的水平线段。

    竖线（分栏）、背景块、下边框都因 height 过大或 width 为 0 被过滤。
    """
    out = []
    for i, g in enumerate(page.get_drawings()):
        r = g.get('rect')
        if r is None:
            continue
        w, h = abs(r.width), abs(r.height)
        if h < 0.5 and minw <= w <= maxw:
            out.append({'id': i, 'x0': r.x0, 'y': r.y0, 'x1': r.x1})
    return out


# ── 重建 ──────────────────────────────────────────────

def norm(c):
    o = ord(c)
    if o in GLYPH:
        v = GLYPH[o]
        return v[0] if isinstance(v, tuple) else v
    if 0xE000 <= o <= 0xF8FF:
        return '⟨?⟩'          # 未识别私用区，提醒人工
    return c


def _dedup_sqrt(txt):
    """根号三段（U+F0E8/E9/EA）连续出现时只保留一个 √。"""
    return txt.replace('√√√', '√').replace('√√', '√')


def scripts(chars):
    r"""一个视觉层内的上下标重建。

    主字号只在数学字符里取众数（中英混排时中文会带偏）；
    方向用 bottom 判（top 几乎相等，用 top 会全判反）。
    """
    if not chars:
        return ''
    mathc = [c for c in chars if is_math_char(c['c'])]
    if not mathc:
        return _dedup_sqrt(''.join(c['c'] for c in sorted(chars, key=lambda z: z['cx'])))

    sizes = collections.Counter(c['size'] for c in mathc)
    main = sizes.most_common(1)[0][0]
    thr = main * RATIO

    main_bt = [c['y1'] for c in mathc if c['size'] == main]
    base_bt = (collections.Counter(round(b) for b in main_bt).most_common(1)[0][0]
               if main_bt else 0)

    out, i = [], 0
    row = sorted(chars, key=lambda c: c['cx'])
    paren_n = 0          # 圆/方括号左右同码位，行内交替判定
    while i < len(row):
        c = row[i]
        o = ord(c['c'])
        if o in (0xF0EE, 0xF0F6):
            pair = GLYPH[o]
            out.append(pair[0] if paren_n % 2 == 0 else pair[1])
            paren_n += 1
            i += 1
            continue
        # 括号/竖线类的字号可能偏小，但它们是定界符，不能判成上下标
        # （实测不排除会把 (x-a) 输出成 _{（}x - a_{（}）
        if norm(c['c']) in '( ) [ ] | { }':
            out.append(norm(c['c']))
            i += 1
            continue
        if is_math_char(c['c']) and c['size'] < thr:
            grp = []
            while i < len(row) and is_math_char(row[i]['c']) and row[i]['size'] < thr:
                grp.append(row[i])
                i += 1
            txt = _dedup_sqrt(''.join(norm(g['c']) for g in grp))
            # bottom 越小越靠上 → 明显高过主线是上标，否则下标
            if min(g['y1'] for g in grp) < base_bt - BASE_TOL:
                out.append('^{%s}' % txt)
            else:
                out.append('_{%s}' % txt)
        else:
            out.append(norm(c['c']))
            i += 1
    return _dedup_sqrt(''.join(out))


def _sub_lines(lines, cs, exclude_id):
    """落在字符集合 cs 范围内的其它分数线（供递归用）。"""
    if not cs:
        return []
    y0 = min(c['y0'] for c in cs)
    y1 = max(c['y1'] for c in cs)
    x0 = min(c['cx'] for c in cs)
    x1 = max(c['cx'] for c in cs)
    return [l for l in lines
            if l['id'] != exclude_id
            and y0 - 3 <= l['y'] <= y1 + 3
            and not (l['x1'] < x0 - 3 or l['x0'] > x1 + 3)]


def build(chars, lines, depth=0):
    """递归：先切分数块，块内再递归，最后落到 scripts() 做上下标。"""
    if not chars:
        return ''
    if lines and depth < 5:
        for L in sorted(lines, key=lambda t: (t['y'], t['x0'])):
            def inx(c):
                return L['x0'] - 1.5 <= c['cx'] <= L['x1'] + 1.5

            num = [c for c in chars if inx(c) and is_math_char(c['c'])
                   and L['y'] - FRAC_TOL <= c['y1'] <= L['y'] + 0.6]
            den = [c for c in chars if inx(c) and is_math_char(c['c'])
                   and L['y'] - 0.6 <= c['y0'] <= L['y'] + FRAC_TOL]
            if not (num and den):
                continue

            nid = set(c['id'] for c in num)
            did = set(c['id'] for c in den)
            rest = [c for c in chars if c['id'] not in nid | did]
            frac = r'\frac{%s}{%s}' % (
                build(num, _sub_lines(lines, num, L['id']), depth + 1),
                build(den, _sub_lines(lines, den, L['id']), depth + 1))

            left = [c for c in rest if c['cx'] < L['x0']]
            right = [c for c in rest if c['cx'] > L['x1']]
            return (build(left, _sub_lines(lines, left, L['id']), depth + 1)
                    + frac
                    + build(right, _sub_lines(lines, right, L['id']), depth + 1))
    return scripts(chars)


def split_rows(chars):
    """按 top 聚类成视觉行。"""
    rows, cur, cy = [], [], None
    for c in sorted(chars, key=lambda z: (z['y0'], z['cx'])):
        if cy is None or abs(c['y0'] - cy) > ROW_TOL:
            if cur:
                rows.append(cur)
            cur, cy = [], c['y0']
        cur.append(c)
    if cur:
        rows.append(cur)
    return rows


def run(chars, lines):
    r"""全局还原：先切分数块，再按行输出。

    分数块必须**先全局切**再归行 —— 分子与分母在 PDF 里分属不同的
    视觉行（分子在线上、分母在线下），按行处理时每行都看不到完整的分数，
    结果就是分数永远出不来。这是第一版踩的坑。
    """
    occupied, fracs = set(), []
    for L in sorted(lines, key=lambda t: (t['y'], t['x0'])):
        def inx(c):
            return L['x0'] - 1.5 <= c['cx'] <= L['x1'] + 1.5

        num = [c for c in chars if c['id'] not in occupied and inx(c)
               and is_math_char(c['c'])
               and L['y'] - FRAC_TOL <= c['y1'] <= L['y'] + 0.6]
        den = [c for c in chars if c['id'] not in occupied and inx(c)
               and is_math_char(c['c'])
               and L['y'] - 0.6 <= c['y0'] <= L['y'] + FRAC_TOL]
        if not (num and den):
            continue
        occupied |= set(c['id'] for c in num) | set(c['id'] for c in den)
        fracs.append({
            'x0': min(min(c['cx'] for c in num), L['x0']),
            'y0': min(c['y0'] for c in num),
            'txt': r'\frac{%s}{%s}' % (
                build(num, _sub_lines(lines, num, L['id'])),
                build(den, _sub_lines(lines, den, L['id']))),
        })

    rest = [c for c in chars if c['id'] not in occupied]
    rows = split_rows(rest)
    tops = [min(c['y0'] for c in r) for r in rows]

    # 每个分数块只归到「分子顶部最接近」的那一行 —— 否则会在
    # 相邻几行里重复出现同一个 \frac（第一版实测一个分数出现 3 次）
    bucket = [[] for _ in rows]
    for f in fracs:
        best, bd = None, 1e9
        for i, t in enumerate(tops):
            d = abs(f['y0'] - t)
            if d < bd:
                bd, best = d, i
        if best is not None and bd <= 12:
            bucket[best].append(f)

    out = []
    for row, fs in zip(rows, bucket):
        ry0 = min(c['y0'] for c in row)
        items = [(c['cx'], 0, norm(c['c'])) for c in row]
        items += [(f['x0'], 1, f['txt']) for f in fs]
        items.sort(key=lambda t: (t[0], t[1]))
        out.append((ry0, ''.join(t[2] for t in items)))
    return out


def stats(page):
    chars = collect(page)
    by_font = collections.defaultdict(collections.Counter)
    for c in chars:
        by_font[c['font']][c['size']] += 1
    print('  字体 / 字号分布（该页共 %d 字符）：' % len(chars))
    for f, cnt in sorted(by_font.items(), key=lambda x: -sum(x[1].values())):
        print('    %-26s %5d 字   主字号 %s'
              % (f, sum(cnt.values()),
                 ', '.join('%.2f×%d' % (s, n) for s, n in cnt.most_common(3))))
    return 0


def find_pages(doc, kw):
    return [i for i in range(len(doc)) if kw in doc[i].get_text()]


def main():
    ap = argparse.ArgumentParser(description='PDF 公式统一还原器（上下标 + 分数线）')
    ap.add_argument('pdf')
    ap.add_argument('--page', type=int, default=None, help='PDF 页（0-based）')
    ap.add_argument('--find', default=None, help='按关键词定位页面')
    ap.add_argument('--x0', type=float)
    ap.add_argument('--x1', type=float)
    ap.add_argument('--y0', type=float)
    ap.add_argument('--y1', type=float)
    ap.add_argument('--minw', type=float, default=FRAC_MINW)
    ap.add_argument('--maxw', type=float, default=FRAC_MAXW)
    ap.add_argument('--plain', action='store_true',
                    help='不按行分组，整页一次性重建')
    ap.add_argument('--stats', action='store_true')
    a = ap.parse_args()

    doc = pymupdf.open(a.pdf)
    if a.find:
        pages = find_pages(doc, a.find)
        if not pages:
            sys.exit('未找到关键词：%s' % a.find)
    elif a.page is not None:
        pages = [a.page]
    else:
        sys.exit('需要 --page 或 --find')

    for pno in pages:
        page = doc[pno]
        if a.stats:
            return stats(page)

        chars = collect(page, a.x0, a.x1, a.y0, a.y1)
        lines = collect_lines(page, a.minw, a.maxw)
        print('=' * 62)
        print('PDF 页 %d（1-based 页 %d）  字符 %d  分数线 %d 条'
              % (pno, pno + 1, len(chars), len(lines)))
        print('=' * 62)

        if a.plain:
            print('  %s' % build(chars, lines))
            continue

        for y, txt in run(chars, lines):
            if not txt.strip():
                continue
            mark = '  ← 含结构' if ('^' in txt or '_' in txt or '\\frac' in txt) else ''
            print('  y=%-7.1f %s%s' % (y, _dedup_sqrt(txt), mark))
    return 0


if __name__ == '__main__':
    sys.exit(main())
