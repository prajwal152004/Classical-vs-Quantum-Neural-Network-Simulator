#!/usr/bin/env python3
"""
Test script for Quantum Blockchain Security Simulator
"""
import sys
sys.path.append('/app')

from quantum_blockchain_app import QuantumCryptographySimulator
import time

def test_quantum_simulation():
    """Test the quantum simulation functionality"""
    print("🔬 Testing Quantum Cryptography Simulator...")
    
    # Initialize simulator
    simulator = QuantumCryptographySimulator()
    
    # Test RSA key generation
    print("\n1. Testing RSA Key Generation...")
    try:
        private_key, public_key = simulator.generate_rsa_keys(1024)
        print("✅ RSA keys generated successfully")
        
        # Get key modulus for analysis
        public_numbers = public_key.public_numbers()
        n = public_numbers.n
        print(f"   RSA modulus (N): {n}")
        
    except Exception as e:
        print(f"❌ RSA key generation failed: {e}")
        return False
    
    # Test quantum circuit creation
    print("\n2. Testing Quantum Circuit Creation...")
    try:
        circuit = simulator.create_shors_circuit(n_bits=4)
        print("✅ Quantum circuit created successfully")
        print(f"   Circuit depth: {circuit.depth()}")
        print(f"   Number of qubits: {circuit.num_qubits}")
        
    except Exception as e:
        print(f"❌ Quantum circuit creation failed: {e}")
        return False
    
    # Test quantum simulation
    print("\n3. Testing Quantum Simulation...")
    try:
        results = simulator.simulate_quantum_circuit(circuit, shots=100)
        if results:
            print("✅ Quantum simulation completed successfully")
            print(f"   Number of measurement outcomes: {len(results)}")
            print(f"   Sample results: {dict(list(results.items())[:3])}")
        else:
            print("⚠️  Quantum simulation returned no results")
            
    except Exception as e:
        print(f"❌ Quantum simulation failed: {e}")
        return False
    
    # Test blockchain transaction
    print("\n4. Testing Blockchain Transaction...")
    try:
        block = simulator.create_blockchain_transaction("Alice", "Bob", 10.0, private_key)
        simulator.blockchain.append(block)
        print("✅ Blockchain transaction created successfully")
        print(f"   Block index: {block['index']}")
        print(f"   Transaction: {block['transaction']}")
        
    except Exception as e:
        print(f"❌ Blockchain transaction failed: {e}")
        return False
    
    # Test transaction verification
    print("\n5. Testing Transaction Verification...")
    try:
        is_valid = simulator.verify_transaction(block, public_key)
        if is_valid:
            print("✅ Transaction verification successful")
        else:
            print("❌ Transaction verification failed")
            return False
            
    except Exception as e:
        print(f"❌ Transaction verification error: {e}")
        return False
    
    # Test security analysis
    print("\n6. Testing Security Analysis...")
    try:
        classical_time = simulator.classical_factorization_time(n)
        quantum_time, qubits_needed = simulator.quantum_factorization_time(1024)
        
        print("✅ Security analysis completed successfully")
        print(f"   Classical factorization time: {classical_time:.2e} years")
        print(f"   Quantum factorization time: {quantum_time:.2f} seconds")
        print(f"   Qubits needed: {qubits_needed}")
        print(f"   Quantum speedup: {(classical_time * 365.25 * 24 * 3600 / quantum_time):.2e}x")
        
    except Exception as e:
        print(f"❌ Security analysis failed: {e}")
        return False
    
    print("\n🎉 All tests completed successfully!")
    print("\n📊 Test Summary:")
    print("   ✅ RSA cryptography")
    print("   ✅ Quantum circuit simulation")
    print("   ✅ Blockchain transactions")  
    print("   ✅ Cryptographic security analysis")
    print("   ✅ Quantum vs classical comparison")
    
    return True

def test_app_startup():
    """Test if the app can be accessed"""
    print("\n🌐 Testing App Accessibility...")
    
    import requests
    try:
        response = requests.get("http://localhost:8501", timeout=5)
        if response.status_code == 200:
            print("✅ Streamlit app is running and accessible")
            return True
        else:
            print(f"❌ App returned status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ App accessibility test failed: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Starting Quantum Blockchain Security Simulator Tests")
    print("=" * 60)
    
    # Test core functionality
    quantum_test_passed = test_quantum_simulation()
    
    # Test app accessibility
    app_test_passed = test_app_startup()
    
    print("\n" + "=" * 60)
    print("📋 FINAL TEST RESULTS:")
    print(f"   Core Functionality: {'✅ PASS' if quantum_test_passed else '❌ FAIL'}")
    print(f"   App Accessibility:  {'✅ PASS' if app_test_passed else '❌ FAIL'}")
    
    if quantum_test_passed and app_test_passed:
        print("\n🎯 SUCCESS: Quantum Blockchain Security Simulator is ready!")
        print("🔗 Access the app at: http://localhost:8501")
    else:
        print("\n⚠️  Some tests failed. Please check the logs above.")
        sys.exit(1)