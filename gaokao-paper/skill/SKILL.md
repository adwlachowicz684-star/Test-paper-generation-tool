# gaokao-import

把高考 / 模考题目从各种来源（PDF、Word、图片、网页、文本）识别并录入 `gaokao-paper` 题库。

**工作目录固定为 `/data/workspace/gaokao-paper`**，所有相对路径都相对它。

## 最快路径：两条命令跑完一批

日常录题走这两条就够，中间步骤由脚本串起来，只在出问题时才展开细节。

```bash
cd /data/workspace/gaokao-paper

# 1. 生成骨架（第18批：M-T-073 出4题、M-T-074 出3题）
python3 tools/new_batch.py 18 -t M-T-073:4 -t M-T-074:3
#   → 生成 tools/input_batch18.py（题目骨架）+ tools/commit_batch18.py（入库脚本）

# 2. 填 input_batch18.py 的内容（题干/选项/答案/详解/review），然后一键跑到底
python3 tools/run_batch.py 18
```

`run_batch` 依次做完：入库 → 导出 HTML/Word/答案卷 → 逐题两端核对 → 后端/前端/文档三项回归 → 刷新计划清单。
全部通过时输出约 12 行；任一步失败立即停下并打印该步报错。

常用变体：

```bash
python3 tools/run_batch.py 18 --no-commit   # 已入库过，只重跑导出/核对/回归
python3 tools/run_batch.py 18 --title '导数含参讨论'
python3 tools/run_batch.py 18 --skip-docs   # 没改底层代码时跳过文档自检
```

## 三种录入模式

先定模式，再动手。这是本 skill 最关键的决策，选错会直接影响题目正确性。

| 模式 | 速度 | 何时用 | 入口 |
|---|---|---|---|
| **A 人工审核**（默认） | 慢，3–5 分钟/题 | **绝大多数情况**，尤其数学、物理、化学 | `references/20-latex.md` + `21-review-rules.md` |
| **B 脚本提取 + 逐题核对** | 中 | 语文、英语等公式少的科目；或题目量大需要初筛 | `references/10-source-pdf.md` |
| **C 纯脚本** | 快 | 快速预览结构，结果写到 `/tmp` 供人工核对 | `references/10-source-pdf.md` |

**默认走模式 A。** 原因见 `references/00-core.md`「为什么默认人工审核」——
PDF 里的函数括号、区间括号是矢量绘制而非文本，脚本无论如何调参都提取不出来。

模式 C 的用法：`extract` 命令加 `--no-commit`，结果只输出到 `/tmp`，
看完再决定要不要走模式 A 重新核对入库。

## 能力路由表

**只加载与当前任务匹配的文档**，一次只读用得上的那一两篇。

| 你要做的事 | 读这个 |
|---|---|
| 首次使用 / 不确定走哪条路 | `references/00-core.md` |
| 来源是 **PDF** | `references/10-source-pdf.md` |
| **教辅 PDF：还原数学符号、核实存疑题、切图题** | `references/14-pdf-glyphs.md` |
| 来源是 **Word / .docx** | `references/11-source-docx.md` |
| 来源是 **图片**（拍照、截图、扫描件） | `references/12-source-image.md` |
| 来源是 **网页文本 / 粘贴文本 / LaTeX** | `references/13-source-web.md` |
| **写题干的 LaTeX**（必读，模式 A 强依赖） | `references/20-latex.md` |
| **人工审核规则**（修什么、怎么判、改答案怎么留痕） | `references/21-review-rules.md` |
| 渲染出问题（公式变源码、选项消失、分数丢失） | `references/30-pitfalls.md` |
| 调用 CLI / hand_input 接口 | `references/40-api.md` |
| 打题型标签、知识点归属 | `references/50-topics.md` |
| 查「哪些题改过原书答案」 | `原书勘误表.md`（`python3 tools/gen_errata.py` 生成） |
| 改了底层代码，怀疑文档过期 | 跑 `python3 tools/check_skill_docs.py` |

## 操作规范

每条都是要**执行**的动作，按顺序做完即达标。

### 1. 入库走 `hand_input`，落库前自动校验

`hand_input.add()` / `add_many()` 内置校验（题型、选项、答案、知识点）。
数据改动一律走这两个函数，它们会顺带做备份和去重。

### 2. 输出写新文件

生成物用新文件名（如 `试卷_第1批_集合与逻辑.docx`）。
原文件保持不动，方便对照和回滚。

### 3. 题库可重建，练习记录不可重建

`data/bank.json` 写入前会自动备份到 `bank.json.bak`，随时可恢复。

