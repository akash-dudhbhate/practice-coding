"""
Compare Decision Tree vs Random Forest
======================================
Train both models on the same dataset and compare train/test accuracy.
Show that random forest has better test accuracy (less overfitting).
"""

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


if __name__ == "__main__":
    X, y = make_classification(
        n_samples=800, n_features=15, n_informative=8,
        n_redundant=3, random_state=42
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Decision Tree (unlimited depth)
    dt = DecisionTreeClassifier(random_state=42)
    dt.fit(X_train, y_train)

    # Random Forest
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)

    dt_train = dt.score(X_train, y_train)
    dt_test = dt.score(X_test, y_test)
    rf_train = rf.score(X_train, y_train)
    rf_test = rf.score(X_test, y_test)

    print("=== Decision Tree vs Random Forest ===\n")
    print(f"{'Model':<20} {'Train Acc':<15} {'Test Acc':<15} {'Gap':<10}")
    print("-" * 60)
    print(f"{'Decision Tree':<20} {dt_train:<15.4f} {dt_test:<15.4f} {dt_train - dt_test:<10.4f}")
    print(f"{'Random Forest':<20} {rf_train:<15.4f} {rf_test:<15.4f} {rf_train - rf_test:<10.4f}")

    print("\n=== Analysis ===")
    if rf_test > dt_test:
        diff = rf_test - dt_test
        print(f"Random forest has better test accuracy by {diff:.4f}.")
    print(f"Decision tree train accuracy: {dt_train:.4f} (likely overfitting).")
    print(f"Random forest reduces overfitting by averaging many trees.")
    print(f"Random forest train-test gap is smaller, indicating better generalization.")
