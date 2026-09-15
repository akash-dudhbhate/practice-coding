"""
Single neuron from scratch
==========================
Implement a single neuron: weighted sum + bias, then sigmoid activation.
Test with 3 inputs, 3 weights, and a bias. Print the output.
"""

import numpy as np


def sigmoid(x):
    """Sigmoid activation: 1 / (1 + e^-x)."""
    x = np.clip(x, -500, 500)
    return 1 / (1 + np.exp(-x))


def single_neuron(inputs, weights, bias):
    """
    Compute output of a single neuron.

    z = sum(inputs * weights) + bias
    output = sigmoid(z)
    """
    z = np.dot(inputs, weights) + bias
    return sigmoid(z)


if __name__ == "__main__":
    # Define 3 inputs, 3 weights, and a bias
    inputs = np.array([0.5, -1.2, 0.8])
    weights = np.array([0.4, 0.9, -0.3])
    bias = 0.1

    print("--- Single Neuron ---")
    print(f"Inputs:  {inputs}")
    print(f"Weights: {weights}")
    print(f"Bias:    {bias}")

    # Compute weighted sum (pre-activation)
    z = np.dot(inputs, weights) + bias
    print(f"\nWeighted sum (z): {z:.4f}")

    # Compute output
    output = single_neuron(inputs, weights, bias)
    print(f"Neuron output (sigmoid(z)): {output:.4f}")

    # Manual verification
    manual_z = (0.5 * 0.4) + (-1.2 * 0.9) + (0.8 * -0.3) + 0.1
    manual_output = 1 / (1 + np.exp(-manual_z))
    print(f"\nManual verification:")
    print(f"  z = 0.5*0.4 + (-1.2)*0.9 + 0.8*(-0.3) + 0.1 = {manual_z:.4f}")
    print(f"  sigmoid(z) = {manual_output:.4f}")
    print(f"  Match: {np.isclose(output, manual_output)}")
