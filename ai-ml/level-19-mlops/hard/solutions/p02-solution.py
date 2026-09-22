"""Level 19 — MLOps — Hard P02 Solution"""

import hashlib
import json

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


def make_dataset():
    """The canonical dataset every run in this level trains on."""
    return make_classification(
        n_samples=200, n_features=5, n_informative=3, random_state=42)


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


def reproduce_run(run_file, run_id, tol=0.01):
    """Reload a logged run, retrain, verify metrics match."""
    # 1. find the run
    run = None
    with open(run_file) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            r = json.loads(line)
            if r.get("run_id") == run_id:
                run = r
                break
    if run is None:
        return {"found": False, "data_ok": False,
                "expected": None, "actual": None, "match": False}

    # 2. rebuild the canonical dataset + verify its hash
    X, y = make_dataset()
    data_ok = data_version_hash(X, y) == run.get("data_hash")

    # 3. retrain with the logged params on the standard split
    Xtr, Xte, ytr, yte = train_test_split(
        X, y, test_size=0.25, random_state=42)
    model = LogisticRegression(**run["params"])
    model.fit(Xtr, ytr)
    actual = model.score(Xte, yte)

    # 4. compare
    expected = run["metrics"]["accuracy"]
    match = data_ok and abs(actual - expected) <= tol
    return {"found": True, "data_ok": data_ok,
            "expected": expected, "actual": actual, "match": match}


if __name__ == "__main__":
    import os

    X, y = make_dataset()
    Xtr, Xte, ytr, yte = train_test_split(
        X, y, test_size=0.25, random_state=42)
    params = {"C": 1.0, "max_iter": 300, "random_state": 42}
    acc = LogisticRegression(**params).fit(Xtr, ytr).score(Xte, yte)
    path = os.path.join(os.path.dirname(__file__), "demo-runs.jsonl")
    with open(path, "w") as f:
        f.write(json.dumps({"run_id": "r1", "params": params,
                            "data_hash": data_version_hash(X, y),
                            "metrics": {"accuracy": acc}}) + "\n")
    print(reproduce_run(path, "r1"))
    os.remove(path)
