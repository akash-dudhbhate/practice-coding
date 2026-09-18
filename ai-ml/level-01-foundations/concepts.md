# Level 01 — Concepts (Detailed Explanations)

> Read each section BEFORE attempting its problem. Each concept explains:
> **What it is** · **Why it exists** · **Where it's used** ·
> **What goes wrong** without it · worked example · code ·
> expected output.

---

## Easy

### 1. Supervised vs Unsupervised Learning — `p01`

**What it is:** The first question in any ML problem: "Do I have
labeled examples?" Labeled means each input comes with the correct
answer. **Supervised** = labeled data (learn the mapping
input→answer). **Unsupervised** = no labels (find structure on your
own). Supervised splits further: **regression** predicts a NUMBER,
**classification** predicts a CATEGORY.

**Why it exists:** Different data requires completely different
algorithms — there's no universal learner. This triage exists so
you pick a method that can actually use the data you have.

**Where it's used:** The opening decision of every ML project,
interview question, and sklearn API call (`fit(X, y)` vs
`fit(X)`).

**What goes wrong without it:** Picking the wrong type wastes
weeks — run regression on a category and you get "predicted
class 1.7"; run supervised learning on unlabeled data and
`fit(X, y)` has no `y` to learn from. Also the classic mix-up:
"classification" does NOT mean "puts things in groups" — that's
clustering (unsupervised). Classification = predict a KNOWN
category from labeled examples; clustering = invent the groups
yourself.

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

**Code:**
```python
def classify(scenario):
    return {
        "A": "supervised-regression",        # predict a number
        "B": "unsupervised",                 # group, no labels
        "C": "supervised-classification",    # predict a category
    }[scenario]
```

**Expected output:** `classify("A")` → `'supervised-regression'`,
`classify("B")` → `'unsupervised'`, `classify("C")` →
`'supervised-classification'`.

---

### 2. Features and Labels — `p02`

**What it is:** Every supervised dataset is a table. **Features (X)**
are the input columns — the clues the model reads. The **label (y)**
is the output column — the thing you're trying to predict. The whole
job of training is learning the mapping X → y.

**Why it exists:** A model can't learn from "everything" — you
must declare which columns are clues and which column is the
answer. The X/y split is that declaration.

**Where it's used:** The universal sklearn convention:
`model.fit(X_train, y_train)`, `model.predict(X_test)`. Every
dataset you'll ever touch gets carved into X and y.

**What goes wrong without it:** Bad feature choice is the #1
cause of bad models — a model can't predict price from house
color if color doesn't matter. Leak the label into X and the
model "learns" to copy the answer — 100% accuracy in testing,
worthless in production. Also: the label is ONE thing you're
predicting; at prediction time it's UNKNOWN — you only have
labels for training data.

**Worked example:**
```
Predicting house price:
  features X = [size_sqft, bedrooms, location, age]
  label    y = price

One row of data:
  X = [1500, 3, "downtown", 12]  →  y = 320000
```

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

**Expected output:** `identify("A")` →
`{'features': ['study_hours', 'attendance', 'past_scores'], 'label': 'pass_fail'}`;
`identify("B")` →
`{'features': ['month', 'last_month_sales', 'season'], 'label': 'total_sales'}`.

---

### 3. Traditional Programming vs ML — `p03`

**What it is:** Traditional: a human writes explicit rules
(`if "free money" in email: spam`). ML: you show the computer many
examples and it LEARNS the rules. Same goal — inputs to outputs —
but who writes the rules differs.

**Why it exists:** Some problems have rules too complex (faces)
or too fast-changing (spam) to hand-write — ML exists for exactly
those. The distinction exists so you don't reach for the
expensive tool when the cheap one works.

**Where it's used:** Scoping any project: "can we just write the
rules?" is the first question a good engineer asks before
proposing a model.

**What goes wrong without it:** Using ML where a rule works = a
model that's slower, flakier, and needs maintenance for something
`sort()` does perfectly. Using rules where ML is needed = a spam
filter that dies the day spammers change one word. "The problem
is about data" does NOT mean "use ML" — sorting data is still
traditional. Ask: "Can I write down the exact rules?" Yes →
traditional. No → ML.

