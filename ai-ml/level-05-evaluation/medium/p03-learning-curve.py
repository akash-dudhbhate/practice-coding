"""
LEVEL 05 — Model Evaluation
MEDIUM P03 — Learning Curve
========================================

CONCEPT:
  Learning curve = score vs training-set size.
    - Train score high + val score low + gap → overfitting
    - Both low and converging → underfitting / need better model
    - Both high and converging → good; more data won't help much

  sklearn's learning_curve() does the sampling + CV for you.

PROBLEM:
  Write `plot_learning_curve()` that:
    1. make_classification(500, 10 features, seed=42)
    2. learning_curve(LogisticRegression, cv=5,
                      train_sizes=linspace(0.1, 1.0, 10))
    3. Plots train vs validation mean scores, saves
       'learning_curve.png'
    4. Returns (train_sizes, train_mean, val_mean)

TRY THIS INPUT:
  ```python
  ts, tr, va = plot_learning_curve()
  print(len(ts))          # 10
  print(f"{va[-1]:.4f}")  # final validation score
  ```

EXPECTED OUTPUT:
  ```
  10
  0.8xxx
  ```

HINT:
  from sklearn.model_selection import learning_curve
  train_scores is (10, 5) — take np.mean(axis=1)

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# ts, tr, va = plot_learning_curve()
# print(va[-1])
