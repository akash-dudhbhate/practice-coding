"""Level 04 — Supervised Learning — Hard P01 Solution"""

import numpy as np
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.datasets import make_regression

def compare_regularization():
    X, y = make_regression(n_samples=100, n_features=10, noise=10, random_state=42)
    lr = LinearRegression().fit(X, y)
    lasso = Lasso(alpha=1.0).fit(X, y)
    ridge = Ridge(alpha=1.0).fit(X, y)
    return lr.coef_, lasso.coef_, ridge.coef_

if __name__ == "__main__":
    lr_c, la_c, ri_c = compare_regularization()
    print(f"{'Feature':<10} {'Linear':<12} {'Lasso':<12} {'Ridge':<12}")
    for i in range(10):
        print(f"{i:<10} {lr_c[i]:<12.4f} {la_c[i]:<12.4f} {ri_c[i]:<12.4f}")
