"""Level 09 Deep Learning — Hard P01 Solution"""

import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import models, transforms

def solve():
    torch.manual_seed(42)
    # Load pretrained ResNet
    model = models.resnet18(pretrained=False)
    # Freeze all layers except the last
    for param in model.parameters():
        param.requires_grad = False
    model.fc = nn.Linear(512, 10)  # CIFAR-10 has 10 classes
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.fc.parameters(), lr=0.001)
    # Dummy data
    X = torch.randn(32, 3, 224, 224)
    y = torch.randint(0, 10, (32,))
    for epoch in range(3):
        optimizer.zero_grad()
        outputs = model(X)
        loss = criterion(outputs, y)
        loss.backward()
        optimizer.step()
        print(f"Epoch {epoch}: loss={loss.item():.4f}")
    print("Transfer learning complete")
    return model

if __name__ == "__main__":
    solve()