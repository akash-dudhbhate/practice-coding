# 11 — Word Break: the "can you reach?" shape (top-down on strings)

> 6-minute read. Yes/No answers, `any()` instead of `max`/`sum` — and memoization returns.

## The idea, plain words

> Can `"leetcode"` be chopped into dictionary words `{"leet", "code"}`?
> (`"catsandog"` with `{"cats","dog","sand","and","cat"}` → can't —
> there's always a letter left over.)

Real-life version: does a jumbled license plate split into real words?

Third phrasing of DP: not "count ways", not "min cost" — **"is it
possible?"** Define a boolean state:

```
can_break(i) = "can the suffix s[i:] be split into words?"
```

Then try every word that fits at position `i`; if ANY leads to a
reachable end, the answer is yes:

```
can_break(i) = any( s[i:] starts with w  AND  can_break(i + len(w)) )
can_break(len(s)) = True    ← empty suffix = success!
```

## Watch the recursion — top-down this time

```
can_break(0)   "leetcode"
 ├─ try "leet"  → matches positions 0-3 → can_break(4)
 │    ├─ try "leet"  → "code" doesn't start with "leet" → dead
 │    └─ try "code"  → matches → can_break(8)
 │           can_break(8) = True   (empty suffix — done!)
 └─ try "code"  → "leet" doesn't start with "code" → dead
Answer: True
```

Same problem, `"aaaa..."` with `{"a","aa"}`: every position branches two
ways → exponential blowup *without* a notebook. But `can_break(i)` only
has `n+1` possible arguments — memoize on `i` and it collapses.

```python
from functools import lru_cache

def word_break(s, wordDict):
    words = set(wordDict)
    @lru_cache(maxsize=None)
    def can_break(i):
        if i == len(s):
            return True                 # reached the end = success
        return any(
            s.startswith(w, i) and can_break(i + len(w))
            for w in words
        )
    return can_break(0)
```

Verified: `word_break("leetcode", ["leet","code"])` → `True`,
`word_break("catsandog", ["cats","dog","sand","and","cat"])` → `False`.

## Why it exists

It rounds out the trio: `sum` over last moves (stairs) · `max`/`min`
over choices (robber, coins) · `any` over ways to arrive (this one).
Notice the memo key is an **index, not a number we build up to** —
top-down memoizes *where you are*, which is why `hard/p01` is most
naturally solved this way.

## Where it's used

`hard/p01`. Same boolean-reachability shape: jump game (can you reach
the last index?), partition equal subset sum (`hard/p03` — can you pick
numbers reaching `total/2`), regex matching.

## Common mistake

A memo key that forgets part of the state. If your subproblem were
`can_break(i, words_used)` and you memoized only on `i`, two different
situations would collide in the cache and return wrong answers. The key
must encode **everything** the answer depends on. (Here `i` alone is
complete — the dictionary never changes.)

## Your turn

`word_break("aaaa", ["a", "aa"])` — True or False, and why was the memo
essential for strings like this?

<details><summary>Answer</summary>
**True** — four `"a"`s, or two `"aa"`s, etc. The memo is essential
because EVERY position can branch into `i+1` and `i+2` — without it,
`can_break` calls explode exponentially; with it, each index computes
once.
</details>

---

**← Prev** [10 — LIS](10-longest-increasing-subsequence.md) ·
**Next →** [12 — Space optimization](12-space-optimization.md)
