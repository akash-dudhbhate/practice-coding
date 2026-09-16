# Level 10 — Concepts Reference

## Easy

### Model Persistence
- `joblib.dump(model, 'model.pkl')` → save
- `joblib.load('model.pkl')` → load, ready to predict

### Flask API
- `app = Flask(__name__)` + `@app.route('/predict', methods=['POST'])`
- `request.json` → input data; `jsonify()` → JSON response
- `app.test_client()` → test without starting a server

### GET Endpoint
- `request.args.get('f')` → query string params
- Load model ONCE at startup, reuse for all requests

## Medium

### FastAPI + Pydantic
- `class Input(BaseModel)` → auto-validated JSON input
- `TestClient(app)` → test endpoints without running a server

### Batch Prediction
- `model.predict([[...], [...]])` → multiple predictions at once
- Better than looping — one call, one response

### Model Versioning
- Dict: `{'v1': {'model': ..., 'accuracy': ...}}`
- Track which version produced which score → rollback if needed

## Hard

### Dockerfile
- `FROM python:3.10-slim` → `WORKDIR /app` → `COPY` → `RUN pip install` → `CMD`
- Container = your app + deps, runs anywhere

### Monitoring
- Wrap predict() to log: prediction, latency, running stats
- Track `total_predictions`, `avg_latency`, error rate

### A/B Testing
- Route by hash of input → consistent experience per input
- `hash(tuple(features)) % 2` → model A vs model B
- Compare which model gets better results on real traffic
