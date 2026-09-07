# -*- coding: utf-8 -*-
r"""生成《教辅录入任务计划清单》xlsx + markdown（带真实进度）。

    python3 tools/make_plan.py

**为什么必须按真实进度生成**

初版把所有 1395 道题都列成「待录入」，而实际上已录 100+ 道。
清单与现状不符的后果是没法用它跟踪进度——每批都显示"没做"，
无法区分"还没轮到"和"做完了但没更新"。

现在的状态来自三处真实数据，不是推算：
  - 已录入  `skipped.recorded_keys()`（读 bank.json 里的 src 字段）
  - 重复    按 (去公式题干, 答案) 判重，同组内第 2 条起算重复
  - 跳过    data/skipped.json
剩余即为待录入，**只有待录入的题参与分批**。

重复与跳过有 5 个 key 重叠（既是重复、又记进了跳过清单），
统计时按「重复 > 跳过」去重，避免重复计数。
"""
import sys, os, json, re
from collections import defaultdict, Counter
sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '..', 'py'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# ---------------- 载入真实状态 ----------------
# 不用 tools/_plan2.json —— 那是第 3 批时的快照，只有 1313 题，
# 缺 82 题（含第 1 批录入的），会让"已录"数少算 59 道。
# 改为从 ref_bank + kp_catalog.TOPICS 实时构建，重跑即最新。
import kp_catalog as K

ref = json.load(open('data/ref_bank.json', encoding='utf-8'))
try:
    PAGES = json.load(open('tools/_toc_pages.json', encoding='utf-8'))
except Exception:
    PAGES = {}

from old_gaokao import old_keys, old_topics
OLD_KEYS = old_keys(ref)
OLD_REASON = old_topics()

items = []
for k in sorted(ref):
    v = ref[k]
    tid = v.get('topic') or k.rsplit('-', 1)[0]
    info = K.TOPICS.get(tid, {})
    l1, l2 = (info.get('primary') or ('?', '?'))
    items.append(dict(
        key=k, topic=tid, tname=info.get('name', ''),
        l1=l1, l2=l2, kind=v.get('kind', ''),
        page=PAGES.get(tid, ''), ans=(v.get('ans') or '').strip(),
        has_sol=bool((v.get('solution') or '').strip()),
        stem=(v.get('stem') or '').replace('\n', ' ')[:120],
    ))

# 补录题：原 PDF 里答案写在详解末尾、无【答案】标记，被提取器过滤，
# 后据详解补录。它们的 key 不在 ref_bank 里，但确实已入库。
# 不纳入统计的话，清单"已录 171"与题库 184 对不上，
# 且这些题在明细里完全查不到。
bank = json.load(open('data/bank.json', encoding='utf-8'))
EXTRA = []
BANK_KEYS = set()
for q in bank:
    m = re.search(r'(M-T-\d+-(?:E\d+|V\d+))', q.get('src') or '')
    if not m:
        continue
    k = m.group(1)
    BANK_KEYS.add(k)
    if k in ref:
        continue
    tid = k.rsplit('-', 1)[0]
    info = K.TOPICS.get(tid, {})
    l1, l2 = (info.get('primary') or ('?', '?'))
    EXTRA.append(dict(
        key=k, topic=tid, tname=info.get('name', ''),
        l1=l1, l2=l2, kind='补录', page=PAGES.get(tid, ''),
        ans=(q.get('answer') or '').strip(), has_sol=True,
        stem=(q.get('stem_text') or '').replace('\n', ' ')[:120],
    ))
items.extend(EXTRA)

groups = {}
for it in items:
    groups.setdefault((it['l1'], it['l2'], it['topic']), []).append(it)
from skipped import recorded_keys
DONE = recorded_keys(ref)
SK = json.load(open('data/skipped.json', encoding='utf-8'))['items']
SKIPPED = set(i['key'] for i in SK)
SK_MAP = {i['key']: i for i in SK}


