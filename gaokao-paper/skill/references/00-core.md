# 核心流程

## 工作目录

`/data/workspace/gaokao-paper`，所有路径相对它。

| 路径 | 内容 |
|---|---|
| `data/bank.json` | 题库（权威数据） |
| `data/progress.json` | 练习记录，**重建不回来**，删题走 `batch-delete`（它会连带清理） |
| `data/ref_bank.json` | 教辅例题（按题目 ID 引用） |
| `data/kp_notes.json` | 知识点讲解 + 题目引用 |
| `data/batches.json` | 批次登记 |
| `py/hand_input.py` | 人工录入入口（**模式 A 走这里**） |
| `py/main.py` | CLI（提取、组卷、导出） |
| `tools/selftest.py` | 后端回归（211 项） |
| `tools/test.mjs` | 前端回归（37 项） |
| `tools/check_skill_docs.py` | 本 skill 文档自检（103 项） |
| `tools/export_excel.py` | 导出 Excel |

## 为什么默认人工审核

PDF 里的这些字符是**矢量绘制，不是文本**：

```
原卷视觉：  定义在 R 上的奇函数 f(x) 满足 f(2-x)=f(x)，且在 (0,1) 上...
脚本提取：  定义在R 上的奇函数f x 满足f 2 - x = f x ，且在0,1 上...
                              ↑            ↑              ↑
                           括号丢失     括号丢失      区间括号丢失
```

换任何正则、调任何参数都拿不回来——**信息在源里就不以文本形式存在**。

同理还有：

| 原卷 | 脚本提取 | 后果 |
|---|---|---|
| `x²` `x₁` | `x2` `x1` | 上标下标混淆 |
| `\frac{1}{4}` | 上下两行文本 | 分数结构丢失 |
| `\sqrt{3}` | `√ 3` 或 `3` | 根号内容丢失 |

**但语文、英语、生物（部分）公式少，模式 B 可用。**

## 模式选择决策树

```
来源是 PDF？
├── 有无文本层？（pymupdf 提取，看字符数）
│   ├── 无（扫描件）→ 转图片流程，见 12-source-image.md
│   └── 有 →
│        ├── 数学 / 物理 / 化学 → 模式 A（人工审核）
│        ├── 语文 / 英语        → 模式 B（脚本提取 + 逐题核对）
│        └── 想快速看结构       → 模式 C（--no-commit，不入库）
```

判断有无文本层：

```python
import pymupdf
d = pymupdf.open(path)
n = sum(len(d[i].get_text().strip()) for i in range(min(5, d.page_count)))
# n < 200 → 基本无文本层（扫描件）
```

## 三种模式的产物

| 模式 | 落库 | 用途 |
|---|---|---|
| A | 是（经校验） | **正式录入** |
| B | 是（人工核对后） | 公式少的科目批量录入 |
| C | **否** | 只看中间结果，`/tmp` 下核对 |

模式 C 的调用方式（`--no-commit` 让结果只写到 `/tmp`，看完再决定）：

```bash
python3 py/main.py extract --pdf <路径> --subject 数学 --no-commit
```

`extract` 默认会写库；加 `--no-commit` 切到预览模式，
结果输出到 `/tmp` 供人工核对，确认无误后再走模式 A 入库。

## 录入前：确认知识点归属

知识点是三层结构，**索引只发生在题型和题目之间**：

```
大知识点（一级）  ── 纯目录，无 ID，不参与索引
小知识点（二级）  ── 纯目录，无 ID，不参与索引
题型（三级）      ── 实体节点，有 ID，与题目双向多对多
```

录入时填 `kp`（一级）与 `kp2`（二级），题型通过 `topics` 挂。

查目录：

```bash
python3 py/main.py kp-catalog            # 全部六科
python3 py/main.py topic-list --subject 数学
```

六科规模（一级/二级/题型）：数学 12/108/422，物理 16/106，化学 16/86，
生物 18/100，语文 8/53，英语 9/56。目前只有数学有题型节点（422 个）。

**数字可能随代码变动。** 查实时值：

