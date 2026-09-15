"""
StratifiedKFold on Imbalanced Data
==================================
Use StratifiedKFold with 5 folds on imbalanced data (90% class 0).
Verify class ratio is maintained in each fold.
Print fold sizes and class counts.
"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import StratifiedKFold


if __name__ == "__main__":
    # Create imbalanced dataset: 90% class 0, 10% class 1
    X, y = make_classification(
        n_samples=1000, n_features=5, n_informative=3,
        weights=[0.9], random_state=42
    )

    print(f"Overall class distribution: {dict(zip(*np.unique(y, return_counts=True)))}")
    print(f"Class 0 ratio: {np.mean(y == 0)*100:.1f}%")
    print(f"Class 1 ratio: {np.mean(y == 1)*100:.1f}%\n")

    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

    print("=== StratifiedKFold: 5 Folds ===\n")
    print(f"{'Fold':<8} {'Train Size':<14} {'Test Size':<12} {'Train 0/1':<16} {'Test 0/1':<14}")
    print("-" * 64)

    for fold, (train_idx, test_idx) in enumerate(skf.split(X, y), 1):
        y_train_fold = y[train_idx]
        y_test_fold = y[test_idx]

        train_0 = np.sum(y_train_fold == 0)
        train_1 = np.sum(y_train_fold == 1)
        test_0 = np.sum(y_test_fold == 0)
        test_1 = np.sum(y_test_fold == 1)

        train_ratio = train_1 / len(y_train_fold) * 100
        test_ratio = test_1 / len(y_test_fold) * 100

        print(f"{fold:<8} {len(train_idx):<14} {len(test_idx):<12} "
              f"{train_0}/{train_1} ({train_ratio:.1f}%)    "
              f"{test_0}/{test_1} ({test_ratio:.1f}%)")

    print("\n=== Verification ===")
    print("StratifiedKFold maintains the same class ratio in each fold.")
    print("Each fold has ~10% class 1, matching the overall distribution.")
    print("This is critical for imbalanced data to ensure the minority class")
    print("is represented in every fold for training and evaluation.")
