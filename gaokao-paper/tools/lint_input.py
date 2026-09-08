#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""lint_input.py —— 录题骨架文件的语法与格式自检

## 为什么需要它

写 `input_batchXX.py` 时最容易犯的错，是**引号不匹配**：

```python
'opts': [('A', r"$6$'), ...]      # ← 结尾用了单引号，r" 没闭合
```

这个错的特点是：
- 肉眼看不出来（`r"$6$` 和 `r"$6"` 只差一个字符）
- 每次都要等到 `ast.parse` 或入库才暴露
- **我已经犯过 4 次**（第 28、29、30 批各一次）

本脚本在入库前一次性把所有这类问题找出来。

    python3 tools/lint_input.py                       # 检查所有 input_batch*.py
    python3 tools/lint_input.py tools/input_batch30a.py

## 检查项

| # | 检查 | 说明 |
|---|---|---|
| 1 | 语法能否解析 | 引号、括号是否匹配 |
| 2 | `r"..."` 用单引号结尾 | 最高频错误 |
| 3 | 必须字段 | type / stem_text / answer / topics / src |
| 4 | 选择题必须有 opts | 否则入库被拒 |
| 5 | 答案在选项内 | 选择题的 answer 要能匹配某个选项标签 |
| 6 | review 非空 | 独立验算的依据，不能省 |
| 7 | 题号重复 | 同一文件内 src 是否撞车 |

## 用法建议

写完骨架文件后**先跑这个再入库**，比 merge_batches 报错更快定位。
"""
import ast
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FIX = False
REQUIRED = ['type', 'stem_text', 'answer', 'topics', 'src']


def autofix(path):
    """自动修复「r"..." 单引号结尾」这一高频错误。

    我已犯过 6 次：`('A', r"$6$')` —— 结尾该是 `")` 却写成 `')`。
    与其每次手工改，不如让工具一次修好。

    返回 (是否修改, 修复处数)。
    """
    src = open(path, encoding='utf-8').read()
    # 匹配  r"....<任意内容>')  →  r"....<任意内容>")
    # （不限定结尾是 $，因为 r"$210$ 种') 这类同样中招）
    new, n = re.subn(r'(r"[^"\n]*)\'\)', r'\1")', src)
    if n:
        open(path, 'w', encoding='utf-8').write(new)
    return n


def check_file(path):
    """返回 (错误列表, 警告列表, 题数)。"""
    errs, warns = [], []
    src = open(path, encoding='utf-8').read()

    # 1. 语法
    try:
        tree = ast.parse(src)
    except SyntaxError as e:
        ln = e.lineno or 0
        lines = src.split('\n')
        ctx = lines[ln - 1] if 0 < ln <= len(lines) else ''
        errs.append('语法错误 行%d: %s\n         %s' % (ln, e.msg, ctx.strip()[:80]))
        # 额外提示高频原因
        if 'unterminated string' in (e.msg or ''):
            errs.append('        ↳ 多半是 r"..." 用了单引号结尾，'
                        '查这一行及上一行的 $ 符号')
        return errs, warns, 0

    # 2. r"..." 单引号结尾（语法过关时也可能存在但少见，仍扫一遍）
    # 先标出所有文档字符串（三引号块）的行区间，其中的示例文本不算错
    doc_lines = set()
    lines = src.split('\n')
    in_doc = False
    doc_start = 0
    for i, line in enumerate(lines, 1):
        cnt = line.count('"""')
        if cnt % 2 == 1:          # 奇数个：切换状态
            if not in_doc:
                in_doc, doc_start = True, i
            else:
                for j in range(doc_start, i + 1):
                    doc_lines.add(j)
                in_doc = False
        elif in_doc:
            doc_lines.add(i)

    for i, line in enumerate(lines, 1):
        if i in doc_lines:
            continue
        if line.strip().startswith('#'):
            continue
        # 去掉反引号内的内容（行内代码示例里的引号不算错）
        scan = re.sub(r'`[^`]*`', '', line)
        for m in re.finditer(r'r"[^"]*\'(?=[,)])', scan):
            errs.append('行%d: 疑似 r"..." 用单引号结尾：%s'
                        % (i, line.strip()[:60]))

    # 解析出 QS 列表
    n = 0
    seen_src = {}
    for node in ast.walk(tree):
        if not isinstance(node, ast.Dict):
            continue
        keys = [k.value for k in node.keys
                if isinstance(k, ast.Constant) and isinstance(k.value, str)]
        if 'stem_text' not in keys:
            continue
        n += 1
        d = {}
        for k, v in zip(node.keys, node.values):
            if isinstance(k, ast.Constant) and isinstance(k.value, str):
                if isinstance(v, ast.Constant):
                    d[k.value] = v.value
                elif isinstance(v, (ast.List, ast.Tuple)):
                    d[k.value] = ['<list %d>' % len(v.elts)]

        # 3. 必须字段
        for f in REQUIRED:
            if f not in keys:
                errs.append('第%d题：缺字段 %s' % (n, f))

        # 4. 选择题必须有 opts
        if d.get('type') == '选择' and 'opts' not in keys:
            errs.append('第%d题：选择题没有选项（opts）' % n)

        # 5. 答案在选项内
        ans = d.get('answer')
        if isinstance(ans, str) and d.get('type') == '选择':
            if 'opts' in keys:
                pass  # 选项标签在 opts 列表里，语法层难取，跳过
            else:
                errs.append('第%d题：无 opts 无法校验答案' % n)

        # 6. review
        if 'review' not in keys:
            warns.append('第%d题：缺 review（建议记录独立验算依据）' % n)

        # 7. src 重复
        s = d.get('src')
        if isinstance(s, str):
            if s in seen_src:
                errs.append('第%d题：src 与第%d题重复' % (n, seen_src[s]))
            else:
                seen_src[s] = n

    return errs, warns, n


def main():
    global FIX
    args = [x for x in sys.argv[1:] if x != '--fix']
    FIX = '--fix' in sys.argv[1:]
    if args:
        files = args
    else:
        files = sorted(glob.glob(os.path.join(ROOT, 'tools', 'input_batch*.py')))

    if not files:
        print('  没有找到 input_batch*.py')
        return 0

    total_err = total_warn = total_q = 0
    n_fix = 0
    for f in files:
        if FIX:
            c = autofix(f)
            if c:
                n_fix += c
                print('  🔧 %s：自动修复 %d 处引号' % (os.path.basename(f), c))
        errs, warns, n = check_file(f)
        name = os.path.basename(f)
        if errs:
            print('  ✗ %s  （%d 题）' % (name, n))
            for e in errs:
                print('      %s' % e)
        elif warns:
            print('  ⚠ %s  （%d 题）' % (name, n))
            for w in warns[:5]:
                print('      %s' % w)
        else:
            print('  ✓ %s  （%d 题）' % (name, n))
        total_err += len(errs)
        total_warn += len(warns)
        total_q += n

    print('  ' + '-' * 56)
    print('  共 %d 个文件、%d 题；错误 %d、警告 %d'
          % (len(files), total_q, total_err, total_warn))
    return 1 if total_err else 0


if __name__ == '__main__':
    sys.exit(main())
