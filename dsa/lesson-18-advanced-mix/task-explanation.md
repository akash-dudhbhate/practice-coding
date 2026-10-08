# Lesson 18 — Advanced Mix (Tries, Bits, Monotonic Stack)

## What you'll learn
- **Tries**: node = `{char: child}` + `is_end` flag; insert/search/startsWith — and why "is this a prefix of ANY word" in O(1)/char accelerates word searches
- **Bit manipulation**: `& | ^ ~ << >>`, the five tricks — `x & (x-1)` clears the lowest bit, XOR cancels pairs, `x & -x` isolates the lowest bit, power-of-2 test
- **Monotonic stack at depth**: next-greater family (each element pushed + popped once → O(n)), circular arrays (`range(2*n)`), largest-rectangle with a sentinel
- **Union-find recap**: dynamic connectivity — when it beats DFS (streaming edges, repeated "connected?" queries)
- **The clue table**: recognizing which advanced tool a problem wants

## Lesson

### Trie — a tree keyed by characters
```python
class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False          # "a full word ends here" — NOT just "path exists"
```
`search(w)` needs path + `is_end`; `startsWith(p)` needs only the path.

### Bit tricks
```python
x & (x - 1)      # clears lowest set bit → power-of-2 test: == 0
x & -x           # isolates lowest set bit → partition for two-singles
a ^ a == 0       # pairs cancel → single_number
1 << k           # 2**k
```

### Monotonic stack — indices of unresolved elements
```python
stack = []
for i, x in enumerate(nums):
    while stack and nums[stack[-1]] < x:   # x dominates the tops
        ans[stack.pop()] = x               # x is THEIR next-greater
    stack.append(i)
```

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels.

### Easy (start here) — bit tricks
1. `easy/p01-xor-single-number.py` — `single_number(nums)` → the one element appearing once (all others twice). O(1) space via XOR.
   `[4,1,2,1,2] → 4`; `[-1,-1,-2] → -2`.
2. `easy/p02-power-of-two-check.py` — `is_power_of_two(n)` → True iff n is a power of 2.
   `16 → True`; `0 → False`; `-8 → False`. One line: `n > 0 and n & (n-1) == 0`.
3. `easy/p03-count-set-bits.py` — `hamming_weight(n)` → number of 1-bits.
   `11 (1011) → 3`; `255 → 8`; `0 → 0`. Loop `n &= n-1`, count iterations.

### Medium — build the tools
4. `medium/p01-implement-trie.py` — class `Trie` with `insert(word)`, `search(word)`, `startsWith(prefix)`.
   Insert `"apple"` → `search("apple")=True`, `search("app")=False`, `startsWith("app")=True`. `is_end` vs path-existence is the whole point.
5. `medium/p02-xor-two-single-numbers.py` — `single_numbers(nums)` → list of the TWO elements appearing once (rest twice).
   `[1,2,1,3,2,5] → [3,5]` (order irrelevant). XOR all → `a^b`; split on `x & -x` lowest differing bit; XOR each group.
6. `medium/p03-next-greater-element-circular.py` — `next_greater_elements(nums)` → next greater for each index, circular (wrap around), `-1` if none.
   `[1,2,1] → [2,-1,2]`; `[5,4,3,2,1] → [-1,5,5,5,5]`. Loop `2*n`, index `i % n`, push only when `i < n`.

### Hard — combine tools
7. `hard/p01-word-search-trie.py` — `find_words(board, words)` → all words findable on the grid (4-directional, no cell reuse within a word), sorted.
   Build a trie of `words`; DFS cells and die early when the path isn't a prefix of anything. `board=[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words=["oath","pea","eat","rain"] → ["eat","oath"]`.
8. `hard/p02-max-xor-two-numbers.py` — `find_maximum_xor(nums)` → max `a ^ b` over pairs.
   `[3,10,5,25,2,8] → 28` (5^25). Bitwise trie; per number greedily take the opposite bit if it exists. O(32·n).
9. `hard/p03-largest-rectangle-histogram.py` — `largest_rectangle_area(heights)` → biggest rectangle inside the histogram.
   `[2,1,5,6,2,3] → 10`. Increasing-height stack of indices; pop on a shorter bar; width from new stack top; append a sentinel `0` to flush.

### How to work
- Read `concepts.md` first — the clue table maps problem smells to tools.
- Open a problem file, read the header, write your code under the TODO marker.
- Run `python3 check.py easy/p01` for one problem, `python3 check.py all` for all nine.
- `coding-check.md` is your manual checklist; `EXTRA-PRACTICE.md` has debug drills after you finish.
- Peek at `solutions/` only after a real attempt — then close it and redo from memory.
