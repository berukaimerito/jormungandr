@echo off
REM This batch file passes all command-line arguments to the Python script

REM Check if Python is available
where python >nul 2>&1
IF ERRORLEVEL 1 (
    ECHO Python is not installed or not found in PATH.
    EXIT /B 1
)

REM Execute the Python script with all passed arguments
python ransom.py %*
