"""
Lesson 02 - Hard P03
Stratified split with imbalanced data (95:5 ratio). Compare the class
distribution with and without stratification.

Solution:
  1. Create a highly imbalanced dataset (95% class 0, 5% class 1).
  2. Split WITHOUT stratify -> show class imbalance can be lost.
  3. Split WITH stratify -> show class ratio is preserved.
  4. Train a LogisticRegression on both and compare recall for the minority class.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# ---------------------------------------------------------------------------
# 1. Create a highly imbalanced dataset (95:5)
# ---------------------------------------------------------------------------
np.random.seed(42)
n_majority = 950
n_minority = 50

X_majority = np.random.randn(n_majority, 4) + 0
y_majority = np.zeros(n_majority, dtype=int)

X_minority = np.random.randn(n_minority, 4) + 2  # shifted distribution
y_minority = np.ones(n_minority, dtype=int)

X = np.vstack([X_majority, X_minority])
y = np.concatenate([y_majority, y_minority])

print(f"Full dataset: {len(y)} samples")
print(f"  Class 0: {np.sum(y == 0)} ({np.mean(y == 0):.1%})")
print(f"  Class 1: {np.sum(y == 1)} ({np.mean(y == 1):.1%})")
print()

# ---------------------------------------------------------------------------
# 2. Split WITHOUT stratification
# ---------------------------------------------------------------------------
# Solution: Without stratify, the random split may assign very few (or zero)
# minority-class samples to the test set, making evaluation unreliable.
X_train_ns, X_test_ns, y_train_ns, y_test_ns = train_test_split(
    X, y, test_size=0.2, random_state=42  # NO stratify
)

print("=" * 60)
print("WITHOUT stratification")
print("=" * 60)
print(f"  Train class distribution: 0 -> {np.sum(y_train_ns == 0)}, 1 -> {np.sum(y_train_ns == 1)}")
print(f"  Test  class distribution: 0 -> {np.sum(y_test_ns == 0)}, 1 -> {np.sum(y_test_ns == 1)}")
print(f"  Test minority ratio: {np.mean(y_test_ns == 1):.2%}")
print()

# ---------------------------------------------------------------------------
# 3. Split WITH stratification
# ---------------------------------------------------------------------------
# Solution: stratify=y ensures the train and test sets have the SAME class
# ratio as the original dataset. This is critical for imbalanced data.
X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("=" * 60)
print("WITH stratification")
print("=" * 60)
print(f"  Train class distribution: 0 -> {np.sum(y_train_s == 0)}, 1 -> {np.sum(y_train_s == 1)}")
print(f"  Test  class distribution: 0 -> {np.sum(y_test_s == 0)}, 1 -> {np.sum(y_test_s == 1)}")
print(f"  Test minority ratio: {np.mean(y_test_s == 1):.2%}")
print()

# ---------------------------------------------------------------------------
# 4. Train models and compare recall on the minority class
# ---------------------------------------------------------------------------
print("=" * 60)
print("Model comparison (LogisticRegression)")
print("=" * 60)

# Without stratify
model_ns = LogisticRegression(random_state=42)
model_ns.fit(X_train_ns, y_train_ns)
print("\nWITHOUT stratify:")
print(classification_report(y_test_ns, model_ns.predict(X_test_ns), zero_division=0))

# With stratify
model_s = LogisticRegression(random_state=42)
model_s.fit(X_train_s, y_train_s)
print("WITH stratify:")
print(classification_report(y_test_s, model_s.predict(X_test_s), zero_division=0))

print("Key takeaway: Always use stratify=y for imbalanced classification")
print("to ensure the minority class is represented in both train and test sets.")
