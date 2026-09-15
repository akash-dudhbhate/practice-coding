# Lesson 09 — Refactoring Challenges

## Refactor 01 (Easy): No __str__
### Before
```python
class User:
    def __init__(self, name):
        self.name = name
# print(user) → <__main__.User at 0x...>
```
### After
```python
class User:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"User({self.name})"
```

## Refactor 02 (Medium): Getter/Setter Instead of Property
### Before
```python
class Temperature:
    def __init__(self, c):
        self._c = c
    def get_celsius(self): return self._c
    def set_celsius(self, v): self._c = v
    def get_fahrenheit(self): return self._c * 9/5 + 32
```
### After
```python
class Temperature:
    def __init__(self, c): self._c = c
    @property
    def celsius(self): return self._c
    @celsius.setter
    def celsius(self, v): self._c = v
    @property
    def fahrenheit(self): return self._c * 9/5 + 32
```

## Refactor 03 (Hard): God Class
### Before
```python
class User:
    def __init__(self): ...
    def save_to_db(self): ...
    def send_email(self): ...
    def validate(self): ...
    def format_display(self): ...
```
### After
```python
class User: # data only
    def __init__(self): ...
class UserRepository: # persistence
    def save(self, user): ...
class EmailService: # email
    def send(self, user): ...
class UserValidator: # validation
    def validate(self, user): ...
```
