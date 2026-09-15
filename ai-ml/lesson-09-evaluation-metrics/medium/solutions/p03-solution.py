"""
Precision-Recall Curve and Average Precision
============================================
Plot the precision-recall curve, calculate average precision (AP),
and compare with ROC for imbalanced data.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import (precision_recall_curve, average_precision_score,
                             roc_curve, auc)


if __name__ == "__main__":
    # Imbalanced dataset: 90% class 0, 10% class 1
    X, y = make_classification(
        n_samples=2000, n_features=10, n_informative=5,
        n_redundant=2, weights=[0.9], random_state=42
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train, y_train)
    y_proba = model.predict_proba(X_test)[:, 1]

    # Precision-Recall curve
    precision, recall, pr_thresholds = precision_recall_curve(y_test, y_proba)
    ap = average_precision_score(y_test, y_proba)

    # ROC curve
    fpr, tpr, roc_thresholds = roc_curve(y_test, y_proba)
    roc_auc = auc(fpr, tpr)

    print(f"Average Precision (AP): {ap:.4f}")
    print(f"ROC AUC:                {roc_auc:.4f}")

    # Plot both curves side by side
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # PR curve
    axes[0].plot(recall, precision, color="blue", lw=2, label=f"PR curve (AP = {ap:.4f})")
    axes[0].set_xlabel("Recall")
    axes[0].set_ylabel("Precision")
    axes[0].set_title("Precision-Recall Curve")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    axes[0].set_xlim([0.0, 1.0])
    axes[0].set_ylim([0.0, 1.05])

    # ROC curve
    axes[1].plot(fpr, tpr, color="darkorange", lw=2, label=f"ROC curve (AUC = {roc_auc:.4f})")
    axes[1].plot([0, 1], [0, 1], "k--", lw=1, label="Random (AUC = 0.5)")
    axes[1].set_xlabel("False Positive Rate")
    axes[1].set_ylabel("True Positive Rate")
    axes[1].set_title("ROC Curve")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    plt.suptitle("PR vs ROC Curve on Imbalanced Data (90:10)", fontsize=13)
    plt.tight_layout()
    plt.savefig("pr_vs_roc.png", dpi=150, bbox_inches="tight")
    plt.show()
    print("Plots saved to pr_vs_roc.png")

    print("\n=== Comparison: PR vs ROC on Imbalanced Data ===")
    print("ROC can look overly optimistic on imbalanced data because FPR is")
    print("dominated by the large number of true negatives.")
    print("PR curves are more informative for imbalanced data because they")
    print("focus on the minority (positive) class performance.")
    print(f"AP = {ap:.4f} directly summarizes PR curve quality.")
    print(f"ROC AUC = {roc_auc:.4f} may appear higher due to TN dominance.")
