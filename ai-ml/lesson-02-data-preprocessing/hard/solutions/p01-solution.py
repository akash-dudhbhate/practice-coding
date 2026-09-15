"""
Lesson 02 - Hard P01
Prevent data leakage: split the data FIRST, then fit preprocessing on the
training set only.

Solution:
  1. Create a dataset with missing values and different scales.
  2. Split into train/test BEFORE any preprocessing.
  3. Fit imputer and scaler on TRAIN data only.
  4. Transform both train and test using the fitted parameters.
  5. Train a model and evaluate.
  6. Compare with the WRONG approach (fit on all data) to show leakage.
"""

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ---------------------------------------------------------------------------
# 1. Create a synthetic dataset
# ---------------------------------------------------------------------------
np.random.seed(42)
n = 300
X = pd.DataFrame({
    "f1": np.random.randn(n) * 10 + 50,
    "f2": np.random.randn(n) * 5 + 100,
    "f3": np.random.randn(n) * 20 + 200,
})
# Inject missing values
mask = np.random.rand(*X.shape) < 0.08
X = X.mask(mask)
y = (X["f1"].fillna(X["f1"].median()) > 50).astype(int)

# ---------------------------------------------------------------------------
# 2. CORRECT approach: split first, then fit preprocessing on train only
# ---------------------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Fit imputer and scaler on TRAIN data only
imputer = SimpleImputer(strategy="median")
scaler = StandardScaler()

X_train_imputed = imputer.fit_transform(X_train)  # fit on train
X_train_scaled = scaler.fit_transform(X_train_imputed)  # fit on train

# Transform test data using the SAME fitted parameters
X_test_imputed = imputer.transform(X_test)  # transform only!
X_test_scaled = scaler.transform(X_test_imputed)  # transform only!

model_correct = LogisticRegression(random_state=42)
model_correct.fit(X_train_scaled, y_train)
acc_correct = accuracy_score(y_test, model_correct.predict(X_test_scaled))

print("=" * 60)
print("CORRECT approach (split first, fit on train only)")
print("=" * 60)
print(f"  Test accuracy: {acc_correct:.4f}")
print()

# ---------------------------------------------------------------------------
# 3. WRONG approach: fit preprocessing on ALL data before splitting (LEAKAGE)
# ---------------------------------------------------------------------------
# Solution: This is data leakage because the scaler's mean/std and the imputer's
# median are computed using test data, giving the model information it should
# not have. This inflates test accuracy unrealistically.
imputer_wrong = SimpleImputer(strategy="median")
scaler_wrong = StandardScaler()

X_all_imputed = imputer_wrong.fit_transform(X)  # fit on ALL data (LEAKAGE)
X_all_scaled = scaler_wrong.fit_transform(X_all_imputed)  # fit on ALL data (LEAKAGE)

X_train_w, X_test_w, y_train_w, y_test_w = train_test_split(
    X_all_scaled, y, test_size=0.2, random_state=42, stratify=y
)

model_wrong = LogisticRegression(random_state=42)
model_wrong.fit(X_train_w, y_train_w)
acc_wrong = accuracy_score(y_test_w, model_wrong.predict(X_test_w))

print("=" * 60)
print("WRONG approach (fit on all data -> leakage)")
print("=" * 60)
print(f"  Test accuracy: {acc_wrong:.4f}")
print()

# ---------------------------------------------------------------------------
# 4. Summary
# ---------------------------------------------------------------------------
print("=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"  Correct (no leakage): {acc_correct:.4f}")
print(f"  Wrong   (leakage):    {acc_wrong:.4f}")
print()
print("  Key rule: ALWAYS split first, then fit preprocessors on the")
print("  training set only. Use .transform() on the test set.")
print("  Better yet, use sklearn Pipeline which handles this automatically.")
