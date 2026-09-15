# Lesson 02 — Debug Exercises

> Fix the broken code. Find bugs mentally before running.

---

## Debug 01 (Easy): Count Vowels — Missing Lowercase

```python
def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
```

**Hint:** What about uppercase vowels (A, E, I, O, U)?

<details><summary>Answer</summary>

**Bug:** Only checks lowercase vowels. `count_vowels("HELLO")` returns 0, not 2.
**Fix:** `for char in text.lower():` or check `char.lower() in vowels`.
</details>

---

## Debug 02 (Medium): Reverse String — Off-by-One

```python
def reverse_string(s):
    result = ""
    for i in range(len(s), 0, -1):
        result += s[i]
    return result
```

**Hint:** What happens when `i = len(s)`?

<details><summary>Answer</summary>

**Bug:** `range(len(s), 0, -1)` starts at `len(s)` which is out of bounds. `s[len(s)]` → IndexError.
**Fix:** `range(len(s) - 1, -1, -1)` or use `range(len(s))` with `s[len(s)-1-i]`.
</details>

---

## Debug 03 (Hard): Palindrome — Not Stripping Spaces

```python
def is_palindrome(s):
    return s == s[::-1]
```

**Hint:** "A Santa at NASA" is a palindrome but this returns False. Why?

<details><summary>Answer</summary>

**Bug:** Doesn't handle spaces or case. `"A Santa at NASA" != "ASAN at atnaS A"`.
**Fix:** `s = s.lower().replace(" ", ""); return s == s[::-1]`.
</details>
