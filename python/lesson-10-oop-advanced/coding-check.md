# Lesson 10 — Coding Check

## Easy

### p01-solve.py — Vehicle and Car
- [ ] `Vehicle("Toyota", "Camry", 2020)` has make, model, year attributes
- [ ] `Car("Honda", "Civic", 2021, 4)` has num_doors = 4
- [ ] `car.display()` returns a string with all info including num_doors
- [ ] Car inherits from Vehicle (isinstance(car, Vehicle) is True)
- [ ] Car overrides display() (different from Vehicle's display)

### p02-solve.py — Rectangle with @property
- [ ] `Rectangle(4, 5).area` returns `20` (no parentheses — it's a property)
- [ ] `Rectangle(4, 5).perimeter` returns `18`
- [ ] Changing width updates area: `r = Rectangle(4, 5); r.width = 6; r.area` returns `30`

### p03-solve.py — Student with __str__
- [ ] `str(Student("Akash", "A"))` returns `"Student: Akash (A)"`
- [ ] `print(Student("Bob", "B"))` prints `Student: Bob (B)`

## Medium

### p01-solve.py — Vector class
- [ ] `Vector(1, 2) + Vector(3, 4)` returns `Vector(4, 6)`
- [ ] `Vector(5, 5) - Vector(2, 3)` returns `Vector(3, 2)`
- [ ] `Vector(1, 2) == Vector(1, 2)` returns `True`
- [ ] `str(Vector(1, 2))` returns `"Vector(1, 2)"`

### p02-solve.py — BankAccount with encapsulation
- [ ] `BankAccount(100).balance` returns `100` (via @property)
- [ ] `account.deposit(50)` increases balance to `150`
- [ ] `account.deposit(-10)` does nothing (rejects negative)
- [ ] `account.withdraw(30)` decreases balance to `70`
- [ ] `account.withdraw(1000)` does nothing (insufficient funds)
- [ ] `account.__balance` raises AttributeError (private)

### p03-solve.py — Abstract Shape
- [ ] `Shape()` raises TypeError (can't instantiate abstract class)
- [ ] `Circle(5).area()` returns ~78.5
- [ ] `Circle(5).perimeter()` returns ~31.4
- [ ] `Square(4).area()` returns `16`
- [ ] `Square(4).perimeter()` returns `16`

## Hard

### p01-solve.py — Employee hierarchy
- [ ] `Employee("Akash", 50000).salary` returns `50000`
- [ ] `Manager("Bob", 80000, ["Alice", "Charlie"]).salary` returns `80000 + bonus` (bonus for having team)
- [ ] `Developer("Carol", 70000, ["Python", "JS"]).languages` returns `["Python", "JS"]`
- [ ] Both Manager and Developer are Employees (isinstance check)
- [ ] Manager's salary calculation is different from base Employee

### p02-solve.py — Stack with composition
- [ ] `stack = Stack(); stack.push(1); stack.push(2); stack.pop()` returns `2`
- [ ] `stack.peek()` returns top without removing
- [ ] `stack.is_empty()` returns `False` when has items, `True` when empty
- [ ] `stack.size()` returns number of items
- [ ] No direct list access: `stack.items` should not be accessible (or should be private)
- [ ] Stack does NOT inherit from list (composition, not inheritance)

### p03-solve.py — Book with classmethod and staticmethod
- [ ] `Book("Title", "Author", "1234567890").is_available` returns `True` initially
- [ ] After borrowing: `book.borrow(); book.is_available` returns `False`
- [ ] `Book.from_string("Python Guide|Akash|1234567890")` creates a Book instance
- [ ] `Book.is_valid_isbn("1234567890")` returns `True` (10 digits)
- [ ] `Book.is_valid_isbn("123")` returns `False` (too short)
- [ ] `Book.is_valid_isbn("1234567890123")` returns `True` (13 digits)
