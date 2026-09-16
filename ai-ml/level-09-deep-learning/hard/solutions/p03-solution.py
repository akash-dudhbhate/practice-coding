"""Level 09 Deep Learning — Hard P03 Solution"""

import torch
import torch.nn as nn
import torch.optim as optim

def solve():
    torch.manual_seed(42)
    # Custom CNN architecture
    model = nn.Sequential(
        # Block 1
        nn.Conv2d(3, 32, 3, padding=1), nn.BatchNorm2d(32), nn.ReLU(),
        nn.Conv2d(32, 32, 3, padding=1), nn.BatchNorm2d(32), nn.ReLU(),
        nn.MaxPool2d(2), nn.Dropout(0.25),
        # Block 2
        nn.Conv2d(32, 64, 3, padding=1), nn.BatchNorm2d(64), nn.ReLU(),
        nn.Conv2d(64, 64, 3, padding=1), nn.BatchNorm2d(64), nn.ReLU(),
        nn.MaxPool2d(2), nn.Dropout(0.25),
        # Block 3
        nn.Conv2d(64, 128, 3, padding=1), nn.BatchNorm2d(128), nn.ReLU(),
        nn.MaxPool2d(2), nn.Dropout(0.25),
        # Classifier
        nn.Flatten(),
        nn.Linear(128 * 4 * 4, 256), nn.ReLU(), nn.Dropout(0.5),
        nn.Linear(256, 10)
    )
    total_params = sum(p.numel() for p in model.parameters())
    print(f"Total parameters: {total_params}")
    # Dummy forward pass
    X = torch.randn(4, 3, 32, 32)
    output = model(X)
    print(f"Output shape: {output.shape}")
    return model

if __name__ == "__main__":
    solve()