# Lesson 02 — Strings & String Methods

## What you'll learn
- String indexing and slicing
- String immutability
- Case methods (.upper, .lower, .capitalize, .title)
- .strip, .split, .join, .replace
- .find, .index, .count
- f-strings for formatting
- Character type checks (.isalpha, .isdigit, etc.)
- Escape characters and raw strings

## Lesson

Strings are sequences of characters. Python has rich built-in methods for manipulating them.

### Indexing & Slicing
```python
text = "hello"
text[0]     # 'h' — first char (index 0)
text[-1]    # 'o' — last char
text[0:3]   # "hel" — substring (stop is exclusive)
text[::-1]  # "olleh" — reversed
```

### Immutability
Strings CANNOT be changed in place. Methods return NEW strings.
```python
name = "akash"
name.upper()      # returns "AKASH" but name is still "akash"
name = name.upper()  # NOW name is "AKASH"
```

### Common methods
```python
"  hello  ".strip()        # "hello" — remove whitespace
"hello world".split()      # ["hello", "world"]
",".join(["a", "b", "c"])  # "a,b,c"
"hello".replace("l", "L")  # "heLLo"
"hello world".find("world") # 6 (position, -1 if not found)
"hello".count("l")         # 2
"hello".startswith("he")   # True
"hello".isalpha()          # True (only letters)
```

### f-strings
```python
name = "Akash"
age = 25
f"Hello, {name}! Age: {age}"        # "Hello, Akash! Age: 25"
f"{3.14159:.2f}"                     # "3.14" — 2 decimal places
```

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels.

### Easy (start here)
1. `easy/p01-solve.py` — Count the number of vowels in a string (case-insensitive).
2. `easy/p02-solve.py` — Return the reversed version of a string (without using slicing).
3. `easy/p03-solve.py` — Check if a string is a palindrome (reads the same forwards and backwards).

### Medium
4. `medium/p01-solve.py` — Given a full name string, return initials (e.g., "John Doe" → "JD").
5. `medium/p02-solve.py` — Count the number of words in a sentence.
6. `medium/p03-solve.py` — Replace all spaces in a string with underscores, and strip leading/trailing whitespace first.

### Hard
7. `hard/p01-solve.py` — Check if two strings are anagrams (same characters, different order).
8. `hard/p02-solve.py` — Compress a string using basic run-length encoding (e.g., "aaabbc" → "a3b2c1").
9. `hard/p03-solve.py` — Extract the domain from an email address (e.g., "user@gmail.com" → "gmail.com").

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete solution from scratch** below the TODO marker.
- Remove the TODO line when done.
- Run `python <filename>` to test with your own inputs.
- When done, tell me and I'll review. Say **"give me next task"** to advance.
