import sqlite3

def check_first_item():
    conn = sqlite3.connect('brain.db')
    cursor = conn.cursor()
    cursor.execute("SELECT title, content FROM brand_voice LIMIT 1")
    row = cursor.fetchone()
    if row:
        print(f"TITLE: {row[0]}")
        print(f"CONTENT PREVIEW: {row[1][:100]}...")
    else:
        print("Table is empty!")
    conn.close()

if __name__ == "__main__":
    check_first_item()
