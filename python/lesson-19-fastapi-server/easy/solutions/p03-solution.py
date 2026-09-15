"""SOLUTION: FastAPI query params (Easy)"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def get_users(skip: int = 0, limit: int = 10, active: bool = True):
    return {"skip": skip, "limit": limit, "active": active}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
