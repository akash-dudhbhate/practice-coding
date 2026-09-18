# Level 06 — Concepts (Detailed Explanations)

> Read each section BEFORE attempting its problem. Each concept explains:
> **What it is** · **Why it exists** · **Where it's used** ·
> **What goes wrong** without it · worked example · code ·
> expected output.

---

## Easy

### 1. Polynomial Features — `p01`

**What it is:** If your data curves but your model can only draw
straight lines, don't switch models — add new features that ARE
the curves. `PolynomialFeatures(degree=2)` turns `[x]` into
`[x, x²]`. LinearRegression stays linear, but in feature-space it
can now draw parabolas.

**Why it exists:** "Wrong model" is often really "wrong features."
Polynomial features exist to let a simple, well-understood model
fit nonlinear patterns — you upgrade the data, not the algorithm.

**Where it's used:** Feature engineering for linear models — the
lever you pull when "the model isn't good enough" but you don't
want to abandon interpretability. A linear model + smart features
beats a fancy model + dumb features surprisingly often.

**What goes wrong without it:** Fit a line to a parabola → best
case is a flat line through symmetric data: R² ≈ 0 or negative —
literally worse than guessing the mean. Watch the trap both ways:
the model is still LINEAR — it's linear in the new features
(`y = a·x + b·x²` is a linear equation in `[x, x²]`). And degree
too high → the polynomial wiggles through every training point —
classic overfitting.

**Worked example:**
```
x values:    [-2, 0, 2]
true y = x²: [4, 0, 4]

LinearRegression on x alone:
  best line through symmetric data ≈ y = 0 (flat!)
  → R² ≈ 0 or even negative — worse than guessing the mean.

After PolynomialFeatures(degree=2):
  features become [[-2, 4], [0, 0], [2, 4]]
  model learns y = 0·x + 1·x²  → perfect fit, R² = 1.0
```

**Code:**
```python
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)   # transform only!
```

**Expected output:** R² jumps from ≈0 (or negative) on raw x to
`1.0` on `[x, x²]` — the model now draws the parabola exactly.
`X_test` uses `transform` only — refitting on test would be
leakage.

---

### 2. One-Hot Encoding — `p02`

**What it is:** Models only understand numbers, but you can't just
assign `red=0, blue=1, green=2` — that falsely implies green is
"more than" blue. Instead, each category gets its own 0/1 column.

**Why it exists:** Label encoding smuggles in a fake ordering —
the model believes green > blue and builds splits on arithmetic
that means nothing. One-hot exists to represent categories as
independent switches, no order implied.

**Where it's used:** The default encoding for non-ordinal
categories: countries, product types, user segments. (For truly
ordered ones like S < M < L, a single LabelEncoder column is
fine.)

**What goes wrong without it:** With integer codes, a linear
model learns "if color ≥ 2 then..." — a rule that means nothing
and fails the day a new category lands. High-cardinality trap:
`get_dummies` on a 10,000-value column (zip codes) creates 10,000
new columns — memory explodes and each column is nearly all
zeros. One-hot is for LOW-cardinality features.

**Worked example:**
```
color  →  color_blue  color_green  color_red
red        0            0            1
blue       1            0            0
green      0            1            0
```

Compare with LabelEncoder (the wrong way for this):
`red=0, blue=1, green=2` → model thinks color order matters.

**Code:**
```python
import pandas as pd
df = pd.DataFrame({'color': ['red','blue','green']})
encoded = pd.get_dummies(df)   # auto-detects text columns
# → columns: color_blue, color_green, color_red (all 0/1)
```

**Expected output:** `encoded` → a 3×3 DataFrame with columns
`color_blue, color_green, color_red`; row 0 = `[0,0,1]`, row 1 =
`[1,0,0]`, row 2 = `[0,1,0]` — exactly one `1` per row.

---

### 3. Feature Scaling (StandardScaler) — `p03`

**What it is:** Put every feature on the same scale so no column
dominates just because its numbers are bigger.
- `StandardScaler`: `(x - mean) / std` → mean 0, std 1
- `MinMaxScaler`: `(x - min) / (max - min)` → range [0, 1]

**Why it exists:** Models can't tell units from importance — a
feature measured in thousands mathematically outweighs one in
decimals. Scaling exists so feature influence reflects signal,
not units.

