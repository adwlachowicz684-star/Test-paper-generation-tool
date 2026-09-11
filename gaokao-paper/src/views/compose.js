/* ============================================================
   组卷视图 —— 按条件筛题并生成可打印试卷
   ============================================================ */
// pickDirectory 必须一并导入：saveHtml / saveDocx 里用到了，
// 少导入的话一点「导出」就抛 "pickDirectory is not defined"。
import { api, call, pickDirectory } from '../app/api.js';
import { renderPaper, renderQuestion, SLICE_BASE } from '../app/render.js';
import { setPending } from './practice.js';

let state = {
  subject: '数学',
  kp: new Set(),      // 一级（大知识点）名
  // 二级（小知识点）：存 "一级>二级" 而非单存二级名。
  // 不同大知识点下可能有同名小知识点（如「综合应用」），
  // 只存名字会串 —— 取消 A 块下的，B 块下同名的也跟着没了。
  kp2: new Set(),
  // 题型：存 **"一级>二级>题型ID"** 三元组，不存裸 ID。
  //
  // 题库里有 35 个题型是**交叉归属**的（同一个 ID 出现在多个小知识点下，
  // 如 M-T-062 同时在「不等式/综合与交叉」和「函数与导数/零点与图像交点」）。
  // 只存 ID 的话：在 A 处勾了，切到 B 处它也显示为已勾；
  // 取消 B 处的，A 处跟着掉 —— 就是「一打开就错乱」的根源。
  // 提交后端时再取最后一段（后端只认题型 ID）。
  topics: new Set(),
  note: { l1: null, l2: null, topic: null },   // 右侧讲解面板当前指向
  // 焦点 = 下方展开区跟随的大知识点，始终等于**最后勾中的那一个**。
  // 其余已勾的大知识点照常参与组卷，只是这里不展开它们。
  focus: { l1: null, l2: null },
  // 已做过「默认全选」的大知识点。
  // 记这个是为了：用户手动取消过某块之后，
  // 来回切换大知识点不该把他的选择冲掉。
  seeded: new Set(),
  types: new Set(),
  exams: new Set(),    // 考试类型（题目标签，多值；空=全部/不限）
  examStat: {},        // {类型: 题数}
  examList: [],        // 后端给的枚举（不含「全部」）
  paperUse: '综合练习', // 卷头用途，由 exams 推出
  // 中间栏当前显示什么：
  //   false = 预览（选中题型的**全部**题目）
  //   true  = 正式生成的试卷
  // 生成前先看预览，是为了让人确认「我选中的是什么范围」，
  // 再决定抽多少题 —— 而不是盲抽完才发现范围选错了。
  paperMode: false,
  previewTick: 0,      // 预览请求序号，用于丢弃过期响应
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
  // 版式：上「筛选条件」整条 → 下「三栏」
  //
  //   左：小知识点 → 题型（三级树）
  //   中：试卷
  //   右：知识点讲解
  //
  // 小知识点 + 题型单挂一栏后**不再用内部滚动框**：
  // 21 个小知识点、138 个题型塞进 300px 的小框里滚，
  // 看不到全貌、也记不住自己滚到哪了。整栏铺开后跟着页面滚，
  // 一屏能看到十几项，比在小框里翻直观得多。
  root.innerHTML = `
    <h2 class="title">自动组卷</h2>
    <p class="sub">按知识点和难度筛题，生成可直接打印的高考版式试卷。
       筛选条件保存后，下次打开自动恢复。</p>

    <div class="card cz-filter">
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
        <label>考试类型</label>
        <span id="f-exams" class="grow"></span>
        <span class="kp-hint" id="exam-tip"></span>
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

      <div class="row" style="align-items:flex-start">
        <label style="padding-top:4px">大知识点</label>
        <div id="f-kp" class="grow">
          <span style="color:#9aa;font-size:12px">加载中…</span>
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

    <div class="cz3">
      <div class="cz3-left">
        <div class="card cz3-card">
          <div class="card-h">小知识点与题型</div>
          <div id="topic-tree"></div>
        </div>
      </div>

      <div class="cz3-mid">
        <div id="paper-out"></div>
      </div>

      <div class="cz3-right">
        <div class="card kp-note-card">
          <div class="kp-note-h">
            <span>知识点讲解</span>
            <span id="kp-note-cov" class="muted sm"></span>
          </div>
          <div id="kp-note" class="kp-note-body">
            <span class="muted sm">点选左侧任意大知识点 / 小知识点 / 题型，
              这里显示对应的方法与要点。</span>
          </div>
        </div>
      </div>
    </div>
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
    state.exams.clear();
    // 换科目后知识点全变了，全选记录必须作废
    state.seeded.clear();
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
    state.exams.clear();
    // seeded 也要清：否则清空后重新勾同一个大知识点，
    // 因为「已经全选过」而不再全选，结果下方空空如也。
    state.seeded.clear();
    state.note = { l1: null, l2: null, topic: null };
    state.focus = { l1: null, l2: null };
    state.diffMin = 0; state.diffMax = 1;
    $('#f-dmin').value = 0; $('#f-dmax').value = 1;
    $('#d-lo').textContent = '0.00'; $('#d-hi').textContent = '1.00';
    // 清空后回到「预览」态：条件都没了，当然不该继续显示上一份卷子
    state.paperMode = false;
    renderTypes(); renderKp(); renderTopicTree();
    renderExams(); renderGrades(); loadNote();
    refreshPreview();
  };
  $('#btn-compose').onclick = doCompose;
  $('#btn-print').onclick = () => window.print();

  renderTypes();
  await loadKpCatalog();
  loadNoteStats();   // 先拿完整目录再渲染，否则目录为空
  await loadKp();
  restore();
  buildTopicNq();   // 题型挂题数映射（空卷提示要用）
  // restore() 只在有存档时走到底；没存档也要渲染一次，
  // 否则首次打开中间栏是空白，像是没加载出来。
  if (!state.paperMode) refreshPreview();
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

    state.examStat = st.by_exam || {};
    state.examList = st.exams || [];

    renderKp(); renderTopicTree(); renderExams(); renderGrades();
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

/**
 * 中间栏：组卷前显示「选中题型的全部题目」，生成后显示正式卷。
 *
 * 为什么要有预览态：
 * 组卷是**抽题**（按配比、随机、限题数），抽完才知道范围对不对。
 * 先把命中的题目全列出来，确认范围再点生成 ——
 * 否则每次都要靠"生成出来的卷子看着不对"来反推条件选错了。
 *
 * 与正式卷的边界：
 *   预览 —— 全部题目、不洗牌、不限量（超 200 道截断并提示）
 *   正式 —— 按配比抽 count 道，带卷头
 * 两者用 state.paperMode 区分，生成后不再自动回预览
 * （用户的心理模型是"我已经出好卷了"）。
 */
async function refreshPreview() {
  const box = document.querySelector('#paper-out');
  if (!box) return;

  // 已生成正式卷就不覆盖 —— 用户正看着卷子，
  // 他在左侧改个题型，中间突然变成预览会很突然。
  if (state.paperMode) return;

  // 走**完整条件**（含难度 / 年级 / 考试类型），与点「生成试卷」一致。
  // 只按 topics 取的话，调了难度预览却不变，会误以为条件没生效。
  const cfg = buildCfg(null);

  // 一个知识点都没选时不做预览：
  // 题库 712 道全列出来既慢也没意义，先引导选范围。
  if (!cfg.kp.length) {
    box.innerHTML = `<div class="card" style="padding:14px">
      <div class="card-h">题目预览</div>
      <div style="padding:26px 14px;text-align:center;color:#9aa8bd;font-size:13px">
        先在上方的「筛选条件」里点一个大知识点。<br>
        <span style="font-size:12px">
          确认范围后点「生成试卷」，按配比抽题并加上卷头。</span>
      </div></div>`;
    return;
  }

  // 请求序号：连点时，晚发的请求可能先回来，
  // 后回来的旧结果会把新结果盖掉。只认最后一次发出的。
  const tick = ++state.previewTick;
  box.innerHTML = `<div class="card" style="padding:14px">
    <div class="card-h">题目预览</div>
    <div style="padding:20px 14px;text-align:center;color:#9aa8bd;font-size:13px">
      加载中…</div></div>`;

  let r;
  try {
    r = await api.previewQuestions(cfg, 200);
  } catch (e) {
    if (tick !== state.previewTick || state.paperMode) return;
    box.innerHTML = `<div class="card" style="padding:14px">
      <div class="card-h">题目预览</div>
      <div style="padding:20px 14px;color:#c0392b;font-size:13px">
        加载失败：${esc(String(e && e.message ? e.message : e))}</div></div>`;
    return;
  }
  // await 之后**必须再查一次** paperMode。
  //
  // 只在开头查是不够的：勾完大知识点会立刻发一次预览请求，
  // 如果用户在它返回前点了「生成试卷」，这个请求恢复执行时
  // 会把刚生成的卷子整个覆盖成预览 ——
  // 表现是"生成的试卷一闪就没了"，且新的 DOM 没有拖拽监听，拖不动。
  // 越慢的机器越容易撞上（请求耗时越长，窗口越大）。
  if (tick !== state.previewTick || state.paperMode) return;

  const items = r.items || [];
  const total = r.total || 0;
  const cut = total - items.length;

  if (!items.length) {
    // 预览与正式卷同源，所以这里"没题"就等于"生成也会是空卷"。
    // 文案要一致，别让人以为只是预览没加载出来。
    const nt = cfg.topics.length;
    box.innerHTML = `<div class="card" style="padding:14px">
      <div class="card-h">题目预览</div>
      <div style="padding:26px 14px;text-align:center;color:#9aa8bd;font-size:13px">
        当前条件下没有题目${nt ? `（选中的 ${nt} 个题型下暂无题目）` : ''}。<br>
        <span style="font-size:12px">试试放宽难度区间，或勾上带题数的题型。</span>
      </div></div>`;
    return;
  }

  box.innerHTML = `<div class="card" style="padding:0">
    <div class="card-h">题目预览
      <span style="font-weight:400;color:#8a97ab;font-size:12px;margin-left:8px">
        共 ${total} 题${cut > 0 ? `，显示前 ${items.length} 题` : ''}
      </span>
    </div>
    <div style="padding:6px 12px;border-bottom:1px solid #eef1f6;
                font-size:12px;color:#8a97ab;background:#fbfcfe">
      ${esc(cfg.kp.join('、'))}　·　${cfg.topics.length
        ? cfg.topics.length + ' 个题型' : '不限细分条件'}
    </div>
    <div class="paper-wrap" style="border:0;box-shadow:none;margin:0;padding:12px 16px">
      ${renumber(items).map(q => renderQuestion(q, { showAnswer: false })).join('')}
    </div>
    ${cut > 0 ? `<div style="padding:10px 16px;font-size:12px;color:#8a97ab;
                    border-top:1px solid #eef1f6">
        还有 ${cut} 道未显示。点「生成试卷」按配比抽
        ${state.count} 道，这才是正式卷。
      </div>` : ''}
  </div>`;
}

/** 生成后回预览（用户手动点「回到预览」） */
function backToPreview() {
  state.paperMode = false;
  refreshPreview();
}

/**
 * 考试类型筛选。
 *
 * 双重语义，都从这一行读出来：
 *   ① 筛题 —— 勾中的类型，命中任一即可（与其他条件是 AND）
 *   ② 卷头用途 —— 只勾一个就用它命名卷子；勾多个/不勾 = 综合练习
 *
 * **「全部」不是一个可打在题目上的标签**，它是「不加这个条件」的清空态。
 * 做成单独一个 chip 而不是第 7 个类型：
 * 混在一起会出现「某道题属于全部考试」这种无意义的数据。
 */
function renderExams() {
  const box = document.querySelector('#f-exams');
  const tip = document.querySelector('#exam-tip');
  if (!box) return;

  const list = state.examList || [];
  if (!list.length) {
    // 老后端没有这个字段 → 整行藏起来，留个空行像加载失败
    box.innerHTML = '';
    const row = box.closest('.row');
    if (row) row.style.display = 'none';
    return;
  }
  const row0 = box.closest('.row');
  if (row0) row0.style.display = '';

  const stat = state.examStat || {};
  const none = state.exams.size === 0;

  box.innerHTML =
    `<span class="chip${none ? ' on' : ''}" data-exam="__all__"
       title="不限类型：所有题都参与组卷">全部</span>`
    + list.map(e => {
      const n = stat[e] || 0;
      return `<span class="chip${state.exams.has(e) ? ' on' : ''}"`
        + ` data-exam="${esc(e)}" title="${esc(e)}：${n} 题${n ? '' : '（题库暂无标注）'}">`
        + `${esc(e)}<span class="n"${n ? '' : ' style="opacity:.4"'}>${n}</span>`
        + `</span>`;
    }).join('');

  if (tip) {
    const un = stat['未标注'] || 0;
    tip.textContent = un
      ? `有 ${un} 道题未标注类型`
      : '';
  }

  box.querySelectorAll('.chip[data-exam]').forEach(el => {
    el.onclick = () => {
      const v = el.dataset.exam;
      if (v === '__all__') state.exams.clear();
      else if (state.exams.has(v)) state.exams.delete(v);
      else state.exams.add(v);
      renderExams();
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
    // 选中的给一个 × 用于取消。
    // 点本体只切焦点、不取消 —— 见下面 onclick 的说明。
    return `<span class="chip${on ? ' on' : ''}${cur ? ' cur' : ''}"`
      + ` data-k="${esc(item.name)}"${tip ? ` title="${esc(tip)}"` : ''}>`
      + `${esc(item.name)}<span class="n"${n ? '' : ' style="opacity:.4"'}>${n}</span>`
      + (on ? `<i class="kp-x" data-del="${esc(item.name)}" title="取消选择">×</i>` : '')
      + `</span>`;
  };

  box.innerHTML =
    withCount.map(x => chip(x, stats[x.name])).join('')
    + without.map(x => chip(x, 0)).join('');

  // × ：取消选中（与其下所有小知识点 / 题型）
  box.querySelectorAll('.kp-x').forEach(x => {
    x.onclick = (e) => {
      e.stopPropagation();          // 否则会冒泡到 chip 的"切焦点"
      const k = x.dataset.del;
      state.kp.delete(k);
      // 取消大知识点时，把它下面的小知识点与题型一并清掉。
      // 不清的话它们会一直留在筛选条件里：
      // 提交时 kp 只剩 A，kp2 却还混着 B 的小知识点名，
      // 条件是死的（永远匹配不到），但看着像有东西没清干净。
      dropL1(k);
      // 焦点回退到上一个仍选中的；都不剩则清空
      if (state.focus.l1 === k) {
        state.focus.l1 = [...state.kp][state.kp.size - 1] || null;
      }
      state.focus.l2 = null;
      renderKp();
      renderTopicTree();
      state.note = { l1: state.focus.l1, l2: null, topic: null };
      loadNote();
      refreshPreview();
    };
  });

  box.querySelectorAll('.chip').forEach(c => {
    c.onclick = () => {
      const k = c.dataset.k;
      const had = state.kp.has(k);
      state.kp.add(k);            // 只加不删：取消走 ×

      // 点本体 = 把下方列表切到这一块（成为焦点）。
      //
      // 原来是 toggle（点已选中的就取消），实际用起来很别扭：
      // 选了 A、B 两块后想"回去看看 A"，一点 A 就把它取消了，
      // 得先取消当前的再点回来。切焦点和取消是两件事，
      // 不该挤在同一个手势里。
      state.focus.l1 = k;
      state.focus.l2 = null;

      // 新勾中的大知识点，其下小知识点与题型默认全选。
      // 否则勾了「不等式」却一道它的题都组不出来，
      // 用户只会以为这科没题。
      seedL1(state.focus.l1);

      renderKp();                 // 刷新 .cur 高亮
      renderTopicTree();
      state.note = { l1: state.focus.l1, l2: null, topic: null };
      loadNote();
      refreshPreview();
      void had;
    };
  });
}

/**
 * 把某大知识点下的小知识点与题型**默认全选**。
 *
 * 只做一次（记在 state.seeded）：
 * 用户手动取消过之后，来回切换大知识点不该把他的选择冲掉。
 */
function seedL1(l1) {
  if (!l1 || state.seeded.has(l1)) return;
  state.seeded.add(l1);
  const item = findL1(l1);
  if (!item) return;
  for (const c of (item.children || [])) {
    state.kp2.add(l1 + '>' + c.name);
    for (const nd of (c.nodes || [])) {
      // 只全选**已挂题**的题型：没挂题的勾了也匹配不到，
      // 只会让筛选条件变长，没有收益。
      if (nd && nd.id && (nd.n_qs || 0) > 0) {
        state.topics.add(tKey(l1, c.name, nd.id));
      }
    }
  }
}

/** 该大知识点下的全部小知识点（按目录顺序） */
function l2List(l1) {
  const item = findL1(l1);
  return item ? (item.children || []) : [];
}

/**
 * 从筛选条件里摘掉某个大知识点的全部下级。
 *
 * 只摘**专属**于它的题型：交叉归属的题型（cross 里还有别的大知识点）
 * 可能仍被别的已选块用到，一并删会误伤。
 */
function dropL1(l1) {
  for (const c of l2List(l1)) {
    state.kp2.delete(l1 + '>' + c.name);
    for (const nd of (c.nodes || [])) {
      if (!nd || !nd.id) continue;
      const others = (nd.cross || []).filter(x => x !== l1);
      // 交叉题型（别的块也有它）不能删：那边可能正勾着。
      // 删了就是「取消 A 块，B 块的同 ID 题型也掉了」。
      if (!others.length) state.topics.delete(tKey(l1, c.name, nd.id));
    }
  }
  // 允许它被重新全选：用户取消后有可能再勾回来，
  // 那时应当恢复默认全选，而不是保持「上次被清空」的样子。
  state.seeded.delete(l1);
}

/** 该大知识点下、当前**已勾选**的小知识点 */
function pickedL2(l1) {
  return l2List(l1).filter(c => state.kp2.has(l1 + '>' + c.name));
}

/** 题型的存储键：三元组。见 state.topics 的说明 */
const tKey = (l1, l2, tid) => l1 + '>' + l2 + '>' + tid;

/** 从存储键取题型 ID（提交后端用） */
const tId = (k) => k.slice(k.lastIndexOf('>') + 1);

/** 题型 ID → 挂题数。用于空卷时判断"是不是只勾了没题的题型" */
const TOPIC_NQ = new Map();

function buildTopicNq() {
  TOPIC_NQ.clear();
  for (const l1 of catL1()) {
    for (const c of (l1.children || [])) {
      for (const nd of (c.nodes || [])) {
        if (nd && nd.id) TOPIC_NQ.set(nd.id, nd.n_qs || 0);
      }
    }
  }
}

/** 该大知识点下、可参与筛选（已挂题）的题型键列表 */
function topicKeys(l1, onlyPicked) {
  const out = [];
  for (const c of (onlyPicked ? pickedL2(l1) : l2List(l1))) {
    for (const nd of (c.nodes || [])) {
      if (nd && nd.id && (nd.n_qs || 0) > 0) {
        out.push(tKey(l1, c.name, nd.id));
      }
    }
  }
  return out;
}

/**
 * 下方展开区：小知识点 → 题型（三级同屏）。
 *
 * 三个层级是**包含关系**，不是并列的三列：
 *   大知识点 → 小知识点 → 题型
 * 题型是小知识点下的分支，所以缩进挂在它下面，
 * 而不是另起一列 —— 分成三列时「这个题型属于哪个小知识点」得靠脑补。
 *
 * 跟随**最后勾中**的大知识点：
 * 其余已勾的大知识点照常参与组卷，只是这里不展开它们，
 * 否则选了三块之后下方会变成一堵墙。
 */
function renderTopicTree() {
  const box = document.querySelector('#topic-tree');
  if (!box) return;

  // 整块重建会丢滚动位置（容器被换掉，scrollTop 归零）。
  // 换大知识点时归零是对的（内容全变了），
  // 但同块内增删小知识点时必须还原，否则用户正看着下面，
  // 点一下就弹回顶部，还得重新滚。
  const body = box.querySelector('.tt-body');
  const keepScroll = (body && state.focus.l1) ? body.scrollTop : 0;
  const sameL1 = body ? body.dataset.l1 : null;

  const l1 = state.focus.l1;
  if (!l1) {
    // 大知识点在上方的筛选卡片里（不在本栏），文案要指对位置
    box.innerHTML = '<span class="kp-empty">'
      + '先在上方的「筛选条件」里点一个大知识点</span>';
    return;
  }

  const kids = l2List(l1);
  if (!kids.length) {
    box.innerHTML = '<span class="kp-empty">'
      + esc(l1) + ' 下暂无小知识点</span>';
    return;
  }

  const picked = pickedL2(l1);
  const nTopAll = kids.reduce((s, c) => s + (c.topics || []).length, 0);

  // 一个「全部」按钮管两级：全选 / 取消。
  // 原来拆成「全部小知识点」「全部题型」两个，功能是重复的 ——
  // 取消小知识点时其下题型已被连带清掉，题型那个「全部」没有独立作用，
  // 还容易让人以为两级要分别操作。
  const head = `<div class="tt-bar">
      <span class="tt-src">${esc(l1)}
        <i>${kids.length} 个小知识点 · ${nTopAll} 个题型</i></span>
      <span class="tt-all${allBtnOn(l1) ? ' on' : ''}"
            data-all="both"
            title="全选 / 取消「${esc(l1)}」下的小知识点和题型">全部</span>
      ${(state.kp.size === 1 && !picked.length)
        ? '<span class="tt-tip">未选细分条件 = 不限，仍会组到这一块的题</span>'
        : ''}
    </div>`;

  const groups = kids.map(c => {
    const key = l1 + '>' + c.name;
    const on = state.kp2.has(key);
    const n = state.kp2Stats[key] || 0;
    const tops = c.topics || [];
    const nodes = c.nodes || [];

    // 未勾选的小知识点，其下的题型**不显示**。
    // 它都不参与组卷了，列出来的题型点了也没用。
    const topsHtml = on
      ? `<div class="tt-tops">`
        + tops.map((t, i) => topicChip(l1, c.name, t, nodes[i])).join('')
        + `</div>`
      : '';

    return `<div class="tt-g">
        <div class="tt-l2${on ? ' on' : ''}" data-k2="${esc(c.name)}"
             data-l1="${esc(l1)}"
             title="${esc(c.name)}：${tops.length} 个题型${n ? '，已入库 ' + n + ' 题' : ''}">
          <span class="tt-box">${on ? '✓' : ''}</span>
          <b>${esc(c.name)}</b>
          <span class="tt-n${n ? '' : ' zero'}">${n}</span>
          <span class="tt-meta">${tops.length} 个题型</span>
        </div>
        ${topsHtml}
      </div>`;
  }).join('');

  box.innerHTML = head
    + `<div class="tt-body" data-l1="${esc(l1)}">${groups}</div>`;

  // 同一个大知识点内重建（增删小知识点、恢复全选）→ 还原滚动位置。
  // 换块时不还原：内容完全不同，停在旧位置反而莫名其妙。
  const nb = box.querySelector('.tt-body');
  if (nb && sameL1 === l1 && keepScroll) nb.scrollTop = keepScroll;
  bindTopicTree();
}

/** 已展开（所属小知识点已勾）的题型是否全选 */
function allTopicsOn(l1) {
  const keys = topicKeys(l1, true);
  if (!keys.length) return false;
  return keys.every(k => state.topics.has(k));
}

/** 单个题型标签 */
function topicChip(l1, l2, tname, nd) {
  const tid = (nd && nd.id) || '';
  const nq = (nd && nd.n_qs) || 0;
  const on = !!tid && state.topics.has(tKey(l1, l2, tid));
  const cross = ((nd && nd.cross) || []).filter(x => x !== l1);
  return `<span class="chip tk${nq ? ' has' : ' zero'}${on ? ' on' : ''}"`
    + ` data-tid="${esc(tid)}" data-nq="${nq}"`
    + ` data-l1="${esc(l1)}" data-l2="${esc(l2)}" data-name="${esc(tname)}"`
    + ` title="${esc(tname)}${nq ? '（已挂 ' + nq + ' 题，点击加入筛选）'
                                : '（题库暂无此题型的题目，也可勾选；'
                                  + '只有它被选中时组不出卷）'}">`
    + esc(tname)
    + (cross.length ? `<b>↔${esc(cross.join('+'))}</b>` : '')
    + `<span class="n"${nq ? '' : ' style="opacity:.45"'}>${nq}</span>`
    + `</span>`;
}

