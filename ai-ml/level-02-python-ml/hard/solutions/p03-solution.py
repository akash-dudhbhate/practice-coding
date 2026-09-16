"""Level 02 — Python for ML — Hard P03 Solution"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def compare_splits():
    X, y = make_classification(n_samples=1000, n_features=10, n_informative=5,
                               weights=[0.95, 0.05], flip_y=0.0, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print("Without stratify:")
    print(f"  Train: {np.bincount(y_train)}")
    print(f"  Test:  {np.bincount(y_test)}")
    X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y)
    print("With stratify:")
    print(f"  Train: {np.bincount(y_train_s)}")
    print(f"  Test:  {np.bincount(y_test_s)}")
    model = RandomForestClassifier(random_state=42).fit(X_train, y_train)
    model_s = RandomForestClassifier(random_state=42).fit(X_train_s, y_train_s)
    acc_a = model.score(X_test, y_test)
    acc_b = model_s.score(X_test_s, y_test_s)
    print(f"Without stratify test accuracy: {acc_a:.4f}")
    print(f"With stratify test accuracy: {acc_b:.4f}")
    return acc_a, acc_b

if __name__ == "__main__":
    compare_splits()
