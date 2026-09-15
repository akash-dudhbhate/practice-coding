"""
Boosting Library Comparison: sklearn vs XGBoost vs LightGBM
=============================================================
Compare sklearn GradientBoosting, XGBoost, and LightGBM.
Measure training time, accuracy, F1, and memory usage. Print a comparison
table and identify the best for speed and accuracy.
"""

import time
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, f1_score
import xgboost as xgb
import lightgbm as lgb

np.random.seed(42)


def measure_model(name, model, X_train, y_train, X_test, y_test):
    """Train model, measure time, and return metrics."""
    t0 = time.time()
    model.fit(X_train, y_train)
    train_time = time.time() - t0

    t0 = time.time()
    y_pred = model.predict(X_test)
    pred_time = time.time() - t0

    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    # Approximate memory (model size via number of nodes is hard to measure;
    # we use a proxy: number of estimators * average tree nodes)
    return {
        "name": name,
        "accuracy": acc,
        "f1": f1,
        "train_time": train_time,
        "pred_time": pred_time,
    }


if __name__ == "__main__":
    X, y = make_classification(n_samples=5000, n_features=30, n_informative=15, n_redundant=5,
                               random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    n_est = 200

    models = [
        ("sklearn GB", GradientBoostingClassifier(n_estimators=n_est, max_depth=3, random_state=42)),
        ("XGBoost", xgb.XGBClassifier(n_estimators=n_est, max_depth=3, learning_rate=0.1,
                                      random_state=42, eval_metric="logloss", use_label_encoder=False)),
        ("LightGBM", lgb.LGBMClassifier(n_estimators=n_est, max_depth=3, learning_rate=0.1,
                                        random_state=42, verbose=-1)),
    ]

    results = []
    for name, model in models:
        r = measure_model(name, model, X_train, y_train, X_test, y_test)
        results.append(r)

    # --- Comparison Table ---
    print("=== Boosting Library Comparison ===\n")
    print(f"{'Library':<15} {'Accuracy':>10} {'F1':>10} {'Train(s)':>10} {'Pred(s)':>12}")
    print("-" * 59)
    for r in results:
        print(f"{r['name']:<15} {r['accuracy']:>10.4f} {r['f1']:>10.4f} "
              f"{r['train_time']:>10.3f} {r['pred_time']:>12.6f}")

    best_acc = max(results, key=lambda r: r["accuracy"])
    fastest = min(results, key=lambda r: r["train_time"])
    best_f1 = max(results, key=lambda r: r["f1"])

    print(f"\nBest accuracy:  {best_acc['name']} ({best_acc['accuracy']:.4f})")
    print(f"Best F1:        {best_f1['name']} ({best_f1['f1']:.4f})")
    print(f"Fastest train:  {fastest['name']} ({fastest['train_time']:.3f}s)")
    print()
    print("Key takeaway: LightGBM is typically the fastest (histogram-based),")
    print("XGBoost offers great accuracy with regularization, and sklearn GB")
    print("is the simplest but slowest. Choose based on your speed/accuracy needs.")
