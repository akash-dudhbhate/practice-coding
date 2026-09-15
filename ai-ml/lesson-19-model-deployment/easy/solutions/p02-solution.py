"""
Flask app with /predict endpoint
=================================
Create a Flask app with a /predict endpoint that loads a saved model,
accepts JSON {"features": [...]}, and returns {"prediction": ...}.
Includes test code.
"""

import joblib
import numpy as np
from flask import Flask, request, jsonify

# --- Model training and saving (run once before starting the app) ---
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier


def train_and_save_model():
    """Train a simple model and save it."""
    iris = load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_s, y_train)
    joblib.dump(model, "iris_model.joblib")
    joblib.dump(scaler, "iris_scaler.joblib")
    print(f"Model saved. Test accuracy: {model.score(scaler.transform(X_test), y_test):.4f}")


# --- Flask App ---
app = Flask(__name__)

# Load model and scaler at startup
try:
    model = joblib.load("iris_model.joblib")
    scaler = joblib.load("iris_scaler.joblib")
except FileNotFoundError:
    print("Model not found. Training and saving...")
    train_and_save_model()
    model = joblib.load("iris_model.joblib")
    scaler = joblib.load("iris_scaler.joblib")


@app.route("/predict", methods=["POST"])
def predict():
    """Accept JSON {"features": [4.5, 3.0, 1.5, 0.3]} and return prediction."""
    data = request.get_json(force=True)
    features = data.get("features", [])

    if not features or len(features) != 4:
        return jsonify({"error": "Expected 'features' list with 4 values"}), 400

    features_array = np.array(features).reshape(1, -1)
    features_scaled = scaler.transform(features_array)
    prediction = model.predict(features_scaled)[0]
    class_name = load_iris().target_names[prediction]

    return jsonify({
        "prediction": int(prediction),
        "class": class_name
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"})


# --- Test code ---
def test_app():
    """Test the Flask app using the test client."""
    with app.test_client() as client:
        # Test /health
        resp = client.get("/health")
        print(f"GET /health -> {resp.status_code}: {resp.get_json()}")

        # Test /predict with valid input
        resp = client.post("/predict", json={"features": [5.1, 3.5, 1.4, 0.2]})
        print(f"POST /predict (valid) -> {resp.status_code}: {resp.get_json()}")

        # Test /predict with invalid input (wrong number of features)
        resp = client.post("/predict", json={"features": [1.0, 2.0]})
        print(f"POST /predict (invalid) -> {resp.status_code}: {resp.get_json()}")


if __name__ == "__main__":
    print("--- Running Tests ---")
    test_app()

    print("\n--- Starting Flask Server ---")
    print("To test: curl -X POST http://localhost:5000/predict "
          "-H 'Content-Type: application/json' "
          "-d '{\"features\": [5.1, 3.5, 1.4, 0.2]}'")
    app.run(host="0.0.0.0", port=5000, debug=True)
