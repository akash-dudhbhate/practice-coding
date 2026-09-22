"""
LESSON 19 — FastAPI Server
EASY P02 — Pydantic Product Model
============================================

CONCEPT:
  A `BaseModel` subclass declares the request body shape. FastAPI
  validates incoming JSON against it and rejects bad payloads with
  422 automatically.

PROBLEM:
  Create a Pydantic model `Product` (name: str, price: float,
  in_stock: bool = True) and `POST /products` on a FastAPI `app`
  that accepts and returns the product.

TRY THIS INPUT:
  ```python
  from fastapi.testclient import TestClient
  client = TestClient(app)
  r = client.post("/products", json={"name": "Book", "price": 9.99})
  print(r.status_code, r.json())
  ```

EXPECTED OUTPUT:
  ```
  200 {'name': 'Book', 'price': 9.99, 'in_stock': True}
  ```

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
