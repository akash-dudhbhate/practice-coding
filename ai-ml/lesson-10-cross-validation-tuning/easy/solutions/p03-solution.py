"""
GridSearchCV to Tune max_depth for Decision Tree
================================================
Use GridSearchCV to find the best max_depth from [1, 3, 5, 10, 20]
for a decision tree on make_classification.
Print the best depth and best score.
"""

from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import GridSearchCV, train_test_split


if __name__ == "__main__":
    X, y = make_classification(
        n_samples=800, n_features=15, n_informative=8,
        n_redundant=3, random_state=42
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    tree = DecisionTreeClassifier(random_state=42)

    param_grid = {"max_depth": [1, 3, 5, 10, 20]}

    grid_search = GridSearchCV(
        tree, param_grid, cv=5, scoring="accuracy", return_train_score=True
    )
    grid_search.fit(X_train, y_train)

    print("=== GridSearchCV Results ===\n")
    print(f"Best max_depth: {grid_search.best_params_['max_depth']}")
    print(f"Best CV score:  {grid_search.best_score_:.4f}")

    # Test set performance with best model
    best_model = grid_search.best_estimator_
    test_score = best_model.score(X_test, y_test)
    print(f"Test accuracy:  {test_score:.4f}\n")

    # All results
    print("=== All Results ===\n")
    print(f"{'max_depth':<12} {'Mean CV Acc':<15} {'Std':<10} {'Train Acc':<12}")
    print("-" * 49)
    results = grid_search.cv_results_
    for i, depth in enumerate(param_grid["max_depth"]):
        mean = results["mean_test_score"][i]
        std = results["std_test_score"][i]
        train_mean = results["mean_train_score"][i]
        print(f"{depth:<12} {mean:<15.4f} {std:<10.4f} {train_mean:<12.4f}")

    print("\n=== Interpretation ===")
    print(f"GridSearchCV tested {len(param_grid['max_depth'])} values with 5-fold CV.")
    print(f"Best max_depth={grid_search.best_params_['max_depth']} with CV accuracy={grid_search.best_score_:.4f}.")
    print("Low depth: underfitting. High depth: overfitting. Best depth balances both.")
