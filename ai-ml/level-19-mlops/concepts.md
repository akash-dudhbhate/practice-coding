# Level 19 — Concepts (Detailed Explanations)

Read each section BEFORE attempting its problem. Each concept explains:
What it is · Why it exists · Where it's used · What goes wrong without
it · worked example · code · expected output.

The theme: training a model once is easy. Knowing WHICH run produced
it, WHAT data it saw, and WHETHER it's safe to ship — that's MLOps.
Everything here is the from-scratch version of what mlflow/wandb/DVC
do with a UI on top.

---

## Easy

### 1. Logging a Run (runs.jsonl) — `p01`

**What it is:** Experiment tracking = appending one JSON object per
training run to a file. `.jsonl` means "JSON Lines" — one complete
JSON object per line, so you can append without rewriting and parse
line-by-line. Each record captures WHEN (timestamp), WHAT (name +
params), and HOW WELL (metrics).

**Why it exists:** "Which experiment got 0.97?" — without a log, the
answer is lost in terminal scrollback. Run logging was invented so
every experiment leaves a durable record; append-only matters
because a corrupted or half-written run never erases the history
before it.

**Where it's used:** This is literally `mlflow.log_param` /
`wandb.log` — those tools write the same record to a database and
add a dashboard. Every serious training pipeline logs runs.

**What goes wrong without it:**
- Opening with `"w"` truncates the file and deletes all previous
  runs — always `"a"`.
- Write ONE line per run (`json.dumps` + `"\n"`), not `json.dump`
  of a list — a JSON array in one file can't be appended without
  rewriting the whole thing (and a crash mid-write corrupts all of
  it, not just the last line).
- No log at all → "the best model" is whichever run you happen to
  remember — unreproducible and unarguable.

**Worked example:**
```python
log_run("lr-baseline", {"C": 1.0}, {"accuracy": 0.95})
log_run("lr-strong",   {"C": 10.0}, {"accuracy": 0.97})
```
writes to `runs.jsonl`:
```
{"timestamp": 1717534800.12, "name": "lr-baseline",
 "params": {"C": 1.0}, "metrics": {"accuracy": 0.95}}
{"timestamp": 1717534811.48, "name": "lr-strong",
 "params": {"C": 10.0}, "metrics": {"accuracy": 0.97}}
```
Two runs, two lines, nothing overwritten.

**Code:**
```python
def log_run(run_name, params, metrics):
    record = {"timestamp": time.time(), "name": run_name,
              "params": params, "metrics": metrics}
    path = os.path.join(os.path.dirname(__file__), "runs.jsonl")
    with open(path, "a") as f:            # 'a' = append, never overwrite
        f.write(json.dumps(record) + "\n")
    return record
```

**Expected output:**
```python
log_run("lr-baseline", {"C": 1.0}, {"accuracy": 0.95})
# → {'timestamp': 1717534800.12, 'name': 'lr-baseline',
#    'params': {'C': 1.0}, 'metrics': {'accuracy': 0.95}}
# runs.jsonl gains exactly ONE new line per call
```

---

### 2. Saving & Loading a Model (joblib) — `p02`

**What it is:** A trained model is an ARTIFACT — a file you save once
and load anywhere: a server, a CI job, a teammate's laptop. `joblib`
serializes sklearn models efficiently (it's like `pickle` but faster
on big numpy arrays).

**Why it exists:** Training takes minutes to days; serving needs the
model in milliseconds. Serialization was invented as the bridge —
freeze the fitted weights into a file so any process can load them
without retraining. It's also what a model registry stores
(medium/p02): the `.joblib` file plus metadata about how it was made.

**Where it's used:** Model registries, offline scoring jobs,
model-as-a-file serving, sharing models between training and
production environments.

**What goes wrong without it:**
- The saved file contains the FITTED model — learned coefficients
  included. Re-fitting after loading re-rolls the dice on a model
  you already validated.
- Security: joblib/pickle files can execute code on load — only
  load files you created or trust. A malicious .pkl is arbitrary
  code execution.
