"""
5-Fold Cross-Validation on Random Forest with Iris
==================================================
Perform 5-fold CV on a random forest with the Iris dataset.
Print mean/std accuracy and compare with a single train/test split.
"""

import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, train_test_split


if __name__ == "__main__":
    iris = load_iris()
    X, y = iris.data, iris.target

    rf = RandomForestClassifier(n_estimators=100, random_state=42)

    # --- 5-fold cross-validation ---
    cv_scores = cross_val_score(rf, X, y, cv=5, scoring="accuracy")

    print("=== 5-Fold Cross-Validation ===\n")
    print(f"Fold accuracies: {cv_scores}")
    print(f"Mean accuracy:   {cv_scores.mean():.4f}")
    print(f"Std accuracy:    {cv_scores.std():.4f}")

    # --- Single train/test split ---
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    rf_split = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_split.fit(X_train, y_train)
    split_acc = rf_split.score(X_test, y_test)

    print(f"\n=== Single Train/Test Split ===\n")
    print(f"Single split accuracy: {split_acc:.4f}")

    print(f"\n=== Comparison ===\n")
    print(f"CV mean:    {cv_scores.mean():.4f} +/- {cv_scores.std():.4f}")
    print(f"Single split: {split_acc:.4f}")
    print("\nCV gives a more reliable estimate by averaging across 5 different splits.")
    print("The std shows how much accuracy varies between folds.")
    print("A single split may be lucky or unlucky; CV reduces this variance.")
