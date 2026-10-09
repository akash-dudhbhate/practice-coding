# 08 — Sliding Window vs Two-Pointers (lesson 04)

> 4-minute read. Two techniques, two fingers each — easy to confuse.

## The idea, plain words

Both techniques hold two indices into a sequence. The difference is
**what matters**:

- **Two-pointers (lesson 04):** the answer is about the *two pointed-at
  elements* — a pair summing to a target, a palindrome's ends. Pointers
  usually move **toward each other** (left/right closing in) or at
  different speeds (fast/slow, like in-place dedup).
- **Sliding window (this lesson):** the answer is about the *whole chunk
  between* the pointers. Both move **the same direction** — `right`
  leads, `left` follows — and the segment `[left..right]` is the object
  of study.

```
Two pointers — ends closing in (sorted pair-sum):
[1, 2, 4, 7, 11]
 L           R      check 1+11 → too big? move R left

Sliding window — same direction, chunk is the answer:
[2, 1, 5, 1, 3, 2]
    └─k=3─┘         L and R both march rightward
```

Honestly, a sliding window IS a two-pointer technique — a special case
where the region *between* the pointers is what you're measuring.

## Side-by-side

| | Two pointers (L04) | Sliding window (L05) |
|---|---|---|
| Movement | toward each other, or fast/slow | same direction, left chases right |
| What's tracked | the pair: `a[l]`, `a[r]` | the chunk: sum / counts of `[l..r]` |
| Needs sorted input? | often (pair sums) | never — order is the problem |
| Question shape | pairs, partitions, in-place edits | contiguous subarray/substring |

## How to tell which tool to grab

Ask: **"Is the answer a contiguous chunk?"**

- Yes → sliding window. The chunk itself is the answer.
- No — it's a *pair*, a *partition point*, an *in-place rearrangement* →
  two pointers.

`"find two numbers summing to 9 in a sorted array"` — the answer is two
*elements*, not a chunk → two pointers, ends closing in.
`"longest substring with no repeats"` — the answer is a chunk → window.

## Why it exists (why learn the boundary?)

Because reaching for the wrong one wastes the interview. Ends-closing-in
on a contiguous problem skips windows entirely. A window on a pair-sum
problem drags bookkeeping (sums, counts) that the problem never asked for.

## Where it's used

Two pointers: pair-sum on sorted arrays, reverse in place, move-zeros,
container-with-water. Sliding window: everything from chapters 01–07 —
rolling stats and longest/shortest contiguous chunks.

## Common mistake

Trying ends-closing-in on a chunk problem. `"smallest subarray with
sum ≥ 7"`: if you start `left=0, right=n−1` and pull inward, you'll test
`[0..n−1]`, `[0..n−2]`, `[1..n−2]`... — you enumerate *some* windows in a
weird order and can still miss the answer, because neither pointer knows
the rule "shrink only while valid." The window's `for right / while shrink`
loop exists precisely because the *whole segment* carries the state.

## Your turn

Classify each: **window** or **two-pointer**?

1. In sorted `nums`, find a pair that sums to `target`.
2. Longest run of `1`s possible after flipping at most `k` zeros.
3. Move all zeros to the end of the array, in place.

<details><summary>Answer</summary>
1. **Two-pointer** — a pair of elements, ends closing in on sorted data.
2. **Window** — "longest contiguous run containing ≤ k zeros" is a
   variable-size window (that's medium/p02!).
3. **Two-pointer** — fast/slow in-place rearrangement; no chunk is being
   measured.
</details>

---

**← Prev** [07 — Why sliding is O(n)](07-why-sliding-is-on.md) ·
**Next →** [09 — The recipe & pitfall gallery](09-the-recipe-and-pitfalls.md)
