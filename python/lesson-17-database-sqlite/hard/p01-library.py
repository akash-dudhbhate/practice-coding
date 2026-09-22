"""
LESSON 17 — Database with SQLite
HARD P01 — Library Class
============================================

CONCEPT:
  Multi-step changes need transactions: if any step fails, ROLLBACK
  so the database never ends up half-updated (e.g., book marked
  borrowed but no loan row written).

PROBLEM:
  Write a `Library` class (db_path defaults to ":memory:") with
  books, borrowers, and loans tables (foreign keys on), and methods:
  `add_book(title, author)`, `borrow_book(book_id, borrower_id)`
  (marks book borrowed + records loan, transactionally — raise
  ValueError if missing/already borrowed), `return_book(book_id)`,
  `list_available_books()`, and `search_by_title(keyword)`
  (LIKE match).

TRY THIS INPUT:
  ```python
  lib = Library()
  lib.add_book("Python 101", "John Doe")
  print(lib.list_available_books())
  ```

EXPECTED OUTPUT:
  ```
  [(1, 'Python 101', 'John Doe')]
  ```

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
