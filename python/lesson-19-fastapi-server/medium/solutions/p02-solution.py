"""SOLUTION: FastAPI dependency for pagination (Medium)"""
from fastapi import FastAPI, Depends

app = FastAPI()

def get_pagination(page: int = 1, size: int = 10):
    return {"skip": (page - 1) * size, "limit": size}

@app.get("/items")
def list_items(pagination: dict = Depends(get_pagination)):
    return {"pagination": pagination, "items": []}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
