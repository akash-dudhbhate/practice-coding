# Lesson 02 — Concepts Explained (Data Preprocessing)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Missing Value Handling

**What:**
Real-world datasets often have gaps — cells that are empty, `NaN`, `None`, or a placeholder like `-999`. You must decide how to fill or remove them before training, because most ML algorithms cannot handle missing values directly.

```python
import pandas as pd
from sklearn.impute import SimpleImputer

df = pd.DataFrame({"age": [25, 30, None, 45], "income": [50000, None, 70000, 90000]})

# Strategy 1: drop rows with any missing values
df_dropped = df.dropna()

# Strategy 2: fill (impute) with the mean
imputer = SimpleImputer(strategy="mean")
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
# age column: [25, 30, 33.33, 45]  — the None is replaced by the mean of the others
```

Common strategies: `mean`, `median`, `most_frequent` (mode), or `constant` (fill with a fixed value like 0 or "Unknown").

**Why it exists:** Data collection is imperfect — sensors fail, users skip form fields, databases lose entries. If you drop every row with a missing value you may lose most of your data. Imputation lets you keep rows while making a reasonable guess for the gap.

**Where it's used:**
- Medical datasets where not every patient took every test.
- Survey data where respondents skip questions.
- IoT/sensor logs where devices go offline intermittently.
- E-commerce user profiles with optional fields.

**What goes wrong without it:**
- `ValueError: Input contains NaN` — sklearn crashes the moment it sees a missing value.
- Dropping too many rows → you lose 60% of your dataset → model underfits.
- Imputing with the mean on a highly skewed column → the mean is misleading (e.g., mean income pulled up by billionaires) → distorted feature.
- Imputing before train/test split → **data leakage**: the mean includes test data → inflated scores. Always fit the imputer on the training set only, then transform the test set.

---

## Categorical Encoding (Label & One-Hot)

**What:**
ML models only understand numbers. Categorical columns (text labels like "red", "Mumbai", "cat") must be converted to numeric form. Two main approaches:

```python
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

df = pd.DataFrame({"color": ["red", "blue", "green", "red", "blue"]})

# Label Encoding: assign each category a unique integer
le = LabelEncoder()
df["color_encoded"] = le.fit_transform(df["color"])
# red=2, blue=0, green=1  (order depends on alphabetical sort)

# One-Hot Encoding: create a binary column per category
df_ohe = pd.get_dummies(df, columns=["color"], prefix="color")
# color_blue  color_green  color_red
#    0            0           1
#    1            0           0
#    0            1           0
```

**Why it exists:** Models do math on numbers. "red" + "blue" is meaningless, but `0 + 1` works. The question is HOW to map categories to numbers without introducing false relationships.

**Where it's used:**
- One-hot: nominal categories (no inherent order) — color, city, product type.
- Label/ordinal encoding: ordinal categories (natural order) — "low/medium/high", "bad/good/excellent", education level.
- Feature engineering for any tabular dataset with text columns.

**What goes wrong without it:**
- Label encoding on nominal data → model thinks "red=2 > blue=0" implies an ordering → learns a false pattern → wrong predictions.
- One-hot encoding a column with 10,000 unique values → you create 10,000 columns → memory explosion and the **curse of dimensionality** → model overfits.
- Forgetting to handle unseen categories at inference time → `ValueError: unseen label` in production when a new category appears that wasn't in training.

---

## Feature Scaling (Standardization)

**What:**
Standardization rescales each feature so it has **mean = 0** and **standard deviation = 1**. This puts all features on the same numeric scale regardless of their original units.

```python
from sklearn.preprocessing import StandardScaler
import numpy as np

X = np.array([[25, 50000], [30, 70000], [45, 90000]])  # age (0-100), income (0-100000+)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
# age:     [-1.06, -0.53, 1.60]   mean=0, std=1
# income:  [-1.22, 0.0, 1.22]     mean=0, std=1
```

