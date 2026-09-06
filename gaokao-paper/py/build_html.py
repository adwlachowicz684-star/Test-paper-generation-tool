# -*- coding: utf-8 -*-
"""生成 HTML 试卷（打印即 PDF，公式用浏览器原生 MathML）

相比 Word 方案的优势：
  1. 公式走 MathML —— 标准、可读、零依赖，不用手写 OMML XML
  2. 分页用 CSS 控制（break-inside / @page），比逐档试错留白可靠
  3. 改样式即改 CSS，浏览器里实时看，不用转 PDF 再验证
  4. 打印时自动矢量输出，清晰度不降

用法：
    python3 build_html.py            # 生成全部试卷
"""
import sys, os, json, re, base64, html

# 路径必须基于 __file__ 推导，不能硬编码。
# 硬编码 /data/workspace 在 Windows 上会导致 import 直接失败。
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract3 import split_rich, merge_script
from mathml import to_mathml, latex_inline
import paper_template as T
import make_paper as MP

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLICE = os.path.join(ROOT, 'src', 'slices')   # 与 py/main.py 同源，且位于 frontendDist 内
OUT = os.path.join(ROOT, 'out')
EMBED_IMG = True          # True=base64 内嵌（单文件）；False=相对路径引用

# 插图显示尺寸上限（cm）。A4 正文宽约 17cm，
# 单张图最多占约 10cm，给题干和选项留空间。
CFG_FIG_MAX_CM = 10.0
CFG_FIG_MAX_H_CM = 8.0

