"""
LEVEL 02 — Python for ML
HARD P02 — ColumnTransformer on Mixed Data
========================================

CONCEPT:
  ColumnTransformer applies DIFFERENT preprocessing to DIFFERENT
  columns in one step — the professional way to handle mixed data.

  ColumnTransformer([
      ('num', num_pipeline, ['num_col1', 'num_col2']),
      ('cat', cat_pipeline, ['cat_col'])
  ])

PROBLEM:
  Write `build()` that:
    1. make_classification(200 samples, 5 features, n_informative=3, seed=42)
       → DataFrame with cols feature_0..feature_4
    2. Add a 'category' column: random choice of A/B/C (seeded!)
    3. Split 80/20 (random_state=42)
    4. ColumnTransformer:
         features → impute(mean) + StandardScaler
         category → impute(most_frequent) + OneHotEncoder
    5. Pipeline → RandomForestClassifier(seed=42)
    6. Return test accuracy

TRY THIS INPUT:
  ```python
  acc = build()
  print(f"Accuracy: {acc:.4f}")
  ```

EXPECTED OUTPUT:
  ```
  Accuracy: 0.9750
  ```

HINT:
  np.random.seed(42) before adding the category column, so the
  random categories are reproducible.

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# acc = build()
# print(acc)
