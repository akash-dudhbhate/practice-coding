"""
Single-layer nn.Module (Linear)
================================
Create a single linear layer (5 inputs, 1 output) using nn.Module.
Pass random input through it. Print output. No training.
"""

import torch
import torch.nn as nn


if __name__ == "__main__":
    # Set seed for reproducibility
    torch.manual_seed(42)

    # Define a single linear layer: 5 inputs -> 1 output
    layer = nn.Linear(in_features=5, out_features=1)

    print("--- Linear Layer ---")
    print(f"Input features:  5")
    print(f"Output features: 1")
    print(f"\nWeight shape: {layer.weight.shape}  (out_features, in_features)")
    print(f"Bias shape:   {layer.bias.shape}  (out_features,)")
    print(f"Weights:\n{layer.weight.data}")
    print(f"Bias: {layer.bias.data}")

    # Create random input: batch of 3 samples, each with 5 features
    x = torch.randn(3, 5)
    print(f"\n--- Input ---")
    print(f"Input shape: {x.shape}")
    print(f"Input:\n{x}")

    # Forward pass
    output = layer(x)
    print(f"\n--- Output ---")
    print(f"Output shape: {output.shape}")
    print(f"Output:\n{output}")

    # Manual computation to verify
    manual = x @ layer.weight.data.T + layer.bias.data
    print(f"\nManual (x @ W^T + b):\n{manual}")
    print(f"Match: {torch.allclose(output, manual)}")
