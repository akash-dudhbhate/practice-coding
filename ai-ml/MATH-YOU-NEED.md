# Math You Actually Need — 10th Grade Level

> You do NOT need advanced math to do this curriculum.
> This file teaches every symbol/formula used, in plain words,
> with small numbers you can check on paper.

If you can do arithmetic, percentages, and basic algebra
(`3x = 12 → x = 4`), you have enough. Everything else is below.

---

## 1. The Σ symbol — just means "add them all"

**`Σ`** (sigma) = sum. `Σ aᵢbᵢ` means: multiply each pair, add them up.

```
a = [1, 2, 3]     b = [4, 5, 6]
Σ aᵢbᵢ = 1×4 + 2×5 + 3×6 = 32
```

**In code:** `sum(x*y for x,y in zip(a,b))` — a loop that adds.

**You'll see it in:** dot product (L00), variance (L00), distances.

---

## 2. x̄ (x-bar) — just means "the average"

**`x̄`** = mean of x. Add all values, divide by how many.

```
x = [2, 4, 6]  →  x̄ = (2+4+6)/3 = 4
```

**You'll see it in:** mean/variance (L00), linear regression (L04).

---

## 3. Squared differences — "how far from average, but always positive"

Variance asks: how far is each point from the mean? If you just
subtract, negatives cancel positives (`2-4=-2`, `6-4=+2` → 0).
Squaring fixes that — every distance is positive.

```
data = [2, 4, 6], mean = 4
(2-4)² + (4-4)² + (6-4)² = 4 + 0 + 4 = 8
variance = 8 / 3 ≈ 2.67
```

**Why squared?** Big errors count MORE — a point 4 away contributes
16, a point 1 away contributes 1. It punishes outliers.

---

## 4. f'(x) or "derivative" — just means "the slope right now"

You don't need to compute derivatives by hand — computers do it
(autograd in PyTorch). You just need to know what it MEANS:

```
f(x) = x² at x=4: the slope f'(4) = 8.
That means: "if x goes up by 0.01, f(x) goes up by ~0.08"
```

**Why it matters:** gradient descent = "the slope says which way is
downhill — step that way." That's all of neural network training.

---

## 5. e (Euler's number) — just a special number, ~2.718

You'll see it in `eˣ` or `exp(x)`. Don't worry why it's special —
it's like π, a number that shows up naturally in growth/decay.

```
sigmoid(x) = 1 / (1 + e^(-x))
sigmoid(0) = 1/2 = 0.5
sigmoid(10) ≈ 1.0
```

**You'll see it in:** logistic regression (L04), softmax (L15).

---

## 6. log — "what power gives me this number?"

`log₂(8) = 3` because 2³ = 8. That's it — the log UNDOES a power.

```
log₂(8) = 3    (2³ = 8)
log₂(16) = 4   (2⁴ = 16)
log₁₀(100) = 2 (10² = 100)
```

**Why it matters:** entropy (L20) uses `-Σ p·log₂(p)` — it counts
"how many yes/no questions to guess the answer." Highly uncertain
data has high entropy.

---

## 7. Vectors & Matrices — just lists of numbers

**Vector** = a list: `[3, 4, 5]`. **Matrix** = a table (list of lists):
```
[[1, 2],
 [3, 4]]
```

**Matrix multiply** = each output cell = row × column dot product.
You did this in level-00! `[[1,2],[3,4]] @ [[5,6],[7,8]]`:
```
[1,2]·[5,7] = 1×5+2×7 = 19   ← row 0, col 0
[1,2]·[6,8] = 1×6+2×8 = 22   ← row 0, col 1
```

A neural network layer IS one matrix multiply. That's the whole trick.

---

## 8. Probability — just fractions that add to 1

P(rain) = 0.3 means "30% chance." All possibilities must sum to 1.

**Bayes' rule** (level-00 hard/p02) is just rearranging fractions:
```
P(sick|+) = P(+|sick) × P(sick) / P(+)
```
The worked example in level-00 concepts shows it with real numbers —
you can verify every step with a calculator.

---

## 9. |x| — absolute value / distance from zero

|−5| = 5, |5| = 5. Just "how big, ignoring the sign."

Used in Manhattan distance and L1 regularization (L04).

---

## 10. What you do NOT need

- ❌ Calculus proofs — you never derive by hand, PyTorch does it
- ❌ Eigen decomposition proofs — level-20 uses np.linalg.eig, you just check it works
- ❌ Matrix algebra identities — `@` does the work
- ❌ Trigonometry beyond sin/cos existing (positional encoding uses them, you don't derive them)

---

## The rule

When you see a formula, ask: **"can I check this with 3 numbers
on paper?"** Every example in this repo is sized so you can.
If the formula is `Σ(xᵢ - x̄)²/n`, plug in `[2,4,6]` and compute —
you'll get the same 2.67 the code gives. That's understanding.
