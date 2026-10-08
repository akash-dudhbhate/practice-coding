# 40 — `a = [[]]*3; a[0].append(1)` — what prints and why (aliasing)

> **Interview question:** "What does `a = [[]]*3; a[0].append(1); print(a)` output, and why?"
> **What the interviewer is really testing:** Whether you understand that `*` copies *references*, not objects — the classic mutable-aliasing trap.

## Theory — what it is

`[[]] * 3` does **not** create three empty lists. It creates **one** empty list, then builds a new list containing three references (pointers) to that same object. All three slots point at a single shared `[]` — this is called **aliasing**: multiple names/refs for one object.

So `a[0].append(1)` mutates the one shared list. Since `a[1]` and `a[2]` are the same object, printing `a` shows `[[1], [1], [1]]`. The multiplication operator copies the *container's contents* — and the contents were a reference. Shallow copy, not deep copy.

The fix: `[[] for _ in range(3)]` — a list comprehension evaluates the expression `[]` fresh on each iteration, creating three genuinely separate lists. The same trap bites with `[0]*3` too... except it doesn't *visibly* bite, because ints are immutable — you can't `.append` to them, so the aliasing never shows. It's still aliasing; it just doesn't matter.

## Why it was needed

This isn't a feature "needed" — it's the natural consequence of Python's object model, and the interview is checking whether you've internalized it. In Python, **variables are name tags, not boxes**. Assignment and `*` copy tags, never the object behind them. `b = a` doesn't copy `a`; both names point at one list.

The model is deliberate: copying every nested object on every operation would be slow and memory-hungry. Python gives you cheap reference semantics by default and explicit tools when you want real copies — `list.copy()`, `copy.copy()` (shallow: new outer, shared inner), `copy.deepcopy()` (fully independent). The trap is that `*` *looks* like it should multiply the object, but it multiplies references to it.

## Where it's used in a real project

- **Matrices/grids:** `grid = [[0]*n]*m` — the classic bug; every row is the same row. Correct: `[[0]*n for _ in range(m)]` (inner `[0]*n` is safe — ints immutable).
- **Game boards / DP tables:** same pattern, same bug — `dp[i][j] = x` appears to write "everywhere."
- **Default dict-of-lists substitute:** `buckets = [[]]*10` then `buckets[h].append(x)` puts everything in one bucket. Use `defaultdict(list)` or a comprehension.
- **Any nested mutable default:** `[{}]*3`, `[[None]]*5`, lists of objects in init code — same aliasing everywhere.

## Diagram

```
a = [[]] * 3        ONE inner list object, three references to it:

a -> [ ref, ref, ref ]
       |    |    |
       +----+----+--> [ ]   <--- single shared list object

a[0].append(1) mutates THE list:   [1]

print(a) -> [[1], [1], [1]]   (all three refs see the same object)

vs  a = [[] for _ in range(3)]:
a -> [ ref1, ref2, ref3 ]
        |     |     |
        v     v     v
       [ ]   [ ]   [ ]        three separate objects
```

## Code — explained

```python
a = [[]] * 3          # one inner list; three refs to it
a[0].append(1)
print(a)              # [[1], [1], [1]]  <- surprise!

print(a[0] is a[1])   # True — literally the same object

b = [[] for _ in range(3)]   # three separate lists
b[0].append(1)
print(b)              # [[1], [], []]   <- what you wanted
print(b[0] is b[1])   # False

c = [0] * 3           # aliasing exists but is harmless — ints immutable
c[0] = 9              # rebinds slot 0; doesn't "mutate" the int
print(c)              # [9, 0, 0]
```

1. `[[]]*3` evaluates `[]` **once** — one object created, three copies of its reference.
2. `a[0].append(1)` mutates that single object; every slot sees it.
3. `is` confirms identity — `a[0]` and `a[1]` are the same object in memory.
4. The comprehension evaluates `[]` per-iteration — three objects.
5. `c[0] = 9` on the int list is *rebinding* (putting a new object in slot 0), not mutation — so no shared-state surprise.

