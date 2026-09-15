"""
GradientBoostingClassifier vs Single Decision Tree
===================================================
Train sklearn's GradientBoostingClassifier on a synthetic dataset.
Print accuracy and compare with a single DecisionTreeClassifier.
"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

np.random.seed(42)


if __name__ == "__main__":
    X, y = make_classification(n_samples=1000, n_features=20, n_informative=10, n_redundant=5,
                               random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    # --- Single Decision Tree ---
    dt = DecisionTreeClassifier(random_state=42)
    dt.fit(X_train, y_train)
    acc_dt = accuracy_score(y_test, dt.predict(X_test))

    # --- Gradient Boosting ---
    gb = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
    gb.fit(X_train, y_train)
    acc_gb = accuracy_score(y_test, gb.predict(X_test))

    print("=== Gradient Boosting vs Decision Tree ===")
    print(f"Decision Tree:       {acc_dt:.4f}")
    print(f"Gradient Boosting:   {acc_gb:.4f}")
    print(f"Improvement:         {acc_gb - acc_dt:+.4f}")
    print()
    print("Key takeaway: Gradient boosting builds trees sequentially, each")
    print("correcting the errors of the previous ones. This ensemble approach")
    print("typically outperforms a single decision tree.")