Formula: `z = (x - mean) / std`

**Why it exists:** Many algorithms use distance or gradient-based optimization. If one feature ranges 0–100 and another 0–1,000,000, the large feature dominates. Scaling ensures every feature contributes equally.

**Where it's used:**
- Distance-based algorithms: KNN, SVM, K-Means — they compute distances between points.
- Gradient-based algorithms: logistic regression, neural networks — scaling speeds up convergence.
- Regularization (L1/L2) — penalties are applied per-feature; unscaled features get unfair penalties.
- NOT needed for tree-based models (decision trees, random forests) — they split on thresholds and are scale-invariant.

**What goes wrong without it:**
- KNN with unscaled data → the feature with the largest range dominates all distance calculations → other features are effectively ignored → wrong neighbors selected.
- Neural network training without scaling → gradients oscillate, convergence is extremely slow or gets stuck → model never learns.
- Regularization without scaling → large-valued features get penalized more just because their numbers are bigger, not because they're less important → wrong feature selection.

---

## Feature Scaling (Normalization / Min-Max)

**What:**
Normalization (Min-Max scaling) rescales features to a fixed range, typically **[0, 1]**. Unlike standardization, it doesn't center around zero — it just squeezes everything into a bounded interval.

```python
from sklearn.preprocessing import MinMaxScaler

X = np.array([[25, 50000], [30, 70000], [45, 90000]])
scaler = MinMaxScaler()
X_normalized = scaler.fit_transform(X)
# age:    [0.0, 0.22, 1.0]     — 25 maps to 0, 45 maps to 1
# income: [0.0, 0.5, 1.0]      — 50000 maps to 0, 90000 maps to 1
```

Formula: `x_scaled = (x - min) / (max - min)`

**Why it exists:** Some algorithms (especially neural networks with sigmoid activation) expect inputs in [0, 1]. Normalization also preserves the original distribution shape (just rescaled), while standardization changes it. It's also useful when you need bounded values (e.g., pixel intensities 0–255 → 0–1).

**Where it's used:**
- Image processing: pixel values 0–255 normalized to 0–1 for neural networks.
- Neural networks with sigmoid/tanh activations.
- Algorithms sensitive to outliers less than standardization (but still affected).
- When you need a specific bounded range.

**What goes wrong without it:**
- Feeding raw pixel values (0–255) into a neural network → large inputs cause exploding gradients → unstable training.
- Min-Max is very sensitive to outliers — a single value of 1,000,000 in an otherwise 0–100 column compresses everything else to near-zero → information lost.
- Confusing normalization with standardization → using Min-Max when you need zero-centered data for a neural network → slower convergence.

---

## Train/Test Split Before Preprocessing

**What:**
You must split your data into train and test sets BEFORE fitting any preprocessing (imputer, scaler, encoder). The preprocessing is **fit on the training data only**, then **applied (transformed) to both train and test**.

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # fit AND transform on train
X_test_scaled = scaler.transform(X_test)         # transform ONLY on test
```

Note: `fit_transform` on train, `transform` only on test. Never call `fit` on test data.

**Why it exists:** The test set simulates unseen real-world data. If you fit the scaler on the entire dataset (including test), information from the test set leaks into training — the model "knows" the test distribution. This is called **data leakage** and produces overly optimistic scores that collapse in production.

**Where it's used:**
- Every ML pipeline that involves preprocessing + evaluation.
- Scikit-learn's `Pipeline` class automates this correctly.
- Kaggle competitions — leakage is the #1 reason for leaderboard shake-ups.

**What goes wrong without it:**
- Fitting scaler on all data → test scores look 5-10% better than reality → you deploy → production performance is much worse.
- Fitting imputer on all data → the imputed values in the test set are influenced by test data → leakage.
- Using `fit_transform` on test set → the test set gets its own scaling parameters → inconsistent with training → wrong predictions.
- Hard to detect — everything looks fine in your notebook, fails silently in production.

---

## Handling Outliers

**What:**
Outliers are data points that are far from the rest — abnormally high, low, or just different. They can be legitimate (a billionaire's income) or errors (a sensor glitch recording 999°C). You detect them with statistical methods and decide whether to remove, cap, or keep them.

```python
import numpy as np

