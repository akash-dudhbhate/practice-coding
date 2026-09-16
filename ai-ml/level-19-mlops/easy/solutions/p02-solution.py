"""Level 19 — MLOps — Easy P02 Solution"""

import joblib


def save_model(model, path):
    """Persist model to path with joblib. Returns path."""
    joblib.dump(model, path)
    return path


def load_model(path):
    """Load and return a joblib-persisted model."""
    return joblib.load(path)


if __name__ == "__main__":
    from sklearn.datasets import load_iris
    from sklearn.linear_model import LogisticRegression

    X, y = load_iris(return_X_y=True)
    m = LogisticRegression(max_iter=200).fit(X, y)
    save_model(m, "model.joblib")
    print(load_model("model.joblib").predict(X[:3]))
