//! 题库 / 组卷 / 练习记录 —— 全部通过调用 Python 桥接层完成。
//!
//! 设计：Rust 只做「进程调度 + 数据透传 + 路径管理」，
//! 业务逻辑留在 Python（已有大量验证过的正则与几何算法）。
//! 这样两边都能独立测试，也避免用 Rust 重写一遍 PDF 解析。

use std::path::PathBuf;
use std::process::Command;
use serde::Serialize;
use serde_json::Value;

/// Python 解释器候选。**返回顺序即优先级，不要随意调整**：
///
///   1. `GAOKAO_PYTHON` 环境变量 —— 优先级最高。
///      指定虚拟环境或自定义安装路径时用，也是调试时最快的切换手段。
///      放在第一位是因为：用户显式指定的意图应当压过一切自动探测。
///   2. 打包内置的 `py/bin/python3` —— 分发版本应当命中这个，
///      不依赖用户装没装 Python、装的是哪个版本。
///   3. `python3` —— 系统默认（macOS / Linux）
///   4. `python`  —— Windows 上通常只有这个名字
///
/// 候选里允许包含不存在的路径：`run_py` 会逐个尝试并跳过失败项，
/// 全部失败时把最后一条 stderr 报出来。
///
/// 注意：不要在这里预先做 `exists()` 过滤 ——
/// 打包后资源解压时机晚于本函数调用，过滤会误判成「没有解释器」。
fn python_candidates() -> Vec<String> {
    let mut v = Vec::new();

    // ① 环境变量指定（虚拟环境 / 自定义路径）
    if let Ok(p) = std::env::var("GAOKAO_PYTHON") {
        let p = p.trim().to_string();
        if !p.is_empty() {
            v.push(p);
        }
    }

    // ② 打包内置解释器（同样要覆盖 macOS 的 Resources 布局）
    if let Ok(exe) = std::env::current_exe() {
        if let Some(dir) = exe.parent() {
            v.push(dir.join("py").join("bin").join("python3")
                     .to_string_lossy().to_string());
            v.push(dir.join("..").join("Resources").join("py")
                     .join("bin").join("python3")
                     .to_string_lossy().to_string());
        }
    }

    // ③④ 系统解释器
    v.push("python3".into());
    v.push("python".into());
    v
}

/// 定位 py/main.py
///
/// 各平台的资源布局不同，必须逐个尝试：
///
/// | 平台 | exe 位置 | resources 位置 |
/// |---|---|---|
/// | Windows | 安装根目录 | 与 exe 同级 |
/// | Linux | /usr/bin 或 AppDir | 与 exe 同级 |
/// | **macOS** | `xxx.app/Contents/MacOS/` | **`xxx.app/Contents/Resources/`** |
///
/// macOS 是唯一的例外：exe 和 resources 不在同一层，
/// 少了 `../Resources` 这一次尝试，打包后必然找不到脚本。
fn script_path() -> Result<PathBuf, String> {
    if let Ok(exe) = std::env::current_exe() {
        if let Some(dir) = exe.parent() {
            // Windows / Linux：resources 与 exe 同级
            let p = dir.join("py").join("main.py");
            if p.exists() {
                return Ok(p);
            }
            // macOS .app：resources 在 Contents/Resources/
            let p = dir.join("..").join("Resources").join("py").join("main.py");
            if p.exists() {
                return Ok(p);
            }
        }
    }
    // 开发环境：CARGO_MANIFEST_DIR/../py/main.py
    let p = PathBuf::from(env!("CARGO_MANIFEST_DIR"))
        .join("..").join("py").join("main.py");
    if p.exists() {
        return Ok(p);
    }
    Err("找不到 py/main.py。请确认 Python 处理层已随应用分发。".into())
}

