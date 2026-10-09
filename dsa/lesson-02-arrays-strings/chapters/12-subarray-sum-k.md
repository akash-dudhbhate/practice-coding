# 12 — Prefix sums + a dict: subarrays that sum to k

> 6-minute read. Two old ideas combine into the hardest one yet.

## The idea, plain words

A **subarray** is a contiguous slice — elements in a row, no gaps.
`[1,1]` inside `[1,1,1]` counts; `[1, ,1]` with a hole does not.

Goal: *count* subarrays whose sum equals `k`. The brute force —
check every start/end pair and sum it — is O(n²) or worse. Instead,
recall the chapter-06 identity:

```
sum(i..j) = P[j+1] - P[i]
```

Rearrange it. While scanning, suppose your running total so far is
`P`. A subarray ending *here* sums to `k` exactly when some earlier
running total was `P - k`:

```
P_now - P_earlier = k   <=>   P_earlier = P_now - k
```

So keep a **dict of every running total seen so far and how many
times** (chapter 10's tally, on sums instead of chars). At each step,
ask: *have I seen `P - k` before?* Each sighting = one subarray ending
here.

Real-life version: **odometer again**. You've driven `P_now` total
miles. "How many trips were exactly `k` miles?" = how many past
odometer readings were `P_now - k`.

## Trace `[1, 1, 1]` with `k = 2`

Seed the dict with `{0: 1}` — "a total of 0 was seen once, before we
started." (Explained below — it's the crucial step.)

```
start:       seen = {0: 1}          P = 0, count = 0

x=1: P=1    P-k = -1   seen? no     count=0     seen={0:1, 1:1}
x=1: P=2    P-k =  0   seen 1 time! count=1     seen={0:1, 1:1, 2:1}
x=1: P=3    P-k =  1   seen 1 time! count=2     seen={..., 3:1}

answer: 2   (subarrays [1,1] at indices 0-1 and 1-2)
```

The code is almost suspiciously short:

```python
def count_subarray_sum(nums, k):
    seen = {0: 1}            # prefix total -> how many times seen
    P = count = 0
    for x in nums:
        P += x                       # running total
        count += seen.get(P - k, 0)  # earlier totals that make a k-sum
        seen[P] = seen.get(P, 0) + 1 # record P for future steps
    return count

print(count_subarray_sum([1, 1, 1], 2))   # -> 2
print(count_subarray_sum([1, 2, 3], 3))   # -> 2  ([1,2] and [3])
```

One pass, one dict → **O(n) time, O(n) space** (ch 10 tally + ch 06
prefix, wearing a trench coat together).

## Why does `{0: 1}` get seeded?

A subarray starting at index 0 has sum = `P_now - 0`. Without `0` in
the dict, `[2]` with `k=2` would report 0 — but `[2]` itself qualifies!
The seed says "the empty prefix, total 0, happened once." Forget it and
every subarray starting at index 0 goes uncounted.

## Why it exists

It's the fullest version of this lesson's theme: **precompute + hash**.
"For each j, check all i < j" (O(n²)) becomes "for each j, one dict
lookup" (O(n)). The general trick — *difference of prefixes in a
hashmap* — unlocks a whole family of subarray problems.

## Where it's used

`hard/p01` (exactly this), subarrays with equal 0s and 1s (map 0→-1,
then k=0!), "how many times did balance hit target" — the pattern
travels far beyond sums.

## Common mistakes (there are two famous ones)

- **Forgetting `{0: 1}`** — see above. Seed first.
- **Recording `P` before checking `P - k`** — then a subarray could
  "end before it starts" and `k=0` cases get phantom matches. Order is:
  update P → look up → record.

## Your turn

`count_subarray_sum([2], 2)` — without the `{0: 1}` seed, what does the
code wrongly return, and why?

<details><summary>Answer</summary>
`0` instead of `1`. At x=2, P=2 and P-k=0 — but `seen` is empty, so the
subarray `[2]` (starting at index 0) is missed. The seed exists purely
for subarrays that begin at the start.
</details>

---

**← Prev** [11 — Building strings: `join`, not `+=`](11-join-not-plus-equals.md) ·
**Next →** [13 — Kadane's: extend or restart](13-kadane-extend-or-restart.md)
