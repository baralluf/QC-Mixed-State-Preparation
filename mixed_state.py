import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit.library import StatePreparation

def prepare_mixed_state(rho: np.ndarray) -> QuantumCircuit:
    """
    Generates a quantum circuit that prepares a given mixed state via purification.
    
    Parameters:
    rho (np.ndarray): A 2^n x 2^n positive semi-definite Hermitian matrix with unit trace.
    
    Returns:
    QuantumCircuit: The compiled Qiskit circuit with measurements applied to the ancilla.
    """
    # Determine the system size dynamically from the input matrix
    dim = rho.shape[0]
    n = int(np.log2(dim))
    
    # 1. Classical Spectral Decomposition
    eigenvalues, eigenvectors = np.linalg.eigh(rho)
    
    # Enforce physical constraints to handle floating-point inaccuracies
    eigenvalues[eigenvalues < 0] = 0
    # Normalize eigenvalues
    eigenvalues = eigenvalues / np.sum(eigenvalues)
    
    # Calculate probability amplitudes for the ancilla register
    amplitudes = np.sqrt(eigenvalues)
    
    # Initialize the quantum registers
    qr_ancilla = QuantumRegister(n, 'Ancilla')
    qr_system = QuantumRegister(n, 'System')
    cr_ancilla = ClassicalRegister(n, 'Meas_ancilla')
    # Build the circiut
    qc = QuantumCircuit(qr_ancilla, qr_system, cr_ancilla)
    
    # Step A: Prepare the ancilla eigenvalue distribution
    ancilla_prep = StatePreparation(amplitudes)
    qc.append(ancilla_prep, qr_ancilla)
    qc.barrier()
    
    # Step B: Entangle the system register via multiplexed operations
    for i in range(dim):
        if eigenvalues[i] > 1e-10:
            target_state = eigenvectors[:, i]
            sys_prep = StatePreparation(target_state)
            
            # Create the conditioned unitary block
            c_sys_prep = sys_prep.control(num_ctrl_qubits=n)
            
            # Isolate the control state |i> using Pauli-X gates
            binary_string = format(i, f'0{n}b')
            for j, bit in enumerate(reversed(binary_string)):
                if bit == '0':
                    qc.x(qr_ancilla[j])
                    
            # Apply the entangling block
            qc.append(c_sys_prep, list(qr_ancilla) + list(qr_system))
            
            # Uncompute the X gates to restore the ancilla superposition
            for j, bit in enumerate(reversed(binary_string)):
                if bit == '0':
                    qc.x(qr_ancilla[j])
            qc.barrier()

    # Step C: Execute the partial trace
    qc.measure(qr_ancilla, cr_ancilla)
    
    return qc

# ==========================================
# Demonstration for n=2
# ==========================================
if __name__ == "__main__":
    # Define a 4x4 mixed state: 50% |00> and 50% Bell state (|00> + |11>)/sqrt(2)
    dim_demo = 4
    rho_demo = np.zeros((dim_demo, dim_demo), dtype=complex)
    rho_demo[0, 0] = 0.5
    bell = np.array([1, 0, 0, 1]) / np.sqrt(2)
    rho_demo += 0.5 * np.outer(bell, bell)
    
    # Generate the circuit
    final_circuit = prepare_mixed_state(rho_demo)
    
    # Save the circuit architecture
    final_circuit.draw(output='mpl', filename='circuit_diagram.png')
    print("Circuit compiled successfully. Open 'circuit_diagram.png' to view the architecture.")