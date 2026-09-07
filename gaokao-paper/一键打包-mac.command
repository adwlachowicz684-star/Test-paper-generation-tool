#!/bin/bash
cd "$(dirname "$0")"
clear
echo "============================================================"
echo "  高考组卷 -- macOS 一键打包"
echo "============================================================"
echo

# 1. Node
if ! command -v node >/dev/null 2>&1; then
    echo "[X] 没找到 Node.js"
    echo "    请先安装：https://nodejs.org/zh-cn/download"
    echo "    或用 Homebrew：brew install node"
    read -p "按回车退出…"; exit 1
fi
echo "[OK] Node $(node -v)"

# 2. Rust
if ! command -v cargo >/dev/null 2>&1; then
    echo "[X] 没找到 Rust"
    echo "    请执行这条命令安装（约 5 分钟）："
    echo "        curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh"
    echo "    装完重新打开终端，再双击本文件。"
    read -p "按回车退出…"; exit 1
fi
echo "[OK] $(cargo -V)"

# 3. Xcode 命令行工具
if ! xcode-select -p >/dev/null 2>&1; then
    echo "[!] 需要 Xcode 命令行工具，正在安装…"
    xcode-select --install
    echo "    请在弹出的窗口里点「安装」，完成后重新运行本脚本。"
    read -p "按回车退出…"; exit 1
fi
echo "[OK] Xcode 命令行工具已就绪"

# 4. 依赖
echo
echo "[4/5] 安装前端依赖（首次约 1 分钟）…"
npm install --no-audit --no-fund || { echo "[X] 依赖安装失败"; read -p "按回车退出…"; exit 1; }
echo "[OK] 依赖就绪"

# 5. 编译
echo
echo "[5/5] 编译打包（首次约 5-15 分钟）…"
npm run tauri build || {
    echo "[X] 编译失败"
    read -p "按回车退出…"; exit 1
}

echo
echo "============================================================"
echo "  打包完成"
echo "============================================================"
DMG="src-tauri/target/release/bundle/dmg"
if [ -d "$DMG" ]; then
    echo "生成文件："
    ls -1 "$DMG"/*.dmg 2>/dev/null | xargs -n1 basename
    echo
    echo "完整路径：$PWD/$DMG"
    echo
    echo "提示：.app 在 src-tauri/target/release/bundle/macos/ 下，"
    echo "      日常使用直接拷贝 .app 到「应用程序」即可，不必用 dmg。"
fi
echo
echo "首次打开若提示「无法验证开发者」，请："
echo "    右键点击 → 打开 → 确认"
echo "============================================================"
read -p "按回车退出…"
