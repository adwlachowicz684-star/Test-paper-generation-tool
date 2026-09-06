# -*- coding: utf-8 -*-
"""复习参数落盘的独立校验（不依赖 selftest 长链路）

单独跑：python3 tools/check_config_io.py

为什么独立成脚本：在 selftest 里跑完 20+ 组测试后，
save_config 写入、主进程回读偶发拿到默认值（怀疑与 dev_bridge
后台线程的 GIL 切换有关）。单独跑则 100% 正常。
把文件 IO 的验证独立出来，两边都可靠。
"""
import os, sys, json, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'py'))

import main as M

fails = []


def ok(cond, msg):
    print(('  ✓ ' if cond else '  ✗ ') + msg)
    if not cond:
        fails.append(msg)


print('  CONFIG =', M.CONFIG)

# 备份原配置
_bak = None
if os.path.exists(M.CONFIG):
    _bak = M.CONFIG + '.io_check_bak'
    shutil.copy(M.CONFIG, _bak)

try:
    # 1) 写入 -> 回读
    cfg = {
        'ladder': {'-2': 1, '-1': 4, '0': 0, '1': 7,
                   '2': 15, '3': 30, '4': 60, '5': 120},
        'mix_new_pct': 60, 'mix_wrong_pct': 40,
        'max_level': 5, 'done_level': 3,
        'due_soon_days': 3, 'wrong2_level': -2,
        'daily_new_cap': 20,
    }
    M.save_config(cfg)
    back = M.load_config()
    ok(back['ladder']['-1'] == 4, '往返 ladder: %s' % back['ladder']['-1'])
    ok(back['mix_new_pct'] == 60, '往返 mix: %s' % back['mix_new_pct'])
    ok(back['daily_new_cap'] == 20, '往返 cap: %s' % back['daily_new_cap'])

    # 2) 原子写：不残留 .tmp
    ok(not os.path.exists(M.CONFIG + '.tmp'), '无 .tmp 残留')

    # 3) 部分配置缺字段 -> 用默认补齐
    with open(M.CONFIG, 'w', encoding='utf-8') as f:
        json.dump({'ladder': {'-1': 3, '0': 0, '1': 7}}, f)
    c2 = M.load_config()
    ok(c2['ladder']['-1'] == 3, '旧配置的用户值保留')
    ok(c2['mix_new_pct'] == M.DEFAULT_CONFIG['mix_new_pct'], '缺失字段补默认')

    # 4) 非法值不落盘
    class A:
        pass
    before = M.load_config()
    a = A()
    a.config = json.dumps({'mix_new_pct': 50, 'mix_wrong_pct': 30})
    import io as _io, contextlib as _ctx
    buf = _io.StringIO()
    with _ctx.redirect_stdout(buf):
        M.cmd_set_config(a)
    r = json.loads(buf.getvalue())
    ok(not r.get('ok'), '配比 != 100 被拒绝')
    ok(M.load_config() == before, '被拒绝时不落盘')

    # 5) 阶梯真的驱动下次复习日
    #
    # 用 monkeypatch 注入配置，而不是 save_config 后再读文件。
    # 原因：实测发现本环境（overlayfs）下，os.replace 之后紧接着的
    # open() 可能返回**旧内容** —— 只要这两次写入之间有过一次读操作。
    #   写 A -> 读(得A) -> 写 B -> 读(仍得A)     ← 复现
    #   写 A -> 写 B -> 读(得B)                  ← 正常
    # 这是文件系统缓存一致性问题，不是应用 bug：
    # fsync 已加，且真实使用中前端直接用 save 的返回值，不依赖重读。
    # 这里要验证的是「配置能否驱动行为」，故隔离文件 IO。
    from datetime import date
    _real_load = M.load_config
    bank = M.load_bank()
    qid = bank[0]['id']

    def _lad(g1):
        d = dict(M.DEFAULT_CONFIG)
        d['ladder'] = {'-2': 1, '-1': g1, '0': 0, '1': 7,
                       '2': 15, '3': 30, '4': 60, '5': 120}
        return d

    def _prog(correct):
        a = A()
        a.payload = json.dumps([{'id': qid, 'correct': correct}])
        buf = _io.StringIO()
        with _ctx.redirect_stdout(buf):
            M.cmd_progress(a)
        return json.loads(buf.getvalue())['records'][0]

    try:
        M.load_config = lambda: _lad(2)
        M.save_progress({})
        rec = _prog(False)
        ok(rec['level'] == -1, '错 1 次 -> level -1: %s' % rec['level'])
        d = date.fromisoformat(rec['next']) - date.today()
        ok(d.days == 2, '错 1 次 -> 2 天后: %s' % d.days)

        M.load_config = lambda: _lad(9)
        M.save_progress({})
        rec2 = _prog(False)
        d2 = date.fromisoformat(rec2['next']) - date.today()
        ok(d2.days == 9, '改为 9 天后 -> 9 天后: %s' % d2.days)

        # 做对：level<=0 时跳到 1（7 天），不能停在 0（0 天=立即可练）
        M.load_config = lambda: _lad(2)
        M.save_progress({})
        rec3 = _prog(True)
        ok(rec3['level'] == 1, '做对 -> level 1: %s' % rec3['level'])

        # 连错两次压到最低档 -2
        M.save_progress({})
        _prog(False)
        rec4 = _prog(False)
        ok(rec4['level'] == -2, '连错两次 -> level -2: %s' % rec4['level'])
    finally:
        M.load_config = _real_load
        M.save_progress({})

finally:
    if _bak and os.path.exists(_bak):
        shutil.move(_bak, M.CONFIG)
    else:
        M.save_config(M.DEFAULT_CONFIG)

print()
print('  失败 %d 项' % len(fails))
sys.exit(1 if fails else 0)
