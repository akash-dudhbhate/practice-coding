# Lesson 18 — Concepts Explained (Advanced Mix: Tries, Bits, Monotonic Stack)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.
> This is the "last 10%" toolkit — rarer in interviews than lessons 02–15, but each tool is *the* answer for its niche, and no general-purpose technique covers that niche well.

---

## Tries — a tree shaped like the alphabet

**What:** A trie (from "re**trie**val", pronounced "try") is a tree where each node holds a *character→child* map plus one boolean: `is_end` — "does a complete word terminate here?" Every path from the root spells a prefix; every `is_end` node spells an inserted word. The shared prefix of two words is stored **once**.

```
words: app, apple, cat, dog          (* = is_end node)

                 (root)
              /    |    \
             a     c     d
             |     |     |
             p     a     o
             |     |     |
             p*    t*    g*          "app" ends here — and keeps going
             |
             l                        "apple" continues below
             |
             e*
```

**Why it exists:** A `set` of words answers "is this exact word present" in O(word length) via hashing — but can't answer "is this *prefix* present" or "list every word starting with 'app'" without scanning everything. A trie walks prefix lookups character by character: `startsWith("app")` costs 3 node hops regardless of how many million words are stored.

**Where it's used:** Autocomplete/typeahead (walk to the prefix node, DFS beneath it for suggestions), spell-checkers, IP routing tables (longest-prefix match), dictionary-based board games — and word-search problems where you need "is this cell-path still a valid prefix of *any* word?" answered in O(1) per step.

**What goes wrong without it:**
- Word-search-with-a-dictionary: checking each of K words separately against the grid → you re-walk the same prefix paths thousands of times. A trie prunes: the moment a path isn't a prefix of *any* word, the DFS dies.
- Confusing `is_end` with "has children": after inserting only `"apple"`, `search("app")` must be **False** (the path exists but `is_end` is False) while `startsWith("app")` is **True**. That distinction IS the data structure.
- Using a fixed 26-slot array when keys aren't lowercase letters — a `dict` of children is more general and nearly as fast.

**Worked example — insert "app", then query:**

```
insert("app"):   root→a→p→p, mark second p is_end=True
search("app"):   walk a→p→p → node exists, is_end=True  → True
search("ap"):    walk a→p   → node exists, is_end=False → False
startsWith("ap"):walk a→p   → node exists               → True (is_end ignored)
```

```python
class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert(self, word):
        node = self
        for c in word:
            node = node.children.setdefault(c, Trie())
        node.is_end = True

    def _walk(self, s):                 # returns node at end of path, or None
        node = self
        for c in s:
            if c not in node.children:
                return None
            node = node.children[c]
        return node

    def search(self, word):
        node = self._walk(word)
        return node is not None and node.is_end

    def startsWith(self, prefix):
        return self._walk(prefix) is not None
```

Expected: after `insert("apple")` — `search("apple")` → **True**, `search("app")` → **False**, `startsWith("app")` → **True**.

---

## Bit Manipulation — operators, and the five classic tricks

**What:** Treating an integer as a bag of bits you can flip, shift, and mask directly. Six operators:

```
&  AND    1 only where BOTH bits are 1        12 & 10  → 1100 & 1010 = 1000 = 8
|  OR     1 where EITHER bit is 1             12 | 10  → 1100 | 1010 = 1110 = 14
^  XOR    1 where bits DIFFER                 12 ^ 10  → 1100 ^ 1010 = 0110 = 6
~  NOT    flips every bit (Python: ~x = -x-1)
<< shift left    ×2 per position              1 << 3 = 8
>> shift right   ⌊÷2⌋ per position            12 >> 2 = 3
```

**Why it exists:** Some problems are about *parity, membership, and flags* — and bits give you O(1) space answers that no array can match. XOR in particular has a magical property: **`a ^ a = 0` and `a ^ 0 = a`** — pairs cancel, a lone element survives. That's an O(1)-space "find the unpaired element" with no data structure at all.

