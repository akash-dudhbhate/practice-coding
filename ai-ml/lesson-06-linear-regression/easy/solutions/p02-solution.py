"""
sklearn LinearRegression on make_regression
============================================
Use scikit-learn's LinearRegression on a synthetic regression dataset.
Print coefficient, intercept, and R^2 score.
"""

from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


if __name__ == "__main__":
    # Generate synthetic regression data
    X, y = make_regression(
        n_samples=200, n_features=1, noise=15, random_state=42
    )

    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Fit the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)

    # Print results
    print(f"Coefficient(s): {model.coef_}")
    print(f"Intercept:      {model.intercept_:.4f}")
    print(f"R^2 (train):    {model.score(X_train, y_train):.4f}")
    print(f"R^2 (test):     {r2_score(y_test, y_pred):.4f}")
    print(f"MSE (test):     {mean_squared_error(y_test, y_pred):.4f}")