**Where it's used:** Distance-based models (KNN, K-Means),
gradient descent, SVM, regularized linear models, and PCA
(`medium/p03`, level-07) which REQUIRES scaled data first.

**What goes wrong without it:** Unscaled, income (range 80,000)
drowns out age (range 20) — KNN picks neighbors by income alone;
gradient descent zig-zags and converges slowly or diverges. The
leakage trap: NEVER `fit_transform` on test data — that lets
test-set statistics leak into training. Fit on train, then only
`.transform()` everything else.

**Worked example:**
```
age:    [25, 30, 35, 40, 45]      mean=35, std≈7.07
income: [30000 ... 110000]        mean=70000, std≈31623

Standard-scaled:
age:    25 → (25-35)/7.07   ≈ -1.41
        35 → (35-35)/7.07   =  0.00
        45 → (45-35)/7.07   ≈ +1.41
income: 30000 → (30000-70000)/31623 ≈ -1.26
        → both columns now live around [-1.4, +1.4]
```

**Code:**
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)   # use TRAIN's mean/std
```

**Expected output:** `X_train_s` → each column centered at mean 0
with std 1 (age column becomes ≈ `[-1.41, -0.71, 0, 0.71,
1.41]`); `X_test_s` uses TRAIN's mean/std so its values aren't
necessarily centered — that's correct behavior, not a bug.

---

## Medium

### 4. Manual Oversampling (Fixing Class Imbalance) — `p01`

**What it is:** When one class is rare (95% class-0, 5% class-1),
a lazy model predicts 0 always and scores 95% — while being
useless. Fix by duplicating random minority samples until the
classes are balanced.

**Why it exists:** Gradient descent (and most learners) minimizes
TOTAL error — on imbalanced data, ignoring the rare class is the
cheap optimum. Oversampling exists to make the minority class
impossible to ignore.

**Where it's used:** Fraud detection, disease diagnosis, defect
detection — the interesting class is ALWAYS the rare one. (The
production version is SMOTE: synthetic interpolated samples
instead of duplicates, via `imbalanced-learn`.)

**What goes wrong without it:** 95% accuracy, 0% recall — the
model literally never predicts the class you care about, and the
accuracy number hides it (that's why these levels use recall/F1).
Critical trap: oversample the TRAINING data only — duplicate
minority rows into the test set and your evaluation is fake
(you're testing on copies of training rows AND you've changed the
real class ratio).

**Worked example:**
```
y = [0]*95 + [1]*5        → 95 zeros, 5 ones

minority_idx = [95,96,97,98,99]        (where the 1s live)
needed = 95 - 5 = 90 more samples
np.random.choice(minority_idx, size=90, replace=True)
  → picks indices like [97, 95, 99, 97, ...] (duplicates allowed)

Result: np.bincount(y_balanced) → [95, 95]
```

**Code:**
```python
minority_idx = np.where(y == 1)[0]
needed = majority_count - len(minority_idx)
extra = np.random.choice(minority_idx, size=needed, replace=True)
X_bal = np.vstack([X, X[extra]])
y_bal = np.concatenate([y, y[extra]])
```

**Expected output:** `np.bincount(y_bal)` → `[95, 95]` — the
minority class now has as many rows as the majority, so "predict
0 always" scores 50% instead of 95% and can't win anymore.

---

### 5. Feature Importance & Selection — `p02`

**What it is:** Tree models (RandomForest) track how much each
feature helped split the data — `feature_importances_`. Keeping
only the top features often IMPROVES accuracy: noise features add
variance without signal.

**Why it exists:** More columns ≠ more signal — each useless
feature is another chance to memorize noise. Importance exists to
measure what the model actually used, so you can cut what it
didn't.

**Where it's used:** Faster training, less overfitting, easier
interpretation — and "which features matter?" is the first thing
stakeholders ask. RFE (level-04 `hard/p03`) automates the same
pruning loop.

**What goes wrong without it:** Keep all 10 features → the model
spends splits on noise → test accuracy drops (0.90 vs 0.95 in the
example). Reading importances wrong: `argsort` returns ASCENDING
order — the top features are at the END (`[-5:]`, not `[:5]` —
grab the wrong end and you keep the WORST features). And
importance ≠ causation: it says "the model used this," not "this
causes y"; correlated features split importance between them.

**Worked example:**
```
10 features, only 5 informative.
RandomForest importances (made-up but typical):
  feat:  [ 0,    1,    2,    3,    4,    5,    6,    7,    8,    9]
  imp:   [.02,  .01,  .03,  .22,  .19,  .18,  .21,  .02,  .12,  .0 ]

