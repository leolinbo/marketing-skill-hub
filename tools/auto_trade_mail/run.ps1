# PowerShell 快速启动脚本
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

Write-Host "====================================================================" -ForegroundColor Cyan
Write-Host " 正在启动 Auto Trade Mail 本地外贸自动化工作站..." -ForegroundColor Green
Write-Host " Web 控制台地址: http://127.0.0.1:8765" -ForegroundColor Yellow
Write-Host "====================================================================" -ForegroundColor Cyan

Start-Process "http://127.0.0.1:8765"
python server.py
