@echo off
:start
echo Starting Server...
python mvp_server.py
echo Server stopped. Press any key to restart...
pause
goto start
