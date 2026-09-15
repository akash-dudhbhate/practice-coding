# Lesson 04 — Debug Exercises

## Debug 01 (Easy): Word Count — Not Lowercasing
```python
def word_count(text):
    words = text.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts
```
**Hint:** "The" and "the" should be the same word.

<details><summary>Answer</summary>
**Bug:** Doesn't lowercase. `word_count("The the")` returns `{"The": 1, "the": 1}` instead of `{"the": 2}`.
**Fix:** `words = text.lower().split()`.
</details>

## Debug 02 (Medium): Has Key — Wrong Check
```python
def has_key(d, key):
    return d.get(key) is not None
```
**Hint:** What if the value IS None?

<details><summary>Answer</summary>
**Bug:** If the key exists but its value is `None`, `d.get(key)` returns `None`, and `is not None` is False — so it says the key doesn't exist. `has_key({"a": None}, "a")` returns False!
**Fix:** `return key in d` or `return d.get(key, sentinel) is not sentinel` where sentinel is a unique object.
</details>

## Debug 03 (Hard): Invert Dict — Duplicate Values Lost
```python
def invert_dict(d):
    return {v: k for k, v in d.items()}
```
**Hint:** What if two keys have the same value?

<details><summary>Answer</summary>
**Bug:** If values aren't unique, later keys overwrite earlier ones. `invert_dict({"a": 1, "b": 1})` returns `{1: "b"}` — "a" is lost silently.
**Fix (if acceptable):** Document that last key wins. **Fix (if need all):** Return `{v: [k1, k2]}` with lists.
</details>
