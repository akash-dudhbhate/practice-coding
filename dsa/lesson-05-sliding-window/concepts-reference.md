# Lesson 05 — Concepts Explained (Sliding Window)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## What a "Window" Is

**What:** A window is a contiguous chunk of an array or string — everything between a `left` index and a `right` index, inclusive. "Sliding" the window means moving `left` and `right` forward through the data while keeping track of *what's inside the chunk*.

```python
nums = [2, 1, 5, 1, 3, 2]
#         ^^^^^^^^         window = nums[1..3] = [1, 5, 1]
# indices: left=1, right=3
```

**Why it exists:** An enormous number of problems ask "find the best *contiguous* chunk" — the subarray of size `k` with the biggest sum, the longest substring with no repeats, the smallest subarray whose sum hits a target. A window is the tool that examines every contiguous chunk without re-examining the same elements over and over.

**Where it's used:** Subarray/substring optimization ("longest/shortest/max/min chunk satisfying X"), network packet analysis over time windows, rolling averages in metrics dashboards, "best k consecutive days" problems, DNA sequence scanning.

**What goes wrong without it:**
- The naive approach enumerates every `(start, end)` pair — O(n²) windows, each scanned again → O(n³) total if you re-sum from scratch. At n = 10⁵ that's 10¹⁵ operations. Dead on arrival.
- People reach for "try all substrings" because it's easy to write, then can't explain why it times out on the large test case.

---

## Fixed-Size vs Variable-Size Windows — the two shapes

**What:** There are exactly two shapes, and recognizing which one you're looking at is half the problem.

- **Fixed-size:** the window length is given (e.g., `k = 3`). It never changes. You slide it one step at a time: add the new element on the right, remove the old element on the left.
- **Variable-size:** the window length is *unknown* — you're asked for the longest/shortest window satisfying some condition. `right` grows the window; `left` shrinks it when the window becomes invalid.

```python
# FIXED — size k never changes
[2, 1, 5, 1, 3, 2], k = 3
[2 1 5]            sum = 8
   [1 5 1]         sum = 7   (drop 2, add 1)
      [5 1 3]      sum = 9   (drop 1, add 3)
         [1 3 2]   sum = 6   (drop 5, add 2)

# VARIABLE — grows and shrinks
"abcabcbb" looking for longest no-repeat window
[a] [ab] [abc] [bca] [cab] [abc] [bc] [b]   window breathes
```

**Why it exists:** Fixed windows are mechanical — the size is a gift, so the only question is "how do I update the window's state in O(1) when I slide?" Variable windows need a loop invariant: "while the window is invalid, shrink it." The two shapes share the idea (one element enters/exits at a time) but the control flow differs.

**Where it's used:** Fixed: rolling averages, k-size max/min, k-size counts. Variable: longest substring problems, minimum-size subarray, "at most K distinct" problems — basically every medium/hard sliding window question in interviews.

**What goes wrong without it:**
- Treating a variable problem like a fixed one: people write `for right` and never move `left`, so the window just grows to the whole array and the answer is garbage.
- Treating a fixed problem like a variable one: writing a `while` shrink when a simple "if right - left + 1 == k, record and slide" was all you needed — works, but harder to get right.

**Worked example (fixed window, real numbers):**

`nums = [2, 1, 5, 1, 3, 2]`, `k = 3`, find the maximum window sum.

```
window [2,1,5] → sum 8   best = 8
window [1,5,1] → sum 7   best = 8    (8 - 2 + 1 = 7: subtract leaving, add entering)
window [5,1,3] → sum 9   best = 9    (7 - 1 + 3 = 9)
window [1,3,2] → sum 6   best = 9    (9 - 5 + 2 = 6)
Answer: 9
```

Each slide is 2 operations (subtract out, add in) instead of re-summing 3 elements.

```python
def max_sum_k(nums, k):
    window_sum = sum(nums[:k])      # build the first window once
    best = window_sum
    for right in range(k, len(nums)):
        window_sum += nums[right]           # new element enters
        window_sum -= nums[right - k]       # oldest element leaves
        best = max(best, window_sum)
    return best
```

Expected output for `max_sum_k([2, 1, 5, 1, 3, 2], 3)`: **9**

**Worked example (variable window, real numbers):**

`s = "abcabcbb"` — longest substring with all unique characters. We expand `right` and record each character's last-seen index; when a repeat enters, we jump `left` past the previous occurrence.

```
right=0 'a': window "a"      len 1   best=1
right=1 'b': window "ab"     len 2   best=2
right=2 'c': window "abc"    len 3   best=3
right=3 'a': 'a' seen at 0 → left jumps to 1. window "bca"  len 3
right=4 'b': 'b' seen at 1 → left jumps to 2. window "cab"  len 3
right=5 'c': 'c' seen at 2 → left jumps to 3. window "abc"  len 3
right=6 'b': 'b' seen at 4 → left jumps to 5. window "cb"   len 2
right=7 'b': 'b' seen at 6 → left jumps to 7. window "b"    len 1
Answer: 3
```

---

## The Expand/Shrink Loop

