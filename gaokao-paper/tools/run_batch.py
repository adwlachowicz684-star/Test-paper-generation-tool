# -*- coding: utf-8 -*-
r"""一批题目的一键流水线：入库 → 导出 → 逐题核对 → 三项回归。

    python3 tools/run_batch.py 17                 # 正常跑：入库 + 后续全部
    python3 tools/run_batch.py 17 --no-commit     # 只跑后续（已入库，重跑核对）
    python3 tools/run_batch.py 17 --title '导数含参讨论'

把原来需要手敲的 6~8 条命令合成一条，并且**只在出问题时展开细节**：
全部通过时输出 6 行左右；任何一步失败才打印该步的报错原文。
这是为了省输出——从前每批要读几百行输出，绝大多数都是"正常"的重复信息。

子命令返回码非 0 即视为失败，会立即停下并打印失败步骤的尾部输出。

产物落在 html/ 和 out/，文件名含批次号，不覆盖别的批次。
"""
import argparse
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
BANK = os.path.join(ROOT, 'data', 'bank.json')
PDF_DEFAULT = '/data/inputs/2024高中数学热点题型归纳完整解析版.pdf'

OK, FAIL, WARN = '✓', '✗', '!'


def run(cmd, tag, tail=25):
    """跑子命令。成功返回 (True, '')；失败返回 (False, 尾部输出)。"""
    p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    if p.returncode == 0:
        return True, ''
    out = (p.stdout or '') + (p.stderr or '')
    lines = [l for l in out.strip().split('\n') if l.strip()]
    return False, '\n'.join('      ' + l for l in lines[-tail:])


def grep1(text, pat, default='?'):
    """从子命令输出里取一个数字/状态，避免打印整段输出。"""
    m = re.search(pat, text)
    return m.group(1) if m else default


