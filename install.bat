@echo off
REM Windows batch file to install dependencies
echo Installing dependencies for RPS World...
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo Failed to create virtual environment.
        echo Please ensure Python is installed correctly.
        pause
        exit /b 1
    )
)

REM Activate virtual environment and install
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Installing required packages...
pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo Installation failed. Please check error messages above.
    pause
    exit /b 1
)

echo.
echo ========================================
echo Installation complete!
echo ========================================
echo.
echo To run the application:
echo   1. Activate the virtual environment: venv\Scripts\activate
echo   2. Run the app: python run.py
echo.
echo Or simply double-click run.bat
echo.
pause