**Where it's used:** Sets-as-integers (bitmask DP, small subsets), permission flags, compression/checksums, cryptography, the "single number" interview family, power-of-two and bit-count tests.

**What goes wrong without it:** You reach for `Counter`/`set` where a single XOR accumulator does it in O(1) space — technically passes, but you missed the point of the problem (interviewers ask "can you do it in constant space?" precisely to force the trick).

### The five classic tricks — with binary worked examples

**1. `x & (x-1)` clears the lowest set bit.** Subtracting 1 flips the lowest 1-bit to 0 and every bit below it to 1 — AND-ing wipes exactly that bit:

```
x   = 12 = 1100
x-1 = 11 = 1011
x & (x-1) = 1000 = 8        lowest 1-bit gone
```

Powers of 2 have exactly ONE set bit → `x & (x-1) == 0` iff x is a power of 2:

```
16 = 10000   15 = 01111   16 & 15 = 0      → power of 2
 6 = 00110    5 = 00101    6 & 5 = 4 ≠ 0   → not
```

**2. XOR cancels pairs.** Every element twice but one → XOR everything; pairs vanish, the loner remains:

```
[4,1,2,1,2]: 4 ^ 1 ^ 2 ^ 1 ^ 2 = 4 ^ (1^1) ^ (2^2) = 4 ^ 0 ^ 0 = 4
```

**3. `x & -x` isolates the lowest set bit.** Two's complement negation keeps the lowest 1 and flips everything above:

```
x  = 12 = ...001100
-x = -12 = ...110100      (flip all bits, add 1)
x & -x = 000100 = 4       ← exactly the lowest set bit
```

Used to split `a^b`: the two unpaired numbers differ in at least one bit — the lowest differing bit partitions the array into two groups, each containing one of them.

**4. Counting set bits by repeatedly clearing the lowest one:**

```
n = 11 = 1011
step 1: n & (n-1) → 1011 & 1010 = 1010   count=1
step 2:           → 1010 & 1001 = 1000   count=2
step 3:           → 1000 & 0111 = 0000   count=3  → three 1-bits ✓
```

**5. Shifts as cheap multiply/divide by powers of 2:** `1 << k` = 2ᵏ, `x >> k` = ⌊x / 2ᵏ⌋.

### Two singles, not one — the XOR partition

