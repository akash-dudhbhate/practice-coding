"""
Feature Engineering Comparison: Staged Improvement
===================================================
Compare model accuracy at four stages of feature engineering:
  (a) raw features
  (b) scaled features
  (c) scaled + encoded categoricals
  (d) scaled + encoded + interaction features
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

np.random.seed(42)


if __name__ == "__main__":
    # Synthetic dataset with numeric + categorical features
    n = 500
    age = np.random.randint(18, 70, n)
    income = np.random.randint(20000, 150000, n)
    education = np.random.choice(["highschool", "bachelor", "master", "phd"], n)
    city = np.random.choice(["NYC", "LA", "Chicago", "Houston"], n)
    # Target: buy product (1) or not (0)
    prob = 1 / (1 + np.exp(-(0.00003 * income + 0.02 * age - 3)))
    y = (np.random.rand(n) < prob).astype(int)

    df = pd.DataFrame({"age": age, "income": income, "education": education, "city": city, "y": y})

    # --- Stage (a): Raw features (numeric only) ---
    X_a = df[["age", "income"]]
    X_tr, X_te, y_tr, y_te = train_test_split(X_a, y, test_size=0.2, random_state=42, stratify=y)
    m = RandomForestClassifier(random_state=42, n_estimators=100)
    m.fit(X_tr, y_tr)
    acc_a = accuracy_score(y_te, m.predict(X_te))

    # --- Stage (b): Scaled features ---
    scaler = StandardScaler()
    X_b = scaler.fit_transform(df[["age", "income"]])
    X_tr, X_te, y_tr, y_te = train_test_split(X_b, y, test_size=0.2, random_state=42, stratify=y)
    m = RandomForestClassifier(random_state=42, n_estimators=100)
    m.fit(X_tr, y_tr)
    acc_b = accuracy_score(y_te, m.predict(X_te))

    # --- Stage (c): Scaled + encoded categoricals ---
    df_encoded = pd.get_dummies(df, columns=["education", "city"], drop_first=True)
    feature_cols_c = ["age", "income"] + [c for c in df_encoded.columns if c.startswith(("education_", "city_"))]
    X_c = df_encoded[feature_cols_c].values.astype(float)
    X_c[:, :2] = StandardScaler().fit_transform(X_c[:, :2])  # scale numeric
    X_tr, X_te, y_tr, y_te = train_test_split(X_c, y, test_size=0.2, random_state=42, stratify=y)
    m = RandomForestClassifier(random_state=42, n_estimators=100)
    m.fit(X_tr, y_tr)
    acc_c = accuracy_score(y_te, m.predict(X_te))

    # --- Stage (d): Scaled + encoded + interactions ---
    df_encoded["age_income"] = df_encoded["age"] * df_encoded["income"]
    df_encoded["income_per_age"] = df_encoded["income"] / (df_encoded["age"] + 1)
    feature_cols_d = feature_cols_c + ["age_income", "income_per_age"]
    X_d = df_encoded[feature_cols_d].values.astype(float)
    X_d[:, :2] = StandardScaler().fit_transform(X_d[:, :2])  # scale numeric
    X_d[:, -2:] = StandardScaler().fit_transform(X_d[:, -2:])  # scale interactions
    X_tr, X_te, y_tr, y_te = train_test_split(X_d, y, test_size=0.2, random_state=42, stratify=y)
    m = RandomForestClassifier(random_state=42, n_estimators=100)
    m.fit(X_tr, y_tr)
    acc_d = accuracy_score(y_te, m.predict(X_te))

    # --- Results ---
    print("=== Feature Engineering Stage Comparison ===")
    print(f"(a) Raw:                    {acc_a:.4f}  ({X_a.shape[1]} features)")
    print(f"(b) Scaled:                 {acc_b:.4f}  ({X_b.shape[1]} features)")
    print(f"(c) Scaled + Encoded:       {acc_c:.4f}  ({X_c.shape[1]} features)")
    print(f"(d) Scaled+Encoded+Inter:   {acc_d:.4f}  ({X_d.shape[1]} features)")
    print()
    print("Key takeaway: encoding categoricals and adding interactions")
    print("can improve accuracy, but diminishing returns at each stage.")
