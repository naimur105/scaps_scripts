@echo off
setlocal

set "python_exe=python"  REM Change this if your Python executable is named differently
set "script_file=update_maxiter.py"  REM Replace this with the actual script filename

REM Run the Python script
"%python_exe%" "%script_file%"

REM Close the console window automatically
ping 127.0.0.1 -n 2 > nul