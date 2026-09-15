# Lesson 12 — Coding Check

## Easy

### p01-solve.py — Imbalanced dataset demo
- [ ] Dataset created (95% class 0, 5% class 1)
- [ ] Logistic regression trained
- [ ] Accuracy printed (high)
- [ ] Classification report printed
- [ ] Recall for class 1 is low (near 0)
- [ ] Problem demonstrated

### p02-solve.py — Class weights
- [ ] `class_weight='balanced'` used
- [ ] Classification report with weights printed
- [ ] Classification report without weights printed
- [ ] Recall for class 1 improved with weights
- [ ] Comparison clear

### p03-solve.py — Stratified split
- [ ] `stratify=y` used in train_test_split
- [ ] Train class counts printed
- [ ] Test class counts printed
- [ ] Both have same class ratio (e.g., 95:5)
- [ ] Without stratify → ratios might differ

## Medium

### p01-solve.py — Over/undersampling
- [ ] `RandomOverSampler` applied
- [ ] `RandomUnderSampler` applied
- [ ] Class counts before and after printed
- [ ] Model trained on oversampled data
- [ ] Model trained on undersampled data
- [ ] F1 scores compared

### p02-solve.py — SMOTE in pipeline
- [ ] `SMOTE` used
- [ ] `imblearn.pipeline.Pipeline` used (not sklearn's)
- [ ] SMOTE applied inside CV (no leakage)
- [ ] Model trained with SMOTE
- [ ] F1 compared with random oversampling
- [ ] SMOTE performs better or similar

### p03-solve.py — Threshold adjustment
- [ ] `predict_proba` used
- [ ] Thresholds 0.3, 0.5, 0.7 tested
- [ ] For each: precision, recall, F1 printed
- [ ] Optimal threshold identified (max F1)
- [ ] Trade-off explained (lower threshold → higher recall, lower precision)

## Hard

### p01-solve.py — Complete imbalanced pipeline
- [ ] 99:1 dataset created
- [ ] 4 approaches compared: baseline, class_weight, SMOTE, SMOTE+undersampling
- [ ] For each: F1, PR-AUC, confusion matrix printed
- [ ] Results in a comparison table
- [ ] Best approach identified
- [ ] Explanation of why it's best

### p02-solve.py — Fraud detection simulation
- [ ] Synthetic transaction data created
- [ ] Features: amount, merchant, time, is_fraud
- [ ] Imbalance handled with SMOTE
- [ ] Model trained
- [ ] Precision-recall curve plotted
- [ ] Threshold for 80% recall found
- [ ] Precision at that threshold reported
- [ ] Results interpreted

### p03-solve.py — Metric comparison
- [ ] Model trained on imbalanced data
- [ ] Accuracy calculated (high, misleading)
- [ ] F1 calculated (low, honest)
- [ ] ROC-AUC calculated (can be misleading)
- [ ] PR-AUC calculated (honest)
- [ ] ROC curve plotted
- [ ] PR curve plotted
- [ ] Explanation: PR-AUC is more honest for imbalanced data
