/* ============================================================
   组卷视图 —— 按条件筛题并生成可打印试卷
   ============================================================ */
import { api, call } from '../app/api.js';
import { renderPaper, SLICE_BASE } from '../app/render.js';
import { setPending } from './practice.js';

let state = {
  subject: '数学',
  kp: new Set(),      // 一级（大知识点）名
  kp2: new Set(),     // 二级（小知识点）名
  topics: new Set(),  // 题型标签（三级节点 ID，多对多）
  note: { l1: null, l2: null, topic: null },   // 右侧讲解面板当前指向
  // 三列联动的当前焦点：决定「小知识点」「题型」两列显示谁的内容。
  // 与「选中」是两件事 —— 选中是筛选条件，焦点只是浏览位置，
  // 所以可以点开看完再决定要不要勾。
  focus: { l1: null, l2: null },
  types: new Set(),
  grades: new Set(),   // 年级（派生字段，见 py/grade_map.py）
  gradeStat: {},       // {年级id: 题数}，来自 stats.by_grade_sub
  gradeList: [],       // 未隐藏的年级配置 [{id,name,...}]
  diffMin: 0.0,
  diffMax: 1.0,
  count: 12,
  seed: null,
  picked: [],
  kpStats: {},       // 一级题数：{一级名: n}
  kp2Stats: {},      // 二级题数：{"一级名>二级名": n}
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
        <label>年级</label>
        <span id="f-grades" class="grow"></span>
        <span class="kp-hint" id="grade-tip"></span>
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
          <div class="row" style="align-items:flex-start;margin-bottom:6px">
            <label style="padding-top:2px">知识点</label>
            <span class="kp-hint">点开大知识点 → 选小知识点 → 挑题型；
              三级都能勾，勾中的才参与组卷。</span>
          </div>
          <div class="kp-cols">
            <div class="kp-col">
              <div class="kp-col-h">大知识点
                <span class="kp-col-tip">可多选</span></div>
              <div id="f-kp" class="kp-col-b">
                <span style="color:#9aa;font-size:12px">加载中…</span></div>
            </div>
            <div class="kp-col">
              <div class="kp-col-h">小知识点
                <span id="l2-src" class="kp-col-tip"></span></div>
              <div id="f-kp2" class="kp-col-b"></div>
            </div>
            <div class="kp-col">
              <div class="kp-col-h">题型
                <span id="l3-src" class="kp-col-tip"></span></div>
              <div id="f-topic" class="kp-col-b"></div>
            </div>
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
    state.kp2.clear();
    state.types.clear();
    state.grades.clear();
    state.focus = { l1: null, l2: null };
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
    state.kp.clear(); state.kp2.clear();
    state.types.clear(); state.topics.clear();
    state.grades.clear();
    state.note = { l1: null, l2: null, topic: null };
    state.focus = { l1: null, l2: null };
    state.diffMin = 0; state.diffMax = 1;
    $('#f-dmin').value = 0; $('#f-dmax').value = 1;
    $('#d-lo').textContent = '0.00'; $('#d-hi').textContent = '1.00';
    renderTypes(); renderKp(); renderKp2(); renderTopicCol();
    renderGrades(); loadNote();
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

    // 二级题数只能从 kp_tree 拿：by_kp 只统计到一级。
    // 老后端没有这个字段时留空 —— 只是题数显示为 0，不影响点选。
    state.kp2Stats = {};
    const tree = (st.kp_tree || {})[state.subject] || [];
    for (const l1 of tree) {
      for (const l2 of (l1.children || [])) {
        state.kp2Stats[l1.name + '>' + l2.name] = l2.n || 0;
      }
    }

    // 年级是派生字段，按科目分别统计（by_grade_sub），key 是**年级 id**。
    // 显示名要从 st.grades 配置里取 —— 直接把 id 打到界面上会显示成 s1 / s2。
    const per = st.by_grade_sub || {};
    state.gradeStat = per[state.subject] || {};
    // 只显示未隐藏的：隐藏的意义就是「这个年级暂时用不上」
    state.gradeList = (st.grades || []).filter(g => !g.hidden);

    renderKp(); renderKp2(); renderTopicCol(); renderGrades();
  } catch (e) {
    if (box) box.innerHTML = `<span style="color:#c0392b">${e.message}</span>`;
  }
}

