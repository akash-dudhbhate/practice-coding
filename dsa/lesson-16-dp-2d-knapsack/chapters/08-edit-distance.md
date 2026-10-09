# 08 — Edit Distance: LCS's Harder Cousin

> 7-minute read. Same table, new question — and a border trap.

## The idea, plain words

How many single-character edits turn string A into string B? Three allowed
moves: **insert**, **delete**, **substitute**. `"cat"` → `"cut"` = 1 edit
(substitute `a`→`u`). `"horse"` → `"ros"` = 3.

Real-life version: **your spell-checker.** "Did you mean…" is literally
edit distance — the suggestion with the fewest edits wins.

The sentence: **`dp[i][j]` = min edits to turn `a`'s first `i` chars into
`b`'s first `j` chars.** Familiar state — the meaning changed from "longest
shared" to "cheapest conversion".

## The recurrence — three moves, one free

```
if a[i-1] == b[j-1]:   dp[i][j] = dp[i-1][j-1]              ← free match, 0 cost
else:                  dp[i][j] = 1 + min(
                            dp[i-1][j],                     delete a's char
                            dp[i][j-1],                     insert b's char
                            dp[i-1][j-1])                   substitute
```

Match → diagonal, free. Mismatch → pay 1 and take the cheapest of three
fixes.

## The border trap — real costs, not zeros

`dp[0][j]` = "turn the *empty* string into `b[:j]`" → costs `j` **inserts**.
`dp[i][0]` = "delete `i` chars" → costs `i`. **Min-problems seed borders
with real costs.** LCS's zero borders would claim "empty→'cut' is free".

## Fill the table — `a = "cat"`, `b = "cut"`

```
          ""   c   u   t
   ""   [ 0   1   2   3 ]   build "cut" from nothing: j inserts
   c    [ 1   0   1   2 ]   'c'=='c' at (1,1) → free
   a    [ 2   1   1   2 ]
   t    [ 3   2   2   1 ]   't'=='t' at (3,3) → dp[2][2] free
```

The money cells:

```
dp[2][2]: 'a' vs 'u' — mismatch → 1 + min(↑dp[1][2]=1, ←dp[2][1]=1,
          ↖dp[1][1]=0) = 1          ← substitute a→u (the ↖ path)
dp[3][3]: 't' vs 't' — MATCH → dp[2][2] = 1
```

Answer: `dp[3][3] = 1` — one substitution. The table *found* the edit.

## The code

```python
def edit_distance(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1): dp[i][0] = i        # delete all of a[:i]
    for j in range(n + 1): dp[0][j] = j        # insert all of b[:j]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]                    # free match
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],               # delete
                                   dp[i][j - 1],               # insert
                                   dp[i - 1][j - 1])           # substitute
    return dp[m][n]
```

Verified: `edit_distance("cat", "cut")` → `1` ·
`edit_distance("horse", "ros")` → `3` (horse → rorse → rose → ros).

## Why it exists

Same as LCS — brute-forcing edit sequences is exponential. The prefix×prefix
state collapses it to `m × n`. The three-move `min` is also the template for
cost-based alignment everywhere (DNA sequencing, OCR correction).

## Common mistake

**Zero borders on a min problem.** `dp[0][2] = 0` claims turning "" into
`"cu"` is free → the whole table under-reports. If your answer is
suspiciously small, check the borders first. (Compare: counting problems
*want* zeros — knapsack row 0 = 0 value is honest.)

## Your turn

`edit_distance("", "abc")` and `edit_distance("abc", "")` — what are they,
and which border cells answer each?

<details><summary>Answer</summary>
`3` and `3` — `dp[0][3]` (insert 3 chars) and `dp[3][0]` (delete 3 chars).
The borders ARE the answers when one side is empty — another reason they
must hold real costs.
</details>

---

**← Prev** [07 — LCS](07-lcs-two-strings.md) ·
**Next →** [09 — Wildcard matching](09-wildcard-matching.md)