`single_numbers([1,2,1,3,2,5])` — every element twice except TWO (3 and 5). XOR all → `3 ^ 5 = 6 = 110`. The 1-bits of 6 are bits where 3 and 5 **differ**. Take the lowest differing bit (`6 & -6 = 2`) and partition the array by it: 3 and 5 land in *different* groups (one has the bit, the other doesn't), and every duplicate pair lands in the *same* group. XOR each group separately → each yields its loner.

```
group "bit 2 set":  3(011), 2(010), 2(010) → 3^2^2 = 3
other group:        1, 1, 5                → 1^1^5 = 5
answer: [3, 5]
```

### Maximum XOR — the bitwise trie

"Find max `a ^ b` over pairs in `nums`" is O(n²) brute-force. The trie version: insert every number as a path of bits (MSB first); then for each `x`, walk the trie choosing the **opposite** bit whenever it exists — greedy, because the most significant bit you can flip contributes more than all lower bits combined. Each walk is ≤ 32 steps → O(32·n).

```
nums = [3, 10, 5, 25, 2, 8]  →  answer 28 = 5 ^ 25
  5 = 00101, 25 = 11001 → xor = 11100 — every bit flipped where the
  partner had the opposite → max possible on those top bits.
```

**Why "prefer opposite bit" is greedy-optimal:** bit position `i` contributes `2^i` to the XOR. Even if every lower bit flips to 1, they sum to `2^i - 1` — strictly less than one higher bit. So at each level, grabbing a differing bit can never be beaten by any combination of lower bits. That's the whole correctness argument, and it's the same shape as every greedy proof in lesson 17: the local choice dominates.

**One more Python-specific gotcha:** `~x` is NOT "flip to unsigned" — Python defines `~x = -(x+1)`, so `~5 = -6`. For "invert within k bits" use `x ^ ((1 << k) - 1)`. And `>>` on negative numbers keeps the sign (`-8 >> 1 = -4`, arithmetic shift) — mask to fixed width first if you want logical shift.

```python
def single_number(nums):
    result = 0
    for x in nums:
        result ^= x          # pairs cancel; loner survives
    return result

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0
```

Expected: `single_number([4,1,2,1,2])` → **4** · `is_power_of_two(16)` → **True**, `is_power_of_two(0)` → **False** (the `n > 0` guard matters — `0 & -1 == 0` would lie).

---

## Monotonic Stack at Depth — "next greater" and friends

**What:** A stack kept *sorted* (usually decreasing) — you push indices/values, and **when a new element breaks the order, you pop everything it dominates and answer a question about the popped elements.** Each element is pushed once and popped once → O(n).

The two questions it answers:
- **Next greater element:** while the new value exceeds stack tops, pop them — the new value IS their next-greater.
- **Largest rectangle in a histogram:** keep *increasing* heights; when a shorter bar arrives, pop taller bars — the popped bar's rectangle ends here, and its left edge is the new stack top.

**Why it exists:** "For each element, find the next position where X" naively scans right per element → O(n²). The stack exploits that a popped element never needs re-checking: anything that would be its answer has already been found (that's why it was safe to pop).

**Where it's used:** Daily temperatures ("days until warmer"), stock span, next/previous greater-or-smaller element, largest rectangle / maximal rectangle, trapping rain water variants, circular arrays (run the loop twice).

**What goes wrong without it:**
- Pushing **values** when you need **indices** — width/distance questions ("how many days until warmer", "how wide is this rectangle") are impossible without indices.
- The circular-array trick (`for i in range(2*n)`, use `i % n`) with pushes on the second pass — push only when `i < n` or you corrupt the stack.
- Largest rectangle: forgetting the sentinel — heights `[2,4]` never pops during the loop; append a 0-height bar at the end to flush every pending rectangle.
- `while` vs `if` again: one new element may dominate MANY stack tops (`[5,4,3,2,1]` then a 6 pops all five).

**Worked example — next greater, `nums = [2,1,2,4,3]`:**

```
stack holds INDICES of unresolved elements (values decreasing)
i=0 (2): push 0            stack=[0]
i=1 (1): 2>1, push 1       stack=[0,1]
i=2 (2): nums[1]=1 < 2 → pop 1 → ans[1]=2
         nums[0]=2 < 2? no → push 2  stack=[0,2]
i=3 (4): pop 2 → ans[2]=4; pop 0 → ans[0]=4; stack empty; push 3
i=4 (3): 4>3, push 4       stack=[3,4]
end: leftovers → -1
answer = [4,2,4,-1,-1] ✓
```

```python
def next_greater(nums):
    ans = [-1] * len(nums)
    stack = []                          # indices, values decreasing top→bottom
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            ans[stack.pop()] = x        # x is that index's next-greater
        stack.append(i)
    return ans
```

Expected output for `next_greater([2,1,2,4,3])`: **[4,2,4,-1,-1]**

**Worked example — largest rectangle, `heights = [2,1,5,6,2,3]`:**

Keep a stack of indices with *increasing* heights. A shorter incoming bar pops taller ones — the popped bar's right edge is `i`, its left edge is just past the new stack top.

```
i=5, cur=3 < heights[4]=2? no — trace the pops at i=6 sentinel (cur=0):
stack = [0,1,4,5] heights 2,1,2,3? — cleaner trace:

i=0(2): push0   i=1(1): 2>1 pop0 h=2 w=1→2; push1
i=2(5): push2   i=3(6): push3
i=4(2): 6>2 pop3 h=6 w=1→6; 5>2 pop2 h=5 w=2→10; 1<2 push4
i=5(3): push5   i=6(cur=0 sentinel): pop5 h=3 w=1→3; pop4 h=2 w=4→8;
                pop1 h=1 w=6→6; stack empty
best = 10  (the 5-and-6 bars, 2 wide × 5 tall)
```

For a **circular** array, loop `i` over `range(2*n)` and read `nums[i % n]` — but only `stack.append` during the first `n` positions; the second pass exists purely to pop leftovers with wraparound answers.

---

## Union-Find Recap — when it beats DFS (brief)

You met union-find in lesson 14; here's the 60-second refresh and — more important — *when it wins*.

**What:** A forest-of-trees with two ops: `find(x)` → which set is x in (with **path compression** — every node on the path gets re-parented to the root), `union(a,b)` → merge the sets (with **union by rank** — shorter tree under taller). Amortized near-O(1) per op.

```python
parent = list(range(n)); rank = [0]*n
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]   # path halving
        x = parent[x]
    return x
```

**When it beats DFS:** the problem is about **dynamic connectivity** — edges/groups arriving over time and you must keep answering "are a and b in the same set?" or "did this edge create a cycle?" A DFS must re-run from scratch per query (O(V+E) each); union-find answers incrementally. Redundant-connection, number-of-provinces-on-stream, accounts-merge — all union-find signatures. DFS/BFS still wins for one-shot questions on a *static* graph ("count islands in this fixed grid").

**Tiny worked example — detecting a redundant edge:** edges `[[1,2],[1,3],[2,3]]` on 3 nodes. Union `[1,2]` → set {1,2}. Union `[1,3]` → set {1,2,3}. Edge `[2,3]`: `find(2) == find(3)` — already same set → **this edge is redundant** (adding it creates a cycle). Three near-O(1) queries instead of three DFS runs.

---

## The Clue Table — which advanced tool does this problem want?

| The problem smells like... | Reach for | This lesson |
|----------------------------|-----------|-------------|
| "prefix", "autocomplete", "words starting with", dictionary-driven search | **Trie** | medium/p01, hard/p01, hard/p02 (bitwise trie) |
| "every element appears twice except…", O(1) space required, parity/cancellation | **XOR tricks** | easy/p01, medium/p02 |
| count/isolate bits, power of two, bitmask over ≤ 20 items | **Bit manipulation** | easy/p02, easy/p03 |
| "next greater/smaller", "days until", span, largest rectangle | **Monotonic stack** | medium/p03, hard/p03 |
| "are a and b connected" as edges stream in, "does this edge make a cycle" | **Union-find** | (recap — problems were lesson 14) |
| top-K, streaming median | **Heap** (lesson 12) | — |
| longest/shortest contiguous window | **Sliding window** (lesson 5) | — |

Two extra recognition heuristics: **"pairs cancel / find the odd one out" → XOR** is nearly deterministic. **"for each element, next/first position where…" → monotonic stack** nearly as much. When a hard problem combines a grid DFS with a word list, the trie is the accelerant — plain DFS×words is the TLE.

---

## The Pitfall Gallery — five ways these tools go wrong

**1. Python's infinite sign bits.** Python ints are arbitrary precision: `-1` is "…infinite 1s". `x & (x-1)` loops forever on negatives, and bit-reversal on negatives needs a mask. When a problem says "32-bit integer," say it in code: `n &= 0xFFFFFFFF`.

**2. `is_end` vs "node exists".** `startsWith` checks path existence; `search` checks path existence AND `is_end`. Conflating them makes `search("app")` lie after only `"apple"` was inserted.

**3. Not restoring the board in word-search DFS.** Mark a cell visited (`'#'`), recurse, then **put the original letter back** — other paths must be allowed through that cell.

**4. Values vs indices on the monotonic stack.** "How far until the next greater" and "how wide is the rectangle" need *positions*. Push indices; read values via `nums[stack[-1]]`.

**5. Forgetting to flush the stack.** Largest-rectangle: bars still on the stack at the end never got their right edge computed. Append a sentinel `0` so every pending bar pops.

**Edge cases to always test:** empty array/single element, all-same-values, negative numbers in bit problems, words that are prefixes of other words (`"app"`/`"apple"`), single-row histograms, and grid words longer than the board can spell.
