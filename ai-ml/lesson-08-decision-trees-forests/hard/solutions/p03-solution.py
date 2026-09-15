"""
Feature Importance Analysis
===========================
Train a random forest, get feature importances, select top 5 features,
retrain with only those features, and compare accuracy before/after.
"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score


if __name__ == "__main__":
    X, y = make_classification(
        n_samples=1000, n_features=20, n_informative=8,
        n_redundant=4, random_state=42
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # --- Train with all features ---
    rf_full = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_full.fit(X_train, y_train)
    y_pred_full = rf_full.predict(X_test)

    acc_full = accuracy_score(y_test, y_pred_full)
    f1_full = f1_score(y_test, y_pred_full)

    # --- Get feature importances and select top 5 ---
    importances = rf_full.feature_importances_
    top5_indices = np.argsort(importances)[::-1][:5]

    print("=== Feature Importance Analysis ===\n")
    print("All feature importances (sorted):")
    sorted_idx = np.argsort(importances)[::-1]
    for rank, idx in enumerate(sorted_idx, 1):
        marker = " <-- top 5" if idx in top5_indices else ""
        print(f"  Feature {idx:2d}: {importances[idx]:.4f}{marker}")

    # --- Retrain with only top 5 features ---
    X_train_top5 = X_train[:, top5_indices]
    X_test_top5 = X_test[:, top5_indices]

    rf_top5 = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_top5.fit(X_train_top5, y_train)
    y_pred_top5 = rf_top5.predict(X_test_top5)

    acc_top5 = accuracy_score(y_test, y_pred_top5)
    f1_top5 = f1_score(y_test, y_pred_top5)

    print(f"\n=== Accuracy Comparison ===\n")
    print(f"{'Model':<25} {'Accuracy':<12} {'F1':<12} {'# Features':<10}")
    print("-" * 59)
    print(f"{'All features':<25} {acc_full:<12.4f} {f1_full:<12.4f} {20:<10}")
    print(f"{'Top 5 features':<25} {acc_top5:<12.4f} {f1_top5:<12.4f} {5:<10}")

    print("\n=== Interpretation ===")
    acc_diff = acc_full - acc_top5
    print(f"Accuracy difference: {acc_diff:+.4f}")
    if abs(acc_diff) < 0.02:
        print("Top 5 features retain nearly all predictive power.")
        print("Feature selection successfully reduced dimensionality with minimal loss.")
    elif acc_diff > 0:
        print("Some accuracy lost by dropping features, but model is simpler.")
    else:
        print("Top 5 features actually improved accuracy (noise removed).")
