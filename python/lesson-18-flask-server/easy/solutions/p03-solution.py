"""SOLUTION: Flask search with query param (Easy)"""
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/search")
def search():
    q = request.args.get("q", "")
    return jsonify({"query": q, "results": []})

if __name__ == "__main__":
    app.run(debug=True)
