"""Level 06 Advanced Ml — Medium P01 Solution"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE

def solve():
    X, y = make_classification(n_samples=1000, n_features=10, weights=[0.95, 0.05], random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # Without SMOTE
    model = LogisticRegression(random_state=42).fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("Without SMOTE:")
    print(classification_report(y_test, y_pred))
    # With SMOTE
    smote = SMOTE(random_state=42)
    X_train_res, y_train_res = smote.fit_resample(X_train, y_train)
    model = LogisticRegression(random_state=42).fit(X_train_res, y_train_res)
    y_pred = model.predict(X_test)
    print("With SMOTE:")
    print(classification_report(y_test, y_pred))
    return y_pred

if __name__ == "__main__":
    solve()