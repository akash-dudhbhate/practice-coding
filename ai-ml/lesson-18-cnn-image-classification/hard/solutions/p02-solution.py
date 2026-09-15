"""
Transfer learning: ResNet18 on CIFAR-10
========================================
Use a pre-trained ResNet18, adapt it for CIFAR-10 (10 classes, 32x32).
Fine-tune for 5 epochs. Compare accuracy and training time with from-scratch CNN.
"""

import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
import time
import matplotlib.pyplot as plt


def get_dataloaders(batch_size=64):
    """Get CIFAR-10 dataloaders with appropriate transforms."""
    # ResNet18 expects 224x224 input with ImageNet normalization
    train_transform = transforms.Compose([
        transforms.Resize(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    test_transform = transforms.Compose([
        transforms.Resize(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    trainset = torchvision.datasets.CIFAR10(root="./data", train=True, download=True, transform=train_transform)
    testset = torchvision.datasets.CIFAR10(root="./data", train=False, download=True, transform=test_transform)

    # Subset for faster comparison (optional: use full dataset)
    trainset = torch.utils.data.Subset(trainset, range(5000))
    testset = torch.utils.data.Subset(testset, range(1000))

    train_loader = DataLoader(trainset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(testset, batch_size=batch_size, shuffle=False)
    return train_loader, test_loader


class SimpleCNN(nn.Module):
    """Simple from-scratch CNN for comparison."""

    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 32, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2, 2),
            nn.Conv2d(32, 64, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2, 2),
            nn.Conv2d(64, 128, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2, 2),
        )
        self.classifier = nn.Sequential(
            nn.Linear(128 * 28 * 28, 256), nn.ReLU(), nn.Dropout(0.3),
            nn.Linear(256, 10)
        )

    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)
        return self.classifier(x)


def train_and_eval(model, train_loader, test_loader, epochs=5, lr=0.001, label=""):
    """Train and evaluate a model. Return accuracy and training time."""
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)

    params = sum(p.numel() for p in model.parameters())
    print(f"\n--- {label} ---")
    print(f"Parameters: {params:,}")

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
        print(f"  Epoch [{epoch+1}/{epochs}] - Loss: {running_loss/len(train_loader):.4f}")
    train_time = time.time() - start

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
    print(f"  Training Time: {train_time:.1f}s")
    return acc, train_time, params


if __name__ == "__main__":
    torch.manual_seed(42)
    train_loader, test_loader = get_dataloaders(batch_size=32)

    # --- From-scratch CNN ---
    scratch_model = SimpleCNN()
    scratch_acc, scratch_time, scratch_params = train_and_eval(
        scratch_model, train_loader, test_loader, epochs=5, label="From-scratch CNN"
    )

    # --- Transfer learning with ResNet18 ---
    from torchvision.models import resnet18, ResNet18_Weights
    weights = ResNet18_Weights.DEFAULT
    resnet = resnet18(weights=weights)
    # Freeze feature extractor (optional — can also fine-tune)
    for param in resnet.parameters():
        param.requires_grad = False
    # Replace final FC layer for 10 classes (this layer IS trainable)
    resnet.fc = nn.Linear(resnet.fc.in_features, 10)
    # Unfreeze last few layers for fine-tuning
    for param in resnet.layer4.parameters():
        param.requires_grad = True

    transfer_acc, transfer_time, transfer_params = train_and_eval(
        resnet, train_loader, test_loader, epochs=5, lr=0.001, label="Transfer Learning (ResNet18)"
    )

    # Comparison
    print(f"\n{'=' * 60}")
    print(f"--- Comparison ---")
    print(f"{'=' * 60}")
    print(f"{'Model':<25} {'Accuracy':<12} {'Time(s)':<12} {'Params':<15}")
    print(f"{'-' * 60}")
    print(f"{'From-scratch CNN':<25} {scratch_acc:<12.4f} {scratch_time:<12.1f} {scratch_params:<15,}")
    print(f"{'ResNet18 (transfer)':<25} {transfer_acc:<12.4f} {transfer_time:<12.1f} {transfer_params:<15,}")
    print(f"\nTransfer learning leverages pre-trained features (edges, textures, shapes)")
    print(f"learned on ImageNet, typically achieving higher accuracy with less training,")
    print(f"especially on small datasets.")
