# 09 — Wildcard Matching: Same Table, Now With Booleans

> 6-minute read. The LCS skeleton one more time — cells become True/False.

## The idea, plain words

Does pattern `p` match *all* of string `s`? The pattern has two wildcards:

- `?` — matches exactly **one** character (any char)
- `*` — matches **any run** of characters, including **zero**

Real-life version: **shell globbing** — `ls *.py` is a wildcard match on
filenames.

The sentence: **`dp[i][j]` = does `p`'s first `j` chars match `s`'s first
`i` chars?** Yes/no per cell — a boolean table.

## The recurrence — three cases

```
p[j-1] == '*':            dp[i][j] = dp[i][j-1]      star matches EMPTY
                                  or dp[i-1][j]      star eats one more char
p[j-1] == '?' or a match: dp[i][j] = dp[i-1][j-1]    consume one char each
otherwise (mismatch):     dp[i][j] = False
```

The `*` line is the heart: `dp[i][j-1]` = "the star stood for nothing";
`dp[i-1][j]` = "the star ate `s`'s char and is *still hungry*" — the pattern
index `j` doesn't advance, so `*` can eat more later.

## Fill the table — `s = "aa"`, `p = "a*"`

```
          ""    a     *
   ""   [ T    F     F ]    "a*" vs "": 'a' needs a char → F; star
                            copies dp[0][1]=F (can't fix the 'a')
   a    [ F    T     T ]    'a'=='a' → diag T;  '*' gets dp[1][1]=T
   a    [ F    F     T ]    '*' gets ←dp[2][1]=F or ↑dp[1][2]=T → T
```

Answer: `dp[2][2] = True` — `a*` matches `aa` (star ate the second `a`).

Watch `dp[0][2]`: it's **False**, not True. A lone `*` matches empty, but
`a*` has that `a` first — the star copies `dp[0][1]` which already failed.
Borders propagate honestly.

## The code

```python
def is_match(s, p):
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True                                  # empty matches empty
    for j in range(1, n + 1):                        # pattern like "***" can
        if p[j - 1] == '*':                          # match the empty string
            dp[0][j] = dp[0][j - 1]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
    return dp[m][n]
```

Verified: `is_match("aa", "a*")` → `True` · `is_match("aa", "*")` → `True` ·
`is_match("adceb", "*a*b")` → `True` · `is_match("acdcb", "a*c?b")` → `False`.

## Why it exists

Recursion on `*` tries every possible run-length — exponential branches.
The `dp[i-1][j]` trick folds "star ate one char" into a neighbor lookup:
each cell is decided by two cells already done. `m × n` cells, O(1) each.

## Where it's used

Glob matching, simplified regex engines, and the family insight you'll reuse
in interviews: **same `dp[i][j]`-over-prefixes state as LCS/edit distance —
only the recurrence and cell type change.** Count → int, min-cost → int,
possible → bool.

## Common mistake

For the `*` case, writing `dp[i][j] = dp[i][j-1]` only — "star = empty".
That fails `"aa"` vs `"a*"`. The `or dp[i-1][j]` half ("star ate a char and
stays alive") is what makes `*` actually wildcard.

## Your turn

For `is_match("abc", "a?c")` — which recurrence branch fires at
`dp[2][2]` (the `?` cell), and what's the final answer?

<details><summary>Answer</summary>
`?` matches any single char → `dp[2][2] = dp[1][1]` (consume `b` and `?`
together). `dp[1][1]` is True (`'a'=='a'`), and `dp[3][3]` gets True via
`'c'=='c'` → answer **True**: `a?c` matches `abc`.
</details>

---

**← Prev** [08 — Edit distance](08-edit-distance.md) ·
**Next →** [10 — Interval DP: pick the LAST move](10-interval-dp-burst-balloons.md)
