/* ============================================================
   组卷视图 —— 按条件筛题并生成可打印试卷
   ============================================================ */
import { api, call } from '../app/api.js';
import { renderPaper, SLICE_BASE } from '../app/render.js';
import { setPending } from './practice.js';

let state = {
  subject: '数学',
  kp: new Set(),
  topics: new Set(),   // 题型标签（三级节点 ID，多对多）
  note: { l1: null, l2: null, topic: null },   // 右侧讲解面板当前指向
  types: new Set(),
  diffMin: 0.0,
  diffMax: 1.0,
  count: 12,
  seed: null,
  picked: [],
  kpStats: {},       // 已入库题目里出现过的知识点（按科目分组后取当前科）
  catalog: {},       // 六科完整标准目录
};

export async function mount(root) {
  root.innerHTML = `
    <h2 class="title">自动组卷</h2>
    <p class="sub">按知识点和难度筛题，生成可直接打印的高考版式试卷。
       筛选条件保存后，下次打开自动恢复。</p>

    <div class="card">
      <h3>筛选条件</h3>
      <div class="row" style="margin-bottom:10px">
        <label>科目</label>
        <select id="f-subject">
          <option>数学</option><option>物理</option>
          <option>化学</option><option>生物</option>
          <option>语文</option><option>英语</option>
        </select>
        <label style="min-width:auto">题数</label>
        <input type="number" id="f-count" value="12" min="1" max="60" style="width:74px">
        <label style="min-width:auto">随机种子</label>
        <input type="text" id="f-seed" placeholder="留空=每次不同" style="width:120px">
      </div>

      <div class="row" style="margin-bottom:8px">
        <label>题型</label>
        <span id="f-types"></span>
      </div>

      <div class="row" style="margin-bottom:8px">
        <label>难度</label>
        <span style="font-size:13px;color:#5a6472">
          系数 <b id="d-lo">0.00</b> ~ <b id="d-hi">1.00</b>
          （0=最难，1=最易）
        </span>
        <input type="range" id="f-dmin" min="0" max="1" step="0.05" value="0"
               style="width:130px">
        <input type="range" id="f-dmax" min="0" max="1" step="0.05" value="1"
               style="width:130px">
      </div>

      <div class="kp-layout">
        <div class="kp-left">
          <div class="row" style="align-items:flex-start">
            <label style="padding-top:4px">知识点</label>
            <div id="f-kp" class="grow" style="max-height:132px;overflow-y:auto">
              <span style="color:#9aa;font-size:12px">加载中…</span>
            </div>
          </div>
          <div class="row" style="align-items:flex-start;margin-top:8px">
            <label style="padding-top:4px"></label>
            <div id="topic-tree" class="grow"></div>
          </div>
        </div>
        <div class="kp-right">
          <div class="kp-note-h">
            <span>知识点讲解</span>
            <span id="kp-note-cov" class="muted sm"></span>
          </div>
          <div id="kp-note" class="kp-note-body">
            <span class="muted sm">点击左侧任意大知识点 / 小知识点 / 题型，
              这里显示对应的方法与要点。</span>
          </div>
        </div>
      </div>

      <div class="row" style="margin-top:14px">
        <button class="primary" id="btn-compose">生成试卷</button>
        <button id="btn-clear">清空条件</button>
        <button id="btn-print" disabled>打印 / 存 PDF</button>
        <span id="cand" style="font-size:12px;color:#5a6472"></span>
      </div>
    </div>

    <div id="compose-msg"></div>
    <div id="paper-out"></div>
  `;

  // ---- 事件绑定 ----
  const $ = (s) => root.querySelector(s);
  $('#f-subject').onchange = async (e) => {
    state.subject = e.target.value;
    // 必须清空：上一科选的知识点在下一科不存在，
    // 留着会作为过滤条件传下去，导致「明明有题却组不出卷」。
    state.kp.clear();
    state.types.clear();
    renderTypes();
    await loadKp();
  };
  $('#f-count').onchange = (e) => { state.count = +e.target.value || 12; };
  $('#f-seed').onchange = (e) => {
    const v = e.target.value.trim();
    state.seed = v === '' ? null : v;
  };
  $('#f-dmin').oninput = (e) => {
    state.diffMin = +e.target.value;
    if (state.diffMin > state.diffMax) {
      state.diffMax = state.diffMin; $('#f-dmax').value = state.diffMax;
    }
    $('#d-lo').textContent = state.diffMin.toFixed(2);
    $('#d-hi').textContent = state.diffMax.toFixed(2);
  };
  $('#f-dmax').oninput = (e) => {
    state.diffMax = +e.target.value;
    if (state.diffMax < state.diffMin) {
      state.diffMin = state.diffMax; $('#f-dmin').value = state.diffMin;
    }
    $('#d-hi').textContent = state.diffMax.toFixed(2);
  };
  $('#btn-clear').onclick = () => {
    state.kp.clear(); state.types.clear(); state.topics.clear();
  state.note = { l1: null, l2: null, topic: null };
    state.diffMin = 0; state.diffMax = 1;
    $('#f-dmin').value = 0; $('#f-dmax').value = 1;
    $('#d-lo').textContent = '0.00'; $('#d-hi').textContent = '1.00';
    renderTypes(); renderKp();
  };
  $('#btn-compose').onclick = doCompose;
  $('#btn-print').onclick = () => window.print();

  renderTypes();
  await loadKpCatalog();
  loadNoteStats();   // 先拿完整目录再渲染，否则目录为空
  await loadKp();
  restore();
}

