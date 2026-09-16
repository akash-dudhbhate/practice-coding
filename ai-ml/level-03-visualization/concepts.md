# Level 03 — Concepts (Detailed Explanations)

Read each section BEFORE attempting its problem. Each concept has:
what it is in plain words → a worked example with real numbers →
why ML cares → the code → what confuses beginners.

---

## Easy

### 1. Line Plots — `p01`

**What it is:** A line plot connects (x, y) points — the chart for
"how does y change as x changes?" matplotlib's workflow: build x
with `np.linspace(start, stop, n)`, plot each curve with a `label`,
then `legend()`, `grid()`, `savefig()`, `show()`.

**Worked example:**
```python
x = np.linspace(0, 10, 100)   # 100 evenly spaced points 0→10
# x[0]=0.0, x[1]≈0.101, ..., x[99]=10.0
plt.plot(x, np.sin(x), label='sin(x)')
plt.plot(x, np.cos(x), label='cos(x)')
# sin(0)=0, sin(π/2)=1 → the curve oscillates −1..1 across 0..10
plt.legend(); plt.grid(True)
plt.savefig('trig_plot.png')
```

**Why ML cares:** Loss-vs-epoch training curves, learning curves,
ROC curves — every diagnostic chart in later levels is a line plot.
`savefig` before `show` because `show()` clears the figure buffer.

**Code:**
```python
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x), label='sin(x)')
plt.xlabel('x'); plt.ylabel('y'); plt.title('Trig')
plt.legend(); plt.grid(True)
plt.savefig('trig_plot.png'); plt.show()
```

**Common confusion:** Nothing appears without `plt.show()` — and
`savefig` AFTER `show()` saves a blank PNG, because `show()` resets
the figure. Save first, then show.

---

### 2. Scatter Plots — `p02`

**What it is:** Points instead of lines — `plt.scatter(x, y)`. The
chart for "is there a relationship between two variables?" To color
by category, plot each group separately with a boolean mask and a
`label`, then `legend()`.

**Worked example:**
```python
np.random.seed(42)
height = np.random.normal(170, 10, 100)        # mean 170, std 10
weight = height * 0.6 + np.random.normal(0, 5, 100)
gender = np.random.choice(['M', 'F'], 100)

mask = gender == 'M'                            # boolean array
plt.scatter(height[mask], weight[mask], c='blue', label='M')
# height[mask] keeps only the M rows → colored cloud per group
# height.mean() ≈ 170.3
```

**Why ML cares:** Scatter plots reveal the shape of your problem
before you model: linear trend → regression; separate clouds →
classification; no pattern → these features won't help. Clustering
results (level-06) are always shown this way.

**Code:**
```python
mask = gender == 'M'
plt.scatter(height[mask], weight[mask], c='blue', label='M')
plt.scatter(height[~mask], weight[~mask], c='red', label='F')
plt.legend(); plt.savefig('scatter_plot.png'); plt.show()
```

**Common confusion:** `c='blue'` (one color) vs `c=array`
(color-per-point via colormap) behave totally differently. For
categories, plotting each group separately with `label` is the
simplest path — `~mask` is "not mask" (the F rows).

---

### 3. Histograms — `p03`

**What it is:** A histogram bins values and counts how many fall in
each bin — the chart for "what's the distribution of ONE variable?"
Add `plt.axvline` for vertical reference lines at the mean/median.

**Worked example:**
```python
scores = np.clip(np.random.normal(75, 15, 200), 0, 100)
# 200 exam scores, bell-curved around 75, clipped to valid range
plt.hist(scores, bins=20, edgecolor='black', alpha=0.7)
# 20 bins → each bin covers (100-0)/20 = 5 points of score
# mean ≈ 74.5, median ≈ 75 — dashed lines show the center
plt.axvline(np.mean(scores),   color='red',   linestyle='--', label='Mean')
plt.axvline(np.median(scores), color='green', linestyle='--', label='Median')
```

**Why ML cares:** Checking distributions is step one of data work —
a feature skewed right might need a log transform; a target with
two humps might actually be two populations. Mean≠median on the
histogram is the visual signature of skew.

**Code:**
```python
plt.hist(scores, bins=20, edgecolor='black', alpha=0.7)
plt.axvline(np.mean(scores), color='red', linestyle='--')
plt.savefig('histogram.png'); plt.show()
```

