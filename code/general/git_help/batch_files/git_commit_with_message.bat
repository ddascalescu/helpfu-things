@echo off
set /p message="Message: "
git commit -a -m "%message%"
pause
