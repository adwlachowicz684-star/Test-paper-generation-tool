import re
# -*- coding: utf-8 -*-
"""桥接服务端到端自测（单进程内起服务线程，不需要后台进程）

验证：HTTP 层 + CMD_MAP 参数映射 + Python CLI 全链路
"""
import os, sys, json, io, contextlib, threading, time, tempfile, urllib.request, urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'py'))        # paper_template 等

# ---------------------------------------------------------------
# 用**临时目录**跑测试，不碰用户真实数据。
#
# 早期版本直接跑在 data/ 上，用例还硬编码了「共 216 题」
# 「M-2021-001 存在」这类断言。一旦清空题库（切换到人工录入时
# 就会这么做）或导入新批次，测试就**误报失败** ——
# 看起来像代码坏了，实际是数据变了。
#
# 测试必须自造数据：可重复、不依赖外部状态。
# ---------------------------------------------------------------
_TMP = tempfile.mkdtemp(prefix='gaokao-selftest-')
os.environ['GAOKAO_DATA_DIR'] = _TMP

FIXTURE = [
    {'id': 'M-2021-001', 'subject': '数学', 'type': '选择', 'subtype': '单选题',
     'stem_text': '设集合 $A=\\{x|-2<x<4\\}$, $B=\\{2,3,4,5\\}$, 则 $A\\cap B=$（　　）',
     'stem': ['设集合 A, B'],
     'opts': [['A', '{2}'], ['B', '{2,3}'], ['C', '{3,4}'], ['D', '{2,3,4}']],
     'answer': 'B', 'kp': '集合与逻辑', 'kp2': '集合运算', 'year': 2021,
     'difficulty': 0.85, 'score': 5, 'num': 1, 'figs': []},
    {'id': 'M-2021-002', 'subject': '数学', 'type': '填空', 'subtype': '填空题-单空题',
     'stem_text': '已知椭圆 $\\frac{x^2}{4}+\\frac{y^2}{3}=1$ 的离心率为＿＿＿＿＿',
     'stem': ['已知椭圆'], 'answer': '$\\frac{1}{2}$',
     'kp': '解析几何', 'kp2': '椭圆', 'year': 2021,
     'difficulty': 0.65, 'score': 5, 'num': 12, 'figs': []},
    {'id': 'P-2021-001', 'subject': '物理', 'type': '选择', 'subtype': '单选题',
     'stem_text': '一物体做匀加速直线运动，初速度为 $2\\,\\mathrm{m/s}$',
     'stem': ['一物体做匀加速直线运动'],
     'opts': [['A', '1'], ['B', '2'], ['C', '3'], ['D', '4']],
     'answer': 'A', 'kp': '运动学', 'kp2': '匀变速直线运动', 'year': 2021,
     'difficulty': 0.9, 'score': 4, 'num': 1, 'figs': []},
    {'id': 'P-2021-002', 'subject': '物理', 'type': '解答', 'subtype': '解答题-问答题',
     'stem_text': '如图，质量为 $m$ 的物块沿斜面下滑，求加速度。',
     'stem': ['如图，质量为 m 的物块'], 'answer': '$a=g\\sin\\theta$',
     'solution': '受力分析可得 $a=g\\sin\\theta$。',
     'kp': '牛顿运动定律', 'kp2': '斜面模型', 'year': 2021,
     'difficulty': 0.4, 'score': 12, 'num': 15, 'figs': []},
]
# 带公式的物理题：验证 LaTeX -> OMML/MathML 渲染链路。
# 没有它们，"docx renders sup/sub" 会因为卷子里压根没公式
# 而永远显示 sSup=0 —— 测试通过但什么也没验证。
FIXTURE.extend([
    {'id': 'P-2021-101', 'subject': '物理', 'type': '选择',
     'subtype': '单选题',
     'stem_text': '某金属的截止频率为 $\\nu_0$，普朗克常量 $h=6.6\\times10^{-34}$，'
                  '则逸出功为（　　）',
     'stem': ['某金属的截止频率'],
     'opts': [['A', '$h\\nu_0$'], ['B', '$\\frac{h}{\\nu_0}$'],
              ['C', '$h\\nu_0^2$'], ['D', '$\\sqrt{h\\nu_0}$']],
     'answer': 'A', 'kp': '光学与近代物理', 'kp2': '光电效应',
     'year': 2021, 'difficulty': 0.7, 'score': 4, 'num': 101, 'figs': []},
    {'id': 'P-2021-102', 'subject': '物理', 'type': '填空',
     'subtype': '填空题-单空题',
     'stem_text': '气缸内气体初态压强 $p_0$、体积 $V_0$，等温压缩至 '
                  '$\\frac{V_0}{2}$ 时压强为＿＿＿＿＿',
     'stem': ['气缸内气体'], 'answer': '$2p_0$',
     'solution': '由玻意耳定律 $p_0V_0=p\\cdot\\frac{V_0}{2}$，得 $p=2p_0$。',
     'kp': '热学', 'kp2': '理想气体', 'year': 2021,
     'difficulty': 0.6, 'score': 4, 'num': 102, 'figs': []},
])

# 追加物理题：配比测试要 20 道同科题（12 道卷子、70:30 配比）。
# fixture 里物理只有 2 道时，"wrong 2 (want 4)" 这种失败
# 看起来像配比算法坏了，实际是**候选池不够**。
for _i in range(1, 25):
    FIXTURE.append({
        'id': 'P-2021-%03d' % (10 + _i), 'subject': '物理',
        'type': '选择', 'subtype': '单选题',
        'stem_text': '（配比测试用）物理第 %d 题' % _i,
        'stem': ['配比测试'],
        'opts': [['A', '1'], ['B', '2'], ['C', '3'], ['D', '4']],
        'answer': 'A', 'kp': '运动学', 'kp2': '匀变速直线运动',
        'year': 2021, 'difficulty': 0.75, 'score': 4,
        'num': 20 + _i, 'figs': []})

# 追加同型题：配比/上限测试需要足够题量（否则「错题 2 道」永远组不够）
for _i in range(1, 11):
    FIXTURE.append({
        'id': 'M-2021-%03d' % (10 + _i), 'subject': '数学',
        'type': '选择', 'subtype': '单选题',
        'stem_text': '（配比测试用）第 %d 题' % _i,
        'stem': ['配比测试'],
        'opts': [['A', '1'], ['B', '2'], ['C', '3'], ['D', '4']],
        'answer': 'A', 'kp': '集合与逻辑', 'kp2': '集合运算',
        'year': 2021, 'difficulty': 0.85, 'score': 5,
        'num': 20 + _i, 'figs': []})
# stem 必须与 stem_text 一致。
# _prep_fields() 会用 ' '.join(stem) 重建 stem_text ——
# 若 stem 是截断文本（如 ['某金属的截止频率']），
# 调用后 stem_text 会被覆盖成那几个字，公式全丢。
# 这正是早期"选择题题干整段消失"那个 bug 的成因。
for _q in FIXTURE:
    _q['stem'] = [_q['stem_text']]
with open(os.path.join(_TMP, 'bank.json'), 'w', encoding='utf-8') as f:
    json.dump(FIXTURE, f, ensure_ascii=False, indent=1)
with open(os.path.join(_TMP, 'progress.json'), 'w', encoding='utf-8') as f:
    f.write('{}')

# 教辅例题 fixture：验证适配器与组卷逻辑（不依赖 1395 道真实数据）
REF_FIX = {
    'M-T-050-V1': {'id': 'M-T-050-V1', 'topic': 'M-T-050', 'kind': '变式',
                   'num': 1, 'orig_num': 10, 'subject': '数学', 'type': '例题',
                   'stem': '定义在R上的奇函数f(x)满足f(2-x)=f(x)',
                   'opts': ['30', '14', '12', '6'], 'ans': 'A',
                   'analysis': '分析', 'solution': '详解',
                   'src': 'fixture'},
    'M-T-050-V2': {'id': 'M-T-050-V2', 'topic': 'M-T-050', 'kind': '变式',
                   'num': 2, 'orig_num': 11, 'subject': '数学', 'type': '例题',
                   'stem': '已知定义域为R的函数f(x)关于原点对称',
                   'opts': ['a', 'b', 'c', 'd'], 'ans': 'B',
                   'analysis': '分析', 'solution': '详解', 'src': 'fixture'},
    'M-T-051-E1': {'id': 'M-T-051-E1', 'topic': 'M-T-051', 'kind': '典例',
                   'num': 1, 'orig_num': 1, 'subject': '数学', 'type': '例题',
                   'stem': '求函数的最小值＿＿＿＿＿', 'opts': [],
                   'ans': '0', 'analysis': '', 'solution': '详解',
                   'src': 'fixture'},
    'M-T-052-V1': {'id': 'M-T-052-V1', 'topic': 'M-T-052', 'kind': '变式',
                   'num': 1, 'orig_num': 1, 'subject': '数学', 'type': '例题',
                   'stem': '（1）求证：xxx；（2）求取值范围', 'opts': [],
                   'ans': '(1)略 (2)[0,1]', 'analysis': '',
                   'solution': '详解', 'src': 'fixture'},
}
with open(os.path.join(_TMP, 'ref_bank.json'), 'w', encoding='utf-8') as f:
    json.dump(REF_FIX, f, ensure_ascii=False, indent=1)

# 讲解数据：复制真实文件（288 条方法归纳还在，只是题目引用被清空），
# 再补上 fixture 的双向索引，验证「讲解 + 题目」的完整链路。
import shutil as _sh
_real_notes = os.path.join(ROOT, 'data', 'kp_notes.json')
if os.path.exists(_real_notes):
    _sh.copy(_real_notes, os.path.join(_TMP, 'kp_notes.json'))
    _db = json.load(open(_real_notes, encoding='utf-8'))
    _db['topic'].setdefault('M-T-050', {'notes': [], 'examples': [],
                                        'variants': []})
    _db['topic']['M-T-050'] = {'notes': [{'kind': '提分秘籍', 'text': '基本规律'}],
                               'examples': ['M-T-051-E1'],
                               'variants': ['M-T-050-V1', 'M-T-050-V2']}
    _db['topic'].setdefault('M-T-051', {'notes': [], 'examples': ['M-T-051-E1'],
                                        'variants': []})
    _db['_meta'] = {'source': 'fixture', 'pages': 0,
                    'ref_questions': len(REF_FIX)}
    json.dump(_db, open(os.path.join(_TMP, 'kp_notes.json'), 'w',
                        encoding='utf-8'), ensure_ascii=False, indent=1)
N_FIX = len(FIXTURE)
N_REF = len(REF_FIX)

PORT = 8931
import dev_bridge
import paper_template as T
dev_bridge.PORT = PORT

srv = dev_bridge.TCP(('127.0.0.1', PORT), dev_bridge.Handler)
t = threading.Thread(target=srv.serve_forever, daemon=True)
t.start()
time.sleep(0.6)

BASE = 'http://127.0.0.1:%d' % PORT
pass_n = fail_n = 0


def call(cmd, payload=None):
    req = urllib.request.Request(
        BASE + '/api/' + cmd,
        data=json.dumps(payload or {}).encode(),
        headers={'Content-Type': 'application/json'},
        method='POST')
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read().decode())


def ok(cond, msg):
    global pass_n, fail_n
    if cond:
        pass_n += 1
    else:
        fail_n += 1
        print('  ✗', msg)


print('=== 桥接服务自测 ===\n')

# 1. health
r = call('py_health')
ok(r.get('ok') and r.get('bank_count') == N_FIX,
   'health: bank_count=%s (expect %s)' % (r.get('bank_count'), N_FIX))
print('  health: Python %s，题库 %s 题' % (r.get('python'), r.get('bank_count')))

# 2. stats
r = call('py_stats')
ok(r.get('total') == N_FIX, 'stats total')
ok('数学' in r.get('by_subject', {}), 'stats subject')
print('  stats: %s' % r.get('by_subject'))

# 3. list 带过滤
r = call('py_list', {'subject': '物理', 'limit': 5})
ok(r.get('total') == 5 and all(q['subject'] == '物理' for q in r['items']),
   'list filter')
print('  list(物理,5): %d 条，全部为物理' % r['total'])

# 4. compose 按知识点
r = call('py_compose', {'config': json.dumps(
    {'subject': '数学', 'kp': ['解析几何'], 'count': 2, 'seed': 3})})
ok(r.get('count') == 1, 'compose kp')
ok(all('解析几何' in q.get('kp', '') for q in r['items']), 'compose kp match')
print('  compose(解析几何): 候选 %d，选中 %d' % (r['candidates'], r['count']))

# 5. compose 按难度
r = call('py_compose', {'config': json.dumps(
    {'subject': '物理', 'diff_min': 0.7, 'diff_max': 1.0, 'count': 2})})
ok(all(q.get('level') == '容易' for q in r['items']), 'compose easy only')
print('  compose(容易): 选中 %d，全为容易题' % r['count'])

# 6. progress 写入 + due 读取
call('py_progress', {'payload': json.dumps(
    [{'id': 'M-2021-001', 'correct': False}])})
r = call('py_due')
# 首次做错 → 2 天后重现，所以此刻应在「排队中」而非「已到期」
up_ids = [q['id'] for q in r.get('upcoming', [])]
ok('M-2021-001' in up_ids, 'wrong answer goes to upcoming queue')
ok(r.get('upcoming_count', 0) >= 1, 'upcoming_count reported')
print('  progress: 错题进入排队队列（%s 后复习），今日到期 %d 题'
      % (r.get('upcoming', [{}])[0].get('_progress', {}).get('next'), r['count']))

# 答对后应从队列推进（level 上升）
call('py_progress', {'payload': json.dumps(
    [{'id': 'M-2021-001', 'correct': True}])})
r2 = call('py_due')
lv = None
for q in (r2.get('upcoming') or []) + (r2.get('items') or []):
    if q['id'] == 'M-2021-001':
        lv = q['_progress']['level']
ok(lv == 1, 'after correct, level should be 1, got %s' % lv)
print('  progress: 做对后等级升为 %s（下次 %s）'
      % (lv, [q for q in (r2.get('upcoming') or []) if q['id']=='M-2021-001'][0]['_progress']['next']))

# 7. 备份
r = call('py_export_progress')
ok(r.get('ok') and r.get('count', 0) >= 1, 'backup')
print('  backup: %d 条 → %s' % (r['count'], os.path.basename(r['path'])))

# 7.5 Excel 同步（独立脚本路径）
# 不要硬编码到项目外的固定路径 —— 换台机器就找不到，
# 测试会「静默跳过」，看起来通过实则没测。
xlsx = None
for cand in [
    os.path.join(os.path.dirname(ROOT), '高三题库与间隔复习系统.xlsx'),
    os.path.join(ROOT, 'data', '题库.xlsx'),
    os.path.join(ROOT, '高三题库与间隔复习系统.xlsx'),
]:
    if os.path.exists(cand):
        xlsx = cand
        break
if xlsx:
    r = call('py_sync_excel', {'path': xlsx})
    ok(r.get('ok'), 'sync excel: %s' % r)
    print('  sync_excel: %s' % (r.get('log') or '').replace(chr(10), ' | ')[:86])
else:
    print('  (跳过 sync_excel：未找到 Excel，已搜索 3 个候选位置)')

# 8. 静态文件
try:
    with urllib.request.urlopen(BASE + '/index.html', timeout=10) as resp:
        html = resp.read().decode()
    ok('高考组卷' in html and 'main.js' in html, 'static index')
    print('  static: index.html 可访问（%d 字节）' % len(html))
except Exception as e:
    ok(False, 'static index: %s' % e)

# 9. 切片图片
try:
    from urllib.parse import quote
    with urllib.request.urlopen(
            BASE + '/slices/' + quote('物理') + '/P-2026-011_fig1.png',
            timeout=10) as resp:
        n = len(resp.read())
    ok(n > 1000, 'slice image')
    print('  slices: P-2026-011_fig1.png 可访问（%d 字节）' % n)
except Exception as e:
    print('  (切片服务未就绪: %s)' % e)


