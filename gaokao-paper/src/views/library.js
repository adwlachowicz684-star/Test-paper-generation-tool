/* ============================================================
   题库视图 —— 浏览、搜索、导入 PDF、同步 Excel、拆题入库
   ============================================================ */
import { api, pickOpenFile } from '../app/api.js';
import { renderQuestion, SLICE_BASE } from '../app/render.js';
import { setPending } from './practice.js';

const baseUrl = SLICE_BASE;

let S = { all: [], filtered: [], page: 0, size: 20, kw: '', subject: '',
          kp: '', batch: '',
          sel: new Set() };

export async function mount(root) {
  root.innerHTML = `
    <h2 class="title">题库</h2>
    <p class="sub">浏览已入库题目，导入新试卷，同步 Excel 里人工校订的知识点与难度。</p>
    <div id="lib-msg"></div>

    <div class="card">
      <h3>概览</h3>
      <div class="stat-grid" id="lib-stats">加载中…</div>
    </div>

    <div class="card">
      <h3>管理</h3>
      <div class="row">
        <button id="btn-import">导入 PDF 拆题</button>
        <button id="btn-sync">从 Excel 同步标签</button>
        <button id="btn-backup">备份练习记录</button>
        <button id="btn-refresh">刷新</button>
        <span id="paths" style="font-size:11px;color:#9aa"></span>
      </div>
      <div class="row" style="margin-top:10px;display:none" id="sel-bar">
        <span style="font-size:13px;color:#5a6472">
          已选 <b id="sel-count">0</b> 题
        </span>
        <button class="primary" id="btn-practice-sel">练习选中题目</button>
        <button id="btn-clear-sel">取消选择</button>
      </div>
      <p style="font-size:12px;color:#5a6472;margin:10px 0 0">
        导入要求：<b>文字版 PDF</b>（浏览器里能选中文字的那种）。
        扫描件和拍照件无法处理 —— 化学式、结构式 OCR 后必然出错。
      </p>
    </div>

    <div class="card">
      <h3>批次管理</h3>
      <p style="font-size:12px;color:#5a6472;margin:0 0 10px">
        每次导入的题目自动归为一个批次。可按批次筛选，
        或把某批整体删除（会连带清理该批的练习记录）。
      </p>
      <div id="batch-box" style="font-size:13px">加载中…</div>
    </div>

    <div class="card">
      <h3>浏览</h3>
      <div class="row" style="margin-bottom:12px">
        <select id="l-subject" style="width:100px">
          <option value="">全部科目</option>
          <option>数学</option><option>物理</option>
          <option>化学</option><option>生物</option>
          <option>语文</option><option>英语</option>
        </select>
        <select id="l-kp" style="width:150px">
          <option value="">全部知识点</option>
        </select>
        <select id="l-batch" style="width:190px">
          <option value="">全部批次</option>
        </select>
        <input type="text" id="l-kw" class="grow" placeholder="搜索题干 / 知识点 / 题目ID">
        <button id="l-search">搜索</button>
      </div>
      <table class="grid">
        <thead><tr>
          <th style="width:34px"><input type="checkbox" id="sel-all"></th>
          <th style="width:96px">题目ID</th>
          <th style="width:52px">科目</th>
          <th style="width:52px">题型</th>
          <th style="width:60px">难度</th>
          <th>题干</th>
          <th style="width:150px">知识点</th>
        </tr></thead>
        <tbody id="l-tbody"></tbody>
      </table>
      <div class="row" style="margin-top:12px;justify-content:center">
        <button id="l-prev">上一页</button>
        <span id="l-page" style="font-size:13px;color:#5a6472"></span>
        <button id="l-next">下一页</button>
      </div>
    </div>

    <div id="l-detail"></div>
  `;

  const $ = (s) => root.querySelector(s);
  $('#btn-refresh').onclick = load;
  await loadKpOptions();
  await loadBatchOptions();
  $('#l-search').onclick = applyFilter;
  $('#l-kw').onkeydown = (e) => { if (e.key === 'Enter') applyFilter(); };
  $('#l-subject').onchange = async () => { await loadKpOptions(); applyFilter(); };
  $('#l-kp').onchange = applyFilter;
  $('#l-batch').onchange = applyFilter;
  $('#l-prev').onclick = () => { if (S.page > 0) { S.page--; renderTable(); } };
  $('#l-next').onclick = () => {
    if ((S.page + 1) * S.size < S.filtered.length) { S.page++; renderTable(); }
  };
  $('#btn-import').onclick = importPdf;
  $('#sel-all').onchange = (e) => {
    const items = S.filtered.slice(S.page * S.size, (S.page + 1) * S.size);
    if (e.target.checked) items.forEach(q => S.sel.add(q.id));
    else items.forEach(q => S.sel.delete(q.id));
    renderTable(); updSelBar();
  };
  $('#btn-clear-sel').onclick = () => { S.sel.clear(); renderTable(); updSelBar(); };
  $('#btn-practice-sel').onclick = () => {
    const qs = S.all.filter(q => S.sel.has(q.id));
    if (!qs.length) return;
    setPending(qs, 'library');
    location.hash = '#/practice';
  };
  $('#btn-sync').onclick = syncExcel;
  $('#btn-backup').onclick = backup;

  try {
    const p = await api.paths();
    $('#paths').textContent = `数据目录：${p.data_dir}`;
  } catch (e) {}

  await load();
}

