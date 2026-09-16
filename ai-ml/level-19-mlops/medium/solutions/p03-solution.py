"""Level 19 — MLOps — Medium P03 Solution"""

import json


def compare_runs(file, metric="accuracy"):
    """Return the run dict with the highest value for `metric`."""
    best = None
    with open(file) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            run = json.loads(line)
            if metric not in run.get("metrics", {}):
                continue
            if best is None or run["metrics"][metric] > best["metrics"][metric]:
                best = run
    return best


if __name__ == "__main__":
    import os

    path = os.path.join(os.path.dirname(__file__), "demo-runs.jsonl")
    with open(path, "w") as f:
        f.write(json.dumps({"name": "a", "metrics": {"accuracy": 0.90}}) + "\n")
        f.write(json.dumps({"name": "b", "metrics": {"accuracy": 0.97}}) + "\n")
        f.write(json.dumps({"name": "c", "metrics": {"accuracy": 0.93}}) + "\n")
    best = compare_runs(path)
    print(best["name"], best["metrics"]["accuracy"])
    os.remove(path)
