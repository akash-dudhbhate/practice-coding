# Lesson 10 — Hard P01: Complete tuning pipeline
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report

# Load real dataset
data = load_breast_cancer()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create pipeline (scaler + model)
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", RandomForestClassifier(random_state=42, min_samples_leaf=1, max_features="sqrt")),
], memory="cache_dir")

# GridSearchCV with 3+ hyperparameters
param_grid = {
    "clf__n_estimators": [50, 100, 200],
    "clf__max_depth": [3, 5, 10, None],
    "clf__min_samples_split": [2, 5],
}

grid = GridSearchCV(pipeline, param_grid, cv=5, scoring="accuracy", n_jobs=-1)
grid.fit(X_train, y_train)

print("Best parameters:", grid.best_params_)
print("Best CV accuracy:", grid.best_score_)

# Evaluate on held-out test set
y_pred = grid.predict(X_test)
test_acc = accuracy_score(y_test, y_pred)
print(f"\nTest accuracy (tuned): {test_acc:.4f}")
print("\nClassification report:")
print(classification_report(y_test, y_pred))

# Compare with default hyperparameters
default_pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", RandomForestClassifier(random_state=42, min_samples_leaf=1, max_features="sqrt")),
], memory="cache_dir")
default_pipeline.fit(X_train, y_train)
default_pred = default_pipeline.predict(X_test)
default_acc = accuracy_score(y_test, default_pred)
print(f"Test accuracy (default): {default_acc:.4f}")
print(f"Improvement: {(test_acc - default_acc):.4f}")
