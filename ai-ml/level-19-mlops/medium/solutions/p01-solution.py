"""Level 19 — MLOps — Medium P01 Solution"""

import json
import os
import time


class ExperimentTracker:
    """Minimal experiment tracker: start → log → end → jsonl line."""

    def __init__(self, path=None):
        self.path = path or os.path.join(os.path.dirname(__file__), "runs.jsonl")
        self._run = None

    def start_run(self, name):
        self._run = {
            "timestamp": time.time(),
            "name": name,
            "params": {},
            "metrics": {},
        }

    def log_param(self, key, value):
        if self._run is None:
            raise RuntimeError("no active run — call start_run() first")
        self._run["params"][key] = value

    def log_metric(self, key, value):
        if self._run is None:
            raise RuntimeError("no active run — call start_run() first")
        self._run["metrics"][key] = value

    def end_run(self):
        if self._run is None:
            raise RuntimeError("no active run — call start_run() first")
        with open(self.path, "a") as f:
            f.write(json.dumps(self._run) + "\n")
        run = self._run
        self._run = None
        return run


if __name__ == "__main__":
    t = ExperimentTracker()
    t.start_run("lr-v1")
    t.log_param("C", 1.0)
    t.log_metric("accuracy", 0.95)
    print(t.end_run())
