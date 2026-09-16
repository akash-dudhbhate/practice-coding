"""Level 06 Advanced Ml — Medium P02 Solution"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def solve():
    X, y = make_classification(n_samples=200, n_features=10, n_informative=5, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    rf = RandomForestClassifier(random_state=42).fit(X_train, y_train)
    importances = rf.feature_importances_
    # Select top 5 features
    top_idx = np.argsort(importances)[-5:]
    X_train_top = X_train[:, top_idx]
    X_test_top = X_test[:, top_idx]
    rf_top = RandomForestClassifier(random_state=42).fit(X_train_top, y_train)
    acc_all = rf.score(X_test, y_test)
    acc_top = rf_top.score(X_test_top, y_test)
    print(f"All features accuracy: {acc_all:.4f}")
    print(f"Top 5 features accuracy: {acc_top:.4f}")
    print(f"Top features: {list(top_idx)}")
    return top_idx, acc_all, acc_top

if __name__ == "__main__":
    solve()