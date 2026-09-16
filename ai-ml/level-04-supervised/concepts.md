# Level 04 — Concepts (Detailed Explanations)

Read each section BEFORE attempting its problem. Each concept has:
what it is in plain words → a worked example with real numbers →
why ML cares → the code → what confuses beginners.

---

## Easy

### 1. Linear Regression (Closed Form) — `p01`

**What it is:** Fit the best straight line `y = mx + b` through your
points. "Best" = smallest total squared error. There's a one-shot
formula: `m = Σ((x−x̄)(y−ȳ)) / Σ((x−x̄)²)` and `b = ȳ − m·x̄` —
the line that passes through the mean point (x̄, ȳ) with the slope
that follows how x and y co-vary.

**Worked example:**
```
x = [1, 2, 3, 4, 5]     y = [2, 4, 5, 4, 5]
x̄ = 3,  ȳ = 4

(x−x̄)(y−ȳ):  (−2)(−2)=4, (−1)(0)=0, (0)(1)=0, (1)(0)=0, (2)(1)=2
             → Σ = 6
(x−x̄)²:      4 + 1 + 0 + 1 + 4 = 10

m = 6/10 = 0.6
b = 4 − 0.6×3 = 2.2          →  y = 0.6x + 2.2
Check x=1: pred 2.8 (actual 2). x=5: pred 5.2 (actual 5). ✓
```

**Why ML cares:** Linear regression is the "hello world" model —
and the closed form shows what "learning" means mathematically:
turning data into coefficients. R² (1 = perfect, 0 = no better than
predicting the mean) is your first fit-quality metric.

**Code:**
```python
def linreg(x, y):
    x, y = np.array(x), np.array(y)
    m = np.sum((x - x.mean()) * (y - y.mean())) / np.sum((x - x.mean())**2)
    b = y.mean() - m * x.mean()
    return m, b
```

**Common confusion:** This formula is only for ONE feature. With
many features you need the matrix version or gradient descent
(`medium/p01`) — which is also the only option when no closed form
exists (most models!).

---

### 2. Sigmoid + Logistic Regression — `p02`

**What it is:** Logistic regression is a CLASSIFIER that outputs a
probability. It computes `z = w·x + b` (a plain linear score), then
squashes z through the **sigmoid** `σ(z) = 1/(1+e⁻ᶻ)` — any number
in, a value between 0 and 1 out. Predict "yes" when σ > 0.5.

**Worked example:**
```
sigmoid(0)   = 1/(1+1)     = 0.50   → boundary, undecided
sigmoid(2)   = 1/(1+0.135) ≈ 0.88   → probably yes
sigmoid(−4)  = 1/(1+54.6)  ≈ 0.02   → almost surely no

Training on X=[[1,2],[2,3],[3,4],[4,5],[5,6]], y=[0,0,0,1,1]:
  start w=0 → everything predicts 0.5
  after 1000 gradient steps: w≈[3.42,−1.52], b≈−4.94
  → all 5 points classified correctly (accuracy 1.0)
```

**Why ML cares:** This is a one-neuron neural network — sigmoid is
literally an activation function. The gradient `dw = X.T@(p−y)/n`
you compute here is the same math backprop uses at scale. Level-05's
ROC curves are built on the probability this model outputs.

**Code:**
```python
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# inside the training loop:
p  = sigmoid(X @ w + b)
dw = X.T @ (p - y) / n          # average gradient
db = np.sum(p - y) / n
w -= lr * dw;  b -= lr * db
```

**Common confusion:** Despite the name, logistic regression does
NOT predict a continuous value — the 0-1 output is a PROBABILITY of
belonging to class 1. Thresholding at 0.5 is what turns it into a
classification.

---

### 3. Decision Trees — `p03`

**What it is:** A flowchart the model builds: each node asks a
yes/no question about one feature ("petal length ≤ 2.45?") and
splits the data; leaves give the final answer. `max_depth` caps how
many questions deep it can grow — the main dial controlling
overfitting.

**Worked example:**
```
Iris: 150 flowers, features = petal/sepal lengths+widths, 3 species.

Learned tree (sketch):
  petal length ≤ 2.45?  → yes → SETOSA (all 50, done in 1 question)
                        → no  → petal width ≤ 1.75?
                                  → yes → mostly VERSICOLOR
                                  → no  → mostly VIRGINICA

depth 3 → test accuracy 1.0000 on this dataset.
A depth-20 tree would score 1.0 on train AND memorize noise —
depth is the brake pedal.
```

**Why ML cares:** Trees are the most interpretable model — you can
print the exact rules. They're also the building block of Random
Forests and Gradient Boosting (`medium/p02`, `hard/p02`), the
workhorses of tabular ML.

**Code:**
```python
from sklearn.tree import DecisionTreeClassifier, plot_tree
tree = DecisionTreeClassifier(max_depth=3, random_state=42)
tree.fit(X_train, y_train)
plot_tree(tree, feature_names=names, filled=True)
plt.savefig('decision_tree.png')
```

