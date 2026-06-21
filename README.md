# Mixed Quantum State Preparation

## Overview
This repository contains the implementation for Mini-Project 10 of the QC Boot Camp. The objective is to provide a generalized Qiskit function that takes an arbitrary $2^n \times 2^n$ density matrix $\rho \in \mathbb{C}^{2^n \times 2^n}$ and outputs a quantum circuit that prepares this exact state. 

The implementation strictly utilizes ancilla qubits, arbitrary 1-qubit gates, and multiplexed Z-rotations to achieve state purification.

## Theoretical Background
Because quantum circuits operate via unitary transformations ($U U^\dagger = I$), they inherently evolve closed systems deterministically and naturally output pure states. To output a mixed state $\rho$ (which represents a statistical ensemble with classical uncertainty), we must rely on the method of **state purification**:

1. **Spectral Decomposition:** The density matrix $\rho$ is mathematically diagonalized to extract its eigenvalues (representing classical probabilities) and its eigenvectors (the target pure states). This guarantees the ensemble is represented by perfectly distinguishable, orthogonal states.
2. **Ancilla Preparation:** A register of $n$ ancilla qubits is initialized in a superposition where the probability amplitudes are precisely the square roots of the classical eigenvalues.
3. **System Entanglement:** The $n$ system qubits are entangled with the ancilla register. This is achieved using multiplexed state preparation gates that map the main system to specific eigenvectors strictly conditioned on the isolated state of the ancillas.
4. **Partial Trace via Measurement:** The ancilla register is measured and the classical outcomes are intentionally discarded. By tracing out the ancillas (losing information to the environment), the reduced density matrix of the remaining system qubits exactly equals the target mixed state $\rho$.

## Repository Structure
* `mixed_state.py`: The main Python script containing the generalized quantum circuit function `prepare_mixed_state(rho)` and an execution block demonstrating an $n=2$ system.
* `mixed_state_demo.ipynb`: A comprehensive Jupyter Notebook containing the rigorous textbook-quality mathematical framework alongside the Qiskit implementation.
* `mixed_state_preparation_theory.tex`: The LaTeX document detailing the physical justifications and theoretical proofs for the project.
* `circuit_diagram.png`: A high-resolution architectural diagram of the generated quantum circuit for the test case.
* `README.md`: This project documentation file.

## Requirements and Installation
To execute the code in this repository, you must have Python (preferably 3.10+) installed along with the required quantum computing libraries.

If you are using an Anaconda environment, you can set up and run the project using the following steps:

**1. Create and activate a new environment:**
```bash
conda create --name qc_bootcamp python=3.10
conda activate qc_bootcamp