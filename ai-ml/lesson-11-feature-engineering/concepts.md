# Lesson 11 — Concepts Explained (Feature Engineering)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## What is Feature Engineering?

**What:** Creating new features from existing data to help the model learn better.

```python
# Raw data: date column
df['date'] = ['2024-01-15', '2024-02-20', '2024-03-10']

# Engineered features:
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year          # 2024
df['month'] = df['date'].dt.month        # 1, 2, 3
df['day_of_week'] = df['date'].dt.dayofweek  # 0=Mon, 6=Sun
df['is_weekend'] = df['day_of_week'] >= 5    # False, False, True
```

**Why it exists:** Models can't extract patterns from raw data automatically. A date string tells the model nothing, but "is_weekend" tells it a lot. Feature engineering transforms raw data into model-friendly features → better performance.

**Where it's used:** Every ML project — often the highest-impact step. "Garbage in, garbage out" → good features matter more than the model choice.

**What goes wrong without it:**
- Feeding raw dates as strings → model treats them as categories → no temporal pattern learned.
- Not creating interaction features (e.g., price_per_sqft = price / sqft) → model misses obvious relationships.
- Over-engineering → too many features → curse of dimensionality → model overfits.

---

## Handling Categorical Variables

**What:** Convert categorical text data to numbers for ML models.

```python
# Label Encoding: assign a number to each category
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['category_encoded'] = le.fit_transform(df['category'])
# ['low', 'medium', 'high'] → [1, 2, 0]

# One-Hot Encoding: create a binary column per category
df_encoded = pd.get_dummies(df, columns=['category'])
# category_low | category_medium | category_high
#       1              0                0
#       0              1                0

# Ordinal Encoding: for ordered categories
mapping = {'low': 0, 'medium': 1, 'high': 2}
df['category_ordinal'] = df['category'].map(mapping)
```

**Why it exists:** ML models need numbers, not text. Encoding converts categories to numbers. Different encodings for different situations: one-hot for unordered, ordinal for ordered.

**Where it's used:** Every dataset with categorical columns (gender, city, product type).

**What goes wrong without it:**
- Label encoding for unordered categories → model thinks 2 > 1 > 0 → false ordering → bad predictions. Use one-hot encoding.
- One-hot encoding for high-cardinality features (1000 cities) → 1000 columns → sparse, slow. Use target encoding or embedding.
- Forgetting to handle unknown categories in test data → error. Use `handle_unknown='ignore'` in OneHotEncoder.

---

## Scaling and Normalization

**What:** Transform features to similar scales → models work better.

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

# Standardization: mean=0, std=1
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[['age', 'income']])

# Min-Max: scale to [0, 1]
scaler = MinMaxScaler()
df_scaled = scaler.fit_transform(df[['age', 'income']])

# Robust: uses median and IQR (resistant to outliers)
scaler = RobustScaler()
df_scaled = scaler.fit_transform(df[['age', 'income']])
```

**Why it exists:** Features with different scales (age: 20-80, income: 20000-200000) → models that use distance (KNN, SVM) or gradient descent (neural networks) are dominated by large-scale features → poor performance. Scaling makes features comparable.

**Where it's used:** Before training KNN, SVM, neural networks, logistic regression. NOT needed for tree-based models (trees split on values, not distances).

**What goes wrong without it:**
- Fitting scaler on full dataset (including test) → data leakage. Fit on train, transform test.
- Using MinMax with outliers → outliers squash all other values into a tiny range. Use RobustScaler.
- Scaling tree-based models → unnecessary, doesn't improve performance, wastes time.

---

## Handling Missing Data

**What:** Deal with missing values (NaN) in the dataset.

```python
# Drop rows with missing values
df_clean = df.dropna()

# Fill with mean/median/mode
df['age'].fillna(df['age'].mean(), inplace=True)
df['category'].fillna(df['category'].mode()[0], inplace=True)

# Forward fill (for time series)
df['value'].fillna(method='ffill', inplace=True)