def norm(t):
    t = re.sub(r'\$[^$]*\$', '#', t or '')
    return re.sub(r'[^一-鿿0-9a-zA-Z]', '', t)[:50]


seen = defaultdict(list)
for k in sorted(ref):
    seen[(norm(ref[k].get('stem')), (ref[k].get('ans') or '').strip())].append(k)
DUP_REASON = {}
for sig, ks in seen.items():
    if len(ks) > 1:
        for k in ks[1:]:
            DUP_REASON[k] = '与 %s 同题' % ks[0]
DUP = set(DUP_REASON)

# 状态判定优先级：已录 > 不录(老高考) > 重复 > 跳过 > 待录
# （重复与跳过有 5 个 key 重叠，按此顺序只算一次）
def status_of(key):
    # 补录题的 key 不在 ref_bank 里（提取器漏了），recorded_keys()
    # 也就认不出来。直接用 bank.json 扫出来的 BANK_KEYS 判定，
    # 否则这 13 题会被当成"待录入"，待录数虚高。
    if key in BANK_KEYS:
        if key not in ref:
            return '已录入(补录)', '原PDF无【答案】标记，据详解补录'
        return '已录入', ''
    if key in OLD_KEYS:
        return '不录(老高考)', OLD_KEYS[key]
    if key in DUP:
        return '重复跳过', DUP_REASON.get(key, '')
    if key in SKIPPED:
        return '人工跳过', SK_MAP[key].get('reason', '')
    return '待录入', ''


for it in items:
    st, note = status_of(it['key'])
    it['status'] = st
    it['status_note'] = note

STAT = Counter(it['status'] for it in items)
assert sum(STAT.values()) == len(items), '状态计数与总数不符'

TODO = [it for it in items if it['status'] == '待录入']
todo_keys = set(it['key'] for it in TODO)
# 只保留有待录题的分组参与分批
groups_todo = {}
for kk, lst in groups.items():
    sub = [x for x in lst if x['key'] in todo_keys]
    if sub:
        groups_todo[kk] = sub

# ---------------- 阶段与分批 ----------------
STAGE = [
    ('函数与导数', 'A', '分值最高，压轴常客'),
    ('三角函数',   'A', '选填+大题，稳拿分模块'),
    ('解析几何',   'A', '压轴大题，计算量大'),
    ('立体几何',   'A', '选填+大题，建系为主'),
    ('数列',       'B', '递推+求和，套路明确'),
    ('概率统计',   'B', '大题必考，含马尔科夫链'),
    ('平面向量',   'B', '小题为主，技巧性强'),
    ('计数原理',   'B', '小题，模型化'),
    ('不等式',     'C', '基本不等式；选讲为老高考内容'),
]
RANK = {n: i for i, (n, _, _) in enumerate(STAGE)}
OLD = {'不等式选讲'}


def ordk(kk):
    l1, l2, t = kk
    return (1 if l2 in OLD else 0, RANK.get(l1, 99), l2, t)


order = [k for k in sorted(groups_todo, key=ordk)]

TARGET, HARD = 18, 24
batches, cur, n = [], [], 0
for kk in order:
    c = len(groups_todo[kk])
    if cur and (kk[1] in OLD) != (cur[-1][1] in OLD):
        batches.append(cur); cur, n = [], 0
    if cur and n + c > HARD:
        batches.append(cur); cur, n = [], 0
    cur.append(kk); n += c
    if n >= TARGET:
        batches.append(cur); cur, n = [], 0
if cur:
    batches.append(cur)

# ---------------- 样式 ----------------
wb = Workbook()
HDR = Font(bold=True, color='FFFFFF', size=11)
FILL = PatternFill('solid', fgColor='2F5597')
SUB = PatternFill('solid', fgColor='D9E2F3')
OLD_F = PatternFill('solid', fgColor='FFF2CC')
DONE_F = PatternFill('solid', fgColor='E2EFDA')   # 浅绿 已录入
SKIP_F = PatternFill('solid', fgColor='FCE4D6')   # 浅橙 跳过
BD = Border(*[Side('thin', color='BFBFBF')] * 4)