**What:** The universal skeleton of every variable-size window problem:

```python
left = 0
for right in range(n):              # EXPAND: nums[right] enters
    add nums[right] to window state
    while window_is_invalid:        # SHRINK: window broke the rule
        remove nums[left] from window state
        left += 1
    record answer using (right - left + 1)
```

`right` only ever moves forward. `left` only ever moves forward. The `while` guarantees: **after shrinking, the window is always valid again.**

**Why it exists:** This loop is the whole algorithm. "Expand right unconditionally; shrink left until valid" visits every *maximal* valid window exactly once — so you never miss the answer, and you never redo work.

**Where it's used:** Every variable-size problem in this lesson: longest substring without repeats, min-size subarray sum, max consecutive ones with k flips, minimum window substring, fruit into baskets.

**What goes wrong without it:**
- Using `if` instead of `while` for the shrink: `if invalid: left += 1` shrinks only ONE step — the window can still be invalid after it. With a `while`, you shrink until the invariant is restored. Classic bug: works on most tests, silently wrong on inputs needing multi-step shrinks.
- Recording the answer *inside* the shrink loop (records invalid windows) or forgetting it after shrink (misses the valid one).
- Shrinking when the window is merely *suboptimal* rather than *invalid* — e.g., in "minimum-size subarray with sum ≥ target", the window is invalid when `sum < target`, so you record answers only while `sum >= target` and shrink to minimize. Getting the condition backwards is the #1 logic error.

**Worked example — min-size subarray with sum ≥ 7, nums = [2,3,1,2,4,3]:**

Here the rule is inverted: we want the SMALLEST valid window, so we record the answer while shrinking.

```
right=0 sum=2  (<7, expand)
right=1 sum=5  (<7)
right=2 sum=6  (<7)
right=3 sum=8  (≥7! record len=4) → shrink: drop 2 → sum=6, left=1 (now <7, stop)
right=4 sum=10 (≥7! record len=4) → drop 3 → sum=7  len=3 record! → drop 1 → sum=6
right=5 sum=9  (≥7! record len=3) → drop 2 → sum=7  len=2 record! → drop 4 → sum=3
Answer: 2  (the subarray [4,3])
```

```python
def min_subarray_len(target, nums):
    left, total, best = 0, 0, float("inf")
    for right in range(len(nums)):
        total += nums[right]                # expand
        while total >= target:              # window is valid → squeeze it
            best = min(best, right - left + 1)
            total -= nums[left]
            left += 1
    return 0 if best == float("inf") else best
```

Expected output for `min_subarray_len(7, [2,3,1,2,4,3])`: **2**

Notice the two shapes of `while`:
- "Longest window that stays valid" → shrink *while invalid*, record *after* the loop (window is guaranteed valid).
- "Shortest window that stays valid" → record *while valid* inside the loop, shrink to squeeze.

---

## Window State Bookkeeping

**What:** The window isn't just two indices — it's *data about those indices*. Depending on the problem, the state is:

| State | Used for | Update on enter / leave |
|-------|----------|------------------------|
| running `sum` | sum/average/threshold problems | `+= x` / `-= x` |
| `dict`/`Counter` of counts | substring problems (distinct chars, required chars) | `count[c] += 1` / `count[c] -= 1`, delete at 0 |
| `set` | simple duplicate detection | `add` / `remove` |
| window `max`/`min` | extremes inside the window | needs a deque (lesson 06!) or re-scan |

**Why it exists:** The O(1) update is the entire point. If you recomputed `sum(window)` or `len(set(window))` from scratch every slide, you'd be back to O(n·k) — the brute force you were trying to escape.

**Where it's used:**
- `sum` state → all three easy problems (max k-sum, averages, count windows ≥ target).
- `count dict` → longest-no-repeat, k-distinct, fruit baskets (track "how many distinct keys have nonzero count").
- `count dict + formed counter` → minimum window substring (track "how many required chars are fully satisfied").

**What goes wrong without it:**
- Recomputing `sum(nums[left:right+1])` each step → O(n·k), times out on n = 10⁵.
- Forgetting to delete zero-counts from the dict: `count[c] -= 1` leaving `count[c] == 0` means `len(count)` overcounts distinct chars → window looks more crowded than it is.
- For "number of satisfied requirements," incrementing a `formed` counter wrongly (incrementing every time you see a needed char instead of only when the count *becomes* exactly the required count).

**Worked example — bookkeeping for "at most 2 distinct" on `"eceba"`:**

```
right=0 'e': count={e:1}        distinct=1 ≤2  len=1
right=1 'c': count={e:1,c:1}    distinct=2     len=2
right=2 'e': count={e:2,c:1}    distinct=2     len=3  best=3
right=3 'b': count={e:2,c:1,b:1} distinct=3 >2 → shrink:
             drop 'e' → e:1, still 3 distinct → drop 'e' → e:0, delete → {c:1,b:1} 2 distinct
             left=3, len=1
right=4 'a': {c:1,b:1,a:1} distinct=3 → shrink: drop 'b' → {c:1,a:1} left=4 len=1
Answer: 3
```

The `delete at zero` step is what keeps `len(count)` truthful.

