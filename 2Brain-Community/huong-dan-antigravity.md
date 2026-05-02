# HƯỚNG DẪN TRIỂN KHAI 2BRAIN COMMUNITY TRÊN ANTIGRAVITY
*Bao gồm: Offer đã được cải tiến theo Hormozi + Landing Page + Thank You Page + Form Email*

---

## PHẦN 0: TÓM TẮT THAY ĐỔI OFFER (HORMOZI)

Trước khi triển khai kỹ thuật, đây là những cải tiến đã được áp dụng vào nội dung dựa trên hệ thống Hormozi $100M:

### Value Equation — 4 biến đã tối ưu:
| Biến | Trước | Sau |
|------|-------|-----|
| Dream Outcome | "Viết bài nhanh hơn" | "Biến kinh nghiệm thành nội dung + dòng tiền — chỉ 15 phút/ngày" |
| Perceived Likelihood | Không có proof | Nhóm thực chiến + template ready-to-use ngay ngày đầu |
| Time Delay | Không rõ | "Dùng được trong ngày đầu tiên", chiến thắng cảm xúc sớm |
| Effort & Sacrifice | "Phức tạp?" | "Checklist 7 ngày từ con số 0, kể cả không biết Notion" |

### Grand Slam Offer Bundle (Value Stack):
1. Template Notion 2Brain → 497,000đ
2. Bộ 50+ Prompt AI viết bài → 297,000đ
3. Framework "3 Khung Bài Viết Chuyển Đổi" → 197,000đ
4. Cộng đồng thực chiến + Hỏi đáp → 997,000đ/tháng
5. Checklist 7 Ngày Setup 2Brain → 97,000đ
**Tổng giá trị: ~2,085,000đ → MIỄN PHÍ**

### 5 Đòn bẩy Tâm lý đã thêm:
- **Scarcity (Khan hiếm):** "Chỉ nhận 500 thành viên đầu tiên — còn 144 chỗ" + thanh progress 72%
- **Urgency (Cấp bách):** "Vào trong 48h đầu nhận thêm bonus Kịch Bản Video Reels 30 giây"
- **Naming (MAGIC):** Cộng Đồng 2Brain — Thử Thách 14 Ngày Viết Bài 15 Phút Cho Chuyên Gia Việt Bận Rộn
- **Guarantee (Bảo đảm):** "Miễn phí hoàn toàn · Không ràng buộc · Rời nhóm bất cứ lúc nào"
- **Bonus:** Value stack rõ ràng với giá trị gán cho từng phần

---

## PHẦN 1: THIẾT LẬP CẤU TRÚC DỰ ÁN TRÊN ANTIGRAVITY

### Bước 1.1 — Tạo 2 trang mới

Truy cập Antigravity dashboard → Projects → Tạo project mới tên "2Brain Community":

| Trang | Slug/URL | Mục đích |
|-------|----------|----------|
| Landing Page | `/` hoặc `/2brain` | Trang chính thu lead |
| Thank You Page | `/cam-on` | Redirect sau khi submit form |

### Bước 1.2 — Cài đặt Font

Trong mỗi trang, vào **Page Settings → Custom Code → Head**:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;600;700&family=Nunito:wght@400;500;600;700&display=swap" rel="stylesheet">
```

---

## PHẦN 2: XÂY DỰNG LANDING PAGE

### Cấu trúc section theo thứ tự từ trên xuống:

---

### SECTION A — Top Banner (Scarcity)

**Block type:** Custom HTML / Announcement Bar

Thêm đoạn HTML sau vào đầu trang (hoặc dùng Announcement Bar widget):

```html
<div style="background:linear-gradient(90deg,#F97316,#dc2626);text-align:center;padding:10px 20px;font-family:'Oswald',sans-serif;font-size:14px;letter-spacing:1px;font-weight:600;color:#fff;">
  ⚠️ <span style="opacity:0.85">Nhóm chỉ nhận</span> <strong>500 thành viên đầu tiên</strong> <span style="opacity:0.85">— Còn</span> <strong>144 chỗ trống</strong>
