# Lesson 10 — Medium P03: Pipeline with StandardScaler + LogisticRegression, tune C
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Create synthetic dataset
X, y = make_classification(n_samples=1000, n_features=20, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build pipeline: scaling is INSIDE the pipeline so it's applied within CV folds (no leakage)
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", LogisticRegression(max_iter=1000, random_state=42)),
], memory="cache_dir")

# Tune C parameter using GridSearchCV
param_grid = {"clf__C": [0.01, 0.1, 1, 10, 100]}
grid = GridSearchCV(pipeline, param_grid, cv=5, scoring="accuracy")
grid.fit(X_train, y_train)

print("Best C:", grid.best_params_["clf__C"])
print("Best CV accuracy:", grid.best_score_)
print("\nAll results:")
for mean, params in zip(grid.cv_results_["mean_test_score"], grid.cv_results_["params"]):
    print(f"  C={params['clf__C']}: accuracy={mean:.4f}")

# Evaluate on test set
test_score = grid.score(X_test, y_test)
print(f"\nTest accuracy with best C: {test_score:.4f}")

# Verify no data leakage: scaling is inside CV, so each fold scales only on its training data
print("\nNo data leakage: StandardScaler is inside the Pipeline, so GridSearchCV")
print("applies scaling within each CV fold (fit on train fold, transform on val fold).")