# ============ 样式 ============
CSS = """
:root{
  --body-w: 162mm;
  --cn: "Songti SC","SimSun","Source Han Serif SC",serif;
  --en: "Times New Roman",Times,serif;
  --math: "Cambria Math","Latin Modern Math","STIX Two Math",serif;
}
*{box-sizing:border-box}
html{-webkit-print-color-adjust:exact;print-color-adjust:exact}
@page{
  size: A4;
  margin: %(mt)dmm %(mr)dmm %(mb)dmm %(ml)dmm;
}
body{
  font-family:var(--cn);
  font-size:10.5pt;
  line-height:1.45;
  margin:0 auto;
  max-width:var(--body-w);
  color:#000;
}
/* ---------- 卷头 ---------- */
.title{
  font-family:var(--cn); font-weight:700; font-size:16pt;
  text-align:center; margin:0 0 2pt;
}
.subtitle{ text-align:center; font-size:11pt; color:#444; margin:0 0 4pt; }
.rule{ border:0; border-top:2px solid #2E75B6; margin:0 0 5pt; }
.meta{
  width:100%%; border-collapse:collapse; margin:0 0 8pt; font-size:9.5pt;
}
.meta th{ font-weight:700; text-align:center; width:30mm; }
.meta td, .meta th{ border:1px solid #9ab; padding:2px 6px; }
/* ---------- 分节 ---------- */
.section{
  font-weight:700; font-size:11pt; color:#1F3864;
  margin:9pt 0 3pt;
}
/* ---------- 题目：矩形模块 ---------- */
/* 两列：第1列题号，第2列放**一个**容器 .qmain，
   题干/选项/插图/留白在 .qmain 内部流式排布。
   不用 grid-row:1/-1 —— 隐式网格下它不能跨所有行，内容会流回第1列。 */
.q{
  display:grid;
  grid-template-columns:2.4em 1fr;
  column-gap:4pt;
  margin:6pt 0 3pt;
  break-inside:avoid;          /* 题目不被分页切断 */
  page-break-inside:avoid;
}
.qnum{
  text-align:right;
  font-weight:700;
  color:#1F3864;               /* 与答案卷同色 */
  white-space:nowrap;
}
.qmain{ min-width:0; }         /* 允许内容收缩，防止撑破列宽 */
/* 选项与插图并排 */
.qbody{ display:flex; gap:6pt; align-items:flex-start; }
.qbody > .opts{ flex:1 1 auto; min-width:0; }
.qbody > .figs{ flex:0 0 auto; }
/* ---------- 选项：固定列宽 → 跨题对齐 ---------- */
.opts{
  display:grid;
  grid-template-columns:repeat(var(--cols,2),1fr);
  column-gap:8pt;
  margin:1pt 0 0;
}
.opt{ margin:0; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
  /* 含公式的选项不裁切。
     overflow:hidden 会把超宽的 MathML 整体切掉 ——
     页面上只剩「A．B．C．D．」看不到内容。
     纯文本长选项仍用省略号，避免撑破版面。 */
  .opts-noclip .opt { overflow:visible; text-overflow:clip; }
.opt b{ font-weight:700; margin-right:2pt; }
/* ---------- 插图 ---------- */
.figs{ text-align:right; }
.figs.alone{ text-align:right; margin:2pt 0; }
.figrow{ display:flex; flex-wrap:wrap; gap:4pt; justify-content:flex-end; }
figure{ margin:0; text-align:center; }
/* 必须显式限宽限高：只写 max-width:100%% 时大图会
   按原始像素撑开，710px 宽的图几乎占满 A4 一行。*/
figure img{ max-width:100%%; height:auto; display:block; margin:0 auto;
  max-height:%(figmaxh).1fcm; }
figcaption{
  font-size:8pt; color:#888; text-align:center; margin:1pt 0 2pt;
}
/* ---------- 答题留白 ---------- */
.blank{
  border-bottom:1px solid #e8e8e8;
  margin-top:2pt;
}
/* ---------- 填空下划线 ---------- */
/* 用 border-bottom 而非 text-decoration：
   text-decoration 画在空白字符上时，部分浏览器（尤其打印预览）
   会跳过纯空白区域，导致下划线看不见。
   inline-block + 固定宽度 + 下边框是任何环境都稳定的画法。*/
u.blank-u{
  display:inline-block;
  min-width:%(blankw).1fem;
  border-bottom:1px solid #000;
  text-decoration:none;
  vertical-align:baseline;
  margin:0 .15em;
}
/* ---------- 答案卷 ---------- */
.ans{ margin:7pt 0 0; break-inside:avoid; }
.ans .a{ color:#c00; font-weight:700; }
.ans .src{ color:#808080; font-size:9pt; margin-left:8mm; }
.ans .ana{ color:#353; font-size:9.5pt; margin-left:8mm; }
/* ---------- 数学字体 ---------- */
/* 显式声明 font-style，**不依赖浏览器默认**。
   MathML 规范里 <mn>/<mo> 该是正体、<mi> 变量该是斜体，
   但各浏览器实现不一致（有的把区间 (0,1) 整体渲染成斜体）。
   这里按数学排版规范写死：
     变量 mi          → 斜体
     数字 mn、运算符 mo → 正体
     函数名（mathvariant=normal）→ 正体（sin/log/max 等不该斜） */
math{ font-family:var(--math); font-size:1.02em; }
math mi{ font-style:italic; }
math mn, math mo, math mtext{ font-style:normal; }
math mi[mathvariant="normal"]{ font-style:normal; }
/* 区间、括号等定界符保持正体（部分浏览器对 <mo> 的默认不可靠） */
math mo{ font-family:var(--math); }
/* ---------- 屏幕提示（打印时隐藏） ---------- */
.tip{
  background:#fffbe6; border:1px solid #ffe58f; padding:6pt 8pt;
  font-size:9pt; margin:0 0 8pt; border-radius:3px;
}
@media print{
  .tip{ display:none; }
  /* 打印时页边距交给 @page，.paper 不能再有 padding，
     否则多页文档的第 2 页起会叠加一次（padding 只在整个元素首尾）。 */
  body{ max-width:none; }
  .paper{ width:auto; min-height:0; padding:0; box-shadow:none; }
}
@media screen{
  /* 屏幕上把 .paper 显示成一张 A4 纸：
     宽 210mm，并用与 @page 相同的页边距做 padding。
     这样屏幕预览的内容宽度 = 210 - 2*%(ml)d = 正文宽，
     与打印输出完全一致（原来 padding 用的是 16/14mm，与页边距不符）。 */
  body{ background:#f5f5f5; padding:12px; max-width:none; }
  .paper{
    width:210mm;
    min-height:297mm;
    padding:%(mt)dmm %(mr)dmm %(mb)dmm %(ml)dmm;
    margin:0 auto;
    background:#fff;
    box-shadow:0 1px 6px rgba(0,0,0,.18);
  }
}
"""


