/* ============================================================
   题目渲染 —— 与 build_html.py 同源

   关键：公式走浏览器原生 MathML，不用 KaTeX / MathJax。
   理由：零依赖、离线可用、矢量打印，且不引入 CDN 请求。
   ============================================================ */

/**
 * 切片图片的基础 URL。**刻意不带前导斜杠**，这很关键。
 *
 * 带前导斜杠（"/slices/"）时会按协议根解析：
 *   - tauri://  → tauri://localhost/slices/…     ✓
 *   - file://   → file:///slices/…               ✗ 跑到文件系统根目录
 * 不带前导斜杠（"slices/"）时按当前页面所在目录解析，三种协议全对：
 *   - file:///…/src/index.html   → file:///…/src/slices/…      ✓
 *   - tauri://localhost/index.html → tauri://localhost/slices/… ✓
 *   - http://host/index.html     → http://host/slices/…        ✓
 */
export const SLICE_BASE = 'slices/';

const IDENT = /[A-Za-z\u0370-\u03ff]/;

function esc(s) {
  return String(s == null ? '' : s)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

/** 把一串字符包成 MathML 叶子节点 */
function tok(s) {
  if (!s) return '';
  const out = [];
  let i = 0;
  while (i < s.length) {
    const ch = s[i];
    if (IDENT.test(ch)) {
      let j = i;
      while (j < s.length && IDENT.test(s[j])) j++;
      out.push(`<mi>${esc(s.slice(i, j))}</mi>`);
      i = j;
    } else if (/[\d.]/.test(ch)) {
      let j = i;
      while (j < s.length && /[\d.]/.test(s[j])) j++;
      out.push(`<mn>${esc(s.slice(i, j))}</mn>`);
      i = j;
    } else {
      out.push(`<mo>${esc(ch)}</mo>`);
      i++;
    }
  }
  return out.join('');
}

/**
 * 参数内容里的「多余尾部分隔符」。
 *
 * PDF 提取时，根号后面紧跟的逗号常被误吞进花括号：
 *   「半径为 √2 的圆锥」 → `\sqrt{2,}`
 * 渲染成 MathML 就是 √(2,)，逗号是脏数据。
 * 只去**尾部**孤立的 , ，不动 `\sqrt{2,5}` 这种（虽然罕见，
 *  但误删会改变语义）。
 */
function trimArg(s) {
  return String(s == null ? '' : s).trim().replace(/[,，]$/, '').trim();
}

/**
 * 把一个参数（分子/分母/被开方数）转成 MathML。
 *
 * **必须递归**：`\frac{\sqrt{3}}{2}` 的分子本身是个根号，
 * 不递归的话 `\sqrt{3}` 会被 tok() 逐字符拆成
 * `<mo>\</mo><mi>sqrt</mi><mo>{</mo>...`，
 * 屏幕上就显示成源码文本 `\sqrt{3}` —— 正是用户看到的问题。
 */
function leaf(s) {
  if (!s) return '<mi></mi>';
  const t = trimArg(s);
  if (!t) return '<mi></mi>';

  // 先递归：参数里若还有 rac / \sqrt，整棵子树重新解析
  const inner = mergeScript(splitRich(t));
  if (inner.length && inner.some(x => x[0] === 'f' || x[0] === 's' || x[0] === 'm' || x[0] === 'p' || x[0] === 'sp')) {
    const kids = inner.map(sg => {
      if (sg[0] === 't') return sg[1] ? `<mtext>${esc(sg[1])}</mtext>` : '';
      if (sg[0] === 'f') return `<mfrac><mrow>${leaf(sg[1])}</mrow>`
        + `<mrow>${leaf(sg[2])}</mrow></mfrac>`;
      if (sg[0] === 's') return `<msqrt><mrow>${leaf(sg[1])}</mrow></msqrt>`;
      if (sg[0] === 'm') return `<msub>${leaf(sg[1])}<mrow>${leaf(sg[2])}</mrow></msub>`;
      if (sg[0] === 'p') return `<msup>${leaf(sg[1])}<mrow>${leaf(sg[2])}</mrow></msup>`;
      if (sg[0] === 'sp') return `<msubsup>${leaf(sg[1])}<mrow>${leaf(sg[2])}</mrow><mrow>${leaf(sg[3])}</mrow></msubsup>`;
      return '';
    }).join('');
    return kids ? `<mrow>${kids}</mrow>` : '<mi></mi>';
  }

  // 没有嵌套：走简单路径
  if (/^[A-Za-z\u0370-\u03ff]+$/.test(t)) return `<mi>${esc(t)}</mi>`;
  if (/^[\d.]+$/.test(t)) return `<mn>${esc(t)}</mn>`;
  const k = tok(t);
  return k ? `<mrow>${k}</mrow>` : '<mi></mi>';
}

/** 解析 \frac{}{} 与 \sqrt{} */
function splitRich(text) {
  const out = [];
  let i = 0, buf = [];
  const grab = (j) => {                 // 从 j 起取一个 {...}
    while (j < text.length && text[j] !== '{') j++;
    if (j >= text.length) return null;
    let depth = 0, k = j;
    while (k < text.length) {
      if (text[k] === '{') depth++;
      else if (text[k] === '}') {
        depth--;
        if (depth === 0) return [text.slice(j + 1, k), k + 1];
      }
      k++;
    }
    return null;
  };
  const flush = () => { if (buf.length) { out.push(['t', buf.join('')]); buf = []; } };

  while (i < text.length) {
    // $...$ 通用 LaTeX（人工录入）。
    // 用 'L' 而不是 'x'：'x' 已被 mergeScript 用作「待合并的上下标」临时类型，
    // 两者混用会让公式被当成上下标处理。
    if (text[i] === '$') {
      const j = text.indexOf('$', i + 1);
      if (j > i + 1) {
        flush();
        out.push(['L', text.slice(i + 1, j)]);
        i = j + 1;
        continue;
      }
    }
    // 向量 / 上划线 / 粗体（与 extract3.split_rich 的段类型一致）
    let hit = null;
    for (const [cmd, tag] of [
      ['\\overrightarrow', 'V'], ['\\overleftarrow', 'V'],
      ['\\overleftrightarrow', 'V'], ['\\vec', 'V'],
      ['\\overline', 'O'], ['\\hat', 'H'],
      ['\\boldsymbol', 'B'], ['\\pmb', 'B']]) {
      if (text.startsWith(cmd, i)) { hit = [cmd, tag]; break; }
    }
    if (hit) {
      const [cmd, tag] = hit;
      let j = i + cmd.length;
      while (j < text.length && text[j] === ' ') j += 1;
      if (j < text.length && text[j] === '{') {
        const a = grab(j);
        if (a) { flush(); out.push([tag, a[0], cmd]); i = a[1]; continue; }
      }
    }
    // cases 分段函数（与 extract3.split_rich 的 C 段一致）
    if (text.startsWith('\\begin', i)) {
      const em = /^\\begin\s*\{([a-zA-Z*]+)\}/.exec(text.slice(i));
      if (em) {
        const env = em[1];
        const endtag = `\\end{${env}}`;
        let k2 = text.indexOf(endtag, i + em[0].length);
        if (k2 < 0) k2 = text.length;
        const body = text.slice(i + em[0].length, k2);
        flush(); out.push(['C', body, env]); i = k2 + endtag.length; continue;
      }
    }
    if (text.startsWith('\\frac', i)) {
      const a = grab(i + 5);
      if (!a) { buf.push(text[i]); i++; continue; }
      const b = grab(a[1]);
      if (!b) { buf.push(text[i]); i++; continue; }
      flush(); out.push(['f', a[0], b[0]]); i = b[1]; continue;
    }
    if (text.startsWith('\\sqrt', i)) {
      const a = grab(i + 5);
      if (!a) { buf.push(text[i]); i++; continue; }
      flush(); out.push(['s', a[0]]); i = a[1]; continue;
    }
    // 上下标 a_{n+1} / x^{2}：先单独切出 ['u'|'w', 内容]，
    // 随后由 mergeScript() 与前面的基底合并成 ['m'|'p'|'sp', ...]。
    if ((text[i] === '_' || text[i] === '^') && text[i + 1] === '{') {
      const a = grab(i + 1);
      if (!a) { buf.push(text[i]); i++; continue; }
      flush(); out.push([text[i] === '_' ? 'u' : 'w', a[0]]); i = a[1]; continue;
    }
    buf.push(text[i]); i++;
  }
  flush();
  return out;
}

/**
 * 把 ['t', 基底] + ['u', 下标] 合并成 ['m', 基底, 下标]。
 *
 * splitRich 产出的是扁平序列，下标段单独存在会丢失基底
 * （a_{n} 会被切成文本「a」和下标「n」两部分），
 * 必须先把紧邻的前一个字符认作基底合成 <msub>。
 */
function mergeScript(segs) {
  // 1) 连续的上/下标段合并成一个 ['x', sub, sup]
  //    不能用 's' —— 's' 已被根号占用，会与根号段混淆
  const tmp = [];
  let i = 0;
  while (i < segs.length) {
    if (segs[i][0] === 'u' || segs[i][0] === 'w') {
      let sub = '', sup = '';
      let j = i;
      while (j < segs.length && (segs[j][0] === 'u' || segs[j][0] === 'w')) {
        if (segs[j][0] === 'u') sub = segs[j][1] + sub;
        else sup = segs[j][1] + sup;
        j++;
      }
      tmp.push(['x', sub, sup]);
      i = j;
    } else {
      tmp.push(segs[i]); i++;
    }
  }
  // 2) 与紧邻的前一个字符合成基底
  const out = [];
  for (const sg of tmp) {
    if (sg[0] === 'x' && out.length) {
      const last = out[out.length - 1];
      if (last && last[0] === 't' && last[1]) {
        const m = last[1].match(/([A-Za-z\u0370-\u03ff0-9])$/);
        if (m) {
          const base = m[1];
          last[1] = last[1].slice(0, last[1].length - base.length);
          if (sg[1] && sg[2]) out.push(['sp', base, sg[1], sg[2]]);
          else if (sg[1]) out.push(['m', base, sg[1]]);
          else out.push(['p', base, sg[2]]);
          continue;
        }
      }
    }
    out.push(sg);
  }
  return out;
}

/**
 * 行内 LaTeX → MathML（人工录入题目用）
 *
 * 与 py/mathml.py 的 latex_inline() 是**同一套规则的两个实现**。
 * 改符号表时两边都要改 —— 已在 tools/test.mjs 里用
 * 相同样例做一致性断言，防止走偏。
 */
const MACRO = {
  // K12 集合与逻辑高频符号。
  // 这几个漏了会直接输出命令名（页面显示 "mid"、"subsetneq"、"complement"）。
  // 与 py/mathml.py 的 MACRO 保持一致 —— tools/test.mjs 有断言守着。
  '\\mid': '∣', '\\nmid': '∤',
  '\\subsetneq': '⊊', '\\supsetneq': '⊋',
  '\\subsetneqq': '⫋', '\\supsetneqq': '⫌',
  '\\complement': '∁', '\\setminus': '∖',
  '\\varnothing': '∅', '\\emptyset': '∅',
  '\\therefore': '∴', '\\because': '∵',
  '\\le': '≤', '\\leq': '≤', '\\leqslant': '≤', '\\eqslantless': '≤',
  '\\ge': '≥', '\\geq': '≥', '\\geqslant': '≥', '\\eqslantgtr': '≥',
  '\\ne': '≠', '\\neq': '≠', '\\approx': '≈', '\\equiv': '≡',
  '\\sim': '∼', '\\propto': '∝',
  '\\in': '∈', '\\notin': '∉', '\\subset': '⊂', '\\subseteq': '⊆',
  '\\supset': '⊃', '\\supseteq': '⊇', '\\cup': '∪', '\\cap': '∩',
  '\\varnothing': '∅', '\\emptyset': '∅', '\\forall': '∀', '\\exists': '∃',
  '\\times': '×', '\\cdot': '⋅', '\\div': '÷', '\\pm': '±', '\\mp': '∓',
  // 角度相关：``90^\\circ`` 的上标是度数符号 ∘。
  // 缺了它，\\circ 会被当成变量序列 c·i·r·c 逐个输出。
  '\\circ': '∘', '\\degree': '°', '\\prime': '′', '\\angle': '∠',
  '\\to': '→', '\\rightarrow': '→', '\\leftarrow': '←',
  '\\Rightarrow': '⇒', '\\Leftarrow': '⇐', '\\leftrightarrow': '↔',
  '\\perp': '⊥', '\\parallel': '∥', '\\angle': '∠', '\\triangle': '△',
  '\\infty': '∞', '\\ldots': '…', '\\cdots': '⋯', '\\dots': '…',
  '\\prime': '′', '\\partial': '∂', '\\therefore': '∴', '\\because': '∵',
};
const GREEK = {
  alpha: 'α', beta: 'β', gamma: 'γ', delta: 'δ', epsilon: 'ϵ',
  varepsilon: 'ε', zeta: 'ζ', eta: 'η', theta: 'θ', iota: 'ι',
  kappa: 'κ', lambda: 'λ', mu: 'μ', nu: 'ν', xi: 'ξ', pi: 'π',
  rho: 'ρ', sigma: 'σ', tau: 'τ', upsilon: 'υ', phi: 'ϕ',
  varphi: 'φ', chi: 'χ', psi: 'ψ', omega: 'ω',
  Gamma: 'Γ', Delta: 'Δ', Theta: 'Θ', Lambda: 'Λ', Xi: 'Ξ',
  Pi: 'Π', Sigma: 'Σ', Phi: 'Φ', Psi: 'Ψ', Omega: 'Ω',
};
// 恒等映射：\mathbb{R} -> R。
// 与 py/mathml.py 的 BB 表保持一致。
// 不做 Unicode 黑板粗体转换：ℝ/ℕ/ℤ 在部分中文字体里缺字形，
// 会显示成方块 □。
const BB = {};
// 识别「字母 + 左括号 = 函数调用」时可跳过的命令
const LEFT_SKIP = new Set(['left', 'bigl', 'Bigl', 'biggl', 'Biggl',
                           '!', ',', ':', ';', ' ', 'quad', 'qquad']);
/** s 在位置 j 之后（跳过空白与 \left / \! 等）是否是左括号。
 *  只对单个字母启用：f(x) 里 f 是函数名；abc(d) 视为多变量相乘。 */
function isFuncCall(s, j) {
  while (j < s.length) {
    if (/\s/.test(s[j])) { j += 1; continue; }
    if (s[j] === '\\') {
      const m = /^\\[a-zA-Z]+|^\\./.exec(s.slice(j));
      if (!m) return false;
      const nm = m[0].slice(1);
      if (LEFT_SKIP.has(nm)) { j += m[0].length; continue; }
      return false;
    }
    break;
  }
  return j < s.length && (s[j] === '(' || s[j] === '[');
}
const FUNCS = ['sin', 'cos', 'tan', 'cot', 'sec', 'csc', 'arcsin',
  'arccos', 'arctan', 'ln', 'lg', 'log', 'exp', 'max', 'min', 'lim'];

function readArg(s, i) {
  if (i >= s.length) return ['', i];
  if (s[i] === '{') {
    let depth = 0, k = i;
    while (k < s.length) {
      if (s[k] === '{') depth++;
      else if (s[k] === '}') { depth--; if (depth === 0) return [s.slice(i + 1, k), k + 1]; }
      k++;
    }
    return [s.slice(i + 1), s.length];
  }
  return [s[i], i + 1];
}

/** 读上下标参数：`x^2` 里 ^ 后面那一段。
 *  与 readArg 的区别：readArg 对非 `{` 只取单个字符，
 *  于是 `90^\circ` 的上标被取成 `\`，剩下 circ 被当成 c·i·r·c。
 *  上下标支持：{..} 取组内；\cmd 取整条命令；其他取单字符。 */
function readScriptArg(s, i) {
  if (i >= s.length) return ['', i];
  if (s[i] === '{') return readArg(s, i);
  if (s[i] === '\\') {
    const m = /^\\[a-zA-Z]+|^\\./.exec(s.slice(i));
    if (m) return [m[0], i + m[0].length];
    return [s[i], i + 1];
  }
  return [s[i], i + 1];
}

function parseLatex(s, i, stop) {
  const out = [];
  while (i < s.length) {
    const c = s[i];
    if (stop && stop.includes(c)) break;
    if (c === '\\') {
      const m = s.slice(i + 1).match(/^[a-zA-Z]+/) || s.slice(i + 1).match(/^./);
      const name = m ? m[0] : '';
      const key = '\\' + name;
      let k = i + 1 + name.length;
      if (['left', 'right', 'big', 'Big', 'bigg', 'Bigg'].includes(name)) { i = k; continue; }
      if ([',', ';', ':', '!', ' '].includes(name) || name === 'quad' || name === 'qquad') { i = k; continue; }
      if (name === '\\' || name === '\n') { i = k; continue; }
      // \dfrac / \tfrac 与 \frac 同构：行内渲染无 display/text 之分，
      // 三者等价。只认 frac 会让 \dfrac 落进未知宏分支，
      // 输出 <mi>dfrac</mi> 后跟散落的数字，分数结构整个丢失。
      if (name === 'frac' || name === 'dfrac' || name === 'tfrac') {
        const [n1, p1] = readArg(s, k);
        const [n2, p2] = readArg(s, p1);
        out.push(`<mfrac><mrow>${parseLatex(n1, 0).join('')}</mrow><mrow>${parseLatex(n2, 0).join('')}</mrow></mfrac>`);
        i = p2; continue;
      }
      if (name === 'sqrt') {
        const [body, p] = readArg(s, k);
        out.push(`<msqrt><mrow>${parseLatex(body, 0).join('')}</mrow></msqrt>`);
        i = p; continue;
      }
      // 向量 / 上划线 / 粗体：K12 高频记号。
      // 缺了它们会原样输出命令名（overrightarrowCA），完全读不通。
      if (['overrightarrow', 'overleftarrow', 'overleftrightarrow', 'vec',
           'overline', 'underline', 'hat', 'bar'].includes(name)) {
        const [body, p] = readArg(s, k);
        const kids = parseLatex(body, 0).join('');
        const ACC = { overrightarrow: '\u2192', overleftarrow: '\u2190',
                      overleftrightarrow: '\u2194', vec: '\u20D7',
                      overline: '\u00AF', underline: '\u0332',
                      hat: '^', bar: '\u00AF' };
        const stretch = name.startsWith('over') ? 'true' : 'false';
        out.push(`<mover accent="true"><mrow>${kids || '<mi></mi>'}</mrow>` +
                 `<mo stretchy="${stretch}">${ACC[name]}</mo></mover>`);
        i = p; continue;
      }
      if (name === 'boldsymbol' || name === 'pmb') {
        const [body, p] = readArg(s, k);
        const kids = parseLatex(body, 0).join('');
        out.push(`<mstyle mathvariant="bold">${kids || '<mi></mi>'}</mstyle>`);
        i = p; continue;
      }
      // 转义花括号 \{ \} → <mo>（正体）。
      // 走"未知宏"分支会输出 <mi>{</mi>，mi 默认斜体，
      // {1,2} 的花括号会显示成斜体，很怪。
      if (name === '{' || name === '}') {
        out.push(`<mo>${name}</mo>`); i = k; continue;
      }
      // \begin{cases}...\end{cases}：分段函数（K12 高频）。
      // 不支持会输出 "begin cases" 源码。
      if (name === 'begin') {
        const em = /^\s*\{([a-zA-Z*]+)\}/.exec(s.slice(k));
        if (em) {
          const env = em[1];
          const endtag = `\\end{${env}}`;
          const k2 = s.indexOf(endtag, k + em[0].length);
          const stopAt = k2 < 0 ? s.length : k2;
          const body = s.slice(k + em[0].length, stopAt);
          const rows = body.split('\\\\').map((ln) => ln.trim())
            .filter(Boolean).map((ln) => {
              const tds = ln.split('&').map((c) => {
                const kd = parseLatex(c.trim(), 0).join('');
                return `<mtd>${kd || '<mi></mi>'}</mtd>`;
              }).join('');
              return tds ? `<mtr>${tds}</mtr>` : '';
            }).join('');
          if (env === 'cases' || env === 'dcases') {
            // rowspacing 必须显式收紧：mtable 默认行距较松，
            // 2 行的 cases 会让左侧 stretchy 的 { 被撑得很高。
            // 与 py/mathml.py 保持同样的 0.15ex。
            // 与 py/mathml.py 同步：mstyle displaystyle="false" 是压低
            // 高度的关键（非展示模式行高更小），
            // rowspacing + framespacing 去掉多余留白。
            out.push(`<mrow><mo stretchy="true">{</mo>` +
                     `<mstyle displaystyle="false">` +
                     `<mtable columnspacing="0.6em" rowspacing="0.1ex" ` +
                     `framespacing="0 0" columnalign="left">${rows}` +
                     `</mtable></mstyle></mrow>`);
          } else {
            out.push(`<mtable>${rows}</mtable>`);
          }
          i = stopAt + endtag.length; continue;
        }
      }
      if (name === 'mathbb' || name === 'mathbf') {
        const [body, p] = readArg(s, k);
        // 数集必须正体：斜体的 R 会被当成普通变量
        out.push(`<mi mathvariant="normal">${esc(BB[body.trim()] || body)}</mi>`);
        i = p; continue;
      }
      if (name === 'text' || name === 'mathrm') {
        const [body, p] = readArg(s, k);
        out.push(`<mtext>${esc(body)}</mtext>`);
        i = p; continue;
      }
      if (GREEK[name]) { out.push(`<mi>${esc(GREEK[name])}</mi>`); i = k; continue; }
      if (MACRO[key]) { out.push(`<mo>${esc(MACRO[key])}</mo>`); i = k; continue; }
      if (FUNCS.includes(name)) { out.push(`<mi mathvariant="normal">${esc(name)}</mi>`); i = k; continue; }
      out.push(`<mi>${esc(name)}</mi>`); i = k; continue;
    }
    if (c === '_' || c === '^') {
      const base = out.length ? out.pop() : '<mi></mi>';
      const [arg, i2] = readScriptArg(s, i + 1);
      const a = parseLatex(arg, 0).join('');
      let j2 = i2;
      while (j2 < s.length && /[ \t]/.test(s[j2])) j2++;
      if (j2 < s.length && (s[j2] === '_' || s[j2] === '^') && s[j2] !== c) {
        const [a2, i3] = readScriptArg(s, j2 + 1);
        const b2 = parseLatex(a2, 0).join('');
        out.push(c === '_' ? `<msubsup>${base}${a}${b2}</msubsup>`
                           : `<msubsup>${base}${b2}${a}</msubsup>`);
        i = i3; continue;
      }
      out.push(c === '_' ? `<msub>${base}<mrow>${a}</mrow></msub>`
                         : `<msup>${base}<mrow>${a}</mrow></msup>`);
      i = i2; continue;
    }
    if (c === '{') {
      const [body, p] = readArg(s, i);
      const kids = parseLatex(body, 0).join('');
      out.push(kids ? `<mrow>${kids}</mrow>` : '<mi></mi>');
      i = p; continue;
    }
    if (c === '}') { i++; continue; }
    if (/[A-Za-z\u0370-\u03ff]/.test(c)) {
      let j = i;
      while (j < s.length && /[A-Za-z\u0370-\u03ff]/.test(s[j])) j++;
      const w = s.slice(i, j);
      if (FUNCS.includes(w)) out.push(`<mi mathvariant="normal">${esc(w)}</mi>`);
      // 单字母函数：f(x)、g(x) 里的 f/g 是函数名，应排正体。
      // 必须跳过 \left / \! 等间距命令，否则 f\!\left(x\right) 会漏判。
      else if (w.length === 1 && isFuncCall(s, j)) out.push(`<mi mathvariant="normal">${esc(w)}</mi>`);
      else for (const ch of w) out.push(`<mi>${esc(ch)}</mi>`);
      i = j; continue;
    }
    if (/[0-9.]/.test(c)) {
      let j = i;
      while (j < s.length && /[0-9.]/.test(s[j])) j++;
      out.push(`<mn>${esc(s.slice(i, j))}</mn>`);
      i = j; continue;
    }
    // 定界符（圆括号、方括号、竖线）显式声明**不可拉伸**。
    // <mo> 默认 stretchy=true，会跟随所在 mrow 的总高度拉伸 ——
    // 于是 f(x)={cases} 里的 ( ) 会被右侧 2 行高的分段函数
    // 一起拉到同样高度（用户反馈的"f(x) 的括号特别大"）。
    // 与 py/mathml.py 保持同一规则。
    if ('+-*/=<>()[]|'.includes(c)) {
      if ('()[]|'.includes(c)) out.push(`<mo stretchy="false">${esc(c)}</mo>`);
      else out.push(`<mo>${esc(c)}</mo>`);
      i++; continue;
    }
    if (/\s/.test(c)) { i++; continue; }
    out.push(`<mo>${esc(c)}</mo>`); i++;
  }
  return out;
}

function latexToMathml(src) {
  const t = String(src || '').trim();
  if (!t) return '';
  const kids = parseLatex(t, 0);
  if (!kids.length) return '';
  const body = kids.length === 1 ? kids[0] : `<mrow>${kids.join('')}</mrow>`;
  return `<math ${MML}>${body}</math>`;
}

function mergeSub(segs) { return mergeScript(segs); }

const MML = 'xmlns="http://www.w3.org/1998/Math/MathML" display="inline"';

function toMathml(segs) {
  const has = segs.some(s => s[0] === 'f' || s[0] === 's' || s[0] === 'm' || s[0] === 'p' || s[0] === 'sp' || s[0] === 'L');
  if (!has) return '';
  const kids = segs.map(sg => {
    if (sg[0] === 't') return sg[1] ? `<mtext>${esc(sg[1])}</mtext>` : '';
    if (sg[0] === 'f')
      return `<mfrac><mrow>${leaf(sg[1])}</mrow><mrow>${leaf(sg[2])}</mrow></mfrac>`;
    if (sg[0] === 's') return `<msqrt><mrow>${leaf(sg[1])}</mrow></msqrt>`;
    if (sg[0] === 'm') return `<msub>${leaf(sg[1])}<mrow>${leaf(sg[2])}</mrow></msub>`;
    if (sg[0] === 'p') return `<msup>${leaf(sg[1])}<mrow>${leaf(sg[2])}</mrow></msup>`;
    if (sg[0] === 'sp') return `<msubsup>${leaf(sg[1])}<mrow>${leaf(sg[2])}</mrow><mrow>${leaf(sg[3])}</mrow></msubsup>`;
    if (sg[0] === 'L') return latexToMathml(sg[1]);
    return '';
  }).join('');
  if (!kids) return '';
  const body = segs.length === 1 ? kids : `<mrow>${kids}</mrow>`;
  return `<math ${MML}>${body}</math>`;
}

/** 文本（可含 LaTeX）→ HTML */
export function rich(text) {
  if (text == null || text === '') return '';
  const segs = mergeScript(splitRich(String(text)));
  // **必须把 'L' 算进去**：$...$ 是人工录入题目的通用写法，
  // 漏掉它的话 $f(x)$ 这种不含 \frac/\sqrt/上下标的公式
  // 会走 esc() 直接输出源码 —— 练习页上孩子看到的是 $f(x)$ 而不是 f(x)。
  if (!segs.some(s => s[0] === 'f' || s[0] === 's' || s[0] === 'm'
                   || s[0] === 'p' || s[0] === 'sp' || s[0] === 'L')) return esc(text);
  return segs.map(sg => {
    if (sg[0] === 't') return esc(sg[1]);
    if (sg[0] === 'L') return latexToMathml(sg[1]);
    return toMathml([sg]);
  }).join('');
}

/** 填空题：把句末句号等标记渲染成下划线 */
const BLANK_PAT = new RegExp([
  '_{2,}', '＿{1,}',
  '(?<=为)\\s*．', '(?<=是)\\s*．', '(?<==)\\s*．',
  '．\\s*(?=$|；|，)', '(?<==)(?=[，。；])',
].map(x => '(?:' + x + ')').join('|'), 'g');

export function blankStem(text) {
  const s = String(text || '');
  let out = '', pos = 0, m;
  BLANK_PAT.lastIndex = 0;
  while ((m = BLANK_PAT.exec(s)) !== null) {
    if (m.index > pos) out += rich(s.slice(pos, m.index));
    out += '<u class="blank-u">&emsp;&emsp;</u>';
    pos = m.index + m[0].length;
  }
  if (pos < s.length) out += rich(s.slice(pos));
  return out;
}

/** 选项列数（与 paper_template 的 col_rules 一致） */
function colsFor(maxlen) {
  if (maxlen <= 8) return 4;
  if (maxlen <= 26) return 2;
  return 1;
}

/**
 * 插图 HTML。baseUrl 为切片目录前缀，必须以 / 结尾。
 * 注意：科目目录名是中文，需要 encodeURIComponent，
 * 否则在部分浏览器/服务器下会取不到图。
 */
function figsHtml(q, baseUrl) {
  const figs = q.figs || [];
  if (!figs.length) return '';
  const items = figs.map((fg, i) => {
    const src = baseUrl + encodeURIComponent(q.subject) + '/' + fg.file;
    const cap = figs.length === 1
      ? `第${q.num}题图`
      : `第${q.num}题图${i + 1}`;
    return `<figure><img src="${esc(src)}" alt=""><figcaption>${cap}</figcaption></figure>`;
  }).join('');
  return `<div class="figs"><div class="figrow">${items}</div></div>`;
}

function optsHtml(q, pickable) {
  const opts = q.opts || [];
  if (!opts.length) return '';
  const plain = opts.map(o => String(o[1])
    .replace(/\\(frac|sqrt)\{[^{}]*\}(\{[^{}]*\})?/g, 'xx'));
  const cols = colsFor(Math.max(...plain.map(x => x.length), 0));
  const cells = opts.map(([L, t]) =>
    `<div class="opt${pickable ? ' pick' : ''}" data-val="${esc(L)}">` +
    `<b>${esc(L)}．</b>${rich(t)}</div>`).join('');
  return `<div class="opts" style="--cols:${cols}">${cells}</div>`;
}

/**
 * 渲染单题
 * @param {object} q 题目
 * @param {object} opt { pickable, baseUrl, showAnswer }
 */
export function renderQuestion(q, opt = {}) {
  const { pickable = false, baseUrl = SLICE_BASE, showAnswer = false } = opt;
  const figs = figsHtml(q, baseUrl);
  let body = '';

  if (q.type === '填空') {
    body = '<div>' + blankStem(q.stem_text) + figs + '</div>';
  } else if (q.type === '解答') {
    const smark = q.smark ? esc(q.smark) : '';
    body = '<div>' + smark + rich(q.stem_text) + figs;
    const sc = Math.max(3.0, Math.min(7.2, 1.6 + (q.score || 8) * 0.28));
    body += `<div class="blank" style="height:${sc.toFixed(2)}cm"></div></div>`;
  } else {
    body = '<div>' + rich(q.stem_text) + '</div>';
    body += figs
      ? `<div class="qbody">${optsHtml(q, pickable)}${figs}</div>`
      : optsHtml(q, pickable);
  }
  // 题号与内容是两个并列容器：.q 只有两个 grid item，
  // 内容在 .qmain 内部流式排布。
  // 不用 grid-row:1/-1 —— 隐式网格下它不能跨所有行，
  // 内容会流回第1列，整块被挤向右侧（与 build_html.py 同样的坑）。
  body = `<div class="qnum">${q.num}．</div><div class="qmain">${body}</div>`;

  if (showAnswer) {
    const ans = q.answer && !String(q.answer).includes('原卷无答案')
      ? esc(q.answer) : '<span style="color:#999">（原卷无答案）</span>';
    const ana = q.ana_text ? `<div class="ana"><b>【解析】</b>${rich(q.ana_text)}</div>` : '';
    body += `<div class="answer-box show"><b>【答案】</b>${ans}${ana}</div>`;
  }

  const tag = `<span class="no-print" style="font-size:11px;color:#9aa;font-weight:400">`
    + `${esc(q.id)}　${esc(q.level || '')}</span>`;
  // data-type：拖动排序时用来限制"只能在同题型内移动"。
  // 卷面是按题型分节的（一、选择题 二、填空题…），
  // 跨题型拖动会把分节结构搅乱，也会让题号重排失去意义。
  return `<div class="q" data-id="${esc(q.id)}" data-type="${esc(q.type || '')}">`
    + `${body}${tag}</div>`;
}

/** 渲染整卷（按题型分节）
 * @param {Array} questions 题目列表
 * @param {object} meta { title, sub, rows, baseUrl }
 */
export function renderPaper(questions, meta = {}) {
  const baseUrl = meta.baseUrl || SLICE_BASE;
  const groups = [];
  for (const q of questions) {
    const t = q.type || '解答';
    const last = groups[groups.length - 1];
    if (last && last.type === t) last.items.push(q);
    else groups.push({ type: t, items: [q] });
  }
  // 序号按实际出现的分节动态生成。
  // 硬编码「一、选择」「二、填空」「三、解答」会导致：
  // 只组了解答题时，卷子上赫然写着「三、解答题」。
  const CN = ['一', '二', '三', '四', '五', '六'];
  const SEC = {
    '选择': '%I%、选择题：在每小题给出的四个选项中，只有一项是符合题目要求的。',
    '填空': '%I%、填空题：本题共 %N% 小题。',
    '解答': '%I%、解答题：解答应写出文字说明、证明过程或演算步骤。',
  };
  let h = `<div class="title">${esc(meta.title || '自动组卷')}</div>`;
  if (meta.sub) h += `<div class="subtitle">${esc(meta.sub)}</div>`;
  h += '<hr class="rule">';
  if (meta.rows && meta.rows.length) {
    h += '<table class="meta">';
    for (const [k, v] of meta.rows) h += `<tr><th>${esc(k)}</th><td>${esc(v)}</td></tr>`;
    h += '</table>';
  }
  let secIdx = 0;
  for (const g of groups) {
    const tpl = SEC[g.type];
    let text;
    if (tpl) {
      text = tpl.replace('%I%', CN[secIdx] || (secIdx + 1))
                .replace('%N%', g.items.length);
      secIdx++;
    } else {
      text = `${g.type}（${g.items.length} 题）`;
    }
    h += `<div class="section">${esc(text)}</div>`;
    // baseUrl 必须一路传下去，否则带图题目在组卷页显示不出插图
    for (const q of g.items) h += renderQuestion(q, { baseUrl });
  }
  return `<div class="paper">${h}</div>`;
}
