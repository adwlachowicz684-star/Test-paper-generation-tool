/* ============================================================
   统计视图 —— 掌握度面板
   ============================================================ */
import { api } from '../app/api.js';

export async function mount(root) {
  root.innerHTML = `
    <h2 class="title">学习统计</h2>
    <p class="sub">题库覆盖情况与练习进展。</p>
    <div id="st-msg"></div>
    <div id="st-body"><div class="card">加载中…</div></div>
  `;
  await load();
}

async function load() {
  const body = document.querySelector('#st-body');
  const msg = document.querySelector('#st-msg');
  try {
    // due 失败不该让整个统计页白屏 —— 它只是锦上添花的一个数字。
    // 用 allSettled 分开处理：stats 失败才真正报错。
    const [stRes, dueRes] = await Promise.allSettled([api.stats(), api.due()]);
    if (stRes.status === 'rejected') throw stRes.reason;
    const st = stRes.value;
    const due = dueRes.status === 'fulfilled' ? dueRes.value : { count: 0 };
    const kp = Object.entries(st.by_kp || {}).sort((a, b) => b[1] - a[1]);
    const maxKp = kp.length ? kp[0][1] : 1;

    body.innerHTML = `
      <div class="card">
        <h3>题库概览</h3>
        <div class="stat-grid">
          <div class="stat"><div class="v">${st.total}</div><div class="k">题目总数</div></div>
          ${Object.entries(st.by_subject).map(([k, v]) =>
            `<div class="stat"><div class="v">${v}</div><div class="k">${k}</div></div>`
          ).join('')}
          <div class="stat"><div class="v lv-困难">${due.count}</div>
            <div class="k">今日到期</div></div>
        </div>
      </div>

      <div class="card">
        <h3>难度分布</h3>
        <div class="stat-grid">
          ${['容易', '适中', '较难', '困难'].map(k =>
            `<div class="stat"><div class="v lv-${k}">${(st.by_level || {})[k] || 0}</div>
             <div class="k">${k}</div></div>`).join('')}
        </div>
        <p style="font-size:12px;color:#5a6472;margin:12px 0 0">
          组卷建议配比：容易 30% / 适中 45% / 较难 20% / 困难 5%。
          中档题是主战场，压轴题量力而行。
        </p>
      </div>

      <div class="card">
        <h3>知识点覆盖</h3>
        <table class="grid">
          <thead><tr>
            <th style="width:220px">知识点</th>
            <th style="width:70px">题数</th>
            <th>占比</th>
          </tr></thead>
          <tbody>
            ${kp.map(([k, v]) => `
              <tr><td>${esc(k)}</td><td>${v}</td>
              <td><div style="background:#eef2f8;border-radius:3px;height:15px;
                    width:${Math.round(v / maxKp * 100)}%;min-width:3px;
                    background:var(--brand2);opacity:.75"></div></td></tr>`).join('')}
          </tbody>
        </table>
      </div>`;
  } catch (e) {
    msg.className = 'msg err show';
    msg.textContent = '加载失败：' + e.message;
    body.innerHTML = '';
  }
}

function esc(s) {
  return String(s == null ? '' : s)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}