/// 调用 Python 桥接，解析其 stdout 里的 JSON
fn run_py(args: &[String]) -> Result<Value, String> {
    let script = script_path()?;
    let mut last_err = String::new();

    for py in python_candidates() {
        let out = Command::new(&py)
            .arg(&script)
            .args(args)
            .output();

        match out {
            Ok(o) if o.status.success() => {
                let text = String::from_utf8_lossy(&o.stdout);
                // Python 侧可能先打印调试信息，只取最后一行 JSON
                let line = text
                    .lines()
                    .rev()
                    .find(|l| l.trim_start().starts_with('{'))
                    .ok_or("Python 未输出 JSON")?;
                return serde_json::from_str(line)
                    .map_err(|e| format!("JSON 解析失败: {} | 原文: {}", e, line));
            }
            Ok(o) => {
                last_err = String::from_utf8_lossy(&o.stderr).to_string();
                if last_err.trim().is_empty() {
                    last_err = format!("退出码 {:?}", o.status.code());
                }
            }
            Err(e) => {
                last_err = e.to_string();
                continue;   // 该候选解释器不存在，试下一个
            }
        }
    }
    Err(format!("Python 调用失败: {}", last_err))
}

// ==================== Commands ====================

#[tauri::command]
fn py_health() -> Result<Value, String> {
    run_py(&["health".into()])
}

/// 列出题目。subject / q / limit 均为可选
#[tauri::command]
fn py_list(subject: Option<String>, q: Option<String>, limit: Option<i64>)
           -> Result<Value, String> {
    let mut a: Vec<String> = vec!["list".into()];
    if let Some(s) = subject { a.push("--subject".into()); a.push(s); }
    if let Some(s) = q       { a.push("--q".into());       a.push(s); }
    if let Some(n) = limit   { a.push("--limit".into());   a.push(n.to_string()); }
    run_py(&a)
}

#[tauri::command]
fn py_stats() -> Result<Value, String> {
    run_py(&["stats".into()])
}

/// 六科知识点标准目录。前端组卷页据此按科目渲染，
/// 选物理不会出现数学的「解析几何」。
#[tauri::command]
fn py_kp_catalog(subject: Option<String>) -> Result<Value, String> {
    let mut a: Vec<String> = vec!["kp-catalog".into()];
    if let Some(s) = subject {
        a.push("--subject".into());
        a.push(s);
    }
    run_py(&a)
}

/// 组卷。config 为 JSON 字符串
#[tauri::command]
fn py_compose(config: String) -> Result<Value, String> {
    run_py(&["compose".into(), "--config".into(), config])
}

/// 拆题入库。pdf 为绝对路径
#[tauri::command]
fn py_extract(pdf: String, subject: String) -> Result<Value, String> {
    run_py(&["extract".into(), "--pdf".into(), pdf,
             "--subject".into(), subject])
}

/// 导出试卷 HTML。ids 为 JSON 数组字符串
#[tauri::command]
fn py_export_html(ids: String, outdir: String, title: Option<String>)
                  -> Result<Value, String> {
    let mut a = vec!["export-html".into(), "--ids".into(), ids,
                     "--outdir".into(), outdir];
    if let Some(t) = title { a.push("--title".into()); a.push(t); }
    run_py(&a)
}

/// 导出试卷 Word（公式是原生 OMML，可在 Word 里双击编辑）
#[tauri::command]
fn py_export_docx(ids: String, outdir: String, title: Option<String>)
                  -> Result<Value, String> {
    let mut a = vec!["export-docx".into(), "--ids".into(), ids,
                     "--outdir".into(), outdir];
    if let Some(t) = title { a.push("--title".into()); a.push(t); }
    run_py(&a)
}

/// 导出答案与解析卷（Word）
#[tauri::command]
fn py_export_answer(ids: String, outdir: String, title: Option<String>)
                    -> Result<Value, String> {
    let mut a = vec!["export-answer".into(), "--ids".into(), ids,
                     "--outdir".into(), outdir];
    if let Some(t) = title { a.push("--title".into()); a.push(t); }
    run_py(&a)
}

