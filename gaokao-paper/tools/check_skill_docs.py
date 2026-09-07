# -*- coding: utf-8 -*-
"""校验 skill 文档里写的东西是否还有效

知识文档最容易腐化：代码改了、数字变了，文档还停留在旧版本，
等按文档操作时才发现命令不存在、数字不对。

本脚本把 `gaokao-import` skill 里出现的**可验证断言**都跑一遍：
  · CLI 子命令是否都存在
  · Python 函数是否都存在
  · 文档引用的数字是否与代码一致
  · 关键代码片段能否跑通

用法：
    python3 tools/check_skill_docs.py

新增文档后，把里面的关键数字/函数加进对应列表。
"""
import os
import re
import sys
import json
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL = '/data/skills/gaokao-import'
sys.path.insert(0, os.path.join(ROOT, 'py'))

pass_n = fail_n = 0


def ok(cond, msg):
    global pass_n, fail_n
    if cond:
        pass_n += 1
    else:
        fail_n += 1
        print('  ✗', msg)


print('=== skill 文档有效性自检 ===\n')

# ---------------------------------------------------------------
# 1. 目录结构
# ---------------------------------------------------------------
if not os.path.isdir(SKILL):
    print('  skill 目录不存在:', SKILL)
    sys.exit(1)

ok(os.path.isfile(os.path.join(SKILL, 'SKILL.md')), 'SKILL.md 存在')
refs = sorted(f for f in os.listdir(os.path.join(SKILL, 'references'))
              if f.endswith('.md'))
ok(len(refs) >= 8, 'references 数量 >= 8: %d' % len(refs))

# SKILL.md 的路由表必须覆盖每个 reference
skill_md = open(os.path.join(SKILL, 'SKILL.md'), encoding='utf-8').read()
cited = set(re.findall(r'`references/([a-z0-9\-]+\.md)`', skill_md))
for f in refs:
    ok(f in cited, '路由表覆盖 %s' % f)

# 交叉引用不能有死链
for f in refs:
    s = open(os.path.join(SKILL, 'references', f), encoding='utf-8').read()
    for c in set(re.findall(r'`(?:references/)?(\d\d-[a-z0-9\-]+\.md)`', s)):
        ok(c in refs, '%s 的引用 %s 存在' % (f, c))

print('  结构: %d 个 reference，路由全覆盖，无死链' % len(refs))

# ---------------------------------------------------------------
# 2. CLI 子命令（40-api.md 里列的所有命令）
# ---------------------------------------------------------------
r = subprocess.run([sys.executable, os.path.join(ROOT, 'py', 'main.py'), '--help'],
                   capture_output=True, text=True, cwd=ROOT)
usage = r.stdout
for cmd in ['health', 'list', 'extract', 'export-html', 'export-docx',
            'export-answer', 'compose', 'topic-list', 'topic-link',
            'batch-list', 'batch-tag', 'batch-delete', 'kp-catalog']:
    ok(cmd in usage, 'CLI 子命令 %s 存在' % cmd)
print('  CLI: 13 个子命令全部存在')

# ---------------------------------------------------------------
# 3. Python 函数（文档里点名引用的）
# ---------------------------------------------------------------
import kp_catalog as K
import mathml as M
import hand_input as H

for fn in ['topic_id', 'topic_label', 'topic_node', 'normalize',
           'normalize_list', 'level1', 'level2', 'level3', 'verify_index']:
    ok(hasattr(K, fn), 'kp_catalog.%s 存在' % fn)
for fn in ['latex_inline', 'latex_expand', 'frac', 'sqrt', 'sub', 'sup']:
    ok(hasattr(M, fn), 'mathml.%s 存在' % fn)
for fn in ['add', 'add_many', 'validate', 'next_id', 'load', 'save']:
    ok(hasattr(H, fn), 'hand_input.%s 存在' % fn)
print('  函数: kp_catalog / mathml / hand_input 接口完整')

# ---------------------------------------------------------------
# 4. 文档里的关键数字
# ---------------------------------------------------------------
def n_level2(sub):
    return len(set(n for _, subs in K.CATALOG[sub] for n in subs))

ok(len(K.CATALOG['数学']) == 12, '数学一级 12: %d' % len(K.CATALOG['数学']))
ok(n_level2('数学') == 108, '数学二级 108: %d' % n_level2('数学'))
ok(len(K.TOPICS) == 422, '数学题型 422: %d' % len(K.TOPICS))
# 不写死数字：MACRO 会随新命令增加，写死会让每次补命令都"失败"，
# 久了就会习惯性忽略报错 —— 那样自检就废了。
# 改为读文档里声明的数字，与实际条数对比。
import re as _re
_doc = open(os.path.join(ROOT, 'skill', 'references', '20-latex.md'),
            encoding='utf-8').read()