- Without serialization, the model lives only in the process that
  trained it — process dies, model's gone; no deploys, no sharing.

**Worked example:**
```python
m = LogisticRegression(max_iter=200).fit(X, y)   # trained on iris
save_model(m, "model.joblib")                    # writes the file
# ... later, in a different process entirely:
m2 = load_model("model.joblib")
m2.predict(X[:3])   → array([0, 0, 0])
# the fitted coefficients came along for the ride — no retraining
```

**Code:**
```python
import joblib

def save_model(model, path):
    joblib.dump(model, path)
    return path

def load_model(path):
    return joblib.load(path)
```

**Expected output:**
```python
save_model(m, "model.joblib")      # → "model.joblib"  (file written)
m2 = load_model("model.joblib")
m2.predict(X[:3])                  # → array([0, 0, 0])
```

---

### 3. Hashing a Model's Configuration — `p03`

**What it is:** A deterministic fingerprint of a model's
hyperparameters. Same params → same hash; any param differs →
different hash. Used to dedupe runs and answer "have I trained this
exact config before?"

**Why it exists:** "Run #47 used config hash `9f2c`" is checkable;
"I think I used C=1.0" isn't. Config hashing was invented so runs
can be deduped, cached, and verified — the fingerprint is the
contract that two configs are identical. Two keys make it stable:
`sort_keys=True` (dict order doesn't change the string) and
`default=str` (non-JSON values like tuples or class refs get
stringified instead of crashing).

**Where it's used:** Registries and caches key on this — dedupe in
experiment trackers, cache keys in training pipelines, config
comparison in CI.

**What goes wrong without it:**
- Python's builtin `hash()` is NOT stable across processes (it's
  salted per-run for security) — `hash(obj)` today ≠ `hash(obj)` in
  tomorrow's process. Always `hashlib` (md5/sha256) for anything
  that must match later.
- No `sort_keys` → `{"C":1,"max_iter":200}` and
  `{"max_iter":200,"C":1}` hash differently despite being the same
  config → phantom "new" configs, cache misses.
- No `default=str` → a tuple or class reference in params crashes
  `json.dumps` mid-run.

**Worked example:**
```python
a = LogisticRegression(C=1.0, max_iter=200)
b = LogisticRegression(C=1.0, max_iter=200)   # same config
c = LogisticRegression(C=5.0, max_iter=200)   # different C

model_hash(a) → e.g. "9f2c..."   (32 hex chars)
model_hash(b) → "9f2c..."        # identical
model_hash(c) → "7ad1..."        # different

the pipeline: get_params() → {"C": 1.0, "max_iter": 200, ...}
  → json.dumps(..., sort_keys=True, default=str)  # canonical string
  → md5(string.encode()).hexdigest()
```

**Code:**
```python
def model_hash(model):
    s = json.dumps(model.get_params(), sort_keys=True, default=str)
    return hashlib.md5(s.encode()).hexdigest()
```

**Expected output:**
```python
model_hash(a) == model_hash(b)     # → True   (same config → same hash)
model_hash(a) == model_hash(c)     # → False  (different C)
model_hash(a)                      # → "9f2c..."  (32 hex chars)
```

---

## Medium

### 4. The ExperimentTracker Class — `p01`

**What it is:** p01's `log_run` works, but real tracking is a
LIFECYCLE: start a run → log params/metrics as training progresses →
end the run and flush to disk. That's the mlflow pattern
(`with mlflow.start_run(): ...`).

**Why it exists:** Metrics aren't known until training finishes —
you log params at the start and metrics at the end (or per epoch).
The open-run-then-flush pattern was invented so one crash
mid-training doesn't leave a half-written line in the log: nothing
hits disk until `end_run()`.

**Where it's used:** `mlflow.start_run()`, wandb runs, Sacred/Neptune
experiment objects — the start→log→end lifecycle is the universal
tracker API.

**What goes wrong without it:**
- Guard `log_*` with "no active run" errors — calling `log_param`
  before `start_run` should fail loudly, not silently write
  nowhere. A silent no-op means your run logs nothing and you find
  out after the experiment.
