import argparse
from qcrypto.bb84 import BB84
from qcrypto.eavesdropper import Eve
from qcrypto.utils import encrypt_decrypt, plot_error_rate

def main():
    parser = argparse.ArgumentParser(description="BB84 Quantum Key Distribution Simulation")
    parser.add_argument("--key_length", type=int, default=50, help="Length of the quantum key")
    parser.add_argument("--eve_present", action="store_true", help="Simulate eavesdropping")
    parser.add_argument("--message", type=str, help="Message to encrypt")
    parser.add_argument("--quantum_hardware", type=str, help="IBM Quantum hardware name (e.g., 'ibmq_quito')")
    args = parser.parse_args()
    
    #implementation of BB84 protocol
    bb84 = BB84(args.key_length, args.quantum_hardware)
    alice_bases, bob_bases = bb84.generate_bases()
    circuits = bb84.prepare_qubits(alice_bases)
    
    #simulate intercept (if enabled)
    if args.eve_present:
        eve = Eve()
        circuits = eve.intercept(circuits)

    bob_measurements = bb84.measure_qubits(circuits, bob_bases)
    alice_key = bb84.sift_keys(alice_bases, bob_bases, [0] * args.key_length)
    bob_key = bb84.sift_keys(alice_bases, bob_bases, bob_measurements)

    #result
    print(f"\nalice_key (first 10 bit): {alice_key[:10]}")
    print(f"bob_key (first 10 bit): {bob_key[:10]}")
    mismatch = sum(a != b for a, b in zip(alice_key, bob_key))
    print(f"mismatch: {mismatch}")

    #Message encryption (if any)
    if args.message:
        encrypted = encrypt_decrypt(args.message, alice_key)
        decrypted = encrypt_decrypt(encrypted, bob_key)
        print(f"\nencrypted message: {encrypted}")
        print(f"decrypted message: {decrypted}")

    #display errors
    if args.eve_present:
        plot_error_rate(alice_key, bob_key)

if __name__ == "__main__":
    main()
