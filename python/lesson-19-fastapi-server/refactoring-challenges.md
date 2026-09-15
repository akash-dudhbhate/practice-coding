# Lesson 19 — Refactoring Challenges

## Refactor 01 (Easy): No Type Hints
### Before
```python
@app.get("/users/{id}")
def get_user(id):
    user = db.get(id)
    return user
```
### After
```python
@app.get("/users/{id}")
def get_user(id: int) -> dict:
    user = db.get(id)
    return user
```

## Refactor 02 (Medium): No Pydantic Model
### Before
```python
@app.post("/users")
def create_user(user: dict):
    db.insert(user)
```
### After
```python
class UserCreate(BaseModel):
    name: str
    email: str

@app.post("/users")
def create_user(user: UserCreate):
    db.insert(user.dict())
```

## Refactor 03 (Hard): Sync in Async Route
### Before
```python
@app.get("/data")
async def get_data():
    data = requests.get(url).json()  # blocking!
    return data
```
### After
```python
import httpx
@app.get("/data")
async def get_data():
    async with httpx.AsyncClient() as client:
        data = (await client.get(url)).json()
    return data
```
