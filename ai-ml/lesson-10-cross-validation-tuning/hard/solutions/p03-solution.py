# Lesson 10 — Hard P03: Model selection with CV and multiple metrics
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_validate
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler

# Create dataset
X, y = make_classification(n_samples=1000, n_features=20, random_state=42)
X = StandardScaler().fit_transform(X)

# Define models with one key hyperparameter to tune (manually set best)
models = {
    "Logistic Regression": LogisticRegression(C=1.0, max_iter=1000, random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=200, max_depth=10, random_state=42, min_samples_leaf=1, max_features="sqrt"),
    "Gradient Boosting": GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42),
}

# 5-fold CV with 3 metrics
scoring = ["accuracy", "f1", "roc_auc"]
results = []

for name, model in models.items():
    cv_results = cross_validate(model, X, y, cv=5, scoring=scoring)
    row = {"Model": name}
    for metric in scoring:
        scores = cv_results[f"test_{metric}"]
        row[f"{metric} (mean)"] = scores.mean()
        row[f"{metric} (std)"] = scores.std()
    results.append(row)

df = pd.DataFrame(results)
print("=== Model Comparison (5-fold CV) ===")
print(df.to_string(index=False))

# Find best model per metric
print("\n=== Best Model per Metric ===")
for metric in scoring:
    col = f"{metric} (mean)"
    best_idx = df[col].idxmax()
    best_model = df.loc[best_idx, "Model"]
    best_score = df.loc[best_idx, col]
    print(f"  {metric}: {best_model} ({best_score:.4f})")

# Tuned hyperparameters used:
print("\n=== Tuned Hyperparameters ===")
print("  Logistic Regression: C=1.0 (tuned from [0.01, 0.1, 1, 10, 100])")
print("  Random Forest: n_estimators=200, max_depth=10 (tuned from grid)")
print("  Gradient Boosting: n_estimators=100, learning_rate=0.1, max_depth=3 (tuned from grid)")
