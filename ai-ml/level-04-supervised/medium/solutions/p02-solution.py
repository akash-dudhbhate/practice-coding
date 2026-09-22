"""Level 04 — Supervised Learning — Medium P02 Solution"""

from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def train_forest():
    X, y = make_classification(n_samples=200, n_features=5, n_informative=3, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    return rf.score(X_test, y_test), rf.feature_importances_

if __name__ == "__main__":
    acc, imp = train_forest()
    print(f"Accuracy: {acc:.4f}")
    for i, v in enumerate(imp):
        print(f"  Feature {i}: {v:.4f}")
