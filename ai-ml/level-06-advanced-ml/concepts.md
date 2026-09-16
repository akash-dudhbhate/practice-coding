# Level 06 — Concepts (Detailed Explanations)

Read each section BEFORE attempting its problem. Each concept has:
what it is in plain words → a worked example with real numbers →
why ML cares → the code → what confuses beginners.

---

## Easy

### 1. Polynomial Features — `p01`

**What it is:** If your data curves but your model can only draw
straight lines, don't switch models — add new features that ARE
the curves. `PolynomialFeatures(degree=2)` turns `[x]` into
`[x, x²]`. LinearRegression stays linear, but in feature-space it
can now draw parabolas.

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

**Why ML cares:** Feature engineering is often worth more than a
fancier model. A linear model + smart features beats a fancy model
+ dumb features surprisingly often. This is THE lever you pull
when "the model isn't good enough."

**Code:**
```python
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)   # transform only!
```

**Common confusion:** The model is still LINEAR — it's linear in
the new features. `y = a·x + b·x²` is a linear equation in
`[x, x²]` even though the plot curves.

---

### 2. One-Hot Encoding — `p02`

**What it is:** Models only understand numbers, but you can't just
assign `red=0, blue=1, green=2` — that falsely implies green is
"more than" blue. Instead, each category gets its own 0/1 column.

**Worked example:**
```
color  →  color_blue  color_green  color_red
red        0            0            1
blue       1            0            0
green      0            1            0
```

Compare with LabelEncoder (the wrong way for this):
`red=0, blue=1, green=2` → model thinks color order matters.

**Why ML cares:** Real data is full of categories: countries,
product types, user segments. Wrong encoding = the model learns
fake patterns ("green > blue"). One-hot is the default for
non-ordinal categories (no natural order). For truly ordered ones
(S < M < L), LabelEncoder is fine.

**Code:**
```python
import pandas as pd
df = pd.DataFrame({'color': ['red','blue','green']})
encoded = pd.get_dummies(df)   # auto-detects text columns
# → columns: color_blue, color_green, color_red (all 0/1)
```

**Common confusion:** `get_dummies` creates one column per unique
value — if a column has 10,000 unique values (like zip codes), you
get 10,000 new columns. One-hot is for LOW-cardinality features.

---

### 3. Feature Scaling (StandardScaler) — `p03`

**What it is:** Put every feature on the same scale so no column
dominates just because its numbers are bigger.
- `StandardScaler`: `(x - mean) / std` → mean 0, std 1
- `MinMaxScaler`: `(x - min) / (max - min)` → range [0, 1]

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

**Why ML cares:** Distance-based models (KNN, K-Means) and gradient
descent treat "bigger number" as "bigger difference." Unscaled,
income (range 80,000) would drown out age (range 20) completely.
Also, PCA (medium/p03, level-07) REQUIRES scaled data first.

**Code:**
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)   # use TRAIN's mean/std
```

**Common confusion:** NEVER `fit_transform` on test data — that
would let test-set statistics leak into training (data leakage).
Fit on train, then only `.transform()` everything else.

---

## Medium

### 4. Manual Oversampling (Fixing Class Imbalance) — `p01`

**What it is:** When one class is rare (95% class-0, 5% class-1),
a lazy model predicts 0 always and scores 95% — while being
useless. Fix by duplicating random minority samples until the
classes are balanced.

**Worked example:**
```
y = [0]*95 + [1]*5        → 95 zeros, 5 ones

minority_idx = [95,96,97,98,99]        (where the 1s live)
needed = 95 - 5 = 90 more samples
np.random.choice(minority_idx, size=90, replace=True)
  → picks indices like [97, 95, 99, 97, ...] (duplicates allowed)

