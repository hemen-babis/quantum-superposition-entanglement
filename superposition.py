"""
Author: Hemen Babis
Date: October 10, 2024

Project: Quantum Superposition Demonstration

Description:
    It shows quantum superposition using a single qubit. The Hadamard gate is 
    applied to the qubit to place it in superposition, and the result is visualized on a Bloch 
    sphere.
"""

from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_bloch_multivector
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt

def run_superposition():
    print("Running Superposition Simulation...")
    
    # Create a quantum circuit with 1 qubit
    qc = QuantumCircuit(1)
    
    #Apply Hadamard gate to the qubit to create superposition
    qc.h(0)
    
    # Draw the circuit
    print(qc.draw('text'))
    
    # Simulate the quantum circuit
    simulator = Aer.get_backend('statevector_simulator')
    result = execute(qc, simulator).result()
    
    # Get the quantum state
    state = Statevector(result.get_statevector())
    
    # plot the Bloch sphere
    plot_bloch_multivector(state)
    plt.show()

if __name__ == '__main__':
    run_superposition()
