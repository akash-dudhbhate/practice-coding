# Level 02 — Concepts (Detailed Explanations)

Read each section BEFORE attempting its problem. Each concept has:
what it is in plain words → a worked example with real numbers →
why ML cares → the code → what confuses beginners.

---

## Easy

### 1. NumPy Arrays — `p01`

**What it is:** A NumPy array is a grid of numbers you can do math
on all at once (vectorized = fast). Every ML library in Python is
built on it. Each array has a `shape` (dimensions), `dtype` (number
type), `ndim` (how many dimensions), and `size` (total elements).
`np.random.seed(42)` freezes randomness so results are reproducible.

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

**Why ML cares:** A dataset IS an array — rows are samples, columns
are features. `axis=0` (down columns) gives per-feature stats, used
for normalization. `axis=1` (across rows) gives per-sample values.
Everything in levels 04+ is array math.

**Code:**
```python
np.random.seed(42)
arr = np.random.randint(0, 100, size=(4, 5))
```

**Common confusion:** `axis=0` means "collapse along rows," giving
one value PER COLUMN — the opposite of intuition. Mnemonic: the
axis you name is the one that disappears.

---

### 2. Pandas DataFrames — `p02`

**What it is:** A DataFrame is a labeled table — think spreadsheet
in Python. Columns have names and types; rows are records. In ML,
raw data almost always lands in a DataFrame before becoming arrays.

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

**Why ML cares:** Data cleaning — the step that eats 80% of real ML
work — is DataFrame work: inspecting (`head`, `dtypes`, `shape`),
fixing types, filling gaps, encoding text. `object` dtype means
"text/mixed" — models can't eat it until you convert it.

**Code:**
```python
df = pd.DataFrame({'name': [...], 'age': [...], 'city': [...]})
print(df.head(), df.shape, df.dtypes)
```

**Common confusion:** `df['age']` is a Series (one column);
`df[['age']]` is a DataFrame (one-column table). Some sklearn
functions demand the 2D version — watch for "expected 2D array"
errors.

---

### 3. Filling Missing Values (Imputation) — `p03`

**What it is:** Real data has holes — `NaN` ("Not a Number") marks
them. Models crash on NaN, so you must fill them. Strategy:
numeric column → **median** (middle value, ignores outliers);
category column → **mode** (most frequent value).

**Worked example:**
```
age:   [25, NaN, 30, NaN, 35]   → median of [25,30,35] = 30
score: [85, 90, NaN, 78, 92]    → median of [78,85,90,92] = 87.5
city:  [Mumbai, Delhi, NaN, Chennai, NaN]
       → counts: Chennai 1(+2 NaN)... mode of known = tie broken
         by appearance counts → 'Chennai' appears most in this task

Filled:
  age   [25, 30, 30, 30, 35]
  score [85, 90, 87.5, 78, 92]
  city  [Mumbai, Delhi, Chennai, Chennai, Chennai]
```

**Why ML cares:** Missing data is guaranteed in every real dataset.
Median beats mean when outliers exist: mean of [10, 12, 11, 500] is
133 (absurd); median is 11.5 (sane). Mode is the only fill that
makes sense for text categories.

**Code:**
```python
df['age']   = df['age'].fillna(df['age'].median())
df['city']  = df['city'].fillna(df['city'].mode()[0])
```

**Common confusion:** `mode()` returns a Series, not a value —
that's why you need `[0]`. And fill BEFORE splitting data? That
computes medians using test data — leakage (see `hard/p01`).

---

## Medium

### 4. sklearn Pipelines — `p01`

**What it is:** A `Pipeline` chains preprocessing + model into ONE
object. Steps run in order: impute → scale → model. The magic: when
you call `pipe.fit(X_train)`, every step sees ONLY training data —
leakage is impossible.

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

**Why ML cares:** Without a pipeline you'd manually juggle "fill NaN
with train's mean, scale by train's std, then train" — one mistake
and test stats contaminate training. Pipelines make the correct way
the easy way. Every sklearn project uses them.

**Code:**
```python
from sklearn.pipeline import Pipeline
pipe = Pipeline([('imputer', SimpleImputer()),
                 ('scaler', StandardScaler()),
                 ('model', LogisticRegression())])
```

**Common confusion:** `pipe.fit` calls `fit_transform` on each
preprocessing step but `fit` on the final model — sklearn handles
the difference. And `score(X_test)` transforms test with TRAIN's
parameters, never re-fits.

---

### 5. Outlier Detection with IQR — `p02`

**What it is:** **Outliers** are values absurdly far from the rest —
they drag means and distort models. The IQR rule: compute Q1 (25th
percentile) and Q3 (75th percentile); IQR = Q3−Q1. Anything outside
`[Q1 − 1.5·IQR, Q3 + 1.5·IQR]` is an outlier. **Capping** replaces
outliers with the boundary value instead of deleting rows.