/**
 * 年级筛选。
 *
 * 年级是**推断**出来的（按知识点映射），不是录入数据，
 * 所以每个选项都标出题数，并把来源写在旁边 ——
 * 用户看到「高二 181」这种数字时，得知道它是算出来的。
 */
function renderGrades() {
  const box = document.querySelector('#f-grades');
  const tip = document.querySelector('#grade-tip');
  if (!box) return;

  const stat = state.gradeStat || {};
  // 用配置里的年级列表（含显示名），而不是统计结果的 key ——
  // 统计 key 是 id（s1/s2），直接显示用户看不懂。
  const grades = state.gradeList || [];
  if (!grades.length) {
    // 没有年级数据就把整行藏起来，留个空行会让人以为是加载失败
    box.innerHTML = '';
    const row = box.closest('.row');
    if (row) row.style.display = 'none';
    return;
  }
  const row0 = box.closest('.row');
  if (row0) row0.style.display = '';

  // 有题的排前面，没题的沉底灰显（与知识点列一致的处理）
  const sorted = grades.slice().sort((a, b) =>
    (stat[b.id] || 0) - (stat[a.id] || 0));

  box.innerHTML = sorted.map(g => {
    const n = stat[g.id] || 0;
    return `<span class="chip${state.grades.has(g.id) ? ' on' : ''}"`
      + ` data-g="${esc(g.id)}" title="${esc(g.name)}：${n} 题">`
      + `${esc(g.name)}<span class="n"${n ? '' : ' style="opacity:.4"'}>${n}</span></span>`;
  }).join('');

  if (tip) tip.textContent = '年级按知识点推断，不是原始录入数据';

  box.querySelectorAll('.chip[data-g]').forEach(c => {
    c.onclick = () => {
      const g = c.dataset.g;
      if (state.grades.has(g)) state.grades.delete(g); else state.grades.add(g);
      c.classList.toggle('on');
    };
  });
}

/** 当前科目的一级目录项（可能含未入库的） */
function catL1() {
  return (state.catalog && state.catalog[state.subject]) || [];
}

/** 按名字取一级目录项 */
function findL1(name) {
  return catL1().find(x => x.name === name) || null;
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

  const cat = catL1();
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
    // 悬停时列出小知识点，一眼看出哪块内容厚。
    const tip = (item.children || []).map(c => {
      const t = (c.topics || []).length;
      return t ? `${c.name}(${t})` : c.name;
    }).join(' / ');
    const on = state.kp.has(item.name);
    const cur = state.focus.l1 === item.name;
    return `<span class="chip${on ? ' on' : ''}${cur ? ' cur' : ''}"`
      + ` data-k="${esc(item.name)}"${tip ? ` title="${esc(tip)}"` : ''}>`
      + `${esc(item.name)}<span class="n"${n ? '' : ' style="opacity:.4"'}>${n}</span>`
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

      // 焦点跟着最后一次点的走；取消选中就退回任意一个还选着的。
      // 焦点决定右边两列显示什么，跟「是否已勾选」解耦，
      // 这样能先点开看内容、再决定勾不勾。
      if (state.kp.has(k)) state.focus.l1 = k;
      else if (state.focus.l1 === k) state.focus.l1 = [...state.kp][0] || null;
      state.focus.l2 = null;

      renderKp();                 // 刷新 .cur 高亮
      renderKp2(); renderTopicCol();
      state.note = { l1: state.kp.has(k) ? k : null, l2: null, topic: null };
      loadNote();
    };
  });
}

/**
 * 第二列：小知识点（二级）。
 *
 * 之前这一层只是题型清单里的小标题，既不能勾、也没有题数，
 * 于是「按小知识点组卷」根本无从下手 —— 只能整块大知识点地选。
 */
