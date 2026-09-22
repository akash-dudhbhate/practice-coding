"""
LESSON 19 — FastAPI Server
HARD P03 — Async Endpoints
============================================

CONCEPT:
  FastAPI routes can be `async def` — they run on the event loop.
  Inside them, `asyncio.gather` fans out concurrent async work.

PROBLEM:
  Build a FastAPI `app` with:
    - GET /weather/{city} — async; awaits a simulated fetch
      (asyncio.sleep) and returns {"city": ..., "temp": ...,
      "condition": ...}
    - POST /notify — accepts {"users": [...], "message": ...} and
      sends notifications to all users concurrently via
      asyncio.gather, returning {"notifications": [...]}.

TRY THIS INPUT:
  ```python
  from fastapi.testclient import TestClient
  client = TestClient(app)
  print(client.get("/weather/Paris").json())
  r = client.post("/notify", json={"users": ["a", "b"], "message": "hi"})
  print(len(r.json()["notifications"]))
  ```

EXPECTED OUTPUT:
  ```
  {'city': 'Paris', 'temp': 25, 'condition': 'sunny'}
  2
  ```

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
