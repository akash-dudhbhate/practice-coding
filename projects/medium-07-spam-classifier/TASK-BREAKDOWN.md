# Spam Classifier (ML) — Task Breakdown

> **Step-by-step implementation guide.** Follow each step in order.

---

## File Structure

```
medium-07-spam-classifier/
├── data_loader.py, preprocess.py, model.py, train.py, predict.py, app.py
└── README.md
```

---

## Implementation Steps

### Step 1: Dataset

Use SMS Spam Collection or Enron dataset. Load, explore class distribution.

**Checkpoint:** Step 1 is complete when the described functionality works.

### Step 2: Text Preprocessing

Lowercase, remove punctuation, tokenize, remove stopwords, lemmatize.

**Checkpoint:** Step 2 is complete when the described functionality works.

### Step 3: Vectorization

TF-IDF vectorizer. Fit on training data. ngram_range=(1,2).

**Checkpoint:** Step 3 is complete when the described functionality works.

### Step 4: Train Models

Naive Bayes baseline. Logistic Regression. Compare with cross-validation.

**Checkpoint:** Step 4 is complete when the described functionality works.

### Step 5: Evaluate

Accuracy, precision, recall, F1, confusion matrix. ROC curve. Class imbalance handling.

**Checkpoint:** Step 5 is complete when the described functionality works.

### Step 6: Hyperparameter Tuning

GridSearchCV: alpha for NB, C for LR. Tune TF-IDF params.

**Checkpoint:** Step 6 is complete when the described functionality works.

### Step 7: Save Pipeline

joblib: save vectorizer + model as a pipeline. Load for prediction.

**Checkpoint:** Step 7 is complete when the described functionality works.

### Step 8: Prediction API

FastAPI: POST /classify with text → {is_spam, probability}. Test with examples.

**Checkpoint:** Step 8 is complete when the described functionality works.

### Step 9: Testing

Test with real spam/ham examples. Edge cases: empty, very long, emoji-only.

**Checkpoint:** Step 9 is complete when the described functionality works.

---

## Final Checklist

- [ ] Dataset loaded and explored
- [ ] Text preprocessing pipeline
- [ ] TF-IDF vectorization
- [ ] Naive Bayes + Logistic Regression
- [ ] Cross-validation
- [ ] Precision/recall/F1/confusion matrix
- [ ] Hyperparameter tuning
- [ ] Model saved as pipeline
- [ ] FastAPI classification endpoint
- [ ] Tested with real examples

---

## Common Pitfalls

1. **Skipping steps** — each step builds on the previous. Don't jump ahead.
2. **Not testing incrementally** — test after each step, not just at the end.
3. **Ignoring error states** — handle empty states, loading, and errors from the start.
4. **Not making it responsive** — test on mobile from the beginning, not as an afterthought.
5. **Hardcoding values** — use environment variables for API keys, URLs, and configuration.
