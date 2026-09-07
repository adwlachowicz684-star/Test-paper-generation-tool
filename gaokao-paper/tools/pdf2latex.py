# -*- coding: utf-8 -*-
r"""PDF 字符流 → LaTeX：结构感知重建，从源头避免「题目破碎」。

    python3 tools/pdf2latex.py <pdf> --page 11 --x0 30 --x1 298 --y0 126 --y1 175
    python3 tools/pdf2latex.py <pdf> --page 11 --scan     # 扫描全页，只输出含上下标的行
    python3 tools/pdf2latex.py <pdf> --page 0 --stats     # 看该页字体与字号分布

## 为什么需要它

常规提取把 PDF 拍平成纯文本，上下标、指数全部塌成一行：

    c = 0.5-0.2          ← 实际是 $c=0.5^{-0.2}$
    a =3,b = 2 3 4        ← 实际是 $a=\sqrt3,\ b=2^{\frac34}$

但**这些信息在 PDF 里一直都在**：上标字号 5.40，正文字号 9.01。
只是存 ref_bank 时被压成平文本丢弃了，导致后面只能靠人猜、反复返工。

本工具反过来利用字号与基线，把结构还原成 LaTeX，
把「人工猜结构」变成「机器算结构 + 人工审核答案」。

## 两种公式排版都支持

| 来源 | 根号 | 括号 | 上下标判据 |
|---|---|---|---|
| MathType（教辅原书） | U+F0E8/E9/EA 三段拼 | U+F0EE 私用区 | 字号 5.40 / 正文 9.01 |
| Word、LibreOffice | U+221A 标准字符 | 标准字符 | 字号 7.2 / 正文 11.99 |

两家**都会丢语义结构**（PDF 只存"字符画在哪个坐标、多大"），
但几何判据对两者都成立，所以本工具通用。

## 按字体分组取主字号（关键）

中英混排时中文与数学字号不同（实测 Word 转的 PDF：中文 10.5、数学 11.99）。
若整行取众数，主字号会被中文带偏到 10.5，导致相对 11.99 的
上标（如 9.5）判不出来。所以**主字号只在「数学字符」里取**。

## 判定规则（在两种 PDF 上逐字符核对过）

- 数学字符 = 非 CJK、非 CJK 标点的字符；中文正文原样输出，不参与上下标判定
- 行内主字号 = 数学字符的字号众数；`size < 主字号 × 0.85` 判为上下标
- 方向用 **bottom**（bbox[3]）判：实测上标与正文的 **top 几乎相等**
  （203.86 vs 203.83），但 bottom 差 3.6，用 top 会全部判反

分数线（\frac）与根号（\sqrt）是**矢量绘制**、不在文本流里，
本工具标出 `⟨?⟩` 占位，由人工按上下文补 —— 这类占比远小于上下标。
"""
import argparse
import collections
import sys

import pymupdf

# 私用区符号 → LaTeX 可读字符（与 dump_pdf.py 保持一致）
GLYPH = {
    0xF0EE: ('(', ')'),   # 圆括号，左右同码
    0xF0F6: ('[', ']'),   # 方括号
    0xF0F4: '|',          # 绝对值竖线
    0xF00A: "'",          # 导数撇号
    0xF001: '·',
    0xF026: '‾',
}
RATIO = 0.85      # 小于主字号的这个比例即判为上下标
ROW_TOL = 3.0     # 同一行的 y 容差
BASE_TOL = 1.5    # bottom 高出主线多少算上标

# CJK 及中文标点：这些是正文，不参与上下标判定
CJK_PUNCT = '，。；：、（）【】“”‘’？！．､　'


def is_math_char(c):
    """数学字符 = 非 CJK、非中文标点。中文正文原样输出。"""
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


def collect(page, x0, x1, y0, y1):
    """取区域内的字符 (top_y, x, size, char, bottom, font)。

    必须带上 bottom（bbox[3]）：判上下标方向只能靠它。
    实测上标与正文的 **top 几乎相等**（203.86 vs 203.83），
    但 bottom 差得很开（209.36 vs 213.0）—— 用 top 会全部判反。

    带上 font 是为了按字体分组取主字号，见文件头说明。
    """
    rd = page.get_text('rawdict')
    out = []
    for b in rd['blocks']:
        if b['type'] != 0:
            continue
        for l in b['lines']:
            for s in l['spans']:
                for ch in s['chars']:
                    x, y = ch['bbox'][0], ch['bbox'][1]
                    if x0 is not None and not (x0 <= x <= x1):
                        continue
                    if y0 is not None and not (y0 <= y <= y1):
                        continue
                    out.append((round(y, 1), round(x, 1),
                                round(s['size'], 2), ch['c'],
                                round(ch['bbox'][3], 1),
                                s['font'].split(',')[0]))
    out.sort()
    return out


