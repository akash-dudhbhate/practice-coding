# Level 02 — Concepts (Detailed Explanations)

> Read each section BEFORE attempting its problem. Each concept explains:
> **What it is** · **Why it exists** · **Where it's used** ·
> **What goes wrong** without it · worked example · code ·
> expected output.

---

## Easy

### 1. NumPy Arrays — `p01`

**What it is:** A NumPy array is a grid of numbers you can do math
on all at once (vectorized = fast). Every ML library in Python is
built on it. Each array has a `shape` (dimensions), `dtype` (number
type), `ndim` (how many dimensions), and `size` (total elements).
`np.random.seed(42)` freezes randomness so results are reproducible.

**Why it exists:** Python lists do math element-by-element in slow
loops; ML needs the same operation on millions of numbers at once.
NumPy exists to make `X @ W` fast — it's C-speed math behind a
Python API.

**Where it's used:** A dataset IS an array — rows are samples,
columns are features. `axis=0` (down columns) gives per-feature
stats, used for normalization. `axis=1` (across rows) gives
per-sample values. Everything in levels 04+ is array math.

**What goes wrong without it:** Pure-Python loops over a million
rows take minutes where NumPy takes milliseconds — training
becomes unusable. The axis trap: `axis=0` means "collapse along
rows," giving one value PER COLUMN — the opposite of intuition.
Average the wrong axis and your "per-feature means" are actually
per-sample means — the normalization that follows is silently
garbage. Mnemonic: the axis you name is the one that disappears.

**Worked example:**
```python
import numpy as np
np.random.seed(42)
arr = np.random.randint(0, 100, size=(4, 5))
# [[51 92 14 71 60]
#  [20 82 86 74 74]
#  [87 99 23  2 21]
#  [52  1 87 29 37]]

arr.shape          # (4, 5)   → 4 rows × 5 cols
arr.ndim           # 2        → a matrix
arr.size           # 20       → 4×5 elements
arr.mean(axis=0)   # [52.5 68.5 52.5 44. 48.] → mean DOWN each column
# e.g. col 0: (51+20+87+52)/4 = 210/4 = 52.5
```

**Code:**
```python
np.random.seed(42)
arr = np.random.randint(0, 100, size=(4, 5))
print(arr.shape, arr.ndim, arr.size)
print(arr.mean(axis=0))
```

**Expected output:** `(4, 5) 2 20` then
`[52.5 68.5 52.5 44. 48.]` — one mean per column. (With
`seed(42)` these exact values reproduce every run.)

---

### 2. Pandas DataFrames — `p02`

**What it is:** A DataFrame is a labeled table — think spreadsheet
in Python. Columns have names and types; rows are records. In ML,
raw data almost always lands in a DataFrame before becoming arrays.

**Why it exists:** Real data has column names, mixed types, and
missing values — NumPy arrays are too bare-metal for that.
DataFrames exist to inspect, clean, and reshape messy tables
before they become model input.

**Where it's used:** Data cleaning — the step that eats 80% of
real ML work — is DataFrame work: inspecting (`head`, `dtypes`,
`shape`), fixing types, filling gaps, encoding text.

**What goes wrong without it:** `object` dtype means "text/mixed"
— models can't eat it and sklearn crashes with
`ValueError: could not convert string to float`. Also the classic:
`df['age']` is a Series (1D) but `df[['age']]` is a DataFrame (2D)
— some sklearn functions demand the 2D version and throw
"expected 2D array" on the 1D one.

**Worked example:**
```python
import pandas as pd
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'age':  [25, 30, 35, 28],
    'city': ['Mumbai', 'Delhi', 'Bangalore', 'Chennai'],
})

df.shape   # (4, 3) — 4 rows, 3 columns
df.dtypes  # name: object, age: int64, city: object
df.head()  # first 5 rows (here: all 4)
```

**Code:**
```python
df = pd.DataFrame({'name': ['Alice','Bob','Charlie','Diana'],
                   'age': [25,30,35,28],
                   'city': ['Mumbai','Delhi','Bangalore','Chennai']})
print(df.head(), df.shape, df.dtypes)
```

**Expected output:** A 4×3 table with Alice/Bob/Charlie/Diana
rows; `shape` → `(4, 3)`; `dtypes` → `name object, age int64,
city object`.

---

### 3. Filling Missing Values (Imputation) — `p03`

**What it is:** Real data has holes — `NaN` ("Not a Number") marks
them. Models crash on NaN, so you must fill them. Strategy:
numeric column → **median** (middle value, ignores outliers);
category column → **mode** (most frequent value).

