"""
Author: Hemen Babis
Date: October 10, 2024

Project: Quantum Entanglement Demonstration

Description:
    It shows quantum entanglement using two qubits. A Hadamard gate and a CNOT
    gate are applied to create an entangled state, and the result is visualized with a measurement
    histogram.
"""

from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def run_entanglement():
    print("Running Entanglement Simulation...")
    
    # Create a quantum circuit with 2 qubits and 2 classical bits for measurement
    qc = QuantumCircuit(2, 2)
    
    # Apply Hadamard gate on the first qubit
    qc.h(0)
    
    # Apply CNOT gate (control qubit 0, target qubit 1)
    qc.cx(0, 1)
    
    # Add measurement operations to both qubits
    qc.measure([0, 1], [0, 1])
    
    # Draw the circuit
    print(qc.draw('text'))
    
    # Simulate the quantum circuit
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(qc, simulator, shots=1024)
    
    # Get the result and measurement counts
    result = job.result()
    counts = result.get_counts()
    
    # Plot the results as a histogram
    plot_histogram(counts)
    plt.show()

if __name__ == '__main__':
    run_entanglement()
