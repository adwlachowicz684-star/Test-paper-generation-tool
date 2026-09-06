
import { rich, blankStem, renderQuestion, renderPaper } from '../src/app/render.js';
import { grade, summarize } from '../src/app/grade.js';

let pass = 0, fail = 0;
const ok = (c, m) => { if (c) pass++; else { fail++; console.log('  X', m); } };

// ---- MathML ----
const r1 = rich('\\frac{ab}{gb}');
ok(r1.includes('<mfrac>'), 'frac: ' + r1);
ok(r1.includes('<mi>ab</mi>') && r1.includes('<mi>gb</mi>'), 'num/den: ' + r1);
const r2 = rich('2\\sqrt{3}');
ok(r2.includes('<msqrt>'), 'sqrt: ' + r2);
ok(rich('plain text') === 'plain text', 'plain passthrough');
const r4 = rich('x = \\frac{1}{2} then');
// 纯文本片段在 HTML 上下文直接输出，不包 <mtext>；只有公式段用 <math>
ok(r4.includes('x = ') && r4.includes('<mfrac>') && r4.includes(' then'), 'mixed: ' + r4.slice(0,70));

// ---- blank ----
ok(blankStem('离心率为．').includes('<u class="blank-u">'), 'underline');
ok(blankStem('值为____').includes('<u class="blank-u">'), 'underscore');

// ---- escape ----
ok(!rich('<script>x</script>').includes('<script>'), 'escape XSS');

// ---- grade: single choice ----
let g = grade({type:'选择', answer:'B', subtype:'单选'}, 'B');
ok(g.correct === true && g.score === 5, 'single right');
g = grade({type:'选择', answer:'B', subtype:'单选'}, 'C');
ok(g.correct === false && g.score === 0, 'single wrong');

// ---- grade: multi ----
g = grade({type:'选择', answer:'AB', subtype:'多选题-2个答案'}, 'AB');
ok(g.correct === true && g.score === 5, 'multi full');
g = grade({type:'选择', answer:'AB', subtype:'多选题-2个答案'}, 'A');
ok(g.partial === true && g.score === 2, 'multi partial: ' + JSON.stringify(g));
g = grade({type:'选择', answer:'AB', subtype:'多选题-2个答案'}, 'AC');
ok(g.correct === false && g.score === 0, 'multi with wrong sel = 0');
g = grade({type:'选择', answer:'AB', subtype:'多选题-2个答案'}, 'BA');
ok(g.correct === true, 'multi order-insensitive');

// ---- grade: fill ----
ok(grade({type:'填空', answer:'12'}, '12').correct === true, 'fill right');
ok(grade({type:'填空', answer:'12'}, '13').correct === false, 'fill wrong');

// ---- no answer ----
ok(grade({type:'选择', answer:'（原卷无答案）'}, 'A').needSelf === true, 'needSelf');
ok(grade({type:'解答', answer:'x', score:15}, 'y').needSelf === true, 'solve self');

// ---- empty answer ----
g = grade({type:'选择', answer:'A', subtype:'单选'}, '');
ok(g.correct === false && g.score === 0, 'empty answer = wrong');

// ---- summarize ----
const s = summarize([
  {correct:true, partial:false, score:5, fullScore:5, needSelf:false},
  {correct:false, partial:true, score:2, fullScore:5, needSelf:false},
  {correct:false, partial:false, score:0, fullScore:5, needSelf:false},
  {correct:null, partial:false, score:0, fullScore:12, needSelf:true},
]);
ok(s.got === 7 && s.full === 27, 'sum score: ' + JSON.stringify(s));
ok(s.nSelf===1 && s.nRight===1 && s.nPartial===1 && s.nWrong===1, 'sum count');
ok(s.acc === 33, 'acc: ' + s.acc);

// ---- grade: fill (严格化后) ----
// 曾用 e.includes(g) || g.includes(e)，导致 答案12 / 学生答1 判为正确，
// 错题进不了复习队列，整套间隔复习失效。以下用例锁死该行为。
const fillCases = [
  ['12', '1', false], ['12', '12', true],
  ['-3', '3', false], ['-3', '-3', true],
  ['3/4', '3', false], ['3/4', '6/8', true], ['3/4', '0.75', true],
  ['0.5', '1/2', true], ['100', '10', false],
  ['2;3', '2;3', true], ['2;3', '2;5', false], ['2;3', '2', false],
];
let fillBad = 0;
for (const [e, g, want] of fillCases) {
  const r = grade({ type: '填空', answer: e }, g);
  if (r.correct !== want) { fillBad++; console.log('  X fill', e, g, '→', r.correct); }
}
ok(fillBad === 0, 'fill grading: ' + fillBad + ' cases wrong');

