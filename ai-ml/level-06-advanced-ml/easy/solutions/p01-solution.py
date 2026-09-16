"""Level 06 — Advanced ML — Easy P01 Solution"""

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression

def compare_linear_poly():
    X, y = make_regression(n_samples=200, n_features=1, noise=30, random_state=42)
    # Make it nonlinear: square the relationship
    y = y ** 2 / 100
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Linear model
    lr = LinearRegression().fit(X_train, y_train)
    r2_linear = lr.score(X_test, y_test)

    # Polynomial (degree 2)
    poly = PolynomialFeatures(degree=2, include_bias=False)
    X_train_poly = poly.fit_transform(X_train)
    X_test_poly = poly.transform(X_test)
    lr_poly = LinearRegression().fit(X_train_poly, y_train)
    r2_poly = lr_poly.score(X_test_poly, y_test)

    return r2_linear, r2_poly

if __name__ == "__main__":
    l, p = compare_linear_poly()
    print(f"Linear R²: {l:.4f}")
    print(f"Poly R²:   {p:.4f}")