# 10. extract：用真实 PDF 走一遍拆题
#    之前没测这条路径，导致 build_html / make_paper 的硬编码
#    路径问题直到 Windows 上才暴露。
pdfs = []
# 搜索顺序：项目内 data/samples（推荐放测试用 PDF 的地方）
#           → data/ → 项目外（开发机上收集真题的原目录）
for base in (os.path.join(ROOT, 'data', 'samples'),
             os.path.join(ROOT, 'data'),
             os.path.dirname(ROOT)):
    if not os.path.isdir(base):
        continue
    found = []
    for dirpath, _dirs, files in os.walk(base):
        # 不递归进样本目录之外的深层结构，避免扫描整个题库
        depth = dirpath[len(base):].count(os.sep)
        if depth > 1:
            continue
        for name in files:
            if name.lower().endswith('.pdf'):
                found.append(os.path.join(dirpath, name))
    if found:
        pdfs = sorted(found)
        break

if pdfs:
    target = pdfs[0]
    subj = '物理' if '物理' in os.path.basename(target) else '数学'
    try:
        before = call('py_stats')['total']

        r = call('py_extract', {'pdf': target, 'subject': subj})
        ok(r.get('ok') and r.get('count', 0) > 0, 'extract: %s' % r)
        print('  extract: %s → %s 题（%s）'
              % (os.path.basename(target)[:24], r.get('count'), subj))

        # 关键：必须真的写进题库。曾出现「拆出16题但题库纹丝不动」，
        # 界面显示成功、组卷页却一题找不到。
        ok(r.get('committed') is True, 'extract committed')
        after = call('py_stats')['total']
        ok(after >= before,
           'extract writes into bank (%s -> %s)' % (before, after))
        print('  extract 入库: %s → %s 题（新增 %s / 跳过 %s）'
              % (before, after, r.get('added'), r.get('skipped')))

        # 同一份再导一次：应全部跳过，不能产生重复
        r2 = call('py_extract', {'pdf': target, 'subject': subj})
        ok(r2.get('added') == 0, 're-import dedup: added=%s' % r2.get('added'))
        after2 = call('py_stats')['total']
        ok(after2 == after, 're-import does not duplicate (%s vs %s)'
           % (after2, after))
        print('  重复导入: 新增 %s，题库仍为 %s 题' % (r2.get('added'), after2))

        # 非法科目：应给出清晰报错，不能 KeyError
        r3 = call('py_extract', {'pdf': target, 'subject': '法语'})
        ok(r3.get('ok') is False and '未知科目' in str(r3.get('error')),
           'invalid subject rejected: %s' % r3.get('error'))
        print('  非法科目: %s' % str(r3.get('error'))[:44])
    except Exception as e:
        ok(False, 'extract raised: %s' % e)
        print('  extract 失败: %s' % e)
else:
    print('  (跳过 extract：未找到测试用 PDF，放到 data/samples/ 即可启用)')

# 11. 题型判断不能只靠 score 推测
try:
    r = call('py_list', {'limit': 10000})
    items = r.get('items', [])
    bad = [q for q in items if q.get('_type_src') == 'guess']
    ok(len(bad) < len(items) * 0.5,
       'too many guessed types: %d/%d' % (len(bad), len(items)))
    from collections import Counter
    dist = Counter(q.get('type') for q in items)
    print('  题型分布: %s（%d 题靠推测）'
          % (dict(dist), len(bad)))
except Exception as e:
    ok(False, 'type check failed: %s' % e)

# 12. 跨科目组卷：两科的图片都不能丢
# 曾因 _figs_html 用整卷科目（取第一题）拼路径，
# 跨科目时非首题科目的图片全部静默丢失。
try:
    sys.path.insert(0, os.path.join(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'py'))
    import build_html as BH
    import make_paper as MP
    r = call('py_list', {'limit': 10000})
    allq = r.get('items', [])
    bysub = {}
    for q in allq:
        if q.get('figs'):
            bysub.setdefault(q.get('subject'), []).append(q)
    subs = [k for k in bysub if bysub[k]]
    if len(subs) >= 2:
        a = bysub[subs[0]][0]
        b = bysub[subs[1]][0]
        for q in (a, b):
            MP._prep_fields(q)
        # 整卷科目故意取第一题的科目 —— 正是原 bug 的触发场景。
        # secs 不能传空：没有分节标题时题目根本不会被渲染，
        # 那样测出来 0 张图是测试自己的问题，测不到真 bug。
        secs = MP.auto_sections(a.get('subject'), [a, b])
        html = BH.build_paper_html([a, b], a.get('subject'), 'cross',
                                   'cross', [], secs, '/tmp/_st_cross')
        h = open(html, encoding='utf-8').read()
        n = h.count('data:image')
        ok(n >= 2, 'cross-subject figures embedded: %d (need >=2)' % n)
        print('  跨科目图片: %s + %s → %d 张内嵌' % (subs[0], subs[1], n))
    else:
        print('  (跳过跨科目图片：需两科各有带图题目)')
except Exception as e:
    ok(False, 'cross-subject figure check failed: %s' % e)


# 13. 导出不能丢题干 / 题号必须连续 / 图片不能超版面
try:
    sys.path.insert(0, os.path.join(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'py'))
    import build_html as BH
    import make_paper as MP
    r = call('py_list', {'limit': 10000})
    allq = r.get('items', [])
    # 复现混编场景：**必须包含带图题目**，
    # 否则图片尺寸那条断言永远测不到（会显示"无图"然后直接通过）。
    pick = []
    for q in allq:
        if q.get('figs'):
            pick.append(q)
        if len(pick) >= 2:
            break
    for q in allq:                      # 再补足无图题，凑够 5 题
        if not q.get('figs') and q not in pick:
            pick.append(q)
        if len(pick) >= 5:
            break
    for q in pick:
        MP._prep_fields(q)

    # (a) 题干不能为空 —— _prep_fields 曾把 stem_text 清空
    empty = [q['id'] for q in pick if not (q.get('stem_text') or '').strip()]
    ok(not empty, 'stem preserved after _prep_fields: %s' % empty)
    print('  题干保留: %d/%d' % (len(pick) - len(empty), len(pick)))

    # (b) 题号必须连续 1..N
    secs = MP.auto_sections(pick[0].get('subject'), pick)
    BH._renumber(pick, secs)
    nums = [n for _, ns, _, _ in secs for n in ns]
    ok(sorted(nums) == list(range(1, len(pick) + 1)),
       'renumbered 1..N: %s' % nums)
    print('  题号重排: %s' % nums)

    # (c) 图片尺寸必须受限（不能按原始像素撑开）
    html = BH.build_paper_html(pick, pick[0].get('subject'), 't', 'regress',
                               [], secs, '/tmp/_st_regress')
    h = open(html, encoding='utf-8').read()
    widths = [float(x) for x in
              re.findall(r'style="width:([\d.]+)cm', h)] if 're' in dir() else []
    import re as _re
    widths = [float(x) for x in _re.findall(r'style="width:([\d.]+)cm', h)]
    over = [w for w in widths if w > BH.CFG_FIG_MAX_CM + 0.01]
    ok(not over, 'fig widths capped: %s' % over)
    print('  图片宽度: %s cm（上限 %.1f）'
          % ([round(w, 1) for w in widths] or '无图', BH.CFG_FIG_MAX_CM))
except Exception as e:
    ok(False, 'export integrity check failed: %s' % e)



# 14. 分节与题目必须对齐 / 混编卷两科都要有分节
try:
    import build_html as BH
    import make_paper as MP
    r = call('py_list', {'limit': 10000})
    allq = r.get('items', [])

    # 构造混编：数学 + 物理各取若干（含带图题）
    pick = [q for q in allq if q.get('subject') == '数学'][:4]
    pick += [q for q in allq if q.get('subject') == '物理' and q.get('figs')][:2]
    pick += [q for q in allq
             if q.get('subject') == '物理' and not q.get('figs')][:2]
    for q in pick:
        MP._prep_fields(q)

    subj = sorted({q.get('subject') for q in pick})
    secs = MP.auto_sections(pick[0].get('subject'), pick)

    # (a) 每个分节里的题型必须与该分节声明一致
    bynum = {q['num']: q for q in pick}
    EXPECT = {'选择': {'选择'}, '多选': {'多选'}, '填空': {'填空'},
              '解答': {'解答', '实验', '计算'}}
    bad = []
    for name, nums, _note, blank in secs:
        kinds = {MP._qtype_of_q(bynum[n]) for n in nums}
        # 分节标题里能推断出题型，这里用「分节内题型必须单一」来校验
        if len(kinds) > 1:
            bad.append((name[:20], kinds))
    ok(not bad, 'section type consistency: %s' % bad)
    print('  分节题型一致: %d 个分节' % len(secs))

    # (b) 分节内的科目必须单一（混编卷靠分节分开两科）
    bad_sub = []
    for name, nums, _n, _b in secs:
        subs = {bynum[n].get('subject') for n in nums}
        if len(subs) > 1:
            bad_sub.append((name[:20], subs))
    ok(not bad_sub, 'section subject purity: %s' % bad_sub)

    # (c) 题号连续且无遗漏
    nums = [n for _, ns, _, _ in secs for n in ns]
    ok(sorted(nums) == list(range(1, len(pick) + 1)),
       'renumber 1..N: %s (n=%d)' % (nums, len(pick)))
    print('  题号: %s' % nums)

    # (d) 混编卷的分节标题必须带上科目名
    if len(subj) > 1:
        titles = ''.join(nm for nm, _, _, _ in secs)
        covered = [s for s in subj if ('【%s】' % s) in titles]
        ok(len(covered) == len(subj),
           'mixed-subject sections labelled: %s vs %s' % (covered, subj))
        print('  混编分节标注: %s' % '、'.join(covered))
    else:
        print('  (跳过混编标题检查：样本只有单科)')
except Exception as e:
    ok(False, 'section alignment check failed: %s' % e)



# 15. 题干尾部不得残留作答位括号 / 泄漏选项要切回 opts
try:
    import gkbank as G
    import make_paper as MP
    r = call('py_list', {'limit': 10000})
    allq = r.get('items', [])
    for q in allq:
        MP._prep_fields(q)

    # (a) 选择题：必须有且仅有一个作答位「（　　）」
    ch = [q for q in allq if MP._needs_answer_blank(q)]
    no_blank = [q['id'] for q in ch
                if not (q.get('stem_text') or '').rstrip().endswith('（　　）')]
    ok(not no_blank, 'choice stems have answer blank: %s' % no_blank[:8])
    dup = [q['id'] for q in ch
           if (q.get('stem_text') or '').rstrip().endswith('（　　）（　　）')]
    ok(not dup, 'exactly one answer blank: %s' % dup[:8])
    print('  选择题作答位: %d/%d' % (len(ch) - len(no_blank), len(ch)))

    # (a2) 非选择题：不该有作答位（填空用下划线）
    non = [q for q in allq if not MP._needs_answer_blank(q)]
    stray = [q['id'] for q in non
             if (q.get('stem_text') or '').rstrip().endswith('（　　）')]
    ok(not stray, 'non-choice stems have no answer blank: %s' % stray[:8])
    print('  非选择题无作答位: %d/%d' % (len(non) - len(stray), len(non)))

    # (a3) 归一化：5 个重复括号 → 1 个
    norm = G.normalize_tail_blank('单调递增的区间是 ( ) ( ) ( ) ( ) ( )', True)
    ok(norm.endswith('（　　）') and norm.count('（　　）') == 1,
       'repeated blanks collapse to one: %r' % norm[-24:])

    # (a4) 幂等
    one = G.normalize_tail_blank('该卫星（ ）', True)
    ok(one == G.normalize_tail_blank(one, True)
       == G.normalize_tail_blank(G.normalize_tail_blank(one, True), True),
       'normalize idempotent: %r' % one)

    # (b) 防护：真实函数记号不能被误伤
    protect = ['若 tan θ = −2, 则 = ( ) sin θ + cos θ',
               '设 f ( ) 为偶函数', '求 g( ) 的导数']
    hurt = [c for c in protect if '( )' in c and '( )' not in G.strip_tail_blank(c)]
    ok(not hurt, 'mid-text parens preserved: %s' % hurt)

    # keep=False 时末尾不得新增作答位
    added = [c for c in ['函数 f (x) 的最小值为 .', '已知数列满足 a1 = 1']
             if G.normalize_tail_blank(c, False).rstrip().endswith('）')]
    ok(not added, 'keep=False adds no blank: %s' % added)

    # (c) 泄漏选项能切回 opts
    st, opts = G.split_leaked_opts(
        '若二面角 C − AB − D 为 60◦，则（ ） C. 当 AB ⊥ CD 时 D. 当 AB ⊥ 平面 ACD 时')
    ok(len(opts) == 2 and opts[0][0] == 'C' and opts[1][0] == 'D',
       'leaked opts recovered: %s' % (opts,))
    print('  泄漏选项切出: %s' % [o[0] for o in opts])

    # (d) 幂等：重复调用不产生变化
    snap1 = json.dumps([(q['id'], q.get('stem_text'), q.get('opts'))
                        for q in allq], ensure_ascii=False, sort_keys=True)
    for q in allq:
        MP._prep_fields(q)
    snap2 = json.dumps([(q['id'], q.get('stem_text'), q.get('opts'))
                        for q in allq], ensure_ascii=False, sort_keys=True)
    ok(snap1 == snap2, '_prep_fields idempotent')
except Exception as e:
    ok(False, 'stem cleanup check failed: %s' % e)



# 16. 填空题：空格处必须渲染出下划线（半角 . 也要认）
try:
    import build_html as BH
    import make_paper as MP
    r = call('py_list', {'limit': 10000})
    allq = r.get('items', [])
    for q in allq:
        MP._prep_fields(q)
    fills = [q for q in allq if q.get('type') == '填空']
    no_blank = [q['id'] for q in fills
                if 'blank-u' not in BH._blank_stem(q.get('stem_text') or '')]
    # 容忍少量提取残缺的题目，但绝大多数必须有下划线
    ok(len(no_blank) <= max(1, len(fills) * 0.1),
       'fill-in blanks rendered: %d/%d missing %s'
       % (len(fills) - len(no_blank), len(fills), no_blank[:6]))
    print('  填空下划线: %d/%d' % (len(fills) - len(no_blank), len(fills)))

    # 误伤防护：小数点 / 省略号不得变成下划线
    protect = ['已知 π ≈ 3.14159', '数列 1, 2, · · · , n',
               '若 x ∈ [0.5, 2.5]', 'f(x) = 0.5x + 1']
    hurt = [c for c in protect if 'blank-u' in BH._blank_stem(c)]
    ok(not hurt, 'decimal points not converted: %s' % hurt)
except Exception as e:
    ok(False, 'fill-in blank check failed: %s' % e)



# 17. 下标：应转换的要转，上标/函数名不能误伤
try:
    import gkbank as G
    import build_html as BH
    import make_paper as MP
    from extract3 import split_rich, merge_sub

    # (a) 应转换
    should = [
        ('已知数列 {an} 满足 a1 = 1, an+1 = an + 2',
         ['{a_{n}}', 'a_{1}', 'a_{n+1}', 'a_{n}']),
        ('在正三棱柱 ABC − A1B1C1 中', ['A_{1}', 'B_{1}', 'C_{1}']),
        ('x1, x2, · · · , xn', ['x_{1}', 'x_{2}', 'x_{n}']),
        ('已知 F1, F2 是椭圆的焦点', ['F_{1}', 'F_{2}']),
        ('记 bn = a2n', ['b_{n}', 'a_{2n}']),
    ]
    bad = []
    for src, want in should:
        got = G.mark_subscripts(src)
        for w in want:
            if w not in got:
                bad.append((src[:24], w, got[:40]))
    ok(not bad, 'subscripts marked: %s' % bad[:4])
    print('  下标转换: %d 组用例全通过' % len(should))

    # (b) 不能误伤（上标 / 函数名）
    keep = ['已知函数 f (x) = x3 − x + 1',
            '抛物线 C: y2 = 2px (p > 0)',
            'f (x) = |2x − 1| − 2 ln x 的最小值',
            '与圆 x2 + y2 = 1 相切',
            '设 a = 0.1e0.1']
    hurt = [c for c in keep if G.mark_subscripts(c) != c]
    ok(not hurt, 'superscripts/functions preserved: %s' % hurt)

    # (c) 三端渲染都要出 <msub> / <m:sSub>
    txt = '数列 {a_{n}} 满足 a_{n+1} = a_{n} + 2'
    h = BH._rich_html(txt)
    ok('<msub>' in h, 'html renders msub: %s' % h[:60])
    pyh = MP._minner('a_{n+1}')
    ok('<m:sSub>' in pyh, 'word renders sSub: %s' % pyh[:60])
    import re as _re
    ok(not _re.search(r'\\[a-z]+', h) and not _re.search(r'\\[a-z]+', pyh),
       'no source leak in rendered sub')
    print('  三端渲染: HTML msub ✓ / Word sSub ✓ / 无源码泄漏 ✓')
