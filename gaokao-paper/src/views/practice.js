/* ============================================================
   练习视图 —— 整套系统最大的价值点

   传统流程：纸上做题 → 家长批改 → 手工登记 Excel → 算下次复习日
   这里：点选答案 → 自动判分 → 自动写记录 → 自动算复习日
   「批改后不登记」这个最大的失败点被彻底消灭。
   ============================================================ */
import { api } from '../app/api.js';
import { renderQuestion, SLICE_BASE } from '../app/render.js';

const baseUrl = SLICE_BASE;
import { grade, summarize } from '../app/grade.js';

let S = {
  questions: [],
  answers: {},      // id -> 学生答案
  submitted: false,
  results: {},
  source: '',       // 'due' | 'compose' | 'manual'
};

/**
 * 待练队列 —— 「组卷 → 在线练习」的桥梁。
 *
 * 组卷页生成试卷后，必须能直接送进来作答登记。
 * 少了这个通道，组出来的卷子只能打印 → 手工批改 → 手工登记，
 * 又回到最初想消灭的手工环节，整套系统就白做了。
 */
let _pending = null;

export function setPending(questions, source = 'compose') {
  _pending = (questions && questions.length) ? { questions, source } : null;
}

export function hasPending() { return !!_pending; }

export async function mount(root, opts = {}) {
  root.innerHTML = `
    <h2 class="title">在线练习</h2>
    <p class="sub">做完提交后自动判分，并按记忆曲线算出下次复习日 —— 无需手工登记。</p>
    <div id="prac-msg"></div>
    <div id="prac-body"></div>
  `;

  // 优先级：显式传入 > 待练队列（从组卷页过来）> 到期题
  if (opts.questions && opts.questions.length) {
    S.questions = opts.questions;
    S.source = opts.source || 'manual';
    render();
  } else if (_pending) {
    S.questions = _pending.questions;
    S.source = _pending.source;
    _pending = null;
    render();
  } else {
    await loadDue();
  }
}

/** 默认载入到期题；没有到期题则提示去组卷 */
async function loadDue() {
  const body = document.querySelector('#prac-body');
  const msg = document.querySelector('#prac-msg');
  body.innerHTML = '<div class="card">正在检查到期题目…</div>';
  try {
    const r = await api.due();
    if (r.count) {
      S.questions = r.items;
      S.source = 'due';
      msg.className = 'msg info show';
      msg.textContent = `有 ${r.count} 道题到期需要复习，已自动载入。`;
      render();
    } else {
      S.questions = [];
      S.source = 'manual';
      body.innerHTML = `
        <div class="card">
          <h3>今天没有到期题</h3>
          <p style="color:#5a6472;font-size:13px;margin:0 0 12px">
            到期题由错题和按间隔应复习的题组成。你可以：</p>
          <div class="row">
            <button class="primary" id="go-compose">去组卷练新题</button>
            <button id="go-stats">查看学习统计</button>
          </div>
        </div>`;
      const gc = document.querySelector('#go-compose');
      if (gc) gc.onclick = () => location.hash = '#/compose';
      const gs = document.querySelector('#go-stats');
      if (gs) gs.onclick = () => location.hash = '#/stats';
    }
  } catch (e) {
    msg.className = 'msg err show';
    msg.textContent = '加载失败：' + e.message;
    body.innerHTML = '';
  }
}

