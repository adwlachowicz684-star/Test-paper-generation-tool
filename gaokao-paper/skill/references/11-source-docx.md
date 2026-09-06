# 来源：Word / .docx

## 关键前提：Word 格式 ≠ 一定有源信息

先跑这段检测，根据结果决定走哪条路：

```python
import docx, re
d = docx.Document(path)
xml = ''.join(p._p.xml for p in d.paragraphs)
for t in d.tables:
    for row in t.rows:
        for c in row.cells:
            xml += c._tc.xml
print('vertAlign(上下标)', xml.count('vertAlign'))
print('oMath(公式)', xml.count('<m:oMath'))
```

| 检测结果 | 文件来源 | 可靠性 |
|---|---|---|
| `vertAlign` / `oMath` 多 | 老师手写的 Word、LaTeX 转换 | **极高，优于 PDF** |
| 都接近 0 | **PDF 转换的 Word** | 源信息已丢失，**不如 PDF** |

实测：PDF 转出的 docx 里 `vertAlign=0`、`oMath=0`，上标 `10⁻⁸` 已经没了。
而同一个内容从原始 PDF 提取反而能还原出 `10^{-8}`。

**所以：拿到 docx 先检测，源信息缺失就退回 PDF 流程或直接人工读。**

## 读取源信息

### 上下标（`w:vertAlign`，布尔判定，最可靠）

```python
import docx
d = docx.Document(path)
for p in d.paragraphs:
    for r in p.runs:
        if r.font.superscript:   # 底层是 <w:vertAlign w:val="superscript"/>
            ...
        if r.font.subscript:
            ...
```

`font.superscript` 是 python-docx 的封装，底层写 `w:vertAlign`。
它是**明确的三态**（True / False / None），比 PDF 的几何推断可靠得多。

也可以直接读 XML：

```python
re.findall(r'<w:vertAlign w:val="(\w+)"/>', xml)   # superscript / subscript
```

### 公式（OMML，`m:oMath`）

```python
re.findall(r'<m:t[^>]*>([^<]*)</m:t>', xml)   # 公式里的文本
```

**注意**：`paragraph.text` 读不到 `<m:t>`，会误判"公式丢失"。
必须直接读 XML。这个坑踩过一次——以为公式没了，其实是读法不对。

### 段落与表格

题目可能在表格里（选项常排成表格）。**遍历时必须把表格算进去**：

```python
for p in d.paragraphs:
    ...
for t in d.tables:
    for row in t.rows:
        for c in row.cells:
            for p in c.paragraphs:
                ...
```

## 模式 A（推荐）

docx 只是阅读对象。用 python-docx 把段落文本 dump 出来，
配合源信息（上下标）理解语义，再按 `20-latex.md` 重建。

```python
import docx
d = docx.Document(path)
for i, p in enumerate(d.paragraphs):
    if not p.text.strip():
        continue
    print(i, p.text[:100])
```

## 模式 B

目前 `py/main.py extract` **只接受 PDF**。docx 需要先转 PDF，或直接人工读。

**原生 Word 直接读 `run.font.superscript` 和 OMML**，比转 PDF 再提取更准——
转换过程会丢掉上下标属性。

## 写入侧：Word 导出

`py/make_paper.py` 生成的 Word 公式是原生 OMML，双击可编辑。
若发现 Word 端公式异常，见 `30-pitfalls.md`。

导出后核对：

```python
import docx
d = docx.Document(out_path)
xml = ''.join(p._p.xml for p in d.paragraphs)
for t in d.tables:                    # 选项在表格里
    for row in t.rows:
        for c in row.cells:
            xml += c._tc.xml
print('m:f', xml.count('<m:f>'), 'sSub', xml.count('<m:sSub>'),
      'sSup', xml.count('<m:sSup>'))
```
