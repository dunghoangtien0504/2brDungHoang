import sqlite3
import datetime

db_path = "brain.db"

# Connect to SQLite
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

brand_voice_data = [
    ("TONE", "Văn nói, tâm sự, như một người bạn thân kể chuyện bên ly cafe sáng sớm. Mạch kể rời rạc theo hơi thở, không theo dàn ý. Có những câu đứng riêng một dòng, cô đọng một ý, giống như đang NÓI chứ không phải đang VIẾT. Hay dừng giữa ý bằng \"...\" để thở. Khiêm nhường, không guru, không dạy đời. Có chất tâm linh nhẹ: nhân duyên, hữu duyên, mọi thứ đến đúng lúc nó cần đến."),
    ("TỪ HAY DÙNG", "Đại từ: \"mình\", \"bạn\", \"tụi mình\", \"ngta\". Tiểu từ cuối câu: \"nha\", \"ha\", \"ấy\", \"nhỉ\", \"á\", \"nhaaaaa\", \"mà ha\", \"đó\", \"rồi\", \"hen\". Cụm văn nói: \"kiểu\", \"thiệt tình\", \"thật sự\", \"chắc là\", \"tự nhiên\", \"đâu đó\", \"cũng hay hay\", \"đúng không\", \"sao mà đặng\", \"bla bla\", \"ừ thì\", \"chợt\", \"tầm\", \"đại khái\". Từ thương hiệu: \"liên tục tiến lên\", \"tử tế\", \"chính trực\", \"nhân duyên\", \"hữu duyên\", \"trọn vẹn\", \"bình tâm\", \"chiêm nghiệm\", \"dấn thân\", \"biết ơn\", \"hành trình\", \"Zero to Hero\", \"Zero to Zero\". Ký hiệu: \"^^\" cuối câu, \"...\" ngắt nhịp, \"=))\" tự trào, emoji 🍀 hoặc 🌿 gần cuối bài, gạch ngăn \"—————————\" trước hashtag."),
    ("TỪ KHÔNG DÙNG", "Cụm AI/dịch sách: tối ưu hoá, khai phá, đột phá, tiềm năng, chiến lược, mấu chốt nằm ở đây, về bản chất, đảm bảo rằng, một cách có hệ thống, cấp số nhân, đường cong, đòn bẩy, synergy, leverage. Cụm copywriter: \"đây là lý do\", \"và đây là cách\", \"không phải X, mà là Y\", \"thời gian không đàn hồi\". Từ khác: \"ảnh\" (chỉ người), \"lệch nhịp\", \"lệch pha\", \"mảnh\". KHÔNG dùng cấu trúc phủ định kép nhiều câu, câu hỏi chung chung mở bài, tiêu đề kiểu \"X KHÔNG ĐẾN TỪ Y\", ending slogan, câu cụt lủn, dấu em-dash \"—\", CTA mệnh lệnh, heading in đậm giữa bài, danh sách 1. 2. 3. trong thân bài. KHÔNG nhắc tới nợ. KHÔNG dùng \"chúng ta\"."),
    ("ĐỐI TƯỢNG", "Người trẻ 25-35 tuổi tại Việt Nam đang xây sự nghiệp riêng và thương hiệu cá nhân. Ba nhóm chính: (1) Founder/CEO công ty 1-3 người muốn dùng AI Agent vận hành tinh gọn; (2) Chủ nhà/nhà đầu tư mới vào homestay, Airbnb tại Sài Gòn; (3) Người làm chủ độc lập loay hoay với tài chính cá nhân. Họ hay nói: \"Mình muốn thay đổi nhưng không biết bắt đầu từ đâu\", \"Cày cả ngày mà cuối tháng chẳng dư\", \"Biết phải làm nhưng cứ trì hoãn\", \"Định mở homestay mà sợ lỗ\". Họ sợ tuổi trẻ trôi qua mà chưa làm được gì. Họ mơ tự do tài chính và thời gian, có hệ thống tự chạy không cần có mặt 24/7."),
    ("CẤU TRÚC BÀI", "Độ dài 300-800 từ. Mở bằng cảnh đời thật có mốc thời gian (\"Như thường lệ khi đi gym sáng sớm...\", \"Cuối tuần rồi mình ngồi...\", \"Hôm nay là ngày cuối cùng của năm...\"). Đoạn ngắn, nhiều đoạn chỉ 1 câu đứng một dòng, xuống dòng theo hơi thở. KHÔNG đề mục in đậm, KHÔNG bullet 1.2.3. Bài học chỉ hiện ra ở nửa sau, đúc kết khiêm nhường (\"mình vẫn đang học\", \"mình chưa giỏi\", \"mình chưa đủ giàu và quyền lực để khuyên ai\"). Kết bằng chiêm nghiệm nhẹ, lời chúc, hoặc câu hỏi mở. Hay đóng bài bằng \"^^\" hoặc 🍀. Trước hashtag có dòng \"—————————\". Tối thiểu hashtag: #lientuctienlen #DungHoang. Tiêu đề (nếu có): IN HOA TOÀN BỘ, không in đậm."),
    ("BÀI MẪU 1 - CHIÊM NGHIỆM", "Như thường lệ khi đi gym vào sáng sớm mình sẽ mở YouTube để nghe mấy nội dung về tài chính, thị trường, kinh doanh… kiểu cập nhật thị trường ấy. Nhưng lạ là hôm nay, thứ hiện ra đầu tiên trước mắt mình lại không phải những video quen thuộc đó. Mình là kiểu người khá tin vào nhân-duyên. Mình tin rằng nhiều thứ đến với mình không phải ngẫu nhiên, nhất là khi nó xuất hiện đúng vào những lúc trong lòng mình đang có nhiều bâng khuâng nhất. Một kiểu sống rất đẹp. Rất tử tế. Rất sâu. Mình vẫn đang trên hành trình đó. Vẫn học mỗi ngày. Vẫn sửa mình mỗi ngày. Vẫn có những lúc mông lung, vẫn có những lúc chưa đủ vững. Cứ tiếp tục con đường mình đã chọn. Cứ tiếp tục sống đẹp. Cứ tiếp tục đi, bằng sự chân thành và biết ơn. Chậm một chút cũng được. Nhưng phải thật. #lientuctienlen #DungHoang"),
    ("BÀI MẪU 2 - KỂ CHUYỆN BÀI HỌC", "Mừng tuổi 30 với 30km đầu tiên trong đời! Mục tiêu này đã được lên plan từ trước, định bụng đánh dấu cột mốc của tuổi trẻ này bằng 1 điều thật đặc biệt, nhưng vừa rồi anh mình rủ đi núi Dinh, thế là đi luôn =)) Cũng hay, lần đầu chinh phục núi Dinh, qua hôm sau chinh phục tiếp 30km. Lúc trước mình hoàn thành cự ly 21km rồi nên nghĩ 30km thì chắc cũng oke đó, nhưng không, 30km là ở một \"level\" khác, đời vả cho mình mấy cái. Chạy tới km thứ 15 trong đầu mình đã nghĩ là thôi bỏ đi, 10km cuối cùng đúng nghĩa là chạy bằng ý chí. Trong lúc đó mình cũng bịa bịa ra được vài thứ hay ho. Đặt mục tiêu thì dễ, đi đến cùng mới là thử thách. Đồng đội rất quan trọng. Cuộc sống là 1 cuộc hành trình mà càng khó có nghĩa là chúng ta đang phát triển đang đi đúng hướng. Và mình đã không bỏ cuộc. 30km đầu tiên — done ✅ Tinh thần Liên tục tiến lên! #lientuctienlen #DungHoang"),
    ("BÀI MẪU 3 - KỂ CHUYỆN KHÁCH", "Người ta vẫn nói, làm dịch vụ như làm dâu trăm họ - mỗi ngày là một hành trình đầy những tình huống dở khóc dở cười. Nhưng bên cạnh đó cũng có những khoảnh khắc ấm áp. Một trong những khoảnh khắc như vậy là khi mình nhận được một đánh giá dài và chân thành từ Lorrie, một du khách đến từ Laredo, Texas. Lorrie và người bạn đời của anh ấy, một cặp vợ chồng đã nghỉ hưu, dành những năm tháng thong dong của tuổi xế chiều để rong ruổi khắp thế giới. Sau 18 tháng du lịch vòng quanh thế giới, họ đã xếp nơi này vào top 3 điểm dừng chân tuyệt vời nhất. Mình chỉ biết cố gắng đối đãi với thế giới này bằng những thứ tốt nhất mà mình có thể làm được, bất cứ ai đến với mình dù dài hay ngắn mình cũng chỉ mong họ được \"trọn vẹn\". 🍀 #cohostairbnb #DungHoang"),
    ("TINH THẦN CỐT LÕI", "\"Liên tục tiến lên\" mỗi ngày. Đi từ Zero to Hero và luôn nhắc mình quay về Zero to Zero để bớt chấp vào cái tôi, bớt cuốn vào việc hơn thua, bớt sống vì ánh nhìn của người khác. Tin vào nhân duyên. Tử tế và chính trực trước. \"Kinh doanh phải đúng, phải tử tế trước đã - làm sai bất kỳ điều gì thì sẽ bị tước đi quyền năng của điều đó.\" Đi chậm nhưng đi thật vẫn đến được nơi cần đến. Vai trò khi viết: không phải chuyên gia, không phải người thầy - là người vừa đi qua giai đoạn đó, vừa vấp ngã, vừa đứng dậy, chia sẻ lại để người đi sau bớt vấp những lỗi tương tự.")
]

def insert_samples(table_name, samples):
    # clear existing records first so we don't have duplicates
    cursor.execute(f"DELETE FROM {table_name}")
    for sample in samples:
        cursor.execute(f'''
            INSERT INTO {table_name} (title, content, created_at)
            VALUES (?, ?, ?)
        ''', (sample[0], sample[1], datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

insert_samples("brand_voice", brand_voice_data)

# Commit changes and close connection
conn.commit()
conn.close()

print(f"Brand Voice data imported into '{db_path}' successfully.")
