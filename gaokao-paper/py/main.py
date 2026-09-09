# -*- coding: utf-8 -*-
"""命令行桥接入口 —— 供 Tauri / Rust 后端调用

设计原则：
  - 所有命令输出 JSON 到 stdout（Rust 侧解析）
  - 错误信息输出到 stderr，退出码非 0
  - 不依赖 Tauri，可独立运行，方便调试

用法：
    python main.py <command> [--arg value ...]

命令：
    health        健康检查（Python 版本、依赖库、可用命令）
    list          列出题库所有题目（可 --subject / --limit 过滤）
    stats         题库统计（按科目/题型/难度/知识点）
    compose       按条件组卷
    extract       拆题入库（从 PDF）
    export-html   导出试卷为 HTML（打印即 PDF）
    progress      读写练习记录
    due           列出到期需复习的题目
"""
import sys, os, json, re, argparse, io, traceback

# 保证「无论从哪个目录调用」都能 import 同目录的模块
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def _data_dir():
    """数据目录。

    支持环境变量 GAOKAO_DATA_DIR 覆盖 —— 测试用它指向临时目录，
    避免测试读写用户真实数据（录错的题、练习记录都不可重建）。
    """
    env = os.environ.get('GAOKAO_DATA_DIR')
    if env:
        return os.path.abspath(env)
    return os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), 'data')

DATA_DIR = _data_dir()
BANK = os.path.join(DATA_DIR, 'bank.json')
PROGRESS = os.path.join(DATA_DIR, 'progress.json')
CONFIG = os.path.join(DATA_DIR, 'config.json')
BATCHES = os.path.join(DATA_DIR, 'batches.json')

# 复习参数默认值。
#
# 这些数值原来硬编码在 cmd_progress() 里（LADDER 字典）和前端，
# 改一次要动两处且必须重新打包。现在统一放在 config.json，
# 在「设置」页签里改，保存即生效，不用重启应用。
DEFAULT_CONFIG = {
    # 复习阶梯：等级 -> 间隔天数
    # 等级由练习结果驱动：做错降到负数档，做对逐档升高。
    "ladder": {
        "-2": 1,    # 连错 2 次以上 → 明天再来
        "-1": 2,    # 错 1 次      → 2 天后（不是 7 天，见下方说明）
        "0": 0,     # 未练习       → 立即可练
        "1": 7,
        "2": 15,
        "3": 30,
        "4": 60,
        "5": 120,
    },
    # 起始间隔为什么是 2 天不是 7 天：
    # 刚做错时，孩子对"自己当时怎么想的"记得最清，此时重做才改思路；
    # 拖到 7 天，多数人只记得答案、忘了错因，变成背答案。
    "wrong2_level": -2,      # 累计错几次后压到最低档
    "max_level": 5,          # 等级上限（到顶后保持 120 天）
    "done_level": 3,         # 达到此等级视为「已掌握」，不再主动出现
    "due_soon_days": 3,      # 「即将到期」的提前提醒天数
    # 组卷时未练题与错题的配比（百分比），和为 100
    "mix_new_pct": 70,
    "mix_wrong_pct": 30,
    # 每日新题上限，避免一次灌太多
    "daily_new_cap": 20,
}


def load_config():
    try:
        with open(CONFIG, encoding='utf-8') as f:
            c = json.load(f)
    except Exception:
        return dict(DEFAULT_CONFIG)
    # 缺字段用默认补齐（旧版本配置文件也能用）
    out = dict(DEFAULT_CONFIG)
    for k, v in (c or {}).items():
        if k == 'ladder':
            out['ladder'] = {str(kk): int(vv) for kk, vv in (v or {}).items()}
        else:
            out[k] = v
    return out


def save_config(c):
    """写配置（原子写 + fsync）

    fsync 不能省：只 flush 到 OS 缓存就 replace，紧接着的 open()
    在部分文件系统（overlayfs / 容器卷 / NFS）上会读到**旧内容**，
    表现为「设置页明明保存成功，读回来却是旧值」。
    """
    _atomic_write(CONFIG, c)
# 切片目录必须在 frontendDist(=src/) 之内。
# 原因：前端用 <img src="/slices/...">，Tauri 会相对 frontendDist 解析。
# 放在项目根 slices/ 的话，打包后路径解析到 src/slices/ → 图片全 404。
SLICE = os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))), 'src', 'slices')


# 写入串行锁。
# 单命令串行时不需要，但 dev_bridge 是多线程 HTTP 服务 ——
# 两个请求同时触发写库（如「导入PDF」与「标记题型」并发），
# 会各自写 .tmp 再 replace，结果互相覆盖，甚至读到截断的半成品。
# 实测 selftest 里就复现过「Expecting value: line N」的 JSON 解析失败。
import threading

_WRITE_LOCK = threading.Lock()


def _atomic_write(path, data):
    """原子写 JSON：加锁 → 写 .tmp → fsync → os.replace

    三步都有必要：
      1. 加锁     —— 防止并发写互相覆盖（dev_bridge 是多线程的）
      2. 写 .tmp  + fsync —— 只 flush 到 OS 缓存就 replace，紧接着的 open()
                    在 overlayfs / 容器卷 / NFS 上可能读到旧内容
      3. replace  —— 原子替换，读者要么见旧要么见新，不会见半截
    """
    os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
    with _WRITE_LOCK:
        tmp = path + '.tmp'
        with open(tmp, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=1)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)


# ---------------- 批次（Batch）----------------
"""
为什么需要批次：
  用户会分多次导入题目（先真题，后模考卷，再学校内部卷）。
  某一批质量不高或想重来时，需要「把这一批整体删掉」，
  而逐题勾选 200 道不现实。

设计：
  题目 q['batch'] = 批次ID
  批次注册表 batches.json 记录元信息（名称、时间、来源、题数）

  题数**不落盘**，每次从题库实时统计 ——
  否则删除题目后注册表会与题库不一致。
"""


def load_batches():
    try:
        with open(BATCHES, encoding='utf-8') as f:
            d = json.load(f)
    except Exception:
        return {}
    # 文件可能是 list（空表被存成 []），而所有调用方都按 dict 用：
    # batch_stats 里 reg.get(bid)、batch-delete 里 reg[bid][...]。
    # 不归一会在批次表为空时抛 'list' object has no attribute 'get'，
    # 表现为删题/统计在边角情况下崩掉。
    if not isinstance(d, dict):
        return {}
    return {k: v for k, v in d.items() if isinstance(v, dict)} \
        if d and all(isinstance(v, dict) for v in d.values()) else d


def save_batches(b):
    _atomic_write(BATCHES, b)


def new_batch_id(name=None):
    """生成批次ID：导入-年月日-时分秒"""
    from datetime import datetime
    ts = datetime.now().strftime('%Y%m%d-%H%M%S')
    return '导入-' + ts


