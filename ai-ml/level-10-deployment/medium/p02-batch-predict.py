"""
LEVEL 10 — Model Deployment
MEDIUM P02 — Batch Prediction Endpoint
========================================

CONCEPT:
  One prediction at a time is slow. Real APIs accept batches:
    POST /predict-batch {"features": [[...], [...], [...]]}
  Return all predictions in one response.

  model.predict(features_list) — sklearn handles 2D arrays natively.

PROBLEM:
  Write `create_batch_app()` that:
    1. Trains + loads iris model
    2. FastAPI app with POST /predict-batch
    3. Accepts {"features": [[5.1,3.5,1.4,0.2], [6.0,2.2,5.0,1.5]]}
    4. Returns {"predictions": [0, 2]}
    5. Returns the app object

TRY THIS INPUT:
  ```python
  app = create_batch_app()
  from fastapi.testclient import TestClient
  c = TestClient(app)
  r = c.post('/predict-batch', json={'features': [[5.1,3.5,1.4,0.2],[6.0,2.2,5.0,1.5]]})
  print(r.json())
  ```

EXPECTED OUTPUT:
  ```
  {'predictions': [0, 2]}
  ```

HINT:
  class BatchInput(BaseModel): features: list[list[float]]
  model.predict(input.features).tolist()

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# app = create_batch_app()
# from fastapi.testclient import TestClient
# c = TestClient(app)
# print(c.post('/predict-batch', json={'features':[[5.1,3.5,1.4,0.2],[6.0,2.2,5.0,1.5]]}).json())
