"""Level 04 Supervised — Hard P01 Solution"""

import numpy as np
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.datasets import make_regression

def solve():
    X, y = make_regression(n_samples=100, n_features=10, noise=10, random_state=42)
    lr = LinearRegression().fit(X, y)
    lasso = Lasso(alpha=1.0).fit(X, y)
    ridge = Ridge(alpha=1.0).fit(X, y)
    print("Coefficients comparison:")
    print(f"{'Feature':<10} {'Linear':<12} {'Lasso':<12} {'Ridge':<12}")
    for i in range(X.shape[1]):
        print(f"{i:<10} {lr.coef_[i]:<12.4f} {lasso.coef_[i]:<12.4f} {ridge.coef_[i]:<12.4f}")
    return lr.coef_, lasso.coef_, ridge.coef_

if __name__ == "__main__":
    solve()