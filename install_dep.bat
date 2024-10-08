@echo off
REM Check if Python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python and try again.
    exit /b 1
)

REM Create a virtual environment
python -m venv venv
IF %ERRORLEVEL% NEQ 0 (
    echo Failed to create a virtual environment.
    exit /b 1
)

echo Virtual environment created successfully.

REM Activate the virtual environment
CALL venv\Scripts\activate

IF %ERRORLEVEL% NEQ 0 (
    echo Failed to activate the virtual environment.
    exit /b 1
)

echo Virtual environment activated successfully.

REM Optional: Upgrade pip in the virtual environment
python -m pip install --upgrade pip
IF %ERRORLEVEL% EQU 0 (
    echo Pip upgraded successfully.
) ELSE (
    echo Failed to upgrade pip.
)

REM Optional: Install requirements from requirements.txt if it exists
IF EXIST requirements.txt (
    python -m pip install -r requirements.txt
    IF %ERRORLEVEL% EQU 0 (
        echo Requirements installed successfully.
    ) ELSE (
        echo Failed to install requirements.
    )
)

REM Keep the command prompt open after the script executes
cmd /k
