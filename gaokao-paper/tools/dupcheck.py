# -*- coding: utf-8 -*-
r"""全局重复题检测：一次扫全库，输出候选供人工审核。

    python3 tools/dupcheck.py                  # 扫描，生成候选清单
    python3 tools/dupcheck.py --threshold 0.80 # 调整阈值（默认 0.75）
    python3 tools/dupcheck.py --only bank      # 只扫已录题库内部
    python3 tools/dupcheck.py --apply          # 按人工审核结果写回

## 为什么是全局而不是每题跑一遍

每录一道题跑一次全库比对 = O(n²) 次 I/O 与解析，
而且**新题与旧题重复时，旧题已经被录进去了**，事后才发现就得返工。
全局一次扫完，重复关系一次看清，还能顺带发现「两道已录题其实同题」。

## 算法选型：级联，从便宜到贵

这是 record-linkage / 去重领域的标准做法，按代价递增分层：

    C(精确哈希) << C(分块) << C(n-gram 相似度) << C(语义向量)

| 层 | 方法 | 作用 |
|---|---|---|
| 1 | 精确签名（现有 make_plan） | 抓完全一样的，零成本 |
| 2 | **Blocking 分块** | 按 (题型, 答案) 分桶，只比桶内 |
| 3 | **长度过滤** | 长度差超 40% 直接跳过 |
| 4 | **字符 3-gram + Jaccard** | 真正算相似度 |

**没有用 MinHash/LSH** —— 那是万亿级语料才必需的。
本库约 1600 题，分块后仅 6 万对候选，暴力 Jaccard 几秒跑完。
上 MinHash 反而引入近似误差和调参负担，得不偿失。

## 四个匹配通道（对应「类型、答案、关键词、公式主要文本」）

| 通道 | 内容 | 权重 |
|---|---|---|
| `txt` | 公式拍平后的字符 3-gram | 0.40 |
| `num` | 数字集合（数学题的强特征） | 0.30 |
| `key` | 关键词：变量名 + 函数名 | 0.15 |
| `opt` | 选项集合（仅选择题） | 0.15 |

**缺失的通道不参与加权**（权重重新归一化）——
已录题有 LaTeX、素材题只有破碎文本，公式通道对后者为空，
若按 0 分会误判为不重复，必须剔除后归一化。

## 关键：公式「拍平」

两边形态不同，必须对齐后才能比：

```
bank    $a=6\ln\pi,\ b=3\pi\ln2$   →  拍平 →  a=6lnπ,b=3πln2
ref     a = 6lnπ，b = 3πln2         →  拍平 →  a=6lnπ,b=3πln2
```

拍平规则：去 `$`、`\left`、`\right`、花括号、空白；
常见命令**还原为字符**（`\pi`→π、`\ln`→ln），其余命令删除但保留参数。
见 `CMD` 表 —— 换教辅时若出现新符号，往这里加。

## 人工审核（不可省）

脚本只给候选，不自动判定。三档：

- **高 ≥0.90**　几乎必是同题，但也可能是「换了数字」的变式，仍需看一眼
- **中 0.75~0.90**　需要人工判断
- **低 0.60~0.75**　仅列出备查

审核方式：在生成的 json 里给每对标 `"verdict": "dup"` / `"not"`，
再跑 `--apply` 写回 `data/skipped.json`。
"""
import argparse
import json
import os
import re
import sys
from collections import defaultdict
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')
sys.path.insert(0, os.path.join(ROOT, 'py'))

REF = os.path.join(ROOT, 'data', 'ref_bank.json')
BANK = os.path.join(ROOT, 'data', 'bank.json')
OUT_JSON = os.path.join(HERE, '_dup_candidates.json')
OUT_MD = os.path.join(ROOT, '重复题候选清单.md')

# ---------------- 公式拍平 ----------------

