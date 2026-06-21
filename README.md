readme_content = """# QC Boot Camp: Mini-Project 10 - Mixed Quantum State Preparation

## Overview
This repository contains the implementation for Mini-Project 10 of the QC Boot Camp. The objective is to provide a generalized Qiskit function that takes an arbitrary $2^n \\times 2^n$ density matrix $\\rho$ and outputs a quantum circuit that prepares this mixed state. 

The implementation strictly utilizes ancilla qubits, arbitrary 1-qubit gates, and multi-controlled operations to achieve state purification.

## Theoretical Background
Because quantum circuits operate via unitary transformations, they inherently prepare pure states. To output a mixed state $\\rho$, we must rely on the method of **state purification**:

1. **Spectral Decomposition:** The density matrix $\\rho$ is mathematically diagonalized to extract its eigenvalues (which represent classical probabilities) and its eigenvectors (the target pure states).
2. **Ancilla Preparation:** A register of $n$ ancilla qubits is initialized in a superposition where the probability amplitudes are exactly the square roots of the eigenvalues.
3. **System Entanglement:** The $n$ system qubits are entangled with the ancilla register. This is done using multiplexed state preparation gates that map the system to specific eigenvectors conditioned on the state of the ancillas.
4. **Partial Trace:** The ancilla register is measured and the classical outcomes are discarded. By tracing out the ancillas, the reduced density matrix of the remaining system qubits exactly equals the target mixed state $\\rho$.

## Repository Structure
* `mixed_state.py`: The main Python script containing the generalized quantum circuit function and the specific demonstration for an $n=2$ system.
* `circuit_diagram.png`: A high-resolution architectural diagram of the generated quantum circuit for the test case.
* `mixed_state_preparation_theory.tex`: The LaTeX document detailing the mathematical proofs and theoretical framework.
* `README.md`: This project documentation file.

## Requirements
To execute the code in this repository, you must have Python installed along with the following packages:
* `qiskit`
* `numpy`
* `scipy`
* `matplotlib`
* `pylatexenc`

You can install all required dependencies within your virtual environment using pip: