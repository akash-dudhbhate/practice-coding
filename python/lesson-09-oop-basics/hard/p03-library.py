"""
LESSON 09 — OOP Basics
HARD P03 — Library Composition
============================================

CONCEPT:
  Composition means one class is built from others — a Library has
  Book objects inside it. This models real "has-a" relationships.

PROBLEM:
  Write a `Book` class (`__init__(title, author)`, `__str__` ->
  "Title by Author") and a `Library` class with `add_book(book)`,
  `find_by_author(author)` returning a list of matching books,
  `__len__` returning the number of books, and `__str__`
  summarizing the collection.

TRY THIS INPUT:
  ```python
  lib = Library()
  lib.add_book(Book("1984", "Orwell"))
  lib.add_book(Book("Animal Farm", "Orwell"))
  lib.add_book(Book("Dune", "Herbert"))
  print(len(lib))
  print(len(lib.find_by_author("Orwell")))
  ```

EXPECTED OUTPUT:
  ```
  3
  2
  ```

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
