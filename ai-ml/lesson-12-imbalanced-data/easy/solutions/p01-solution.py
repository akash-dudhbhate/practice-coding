"""
Imbalanced Dataset: High Accuracy, Low Recall
==============================================
Create a 95:5 imbalanced dataset, train logistic regression, and show that
accuracy is deceptively high while recall for the minority class is near 0.
"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, recall_score

np.random.seed(42)


if __name__ == "__main__":
    # Create imbalanced dataset: 95% class 0, 5% class 1
    X, y = make_classification(
        n_samples=1000,
        n_features=10,
        n_informative=5,
        n_redundant=2,
        weights=[0.95, 0.05],
        flip_y=0.0,
        random_state=42,
    )

    print(f"Class distribution: {dict(zip(*np.unique(y, return_counts=True)))}")
    print()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    model = LogisticRegression(random_state=42, max_iter=1000)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print("=== Results ===")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print(f"Recall (minority class 1): {recall_score(y_test, y_pred, pos_label=1):.4f}")
    print()

    print("=== Classification Report ===")
    print(classification_report(y_test, y_pred))
    print()
    print("Key takeaway: Accuracy looks great (~95%) but the model")
    print("is just predicting the majority class. Recall for the")
    print("minority class is near 0 -- the model misses almost all positives.")
