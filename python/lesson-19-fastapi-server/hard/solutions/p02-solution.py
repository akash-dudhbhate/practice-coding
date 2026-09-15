"""SOLUTION: FastAPI auth with JWT (Hard)"""
from datetime import datetime, timedelta
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer
from pydantic import BaseModel
from jose import jwt

app = FastAPI()
SECRET = "my-secret"
ALGORITHM = "HS256"
users_db = {}
security = HTTPBearer()

class UserCreate(BaseModel):
    username: str
    password: str

class LoginRequest(BaseModel):
    username: str
    password: str

def create_token(username: str):
    payload = {"sub": username, "exp": datetime.utcnow() + timedelta(hours=24)}
    return jwt.encode(payload, SECRET, algorithm=ALGORITHM)

def get_current_user(credentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        username = payload["sub"]
        if username not in users_db:
            raise HTTPException(status_code=401, detail="Invalid token")
        return username
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/register")
def register(user: UserCreate):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="User exists")
    users_db[user.username] = user.password
    return {"status": "registered"}

@app.post("/login")
def login(req: LoginRequest):
    if users_db.get(req.username) != req.password:
        raise HTTPException(status_code=401, detail="Bad credentials")
    token = create_token(req.username)
    return {"access_token": token}

@app.get("/me")
def me(username: str = Depends(get_current_user)):
    return {"username": username}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
