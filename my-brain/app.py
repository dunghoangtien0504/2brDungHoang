from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import sqlite3

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

ACCESS_CODE = "687568"

def check_access(request: Request):
    token = request.cookies.get("access_token")
    return token == ACCESS_CODE

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

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
    
    # Sort brain_scores by day and session order
    cursor.execute("SELECT * FROM brain_scores ORDER BY day, CASE session WHEN 'Sáng' THEN 1 WHEN 'Trưa' THEN 2 WHEN 'Tối' THEN 3 END")
    data["brain_scores"] = [dict(row) for row in cursor.fetchall()]
        
    conn.close()
    return data

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    if not check_access(request):
        return RedirectResponse(url="/login", status_code=303)
    data = get_db_data()
    return templates.TemplateResponse(
        request,
        "index.html",
        {"data": data}
    )

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
