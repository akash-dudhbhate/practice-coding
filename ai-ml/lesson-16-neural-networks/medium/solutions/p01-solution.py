"""
Forward propagation for 2-layer network from scratch
=====================================================
Implement forward propagation for a 2-layer network:
  input(3) -> hidden(4, ReLU) -> output(1, sigmoid)
Use random weights. Print output for a batch of inputs.
"""

import numpy as np


def relu(x):
    """ReLU activation."""
    return np.maximum(0, x)


def sigmoid(x):
    """Sigmoid activation."""
    x = np.clip(x, -500, 500)
    return 1 / (1 + np.exp(-x))


def forward_propagation(X, W1, b1, W2, b2):
    """
    Forward pass through a 2-layer network.

    X:  input  (batch_size, 3)
    W1: weights input->hidden  (3, 4)
    b1: bias hidden  (4,)
    W2: weights hidden->output  (4, 1)
    b2: bias output  (1,)

    Returns: output (batch_size, 1)
    """
    # Hidden layer: z1 = X @ W1 + b1, a1 = relu(z1)
    z1 = X @ W1 + b1
    a1 = relu(z1)

    # Output layer: z2 = a1 @ W2 + b2, a2 = sigmoid(z2)
    z2 = a1 @ W2 + b2
    a2 = sigmoid(z2)

    return a2


if __name__ == "__main__":
    np.random.seed(42)

    # Network dimensions: input(3) -> hidden(4) -> output(1)
    # Random weights and biases
    W1 = np.random.randn(3, 4) * 0.5   # (3, 4)
    b1 = np.zeros(4)                    # (4,)
    W2 = np.random.randn(4, 1) * 0.5   # (4, 1)
    b2 = np.zeros(1)                    # (1,)

    print("--- Network Architecture ---")
    print(f"Input:  3 features")
    print(f"Hidden: 4 neurons (ReLU)")
    print(f"Output: 1 neuron  (sigmoid)")
    print(f"\nWeights W1 shape: {W1.shape}")
    print(f"Weights W2 shape: {W2.shape}")

    # Batch of 5 input samples
    X_batch = np.random.randn(5, 3)
    print(f"\nInput batch shape: {X_batch.shape}")
    print(f"Input batch:\n{X_batch}")

    # Forward propagation
    output = forward_propagation(X_batch, W1, b1, W2, b2)

    print(f"\n--- Forward Propagation Output ---")
    print(f"Output shape: {output.shape}")
    print(f"Outputs (sigmoid, range 0-1):")
    for i, val in enumerate(output.flatten()):
        print(f"  Sample {i}: {val:.4f}")
