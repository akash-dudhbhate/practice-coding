"""
SMOTE vs Random Oversampling
=============================
Apply SMOTE (Synthetic Minority Over-sampling Technique) to imbalanced data
and compare F1 with random oversampling. Use imblearn.pipeline.Pipeline to
ensure no data leakage (resampling only applied to training folds in CV).
"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, classification_report
from imblearn.over_sampling import SMOTE, RandomOverSampler
from imblearn.pipeline import Pipeline  # imblearn Pipeline, not sklearn!

np.random.seed(42)


if __name__ == "__main__":
    # Imbalanced dataset: 95:5
    X, y = make_classification(
        n_samples=2000,
        n_features=15,
        n_informative=8,
        weights=[0.95, 0.05],
        flip_y=0.0,
        random_state=42,
    )

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    print(f"Train class counts: {dict(zip(*np.unique(y_train, return_counts=True)))}\n")

    # --- Baseline (no resampling) ---
    model_base = RandomForestClassifier(random_state=42, n_estimators=100)
    model_base.fit(X_train, y_train)
    f1_base = f1_score(y_test, model_base.predict(X_test))

    # --- Random Oversampling (with imblearn Pipeline for no leakage) ---
    pipe_ros = Pipeline([
        ("ros", RandomOverSampler(random_state=42)),
        ("clf", RandomForestClassifier(random_state=42, n_estimators=100)),
    ])
    pipe_ros.fit(X_train, y_train)
    f1_ros = f1_score(y_test, pipe_ros.predict(X_test))

    # --- SMOTE (with imblearn Pipeline for no leakage) ---
    pipe_smote = Pipeline([
        ("smote", SMOTE(random_state=42, k_neighbors=5)),
        ("clf", RandomForestClassifier(random_state=42, n_estimators=100)),
    ])
    pipe_smote.fit(X_train, y_train)
    f1_smote = f1_score(y_test, pipe_smote.predict(X_test))

    # --- Cross-validation comparison (no leakage) ---
    cv_f1_base = cross_val_score(RandomForestClassifier(random_state=42, n_estimators=100),
                                 X_train, y_train, cv=5, scoring="f1").mean()
    cv_f1_smote = cross_val_score(pipe_smote, X_train, y_train, cv=5, scoring="f1").mean()

    print("=== F1 Comparison (test set) ===")
    print(f"Baseline:            {f1_base:.4f}")
    print(f"Random Oversampling: {f1_ros:.4f}")
    print(f"SMOTE:               {f1_smote:.4f}")
    print()
    print("=== Cross-validated F1 (no leakage) ===")
    print(f"Baseline CV F1: {cv_f1_base:.4f}")
    print(f"SMOTE CV F1:    {cv_f1_smote:.4f}")
    print()
    print("Key takeaway: imblearn Pipeline applies SMOTE only to training")
    print("folds during CV, preventing data leakage. SMOTE generates")
    print("synthetic minority samples, often outperforming random duplication.")
