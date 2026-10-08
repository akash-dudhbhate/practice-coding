# Lesson 04 — Concepts Explained (Two Pointers)

> Read this before solving the problems. Each concept explains:
> **What it is** · **Why it exists** · **Where it's used** · **What goes wrong** without it.
> Then a worked example with real numbers, code, and expected output.

---

## What the Two-Pointer Pattern Is

**What it is:** Instead of nested loops that compare every pair of elements, keep
two indices ("pointers") into the array/string and move them by rules. Each step
eliminates work — the pointers only move forward (toward each other, or both
rightward), never restart. One pass, O(n).

```
nums = [1, 3, 5, 7, 9]
        L           R        <- left at start, right at end
        move L -> / <- R based on what you see
```

**Why it exists:** Brute-force pair problems are O(n²) because they re-look at
everything. Two pointers exploit *structure* — sortedness, symmetry, or
read/write roles — so each comparison throws away a whole row or column of the
search space.

**Where it's used:** Reversals, palindromes, pair-sum on sorted arrays, in-place
dedup/compaction, merging sorted data, and it powers 3-sum, container-with-water,
and trapping-rain-water.

**What goes wrong without it:**
- Nested loops: n = 10⁵ → ~5·10⁹ comparisons → timeouts.
- Making copies: `s[::-1]` or building a new list uses O(n) extra space when the
  task says "in place".
- Moving BOTH pointers unconditionally — the power comes from moving exactly the
  pointer that can't produce a better answer.

**Worked example (real numbers):** is "racecar" a palindrome?

```
L=0 'r'  R=6 'r'  match -> L=1, R=5
L=1 'a'  R=5 'a'  match -> L=2, R=4
L=2 'c'  R=4 'c'  match -> L=3, R=3 -> L>=R, done: palindrome
```

```python
def is_palindrome(s):
    L, R = 0, len(s) - 1
    while L < R:
        if s[L] != s[R]:
            return False
        L += 1
        R -= 1
    return True

print(is_palindrome("racecar"))
print(is_palindrome("hello"))
```

Expected output:
```
True
False
```

---

## Opposite-End Pointers (Meet in the Middle)

**What it is:** Start `left` at index 0 and `right` at the last index; move them
toward each other until they cross. Each iteration compares or combines the two
ends — perfect for symmetric questions (palindrome, reversal) and sorted pair
search.

```python
left, right = 0, len(arr) - 1
while left < right:
    # compare or swap arr[left], arr[right]
    left += 1
    right -= 1
```

**Why it exists:** If the answer depends on the two ends being consistent
(palindrome) or on a pair anywhere in the array (pair-sum), walking inward visits
every relevant pair exactly once.

**Where it's used:** `reverse in place`, palindrome checks, pair-sum on sorted
input, container-with-most-water, trapping rain water.

**What goes wrong without it:**
- `while left <= right` on reversal swaps the middle element with itself —
  harmless on strings but a real bug when swapping different slots. Use `<`.
- Forgetting to move BOTH pointers → infinite loop.
- On unsorted data, "which pointer do I move?" has no correct answer — the
  pattern needs structure to decide.

**Worked example (real numbers):** reverse `[1, 2, 3, 4]` in place.

```
swap arr[0]<->arr[3]:  [4, 2, 3, 1]
swap arr[1]<->arr[2]:  [4, 3, 2, 1]
L=2, R=1 -> stop
```

Expected output: `[4, 3, 2, 1]`

---

## Sorted Pair-Sum: Why Sortedness Unlocks It

**What it is:** On a *sorted ascending* array, the pair `[L, R]` tells you
everything: if `arr[L] + arr[R] < target`, then `arr[L]` is too small to pair
with ANY element at or before R — discard it (`L += 1`). If the sum is too big,
`arr[R]` is too big for everyone — discard it (`R -= 1`). Each step removes one
candidate for good.

