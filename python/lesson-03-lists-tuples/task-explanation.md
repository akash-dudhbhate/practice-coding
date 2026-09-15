# Lesson 03 — Lists & Tuples

## What you'll learn
- Creating and accessing lists and tuples.
- Mutating lists with `append`, `insert`, `pop`, `remove`.
- Sorting and reversing collections.
- The difference between mutable lists and immutable tuples.
- Unpacking and iterating safely.

## Lesson

Lists and tuples are Python's ordered collections. Lists change; tuples don't.

### Lists
```python
nums = [3, 1, 4, 1, 5]
nums.append(9)        # [3, 1, 4, 1, 5, 9]
nums.sort()           # [1, 1, 3, 4, 5, 9]  (in place)
nums.pop()            # removes & returns 9
```

### Tuples
```python
point = (3, 4)
x, y = point          # unpacking
# point[0] = 10       # TypeError — immutable
```

### Key rules
- Indexing starts at 0; negative indices count from the end.
- `sort()` / `reverse()` modify in place and return `None`. Use `sorted()` / `reversed()` for copies.
- Tuples are immutable and hashable (can be dict keys); lists are not.
- Don't mutate a list while iterating over it.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels. Start with `easy/` and work your way up. Each problem file has the description at the top — **write your complete solution from scratch below** (function signature + body) to practice remembering syntax.

### Easy (start here)
1. `easy/p01-solve.py` — `sum_list(nums)`: return the sum of all numbers in a list (no built-in `sum()`).
2. `easy/p02-solve.py` — `reverse_list(items)`: return a new list with the elements in reverse order (don't mutate the input).
3. `easy/p03-solve.py` — `contains(items, target)`: return `True` if `target` is in the list, `False` otherwise (no `in` operator — loop manually).

### Medium
4. `medium/p01-solve.py` — `remove_duplicates(items)`: return a new list with duplicates removed, preserving original order.
5. `medium/p02-solve.py` — `sort_by_length(words)`: return a new list of strings sorted by length (shortest first), using `sorted()` with a `key`.
6. `medium/p03-solve.py` — `swap_pairs(items)`: swap every pair of adjacent elements. For `[1,2,3,4,5]` return `[2,1,4,3,5]` (last element stays if odd length).

### Hard
7. `hard/p01-solve.py` — `flatten(nested)`: given a list that may contain sub-lists (one level deep), return a single flat list. `[[1,2],[3],[4,5]]` → `[1,2,3,4,5]`.
8. `hard/p02-solve.py` — `second_largest(nums)`: return the second largest unique value. `second_largest([5,1,4,4,3])` → `4`. Handle lists with fewer than 2 unique values by returning `None`.
9. `hard/p03-solve.py` — `tuple_stats(nums)`: given a tuple of numbers, return a tuple `(min, max, average)` where average is a float. Handle an empty tuple by returning `(None, None, 0.0)`.

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete solution from scratch** below the TODO marker.
- Remove the TODO line when done.
- Run `python <filename>` to test with your own inputs.
- When done, tell me and I'll review. Say **"give me next task"** to advance to the next lesson.
