#!/usr/bin/env bash
# 用法：把本文件连同本目录所有内容，放进你的仓库本地克隆里，然后 ./推送到GitHub.sh
set -e
REPO_URL="${1:-https://github.com/adwlachowicz684-star/Test-paper-generation-tool.git}"
BRANCH="${2:-main}"

echo ">>> 目标仓库: $REPO_URL (分支 $BRANCH)"

git init -q 2>/dev/null || true
git remote remove origin 2>/dev/null || true
git remote add origin "$REPO_URL"

git add -A
git -c user.name="adwlachowicz684-star" -c user.email="adwlachowicz684-star@users.noreply.github.com" \
    commit -q -m "整理项目结构：扁平化上传，移除重复的旧 README 与缓存文件" 2>/dev/null \
    || echo "（没有需要提交的改动）"

git branch -M "$BRANCH"
echo ">>> 正在推送，弹出窗口时输入 GitHub 用户名 + Personal Access Token"
git push -u origin "$BRANCH" --force
echo ">>> 完成，去仓库页面刷新看看"
