# Level 06 — Advanced ML

> **Math level:** 10th grade is enough. See [MATH-YOU-NEED.md](../MATH-YOU-NEED.md) — it explains every symbol used here.

## What You'll Learn
- Polynomial features (nonlinear data with linear models)
- One-hot encoding, feature scaling
- Manual oversampling for imbalanced data
- Feature importance filtering, PCA
- Custom sklearn transformers, feature engineering pipelines
- class_weight='balanced' for imbalanced data

## Prerequisites
- Level 05 (evaluation)

## Problems

### Easy
1. `easy/p01-polynomial-features.py` — `compare_linear_poly()` → linear vs poly R²
2. `easy/p02-label-encode.py` — `encode()` → one-hot encode
3. `easy/p03-feature-scale.py` — `scale_features()` → StandardScaler

### Medium
4. `medium/p01-smote-imbalance.py` — `oversample(X, y)` → manual oversampling
5. `medium/p02-feature-importance.py` — `select_top()` → top-5 features
6. `medium/p03-pca-reduce.py` — `reduce_pca()` → 10D → 3D

### Hard
7. `hard/p01-custom-transformer.py` — `LogTransformer` → custom pipeline step
8. `hard/p02-feature-engineering-pipeline.py` — `engineer_and_train()` → new features
9. `hard/p03-imbalanced-ensemble.py` — `compare_balanced()` → class_weight effect

### Project
`project/` — Build a full feature engineering pipeline on real data.

## Verify

```bash
python3 check.py easy/p01
python3 check.py all
```