def esc(s):
    return html.escape(s or '')


def _fig_css_size(fg, max_cm):
    """按图片真实像素 + dpi 算出显示尺寸（cm）。

    与 Word 端 _fig_size() 同一套规则：cm = 像素宽 / dpi * 2.54，
    超出上限时等比缩放。

    不写死宽度的话，浏览器按**原始像素**排版：
    710px 宽的图在 A4（正文约 794px@96dpi）上几乎占满一行，
    高 708px 的图直接吃掉半张纸。
    """
    w_px = fg.get('w') or 0
    h_px = fg.get('h') or 0
    if not w_px or not h_px:
        return None
    dpi = T.FIGURE.get('dpi', 300)
    w = w_px / dpi * 2.54
    h = h_px / dpi * 2.54
    if w > max_cm:
        h = h * max_cm / w
        w = max_cm
    max_h = CFG_FIG_MAX_H_CM
    if h > max_h:
        w = w * max_h / h
        h = max_h
    return w, h


def _img_tag(sub, fg, max_cm=None):
    fp = os.path.join(SLICE, sub, fg['file'])
    if not os.path.exists(fp):
        return ''
    if EMBED_IMG:
        ext = fg['file'].rsplit('.', 1)[-1].lower()
        mime = 'image/jpeg' if ext in ('jpg', 'jpeg') else 'image/png'
        with open(fp, 'rb') as f:
            b64 = base64.b64encode(f.read()).decode()
        src = f'data:{mime};base64,{b64}'
    else:
        src = f'{SLICE}/{sub}/{fg["file"]}'
    sz = _fig_css_size(fg, max_cm or CFG_FIG_MAX_CM)
    if sz:
        return (f'<img src="{src}" alt="" '
                f'style="width:{sz[0]:.2f}cm;height:{sz[1]:.2f}cm">')
    return f'<img src="{src}" alt="">' 
    fp = os.path.join(SLICE, sub, fg['file'])
    if not os.path.exists(fp):
        return ''
    if EMBED_IMG:
        ext = fg['file'].rsplit('.', 1)[-1].lower()
        mime = 'image/jpeg' if ext in ('jpg', 'jpeg') else 'image/png'
        with open(fp, 'rb') as f:
            b64 = base64.b64encode(f.read()).decode()
        src = f'data:{mime};base64,{b64}'
    else:
        src = f'{SLICE}/{sub}/{fg["file"]}'
    return f'<img src="{src}" alt="">'


def _figs_html(q, sub, layout, ncol=4):
    figs = q.get('figs') or []
    if not figs:
        return ''
    # 必须用**该题自己的科目**去拼路径。
    # 之前用整卷的 sub（取的是第一题的科目），跨科目组卷时
    # 非首题科目的图片会去错目录找 → 全部静默丢失。
    qsub = q.get('subject') or sub
    cap = T.FIGURE['caption']
    items = []
    for i, fg in enumerate(figs, 1):
        # 多图时单张要窄一些，避免一排挤爆版心
        n_fig = len(figs)
        max_cm = (CFG_FIG_MAX_CM if n_fig == 1
                   else CFG_FIG_MAX_CM / min(n_fig, 4) * 1.7)
        tag = _img_tag(qsub, fg, max_cm)
        if not tag:
            # 兜底：再用整卷科目试一次（历史数据里 subject 可能缺失）
            tag = _img_tag(sub, fg, max_cm)
        if not tag:
            continue
        if len(figs) == 1:
            txt = cap['text'].format(n=1, q=q['num'])
        else:
            txt = cap['text_multi'].format(n=i, q=q['num'])
        c = f'<figcaption>{esc(txt)}</figcaption>' if cap['show'] else ''
        items.append(f'<figure>{tag}{c}</figure>')
    if not items:
        return ''
    if layout == 'choice':
        return f'<div class="figs"><div class="figrow">{"".join(items)}</div></div>'
    return f'<div class="figs alone"><div class="figrow">{"".join(items)}</div></div>'


# 公式引擎：mathml（零依赖、离线可用）/ katex（CDN、排版更精美）
MATH_ENGINE = 'mathml'