function renderTypes() {
  const box = document.querySelector('#f-types');
  if (!box) return;
  box.innerHTML = ['选择', '填空', '解答'].map(t =>
    `<span class="chip${state.types.has(t) ? ' on' : ''}" data-t="${t}">${t}</span>`
  ).join('');
  box.querySelectorAll('.chip').forEach(c => {
    c.onclick = () => {
      const t = c.dataset.t;
      if (state.types.has(t)) state.types.delete(t); else state.types.add(t);
      c.classList.toggle('on');
    };
  });
}

async function loadKpCatalog() {
  try {
    const r = await call('py_kp_catalog', {});
    state.catalog = r.catalog || {};
  } catch (e) {
    state.catalog = {};
    try { console.warn('[compose] 知识点目录加载失败：' + e.message); } catch (_) {}
  }
}

async function loadKp() {
  const box = document.querySelector('#f-kp');
  try {
    // by_kp 已按科目分组；这里只取当前科目那一份。
    // 之前取的是全库统计，所以切到物理仍显示「解析几何」这类数学知识点。
    const st = await api.stats();
    const grouped = st.by_kp || {};
    state.kpStats = {};
    for (const [k, n] of (grouped[state.subject] || [])) state.kpStats[k] = n;
    renderKp();
  } catch (e) {
    if (box) box.innerHTML = `<span style="color:#c0392b">${e.message}</span>`;
  }
}

/**
 * 渲染知识点选择区。
 *
 * 展示当前科目的**完整标准目录**（不是只有已入库的那些），
 * 已入库的排在前面并标出题数，暂缺的排在后面灰显。
 *
 * 严格按科目过滤 —— 选物理绝不会出现「解析几何」。
 */
function renderKp() {
  const box = document.querySelector('#f-kp');
  if (!box) return;

  const sub = state.subject;
  const cat = (state.catalog && state.catalog[sub]) || [];
  const stats = state.kpStats || {};

  if (!cat.length) {
    box.innerHTML = '<span style="color:#9aa;font-size:12px">'
      + '该科暂无知识点目录</span>';
    return;
  }

  const withCount = cat.filter(x => stats[x.name] > 0)
    .sort((a, b) => stats[b.name] - stats[a.name]);
  const without = cat.filter(x => !stats[x.name]);

  const chip = (item, n) => {
    // children 是 [{name, topics}]，不能直接 join —— 会得到 [object Object]。
    // 二级名后面标题型数，一眼看出哪块内容厚。
    const tip = (item.children || []).map(c => {
      const t = (c.topics || []).length;
      return t ? `${c.name}(${t})` : c.name;
    }).join(' / ');
    return `<span class="chip${state.kp.has(item.name) ? ' on' : ''}"`
      + ` data-k="${item.name}"${tip ? ` title="${tip}"` : ''}>`
      + `${item.name}<span class="n"${n ? '' : ' style="opacity:.4"'}>${n}</span>`
      + `</span>`;
  };

  box.innerHTML =
    withCount.map(x => chip(x, stats[x.name])).join('')
    + without.map(x => chip(x, 0)).join('');

  box.querySelectorAll('.chip').forEach(c => {
    c.onclick = () => {
      const k = c.dataset.k;
      if (state.kp.has(k)) state.kp.delete(k); else state.kp.add(k);
      c.classList.toggle('on');
      // 选中就顺便把讲解定位到这一块；取消选中则回退到「未选」
      state.note = { l1: state.kp.has(k) ? k : null, l2: null, topic: null };
      renderTopics();
      loadNote();
    };
  });

  renderTopics();
}

