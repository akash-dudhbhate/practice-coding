# 07 — LCS: Comparing Two Strings

> 7-minute read. The two-pointer state — one per sequence.

## The idea, plain words

A **subsequence** is what you get by *deleting* characters — order kept,
gaps allowed. `"ace"` is a subsequence of `"abcde"` (drop `b`, `d`).

The **Longest Common Subsequence (LCS)** of two strings is the longest
subsequence living inside both. `"abcde"` vs `"ace"` → `"ace"`, length 3.

Real-life version: **`git diff` / DNA alignment / spell-checkers** — "what
do these two sequences share, in order?" is asked constantly.

The sentence: **`dp[i][j]` = LCS length of `a`'s first `i` chars vs `b`'s
first `j` chars.** Two prefixes — two dimensions. (Chapter 1's rule.)

## The recurrence — a two-way choice

Look at the last chars of each prefix:

```
if a[i-1] == b[j-1]:   dp[i][j] = dp[i-1][j-1] + 1    ← match! extend the LCS
else:                  dp[i][j] = max(dp[i-1][j],        ← drop a's last char
                                      dp[i][j-1])        ← or drop b's last char
```

Match → diagonal + 1. Mismatch → best of skipping either side.

## Fill the table — `a = "abc"`, `b = "acd"`

```
          ""   a   c   d
   ""   [ 0   0   0   0 ]   empty vs anything = 0
   a    [ 0   1   1   1 ]   'a'=='a' at (1,1): diag+1
   b    [ 0   1   1   1 ]   'b' matches nothing: inherit best
   c    [ 0   1   2   2 ]   'c'=='c' at (3,2): dp[2][1]+1 = 2
```

Cell-by-cell for two interesting spots:

```
dp[1][1]: 'a' vs 'a' — MATCH → dp[0][0] + 1 = 1
dp[2][2]: 'b' vs 'c' — no match → max(↑dp[1][2]=1, ←dp[2][1]=1) = 1
dp[3][2]: 'c' vs 'c' — MATCH → dp[2][1] + 1 = 2     ← the 'c' links up
```

Answer: `dp[3][3] = 2` — the shared subsequence is `"ac"`.

## The code

```python
def lcs(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:                     # chars under the
                dp[i][j] = dp[i - 1][j - 1] + 1          # prefixes match
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]
```

Verified: `lcs("abcde", "ace")` → `3` · `lcs("abc", "acd")` → `2` ·
`lcs("abc", "def")` → `0` (nothing shared — a real answer, not an error).

## Why it exists

Comparing all subsequences of two length-`n` strings is exponential
(each string has `2ⁿ` subsequences). The prefix×prefix table makes it
`m × n` cells of O(1) work each.

## Where it's used

- Diff tools (`diff`, `git diff`) — LCS of lines = what stayed the same.
- Bioinformatics — DNA/protein alignment.
- Spell-checkers and fuzzy search — "how similar are these?"
- The **skeleton for edit distance and wildcard matching** (next two
  chapters): same state, new recurrence.

## Common mistake

Confusing **subsequence** with **substring**. Substring = contiguous block
(`"cd"` in `"abcde"`); subsequence = in-order with gaps allowed (`"ace"`).
LCS answers are *larger* than longest-common-substring answers — if your
LCS on `"abcde"`/`"ace"` isn't 3, you solved the substring version.

Also: the char under `dp[i][j]` is `a[i-1]`/`b[j-1]` — same off-by-one as
knapsack. Row `i` = first `i` chars.

## Your turn

Using the `abc`/`acd` table: why is `dp[3][3] = 2` even though `'c' != 'd'`?

<details><summary>Answer</summary>
Mismatch → `max(dp[2][3]=1, dp[3][2]=2) = 2`. "Drop 'd' from the right side"
keeps the `ac` match found at `dp[3][2]`. The answer inherits the best
nearby cell instead of resetting.
</details>

---

**← Prev** [06 — The backwards loop trick](06-the-backwards-loop-trick.md) ·
**Next →** [08 — Edit distance](08-edit-distance.md)
