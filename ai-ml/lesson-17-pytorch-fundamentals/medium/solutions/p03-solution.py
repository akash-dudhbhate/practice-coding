"""
Compare optimizers: SGD, SGD+momentum, Adam
============================================
Train the same network with three different optimizers.
Plot loss curves. Identify the fastest converging optimizer.
"""

import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


class SimpleNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(10, 64)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(64, 2)

    def forward(self, x):
        return self.fc2(self.relu(self.fc1(x)))


def train_with_optimizer(optimizer_name, X_train, y_train, epochs=100):
    """Train model with given optimizer, return loss history."""
    torch.manual_seed(42)
    model = SimpleNN()
    criterion = nn.CrossEntropyLoss()

    if optimizer_name == "SGD":
        opt = torch.optim.SGD(model.parameters(), lr=0.01)
    elif optimizer_name == "SGD+momentum":
        opt = torch.optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
    elif optimizer_name == "Adam":
        opt = torch.optim.Adam(model.parameters(), lr=0.01)
    else:
        raise ValueError(f"Unknown optimizer: {optimizer_name}")

    losses = []
    for epoch in range(epochs):
        model.train()
        outputs = model(X_train)
        loss = criterion(outputs, y_train)
        opt.zero_grad()
        loss.backward()
        opt.step()
        losses.append(loss.item())

    return losses


if __name__ == "__main__":
    # Prepare data
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

    X_train_t = torch.FloatTensor(X_train_s)
    y_train_t = torch.LongTensor(y_train)

    # Train with each optimizer
    optimizers = ["SGD", "SGD+momentum", "Adam"]
    all_losses = {}
    print("--- Optimizer Comparison (100 epochs) ---\n")

    for opt_name in optimizers:
        losses = train_with_optimizer(opt_name, X_train_t, y_train_t, epochs=100)
        all_losses[opt_name] = losses
        print(f"{opt_name:<20} Final loss: {losses[-1]:.4f}  "
              f"(loss at epoch 10: {losses[9]:.4f})")

    # Plot loss curves
    plt.figure(figsize=(8, 5))
    for opt_name, losses in all_losses.items():
        plt.plot(losses, label=opt_name, linewidth=2)
    plt.title("Optimizer Comparison: Loss Curves")
    plt.xlabel("Epoch")
    plt.ylabel("Cross-Entropy Loss")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig("optimizer_comparison.png", dpi=100, bbox_inches="tight")
    plt.show()
    print("\nPlot saved to optimizer_comparison.png")

    # Identify fastest converging (lowest loss at epoch 10)
    fastest = min(all_losses, key=lambda k: all_losses[k][9])
    print(f"\nFastest converging optimizer (by epoch 10 loss): {fastest}")
    print(f"\nExplanation:")
    print(f"  - SGD: vanilla gradient descent, slow and may get stuck.")
    print(f"  - SGD+momentum: accelerates in consistent gradient directions, faster.")
    print(f"  - Adam: adaptive per-parameter learning rates, typically fastest convergence.")
