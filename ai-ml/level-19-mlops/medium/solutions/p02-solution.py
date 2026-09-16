"""Level 19 — MLOps — Medium P02 Solution"""

import hashlib
import json
import os
import time

import joblib


def register_model(model, name, metrics):
    """Save model + record a versioned entry in registry.json."""
    d = os.path.dirname(__file__)
    reg_path = os.path.join(d, "registry.json")

    registry = {}
    if os.path.exists(reg_path):
        with open(reg_path) as f:
            registry = json.load(f)

    version = len([k for k in registry if k.startswith(f"{name}-v")]) + 1
    model_path = os.path.join(d, f"{name}_v{version}.joblib")
    joblib.dump(model, model_path)

    h = hashlib.md5(
        json.dumps(model.get_params(), sort_keys=True, default=str).encode()
    ).hexdigest()

    entry = {
        "name": name,
        "version": version,
        "hash": h,
        "metrics": metrics,
        "timestamp": time.time(),
        "model_path": model_path,
    }
    registry[f"{name}-v{version}"] = entry

    with open(reg_path, "w") as f:
        json.dump(registry, f, indent=2)

    return entry


if __name__ == "__main__":
    from sklearn.datasets import load_iris
    from sklearn.linear_model import LogisticRegression

    X, y = load_iris(return_X_y=True)
    m = LogisticRegression(max_iter=200).fit(X, y)
    print(register_model(m, "iris", {"accuracy": 0.93}))
