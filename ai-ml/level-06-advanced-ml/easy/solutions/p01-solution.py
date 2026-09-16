"""Level 06 Advanced Ml — Easy P01 Solution"""

import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def solve():
    np.random.seed(42)
    X = np.random.rand(50, 1) * 10
    y = 3 * X.flatten()**2 + 2 * X.flatten() + np.random.randn(50) * 10
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # Without polynomial
    lr = LinearRegression().fit(X_train, y_train)
    score_linear = lr.score(X_test, y_test)
    # With polynomial
    poly = PolynomialFeatures(degree=2)
    X_train_poly = poly.fit_transform(X_train)
    X_test_poly = poly.transform(X_test)
    lr_poly = LinearRegression().fit(X_train_poly, y_train)
    score_poly = lr_poly.score(X_test_poly, y_test)
    print(f"Linear R²: {score_linear:.4f}")
    print(f"Polynomial R²: {score_poly:.4f}")
    return score_linear, score_poly

if __name__ == "__main__":
    solve()