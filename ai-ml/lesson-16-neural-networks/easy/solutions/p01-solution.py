"""
Implement ReLU, sigmoid, tanh from scratch
==========================================
Plot all three activation functions on the same graph for input range -5 to 5.
Verify their output ranges.
"""

import numpy as np
import matplotlib.pyplot as plt


def relu(x):
    """ReLU: f(x) = max(0, x). Range: [0, inf)."""
    return np.maximum(0, x)


def sigmoid(x):
    """Sigmoid: f(x) = 1 / (1 + e^-x). Range: (0, 1)."""
    # Clip to avoid overflow warnings for large negative values
    x = np.clip(x, -500, 500)
    return 1 / (1 + np.exp(-x))


def tanh(x):
    """tanh: f(x) = (e^x - e^-x) / (e^x + e^-x). Range: (-1, 1)."""
    return np.tanh(x)


if __name__ == "__main__":
    # Input range -5 to 5
    x = np.linspace(-5, 5, 200)

    # Compute activations
    y_relu = relu(x)
    y_sigmoid = sigmoid(x)
    y_tanh = tanh(x)

    # Plot all three on the same graph
    plt.figure(figsize=(8, 5))
    plt.plot(x, y_relu, label="ReLU", linewidth=2)
    plt.plot(x, y_sigmoid, label="Sigmoid", linewidth=2)
    plt.plot(x, y_tanh, label="tanh", linewidth=2)
    plt.title("Activation Functions: ReLU, Sigmoid, tanh")
    plt.xlabel("Input (x)")
    plt.ylabel("Output")
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig("activation_functions.png", dpi=100, bbox_inches="tight")
    plt.show()
    print("Plot saved to activation_functions.png")

    # Verify ranges
    print("\n--- Range Verification ---")
    print(f"ReLU range:    [{y_relu.min():.4f}, {y_relu.max():.4f}]  (expected [0, 5])")
    print(f"Sigmoid range: [{y_sigmoid.min():.4f}, {y_sigmoid.max():.4f}]  (expected (0, 1))")
    print(f"tanh range:    [{y_tanh.min():.4f}, {y_tanh.max():.4f}]  (expected (-1, 1))")

    # Spot checks
    print("\n--- Spot Checks ---")
    print(f"relu(-2) = {relu(-2.0)}  (expected 0)")
    print(f"relu(3)  = {relu(3.0)}  (expected 3)")
    print(f"sigmoid(0) = {sigmoid(0.0):.4f}  (expected 0.5)")
    print(f"tanh(0) = {tanh(0.0):.4f}  (expected 0)")
