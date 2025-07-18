@echo off
title NaMo Framework Server AutoRun
color 0A

echo 🚀 Checking Python installation...
python --version || (
    echo ❌ Python not found. Please install Python first.
    pause
    exit /b
)

echo ✅ Python found.

echo 🔥 Activating virtual environment (if any)...
if exist venv\Scripts\activate (
    call venv\Scripts\activate
    echo ✅ Virtual environment activated.
) else (
    echo ⚡ No virtual environment found. Continuing with system Python.
)

echo 📦 Installing FastAPI and Uvicorn (if not installed)...
pip install fastapi uvicorn >nul 2>&1

echo 🔎 Checking main.py...
if not exist main.py (
    echo ⚠️ main.py not found. Creating default main.py...
    echo from fastapi import FastAPI > main.py
    echo. >> main.py
    echo app = FastAPI() >> main.py
    echo. >> main.py
    echo @app.get("/") >> main.py
    echo def root(): >> main.py
    echo     return {"message": "NaMo Framework API is running 🚀"} >> main.py
    echo ✅ Default main.py created.
) else (
    echo ✅ Found existing main.py
)

echo 🚀 Starting NaMo Framework API server...
uvicorn main:app --reload

pause
