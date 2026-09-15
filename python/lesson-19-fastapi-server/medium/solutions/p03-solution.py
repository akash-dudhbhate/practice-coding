"""SOLUTION: FastAPI separate input/output models (Medium)"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

users = []
next_id = 1

@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate):
    global next_id
    new_user = UserResponse(id=next_id, name=user.name, email=user.email)
    users.append({"id": next_id, **user.dict()})
    next_id += 1
    return new_user

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
