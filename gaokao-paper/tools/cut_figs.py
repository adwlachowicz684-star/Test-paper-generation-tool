# -*- coding: utf-8 -*-
r"""图题切图 —— 列出图位、校验边界、按题目 ID 命名切出。

    # 1) 先看某页有哪些图、各自在什么位置
    python3 tools/cut_figs.py <pdf> --list 45

    # 2) 校验候选框四周有没有混入邻题文字（不切图，只看报告）
    python3 tools/cut_figs.py <pdf> --check 45 --boxes 332,491,442,601 457,493,557,601

    # 3) 正式切图，文件名用题目 ID（入库后才知道 ID 就先填预估的，见下）
    python3 tools/cut_figs.py <pdf> --cut 45 --qid M-H0190 --boxes 332,491,442,601 457,493,557,601

切完把返回的 figs 列表原样填进题目的 figs 字段即可，三端（网页/HTML/Word）
都按 `{qid}_fig{n}.png` 在 `src/slices/<科目>/` 下找图。

ID 尚未确定时的做法：先按预估 ID 切（下一批的第一个号），入库后若实际 ID
不同，本工具会打印改名命令；也可直接跑 --rename 修正。
"""
import argparse
import os
import sys

import pymupdf

SLICE = os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))), 'src', 'slices')
PAD = 6        # 边界校验时向外扩的探测宽度


def parse_boxes(items):
    out = []
    for s in items:
        a = [float(v) for v in s.replace(' ', ',').split(',') if v != '']
        if len(a) != 4:
            raise SystemExit('框格式应为 x0,y0,x1,y1，收到：%r' % s)
        out.append(a)
    return out


def list_figs(page):
    """列出该页所有位图及其位置。矢量图（get_drawings）不在此列。"""
    rows = []
    for i, im in enumerate(page.get_images(full=True)):
        for r in page.get_image_rects(im[0]):
            rows.append((i, im[0], im[2], im[3], r))
    print('  页内位图 %d 个' % len(rows))
    for i, xref, w, h, r in rows:
        print('  #%d  xref=%d  原始 %dx%d  位置 (%d,%d)-(%d,%d)  → --boxes %d,%d,%d,%d'
              % (i, xref, w, h, r.x0, r.y0, r.x1, r.y1,
                 round(r.x0), round(r.y0), round(r.x1), round(r.y1)))
    return rows


def check_boxes(page, boxes):
    """校验每个框有没有切错。

    判据是**框内**有没有邻题文字 —— 框外紧贴着选项/作答位是正常的
    （题目排版本就如此），框内出现它们才是切歪了。
    纯曲线图框内应无文字；有坐标轴标注（如 `O`、`x`、`y`、数字）属正常。
    """
    ok = True
    for n, (x0, y0, x1, y1) in enumerate(boxes, 1):
        print('  ── 框%d (%g,%g)-(%g,%g)' % (n, x0, y0, x1, y1))
        inner = page.get_textbox(pymupdf.Rect(x0, y0, x1, y1)).strip()
        if inner:
            # 坐标轴标注通常很短，且不含中文
            if len(inner) <= 12 and not any('一' <= c <= '龥' for c in inner):
                print('     框内标注: %r   → 坐标轴标注，正常' % inner)
            else:
                print('     ★ 框内有正文: %r   → 切进邻题了，收窄该框' % inner)
                ok = False
        else:
            print('     框内无文字 → 纯图，安全')
        # 框外一圈只作提示，帮助判断边界贴得紧不紧
        around = {
            '上': (x0 - PAD, y0 - PAD - 8, x1 + PAD, y0 - 2),
            '下': (x0 - PAD, y1 + 2, x1 + PAD, y1 + PAD + 8),
            '左': (x0 - PAD - 8, y0 - PAD, x0 - 2, y1 + PAD),
            '右': (x1 + 2, y0 - PAD, x1 + PAD + 8, y1 + PAD),
        }
        for name, r in around.items():
            t = page.get_textbox(pymupdf.Rect(*r)).strip().replace('\n', '/')
            if t:
                print('     框外%s侧紧邻: %r' % (name, t))
    return ok


def do_cut(page, qid, boxes, sub='数学'):
    outdir = os.path.join(SLICE, sub)
    os.makedirs(outdir, exist_ok=True)
    figs = []
    for gi, (x0, y0, x1, y1) in enumerate(boxes, 1):
        pix = page.get_pixmap(clip=pymupdf.Rect(x0, y0, x1, y1), dpi=300)
        fn = '%s_fig%d.png' % (qid, gi)
        pix.save(os.path.join(outdir, fn))
        kb = os.path.getsize(os.path.join(outdir, fn)) // 1024
        figs.append({'file': fn, 'w': pix.width, 'h': pix.height, 'kb': kb})
        print('  切出 %s  %dx%d  %dKB' % (fn, pix.width, pix.height, kb))
    print('\n填进题目的 figs 字段：')
    print('  %r' % (figs,))
    return figs


def do_rename(old, new, sub='数学'):
    outdir = os.path.join(SLICE, sub)
    n = 0
    for gi in range(1, 10):
        src = os.path.join(outdir, '%s_fig%d.png' % (old, gi))
        if not os.path.exists(src):
            break
        dst = os.path.join(outdir, '%s_fig%d.png' % (new, gi))
        os.rename(src, dst)
        print('  %s → %s' % (os.path.basename(src), os.path.basename(dst)))
        n += 1
    print('  改名 %d 张；记得同步把 bank.json 里该题 figs 的 file 一起改掉' % n)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('pdf')
    ap.add_argument('--list', type=int, metavar='PAGE')
    ap.add_argument('--check', type=int, metavar='PAGE')
    ap.add_argument('--cut', type=int, metavar='PAGE')
    ap.add_argument('--boxes', nargs='+', default=[])
    ap.add_argument('--qid', help='题目 ID，如 M-H0190')
    ap.add_argument('--sub', default='数学')
    ap.add_argument('--rename', nargs=2, metavar=('OLD', 'NEW'))
    a = ap.parse_args()

    if a.rename:
        return do_rename(a.rename[0], a.rename[1], a.sub)

    doc = pymupdf.open(a.pdf)

    if a.list is not None:
        return list_figs(doc[a.list])

    if a.check is not None:
        boxes = parse_boxes(a.boxes)
        ok = check_boxes(doc[a.check], boxes)
        print('\n  结论：%s' % ('边界安全，可切' if ok else '有问题，先收窄再切'))
        return 0 if ok else 1

    if a.cut is not None:
        if not a.qid:
            raise SystemExit('--cut 需要 --qid')
        boxes = parse_boxes(a.boxes)
        if not boxes:
            raise SystemExit('--cut 需要 --boxes')
        check_boxes(doc[a.cut], boxes)
        return do_cut(doc[a.cut], a.qid, boxes, a.sub)

    print(__doc__)
    return 0


if __name__ == '__main__':
    sys.exit(main())
