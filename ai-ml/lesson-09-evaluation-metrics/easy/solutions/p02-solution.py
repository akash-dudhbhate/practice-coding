"""
Train Logistic Regression and Print Classification Report
=========================================================
Train on make_classification, print sklearn's classification_report,
and interpret each metric.
"""

from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


if __name__ == "__main__":
    X, y = make_classification(
        n_samples=500, n_features=10, n_informative=5,
        n_redundant=2, weights=[0.7], random_state=42
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print("=== Classification Report ===\n")
    print(classification_report(y_test, y_pred, target_names=["Class 0", "Class 1"]))

    print("=== Interpretation ===")
    print("Precision (per class): Of all predicted as this class, how many were correct?")
    print("Recall (per class): Of all actual instances of this class, how many were found?")
    print("F1-score: Harmonic mean of precision and recall (balances both).")
    print("Support: Number of actual occurrences of each class in the test set.")
    print("Macro avg: Unweighted mean of metrics across classes.")
    print("Weighted avg: Mean weighted by support (class frequency).")