- `end_run` must CLEAR `self._run`; leaving it set means the next
  `start_run` could leak old metrics into a new run.
- Writing each metric line-by-line as it arrives → a crash mid-run
  leaves a half-record in the log, indistinguishable from a real
  run.

**Worked example:**
```python
t = ExperimentTracker()
t.start_run("lr-v1")          # opens {"timestamp": ..., "name": "lr-v1",
                            #         "params": {}, "metrics": {}}
t.log_param("C", 1.0)         # run["params"]["C"] = 1.0
t.log_metric("accuracy", 0.95)  # run["metrics"]["accuracy"] = 0.95
t.end_run()                   # appends ONE line to runs.jsonl,
                            # clears the open run, returns the dict
→ {'timestamp': 1717..., 'name': 'lr-v1',
   'params': {'C': 1.0}, 'metrics': {'accuracy': 0.95}}
```

**Code:**
```python
class ExperimentTracker:
    def __init__(self, path=None):
        self.path = path or os.path.join(
            os.path.dirname(__file__), "runs.jsonl")
        self._run = None

    def start_run(self, name):
        self._run = {"timestamp": time.time(), "name": name,
                     "params": {}, "metrics": {}}

    def log_param(self, key, value):
        if self._run is None:
            raise RuntimeError("no active run")
        self._run["params"][key] = value

    def log_metric(self, key, value):
        if self._run is None:
            raise RuntimeError("no active run")
        self._run["metrics"][key] = value

    def end_run(self):
        with open(self.path, "a") as f:
            f.write(json.dumps(self._run) + "\n")
        run, self._run = self._run, None
        return run
```

**Expected output:**
```python
t = ExperimentTracker()
t.start_run("lr-v1")
t.log_param("C", 1.0); t.log_metric("accuracy", 0.95)
t.end_run()
# → {'timestamp': 1717..., 'name': 'lr-v1',
#    'params': {'C': 1.0}, 'metrics': {'accuracy': 0.95}}
t.log_param("x", 1)     # → RuntimeError: no active run
```

---

### 5. The Model Registry — `p02`

**What it is:** A registry answers "what models do we have, which
version is which, and how good is each?" It's a JSON file mapping
`"name-vN"` → metadata, sitting next to the saved `.joblib` files.

**Why it exists:** Teams need to answer "which model is in prod?"
and "can we roll back to v1?" — questions a folder of anonymous
`.joblib` files can't answer. The registry was invented as the
versioned, queryable memory of every model ever trained. Same
config hash on v1 and v2 but different metrics? That's a data or
code change talking — the hash lets you see it (hard/p01 makes that
check rigorous).

**Where it's used:** MLflow Model Registry, SageMaker Model
Registry, Hugging Face model repos — every production team keeps
one.

**What goes wrong without it:**
- Version counts entries for THAT name only — `"iris-v1"`,
  `"iris-v2"`; a `"mnist-v1"` entry doesn't bump iris's counter.
  Count keys starting with `f"{name}-v"`, or different model
  families corrupt each other's versioning.
- No registry → "model_final_v2_REAL.joblib" chaos: nobody knows
  which file is deployed or whether rollback is possible.

**Worked example:**
```python
m = LogisticRegression(max_iter=200).fit(X, y)
e1 = register_model(m, "iris", {"accuracy": 0.93})
e2 = register_model(m, "iris", {"accuracy": 0.95})

e1["version"] → 1    e2["version"] → 2

registry.json after both:
{
  "iris-v1": {"name": "iris", "version": 1, "hash": "9f2c...",
              "metrics": {"accuracy": 0.93}, "timestamp": ...,
              "model_path": ".../iris_v1.joblib"},
  "iris-v2": {"name": "iris", "version": 2, "hash": "9f2c...",
              "metrics": {"accuracy": 0.95}, "timestamp": ...,
              "model_path": ".../iris_v2.joblib"}
}
version = (# existing "iris-v*" keys) + 1
```

