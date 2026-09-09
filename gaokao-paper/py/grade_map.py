# -*- coding: utf-8 -*-
"""年级体系：内置年级定义 + 知识点 → 年级 映射

## 年级为什么用 ID 而不是名字

年级可以被用户**重命名**（设置页）。如果题目上存的是显示名
（比如 "高一"），改名后这道题就指向一个不存在的年级，变成孤儿数据。

所以：
  - 题目 / 映射表一律存 **ID**（s1 / s2 / s3 …）
  - 名字只用于显示，改名字不影响任何数据关联

## 覆盖全部教育年级

内置 12 个年级（小学 6 + 初中 3 + 高中 3），ID 与顺序固定：

    p1..p6  小学一年级 ~ 六年级
    j1..j3  初一 / 初二 / 初三
    s1..s3  高一 / 高二 / 高三

默认**隐藏小学与初中**：当前题库是高考数学，9 个空年级全列出来
只会让人以为「加载失败」。要用就在设置页打开，一次点开即可。

## 隐藏 vs 删除

| 操作 | 数据 | 题目 |
|---|---|---|
| 隐藏 | 年级定义还在，随时可恢复 | 不受影响，仍属于该年级 |
| 删除 | 年级定义消失 | 引用它的题退回「未标注」 |

删除前必须让用户看到有多少题受影响 —— 这个数字由 stats 接口提供。

## 映射精度

**二级（小知识点）优先于一级。**「函数与导数」269 题横跨高一（函数性质）
到高三（导数压轴），只按一级分必然失真。

未命中返回 UNKNOWN（「未标注」）—— 宁可留白，也不硬塞。
"""

import json
import os

UNKNOWN = '未标注'

# ---------- 内置年级 ----------
# (id, 默认名, 学段)
# 顺序即展示顺序，不可调整 —— 小学→初中→高中是天然顺序，
# 让用户自由排序只会制造混乱。
_BUILTIN = [
    ('p1', '一年级', '小学'),
    ('p2', '二年级', '小学'),
    ('p3', '三年级', '小学'),
    ('p4', '四年级', '小学'),
    ('p5', '五年级', '小学'),
    ('p6', '六年级', '小学'),
    ('j1', '初一', '初中'),
    ('j2', '初二', '初中'),
    ('j3', '初三', '初中'),
    ('s1', '高一', '高中'),
    ('s2', '高二', '高中'),
    ('s3', '高三', '高中'),
]

# 默认隐藏的年级：题库是高考内容，这些年级排不上用场
_DEFAULT_HIDDEN = {'p1', 'p2', 'p3', 'p4', 'p5', 'p6',
                   'j1', 'j2', 'j3'}

SEGMENTS = ['小学', '初中', '高中']


def default_grades():
    """默认年级列表（配置里没有这个字段时用它兜底）"""
    return [{'id': i, 'name': n, 'seg': s,
             'hidden': i in _DEFAULT_HIDDEN, 'builtin': True}
            for i, n, s in _BUILTIN]


# ---------- 配置读写 ----------
# 单独实现一份轻量读取，不 import main ——
# main 会 import 本模块，反过来 import main 就是循环依赖。
_HERE = os.path.dirname(os.path.abspath(__file__))
CONFIG = os.path.join(os.path.dirname(_HERE), 'data', 'config.json')


def load_grades():
    """读年级配置。文件缺失 / 损坏 / 结构不对，都退回默认。

    容错要厚：这是**配置**，不是业务数据。
    配置坏了导致整个应用起不来，是最不该发生的事。
    """
    try:
        with open(CONFIG, encoding='utf-8') as f:
            c = json.load(f)
        g = (c or {}).get('grades')
        if isinstance(g, list) and g and all(
                isinstance(x, dict) and x.get('id') for x in g):
            return _normalize(g)
    except Exception:
        pass
    return default_grades()


def _builtin(gid):
    """查内置定义，返回 (默认名, 学段)，非内置返回 None"""
    for i, n, s in _BUILTIN:
        if i == gid:
            return (n, s)
    return None


def _normalize(grades):
    """补齐缺字段（hidden / name / seg），并去掉重复 id"""
    out, seen = [], set()
    for x in grades:
        gid = str(x.get('id') or '').strip()
        if not gid or gid in seen:
            continue
        seen.add(gid)
        b = _builtin(gid)
        out.append({
            'id': gid,
            'name': str(x.get('name') or (b[0] if b else gid)).strip(),
            'seg': str(x.get('seg') or (b[1] if b else '自定义')).strip(),
            'hidden': bool(x.get('hidden')),
            'builtin': bool(x.get('builtin', bool(b))),
        })
    return out or default_grades()


