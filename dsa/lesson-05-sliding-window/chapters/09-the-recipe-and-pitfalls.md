# 09 — The Recipe & the Pitfall Gallery

> 5-minute read. Recognition in 10 seconds, plus the five ways windows die.

## The recipe — three questions

When a new problem lands, ask in order:

1. **"Contiguous subarray/substring?"** If yes → sliding window is a
   candidate. (Non-contiguous → probably hashing, sorting, or two
   pointers.)
2. **"Is the size given (k)?"** → **fixed window**: build the first one,
   then slide with `+= enterer / −= leaver`, record every stop.
3. **"Longest or shortest satisfying a rule?"** → **variable window**:
   `for right`, shrink `left` with `while`, and record at the right
   moment:
   - *Longest valid* → `while invalid: shrink`, record **after** the loop.
   - *Shortest valid* → `while valid: record, shrink` inside the loop.

Then say the complexity out loud: **O(n) time** (each element enters and
leaves once), **O(1) or O(k) space** for the bookkeeping.

## The map — every problem in this lesson

```
fixed:  easy/p01 max k-sum · easy/p02 averages · easy/p03 count ≥ target
var., longest:  medium/p01 no-repeat · medium/p02 ones-with-flips
                hard/p02 k-distinct · hard/p03 fruit baskets (k=2)
var., shortest: medium/p03 min-subarray · hard/p01 min-window-substring
```

## The pitfall gallery — five ways windows go wrong

Check these in order when something's off:

**1. `if` where `while` belongs.** Shrinking once leaves the window still
invalid. `while` shrinks *until* the rule holds again (chapter 05).

**2. Recording at the wrong moment.** Longest: after the shrink loop.
Shortest: inside it. Fixed: every slide once `right >= k−1`.

**3. `left` moving backward.** In the last-seen-index version, guard the
jump:

```python
if c in last and last[c] >= left:    # the >= is load-bearing
    left = last[c] + 1
```

Without it, `"abba"` drags `left` back to a stale index and re-admits a
duplicate.

**4. Zombie keys.** `count[d] -= 1` leaving `0` makes `len(count)`
overcount distinct items → `del count[d]` at zero (chapter 06).

**5. Re-deriving state.** `sum(nums[left:right+1])`, `max(window)`,
slicing inside the loop — each is O(window size), quietly converting
O(n) back into O(n·k) (chapter 07). State changes by exactly one element
per pointer move, or you're brute force in disguise.

## Edge cases to always test

Empty input · `k > len` (fixed → `[]`/`0`) · `k == 0` (distinct problems →
0) · all-identical elements (`"bbbbb"` → 1) · all-negative numbers (never
init `best = 0` on a max problem) · impossible target (return `0`/`""`,
don't crash).

## Your turn — map before you code

For each of these, say *fixed or variable*, and for variable say *when
you'd record*:

1. Average of every 30-day stretch of sales.
2. Longest substring containing at most 2 distinct characters.
3. Shortest subarray whose sum reaches a target.

<details><summary>Answer</summary>
1. **Fixed** (k = 30): build, slide, divide by k each stop.
2. **Variable, longest**: `while len(count) > 2: shrink`; record **after**
   the shrink loop. (This is hard/p03 in disguise.)
3. **Variable, shortest**: `while sum >= target: record, shrink` — record
   *inside* the loop, squeezing (chapter 05).
</details>

## What you now know

You can: explain a window, price brute force vs sliding, run both fixed
and variable skeletons, keep a count dict honest, argue O(n) from pointer
movement, tell windows from two-pointers, and debug the five classic
failures. **That's the whole lesson.** Now open `easy/p01` and make the
window move.

---

**← Prev** [08 — Windows vs two-pointers](08-windows-vs-two-pointers.md) ·
Done with concepts? → Open `../task-explanation.md` and solve `easy/p01` next.