</div>
```

**Cài đặt:** Background = tự code như trên (không dùng màu mặc định của Antigravity cho banner này)

---

### SECTION B — Hero Section

**Block type:** Hero / Banner block

Thiết lập:
- **Nền (Background):** Màu #0C0C0C (rất tối) + thêm radial gradient nhẹ màu cam nếu có option
- **Alignment:** Căn giữa

Nội dung cần nhập:

**Pre-headline (Badge/Tag nhỏ):**
```
Dành riêng cho ai muốn xây thương hiệu cá nhân nhưng "BÍ" ý tưởng và THIẾU thời gian!
```
Style: Chữ nhỏ, nền đỏ mờ, viền đỏ, chữ hồng nhạt, bo góc pill

**Headline chính:**
```
BÍ QUYẾT ỨNG DỤNG "2BRAIN" TRÊN NOTION:
Rút Ngắn Thời Gian Viết Bài Từ 3–4 Giờ Xuống Chỉ Còn 10–15 Phút/Ngày!
```
Style: Font Oswald, cỡ chữ lớn nhất (48-58px desktop, 32px mobile), "2BRAIN" và "10–15 Phút/Ngày!" màu cam #F97316

**Sub-headline:**
```
Hệ thống hóa kiến thức, biến kinh nghiệm cá nhân thành nội dung bán hàng sắc bén.
Không cần là copywriter xuất chúng — chỉ cần đúng hệ thống.
```
Style: Font Nunito, 18px, màu trắng mờ 60%, "chỉ cần đúng hệ thống" in đậm màu vàng amber

**Nút CTA 1:**
```
👉 THAM GIA CỘNG ĐỒNG TELEGRAM MIỄN PHÍ NGAY 👈
```
- Link: https://t.me/+ju9HuPOviThhMmU1
- Style: Nền cam #F97316, chữ trắng, font Oswald, padding rộng, hiệu ứng glow/pulse
- Sub-note bên dưới nút: "✅ Miễn phí 100% · Không cần thẻ tín dụng · Vào ngay, hỏi ngay"

**Scarcity Progress Bar (Custom HTML block dưới Hero):**

```html
<div style="background:#1E1E1E;border:1px solid rgba(251,191,36,0.2);border-radius:12px;padding:16px 24px;margin:24px auto;max-width:600px;display:flex;align-items:center;gap:16px;flex-wrap:wrap;justify-content:center;">
  <span style="background:rgba(239,68,68,0.15);border:1px solid rgba(239,68,68,0.3);color:#FCA5A5;font-size:12px;font-weight:700;letter-spacing:1px;text-transform:uppercase;padding:4px 12px;border-radius:100px;">🔥 Gần đầy</span>
  <div style="width:200px;height:8px;background:rgba(255,255,255,0.1);border-radius:100px;overflow:hidden;">
    <div style="height:100%;width:72%;background:linear-gradient(90deg,#F97316,#dc2626);border-radius:100px;"></div>
  </div>
  <p style="font-size:14px;color:rgba(245,245,240,0.6);"><strong style="color:#FBBF24;">356/500</strong> chỗ đã được lấp đầy</p>
