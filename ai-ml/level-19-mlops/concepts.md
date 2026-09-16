# Level 19 — Concepts Reference

## Easy

### Experiment Tracking (runs.jsonl)
- One JSON object per line = one training run
- Minimum fields: `timestamp`, `name`, `params`, `metrics`
- Append-only (`open(path, "a")`) → never lose history
- This is what mlflow/wandb do — just with a UI on top

### Model Persistence
- `joblib.dump(model, path)` → save; `joblib.load(path)` → load
- Registry = model file + metadata, keep them side by side

### Model Hash
- `model.get_params()` → dict of hyperparameters
- `json.dumps(params, sort_keys=True, default=str)` → stable string
- `hashlib.md5(s.encode()).hexdigest()` → deterministic ID
- Same params → same hash → dedupe / lookup in registry

## Medium

### ExperimentTracker Class
- `start_run(name)` → opens a run dict in memory
- `log_param(k, v)` / `log_metric(k, v)` → fill it
- `end_run()` → write one line to runs.jsonl
- Wraps the easy/p01 pattern behind a clean API

### Model Registry
- `registry.json`: `{"name-v1": {name, version, hash, metrics, timestamp}, ...}`
- Version = count existing entries for that name + 1
- Save the model file as `{name}_v{version}.joblib`
- Lets you answer: "which model is in prod? can we roll back?"

### Compare Runs
- Load every line of runs.jsonl, keep the max by one metric
- "Best" is always relative to a chosen metric — pass it in

## Hard

### Data Versioning
- Params + code aren't enough — the DATA must be pinned too
- Hash: shape + head/tail sample values of X and y
- Any change to the dataset → different hash → reproducibility alarm

### Reproduce a Run
- Recipe: logged params + data hash + fixed seeds → same metrics
- Steps: find run → rebuild data → check hash → retrain →
  compare metrics within tolerance
- If it doesn't reproduce, the run log was incomplete

### CI Gate for ML
- Like unit tests, but for metrics: `accuracy >= 0.85` etc.
- Return `{"pass": bool, "failures": [str]}` — never just assert;
  report WHICH thresholds failed
- Blocks bad models from reaching production automatically