/// 取知识点讲解（按 题型 > 小知识点 > 大知识点 优先）
#[tauri::command]
fn py_kp_notes(subject: Option<String>, l1: Option<String>,
               l2: Option<String>, topic: Option<String>) -> Result<Value, String> {
    let mut a = vec!["kp-notes".into()];
    if let Some(x) = subject { a.push("--subject".into()); a.push(x); }
    if let Some(x) = l1 { a.push("--l1".into()); a.push(x); }
    if let Some(x) = l2 { a.push("--l2".into()); a.push(x); }
    if let Some(x) = topic { a.push("--topic".into()); a.push(x); }
    run_py(&a)
}

/// 按题目 ID 取参考题目正文（含详解）
#[tauri::command]
fn py_ref_questions(ids: String) -> Result<Value, String> {
    run_py(&["ref-questions".into(), "--ids".into(), ids])
}

/// 知识点讲解覆盖统计
#[tauri::command]
fn py_kp_notes_stats() -> Result<Value, String> {
    run_py(&["kp-notes-stats".into()])
}

/// 列出所有批次（含实时题数）
#[tauri::command]
fn py_batch_list() -> Result<Value, String> {
    run_py(&["batch-list".into()])
}

/// 给现有题目打批次标记
#[tauri::command]
fn py_batch_tag(name: Option<String>, ids: Option<String>,
                batch_id: Option<String>, src: Option<String>) -> Result<Value, String> {
    // 注意：Tauri v2 默认把 Rust 的 snake_case 参数转为 camelCase 传给前端，
    // 但这里前端显式传 batch_id / has_qs 等 snake_case 键，
    // 与既有命令（py_topic_list 的 has_qs）保持一致。
    let mut a = vec!["batch-tag".into()];
    if let Some(x) = name { a.push("--name".into()); a.push(x); }
    if let Some(x) = ids { a.push("--ids".into()); a.push(x); }
    if let Some(x) = batch_id { a.push("--batch-id".into()); a.push(x); }
    if let Some(x) = src { a.push("--src".into()); a.push(x); }
    run_py(&a)
}

/// 按批次删除题目（高危：连带清理练习记录）
#[tauri::command]
fn py_batch_delete(batch: String) -> Result<Value, String> {
    run_py(&["batch-delete".into(), "--batch".into(), batch])
}

/// 读复习参数（记忆曲线阶梯、配比等）
#[tauri::command]
fn py_get_config() -> Result<Value, String> {
    run_py(&["get-config".into()])
}

/// 写复习参数（带校验，不通过则不落盘）
#[tauri::command]
fn py_set_config(config: String) -> Result<Value, String> {
    run_py(&["set-config".into(), "--config".into(), config])
}

/// 列题型节点（三级是实体，有 ID，多对多挂题目）
#[tauri::command]
fn py_topic_list(subject: Option<String>, l1: Option<String>,
                 l2: Option<String>, has_qs: bool) -> Result<Value, String> {
    let mut a = vec!["topic-list".into()];
    if let Some(x) = subject { a.push("--subject".into()); a.push(x); }
    if let Some(x) = l1 { a.push("--l1".into()); a.push(x); }
    if let Some(x) = l2 { a.push("--l2".into()); a.push(x); }
    if has_qs { a.push("--has-qs".into()); }
    run_py(&a)
}

/// 把题目挂到题型上（多对多，幂等）
#[tauri::command]
fn py_topic_link(payload: String) -> Result<Value, String> {
    run_py(&["topic-link".into(), "--payload".into(), payload])
}

/// 查某题挂了哪些题型
#[tauri::command]
fn py_question_topics(qid: String) -> Result<Value, String> {
    run_py(&["question-topics".into(), "--qid".into(), qid])
}

/// 写入练习结果（自动更新记忆曲线）
#[tauri::command]
fn py_progress(payload: String) -> Result<Value, String> {
    run_py(&["progress".into(), "--payload".into(), payload])
}

/// 到期需复习的题目
#[tauri::command]
fn py_due() -> Result<Value, String> {
    run_py(&["due".into()])
}

