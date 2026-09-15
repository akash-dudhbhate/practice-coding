"""
sklearn LogisticRegression on make_classification
==================================================
Train logistic regression on a binary classification dataset.
Print accuracy, precision, recall, and F1 score.
"""

from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score, precision_score,
                             recall_score, f1_score)


if __name__ == "__main__":
    # Generate binary classification data
    X, y = make_classification(
        n_samples=500, n_features=10, n_informative=5,
        n_redundant=2, n_classes=2, random_state=42
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train logistic regression
    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print("=== Logistic Regression Results ===\n")
    print(f"Accuracy:  {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")
    print(f"F1 Score:  {f1:.4f}")

    print("\n=== Interpretation ===")
    print(f"Accuracy:  {accuracy*100:.1f}% of predictions are correct.")
    print(f"Precision: {precision*100:.1f}% of predicted positives are true positives.")
    print(f"Recall:    {recall*100:.1f}% of actual positives were correctly identified.")
    print(f"F1 Score:  Harmonic mean of precision and recall.")