function render() {
  const body = document.querySelector('#prac-body');
  const qs = S.questions;
  if (!qs.length) return;

  const isDue = S.source === 'due';
  body.innerHTML = `
    <div class="card no-print" style="padding:10px 14px">
      <div class="row">
        <span style="font-size:13px;color:#5a6472">
          共 <b>${qs.length}</b> 题
          ${isDue ? '（到期复习）' : ''}
        </span>
        <button class="primary" id="btn-submit">提交并判分</button>
        <button id="btn-print-p">打印空白卷</button>
        <span id="fill-hint" style="font-size:12px;color:#9aa"></span>
      </div>
    </div>
    <div class="paper-wrap" id="pw"></div>
    <div id="summary"></div>`;

  const pw = document.querySelector('#pw');
  pw.innerHTML = qs.map(q => renderQuestion(q, { pickable: true, baseUrl })).join('');

  // 选择题点选
  pw.querySelectorAll('.opt.pick').forEach(el => {
    el.onclick = () => {
      if (S.submitted) return;
      const qEl = el.closest('.q');
      const id = qEl.dataset.id;
      const q = qs.find(x => x.id === id);
      if (/多选/.test((q.subtype || '') + (q.type || ''))) {
        // 多选：可点选多个
        el.classList.toggle('sel');
        const sel = [...qEl.querySelectorAll('.opt.pick.sel')]
          .map(x => x.dataset.val).sort().join('');
        S.answers[id] = sel;
      } else {
        qEl.querySelectorAll('.opt.pick').forEach(x => x.classList.remove('sel'));
        el.classList.add('sel');
        S.answers[id] = el.dataset.val;
      }
      updHint();
    };
  });

  // 填空题输入
  // 多空题（如答案 "2;3"）给每个空一个独立输入框，
  // 避免学生把两个空填进一个框里、格式不对被判错。
  qs.forEach(q => {
    if (q.type !== '填空') return;
    const qEl = pw.querySelector(`.q[data-id="${q.id}"]`);
    if (!qEl) return;

    const blanks = countBlanks(q.answer, q);
    const inputs = blanks === 1
      ? `<input type="text" data-fill="${q.id}" data-i="0"
                style="width:200px" placeholder="填数值或表达式">`
      : Array.from({ length: blanks }, (_, i) =>
          `<span style="font-size:12px;color:#5a6472">第${i + 1}空</span>
           <input type="text" data-fill="${q.id}" data-i="${i}"
                  style="width:120px">`).join(' ');

    const inp = document.createElement('div');
    inp.className = 'no-print';
    inp.innerHTML = `<div class="row" style="margin:6px 0 12px">
        <label style="min-width:auto">你的答案</label>
        ${inputs}
        ${blanks > 1 ? '<span style="font-size:11px;color:#9aa">'
                       + '分数请写 3/4 或 0.75</span>' : ''}
      </div>`;
    qEl.appendChild(inp);

    // 多个输入框的值按空序拼成 "a;b"
    const boxes = [...inp.querySelectorAll('input[data-fill]')];
    const collect = () => {
      S.answers[q.id] = boxes.map(b => b.value.trim()).join(';').trim();
      updHint();
    };
    boxes.forEach(b => { b.oninput = collect; });
  });

  // 解答题自评
  qs.forEach(q => {
    if (q.type !== '解答') return;
    const qEl = pw.querySelector(`.q[data-id="${q.id}"]`);
    if (!qEl) return;
    const box = document.createElement('div');
    box.className = 'no-print';
    box.innerHTML = `<div class="row" style="margin:8px 0 14px">
        <label style="min-width:auto">自评</label>
        <span class="chip" data-self="${q.id}" data-v="1">做对了</span>
        <span class="chip" data-self="${q.id}" data-v="0">没做对</span>
      </div>`;
    qEl.appendChild(box);
    box.querySelectorAll('.chip').forEach(c => {
      c.onclick = () => {
        box.querySelectorAll('.chip').forEach(x => x.classList.remove('on'));
        c.classList.add('on');
        S.answers[q.id] = c.dataset.v === '1' ? '__ok__' : '__no__';
        updHint();
      };
    });
  });

  document.querySelector('#btn-submit').onclick = submit;
  document.querySelector('#btn-print-p').onclick = () => window.print();
  updHint();
}

/**
 * 估算填空题有几个空。
 * 依据：答案里的空数 > 题干下划线数 > 1
 * 没有答案时（原卷无答案）只能靠题干，取 1 保守处理。
 */
function countBlanks(answer, q) {
  const ans = String(answer || '');
  if (ans && !ans.includes('原卷无答案')) {
    const parts = ans.split(/[；;，,、｜|]+/).map(x => x.trim())
                     .filter(x => x !== '');
    if (parts.length > 1) return Math.min(parts.length, 4);
  }
  const stem = String((q && q.stem_text) || '');
  const m = stem.match(/_{2,}|＿+/g);
  if (m && m.length > 1) return Math.min(m.length, 4);
  return 1;
}

function updHint() {
  const n = S.questions.filter(q => S.answers[q.id]).length;
  const h = document.querySelector('#fill-hint');
  if (h) h.textContent = `已答 ${n} / ${S.questions.length}`;
}

