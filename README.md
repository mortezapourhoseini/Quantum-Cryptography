# QuantumCryptography-BB84-Simulation 🌌🔐

A Python-based simulation of the BB84 Quantum Key Distribution (QKD) protocol using IBM's Qiskit. This project demonstrates quantum-safe encryption, eavesdropping detection, and message encryption/decryption.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green)](https://www.python.org/)
[![Qiskit](https://img.shields.io/badge/Qiskit-0.44+-purple)](https://qiskit.org/)

---

## 📜 Overview
This repository simulates the **BB84 Quantum Key Distribution (QKD)** protocol, a foundational method for secure quantum communication. The project includes:
- **Quantum Key Generation**: Simulates Alice and Bob creating a shared secret key using qubits.
- **Eavesdropping (Eve) Simulation**: Demonstrates how eavesdropping introduces errors in the key.
- **Message Encryption/Decryption**: Uses the quantum key to encrypt and decrypt messages.
- **IBM Quantum Integration**: Optional support for running simulations on IBM Quantum hardware.

---

## 🚀 Features
- **BB84 Protocol Implementation**: Simulates qubit preparation, measurement, and sifting.
- **Eavesdropping Detection**: Measures error rates caused by an eavesdropper (Eve).
- **Quantum Hardware Support**: Compatible with IBM Quantum devices via Qiskit.
- **Interactive Visualization**: Plots error rates and key mismatches.

---

## ⚙️ Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/QuantumCryptography-BB84-Simulation.git
   cd QuantumCryptography-BB84-Simulation
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🧪 Usage

### Basic Simulation (No Eavesdropping)
```python
python main.py --key_length 100
```

### Simulate Eavesdropping
```python
python main.py --key_length 100 --eve_present
```

### Encrypt/Decrypt a Message
```python
python main.py --message "Hello Quantum World!" --key_length 50
```

### Run on IBM Quantum Hardware
1. Add your IBM Quantum API token to `config.py`.
2. Execute:
   ```python
   python main.py --quantum_hardware ibmq_quito
   ```

---

## 📊 Example Output
![Key Mismatch Visualization](images/error_plot.png)  
*Example plot showing eavesdropping-induced errors.*

---

## 📂 File Structure
```
├── main.py                 # Main simulation script
├── qcrypto/                # Core modules
│   ├── bb84.py             # BB84 protocol implementation
│   ├── eavesdropper.py     # Eavesdropping logic
│   └── utils.py            # Helper functions
├── requirements.txt        # Dependencies
├── config.py               # API token configuration
└── README.md
```

---

## 🌟 Contributing
Contributions are welcome!  
1. Fork the repository.  
2. Create a branch: `git checkout -b feature/your-idea`.  
3. Commit changes: `git commit -m "Add amazing feature"`.  
4. Push to the branch: `git push origin feature/your-idea`.  
5. Open a pull request.  

---

## 📧 Contact
For questions or collaborations, email: **your-email@example.com**
