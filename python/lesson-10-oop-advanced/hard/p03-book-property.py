"""
LESSON 10 — OOP Advanced
HARD P03 — Book: property + classmethod + staticmethod
============================================

CONCEPT:
  Combine the toolkit: @property for computed state, @classmethod
  for alternate constructors, @staticmethod for helpers that belong
  to the class but need no instance.

PROBLEM:
  Write a `Book` class with:
    - `__init__(title, author, isbn)` — starts unborrowed.
    - `is_available` @property — True when not borrowed.
    - `borrow()` — marks borrowed, ValueError if already borrowed.
    - `return_book()` — marks available again.
    - `from_string(s)` @classmethod — parses "Title|Author|ISBN".
    - `is_valid_isbn(isbn)` @staticmethod — True if length is 10 or 13.

TRY THIS INPUT:
  ```python
  b = Book.from_string("Dune|Herbert|9876543210")
  print(b.title, b.is_available)
  b.borrow()
  print(b.is_available)
  print(Book.is_valid_isbn("123"), Book.is_valid_isbn("1234567890"))
  ```

EXPECTED OUTPUT:
  ```
  Dune True
  False
  False True
  ```

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
