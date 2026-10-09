# 05 — Palindrome Check

> 4-minute read.

## The idea, plain words

A palindrome reads the same forwards and backwards — "racecar", "level".
To check one: point `L` at the first character and `R` at the last.
**If the ends don't match, it's not a palindrome — answer done.** If they
match, step both inward and check the next pair.

Real-life version: **folding a word in half like a paper strip.** If it's
a palindrome, every letter lands exactly on its twin. The two pointers
are your two fingers checking each overlapping pair.

## In code

```python
def is_palindrome(s):
    L, R = 0, len(s) - 1
    while L < R:
        if s[L] != s[R]:        # ends disagree → not a palindrome
            return False
        L += 1
        R -= 1
    return True                 # every pair matched

print(is_palindrome("racecar"))
print(is_palindrome("hello"))
```

Output:

```
True
False
```

## Hand trace — small data

`"racecar"`, matching all the way in:

```
r → [r a c e c a r] ← r     'r' == 'r' → step in
    a → [a c e c a] ← a     'a' == 'a' → step in
        c → [c e c] ← c     'c' == 'c' → step in
            L == R on 'e'   middle char mirrors itself → True
```

`"hello"` fails fast — that's the point:

```
h → [h e l l o] ← o         'h' != 'o' → return False immediately
```

One comparison killed it. We never looked at the middle three letters.

## Why it exists

The palindrome *definition* is symmetric — character i must equal
character n−1−i. Two pointers check each required pair once, O(n) time,
O(1) space. The naive alternative `s == s[::-1]` works, but builds a
reversed copy first — O(n) extra space for a question two fingers answer
for free.

## Where it's used

`easy/p02` — with one upgrade: real problems give messy input like
`"A man, a plan, a canal: Panama"`. Fix = let each pointer **skip**
non-letters before comparing:

```python
def is_palindrome_messy(s):
    L, R = 0, len(s) - 1
    while L < R:
        while L < R and not s[L].isalnum(): L += 1   # L skips junk
        while L < R and not s[R].isalnum(): R -= 1   # R skips junk
        if s[L].lower() != s[R].lower():
            return False
        L += 1; R -= 1
    return True

print(is_palindrome_messy("A man, a plan, a canal: Panama"))
```

Output: `True`

## Common mistake

Forgetting to **skip and normalize**: comparing `'A'` to `'a'` (use
`.lower()`) or stopping on a space/comma. Inner skip-loops stay O(n)
because each pointer still only moves forward, never back — total steps
across all loops ≤ n.

## Your turn

Is `"noon"` a palindrome? How many comparisons does the check run?

<details><summary>Answer</summary>
Yes. `n → [n o o n] ← n` match; `o → [o o] ← o` match; pointers cross.
**2 comparisons** — the middle pair counted once, not twice.
</details>

---

**← Prev** [04 — Reverse in place](04-reverse-in-place.md) ·
**Next →** [06 — Sorted pair-sum: the blame rule](06-sorted-pair-sum.md)
