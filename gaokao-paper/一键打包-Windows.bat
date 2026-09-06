@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"

echo ============================================================
echo   高考组卷 -- Windows 一键打包
echo ============================================================
echo.

REM ---------- 1. 检查 Node ----------
where node >nul 2>nul
if errorlevel 1 (
    echo [X] 没找到 Node.js
    echo.
    echo     请先安装 Node.js 20 或更高版本：
    echo         https://nodejs.org/zh-cn/download
    echo     安装时一路下一步即可，装完重新双击本文件。
    echo.
    pause & exit /b 1
)
for /f "tokens=*" %%v in ('node -v') do set NODEV=%%v
echo [OK] Node %NODEV%

REM ---------- 2. 检查 Rust ----------
where cargo >nul 2>nul
if errorlevel 1 (
    echo [X] 没找到 Rust 工具链
    echo.
    echo     请先安装 Rust（约 5 分钟）：
    echo         1. 打开 https://rustup.rs
    echo         2. 下载 rustup-init.exe 并运行
    echo         3. 出现选项时直接按回车用默认配置
    echo         4. 装完**重新打开一个命令行窗口**再双击本文件
    echo.
    echo     注意：安装程序会提示需要 Visual Studio 生成工具，
    echo           选 "1" 让它自动安装（约 2GB，必须装，否则编译不了）
    echo.
    pause & exit /b 1
)
for /f "tokens=1,2" %%a in ('cargo -V') do set CARGOV=%%a %%b
echo [OK] %CARGOV%

REM ---------- 3. 装依赖 ----------
echo.
echo [3/5] 安装前端依赖（首次约 1 分钟）...
call npm install --no-audit --no-fund
if errorlevel 1 (
    echo [X] 依赖安装失败，检查网络后重试
    pause & exit /b 1
)
echo [OK] 依赖就绪

REM ---------- 4. 编译 ----------
echo.
echo [4/5] 编译打包（首次约 5-15 分钟，请耐心等待）...
call npm run tauri build
if errorlevel 1 (
    echo.
    echo [X] 编译失败。常见原因：
    echo        - 没装 Visual Studio 生成工具（C++ 桌面开发）
    echo        - 杀毒软件拦截了编译过程
    echo        - 磁盘空间不足（需 5GB 以上）
    echo.
    pause & exit /b 1
)
echo [OK] 编译完成

REM ---------- 5. 收尾 ----------
echo.
echo [5/5] 打包完成！
echo.
set "OUT=%~dp0src-tauri\target\release\bundle\nsis"
if exist "%OUT%" (
    echo     安装程序位置：
    dir /b "%OUT%\*.exe" 2>nul
    echo.
    echo     完整路径：%OUT%
) else (
    echo     未找到 nsis 目录，请查看 src-tauri\target\release\bundle\
)

echo.
echo ============================================================
echo   说明
echo ============================================================
echo   1. 生成的是**安装程序**，不是免安装单文件 exe。
echo      这是 Tauri/WebView 架构决定的 —— 程序依赖
echo      WebView2 运行时，无法压成单个自包含文件。
echo.
echo   2. 目标电脑需要 WebView2：
echo      - Windows 11：系统自带，不用管
echo      - Windows 10：多数已随系统更新装上；
echo        若打不开，装 https://go.microsoft.com/fwlink/p/?LinkId=2124703
echo.
echo   3. 程序已内置 Python 题库逻辑，目标电脑**不需要装 Python**。
echo      若想用「导入 PDF」功能才需要额外配置 Python 环境。
echo ============================================================
echo.
pause
