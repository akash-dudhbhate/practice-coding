"""
Compare Learning Rates with Adjusted n_estimators
===================================================
Test learning rates [0.001, 0.01, 0.1, 0.3] with adjusted n_estimators.
Print accuracy for each combination and identify the best.
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

    # Lower learning rate needs more estimators (and vice versa)
    configs = [
        (0.001, 1000),
        (0.01, 500),
        (0.1, 100),
        (0.3, 50),
    ]

    print(f"{'Learning Rate':>15} {'n_estimators':>15} {'Test Accuracy':>15}")
    print("-" * 47)

    results = []
    for lr, n_est in configs:
        gb = GradientBoostingClassifier(
            n_estimators=n_est, learning_rate=lr, max_depth=3, random_state=42,
        )
        gb.fit(X_train, y_train)
        acc = accuracy_score(y_test, gb.predict(X_test))
        results.append((lr, n_est, acc))
        print(f"{lr:>15.3f} {n_est:>15} {acc:>15.4f}")

    best = max(results, key=lambda r: r[2])
    print(f"\nBest: learning_rate={best[0]}, n_estimators={best[1]}, accuracy={best[2]:.4f}")
    print()
    print("Key takeaway: There's a trade-off between learning rate and")
    print("n_estimators. Smaller learning rates need more trees but converge")
    print("more smoothly. The 'sweet spot' is often around lr=0.1.")
