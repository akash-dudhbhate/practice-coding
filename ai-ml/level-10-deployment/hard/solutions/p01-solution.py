"""Level 10 Deployment — Hard P01 Solution"""

def solve():
    dockerfile = '''
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
'''
    requirements = '''
fastapi==0.104.1
uvicorn==0.24.0
scikit-learn==1.3.2
numpy==1.24.3
pandas==2.1.4
'''
    print("Dockerfile:")
    print(dockerfile)
    print("requirements.txt:")
    print(requirements)
    return dockerfile, requirements

if __name__ == "__main__":
    solve()