KATEX_HEAD = """
<link rel="stylesheet"
 href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script defer
 src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script>
document.addEventListener("DOMContentLoaded",function(){
  if(!window.katex){return;}
  document.querySelectorAll(".tex").forEach(function(el){
    try{ katex.render(el.textContent, el, {throwOnError:false}); }
    catch(e){ el.style.color="#c00"; el.title="公式渲染失败"; }
  });
});
</script>
"""


def _rich_html(text):
    """文本 + \\frac / \\sqrt / _{} → HTML

    mathml: 直接输出 <math>（浏览器原生，离线可用）
    katex : 输出 <span class="tex">LaTeX</span>，由 KaTeX 在浏览器端渲染

    必须过 merge_sub()：split_rich 把 a_{n+1} 切成
    文本「a」+ 下标「n+1」两段，不合并的话下标段单独渲染
    会丢掉基底，页面上看到的就是平文本。
    """
    segs = merge_script(split_rich(text))
    has = any(s[0] in ('f', 's', 'm', 'p', 'sp', 'L') for s in segs)
    if not has:
        return esc(text)
    out = []
    for sg in segs:
        if sg[0] == 'L':
            # 人工录入的 $...$ 通用公式。
            # katex 引擎下直接透传源码由浏览器渲染；
            # mathml 引擎下走 latex_inline 转标准 MathML。
            if MATH_ENGINE == 'katex':
                out.append('<span class="tex">%s</span>' % esc(sg[1]))
            else:
                out.append(latex_inline(sg[1]))
        elif sg[0] == 't':
            out.append(esc(sg[1]))
        elif sg[0] == 'f':
            if MATH_ENGINE == 'katex':
                out.append('<span class="tex">\\frac{%s}{%s}</span>'
                           % (esc(sg[1]), esc(sg[2])))
            else:
                out.append(to_mathml([sg]))
        elif sg[0] == 's':
            if MATH_ENGINE == 'katex':
                out.append('<span class="tex">\\sqrt{%s}</span>' % esc(sg[1]))
            else:
                out.append(to_mathml([sg]))
        elif sg[0] == 'm':
            if MATH_ENGINE == 'katex':
                out.append('<span class="tex">%s_{%s}</span>'
                           % (esc(sg[1]), esc(sg[2])))
            else:
                out.append(to_mathml([sg]))
        elif sg[0] == 'p':
            if MATH_ENGINE == 'katex':
                out.append('<span class="tex">%s^{%s}</span>'
                           % (esc(sg[1]), esc(sg[2])))
            else:
                out.append(to_mathml([sg]))
        elif sg[0] == 'sp':
            if MATH_ENGINE == 'katex':
                out.append('<span class="tex">%s_{%s}^{%s}</span>'
                           % (esc(sg[1]), esc(sg[2]), esc(sg[3])))
            else:
                out.append(to_mathml([sg]))
    return ''.join(out)


def _blank_stem(text):
    """填空题：把填空标记渲染成下划线"""
    cfg = T.FILL['blank']
    pat = '|'.join('(?:%s)' % x for x in cfg['patterns'])
    out, pos = [], 0
    for m in re.finditer(pat, text):
        if m.start() > pos:
            out.append(_rich_html(text[pos:m.start()]))
        # 用 &nbsp; 保底（万一 CSS 未加载还能看出是空位），
        # 实际宽度由 CSS 的 min-width 决定。
        out.append(u'<u class="blank-u">&nbsp;</u>')
        pos = m.end()
    if pos < len(text):
        out.append(_rich_html(text[pos:]))
    return ''.join(out)


def _math_len(t):
    """估算公式渲染宽度 —— 委托给 paper_template.render_width。

    保留此函数是因为 Word/HTML 两端都要用同一个估算口径。
    实现见 paper_template.render_width 的说明：
    分数是上下堆叠的，宽度 = max(分子, 分母)，不是源码字符数。
    """
    return T.render_width(t)


