# 11 — Leveling Up: the Pattern Compounds

> 5-minute read. Everything here is chapters 03–08 wearing a costume.

## The idea, plain words

The medium and hard problems aren't new patterns — they're the two you
already know, **combined or pointed in a new direction.** Four moves to
recognize:

- **3-sum / 4-sum** = sort → fix element(s) → run chapter-06 pair-sum on
  the rest.
- **Container / rain water** = opposite ends, but the move rule is
  "discard the shorter/weaker side."
- **Merge into a buffer** = read/write pointers walking **backward** so
  the writer never tramples unread data.

## 3-sum — `medium/p03`

Sort `[-1, 0, 1, 2, -1, -4]` → `[-4, -1, -1, 0, 1, 2]`. Fix `nums[i]`,
then pair-sum the slice after it for `−nums[i]`:

```
i=1, fix -1 → need +1 from the rest:
L → [-1, 0, 1, 2] ← R    (indexes 2..5)   -1 + 2 = 1 → triplet (-1,-1,2)
    L → [0, 1] ← R        step in          0 + 1 = 1 → triplet (-1,0,1)
```

The outer loop is O(n), the inner walk is O(n) → **O(n²)** — one n
better than the n³ triple loop. Skip duplicate fixed values and
duplicate pairs to keep triplets unique. 4-sum (`hard/p03`) = one more
fixed loop around the same core → O(n³).

## Container with most water — `medium/p02`

`L` and `R` at the ends of heights; water held = `min(h[L], h[R]) ×
(R − L)`. **Move the shorter side inward** — the short wall is the
bottleneck, so moving the tall one can't possibly help.

```
L → [1, 8, 6, 2, 5, 4, 8, 3, 7] ← R   area = min(1,7)×8 = 8,  L short → L++
    L → [8, 6, 2, 5, 4, 8, 3, 7] ← R   area = min(8,7)×7 = 49 ← best
         ...keep moving the shorter end; 49 wins
```

## Merge into a back-buffer — `hard/p02`

`nums1 = [1, 2, 3, 0, 0, 0]` (zeros = reserved room), `nums2 = [2, 5, 6]`.
Write pointer `W` starts at the **end** of nums1; compare the biggest
remaining elements and place the winner at the back:

```
[1, 2, 3, 0, 0, 0] ← W      compare 3 vs 6 → 6 wins → write@5
[1, 2, 3, 0, 0, 6] ← W      compare 3 vs 5 → 5 wins → write@4
[1, 2, 3, 0, 5, 6] ← W      compare 3 vs 2 → 3 wins → write@3
... → [1, 2, 2, 3, 5, 6]
```

Backward = the empty slots are exactly where you write; nothing unread
gets crushed. Chapter 08's rule ("writer chases reader") flipped around.

## Rain water — `hard/p01`

Water trapped at position i = `min(max_left, max_right) − h[i]`.
Opposite-end pointers carry running `max_left` and `max_right`; process
whichever side is **lower** — its bound is already known. One pass,
O(1) space. The full trace lives in `concepts-reference.md`.

## Why it exists

The pattern compounds because the cheap move-rules are reusable: sort
once and the blame rule handles pairs *inside* any loop; point the
writer backward and compaction works into a buffer's tail. Hard
problems are combinations, not inventions.

## Where it's used

| Problem | Which chapters' pattern |
|---|---|
| `medium/p01` dedup | ch. 07 |
| `medium/p02` container | ch. 03 + "move the weaker side" |
| `medium/p03` three-sum | ch. 06 inside a loop |
| `hard/p01` rain water | ch. 03 + carried bounds |
| `hard/p02` merge in place | ch. 08, backward |
| `hard/p03` four-sum | ch. 06 inside two loops |

## Common mistake

Reaching for a new technique when it's the old one rotated. Sort-first +
pair-sum inside a loop **is** 3-sum. If you catch yourself writing a
nested scan inside a sorted array, ask: "can two pointers walk this
instead?"

## Your turn

"Merge two sorted arrays, and `nums1` has zeros padded at the END for
extra room" — do the pointers start at the fronts or the backs?

<details><summary>Answer</summary>
**Backs.** Writing the largest remaining value at the back fills the
empty buffer without overwriting `nums1`'s real elements. Front-writing
would crush unread data (chapter 08's mistake, literal).
</details>

---

**← Prev** [10 — When two pointers fails](10-when-it-fails.md) ·
Done with concepts? → Open `task-explanation.md`, then solve `easy/p01`.
