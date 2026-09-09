/**
 * 设置页：复习参数
 *
 * 这里管的是**学习节奏**，不是应用外观：
 *   - 记忆曲线阶梯（答错/答对后隔多久再来）
 *   - 组卷时新题与错题的配比
 *   - 每日新题上限
 *
 * 原来这些数值硬编码在 py/main.py 的 LADDER 字典里，
 * 改一次要动代码并重新打包。现在存 config.json，改完即生效。
 */
import * as api from '../app/api.js';

const LADDER_ROWS = [
  { lv: -2, name: '连错 2 次以上', tip: '压到最低档，最短间隔后就重来' },
  { lv: -1, name: '错 1 次',       tip: '建议 2 天：刚做错时还记着当时的思路，此时重做才改得动' },
  { lv: 0,  name: '未练习',        tip: '固定 0，立即可练' },
  { lv: 1,  name: '对 1 次',       tip: '默认 7 天' },
  { lv: 2,  name: '对 2 次',       tip: '默认 15 天' },
  { lv: 3,  name: '对 3 次',       tip: '默认 30 天' },
  { lv: 4,  name: '对 4 次',       tip: '默认 60 天' },
  { lv: 5,  name: '对 5 次',       tip: '默认 120 天，基本已掌握' },
];

let state = {
  config: null,
  defaults: null,
  dirty: false,
  grades: [],      // 年级列表 [{id,name,seg,hidden,builtin}]
  usage: {},       // {年级ID: 题数}
  unknown: '未标注',
};

export async function mount(host) {
  state.config = null; state.dirty = false;
  host.innerHTML = `
    <div class="card">
      <h2>复习设置</h2>
      <p class="hint">
        这里控制题目的复习节奏。改动保存后立即生效，不需要重启应用。
      </p>

      <div class="sec">
        <div class="sec-h">记忆曲线阶梯</div>
        <p class="hint sm">
          答错后退到最低档，答对后逐档升高、间隔拉长。
          任何一次答错都会退回最低档重新爬。
        </p>
        <div id="ladder-box" class="ladder">
          <span class="muted sm">加载中…</span>
        </div>
      </div>

      <div class="sec">
        <div class="sec-h">组卷配比</div>
        <p class="hint sm">自动组卷时，未练过的新题与错题的占比。两者之和需为 100。</p>
        <div class="row">
          <label>新题 %</label>
          <input type="number" id="mix-new" min="0" max="100" step="5">
          <label style="margin-left:14px">错题 %</label>
          <input type="number" id="mix-wrong" min="0" max="100" step="5">
          <span id="mix-sum" class="mix-sum"></span>
        </div>
      </div>

      <div class="sec">
        <div class="sec-h">其他</div>
        <div class="row">
          <label>每日新题上限</label>
          <input type="number" id="daily-cap" min="1" max="200" step="1">
          <span class="hint sm" style="margin-left:8px">避免一次灌太多</span>
        </div>
        <div class="row">
          <label>「已掌握」阈值</label>
          <input type="number" id="done-lv" min="1" max="5" step="1">
          <span class="hint sm" style="margin-left:8px">达到该等级后不再主动出现</span>
        </div>
        <div class="row">
          <label>到期提前提醒</label>
          <input type="number" id="due-soon" min="0" max="14" step="1">
          <span class="hint sm" style="margin-left:8px">天</span>
        </div>
      </div>

      <div class="sec">
        <div class="sec-h">年级管理</div>
        <p class="hint sm">
          年级是<b>按知识点推断</b>出来的（规则见 <code>py/grade_map.py</code>），
          这里管理年级本身的增删改与显示。
          内置 12 个年级覆盖小学到高中，小学与初中默认隐藏。
        </p>
        <div id="grade-box" class="gm"><span class="muted sm">加载中…</span></div>
        <div class="row" style="margin-top:8px">
          <button id="btn-grade-add">+ 新增年级</button>
          <button id="btn-grade-showall">显示全部</button>
          <button id="btn-grade-reset">恢复默认年级</button>
          <span class="hint sm" id="grade-sum"></span>
        </div>
      </div>

      <div class="row" style="margin-top:16px">
        <button class="primary" id="btn-save">保存</button>
        <button id="btn-reset">恢复默认</button>
        <span class="msg" id="cfg-msg"></span>
      </div>
    </div>`;

  await load();
}

