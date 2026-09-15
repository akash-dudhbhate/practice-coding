"""
KNN from Scratch
=================
Implement KNN from scratch: Euclidean distance, find K nearest neighbors,
majority vote. Train on 2D data, plot the decision boundary, and compare
with sklearn's KNeighborsClassifier.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from collections import Counter

np.random.seed(42)


class KNNScratch:
    """K-Nearest Neighbors classifier implemented from scratch."""

    def __init__(self, k=5):
        self.k = k

    def fit(self, X, y):
        self.X_train = np.array(X)
        self.y_train = np.array(y)

    def _euclidean(self, x1, x2):
        return np.sqrt(np.sum((x1 - x2) ** 2))

    def predict(self, X):
        return np.array([self._predict_one(x) for x in np.array(X)])

    def _predict_one(self, x):
        # Compute distances to all training points
        distances = [self._euclidean(x, x_train) for x_train in self.X_train]
        # Get indices of k nearest
        k_indices = np.argsort(distances)[: self.k]
        # Majority vote
        k_labels = self.y_train[k_indices]
        most_common = Counter(k_labels).most_common(1)
        return most_common[0][0]


def plot_boundary(ax, model, X, y, title):
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
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)

    K = 5

    # --- From scratch ---
    knn_scratch = KNNScratch(k=K)
    knn_scratch.fit(X_train_s, y_train)
    y_pred_scratch = knn_scratch.predict(X_test_s)
    acc_scratch = accuracy_score(y_test, y_pred_scratch)

    # --- Sklearn ---
    knn_sklearn = KNeighborsClassifier(n_neighbors=K)
    knn_sklearn.fit(X_train_s, y_train)
    y_pred_sklearn = knn_sklearn.predict(X_test_s)
    acc_sklearn = accuracy_score(y_test, y_pred_sklearn)

    print("=== KNN Comparison (K=5) ===")
    print(f"From scratch: {acc_scratch:.4f}")
    print(f"Sklearn:      {acc_sklearn:.4f}")
    print(f"Predictions match: {np.array_equal(y_pred_scratch, y_pred_sklearn)}")

    # Plot decision boundaries
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    plot_boundary(axes[0], knn_scratch, X_train_s, y_train, f"KNN Scratch (acc={acc_scratch:.3f})")
    plot_boundary(axes[1], knn_sklearn, X_train_s, y_train, f"KNN Sklearn (acc={acc_sklearn:.3f})")
    plt.tight_layout()
    plt.savefig("knn_from_scratch.png", dpi=150)
    print("\nPlot saved to knn_from_scratch.png")
