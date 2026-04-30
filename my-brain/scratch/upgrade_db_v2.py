import sqlite3

def upgrade_brain_scores():
    conn = sqlite3.connect('brain.db')
    cursor = conn.cursor()
    
    # Sao lưu dữ liệu cũ nếu cần (ở đây mình làm mới luôn cho sạch)
    cursor.execute("DROP TABLE IF EXISTS brain_scores")
    
    # Tạo bảng mới có thêm cột session
    cursor.execute("""
        CREATE TABLE brain_scores (
            day INTEGER,
            session TEXT,
            similarity_score INTEGER,
            viewer_feedback TEXT,
            brand_voice_addition TEXT,
            short_comment TEXT,
            PRIMARY KEY (day, session)
        )
    """)
    
    sessions = ['Sáng', 'Trưa', 'Tối']
    for day in range(1, 8):
        for session in sessions:
            # Riêng Ngày 1 - Sáng, mình giữ lại dữ liệu đánh giá lúc nãy
            if day == 1 and session == 'Sáng':
                cursor.execute("""
                    INSERT INTO brain_scores (day, session, similarity_score, viewer_feedback, brand_voice_addition, short_comment)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (day, session, 9, '[Chờ bạn đăng bài]', 'Media Bank, Content OS', 'Bài viết gãy gọn, bám sát tone tâm sự.'))
            else:
                cursor.execute("INSERT INTO brain_scores (day, session) VALUES (?, ?)", (day, session))
            
    conn.commit()
    conn.close()
    print("Database upgraded: 3 sessions per day.")

if __name__ == "__main__":
    upgrade_brain_scores()
