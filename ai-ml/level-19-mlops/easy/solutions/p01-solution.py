"""Level 19 — MLOps — Easy P01 Solution"""

import json
import os
import time


def log_run(run_name, params, metrics):
    """Append one run record to runs.jsonl. Returns the record."""
    record = {
        "timestamp": time.time(),
        "name": run_name,
        "params": params,
        "metrics": metrics,
    }
    path = os.path.join(os.path.dirname(__file__), "runs.jsonl")
    with open(path, "a") as f:
        f.write(json.dumps(record) + "\n")
    return record


if __name__ == "__main__":
    print(log_run("lr-baseline", {"C": 1.0}, {"accuracy": 0.95}))
