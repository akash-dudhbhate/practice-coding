"""
Complete Feature Engineering Pipeline (Titanic)
================================================
End-to-end pipeline on the Titanic dataset:
  1. Handle missing values
  2. Encode categoricals
  3. Scale numerical features
  4. Create interaction features
  5. Select top 10 features
Train a model with engineered features vs raw features and compare accuracy.
"""

import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def load_and_clean(df):
    """Handle missing values."""
    df = df.copy()
    # Numeric: fill with median
    df["age"] = df["age"].fillna(df["age"].median())
    df["fare"] = df["fare"].fillna(df["fare"].median())
    # Categorical: fill with mode
    df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])
    df["embark_town"] = df["embark_town"].fillna(df["embark_town"].mode()[0])
    # Drop columns with too many missing or non-predictive
    df = df.drop(columns=["deck"], errors="ignore")
    return df


def engineer_features(df):
    """Create new features and encode categoricals."""
    df = df.copy()
    # Family features
    df["family_size"] = df["sibsp"] + df["parch"] + 1
    df["is_alone"] = (df["family_size"] == 1).astype(int)
    # Title from name
    df["title"] = df["who"]  # use 'who' as a simple proxy
    # Interaction: class * age
    df["class_age"] = df["pclass"] * df["age"]
    # Interaction: fare per family member
    df["fare_per_person"] = df["fare"] / df["family_size"]
    # One-hot encode categoricals
    categorical_cols = ["sex", "embarked", "class", "who", "embark_town", "alone"]
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    # Drop non-numeric / non-useful columns
    drop_cols = ["alive", "adult_male", "title"]
    df = df.drop(columns=drop_cols, errors="ignore")
    return df


if __name__ == "__main__":
    # Load Titanic dataset from seaborn
    titanic = sns.load_dataset("titanic")

    # --- RAW features (minimal preprocessing) ---
    raw = titanic[["pclass", "age", "sibsp", "parch", "fare", "survived"]].copy()
    raw["age"] = raw["age"].fillna(raw["age"].median())
    raw["fare"] = raw["fare"].fillna(raw["fare"].median())
    raw["sex_male"] = (titanic["sex"] == "male").astype(int)

    X_raw = raw.drop(columns=["survived"])
    y = raw["survived"]

    X_train_raw, X_test_raw, y_train, y_test = train_test_split(
        X_raw, y, test_size=0.2, random_state=42, stratify=y
    )
    model_raw = RandomForestClassifier(random_state=42)
    model_raw.fit(X_train_raw, y_train)
    acc_raw = accuracy_score(y_test, model_raw.predict(X_test_raw))

    # --- ENGINEERED features ---
    cleaned = load_and_clean(titanic)
    engineered = engineer_features(cleaned)

    # Keep only numeric columns
    engineered = engineered.select_dtypes(include=[np.number])
    y_eng = engineered["survived"]
    X_eng = engineered.drop(columns=["survived"])

    # Scale numerical features
    scaler = StandardScaler()
    X_eng_scaled = scaler.fit_transform(X_eng)

    # Select top 10 features
    selector = SelectKBest(f_classif, k=10)
    X_eng_selected = selector.fit_transform(X_eng_scaled, y_eng)

    # Get selected feature names
    selected_mask = selector.get_support()
    selected_features = X_eng.columns[selected_mask].tolist()
    print(f"Top 10 selected features: {selected_features}\n")

    X_train_eng, X_test_eng, y_train_eng, y_test_eng = train_test_split(
        X_eng_selected, y_eng, test_size=0.2, random_state=42, stratify=y_eng
    )
    model_eng = RandomForestClassifier(random_state=42)
    model_eng.fit(X_train_eng, y_train_eng)
    acc_eng = accuracy_score(y_test_eng, model_eng.predict(X_test_eng))

    print("=== Accuracy Comparison ===")
    print(f"Raw features ({X_raw.shape[1]} features):      {acc_raw:.4f}")
    print(f"Engineered features (top 10 of {X_eng.shape[1]}): {acc_eng:.4f}")
    print(f"Improvement: {acc_eng - acc_raw:+.4f}")
