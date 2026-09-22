"""Level 19 — MLOps — Hard P01 Solution"""

import hashlib
import json


def data_version_hash(X, y):
    """Deterministic hex digest fingerprinting a dataset."""
    if hasattr(X, "tolist"):
        X = X.tolist()
    if hasattr(y, "tolist"):
        y = y.tolist()
    payload = {
        "n_rows": len(X),
        "n_cols": len(X[0]) if X else 0,
        "n_labels": len(y),
        "x_head": [[round(float(v), 6) for v in row] for row in X[:5]],
        "x_tail": [[round(float(v), 6) for v in row] for row in X[-5:]],
        "y_head": [int(v) for v in y[:5]],
        "y_tail": [int(v) for v in y[-5:]],
    }
    return hashlib.md5(
        json.dumps(payload, sort_keys=True).encode()).hexdigest()


if __name__ == "__main__":
    from sklearn.datasets import load_iris

    X, y = load_iris(return_X_y=True)
    print(data_version_hash(X, y))
    print(data_version_hash(X, y) == data_version_hash(X[:100], y[:100]))
