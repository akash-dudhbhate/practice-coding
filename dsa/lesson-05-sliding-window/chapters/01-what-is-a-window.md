# 01 — What is a "Window"?

> 4-minute read. One idea only.

## The idea, plain words

A **window** is a chunk of an array — items sitting **next to each other**,
marked by two fingers: a `left` index and a `right` index.

Put your two index fingers on a row of numbers. Everything between your
fingers *is* the window. Slide both fingers one step right — the window
"slides." That's the entire metaphor; everything else is bookkeeping.

```python
nums = [2, 1, 5, 1, 3, 2]
left, right = 1, 3          # the window is nums[1..3] = [1, 5, 1]
```

Picture it:

```
[2, 1, 5, 1, 3, 2]
    └─window─┘        left=1, right=3 → the chunk [1, 5, 1]
```

Key point: the window is **not a copy** of the numbers. It's just two small
numbers (`left`, `right`) that *point at* the chunk. Sliding = adding 1 to
each. No data moves at all.

## Try it — walk every size-3 window

```python
nums = [2, 1, 5, 1, 3, 2]
k = 3
for left in range(len(nums) - k + 1):
    right = left + k - 1
    print(left, right, nums[left:right + 1])
```

Output:

```
0 2 [2, 1, 5]
1 3 [1, 5, 1]
2 4 [5, 1, 3]
3 5 [1, 3, 2]
```

Same array — the window just walked across it, one step at a time.
How many size-`k` windows does an n-item array have? `n - k + 1`.
Here: 6 − 3 + 1 = **4**.

## Why it exists

A huge number of problems ask for the best **contiguous** chunk: the 3 days
with the most sales, the longest stretch of text with no repeated letter,
the shortest subarray that reaches a target. "Contiguous chunk" = window.
Giving it a name turns a vague idea into two variables you can move.

## Where it's used

Rolling averages on dashboards, "best k consecutive days" questions,
longest/shortest substring puzzles, network traffic per time window,
DNA sequence scanning.

## Common mistake

Treating `nums[left:right+1]` — a slice, which **copies** — as if it were
the window itself. It's not; it's a snapshot you pay ~k work to build.
The window is only the two indices. Chapter 03 shows why that difference
is worth real money.

## Your turn

For `nums = [4, 8, 2, 9, 1]` with `k = 2`, list every window as a
`(left, right)` pair.

<details><summary>Answer</summary>
(0,1), (1,2), (2,3), (3,4) — four windows, since n − k + 1 = 5 − 2 + 1 = 4.
</details>

---

**Next →** [02 — The brute-force way](02-the-brute-force-way.md)
