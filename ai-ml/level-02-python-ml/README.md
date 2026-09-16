# Level 02 Python Ml — Python for ML

## What You'll Learn
- NumPy arrays and operations
- Pandas DataFrames
- Data loading and inspection
- Missing value handling
- Feature scaling
- Train/test splitting

## Prerequisites
- Previous levels completed
- Python basics

## How This Level Works

Each problem has:
1. **CONCEPT** — the idea you need to understand
2. **PROBLEM** — what to build
3. **TRY THIS INPUT** — test code to verify your solution
4. **EXPECTED OUTPUT** — what it should print
5. **AUTO-CHECK** — run `check.py` to verify automatically

Start with `easy/` problems, then `medium/`, then `hard/`, then the project.

---

## Problems

### Easy
1. `easy/p01-create-array.py` — Create a 4x5 NumPy array of random integers (0-100) with a f...
2. `easy/p02-load-csv.py` — Load a CSV file into a pandas DataFrame. Print the first 5 r...
3. `easy/p03-fill-missing.py` — Given a DataFrame with NaN values, fill numeric columns with...

### Medium
4. `medium/p01-preprocess-pipeline.py` — Build a preprocessing pipeline: impute missing values, scale...
5. `medium/p02-detect-outliers.py` — Detect outliers using IQR method. Cap them and return the cl...
6. `medium/p03-mixed-types.py` — Handle a DataFrame with numeric, categorical, and datetime c...

### Hard
7. `hard/p01-data-leakage.py` — Prevent data leakage: split FIRST, then fit preprocessing on...
8. `hard/p02-column-transformer.py` — Use ColumnTransformer to apply different preprocessing to nu...
9. `hard/p03-stratified-split.py` — Create imbalanced data (95/5), split with and without strati...

### Project
`project/` — Clean a real messy dataset — handle missing values, encode categories, scale features, train a model, evaluate.

---

## Verify Your Work

```bash
# Run a problem
python3 easy/p01-create-array.py

# Check your answer
python3 check.py easy/p01
```

When `check.py` says "PASS", add `# DONE` to the first line and move on.