async function load() {
  const msg = document.querySelector('#lib-msg');
  try {
    const st = await api.stats();
    const box = document.querySelector('#lib-stats');
    box.innerHTML = [
      ['题目总数', st.total],
      ['数学', st.by_subject['数学'] || 0],
      ['物理', st.by_subject['物理'] || 0],
      ['选择', st.by_type['选择'] || 0],
      ['填空', st.by_type['填空'] || 0],
      ['解答', st.by_type['解答'] || 0],
    ].map(([k, v]) => `<div class="stat"><div class="v">${v}</div>`
      + `<div class="k">${k}</div></div>`).join('');
    const lv = st.by_level || {};
    box.innerHTML += ['容易', '适中', '较难', '困难'].map(k =>
      `<div class="stat"><div class="v lv-${k}">${lv[k] || 0}</div>`
      + `<div class="k">${k}</div></div>`).join('');

    const r = await api.list({ limit: 10000 });
    S.all = r.items || [];
    applyFilter();
    msg.className = 'msg';
  } catch (e) {
    msg.className = 'msg err show';
    msg.textContent = '加载题库失败：' + e.message;
  }
}

/**
 * 知识点下拉跟随科目联动。
 * 之前题库页的科目下拉只有四科且与知识点无联动，
 * 切到「物理」后知识点选项里仍混着数学词汇。
 */
let _catalog = {};

async function loadKpOptions() {
  try {
    if (!Object.keys(_catalog).length) {
      const r = await api.kpCatalog();
      _catalog = r.catalog || {};
    }
    const sel = document.querySelector('#l-kp');
    if (!sel) return;
    const subj = document.querySelector('#l-subject')?.value || '';
    const keep = sel.value;
    const list = subj ? ((_catalog[subj] || []).map(x => x.name)) : [];
    sel.innerHTML = '<option value="">全部知识点</option>'
      + list.map(k => `<option${k === keep ? ' selected' : ''}>${k}</option>`).join('');
    sel.disabled = !subj;
    sel.title = subj ? '' : '先选科目，再按知识点筛选';
  } catch (e) {
    try { console.warn('[library] 知识点目录加载失败：' + e.message); } catch (_) {}
  }
}

function applyFilter() {
  S.subject = document.querySelector('#l-subject').value;
  S.kp = document.querySelector('#l-kp')?.value || '';
  S.kw = document.querySelector('#l-kw').value.trim();
  S.batch = document.querySelector('#l-batch')?.value || '';
  S.page = 0;
  S.filtered = S.all.filter(q => {
    if (S.subject && q.subject !== S.subject) return false;
    if (S.kp && !(q.kp_list || []).includes(S.kp)) return false;
    // 批次筛选：未标记的题归到「未标记」，
    // 否则早期导入又没打标的题会在这个筛选下凭空消失
    if (S.batch) {
      const b = q.batch || '未标记';
      if (b !== S.batch) return false;
    }
    if (!S.kw) return true;
    const hay = (q.stem_text || '') + ' ' + (q.kp || '') + ' ' + q.id
      + ' ' + (q.src || '');
    return hay.toLowerCase().includes(S.kw.toLowerCase());
  });
  renderTable();
}

const SUBJ_NAME = { M: '数学', P: '物理', C: '化学', B: '生物',
                    Y: '语文', E: '英语' };

