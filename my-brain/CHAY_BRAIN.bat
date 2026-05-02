@echo off
d:
cd "d:\Học\Học AI\Thực Hành\my-brain"
echo Dang kiem tra thu vien he thong...
pip install -r requirements.txt
echo.
echo Dang khoi dong Second Brain Server...
python app.py
pause