</div>
```

---

### SECTION C — Pain Points

**Block type:** Feature List / Icon List

- **Nền:** #141414 (tối hơn hero một chút)
- **Section Tag:** "Bạn có đang gặp vấn đề này?" (màu cam, nền cam mờ)
- **Tiêu đề:** "Bạn có đang bế tắc với những điều này mỗi ngày?"

4 pain points, mỗi cái là 1 item trong list:
- Icon: ✕ đỏ (hoặc dùng X icon đỏ của Antigravity)
- Border trái màu đỏ
- Nền card tối #1E1E1E

Pain 1: Ngồi nhìn màn hình 3–4 tiếng đồng hồ mà không rặn ra được một bài viết chất lượng?
Pain 2: Có rất nhiều kinh nghiệm thực chiến, chuyên môn giỏi nhưng không biết cách "đóng gói" thành nội dung viral?
Pain 3: Viết bài bán hàng khô khan, ít tương tác và không chuyển đổi thành doanh thu?
Pain 4: Làm việc tùy hứng, thiếu hệ thống lưu trữ và quản trị tri thức cá nhân bài bản?

---

### SECTION D — Solution

**Block type:** 4-column Feature Grid hoặc Cards

- **Section Tag:** "Giải pháp" (màu cam)
- **Tiêu đề:** "Đừng lo! Hệ thống 2Brain chính là 'vũ khí' bạn cần."
- **Sub:** "2Brain không chỉ là công cụ ghi chép. Đây là hệ thống quản lý tri thức và tự động hóa nội dung..."

4 cards:
| Số | Tiêu đề | Mô tả |
|----|---------|-------|
| 01 | Thu thập có tổ chức | Lưu mọi ý tưởng lóe lên vào đúng chỗ — không bao giờ mất đi một insight quý giá |
| 02 | Phân loại tự động | Hệ thống tự liên kết và gợi ý mối quan hệ giữa các ý tưởng chuyên môn |
| 03 | Lắp ghép siêu tốc | Framework có sẵn giúp "lắp ráp" thành bài viết chỉ trong 10–15 phút |
| 04 | Đăng đều đặn mãi mãi | Không còn cảnh "bí bài" — thương hiệu cá nhân luôn sáng đèn |

Style card: Nền tối #1E1E1E, viền mờ, số lớn màu cam nhạt, hover border cam

---

### SECTION E — Value Stack (QUAN TRỌNG — Hormozi Bundle)

**Nền:** #141414

**Block type:** Custom HTML (copy nguyên đoạn HTML từ file landing-page-2brain.html, phần `<div class="value-stack">`)

Hoặc nếu Antigravity có Pricing/Feature List block, tạo thủ công:

- **Header của table:** "📦 Gói Cộng Đồng 2Brain Community" + badge "Trị giá thực ~2,085,000đ"
- **5 items:** (xem danh sách Value Stack ở Phần 0 bên trên)
- **Footer:** 
  - Bên trái: "Tổng giá trị thực tế:" + gạch ngang "2,085,000đ" + chữ to "MIỄN PHÍ" màu cam
  - Bên phải: Urgency box vàng "⚡ Bonus đặc biệt 48h: Vào nhóm trong 48 giờ tới, nhận thêm bộ Kịch Bản Video Reels 30 Giây!"

**Nút CTA 2 (dưới value stack):**
```
👉 VÀO NHÓM ĐỂ LẤY TEMPLATE & HỌC HỎI NGAY 👈
```
Link: https://t.me/+ju9HuPOviThhMmU1

---

### SECTION F — Đối tượng phù hợp (3 cards)

**Block type:** 3-column Cards

- **Section Tag:** "Đây có phải dành cho bạn?"
- **Tiêu đề:** "Cộng đồng này dành cho ai?"

| Icon | Tiêu đề | Mô tả |
|------|---------|-------|
| 🏢 | Chủ doanh nghiệp & Founder | Muốn xây dựng thương hiệu cá nhân để hút nhân tài, đối tác và khách hàng |
| 💼 | Chuyên gia & Freelancer | Muốn bán dịch vụ, khóa học từ chính kinh nghiệm thực chiến |
| ⚙️ | Người làm việc thông minh | Muốn ứng dụng hệ thống và công nghệ — Work Smart, Not Hard |

---

### SECTION G — FAQ (Accordion)

**Block type:** FAQ / Accordion block

Nếu Antigravity có FAQ block thì dùng trực tiếp. Nếu không, dùng Custom HTML từ file.

4 câu hỏi:
1. Tham gia nhóm có mất phí không? → "Hoàn toàn MIỄN PHÍ..."
2. Tôi không rành công nghệ, không biết dùng Notion — có được không? → "Hoàn toàn được..."
3. Tôi bận lắm, mỗi ngày chỉ có khoảng 15–20 phút — có phù hợp không? → "15–20 phút chính xác là những gì..."
4. Sau khi vào nhóm tôi cần làm gì ngay lập tức? → "Đọc ghim hướng dẫn, tải Template..."

---

### SECTION H — Final CTA

**Block type:** CTA Section

- **Nền:** Tối + radial gradient cam nhẹ từ dưới lên
- **Tiêu đề:** "Đừng để kho báu kinh nghiệm của bạn bị lãng phí."
- **Sub:** "Biến kinh nghiệm thực chiến thành nội dung, thương hiệu và dòng tiền — ngay hôm nay."
- **Nút CTA 3 (to nhất trang):**
```
👉 CLICK ĐỂ THAM GIA GROUP TELEGRAM NGAY 👈
```
Link: https://t.me/+ju9HuPOviThhMmU1
- **Guarantee note bên dưới:** "🔒 Miễn phí hoàn toàn · Không ràng buộc · Rời nhóm bất cứ lúc nào"

---

## PHẦN 3: XÂY DỰNG THANK YOU PAGE

### Lưu ý quan trọng về Thank You Page

Trang này có **MỘT MỤC TIÊU DUY NHẤT**: đưa người dùng vào Telegram. Không thêm bất cứ thứ gì làm phân tán sự chú ý.

### Cấu trúc từ trên xuống:

**Header:**
- Icon ✅ to, nền xanh lá nhạt
- H1: "Đăng ký thành công!"
- Sub (chữ đỏ): "Nhưng khoan đã, đăng ký xong chưa phải là xong. Còn 1 việc cuối cùng bạn cần làm ngay."

**Telegram CTA Box (quan trọng nhất):**

Dùng Custom HTML block, paste đoạn sau:

```html
<div style="background:linear-gradient(135deg,#1A3D5C 0%,#0D2840 100%);border:2px solid rgba(34,158,217,0.4);border-radius:16px;padding:36px 32px;text-align:center;margin:32px auto;max-width:560px;">
  <p style="font-family:'Oswald',sans-serif;font-size:22px;font-weight:700;color:#F5F5F0;margin-bottom:14px;">👉 VÀO NHÓM TELEGRAM NGAY BÂY GIỜ</p>
  <p style="font-size:14px;color:rgba(255,255,255,0.75);line-height:1.7;margin-bottom:28px;">Đây là kênh <strong style="color:#FBBF24;">DUY NHẤT</strong> mình gửi các Template Notion mẫu, bộ Prompt AI và hỗ trợ bạn trực tiếp cách setup hệ thống 2Brain.</p>
  <a href="https://t.me/+ju9HuPOviThhMmU1" target="_blank" style="display:inline-flex;align-items:center;gap:12px;background:#fff;color:#1A75A8;font-family:'Oswald',sans-serif;font-size:18px;font-weight:600;padding:16px 32px;border-radius:10px;text-decoration:none;">
    <span style="width:28px;height:28px;background:#229ED9;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:14px;color:#fff;flex-shrink:0;">✈</span>
    BẤM VÀO ĐÂY ĐỂ VÀO TELEGRAM
  </a>
  <div style="display:flex;align-items:center;gap:8px;margin-top:18px;padding:10px 16px;background:rgba(251,191,36,0.08);border:1px solid rgba(251,191,36,0.2);border-radius:8px;font-size:12px;color:#FBBF24;text-align:left;">
    <span>⚠️</span>
    <span><strong>Quan trọng:</strong> Nhóm sẽ kiểm duyệt thành viên, hãy vào ngay để được duyệt sớm nhất.</span>
  </div>
