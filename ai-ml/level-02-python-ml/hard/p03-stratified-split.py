"""
LEVEL 02 — Python for ML
HARD P03 — Stratified Splitting
========================================

CONCEPT:
  With imbalanced data (e.g., 95% class 0, 5% class 1), a random
  split can put almost NO minority samples in train or test.

  stratify=y keeps the SAME class ratio in both splits:
    Without: train [757, 43], test [193, 7]
    With:    train [760, 40], test [190, 10]  ← 5% ratio preserved

  train_test_split(..., stratify=y)

PROBLEM:
  Write `compare_splits()` that:
    1. make_classification(1000 samples, 10 features, n_informative=5,
       weights=[0.95, 0.05], flip_y=0.0, random_state=42)
    2. Split WITHOUT stratify → print class counts (np.bincount)
    3. Split WITH stratify=y → print class counts
    4. Train RandomForestClassifier(seed=42) on each, print both
       test accuracies
    5. Return (acc_without, acc_with)

TRY THIS INPUT:
  ```python
  a, b = compare_splits()
  ```

EXPECTED OUTPUT:
  ```
  Without stratify:
    Train: [757  43]
    Test:  [193   7]
  With stratify:
    Train: [760  40]
    Test:  [190  10]
  Without stratify test accuracy: 0.9750
  With stratify test accuracy: 0.9700
  ```

HINT:
  train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# a, b = compare_splits()
