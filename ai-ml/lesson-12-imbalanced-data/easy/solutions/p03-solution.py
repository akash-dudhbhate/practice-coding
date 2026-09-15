"""
Stratified Train-Test Split
============================
Use stratify=y in train_test_split to maintain the same class ratio in
train and test sets. Verify by printing class counts.
"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split


if __name__ == "__main__":
    # Imbalanced dataset: 90:10
    X, y = make_classification(
        n_samples=1000,
        n_features=5,
        n_informative=3,
        weights=[0.90, 0.10],
        flip_y=0.0,
        random_state=42,
    )

    print(f"Full dataset class counts: {dict(zip(*np.unique(y, return_counts=True)))}")
    full_ratio = np.bincount(y) / len(y)
    print(f"Full dataset class ratio:  {full_ratio}\n")

    # --- WITHOUT stratification ---
    X_train_ns, X_test_ns, y_train_ns, y_test_ns = train_test_split(
        X, y, test_size=0.2, random_state=42  # no stratify
    )
    print("=== WITHOUT stratify ===")
    print(f"Train class counts: {dict(zip(*np.unique(y_train_ns, return_counts=True)))}")
    print(f"Test  class counts: {dict(zip(*np.unique(y_test_ns, return_counts=True)))}")
    train_ratio_ns = np.bincount(y_train_ns) / len(y_train_ns)
    test_ratio_ns = np.bincount(y_test_ns) / len(y_test_ns)
    print(f"Train ratio: {train_ratio_ns}")
    print(f"Test  ratio: {test_ratio_ns}\n")

    # --- WITH stratification ---
    X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print("=== WITH stratify=y ===")
    print(f"Train class counts: {dict(zip(*np.unique(y_train_s, return_counts=True)))}")
    print(f"Test  class counts: {dict(zip(*np.unique(y_test_s, return_counts=True)))}")
    train_ratio_s = np.bincount(y_train_s) / len(y_train_s)
    test_ratio_s = np.bincount(y_test_s) / len(y_test_s)
    print(f"Train ratio: {train_ratio_s}")
    print(f"Test  ratio: {test_ratio_s}\n")

    print("Key takeaway: stratify=y ensures the class proportions in the")
    print("original data are preserved in both train and test splits.")
