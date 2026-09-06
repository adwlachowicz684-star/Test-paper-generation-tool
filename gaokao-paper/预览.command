#!/bin/bash
cd "$(dirname "$0")"
echo ""
echo "  高考组卷 - 一键预览"
echo "  ------------------------------"
echo "  文件变动会自动刷新"
echo "  打印请按 Cmd+P"
echo "  关闭此窗口即停止预览"
echo "  ------------------------------"
echo ""
python3 tools/preview.py
echo ""
read -n 1 -s -r -p "  按任意键关闭..."
