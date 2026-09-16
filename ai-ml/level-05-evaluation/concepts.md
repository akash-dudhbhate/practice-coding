# Level 05 — Concepts (Detailed Explanations)

Read each section BEFORE attempting its problem. Each concept has:
what it is in plain words → a worked example with real numbers →
why ML cares → the code → what confuses beginners.

---

## Easy

### 1. Accuracy, Precision, Recall, F1 — `p01`

**What it is:** Four ways to score a yes/no classifier, all built
from TP/FP/TN/FN. **Accuracy** = fraction correct overall.
**Precision** = of everything you flagged YES, what fraction was
actually yes. **Recall** = of everything actually YES, what fraction
you caught. **F1** = harmonic mean of precision and recall — one
number that punishes you if either is bad.

**Worked example:**
```
y_true = [0,0,1,1,1,0,1,0,1,1]
y_pred = [0,1,1,1,0,0,1,0,1,1]

TP=5 (both 1), FP=1 (pos 2: pred 1, true 0),
TN=3 (both 0), FN=1 (pos 5: pred 0, true 1)

accuracy  = (5+3)/10        = 0.800
precision = 5/(5+1)         = 0.833   ← 1 false alarm of 6 flags
recall    = 5/(5+1)         = 0.833   ← 1 miss of 6 real positives
f1        = 2·0.833·0.833/(0.833+0.833) = 0.833
(P and R tie here because FP = FN = 1 — usually they differ!)
```

