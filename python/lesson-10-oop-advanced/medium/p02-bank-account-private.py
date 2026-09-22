"""
LESSON 10 — OOP Advanced
MEDIUM P02 — BankAccount with Private Balance
============================================

CONCEPT:
  A double-underscore attribute like `self.__balance` is
  name-mangled, so outside code can't touch it directly. Expose a
  read-only view with @property.

PROBLEM:
  Write a `BankAccount` class with `__init__(owner, balance=0)`
  storing balance privately, `deposit(amount)` (ValueError if
  amount <= 0), `withdraw(amount)` (ValueError if insufficient
  funds), and a `balance` @property getter.

TRY THIS INPUT:
  ```python
  acc = BankAccount("Akash", 100)
  acc.deposit(50)
  print(acc.balance)
  try:
      acc.withdraw(200)
  except ValueError as e:
      print("caught:", e)
  ```

EXPECTED OUTPUT:
  ```
  150
  caught: Insufficient funds
  ```

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