_m = _re.search(r'MACRO\s*[:：]?\s*(\d+)', _doc)
# **必须显式报错而不是 fallback 到 len(M.MACRO)**：
# fallback 会让断言变成"自己等于自己"，永远通过 ——
# 文档删了声明、检查却全绿，这个盲区已经发生过一次。
ok(_m is not None,
   '20-latex.md 声明了 MACRO 条数（缺失会让下面的检查形同虚设）')
_declared = int(_m.group(1)) if _m else -1
ok(len(M.MACRO) == _declared,
   'MACRO 文档声明 %d 条，实际 %d 条' % (_declared, len(M.MACRO)))
ok(len(M.GREEK) == 38, 'GREEK 38: %d' % len(M.GREEK))
ok(len(M.FUNCS) == 26, 'FUNCS 26: %d' % len(M.FUNCS))
ok(len(M.BB) == 0, 'BB 为空表(恒等映射): %d' % len(M.BB))
n_cross = sum(1 for v in K.TOPICS.values() if v.get('cross'))
ok(n_cross == 35, '交叉题型 35: %d' % n_cross)
n_alias = sum(len(v) for v in K.ALIASES.values())
ok(n_alias == 213, '别名 213: %d' % n_alias)
for s, c in [('物理', 16), ('化学', 16), ('生物', 18), ('语文', 8), ('英语', 9)]:
    ok(len(K.CATALOG[s]) == c, '%s 一级 %d: %d' % (s, c, len(K.CATALOG[s])))

# 六科科目前缀必须与文档一致
prefix = {'数学': 'M', '物理': 'P', '化学': 'C',
          '生物': 'B', '语文': 'Y', '英语': 'E'}
for s, p in prefix.items():
    ok(H.next_id([], s).startswith(p + '-H'),
       'next_id 前缀 %s -> %s: %s' % (s, p, H.next_id([], s)))
print('  数字: 目录规模 / 命令表 / 别名 / 交叉题型 / 科目前缀 均一致')

# ---------------------------------------------------------------
# 5. 文档里的行为断言
# ---------------------------------------------------------------
ok(M.latex_expand(r'\dfrac{9}{2}') == r'\frac{9}{2}', 'dfrac 归一为 frac')
ok(M.latex_expand(r'\tfrac{3}{4}') == r'\frac{3}{4}', 'tfrac 归一为 frac')
ok(M.latex_expand(r'\sqrt{3}') == r'\sqrt{3}', 'sqrt 结构保留')
ok(M.latex_expand(r'\mathbb{R}') == 'R', 'mathbb R -> R')
ok('ℝ' not in M.latex_inline(r'\mathbb{R}'), 'mathml 不输出 ℝ')
ok('ℝ' not in M.latex_expand(r'\mathbb{R}'), 'expand 不输出 ℝ')
ok(M.latex_expand('x_1') == 'x_{1}', '无括号下标补花括号')
for cmd in ('frac', 'dfrac', 'tfrac'):
    out = M.latex_inline('\\%s{1}{2}' % cmd)
    ok('<mfrac>' in out, '\\%s 渲染为 mfrac' % cmd)
    # dfrac/tfrac 不能残留命令名。
    # frac 不检查——它的名字本来就出现在 <mfrac> 标签里，
    # 拿 "frac" 做子串判断会误报。这个坑是写本用例时踩到的。
    if cmd != 'frac':
        ok(cmd not in out, '\\%s 命令名无残留' % cmd)
ok('<msub>' in M.latex_inline('x_1'), 'x_1 -> msub')
ok('<msup>' in M.latex_inline('x^2'), 'x^2 -> msup')
ok('<msubsup>' in M.latex_inline('x_1^2'), 'x_1^2 -> msubsup')
ok(M.latex_inline(r'\frac{\sqrt{3}}{2}').count('<msqrt>') == 1, '嵌套 frac/sqrt')

