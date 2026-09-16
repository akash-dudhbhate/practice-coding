"""Level 10 — Model Deployment — Medium P01 Solution"""

from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

class Features(BaseModel):
    features: list[float]

def create_fastapi_app():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=200, random_state=42)
    model.fit(X_train, y_train)

    app = FastAPI()

    @app.post('/predict')
    def predict(data: Features):
        pred = model.predict([data.features])[0]
        probs = model.predict_proba([data.features])[0].tolist()
        return {'prediction': int(pred), 'probabilities': probs}

    return app

if __name__ == "__main__":
    app = create_fastapi_app()
    from fastapi.testclient import TestClient
    c = TestClient(app)
    r = c.post('/predict', json={'features': [5.1, 3.5, 1.4, 0.2]})
    print(r.json())
