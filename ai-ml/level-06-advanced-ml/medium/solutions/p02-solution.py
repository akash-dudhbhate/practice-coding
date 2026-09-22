"""Level 06 — Advanced ML — Medium P02 Solution"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def select_top():
    X, y = make_classification(n_samples=200, n_features=10, n_informative=5, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    rf = RandomForestClassifier(random_state=42).fit(X_train, y_train)
    all_acc = rf.score(X_test, y_test)
    top5 = np.argsort(rf.feature_importances_)[-5:]
    rf2 = RandomForestClassifier(random_state=42).fit(X_train[:, top5], y_train)
    top5_acc = rf2.score(X_test[:, top5], y_test)
    return all_acc, top5_acc, sorted(top5.tolist())

if __name__ == "__main__":
    a, b, idx = select_top()
    print(f"All: {a:.4f}  Top5: {b:.4f}")
    print(idx)
