@echo off
chcp 65001 >nul
title Auto Trade Mail + Cloudflare Tunnel
echo ================================================================
echo  Auto Trade Mail - 自动化外贸开发信工作站 (Cloudflare 全球部署版)
echo ================================================================
echo.

cd /d "%~dp0"

echo [1/2] 正在启动本地 Python Web 服务 (端口 8765)...
start /b python server.py

echo [2/2] 正在建立 Cloudflare 安全加密隧道...
echo 稍等 3~5 秒，Cloudflare 将为您生成公网 HTTPS 访问域名：
echo.

.\cloudflared.exe tunnel --protocol http2 --url http://localhost:8765

pause