**Common confusion:** Unlimited depth = guaranteed overfitting — a
deep tree can carve out a leaf for EVERY training sample (train
accuracy 1.0, test mediocre). `max_depth=3` isn't a limitation,
it's the feature that makes it generalize.

---

## Medium

### 4. Gradient Descent for Regression — `p01`

**What it is:** When no formula exists, optimize iteratively:
predict → measure MSE → compute gradients (which direction is
downhill) → step the parameters: `m −= lr·dm`, `b −= lr·db`.
Repeat until the loss stops dropping.

**Worked example (one full step):**
```
Data: X=[1,2], y=[3,5]  (true line: y=2x+1)
Start m=0, b=0, lr=0.1

predictions ŷ = [0, 0]     errors (y−ŷ) = [3, 5]
MSE = (9+25)/2 = 17.0

dm = −2·mean(x·(y−ŷ)) = −2·(1·3 + 2·5)/2 = −13
db = −2·mean(y−ŷ)     = −2·(3+5)/2       = −8

m = 0 − 0.1×(−13) = 1.3      b = 0 − 0.1×(−8) = 0.8
new ŷ = [2.1, 3.4]  → MSE = (0.81+2.56)/2 ≈ 1.68
One step cut the loss 17.0 → 1.68. Repeat ~100 times → m≈3, b≈2
on the real noisy data (expected output: 2.9284, 2.0037).
```

**Why ML cares:** This IS how neural networks train — the loss,
gradient, and update-loop shape here are identical to PyTorch's.
The loss history (`losses[0]=10.1 → losses[-1]=0.22`) is your proof
it's converging; always plot it.

**Code:**
```python
for i in range(100):
    y_pred = m * X + b
    losses.append(np.mean((y - y_pred) ** 2))
    dm = -2 * np.mean(X * (y - y_pred))
    db = -2 * np.mean(y - y_pred)
    m -= lr * dm;  b -= lr * db
```

**Common confusion:** The gradient uses (y − ŷ) — error with a
MINUS slope — and you SUBTRACT lr·gradient. Both signs combine so
you step downhill. If your loss explodes upward, check that you're
subtracting, not adding — or that lr isn't too big.

---

### 5. Random Forest + Feature Importances — `p02`

**What it is:** Train hundreds of decision trees, each on a random
subset of rows AND a random subset of features, then majority-vote
their predictions. The randomness makes each tree wrong in
different ways — errors cancel, so the forest generalizes better
than any single tree.

**Worked example:**
```
make_classification: 200 samples, 5 features, only 3 informative
RandomForestClassifier(100 trees) → test accuracy 0.95

feature_importances_ = [0.4379, 0.2187, 0.1961, 0.0720, 0.0753]
  sums to 1.0. Feature 0 carries 44% of the decisions — it's one
  of the "informative" ones; features 3,4 are mostly noise.
```

