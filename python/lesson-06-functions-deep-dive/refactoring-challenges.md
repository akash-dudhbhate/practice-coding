# Lesson 06 — Refactoring Challenges

## Refactor 01 (Easy): Repeated Function Calls
### Before
```python
def get_info(user):
    name = user.get("name")
    age = user.get("age")
    email = user.get("email")
    return f"{name}, {age}, {email}"
```
### After
```python
def get_info(user):
    return ", ".join(str(user.get(k, "")) for k in ("name", "age", "email"))
```

## Refactor 02 (Medium): Boolean Flag Parameter
### Before
```python
def process(data, is_upper):
    if is_upper:
        return data.upper()
    else:
        return data.lower()
```
### After
```python
def process(data, transform=str.upper):
    return transform(data)
```

## Refactor 03 (Hard): Long Parameter List
### Before
```python
def create_user(name, age, email, role, dept, salary, start_date):
    # ... 7 params, hard to read calls
```
### After
```python
from dataclasses import dataclass
@dataclass
class UserConfig:
    name: str
    age: int
    email: str
    role: str = "member"
    dept: str = "general"
    salary: float = 0
    start_date: str = ""

def create_user(config: UserConfig):
    # ... use config.name, config.age etc.
```
