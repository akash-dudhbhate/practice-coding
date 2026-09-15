"""SOLUTION: FastAPI books CRUD with SQLite (Hard)"""
import sqlite3
from fastapi import FastAPI, HTTPException, Depends, Query
from pydantic import BaseModel

app = FastAPI()
DB_PATH = "books.db"

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()

class BookCreate(BaseModel):
    title: str
    author: str
    year: int

class Book(BookCreate):
    id: int

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER)")
    conn.commit()
    conn.close()

@app.get("/books")
def list_books(author: str = Query(None), skip: int = 0, limit: int = 10, db = Depends(get_db)):
    if author:
        rows = db.execute("SELECT * FROM books WHERE author LIKE ? LIMIT ? OFFSET ?", (f"%{author}%", limit, skip)).fetchall()
    else:
        rows = db.execute("SELECT * FROM books LIMIT ? OFFSET ?", (limit, skip)).fetchall()
    return [dict(r) for r in rows]

@app.post("/books", response_model=Book, status_code=201)
def create_book(book: BookCreate, db = Depends(get_db)):
    cursor = db.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (book.title, book.author, book.year))
    db.commit()
    return Book(id=cursor.lastrowid, **book.dict())

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int, db = Depends(get_db)):
    row = db.execute("SELECT * FROM books WHERE id = ?", (book_id,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Book not found")
    return dict(row)

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db = Depends(get_db)):
    cursor = db.execute("DELETE FROM books WHERE id = ?", (book_id,))
    db.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"deleted": book_id}

if __name__ == "__main__":
    init_db()
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
