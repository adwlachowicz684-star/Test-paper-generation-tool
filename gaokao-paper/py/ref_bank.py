# -*- coding: utf-8 -*-
"""教辅例题库（ref_bank）适配器

bank.json 装的是**真题**（216 道，来自高考卷 PDF）；
ref_bank.json 装的是**教辅例题**（1395 道，来自《2024 高中数学热点题型归纳》
的【典例分析】【变式演练】）。

两者字段差异很大，本模块负责把教辅题**适配成渲染层认识的形状**，
这样 build_html / make_paper 不用改一行就能渲染教辅题。

| 字段 | ref_bank | 渲染层需要 |
|---|---|---|
| stem | str | stem_text (str) |
| opts | ['16','9'] | [['A','16'], ['B','9']] |
| type | '例题' | '选择' / '填空' / '解答' |

**写适配器而不是改提取器**，是因为提取器已经跑完并固化进 JSON，
重跑要 3 分钟且可能引入新的提取差异；适配是纯函数，随时可调。
"""
import os
import re
import json

_HERE = os.path.dirname(os.path.abspath(__file__))
def _data_dir():
    env = os.environ.get('GAOKAO_DATA_DIR')
    return os.path.abspath(env) if env else os.path.join(
        os.path.dirname(_HERE), 'data')


PATH = os.path.join(_data_dir(), 'ref_bank.json')

LETTERS = 'ABCDEFGH'
_cache = None


def load():
    global _cache
    if _cache is None:
        try:
            with open(PATH, encoding='utf-8') as f:
                _cache = json.load(f)
        except Exception:
            _cache = {}
    return _cache


def reload():
    global _cache
    _cache = None
    return load()


# ---- 题干清洗 ----------------------------------------------------------
#
# 教辅 PDF 提取出的题干有三个特征问题：
#   1. 公式被拆成多行      "设I = 1,2,3,4,\n\n，A 与B 是I 的子集"
#   2. 集合/区间花括号丢失  PDF 里是矢量绘制，不是文本字符
#   3. 题号行混入          "14. 设I = ..."（已在提取时剥离，但边界情况仍有）
_WS = re.compile(r'[ \t]+\n')
_MULTI_NL = re.compile(r'\n{2,}')
_LEAD_NUM = re.compile(r'^\s*(?:例\s*)?\d{1,3}\s*[.．]\s*')


def clean_stem(s):
    """压缩多余空行，但**保留单换行以内的结构**。

    为什么不完全压成一行：公式分子分母原本就是上下两行，
    压成一行会变成 "1,2,3,4,，A 与B" 这种粘连。
    只压 2 个以上连续换行（公式碎片留下的空档）。
    """
    if not s:
        return ''
    s = _WS.sub('\n', s)
    s = _MULTI_NL.sub('\n', s)
    return s.strip()


# ---- 题型判定 ----------------------------------------------------------
_QMARK = re.compile(r'[（(]\s*1\s*[)）]')          # (1) 多问 -> 解答题
_BLANK = re.compile(r'[＿_]{2,}|［\s*］|\[\s*\]')   # 下划线 -> 填空题


def guess_type(item):
    """教辅题没有题型字段，只有「有选项 / 无选项」之分。

    判定顺序（先特殊后一般）：
      1. 有选项        -> 选择
      2. 含 (1)(2) 多问 -> 解答（需要留白）
      3. 含下划线      -> 填空
      4. 其余          -> 填空（教辅里裸干题多数是填空）
    """
    if item.get('opts'):
        return '选择'
    st = item.get('stem') or ''
    if _QMARK.search(st):
        return '解答'
    if _BLANK.search(st):
        return '填空'
    # 长题干（含多个句号/分号）多半是解答题
    if len(st) > 160 or st.count('。') + st.count('.') >= 3:
        return '解答'
    return '填空'


def num_opts(opts):
    opts = opts or []
    return len(opts)


def subtype(item, qtype):
    """细分题型：单选/多选 影响判分规则（多选有部分分）"""
    if qtype != '选择':
        return '填空题-单空题' if qtype == '填空' else '解答题-问答题'
    # 教辅不标注单选多选。答案里出现多个字母 -> 多选
    ans = (item.get('ans') or '').strip()
    letters = set(re.findall(r'[A-D]', ans.upper()))
    if len(letters) > 1:
        return '多选题-%d个答案' % len(letters)
    return '单选题'


def adapt(item, kp_map=None):
    """把一条 ref_bank 记录适配成渲染层格式"""
    qtype = guess_type(item)
    opts = item.get('opts') or []
    # opts: ['16','9'] -> [['A','16'], ['B','9']]
    opt_pairs = [(LETTERS[i] if i < len(LETTERS) else str(i + 1), t)
                 for i, t in enumerate(opts)]
    st = clean_stem(item.get('stem'))
    tid = item.get('topic') or ''
    kp1, kp2 = (kp_map or {}).get(tid, ('', ''))
    return {
        'id': item['id'],
        'num': item.get('num') or 0,
        'stem_text': st,
        'stem': [st],
        'opts': opt_pairs,
        'figs': [],                       # 教辅题未切图（见 README 已知限制）
        'qtype': qtype,
        'type': qtype,
        'subtype': subtype(item, qtype),
        'answer': item.get('ans') or '',
        'ana_text': item.get('analysis') or '',
        'analysis': item.get('analysis') or '',
        'solution': item.get('solution') or '',
        'score': 5 if qtype == '选择' else 5,
        'smark': '',
        'subject': item.get('subject') or '数学',
        'src': item.get('src') or '',
        'topic': tid,
        'kind': item.get('kind') or '',
        'kp': kp1,                        # 从题型节点反查的一级知识点
        'kp2': kp2,
        'kp_list': [x for x in (kp1, kp2) if x],
        'difficulty': 0.65,               # 教辅无难度系数，给中间值
        'batch': '教辅-' + (item.get('src') or 'ref'),
        'is_ref': True,                   # 供渲染层/判分区分来源
    }


def kp_index():
    """题型 ID -> (一级, 二级)。

    教辅题只记了题型 ID，没有知识点。
    反查目录才能按「函数与导数」筛教辅题 ——
    否则教辅题在知识点筛选下永远选不出来。
    """
    try:
        import kp_catalog as K
    except ImportError:
        return {}
    out = {}
    for sub in K.CATALOG:
        for l1, subs in K.CATALOG[sub]:
            for l2, tops in subs.items():
                if l2 == K.XSECTION:
                    continue
                for t in tops:
                    tid = K.topic_id(sub, l1, l2, t)
                    if tid:
                        out[tid] = (l1, l2)
    return out


def all_items(kp_map=None):
    kp_map = kp_map if kp_map is not None else kp_index()
    return [adapt(v, kp_map) for v in load().values()]


def stats():
    """按题型/知识点统计（供前端显示）"""
    items = all_items()
    from collections import Counter
    return {
        'total': len(items),
        'by_kind': dict(Counter(x.get('kind') for x in items)),
        'by_type': dict(Counter(x.get('qtype') for x in items)),
        'by_kp': dict(Counter(x.get('kp') for x in items if x.get('kp'))),
        'with_ans': sum(1 for x in items if x.get('answer')),
    }
