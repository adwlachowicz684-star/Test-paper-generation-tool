/* ============================================================
   Tauri 调用层 —— 带 Web 降级

   为什么要有降级：
   直接用 `npm run dev` 在浏览器打开时，window.__TAURI__ 不存在。
   降级到直接执行 python3 py/main.py，界面依然可用（只是没有
   原生文件对话框）。这样调试前端不必每次都启动完整的 Tauri。
   ============================================================ */

/**
 * 是否运行在 Tauri 里。
 *
 * 这个判断**必须可靠**：一旦误判为浏览器模式，
 * 请求会走 fetch('/api/...') → 必然 404 → 弹出「桥接服务未启动」，
 * 而用户明明是桌面应用，会完全摸不着头脑。
 *
 * Tauri 2 注入 __TAURI_INTERNALS__；Tauri 1 注入 __TAURI__。
 * 两个都查一遍，外加 navigator.userAgent 兜底（含 "Tauri"）。
 */
const IS_TAURI = (() => {
  if (typeof window === 'undefined') return false;
  if (window.__TAURI_INTERNALS__) return true;
  if (window.__TAURI__) return true;
  try {
    if (/Tauri/i.test(navigator.userAgent || '')) return true;
  } catch (e) { /* ignore */ }
  // 注入的 asset / tauri 协议也是 Tauri 的标志
  try {
    const proto = location.protocol;
    if (proto === 'tauri:' || proto === 'asset:') return true;
  } catch (e) { /* ignore */ }
  return false;
})();

let _invoke = null;
let _bridgeDead = false;      // 桥接服务不可用（避免每个请求都弹一次提示）
let _onBridgeError = null;    // 由 main.js 注册，用于显示醒目提示

/** 注册桥接失败回调（显示一条可操作的引导，而不是静默失败） */
export function onBridgeError(fn) { _onBridgeError = fn; }

/**
 * Tauri 会在 webview 里注入 window.__TAURI_INTERNALS__.invoke。
 *
 * **必须优先用它，而不是 import('@tauri-apps/api/core')**：
 * 本项目是零构建前端，浏览器原生 ES Module 无法解析裸模块说明符
 * （bare specifier），import('@tauri-apps/api/core') 会直接抛
 * "Failed to resolve module specifier" —— 所有 API 调用全挂，
 * 界面看起来是启动了，但什么都点不动。
 *
 * 注入的全局 API 零依赖、始终可用，是零构建场景的唯一正解。
 */
function nativeInvoke() {
  if (typeof window === 'undefined') return null;
  const t = window.__TAURI_INTERNALS__ || window.__TAURI__;
  if (t && typeof t.invoke === 'function') return t.invoke.bind(t);
  return null;
}

async function ensureInvoke() {
  if (_invoke) return _invoke;
  if (!IS_TAURI) return null;

  // ① 注入的全局 API（正常路径）
  const inj = nativeInvoke();
  if (inj) {
    _invoke = inj;
    return _invoke;
  }
  // ② 兜底：将来若接入打包器，npm 包可用
  try {
    const mod = await import('@tauri-apps/api/core');
    _invoke = mod.invoke;
  } catch (e) {
    sysWarn('无法获取 Tauri invoke：' + e.message);
  }
  return _invoke;
}

function sysWarn(m) {
  try { console.warn('[api]', m); } catch (e) { /* ignore */ }
}

/** 统一调用入口。tauri 不可用时走本地桥接服务 */
export async function call(cmd, args = {}) {
  const invoke = await ensureInvoke();
  if (invoke) {
    try {
      return await invoke(cmd, args);
    } catch (e) {
      throw new Error(typeof e === 'string' ? e : (e.message || String(e)));
    }
  }

  // ---- Web 降级：交给本地桥接服务（tools/dev_bridge.py）----
  try {
    const r = await fetch('/api/' + cmd, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(args),
    });
    const j = await r.json();
    if (j && j.ok === false) throw new Error(j.error || '未知错误');
    _bridgeDead = false;
    return j;
  } catch (e) {
    // 关键区分：桥接服务没启动 ≠ 业务逻辑出错。
    // 前者要给出「怎么启动」的指引，后者才显示错误详情。
    const networkFail = e instanceof TypeError
      || /Failed to fetch|NetworkError|ERR_CONNECTION/i.test(e.message || '');
    if (networkFail) {
      if (!_bridgeDead) {
        _bridgeDead = true;
        if (_onBridgeError) _onBridgeError();
      }
      throw new Error('桥接服务未启动');
    }
    throw e;
  }
}

/** 判断当前环境是否具备原生能力 */
export function isNative() { return IS_TAURI; }

/** 桥接服务是否确认不可用（main.js 用它决定是否显示引导） */
export function isBridgeDead() { return _bridgeDead; }

/**
 * 探测桥接服务是否可达。
 * 用于启动时先探一次，避免在加载每个视图时才被动失败。
 */
