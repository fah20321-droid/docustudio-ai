from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

BASE = Path(__file__).resolve().parent
app = FastAPI(title="DocuStudio AI")
app.mount("/static", StaticFiles(directory=BASE / "static"), name="static")
templates = Jinja2Templates(directory=BASE / "templates")
projects = [{"id": 1, "title": "مشروعي الأول", "description": "مشروع تجريبي لاستكشاف DocuStudio AI", "scenes": []}]

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "projects": projects})

@app.post("/projects")
async def create_project(title: str = Form(...), description: str = Form("")):
    projects.append({"id": len(projects) + 1, "title": title, "description": description, "scenes": []})
    return RedirectResponse("/", status_code=303)

@app.get("/health")
async def health():
    return {"status": "ok"}
