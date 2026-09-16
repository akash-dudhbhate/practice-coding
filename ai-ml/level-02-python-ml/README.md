# Level 02 — Python for ML

## What You'll Learn
- NumPy arrays — the foundation of all ML data
- pandas DataFrames — loading, inspecting, cleaning data
- Filling missing values (imputation)
- Scaling features and encoding categories
- Pipelines and ColumnTransformer
- Preventing data leakage

## Prerequisites
- Level 01 complete
- Python basics (functions, lists, dicts)

---

## Problems

### Easy
1. `easy/p01-create-array.py` — `create_array()` → 4×5 random array, print stats
2. `easy/p02-load-csv.py` — `load_data()` → build a DataFrame
3. `easy/p03-fill-missing.py` — `fill_missing()` → impute NaN correctly

### Medium
4. `medium/p01-preprocess-pipeline.py` — `build_pipeline()` → sklearn Pipeline
5. `medium/p02-detect-outliers.py` — `detect_outliers(data)` → IQR capping
6. `medium/p03-mixed-types.py` — `process()` → datetime + encode + scale

### Hard
7. `hard/p01-data-leakage.py` — `train_clean()` → split-first pipeline
8. `hard/p02-column-transformer.py` — `build()` → mixed preprocessing
9. `hard/p03-stratified-split.py` — `compare_splits()` → stratify=y

### Project
`project/` — Clean a real messy dataset end-to-end.

---

## Verify Your Work

```bash
python3 check.py easy/p01    # one problem
python3 check.py all         # all 9 problems
```

When it says PASS, add `# DONE` to the first line of your file.
