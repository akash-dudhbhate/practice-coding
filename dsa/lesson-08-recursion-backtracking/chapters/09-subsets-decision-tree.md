# 09 — Subsets: the Include/Skip Decision Tree

> 6-minute read. Your first real backtracking problem, drawn as a tree.

## The idea, plain words

"Give me every subset of `[1, 2]`" — that's `[[], [1], [2], [1,2]]`. Four
answers. How does code find all four?

Walk the input left to right. At each element, the problem forks into TWO
choices: **include it, or skip it.** Each choice is a recursive call on the
rest of the list.

## The decision tree for [1, 2]

Depth = which position you're deciding. At each node the left child
includes, the right child skips:

```
                      []
               put 1?  /  \  skip 1?
                    [1]    []
                2?/    \?  2?/    \?
               [1,2]   [1] [2]    []
                leaf   leaf leaf   leaf
```

Every **leaf** (where you've decided on every element) is one subset:
`[1,2]`, `[1]`, `[2]`, `[]`. n elements → 2 choices each → `2ⁿ` leaves.
For `[1,2,3]` that's 8 subsets — the answer set itself is exponential,
which is why backtracking (not a loop) is the right tool.

## The code — same tree, seven lines

```python
def subsets(nums):
    out = []
    def dfs(i, path):
        if i == len(nums):              # decided on every element — a leaf
            out.append(path.copy())     # record a COPY of this path
            return
        dfs(i + 1, path + [nums[i]])    # CHOICE A: include nums[i]
        dfs(i + 1, path)                # CHOICE B: skip it
    dfs(0, [])
    return out
```

`print(subsets([1, 2]))` → `[[1, 2], [1], [2], []]` — the four leaves, in
the order the tree visits them (include-first, left to right).

Note the shape: **two recursive calls per level** — that's the two branches
of the tree, literally. `dfs(0, [])` starts at the root with an empty path;
each call spawns its two children.

Here `path + [nums[i]]` builds a *fresh* list for the include-branch, so
no manual undo is needed. The classic form mutates one shared list —
`path.append(x)` → `dfs` → `path.pop()` — the choose/explore/unchoose from
chapter 08.

## Why it exists

Without the tree, "find all subsets" sounds like you need 4 separate
generators. The tree shows it's ONE process: n decision points, 2-way fork
at each, record every leaf. Reading problems as decision trees is the
*whole* backtracking skill — chapters 10-11 reuse it.

## Common mistake — THE #1 backtracking bug

```python
out.append(path)      # ← appends the LIST ITSELF, not a snapshot
```

`path` keeps mutating after you store it — every entry in `out` points at
the SAME list object, so all four "answers" end up equal to whatever `path`
looks like at the end (usually `[]`). Always `path.copy()` — or build
fresh lists with `path + [x]`.

## Your turn

How many subsets does `[1, 2, 3, 4]` have, and what depth is the tree?

<details><summary>Answer</summary>
16 subsets (`2⁴`), tree depth 4 — one decision level per element. Depth
never exceeds n, so the call stack stays tiny even though the answer set
doubles with each element.
</details>

---

**← Prev** [08 — Choose, explore, unchoose](08-backtracking-choose-explore-unchoose.md) ·
**Next →** [10 — Permutations: the "any unused" tree](10-permutations-decision-tree.md)
