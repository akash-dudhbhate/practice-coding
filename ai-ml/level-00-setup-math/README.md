# Level 00 — Setup & Math Foundations

> **Math level:** 10th grade is enough. See [MATH-YOU-NEED.md](../MATH-YOU-NEED.md) — it explains every symbol used here.

## What You'll Learn
- Verify your Python environment works
- Vectors and dot products (the math inside every ML model)
- Mean, variance, standard deviation
- Basic probability intuition

## Why This Level Exists
Every ML model is just math on vectors. If you can:
  - multiply vectors (dot product)
  - understand mean/variance
  - reason about probability
...then everything later makes sense instead of feeling like magic.

## Prerequisites
- Python installed (3.10+)

---

## Problems

### Easy
1. `easy/p01-env-check.py` — `check_env()` → verify numpy/pandas/sklearn work
2. `easy/p02-dot-product.py` — `dot(a, b)` → vector dot product by hand
3. `easy/p03-mean-variance.py` — `stats(data)` → mean, variance, std

### Medium
4. `medium/p01-weighted-sum.py` — `weighted_sum(x, w, b)` → the core of every neuron
5. `medium/p02-normalize.py` — `normalize(data)` → min-max scaling by hand
6. `medium/p03-distance.py` — `euclidean(a, b)` → distance between points

### Hard
7. `hard/p01-gradient-intuition.py` — `descend()` → walk downhill on a parabola
8. `hard/p02-coin-bayes.py` — `bayes(...)` → Bayes' theorem calculation
9. `hard/p03-matrix-multiply.py` — `matmul(A, B)` → matrix multiplication by hand

### Project
`project/` — Build a tiny "prediction engine" using only a weighted sum.

## Verify

```bash
python3 check.py easy/p01
python3 check.py all
```
