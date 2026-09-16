"""Level 05 — Model Evaluation — Hard P03 Solution"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, GridSearchCV

def nested_cv():
    X, y = make_classification(n_samples=200, n_features=10, random_state=42)
    param_grid = {'n_estimators': [50, 100], 'max_depth': [3, 5]}
    inner = GridSearchCV(RandomForestClassifier(random_state=42),
                       param_grid, cv=3)
    scores = cross_val_score(inner, X, y, cv=5)
    return scores

if __name__ == "__main__":
    s = nested_cv()
    print(f"Scores: {s}")
    print(f"Mean: {s.mean():.4f} (+/- {s.std():.4f})")
