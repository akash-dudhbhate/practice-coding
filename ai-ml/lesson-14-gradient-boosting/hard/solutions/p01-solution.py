"""
Complete XGBoost Pipeline
==========================
End-to-end XGBoost pipeline on a real dataset:
  1. Preprocess (handle categoricals, scale)
  2. Grid search (max_depth, learning_rate, n_estimators, subsample, colsample_bytree)
  3. Early stopping with cross-validation
  4. Plot feature importance
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score
import xgboost as xgb

np.random.seed(42)


if __name__ == "__main__":
    # Load a real dataset (adult/census income from OpenML)
    try:
        dataset = fetch_openml(name="adult", version=2, as_frame=True, parser="auto")
        df = dataset.frame
    except Exception:
        # Fallback: use a smaller synthetic dataset if OpenML is unavailable
        from sklearn.datasets import make_classification
        X_synth, y_synth = make_classification(n_samples=2000, n_features=15, n_informative=8,
                                               n_redundant=3, random_state=42)
        df = pd.DataFrame(X_synth, columns=[f"feat_{i}" for i in range(15)])
        df["target"] = y_synth

    print(f"Dataset shape: {df.shape}")
    print(df.head(), "\n")

    # Determine target column
    if "class" in df.columns:
        target_col = "class"
    elif "target" in df.columns:
        target_col = "target"
    else:
        target_col = df.columns[-1]

    y_raw = df[target_col]
    X_df = df.drop(columns=[target_col])

    # Encode target if categorical
    if y_raw.dtype == "object" or y_raw.dtype.name == "category":
        le = LabelEncoder()
        y = le.fit_transform(y_raw)
    else:
        y = y_raw.values

    # Encode categorical features
    X_df = pd.get_dummies(X_df, drop_first=True)

    # Scale numeric features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_df)
    feature_names = X_df.columns.tolist()

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42, stratify=y
    )

    # --- Grid Search ---
    param_grid = {
        "max_depth": [3, 5, 7],
        "learning_rate": [0.01, 0.1],
        "n_estimators": [100, 300],
        "subsample": [0.8, 1.0],
        "colsample_bytree": [0.8, 1.0],
    }

    xgb_clf = xgb.XGBClassifier(
        random_state=42, eval_metric="logloss",
        early_stopping_rounds=10, use_label_encoder=False,
    )

    # Use a validation split for early stopping
    X_tr, X_val, y_tr, y_val = train_test_split(
        X_train, y_train, test_size=0.15, random_state=42, stratify=y_train
    )

    grid_search = GridSearchCV(xgb_clf, param_grid, cv=3, scoring="accuracy", n_jobs=-1, verbose=0)
    grid_search.fit(X_tr, y_tr, eval_set=[(X_val, y_val)], verbose=False)

    print("=== Grid Search Results ===")
    print(f"Best parameters: {grid_search.best_params_}")
    print(f"Best CV score:   {grid_search.best_score_:.4f}")
    print(f"Test accuracy:   {accuracy_score(y_test, grid_search.predict(X_test)):.4f}\n")

    # --- Feature Importance ---
    best_model = grid_search.best_estimator_
    importances = best_model.feature_importances_

    # Sort and show top 15
    sorted_idx = np.argsort(importances)[::-1][:15]
    plt.figure(figsize=(10, 6))
    plt.barh(range(len(sorted_idx)), importances[sorted_idx][::-1])
    plt.yticks(range(len(sorted_idx)), [feature_names[i] for i in sorted_idx[::-1]])
    plt.xlabel("Feature Importance")
    plt.title("XGBoost — Top 15 Feature Importances")
    plt.tight_layout()
    plt.savefig("xgboost_feature_importance.png", dpi=150)
    print("Feature importance plot saved to xgboost_feature_importance.png")

    print("\nTop 5 features:")
    for i in sorted_idx[:5]:
        print(f"  {feature_names[i]:30s}  importance={importances[i]:.4f}")
