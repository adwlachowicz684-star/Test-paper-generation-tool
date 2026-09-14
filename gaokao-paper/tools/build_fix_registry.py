#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""给「人工修正过」的题目打标记，便于后期复核。

    python3 tools/build_fix_registry.py

产出：
  1. bank.json 每题写入 fix 字段（结构化，机器可读）
        {"cls": "A", "level": "原书答案有误", "old": "...", "new": "...",
         "note": "...", "src": "M-T-xxx-Vn"}
  2. data/fix_registry.json          登记表（供脚本校验）
  3. 已修正题目清单.md                人工复核清单（按类别分组，含验证要点）

分类与《原书勘误表》一致，A/B/C/D 四类直接复用 gen_errata.py 的清单
（单一数据源，避免两处漂移）；E 类是本脚本新增：

  A 类  原书【答案】本身有误 → 已按正确答案录入
  B 类  PDF 提取丢符号 → 还原（原书无误）
  C 类  答案未改，仅详解/选项笔误
  D 类  存疑，按原书保留
  E 类  录入与排版修正（错码、命令粘连、$ 未闭合、字面 \n、区间括号等）
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

BANK = os.path.join(ROOT, 'data', 'bank.json')
REG = os.path.join(ROOT, 'data', 'fix_registry.json')
OUT_MD = os.path.join(ROOT, '已修正题目清单.md')

LEVEL = {
    'A': '原书答案有误·已更正',
    'B': '提取丢符号·已还原',
    'C': '详解/选项笔误·已修正',
    'D': '存疑·按原书保留',
    'E': '录入排版修正',
}

# ── E 类：录入与排版修正（人工维护） ──────────────────────────
# (题号, 修正内容)
E_ITEMS = [
    ('M-H0757', '详解与标答矛盾：详解算出 $|OG|_{\\min}=\\frac{5(\\sqrt2-1)}6$（对应选项 B），'
                '答案字段却存 D；根因是开根时把 $\\sqrt{25/18}$ 写成 $\\frac56$（漏 $\\sqrt2$ 因子）。'
                '已重写推导并补校验行，正确值 $\\frac{10-5\\sqrt2}6\\approx0.488155$'),
    ('M-H0578', '详解中间式 $\\frac{2a+2m}{2m}\\cdot\\frac22$ 是残留乱码，正确为 $\\frac{2a+m}{2m}$；结论 D 不受影响'),
    ('M-H0357', '批注写错：原批注称「严格推答案应为 B(610)」，实为 $F(16)=987$，**原书答案 C 本来就对**，已更正批注'),
    ('M-H0014', '选项 A 与 B 文本完全相同（原书印刷/排版问题），经推导答案正确，已批注'),
    ('M-H0042', '选项 B 与 C 文本完全相同，已批注'),
    ('M-H0350', '选项 B 与 C 文本完全相同，已批注'),
    ('M-H0540', '选项 A 与 B 文本完全相同；因原书根号丢失无法还原被吃掉的干扰项，**未臆造**，已批注'),
    ('M-H0466', '题干错码：`\\x07ngle`（控制字符 0x07 顶替了字母 a）→ $\\angle$'),
    ('M-H0049', '错码：`\\x0crac`（换页符 0x0C 顶替字母 f）→ $\\frac$'),
    ('M-H0142', '错码：`\\x0crac` → $\\frac$'),
    ('M-H0802', '答案区间括号错位：$(-3/2,\\,3]$ → $[-3/2,\\,3]$（$x=0$ 在定义域内、$-\\frac32$ 取得到，左端应闭）'),
    ('M-H0595', '端点存疑：严格应为开区间 $(1,\\sqrt2)$（渐近线上 $||PF_1|-|PF_2||<2a$ 取不到等号），'
                '但四个选项无精确匹配，保留 A 并强化批注'),
    ('M-H1341', '命令错误：$AB\\paralleq EC$ → $AB\\parallel EC$（3 处；$\\paralleq$ 不是合法命令）'),
    ('M-H0069', '详解 $f\\\'(t)$ → $f\'(t)$（$\\\'$ 是重音命令，不是撇号）'),
    ('M-H0652', '$\\text{$D$ 到平面 }$ 在 $\\text{}$ 内嵌了 $ → 改为 $\\text{D 到平面 }$'),
    ('M-H1180', '$$ 未正确闭合导致中文被吞进公式（2 处），已改为正确的行间/行内配对'),
    ('M-H1181', '$$ 误用（应为行内 $）导致 3 段中文进入数学模式，已修正'),
    ('M-H1182', '$$ 未闭合，下一处 $$ 错位充当了闭合符，已修正'),
    ('M-H1184', '$$ 未闭合 3 处，导致中文段落被吞进公式，已修正'),
    ('M-H1257', '$$ 未闭合，连锁导致后续两段中文进入数学模式，已修正'),
    ('M-H1302', '字面 $\\backslash n$ 未还原为真实换行，已修正'),
] + [('M-H%04d' % i, '字面 $\\backslash n$ 未还原为真实换行（该批目录入时的字符串拼接残留），已修正')
     for i in range(336, 344)]

# 批量命令粘连/罗马数字修复：题号已不可精确追溯，登记说明
E_BATCH_NOTE = (
    '另有两批**批量符号修复**（约 40 题）：① 命令与变量名粘连，如 '
    '$\\leqslanta$→$\\leqslant a$（18 处，在题干）、$\\gea/\\geb/\\gec/\\gep$、'
    '$\\paralleleq$→$\\parallel$、$\\qquady$、$\\becausef$/$\\thereforef$ 等；'
    '② 不存在的命令 $\\RomanNumeral{1..5}$（17 处）→ 罗马数字 Ⅰ–Ⅴ。'
    '当时未逐题留痕，题号已不可考；现已通过 `tools/lint_math.py` 全库校验确认修复到位。'
)


