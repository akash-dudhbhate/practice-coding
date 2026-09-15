# Lesson 19 — Medium P03: Tests for ML API (pytest + TestClient)
# Unit test, integration test, and edge case tests for a FastAPI ML endpoint.

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel
import joblib
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# --- Setup: train and save a model ---
iris = load_iris()
model = LogisticRegression(max_iter=200)
model.fit(iris.data, iris.target)
joblib.dump(model, "test_model.joblib")

# --- FastAPI app ---
app = FastAPI()
loaded_model = joblib.load("test_model.joblib")


class PredictRequest(BaseModel):
    features: list[float]


@app.post("/predict")
def predict(req: PredictRequest):
    if len(req.features) != 4:
        return {"error": "Expected 4 features"}
    features = np.array(req.features).reshape(1, -1)
    prediction = int(loaded_model.predict(features)[0])
    return {"prediction": prediction}


client = TestClient(app)

# --- Tests ---

def test_unit_model_produces_valid_output():
    """Unit test: model produces a valid class label (0, 1, or 2)."""
    features = np.array([[5.1, 3.5, 1.4, 0.2]])
    pred = loaded_model.predict(features)[0]
    assert pred in [0, 1, 2], f"Invalid prediction: {pred}"


def test_integration_api_responds_correctly():
    """Integration test: API responds with a valid prediction."""
    response = client.post("/predict", json={"features": [5.1, 3.5, 1.4, 0.2]})
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
    assert data["prediction"] in [0, 1, 2]


def test_edge_case_invalid_input_returns_422():
    """Edge case: non-numeric input returns 422 validation error."""
    response = client.post("/predict", json={"features": ["a", "b", "c", "d"]})
    assert response.status_code == 422


def test_edge_case_missing_field_returns_error():
    """Edge case: missing 'features' field returns error."""
    response = client.post("/predict", json={})
    assert response.status_code == 422


def test_edge_case_wrong_number_of_features():
    """Edge case: wrong number of features returns error message."""
    response = client.post("/predict", json={"features": [1.0, 2.0]})
    assert response.status_code == 200
    data = response.json()
    assert "error" in data


# Run tests: pytest medium/p03-solution.py -v
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
