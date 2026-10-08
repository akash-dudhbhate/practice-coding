# 34 — Optimizing a slow script

> **Interview question:** "You have a Python script that's too slow. Walk me through how you'd make it faster."
> **What the interviewer is really testing:** Whether you *measure before you optimize* — profile first, fix the algorithm second, then I/O, then reach for heavy tools — or whether you jump straight to "rewrite it in Cython" without knowing where the time goes.

## Theory — what it is

**Profiling** means measuring where your program actually spends time, instead of guessing. Guessing is almost always wrong: developers routinely "optimize" code that costs 2% of runtime while the real 80% hotspot sits untouched.

The workflow, in order:

1. **Profile** — `cProfile` (built-in) reports how many times each function was called and how many seconds it consumed. `time.perf_counter()` for quick timing, `timeit` for micro-benchmarks, `line_profiler`/`py-spy` for line-level detail.
2. **Fix the algorithm** — a better big-O beats any micro-optimization. `O(n²)` nested loop → `O(n)` with a dict/set lookup. No amount of Cython rescues a quadratic algorithm on large input.
3. **Fix I/O and calls** — batch DB queries (N+1 → one query), cache repeated work (`functools.lru_cache`), use generators to avoid materializing lists, move work out of loops.
4. **Only then go lower** — vectorize with NumPy (push loops into C), use `multiprocessing` for CPU-bound work, or compile hotspots with Cython/mypyc/Rust extensions.

"Jargon" decoded: **hotspot** = the few lines consuming most runtime. **big-O** = how runtime scales with input size. **vectorize** = replacing a Python loop with a C-level array operation (NumPy).

## Why it was needed

Because intuition fails. Amdahl's law: speeding up a section that takes 10% of runtime can *at most* make the program 11% faster — even if you make that section instant. Without profiling you don't know which section is the 90%.

Also because "Python is slow" is usually the wrong diagnosis. Most real scripts are slow because of: a bad algorithm, redundant recomputation, one-query-per-row database access, or reading a whole file when a stream would do — none of which require leaving Python.

## Where it's used in a real project

- **Data pipelines**: `cProfile` shows 70% of time in `json.loads` → switch to a faster parser or skip parsing unused fields.
- **API handlers**: profiler reveals an ORM N+1 → add `select_related`/`joinedload`; response time drops 10× with zero new code.
- **Batch jobs**: a nested `for` doing `x in list` (O(n) scan) → `x in set` (O(1)) turns an overnight job into a minutes-long one.
- **Number crunching**: a Python loop over a million floats → NumPy vector op → 50–100× speedup because the loop moves into compiled C.

## Diagram

```
SLOW SCRIPT
    |
    v
[1] PROFILE (cProfile) ------> "where does time go?"
    |                            |
    |                     80% in one function? -> fix THAT
    v
[2] ALGORITHM -------------> O(n^2) -> O(n)?
    |                        dict/set lookups, early exit
    v
[3] I/O & CALLS -----------> batch queries? cache? stream?
    |                        lru_cache, generators, bulk ops
    v
[4] HEAVY GUNS -------------> NumPy vectorize | multiprocessing |
    |                         Cython/Rust — LAST resort
    v
FAST ENOUGH — stop when it meets the requirement,
not when it's theoretically optimal
```

## Code — explained

```python
import cProfile, pstats

def slow_find(pairs, targets):                      # 1
    found = []
    for t in targets:
        for k, v in pairs:                          # 2
            if k == t:
                found.append(v)
                break
    return found

def fast_find(pairs, targets):                      # 3
    lookup = dict(pairs)                            # 4
    return [lookup[t] for t in targets if t in lookup]

pairs = [(i, i * 10) for i in range(10_000)]
targets = list(range(5_000, 15_000))

prof = cProfile.Profile()                           # 5
prof.enable()
slow_find(pairs, targets)
prof.disable()
pstats.Stats(prof).sort_stats("cumulative").print_stats(4)  # 6
```

1. `slow_find` is O(n×m) — for every target it scans the whole pair list.
2. The inner loop is the hotspot: 10,000 pairs × 10,000 targets ≈ up to 100M comparisons.
3. `fast_find` converts to a dict once — O(n) — then each lookup is O(1).
4. `dict(pairs)` costs one pass; after that, `lookup[t]` is a hash lookup.
5. `cProfile.Profile()` + `enable()`/`disable()` times everything between the markers.
6. `print_stats(4)` shows the top functions by cumulative time — you'd see `slow_find` dominating, while `fast_find` barely registers. On this input the dict version is typically **~1000× faster**.

## Problems

### Easy — time two approaches
**Problem:** Use `time.perf_counter` to time building a string via `+=` vs `"".join` for 20,000 parts. Print both durations.
**Try this input:** 20,000 parts
**Expected output:**
```
+= : 0.00..s
join: 0.00..s
```
(join measurably faster; exact numbers vary by machine)
**Solution:**
```python
import time

parts = ["x"] * 20_000

t0 = time.perf_counter()
s = ""
for p in parts:
    s += p
t1 = time.perf_counter()
print("+= :", round(t1 - t0, 4), "s")

t2 = time.perf_counter()
s2 = "".join(parts)
t3 = time.perf_counter()
print("join:", round(t3 - t2, 4), "s")
```
**Logic explained:**
1. `time.perf_counter()` is the right clock for measuring elapsed time (monotonic, high resolution).
2. Wrap each approach in start/stop timestamps — this is the smallest possible "profile."
3. `join` allocates once; `+=` may realloc each iteration → join wins.
4. Even here we *measured* instead of assuming — the habit is the point.

