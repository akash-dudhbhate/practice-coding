# Lesson 01 — Variables, Types & Functions

## What you'll learn
- Python's core data types.
- How to define and call functions.
- Type hints and return values.

## Lesson

Python is dynamically typed — you don't declare types, but every value has one.

### Core types
```python
name = "Akash"        # str
age = 25              # int
height = 5.9          # float
is_dev = True         # bool
skills = ["py", "js"] # list
```

### Functions
```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("Akash"))  # Hello, Akash!
```
- `def` defines a function.
- Parameters can have **type hints** (`name: str`) — optional but good practice.
- `-> str` hints the return type.
- `f"..."` is an f-string for embedding variables.

### Key rules
- Indentation defines blocks (4 spaces).
- Functions must be defined before they're called.
- Use `return` to send a value back; without it, the function returns `None`.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels. Start with `easy/` and work your way up. Each problem file has the description at the top — **write your complete solution from scratch below** (function signature + body) to practice remembering syntax.

### Easy (start here)
1. `easy/p01-max-of-two.py` — return the larger of two integers (no built-in `max()`).
2. `easy/p02-even-or-odd.py` — return True if even, False if odd.
3. `easy/p03-celsius-to-fahrenheit.py` — convert C to F using the formula.

### Medium
4. `medium/p01-max-of-three.py` — reuse `max_of_two` from easy to find the max of three.
5. `medium/p02-leap-year.py` — determine if a year is a leap year (divisibility rules).
6. `medium/p03-count-vowels.py` — count vowels in a string (case-insensitive).

### Hard
7. `hard/p01-fizzbuzz.py` — classic FizzBuzz, return a list of strings.
8. `hard/p02-reverse-string.py` — reverse a string WITHOUT using slicing or `reversed()`.
9. `hard/p03-is-prime.py` — check if a number is prime.

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete solution from scratch** below the TODO marker.
- Remove the TODO line when done.
- Run `python <filename>` to test with your own inputs.
- When done, tell me and I'll review. Say **"give me next task"** to advance to the next lesson.
