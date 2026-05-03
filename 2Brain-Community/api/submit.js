module.exports = async (req, res) => {
  if (req.method !== 'POST') {
    return res.status(405).json({ message: 'Method Not Allowed' });
  }

  const { fullName, email, industry } = req.body;

  if (!fullName || !email) {
    return res.status(400).json({ message: 'Vui lòng nhập đầy đủ tên và email.' });
  }

  // API Key MailerLite của bạn
  const MAILERLITE_API_KEY = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI0IiwianRpIjoiMWE5OWY0YzYzZDJjMTA4ZWRkNGE4NGQxYWRiNjA3MDNmNDY1MTI1MGQ4OWEzMGZiNmQzMDdhYWU5MTU4YjcyNTY1MTVhNDBiMmYwOTg3MjYiLCJpYXQiOjE3Nzc3OTA3OTkuNDE2MjA0LCJuYmYiOjE3Nzc3OTA3OTkuNDE2MjA3LCJleHAiOjQ5MzM0NjQzOTkuMzk4MDI4LCJzdWIiOiIyMzMxNjI3Iiwic2NvcGVzIjpbXX0.Z3m1rD_X0lEBnAuHOSejbxacGEs7esePr3B8em0hMFZI1yIYmhoazzr7BtaacIKg6Zib2pLXE_kZj-FS37AmgkcLmIw7teoM_JPHIsHpAz56QHqHGvQYrHcskVO8tKoo8PpaYB7JMiXljx46VsMccHiOUY1XSCbv4exKIQRUeBEyEYaFec9JSZjDJOj0wdjAuf5gvkt6QlCH-7h7iT5xFnf4v_WGlCK49MXvMxzklbrDaML0_mUDj-mT3VA71uFgUXvf4rg_65bNmcfj9Hou4hZg7pdzSfO8kp2S16Hzf_dQxo49TCttaoAof03vWTr_GBpjrwV8hrFxMJfeE0-jdUd0LyF-sZSaZGj0tXvTVntBONu2oEz46qnuWbmjtO1ue-y8NQ-HKP7EVf7XGX1XNFHVtIsUNiElxhSKf1cleILetVBnZuQ0ZiQOkVMM4fdmUBvbuPYiEyEmuiXxdHsG_RfwyIi5JDZsdJDBNA8rJOFH9UsDgFitJvPfpBQ2L2IABFXk9RJbLSpPNkex6tMd3EbwDxNnaummN_OGiwbbg--ctHrSxMK6iLsRD_SV-pqKRk45ZnwMcH0uwN6gF7D2e26Lw41JzJU200W6VjckeiTz9_dWOONJ1IBBQQfPzlzXJiWnjVhJ91-X7lykIFEe_HQSl7BmQHe057Qwgjhsa30';
  const GROUP_ID = '186427233165903270';

  try {
    const response = await fetch('https://connect.mailerlite.com/api/subscribers', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${MAILERLITE_API_KEY}`,
      },
      body: JSON.stringify({
        email: email,
        fields: {
          name: fullName,
          industry: industry || ''
        },
        groups: [GROUP_ID]
      }),
    });

    const data = await response.json();

    if (!response.ok) {
      console.error('MailerLite Error:', response.status, data);
      return res.status(response.status).json({ message: 'Lỗi kết nối MailerLite', details: data });
    }

    return res.status(200).json({ success: true, message: 'Đã lưu thông tin vào MailerLite!', data });
    
  } catch (error) {
    console.error('Lỗi Server Function:', error);
    return res.status(500).json({ message: 'Đã xảy ra lỗi nội bộ máy chủ.', error: error.message });
  }
};
