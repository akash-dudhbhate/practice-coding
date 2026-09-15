"""
Gini Impurity from Scratch
==========================
Implement Gini impurity and verify the calculation:
  Gini([3 pos, 2 neg]) = 1 - (3/5)^2 - (2/5)^2 = 0.48
"""

import numpy as np


def gini_impurity(labels):
    """Calculate Gini impurity for a list of class labels.

    Gini = 1 - sum(p_i^2) for each class i
    where p_i is the proportion of class i.
    """
    labels = np.array(labels)
    n = len(labels)
    if n == 0:
        return 0.0

    # Count each class
    classes, counts = np.unique(labels, return_counts=True)
    proportions = counts / n

    gini = 1.0 - np.sum(proportions ** 2)
    return gini


if __name__ == "__main__":
    # Test: [3 positive, 2 negative] -> expected 0.48
    labels = [1, 1, 1, 0, 0]  # 3 positive, 2 negative
    gini = gini_impurity(labels)
    expected = 1 - (3 / 5) ** 2 - (2 / 5) ** 2

    print("=== Gini Impurity from Scratch ===\n")
    print(f"Labels: {labels} (3 positive, 2 negative)")
    print(f"Calculated Gini: {gini:.4f}")
    print(f"Expected Gini:   {expected:.4f}")
    print(f"Match: {np.isclose(gini, expected)}")
    print(f"Expected value:  0.48")
    print(f"Verified: {np.isclose(gini, 0.48)}")

    # Additional test cases
    print("\n=== Additional Test Cases ===")
    test_cases = [
        ([0, 0, 0, 0], "Pure (all same)"),
        ([0, 1, 0, 1], "Balanced 50/50"),
        ([0, 0, 0, 0, 0, 1], "Imbalanced 5:1"),
        ([0, 1, 2, 0, 1, 2], "3 classes balanced"),
    ]

    for labels, desc in test_cases:
        g = gini_impurity(labels)
        print(f"  {desc:25s}: Gini = {g:.4f}")

    print("\n=== Interpretation ===")
    print("Gini = 0: perfectly pure (all same class).")
    print("Gini = 0.5: maximum impurity for binary (50/50 split).")
    print("Lower Gini = better split for decision trees.")
