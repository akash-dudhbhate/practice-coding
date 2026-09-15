# Lesson 19 — Hard P01: Complete deployment package
# Train, save, FastAPI app (/predict, /health), Dockerfile, tests, README, client.py
# All in one file with clearly marked sections.

import joblib
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# ============ SECTION 1: Train and Save Model ============
iris = load_iris()
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", LogisticRegression(max_iter=200)),
])
pipeline.fit(iris.data, iris.target)
joblib.dump(pipeline, "iris_model.joblib")
print("Model saved to iris_model.joblib")

# ============ SECTION 2: FastAPI App (app.py) ============
APP_CODE = '''
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="Iris Classifier API")
model = joblib.load("iris_model.joblib")

class PredictRequest(BaseModel):
    features: list[float]

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/predict")
def predict(req: PredictRequest):
    features = np.array(req.features).reshape(1, -1)
    prediction = int(model.predict(features)[0])
    return {"prediction": prediction}
'''
print("\n--- app.py ---")
print(APP_CODE)

# ============ SECTION 3: Dockerfile ============
DOCKERFILE = '''
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py iris_model.joblib ./
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
'''
print("\n--- Dockerfile ---")
print(DOCKERFILE)

# ============ SECTION 4: requirements.txt ============
REQUIREMENTS = """
fastapi==0.104.1
uvicorn==0.24.0
scikit-learn==1.3.2
joblib==1.3.2
numpy==1.26.2
pydantic==2.5.2
"""
print("\n--- requirements.txt ---")
print(REQUIREMENTS)

# ============ SECTION 5: Tests (test_app.py) ============
TEST_CODE = '''
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_predict():
    response = client.post("/predict", json={"features": [5.1, 3.5, 1.4, 0.2]})
    assert response.status_code == 200
    assert "prediction" in response.json()

def test_invalid_input():
    response = client.post("/predict", json={"features": [1.0]})
    assert response.status_code == 422 or "error" in response.json()
'''
print("\n--- test_app.py ---")
print(TEST_CODE)

# ============ SECTION 6: client.py ============
CLIENT_CODE = '''
import requests
response = requests.post(
    "http://localhost:8000/predict",
    json={"features": [5.1, 3.5, 1.4, 0.2]}
)
print(f"Prediction: {response.json()}")
'''
print("\n--- client.py ---")
print(CLIENT_CODE)

# ============ SECTION 7: README.md ============
README = """
# Iris Classifier API

## Usage
1. Build: `docker build -t iris-api .`
2. Run: `docker run -p 8000:8000 iris-api`
3. Test: `python client.py`
4. Docs: `http://localhost:8000/docs`

## Endpoints
- GET /health — Health check
- POST /predict — Predict iris species
"""
print("\n--- README.md ---")
print(README)
