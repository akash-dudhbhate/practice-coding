# Level 03 — Concepts (Detailed Explanations)

> Read each section BEFORE attempting its problem. Each concept explains:
> **What it is** · **Why it exists** · **Where it's used** ·
> **What goes wrong** without it · worked example · code ·
> expected output — here, the expected output is a CHART: what
> the correct image should look like, so you can compare visually.

---

## Easy

### 1. Line Plots — `p01`

**What it is:** A line plot connects (x, y) points — the chart for
"how does y change as x changes?" matplotlib's workflow: build x
with `np.linspace(start, stop, n)`, plot each curve with a `label`,
then `legend()`, `grid()`, `savefig()`, `show()`.

**Why it exists:** A column of 10,000 numbers shows no pattern;
the same data as a curve shows trend, period, and anomalies at a
glance. Line plots exist to make continuous relationships visible.

**Where it's used:** Loss-vs-epoch training curves, learning
curves, ROC curves — every diagnostic chart in later levels is a
line plot.

**What goes wrong without it:** Without `plt.show()` nothing
appears — the script runs "successfully" and you see nothing.
`savefig` AFTER `show()` saves a blank PNG, because `show()`
resets the figure — save first, then show. And without labels/legend,
two curves on one axes are indistinguishable — you can't tell sin
from cos, or train loss from val loss.

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

**Code:**
```python
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x), label='sin(x)')
plt.xlabel('x'); plt.ylabel('y'); plt.title('Trig')
plt.legend(); plt.grid(True)
plt.savefig('trig_plot.png'); plt.show()
```

**Expected output:** A PNG titled "Trig" showing a smooth sine
wave starting at 0, rising to 1, falling through −1, and back —
oscillating between −1 and +1 across x=0..10. Light grid lines,
labeled axes, a legend naming the curve. If a second cosine curve
is plotted it starts at 1 and oscillates out of phase with sin.

---

### 2. Scatter Plots — `p02`

**What it is:** Points instead of lines — `plt.scatter(x, y)`. The
chart for "is there a relationship between two variables?" To color
by category, plot each group separately with a boolean mask and a
`label`, then `legend()`.

**Why it exists:** Relationships between two variables are
invisible in tables. A point cloud shows correlation, clusters,
and outliers instantly — it's the fastest way to SEE whether a
model has anything to learn.

**Where it's used:** Reading the shape of your problem before
modeling: linear trend → regression; separate clouds →
classification; no pattern → these features won't help.
Clustering results (level-07) are always shown this way.

**What goes wrong without it:** Skip the scatter and you can run
regression on data with no relationship — the model "succeeds"
with R² ≈ 0 and you only find out after training. In code:
`c='blue'` (one color) vs `c=array` (color-per-point colormap)
behave totally differently — pass a number array and you get a
rainbow you didn't ask for. For categories, plotting each group
separately with `label` is the simplest path; `~mask` is "not
mask" (the other rows).

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

**Code:**
```python
mask = gender == 'M'
plt.scatter(height[mask], weight[mask], c='blue', label='M')
plt.scatter(height[~mask], weight[~mask], c='red', label='F')
plt.legend(); plt.savefig('scatter_plot.png'); plt.show()
```

**Expected output:** A scatter plot trending up-right — taller
people weigh more. Two overlapping clouds: blue points for M,
red points for F, mixed throughout the same diagonal band
centered around (170, ~102). A legend distinguishes the two
colors. Axes roughly x=140–200 (height), y=90–115 (weight).

---

### 3. Histograms — `p03`

**What it is:** A histogram bins values and counts how many fall in
each bin — the chart for "what's the distribution of ONE variable?"
Add `plt.axvline` for vertical reference lines at the mean/median.

**Why it exists:** You can't see a distribution in a column of
numbers — is it bell-shaped? skewed? two-humped? The histogram
exists to answer that in one glance, which determines what
preprocessing the feature needs.

**Where it's used:** Step one of any data work — a feature skewed
right might need a log transform; a target with two humps might
actually be two populations. Mean≠median on the histogram is the
visual signature of skew.

**What goes wrong without it:** Model a two-humped feature as one
population → the "average" lands in the empty valley between
groups and represents nobody. `bins` is the number of BARS, not
their width: too few hides the shape (all data in 3 bars), too
many shows noise as fake patterns — 20-30 is a reasonable default
for a few hundred points.

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

**Code:**
```python
plt.hist(scores, bins=20, edgecolor='black', alpha=0.7)
plt.axvline(np.mean(scores), color='red', linestyle='--')
plt.axvline(np.median(scores), color='green', linestyle='--')
plt.savefig('histogram.png'); plt.show()
```

**Expected output:** A roughly bell-shaped histogram centered near
75 — tallest bars (~5-point-wide bins) in the 65-85 range, tailing
off toward 0 and 100 with a slight pile-up at 100 from clipping.
Two nearly overlapping dashed vertical lines near x≈75: red
(mean) and green (median) — their near-coincidence confirms a
roughly symmetric distribution.

---

## Medium

