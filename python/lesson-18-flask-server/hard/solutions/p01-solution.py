"""SOLUTION: Flask blog API with SQLite (Hard)"""
import sqlite3
from flask import Flask, request, jsonify, g

app = Flask(__name__)
DB_PATH = "blog.db"

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(error):
    db = g.pop("db", None)
    if db: db.close()

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY, title TEXT, content TEXT, tag TEXT);
        CREATE TABLE IF NOT EXISTS comments (id INTEGER PRIMARY KEY, post_id INTEGER, text TEXT);
    """)
    conn.commit()
    conn.close()

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(400)
def bad_request(e):
    return jsonify({"error": "Bad request"}), 400

@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Server error"}), 500

@app.route("/posts", methods=["GET"])
def list_posts():
    tag = request.args.get("tag")
    db = get_db()
    if tag:
        posts = db.execute("SELECT * FROM posts WHERE tag = ?", (tag,)).fetchall()
    else:
        posts = db.execute("SELECT * FROM posts").fetchall()
    return jsonify([dict(p) for p in posts])

@app.route("/posts", methods=["POST"])
def create_post():
    data = request.get_json()
    db = get_db()
    cursor = db.execute("INSERT INTO posts (title, content, tag) VALUES (?, ?, ?)",
                        (data.get("title"), data.get("content"), data.get("tag")))
    db.commit()
    return jsonify({"id": cursor.lastrowid}), 201

@app.route("/posts/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):
    db = get_db()
    db.execute("DELETE FROM posts WHERE id = ?", (post_id,))
    db.commit()
    return "", 204

@app.route("/posts/<int:post_id>/comments", methods=["POST"])
def add_comment(post_id):
    data = request.get_json()
    db = get_db()
    cursor = db.execute("INSERT INTO comments (post_id, text) VALUES (?, ?)", (post_id, data.get("text")))
    db.commit()
    return jsonify({"id": cursor.lastrowid}), 201

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
