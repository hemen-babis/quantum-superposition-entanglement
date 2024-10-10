# Quantum Superposition and Entanglement

Author: Hemen Babis  
Date: October 10, 2024

## Project Overview

This project demonstrates two important concepts in quantum computing: **Superposition** and **Entanglement**. It uses the Qiskit library to build quantum circuits and visualize the results.

- **Superposition**: Using a Hadamard gate on a single qubit to put it in a state where it's simultaneously |0⟩ and |1⟩.
- **Entanglement**: Using a Hadamard gate and a CNOT gate to create an entangled state between two qubits, where measuring one qubit determines the state of the other.

## How to Run This Project

### 1 ---> Let's clone the repository

First, you'll need to clone this repository to your local machine:

```bash
git clone https://github.com/hemen-babis/quantum-superposition-entanglement.git
```

### 2 ---> Then install dependencies

Make sure you have Python installed (version 3.8 or higher). Install the dependencies by running:

```bash
pip install -r requirements.txt
```

### 3 ---> Run!!!

You can run the project by executing:

```bash
python main.py
```

Once you run it, you'll be asked to choose between simulating **superposition** (option 1) or **entanglement** (option 2). Pick one and let the program do its magic!

## What the Project Does

### Superposition

When you choose superposition (option 1), the program creates a quantum circuit with a single qubit and applies a Hadamard gate to it. This puts the qubit in a superposition of states |0⟩ and |1⟩ at the same time. The output is visualized on a Bloch sphere:

![Figure_1](https://github.com/user-attachments/assets/dd6bf25c-32c9-4c37-8798-7d39a1fb94a9)

### Entanglement

When you choose entanglement (option 2), the program creates a quantum circuit with two qubits. It first applies a Hadamard gate to the first qubit and then a CNOT gate, which entangles the two qubits. The result is that the qubits are linked, so measuring one affects the state of the other. The measurement results are shown in a histogram:

![Figure_2](https://github.com/user-attachments/assets/9f3aae73-10d1-4fd9-8dda-981d339aa927)

## Figures

- **Superposition Bloch Sphere**: A Bloch sphere representation of the quantum state after applying the Hadamard gate on a single qubit.
- **Entaglement Histogram**: A histogram showing the measurement results for two entangled qubits, with possible outcomes `00` and `11`.
  
