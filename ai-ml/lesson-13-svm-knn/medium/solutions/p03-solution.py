"""
Grid Search SVM: C and gamma
=============================
Perform grid search over C [0.1, 1, 10, 100] and gamma [0.001, 0.01, 0.1, 1]
with an RBF kernel. Print best parameters and score. Use scaled data.
"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

np.random.seed(42)


if __name__ == "__main__":
    X, y = make_classification(n_samples=500, n_features=10, n_informative=5, n_redundant=2,
                               random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Grid search
    param_grid = {
        "C": [0.1, 1, 10, 100],
        "gamma": [0.001, 0.01, 0.1, 1],
    }

    svm = SVC(kernel="rbf", random_state=42)
    grid_search = GridSearchCV(svm, param_grid, cv=5, scoring="accuracy", n_jobs=-1)
    grid_search.fit(X_train_scaled, y_train)

    print("=== SVM Grid Search (RBF kernel) ===")
    print(f"Best parameters: {grid_search.best_params_}")
    print(f"Best CV score:   {grid_search.best_score_:.4f}")
    print(f"Test accuracy:   {grid_search.score(X_test_scaled, y_test):.4f}")
    print()

    # Show full results
    results = grid_search.cv_results_
    print(f"{'C':>8} {'gamma':>10} {'mean_score':>12} {'rank':>6}")
    print("-" * 38)
    for i in range(len(results["params"])):
        p = results["params"][i]
        print(f"{p['C']:>8} {p['gamma']:>10} {results['mean_test_score'][i]:>12.4f} {results['rank_test_score'][i]:>6}")

    print()
    print("Key takeaway: C controls regularization (high C = less regularization),")
    print("gamma controls the RBF kernel width (high gamma = tight fit, risk of")
    print("overfitting). Grid search finds the best balance.")
