"""
Threshold Optimization for Logistic Regression
==============================================
Get prediction probabilities, sweep thresholds from 0.1 to 0.9,
calculate precision/recall/F1 at each threshold.
Plot the PR curve and find the optimal threshold for F1.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score


if __name__ == "__main__":
    X, y = make_classification(
        n_samples=1000, n_features=10, n_informative=5,
        n_redundant=2, weights=[0.7], random_state=42
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train, y_train)

    # Get probabilities for the positive class
    y_proba = model.predict_proba(X_test)[:, 1]

    # Sweep thresholds
    thresholds = np.arange(0.1, 0.91, 0.05)
    precisions = []
    recalls = []
    f1s = []

    print(f"{'Threshold':<12} {'Precision':<12} {'Recall':<12} {'F1':<12}")
    print("-" * 48)

    for t in thresholds:
        y_pred_t = (y_proba >= t).astype(int)
        p = precision_score(y_test, y_pred_t, zero_division=0)
        r = recall_score(y_test, y_pred_t, zero_division=0)
        f1 = f1_score(y_test, y_pred_t, zero_division=0)

        precisions.append(p)
        recalls.append(r)
        f1s.append(f1)

        print(f"{t:<12.2f} {p:<12.4f} {r:<12.4f} {f1:<12.4f}")

    # Find optimal threshold for F1
    best_idx = np.argmax(f1s)
    best_threshold = thresholds[best_idx]
    best_f1 = f1s[best_idx]

    print(f"\nOptimal threshold (max F1): {best_threshold:.2f}")
    print(f"Best F1: {best_f1:.4f}")
    print(f"Precision at optimal: {precisions[best_idx]:.4f}")
    print(f"Recall at optimal:    {recalls[best_idx]:.4f}")

    # Plot PR curve
    plt.figure(figsize=(8, 6))
    plt.plot(recalls, precisions, "b-o", markersize=4, label="PR Curve")
    plt.scatter([recalls[best_idx]], [precisions[best_idx]],
                color="red", s=100, zorder=5, label=f"Optimal (t={best_threshold:.2f})")
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.title("Precision-Recall Curve (Threshold Sweep)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("pr_curve_threshold.png", dpi=150)
    plt.show()
    print("PR curve saved to pr_curve_threshold.png")
