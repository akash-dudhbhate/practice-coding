# Lesson 11 — Coding Check

## Easy

### p01-solve.py — Module with __name__ guard
- [ ] `greet("Akash")` returns `"Hi Akash"` (or similar greeting)
- [ ] `PI` is accessible as a constant (3.14159 or similar)
- [ ] Running `python p01-solve.py` prints a greeting
- [ ] Importing the module does NOT print anything

### p02-solve.py — Standard library imports
- [ ] Uses `import math` and `import random`
- [ ] Generates 3 random numbers using `random.randint`
- [ ] Prints square roots using `math.sqrt`
- [ ] Output shows 3 numbers and their square roots

### p03-solve.py — String utils module
- [ ] `reverse_string("hello")` returns `"olleh"`
- [ ] `count_vowels("hello")` returns `2`
- [ ] Module can be imported without errors
- [ ] Main script uses both functions

## Medium

### p01-solve.py — Package structure
- [ ] `myapp/` folder exists with `__init__.py`
- [ ] `myapp/utils.py` has `format_date()` function
- [ ] `myapp/models/` folder exists with `__init__.py`
- [ ] `myapp/models/user.py` has `User` class
- [ ] Test script imports successfully: `from myapp.models.user import User`
- [ ] `from myapp.utils import format_date` works

### p02-solve.py — CLI temperature converter
- [ ] `python p02-solve.py 25 C` outputs Fahrenheit conversion
- [ ] `python p02-solve.py 77 F` outputs Celsius conversion
- [ ] No arguments → prints usage message
- [ ] Invalid unit → prints error message
- [ ] Uses `sys.argv` for argument parsing

### p03-solve.py — File listing with os/pathlib
- [ ] Lists all `.py` files in current directory
- [ ] Prints file name and size for each
- [ ] Uses `os` or `pathlib` (or both)
- [ ] Handles empty directory gracefully

## Hard

### p01-solve.py — Calculator package
- [ ] `calculator/` package with `basic.py` and `advanced.py` modules
- [ ] `basic.py` has: add, subtract, multiply, divide
- [ ] `advanced.py` has: power, sqrt, factorial
- [ ] `__init__.py` exposes all functions: `from calculator import add, power`
- [ ] Divide by zero returns error message or raises appropriate exception
- [ ] Test script demonstrates all operations

### p02-solve.py — Requirements generator
- [ ] Reads a Python file and finds all `import X` and `from X import Y` statements
- [ ] Distinguishes standard library from third-party (using sys.stdlib_module_names or a hardcoded list)
- [ ] Outputs third-party packages to requirements.txt
- [ ] Handles syntax errors in the input file gracefully

### p03-solve.py — Plugin system
- [ ] `plugins/` package exists with at least 2 plugin files
- [ ] Each plugin has a `run()` function
- [ ] Loader dynamically imports all plugins (using importlib or __import__)
- [ ] Loader runs all plugins and prints results
- [ ] Adding a new plugin file works without modifying the loader
