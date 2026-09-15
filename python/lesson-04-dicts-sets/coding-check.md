# Lesson 04 — Coding Check

Use this to verify your solutions before asking me to review. Each problem file has its own expected behavior — check against these.

## Easy

### p01-solve.py (word_count)
- [ ] `word_count("the cat the dog")` returns `{"the": 2, "cat": 1, "dog": 1}`
- [ ] `word_count("")` returns `{}`
- [ ] `word_count("Hello hello")` returns `{"hello": 2}` (case-insensitive)
- [ ] Words are split on whitespace

### p02-solve.py (has_key)
- [ ] `has_key({"a": 1}, "a")` returns `True`
- [ ] `has_key({"a": 1}, "b")` returns `False`
- [ ] `has_key({}, "a")` returns `False`
- [ ] Uses `.get()` (not `in`)

### p03-solve.py (unique_items)
- [ ] `unique_items([1, 2, 2, 3, 3, 3])` returns `[1, 2, 3]`
- [ ] `unique_items([])` returns `[]`
- [ ] Order of first appearance is preserved
- [ ] Uses a set for tracking

## Medium

### p01-solve.py (merge_dicts)
- [ ] `merge_dicts({"a":1,"b":2}, {"b":3,"c":4})` returns `{"a":1,"b":3,"c":4}`
- [ ] Original dicts are NOT mutated
- [ ] `merge_dicts({}, {"a":1})` returns `{"a":1}`
- [ ] `merge_dicts({"a":1}, {})` returns `{"a":1}`

### p02-solve.py (invert_dict)
- [ ] `invert_dict({"a":1,"b":2})` returns `{1:"a", 2:"b"}`
- [ ] `invert_dict({"a":1,"b":1})` returns `{1:"b"}` (last key wins)
- [ ] `invert_dict({})` returns `{}`
- [ ] Returns a NEW dict

### p03-solve.py (common_elements)
- [ ] `common_elements([1,2,3], [2,3,4])` returns `[2, 3]`
- [ ] `common_elements([1,1,2], [2,2,1])` returns `[1, 2]` (no dupes, sorted)
- [ ] `common_elements([], [1,2])` returns `[]`
- [ ] Uses set intersection

## Hard

### p01-solve.py (group_by_parity)
- [ ] `group_by_parity([1,2,3,4,5])` returns `{"even": [2,4], "odd": [1,3,5]}`
- [ ] `group_by_parity([])` returns `{"even": [], "odd": []}`
- [ ] `group_by_parity([2,4,6])` returns `{"even": [2,4,6], "odd": []}`
- [ ] Both keys always present

### p02-solve.py (set_difference)
- [ ] `set_difference([1,2,3], [2,3,4])` returns `{"only_a": [1], "only_b": [4]}`
- [ ] `set_difference([], [1,2])` returns `{"only_a": [], "only_b": [1,2]}`
- [ ] `set_difference([1,1,2], [2,3])` returns `{"only_a": [1], "only_b": [3]}`
- [ ] Lists are sorted with no duplicates

### p03-solve.py (char_frequency)
- [ ] `char_frequency("aab bc")` returns `[('a',2),('b',2),('c',1)]`
- [ ] `char_frequency("")` returns `[]`
- [ ] Spaces are excluded
- [ ] Ties may be in any order, but sorted by count descending

## How to verify

Run each file with your own test calls:
```bash
python easy/p01-solve.py
```

Or test from a REPL:
```bash
python -c "from easy.p01_solve import word_count; print(word_count('the cat the dog'))"
```
