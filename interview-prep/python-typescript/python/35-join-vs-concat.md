# 35 — `"".join(list)` vs `+=` in a loop

> **Interview question:** "Why is `''.join(parts)` faster than concatenating strings with `+=` in a loop?"
> **What the interviewer is really testing:** Whether you understand that strings are *immutable*, so every `+=` copies the whole accumulated string — turning an O(n) job into O(n²) — versus just parroting "join is faster."

## Theory — what it is

Python strings are **immutable** — once created, a string object can never change. So `s += part` cannot "append" to `s`; it must allocate a **brand-new string** big enough for `old_s + part`, copy every character of the old string into it, copy the new part, then rebind the name `s`. The old string becomes garbage.

In a loop of `n` parts, the accumulated string is copied over and over: on iteration 1 you copy ~1 unit, iteration 2 you copy ~2 units, … iteration `n` copies ~n units. Total copying = 1 + 2 + … + n = **O(n²)** characters copied to produce O(n) of output.

`"".join(parts)` works differently: it makes **two passes** over the list — first to measure the total length, then a single allocation of exactly that size, then one copy of each part into its slot. Total work = **O(n)** — each character is copied exactly once.

"Jargon" decoded: **immutable** = cannot be modified after creation. **allocate** = request a fresh block of memory. **O(n²)** = runtime grows with the *square* of input size — double the input, quadruple the work.

## Why it was needed

The `+=` version isn't a small inefficiency — it's a complexity cliff:

| parts (each ~10 chars) | `+=` copies ≈ | `join` copies ≈ |
|---|---|---|
| 1,000 | 5,000,000 chars | 10,000 chars |
| 100,000 | 50,000,000,000 chars | 1,000,000 chars |
| 1,000,000 | 5,000,000,000,000 chars | 10,000,000 chars |

At a million parts, `+=` does ~500× more copying than `join`. This is the difference between "finishes instantly" and "minutes of garbage collection and memory churn." Immutability is a *design choice* (safe sharing, hashability, thread safety) — `join` is the tool the language gives you to build strings efficiently *within* that design.

## Where it's used in a real project

- **Building CSV/log lines**: `",".join(fields)` for each row instead of `line += field + ","`.
- **HTML/SQL assembly**: collecting fragments in a list, joining once at the end.
- **Repeated string building in parsers**: accumulating output tokens — list-append + join.
- **f-strings for few items**: `f"{a}-{b}"` is fine — join's advantage only matters in loops/many parts. (And CPython sometimes optimizes `+=` on a uniquely-referenced string, but never rely on it — it's an implementation detail, and quadratic at scale anyway.)

## Diagram

```
+= in a loop (strings immutable — every step copies EVERYTHING):

s = ""        s = "ab"        s = "abcd"        s = "abcdef"
+ "ab"   ->   + "cd"     ->   + "ef"       ->   ...
 copy 2        copy 4          copy 6
 ────────      ────────        ────────
 [ab]          [ab|cd]         [abcd|ef]
  ^new alloc    ^copy ab+cd     ^copy abcd+ef
total copied: 2 + 4 + 6 + ...   = O(n^2)


"".join(parts):

pass 1: measure  -> 2+2+2 = 6 chars needed
pass 2: ONE allocation [ _ _ _ _ _ _ ]
        copy each part once -> [a b c d e f]

total copied: each char once     = O(n)
```

## Code — explained

```python
import time

parts = ["chunk"] * 200_000                       # 1

# slow way
t0 = time.perf_counter()
s = ""
for p in parts:
    s += p                                        # 2
t1 = time.perf_counter()

# fast way
t2 = time.perf_counter()
s2 = "".join(parts)                               # 3
t3 = time.perf_counter()

print("+=  :", round(t1 - t0, 4), "s")            # 4
print("join:", round(t3 - t2, 4), "s")
print(s == s2)                                    # 5
```

Output (times vary by machine, ratio is the point):

```
+=  : 0.03-1.0 s
join: 0.001-0.003 s
True
```

1. 200k parts of 5 chars each → final string is 1,000,000 chars.
2. `s += p` — each iteration allocates a new string and copies *everything so far*. Iteration 100,000 copies ~500,000 chars just to add 5.
3. `"".join(parts)` — the separator is `""` (empty); `join` measures total size (1,000,000), allocates once, copies each part once.
4. On typical hardware `join` is tens to hundreds of times faster here, and the gap *widens* with more parts — that's the quadratic vs linear difference.
5. `s == s2` → `True`: identical result, wildly different cost. Correctness is the same; only the work differs.

