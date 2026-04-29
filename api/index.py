from fastapi import FastAPI
import sys
import os

# Thêm thư mục gốc vào path để có thể import main.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app
