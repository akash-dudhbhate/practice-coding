"""Level 06 Advanced Ml — Hard P03 Solution"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from imblearn.ensemble import BalancedRandomForestClassifier

def solve():
    X, y = make_classification(n_samples=2000, n_features=10, weights=[0.98, 0.02], random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # Regular RF
    rf = RandomForestClassifier(random_state=42).fit(X_train, y_train)
    y_pred = rf.predict(X_test)
    print("Regular RandomForest:")
    print(classification_report(y_test, y_pred))
    # Balanced RF
    brf = BalancedRandomForestClassifier(random_state=42).fit(X_train, y_train)
    y_pred = brf.predict(X_test)
    print("Balanced RandomForest:")
    print(classification_report(y_test, y_pred))
    return y_pred

if __name__ == "__main__":
    solve()