/**
 * 三级题型浏览：选中的大知识点 → 小知识点 → 题型。
 *
 * 目录里的题型来自《2024 高中数学热点题型归纳》，是**备考清单**性质，
 * 与题库里的真题不是一一对应关系（题库只有 216 道真题）。
 * 它的用途是：选题时提醒「这块还有哪些考法没练到」。
 */
function renderTopics() {
  const host = document.querySelector('#topic-tree');
  if (!host) return;

  const cat = (state.catalog && state.catalog[state.subject]) || [];
  const picked = cat.filter(x => state.kp.has(x.name));

  if (!picked.length || !picked.some(x =>
        (x.children || []).some(c => (c.topics || []).length))) {
    host.innerHTML = '';
    return;
  }

  const blocks = picked.map(l1 => {
    const kids = (l1.children || []).filter(c => (c.topics || []).length);
    if (!kids.length) return '';
    const inner = kids.map(c => {
      // 题型是**节点**：有 ID、可挂多个题目、可跨多个大知识点。
      // 挂了题的显示题数并可点击筛选，没挂的灰显。
      const lis = c.topics.map((t, i) => {
        const nd = (c.nodes && c.nodes[i]) || {};
        const ow = (c.owners && c.owners[t]) || [];
        const cross = ow.length > 1
          ? ow.filter(x => x[0] !== l1.name).map(x => x[0]).join('+') : '';
        const nq = nd.n_qs || 0;
        const cls = nq ? 'tk on' : 'tk';
        const tip = nd.label || t;
        return `<i class="${cls}" data-tid="${esc(nd.id || '')}"`
             + ` data-nq="${nq}"`
             + ` title="${esc(tip)}${nq ? '（已挂 ' + nq + ' 题，点击加入筛选）'
                                          : '（暂无题目，点击查看讲解）'}">`
             + `${esc(t)}`
             + (cross ? `<b>↔${esc(cross)}</b>` : '')
             + (nq ? `<u>${nq}</u>` : '')
             + `</i>`;
      }).join('');
      return `<div class="tp-l2"><b class="tp-l2n" data-l1="${esc(l1.name)}"`
        + ` data-l2="${esc(c.name)}" title="查看「${esc(c.name)}」要点">`
        + `${esc(c.name)}</b>`
        + `<span class="tp-n">${c.topics.length}</span>`
        + `<div class="tp-l3">${lis}</div></div>`;
    }).join('');
    return `<div class="tp-l1"><div class="tp-h">${esc(l1.name)}</div>${inner}</div>`;
  }).join('');

  host.innerHTML =
    `<div class="topic-box"><div class="topic-h">题型清单`
    + `<span>（点击已挂题的题型可加入筛选）</span></div>${blocks}</div>`;

  // 二级标题：点击 -> 讲解面板切到该小知识点
  host.querySelectorAll('b.tp-l2n').forEach(el => {
    el.onclick = () => {
      state.note = { l1: el.dataset.l1, l2: el.dataset.l2, topic: null };
      loadNote();
    };
  });

  // 题型节点：点击 -> 讲解面板切到该题型
  // 没挂题的题型不能用来筛题，但**讲解对全部题型都有意义**，
  // 所以这里不区分 on/off，全部可点。
  host.querySelectorAll('i.tk[data-tid]').forEach(el => {
    el.onclick = () => {
      const tid = el.dataset.tid;
      if (!tid) return;
      const nq = Number(el.dataset.nq || 0);

      // 没挂题的题型：只能看讲解，不能拿去筛题。
      // 否则会被加进筛选条件，却一题都匹配不到，组出空卷。
      if (nq > 0) {
        if (state.topics.has(tid)) state.topics.delete(tid);
        else state.topics.add(tid);
        el.classList.toggle('sel');
      }

      const p = el.closest('.tp-l2')?.querySelector('b.tp-l2n');
      state.note = { l1: p?.dataset.l1 || null, l2: p?.dataset.l2 || null,
                     topic: tid };
      loadNote();
    };
  });
}

/**
 * 右侧讲解面板：按 state.note 指向的层级取内容。
 *
 * 层级优先：题型 > 小知识点 > 大知识点。
 * 没有内容时不报错，只提示可下钻 —— 目录覆盖 6 科，
 * 目前只有数学有教辅来源，其余科目为空属正常。
 */
