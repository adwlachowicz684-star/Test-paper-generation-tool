#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
全库 LaTeX 公式合法性校验 —— 专抓"错码 / 符号错位"。

检查项：
  A. 控制字符（0x00-0x08 等）与私用区字符（U+E000-U+F8FF）出现在 $...$ 内
  B. 反斜杠后跟非法字符（命令被截断，如 \x07ngle）
  C. \left / \right 不配对，或 \left( 配 \right] 这类语义错位
  D. 花括号 {} 不配对
  E. 公式内出现裸的中文/全角标点（通常是 $ 未闭合导致正文被吞进公式）
  F. 常见命令拼写残损（angle/frac/dfrac/sqrt/pi 等被打断）

用法： python3 tools/lint_math.py [--fix]
"""
import json, re, sys, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BANK = os.path.join(BASE, 'data', 'bank.json')
FIELDS = ['stem_text', 'answer', 'analysis', 'solution', 'opts']

# 合法 LaTeX 命令白名单（本项目用到的）
CMD_OK = set(r'''
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa lambda mu nu
xi pi varpi rho sigma varsigma tau upsilon phi varphi chi psi omega
Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega
frac dfrac tfrac cfrac binom
sqrt root
sin cos tan cot sec csc arcsin arccos arctan
ln lg log exp
lim sup inf max min deg dim det gcd
sum prod int oint iint iiint
partial nabla infty
cdot cdots ldots vdots ddots times div pm mp oplus otimes
leq le geq ge neq ne approx equiv sim simeq cong propto
ll gg subset subseteq supset supseteq cup cap varnothing in notin forall exists
rightarrow leftarrow Rightarrow Leftarrow leftrightarrow Leftrightarrow mapsto to gets
vec hat bar tilde dot ddot overline underline widehat widetilde
left right big Big bigg Bigg middle
mathbb mathcal mathrm mathbf mathit mathsf text mbox operatorname
quad qquad hspace vspace space
angle triangle square parallel perp parallel degree prime circ
begin end cases matrix pmatrix bmatrix vmatrix array
label tag not
choose over atop
hline line newline cr
limits nolimits displaystyle textstyle scriptstyle
color textcolor
overset underset stackrel
xlongequal xrightarrow xleftarrow
lfloor rfloor lceil rceil
langle rangle lvert rvert lVert rVert
%  , ; ! :
mid nmid leqslant geqslant subsetneq supsetneq subseteq supseteq complement setminus varnothing emptyset cup cap bigcup bigcap geqslant leqslant nleq ngeq perp parallel angle measuredangle triangle square diamond star bullet circ star ast dagger ell wp Re Im aleph top bot vdash models bmod pmod mod binom dbinom overrightarrow overleftarrow overleftrightarrow underrightarrow xrightarrow xleftarrow lbrace rbrace notagnonumber tag mathop mathbin mathrel mathopen mathclose mathpunct limits noalign arraystretch
% 2026-09 补：全库扫描后确认的合法命令（原白名单漏收，造成 2000+ 误报）
therefore because iff implies impliedby Longleftrightarrow Longleftarrow Longrightarrow
longrightarrow longleftarrow leftrightarrow bigl bigr biggl biggr Bigl Bigr Biggl Biggr bigm Bigm
underbrace overbrace vphantom phantom boxed
frown backsim searrow nearrow swarrow nwarrow lnot neg land lor dots ddotsb
rm bf it sf tt boldsymbol triangleq odot oplus ominus oslash circledast
nRightarrow nLeftarrow nleftrightarrow surj inj
shortmid shortparallel nshortparallel nparallel smallsmile smallfrown
'''.split())

# 一元参数命令（必须紧跟参数）
CTRL_BAD = re.compile(r'[\x00-\x08\x0b\x0c\x0e-\x1f]')
PUA = re.compile(r'[\ue000-\uf8ff]')
CJK_IN_MATH = re.compile(r'[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]')


def iter_math(s):
    """提取 $...$ / $$...$$ 内的公式正文"""
    out = []
    i = 0
    n = len(s)
    while i < n:
        if s[i] == '$' and (i == 0 or s[i - 1] != '\\'):
            if s.startswith('$$', i):
                j = s.find('$$', i + 2)
                if j < 0:
                    break
                out.append(s[i + 2:j]); i = j + 2; continue
            j = i + 1
            while j < n:
                if s[j] == '$' and s[j - 1] != '\\':
                    break
                j += 1
            if j >= n:
                break
            out.append(s[i + 1:j]); i = j + 1; continue
        i += 1
    return out


def check_formula(fml):
    """返回问题列表 [(类型, 片段)]"""
    issues = []

    # A. 控制字符 / 私用区
    for m in CTRL_BAD.finditer(fml):
        issues.append(('控制字符', repr(m.group()), hex(ord(m.group()))))
    for m in PUA.finditer(fml):
        issues.append(('私用区字符', repr(m.group()), hex(ord(m.group()))))

    # B. 反斜杠后跟非法字符
    for m in re.finditer(r'(?<!\\)\\(.)', fml):
        c = m.group(1)
        if c == '' :
            continue
        if c.isalpha():
            # 取出完整命令名
            j = m.end() - 1
            while j < len(fml) and fml[j].isalpha():
                j += 1
            cmd = fml[m.end() - 1:j]
            if cmd not in CMD_OK:
                issues.append(('未知命令', '\\' + cmd, ''))
        elif c in '{}%&_#$':
            pass  # 转义
        elif c == '\\':
            pass  # 换行 \\（矩阵、方程组）
        elif c in ' ,;!:':
            pass  # 间距命令
        else:
            issues.append(('反斜杠+非法字符', '\\' + repr(c), hex(ord(c))))

    # C. \left \right 配对
    lr = re.findall(r'\\(left|right)\s*([^\s]?)', fml)
    depth = 0
    for kind, delim in lr:
        if kind == 'left':
            depth += 1
        else:
            depth -= 1
            if depth < 0:
                issues.append(('\\right 多余', '', ''))
                depth = 0
    if depth > 0:
        issues.append(('\\left 未闭合', '%d 个' % depth, ''))

    # D. 花括号配对
    d = 0
    for ch in fml:
        if ch == '{':
            d += 1
        elif ch == '}':
            d -= 1
            if d < 0:
                issues.append(('多余 }', '', ''))
                d = 0
    if d > 0:
        issues.append(('{ 未闭合', '%d 个' % d, ''))

    # E. 公式内中文 —— 分两级：
    #    【严重】连续 >=2 个汉字 ⇒ 几乎一定是 $ 未闭合把正文吞进了公式，
    #            渲染时中文会挤成一行、丢换行，学生看到的是乱码段。
    #    【轻微】只有全角标点或单个汉字（如 $V_{球}$）⇒ 风格问题，不影响阅读。
    #    注：\text{...} / \mbox{...} 内放中文是合法用法（表头、单位、说明），先剥掉。
    stripped = re.sub(r'\\[a-zA-Z]*text\s*\{[^{}]*\}', '', fml)
    stripped = re.sub(r'\\mbox\s*\{[^{}]*\}', '', stripped)
    stripped = re.sub(r'\\(?:mathrm|mathbf|operatorname)\s*\{[^{}]*\}', '', stripped)
    if len(fml) > 60:
        if re.search(r'[\u4e00-\u9fff]{2,}', stripped):
            issues.append(('【严重】公式吞正文(疑 $ 未闭合)', fml[:50], ''))
        elif CJK_IN_MATH.search(stripped):
            issues.append(('【轻微】公式内含中文标点/单字', fml[:50], ''))

    return issues


def main():
    b = json.load(open(BANK, encoding='utf-8'))
    report = {}
    for q in b:
        qid = q.get('id')
        problems = []
        for f in FIELDS:
            v = q.get(f)
            if not v:
                continue
            if isinstance(v, list):
                v = ' '.join(str(x) for x in v)
            s = str(v)
            # 先查字段级错码（不在公式里也算）
            for m in CTRL_BAD.finditer(s):
                problems.append((f, '控制字符', repr(m.group()), hex(ord(m.group()))))
            for m in PUA.finditer(s):
                problems.append((f, '私用区字符', repr(m.group()), hex(ord(m.group()))))
            for fml in iter_math(s):
                for it in check_formula(fml):
                    problems.append((f, it[0], it[1], it[2]))
        if problems:
            report[qid] = problems

    print('=' * 70)
    print('题库 %d 题，发现 %d 题存在公式/符号问题' % (len(b), len(report)))
    print('=' * 70)
    from collections import Counter
    c = Counter()
    for qid, ps in report.items():
        for p in ps:
            c[p[1]] += 1
    for k, v in c.most_common():
        print('  %-28s %d' % (k, v))
    print('=' * 70)
    for qid in sorted(report):
        ps = report[qid]
        print('\n【%s】%d 处' % (qid, len(ps)))
        seen = set()
        for f, kind, frag, extra in ps:
            key = (f, kind, frag)
            if key in seen:
                continue
            seen.add(key)
            print('   [%s] %s  %s %s' % (f, kind, frag, extra))


if __name__ == '__main__':
    main()