def load_errata_classes():
    """从 gen_errata.py 复用 A/B/C/D 四类清单，避免两处维护。"""
    import gen_errata
    out = {}
    for qid, src, old, new, reason in gen_errata.A_MANUAL:
        out[qid] = {'cls': 'A', 'old': old, 'new': new, 'note': reason, 'src': src}
    # 优先级：A（改答案）> D（存疑待复核）> C（详解笔误）> B（符号还原，量大）
    # 用 setdefault 实现：先加载的类别不被后面的区间清单覆盖。
    # 例：M-H0220 既在 A_MANUAL 又落在 B 的 range(201,217)；
    #     M-H0252 既是 D 类又落在 B 的 range(250,262)。
    for qid, keys in (('D', gen_errata.D_KEYS), ('C', gen_errata.C_KEYS),
                      ('B', gen_errata.B_KEYS)):
        for x in keys:
            # setdefault：A 类（答案更正）优先，不被 B/C/D 的区间清单覆盖。
            # 例：M-H0220 既在 A_MANUAL，又落在 B_KEYS 的 range(201,217) 里。
            out.setdefault(x, {'cls': qid, 'old': '', 'new': '',
                               'note': '', 'src': ''})
    return out


def main():
    bank = json.load(open(BANK, encoding='utf-8'))
    idx = {q['id']: q for q in bank}

    reg = load_errata_classes()
    for qid, note in E_ITEMS:
        reg.setdefault(qid, {'cls': 'E', 'old': '', 'new': '', 'note': note, 'src': ''})

    # 写入 bank
    n = 0
    miss = []
    for qid, info in reg.items():
        q = idx.get(qid)
        if not q:
            miss.append(qid)
            continue
        src = info.get('src') or (q.get('src') or '').split('·')[-1].strip()
        q['fix'] = {
            'cls': info['cls'],
            'level': LEVEL[info['cls']],
            'old': info.get('old', ''),
            'new': info.get('new', ''),
            'note': info.get('note', ''),
            'src': src,
        }
        n += 1

    json.dump(bank, open(BANK, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    json.dump({k: v for k, v in reg.items() if k in idx},
              open(REG, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

    # 生成人工复核清单
    groups = {}
    for qid, info in reg.items():
        if qid not in idx:
            continue
        groups.setdefault(info['cls'], []).append(qid)

    L = ['# 已修正题目清单（人工复核用）', '',
         '本清单由 `tools/build_fix_registry.py` 生成。被人工改动过的题目在 `bank.json` 里都带 '
         '`fix` 字段（`cls` 为类别、`old`/`new` 为改动前后、`note` 为依据），'
         '可按 `fix.cls` 检索复核。',
         '',
         '> 与《原书勘误表》同源：A/B/C/D 四类直接复用 `gen_errata.py` 的清单；'
         'E 类是录入与排版修正。',
         '']
    total = 0
    for cls in 'ABCDE':
        ids = sorted(groups.get(cls, []))
        if not ids:
            continue
        total += len(ids)
        L.append('## %s 类：%s（%d 题）' % (cls, LEVEL[cls], len(ids)))
        L.append('')
        if cls == 'A':
            L.append('**复核要点**：这类改动了原书答案，逐题核对 `fix.note` 里的依据是否成立，'
                     '必要时用数值验证复算。')
        elif cls == 'B':
            L.append('**复核要点**：原书无误，改动的是 PDF 提取丢掉的符号。'
                     '核对还原后的式子能否复现原书答案与详解中间量。')
        elif cls == 'C':
            L.append('**复核要点**：答案未动，只修了推导链。核对修正后的详解能否推出原答案。')
        elif cls == 'D':
            L.append('**复核要点**：证据不足以推翻原书，按原书保留。'
                     '复核时重点看 `review` 里记的疑点能否定论。')
        else:
            L.append('**复核要点**：多为错码、命令错误、`$` 未闭合等排版问题。'
                     '已通过 `tools/lint_math.py` 全库校验；改答案的（M-H0757、M-H0802）需重点复算。')
            L.append('')
            L.append('> ' + E_BATCH_NOTE)
        L.append('')
        L.append('| 题号 | 来源 | 说明 |')
        L.append('|---|---|---|')
        for qid in ids:
            info = reg[qid]
            src = info.get('src') or (idx[qid].get('src') or '').split('·')[-1].strip() or '—'
            note = (info.get('note') or '').replace('\n', ' ')
            if not note:
                note = '（详见该题 `review` 字段）'
            if len(note) > 150:
                note = note[:150] + '…'
            L.append('| %s | %s | %s |' % (qid, src, note))
        L.append('')

    L.append('---')
    L.append('')
    L.append('**合计 %d 题**（题库共 %d 题，占 %.1f%%）。' % (total, len(bank), 100.0 * total / len(bank)))
    L.append('')
    L.append('复核时可用：`python3 tools/lint_math.py`（公式/符号校验，应无【严重】项）。')

    open(OUT_MD, 'w', encoding='utf-8').write('\n'.join(L) + '\n')

    print('  已标记 %d 题（题库 %d 题）' % (n, len(bank)))
    if miss:
        print('  ! 以下题号不在题库，已跳过：%s' % ', '.join(miss))
    print('  登记表 → %s' % REG)
    print('  复核清单 → %s' % OUT_MD)
    return 0


if __name__ == '__main__':
    sys.exit(main())
