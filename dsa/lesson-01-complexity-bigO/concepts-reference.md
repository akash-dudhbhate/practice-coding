# Lesson 01 — Concepts Explained (Time/Space Complexity & Big-O)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Time Complexity (counting work, not seconds)

**What:** Time complexity is a count of the *operations* your code performs as the input size `n` grows — additions, comparisons, assignments. It is NOT a count of seconds.

**Why it exists:** Seconds lie. The same code runs at different speeds on a laptop vs a phone vs a 10-year-old server. But the *number of operations* is the same on every machine. So instead of asking "how many seconds?", we ask "how many steps?"

**Where it's used:** Comparing two algorithms before you write them, predicting whether code will survive a 10-million-row input, interview discussions ("what's the runtime?"), deciding whether a naive solution is good enough.

**What goes wrong without it:**
- Code that finishes instantly on 10 items takes hours on 10 million — and you only find out in production.
- You can't compare algorithms fairly: "it ran in 2 seconds on my laptop" is meaningless.
- You waste time optimizing a fast part of the program while the real bottleneck sits untouched.

**Worked example (real numbers):**

```python
def print_first(nums):      # runs the same way for any n
    print(nums[0])          # 1 operation — always

def print_all(nums):        # depends on n
    for x in nums:
        print(x)            # n operations — one per element
```

- `n = 100` → `print_first` does 1 op, `print_all` does 100 ops.
- `n = 1,000,000` → `print_first` still does 1 op, `print_all` does 1,000,000 ops.

The first function's work stays flat; the second grows *with* the input.

---

## Big-O Notation (the shape of growth)

**What:** Big-O is a shorthand that describes the *shape* of a function's growth as `n` gets big. It keeps only the fastest-growing part and throws away the rest. `O(n)` means "work grows in a straight line with n". `O(n²)` means "work grows with n squared".

**Why it exists:** Exact op counts get messy fast — `3n² + 12n + 7` ops is precise but unhelpful. Big-O compresses that to `O(n²)`, which is what matters when n is large: the n² term dominates everything else.

**Where it's used:** Every algorithm textbook, every interview, every library doc ("dict lookup is O(1) average"), every code review that asks "will this scale?"

**What goes wrong without it:**
- You can't talk about performance precisely — "it's kinda slow on big data" isn't actionable.
- You may pick an `O(2ⁿ)` algorithm where an `O(n)` one exists and never notice until it's too late.
- You can't tell whether an optimization actually changed the growth rate or just shaved a constant.

**The common classes, smallest growth to largest:**

| Big-O | Name | Ops at n=10 | Ops at n=1000 | Feels like |
|-------|------|-------------|---------------|------------|
| O(1) | constant | 1 | 1 | instant, always |
| O(log n) | logarithmic | ~4 | ~10 | halving each step |
| O(n) | linear | 10 | 1,000 | one pass |
| O(n log n) | linearithmic | ~40 | ~10,000 | good sorting |
| O(n²) | quadratic | 100 | 1,000,000 | all pairs |
| O(2ⁿ) | exponential | 1,024 | more than atoms on Earth | try everything |

**Code for each class:**

```python
def constant(nums):            # O(1)
    return nums[0]

def logarithmic(nums, target): # O(log n) — binary search halves the range
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

def linear(nums):              # O(n) — one visit per element
    total = 0
    for x in nums:
        total += x
    return total

def quadratic(nums):           # O(n²) — every element pairs with every element
    count = 0
    for x in nums:             # n times
        for y in nums:         # n times
            count += 1         # n × n total
    return count
```

**Expected output if you count the quadratic one:**

```python
for i in range(3):
    for j in range(3):
        print(i, j)
# prints 9 lines: (0,0)(0,1)(0,2)(1,0)(1,1)(1,2)(2,0)(2,1)(2,2) — 3² = 9 ops
```

---

## Loop Rules (how to read complexity off code)

**What:** Simple rules for counting:
- Code that runs a fixed number of times → `O(1)`.
- A loop over `n` items → `O(n)`.
- Two nested loops each over `n` → `O(n × n) = O(n²)`.
- Sequential loops add: `O(n) + O(n) = O(n)` (still linear).
- A loop that halves the data each step → `O(log n)`.

**Why it exists:** You rarely time code in practice — you *read* it and estimate. These rules let you look at any loop and say its Big-O in seconds.

**Where it's used:** Analyzing your own code before running it, code review, whiteboard interviews.