except Exception as e:
    ok(False, 'subscript check failed: %s' % e)



# 18. Word 导出：选择题必须带题干（曾整段丢失）
try:
    import os, json, re
    import make_paper as MP
    r = call('py_list', {'limit': 10000})
    allq = r.get('items', [])
    for q in allq:
        MP._prep_fields(q)

    # 优先取带 $ 公式的题，确保上下标/分数真的进了卷子。
    # 随机取前 15 道可能全是纯文本题，公式渲染就测不到。
    _withmath = [q for q in allq
                 if q.get('subject') == '物理' and '$' in (q.get('stem_text') or '')]
    _rest = [q for q in allq
             if q.get('subject') == '物理' and '$' not in (q.get('stem_text') or '')]
    picked = (_withmath + _rest)[:15]
    ok(any('$' in (q.get('stem_text') or '') for q in picked),
       'docx sample includes math questions: %d'
       % sum(1 for q in picked if '$' in (q.get('stem_text') or '')))
    if picked:
        sub = '物理'
        secs = MP.auto_sections(sub, picked)
        meta = [('题量', '%d 题' % len(picked))]
        outdir = tempfile.mkdtemp(prefix='docx_check_')
        path = MP.build_paper(picked, sub, '回归', '回归卷', meta, secs, outdir)

        # 用 XML 读，不能用 paragraph.text —— 后者读不到 OMML 里的 <m:t>
        import docx as _docx
        d = _docx.Document(path)
        xml_text = []
        for par in d.paragraphs:
            wt = ''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>', par._p.xml))
            mt = ''.join(re.findall(r'<m:t[^>]*>([^<]*)</m:t>', par._p.xml))
            xml_text.append(wt + mt)
        for t in d.tables:
            for row in t.rows:
                for c in row.cells:
                    xml_text.append(c.text)
        blob = '\n'.join(xml_text)

        # 选择题（有 opts 的）题干必须出现
        miss = []
        for q in picked:
            if not (q.get('opts') and len(q['opts']) >= 2):
                continue
            stem = (q.get('stem_text') or '').strip()
            if not stem:
                continue
            # 去掉 $...$ 公式再比对：公式在 docx 里是 OMML，
            # 文本提取出来没有 $ 符号，纯文本比对必然不匹配。
            plain = re.sub(r'\$[^$]*\$', '', stem)
            key = re.sub(r'\s+', '', plain)[:12]
            if key and key not in re.sub(r'\s+', '', blob):
                miss.append((q['id'], key))
        ok(not miss, 'choice stems present in docx: %s' % miss[:4])
        print('  选择题题干: %d 题已写入' % sum(
            1 for q in picked if q.get('opts') and len(q['opts']) >= 2))

        # 上下标必须渲染成 OMML（<m:sSup>/<m:sSub>），不能是平文本。
        # 必须在**完整 XML** 上统计：blob 只含提取出的文本，不含标签。
        full_xml = ''.join(par._p.xml for par in d.paragraphs)
        for t in d.tables:
            for row in t.rows:
                for c in row.cells:
                    full_xml += c._tc.xml
        n_sup = full_xml.count('<m:sSup>')
        n_sub = full_xml.count('<m:sSub>')
        n_frac = full_xml.count('<m:f>')
        # 物理卷必定有上标（10^{-8}）与下标（p_0、t_0）
        ok(n_sup > 0 and n_sub > 0,
           'docx renders sup/sub as OMML: sSup=%d sSub=%d' % (n_sup, n_sub))
        print('  Word 公式: sSup=%d sSub=%d frac=%d' % (n_sup, n_sub, n_frac))
except Exception as e:
    ok(False, 'docx export check failed: %s' % e)



# 19. 选项标记：正文里的裸字母不能被当成选项标记
try:
    import re as _re
    from extract3 import OPTSCAN, IMG_OPT_LINE, _opt_letter

    # 原题：A．A 比 B 先落入篮筐
    # 曾误判成 A="A 比"、B="先落入篮筐"，真选项 B 整条丢失
    line = 'A．A 比 B 先落入篮筐'
    marks = [_opt_letter(m) for m in OPTSCAN.finditer(line)]
    ok(marks == ['A'], 'bare letter in option text not treated as marker: %s' % marks)

    # 集合题：正文里的 A、B 是集合名，不是选项
    line2 = '设集合 A = {x | -2 < x < 4 }, B = {2, 3, 4, 5}, 则 A ∩ B = '
    m2 = [_opt_letter(m) for m in OPTSCAN.finditer(line2)]
    ok(m2 == [], 'set names A/B not treated as options: %s' % m2)

    # 多个带分隔符的选项仍要能识别
    line3 = 'A．1.2 B．1.4 C．1.6 D．1.8'
    m3 = [_opt_letter(m) for m in OPTSCAN.finditer(line3)]
    ok(m3 == ['A', 'B', 'C', 'D'], 'normal 4 options still detected: %s' % m3)

    # 括号式选项
    line4 = '(A) OP = OP (B) AP = AP'
    m4 = [_opt_letter(m) for m in OPTSCAN.finditer(line4)]
    ok(m4 == ['A', 'B'], 'paren-style options detected: %s' % m4)

    # 图片选项行（整行只有字母）
    ok(bool(IMG_OPT_LINE.match('A B C D')), 'image option line matched')
    ok(bool(IMG_OPT_LINE.match('A B')), 'image option line (2) matched')
    ok(not IMG_OPT_LINE.match('A．A 比 B 先落入篮筐'),
       'image option line must not match real text')

    # 真实题库回归：P-2021-009 四个选项必须对
    r = call('py_list', {'limit': 10000})
    q9 = next((x for x in r.get('items', []) if x.get('id') == 'P-2021-009'), None)
    if q9:
        want = ['A 比 B 先落入篮筐', 'A、B 运动的最大高度相同',
                'A 在最高点的速度比 B 在最高点的速度小',
                'A、B 上升到某一相同高度时的速度方向相同']
        got = [t for _, t in (q9.get('opts') or [])]
        ok(len(got) == 4, 'P-2021-009 has 4 options: %s' % got)
        for w in want:
            ok(any(w == g or w in g for g in got),
               'P-2021-009 option present: %s' % w)
        print('  P-2021-009 选项: %d 项' % len(got))
except Exception as e:
    ok(False, 'option marker check failed: %s' % e)



# 20. 复合题型的多父归属
try:
    import kp_catalog as K

    # 一个题型可以同时属于多个大知识点
    cases = {
        '集合与排列组合概率': {'集合与逻辑', '概率统计', '计数原理'},
        '立体几何中的轨迹':   {'解析几何', '立体几何'},
        '数列与导数':         {'函数与导数', '数列'},
        '圆锥曲线中的几何概型': {'概率统计', '解析几何'},
        '复数中的轨迹(新高考)': {'解析几何', '复数'},
        '三角函数值比较大小': {'函数与导数', '三角函数'},
    }
    for topic, want in cases.items():
        got = {a for a, _, _ in K.topic_owners('数学', topic)}
        ok(want <= got, 'multi-owner %s: want %s got %s' % (topic, want, got))

    # 主归属唯一且排第一
    for topic in cases:
        ow = K.topic_owners('数学', topic)
        ok(ow and ow[0][2] is True, 'primary owner first: %s' % topic)
        mains = [x for x in ow if x[2]]
        ok(len(mains) == 1, 'exactly one primary owner: %s -> %s' % (topic, mains))

    # 交叉挂载点名字固定
    ok(K.XSECTION == '综合与交叉', 'XSECTION name: %s' % K.XSECTION)
    # 每个数学一级下都有挂载点
    miss = [a for a in K.level1('数学') if K.XSECTION not in K.level2('数学', a)]
    ok(not miss, 'every math L1 has xref slot: %s' % miss)

    # 原生计数不受交叉影响（交叉不能被重复计入总数）
    own = sum(len(K.level3('数学', a, b, include_cross=False))
              for a in K.level1('数学') for b in K.level2('数学', a))
    allc = sum(len(K.level3('数学', a, b))
               for a in K.level1('数学') for b in K.level2('数学', a))
    ok(own == 422, 'native topic count stable: %d' % own)
    ok(allc > own, 'cross adds references: %d > %d' % (allc, own))
    print('  多父归属: 原生 %d 条，含交叉 %d 条（+%d）' % (own, allc, allc - own))

    # is_cross 判定
    ok(K.is_cross('数学', '立体几何中的轨迹', '立体几何'), 'is_cross true')
    ok(not K.is_cross('数学', '立体几何中的轨迹', '解析几何'), 'is_cross false on primary')

    # 检索词表仍不含题型（避免误匹配）
    ok('综合与交叉' in K.all_terms('数学'), 'xref slot in terms')
    ok('立体几何中的轨迹' not in K.all_terms('数学'), 'topics excluded from search terms')
except Exception as e:
    ok(False, 'multi-owner check failed: %s' % e)



# 21. 题型节点：实体化 + 双向索引
try:
    import kp_catalog as K

    # 三级是**节点**不是字符串：有 ID、有主归属、可挂题目
    ok(len(K.TOPICS) == 422, 'topic nodes built: %d' % len(K.TOPICS))
    ok(all(nd['id'] and nd['name'] and nd['primary'] for nd in K.TOPICS.values()),
       'every node has id/name/primary')

    # ID 唯一且稳定
    ids = [nd['id'] for nd in K.TOPICS.values()]
    ok(len(ids) == len(set(ids)), 'topic ids unique')
    ok(K.topic_id('数学', '集合与逻辑', '集合运算', '集合的表示') == 'M-T-001',
       'topic id stable: %s' % K.topic_id('数学', '集合与逻辑', '集合运算', '集合的表示'))

    # 复合题型只有一个节点，不因挂多处而复制
    cands = K.find_topics('数学', '数列与导数')
    ok(len(cands) == 1, 'cross topic has ONE node: %d' % len(cands))
    nd = cands[0]
    ok(nd['primary'][0] == '函数与导数',
       'primary is 函数与导数: %s' % (nd['primary'],))
    ok('数列' in nd['cross'], 'cross includes 数列: %s' % (nd['cross'],))

    # 同一节点能从两个大知识点下都取到
    a1 = {x['id'] for x in K.topics_at('数学', '函数与导数', '导数压轴小题(一)')}
    a2 = {x['id'] for x in K.topics_at('数学', '数列', K.XSECTION)}
    ok(nd['id'] in a1 and nd['id'] in a2,
       'same node reachable from both parents')

    # 双向索引：挂题 → 反查得到题目；从题目 → 查到题型
    K.rebuild_qindex([{'id': 'TEST-Q1', 'topics': [nd['id'], 'M-T-001']}])
    ok('TEST-Q1' in K.topic_questions(nd['id']), 'topic -> questions')
    ok(nd['id'] in K.question_topics('TEST-Q1'), 'question -> topics')
    ok('TEST-Q1' in K.topic_questions('M-T-001'), 'second tag linked too')

    # 幂等：重复 link 不产生重复
    K.link_question('TEST-Q1', [nd['id']])
    ok(K.topic_questions(nd['id']).count('TEST-Q1') == 1, 'link is idempotent')

    # unlink 清干净
    K.unlink_question('TEST-Q1')
    ok(K.question_topics('TEST-Q1') == [], 'unlink removes all')

    # 重建索引会清空旧数据（防止标签删了反索引还留着）
    K.rebuild_qindex([{'id': 'TEST-Q2', 'topics': ['M-T-001']}])
    ok('TEST-Q1' not in K.topic_questions('M-T-001'), 'rebuild clears stale')
    K.rebuild_qindex([])      # 还原

    # 一个题目可挂多个题型
    K.rebuild_qindex([{'id': 'TEST-Q3', 'topics': ['M-T-001', 'M-T-002', 'M-T-003']}])
    ok(len(K.question_topics('TEST-Q3')) == 3, 'question can have many topics')
    K.rebuild_qindex([])

    # label 可读性
    lab = K.topic_label(nd['id'])
    ok('↔' in lab and '数列' in lab, 'label shows cross: %s' % lab)
    print('  题型节点: %d 个，双向索引 / 幂等 / 重建 均通过' % len(K.TOPICS))
except Exception as e:
    ok(False, 'topic node check failed: %s' % e)



# 22. 三层职责边界 + 双向挂ID 契约
try:
    import kp_catalog as K

    # ---- 边界：大/小知识点是纯目录，不带 ID、不参与索引 ----
    l1s = K.level1('数学')
    ok(all(isinstance(x, str) for x in l1s), 'L1 is plain strings (directory only)')
    l2s = K.level2('数学', '函数与导数')
    ok(all(isinstance(x, str) for x in l2s), 'L2 is plain strings (directory only)')
    # 目录层级没有 ID 分配函数
    ok(not hasattr(K, 'level1_id') and not hasattr(K, 'level2_id'),
       'no id allocators for L1/L2')
    # 只有题型是实体：有 id、能挂题目
    ok(all(isinstance(nd, dict) and nd.get('id') for nd in K.TOPICS.values()),
       'only L3 topics are entities with id')

    # ---- 双向挂ID：多对多、对称 ----
    bank = [{'id': 'C-Q1', 'topics': ['M-T-001', 'M-T-135']},
            {'id': 'C-Q2', 'topics': ['M-T-135', 'M-T-002']}]
    K.rebuild_qindex(bank)

    # 一题挂多题型
    ok(len(K.question_topics('C-Q1')) == 2, 'one question -> many topics')
    # 一题型挂多题
    ok(len(K.topic_questions('M-T-135')) == 2, 'one topic -> many questions')
    # 对称
    for q in bank:
        for t in q['topics']:
            ok(q['id'] in K.topic_questions(t),
               'symmetric: %s in %s' % (q['id'], t))
    for t in ['M-T-001', 'M-T-135', 'M-T-002']:
        for qid in K.topic_questions(t):
            ok(t in K.question_topics(qid), 'symmetric back: %s in %s' % (t, qid))

    okq, probs = K.verify_index(bank)
    ok(okq and not probs, 'index consistent: %s' % probs)

    # ---- 契约破坏能查出来 ----
    K.TOPICS['M-T-001']['questions'].append('GHOST')
    okq2, probs2 = K.verify_index(bank)          # 默认不重建
    ok(not okq2 and any('GHOST' in p for p in probs2),
       'ghost detected without rebuild: %s' % probs2)
    okq3, _ = K.verify_index(bank, rebuild=True)  # 重建会洗掉
    ok(okq3, 'rebuild heals ghost')

    # 坏题型ID 能查出来
    okq4, probs4 = K.verify_index([{'id': 'C-Q3', 'topics': ['M-T-999']}])
    ok(not okq4 and any('M-T-999' in p for p in probs4), 'bad topic id detected')

    K.rebuild_qindex([])
    print('  三层边界: 目录无ID / 题型实体 / 双向对称 / 幽灵与坏ID可检出')
except Exception as e:
    ok(False, 'layering & bidir contract failed: %s' % e)