Result: np.bincount(y_balanced) → [95, 95]
```

**Why ML cares:** Fraud detection, disease diagnosis, defect
detection — the interesting class is ALWAYS the rare one. Accuracy
lies on imbalanced data; that's why levels use recall/F1 instead.
(Real-world version: SMOTE creates synthetic samples instead of
duplicates — same idea, needs `imbalanced-learn`.)

**Code:**
```python
minority_idx = np.where(y == 1)[0]
needed = majority_count - len(minority_idx)
extra = np.random.choice(minority_idx, size=needed, replace=True)
X_bal = np.vstack([X, X[extra]])
y_bal = np.concatenate([y, y[extra]])
```

**Common confusion:** Oversample the TRAINING data only — never
the test set. Test data must stay realistically imbalanced, or
your evaluation is fake.

---

### 5. Feature Importance & Selection — `p02`

**What it is:** Tree models (RandomForest) track how much each
feature helped split the data — `feature_importances_`. Keeping
only the top features often IMPROVES accuracy: noise features add
variance without signal.

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

**Why ML cares:** Fewer features = faster training, less
overfitting, easier interpretation. "Which features matter?" is
also the first thing stakeholders ask — feature importance answers it.

**Code:**
```python
importances = rf.feature_importances_
top5_idx = np.argsort(importances)[-5:]
rf2 = RandomForestClassifier().fit(X_train[:, top5_idx], y_train)
```

**Common confusion:** argsort returns ASCENDING order — the top
features are at the END: `[-5:]`, not `[:5]`. And importance ≠
causation — it says "the model used this," not "this causes y."

---

### 6. PCA (Dimensionality Reduction) — `p03`

**What it is:** PCA finds the directions where data varies MOST
and projects onto those axes. 10 features → 3 components that
still capture most of the information. Think of it as the best
"shadow" of high-D data in fewer dimensions.

**Worked example:**
```
10 features → PCA(n_components=3)
explained_variance_ratio_ = [0.28, 0.15, 0.10]

Meaning: component 1 alone holds 28% of all variance,
components 1-3 together hold 0.28+0.15+0.10 = 53%.

X_reduced.shape: (200, 3) — each row is now 3 numbers
that summarize the original 10.
```

**Why ML cares:** High-dimensional data is slow to train, hard to
visualize, and prone to overfitting (curse of dimensionality).
PCA compresses it. Also used for visualization (level-07 easy/p03
projects iris to 2D) and as a preprocessing step before
clustering.

**Code:**
```python
from sklearn.decomposition import PCA
X_s = StandardScaler().fit_transform(X)      # ALWAYS scale first
pca = PCA(n_components=3)
X_reduced = pca.fit_transform(X_s)
print(pca.explained_variance_ratio_.sum())   # e.g. 0.53
```

**Common confusion:** PCA components are NOT original features —
they're mixtures of all of them. `X_reduced[:, 0]` isn't
"feature 0," it's a weighted blend. You lose interpretability
to gain compactness.

---

## Hard

### 7. Custom sklearn Transformer — `p01`

**What it is:** You can write your OWN transformer that plugs into
any sklearn Pipeline. Subclass `BaseEstimator` + `TransformerMixin`,
implement `fit()` (learn stats, return `self`) and `transform()`
(return modified data).

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

**Why ML cares:** Real feature engineering (log-transforms, binning,
interaction terms) must happen INSIDE the pipeline so it applies
identically to train/test/production data. Custom transformers make
that possible — this is how production ML code is actually written.

**Code:**
```python
from sklearn.base import BaseEstimator, TransformerMixin
# subclass both, implement fit + transform, fit returns self
```

**Common confusion:** `fit` MUST `return self` — the pipeline calls
`fit` then chains into `transform` on the returned object. Forgetting
`return self` gives `AttributeError: 'NoneType'`. Also, `log1p` =
`log(1+x)` and crashes on negative input — use `np.abs` if needed.

---

### 8. Feature Engineering — `p02`

**What it is:** Create NEW features by combining existing ones.
The model can't see relationships you don't give it — but a ratio
or product of two columns can encode the pattern directly.

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

**Why ML cares:** This is the unglamorous secret of applied ML.
Kaggle winners and production systems both win on features, not
exotic models. A domain expert who knows "income/age matters" beats
a bigger model that doesn't.

**Code:**
```python
df['income_per_age'] = df['income'] / df['age']
df['is_weekend'] = (df['day_of_week'] >= 5).astype(int)
df['income_log'] = np.log1p(df['income'])
```

**Common confusion:** More features ≠ better. Each engineered
feature should have a REASON (a hypothesis about the target).
Random feature soup just adds noise — combine with feature
importance (medium/p02) to prune.

---

### 9. class_weight='balanced' — `p03`

**What it is:** Alternative to resampling for imbalanced data:
tell the model "mistakes on the minority class cost more." sklearn
auto-computes weights inversely proportional to class frequency.

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

**Why ML cares:** This is the precision-recall tradeoff in the
flesh. For fraud/disease, missing a positive (low recall) is far
worse than a false alarm (low precision) — so `class_weight` is
often worth it. It's also a one-line fix: no resampling, no extra
libraries.

**Code:**
```python
model = LogisticRegression(class_weight='balanced', max_iter=1000)
from sklearn.metrics import recall_score, f1_score
recall = recall_score(y_test, y_pred)   # of those truly 1, how many found
```

**Common confusion:** "Balanced" does NOT mean better accuracy —
it usually LOWERS overall accuracy on purpose. It trades raw
accuracy for catching the rare class. Judge it by recall/F1, not
accuracy.

---

## Done with concepts? → Try `easy/p01-polynomial-features.py`