function bindTopicTree() {
  const box = document.querySelector('#topic-tree');
  if (!box) return;

  // ---- 顶部「全部」按钮：一下全选，再点取消 ----
  box.querySelectorAll('[data-all]').forEach(el => {
    el.onclick = () => {
      const l1 = state.focus.l1;
      if (!l1) return;
      // 先判状态再改：allBtnOn 依赖 pickedL2 / topics，改完就判不准了
      toggleAll(l1, !allBtnOn(l1));
      renderTopicTree();
      refreshPreview();
    };
  });

  // ---- 小知识点：单击切换勾选 ----
  box.querySelectorAll('.tt-l2').forEach(el => {
    el.onclick = () => {
      const l1 = el.dataset.l1;
      const k2 = el.dataset.k2;
      const key = l1 + '>' + k2;
      const wasOn = state.kp2.has(key);
      if (wasOn) state.kp2.delete(key); else state.kp2.add(key);

      // 取消小知识点 → 连带摘掉它下面的题型。
      // 不摘的话题型虽然不显示了，却还留在筛选条件和中间栏预览里 ——
      // 用户看到「这块没勾，怎么还有它的题」，而且找不到原因。
      // 勾回来时按默认全选恢复（与「新勾中一块」的行为一致）。
      const c = l2List(l1).find(x => x.name === k2);
      if (c) {
        for (const nd of (c.nodes || [])) {
          if (!nd || !nd.id) continue;
          const others = (nd.cross || []).filter(x => x !== l1);
          if (wasOn) {
            if (!others.length) state.topics.delete(tKey(l1, k2, nd.id));
          } else if ((nd.n_qs || 0) > 0) {
            state.topics.add(tKey(l1, k2, nd.id));
          }
        }
      }

      // 取消最后一个 → 自动回到全选。
      // 「至少选一个」用恢复全选兜底，比禁用取消更好：
      // 用户的意图多半是「我不要这一个」，而不是「我什么都不要」。
      if (!pickedL2(l1).length) seedAll(l1);

      state.note = { l1, l2: state.kp2.has(key) ? k2 : null, topic: null };
      renderTopicTree();
      loadNote();
      refreshPreview();
    };
  });

  // ---- 题型：勾选参与筛选；没挂题的仍可点开看讲解 ----
  //
  // **只切 class，不整块重建**。
  // 原来这里调 renderTopicTree()，把 #topic-tree 整个 innerHTML 换掉：
  // 滚动容器（.tt-body）随之重建，scrollTop 归零 ——
  // 表现就是「点一下，列表瞬间弹回最上面」，
  // 而且视觉上跳走了，看起来像"没点中"。
  // 勾选题型不改变列表结构（题型不会消失），没必要重建。
  box.querySelectorAll('.chip[data-tid]').forEach(el => {
    el.onclick = (e) => {
      e.stopPropagation();
      const tid = el.dataset.tid;
      const nq = Number(el.dataset.nq || 0);
      const l1 = el.dataset.l1;
      const l2 = el.dataset.l2 || '';
      const key = tKey(l1, l2, tid);
      // 不再要求 nq > 0 才能勾选。
      //
      // 原来卡这个条件是为了「防止组出空卷」，但理由不成立：
      // 后端 topics 是**命中任一**（any），勾一个没题的题型
      // 只是多加一个候选来源，不会让已有结果变空；
      // 真全勾了空题型，生成时本来就有明确提示。
      // 卡住的代价却是：用户点了没反应，以为功能坏了。
      if (tid) {
        if (state.topics.has(key)) state.topics.delete(key);
        else state.topics.add(key);
        // 同样：取消到 0 个就恢复全选
        if (!countTopicsOn(l1)) {
          seedTopics(l1);
          // 恢复全选影响的是**全部**题型的显示，只能整块刷新。
          // 这时保住滚动位置（见 renderTopicTree 内的 keepScroll）。
          renderTopicTree();
        } else {
          // 常规路径：就地更新，不碰滚动
          el.classList.toggle('on', state.topics.has(key));
          const allBtn = box.querySelector('[data-all="both"]');
          if (allBtn) allBtn.classList.toggle('on', allBtnOn(l1));
        }
      }
      state.note = { l1, l2: l2 || null, topic: tid || null };
      loadNote();
      refreshPreview();
    };
  });
}

