# 🚀 Quantum Computing vs Blockchain Security Simulator

A comprehensive Streamlit application that demonstrates the impact of quantum computing on blockchain cryptography, featuring real quantum simulations and interactive security analysis.

## 🎯 Key Features

### 1. **Security Analysis Mode**
- **Interactive RSA Key Generation**: Generate RSA keys from 1024 to 4096 bits
- **Classical vs Quantum Comparison**: Real-time factorization time analysis
- **Quantum Speedup Visualization**: See the dramatic difference between classical and quantum computing power
- **Security Vulnerability Assessment**: Understand when your encryption becomes vulnerable

### 2. **Live Attack Simulation**
- **Blockchain Transaction Creation**: Create realistic blockchain transactions with RSA signatures
- **Real Quantum Circuit Simulation**: Uses Qiskit to simulate Shor's algorithm
- **Interactive Attack Demo**: Watch quantum computing break RSA encryption in real-time
- **Transaction Forgery**: Demonstrate the consequences of compromised private keys

### 3. **Post-Quantum Solutions**
- **Future-Proof Cryptography**: Learn about quantum-resistant algorithms
- **Migration Strategies**: Roadmap for transitioning to post-quantum cryptography
- **Timeline Analysis**: Understand when quantum computers will pose a real threat
- **Algorithm Comparison**: Compare different post-quantum cryptographic approaches

## 🔬 Technical Implementation

### Quantum Computing Features
- **Real Quantum Circuits**: Built with Qiskit, the world's leading quantum computing framework
- **Shor's Algorithm Simulation**: Actual implementation of the quantum factorization algorithm
- **Quantum State Visualization**: Interactive plots of quantum measurement outcomes
- **Performance Analysis**: Real comparison of classical vs quantum complexity

### Blockchain Integration
- **Digital Signatures**: RSA-based transaction signing and verification
- **Block Creation**: Simulated blockchain with cryptographic hashing
- **Transaction Integrity**: Demonstrate how quantum computing breaks blockchain security
- **Vulnerability Testing**: Show real attack scenarios and their consequences

### Cryptographic Security
- **Multiple Key Sizes**: Support for 1024, 2048, 3072, and 4096-bit RSA keys
- **Time Complexity Analysis**: Mathematical modeling of factorization difficulty
- **Quantum Resource Estimation**: Calculate qubits needed for quantum attacks
- **Security Level Assessment**: Real-world security implications

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Streamlit
- Qiskit (for quantum simulation)
- Cryptography library
- Plotly (for visualizations)

## 🚀 Getting Started

### **Quick Start (3 Steps)**
1. **Install dependencies**: `pip install -r requirements.txt`
2. **Test installation**: `python test_quantum_app.py`  
3. **Run the app**: `streamlit run quantum_blockchain_app.py`

**Then open**: `http://localhost:8501`

### **Automated Setup**
```bash
# Linux/Mac - Run the auto-setup script
./run_simulator.sh

# Windows - Double-click or run
run_simulator.bat
```

### **Detailed Instructions**
- 📖 **Complete Setup Guide**: See [SETUP_INSTRUCTIONS.md](SETUP_INSTRUCTIONS.md)
- ⚡ **Quick Reference**: See [QUICKSTART.md](QUICKSTART.md)

## 📊 Example Results

### Security Analysis Results (2048-bit RSA)
- **Classical Factorization Time**: ~300 billion years
- **Quantum Factorization Time**: ~1,000 seconds
- **Quantum Speedup**: ~10¹⁵x faster
- **Qubits Required**: ~4,097 qubits

## 🛡️ Post-Quantum Cryptography

The app covers several quantum-resistant algorithms:

### Lattice-Based Cryptography
- **CRYSTALS-Kyber**: Key encapsulation mechanism
- **CRYSTALS-Dilithium**: Digital signature algorithm
- **Security**: Based on hard lattice problems
- **Status**: NIST standardized

### Hash-Based Signatures
- **SPHINCS+**: Stateless hash-based signatures
- **XMSS**: Extended Merkle signature scheme
- **Security**: Based on cryptographic hash functions
- **Advantage**: Proven security assumptions

## 📈 Quantum Threat Timeline

| Year | Quantum Computer Capability | Risk Level | Action Required |
|------|---------------------------|------------|-----------------|
| 2025 | ~100 logical qubits | Low | Monitor developments |
| 2030 | ~1,000 logical qubits | Medium | Begin migration planning |
| 2035 | ~10,000 logical qubits | High | Active migration to post-quantum |
| 2040+ | ~100,000+ logical qubits | Critical | Full post-quantum deployment |

## 🎓 Educational Content

### Learning Objectives
1. **Understand Quantum Computing**: Learn how quantum computers work
2. **Grasp Cryptographic Vulnerabilities**: See why current encryption is at risk
3. **Explore Future Solutions**: Discover quantum-resistant alternatives
4. **Visualize Complex Concepts**: Interactive demonstrations of abstract ideas

### Use Cases
- **Academic Research**: Quantum computing and cryptography studies
- **Industry Training**: Blockchain and cybersecurity education
- **Policy Making**: Understanding the quantum threat timeline
- **Technology Planning**: Preparing for post-quantum transitions