export async function probeBridge() {
  if (IS_TAURI) return true;
  try {
    const r = await fetch('/api/py_health', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: '{}',
    });
    const j = await r.json();
    return j && j.ok === true;
  } catch (e) {
    return false;
  }
}

export const api = {
  health:   () => call('py_health'),
  list:     (o = {}) => call('py_list', o),
  stats:    () => call('py_stats'),
  compose:  (config) => call('py_compose', { config: JSON.stringify(config) }),
  extract:  (pdf, subject) => call('py_extract', { pdf, subject }),
  exportHtml: (ids, outdir, title) =>
    call('py_export_html', { ids: JSON.stringify(ids),
                             outdir, title: title || null }),
  // Word 导出：可二次编辑（改分值、换选项、加批注），
  // 公式是原生 OMML，在 Word 里双击即可编辑。
  exportDocx: (ids, outdir, title) =>
    call('py_export_docx', { ids: JSON.stringify(ids),
                             outdir, title: title || null }),
  exportAnswer: (ids, outdir, title) =>
    call('py_export_answer', { ids: JSON.stringify(ids),
                               outdir, title: title || null }),
  progress: (items) => call('py_progress', { payload: JSON.stringify(items) }),
  due:      () => call('py_due'),
  backup:   (outdir) => call('py_export_progress', { outdir: outdir || null }),
  syncExcel: (path) => call('py_sync_excel', { path: path || null }),
  // 知识点讲解（教辅提分秘籍，按层级取）
  kpNotes: (subject, l1, l2, topic) =>
    call('py_kp_notes', { subject: subject || '数学', l1: l1 || null,
                          l2: l2 || null, topic: topic || null }),
  kpNotesStats: () => call('py_kp_notes_stats'),
  // 参考题目正文（典例/变式，含详解），点开时才加载
  refQuestions: (ids) =>
    call('py_ref_questions', { ids: (ids || []).join(',') }),
  // 批次：分次导入的题目可整批筛选/删除
  batchList: () => call('py_batch_list'),
  batchTag: (name, ids, batchId, src) =>
    call('py_batch_tag', { name: name || null, ids: ids || null,
                           batchId: batchId || null, src: src || null }),
  batchDelete: (batch) => call('py_batch_delete', { batch }),
  // 复习参数（记忆曲线阶梯、组卷配比等）
  gradeUsage: () => call('py_grade_usage'),
  getConfig: () => call('py_get_config'),
  setConfig: (config) =>
    call('py_set_config', { config: JSON.stringify(config) }),
  kpCatalog: (subject) => call('py_kp_catalog', { subject: subject || null }),
  // 题型节点：多对多标签，一个题目可挂多个，一个题型可挂多个题目
  topicList: (subject, l1, l2, hasQs) =>
    call('py_topic_list', { subject: subject || null, l1: l1 || null,
                            l2: l2 || null, hasQs: !!hasQs }),
  topicLink: (qid, topics) =>
    call('py_topic_link', { payload: JSON.stringify({ qid, topics }) }),
  questionTopics: (qid) => call('py_question_topics', { qid }),
  // 批量设置考试类型（mode: replace / add / remove）
  examTag: (ids, exams, mode) =>
    call('py_exam_tag', { ids: (ids || []).join(','),
                          exams: (exams || []).join(','),
                          mode: mode || 'replace' }),
  // 组卷前预览：取勾选题型下的**全部**题目（不抽题、不洗牌）
  topicQuestions: (topics, subject, limit) =>
    call('py_topic_questions', { topics: (topics || []).join(','),
                                 subject: subject || null,
                                 limit: limit || 200 }),
  paths:    () => call('app_paths'),
};

/**
 * 调用 dialog 插件的命令。
 * 直接走 invoke('plugin:dialog|xxx')，同样是零构建下的唯一可行方式。
 */
async function dialogCmd(action, options) {
  const invoke = await ensureInvoke();
  if (!invoke) return null;
  try {
    return await invoke('plugin:dialog|' + action, { options: options || {} });
  } catch (e) {
    sysWarn('dialog ' + action + ' 失败：' + e.message);
    return null;
  }
}

/** 原生文件对话框（保存/打开），非 Tauri 环境返回 null 由调用方处理 */
export async function pickSaveFile(defaultName) {
  if (!IS_TAURI) return null;
  return await dialogCmd('save', { defaultPath: defaultName });
}

export async function pickOpenFile(filters) {
  if (!IS_TAURI) return null;
  return await dialogCmd('open', { multiple: false, filters });
}

export async function pickDirectory() {
  if (!IS_TAURI) return null;
  return await dialogCmd('open', { directory: true, multiple: false });
}

export async function notify(title, body) {
  if (!IS_TAURI) { console.log(title, body); return; }
  await dialogCmd('message', { title, kind: 'info' , message: body});
}