/**
 * 「全部」按钮是否处于全选态。
 *
 * 原来「全部小知识点」「全部题型」是两个按钮，但功能重复：
 * 题型挂在小知识点下，取消小知识点时其题型已被连带清掉，
 * 单独再给题型一个「全部」没有独立意义。
 * 合成一个后，全选态 = 小知识点全勾 **且** 其下有题的题型全勾。
 */
/**
 * 把界面状态拼成后端要的 cfg。
 *
 * 抽成函数是因为**预览和正式组卷必须用同一份条件**：
 * 早先预览只提交 topics（连难度、年级、考试类型都没传），
 * 结果预览显示的题和点「生成试卷」实际抽的题不是同一批 ——
 * 调了难度后预览还是老样子，最误导人的那类问题。
 */
function buildCfg(seed) {
  return {
    subject: state.subject,
    types: [...state.types],
    kp: [...state.kp],
    // 后端要的是二级**名字**列表，这里存的是 "一级>二级"，取后半段。
    kp2: [...state.kp2].map(k => k.slice(k.indexOf('>') + 1)),
    // kp2Full 是**存档专用**：带 "一级>二级" 前缀，用来在下次打开时
    // 还原「哪个大知识点下取消了哪几个小知识点」。
    // 少了它，重开后所有块都会被默认全选覆盖 ——
    // 用户取消过的选择全丢，而且看不出为什么。
    // 后端不认识这个字段，会直接忽略。
    kp2Full: [...state.kp2],
    grades: [...state.grades],
    exams: [...state.exams],
    // 内部存的是 "一级>二级>题型ID"，后端只认题型 ID —— 取最后一段。
    // 要去重：交叉归属的题型在多个位置出现，
    // 每个位置都勾着的话会提交重复的 ID（后端 any() 匹配，重复无害但冗余）。
    topics: [...new Set([...state.topics].map(tId))],
    diff_min: state.diffMin,
    diff_max: state.diffMax,
    count: state.count,
    seed: seed === undefined ? null : seed,
  };
}

