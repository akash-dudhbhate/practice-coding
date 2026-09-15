"""
Multiclass Logistic Regression on Iris
======================================
Train multiclass logistic regression on the Iris dataset (3 classes).
Print accuracy, confusion matrix, and classification report.
"""

from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score, confusion_matrix,
                             classification_report)


if __name__ == "__main__":
    # Load Iris dataset
    iris = load_iris()
    X, y = iris.data, iris.target
    class_names = iris.target_names

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Train multiclass logistic regression (multinomial)
    model = LogisticRegression(
        max_iter=1000, multi_class="multinomial", solver="lbfgs",
        random_state=42
    )
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Results
    print("=== Multiclass Logistic Regression on Iris ===\n")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}\n")

    print("Confusion Matrix:")
    cm = confusion_matrix(y_test, y_pred)
    print(f"  {'':>15} {'setosa':>10} {'versicolor':>12} {'virginica':>10}")
    for i, name in enumerate(class_names):
        print(f"  {name:>15} {cm[i, 0]:>10} {cm[i, 1]:>12} {cm[i, 2]:>10}")

    print(f"\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=class_names))

    print("=== Interpretation ===")
    print("Each class has its own set of coefficients (one-vs-rest or multinomial).")
    print("Precision per class: how many predicted as that class were correct.")
    print("Recall per class: how many actual samples of that class were found.")
