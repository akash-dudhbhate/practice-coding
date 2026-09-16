"""
LESSON — Gradient Boosting
HARD P01 — Build a complete XGBoost pipeline: load a real dataset, preprocess, tune with grid search (max_depth, learning_rate, n_estimators, subsample, colsample_bytree), use early stopping, evaluate with CV, and plot feature importance.
==================================================

CONCEPT:
  See concepts.md in this lesson folder for detailed explanations.

PROBLEM:
  Build a complete XGBoost pipeline: load a real dataset, preprocess, tune with grid search (max_depth, learning_rate, n_estimators, subsample, colsample_bytree), use early stopping, evaluate with CV, and plot feature importance


Write a function `solve()` that implements the solution.

# Check your answer: compare with solutions/p01-solution.py
"""

TRY THIS INPUT:
  Add this test code at the bottom of your file:

  ```python
  dataset = fetch_openml(name="adult", version=2, as_frame=True, parser="auto")
  df = dataset.frame
  X_synth, y_synth = make_classification(n_samples=2000, n_features=15, n_informative=8,
  n_redundant=3, random_state=42)
  df = pd.DataFrame(X_synth, columns=[f"feat_{i}" for i in range(15)])
  df["target"] = y_synth

  # Call your function
  result = solve(...)
  print(result)
  ```

EXPECTED OUTPUT:
  Run the solution file to see expected output:
    python3 hard/solutions/p01-solution.py

  Then compare your output format with theirs.

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