np.argsort(imp)[-5:] → [3, 4, 5, 6, 8]  (the top 5)

All features acc:  0.90
Top-5 acc:         0.95  ← higher! Removed noise = cleaner signal
```

**Code:**
```python
importances = rf.feature_importances_
top5_idx = np.argsort(importances)[-5:]
rf2 = RandomForestClassifier().fit(X_train[:, top5_idx], y_train)
```

**Expected output:** `top5_idx` → `[3, 4, 5, 6, 8]`; retrained
model scores `0.95` vs `0.90` with all features — dropping noise
columns literally improved the model.

---

### 6. PCA (Dimensionality Reduction) — `p03`

**What it is:** PCA finds the directions where data varies MOST
and projects onto those axes. 10 features → 3 components that
still capture most of the information. Think of it as the best
"shadow" of high-D data in fewer dimensions.

**Why it exists:** High-dimensional data is slow to train, hard
to visualize, and prone to overfitting (curse of dimensionality).
PCA exists because most datasets' variance concentrates in a few
directions — you keep the signal and drop the rest.

**Where it's used:** Compression before training, 2D
visualization (level-07 `easy/p03` projects iris to 2D),
denoising, and as a preprocessing step before clustering.

**What goes wrong without it:** Train on 100 correlated features
→ slow, overfit, unvisualizable. Forget to scale first → the
highest-magnitude column becomes "component 1" regardless of
information content (PCA maximizes variance; unscaled income has
the biggest variance by units alone). And the interpretation
trap: components are NOT original features — `X_reduced[:,0]` is
a weighted blend of all 10, so you lose interpretability to gain
compactness.

**Worked example:**
```
10 features → PCA(n_components=3)
explained_variance_ratio_ = [0.28, 0.15, 0.10]

Meaning: component 1 alone holds 28% of all variance,
components 1-3 together hold 0.28+0.15+0.10 = 53%.

X_reduced.shape: (200, 3) — each row is now 3 numbers
that summarize the original 10.
```

**Code:**
```python
from sklearn.decomposition import PCA
X_s = StandardScaler().fit_transform(X)      # ALWAYS scale first
pca = PCA(n_components=3)
X_reduced = pca.fit_transform(X_s)
print(pca.explained_variance_ratio_.sum())   # e.g. 0.53
```

**Expected output:** `X_reduced.shape` → `(200, 3)`;
`explained_variance_ratio_.sum()` → `0.53` — 3 blended features
keeping 53% of the original 10 features' information.

---

## Hard

### 7. Custom sklearn Transformer — `p01`

**What it is:** You can write your OWN transformer that plugs into
any sklearn Pipeline. Subclass `BaseEstimator` + `TransformerMixin`,
implement `fit()` (learn stats, return `self`) and `transform()`
(return modified data).

**Why it exists:** Real feature engineering (log-transforms,
binning, interaction terms) must happen INSIDE the pipeline so it
applies identically to train/test/production — the mixin
interface exists so your code gets the pipeline's leak-free
guarantees for free.

**Where it's used:** Production ML code — domain-specific
transforms that sklearn doesn't ship, wired into the same
Pipeline as scaling and the model.

**What goes wrong without it:** `fit` MUST `return self` — the
pipeline calls `fit` then chains into `transform` on the returned
object; forget it and you get `AttributeError: 'NoneType' object
has no attribute 'transform'`. Mutate X in place (skip
`X.copy()`) → you corrupt the caller's data. And `log1p` =
`log(1+x)` crashes on negative input — use `np.abs` if needed.
Transform outside the pipeline → train/test processed
differently → subtle skew.

**Worked example:**
```python
class LogTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, cols):
        self.cols = cols          # e.g. [0, 2]
    def fit(self, X, y=None):
        return self               # nothing to learn — still return self!
    def transform(self, X):
        X = X.copy()
        X[:, self.cols] = np.log1p(np.abs(X[:, self.cols]))
        return X
