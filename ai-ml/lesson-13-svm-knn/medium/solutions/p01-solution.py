"""
Tune K for KNN with Cross-Validation
=====================================
Test K=1 to 50 (odd values only) with 5-fold cross-validation on scaled data.
Plot accuracy vs K and identify the optimal K.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

np.random.seed(42)


if __name__ == "__main__":
    X, y = load_iris(return_X_y=True)

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Test odd K values from 1 to 49
    k_values = list(range(1, 50, 2))
    cv_scores = []
    cv_stds = []

    for k in k_values:
        knn = KNeighborsClassifier(n_neighbors=k)
        scores = cross_val_score(knn, X_scaled, y, cv=5, scoring="accuracy")
        cv_scores.append(scores.mean())
        cv_stds.append(scores.std())

    cv_scores = np.array(cv_scores)
    cv_stds = np.array(cv_stds)

    # Find optimal K
    best_idx = np.argmax(cv_scores)
    best_k = k_values[best_idx]
    best_score = cv_scores[best_idx]

    print("=== KNN K Tuning (5-fold CV) ===")
    print(f"Tested K values: {k_values}")
    print(f"Best K: {best_k}")
    print(f"Best CV accuracy: {best_score:.4f} (+/- {cv_stds[best_idx]:.4f})")
    print()

    # Plot
    plt.figure(figsize=(10, 5))
    plt.plot(k_values, cv_scores, "bo-", label="CV Accuracy")
    plt.fill_between(k_values, cv_scores - cv_stds, cv_scores + cv_stds, alpha=0.2)
    plt.axvline(x=best_k, color="r", linestyle="--", label=f"Best K={best_k}")
    plt.xlabel("K (number of neighbors)")
    plt.ylabel("CV Accuracy")
    plt.title("KNN: Accuracy vs K (5-fold cross-validation)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("knn_k_tuning.png", dpi=150)
    print("Plot saved to knn_k_tuning.png")
