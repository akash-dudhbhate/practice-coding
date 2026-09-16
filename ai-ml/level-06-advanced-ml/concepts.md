# Level 06 — Concepts Reference

## Easy

### Polynomial Features
- `PolynomialFeatures(degree=2)` — [x] → [x, x²]
- Linear model on nonlinear data → add nonlinear features, keep linear model

### One-Hot Encoding
- `pd.get_dummies(df)` — each category → 0/1 column
- Prefer over LabelEncoder for non-ordinal categories

### Feature Scaling
- StandardScaler: mean=0, std=1. MinMaxScaler: range [0,1]
- Fit on train, transform test — never fit on test

## Medium

### Manual Oversampling
- `np.random.choice(minority_idx, size=needed, replace=True)`
- Duplicates minority samples until classes balance

### Feature Selection
- `rf.feature_importances_` → `np.argsort(...)[-5:]`
- Top features often beat all features (less noise)

### PCA
- `PCA(n_components=3)` → top components capture most variance
- `explained_variance_ratio_` → how much info each keeps

## Hard

### Custom Transformer
- Subclass `BaseEstimator + TransformerMixin`, implement fit/transform
- Plugs into any sklearn Pipeline

### Feature Engineering
- Ratios (income/age), polynomials (age²), flags (is_weekend)
- The right feature can make a weak model strong

### class_weight
- `class_weight='balanced'` — model pays more attention to minority
- Tradeoff: better recall, worse precision (fewer misses, more alarms)
