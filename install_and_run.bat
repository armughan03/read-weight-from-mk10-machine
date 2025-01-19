@echo off

SET MINICONDA_INSTALLER=Miniconda3-latest-Windows-x86_64.exe
SET MINICONDA_DIR=%USERPROFILE%\miniconda3

REM Step 1: Check if Miniconda is already installed
IF NOT EXIST "%MINICONDA_DIR%\Scripts\conda.exe" (
    echo Miniconda not found. Downloading Miniconda3...
    curl -L -o %MINICONDA_INSTALLER% https://repo.anaconda.com/miniconda/%MINICONDA_INSTALLER%

    REM Step 2: Install Miniconda3 silently
    echo Installing Miniconda3...
    start /wait %MINICONDA_INSTALLER% /S /D=%USERPROFILE%\miniconda3
) ELSE (
    echo Miniconda is already installed.
)

REM Step 3: Add Miniconda to the PATH (this only affects the current session)
set PATH=%MINICONDA_DIR%;%MINICONDA_DIR%\Scripts;%PATH%

REM Step 4: Initialize Miniconda (only if not already initialized)
IF NOT EXIST "%USERPROFILE%\miniconda3\Scripts\conda.exe" (
    echo Initializing Miniconda...
    call %MINICONDA_DIR%\Scripts\conda init
)

REM Step 5: Update Conda to the latest version
echo Updating Conda...
call conda update -y conda

REM Step 6: Check if the environment exists
IF NOT EXIST "%MINICONDA_DIR%\envs\myenv" (
    echo Creating a Conda environment named 'myenv'...
    call conda create -y -n myenv python=3.11
) ELSE (
    echo Conda environment 'myenv' already exists.
)

REM Step 7: Activate the Conda environment
echo Activating the Conda environment...
call conda activate myenv

REM Step 8: Install dependencies from requirements.txt
echo Installing packages from requirements.txt...
call pip install -r requirements.txt

REM Step 9: Go to the server directory
cd server

REM Step 10: Run the server
echo Running the server...
call uvicorn app:app --host 0.0.0.0 --port 9999

echo Server started.
pause
