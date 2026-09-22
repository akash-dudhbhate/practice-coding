# lesson-02-strings-methods — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

> Don't run the code. Answer mentally first.

---

## Check 01: String Immutability
```python
s = "hello"
s[0] = "H"
```
What happens?
- (A) s becomes "Hello"
- (B) TypeError
- (C) Nothing

<details><summary>Answer</summary>
**(B) TypeError** — Strings are immutable in Python. You can't change individual characters. Use `s = "H" + s[1:]`.
</details>

---

## Check 02: Slicing
```python
s = "abcdef"
print(s[1:4])
print(s[:3])
print(s[3:])
print(s[::-1])
```
What prints (4 lines)?

<details><summary>Answer</summary>
```
bcd
abc
def
fedcba
```
`[start:stop]` — stop is exclusive. `[:3]` = first 3. `[3:]` = from index 3 to end. `[::-1]` = reverse.
</details>

---

## Check 03: String Methods Chaining
```python
s = "  Hello World  "
print(s.strip().lower().replace(" ", "_"))
```
What prints?

<details><summary>Answer</summary>
```
hello_world
```
Methods chain left to right: strip removes spaces, lower makes lowercase, replace swaps spaces for underscores.
</details>

---

## Check 04: Concatenation
```python
print("2" + "3")
print(2 + 3)
print("2" + 3)
```
What happens (3 lines)?

<details><summary>Answer</summary>
```
23
5
TypeError
```
`"2" + "3"` = string concatenation. `2 + 3` = addition. `"2" + 3` = TypeError (can't add str and int). Use `str(3)` or `int("2")`.
</details>

---

## Check 05: f-strings
```python
name = "Akash"
age = 25
print(f"{name=}, {age=}")
```
What prints? (Python 3.8+)

<details><summary>Answer</summary>
```
name='Akash', age=25
```
`{name=}` is a debug feature — prints the variable name and value. Great for debugging.
</details>

---

## Debug Exercises — find and fix the bug

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

---

## Common Mistakes — the traps learners hit

---

## Mistake 01: Forgetting strings are immutable
```python
# WRONG
s = "hello"
s[0] = "H"  # TypeError

# CORRECT
s = "H" + s[1:]  # "Hello"
# or
s = s.replace("h", "H")
```

## Mistake 02: Not handling case
```python
# WRONG — misses uppercase
if "a" in text:  # misses "A"

# CORRECT
if "a" in text.lower():
```

## Mistake 03: Using == for string search
```python
# WRONG — exact match only
if text == "hello":  # misses "Hello", "hello ", " hello"

# CORRECT — for partial match
if "hello" in text.lower():
```

## Mistake 04: Not stripping user input
```python
# WRONG — " hello " != "hello"
if user_input == "yes":

# CORRECT
if user_input.strip().lower() == "yes":
```

## Mistake 05: Concatenating with + instead of f-strings
```python
# HARD TO READ
msg = "Hello, " + name + "! You are " + str(age) + " years old."

# BETTER — f-string
msg = f"Hello, {name}! You are {age} years old."
```

## Mistake 06: Not using .join() for multiple concatenations
```python
# SLOW — creates new string each time
result = ""
for word in words:
    result += word + " "

# FAST — joins in one operation
result = " ".join(words)
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Manual Loop
### Before
```python
def count_vowels(text):
    count = 0
    for c in text:
        if c in "aeiouAEIOU":
            count = count + 1
    return count
```
### Problems
1. `count = count + 1` → use `count += 1`
2. Manual loop when `sum()` works

### After
```python
def count_vowels(text):
    return sum(1 for c in text.lower() if c in "aeiou")
```

---

## Refactor 02 (Medium): String Concatenation in Loop
### Before
```python
def join_words(words):
    result = ""
    for word in words:
        result = result + word + " "
    return result
```
### Problems
1. `+=` on strings in loop is O(n²) — creates new string each time
2. Trailing space at end

### After
```python
def join_words(words):
    return " ".join(words)
```

---

## Refactor 03 (Hard): Repeated Method Calls
### Before
```python
def clean_text(text):
    text = text.strip()
    text = text.lower()
    text = text.replace("  ", " ")
    text = text.replace("  ", " ")
    return text
```
### Problems
1. Repeated `text =` assignment
2. `replace("  ", " ")` called twice for multiple spaces — fragile

### After
```python
import re
def clean_text(text):
    return re.sub(r"\s+", " ", text.strip().lower())
```

---

## Approach Comparison — different ways to solve it

## Problem: Count Vowels

### Approach 1: Loop with counter
```python
def count_vowels(text):
    count = 0
    for c in text.lower():
        if c in "aeiou":
            count += 1
    return count
```
**Pros:** Clear, beginner-friendly. **Cons:** Verbose.

### Approach 2: Sum with generator
```python
def count_vowels(text):
    return sum(1 for c in text.lower() if c in "aeiou")
```
**Pros:** One line, Pythonic. **Cons:** Less readable for beginners.

### Approach 3: Set intersection
```python
def count_vowels(text):
    return len(set(text.lower()) & set("aeiou"))
```
**Bug!** This counts UNIQUE vowels, not total. "aaee" → 2, not 4. Wrong approach.

**Winner:** Approach 2 for production, Approach 1 for learning.

---

## Problem: Reverse a String

### Approach 1: Loop
```python
def reverse_string(s):
    result = ""
    for c in s:
        result = c + result
    return result
```
**Pros:** Teaches string building. **Cons:** O(n²) — each `c + result` creates a new string.

### Approach 2: Slicing
```python
def reverse_string(s):
    return s[::-1]
```
**Pros:** One line, O(n), Pythonic. **Cons:** "Magic" — beginners don't understand `[::-1]`.

### Approach 3: reversed()
```python
def reverse_string(s):
    return "".join(reversed(s))
```
**Pros:** Explicit. **Cons:** Longer than slicing.

**Winner:** Approach 2 (slicing) — the standard Python way.

---

## Problem: Check Palindrome

### Approach 1: Slicing
```python
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
```
**Pros:** One line, O(n). **Cons:** Creates a reversed copy.

### Approach 2: Two pointers
```python
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```
**Pros:** O(1) space, early exit. **Cons:** More code.

**Winner:** Approach 1 for simplicity. Approach 2 for interviews (shows algorithm knowledge).
