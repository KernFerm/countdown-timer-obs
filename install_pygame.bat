@echo off
setlocal

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python and try again.
    exit /b 1
)

REM Check if pip is installed
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo pip is not installed. Installing pip...
    python -m ensurepip --upgrade
)

REM Install pygame==2.1.0
echo Installing pygame version 2.1.0...
pip install pygame==2.1.0

REM Check if the installation was successful
if %errorlevel% neq 0 (
    echo Failed to install pygame.
    exit /b 1
) else (
    echo pygame version 2.1.0 installed successfully.
)

endlocal
pause
