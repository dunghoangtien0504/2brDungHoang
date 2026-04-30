import sqlite3
import sys

# Set stdout to use utf-8
sys.stdout.reconfigure(encoding='utf-8')

def get_brand_voice():
    conn = sqlite3.connect('brain.db')
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT content FROM brand_voice")
        rows = cursor.fetchall()
        for row in rows:
            print(row[0])
            print("-" * 20)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    get_brand_voice()
