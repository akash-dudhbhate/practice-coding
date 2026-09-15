"""
Metric Comparison: 3 Models on Same Dataset
===========================================
Train Logistic Regression, Decision Tree, and Random Forest on the same data.
Print accuracy, precision, recall, F1, and AUC in a comparison DataFrame.
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                             f1_score, roc_auc_score)


if __name__ == "__main__":
    X, y = make_classification(
        n_samples=1000, n_features=15, n_informative=8,
        n_redundant=3, random_state=42
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
        "Decision Tree": DecisionTreeClassifier(max_depth=5, random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    }

    results = []
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        y_proba = model.predict_proba(X_test)[:, 1]

        results.append({
            "Model": name,
            "Accuracy": accuracy_score(y_test, y_pred),
            "Precision": precision_score(y_test, y_pred),
            "Recall": recall_score(y_test, y_pred),
            "F1": f1_score(y_test, y_pred),
            "AUC": roc_auc_score(y_test, y_proba),
        })

    df = pd.DataFrame(results)
    df = df.set_index("Model")

    print("=== Model Comparison Table ===\n")
    print(df.to_string(float_format="{:.4f}".format))

    # Best model per metric
    print("\n=== Best Model per Metric ===")
    for col in df.columns:
        best = df[col].idxmax()
        print(f"  {col:12s}: {best} ({df.loc[best, col]:.4f})")

    print("\n=== Interpretation ===")
    print("Logistic Regression: linear model, good baseline, interpretable.")
    print("Decision Tree: captures non-linear patterns, but can overfit.")
    print("Random Forest: ensemble, typically best overall on tabular data.")