def head(ws, cols, widths):
    ws.append(cols)
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
        c = ws.cell(1, i); c.font = HDR; c.fill = FILL
        c.alignment = Alignment('center', 'center')
    ws.freeze_panes = 'A2'


def fill_by_status(row, start=0):
    v = row[start].value if len(row) > start else None
    f = {'已录入': DONE_F, '已录入(补录)': DONE_F,
         '重复跳过': SKIP_F, '人工跳过': SKIP_F,
         '不录(老高考)': OLD_F, '待录入': None}.get(v)
    if f:
        for c in row:
            c.fill = f


# ---- Sheet0 进度总览 ----
ws0 = wb.active; ws0.title = '进度总览'
head(ws0, ['项目', '题数', '说明'], [16, 10, 62])
ws0.append(['教辅总题数', len(items), 'ref_bank.json 中提取的题目总数'])
ws0.append(['已录入', STAT.get('已录入', 0), '已写入 bank.json，可组卷使用'])
ws0.append(['其中补录', STAT.get('已录入(补录)', 0),
            '原PDF无【答案】标记，据详解补录（不在 ref_bank）'])
ws0.append(['不录(老高考)', STAT.get('不录(老高考)', 0),
            '柯西/绝对值不等式、线性规划，新高考不考'])
ws0.append(['重复跳过', STAT.get('重复跳过', 0),
            '与前面某题同题干同答案，避免重复刷'])
ws0.append(['人工跳过', STAT.get('人工跳过', 0),
            '待人工裁定，见「跳过清单」表'])
ws0.append(['待录入', STAT.get('待录入', 0), '参与本计划分批'])
ws0.append(['合计', len(items), ''])
ws0.append([])
ws0.append(['计划批次数', len(batches), '每批约 18 题，尽量不切断题型'])
ws0.append(['已录题型数', len(DONE and set(k.rsplit('-', 1)[0] for k in DONE)),
            '涉及多少个 M-T 题型'])
ws0.append(['不录题型数', len(OLD_REASON),
            '老高考专属题型，整题型排除'])
for row in ws0.iter_rows(min_row=2):
    for c in row:
        c.border = BD
for i, row in enumerate(ws0.iter_rows(min_row=2), start=2):
    if row[0].value in ('合计', '待录入'):
        for c in row:
            c.font = Font(bold=True); c.fill = SUB

# ---- Sheet1 批次计划（只含待录入）----
ws = wb.create_sheet('批次计划')
head(ws, ['批次', '阶段', '优先级', '题型范围', '题数', '页码', '状态',
          '录入日期', '备注'], [7, 12, 8, 22, 7, 12, 10, 12, 34])
def _tid(t):
    return int(t.replace('M-T-', ''))


rows, bidx = [], 0
for b in batches:
    bidx += 1
    ts = sorted((k[2] for k in b), key=_tid)   # 按编号排，别按知识点顺序显示
    l1 = b[0][0]
    cnt = sum(len(groups_todo[k]) for k in b)
    nums = [_tid(t) for t in ts]
    # 编号连续才显示成区间，否则显示"共 N 个题型"——
    # 显示成 T053~T162 会让人以为中间漏了上百个题型
    if len(nums) == 1:
        rng = 'T%03d' % nums[0]
    elif nums == list(range(nums[0], nums[-1] + 1)):
        rng = 'T%03d~T%03d' % (nums[0], nums[-1])
    else:
        rng = 'T%03d 等 %d 个题型' % (nums[0], len(nums))
    pgs = sorted({int(groups_todo[k][0]['page']) for k in b
                  if str(groups_todo[k][0].get('page') or '').isdigit()})
    pgt = ('p%d~p%d' % (pgs[0], pgs[-1])) if pgs else '—'
    pr = dict((n, p) for n, p, _ in STAGE).get(l1, '—')
    note = next((nt for n, _, nt in STAGE if n == l1), '')
    if any(k[1] in OLD for k in b):
        pr, note = '可选', '老高考内容，新高考不考，建议跳过'
    rows.append([('第%02d批' % bidx), l1, pr, rng, cnt, pgt,
                 '待录入', '', note])