def _opts_html(q):
    opts = q.get('opts') or []
    if not opts:
        return ''
    # 分列依据：**渲染宽度**，不是源码字符数。
    # 见 paper_template.render_width 的说明 ——
    # $\dfrac{4}{3}$ 源码 13 字符，渲染出来只有约 1.4 字符宽，
    # 按源码长度算会被误判成 2 列。
    lens = [T.render_width(t or '') for _, t in opts]
    cols = T.cols_for(max(lens) if lens else 0)
    cells = []
    has_math = any('$' in (t or '') for _, t in opts)
    for L, t in opts:
        cells.append(f'<div class="opt"><b>{esc(L)}．</b>{_rich_html(t)}</div>')
    # 含公式的选项不裁切：CSS 的 overflow:hidden 会把超宽公式
    # 整个切掉（MathML 是整体元素，不像文本能省略号截断）。
    cls = 'opts' + (' opts-noclip' if has_math else '')
    return (f'<div class="{cls}" style="--cols:{cols}">'
            f'{"".join(cells)}</div>')


def render_q(q, sub, qtype, ctx):
    """渲染一个题目模块

    题号独占左侧一列（grid 第 1 列，跨所有行），
    题干/选项/插图/留白全部在第 2 列。

    **为什么题号要独立成列**：原来题号是内联在题干文本流里的
    （`<span class="qnum">1．</span>题干...`），扫题时题号淹没在
    正文里，找第 N 题要逐行读。独立成列后，左侧一列全是数字，
    视线可以直接纵扫定位。

    **其余内容必须各自包在容器里**：grid 布局下裸文本节点会被
    匿名包裹成 grid item，可能串到第 1 列。所以题干一律包 <div>。
    """
    figs = q.get('figs') or []
    # 结构：**题号 与 内容 是两个并列容器，内容内部再流式排布。**
    #
    # 【曾用 grid-row:1/-1 跨行，不可靠】
    # `grid-row: 1 / -1` 的 `-1` 指向**显式网格**的最后一条线。
    # 而 .q 没有定义 grid-template-rows（行是隐式生成的），
    # 于是 span 到 -1 并不能覆盖所有行 —— 题号之后的内容会流回
    # 第 1 列，整块内容被挤向右侧。
    #
    # 改为嵌套：.q 只有两个 grid item（题号、内容），
    # 内容在自己的容器里怎么排都不会跑到题号列。
    inner = []
    if qtype == '填空':
        inner.append('<div>' + _blank_stem(q['stem_text']) + '</div>')
        if figs:
            inner.append(_figs_html(q, sub, 'solve'))
    elif qtype == '解答':
        smark = q.get('smark', '')
        inner.append('<div>' + esc(smark) + _rich_html(q['stem_text']) + '</div>')
        if figs:
            inner.append(_figs_html(q, sub, 'solve'))
        if ctx.get('sec_blank'):
            h = T.SOLVE['answer_space']
            cm = max(h['min'], min(h['max'],
                     h['base'] + q.get('score', 8) * h['per_score']))
            inner.append(f'<div class="blank" style="height:{cm:.2f}cm"></div>')
    else:
        inner.append('<div>' + _rich_html(q['stem_text']) + '</div>')
        if figs:
            inner.append('<div class="qbody">'
                         + _opts_html(q)
                         + _figs_html(q, sub, 'choice')
                         + '</div>')
        else:
            inner.append(_opts_html(q))
    return (f'<div class="q">'
            f'<div class="qnum">{q["num"]}．</div>'
            f'<div class="qmain">{"".join(inner)}</div>'
            f'</div>')


def _css():
    return CSS % {
        'mt': T.PAGE['margin_tb'] * 10, 'mb': T.PAGE['margin_tb'] * 10,
        'ml': T.PAGE['margin_lr'] * 10, 'mr': T.PAGE['margin_lr'] * 10,
        'figmaxh': CFG_FIG_MAX_H_CM,
        'blankw': T.FILL['blank'].get('width_em', 4.0),
    }



def _renumber(qs, secs):
    """编号校验 —— **不做任何重排**。

    题号已由 make_paper.auto_sections() 统一编排。
    这里曾再按 (题号) 重排一次，而 auto_sections 是按
    (科目, 题型, 题号) 排的，两次顺序不一致 →
    按分节题数切分时题目被分进错误的分节
    （「填空题」分节里出现物理解答题）。
    """
    nums = [n for _, ns, _, _ in secs for n in ns]
    if len(nums) != len(set(nums)):
        raise ValueError('分节题号重复: %s' % nums)
    missing = [q['num'] for q in qs if q['num'] not in set(nums)]
    if missing:
        raise ValueError('有题目未被任何分节覆盖: %s' % missing)
    return secs


