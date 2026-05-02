import sqlite3

def fix_database():
    conn = sqlite3.connect('brain.db')
    cursor = conn.cursor()
    
    # 1. Đảm bảo các bảng cơ bản tồn tại
    tables = {
        "knowledge": "id INTEGER PRIMARY KEY, title TEXT, content TEXT, created_at DATETIME DEFAULT CURRENT_TIMESTAMP",
        "business": "id INTEGER PRIMARY KEY, title TEXT, content TEXT, created_at DATETIME DEFAULT CURRENT_TIMESTAMP",
        "brand_voice": "id INTEGER PRIMARY KEY, title TEXT, content TEXT, created_at DATETIME DEFAULT CURRENT_TIMESTAMP"
    }
    
    for table, schema in tables.items():
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table} ({schema})")
    
    # 2. Xử lý bảng brain_scores (quan trọng nhất)
    cursor.execute("DROP TABLE IF EXISTS brain_scores")
    cursor.execute("""
        CREATE TABLE brain_scores (
            day INTEGER,
            session TEXT,
            post_time TEXT,
            similarity_score INTEGER,
            viewer_feedback TEXT,
            brand_voice_addition TEXT,
            short_comment TEXT,
            PRIMARY KEY (day, session)
        )
    """)
    
    sessions = ['Sáng', 'Trưa', 'Tối']
    times = {'Sáng': '07:30', 'Trưa': '11:30', 'Tối': '20:00'}
    
    for day in range(1, 8):
        for session in sessions:
            if day == 1 and session == 'Sáng':
                cursor.execute("""
                    INSERT INTO brain_scores (day, session, post_time, similarity_score, viewer_feedback, brand_voice_addition, short_comment)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (day, session, times[session], 9, '[Chờ bạn đăng bài]', 'Media Bank, Content OS', 'Bài viết gãy gọn, bám sát tone tâm sự.'))
            else:
                cursor.execute("INSERT INTO brain_scores (day, session, post_time) VALUES (?, ?, ?)", (day, session, times[session]))
    
    conn.commit()
    conn.close()
    print("Database fixed and initialized successfully!")

if __name__ == "__main__":
    fix_database()
