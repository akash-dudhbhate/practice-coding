"""
Level 19 Checker — MLOps
=========================
Runs each check function against your work file.
Usage:
    python3 check.py easy/p01
    python3 check.py all
"""

import importlib.util
import os
import sys
import glob
import json

LEVEL_DIR = os.path.dirname(os.path.abspath(__file__))


def load_mod(fp):
    spec = importlib.util.spec_from_file_location("work", fp)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _mod_dir(mod):
    return os.path.dirname(os.path.abspath(mod.__file__))


# ---------------- EASY ----------------

def check_easy_p01(mod):
    if not hasattr(mod, 'log_run'):
        return False, "Function 'log_run' not found"
    runs_path = os.path.join(_mod_dir(mod), "runs.jsonl")
    if os.path.exists(runs_path):
        os.remove(runs_path)
    try:
        mod.log_run("test-a", {"C": 1.0}, {"accuracy": 0.9})
        mod.log_run("test-b", {"C": 2.0}, {"accuracy": 0.8})
        if not os.path.exists(runs_path):
            return False, "runs.jsonl was not created"
        with open(runs_path) as f:
            lines = [l for l in f if l.strip()]
        if len(lines) != 2:
            return False, f"Expected 2 lines in runs.jsonl, got {len(lines)}"
        r = json.loads(lines[0])
        for k in ("timestamp", "name", "params", "metrics"):
            if k not in r:
                return False, f"Record missing key '{k}': {r}"
        if r["name"] != "test-a" or r["params"] != {"C": 1.0} \
                or r["metrics"] != {"accuracy": 0.9}:
            return False, f"Bad record contents: {r}"
        if json.loads(lines[1])["name"] != "test-b":
            return False, "Second run was not appended correctly"
        return True, "All tests passed!"
    finally:
        if os.path.exists(runs_path):
            os.remove(runs_path)


def check_easy_p02(mod):
    for fn in ("save_model", "load_model"):
        if not hasattr(mod, fn):
            return False, f"Function '{fn}' not found"
    from sklearn.datasets import load_iris
    from sklearn.linear_model import LogisticRegression
    X, y = load_iris(return_X_y=True)
    m = LogisticRegression(max_iter=200).fit(X, y)
    path = os.path.join(LEVEL_DIR, "_check_model.joblib")
    try:
        ret = mod.save_model(m, path)
        if ret != path:
            return False, f"save_model should return path, got {ret!r}"
        if not os.path.exists(path):
            return False, "Model file was not created"
        m2 = mod.load_model(path)
        if list(m2.predict(X[:5])) != list(m.predict(X[:5])):
            return False, "Loaded model predicts differently"
        return True, "All tests passed!"
    finally:
        if os.path.exists(path):
            os.remove(path)


def check_easy_p03(mod):
    if not hasattr(mod, 'model_hash'):
        return False, "Function 'model_hash' not found"
    from sklearn.linear_model import LogisticRegression
    a = LogisticRegression(C=1.0, max_iter=200)
    b = LogisticRegression(C=1.0, max_iter=200)
    c = LogisticRegression(C=5.0, max_iter=200)
    h1, h2, h3 = mod.model_hash(a), mod.model_hash(b), mod.model_hash(c)
    if not isinstance(h1, str) or len(h1) < 8:
        return False, f"Expected hex string hash, got {h1!r}"
    if h1 != h2:
        return False, "Same params should give the same hash"
    if h1 == h3:
        return False, "Different params should give a different hash"
    return True, "All tests passed!"


# ---------------- MEDIUM ----------------

def check_medium_p01(mod):
    if not hasattr(mod, 'ExperimentTracker'):
        return False, "Class 'ExperimentTracker' not found"
    runs_path = os.path.join(_mod_dir(mod), "runs.jsonl")
    if os.path.exists(runs_path):
        os.remove(runs_path)
    try:
        t = mod.ExperimentTracker()
        t.start_run("exp1")
        t.log_param("C", 1.0)
        t.log_metric("accuracy", 0.9)
        run = t.end_run()
        if not isinstance(run, dict) or run.get("name") != "exp1":
            return False, f"end_run should return the run dict, got {run!r}"
        if run.get("params") != {"C": 1.0} \
                or run.get("metrics") != {"accuracy": 0.9}:
            return False, f"Params/metrics not recorded: {run}"
        if "timestamp" not in run:
            return False, "Run record missing 'timestamp'"
        if not os.path.exists(runs_path):
            return False, "runs.jsonl was not written on end_run()"
        with open(runs_path) as f:
            lines = [l for l in f if l.strip()]
        if len(lines) != 1:
            return False, f"Expected 1 line in runs.jsonl, got {len(lines)}"
        if json.loads(lines[0])["metrics"]["accuracy"] != 0.9:
            return False, "Persisted run has wrong metrics"
        return True, "All tests passed!"
    finally:
        if os.path.exists(runs_path):
            os.remove(runs_path)


