"""
Dockerfile and requirements for FastAPI app
=============================================
Write a Dockerfile for a FastAPI ML app. Include Python base image,
requirements, model file, app code, and CMD. Write requirements.txt.
Document build/run commands in comments.

NOTE: This file also writes the Dockerfile and requirements.txt to disk
so they can be used directly. The app code is included inline as a reference.
"""

import os

# --- App code (app.py) ---
APP_CODE = '''"""FastAPI ML app for Docker deployment."""
import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel, Field
from sklearn.datasets import load_iris

app = FastAPI(title="Iris API", version="1.0.0")
pipeline = joblib.load("iris_pipeline.joblib")
iris_data = load_iris()


class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict")
def predict(features: IrisFeatures):
    input_array = np.array([[
        features.sepal_length, features.sepal_width,
        features.petal_length, features.petal_width,
    ]])
    prediction = int(pipeline.predict(input_array)[0])
    return {"prediction": prediction, "class": iris_data.target_names[prediction]}
'''

# --- requirements.txt ---
REQUIREMENTS = """fastapi==0.104.1
uvicorn==0.24.0
scikit-learn==1.3.2
joblib==1.3.2
numpy==1.26.2
pydantic==2.5.2
"""

# --- Dockerfile ---
DOCKERFILE = """# Use Python slim base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for Docker layer caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy model file and app code
COPY iris_pipeline.joblib .
COPY app.py .

# Expose port
EXPOSE 8000

# Run the app with uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
"""

# --- README content ---
README = """# Iris Prediction API

## Build and Run with Docker

# Build the Docker image
docker build -t iris-api .

# Run the container
docker run -p 8000:8000 iris-api

# Test the API
curl http://localhost:8000/health
curl -X POST http://localhost:8000/predict \\
  -H "Content-Type: application/json" \\
  -d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'

# Interactive docs at http://localhost:8000/docs
"""


if __name__ == "__main__":
    # Write all deployment files
    files = {
        "app.py": APP_CODE,
        "requirements.txt": REQUIREMENTS,
        "Dockerfile": DOCKERFILE,
        "README.md": README,
    }

    print("--- Writing deployment files ---")
    for filename, content in files.items():
        with open(filename, "w") as f:
            f.write(content)
        print(f"  Written: {filename}")

    print(f"\n--- Build & Run Commands ---")
    print(f"# Build Docker image:")
    print(f"  docker build -t iris-api .")
    print(f"\n# Run container:")
    print(f"  docker run -p 8000:8000 iris-api")
    print(f"\n# Test:")
    print(f"  curl http://localhost:8000/health")
    print(f"  curl -X POST http://localhost:8000/predict \\")
    print(f"    -H 'Content-Type: application/json' \\")
    print(f"    -d '{{\"sepal_length\": 5.1, \"sepal_width\": 3.5, \"petal_length\": 1.4, \"petal_width\": 0.2}}'")
    print(f"\n# Docs: http://localhost:8000/docs")

    print(f"\n--- Dockerfile Explanation ---")
    print(f"1. FROM python:3.11-slim  — lightweight Python base image")
    print(f"2. WORKDIR /app           — set working directory inside container")
    print(f"3. COPY requirements.txt  — copy deps first for layer caching")
    print(f"4. RUN pip install        — install Python packages")
    print(f"5. COPY model + app       — copy model artifact and application code")
    print(f"6. EXPOSE 8000            — expose the API port")
    print(f"7. CMD uvicorn            — start the FastAPI server")
