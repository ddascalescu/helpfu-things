@echo off
set /p file="File: "
for /f %%f in ('git rev-parse --show-toplevel') do (
	set base=%%f
)
git add %base%/%file%
pause
