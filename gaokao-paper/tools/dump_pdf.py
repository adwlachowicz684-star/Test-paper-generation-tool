# -*- coding: utf-8 -*-
r"""教辅 PDF 一键 dump —— 把数学符号还原成人能读的文本。

    python3 tools/dump_pdf.py <pdf路径> --find '特征词' [--context 2500]
    python3 tools/dump_pdf.py <pdf路径> --pages 44 45      # 整页还原
    python3 tools/dump_pdf.py <pdf路径> --pages 44 --chars # 字符级（定括号/撇号用）
    python3 tools/dump_pdf.py <pdf路径> --glyphs           # 统计私用区码位

教辅 PDF 用 MathType/PMExtra 字体，数学符号落在 Unicode 私用区，
常规 get_text() 直接吞掉 —— 这是「提取出来的题干自相矛盾」的头号原因。
本脚本按码位把它们还原成 LaTeX 可读的字符。

已验证的映射见 GLYPH 表；未列出的码位原样保留并在后面标 ?，
用 --chars 看上下文即可判定（见 skill/references/14-pdf-glyphs.md）。
"""
import argparse
import re
import sys

import pymupdf

# ── 已验证的码位映射（在《2024高中数学热点题型归纳完整解析版》上逐字符核对过）
GLYPH = {
    0xF0EE: '(',   # 圆括号 ( 或 ) —— 左右同码，靠 x 坐标定左右
    0xF0F6: '[',   # 方括号 [ 或 ]
    0xF0F4: '|',   # 绝对值竖线
    0xF00A: '′',   # 导数撇号 f′(x)
    0xF001: '·',   # 目录点线 / 填充点
    0xF026: '‾',   # 平均值上划线（如 ȳ）
}

# ── 成对判左右：同一行内按 x 坐标，小的为左、大的为右
PAIR = {0xF0EE: ('(', ')'), 0xF0F6: ('[', ']'), 0xF0F4: ('|', '|')}


COL_X = 298.0     # 双栏分栏线（A4 两栏教辅通用，可按需改）
ROW_TOL = 4.0     # 同一行的 y 容差


def _cluster_rows(chars, tol=ROW_TOL):
    """把 (x, y, c) 按 y 聚类成视觉行；行内按 x 排序。"""
    rows = []
    cur = []
    cur_y = None
    for x, y, c in sorted(chars, key=lambda t: (t[1], t[0])):
        if cur and abs(y - cur_y) > tol:
            rows.append(cur)
            cur = []
            cur_y = None
        if not cur:
            cur_y = y
        cur.append((x, c))
    if cur:
        rows.append(cur)
    return [sorted(r) for r in rows]


def page_text(page, col_x=COL_X):
    """还原单页文本。返回 (文本, 该页未知码位集合)。

    不用 PyMuPDF 的行切分：括号/撇号是独立字体、基线不同，
    会被切到单独的行里，导致「一行里只有 1 个括号」而无法配对。
    这里改为自己按 (栏, y) 聚类重建视觉行，配对才稳定。
    """
    rd = page.get_text('rawdict')
    buckets = {0: [], 1: []}
    for b in rd['blocks']:
        if b['type'] != 0:
            continue
        for l in b['lines']:
            for s in l['spans']:
                for ch in s['chars']:
                    x, y = ch['bbox'][0], ch['bbox'][1]
                    buckets[0 if x < col_x else 1].append((x, y, ch['c']))

    unknown = set()
    out = []
    for col in (0, 1):
        if not buckets[col]:
            continue
        if col == 1:
            out.append('\n' + '─' * 12 + ' 右栏 ' + '─' * 12)
        for row in _cluster_rows(buckets[col]):
            # 成对符号：同一行内按 x 排序后**交替**判左右。
            # 一行常有多对括号（如 `(0,+∞)` 与 `f(x)` 并存），
            # 只认最左最右会把中间几对全部漏掉、还原成乱码。
            for code, (lp, rp) in PAIR.items():
                xs = sorted(x for x, c in row if ord(c) == code)
                if not xs:
                    continue
                side = {x: (lp if i % 2 == 0 else rp)
                        for i, x in enumerate(xs)}
                row = [(x, side.get(x, c) if ord(c) == code else c)
                       for x, c in row]
            parts = []
            for x, c in row:
                o = ord(c)
                if o in PAIR:                       # 已在上面替换成 ASCII
                    parts.append(c)
                elif o in GLYPH:
                    parts.append(GLYPH[o])
                elif 0xE000 <= o <= 0xF8FF:
                    parts.append(c)
                    unknown.add(o)
                else:
                    parts.append(c)
            out.append(''.join(parts))
    return '\n'.join(out), unknown


