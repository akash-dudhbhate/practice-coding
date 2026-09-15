"""
Single Conv2d layer on MNIST image
===================================
Apply a single Conv2d layer (1 -> 16 channels, 3x3 kernel) to a 28x28 MNIST image.
Print input/output shapes. Visualize feature maps.
"""

import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt


if __name__ == "__main__":
    # Load a single MNIST image
    transform = transforms.Compose([transforms.ToTensor()])
    trainset = torchvision.datasets.MNIST(
        root="./data", train=True, download=True, transform=transform
    )
    image, label = trainset[0]

    # Add batch dimension: (1, 1, 28, 28)
    x = image.unsqueeze(0)
    print(f"Input shape:  {x.shape}  (batch, channels, height, width)")

    # Define a single Conv2d layer: 1 input channel -> 16 output channels, 3x3 kernel
    conv = nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3, padding=1)
    print(f"\nConv2d config: in_channels=1, out_channels=16, kernel_size=3, padding=1")
    print(f"Weight shape: {conv.weight.shape}  (out_channels, in_channels, kH, kW)")
    print(f"Bias shape:   {conv.bias.shape}")

    # Forward pass
    output = conv(x)
    print(f"\nOutput shape: {output.shape}  (batch, channels, height, width)")
    print(f"  Spatial dims preserved due to padding=1: 28x28 -> 28x28")
    print(f"  Channels expanded: 1 -> 16")

    # Visualize feature maps (first 8 channels)
    fig, axes = plt.subplots(2, 5, figsize=(12, 5))
    # Original image
    axes[0, 0].imshow(x[0, 0].numpy(), cmap="gray")
    axes[0, 0].set_title("Original")
    axes[0, 0].axis("off")

    # Feature maps
    feature_maps = output[0].detach().numpy()
    for i in range(8):
        row, col = (i + 1) // 5, (i + 1) % 5
        axes[row, col].imshow(feature_maps[i], cmap="viridis")
        axes[row, col].set_title(f"Filter {i}")
        axes[row, col].axis("off")

    axes[1, 4].axis("off")
    plt.suptitle("Conv2d Feature Maps (1 -> 16 channels, 3x3 kernel)")
    plt.tight_layout()
    plt.savefig("conv_feature_maps.png", dpi=100, bbox_inches="tight")
    plt.show()
    print("\nFeature maps saved to conv_feature_maps.png")
