/* ============================================================
   判分逻辑
   支持：单选、多选（部分分）、填空、解答（自评）
   ============================================================ */

const MULTI_SCORE = { full: 5, partial: 2 };

/** 规范化答案：去空格、统一大写、去句号 */
function norm(s) {
  return String(s == null ? '' : s)
    .replace(/[\s\u3000]/g, '')
    .replace(/[．.、,，;；]/g, '')
    .toUpperCase();
}

/**
 * 填空题专用的轻量清洗。
 *
 * 不能直接用 norm()：norm 会删掉 `.`，
 * 导致 0.75 → 075、3.5 → 35，小数全部判错。
 * 这里只去掉：空白、末尾/孤立的中英文句号、多余括号。
 */
function fillKey(s) {
  return String(s == null ? '' : s)
    .replace(/[\s\u3000]/g, '')       // 空白
    .replace(/[．。]$/g, '')            // 末尾句号
    .replace(/[（）()]/g, '')           // 括号
    .toUpperCase();
}

/** 判断题型细分是否为多选 */
function isMulti(q) {
  const st = (q.subtype || '') + (q.type || '');
  return /多选/.test(st);
}

/**
 * 判分
 * @returns {object} { correct, partial, score, fullScore, expect, given }
 */
export function grade(q, given) {
  const expect = q.answer || '';
  const full = q.score || (q.type === '选择' ? 5 : (q.type === '填空' ? 5 : 12));

  // 无答案（数学卷原卷不含答案）→ 只能自评
  if (!expect || String(expect).includes('原卷无答案')) {
    return { correct: null, partial: false, score: 0, fullScore: full,
             expect: '(原卷无答案)', given: given, needSelf: true };
  }

  if (q.type === '选择') {
    const e = norm(expect), g = norm(given);
    if (!g) return { correct: false, partial: false, score: 0, fullScore: full,
                     expect, given, needSelf: false };
    if (isMulti(q) || e.length > 1) {
      // 多选：全部命中得满分，部分命中且无错选得部分分
      const es = new Set(e.split('')), gs = new Set(g.split(''));
      let hit = 0, wrong = 0;
      for (const c of gs) { if (es.has(c)) hit++; else wrong++; }
      if (wrong > 0) {
        return { correct: false, partial: false, score: 0, fullScore: full,
                 expect, given, needSelf: false };
      }
      if (hit === es.size) {
        return { correct: true, partial: false, score: MULTI_SCORE.full,
                 fullScore: MULTI_SCORE.full, expect, given, needSelf: false };
      }
      return { correct: false, partial: true, score: MULTI_SCORE.partial,
               fullScore: MULTI_SCORE.full, expect, given, needSelf: false };
    }
    // 单选
    return { correct: g === e, partial: false, score: g === e ? full : 0,
             fullScore: full, expect, given, needSelf: false };
  }

  if (q.type === '填空') {
    const r = gradeFill(expect, given);
    return { correct: r.correct, partial: r.partial,
             score: r.correct ? full : (r.partial ? Math.round(full / 2) : 0),
             fullScore: full, expect, given, needSelf: false };
  }

  // 解答题：程序无法自动判，交给自评
  return { correct: null, partial: false, score: 0, fullScore: full,
           expect, given, needSelf: true };
}

/**
 * 填空题判分
 *
 * 之前用 `e.includes(g) || g.includes(e)`，导致：
 *   答案是 12，学生答 1 → "12".includes("1") → 判为正确
 *   答案是 -3，学生答 3 → 判为正确
 * 后果很严重：孩子一直被判对，错题进不了复习队列，
 * 整套间隔复习系统失效。
 *
 * 改为：
 *   1. 按分隔符拆成多个空，逐个比对
 *   2. 优先数值比较（3/4 与 6/8 视为相等）
 *   3. 数值不可比时退回字符串精确匹配
 *   4. 多空题允许部分正确（对新高考填空题的部分分场景）
 */
function splitBlanks(s) {
  // 注意：不要把 / 当分隔符！
  // 否则分数 3/4 会被拆成 ["3","4"]，判分全错。
  // 多空答案用中文分号、逗号、顿号或竖线分隔即可。
  return String(s == null ? '' : s)
    .split(/[；;，,、｜|]+/)
    .map(x => x.trim())
    .filter(x => x !== '');
}

/** 尝试解析成分数或小数，失败返回 null */
function asNum(s) {
  const t = String(s).replace(/[\s]/g, '');
  if (t === '') return null;
  // 分数 a/b
  let m = t.match(/^(-?\d+)\s*\/\s*(-?\d+)$/);
  if (m) {
    const d = parseFloat(m[2]);
    if (d === 0) return null;
    return parseFloat(m[1]) / d;
  }
  // 负分数 -(a/b)
  m = t.match(/^-\s*\(\s*(\d+)\s*\/\s*(\d+)\s*\)$/);
  if (m) {
    const d = parseFloat(m[2]);
    if (d === 0) return null;
    return -parseFloat(m[1]) / d;
  }
  // 小数 / 整数（含负号）
  if (/^-?\d+(\.\d+)?$/.test(t)) return parseFloat(t);
  return null;
}

function oneBlankMatch(exp, giv) {
  if (exp === giv) return true;
  const ne = asNum(exp), ng = asNum(giv);
  if (ne !== null && ng !== null) {
    return Math.abs(ne - ng) < 1e-9;
  }
  // 非数值：忽略大小写与空格后再比一次（如 选项字母、符号答案）
  return exp.replace(/\s/g, '').toLowerCase()
      === giv.replace(/\s/g, '').toLowerCase();
}

function gradeFill(expect, given) {
  const es = splitBlanks(fillKey(expect));
  const gs = splitBlanks(fillKey(given));
  if (!es.length) return { correct: false, partial: false };
  if (!gs.length) return { correct: false, partial: false };

  // 单空：直接比对
  if (es.length === 1) {
    const ok = oneBlankMatch(es[0], gs[0]);
    return { correct: ok, partial: false };
  }

  // 多空：按位置比对，全对才满分
  let hit = 0;
  for (let i = 0; i < Math.min(es.length, gs.length); i++) {
    if (oneBlankMatch(es[i], gs[i])) hit++;
  }
  if (hit === es.length && gs.length === es.length) {
    return { correct: true, partial: false };
  }
  return { correct: false, partial: hit > 0 };
}

/** 汇总一卷 */
export function summarize(results) {
  let got = 0, full = 0, nRight = 0, nPartial = 0, nWrong = 0, nSelf = 0;
  for (const r of results) {
    full += r.fullScore || 0;
    got += r.score || 0;
    if (r.needSelf) nSelf++;
    else if (r.correct) nRight++;
    else if (r.partial) nPartial++;
    else nWrong++;
  }
  return { got, full, nRight, nPartial, nWrong, nSelf,
           rate: full ? Math.round(got / full * 100) : 0,
           acc: (nRight + nPartial + nWrong)
                 ? Math.round(nRight / (nRight + nPartial + nWrong) * 100) : 0 };
}