**Why ML cares:** This is THE vocabulary of model evaluation — every
paper, dashboard, and interview uses it. The choice is a business
decision: spam wants precision (don't delete real mail); disease
screening wants recall (don't miss cases). Accuracy lies on
imbalanced data — always check P and R too.

**Code:**
```python
TP = sum(1 for t,p in zip(y_true,y_pred) if t==1 and p==1)
FP = sum(1 for t,p in zip(y_true,y_pred) if t==0 and p==1)
TN = sum(1 for t,p in zip(y_true,y_pred) if t==0 and p==0)
FN = sum(1 for t,p in zip(y_true,y_pred) if t==1 and p==0)
precision = TP/(TP+FP) if TP+FP else 0.0   # guard ÷0!
```

**Common confusion:** Precision's denominator is PREDICTED positives
(TP+FP); recall's is ACTUAL positives (TP+FN). Mnemonic: precision
asks "can I trust a YES?"; recall asks "did I miss any YESes?"

---

### 2. Confusion Matrix — `p02`

**What it is:** The 2×2 table every classification metric derives
from. Rows = reality, columns = prediction. TP = said yes, was yes;
FN = said no, was yes (a miss); FP = said yes, was no (false
alarm); TN = said no, was no.

**Worked example:**
```
y_true = [0,0,1,1,1,0,1,0,1,1]
y_pred = [0,1,1,1,0,0,1,0,1,1]

Position-by-position:
  idx0: 0→0 TN | idx1: 0→1 FP | idx2: 1→1 TP | idx3: 1→1 TP
  idx4: 1→0 FN | idx5: 0→0 TN | idx6: 1→1 TP | idx7: 0→0 TN
  idx8: 1→1 TP | idx9: 1→1 TP

Totals: TP=5, FP=1, TN=3, FN=1  (sum = 10 = all predictions)
```

**Why ML cares:** When someone says "the model is 80% accurate," the
confusion matrix shows WHERE the errors are — two FP and two FN
tell a different story than five FP and zero FN. Level-01 `hard/p02`
showed why: on 92%-healthy patients, "always healthy" hits 92%
accuracy with ZERO detected cases.

**Code:**
```python
def confusion(y_true, y_pred):
    c = {"TP": 0, "FP": 0, "TN": 0, "FN": 0}
    for t, p in zip(y_true, y_pred):
        if t == 1 and p == 1: c["TP"] += 1
        elif t == 0 and p == 1: c["FP"] += 1
        elif t == 1 and p == 0: c["FN"] += 1
        else: c["TN"] += 1
    return c
```

**Common confusion:** sklearn's `confusion_matrix` prints
`[[TN, FP], [FN, TP]]` — actual as ROWS, predicted as COLUMNS, and
negative class first. Reading it as [[TP,...]] flips everything;
check `labels`/`y` ordering before interpreting.

---

### 3. K-Fold Cross-Validation — `p03`

**What it is:** One train/test split can be lucky or unlucky —
maybe your 20% happened to be easy. K-fold CV splits data into k
parts, trains k times (each part takes a turn as test), giving k
scores. **Mean** = performance estimate; **std** = how much luck
matters.

**Worked example:**
```
150 iris flowers, cv=5:
  fold 1: train on folds 2-5, test on fold 1 → score 1.00
  fold 2: train on 1,3,4,5,  test on fold 2 → score 0.93
  ...×5 → scores like [0.967, 0.933, 0.967, 1.000, 0.967]

mean = 0.9667, std = 0.0211
→ "96.7% ± 2.1%" — far more honest than one 97% split.
```

**Why ML cares:** It's the default answer to "how good is this
model, really?" Every fold's test slice is unseen, so nothing leaks,
and the spread tells you if a 3% improvement is real or noise.
Grid search (`medium/p02`) and nested CV (`hard/p03`) are built on
it.

**Code:**
```python
from sklearn.model_selection import cross_val_score
scores = cross_val_score(
    RandomForestClassifier(random_state=42), X, y, cv=5)
scores.mean(), scores.std()   # 0.9667, 0.0211
```

**Common confusion:** CV does NOT produce one trained model — it
produces k scores for EVALUATION. After estimating performance, you
still retrain on all data (or keep the tuned model) for deployment.
Also: for imbalanced classes use `StratifiedKFold` (same ratio per
fold, level-02 `hard/p03`).

---

## Medium

### 4. ROC Curve and AUC — `p01`

**What it is:** Classifiers output probabilities; the threshold
(usually 0.5) decides yes/no. The **ROC curve** plots True Positive
Rate (recall) vs False Positive Rate at EVERY threshold from 0 to
1. **AUC** = area under it: the probability the model ranks a random
positive above a random negative. 1.0 = perfect, 0.5 = coin flip.

**Worked example:**
```
Model says: P(sick)=0.9 for a truly sick patient → TP at any
            threshold below 0.9. P(sick)=0.4 for a healthy one →
            FP only if threshold ≤ 0.4.

Threshold 0.9: TPR low (misses borderline sick), FPR ~0 (few alarms)
Threshold 0.5: balanced TPR/FPR
Threshold 0.1: TPR high (catches almost all), FPR high (alarm storm)

Curve bows toward top-left; AUC = 0.8854 here — good but imperfect.
```

**Why ML cares:** AUC judges RANKING quality independent of any
threshold — perfect when you haven't decided how aggressive to be.
It's also robust to class imbalance, unlike accuracy. Comparing
models by AUC (`hard/p02`) is standard practice.

**Code:**
```python
from sklearn.metrics import roc_curve, auc
y_prob = model.predict_proba(X_test)[:, 1]   # P(class=1), NOT predict()
fpr, tpr, _ = roc_curve(y_test, y_prob)
a = auc(fpr, tpr)                            # 0.8854
plt.plot(fpr, tpr); plt.savefig('roc_curve.png')
```

**Common confusion:** `roc_curve` needs PROBABILITIES
(`predict_proba`), not 0/1 predictions — feeding `predict` gives a
degenerate 3-point curve. And a perfect model's curve hugs the
top-left corner; the diagonal dashed line is random guessing.

---

### 5. Grid Search (Hyperparameter Tuning) — `p02`

**What it is:** **Hyperparameters** are knobs YOU set before
training (number of trees, max depth) — unlike weights, the model
can't learn them. Grid search tries every combination, scores each
via cross-validation, and returns the winner.

**Worked example:**
```
param_grid = {
    'n_estimators':      [50, 100, 200],
    'max_depth':         [3, 5, 10],
    'min_samples_split': [2, 5],
}
3 × 3 × 2 = 18 combos × cv=3 folds = 54 model fits

best_params_ = {'max_depth': 10, 'min_samples_split': 5,
                'n_estimators': 200}
best_score_  ≈ 0.9x (mean CV accuracy of the winner)
Then verify once on the held-out test set.
```

**Why ML cares:** Default hyperparameters are rarely optimal, and
hand-tuning is guessing. Grid search systematizes it — and using
CV (not the test set!) to pick the winner is what keeps the test
score honest. Nested CV (`hard/p03`) is the extra-paranoid version.

**Code:**
```python
from sklearn.model_selection import GridSearchCV
gs = GridSearchCV(RandomForestClassifier(random_state=42),
                  param_grid, cv=3)
gs.fit(X_train, y_train)
gs.best_params_, gs.best_score_, gs.score(X_test, y_test)
```

**Common confusion:** The CV score and test score answer different
questions: `best_score_` = "which setting won during tuning";
`score(X_test)` = "how good is the tuned model on untouched data."
Reporting `best_score_` as your final result is optimistic — it
was chosen BECAUSE it was highest.

---

### 6. Learning Curves — `p03`

**What it is:** Plot score vs training-set size: train a model on
10% of data, 20%, ..., 100%, scoring train and validation at each
size. The SHAPE diagnoses your problem — it's the bias-variance
tradeoff (level-01) drawn as a picture.

**Worked example:**
```
10 points on the x-axis (10%→100% of ~400 train samples),
two lines:

train_mean:  starts ~1.0 (tiny data = memorizable), falls slightly
val_mean:    starts low (little data = poor model), climbs to ~0.85

Diagnosis by shape:
  Big gap between lines  → overfitting → GET MORE DATA helps
  Both low, converged    → underfitting → better model/features
  Both high, converged   → done — more data won't help
```

**Why ML cares:** "Should I collect more data or build a fancier
model?" is THE most expensive question in ML — this chart answers
it for free. Validation still rising at 100% → data is the
bottleneck. Flat val + low scores → model is the bottleneck.

**Code:**
```python
from sklearn.model_selection import learning_curve
sizes, train_sc, val_sc = learning_curve(
    LogisticRegression(max_iter=1000), X, y, cv=5,
    train_sizes=np.linspace(0.1, 1.0, 10))
train_mean = train_sc.mean(axis=1)   # scores are (10 sizes, 5 folds)
val_mean   = val_sc.mean(axis=1)
```

**Common confusion:** The returned scores are a 2D array (sizes ×
folds) — you must average `axis=1` (over folds) to get one point
per size. Averaging `axis=0` gives you 5 nonsense points per fold
instead.

---

## Hard

### 7. Precision-Recall Threshold Tuning — `p01`

**What it is:** The 0.5 threshold is a default, not a law. Slide it
down → the model says "yes" more → recall rises (catch more real
cases) but precision falls (more false alarms). `precision_recall_
curve` computes (precision, recall) at every threshold so you pick
the tradeoff on purpose.

**Worked example:**
```
Data: 90% class-0 / 10% class-1 (imbalanced, like fraud/disease)

threshold 0.50 → recall ≈ 0.4  (misses 60% of positives!)
threshold 0.15 → recall ≈ 0.80 (catches 80%)
                 but precision ≈ 0.50 (half your flags are wrong)

idx = argmin(|recalls − 0.80|) → threshold ≈ 0.1466,
precision there ≈ 0.50 — the literal price of higher recall.
```

**Why ML cares:** In production you tune the threshold to the cost
of errors — a disease screener accepts low precision for high
recall; a spam filter does the reverse. This is where ML meets
business logic, and it's why `hard/p02` compares models on more
than one metric.

**Code:**
```python
from sklearn.metrics import precision_recall_curve
y_prob = model.predict_proba(X_test)[:, 1]
precisions, recalls, thresholds = precision_recall_curve(y_test, y_prob)
idx = np.argmin(np.abs(recalls - 0.8))
threshold, precision = thresholds[idx], precisions[idx]
```

**Common confusion:** `thresholds` has ONE FEWER element than
`precisions`/`recalls` (sklearn appends a sentinel) — indexing
`thresholds[idx]` is safe when idx comes from the recalls array,
but don't assume equal lengths when slicing. Also: tune the
threshold on VALIDATION data, not test, to keep test honest.

---

### 8. Multi-Model Comparison — `p02`

**What it is:** Train several algorithms on the SAME split and
compare them across SEVERAL metrics — accuracy (overall), F1
(precision-recall balance), AUC (ranking quality). No single number
crowns a winner; different metrics can rank models differently.

**Worked example:**
```
Same data, same split:
                    acc     f1      auc
Logistic Regression 0.88    0.872   0.946
Random Forest       0.94    0.935   0.989
Gradient Boosting   0.95    0.946   0.995  ← best on all three
SVM                 0.88    0.872   0.967
KNN                 0.90    0.891   0.959

Boosting wins here — but SVM's AUC (0.967) beats KNN's (0.959)
despite LOWER accuracy: SVM ranks better, its 0.5 threshold just
isn't optimal.
```

**Why ML cares:** This table IS the "results section" of every real
ML experiment. It teaches that "best" is metric-dependent — and
that a model with lower accuracy but higher AUC might win once you
tune its threshold (`hard/p01`).

**Code:**
```python
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
for name, m in models.items():
    m.fit(X_train, y_train)
    prob = m.predict_proba(X_test)[:, 1]
    results[name] = {"accuracy": accuracy_score(y_test, m.predict(X_test)),
                     "f1": f1_score(y_test, m.predict(X_test)),
                     "auc": roc_auc_score(y_test, prob)}
```

**Common confusion:** `SVC` has NO `predict_proba` unless you pass
`probability=True` at construction — it computes probabilities via
a slow extra fitting step. Forgetting it crashes the AUC column.

---

### 9. Nested Cross-Validation — `p03`

**What it is:** If you grid-search hyperparameters on all your data
and then CV-evaluate on the same data, the "test" folds influenced
tuning — your score is optimistically biased. **Nested CV** fixes
it: an OUTER 5-fold loop evaluates; inside each outer-train chunk,
an INNER 3-fold grid search tunes — the outer test fold never
touches tuning.

**Worked example:**
```
outer fold 1: tune on 160 samples (inner 3-fold grid search)
              → best params (maybe n=100, depth=5)
              → score on the held-out 40 → 0.85
outer fold 2: RETUNE from scratch on a different 160
              → best params may differ! → score 0.90
...×5 → scores ≈ [0.85, 0.90, 0.88, 0.90, 0.90]
mean = 0.885 ± 0.030 — unbiased estimate of "a tuned RF on
this kind of data," even though params vary per fold.
```

**Why ML cares:** It's the gold standard when data is small and you
must both tune AND honestly evaluate. If outer-fold best-params
differ each fold, that's a signal your tuning is unstable — useful
information a single grid search hides.

**Code:**
```python
inner = GridSearchCV(
    RandomForestClassifier(random_state=42),
    {'n_estimators': [50, 100], 'max_depth': [3, 5]}, cv=3)
scores = cross_val_score(inner, X, y, cv=5)   # pass the OBJECT
scores.mean(), scores.std()                    # 0.8850, 0.0300
```

**Common confusion:** Pass the UNFITTED `GridSearchCV` object to
`cross_val_score` — sklearn refits (and retunes) it inside each
outer fold. Calling `inner.fit(X, y)` first leaks tuning across all
folds and defeats the entire point.

---

## Done with concepts? → Try `easy/p01-metrics-scratch.py`
