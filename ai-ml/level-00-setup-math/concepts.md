# Level 00 — Concepts (Detailed Explanations)

> Read each section BEFORE attempting its problem. Each concept explains:
> **What it is** · **Why it exists** · **Where it's used** ·
> **What goes wrong** without it · worked example · code ·
> expected output.

---

## Easy

### 1. Checking Your Environment — `p01`

**What it is:** Before doing any ML, you verify your tools are
installed. Every Python library has a `.__version__` attribute.

**Why it exists:** "Is it installed?" is a separate question from
"is my code right?" — you need a way to ask it in one line before
debugging anything else.

**Where it's used:** The first cell of every notebook, every bug
report ("what versions are you on?"), every CI setup script.

**What goes wrong without it:** 90% of "my code doesn't work" is
actually "my environment is broken." Skip the check and you debug
your code for an hour when the real bug is that NumPy was never
installed — `ModuleNotFoundError` hits at the worst time, deep in
a problem.

**Worked example:**
```python
import numpy as np
print(np.__version__)   # e.g. 2.2.6
```
If this prints a number, NumPy works. If you get
`ModuleNotFoundError`, the library isn't installed — run
`pip install -r ../requirements.txt` from `ai-ml/`.

**Code:**
```python
import numpy as np
import pandas as pd
print(np.__version__, pd.__version__)
```

**Expected output:** Two version strings, e.g. `2.2.6 2.2.3`.
Exact numbers depend on your install — any printed versions = pass.

**Watch out:** `import sklearn` fails even when
`pip install scikit-learn` worked — the pip name and import
name differ. That's normal.

---

### 2. Dot Product — `p02`

**What it is:** Multiply two lists element-by-element, then add
the results into ONE number.

**Why it exists:** It's the minimal way to combine "inputs" with
"how much each matters" into a single score — which is exactly
what a neuron does.

**Where it's used:** Every layer of every neural network is
thousands of dot products (`inputs·weights`). Cosine similarity
in RAG is a normalized dot product. Attention in transformers
scores relevance with dot products.

**What goes wrong without it:** Without it you can't compute a
weighted vote — each input would count equally and a useless
feature (house color) would shout as loud as size. And the
classic beginner bug: stopping at `[4, 10, 18]` (element-wise
multiply) instead of summing — the SUM is what makes it one
score: 32.

**Worked example:**
```
a = [1, 2, 3]
b = [4, 5, 6]

a · b = (1×4) + (2×5) + (3×6)
      =   4   +  10   +  18
      =  32
```

**Code:**
```python
def dot(a, b):
    return sum(x * y for x, y in zip(a, b))
```

**Expected output:** `dot([1,2,3], [4,5,6])` → `32` — a single
number, not a list.

---

### 3. Mean, Variance, Std Dev — `p03`

**What it is:** Three numbers that describe a dataset.
- **Mean** — where the center is
- **Variance** — how far values spread from the center (squared units)
- **Std** — same spread, in original units (sqrt of variance)

**Why it exists:** Raw lists of numbers are unreadable — you need
summary statistics to say "where's the center" and "how spread
out" in two numbers.