**Why ML cares:** Forests are the default "try this first" model for
tabular data — strong accuracy, almost no tuning, handles any
feature scale. `feature_importances_` doubles as free feature
selection and a sanity check ("does the model rely on the column I
think it should?").

**Code:**
```python
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
rf.score(X_test, y_test)         # 0.95
rf.feature_importances_          # array, sums to 1
```

**Common confusion:** Importance is RELATIVE usage, not absolute
effect — 0.44 means "used in 44% of splits," not "44% of
predictions depend on it." Correlated features also split
importance between them, so don't read single numbers as gospel.

---

### 6. SVM vs KNN — `p03`

**What it is:** Two classifiers with opposite philosophies. **KNN**:
to classify a point, find its k nearest training points and take a
majority vote — pure "you are who your neighbors are." **SVM**:
find the boundary line that separates classes with the widest
possible margin (gap), keeping only the boundary-adjacent points
("support vectors") relevant.

**Worked example:**
```
Same 200-sample, 5-feature dataset, same 80/20 split:

SVC()                    → test accuracy 0.85
KNeighborsClassifier(5)  → test accuracy 0.80

A point lands near the boundary. KNN asks its 5 nearest
neighbors (say 3 class-A, 2 class-B → votes A). SVM just checks
which side of the margin it's on. Different mechanisms →
different answers on edge cases → different scores.
```

**Why ML cares:** No algorithm wins everywhere — this is the "no
free lunch" theorem in action. Comparing two models on the SAME
split is the baseline habit of real ML work. Also: KNN needs scaled
features (it's distance-based — level-02!); SVM's margin does too.

**Code:**
```python
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
svm = SVC(random_state=42).fit(X_train, y_train)
knn = KNeighborsClassifier(n_neighbors=5).fit(X_train, y_train)
svm.score(X_test, y_test), knn.score(X_test, y_test)  # 0.85, 0.80
```

**Common confusion:** K in KNN means NEIGHBOR COUNT (5), not number
of clusters — don't confuse it with K-Means' K. Small k = wiggly,
overfit boundary; k=1 memorizes the training set entirely.

---

## Hard

### 7. L1 vs L2 Regularization — `p01`

**What it is:** A penalty added to the loss for having large
weights — "you may fit the data, but keep coefficients small."
**L1 (Lasso)** penalizes `|w|` → pushes weak coefficients to
EXACTLY 0 (built-in feature selection). **L2 (Ridge)** penalizes
`w²` → shrinks everything smoothly but rarely to 0.

**Worked example:**
```
10 features, 3 models, same data — coefficient of feature 0:
  LinearRegression: 18.4465
  Lasso(alpha=1.0): 17.3065   ← shrunk
  Ridge(alpha=1.0): 18.4271   ← shrunk less

Feature 2 (weak signal):  linear 3.91 → lasso 2.29 (shrunk 41%)
                          ridge  ≈3.9 (barely moved)
Push alpha higher and Lasso zeros out the weakest features
entirely; Ridge keeps them all small-but-nonzero.
```

**Why ML cares:** Big coefficients = the model contorting to fit
noise (variance, from level-01). Regularization is the standard
overfitting fix for linear models — and the same idea reappears as
"weight decay" in neural networks.

**Code:**
```python
from sklearn.linear_model import Lasso, Ridge
lasso = Lasso(alpha=1.0).fit(X, y)
ridge = Ridge(alpha=1.0).fit(X, y)
lasso.coef_   # some entries exactly 0.0
```

**Common confusion:** `alpha` is INVERSE strength in sklearn —
bigger alpha = MORE penalty = simpler model (some libraries call
the opposite-direction knob `lambda`/`C`). Also: regularize only
after scaling features, or the penalty hits big-scale features
unfairly.

---

### 8. Ensembles: Bagging vs Boosting — `p02`

**What it is:** Two ways to combine many trees. **Bagging (Random
Forest)**: trees train independently on random subsets, then vote —
averaging kills individual trees' noise. **Boosting (Gradient
Boosting)**: trees train SEQUENTIALLY, each one fixing the previous
trees' errors — compounding accuracy.

**Worked example:**
```
Same data, 80/20 split — train / test accuracy:
  Decision Tree:      1.00 / 0.92   ← memorized train, gap = overfit
  Random Forest:      1.00 / 0.94   ← averaging recovered 2 points
  Gradient Boosting:  1.00 / 0.95   ← error-correction won again

All three "know" the training data perfectly; only the ensembles
generalize better.
```

**Why ML cares:** Boosting libraries (XGBoost, LightGBM) won most
Kaggle tabular competitions for a decade — understanding WHY they
beat single trees (each tree targets residual errors) is the core
insight. The train/test gap comparison is your diagnostic: same
train score, better test score = genuinely better model.

**Code:**
```python
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
models = {
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(random_state=42),
    "Gradient Boosting": GradientBoostingClassifier(random_state=42),
}
results = {name: (m.fit(X_train, y_train).score(X_train, y_train),
                  m.score(X_test, y_test)) for name, m in models.items()}
```

**Common confusion:** "More trees = better" is not free — bagging
plateaus (100 trees ≈ 500 trees), while boosting can OVERFIT if you
keep adding trees without a small learning rate. Watch test
accuracy, not just train.

---

### 9. Recursive Feature Elimination (RFE) — `p03`

**What it is:** Automatic feature selection: train a model, look at
importances, delete the least-useful feature, retrain, repeat until
N features remain. Surviving features are the ones the model
actually depends on — noise columns get voted off the island.

**Worked example:**
```
10 features, only 5 informative (n_informative=5):
  round 1: all 10 → drop weakest (say feature 0)
  round 2: 9 feats → drop next weakest ... until 5 left

rfe.support_ = [False False False  True  True  True  True False  True False]
np.where(support_)[0] → [3, 4, 5, 6, 8]  ← the informative ones!

Retrain on just those → test accuracy 0.9250
```

**Why ML cares:** Noise features hurt: they slow training, add
variance, and muddy interpretation. "Use everything" is a beginner
habit; pros prune. RFE wraps any model with importances/coefs —
it's model-agnostic feature selection.

**Code:**
```python
from sklearn.feature_selection import RFE
rfe = RFE(RandomForestClassifier(random_state=42),
          n_features_to_select=5)
rfe.fit(X_train, y_train)
kept = np.where(rfe.support_)[0].tolist()   # [3,4,5,6,8]
X_train_sel = X_train[:, rfe.support_]      # column mask
```

**Common confusion:** Fit RFE on TRAIN only — letting it see test
data during selection is leakage (level-02 `hard/p01` again). Then
apply `rfe.support_` to BOTH train and test to keep the columns
aligned.

---

## Done with concepts? → Try `easy/p01-linear-scratch.py`
