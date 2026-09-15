# Lesson 15 — Refactoring Challenges

## Refactor 01 (Easy): No Assert
### Before
```python
def test_add():
    result = add(1, 2)
    if result == 3:
        print("pass")
```
### After
```python
def test_add():
    assert add(1, 2) == 3
```

## Refactor 02 (Medium): Repeated Setup
### Before
```python
def test_a():
    db = create_db()
    db.add("x")
    assert db.count() == 1
def test_b():
    db = create_db()
    db.add("y")
    assert db.count() == 1
```
### After
```python
@pytest.fixture
def db():
    return create_db()
def test_a(db):
    db.add("x")
    assert db.count() == 1
```

## Refactor 03 (Hard): Multiple Asserts in One Test
### Before
```python
def test_user():
    u = create_user("A")
    assert u.name == "A"
    assert u.age == 0
    assert u.email is None
    assert u.is_active
```
### After
```python
def test_user_name():
    assert create_user("A").name == "A"
def test_user_defaults():
    u = create_user("A")
    assert u.age == 0
    assert u.email is None
    assert u.is_active
```
