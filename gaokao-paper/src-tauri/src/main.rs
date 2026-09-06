// 防止 Windows 下启动时弹出控制台窗口
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

fn main() {
    gaokao_paper_lib::run()
}