**Code:**
```python
def register_model(model, name, metrics):
    d = os.path.dirname(__file__)
    reg_path = os.path.join(d, "registry.json")
    reg = json.load(open(reg_path)) if os.path.exists(reg_path) else {}
    version = sum(1 for k in reg if k.startswith(f"{name}-v")) + 1
    model_path = os.path.join(d, f"{name}_v{version}.joblib")
    joblib.dump(model, model_path)
    h = hashlib.md5(json.dumps(
        model.get_params(), sort_keys=True).encode()).hexdigest()
    entry = {"name": name, "version": version, "hash": h,
             "metrics": metrics, "timestamp": time.time(),
             "model_path": model_path}
    reg[f"{name}-v{version}"] = entry
    json.dump(reg, open(reg_path, "w"), indent=2)
    return entry
```

**Expected output:**
```python
e1 = register_model(m, "iris", {"accuracy": 0.93})
e1["version"]                      # → 1
e2 = register_model(m, "iris", {"accuracy": 0.95})
e2["version"]                      # → 2
# registry.json now has keys "iris-v1" and "iris-v2", each pointing
# at its own .joblib file
```

---

### 6. Comparing Runs (pick the best) — `p03`

**What it is:** Tracking is useless unless you can answer "which run
won?" Scan every line of `runs.jsonl`, keep the run with the highest
value for a chosen metric.

**Why it exists:** A pile of run records without a "best" query is
just a diary. Comparison was invented to turn the log into a
decision: "best" is always relative to a metric — highest accuracy
might come with terrible latency, so the metric name is a
parameter, not hardcoded.

**Where it's used:** `mlflow.search_runs` +
`order_by("metrics.accuracy DESC")` minus the database —
leaderboards, model selection, hyperparameter sweeps.

**What goes wrong without it:**
- `run.get("metrics", {})` — some runs may lack a `metrics` key
  entirely, and `run["metrics"]` would KeyError mid-scan, killing
  the whole comparison on the one malformed line.
- Return `None` (not a crash) when nothing qualifies — an empty
  file or all-missing-metric shouldn't raise.
- Comparing on a metric the run didn't record → silently wrong
  "best"; skipping runs missing the metric is the correct behavior.

**Worked example:**
```
runs.jsonl:
  {"name": "lr-baseline", "metrics": {"accuracy": 0.90}, ...}
  {"name": "lr-strong",   "metrics": {"accuracy": 0.97}, ...}
  {"name": "lr-tuned",    "metrics": {"accuracy": 0.93}, ...}
  {"name": "svm-test",    "metrics": {"f1": 0.88}, ...}   ← no accuracy!

compare_runs("runs.jsonl", metric="accuracy")
  → the "lr-strong" dict; svm-test is skipped (metric missing)

compare_runs("empty.jsonl") → None
```

**Code:**
```python
def compare_runs(file, metric="accuracy"):
    best = None
    for line in open(file):
        line = line.strip()
        if not line:
            continue
        run = json.loads(line)
        if metric not in run.get("metrics", {}):
            continue
        if best is None or run["metrics"][metric] \
                > best["metrics"][metric]:
            best = run
    return best
```

**Expected output:**
```python
compare_runs("runs.jsonl", metric="accuracy")
# → {'name': 'lr-strong', 'metrics': {'accuracy': 0.97}, ...}
compare_runs("runs.jsonl", metric="f1")
# → {'name': 'svm-test', 'metrics': {'f1': 0.88}, ...}
compare_runs("empty.jsonl")        # → None
```

---

## Hard

### 7. Dataset Version Hash — `p01`

**What it is:** Reproducibility needs THREE pins: code,
hyperparameters, and DATA. A data hash fingerprints a dataset —
shape plus sample values — so any silent change (new rows, a fixed
preprocessing bug) produces a different hash.

