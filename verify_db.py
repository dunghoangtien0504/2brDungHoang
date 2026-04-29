import sqlite3
import os

def verify_db():
    db_path = 'brain.db'
    if not os.path.exists(db_path):
        print(f"File {db_path} not found.")
        return
        
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Check tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print(f"Tables: {tables}")
    
    # Check brand_voice count
    try:
        cursor.execute("SELECT COUNT(*) FROM brand_voice")
        count = cursor.fetchone()[0]
        print(f"Row count in brand_voice: {count}")
        
        if count > 0:
            cursor.execute("SELECT id, title FROM brand_voice LIMIT 5")
            rows = cursor.fetchall()
            print("First 5 rows:")
            for row in rows:
                print(row)
    except Exception as e:
        print(f"Error checking brand_voice: {e}")
        
    conn.close()

if __name__ == "__main__":
    verify_db()
