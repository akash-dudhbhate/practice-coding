# Lesson 01 — Coding Check

Use this to verify your answers before asking me to review. These are concept questions — the check is whether your reasoning is correct and in your own words.

## Easy

### p01-classify-problem-type.py
- [ ] A (house price) → supervised-regression (predicting a number)
- [ ] B (shopper clusters) → unsupervised (no labels given)
- [ ] C (tumor malignant/benign) → supervised-classification (categories)
- [ ] Each has a one-line reason.

### p02-identify-features-labels.py
- [ ] A (student pass/fail): 3 features listed, label = pass/fail (binary)
- [ ] B (store sales): 3 features listed, label = sales amount (number)

### p03-traditional-vs-ml.py
- [ ] A (cart total) → traditional (fixed formula)
- [ ] B (spam detection) → ml (complex, changing patterns)
- [ ] C (sorting) → traditional (well-defined algorithm)
- [ ] D (movie recommendations) → ml (subtle taste patterns)

## Medium

### p01-design-spam-classifier.py
- [ ] Q1: supervised classification (labeled spam/not-spam)
- [ ] Q2: 5 features listed (e.g., sender, subject keywords, links, attachments, time)
- [ ] Q3: label = spam (yes/no or 1/0)
- [ ] Q4: data source mentioned (labeled emails from users/providers)
- [ ] Q5: one metric named (accuracy, precision, recall, etc.)

### p02-train-test-split.py
- [ ] Q1: explains why we need unseen test data to evaluate generalization
- [ ] Q2: 80/20 or 70/30 mentioned
- [ ] Q3: overfitting = model memorizes training data, fails on new data
- [ ] Q4: 99% train / 60% test = overfitting

### p03-match-algorithm-to-problem.py
- [ ] A (temperature) → linear-regression
- [ ] B (customer segments) → kmeans-clustering
- [ ] C (spam/not-spam) → logistic-regression
- [ ] D (house prices) → linear-regression or decision-tree
- [ ] E (object recognition) → neural-network

## Hard

### p01-full-ml-pipeline-design.py
- [ ] Q1: supervised classification
- [ ] Q2: 6 features + label (diabetes yes/no)
- [ ] Q3: data source + privacy concerns (HIPAA, patient consent)
- [ ] Q4: 3 preprocessing steps (normalization, missing values, encoding)
- [ ] Q5: 2 algorithms with reasons
- [ ] Q6: 2 metrics + why accuracy alone is misleading (class imbalance)
- [ ] Q7: practical deployment described
- [ ] Q8: 2 ethical risks (bias, false positives/negatives impact)

### p02-confusion-matrix-intuition.py
- [ ] Q1: TP = 35 (sick and tested positive)
- [ ] Q2: FP = 10 (healthy but tested positive)
- [ ] Q3: TN = 50 (healthy and tested negative)
- [ ] Q4: FN = 5 (sick but tested negative)
- [ ] Q5: accuracy = (35+50)/100 = 85%
- [ ] Q6: false negative is worse (missed disease > false alarm)

### p03-bias-variance-tradeoff.py
- [ ] Q1: bias = error from wrong assumptions (oversimplification)
- [ ] Q2: variance = sensitivity to training data (noise fitting)
- [ ] Q3: high bias + low variance = underfitting
- [ ] Q4: low bias + high variance = overfitting
- [ ] Q5: decision tree case = high variance → prune/limit depth
- [ ] Q6: linear regression case = high bias → use more complex model
- [ ] Q7: tradeoff because reducing bias usually increases variance

## How to verify

Run each file to print your answers:
```bash
python easy/p01-classify-problem-type.py
```