def batch_stats(bank=None):
    """统计各批次的题数（实时算，不落盘）"""
    bank = bank if bank is not None else load_bank()
    from collections import Counter, defaultdict
    cnt = Counter(q.get('batch') or '未标记' for q in bank)
    # 用 subject 字段统计，而不是 ID 首字母。
    # ID 前缀只是约定（M/P/C…），subject 才是权威字段；
    # 且 enrich() 之后 subject 一定有值，ID 前缀却可能不标准。
    sub = defaultdict(lambda: defaultdict(int))
    for q in bank:
        b = q.get('batch') or '未标记'
        sj = q.get('subject') or SUBJ.get(str(q.get('id', ''))[:1], '?')
        sub[b][sj] += 1
    reg = load_batches()
    out = []
    for bid in sorted(set(list(cnt) + list(reg)), key=lambda x: str(x)):
        meta = reg.get(bid) or {}
        out.append({
            'id': bid,
            'name': meta.get('name') or bid,
            'time': meta.get('time') or '',
            'src': meta.get('src') or '',
            'count': cnt.get(bid, 0),          # 实时题数
            'by_subject': dict(sub.get(bid) or {}),
            'registered': bid in reg,
        })
    # 有题的排前面，其次按 ID 倒序（新的在前）
    out.sort(key=lambda x: (-x['count'], x['id']), reverse=False)
    out.sort(key=lambda x: (x['count'] == 0, x['id']), reverse=(False, True)[0])
    return out


def _out(obj):
    """统一输出：ensure_ascii=False 保证中文可读"""
    print(json.dumps(obj, ensure_ascii=False))
    return 0


def _fail(msg, code=1):
    print(json.dumps({'ok': False, 'error': str(msg)}, ensure_ascii=False))
    sys.stderr.write(str(msg) + '\n')
    return code


def load_bank():
    if not os.path.exists(BANK):
        return []
    with open(BANK, encoding='utf-8') as f:
        return json.load(f)


