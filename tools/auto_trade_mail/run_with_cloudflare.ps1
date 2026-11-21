# Auto Trade Mail + Cloudflare Tunnel 一键启动脚本
$Host.UI.RawUI.WindowTitle = "Auto Trade Mail + Cloudflare Tunnel"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

Write-Host "================================================================" -ForegroundColor Cyan
Write-Host " Auto Trade Mail - 自动化外贸开发信工作站 (Cloudflare 全球部署版)" -ForegroundColor Cyan
Write-Host "================================================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "[1/2] 正在启动本地 Python Web 服务 (端口 8765)..." -ForegroundColor Yellow
Start-Process -FilePath "python" -ArgumentList "server.py" -WindowStyle Hidden

Start-Sleep -Seconds 2

Write-Host "[2/2] 正在建立 Cloudflare 安全加密隧道..." -ForegroundColor Yellow
Write-Host "稍等 3~5 秒，Cloudflare 将为您生成全球公网 HTTPS 访问域名：" -ForegroundColor Green
Write-Host ""

& ".\cloudflared.exe" tunnel --protocol http2 --url http://localhost:8765
