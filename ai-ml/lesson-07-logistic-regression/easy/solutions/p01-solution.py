"""
Sigmoid Function from Scratch
=============================
Implement the sigmoid function: sigma(z) = 1 / (1 + e^(-z))
Test with various inputs and verify output is in [0, 1].
"""

import numpy as np


def sigmoid(z):
    """Compute the sigmoid function.

    sigma(z) = 1 / (1 + e^(-z))

    For very negative z, e^(-z) can overflow, so we clip.
    """
    z = np.clip(z, -500, 500)  # prevent overflow
    return 1.0 / (1.0 + np.exp(-z))


if __name__ == "__main__":
    test_values = [0, 5, -5, 100, -100]
    print("=== Sigmoid Function Test ===\n")
    print(f"{'Input':<10} {'Sigmoid':<15} {'In [0,1]?':<10}")
    print("-" * 35)

    for val in test_values:
        result = sigmoid(val)
        in_range = 0 <= result <= 1
        print(f"{val:<10} {result:<15.8f} {str(in_range):<10}")

    # Additional properties
    print("\n=== Key Properties ===")
    print(f"sigmoid(0)  = {sigmoid(0):.4f}  (should be 0.5)")
    print(f"sigmoid(5)  = {sigmoid(5):.4f}  (close to 1)")
    print(f"sigmoid(-5) = {sigmoid(-5):.4f}  (close to 0)")
    print(f"sigmoid(100)  = {sigmoid(100):.8f}  (essentially 1)")
    print(f"sigmoid(-100) = {sigmoid(-100):.8f}  (essentially 0)")

    # Symmetry: sigmoid(-z) = 1 - sigmoid(z)
    z = 3.7
    print(f"\nSymmetry check: sigmoid(-{z}) = {sigmoid(-z):.6f}")
    print(f"                 1 - sigmoid({z}) = {1 - sigmoid(z):.6f}")
    print(f"                 Match: {np.isclose(sigmoid(-z), 1 - sigmoid(z))}")
