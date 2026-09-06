# -*- coding: utf-8 -*-
"""人工审核录入（Hand Input）

与自动提取的区别：
    自动提取 —— 脚本读 PDF 坐标重建结构。快，但会丢括号、
                 把详解碎片当题目、公式渲染成分行文本。
    人工录入 —— 读原文、理解语义、手工重建为规范 LaTeX。
                 慢（一道 3-5 分钟），但**内容正确**。

本模块不负责"读题"，只负责**入库与校验**。
题目内容由人工（或 AI 读原文后）写好传进来。

之所以仍要工具而不是直接改 JSON：
    手改 JSON 出错不报错（漏逗号、字段名拼错、选项少一个），
    等渲染时才发现，排查成本高。工具在入库时就拦住。

用法：
    from hand_input import add
    add({
        'stem_text': '已知 $f(x)=x^2$，则 $f(2)$ =',
        'opts': [['A','1'], ['B','2'], ['C','3'], ['D','4']],
        'answer': 'B',
        'type': '选择',
        'kp': '函数与导数',
    })
"""
import os
import re
import json

_HERE = os.path.dirname(os.path.abspath(__file__))
def _data_dir():
    env = os.environ.get('GAOKAO_DATA_DIR')
    return os.path.abspath(env) if env else os.path.join(
        os.path.dirname(_HERE), 'data')


DATA = _data_dir()
PATH = os.path.join(DATA, 'bank.json')

LETTERS = 'ABCDEFGH'
REQUIRED = ('stem_text',)
QTYPE = ('选择', '填空', '解答')


def load():
    try:
        with open(PATH, encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return []


def save(bank):
    """原子写 + 备份。

    与 py/main.py 的 _atomic_write 同策略：
    先写 .tmp 再 os.replace，避免写一半崩溃损坏整个题库。
    人工录入的数据更珍贵（一道 3-5 分钟），必须保护。
    """
    bak = PATH + '.bak'
    if os.path.exists(PATH):
        with open(PATH, encoding='utf-8') as f:
            old = f.read()
        with open(bak, 'w', encoding='utf-8') as f:
            f.write(old)
    tmp = PATH + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(bank, f, ensure_ascii=False, indent=1)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, PATH)


def _check_latex(s):
    """LaTeX 括号配对检查。

    人工录入最常见的手误：\\frac{1}{2 少了右括号。
    渲染时这种错误会静默吞掉后面所有内容，极难排查。
    """
    if not s:
        return []
    errs = []
    # 去掉转义括号
    t = re.sub(r'\\[{}]', '', s)
    depth = 0
    for i, c in enumerate(t):
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth < 0:
                errs.append('位置 %d 多出 }' % i)
                depth = 0
    if depth > 0:
        errs.append('有 %d 个 { 未闭合' % depth)
    # $ 必须成对
    if t.count('$') % 2:
        errs.append('$ 未成对（%d 个）' % t.count('$'))
    return errs


# 科目 -> ID 前缀。
# 人工录入的 ID 也要带科目前缀（如 M-H0001），
# 因为系统里 ID 前缀有语义：切片目录按科目分、统计按前缀分组。
SUBJ_PREFIX = {'数学': 'M', '物理': 'P', '化学': 'C',
               '生物': 'B', '语文': 'Y', '英语': 'E'}


def next_id(bank, subject='数学'):
    """生成下一个人工录入 ID：M-H0001, M-H0002...

    格式 = 科目前缀 + "-H" + 序号。
    带科目前缀是为了与真题 ID（M-2021-001）保持同一命名空间，
    切片/统计/导出都按前缀分科目，不加前缀会掉出这些逻辑。
    中间加 H 是为了一眼区分「人工录入」与「自动提取」。
    """
    pre = SUBJ_PREFIX.get(subject, 'X')
    mx = 0
    for q in bank:
        m = re.match(r'^%s-H(\d+)$' % re.escape(pre), str(q.get('id') or ''))
        if m:
            mx = max(mx, int(m.group(1)))
    return '%s-H%04d' % (pre, mx + 1)


