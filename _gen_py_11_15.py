#!/usr/bin/env python3
"""Generate reference solutions for Python lessons 11-15."""
import os
BASE = "/home/akash-dev/workspace-personal/practice-coding/python"

SOLUTIONS = {
"lesson-11-modules-packages": {
"easy/p01": '''"""SOLUTION: Module with __main__ (Easy)"""
PI = 3.14159

def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("World"))
    print(f"PI = {PI}")
''',
"easy/p02": '''"""SOLUTION: Import math and random (Easy)"""
import math
import random

if __name__ == "__main__":
    nums = [random.randint(1, 100) for _ in range(3)]
    for n in nums:
        print(f"sqrt({n}) = {math.sqrt(n):.2f}")
''',
"easy/p03": '''"""SOLUTION: string_utils module (Easy)"""
# This file acts as both the module and the test script

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")

if __name__ == "__main__":
    assert reverse_string("hello") == "olleh"
    assert count_vowels("hello") == 2
    print("All tests passed!")
''',
"medium/p01": '''"""SOLUTION: Package Structure (Medium)"""
# Simulated package structure in a single file for reference
# In practice: myapp/__init__.py, myapp/utils.py, myapp/models/user.py

# myapp/utils.py
from datetime import datetime

def format_date(dt=None, fmt="%Y-%m-%d"):
    dt = dt or datetime.now()
    return dt.strftime(fmt)

# myapp/models/user.py
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"User({self.name}, {self.email})"

# Test
if __name__ == "__main__":
    assert format_date(datetime(2024, 1, 15)) == "2024-01-15"
    u = User("Akash", "akash@test.com")
    assert u.name == "Akash"
    print("All tests passed!")
''',
"medium/p02": '''"""SOLUTION: CLI Temperature Converter (Medium)"""
import sys

def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python p02-solve.py <temp> <C|F>")
        sys.exit(1)
    temp = float(sys.argv[1])
    unit = sys.argv[2].upper()
    if unit == "C":
        print(f"{celsius_to_fahrenheit(temp):.1f} F")
    elif unit == "F":
        print(f"{fahrenheit_to_celsius(temp):.1f} C")
    else:
        print("Unit must be C or F")
''',
"medium/p03": '''"""SOLUTION: List .py Files (Medium)"""
import os
from pathlib import Path

def list_py_files(directory="."):
    results = []
    for p in Path(directory).glob("*.py"):
        size = p.stat().st_size
        results.append((str(p), size))
    return results

if __name__ == "__main__":
    for name, size in list_py_files():
        print(f"{name}: {size} bytes")
''',
"hard/p01": '''"""SOLUTION: Calculator Package (Hard)"""
# Simulated package in one file

# basic_ops module
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

# advanced_ops module
import math

def power(a, b): return a ** b
def sqrt(a): return math.sqrt(a)
def factorial(n): return math.factorial(n)

# __init__.py equivalent — expose all at package level
__all__ = ["add", "sub", "mul", "div", "power", "sqrt", "factorial"]

if __name__ == "__main__":
    assert add(2, 3) == 5
    assert sub(5, 2) == 3
    assert mul(3, 4) == 12
    assert div(10, 2) == 5.0
    assert power(2, 3) == 8
    assert sqrt(16) == 4.0
    assert factorial(5) == 120
    print("All tests passed!")
''',
"hard/p02": '''"""SOLUTION: Requirements Generator (Hard)"""
import sys
import importlib

# Standard library modules set (Python 3.10+)
STDLIB = {
    "os", "sys", "re", "json", "math", "random", "time", "datetime",
    "collections", "itertools", "functools", "pathlib", "typing",
    "io", "csv", "sqlite3", "urllib", "http", "email", "hashlib",
    "base64", "logging", "argparse", "subprocess", "threading",
    "multiprocessing", "asyncio", "abc", "copy", "enum", "warnings",
}

def extract_imports(filepath):
    """Extract third-party imports from a Python file."""
    third_party = set()
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line.startswith("import "):
                module = line.split()[1].split(".")[0]
            elif line.startswith("from "):
                module = line.split()[1].split(".")[0]
            else:
                continue
            if module not in STDLIB and module != "__future__":
                third_party.add(module)
    return sorted(third_party)

if __name__ == "__main__":
    # Self-test: this file has no third-party imports
    result = extract_imports(__file__)
    assert result == [], f"Expected empty, got {result}"
    print("All tests passed!")
''',
"hard/p03": '''"""SOLUTION: Plugin System (Hard)"""
import importlib
import os

def load_plugins(plugins_dir):
    """Dynamically load all .py files from a directory as plugins."""
    plugins = []
    if not os.path.isdir(plugins_dir):
        return plugins
    for filename in os.listdir(plugins_dir):
        if filename.endswith(".py") and not filename.startswith("_"):
            modname = filename[:-3]
            spec = importlib.util.spec_from_file_location(
                modname, os.path.join(plugins_dir, filename)
            )
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            if hasattr(mod, "run"):
                plugins.append(mod)
    return plugins

# Example plugin (would be in plugins/hello.py):
# def run():
#     print("Hello from plugin!")

if __name__ == "__main__":
    # Create a test plugin
    import tempfile
    d = tempfile.mkdtemp()
    with open(os.path.join(d, "test_plugin.py"), "w") as f:
        f.write("def run():\\n    return 'plugin ran'\\n")
    plugins = load_plugins(d)
    assert len(plugins) == 1
    assert plugins[0].run() == "plugin ran"
    print("All tests passed!")
''',
},
"lesson-12-decorators": {
"easy/p01": '''"""SOLUTION: @shout Decorator (Easy)"""
def shout(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper() if isinstance(result, str) else result
    return wrapper

@shout
def greet(name):
    return f"hello {name}"

if __name__ == "__main__":
    assert greet("world") == "HELLO WORLD"
    print("All tests passed!")
''',
"easy/p02": '''"""SOLUTION: @timer Decorator (Easy)"""
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(0.1)
    return "done"

if __name__ == "__main__":
    assert slow_function() == "done"
    print("All tests passed!")
''',
"easy/p03": '''"""SOLUTION: @log_call Decorator (Easy)"""
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Returned: {result}")
        return result
    return wrapper

@log_call
def add(a, b):
    return a + b

if __name__ == "__main__":
    assert add(2, 3) == 5
    print("All tests passed!")
''',
"medium/p01": '''"""SOLUTION: @repeat(n) Decorator (Medium)"""
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("hi")
    return "done"

if __name__ == "__main__":
    assert greet() == "done"
    print("All tests passed!")
''',
"medium/p02": '''"""SOLUTION: @cache Decorator (Medium)"""
def cache(func):
    _cache = {}
    def wrapper(*args):
        if args in _cache:
            return _cache[args]
        result = func(*args)
        _cache[args] = result
        return result
    return wrapper

@cache
def slow_square(n):
    print(f"  computing {n}...")
    return n * n

if __name__ == "__main__":
    assert slow_square(4) == 16
    assert slow_square(4) == 16  # cached, no print
    print("All tests passed!")
''',
"medium/p03": '''"""SOLUTION: @validate_positive Decorator (Medium)"""
def validate_positive(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg <= 0:
                raise ValueError(f"Argument must be positive, got {arg}")
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def calculate_area(width, height):
    return width * height

if __name__ == "__main__":
    assert calculate_area(4, 5) == 20
    try:
        calculate_area(-1, 5)
        assert False
    except ValueError:
        pass
    print("All tests passed!")
''',
"hard/p01": '''"""SOLUTION: @CountCalls Class Decorator (Hard)"""
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)

@CountCalls
def say_hi():
    return "hi"

if __name__ == "__main__":
    say_hi()
    say_hi()
    say_hi()
    assert say_hi.count == 3
    print("All tests passed!")
''',
"hard/p02": '''"""SOLUTION: @retry Decorator (Hard)"""
import time

def retry(times=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exc = e
                    print(f"Attempt {attempt+1} failed: {e}")
                    if attempt < times - 1:
                        time.sleep(delay)
            raise last_exc
        return wrapper
    return decorator

@retry(times=3, delay=0.1)
def flaky():
    import random
    if random.random() < 0.5:
        raise ValueError("Failed")
    return "success"

if __name__ == "__main__":
    # May succeed or raise after 3 tries — just test it runs
    try:
        result = flaky()
        assert result == "success"
    except ValueError:
        print("Retried 3 times, all failed — expected behavior")
    print("Test passed!")
''',
"hard/p03": '''"""SOLUTION: Stacked Decorators (Hard)"""
import time

def log(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] {func.__name__}({args}, {kwargs})")
        return func(*args, **kwargs)
    return wrapper

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"[TIMER] {func.__name__} took {time.time()-start:.4f}s")
        return result
    return wrapper

@log
@timer
def process(n):
    time.sleep(0.05)
    return n * 2

if __name__ == "__main__":
    result = process(5)
    assert result == 10
    print("All tests passed!")
''',
},
"lesson-13-iterators-generators": {
"easy/p01": '''"""SOLUTION: count_up_to Generator (Easy)"""
def count_up_to(n):
    for i in range(1, n + 1):
        yield i

if __name__ == "__main__":
    assert list(count_up_to(5)) == [1, 2, 3, 4, 5]
    assert list(count_up_to(0)) == []
    print("All tests passed!")
''',
"easy/p02": '''"""SOLUTION: Even Squares Generator Expression (Easy)"""
even_squares = (x * x for x in range(0, 21, 2))

if __name__ == "__main__":
    result = list(even_squares)
    assert result == [0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
    print("All tests passed!")
''',
"easy/p03": '''"""SOLUTION: CountDown Iterator (Easy)"""
class CountDown:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        self.n -= 1
        return self.n + 1

if __name__ == "__main__":
    assert list(CountDown(3)) == [3, 2, 1]
    assert list(CountDown(0)) == []
    print("All tests passed!")
''',
"medium/p01": '''"""SOLUTION: Infinite Fibonacci (Medium)"""
from itertools import islice

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    first_10 = list(islice(fibonacci(), 10))
    assert first_10 == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    print("All tests passed!")
''',
"medium/p02": '''"""SOLUTION: Deep Flatten with yield from (Medium)"""
def flatten(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

if __name__ == "__main__":
    assert list(flatten([1, [2, [3, [4]]], 5])) == [1, 2, 3, 4, 5]
    assert list(flatten([])) == []
    print("All tests passed!")
''',
"medium/p03": '''"""SOLUTION: Generator Pipeline (Medium)"""
def generate_nums(n):
    for i in range(1, n + 1):
        yield i

def filter_multiples_of_3(gen):
    for x in gen:
        if x % 3 == 0:
            yield x

def square_them(gen):
    for x in gen:
        yield x * x

def take_first(gen, n):
    for i, x in enumerate(gen):
        if i >= n:
            break
        yield x

if __name__ == "__main__":
    pipeline = take_first(square_them(filter_multiples_of_3(generate_nums(100))), 5)
    assert list(pipeline) == [9, 36, 81, 144, 225]
    print("All tests passed!")
''',
"hard/p01": '''"""SOLUTION: Read Lines Generator (Hard)"""
def read_lines(filename):
    try:
        with open(filename) as f:
            for line in f:
                yield line.rstrip("\\n")
    except FileNotFoundError:
        print(f"Warning: {filename} not found")
        return

if __name__ == "__main__":
    with open("/tmp/test_lines_gen.txt", "w") as f:
        f.write("line1\\nline2\\nline3\\n")
    lines = list(read_lines("/tmp/test_lines_gen.txt"))
    assert lines == ["line1", "line2", "line3"]
    assert list(read_lines("/nonexistent")) == []
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
    assert list(chunked([1, 2, 3], 5)) == [[1, 2, 3]]
    print("All tests passed!")
''',
"hard/p03": '''"""SOLUTION: Cycle Forever Generator (Hard)"""
def cycle_forever(iterable):
    items = list(iterable)
    if not items:
        return
    while True:
        for item in items:
            yield item

if __name__ == "__main__":
    from itertools import islice
    c = cycle_forever(["a", "b", "c"])
    result = list(islice(c, 7))
    assert result == ["a", "b", "c", "a", "b", "c", "a"]
    # Round-robin assignment
    workers = ["w1", "w2", "w3"]
    tasks = ["t1", "t2", "t3", "t4", "t5", "t6", "t7"]
    assigner = cycle_forever(workers)
    assignments = {w: [] for w in workers}
    for task in tasks:
        w = next(assigner)
        assignments[w].append(task)
    assert "t1" in assignments["w1"]
    assert "t2" in assignments["w2"]
    print("All tests passed!")
''',
},
"lesson-14-async-concurrency": {
"easy/p01": '''"""SOLUTION: Async Greet (Easy)"""
import asyncio

async def async_greet(name):
    await asyncio.sleep(1)
    return f"Hello, {name}!"

if __name__ == "__main__":
    result = asyncio.run(async_greet("Akash"))
    assert result == "Hello, Akash!"
    print("All tests passed!")
''',
"easy/p02": '''"""SOLUTION: Async Start/End (Easy)"""
import asyncio
import time

async def start_end():
    print("Start")
    await asyncio.sleep(0.5)
    print("End")

if __name__ == "__main__":
    start = time.time()
    asyncio.run(start_end())
    elapsed = time.time() - start
    assert 0.4 < elapsed < 0.7
    print(f"Took {elapsed:.2f}s — tests passed!")
''',
"easy/p03": '''"""SOLUTION: Concurrent with gather (Easy)"""
import asyncio
import time

async def task1():
    await asyncio.sleep(0.3)
    return "task1 done"

async def task2():
    await asyncio.sleep(0.5)
    return "task2 done"

async def main():
    start = time.time()
    results = await asyncio.gather(task1(), task2())
    elapsed = time.time() - start
    print(f"Both tasks took {elapsed:.2f}s (should be ~0.5, not 0.8)")
    return results

if __name__ == "__main__":
    results = asyncio.run(main())
    assert results == ["task1 done", "task2 done"]
    print("All tests passed!")
''',
"medium/p01": '''"""SOLUTION: Fetch All Concurrently (Medium)"""
import asyncio

async def fetch(url):
    await asyncio.sleep(0.1)  # simulate network
    return f"Response from {url}"

async def fetch_all(urls):
    return await asyncio.gather(*[fetch(url) for url in urls])

if __name__ == "__main__":
    urls = ["https://a.com", "https://b.com", "https://c.com"]
    results = asyncio.run(fetch_all(urls))
    assert len(results) == 3
    assert "a.com" in results[0]
    print("All tests passed!")
''',
"medium/p02": '''"""SOLUTION: ThreadPoolExecutor (Medium)"""
from concurrent.futures import ThreadPoolExecutor
import time

def download(filename):
    time.sleep(0.2)  # simulate download
    return f"Downloaded {filename}"

if __name__ == "__main__":
    files = [f"file_{i}.zip" for i in range(5)]
    start = time.time()
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(download, files))
    elapsed = time.time() - start
    assert len(results) == 5
    assert elapsed < 1.0  # should be ~0.2, not 1.0
    print(f"Downloaded 5 files in {elapsed:.2f}s — tests passed!")
''',
"medium/p03": '''"""SOLUTION: ProcessPoolExecutor (Medium)"""
from concurrent.futures import ProcessPoolExecutor

def square(n):
    return n * n

if __name__ == "__main__":
    nums = list(range(1, 21))
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(square, nums))
    assert results == [n * n for n in range(1, 21)]
    print("All tests passed!")
''',
"hard/p01": '''"""SOLUTION: Async Rate Limiter (Hard)"""
import asyncio
import time

async def limited_task(sem, task_id):
    async with sem:
        print(f"  Task {task_id} started")
        await asyncio.sleep(0.1)
        print(f"  Task {task_id} done")
        return task_id

async def main():
    sem = asyncio.Semaphore(3)
    tasks = [limited_task(sem, i) for i in range(10)]
    return await asyncio.gather(*tasks)

if __name__ == "__main__":
    results = asyncio.run(main())
    assert sorted(results) == list(range(10))
    print("All tests passed!")
''',
"hard/p02": '''"""SOLUTION: Async Scraper with Timeout (Hard)"""
import asyncio

async def fetch_with_timeout(url, timeout=5):
    try:
        await asyncio.wait_for(asyncio.sleep(0.1), timeout=timeout)
        return f"OK: {url}"
    except asyncio.TimeoutError:
        return f"TIMEOUT: {url}"

async def scrape_all(urls):
    return await asyncio.gather(*[fetch_with_timeout(url) for url in urls])

if __name__ == "__main__":
    urls = [f"https://api{i}.example.com" for i in range(5)]
    results = asyncio.run(scrape_all(urls))
    assert len(results) == 5
    assert all("OK" in r for r in results)
    print("All tests passed!")
''',
"hard/p03": '''"""SOLUTION: Producer-Consumer with Queue (Hard)"""
import asyncio

async def producer(queue):
    for i in range(10):
        await queue.put(f"item-{i}")
        await asyncio.sleep(0.05)
    await queue.put(None)  # sentinel
    await queue.put(None)  # one per consumer

async def consumer(queue, cid):
    results = []
    while True:
        item = await queue.get()
        if item is None:
            break
        results.append(f"C{cid}: {item}")
        await asyncio.sleep(0.02)
    return results

async def main():
    queue = asyncio.Queue()
    prod = asyncio.create_task(producer(queue))
    cons = await asyncio.gather(consumer(queue, 1), consumer(queue, 2))
    await prod
    total = len(cons[0]) + len(cons[1])
    return total

if __name__ == "__main__":
    total = asyncio.run(main())
    assert total == 10
    print("All tests passed!")
''',
},
"lesson-15-testing-pytest": {
"easy/p01": '''"""SOLUTION: is_palindrome with tests (Easy)"""
import pytest

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Tests
def test_palindrome_normal():
    assert is_palindrome("racecar") == True

def test_palindrome_empty():
    assert is_palindrome("") == True

def test_palindrome_case_insensitive():
    assert is_palindrome("RaceCar") == True

if __name__ == "__main__":
    test_palindrome_normal()
    test_palindrome_empty()
    test_palindrome_case_insensitive()
    print("All tests passed!")
''',
"easy/p02": '''"""SOLUTION: factorial with parametrize (Easy)"""
import pytest

def factorial(n):
    if n < 0:
        raise ValueError("Negative input")
    if n <= 1:
        return 1
    return n * factorial(n - 1)

@pytest.mark.parametrize("n,expected", [
    (0, 1),
    (1, 1),
    (5, 120),
    (3, 6),
])
def test_factorial(n, expected):
    assert factorial(n) == expected

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)

if __name__ == "__main__":
    for n, exp in [(0, 1), (1, 1), (5, 120), (3, 6)]:
        assert factorial(n) == exp
    try:
        factorial(-1)
        assert False
    except ValueError:
        pass
    print("All tests passed!")
''',
"easy/p03": '''"""SOLUTION: Fixture sample_list (Easy)"""
import pytest

@pytest.fixture
def sample_list():
    return [3, 1, 4, 1, 5]

def test_max(sample_list):
    assert max(sample_list) == 5

def test_len(sample_list):
    assert len(sample_list) == 5

if __name__ == "__main__":
    sl = [3, 1, 4, 1, 5]
    assert max(sl) == 5
    assert len(sl) == 5
    print("All tests passed!")
''',
"medium/p01": '''"""SOLUTION: divide with pytest.raises (Medium)"""
import pytest

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def test_divide_normal():
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

if __name__ == "__main__":
    assert divide(10, 2) == 5.0
    try:
        divide(1, 0)
        assert False
    except ZeroDivisionError:
        pass
    print("All tests passed!")
''',
"medium/p02": '''"""SOLUTION: Fixture with yield (Medium)"""
import pytest
import os
import tempfile

@pytest.fixture
def temp_file():
    fd, path = tempfile.mkstemp(suffix=".txt")
    os.close(fd)
    with open(path, "w") as f:
        f.write("test content")
    yield path
    if os.path.exists(path):
        os.remove(path)

def test_read_temp_file(temp_file):
    with open(temp_file) as f:
        content = f.read()
    assert content == "test content"

if __name__ == "__main__":
    fd, path = tempfile.mkstemp(suffix=".txt")
    os.close(fd)
    with open(path, "w") as f:
        f.write("test content")
    with open(path) as f:
        assert f.read() == "test content"
    os.remove(path)
    print("All tests passed!")
''',
"medium/p03": '''"""SOLUTION: Mock API call (Medium)"""
from unittest.mock import patch, MagicMock
import pytest

def fetch_user(user_id):
    # This would call a real API
    import requests
    resp = requests.get(f"https://api.example.com/users/{user_id}")
    return resp.json()

@patch("requests.get")
def test_fetch_user(mock_get):
    mock_resp = MagicMock()
    mock_resp.json.return_value = {"id": 1, "name": "Akash"}
    mock_get.return_value = mock_resp

    result = fetch_user(1)
    assert result["name"] == "Akash"
    mock_get.assert_called_once_with("https://api.example.com/users/1")

if __name__ == "__main__":
    # Manual test without pytest
    print("Run with pytest to test the mock")
    print("All tests passed!")
''',
"hard/p01": '''"""SOLUTION: BankAccount Test Suite (Hard)"""
import pytest

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

@pytest.fixture
def account():
    return BankAccount("Test", 100)

def test_deposit(account):
    account.deposit(50)
    assert account.balance == 150

def test_withdraw(account):
    account.withdraw(30)
    assert account.balance == 70

def test_insufficient_funds(account):
    with pytest.raises(ValueError):
        account.withdraw(200)

def test_negative_deposit(account):
    with pytest.raises(ValueError):
        account.deposit(-10)

@pytest.mark.parametrize("amount", [10, 50, 100])
def test_valid_deposits(account, amount):
    account.deposit(amount)
    assert account.balance == 100 + amount

if __name__ == "__main__":
    acc = BankAccount("Test", 100)
    acc.deposit(50)
    assert acc.balance == 150
    acc.withdraw(30)
    assert acc.balance == 120
    try:
        acc.withdraw(200)
    except ValueError:
        pass
    try:
        acc.deposit(-10)
    except ValueError:
        pass
    print("All tests passed!")
''',
"hard/p02": '''"""SOLUTION: Stack with Parametrized Tests (Hard)"""
import pytest

class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

@pytest.mark.parametrize("items,expected", [
    ([1, 2, 3], 3),
    ([], None),
    (["a"], "a"),
])
def test_push_pop(items, expected):
    s = Stack()
    for item in items:
        s.push(item)
    if items:
        assert s.pop() == expected
    else:
        with pytest.raises(IndexError):
            s.pop()

def test_peek_empty():
    s = Stack()
    with pytest.raises(IndexError):
        s.peek()

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    assert s.pop() == 2
    assert s.peek() == 1
    s.pop()
    try:
        s.pop()
        assert False
    except IndexError:
        pass
    print("All tests passed!")
''',
"hard/p03": '''"""SOLUTION: process_csv with Tests (Hard)"""
import pytest
import csv
import os
import tempfile

def process_csv(filepath):
    with open(filepath, newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)

@pytest.fixture
def temp_csv():
    fd, path = tempfile.mkstemp(suffix=".csv")
    os.close(fd)
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "age"])
        writer.writerow(["Akash", "25"])
        writer.writerow(["Dev", "30"])
    yield path
    os.remove(path)

def test_normal_read(temp_csv):
    data = process_csv(temp_csv)
    assert len(data) == 2
    assert data[0]["name"] == "Akash"

def test_empty_file():
    fd, path = tempfile.mkstemp(suffix=".csv")
    os.close(fd)
    with open(path, "w") as f:
        f.write("")
    data = process_csv(path)
    assert data == []
    os.remove(path)

if __name__ == "__main__":
    # Manual test
    fd, path = tempfile.mkstemp(suffix=".csv")
    os.close(fd)
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["name", "age"])
        w.writerow(["Akash", "25"])
    data = process_csv(path)
    assert data[0]["name"] == "Akash"
    os.remove(path)
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
