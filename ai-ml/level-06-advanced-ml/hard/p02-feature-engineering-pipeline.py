"""
LEVEL 06 — Advanced ML
HARD P02 — Full Feature Engineering Pipeline
========================================

CONCEPT:
  Real feature engineering = creating NEW features from existing ones:
    - income_per_age = income / age
    - age_squared = age²
    - is_weekend = day_of_week >= 5
    - income_log = log1p(income)

  Then feed everything into a Pipeline: engineer → scale → model.

PROBLEM:
  Write `engineer_and_train()` that:
    1. Creates DataFrame (200 rows, seed=42):
       age 18-70, income 20k-120k, day_of_week 0-6
       target = 1 if income/age > 1500 else 0
    2. Adds features: income_per_age, age_sq, income_log, is_weekend
    3. Split 80/20 (seed=42)
    4. Pipeline: StandardScaler → LogisticRegression(seed=42)
    5. Returns (test_acc, feature_names_list)

TRY THIS INPUT:
  ```python
  acc, feats = engineer_and_train()
  print(f"{acc:.4f}")
  print(feats)
  ```

EXPECTED OUTPUT:
  ```
  ~0.95+  (engineered feature income_per_age IS the target rule)
  ['age', 'income', 'day_of_week', 'income_per_age', 'age_sq',
   'income_log', 'is_weekend']
  ```

HINT:
  df['income_per_age'] = df['income'] / df['age']
  df['is_weekend'] = (df['day_of_week'] >= 5).astype(int)

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# acc, feats = engineer_and_train()
# print(acc, feats)
