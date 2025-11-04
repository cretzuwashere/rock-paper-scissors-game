@echo off
REM Windows batch file to run tests
echo Running RPS World test suite...
echo.

if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
)

python run_tests.py

if errorlevel 1 (
    echo.
    echo Tests failed. Please review the output above.
) else (
    echo.
    echo All tests passed!
)

echo.
pause