/// 备份练习记录 —— 防止浏览器/应用数据被清导致一学期错题历史丢失
#[tauri::command]
fn py_export_progress(outdir: Option<String>) -> Result<Value, String> {
    let mut a = vec!["export-progress".into()];
    if let Some(d) = outdir { a.push("--outdir".into()); a.push(d); }
    run_py(&a)
}

/// 从 Excel 同步人工校订的字段（知识点 / 难度 / 题型细分）回 JSON
#[tauri::command]
fn py_sync_excel(path: Option<String>) -> Result<Value, String> {
    let script = script_path()?;
    let sync = script
        .parent()
        .ok_or("脚本路径异常")?
        .join("sync_excel.py");
    let mut a: Vec<String> = Vec::new();
    if let Some(p) = path { a.push(p); }

    for py in python_candidates() {
        let out = Command::new(&py).arg(&sync).args(&a).output();
        if let Ok(o) = out {
            if o.status.success() {
                return Ok(serde_json::json!({
                    "ok": true,
                    "log": String::from_utf8_lossy(&o.stdout)
                }));
            } else {
                return Err(String::from_utf8_lossy(&o.stderr).to_string());
            }
        }
    }
    Err("找不到可用的 Python 解释器".into())
}

#[derive(Serialize)]
struct AppPaths {
    data_dir: String,
    bank: String,
    progress: String,
    slices: String,
}

/// 暴露数据目录，便于前端提示用户去哪里找文件
///
/// **不能用 `env!("CARGO_MANIFEST_DIR")`** —— 它在编译期就被替换成
/// 开发者机器上的源码路径，打包到用户电脑上后指向一个不存在的目录，
/// `canonicalize()` 直接失败。
///
/// 正确做法是用 Tauri 的 PathResolver，它会按平台返回真实的资源目录：
///   Windows / Linux → 与 exe 同级
///   macOS           → xxx.app/Contents/Resources/
#[tauri::command]
fn app_paths(app: tauri::AppHandle) -> Result<AppPaths, String> {
    // 开发与打包的布局不同，两者都要覆盖：
    //
    //   打包后：res = 安装目录（Win/Linux）或 Contents/Resources（macOS）
    //           → data 在 res/data
    //   开发时：res 可能指向 src-tauri/，那里没有 data/
    //           → 回退到 CARGO_MANIFEST_DIR/.. （即项目根）
    //
    // 必须与 py/main.py 的 DATA_DIR 指向同一处，
    // 否则界面上显示的数据目录是假的，家长照着找会找不到文件。
    let res = app.path()
        .resource_dir()
        .map_err(|e| format!("无法定位资源目录: {}", e))?;

    let dev_root = PathBuf::from(env!("CARGO_MANIFEST_DIR")).join("..");
    let root = if res.join("data").exists() {
        res.clone()
    } else if dev_root.join("data").exists() {
        dev_root
    } else {
        res.clone()
    };

    let data = root.join("data");
    Ok(AppPaths {
        data_dir: data.to_string_lossy().to_string(),
        bank: data.join("bank.json").to_string_lossy().to_string(),
        progress: data.join("progress.json").to_string_lossy().to_string(),
        slices: res.join("src").join("slices").to_string_lossy().to_string(),
    })
}

// ==================== 入口 ====================

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_dialog::init())
        .plugin(tauri_plugin_fs::init())
        .plugin(tauri_plugin_opener::init())
        .invoke_handler(tauri::generate_handler![
            py_health,
            py_list,
            py_stats,
            py_kp_catalog,
            py_compose,
            py_extract,
            py_export_html,
            py_export_docx,
            py_export_answer,
            py_kp_notes,
            py_kp_notes_stats,
            py_ref_questions,
            py_batch_list,
            py_batch_tag,
            py_batch_delete,
            py_get_config,
            py_set_config,
            py_topic_list,
            py_topic_link,
            py_question_topics,
            py_progress,
            py_due,
            py_export_progress,
            py_sync_excel,
            app_paths,
        ])
        .run(tauri::generate_context!())
        .expect("启动 Tauri 应用失败");
}
