"""
Class Weight = 'balanced' on Imbalanced Data
=============================================
Train logistic regression with class_weight='balanced' on the same 95:5
dataset. Compare recall with and without class weights.
"""

import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, recall_score

np.random.seed(42)


if __name__ == "__main__":
    # Same 95:5 imbalanced dataset
    X, y = make_classification(
        n_samples=1000,
        n_features=10,
        n_informative=5,
        n_redundant=2,
        weights=[0.95, 0.05],
        flip_y=0.0,
        random_state=42,
    )

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    # --- Without class weights ---
    model_no_weight = LogisticRegression(random_state=42, max_iter=1000)
    model_no_weight.fit(X_train, y_train)
    y_pred_no = model_no_weight.predict(X_test)

    print("=== WITHOUT class_weight='balanced' ===")
    print(f"Accuracy: {accuracy_score(y_test, y_pred_no):.4f}")
    print(f"Recall (class 1): {recall_score(y_test, y_pred_no, pos_label=1):.4f}")
    print(classification_report(y_test, y_pred_no))

    # --- With class weights ---
    model_weighted = LogisticRegression(random_state=42, max_iter=1000, class_weight="balanced")
    model_weighted.fit(X_train, y_train)
    y_pred_w = model_weighted.predict(X_test)

    print("=== WITH class_weight='balanced' ===")
    print(f"Accuracy: {accuracy_score(y_test, y_pred_w):.4f}")
    print(f"Recall (class 1): {recall_score(y_test, y_pred_w, pos_label=1):.4f}")
    print(classification_report(y_test, y_pred_w))

    print("=== Comparison ===")
    print(f"Recall without weights: {recall_score(y_test, y_pred_no, pos_label=1):.4f}")
    print(f"Recall with weights:    {recall_score(y_test, y_pred_w, pos_label=1):.4f}")
    print()
    print("Key takeaway: class_weight='balanced' increases recall for the")
    print("minority class by penalizing misclassifications of that class more.")
    print("Accuracy may drop, but the model now actually detects positives.")
