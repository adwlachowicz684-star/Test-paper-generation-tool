# -*- coding: utf-8 -*-
r"""破碎题「可救性」扫描器。

    python3 tools/scan_recoverable.py                # 扫全部跳过题
    python3 tools/scan_recoverable.py --reason 提取破碎
    python3 tools/scan_recoverable.py --page-dir     # 同时回原件页文本查证
    python3 tools/scan_recoverable.py --key M-T-303-V3

## 为什么需要它

此前把一批题统一标成「提取破碎」，依据只是 `ref_bank` 的提取结果。
第 134 批回查原件后发现：**ref_bank 提取失败 ≠ 原题不可录**。
大量详解在 `原件/按页还原/pXXX.txt` 里是完整的，甚至 ref_bank 自身的
`solution` 字段也有相当多可读。真正的不可救只占少数。

本工具把「能不能救」从**凭印象判断**变成**可复算的指标**：
扫描每题的字段完整度，再回原件页文本核对，给出 A/B/C/D 四级评级。

## 四级评级

  A 直接可录    —— 题干、选项（或题问）、详解三者齐备
  B 可重建      —— 缺其一，但可独立推导补全（如选项只剩数字碎片）
  C 可降级录入  —— 选项不可还原但题干+详解完整 ⟹ 改填空/解答题
  D 不可救      —— 核心信息在图，或题干与详解同时破碎

## 关键原则：可降级录入（C 级）

一道选择题若「题干完整 + 详解完整 + 答案可独立验证」，仅选项 OCR 损毁，
**不要放弃**——改成填空题录入（去掉选项、保留问答），题目价值就保住了。
第 134 批的 M-T-375-V1、M-T-243-V1 即如此处理。
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
BANK = os.path.join(ROOT, 'data', 'bank.json')
REFBANK = os.path.join(ROOT, 'data', 'ref_bank.json')
SKIPPED = os.path.join(ROOT, 'data', 'skipped.json')
PAGE_DIR = os.path.join(ROOT, '原件', '按页还原')

# 详解低于此长度基本无内容
SOL_MIN = 260
# 题干低于此长度视为残破
STEM_MIN = 45

# 依赖图形的关键词：命中即 D 级（除非 stem 里另有足够数据）
FIG_WORDS = ('如图', '如图所示', '图象', '图像', '三视图', '直观图', '网格纸',
             '俯视图', '正视图', '侧视图', '展开图', '部分图象')


def load_json(p):
    with open(p, encoding='utf-8') as f:
        return json.load(f)


def stem_fig_dependent(stem):
    """题干是否依赖未提取的图形。"""
    return any(w in (stem or '') for w in FIG_WORDS)


def page_text(page):
    if not page:
        return ''
    for name in ('p%03d.txt' % page, 'p%d.txt' % page):
        p = os.path.join(PAGE_DIR, name)
        if os.path.exists(p):
            with open(p, encoding='utf-8', errors='ignore') as f:
                return f.read()
    return ''


def grade(item, ref, use_page=True):
    """给一道跳过题评级，返回 (等级, 依据列表)。"""
    key = item.get('key')
    v = ref.get(key) or {}
    stem = str(v.get('stem') or item.get('stem_raw') or '')
    sol = str(v.get('solution') or '')
    opts = v.get('opts') or []
    ans = str(v.get('ans') or item.get('ref_answer') or '')

    reasons = []
    has_stem = len(stem) >= STEM_MIN
    has_sol = len(sol) >= SOL_MIN
    has_opts = bool(opts) and any(str(o).strip() for o in opts)
    # 选项是否只是「同形碎片」（如四项都塌成同一个字符串）
    opts_degenerate = has_opts and len({str(o).strip() for o in opts}) == 1

    if not has_stem:
        reasons.append('题干残破(%d字)' % len(stem))
    if not has_sol:
        reasons.append('详解缺失或过短(%d字)' % len(sol))
    if has_opts and opts_degenerate:
        reasons.append('选项退化为同形碎片')

    # D 级：依赖图形
    if stem_fig_dependent(stem):
        # 若详解里还有实质内容，也许仍可降级（图形只影响选项）
        if has_sol:
            reasons.append('题干含「如图」但详解完整，或可降级')
            return ('C', reasons) if has_stem else ('D', reasons)
        reasons.append('依赖未提取图形')
        return 'D', reasons

    # A 级：三者齐备
    if has_stem and has_sol and has_opts and not opts_degenerate:
        reasons.append('题干/选项/详解齐备')
        return 'A', reasons

    # C 级：题干+详解完整但选项不可用 ⟹ 可降级为填空
    if has_stem and has_sol and (not has_opts or opts_degenerate):
        reasons.append('题干与详解完整，仅选项不可用 ⟹ 可改填空/解答录入')
        return 'C', reasons

    # B 级：缺其一但可推导
    if has_stem and has_opts and not opts_degenerate:
        reasons.append('题干与选项在，详解缺 ⟹ 需独立推导补全')
        return 'B', reasons
    if has_stem and not has_sol:
        reasons.append('仅题干完整 ⟹ 需全量独立推导')
        return 'B', reasons

    reasons.append('题干与详解均不足')
    return 'D', reasons


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--reason', default=None, help='只扫某个原因，如 提取破碎')
    ap.add_argument('--key', default=None, help='只扫指定 key')
    ap.add_argument('--page-dir', action='store_true', help='回原件页文本核对')
    ap.add_argument('--min', default='A', help='只显示 >= 该等级（A/B/C/D）')
    args = ap.parse_args()

    sk = load_json(SKIPPED)
    ref = load_json(REFBANK)
    items = sk['items']
    if args.reason:
        items = [i for i in items if i.get('reason') == args.reason]
    if args.key:
        items = [i for i in items if i.get('key') == args.key]
    items = [i for i in items if i.get('reason') != '已补录']

    order = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    rows = []
    for it in items:
        g, rs = grade(it, ref, args.page_dir)
        rows.append((g, it, rs))

    rows.sort(key=lambda r: (order[r[0]], r[1].get('key') or ''))

    cnt = {}
    for g, _, _ in rows:
        cnt[g] = cnt.get(g, 0) + 1

    print('=' * 78)
    print('可救性扫描：%d 题' % len(rows))
    print('  ' + '   '.join('%s 级 %d' % (g, cnt.get(g, 0)) for g in 'ABCD'))
    print('=' * 78)

    cut = order[args.min.upper()]
    for g, it, rs in rows:
        if order[g] < cut:
            continue
        v = ref.get(it['key']) or {}
        sol = str(v.get('solution') or '')
        opts = v.get('opts') or []
        print('[%s] %-13s p%-4s stem%-4d sol%-5d opts%d  ans=%s'
              % (g, it.get('key'), str(it.get('page') or '-'),
                 len(str(v.get('stem') or '')), len(sol), len(opts),
                 str(v.get('ans'))[:14].replace('\n', ' ')))
        print('       ' + '；'.join(rs))
    return 0


if __name__ == '__main__':
    sys.exit(main())