```

Then in a pipeline:
```python
pipe = Pipeline([
    ('log', LogTransformer(cols=[0, 2])),
    ('model', LogisticRegression())
])
pipe.fit(X_train, y_train)   # calls log.fit → log.transform → model.fit
```

**Code:**
```python
from sklearn.base import BaseEstimator, TransformerMixin
# subclass both, implement fit + transform, fit returns self
```

**Expected output:** `pipe.fit(X_train, y_train)` runs end-to-end:
columns 0 and 2 get `log1p(|x|)` applied identically in train and
test; `pipe.score(X_test, y_test)` returns a normal accuracy with
no leakage and no `AttributeError`.

---

### 8. Feature Engineering — `p02`

**What it is:** Create NEW features by combining existing ones.
The model can't see relationships you don't give it — but a ratio
or product of two columns can encode the pattern directly.

**Why it exists:** Models see columns, not meaning — a linear
model cannot divide income by age unless a column IS
income/age. Feature engineering exists to hand the model the
pattern pre-computed.

**Where it's used:** The unglamorous secret of applied ML —
Kaggle winners and production systems both win on features, not
exotic models. A domain expert who knows "income/age matters"
beats a bigger model that doesn't.

**What goes wrong without it:** The model must somehow discover
the ratio itself → a linear model CAN'T (division isn't linear)
→ accuracy caps low while one derived column would have solved
it. Opposite trap: more features ≠ better — each engineered
feature needs a REASON (a hypothesis about the target); random
feature soup just adds noise — combine with feature importance
(`medium/p02`) to prune.

**Worked example:**
```
Raw columns: age, income, day_of_week
True rule:   target = 1 if income/age > 1500

Engineered:
  income_per_age = income / age          ← THE rule, handed to the model
  age_sq         = age²                   (nonlinear effect)
  income_log     = log1p(income)          (tame skew: 30k→10.3, 110k→11.6)
  is_weekend     = 1 if day_of_week >= 5  (binary flag)

Before: model must somehow divide income by age itself → hard
After:  one weight on income_per_age solves it → ~95%+ accuracy
```

**Code:**
```python
df['income_per_age'] = df['income'] / df['age']
df['is_weekend'] = (df['day_of_week'] >= 5).astype(int)
df['income_log'] = np.log1p(df['income'])
```

**Expected output:** `df` gains 3 columns: `income_per_age`
(e.g., 60000/30 → `2000.0`), `is_weekend` (`0`/`1` flags),
`income_log` (30000 → `10.3`, 110000 → `11.6` — the skew
compressed). Model accuracy jumps to ~95%+ with the new columns.

---

### 9. class_weight='balanced' — `p03`

**What it is:** Alternative to resampling for imbalanced data:
tell the model "mistakes on the minority class cost more." sklearn
auto-computes weights inversely proportional to class frequency.

**Why it exists:** Resampling changes the data; sometimes you
can't or shouldn't. Class weighting exists to fix the incentive
instead — same balance, achieved by pricing errors rather than
duplicating rows.

**Where it's used:** Fraud/disease/defect models where missing a
positive (low recall) is far worse than a false alarm (low
precision) — a one-line fix: no resampling, no extra libraries.

**What goes wrong without it:** The default model on 95/5 data
learns "always predict 0" — recall 0.00, catches ZERO minority
cases, and accuracy still looks great. "Balanced" does NOT mean
better accuracy — it usually LOWERS overall accuracy on purpose,
trading it for catching the rare class. Judge it by recall/F1,
not accuracy — if you evaluate the balanced model on accuracy
you'll think it got worse when it got useful.

**Worked example:**
```
Data: 95% class-0, 5% class-1.

Weight for class-1 ≈ n / (2 × count_1) = 1000/(2×50) = 10
Weight for class-0 ≈ 1000/(2×950) ≈ 0.53
→ each minority mistake counts ~19× more during training.

Results on test set:
  Default model:  recall = 0.00   (predicts 0 always — catches ZERO!)
  Balanced model: recall = 0.86   (catches 86% of the minority)
                  f1 = 0.25       (but lots of false alarms)
```

**Code:**
```python
model = LogisticRegression(class_weight='balanced', max_iter=1000)
from sklearn.metrics import recall_score, f1_score
recall = recall_score(y_test, y_pred)   # of those truly 1, how many found
```

**Expected output:** Default model: `recall = 0.0`. Balanced
model: `recall ≈ 0.86`, `f1 ≈ 0.25` — you catch most of the rare
class at the price of many false alarms, which is exactly the
trade you asked for.

---

## Done with concepts? → Try `easy/p01-polynomial-features.py`