async function loadBatchOptions() {
  const sel = document.querySelector('#l-batch');
  const box = document.querySelector('#batch-box');
  if (!sel) return;
  let items = [];
  try {
    const r = await api.batchList();
    items = r.items || [];
  } catch (e) {
    if (box) box.innerHTML = '<span class="err">批次加载失败：' + esc(String(e)) + '</span>';
    return;
  }
  const keep = S.batch;
  sel.innerHTML = '<option value="">全部批次</option>' + items.map(b =>
    `<option value="${esc(b.id)}">${esc(b.name)}（${b.count}）</option>`
  ).join('');
  sel.value = items.some(b => b.id === keep) ? keep : '';
  S.batch = sel.value;
  renderBatchBox(items);
}

function renderBatchBox(items) {
  const box = document.querySelector('#batch-box');
  if (!box) return;
  if (!items.length) {
    box.innerHTML = '<span class="muted">暂无批次</span>';
    return;
  }
  box.innerHTML = `
    <table style="width:100%;border-collapse:collapse">
      <thead><tr style="text-align:left;color:#8a94a6;font-size:12px">
        <th style="padding:4px 6px">批次</th>
        <th style="padding:4px 6px">导入时间</th>
        <th style="padding:4px 6px">来源</th>
        <th style="padding:4px 6px">题数</th>
        <th style="padding:4px 6px"></th>
      </tr></thead>
      <tbody>${items.map(b => {
        const subs = Object.entries(b.by_subject || {})
          .map(([k, v]) => (SUBJ_NAME[k] || k) + v).join(' ');
        return `<tr style="border-top:1px solid #eef1f6">
          <td style="padding:6px"><b>${esc(b.name)}</b>
            <div class="muted sm">${esc(b.id)}</div></td>
          <td style="padding:6px" class="muted sm">${esc(b.time || '—')}</td>
          <td style="padding:6px" class="muted sm">${esc(b.src || '—')}</td>
          <td style="padding:6px">${b.count}
            <span class="muted sm">${esc(subs)}</span></td>
          <td style="padding:6px;text-align:right">
            <button class="danger sm" data-del="${esc(b.id)}"
              data-name="${esc(b.name)}" ${b.count ? '' : 'disabled'}>删除整批</button>
          </td></tr>`;
      }).join('')}</tbody>
    </table>`;

  box.querySelectorAll('button[data-del]').forEach(btn => {
    btn.onclick = async () => {
      const bid = btn.dataset.del, nm = btn.dataset.name;
      if (!confirm(`确定删除批次「${nm}」下的全部题目？\n\n`
        + `该批的练习记录会一并清理。此操作不可撤销，建议先备份。`)) return;
      btn.disabled = true; btn.textContent = '删除中…';
      try {
        const r = await api.batchDelete(bid);
        await load();
        await loadBatchOptions();
        msg(`已删除 ${r.removed} 题，清理练习记录 ${r.progress_cleaned} 条，剩余 ${r.remaining} 题`, 'ok');
      } catch (e) {
        msg('删除失败：' + (e && e.message ? e.message : e), 'err');
        btn.disabled = false; btn.textContent = '删除整批';
      }
    };
  });
}

function renderTable() {
  const tb = document.querySelector('#l-tbody');
  const items = S.filtered.slice(S.page * S.size, (S.page + 1) * S.size);
  tb.innerHTML = items.map(q => `
    <tr data-id="${q.id}" style="cursor:pointer">
      <td><input type="checkbox" class="sel-one" data-id="${q.id}"
            ${S.sel.has(q.id) ? 'checked' : ''}></td>
      <td style="font-size:12px">${q.id}</td>
      <td>${q.subject || ''}</td>
      <td>${q.type || ''}</td>
      <td class="lv-${q.level || ''}">${q.level || '-'}</td>
      <td style="font-size:12px;color:#5a6472">${esc((q.stem_text || '').slice(0, 58))}</td>
      <td style="font-size:12px">${esc(q.kp || '-')}</td>
    </tr>`).join('') ||
    '<tr><td colspan="7" style="text-align:center;color:#9aa;padding:20px">'
    + '没有匹配的题目</td></tr>';

  tb.querySelectorAll('tr[data-id]').forEach(tr => {
    tr.onclick = (ev) => {
      // 点复选框本身不算「查看详情」
      if (ev && ev.target && ev.target.classList.contains('sel-one')) return;
      showDetail(tr.dataset.id);
    };
  });
  tb.querySelectorAll('.sel-one').forEach(cb => {
    cb.onclick = (ev) => { ev.stopPropagation(); };
    cb.onchange = () => {
      const id = cb.dataset.id;
      if (cb.checked) S.sel.add(id); else S.sel.delete(id);
      updSelBar();
    };
  });
  updSelBar();
  const total = S.filtered.length;
  document.querySelector('#l-page').textContent =
    total ? `第 ${S.page + 1} / ${Math.ceil(total / S.size)} 页（共 ${total} 题）` : '';
}

