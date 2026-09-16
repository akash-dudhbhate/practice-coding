# Level 01 — Concepts (Detailed Explanations)

Read each section BEFORE attempting its problem. Each concept has:
what it is in plain words → a worked example with real numbers →
why ML cares → the code → what confuses beginners.

---

## Easy

### 1. Supervised vs Unsupervised Learning — `p01`

**What it is:** The first question in any ML problem: "Do I have
labeled examples?" Labeled means each input comes with the correct
answer. **Supervised** = labeled data (learn the mapping
input→answer). **Unsupervised** = no labels (find structure on your
own). Supervised splits further: **regression** predicts a NUMBER,
**classification** predicts a CATEGORY.

**Worked example:**
```
Scenario A: predict house price from size+location
  → labels exist (past sales with prices), output is a NUMBER
  → supervised-regression

Scenario B: group shoppers by purchase history, no labels
  → no "correct answer" column, just finding groups
  → unsupervised (clustering)

Scenario C: tumor malignant or benign from images
  → labels exist (diagnosed cases), output is a CATEGORY
  → supervised-classification
```

**Why ML cares:** Picking the wrong type wastes weeks. If you try
regression on a category, or supervised on unlabeled data, nothing
works. Every later level assumes you can do this triage instantly.

**Code:**
```python
def classify(scenario):
    return {
        "A": "supervised-regression",        # predict a number
        "B": "unsupervised",                 # group, no labels
        "C": "supervised-classification",    # predict a category
    }[scenario]
```

**Common confusion:** "Classification" does NOT mean "puts things in
groups" — that's clustering (unsupervised). Classification = predict
a known category FROM labeled examples. Clustering = invent the
groups yourself because no labels exist.

---

### 2. Features and Labels — `p02`

**What it is:** Every supervised dataset is a table. **Features (X)**
are the input columns — the clues the model reads. The **label (y)**
is the output column — the thing you're trying to predict. The whole
job of training is learning the mapping X → y.

**Worked example:**
```
Predicting house price:
  features X = [size_sqft, bedrooms, location, age]
  label    y = price

One row of data:
  X = [1500, 3, "downtown", 12]  →  y = 320000
```

**Why ML cares:** The entire X/y naming convention is everywhere:
`model.fit(X_train, y_train)`, `model.predict(X_test)`. Bad feature
choice is the #1 cause of bad models — a model can't predict price
from house color if color doesn't matter.

**Code:**
```python
def identify(scenario):
    if scenario == "A":  # will a student pass?
        return {"features": ["study_hours", "attendance", "past_scores"],
                "label": "pass_fail"}
    if scenario == "B":  # next month's store sales
        return {"features": ["month", "last_month_sales", "season"],
                "label": "total_sales"}
```

**Common confusion:** The label is always ONE thing you're predicting;
features are MANY things you observe. Also: the label at prediction
time is UNKNOWN — you only have labels for the training data.

---

### 3. Traditional Programming vs ML — `p03`

**What it is:** Traditional: a human writes explicit rules
(`if "free money" in email: spam`). ML: you show the computer many
examples and it LEARNS the rules. Same goal — inputs to outputs —
but who writes the rules differs.

**Worked example:**
```
Cart total     → rules are fixed: sum(prices).      → traditional
Sort names     → rules are fixed: sort().           → traditional
Spam filter    → rules change daily, can't hand-code → ml
Face detection → no one can write "if pixel pattern
                 looks like a face" by hand          → ml
```

**Why ML cares:** ML is not magic for everything. If you can write
the rule in 10 lines of `if` statements, do that — it's free, fast,
and perfect. ML shines when rules are too complex (faces, speech) or
constantly changing (spam, fraud).

**Code:**
```python
def choose(scenario):
    return {
        "A": "traditional",   # cart total — fixed math
        "B": "ml",            # spam — evolving patterns
        "C": "traditional",   # sorting — fixed algorithm
        "D": "ml",            # faces — too complex to hand-code
    }[scenario]
```

**Common confusion:** "The problem is about data" does NOT mean "use
ML." Sorting data and summing a cart are still traditional. Ask:
"Can I write down the exact rules?" Yes → traditional. No → ML.

---

## Medium

### 4. Designing an ML System — `p01`