function renderKp2() {
  const box = document.querySelector('#f-kp2');
  const src = document.querySelector('#l2-src');
  if (!box) return;

  // 勾了多个大知识点时，把它们的小知识点**全列出来**（按大知识点分组）。
  // 只看最后点开的那个会让人以为另一个大知识点没内容。
  // 只勾一个、或还没勾时跟随焦点 —— 焦点的意义就是「先点开看看再决定勾不勾」。
  const picked = [...state.kp];
  const names = picked.length > 1 ? picked
    : (state.focus.l1 ? [state.focus.l1] : picked);

  if (!names.length) {
    box.innerHTML = '<span class="kp-empty">先在左边点开一个大知识点</span>';
    if (src) src.textContent = '';
    return;
  }

  const groups = names.map(n => ({ name: n, item: findL1(n) }))
    .filter(g => g.item);

  if (!groups.length) {
    box.innerHTML = '<span class="kp-empty">该大知识点下暂无小知识点</span>';
    if (src) src.textContent = '';
    return;
  }

  if (src) {
    src.textContent = groups.length === 1
      ? groups[0].name
      : `来自 ${groups.length} 个大知识点`;
  }

  const chip = (l1Name, c) => {
    const n = state.kp2Stats[l1Name + '>' + c.name] || 0;
    const nt = (c.topics || []).length;
    const on = state.kp2.has(c.name);
    const cur = state.focus.l2 === c.name;
    return `<span class="chip${on ? ' on' : ''}${cur ? ' cur' : ''}"`
      + ` data-l1="${esc(l1Name)}" data-k2="${esc(c.name)}"`
      + ` title="${esc(c.name)}：${nt} 个题型${n ? '，已入库 ' + n + ' 题' : '，暂无题目'}">`
      + `${esc(c.name)}<span class="n"${n ? '' : ' style="opacity:.4"'}>${n}</span>`
      + `</span>`;
  };

  // 多个大知识点时分组显示，否则平铺 —— 一级名字已经写在列头了
  box.innerHTML = groups.map(g => {
    const kids = g.item.children || [];
    if (!kids.length) return '';
    const inner = kids.map(c => chip(g.name, c)).join('');
    if (groups.length === 1) return inner;
    return `<div class="kp-gh">${esc(g.name)}</div><div class="kp-gg">${inner}</div>`;
  }).join('') || '<span class="kp-empty">该大知识点下暂无小知识点</span>';

  box.querySelectorAll('.chip[data-k2]').forEach(c => {
    c.onclick = () => {
      const k2 = c.dataset.k2;
      const l1 = c.dataset.l1;
      if (state.kp2.has(k2)) state.kp2.delete(k2); else state.kp2.add(k2);
      c.classList.toggle('on');

      state.focus.l1 = l1;
      if (state.kp2.has(k2)) state.focus.l2 = k2;
      else if (state.focus.l2 === k2) {
        state.focus.l2 = [...state.kp2][0] || null;
      }

      renderKp2(); renderTopicCol();
      state.note = { l1, l2: state.kp2.has(k2) ? k2 : null, topic: null };
      loadNote();
    };
  });
}

/**
 * 第三列：题型（三级节点）。
 *
 * 数据源优先取当前焦点的小知识点；
 * 没勾二级时，退化为「已选大知识点下的全部题型」，
 * 否则用户不勾二级就一列空白，会以为题型加载失败。
 */
