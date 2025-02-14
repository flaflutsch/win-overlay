@echo off
REM Change to the desired directory
cd /d "C:\Dev\win-overlay"

REM Check if the virtual environment directory exists
if not exist ".venv\Scripts\activate.bat" (
    echo Virtual environment not found. Please ensure it is set up correctly.
    exit /b 1
)

REM Activate the Python virtual environment
call .venv\Scripts\activate

REM Check if the activation was successful
if "%VIRTUAL_ENV%"=="" (
    echo Failed to activate the virtual environment.
    exit /b 1
)

REM Execute the Python script
start /B pythonw main.py

REM Optional: Deactivate the virtual environment after running the script
call .venv\Scripts\deactivate.bat