# Lesson 20 — Approach Comparison

## Problem: Project Structure

### Approach 1: Flat
```
project/
  main.py
  utils.py
  models.py
```
**Cons:** Hard to navigate as project grows.

### Approach 2: Layered
```
project/
  main.py
  config.py
  models/
    __init__.py
    user.py
    product.py
  services/
    __init__.py
    auth.py
    email.py
  views/
    __init__.py
    user_view.py
```
**Pros:** Clear separation, scalable.

**Winner:** Approach 2 — scales with project size.

---

## Problem: Configuration Management

### Approach 1: Constants file
```python
# config.py
DB_URL = "postgresql://..."
API_KEY = "abc123"
```
**Cons:** Can't change without redeploying. Secrets in code.

### Approach 2: Environment variables
```python
# config.py
import os
DB_URL = os.environ["DB_URL"]
API_KEY = os.environ["API_KEY"]
```
**Pros:** 12-factor app compliant. Secrets not in code.

### Approach 3: pydantic Settings
```python
from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    db_url: str
    api_key: str
    class Config:
        env_file = ".env"
```
**Pros:** Type validation, .env support, defaults.

**Winner:** Approach 3 (pydantic) for production. Approach 2 for simple projects.
