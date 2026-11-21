@echo off
chcp 65001 >nul
title Auto Trade Mail - 自动化外贸发信工作站
echo ====================================================================
echo  正在启动 Auto Trade Mail 本地外贸自动化工作站...
echo ====================================================================

cd /d "%~dp0"

start "" "http://127.0.0.1:8765"
python server.py

pause
