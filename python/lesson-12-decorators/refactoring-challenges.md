# Lesson 12 — Refactoring Challenges

## Refactor 01 (Easy): No @wraps
### Before
```python
def timer(func):
    def wrapper(*a, **k):
        return func(*a, **k)
    return wrapper
```
### After
```python
from functools import wraps
def timer(func):
    @wraps(func)
    def wrapper(*a, **k):
        return func(*a, **k)
    return wrapper
```

## Refactor 02 (Medium): Manual Timing
### Before
```python
def fetch_data():
    start = time.time()
    result = api.get()
    print(f"Took {time.time() - start}s")
    return result
```
### After
```python
@timer
def fetch_data():
    return api.get()
```

## Refactor 03 (Hard): Repeated Try/Except Pattern
### Before
```python
def fetch_user(): 
    try: return api.get_user()
    except: return None
def fetch_post():
    try: return api.get_post()
    except: return None
```
### After
```python
def safe_api(func):
    @wraps(func)
    def wrapper(*a, **k):
        try: return func(*a, **k)
        except: return None
    return wrapper

fetch_user = safe_api(api.get_user)
fetch_post = safe_api(api.get_post)
```
