# 08 — Backtracking = Recursion + Undo

> 5-minute read. The second half of the lesson starts here — and it's the
> same machinery plus one new move.

## The idea, plain words

**Backtracking** is recursion where each level makes a **choice**, explores
where it leads, then **undoes** the choice to try the next one.

Real-life version: **solving a maze with chalk.** At a junction you mark
"path A" and walk in. Dead end? Walk back, ERASE the mark, try "path B."
The maze looks untouched for each new attempt — but you keep a list of the
routes that reached the exit.

The pattern — three steps, always in this order:

```python
def backtrack(state):
    if done(state):
        results.append(state.copy())    # a full solution — record a COPY
        return
    for choice in available_choices:
        state.append(choice)            # 1. CHOOSE   — make the mark
        backtrack(state)                # 2. EXPLORE  — walk deeper
        state.pop()                     # 3. UNCHOOSE — erase the mark
```

## Watch the undo work, tiny version

```python
path = []

path.append("kitchen");  print("chose kitchen   →", path)
path.append("bedroom");  print("chose bedroom   →", path)
path.pop();              print("undid bedroom   →", path)
```

```
chose kitchen   → ['kitchen']
chose bedroom   → ['kitchen', 'bedroom']
undid bedroom   → ['kitchen']
```

One shared `path` list. Append on the way in, pop on the way out — so the
next sibling branch sees a clean slate. That's the "erase the chalk" step.

## Why it exists

"Generate ALL X" problems — all subsets, all orderings, all valid boards —
have exponentially many answers; there's no shortcut formula. The only way
is systematic enumeration: try every first choice, and under each, every
second choice, and so on.

And the call stack is the *perfect* undo journal: when a recursive call
returns, its frame dies — you're instantly back in the parent, holding the
parent's state. As long as you cleaned up your mark (`pop`), the next
choice starts fresh for free.

## Where it's used

`medium/` is built on this: subsets, permutations, letter-case
permutations. `hard/` adds constraint-checking (N-Queens, combination sum,
word search) — same skeleton, plus a "skip invalid choices" test. Also:
sudoku solvers, puzzle games, compilers.

## Common mistake

Mutating state but never restoring it. If you `append` and forget the
`pop`, the sibling branch inherits your leftovers — subsets comes back with
`[1,2]` junk inside what should be `[]`. Choose/explore/unchoose is a
THREE-part pattern; skipping step 3 is the classic beginner bug.

## Your turn

```python
state = []
state.append("a")
state.append("b")
state.pop()
state.append("c")
```

What is `state` now?

<details><summary>Answer</summary>
`["a", "c"]`. The pop removed `"b"`, then `"c"` landed in its place — as if
the `"b"` choice never happened. That visible "swap" IS backtracking in
miniature.
</details>

---

**← Prev** [07 — The three questions](07-the-three-questions.md) ·
**Next →** [09 — Subsets: the include/skip decision tree](09-subsets-decision-tree.md)
