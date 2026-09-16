# Level 07 — Concepts (Detailed Explanations)

Read each section BEFORE attempting its problem. Each concept has:
what it is in plain words → a worked example with real numbers →
why ML cares → the code → what confuses beginners.

---

## Easy

### 1. K-Means Clustering — `p01`

**What it is:** Group unlabeled data into K clusters. There are no
answers to learn from — the algorithm just finds groups of points
that sit close together. It loops: assign each point to its nearest
center → move each center to the mean of its points → repeat.

**Worked example:**
```
Points: [1,1], [1,2], [2,1], [9,9], [9,8], [8,9]   (2 obvious groups)
Say K=2, initial centers land at c1=[1.5,1], c2=[8,9]

Round 1 — assign:
  [1,1] dist to c1 = 0.5, to c2 ≈ 11 → cluster 1
  [9,9] dist to c1 ≈ 11,  to c2 = 1  → cluster 2
  ... all left points → 1, all right points → 2

Round 1 — update centers:
  c1 = mean of [1,1],[1,2],[2,1] = [1.33, 1.33]
  c2 = mean of [9,9],[9,8],[8,9] = [8.67, 8.67]

Round 2 — assignments don't change → CONVERGED.
```

**Why ML cares:** Clustering is the #1 unsupervised tool: customer
segments, image grouping, document grouping, anomaly pre-processing.
Whenever you have data but no labels, clustering is where you start.

**Code:**
```python
from sklearn.cluster import KMeans
km = KMeans(n_clusters=3, random_state=42, n_init=10)
km.fit(X)
km.labels_           # which cluster each point got: e.g. [0,2,1,...]
km.cluster_centers_  # the 3 learned centers
```

**Common confusion:** `n_init=10` means sklearn runs the whole
algorithm 10 times with different random starts and keeps the best
— K-Means can get stuck in bad local optima. Always set it.

---

### 2. Elbow Method (Picking K) — `p02`

**What it is:** K-Means needs YOU to choose K — it can't guess.
Try every K from 1 to 10, record `inertia_` (sum of squared
distances from each point to its center — lower = tighter
clusters). The "elbow" is where improvement suddenly flattens.

**Worked example:**
```
K=1: inertia ≈ 20402   (one giant cluster — terrible)
K=2: inertia ≈  3000   (big improvement)
K=3: inertia ≈   567   (huge drop — the true number!)
K=4: inertia ≈   500   (barely better)
K=5: inertia ≈   460   (diminishing returns...)

Plot looks like an arm: steep drop, then flat.
The bend — the "elbow" — is at K=3.
```

**Why ML cares:** "How many groups are there?" is a business
question disguised as a math one. Elbow gives you a defensible
answer instead of a guess. Silhouette score (medium/p01) is the
numeric version of the same idea.

**Code:**
```python
inertias = []
for k in range(1, 11):
    km = KMeans(n_clusters=k, n_init=10).fit(X)
    inertias.append(km.inertia_)
```

**Common confusion:** Inertia ALWAYS decreases as K grows (K = n
points → inertia 0). You're not looking for the LOWEST inertia —
you're looking for where the drop-off stops being worth it.

---

### 3. PCA for Visualization — `p03`

**What it is:** You can't plot 4-dimensional data — but PCA can
squash it to 2D while keeping as much variance (spread = information)
as possible. `explained_variance_ratio_` tells you how much
information survived the squashing.

**Worked example:**
```
Iris dataset: 150 flowers × 4 features (petal/sepal length+width)

After StandardScaler → PCA(n_components=2):
  explained_variance_ratio_ = [0.7296, 0.2285]
  total = 0.9581

Meaning: the 2D plot keeps 95.8% of the original 4D information.
You lose almost nothing and gain a picture you can actually see —
the 3 iris species show up as visibly separate blobs.
```

**Why ML cares:** "Let me look at the data" is the first move in
any project — PCA makes high-D data lookable. It's also a legit
preprocessing step (level-06 p03): fewer dimensions → faster
models, less overfitting.

**Code:**
```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
X_s = StandardScaler().fit_transform(X)   # scale FIRST, always
X_2d = PCA(n_components=2).fit_transform(X_s)   # (150, 4) → (150, 2)
```

**Common confusion:** The 2 new axes are NOT "the 2 best original
features" — they're blends (weighted sums) of all 4. That's why
PCA axes can't be labeled with meaningful names.

