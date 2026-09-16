"""
LEVEL 10 — Model Deployment
EASY P03 — Model Loading Endpoint
========================================

CONCEPT:
  In production, you load a saved model once at startup
  (not on every request). Serve predictions via HTTP.

  joblib.load('model.pkl') at startup → reuse for all requests.

PROBLEM:
  Write `create_predict_app()` that:
    1. Trains + saves model to 'model.pkl' (iris, LogisticRegression)
    2. Loads it back at startup
    3. Flask app: GET /predict?f=5.1,3.5,1.4,0.2
       → parses comma-separated features from query string
    4. Returns JSON {"prediction": class_index}
    5. Returns the app object

TRY THIS INPUT:
  ```python
  app = create_predict_app()
  c = app.test_client()
  r = c.get('/predict?f=5.1,3.5,1.4,0.2')
  print(r.get_json())
  ```

EXPECTED OUTPUT:
  ```
  {'prediction': 0}
  ```

HINT:
  request.args.get('f').split(',') → [float(x) for x in ...]

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# app = create_predict_app()
# c = app.test_client()
# print(c.get('/predict?f=5.1,3.5,1.4,0.2').get_json())
