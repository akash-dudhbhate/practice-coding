# Lesson 20 — Common Mistakes

## Mistake 01: Everything in one file
```python
# WRONG — 1000-line main.py
# CORRECT — split into modules
project/
  models.py
  services.py
  views.py
  main.py
```

## Mistake 02: Hardcoded configuration
```python
# WRONG
API_URL = "https://api.example.com"

# CORRECT
API_URL = os.getenv("API_URL", "https://default.example.com")
```

## Mistake 03: No error handling
```python
# WRONG — crashes on any error
def process(data):
    return transform(clean(data))

# CORRECT — graceful degradation
def process(data):
    try:
        return transform(clean(data))
    except Exception as e:
        logger.error(f"Processing failed: {e}")
        return None
```

## Mistake 04: No documentation
```python
# WRONG — no docstring
def process(data): ...

# CORRECT
def process(data: list[dict]) -> dict[str, int]:
    """Process raw data into summary statistics.
    
    Args:
        data: List of raw records.
    Returns:
        Summary dict mapping category to count.
    """
```

## Mistake 05: No tests
```python
# Always write tests for critical functions
def test_process():
    assert process([{"cat": "a"}]) == {"a": 1}
```