def ordered(grades=None):
    """按内置顺序输出；自定义年级排在最后（没有天然位置）"""
    g = grades or load_grades()
    rank = {i: n for n, (i, _, _) in enumerate(_BUILTIN)}
    return sorted(g, key=lambda x: (rank.get(x['id'], 999), x['id']))


def visible(grades=None):
    """未隐藏的年级"""
    return [x for x in ordered(grades) if not x.get('hidden')]


def id_of(value, grades=None):
    """把任意写法（ID / 显示名）归一化成 ID。

    兼容历史数据：题目上如果人工写了中文名（"高一"），
    也要能认出来。认不出返回 UNKNOWN。
    """
    v = str(value or '').strip()
    if not v or v == UNKNOWN:
        return UNKNOWN
    for x in (grades or load_grades()):
        if v == x['id'] or v == x.get('name'):
            return x['id']
    return UNKNOWN


def name_of(gid, grades=None):
    for x in (grades or load_grades()):
        if x['id'] == gid:
            return x.get('name') or gid
    return gid if gid and gid != UNKNOWN else UNKNOWN


def is_hidden(gid, grades=None):
    for x in (grades or load_grades()):
        if x['id'] == gid:
            return bool(x.get('hidden'))
    return False


# ---------- 知识点 → 年级 ----------
# 映射值一律用 **ID**，不用显示名（改名不影响）

_L1_MATH = {
    '集合与逻辑': 's1',
    '不等式':     's1',
    '函数与导数': 's2',
    '三角函数':   's1',
    '平面向量':   's1',
    '立体几何':   's2',
    '解析几何':   's2',
    '概率统计':   's1',
    '计数原理':   's2',
    '数列':       's2',
    '复数':       's2',
    '统计':       's1',
}

_L2_MATH = {
    # 高一：函数入门、基本初等函数
    ('集合与逻辑', '集合运算'):             's1',
    ('不等式', '基本不等式'):               's1',
    ('不等式', '不等式选讲'):               's3',   # 选讲是高三选考内容
    ('函数与导数', '幂指对比较大小'):        's1',
    ('函数与导数', '对称性与周期性'):        's1',
    ('函数与导数', '零点与图像交点'):        's1',
    ('函数与导数', '零点区间与个数'):        's1',
    ('函数与导数', '复合函数与嵌套函数零点'): 's1',

    # 高二：导数、圆锥曲线
    ('函数与导数', '导数切线与公切线'):      's2',
    ('函数与导数', '导数含参讨论'):          's2',
    ('函数与导数', '导数构造函数'):          's2',
    ('函数与导数', '导数压轴小题(二)'):      's3',   # 压轴 = 高三综合
    ('解析几何', '离心率'):                 's2',
    ('解析几何', '轨迹方程'):               's2',
    ('解析几何', '圆锥曲线小题'):           's2',
    ('立体几何', '外接球'):                 's2',
    ('计数原理', '排列组合'):               's2',
    ('平面向量', '向量小题'):               's1',
    ('三角函数', '三角函数性质与最值'):      's1',
    ('三角函数', '解三角形小题(一)'):        's1',
    ('三角函数', '解三角形小题(二)'):        's1',
    ('概率统计', '概率小题'):               's1',
}

# 按科目分表：物理/化学的教学顺序与数学完全不同，
# 没配置的科目一律 UNKNOWN —— 不拿数学的表去套别的科。
_BY_SUBJ = {'数学': (_L1_MATH, _L2_MATH)}


def grade_of(subject, l1, l2=None):
    """按 (一级, 二级) 推断年级 ID

    命中顺序：二级精确 → 一级兜底 → UNKNOWN
    """
    conf = _BY_SUBJ.get(subject or '')
    if not conf:
        return UNKNOWN
    l1map, l2map = conf
    if l2:
        g = l2map.get((l1, l2))
        if g:
            return g
    return l1map.get(l1) or UNKNOWN


def grade_of_question(q, grades=None):
    """给一道题定年级（返回 ID）

    **题目自带 grade 优先**：人工校订时可以覆盖自动推断。
    自带值可能是中文名（历史数据），走 id_of() 归一化。
    """
    g = id_of(q.get('grade'), grades)
    if g != UNKNOWN:
        return g

    l1s = q.get('kp_list') or []
    l2 = (q.get('kp2') or '').strip()

    # 多知识点题取**最高年级**：
    # 一道同时考「集合+导数」的题高二才做得了，归到高一会让筛选漏掉它。
    g = grades or load_grades()
    order = [x['id'] for x in ordered(g)]
    best = None
    for l1 in l1s:
        gid = grade_of(q.get('subject'), l1, l2 or None)
        if gid == UNKNOWN or gid not in order:
            continue
        if best is None or order.index(gid) > order.index(best):
            best = gid
    return best or UNKNOWN