```python
import sys; sys.path.insert(0, 'py')
import kp_catalog as K
for s in K.CATALOG:
    n2 = len(set(n for _, subs in K.CATALOG[s] for n in subs))
    print(s, len(K.CATALOG[s]), n2)
```

## 录入后：必做校验

### 1. 端到端一致性

导出 HTML 与 Word，核对同一个公式在两端是否都在：

```python
import re, docx
h = open('html/试卷_XXX.html', encoding='utf-8').read()
d = docx.Document('out/试卷_XXX.docx')
full = ''.join(p._p.xml for p in d.paragraphs)
for t in d.tables:                      # ← 选项在表格里，必须算进去
    for row in t.rows:
        for c in row.cells:
            full += c._tc.xml
print('mfrac', h.count('<mfrac'), '/ m:f', full.count('<m:f>'))
print('残留 dfrac', h.count('dfrac'), full.count('dfrac'))
print('残留 ℝ', h.count('ℝ'), full.count('ℝ'))
print('源码残留', len(re.findall(r'\\[a-zA-Z]+\{|\$', h)))
```

**只数 `d.paragraphs` 会漏掉选项里的公式**，误判成「Word 端公式丢失」——这个坑踩过。

### 2. 跑回归

```bash
python3 tools/selftest.py        # 期望 211/211
node tools/test.mjs              # 期望 37/37
python3 tools/check_skill_docs.py  # 期望 103/103（改了底层代码时）
```

### 3. 交付

```bash
python3 tools/export_excel.py
```

## 批次管理

每次录入归一个新批次，方便后续整批删除：

```python
import hand_input as H
H.add_many(QS, batch='人工录入-00N')
```

每批用新 ID（如 `人工录入-001`）。复用会把两批混在一起，之后无法分别删除。

删除整批走 CLI（会连带清理练习记录）：

```bash
python3 py/main.py batch-delete --batch-id '<批次ID>'
```

切片图片会保留：图片按题目 ID 命名，可能跨批次复用，留着更安全。


## 从教辅 PDF 批量录入（模式 C 变体）

适用：`2024高中数学热点题型归纳` 这类**题型 + 典例 + 变式**结构的教辅。

### 流程

```bash
# 1. 提取（只取【提分秘籍】【典例分析】【变式演练】）
python3 tools/extract_ref.py <pdf路径>
#    → data/ref_bank.json（题目正文）
#    → data/kp_notes.json（讲解 + 题目ID 引用）

# 2. 人工重建：ref_bank 的 stem 是 PDF 原文，
#    公式被拆成上下行（"kπ + π\n2\n- π\n4"），必须重建为 LaTeX

# 3. 入库时挂 topic，形成「题型 ←→ 题目」双向索引
```

### ref_bank 的数据特点

| 字段 | 说明 |
|---|---|
| `stem` | PDF 原文，**公式上下分行**，需重建 |
| `opts` / `opt_letters` | 选项文本与字母，分开存 |
| `ans` | 答案（覆盖率 100%） |
| `analysis` | 分析 |
| `solution` | 详解（覆盖率 95%） |
| `topic` | 所属题型 ID（如 `M-T-001`） |
| `kind` | `典例` 或 `变式` |

字段名是 `stem`（不是 `stem_text`）——
与正式题库 `bank.json` 的 `stem_text` 不同，取值时注意区分。

### 重建要点

教辅原文的典型碎裂形式：

```
M
=
{ x
x = kπ + π
2
- π
4 ，k ∈Z
```

还原为：

```latex
设集合 $M=\left\{x \mid x=\frac{k\pi}{2}+\frac{\pi}{4}, k\in\mathbb{Z}\right\}$，
$N=\left\{x \mid x=\frac{k\pi}{4}+\frac{\pi}{2}, k\in\mathbb{Z}\right\}$，则
```

判断依据：**结合 solution 反推**。solution 里通常有更完整的表述。

### 分页录入

1395 题不可能一次录完。建议每批 15~25 题，
**按 topic 顺序**（M-T-001 → M-T-002 → …），
每批生成四份文件供审核：HTML 试卷、Word 试卷、Word 答案与解析、Excel。
