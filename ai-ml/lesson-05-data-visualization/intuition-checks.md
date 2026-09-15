# Lesson 05 — Intuition Checks

## Check 01: Chart selection
When should you use: bar, line, scatter, histogram?
<details><summary>Answer</summary>
- Bar — categorical comparisons
- Line — trends over time
- Scatter — relationship between two variables
- Histogram — distribution of one variable
</details>

## Check 02: matplotlib vs seaborn
<details><summary>Answer</summary>
matplotlib — low-level, full control, verbose. seaborn — high-level, statistical plots, prettier defaults, built on matplotlib. Use seaborn for quick EDA, matplotlib for custom plots.
</details>

## Check 03: Figure vs Axes
```python
fig, ax = plt.subplots()
ax.plot(x, y)
```
<details><summary>Answer</summary>
Figure = container (the whole image). Axes = one plot area. Multiple axes per figure for subplots. Object-oriented interface is more flexible than pyplot.
</details>

## Check 04: Color in scatter
```python
plt.scatter(x, y, c=categories, cmap="viridis")
```
<details><summary>Answer</summary>
`c` colors points by values. `cmap` chooses color scheme. Useful for showing a third dimension.
</details>

## Check 05: Subplots
```python
fig, axes = plt.subplots(2, 2)
axes[0, 0].plot(...)
axes[0, 1].bar(...)
```
<details><summary>Answer</summary>
Creates 2x2 grid of plots. Access each by index. Good for comparing multiple views.
</details>