```python
def length_of_longest_k_distinct(s, k):
    left, best, count = 0, 0, {}
    for right, c in enumerate(s):
        count[c] = count.get(c, 0) + 1      # enter
        while len(count) > k:               # too many distinct → shrink
            d = s[left]
            count[d] -= 1
            if count[d] == 0:
                del count[d]                # keep len(count) honest
            left += 1
        best = max(best, right - left + 1)
    return best
```

Expected output for `length_of_longest_k_distinct("eceba", 2)`: **3**

---

## Why It's O(n), Not O(n²)

**What:** The sliding window looks like a nested loop — a `while` inside a `for` — but it's linear. The reason: **`left` and `right` each move forward only, and each moves at most n times total.**

**Why it exists:** Nested-loop intuition says `for × while = O(n²)`. That intuition fails here because the inner `while` doesn't restart — `left` never resets to 0 or steps backward. Work is measured by *total pointer movement*, not iterations of the outer loop.

- `right` visits each index once → at most `n` moves.
- `left` visits each index once → at most `n` moves.
- Each move does O(1) bookkeeping (add/subtract/dict update).
- Total: ≤ 2n moves × O(1) = **O(n)**.

**Where it's used:** This "two pointers that never go back" argument is called *amortized analysis* — the same reason `list.append` is O(1) amortized and two-stack queues (lesson 06 hard) are O(1) amortized.

**What goes wrong without it:**
- Adding an operation inside the loops that ISN'T O(1) — e.g., `sum(window)`, `window.count(x)`, slicing `s[left:right]` — and silently turning it back into O(n·k). The pointer argument only protects O(1) work per step.
- Resetting `left = right` on some condition and then ALSO scanning backward — breaks the "each pointer moves once" invariant.
- Copying the window for output (`"".join(...)`, `s[left:right+1]`) inside the loop → that's O(window size) each step. In min-window-substring, you copy **only when you find a better answer**, and even then it's fine because string copy is the output, not the scan.

**Counted example — the same input, both ways:**

`nums` has 1,000 elements, `k = 500`:

- Brute force: ~501 windows × ~500 adds each = **~250,000 operations**.
- Sliding: 1 build (500 adds) + 500 slides × 2 ops = **~1,500 operations**.

That's a ~170× reduction at n=1,000 — and the gap *grows* with n, because brute force is O(n·k) while sliding is O(n).

**The amortized proof in one picture:**

```
array index:   0  1  2  3  4  5  6  7
right visits:  ✓  ✓  ✓  ✓  ✓  ✓  ✓  ✓   each index enters ONCE
left  visits:  ✓  ✓  ✓  ✓  ✓  ✓  ✓  ✓   each index leaves ONCE
```

Total work ∝ 2n. Every sliding-window problem in this lesson rides on this single fact.

---

## The Recipe — recognize it in 10 seconds

Ask three questions:

1. **"Contiguous subarray/substring?"** If yes, sliding window is a candidate. (Non-contiguous → probably hashing, sorting, or DP.)
2. **Fixed size given (k)?** → fixed window: build first, then slide with add/subtract.
3. **"Longest/shortest satisfying condition?"** → variable window: `for right`, `while invalid: shrink left`, record answer at the right moment (after shrink for longest, during shrink for shortest).

And always say the complexity out loud: **O(n) time** because each element enters and exits once; **O(k) or O(1) space** for the bookkeeping structure.

---

## The Pitfall Gallery — five ways windows go wrong

These five bugs account for nearly every sliding-window failure. Check them in order when something's off.

**1. `if` where `while` belongs.**
```python
# WRONG — shrinks once, window may still be invalid
if len(count) > k:
    left += 1
# CORRECT — shrink until the invariant holds again
while len(count) > k:
    left += 1
```

**2. Recording at the wrong moment.**
- Longest-valid: record AFTER the shrink loop (window is guaranteed valid).
- Shortest-valid: record INSIDE the while loop BEFORE shrinking (valid only until you remove).
- Fixed window: record each slide, once `right >= k - 1`.

**3. `left` moving backward (stale indices).**
```python
if c in last and last[c] >= left:   # the >= guard is load-bearing
    left = last[c] + 1
```
Without the guard, `"abba"` breaks: the old `'a'` at index 0 drags `left` back and re-admits a duplicate.

**4. Zombie keys in the count dict.**
`count[c] -= 1` leaving `0` means `len(count)` overstates distinct items → shrink loop behaves as if the window is fuller than it is. Always `del` at zero — or use `sum(v > 0 for v in count.values())` (slower but safe).

**5. Re-deriving state instead of updating it.**
`sum(nums[left:right+1])`, `set(s[left:right])`, `max(window)` inside the slide — each is O(window size), converting your O(n) algorithm into O(n·k). The whole trick is that state changes by exactly one element per pointer move.

**Edge cases to always test:** empty input, `k > len` (fixed windows → `[]`/`0`), `k == 0` (k-distinct → `0`), all-identical elements, all-negative numbers (never init `best = 0` for max problems), and impossible targets (return `0`/`""`, don't crash).
