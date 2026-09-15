"""
Tune XGBoost with Grid Search
==============================
Grid search over max_depth [3,5,7], learning_rate [0.01,0.1],
n_estimators [100,500]. Print best parameters and score. Use early stopping.
"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score
import xgboost as xgb

np.random.seed(42)


if __name__ == "__main__":
    X, y = make_classification(n_samples=1000, n_features=20, n_informative=10, n_redundant=5,
                               random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    # Grid search
    param_grid = {
        "max_depth": [3, 5, 7],
        "learning_rate": [0.01, 0.1],
        "n_estimators": [100, 500],
    }

    xgb_clf = xgb.XGBClassifier(
        random_state=42, eval_metric="logloss",
        early_stopping_rounds=10,
        use_label_encoder=False,
    )

    # For early_stopping_rounds in grid search, we need a validation set
    # GridSearchCV will handle CV splits; early stopping uses internal validation
    grid_search = GridSearchCV(
        xgb_clf, param_grid, cv=5, scoring="accuracy", n_jobs=-1,
        # Pass eval_set via fit_params through the estimator's early stopping
    )

    # Fit with eval_set for early stopping
    X_train_sub, X_val, y_train_sub, y_val = train_test_split(
        X_train, y_train, test_size=0.15, random_state=42, stratify=y_train
    )

    grid_search.fit(X_train_sub, y_train_sub, eval_set=[(X_val, y_val)], verbose=False)

    print("=== XGBoost Grid Search ===")
    print(f"Best parameters: {grid_search.best_params_}")
    print(f"Best CV score:   {grid_search.best_score_:.4f}")
    print(f"Test accuracy:   {accuracy_score(y_test, grid_search.predict(X_test)):.4f}")
    print()

    # Show all results
    results = grid_search.cv_results_
    print(f"{'max_depth':>10} {'lr':>8} {'n_est':>8} {'mean_acc':>10} {'rank':>6}")
    print("-" * 44)
    for i in range(len(results["params"])):
        p = results["params"][i]
        print(f"{p['max_depth']:>10} {p['learning_rate']:>8} {p['n_estimators']:>8} "
              f"{results['mean_test_score'][i]:>10.4f} {results['rank_test_score'][i]:>6}")

    print()
    print("Key takeaway: Grid search systematically explores hyperparameter")
    print("combinations. Early stopping prevents overfitting by halting when")
    print("validation performance stops improving.")
