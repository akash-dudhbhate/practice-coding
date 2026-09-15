"""
Gradient Boosting with Early Stopping
======================================
Use n_iter_no_change for early stopping in GradientBoostingClassifier.
Print accuracy and the number of estimators actually used.
"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score

np.random.seed(42)


if __name__ == "__main__":
    X, y = make_classification(n_samples=1000, n_features=20, n_informative=10, n_redundant=5,
                               random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    # Without early stopping (all 200 estimators)
    gb_full = GradientBoostingClassifier(n_estimators=200, learning_rate=0.1, max_depth=3, random_state=42)
    gb_full.fit(X_train, y_train)
    acc_full = accuracy_score(y_test, gb_full.predict(X_test))

    # With early stopping: stop if no improvement for 10 iterations
    gb_early = GradientBoostingClassifier(
        n_estimators=200, learning_rate=0.1, max_depth=3,
        n_iter_no_change=10, validation_fraction=0.15,
        tol=1e-4, random_state=42,
    )
    gb_early.fit(X_train, y_train)
    acc_early = accuracy_score(y_test, gb_early.predict(X_test))

    print("=== Gradient Boosting: Early Stopping ===")
    print(f"Without early stopping: accuracy={acc_full:.4f}, estimators used={gb_full.n_estimators}")
    print(f"With early stopping:    accuracy={acc_early:.4f}, estimators used={gb_early.n_estimators_}")
    print(f"Estimators saved:       {gb_full.n_estimators - gb_early.n_estimators_}")
    print()
    print("Key takeaway: Early stopping monitors a validation fraction and")
    print("halts training when performance stops improving. This prevents")
    print("overfitting and reduces unnecessary computation.")
