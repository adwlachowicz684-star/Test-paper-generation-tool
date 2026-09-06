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

let state = { config: null, defaults: null, dirty: false };

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
  } catch (e) {
    document.querySelector('#ladder-box').innerHTML =
      '<span class="err">加载失败：' + esc(String(e)) + '</span>';
  }
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
      state.config = payload;
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
}

function esc(s) {
  return String(s == null ? '' : s).replace(/[&<>"]/g,
    c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
}
