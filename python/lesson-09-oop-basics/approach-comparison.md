# Lesson 09 — Approach Comparison

## Problem: Bank Account with Validation

### Approach 1: Public attributes
```python
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
```
**Cons:** Anyone can set `acc.balance = -1000` — no validation.

### Approach 2: Private + getters/setters
```python
class BankAccount:
    def __init__(self):
        self.__balance = 0
    def get_balance(self):
        return self.__balance
    def set_balance(self, value):
        if value < 0:
            raise ValueError
        self.__balance = value
```
**Cons:** Java-style, not Pythonic. Verbose.

### Approach 3: Private + @property
```python
class BankAccount:
    def __init__(self):
        self.__balance = 0
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError
        self.__balance = value
```
**Pros:** Clean API (`acc.balance = 100`), validation built in. Pythonic.

**Winner:** Approach 3 — @property gives clean syntax with validation.
