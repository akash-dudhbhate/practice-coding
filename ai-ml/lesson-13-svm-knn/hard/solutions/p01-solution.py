"""
Model Comparison: KNN, SVM(linear), SVM(RBF), Random Forest
============================================================
Tune the key hyperparameter for each model with cross-validation.
Print the best score for each and a comparison table. Identify the best model.
"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

np.random.seed(42)


if __name__ == "__main__":
    X, y = make_classification(n_samples=800, n_features=15, n_informative=8, n_redundant=3,
                               n_clusters_per_class=2, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)

    models = {
        "KNN": (KNeighborsClassifier(), {"n_neighbors": [3, 5, 7, 11, 15, 21]}),
        "SVM (linear)": (SVC(kernel="linear", random_state=42), {"C": [0.1, 1, 10]}),
        "SVM (RBF)": (SVC(kernel="rbf", random_state=42), {"C": [0.1, 1, 10], "gamma": ["scale", 0.01, 0.1]}),
        "Random Forest": (RandomForestClassifier(random_state=42), {"n_estimators": [50, 100, 200]}),
    }

    results = []
    print("=== Model Comparison ===\n")

    for name, (model, params) in models.items():
        gs = GridSearchCV(model, params, cv=5, scoring="accuracy", n_jobs=-1)
        gs.fit(X_train_s, y_train)
        test_acc = gs.score(X_test_s, y_test)
        results.append({
            "name": name,
            "best_params": gs.best_params_,
            "cv_score": gs.best_score_,
            "test_acc": test_acc,
        })
        print(f"{name:20s} | best params: {gs.best_params_} | CV: {gs.best_score_:.4f} | Test: {test_acc:.4f}")

    # Comparison table
    print(f"\n{'Model':<20} {'Best Params':<35} {'CV Score':>10} {'Test Acc':>10}")
    print("-" * 77)
    for r in results:
        params_str = str(r["best_params"])
        print(f"{r['name']:<20} {params_str:<35} {r['cv_score']:>10.4f} {r['test_acc']:>10.4f}")

    best = max(results, key=lambda r: r["test_acc"])
    print(f"\nBest model: {best['name']} (test accuracy = {best['test_acc']:.4f})")
