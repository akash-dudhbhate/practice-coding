# Lesson 15 — Testing with pytest

## What you'll learn
- Why automated testing matters
- pytest basics and test discovery
- assert statements
- Fixtures (setup/teardown with yield)
- @pytest.mark.parametrize
- Testing exceptions
- Mocking with unittest.mock
- Test coverage
- Test organization

## Lesson

### Basic test
```python
def test_add():
    assert add(2, 3) == 5
```

### Fixture
```python
@pytest.fixture
def sample_data():
    return [1, 2, 3]

def test_sum(sample_data):
    assert sum(sample_data) == 6
```

### Parametrize
```python
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3), (0, 0, 0), (-1, 1, 0)
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.py` — Write a function `is_palindrome(s)` and 3 pytest test functions for it (normal, empty, case-insensitive).
2. `easy/p02-solve.py` — Write a function `factorial(n)` and test it with `@pytest.mark.parametrize` using 5 test cases (0!, 1!, 5!, 3!, and negative input).
3. `easy/p03-solve.py` — Write a fixture `sample_list` that returns `[3, 1, 4, 1, 5]`. Write 2 tests using it: one for `max()`, one for `len()`.

### Medium
4. `medium/p01-solve.py` — Write a function `divide(a, b)` that raises `ZeroDivisionError` when b=0. Test that the exception is raised using `pytest.raises()`.
5. `medium/p02-solve.py` — Write a fixture with `yield` that creates a temporary file, yields its path, and cleans it up after the test. Write a test that reads the file.
6. `medium/p03-solve.py` — Write a function `fetch_user(user_id)` that calls an external API. Mock the API call using `unittest.mock.patch` and test the function without making a real HTTP request.

### Hard
7. `hard/p01-solve.py` — Write a `BankAccount` class (deposit, withdraw, balance). Write a complete test suite: test deposit, test withdraw, test insufficient funds (exception), test negative deposit (exception). Use fixtures and parametrize.
8. `hard/p02-solve.py` — Write a `Stack` class (push, pop, peek, is_empty). Write tests with parametrize for push/pop sequences. Test popping from empty stack raises exception.
9. `hard/p03-solve.py` — Write a function `process_csv(filepath)` that reads a CSV and returns list of dicts. Write tests using a fixture that creates a temp CSV file, tests normal reading, empty file, and malformed CSV.

### How to work
- Write your complete solution from scratch below the TODO marker.
- Remove the TODO line when done.
- Run tests with: `pytest <filename> -v`
