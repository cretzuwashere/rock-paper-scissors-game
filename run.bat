@echo off
REM Windows batch file to run RPS World
echo Starting Rock-Paper-Scissors World...
python run.py
if errorlevel 1 (
    echo.
    echo Python is not found or an error occurred.
    echo Please ensure Python is installed and in your PATH.
    echo.
    pause
)

