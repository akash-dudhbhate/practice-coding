"""
Compare SVM Kernels on make_moons
=================================
Compare linear, RBF, and polynomial kernels on the make_moons dataset.
Print accuracy for each and plot their decision boundaries.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

np.random.seed(42)


def plot_decision_boundary(ax, model, X, y, title):
    """Plot the decision boundary of a classifier."""
    h = 0.02
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    ax.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.RdYlBu)
    ax.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.RdYlBu, edgecolors="k", s=30)
    ax.set_title(title)


if __name__ == "__main__":
    X, y = make_moons(n_samples=300, noise=0.15, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    kernels = {
        "linear": SVC(kernel="linear", random_state=42),
        "RBF": SVC(kernel="rbf", random_state=42),
        "poly": SVC(kernel="poly", degree=3, random_state=42),
    }

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    print("=== SVM Kernel Comparison on make_moons ===\n")

    for ax, (name, model) in zip(axes, kernels.items()):
        model.fit(X_train_scaled, y_train)
        acc = accuracy_score(y_test, model.predict(X_test_scaled))
        print(f"{name:8s} kernel: accuracy = {acc:.4f}, support vectors = {sum(model.n_support_)}")
        plot_decision_boundary(ax, model, X_train_scaled, y_train, f"{name} (acc={acc:.3f})")

    plt.tight_layout()
    plt.savefig("svm_kernel_comparison.png", dpi=150)
    print("\nPlot saved to svm_kernel_comparison.png")
    print("\nKey takeaway: The moons dataset is non-linear. The linear kernel")
    print("struggles, while RBF and poly can capture the curved boundary.")
