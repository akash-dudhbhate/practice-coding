# Level 05 — Concepts (Detailed Explanations)

> Read each section BEFORE attempting its problem. Each concept explains:
> **What it is** · **Why it exists** · **Where it's used** ·
> **What goes wrong** without it · worked example · code ·
> expected output.

---

## Easy

### 1. Accuracy, Precision, Recall, F1 — `p01`

**What it is:** Four ways to score a yes/no classifier, all built
from TP/FP/TN/FN. **Accuracy** = fraction correct overall.
**Precision** = of everything you flagged YES, what fraction was
actually yes. **Recall** = of everything actually YES, what fraction
you caught. **F1** = harmonic mean of precision and recall — one
number that punishes you if either is bad.

**Why it exists:** Accuracy collapses all errors into one number —
but a false alarm and a missed case cost completely different
things. Precision/recall exist to separate "how trustworthy is a
YES" from "how many YESes did we miss"; F1 exists because
optimizing one can tank the other.

**Where it's used:** THE vocabulary of model evaluation — every
paper, dashboard, and interview uses it. The choice is a business
decision: spam wants precision (don't delete real mail); disease
screening wants recall (don't miss cases).

**What goes wrong without it:** On imbalanced data accuracy lies —
"always healthy" scores 92% while catching zero sick people
(level-01 `hard/p02`). The classic mix-up: precision's denominator
is PREDICTED positives (TP+FP); recall's is ACTUAL positives
(TP+FN) — swap them and you optimize the wrong error. And
`TP/(TP+FP)` crashes `ZeroDivisionError` when the model predicts
no positives at all — guard it.

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

**Code:**
```python
TP = sum(1 for t,p in zip(y_true,y_pred) if t==1 and p==1)
FP = sum(1 for t,p in zip(y_true,y_pred) if t==0 and p==1)
TN = sum(1 for t,p in zip(y_true,y_pred) if t==0 and p==0)
FN = sum(1 for t,p in zip(y_true,y_pred) if t==1 and p==0)
precision = TP/(TP+FP) if TP+FP else 0.0   # guard ÷0!
```

**Expected output:** `TP=5, FP=1, TN=3, FN=1` →
`accuracy 0.8, precision 0.833, recall 0.833, f1 0.833`.

---

### 2. Confusion Matrix — `p02`

**What it is:** The 2×2 table every classification metric derives
from. Rows = reality, columns = prediction. TP = said yes, was yes;
FN = said no, was yes (a miss); FP = said yes, was no (false
alarm); TN = said no, was no.

**Why it exists:** A single score hides WHERE the errors are —
two FP and two FN tell a different story than five FP and zero FN.
The matrix exists to keep the error TYPES visible.

**Where it's used:** Every classification report — sklearn's
`confusion_matrix`, `classification_report`, and all the metrics
in `easy/p01` are computed from these four cells.

**What goes wrong without it:** sklearn's `confusion_matrix`
prints `[[TN, FP], [FN, TP]]` — actual as ROWS, predicted as
COLUMNS, negative class first. Read it as `[[TP,...]]` and you
flip every cell — your "false alarms" are actually missed cases
and you tune the wrong error. Check `labels`/ordering before
interpreting.

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

**Expected output:** `confusion(y_true, y_pred)` →
`{'TP': 5, 'FP': 1, 'TN': 3, 'FN': 1}` — the four cells sum to
10, the total number of predictions.

---

### 3. K-Fold Cross-Validation — `p03`

**What it is:** One train/test split can be lucky or unlucky —
maybe your 20% happened to be easy. K-fold CV splits data into k
parts, trains k times (each part takes a turn as test), giving k
scores. **Mean** = performance estimate; **std** = how much luck
matters.

**Why it exists:** A single split's score has unknown error bars —
you can't tell "the model is good" from "the split was easy."
K-fold exists to turn one lucky-or-unlucky number into a
distribution you can trust.

**Where it's used:** The default answer to "how good is this
model, really?" Every fold's test slice is unseen, so nothing
leaks; grid search (`medium/p02`) and nested CV (`hard/p03`) are
built on it.

**What goes wrong without it:** Report one split's 97% and you
might be quoting the lucky fold — the next split scores 90% and
you can't explain the discrepancy to your team. Note what CV does
NOT produce: one trained model — it gives k scores for
EVALUATION; you still retrain on all data for deployment. And on
imbalanced classes use `StratifiedKFold` (same ratio per fold,
level-02 `hard/p03`) or some folds get zero positives.

**Worked example:**
```
150 iris flowers, cv=5:
  fold 1: train on folds 2-5, test on fold 1 → score 1.00
  fold 2: train on 1,3,4,5,  test on fold 2 → score 0.93
  ...×5 → scores like [0.967, 0.933, 0.967, 1.000, 0.967]

mean = 0.9667, std = 0.0211
→ "96.7% ± 2.1%" — far more honest than one 97% split.
```

**Code:**
```python
from sklearn.model_selection import cross_val_score
scores = cross_val_score(
    RandomForestClassifier(random_state=42), X, y, cv=5)
scores.mean(), scores.std()   # 0.9667, 0.0211
```

**Expected output:** `scores` → `[0.967, 0.933, 0.967, 1.0,
0.967]` (5 fold scores); `(scores.mean(), scores.std())` →
`(0.9667, 0.0211)` — report as "96.7% ± 2.1%".

---

## Medium

### 4. ROC Curve and AUC — `p01`

**What it is:** Classifiers output probabilities; the threshold
(usually 0.5) decides yes/no. The **ROC curve** plots True Positive
Rate (recall) vs False Positive Rate at EVERY threshold from 0 to
1. **AUC** = area under it: the probability the model ranks a random
positive above a random negative. 1.0 = perfect, 0.5 = coin flip.

**Why it exists:** Every metric at a fixed threshold conflates
"how good is the ranking" with "where did we cut." AUC exists to
judge RANKING quality alone — before you've decided how
aggressive to be.

**Where it's used:** Comparing models when the threshold isn't
decided yet (`hard/p02`), and on imbalanced data where accuracy
is meaningless — AUC stays honest when positives are rare.

**What goes wrong without it:** `roc_curve` needs PROBABILITIES
(`predict_proba`), not 0/1 predictions — feed it `predict` and
you get a degenerate 3-point curve whose AUC is garbage. Misread
the chart: the diagonal dashed line is random guessing (AUC
0.5) — a model whose curve hugs that diagonal has learned
nothing; a perfect model's curve hugs the top-left corner.

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

**Code:**
```python
from sklearn.metrics import roc_curve, auc
y_prob = model.predict_proba(X_test)[:, 1]   # P(class=1), NOT predict()
fpr, tpr, _ = roc_curve(y_test, y_prob)
a = auc(fpr, tpr)                            # 0.8854
plt.plot(fpr, tpr); plt.savefig('roc_curve.png')
```

**Expected output:** `a` → `0.8854`; `roc_curve.png` shows a
curve starting at (0,0), bowing up toward the top-left corner
(faster than the diagonal), ending at (1,1) — visibly above the
diagonal random-guess line.

---

### 5. Grid Search (Hyperparameter Tuning) — `p02`

**What it is:** **Hyperparameters** are knobs YOU set before
training (number of trees, max depth) — unlike weights, the model
can't learn them. Grid search tries every combination, scores each
via cross-validation, and returns the winner.

**Why it exists:** The model can't learn its own knobs, and
hand-tuning is guessing. Grid search exists to make "which
settings" an experiment instead of a hunch — every combination,
scored the same way.

**Where it's used:** Tuning any model — defaults are rarely
optimal. Using CV (not the test set!) to pick the winner is what
keeps the test score honest; nested CV (`hard/p03`) is the
extra-paranoid version.

**What goes wrong without it:** Tune against the test set and
the test set stops being a test — you picked the params that
score best ON it (a subtle leak; your "honest" number is
inflated). Reporting `best_score_` as your final result is
optimistic too — it was chosen BECAUSE it was highest. The CV
score and test score answer different questions: `best_score_`
= "which setting won during tuning"; `score(X_test)` = "how good
is the tuned model on untouched data."

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

**Code:**
```python
from sklearn.model_selection import GridSearchCV
gs = GridSearchCV(RandomForestClassifier(random_state=42),
                  param_grid, cv=3)
gs.fit(X_train, y_train)
gs.best_params_, gs.best_score_, gs.score(X_test, y_test)
```

**Expected output:** `gs.best_params_` → `{'max_depth': 10,
'min_samples_split': 5, 'n_estimators': 200}`; `gs.best_score_`
→ ~0.9x (the winner's mean CV accuracy); `gs.score(X_test,
y_test)` → a slightly different, honest final number.

---

### 6. Learning Curves — `p03`

**What it is:** Plot score vs training-set size: train a model on
10% of data, 20%, ..., 100%, scoring train and validation at each
size. The SHAPE diagnoses your problem — it's the bias-variance
tradeoff (level-01) drawn as a picture.

**Why it exists:** "Should I collect more data or build a fancier
model?" is THE most expensive question in ML — the learning curve
exists to answer it from data you already have, for free.

**Where it's used:** Deciding where to invest: validation still
rising at 100% → data is the bottleneck (collect more). Flat val
+ low scores → model is the bottleneck (better model/features).

**What goes wrong without it:** Guess wrong and you spend months
collecting data for a high-bias model that can't use it — or
swap in a fancier model when 10× more data was the real fix.
Mechanically: the returned scores are a 2D array (sizes × folds)
— average `axis=1` (over folds) for one point per size;
averaging `axis=0` gives you 5 nonsense points per fold instead.

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

**Code:**
```python
from sklearn.model_selection import learning_curve
sizes, train_sc, val_sc = learning_curve(
    LogisticRegression(max_iter=1000), X, y, cv=5,
    train_sizes=np.linspace(0.1, 1.0, 10))
train_mean = train_sc.mean(axis=1)   # scores are (10 sizes, 5 folds)
val_mean   = val_sc.mean(axis=1)
```

**Expected output:** `train_mean` → 10 values starting near 1.0
and drifting down; `val_mean` → 10 values climbing from ~0.6
toward ~0.85. Plotted: two lines converging from opposite sides
with a visible gap — the classic "more data helps" shape.

---

## Hard

### 7. Precision-Recall Threshold Tuning — `p01`

**What it is:** The 0.5 threshold is a default, not a law. Slide it
down → the model says "yes" more → recall rises (catch more real
cases) but precision falls (more false alarms). `precision_recall_
curve` computes (precision, recall) at every threshold so you pick
the tradeoff on purpose.

**Why it exists:** The cost of a false alarm vs a missed case is
a business decision, not a math one — the same model needs
different thresholds for spam (precision) vs disease (recall).
The curve exists so you can choose the tradeoff deliberately
instead of accepting sklearn's default.

**Where it's used:** Production classification — fraud flags,
medical screening, content moderation: anywhere the two error
types have different prices. It's why `hard/p02` compares models
on more than one metric.

**What goes wrong without it:** Ship the 0.5 default on a 90/10
dataset and recall sits at 0.4 — you miss 60% of real cases while
declaring victory on accuracy. Mechanically: `thresholds` has ONE
FEWER element than `precisions`/`recalls` (sklearn appends a
sentinel) — indexing `thresholds[idx]` is safe when idx comes
from the recalls array, but don't assume equal lengths when
slicing. And tune the threshold on VALIDATION data, not test.

**Worked example:**
```
Data: 90% class-0 / 10% class-1 (imbalanced, like fraud/disease)

threshold 0.50 → recall ≈ 0.4  (misses 60% of positives!)
threshold 0.15 → recall ≈ 0.80 (catches 80%)
                 but precision ≈ 0.50 (half your flags are wrong)

idx = argmin(|recalls − 0.80|) → threshold ≈ 0.1466,
precision there ≈ 0.50 — the literal price of higher recall.
```

**Code:**
```python
from sklearn.metrics import precision_recall_curve
y_prob = model.predict_proba(X_test)[:, 1]
precisions, recalls, thresholds = precision_recall_curve(y_test, y_prob)
idx = np.argmin(np.abs(recalls - 0.8))
threshold, precision = thresholds[idx], precisions[idx]
```

**Expected output:** `threshold ≈ 0.1466`, `precision ≈ 0.50` —
lowering the threshold from 0.5 to ~0.15 buys recall ≈ 0.80 at
the cost of half your flags being false alarms.

---

### 8. Multi-Model Comparison — `p02`

**What it is:** Train several algorithms on the SAME split and
compare them across SEVERAL metrics — accuracy (overall), F1
(precision-recall balance), AUC (ranking quality). No single number
crowns a winner; different metrics can rank models differently.

**Why it exists:** "Best model" depends on what you're optimizing —
a model can lose accuracy while winning AUC (it ranks better, its
0.5 threshold just isn't optimal — fixable via `hard/p01`).
Multi-metric comparison exists to keep you from crowning the
wrong winner.

**Where it's used:** The results table of every real ML
experiment — and model selection interviews ("why did you pick
this one?" needs a metric-aware answer).

**What goes wrong without it:** Comparing on different splits or
different data → you're measuring luck, not models. One metric
only → you discard SVM for lower accuracy while its AUC (0.967)
was better than KNN's — tune its threshold and it could win.
Mechanical trap: `SVC` has NO `predict_proba` unless you pass
`probability=True` at construction — forgetting it crashes the
AUC column with `AttributeError`.

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

**Expected output:** `results` → a dict like
`{'Logistic Regression': {'accuracy': 0.88, 'f1': 0.872, 'auc':
0.946}, 'Random Forest': {0.94, 0.935, 0.989}, 'Gradient
Boosting': {0.95, 0.946, 0.995}, ...}` — matching the worked
table row for row.

---

### 9. Nested Cross-Validation — `p03`

**What it is:** If you grid-search hyperparameters on all your data
and then CV-evaluate on the same data, the "test" folds influenced
tuning — your score is optimistically biased. **Nested CV** fixes
it: an OUTER 5-fold loop evaluates; inside each outer-train chunk,
an INNER 3-fold grid search tunes — the outer test fold never
touches tuning.

**Why it exists:** Tuning IS a form of learning — let the test
folds influence it and they're no longer unseen. Nested CV exists
to keep tuning quarantined inside training data at every level.

**Where it's used:** The gold standard when data is small and you
must both tune AND honestly evaluate — small medical/genomics
datasets, any "we tuned and want a defensible score" situation.

**What goes wrong without it:** Single-loop CV after grid search
reports an inflated score — the params were chosen partly BECAUSE
they fit those folds. Mechanical trap: pass the UNFITTED
`GridSearchCV` object to `cross_val_score` — sklearn refits (and
retunes) it inside each outer fold. Call `inner.fit(X, y)` first
and tuning leaks across all folds, defeating the entire point.
Note: if outer-fold best-params differ each fold, that's a signal
your tuning is unstable — useful information a single grid search
hides.

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

**Code:**
```python
inner = GridSearchCV(
    RandomForestClassifier(random_state=42),
    {'n_estimators': [50, 100], 'max_depth': [3, 5]}, cv=3)
scores = cross_val_score(inner, X, y, cv=5)   # pass the OBJECT
scores.mean(), scores.std()                    # 0.8850, 0.0300
```

**Expected output:** `scores` → ≈ `[0.85, 0.90, 0.88, 0.90,
0.90]`; `(scores.mean(), scores.std())` → `(0.8850, 0.0300)` —
the honest estimate of a tuned model, lower than the optimistic
single-loop number.

---

## Done with concepts? → Try `easy/p01-metrics-scratch.py`
