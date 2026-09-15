"""
Lesson 02 - Medium P01
Full preprocessing pipeline: impute + scale + LogisticRegression in a single
sklearn Pipeline.

Solution:
  1. Create a synthetic dataset with missing values.
  2. Build a Pipeline: SimpleImputer -> StandardScaler -> LogisticRegression.
  3. Split into train/test.
  4. Fit, predict, and evaluate accuracy.
"""

import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# ---------------------------------------------------------------------------
# 1. Create a synthetic dataset with missing values
# ---------------------------------------------------------------------------
np.random.seed(42)
n_samples = 200
X = pd.DataFrame({
    "feature_1": np.random.randn(n_samples) * 10 + 50,
    "feature_2": np.random.randn(n_samples) * 5 + 100,
    "feature_3": np.random.randn(n_samples) * 20 + 200,
})
# Introduce ~10% missing values randomly
mask = np.random.rand(*X.shape) < 0.10
X = X.mask(mask)
y = (X["feature_1"].fillna(X["feature_1"].median()) > 50).astype(int)

print(f"Dataset shape: {X.shape}")
print(f"Missing values per column:\n{X.isnull().sum()}\n")

# ---------------------------------------------------------------------------
# 2. Build the preprocessing + model pipeline
# ---------------------------------------------------------------------------
# Solution: A Pipeline chains preprocessing and modeling so that:
#   - The imputer is fit ONLY on the training fold (no data leakage).
#   - The scaler is fit ONLY on the training fold.
#   - The same transformations are applied to test data using fitted params.
pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(random_state=42)),
])

# ---------------------------------------------------------------------------
# 3. Split into train and test sets
# ---------------------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"Train size: {X_train.shape[0]}, Test size: {X_test.shape[0]}\n")

# ---------------------------------------------------------------------------
# 4. Fit, predict, and evaluate
# ---------------------------------------------------------------------------
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Test Accuracy: {accuracy:.4f}\n")
print("Classification Report:")
print(classification_report(y_test, y_pred))

# ---------------------------------------------------------------------------
# 5. Inspect the fitted pipeline steps
# ---------------------------------------------------------------------------
print("Pipeline steps:")
for name, step in pipeline.named_steps.items():
    print(f"  {name}: {step.__class__.__name__}")
