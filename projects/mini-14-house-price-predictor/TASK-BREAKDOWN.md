# House Price Predictor (ML) — Task Breakdown

> **Step-by-step implementation guide.** Follow each step in order.

---

## File Structure

```
mini-14-house-price-predictor/
├── data_loader.py, model.py, predict.py, train.py, app.py
└── README.md
```

---

## Implementation Steps

### Step 1: Load Dataset

Use California Housing or Ames dataset. Split into X (features) and y (target).

**Checkpoint:** Step 1 is complete when the described functionality works.

### Step 2: EDA

Correlation heatmap, distribution plots, feature vs target scatter plots.

**Checkpoint:** Step 2 is complete when the described functionality works.

### Step 3: Feature Engineering

Create new features (rooms_per_household, bedrooms_per_room). Scale features.

**Checkpoint:** Step 3 is complete when the described functionality works.

### Step 4: Train Model

LinearRegression baseline. Then RandomForest. Cross-validation for both.

**Checkpoint:** Step 4 is complete when the described functionality works.

### Step 5: Evaluate

RMSE, MAE, R². Compare models. Feature importance plot.

**Checkpoint:** Step 5 is complete when the described functionality works.

### Step 6: Hyperparameter Tuning

GridSearchCV on RandomForest: n_estimators, max_depth, min_samples_split.

**Checkpoint:** Step 6 is complete when the described functionality works.

### Step 7: Save Model

joblib.dump the best model + scaler. Save feature names.

**Checkpoint:** Step 7 is complete when the described functionality works.

### Step 8: Prediction Script

predict.py: load model, take input (CLI or JSON), output prediction.

**Checkpoint:** Step 8 is complete when the described functionality works.

### Step 9: Simple API

FastAPI endpoint: POST /predict with feature values → price prediction.

**Checkpoint:** Step 9 is complete when the described functionality works.

---

## Final Checklist

- [ ] Dataset loaded and explored
- [ ] Feature engineering (new features)
- [ ] Feature scaling
- [ ] LinearRegression baseline
- [ ] RandomForest with tuning
- [ ] Cross-validation
- [ ] RMSE/MAE/R² metrics
- [ ] Model saved with joblib
- [ ] Prediction CLI
- [ ] FastAPI prediction endpoint

---

## Common Pitfalls

1. **Skipping steps** — each step builds on the previous. Don't jump ahead.
2. **Not testing incrementally** — test after each step, not just at the end.
3. **Ignoring error states** — handle empty states, loading, and errors from the start.
4. **Not making it responsive** — test on mobile from the beginning, not as an afterthought.
5. **Hardcoding values** — use environment variables for API keys, URLs, and configuration.
