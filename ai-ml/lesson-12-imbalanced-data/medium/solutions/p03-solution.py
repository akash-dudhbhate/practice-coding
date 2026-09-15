"""
Decision Threshold Adjustment
=============================
Adjust the classification decision threshold to trade precision for recall.
Test thresholds [0.3, 0.5, 0.7], print precision/recall/F1 for each, and
find the best F1 threshold.
"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, f1_score

np.random.seed(42)


if __name__ == "__main__":
    # Imbalanced dataset: 90:10
    X, y = make_classification(
        n_samples=2000,
        n_features=10,
        n_informative=5,
        weights=[0.90, 0.10],
        flip_y=0.0,
        random_state=42,
    )

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    model = LogisticRegression(random_state=42, max_iter=1000)
    model.fit(X_train, y_train)

    # Get predicted probabilities for the positive class
    y_proba = model.predict_proba(X_test)[:, 1]

    # Test different thresholds
    thresholds = [0.3, 0.5, 0.7]
    results = []

    print(f"{'Threshold':>10} {'Precision':>10} {'Recall':>10} {'F1':>10}")
    print("-" * 44)

    for thresh in thresholds:
        y_pred = (y_proba >= thresh).astype(int)
        precision = precision_score(y_test, y_pred, zero_division=0)
        recall = recall_score(y_test, y_pred, zero_division=0)
        f1 = f1_score(y_test, y_pred, zero_division=0)
        results.append((thresh, precision, recall, f1))
        print(f"{thresh:>10.2f} {precision:>10.4f} {recall:>10.4f} {f1:>10.4f}")

    # --- Find best F1 threshold (fine-grained search) ---
    best_f1 = 0
    best_thresh = 0.5
    for thresh in np.arange(0.05, 0.95, 0.05):
        y_pred = (y_proba >= thresh).astype(int)
        f1 = f1_score(y_test, y_pred, zero_division=0)
        if f1 > best_f1:
            best_f1 = f1
            best_thresh = thresh

    print(f"\nBest F1 threshold: {best_thresh:.2f} (F1={best_f1:.4f})")
    print()
    print("Key takeaway: Lowering the threshold increases recall (catch more")
    print("positives) but may decrease precision (more false positives).")
    print("The best threshold depends on the business cost of each error type.")
