"""
SVM with Linear Kernel on make_classification
===============================================
Train a linear SVM on a synthetic classification dataset. Print accuracy
and the number of support vectors used by the model.
"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

np.random.seed(42)


if __name__ == "__main__":
    X, y = make_classification(n_samples=500, n_features=10, n_informative=5, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    # Scale features (important for SVM)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Train SVM with linear kernel
    svm = SVC(kernel="linear", random_state=42)
    svm.fit(X_train_scaled, y_train)

    y_pred = svm.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred)

    print("=== SVM (Linear Kernel) ===")
    print(f"Accuracy:          {acc:.4f}")
    print(f"Number of support vectors: {svm.n_support_}")
    print(f"Total support vectors:     {sum(svm.n_support_)}")
    print(f"Support vectors per class: {dict(enumerate(svm.n_support_))}")
    print()
    print("Key takeaway: Support vectors are the data points that lie on or")
    print("near the decision boundary. Fewer support vectors = simpler model.")
