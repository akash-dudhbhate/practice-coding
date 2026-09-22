"""Level 06 — Advanced ML — Hard P01 Solution"""

import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

class LogTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, cols=None):
        self.cols = cols

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = np.array(X, dtype=float).copy()
        for c in (self.cols or range(X.shape[1])):
            X[:, c] = np.log1p(np.abs(X[:, c])) * np.sign(X[:, c])
        return X

def run_pipeline():
    X, y = make_classification(n_samples=200, n_features=5, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    pipeline = Pipeline([
        ('log', LogTransformer(cols=[0, 1])),
        ('model', LogisticRegression(max_iter=1000))
    ])
    pipeline.fit(X_train, y_train)
    return pipeline.score(X_test, y_test)

if __name__ == "__main__":
    print(f"Accuracy: {run_pipeline():.4f}")
