@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo.
echo   高考组卷 - 一键预览
echo   ------------------------------
echo   文件变动会自动刷新，改完不用手动刷新
echo   打印请按 Ctrl+P（图片公式均为矢量）
echo   关闭此窗口即停止预览
echo   ------------------------------
echo.
python tools\preview.py
if errorlevel 1 (
  echo.
  echo   启动失败。请确认已安装 Python 3.8+ 并勾选 Add to PATH
  echo   下载地址：https://www.python.org/downloads/
  pause
)