**What it is:** Before touching code, answer 5 questions:
(1) problem type, (2) features, (3) label, (4) where data comes
from, (5) how you measure success. Skipping these is how projects
die — you train the wrong model on the wrong data judged by the
wrong metric.

**Worked example (spam classifier):**
```
1. problem_type: supervised-classification (spam / not-spam)
2. features: [sender_domain, subject_words, has_links,
              num_caps, email_length]
3. label: "spam" or "not_spam"
4. data_source: public datasets (Enron) or hand-label emails
5. metric: precision — a false alarm deletes a REAL email,
           which users hate more than seeing spam
```

**Why ML cares:** This is literally what ML interviews and design
docs ask. "How would you build X?" always starts with these five
questions, not with "I'd use a neural network."

**Code:**
```python
def design():
    return {
        "problem_type": "supervised-classification",
        "features": ["sender_domain", "subject_words",
                     "has_links", "num_caps", "email_length"],
        "label": "spam or not_spam",
        "data_source": "public datasets like Enron or manual labeling",
        "metric": "precision",
    }
```

**Common confusion:** Metric choice is part of DESIGN, not an
afterthought. For spam, precision matters (don't nuke real mail).
For disease screening, recall matters (don't miss a case). Choosing
"accuracy" blindly is a rookie move — see `hard/p02` for why.

---

### 5. Train/Test Split — `p02`

**What it is:** Hold out a slice of data the model NEVER sees during
training. Train on ~80%, evaluate on the ~20% test set. The test
score estimates how the model does on genuinely new data.

**Worked example:**
```
1000 labeled emails → shuffle → split:
  train = emails[0:800]    # model learns from these
  test  = emails[800:1000] # model never touches these while training

Results: train accuracy 99%, test accuracy 60%
  → the 39-point gap = classic OVERFITTING
  → the model memorized those 800 emails, didn't learn "spam-ness"
```

**Why ML cares:** Testing on training data is like grading a student
on the exact problems they memorized — you learn nothing. Every
level from here on starts with `train_test_split` (level-05 shows
cross-validation, the grown-up version).

**Code:**
```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
```

**Common confusion:** You may never "peek" at the test set to make
decisions — that includes normalizing with stats computed on ALL
data (leakage!). Compute means/stds on train only, then apply to
test.

---

### 6. Choosing an Algorithm — `p03`

**What it is:** Match the algorithm to the problem SHAPE: number or
category? labeled or not? simple or complex? There is no "best"
algorithm — only "right for this problem."

**Worked example:**
```
A) tomorrow's temperature (a number, labeled)     → linear-regression
B) 5 customer segments (no labels)                → kmeans-clustering
C) spam or not (binary category, labeled)         → logistic-regression
D) house price from 50 features (number, labeled) → linear-regression
E) objects in photos (complex patterns, labeled)  → neural-network
```

**Why ML cares:** Interviewers love "which model and why?" The
mental flowchart: labeled? → number or category? → need
interpretability? → how complex is the pattern? You'll meet each
of these hands-on in level-04.

**Code:**
```python
def match(scenario):
    return {
        "A": "linear-regression",
        "B": "kmeans-clustering",
        "C": "logistic-regression",
        "D": "linear-regression",
        "E": "neural-network",
    }[scenario]
```

**Common confusion:** "Logistic regression" is for CLASSIFICATION
(categories), despite having "regression" in its name. It outputs a
probability that gets thresholded into yes/no. Don't let the name
fool you.

---

## Hard

### 7. The Full ML Pipeline — `p01`

**What it is:** Every ML project is the same 8 steps, in order:
Define → Collect → Preprocess → Split → Choose → Train → Evaluate →
Deploy. "Training" is step 6 of 8 — most of the work is everything
around it.

**Worked example (diabetes risk predictor):**
```
1. problem:      classification (diabetic / not-diabetic)
2. data:         patient records — age, BMI, blood pressure,
                 glucose, family history
3. preprocessing: fill missing values, normalize numbers,
                 encode categories
4. split:        80/20 train/test
5. model:        logistic regression or decision tree (start simple)
6. training:     model.fit(X_train, y_train)
7. evaluation:   recall — missing a real case is worse than
                 a false alarm
8. deployment:   API endpoint: patient data in → risk score out
```

**Why ML cares:** This is the skeleton of EVERY project in this repo
(and real jobs). Levels 02-05 are literally these steps zoomed in:
02 = preprocess, 03 = explore, 04 = choose+train, 05 = evaluate.

**Code:**
```python
def design_pipeline():
    return {
        "problem": "classification (diabetic / not-diabetic)",
        "data": "patient records: age, BMI, blood pressure, glucose, family history",
        "preprocessing": "handle missing values, normalize numeric features, encode categories",
        "split": "80/20",
        "model": "logistic regression or decision tree",
        "training": "model.fit(X_train, y_train)",
        "evaluation": "recall — missing a disease is worse than a false alarm",
        "deployment": "API endpoint that takes patient data and returns risk score",
    }
```

**Common confusion:** Beginners think "ML project = pick an
algorithm." Actually steps 2-4 (data) eat 80% of real-world time.
A simple model on clean data beats a fancy model on garbage.

---

### 8. Confusion Matrix — `p02`

**What it is:** A 2×2 tally of predictions vs reality for a yes/no
classifier. TP = said yes, was yes. TN = said no, was no.
FP = said yes, was no (false alarm). FN = said no, was yes
(missed case). Accuracy = (TP+TN)/total.

**Worked example (1000 patients, 80 sick):**
```
                Predicted SICK   Predicted HEALTHY
  Actually SICK     TP = 70          FN = 10   (missed!)
  Actually HEALTHY  FP = 30          TN = 890

accuracy = (70 + 890) / 1000 = 0.96  → 96%!
But: the test missed 10 of 80 real cases (12.5% of the sick).
For a medical test, FN is the worse error → "false-negative".
```

**Why ML cares:** 96% accuracy sounds great until you realize a
"always healthy" predictor scores 92% and catches ZERO sick people.
On imbalanced data, accuracy lies. Level-05 turns these 4 numbers
into precision, recall, F1, ROC-AUC.

**Code:**
```python
def analyze():
    TP, FN, FP, TN = 70, 10, 30, 890
    return {
        "TP": TP, "FP": FP, "TN": TN, "FN": FN,
        "accuracy": (TP + TN) / 1000,        # 0.96
        "worse_error": "false-negative",     # missed disease > false alarm
    }
```

**Common confusion:** Which is the Positive? YOU choose — usually
the rare/important class (sick, spam, fraud). FP means "flagged it
but it was fine"; FN means "missed it and it was real." Mixing
these up flips your entire analysis.

---

### 9. Bias-Variance Tradeoff — `p03`

**What it is:** Two ways a model can be wrong. **Bias** = error from
being too simple (underfitting — misses the real pattern). **Variance**
= error from being too sensitive to the exact training data
(overfitting — memorizes noise). Making the model more complex
lowers bias but raises variance — you balance, you don't eliminate.

**Worked example:**
```
Tree with 100% train, 65% test:
  perfect on data it saw, bad on new data
  → high variance (overfitting)
  → fix: prune the tree, limit depth, get more data

Linear model with 70% train, 70% test:
  bad on BOTH — too simple to capture the pattern
  → high bias (underfitting)
  → fix: more complex model, more features
```

**Why ML cares:** The train-vs-test gap is the single most useful
diagnostic in ML. Gap big → variance. Both bad → bias. This tells
you WHICH knob to turn instead of guessing. Returns in every model
level (04, 08, 09) — regularization, pruning, and dropout are all
variance-reducers.

**Code:**
```python
def explain():
    return {
        "bias": "Error from oversimplified assumptions — model is too simple",
        "variance": "Error from sensitivity to training data — model memorizes noise",
        "high_bias": "underfitting",
        "high_variance": "overfitting",
        "tree_100_65": "high variance (overfitting) — fix: prune the tree, limit depth",
        "linear_70_70": "high bias (underfitting) — fix: use a more complex model",
        "tradeoff": "Reducing bias increases variance and vice versa — it's a balance",
    }
```

**Common confusion:** High variance is not "the model varies a lot"
in its outputs — it means the model CHANGES a lot if you retrain it
on a different sample of data. It over-adapts to whatever noise was
in the training set it happened to see.

---

## Done with concepts? → Try `easy/p01-classify-type.py`
