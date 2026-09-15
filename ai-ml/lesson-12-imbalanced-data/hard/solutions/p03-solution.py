"""
Evaluation Metrics Comparison on Imbalanced Data
=================================================
Show how accuracy and ROC-AUC can look deceptively good on imbalanced data
while F1 and PR-AUC reveal the true model quality. Plot both ROC and PR curves.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, f1_score, roc_auc_score, average_precision_score,
    roc_curve, precision_recall_curve, classification_report,
)

np.random.seed(42)


if __name__ == "__main__":
    # Highly imbalanced: 95:5
    X, y = make_classification(
        n_samples=2000,
        n_features=10,
        n_informative=5,
        weights=[0.95, 0.05],
        flip_y=0.0,
        random_state=42,
    )

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

    model = LogisticRegression(random_state=42, max_iter=1000)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]

    # --- Compute all metrics ---
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, zero_division=0)
    roc_auc = roc_auc_score(y_test, y_proba)
    pr_auc = average_precision_score(y_test, y_proba)

    print("=== Metrics on Imbalanced Data ===")
    print(f"Accuracy:  {acc:.4f}  <-- looks good (deceptive!)")
    print(f"ROC-AUC:   {roc_auc:.4f}  <-- looks good (deceptive!)")
    print(f"F1:        {f1:.4f}  <-- reveals poor minority detection")
    print(f"PR-AUC:    {pr_auc:.4f}  <-- reveals poor minority detection")
    print()
    print("=== Classification Report ===")
    print(classification_report(y_test, y_pred))
    print()
    print("Key takeaway: Accuracy and ROC-AUC are inflated by the majority")
    print("class. F1 and PR-AUC are more informative for imbalanced data.")
    print("Always look at per-class metrics, not just overall numbers.")

    # --- Plot ROC and PR curves side by side ---
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # ROC curve
    fpr, tpr, _ = roc_curve(y_test, y_proba)
    axes[0].plot(fpr, tpr, label=f"ROC (AUC={roc_auc:.3f})")
    axes[0].plot([0, 1], [0, 1], "k--", label="Random")
    axes[0].set_xlabel("False Positive Rate")
    axes[0].set_ylabel("True Positive Rate")
    axes[0].set_title("ROC Curve")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    # PR curve
    precision, recall, _ = precision_recall_curve(y_test, y_proba)
    axes[1].plot(recall, precision, label=f"PR (AP={pr_auc:.3f})")
    axes[1].axhline(y=y_test.mean(), color="k", linestyle="--", label=f"Baseline ({y_test.mean():.2f})")
    axes[1].set_xlabel("Recall")
    axes[1].set_ylabel("Precision")
    axes[1].set_title("Precision-Recall Curve")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("roc_pr_comparison.png", dpi=150)
    print("\nCurves saved to roc_pr_comparison.png")