async function submit() {
  const msg = document.querySelector('#prac-msg');
  const unanswered = S.questions.filter(q => !S.answers[q.id]);
  if (unanswered.length) {
    if (!confirm(`还有 ${unanswered.length} 题未作答，未作答按「错误」计。继续提交？`))
      return;
  }

  S.submitted = true;
  const results = [];
  const payload = [];

  for (const q of S.questions) {
    const given = S.answers[q.id] || '';
    let g;
    if (given === '__ok__') g = { correct: true, partial: false, score: q.score || 12,
                                   fullScore: q.score || 12, expect: q.answer || '',
                                   given: '自评：做对', needSelf: false };
    else if (given === '__no__') g = { correct: false, partial: false, score: 0,
                                        fullScore: q.score || 12, expect: q.answer || '',
                                        given: '自评：没做对', needSelf: false };
    else g = grade(q, given);

    S.results[q.id] = g;
    results.push(g);
    payload.push({ id: q.id, correct: !!g.correct, partial: !!g.partial });
  }

  // 在题目下方显示判分
  const pw = document.querySelector('#pw');
  for (const q of S.questions) {
    const qEl = pw.querySelector(`.q[data-id="${q.id}"]`);
    if (!qEl) continue;
    const g = S.results[q.id];
    // 标色
    if (!g.needSelf && q.type === '选择') {
      const expect = String(g.expect || '').toUpperCase();
      qEl.querySelectorAll('.opt.pick').forEach(el => {
        const v = (el.dataset.val || '').toUpperCase();
        el.classList.remove('sel');
        if (expect.includes(v)) el.classList.add('right');
        else if (el.classList.contains('sel')) el.classList.add('wrong');
      });
    }
    const box = document.createElement('div');
    box.className = 'answer-box show';
    const verdict = g.needSelf
      ? '<span style="color:#c8891a">需自评</span>'
      : (g.correct ? '<span style="color:#2e7d4f">✔ 正确</span>'
        : (g.partial ? '<span style="color:#c8891a">△ 部分正确</span>'
          : '<span style="color:#c0392b">✘ 错误</span>'));
    box.innerHTML =
      `<div>${verdict}　得分 <b>${g.score}</b> / ${g.fullScore}</div>`
      + `<div style="margin-top:4px;color:#5a6472">你的答案：${esc(g.given) || '（未答）'}`
      + `　正确答案：<b>${esc(g.expect)}</b></div>`
      + (q.ana_text ? `<div class="ana"><b>【解析】</b>${esc(q.ana_text)}</div>` : '');
    qEl.appendChild(box);
  }

  // 汇总
  const s = summarize(results);
  const sum = document.querySelector('#summary');
  sum.innerHTML = `
    <div class="card no-print">
      <h3>本次成绩</h3>
      <div class="stat-grid">
        <div class="stat"><div class="v">${s.got}</div><div class="k">得分 / ${s.full}</div></div>
        <div class="stat"><div class="v">${s.acc}%</div><div class="k">正确率</div></div>
        <div class="stat"><div class="v" style="color:#2e7d4f">${s.nRight}</div><div class="k">全对</div></div>
        <div class="stat"><div class="v" style="color:#c8891a">${s.nPartial}</div><div class="k">部分对</div></div>
        <div class="stat"><div class="v" style="color:#c0392b">${s.nWrong}</div><div class="k">错误</div></div>
        <div class="stat"><div class="v">${s.nSelf}</div><div class="k">待自评</div></div>
      </div>
    </div>`;

  // 写入练习记录（自动更新记忆曲线）
  try {
    const r = await api.progress(payload);
    msg.className = 'msg ok show';
    const dues = (r.records || []).filter(x => !x.done);
    msg.innerHTML =
      `已判分并写入练习记录。${dues.length} 道题进入复习排期，`
      + `最近一次复习在 ${dues.length ? dues[0].next : '-'}。`
      + (S.source === 'compose'
         ? `　<button id="btn-next-batch" class="ghost" style="margin-left:8px">`
           + `再练一组</button>` : '');
    const nb = document.querySelector('#btn-next-batch');
    if (nb) nb.onclick = () => { location.hash = '#/compose'; };
  } catch (e) {
    msg.className = 'msg err show';
    msg.textContent = '判分完成，但写入练习记录失败：' + e.message
      + '（请检查 Python 环境）';
  }

  document.querySelector('#btn-submit').disabled = true;
  document.querySelector('#btn-submit').textContent = '已提交';
}

function esc(s) {
  return String(s == null ? '' : s)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}