**Why it exists:** "The model got 0.96" is meaningless if nobody can
say WHICH data produced it. Data hashing was invented as DVC /
lakeFS / delta-table versioning in miniature: one hash per dataset
version. If the data pipeline changes overnight, next morning's
hash differs and your reproduction check (p02) screams instead of
silently comparing apples to oranges.

**Where it's used:** Data versioning tools (DVC, lakeFS, Pachyderm),
training-data audits, and reproducibility checks in regulated
industries.

**What goes wrong without it:**
- Hash a fingerprint (shape + head/tail samples), not the entire
  dataset — full-data hashing works but is slow on gigabytes.
- Rounding to 6 decimals matters: float noise like
  `0.30000000000000004` vs `0.3` would flip the hash on identical
  data → phantom "data changed" alerts.
- No data pin → "we retrained on the same data" is unfalsifiable —
  a preprocessing change slips in and metrics move for reasons
  nobody can see.

**Worked example:**
```python
X, y = load_iris(return_X_y=True)          # 150×4, 150 labels
data_version_hash(X, y)     → "a4f8..."

data_version_hash(X[:100], y[:100])  → "72be..."   # different!
# the payload that gets hashed:
{"n_rows": 150, "n_cols": 4, "n_labels": 150,
 "x_head": [[5.1, 3.5, 1.4, 0.2], ...first 5 rows...],
 "x_tail": [...last 5 rows...],
 "y_head": [0, 0, 0, 0, 0], "y_tail": [2, 2, 2, 2, 2]}
```

**Code:**
```python
def data_version_hash(X, y):
    if hasattr(X, "tolist"): X = X.tolist()    # numpy → plain lists
    if hasattr(y, "tolist"): y = y.tolist()
    payload = {
        "n_rows": len(X), "n_cols": len(X[0]) if X else 0,
        "n_labels": len(y),
        "x_head": [[round(float(v), 6) for v in r] for r in X[:5]],
        "x_tail": [[round(float(v), 6) for v in r] for r in X[-5:]],
        "y_head": [int(v) for v in y[:5]],
        "y_tail": [int(v) for v in y[-5:]],
    }
    return hashlib.md5(
        json.dumps(payload, sort_keys=True).encode()).hexdigest()
```

**Expected output:**
```python
data_version_hash(X, y)               # → "a4f8..."  (32 hex chars)
data_version_hash(X, y)               # → same value every call
data_version_hash(X[:100], y[:100])   # → different hash
```

---

### 8. Reproducing a Run — `p02`

**What it is:** A logged run is only trustworthy if you can REPRODUCE
it: same data + same params + same seed → same metrics. This function
re-runs the experiment and reports whether the claim holds up.

**Why it exists:** This is the audit behind every "our model
achieves X" claim. If retraining doesn't reproduce the metric, the
run log was incomplete — a missing seed, an unlogged param, a
dataset that drifted. Reproduction checks were invented to catch
that in CI instead of in a customer escalation. The params MUST
include `random_state` — without it, sklearn's solver init varies
run to run.

**Where it's used:** CI reproduction gates, audit trails, paper
replication checks, "can we trust this registry entry" validation.

**What goes wrong without it:**
- Even when `data_ok` is False, still retrain and report `actual` —
  the number is informative ("hash mismatch AND the metric moved"
  vs "hash mismatch but same result" are very different bugs).
  `match` just ANDs in `data_ok` at the end.
- Missing `random_state` in logged params → the "same" training
  gives a different score every run → irreproducible by
  construction.
- No reproduction check → a typo'd or incomplete log entry ships as
  fact; nobody discovers the 0.96 was really 0.91 until prod.

**Worked example:**
```python
reproduce_run("runs.jsonl", "run-1")

steps inside:
  1. scan jsonl → find run with run_id "run-1"
  2. X, y = make_dataset()  → canonical dataset
     data_version_hash(X, y) == run["data_hash"]?  → data_ok
  3. split (test_size=0.25, random_state=42),
     retrain LogisticRegression(**run["params"])
  4. actual = accuracy on test split

result:
  {'found': True, 'data_ok': True,
   'expected': 0.96, 'actual': 0.96, 'match': True}
  # match = data_ok AND |expected - actual| <= tol (0.01)
```

