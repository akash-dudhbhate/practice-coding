"""
LESSON 09 — OOP Basics
HARD P01 — ShoppingCart Class
============================================

CONCEPT:
  Objects can own collections. Storing (name, price) tuples in a
  list lets methods like total() and remove_item() work over the
  cart's contents.

PROBLEM:
  Write a class `ShoppingCart` that holds (name, price) items with
  `add_item(name, price)`, `total()` returning the price sum,
  `remove_item(name)` removing the first match, and `__str__`
  listing items and the total.

TRY THIS INPUT:
  ```python
  cart = ShoppingCart()
  cart.add_item("apple", 1.5)
  cart.add_item("bread", 3.0)
  print(cart.total())
  cart.remove_item("apple")
  print(cart.total())
  ```

EXPECTED OUTPUT:
  ```
  4.5
  3.0
  ```

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
