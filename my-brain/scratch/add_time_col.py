import sqlite3

def add_post_time_column():
    conn = sqlite3.connect('brain.db')
    cursor = conn.cursor()
    
    try:
        # Thêm cột post_time vào bảng
        cursor.execute("ALTER TABLE brain_scores ADD COLUMN post_time TEXT")
        
        # Cập nhật giờ mặc định theo plan cho Ngày 1
        cursor.execute("UPDATE brain_scores SET post_time = '07:30' WHERE day = 1 AND session = 'Sáng'")
        cursor.execute("UPDATE brain_scores SET post_time = '11:30' WHERE day = 1 AND session = 'Trưa'")
        cursor.execute("UPDATE brain_scores SET post_time = '20:00' WHERE day = 1 AND session = 'Tối'")
        
        conn.commit()
        print("Database updated: Added post_time column.")
    except Exception as e:
        print(f"Lưu ý: {e}") # Có thể cột đã tồn tại
    finally:
        conn.close()

if __name__ == "__main__":
    add_post_time_column()