</div>
```

**Checklist 4 bước (Timeline dọc):**

Tạo bằng Steps/Timeline block hoặc Custom HTML:

| Icon | Badge | Tiêu đề | Mô tả |
|------|-------|---------|-------|
| ✓ xanh | Hoàn tất | Bước 1: Giữ chỗ thành công | Tên & Email đã được lưu an toàn. |
| ✈ xanh dương | Làm ngay! | Bước 2: Vào nhóm Telegram | Bấm nút phía trên. Mọi tài liệu diễn ra ở đây. |
| ✉ mờ | Tiếp theo | Bước 3: Kiểm tra Email xác nhận | Kiểm tra tab Quảng cáo / Spam nếu không thấy. |
| 💻 mờ | Chuẩn bị | Bước 4: Tạo tài khoản Notion.so | Tạo sẵn miễn phí để copy hệ thống 2Brain. |

Style: Bước 2 có viền xanh dương nổi bật hơn 3 bước còn lại.

**Viral Box (Share link):**
```
💝 Gợi ý nhỏ — Mời thêm bạn bè cùng làm
"Xây dựng thương hiệu cá nhân có đồng đội sẽ đi nhanh hơn..."
[Box chứa link squeeze page + nút Sao chép]
```

---

## PHẦN 4: THIẾT LẬP FORM + EMAIL MARKETING

### Bước 4.1 — Chọn platform

Khuyến nghị theo độ ưu tiên:
1. **GetResponse** (hỗ trợ tiếng Việt, có automation tốt)
2. **MailerLite** (miễn phí đến 1000 sub, dễ dùng)
3. **Funnelaz** (nếu đã dùng)

### Bước 4.2 — Tạo Form trên hệ thống Email Marketing

1. Vào hệ thống Email Marketing → tạo **Form Inline** (2 field: Tên + Email)
2. Tại cài đặt form, tìm **"Redirect URL after signup"** → dán link Thank You Page
   - Ví dụ: `https://your-domain.com/cam-on`
