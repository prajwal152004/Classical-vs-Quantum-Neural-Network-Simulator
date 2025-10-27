# ⚡ **Quick Start Guide**

## 🚀 **Get Running in 3 Steps**

### **1. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **2. Test Installation**
```bash
python test_quantum_app.py
```

### **3. Run the App**
```bash
streamlit run quantum_blockchain_app.py
```

**Then open**: `http://localhost:8501`

---

## 🎯 **What to Try First**

1. **Security Analysis** → Generate RSA keys → See quantum vs classical times
2. **Live Attack Demo** → Create transaction → Launch quantum attack
3. **Post-Quantum Solutions** → Learn about future-proof cryptography

---

## ⚠️ **Quick Troubleshooting**

**App won't start?**
```bash
# Check Python version (need 3.9+)
python --version

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

**Port busy?**
```bash
# Kill existing processes
pkill -f streamlit

# Or use different port
streamlit run quantum_blockchain_app.py --server.port 8502
```

**Need help?** → See detailed instructions in `SETUP_INSTRUCTIONS.md`

---

**🎉 Enjoy exploring quantum computing vs blockchain security!**