# Using sklearn
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='median')
df_imputed = imputer.fit_transform(df[['age', 'income']])
```

**Why it exists:** Most ML models can't handle NaN → error. Missing data must be handled before training. Different strategies for different situations.

**Where it's used:** Every dataset with missing values — which is almost every real-world dataset.

**What goes wrong without it:**
- Dropping all rows with any NaN → might lose most of your data. Check how much is missing first.
- Filling with mean → skewed by outliers. Use median for skewed distributions.
- Not creating a "is_missing" indicator → the fact that a value was missing might be informative. Add `df['age_was_missing'] = df['age'].isna()`.

---

## Binning (Discretization)

**What:** Convert continuous values into discrete bins.

```python
# Equal-width binning
df['age_group'] = pd.cut(df['age'], bins=[0, 18, 35, 60, 100], labels=['child', 'young', 'adult', 'senior'])

# Equal-frequency (quantile) binning
df['income_quartile'] = pd.qcut(df['income'], q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])
```

**Why it exists:** Sometimes continuous values have non-linear relationships with the target. Binning captures this → "age 20-30 buys more" is easier to learn than a linear age effect.

**Where it's used:** Age groups, income brackets, price ranges — any continuous variable with natural groupings.

**What goes wrong without it:**
- Too many bins → overfitting (each bin has few samples). Too few → loses information.
- Equal-width with skewed data → most values in one bin. Use quantile binning instead.
- Binning when the relationship is actually linear → loses information. Check the relationship first.

---

## Feature Interactions

**What:** Create new features by combining existing ones.

```python
# Multiplication
df['price_per_sqft'] = df['price'] / df['sqft']

# Addition
df['total_rooms'] = df['bedrooms'] + df['bathrooms']

# Ratio
df['debt_to_income'] = df['debt'] / df['income']

# Polynomial features
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=2, interaction_only=True)
df_poly = poly.fit_transform(df[['age', 'income']])
# Creates: age, income, age*income
```

**Why it exists:** Models like linear regression can't capture interactions automatically. `price/sqft` is more informative than price and sqft separately. Interaction features give the model this information directly.

**Where it's used:** Any domain where feature combinations are meaningful — real estate, finance, e-commerce.

**What goes wrong without it:**
- Creating too many interactions → exponential features → overfitting, slow training.
- Division by zero → NaN. Handle: `df['ratio'] = df['a'] / df['b'].replace(0, np.nan)`.
- Interaction features for tree-based models → trees can find interactions automatically → less benefit.

---

## Text Features

**What:** Convert text data to numerical features.

```python
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

# Bag of Words: count word occurrences
vectorizer = CountVectorizer(max_features=1000)
X_text = vectorizer.fit_transform(df['text'])

# TF-IDF: term frequency * inverse document frequency
tfidf = TfidfVectorizer(max_features=1000, stop_words='english')
X_text = tfidf.fit_transform(df['text'])

# Basic text features
df['text_length'] = df['text'].str.len()
df['word_count'] = df['text'].str.split().str.len()
df['has_url'] = df['text'].str.contains('http').astype(int)
```

**Why it exists:** ML models need numbers, not text. Text vectorization converts text to numerical features → models can process it.

**Where it's used:** NLP tasks — sentiment analysis, spam detection, document classification.

**What goes wrong without it:**
- `max_features` not set → vocabulary is huge → thousands of columns → slow, overfits. Limit to top 1000-5000.
- Not removing stop words → "the", "is", "and" dominate → noise. Use `stop_words='english'`.
- CountVectorizer vs TfidfVectorizer: TF-IDF downweights common words → usually better. Use TF-IDF.

---

## Feature Selection

**What:** Select the most useful features → remove noise, reduce dimensionality.

```python
from sklearn.feature_selection import SelectKBest, f_classif

# Select top K features by statistical test
selector = SelectKBest(f_classif, k=10)
X_selected = selector.fit_transform(X, y)
selected_features = selector.get_feature_names_out()

# From model importance
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X, y)
importances = model.feature_importances_
top_features = np.argsort(importances)[-10:]
```

**Why it exists:** Too many features → overfitting, slow training, hard to interpret. Feature selection keeps only the useful ones → better performance, faster training, interpretable model.

**Where it's used:** After feature engineering → select the best subset before final training.

**What goes wrong without it:**
- Selecting features using the full dataset (including test) → data leakage. Select on train, apply to test.
- Selecting too few features → underfitting. Select too many → overfitting. Use CV to find the right number.
- Removing features that are useful in interaction → single-feature importance misses interactions. Use model-based selection.
