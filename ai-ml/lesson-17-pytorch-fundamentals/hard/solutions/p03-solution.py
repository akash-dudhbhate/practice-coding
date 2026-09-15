"""
Regression pipeline with PyTorch MLP
=====================================
Non-linear regression dataset, PyTorch MLP, MSE loss, Adam optimizer.
Plot predictions vs actual. Track train/val loss.
Add dropout and show reduced overfitting.
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader, TensorDataset
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


class RegressionMLP(nn.Module):
    """MLP for regression with optional dropout."""

    def __init__(self, input_size=1, hidden_size=64, dropout=0.0):
        super().__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, hidden_size)
        self.fc3 = nn.Linear(hidden_size, 1)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.relu(self.fc2(x))
        x = self.dropout(x)
        return self.fc3(x)


def train_model(use_dropout, X_train, y_train, X_val, y_val, epochs=500):
    """Train regression MLP with or without dropout. Return model and loss history."""
    torch.manual_seed(42)
    dropout = 0.3 if use_dropout else 0.0
    model = RegressionMLP(input_size=1, hidden_size=64, dropout=dropout)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.01)

    X_t = torch.FloatTensor(X_train)
    y_t = torch.FloatTensor(y_train).reshape(-1, 1)
    X_v = torch.FloatTensor(X_val)
    y_v = torch.FloatTensor(y_val).reshape(-1, 1)

    train_losses, val_losses = [], []

    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()
        pred = model(X_t)
        loss = criterion(pred, y_t)
        loss.backward()
        optimizer.step()
        train_losses.append(loss.item())

        model.eval()
        with torch.no_grad():
            val_pred = model(X_v)
            val_loss = criterion(val_pred, y_v)
        val_losses.append(val_loss.item())

    return model, train_losses, val_losses


if __name__ == "__main__":
    # Non-linear regression: y = sin(x) + noise
    np.random.seed(42)
    X = np.sort(np.random.rand(300, 1) * 10, axis=0)
    y = np.sin(X).ravel() + np.random.randn(300) * 0.15

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    X_train2, X_val, y_train2, y_val = train_test_split(
        X_train, y_train, test_size=0.25, random_state=42
    )

    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train2)
    X_val_s = scaler.transform(X_val)
    X_test_s = scaler.transform(X_test)

    # Train without dropout (may overfit)
    print("--- Training without dropout ---")
    model_no_drop, train_loss_nd, val_loss_nd = train_model(
        False, X_train_s, y_train2, X_val_s, y_val, epochs=500
    )
    print(f"Final train loss: {train_loss_nd[-1]:.4f}, val loss: {val_loss_nd[-1]:.4f}")

    # Train with dropout (reduced overfitting)
    print("\n--- Training with dropout (p=0.3) ---")
    model_drop, train_loss_d, val_loss_d = train_model(
        True, X_train_s, y_train2, X_val_s, y_val, epochs=500
    )
    print(f"Final train loss: {train_loss_d[-1]:.4f}, val loss: {val_loss_d[-1]:.4f}")

    # Plot loss curves
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    axes[0].plot(train_loss_nd, label="Train (no dropout)", alpha=0.8)
    axes[0].plot(val_loss_nd, label="Val (no dropout)", alpha=0.8)
    axes[0].plot(train_loss_d, label="Train (dropout)", alpha=0.8, linestyle="--")
    axes[0].plot(val_loss_d, label="Val (dropout)", alpha=0.8, linestyle="--")
    axes[0].set_title("Train/Val Loss Comparison")
    axes[0].set_xlabel("Epoch")
    axes[0].set_ylabel("MSE Loss")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    # Plot predictions vs actual
    sort_idx = np.argsort(X_test_s.ravel())
    model_no_drop.eval()
    model_drop.eval()
    with torch.no_grad():
        pred_nd = model_no_drop(torch.FloatTensor(X_test_s)).numpy()
        pred_d = model_drop(torch.FloatTensor(X_test_s)).numpy()

    axes[1].scatter(X_test_s, y_test, s=10, alpha=0.5, label="Actual", color="gray")
    axes[1].plot(X_test_s.ravel()[sort_idx], pred_nd[sort_idx],
                 "r-", linewidth=2, label="No dropout")
    axes[1].plot(X_test_s.ravel()[sort_idx], pred_d[sort_idx],
                 "b--", linewidth=2, label="With dropout")
    axes[1].set_title("Predictions vs Actual")
    axes[1].set_xlabel("X (scaled)")
    axes[1].set_ylabel("y")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("regression_dropout.png", dpi=100, bbox_inches="tight")
    plt.show()
    print("\nPlot saved to regression_dropout.png")

    # Overfitting gap comparison
    gap_nd = val_loss_nd[-1] - train_loss_nd[-1]
    gap_d = val_loss_d[-1] - train_loss_d[-1]
    print(f"\n--- Overfitting Gap (val - train) ---")
    print(f"Without dropout: {gap_nd:.4f}")
    print(f"With dropout:    {gap_d:.4f}")
    print(f"Dropout reduces overfitting by randomly zeroing neurons during training,")
    print(f"forcing the network to learn more robust features.")