```python
def pair_sum_sorted(nums, target):
    L, R = 0, len(nums) - 1
    while L < R:
        s = nums[L] + nums[R]
        if s == target:
            return [L, R]
        if s < target:
            L += 1        # nums[L] can't work with anything left
        else:
            R -= 1        # nums[R] can't work with anything left
    return []
```

**Why it exists:** Sorted order gives a *direction to blame*: too small → the
small end is at fault; too big → the big end is at fault. Unsorted, you can't
blame either end — you'd have to try everything (back to O(n²) or hashing).

**Where it's used:** Pair-sum on sorted data, and it's the inner engine of
3-sum / 4-sum (fix one element, two-pointer the rest).

**What goes wrong without it:**
- On unsorted input this silently returns wrong answers — sort first (but sorting
  destroys original indices — store `(value, index)` pairs if you need them).
- When `s < target`, decrementing R is WRONG — the sum is already too small, and
  R is the biggest remaining element. Only L can fix it. Same logic reversed for
  `s > target`.

**Worked example (real numbers):** `nums = [1, 2, 4, 7, 11]`, `target = 9`.

```
L=0(1) R=4(11)  sum=12 > 9   -> R=3   (11 too big for everyone)
L=0(1) R=3(7)   sum=8  < 9   -> L=1   (1 too small for everyone)
L=1(2) R=3(7)   sum=9  ==    -> return [1, 3]
```

Expected output: `[1, 3]`

---

## Same-Direction Pointers (Fast/Slow, Read/Write)

**What it is:** Both pointers move left → right, but at different jobs: `fast`
(or `read`) scans every element; `slow` (or `write`) marks where the next
*keeper* goes. When `fast` sees a value worth keeping, write it at `slow` and
advance `slow`. Everything left of `slow` is your compacted answer — in place,
O(1) extra space.

```python
slow = 0
for fast in range(len(nums)):
    if nums[fast] should_be_kept:
        nums[slow] = nums[fast]
        slow += 1
# answer lives in nums[:slow]; slow is the new length
```

**Why it exists:** "Remove/compaction" problems naively create a new array
(O(n) space) or call `.remove()` (O(n) shift each → O(n²)). The write-pointer
trick compacts in one pass, in place, and hands you the new length.

**Where it's used:** Remove duplicates from a sorted array, move zeros to the
end, remove a value in place, partition-by-condition — the standard "return new
length, first k elements valid" interview format.

**What goes wrong without it:**
- Building a new list when the problem says *in place* — you burn O(n) space and
  the caller's array never changes.
- The elements AFTER index `slow-1` are garbage — the answer is `nums[:slow]`,
  not `nums`. Forgetting this makes stale tail values look like real data.
- On UNSORTED input, "skip duplicates" needs a seen-set; same-direction dedup
  only works because sorted order puts equals adjacent.

**Worked example (real numbers):** dedup `[0, 0, 1, 1, 2]` in place.

```
fast=0: nums[0]=0  first elem, keep        -> slow=1   [0, _, _, _, _]
fast=1: nums[1]=0  == nums[0] skip
fast=2: nums[2]=1  != nums[0] write@1      -> slow=2   [0, 1, _, _, _]
fast=3: nums[3]=1  == nums[1](now 1) skip
fast=4: nums[4]=2  != nums[1] write@2      -> slow=3   [0, 1, 2, _, _]
return 3, array prefix [0,1,2]
```

```python
def remove_duplicates(nums):
    if not nums:
        return 0
    slow = 1
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow - 1]:
            nums[slow] = nums[fast]
            slow += 1
    return slow

arr = [0, 0, 1, 1, 2]
k = remove_duplicates(arr)
print(k, arr[:k])
```

Expected output:
```
3 [0, 1, 2]
```

---

## Two Pointers vs Hashing — the Space Tradeoff

**What it is:** Two-sum on UNSORTED data → hashing, O(n) space. On SORTED data →
two pointers, O(1) space. Same O(n) time, different memory bill. When the input
is already sorted — or you're allowed to sort and don't need original indices —
two pointers win the space.

