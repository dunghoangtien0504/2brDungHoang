import sqlite3
import os

def dump_db():
    db_path = 'brain.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, length(content) FROM brand_voice")
    rows = cursor.fetchall()
    
    with open('db_dump.txt', 'w', encoding='utf-8') as f:
        f.write(f"Total rows: {len(rows)}\n")
        for row in rows:
            f.write(f"ID: {row[0]}, Title: {row[1]}, Content Length: {row[2]}\n")
            
    conn.close()

if __name__ == "__main__":
    dump_db()
