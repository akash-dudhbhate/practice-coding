"""SOLUTION: FastAPI todo CRUD (Medium)"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class TodoCreate(BaseModel):
    title: str
    done: bool = False

class Todo(TodoCreate):
    id: int

todos = []
next_id = 1

@app.get("/todos")
def list_todos():
    return todos

@app.post("/todos", status_code=201)
def create_todo(todo: TodoCreate):
    global next_id
    new_todo = Todo(id=next_id, **todo.dict())
    todos.append(new_todo.dict())
    next_id += 1
    return new_todo

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: TodoCreate):
    for i, t in enumerate(todos):
        if t["id"] == todo_id:
            updated = Todo(id=todo_id, **todo.dict())
            todos[i] = updated.dict()
            return updated
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return {"deleted": todo_id}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
