"""Level 10 Deployment — Easy P01 Solution"""

import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification

def solve():
    X, y = make_classification(n_samples=100, n_features=5, random_state=42)
    model = LogisticRegression(random_state=42).fit(X, y)
    # Save model
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
    # Load and predict
    with open('model.pkl', 'rb') as f:
        loaded_model = pickle.load(f)
    prediction = loaded_model.predict(X[:5])
    print(f"Predictions: {prediction}")
    return loaded_model

if __name__ == "__main__":
    solve()