### 4. Correlation Heatmap — `p01`

**What it is:** **Correlation** measures how much two variables move
together: +1 = perfectly together, 0 = unrelated, −1 = opposite.
`df.corr()` builds the n×n matrix of all pairs; `sns.heatmap`
draws it as a color-coded grid so patterns jump out.

**Why it exists:** Ten features = 45 pairs of relationships — too
many numbers to scan. The heatmap exists to compress that matrix
into color, so "which features matter" becomes a visual task.

**Where it's used:** Feature selection before training — the
target row tells you which features matter; two features at 0.95
= redundant, one can be dropped. It's the fastest "which columns
matter?" scan there is (level-04 `hard/p03`).

**What goes wrong without it:** Skipping it, you train on
redundant features (two columns carrying the same signal adds
noise, not signal) or miss that your best predictor was hiding in
plain sight. Correlation ≠ causation, and it's NOT slope — 0.9
means "tightly linear," not "y grows 0.9 per x." And without
`annot=True` you're guessing shades of red — the numbers belong
ON the cells.

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

**Code:**
```python
import seaborn as sns
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, fmt='.2f')
plt.savefig('correlation_heatmap.png'); plt.show()
```

**Expected output:** A square 5×5 grid with a colorbar on the
right ranging −1 (blue) to +1 (red). The diagonal glows solid
red (all 1.00). Cells carry printed numbers; the feat_b↔target
cell stands out warm-orange (~0.55) against a mostly pale,
near-zero grid — the matrix is symmetric top-left to
bottom-right.

---

### 5. Subplots — `p02`

**What it is:** `plt.subplots(2, 2)` returns one figure plus a 2×2
GRID of axes objects — each subplot is an independent plot you
address like a matrix: `axes[0,0]` top-left, `axes[1,1]`
bottom-right.

**Why it exists:** One chart per window can't show comparisons —
you'd flip between four windows trying to hold them in your head.
Subplots exist to put the comparison in ONE image.

**Where it's used:** Before/after scaling histograms, train vs
test distributions, multiple model ROC curves, experiment
dashboards — side-by-side IS the analysis.

**What goes wrong without it:** With `plt.plot` you call
`plt.xlabel`; with an axes object it's `ax.set_xlabel` — method
names get `set_` prefixes (`set_title`, `set_xlabel`). Mixing
`plt.` and `ax.` calls puts labels on the WRONG subplot (or on
whichever axes is "current" — usually the last one touched). And
without `tight_layout()`, titles and axis labels overlap into an
unreadable mess.

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

**Code:**
```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes[0, 0].plot(x, np.sin(x)); axes[0, 0].set_title('sin')
plt.tight_layout()              # stop labels overlapping
plt.savefig('dashboard.png'); plt.show()
```

**Expected output:** One PNG containing a 2×2 grid: top-left a
smooth sine wave titled 'sin'; top-right a shapeless cloud of
random dots filling the frame; bottom-left a bell-shaped
histogram centered at 0; bottom-right four ascending bars
A<B<C<D (23 → 78). Titles and tick labels don't overlap.

---

### 6. Box Plots + Swarm Overlay — `p03`

**What it is:** A box plot summarizes each group's distribution in
5 numbers: the box spans Q1→Q3 (middle 50%), the line inside is the
median, whiskers reach ~1.5×IQR, dots beyond are outliers.
`sns.swarmplot` draws every raw point on top — summary AND evidence.

**Why it exists:** Comparing groups by mean alone hides spread,
skew, and outliers. The box plot exists to show the whole
distribution per group in a compact glyph — and the swarm overlay
exists because a clean-looking box can hide that it's drawn from
3 points.

**Where it's used:** Comparing distributions across categories —
does "income" separate churners from non-churners? The box shows
it at a glance; the swarm proves it's not 3 outliers faking the
difference.

**What goes wrong without it:** Without the overlay, a "clean
separation" can be one outlier per group. Misreading it: the box
EDGE is not the mean — it's the quartiles (Q1, median, Q3).
Whiskers are NOT min/max — they're ~1.5×IQR fences, with points
beyond drawn separately as candidate outliers (same 1.5×IQR rule
as level-02 `medium/p02`).

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

**Code:**
```python
sns.boxplot(x='category', y='value', data=df)
sns.swarmplot(x='category', y='value', data=df,
              color='black', alpha=0.4, size=3)
plt.savefig('boxplot.png'); plt.show()
```

**Expected output:** Four vertical box plots side by side labeled
A, B, C, D on the x-axis. Reading heights: D's box sits highest
(centered ~70), then B (~60), C (~55), A (~50). B's box is
tallest (widest spread, std 15); D's is most compact (std 8).
Median lines run through each box; faint black dots (the swarm)
fill each column, showing ~50 raw points each. A few isolated
dots may sit beyond some whiskers — those are the outliers.

---

## Hard

### 7. Groupby + Dashboards — `p01`