def load_progress():
    if not os.path.exists(PROGRESS):
        return {}
    try:
        with open(PROGRESS, encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {}


def save_progress(p):
    _atomic_write(PROGRESS, p)     # 原子写，避免写一半崩溃导致记录全丢


SUBJ = {'M': '数学', 'P': '物理', 'C': '化学',
        'B': '生物', 'Y': '语文', 'E': '英语'}

# 题目只标了大知识点、没有小知识点时的兜底分组名。
# 用它占位而不是丢掉，保证「大知识点题数 = 其下小知识点题数之和」。
UNSPLIT = '（未细分）'


def _save_bank(bank):
    """写回题库（原子写 + 备份）。

    题型标签也在里面，所以必须用与练习记录同等级的保护：
    写一半崩溃会丢掉整个题库的标签。
    """
    os.makedirs(DATA_DIR, exist_ok=True)
    try:
        import shutil
        shutil.copy(BANK, BANK + '.bak')
    except Exception:
        pass
    _atomic_write(BANK, bank)


# ---------------- 难度 ----------------
def level_of(coef):
    """难度系数 → 等级（与 Excel 的 Z 列公式保持一致）"""
    if coef is None:
        return ''
    if coef >= 0.7:
        return '容易'
    if coef >= 0.5:
        return '适中'
    if coef >= 0.3:
        return '较难'
    return '困难'


def _estimate_diff(q, total):
    """按卷结构与题号估算难度系数（与 Excel 预填口径一致）"""
    num = q.get('num', 0)
    pre = q.get('id', 'M')[0]
    if pre == 'M':
        if total >= 22:
            if num <= 8:
                return 0.85 if num <= 6 else (0.65 if num <= 7 else 0.5)
            if num <= 12:
                return [0.65, 0.5, 0.4, 0.4][num - 9]
            if num <= 16:
                return [0.75, 0.6, 0.45, 0.3][num - 13]
            return [0.7, 0.6, 0.45, 0.35, 0.25, 0.15][min(num - 17, 5)]
        if num <= 8:
            return 0.85 if num <= 6 else (0.65 if num <= 7 else 0.5)
        if num <= 11:
            return [0.65, 0.4, 0.4][num - 9]
        if num <= 14:
            return [0.75, 0.55, 0.3][num - 12]
        return [0.65, 0.55, 0.4, 0.3, 0.15][min(num - 15, 4)]
    if num <= 11:
        return 0.85 if num <= 5 else (0.7 if num <= 8 else 0.55)
    return [0.7, 0.6, 0.5, 0.35, 0.25][min(num - 12, 4)]


def type_from_subtype(q):
    """从 subtype（Excel 里标注的题型细分）推断大题型。

    为什么必须优先用它：
      subtype 是标注阶段确定的、可信的分类；
      而靠 opts/score 运行时推测会大面积出错 ——
      实测 216 题里误判 48 题（22%），
      典型场景：带公式的选项提取失败 → 多选题被判成填空；
                解答题 score 未提取到（为 0）→ 被判成填空。
    """
    st = str(q.get('subtype') or '').strip()
    if st.startswith(('单选', '多选')):
        return '选择'
    # **不能只认 '填空' 开头**。
    # subtype 用的是原卷细分名，「单空题」「多空题」「填空题-单空题」
    # 都不以「填空」二字开头（「填空」在中间或没有）。
    # 只写 startswith('填空') 的话这类题全部落空 → 走到 type_guess
    # → 靠题干长度猜测 → 长题干填空题被判成解答题。
    if '填空' in st or st.startswith(('单空', '多空')):
        return '填空'
    if st.startswith(('解答', '实验', '证明', '计算', '问答题')):
        return '解答'
    return ''


def type_guess(q):
    """无 subtype 时的兜底推测（准确率明显低于 subtype）"""
    if len(q.get('opts') or []) >= 2:
        return '选择'
    # 注意：score 可能为 0（提取失败），不能只靠它判断。
    # 用题干长度辅助：解答题题干通常较长且含小问编号。
    stem = q.get('stem_text') or ''
    if re.search(r'[(（]\s*[12]\s*[)）]', stem) or len(stem) > 120:
        return '解答'
    if q.get('score'):
        return '解答'
    return '填空'


def enrich(qs):
    """补齐前端需要的派生字段（难度、科目、知识点数组、题型）"""
    from collections import defaultdict
    totals = defaultdict(int)
    for q in qs:
        totals[(q['id'][0], q.get('year'))] += 1
    for q in qs:
        pre = q['id'][0]
        # 科目：**显式字段优先**，没有才从 ID 前缀推断。
        # 早期版本无条件用 ID 首字母覆盖，人工录入的题目（ID 如 M-H0001，
        # 或科目前缀不在 SUBJ 表内）会被改成错误科目，
        # 进而被 `--subject 数学` 静默筛掉 —— 录入成功了却查不到。
        # 同理，difficulty 也是显式优先。
        if not q.get('subject'):
            q['subject'] = SUBJ.get(pre, pre)
        if 'difficulty' not in q:
            q['difficulty'] = _estimate_diff(q, totals[(pre, q.get('year'))])
        q['level'] = level_of(q.get('difficulty'))
        # 归一到本科目标准知识点。
        # 否则「圆锥曲线」和「解析几何」会被当成两个不同考点，
        # 统计分散、组卷筛选也会漏题。
        import kp_catalog as _K
        kp = q.get('kp') or ''
        raw = [x.strip() for x in str(kp).split(';') if x.strip()]
        q['kp_list'] = _K.normalize_list(q['subject'], raw)
        q['kp_raw'] = raw
        # **显式 type 优先，不可覆盖**。
        #
        # 人工录入时 type 是确定的（'选择'/'填空'/'解答'），
        # 这是最可信的信息。原来的写法无条件用 type_guess 覆盖，
        # 而 type_guess 兜底规则里有「题干长度 > 120 → 解答」，
        # 于是长题干的**填空题被判成解答题**：
        #   - 渲染器从 render_fill 变成 render_solve
        #   - 填空下划线不渲染（题干里的 ____ 原样显示为文本）
        #   - 还会凭空多出一大片答题留白
        # 实测 25 题里误判 2 题，且只在导出时暴露，不报错。
        #
        # type_from_subtype / type_guess 只用于**自动提取**的题
        # （那时没有可信的 type 字段）。
        _VT = ('选择', '多选', '填空', '解答', '实验', '计算')
        _explicit = str(q.get('type') or '').strip()
        if _explicit in _VT:
            q['_type_src'] = 'explicit'
        else:
            tfs = type_from_subtype(q)
            q['type'] = tfs or type_guess(q)
            q['_type_src'] = 'subtype' if tfs else 'guess'
        if 'topics' not in q:
            q['topics'] = []
        # 题型标签带上可读名，前端免得再查一次
        q['topic_names'] = [
            {'id': t, 'label': _K.topic_label(t)}
            for t in (q.get('topics') or []) if _K.topic_node(t)
        ]
        # 年级：**派生**字段，不写回题库。
        # 题目自带 grade 的以自带为准（人工校订过最可信），
        # 其余按知识点映射推断 —— 见 grade_map.py 的设计说明。
        # 必须在 kp_list / kp2 都归完之后才算，否则映射查不到。
        import grade_map as _G
        q['grade'] = _G.grade_of_question(q)
    # 双向索引：题型 → 题目，每次从题目上的标签重建。
    # 只存单向（题目→题型）避免双写不一致。
    _K.rebuild_qindex(qs)
    return qs


# ================= 命令实现 =================
def cmd_health(a):
    info = {'ok': True, 'python': sys.version.split()[0],
            'bank_exists': os.path.exists(BANK)}
    for m in ('pymupdf', 'docx', 'PIL'):
        try:
            __import__(m)
            info['dep_' + m] = True
        except ImportError:
            info['dep_' + m] = False
    if os.path.exists(BANK):
        info['bank_count'] = len(load_bank())
    return _out(info)


def cmd_list(a):
    qs = enrich(load_bank())
    if a.subject:
        qs = [q for q in qs if q.get('subject') == a.subject]
    if a.q:
        qs = [q for q in qs
              if a.q in json.dumps(q, ensure_ascii=False)]
    if a.limit:
        qs = qs[:a.limit]
    return _out({'ok': True, 'total': len(qs), 'items': qs})


def cmd_stats(a):
    from collections import Counter, defaultdict
    import kp_catalog as K
    import grade_map as _G0
    qs = enrich(load_bank())
    c_sub = Counter(q.get('subject') for q in qs)
    c_type = Counter(q.get('type') for q in qs)
    c_lv = Counter(q.get('level') for q in qs)

    # by_kp 必须按科目分组。
    # 之前是全库一份，前端不区分地直接渲染，
    # 结果切到物理还是显示「解析几何」「三角函数」这类数学知识点。
    by_kp = defaultdict(Counter)
    for q in qs:
        sub = q.get('subject') or ''
        for k in q.get('kp_list', []):
            by_kp[sub][k] += 1

    # 三级展开：大知识点 → 小知识点 → 题型。
    #
    # 光有 by_kp 不够：它只到一级，且值是 [[名, 题数], ...] 数组，
    # 前端若按 {名: 题数} 渲染，整个数组会被当字符串塞进一个单元格，
    # 一科的知识点全挤成一行（统计页就是这么坏的）。
    # 所以这里直接把三级树算好，前端照着铺行即可。
    #
    # 归属以**题型节点的主归属为准**（topic.primary = (一级, 二级)），
    # 没挂题型的题才退回用 q['kp'] / q['kp2']，避免同一题在两级上错位。
    pair = defaultdict(Counter)     # (科目, 一级) -> Counter(二级)
    trio = defaultdict(Counter)     # (科目, 一级, 二级) -> Counter(题型ID)
    for q in qs:
        sub = q.get('subject') or ''
        tops = [t for t in (q.get('topics') or []) if K.topic_node(t)]
        seen = set()
        if tops:
            for tid in tops:
                l1, l2 = K.topic_node(tid)['primary']
                if (l1, l2) not in seen:
                    pair[(sub, l1)][l2] += 1
                    seen.add((l1, l2))
                trio[(sub, l1, l2)][tid] += 1
        else:
            l2 = (q.get('kp2') or '').strip() or UNSPLIT
            for l1 in (q.get('kp_list') or []):
                if (l1, l2) in seen:
                    continue
                seen.add((l1, l2))
                pair[(sub, l1)][l2] += 1

    kp_tree = {}
    for sub, c1 in by_kp.items():
        kids_of = []
        for l1, n1 in c1.most_common():
            l2s = []
            for l2, n2 in pair[(sub, l1)].most_common():
                l2s.append({
                    'name': l2, 'n': n2,
                    # 只用 nd['name']：topic_label() 会拼成
                    # 「一级 / 二级 · 题型」，而这里一二级已经是独立列了，
                    # 再拼一遍每行都会重复拖得很长。
                    'topics': [{'id': tid,
                                'name': (K.topic_node(tid) or {}).get('name', tid),
                                'n': n}
                               for tid, n in trio[(sub, l1, l2)].most_common()],
                })
            kids_of.append({'name': l1, 'n': n1, 'children': l2s})
        kp_tree[sub] = kids_of

    # 年级：派生字段（见 grade_map.py）。
    # 单独给一份 by_grade，前端加个概览块就能用，不必自己再算一遍。
    c_gd = Counter(q.get('grade') or _G0.UNKNOWN for q in qs)
    # 年级 × 科目：只看单科统计时全局数字会误导
    # （数学的高一题数 ≠ 整个题库的高一题数）。
    grade_by_sub = defaultdict(Counter)
    for q in qs:
        grade_by_sub[q.get('subject') or ''][q.get('grade') or _G0.UNKNOWN] += 1

    return _out({
        'ok': True, 'total': len(qs),
        'by_subject': dict(c_sub),
        'by_type': dict(c_type),
        'by_level': dict(c_lv),
        'by_grade': dict(c_gd),
        'by_grade_sub': {s: dict(c) for s, c in grade_by_sub.items()},
        'grades': _G0.GRADES,
        'by_kp': {s: c.most_common() for s, c in by_kp.items()},
        'kp_tree': kp_tree,
        'subjects': K.SUBJECTS,
    })


def cmd_kp_catalog(a):
    """返回六科知识点标准目录（一级 + 二级）

    前端组卷页据此渲染：选数学只出现数学的 12 个一级知识点，
    选物理只出现物理的 16 个，不会杂糅。
    """
    import kp_catalog as K
    # 题型挂题数（n_qs）来自**运行时反建**的索引 TOPICS[tid]['questions']。
    #
    # 这个进程若还没加载过题库，索引就是空的 —— n_qs 会全部返回 0。
    # 前端据此把题型灰显、禁止勾选（没挂题的题型勾了只会组出空卷），
    # 于是题型筛选整块失效，460 个题型一个都点不动，还不报错。
    # 所以出目录前必须先加载题库重建索引。
    try:
        K.rebuild_qindex(enrich(load_bank()))
    except Exception as _e:
        # 题库打不开不该让目录整个挂掉：没有题数只是显示灰，目录本身还能用
        try:
            sys.stderr.write('[kp-catalog] 题库索引重建失败：%s\n' % _e)
        except Exception:
            pass
    sub = getattr(a, 'subject', None)
    if sub and sub in K.CATALOG:
        return _out({'ok': True, 'subject': sub,
                     'catalog': K.catalog_for_frontend()[sub]})
    return _out({'ok': True, 'subjects': K.SUBJECTS,
                 'catalog': K.catalog_for_frontend()})


def cmd_compose(a):
    """按条件组卷

    支持：科目、题型、知识点、难度区间、题数、排除已练
    """
    cfg = json.loads(a.config) if a.config else {}
    qs = enrich(load_bank())
    prog = load_progress()

    sub = cfg.get('subject')
    if sub:
        qs = [q for q in qs if q.get('subject') == sub]
    types = cfg.get('types') or []
    if types:
        qs = [q for q in qs if q.get('type') in types]
    kps = cfg.get('kp') or []
    if kps:
        # 多值字段用「包含」匹配。
        # 同时认 kp（一级）与 kp2（二级）：
        # enrich() 会把 kp_list 归一到**一级**（二级被映射掉），
        # 只查 kp_list 会让「按二级知识点组卷」静默筛出 0 题 ——
        # 不报错、只是没题，最难排查的那种。
        qs = [q for q in qs
              if any(k in (q.get('kp_list') or [])
                     or k == q.get('kp')
                     or k == q.get('kp2')
                     for k in kps)]

    # 二级知识点（小知识点）：与一级是 **AND** —— 先圈大块，再收窄到小块。
    #
    # 不能塞进上面的 kps：那里是 OR，选「函数与导数 + 导数含参讨论」
    # 会被展开成「属于函数与导数 **或** 属于导数含参讨论」= 整个大块，
    # 收窄失效，用户以为选了小块、出卷却是大块的题。
    kp2s = set(x for x in (cfg.get('kp2') or []) if x)
    if kp2s:
        import kp_catalog as _K2
        def _l2_of(q):
            # kp2 字段是主来源；没写的（或只挂了题型标签的）
            # 再按题型节点的主归属回查，避免漏题。
            out = set()
            v = (q.get('kp2') or '').strip()
            if v:
                out.add(v)
            for tid in (q.get('topics') or []):
                nd = _K2.topic_node(tid)
                if nd:
                    out.add(nd['primary'][1])
            return out
        qs = [q for q in qs if _l2_of(q) & kp2s]

    # 年级：派生字段，多选取「命中任一」。
    # 与知识点是 AND —— 「高一 且 在函数与导数里」。
    #
    # 「未标注」要能显式筛出来：题库里凡是映射没覆盖到的题都是这个值，
    # 不让它可选的话，这批题在所有年级筛选下都消失，
    # 用户只会觉得「题少了」，看不出是筛掉了。
    grs = [x for x in (cfg.get('grades') or []) if x]
    if grs:
        import grade_map as _G3
        qs = [q for q in qs
              if (q.get('grade') or _G3.UNKNOWN) in grs]

    # 题型标签：多对多，命中任一即可。
    # 与知识点筛选是 AND 关系 —— 「三角函数里、且属于『面积最值』题型的题」。
    tps = cfg.get('topics') or []
    if tps:
        qs = [q for q in qs
              if any(t in (q.get('topics') or []) for t in tps)]
    lo, hi = cfg.get('diff_min', 0), cfg.get('diff_max', 1)
    qs = [q for q in qs if lo <= (q.get('difficulty') or 0.5) <= hi]

    if cfg.get('exclude_done'):
        qs = [q for q in qs if not prog.get(q['id'], {}).get('done')]

    count = cfg.get('count', 10)
    seed = cfg.get('seed')
    if seed is not None:
        import random
        random.seed(seed)
        random.shuffle(qs)

    # 按「新题 : 错题」配比抽题。
    # 纯随机会把错题淹没 —— 而错题才是提分的关键部分，
    # 所以配比单独可配（默认 70:30），用户在设置页调整。
    _c = load_config()
    picked = _pick_mixed(qs, prog, count, _c, cfg.get('mix'))
    # 按高考卷结构排序：选择 → 填空 → 解答。
    # 不排序的话跨年份选题会得到 [解答, 选择, 解答] 这类乱序，
    # 前端按连续同型分组会产生碎片化的分节标题。
    order = {'选择': 0, '填空': 1, '解答': 2}
    picked.sort(key=lambda q: (order.get(q.get('type'), 3),
                               q.get('year', ''), q.get('num', 0)))
    return _out({'ok': True, 'count': len(picked),
                 'candidates': len(qs), 'items': picked})


def cmd_compose_ref(a):
    """用**教辅例题**组卷（区别于 cmd_compose 的真题）

    教辅题 1395 道全部带答案，适合专项突破：
    按知识点挑一个薄弱块，直接刷 20 道同类题。

    筛选：科目 / 知识点(一级) / 小知识点 / 题型 / 题数 / 种子
    """
    try:
        import ref_bank as R
    except ImportError as e:
        return _fail('缺少模块: %s' % e)
    cfg = json.loads(a.config) if a.config else {}
    # 合并命令行参数。
    # 早期版本只读 cfg（前端走 --config），命令行传的 --subject/--kp
    # 会被**静默忽略** —— 调用方以为筛了某知识点，实际返回全库。
    # 这类"看起来成功、结果不对"的问题比报错更难发现。
    for k in ('subject', 'count', 'seed', 'per_topic'):
        v = getattr(a, k, None)
        if v is not None:
            cfg[k] = v
    for k in ('kp', 'kp2', 'types', 'topics', 'kinds'):
        v = getattr(a, k, None)
        if v:
            cfg[k] = [x.strip() for x in v.split(',') if x.strip()]

    items = R.all_items()
    sub = cfg.get('subject')
    if sub:
        items = [q for q in items if q.get('subject') == sub]
    kps = cfg.get('kp') or []
    if kps:
        items = [q for q in items if q.get('kp') in kps]
    kp2s = cfg.get('kp2') or []
    if kp2s:
        items = [q for q in items if q.get('kp2') in kp2s]
    types = cfg.get('types') or []
    if types:
        items = [q for q in items if q.get('qtype') in types]
    topics = cfg.get('topics') or []
    if topics:
        items = [q for q in items if q.get('topic') in topics]
    kinds = cfg.get('kinds') or []
    if kinds:
        items = [q for q in items if q.get('kind') in kinds]

    count = int(cfg.get('count') or 10)
    seed = cfg.get('seed')
    import random
    rng = random.Random(seed) if seed is not None else random.Random()
    rng.shuffle(items)

    # 每个题型节点最多取 2 道 —— 否则同一考法扎堆，
    # 刷 20 题实际只练了 3 种，达不到「覆盖面」的目的。
    per_topic = int(cfg.get('per_topic') or 2)
    used = {}
    picked = []
    for q in items:
        t = q.get('topic') or q['id']
        if used.get(t, 0) >= per_topic:
            continue
        used[t] = used.get(t, 0) + 1
        picked.append(q)
        if len(picked) >= count:
            break

    order = {'选择': 0, '填空': 1, '解答': 2}
    picked.sort(key=lambda q: (order.get(q.get('qtype'), 3),
                               q.get('kp') or '', q.get('topic') or ''))
    for i, q in enumerate(picked, 1):
        q['num'] = i
    return _out({'ok': True, 'count': len(picked),
                 'candidates': len(items), 'items': picked})


def _pick_mixed(qs, prog, count, cfg, override=None):
    """按新题/错题配比抽题。

    任一类不足时由另一类补足，保证总能凑够 count 道 ——
    否则题库里错题少的时候会组出半张卷子。
    """
    import random
    mix = override or {}
    new_pct = int(mix.get('new', cfg.get('mix_new_pct', 70)) or 0)
    wrong_pct = int(mix.get('wrong', cfg.get('mix_wrong_pct', 30)) or 0)
    tot = new_pct + wrong_pct
    if tot <= 0:                       # 配置异常时退化为默认配比
        new_pct, wrong_pct, tot = 70, 30, 100

    def is_wrong(q):
        r = prog.get(q.get('id')) or {}
        return int(r.get('wrong') or 0) > 0 and not r.get('done')

    wrong_pool = [q for q in qs if is_wrong(q)]
    wrong_ids = {q.get('id') for q in wrong_pool}
    new_pool = [q for q in qs if q.get('id') not in wrong_ids]

    n_wrong = min(len(wrong_pool), round(count * wrong_pct / tot))
    n_new = min(len(new_pool), count - n_wrong)
    n_wrong = min(len(wrong_pool), count - n_new)   # 新题不足 -> 错题补

    picked = []
    if n_wrong:
        picked += random.sample(wrong_pool, n_wrong)
    if n_new:
        picked += random.sample(new_pool, n_new)

    # 仍不足（两类都不够）-> 从剩余里补
    if len(picked) < count:
        got = {q.get('id') for q in picked}
        rest = [q for q in qs if q.get('id') not in got]
        picked += rest[:count - len(picked)]

    # 每日新题上限：只限制新题，错题复习不受限。
    # 否则孩子错题多的时候，会被上限卡住练不了错题。
    cap = int(cfg.get('daily_new_cap') or 0)
    if cap > 0:
        new_used = [q for q in picked if q.get('id') not in wrong_ids]
        if len(new_used) > cap:
            drop = {q.get('id') for q in new_used[:len(new_used) - cap]}
            picked = [q for q in picked if q.get('id') not in drop]
            # 砍掉的新题要用错题补回来，否则会组出半张卷子。
            # 错题池也空了才真的少给。
            got = {q.get('id') for q in picked}
            extra = [q for q in wrong_pool if q.get('id') not in got]
            picked += extra[:count - len(picked)]

    return picked


def probe_year(pdf_path, sub):
    """确定试卷年份。

    为什么不能只从文件名提取：
      用户把文件命名为「物理卷.pdf」「新建 PDF.pdf」很常见，
      此时年份变成 0000，而**两份无年份的同科目卷会共用
      P-0000-001 这类 ID，后导入的静默覆盖先导入的**。

    三级回退：
      1. 文件名
      2. PDF 正文前 3 页（真题卷首页通常有「2026 年普通高校…」）
      3. 都没有 → 返回 None，由调用方报错，拒绝用 0000 兜底
    """
    import re as _re
    name = os.path.basename(pdf_path)
    m = _re.search(r'(20\d{2})', name)
    if m:
        return m.group(1)

    # 文件名没有 → 读 PDF 正文
    try:
        import pymupdf
        doc = pymupdf.open(pdf_path)
        text = ''
        for i in range(min(3, doc.page_count)):
            text += doc[i].get_text() or ''
        doc.close()
        # 「2026 年普通高等学校招生…」这类表述
        m = _re.search(r'(20\d{2})\s*年', text)
        if m:
            return m.group(1)
        m = _re.search(r'(20\d{2})', text)
        if m:
            return m.group(1)
    except Exception:
        pass
    return None


def cmd_extract(a):
    """拆题入库：PDF → 题目 → **写回 bank.json**

    commit 默认开启。拆完不入库的话，界面显示「成功 16 题」
    但组卷页一题都找不到 —— 流程完全断裂。

    --no-commit 只在需要人工核对中间结果时用。
    """
    try:
        import pymupdf
        from extract3 import extract, extract_answer
        from gkbank import crop_figs
        import make_paper as MP
    except ImportError as e:
        return _fail('缺少依赖: %s' % e)

    if not os.path.exists(a.pdf):
        return _fail('文件不存在: %s' % a.pdf)

    sub = a.subject
    # P2-5：科目名非法时给出清晰报错，而不是 KeyError
    pre = None
    for k, v in SUBJ.items():
        if v == sub:
            pre = k
            break
    if pre is None:
        return _fail('未知科目「%s」，可选：%s' % (sub, '、'.join(SUBJ.values())))

    yr = probe_year(a.pdf, sub)

    if yr is None:
        return _fail(
            '无法确定年份。请把文件名改成含年份的形式（如 '
            '「2026江苏卷物理.pdf」），或确保 PDF 首页正文里有「2026 年」'
            '这类表述。\n不能用 0000 兜底 —— 两份无年份的同科目卷会共用 '
            'ID，后导入的会静默覆盖先导入的。')

    try:
        doc, qs, fb = extract(a.pdf, sub)
        os.makedirs(os.path.join(SLICE, sub), exist_ok=True)
        for q in qs:
            q['id'] = '%s-%s-%03d' % (pre, yr, q['num'])
        crop_figs(doc, qs, os.path.join(SLICE, sub), fb)
        for q in qs:
            MP._prep_fields(q)
            q['answer'] = extract_answer(q['ana_text'], len(q['opts']) >= 2)
            q['year'] = yr
            q['src'] = os.path.basename(a.pdf).replace('.pdf', '')
            # 新拆的题也要有 subtype，否则题型只能靠推测
            q.setdefault('subtype', '')

        if getattr(a, 'no_commit', False):
            return _out({'ok': True, 'count': len(qs), 'committed': False,
                         'year': yr, 'subject': sub, 'items': qs})

        return _commit(qs, sub, yr, os.path.basename(a.pdf))
    except Exception as e:
        traceback.print_exc(file=sys.stderr)
        return _fail('拆题失败: %s' % e)


def _commit(new_qs, sub, yr, src_name, batch=None, batch_name=None):
    """把新拆的题合并进 bank.json

    要点：
      - 先备份再写，写坏了能回滚
      - 按 ID 去重：同一份 PDF 导入两次不会产生重复题
      - 原子写：避免写一半崩溃导致整个题库损坏
      - 自动归入批次，便于日后整批删除
    """
    from datetime import datetime

    # 每次导入一个新批次：这样用户能单独删掉某一次导入的卷子。
    # 若沿用旧批次，混入后就再也分不开了。
    if not batch:
        batch = new_batch_id()
    for q in new_qs:
        q['batch'] = batch
    bank = load_bank()
    index = {q['id']: i for i, q in enumerate(bank)}

    added, updated, skipped = [], [], []
    for q in new_qs:
        qid = q['id']
        if qid in index:
            old = bank[index[qid]]
            # 已有条目：仅当新的信息更完整时才覆盖
            if len(q.get('ana_text') or '') > len(old.get('ana_text') or ''):
                bank[index[qid]] = q
                updated.append(qid)
            else:
                skipped.append(qid)
        else:
            bank.append(q)
            added.append(qid)

    if not added and not updated:
        return _out({'ok': True, 'count': len(new_qs), 'committed': True,
                     'added': 0, 'updated': 0,
                     'skipped': len(skipped),
                     'bank_total': len(bank),
                     'year': yr, 'subject': sub,
                     'note': '全部题目已存在，未做改动'})

    # 备份（只保留最近一份）
    if os.path.exists(BANK):
        try:
            with open(BANK + '.bak', 'w', encoding='utf-8') as f:
                json.dump(load_bank(), f, ensure_ascii=False, indent=1)
        except Exception as e:
            sys.stderr.write('备份失败（继续写入）: %s\n' % e)

    _save_bank(bank)

    # 登记批次元信息
    reg = load_batches()
    if batch not in reg:
        reg[batch] = {
            'name': batch_name or ('%s %s %s' % (src_name, sub, yr)).strip(),
            'time': datetime.now().strftime('%Y-%m-%d %H:%M'),
            'src': src_name,
            'n_tagged': len(new_qs),
        }
        save_batches(reg)

    return _out({'ok': True, 'count': len(new_qs), 'committed': True,
                 'added': len(added), 'updated': len(updated),
                 'skipped': len(skipped),
                 'bank_total': len(bank),
                 'batch': batch,
                 'year': yr, 'subject': sub,
                 'backup': BANK + '.bak'})


def _pool():
    """导出/组卷的题目池 = 真题(bank) + 教辅例题(ref_bank)

    两个库的题都可能被选进同一张卷，取题必须查两处。
    早期版本只查 bank，用教辅题组卷后点导出会报「未选中任何题目」。
    """
    out = list(enrich(load_bank()))
    try:
        import ref_bank as R
        have = {q.get('id') for q in out}
        for q in R.all_items():
            if q.get('id') not in have:
                out.append(q)
    except Exception:
        pass
    return out


def cmd_export_html(a):
    """导出试卷为 HTML（打印即 PDF）"""
    try:
        import build_html as BH
        import make_paper as MP
    except ImportError as e:
        return _fail('缺少依赖: %s' % e)

    ids = json.loads(a.ids) if a.ids else []
    picked = [q for q in _pool() if q['id'] in ids]
    if not picked:
        return _fail('未选中任何题目')

    sub = picked[0].get('subject', '数学')
    for q in picked:
        MP._prep_fields(q)
    secs = MP.auto_sections(sub, picked)
    meta = [('题量', '%d 题' % len(picked)),
            ('科目', sub),
            ('生成时间', a.title or '')]
    os.makedirs(a.outdir, exist_ok=True)
    path = BH.build_paper_html(picked, sub, a.title or '自动组卷',
                               a.title or '练习卷', meta, secs, a.outdir)
    return _out({'ok': True, 'path': path, 'count': len(picked)})


def cmd_export_docx(a):
    """导出试卷为 Word（可编辑，公式是原生 OMML）

    与 cmd_export_html 并存：
      HTML —— 单文件、图片内嵌、双击即看、打印即 PDF
      Word —— 可二次编辑（老师改题、调整分值）

    公式走 OMML 而非图片，所以在 Word 里**可双击编辑**。
    """
    try:
        import make_paper as MP
    except ImportError as e:
        return _fail('缺少依赖: %s' % e)

    ids = json.loads(a.ids) if a.ids else []
    picked = [q for q in _pool() if q['id'] in ids]
    if not picked:
        return _fail('未选中任何题目')

    sub = picked[0].get('subject', '数学')
    for q in picked:
        MP._prep_fields(q)
    secs = MP.auto_sections(sub, picked)
    meta = [('题量', '%d 题' % len(picked)),
            ('科目', sub),
            ('生成时间', a.title or '')]
    os.makedirs(a.outdir, exist_ok=True)

    # 末页空白页防护：先按 1.0 试排，末页纯空则按比例缩减留白重排
    last = 1.0
    for try_scale in (1.0, 0.85, 0.7, 0.55):
        path = MP.build_paper(picked, sub, a.title or '自动组卷',
                              a.title or '练习卷', meta, secs,
                              a.outdir, last_scale=try_scale)
        last = try_scale
        if not MP.has_blank_last_page(path):
            break
    return _out({'ok': True, 'path': path, 'count': len(picked)})


def cmd_export_answer(a):
    """导出答案与解析卷（Word）"""
    try:
        import make_paper as MP
    except ImportError as e:
        return _fail('缺少依赖: %s' % e)

    ids = json.loads(a.ids) if a.ids else []
    picked = [q for q in _pool() if q['id'] in ids]
    if not picked:
        return _fail('未选中任何题目')

    sub = picked[0].get('subject', '数学')
    for q in picked:
        MP._prep_fields(q)
    # 必须与试卷用同一套排序与编号，否则答案卷第 N 题
    # 对不上试卷第 N 题。曾经因为不调用它，人工录入的题
    # （num 默认 0）在答案卷里全是「0．」，且顺序与试卷不一致。
    ordered = MP.order_and_number(sub, picked)
    meta = [('题量', '%d 题' % len(picked)), ('科目', sub)]
    os.makedirs(a.outdir, exist_ok=True)
    src = '%s %s' % (picked[0].get('year', ''), sub)
    path = MP.build_answer(ordered, sub, '答案与解析',
                           a.title or '练习卷', meta, src, a.outdir)
    return _out({'ok': True, 'path': path, 'count': len(picked)})


def cmd_topic_list(a):
    """列题型节点。

    可按 科目/一级/二级 过滤；带挂题数。
    has_qs=true 时只返回已挂题的（用于选题时缩小范围）。
    """
    import kp_catalog as K
    sub = a.subject or None
    out = []
    for tid, nd in K.TOPICS.items():
        if sub and nd['subject'] != sub:
            continue
        if a.l1 and nd['primary'][0] != a.l1:
            continue
        if a.l2 and nd['primary'][1] != a.l2:
            continue
        if getattr(a, 'has_qs', False) and not nd['questions']:
            continue
        out.append({
            'id': tid, 'name': nd['name'], 'subject': nd['subject'],
            'primary': list(nd['primary']), 'cross': nd['cross'],
            'n_qs': len(nd['questions']),
            'label': K.topic_label(tid),
        })
    out.sort(key=lambda x: (-x['n_qs'], x['id']))
    return _out({'ok': True, 'items': out, 'count': len(out)})


def cmd_topic_link(a):
    """把题目挂到题型上（多对多，幂等）。

    payload: {"qid": "M-2021-001", "topics": ["M-T-005", "M-T-137"]}
    传空列表 = 清空该题的题型标签。
    """
    import kp_catalog as K
    try:
        payload = json.loads(a.payload)
    except Exception as e:
        return _fail('payload 解析失败: %s' % e)
    qid = payload.get('qid')
    tids = payload.get('topics') or []
    if not qid:
        return _fail('缺少 qid')

    bank = load_bank()
    tgt = next((q for q in bank if q.get('id') == qid), None)
    if not tgt:
        return _fail('找不到题目: %s' % qid)

    # 校验题型ID，避免把错ID写进题库
    bad = [t for t in tids if not K.topic_node(t)]
    if bad:
        return _fail('题型ID 不存在: %s' % bad)

    tgt['topics'] = list(dict.fromkeys(tids))   # 去重保序
    K.rebuild_qindex(enrich(bank))
    _save_bank(bank)
    return _out({'ok': True, 'id': qid, 'topics': tgt['topics'],
                 'labels': [K.topic_label(t) for t in tgt['topics']]})


def cmd_question_topics(a):
    """查某题挂了哪些题型"""
    import kp_catalog as K
    bank = enrich(load_bank())
    q = next((x for x in bank if x.get('id') == a.qid), None)
    if not q:
        return _fail('找不到题目: %s' % a.qid)
    return _out({'ok': True, 'id': a.qid,
                 'topics': [{'id': t, 'label': K.topic_label(t)}
                            for t in (q.get('topics') or [])
                            if K.topic_node(t)]})


def cmd_batch_list(a):
    """列出所有批次及其题数（题数实时统计）"""
    return _out({'ok': True, 'items': batch_stats(),
                 'total': len(load_bank())})


def cmd_batch_tag(a):
    """给现有题目打批次标记

    --name    批次名（默认「已有题目」）
    --ids     逗号分隔的题目ID；不传则标记**所有未标记**的题目

    典型用法：给早期导入的 216 道真题统一打标，
    之后新导入的自动是新批次，可按批次整体删除。
    """
    from datetime import datetime
    bank = load_bank()
    reg = load_batches()

    ids = None
    if getattr(a, 'ids', None):
        ids = [x.strip() for x in a.ids.split(',') if x.strip()]

    name = a.name or '已有题目'
    bid = getattr(a, 'batch_id', None) or new_batch_id()

    force = bool(getattr(a, 'all', False))
    if ids:
        wanted = set(ids)
        targets = [q for q in bank if q['id'] in wanted]
    elif force:
        # --all：重新标记**全部**题目，会覆盖已有批次。
        # 用于「之前标错了，想统一重来」的场景。
        targets = list(bank)
    else:
        # 默认只标「还没打过标记」的，避免重复打标覆盖已有批次
        targets = [q for q in bank if not q.get('batch')]

    if not targets:
        return _fail('没有符合条件的题目（可能都已标记过）')

    for q in targets:
        q['batch'] = bid

    reg[bid] = {
        'name': name,
        'time': datetime.now().strftime('%Y-%m-%d %H:%M'),
        'src': getattr(a, 'src', '') or '手工标记',
        'n_tagged': len(targets),     # 仅记录当初标记了多少，实际题数以统计为准
    }
    _save_bank(bank)
    save_batches(reg)
    return _out({'ok': True, 'batch_id': bid, 'name': name,
                 'tagged': len(targets), 'items': batch_stats(bank)})


def cmd_batch_delete(a):
    """按批次删除题目

    高危操作，三重保护：
      1. 必须显式传 --batch（不允许空值误删全部）
      2. 先备份 bank.json
      3. 同时清理 progress.json 里对应的练习记录，
         否则 progress 会越攒越多，且复习页混着已删题目

    切片图片**不删**：图片按题目ID命名但可能跨批次复用，
    误删会破坏其他批次的题目。磁盘占用可接受。
    """
    bid = getattr(a, 'batch', None)
    if not bid:
        return _fail('必须指定 --batch')

    bank = load_bank()
    keep = [q for q in bank if (q.get('batch') or '未标记') != bid]
    removed = [q for q in bank if (q.get('batch') or '未标记') == bid]

    if not removed:
        return _fail('批次「%s」下没有题目' % bid)

    removed_ids = {q['id'] for q in removed}

    # 清理练习记录
    prog = load_progress()
    prog_keep = {k: v for k, v in prog.items() if k not in removed_ids}
    n_prog = len(prog) - len(prog_keep)

    _save_bank(keep)
    save_progress(prog_keep)

    # 批次表：题数归零后仍保留记录（留个痕迹），但标为已清空
    reg = load_batches()
    if isinstance(reg.get(bid), dict):
        # 原来写成 `if 'datetime' in dir()` —— 在全局命名空间里查 datetime，
        # 条件恒假，cleared 被赋成空串，等于没记录清空时间。
        from datetime import datetime as _dt
        reg[bid]['cleared'] = _dt.now().strftime('%Y-%m-%d %H:%M')
        save_batches(reg)

    # 不返回 items（全量批次统计）：删一批会打印十几条批次明细，
    # 而前端只用 removed / progress_cleaned / remaining 三个数。
    return _out({'ok': True, 'batch': bid,
                 'removed': len(removed),
                 'progress_cleaned': n_prog,
                 'remaining': len(keep)})


def cmd_kp_notes(a):
    """取知识点讲解

    按层级优先：题型 > 小知识点 > 大知识点。
    前端右侧面板用；没有内容时返回空 items，由前端提示可补充。
    """
    try:
        import kp_notes as N
    except ImportError as e:
        return _fail('缺少模块: %s' % e)
    r = N.get(a.subject or '数学', getattr(a, 'l1', None),
              getattr(a, 'l2', None), getattr(a, 'topic', None))
    # 题目**只返回摘要**（题干/选项/答案），不带详解。
    # 详解点开时才单独取 —— 一次传几十道题的全文会很慢。
    r['example_list'] = N.qsummary(r.get('examples'))
    r['variant_list'] = N.qsummary(r.get('variants'))
    r['ok'] = True
    r['coverage'] = N.stats()
    return _out(r)


def cmd_ref_questions(a):
    """按题目 ID 取参考题目正文（含详解）

    支持 --ids 逗号分隔批量取。
    用于讲解面板里「点开某道典例/变式」时加载详情。
    """
    try:
        import kp_notes as N
    except ImportError as e:
        return _fail('缺少模块: %s' % e)
    ids = [x.strip() for x in (getattr(a, 'ids', '') or '').split(',') if x.strip()]
    if not ids:
        return _fail('请传 --ids')
    return _out({'ok': True, 'items': N.questions(ids)})


def cmd_kp_notes_stats(a):
    """知识点讲解的覆盖情况"""
    try:
        import kp_notes as N
    except ImportError as e:
        return _fail('缺少模块: %s' % e)
    return _out({'ok': True, **N.stats()})


# ---------------- 记忆曲线 ----------------
# 阶梯不再硬编码，改从 config.json 读（「设置」页签可改）
def _ladder():
    return {int(k): int(v) for k, v in (load_config().get('ladder') or {}).items()}


def cmd_get_config(a):
    """读复习参数（含默认值说明，供设置页渲染）"""
    return _out({'ok': True, 'config': load_config(),
                 'defaults': DEFAULT_CONFIG})


def cmd_set_config(a):
    """写复习参数

    校验要点：
      - ladder 的 key 必须是整数字符串，value 必须 >=0
      - 必须有 "-1" 档且 > 0，否则错题永远 0 天后到期（等于不复习）
      - 配比之和必须为 100
    校验不通过就原样返回错误，**不落盘**（半截配置更危险）。
    """
    try:
        cfg = json.loads(a.config)
    except Exception as e:
        return _fail('config 解析失败: %s' % e)

    # 先与默认值合并再校验。
    # 否则前端只传改动的那几项时，其余字段取 0，会冒出一堆假报错
    # （如「阶梯不能为空」「等级上限必须 >= 1」）。
    merged = dict(DEFAULT_CONFIG)
    for k in DEFAULT_CONFIG:
        if k in cfg:
            merged[k] = cfg[k]
    cfg = merged

    errs = []
    lad = cfg.get('ladder') or {}
    if not lad:
        errs.append('阶梯不能为空')
    for k, v in lad.items():
        try:
            int(k); int(v)
        except Exception:
            errs.append('阶梯值必须是整数: %s=%s' % (k, v))
            continue
        if int(v) < 0:
            errs.append('间隔天数不能为负: %s=%s' % (k, v))
    if lad and int(lad.get('-1', 0) or 0) <= 0:
        errs.append('「错1次」档必须 > 0 天，否则错题不会重新出现')

    mix = int(cfg.get('mix_new_pct', 0) or 0) + int(cfg.get('mix_wrong_pct', 0) or 0)
    if mix != 100:
        errs.append('新题与错题配比之和必须是 100，当前 %d' % mix)

    if int(cfg.get('max_level', 0) or 0) < 1:
        errs.append('等级上限必须 >= 1')

    if errs:
        return _fail('；'.join(errs))

    save_config(cfg)
    return _out({'ok': True, 'config': cfg})


def cmd_progress(a):
    """写入一次练习结果，自动更新复习等级与下次复习日"""
    from datetime import date, timedelta
    prog = load_progress()
    try:
        payload = json.loads(a.payload)
    except Exception as e:
        return _fail('payload 解析失败: %s' % e)

    today = date.today().isoformat()
    _cfg = load_config()
    LADDER = {int(k): int(v) for k, v in (_cfg.get('ladder') or {}).items()}
    CFG_MAXLV = int(_cfg.get('max_level') or 5)
    CFG_W2LV = int(_cfg.get('wrong2_level') or -2)
    CFG_DONELV = int(_cfg.get('done_level') or 3)
    updated = []
    for item in (payload if isinstance(payload, list) else [payload]):
        qid = item.get('id')
        if not qid:
            continue
        rec = prog.get(qid) or {
            'id': qid, 'count': 0, 'wrong': 0, 'level': 0,
            'last': None, 'last_ok': None, 'next': None, 'done': False}
        correct = bool(item.get('correct'))
        rec['count'] = int(rec.get('count') or 0) + 1
        if not correct:
            rec['wrong'] = int(rec.get('wrong') or 0) + 1
        rec['last'] = today
        rec['last_ok'] = correct
        if correct:
            # 关键：等级 <=0（未练或刚错）时，做对直接跳到 1。
            # 若只是 +1，错题做对后等级变 0，而 0 对应间隔 0 天（未练习态），
            # 会导致刚做对的题立刻被判为到期。
            cur = int(rec.get('level') or 0)
            rec['level'] = 1 if cur <= 0 else min(CFG_MAXLV, cur + 1)
        else:
            # 做错 → 退回最低档；累计错够次数压到最低档
            rec['level'] = (CFG_W2LV if int(rec.get('wrong') or 0) >= abs(CFG_W2LV)
                            else -1)
        gap = LADDER.get(rec['level'], 7)
        rec['next'] = (date.today() + timedelta(days=gap)).isoformat() if gap else today
        rec['done'] = rec['level'] >= CFG_DONELV
        prog[qid] = rec
        updated.append(rec)

    save_progress(prog)
    return _out({'ok': True, 'updated': len(updated), 'records': updated})


def cmd_due(a):
    """列出到期需复习的题目（含完整题目内容）"""
    from datetime import date
    prog = load_progress()
    today = date.today().isoformat()
    bank = {q['id']: q for q in enrich(load_bank())}

    due, upcoming = [], []
    for qid, v in prog.items():
        if v.get('done') or not v.get('next'):
            continue
        q = bank.get(qid)
        if not q:
            continue
        q = dict(q)
        q['_progress'] = v
        # 尚未做对的题才进队列：错题与低等级题
        (due if v['next'] <= today else upcoming).append(q)

    due.sort(key=lambda q: q['_progress'].get('next', ''))
    upcoming.sort(key=lambda q: q['_progress'].get('next', ''))

    return _out({
        'ok': True,
        'count': len(due),
        'items': due,
        # 排队中（已练过但还没到复习日）。
        # 没有它的话，刚做错的题要等 2 天后才出现，
        # 界面上会「凭空消失」，家长以为没记上。
        'upcoming_count': len(upcoming),
        'upcoming': upcoming,
        'today': today,
    })


def cmd_export_progress(a):
    """导出练习记录（备份用）—— 这是防数据丢失的关键功能"""
    prog = load_progress()
    path = a.outdir or os.path.join(DATA_DIR, 'progress_backup.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(prog, f, ensure_ascii=False, indent=1)
    return _out({'ok': True, 'path': path, 'count': len(prog)})


def main():
    ap = argparse.ArgumentParser(description='高考题库桥接 CLI')
    sub = ap.add_subparsers(dest='cmd', required=True)

    sub.add_parser('health').set_defaults(fn=cmd_health)

    p = sub.add_parser('list')
    p.add_argument('--subject'); p.add_argument('--q')
    p.add_argument('--limit', type=int)
    p.set_defaults(fn=cmd_list)

    sub.add_parser('stats').set_defaults(fn=cmd_stats)

    p = sub.add_parser('kp-catalog')
    p.add_argument('--subject')
    p.set_defaults(fn=cmd_kp_catalog)

    p = sub.add_parser('compose')
    p.add_argument('--config')
    p.set_defaults(fn=cmd_compose)

    p = sub.add_parser('extract')
    p.add_argument('--pdf', required=True)
    p.add_argument('--subject', required=True)
    p.add_argument('--no-commit', action='store_true',
                   help='只拆题不写回题库（用于人工核对中间结果）')
    p.set_defaults(fn=cmd_extract)

    p = sub.add_parser('export-html')
    p.add_argument('--ids', required=True)
    p.add_argument('--outdir', required=True)
    p.add_argument('--title')
    p.set_defaults(fn=cmd_export_html)

    # Word 导出：可二次编辑（老师改题、调整分值）。
    # 此前 build_paper() 一直存在但没接进 CLI，打包后的应用里用不了。
    p = sub.add_parser('export-docx')
    p.add_argument('--ids', required=True)
    p.add_argument('--outdir', required=True)
    p.add_argument('--title')
    p.set_defaults(fn=cmd_export_docx)

    p = sub.add_parser('export-answer')
    p.add_argument('--ids', required=True)
    p.add_argument('--outdir', required=True)
    p.add_argument('--title')
    p.set_defaults(fn=cmd_export_answer)

    p = sub.add_parser('progress')
    p.add_argument('--payload', required=True)
    p.set_defaults(fn=cmd_progress)

    sub.add_parser('due').set_defaults(fn=cmd_due)

    p = sub.add_parser('topic-list')
    p.add_argument('--subject'); p.add_argument('--l1'); p.add_argument('--l2')
    p.add_argument('--has-qs', action='store_true')
    p.set_defaults(fn=cmd_topic_list)

    p = sub.add_parser('topic-link')
    p.add_argument('--payload', required=True)
    p.set_defaults(fn=cmd_topic_link)

    p = sub.add_parser('question-topics')
    p.add_argument('--qid', required=True)
    p.set_defaults(fn=cmd_question_topics)

    p = sub.add_parser('kp-notes')
    p.add_argument('--subject'); p.add_argument('--l1')
    p.add_argument('--l2'); p.add_argument('--topic')
    p.set_defaults(fn=cmd_kp_notes)

    p = sub.add_parser('ref-questions')
    p.add_argument('--ids', required=True)
    p.set_defaults(fn=cmd_ref_questions)

    p = sub.add_parser('kp-notes-stats')
    p.set_defaults(fn=cmd_kp_notes_stats)

    p = sub.add_parser('compose-ref')
    p.add_argument('--config')
    p.add_argument('--subject'); p.add_argument('--kp')
    p.add_argument('--types'); p.add_argument('--count', type=int)
    p.add_argument('--seed'); p.add_argument('--out')
    p.set_defaults(fn=cmd_compose_ref)

    p = sub.add_parser('batch-list')
    p.set_defaults(fn=cmd_batch_list)

    p = sub.add_parser('batch-tag')
    p.add_argument('--name'); p.add_argument('--ids')
    p.add_argument('--batch-id'); p.add_argument('--src')
    p.add_argument('--all', action='store_true')
    p.set_defaults(fn=cmd_batch_tag)

    p = sub.add_parser('batch-delete')
    p.add_argument('--batch', required=True)
    p.set_defaults(fn=cmd_batch_delete)

    p = sub.add_parser('get-config')
    p.set_defaults(fn=cmd_get_config)

    p = sub.add_parser('set-config')
    p.add_argument('--config', required=True)
    p.set_defaults(fn=cmd_set_config)

    p = sub.add_parser('export-progress')
    p.add_argument('--outdir')
    p.set_defaults(fn=cmd_export_progress)

    a = ap.parse_args()
    try:
        return a.fn(a)
    except SystemExit:
        raise
    except Exception as e:
        traceback.print_exc(file=sys.stderr)
        return _fail(e)


if __name__ == '__main__':
    sys.exit(main())