**Worked example:**
```
Cart total     → rules are fixed: sum(prices).      → traditional
Sort names     → rules are fixed: sort().           → traditional
Spam filter    → rules change daily, can't hand-code → ml
Face detection → no one can write "if pixel pattern
                 looks like a face" by hand          → ml
```

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

**Expected output:** `choose("A")` → `'traditional'`,
`choose("B")` → `'ml'`, `choose("C")` → `'traditional'`,
`choose("D")` → `'ml'`.

---

## Medium

### 4. Designing an ML System — `p01`

**What it is:** Before touching code, answer 5 questions:
(1) problem type, (2) features, (3) label, (4) where data comes
from, (5) how you measure success.

**Why it exists:** Skipping design is how projects die — you can
train a flawless model on the wrong data judged by the wrong
metric and deliver nothing. The five questions exist to catch
that before a single line of code.

**Where it's used:** ML system-design interviews, project design
docs, and the first page of every real proposal — "how would you
build X?" always starts with these five, never with "I'd use a
neural network."

**What goes wrong without it:** Train first, think later → you
get a model that optimizes accuracy when the business needed
recall, or predicts a label nobody can act on. Choosing
"accuracy" blindly is a rookie move — for spam, precision matters
(don't nuke real mail); for disease screening, recall matters
(don't miss a case). See `hard/p02` for why.

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

**Expected output:** A dict with keys `problem_type`, `features`,
`label`, `data_source`, `metric` — values matching the worked
example above.

---

### 5. Train/Test Split — `p02`

**What it is:** Hold out a slice of data the model NEVER sees during
training. Train on ~80%, evaluate on the ~20% test set. The test
score estimates how the model does on genuinely new data.

**Why it exists:** A model that memorized its training data looks
perfect until it meets the real world. The test set exists to
detect that — it's the only honest estimate of "will this work
tomorrow?"

**Where it's used:** Every level from here on starts with
`train_test_split`; level-05 shows cross-validation, the
grown-up version.

**What goes wrong without it:** Testing on training data is like
grading a student on the problems they memorized — you learn
nothing and ship an overfit model. Subtler version: you may never
"peek" at test data to make decisions — that includes normalizing
with stats computed on ALL data (leakage!). Compute means/stds
on train only, then apply to test.

**Worked example:**
```
1000 labeled emails → shuffle → split:
  train = emails[0:800]    # model learns from these
  test  = emails[800:1000] # model never touches these while training

Results: train accuracy 99%, test accuracy 60%
  → the 39-point gap = classic OVERFITTING
  → the model memorized those 800 emails, didn't learn "spam-ness"
```

**Code:**
```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
```

**Expected output:** Four arrays — `X_train` with ~80% of the rows
(800 of 1000), `X_test` with ~20% (200), and the matching
`y_train`/`y_test` labels, same order preserved.

---

### 6. Choosing an Algorithm — `p03`

**What it is:** Match the algorithm to the problem SHAPE: number or
category? labeled or not? simple or complex? There is no "best"
algorithm — only "right for this problem."

**Why it exists:** Algorithms have different assumptions —
linearity, distance, tree-splits. Matching the assumption to the
data's shape is why the menu exists; the no-free-lunch theorem
guarantees no single winner.

**Where it's used:** Interviewers love "which model and why?"
The mental flowchart: labeled? → number or category? → need
interpretability? → how complex is the pattern? You'll meet each
hands-on in level-04.

**What goes wrong without it:** Force a linear model on curved
data → underfits no matter how long it trains. Throw a neural
net at 50 rows → overfits instantly. And the name trap:
"logistic regression" is for CLASSIFICATION despite having
"regression" in its name — it outputs a probability that gets
thresholded into yes/no.

**Worked example:**
```
A) tomorrow's temperature (a number, labeled)     → linear-regression
B) 5 customer segments (no labels)                → kmeans-clustering
C) spam or not (binary category, labeled)         → logistic-regression
D) house price from 50 features (number, labeled) → linear-regression
E) objects in photos (complex patterns, labeled)  → neural-network
```

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

**Expected output:** `match("A")` → `'linear-regression'`,
`match("B")` → `'kmeans-clustering'`, `match("C")` →
`'logistic-regression'`, `match("E")` → `'neural-network'`.

---

## Hard

### 7. The Full ML Pipeline — `p01`

**What it is:** Every ML project is the same 8 steps, in order:
Define → Collect → Preprocess → Split → Choose → Train → Evaluate →
Deploy. "Training" is step 6 of 8 — most of the work is everything
around it.

**Why it exists:** Steps depend on each other — you can't
preprocess data you haven't collected, or evaluate a model you
haven't trained. The pipeline exists so nothing gets skipped
under deadline pressure.

**Where it's used:** The skeleton of EVERY project in this repo
(and real jobs). Levels 02-05 are literally these steps zoomed
in: 02 = preprocess, 03 = explore, 04 = choose+train, 05 =
evaluate.

**What goes wrong without it:** Beginners think "ML project =
pick an algorithm." Skip preprocessing → model crashes on NaN.
Skip the split → no honest evaluation. Skip deployment thinking
→ a model that can't receive input in production. Steps 2-4
(data) eat 80% of real-world time — a simple model on clean data
beats a fancy model on garbage.

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

**Expected output:** A dict with all 8 keys (`problem` …
`deployment`), matching the worked example step-for-step.

---

### 8. Confusion Matrix — `p02`

**What it is:** A 2×2 tally of predictions vs reality for a yes/no
classifier. TP = said yes, was yes. TN = said no, was no.
FP = said yes, was no (false alarm). FN = said no, was yes
(missed case). Accuracy = (TP+TN)/total.

**Why it exists:** One accuracy number hides WHICH errors you
make. The matrix exists because "10 false alarms" and "10 missed
cases" cost completely different things in the real world.

**Where it's used:** Every classification report — level-05 turns
these 4 numbers into precision, recall, F1, ROC-AUC. Medical,
fraud, and spam systems are all specified in FP/FN terms.

**What goes wrong without it:** 96% accuracy sounds great until
you realize an "always healthy" predictor scores 92% on this data
and catches ZERO sick people — on imbalanced data, accuracy lies
and only the matrix shows it. Also: YOU choose which class is
Positive — mixing up FP and FN flips the entire analysis
(a missed disease becomes a "false alarm," the wrong thing gets
optimized).

**Worked example (1000 patients, 80 sick):**
```
                Predicted SICK   Predicted HEALTHY
  Actually SICK     TP = 70          FN = 10   (missed!)
  Actually HEALTHY  FP = 30          TN = 890

accuracy = (70 + 890) / 1000 = 0.96  → 96%!
But: the test missed 10 of 80 real cases (12.5% of the sick).
For a medical test, FN is the worse error → "false-negative".
```

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

**Expected output:** `{'TP': 70, 'FP': 30, 'TN': 890, 'FN': 10,
'accuracy': 0.96, 'worse_error': 'false-negative'}`.

---

### 9. Bias-Variance Tradeoff — `p03`

**What it is:** Two ways a model can be wrong. **Bias** = error from
being too simple (underfitting — misses the real pattern). **Variance**
= error from being too sensitive to the exact training data
(overfitting — memorizes noise). Making the model more complex
lowers bias but raises variance — you balance, you don't eliminate.

**Why it exists:** "The model is bad" doesn't tell you what to fix.
Bias/variance splits failure into two diseases with opposite cures
— it's the diagnostic that tells you which knob to turn instead of
guessing.

**Where it's used:** Reading any train-vs-test score gap — the
single most useful diagnostic in ML. Returns in every model level
(04, 08, 09): regularization, pruning, and dropout are all
variance-reducers.

**What goes wrong without it:** Misdiagnose and you apply the
wrong cure — adding complexity to an already-overfit model makes
variance worse; gathering more data for a high-bias model changes
nothing. High variance isn't "the model varies a lot" — it means
the model CHANGES a lot when retrained on a different sample: it
over-adapts to whatever noise was in the data it happened to see.

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

**Expected output:** A dict with keys `bias`, `variance`,
`high_bias`, `high_variance`, `tree_100_65`, `linear_70_70`,
`tradeoff` — `explain()["high_variance"]` → `'overfitting'`.

---

## Done with concepts? → Try `easy/p01-classify-type.py`