# 有语义的命令 → 还原成字符。换教辅时按需增补。
CMD = {
    'pi': 'π', 'alpha': 'α', 'beta': 'β', 'gamma': 'γ', 'theta': 'θ',
    'ln': 'ln', 'log': 'log', 'lg': 'lg', 'sin': 'sin', 'cos': 'cos',
    'tan': 'tan', 'cot': 'cot', 'sec': 'sec', 'csc': 'csc',
    'cdot': '·', 'times': '×', 'div': '÷', 'pm': '±',
    'le': '≤', 'leq': '≤', 'ge': '≥', 'geq': '≥', 'ne': '≠', 'neq': '≠',
    'approx': '≈', 'equiv': '≡', 'infty': '∞', 'in': '∈',
    'cup': '∪', 'cap': '∩', 'subset': '⊂', 'subseteq': '⊆',
    'forall': '∀', 'exists': '∃', 'Rightarrow': '⇒', 'rightarrow': '→',
    'sqrt': '', 'frac': '', 'dfrac': '', 'tfrac': '', 'binom': '',
    'mathrm': '', 'mathbf': '', 'text': '', 'mbox': '', 'rm': '',
    'left': '', 'right': '', 'middle': '', 'big': '', 'Big': '',
    'quad': '', 'qquad': '', 'hspace': '', 'vspace': '', ',': '', ';': '',
    '!': '', 'limits': '', 'displaystyle': '', 'nonumber': '',
}


def flatten(s, expand_cmd=True):
    r"""把含 LaTeX 的文本拍平成裸字符流。

    $a=6\ln\pi$  →  a=6lnπ
    去掉 $、花括号、空白；有语义的命令还原为字符，其余删除（保留参数）。
    """
    s = s or ''
    s = re.sub(r'\$([^$]*)\$', lambda m: m.group(1), s)   # 脱 $ 外壳
    if expand_cmd:
        s = re.sub(r'\\([a-zA-Z]+|.)',
                   lambda m: CMD.get(m.group(1), ''), s)
    else:
        s = re.sub(r'\\[a-zA-Z]+', '', s)
    s = s.replace('\\', '').replace('{', '').replace('}', '')
    return re.sub(r'\s+', '', s)


def src_key(s):
    """从 src 字段里抽出题号，如 '… · M-T-038-V1' → 'M-T-038-V1'。

    **必须用正则，不能用 split('·')** —— 早期录入的题 src 写作
    `2024热点题型归纳 M-T-009-V4`，没有 `·` 分隔符，
    split 会返回整串，导致「已录题 ⟷ 素材源」的配对排除不掉。
    """
    m = re.search(r'(M-T-\d+-(?:E\d+|V\d+))', s or '')
    return m.group(1) if m else ''


def trigrams(s):
    return {s[i:i + 3] for i in range(max(0, len(s) - 2))} or {s}


def numset(s):
    """数字集合。数学题换数字即换题，这是最强的判重特征。"""
    return set(re.findall(r'\d+\.?\d*', s or ''))


def keyset(s):
    """关键词：单字母变量 + 函数名。"""
    fns = set(re.findall(r'\b(?:ln|log|lg|sin|cos|tan|e)\b', s or ''))
    return fns | set(re.findall(r'(?<![a-zA-Z])[a-df-hm-pr-txyz](?![a-zA-Z])', s or ''))


def jac(a, b):
    if not a or not b:
        return None          # 通道缺失，返回 None 表示不参与
    return len(a & b) / len(a | b)


# ---------------- 载入 ----------------

