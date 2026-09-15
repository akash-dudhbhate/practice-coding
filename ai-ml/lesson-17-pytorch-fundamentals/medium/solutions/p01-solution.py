"""
2-layer NN with nn.Module
=========================
Build a 2-layer neural network (10 -> 64 -> 2) with ReLU using nn.Module.
Train on a synthetic dataset for 100 epochs with SGD. Print loss every 10 epochs.
"""

import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


class TwoLayerNN(nn.Module):
    """2-layer network: input(10) -> hidden(64, ReLU) -> output(2)."""

    def __init__(self, input_size=10, hidden_size=64, num_classes=2):
        super().__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x


if __name__ == "__main__":
    torch.manual_seed(42)

    # Synthetic dataset: 10 features, 2 classes
    X, y = make_classification(
        n_samples=500, n_features=10, n_informative=5,
        n_classes=2, random_state=42
    )
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)

    # Convert to tensors
    X_train_t = torch.FloatTensor(X_train_s)
    y_train_t = torch.LongTensor(y_train)
    X_test_t = torch.FloatTensor(X_test_s)
    y_test_t = torch.LongTensor(y_test)

    # Initialize model, loss, optimizer
    model = TwoLayerNN(input_size=10, hidden_size=64, num_classes=2)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.1)

    print("--- Training 2-Layer NN (10 -> 64 -> 2) ---")
    print(f"Epochs: 100, Optimizer: SGD, LR: 0.1\n")

    # Training loop
    epochs = 100
    for epoch in range(epochs):
        # Forward
        outputs = model(X_train_t)
        loss = criterion(outputs, y_train_t)

        # Backward
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if (epoch + 1) % 10 == 0:
            # Compute training accuracy
            _, predicted = torch.max(outputs, 1)
            acc = (predicted == y_train_t).float().mean().item()
            print(f"Epoch [{epoch+1}/{epochs}] - Loss: {loss.item():.4f} - Train Acc: {acc:.4f}")

    # Final test accuracy
    model.eval()
    with torch.no_grad():
        test_outputs = model(X_test_t)
        _, test_pred = torch.max(test_outputs, 1)
        test_acc = (test_pred == y_test_t).float().mean().item()
    print(f"\nFinal Test Accuracy: {test_acc:.4f}")
