# 09 — Two Pointers vs Hashing: the Space Tradeoff

> 4-minute read.

## The idea, plain words

"Find a pair that sums to `target`" has **two** famous solutions:

- **Hash set** (lesson 03): walk once, ask "have I seen `target − x`?"
  Works on *any* array — but stores up to n numbers → O(n) extra space.
- **Two pointers** (chapter 06): works only on *sorted* arrays — but
  stores just two index variables → **O(1)** extra space.

Same O(n) time. Different memory bill. That's the whole tradeoff:

```
                 |  hashing          |  two pointers
-----------------|-------------------|----------------
time             |  O(n)             |  O(n)*
extra space      |  O(n)             |  O(1)
needs            |  nothing          |  sorted input
keeps indices    |  yes              |  lost if you sort
                 *plus O(n log n) to sort if it isn't already
```

## In code — same problem, two bills

```python
def pair_sum_hash(nums, target):       # works unsorted, costs memory
    seen = set()
    for x in nums:
        if target - x in seen:
            return True
        seen.add(x)
    return False

def pair_sum_ptr(nums, target):        # sorted input, zero memory
    L, R = 0, len(nums) - 1
    while L < R:
        s = nums[L] + nums[R]
        if s == target: return True
        L, R = (L + 1, R) if s < target else (L, R - 1)
    return False

print(pair_sum_hash([8, 2, 5, 1], 9))   # any order
print(pair_sum_ptr([1, 2, 5, 8], 9))    # must be sorted
```

Output:

```
True
True
```

## Hand trace — same input, two memory footprints

On `[1, 2, 5, 8]`, target 9 — hashing's `seen` set grows with every step
while the pointers stay two integers:

```
hashing:   x → [1, 2, 5, 8]      seen = {1, 2, 5, ...}  up to n stored
pointers:  L → [1, 2, 5, 8] ← R  1+8=9 → found          0 extra stored
```

## Why it exists

Interviews love the follow-up: *"Can you do it in O(1) space?"* Hashing
has no answer — its memory grows with n. Two pointers is the answer,
**if** the input is sorted (or you're allowed to sort). Knowing both —
and when each applies — is worth more than knowing either alone.

## Where it's used

- Already-sorted input or a strict memory budget → two pointers.
- Unsorted input, original indices needed, streaming data → hashing.
- In-place requirements (reversal, dedup, merge) → hashing can't even
  play; pointers win by default.

## Common mistake

Sorting to enable two pointers **destroys the original indices.** If the
answer requires positions, carry them: sort `(value, index)` pairs
together, or just use hashing — paying O(n) space to keep O(n) simplicity
is often the right trade.

## Your turn

Unsorted array, must return the *indices* of the pair. Hashing or two
pointers — and why?

<details><summary>Answer</summary>
**Hashing.** Two pointers needs sorted order, and sorting shuffles the
indices away (you'd have to lug `(value, index)` pairs through a sort).
The hash set answers on unsorted data directly — O(n) space is the price
of skipping the sort.
</details>

---

**← Prev** [08 — Partition: move-zeros](08-partition-move-zeros.md) ·
**Next →** [10 — When two pointers FAILS](10-when-it-fails.md)
