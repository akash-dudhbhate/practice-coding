"""
House Price Predictor (Multiple Linear Regression)
===================================================
Create a synthetic house dataset with features: size (sqft), bedrooms, age (years).
Train multiple linear regression and interpret coefficients.
"""

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


def generate_house_data(n=500, seed=42):
    """Generate synthetic house data.

    price = 50*size + 20000*bedrooms - 3000*age + noise
    """
    rng = np.random.RandomState(seed)
    size = rng.randint(800, 4000, n)
    bedrooms = rng.randint(1, 6, n)
    age = rng.randint(0, 50, n)

    # Base price + feature contributions + noise
    price = 50 * size + 20000 * bedrooms - 3000 * age + rng.randn(n) * 5000 + 50000

    X = np.column_stack([size, bedrooms, age])
    y = price
    return X, y


if __name__ == "__main__":
    X, y = generate_house_data()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    feature_names = ["Size (sqft)", "Bedrooms", "Age (years)"]

    print("=== House Price Predictor ===\n")
    print(f"Intercept (base price): ${model.intercept_:,.2f}\n")
    print("Coefficients (feature impact on price):")
    for name, coef in zip(feature_names, model.coef_):
        print(f"  {name:15s}: ${coef:,.2f}")

    print(f"\nR^2 (test):  {r2_score(y_test, y_pred):.4f}")
    print(f"MSE (test):  {mean_squared_error(y_test, y_pred):,.2f}")
    print(f"RMSE (test): {np.sqrt(mean_squared_error(y_test, y_pred)):,.2f}")

    # Interpretation
    print("\n=== Interpretation ===")
    print("Each additional sqft adds ~$50 to the price.")
    print("Each additional bedroom adds ~$20,000 to the price.")
    print("Each additional year of age reduces price by ~$3,000.")