## Problems

### Easy — predict the output
**Problem:** What prints?
**Try this input:** `x = [[0] * 2] * 2; x[0][0] = 7; print(x)`
**Expected output:** `[[7, 0], [7, 0]]`
**Solution:**
```python
x = [[0] * 2] * 2     # outer *2 aliases the SAME inner list
x[0][0] = 7           # mutates the shared inner list
print(x)              # [[7, 0], [7, 0]]
```
**Logic explained:**
1. `[0]*2` is safe — ints are immutable, aliasing invisible.
2. `[[0]*2]*2` copies the *reference* to the inner list — `x[0]` and `x[1]` are one object.
3. `x[0][0] = 7` mutates it; `x[1]` sees the change. Correct version: `[[0]*2 for _ in range(2)]`.

### Medium — fix the bucket bug
**Problem:** This code tries to distribute numbers into 3 buckets by `n % 3`, but every number lands everywhere. Fix it.
**Try this input:** `nums = [0, 1, 2, 3, 4, 5]`
**Expected output:** `[[0, 3], [1, 4], [2, 5]]`
**Solution:**
```python
def bucket(nums):
    buckets = [[] for _ in range(3)]   # was [[]]*3 — one shared list
    for n in nums:
        buckets[n % 3].append(n)
    return buckets

print(bucket([0, 1, 2, 3, 4, 5]))
# [[0, 3], [1, 4], [2, 5]]
```
**Logic explained:**
1. Buggy `buckets = [[]]*3` makes all buckets one list — output would be `[[0,1,2,3,4,5]] * 3`.
2. The comprehension creates three independent lists.
3. Now `buckets[n % 3].append(n)` writes to exactly one bucket.

### Hard — deep-copy a matrix correctly
**Problem:** You get a template row and must build an `n x m` grid where each row is independent. Then modify one cell without touching others — implement and prove independence.
**Try this input:** `rows, cols = 3, 4`; set `grid[1][2] = "X"`
**Expected output:** only row 1 has `X`: `[[0,0,0,0],[0,0,'X',0],[0,0,0,0]]`
**Solution:**
```python
def make_grid(rows, cols):
    return [[0] * cols for _ in range(rows)]
    # inner [0]*cols fine (ints); outer comprehension -> new row each time

g = make_grid(3, 4)
g[1][2] = "X"
for row in g:
    print(row)
# [0, 0, 0, 0]
# [0, 0, 'X', 0]
# [0, 0, 0, 0]
print(g[0] is g[1])   # False — independent rows
```
**Logic explained:**
1. Outer `for _ in range(rows)` evaluates `[0]*cols` fresh per row — no shared rows.
2. `[0]*cols` inside is safe only because ints are immutable — nested mutables would re-create the trap one level down.
3. For nested mutable rows (e.g., each cell a list), you'd need `copy.deepcopy` or another comprehension layer.

## The 30-second interview answer

"It prints `[[1], [1], [1]]`. `[[]]*3` creates one inner list and copies the *reference* to it three times — all three slots alias the same object, so appending through any index mutates the shared list. Python copies references, never objects, which is why `b = a` also aliases. The fix is a list comprehension — `[[] for _ in range(3)]` — which evaluates `[]` fresh each iteration. Note `[0]*3` is *also* aliasing, but ints are immutable so it can't bite — which is why `[[0]*3 for _ in range(3)]` is the correct grid pattern."

## Follow-up trap

**"How do you actually copy a nested list?"** Three levels: `a.copy()` / `a[:]` — shallow copy (new outer list, inner objects still shared — the same trap one level down); `copy.deepcopy(a)` — fully recursive copy. Also expect: *"Does this apply to function default args?"* — yes! `def f(x=[])` is the same mutable-default aliasing bug; the list is created once at definition time. Fix: `def f(x=None): x = x or []`.
