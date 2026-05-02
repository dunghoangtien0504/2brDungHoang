from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import sqlite3

import difflib

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

ACCESS_CODE = "687568"

# --- Logic Phân tích & Tự động hóa ---
def calculate_similarity(text1, text2):
    if not text1 or not text2: return 0
    ratio = difflib.SequenceMatcher(None, text1, text2).ratio()
    return round(ratio * 10)

def analyze_differences(draft, final):
    if not draft or not final: return "Chưa có dữ liệu so sánh."
    d = difflib.Differ()
    diff = list(d.compare(draft.split(), final.split()))
    added = [word[2:] for word in diff if word.startswith('+ ')]
    removed = [word[2:] for word in diff if word.startswith('- ')]
    analysis = []
    if added: analysis.append(f"Thêm: {', '.join(added[:3])}")
    if removed: analysis.append(f"Bớt: {', '.join(removed[:3])}")
    if draft.count('\n') != final.count('\n'): analysis.append("Đổi ngắt dòng")
    return " | ".join(analysis)

def check_access(request: Request):
    token = request.cookies.get("access_token")
    return token == ACCESS_CODE

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    try:
        return templates.TemplateResponse(request=request, name="login.html", context={})
    except Exception as e:
        print(f"--- LOI TRANG LOGIN ---: {e}")
        import traceback
        traceback.print_exc()
        return HTMLResponse(content=f"<h1>Lỗi trang Login</h1><p>{e}</p>", status_code=500)

@app.post("/login")
async def login(code: str = Form(...)):
    if code == ACCESS_CODE:
        response = RedirectResponse(url="/", status_code=303)
        response.set_cookie(key="access_token", value=ACCESS_CODE, httponly=True, max_age=2592000) # 30 days
        return response
    return RedirectResponse(url="/login?error=1", status_code=303)

def get_db_data():
    conn = sqlite3.connect("brain.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    data = {}
    for table in ["knowledge", "business", "brand_voice"]:
        cursor.execute(f"SELECT * FROM {table}")
        data[table] = [dict(row) for row in cursor.fetchall()]
    
    # Brain Scores
    cursor.execute("SELECT * FROM brain_scores ORDER BY day, CASE session WHEN 'Sáng' THEN 1 WHEN 'Trưa' THEN 2 WHEN 'Tối' THEN 3 END")
    data["brain_scores"] = [dict(row) for row in cursor.fetchall()]
    
    # Articles
    cursor.execute("SELECT * FROM articles ORDER BY day DESC, session")
    data["articles"] = [dict(row) for row in cursor.fetchall()]
        
    conn.close()
    return data

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    if not check_access(request):
        return RedirectResponse(url="/login", status_code=303)
    try:
        data = get_db_data()
        return templates.TemplateResponse(
            request=request, name="index.html", context={"data": data}
        )
    except Exception as e:
        print(f"--- LOI HE THONG ---: {e}")
        import traceback
        traceback.print_exc()
        return HTMLResponse(content=f"<h1>Lỗi hệ thống</h1><p>{e}</p>", status_code=500)

@app.post("/update_score")
async def update_score(
    request: Request,
    day: int = Form(...),
    session: str = Form(...),
    post_time: str = Form(None),
    similarity_score: int = Form(None),
    viewer_feedback: str = Form(""),
    brand_voice_addition: str = Form(""),
    short_comment: str = Form("")
):
    if not check_access(request):
        return RedirectResponse(url="/login", status_code=303)
    conn = sqlite3.connect("brain.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE brain_scores 
        SET post_time = ?, similarity_score = ?, viewer_feedback = ?, brand_voice_addition = ?, short_comment = ?
        WHERE day = ? AND session = ?
    """, (post_time, similarity_score, viewer_feedback, brand_voice_addition, short_comment, day, session))
    conn.commit()
    conn.close()
    return RedirectResponse(url="/#brain-score", status_code=303)

@app.post("/save_article")
async def save_article(
    request: Request,
    day: int = Form(...),
    session: str = Form(...),
    draft_a: str = Form(""),
    final_b: str = Form("")
):
    if not check_access(request):
        return RedirectResponse(url="/login", status_code=303)
    
    conn = sqlite3.connect("brain.db")
    cursor = conn.cursor()
    
    # Lưu hoặc cập nhật bài viết
    cursor.execute("SELECT id FROM articles WHERE day = ? AND session = ?", (day, session))
    existing = cursor.fetchone()
    
    if existing:
        cursor.execute("UPDATE articles SET draft_a = ?, final_b = ? WHERE id = ?", (draft_a, final_b, existing[0]))
    else:
        cursor.execute("INSERT INTO articles (day, session, draft_a, final_b) VALUES (?, ?, ?, ?)", (day, session, draft_a, final_b))
    
    # --- AUTOMATION: Tự động chấm điểm & Phân tích ---
    score = calculate_similarity(draft_a, final_b)
    analysis = analyze_differences(draft_a, final_b)
    
    cursor.execute("""
        UPDATE brain_scores 
        SET similarity_score = ?, short_comment = ?
        WHERE day = ? AND session = ?
    """, (score, analysis, day, session))
    
    conn.commit()
    conn.close()
    return RedirectResponse(url="/#articles", status_code=303)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