**Worked example:**
```
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]

Q1 = 3.25,  Q3 = 7.75,  IQR = 4.5
lower = 3.25 − 1.5×4.5 = −3.5
upper = 7.75 + 1.5×4.5 = 14.5

100 > 14.5 → outlier!
Capped: [1, 2, 3, 4, 5, 6, 7, 8, 9, 14.5]   → 1 outlier found
```

**Why ML cares:** One corrupt sensor reading or data-entry typo can
wreck a model — especially regression (one huge value warps the
whole line) and KNN (one far point distorts all distances). Capping
keeps the row but removes the poison.

**Code:**
```python
Q1, Q3 = np.percentile(data, [25, 75])
IQR = Q3 - Q1
lower, upper = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR
n_outliers = int(((data < lower) | (data > upper)).sum())
cleaned = np.clip(data, lower, upper)
```

**Common confusion:** Don't DELETE outliers blindly — sometimes they
ARE the signal (fraud detection, disease). Capping with `np.clip`
is the safer default: the sample stays, the extreme value doesn't.

---

### 6. Mixed Data Types — `p03`

**What it is:** Real datasets mix text dates, categories, and
numbers. Models only understand numbers, so each type needs its own
conversion: date strings → `pd.to_datetime`, categories →
`LabelEncoder` (each label becomes an int), numbers →
`StandardScaler` ((x − mean) / std).

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

**Why ML cares:** You can't `model.fit` on "Mumbai" — strings crash
every algorithm. And unscaled features (age 0-100 vs income
0-120000) make bigger-magnitude columns dominate distance and
gradient calculations.

**Code:**
```python
df['signup_date'] = pd.to_datetime(df['signup_date'])
df['city_encoded'] = LabelEncoder().fit_transform(df['city'])
df['age_scaled'] = StandardScaler().fit_transform(df[['age']])
```

**Common confusion:** `LabelEncoder` invents a fake ordering
(Mumbai=3 > Delhi=2) that can mislead linear models — for model
features, `OneHotEncoder` is safer (see `hard/p02`). LabelEncoder is
fine for LABELS (y), risky for FEATURES (X).

---

## Hard

### 7. Data Leakage — `p01`

**What it is:** Leakage = test data influencing training. The
classic bug: compute medians/scaling on ALL data, THEN split — the
test set's statistics just leaked into what the model learned.
Result: inflated scores that vanish in production. Rule: **split
first**, fit preprocessing on train only.

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

**Why ML cares:** Leakage is the #1 silent killer of real ML
projects — papers have been retracted over it. Any preprocessing
fit on full data (imputation, scaling, feature selection, SMOTE)
is a leak. A `Pipeline` fit after splitting is the fix.

**Code:**
```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)      # split FIRST
pipe = Pipeline([('pre', preprocessor),
                 ('model', RandomForestClassifier(n_estimators=50,
                                                  random_state=42))])
pipe.fit(X_train, y_train)                     # preprocessor sees train only
```

**Common confusion:** It "leaks" even though the model never sees
test ROWS — the test data's STATISTICS leaked through the mean/
median you computed. That's subtle enough to fool experienced devs.

---

### 8. ColumnTransformer — `p02`

**What it is:** Different columns need different preprocessing —
numbers get impute+scale, categories get impute+one-hot-encode.
`ColumnTransformer` applies each pipeline to its own column list in
one step, then glues the results back together.

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

**Why ML cares:** This is THE production-grade pattern for tabular
data. `fit_transform` on the DataFrame gives one clean numeric
matrix for the model — no manual column surgery. Wrap it in a
Pipeline with the classifier and you also get leak-free splits.

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

**Common confusion:** `LabelEncoder` turns 'B' into `1` — one number
with a fake order. `OneHotEncoder` turns 'B' into `[0,1,0]` — one
binary column per category, no ordering implied. For model features,
one-hot is the safe choice.

---

### 9. Stratified Splitting — `p03`

**What it is:** With imbalanced classes (95% negative / 5%
positive), a random split can starve one side of minority samples —
e.g., only 7 positives land in test, making the test score noisy
luck. `stratify=y` forces both splits to keep the SAME class ratio
as the full data.

**Worked example:**
```
1000 samples: 950 class-0, 50 class-1  (5%)

Random split (no stratify):   train [757, 43]   test [193, 7]
                              test is only 3.5% positive — skewed!

Stratified split:             train [760, 40]   test [190, 10]
                              test is exactly 5% positive ✓
```

**Why ML cares:** A test set with 7 positive samples can't measure
anything — one lucky guess swings accuracy 14%. Medical, fraud, and
churn data are all imbalanced, so `stratify=y` should be your
default reflex for classification splits.

**Code:**
```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)
np.bincount(y_train)   # verify ratios preserved
```

**Common confusion:** Stratify does NOT balance the classes — it
PRESERVES the imbalance (5% stays 5%). To actually balance classes
you need resampling/SMOTE, which is a different (training-only)
tool.

---

## Done with concepts? → Try `easy/p01-create-array.py`