// ---- 公式渲染：不得出现 LaTeX 源码字面量 ----
// 曾因 leaf() 不递归，\frac{\sqrt{3}}{2} 的分子被当普通文本，
// 屏幕上直接显示 \sqrt{3}。以下用例锁死该行为。
const mathCases = [
  String.raw`\sqrt{3}`,
  String.raw`2\sqrt{3}`,
  String.raw`\sqrt{2,}`,                 // 逗号是 PDF 提取脏数据，须清掉
  String.raw`\frac{\sqrt{3}}{2}`,       // 嵌套：分数里套根号
  String.raw`\sqrt{\frac{1}{2}}`,       // 嵌套：根号里套分数
  String.raw`\frac{1}{2}`,
];
let mathBad = 0;
for (const c of mathCases) {
  const h = rich(c);
  // 检测字面量（带反斜杠），mfrac/msqrt 是正常的 MathML 标签
  if (/\\[a-z]+/.test(h)) { mathBad++; console.log('  X math leak:', c, '→', h.slice(0, 90)); }
  if (!/<math /.test(h)) { mathBad++; console.log('  X no <math>:', c); }
}
ok(mathBad === 0, 'math render: ' + mathBad + ' cases leaked source');

// 逗号清理：√(2,) 必须渲染成 √(2)
{
  const h = rich(String.raw`\sqrt{2,}`);
  const nums = [...h.matchAll(/<mn>([^<]*)<\/mn>/g)].map(m => m[1]);
  ok(nums.length === 1 && nums[0] === '2',
     'sqrt trailing comma trimmed: ' + JSON.stringify(nums));
}
// 不能误伤 \sqrt{2,5}
{
  const h = rich(String.raw`\sqrt{2,5}`);
  // 渲染后 2/5 变 <mn>、逗号变 <mo>，不再是连续字符串，按节点序列检查
  const seq = [...h.matchAll(/<(mn|mo)>([^<]*)<\/(?:mn|mo)>/g)].map(m => m[2]);
  ok(seq.join('') === '2,5', 'sqrt{2,5} middle comma kept: ' + JSON.stringify(seq));
}

// ---- 下标渲染 ----
// PDF 提取把 a_{n+1} 压成 an+1；还原后必须渲染成 <msub>，
// 不能在页面上看到 a_{n+1} 这种源码文本。
{
  const h = rich('数列 {a_{n}} 满足 a_{n+1} = a_{n} + 2');
  ok((h.match(/<msub>/g) || []).length === 3,
     'subscripts render as msub: ' + (h.match(/<msub>/g) || []).length);
  ok(!/_{/.test(h), 'no raw _{} left: ' + h.slice(0, 80));
  // 下标里套分数
  const h2 = rich(String.raw`a_{\frac{1}{2}}`);
  ok(/<msub>[\s\S]*<mfrac>/.test(h2), 'nested frac inside subscript');
}

// ---- renderQuestion ----
const q = {id:'P-2026-011', num:11, subject:'物理', type:'选择', level:'适中',
  stem_text:'小球沿正方形线框运行，冲量比值为（ ）',
  opts:[['A','\\frac{ab}{gb}'],['B','\\frac{ab}{bd}']]};
const h = renderQuestion(q, {pickable:true});
ok(h.includes('data-id="P-2026-011"'), 'render id');
ok(h.includes('<mfrac>'), 'render mathml');
ok(h.includes('opt pick'), 'render pickable');
ok(h.includes('A．'), 'render option letter');

// ---- 上标（区分于下标）----
// PDF 里 x3 既可能是 x³ 也可能是 x₃，靠**源信息**（字号+基线）区分，
// 绝不能靠「字母+数字」猜。以下锁死：上标走 msup，不退化成 msub。
{
  const h = rich('f(x) = x^{3} − x + 1');
  ok(/<msup>/.test(h), 'superscript renders as msup');
  ok(!/<msub>/.test(h), 'superscript must not become msub');
}
{
  // 同一基底同时有上下标 → msubsup
  const h = rich('x^{2}_{1}');
  ok(/<msubsup>/.test(h), 'sub+sup renders as msubsup: ' + h.slice(0, 70));
}
{
  // 根号标记 's' 与上/下标组 'x' 不能混淆
  const h = rich(String.raw`2\sqrt{3}`);
  ok(/<msqrt>/.test(h) && !/<msub>/.test(h),
     'sqrt not confused with subscript: ' + h.slice(0, 70));
}

console.log('\nPASS ' + pass + ' / ' + (pass+fail));
if (fail) process.exit(1);

