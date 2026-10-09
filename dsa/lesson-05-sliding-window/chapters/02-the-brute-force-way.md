# 02 — The Brute-Force Way (and its real cost)

> 5-minute read. We'll solve a real problem the slow way on purpose —
> you need to feel the pain before the trick lands.

## The problem

**Max sum of `k` consecutive numbers.** Given `nums` and `k`, find the
biggest sum any size-`k` window produces.

```
nums = [2, 1, 5, 1, 3, 2],  k = 3
```

## The honest first answer

Walk the window across. At each stop, add up everything inside:

```python
def max_sum_k_slow(nums, k):
    best = sum(nums[:k])                       # first window
    for left in range(1, len(nums) - k + 1):
        window_sum = sum(nums[left:left + k])  # re-add ALL k items
        best = max(best, window_sum)
    return best

print(max_sum_k_slow([2, 1, 5, 1, 3, 2], 3))   # 9
```

It works. Now watch what it actually does:

```
[2, 1, 5, 1, 3, 2]
 └─k=3─┘              2+1+5 = 8   best=8
    └─k=3─┘           1+5+1 = 7   best=8
       └─k=3─┘        5+1+3 = 9   best=9
          └─k=3─┘     1+3+2 = 6   best=9
```

**Count the work:** 4 windows × 3 additions each = **12 adds**.
In general: `(n − k + 1)` windows × `k` adds ≈ **n·k** operations → O(n·k).

Now the uncomfortable part. Look at windows 1 and 2:

```
window 1:  [2, 1, 5]      we added 2 + 1 + 5
window 2:  [1, 5, 1]      we added 1 + 5 + 1   ← wait, we ALREADY added 1+5
```

Neighboring windows share `k − 1` elements — here, 2 of the 3. We re-add
them anyway. That's the waste: **only one element is actually new** at
each step, yet we re-sum all k.

## Why it exists (why learn the slow way?)

Because it's the honest baseline. Every optimization in this course is
"the same answer with less work," and you can only see the saving if you
priced the original. Also: interviewers love "what's wrong with the naive
version?" — now you have a concrete answer.

## Where it's used

Honestly — nowhere, once n gets big. At n = 1,000 and k = 500, that's
~501 windows × ~500 adds ≈ **250,000 operations**. It's fine for a
whiteboard sketch; it times out on real input.

## Common mistake

`sum(nums[left:left+k])` looks innocent — one line, no visible inner loop.
But `sum` over k items **is** a hidden k-step loop, and the slice copies
k items on top of that. The code reads like O(n) and runs like O(n·k).

## Your turn

`nums` has 1,000 elements, `k = 500`. Roughly how many additions does the
brute-force version do? (Say the formula, then the number.)

<details><summary>Answer</summary>
Windows: n − k + 1 = 1000 − 500 + 1 = 501. Each needs ~500 adds.
Total ≈ 501 × 500 ≈ **250,000 additions**. Keep this number — chapter 03
demolishes it.
</details>

---

**← Prev** [01 — What is a window?](01-what-is-a-window.md) ·
**Next →** [03 — The slide](03-the-slide.md)