def split_rows(chars):
    """按 top_y 聚类成视觉行，整条记录原样传递（含 bottom 与 font）。"""
    rows, cur, cy = [], [], None
    for rec in chars:
        y = rec[0]
        if cy is None or abs(y - cy) > ROW_TOL:
            if cur:
                rows.append(cur)
            cur, cy = [], y
        cur.append(rec)
    if cur:
        rows.append(cur)
    return rows


def norm(c):
    o = ord(c)
    if o in GLYPH:
        v = GLYPH[o]
        if isinstance(v, tuple):
            return v[0]          # 左右靠 x 定，这里先给左
        return v
    if 0xE000 <= o <= 0xF8FF:
        return '⟨?⟩'             # 未识别私用区，提醒人工
    return c


def rebuild_row(row):
    r"""单行 → LaTeX 片段。返回 (文本, 是否含上下标)。

    主字号只在**数学字符**里取众数：中英混排时中文字号不同，
    整行取众数会被中文带偏，导致相对数学主字号的上标判不出来。
    """
    if not row:
        return '', False

    math_chars = [r for r in row if is_math_char(r[3])]
    if not math_chars:
        # 纯中文行，原样输出
        return ''.join(r[3] for r in sorted(row, key=lambda z: z[1])), False

    # ── 主字号：只在数学字符里取众数 ──
    sizes = collections.Counter(r[2] for r in math_chars)
    main = sizes.most_common(1)[0][0]
    thr = main * RATIO

    # ── 主线基线：主字号数学字符的 bottom 众数 ──
    main_bt = [r[4] for r in math_chars if r[2] == main]
    base_bt = (collections.Counter(round(b) for b in main_bt).most_common(1)[0][0]
               if main_bt else 0)

    out, i, has_script = [], 0, False
    row = sorted(row, key=lambda r: r[1])      # 行内按 x 排
    while i < len(row):
        y, x, sz, c, bt, font = row[i]
        if is_math_char(c) and sz < thr:
            # 收集连续的小字（数学字符且小于阈值）
            grp = []
            while i < len(row) and is_math_char(row[i][3]) and row[i][2] < thr:
                grp.append(row[i])
                i += 1
            txt = ''.join(norm(r[3]) for r in grp)
            gbt = min(r[4] for r in grp)       # 该组的最高点(bottom 最小)
            # bottom 越小越靠上：明显高过主线 → 上标，否则下标
            if gbt < base_bt - BASE_TOL:
                out.append('^{%s}' % txt)
            else:
                out.append('_{%s}' % txt)
            has_script = True
        else:
            out.append(norm(c))
            i += 1
    return ''.join(out), has_script


def stats(page):
    """打印该页字体与字号分布，便于判断主字号阈值是否合理。"""
    chars = collect(page, None, None, None, None)
    by_font = collections.defaultdict(collections.Counter)
    for _, _, sz, c, _, font in chars:
        by_font[font][round(sz, 2)] += 1
    print('  字体 / 字号分布（该页共 %d 字符）：' % len(chars))
    for font, cnt in sorted(by_font.items(), key=lambda x: -sum(x[1].values())):
        tot = sum(cnt.values())
        top = cnt.most_common(3)
        print('    %-26s %5d 字   主字号 %s'
              % (font, tot, ', '.join('%.2f×%d' % (s, n) for s, n in top)))
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('pdf')
    ap.add_argument('--page', type=int, default=0)
    ap.add_argument('--x0', type=float)
    ap.add_argument('--x1', type=float)
    ap.add_argument('--y0', type=float)
    ap.add_argument('--y1', type=float)
    ap.add_argument('--scan', action='store_true',
                    help='扫描全页，只输出含上下标的行')
    ap.add_argument('--stats', action='store_true',
                    help='打印该页字体/字号分布')
    a = ap.parse_args()

    doc = pymupdf.open(a.pdf)
    page = doc[a.page]

    if a.stats:
        return stats(page)

    chars = collect(page, a.x0, a.x1, a.y0, a.y1)
    rows = split_rows(chars)

    if a.scan:
        print('  含上下标的行（已标为 ^{...} / _{...}）：')
        hit = 0
        for row in rows:
            txt, has = rebuild_row(row)
            if not has or len(txt.strip()) < 3:
                continue
            hit += 1
            print('    %s' % txt)
        print('  共 %d 行' % hit)
        return 0

    print('  区域重建结果：')
    for row in rows:
        txt, has = rebuild_row(row)
        if not txt.strip():
            continue
        print('    %s%s' % (txt, '   ← 含上下标' if has else ''))
    return 0


if __name__ == '__main__':
    sys.exit(main())
