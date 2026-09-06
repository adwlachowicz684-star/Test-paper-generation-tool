@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"
set REPO_URL=https://github.com/adwlachowicz684-star/Test-paper-generation-tool.git

echo ^>^>^> 目标仓库: %REPO_URL%
git init
git remote remove origin 2>nul
git remote add origin %REPO_URL%
git add -A
git -c user.name=adwlachowicz684-star -c user.email=adwlachowicz684-star@users.noreply.github.com commit -m "整理项目结构：扁平化上传，移除重复的旧 README 与缓存文件"
git branch -M main
echo ^>^>^> 正在推送，弹出窗口时输入 GitHub 用户名 + Personal Access Token
git push -u origin main --force
echo ^>^>^> 完成
pause