def page_chars(page, y0=None, y1=None, x0=None, x1=None, codes=None):
    """字符级输出：逐字符列出码位，用于精确定括号/撇号/竖线。"""
    rd = page.get_text('rawdict')
    rows = []
    for b in rd['blocks']:
        if b['type'] != 0:
            continue
        for l in b['lines']:
            for s in l['spans']:
                for ch in s['chars']:
                    x, y = ch['bbox'][0], ch['bbox'][1]
                    if y0 is not None and not (y0 <= y <= y1):
                        continue
                    if x0 is not None and not (x0 <= x <= x1):
                        continue
                    o = ord(ch['c'])
                    if codes and o not in codes:
                        continue
                    rows.append((y, x, s['font'], o, ch['c']))
    rows.sort(key=lambda r: (round(r[0], 1), r[1]))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('pdf')
    ap.add_argument('--find', help='按特征词定位，打印上下文')
    ap.add_argument('--context', type=int, default=2500)
    ap.add_argument('--pages', type=int, nargs='+', help='页码（0-based）')
    ap.add_argument('--chars', action='store_true', help='字符级输出')
    ap.add_argument('--y0', type=float)
    ap.add_argument('--y1', type=float)
    ap.add_argument('--x0', type=float)
    ap.add_argument('--x1', type=float)
    ap.add_argument('--glyphs', action='store_true', help='统计全书私用区码位')
    a = ap.parse_args()

    doc = pymupdf.open(a.pdf)

    if a.glyphs:
        import collections
        cnt = collections.Counter()
        sample = {}
        for pno in range(doc.page_count):
            for row in page_chars(doc[pno]):
                o = row[3]
                if 0xE000 <= o <= 0xF8FF:
                    cnt[o] += 1
                    sample.setdefault(o, (pno, round(row[1]), round(row[0])))
        print('%-10s %8s  %s' % ('码位', '次数', '首次出现(页,x,y)'))
        for o, n in cnt.most_common():
            known = GLYPH.get(o, '')
            print('U+%04X    %7d  %-20s %s'
                  % (o, n, str(sample[o]), ('→ ' + known) if known else ''))
        return 0

    if a.chars:
        for pno in a.pages:
            print('=' * 20, '页', pno, '=' * 20)
            for y, x, f, o, c in page_chars(doc[pno], a.y0, a.y1, a.x0, a.x1):
                mark = '   ← 已知:%s' % GLYPH[o] if o in GLYPH else (
                    '   ← 未知私用区' if 0xE000 <= o <= 0xF8FF else '')
                print('  y=%7.2f x=%6.1f %-16s U+%04X %r%s'
                      % (y, x, f.split(',')[0], o, c, mark))
        return 0

    if a.pages is not None:
        for pno in a.pages:
            t, unk = page_text(doc[pno])
            print('=' * 20, '页', pno, '=' * 20)
            print(t)
            if unk:
                print('\n  [未知码位] ' + ' '.join(
                    'U+%04X' % o for o in sorted(unk)))
        return 0

    if a.find:
        full = []
        for i in range(doc.page_count):
            t, _ = page_text(doc[i])
            full.append(t)
        for pno, t in enumerate(full):
            i = t.find(a.find)
            if i >= 0:
                print('>>> 命中于 PDF 页 %d（0-based）' % pno)
                print(t[max(0, i - 500): i + a.context])
                return 0
        print('未找到：%r' % a.find)
        return 1

    print(__doc__)
    return 0


if __name__ == '__main__':
    sys.exit(main())