def validate(q, bank=None):
    """入库前校验，返回 (ok, 问题列表)"""
    errs = []

    for k in REQUIRED:
        if not (q.get(k) or '').strip():
            errs.append('缺必填字段: %s' % k)

    qt = q.get('type') or ''
    if qt not in QTYPE:
        errs.append('type 必须是 %s 之一，当前 %r' % (list(QTYPE), qt))

    # 选项
    opts = q.get('opts') or []
    if qt == '选择':
        if not opts:
            errs.append('选择题没有选项')
        elif len(opts) < 2:
            errs.append('选择题选项少于 2 个')
        for i, o in enumerate(opts):
            if not (isinstance(o, (list, tuple)) and len(o) == 2):
                errs.append('选项 %d 形状应为 (字母, 文本)' % i)
                continue
            L, t = o
            if L not in LETTERS:
                errs.append('选项 %d 的字母 %r 非法' % (i, L))
            if not str(t).strip():
                errs.append('选项 %s 内容为空' % L)
        # 字母不重复
        ls = [o[0] for o in opts if isinstance(o, (list, tuple))]
        if len(ls) != len(set(ls)):
            errs.append('选项字母重复: %s' % ls)
        # 答案必须在选项内
        ans = (q.get('answer') or '').strip()
        if ans and ls:
            a_letters = set(re.findall(r'[A-H]', ans.upper()))
            if not a_letters <= set(ls):
                errs.append('答案 %r 超出选项范围 %s' % (ans, ls))
    elif qt == '填空':
        if not (q.get('answer') or '').strip():
            errs.append('填空题没有答案')
    elif qt == '解答':
        if not (q.get('solution') or '').strip():
            errs.append('解答题没有详解')

    # LaTeX 配对
    for k in ('stem_text', 'analysis', 'solution'):
        for e in _check_latex(q.get(k) or ''):
            errs.append('%s: %s' % (k, e))
    for L, t in (opts if isinstance(opts, list) else []):
        if isinstance(t, str):
            for e in _check_latex(t):
                errs.append('选项 %s: %s' % (L, e))

    # ID 唯一
    if bank is not None:
        qid = q.get('id')
        if qid and any(x.get('id') == qid for x in bank):
            errs.append('ID 重复: %s' % qid)

    # 知识点
    if not (q.get('kp') or '').strip():
        errs.append('缺一级知识点 kp')

    return (not errs), errs


def add(q, batch='人工录入'):
    """校验并入库一道题。返回 (ok, id 或 问题列表)"""
    bank = load()
    ok, errs = validate(q, bank)
    if not ok:
        return False, errs

    q.setdefault('subject', '数学')
    if not q.get('id'):
        q['id'] = next_id(bank, q['subject'])
    q.setdefault('num', 0)
    q.setdefault('score', 5 if q.get('type') == '选择' else 5)
    q.setdefault('figs', [])
    q.setdefault('difficulty', 0.65)
    q.setdefault('batch', batch)
    q.setdefault('smark', '')
    q.setdefault('subtype', _subtype(q))
    q.setdefault('kp2', '')
    q.setdefault('topics', [])
    q.setdefault('kp_list', [x for x in (q.get('kp'), q.get('kp2')) if x])
    q.setdefault('src', '')
    q.setdefault('review', '')       # 人工审核备注（记改了什么、为什么）
    q['ana_text'] = q.get('analysis') or ''
    # 渲染层用的 stem（列表形式）
    q['stem'] = [q['stem_text']]

    bank.append(q)
    save(bank)
    return True, q['id']


def _subtype(q):
    if q.get('type') != '选择':
        return '填空题-单空题' if q.get('type') == '填空' else '解答题-问答题'
    letters = set(re.findall(r'[A-H]', (q.get('answer') or '').upper()))
    if len(letters) > 1:
        return '多选题-%d个答案' % len(letters)
    return '单选题'


def add_many(qs, batch='人工录入'):
    """批量录入。

    整批校验，**任一题有问题就整批拒绝** ——
    半截入库的数据比不入库更麻烦（不知道哪些进了哪些没进）。
    """
    bank = load()
    all_errs = []
    for i, q in enumerate(qs):
        ok, errs = validate(q, bank)
        for e in errs:
            all_errs.append('第 %d 题: %s' % (i + 1, e))
    if all_errs:
        return False, all_errs

    ids = []
    for q in qs:
        q.setdefault('subject', '数学')
        if not q.get('id'):
            q['id'] = next_id(bank, q['subject'])
        q.setdefault('num', 0)
        q.setdefault('score', 5)
        q.setdefault('figs', [])
        q.setdefault('difficulty', 0.65)
        q.setdefault('batch', batch)
        q.setdefault('smark', '')
        q.setdefault('subtype', _subtype(q))
        q.setdefault('kp2', '')
        q.setdefault('topics', [])
        q.setdefault('kp_list', [x for x in (q.get('kp'), q.get('kp2')) if x])
        q.setdefault('src', '')
        q.setdefault('review', '')
        q['ana_text'] = q.get('analysis') or ''
        q['stem'] = [q['stem_text']]
        bank.append(q)
        ids.append(q['id'])
    save(bank)
    return True, ids
