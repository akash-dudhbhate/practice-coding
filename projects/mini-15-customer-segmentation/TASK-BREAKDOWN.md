# Customer Segmentation (Unsupervised ML) — Task Breakdown

> **Step-by-step implementation guide.** Follow each step in order.

---

## File Structure

```
mini-15-customer-segmentation/
├── data_loader.py, segmentation.py, visualize.py, main.py
└── README.md
```

---

## Implementation Steps

### Step 1: Load Data

Mall customers or e-commerce data. Features: age, income, spending score.

**Checkpoint:** Step 1 is complete when the described functionality works.

### Step 2: EDA

Distributions, correlations, pair plots. Understand the data.

**Checkpoint:** Step 2 is complete when the described functionality works.

### Step 3: Feature Scaling

StandardScaler for KMeans (distance-based). Fit and transform.

**Checkpoint:** Step 3 is complete when the described functionality works.

### Step 4: Find Optimal K

Elbow method (inertia vs K). Silhouette score for each K. Plot both.

**Checkpoint:** Step 4 is complete when the described functionality works.

### Step 5: Train KMeans

Fit KMeans with optimal K. Get cluster labels. Cluster centers.

**Checkpoint:** Step 5 is complete when the described functionality works.

### Step 6: Analyze Clusters

Mean values per cluster. Name clusters (e.g., 'High Value', 'Budget').

**Checkpoint:** Step 6 is complete when the described functionality works.

### Step 7: Visualize

Scatter plot with cluster colors. 3D plot if 3+ features. PCA for visualization.

**Checkpoint:** Step 7 is complete when the described functionality works.

### Step 8: DBSCAN Comparison

Train DBSCAN. Compare clusters. When is DBSCAN better?

**Checkpoint:** Step 8 is complete when the described functionality works.

### Step 9: Export Results

Save customer data with cluster labels. Generate segment summary report.

**Checkpoint:** Step 9 is complete when the described functionality works.

---

## Final Checklist

- [ ] Data loaded and explored
- [ ] Feature scaling
- [ ] Elbow method for optimal K
- [ ] Silhouette score
- [ ] KMeans trained
- [ ] Clusters analyzed and named
- [ ] Visualization (scatter, 3D or PCA)
- [ ] DBSCAN comparison
- [ ] Results exported with labels

---

## Common Pitfalls

1. **Skipping steps** — each step builds on the previous. Don't jump ahead.
2. **Not testing incrementally** — test after each step, not just at the end.
3. **Ignoring error states** — handle empty states, loading, and errors from the start.
4. **Not making it responsive** — test on mobile from the beginning, not as an afterthought.
5. **Hardcoding values** — use environment variables for API keys, URLs, and configuration.
