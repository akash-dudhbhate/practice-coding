# Level 07 — Concepts (Detailed Explanations)

> Read each section BEFORE attempting its problem. Each concept explains:
> **What it is** · **Why it exists** · **Where it's used** ·
> **What goes wrong** without it · worked example · code ·
> expected output.

---

## Easy

### 1. K-Means Clustering — `p01`

**What it is:** Group unlabeled data into K clusters. There are no
answers to learn from — the algorithm just finds groups of points
that sit close together. It loops: assign each point to its nearest
center → move each center to the mean of its points → repeat.

**Why it exists:** Most real data has no labels — nobody tagged
"customer segment" for you. K-Means exists to find structure
anyway, using proximity as the definition of "same group."

**Where it's used:** The #1 unsupervised tool: customer
segments, image grouping, document grouping, anomaly
pre-processing. Whenever you have data but no labels, clustering
is where you start.

**What goes wrong without it:** Without it, "find the natural
groups" means eyeballing thousands of rows. The algorithm's own
failure: it can get stuck in bad local optima — a lucky/unlucky
random start decides the clusters. `n_init=10` runs the whole
thing 10 times with different starts and keeps the best; skip it
and one bad seed gives you nonsense clusters that still "worked."
Also it assumes round blobs — crescents get sliced in half (see
`medium/p02`).

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

**Code:**
```python
from sklearn.cluster import KMeans
km = KMeans(n_clusters=3, random_state=42, n_init=10)
km.fit(X)
km.labels_           # which cluster each point got: e.g. [0,2,1,...]
km.cluster_centers_  # the 3 learned centers
```

**Expected output:** `km.labels_` → an array of cluster ids like
`[0,2,1,0,...]` (one per point); `km.cluster_centers_` → a `(3,
n_features)` array holding each cluster's center point.

---

### 2. Elbow Method (Picking K) — `p02`

**What it is:** K-Means needs YOU to choose K — it can't guess.
Try every K from 1 to 10, record `inertia_` (sum of squared
distances from each point to its center — lower = tighter
clusters). The "elbow" is where improvement suddenly flattens.

**Why it exists:** "How many groups are there?" is a business
question disguised as a math one — the algorithm won't answer it.
The elbow exists to turn "pick a number" into a defensible
reading of diminishing returns.

**Where it's used:** Choosing K for K-Means before segmentation,
grouping, or compression work. Silhouette score (`medium/p01`) is
the numeric version of the same idea.

**What goes wrong without it:** Guess K=5 on 3-cluster data → two
real clusters get split arbitrarily and two fake ones get merged —
your "segments" don't correspond to anything real. Reading trap:
inertia ALWAYS decreases as K grows (K = n points → inertia 0).
You're not looking for the LOWEST inertia — you're looking for
where the drop-off stops being worth it.

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

**Code:**
```python
inertias = []
for k in range(1, 11):
    km = KMeans(n_clusters=k, n_init=10).fit(X)
    inertias.append(km.inertia_)
```

**Expected output:** `inertias` → a decreasing list like
`[20402, 3000, 567, 500, 460, ...]` — plotted, a steep cliff from
K=1→3 then a flat tail; the elbow sits at K=3.

---

### 3. PCA for Visualization — `p03`

**What it is:** You can't plot 4-dimensional data — but PCA can
squash it to 2D while keeping as much variance (spread = information)
as possible. `explained_variance_ratio_` tells you how much
information survived the squashing.

**Why it exists:** "Let me look at the data" is the first move in
any project — and humans see in 2D. PCA exists to make high-D
data lookable while keeping the most faithful projection.

**Where it's used:** Visualizing clusters, checking class
separability before training, spotting outliers by eye — also a
legit preprocessing step (level-06 `p03`): fewer dimensions →
faster models, less overfitting.

**What goes wrong without it:** Plot two raw features out of four
→ you might pick the two that DON'T separate the classes and
conclude the data is hopeless. Forget to scale first → PCA
worships the biggest-magnitude column (it maximizes variance, and
unscaled income has the most "variance" by units alone). And the
axes can't be labeled meaningfully — they're blends of all 4
features, not "the 2 best original features."

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

**Code:**
```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
X_s = StandardScaler().fit_transform(X)   # scale FIRST, always
X_2d = PCA(n_components=2).fit_transform(X_s)   # (150, 4) → (150, 2)
```

**Expected output:** `X_2d.shape` → `(150, 2)`;
`explained_variance_ratio_` → `[0.7296, 0.2285]` (sum `0.9581`).
Plotted: three species as visibly separate point blobs — setosa
far to one side, versicolor and virginica closer together but
still mostly distinct.

