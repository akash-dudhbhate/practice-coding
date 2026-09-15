# Lesson 16 — Refactoring Challenges

## Refactor 01 (Easy): No Status Code Check
### Before
```python
data = requests.get(url).json()
```
### After
```python
res = requests.get(url)
res.raise_for_status()
data = res.json()
```

## Refactor 02 (Medium): Repeated Route Definitions
### Before
```python
@app.get("/users")
def list_users(): return users_db.all()
@app.get("/posts")
def list_posts(): return posts_db.all()
```
### After
```python
def create_crud_routes(app, path, db):
    @app.get(f"/{path}")
    def list_all(): return db.all()

create_crud_routes(app, "users", users_db)
create_crud_routes(app, "posts", posts_db)
```

## Refactor 03 (Hard): No Schema Validation
### Before
```python
@app.post("/users")
def create_user():
    data = request.json
    # no validation — crashes on bad data
    return db.insert(data)
```
### After
```python
from pydantic import BaseModel
class UserCreate(BaseModel):
    name: str
    email: str
    age: int = 0

@app.post("/users")
def create_user():
    user = UserCreate(**request.json)
    return db.insert(user.dict())
```
