# 10 — Permutations: the "Any Unused" Decision Tree

> 6-minute read. Same tree idea — different kind of choice.

## The idea, plain words

All *orderings* of `[1, 2, 3]` — that's `[1,2,3] [1,3,2] [2,1,3] [2,3,1]
[3,1,2] [3,2,1]`: six answers (`3!`).

The difference from subsets: the question at each level isn't "include or
skip?" — it's **"which unused element goes next?"** Position 1 has 3
choices, position 2 has 2 *remaining* choices, position 3 gets whatever's
left.

## The decision tree for [1, 2, 3] (same picture works for "abc")

```
                        []
              ┌─────────┼─────────┐
           pick 1     pick 2     pick 3
             [1]        [2]        [3]
           ┌──┴──┐    ┌──┴──┐    ┌──┴──┐
         then 2 then 3 ...  ...      ...
        [1,2]  [1,3]
         │       │
       [1,2,3] [1,3,2]  ...6 leaves total
```

Each node branches over **all still-unused** elements — so the fan-out
shrinks: 3 choices, then 2, then 1. Leaves = `3 × 2 × 1 = 6`. Depth is
still n; the branching is wider than subsets (n choices, not 2), which is
why `n!` dwarfs `2ⁿ` fast: `10!` = 3.6 million.

## The code — the classic mutating form

```python
def permutations(nums):
    out = []
    def dfs(path, used):
        if len(path) == len(nums):          # placed every element — leaf
            out.append(path.copy())         # COPY — same lesson as ch.09
            return
        for i in range(len(nums)):
            if used[i]:
                continue                    # element already in path — skip
            used[i] = True                  # CHOOSE: mark it taken
            path.append(nums[i])
            dfs(path, used)                 # EXPLORE the subtree
            path.pop()                      # UNCHOOSE: free it for siblings
            used[i] = False
    dfs([], [False] * len(nums))
    return out
```

`permutations([1, 2, 3])` → the six orderings above.

Here `used[i]` is the "chalk mark" — set before recursing, cleared after.
That clear step is the UNCHOOSE: without it, element `i` would stay
"taken" forever and the sibling branches would see it as unavailable.

Side by side with subsets:

| | subsets | permutations |
|---|---|---|
| choice per level | include / skip (2) | which unused element (shrinks) |
| leaf reached when | all positions decided | path is full |
| answer count | `2ⁿ` | `n!` |

## Why it exists

Whenever "all arrangements/orderings" appears — seating charts, playlists,
permutation ciphers, `itertools.permutations` under the hood — this is the
skeleton. `medium/p03` (letter-case permutation) is the same tree with a
2-way "lower or upper" fork per letter.

## Common mistake

Forgetting `used[i] = False` after the call. The element stays marked, so
downstream branches can't pick it — you get *some* permutations with
mysterious holes instead of all n!. Mark and unmark must bookend the call,
always.

## Your turn

`permutations([1, 2])` — draw or picture the tree. How many levels, how
many leaves, what are they?

<details><summary>Answer</summary>
Root `[]` → two children `[1]`, `[2]` → each has one remaining element →
leaves `[1,2]` and `[2,1]`. Depth 2, `2! = 2` leaves. The fan-out at the
root is 2, then 1.
</details>

---

**← Prev** [09 — Subsets](09-subsets-decision-tree.md) ·
**Next →** [11 — Enumerate or optimize?](11-enumerate-or-optimize.md)
