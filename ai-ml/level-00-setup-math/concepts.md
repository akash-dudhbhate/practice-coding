# Level 00 — Concepts (Detailed Explanations)

Read each section BEFORE attempting its problem. Each concept has:
what it is in plain words → a worked example with real numbers →
why ML cares → the code → what confuses beginners.

---

## Easy

### 1. Checking Your Environment

**What it is:** Before doing any ML, you verify your tools are
installed. Every Python library has a `.__version__` attribute.

**Worked example:**
```python
import numpy as np
print(np.__version__)   # e.g. 2.2.6
```
If this prints a number, NumPy works. If you get
`ModuleNotFoundError`, the library isn't installed — run
`pip install -r ../requirements.txt` from `ai-ml/`.

**Why ML cares:** 90% of "my code doesn't work" is actually
"my environment is broken." Pros check first.

**Common confusion:** `import sklearn` fails even when
`pip install scikit-learn` worked — the pip name and import
name differ. That's normal.

---

### 2. Dot Product — `p02`

**What it is:** Multiply two lists element-by-element, then add
the results into ONE number.

**Worked example:**
```
a = [1, 2, 3]
b = [4, 5, 6]

a · b = (1×4) + (2×5) + (3×6)
      =   4   +  10   +  18
      =  32
```

**Why ML cares:** This single operation is THE neuron. A neuron
takes inputs `[x1,x2,x3]`, has weights `[w1,w2,w3]`, and computes
`inputs·weights`. Every layer of every neural network is just
thousands of dot products. Also: cosine similarity in RAG is a
normalized dot product.

**Code:**
```python
def dot(a, b):
    return sum(x * y for x, y in zip(a, b))
```

**Common confusion:** Dot product is NOT `[4, 10, 18]` (that's
element-wise multiply). The SUM makes it a single number: 32.

---

### 3. Mean, Variance, Std Dev — `p03`

**What it is:** Three numbers that describe a dataset.
- **Mean** — where the center is
- **Variance** — how far values spread from the center (squared units)
- **Std** — same spread, in original units (sqrt of variance)

**Worked example:**
```
data = [2, 4, 6]
mean  = (2+4+6)/3 = 4
var   = ((2-4)² + (4-4)² + (6-4)²) / 3
      = (4 + 0 + 4) / 3 = 8/3 ≈ 2.667
std   = √2.667 ≈ 1.633
```

**Why ML cares:** Features on wildly different scales (age 0-100,
income 0-1,000,000) confuse models — you normalize using mean/std.
Variance also shows up in bias-variance tradeoff (level-01) and
PCA (levels 07, 20).

**Code:**
```python
import statistics
statistics.mean([2,4,6])      # 4
statistics.pvariance([2,4,6]) # 2.667 (population)
statistics.pstdev([2,4,6])    # 1.633
```

**Common confusion:** `variance` vs `pstdev` — NumPy's `np.var`
divides by n (population); `statistics.variance` divides by n-1
(sample). Use `np.var`/`np.std` in this level.

---

## Medium

### 4. Weighted Sum = The Neuron — `p01`

**What it is:** A dot product plus a bias number:
`output = (inputs · weights) + bias`

**Worked example:**
```
inputs  = [10, 20, 30]
weights = [0.5, 0.3, 0.2]
bias    = 0.1

output = (10×0.5 + 20×0.3 + 30×0.2) + 0.1
       = (5 + 6 + 6) + 0.1
       = 17.1
```

