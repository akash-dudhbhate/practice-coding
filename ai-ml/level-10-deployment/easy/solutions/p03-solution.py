"""Level 10 — Model Deployment — Easy P03 Solution"""

import joblib
from flask import Flask, request, jsonify
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def create_predict_app():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=200, random_state=42)
    model.fit(X_train, y_train)
    joblib.dump(model, 'model.pkl')
    model = joblib.load('model.pkl')

    app = Flask(__name__)

    @app.route('/predict')
    def predict():
        f = request.args.get('f', '')
        features = [float(x) for x in f.split(',')]
        pred = model.predict([features])[0]
        return jsonify({'prediction': int(pred)})

    return app

if __name__ == "__main__":
    app = create_predict_app()
    client = app.test_client()
    r = client.get('/predict?f=5.1,3.5,1.4,0.2')
    print(r.get_json())
