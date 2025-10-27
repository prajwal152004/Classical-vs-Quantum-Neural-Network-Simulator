@echo off
REM 🚀 Quantum Blockchain Security Simulator - Auto Setup Script (Windows)
REM This script automatically sets up and runs the quantum simulator

echo 🚀 Quantum Blockchain Security Simulator - Auto Setup
echo ====================================================

REM Check Python installation
echo 🔍 Checking Python version...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Error: Python not found!
    echo    Please install Python 3.9+ from https://python.org
    echo    Make sure to add Python to PATH during installation
    pause
    exit /b 1
)

python --version
echo ✅ Python found

REM Install dependencies
echo.
echo 📦 Installing dependencies...
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo ❌ Error: Failed to install dependencies!
    echo    Try running as administrator or use: pip install -r requirements.txt --user
    pause
    exit /b 1
)

echo ✅ Dependencies installed successfully

REM Run tests
echo.
echo 🧪 Running tests...
python test_quantum_app.py

if %errorlevel% neq 0 (
    echo ❌ Error: Tests failed!
    echo    Check the error messages above
    pause
    exit /b 1
)

echo ✅ All tests passed!

REM Start the application
echo.
echo 🚀 Starting Quantum Blockchain Security Simulator...
echo    The app will open in your browser at: http://localhost:8501
echo.
echo 📚 Quick tips:
echo    • Start with 'Security Analysis' mode
echo    • Try different RSA key sizes  
echo    • Watch the quantum attack demo
echo    • Explore post-quantum solutions
echo.
echo 🛑 To stop the app: Press Ctrl+C
echo.

REM Launch Streamlit
streamlit run quantum_blockchain_app.py

pause