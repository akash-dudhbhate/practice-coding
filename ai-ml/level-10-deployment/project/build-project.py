"""
LEVEL 10 PROJECT — Production-Ready Iris API
=============================================

Ship a complete model service — the full level-10 skillset in
one FastAPI app.

BUILD `create_service()` that returns a FastAPI app with:

  GET  /health            → {"status": "ok", "model": "iris-rf", "version": "1.0"}
  POST /predict           → {"prediction": int, "probability": float}
                            body: {"features": [4 floats]}
  POST /predict-batch     → {"predictions": [ints]}
                            body: {"features": [[4 floats], ...]}
  GET  /model-info        → {"type": "RandomForest", "n_features": 4,
                             "classes": ["setosa","versicolor","virginica"],
                             "test_accuracy": 0.9x}

MODEL: RandomForestClassifier(42) on iris, save+load via joblib
at startup (production pattern: load once, reuse).

TEST IT (this should run end-to-end):
  ```python
  from fastapi.testclient import TestClient
  app = create_service()
  c = TestClient(app)
  print(c.get('/health').json())
  print(c.post('/predict', json={'features':[5.1,3.5,1.4,0.2]}).json())
  ```

EXPECTED:
  ```
  {'status': 'ok', 'model': 'iris-rf', 'version': '1.0'}
  {'prediction': 0, 'probability': 0.9x}
  ```

BONUS: add request logging — print each /predict latency.
"""

# === WRITE YOUR CODE BELOW ===

def create_service():
    # TODO
    pass


if __name__ == "__main__":
    from fastapi.testclient import TestClient
    app = create_service()
    c = TestClient(app)
    print(c.get('/health').json())
    print(c.post('/predict', json={'features': [5.1, 3.5, 1.4, 0.2]}).json())
    print(c.post('/predict-batch',
                 json={'features': [[5.1,3.5,1.4,0.2],[6.0,2.2,5.0,1.5]]}).json())
    print(c.get('/model-info').json())