---

## Medium

### 4. Silhouette Score — `p01`

**What it is:** A NUMBER that grades cluster quality — no eyeballing
a plot required. For each point, compare how close it is to its own
cluster vs. the nearest other cluster. Score in [-1, 1]; higher = better.

**Why it exists:** Elbow is subjective — two people disagree on
where the bend is. Silhouette exists to make cluster quality an
argmax-able number: `best_k = max(scores)`.

**Where it's used:** Choosing K programmatically, comparing
clustering runs, reporting cluster quality in papers and
dashboards.

**What goes wrong without it:** Without a number, "K=3 looked
right" is a vibe you can't defend or automate — pick K by eye and
the next person picks K=4 from the same plot. Its own limits:
needs at least 2 clusters (can't compute "nearest OTHER cluster"
with K=1 → error), and assumes blob-ish clusters like K-Means —
on crescent shapes it can reward the WRONG clustering.

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

**Code:**
```python
from sklearn.metrics import silhouette_score
scores = {}
for k in range(2, 8):
    labels = KMeans(n_clusters=k, n_init=10).fit_predict(X)
    scores[k] = silhouette_score(X, labels)
best_k = max(scores, key=scores.get)
```

**Expected output:** `scores` → `{2: ~0.68, 3: ~0.85, 4: ~0.7,
...}`; `best_k` → `3` — matching the elbow's answer with a number
(≈ 0.847) you can put in a report.

---

### 5. DBSCAN (Density-Based Clustering) — `p02`

**What it is:** K-Means assumes clusters are round blobs — it will
slice a crescent moon in half. DBSCAN instead groups by DENSITY:
points with enough neighbors close by are one cluster; points in
empty regions get labeled noise (-1). No K needed, any shape allowed.

**Why it exists:** Real clusters are rarely spherical — geographic
regions, fraud rings, sensor networks. DBSCAN exists to follow the
shape of the data itself rather than forcing circles onto it.

**Where it's used:** Non-blob clustering and FREE outlier
detection (the -1 points) — geographic data, trajectory data,
anywhere the "clusters" are weird shapes with scattered noise.

**What goes wrong without it:** K-Means on moon-shaped data draws
a straight boundary — each "cluster" contains half of BOTH
moons, confidently wrong. DBSCAN's own trap: `eps` is the whole
game — too small → everything is noise (-1 everywhere, no
clusters found); too big → everything merges into one cluster.
Scale features first and sweep eps or you'll debug "why does it
return only -1?"

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

**Code:**
```python
from sklearn.cluster import DBSCAN
labels = DBSCAN(eps=0.3, min_samples=5).fit_predict(X)
# set(labels) may include -1 = noise points
```

**Expected output:** `labels` → mostly `0`/`1` tracing the two
crescents correctly, plus a few `-1` for isolated noise points —
`set(labels)` → `{0, 1, -1}`; K-Means on the same data visibly
splits each crescent down the middle.

---

### 6. Hierarchical / Agglomerative Clustering — `p03`

**What it is:** Build clusters bottom-up like a family tree: start
with every point as its own cluster, repeatedly merge the two
closest clusters, stop when K remain. The merge history is a
dendrogram — a tree showing which groups joined when.

**Why it exists:** "How many groups" often depends on zoom level —
genes, documents, product taxonomies all have nested structure.
Hierarchical clustering exists to give you the whole tree, so K=2
vs K=5 is a choice you make AFTER seeing the structure, not before.

**Where it's used:** Taxonomies, document organization, gene
expression analysis — anywhere "groups of groups" is the real
shape of the data. `linkage='ward'` (the default) merges to keep
clusters tight and compact.

**What goes wrong without it:** With only K-Means you get flat
clusters — you never learn that your "3 segments" are really 2
super-groups with sub-structure. Scaling trap: it's O(n²) or
worse — fine for 50-5,000 points, painful for 500,000. For big
data, K-Means or mini-batch variants scale better — reach for
this when n is modest and the hierarchy itself is the payoff.

**Worked example:**
```
Points on a line: [1, 2, 3, 10, 11, 20]

Step 1: closest pair = {1,2} → merge → cluster {1,2}
Step 2: {1,2} vs 3 → merge → {1,2,3}
Step 3: {10,11} → merge → {10,11}
Now: {1,2,3}, {10,11}, {20}
Step 4: stop at n_clusters=3 → labels [0,0,0,1,1,2]
```

**Code:**
```python
from sklearn.cluster import AgglomerativeClustering
labels = AgglomerativeClustering(n_clusters=3).fit_predict(X)
```