async function load() {
  try {
    const r = await api.getConfig();
    state.config = r.config;
    state.defaults = r.defaults;
    renderLadder();
    fill();
    // 年级单独取（要带题数，用于「删除会影响多少题」的提示）。
    // 失败不该拖垮整个设置页 —— 复习参数照常能用。
    await loadGrades();
  } catch (e) {
    document.querySelector('#ladder-box').innerHTML =
      '<span class="err">加载失败：' + esc(String(e)) + '</span>';
  }
}

async function loadGrades() {
  const box = document.querySelector('#grade-box');
  try {
    const r = await api.gradeUsage();
    state.grades = r.grades || [];
    state.usage = r.usage || {};
    state.unknown = r.unknown || '未标注';
    renderGrades();
  } catch (e) {
    if (box) box.innerHTML = '<span class="err">年级加载失败：' + esc(String(e)) + '</span>';
  }
}

/**
 * 年级列表。
 *
 * 「隐藏」和「删除」的区别必须一眼看懂，否则用户以为隐藏就是删了、
 * 或者删了之后找不回来：
 *   隐藏 —— 年级还在，只是不出现在筛选和统计里，随时能显示回来
 *   删除 —— 年级定义消失，属于它的题退回「未标注」；
 *           内置年级删除后要靠「恢复默认年级」才能找回来
 */
function renderGrades() {
  const box = document.querySelector('#grade-box');
  const sum = document.querySelector('#grade-sum');
  if (!box) return;

  if (!state.grades.length) {
    box.innerHTML = '<span class="muted sm">暂无年级</span>';
    if (sum) sum.textContent = '';
    return;
  }

  box.innerHTML = state.grades.map(g => {
    const n = state.usage[g.id] || 0;
    const delTitle = n
      ? `删除「${g.name}」？属于它的 ${n} 道题会变成「${state.unknown}」。`
      : `删除「${g.name}」`;
    return `<div class="gm-row${g.hidden ? ' off' : ''}" data-id="${esc(g.id)}">
      <input class="gm-name" value="${esc(g.name)}" data-id="${esc(g.id)}"
             title="改名只影响显示，不影响题目归属">
      <span class="gm-seg">${esc(g.seg || '自定义')}</span>
      <span class="gm-n${n ? '' : ' zero'}" title="${n} 道题">${n}</span>
      <label class="gm-hide" title="隐藏：不出现在筛选与统计里，数据仍在">
        <input type="checkbox" data-hide="${esc(g.id)}"${g.hidden ? ' checked' : ''}>
        隐藏
      </label>
      <button class="sm danger gm-del" data-del="${esc(g.id)}"
              title="${esc(delTitle)}">删除</button>
    </div>`;
  }).join('');

  const hidden = state.grades.filter(g => g.hidden).length;
  if (sum) {
    sum.textContent = `共 ${state.grades.length} 个`
      + (hidden ? `，已隐藏 ${hidden} 个` : '')
      + `　${state.unknown}：${state.usage[state.unknown] || 0} 题`;
  }

  bindGradeRows();
}

