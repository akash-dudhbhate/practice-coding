"""
Cross-Validation Evaluation with Multiple Metrics
=================================================
Perform 5-fold CV with 3 scoring metrics (accuracy, f1, roc_auc).
Print mean +/- std for each. Explain why different metrics may rank models differently.
"""

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score


if __name__ == "__main__":
    X, y = make_classification(
        n_samples=1000, n_features=15, n_informative=8,
        n_redundant=3, weights=[0.7], random_state=42
    )

    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
        "Decision Tree": DecisionTreeClassifier(max_depth=5, random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    }

    metrics = ["accuracy", "f1", "roc_auc"]

    print("=== 5-Fold Cross-Validation Results ===\n")
    print(f"{'Model':<22} {'Metric':<12} {'Mean':<10} {'Std':<10}")
    print("-" * 54)

    results = {}
    for name, model in models.items():
        results[name] = {}
        for metric in metrics:
            scores = cross_val_score(model, X, y, cv=5, scoring=metric)
            mean = scores.mean()
            std = scores.std()
            results[name][metric] = (mean, std)
            print(f"{name:<22} {metric:<12} {mean:<10.4f} {std:<10.4f}")
        print()

    # Summary table
    print("=== Summary (Mean +/- Std) ===\n")
    print(f"{'Model':<22} {'Accuracy':<18} {'F1':<18} {'AUC':<18}")
    print("-" * 76)
    for name in models:
        acc_m, acc_s = results[name]["accuracy"]
        f1_m, f1_s = results[name]["f1"]
        auc_m, auc_s = results[name]["roc_auc"]
        print(f"{name:<22} {acc_m:.4f}+/-{acc_s:.4f}   {f1_m:.4f}+/-{f1_s:.4f}   {auc_m:.4f}+/-{auc_s:.4f}")

    # Best model per metric
    print("\n=== Best Model per Metric ===")
    for metric in metrics:
        best = max(results, key=lambda k: results[k][metric][0])
        print(f"  {metric:12s}: {best} (mean={results[best][metric][0]:.4f})")

    print("\n=== Why Different Rankings? ===")
    print("Accuracy: measures overall correctness, can be misleading if imbalanced.")
    print("F1: balances precision and recall, focuses on positive class performance.")
    print("AUC: measures ranking ability across all thresholds, threshold-independent.")
    print("A model can have high accuracy but low F1 if it misses minority class examples.")
    print("AUC may favor models with good probability calibration even if F1 is lower.")
