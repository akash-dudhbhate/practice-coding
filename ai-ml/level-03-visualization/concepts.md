# Level 03 — Concepts Reference

## Easy

### Line Plots
- `plt.plot(x, y, label='name')` — line chart
- `plt.legend()`, `plt.grid(True)`, `plt.savefig('f.png')`

### Scatter Plots
- `plt.scatter(x, y, c=color, alpha=0.6)` — points
- Color by group: plot each subset separately with a label

### Histograms
- `plt.hist(data, bins=20, edgecolor='black')` — distribution
- `plt.axvline(mean, color='red', linestyle='--')` — reference line

## Medium

### Correlation Heatmap
- `df.corr()` → matrix; `sns.heatmap(corr, annot=True, cmap='coolwarm')`
- Diagonal is always 1.0 (self-correlation)

### Subplots
- `fig, axes = plt.subplots(2, 2)` → grid of axes
- `axes[i, j].plot(...)` — each subplot is its own axes

### Box Plots
- `sns.boxplot(x='cat', y='val', data=df)` — distribution per group
- `sns.swarmplot(...)` — raw points on top

## Hard

### Dashboards
- `df.groupby('col')['val'].sum().plot(kind='bar')` — pandas plots
- `.unstack()` pivots groupby output for heatmaps

### Animation
- `FuncAnimation(fig, update, frames=100)` — calls update per frame
- `line.set_ydata(...)` to mutate the plotted data

### Publication Quality
- `rcParams['font.family']='serif'`; `spines['top'].set_visible(False)`
- `savefig(dpi=300)` for print quality
