"""
Complete model serving with sklearn Pipeline
=============================================
Train on a real dataset, save model AND scaler as a sklearn Pipeline.
FastAPI app that takes raw input -> scales -> predicts. Test with 3 samples.
"""

import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel, Field
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline


# --- Train and save pipeline ---
def train_and_save_pipeline():
    """Train a Pipeline (scaler + model) and save it."""
    iris = load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", RandomForestClassifier(n_estimators=100, random_state=42)),
    ])
    pipeline.fit(X_train, y_train)
    acc = pipeline.score(X_test, y_test)
    print(f"Pipeline trained. Test accuracy: {acc:.4f}")
    joblib.dump(pipeline, "iris_pipeline.joblib")
    return pipeline


# --- Pydantic models ---
class IrisFeatures(BaseModel):
    sepal_length: float = Field(..., description="Sepal length in cm")
    sepal_width: float = Field(..., description="Sepal width in cm")
    petal_length: float = Field(..., description="Petal length in cm")
    petal_width: float = Field(..., description="Petal width in cm")


class PredictionResponse(BaseModel):
    prediction: int
    class_name: str
    probabilities: dict[str, float]


# --- FastAPI App ---
app = FastAPI(title="Iris Pipeline API", version="1.0.0")

try:
    pipeline = joblib.load("iris_pipeline.joblib")
except FileNotFoundError:
    pipeline = train_and_save_pipeline()

iris_data = load_iris()


@app.get("/health")
def health():
    return {"status": "healthy", "model_loaded": True}


@app.post("/predict", response_model=PredictionResponse)
def predict(features: IrisFeatures):
    """Predict from raw input — pipeline handles scaling internally."""
    input_array = np.array([[
        features.sepal_length,
        features.sepal_width,
        features.petal_length,
        features.petal_width,
    ]])

    prediction = int(pipeline.predict(input_array)[0])
    class_name = iris_data.target_names[prediction]

    # Get probabilities
    probs = pipeline.predict_proba(input_array)[0]
    probabilities = {
        iris_data.target_names[i]: float(probs[i])
        for i in range(len(iris_data.target_names))
    }

    return PredictionResponse(
        prediction=prediction,
        class_name=class_name,
        probabilities=probabilities,
    )


# --- Test with 3 samples ---
def test_app():
    from fastapi.testclient import TestClient
    client = TestClient(app)

    test_samples = [
        {"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2},  # setosa
        {"sepal_length": 6.7, "sepal_width": 3.0, "petal_length": 5.0, "petal_width": 1.7},  # virginica
        {"sepal_length": 5.9, "sepal_width": 3.0, "petal_length": 4.2, "petal_width": 1.5},  # versicolor
    ]

    print("--- Testing 3 Samples ---")
    for i, sample in enumerate(test_samples):
        resp = client.post("/predict", json=sample)
        data = resp.json()
        print(f"\nSample {i+1}: {sample}")
        print(f"  Prediction: {data['prediction']} ({data['class_name']})")
        print(f"  Probabilities: {data['probabilities']}")


if __name__ == "__main__":
    test_app()

    print(f"\n--- Server Info ---")
    print(f"Docs: http://localhost:8000/docs")
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
