import streamlit as st
import numpy as np
import hashlib
import time
import random
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
import math

# Qiskit imports for real quantum simulation
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.visualization import circuit_drawer
from qiskit_aer import AerSimulator
from qiskit import transpile

# Set page config
st.set_page_config(
    page_title="Quantum vs Blockchain Security",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(45deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .main-header h1 {
        color: white;
        text-align: center;
        margin: 0;
    }
    .metric-container {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #667eea;
    }
    .vulnerability-alert {
        background: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .secure-alert {
        background: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

class QuantumCryptographySimulator:
    def __init__(self):
        self.rsa_keys = {}
        self.blockchain = []
        
    def generate_rsa_keys(self, key_size):
        """Generate RSA key pair"""
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size,
        )
        public_key = private_key.public_key()
        return private_key, public_key
    
    def classical_factorization_time(self, n):
        """Estimate classical factorization time (simplified)"""
        # Using General Number Field Sieve complexity
        log_n = math.log(n)
        complexity = math.exp(1.923 * (log_n ** (1/3)) * ((math.log(log_n)) ** (2/3)))
        # Convert to approximate years on modern computer
        operations_per_second = 10**12  # 1 TFlop/s
        seconds = complexity / operations_per_second
        years = seconds / (365.25 * 24 * 3600)
        return years
    
    def quantum_factorization_time(self, key_size):
        """Estimate quantum factorization time using Shor's algorithm"""
        # Simplified: Shor's algorithm runs in O((log N)^3) time
        qubits_needed = 2 * key_size + 1
        quantum_gates = (key_size ** 3) * math.log(key_size)
        # Assume quantum gate time of 100 nanoseconds
        gate_time = 100e-9
        total_time = quantum_gates * gate_time
        return total_time, qubits_needed
    
    def create_shors_circuit(self, n_bits=4):
        """Create a simplified Shor's algorithm quantum circuit"""
        # Create quantum circuit for simplified Shor's algorithm demo
        qr = QuantumRegister(n_bits, 'q')
        cr = ClassicalRegister(n_bits, 'c')
        circuit = QuantumCircuit(qr, cr)
        
        # Step 1: Create superposition
        for i in range(n_bits//2):
            circuit.h(qr[i])
        
        # Step 2: Quantum Fourier Transform (simplified)
        for i in range(n_bits//2):
            circuit.h(qr[i])
            for j in range(i+1, n_bits//2):
                circuit.cp(np.pi/2**(j-i), qr[j], qr[i])
        
        # Step 3: Measure
        circuit.measure(qr, cr)
        
        return circuit
    
    def simulate_quantum_circuit(self, circuit, shots=1024):
        """Simulate quantum circuit and return results"""
        try:
            simulator = AerSimulator()
            compiled_circuit = transpile(circuit, simulator)
            result = simulator.run(compiled_circuit, shots=shots).result()
            counts = result.get_counts(compiled_circuit)
            return counts
        except Exception as e:
            st.error(f"Quantum simulation error: {e}")
            return {}
    
    def create_blockchain_transaction(self, sender, receiver, amount, private_key):
        """Create a blockchain transaction with RSA signature"""
        transaction_data = f"{sender}->{receiver}:{amount}:{datetime.now().isoformat()}"
        
        # Sign transaction with RSA private key
        signature = private_key.sign(
            transaction_data.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        
        # Create block
        previous_hash = self.blockchain[-1]['hash'] if self.blockchain else "0"
        block_data = {
            'index': len(self.blockchain),
            'timestamp': datetime.now().isoformat(),
            'transaction': transaction_data,
            'signature': signature.hex(),
            'previous_hash': previous_hash,
            'sender_public_key': None  # We'll store the key separately for demo
        }
        
        # Calculate block hash
        block_string = f"{block_data['index']}{block_data['timestamp']}{block_data['transaction']}{block_data['previous_hash']}"
        block_data['hash'] = hashlib.sha256(block_string.encode()).hexdigest()
        
        return block_data
    
    def verify_transaction(self, block, public_key):
        """Verify transaction signature"""
        try:
            signature = bytes.fromhex(block['signature'])
            public_key.verify(
                signature,
                block['transaction'].encode(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except:
            return False

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🚀 Quantum Computing vs Blockchain Security</h1>
        <p style="text-align: center; color: white; margin: 0;">
            Explore how quantum computers could break current blockchain cryptography
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize simulator
    if 'simulator' not in st.session_state:
        st.session_state.simulator = QuantumCryptographySimulator()
    
    simulator = st.session_state.simulator
    
    # Sidebar controls
    st.sidebar.title("🔧 Simulation Controls")
    
    # RSA Key Size Selection
    key_size = st.sidebar.selectbox(
        "RSA Key Size (bits)",
        [1024, 2048, 3072, 4096],
        index=1,
        help="Larger keys are more secure but require more computational power"
    )
    
    simulation_mode = st.sidebar.selectbox(
        "Simulation Mode",
        ["Security Analysis", "Live Attack Demo", "Post-Quantum Solutions"]
    )
    
    # Main content area
    if simulation_mode == "Security Analysis":
        st.header("🔍 Cryptographic Security Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Classical Computing")
            
            # Generate RSA keys for analysis
            if st.button("Generate New RSA Keys"):
                with st.spinner("Generating RSA keys..."):
                    private_key, public_key = simulator.generate_rsa_keys(key_size)
                    st.session_state.current_keys = (private_key, public_key)
                    st.success(f"Generated {key_size}-bit RSA key pair!")
            
            if 'current_keys' in st.session_state:
                private_key, public_key = st.session_state.current_keys
                
                # Get public key modulus for factorization analysis
                public_numbers = public_key.public_numbers()
                n = public_numbers.n
                
                classical_time = simulator.classical_factorization_time(n)
                
                st.markdown(f"""
                <div class="metric-container">
                    <h4>Classical Factorization Time</h4>
                    <h2 style="color: #28a745;">{classical_time:.2e} years</h2>
                    <p>Time required using best classical algorithms</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Show key details
                st.info(f"""
                **Key Details:**
                - Key Size: {key_size} bits
                - Modulus (N): {n}
                - Security Level: Classical computers would need {classical_time:.1e} years to break this
                """)
        
        with col2:
            st.subheader("Quantum Computing")
            
            if 'current_keys' in st.session_state:
                quantum_time, qubits_needed = simulator.quantum_factorization_time(key_size)
                
                st.markdown(f"""
                <div class="metric-container">
                    <h4>Quantum Factorization Time</h4>
                    <h2 style="color: #dc3545;">{quantum_time:.2f} seconds</h2>
                    <p>Time required using Shor's algorithm</p>
                </div>
                """, unsafe_allow_html=True)
                
                st.error(f"""
                **Quantum Threat:**
                - Qubits Required: {qubits_needed}
                - Algorithm: Shor's factorization
                - Time Complexity: O((log N)³)
                - **Security Level: BROKEN** 💥
                """)
                
                # Vulnerability chart
                speedup_factor = classical_time * 365.25 * 24 * 3600 / quantum_time
                
                fig = go.Figure(data=[
                    go.Bar(name='Classical', x=['Factorization Time'], y=[classical_time * 365.25 * 24 * 3600], marker_color='green'),
                    go.Bar(name='Quantum', x=['Factorization Time'], y=[quantum_time], marker_color='red')
                ])
                fig.update_layout(
                    title=f"Security Comparison (log scale)",
                    yaxis_type="log",
                    yaxis_title="Time (seconds)",
                    showlegend=True
                )
                st.plotly_chart(fig, use_container_width=True)
                
                st.warning(f"**Quantum Speedup: {speedup_factor:.2e}x faster!**")
    
    elif simulation_mode == "Live Attack Demo":
        st.header("⚡ Live Quantum Attack Simulation")
        
        # Create a simple blockchain
        st.subheader("1. Create Blockchain Transaction")
        
        col1, col2 = st.columns(2)
        with col1:
            sender = st.text_input("Sender", "Alice")
            receiver = st.text_input("Receiver", "Bob")
            amount = st.number_input("Amount", min_value=0.01, value=10.0, step=0.01)
        
        with col2:
            if st.button("Create Transaction"):
                if 'current_keys' not in st.session_state:
                    private_key, public_key = simulator.generate_rsa_keys(key_size)
                    st.session_state.current_keys = (private_key, public_key)
                
                private_key, public_key = st.session_state.current_keys
                
                # Create transaction
                block = simulator.create_blockchain_transaction(sender, receiver, amount, private_key)
                simulator.blockchain.append(block)
                
                st.success("Transaction created and added to blockchain!")
                
        # Display blockchain
        if simulator.blockchain:
            st.subheader("2. Current Blockchain State")
            
            for i, block in enumerate(simulator.blockchain[-3:]):  # Show last 3 blocks
                verified = "✅ Verified" if 'current_keys' in st.session_state and simulator.verify_transaction(block, st.session_state.current_keys[1]) else "❌ Invalid"
                
                st.markdown(f"""
                <div class="secure-alert">
                    <strong>Block #{block['index']}</strong> {verified}<br>
                    <strong>Transaction:</strong> {block['transaction']}<br>
                    <strong>Hash:</strong> {block['hash'][:32]}...<br>
                    <strong>Timestamp:</strong> {block['timestamp']}
                </div>
                """, unsafe_allow_html=True)
        
        # Quantum attack simulation
        st.subheader("3. Simulate Quantum Attack")
        
        # Initialize attack state
        if 'attack_completed' not in st.session_state:
            st.session_state.attack_completed = False
        
        if st.button("🚨 Launch Quantum Attack"):
            if not simulator.blockchain:
                st.error("Create some transactions first!")
            else:
                st.warning("**Quantum computer deploying Shor's algorithm...**")
                
                # Create and display quantum circuit
                st.subheader("Quantum Circuit: Shor's Algorithm")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    # Create Shor's algorithm circuit
                    circuit = simulator.create_shors_circuit(n_bits=6)
                    
                    # Display circuit as text (since we can't easily render images in this environment)
                    st.code(str(circuit), language="text")
                    
                    st.info("""
                    **Quantum Circuit Elements:**
                    - H gates: Create superposition
                    - CP gates: Controlled phase for quantum Fourier transform
                    - Measurement: Extract classical result
                    """)
                
                with col2:
                    # Simulate the circuit
                    st.write("**Running quantum simulation...**")
                    with st.spinner("Quantum gates executing..."):
                        time.sleep(2)  # Simulate quantum computation time
                        
                        # Run quantum simulation
                        results = simulator.simulate_quantum_circuit(circuit, shots=1024)
                        
                        if results:
                            # Display quantum measurement results
                            st.write("**Quantum Measurement Results:**")
                            
                            # Create a bar chart of measurement outcomes
                            if results:
                                states = list(results.keys())
                                counts = list(results.values())
                                
                                fig = go.Figure(data=[
                                    go.Bar(x=states[:10], y=counts[:10], marker_color='red')
                                ])
                                fig.update_layout(
                                    title="Quantum State Measurements",
                                    xaxis_title="Quantum States",
                                    yaxis_title="Measurement Count",
                                    height=300
                                )
                                st.plotly_chart(fig, use_container_width=True)
                                
                                # Show quantum advantage
                                total_measurements = sum(counts)
                                most_frequent = max(results.items(), key=lambda x: x[1])
                                
                                st.success(f"""
                                **Quantum Pattern Found!**
                                - Most frequent state: {most_frequent[0]}
                                - Probability: {most_frequent[1]/total_measurements:.2%}
                                - Total measurements: {total_measurements}
                                """)
                
                # Simulate the factorization process
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                steps = [
                    "Initializing quantum registers",
                    "Creating superposition states", 
                    "Applying quantum Fourier transform",
                    "Measuring quantum periodicity",
                    "Processing quantum results",
                    "Extracting classical factors"
                ]
                
                for i, step in enumerate(steps):
                    status_text.text(f"Step {i+1}: {step}")
                    progress_bar.progress((i + 1) / len(steps))
                    time.sleep(0.8)
                
                st.error("**🔓 RSA Private Key Extracted!**")
                
                # Mark attack as completed
                st.session_state.attack_completed = True
                
                # Show the attack consequences
                st.markdown("""
                <div class="vulnerability-alert">
                    <h4>⚠️ BLOCKCHAIN COMPROMISED</h4>
                    <p>With the private key extracted, an attacker can now:</p>
                    <ul>
                        <li>Forge transactions from any user</li>
                        <li>Double-spend coins</li>
                        <li>Manipulate transaction history</li>
                        <li>Steal funds from any wallet</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
        
        # Show forged transaction option if attack was completed
        if st.session_state.attack_completed:
            st.subheader("4. Demonstrate Attack Consequences")
            
            st.markdown("""
            <div class="vulnerability-alert">
                <h4>⚠️ BLOCKCHAIN COMPROMISED</h4>
                <p>With the private key extracted, an attacker can now:</p>
                <ul>
                    <li>Forge transactions from any user</li>
                    <li>Double-spend coins</li>
                    <li>Manipulate transaction history</li>
                    <li>Steal funds from any wallet</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("💀 Create Forged Transaction"):
                    if 'current_keys' in st.session_state:
                        private_key, public_key = st.session_state.current_keys
                        forged_block = simulator.create_blockchain_transaction(
                            "Bob", "Attacker", 1000000, private_key
                        )
                        simulator.blockchain.append(forged_block)
                        st.session_state.forged_transaction_created = True
                        st.error("💀 Forged transaction created! Bob's account drained!")
                    else:
                        st.error("No keys available for forging!")
            
            with col2:
                if st.button("🔄 Reset Attack Demo"):
                    st.session_state.attack_completed = False
                    st.session_state.forged_transaction_created = False
                    st.success("Attack demo reset! You can run the attack again.")
                    st.rerun()
            
            # Show forged transaction confirmation
            if st.session_state.get('forged_transaction_created', False):
                st.error("""
                **🚨 ATTACK SUCCESSFUL! 🚨**
                
                The quantum computer has successfully:
                ✅ Broken RSA encryption  
                ✅ Extracted private keys  
                ✅ Forged blockchain transactions  
                ✅ Compromised network security  
                
                **This demonstrates why we need post-quantum cryptography!**
                """)
                
                # Show the latest forged transaction
                if simulator.blockchain:
                    latest_block = simulator.blockchain[-1]
                    if "Attacker" in latest_block['transaction']:
                        st.markdown(f"""
                        <div class="vulnerability-alert">
                            <strong>🔍 Latest Forged Transaction:</strong><br>
                            <strong>Block #{latest_block['index']}</strong><br>
                            <strong>Transaction:</strong> {latest_block['transaction']}<br>
                            <strong>Hash:</strong> {latest_block['hash'][:32]}...<br>
                            <strong>Status:</strong> ❌ FRAUDULENT
                        </div>
                        """, unsafe_allow_html=True)
    
    elif simulation_mode == "Post-Quantum Solutions":
        st.header("🛡️ Post-Quantum Cryptography Solutions")
        
        st.info("""
        **The Future of Blockchain Security**
        
        As quantum computers become more powerful, the blockchain ecosystem must evolve.
        Here are the quantum-resistant solutions being developed:
        """)
        
        # Solutions comparison
        solutions = {
            "Lattice-Based Cryptography": {
                "security": "Very High",
                "speed": "Fast",
                "key_size": "Large",
                "description": "Based on hard problems in high-dimensional lattices",
                "examples": "CRYSTALS-Kyber, CRYSTALS-Dilithium"
            },
            "Hash-Based Signatures": {
                "security": "Proven",
                "speed": "Slow",
                "key_size": "Very Large",
                "description": "Security based on cryptographic hash functions",
                "examples": "SPHINCS+, XMSS"
            },
            "Code-Based Cryptography": {
                "security": "High",
                "speed": "Medium",
                "key_size": "Large",
                "description": "Based on error-correcting codes",
                "examples": "Classic McEliece, BIKE"
            },
            "Multivariate Cryptography": {
                "security": "Medium",
                "speed": "Fast",
                "key_size": "Medium",
                "description": "Based on solving multivariate polynomial equations",
                "examples": "Rainbow, GeMSS"
            }
        }
        
        for name, details in solutions.items():
            with st.expander(f"🔒 {name}"):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write(f"**Description:** {details['description']}")
                    st.write(f"**Examples:** {details['examples']}")
                
                with col2:
                    st.write(f"**Security Level:** {details['security']}")
                    st.write(f"**Performance:** {details['speed']}")
                    st.write(f"**Key Size:** {details['key_size']}")
        
        # Timeline
        st.subheader("📅 Quantum Threat Timeline")
        
        timeline_data = {
            "Year": [2025, 2030, 2035, 2040],
            "Quantum_Computers": [100, 1000, 10000, 100000],
            "Risk_Level": ["Low", "Medium", "High", "Critical"]
        }
        
        fig = px.line(x=timeline_data["Year"], y=timeline_data["Quantum_Computers"],
                     title="Projected Quantum Computer Development",
                     labels={"x": "Year", "y": "Logical Qubits"})
        fig.add_hline(y=4096, line_dash="dash", line_color="red", 
                     annotation_text="RSA-2048 broken")
        st.plotly_chart(fig, use_container_width=True)
        
        # Migration strategy
        st.subheader("🔄 Migration Strategy for Blockchain")
        
        migration_steps = [
            "1. **Hybrid Period**: Implement dual signatures (classical + quantum-resistant)",
            "2. **Algorithm Agility**: Design systems that can quickly switch cryptographic algorithms",
            "3. **Gradual Migration**: Phase out RSA/ECDSA over 5-10 years",
            "4. **Standards Adoption**: Follow NIST post-quantum cryptography standards",
            "5. **Testing & Validation**: Extensive testing of quantum-resistant implementations"
        ]
        
        for step in migration_steps:
            st.write(step)
    
    # Footer with educational content
    st.markdown("---")
    st.markdown("""
    ### 📚 Learn More
    - **Shor's Algorithm**: Quantum algorithm that can efficiently factor large integers
    - **Post-Quantum Cryptography**: Cryptographic algorithms designed to be secure against quantum attacks
    - **NIST Competition**: Ongoing effort to standardize quantum-resistant cryptographic algorithms
    - **Quantum Supremacy**: The point where quantum computers outperform classical computers for specific tasks
    """)

if __name__ == "__main__":
    main()