**What it is:** `df.groupby('col')['val'].sum()` collapses rows into
per-group aggregates — pandas' version of SQL GROUP BY. Pandas can
plot these directly (`.plot(kind='bar')`), and `.unstack()` pivots
a two-key groupby into a matrix for heatmaps.

**Why it exists:** Raw transaction rows can't answer "which
product sells best WHERE?" — aggregation exists to collapse 90
rows into the 3 totals a human (or a chart) can act on.

**Where it's used:** Every dashboard and report — and the same
"total per group" move is feature engineering in real ML
pipelines (cluster-mean features, segment statistics).

**What goes wrong without it:** `groupby` alone is lazy —
`df.groupby('col')` returns a groupby OBJECT, not data; print it
and you get `<DataFrameGroupBy object>`, not numbers. You must
add an aggregation (`.sum()`, `.mean()`). And feeding a two-level
groupby straight to `sns.heatmap` fails — `.unstack()` is what
turns it into the 2D table the heatmap can eat.

**Worked example:**
```
90 rows of sales: date, revenue ~ N(10000, 2000), product, region

df.groupby('product')['revenue'].sum()
  → A ~3.0M, B ~3.0M, C ~3.0M  (one total per product)

df.groupby(['product','region'])['revenue'].sum().unstack()
  → 3×4 matrix: product rows × region columns
    A/North, A/South, ... — perfect input for sns.heatmap
```

**Code:**
```python
data.groupby('product')['revenue'].sum().plot(
    kind='bar', ax=axes[0, 1])
pivot = data.groupby(['product', 'region'])['revenue'].sum().unstack()
sns.heatmap(pivot, annot=True, ax=axes[1, 1])
```

**Expected output:** Within a multi-panel dashboard: a bar chart
with three product bars (A, B, C) all near the same height (~3.0M
revenue each — random data means no real winner), and a 3×4
heatmap (products × regions) with annotated dollar totals in
each cell, colored by magnitude — no dramatic hotspots since the
data is random.

---

### 8. Animation with FuncAnimation — `p02`

**What it is:** `FuncAnimation` calls YOUR update function once per
frame; each call mutates the plotted artists (e.g.,
`line.set_ydata(...)`) instead of redrawing from scratch. `frames`
= how many times, `interval` = ms between frames, `blit=True` =
redraw only what changed (fast).

**Why it exists:** Iterative processes (gradient descent
converging, clusters forming, waves traveling) can't be shown in
one static image — animation exists to show the PROCESS, not
just the endpoint.

**Where it's used:** Visualizing gradient descent rolling
downhill, K-Means centroids migrating to their clusters, decision
boundaries shifting per epoch — also a sanity check that
iterative code is doing something sensible per step.

**What goes wrong without it:** `line, = plt.plot(...)` — the
trailing comma unpacks the LIST `plot` returns (one Line2D).
Without it, `line` is a list and `set_ydata` throws
`AttributeError`. `update` must RETURN the changed artists when
`blit=True`, or nothing moves — the animation plays but the
frame never changes. And redrawing the whole plot each frame
instead of mutating artists makes the animation crawl.

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

**Code:**
```python
from matplotlib.animation import FuncAnimation
def update(frame):
    line.set_ydata(np.sin(x + frame / 10))
    return line,
anim = FuncAnimation(fig, update, frames=100, interval=50, blit=True)
plt.show()
```

**Expected output:** A live window (not a static PNG) where a
sine wave slides smoothly to the right — the same −1..+1 wave
shape, continuously shifting phase, completing a 5-second loop
and restarting. The wave shape itself never distorts; it just
travels.

---

### 9. Publication-Quality Figures — `p03`

**What it is:** Journal/blog-ready polish: serif fonts via
`rcParams`, removed top/right spines for a clean look,
`fill_between` for shaded regions, `tight_layout` so nothing clips,
and `dpi=300` so the PNG is sharp in print (screen default is ~100).

**Why it exists:** Figures in reports and papers get judged — a
pixelated chart with heavy chartjunk undermines good analysis.
The polish layer exists to make the reader trust (and read) the
data.

**Where it's used:** The rcParams + spine-removal + high-DPI
combo is the standard "publication preset" used in real ML
papers, blog posts, and slide decks.

**What goes wrong without it:** Default `dpi=100` looks fine on
screen but pixelates when printed or projected — the fix is
`dpi=300` on `savefig` (it does nothing to the on-screen window).
`rcParams` are GLOBAL — set them once and they affect every later
plot in the session, including ones you didn't mean to restyle.
And skipping `tight_layout()` clips axis labels off the edge of
the saved PNG.

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

**Code:**
```python
plt.rcParams['font.family'] = 'serif'
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.fill_between(x, y1, y2, alpha=0.2)
plt.savefig('fig.png', dpi=300)
```

**Expected output:** A crisp 2400×1500 px PNG: serif labels, sin
and cos curves crossing each other with the lens-shaped regions
between them lightly shaded (alpha 0.2). Only the left and bottom
axis spines remain — no top/right box frame. The image stays
sharp when zoomed or printed.

---

## Done with concepts? → Try `easy/p01-line-plot.py`