**Common confusion:** `bins` is the number of BARS, not their width.
Too few bins hides the shape (all data in 3 bars); too many shows
noise as fake patterns. 20-30 is a reasonable default for a few
hundred points.

---

## Medium

### 4. Correlation Heatmap — `p01`

**What it is:** **Correlation** measures how much two variables move
together: +1 = perfectly together, 0 = unrelated, −1 = opposite.
`df.corr()` builds the n×n matrix of all pairs; `sns.heatmap`
draws it as a color-coded grid so patterns jump out.

**Worked example:**
```
df = 5 columns × 100 rows of random normals

corr matrix (concept):
              feat_a  feat_b  feat_c  feat_d  target
  feat_a       1.00    0.12   -0.05    0.03    0.21
  feat_b       0.12    1.00    0.08   -0.02    0.55  ← strongest
  ...                                    ...          predictor
  target       0.21    0.55    ...     ...     1.00

Diagonal is always 1.00 — every column correlates perfectly
with itself.
```

**Why ML cares:** The target row tells you which features matter
before you train anything (feature selection, `hard/p03` in
level-04). Two features at 0.95 = redundant — one may be dropped.
This is the fastest "which columns matter?" scan there is.

**Code:**
```python
import seaborn as sns
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, fmt='.2f')
plt.savefig('correlation_heatmap.png'); plt.show()
```

**Common confusion:** Correlation ≠ causation, and it's NOT slope —
correlation of 0.9 doesn't mean y grows 0.9 per x, it means the
relationship is tightly linear. Also: `annot=True` prints the
numbers ON the cells; without it you're guessing shades of red.

---

### 5. Subplots — `p02`

**What it is:** `plt.subplots(2, 2)` returns one figure plus a 2×2
GRID of axes objects — each subplot is an independent plot you
address like a matrix: `axes[0,0]` top-left, `axes[1,1]`
bottom-right.

**Worked example:**
```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].plot(x, np.sin(x))                      # line
axes[0, 1].scatter(np.random.rand(50), np.random.rand(50))
axes[1, 0].hist(np.random.normal(0, 1, 200), bins=20)
axes[1, 1].bar(['A','B','C','D'], [23, 45, 56, 78])  # bars:
# A=23, B=45, C=56, D=78 — heights 23..78

len(fig.axes)   # 4
```

**Why ML cares:** Comparing plots side-by-side IS analysis — e.g.,
before/after scaling histograms, train vs test distributions,
multiple model ROC curves. Single-plot thinking hides comparisons
that matter.

**Code:**
```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes[0, 0].plot(x, np.sin(x)); axes[0, 0].set_title('sin')
plt.tight_layout()              # stop labels overlapping
plt.savefig('dashboard.png'); plt.show()
```

**Common confusion:** With `plt.plot` you call `plt.xlabel`; with
an axes object it's `ax.set_xlabel` — method names get `set_`
prefixes (`set_title`, `set_xlabel`). Mixing `plt.` and `ax.` calls
puts labels on the WRONG subplot.

---

### 6. Box Plots + Swarm Overlay — `p03`

**What it is:** A box plot summarizes each group's distribution in
5 numbers: the box spans Q1→Q3 (middle 50%), the line inside is the
median, whiskers reach ~1.5×IQR, dots beyond are outliers.
`sns.swarmplot` draws every raw point on top — summary AND evidence.

**Worked example:**
```
4 groups × 50 points each:
  A ~ normal(50, 10)   → mean ≈ 50
  B ~ normal(60, 15)   → mean ≈ 60   (widest box — std 15)
  C ~ normal(55, 12)   → mean ≈ 55
  D ~ normal(70, 8)    → mean ≈ 70   (narrowest box — std 8)

Reading the plot: D's box sits highest, B's box is tallest.
df.groupby('category')['value'].mean() → A 50, B 60, C 55, D 70
```

**Why ML cares:** Comparing distributions across categories is how
you spot group differences — e.g., does feature "income" separate
churners from non-churners? Box plots show it at a glance; the
swarm overlay proves it's not 3 outliers faking the difference.

**Code:**
```python
sns.boxplot(x='category', y='value', data=df)
sns.swarmplot(x='category', y='value', data=df,
              color='black', alpha=0.4, size=3)
plt.savefig('boxplot.png'); plt.show()
```

**Common confusion:** The box EDGE is not the mean — it's the
quartiles (Q1, median, Q3). And whiskers are NOT min/max: they're
~1.5×IQR fences, with points beyond them drawn separately as
candidate outliers (same 1.5×IQR rule as level-02 `medium/p02`).

