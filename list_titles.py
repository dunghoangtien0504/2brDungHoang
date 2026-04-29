import sqlite3

def list_titles():
    db_path = 'brain.db'
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT title FROM brand_voice")
    rows = cursor.fetchall()
    for row in rows:
        # Encode to avoid console issues if needed, but here we just want to see the count and basic info
        print(f"Title: {row[0][:50]}...")
    conn.close()

if __name__ == "__main__":
    list_titles()
