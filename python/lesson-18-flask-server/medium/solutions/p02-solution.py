"""SOLUTION: Flask session-based login (Medium)"""
from flask import Flask, request, session, redirect, jsonify

app = Flask(__name__)
app.secret_key = "my-secret-key"

USERS = {"admin": "password123"}

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if USERS.get(username) == password:
        session["user"] = username
        return jsonify({"status": "logged in"})
    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return jsonify({"error": "Please login"}), 401
    return jsonify({"user": session["user"], "message": "Welcome!"})

@app.route("/logout")
def logout():
    session.pop("user", None)
    return jsonify({"status": "logged out"})

if __name__ == "__main__":
    app.run(debug=True)