## Problems

### Easy — rewrite to join
**Problem:** Rewrite this to use `join` and print the result.
```python
words = ["the", "quick", "brown", "fox"]
sentence = ""
for w in words:
    sentence += w + " "
```
**Try this input:** the list above
**Expected output:** `the quick brown fox` (note: no trailing space)
**Solution:**
```python
words = ["the", "quick", "brown", "fox"]
sentence = " ".join(words)
print(sentence)
```
**Logic explained:**
1. `" ".join(words)` puts the separator *between* items — no trailing space, which also fixes the `+=` version's trailing-space bug.
2. One call, one allocation, O(total length) work.

### Medium — join with transformation
**Problem:** Given `nums = [1, 2, 3, 4]`, produce `"1-2-3-4"`. Why does `"-".join(nums)` fail, and what's the fix?
**Try this input:** `nums = [1, 2, 3, 4]`
**Expected output:** `1-2-3-4`
**Solution:**
```python
nums = [1, 2, 3, 4]
print("-".join(str(n) for n in nums))
```
**Logic explained:**
1. `join` requires an iterable of **strings** — `"-".join(nums)` raises `TypeError: sequence item 0: expected str instance, int found`.
2. Fix: a generator expression `str(n) for n in nums` converts each item lazily — no intermediate list needed (though a list comp `"-".join([str(n) for n in nums])` is equally fine and sometimes marginally faster since join scans twice).
3. Result: `1-2-3-4`.

### Hard — measure the crossover
**Problem:** Show empirically that `+=` grows quadratically: time both approaches for `n = 10_000` and `n = 40_000` parts (4× input). Report the ratios.
**Try this input:** n = 10,000 then 40,000
**Expected output:**
```
n=10000  +=: ...s  join: ...s
n=40000  +=: ...s  join: ...s
+= grew ~16x, join grew ~4x
```
**Solution:**
```python
import time

def build_plus(n):
    s = ""
    for _ in range(n):
        s += "x"
    return s

def build_join(n):
    return "".join(["x"] * n)

for n in (10_000, 40_000):
    t0 = time.perf_counter(); build_plus(n);  t1 = time.perf_counter()
    t2 = time.perf_counter(); build_join(n);  t3 = time.perf_counter()
    print(f"n={n}  +=: {t1-t0:.4f}s  join: {t3-t2:.4f}s")
```
**Logic explained:**
1. Quadruple the input (10k → 40k): `join` time grows ~4× — linear, as expected.
2. `+=` time grows ~16× — quadratic (4²), because each `+=` copies the whole string built so far.
3. Note: CPython *does* have a refcount-based optimization where `s += x` on a string with only one reference can resize in place — so on some inputs `+=` looks linear-ish for short runs. It still degrades badly with longer strings and more parts, and it's an implementation detail — `join` is the guaranteed O(n) contract.

## The 30-second interview answer

"Strings in Python are immutable, so `s += part` can't extend `s` — it allocates a new string and copies all the accumulated content plus the new part. In a loop of n parts, you copy 1 + 2 + … + n characters — O(n²) total copying and O(n) allocations. `''.join(parts)` does two passes: it sums the lengths, allocates once at exactly the right size, and copies each part exactly once — O(n). Same result, but the difference is quadratic vs linear, so join wins by orders of magnitude at scale. For just two or three strings, `+` or an f-string is perfectly readable and fine."

## Follow-up trap

**"But I timed `+=` and it seemed fast — is join really necessary?"** — CPython has an optimization: if the string's refcount is 1 (no other references), `+=` may resize in place instead of copying. That makes small benchmarks misleading. It's an implementation detail, it breaks down when other references exist or strings get large, and PyPy/other interpreters don't promise it. `join` is O(n) *by contract* — always use it in loops.

**"What if the parts are produced one at a time, e.g. inside a loop with conditions?"** — Append each part to a **list** (O(1) amortized appends, no copying), then `''.join(the_list)` once at the end. You still get O(n) total: lists are mutable, so appending doesn't copy — unlike strings.
