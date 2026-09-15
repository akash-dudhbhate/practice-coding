"""
GridSearchCV for Random Forest
==============================
Tune n_estimators [50, 100, 200] and max_depth [3, 5, 10, None]
for a random forest using GridSearchCV.
Print best params, best score, and a full results table.
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import GridSearchCV


if __name__ == "__main__":
    X, y = make_classification(
        n_samples=800, n_features=15, n_informative=8,
        n_redundant=3, random_state=42
    )

    rf = RandomForestClassifier(random_state=42)

    param_grid = {
        "n_estimators": [50, 100, 200],
        "max_depth": [3, 5, 10, None],
    }

    grid_search = GridSearchCV(
        rf, param_grid, cv=5, scoring="accuracy",
        return_train_score=True, n_jobs=-1
    )
    grid_search.fit(X, y)

    print("=== GridSearchCV for Random Forest ===\n")
    print(f"Best parameters: {grid_search.best_params_}")
    print(f"Best CV score:   {grid_search.best_score_:.4f}\n")

    # Full results table
    results = grid_search.cv_results_
    df = pd.DataFrame({
        "n_estimators": results["param_n_estimators"],
        "max_depth": results["param_max_depth"],
        "mean_test_score": results["mean_test_score"],
        "std_test_score": results["std_test_score"],
        "mean_train_score": results["mean_train_score"],
        "rank": results["rank_test_score"],
    })
    df = df.sort_values("rank")

    print("=== All Results (sorted by rank) ===\n")
    print(df.to_string(index=False, float_format="{:.4f}".format))

    print(f"\n=== Interpretation ===")
    print(f"Tested {len(df)} parameter combinations with 5-fold CV.")
    print(f"Best: n_estimators={grid_search.best_params_['n_estimators']}, "
          f"max_depth={grid_search.best_params_['max_depth']}")
    print("More estimators generally improve performance but increase training time.")
    print("max_depth=None allows full tree growth; may or may not be best depending on data.")
