"""SOLUTION: Flask todo REST API (Medium)"""
from flask import Flask, request, jsonify

app = Flask(__name__)
todos = []
next_id = 1

@app.route("/todos", methods=["GET"])
def list_todos():
    return jsonify(todos)

@app.route("/todos", methods=["POST"])
def create_todo():
    global next_id
    data = request.get_json()
    todo = {"id": next_id, "title": data.get("title", ""), "done": False}
    todos.append(todo)
    next_id += 1
    return jsonify(todo), 201

@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return "", 204

if __name__ == "__main__":
    app.run(debug=True)