# Method 1: IQR (Interquartile Range) method
Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = data[(data < lower_bound) | (data > upper_bound)]

# Method 2: Z-score (flag values more than 3 std devs from mean)
from scipy import stats
z_scores = stats.zscore(data)
outliers = data[np.abs(z_scores) > 3]

# Method 3: Capping (winsorization) — replace extreme values with the boundary
data_capped = np.clip(data, lower_bound, upper_bound)
```

**Why it exists:** Outliers distort mean, standard deviation, and regression lines. A single extreme value can pull a regression line far off course. But blindly removing all outliers can delete legitimate, important data points. You need a principled approach.

**Where it's used:**
- Fraud detection — outliers ARE the signal (unusual transactions = fraud).
- Sensor data cleaning — removing equipment malfunction readings.
- Financial modeling — deciding whether extreme market events should be included.
- House price prediction — removing data-entry errors (e.g., 100-bedroom house).

**What goes wrong without it:**
- A single outlier in training data → regression line is pulled toward it → all predictions are skewed.
- Mean imputation with outliers present → the mean is distorted → imputed values are wrong.
- Min-Max scaling with an outlier → all normal values compressed to a tiny range → information lost.
- Removing legitimate outliers (e.g., removing all high-income customers) → model can't predict for that segment → biased model.
- Keeping error outliers → model learns from garbage → wrong patterns.

---

## Handling Duplicate Data

**What:**
Duplicate rows are identical entries that appear more than once. They can arise from data collection errors, joining tables, or repeated API calls. You detect and remove them to prevent the model from over-weighting repeated examples.

```python
import pandas as pd

df = pd.DataFrame({"name": ["Alice", "Bob", "Alice", "Charlie"], "age": [25, 30, 25, 35]})
# Row 0 and Row 2 are duplicates

df_deduplicated = df.drop_duplicates()
# Keeps: Alice(25), Bob(30), Charlie(35)

# Check for duplicates
num_duplicates = df.duplicated().sum()
```

**Why it exists:** If the same row appears 10 times, the model sees it as 10 separate examples and gives it 10x the weight. This biases the model toward duplicated patterns and inflates training metrics.

**Where it's used:**
- Web scraping cleanup — pages crawled multiple times.
- Database merges — join operations producing duplicate rows.
- Log data — events logged multiple times due to retries.
- Survey data — respondents submitting the form twice.

**What goes wrong without it:**
- 500 duplicate rows of one pattern → model overfits to that pattern → poor generalization.
- Train/test split with duplicates in both → the same row appears in train AND test → data leakage → inflated test score.
- Evaluation metrics are skewed → the model appears to perform well on duplicated examples but fails on unique ones.
- Training takes longer (more rows to process) with no additional information.

---

## Data Type Conversion

**What:**
Columns in a DataFrame have types (int, float, string, datetime). Often the loaded type doesn't match what you need — numbers stored as strings, dates as text, categories as objects. You must convert them before processing.

```python
import pandas as pd

df = pd.DataFrame({"price": ["$100", "$200", "$300"], "date": ["2024-01-01", "2024-02-01", "2024-03-01"]})

# Convert string prices to numeric (strip the $ sign first)
df["price"] = df["price"].str.replace("$", "").astype(float)

# Convert string dates to datetime objects
df["date"] = pd.to_datetime(df["date"])

# Convert float to int (when decimals are noise)
df["count"] = df["count"].astype(int)

