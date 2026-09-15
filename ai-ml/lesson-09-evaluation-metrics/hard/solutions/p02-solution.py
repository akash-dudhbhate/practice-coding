"""
Custom Threshold Optimizer
==========================
Get prediction probabilities, sweep thresholds from 0.1 to 0.9,
calculate F1 at each threshold, plot F1 vs threshold, find optimal.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, precision_score, recall_score


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
    y_proba = model.predict_proba(X_test)[:, 1]

    # Sweep thresholds
    thresholds = np.arange(0.1, 0.91, 0.05)
    f1_scores = []
    precisions = []
    recalls = []

    print(f"{'Threshold':<12} {'Precision':<12} {'Recall':<12} {'F1':<12}")
    print("-" * 48)

    for t in thresholds:
        y_pred_t = (y_proba >= t).astype(int)
        p = precision_score(y_test, y_pred_t, zero_division=0)
        r = recall_score(y_test, y_pred_t, zero_division=0)
        f1 = f1_score(y_test, y_pred_t, zero_division=0)

        precisions.append(p)
        recalls.append(r)
        f1_scores.append(f1)

        print(f"{t:<12.2f} {p:<12.4f} {r:<12.4f} {f1:<12.4f}")

    # Find optimal threshold
    best_idx = np.argmax(f1_scores)
    best_threshold = thresholds[best_idx]
    best_f1 = f1_scores[best_idx]

    print(f"\nOptimal threshold: {best_threshold:.2f}")
    print(f"Best F1: {best_f1:.4f}")
    print(f"Precision at optimal: {precisions[best_idx]:.4f}")
    print(f"Recall at optimal:    {recalls[best_idx]:.4f}")

    # Plot F1 vs threshold
    plt.figure(figsize=(9, 5))
    plt.plot(thresholds, f1_scores, "o-", color="blue", label="F1 Score")
    plt.plot(thresholds, precisions, "s--", color="green", label="Precision", alpha=0.7)
    plt.plot(thresholds, recalls, "^--", color="red", label="Recall", alpha=0.7)
    plt.axvline(x=best_threshold, color="black", linestyle=":", label=f"Optimal t={best_threshold:.2f}")
    plt.xlabel("Threshold")
    plt.ylabel("Score")
    plt.title("F1 Score vs Decision Threshold")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("f1_vs_threshold.png", dpi=150)
    plt.show()
    print("Plot saved to f1_vs_threshold.png")

    print("\n=== Interpretation ===")
    print("Lower threshold: more predictions as positive (higher recall, lower precision).")
    print("Higher threshold: fewer predictions as positive (higher precision, lower recall).")
    print(f"Optimal F1 at threshold {best_threshold:.2f} balances precision and recall.")
