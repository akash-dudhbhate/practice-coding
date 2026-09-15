"""
Complete NN from scratch: forward prop, backprop, gradient descent
==================================================================
Implement a neural network from scratch (NumPy only) with:
  - Forward propagation
  - Backpropagation
  - Gradient descent
Train on the make_moons dataset. Plot decision boundary and loss curve.
Architecture: input(2) -> hidden(8, ReLU) -> output(1, sigmoid).
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def relu(x):
    return np.maximum(0, x)


def relu_deriv(x):
    return (x > 0).astype(float)


def sigmoid(x):
    x = np.clip(x, -500, 500)
    return 1 / (1 + np.exp(-x))


class NeuralNetwork:
    """2-layer NN: input(2) -> hidden(8, ReLU) -> output(1, sigmoid)."""

    def __init__(self, input_size=2, hidden_size=8, lr=0.1, seed=42):
        np.random.seed(seed)
        self.lr = lr
        self.W1 = np.random.randn(input_size, hidden_size) * 0.5
        self.b1 = np.zeros((1, hidden_size))
        self.W2 = np.random.randn(hidden_size, 1) * 0.5
        self.b2 = np.zeros((1, 1))
        self.losses = []

    def forward(self, X):
        self.z1 = X @ self.W1 + self.b1
        self.a1 = relu(self.z1)
        self.z2 = self.a1 @ self.W2 + self.b2
        self.a2 = sigmoid(self.z2)
        return self.a2

    def backward(self, X, y):
        m = X.shape[0]
        # Output layer error
        dz2 = self.a2 - y.reshape(-1, 1)          # (m, 1)
        dW2 = (self.a1.T @ dz2) / m               # (hidden, 1)
        db2 = np.sum(dz2, axis=0, keepdims=True) / m
        # Hidden layer error (backprop through ReLU)
        da1 = dz2 @ self.W2.T                      # (m, hidden)
        dz1 = da1 * relu_deriv(self.z1)            # (m, hidden)
        dW1 = (X.T @ dz1) / m                      # (input, hidden)
        db1 = np.sum(dz1, axis=0, keepdims=True) / m
        # Gradient descent update
        self.W2 -= self.lr * dW2
        self.b2 -= self.lr * db2
        self.W1 -= self.lr * dW1
        self.b1 -= self.lr * db1

    def compute_loss(self, y_true, y_pred):
        eps = 1e-7
        y_true = y_true.reshape(-1, 1)
        loss = -np.mean(y_true * np.log(y_pred + eps) + (1 - y_true) * np.log(1 - y_pred + eps))
        return loss

    def train(self, X, y, epochs=1000):
        for epoch in range(epochs):
            self.forward(X)
            self.backward(X, y)
            loss = self.compute_loss(y, self.a2)
            self.losses.append(loss)
            if (epoch + 1) % 200 == 0:
                print(f"Epoch {epoch+1}/{epochs} - Loss: {loss:.4f}")

    def predict(self, X):
        return (self.forward(X) >= 0.5).astype(int).flatten()


def plot_decision_boundary(model, X, y, title, filename):
    """Plot decision boundary of the trained model."""
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
                         np.linspace(y_min, y_max, 200))
    grid = np.c_[xx.ravel(), yy.ravel()]
    Z = model.predict(grid).reshape(xx.shape)
    plt.figure(figsize=(6, 5))
    plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.RdBu)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.RdBu, edgecolors="k")
    plt.title(title)
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.savefig(filename, dpi=100, bbox_inches="tight")
    plt.show()
    print(f"Decision boundary saved to {filename}")


if __name__ == "__main__":
    # Generate make_moons dataset
    X, y = make_moons(n_samples=500, noise=0.2, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)

    # Train the network
    nn = NeuralNetwork(input_size=2, hidden_size=8, lr=0.1)
    nn.train(X_train_s, y_train, epochs=1000)

    # Evaluate
    train_acc = np.mean(nn.predict(X_train_s) == y_train)
    test_acc = np.mean(nn.predict(X_test_s) == y_test)
    print(f"\nTrain accuracy: {train_acc:.4f}")
    print(f"Test accuracy:  {test_acc:.4f}")

    # Plot decision boundary
    plot_decision_boundary(nn, X_test_s, y_test,
                           "NN Decision Boundary (make_moons)",
                           "decision_boundary.png")

    # Plot loss curve
    plt.figure(figsize=(6, 4))
    plt.plot(nn.losses, linewidth=1.5)
    plt.title("Training Loss Curve")
    plt.xlabel("Epoch")
    plt.ylabel("Binary Cross-Entropy Loss")
    plt.grid(True, alpha=0.3)
    plt.savefig("loss_curve.png", dpi=100, bbox_inches="tight")
    plt.show()
    print("Loss curve saved to loss_curve.png")
