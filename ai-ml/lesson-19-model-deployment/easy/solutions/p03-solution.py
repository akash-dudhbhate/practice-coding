"""
FastAPI app with /predict endpoint
===================================
Create a FastAPI app with the same /predict endpoint as the Flask version.
Use a Pydantic model for input validation. Include uvicorn run code.
Print the docs URL (/docs).
"""

import joblib
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier


# --- Train and save model (if not already saved) ---
def train_and_save_model():
    iris = load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_s, y_train)
    joblib.dump(model, "iris_model.joblib")
    joblib.dump(scaler, "iris_scaler.joblib")
    print(f"Model saved. Accuracy: {model.score(scaler.transform(X_test), y_test):.4f}")


# --- Pydantic model for input validation ---
class PredictRequest(BaseModel):
    features: list[float] = Field(..., description="List of 4 feature values", min_length=4, max_length=4)


class PredictResponse(BaseModel):
    prediction: int
    class_name: str


# --- FastAPI App ---
app = FastAPI(title="Iris Prediction API", version="1.0.0")

try:
    model = joblib.load("iris_model.joblib")
    scaler = joblib.load("iris_scaler.joblib")
except FileNotFoundError:
    train_and_save_model()
    model = joblib.load("iris_model.joblib")
    scaler = joblib.load("iris_scaler.joblib")

iris_data = load_iris()


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    """Predict Iris species from 4 features."""
    features_array = np.array(request.features).reshape(1, -1)
    features_scaled = scaler.transform(features_array)
    prediction = int(model.predict(features_scaled)[0])
    class_name = iris_data.target_names[prediction]
    return PredictResponse(prediction=prediction, class_name=class_name)


# --- Test code ---
def test_app():
    """Test the FastAPI app using TestClient."""
    from fastapi.testclient import TestClient
    client = TestClient(app)

    print("--- Running Tests ---")

    # Test /health
    resp = client.get("/health")
    print(f"GET /health -> {resp.status_code}: {resp.json()}")

    # Test /predict with valid input
    resp = client.post("/predict", json={"features": [5.1, 3.5, 1.4, 0.2]})
    print(f"POST /predict (valid) -> {resp.status_code}: {resp.json()}")

    # Test /predict with invalid input (missing field)
    resp = client.post("/predict", json={"wrong_field": [1, 2, 3, 4]})
    print(f"POST /predict (missing field) -> {resp.status_code}: {resp.json()}")

    # Test /predict with wrong number of features
    resp = client.post("/predict", json={"features": [1.0, 2.0]})
    print(f"POST /predict (wrong count) -> {resp.status_code}: {resp.json()}")


if __name__ == "__main__":
    test_app()

    print(f"\n--- FastAPI Server ---")
    print(f"Docs URL: http://localhost:8000/docs")
    print(f"Health:   http://localhost:8000/health")
    print(f"Predict:  POST http://localhost:8000/predict")

    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
