import sqlite3
import difflib

def upgrade_system_v3():
    conn = sqlite3.connect('brain.db')
    cursor = conn.cursor()
    
    # 1. Tạo bảng articles
    cursor.execute("DROP TABLE IF EXISTS articles")
    cursor.execute("""
        CREATE TABLE articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            day INTEGER,
            session TEXT,
            draft_a TEXT,
            final_b TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Thêm dữ liệu mẫu từ Ngày 1 và Ngày 2 (Draft A)
    # Lưu ý: Ở đây mình chỉ thêm Draft A, bạn sẽ là người điền Final B sau.
    # Mình lấy nội dung từ các file day1.txt và day2.txt đã tạo.
    
    print("Database upgraded: Added articles table.")
    conn.commit()
    conn.close()

def calculate_similarity(text1, text2):
    """Tính toán độ tương đồng giữa 2 văn bản (1-10)"""
    if not text1 or not text2: return 0
    ratio = difflib.SequenceMatcher(None, text1, text2).ratio()
    return round(ratio * 10)

def analyze_differences(draft, final):
    """Phân tích sự khác biệt giữa bản Draft và bản Final"""
    if not draft or not final: return "Chưa có dữ liệu so sánh."
    
    d = difflib.Differ()
    diff = list(d.compare(draft.split(), final.split()))
    
    added = [word[2:] for word in diff if word.startswith('+ ')]
    removed = [word[2:] for word in diff if word.startswith('- ')]
    
    analysis = []
    if added:
        analysis.append(f"Thêm từ mới: {', '.join(added[:5])}...")
    if removed:
        analysis.append(f"Loại bỏ từ thừa: {', '.join(removed[:5])}...")
    
    # Kiểm tra cấu trúc xuống dòng (đếm số dòng)
    if draft.count('\n') != final.count('\n'):
        analysis.append("Thay đổi cấu trúc ngắt dòng.")
        
    return " | ".join(analysis) if analysis else "Văn phong gần như trùng khớp hoàn toàn."

if __name__ == "__main__":
    upgrade_system_v3()
