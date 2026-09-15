# Lesson 19 — Model Deployment

## What you'll learn
- What model deployment is (making models accessible)
- Saving and loading models (joblib, PyTorch)
- Flask API for model serving
- FastAPI for model serving (modern, async)
- Docker for deployment (containerization)
- Batch vs real-time prediction
- Model monitoring (data drift, performance)
- Testing ML systems (unit, integration, edge cases)
- Deployment checklist

## Lesson

### Save and load
```python
import joblib
joblib.dump(model, 'model.pkl')
model = joblib.load('model.pkl')
```

### FastAPI
```python
from fastapi import FastAPI
app = FastAPI()
@app.post('/predict')
def predict(data: InputData):
    return {'prediction': int(model.predict([data.features])[0])}
```

### Docker
```dockerfile
FROM python:3.9-slim
COPY . /app
RUN pip install -r requirements.txt
CMD ["uvicorn", "app:app", "--host", "0.0.0.0"]
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.py` — Train a simple model (Iris classification). Save it with `joblib.dump`. Load it back and verify predictions match. Print before and after predictions.
2. `easy/p02-solve.py` — Create a Flask app with one `/predict` endpoint. Load a saved model. Accept JSON input `{"features": [...]}`, return `{"prediction": ...}`. Test with a sample request (use `requests` or curl).
3. `easy/p03-solve.py` — Create a FastAPI app with the same endpoint. Define a Pydantic model for input. Run with uvicorn. Test with a sample request. Print the automatic docs URL (`/docs`).

### Medium
4. `medium/p01-solve.py` — Build a complete model serving pipeline: train a model on a real dataset, save the model AND the scaler (use a sklearn Pipeline), create a FastAPI app that accepts raw input, scales it, and predicts. Test with 3 sample inputs.
5. `medium/p02-solve.py` — Write a Dockerfile for the FastAPI app. Include: Python base image, requirements installation, model file, app code, and CMD. Write the `requirements.txt` file. Document the build and run commands in comments.
6. `medium/p03-solve.py` — Write tests for the ML API: unit test (model produces valid output), integration test (API responds correctly), edge case test (invalid input returns 422, missing field returns error). Use `pytest` and `TestClient` from FastAPI.

### Hard
7. `hard/p01-solve.py` — Build a complete deployment package: train a model, save it, create a FastAPI app with `/predict` and `/health` endpoints, write a Dockerfile, write tests, and create a `README.md` with usage instructions. Include a `client.py` script that sends a test request.
8. `hard/p02-solve.py` — Build a batch prediction script: load a saved model, read a CSV file with input data, predict on all rows, save predictions to a new CSV. Compare batch prediction time with making individual API calls for each row. Document the performance difference.
9. `hard/p03-solve.py` — Build a monitoring script: simulate a deployed model, log predictions with timestamps, track input data statistics (mean, std) over time, detect data drift (compare current input stats to training stats), and raise an alert if drift is detected. Print a monitoring report.

### How to work
- Write your complete Python solution.
- Remove the TODO comment when done.
- Test with `python <filename>`.