**Expected output:** `labels` → `[0, 0, 0, 1, 1, 2]` — the three
groups {1,2,3}, {10,11}, {20} recovered exactly, plus a merge
history showing {1,2} joined first.

---

## Hard

### 7. Customer Segmentation — `p01`

**What it is:** The classic business use of clustering: group
customers by behavior (age, income, spending), then read the
per-cluster averages to name each segment. Clustering gives you
groups; the means table tells you what the groups MEAN.

**Why it exists:** "Different customers need different treatment"
is a strategy, not a script — segmentation exists to turn raw
behavior into a small number of actionable groups.

**Where it's used:** Marketing segments, product tiers, pricing —
clustering's paycheck. The ML is one line (KMeans); the VALUE is
in scaling correctly and interpreting the means.

**What goes wrong without it:** Cluster on unscaled features →
income (0-120k) dominates distance, so your "segments" are just
income buckets wearing a costume — age and spending contributed
nothing. Interpretation trap: cluster on SCALED features but read
means on the ORIGINAL columns (that's why the label goes on the
original df). And cluster IDs are arbitrary names, not rankings —
cluster 0 isn't "best."

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

**Code:**
```python
X_s = StandardScaler().fit_transform(df[['age','income','spending']])
df['cluster'] = KMeans(5, random_state=42, n_init=10).fit_predict(X_s)
means = df.groupby('cluster')[['age','income','spending']].mean()
```

**Expected output:** `means` → a 5-row table where each cluster's
original-scale averages differ meaningfully (e.g., one row high
income+spending = VIPs, another low income+low spending = budget
segment) — the rows read as distinct customer personas.

---

### 8. Anomaly Detection (Isolation Forest) — `p02`

**What it is:** Find weird points without labeled examples.
IsolationForest builds random split trees; normal points hide deep
in the crowd (many splits to isolate), anomalies sit alone (few
splits). Fewer splits to isolate = more anomalous.

**Why it exists:** You rarely have labeled "anomaly" examples —
fraud is rare and mutates. IsolationForest exists because "easy
to separate from the crowd" is learnable WITHOUT labels.

**Where it's used:** Fraud detection, defective parts, network
intrusion, sensor failures — flagging the weird rows for human
review.

**What goes wrong without it:** Supervised learning can't help
(you have no "fraud" labels), and eyeballing misses subtle
multivariate weirdness — a normal age + normal income that's
impossible TOGETHER. Its own trap: `contamination` is your GUESS
of the anomaly rate — set 0.1 and it flags ~10% even if the true
rate is 1%, burying real anomalies in false alarms. It's a
threshold knob, not a detector of the true rate.

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

**Code:**
```python
from sklearn.ensemble import IsolationForest
iso = IsolationForest(contamination=0.1, random_state=42)
preds = iso.fit_predict(X)          # +1 normal, -1 anomaly
n_anomalies = (preds == -1).sum()
```

**Expected output:** `preds` → an array of `1`s and `-1`s;
`n_anomalies` → `11` (the 10 injected outliers plus ~1 borderline
normal point) — matching `contamination=0.1` on 110 rows.

---

### 9. Topic Modeling (TF-IDF → NMF) — `p03`

**What it is:** Discover hidden themes in documents with no labels.
Step 1: `TfidfVectorizer` turns text into numbers (each doc = a
vector of word-importance scores). Step 2: `NMF` factorizes that
matrix into "each doc = mix of topics" × "each topic = mix of words."

**Why it exists:** "What are these 10,000 documents about?" has no
label column to learn from — topics must be discovered, not
predicted. TF-IDF exists because raw word counts reward common
words; NMF exists because co-occurring words reveal the themes.

**Where it's used:** "What are customers complaining about," news
categorization, support-ticket routing — the text version of
clustering, and a stepping stone to embeddings/LLM-era NLP.

**What goes wrong without it:** Skip `stop_words='english'` and
every topic is "the, and, of" — the top words carry zero signal.
And NMF doesn't NAME anything — "topic 0" is just a bag of words
until a human reads the top words and labels it "the ML topic."
Ship unnamed topic IDs to a stakeholder and the output is
useless.

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

**Expected output:** `W` → a (4, 2) matrix like `[[0.9, 0.05],
[0.85, 0.1], [0.05, 0.9], [0.1, 0.85]]` — ML docs heavy on topic
0, cooking docs heavy on topic 1. `words` per topic →
`['python', 'machine', 'learning', 'model', 'data']` and
`['recipe', 'food', 'kitchen', 'cook', 'bake']`.

---

## Done with concepts? → Try `easy/p01-kmeans.py`
