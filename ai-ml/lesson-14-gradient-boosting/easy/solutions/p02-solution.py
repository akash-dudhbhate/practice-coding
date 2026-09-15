"""
XGBoost vs sklearn Gradient Boosting
=====================================
Train XGBoost on the same dataset and compare accuracy with sklearn's
GradientBoostingClassifier.
"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
import xgboost as xgb

np.random.seed(42)


if __name__ == "__main__":
    X, y = make_classification(n_samples=1000, n_features=20, n_informative=10, n_redundant=5,
                               random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    # --- sklearn Gradient Boosting ---
    sk_gb = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
    sk_gb.fit(X_train, y_train)
    acc_sk = accuracy_score(y_test, sk_gb.predict(X_test))

    # --- XGBoost ---
    xgb_clf = xgb.XGBClassifier(n_estimators=100, learning_rate=0.1, max_depth=3,
                                random_state=42, eval_metric="logloss", use_label_encoder=False)
    xgb_clf.fit(X_train, y_train)
    acc_xgb = accuracy_score(y_test, xgb_clf.predict(X_test))

    print("=== XGBoost vs sklearn Gradient Boosting ===")
    print(f"sklearn GradientBoosting: {acc_sk:.4f}")
    print(f"XGBoost:                  {acc_xgb:.4f}")
    print(f"Difference:               {acc_xgb - acc_sk:+.4f}")
    print()
    print("Key takeaway: XGBoost is an optimized gradient boosting library")
    print("with regularization, faster training, and often slightly better")
    print("accuracy than sklearn's implementation.")