3. Tạo Automation:
   - **Trigger:** Khi có người điền form này
   - **Action:** Gửi ngay email chào mừng (delay = 0 phút)

### Bước 4.3 — Nội dung Email Chào Mừng

```
Tiêu đề: Chào mừng bạn! Đây là bước tiếp theo để xây dựng 2Brain trên Notion 🧠

---

Chào [TÊN KHÁCH HÀNG],

Chúc mừng bạn đã đăng ký thành công!

Bạn vừa tiến một bước rất gần đến việc giải phóng bản thân khỏi áp lực phải ngồi rặn từng chữ mỗi ngày.

Hệ thống 2Brain sẽ giúp bạn tổ chức lại mọi kinh nghiệm thực chiến thành tài sản nội dung số — xây dựng thương hiệu cá nhân sắc bén và tiết kiệm hàng giờ đồng hồ.

▶ VIỆC BẠN CẦN LÀM NGAY BÂY GIỜ:

Nếu bạn chưa kịp vào nhóm Telegram từ Trang Cảm Ơn, hãy bấm vào link dưới đây để tham gia ngay. Mọi tài liệu, Template Notion và các phiên hỏi đáp sẽ diễn ra tại đây:

👉 [LINK THAM GIA GROUP TELEGRAM]
https://t.me/+ju9HuPOviThhMmU1

Hẹn gặp bạn ở bên trong cộng đồng,

Dũng — Hệ thống 2Brain
```

### Bước 4.4 — Gắn Form vào Landing Page Antigravity

Có 2 cách:

**Cách 1: Dùng Form Widget sẵn có của Email Platform**
1. Vào hệ thống Email → Form → Publish → chọn "Embed/Script"
2. Copy đoạn `<script>` hoặc `<iframe>` được cấp
3. Trên Antigravity, kéo block **Custom HTML** vào vị trí muốn đặt form (thường đặt sau Hero hoặc sau Value Stack)
4. Paste đoạn script vào

**Cách 2: Dùng Form sẵn có của Antigravity + Webhook**
1. Tạo Form block trực tiếp trong Antigravity (Tên + Email + Nút Submit)
2. Tại phần Submit Action → chọn **"Redirect to URL"** → nhập link Thank You Page
3. Thêm webhook để đẩy data sang hệ thống Email (nếu Antigravity hỗ trợ)

---

## PHẦN 5: CÀI ĐẶT MÀU SẮC VÀ TYPOGRAPHY

### Palette màu (dùng xuyên suốt):

