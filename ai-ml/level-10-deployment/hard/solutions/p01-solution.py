"""Level 10 — Model Deployment — Hard P01 Solution"""

def generate_dockerfile():
    return """FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]"""

if __name__ == "__main__":
    print(generate_dockerfile())