def check_medium_p02(mod):
    if not hasattr(mod, 'register_model'):
        return False, "Function 'register_model' not found"
    from sklearn.datasets import load_iris
    from sklearn.linear_model import LogisticRegression
    mod_dir = _mod_dir(mod)
    reg_path = os.path.join(mod_dir, "registry.json")
    if os.path.exists(reg_path):
        os.remove(reg_path)
    try:
        X, y = load_iris(return_X_y=True)
        m = LogisticRegression(max_iter=200).fit(X, y)
        e1 = mod.register_model(m, "checkmodel", {"accuracy": 0.9})
        e2 = mod.register_model(m, "checkmodel", {"accuracy": 0.95})
        for k in ("name", "version", "hash", "metrics", "timestamp"):
            if k not in e1:
                return False, f"Registry entry missing '{k}': {e1}"
        if e1["version"] != 1 or e2["version"] != 2:
            return False, (f"Expected versions 1 and 2, got "
                           f"{e1['version']} and {e2['version']}")
        if not os.path.exists(reg_path):
            return False, "registry.json was not written"
        with open(reg_path) as f:
            reg = json.load(f)
        if "checkmodel-v1" not in reg or "checkmodel-v2" not in reg:
            return False, f"registry.json missing versioned entries: {list(reg)}"
        arts = glob.glob(os.path.join(mod_dir, "checkmodel*.joblib")) \
            + glob.glob(os.path.join(mod_dir, "checkmodel*.pkl"))
        if not arts:
            return False, "No model artifact file was saved"
        return True, "All tests passed!"
    finally:
        if os.path.exists(reg_path):
            os.remove(reg_path)
        for f in glob.glob(os.path.join(mod_dir, "checkmodel*.joblib")) \
                + glob.glob(os.path.join(mod_dir, "checkmodel*.pkl")):
            os.remove(f)


def check_medium_p03(mod):
    if not hasattr(mod, 'compare_runs'):
        return False, "Function 'compare_runs' not found"
    path = os.path.join(LEVEL_DIR, "_check_runs.jsonl")
    try:
        with open(path, "w") as f:
            f.write(json.dumps({"name": "a", "metrics": {"accuracy": 0.90}}) + "\n")
            f.write(json.dumps({"name": "b", "metrics": {"accuracy": 0.97}}) + "\n")
            f.write(json.dumps({"name": "c", "metrics": {"accuracy": 0.93}}) + "\n")
            f.write(json.dumps({"name": "d", "metrics": {"f1": 0.99}}) + "\n")
        best = mod.compare_runs(path)
        if not isinstance(best, dict):
            return False, f"Expected run dict, got {best!r}"
        if best.get("name") != "b":
            return False, f"Expected best run 'b', got {best.get('name')!r}"
        if best["metrics"]["accuracy"] != 0.97:
            return False, f"Wrong metrics in best run: {best['metrics']}"
        best_f1 = mod.compare_runs(path, metric="f1")
        if not isinstance(best_f1, dict) or best_f1.get("name") != "d":
            return False, "metric='f1' should select run 'd'"
        return True, "All tests passed!"
    finally:
        if os.path.exists(path):
            os.remove(path)


# ---------------- HARD ----------------

def check_hard_p01(mod):
    if not hasattr(mod, 'data_version_hash'):
        return False, "Function 'data_version_hash' not found"
    from sklearn.datasets import load_iris
    X, y = load_iris(return_X_y=True)
    h1 = mod.data_version_hash(X, y)
    if not isinstance(h1, str) or len(h1) < 8:
        return False, f"Expected hex string hash, got {h1!r}"
    if mod.data_version_hash(X, y) != h1:
        return False, "Hash is not deterministic for identical data"
    if mod.data_version_hash(X[:100], y[:100]) == h1:
        return False, "Truncated data gave the same hash"
    X2 = X.copy()
    X2[0] = X2[0] + 1.0
    if mod.data_version_hash(X2, y) == h1:
        return False, "Modified feature value not detected"
    return True, "All tests passed!"


