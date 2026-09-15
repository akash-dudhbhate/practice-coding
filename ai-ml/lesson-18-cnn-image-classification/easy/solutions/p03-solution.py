"""
MaxPool2d layer on 28x28 tensor
================================
Apply a MaxPool2d layer (2x2) to a 28x28 tensor.
Print input/output shapes. Verify spatial dimensions are halved.
"""

import torch
import torch.nn as nn


if __name__ == "__main__":
    # Create a 28x28 tensor (simulating a single-channel MNIST image with batch dim)
    x = torch.randn(1, 1, 28, 28)
    print(f"Input shape:  {x.shape}  (batch, channels, height, width)")

    # Define MaxPool2d with 2x2 kernel
    pool = nn.MaxPool2d(kernel_size=2, stride=2)
    print(f"\nMaxPool2d config: kernel_size=2, stride=2")

    # Forward pass
    output = pool(x)
    print(f"Output shape: {output.shape}")
    print(f"\n--- Spatial Dimension Verification ---")
    print(f"Input H x W:  {x.shape[2]} x {x.shape[3]}")
    print(f"Output H x W: {output.shape[2]} x {output.shape[3]}")
    print(f"Expected:      {x.shape[2] // 2} x {x.shape[3] // 2}  (halved by 2x2 pooling)")
    print(f"Correct: {output.shape[2] == 14 and output.shape[3] == 14}")

    # Demonstrate with a small example to show how max pooling works
    print(f"\n--- Small Example ---")
    small = torch.tensor([[[[1.0, 2, 3, 4],
                             5, 6, 7, 8],
                            [9, 10, 11, 12],
                            [13, 14, 15, 16]]]]).reshape(1, 1, 4, 4)
    print(f"Input (4x4):\n{small[0, 0]}")
    pooled = pool(small)
    print(f"Output (2x2):\n{pooled[0, 0]}")
    print(f"\nEach output value = max of the corresponding 2x2 region:")
    print(f"  max(1,2,5,6)={max(1,2,5,6)}, max(3,4,7,8)={max(3,4,7,8)},")
    print(f"  max(9,10,13,14)={max(9,10,13,14)}, max(11,12,15,16)={max(11,12,15,16)}")