**Code:**
```python
def reproduce_run(run_file, run_id, tol=0.01):
    run = next((json.loads(l) for l in open(run_file)
                if json.loads(l).get("run_id") == run_id), None)
    if run is None:
        return {"found": False, "data_ok": False,
                "expected": None, "actual": None, "match": False}
    X, y = make_dataset()
    data_ok = data_version_hash(X, y) == run["data_hash"]
    Xtr, Xte, ytr, yte = train_test_split(
        X, y, test_size=0.25, random_state=42)
    m = LogisticRegression(**run["params"]).fit(Xtr, ytr)
    actual = m.score(Xte, yte)
    expected = run["metrics"]["accuracy"]
    return {"found": True, "data_ok": data_ok, "expected": expected,
            "actual": actual,
            "match": data_ok and abs(expected - actual) <= tol}
```

**Expected output:**
```python
reproduce_run("runs.jsonl", "run-1")
# → {'found': True, 'data_ok': True, 'expected': 0.96,
#    'actual': 0.96, 'match': True}
reproduce_run("runs.jsonl", "run-missing")
# → {'found': False, 'data_ok': False, 'expected': None,
#    'actual': None, 'match': False}
```

---

### 9. CI Gate for Models — `p03`

**What it is:** Software CI blocks merges when tests fail; ML CI
blocks DEPLOYS when metrics drop. The gate checks each metric against
a minimum threshold and reports EVERY failure — never just asserts
the first one.

**Why it exists:** A model that misses the bar must never ship —
this gate was invented as the automated guardrail between
"notebook experiment" and "production deploy." Reporting ALL
failures (not failing fast) is a deliberate design choice: an
engineer seeing three failing metrics debugs once, not three times.

**Where it's used:** Model deploy pipelines — the check between
"training finished" and "new version promoted" in every mature
MLOps setup.

**What goes wrong without it:**
- A missing metric is a FAILURE (`"missing metric: recall"`), not
  a skip — silently ignoring absent metrics means a renamed metric
  key would quietly disable the safety check forever.
- Fail-fast (assert on first failure) → fix metric A, re-run, hit
  metric B, fix, re-run, hit metric C — three deploy cycles instead
  of one report.
- No gate → a regression ships automatically; the first alert is
  the production dashboard tanking.

**Worked example:**
```python
ci_gate({"accuracy": 0.9, "f1": 0.85},
        {"accuracy": 0.8, "f1": 0.9})
# accuracy: 0.9 >= 0.8 ✓      f1: 0.85 < 0.9 ✗
→ {'pass': False, 'failures': ['f1: 0.85 < 0.9']}

ci_gate({"accuracy": 0.9}, {"accuracy": 0.8, "recall": 0.7})
→ {'pass': False, 'failures': ['missing metric: recall']}

ci_gate({"accuracy": 0.95, "f1": 0.91}, {"accuracy": 0.8, "f1": 0.9})
→ {'pass': True, 'failures': []}
```

**Code:**
```python
def ci_gate(metrics, thresholds):
    failures = []
    for name, req in thresholds.items():
        if name not in metrics:
            failures.append(f"missing metric: {name}")
        elif metrics[name] < req:
            failures.append(f"{name}: {metrics[name]} < {req}")
    return {"pass": not failures, "failures": failures}
```

**Expected output:**
```python
ci_gate({"accuracy": 0.9, "f1": 0.85},
        {"accuracy": 0.8, "f1": 0.9})
# → {'pass': False, 'failures': ['f1: 0.85 < 0.9']}
ci_gate({"accuracy": 0.9}, {"accuracy": 0.8, "recall": 0.7})
# → {'pass': False, 'failures': ['missing metric: recall']}
ci_gate({"accuracy": 0.95, "f1": 0.91},
        {"accuracy": 0.8, "f1": 0.9})
# → {'pass': True, 'failures': []}
```

---

## Done with concepts? → Try `easy/p01-log-run.py`
