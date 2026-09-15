"""
CNN architecture comparison: shallow vs medium vs deep
======================================================
Compare 3 architectures (shallow: 1 conv, medium: 2 conv, deep: 4 conv) on MNIST.
Print accuracy, parameter count, and training time. Display comparison table.
"""

import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
import time


class ShallowCNN(nn.Module):
    """1 conv layer."""

    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 16, 3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc = nn.Linear(16 * 14 * 14, 10)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.pool(self.relu(self.conv1(x)))
        x = x.view(x.size(0), -1)
        return self.fc(x)


class MediumCNN(nn.Module):
    """2 conv layers."""

    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 16, 3, padding=1)
        self.conv2 = nn.Conv2d(16, 32, 3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc = nn.Linear(32 * 7 * 7, 10)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.pool(self.relu(self.conv1(x)))
        x = self.pool(self.relu(self.conv2(x)))
        x = x.view(x.size(0), -1)
        return self.fc(x)


class DeepCNN(nn.Module):
    """4 conv layers."""

    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 16, 3, padding=1)
        self.conv2 = nn.Conv2d(16, 32, 3, padding=1)
        self.conv3 = nn.Conv2d(32, 64, 3, padding=1)
        self.conv4 = nn.Conv2d(64, 128, 3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(128 * 1 * 1, 64)
        self.fc2 = nn.Linear(64, 10)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.pool(self.relu(self.conv1(x)))   # 28 -> 14
        x = self.pool(self.relu(self.conv2(x)))   # 14 -> 7
        x = self.pool(self.relu(self.conv3(x)))   # 7 -> 3
        x = self.pool(self.relu(self.conv4(x)))   # 3 -> 1
        x = x.view(x.size(0), -1)
        x = self.relu(self.fc1(x))
        return self.fc2(x)


def train_and_eval(model, train_loader, test_loader, epochs=3, label=""):
    """Train and evaluate. Return accuracy, param count, training time."""
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    torch.manual_seed(42)
    model = model.to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    params = sum(p.numel() for p in model.parameters())

    start = time.time()
    for epoch in range(epochs):
        model.train()
        running_loss = 0.0
        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
    train_time = time.time() - start

    model.eval()
    correct, total = 0, 0
    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    acc = correct / total
    return acc, params, train_time


if __name__ == "__main__":
    torch.manual_seed(42)

    transform = transforms.Compose([transforms.ToTensor()])
    trainset = torchvision.datasets.MNIST(root="./data", train=True, download=True, transform=transform)
    testset = torchvision.datasets.MNIST(root="./data", train=False, download=True, transform=transform)
    train_loader = DataLoader(trainset, batch_size=64, shuffle=True)
    test_loader = DataLoader(testset, batch_size=64, shuffle=False)

    architectures = [
        ("Shallow (1 conv)", ShallowCNN()),
        ("Medium (2 conv)", MediumCNN()),
        ("Deep (4 conv)", DeepCNN()),
    ]

    results = []
    for name, model in architectures:
        acc, params, t = train_and_eval(model, train_loader, test_loader, epochs=3, label=name)
        results.append((name, acc, params, t))
        print(f"{name}: acc={acc:.4f}, params={params:,}, time={t:.1f}s")

    # Comparison table
    print(f"\n{'=' * 70}")
    print(f"{'Architecture':<25} {'Accuracy':<12} {'Params':<15} {'Time(s)':<10}")
    print(f"{'-' * 70}")
    for name, acc, params, t in results:
        print(f"{name:<25} {acc:<12.4f} {params:<15,} {t:<10.1f}")
    print(f"{'=' * 70}")

    print(f"\n--- Key Observations ---")
    print(f"- Shallow: fewest params, fastest, but may underfit complex data.")
    print(f"- Medium: good balance of capacity and speed for MNIST.")
    print(f"- Deep: most params, slowest, may overfit on simple MNIST but scales to harder tasks.")
    print(f"- On MNIST (simple), even shallow CNNs achieve >98%. Deeper networks shine on")
    print(f"  more complex datasets (CIFAR-10, ImageNet).")