def build_paper_html(qs, sub, title, sub_title, meta_rows, secs, outdir):
    os.makedirs(outdir, exist_ok=True)
    # 题号重排为 1..N。
    # 组卷出来的卷子题号必须连续：跨年份/跨科目选题时原题号
    # 会是 3、9、17 这种，甚至两科都有「第 4 题」，打印出来没法用。
    _renumber(qs, secs)
    _by_num = {q['num']: q for q in qs}
    h = []
    h.append('<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">')
    h.append(f'<title>{esc(sub_title)}</title>')
    h.append(f'<style>{_css()}</style>')
    if MATH_ENGINE == 'katex':
        h.append(KATEX_HEAD)
    h.append('</head><body><div class="paper">')
    h.append('<div class="tip">提示：按 Ctrl/Cmd + P 打印，'
             '在打印设置中选择「另存为 PDF」，纸张 A4、边距设为「默认」。</div>')
    h.append(f'<div class="title">{esc(title)}</div>')
    h.append(f'<div class="subtitle">{esc(sub_title)}</div>')
    h.append('<hr class="rule">')
    h.append('<table class="meta">')
    for k, v in meta_rows:
        h.append(f'<tr><th>{esc(k)}</th><td>{esc(v)}</td></tr>')
    h.append('</table>')

    ctx = {'sub': sub}
    for sec_name, nums, note, sec_blank in secs:
        h.append(f'<div class="section">{esc(sec_name)}</div>')
        ctx['sec_blank'] = sec_blank
        for n in nums:
            q = _by_num.get(n)
            if not q:
                continue
            # 题型从题目自身读取，不用 T.qtype_of(sub, n)：
            # 后者按题号查全局规则表，混编卷会串到别的科目结构上去。
            qtype = MP._qtype_of_q(q) if hasattr(MP, '_qtype_of_q') \
                else (q.get('type') or '解答')
            h.append(render_q(q, q.get('subject') or sub, qtype, ctx))
    h.append('</div></body></html>')

    # 文件名统一用连字符：下划线在 Markdown 里会被当作斜体标记吃掉，
    # 导致用户看到的文件名少一截（试卷_第3批_X 显示成 试卷第3批X）。
    safe = (sub_title or '练习卷').replace('_', '-')
    path = os.path.join(outdir, f'试卷-{safe}.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(''.join(h))
    return path


def build_answer_html(qs, sub, title, sub_title, meta_rows, src_label, outdir):
    os.makedirs(outdir, exist_ok=True)
    A = T.ANSWER_SHEET
    h = ['<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">',
         f'<title>{esc(sub_title)} 参考答案与解析</title>',
         f'<style>{_css()}</style>']
    if MATH_ENGINE == 'katex':
        h.append(KATEX_HEAD)
    h.append('</head><body><div class="paper">')
    h.append(f'<div class="title">{esc(title)}　参考答案与解析</div>')
    h.append(f'<div class="subtitle">{esc(sub_title)}</div>')
    h.append('<hr class="rule">')
    h.append('<table class="meta">')
    for k, v in meta_rows:
        h.append(f'<tr><th>{esc(k)}</th><td>{esc(v)}</td></tr>')
    h.append('</table>')
    for q in qs:
        ans, ana = q.get('answer'), q.get('ana_text', '')
        if not ans and not ana:
            continue
        h.append(f'<div class="ans"><span class="qnum">{q["num"]}．</span>')
        if ans:
            h.append(f'<span class="a">{esc(A["label_answer"])}{esc(ans)}</span>')
        else:
            h.append(f'<span class="a" style="color:#999">'
                     f'{esc(A["label_answer"])}{esc(A["no_answer_text"])}</span>')
        src = A['source_template'].format(src=src_label, num=q['num'])
        h.append(f'<div class="src">{esc(A["label_source"])}{esc(src)}</div>')
        if ana:
            h.append(f'<div class="ana">{esc(A["label_analysis"])}'
                     f'{_rich_html(ana)}</div>')
        h.append('</div>')
    h.append('</div></body></html>')
    path = os.path.join(outdir, f'答案与解析_{sub_title}.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(''.join(h))
    return path
