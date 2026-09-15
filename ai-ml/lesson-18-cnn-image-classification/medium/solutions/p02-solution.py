"""
Data augmentation on MNIST
===========================
Apply RandomRotation and RandomAffine augmentation to MNIST.
Train the same CNN with and without augmentation. Compare accuracy.
"""

import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader


class SimpleCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 16, kernel_size=3, padding=1)
        self.pool1 = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, padding=1)
        self.pool2 = nn.MaxPool2d(2, 2)
        self.fc = nn.Linear(32 * 7 * 7, 10)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.pool1(self.relu(self.conv1(x)))
        x = self.pool2(self.relu(self.conv2(x)))
        x = x.view(x.size(0), -1)
        return self.fc(x)


def train_and_evaluate(train_loader, test_loader, epochs=3, label=""):
    """Train CNN and return test accuracy."""
    torch.manual_seed(42)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = SimpleCNN().to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    print(f"\n--- Training {label} ---")
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
        print(f"  Epoch [{epoch+1}/{epochs}] - Loss: {running_loss/len(train_loader):.4f}")

    # Evaluate
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
    print(f"  Test Accuracy: {acc:.4f}")
    return acc


if __name__ == "__main__":
    # Transforms
    basic_transform = transforms.Compose([transforms.ToTensor()])

    augment_transform = transforms.Compose([
        transforms.RandomRotation(degrees=10),
        transforms.RandomAffine(degrees=0, translate=(0.1, 0.1)),
        transforms.ToTensor(),
    ])

    # Test transform is always basic (no augmentation on test)
    test_transform = transforms.Compose([transforms.ToTensor()])

    # Datasets
    train_basic = torchvision.datasets.MNIST(root="./data", train=True, download=True, transform=basic_transform)
    train_aug = torchvision.datasets.MNIST(root="./data", train=True, download=True, transform=augment_transform)
    testset = torchvision.datasets.MNIST(root="./data", train=False, download=True, transform=test_transform)

    train_loader_basic = DataLoader(train_basic, batch_size=64, shuffle=True)
    train_loader_aug = DataLoader(train_aug, batch_size=64, shuffle=True)
    test_loader = DataLoader(testset, batch_size=64, shuffle=False)

    # Train without augmentation
    acc_basic = train_and_evaluate(train_loader_basic, test_loader, epochs=3, label="WITHOUT augmentation")

    # Train with augmentation
    acc_aug = train_and_evaluate(train_loader_aug, test_loader, epochs=3, label="WITH augmentation")

    # Comparison
    print(f"\n{'=' * 50}")
    print(f"--- Comparison ---")
    print(f"{'=' * 50}")
    print(f"Without augmentation: {acc_basic:.4f}")
    print(f"With augmentation:    {acc_aug:.4f}")
    print(f"Difference:           {acc_aug - acc_basic:+.4f}")
    print(f"\nNote: Augmentation artificially expands training data with realistic")
    print(f"variations (rotation, translation), improving generalization. On MNIST")
    print(f"(which is already clean), gains may be modest, but augmentation shines")
    print(f"on smaller or more varied datasets.")