**Why it exists:** Every estimator in sklearn refuses to train on
NaN — missing values must become SOMETHING. Median/mode exist
because they fill holes with a "typical" value instead of a
biased one.

**Where it's used:** The first preprocessing step in nearly every
tabular pipeline — `SimpleImputer` in sklearn does this
automatically inside a Pipeline (see `medium/p01`).

**What goes wrong without it:** `model.fit` on NaN →
`ValueError: Input contains NaN`. Fill with MEAN when outliers
exist → mean of [10, 12, 11, 500] is 133 (absurd) vs median 11.5
(sane) — one corrupt row poisons every fill. `mode()` returns a
Series, not a value — forgetting `[0]` inserts a Series where a
scalar belongs. And fill BEFORE splitting? That computes medians
using test data — leakage (see `hard/p01`).

**Worked example:**
```
age:   [25, NaN, 30, NaN, 35]   → median of [25,30,35] = 30
score: [85, 90, NaN, 78, 92]    → median of [78,85,90,92] = 87.5
city:  [Mumbai, Delhi, NaN, Chennai, NaN]
       → mode of the known values → 'Chennai'

Filled:
  age   [25, 30, 30, 30, 35]
  score [85, 90, 87.5, 78, 92]
  city  [Mumbai, Delhi, Chennai, Chennai, Chennai]
```

**Code:**
```python
df['age']   = df['age'].fillna(df['age'].median())
df['city']  = df['city'].fillna(df['city'].mode()[0])
```

**Expected output:** No NaN remains — `age` becomes
`[25, 30, 30, 30, 35]` (median 30 in both holes), `city` has
`'Chennai'` where the NaNs were.

---

## Medium

### 4. sklearn Pipelines — `p01`

**What it is:** A `Pipeline` chains preprocessing + model into ONE
object. Steps run in order: impute → scale → model. The magic: when
you call `pipe.fit(X_train)`, every step sees ONLY training data —
leakage is impossible.

**Why it exists:** Doing impute/scale/train by hand means
juggling "which statistics came from which data" — one slip and
test stats contaminate training. Pipeline exists to make the
correct order and the correct data the automatic path.

**Where it's used:** Every production sklearn project — it's also
the only thing `GridSearchCV` and `cross_val_score` can safely
tune without leaking preprocessing across folds.

**What goes wrong without it:** Manually you'd `fillna` on all
data, split, then train — test's mean just leaked into train's
fill values and your 0.99 test score is fake (see `hard/p01`).
Also, `pipe.fit` calls `fit_transform` on each preprocessing step
but `fit` on the final model — reimplementing that by hand, it's
easy to call the wrong one. `score(X_test)` transforms test with
TRAIN's parameters, never re-fits.

**Worked example:**
```python
pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),   # fill NaN
    ('scaler',  StandardScaler()),                  # mean 0, std 1
    ('model',   LogisticRegression()),              # classifier
])
pipe.fit(X_train, y_train)   # learns fill values + scales on TRAIN
pipe.score(X_test, y_test)   # applies train's values to TEST → 0.875
```

**Code:**
```python
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
pipe = Pipeline([('imputer', SimpleImputer()),
                 ('scaler', StandardScaler()),
                 ('model', LogisticRegression())])
```

**Expected output:** `pipe.fit(X_train, y_train)` returns the
fitted pipeline; `pipe.score(X_test, y_test)` → `0.875` on this
problem's data — an honest score because the imputer and scaler
learned only from train.

---

### 5. Outlier Detection with IQR — `p02`

**What it is:** **Outliers** are values absurdly far from the rest —
they drag means and distort models. The IQR rule: compute Q1 (25th
percentile) and Q3 (75th percentile); IQR = Q3−Q1. Anything outside
`[Q1 − 1.5·IQR, Q3 + 1.5·IQR]` is an outlier. **Capping** replaces
outliers with the boundary value instead of deleting rows.

**Why it exists:** Means and distances are not robust — ONE
corrupt sensor reading can pull them arbitrarily far. The IQR
rule exists because quartiles barely move when an extreme value
appears, so they're a stable basis for deciding "absurdly far."

**Where it's used:** Preprocessing for regression (one huge value
warps the whole line) and KNN (one far point distorts all
distances); box plots draw these same fences visually
(level-03 `medium/p03`).

