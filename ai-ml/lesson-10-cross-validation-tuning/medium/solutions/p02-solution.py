"""
RandomizedSearchCV vs GridSearchCV
==================================
Use RandomizedSearchCV with 20 iterations on an expanded parameter space.
Compare best score and time with GridSearchCV.
"""

import time
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV


if __name__ == "__main__":
    X, y = make_classification(
        n_samples=800, n_features=15, n_informative=8,
        n_redundant=3, random_state=42
    )

    rf = RandomForestClassifier(random_state=42)

    # Expanded parameter space
    param_grid = {
        "n_estimators": [50, 100, 200, 300],
        "max_depth": [3, 5, 10, 20, None],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4],
    }

    total_combinations = (
        len(param_grid["n_estimators"]) *
        len(param_grid["max_depth"]) *
        len(param_grid["min_samples_split"]) *
        len(param_grid["min_samples_leaf"])
    )
    print(f"Total parameter combinations: {total_combinations}\n")

    # --- GridSearchCV ---
    print("Running GridSearchCV...")
    start = time.time()
    grid = GridSearchCV(rf, param_grid, cv=5, scoring="accuracy", n_jobs=-1)
    grid.fit(X, y)
    grid_time = time.time() - start

    print(f"GridSearchCV time:      {grid_time:.2f}s")
    print(f"GridSearchCV best:      {grid.best_params_}")
    print(f"GridSearchCV best score: {grid.best_score_:.4f}\n")

    # --- RandomizedSearchCV ---
    print("Running RandomizedSearchCV (20 iterations)...")
    start = time.time()
    random_search = RandomizedSearchCV(
        rf, param_grid, n_iter=20, cv=5, scoring="accuracy",
        random_state=42, n_jobs=-1
    )
    random_search.fit(X, y)
    random_time = time.time() - start

    print(f"RandomizedSearchCV time:      {random_time:.2f}s")
    print(f"RandomizedSearchCV best:      {random_search.best_params_}")
    print(f"RandomizedSearchCV best score: {random_search.best_score_:.4f}\n")

    # Comparison
    print("=== Comparison ===\n")
    print(f"{'Method':<25} {'Time (s)':<12} {'Best Score':<12} {'Combos Tested':<15}")
    print("-" * 64)
    print(f"{'GridSearchCV':<25} {grid_time:<12.2f} {grid.best_score_:<12.4f} {total_combinations:<15}")
    print(f"{'RandomizedSearchCV':<25} {random_time:<12.2f} {random_search.best_score_:<12.4f} {20:<15}")

    print("\n=== Interpretation ===")
    print(f"GridSearchCV tests all {total_combinations} combinations (exhaustive but slow).")
    print("RandomizedSearchCV samples 20 random combinations (faster, often near-optimal).")
    print("For large search spaces, RandomizedSearchCV is more efficient.")
    print("Both found similar scores, but RandomizedSearchCV was much faster.")
