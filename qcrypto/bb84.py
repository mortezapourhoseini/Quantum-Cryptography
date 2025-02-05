import numpy as np
from qiskit import QuantumCircuit, Aer, execute, IBMProvider
from qiskit_ibm_provider import IBMProvider

class BB84:
    def __init__(self, key_length=50, quantum_hardware=None):
        self.key_length = key_length
        self.quantum_hardware = quantum_hardware
        self.backend = Aer.get_backend('qasm_simulator') if not quantom_hardware else IBMProvider().get_backend(quantum_hardware)

    def generate_bases(self):
        return (
                np.random.choice([0, 1], size=self.key_length), #alice
                np.random.choice([0, 1], size=self.key_length) #bob
        )


    def prepare_qubits(self, alice_bases):
        circuits = []
        for basis in alice_bases:
            qc = QuantomCircuit(1, 1)
            if basis == 1:
                qc.h(0)
            qc.barrier()
            circuits.append(qc)
        return circuits

    def measure_qubits(self, circuits, bob_bases):
        measurements = []
        for qc, basis in zip(circuits, bob_bases):
            temp = qc.copy()
            if basis == 1:
                temp.h(0)
            temp.measure(0,0)
            job = execute(temp, self.backend, shots=1)
            result = job.result()
            measured_bit = int(list(result.get_counts().keys())[0])
            measurements.append(measured_bit)
        return measurements

    def sift_keys(self, alice_bases, bob_bases, measurements):
        return [bit for a, b, bit in zip(alice_bases, bob_bases, measurements) if a == b]