### Medium — profile reveals the real hotspot
**Problem:** This script is slow. A dev assumes `write_report` is the problem and wants to optimize it. Profile it, find the true hotspot, and fix it.
```python
import cProfile, pstats, io

def is_duplicate(item, seen):      # seen is a LIST
    return item in seen

def ingest(rows):
    seen = []
    out = []
    for r in rows:
        if not is_duplicate(r, seen):
            seen.append(r)
            out.append(r * 2)
    return out

def write_report(values):
    return "total: " + str(sum(values))

def main():
    rows = [i % 5000 for i in range(200_000)]
    vals = ingest(rows)
    print(write_report(vals))

cProfile.run("main()")
```
**Try this input:** run `main()`
**Expected output:** `total: 24995000` — and the profile shows `is_duplicate` called 200,000 times dominating runtime, not `write_report`.
**Solution:**
```python
def ingest(rows):
    seen = set()                    # O(1) membership
    out = []
    for r in rows:
        if r not in seen:
            seen.add(r)
            out.append(r * 2)
    return out
```
**Logic explained:**
1. `item in seen` on a **list** is a linear scan — O(n) per call, called 200,000 times → the real hotspot.
2. `write_report` runs once and is already O(n) — the dev's intuition was wrong; only the profiler showed it.
3. Switching `seen` to a `set` makes membership O(1) — total work drops from O(n²) to O(n).
4. Same output, orders of magnitude faster — a one-line algorithmic fix found by measuring.

### Hard — the full ladder
**Problem:** Optimize step by step: (a) profile this, (b) fix the algorithm, (c) replace the remaining Python loop with NumPy. `data` has 1M floats; `threshold = 0.5`.
```python
def count_above(data, threshold):
    count = 0
    for x in data:
        if x > threshold:
            count += 1
    return count
```
**Try this input:** `data = [i / 1_000_000 for i in range(1_000_000)]`, `threshold=0.5`
**Expected output:** `499999` — identical for all three versions, each faster than the last.
**Solution:**
```python
import numpy as np

data = [i / 1_000_000 for i in range(1_000_000)]

# (b) algorithmic/Pythonic fix: sum() over a generator runs at C speed
def count_above_v2(data, threshold):
    return sum(1 for x in data if x > threshold)

# (c) vectorized fix: the loop moves into compiled C entirely
def count_above_v3(data, threshold):
    arr = np.asarray(data)
    return int(np.sum(arr > threshold))

print(count_above_v2(data, 0.5))
print(count_above_v3(data, 0.5))
```
**Logic explained:**
1. Profiling first would show 100% of time in the `for` loop — that's the hotspot.
2. v2 removes the manual counter and lets `sum` + generator do the iteration — fewer Python-level bytecodes, ~2× faster typically.
3. v3 converts to a NumPy array once, then `arr > threshold` is a vectorized comparison producing a boolean array, and `np.sum` counts `True`s — both run as compiled C over contiguous memory → ~50–100× faster than v1.
4. All three return `499999` (values 0.500001…0.999999) — optimization must never change the result.
5. The ladder matters: we tried cheap Python fixes before pulling in a dependency — NumPy is justified here, but if the script ran once a day in 2s, even v1 might be "fast enough."

## The 30-second interview answer

"First I profile — `cProfile` or `py-spy` — because my guess about the bottleneck is usually wrong, and Amdahl's law means optimizing a 10% section caps gains at ~11%. Then I work down the ladder: fix the algorithm first — O(n²) to O(n) with a dict or set beats everything else; then reduce I/O — batch DB queries, cache with `lru_cache`, stream instead of loading; then optimize the Python itself — comprehensions, `sum`/`any`, fewer attribute lookups. Only if it's still too slow do I go heavier: NumPy to vectorize loops into C, `multiprocessing` for CPU-bound parallelism, or Cython for a hotspot. And I stop when it meets the requirement — the goal is fast enough, not theoretically optimal."

## Follow-up trap

**"The profile shows `func` is called a million times but each call is fast — is it the bottleneck?"** — Look at **cumulative time** and **calls together**. A million cheap calls with big total time IS the bottleneck (fix the call pattern — batch or hoist it out of the loop). `tottime` (time inside the function itself) vs `cumtime` (including children) tells you whether the function is slow or just calling something slow.

**"Why not just rewrite the whole thing in Cython/Rust first?"** — Because if the algorithm is O(n²), a 10× faster O(n²) still loses to a plain-Python O(n) at scale. Rewriting costs weeks and adds a build toolchain; algorithm fixes cost minutes and often give bigger wins. Heavy tools are for the *residual* hotspot after the cheap wins.