function allBtnOn(l1) {
  const kids = l2List(l1);
  if (!kids.length) return false;
  if (pickedL2(l1).length !== kids.length) return false;
  const keys = topicKeys(l1, true);
  // 该块下没有任何「有题题型」时只看小知识点。
  // 否则这种块永远进不了全选态，点「全部」会一直重复全选。
  return keys.length ? keys.every(k => state.topics.has(k)) : true;
}

/**
 * 全选 / 取消某大知识点下的小知识点与题型。
 *
 * 注意「取消」的语义：清空后 kp2 与 topics 都为空，
 * 而后端对空条件是**不限**（不是「不选」）——
 * 只勾了这一个大知识点时，取消后的组卷结果与全选相同。
 * 只有在**还勾着别的大知识点**时，取消才真正收窄范围
 * （等于「只要其他块的题」）。
 * 这个反直觉点在界面上用 tt-tip 说明，见 renderTopicTree。
 */
function toggleAll(l1, on) {
  const kids = l2List(l1);
  if (on) {
    for (const c of kids) state.kp2.add(l1 + '>' + c.name);
    // kp2 已全勾，此时 topicKeys 返回的是全部有题题型
    for (const k of topicKeys(l1, true)) state.topics.add(k);
  } else {
    for (const c of kids) state.kp2.delete(l1 + '>' + c.name);
    // 清掉该大知识点下的**所有**题型，含手动勾的暂缺题型。
    // 只清 topicKeys 会漏掉暂缺的（它们 n_qs=0，不在 topicKeys 里），
    // 表现为「点了取消，那几个还亮着」。
    for (const k of [...state.topics]) {
      if (k.indexOf(l1 + '>') === 0) state.topics.delete(k);
    }
  }
}

