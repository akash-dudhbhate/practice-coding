# Lesson 11 — Coding Check

## Easy

### p01-solve.py — One-hot encoding
- [ ] Categorical column created (color: red/blue/green)
- [ ] `pd.get_dummies` used
- [ ] Before encoding printed
- [ ] After encoding printed
- [ ] Binary columns created for each category

### p02-solve.py — StandardScaler
- [ ] Two columns with different scales created
- [ ] `StandardScaler` applied
- [ ] Before scaling printed
- [ ] After scaling printed
- [ ] Scaled data has mean≈0, std≈1

### p03-solve.py — Missing data
- [ ] DataFrame with NaN values created
- [ ] Numerical column filled with median
- [ ] Categorical column filled with mode
- [ ] Before filling printed
- [ ] After filling printed (no NaN)

## Medium

### p01-solve.py — Date feature engineering
- [ ] Date column created
- [ ] Converted to datetime
- [ ] Year extracted
- [ ] Month extracted
- [ ] Day of week extracted
- [ ] is_weekend feature created
- [ ] Quarter extracted
- [ ] All features printed

### p02-solve.py — House dataset interactions
- [ ] Dataset with sqft, bedrooms, price created
- [ ] price_per_sqft engineered
- [ ] total_rooms engineered
- [ ] bedrooms_per_sqft engineered
- [ ] Model trained without engineered features
- [ ] Model trained with engineered features
- [ ] R² compared (should improve)

### p03-solve.py — Text features
- [ ] 10+ sentences created
- [ ] Text length extracted
- [ ] Word count extracted
- [ ] has_url feature created
- [ ] has_question_mark feature created
- [ ] TF-IDF vectorization applied
- [ ] All features combined

## Hard

### p01-solve.py — Complete pipeline
- [ ] Real dataset loaded (Titanic or similar)
- [ ] Missing data handled
- [ ] Categoricals encoded
- [ ] Numericals scaled
- [ ] Interaction features created
- [ ] Top 10 features selected
- [ ] Model trained with engineered features
- [ ] Model trained with raw data
- [ ] Performance compared

### p02-solve.py — Feature engineering stages
- [ ] Stage (a): raw features → accuracy
- [ ] Stage (b): scaled features → accuracy
- [ ] Stage (c): scaled + encoded → accuracy
- [ ] Stage (d): scaled + encoded + interactions → accuracy
- [ ] Accuracy printed for each stage
- [ ] Improvement shown at each step
- [ ] Results visualized (bar chart or table)

### p03-solve.py — Text classification pipeline
- [ ] 20+ documents in 2 categories created
- [ ] TF-IDF features extracted
- [ ] Custom features added (length, word count, sentiment)
- [ ] All features combined
- [ ] Classifier trained
- [ ] Model evaluated (accuracy, F1)
- [ ] Most important features identified
- [ ] Results printed
