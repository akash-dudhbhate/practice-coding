"""
Complete Imbalanced Pipeline: 99:1 Dataset
============================================
Compare 4 approaches on an extremely imbalanced (99:1) dataset:
  (a) Baseline (no handling)
  (b) class_weight='balanced'
  (c) SMOTE
  (d) SMOTE + undersampling
Print F1, PR-AUC, and confusion matrix for each. Identify the best approach.
"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, average_precision_score, confusion_matrix
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from imblearn.pipeline import Pipeline

np.random.seed(42)


def evaluate(y_true, y_pred, y_proba, name):
    """Compute and print metrics for an approach."""
    f1 = f1_score(y_true, y_pred, zero_division=0)
    pr_auc = average_precision_score(y_true, y_proba)
    cm = confusion_matrix(y_true, y_pred)
    print(f"\n--- {name} ---")
    print(f"F1:     {f1:.4f}")
    print(f"PR-AUC: {pr_auc:.4f}")
    print(f"Confusion Matrix:\n{cm}")
    return {"name": name, "f1": f1, "pr_auc": pr_auc}


if __name__ == "__main__":
    # Extremely imbalanced: 99:1
    X, y = make_classification(
        n_samples=10000,
        n_features=20,
        n_informative=10,
        weights=[0.99, 0.01],
        flip_y=0.0,
        random_state=42,
    )

    print(f"Class distribution: {dict(zip(*np.unique(y, return_counts=True)))}")

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    print(f"Train: {dict(zip(*np.unique(y_train, return_counts=True)))}")
    print(f"Test:  {dict(zip(*np.unique(y_test, return_counts=True)))}\n")

    results = []

    # (a) Baseline
    m = RandomForestClassifier(random_state=42, n_estimators=100)
    m.fit(X_train, y_train)
    results.append(evaluate(y_test, m.predict(X_test), m.predict_proba(X_test)[:, 1], "Baseline"))

    # (b) class_weight='balanced'
    m = RandomForestClassifier(random_state=42, n_estimators=100, class_weight="balanced")
    m.fit(X_train, y_train)
    results.append(evaluate(y_test, m.predict(X_test), m.predict_proba(X_test)[:, 1], "class_weight=balanced"))

    # (c) SMOTE only
    pipe = Pipeline([
        ("smote", SMOTE(random_state=42, k_neighbors=3)),
        ("clf", RandomForestClassifier(random_state=42, n_estimators=100)),
    ])
    pipe.fit(X_train, y_train)
    results.append(evaluate(y_test, pipe.predict(X_test), pipe.predict_proba(X_test)[:, 1], "SMOTE"))

    # (d) SMOTE + undersampling
    pipe = Pipeline([
        ("smote", SMOTE(random_state=42, k_neighbors=3, sampling_strategy=0.1)),
        ("under", RandomUnderSampler(random_state=42, sampling_strategy=0.5)),
        ("clf", RandomForestClassifier(random_state=42, n_estimators=100)),
    ])
    pipe.fit(X_train, y_train)
    results.append(evaluate(y_test, pipe.predict(X_test), pipe.predict_proba(X_test)[:, 1], "SMOTE+Undersampling"))

    # --- Summary ---
    print("\n=== Summary ===")
    print(f"{'Approach':<25} {'F1':>8} {'PR-AUC':>8}")
    print("-" * 43)
    for r in results:
        print(f"{r['name']:<25} {r['f1']:>8.4f} {r['pr_auc']:>8.4f}")

    best = max(results, key=lambda r: r["f1"])
    print(f"\nBest by F1: {best['name']} (F1={best['f1']:.4f})")
