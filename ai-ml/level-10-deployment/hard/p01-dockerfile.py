"""
LEVEL 10 — Model Deployment
HARD P01 — Write a Dockerfile
========================================

CONCEPT:
  Docker packages your app + dependencies into a container.
  Anyone can run it — "works on my machine" becomes "works everywhere."

  A Dockerfile for an ML API:
    FROM python:3.10-slim      — base image
    WORKDIR /app               — working directory
    COPY requirements.txt .    — deps first (caching)
    RUN pip install -r requirements.txt
    COPY . .                   — app code
    CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]

PROBLEM:
  Write `generate_dockerfile()` that returns a Dockerfile string
  for a FastAPI app with requirements.txt containing
  fastapi, uvicorn, scikit-learn, pandas.

TRY THIS INPUT:
  ```python
  df = generate_dockerfile()
  print(df)   # the Dockerfile content as a string
  ```

EXPECTED OUTPUT:
  ```
  FROM python:3.10-slim
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install -r requirements.txt
  COPY . .
  CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
  ```

HINT:
  Multi-line string with the Dockerfile steps.

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# print(generate_dockerfile())
