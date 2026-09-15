# Lesson 19 — Concepts Explained (Model Deployment)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## What is Model Deployment?

**What:** Making a trained model available for predictions in production.

```python
# Training (development):
model.fit(X_train, y_train)  # done on your laptop

# Deployment (production):
# User sends data → model predicts → user gets result
# This needs a server, API, and infrastructure
```

**Why it exists:** A trained model on your laptop is useless to users. Deployment makes it accessible → users can send data and get predictions → the model creates value.

**Where it's used:** Every ML model that needs to serve predictions to users — web apps, mobile apps, APIs.

**What goes wrong without it:**
- Training a model but never deploying → no business value → wasted effort.
- Deploying without testing → model crashes on real data → bad user experience.
- Not monitoring → model degrades over time (data drift) → predictions become wrong.

---

## Saving and Loading Models

**What:** Persist a trained model to disk → load it later for inference.

```python
import joblib

# Save
joblib.dump(model, 'model.pkl')

# Load
model = joblib.load('model.pkl')
predictions = model.predict(X_new)
```

```python
# For PyTorch
import torch

# Save
torch.save(model.state_dict(), 'model.pth')

# Load
model = MyModel()
model.load_state_dict(torch.load('model.pth'))
model.eval()
```

**Why it exists:** Training takes time (minutes to days). You don't want to retrain every time you need a prediction. Saving → load instantly → fast inference.

**Where it's used:** Every deployment — save after training, load for inference.

**What goes wrong without it:**
- Using `pickle` for sklearn models → works but `joblib` is better (handles NumPy arrays efficiently).
- For PyTorch: saving the entire model (`torch.save(model, ...)`) → breaks if the class changes. Save `state_dict` only.
- Not saving the preprocessing pipeline → model expects scaled data, you feed raw → wrong predictions. Save the pipeline, not just the model.

---

## Flask API for Model Serving

**What:** Wrap the model in a Flask web API → users send HTTP requests → get predictions.

```python
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

# Client request:
# POST /predict
# {"features": [25, 50000, 3]}
# Response: {"prediction": 1}
```

**Why it exists:** Without an API, the model is just a Python script. An API makes it accessible from any language (web, mobile, other services) → production-ready.

**Where it's used:** Every model that serves predictions to applications.

**What goes wrong without it:**
- Loading the model inside the route → loaded on every request → slow. Load once at startup.
- Not validating input → user sends wrong format → crash. Validate before predicting.
- Synchronous Flask → can't handle concurrent requests. Use Gunicorn or FastAPI for production.

---

## FastAPI for Model Serving

**What:** FastAPI is a modern, fast alternative to Flask with automatic documentation.

```python
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
model = joblib.load('model.pkl')

class InputData(BaseModel):
    features: list

@app.post('/predict')
def predict(data: InputData):
    features = np.array(data.features).reshape(1, -1)
    prediction = model.predict(features)
    return {'prediction': int(prediction[0])}

# Run: uvicorn app:app --reload
# Docs: http://localhost:8000/docs (automatic Swagger UI)
```

**Why it exists:** Flask is simple but slow and untyped. FastAPI is async (fast), has type validation (Pydantic), and auto-generates docs → better for production ML APIs.

**Where it's used:** Modern ML APIs, production model serving.

**What goes wrong without it:**
- Not installing: `pip install fastapi uvicorn`.
- Pydantic model doesn't match input → 422 error (validation). Define the schema correctly.
- Not using async for I/O-bound tasks → slower than possible. Use `async def` for database calls.

---

## Docker for Model Deployment

**What:** Package the model, API, and dependencies into a Docker container → runs anywhere.

```dockerfile
# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY model.pkl .
COPY app.py .

EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

```bash
# Build
docker build -t ml-model .

