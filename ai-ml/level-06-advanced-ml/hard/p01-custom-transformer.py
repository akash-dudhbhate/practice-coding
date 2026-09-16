"""
LEVEL 06 — Advanced ML
HARD P01 — Custom sklearn Transformer
========================================

CONCEPT:
  You can write your own transformer that plugs into any Pipeline.
  Rules: subclass BaseEstimator + TransformerMixin, implement
  fit() and transform(). fit() returns self; transform() returns data.

  Why: reusable feature engineering — e.g., log-transform skewed
  columns, add interaction terms, bin ages.

PROBLEM:
  Write a class `LogTransformer` (subclass BaseEstimator,
  TransformerMixin) that:
    - fit(X, y=None): returns self
    - transform(X): returns np.log1p(X) — but ONLY on columns
      given at init: LogTransformer(cols=[0, 2])
  Then use it in a Pipeline before LogisticRegression on
  make_classification(200, 5 features, seed=42), return test acc.

TRY THIS INPUT:
  ```python
  acc = run_pipeline()
  print(f"{acc:.4f}")
  ```

EXPECTED OUTPUT:
  ```
  0.8750
  ```

HINT:
  from sklearn.base import BaseEstimator, TransformerMixin
  transform: copy X, apply np.log1p to self.cols only.
  Careful: log1p needs non-negative values — use np.abs first if
  features can be negative.

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# acc = run_pipeline()
# print(acc)
