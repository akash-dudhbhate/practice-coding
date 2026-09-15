"""
NN from scratch using only tensors and autograd (no nn.Module)
================================================================
Implement a neural network using raw tensors with requires_grad=True.
Manual forward and backward passes (using autograd for gradients).
Train on make_moons. Plot decision boundary.
"""

import torch
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def train_nn(X_train, y_train, epochs=1000, lr=0.1, hidden_size=16):
    """Train a 2-layer NN using only tensors and autograd."""
    torch.manual_seed(42)
    input_size = X_train.shape[1]

    # Initialize weights as tensors with requires_grad
    W1 = torch.randn(input_size, hidden_size, requires_grad=True)
    b1 = torch.zeros(hidden_size, requires_grad=True)
    W2 = torch.randn(hidden_size, 1, requires_grad=True)
    b2 = torch.zeros(1, requires_grad=True)

    X = torch.FloatTensor(X_train)
    y = torch.FloatTensor(y_train).reshape(-1, 1)

    losses = []
    for epoch in range(epochs):
        # Forward pass (builds computation graph)
        z1 = X @ W1 + b1
        a1 = torch.relu(z1)
        z2 = a1 @ W2 + b2
        a2 = torch.sigmoid(z2)

        # Binary cross-entropy loss
        eps = 1e-7
        loss = -torch.mean(y * torch.log(a2 + eps) + (1 - y) * torch.log(1 - a2 + eps))
        losses.append(loss.item())

        # Backward pass (autograd computes gradients)
        loss.backward()

        # Manual gradient descent update (no optimizer)
        with torch.no_grad():
            W1 -= lr * W1.grad
            b1 -= lr * b1.grad
            W2 -= lr * W2.grad
            b2 -= lr * b2.grad

            # Zero gradients for next iteration
            W1.grad.zero_()
            b1.grad.zero_()
            W2.grad.zero_()
            b2.grad.zero_()

        if (epoch + 1) % 200 == 0:
            print(f"Epoch {epoch+1}/{epochs} - Loss: {loss.item():.4f}")

    # Return parameters as a dict and loss history
    params = {"W1": W1.detach(), "b1": b1.detach(),
              "W2": W2.detach(), "b2": b2.detach()}
    return params, losses


def predict(params, X):
    """Predict using trained parameters."""
    X_t = torch.FloatTensor(X)
    with torch.no_grad():
        z1 = X_t @ params["W1"] + params["b1"]
        a1 = torch.relu(z1)
        z2 = a1 @ params["W2"] + params["b2"]
        a2 = torch.sigmoid(z2)
    return (a2.numpy() >= 0.5).astype(int).flatten()


def plot_decision_boundary(params, X, y, filename):
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
                         np.linspace(y_min, y_max, 200))
    grid = np.c_[xx.ravel(), yy.ravel()]
    Z = predict(params, grid).reshape(xx.shape)

    plt.figure(figsize=(6, 5))
    plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.RdBu)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.RdBu, edgecolors="k")
    plt.title("NN from Scratch (tensors + autograd) — make_moons")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.savefig(filename, dpi=100, bbox_inches="tight")
    plt.show()
    print(f"Decision boundary saved to {filename}")


if __name__ == "__main__":
    # Generate make_moons
    X, y = make_moons(n_samples=500, noise=0.2, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)

    # Train
    params, losses = train_nn(X_train_s, y_train, epochs=1000, lr=0.1, hidden_size=16)

    # Evaluate
    train_acc = np.mean(predict(params, X_train_s) == y_train)
    test_acc = np.mean(predict(params, X_test_s) == y_test)
    print(f"\nTrain accuracy: {train_acc:.4f}")
    print(f"Test accuracy:  {test_acc:.4f}")

    # Plot decision boundary
    plot_decision_boundary(params, X_test_s, y_test, "autograd_nn_boundary.png")

    # Plot loss curve
    plt.figure(figsize=(6, 4))
    plt.plot(losses, linewidth=1.5)
    plt.title("Training Loss (autograd NN)")
    plt.xlabel("Epoch")
    plt.ylabel("BCE Loss")
    plt.grid(True, alpha=0.3)
    plt.savefig("autograd_nn_loss.png", dpi=100, bbox_inches="tight")
    plt.show()
    print("Loss curve saved to autograd_nn_loss.png")
