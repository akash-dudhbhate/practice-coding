# Lesson 04 — Dictionaries & Sets

## What you'll learn
- Storing and looking up data with dictionaries.
- Safe access with `.get()` and iterating with `.keys()/.values()/.items()`.
- Using sets for uniqueness and membership testing.
- Set operations (union, intersection, difference).
- `frozenset` and why keys must be hashable.

## Lesson

Dictionaries map keys to values (O(1) lookup). Sets store unique items (O(1) membership).

### Dictionaries
```python
user = {"name": "Akash", "age": 25}
user.get("email", "unknown")   # safe lookup
for key, value in user.items():
    print(key, value)
```

### Sets
```python
a = {1, 2, 3}
b = {3, 4, 5}
a | b   # {1, 2, 3, 4, 5}  union
a & b   # {3}              intersection
a - b   # {1, 2}           difference
```

### Key rules
- Dict keys and set elements must be hashable (immutable). Use a tuple, not a list.
- `.get(key, default)` avoids `KeyError`.
- Sets are unordered and reject duplicates automatically.
- Don't modify a dict/set while iterating over it.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels. Start with `easy/` and work your way up. Each problem file has the description at the top — **write your complete solution from scratch below** (function signature + body) to practice remembering syntax.

### Easy (start here)
1. `easy/p01-solve.py` — `word_count(text)`: return a dict mapping each word (lowercased) to its count. `word_count("the cat the dog")` → `{"the": 2, "cat": 1, "dog": 1}`.
2. `easy/p02-solve.py` — `has_key(d, key)`: return `True` if `key` is in dict `d`, using `.get()` (not `in`). Return `False` otherwise.
3. `easy/p03-solve.py` — `unique_items(items)`: return a list of unique items preserving first-seen order, using a set for tracking. `[1,2,2,3,3,3]` → `[1,2,3]`.

### Medium
4. `medium/p01-solve.py` — `merge_dicts(d1, d2)`: return a new dict merging `d1` and `d2`; values in `d2` override `d1` on conflict. Don't mutate inputs.
5. `medium/p02-solve.py` — `invert_dict(d)`: return a new dict with keys and values swapped. If values aren't unique, keep the last key seen for each value.
6. `medium/p03-solve.py` — `common_elements(a, b)`: return a sorted list of elements present in BOTH lists, using set intersection. `common_elements([1,2,3],[2,3,4])` → `[2, 3]`.

### Hard
7. `hard/p01-solve.py` — `group_by_parity(nums)`: return a dict `{"even": [...], "odd": [...]}` grouping numbers by parity. Handle empty input.
8. `hard/p02-solve.py` — `set_difference(a, b)`: return a dict with keys `"only_a"` and `"only_b"`, each a sorted list of items in `a` but not `b`, and `b` but not `a`, respectively (symmetric difference split).
9. `hard/p03-solve.py` — `char_frequency(s)`: return a dict of character frequencies for non-space chars, sorted by frequency descending (return a list of `(char, count)` tuples). `char_frequency("aab bc")` → `[('a',2),('b',2),('c',1)]`.

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete solution from scratch** below the TODO marker.
- Remove the TODO line when done.
- Run `python <filename>` to test with your own inputs.
- When done, tell me and I'll review. Say **"give me next task"** to advance to the next lesson.
