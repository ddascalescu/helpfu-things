@echo off
for /f "tokens=* USEBACKQ" %%f in (`git rev-parse --show-toplevel`) do (
	set base=%%f
)
git restore --staged %base%
pause