**What goes wrong without it:**
- Nested loops sneaking in: `x in list` inside a `for` loop is a *hidden* inner loop — `in` scans the whole list. The code looks like one loop but runs O(n²).
- Confusing "two loops" with "n²": two loops *side by side* are `O(n) + O(n) = O(n)`; two loops *nested* are `O(n²)`.

**Worked example:**

```python
def mystery(nums):       # n = len(nums)
    total = 0
    for x in nums:       # outer loop: n iterations
        total += x
    for x in nums:       # second loop: n more iterations
        total += x
    return total         # 2n ops → O(n) — sequential, not nested

def mystery2(nums):
    count = 0
    for x in nums:       # outer: n
        for y in nums:   # inner: n per outer
            count += 1
    return count         # n×n → O(n²)
```

`mystery(100 elements)` does ~200 ops. `mystery2(100 elements)` does ~10,000 ops.

---

## Worst, Average, Best Case

**What:** The same algorithm can do different amounts of work depending on the input. Best case = luckiest input. Worst case = unluckiest. Average = typical. Unless stated otherwise, Big-O usually means *worst case*.

**Why it exists:** A single number can't capture "it depends". Linear search finds the target in 1 step if it's first, `n` steps if it's last or missing. Saying just "O(n)" hides that difference.

**Where it's used:** Linear search (best O(1), worst O(n)), quicksort (average O(n log n), worst O(n²)), hash lookups (average O(1), worst O(n)).

**What goes wrong without it:**
- You claim "it's fast" because it was fast on your test input — but your test input was the lucky case.
- You get burned by worst-case inputs: sorted data into naive quicksort, crafted hash collisions (a real DoS attack).

**Worked example — linear search:**

```python
def find(nums, target):
    for i, x in enumerate(nums):   # counts as 1 comparison per element
        if x == target:
            return i               # found — early exit!
    return -1                      # checked everything
```

- `find([5, 9, 2, 7], 5)` → best case: **1 comparison** (first element).
- `find([5, 9, 2, 7], 7)` → worst-ish: **4 comparisons** (last element).
- `find([5, 9, 2, 7], 99)` → worst case: **4 comparisons** (never found).

Best = O(1), worst = O(n). When someone asks "what's the complexity?", you answer the worst case: **O(n)**.

---

## Dropping Constants and Lower-Order Terms

**What:** Two simplification rules:
1. Drop constants: `O(2n)` → `O(n)`. `O(500)` → `O(1)`.
2. Keep only the biggest term: `O(n² + n)` → `O(n²)`. `O(n + log n)` → `O(n)`.

**Why it exists:** For large `n`, the biggest term swallows everything. When `n = 1,000,000`: `n²` is a trillion, `n` is a million — the n term is a rounding error. Constants matter even less: `2n` vs `n` is just a 2× speedup, and hardware differences are bigger than that.

**Where it's used:** Simplifying analysis — nobody says "O(3n² + 4n + 2)", they say "O(n²)".

**What goes wrong without it:**
- Over-precision: arguing whether code is O(2n) or O(3n) when both scale identically.
- BUT the reverse trap exists too: Big-O ignores constants that *do* matter at your scale. An O(n) algorithm with a huge constant can lose to O(n log n) for small n. Big-O is about *growth*, not your exact n.

**Worked example:**

```python
def two_passes(nums):
    for x in nums:    # n ops
        print(x)
    for x in nums:    # n ops
        print(x * 2)
# Total: 2n ops → drop the 2 → O(n)

def mixed(nums):
    for x in nums:           # n
        print(x)
    for x in nums:           # n²
        for y in nums:
            print(x + y)
# Total: n + n² → drop the n → O(n²)
```

At `n = 100`: exact ops = 100 + 10,000 = 10,100. The n² part is 99% of the work — dropping the n loses almost nothing.

---

## Space Complexity & Auxiliary Space

**What:** Time complexity counts *steps*; space complexity counts *extra memory*. "Auxiliary space" is the extra memory beyond the input itself — new lists, dicts, counters you create.

**Why it exists:** Memory is finite too. An algorithm can be fast but use so much RAM it crashes. Interviewers always ask "and the space?" after "and the time?"

**Where it's used:** Deciding between algorithms (sort in place O(1) space vs copy O(n) space), embedded/big-data constraints, trading memory for speed (caching, hash sets).

**What goes wrong without it:**
- A "clever" solution that copies the input 5 times blows the memory limit on large data.
- Recursion eats stack space: `fib(10000)` without care can hit Python's recursion limit — that's a space complexity problem.
- Accidentally O(n) space when O(1) was required: `result = nums[:]` inside a loop.

**Worked example:**