async function loadNote() {
  const box = document.querySelector('#kp-note');
  if (!box) return;
  const { l1, l2, topic } = state.note;
  if (!l1 && !l2 && !topic) {
    box.innerHTML = '<span class="muted sm">点击左侧任意大知识点 / '
      + '小知识点 / 题型，这里显示对应的方法与要点。</span>';
    return;
  }
  box.innerHTML = '<span class="muted sm">加载中…</span>';
  try {
    const r = await api.kpNotes(state.subject, l1, l2, topic);
    renderNote(r);
  } catch (e) {
    box.innerHTML = '<span class="err sm">加载失败：' + esc(String(e)) + '</span>';
  }
}

function renderNote(r) {
  const box = document.querySelector('#kp-note');
  if (!box) return;

  const notes = r.notes || r.items || [];      // r.items 兼容旧格式
  const ex = r.example_list || [];
  const va = r.variant_list || [];

  if (!notes.length && !ex.length && !va.length) {
    box.innerHTML = `<div class="kp-note-t">${esc(r.title || '')}</div>`
      + '<div class="muted sm" style="margin-top:8px">这一层暂无内容。'
      + '<br>可逐级下钻查看；其他科目待补充教辅资料。</div>';
    return;
  }

  const lvName = { topic: '题型', l2: '小知识点', l1: '大知识点' }[r.level] || '';
  let html = `<div class="kp-note-t">${esc(r.title || '')}`
    + `<span class="kp-lv">${esc(lvName)}</span></div>`;

  html += notes.map(it =>
    `<div class="kp-blk"><div class="kp-kind">${esc(it.kind)}</div>`
    + `<div class="kp-txt">${esc(it.text)}</div></div>`).join('');

  html += qSection('典例分析', ex, 'ex');
  html += qSection('变式演练', va, 'va');

  box.innerHTML = html;
  bindQuestions(box);
}

/** 典例/变式区块：默认折叠，点标题展开摘要，点题目展开详解 */
function qSection(title, list, key) {
  if (!list || !list.length) return '';
  const rows = list.map(q => `
    <div class="rq" data-q="${esc(q.id)}">
      <div class="rq-h">
        <b>${esc(q.id.split('-').pop())}</b>
        <span class="rq-stem">${esc(collapse(q.stem))}</span>
        ${q.ans ? `<span class="rq-ans" title="答案">${esc(q.ans)}</span>` : ''}
      </div>
      <div class="rq-body" style="display:none"></div>
    </div>`).join('');
  return `<div class="kp-qs">
    <div class="kp-qh" data-key="${key}">${esc(title)}
      <span class="n">${list.length}</span><i>展开</i></div>
    <div class="kp-ql" data-key="${key}" style="display:none">${rows}</div>
  </div>`;
}

/** 题干折成一行：教辅 PDF 的公式被拆成多行，原样显示会很长 */
function collapse(s) {
  return String(s || '').replace(/\s*\n+\s*/g, ' ').trim().slice(0, 80);
}

function bindQuestions(box) {
  // 分组展开/收起
  box.querySelectorAll('.kp-qh').forEach(h => {
    h.onclick = () => {
      const k = h.dataset.key;
      const l = box.querySelector(`.kp-ql[data-key="${k}"]`);
      if (!l) return;
      const open = l.style.display !== 'none';
      l.style.display = open ? 'none' : '';
      h.querySelector('i').textContent = open ? '展开' : '收起';
    };
  });

  // 点题目 -> 异步加载详解
  box.querySelectorAll('.rq-h').forEach(h => {
    h.onclick = async () => {
      const row = h.closest('.rq');
      const body = row?.querySelector('.rq-body');
      if (!body) return;
      if (body.style.display !== 'none') { body.style.display = 'none'; return; }
      if (body.dataset.loaded) { body.style.display = ''; return; }
      body.innerHTML = '<span class="muted sm">加载中…</span>';
      body.style.display = '';
      try {
        const r = await api.refQuestions([row.dataset.q]);
        const v = (r.items || [])[0];
        body.dataset.loaded = '1';
        if (!v) { body.innerHTML = '<span class="err sm">未找到</span>'; return; }
        body.innerHTML =
          `<div class="rq-full">${esc(v.stem || '')}</div>`
          + ((v.opts || []).length
             ? `<div class="rq-opts">${v.opts.map((o, i) =>
                 `<div><b>${'ABCD'[i] || i + 1}.</b> ${esc(o)}</div>`).join('')}</div>`
             : '')
          + (v.analysis ? `<div class="rq-sec"><u>分析</u>${esc(v.analysis)}</div>` : '')
          + (v.solution ? `<div class="rq-sec"><u>详解</u>${esc(v.solution)}</div>` : '')
          + (v.ans ? `<div class="rq-sec"><u>答案</u>${esc(v.ans)}</div>` : '');
      } catch (e) {
        body.innerHTML = '<span class="err sm">加载失败：' + esc(String(e)) + '</span>';
      }
    };
  });
}

