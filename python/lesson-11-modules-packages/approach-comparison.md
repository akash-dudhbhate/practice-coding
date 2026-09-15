# Lesson 11 — Approach Comparison

## Problem: Organize a Project

### Approach 1: Flat structure
```
project/
  main.py
  utils.py
  db.py
  models.py
```
**Cons:** Hard to find things as project grows.

### Approach 2: Package structure
```
project/
  __init__.py
  main.py
  utils/
    __init__.py
    text.py
    math.py
  db/
    __init__.py
    connection.py
```
**Pros:** Scalable, clear organization.

**Winner:** Approach 2 — packages scale better.
