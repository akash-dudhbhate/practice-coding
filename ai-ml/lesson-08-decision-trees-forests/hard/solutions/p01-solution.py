"""
Classification Pipeline: Breast Cancer
=====================================
Compare decision tree, random forest, and gradient boosting on Breast Cancer.
Print accuracy, precision, recall, F1 in a comparison table.
"""

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import (accuracy_score, precision_score,
                             recall_score, f1_score)


if __name__ == "__main__":
    data = load_breast_cancer()
    X, y = data.data, data.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)

    models = {
        "Decision Tree": DecisionTreeClassifier(max_depth=5, random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
        "Gradient Boosting": GradientBoostingClassifier(random_state=42),
    }

    print("=== Model Comparison: Breast Cancer Dataset ===\n")
    print(f"{'Model':<20} {'Accuracy':<12} {'Precision':<12} {'Recall':<12} {'F1':<12}")
    print("-" * 68)

    results = {}
    for name, model in models.items():
        model.fit(X_train_s, y_train)
        y_pred = model.predict(X_test_s)

        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred)
        rec = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)

        results[name] = {"accuracy": acc, "precision": prec, "recall": rec, "f1": f1}

        print(f"{name:<20} {acc:<12.4f} {prec:<12.4f} {rec:<12.4f} {f1:<12.4f}")

    # Find best model
    best_model = max(results, key=lambda k: results[k]["f1"])
    print(f"\nBest model (by F1): {best_model} (F1={results[best_model]['f1']:.4f})")

    print("\n=== Interpretation ===")
    print("Decision Tree: single tree, prone to overfitting but interpretable.")
    print("Random Forest: ensemble of trees, reduces variance, robust.")
    print("Gradient Boosting: sequential ensemble, often best performance.")
    print("Gradient boosting typically wins on structured/tabular data.")
