# 11 — Running Totals in a Map (prefix sums)

> 6-minute read. The complement trick, one level deeper.

## The idea, plain words

New question: *how many subarrays sum to exactly `k`?*

Brute force tries every start/end pair — O(n²). Instead, keep a
**prefix** — the running total of everything seen so far — and notice:

```
sum of subarray (i..j)   =   prefix[j] - prefix[i-1]

so a subarray sums to k  <=>  some earlier prefix equals  prefix[j] - k
```

That's the complement trick again — the "partner" is an **old prefix**.
Keep a frequency map of prefixes seen; at each step ask *"have I seen
`prefix - k`? Each time it appeared is one valid subarray ending here."*

```python
def count_subarrays(nums, k):
    count = 0
    prefix = 0
    freq = {0: 1}                          # the empty prefix counts once!
    for x in nums:
        prefix += x
        count += freq.get(prefix - k, 0)   # past prefixes that work
        freq[prefix] = freq.get(prefix, 0) + 1
    return count

print(count_subarrays([1, -1, 0], 0))
```

```
3
```

## Walk it by hand — nums = [1, -1, 0], k = 0

```
start    prefix=0    freq={0:1}
x=1      prefix=1    need 1-0=1   miss      freq={0:1, 1:1}   count=0
x=-1     prefix=0    need 0-0=0   hit x1    freq={0:2, 1:1}   count=1  ([1,-1])
x=0      prefix=0    need 0-0=0   hit x2    freq={0:3, 1:1}   count=3  ([1,-1,0], [0])
```

## Why it exists

The frequency map turns "how many subarrays ending here sum to k?" into
an O(1) question — every matching old prefix is one complete subarray,
and the map counted them all for free.

The `{0: 1}` seed matters: it stands for *"the sum before the array
started"*, so a subarray that begins at index 0 and hits k gets counted
too.

## Where it's used

Subarray-sum-equals-k, "divisible by k" variants (store `prefix % k`),
balanced 0/1 subarrays (treat 0 as -1, so balanced means sum 0),
continuous-range-sum analytics.

## Common mistakes

- Forgetting `freq = {0: 1}` — `[2, -2]` with `k=0` sums to 0 via the
  empty prefix; no seed → missed.
- Recording the new prefix **before** querying — a zero-length
  "subarray" could wrongly count when `k == 0`. Query first, then store.
- Trying it for "sum **≥** k" — hashing answers *exact equality* only.
  Inequalities need other tools (sliding window — lesson 05).

## Your turn

`nums = [1, 2, 3]`, `k = 3` — walk the table. How many subarrays sum
to 3? (Remember the `{0:1}` seed.)

<details><summary>Answer</summary>
**2.** prefixes: seed 0; after 1 → prefix 1, need −2, miss;
after 2 → prefix 3, need 0 → hit (seed) = `[1,2]`; after 3 → prefix 6,
need 3 → hit = `[3]`. Count = 2.
</details>

---

**← Prev** [10 — The complement trick](10-the-complement-trick.md) ·
**Next →** [12 — Remembering order](12-remembering-order-lru.md)
