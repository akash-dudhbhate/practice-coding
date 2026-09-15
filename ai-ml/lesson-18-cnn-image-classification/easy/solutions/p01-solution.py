"""
Load MNIST with torchvision
============================
Load the MNIST dataset using torchvision. Visualize 5 samples with labels
using matplotlib. Print the shape of a single image tensor.
"""

import torch
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":
    # Define transform: convert to tensor and normalize
    transform = transforms.Compose([
        transforms.ToTensor(),
    ])

    # Load MNIST training set
    trainset = torchvision.datasets.MNIST(
        root="./data", train=True, download=True, transform=transform
    )

    print(f"MNIST training set size: {len(trainset)}")
    print(f"Classes: {trainset.classes}")

    # Get a single image and inspect its tensor shape
    image, label = trainset[0]
    print(f"\nSingle image tensor shape: {image.shape}")
    print(f"  (channels, height, width) = ({image.shape[0]}, {image.shape[1]}, {image.shape[2]})")
    print(f"  Label: {label} ({trainset.classes[label]})")
    print(f"  Tensor dtype: {image.dtype}")
    print(f"  Min pixel: {image.min():.4f}, Max pixel: {image.max():.4f}")

    # Visualize 5 samples with labels
    fig, axes = plt.subplots(1, 5, figsize=(12, 3))
    for i in range(5):
        img, lbl = trainset[i]
        # img shape is (1, 28, 28), squeeze to (28, 28) for display
        axes[i].imshow(img.squeeze(), cmap="gray")
        axes[i].set_title(f"Label: {lbl}")
        axes[i].axis("off")

    plt.suptitle("MNIST Samples")
    plt.tight_layout()
    plt.savefig("mnist_samples.png", dpi=100, bbox_inches="tight")
    plt.show()
    print("\nPlot saved to mnist_samples.png")
