"""
SVM from Scratch with Gradient Descent (Hinge Loss)
====================================================
Implement a linear SVM from scratch using hinge loss and gradient descent.
Implement the loss function and its gradient. Train on 2D data, plot the
boundary and margin, and compare with sklearn's SVC.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

np.random.seed(42)


class SVMScratch:
    """Linear SVM using hinge loss and gradient descent."""

    def __init__(self, learning_rate=0.001, lambda_param=0.01, n_iters=1000):
        self.lr = learning_rate
        self.lambda_param = lambda_param  # regularization strength
        self.n_iters = n_iters
        self.w = None
        self.b = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        # Convert labels: {0,1} -> {-1,+1}
        y_ = np.where(y == 0, -1, 1)

        self.w = np.zeros(n_features)
        self.b = 0.0

        for _ in range(self.n_iters):
            for idx in range(n_samples):
                condition = y_[idx] * (np.dot(X[idx], self.w) + self.b) >= 1
                if condition:
                    # Only regularization gradient
                    dw = 2 * self.lambda_param * self.w
                    db = 0.0
                else:
                    # Hinge loss + regularization gradient
                    dw = 2 * self.lambda_param * self.w - np.dot(X[idx], y_[idx])
                    db = -y_[idx]
                self.w -= self.lr * dw
                self.b -= self.lr * db

    def predict(self, X):
        linear_output = np.dot(X, self.w) + self.b
        return np.where(linear_output >= 0, 1, 0)

    def decision_function(self, X):
        return np.dot(X, self.w) + self.b


if __name__ == "__main__":
    # Linearly separable 2D data
    X, y = make_blobs(n_samples=200, centers=2, n_features=2, random_state=42, cluster_std=1.0)
    # Labels are 0/1; our SVM uses 0/1 -> {-1,+1} internally

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # --- From scratch ---
    svm_scratch = SVMScratch(learning_rate=0.001, lambda_param=0.01, n_iters=500)
    svm_scratch.fit(X_scaled, y)
    y_pred_scratch = svm_scratch.predict(X_scaled)
    acc_scratch = accuracy_score(y, y_pred_scratch)

    # --- Sklearn ---
    svm_sklearn = SVC(kernel="linear", random_state=42)
    svm_sklearn.fit(X_scaled, y)
    y_pred_sklearn = svm_sklearn.predict(X_scaled)
    acc_sklearn = accuracy_score(y, y_pred_sklearn)

    print("=== SVM Comparison ===")
    print(f"From scratch: {acc_scratch:.4f}")
    print(f"Sklearn SVC:  {acc_sklearn:.4f}")
    print(f"Scratch weights: {svm_scratch.w}, bias: {svm_scratch.b:.4f}")
    print(f"Sklearn weights: {svm_sklearn.coef_[0]}, bias: {svm_sklearn.intercept_[0]:.4f}")

    # --- Plot boundary and margins ---
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    for ax, model, title, acc in [
        (axes[0], svm_scratch, "SVM Scratch", acc_scratch),
        (axes[1], svm_sklearn, "SVM Sklearn", acc_sklearn),
    ]:
        ax.scatter(X_scaled[:, 0], X_scaled[:, 1], c=y, cmap=plt.cm.RdYlBu, edgecolors="k", s=30)

        # Decision boundary: w[0]*x + w[1]*y + b = 0
        x0 = np.linspace(X_scaled[:, 0].min() - 1, X_scaled[:, 0].max() + 1, 100)
        if hasattr(model, "w"):
            w, b = model.w, model.b
        else:
            w, b = model.coef_[0], model.intercept_[0]

        # Decision boundary: x1 = -(w0*x0 + b) / w1
        x1_boundary = -(w[0] * x0 + b) / w[1]
        # Margins: w0*x0 + w1*x1 + b = +/- 1
        x1_margin_pos = -(w[0] * x0 + b - 1) / w[1]
        x1_margin_neg = -(w[0] * x0 + b + 1) / w[1]

        ax.plot(x0, x1_boundary, "k-", label="Decision boundary")
        ax.plot(x0, x1_margin_pos, "k--", alpha=0.5, label="Margin (+1)")
        ax.plot(x0, x1_margin_neg, "k--", alpha=0.5, label="Margin (-1)")
        ax.set_title(f"{title} (acc={acc:.3f})")
        ax.legend(fontsize=8)
        ax.set_xlim(X_scaled[:, 0].min() - 1, X_scaled[:, 0].max() + 1)
        ax.set_ylim(X_scaled[:, 1].min() - 1, X_scaled[:, 1].max() + 1)

    plt.tight_layout()
    plt.savefig("svm_from_scratch.png", dpi=150)
    print("\nPlot saved to svm_from_scratch.png")
