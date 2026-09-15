"""
Complete Regression Pipeline: California Housing
=================================================
Load the California Housing dataset, scale features, train a linear regression
model, evaluate with MSE and R^2, and plot actual vs predicted values.
"""

import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np


if __name__ == "__main__":
    # Load California Housing dataset
    data = fetch_california_housing()
    X, y = data.data, data.target
    feature_names = data.feature_names

    print(f"Dataset shape:  {X.shape}")
    print(f"Target:         Median house value (in 100,000s)")
    print(f"Features:       {feature_names}\n")

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Train
    model = LinearRegression()
    model.fit(X_train_scaled, y_train)

    # Predict
    y_pred = model.predict(X_test_scaled)

    # Evaluate
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    print("=== Model Evaluation ===")
    print(f"MSE:  {mse:.4f}")
    print(f"RMSE: {rmse:.4f}")
    print(f"R^2:  {r2:.4f}\n")

    print("Coefficients (scaled features):")
    for name, coef in zip(feature_names, model.coef_):
        print(f"  {name:12s}: {coef:+.4f}")

    # Plot actual vs predicted
    plt.figure(figsize=(7, 7))
    plt.scatter(y_test, y_pred, alpha=0.3, s=10, color="steelblue")
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()],
             "r--", lw=2, label="Perfect prediction")
    plt.xlabel("Actual Values")
    plt.ylabel("Predicted Values")
    plt.title("California Housing: Actual vs Predicted")
    plt.legend()
    plt.tight_layout()
    plt.savefig("actual_vs_predicted.png", dpi=150)
    plt.show()
    print("\nPlot saved to actual_vs_predicted.png")