def check_hard_p02(mod):
    if not hasattr(mod, 'reproduce_run'):
        return False, "Function 'reproduce_run' not found"
    from sklearn.datasets import make_classification
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split
    path = os.path.join(LEVEL_DIR, "_check_repro.jsonl")
    try:
        if hasattr(mod, "make_dataset"):
            X, y = mod.make_dataset()
        else:
            X, y = make_classification(
                n_samples=200, n_features=5, n_informative=3, random_state=42)
        params = {"C": 0.5, "max_iter": 300, "random_state": 42}
        Xtr, Xte, ytr, yte = train_test_split(
            X, y, test_size=0.25, random_state=42)
        acc = LogisticRegression(**params).fit(Xtr, ytr).score(Xte, yte)
        if hasattr(mod, "data_version_hash"):
            dh = mod.data_version_hash(X, y)
        else:
            import hashlib
            Xl, yl = X.tolist(), y.tolist()
            payload = {
                "n_rows": len(Xl), "n_cols": len(Xl[0]), "n_labels": len(yl),
                "x_head": [[round(float(v), 6) for v in r] for r in Xl[:5]],
                "x_tail": [[round(float(v), 6) for v in r] for r in Xl[-5:]],
                "y_head": [int(v) for v in yl[:5]],
                "y_tail": [int(v) for v in yl[-5:]],
            }
            dh = hashlib.md5(
                json.dumps(payload, sort_keys=True).encode()).hexdigest()
        with open(path, "w") as f:
            f.write(json.dumps({"run_id": "r1", "params": params,
                                "data_hash": dh,
                                "metrics": {"accuracy": acc}}) + "\n")
        res = mod.reproduce_run(path, "r1")
        if not isinstance(res, dict):
            return False, f"Expected dict result, got {res!r}"
        if not res.get("found"):
            return False, f"Run 'r1' not found: {res}"
        if not res.get("data_ok"):
            return False, f"Data hash verification failed: {res}"
        if not res.get("match"):
            return False, f"Metrics did not reproduce: {res}"
        res2 = mod.reproduce_run(path, "no-such-run")
        if res2.get("found") is not False:
            return False, f"Missing run should return found=False: {res2}"
        return True, "All tests passed!"
    finally:
        if os.path.exists(path):
            os.remove(path)


def check_hard_p03(mod):
    if not hasattr(mod, 'ci_gate'):
        return False, "Function 'ci_gate' not found"
    r1 = mod.ci_gate({"accuracy": 0.9, "f1": 0.85},
                     {"accuracy": 0.8, "f1": 0.8})
    if r1.get("pass") is not True or r1.get("failures") != []:
        return False, f"Expected pass=True, failures=[], got {r1}"
    r2 = mod.ci_gate({"accuracy": 0.7, "f1": 0.9},
                     {"accuracy": 0.8, "f1": 0.85})
    if r2.get("pass") is not False:
        return False, f"Expected pass=False, got {r2}"
    if not r2.get("failures") \
            or not any("accuracy" in s for s in r2["failures"]):
        return False, f"Expected an accuracy failure listed, got {r2}"
    r3 = mod.ci_gate({"accuracy": 0.9},
                     {"accuracy": 0.8, "precision": 0.5})
    if r3.get("pass") is not False or not r3.get("failures"):
        return False, f"Missing metric should fail the gate, got {r3}"
    return True, "All tests passed!"


CHECKS = {
    "easy/p01": check_easy_p01,   "easy/p02": check_easy_p02,
    "easy/p03": check_easy_p03,
    "medium/p01": check_medium_p01, "medium/p02": check_medium_p02,
    "medium/p03": check_medium_p03,
    "hard/p01": check_hard_p01,   "hard/p02": check_hard_p02,
    "hard/p03": check_hard_p03,
}


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 check.py <difficulty/pXX> or 'all'")
        return
    t = sys.argv[1]
    if t == "all":
        [run_one(c) for c in sorted(CHECKS)]
        return
    run_one(t)


def run_one(cid):
    if cid not in CHECKS:
        print(f"Unknown: {cid}")
        return
    diff, num = cid.split("/")
    nc = num.lstrip("p")
    d = os.path.join(os.path.dirname(__file__), diff)
    ms = [f for f in glob.glob(os.path.join(d, f"p{nc}-*.py"))
          if "solutions" not in f]
    w = ms[0] if ms else None
    if not w:
        print(f"{cid}: FILE NOT FOUND")
        return
    try:
        mod = load_mod(w)
        passed, msg = CHECKS[cid](mod)
        print(f"{cid}: {'PASS' if passed else 'FAIL'} — {msg}")
        if passed:
            with open(w) as f:
                if "DONE" not in f.readline().strip():
                    print("  → add '# DONE' to mark complete")
    except Exception as e:
        print(f"{cid}: ERROR — {e}")


if __name__ == "__main__":
    main()