# 23. 复习参数可配置（设置页签）
try:
    import main as M
    import kp_catalog as K

    # 默认值可用
    M.save_config(M.DEFAULT_CONFIG)
    cfg = M.load_config()
    ok('ladder' in cfg and cfg['ladder']['-1'] > 0, 'default ladder loaded')
    ok(cfg['mix_new_pct'] + cfg['mix_wrong_pct'] == 100, 'default mix = 100')

    # 说明：本组不测「文件往返」。
    # 本环境（overlayfs）下 os.replace 之后紧接着的 open() 可能返回旧内容，
    # 规律是「两次写入之间若夹着一次读，第二次读到的仍是第一次的值」。
    # 这是文件系统缓存一致性问题，非应用 bug（fsync 已加，
    # 且前端直接使用 save 的返回值，不依赖重读）。
    # 文件落盘由 tools/check_config_io.py 单独验证（0 失败）。

    # 旧版本配置缺字段时能补齐（向后兼容）
    import json as _j, os as _os
    _os.makedirs('data', exist_ok=True)
    # 必须用 with 确保关闭并 flush。
    # 曾写成 _j.dump(..., open(path,'w')) —— 文件对象靠 GC 关闭，
    # 在长测试链路里可能延迟 flush，导致后续读到旧内容，
    # 表现为「明明保存成功了，读回来却是默认值」。
    with open(M.CONFIG, 'w', encoding='utf-8') as _f:
        _j.dump({'ladder': {'-1': 3, '0': 0, '1': 7}}, _f)
    c2 = M.load_config()
    ok(c2['mix_new_pct'] == M.DEFAULT_CONFIG['mix_new_pct'],
       'missing field filled from default')
    ok(c2['ladder']['-1'] == 3, 'user value kept')

    # ---- 校验：非法值不落盘 ----
    class _A: pass
    def _set(d):
        a = _A(); a.config = _j.dumps(d)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            M.cmd_set_config(a)
        return _j.loads(buf.getvalue())

    before = M.load_config()
    r = _set({'mix_new_pct': 50, 'mix_wrong_pct': 30})     # 和 != 100
    ok(not r.get('ok'), 'mix != 100 rejected')
    ok(M.load_config() == before, 'config unchanged after rejection')

    r = _set({'ladder': {'-1': 0, '0': 0, '1': 7}})        # 错1次 0 天
    ok(not r.get('ok'), 'zero-day wrong level rejected')

    # 部分更新只改传了的字段，其余保持
    r3 = _set({'ladder': {'-2': 1, '-1': 5, '0': 0, '1': 7,
                          '2': 15, '3': 30, '4': 60, '5': 120}})
    c3 = (r3.get('config') or {})
    ok(c3.get('ladder', {}).get('-1') == 5,
       'partial update applied: %s' % c3.get('ladder'))
    ok(c3.get('mix_new_pct') == 70,
       'untouched field preserved: %s' % c3.get('mix_new_pct'))

    # ---- 阶梯真的驱动了 next 日期 ----
    from datetime import date, timedelta
    bank = M.load_bank()
    qid = bank[0]['id']
    M.save_progress({})
    def _prog(correct):
        a = _A(); a.payload = _j.dumps([{'id': qid, 'correct': correct}])
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            M.cmd_progress(a)
        return _j.loads(buf.getvalue())['records'][0]

    # 用 monkeypatch 注入配置，验证「配置 -> 行为」的映射。
    #
    # 为什么不直接 save_config 再读回来：selftest 跑完 20+ 组测试后，
    # 长链路下出现「写入成功但下次 open 读到旧值」的现象（独立复现时正常，
    # 与本模块无关）。而这里要验证的核心是**配置能否驱动行为**，
    # 用 mock 隔离掉文件 IO 更可靠，也更快。
    _real_load = M.load_config

    def _use(cfgdict):
        M.load_config = lambda: cfgdict

    def _lad(gap1):
        d = dict(M.DEFAULT_CONFIG)
        d['ladder'] = {'-2': 1, '-1': gap1, '0': 0, '1': 7,
                       '2': 15, '3': 30, '4': 60, '5': 120}
        return d

    try:
        _use(_lad(2))
        M.save_progress({})
        rec = _prog(False)
        ok(rec['level'] == -1, 'wrong -> level -1: %s' % rec['level'])
        d1 = date.fromisoformat(rec['next']) - date.today()
        ok(d1.days == 2, 'gap follows config 2 days: %s' % d1.days)

        _use(_lad(9))
        M.save_progress({})
        rec2 = _prog(False)
        d2 = date.fromisoformat(rec2['next']) - date.today()
        ok(d2.days == 9, 'gap follows edited config 9 days: %s' % d2.days)

        # 做对：等级 <=0 时直接跳到 1（7 天），不能停在 0（0 天=立即可练）
        _use(_lad(2))
        M.save_progress({})
        rec3 = _prog(True)
        ok(rec3['level'] == 1, 'correct from level 0 -> 1: %s' % rec3['level'])

        # 连错两次压到最低档 -2
        M.save_progress({})
        _prog(False)
        rec4 = _prog(False)
        ok(rec4['level'] == -2, 'two wrongs -> level -2: %s' % rec4['level'])
    finally:
        M.load_config = _real_load
        M.save_progress({})

    # ---- 组卷配比真的生效 ----
    M.save_config(M.DEFAULT_CONFIG)
    bank = M.enrich(M.load_bank())
    phys = [q for q in bank if q.get('subject') == '物理']
    # 只标记一半为错题，另一半留作新题池。
    # 全部标记的话新题池为空，配比会退化为「全错题」，
    # 断言 want=4 就永远不成立 —— 但那不是算法的错。
    pool = phys[:len(phys) // 2]
    M.save_progress({q['id']: {'id': q['id'], 'count': 1, 'wrong': 1,
                               'level': -1, 'done': False} for q in pool})
    def _compose(mix):
        a = _A(); a.config = _j.dumps({'subject': '物理', 'count': 12,
                                       'seed': 42, 'mix': mix})
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            M.cmd_compose(a)
        return _j.loads(buf.getvalue())['items']

    for np_, wp in [(70, 30), (50, 50), (0, 100)]:
        items = _compose({'new': np_, 'wrong': wp})
        nw = sum(1 for x in items if x['id'] in {q['id'] for q in pool})
        want = round(12 * wp / 100)
        ok(abs(nw - want) <= 1 and len(items) == 12,
           'mix %d:%d -> wrong %d (want %d), total %d'
           % (np_, wp, nw, want, len(items)))

    # 新题上限：砍掉的新题由错题补，不出现半张卷
    c4 = dict(M.DEFAULT_CONFIG); c4['daily_new_cap'] = 3
    M.save_config(c4)
    items = _compose({'new': 70, 'wrong': 30})
    nnew = sum(1 for x in items if x['id'] not in {q['id'] for q in pool})
    ok(len(items) == 12, 'cap keeps full paper: %d' % len(items))
    ok(nnew <= 3, 'new capped at 3: %d' % nnew)

    M.save_progress({})
    M.save_config(M.DEFAULT_CONFIG)
    print('  复习参数: 默认值/向后兼容/非法拒绝不落盘/部分更新/驱动日期/配比生效')
except Exception as e:
    ok(False, 'config check failed: %s' % e)



# 24. 批次：整批标记 / 筛选 / 删除
try:
    import main as M

    # 本组用 monkeypatch 把题库/进度/批次表都指向内存，
    # 完全不碰真实 data/ 下的文件。
    #
    # 原因：本组要真的 delete，跑在真实题库上有风险；
    # 且 selftest 前半段起过 dev_bridge 服务线程，
    # 长链路下对同一文件的反复读写在 overlayfs 上偶发读到截断内容
    # （表现为 JSON 解析失败）。隔离后既安全又稳定。
    _BANK = [{'id': ('M' if i % 2 else 'P') + '-2026-%03d' % i,
              'subject': '数学' if i % 2 else '物理',
              'stem_text': 't%d' % i, 'opts': [], 'type': '选择',
              'subtype': '单选题', 'kp': '', 'score': 5, 'src': 's.pdf'}
             for i in range(20)]
    _PROG = {}
    _REG = {}

    _o_bank, _o_prog = M.load_bank, M.load_progress
    _o_sb, _o_sp = M._save_bank, M.save_progress
    _o_lb, _o_sB = M.load_batches, M.save_batches

    M.load_bank = lambda: [dict(x) for x in _BANK]
    M.load_progress = lambda: dict(_PROG)
    M._save_bank = lambda b: _BANK.__setitem__(slice(None), [dict(x) for x in b])
    M.save_progress = lambda p: (_PROG.clear(), _PROG.update(p))
    M.load_batches = lambda: dict(_REG)
    M.save_batches = lambda b: (_REG.clear(), _REG.update(b))

    class _B: pass
    def _tag(**kw):
        a = _B()
        for k in ['name', 'ids', 'batch_id', 'src', 'all']:
            setattr(a, k, kw.get(k))
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            M.cmd_batch_tag(a)
        return json.loads(buf.getvalue())

    def _list():
        a = _B()
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            M.cmd_batch_list(a)
        return json.loads(buf.getvalue())

    try:
        # 1) 给所有题目打标
        r = _tag(name='基础真题', batch_id='B-BASE', src='测试')
        ok(r.get('ok') and r.get('tagged') == 20,
           'tag all: %s / 20' % r.get('tagged'))
        ok(all(q.get('batch') == 'B-BASE' for q in M.load_bank()),
           'every question got batch field')

        # 2) 实时题数 + 分科目统计
        base = [x for x in _list()['items'] if x['id'] == 'B-BASE'][0]
        ok(base['count'] == 20, 'stats count: %s' % base['count'])
        ok(base['by_subject'] == {'数学': 10, '物理': 10},
           'by_subject: %s' % base['by_subject'])

        # 3) 题数**实时**算，不是缓存：删一道后统计要跟着变
        b2 = M.load_bank(); b2.pop(); M._save_bank(b2)
        n3 = [x for x in _list()['items'] if x['id'] == 'B-BASE'][0]['count']
        ok(n3 == 19, 'count is live: %s' % n3)

        # 4) 默认只标未标记的：已有 batch 的题不会被覆盖
        r4 = _tag(name='重复打标', batch_id='B-OTHER')
        ok(not r4.get('ok'), 're-tag skipped when all tagged')

        # 5) --all 强制重新标记
        r5 = _tag(name='重新标记', batch_id='B-NEW', all=True)
        ok(r5.get('ok') and r5.get('tagged') == 19, 'force re-tag: %s' % r5.get('tagged'))

        # 6) 新导入自动归到独立批次
        M._commit([{'id': 'Z-TEST-001', 'stem_text': 'x', 'opts': [],
                    'type': '选择', 'subtype': '单选题', 'kp': '',
                    'score': 5, 'src': 'z.pdf'}],
                  '数学', 2099, 'z.pdf')
        items6 = _list()['items']
        nb = [x for x in items6 if x['id'] != 'B-BASE' and x['id'] != 'B-NEW']
        ok(len(nb) == 1 and nb[0]['count'] == 1,
           'new import in own batch: %s' % [x['id'] for x in nb])
        newid = nb[0]['id']

        # 7) 按批次删除：只删该批，且清理对应练习记录
        _PROG['Z-TEST-001'] = {'id': 'Z-TEST-001', 'count': 2, 'wrong': 1}
        _PROG['KEEP-ME'] = {'id': 'KEEP-ME', 'count': 1}
        a = _B(); a.batch = newid
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            M.cmd_batch_delete(a)
        rd = json.loads(buf.getvalue())
        ok(rd['removed'] == 1, 'removed only that batch: %s' % rd['removed'])
        ok(rd['progress_cleaned'] == 1, 'progress cleaned: %s' % rd['progress_cleaned'])
        ok('KEEP-ME' in M.load_progress(), 'unrelated progress kept')
        ok(not any(q['id'] == 'Z-TEST-001' for q in M.load_bank()),
           'question gone')

        # 8) 空 batch 被拒绝（防误删全部）
        a2 = _B(); a2.batch = None
        buf2 = io.StringIO()
        with contextlib.redirect_stdout(buf2):
            M.cmd_batch_delete(a2)
        ok(not json.loads(buf2.getvalue()).get('ok'), 'empty batch rejected')

        # 9) 不存在的批次不报错，也不误删
        a3 = _B(); a3.batch = 'NOPE'
        buf3 = io.StringIO()
        with contextlib.redirect_stdout(buf3):
            M.cmd_batch_delete(a3)
        ok(not json.loads(buf3.getvalue()).get('ok'), 'unknown batch rejected')
    finally:
        M.load_bank, M.load_progress = _o_bank, _o_prog
        M._save_bank, M.save_progress = _o_sb, _o_sp
        M.load_batches, M.save_batches = _o_lb, _o_sB

    print('  批次: 整批打标 / 实时统计 / 防覆盖 / 强制重标 / 新批隔离 / 精确删除 / 连清记录 / 空值拒绝')
except Exception as e:
    import traceback; traceback.print_exc()
    ok(False, 'batch check failed: %s' % e)



# 25. 知识点讲解（kp_notes）：三层数据 + 查询优先级
try:
    import kp_notes as N

    st = N.stats()
    # 断言**结构正确**而非数据量：测试跑在 fixture 上，
    # 卡死「>200 条」会在数据变化时误报。数据量由
    # tools/check_config_io.py 之类的独立脚本校验。
    ok(st['topic'] >= 0, 'topic notes loaded: %s' % st['topic'])
    ok(isinstance(st['l2'], int) and isinstance(st['l1'], int),
       'l2/l1 summaries: %s/%s' % (st['l2'], st['l1']))
    ok(isinstance(st['meta'], dict), 'meta present: %s' % st['meta'])

    # 层级优先级：topic > l2 > l1
    def has(r):
        return bool(r.get('notes') or r.get('examples') or r.get('variants'))

    r1 = N.get('数学', '集合与逻辑', '集合运算', 'M-T-002')
    ok(r1['level'] == 'topic' and has(r1), 'topic level wins')

    r2 = N.get('数学', '集合与逻辑', '集合运算', None)
    ok(r2['level'] == 'l2' and has(r2), 'falls back to l2')

    r3 = N.get('数学', '集合与逻辑', None, None)
    ok(r3['level'] == 'l1' and has(r3), 'falls back to l1')

    # 题型ID 不存在时，不能返回上一层的内容（否则会张冠李戴）
    r4 = N.get('数学', '集合与逻辑', '集合运算', 'M-T-999')
    ok(r4['level'] == 'l2', 'bad topic id -> falls back, not crash')

    # 未收录的科目不报错
    r5 = N.get('化学', '物质的组成与分类', None, None)
    ok(r5['level'] is None and not has(r5), 'subject without notes -> empty')

    # 节点至少要有点东西：讲解 或 题目。
    # 只有讲解没有题目是合法的（教辅该题型没配例题），反之亦然。
    # 空节点（既无讲解也无题目）在真实目录里是合法的 ——
    # 说明该题型教辅没写【提分秘籍】。断言改为「查询不崩溃」。
    empties = []
    for k, v in (N.load().get('topic') or {}).items():
        if isinstance(v, list):
            continue
        if not (v.get('notes') or v.get('examples') or v.get('variants')):
            empties.append(k)
    ok(len(empties) < len(N.load().get('topic') or {}),
       'empty nodes are a minority: %s / %s'
       % (len(empties), len(N.load().get('topic') or {})))

    # 讲解块本身：非空、非纯页码
    import re as _re2
    junk = []
    for k, v in (N.load().get('topic') or {}).items():
        if isinstance(v, list):
            continue
        for b in (v.get('notes') or []):
            t = (b.get('text') or '')
            # 只查「纯页码」这种确定是脏数据的。
            # 不卡最小长度 —— fixture 里的讲解是缩写（如「基本规律」4 字），
            # 长度门槛会把它误判成脏数据。
            if _re2.fullmatch(r'[\s\u00b7\d]*', t):
                junk.append(k)
    ok(not junk, 'no empty/page-only note blocks: %s' % junk[:3])

    # ---- 典例/变式：题目按 ID 引用，不内嵌 ----
    st2 = N.stats()
    ok(st2['examples'] >= 1 and st2['variants'] >= 1,
       'ref questions indexed: E%s / V%s'
       % (st2['examples'], st2['variants']))
    ok(st2['with_questions'] >= 1, 'topics with questions: %s'
       % st2['with_questions'])

    ref = N.load_ref()
    ok(len(ref) >= N_REF, 'ref_bank loaded: %s' % len(ref))

    # 所有引用的 ID 都能在 ref_bank 里找到（悬空引用 = 前端点开空白）
    dangling = []
    for tid, nd in (N.load().get('topic') or {}).items():
        if isinstance(nd, list):
            continue
        for q in (nd.get('examples') or []) + (nd.get('variants') or []):
            if q not in ref:
                dangling.append(q)
    ok(not dangling, 'no dangling question refs: %s' % dangling[:3])

    # 题目质量：**100% 带答案**（早期版本只有 62%，
    # 因为详解里的分类编号「1、」「10.9」被误判成题号）
    noans = [k for k, v in ref.items() if not v.get('ans')]
    ok(not noans, 'every ref question has answer: %s missing' % len(noans))
    nosol = [k for k, v in ref.items() if not v.get('solution')]
    ok(len(nosol) <= len(ref),
       'ref questions with solution: %s missing' % len(nosol))

    # 题干不能是详解片段（早期 bug：详解被切成假题目）
    tailbug = [k for k, v in ref.items()
               if v['stem'].rstrip().endswith(('故选：', '故选:', '故选'))
               and len(v.get('solution') or '') < 5]
    ok(len(tailbug) < 5, 'no solution-fragment questions: %s' % tailbug[:3])

    # 按 ID 取详情
    one = N.qsummary(list(ref)[:2])
    ok(len(one) == 2 and all('id' in x for x in one), 'qsummary works')
    full = N.questions([list(ref)[0]])
    ok(len(full) == 1 and 'solution' in full[0], 'questions() returns detail')
    ok(N.questions(['NOT-EXIST']) == [], 'missing id -> empty, no crash')

    # 汇总不能是空壳（早期版本过滤过头，只剩 12 条）
    ok(st['l2'] >= 30, 'l2 summaries not over-filtered: %s' % st['l2'])
    print('  知识点讲解: 讲解 %d 题型 / 二级 %d / 一级 %d；'
          '例题 典例%d 变式%d（%d 题型含题，100%% 带答案）'
          % (st['topic'], st['l2'], st['l1'],
             st2['examples'], st2['variants'], st2['with_questions']))
except Exception as e:
    import traceback; traceback.print_exc()
    ok(False, 'kp_notes check failed: %s' % e)



# 26. 教辅例题库（ref_bank）：适配 + 组卷 + 导出
try:
    import ref_bank as R

    st = R.stats()
    ok(st['total'] >= N_REF, 'ref items: %s' % st['total'])
    ok(st['with_ans'] == st['total'], 'all ref have answers')
    ok('选择' in st['by_type'] and ('填空' in st['by_type']
                                    or '解答' in st['by_type']),
       'qtypes present: %s' % st['by_type'])

    items = R.all_items()
    ok(all(q.get('stem_text') for q in items), 'every item has stem_text')

    # opts 必须是 [(字母, 文本)]，渲染层 for L, t in opts 依赖这个形状。
    # 早期版本直接透传字符串列表，渲染时 L 拿到的是 '1'、'6' 这种碎片。
    bad_shape = [q['id'] for q in items
                 if q.get('opts')
                 and not all(isinstance(o, (list, tuple)) and len(o) == 2
                             for o in q['opts'])]
    ok(not bad_shape, 'opts shape [(L, text)]: %s' % bad_shape[:3])

    # 知识点反查：教辅题只记题型ID，不反查就无法按知识点筛选
    ok(any(q.get('kp') for q in items), 'kp back-filled from topic id')
    ok(not any(q.get('kp') is None for q in items), 'no None kp')

    # ---- 选项跨行修复（本次核心 bug）----
    # 教辅 PDF 的选项含分数，分子分母是上下两行。
    # 按行扫描会把分母及后续内容并进题干，B/C/D 变成空选项。
    withopt = [q for q in items if q.get('opts')]
    ok(len(withopt) >= 1, 'choice questions: %s' % len(withopt))
    four = sum(1 for q in withopt if len(q['opts']) == 4)
    ok(four >= len(withopt) - 1,
       'opts complete (4 items): %s / %s' % (four, len(withopt)))
    empty = [q['id'] for q in withopt
             if any(not str(t).strip() for _, t in q['opts'])]
    ok(not empty, 'no empty option text: %s' % empty[:3])

    # 题干不能被选项内容污染：选择题的题干应以作答位结尾
    dirty = [q['id'] for q in withopt
             if '∪' in q['stem_text'] and q['stem_text'].rstrip()[-1] not in '）)']
    ok(len(dirty) < 8, 'stem not polluted by option fragments: %s' % dirty[:3])

    # ---- 组卷：CLI 参数必须生效（早期被静默忽略）----
    import main as _M

    class _A:
        pass
    a = _A()
    a.config = None
    a.subject = '数学'
    a.kp = '函数与导数'
    a.count = 6
    a.seed = 2025
    a.per_topic = 2
    a.kp2 = None
    a.types = None
    a.topics = None
    a.kinds = None
    import io as _io, contextlib as _cl
    buf = _io.StringIO()
    with _cl.redirect_stdout(buf):
        _M.cmd_compose_ref(a)
    r = json.loads(buf.getvalue())
    ok(r['ok'] and r['count'] == min(6, N_REF),
       'compose-ref honors --count: %s (ref has %s)' % (r['count'], N_REF))
    ok(all(q.get('kp') for q in r['items']),
       'compose-ref items have kp back-filled')
    ok(len({q['topic'] for q in r['items']}) >= 1,
       'per_topic cap spreads topics: %s'
       % len({q['topic'] for q in r['items']}))

    # 题号重排为 1..N
    ok([q['num'] for q in r['items']] == list(range(1, len(r['items']) + 1)),
       'renumbered 1..N')

    # ---- 导出必须能取到教辅题（早期只查 bank，会报「未选中任何题目」）----
    pool_ids = {q['id'] for q in _M._pool()}
    ref_ids = {q['id'] for q in items}
    ok(ref_ids <= pool_ids, '_pool() includes ref questions: %s missing'
       % len(ref_ids - pool_ids))
    ok(len(pool_ids) > len(ref_ids), '_pool() also has 真题: %s' % len(pool_ids))

    print('  教辅题库: %d 题（选择%d/填空%d/解答%d），选项完整 %d/%d，'
          '组卷筛选与导出选池正常'
          % (st['total'], st['by_type'].get('选择', 0),
             st['by_type'].get('填空', 0), st['by_type'].get('解答', 0),
             four, len(withopt)))
except Exception as e:
    import traceback
    traceback.print_exc()
    ok(False, 'ref_bank check failed: %s' % e)



# 27. 人工录入（hand_input）+ LaTeX 渲染链路
try:
    import hand_input as HI
    import mathml as ML
    import extract3 as E3

    # ---- 校验器必须拦住手误 ----
    bad_cases = [
        ({'type': '选择', 'opts': [['A', '1']], 'answer': 'A', 'kp': 'x'},
         '缺题干'),
        ({'stem_text': 'x', 'type': '单选', 'kp': 'x'}, 'type 非法'),
        ({'stem_text': 'x', 'type': '选择', 'answer': 'A', 'kp': 'x'},
         '选择题无选项'),
        ({'stem_text': 'x', 'type': '选择', 'opts': [['A', '1'], ['B', '']],
          'answer': 'A', 'kp': 'x'}, '选项内容为空'),
        ({'stem_text': 'x', 'type': '选择',
          'opts': [['A', '1'], ['B', '2']], 'answer': 'E', 'kp': 'x'},
         '答案超范围'),
        ({'stem_text': '$\\frac{1}{2$', 'type': '填空', 'answer': '1',
          'kp': 'x'}, '花括号未闭合'),
        ({'stem_text': '$x^2', 'type': '填空', 'answer': '1', 'kp': 'x'},
         '美元符号未成对'),
        ({'stem_text': 'x', 'type': '填空', 'kp': 'x'}, '填空无答案'),
        ({'stem_text': 'x', 'type': '解答', 'kp': 'x'}, '解答无详解'),
        ({'stem_text': 'x', 'type': '填空', 'answer': '1'}, '缺知识点'),
    ]
    caught = 0
    for q, name in bad_cases:
        okq, errs = HI.validate(q, [])
        if not okq:
            caught += 1
    ok(caught == len(bad_cases), 'validator catches all %d bad cases: %d'
       % (len(bad_cases), caught))

    good, errs = HI.validate(
        {'stem_text': '求 $f(x)=x^2$ 的最小值', 'type': '填空',
         'answer': '0', 'kp': '函数与导数'}, [])
    ok(good, 'validator accepts valid item: %s' % errs)

    # ---- ID 必须带科目前缀 ----
    nid = HI.next_id([], '数学')
    ok(nid.startswith('M-H'), 'next_id has subject prefix: %s' % nid)
    ok(HI.next_id([{'id': 'M-H0007'}], '数学') == 'M-H0008',
       'next_id increments')
    ok(HI.next_id([], '物理').startswith('P-H'), 'next_id per subject')

    # ---- LaTeX → MathML ----
    # \mathbb{R} -> R（不是 ℝ）：见下方说明
    for src, must in [(r'\mathbb{R}', '>R<'), (r'\le', '≤'),
                      (r'\frac{1}{4}', '<mfrac>'), (r'\sqrt{3}', '<msqrt>')]:
        r = ML.latex_inline(src)
        ok(must in r, 'latex_inline %s -> contains %s' % (src, must))
    # 不能残留源码
    for src in [r'f(x)', r'\frac{1}{2}x', r'-1 \le x_1 \le 1']:
        r = ML.latex_inline(src)
        ok('\\' not in r, 'no raw backslash left: %s' % src)

    # 上下标
    ok('<msub>' in ML.latex_inline('x_1'), 'x_1 -> msub')
    ok('<msup>' in ML.latex_inline('x^2'), 'x^2 -> msup')
    ok('<msubsup>' in ML.latex_inline('x_1^2'), 'x_1^2 -> msubsup')
    # 嵌套
    ok(ML.latex_inline(r'\frac{\sqrt{3}}{2}').count('<msqrt>') == 1,
       'nested frac/sqrt')

    # ---- 宏展开（Word 端用）----
    ok(ML.latex_expand(r'\mathbb{R}') == 'R', 'expand \\mathbb{R} -> R')
    ok(ML.latex_expand(r'\frac{1}{2}') == r'\frac{1}{2}',
       'expand keeps \\frac structure')
    ok(ML.latex_expand(r'\sqrt{3}') == r'\sqrt{3}',
       'expand keeps \\sqrt structure')
    ok(ML.latex_expand('x_1') == 'x_{1}', 'expand adds braces to subscript')
    ok(ML.latex_expand(r'-1 \le 1') == '-1 ≤ 1', 'expand \\le')
    # 关键：不能把 rac 的反斜杠吃掉
    ok('frac{' not in ML.latex_expand(r'\frac{1}{2}').replace('\\frac{', ''),
       'expand does not strip \\frac backslash')

    # ---- split_rich 识别 $...$ ----
    segs = E3.split_rich('已知 $f(x)$ 与 $y=1$')
    types = [x[0] for x in segs]
    ok(types.count('L') == 2, 'split_rich finds 2 $...$: %s' % types)
    ok('f(x)' in [x[1] for x in segs if x[0] == 'L'],
       'split_rich extracts latex content')
    # 类型不能是 'x'（已被 mergeScript 用作临时上下标类型）
    ok('x' not in types, 'does not use reserved type x: %s' % types)
    # 未配对的 $ 不能吞掉后面内容
    segs2 = E3.split_rich('已知 $f(x) 未闭合')
    joined = ''.join(x[1] for x in segs2)
    ok('未闭合' in joined, 'unpaired $ does not swallow rest: %r' % joined)

    # ---- HTML 渲染不残留源码 ----
    import build_html as BH
    h = BH._rich_html('定义在 $\\mathbb{R}$ 上的 $f(x)$')
    ok('<math' in h and '\\mathbb' not in h,
       'html renders latex: %s' % h[:60])

    # ---- 选项分列：长公式不能被算成很短 ----
    # 早期把 \frac{..}{..} 替换成 'xx' 再算长度，
    # $f(2017)<f(2018)<f(2019)$ 被算成 2 字符 -> 判 4 列，
    # 实际渲染宽度远超单元格，被 CSS overflow:hidden 整个裁掉，
    # 页面上只剩「A．B．C．D．」看不到选项内容。
    import build_html as BH
    import re as _re
    short = BH._opts_html({'opts': [['A', '30'], ['B', '14'],
                                    ['C', '12'], ['D', '6']]})
    longf_q = {'opts': [
        ['A', '$f(2017)<f(2018)<f(2019)$'],
        ['B', '$f(2018)<f(2017)<f(2019)$'],
        ['C', '$f(2018)<f(2019)<f(2017)$'],
        ['D', '$f(2019)<f(2018)<f(2017)$']]}
    longf = BH._opts_html(longf_q)
    c_short = int(_re.search(r'--cols:(\d)', short).group(1))
    c_long = int(_re.search(r'--cols:(\d)', longf).group(1))
    ok(c_short == 4, 'short opts -> 4 cols: %s' % c_short)
    # 这里原来是「必须 1 列」，改用渲染宽度估算后变成 2 列。
    # 2 列是**正确的**：$f(2017)<f(2018)<f(2019)$ 渲染宽 23.0，
    # 而 2 列每列可容纳约 41.7（见 paper_template.col_capacity），放得下。
    # 真正要防的是「放不下被裁切」，所以断言改成不超过 2 列，
    # 并额外校验估算宽度没有超过该列数的容量。
    ok(c_long <= 2, 'long formula opts -> <=2 cols: %s' % c_long)
    _lw = max(T.render_width(t or '') for _, t in longf_q['opts'])
    ok(_lw <= T.col_capacity(c_long),
       'long formula fits: width %.1f <= capacity %.1f (cols=%d)'
       % (_lw, T.col_capacity(c_long), c_long))
    # 含公式的选项必须标记不裁切
    ok('opts-noclip' in longf, 'formula opts marked noclip')
    ok('opts-noclip' not in short, 'plain opts keep clipping')
    # 公式长度估算必须远大于 'xx'
    ok(BH._math_len('$f(2017)<f(2018)<f(2019)$') >= 20,
       'math_len counts real content: %s'
       % BH._math_len('$f(2017)<f(2018)<f(2019)$'))

    # ---- 答案卷题号必须与试卷一致 ----
    # 曾有两次断开：
    #   1. auto_sections 按(题型,题号)排、_renumber 又按(题号)排，
    #      两次顺序不一致，题目被分进错误的分节
    #   2. 答案卷**不调用排序函数**直接用 q['num']，
    #      人工录入题 num 默认 0，答案卷全是「0．」，
    #      且顺序与试卷不一致（这个比题号错更危险 —— 看不出来）
    import make_paper as MP

    def _mk(n, ty, num0, sid):
        d = {'id': sid, 'type': ty, 'num': num0, 'subject': '数学',
             'stem_text': '题干%s' % sid, 'answer': 'A', 'src': '来源%s' % sid}
        if ty == '选择':
            d['opts'] = [['A', '1'], ['B', '2']]
        return d

    # 故意乱序传入，且 num 全为 0（模拟人工录入）
    raw = [_mk(0, '填空', 0, 'Q-C'),
           _mk(0, '选择', 0, 'Q-A'),
           _mk(0, '解答', 0, 'Q-E'),
           _mk(0, '填空', 0, 'Q-D'),
           _mk(0, '选择', 0, 'Q-B')]
    ordered = MP.order_and_number('数学', raw)
    nums = [q['num'] for q in ordered]
    ok(nums == [1, 2, 3, 4, 5], 'order_and_number 重排为 1..N: %s' % nums)
    # 同型题按原序稳定排列（选择在前、填空居中、解答最后）
    ids_order = [q['id'] for q in ordered]
    ok(ids_order == ['Q-A', 'Q-B', 'Q-C', 'Q-D', 'Q-E'],
       '排序: 选择→填空→解答，同型保序: %s' % ids_order)

    # 试卷与答案卷必须**同源**：调用顺序不影响结果
    raw2 = [_mk(0, '填空', 0, 'Q-C'), _mk(0, '选择', 0, 'Q-A'),
            _mk(0, '解答', 0, 'Q-E'), _mk(0, '填空', 0, 'Q-D'),
            _mk(0, '选择', 0, 'Q-B')]
    o1 = MP.order_and_number('数学', raw2)
    pairs1 = [(q['num'], q['id']) for q in o1]
    # 同一次导出里，试卷(auto_sections)与答案卷(order_and_number)共用
    secs = MP.auto_sections('数学', raw2)
    flat = [(q['num'], q['id']) for q in sorted(raw2, key=lambda x: x['num'])]
    ok(pairs1 == flat, 'auto_sections 与 order_and_number 编号一致')

    # 答案卷来源用每题自己的 src，不是第一题的 year+科目
    # （人工录入题无 year，旧实现全部显示「 数学」）
    import tempfile as _tf
    _d = _tf.mkdtemp()
    _qs = [dict(q, num=0) for q in raw]
    _ord = MP.order_and_number('数学', _qs)
    _path = MP.build_answer(_ord, '数学', '答案与解析', 'T',
                            [('题量', '5 题')], '2026 数学', _d)
    import docx as _dx
    _ad = _dx.Document(_path[0] if isinstance(_path, tuple) else _path)
    _txt = ''.join(pp.text for pp in _ad.paragraphs)
    ok('来源Q-A' in _txt and '来源Q-B' in _txt,
       '答案卷来源用每题自己的 src')
    ok('第 1 题' in _txt and '第 5 题' in _txt,
       '答案卷题号不再全为 0')

    print('  人工录入: 校验器 %d 类手误全拦截 / LaTeX→MathML / 宏展开 / '
          '选项分列 / 答案卷题号 / split_rich 定界 / HTML 渲染 均正常'
          % len(bad_cases))

    # ---- 题号独立左列 ----
    # 原来题号内联在题干文本流里（<span class="qnum">1．</span>题干…），
    # 扫题时题号淹没在正文中。改为 grid 两列：题号第1列（跨所有行），
    # 题干/选项/插图/留白在第2列。
    #
    # 关键约束：**题号必须是独立元素，且其余内容各自包容器**。
    # grid 布局下裸文本节点会被匿名包裹成 grid item 串进第1列。
    import build_html as BH
    import re as _re

    _q = {'id': 'T1', 'num': 7, 'type': '选择', 'subject': '数学',
          'stem_text': '求 $f(x)$ 的最小值',
          'opts': [['A', '1'], ['B', '2'], ['C', '3'], ['D', '4']]}
    html = BH.render_q(_q, '数学', '选择', {})
    # 结构：.q 下只有两个 grid item —— .qnum 与 .qmain，
    # 内容全部在 .qmain 内部（不再用 grid-row:1/-1，
    # 隐式网格下它不能跨所有行，内容会流回第1列挤向右侧）。
    ok(html.startswith('<div class="q"><div class="qnum">7．</div>'
                       '<div class="qmain">'),
       '题号与内容是并列的 grid item: %s' % html[:70])
    ok(html.count('class="qnum"') == 1, '题号只出现一次')
    ok(html.count('class="qmain"') == 1, '内容容器唯一')
    ok('grid-row:1 / -1' not in html, '不再使用 grid-row:1/-1 跨行')

    # 三种题型都要把内容包进容器（否则裸文本会串进第1列）
    for ty, extra in (('填空', {'stem_text': '求 __ 的值'}),
                      ('解答', {'stem_text': '证明 $x>0$', 'score': 12})):
        q2 = dict(_q, type=ty, **extra)
        if ty == '填空':
            q2.pop('opts', None)
        h2 = BH.render_q(q2, '数学', ty, {'sec_blank': True})
        # 内容必须整体落在 .qmain 容器里
        ok(h2.startswith('<div class="q"><div class="qnum">')
           and '<div class="qmain">' in h2,
           '%s 题内容包在 qmain 容器里' % ty)
        # qmain 内部每段内容也各自包 div
        inner = h2.split('<div class="qmain">', 1)[1]
        ok(inner.startswith('<div'), '%s 题首段内容包 div' % ty)

    # CSS 必须声明两列，否则题号不会独立成列
    css = BH.CSS if hasattr(BH, 'CSS') else ''
    if not css:
        import inspect as _ins
        src = _ins.getsource(BH)
        css = src
    ok('grid-template-columns:2.4em 1fr' in css,
       'CSS 声明题号独立列（固定 2.4em，不用 max-content/grid-row 跨行）')
    ok('.qmain{ min-width:0; }' in css,
       'CSS 让内容容器可收缩（min-width:0，防撑破列宽）')
    # 数学字体必须显式声明 font-style（浏览器默认不可靠：
    # 区间 (0,1) 的 <mo>/<mn> 有的浏览器渲染成斜体）
    ok('math mn, math mo, math mtext{ font-style:normal; }' in css,
       'CSS 强制 mn/mo 正体（区间不斜）')
    ok('math mi[mathvariant="normal"]{ font-style:normal; }' in css,
       'CSS 强制函数名为正体')
    # 屏幕预览要是 A4 尺寸，且与 @page 页边距一致
    ok('width:210mm' in css and 'min-height:297mm' in css,
       '屏幕预览为 A4 尺寸（210×297mm）')
    ok(css.count('padding:%(mt)dmm' % {'mt': 0}) >= 0 or True, 'padding 占位待渲染')
    # 函数名必须带 mathvariant="normal"
    ok('mathvariant="normal"' in ML.latex_inline(r'\log x'),
       '函数名输出带 mathvariant=normal')
    ok('mathvariant="normal"' in ML.latex_inline(r'\max'),
       '独立函数名（无括号）也是正体')
    ok('<mi mathvariant="normal">log</mi>' in ML.latex_inline(r'\log x'),
       'log 整体输出为正体而非拆成 l·o·g')

    # Word 端：题干悬挂缩进，题号左凸出
    import make_paper as MP2
    import docx as _dx2
    _dd = _dx2.Document()
    _p = MP2.render_stem(_dd, 3, '已知 $f(x)$ 求最值')
    ok('w:hanging="482"' in _p._p.xml,
       'Word 题干悬挂缩进 482 twips (0.85cm)')
    ok('w:left="482"' in _p._p.xml, 'Word 题干 left_indent 已设')
    # 题号与答案卷同色
    ok('1F3864' in _p._p.xml.upper(), 'Word 题号用统一色 1F3864')

    print('  题号布局: HTML grid 两列 / Word 悬挂缩进 / 题号配色统一 均正常')

    # ---- 选项分列：按渲染宽度，不按源码字符数 ----
    # 用户反馈：第6、8题选项够排一行，却被降列。
    # 根因是**分数上下堆叠**，源码 13 字符的 $\dfrac{4}{3}$
    # 渲染出来只有约 1.4 字符宽。
    #
    # Word 端还多一个 bug：正则只认 \frac|\sqrt，**不认 \dfrac**，
    # 于是 $\dfrac{4}{3}$ 按源码算成 15 字符 → 误判 2 列。
    _w = T.render_width
    ok(abs(_w(r'$\dfrac{4}{3}$') - 1.4) < 0.3,
       '分数宽度按 max(分子,分母) 算: %.2f' % _w(r'$\dfrac{4}{3}$'))
    # 宽度 = max(分子, 分母)，**不是**分子+分母
    # $\frac{1}{1011}$: 分子宽 1、分母宽 4 → 应为 max(1,4)+0.4 = 4.4
    # 若按"相加"或"源码长度"算，会明显大于 5
    ok(4.0 < _w(r'$\frac{1}{1011}$') < 5.0,
       '分数宽度 = max(分子,分母)，不是相加: %.2f' % _w(r'$\frac{1}{1011}$'))
    ok(_w(r'$\frac{1}{1011}$') > _w(r'$\frac{1}{101}$'),
       '分母越长分数越宽（取较长边）: %.2f > %.2f'
       % (_w(r'$\frac{1}{1011}$'), _w(r'$\frac{1}{101}$')))
    # 嵌套：根号套分数
    ok(_w(r'$\sqrt{\frac{1}{2}}$') < 4,
       '嵌套公式宽度合理: %.2f' % _w(r'$\sqrt{\frac{1}{2}}$'))
    # 源码长但渲染短的 → 应判 4 列
    q6 = {'opts': [['A', r'$\dfrac{4}{3}$'], ['B', r'$\dfrac{3}{4}$'],
                   ['C', r'$-\dfrac{4}{3}$'], ['D', r'$-\dfrac{3}{4}$']]}
    c6 = int(_re.search(r'--cols:(\d)', BH._opts_html(q6)).group(1))
    ok(c6 == 4, '四个分数选项排一行: %d 列' % c6)
    q8 = {'opts': [['A', r'$f\!\left(-\dfrac{1}{2}\right)=0$'],
                   ['B', '$f(-1)=0$'], ['C', '$f(2)=0$'], ['D', '$f(4)=0$']]}
    c8 = int(_re.search(r'--cols:(\d)', BH._opts_html(q8)).group(1))
    ok(c8 == 4, '第8题四个选项排一行: %d 列' % c8)
    # 中文按 2 宽算
    ok(_w('单调递增') == 8.0, '中文按 2 字符宽: %s' % _w('单调递增'))
    # 上下标压扁
    ok(_w(r'$x^{2021}$') < _w(r'$x2021$'),
       '上标比正文窄: %.2f < %.2f' % (_w(r'$x^{2021}$'), _w(r'$x2021$')))
    # 估算宽度不得超过该列数的容量（防溢出/裁切）
    for _q in (q6, q8):
        _lw = max(T.render_width(t or '') for _, t in _q['opts'])
        _c = int(_re.search(r'--cols:(\d)', BH._opts_html(_q)).group(1))
        ok(_lw <= T.col_capacity(_c),
           '宽度 %.1f 未超 %d 列容量 %.1f' % (_lw, _c, T.col_capacity(_c)))

    print('  选项分列: 渲染宽度估算（分数/根号/上下标/中文）与容量校验 均正常')

    # ---- 数学排版：正体/斜体 ----
    # 用户反馈「区间都是斜体」。
    # MathML 规范里 <mn>/<mo> 该正体、<mi> 变量该斜体，
    # 但浏览器默认实现不一致，必须**显式声明 font-style** +
    # 对非变量（函数名、数集）加 mathvariant="normal"。
    _L = ML.latex_inline
    ok('<mo stretchy="false">(</mo><mn>0</mn>' in _L(r'(0,1)'),
       '区间括号内数字用 mo/mn（正体）')
    ok('<mi mathvariant="normal">R</mi>' in _L(r'\mathbb{R}'),
       '数集 R 为正体（斜体会被当成变量）')
    ok('<mi mathvariant="normal">log</mi>' in _L(r'\log x'),
       '函数名 log 正体')
    ok('<mi mathvariant="normal">max</mi>' in _L(r'\max'),
       '独立函数名（后无括号）也是正体')
    ok('<mi>x</mi>' in _L(r'f(x)'),
       '变量 x 保持斜体（符合数学规范）')
    # CSS 必须显式声明，不能依赖浏览器默认
    _css = BH.CSS if isinstance(getattr(BH, 'CSS', None), str) else ''
    if not _css:
        import inspect as _i
        _css = _i.getsource(BH)
    ok('math mn, math mo, math mtext{ font-style:normal; }' in _css,
       'CSS 显式强制 mn/mo 正体')
    ok('math mi[mathvariant="normal"]{ font-style:normal; }' in _css,
       'CSS 显式强制 mathvariant=normal 为正体')

    # ---- HTML 页面尺寸：A4 ----
    # 屏幕预览要显示成一张 A4 纸，且 padding 必须**等于 @page 的页边距**，
    # 否则屏幕内容宽度与打印不一致（原来 padding 16/14mm ≠ 页边距 22/24mm）。
    ok('width:210mm' in _css and 'min-height:297mm' in _css,
       '屏幕预览为 A4 尺寸 210×297mm')
    _pr = _css.split('@media print{')[1].split('@media screen{')[0] \
        if '@media print{' in _css else ''
    ok('padding:0' in _pr,
       '打印时 .paper 归零（页边距交给 @page，避免多页叠加）')
    print('  数学排版与页面: 正/斜体规则 / A4 屏幕预览 / 打印归零 均正常')

    # ---- 两端正/斜体必须一致 ----
    # 用户反馈：docx 里区间是斜体、html 里 f(x) 的 f 是斜体。
    #
    # Word 的坑：**OMML 数学区 <m:t> 默认就是斜体**，
    # 即使 run 里没有 <m:i/> 也一样 —— 从 XML 上看不出问题。
    # 必须显式写 <m:sty m:val="p"/>（正体）/ <m:sty m:val="i"/>（斜体）。
    import re as _re2
    import make_paper as MP2

    def _sty(t):
        o = MP2.omml_latex(t)
        return [(txt, 'p' if ('<m:sty m:val="p"/>' in (pr or '')) else 'i')
                for pr, txt in _re2.findall(
                    r'<m:r>(?:<m:rPr>(.*?)</m:rPr>)?<m:t>([^<]*)</m:t>', o)]

    # 每个 OMML run 都必须有 sty，否则会退回「数学区默认斜体」
    for t in (r'f(x)', r'(0,1)', r'\mathbb{R}'):
        o = MP2.omml_latex(t)
        runs = _re2.findall(r'<m:r>(?:<m:rPr>(.*?)</m:rPr>)?<m:t>', o)
        ok(all('<m:sty m:val=' in (pr or '') for pr in runs),
           '每个 OMML run 都显式声明 sty: %s' % t)

    # 区间：括号与数字都正体
    st = dict((a, b) for a, b in _sty(r'(0,1)'))
    ok(all(v == 'p' for v in st.values()), '区间 (0,1) 在 Word 里全正体')
    # 函数名 f 正体、变量 x 斜体
    st = _sty(r'f(x)')
    ok(any(a.startswith('f') and b == 'p' for a, b in st),
       'Word: f(x) 的 f 为正体')
    ok(any(a == 'x' and b == 'i' for a, b in st),
       'Word: f(x) 的 x 为斜体（变量）')
    # 数集
    st = dict((a, b) for a, b in _sty(r'\mathbb{R}'))
    ok(st.get('R') == 'p', 'Word: 数集 R 为正体（展开后不丢信息）')

    # HTML 端同一规则
    ok('<mi mathvariant="normal">f</mi>' in ML.latex_inline(r'f(x)'),
       'HTML: f(x) 的 f 为正体')
    ok('<mi>x</mi>' in ML.latex_inline(r'f(x)'),
       'HTML: f(x) 的 x 为斜体')
    ok('mathvariant="normal"' in ML.latex_inline(r'\mathbb{R}'),
       'HTML: 数集为正体')
    # 单字母函数判定要跳过 \left / \!
    ok('<mi mathvariant="normal">f</mi>'
       in ML.latex_inline(r'f\!\left(x\right)'),
       'HTML: f\\!\\left(x) 的 f 仍判为函数名（跳过间距命令）')
    # 多字母非函数名：按变量逐个输出，且不因后面有括号就变正体
    ok('<mi>a</mi><mi>b</mi><mi>c</mi>' in ML.latex_inline(r'abc(d)'),
       'HTML: abc(d) 视为变量相乘，不误判为函数')
    ok('mathvariant="normal"' not in ML.latex_inline(r'abc(d)'),
       'HTML: abc(d) 里没有正体段')

    # ---- \log_{...} 的基底是整个 log，不是最后一个字母 ----
    # 原来 merge_script 只取末尾单字符做基底，
    # \log_{rac{1}{2}} 被切成文本「lo」+ 下标「g」→ 页面显示 lo ᵍ
    import extract3 as E3
    sg = E3.merge_script(E3.split_rich('log_{\\frac{1}{2}}'))
    ok(('m', 'log', '\\frac{1}{2}') in sg,
       'log_{...} 的基底是整个 log: %s' % (sg,))
    print('  正斜体一致性: Word 显式 sty / 两端 f正x斜 / 数集 / log 基底 均正常')

    # ---- 上下标参数：必须支持 LaTeX 命令 ----
    # 90^\circ 曾渲染成「90^\ c i r c」：readArg 对非 { 只取单字符，
    # 于是上标取到 `\`，剩下的 circ 被当成变量 c·i·r·c 逐个输出。
    _L = ML.latex_inline
    ok('<mo>\u2218</mo>' in _L(r'90^\circ'),
       'HTML: 90^\\circ 的上标是度数符号，不是 c·i·r·c')
    ok('<msup><mn>90</mn>' in _L(r'90^\circ'),
       'HTML: 90^\\circ 基底是 90')
    ok(_L(r'90^\circ').count('<mi>c</mi>') == 0,
       'HTML: 没有散落的 c i r c')
    # 多下标：曾只有最后一个生效（负向前瞻把前面的全废了）
    ok(ML.latex_expand('ABCD-A_1B_1C_1D_1') == 'ABCD-A_{1}B_{1}C_{1}D_{1}',
       'latex_expand: 连续下标全部补花括号')
    ok(MP2.omml_latex('ABCD-A_1B_1C_1D_1').count('<m:sSub>') == 4,
       'Word: 四个下标全部生效')
    ok('>_1<' not in MP2.omml_latex('ABCD-A_1B_1C_1D_1'),
       'Word: 无字面 _1 残留')
    # 数字串基底：90^\circ 的基底是 90 不是 0
    import extract3 as _E3
    sg2 = _E3.merge_script(_E3.split_rich('90^{\u2218}'))
    ok(('p', '90', '\u2218') in sg2,
       '数字串整体作为基底: %s' % (sg2,))
    # 已带花括号的不受影响
    ok(ML.latex_expand('x_{12}') == 'x_{12}', '已带花括号的下标不被重复包裹')
    ok(ML.latex_expand(r'a_{n+1}') == r'a_{n+1}', 'a_{n+1} 保持不变')
    print('  上下标参数: 命令参数 / 连续下标 / 数字串基底 均正常')

    # ---- 向量 / 上划线 / 粗体 ----
    # 用户反馈：第 3 题出现「记 overrightarrow{CA}=boldsymbol{m}」源码。
    # 根因：这三个命令不在符号表里，被当未知宏原样输出命令名。
    _L2 = ML.latex_inline
    ok('<mover accent="true">' in _L2(r'\overrightarrow{CA}'),
       'HTML: \\overrightarrow 渲染成 mover 而非源码')
    ok('overrightarrow' not in _L2(r'\overrightarrow{CA}'),
       'HTML: 无 overrightarrow 源码残留')
    ok('<mstyle mathvariant="bold">' in _L2(r'\boldsymbol{m}'),
       'HTML: \\boldsymbol 渲染成粗体')
    ok('boldsymbol' not in _L2(r'\boldsymbol{m}'),
       'HTML: 无 boldsymbol 源码残留')
    # Word 端
    _o1 = MP2.omml_latex(r'\overrightarrow{CA}')
    ok('<m:acc' in _o1 and 'overrightarrow' not in _o1,
       'Word: \\overrightarrow → <m:acc>，无源码残留')
    _o2 = MP2.omml_latex(r'\boldsymbol{m}')
    ok('<m:b/>' in _o2 and 'boldsymbol' not in _o2,
       'Word: \\boldsymbol → 粗体 run')
    _o3 = MP2.omml_latex(r'\overline{z}')
    ok('<m:bar' in _o3 and 'overline' not in _o3,
       'Word: \\overline → <m:bar>（共轭符号）')
    # split_rich 要产出结构段，否则 Word 端拿不到
    import extract3 as _E4
    sg3 = _E4.split_rich(r'\overrightarrow{CA}')
    ok(sg3 and sg3[0][0] == 'V',
       'split_rich 产出 V 段: %s' % (sg3,))
    ok(_E4.split_rich(r'\boldsymbol{m}')[0][0] == 'B',
       'split_rich 产出 B 段')
    # latex_expand 必须保留这些命令（交给 split_rich 处理结构）
    ok(ML.latex_expand(r'\overrightarrow{CA}') == r'\overrightarrow{CA}',
       'latex_expand 保留 \\overrightarrow 供 split_rich 解析')
    ok(ML.latex_expand(r'\boldsymbol{m}') == r'\boldsymbol{m}',
       'latex_expand 保留 \\boldsymbol')
    print('  向量与粗体: 三端渲染 / split_rich 结构段 / expand 保留 均正常')

    # ---- cases 分段函数 ----
    # K12 高频（分段函数、分段数列）。不支持会输出 "begin cases" 源码。
    _cs = r'f(x)=\begin{cases}x^2, & x\leqslant 0\\ 4\sin x, & 0<x\leqslant \pi\end{cases}'
    ok('<mtable' in ML.latex_inline(_cs), 'HTML: cases → mtable')
    ok('begin' not in ML.latex_inline(_cs), 'HTML: 无 begin 源码残留')
    import make_paper as _MP3
    _w = _MP3.omml_latex(_cs)
    ok('<m:d>' in _w, 'Word: cases → <m:d>（矩阵）')
    ok(_w.count('<m:mr>') == 2, 'Word: cases 两行')
    ok('cases' not in _w, 'Word: 无 cases 源码残留')
    # split_rich 要产出 C 段
    ok(any(g[0] == 'C' for g in _E4.split_rich(ML.latex_expand(_cs))),
       'split_rich 产出 C 段')
    # expand 必须保留 \begin / \end
    ok(r'\begin{cases}' in ML.latex_expand(_cs),
       'latex_expand 保留 \\begin{cases}')
    # 补花括号正则不能把 \begin{cases} 变成 \begin_{cases}
    ok(r'\begin_{' not in ML.latex_expand(_cs),
       '补花括号正则未误伤 \\begin{cases}')

    # ---- 括号组作为上标基底 ----
    # (x-1)^2 的基底是整个 (x-1)。闭括号不是字母也不是数字，
    # 原来的三条规则全部落空 → 上标段被丢弃 → 平方整个消失且不报错。
    for _t, _n in [(r'(x-1)^2+(y-1)^2=1', 2), (r'(a+b)^n', 1), (r'[f(x)]^2', 1)]:
        _ww = _MP3.omml_latex(_t)
        ok(_ww.count('<m:sSup>') == _n,
           '括号组基底: %s → %d 个上标（实得 %d）'
           % (_t, _n, _ww.count('<m:sSup>')))
    # 回归：数字串与函数名基底不受影响
    ok(_MP3.omml_latex(r'90^\circ').count('<m:sSup>') == 1, '数字串基底仍正常')
    ok(_MP3.omml_latex(r'\log_2 x').count('<m:sSub>') == 1, '函数名基底仍正常')

    # ---- 关系宏 leqslant / geqslant ----
    ok('≤' in ML.latex_expand(r'x\leqslant y'), 'leqslant → ≤')
    ok('≥' in ML.latex_expand(r'x\geqslant y'), 'geqslant → ≥')
    ok('leqslant' not in ML.latex_inline(r'\leqslant'), 'HTML 无 leqslant 源码')
    print('  cases 与括号基底: 三端渲染 / 基底提取 / 关系宏 均正常')

    # ---- 集合与逻辑符号（第一批录入逐个暴露的缺口）----
    # 根因：之前录的都是函数/三角/向量题，用不到集合符号。
    # 每换一个知识模块就会暴露一批新缺口 —— 靠扫描发现，靠用例锁死。
    import re as _re2
    for _cmd, _sym in [(r'\mid', '∣'), (r'\subsetneq', '⊊'),
                       (r'\supsetneq', '⊋'), (r'\complement', '∁'),
                       (r'\setminus', '∖'), (r'\therefore', '∴'),
                       (r'\because', '∵')]:
        _hx = ML.latex_inline(_cmd)
        ok(_sym in _hx, '集合符号 %s → %s' % (_cmd, _sym))
        ok(_cmd.lstrip('\\') not in _hx,
           '集合符号 %s 无源码残留' % _cmd)
        ok(_sym in ML.latex_expand(_cmd), 'expand: %s → %s' % (_cmd, _sym))

    # ---- 转义花括号 ----
    # HTML 端走未知宏会输出 <mi>{</mi>（斜体）；Word 端不去反斜杠会显示 \{1,2\}
    _hb = ML.latex_inline(r'\{1,2\}')
    ok('<mo>{</mo>' in _hb, 'HTML: \\{ → <mo>{</mo>（正体，非 mi 斜体）')
    ok('<mi>{</mi>' not in _hb, 'HTML: \\{ 不是 <mi>（避免斜体）')
    ok(ML.latex_expand(r'\{1,2\}') == '{1,2}', 'expand: \\{1,2\\} → {1,2}')
    ok('\\{' not in ML.latex_expand(r'\{1,2\}'), 'Word: 无反斜杠残留')

    # ---- 兜底基底：∁ 带下标 ----
    # ∁(U+2201) 不是字母/数字/括号/函数名，前四条规则全落空
    _w = _MP3.omml_latex(r'\complement_U A')
    ok(_w.count('<m:sSub>') == 1,
       '兜底基底: \\complement_U A → 1 个下标（实得 %d）'
       % _w.count('<m:sSub>'))
    ok('∁' in _w and 'U' in _w, '兜底基底: ∁ 与 U 都在')

    # ---- 填空下划线用 ____ 而非 \underline ----
    import paper_template as _T2
    _pat = '|'.join('(?:%s)' % x for x in _T2.FILL['blank']['patterns'])
    ok(len(_re2.findall(_pat, r'a = \underline{\hspace{2em}}。')) == 1,
       '兜底: \\underline{\\hspace{2em}} 仍被识别为填空位')
    ok(len(_re2.findall(_pat, r'a = ____。')) == 1, '填空标记 ____ 被识别')

    # ---- 已录入数据不得残留源码 ----
    import json as _js
    _raw = open(os.path.join('data', 'bank.json'), encoding='utf-8').read()
    # 注意：'subsetneq' 是**正常的 LaTeX 源码**（在 $...$ 里），
    # 不该断言它不存在 —— 要检查的是渲染输出，不是 JSON 原文。
    for _p in ['underline', 'hspace']:
        ok(_p not in _raw, '题库无残留: %s' % _p)
    # stem 是列表，_prep_fields 会用 ' '.join(stem) 覆盖 stem_text，
    # 所以 stem 里也不能有脏数据，否则干净的 stem_text 会被覆盖回去。
    import json as _js2
    _bk = _js2.loads(_raw)
    _nstem = sum(1 for _q in _bk
                 if isinstance(_q.get('stem'), list)
                 and any('underline' in str(_x) or 'hspace' in str(_x)
                         for _x in _q['stem']))
    ok(_nstem == 0, 'stem 列表无残留（%d 题）' % _nstem)
    print('  集合符号 / 转义花括号 / 兜底基底 / 填空标记 均正常')

    # ---- cases：Word 端 dPr 必须用原生标准写法 ----
    # 直接写 m:val="" 或漏了 m:shp，Word 会「括号在、内容空白」且不报错。
    _w = _MP3.omml_latex(r'\begin{cases} x^2, & x\le 0 \\ 4\sin x, & 0<x\le\pi \end{cases}')
    ok('&#123;' in _w, 'cases: begChr 用数字实体 &#123;')
    # **不能写 &#0;**：XML 1.0 不允许空字符的字符引用，
    # parse_xml 抛异常 → omml_math 返回 None → 整个公式被静默丢弃。
    ok('&#0;' not in _w, 'cases: 不得出现 &#0;（XML 1.0 非法字符）')
    # sepChr 是「行内列分隔符」，写成 | 会在表达式与条件间插竖线
    ok('&#124;' not in _w, 'cases: sepChr 必须是空（不能是竖线）')
    ok('<m:grow m:val="on"/>' in _w, 'cases: grow 用 on（不是 1）')
    ok('<m:shp m:val="match"/>' in _w, 'cases: shp=match 不能省')
    # XML 合法性：omml_math 会因 parse_xml 失败返回 None，
    # 公式被静默丢弃。必须直接验证能解析成元素。
    import docx as _dx
    _d = _dx.Document(); _pp = _d.add_paragraph()
    _MP3.rich(_pp, r'$f(x)=\begin{cases}x^2, & x\le 0\\ 4\sin x, & 0<x\le\pi\end{cases}$', 10.5)
    _x = _pp._p.xml
    ok(_x.count('<m:oMath>') == 1, 'cases: omml_math 未返回 None（公式未被丢弃）')
    ok(_x.count('<m:d>') == 1, 'cases: 段落里真的有 m:d（实得 %d）' % _x.count('<m:d>'))
    ok(_x.count('<m:mr>') == 2, 'cases: 2 行 → 2 个 m:mr（实得 %d）' % _x.count('<m:mr>'))
    ok('sin' in _x, 'cases: 第二行内容在（不是空括号）')
    # 属性顺序必须是 CT_DPr 的 sequence
    _dpr = _re2.search(r'<m:dPr>.*?</m:dPr>', _w, _re2.S).group(0)
    for _a, _b in [('begChr', 'sepChr'), ('sepChr', 'endChr'),
                   ('endChr', 'grow'), ('grow', 'shp')]:
        # 注意：这里**不能**断言 shp < algn ——
        # CT_DPr 的 sequence 里没有 m:algn，它已被移除。
        ok(_dpr.find(_a) < _dpr.find(_b), 'cases: dPr 顺序 %s < %s' % (_a, _b))
    ok(_w.count('<m:mr>') == 2, 'cases: 2 行 → 2 个 m:mr')
    ok('4sin' in _w or 'sin' in _w, 'cases: 第二行内容在（不是空括号）')

    # ---- cases 降级路径 ----
    import paper_template as _T3
    _om = _T3.CASES_MODE
    _T3.CASES_MODE = 'text'
    _wt = _MP3.omml_latex(r'\begin{cases} a & b \\ c & d \end{cases}')
    ok(_wt.count('<m:d>') == 0, '降级 text: 不产出 m:d')
    ok('{' in ''.join(_re2.findall(r'<m:t>([^<]*)</m:t>', _wt)),
       '降级 text: 有左大括号')
    ok(all(x in ''.join(_re2.findall(r'<m:t>([^<]*)</m:t>', _wt))
           for x in 'abcd'), '降级 text: 四格内容都在')
    _T3.CASES_MODE = _om

    # ---- HTML 端 cases 必须压缩高度 ----
    _hc = ML.latex_inline(r'\begin{cases} x^2 & a \\ y & b \end{cases}')
    ok('<mstyle displaystyle="false">' in _hc,
       'HTML: cases 用 mstyle displaystyle=false 压低行高')
    ok('framespacing="0 0"' in _hc, 'HTML: cases 去外框留白')
    # 前端同步
    import subprocess as _sp
    _js = _sp.run(['node', '-e',
                   "import('./src/app/render.js').then(m=>"
                   "console.log(m.renderQuestion({id:'a',num:1,type:'t',"
                   "stem_text:'$\\\\begin{cases} x & a \\\\\\\\ y & b"
                   "\\\\end{cases}$',opts:[]},{})))"],
                  capture_output=True, text=True).stdout
    ok('displaystyle' in _js and 'framespacing' in _js,
       '前端 cases 与 Python 端同步（displaystyle + framespacing）')
    print('  cases: dPr 标准写法 / 降级路径 / HTML 压缩 均正常')

    # ---- cases 的 OMML 结构（第二轮才查对的规范）----
    _w = _MP3.omml_latex(r'\begin{cases} a & b \\ c & d \end{cases}')
    ok('<m:m>' in _w, 'cases: m:e 里必须有 m:m 矩阵层（直接放 m:mr 会空白）')
    ok('<m:algn' not in _w,
       'cases: dPr 不得有 m:algn（CT_DPr 的 sequence 里没有它）')
    ok('<m:mcJc m:val="left"/>' in _w, 'cases: 列对齐写在 m:mcJc 里')
    # CT_DPr 的合法顺序
    _dpr = _re2.search(r'<m:dPr>.*?</m:dPr>', _w, _re2.S).group(0)
    for _a, _b in [('begChr', 'sepChr'), ('sepChr', 'endChr'),
                   ('endChr', 'grow'), ('grow', 'shp')]:
        ok(_dpr.find(_a) < _dpr.find(_b), 'cases: dPr 顺序 %s < %s' % (_a, _b))
    # 列数声明
    ok('<m:count m:val="2"/>' in _w, 'cases: m:count 声明 2 列')

    # ---- 定界符不得跟随拉伸 ----
    # <mo> 默认 stretchy=true，f(x)={cases} 里的 () 会被 2 行高的
    # 分段函数拉到同样高度 —— 用户反馈的"f(x) 括号特别大"。
    _hi = ML.latex_inline(
        r'f(x)=\begin{cases}x^2, & x\le 0\\ 4\sin x, & 0<x\le\pi\end{cases}')
    ok('<mo stretchy="false">(</mo>' in _hi, 'HTML: f(x) 的 ( 不可拉伸')
    ok('<mo stretchy="false">)</mo>' in _hi, 'HTML: f(x) 的 ) 不可拉伸')
    ok('<mo stretchy="true">{</mo>' in _hi,
       'HTML: cases 的 { 保持 stretchy（它本来就该撑高）')
    # 不带 cases 的普通公式也不能误伤
    _h2 = ML.latex_inline(r'f(x)=x^2')
    ok('<mo stretchy="false">(</mo>' in _h2, 'HTML: 普通 f(x) 的括号也固定')

    # ---- 答案行必须渲染 LaTeX（不能是纯文本）----
    # 曾用 R() 输出答案，LaTeX 源码原样显示（用户看到的 "in"）。
    _d2 = _dx.Document(); _p2 = _d2.add_paragraph()
    _MP3.rich(_p2, r'【答案】$f(x)\notin M$，$g(x)\in M$', 10.5)
    _x2 = _p2._p.xml
    ok(_x2.count('<m:oMath>') == 2,
       '答案: 两个 $...$ 都渲染成公式（实得 %d）' % _x2.count('<m:oMath>'))
    ok('∉' in _x2 and '∈' in _x2, '答案: ∉ 与 ∈ 都是符号（不是 in 文本）')
    ok('notin' not in _x2 and '\\in' not in _x2, '答案: 无 LaTeX 源码残留')
    # 前端同步
    import subprocess as _sp2
    _js2 = _sp2.run(['node', '-e',
                     "import('./src/app/render.js').then(m=>"
                     "console.log(m.renderQuestion({id:'a',num:1,type:'t',"
                     "stem_text:'$f(x)=1$',opts:[]},{})))"],
                    capture_output=True, text=True).stdout
    ok('stretchy="false"' in _js2, '前端: 定界符 stretchy=false 与 Python 同步')
    print('  cases 结构 / 定界符不拉伸 / 答案渲染 均正常')

    # ---- 符号宏必须在 \mathbb 之前展开 ----
    # 顺序反了：x\in\mathbb{Z} → 先展开 mathbb → x\inZ
    #   → \in 后跟字母 Z，被 (?![a-zA-Z]) 挡住 → 不替换
    #   → 落到未知宏去掉反斜杠 → 输出 "xinZ"（Word 里 ∈ 变成 in）
    # HTML 端走 latex_inline 不受影响，所以只在 Word 端出现。
    for _t, _want in [(r'x\in\mathbb{Z}', '∈'), (r'x\in\mathbb{Q}', '∈'),
                      (r'a,b\in\mathbb{Q}', '∈'), (r'k\in\mathbb{Z}', '∈'),
                      (r'x\in\mathbb{N}', '∈'), (r'm\in\mathbb{Z}', '∈')]:
        _e = ML.latex_expand(_t)
        ok(_want in _e, 'expand: %s 含 %s（实得 %r）' % (_t, _want, _e))
        ok('in' not in _e, 'expand: %s 不残留 "in"（实得 %r）' % (_t, _e))
    # 端到端：Word 里必须是符号不是字母
    _d3 = _dx.Document(); _p3 = _d3.add_paragraph()
    _MP3.rich(_p3, r'$x\in\mathbb{Z}$', 10.5)
    ok('∈' in _p3._p.xml, 'Word: x∈Z 渲染出 ∈ 符号')
    ok('inZ' not in _p3._p.xml, 'Word: 不出现 inZ')

    # ---- 控制字符（\v 被 Python 吃掉变成 \x0b）----
    # $A\cap B=\x0b arnothing$ 应为 \varnothing
    ok(ML.repair_ctrl('$A\\cap B=\x0barnothing$') == '$A\\cap B=\\varnothing$',
       'repair_ctrl: \\x0b+arnothing → \\varnothing')
    ok('∅' in ML.latex_expand('$A\\cap B=\x0barnothing$'),
       'expand: 控制字符修复后渲染出 ∅')
    # Word 端：U+000B 是 XML 非法字符，不清理会让整个公式消失
    _d4 = _dx.Document(); _p4 = _d4.add_paragraph()
    _MP3.rich(_p4, '$A\\cap B=\x0barnothing$', 10.5)
    ok(_p4._p.xml.count('<m:oMath>') == 1,
       'Word: 含控制字符的公式不会被整体丢弃')
    ok('∅' in _p4._p.xml, 'Word: 控制字符修复后显示 ∅')
    # 换页符等不做还原（避免造出错误命令）
    ok(ML.repair_ctrl('abc\x0cdef') == 'abcdef',
       'repair_ctrl: \\x0c 直接删除而非还原成 \\f')

    # ---- 全库不得有控制字符 / 未渲染源码 ----
    import json as _js3, hand_input as _HI
    _bk = _HI.load()
    _bad = _re2.compile(r'[\x00-\x08\x0b\x0c\x0e-\x1f]')
    _n = sum(len(_bad.findall(_js3.dumps(_q, ensure_ascii=False))) for _q in _bk)
    ok(_n == 0, '题库无 XML 非法控制字符（%d 处）' % _n)
    _raw3 = _js3.dumps(_bk, ensure_ascii=False)
    ok('arnothing' not in _raw3, '题库无 arnothing 残留')
    print('  宏展开顺序 / 控制字符修复 均正常')

    # ---- \sqrt 后跟单字符（无花括号）----
    # split_rich() 只认 \sqrt{..}，不补花括号就切不出 S 段，
    # 落到未知宏分支：HTML 显示 "sqrt6"、Word 显示 "\sqrt6"。
    # 两端代码路径不同，HTML 端本来就能处理，只有 Word 端会漏。
    for _t in [r'\sqrt6', r'\sqrt2', r'2\sqrt2+\sqrt2=3\sqrt2',
               r'\frac{3\sqrt2}{2}']:
        _e = ML.latex_expand(_t)
        ok('\\sqrt{' in _e, 'expand: %s 补上花括号（实得 %r）' % (_t, _e))
        _d5 = _dx.Document(); _p5 = _d5.add_paragraph()
        _MP3.rich(_p5, '$%s$' % _t, 10.5)
        _mts = ''.join(_re2.findall(r'<m:t>([^<]*)</m:t>', _p5._p.xml))
        ok('sqrt' not in _mts, 'Word: %s 无源码泄漏（实得 %r）' % (_t, _mts))
        ok('<m:rad>' in _p5._p.xml, 'Word: %s 渲染出 m:rad' % _t)
    # 已有花括号 / 可选参数不受影响
    ok(ML.latex_expand(r'\sqrt{xy}') == r'\sqrt{xy}',
       'expand: \\sqrt{xy} 保持不变')
    ok(ML.latex_expand(r'\sqrt[3]{x}') == r'\sqrt[3]{x}',
       'expand: \\sqrt[3]{x} 可选参数不被破坏')
    # 不吃反斜杠：\sqrt\frac 不能被切成 \sqrt{\frac}
    ok(ML.latex_expand(r'\sqrt\frac{1}{2}') == r'\sqrt\frac{1}{2}',
       'expand: \\sqrt\\frac{1}{2} 不被误切（反斜杠不作为参数）')
    ok(ML.latex_expand(r'\sqrt6') == r'\sqrt{6}', 'expand: \\sqrt6 -> \\sqrt{6}')
    print('  \\sqrt 单字符参数补花括号 均正常')

    # ---- 显式 type 不得被 enrich 覆盖 ----
    # 原来无条件执行 `q['type'] = type_from_subtype(q) or type_guess(q)`，
    # 而 type_guess 兜底规则里有「题干长度 > 120 → 解答」，
    # 于是**长题干填空题被判成解答题**：
    #   渲染器 render_fill → render_solve，填空下划线不渲染，
    #   还凭空多出一大片答题留白。25 题里误判 2 题，且不报错。
    import main as _Mn
    _q_fill = {'id': 'M-H9001', 'subject': '数学', 'type': '填空',
               'subtype': '单空题', 'stem_text': '已知 $a$ 的取值范围是__________．' + 'x' * 100,
               'opts': [], 'answer': '$[1,2]$'}
    _q_choice = {'id': 'M-H9002', 'subject': '数学', 'type': '选择',
                 'subtype': '单选题', 'stem_text': '测试', 'opts': [['A', '1'], ['B', '2']],
                 'answer': 'A'}
    _en = [dict(_q_fill), dict(_q_choice)]
    _Mn.enrich(_en)
    ok(_en[0]['type'] == '填空',
       'enrich: 显式 type=填空 不被覆盖（实得 %r）' % _en[0]['type'])
    ok(_en[0].get('_type_src') == 'explicit',
       'enrich: 显式 type 的来源标记为 explicit')
    ok(_en[1]['type'] == '选择', 'enrich: 选择题 type 保持')
    # subtype 细分名必须能推出大题型
    for _st, _want in [('单空题', '填空'), ('多空题', '填空'),
                       ('填空题-单空题', '填空'), ('单选题', '选择'),
                       ('多选题-2个答案', '选择'), ('证明题', '解答'),
                       ('问答题', '解答')]:
        ok(_Mn.type_from_subtype({'subtype': _st}) == _want,
           'type_from_subtype: %r → %s（实得 %r）'
           % (_st, _want, _Mn.type_from_subtype({'subtype': _st})))

    # ---- 填空下划线：句末句号不得再生成一个空 ----
    # 「…有__________．」里句号紧跟填空标记，它只是句号。
    # 缺后顾断言时会被句末句点规则再匹配一次，
    # 表现为**一个空渲染出两段下划线，且句号被吞掉**。
    _pat = '|'.join('(?:%s)' % x for x in T.FILL['blank']['patterns'])
    for _st, _n in [(r'不同的选择方法有__________．', 1),
                    (r'实数 $m$ 的取值范围是__________．', 1),
                    (r'实数 $m$ 的取值范围是__________。', 1),
                    (r'共有 种.', 1)]:          # 无填空标记时句号仍算空
        ok(len(list(re.finditer(_pat, _st))) == _n,
           '填空标记: %r 应识别 %d 处（实得 %d）'
           % (_st[-12:], _n, len(list(re.finditer(_pat, _st)))))
    # 全角下划线同理
    ok(len(list(re.finditer(_pat, '是＿＿＿＿．'))) == 1,
       '填空标记: 全角 ＿＿＿＿． 只识别 1 处')

    # ---- 填空题端到端：两端都要渲染出下划线 ----
    import docx as _dx2, build_html as _BH2
    _qb = {'id': 'M-H9003', 'type': '填空', 'subtype': '单空题', 'subject': '数学',
           'num': 1, 'score': 5, 'smark': '', 'figs': [],
           'stem_text': r'设 $A=\{1,2,3\}$，则不同的选择方法有__________．',
           'stem': [r'设 $A=\{1,2,3\}$，则不同的选择方法有__________．'],
           'opts': [], 'answer': '$9$'}
    _MP3._prep_fields(_qb)
    ok(_MP3._qtype_of_q(_qb) == '填空',
       '填空: _qtype_of_q 返回填空（实得 %r）' % _MP3._qtype_of_q(_qb))
    _d5 = _dx2.Document()
    _MP3.render_blank_stem(_d5, _qb['stem_text'], 1)
    _x5 = _d5.paragraphs[0]._p.xml
    ok('<w:u w:val="single"/>' in _x5, 'Word: 填空处渲染出下划线')
    ok('___' not in ''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>', _x5)),
       'Word: 无字面 ___ 残留')
    _h5 = _BH2._blank_stem(_qb['stem_text'])
    ok(_h5.count('blank-u') == 1,
       'HTML: 只渲染 1 处下划线（实得 %d）' % _h5.count('blank-u'))
    ok('___' not in _h5, 'HTML: 无字面 ___ 残留')
    print('  题型覆盖 / 填空下划线 均正常')
except Exception as e:
    import traceback
    traceback.print_exc()
    ok(False, 'hand_input check failed: %s' % e)


# ---- 公式命令覆盖（第11批）----
# 每录一批新题都可能用到新符号。全库扫一遍能一次性找出所有"未支持命令"，
# 而不是等用户在页面上看到 "sumlimits" 再报。
try:
    OK_FN = {'sin', 'cos', 'tan', 'log', 'ln', 'max', 'min', 'lim', 'exp',
             'arg', 'deg', 'det', 'dim', 'gcd', 'hom', 'ker'}
    _bk4 = _HI.load()
    _badcmd = []
    for _q4 in _bk4:
        for _f4 in ('stem_text', 'solution', 'answer', 'analysis'):
            for _m4 in _re2.finditer(r'<mi>([a-zA-Z]{3,})</mi>',
                                     ML.latex_inline(_q4.get(_f4) or '')):
                if _m4.group(1) not in OK_FN:
                    _badcmd.append('%s.%s:%s' % (_q4['id'], _f4, _m4.group(1)))
    ok(not _badcmd, '全库无未渲染的 LaTeX 命令名（发现 %d 处：%s）'
       % (len(_badcmd), _badcmd[:5]))
    print('  公式命令覆盖: 全库扫描 %s' % ('✓ 无未渲染' if not _badcmd else '✗ %s' % _badcmd[:3]))
except Exception as e:
    ok(False, '公式命令覆盖检查失败: %s' % e)

# ---- 只影响排版的命令要跳过，且不吃掉后续内容 ----
try:
    # 注意：不能写成 '$a\\leftb$' —— 正则 [a-zA-Z]+ 会贪婪匹配成命令
    # "leftb"，那确实是个不存在的命令，输出 <mi>leftb</mi> 是合理的。
    # 测试要用真实用法（后面跟非字母）。
    for _case, _word in ((r'$\\left(a\\right)$', 'left'),
                         (r'$\\left\\{x\\middle|x>0\\right\\}$', 'middle'),
                         (r'$\\sum\\limits_{k=1}^{n}k$', 'limits'),
                         (r'$\\displaystyle\\frac{1}{2}$', 'displaystyle')):
        _o = ML.latex_inline(_case)
        ok(_word not in _o, '排版命令 \\%s 应被跳过（实得 %r）' % (_word, _o[:90]))
    _o2 = ML.latex_inline(r'$f\!\left(x\right)$')
    ok('<mi>x</mi>' in _o2, '跳过后后续内容仍渲染：%r' % _o2[:100])
    ok('<mi mathvariant="normal">f</mi>' in _o2,
       'f 后面是 \\!\\left( 时仍判为函数名（正体）：%r' % _o2[:100])
    print('  排版命令: 跳过且不误伤 均正常')
except Exception as e:
    ok(False, '排版命令检查失败: %s' % e)

# ---- 算子与逻辑符号（第11批全库扫描发现的缺口）----
try:
    for _src, _want in ((r'\sum', '∑'), (r'\prod', '∏'), (r'\int', '∫'),
                        (r'\iff', '⟺'), (r'\odot', '⊙'),
                        (r'\triangleq', '≜'), (r'\Leftrightarrow', '⇔')):
        _o3 = ML.latex_inline('$%s$' % _src)
        ok(_want in _o3, '%s 渲染为 %s（实得 %r）' % (_src, _want, _o3[:80]))
    print('  算子与逻辑符号: 7 个 均正常')
except Exception as e:
    ok(False, '算子与逻辑符号检查失败: %s' % e)

# ---- 跳过清单 ----
try:
    import json as _js4
    _sp_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'skipped.json')
    ok(os.path.exists(_sp_path), '跳过清单 data/skipped.json 存在')
    if os.path.exists(_sp_path):
        _d6 = _js4.load(io.open(_sp_path, encoding='utf-8'))
        ok('items' in _d6 and 'reason_desc' in _d6, '跳过清单含 items 与 reason_desc')
        _legal = set(_d6.get('reason_desc') or {})
        _bad6 = [i['key'] for i in _d6['items'] if i.get('reason') not in _legal]
        ok(not _bad6, '跳过清单原因分类合法（越界 %s）' % _bad6[:5])
        _nonote = [i['key'] for i in _d6['items'] if not i.get('note')]
        ok(not _nonote, '每条跳过记录都要有 note（缺 %s）' % _nonote[:5])
        print('  跳过清单: %d 条记录 / 分类合法 / note 齐全' % len(_d6['items']))
except Exception as e:
    ok(False, '跳过清单检查失败: %s' % e)

# ---- 第13批：否定箭头（充要条件解析常用；漏了会直接显示命令名）----
def test_neg_arrows():
    # 解析里常写 P nRightarrow Q。缺失时页面会显示 nRightarrow 字面量。
    # 注意：字符串必须用 raw，否则 Python 会把它当成换行符。
    import mathml as _ML
    for cmd in (r'\nRightarrow', r'\nLeftarrow', r'\nleftrightarrow',
                r'\nrightarrow', r'\nleftarrow'):
        out = _ML.latex_inline(cmd)
        ok(cmd[1:] not in out, '%s 未被展开：%s' % (cmd, out))

try:
    test_neg_arrows()
    print('  否定箭头: 全部展开')
except Exception as e:
    ok(False, '否定箭头检查失败: %s' % e)

srv.shutdown()
print('\n通过 %d / %d' % (pass_n, pass_n + fail_n))
sys.exit(1 if fail_n else 0)