| | Hashing | Two pointers (sorted) |
|---|---|---|
| Time | O(n) | O(n) (after sort: O(n log n)) |
| Extra space | O(n) | O(1) |
| Keeps indices | yes | must store (value,index) pairs |
| Needs | nothing | sorted input |

**Why it exists:** Interviews love this tradeoff question. "Can you do it in O(1)
space?" is the follow-up that hashing can't answer.

**Where it's used:** Memory-constrained contexts, already-sorted inputs, and any
in-place requirement (reversal, dedup, merge) where a hash map is banned.

**What goes wrong without it:**
- Sorting to save space destroys index order — if the answer needs original
  indices, you must carry them: `sorted((v, i) for i, v in enumerate(nums))`.
- Two pointers on unsorted data gives wrong answers *silently* — no error, just
  a missed pair. Confirm the sorted precondition first.

---

## When NOT to Use Two Pointers

**What it is:** The pattern fails when there's no rule telling you which pointer
to move — i.e., no exploitable order or symmetry.

**Don't reach for it when:**
- The array is unsorted AND pair order matters / indices needed → hashing.
- You need ALL pairs, not one → two pointers find one answer per outer step
  (fine for counting problems it was designed for, wrong for "list every pair"
  in general).
- Elements can't be revisited cheaply (streams) and the pointers need random
  access — linked lists need the slow/fast variant, not index pointers.
- The "pair" relationship isn't monotone — two pointers rely on
  `sum too small → move left` style reasoning that requires sorted input.

**What goes wrong:** applying opposite-end pointers to `[3, 0, 5, 1]` target=4
concludes "no pair" after shrinking — but `3+1=4` exists. No error, just a wrong
answer. That's the dangerous failure mode.

---

## Escalating the Pattern (3-Sum, Containers, Merge, Rain Water)

**What it is:** The same core loops combine into the classic hard problems:

- **3-sum:** sort, fix `nums[i]`, run sorted pair-sum on `nums[i+1:]` for
  `-nums[i]`. Skip duplicate i's and duplicate pairs. O(n²).
- **4-sum:** sort, fix TWO outer elements `nums[i], nums[j]`, two-pointer the
  rest. O(n³).
- **Container with most water:** L and R at the ends; area = min(h[L],h[R])·(R-L).
  The shorter side is the bottleneck — moving the taller side can't help, so
  move the shorter one inward. Greedy elimination, O(n).
- **Trapping rain water:** water at i = min(max_left, max_right) - h[i].
  Two pointers carry running `max_left`/`max_right`; process whichever side is
  lower — that's the side whose bound is known. O(n) time, O(1) space.
- **Merge two sorted arrays in place:** write pointer at the END of the buffer;
  compare the biggest remaining elements of both arrays, place the larger at the
  back, walk left. Backward = no overwriting unread values.

**Worked example (real numbers):** 3-sum on `[-1, 0, 1, 2, -1, -4]` → sort →
`[-4, -1, -1, 0, 1, 2]`.

```
i=0 (-4): need 4 from [-1,-1,0,1,2]  -> L=-1 R=2 sum=1; L=-1 R=2... max 1 -> none
i=1 (-1): need 1 from [-1,0,1,2]
            L=2(-1) R=5(2) sum=1 -> record (-1,-1,2)
            then (-1,0,1) also sums to 0? -1+0+1=0 -> record (-1,0,1)
i=2 (-1): duplicate of i=1 value -> skip
i>=3: nums[i] > 0 -> can stop early
```

Expected output:
```
[[-1, -1, 2], [-1, 0, 1]]
```

---

## Quick Reference

| Problem shape | Pointer style | Move rule |
|---|---|---|
| reverse / palindrome | opposite ends | both inward |
| pair-sum (sorted) | opposite ends | small→L++, big→R-- |
| dedup / compact in place | fast+slow | fast scans, slow writes |
| merge into buffer | from the back | biggest to the end |
| container / rain water | opposite ends | move the shorter side |
| 3-sum / 4-sum | fixed + pair | two-pointer per fixed element |
