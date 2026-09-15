"""
Random Forest vs Gradient Boosting
===================================
Compare Random Forest and Gradient Boosting. Tune key hyperparameters for
each. Print best accuracy, training time, and prediction time in a table.
"""

import time
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score

np.random.seed(42)


if __name__ == "__main__":
    X, y = make_classification(n_samples=2000, n_features=25, n_informative=12, n_redundant=5,
                               random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    results = []

    # --- Random Forest ---
    rf_params = {"n_estimators": [50, 100, 200], "max_depth": [5, 10, None]}
    rf = RandomForestClassifier(random_state=42, n_jobs=-1)
    gs_rf = GridSearchCV(rf, rf_params, cv=5, scoring="accuracy", n_jobs=-1)

    t0 = time.time()
    gs_rf.fit(X_train, y_train)
    train_time_rf = time.time() - t0

    t0 = time.time()
    y_pred_rf = gs_rf.predict(X_test)
    pred_time_rf = time.time() - t0

    acc_rf = accuracy_score(y_test, y_pred_rf)
    results.append(("Random Forest", gs_rf.best_params_, acc_rf, train_time_rf, pred_time_rf))

    # --- Gradient Boosting ---
    gb_params = {"n_estimators": [50, 100, 200], "max_depth": [3, 5], "learning_rate": [0.1, 0.3]}
    gb = GradientBoostingClassifier(random_state=42)
    gs_gb = GridSearchCV(gb, gb_params, cv=5, scoring="accuracy", n_jobs=-1)

    t0 = time.time()
    gs_gb.fit(X_train, y_train)
    train_time_gb = time.time() - t0

    t0 = time.time()
    y_pred_gb = gs_gb.predict(X_test)
    pred_time_gb = time.time() - t0

    acc_gb = accuracy_score(y_test, y_pred_gb)
    results.append(("Gradient Boosting", gs_gb.best_params_, acc_gb, train_time_gb, pred_time_gb))

    # --- Comparison Table ---
    print("=== Random Forest vs Gradient Boosting ===\n")
    print(f"{'Model':<20} {'Best Params':<45} {'Accuracy':>10} {'Train(s)':>10} {'Pred(s)':>10}")
    print("-" * 97)
    for name, params, acc, tt, pt in results:
        print(f"{name:<20} {str(params):<45} {acc:>10.4f} {tt:>10.3f} {pt:>10.6f}")

    best = max(results, key=lambda r: r[2])
    fastest_train = min(results, key=lambda r: r[3])
    print(f"\nBest accuracy:    {best[0]} ({best[2]:.4f})")
    print(f"Fastest training: {fastest_train[0]} ({fastest_train[3]:.3f}s)")
    print()
    print("Key takeaway: RF trains trees in parallel (faster), GB trains")
    print("sequentially (slower but often more accurate). RF is less prone")
    print("to overfitting; GB can squeeze out more performance with tuning.")