**What goes wrong without it:** One typo'd value (age = 999)
distorts every mean, std, and distance downstream — the model
fits the typo. But don't DELETE outliers blindly either:
sometimes they ARE the signal (fraud, disease). Capping with
`np.clip` is the safer default — the sample stays, the extreme
value doesn't.

**Worked example:**
```
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]

Q1 = 3.25,  Q3 = 7.75,  IQR = 4.5
lower = 3.25 − 1.5×4.5 = −3.5
upper = 7.75 + 1.5×4.5 = 14.5

100 > 14.5 → outlier!
Capped: [1, 2, 3, 4, 5, 6, 7, 8, 9, 14.5]   → 1 outlier found
```

**Code:**
```python
Q1, Q3 = np.percentile(data, [25, 75])
IQR = Q3 - Q1
lower, upper = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR
n_outliers = int(((data < lower) | (data > upper)).sum())
cleaned = np.clip(data, lower, upper)
```

**Expected output:** `n_outliers` → `1`; `cleaned` →
`[1, 2, 3, 4, 5, 6, 7, 8, 9, 14.5]` — the 100 pulled back to the
upper fence.

---

### 6. Mixed Data Types — `p03`

**What it is:** Real datasets mix text dates, categories, and
numbers. Models only understand numbers, so each type needs its own
conversion: date strings → `pd.to_datetime`, categories →
`LabelEncoder` (each label becomes an int), numbers →
`StandardScaler` ((x − mean) / std).

**Why it exists:** `model.fit` is pure arithmetic — "Mumbai" is
not a number. Each dtype needs a translator that preserves the
information while producing something arithmetic can eat.

**Where it's used:** The type-conversion block of every tabular
pipeline — dates → timestamps/features, categories → codes or
one-hot, numbers → scaled. `ColumnTransformer` (`hard/p02`)
automates exactly this split.

**What goes wrong without it:** Feed a string column to sklearn →
`ValueError: could not convert string to float: 'Mumbai'`. Leave
features unscaled (age 0-100 vs income 0-120000) → the bigger
magnitude dominates distances and gradients. And `LabelEncoder`
invents a fake ordering (Mumbai=3 > Delhi=2) that can mislead
linear models — fine for LABELS (y), risky for FEATURES (X);
`OneHotEncoder` is safer for features (`hard/p02`).

**Worked example:**
```
city:    ['Mumbai', 'Delhi', 'Bangalore', 'Chennai']
LabelEncoder sorts alphabetically → codes:
  Bangalore=0, Chennai=1, Delhi=2, Mumbai=3
  → city_encoded = [3, 2, 0, 1]

age: [25, 30, 35, 28]
  mean = 29.5, std ≈ 3.640
  25 → (25 − 29.5)/3.640 ≈ −1.236
  35 → (35 − 29.5)/3.640 ≈ +1.511
```

**Code:**
```python
df['signup_date'] = pd.to_datetime(df['signup_date'])
df['city_encoded'] = LabelEncoder().fit_transform(df['city'])
df['age_scaled'] = StandardScaler().fit_transform(df[['age']])
```

**Expected output:** `signup_date` becomes datetime64 dtype;
`city_encoded` → `[3, 2, 0, 1]`; `age_scaled` →
`[-1.236, 0.137, 1.511, -0.412]` (mean 0, std 1).

---

## Hard

### 7. Data Leakage — `p01`

**What it is:** Leakage = test data influencing training. The
classic bug: compute medians/scaling on ALL data, THEN split — the
test set's statistics just leaked into what the model learned.
Result: inflated scores that vanish in production. Rule: **split
first**, fit preprocessing on train only.

**Why it exists:** The test set's only job is simulating unseen
data — the moment its information shapes training, that
simulation is broken. The split-first rule exists to keep the
test set a true stranger.

**Where it's used:** Every preprocessing decision in every
project — imputation, scaling, feature selection, SMOTE all must
fit inside `pipe.fit(X_train)` or inside CV folds.

**What goes wrong without it:** This is the #1 silent killer of
real ML projects — papers have been retracted over it. You get a
0.99 test score that's pure fiction: it drops to 0.80 in
production where the "future" statistics aren't available. It
fools experienced devs because the model never sees test ROWS —
the test data's STATISTICS leaked through the mean/median you
computed.

**Worked example:**
```
LEAKY (wrong):
  mean_age = df['age'].mean()      # computed on ALL 200 rows
  df['age'] -= mean_age            # test rows influenced training!
  split → train → test 0.99  ← fake score

CLEAN (right):
  split FIRST (80/20, random_state=42)
  Pipeline fits imputer+scaler inside .fit(X_train)
  → only train's 160 rows set the parameters
  → test 0.95 ← honest score
```