def run_capture(cmd):
    p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    return p.returncode, (p.stdout or '') + (p.stderr or '')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('batch', help='批次号，如 17')
    ap.add_argument('--no-commit', action='store_true',
                    help='跳过入库，只跑导出/核对/回归')
    ap.add_argument('--title', help='试卷标题，默认「第NN批」')
    ap.add_argument('--skip-docs', action='store_true',
                    help='跳过文档自检（改了底层代码时才需要跑）')
    a = ap.parse_args()

    n = a.batch
    title = a.title or ('第%s批' % n)
    commit_py = os.path.join(HERE, 'commit_batch%s.py' % n)
    steps = []

    # ── 1. 入库 ──────────────────────────────────────────────
    before = set()
    if os.path.exists(BANK):
        before = {q['id'] for q in json.load(open(BANK, encoding='utf-8'))}

    if a.no_commit:
        steps.append((OK, '入库      跳过（--no-commit）'))
    else:
        if not os.path.exists(commit_py):
            print('%s 找不到 %s' % (FAIL, os.path.basename(commit_py)))
            return 1
        ok, err = run([sys.executable, 'tools/commit_batch%s.py' % n], '入库')
        if not ok:
            print('%s 入库失败（整批已拒绝，题库未改动）' % FAIL)
            print(err)
            return 1

    bank = json.load(open(BANK, encoding='utf-8'))
    after = {q['id'] for q in bank}
    ids = sorted(after - before)
    if not ids:
        # --no-commit 或重跑：靠 batch 字段兜底
        pat = re.compile(r'第0*%s批' % n)
        ids = sorted(q['id'] for q in bank
                     if pat.search(str(q.get('batch') or '')))
    if not ids:
        print('%s 没找到本批的题：入库前后 ID 无变化，batch 字段也匹配不上'
              % WARN)
        print('     若首次入库，检查 commit_batch%s.py 里的 BATCH 常量'
              '是否含「第%s批」' % (n, n))
        return 1
    steps.append((OK, '入库      %d 题  %s ~ %s' % (len(ids), ids[0], ids[-1])))

    idjson = json.dumps(ids, ensure_ascii=False)

    # ── 2. 导出三份 ──────────────────────────────────────────
    # 三个导出命令都会自己加前缀：试卷- / 试卷- / 答案与解析-。
    # title 里再拼一次前缀会得到「试卷-试卷-…」，文件名对不上就查不到产物。
    exports = [
        ('HTML', ['py/main.py', 'export-html', '--ids', idjson,
                  '--outdir', 'html', '--title', title]),
        ('Word', ['py/main.py', 'export-docx', '--ids', idjson,
                  '--outdir', 'out', '--title', title]),
        ('答案', ['py/main.py', 'export-answer', '--ids', idjson,
                  '--outdir', 'out', '--title', title]),
    ]
    paths = {}
    for name, cmd in exports:
        ok, err = run([sys.executable] + cmd, name)
        if not ok:
            print('%s 导出%s失败' % (FAIL, name))
            print(err)
            return 1
        paths[name] = cmd[-1]
    html_p = os.path.join('html', '试卷-%s.html' % title)
    docx_p = os.path.join('out', '试卷-%s.docx' % title)
    ans_p = os.path.join('out', '答案与解析-%s.docx' % title)
    n_fig = sum(len(q.get('figs') or []) for q in bank if q['id'] in set(ids))
    steps.append((OK, '导出      HTML / Word / 答案卷'
                     + ('（含图 %d 张）' % n_fig if n_fig else '')))

    # ── 3. 逐题核对两端 ──────────────────────────────────────
    ok, err = run([sys.executable, 'tools/check_render.py', html_p, docx_p]
                  + ids + ['--quiet'], '核对')
    if not ok:
        print('%s 两端核对有题缺失：' % FAIL)
        print(err)
        return 1
    rc, out = run_capture([sys.executable, 'tools/check_render.py',
                           html_p, docx_p] + ids + ['--quiet'])
    steps.append((OK, '两端核对  %s' % grep1(out, r'两端一致:\s*(\S+ / \S+)')))

    # ── 4. 三项回归 ──────────────────────────────────────────
    rc, out = run_capture([sys.executable, 'tools/selftest.py'])
    be = grep1(out, r'(通过 \d+ / \d+|通过\s+\S+\s*/\s*\S+)')
    if rc != 0:
        print('%s 后端回归失败' % FAIL)
        print('\n'.join('      ' + l for l in out.strip().split('\n')[-25:]))
        return 1
    rc2, out2 = run_capture(['node', 'tools/test.mjs'])
    fe = grep1(out2, r'(PASS \d+ / \d+|\d+ / \d+ passing)')
    if rc2 != 0:
        print('%s 前端回归失败' % FAIL)
        print('\n'.join('      ' + l for l in out2.strip().split('\n')[-20:]))
        return 1
    steps.append((OK, '回归      后端 %s   前端 %s' % (be, fe)))

    if not a.skip_docs:
        import shutil
        dst = '/data/skills/gaokao-import'
        src = os.path.join(ROOT, 'skill')
        if os.path.isdir(dst):
            shutil.rmtree(dst)
        os.makedirs(dst)
        for f in os.listdir(src):
            s, d = os.path.join(src, f), os.path.join(dst, f)
            shutil.copytree(s, d) if os.path.isdir(s) else shutil.copy2(s, d)
        rc3, out3 = run_capture([sys.executable, 'tools/check_skill_docs.py'])
        de = grep1(out3, r'(通过 \d+ / \d+)')
        if rc3 != 0:
            print('%s 文档自检失败' % FAIL)
            print('\n'.join('      ' + l for l in out3.strip().split('\n')[-20:]))
            return 1
        steps.append((OK, '文档自检  %s' % de))

    # ── 5. 计划清单（顺手刷新，待录数才会更新）────────────────
    rc4, out4 = run_capture([sys.executable, 'tools/make_plan.py'])
    pend = grep1(out4, r'待录 (\d+)')
    tot = grep1(out4, r'总题 (\d+)')
    steps.append((OK, '清单      总 %s  待录 %s' % (tot, pend)))

    # ── 6. 勘误表（本批若有改答案的题，提醒补 A_MANUAL）────────
    rc5, out5 = run_capture([sys.executable, 'tools/gen_errata.py'])
    if rc5 != 0:
        print('%s 勘误表生成失败' % FAIL)
        print('\n'.join('      ' + l for l in out5.strip().split('\n')[-15:]))
        return 1
    ne = grep1(out5, r'(A 类 \d+ / B 类 \d+ / C 类 \d+ / D 类 \d+)')
    steps.append((OK, '勘误表    %s' % ne))

    # ── 7. 题型页码索引（并行录入分工表，随进度刷新）────────────
    rc7, out7 = run_capture([sys.executable, 'tools/make_index.py'])
    if rc7 != 0:
        print('%s 页码索引生成失败' % FAIL)
        print('\n'.join('      ' + l for l in out7.strip().split('\n')[-15:]))
        return 1
    steps.append((OK, '页码索引  tools/make_index.py 已刷新'))

    # ── 汇总 ────────────────────────────────────────────────
    print('第%s批 流水线完成' % n)
    for sym, txt in steps:
        print('  %s %s' % (sym, txt))
    print('')
    print('  产物：')
    print('    %s' % html_p)
    print('    %s' % docx_p)
    print('    %s' % ans_p)
    print('    原书勘误表.md')
    print('')
    print('  本批若改过原书答案，记得把结论补进 tools/gen_errata.py 的 A_MANUAL。')
    return 0


if __name__ == '__main__':
    sys.exit(main())
