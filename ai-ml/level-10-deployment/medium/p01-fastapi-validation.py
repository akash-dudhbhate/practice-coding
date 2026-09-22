"""
LEVEL 10 — Model Deployment
MEDIUM P01 — FastAPI with Pydantic Validation
========================================

CONCEPT:
  FastAPI = modern Flask alternative with automatic validation.
  Pydantic models define the expected JSON shape — bad input gets
  rejected automatically with a clear error.

    class Input(BaseModel):
        features: list[float]

    @app.post('/predict')
    def predict(data: Input):
        return {"prediction": model.predict([data.features])[0]}

PROBLEM:
  Write `create_fastapi_app()` that:
    1. Trains + loads iris model
    2. Creates FastAPI app with Pydantic input validation
    3. POST /predict accepts {"features": [f1,f2,f3,f4]}
    4. Returns {"prediction": int, "probabilities": [...]}
    5. Returns the app object

TRY THIS INPUT:
  ```python
  app = create_fastapi_app()
  from fastapi.testclient import TestClient
  c = TestClient(app)
  r = c.post('/predict', json={'features': [5.1,3.5,1.4,0.2]})
  print(r.json())
  ```

EXPECTED OUTPUT:
  ```
  {'prediction': 0, 'probabilities': [0.9x, 0.0x, 0.0x]}
  ```

HINT:
  from fastapi import FastAPI
  from pydantic import BaseModel
  from fastapi.testclient import TestClient

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# app = create_fastapi_app()
# from fastapi.testclient import TestClient
# c = TestClient(app)
# print(c.post('/predict', json={'features':[5.1,3.5,1.4,0.2]}).json())
