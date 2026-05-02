import sqlite3

def populate_articles():
    conn = sqlite3.connect('brain.db')
    cursor = conn.cursor()
    
    # Dữ liệu từ các file đã tạo
    day1_content = {
        'Sáng': 'MỘT BUỔI SÁNG CHỦ NHẬT VÀ MÀN HÌNH TRẮNG BÓC\n\nSáng chủ nhật, mình ngồi đó, bên ly cafe đá đã tan gần hết...',
        'Trưa': 'TẠI SAO BẠN VIẾT MÃI KHÔNG XONG 1 BÀI ĐĂNG?\n\nCâu trả lời thường không nằm ở kỹ năng viết, mà nằm ở "Hệ thống vận hành content"...',
        'Tối': 'Đừng cố viết bài bằng "cảm hứng" nữa các bạn ơi... Thiệt tình đó!\n\nCảm hứng giống như người yêu cũ vậy á...'
    }
    
    day2_content = {
        'Sáng': 'TÀI NGUYÊN CÓ HẠN VÀ NHỮNG KHOẢNG TRỐNG TRONG ĐẦU\n\nNhư thường lệ, khi đi gym sáng sớm, mình hay có thói quen quan sát nhịp thở...',
        'Trưa': 'Có bao giờ bạn thấy người ta đăng bài ầm ầm, bán được hàng, còn mình thì cứ im lặng mãi...',
        'Tối': 'THỬ VIẾT MỘT BÀI ĐĂNG TRONG 5 PHÚT CÙNG 2BRAIN\n\nNhiều bạn hỏi mình: "Viết bài xây kênh tốn thời gian quá, làm sao mà duy trì đều đặn được?"'
    }
    
    for session, content in day1_content.items():
        cursor.execute("INSERT OR REPLACE INTO articles (day, session, draft_a) VALUES (1, ?, ?)", (session, content))
        
    for session, content in day2_content.items():
        cursor.execute("INSERT OR REPLACE INTO articles (day, session, draft_a) VALUES (2, ?, ?)", (session, content))
        
    conn.commit()
    conn.close()
    print("Pre-populated articles for Day 1 and Day 2.")

if __name__ == "__main__":
    populate_articles()
