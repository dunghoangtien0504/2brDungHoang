import sqlite3
import datetime

def setup_database():
    # Kết nối đến database (sẽ tự động tạo nếu chưa có)
    conn = sqlite3.connect('brain.db')
    cursor = conn.cursor()

    # Xóa các bảng cũ nếu có để khởi tạo mới hoàn toàn (tùy chọn, ở đây ta cứ tạo nếu chưa có)
    # cursor.execute("DROP TABLE IF EXISTS knowledge")
    # cursor.execute("DROP TABLE IF EXISTS business")
    # cursor.execute("DROP TABLE IF EXISTS brand_voice")

    # Tạo bảng knowledge
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS knowledge (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Tạo bảng business
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS business (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Tạo bảng brand_voice
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS brand_voice (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Thêm dữ liệu mẫu
    sample_data = {
        'knowledge': [
            ('Cách học AI hiệu quả', 'Tập trung vào thực hành qua project thực tế thay vì chỉ đọc lý thuyết.'),
            ('Nguyên lý 80/20', '80% kết quả đến từ 20% nỗ lực quan trọng nhất.')
        ],
        'business': [
            ('Sản phẩm A', 'Khóa học hướng dẫn xây dựng AI Agent cá nhân.'),
            ('Khách hàng tiềm năng', 'Các chủ doanh nghiệp vừa và nhỏ muốn tối ưu quy trình bằng AI.')
        ],
        'brand_voice': [
            ('Giọng văn chuyên gia', 'Sử dụng ngôn từ súc tích, chuyên nghiệp nhưng dễ hiểu.'),
            ('Tone màu thương hiệu', 'Sử dụng tone màu tối (Dark Mode) với điểm nhấn là màu cam năng động.')
        ]
    }

    for table, rows in sample_data.items():
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        if cursor.fetchone()[0] == 0:
            cursor.executemany(f"INSERT INTO {table} (title, content) VALUES (?, ?)", rows)
            print(f"Added sample data to table {table}.")
        else:
            print(f"Table {table} already has data, skipping sample insertion.")

    conn.commit()
    conn.close()
    print("Database brain.db setup completed successfully!")

if __name__ == "__main__":
    setup_database()
