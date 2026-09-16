"""
LEVEL 10 — Model Deployment
EASY P02 — Flask Prediction API
========================================

CONCEPT:
  Flask = lightweight web framework. Create an app, define
  routes (URLs), return JSON.

    app = Flask(__name__)
    @app.route('/predict', methods=['POST'])
    def predict():
        data = request.json
        return jsonify({'prediction': ...})

  Run: app.run() — then anyone can POST to your model.

PROBLEM:
  Write `create_app()` that:
    1. Trains a tiny model (iris, 80/20 split, LogisticRegression)
    2. Creates Flask app with POST /predict route
    3. Expects JSON: {"features": [5.1, 3.5, 1.4, 0.2]}
    4. Returns {"prediction": 0} (class index)
    5. Returns the app object

TRY THIS INPUT:
  ```python
  app = create_app()
  client = app.test_client()
  r = client.post('/predict', json={'features': [5.1,3.5,1.4,0.2]})
  print(r.get_json())  # {"prediction": 0}
  ```

EXPECTED OUTPUT:
  ```
  {'prediction': 0}
  ```

HINT:
  from flask import Flask, request, jsonify
  model.predict([features])[0] → int → jsonify

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# app = create_app()
# c = app.test_client()
# print(c.post('/predict', json={'features': [5.1,3.5,1.4,0.2]}).get_json())