def load_items(only=None):
    """统一成 [{id, src, type, ans, text, opts}]，ref 与 bank 同构。"""
    items = []
    if only in (None, 'bank'):
        for q in json.load(open(BANK, encoding='utf-8')):
            stem = q.get('stem_text') or q.get('stem') or ''
            opts = [str(o[1]) for o in (q.get('opts') or [])
                    if isinstance(o, (list, tuple)) and len(o) > 1]
            items.append({
                'id': q['id'], 'lib': 'bank', 'type': q.get('type') or '?',
                'ans': (q.get('answer') or '').strip(), 'stem': stem,
                'flat': flatten(stem), 'opts': [flatten(o) for o in opts],
                'src': src_key(q.get('src')),
            })
    if only in (None, 'ref'):
        ref = json.load(open(REF, encoding='utf-8'))
        for k, v in ref.items():
            stem = v.get('stem') or ''
            items.append({
                'id': k, 'lib': 'ref', 'type': v.get('kind') or '例题',
                'ans': (v.get('ans') or '').strip(), 'stem': stem,
                'flat': flatten(stem), 'opts': [flatten(o) for o in (v.get('opts') or [])],
                'src': k,
            })
    for it in items:
        it['_tri'] = trigrams(it['flat'])
        it['_num'] = numset(it['flat'])
        it['_key'] = keyset(it['flat'])
        it['_opt'] = set(it['opts'])
        # 两库题型字段不同域（bank: 选择/填空/解答，ref: 典例/变式），
        # 无法直接用作分块键。用「有无选项」统一 —— ref 的 opts 数只有 4 或 0，
        # 恰好对应选择 / 非选择，判据可靠。
        it['_qt'] = '选择' if len(it['opts']) >= 2 else '非选择'
    return items


# ---------------- 打分 ----------------

W = {'txt': 0.40, 'num': 0.30, 'key': 0.15, 'opt': 0.15}


def score(a, b):
    """多通道加权；缺失通道剔除后重新归一化。"""
    ch = {
        'txt': jac(a['_tri'], b['_tri']),
        'num': jac(a['_num'], b['_num']),
        'key': jac(a['_key'], b['_key']),
        'opt': jac(a['_opt'], b['_opt']),
    }
    live = {k: v for k, v in ch.items() if v is not None}
    if not live:
        return 0.0, {}
    tot = sum(W[k] for k in live)
    return sum(W[k] * v for k, v in live.items()) / tot, ch


def scan(only=None, threshold=0.60, length_ratio=0.6):
    items = load_items(only)
    by_id = {it['id']: it for it in items}

    seen_pair = set()
    pairs = []

    def compare(grp):
        """桶内两两比，带长度过滤。"""
        grp = sorted(grp, key=lambda x: len(x['flat']))
        n = len(grp)
        for i in range(n):
            a = grp[i]
            la = len(a['flat']) or 1
            for j in range(i + 1, n):
                b = grp[j]
                lb = len(b['flat']) or 1
                # 已按长度升序，b 只会更长：lb/la 递增，la/lb 递减
                if lb / la < length_ratio:
                    continue
                if la / lb < length_ratio:
                    break
                key = (a['id'], b['id'])
                if key in seen_pair:
                    continue
                # 排除「已录题 ⟷ 它的素材源」——那是正常的录入对应关系，
                # 不是重复。不排除的话几百对全是噪音，人工根本看不过来。
                if a['src'] == b['id'] or b['src'] == a['id']:
                    continue
                s, ch = score(a, b)
                if s >= threshold:
                    seen_pair.add(key)
                    pairs.append((s, a['id'], b['id'], ch))

    # ── 层2a：主分块，按 (统一题型, 答案) ──
    # 用 _qt 而不是 type：两库题型字段不同域，直接分块会导致跨库对永不同桶。
    buckets = defaultdict(list)
    for it in items:
        buckets[(it['_qt'], it['ans'])].append(it)
    for grp in buckets.values():
        if len(grp) >= 2:
            compare(grp)

    # ── 层2b：兜底，数字集合完全相同才比 ──
    # 抓「选项重排导致答案字母不同」的情况 —— 主分块按答案分桶会漏掉。
    # 数字是数学题的强特征：同题必同数字，不同题极少撞全。
    nb = defaultdict(list)
    for it in items:
        if len(it['_num']) >= 3:          # 少于 3 个数字的签名太泛，跳过
            nb[frozenset(it['_num'])].append(it)
    for grp in nb.values():
        if 2 <= len(grp) <= 40:           # 巨型桶说明签名无区分度，跳过
            compare(grp)

    pairs.sort(reverse=True, key=lambda p: p[0])
    return by_id, pairs