# Run
docker run -p 8000:8000 ml-model
```

**Why it exists:** Without Docker, "works on my machine" → deployment fails because the server has different Python/library versions. Docker packages everything → runs identically everywhere → reliable deployment.

**Where it's used:** Every production ML deployment.

**What goes wrong without it:**
- Large Docker image → slow to build and deploy. Use `python:3.9-slim` not `python:3.9`.
- Not pinning versions in `requirements.txt` → `flask` → might install a newer, breaking version. Use `flask==2.3.0`.
- Copying the entire project → includes data, notebooks → huge image. Use `.dockerignore`.

---

## Batch vs Real-time Prediction

**What:** Two deployment patterns:

```python
# Batch prediction: predict on many samples at once (offline)
# Good for: daily reports, recommendations, non-urgent tasks
predictions = model.predict(all_data)
save_to_database(predictions)

# Real-time prediction: predict on one sample at a time (online)
# Good for: user-facing apps, fraud detection, urgent tasks
@app.route('/predict', methods=['POST'])
def predict():
    prediction = model.predict(single_sample)
    return jsonify({'prediction': prediction})
```

**Why it exists:** Different use cases need different patterns. Batch is efficient for large-scale, non-urgent predictions. Real-time is necessary for user-facing applications.

**Where it's used:** Batch → reporting, recommendations. Real-time → web apps, fraud detection.

**What goes wrong without it:**
- Real-time for everything → expensive (server always running). Use batch for non-urgent tasks.
- Batch for user-facing → user waits for the next batch run → bad UX. Use real-time.
- Not choosing → ad-hoc → inefficient and inconsistent.

---

## Model Monitoring

**What:** Track the model's performance in production over time.

```python
# Log predictions and actual outcomes
import logging

logging.info(f"Input: {features}, Prediction: {prediction}")

# Track metrics over time
# - Prediction latency (ms per request)
# - Input data distribution (data drift)
# - Accuracy (when ground truth is available)
# - Error rate (crashes, NaN predictions)
```

**Why it exists:** Models degrade over time → data drift (user behavior changes), concept drift (the relationship changes). Without monitoring, you don't know the model is failing → silent errors → business impact.

**Where it's used:** Every production ML model.

**What goes wrong without it:**
- No monitoring → model fails silently → users get wrong predictions → trust lost.
- Only monitoring accuracy → but ground truth is often delayed (fraud confirmed weeks later). Monitor input distribution too.
- Not alerting → you check logs manually → miss issues. Set up automated alerts for anomalies.

---

## Testing ML Systems

**What:** Test the model and API before deployment.

```python
# Unit test: model produces valid output
def test_model_output():
    model = joblib.load('model.pkl')
    X = np.array([[25, 50000, 3]])
    pred = model.predict(X)
    assert pred is not None
    assert 0 <= pred[0] <= 1  # valid range

# Integration test: API responds correctly
def test_api():
    response = client.post('/predict', json={'features': [25, 50000, 3]})
    assert response.status_code == 200
    assert 'prediction' in response.json()

# Edge case test: invalid input
def test_invalid_input():
    response = client.post('/predict', json={'features': 'invalid'})
    assert response.status_code == 422  # validation error
```

**Why it exists:** Without testing, you deploy blindly → bugs in production → bad user experience. Testing catches issues before they reach users.

**Where it's used:** Every ML deployment — test before going live.

**What goes wrong without it:**
- Only testing accuracy → but the API might crash on edge cases (NaN input, missing features).
- Not testing with real data → test data is clean, production data is messy → crashes.
- No CI/CD → tests are manual → forgotten → bugs slip through. Automate testing.

---

## Deployment Checklist

**What:** A checklist for production deployment:

1. **Model:** saved, loaded, produces correct predictions
2. **API:** endpoints work, input validation, error handling
3. **Docker:** container builds and runs
4. **Testing:** unit, integration, edge case tests pass
5. **Monitoring:** logs, metrics, alerts configured
6. **Performance:** latency < target, can handle expected load
7. **Documentation:** API docs, usage examples
8. **Rollback:** plan to revert if something goes wrong

**Why it exists:** Without a checklist, you forget steps → production issues. A checklist ensures consistency → reliable deployments.

**Where it's used:** Every production deployment.

**What goes wrong without it:**
- Skipping monitoring → model fails silently.
- No rollback plan → if deployment breaks → can't revert → downtime.
- Not load testing → works for 1 request, crashes for 1000. Test under realistic load.
