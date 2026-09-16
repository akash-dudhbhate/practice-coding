"""
LEVEL 02 — Python for ML
MEDIUM P01 — Preprocessing Pipeline
========================================

CONCEPT:
  A Pipeline chains steps so they run in order and are fit ONLY
  on training data (prevents leakage):

    impute missing → scale features → train model

  sklearn Pipeline:
    Pipeline([('name1', Step1()), ('name2', Step2()), ...])
    pipeline.fit(X_train, y_train)
    pipeline.score(X_test, y_test)

PROBLEM:
  Write `build_pipeline()` that:
    1. Generates data: make_classification(n_samples=200, n_features=5,
       random_state=42)
    2. Splits 80/20 (random_state=42)
    3. Builds a Pipeline: SimpleImputer(mean) → StandardScaler →
       LogisticRegression
    4. Fits on train, returns test accuracy

TRY THIS INPUT:
  ```python
  acc = build_pipeline()
  print(f"Accuracy: {acc:.4f}")
  ```

EXPECTED OUTPUT:
  ```
  Accuracy: 0.8750
  ```

HINT:
  from sklearn.pipeline import Pipeline
  from sklearn.impute import SimpleImputer
  from sklearn.preprocessing import StandardScaler
  from sklearn.linear_model import LogisticRegression

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# acc = build_pipeline()
# print(f"Accuracy: {acc:.4f}")
