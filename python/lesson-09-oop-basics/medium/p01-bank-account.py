"""
LESSON 09 — OOP Basics
MEDIUM P01 — BankAccount Class
============================================

CONCEPT:
  Methods can enforce rules before changing state. Raising
  ValueError on a bad operation protects the object's invariant
  (balance can't go negative).

PROBLEM:
  Write a class `BankAccount` with `__init__(self, owner, balance=0)`,
  `deposit(amount)`, `withdraw(amount)` which raises ValueError if
  funds are insufficient, and `__str__` returning "Owner: $balance".

TRY THIS INPUT:
  ```python
  acc = BankAccount("Akash", 100)
  acc.deposit(50)
  acc.withdraw(30)
  print(acc.balance)
  print(str(acc))
  ```

EXPECTED OUTPUT:
  ```
  120
  Akash: $120
  ```

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