for r_ in rows:
    ws.append(r_)
for row in ws.iter_rows(min_row=2):
    for c in row:
        c.border = BD; c.alignment = Alignment('center', 'center', wrap_text=True)
    if row[8].value and '老高考' in str(row[8].value):
        for c in row:
            c.fill = OLD_F
ws.auto_filter.ref = 'A1:I%d' % (len(rows) + 1)

# ---- Sheet2 题目明细（全部，带状态）----
ws2 = wb.create_sheet('题目明细')
head(ws2, ['状态', '批次', '题型ID', '题型名', '大知识点', '小知识点', '类型',
           'ref_bank key', '页码', '参考答案', '有详解', '题干摘录', '备注'],
     [10, 7, 9, 24, 11, 15, 6, 15, 7, 10, 7, 52, 30])
k2b = {}
for i, b in enumerate(batches, 1):
    for kk in b:
        for it in groups_todo[kk]:
            k2b[it['key']] = i
for it in items:
    ws2.append([it['status'],
                ('第%02d批' % k2b[it['key']]) if it['key'] in k2b else '—',
                it['topic'].replace('M-T-', 'T'), it['tname'],
                it['l1'], it['l2'], it['kind'], it['key'],
                it['page'] or '—', it['ans'],
                '有' if it['has_sol'] else '无', it['stem'],
                it['status_note']])
for row in ws2.iter_rows(min_row=2):
    for c in row:
        c.border = BD
    fill_by_status(row, 0)
ws2.auto_filter.ref = 'A1:M%d' % (len(items) + 1)

# ---- Sheet3 不录清单（老高考）----
ws5 = wb.create_sheet('不录清单')
head(ws5, ['ref_bank key', '题型', '题型名', '页码', '原书答案', '不录原因',
           '题干摘录'], [15, 9, 30, 7, 11, 34, 52])
old_items = [it for it in items if it['status'] == '不录(老高考)']
for it in sorted(old_items, key=lambda x: x['key']):
    ws5.append([it['key'], it['topic'].replace('M-T-', 'T'), it['tname'],
                it['page'] or '—', it['ans'], it['status_note'], it['stem']])
for row in ws5.iter_rows(min_row=2):
    for c in row:
        c.border = BD; c.fill = OLD_F
ws5.auto_filter.ref = 'A1:G%d' % (len(old_items) + 1)

# ---- Sheet4 跳过清单 ----
ws3 = wb.create_sheet('跳过清单')
head(ws3, ['ref_bank key', '题型', '题型名', '页码', '原书答案', '跳过原因',
           '说明', '题干摘录'], [15, 9, 22, 7, 12, 12, 34, 52])
for i in SK:
    ws3.append([i.get('key'), (i.get('topic') or '').replace('M-T-', 'T'),
                i.get('topic_name', ''), i.get('page', ''),
                i.get('ref_answer', ''), i.get('reason', ''),
                i.get('note', ''), i.get('stem_raw', '')])
for row in ws3.iter_rows(min_row=2):
    for c in row:
        c.border = BD; c.fill = SKIP_F
ws3.auto_filter.ref = 'A1:H%d' % (len(SK) + 1)

# ---- Sheet4 阶段总览 ----
ws4 = wb.create_sheet('阶段总览')
head(ws4, ['阶段', '优先级', '待录题数', '批次数', '说明'], [12, 8, 10, 8, 46])
cnt1, bcnt = {}, {}
for b in batches:
    for kk in b:
        cnt1[kk[0]] = cnt1.get(kk[0], 0) + len(groups_todo[kk])
    bcnt[b[0][0]] = bcnt.get(b[0][0], 0) + 1
for name, pr, note in STAGE:
    if name in cnt1:
        ws4.append([name, pr, cnt1[name], bcnt.get(name, 0), note])
