"""SOLUTION: Flask with blueprints (Medium)"""
from flask import Flask, Blueprint, request, jsonify

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")
api_bp = Blueprint("api", __name__, url_prefix="/api")

@auth_bp.route("/login", methods=["POST"])
def login():
    return jsonify({"status": "login endpoint"})

@auth_bp.route("/register", methods=["POST"])
def register():
    return jsonify({"status": "register endpoint"})

@api_bp.route("/items", methods=["GET"])
def list_items():
    return jsonify({"items": []})

@api_bp.route("/items", methods=["POST"])
def create_item():
    return jsonify({"status": "created"}), 201

app = Flask(__name__)
app.register_blueprint(auth_bp)
app.register_blueprint(api_bp)

if __name__ == "__main__":
    app.run(debug=True)
