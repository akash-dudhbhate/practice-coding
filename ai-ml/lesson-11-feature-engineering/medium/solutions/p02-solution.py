"""
House Dataset Feature Engineering
=================================
Engineer new features from a house dataset (sqft, bedrooms, price):
  - price_per_sqft
  - total_rooms (bedrooms + bathrooms)
  - bedrooms_per_sqft
Train a model with and without engineered features and compare R^2.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score

np.random.seed(42)


if __name__ == "__main__":
    # Generate synthetic house dataset
    n = 200
    sqft = np.random.randint(800, 4000, n)
    bedrooms = np.random.randint(1, 6, n)
    bathrooms = np.random.randint(1, 4, n)
    # Price is roughly correlated with sqft and rooms
    price = sqft * 150 + bedrooms * 10000 + bathrooms * 5000 + np.random.normal(0, 20000, n)

    df = pd.DataFrame({"sqft": sqft, "bedrooms": bedrooms, "bathrooms": bathrooms, "price": price})

    print("=== Raw dataset ===")
    print(df.head())
    print()

    # --- Model WITHOUT engineered features ---
    X_raw = df[["sqft", "bedrooms", "bathrooms"]]
    y = df["price"]

    X_train_raw, X_test_raw, y_train, y_test = train_test_split(X_raw, y, test_size=0.2, random_state=42)
    model_raw = RandomForestRegressor(random_state=42)
    model_raw.fit(X_train_raw, y_train)
    r2_raw = r2_score(y_test, model_raw.predict(X_test_raw))

    # --- Engineer new features ---
    df["price_per_sqft"] = df["price"] / df["sqft"]
    df["total_rooms"] = df["bedrooms"] + df["bathrooms"]
    df["bedrooms_per_sqft"] = df["bedrooms"] / df["sqft"]

    print("=== After feature engineering ===")
    print(df[["sqft", "bedrooms", "bathrooms", "price_per_sqft", "total_rooms", "bedrooms_per_sqft"]].head())
    print()

    # --- Model WITH engineered features ---
    # NOTE: exclude 'price' and 'price_per_sqft' (target leakage) from features
    X_eng = df[["sqft", "bedrooms", "bathrooms", "total_rooms", "bedrooms_per_sqft"]]
    # Use price_per_sqft only if we wouldn't know price at prediction time
    # Here we exclude it to avoid data leakage

    X_train_eng, X_test_eng, y_train_eng, y_test_eng = train_test_split(
        X_eng, y, test_size=0.2, random_state=42
    )
    model_eng = RandomForestRegressor(random_state=42)
    model_eng.fit(X_train_eng, y_train_eng)
    r2_eng = r2_score(y_test_eng, model_eng.predict(X_test_eng))

    print("=== R^2 Comparison ===")
    print(f"Without engineered features: {r2_raw:.4f}")
    print(f"With engineered features:    {r2_eng:.4f}")
    print(f"Improvement:                  {r2_eng - r2_raw:+.4f}")
