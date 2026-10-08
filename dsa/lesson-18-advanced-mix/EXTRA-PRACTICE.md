# lesson-18-advanced-mix — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

> Don't run the code. Answer mentally first.

---

## Check 01: Which tool does this want?

Match each problem statement to trie / XOR / monotonic stack / union-find:

1. "Every number appears three times except one — find it in O(1) space."
2. "Return all dictionary words that can be spelled walking adjacent grid cells."
3. "For each day, how many days until a warmer temperature?"
4. "Edges arrive one per query; report the first edge that would create a cycle."
5. "Suggest completions as the user types each character."

<details><summary>Answer</summary>

1. Bit trick — but NOT plain XOR (three-fold pairs need bit-counting mod 3 per position, or a different trick). Recognizing "pairs cancel" → XOR is for *twice*. For thrice: count bits per position mod 3.
2. **Trie** — prefix pruning inside the DFS is the whole speedup.
3. **Monotonic stack** — "next position where X" is its signature.
4. **Union-find** — dynamic connectivity; `find(a) == find(b)` before unioning means cycle.
5. **Trie** — walk to the typed prefix node, collect `is_end` descendants.
</details>

---

## Check 02: Bit trace

What is `x & (x - 1)` for `x = 40`? And what does `x & -x` give?

<details><summary>Answer</summary>

`x = 40 = 101000`.
`x - 1 = 39 = 100111`.
`x & (x-1) = 100000 = 32` — cleared the lowest set bit.

`x & -x`: `-40` in two's complement = `...11011000`; AND with `101000` → `001000 = 8` — the lowest set bit *isolated*.

Same bit, two views: `x & (x-1)` erases it, `x & -x` extracts it.
</details>

---

## Check 03: Trie semantics

```python
trie = Trie()
trie.insert("apple")
print(trie.search("app"), trie.startsWith("app"), trie.search("apples"))
```

<details><summary>Answer</summary>

`False True False`.

- `search("app")` — the path a→p→p exists but `is_end` there is False (only "apple" was inserted) → **False**.
- `startsWith("app")` — path existence only → **True**.
- `search("apples")` — walking 's' from the 'e' node fails → **False** (and `startsWith("apples")` would also be False — the path itself dies).
</details>

---

## Check 04: Stack trace

`next_greater_elements([5,4,3,2,1])` — circular. Which index resolves first on the SECOND pass, and with what value?

<details><summary>Answer</summary>

First pass pushes all five indices (strictly decreasing — nothing pops). Stack: `[0,1,2,3,4]` with values `5,4,3,2,1`.

Second pass, `i=5` → `i % n = 0` → value `5`: pops index 4 (value 1) → `ans[4]=5`; pops 3 (`ans[3]=5`), 2 (`ans[2]=5`), 1 (`ans[1]=5`); stops at index 0 (`5 < 5` false). Index 4 resolves FIRST with value 5.

Final: `[-1, 5, 5, 5, 5]` — index 0's own 5 never pops (nothing strictly greater exists).
</details>

---

## Check 05: Does the partition trick still work?

`single_numbers([4,4,7,7,3,1])` — XOR-all gives `3 ^ 1 = 2`. Splitting on bit `2`: which groups form, and does each contain exactly one loner?

<details><summary>Answer</summary>

`xor_all = 2` (binary 010) — 3 (`011`) and 1 (`001`) differ in bit 1.

- Group "bit 1 set": 4? `100` no. 7? `111` yes ×2. 3? `011` yes. → `{7,7,3}` → XOR = **3**.
- Group "bit 1 clear": 4,4 → XOR = 0; 1 → **1**.

Each group holds exactly one loner (they differ in this bit by construction) plus only duplicate pairs → XOR per group recovers `[3, 1]`. ✓
</details>

---

## Debug Exercises — find and fix the bug

> Fix the broken code. Find bugs mentally before running.

---

## Debug 01 (Easy): Power of two — missing the guard

```python
def is_power_of_two(n):
    return (n & (n - 1)) == 0
```

**Hint:** What's `is_power_of_two(0)`? Is 0 a power of two?

<details><summary>Answer</summary>

**Bug:** `0 & -1 == 0` → returns `True` for 0 (and for negatives the Python bit pattern gets weird). 0 is not a power of two.
**Fix:** `return n > 0 and (n & (n - 1)) == 0`.
</details>

---