function bindGradeRows() {
  const box = document.querySelector('#grade-box');
  if (!box) return;

  // 改名：回车或失焦时保存
  box.querySelectorAll('.gm-name').forEach(el => {
    const commit = () => {
      const g = state.grades.find(x => x.id === el.dataset.id);
      if (!g) return;
      const v = el.value.trim();
      if (!v || v === g.name) { el.value = g.name; return; }
      g.name = v;
      saveGrades();
    };
    el.onchange = commit;
    el.onkeydown = (e) => {
      if (e.key === 'Enter') { e.preventDefault(); el.blur(); }
    };
  });

  box.querySelectorAll('input[data-hide]').forEach(el => {
    el.onchange = () => {
      const g = state.grades.find(x => x.id === el.dataset.hide);
      if (!g) return;
      g.hidden = el.checked;
      saveGrades();
    };
  });

  box.querySelectorAll('[data-del]').forEach(el => {
    el.onclick = () => removeGrade(el.dataset.del);
  });
}

/**
 * 保存年级。
 *
 * 必须带上 config 的其他字段一起提交：
 * setConfig 在后端会与默认值合并，只传 grades 的话
 * 复习参数会被重置成默认 —— 改个年级却把复习节奏冲掉，太冤。
 */
async function saveGrades(extraMsg) {
  const msg = document.querySelector('#cfg-msg');
  try {
    await api.setConfig({ ...state.config, grades: state.grades });
    state.config.grades = state.grades;
    renderGrades();
    if (msg) {
      msg.className = 'msg ok show';
      msg.textContent = extraMsg || '年级已保存，立即生效';
    }
  } catch (e) {
    // 失败了要把界面回滚到实际状态，否则显示的是改成功、实际没改
    await loadGrades();
    if (msg) {
      msg.className = 'msg err show';
      msg.textContent = String(e && e.message ? e.message : e);
    }
  }
}

function removeGrade(id) {
  const g = state.grades.find(x => x.id === id);
  if (!g) return;
  const n = state.usage[id] || 0;
  const tail = n
    ? `\n\n属于它的 ${n} 道题会变成「${state.unknown}」。`
    : '';
  const builtin = g.builtin
    ? `\n（这是内置年级，删除后只能通过「恢复默认年级」找回）`
    : '';
  if (!confirm(`删除年级「${g.name}」？${tail}${builtin}`)) return;
  state.grades = state.grades.filter(x => x.id !== id);
  saveGrades('已删除年级');
}

function addGrade() {
  const name = (prompt('新年级名称（如「竞赛班」「预科」）') || '').trim();
  if (!name) return;
  if (state.grades.some(x => x.name === name)) {
    alert(`已存在同名的年级「${name}」`);
    return;
  }
  // 自定义 id 加 u 前缀，避开内置 id（p*/j*/s*），
  // 否则日后「恢复默认年级」可能撞车。
  let i = 1;
  while (state.grades.some(x => x.id === 'u' + i)) i++;
  state.grades.push({
    id: 'u' + i, name, seg: '自定义', hidden: false, builtin: false,
  });
  saveGrades(`已新增「${name}」`);
}

function showAllGrades() {
  state.grades.forEach(g => { g.hidden = false; });
  saveGrades('已显示全部年级');
}

function resetGrades() {
  const defs = (state.defaults && state.defaults.grades) || [];
  if (!defs.length) return;
  if (!confirm('恢复为内置年级（小学到高中）？\n\n'
             + '自定义的年级会被移除，改名与隐藏状态也会重置。')) return;
  // 深拷贝：直接用 defaults 的对象会被后续编辑改到，
  // 下次再点「恢复默认」拿到的就是被污染的那份。
  state.grades = defs.map(g => ({ ...g }));
  saveGrades('已恢复默认年级');
}

function renderLadder() {
  const box = document.querySelector('#ladder-box');
  const lad = state.config.ladder || {};
  box.innerHTML = LADDER_ROWS.map(r => {
    const fixed = r.lv === 0;
    const v = Number(lad[String(r.lv)] ?? 0);
    return `<div class="row ladder-row" title="${esc(r.tip)}">
        <label class="lv-name">${esc(r.name)}</label>
        <span class="lv-tag">${r.lv}</span>
        <input type="number" min="0" max="365" step="1"
               data-lv="${r.lv}" value="${v}"
               ${fixed ? 'disabled' : ''}>
        <span class="unit">天后重现</span>
      </div>`;
  }).join('');

  box.querySelectorAll('input[data-lv]').forEach(el => {
    el.oninput = () => { state.dirty = true; syncMix(); };
  });
}