---

## Hard

### 7. Groupby + Dashboards — `p01`

**What it is:** `df.groupby('col')['val'].sum()` collapses rows into
per-group aggregates — pandas' version of SQL GROUP BY. Pandas can
plot these directly (`.plot(kind='bar')`), and `.unstack()` pivots
a two-key groupby into a matrix for heatmaps.

**Worked example:**
```
90 rows of sales: date, revenue ~ N(10000, 2000), product, region

df.groupby('product')['revenue'].sum()
  → A ~3.0M, B ~3.0M, C ~3.0M  (one total per product)

df.groupby(['product','region'])['revenue'].sum().unstack()
  → 3×4 matrix: product rows × region columns
    A/North, A/South, ... — perfect input for sns.heatmap
```

**Why ML cares:** Dashboards are how results get communicated.
Aggregating raw rows into "total revenue per product per region" is
exactly the feature-engineering move used in real ML pipelines too.

**Code:**
```python
data.groupby('product')['revenue'].sum().plot(
    kind='bar', ax=axes[0, 1])
pivot = data.groupby(['product', 'region'])['revenue'].sum().unstack()
sns.heatmap(pivot, annot=True, ax=axes[1, 1])
```

**Common confusion:** `groupby` alone is lazy — `df.groupby('col')`
returns a groupby OBJECT, not data. You must add an aggregation
(`.sum()`, `.mean()`). And `.unstack()` is what turns the
two-level groupby into a 2D table the heatmap can eat.

---

### 8. Animation with FuncAnimation — `p02`

**What it is:** `FuncAnimation` calls YOUR update function once per
frame; each call mutates the plotted artists (e.g.,
`line.set_ydata(...)`) instead of redrawing from scratch. `frames`
= how many times, `interval` = ms between frames, `blit=True` =
redraw only what changed (fast).

**Worked example:**
```python
x = np.linspace(0, 2*np.pi, 100)        # x[-1] ≈ 6.2832
line, = plt.plot(x, np.sin(x))

def update(frame):
    # frame counts 0,1,2,...,99 — phase shifts the wave right
    line.set_ydata(np.sin(x + frame / 10))
    return line,                        # artists that changed

anim = FuncAnimation(fig, update, frames=100,
                     interval=50, blit=True)
# 100 frames × 50ms = 5-second loop of a traveling sine wave
```

**Why ML cares:** Watching a process evolve beats static snapshots —
gradient descent converging, clusters forming, decision boundaries
shifting. It's also a great sanity check that your iterative code
is actually doing something sensible per step.

**Code:**
```python
from matplotlib.animation import FuncAnimation
def update(frame):
    line.set_ydata(np.sin(x + frame / 10))
    return line,
anim = FuncAnimation(fig, update, frames=100, interval=50, blit=True)
plt.show()
```

**Common confusion:** `line, = plt.plot(...)` — the trailing comma
unpacks the LIST `plot` returns (one Line2D). Without it, `line` is
a list and `set_ydata` fails. Also `update` must RETURN the changed
artists when `blit=True`, or nothing moves.

---

### 9. Publication-Quality Figures — `p03`

**What it is:** Journal/blog-ready polish: serif fonts via
`rcParams`, removed top/right spines for a clean look,
`fill_between` for shaded regions, `tight_layout` so nothing clips,
and `dpi=300` so the PNG is sharp in print (screen default is ~100).

**Worked example:**
```python
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 12

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, np.sin(x)); ax.plot(x, np.cos(x))
ax.fill_between(x, np.sin(x), np.cos(x), alpha=0.2)
# shades the lens-shaped regions where sin and cos differ
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.savefig('publication_figure.png', dpi=300)   # 2400×1500 px
```

**Why ML cares:** Figures in reports and papers get judged — a
pixelated chart with chartjunk undermines good analysis. The
rcParams + spine-removal + high-DPI combo is the standard
"publication preset" used in real ML papers.

**Code:**
```python
plt.rcParams['font.family'] = 'serif'
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.fill_between(x, y1, y2, alpha=0.2)
plt.savefig('fig.png', dpi=300)
```

**Common confusion:** `rcParams` are GLOBAL — set them once and they
affect every later plot in the session (including ones you didn't
mean to restyle). And `dpi` only matters on `savefig` — it does
nothing to the on-screen window.

---

## Done with concepts? → Try `easy/p01-line-plot.py`