ws4.append(['合计', '', sum(cnt1.values()), len(batches), ''])
for row in ws4.iter_rows(min_row=2):
    for c in row:
        c.border = BD; c.alignment = Alignment('center', 'center')
for c in ws4[ws4.max_row]:
    c.font = Font(bold=True); c.fill = SUB

out = '教辅录入任务计划清单.xlsx'
wb.save(out)
print('  已生成:', out)
print('    总题 %d = 已录 %d(含补录 %d) + 不录 %d + 重复 %d + 跳过 %d + 待录 %d'
      % (len(items), STAT.get('已录入', 0) + STAT.get('已录入(补录)', 0),
         STAT.get('已录入(补录)', 0), STAT.get('不录(老高考)', 0),
         STAT.get('重复跳过', 0), STAT.get('人工跳过', 0),
         STAT.get('待录入', 0)))
assert sum(STAT.values()) == len(items), '状态之和与总数不符'
# 用 BANK_KEYS 而非 DONE：DONE 来自 recorded_keys()，只认 ref_bank 里的 key，
# 补录题（13 道）不在其中，拿它当基准会永远差 13。
assert (STAT.get('已录入', 0)
        + STAT.get('已录入(补录)', 0)) == len(BANK_KEYS), (
    '清单已录数(%d) 与题库教辅题数(%d) 不符'
    % (STAT.get('已录入', 0) + STAT.get('已录入(补录)', 0), len(BANK_KEYS)))
print('    待录分批 %d 批，覆盖 %d 题' % (len(batches), len(todo_keys)))

# ---------------- Markdown ----------------
md = ['# 教辅录入任务计划清单', '',
      '**来源**：2024高中数学热点题型归纳完整解析版.pdf（456 页）', '',
      '**本清单按真实进度生成**（`tools/make_plan.py`），'
      '重跑即刷新，不再手工维护。', '',
      '## 进度总览', '',
      '| 项目 | 题数 | 说明 |', '|---|---:|---|',
      '| 教辅总题数 | %d | ref_bank 提取总数 |' % len(items),
      '| 已录入 | %d | 已入库可组卷（含补录 %d 题）|'
      % (STAT.get('已录入', 0) + STAT.get('已录入(补录)', 0),
         STAT.get('已录入(补录)', 0)),
      '| 不录(老高考) | %d | 柯西/绝对值不等式、线性规划 |'
      % STAT.get('不录(老高考)', 0),
      '| 重复跳过 | %d | 与前面某题同题 |' % STAT.get('重复跳过', 0),
      '| 人工跳过 | %d | 待裁定，见跳过清单表 |' % STAT.get('人工跳过', 0),
      '| **待录入** | **%d** | 参与分批 |' % STAT.get('待录入', 0),
      '| 批次数 | %d | 每批约 18 题 |' % len(batches), '',
      '## 阶段总览', '',
      '| 阶段 | 优先级 | 待录题数 | 批次数 | 说明 |', '|---|---|---:|---:|---|']
for name, pr, note in STAGE:
    if name in cnt1:
        md.append('| %s | %s | %d | %d | %s |' % (name, pr, cnt1[name],
                                                  bcnt.get(name, 0), note))
md += ['| **合计** | | **%d** | **%d** | |'
       % (sum(cnt1.values()), len(batches)), '',
       '## 批次明细', '',
       '| 批次 | 阶段 | 题型范围 | 题数 | 页码 | 备注 |',
       '|---|---|---|---:|---|---|']
for r_ in rows:
    md.append('| %s | %s | %s | %d | %s | %s |'
              % (r_[0], r_[1], r_[3], r_[4], r_[5], r_[8]))
md += ['', '> 「不等式选讲」为老高考内容，新高考不考，'
       '已单独成批，可整批跳过。', '']
mdf = '教辅录入任务计划清单.md'
open(mdf, 'w', encoding='utf-8').write('\n'.join(md))
print('  已生成:', mdf)