/** 全选某大知识点下的小知识点（不动题型） */
function seedAll(l1) {
  for (const c of l2List(l1)) state.kp2.add(l1 + '>' + c.name);
}

/** 全选已展开小知识点下的题型 */
function seedTopics(l1) {
  for (const k of topicKeys(l1, true)) state.topics.add(k);
}

/** 当前已展开且已勾选的题型数 */
function countTopicsOn(l1) {
  return topicKeys(l1, true).filter(k => state.topics.has(k)).length;
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

/**
 * 试卷内拖动排序（仅正式卷，预览不可拖）。
 *
 * 拖完的顺序要带到导出 / 打印 / 在线练习 ——
 * 所以不只是挪 DOM，还要同步回 state.picked。
 * 否则拖了半天，一点导出又变回原顺序。
 *
 * 用 **Pointer Events** 而不是 HTML5 拖放（draggable + dragstart）：
 * HTML5 拖放在**触屏上完全不触发** —— 平板上根本拖不动。
 * pointer 事件鼠标 / 触屏 / 触控笔统一，一套代码三端可用。
 *
 * 触屏上必须靠手柄启动拖动：
 * 若整个题目都能拖，则手指在题目上滑动会变成"拖题"而不是"滚页面"，
 * 页面就滚不动了。手柄上才设 touch-action:none，
 * 页面其它区域照常滚动。
 */
const DRAG_THRESHOLD = 6;   // 位移超过这个距离才算"拖"，否则视为点击

function enablePaperDrag(pw) {
  if (!pw) return;
  const qs = [...pw.querySelectorAll('.q')];
  if (!qs.length) return;

  let pending = null;    // 按下但还没开始拖
  let dragging = null;   // 已在拖动
  let dragId = null;     // 拖动中的 pointerId
  let lastTgt = null;    // 上一次落点，避免同一目标反复触发
  let lastY = 0;         // 上一次指针 Y，用于判断拖动方向（兜底路径）

  const clear = () => {
    qs.forEach(el => {
      el.classList.remove('dragging', 'drop-ok');
      // 清掉 FLIP 残留的 transform/transition。
      // 留着的话下一次拖动的起点会量到旧 transform，动画抽搐。
      el.style.transition = '';
      el.style.transform = '';
    });
    document.body.classList.remove('q-dragging');
  };

  const finish = () => {
    if (!dragging) { pending = null; return; }
    clear();
    dragging = null; pending = null; dragId = null; lastTgt = null;
    commitPaperOrder(pw);
  };

  qs.forEach(el => {
    // 手柄：触屏唯一的拖动入口，桌面上也是更明确的抓手。
    // 塞进 .qnum 内部而不是 .q 下 —— .q 是两列 grid，
    // 直接加子元素会让手柄占一格，把题号挤到下一行。
    const numEl = el.querySelector('.qnum');
    if (numEl && !numEl.querySelector('.q-handle')) {
      // 符号用 CSS ::before 画，不放文字节点：
      // 放文字的话 .qnum 的 textContent 会变成「⠿1．」，
      // 复制题干、另存文本时都带着这个符号。
      numEl.insertAdjacentHTML('afterbegin',
        '<span class="q-handle no-print" title="按住拖动排序"></span>');
    }

    el.addEventListener('pointerdown', (e) => {
      // 触屏：只有按在手柄上才能拖，否则留给页面滚动
      const onHandle = e.target && e.target.closest
        && e.target.closest('.q-handle');
      if (e.pointerType === 'touch' && !onHandle) return;
      if (e.button != null && e.button !== 0) return;   // 只响应左键
      pending = { el, x: e.clientX, y: e.clientY, id: e.pointerId };
    });

    el.addEventListener('pointermove', (e) => {
      if (!dragging) {
        if (!pending || e.pointerId !== pending.id) return;
        const dx = e.clientX - pending.x, dy = e.clientY - pending.y;
        if (Math.abs(dx) < DRAG_THRESHOLD && Math.abs(dy) < DRAG_THRESHOLD) return;
        dragging = pending.el;
        dragId = e.pointerId;
        lastTgt = null;
        lastY = e.clientY;
        dragging.classList.add('dragging');
        document.body.classList.add('q-dragging');
        // 标出可放置范围：同题型那一段。
        // 不给提示的话，用户把题拖到不同题型上"没反应"，
        // 只会以为功能坏了 —— 得让他看见边界在哪。
        const r = sameTypeRange(dragging);
        if (r) for (let i = r.from; i <= r.to; i++) {
          r.kids[i].classList.add('drop-ok');
        }
        // 捕获指针：手指移出元素边界也能继续收到事件
        try { el.setPointerCapture(e.pointerId); } catch (err) { /* ignore */ }
      } else if (e.pointerId !== dragId) {
        return;
      }

      e.preventDefault();
      const dir = e.clientY - lastY;
      lastY = e.clientY;

      // 只能在**同题型的连续块内**排序 —— 见 sameTypeRange 的说明。
      const rng = sameTypeRange(dragging);
      if (!rng) return;

      let tgt = dropTargetAt(pw, e.clientX, e.clientY, dragging);
      if (!tgt) {
        // 兜底：指针落在题目之间的空隙、或环境不支持 elementFromPoint 时
        // （无布局引擎的测试环境、部分精简 webview 会返回 null），
        // 退化为「按方向挪一格」。
        // 宁可一格一格挪，也不能整个拖不动 ——
        // 后者用户只会以为功能坏了。
        if (!dir) return;
        const i = rng.kids.indexOf(dragging);
        const j = i + (dir > 0 ? 1 : -1);
        if (j < rng.from || j > rng.to) return;   // 越出本块 = 跨题型，拒绝
        tgt = rng.kids[j];
      }
      // 目标不在本块内（不同题型 / 被别的题型隔开）→ 不接受。
      // 静默忽略比弹提示好：拖动是连续手势，
      // 每次移到不可放的位置都弹窗会非常烦。
      const ti = rng.kids.indexOf(tgt);
      if (ti < rng.from || ti > rng.to) return;

      // 同一个目标只处理一次。
      // pointermove 每几毫秒就来一次，指针停在某个题目上不动时
      // 会反复"插到它前面 / 再插到它后面"，表现为拖着来回抖。
      // HTML5 拖放靠 dragenter（进入新元素才触发）天然避开了这点，
      // pointer 版必须自己记。
      if (!tgt || tgt === dragging || tgt === lastTgt) return;
      lastTgt = tgt;

      // 被拖的元素在目标**之前** → 插到目标后面；否则插到目标前面。
      // 这样往下拖时跟手，往上拖时也不会来回跳。
      //
      // 用子节点下标比较而不是 compareDocumentPosition + Node 常量：
      // 后者依赖全局 Node，某些精简 webview / 测试环境里没暴露它。
      const iD = rng.kids.indexOf(dragging), iT = ti;
      if (iD < 0 || iT < 0) return;
      // 包一层 flip：DOM 换了位置，视觉上滑过去（0.3s）
      flip(pw, () => {
        if (iD < iT) dragging.parentNode.insertBefore(dragging, tgt.nextSibling);
        else dragging.parentNode.insertBefore(dragging, tgt);
      });
      syncPaperNumbers(pw);   // 实时更新题号，松手前就能看到排好后的样子
    });

    el.addEventListener('pointerup', finish);
    el.addEventListener('pointercancel', finish);
  });

  // 松手落在题目之外时也要收尾，否则 dragging 一直挂着。
  // 用**具名函数 + 去重**：直接 addEventListener(finish) 的话，
  // 每次重新生成试卷都会多挂一个，旧的闭包还引用着已被移除的 DOM，
  // 既泄漏又会在后续拖动时误触发。
  if (!enablePaperDrag._bound) {
    enablePaperDrag._bound = [];
    document.addEventListener('pointerup', (e) => {
      enablePaperDrag._bound.forEach(fn => fn(e));
    });
    document.addEventListener('pointercancel', (e) => {
      enablePaperDrag._bound.forEach(fn => fn(e));
    });
  }
  // 旧试卷的监听器先摘掉，只保留当前这一份
  enablePaperDrag._bound = [finish];
}

/**
 * FLIP 动画：让题目"滑"到新位置（0.3s），而不是瞬间跳过去。
 *
 * 瞬间跳的坏处是**看不出发生了什么** ——
 * 拖动时列表一闪就变了，用户不确定自己拖到了哪。
 * 滑动动画能明确展示"这道题从这里移到了那里"。
 *
 * FLIP = First, Last, Invert, Play：
 *   先量旧位置 → 改 DOM → 量新位置 →
 *   用 transform 把元素**倒推**回旧位置 → 再动画回 0。
 * 直接 transition top/left 会触发重排，几十道题会很卡；
 * transform 走合成层，不掉帧。
 */
const FLIP_MS = 300;

function flip(pw, mutate) {
  const items = [...pw.querySelectorAll('.q')];
  if (!items.length) { mutate(); return; }

  // 先清掉上一轮可能残留的 transform / transition。
  // 连续快速拖动时上一轮动画还没跑完，
  // 不清的话 getBoundingClientRect 量到的是动画**中间态**，
  // 起点算错，动画就会抽搐。
  items.forEach(el => {
    el.style.transition = 'none';
    el.style.transform = '';
  });

  const before = new Map();
  items.forEach(el => before.set(el, el.getBoundingClientRect().top));

  mutate();

  items.forEach(el => {
    const dy = (before.get(el) || 0) - el.getBoundingClientRect().top;
    if (!dy) return;
    el.style.transform = `translateY(${dy}px)`;
  });

  // 强制一次重排，让上面的 transform 真正生效。
  // 少了这行，浏览器会把"设置 transform"和"清除 transform"合并成一次计算，
  // 等于什么都没做 —— 动画不会出现。
  void pw.offsetHeight;

  items.forEach(el => {
    if (!el.style.transform) { el.style.transition = ''; return; }
    el.style.transition = `transform ${FLIP_MS}ms cubic-bezier(.2,.8,.3,1)`;
    el.style.transform = '';
  });
}

/**
 * 与 el 同题型、且在 DOM 上**连续**的兄弟范围 [from, to]。
 *
 * 只比 data-type 是不够的：万一同种题型被别的题型隔成两段
 * （后端顺序变动时理论上可能），跨段拖动会破坏分节结构。
 * 限制在同一个连续块内，才能保证"一、选择题"始终是一整块。
 */
function sameTypeRange(el) {
  const parent = el.parentNode;
  if (!parent) return null;
  const kids = [...parent.children]
    .filter(x => x.classList && x.classList.contains('q'));
  const i = kids.indexOf(el);
  if (i < 0) return null;
  const t = el.dataset.type;
  let from = i, to = i;
  while (from > 0 && kids[from - 1].dataset.type === t) from--;
  while (to < kids.length - 1 && kids[to + 1].dataset.type === t) to++;
  return { kids, from, to, type: t };
}

/** 找出指针位置下、属于本试卷的题目元素 */
function dropTargetAt(pw, x, y, exclude) {
  let el = null;
  try {
    el = document.elementFromPoint(x, y);
  } catch (err) { /* 某些环境不支持 */ }
  if (!el || !el.closest) return null;
  const q = el.closest('.q');
  if (!q || !pw.contains(q) || q === exclude) return null;
  return q;
}

/**
 * 把 DOM 顺序同步回 state.picked，并重排题号。
 *
 * 题号按**连续同类分节**重新编号（选择 1、2、3；填空 1、2…）。
 * 不重排的话，把一道解答题拖到选择题中间，
 * 卷面会出现「1、2、7、3」这种跳号。
 */
function commitPaperOrder(pw) {
  const ids = [...pw.querySelectorAll('.q')].map(el => el.dataset.id);
  const byId = new Map((state.picked || []).map(q => [q.id, q]));
  const ordered = ids.map(id => byId.get(id)).filter(Boolean);
  // 数量对不上说明 DOM 与数据已经不同步，宁可不动 ——
  // 静默丢题比顺序不对严重得多。
  if (!ordered.length || ordered.length !== state.picked.length) return;

  state.picked = renumber(ordered);
  syncPaperNumbers(pw);
}

/** 按连续同类分节重排题号（返回新数组，不改原对象） */
function renumber(items) {
  const out = [];
  let n = 0;
  let lastType;
  for (const q of items) {
    if (q.type !== lastType) { n = 0; lastType = q.type; }
    out.push(Object.assign({}, q, { num: ++n }));
  }
  return out;
}

/** 只改 DOM 里的题号文本，不重建整卷（保住已展开的答案） */
function syncPaperNumbers(pw) {
  const items = state.picked || [];
  const byId = new Map(items.map(q => [q.id, q]));
  pw.querySelectorAll('.q').forEach(el => {
    const q = byId.get(el.dataset.id);
    if (!q) return;
    const box = el.querySelector('.qnum');
    if (box) box.textContent = `${q.num}．`;
  });
}

async function doCompose() {
  const btn = document.querySelector('#btn-compose');
  const msg = document.querySelector('#compose-msg');
  const out = document.querySelector('#paper-out');
  btn.disabled = true; btn.textContent = '生成中…';
  msg.className = 'msg'; out.innerHTML = '';

  try {
    const cfg = buildCfg(state.seed === null ? Date.now() % 100000 : state.seed);
    save(cfg);
    const r = await api.compose(cfg);
    // 存副本：拖动排序会重排这个数组，直接存 r.items 的话
    // 后面按 id 回查时原数组已经被改，容易出隐晦的错。
    //
    // 同时**重排题号**：题库里 463 道题的 num 全是 0（导入时没写），
    // 直接用会让整张卷子每题都显示「0．」。
    // 组出来的卷子本就该按「1、2、3…」重新编号，
    // 沿用原题号也没意义（跨年份抽的题，原题号拼不成序）。
    state.picked = renumber(r.items || []);

    if (!r.items.length) {
      msg.className = 'msg err show';
      // 勾了考试类型却出空卷，八成是题库还没标过这个类型 ——
      // 而不是「难度/知识点」没调好。按最可能的原因给提示，
      // 否则用户会去调一堆无关的条件。
      const exs = [...state.exams];
      const allZero = exs.length && exs.every(e => !(state.examStat[e] || 0));
      // 只勾了「暂缺」题型是另一种常见的空卷原因，
      // 而且比"难度没调好"更可能 —— 提示要指对方向，
      // 否则用户会去拖难度滑块，怎么调都不会有题。
      const tids = [...new Set([...state.topics].map(tId))];
      const noQs = tids.length && tids.every(t => !(TOPIC_NQ.get(t) || 0));
      msg.textContent = allZero
        ? `题库里还没有标注为「${exs.join('、')}」的题目，`
          + '所以选不出卷。可以先点「全部」不限类型，'
          + '或先给题目补上考试类型标签。'
        : noQs
        ? `选中的 ${tids.length} 个题型在题库里都还没有题目`
          + '（灰显虚线框的就是暂缺题型）。'
          + '勾上带题数的题型，或点「全部」。'
        : '没有符合条件的题目。'
          + '试试放宽难度区间，或减少知识点/题型的组合条件。';
      document.querySelector('#btn-print').disabled = true;
      return;
    }

    // 进入「正式卷」模式：此后左侧改条件不再自动覆盖中间栏，
    // 否则用户改个题型，刚生成的卷子就没了。
    state.paperMode = true;

    out.innerHTML =
      `<div class="card no-print" style="padding:10px 14px">
         <div class="row">
           <button id="btn-back-preview" title="回到「选中题型的全部题目」预览"
                   style="font-size:12px">← 回到预览</button>
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
    // 卷头用途由后端算好（规则只有一处），前端只消费。
    // 组一份「月考」卷子，卷头就该写月考 —— 否则打出来还得手改。
    state.paperUse = r.paper_use || '综合练习';
    // 用 state.picked（已重排题号），不用 r.items ——
    // 后者 num 全是 0，卷面会显示一片「0．」
    pw.innerHTML = renderPaper(state.picked, {
      title: `${cfg.subject} · ${state.paperUse}卷`,
      sub: `${new Date().toLocaleDateString('zh-CN')}　共 ${r.count} 题`,
      rows: [['科目', cfg.subject],
             ['题量', `${r.count} 题`],
             ['难度区间', `${cfg.diff_min.toFixed(2)} ~ ${cfg.diff_max.toFixed(2)}`]],
      baseUrl: SLICE_BASE,
    });
    document.querySelector('#btn-print2').onclick = () => window.print();
    const bp = document.querySelector('#btn-back-preview');
    if (bp) bp.onclick = backToPreview;

    // 导出/练习都读 state.picked —— 拖完的顺序才能带过去。
    // 用 r.items 的话，拖动只改了 DOM，导出仍是原顺序。
    document.querySelector('#btn-practice').onclick = () => {
      setPending(state.picked, 'compose');
      location.hash = '#/practice';
    };
    document.querySelector('#btn-save-html').onclick =
      () => saveHtml(state.picked, cfg);
    document.querySelector('#btn-save-docx').onclick =
      () => saveDocx(state.picked, cfg);

    enablePaperDrag(pw);   // 正式卷可拖动排序（预览不可）
    const ba = document.querySelector('#btn-ans');
    let shown = false;
    ba.onclick = () => {
      shown = !shown;
      ba.textContent = shown ? '隐藏答案' : '显示答案';
      // 用 state.picked（当前拖动后的顺序），不是 r.items（初始顺序）。
      // 用后者的话，一点「显示答案」刚排好的顺序就被打回原形。
      pw.innerHTML = renderPaper(state.picked, {
        title: `${cfg.subject} · ${state.paperUse}卷`,
        sub: `${new Date().toLocaleDateString('zh-CN')}　共 ${r.count} 题`,
        rows: [['科目', cfg.subject], ['题量', `${r.count} 题`]],
        baseUrl: SLICE_BASE,
      });
      enablePaperDrag(pw);
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
      `${cfg.subject}_${state.paperUse}_${new Date().toISOString().slice(0, 10)}_${items.length}题`);
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
      `${cfg.subject}_${state.paperUse}_${new Date().toISOString().slice(0, 10)}_${items.length}题`);
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
    (c.grades || []).forEach(g => state.grades.add(g));
    (c.exams || []).forEach(e => state.exams.add(e));

    // 优先读 kp2Full（带 "一级>二级" 前缀，能精确定位）。
    // 旧存档只有二级名、没有一级信息，拼不回来就退回默认全选 ——
    // 丢了只是回到全选，比拿一个猜错的一级名去匹配（结果筛掉整块）要好。
    const savedKp2 = new Set(
      (c.kp2Full || c.kp2 || []).map(String).filter(x => x.includes('>')));

    // 已选的大知识点先全部标记为「已全选过」，
    // 否则后续任何一次渲染都会把用户上次的选择覆盖掉。
    // 然后只保留存过的项 —— 即「全选为底，再减掉上次取消的」。
    for (const l1 of state.kp) {
      state.seeded.add(l1);
      for (const c2 of l2List(l1)) {
        const key = l1 + '>' + c2.name;
        if (savedKp2.size === 0 || savedKp2.has(key)) state.kp2.add(key);
      }
    }

    // 焦点 = 最后一个勾中的大知识点（与点击时保持一致）
    state.focus = { l1: [...state.kp][state.kp.size - 1] || null, l2: null };
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
    renderKp(); renderTopicTree(); loadNote();
    refreshPreview();   // 打开就有内容，中间栏不空着
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
