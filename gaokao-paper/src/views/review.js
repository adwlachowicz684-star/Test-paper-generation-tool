/* ============================================================
   复习计划视图 —— 到期题、错题本、数据备份
   ============================================================ */
import { api } from '../app/api.js';
import { renderQuestion, SLICE_BASE } from '../app/render.js';

const baseUrl = SLICE_BASE;

export async function mount(root) {
  root.innerHTML = `
    <h2 class="title">复习计划</h2>
    <p class="sub">按记忆曲线自动排期。做错的题 2 天后重现，做对后逐级拉长间隔。</p>
    <div id="rev-msg"></div>
    <div id="rev-body"><div class="card">加载中…</div></div>
  `;
  await load();
}

async function load() {
  const body = document.querySelector('#rev-body');
  const msg = document.querySelector('#rev-msg');
  try {
    const r = await api.due();
    const due = r.items || [];

    // 按到期日分组
    const byDate = {};
    for (const q of due) {
      const d = q._progress.next || '';
      (byDate[d] = byDate[d] || []).push(q);
    }
    const dates = Object.keys(byDate).sort();

    body.innerHTML = `
      <div class="card">
        <h3>到期概览</h3>
        <div class="stat-grid">
          <div class="stat"><div class="v">${due.length}</div><div class="k">今日到期</div></div>
          <div class="stat"><div class="v">${r.upcoming_count || 0}</div><div class="k">排队中</div></div>
          <div class="stat"><div class="v">${dates.length}</div><div class="k">涉及日期</div></div>
        </div>
        <div class="row" style="margin-top:14px">
          <button class="primary" id="go-prac" ${due.length ? '' : 'disabled'}>
            开始复习${due.length ? `（${due.length} 题）` : ''}
          </button>
          <button id="btn-backup">备份练习记录</button>
        </div>
      </div>

      ${(r.upcoming || []).length ? `
      <div class="card">
        <h3>排队中（未到复习日）</h3>
        <p style="font-size:12px;color:#5a6472;margin:0 0 10px">
          这些题已练过但还没到下次复习时间。刚做错的题会在这里，
          2 天后自动进入上方「今日到期」。
        </p>
        <table class="grid">
          <thead><tr>
            <th style="width:96px">题目ID</th>
            <th style="width:52px">科目</th>
            <th style="width:88px">复习日</th>
            <th style="width:62px">等级</th>
            <th>题干</th>
          </tr></thead>
          <tbody>
            ${(r.upcoming || []).slice(0, 30).map(q => `
              <tr data-id="${q.id}" style="cursor:pointer">
                <td style="font-size:12px">${q.id}</td>
                <td>${q.subject || ''}</td>
                <td style="font-size:12px">${q._progress.next}</td>
                <td>${q._progress.level}</td>
                <td style="font-size:12px;color:#5a6472">
                  ${esc((q.stem_text || '').slice(0, 50))}</td>
              </tr>`).join('')}
          </tbody>
        </table>
      </div>` : ''}

      <div class="card">
        <h3>数据备份</h3>
        <p style="font-size:13px;color:#5a6472;margin:0">
          练习记录存在本地文件里。<b style="color:#c0392b">换电脑、清缓存、</b>
          <b style="color:#c0392b">重装系统都会导致一个学期的错题历史丢失</b>，
          且无法重建。建议每周备份一次，文件可放网盘。
        </p>
      </div>

      ${dates.map(d => `
        <div class="card">
          <h3>${d}　<span style="font-weight:400;color:#5a6472;font-size:12px">
            ${byDate[d].length} 题</span></h3>
          <table class="grid">
            <thead><tr>
              <th style="width:96px">题目ID</th>
              <th style="width:52px">科目</th>
              <th style="width:62px">错次</th>
              <th style="width:62px">等级</th>
              <th>题干</th>
            </tr></thead>
            <tbody>
              ${byDate[d].map(q => `
                <tr data-id="${q.id}" style="cursor:pointer">
                  <td style="font-size:12px">${q.id}</td>
                  <td>${q.subject || ''}</td>
                  <td>${q._progress.wrong || 0}</td>
                  <td>${q._progress.level}</td>
                  <td style="font-size:12px;color:#5a6472">
                    ${esc((q.stem_text || '').slice(0, 52))}</td>
                </tr>`).join('')}
            </tbody>
          </table>
        </div>`).join('') || `
        <div class="card" style="text-align:center;padding:32px">
          <p style="color:#5a6472;margin:0 0 4px;font-size:15px">暂无到期题</p>
          <p style="color:#9aa;margin:0;font-size:13px">
            完成练习后，做错的题会在 2 天后出现在这里</p>
        </div>`}

      <div id="rev-detail"></div>`;

    const gp = document.querySelector('#go-prac');
    if (gp) gp.onclick = () => location.hash = '#/practice';
    document.querySelector('#btn-backup').onclick = async () => {
      try {
        const b = await api.backup(null);
        msg.className = 'msg ok show';
        msg.textContent = `已备份 ${b.count} 条 → ${b.path}`;
      } catch (e) {
        msg.className = 'msg err show';
        msg.textContent = '备份失败：' + e.message;
      }
    };

    body.querySelectorAll('tr[data-id]').forEach(tr => {
      tr.onclick = () => showDetail(tr.dataset.id, due.concat(r.upcoming || []));
    });
  } catch (e) {
    msg.className = 'msg err show';
    msg.textContent = '加载失败：' + e.message;
    body.innerHTML = '';
  }
}

function showDetail(id, pool) {
  const q = pool.find(x => x.id === id);
  if (!q) return;
  const box = document.querySelector('#rev-detail');
  box.innerHTML = `
    <div class="card">
      <div class="row" style="margin-bottom:8px">
        <h3 style="margin:0">${q.id}</h3>
        <span style="font-size:12px;color:#5a6472">
          练习 ${q._progress.count} 次　错 ${q._progress.wrong || 0} 次
          　上次 ${q._progress.last}　${q._progress.last_ok ? '✔' : '✘'}
        </span>
        <button class="ghost" id="rd-close" style="margin-left:auto">收起</button>
      </div>
      <div class="paper-wrap"><div class="paper">
        ${renderQuestion(q, { showAnswer: true, baseUrl })}
      </div></div>
    </div>`;
  document.querySelector('#rd-close').onclick = () => { box.innerHTML = ''; };
  box.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function esc(s) {
  return String(s == null ? '' : s)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}
