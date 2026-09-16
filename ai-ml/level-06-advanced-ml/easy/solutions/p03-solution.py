"""Level 06 Advanced Ml — Easy P03 Solution"""

import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

def solve():
    X, y = make_classification(n_samples=200, n_features=2, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # No scaling
    model = LogisticRegression(random_state=42).fit(X_train, y_train)
    score_none = model.score(X_test, y_test)
    # Standardization
    scaler = StandardScaler()
    X_train_std = scaler.fit_transform(X_train)
    X_test_std = scaler.transform(X_test)
    model = LogisticRegression(random_state=42).fit(X_train_std, y_train)
    score_std = model.score(X_test_std, y_test)
    # Normalization
    scaler = MinMaxScaler()
    X_train_norm = scaler.fit_transform(X_train)
    X_test_norm = scaler.transform(X_test)
    model = LogisticRegression(random_state=42).fit(X_train_norm, y_train)
    score_norm = model.score(X_test_norm, y_test)
    print(f"No scaling: {score_none:.4f}")
    print(f"Standardization: {score_std:.4f}")
    print(f"Normalization: {score_norm:.4f}")
    return score_none, score_std, score_norm

if __name__ == "__main__":
    solve()