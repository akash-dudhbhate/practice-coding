# Lesson 11 — Modules & Packages

## What you'll learn
- Creating and importing modules
- `from ... import` syntax
- `__name__ == "__main__"` guard
- Packages and `__init__.py`
- pip and virtual environments
- requirements.txt
- Standard library overview
- Relative vs absolute imports

## Lesson

### Creating a module
```python
# mymath.py
def square(x): return x ** 2
PI = 3.14159

# main.py
import mymath
mymath.square(4)      # 16
from mymath import square, PI
square(4)             # 16 (no prefix)
```

### __name__ guard
```python
def greet(name): return f"Hi {name}"

if __name__ == "__main__":
    print(greet("World"))  # only runs when executed directly
```

### Packages
```
myapp/
├── __init__.py
├── utils.py
└── models/
    ├── __init__.py
    └── user.py
```
```python
from myapp.models.user import User
```

### Virtual environments
```bash
python -m venv venv
source venv/bin/activate
pip install requests
pip freeze > requirements.txt
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.py` — Create a module with a `greet(name)` function and a `PI` constant. Use `__name__ == "__main__"` to print a greeting when run directly.
2. `easy/p02-solve.py` — Write a script that imports `math` and `random` from the standard library. Use `math.sqrt` and `random.randint` to generate 3 random numbers and print their square roots.
3. `easy/p03-solve.py` — Create a module `string_utils.py` with `reverse_string(s)` and `count_vowels(s)` functions. Write a main script that imports and uses both.

### Medium
4. `medium/p01-solve.py` — Create a package structure: `myapp/__init__.py`, `myapp/utils.py` (with a `format_date()` function), `myapp/models/__init__.py`, `myapp/models/user.py` (with a `User` class). Write a test script that imports from the package.
5. `medium/p02-solve.py` — Write a CLI tool using `sys.argv` and `__name__ == "__main__"` that takes a temperature and unit (C or F) as arguments and converts between Celsius and Fahrenheit.
6. `medium/p03-solve.py` — Write a script that uses `os` and `pathlib` to list all `.py` files in the current directory and print their sizes.

### Hard
7. `hard/p01-solve.py` — Create a calculator package with separate modules for basic ops (add, sub, mul, div) and advanced ops (power, sqrt, factorial). Use `__init__.py` to expose all functions at the package level. Write a test script.
8. `hard/p02-solve.py` — Write a requirements.txt generator script that scans a Python file for `import` statements, identifies third-party packages (not standard library), and writes them to a requirements.txt file.
9. `hard/p03-solve.py` — Create a plugin system: a `plugins/` package where each `.py` file is a plugin with a `run()` function. Write a loader that dynamically imports all plugins and runs them.

### How to work
- Write your complete solution from scratch below the TODO marker.
- Remove the TODO line when done.
