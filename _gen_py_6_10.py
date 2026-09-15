#!/usr/bin/env python3
"""Generate reference solutions for Python lessons 6-10."""
import os
BASE = "/home/akash-dev/workspace-personal/practice-coding/python"

SOLUTIONS = {
"lesson-06-functions-deep-dive": {
"easy/p01": '''"""SOLUTION: Greet with Default (Easy)"""
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

if __name__ == "__main__":
    assert greet("Akash") == "Hello, Akash!"
    assert greet("Dev", "Hi") == "Hi, Dev!"
    print("All tests passed!")
''',
"easy/p02": '''"""SOLUTION: Sum All with *args (Easy)"""
def sum_all(*nums):
    total = 0
    for n in nums:
        total += n
    return total

if __name__ == "__main__":
    assert sum_all(1, 2, 3) == 6
    assert sum_all() == 0
    assert sum_all(10) == 10
    print("All tests passed!")
''',
"easy/p03": '''"""SOLUTION: Lambda Square (Easy)"""
square = lambda n: n * n

if __name__ == "__main__":
    assert square(5) == 25
    assert square(0) == 0
    assert square(-3) == 9
    print("All tests passed!")
''',
"medium/p01": '''"""SOLUTION: Make HTML Tag (Medium)"""
def make_tag(tag, text, **attrs):
    attr_str = ""
    for k, v in attrs.items():
        attr_str += f' {k}="{v}"'
    return f"<{tag}{attr_str}>{text}</{tag}>"

if __name__ == "__main__":
    assert make_tag("a", "link", href="x.com") == '<a href="x.com">link</a>'
    assert make_tag("p", "hi") == "<p>hi</p>"
    print("All tests passed!")
''',
"medium/p02": '''"""SOLUTION: Safe Append (Medium)"""
def safe_append(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

if __name__ == "__main__":
    assert safe_append(1) == [1]
    assert safe_append(2) == [2]  # not [1, 2] — new list each time
    assert safe_append(1, [0]) == [0, 1]
    print("All tests passed!")
''',
"medium/p03": '''"""SOLUTION: Apply Func (Medium)"""
def apply_func(func, items):
    return [func(item) for item in items]

if __name__ == "__main__":
    assert apply_func(lambda x: x * 2, [1, 2, 3]) == [2, 4, 6]
    assert apply_func(str, [1, 2]) == ["1", "2"]
    print("All tests passed!")
''',
"hard/p01": '''"""SOLUTION: Make Counter Closure (Hard)"""
def make_counter(start=0):
    count = start
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

if __name__ == "__main__":
    c = make_counter()
    assert c() == 1
    assert c() == 2
    c2 = make_counter(10)
    assert c2() == 11
    print("All tests passed!")
''',
"hard/p02": '''"""SOLUTION: Compose (Hard)"""
def compose(f, g):
    def composed(x):
        return f(g(x))
    return composed

if __name__ == "__main__":
    h = compose(lambda x: x + 1, lambda x: x * 2)
    assert h(3) == 7  # (3*2)+1
    print("All tests passed!")
''',
"hard/p03": '''"""SOLUTION: Build Profile + Format (Hard)"""
def build_profile(name, **info):
    return {"name": name, **info}

def format_profile(profile):
    name = profile["name"]
    info_str = ", ".join(f"{k}={v}" for k, v in profile.items() if k != "name")
    return f"{name} ({info_str})"

if __name__ == "__main__":
    p = build_profile("Akash", role="dev", level=5)
    assert p["name"] == "Akash"
    assert p["role"] == "dev"
    f = format_profile(p)
    assert "Akash" in f and "role=dev" in f
    print("All tests passed!")
''',
},
"lesson-07-file-io-error-handling": {
"easy/p01": '''"""SOLUTION: Read File (Easy)"""
def read_file(path):
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return None

if __name__ == "__main__":
    with open("/tmp/test_read.txt", "w") as f:
        f.write("hello")
    assert read_file("/tmp/test_read.txt") == "hello"
    assert read_file("/nonexistent") is None
    print("All tests passed!")
''',
"easy/p02": '''"""SOLUTION: Write File (Easy)"""
def write_file(path, text):
    try:
        with open(path, "w") as f:
            f.write(text)
        return True
    except Exception:
        return False

if __name__ == "__main__":
    assert write_file("/tmp/test_write.txt", "content") == True
    assert read_file := open("/tmp/test_write.txt").read() == "content"
    print("All tests passed!")
''',
"easy/p03": '''"""SOLUTION: Safe Int (Easy)"""
def safe_int(s):
    try:
        return int(s)
    except ValueError:
        return None

if __name__ == "__main__":
    assert safe_int("42") == 42
    assert safe_int("abc") is None
    assert safe_int("") is None
    print("All tests passed!")
''',
"medium/p01": '''"""SOLUTION: Count Lines (Medium)"""
def count_lines(path):
    try:
        with open(path, "r") as f:
            return len(f.readlines())
    except FileNotFoundError:
        return 0

if __name__ == "__main__":
    with open("/tmp/test_lines.txt", "w") as f:
        f.write("line1\\nline2\\nline3\\n")
    assert count_lines("/tmp/test_lines.txt") == 3
    assert count_lines("/nonexistent") == 0
    print("All tests passed!")
''',
"medium/p02": '''"""SOLUTION: Append Log (Medium)"""
def append_log(path, message):
    with open(path, "a") as f:
        f.write(message + "\\n")

if __name__ == "__main__":
    import os
    p = "/tmp/test_log.txt"
    if os.path.exists(p):
        os.remove(p)
    append_log(p, "First")
    append_log(p, "Second")
    with open(p) as f:
        lines = f.readlines()
    assert len(lines) == 2
    print("All tests passed!")
''',
"medium/p03": '''"""SOLUTION: Read JSON (Medium)"""
import json

def read_json(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

if __name__ == "__main__":
    import json as j
    with open("/tmp/test.json", "w") as f:
        j.dump({"key": "val"}, f)
    assert read_json("/tmp/test.json") == {"key": "val"}
    assert read_json("/nonexistent") is None
    with open("/tmp/bad.json", "w") as f:
        f.write("not json")
    assert read_json("/tmp/bad.json") is None
    print("All tests passed!")
''',
"hard/p01": '''"""SOLUTION: Safe Divide with Custom Error (Hard)"""
class DivideByZeroError(Exception):
    pass

def safe_divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numeric")
    if b == 0:
        raise DivideByZeroError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    assert safe_divide(10, 2) == 5.0
    try:
        safe_divide(1, 0)
        assert False
    except DivideByZeroError:
        pass
    try:
        safe_divide("a", 1)
        assert False
    except TypeError:
        pass
    print("All tests passed!")
''',
"hard/p02": '''"""SOLUTION: Process File (Hard)"""
def process_file(path):
    try:
        with open(path, "r") as f:
            total = 0
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    total += int(line)
                except ValueError:
                    print(f"Warning: skipping non-numeric line: {line}")
            return total
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")

if __name__ == "__main__":
    with open("/tmp/test_nums.txt", "w") as f:
        f.write("10\\n20\\n\\nabc\\n30\\n")
    assert process_file("/tmp/test_nums.txt") == 60
    print("All tests passed!")
''',
"hard/p03": '''"""SOLUTION: Config Loader (Hard)"""
import json

class ConfigError(Exception):
    pass

def config_loader(path):
    try:
        with open(path, "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        raise ConfigError(f"Config file not found: {path}")
    except json.JSONDecodeError:
        raise ConfigError(f"Invalid JSON in config: {path}")
    if "host" not in config:
        raise ConfigError("Config must contain 'host' key")
    return config

if __name__ == "__main__":
    with open("/tmp/test_cfg.json", "w") as f:
        json.dump({"host": "localhost", "port": 8080}, f)
    cfg = config_loader("/tmp/test_cfg.json")
    assert cfg["host"] == "localhost"
    with open("/tmp/test_cfg2.json", "w") as f:
        json.dump({"port": 8080}, f)
    try:
        config_loader("/tmp/test_cfg2.json")
        assert False
    except ConfigError:
        pass
    print("All tests passed!")
''',
},
"lesson-08-comprehensions-generators": {
"easy/p01": '''"""SOLUTION: Squares Comprehension (Easy)"""
def squares(n):
    return [i * i for i in range(n)]

if __name__ == "__main__":
    assert squares(4) == [0, 1, 4, 9]
    assert squares(0) == []
    print("All tests passed!")
''',
"easy/p02": '''"""SOLUTION: Evens Comprehension (Easy)"""
def evens(nums):
    return [n for n in nums if n % 2 == 0]

if __name__ == "__main__":
    assert evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert evens([1, 3, 5]) == []
    print("All tests passed!")
''',
"easy/p03": '''"""SOLUTION: Lengths Dict Comprehension (Easy)"""
def lengths(words):
    return {w: len(w) for w in words}

if __name__ == "__main__":
    assert lengths(["hi", "hello"]) == {"hi": 2, "hello": 5}
    print("All tests passed!")
''',
"medium/p01": '''"""SOLUTION: Flatten 2D (Medium)"""
def flatten(matrix):
    return [item for row in matrix for item in row]

if __name__ == "__main__":
    assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert flatten([]) == []
    print("All tests passed!")
''',
"medium/p02": '''"""SOLUTION: Sum Squares Generator (Medium)"""
def sum_squares(n):
    return sum(i * i for i in range(n))

if __name__ == "__main__":
    assert sum_squares(4) == 0 + 1 + 4 + 9
    assert sum_squares(0) == 0
    print("All tests passed!")
''',
"medium/p03": '''"""SOLUTION: Even Squares (Medium)"""
def even_squares(n):
    return [i * i for i in range(n) if (i * i) % 2 == 0]

if __name__ == "__main__":
    assert even_squares(5) == [0, 4, 16]
    print("All tests passed!")
''',
"hard/p01": '''"""SOLUTION: Fibonacci Generator (Hard)"""
def fibonacci_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    assert list(fibonacci_gen(6)) == [0, 1, 1, 2, 3, 5]
    assert list(fibonacci_gen(0)) == []
    assert list(fibonacci_gen(1)) == [0]
    print("All tests passed!")
''',
"hard/p02": '''"""SOLUTION: Chunked Generator (Hard)"""
def chunked(iterable, size):
    chunk = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk

if __name__ == "__main__":
    assert list(chunked([1, 2, 3, 4, 5], 2)) == [[1, 2], [3, 4], [5]]
    assert list(chunked([], 3)) == []
    print("All tests passed!")
''',
"hard/p03": '''"""SOLUTION: Generator Pipeline (Hard)"""
def filter_positive(data):
    return (x for x in data if x > 0)

def double(data):
    return (x * 2 for x in data)

def to_strings(data):
    return (str(x) for x in data)

def pipeline(data):
    return list(to_strings(double(filter_positive(data))))

if __name__ == "__main__":
    assert pipeline([-1, 2, -3, 4]) == ["4", "8"]
    assert pipeline([]) == []
    print("All tests passed!")
''',
},
"lesson-09-oop-basics": {
"easy/p01": '''"""SOLUTION: Rectangle Class (Easy)"""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

if __name__ == "__main__":
    r = Rectangle(4, 5)
    assert r.area() == 20
    assert r.perimeter() == 18
    print("All tests passed!")
''',
"easy/p02": '''"""SOLUTION: Counter Class (Easy)"""
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get(self):
        return self.count

if __name__ == "__main__":
    c = Counter()
    c.increment()
    c.increment()
    assert c.get() == 2
    print("All tests passed!")
''',
"easy/p03": '''"""SOLUTION: Book Class (Easy)"""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

if __name__ == "__main__":
    b = Book("1984", "Orwell")
    assert str(b) == "1984 by Orwell"
    print("All tests passed!")
''',
"medium/p01": '''"""SOLUTION: BankAccount Class (Medium)"""
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def __str__(self):
        return f"{self.owner}: ${self.balance}"

if __name__ == "__main__":
    acc = BankAccount("Akash", 100)
    acc.deposit(50)
    assert acc.balance == 150
    acc.withdraw(30)
    assert acc.balance == 120
    try:
        acc.withdraw(200)
        assert False
    except ValueError:
        pass
    print("All tests passed!")
''',
"medium/p02": '''"""SOLUTION: Stack Class (Medium)"""
class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)

if __name__ == "__main__":
    s = Stack()
    assert s.is_empty()
    s.push(1)
    s.push(2)
    assert len(s) == 2
    assert s.pop() == 2
    assert s.peek() == 1
    try:
        s2 = Stack()
        s2.pop()
        assert False
    except IndexError:
        pass
    print("All tests passed!")
''',
"medium/p03": '''"""SOLUTION: Temperature Class (Medium)"""
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, f):
        return cls((f - 32) * 5 / 9)

    @staticmethod
    def to_fahrenheit(c):
        return c * 9 / 5 + 32

    def fahrenheit(self):
        return self.to_fahrenheit(self.celsius)

if __name__ == "__main__":
    t = Temperature(100)
    assert t.fahrenheit() == 212.0
    t2 = Temperature.from_fahrenheit(32)
    assert abs(t2.celsius - 0) < 0.01
    print("All tests passed!")
''',
"hard/p01": '''"""SOLUTION: ShoppingCart Class (Hard)"""
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append((name, price))

    def total(self):
        return sum(price for _, price in self.items)

    def remove_item(self, name):
        for i, (n, _) in enumerate(self.items):
            if n == name:
                self.items.pop(i)
                return

    def __str__(self):
        items_str = "\\n".join(f"  {n}: ${p}" for n, p in self.items)
        return f"Cart:\\n{items_str}\\nTotal: ${self.total()}"

if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("apple", 1.5)
    cart.add_item("bread", 3.0)
    assert cart.total() == 4.5
    cart.remove_item("apple")
    assert cart.total() == 3.0
    print("All tests passed!")
''',
"hard/p02": '''"""SOLUTION: Student with Class Counter (Hard)"""
class Student:
    count = 0

    def __init__(self, name, grades=None):
        self.name = name
        self.grades = list(grades) if grades else []
        Student.count += 1

    def add_grade(self, g):
        self.grades.append(g)

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    @classmethod
    def get_count(cls):
        return cls.count

if __name__ == "__main__":
    Student.count = 0  # reset
    s1 = Student("Akash", [90, 80])
    s2 = Student("Dev")
    assert Student.get_count() == 2
    s2.add_grade(70)
    assert s2.average() == 70
    print("All tests passed!")
''',
"hard/p03": '''"""SOLUTION: Library Composition (Hard)"""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_by_author(self, author):
        return [b for b in self.books if b.author == author]

    def __len__(self):
        return len(self.books)

    def __str__(self):
        return f"Library: {len(self)} books"

if __name__ == "__main__":
    lib = Library()
    lib.add_book(Book("1984", "Orwell"))
    lib.add_book(Book("Animal Farm", "Orwell"))
    lib.add_book(Book("Dune", "Herbert"))
    assert len(lib) == 3
    orwell = lib.find_by_author("Orwell")
    assert len(orwell) == 2
    print("All tests passed!")
''',
},
"lesson-10-oop-advanced": {
"easy/p01": '''"""SOLUTION: Vehicle and Car Inheritance (Easy)"""
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display(self):
        return f"{super().display()} ({self.num_doors} doors)"

if __name__ == "__main__":
    c = Car("Toyota", "Camry", 2020, 4)
    assert "2020 Toyota Camry" in c.display()
    assert "4 doors" in c.display()
    print("All tests passed!")
''',
"easy/p02": '''"""SOLUTION: Rectangle with @property (Easy)"""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)

if __name__ == "__main__":
    r = Rectangle(4, 5)
    assert r.area == 20
    assert r.perimeter == 18
    print("All tests passed!")
''',
"easy/p03": '''"""SOLUTION: Student __str__ (Easy)"""
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"Student: {self.name} ({self.grade})"

if __name__ == "__main__":
    s = Student("Akash", "A")
    assert str(s) == "Student: Akash (A)"
    print("All tests passed!")
''',
"medium/p01": '''"""SOLUTION: Vector Class (Medium)"""
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

if __name__ == "__main__":
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    assert (v1 + v2) == Vector(4, 6)
    assert (v2 - v1) == Vector(2, 2)
    print("All tests passed!")
''',
"medium/p02": '''"""SOLUTION: BankAccount with Private Balance (Medium)"""
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    @property
    def balance(self):
        return self.__balance

if __name__ == "__main__":
    acc = BankAccount("Akash", 100)
    assert acc.balance == 100
    acc.deposit(50)
    assert acc.balance == 150
    try:
        acc.withdraw(200)
    except ValueError:
        pass
    print("All tests passed!")
''',
"medium/p03": '''"""SOLUTION: Abstract Shape (Medium)"""
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

if __name__ == "__main__":
    c = Circle(5)
    assert abs(c.area() - 78.54) < 1
    s = Square(4)
    assert s.area() == 16
    print("All tests passed!")
''',
"hard/p01": '''"""SOLUTION: Employee Hierarchy (Hard)"""
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary

class Manager(Employee):
    def __init__(self, name, salary, team=None):
        super().__init__(name, salary)
        self.team = team or []

    def calculate_salary(self):
        return self.salary + len(self.team) * 100  # bonus per team member

class Developer(Employee):
    def __init__(self, name, salary, languages=None):
        super().__init__(name, salary)
        self.languages = languages or []

    def calculate_salary(self):
        return self.salary + len(self.languages) * 50  # bonus per language

if __name__ == "__main__":
    m = Manager("Alice", 80000, ["Bob", "Carol"])
    assert m.calculate_salary() == 80200
    d = Developer("Dave", 70000, ["Python", "JS"])
    assert d.calculate_salary() == 70100
    print("All tests passed!")
''',
"hard/p02": '''"""SOLUTION: Stack with Composition (Hard)"""
class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

if __name__ == "__main__":
    s = Stack()
    assert s.is_empty()
    s.push(1)
    s.push(2)
    assert s.size() == 2
    assert s.pop() == 2
    assert s.peek() == 1
    print("All tests passed!")
''',
"hard/p03": '''"""SOLUTION: Book with property, classmethod, staticmethod (Hard)"""
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self._borrowed = False

    @property
    def is_available(self):
        return not self._borrowed

    def borrow(self):
        if self._borrowed:
            raise ValueError("Already borrowed")
        self._borrowed = True

    def return_book(self):
        self._borrowed = False

    @classmethod
    def from_string(cls, s):
        title, author, isbn = s.split("|")
        return cls(title, author, isbn)

    @staticmethod
    def is_valid_isbn(isbn):
        return len(isbn) == 10 or len(isbn) == 13

if __name__ == "__main__":
    b = Book("1984", "Orwell", "1234567890")
    assert b.is_available == True
    b.borrow()
    assert b.is_available == False
    b2 = Book.from_string("Dune|Herbert|9876543210")
    assert b2.title == "Dune"
    assert Book.is_valid_isbn("1234567890") == True
    assert Book.is_valid_isbn("123") == False
    print("All tests passed!")
''',
},
}

count = 0
for lesson, problems in SOLUTIONS.items():
    for key, code in problems.items():
        diff, pnum = key.split("/")
        d = os.path.join(BASE, lesson, diff, "solutions")
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, f"{pnum}-solution.py"), 'w') as f:
            f.write(code)
        count += 1
print(f"Generated {count} solutions")