---

## Medium

### 4. Silhouette Score — `p01`

**What it is:** A NUMBER that grades cluster quality — no eyeballing
a plot required. For each point, compare how close it is to its own
cluster vs. the nearest other cluster. Score in [-1, 1]; higher = better.

**Worked example:**
```
For one point p in cluster A:
  a = mean distance from p to others in A      = 1.2  (cohesion)
  b = mean distance from p to nearest cluster B = 4.8  (separation)

  s = (b - a) / max(a, b) = (4.8 - 1.2) / 4.8 = 0.75  → well clustered

If p were closer to B than its own cluster (a=4.8, b=1.2):
  s = (1.2 - 4.8)/4.8 = -0.75  → p is probably misassigned!

Average s over all points = silhouette_score.
K=2..7 on blob data: K=3 wins with s ≈ 0.847.
```

**Why ML cares:** Elbow is subjective — two people can disagree on
where the bend is. Silhouette gives a number you can argue with,
report in a paper, or pick the argmax of in code.

**Code:**
```python
from sklearn.metrics import silhouette_score
scores = {}
for k in range(2, 8):
    labels = KMeans(n_clusters=k, n_init=10).fit_predict(X)
    scores[k] = silhouette_score(X, labels)
best_k = max(scores, key=scores.get)
```

