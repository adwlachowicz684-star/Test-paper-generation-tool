# -*- coding: utf-8 -*-
"""知识点讲解（Knowledge Notes）

数据来源：教辅 PDF 里每个题型下的板块。

    【典例分析】  例题  —— 录入 ref_bank.json，按 ID 引用
    【变式演练】  练习题 —— 同上
    【提分秘籍】  方法归纳 —— 直接存文本
    【点睛】      补充要点 —— 直接存文本

**题目不内嵌，只存 ID**。
一道真题常被多个题型引用（实测「已知双曲线…」出现 4 次），
内嵌会让同一道题在 JSON 里重复 4 份；
按 ID 引用则只存一份，且前端可单独加载/跳转。

存储：
    data/kp_notes.json   讲解 + 题目ID 引用
    data/ref_bank.json   题目正文（qid -> 题目）
"""
import os
import json

_HERE = os.path.dirname(os.path.abspath(__file__))
def _data_dir():
    env = os.environ.get('GAOKAO_DATA_DIR')
    return os.path.abspath(env) if env else os.path.join(
        os.path.dirname(_HERE), 'data')


DATA = _data_dir()
PATH = os.path.join(DATA, 'kp_notes.json')
REFPATH = os.path.join(DATA, 'ref_bank.json')

_cache = None
_refcache = None


def load():
    global _cache
    if _cache is None:
        try:
            with open(PATH, encoding='utf-8') as f:
                _cache = json.load(f)
        except Exception:
            _cache = {'topic': {}, 'l2': {}, 'l1': {}, '_meta': {}}
    return _cache


def load_ref():
    global _refcache
    if _refcache is None:
        try:
            with open(REFPATH, encoding='utf-8') as f:
                _refcache = json.load(f)
        except Exception:
            _refcache = {}
    return _refcache


def reload():
    global _cache, _refcache
    _cache = None
    _refcache = None
    return load()


def get(subject, l1=None, l2=None, topic=None):
    """按层级取讲解：题型 > 小知识点 > 大知识点。

    返回 {level, title, notes:[...], examples:[qid], variants:[qid]}
    没有内容时各字段为空，由前端提示可补充。
    """
    db = load()
    if topic:
        nd = (db.get('topic') or {}).get(topic)
        if nd:
            return {'level': 'topic', 'title': l2 or '',
                    'notes': nd.get('notes') or [],
                    'examples': nd.get('examples') or [],
                    'variants': nd.get('variants') or []}
    if l1 and l2:
        key = '%s|%s|%s' % (subject, l1, l2)
        if key in (db.get('l2') or {}):
            return {'level': 'l2', 'title': '%s / %s' % (l1, l2),
                    'notes': [{'kind': '要点', 'text': db['l2'][key]}],
                    'examples': [], 'variants': []}
    if l1:
        key = '%s|%s' % (subject, l1)
        if key in (db.get('l1') or {}):
            return {'level': 'l1', 'title': l1,
                    'notes': [{'kind': '概览', 'text': db['l1'][key]}],
                    'examples': [], 'variants': []}
    return {'level': None, 'title': l1 or l2 or '',
            'notes': [], 'examples': [], 'variants': []}


def questions(qids):
    """按 ID 批量取题目（缺失的静默跳过，不报错）"""
    ref = load_ref()
    out = []
    for q in (qids or []):
        v = ref.get(q)
        if v:
            out.append(v)
    return out


def qsummary(qids):
    """给前端列表用的摘要（不含详解，避免一次传太多）"""
    ref = load_ref()
    out = []
    for q in (qids or []):
        v = ref.get(q)
        if not v:
            continue
        out.append({'id': v['id'], 'stem': v.get('stem') or '',
                    'opts': v.get('opts') or [],
                    'ans': v.get('ans') or '',
                    'has_sol': bool(v.get('solution'))})
    return out


def stats():
    db = load()
    t = db.get('topic') or {}
    return {
        'topic': sum(1 for v in t.values() if v.get('notes')),
        'with_questions': sum(1 for v in t.values()
                              if v.get('examples') or v.get('variants')),
        'l2': len(db.get('l2') or {}),
        'l1': len(db.get('l1') or {}),
        'examples': sum(len(v.get('examples') or []) for v in t.values()),
        'variants': sum(len(v.get('variants') or []) for v in t.values()),
        'meta': db.get('_meta') or {},
    }
