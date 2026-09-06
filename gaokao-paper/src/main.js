/* ============================================================
   应用入口 —— 路由与装配
   ============================================================ */
import { api, isNative, onBridgeError, probeBridge } from './app/api.js';
import * as Compose from './views/compose.js';
import * as Practice from './views/practice.js';
import * as Library from './views/library.js';
import * as Review from './views/review.js';
import * as Stats from './views/stats.js';
import * as Settings from './views/settings.js';

/** 桥接服务未启动时显示的引导页 */
const BRIDGE_GUIDE = `
  <div class="card" style="border-color:#e8b4a8;background:#fdf3f1">
    <h3 style="color:#c0392b;margin-bottom:10px">⚠ 桥接服务未启动</h3>
    <p style="font-size:13px;color:#5a6472;margin:0 0 12px">
      当前运行在<b>浏览器模式</b>，需要一个本地服务来转发 Python 调用。
      请在项目根目录执行：
    </p>
    <pre style="background:#1f2430;color:#e6e9ef;padding:12px 14px;
                border-radius:6px;font-size:12.5px;overflow-x:auto;margin:0 0 12px">python3 tools/dev_bridge.py</pre>
    <p style="font-size:13px;color:#5a6472;margin:0 0 12px">
      然后刷新本页。或者用桌面模式启动，就不需要这一步：
    </p>
    <pre style="background:#1f2430;color:#e6e9ef;padding:12px 14px;
                border-radius:6px;font-size:12.5px;overflow-x:auto;margin:0">npm run tauri dev</pre>
    <div class="row" style="margin-top:14px">
      <button class="primary" id="btn-retry">重试连接</button>
    </div>
  </div>`;

function showBridgeGuide() {
  const main = document.getElementById('main');
  if (!main || main.dataset.guide === '1') return;
  main.dataset.guide = '1';
  main.innerHTML = '<div class="view active">' + BRIDGE_GUIDE + '</div>';
  const b = document.getElementById('btn-retry');
  if (b) b.onclick = () => { main.dataset.guide = ''; boot(); };
}

const ROUTES = {
  '#/compose':  { name: '自动组卷', icon: '📝', view: Compose },
  '#/practice': { name: '在线练习', icon: '✏️', view: Practice },
  '#/review':   { name: '复习计划', icon: '🔁', view: Review },
  '#/library':  { name: '题库',     icon: '📚', view: Library },
  '#/stats':    { name: '学习统计', icon: '📊', view: Stats },
  '#/settings': { name: '设置',     icon: '⚙️', view: Settings },
};

async function render() {
  const hash = location.hash || '#/compose';
  const route = ROUTES[hash] || ROUTES['#/compose'];

  document.querySelectorAll('#sidebar nav a').forEach(a => {
    a.classList.toggle('active', a.dataset.hash === hash);
  });

  const main = document.getElementById('main');
  main.innerHTML = '<div class="view active"></div>';
  const host = main.querySelector('.view');
  await route.view.mount(host);
  // 各视图自己的按钮接线（mount 之后 DOM 才存在）
  if (typeof route.view.wire === 'function') route.view.wire();
  main.scrollTop = 0;
}

async function refreshBadge() {
  try {
    const r = await api.due();
    const b = document.getElementById('due-badge');
    if (b) {
      b.textContent = r.count || '';
      b.style.display = r.count ? '' : 'none';
    }
  } catch (e) { /* 静默 */ }
}

async function checkHealth() {
  const el = document.getElementById('health');
  if (!el) return;
  try {
    const h = await api.health();
    const miss = ['pymupdf', 'docx', 'PIL'].filter(k => !h['dep_' + k]);
    const mode = isNative() ? '桌面模式' : '浏览器模式';
    if (miss.length) {
      // 缺库只影响「导入 PDF」和「生成 Word」，
      // 组卷/练习/复习这些核心功能不受影响 —— 别写成整体不可用
      el.innerHTML = `Python ${h.python}　题库 ${h.bank_count || 0} 题`
        + `<br>${mode}`
        + `<br><span style="color:#e8b4a8">⚠ 缺库：${miss.join('、')}`
        + `<br>（仅影响导入 PDF）</span>`;
    } else {
      el.innerHTML = `Python ${h.python}　题库 ${h.bank_count || 0} 题<br>${mode}`;
    }
  } catch (e) {
    el.innerHTML = `<span style="color:#e8b4a8">⚠ Python 不可用<br>${e.message}</span>`;
  }
}

function buildSidebar() {
  const nav = document.getElementById('nav');
  nav.innerHTML = Object.entries(ROUTES).map(([h, r]) =>
    `<a data-hash="${h}"><span>${r.icon}</span><span>${r.name}</span>`
    + (h === '#/review' ? '<span class="badge" id="due-badge" style="display:none"></span>' : '')
    + `</a>`).join('');
  nav.querySelectorAll('a').forEach(a => {
    a.onclick = () => { location.hash = a.dataset.hash; };
  });
}

window.addEventListener('hashchange', () => { render(); refreshBadge(); });

async function boot() {
  buildSidebar();
  checkHealth();

  // 浏览器模式下先探一次桥接服务。
  // 不探测的话，用户会看到各视图逐个报错，却不知道根因是服务没起。
  if (!isNative()) {
    const alive = await probeBridge();
    if (!alive) {
      showBridgeGuide();
      return;
    }
  }
  await render();
  refreshBadge();
}

document.addEventListener('DOMContentLoaded', () => {
  onBridgeError(showBridgeGuide);   // 运行中断连时也能给出指引
  boot();
});