# Convert object to category (saves memory for repeated strings)
df["city"] = df["city"].astype("category")
```

**Why it exists:** Data comes from many sources (CSV, SQL, APIs) and types get mangled. Strings that look like numbers aren't numbers — you can't do math on `"$100"`. Dates as strings can't be sorted or filtered by month. Type conversion is the bridge between raw data and usable data.

**Where it's used:**
- Loading CSV files where everything defaults to string/object.
- Preparing features for ML — models need numeric inputs.
- Memory optimization — converting repeated strings to `category` type can save 90% memory.
- Time-series analysis — datetime types enable resampling, rolling windows, date arithmetic.

**What goes wrong without it:**
- Numeric column stored as strings → `ValueError` when you try to scale or train → pipeline crashes.
- Dates as strings → sorting gives "01-02-2024" before "01-03-2023" (alphabetical, not chronological) → wrong time ordering.
- Float column that should be int → unnecessary memory usage, potential grouping issues.
- Forgetting to convert → silent bugs where operations produce wrong results (string concatenation instead of numeric addition: `"10" + "20" = "1020"` instead of `30`).

---

## Sklearn Pipeline

**What:**
A `Pipeline` chains multiple preprocessing steps and a model into a single object. When you call `fit()`, it runs each step in order. When you call `predict()`, it applies the same transformations to new data. This guarantees consistency and prevents leakage.

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression

pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="mean")),   # Step 1: fill missing values
    ("scaler", StandardScaler()),                   # Step 2: scale features
    ("model", LogisticRegression())                 # Step 3: train model
])

pipeline.fit(X_train, y_train)    # runs imputer.fit_transform → scaler.fit_transform → model.fit
predictions = pipeline.predict(X_test)  # runs imputer.transform → scaler.transform → model.predict
```

**Why it exists:** Without a pipeline, you manually call fit/transform on each step. It's easy to forget to transform the test set, or to accidentally fit on test data. The pipeline makes the correct behavior automatic — you literally cannot fit on test data because the pipeline only exposes `fit` (train) and `predict`/`transform` (apply).

**Where it's used:**
- Every production ML pipeline.
- Cross-validation — `cross_val_score(pipeline, X, y)` correctly refits preprocessing on each fold.
- Hyperparameter tuning — `GridSearchCV(pipeline, params)` tunes preprocessing + model together.
- Deploying models — save one pipeline object, load it, and everything works.

**What goes wrong without it:**
- Manual preprocessing → you forget to apply the scaler to test data → model gets unscaled inputs → wrong predictions.
- Manual preprocessing → you accidentally fit the imputer on the full dataset → data leakage → inflated scores.
- Cross-validation without a pipeline → preprocessing is done once on all data, not per-fold → leakage across folds → CV scores look great, real performance is worse.
- Adding a new preprocessing step → you have to manually wire it into every code path → bugs.

---

## Train/Test Split (with stratify)

**What:**
`train_test_split` divides data into training and testing sets. The `stratify` parameter ensures the class distribution is preserved in both splits — if 20% of your data is positive, both train and test will have ~20% positive.

```python
from sklearn.model_selection import train_test_split

# Without stratify — random split, class ratio may differ
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# With stratify — class ratio preserved in both splits
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
```

**Why it exists:** In a random split, a rare class (e.g., 5% of data) might end up as 0% in the test set by chance. Then you can't evaluate the model on that class at all. Stratification guarantees representation.

**Where it's used:**
- Classification problems with class imbalance.
- Any split where preserving the distribution matters.
- Multi-class classification — ensures all classes appear in both splits.

**What goes wrong without it:**
- Imbalanced data without stratify → test set has 0 examples of the minority class → recall is undefined (division by zero) → can't evaluate.
- Rare class all ends up in training → model can't be tested on it → you don't know if it works.
- Distribution mismatch between train and test → model trained on 50/50 split but tested on 90/10 → scores are misleading.
- Multi-class without stratify → some classes missing from test set → per-class metrics are incomplete.