**Where it's used:** Feature normalization (`(x − mean)/std` is
StandardScaler), the bias-variance tradeoff (level-01), PCA
(levels 07, 20), anomaly detection ("more than 3 std from mean =
weird").

**What goes wrong without it:** Features on wildly different
scales (age 0-100, income 0-1,000,000) confuse models — the
income column drowns out age purely because of magnitude, not
meaning. You can't fix that without mean/std. Also: `np.var`
divides by n (population) while `statistics.variance` divides by
n-1 (sample) — mixing them gives subtly different answers; use
`np.var`/`np.std` in this level.

**Worked example:**
```
data = [2, 4, 6]
mean  = (2+4+6)/3 = 4
var   = ((2-4)² + (4-4)² + (6-4)²) / 3
      = (4 + 0 + 4) / 3 = 8/3 ≈ 2.667
std   = √2.667 ≈ 1.633
```

**Code:**
```python
import statistics
statistics.mean([2,4,6])      # 4
statistics.pvariance([2,4,6]) # 2.667 (population)
statistics.pstdev([2,4,6])    # 1.633
```

**Expected output:** `4`, `2.6666666666666665`, `1.632993161855452`.

---

## Medium

### 4. Weighted Sum = The Neuron — `p01`

**What it is:** A dot product plus a bias number:
`output = (inputs · weights) + bias`

**Why it exists:** It's the literal definition of a neuron —
the smallest unit of computation a neural network is built from.

**Where it's used:** A neural network layer = a matrix of these
(each row = one neuron's weights). When you "train" a model,
you're tuning weights and biases until outputs match reality —
this is what `X @ W + b` computes in PyTorch.

**What goes wrong without it:** Drop the bias and the neuron is
nailed to the origin — it can never output non-zero when all
inputs are 0 (an empty plot would be predicted to cost $0). Miss
one weight-input pairing and the vote math scrambles silently —
no error, just wrong predictions.

**Worked example:**
```
inputs  = [10, 20, 30]
weights = [0.5, 0.3, 0.2]
bias    = 0.1

output = (10×0.5 + 20×0.3 + 30×0.2) + 0.1
       = (5 + 6 + 6) + 0.1
       = 17.1
```

**Code:**
```python
def weighted_sum(inputs, weights, bias):
    return sum(x*w for x, w in zip(inputs, weights)) + bias
```

**Expected output:** `weighted_sum([10,20,30],[0.5,0.3,0.2],0.1)`
→ `17.1`.

---

### 5. Normalization (min-max scaling) — `p02`

**What it is:** Squash numbers into [0, 1] so features compare
fairly. Formula: `(x - min) / (max - min)`

**Why it exists:** Models can't tell magnitude from importance —
a feature measured in thousands dominates one measured in
decimals purely because of units, not meaning. Normalization
puts every feature on the same ruler.

**Where it's used:** Preprocessing for gradient descent,
distance-based models (KNN, K-Means), and neural nets — all of
which treat "bigger number" as "more important." Level-06 `p03`
covers the standard version.

**What goes wrong without it:** A salary column (0–120,000)
drowns out an age column (0–100) — KNN's distances become
99.9% salary, so neighbors are chosen by income alone and your
other features might as well not exist. Edge case: all values
equal → max−min = 0 → `ZeroDivisionError` crash; always guard it.

**Worked example:**
```
data = [10, 20, 30]   →  min=10, max=30, range=20
10 → (10-10)/20 = 0.0
20 → (20-10)/20 = 0.5
30 → (30-30)/20 = 1.0
```

**Code:**
```python
def normalize(vals):
    lo, hi = min(vals), max(vals)
    if hi == lo:                    # edge case!
        return [0.0] * len(vals)
    return [(v - lo) / (hi - lo) for v in vals]
```

**Expected output:** `normalize([10,20,30])` → `[0.0, 0.5, 1.0]`;
`normalize([7,7,7])` → `[0.0, 0.0, 0.0]` (guarded, no crash).

---

### 6. Euclidean Distance — `p03`

**What it is:** Straight-line distance between two points:
`sqrt(Σ(aᵢ - bᵢ)²)`. In 2D it's the Pythagorean theorem.

**Why it exists:** "Similar" needs a ruler. Distance is how you
turn "how alike are these two rows of numbers" into a number
you can sort by.

**Where it's used:** KNN classifies by nearest neighbors;
K-Means assigns points to the closest centroid; anomaly
detection flags far-away points. RAG uses its cousin (cosine
similarity) for "most similar documents."

**What goes wrong without it:** Without a distance metric,
"find the most similar customer" has no answer — similarity
becomes vibes. And it works in ANY number of dimensions — a
common bug is hardcoding 2D (`sqrt(dx² + dy²)`), which silently
drops the other features of a 10-feature row.

**Worked example:**
```
a = [0, 0]   b = [3, 4]
d = √((0-3)² + (0-4)²) = √(9 + 16) = √25 = 5
```

**Code:**
```python
import math
def euclidean(a, b):
    return math.sqrt(sum((x-y)**2 for x, y in zip(a, b)))
```

**Expected output:** `euclidean([0,0],[3,4])` → `5.0`;
`euclidean([0,0,0],[1,1,1])` → `1.7320508075688772` (√3 — works
in 3D too).

---

## Hard

### 7. Gradient Descent — `p01`

**What it is:** To find a function's minimum, look at the slope
(derivative) where you are, then take a step DOWNHILL:
`x_new = x - learning_rate × slope`

**Why it exists:** Most functions can't be minimized with a
formula — there's no closed-form answer for a billion weights.
Iterating "check slope, step downhill" is the only method that
scales.

**Where it's used:** This IS how every neural network learns.
"Training" = compute the slope of the loss w.r.t. each weight,
step downhill, repeat millions of times. Levels 08, 09, 17 all
use it; `optimizer.step()` in PyTorch is this line.

**What goes wrong without it:** lr too big → overshoot: x jumps
past the minimum and each step lands farther away — loss
explodes to infinity (divergence). lr too small → thousands of
steps and still not there — GPU bills for nothing. There's no
"correct" lr — you tune it (level-05 covers this).

**Worked example:** minimize f(x) = x². Slope f'(x) = 2x.
Start x=4, lr=0.1:
```
step 1: x = 4   - 0.1×8   = 3.2
step 2: x = 3.2 - 0.1×6.4 = 2.56
step 3: x = 2.56- 0.1×5.12= 2.048
... converges to 0 (the minimum)
```

**Code:**
```python
def descend(f, df, x, lr=0.1, iters=50):
    for _ in range(iters):
        x -= lr * df(x)
    return x
```

**Expected output:** `descend(f, df, x=4)` → ≈ `0.000057` —
each step multiplies x by 0.8, so 4·0.8⁵⁰ ≈ 0.00006 (essentially
the minimum, 0).

---

### 8. Bayes' Theorem — `p02`

**What it is:** Update a belief when you get new evidence:
`P(A|B) = P(B|A)·P(A) / P(B)`

**Why it exists:** "Test is 99% accurate" is NOT the same as
"99% chance you're sick." Bayes exists because intuition mixes
up P(test+|sick) with P(sick|test+) — they're different numbers,
and the gap is enormous when the thing you're testing for is rare.

**Where it's used:** Naive Bayes classifiers (the original spam
filters), medical screening interpretation, any system that
updates a probability as evidence arrives.

**What goes wrong without it:** People intuitively think
P(sick|+) ≈ 99% — so a real positive result triggers panic (or a
real system flags thousands of false alarms) when the actual
chance is ~17%. Skipping the base rate makes a "great" test look
useless and a useless test look great.

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

The false positives on the huge healthy population swamp the
true positives on the tiny sick population.

**Code:**
```python
def bayes(p_a, p_b_given_a, p_b_given_not_a):
    p_b = p_b_given_a * p_a + p_b_given_not_a * (1 - p_a)
    return p_b_given_a * p_a / p_b
```

**Expected output:** `bayes(0.01, 0.99, 0.05)` → `0.1666…`
(≈ 16.7% — not 99%).

---

### 9. Matrix Multiplication — `p03`

**What it is:** C[i][j] = dot product of row i of A with
column j of B. Rule: A's columns must equal B's rows.
(m×n) × (n×p) → (m×p)

**Why it exists:** One dot product computes one neuron's score —
a matrix multiply computes ALL neurons for ALL inputs at once.
It's the batch version of the weighted sum.

**Where it's used:** Every neural network layer IS a matrix
multiply: `output = X @ W + b`. GPUs dominate AI because they're
parallel matmul machines — training GPT is essentially one giant
sequence of these.

**What goes wrong without it:** Without batching you'd loop per
neuron per input — training a large model would take centuries
instead of weeks. Shape bugs: `(m×n) @ (p×q)` with n≠p →
`ValueError: shapes not aligned`, the most common crash in
neural-net code. And A@B ≠ B@A — order matters; `A * B` in NumPy
is element-wise, a completely different operation that gives a
wrong-shaped answer silently.

**Worked example:**
```
A = [[1,2],[3,4]]   B = [[5,6],[7,8]]

C[0][0] = 1×5 + 2×7 = 19
C[0][1] = 1×6 + 2×8 = 22
C[1][0] = 3×5 + 4×7 = 43
C[1][1] = 3×6 + 4×8 = 50
C = [[19,22],[43,50]]
```

**Code:**
```python
import numpy as np
C = np.array(A) @ np.array(B)   # @ = matmul
```

**Expected output:** `[[19 22]
 [43 50]]` — a 2×2 array matching the hand-computed table.

---

## Done with concepts? → Try `easy/p01-env-check.py`
