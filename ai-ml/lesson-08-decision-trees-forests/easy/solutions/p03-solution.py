"""
Decision Tree: With vs Without max_depth
========================================
Compare a decision tree with max_depth vs unlimited depth.
Show that unlimited depth overfits (high train, lower test accuracy).
"""

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


if __name__ == "__main__":
    X, y = make_classification(
        n_samples=500, n_features=10, n_informative=5,
        n_redundant=2, n_repeated=1, random_state=42
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # Tree with max_depth=3 (constrained)
    tree_limited = DecisionTreeClassifier(max_depth=3, random_state=42)
    tree_limited.fit(X_train, y_train)

    # Tree with unlimited depth (can overfit)
    tree_unlimited = DecisionTreeClassifier(max_depth=None, random_state=42)
    tree_unlimited.fit(X_train, y_train)

    train_acc_limited = tree_limited.score(X_train, y_train)
    test_acc_limited = tree_limited.score(X_test, y_test)
    train_acc_unlimited = tree_unlimited.score(X_train, y_train)
    test_acc_unlimited = tree_unlimited.score(X_test, y_test)

    print("=== Decision Tree: With vs Without max_depth ===\n")
    print(f"{'Model':<25} {'Train Acc':<15} {'Test Acc':<15} {'Gap':<10}")
    print("-" * 65)
    print(f"{'max_depth=3':<25} {train_acc_limited:<15.4f} {test_acc_limited:<15.4f} {train_acc_limited - test_acc_limited:<10.4f}")
    print(f"{'max_depth=None':<25} {train_acc_unlimited:<15.4f} {test_acc_unlimited:<15.4f} {train_acc_unlimited - test_acc_unlimited:<10.4f}")

    print("\n=== Overfitting Analysis ===")
    gap_unlimited = train_acc_unlimited - test_acc_unlimited
    gap_limited = train_acc_limited - test_acc_limited
    print(f"Unlimited depth train accuracy: {train_acc_unlimited:.4f} (perfect = overfitting)")
    print(f"Unlimited depth test accuracy:  {test_acc_unlimited:.4f}")
    print(f"Train-test gap (unlimited):     {gap_unlimited:.4f} (large gap = overfitting)")
    print(f"\nLimited depth train accuracy:   {train_acc_limited:.4f}")
    print(f"Limited depth test accuracy:    {test_acc_limited:.4f}")
    print(f"Train-test gap (limited):       {gap_limited:.4f} (smaller gap = better generalization)")
    print("\nConclusion: Constraining max_depth prevents overfitting.")