function renderTopicCol() {
  const box = document.querySelector('#f-topic');
  const src = document.querySelector('#l3-src');
  if (!box) return;

  const rows = [];   // {tid, name, nq, l1, l2, cross}
  const push = (l1Name, l2, nd, tname) => {
    rows.push({
      tid: nd ? nd.id : '', name: tname,
      nq: nd ? (nd.n_qs || 0) : 0,
      l1: l1Name, l2: l2.name,
      cross: (nd && nd.cross || []).filter(x => x !== l1Name),
    });
  };

  const collect = (l1Name, onlyL2) => {
    const item = findL1(l1Name);
    if (!item) return;
    for (const c of (item.children || [])) {
      if (onlyL2 && c.name !== onlyL2) continue;
      (c.topics || []).forEach((t, i) => {
        const nd = (c.nodes && c.nodes[i]) || null;
        push(l1Name, c, nd, t);
      });
    }
  };

  // 与二级列同样的口径：多选了大知识点就把它们的题型合起来，
  // 只有一个 / 还没勾时跟着焦点走。
  const l1s = state.kp.size > 1 ? [...state.kp]
    : (state.focus.l1 ? [state.focus.l1] : [...state.kp]);

  if (state.focus.l2 && state.focus.l1) {
    collect(state.focus.l1, state.focus.l2);
  } else {
    for (const n of l1s) collect(n, null);
  }

  if (src) {
    src.textContent = state.focus.l2 ? state.focus.l2
      : (state.focus.l1 && state.kp.size < 2
          ? state.focus.l1 + ' · 全部题型'
          : (state.kp.size > 1 ? `已选 ${state.kp.size} 个大知识点 · 全部题型` : ''));
  }

  if (!rows.length) {
    box.innerHTML = state.focus.l1 || state.kp.size
      ? '<span class="kp-empty">这一层暂无题型</span>'
      : '<span class="kp-empty">先在左边点开大知识点</span>';
    return;
  }

  // 已挂题的排前面：能筛的优先，灰的沉底
  rows.sort((a, b) => (b.nq - a.nq) || a.name.localeCompare(b.name, 'zh'));

  box.innerHTML = rows.map(r => {
    const sel = r.tid && state.topics.has(r.tid);
    const cur = r.tid && state.note.topic === r.tid;
    const showL2 = !state.focus.l2 && rows.some(x => x.l2 !== r.l2);
    return `<span class="chip tk${r.nq ? ' has' : ''}${sel ? ' on' : ''}${cur ? ' cur' : ''}"`
      + ` data-tid="${esc(r.tid)}" data-nq="${r.nq}"`
      + ` data-l1="${esc(r.l1)}" data-l2="${esc(r.l2)}"`
      + ` data-name="${esc(r.name)}"`
      + ` title="${esc(r.name)}${r.nq ? '（已挂 ' + r.nq + ' 题，点击加入筛选）'
                                      : '（暂无题目，只能查看讲解）'}">`
      + (showL2 ? `<i>${esc(r.l2)} · </i>` : '')
      + `${esc(r.name)}`
      + (r.cross.length ? `<b>↔${esc(r.cross.join('+'))}</b>` : '')
      + (r.nq ? `<span class="n">${r.nq}</span>` : '')
      + `</span>`;
  }).join('');

  box.querySelectorAll('.chip[data-tid]').forEach(c => {
    c.onclick = () => {
      const tid = c.dataset.tid;
      const nq = Number(c.dataset.nq || 0);

      // 没挂题的题型勾了也匹配不到题目，只会组出空卷，
      // 但仍然可以点开看讲解。
      if (tid && nq > 0) {
        if (state.topics.has(tid)) state.topics.delete(tid);
        else state.topics.add(tid);
        c.classList.toggle('on');
      }

      state.note = { l1: c.dataset.l1 || null, l2: c.dataset.l2 || null,
                     topic: tid || null };
      renderTopicCol();
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
      kp2: [...state.kp2],
      grades: [...state.grades],
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
    (c.kp2 || []).forEach(k => state.kp2.add(k));
    (c.types || []).forEach(t => state.types.add(t));
    (c.grades || []).forEach(g => state.grades.add(g));
    // 恢复焦点：右侧两列才有内容，否则恢复后看着像没恢复
    state.focus = { l1: [...state.kp][0] || null, l2: [...state.kp2][0] || null };
    // 讲解面板跟着落到恢复出来的那一块，否则左侧有勾选、右侧还是空提示
    state.note = { l1: state.focus.l1, l2: state.focus.l2, topic: null };
    const $ = (s2) => document.querySelector(s2);
    $('#f-subject').value = state.subject;
    $('#f-count').value = state.count;
    $('#f-dmin').value = state.diffMin;
    $('#f-dmax').value = state.diffMax;
    $('#d-lo').textContent = state.diffMin.toFixed(2);
    $('#d-hi').textContent = state.diffMax.toFixed(2);
    renderTypes();
    // 年级统计要等 loadKp() 拉完 stats 才有，这里渲染不出内容也没关系：
    // 它会在 loadKp 里再渲染一次。提前渲染是为了恢复出勾选高亮。
    renderGrades();
    renderKp(); renderKp2(); renderTopicCol(); loadNote();
  } catch (e) {}
}

/**
 * HTML 转义。
 *
 * 这个文件里到处在用 esc()，但**从来没有定义过** ——
 * 一调用就抛 ReferenceError。后果不是报错弹窗，而是：
 *   - renderTopics() 抛错 → 题型 / 小知识点那一整块渲染中断
 *   - renderNote() 抛错 → 讲解面板永远显示「加载失败」
 * 所以页面看着是「小知识点看不见」，其实是渲染函数第一行就炸了。
 *
 * 另外必须转义引号：这些串要塞进 title="..." / data-x="..." 属性里，
 * 只转义尖括号的话，遇到含双引号的题型名会把属性提前闭合。
 */
function esc(s) {
  return String(s == null ? '' : s)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
}
