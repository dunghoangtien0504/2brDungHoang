import sqlite3

def update_db():
    conn = sqlite3.connect('brain.db')
    cursor = conn.cursor()
    try:
        cursor.execute("""
            UPDATE brain_scores 
            SET similarity_score = 9, 
                viewer_feedback = '[Chờ bạn đăng bài]', 
                brand_voice_addition = 'Media Bank, Content OS', 
                short_comment = 'Bài viết gãy gọn, bám sát tone tâm sự.'
            WHERE day = 1
        """)
        conn.commit()
        print("Updated brain.db for Day 1")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    update_db()
