"""
RandomOverSampler and RandomUnderSampler
=========================================
Use imblearn's RandomOverSampler and RandomUnderSampler to balance the
dataset. Train a model on each and compare F1 scores. Print class counts
before and after resampling.
"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, classification_report
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler

np.random.seed(42)


if __name__ == "__main__":
    # Imbalanced dataset: 90:10
    X, y = make_classification(
        n_samples=1000,
        n_features=10,
        n_informative=5,
        weights=[0.90, 0.10],
        flip_y=0.0,
        random_state=42,
    )

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    print(f"Original train class counts: {dict(zip(*np.unique(y_train, return_counts=True)))}\n")

    # --- Random Over Sampling ---
    ros = RandomOverSampler(random_state=42)
    X_ros, y_ros = ros.fit_resample(X_train, y_train)
    print(f"After RandomOverSampler: {dict(zip(*np.unique(y_ros, return_counts=True)))}")

    model_ros = LogisticRegression(random_state=42, max_iter=1000)
    model_ros.fit(X_ros, y_ros)
    y_pred_ros = model_ros.predict(X_test)
    f1_ros = f1_score(y_test, y_pred_ros)
    print(f"F1 (oversampling): {f1_ros:.4f}\n")

    # --- Random Under Sampling ---
    rus = RandomUnderSampler(random_state=42)
    X_rus, y_rus = rus.fit_resample(X_train, y_train)
    print(f"After RandomUnderSampler: {dict(zip(*np.unique(y_rus, return_counts=True)))}")

    model_rus = LogisticRegression(random_state=42, max_iter=1000)
    model_rus.fit(X_rus, y_rus)
    y_pred_rus = model_rus.predict(X_test)
    f1_rus = f1_score(y_test, y_pred_rus)
    print(f"F1 (undersampling): {f1_rus:.4f}\n")

    # --- Baseline (no resampling) ---
    model_base = LogisticRegression(random_state=42, max_iter=1000)
    model_base.fit(X_train, y_train)
    y_pred_base = model_base.predict(X_test)
    f1_base = f1_score(y_test, y_pred_base)
    print(f"F1 (baseline):      {f1_base:.4f}\n")

    print("=== F1 Comparison ===")
    print(f"Baseline:       {f1_base:.4f}")
    print(f"Oversampling:   {f1_ros:.4f}")
    print(f"Undersampling:  {f1_rus:.4f}")
