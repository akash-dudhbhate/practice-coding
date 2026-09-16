"""Level 09 — Deep Learning — Easy P02 Solution"""

import torch
import torch.nn as nn

def build_cnn():
    return nn.Sequential(
        nn.Conv2d(1, 16, kernel_size=3, padding=1),
        nn.ReLU(),
        nn.MaxPool2d(2),
        nn.Conv2d(16, 32, kernel_size=3, padding=1),
        nn.ReLU(),
        nn.MaxPool2d(2),
        nn.Flatten(),
        nn.Linear(32 * 7 * 7, 128),
        nn.ReLU(),
        nn.Linear(128, 10)
    )

if __name__ == "__main__":
    model = build_cnn()
    print(model[0])
    x = torch.randn(1, 1, 28, 28)
    print(model(x).shape)
