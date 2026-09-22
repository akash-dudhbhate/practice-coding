"""
LEVEL 02 — Python for ML
HARD P01 — Prevent Data Leakage
========================================

CONCEPT:
  DATA LEAKAGE = when info from test data "leaks" into training.
  Example: if you fit a scaler on ALL data before splitting, the
  test data's statistics influenced training → inflated scores.

  RULE: split FIRST. Then fit preprocessing on train ONLY.

  sklearn Pipeline does this correctly — inside fit(), each step
  only sees training data.

PROBLEM:
  Write `train_clean()` that:
    1. Builds this dataset (200 rows):
         age (int 18-70, ~20 NaN), income (int 20k-120k),
         city (Mumbai/Delhi/Chennai, ~15 NaN),
         target = 1 if age > 40 else 0  (compute BEFORE injecting NaN!)
    2. Splits 80/20 (random_state=42)
    3. ColumnTransformer:
         numeric [age, income] → SimpleImputer(median) + StandardScaler
         categorical [city]    → SimpleImputer(most_frequent) + OneHotEncoder
    4. Pipeline(preprocessor → RandomForestClassifier(50, seed=42))
    5. Returns (train_acc, test_acc)

TRY THIS INPUT:
  ```python
  tr, te = train_clean()
  print(f"Train: {tr:.4f}  Test: {te:.4f}")
  ```

EXPECTED OUTPUT:
  ```
  Train: 1.0000  Test: 0.9500
  ```

HINT:
  ColumnTransformer([('num', Pipeline([...]), ['age','income']),
                     ('cat', Pipeline([...]), ['city'])])
  Use OneHotEncoder(handle_unknown='ignore').

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# tr, te = train_clean()
# print(tr, te)
