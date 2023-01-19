@echo off

call %~dp0telegram_bot\venv\Scripts\activate

cd %~dp0telegram_bot

set TOKEN=5884044111:AAHJPaabyvwrHRmfm-lrRKouMkZSJiXIeoY

python bot_telegram.py

pause