"""SOLUTION: FastAPI with Pydantic model (Easy)"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    name: str
    price: float
    in_stock: bool = True

@app.post("/products")
def create_product(product: Product):
    return product

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
