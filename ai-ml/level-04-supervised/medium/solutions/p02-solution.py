"""Level 04 Supervised — Medium P02 Solution"""

from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np

def solve():
    X, y = make_classification(n_samples=200, n_features=5, n_informative=3, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    accuracy = rf.score(X_test, y_test)
    importances = rf.feature_importances_
    print(f"Accuracy: {accuracy:.4f}")
    print("Feature importances:")
    for i, imp in enumerate(importances):
        print(f"  Feature {i}: {imp:.4f}")
    return accuracy, importances

if __name__ == "__main__":
    solve()