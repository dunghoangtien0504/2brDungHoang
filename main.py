from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import sqlite3
import os
from typing import List, Optional

app = FastAPI()

import os

# Get absolute path to the current directory (project root)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'brain.db')
STATIC_PATH = os.path.join(BASE_DIR, 'static')

# Database connection helper
def get_db():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()

# Models
class Item(BaseModel):
    id: Optional[int] = None
    title: str
    content: str
    created_at: Optional[str] = None

class PasswordCheck(BaseModel):
    password: str

# Auth middleware (simple password check for this demo)
CORRECT_PASSWORD = "687568"

@app.post("/api/auth")
async def verify_password(data: PasswordCheck):
    if data.password == CORRECT_PASSWORD:
        return {"status": "success"}
    raise HTTPException(status_code=401, detail="Incorrect password")

# CRUD Routes
@app.get("/api/{table}")
async def get_items(table: str, db: sqlite3.Connection = Depends(get_db)):
    if table not in ["knowledge", "business", "brand_voice"]:
        raise HTTPException(status_code=400, detail="Invalid table name")
    
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM {table} ORDER BY created_at DESC")
    rows = cursor.fetchall()
    return [dict(row) for row in rows]

@app.post("/api/{table}")
async def create_item(table: str, item: Item, db: sqlite3.Connection = Depends(get_db)):
    if table not in ["knowledge", "business", "brand_voice"]:
        raise HTTPException(status_code=400, detail="Invalid table name")
    
    cursor = db.cursor()
    cursor.execute(f"INSERT INTO {table} (title, content) VALUES (?, ?)", (item.title, item.content))
    db.commit()
    return {"status": "success", "id": cursor.lastrowid}

@app.put("/api/{table}/{item_id}")
async def update_item(table: str, item_id: int, item: Item, db: sqlite3.Connection = Depends(get_db)):
    if table not in ["knowledge", "business", "brand_voice"]:
        raise HTTPException(status_code=400, detail="Invalid table name")
    
    cursor = db.cursor()
    cursor.execute(f"UPDATE {table} SET title = ?, content = ? WHERE id = ?", (item.title, item.content, item_id))
    db.commit()
    return {"status": "success"}

@app.delete("/api/{table}/{item_id}")
async def delete_item(table: str, item_id: int, db: sqlite3.Connection = Depends(get_db)):
    if table not in ["knowledge", "business", "brand_voice"]:
        raise HTTPException(status_code=400, detail="Invalid table name")
    
    cursor = db.cursor()
    cursor.execute(f"DELETE FROM {table} WHERE id = ?", (item_id,))
    db.commit()
    return {"status": "success"}

# Serve static files
if not os.path.exists(STATIC_PATH):
    os.makedirs(STATIC_PATH)

app.mount("/static", StaticFiles(directory=STATIC_PATH), name="static")

@app.get("/")
async def read_index():
    return FileResponse(os.path.join(STATIC_PATH, "index.html"))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
