"""Level 10 — Model Deployment — Easy P01 Solution"""

import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def save_and_load():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=200, random_state=42)
    model.fit(X_train, y_train)
    joblib.dump(model, 'model.pkl')
    loaded = joblib.load('model.pkl')
    return loaded.predict(X_test[:5]).tolist()

if __name__ == "__main__":
    print(save_and_load())
