# Level 19 — MLOps

## What You'll Learn
- Experiment tracking: log runs to `runs.jsonl`
- Model persistence: save/load with joblib
- Model identity: deterministic hash of hyperparameters
- `ExperimentTracker` class (start_run / log_param / log_metric / end_run)
- Model registry: versioned entries in `registry.json`
- Compare runs, pick the best by metric
- Data versioning: hash a dataset for reproducibility
- Reproduce a run: retrain from logged params, verify metrics
- CI for ML: gate deployments on metric thresholds

We teach the *patterns* with sklearn + joblib + json — the same ideas
power mlflow, wandb, and every production ML platform.

## Prerequisites
- Level 04–05 (train + evaluate sklearn models)
- `pip install scikit-learn joblib`

## Problems

### Easy
1. `easy/p01-log-run.py` — `log_run(name, params, metrics)` → append to runs.jsonl
2. `easy/p02-save-model.py` — `save_model()` / `load_model()` → joblib round-trip
3. `easy/p03-model-hash.py` — `model_hash(model)` → deterministic model ID

### Medium
4. `medium/p01-experiment-tracker.py` — `ExperimentTracker` → run lifecycle API
5. `medium/p02-register-model.py` — `register_model()` → registry.json + versions
6. `medium/p03-compare-runs.py` — `compare_runs(file)` → best run by metric

### Hard
7. `hard/p01-data-hash.py` — `data_version_hash(X, y)` → dataset fingerprint
8. `hard/p02-reproduce-run.py` — `reproduce_run(file, id)` → retrain + verify
9. `hard/p03-ci-gate.py` — `ci_gate(metrics, thresholds)` → pass/fail gate

### Project
`project/` — Mini MLOps pipeline: train → track → register → CI gate.

## Verify

```bash
python3 check.py easy/p01
python3 check.py all
```
