"""SOLUTION: Flask with decorator middleware (Hard)"""
import time
from functools import wraps
from flask import Flask, request, jsonify

app = Flask(__name__)
API_KEY = "secret123"
request_log = []
rate_limit_store = {}

def require_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if request.headers.get("X-API-Key") != API_KEY:
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return wrapper

def rate_limit(max_requests=5, window=60):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            ip = request.remote_addr
            now = time.time()
            if ip not in rate_limit_store:
                rate_limit_store[ip] = []
            rate_limit_store[ip] = [t for t in rate_limit_store[ip] if now - t < window]
            if len(rate_limit_store[ip]) >= max_requests:
                return jsonify({"error": "Rate limit exceeded"}), 429
            rate_limit_store[ip].append(now)
            return f(*args, **kwargs)
        return wrapper
    return decorator

def log_request(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        response = f(*args, **kwargs)
        request_log.append({"method": request.method, "path": request.path, "status": response[1] if isinstance(response, tuple) else 200})
        return response
    return wrapper

@app.route("/api/protected")
@log_request
@rate_limit(max_requests=3)
@require_auth
def protected():
    return jsonify({"data": "secret"})

if __name__ == "__main__":
    app.run(debug=True)
