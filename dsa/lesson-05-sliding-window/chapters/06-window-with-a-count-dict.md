# 06 — The Window + a Count Dict

> 6-minute read. The pattern behind every substring problem.

## The idea, plain words

So far the window's "state" was one number — a running sum. For string
problems the state is a **notebook**: a dict counting how many times each
character sits inside the window.

- Enter on the right → `count[c] += 1`
- Leave on the left → `count[c] -= 1`

The window is "invalid" when the notebook says a rule is broken — e.g.,
some character's count is above 1 in a "no repeats" problem.

## The classic: longest substring with no repeated characters

`s = "abcabcbb"`. Same skeleton as chapter 05: expand `right`, and while
`count` reports a duplicate, shrink `left`.

```
s = "a b c a b c b b"
i =  0 1 2 3 4 5 6 7

right=0 'a'  count{a:1}           window "a"    len 1  best=1
right=1 'b'  count{a:1,b:1}       window "ab"   len 2  best=2
right=2 'c'  count{a:1,b:1,c:1}   window "abc"  len 3  best=3
right=3 'a'  a→2, invalid → shrink: drop 'a'(0) → a:1, left=1.  "bca" len 3
right=4 'b'  b→2 → shrink: drop 'b'(1) → b:1, left=2.           "cab" len 3
right=5 'c'  c→2 → shrink: drop 'c'(2) → c:1, left=3.           "abc" len 3
right=6 'b'  b→2 → shrink: drop 'a'(3) → a:0; still 2 → drop 'b'(4) → b:1, left=5. "cb" len 2
right=7 'b'  b→2 → shrink: drop 'c'(5) → c:0; still 2 → drop 'b'(6) → b:1, left=7. "b"  len 1
answer: 3
```

## The code

```python
def longest_no_repeat(s):
    count = {}
    left = best = 0
    for right, c in enumerate(s):
        count[c] = count.get(c, 0) + 1     # enter
        while count[c] > 1:                # a duplicate inside → invalid
            d = s[left]
            count[d] -= 1
            left += 1                      # shrink until it's gone
        best = max(best, right - left + 1) # window is valid again → record
    return best

print(longest_no_repeat("abcabcbb"))   # 3
```

## Level-up peek (used in medium/p01's solution)

When `'a'` repeats, we stepped `left` one at a time. A faster version keeps
`last[c]` = the index where `c` was last seen, and **jumps** `left` past it
in one move (`left = last[c] + 1`, guarded so it never moves backward).
Same answer, fewer steps. Peek at `medium/solutions/p01` after your own
attempt — the guarded-jump version lives there.

## Why it exists

A running sum can't answer "does this substring have repeats?" — sums
don't see *which* elements are inside, only their total. The count dict
sees membership: `count[c] > 0` means "c is in the window right now."
Different question → different state. Same window.

## Where it's used

Longest-no-repeat (here), "at most k distinct characters," fruit into
baskets, minimum window substring — every `medium`/`hard` problem swaps
the running sum for this notebook. For "at most k distinct," invalid =
`len(count) > k`, which is why you must `del count[d]` when it hits 0 —
zombie zero-count keys make `len(count)` lie.

## Common mistake

Forgetting `del` on zero counts (when your check uses `len(count)`):

```python
count[d] -= 1
if count[d] == 0:
    del count[d]     # keep len(count) honest
```

Without it, `count` claims a character is still in the window after it
left — the window looks more crowded than it is.

## Your turn

In the trace, at `right=6` the shrink dropped **two** characters
(`a` then `b`) in one round. Why two, not one?

<details><summary>Answer</summary>
The new `'b'` at index 6 duplicated the `'b'` at index 4. Shrinking once
dropped `'a'` (index 3), but `b` still had count 2 — the window was still
invalid — so `while` kept going until `left` passed the old `'b'`.
That's exactly why `while`, not `if`, matters (chapter 05).
</details>

---

**← Prev** [05 — Variable-size windows](05-variable-size-windows.md) ·
**Next →** [07 — Why sliding is O(n)](07-why-sliding-is-on.md)
