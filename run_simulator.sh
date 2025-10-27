#!/bin/bash

# 🚀 Quantum Blockchain Security Simulator - Auto Setup Script
# This script automatically sets up and runs the quantum simulator

echo "🚀 Quantum Blockchain Security Simulator - Auto Setup"
echo "===================================================="

# Check Python version
echo "🔍 Checking Python version..."
python_version=$(python --version 2>&1 | awk '{print $2}')
echo "   Found Python $python_version"

# Check if Python 3.9+
python -c "import sys; exit(0 if sys.version_info >= (3, 9) else 1)"
if [ $? -ne 0 ]; then
    echo "❌ Error: Python 3.9 or higher required!"
    echo "   Please install Python 3.9+ from https://python.org"
    exit 1
fi

echo "✅ Python version OK"

# Install dependencies
echo ""
echo "📦 Installing dependencies..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Error: Failed to install dependencies!"
    echo "   Try: pip install -r requirements.txt --user"
    exit 1
fi

echo "✅ Dependencies installed successfully"

# Run tests
echo ""
echo "🧪 Running tests..."
python test_quantum_app.py

if [ $? -ne 0 ]; then
    echo "❌ Error: Tests failed!"
    echo "   Check the error messages above"
    exit 1
fi

echo "✅ All tests passed!"

# Start the application
echo ""
echo "🚀 Starting Quantum Blockchain Security Simulator..."
echo "   The app will open in your browser at: http://localhost:8501"
echo ""
echo "📚 Quick tips:"
echo "   • Start with 'Security Analysis' mode"
echo "   • Try different RSA key sizes"
echo "   • Watch the quantum attack demo"
echo "   • Explore post-quantum solutions"
echo ""
echo "🛑 To stop the app: Press Ctrl+C"
echo ""

# Launch Streamlit
streamlit run quantum_blockchain_app.py