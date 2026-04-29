import sqlite3

def check_all_counts():
    conn = sqlite3.connect('brain.db')
    cursor = conn.cursor()
    for table in ['knowledge', 'business', 'brand_voice']:
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        count = cursor.fetchone()[0]
        print(f"Table {table}: {count} items")
    conn.close()

if __name__ == "__main__":
    check_all_counts()
