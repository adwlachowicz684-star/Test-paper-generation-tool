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
      <div class="card">
        <h3>知识点覆盖 · ${esc(sub)}</h3>
        <p style="font-size:12px;color:#5a6472;margin:-4px 0 10px">
          共 ${l1s.length} 个大知识点、${n2} 个小知识点、${n3} 个题型。
          点名称前的三角可折叠下一层。
        </p>
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

/** 展开/折叠：只切显示，不重渲染，展开状态自然保留 */
function bindToggles() {
  const body = document.querySelector('#st-body');
  if (!body) return;
  body.addEventListener('click', e => {
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
  });
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