async function loadNoteStats() {
  const el = document.querySelector('#kp-note-cov');
  if (!el) return;
  try {
    const r = await api.kpNotesStats();
    const m = r.meta || {};
    const qs = (r.examples || 0) + (r.variants || 0);
    el.textContent = m.source
      ? `讲解 ${r.topic} · 例题 ${qs}`
      : '暂无讲解数据';
    el.title = m.source ? `${m.source}（${m.pages} 页）` : '';
  } catch (e) { el.textContent = ''; }
}

async function doCompose() {
  const btn = document.querySelector('#btn-compose');
  const msg = document.querySelector('#compose-msg');
  const out = document.querySelector('#paper-out');
  btn.disabled = true; btn.textContent = '生成中…';
  msg.className = 'msg'; out.innerHTML = '';

  try {
    const cfg = {
      subject: state.subject,
      types: [...state.types],
      kp: [...state.kp],
      topics: [...state.topics],
      diff_min: state.diffMin,
      diff_max: state.diffMax,
      count: state.count,
      seed: state.seed === null ? Date.now() % 100000 : state.seed,
    };
    save(cfg);
    const r = await api.compose(cfg);
    state.picked = r.items;

    if (!r.items.length) {
      msg.className = 'msg err show';
      msg.textContent = '没有符合条件的题目。'
        + '试试放宽难度区间，或减少知识点/题型的组合条件。';
      document.querySelector('#btn-print').disabled = true;
      return;
    }

    out.innerHTML =
      `<div class="card no-print" style="padding:10px 14px">
         <div class="row">
           <span style="font-size:13px;color:#5a6472">
             共 <b>${r.count}</b> 题（候选题池 ${r.candidates} 题）
           </span>
           <button id="btn-practice" class="primary">在线练习这份卷</button>
           <button id="btn-print2">打印 / 存为 PDF</button>
           <button id="btn-ans">显示答案</button>
           <button id="btn-save-html" title="导出为单个 HTML 文件，可直接双击打开、"
             + "发给家教或存档（图片已内嵌，无需联网）">导出 HTML 文件</button>
           <button id="btn-save-docx" title="导出为 Word 文档，公式可双击编辑，"
             + "适合老师改题、调分值、加批注">导出 Word（可编辑）</button>
         </div>
       </div>
       <div class="paper-wrap" id="pw"></div>`;

    const pw = document.querySelector('#pw');
    pw.innerHTML = renderPaper(r.items, {
      title: `${cfg.subject} · 自动组卷`,
      sub: `${new Date().toLocaleDateString('zh-CN')}　共 ${r.count} 题`,
      rows: [['科目', cfg.subject],
             ['题量', `${r.count} 题`],
             ['难度区间', `${cfg.diff_min.toFixed(2)} ~ ${cfg.diff_max.toFixed(2)}`]],
      baseUrl: SLICE_BASE,
    });
    document.querySelector('#btn-print2').onclick = () => window.print();
    document.querySelector('#btn-practice').onclick = () => {
      setPending(r.items, 'compose');
      location.hash = '#/practice';
    };
    document.querySelector('#btn-save-html').onclick = () => saveHtml(r.items, cfg);
    document.querySelector('#btn-save-docx').onclick = () => saveDocx(r.items, cfg);
    const ba = document.querySelector('#btn-ans');
    let shown = false;
    ba.onclick = () => {
      shown = !shown;
      ba.textContent = shown ? '隐藏答案' : '显示答案';
      pw.innerHTML = renderPaper(r.items, {
        title: `${cfg.subject} · 自动组卷`,
        sub: `${new Date().toLocaleDateString('zh-CN')}　共 ${r.count} 题`,
        rows: [['科目', cfg.subject], ['题量', `${r.count} 题`]],
        baseUrl: SLICE_BASE,
      });
      if (shown) {
        pw.querySelectorAll('.q').forEach(el => {
          const id = el.dataset.id;
          const q = r.items.find(x => x.id === id);
          if (!q) return;
          const ans = q.answer && !String(q.answer).includes('原卷无答案')
            ? q.answer : '<span style="color:#999">（原卷无答案）</span>';
          const ana = q.ana_text || '';
          const d = document.createElement('div');
          d.className = 'answer-box show';
          d.innerHTML = `<b>【答案】</b>${ans}`
            + (ana ? `<div class="ana"><b>【解析】</b>${ana}</div>` : '');
          el.appendChild(d);
        });
      }
    };
    document.querySelector('#btn-print').disabled = false;
    msg.className = 'msg ok show';
    msg.textContent = `已生成 ${r.count} 题试卷。打印时纸张选 A4、边距「默认」。`;
  } catch (e) {
    msg.className = 'msg err show';
    msg.textContent = '生成失败：' + e.message;
  } finally {
    btn.disabled = false; btn.textContent = '生成试卷';
  }
}

