# Lesson 15 — Approach Comparison

## Problem: Test a Function

### Approach 1: unittest
```python
import unittest
class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
```

### Approach 2: pytest
```python
def test_add():
    assert add(1, 2) == 3
```

**Winner:** Approach 2 (pytest) — less boilerplate, better assertions, fixtures.

---

## Problem: Mock External API

### Approach 1: Manual mock
```python
def test_fetch():
    original = requests.get
    requests.get = lambda *a, **k: Mock(text="data")
    try:
        assert fetch() == "data"
    finally:
        requests.get = original
```

### Approach 2: patch
```python
from unittest.mock import patch
@patch("requests.get")
def test_fetch(mock_get):
    mock_get.return_value.text = "data"
    assert fetch() == "data"
```

**Winner:** Approach 2 — auto-restores, cleaner.