## Debug 02 (Medium): Trie — `is_end` vs path existence

```python
class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False
    def search(self, word):
        node = self
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return True               # BUG: path exists ≠ word inserted
```

**Hint:** Insert `"apple"`, then `search("app")`.

<details><summary>Answer</summary>

**Bug:** returns True for any *prefix* of an inserted word — `search("app")` is True after only `"apple"` inserted. That's `startsWith`'s job.
**Fix:** `return node.is_end` — the flag is what separates "word" from "path".
</details>

---

## Debug 03 (Medium): Circular next-greater — pushing twice

```python
def next_greater_elements(nums):
    n = len(nums)
    ans = [-1] * n
    stack = []
    for i in range(2 * n):
        j = i % n
        while stack and nums[stack[-1]] < nums[j]:
            ans[stack.pop()] = nums[j]
        stack.append(j)               # BUG: pushes on pass 2 as well
    return ans
```

**Hint:** Trace `[1,2,1]` — what lands on the stack during pass 2?

<details><summary>Answer</summary>

**Bug:** pass 2 re-pushes indices — the same index can appear twice and later resolve *itself* or get overwritten inconsistently (`ans` writes race). On `[5,4,3,2,1]`, index 0 gets pushed twice; a later 5 would resolve index 0 to... itself-as-answer chaos.
**Fix:** only push during the first lap:
```python
if i < n:
    stack.append(i)
```
Pass 2 exists solely to pop leftovers with wraparound values.
</details>

---

## Debug 04 (Hard): Word search — not restoring the cell

```python
def dfs(r, c, node):
    ch = board[r][c]
    if ch not in node:
        return
    nxt = node[ch]
    if '#' in nxt:
        found.append(nxt['#']); del nxt['#']
    board[r][c] = '.'                 # visited mark
    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
        nr, nc = r+dr, c+dc
        if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != '.':
            dfs(nr, nc, nxt)
    # BUG: never restores board[r][c] = ch
```

**Hint:** A word that ends mid-board leaves its path permanently blocked.

<details><summary>Answer</summary>

**Bug:** cells stay `'.'` after the DFS returns — later searches can't pass through them, silently deleting valid words. Board `[["a","b"],["c","d"]]`, words `["ab","ba"]`: after "ab" is found, 'a' and 'b' remain blocked if the restore is missing in the right place — "ba" becomes unreachable.
**Fix:** restore after the recursion:
```python
board[r][c] = ch                    # backtrack — unmark
```
</details>

---

## Common Mistakes — the traps learners hit

---

## Mistake 01: `n & (n-1)` on negatives / forgetting `n > 0`
```python
# WRONG — 0 passes, negatives loop forever in while n
return (n & (n-1)) == 0

# CORRECT
return n > 0 and (n & (n - 1)) == 0
```

## Mistake 02: `search` returning path-existence
```python
# WRONG — "app" found after only "apple" inserted
return True

# CORRECT — a word exists only where is_end says so
return node.is_end
```

## Mistake 03: Values on the stack instead of indices
```python
# WRONG — can't answer "how many positions away" / "how wide"
stack.append(nums[i])

# CORRECT — index on stack, value read through it
stack.append(i)
... nums[stack[-1]] ...
```

## Mistake 04: `if` where `while` belongs (again)
```python
# WRONG — one new element can dominate MANY tops
if stack and nums[stack[-1]] < x:
    ans[stack.pop()] = x

# CORRECT — pop everything x dominates
while stack and nums[stack[-1]] < x:
    ans[stack.pop()] = x
```

## Mistake 05: No sentinel/flush for the histogram
```python
# WRONG — increasing heights never pop: [2,4] leaves both unresolved
for i in range(len(heights)): ...

# CORRECT — sentinel 0 forces every pending bar to finalize
for i in range(len(heights) + 1):
    cur = heights[i] if i < len(heights) else 0
```

## Mistake 06: Splitting two-singles on a bit where they DON'T differ
```python
# WRONG — any set bit of xor_all is a bit where a,b differ; using bit 0
# (or a bit not in xor_all) puts them in the SAME group → both cancel to 0
diff = 1

# CORRECT — take a bit that IS in xor_all (the lowest one is easiest)
diff = xor_all & -xor_all
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Binary-string bit counting
### Before
```python
def hamming_weight(n):
    return bin(n).count("1")