function fill() {
  const c = state.config;
  document.querySelector('#mix-new').value = c.mix_new_pct;
  document.querySelector('#mix-wrong').value = c.mix_wrong_pct;
  document.querySelector('#daily-cap').value = c.daily_new_cap;
  document.querySelector('#done-lv').value = c.done_level;
  document.querySelector('#due-soon').value = c.due_soon_days;
  ['#mix-new', '#mix-wrong', '#daily-cap', '#done-lv', '#due-soon']
    .forEach(sel => {
      const el = document.querySelector(sel);
      el.oninput = () => { state.dirty = true; syncMix(); };
    });
  syncMix();
}

/** 配比之和实时提示，不等于 100 就标红 —— 让用户在保存前就发现 */
function syncMix() {
  const a = Number(document.querySelector('#mix-new').value || 0);
  const b = Number(document.querySelector('#mix-wrong').value || 0);
  const el = document.querySelector('#mix-sum');
  if (!el) return;
  const ok = a + b === 100;
  el.textContent = `合计 ${a + b}${ok ? '' : '（需为 100）'}`;
  el.className = 'mix-sum' + (ok ? '' : ' bad');
}

export const actions = {
  async save() {
    const msg = document.querySelector('#cfg-msg');
    msg.className = 'msg';
    const ladder = {};
    document.querySelectorAll('#ladder-box input[data-lv]').forEach(el => {
      ladder[el.dataset.lv] = Number(el.value || 0);
    });
    const payload = {
      ladder,
      mix_new_pct: Number(document.querySelector('#mix-new').value || 0),
      mix_wrong_pct: Number(document.querySelector('#mix-wrong').value || 0),
      daily_new_cap: Number(document.querySelector('#daily-cap').value || 0),
      done_level: Number(document.querySelector('#done-lv').value || 0),
      due_soon_days: Number(document.querySelector('#due-soon').value || 0),
    };
    try {
      await api.setConfig(payload);
      // 补回 grades：payload 里没有它（后端会保留现有值），
      // 但本地 state.config 别丢，否则随后改年级时提交的 config 不完整。
      state.config = { ...payload, grades: state.grades };
      state.dirty = false;
      msg.className = 'msg ok show';
      msg.textContent = '已保存，立即生效';
    } catch (e) {
      msg.className = 'msg err show';
      msg.textContent = String(e && e.message ? e.message : e);
    }
  },
  async reset() {
    const msg = document.querySelector('#cfg-msg');
    if (!confirm('恢复为默认参数？当前的自定义设置会被覆盖。')) return;
    try {
      await api.setConfig(state.defaults);
      await load();
      msg.className = 'msg ok show';
      msg.textContent = '已恢复默认';
    } catch (e) {
      msg.className = 'msg err show';
      msg.textContent = String(e && e.message ? e.message : e);
    }
  },
};

export function wire() {
  const b1 = document.querySelector('#btn-save');
  const b2 = document.querySelector('#btn-reset');
  if (b1) b1.onclick = () => actions.save();
  if (b2) b2.onclick = () => actions.reset();
  const g1 = document.querySelector('#btn-grade-add');
  const g2 = document.querySelector('#btn-grade-showall');
  const g3 = document.querySelector('#btn-grade-reset');
  if (g1) g1.onclick = addGrade;
  if (g2) g2.onclick = showAllGrades;
  if (g3) g3.onclick = resetGrades;
}

function esc(s) {
  return String(s == null ? '' : s).replace(/[&<>"]/g,
    c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
}