**Code:**
```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)      # split FIRST
pipe = Pipeline([('pre', preprocessor),
                 ('model', RandomForestClassifier(n_estimators=50,
                                                  random_state=42))])
pipe.fit(X_train, y_train)                     # preprocessor sees train only
```

**Expected output:** `pipe.score(X_test, y_test)` → `0.95` —
slightly lower than the leaky 0.99, but it's the number that
survives contact with production.

---

### 8. ColumnTransformer — `p02`

**What it is:** Different columns need different preprocessing —
numbers get impute+scale, categories get impute+one-hot-encode.
`ColumnTransformer` applies each pipeline to its own column list in
one step, then glues the results back together.

**Why it exists:** Without it you'd slice the DataFrame, transform
each piece, and reassemble by hand — three places for a column
alignment bug. It exists to make "different treatment per column"
one declarative object that a Pipeline can own.

**Where it's used:** THE production-grade pattern for tabular
data — `fit_transform` gives one clean numeric matrix for the
model, and wrapped in a Pipeline it also gives leak-free splits.

**What goes wrong without it:** Manual column surgery → scaled
column lands in the wrong position, or you fit the encoder on the
full data (leakage again). And the encoding trap: `LabelEncoder`
turns 'B' into `1` — one number with a fake order a linear model
will believe. `OneHotEncoder` turns 'B' into `[0,1,0]` — one
binary column per category, no ordering implied. For model
features, one-hot is the safe choice.

**Worked example:**
```
DataFrame: feature_0..feature_4 (numbers) + category ('A'/'B'/'C')

ColumnTransformer([
    ('num', Pipeline([impute(mean), StandardScaler]),
            ['feature_0', ..., 'feature_4']),
    ('cat', Pipeline([impute(most_frequent), OneHotEncoder]),
            ['category']),
])

One row in:  [1.2, -0.5, 0.3, 2.1, -1.0, 'B']
One row out: [scaled 5 numbers..., 0, 1, 0]   # 'B' → one-hot vector
```

**Code:**
```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

pre = ColumnTransformer([
    ('num', Pipeline([('imp', SimpleImputer(strategy='mean')),
                      ('sc', StandardScaler())]), num_cols),
    ('cat', Pipeline([('imp', SimpleImputer(strategy='most_frequent')),
                      ('oh', OneHotEncoder())]), cat_cols),
])
```

**Expected output:** `pre.fit_transform(df)` → a numeric matrix
with `len(num_cols) + n_categories` columns — e.g., 5 scaled
numbers + `[0, 1, 0]` for category 'B' = 8 columns per row, zero
strings, zero NaN.

---

### 9. Stratified Splitting — `p03`

**What it is:** With imbalanced classes (95% negative / 5%
positive), a random split can starve one side of minority samples —
e.g., only 7 positives land in test, making the test score noisy
luck. `stratify=y` forces both splits to keep the SAME class ratio
as the full data.

**Why it exists:** Random sampling doesn't respect rare classes —
on a 5%-positive dataset, chance decides whether your test set
has 7 positives (meaningless) or 10 (matches reality). Stratify
exists to make the split representative by construction, not luck.

**Where it's used:** The default reflex for classification splits
— medical, fraud, and churn data are all imbalanced.
`StratifiedKFold` (level-05) applies the same idea inside
cross-validation.

**What goes wrong without it:** A test set with 7 positive
samples can't measure anything — one lucky guess swings accuracy
14%. You'd report a "95% recall" that's really "we found 5 of 7."
And note what stratify does NOT do: it PRESERVES the imbalance
(5% stays 5%) — actually balancing classes needs
resampling/SMOTE, a training-only tool (level-06 `medium/p01`).

**Worked example:**
```
1000 samples: 950 class-0, 50 class-1  (5%)

Random split (no stratify):   train [757, 43]   test [193, 7]
                              test is only 3.5% positive — skewed!

Stratified split:             train [760, 40]   test [190, 10]
                              test is exactly 5% positive ✓
```

**Code:**
```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)
np.bincount(y_train)   # verify ratios preserved
```

**Expected output:** `np.bincount(y_train)` → `[760, 40]` and
`np.bincount(y_test)` → `[190, 10]` — exactly 5% positive in
both, matching the full data.

---

## Done with concepts? → Try `easy/p01-create-array.py`