```
### Problems
1. Converts the whole integer to a string — O(bits) time + O(bits) space, and dodges the concept being taught.
2. `bin(-n)` includes a `'-'` and sign games on negatives.

### After
```python
def hamming_weight(n):
    n &= 0xFFFFFFFF                  # treat as unsigned 32-bit (handles negatives)
    count = 0
    while n:
        n &= n - 1                   # erase lowest set bit — one iteration per 1-bit
        count += 1
    return count
```

---

## Refactor 02 (Medium): Trie with explicit node class overhead
### Before
```python
class TrieNode:
    def __init__(self):
        self.children = [None] * 26     # array — breaks on any char beyond a-z
        self.is_end = False
```
### Problems
1. Hardcoded 26 slots — silently fails on digits/uppercase.
2. Index math `ord(c) - ord('a')` scattered through every method.

### After
```python
class Trie:
    def __init__(self):
        self.children = {}            # dict — any character works
        self.is_end = False
```
A `dict` of children is the general version; the 26-array is a micro-optimization for the lowercase-only special case.

---

## Refactor 03 (Hard): Max-XOR — O(n²) to bitwise trie
### Before
```python
def find_maximum_xor(nums):
    best = 0
    for a in nums:
        for b in nums:
            best = max(best, a ^ b)
    return best
```
### Problems
1. O(n²) — n = 10⁵ is ~10¹⁰ XORs. Dead.
2. Re-checks every pair symmetrically.

### After
```python
def find_maximum_xor(nums):
    if len(nums) < 2:
        return 0
    L = max(nums).bit_length()
    trie = {}
    for num in nums:                        # insert: path of bits, MSB first
        node = trie
        for i in range(L - 1, -1, -1):
            node = node.setdefault((num >> i) & 1, {})
    best = 0
    for num in nums:                        # query: greedily prefer opposite bit
        node = trie
        cur = 0
        for i in range(L - 1, -1, -1):
            bit = (num >> i) & 1
            want = 1 - bit
            if want in node:
                cur |= 1 << i
                node = node[want]
            else:
                node = node[bit]
        best = max(best, cur)
    return best
```
O(32·n) — the "opposite bit first" greedy works because a flipped high bit outweighs every lower bit combined.

---

## Approach Comparison — different ways to solve it

## Problem: Single number (one element appears once)

### Approach 1: XOR (this lesson)
```python
def f(nums):
    r = 0
    for x in nums:
        r ^= x
    return r
```
**O(n) time, O(1) space.** Optimal.

### Approach 2: Hash set math — `2*sum(set) - sum(list)`
```python
def f(nums):
    return 2 * sum(set(nums)) - sum(nums)
```
**Pros:** cute one-liner. **Cons:** builds a set (O(n) space), overflow-free in Python but not in fixed-width languages.

### Approach 3: Counter / sorting
```python
# Counter(nums) then scan for count==1 — O(n) space
# or sort then check pairs — O(n log n), destroys input order
```
**Pros:** obvious. **Cons:** both violate the "O(1) space" follow-up — the question exists to force XOR.

**Winner:** Approach 1. In interviews say the XOR invariant out loud: commutative + `a^a=0` → pairs annihilate.

---

## Problem: Largest rectangle in histogram

### Approach 1: Monotonic stack (this lesson)
```python
def f(heights):
    stack, best = [], 0
    for i in range(len(heights) + 1):
        cur = heights[i] if i < len(heights) else 0   # sentinel flushes
        while stack and heights[stack[-1]] > cur:
            h = heights[stack.pop()]
            left = stack[-1] + 1 if stack else 0
            best = max(best, h * (i - left))
        stack.append(i)
    return best
```
**O(n)** — each bar pushed once, popped once.

### Approach 2: For each bar, expand outward to first-smaller on each side
```python
# precompute left[i], right[i] via two monotonic-stack passes → same idea,
# more code; or naive expand → O(n²)
```
**Pros:** the expand-outward version is intuitive. **Cons:** naive is O(n²); the two-pass version is the same algorithm written longer.

### Approach 3: Divide & conquer on the minimum bar
```python
# area = max(min_height * width, recurse_left, recurse_right)
```
**Pros:** elegant recursion. **Cons:** worst case O(n²) on sorted input (min is always at the edge); O(n log n) only with a sparse table.

**Winner:** Approach 1 — the single-pass stack IS the canonical answer; know the sentinel trick.
