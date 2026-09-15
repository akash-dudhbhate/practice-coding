"""
Logistic Regression from Scratch with Gradient Descent
======================================================
Implement sigmoid, log-loss cost function, and gradient descent.
Train on 2D synthetic data, plot the loss curve and decision boundary.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification


def sigmoid(z):
    """Sigmoid function with overflow protection."""
    z = np.clip(z, -500, 500)
    return 1.0 / (1.0 + np.exp(-z))


def log_loss(y_true, y_pred):
    """Binary cross-entropy (log loss).

    L = -(1/n) * sum[y*log(p) + (1-y)*log(1-p)]
    """
    eps = 1e-15
    y_pred = np.clip(y_pred, eps, 1 - eps)
    return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))


def train_logistic_regression(X, y, lr=0.1, iterations=1000):
    """Train logistic regression via gradient descent.

    Returns weights, bias, and loss history.
    """
    n_samples, n_features = X.shape
    w = np.zeros(n_features)
    b = 0.0
    loss_history = []

    for _ in range(iterations):
        z = np.dot(X, w) + b
        y_pred = sigmoid(z)

        # Gradients
        dw = (1 / n_samples) * np.dot(X.T, (y_pred - y))
        db = (1 / n_samples) * np.sum(y_pred - y)

        # Update
        w -= lr * dw
        b -= lr * db

        loss_history.append(log_loss(y, y_pred))

    return w, b, loss_history


def predict(X, w, b, threshold=0.5):
    """Predict class labels."""
    return (sigmoid(np.dot(X, w) + b) >= threshold).astype(int)


if __name__ == "__main__":
    X, y = make_classification(
        n_samples=300, n_features=2, n_informative=2, n_redundant=0,
        n_clusters_per_class=1, random_state=42
    )

    w, b, loss_history = train_logistic_regression(X, y, lr=0.1, iterations=1000)
    y_pred = predict(X, w, b)
    accuracy = np.mean(y_pred == y)

    print(f"Final weights: {w}")
    print(f"Final bias:    {b:.4f}")
    print(f"Final loss:    {loss_history[-1]:.6f}")
    print(f"Accuracy:      {accuracy:.4f}")

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Plot 1: Loss curve
    axes[0].plot(loss_history, color="blue")
    axes[0].set_xlabel("Iteration")
    axes[0].set_ylabel("Log Loss")
    axes[0].set_title("Training Loss Curve")
    axes[0].grid(True, alpha=0.3)

    # Plot 2: Decision boundary
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                         np.arange(y_min, y_max, 0.02))
    Z = predict(np.c_[xx.ravel(), yy.ravel()], w, b).reshape(xx.shape)

    axes[1].contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.RdYlBu)
    axes[1].scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.RdYlBu,
                    edgecolors="black", s=30)
    axes[1].set_xlabel("Feature 1")
    axes[1].set_ylabel("Feature 2")
    axes[1].set_title("Decision Boundary")

    plt.tight_layout()
    plt.savefig("logistic_regression_scratch.png", dpi=150)
    plt.show()
    print("Plots saved to logistic_regression_scratch.png")
