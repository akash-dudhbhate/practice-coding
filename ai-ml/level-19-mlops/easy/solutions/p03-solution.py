"""Level 19 — MLOps — Easy P03 Solution"""

import hashlib
import json


def model_hash(model):
    """Deterministic hex digest of the model's hyperparameters."""
    s = json.dumps(model.get_params(), sort_keys=True, default=str)
    return hashlib.md5(s.encode()).hexdigest()


if __name__ == "__main__":
    from sklearn.linear_model import LogisticRegression

    a = LogisticRegression(C=1.0, max_iter=200)
    b = LogisticRegression(C=1.0, max_iter=200)
    c = LogisticRegression(C=5.0, max_iter=200)
    print(model_hash(a) == model_hash(b))  # True
    print(model_hash(a) == model_hash(c))  # False
