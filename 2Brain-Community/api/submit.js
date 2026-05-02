module.exports = async (req, res) => {
  // Chỉ cho phép phương thức POST
  if (req.method !== 'POST') {
    return res.status(405).json({ message: 'Method Not Allowed' });
  }

  const { fullName, email } = req.body;

  if (!fullName || !email) {
    return res.status(400).json({ message: 'Vui lòng nhập đầy đủ tên và email.' });
  }

  const API_KEY = process.env.SYSTEME_API_KEY;
  if (!API_KEY) {
    return res.status(500).json({ message: 'Lỗi cấu hình máy chủ (Thiếu API Key).' });
  }

  try {
    const payload = {
      email: email,
      fields: [
        {
          slug: "first_name",
          value: fullName
        }
      ],
      tags: [
        {
          id: 1991468 
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

    const data = await response.json();

    if (!response.ok) {
      console.error('Systeme.io Error:', response.status, data);
      return res.status(response.status).json({ 
        message: 'Lỗi kết nối Systeme.io', 
        details: data 
      });
    }

    return res.status(200).json({ success: true, message: 'Thêm contact thành công!', data });
    
  } catch (error) {
    console.error('Lỗi Server Function:', error);
    return res.status(500).json({ message: 'Đã xảy ra lỗi nội bộ máy chủ.', error: error.message });
  }
};
