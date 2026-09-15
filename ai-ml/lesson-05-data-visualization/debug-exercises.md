# Lesson 05 — Debug Exercises

## Debug 01 (Easy: Wrong Chart Type
```python
plt.plot(categories, values)  # line chart for categories
```
<details><summary>Answer</summary>
**Bug:** Line chart implies continuous data. Categories are discrete.
**Fix:** `plt.bar(categories, values)`.
</details>

## Debug 02 (Medium: Not Showing Plot
```python
plt.scatter(x, y)
# no plt.show()
```
<details><summary>Answer</summary>
**Bug:** In scripts, plot won't display without `plt.show()`. In Jupyter, it auto-shows.
**Fix:** Add `plt.show()` at the end.
</details>

## Debug 03 (Hard: Overlapping Labels
```python
plt.bar(long_labels, values)
```
<details><summary>Answer</summary>
**Bug:** Long labels overlap and are unreadable.
**Fix:** `plt.xticks(rotation=45)` or use horizontal bar chart.
</details>