function updSelBar() {
  const bar = document.querySelector('#sel-bar');
  const cnt = document.querySelector('#sel-count');
  if (!bar) return;
  const n = S.sel.size;
  bar.style.display = n ? 'flex' : 'none';
  if (cnt) cnt.textContent = n;
}

function showDetail(id) {
  const q = S.all.find(x => x.id === id);
  if (!q) return;
  const box = document.querySelector('#l-detail');
  box.innerHTML = `
    <div class="card">
      <div class="row" style="margin-bottom:8px">
        <h3 style="margin:0">${q.id}</h3>
        <span style="font-size:12px;color:#5a6472">
          ${q.subject || ''}　${q.type || ''}　难度 ${(q.difficulty ?? '-')}
          　知识点 ${q.kp || '-'}
        </span>
        <button class="ghost" id="d-close" style="margin-left:auto">收起</button>
      </div>
      <div class="paper-wrap"><div class="paper">
        ${renderQuestion(q, { showAnswer: true, baseUrl })}
      </div></div>
    </div>`;
  document.querySelector('#d-close').onclick = () => { box.innerHTML = ''; };
  box.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

async function importPdf() {
  const msg = document.querySelector('#lib-msg');
  let pdf = null;
  try {
    pdf = await pickOpenFile([{ name: 'PDF', extensions: ['pdf'] }]);
  } catch (e) { /* 非 Tauri 环境 */ }

  if (!pdf) {
    const p = prompt('请输入 PDF 的绝对路径：');
    if (!p) return;
    pdf = p;
  }
  const subject = prompt('科目（数学 / 物理 / 化学 / 生物 / 语文 / 英语）：', '数学');
  if (!subject) return;

  msg.className = 'msg info show';
  msg.textContent = '正在拆题，请稍候（每份约 1—2 分钟）…';
  try {
    const r = await api.extract(pdf, subject);
    msg.className = 'msg ok show';
    msg.textContent = `拆题成功：${r.count} 题（${r.year} 年 ${r.subject}）。`
      + `注意：新题尚未合并进题库，请在 py/ 目录确认后再覆盖 data/bank.json。`;
    await load();
  } catch (e) {
    msg.className = 'msg err show';
    msg.textContent = '拆题失败：' + e.message;
  }
}

async function syncExcel() {
  const msg = document.querySelector('#lib-msg');
  let path = null;
  try {
    path = await pickOpenFile([{ name: 'Excel', extensions: ['xlsx'] }]);
  } catch (e) {}
  if (!path) {
    path = prompt('Excel 绝对路径（留空则使用默认路径）：') || null;
  }
  msg.className = 'msg info show';
  msg.textContent = '正在同步…';
  try {
    const r = await api.syncExcel(path);
    msg.className = 'msg ok show';
    msg.textContent = '同步完成：' + (r.log || '').replace(/\n/g, ' ');
    await load();
  } catch (e) {
    msg.className = 'msg err show';
    msg.textContent = '同步失败：' + e.message;
  }
}

async function backup() {
  const msg = document.querySelector('#lib-msg');
  try {
    const r = await api.backup(null);
    msg.className = 'msg ok show';
    msg.textContent = `已备份 ${r.count} 条练习记录 → ${r.path}`;
  } catch (e) {
    msg.className = 'msg err show';
    msg.textContent = '备份失败：' + e.message;
  }
}

function esc(s) {
  return String(s == null ? '' : s)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

/** 顶部消息条（#lib-msg） */
function msg(text, kind) {
  const el = document.querySelector('#lib-msg');
  if (!el) return;
  el.className = 'msg ' + (kind || '') + ' show';
  el.textContent = text;
  if (kind !== 'err') setTimeout(() => { el.classList.remove('show'); }, 4000);
}
