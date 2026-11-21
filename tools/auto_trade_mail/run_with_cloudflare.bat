@echo off
chcp 65001 >nul
title Auto Trade Mail + Cloudflare Tunnel
echo ================================================================
echo  Auto Trade Mail - 自动化外贸开发信工作站 (Cloudflare 全球部署版)
echo ================================================================
echo.

cd /d "%~dp0"

REM 检查是否安装了 Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [错误] 未检测到 Python，请先下载并安装 Python 3 (记得勾选 Add Python to PATH)！
    pause
    exit /b
)

REM 检查并自动下载 cloudflared.exe
if not exist "cloudflared.exe" (
    echo [提示] 首次在此电脑运行，正在自动准备 Cloudflare 隧道组件 (约 40MB)...
    powershell -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri 'https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe' -OutFile 'cloudflared.exe'"
    if not exist "cloudflared.exe" (
        echo [警告] 自动下载失败，您可以直接使用本地模式: 双击 run.bat
    )
)

echo [1/2] 正在启动 Python 外贸邮件服务...
start /b python server.py

echo [2/2] 正在建立 Cloudflare 安全加密隧道...
echo 稍等 3~5 秒，Cloudflare 将为您生成全球公网 HTTPS 访问域名：
echo (局域网本地也可以随时打开: http://127.0.0.1:8765)
echo.

if exist "cloudflared.exe" (
    .\cloudflared.exe tunnel --protocol http2 --url http://localhost:8765
) else (
    start http://127.0.0.1:8765
    pause
)
