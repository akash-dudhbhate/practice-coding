"""Level 05 Evaluation — Easy P03 Solution"""

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import numpy as np

def solve():
    iris = load_iris()
    X, y = iris.data, iris.target
    rf = RandomForestClassifier(random_state=42)
    scores = cross_val_score(rf, X, y, cv=5)
    print(f"Fold scores: {scores}")
    print(f"Mean accuracy: {scores.mean():.4f}")
    print(f"Std accuracy: {scores.std():.4f}")
    return scores

if __name__ == "__main__":
    solve()