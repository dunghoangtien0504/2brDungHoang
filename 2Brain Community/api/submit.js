export default async function handler(req, res) {
  // Chỉ cho phép phương thức POST
  if (req.method !== 'POST') {
    return res.status(405).json({ message: 'Method Not Allowed' });
  }

  const { fullName, email, industry } = req.body;

  if (!fullName || !email || !industry) {
    return res.status(400).json({ message: 'Vui lòng nhập đầy đủ thông tin.' });
  }

  const API_KEY = process.env.SYSTEME_API_KEY;
  if (!API_KEY) {
    console.error("Missing SYSTEME_API_KEY environment variable");
    return res.status(500).json({ message: 'Lỗi cấu hình máy chủ (Thiếu API Key).' });
  }

  try {
    const payload = {
      email: email,
      fields: [
        {
          slug: "first_name",
          value: fullName
        },
        {
          slug: "industry", // Hãy đảm bảo slug này tồn tại trong Systeme.io Custom Fields
          value: industry
        }
      ],
      tags: [
        {
          id: 1991468 // ID Tag từ yêu cầu của User
        }
      ]
    };

    const response = await fetch('https://api.systeme.io/api/contacts', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-API-Key': API_KEY,
      },
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      const errorText = await response.text();
      console.error('Systeme.io Error:', response.status, errorText);
      return res.status(response.status).json({ message: 'Lỗi kết nối Systeme.io', details: errorText });
    }

    const data = await response.json();
    return res.status(200).json({ success: true, message: 'Thêm contact thành công!', data });
    
  } catch (error) {
    console.error('Lỗi Server Function:', error);
    return res.status(500).json({ message: 'Đã xảy ra lỗi nội bộ máy chủ.' });
  }
}
