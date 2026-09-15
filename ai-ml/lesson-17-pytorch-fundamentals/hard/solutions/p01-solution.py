"""
Complete PyTorch training pipeline
===================================
Custom dataset, DataLoader, 3-layer network, train/val split,
loss tracking, early stopping, test evaluation.
Print train/val/test accuracy.
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader, Subset
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np


class CustomDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.FloatTensor(X)
        self.y = torch.LongTensor(y)

    def __len__(self):
        return len(self.y)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]


class ThreeLayerNN(nn.Module):
    """3-layer network: 20 -> 64 -> 32 -> 2."""

    def __init__(self, input_size=20):
        super().__init__()
        self.fc1 = nn.Linear(input_size, 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, 2)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        return self.fc3(x)


def evaluate_accuracy(model, loader):
    """Compute accuracy on a DataLoader."""
    model.eval()
    correct, total = 0, 0
    with torch.no_grad():
        for X, y in loader:
            outputs = model(X)
            _, predicted = torch.max(outputs, 1)
            total += y.size(0)
            correct += (predicted == y).sum().item()
    return correct / total


if __name__ == "__main__":
    torch.manual_seed(42)

    # Generate dataset
    X, y = make_classification(
        n_samples=1000, n_features=20, n_informative=10,
        n_classes=2, random_state=42
    )

    # Three-way split: train/val/test (60/20/20)
    X_temp, X_test, y_temp, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    X_train, X_val, y_train, y_val = train_test_split(
        X_temp, y_temp, test_size=0.25, random_state=42  # 0.25 * 0.8 = 0.2
    )

    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_val_s = scaler.transform(X_val)
    X_test_s = scaler.transform(X_test)

    train_ds = CustomDataset(X_train_s, y_train)
    val_ds = CustomDataset(X_val_s, y_val)
    test_ds = CustomDataset(X_test_s, y_test)

    train_loader = DataLoader(train_ds, batch_size=32, shuffle=True)
    val_loader = DataLoader(val_ds, batch_size=32, shuffle=False)
    test_loader = DataLoader(test_ds, batch_size=32, shuffle=False)

    print(f"Train: {len(train_ds)}, Val: {len(val_ds)}, Test: {len(test_ds)}")

    # Model, loss, optimizer
    model = ThreeLayerNN(input_size=20)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # Training with early stopping
    max_epochs = 100
    patience = 10
    best_val_loss = float("inf")
    patience_counter = 0
    best_state = None

    train_losses, val_losses = [], []

    for epoch in range(max_epochs):
        # Train
        model.train()
        epoch_loss = 0.0
        for X_batch, y_batch in train_loader:
            optimizer.zero_grad()
            outputs = model(X_batch)
            loss = criterion(outputs, y_batch)
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item()
        train_loss = epoch_loss / len(train_loader)
        train_losses.append(train_loss)

        # Validate
        model.eval()
        val_loss = 0.0
        with torch.no_grad():
            for X_batch, y_batch in val_loader:
                outputs = model(X_batch)
                val_loss += criterion(outputs, y_batch).item()
        val_loss /= len(val_loader)
        val_losses.append(val_loss)

        if (epoch + 1) % 10 == 0:
            train_acc = evaluate_accuracy(model, train_loader)
            val_acc = evaluate_accuracy(model, val_loader)
            print(f"Epoch [{epoch+1}/{max_epochs}] - "
                  f"Train Loss: {train_loss:.4f} - Val Loss: {val_loss:.4f} - "
                  f"Train Acc: {train_acc:.4f} - Val Acc: {val_acc:.4f}")

        # Early stopping check
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            patience_counter = 0
            best_state = model.state_dict().copy()
        else:
            patience_counter += 1
            if patience_counter >= patience:
                print(f"\nEarly stopping at epoch {epoch+1} (patience={patience})")
                break

    # Restore best model
    model.load_state_dict(best_state)

    # Final evaluation
    train_acc = evaluate_accuracy(model, train_loader)
    val_acc = evaluate_accuracy(model, val_loader)
    test_acc = evaluate_accuracy(model, test_loader)

    print(f"\n--- Final Accuracy ---")
    print(f"Train: {train_acc:.4f}")
    print(f"Val:   {val_acc:.4f}")
    print(f"Test:  {test_acc:.4f}")
