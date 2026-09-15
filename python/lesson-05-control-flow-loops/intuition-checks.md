# Lesson 05 — Intuition Checks

## Check 01: For vs While
```python
# Which loop for: "print 1 to 10"?
# A: for
# B: while
```
<details><summary>Answer</summary>
**A (for)** — When you know the count, use `for`. Use `while` for unknown iterations (e.g., "keep asking until valid input").
</details>

## Check 02: Range
```python
for i in range(3, 10, 2):
    print(i)
```
What prints?

<details><summary>Answer</summary>
```
3
5
7
9
```
`range(start, stop, step)` — 3 to 9 (exclusive 10), step 2.
</details>

## Check 03: Break vs Continue
```python
for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)
```
What prints?

<details><summary>Answer</summary>
```
0
1
3
```
`continue` at i=2 skips printing 2. `break` at i=4 exits the loop before printing 4. 3 prints because continue only skips that one iteration.
</details>

## Check 04: Else on Loop
```python
for i in range(5):
    if i == 3:
        break
else:
    print("completed")
```
What prints?

<details><summary>Answer</summary>
Nothing. The `else` on a `for` loop runs only if the loop completes WITHOUT `break`. Since we broke at i=3, the else doesn't run.
</details>

## Check 05: Nested Loop Complexity
```python
for i in range(n):
    for j in range(n):
        print(i, j)
```
How many times does print run (in terms of n)?

<details><summary>Answer</summary>
**n² times.** Nested loops over the same range are O(n²). For n=100, that's 10,000 iterations. Be careful with nested loops on large data.
</details>
