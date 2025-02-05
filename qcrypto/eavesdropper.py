import numpy as np
from qiskit import QuantumCircuit, Aer, execute

class Eve:
    def __init__(self):
        self.backend = Aer.get_backend('qasm_simulator')

    def intercept(self, circuits):
        eve_bases = np.random.choice([0, 1], size=len(circuits))
        attacked_circuits = []
        for qc, basis in zip(circuits, eve_bases):
            temp = qc.copy()
            if basis == 1:
                temp.h(0)
            temp.measure(0, 0)
            result = execute(temp, self.backend, shots=1).result()
            measured_bit = int(list(result.get_counts().keys())[0])
            new_qc= QuantumCircuit(1, 1)
            if basis == 1:
                new_qc.h(0)
            if measured_bit == 1:
                new_qc.x(0)
            attacked_circuits.append(new_qc)
        return attacked_circuits
    