```python
def sum_list(nums):            # O(1) auxiliary space
    total = 0                  # one variable, regardless of n
    for x in nums:
        total += x
    return total

def doubled(nums):             # O(n) auxiliary space
    out = []                   # new list grows with n
    for x in nums:
        out.append(x * 2)
    return out
```

`n = 1,000,000`: `sum_list` uses ~1 variable's worth of extra memory. `doubled` uses ~8 MB for the new list (a million pointers at 8 bytes each).

---

## The Hidden Loop Trap (`in`, `count`, `index` on lists)

**What:** Some single *looking* operations are secretly loops. `x in my_list` scans the list. `my_list.count(x)` scans it. `my_list.index(x)` scans it. Inside a `for` loop, each makes the code O(n²).

**Why it exists:** Python makes these operations one line for readability — the scan still happens, it's just invisible. Sets and dicts answer `in` in O(1) average because they hash instead of scan.

**Where it's used:** This is THE most common way beginners accidentally write O(n²) code: "check membership inside a loop".

**What goes wrong without it:**

```python
def dedup_slow(nums):          # looks O(n) — is O(n²)
    result = []
    for x in nums:             # n iterations
        if x not in result:    # hidden scan: up to n ops each time!
            result.append(x)
    return result

def dedup_fast(nums):          # truly O(n)
    seen = set()
    result = []
    for x in nums:             # n iterations
        if x not in seen:      # O(1) average — hash lookup
            seen.add(x)
            result.append(x)
    return result
```

At `n = 10,000`: `dedup_slow` does up to ~50 million comparisons (seconds). `dedup_fast` does ~10,000 lookups (milliseconds). Same output — 1000× difference in work.

---

## Recursion and Complexity

**What:** A recursive function's cost = (cost per call) × (number of calls). If each call spawns *two* more calls (like naive Fibonacci), the call count explodes exponentially.

**Why it exists:** Recursion hides its loop inside the call stack. You can't count iterations by looking at a `for` — you count *calls*.

**Where it's used:** Fibonacci, tree/graph traversal, divide-and-conquer, backtracking.

**What goes wrong without it:**

```python
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)   # two calls per call → O(2ⁿ)
```

`fib(5)` makes 15 total calls. `fib(10)` makes 177. `fib(30)` makes ~2.7 million. `fib(50)` is roughly **a trillion calls** — you will not finish this lesson waiting for it.

Each level roughly doubles the calls: 1 → 2 → 4 → 8 → ... which is where the `2ⁿ` comes from.

---

## Amortized Analysis (the big picture)

**What:** Some operations are *usually* cheap but *occasionally* expensive — so we average the cost over many operations. `list.append` is the famous example: it's **O(1) amortized**.

**Why it exists:** A Python list keeps a block of memory. When it's full, Python allocates a bigger block (~roughly doubling) and copies everything — that one append costs O(n). But doublings are rare: most appends just drop a value into an empty slot. Spread over n appends, the copies average out to a tiny constant per append.

**Where it's used:** `list.append`, dict/set inserts (occasional rehash), dynamic arrays everywhere.

**What goes wrong without it:**
- Thinking `append` is literally O(1) always → confusion when profiling shows a spike.
- Thinking `append` is O(n) → you'd wrongly avoid lists and pre-allocate everything.

**Worked example — appends vs copies:**

```
Capacity:   4   4   4   4 | 8   8   8   8 | 16 ...
Appends:    1   2   3   4 | 5   6   7   8 | 9  ...
Copy cost:  0   0   0   4 | 0   0   0   8 | 0  ... (copy only when full)
```

8 appends → total copy work = 4 + 8 = 12 extra moves. Averaged: 12/8 = 1.5 extra ops per append. Still effectively constant.

---

## Putting It Together — the analysis recipe

When someone hands you code and asks "what's the complexity?":

1. Find `n` — what grows? (usually input size)
2. Count the *dominant* work — innermost loop, hidden scans (`in`, `count`, `index`), recursive calls.
3. Drop constants and lower terms.
4. Say worst case unless told otherwise.
5. State space complexity too — what new memory does it allocate?

```python
def analyze_me(nums, k):
    seen = set()                    # O(1) setup
    for x in nums:                  # n iterations
        if k - x in seen:           # O(1) hash lookup, not a scan
            return True
        seen.add(x)                 # O(1) amortized
    return False
```

- Time: n × O(1) = **O(n)**.
- Space: the `seen` set can hold up to n elements → **O(n)**.
- Worst case: k never formed → scans everything → still O(n).

That's the whole skill — and every DSA lesson after this one will ask you to say it out loud.
