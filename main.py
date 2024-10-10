"""
Author: Hemen Babis
Date: October 10, 2024

Project: Quantum Superposition Demonstration

Description:
    It shows quantum superposition using a single qubit. The Hadamard gate is 
    applied to the qubit to place it in superposition, and the result is visualized on a Bloch 
    sphere.
"""

import superposition
import entanglement

def main():
    print("Quantum Demonstration: Superposition and Entanglement")
    choice = input("Choose an option (1: Superposition, 2: Entanglement): ")
    
    if choice == '1':
        superposition.run_superposition()
    elif choice == '2':
        entanglement.run_entanglement()
    else:
        print("Invalid choice! Please select 1 or 2.")

if __name__ == '__main__':
    main()
