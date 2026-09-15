# -*- coding: utf-8 -*-
"""第137批样卷：从 bank 取 M-H1163~M-H1172 生成 HTML + Word"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, 'py'))
sys.path.insert(0, HERE)

import hand_input, kp_catalog as K
import build_html as BH
import make_paper as MP

IDS = ['M-H%04d' % i for i in range(1412, 1415)]
TITLE = '2024 高中数学热点题型归纳'
SUB = '第137批-绝对值最值与计数回填'
META = [('适用范围', '高三二轮复习'), ('题量', '3 题'), ('专题', '绝对值最值 · 平面染色 · 停车排列')]

def main():
    bank = hand_input.load()
    by = {q['id']: q for q in bank}
    qs = [dict(by[i]) for i in IDS if i in by]
    miss = [i for i in IDS if i not in by]
    if miss:
        print('缺:', miss); return 1
    secs = MP.auto_sections('数学', qs)
    p = BH.build_paper_html(qs, '数学', TITLE, SUB, META, secs, os.path.join(ROOT, 'html'))
    print('HTML 样卷 ->', p)
    a = BH.build_answer_html(qs, '数学', TITLE, SUB, META, '热点题型归纳', os.path.join(ROOT, 'html'))
    print('HTML 答案 ->', a)
    try:
        d = MP.build_paper(qs, '数学', TITLE, SUB, META, secs, os.path.join(ROOT, 'out'))
        print('Word 样卷 ->', d)
    except Exception as e:
        print('Word 失败:', e)
    return 0

if __name__ == '__main__':
    sys.exit(main())
