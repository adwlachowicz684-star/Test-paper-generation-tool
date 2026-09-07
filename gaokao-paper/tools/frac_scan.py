#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""分数线自动扫描 —— 从 PDF 绘图指令还原分数结构

## 为什么需要它

教辅里的分数线是**矢量绘制**的（不是字符），常规 get_text() 完全看不到，
所以提取结果是「1 + x」与「ex」分列两行，中间那根线消失 —— 这是题干破碎的
头号原因，占已录题目的 13%。

但**分数线在绘图指令里是拿得到的**：它表现为一条「高度≈0、宽度几 pt」的
水平线段。本脚本扫描这些线段，再按坐标把上下的数学字符配成分子和分母。

    >>> \frac{x - 2lnx + 1 - 2a}{x3}   ← 自动识别出 M-T-111-E1 的 g'(x)

## 用法

    python3 tools/frac_scan.py <pdf> --page 77              # 扫一页
    python3 tools/frac_scan.py <pdf> --page 77 --context 3  # 带上下文原文
    python3 tools/frac_scan.py <pdf> --find 'lnx - x + a'   # 按关键词定位

## 输出解读

    \frac{1 x}{ex}   ← 实际是 \frac{1+x}{e^x}

- **加减号会丢**：± 是特殊码位，需配合 dump_pdf.py --chars 确认
- **上标显示为平文本**（x3 实为 x³）：用 pdf2latex.py 的字号判据补
- 分子/分母只取数学字体字符，中文正文自动排除

## 已知限制

1. **根号不能这样还原** —— 根号是 U+F0E8/E9/EA 三段拼的字符，不是线段
2. **嵌套分数**（分子里还有分数）只出外层，需递归，目前人工补
3. 分数线过宽（>80pt）或过窄（<2pt）会被过滤，可调 --minw/--maxw

## 与 pdf2latex.py 的关系

    pdf2latex.py  处理上下标（字号 + bottom 判据）
    frac_scan.py  处理分数线（绘图指令 + 坐标配对）
    两者互补，合起来覆盖绝大部分破碎场景
"""

import argparse
import re
import sys

try:
    import fitz  # PyMuPDF
except ImportError:
    sys.exit('需要 PyMuPDF：pip install pymupdf')

# 数学字体关键词（用于排除中文正文）
MATH_FONT_KW = ('Math', 'Symbol', 'MT', 'Cambria', 'Extra')


def is_math_font(name):
    return any(k in (name or '') for k in MATH_FONT_KW)


def collect_chars(page):
    """收集字符 (x0, y0, x1, y1, char, font, size)。"""
    out = []
    try:
        rd = page.get_text('rawdict')
    except Exception:
        return out
    for b in rd.get('blocks', []):
        for ln in b.get('lines', []):
            for sp in ln.get('spans', []):
                f = sp.get('font', '')
                sz = sp.get('size', 0)
                for c in sp.get('chars', []):
                    bb = c['bbox']
                    out.append((bb[0], bb[1], bb[2], bb[3], c['c'], f, sz))
    return out


def collect_frac_lines(page, minw=2.0, maxw=80.0):
    """从绘图指令里挑出疑似分数线的水平线段。"""
    out = []
    try:
        drawings = page.get_drawings()
    except Exception:
        return out
    for g in drawings:
        r = g.get('rect')
        if r is None:
            continue
        w, h = abs(r.width), abs(r.height)
        # 水平、细长、宽度在合理区间
        if h < 0.5 and minw <= w <= maxw:
            out.append((r.x0, r.y0, r.x1))
    return out


def scan_page(page, minw=2.0, maxw=80.0, gap=10.0):
    """返回 [(y, x0, x1, 分子, 分母), ...]"""
    lines = collect_frac_lines(page, minw, maxw)
    chars = collect_chars(page)
    math = [c for c in chars if is_math_font(c[5])]
    res = []
    for x0, y, x1 in sorted(lines, key=lambda t: t[1]):
        cx_lo, cx_hi = x0 - 1, x1 + 1
        above = [c for c in math
                 if cx_lo <= (c[0] + c[2]) / 2 <= cx_hi
                 and y - gap <= c[3] <= y + 0.6]
        below = [c for c in math
                 if cx_lo <= (c[0] + c[2]) / 2 <= cx_hi
                 and y - 0.6 <= c[1] <= y + gap]
        if above and below:
            num = ''.join(c[4] for c in sorted(above, key=lambda t: t[0]))
            den = ''.join(c[4] for c in sorted(below, key=lambda t: t[0]))
            res.append((y, x0, x1, num, den))
    return res


def find_pages(doc, keyword, maxpages=None):
    """按关键词找 PDF 页（0-based）。"""
    hits = []
    limit = maxpages or len(doc)
    for i in range(min(limit, len(doc))):
        try:
            t = doc[i].get_text()
        except Exception:
            continue
        if keyword in t:
            hits.append(i)
    return hits


def main():
    ap = argparse.ArgumentParser(
        description='分数线自动扫描：从 PDF 绘图指令还原分数结构')
    ap.add_argument('pdf')
    ap.add_argument('--page', type=int, default=None,
                    help='PDF 页（0-based；索引里的 p077.txt 对应 --page 76）')
    ap.add_argument('--find', default=None, help='按关键词定位页面')
    ap.add_argument('--minw', type=float, default=2.0, help='分数线最小宽度')
    ap.add_argument('--maxw', type=float, default=80.0, help='分数线最大宽度')
    ap.add_argument('--gap', type=float, default=10.0, help='分子/分母最大垂直距离')
    ap.add_argument('--context', type=int, default=0,
                    help='>0 时同时打印该页原文（0 表示不打印）')
    a = ap.parse_args()

    doc = fitz.open(a.pdf)
    pages = []
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
        res = scan_page(page, a.minw, a.maxw, a.gap)
        print('=' * 60)
        print('PDF 页 %d（1-based 页 %d）  检出分数 %d 处'
              % (pno, pno + 1, len(res)))
        print('=' * 60)
        if a.context:
            print(page.get_text()[:a.context * 500])
            print('-' * 60)
        for y, x0, x1, num, den in res:
            print('  \\frac{%s}{%s}      y=%.1f x=[%.1f,%.1f]'
                  % (num, den, y, x0, x1))
        if not res:
            print('   （未检出；可放宽 --minw/--maxw/--gap 再试）')


if __name__ == '__main__':
    main()
