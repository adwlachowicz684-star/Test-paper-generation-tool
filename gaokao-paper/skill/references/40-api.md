# 接口参考

## hand_input（模式 A 入口）

```python
import sys; sys.path.insert(0, 'py')
import hand_input as H
```

### add / add_many

```python
ok, res = H.add_many([q1, q2, ...], batch='人工录入-00N')
# 成功：ok=True, res=['M-H0007', 'M-H0008', ...]
# 失败：ok=False, res=['第 2 题: 选择题没有选项', ...]
```

**整批校验，任一题有问题就整批拒绝。**
半截入库的数据比不入库更麻烦——不知道哪些进了哪些没进。

```python
ok, res = H.add(q)      # 单题
```

### 题目字段

必填：

| 字段 | 说明 |
|---|---|
| `type` | `选择` / `填空` / `解答` 三选一 |
| `stem_text` | 题干，LaTeX 用 `$...$` 包裹 |
| `kp` | 一级知识点 |

按题型必填：

| 题型 | 额外必填 |
|---|---|
| 选择 | `opts`（≥2 项）、`answer` |
| 填空 | `answer` |
| 解答 | `solution` |

建议填：

| 字段 | 说明 |
|---|---|
| `kp2` | 二级知识点 |
| `topics` | 题型标签 ID 列表 |
| `difficulty` | 难度系数（得分率，0–1，默认 0.65） |
| `src` | 来源，如「2024高中数学热点题型归纳 变式16」 |
| `review` | **人工审核备注，必须写** |
| `analysis` | 分析（短） |
| `solution` | 详解（长） |

自动补全（不用填）：`id` `subject` `num` `score` `figs` `subtype`
`kp_list` `smark` `stem` `ana_text` `batch`

### ID 规则

`M-H0001` = 科目前缀 + `-H` + 序号。

| 科目 | 前缀 |
|---|---|
| 数学 | `M` |
| 物理 | `P` |
| 化学 | `C` |
| 生物 | `B` |
| 语文 | `Y` |
| 英语 | `E` |

带科目前缀是为了与真题 ID（`M-2021-001`）同命名空间——
切图、统计、导出都按前缀分科目。中间加 `H` 区分人工与自动。

### validate

```python
ok, errs = H.validate(q, bank)     # bank 可为 []
```

入库前自查用。`add*` 内部已调用。

拦截范围（10 类）：缺题干、type 非法、选择题无选项、
选项内容为空、答案超范围、字母重复、花括号未闭合、
`$` 未成对、填空/解答无答案、缺知识点。

**LaTeX 配对检查**：花括号与 `$` 必须配对。
`\frac{1}{2` 这种手误在渲染时会静默吞掉后面所有内容，极难排查，
所以入库时就拦住。

## CLI

```bash
python3 py/main.py <command> [options]
```

常用：

| 命令 | 用途 |
|---|---|
| `health` | 查题库状态 |
| `list --subject 数学 --limit 10000` | 列题 |
| `extract --pdf <路径> --subject 数学 [--no-commit]` | 脚本提取 |
| `export-html --ids '["M-H0001"]' --outdir html --title X` | 导出 HTML |
| `export-docx` / `export-answer` | 导出 Word |
| `compose --config '{...}'` | 组卷 |
| `topic-list --subject 数学` | 题型列表 |
| `topic-link --payload '{...}'` | 挂题型标签 |
| `batch-list` / `batch-tag` / `batch-delete` | 批次管理 |
| `kp-catalog` | 六科知识点目录 |

完整列表：`python3 py/main.py --help`

### 导出示例

```bash
python3 py/main.py export-html \
  --ids '["M-H0001","M-H0002","M-H0003"]' \
  --outdir html --title '函数与导数专项'
```

`--ids` 是 JSON 数组字符串，注意 shell 引号。

**三个导出命令必须一起用**，且传同一份 `--ids`：
`export-html` / `export-docx` / `export-answer`。
它们内部共用 `order_and_number()`，所以题号与顺序天然一致；
分开导出不同 ids 会导致答案对不上题。

## 导出 Excel

```bash
python3 tools/export_excel.py
```

输出 `高三题库与间隔复习系统.xlsx`，22 列含审核备注列。
可在 Excel 里直接校订，改完：

```bash
python3 py/sync_excel.py        # Excel → bank.json
```

方向别搞反：

```
export_excel : bank.json → Excel   （给人看/改）
sync_excel   : Excel     → bank.json（把改动同步回库）
```

## 回归

```bash
python3 tools/selftest.py          # 后端 211 项
node tools/test.mjs                # 前端 37 项
python3 tools/check_skill_docs.py  # skill 文档 103 项
```

后端第 27 组是人工录入专项。
测试用临时目录 + fixture（`GAOKAO_DATA_DIR` 环境变量），**不碰真实数据**。

## 数据目录环境变量

```python
import os
os.environ['GAOKAO_DATA_DIR'] = '/tmp/xxx'   # 测试用
```

不设则用 `<项目根>/data`。写自测脚本时用这个隔离。


## 录入数据文件的书写规范（input_batchN.py）

这三条规定都是**真踩过**的，每一条都让脚本报出莫名其妙的错。

### 1. LaTeX 字符串一律 raw **双**引号 `r"..."`

单引号会被导数撇号提前终止：

```python
# ✗ 错：$f'(1)$ 里的 ' 提前结束了字符串，报错位置还指向下一行
review='此时 $f'(1)=1$，...'
# ✓ 对
review=r"此时 $f'(1)=1$，..."
```

### 2. 中文行文里用中文弯引号“”，不要 ASCII 双引号

```python
# ✗ 错：ASCII 双引号终止了 r"..." 字符串
r"的"距离为 1"的等高线相切。"
# ✓ 对
r"的“距离为 1”的等高线相切。"
```

### 3. 选项元组的结尾引号要和开头配对

```python
# ✗ 错：r" 开头，' 结尾
opts=[('A', r"$1$'), ('B', r"$2$")]
#            ^^^^ 应为 $1$")
# ✓ 对
opts=[('A', r"$1$"), ('B', r"$2$")]
```

**自检办法**：写完先跑一次 `python3 -c "import ast; ast.parse(open('tools/input_batchN.py').read())"`。
语法通过了再入库。上面三条错误都会表现为 SyntaxError，且**报错行号常常不是真正出错的那行**
（字符串提前终止会让后续内容全被当代码解析），所以逐行读不如直接让解析器告诉你。

### 4. 多行 raw 字符串拼接时，逗号只在最后一行

```python
# ✗ 错：中间行有逗号，变成两个表达式
solution=r"第一行内容",
         r"第二行内容",
# ✓ 对
solution=r"第一行内容"
         r"第二行内容",
```

### 5. 长解析用 solution_ext / solution_ext2 分段

一个 raw 字符串写太长容易出错，可以拆成 `solution` + `solution_ext` +
`solution_ext2`，入库脚本会自动拼成完整解析。
