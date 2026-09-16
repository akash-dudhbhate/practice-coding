"""Level 05 Evaluation — Hard P03 Solution"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, GridSearchCV

def solve():
    X, y = make_classification(n_samples=200, n_features=10, random_state=42)
    # Inner CV for hyperparameter tuning
    param_grid = {'n_estimators': [50, 100], 'max_depth': [3, 5]}
    rf = RandomForestClassifier(random_state=42)
    inner_cv = GridSearchCV(rf, param_grid, cv=3)
    # Outer CV for unbiased evaluation
    outer_scores = cross_val_score(inner_cv, X, y, cv=5)
    print(f"Nested CV scores: {outer_scores}")
    print(f"Mean: {outer_scores.mean():.4f} (+/- {outer_scores.std():.4f})")
    return outer_scores

if __name__ == "__main__":
    solve()