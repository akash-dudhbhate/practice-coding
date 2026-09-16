"""Level 09 Deep Learning — Hard P02 Solution"""

import torch
from torchvision import transforms
import numpy as np
from PIL import Image

def solve():
    # Data augmentation pipeline
    transform = transforms.Compose([
        transforms.RandomHorizontalFlip(p=0.5),
        transforms.RandomRotation(15),
        transforms.RandomCrop(32, padding=4),
        transforms.ColorJitter(brightness=0.2, contrast=0.2),
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])
    print("Augmentation pipeline:")
    print(transform)
    # Apply to a dummy image
    img = Image.fromarray(np.random.randint(0, 255, (32, 32, 3), dtype=np.uint8))
    augmented = transform(img)
    print(f"Original size: {img.size}")
    print(f"Augmented shape: {augmented.shape}")
    return transform

if __name__ == "__main__":
    solve()