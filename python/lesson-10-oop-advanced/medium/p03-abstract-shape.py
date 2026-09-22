"""
LESSON 10 — OOP Advanced
MEDIUM P03 — Abstract Shape
============================================

CONCEPT:
  An abstract base class (abc.ABC + @abstractmethod) defines an
  interface that subclasses MUST implement — you can't instantiate
  the abstract class itself.

PROBLEM:
  Write an abstract `Shape` class with abstract methods `area()`
  and `perimeter()`. Then implement `Circle(radius)` and
  `Square(side)` subclasses (use math.pi).

TRY THIS INPUT:
  ```python
  c = Circle(5)
  print(round(c.area(), 1))
  s = Square(4)
  print(s.area(), s.perimeter())
  ```

EXPECTED OUTPUT:
  ```
  78.5
  16 16
  ```

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