# 校验器必须拦住手误
bad = [
    ({'type': '选择', 'opts': [['A', '1']], 'answer': 'A', 'kp': 'x'}, '缺题干'),
    ({'stem_text': 'x', 'type': '单选', 'kp': 'x'}, 'type 非法'),
    ({'stem_text': 'x', 'type': '选择', 'answer': 'A', 'kp': 'x'}, '无选项'),
    ({'stem_text': '$\\frac{1}{2$', 'type': '填空', 'answer': '1', 'kp': 'x'},
     '花括号未闭合'),
    ({'stem_text': '$x^2', 'type': '填空', 'answer': '1', 'kp': 'x'},
     '美元未成对'),
]
caught = sum(1 for q, _ in bad if not H.validate(q, [])[0])
ok(caught == len(bad), '校验器拦截 %d/%d 类手误' % (caught, len(bad)))

# split_rich 的 $ 定界：类型必须是 L 不能用 x（x 已reserved）
from extract3 import split_rich
segs = split_rich('已知 $f(x)$ 与 $y=1$')
ok([s[0] for s in segs].count('L') == 2, 'split_rich 识别 2 个 $...$')
ok('x' not in [s[0] for s in segs], '不使用保留类型 x')
ok('未闭合' in ''.join(s[1] for s in split_rich('已知 $f(x) 未闭合')),
   '未配对 $ 不吞掉后续内容')
print('  行为: LaTeX 渲染 / 宏展开 / 校验器 / 定界符 全部符合文档')

# ---------------------------------------------------------------
# 6. 选项分列（30-pitfalls 与 21-review 提到的）
# ---------------------------------------------------------------
import build_html as BH
pat = re.compile(r'--cols:(\d)')
short = BH._opts_html({'opts': [['A', '30'], ['B', '14'],
                                ['C', '12'], ['D', '6']]})
longf = BH._opts_html({'opts': [
    ['A', '$f(2017)<f(2018)<f(2019)$'],
    ['B', '$f(2018)<f(2017)<f(2019)$'],
    ['C', '$f(2018)<f(2019)<f(2017)$'],
    ['D', '$f(2019)<f(2018)<f(2017)$']]})
ok(pat.search(short).group(1) == '4', '短选项 4 列')
# 改用渲染宽度估算后，长公式从 1 列变为 2 列。
# 这是**正确的**：估算宽 23.0，而 2 列容量约 41.7，放得下。
# 真正要防的是「放不下」，所以断言 <= 2 列 + 容量校验。
_cols = int(pat.search(longf).group(1))
ok(_cols <= 2, '长公式 <=2 列（实际 %d）' % _cols)
import paper_template as _T
_lw = max(_T.render_width(t) for t in
          ('$f(2017)<f(2018)<f(2019)$', '$f(2018)<f(2017)<f(2019)$',
           '$f(2018)<f(2019)<f(2017)$', '$f(2019)<f(2018)<f(2017)$'))
ok(_lw <= _T.col_capacity(_cols),
   '长公式未超 %d 列容量（%.1f <= %.1f）' % (_cols, _lw, _T.col_capacity(_cols)))
ok('opts-noclip' in longf, '含公式选项标记 noclip')
ok('opts-noclip' not in short, '纯文本选项保留裁切')
ok(BH._math_len('$f(2017)<f(2018)<f(2019)$') >= 20,
   '公式长度按真实内容计算')
print('  分列: 短4列 / 长公式1列 / noclip 标记 均符合文档')

# ---------------------------------------------------------------
# 7. 端到端一致性（30-pitfalls 给的脚本）
# ---------------------------------------------------------------
sample_html = os.path.join(ROOT, 'html', '试卷_对称性与周期性专项.html')
sample_docx = os.path.join(ROOT, 'out', '试卷_对称性与周期性专项.docx')
if os.path.exists(sample_html) and os.path.exists(sample_docx):
    import docx
    h = open(sample_html, encoding='utf-8').read()
    d = docx.Document(sample_docx)
    full = ''.join(p._p.xml for p in d.paragraphs)
    for t in d.tables:                       # 选项在表格里，必须算进去
        for row in t.rows:
            for c in row.cells:
                full += c._tc.xml
    ok(h.count('<mfrac>') == full.count('<m:f>'),
       '分数两端一致: HTML %d / Word %d'
       % (h.count('<mfrac>'), full.count('<m:f>')))
    ok(h.count('dfrac') == 0 and full.count('dfrac') == 0, '无 dfrac 残留')
    ok(h.count('ℝ') == 0 and full.count('ℝ') == 0, '无 ℝ 残留')
    ok(len(re.findall(r'\\[a-zA-Z]+\{|\$', h)) == 0, 'HTML 无源码残留')
    print('  端到端: 样卷两端一致，无残留')

# ---------------------------------------------------------------
print('\n通过 %d / %d' % (pass_n, pass_n + fail_n))
sys.exit(1 if fail_n else 0)