**Common confusion:** Silhouette needs at least 2 clusters (you
can't compute "nearest OTHER cluster" with K=1) and breaks down
when clusters have weird shapes — it's still assuming blob-ish
clusters like K-Means does.

---

### 5. DBSCAN (Density-Based Clustering) — `p02`

**What it is:** K-Means assumes clusters are round blobs — it will
slice a crescent moon in half. DBSCAN instead groups by DENSITY:
points with enough neighbors close by are one cluster; points in
empty regions get labeled noise (-1). No K needed, any shape allowed.

**Worked example:**
```
make_moons data: two interleaved crescents.

K-Means(2): draws a straight boundary → each "cluster" contains
            half of BOTH moons. Wrong.

DBSCAN(eps=0.3, min_samples=5):
  - picks a point, checks: are ≥5 points within 0.3 distance?
  - if yes: those points + their dense neighbors = one cluster,
    growing outward along the dense moon
  - isolated points → label -1 (noise)

Result: 2 clusters that actually match the crescents.
```

**Why ML cares:** Real clusters are rarely spherical — geographic
regions, fraud rings, sensor networks. DBSCAN also gives you FREE
outlier detection (the -1 points). It's the tool you reach for when
K-Means' shapes look wrong.

**Code:**
```python
from sklearn.cluster import DBSCAN
labels = DBSCAN(eps=0.3, min_samples=5).fit_predict(X)
# set(labels) may include -1 = noise points
```

**Common confusion:** `eps` is the whole game. Too small →
everything is noise (-1 everywhere). Too big → everything merges
into one cluster. Scale your features first and sweep eps.

---

### 6. Hierarchical / Agglomerative Clustering — `p03`

**What it is:** Build clusters bottom-up like a family tree: start
with every point as its own cluster, repeatedly merge the two
closest clusters, stop when K remain. The merge history is a
dendrogram — a tree showing which groups joined when.

**Worked example:**
```
Points on a line: [1, 2, 3, 10, 11, 20]

Step 1: closest pair = {1,2} → merge → cluster {1,2}
Step 2: {1,2} vs 3 → merge → {1,2,3}
Step 3: {10,11} → merge → {10,11}
Now: {1,2,3}, {10,11}, {20}
Step 4: stop at n_clusters=3 → labels [0,0,0,1,1,2]
```

**Why ML cares:** Unlike K-Means you get a full hierarchy — useful
when "how many groups" depends on zoom level (genes, documents,
product taxonomies). `linkage='ward'` (the default) merges to keep
clusters tight and compact.

**Code:**
```python
from sklearn.cluster import AgglomerativeClustering
labels = AgglomerativeClustering(n_clusters=3).fit_predict(X)
```

**Common confusion:** It's O(n²) or worse — fine for 50-5,000
points, painful for 500,000. For big data, K-Means or mini-batch
variants scale better.

---

## Hard

### 7. Customer Segmentation — `p01`

**What it is:** The classic business use of clustering: group
customers by behavior (age, income, spending), then read the
per-cluster averages to name each segment. Clustering gives you
groups; the means table tells you what the groups MEAN.

**Worked example:**
```
200 customers × [age, income, spending], KMeans(5) →

groupby('cluster').mean() gives something like:
  cluster | age  | income | spending
     0    | 28   | 90k    | 85    → "young rich big spenders" ← VIPs
     1    | 55   | 45k    | 20    → "older low spenders"
     2    | 35   | 30k    | 50    → "budget shoppers"
    ...

Action: market differently to each segment.
```

**Why ML cares:** This is clustering's paycheck — segmentation
drives real marketing, product, and pricing decisions. The ML is
one line (KMeans); the VALUE is in scaling correctly and
interpreting the means.

**Code:**
```python
X_s = StandardScaler().fit_transform(df[['age','income','spending']])
df['cluster'] = KMeans(5, random_state=42, n_init=10).fit_predict(X_s)
means = df.groupby('cluster')[['age','income','spending']].mean()
```

**Common confusion:** Cluster on SCALED features but interpret the
means on the ORIGINAL columns — that's why you add the cluster
label to the original df. And cluster IDs (0,1,2,...) are arbitrary
names, not rankings — cluster 0 isn't "best."

---

### 8. Anomaly Detection (Isolation Forest) — `p02`

**What it is:** Find weird points without labeled examples.
IsolationForest builds random split trees; normal points hide deep
in the crowd (many splits to isolate), anomalies sit alone (few
splits). Fewer splits to isolate = more anomalous.

**Worked example:**
```
Data: 100 normal points ~ N(0, 0.5)   → tight blob near origin
      + 10 injected outliers ~ U(-5,5) → scattered far away

IsolationForest(contamination=0.1).predict(X)
  → returns +1 (normal) or -1 (anomaly) per point

Output: 110 predictions, 11 flagged as -1
(the 10 injected outliers + 1 borderline normal point —
 close to the expected 10% contamination)
```

**Why ML cares:** Fraud detection, defective parts, network
intrusion, sensor failures — you rarely have labeled "anomaly"
examples, so supervised learning can't help. Contamination tells
the model roughly what fraction to flag.

**Code:**
```python
from sklearn.ensemble import IsolationForest
iso = IsolationForest(contamination=0.1, random_state=42)
preds = iso.fit_predict(X)          # +1 normal, -1 anomaly
n_anomalies = (preds == -1).sum()
```

**Common confusion:** `contamination` is your GUESS of the anomaly
rate — set it to 0.1 and it will flag ~10% even if the true rate
is 1%. It's a threshold knob, not a detector of the true rate.

---

### 9. Topic Modeling (TF-IDF → NMF) — `p03`

**What it is:** Discover hidden themes in documents with no labels.
Step 1: `TfidfVectorizer` turns text into numbers (each doc = a
vector of word-importance scores). Step 2: `NMF` factorizes that
matrix into "each doc = mix of topics" × "each topic = mix of words."

**Worked example:**
```
Docs: 2 about ML ("python machine learning model...")
      2 about cooking ("recipe food kitchen bake...")

TF-IDF → matrix (4 docs × ~30 words)
NMF(n_components=2) splits it into:

  Topic 0 top words: python, machine, learning, model, data  → ML
  Topic 1 top words: recipe, food, kitchen, cook, bake       → cooking

doc-topic matrix W (4×2): doc 0 ≈ [0.9, 0.05] → mostly topic 0
```

**Why ML cares:** Topic modeling powers "what are customers
complaining about," news categorization, and support-ticket routing
— all unlabeled. It's the text version of clustering, and a stepping
stone to embeddings/LLM-era NLP.

**Code:**
```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
vec = TfidfVectorizer(stop_words='english')
X = vec.fit_transform(docs)
nmf = NMF(n_components=2, random_state=42).fit(X)
W = nmf.transform(X)                              # docs × topics
top = nmf.components_[i].argsort()[-5:][::-1]     # top words for topic i
words = vec.get_feature_names_out()[top]
```

**Common confusion:** NMF finds word-groups but doesn't NAME them —
"topic 0" is just a bag of words until a human reads the top words
and labels it "the ML topic." Also, `stop_words='english'` is
essential or every topic is "the, and, of."

---

## Done with concepts? → Try `easy/p01-kmeans.py`
