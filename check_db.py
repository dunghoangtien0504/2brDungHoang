import sqlite3

def check_db():
    db_path = 'brain.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print("--- Table Schema: brand_voice ---")
    cursor.execute("PRAGMA table_info(brand_voice)")
    for col in cursor.fetchall():
        print(col)
        
    print("\n--- Current Data in brand_voice ---")
    cursor.execute("SELECT id, title FROM brand_voice")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        
    conn.close()

if __name__ == "__main__":
    check_db()
