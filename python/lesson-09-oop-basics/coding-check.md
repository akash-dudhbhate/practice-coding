# Lesson 09 — Coding Check

Use this to verify your solutions before asking me to review. Each problem file has its own expected behavior — check against these.

## Easy

### p01-solve.py (Rectangle)
- [ ] `Rectangle(3, 4).area()` returns `12`
- [ ] `Rectangle(3, 4).perimeter()` returns `14`
- [ ] `Rectangle(0, 5).area()` returns `0`

### p02-solve.py (Counter)
- [ ] `Counter().get()` returns `0`
- [ ] After `increment()` twice, `get()` returns `2`
- [ ] Each instance has its own count

### p03-solve.py (Book)
- [ ] `str(Book("1984", "Orwell"))` returns `"1984 by Orwell"`
- [ ] Has `title` and `author` attributes
- [ ] `__str__` defined (not default object repr)

## Medium

### p01-solve.py (BankAccount)
- [ ] `BankAccount("Akash", 100).deposit(50)` makes balance `150`
- [ ] `withdraw(200)` on a 100-balance account raises `ValueError`
- [ ] `str(BankAccount("Akash", 100))` returns `"Akash: $100"`
- [ ] `balance` defaults to 0

### p02-solve.py (Stack)
- [ ] `push(1); push(2); pop()` returns `2`
- [ ] `pop()` on empty stack raises `IndexError`
- [ ] `peek()` returns top without removing
- [ ] `is_empty()` returns `True` on new stack
- [ ] `len(Stack())` returns `0` (`__len__` defined)

### p03-solve.py (Temperature)
- [ ] `Temperature(100).fahrenheit()` returns `212.0`
- [ ] `Temperature.to_fahrenheit(100)` returns `212.0` (static, no instance)
- [ ] `Temperature.from_fahrenheit(212).celsius` returns `100.0`
- [ ] `from_fahrenheit` is a `@classmethod`

## Hard

### p01-solve.py (ShoppingCart)
- [ ] `add_item("pen", 2); add_item("book", 10); total()` returns `12`
- [ ] `remove_item("pen")` removes the first matching item
- [ ] `str(cart)` includes the total
- [ ] Empty cart `total()` returns `0`

### p02-solve.py (Student)
- [ ] `Student.count` increases by 1 per new student
- [ ] `add_grade(90); add_grade(80); average()` returns `85.0`
- [ ] Two students don't share grades (no mutable-default bug)
- [ ] `Student.get_count()` returns total students created

### p03-solve.py (Library)
- [ ] `add_book(Book("1984","Orwell"))` then `find_by_author("Orwell")` returns a list with that book
- [ ] `find_by_author("Nobody")` returns `[]`
- [ ] `len(library)` returns number of books
- [ ] `str(library)` summarizes the collection

## How to verify

Run each file with your own test calls:
```bash
python easy/p01-solve.py
```

Or test from a REPL:
```bash
python -c "from easy.p01_solve import Rectangle; print(Rectangle(3,4).area())"
```