/**
 * 导出单文件 HTML。
 * 与「打印」的区别：打印只在本地出纸，导出的 HTML 可以
 *   - 发给家教 / 同学
 *   - 存档留底
 *   - 在没有装本应用的电脑上打开
 * 图片以 base64 内嵌，离线可用。
 */
async function saveHtml(items, cfg) {
  const btn = document.querySelector('#btn-save-html');
  const msg = document.querySelector('#compose-msg');
  if (!btn) return;
  btn.disabled = true;
  btn.textContent = '导出中…';
  try {
    let outdir = await pickDirectory();

    if (!outdir) {
      outdir = prompt('保存到哪个目录？（填绝对路径，留空则用默认下载目录）',
                      '');
      if (outdir === null) return;          // 用户取消
      if (outdir.trim() === '') outdir = 'out';
    }
    const r = await api.exportHtml(
      items.map(q => q.id), outdir,
      `${cfg.subject}_${new Date().toISOString().slice(0, 10)}_${items.length}题`);
    msg.className = 'msg ok show';
    msg.textContent = `已导出 ${r.count} 题 → ${r.path}`;
  } catch (e) {
    msg.className = 'msg err show';
    msg.textContent = '导出失败：' + e.message;
  } finally {
    btn.disabled = false;
    btn.textContent = '导出 HTML 文件';
  }
}

/**
 * 导出 Word。
 * 与 HTML 的区别：HTML 适合直接打印与分发，
 * Word 适合老师二次编辑 —— 公式是原生 OMML，双击即可修改。
 */
async function saveDocx(items, cfg) {
  const btn = document.querySelector('#btn-save-docx');
  const msg = document.querySelector('#compose-msg');
  if (!btn) return;
  btn.disabled = true;
  btn.textContent = '导出中…';
  try {
    let outdir = await pickDirectory();
    if (!outdir) {
      outdir = prompt('保存到哪个目录？（填绝对路径，留空则用默认下载目录）', '');
      if (outdir === null) return;
      if (outdir.trim() === '') outdir = 'out';
    }
    const r = await api.exportDocx(
      items.map(q => q.id), outdir,
      `${cfg.subject}_${new Date().toISOString().slice(0, 10)}_${items.length}题`);
    msg.className = 'msg ok show';
    msg.textContent = `已导出 Word ${r.count} 题 → ${r.path}`;
  } catch (e) {
    msg.className = 'msg err show';
    msg.textContent = '导出失败：' + e.message;
  } finally {
    btn.disabled = false;
    btn.textContent = '导出 Word（可编辑）';
  }
}

function save(cfg) {
  try { localStorage.setItem('compose.cfg', JSON.stringify(cfg)); } catch (e) {}
}
function restore() {
  try {
    const s = localStorage.getItem('compose.cfg');
    if (!s) return;
    const c = JSON.parse(s);
    state.subject = c.subject || state.subject;
    state.count = c.count || state.count;
    state.diffMin = c.diff_min ?? 0;
    state.diffMax = c.diff_max ?? 1;
    (c.kp || []).forEach(k => state.kp.add(k));
    (c.types || []).forEach(t => state.types.add(t));
    const $ = (s2) => document.querySelector(s2);
    $('#f-subject').value = state.subject;
    $('#f-count').value = state.count;
    $('#f-dmin').value = state.diffMin;
    $('#f-dmax').value = state.diffMax;
    $('#d-lo').textContent = state.diffMin.toFixed(2);
    $('#d-hi').textContent = state.diffMax.toFixed(2);
    renderTypes();
    renderKp();
  } catch (e) {}
}
