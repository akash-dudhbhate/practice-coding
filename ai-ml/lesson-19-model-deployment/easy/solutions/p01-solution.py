"""
Train simple model, save with joblib, load and verify
======================================================
Train a model on the Iris dataset, save it with joblib.dump,
load it back, and verify predictions match.
"""

import joblib
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier


if __name__ == "__main__":
    # Load Iris
    iris = load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Scale features
    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)

    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_s, y_train)

    # Predictions BEFORE saving
    pred_before = model.predict(X_test_s)
    print("--- Before Saving ---")
    print(f"Predictions: {pred_before}")
    print(f"Accuracy:    {model.score(X_test_s, y_test):.4f}")

    # Save model and scaler with joblib
    joblib.dump(model, "iris_model.joblib")
    joblib.dump(scaler, "iris_scaler.joblib")
    print(f"\nModel saved to iris_model.joblib")
    print(f"Scaler saved to iris_scaler.joblib")

    # Load model and scaler back
    loaded_model = joblib.load("iris_model.joblib")
    loaded_scaler = joblib.load("iris_scaler.joblib")
    print(f"\nModel and scaler loaded back.")

    # Predictions AFTER loading
    X_test_s_loaded = loaded_scaler.transform(X_test)
    pred_after = loaded_model.predict(X_test_s_loaded)
    print(f"\n--- After Loading ---")
    print(f"Predictions: {pred_after}")
    print(f"Accuracy:    {loaded_model.score(X_test_s_loaded, y_test):.4f}")

    # Verify they match
    match = np.array_equal(pred_before, pred_after)
    print(f"\n--- Verification ---")
    print(f"Predictions match: {match}")
    print(f"All predictions identical: {match}")