def band(s):
    if s >= 0.90:
        return '高'
    if s >= 0.75:
        return '中'
    return '低'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--threshold', type=float, default=0.60)
    ap.add_argument('--only', choices=['bank', 'ref'], default=None)
    ap.add_argument('--apply', action='store_true', help='按审核结果写回')
    a = ap.parse_args()

    if a.apply:
        return apply_verdicts()

    items_by_id, pairs = scan(a.only, a.threshold)
    n = len(items_by_id)
    print('  扫描 %d 题 → 候选 %d 对' % (n, len(pairs)))

    tiers = defaultdict(int)
    for s, _, _, _ in pairs:
        tiers[band(s)] += 1
    print('    高(≥0.90) %d   中(0.75~0.90) %d   低(0.60~0.75) %d'
          % (tiers['高'], tiers['中'], tiers['低']))

    # ---- 机器可读 ----
    recs = []
    for s, i1, i2, ch in pairs:
        recs.append({
            'score': round(s, 4), 'band': band(s),
            'a': i1, 'b': i2,
            'a_lib': items_by_id[i1]['lib'], 'b_lib': items_by_id[i2]['lib'],
            'detail': {k: (round(v, 3) if v is not None else None)
                       for k, v in ch.items()},
            'a_text': items_by_id[i1]['flat'][:70],
            'b_text': items_by_id[i2]['flat'][:70],
            'a_src': items_by_id[i1]['src'], 'b_src': items_by_id[i2]['src'],
            'verdict': '',      # 人工填 dup / not
        })
    json.dump(recs, open(OUT_JSON, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)

    # ---- 人工审核清单 ----
    L = ['# 重复题候选清单', '',
         '由 `tools/dupcheck.py` 生成，%s' % datetime.now().strftime('%Y-%m-%d %H:%M'),
         '',
         '**脚本只给候选，不自动判定**，需要人工逐条看后在下方的 json 里标记。',
         '',
         '| 档 | 分数 | 说明 |', '|---|---|---|',
         '| 高 | ≥0.90 | 几乎必是同题，但仍可能是「换了数字」的变式 |',
         '| 中 | 0.75~0.90 | 需要人工判断 |',
         '| 低 | 0.60~0.75 | 仅备查 |', '']
    for t in ('高', '中', '低'):
        sub = [r for r in recs if r['band'] == t]
        if not sub:
            continue
        L += ['## %s疑似（%d 对）' % (t, len(sub)), '']
        for r in sub:
            d = r['detail']
            det = '  '.join('%s=%.2f' % (k, v) for k, v in d.items()
                            if v is not None)
            L += ['### %.3f　%s ⟷ %s' % (r['score'], r['a'], r['b'])]
            L += ['- 分通道：%s' % det]
            L += ['- A（%s）：`%s`' % (r['a_lib'], r['a_text'])]
            L += ['- B（%s）：`%s`' % (r['b_lib'], r['b_text'])]
            L += ['']
    L += ['---', '',
          '## 审核方式', '',
          '打开 `tools/_dup_candidates.json`，给每对填 `"verdict"`：',
          '',
          '- `"dup"`　确认同题，保留 `a`、把 `b` 记为重复',
          '- `"not"`　不是同题，后续不再报',
          '- 留空　　还没看',
          '',
          '填完执行：', '', '```bash',
          'python3 tools/dupcheck.py --apply', '```']
    open(OUT_MD, 'w', encoding='utf-8').write('\n'.join(L))

    print('  已生成 %s' % os.path.basename(OUT_MD))
    print('  已生成 tools/_dup_candidates.json（填 verdict 后跑 --apply）')
    if pairs:
        print()
        print('  分数最高的 5 对：')
        for s, i1, i2, ch in pairs[:5]:
            print('    %.3f  %s ⟷ %s' % (s, i1, i2))
    return 0


def apply_verdicts():
    r"""按人工审核结果写回 data/skipped.json。

    **保留谁、标记谁** 不能简单按 a/b 顺序，要看库别：
      - 一边已录(bank)、一边素材(ref) → 保留已录的，把素材标记为重复
        （候选里 a、b 顺序由分数排序决定，不能直接信）
      - 两边都是素材 → 保留 a，标记 b
      - 两边都已录 → 不自动处理，只告警
        （要从 bank.json 里删题，影响面大，必须人工决定）
    """
    if not os.path.exists(OUT_JSON):
        print('  没有候选文件，先跑一遍扫描')
        return 1
    recs = json.load(open(OUT_JSON, encoding='utf-8'))
    dups = [r for r in recs if r.get('verdict') == 'dup']
    if not dups:
        print('  没有标记为 dup 的记录（在 %s 里填 verdict）'
              % os.path.basename(OUT_JSON))
        return 1

    # 精确判重（make_plan 按「去公式题干+答案」签名）已覆盖的，不必再写：
    # 那边已经算作「重复跳过」了，重复记录会干扰状态统计。
    ref0 = json.load(open(REF, encoding='utf-8'))

    def _norm(t):
        t = re.sub(r'\$[^$]*\$', '#', t or '')
        return re.sub(r'[^一-鿿0-9a-zA-Z]', '', t)[:50]

    sig = defaultdict(list)
    for k, v in ref0.items():
        sig[(_norm(v.get('stem')), (v.get('ans') or '').strip())].append(k)
    exact_dup = set()
    for ks in sig.values():
        if len(ks) > 1:
            exact_dup.update(ks[1:])

    sk = os.path.join(ROOT, 'data', 'skipped.json')
    data = json.load(open(sk, encoding='utf-8'))
    items = data.setdefault('items', [])
    have = {it.get('key') for it in items}

    ref = json.load(open(REF, encoding='utf-8'))
    n, warn, already = 0, [], 0
    for r in dups:
        a_l, b_l = r['a_lib'], r['b_lib']
        if a_l == 'bank' and b_l == 'bank':
            warn.append('%s ⟷ %s（两边都已录入，需人工决定删哪题）'
                        % (r['a'], r['b']))
            continue
        # 确定保留者 / 被标记者
        if a_l == 'bank':
            keep, drop = r['a'], r['b']
        elif b_l == 'bank':
            keep, drop = r['b'], r['a']
        else:                       # 都是素材，按 a、b 顺序
            keep, drop = r['a'], r['b']
        if drop in have:
            continue
        if drop in exact_dup:
            already += 1      # 精确判重已算作重复，跳过
            continue
        v = ref.get(drop, {})
        items.append({
            'key': drop,
            'page': 0,
            'topic': (drop.rsplit('-', 1)[0] if '-' in drop else ''),
            'topic_name': v.get('topic', ''),
            'kp1': '', 'kp2': '',
            'kind': v.get('kind', ''),
            'ref_answer': v.get('ans', ''),
            'reason': '重复',
            'note': '与 %s 同题（dupcheck %.3f），已录 %s'
                    % (keep, r['score'], keep),
            'stem_raw': (v.get('stem') or '')[:200],
            'has_solution': bool(v.get('solution')),
        })
        have.add(drop)
        n += 1

    json.dump(data, open(sk, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print('  已把 %d 条标记为重复，写入 data/skipped.json' % n)
    if already:
        print('  · %d 条已由精确判重覆盖，未重复写入' % already)
    for w in warn:
        print('  ⚠ 跳过：%s' % w)
    print('  重跑 python3 tools/make_plan.py 刷新清单')
    return 0


if __name__ == '__main__':
    sys.exit(main())
