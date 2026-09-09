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

      ${renderGradeCard(st)}
      ${renderKpCards(st)}`;

    bindToggles();
  } catch (e) {
    msg.className = 'msg err show';
    msg.textContent = '加载失败：' + e.message;
    body.innerHTML = '';
  }
}

/* ------------------------------------------------------------
   知识点覆盖
   ------------------------------------------------------------
   by_kp 是**按科目分组**的：{科目: [[大知识点, 题数], ...]}。

   之前这里当成了 {知识点: 题数} 直接 Object.entries 渲染，
   于是 value 是数组、被字符串化后整段塞进「题数」单元格，
   一科所有知识点全挤在一行里，占比条的宽度还算出 NaN。
   ------------------------------------------------------------ */

/** 归一成 {科目: [[大知识点, 题数], ...]}，容忍后端返回旧格式 */
function groupedKp(byKp) {
  const out = {};
  for (const [k, v] of Object.entries(byKp || {})) {
    if (Array.isArray(v)) out[k] = v;
    else if (typeof v === 'number') (out[''] = out[''] || []).push([k, v]);
  }
  return out;
}

/**
 * 三级明细树：{科目: [{name, n, children:[{name, n, topics:[{id,name,n}]}]}]}
 * 后端没给（老版本 / 接口失败）时，退化成只有一级，至少不再串行。
 */
function kpTree(st) {
  if (st.kp_tree && Object.keys(st.kp_tree).length) return st.kp_tree;
  const tree = {};
  for (const [sub, list] of Object.entries(groupedKp(st.by_kp))) {
    tree[sub] = list.map(([name, n]) => ({ name, n, children: [] }));
  }
  return tree;
}

/**
 * 年级分布。
 *
 * grade 是**派生字段**：题库里没有这个数据，由 grade_map.py
 * 按「知识点 → 年级」实时推断，不写回题库。
 * 好处是改映射立刻生效、错题不会固化；代价是映射改了数字就变。
 * 所以这里必须说清来源，否则用户会当成权威数据用。
 */
function renderGradeCard(st) {
  const per = st.by_grade_sub || {};
  const subs = Object.keys(per);
  // 老后端没有这份数据，直接不显示 —— 空卡片比「全是0」更少误导
  if (!subs.length) return '';

  // 年级列表：先按后端给的标准顺序，再补上数据里多出来的（如「未标注」）。
  // 用 Set 去重 —— 直接 concat 会把已存在的年级再拼一遍，
  // 表头出现「高一 高二 高三 高一 高二 高三」。
  const grades = [];
  const seenG = new Set();
  for (const g of (st.grades || [])) {
    if (!seenG.has(g)) { seenG.add(g); grades.push(g); }
  }
  for (const c of Object.values(per)) {
    for (const g of Object.keys(c)) {
      if (!seenG.has(g)) { seenG.add(g); grades.push(g); }
    }
  }

  // 占比条按**全库最大**做基准。
  // 若用每行自己的总数，每行都是 100%，条一样长，看着像数据没变。
  const rowMax = Math.max(1, ...subs.map(s =>
    Object.values(per[s] || {}).reduce((a, b) => a + b, 0)));

  const row = (label, counter) => {
    const total = Object.values(counter).reduce((a, b) => a + b, 0);
    return `<tr>
      <td class="kp-cell">${esc(label)}</td>
      ${grades.map(g => `<td class="kp-num">${counter[g] || 0}</td>`).join('')}
      <td class="kp-num"><b>${total}</b></td>
      <td>${bar(total, rowMax)}</td>
    </tr>`;
  };

  return `
    <div class="card">
      <h3>年级分布</h3>
      <table class="grid kp-table">
        <thead><tr>
          <th>科目</th>${grades.map(g => `<th style="width:64px">${esc(g)}</th>`).join('')}
          <th style="width:56px">合计</th>
          <th style="width:150px">占比</th>
        </tr></thead>
        <tbody>${subs.map(s => row(s, per[s] || {})).join('')}</tbody>
      </table>
      <p style="font-size:12px;color:#5a6472;margin:10px 0 0">
        年级是<b>按知识点推断</b>的，不是原始录入数据 ——
        映射规则见 <code>py/grade_map.py</code>，改完立即生效。
        个别题目判断不准属正常，可在题目上直接写 <code>grade</code> 字段覆盖。
      </p>
    </div>`;
}

function renderKpCards(st) {
  const tree = kpTree(st);
  const subs = Object.keys(tree);
  if (!subs.length) {
    return `<div class="card"><h3>知识点覆盖</h3>
      <p style="font-size:13px;color:#5a6472">题库里还没有标注知识点的题目。</p></div>`;
  }

  // 每一级各用自己的最大值做占比基准：
  // 拿大知识点的量级去量题型，题型条会全被压成一条线。
  let maxN1 = 1, maxN2 = 1, maxN3 = 1;
  for (const l1s of Object.values(tree)) {
    for (const l1 of l1s) {
      maxN1 = Math.max(maxN1, l1.n || 0);
      for (const l2 of l1.children || []) {
        maxN2 = Math.max(maxN2, l2.n || 0);
        for (const t of l2.topics || []) maxN3 = Math.max(maxN3, t.n || 0);
      }
    }
  }

  return subs.map(sub => {
    const l1s = tree[sub] || [];
    const n2 = l1s.reduce((s, x) => s + (x.children || []).length, 0);
    const n3 = l1s.reduce((s, x) => s +
      (x.children || []).reduce((s2, c) => s2 + (c.topics || []).length, 0), 0);

    const rows = [];
    l1s.forEach((l1, gi) => {
      const kids = l1.children || [];
      // 折叠后也要能一眼看出这一块有多厚
      const nTop = kids.reduce((s, c) => s + (c.topics || []).length, 0);
      rows.push(
        `<tr class="kp-r1" data-g="${gi}">
           <td class="kp-cell kp-l1">
             <span class="kp-tg" data-tg="${gi}">${kids.length ? '▾' : '·'}</span>${esc(l1.name)}
             ${kids.length ? `<span class="kp-meta">${kids.length} 个小知识点 · ${nTop} 个题型</span>` : ''}
           </td>
           <td class="kp-num">${l1.n}</td>
           <td>${bar(l1.n, maxN1)}</td>
         </tr>`);

      kids.forEach((l2, ci) => {
        const tops = l2.topics || [];
        rows.push(
          `<tr class="kp-r2 g${gi}" data-g="${gi}">
             <td class="kp-cell kp-l2">
               <span class="kp-tg" data-tg="${gi}_${ci}">${tops.length ? '▾' : '·'}</span>${esc(l2.name)}
             </td>
             <td class="kp-num">${l2.n}</td>
             <td>${bar(l2.n, maxN2)}</td>
           </tr>`);

        // 没挂题型的小知识点，自己就是叶子，不再往下铺行
        (tops || []).forEach(t => {
          rows.push(
            `<tr class="kp-r3 g${gi} c${gi}_${ci}" data-g="${gi}">
               <td class="kp-cell kp-l3">${esc(t.name)}</td>
               <td class="kp-num">${t.n}</td>
               <td>${bar(t.n, maxN3)}</td>
             </tr>`);
        });
      });
    });

    return `
      <div class="card kp-card" data-sub="${esc(sub || '默认')}">
        <h3>知识点覆盖 · ${esc(sub)}</h3>
        <p style="font-size:12px;color:#5a6472;margin:-4px 0 10px">
          共 ${l1s.length} 个大知识点、${n2} 个小知识点、${n3} 个题型。
          点名称前的三角可折叠下一层。
        </p>
        ${kpTools(n2, n3)}
        <table class="grid kp-table">
          <colgroup>
            <col style="width:auto"><col style="width:56px"><col style="width:180px">
          </colgroup>
          <thead><tr>
            <th>大知识点 / 小知识点 / 题型</th>
            <th>题数</th>
            <th>占比</th>
          </tr></thead>
          <tbody>${rows.join('') || '<tr><td colspan="3">暂无数据</td></tr>'}</tbody>
        </table>
      </div>`;
  }).join('');
}

/**
 * 批量层级按钮。
 *
 * 三级全铺开有 160+ 行，想只看小知识点得一行行点 ——
 * 所以给一组「一次铺到指定深度」的按钮。
 *
 * 没有数据的层级直接禁用：只有大知识点时点「到题型」什么都不会发生，
 * 与其让用户以为是坏了，不如一开始就点不动。
 */
function kpTools(n2, n3) {
  const b = (lv, label, ok) =>
    `<button class="kp-lv" data-level="${lv}"${ok ? '' : ' disabled'}`
    + `${ok ? '' : ` title="该层暂无数据"`}>${label}</button>`;
  return `
    <div class="kp-tools">
      <span class="kp-tools-t">展开层级</span>
      ${b(1, '仅大知识点', true)}
      ${b(2, '到小知识点', n2 > 0)}
      ${b(3, '到题型', n3 > 0)}
      <span class="kp-cnt"></span>
    </div>`;
}

/* ------------------------------------------------------------
   展开 / 折叠
   ------------------------------------------------------------
   两种操作共用一个状态 —— 行上的 style.display：
     · 点三角：只动某一块
     · 点层级按钮：整表铺到指定深度
   每次改完都要同步三角符号和按钮高亮，
   否则会出现「按钮显示已展开、实际却是收起的」这种自相矛盾的界面。
   ------------------------------------------------------------ */

function bindToggles() {
  const body = document.querySelector('#st-body');
  if (!body) return;

  body.addEventListener('click', e => {
    // ① 层级按钮
    const lvBtn = e.target.closest('.kp-lv');
    if (lvBtn) {
      if (lvBtn.disabled) return;
      setLevel(lvBtn.closest('.kp-card'), +lvBtn.dataset.level);
      return;
    }

    // ② 单个三角
    const tg = e.target.closest('.kp-tg');
    if (!tg) return;
    const key = tg.dataset.tg || '';
    const now = tg.textContent === '▾';
    tg.textContent = now ? '▸' : '▾';
    const sel = key.includes('_')
      // 收小知识点：只藏它下面的题型行
      ? `.kp-r3.c${key}`
      // 收大知识点：连小知识点带题型一起藏
      : `.kp-r2.g${key}, .kp-r3.g${key}`;
    body.querySelectorAll(sel).forEach(tr => { tr.style.display = now ? 'none' : ''; });

    // 手动点过之后可能是「半展开」的自定义状态，按钮高亮要重算
    syncLevelBtns(tg.closest('.kp-card'));
    updateRowCount(tg.closest('.kp-card'));
  });

  body.querySelectorAll('.kp-card').forEach(c => {
    const want = savedLevel(c.dataset.sub || '');
    if (!want) { syncLevelBtns(c); updateRowCount(c); return; }

    // 记住的层级可能已经不成立了（题库变动后某层没了）。
    // 降级到实际存在的最深一层，否则会停在「按钮全不高亮」的哑状态，
    // 用户看不出当前到底是几级。
    const avail = [...c.querySelectorAll('.kp-lv')]
      .filter(b => !b.disabled).map(b => +b.dataset.level);
    let lv = want;
    while (lv > 1 && !avail.includes(lv)) lv--;
    setLevel(c, lv);
  });
}

/**
 * 记住每张卡片上次选的展开层级。
 *
 * 按**科目**分别记：数学想看题型、物理只想看大块，是两种合理需求，
 * 不该因为切了个科就把另一边的偏好冲掉。
 *
 * 存 localStorage 而非后端 —— 这只是界面偏好，换台电脑重设一次无妨。
 * 读写都包在 try 里：隐私模式下 localStorage 可能直接抛异常，
 * 不能因为记不住偏好就让统计页打不开。
 */
const PREF_KEY = 'stats.kpLevel.';

function savedLevel(sub) {
  try {
    const v = +(localStorage.getItem(PREF_KEY + sub) || 0);
    return v >= 1 && v <= 3 ? v : 0;      // 0 = 没记过，走默认
  } catch (e) { return 0; }
}

function saveLevel(sub, level) {
  try { localStorage.setItem(PREF_KEY + sub, String(level)); } catch (e) {}
}

/** 批量铺到指定层级：1=仅大知识点 2=+小知识点 3=+题型 */
function setLevel(card, level) {
  if (!card) return;
  const show2 = level >= 2, show3 = level >= 3;

  card.querySelectorAll('tr.kp-r2')
    .forEach(tr => { tr.style.display = show2 ? '' : 'none'; });
  card.querySelectorAll('tr.kp-r3')
    .forEach(tr => { tr.style.display = show3 ? '' : 'none'; });

  // 三角符号跟着翻，否则「全展开」后图标还是收起的 ▸
  card.querySelectorAll('.kp-tg').forEach(tg => {
    if (tg.textContent === '·') return;        // 没有下一层，保持原样
    const isL2 = (tg.dataset.tg || '').includes('_');
    tg.textContent = (isL2 ? show3 : show2) ? '▾' : '▸';
  });

  card.querySelectorAll('.kp-lv').forEach(b => {
    b.classList.toggle('on', !b.disabled && +b.dataset.level === level);
  });
  updateRowCount(card);
  saveLevel(card.dataset.sub || '', level);
}

/**
 * 由当前实际显示状态反推层级，同步按钮高亮。
 * 谁都不匹配时（比如手动展开了某几个）全部不高亮 ——
 * 这时叫「自定义」，硬点亮某个按钮反而是在骗人。
 */
function syncLevelBtns(card) {
  if (!card) return;
  const vis = tr => tr.style.display !== 'none';
  // 空列表必须与任何状态**都兼容**：
  // 某层没数据时它在判断里不提供信息。若按「空 = 任意 want 都成立」，
  // 只有大知识点时会同时满足 1 级和 3 级，最后算出 lv=3，
  // 于是被禁用的「到题型」反而高亮 —— 禁用按钮点不动却亮着，自相矛盾。
  const eq = (list, want) => list.length
    ? list.every(tr => vis(tr) === want) : true;

  const r2 = [...card.querySelectorAll('tr.kp-r2')];
  const r3 = [...card.querySelectorAll('tr.kp-r3')];

  let lv = 0;
  if (eq(r2, false) && eq(r3, false)) lv = 1;
  else if (eq(r2, true) && eq(r3, false)) lv = 2;
  else if (eq(r2, true) && eq(r3, true)) lv = 3;

  card.querySelectorAll('.kp-lv').forEach(b => {
    b.classList.toggle('on', !b.disabled && +b.dataset.level === lv);
  });
}

/** 右上角行数：折叠了多少一眼可见 */
function updateRowCount(card) {
  if (!card) return;
  const el = card.querySelector('.kp-cnt');
  if (!el) return;
  const all = [...card.querySelectorAll('.kp-table tbody tr')];
  if (!all.length) { el.textContent = ''; return; }
  const shown = all.filter(tr => tr.style.display !== 'none').length;
  el.textContent = `显示 ${shown} / ${all.length} 行`;
}

function bar(n, max) {
  const w = Math.round((n || 0) / (max || 1) * 100);
  return `<div style="background:#eef2f8;border-radius:3px;height:15px">
            <div style="border-radius:3px;height:15px;width:${Math.max(w, 2)}%;
              min-width:3px;background:var(--brand2);opacity:.75"></div>
          </div>`;
}

function esc(s) {
  return String(s == null ? '' : s)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}