```
Nền chính:     #0C0C0C (rất tối)
Nền thứ cấp:   #141414
Card/Block:    #1E1E1E
Viền:          rgba(255,255,255,0.08)

Màu nhấn chính (CTA):  #F97316  (cam)
Màu nhấn phụ:          #FBBF24  (amber/vàng)
Màu Telegram:          #229ED9  (xanh dương)
Màu cảnh báo:          #EF4444  (đỏ)
Màu thành công:        #22C55E  (xanh lá)

Chữ chính:     #F5F5F0  (trắng ấm)
Chữ mờ:        rgba(245,245,240,0.6)
```

### Typography:
- **Headline lớn:** Font Oswald, weight 700
- **Body text:** Font Nunito, weight 400/600
- **Size hierarchy:** H1 = 48-58px / H2 = 36-40px / H3 = 20-24px / Body = 15-17px

---

## PHẦN 6: CÀI ĐẶT META & SEO CƠ BẢN

Trong Page Settings của cả 2 trang:

**Landing Page:**
```
Title: Cộng Đồng 2Brain — Viết Bài 15 Phút/Ngày Cho Chuyên Gia Việt
Description: Tham gia miễn phí — nhận Template Notion 2Brain, 50+ Prompt AI và cộng đồng thực chiến giúp bạn viết bài chuyên môn chỉ trong 10-15 phút/ngày.
OG Image: [Tạo ảnh 1200x630px với nền tối, text "2BRAIN COMMUNITY" màu cam]
```

**Thank You Page:**
```
Title: Đăng Ký Thành Công! — 2Brain Community
Description: Chào mừng bạn. Làm ngay bước quan trọng cuối cùng để nhận toàn bộ tài liệu.
Robots: noindex (không cần SEO cho trang này)
```

---

## PHẦN 7: CHECKLIST TRƯỚC KHI PUBLISH

### Landing Page:
- [ ] Top banner scarcity hiển thị đúng
- [ ] Hero headline đủ lớn, "2BRAIN" và số liệu màu cam
- [ ] 3 nút CTA đều link đúng: https://t.me/+ju9HuPOviThhMmU1
- [ ] Scarcity bar hiển thị đúng (72% progress)
- [ ] Value stack bundle hiển thị đầy đủ 5 items
- [ ] Urgency bonus 48h hiển thị
- [ ] FAQ accordion hoạt động (click mở/đóng)
- [ ] Test trên mobile — nút CTA đủ to (min 48px height)
- [ ] Form submit → redirect đúng Thank You Page URL

### Thank You Page:
- [ ] Nút Telegram màu xanh nổi bật nhất trang
- [ ] Link Telegram đúng: https://t.me/+ju9HuPOviThhMmU1
- [ ] Checklist 4 bước hiển thị đủ
- [ ] Share link box có nút Sao chép hoạt động
- [ ] Cập nhật link trong share box thành URL landing page thực tế

### Email Automation:
- [ ] Form kết nối với hệ thống Email
- [ ] Test submit form → nhận email trong vòng 60 giây
- [ ] Redirect sau submit → đến đúng trang /cam-on
- [ ] Email có link Telegram đúng

---

## GHI CHÚ KỸ THUẬT

1. **Cập nhật số liệu Scarcity:** Mỗi tuần vào Top Banner và Scarcity Bar để cập nhật con số thực tế (356/500 → 400/500...) để duy trì tính chân thực.

2. **Bonus 48h:** Nếu muốn tự động hóa — tạo 2 version email, version đặc biệt gửi trong 48h đầu.

3. **Pixel tracking:** Nếu có chạy Facebook Ads, thêm Facebook Pixel vào `<head>` của Landing Page trong Custom Code.

4. **A/B Test gợi ý:** Test headline "Rút Ngắn 3-4 Giờ Xuống 10-15 Phút" vs "Viết Bài Trong 15 Phút Dù Chưa Có Ý Tưởng".

---

*Tài liệu được tạo bởi 2Brain AI System — Dũng Hoàng*