**Why ML cares:** This IS a neuron — the literal definition.
A neural network layer = a matrix of these (each row = one
neuron's weights). When you "train" a model, you're tuning
weights and biases until outputs match reality.

**Code:**
```python
def weighted_sum(inputs, weights, bias):
    return sum(x*w for x, w in zip(inputs, weights)) + bias
```

**Common confusion:** The bias lets the neuron output non-zero
even when all inputs are 0 — like the intercept in y = mx + b.

---

### 5. Normalization (min-max scaling) — `p02`

**What it is:** Squash numbers into [0, 1] so features compare
fairly. Formula: `(x - min) / (max - min)`

**Worked example:**
```
data = [10, 20, 30]   →  min=10, max=30, range=20
10 → (10-10)/20 = 0.0
20 → (20-10)/20 = 0.5
30 → (30-30)/20 = 1.0
```

**Why ML cares:** Gradient descent and distance-based models
(KNN, K-Means) treat "bigger numbers" as "more important."
Without normalization, a salary column would drown out an
age column purely because of scale, not meaning.

**Code:**
```python
def normalize(vals):
    lo, hi = min(vals), max(vals)
    if hi == lo:                    # edge case!
        return [0.0] * len(vals)
    return [(v - lo) / (hi - lo) for v in vals]
```

**Common confusion:** If all values are equal, max-min = 0 →
division by zero crash. Always guard it.

---

### 6. Euclidean Distance — `p03`

**What it is:** Straight-line distance between two points:
`sqrt(Σ(aᵢ - bᵢ)²)`. In 2D it's the Pythagorean theorem.

**Worked example:**
```
a = [0, 0]   b = [3, 4]
d = √((0-3)² + (0-4)²) = √(9 + 16) = √25 = 5
```

**Why ML cares:** "Similar" in ML = "close together."
KNN classifies by nearest neighbors; K-Means assigns points
to the closest centroid; RAG finds "most similar documents"
this way (with cosine instead).

**Code:**
```python
import math
def euclidean(a, b):
    return math.sqrt(sum((x-y)**2 for x, y in zip(a, b)))
```

**Common confusion:** It works in ANY number of dimensions —
[0,0,0] to [1,1,1] is √3, not just 2D geometry.

---

## Hard

### 7. Gradient Descent — `p01`

**What it is:** To find a function's minimum, look at the slope
(derivative) where you are, then take a step DOWNHILL:
`x_new = x - learning_rate × slope`

**Worked example:** minimize f(x) = x². Slope f'(x) = 2x.
Start x=4, lr=0.1:
```
step 1: x = 4   - 0.1×8   = 3.2
step 2: x = 3.2 - 0.1×6.4 = 2.56
step 3: x = 2.56- 0.1×5.12= 2.048
... converges to 0 (the minimum)
```

**Why ML cares:** This IS how every neural network learns.
"Training" = compute the slope of the loss w.r.t. each weight,
step downhill, repeat millions of times. Levels 08, 09, 17
all use this.

**Code:**
```python
def descend(f, df, x, lr=0.1, iters=50):
    for _ in range(iters):
        x -= lr * df(x)
    return x
```

**Common confusion:** lr too big → overshoot and diverge.
lr too small → takes forever. There's no "correct" lr —
you tune it (level-05 covers this).

---

### 8. Bayes' Theorem — `p02`

**What it is:** Update a belief when you get new evidence:
`P(A|B) = P(B|A)·P(A) / P(B)`

**Worked example (the classic medical test):**
```
Disease rate: P(sick) = 0.01       (1% of people)
Test accuracy: P(+|sick) = 0.99    (catches 99% of sick)
False alarms:  P(+|healthy) = 0.05 (5% of healthy test +)

You test positive. P(sick|+) = ?

P(+) = P(+|sick)·P(sick) + P(+|healthy)·P(healthy)
     = 0.99×0.01 + 0.05×0.99 = 0.0099 + 0.0495 = 0.0594

P(sick|+) = 0.0099 / 0.0594 ≈ 0.167   → only 16.7%!
```

**Why ML cares:** Naive Bayes classifiers (spam filters!) use
this directly. More importantly, it teaches that base rates
matter — a "99% accurate" test on a rare thing is mostly
false alarms.

**Common confusion:** People intuitively think P(sick|+) ≈ 99%.
The false positives on the huge healthy population swamp the
true positives on the tiny sick population.

---

### 9. Matrix Multiplication — `p03`

**What it is:** C[i][j] = dot product of row i of A with
column j of B. Rule: A's columns must equal B's rows.
(m×n) × (n×p) → (m×p)

**Worked example:**
```
A = [[1,2],[3,4]]   B = [[5,6],[7,8]]

C[0][0] = 1×5 + 2×7 = 19
C[0][1] = 1×6 + 2×8 = 22
C[1][0] = 3×5 + 4×7 = 43
C[1][1] = 3×6 + 4×8 = 50
C = [[19,22],[43,50]]
```

**Why ML cares:** A neural network layer IS a matrix multiply:
`output = X @ W + b`. One matrix multiply computes ALL neurons
for ALL inputs at once — that's why GPUs (parallel matmul
machines) dominate AI.

**Code:**
```python
import numpy as np
C = np.array(A) @ np.array(B)   # @ = matmul
```

**Common confusion:** A@B ≠ B@A — matrix multiplication is NOT
commutative. And `A * B` in NumPy is element-wise (different
thing entirely).

---

## Done with concepts? → Try `easy/p01-env-check.py`
