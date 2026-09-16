# Level 00 — Concepts Reference

## Easy

### Environment
- `import numpy/pandas/sklearn` + `.__version__` → verify install

### Dot Product
- `a · b = Σ aᵢbᵢ` — the atom of all ML. Every neuron does this.
- `sum(x*y for x,y in zip(a,b))`

### Mean / Variance / Std
- mean = center; variance = spread²; std = spread
- `variance = Σ(x - mean)² / n`

## Medium

### Weighted Sum (the neuron)
- `output = inputs·weights + bias` — literally what a neuron computes
- Every layer of a neural network = matrix of these

### Normalization
- `(x - min) / (max - min)` → scale to [0, 1]
- Guard the edge case: max == min → return zeros

### Euclidean Distance
- `sqrt(Σ(aᵢ - bᵢ)²)` — straight-line distance
- Used by KNN, K-Means, and vector similarity (RAG)

## Hard

### Gradient Descent
- `x -= lr × f'(x)` — walk opposite the slope to find the minimum
- This IS how models learn — everything else is detail

### Bayes' Theorem
- `P(sick|+) = P(+|sick)·P(sick) / P(+)` 
- Rare events + imperfect tests → surprising results (8.8%!)

### Matrix Multiplication
- `C[i][j] = A[i]·B[:,j]` — row × column
- Neural networks = giant chains of matrix multiplies