`data/progress.json` 是孩子一个学期的错题历史，**重建不回来**。
删题只走 `batch-delete`，它会连带清理对应的练习记录，保持两份数据一致。

### 4. 图片来源：OCR 拿骨架，公式靠重建

实测 tesseract 对数学公式基本无能（`(-∞,-1)` 识别成 `(—00,-1)`）。
图片走「OCR 拿中文骨架 + 人工重建公式」，见 `12-source-image.md`。

### 5. `review` 字段写清楚改了什么、为什么

人工录入的全部价值在这里。原卷笔误、公式重建依据、存疑点都记下来。

### 6. 原卷自相矛盾时，以【详解】推导为准

修正题干，并把判定依据写进 `review`。这样后面复核的人能看到推理链。

### 7. 每次入库后跑回归

```bash
python3 tools/selftest.py     # 后端
node tools/test.mjs           # 前端
```

确保新数据没破坏既有能力。

### 8. 改动底层代码后跑文档自检

```bash
python3 tools/check_skill_docs.py
```

它校验本 skill 文档里的命令、函数、数字是否还有效。
文档最容易腐化——代码改了数字变了，文档还停在旧版本。

### 9. 每批录完导出四份文件供审核

样卷 HTML、样卷 Word、答案与解析 Word、题库 Excel。
逐题目视核对，交付给用户看。

## 标准流程（模式 A）

第 6–9 步由 `run_batch.py` 一键完成，手工只需做前五步。

```
1. 生成骨架     tools/new_batch.py 18 -t M-T-073:4      ← 30 秒
2. 定位原文     教辅 PDF 走 tools/dump_pdf.py --find（符号已还原）
                其他来源直接读原文，含【答案】【详解】
3. 重建题干     按 references/20-latex.md 写成规范 LaTeX，填进骨架
4. 交叉验证     用【详解】反推题干是否自洽，发现矛盾按规范 6 处理
5. 存疑核实     按 14-pdf-glyphs.md 第二节逐条核实，核实完再决定录不录
   图题切图     tools/cut_figs.py --list / --check / --cut（仅图题）
─────────────── 以下由 run_batch 自动完成 ───────────────
6. 入库         hand_input.add_many（整批校验，任一题有问题整批拒绝）
7. 导出样卷     export-html / export-docx / export-answer
8. 逐题核对     check_render.py --quiet（只报缺失的题）
9. 跑回归       selftest.py + test.mjs + check_skill_docs.py
10. 刷新清单    make_plan.py（待录题数才会更新）
```

```bash
python3 tools/run_batch.py 18
```

批量录入时，**每批 15–25 题就导出一次样卷核对**。
错误会批量复制，早发现返工量小。

### 图题不用预估 ID

切图时用临时名，入库后脚本按实际 ID 自动改名：

```bash
# 1~2. 列图位、校验边界
python3 tools/cut_figs.py "$PDF" --list 45
python3 tools/cut_figs.py "$PDF" --check 45 --boxes 334,493,440,603 459,495,555,603
# 3. 用 _tmp 开头的 qid 切图
python3 tools/cut_figs.py "$PDF" --cut 45 --qid _tmp_T071E1 --boxes 334,493,440,603
# 4. input 里 figs 的 file 填 '_tmp_T071E1_fig1.png'
# 5. run_batch 入库后自动改名为 {实际ID}_fig1.png，并同步 bank
```

ID 算错也不会留下对不上的图名。

### 教辅 PDF 的两个提速点

教辅（如《2024高中数学热点题型归纳完整解析版》）的公式符号是私用区字符，
常规提取会丢失、导致题干自相矛盾。用配套工具省掉这部分排查时间：

```bash
PDF=/data/inputs/2024高中数学热点题型归纳完整解析版.pdf

python3 tools/dump_pdf.py "$PDF" --find '题干特征词' --context 1200   # 符号已还原的原文
python3 tools/dump_pdf.py "$PDF" --pages 44 --chars --x0 320 --x1 580 # 精确定括号/撇号
python3 tools/cut_figs.py "$PDF" --list 45                            # 图题：列图位
```

图题以前只能跳过，现在切图→入库→三端渲染已跑通，按 `14-pdf-glyphs.md` 走即可。

## 交付给用户什么

一批录完后，交付：

- 样卷 HTML（自包含单文件，双击可看，Ctrl+P 打印）
- 样卷 Word（公式原生可编辑）
- 答案与解析 Word
- 更新后的题库 Excel（`python3 tools/export_excel.py`）

回复里说明：**录了几题、发现并修正了哪些原卷问题、哪些地方存疑需要复核**。
用户据此判断要不要继续下一批。
