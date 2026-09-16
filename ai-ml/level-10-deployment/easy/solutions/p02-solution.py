"""Level 10 — Model Deployment — Easy P02 Solution"""

from flask import Flask, request, jsonify
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def create_app():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=200, random_state=42)
    model.fit(X_train, y_train)

    app = Flask(__name__)

    @app.route('/predict', methods=['POST'])
    def predict():
        data = request.get_json()
        features = data['features']
        pred = model.predict([features])[0]
        return jsonify({'prediction': int(pred)})

    return app

if __name__ == "__main__":
    app = create_app()
    client = app.test_client()
    r = client.post('/predict', json={'features': [5.1, 3.5, 1.4, 0.2]})
    print(r.get_json())
