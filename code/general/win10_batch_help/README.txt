Get user input
	set /p input="Input: "
	echo %input%

Set variable to command output
	for /f %%f in ('command') do (
		set var=%%f
	)
	for /f "tokens=* USEBACKQ" %%f in (`command`) do (
		set var=%%f
	)

For loop
	for /l %%a in (1, 1, 200) do (
		echo %%a
	)
	for %%file in (directory\*.*) do (
		echo %%file
	)
